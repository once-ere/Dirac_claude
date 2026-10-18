## 6. Spinors in curved 4+4 space: vielbein, spin connection and $\gamma^\mu\Omega_\mu$

The two fields of the author, dirac16complex and dirac16complex00, have sixteen components at every point of spacetime. Chapters 4 and 5 built the eight gamma matrices that act on these components and the groups Pin(4,4) and Spin(4,4) that turn them. All of that was done in flat 4+4 space, where the eight directions are the same at every point. The author's universe is not flat: 3-space inflates, while the hidden direction and the three extra times deflate exponentially together (Chapter 3). This chapter teaches, from zero, how a field with sixteen components is differentiated in such a curved space, and it computes exactly what gravity puts into the field equations of the author's two fields through the canonical spin connection, for the corrected metric of 2026-10-16. The answer is one $16 \times 16$ matrix,

$$
\gamma^\mu\Omega_\mu = \tfrac32 H e^{a_4}b_4^{-1/2}\,\gamma^{(x0)} + \Big(\frac{b_4'}{b_4} - \frac{a_4'}{2}\Big)\gamma^{(x4)} ,
$$

which is $\frac32He^{Hx_4/3}\gamma^{(x0)} + \frac56H\gamma^{(x4)}$ on the history of the Revision record, and the chapter also proves precisely what this matrix does and does not mean.

### 6.1 What this chapter does

**The problem in plain words.** A spinor field $\Psi$ is a list of sixteen numbers at every point. The numbers are not measured in the coordinates $x_0, \dots, x_7$ directly: they are measured with respect to eight perpendicular unit directions chosen at each point, a **frame**. In flat space one frame serves everywhere. In a curved space the frame of one point and the frame of a neighbouring point are turned with respect to each other, so the plain derivative $\partial_\mu\Psi$ mixes two things: how the field really changes, and how the frame turns. The **spin connection** measures how the frame turns, and the **covariant derivative** $D_\mu\Psi = \partial_\mu\Psi + \Omega_\mu\Psi$ removes the turning. The field equation of both fields (Chapter 7 derives it) is

$$
\sum_\mu \gamma^\mu D_\mu\Psi = \big(m + U'(S)\big)\Psi ,
$$

and the spin connection enters it only through the one matrix $\sum_\mu\gamma^\mu\Omega_\mu$. The author asked that the field equations "always possess non-zero contributions from gravity (through the canonical spin-connection, unless we are in flat 4+4 spacetime)" (quoted from `Revision/README.md`). This chapter computes the matrix exactly and examines the request line by line.

**What the chapter proves.**

- The corrected metric, with its two functions $a_4(x_4)$ and $b_4(x_4) > 0$, has a diagonal vielbein (Section 6.2), 21 independent nonzero Christoffel symbols (Section 6.3) and a canonical spin connection with 10 independent nonzero components (Sections 6.4 to 6.6).
- The spinor connection $\Omega_\mu$ makes the curved gammas covariantly constant (Section 6.7), and in the diagonal vielbein $\sum_\mu\gamma^\mu\Omega_\mu = c_g\gamma^{(x0)} + v_g\gamma^{(x4)}$ with $c_g = \frac32He^{a_4}b_4^{-1/2}$ and $v_g = b_4'/b_4 - a_4'/2$, for every $H > 0$ and all functions $a_4$ and $b_4 > 0$ (Sections 6.8 and 6.9). The term along the time is half the rate at which the proper 7-volume of a slice of constant time grows; 3-space contributes $+\frac32a_4'$ to it and the four directions of the hidden block (the hidden direction and the three extra times, which shrink together) contribute $-2a_4' + b_4'/b_4$. The term along the hidden direction comes from the warp of the three extra times alone. On the history of the Revision record the matrix is $\frac32He^{Hx_4/3}\gamma^{(x0)} + \frac56H\gamma^{(x4)}$.
- This matrix sends a nonzero field to zero only where $c_g = \pm v_g$; on the history of the record this happens at one single time, $x_4 = 3\ln(5/9)/H \approx -1.7634/H$, before the first state of the record's history (Section 6.10).
- A **negative control**: if the hidden block grew like 3-space instead of shrinking, the coefficient of $a_4'$ along the time would be $+\frac72$ instead of $-\frac12$; the term sees in which direction the hidden block changes (Section 6.10).
- The value of $\gamma^\mu\Omega_\mu$ belongs to the chosen frame: in a frame boosted in the plane of $x4$ and $x0$ with the rapidity $b(x_4)$ the contraction is $(c_g - \frac{b'}{2})(\cosh b\,\gamma^{(x0)} - \sinh b\,\gamma^{(x4)}) + v_g(\cosh b\,\gamma^{(x4)} - \sinh b\,\gamma^{(x0)})$, whose first part vanishes for $b' = 2c_g$ while the part $v_g$ remains in every such frame (Sections 6.15 and 6.16), and a rescaling of the field removes it all (Section 6.18). What no frame and no rescaling can remove is the curvature: the Riemann tensor of the corrected metric consists of the curvatures of the 28 coordinate planes, it does not vanish on the history of the record, and it vanishes only for special functions $a_4$ and $b_4$, such as $a_4 = 0$, $b_4 = H^2x_4^2$ (Section 6.17).
- Why the record contracts the spin connection with both frame indices down: the author's notebook contracts the mixed components, which lacks a metric factor; that contraction deletes all 16 boost parts of the connection and would give $\frac32(a_4' - \frac{b_4'}{2b_4})\gamma^{(x4)}$ with no term $\gamma^{(x0)}$ at all (Sections 6.23 and 6.24).

**The three worked examples.** Each is a complete Jupyter notebook; the chapter places each one where its theory has been explained, gives the complete instructions to run it, prints its complete text and then explains every line of its code.

| notebook | what it computes | figures | checks |
| --- | --- | --- | --- |
| 06a | vielbein, Christoffel symbols, spin connection, $\Omega_\mu$, the contraction $\gamma^\mu\Omega_\mu$ direction by direction, the divergence form, the Dirac operator, the negative control, a warm-up in the plane | 10 | 40 |
| 06b | a boosted frame, local spin covariance, the Riemann and Ricci tensors, the flat member, the spinor curvature, the rescaling | 6 | 29 |
| 06c | the mixed contraction of the author's notebook and what the missing metric factor changes | 6 | 28 |

All three reproduce the Revision record where they overlap with it; every such check prints a second line that names the record file and its check. Their last lines are ALL 40 CHECKS PASSED (notebook 06a), ALL 29 CHECKS PASSED (notebook 06b) and ALL 28 CHECKS PASSED (notebook 06c).

**Statuses.** Every statement carries one of the five labels of Chapter 0. **PROVED**: derived exactly here, line by line, and confirmed by an exact check of a notebook; where the Revision record proves the same, the record file and its check are named. **COMPUTED**: a number obtained by a notebook, with its accuracy. **ASSUMED**: the corrected metric itself (the input of the theory), two standard theorems that are quoted and named where they are used, and the histories used only in some plots, sample points and evaluations: the prescribed background of Chapter 3, $a_4 = AHx_4$ with $b_4 = b_4(0)\,e^{4AHx_4/3}$, $A = 1$ and $b_4(0) = 1$ (and $H = 1$ in the pictures), and in one plot the illustrative $b_4 = e^{4x_4/3}(1 + \frac12\sin x_4)$. No HYPOTHESIS enters this chapter. One point is OPEN here: the boundary condition at the fold, which the antisymmetry of the hidden-direction operator needs (Section 6.24); Chapter 14 treats the conditions at the fold, which are ASSUMED there. Nothing in this chapter concerns pairs of universes, their creation, or matter and antimatter; Chapters 18 to 21 treat those questions and state exactly what is and what is not proved about them.

**Notation.** The eight directions are named $x0, \dots, x7$ as in Chapter 5: $x0$ is the hidden direction (space-like), $x1, x2, x3$ are 3-space (inflating), $x4$ is the time, $x5, x6, x7$ are the three extra times (time-like, deflating exponentially). Inside formulas the coordinate values are written $x_0, \dots, x_7$, for example $z = 6Hx_0$. The angle $z$ takes every real value; as in Chapter 3, Section 3.5, a **cell** is $0 < z < \pi$, the **fold** $\cos z = 0$ ($z = \pi/2$) joins its two **halves**, the **tips** $\sin z = 0$ are its ends, and every formula of this chapter holds at every point with $\sin z\cos z \neq 0$ (between the degenerate points). The letter $i$ stands for one of the 3-space directions $x1, x2, x3$ and the letter $t$ for one of the extra times $x5, x6, x7$ (except in the polar plane, where $i$ is the imaginary unit, and in Sections 6.16 and 6.23, where $t$ is a component or a coordinate). The functions $a_4$ and $b_4 > 0$ depend on $x_4$ only; $a_4' = da_4/dx_4$, $a_4'' = d^2a_4/dx_4^2$, and the same for $b_4$. Three abbreviations are used throughout, the same as in the notebooks and in the record:

$$
s_b = e^{-a_4}b_4^{1/2}, \qquad h_4 = \partial_4\ln s_b = \frac{b_4'}{2b_4} - a_4', \qquad W = (\sin^2 z)^{1/12} = \lvert\sin z\rvert^{1/6} .
$$

$s_b$ is the **hidden scale**, the factor that the hidden direction and the three extra times share; Chapter 3 writes it $f$, but in this chapter the letter $f$ is needed for the vielbein factors. $h_4$ is its rate, which Chapter 3 calls $\alpha_t$ (it is not the scale factor $h_4 = 1$ of the time in Chapter 3, Section 3.7); $a_4'$ is the rate of 3-space. $W$ is the **warp factor** of the three extra times. On the history of the Revision record, $a_4 = AHx_4$ and $b_4 = b_4(0)\,e^{\beta AHx_4}$ with $A = 1$, $\beta = 4/3$ and $b_4(0) = 1$ (Chapter 3, Section 3.8), these are $s_b = e^{-Hx_4/3}$ and $h_4 = -H/3$: the hidden block shrinks at one third of the rate at which 3-space grows. Every formula of this chapter holds for every $a_4$ and $b_4$ unless it says otherwise. The frame metric is

$$
\eta = \mathrm{diag}(+1, +1, +1, +1, -1, -1, -1, -1)
$$

in the order $x0, \dots, x7$; $\eta_{aa}$ is its entry for the direction $a$, and $\eta^{aa} = \eta_{aa}$ because every entry is $\pm 1$. The constant gamma matrix of a direction carries the direction in parentheses, $\gamma^{(x4)}$; a gamma without parentheses, $\gamma^{x4}$ or $\gamma^\mu$, is a **curved gamma** (Section 6.2). Sums are written with $\sum$ as in Chapter 3. The one exception is the contraction $\gamma^\mu\Omega_\mu$: it always means $\sum_\mu\gamma^\mu\Omega_\mu$, and a single term is marked "(no sum)". Finally $c_g = \frac32He^{a_4}b_4^{-1/2}$ and $v_g = b_4'/b_4 - a_4'/2$ denote the two coefficients of the result (the letter g for gravity).

**The record files.** The Revision record files are named by their short names. The formula file `field-theory.json` (the formulas of the field theory for the corrected metric of 2026-10-16) lies in the folder `Revision/theory`. The reports `python-field-theory.json` and `wolfram-field-theory.json` (written by a sympy program and by a WolframScript program that share no code) and the two scope reports `python-scope.json` and `wolfram-scope.json`, all for the corrected metric with general $a_4$ and $b_4$ and every real $z$, lie in the folder `Revision/theory/reports`. The record `parameters.json` of the Revision Kohn-Sham work, which holds the history, lies in the folder `Revision/kohn_sham/results`. The **lead report** is the file `emt-divergence-and-spin-connection.json` in the folder `Revision/lead_checks/reports`, written by an independent program of the lead of the Revision work for the corrected metric. The curvature record `curvature.json` and its report `python-lovelock-report.json` lie in the folder `Revision/gkd_lovelock/results`.

**A dated note.** An earlier version of this chapter computed the same quantities for the metric of 2026-10-14, withdrawn on 2026-10-16. Where a comparison teaches something, it is given as dated history and marked so; it is never current physics.

### 6.2 A frame at every point: the vielbein

**Why a spinor needs a frame.** The gamma matrices obey the Clifford relation $\gamma^a\gamma^b + \gamma^b\gamma^a = 2\eta^{ab}1$ with the constant matrix $\eta$ (Chapter 4). In a curved space the metric $g_{\mu\nu}(x)$ changes from point to point and is not $\eta$. The way out is to describe every point by its own eight reference directions, perpendicular to each other and of unit length (unit duration for a time-like direction). Measured in such a frame the metric looks exactly like $\eta$, so the constant gammas of Chapter 4 can be used unchanged. The spinor components are always measured with respect to such a frame.

**Definition (vielbein).** A **vielbein** (German for "many legs") is an $8 \times 8$ matrix $e^a{}_\mu(x)$ at every point with

$$
g_{\mu\nu} = \sum_{a} \eta_{aa}\, e^a{}_\mu\, e^a{}_\nu \qquad \text{for all } \mu, \nu .
$$

The upper index $a$ is a **frame index**: it numbers the eight frame directions. The lower index $\mu$ is a **coordinate index**: it numbers the coordinates. Row $a$ of the matrix holds the components of the frame direction $a$ in the sense that a small coordinate step $dx^\mu$ has the frame components $dX^a = \sum_\mu e^a{}_\mu dx^\mu$, and then $ds^2 = \sum_{\mu,\nu} g_{\mu\nu}dx^\mu dx^\nu = \sum_a \eta_{aa}(dX^a)^2$: lengths in frame components are computed with $\eta$. The **inverse vielbein** $e_a{}^\mu$ is the inverse matrix, $\sum_\mu e^a{}_\mu e_b{}^\mu = \delta^a_b$ (1 when $a = b$, 0 otherwise).

**The diagonal vielbein of the corrected metric.** The corrected metric (Chapter 3, Section 3.5) is diagonal,

$$
g = \mathrm{diag}\big(e^{-2a_4}b_4\cot^2 z,\ e^{2a_4}\ (\times3),\ -1,\ -e^{-2a_4}b_4W^2\ (\times3)\big), \qquad z = 6Hx_0 ,
$$

with $W^2 = (\sin^2 z)^{1/6}$ (each entry marked $(\times3)$ appears three times, for $x1, x2, x3$ and for $x5, x6, x7$), so $g_{\mu\mu} = \eta_{\mu\mu}f_\mu^2$ with the **vielbein factors** (Chapter 3 calls their absolute values the scale factors)

$$
f = \big(s_b\cot z,\ e^{a_4},\ e^{a_4},\ e^{a_4},\ 1,\ s_bW,\ s_bW,\ s_bW\big), \qquad s_b = e^{-a_4}b_4^{1/2} .
$$

The diagonal matrix $e^a{}_\mu = f_a\,\delta^a_\mu$ is a vielbein: in the sum $\sum_a \eta_{aa}e^a{}_\mu e^a{}_\nu$ only $a = \mu = \nu$ survives, which gives $\eta_{\mu\mu}f_\mu^2 = g_{\mu\mu}$. For example, for $\mu = \nu = x1$,

$$
\eta_{11}f_1^2 = (+1)\big(e^{a_4}\big)^2 = e^{2a_4}
$$

(a power of a power multiplies the exponents), which is $g_{11}$; for $\mu = \nu = x5$,

$$
\eta_{55}f_5^2 = (-1)\big(e^{-a_4}b_4^{1/2}W\big)^2 = -e^{-2a_4}b_4W^2
$$

(a power of a product is the product of the powers; $(b_4^{1/2})^2 = b_4$), which is $g_{55}$; and for $x0$, $(+1)(s_b\cot z)^2 = e^{-2a_4}b_4\cot^2 z = g_{00}$. The factor $f_0 = s_b\cot z$ keeps the sign of $\cot z$, as in the record: only its square enters the metric, and with the sign the factor changes smoothly through the fold, where it vanishes. At the fold ($\cos z = 0$) $f_0 = 0$, and at the tips ($\sin z = 0$) $f_0$ grows without bound and $W = 0$: there the vielbein is not invertible, and nothing in this chapter is computed there. The inverse vielbein is diagonal too, $e_a{}^\mu = \delta_a^\mu/f_a$. PROVED; `field-theory.json`, formulas `metric` and `vielbein_diagonal`; `wolfram-field-theory.json`, check `metric_is_the_corrected_metric`; `python-field-theory.json`, check `metric_from_vielbein_equals_SPEC`; the lead report, check `vielbein_reproduces_metric`; Notebook 06a, In [7].

**The volume factor.** The determinant of a diagonal matrix is the product of its diagonal entries, so $\det g = \prod_\mu \eta_{\mu\mu}f_\mu^2 = (+1)^4(-1)^4\prod_\mu f_\mu^2$, and $\sqrt{\lvert\det g\rvert} = \lvert f_0 f_1\cdots f_7\rvert$. Line by line:

$$
f_1f_2f_3 = e^{3a_4}, \qquad f_5f_6f_7 = s_b^3W^3 = e^{-3a_4}b_4^{3/2}W^3
$$

(three equal factors; $e^{a_4}e^{a_4}e^{a_4} = e^{3a_4}$ and $(e^{-a_4}b_4^{1/2})^3 = e^{-3a_4}b_4^{3/2}$),

$$
f_1f_2f_3\,f_4\,f_5f_6f_7 = e^{3a_4}\cdot 1\cdot e^{-3a_4}b_4^{3/2}W^3 = b_4^{3/2}W^3
$$

(the exponentials cancel, $e^{u}e^{-u} = 1$),

$$
f_0f_1\cdots f_7 = e^{-a_4}b_4^{1/2}\cot z\cdot b_4^{3/2}W^3 = e^{-a_4}b_4^2\cot z\,W^3
$$

(multiply by $f_0$; $b_4^{1/2}b_4^{3/2} = b_4^2$), and with $W^3 = (\sin^2 z)^{1/4}$

$$
\sqrt{\lvert\det g\rvert} = e^{-a_4}b_4^2\,\lvert\cot z\rvert\,(\sin^2 z)^{1/4} = G\,f_0f_1\cdots f_7, \qquad G = \mathrm{sign}(\cot z) .
$$

$G$ is $+1$ on the first half of a cell and $-1$ on the second; it is constant between the degenerate points, so it disappears from every derivative of $\ln\sqrt{\lvert g\rvert}$. The record writes the same formula with the symbol `rftSig` for $G$. **The function $a_4$ does not drop out of the volume factor**: the factor $e^{3a_4}$ of the inflating 3-space and the factor $e^{-3a_4}$ of the deflating extra times cancel, but the factor $e^{-a_4}$ of the hidden direction is left over, because the hidden direction shrinks together with the extra times. The proper 7-volume of a slice of constant time (Chapter 3, Section 3.6) has the volume factor $\sqrt{\lvert\det g\rvert}$ (the time factor is $f_4 = 1$), and its rate of growth is

$$
\partial_4\ln\sqrt{\lvert\det g\rvert} = \partial_4\big(-a_4 + 2\ln b_4\big) = -a_4' + \frac{2b_4'}{b_4}
$$

(the logarithm of a product is the sum of the logarithms; the factor with $z$ does not depend on $x_4$; the derivative of $\ln b_4$ is $b_4'/b_4$), which is $-H + \frac83H = \frac53H$ on the history of the record. PROVED; `field-theory.json`, formula `sqrt_det_g`; `wolfram-field-theory.json` and `python-field-theory.json`, check `sqrt_det_g`; Notebook 06a, In [7]. Half of this rate will reappear in Section 6.9 as the term $v_g$.

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
\gamma^{x0} = e^{a_4}b_4^{-1/2}\tan z\,\gamma^{(x0)},\qquad \gamma^{x_i} = e^{-a_4}\gamma^{(x_i)},\qquad \gamma^{x4} = \gamma^{(x4)},\qquad \gamma^{x_t} = e^{a_4}b_4^{-1/2}W^{-1}\gamma^{(x_t)} ,
$$

with $i = 1, 2, 3$, $t = 5, 6, 7$, $1/s_b = e^{a_4}b_4^{-1/2}$ and $1/\cot z = \tan z$.

**A vielbein is a choice.** Let $\Lambda(x)$ be an $8 \times 8$ matrix at every point with $\Lambda^T\eta\Lambda = \eta$ (an element of O(4,4), Chapter 5). Then $e'^a{}_\mu = \sum_c \Lambda^a{}_c\,e^c{}_\mu$ is another vielbein of the same metric. Line by line, in matrix form ($g = e^T\eta e$ is the definition written with matrices, $e$ having rows $a$ and columns $\mu$):

$$
e'^T\eta\,e' = (\Lambda e)^T\eta(\Lambda e) = e^T\big(\Lambda^T\eta\Lambda\big)e = e^T\eta\,e = g
$$

(the transpose of a product is the product of the transposes in reverse order; then the defining property of $\Lambda$). Such a point-dependent turning of the frame is a **local frame rotation** (a rotation, or a boost when it mixes a space-like with a time-like direction; Chapter 5). The diagonal vielbein is the simplest choice for the corrected metric, but it is one choice among infinitely many. Sections 6.15 and 6.16 show that this freedom matters.

| statement | status | where it is verified |
| --- | --- | --- |
| $e^a{}_\mu = f_a\delta^a_\mu$ reproduces the corrected metric | PROVED | `field-theory.json`, formulas `metric` and `vielbein_diagonal`; `wolfram-field-theory.json`, check `metric_is_the_corrected_metric`; `python-field-theory.json`, check `metric_from_vielbein_equals_SPEC`; lead report, check `vielbein_reproduces_metric` |
| $\sqrt{\lvert\det g\rvert} = e^{-a_4}b_4^2\lvert\cot z\rvert(\sin^2 z)^{1/4}$; the 7-volume grows at the rate $-a_4' + 2b_4'/b_4$ | PROVED | `field-theory.json`, formula `sqrt_det_g`; `wolfram-field-theory.json` and `python-field-theory.json`, check `sqrt_det_g` |
| curved Clifford relation; another frame $\Lambda e$ gives the same metric | PROVED (above) | Notebook 06b checks the second for a boost, In [7] |

### 6.3 The Christoffel symbols of the corrected metric

**What they are.** Chapter 3 introduced the **Christoffel symbols**, the numbers that say how the coordinate directions change from point to point:

$$
\Gamma^\lambda{}_{\mu\nu} = \tfrac12\sum_\rho g^{\lambda\rho}\big(\partial_\mu g_{\rho\nu} + \partial_\nu g_{\rho\mu} - \partial_\rho g_{\mu\nu}\big) .
$$

They are symmetric in the two lower indices, $\Gamma^\lambda{}_{\mu\nu} = \Gamma^\lambda{}_{\nu\mu}$ (exchange $\mu$ and $\nu$: the first two terms exchange places and the third is unchanged because $g$ is symmetric). They enter the **coordinate covariant derivative** of a vector field, $\nabla_\mu V^\nu = \partial_\mu V^\nu + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}V^\lambda$, the derivative that compares the vector at two points correctly although the coordinate directions change between them.

**A diagonal metric.** When $g$ is diagonal, so is its inverse, $g^{\lambda\rho} = \delta^{\lambda\rho}/g_{\lambda\lambda}$, and only $\rho = \lambda$ survives in the sum. With $g_{\lambda\lambda} = \eta_{\lambda\lambda}f_\lambda^2$ there are four cases, each derived from the formula with $\rho = \lambda$ (no sums below).

(a) All three indices equal, $\lambda = \mu = \nu$:

$$
\Gamma^\lambda{}_{\lambda\lambda} = \frac{1}{2g_{\lambda\lambda}}\big(\partial_\lambda g_{\lambda\lambda} + \partial_\lambda g_{\lambda\lambda} - \partial_\lambda g_{\lambda\lambda}\big) = \frac{\partial_\lambda g_{\lambda\lambda}}{2g_{\lambda\lambda}} = \frac{2\eta_{\lambda\lambda}f_\lambda\partial_\lambda f_\lambda}{2\eta_{\lambda\lambda}f_\lambda^2} = \frac{\partial_\lambda f_\lambda}{f_\lambda}
$$

(two of the three terms cancel; the derivative of $f^2$ is $2f\,\partial f$). We write $\partial f/f = \partial\ln\lvert f\rvert$; for a positive factor this is $\partial\ln f$, and for the factor $f_0 = s_b\cot z$, which may be negative, the same holds with the absolute value, because the derivative of $\ln\lvert u\rvert$ is $u'/u$ for both signs of $u$.

(b) The upper index equals one lower index, $\lambda = \mu \neq \nu$:

$$
\Gamma^\lambda{}_{\lambda\nu} = \frac{1}{2g_{\lambda\lambda}}\big(\partial_\lambda g_{\lambda\nu} + \partial_\nu g_{\lambda\lambda} - \partial_\lambda g_{\lambda\nu}\big) = \frac{\partial_\nu g_{\lambda\lambda}}{2g_{\lambda\lambda}} = \frac{\partial_\nu f_\lambda}{f_\lambda}
$$

($g_{\lambda\nu} = 0$ for $\lambda \neq \nu$; then the same steps as in (a)).

(c) The two lower indices equal, the upper one different, $\mu = \nu \neq \lambda$:

$$
\Gamma^\lambda{}_{\mu\mu} = \frac{1}{2g_{\lambda\lambda}}\big(0 + 0 - \partial_\lambda g_{\mu\mu}\big) = -\frac{\eta_{\mu\mu}\,2f_\mu\partial_\lambda f_\mu}{2\eta_{\lambda\lambda}f_\lambda^2} = -\eta_{\lambda\lambda}\eta_{\mu\mu}\,\frac{f_\mu\,\partial_\lambda f_\mu}{f_\lambda^2}
$$

(the off-diagonal entries $g_{\lambda\mu}$ vanish; $1/\eta_{\lambda\lambda} = \eta_{\lambda\lambda}$ because $\eta_{\lambda\lambda} = \pm1$).

(d) All three different: every term contains an off-diagonal entry of $g$, so $\Gamma^\lambda{}_{\mu\nu} = 0$.

**The derivatives of the factors.** The corrected metric depends on $x_0$ (through $z = 6Hx_0$) and on $x_4$ (through $a_4$ and $b_4$) only, so only $\partial_0$ and $\partial_4$ of the factors can be nonzero. The logarithms are

$$
\ln\lvert f_0\rvert = -a_4 + \tfrac12\ln b_4 + \ln\lvert\cot z\rvert, \qquad \ln f_i = a_4, \qquad \ln f_4 = 0, \qquad \ln f_t = -a_4 + \tfrac12\ln b_4 + \tfrac1{12}\ln\sin^2 z
$$

(the logarithm of a product is the sum of the logarithms; $\ln b_4^{1/2} = \frac12\ln b_4$ and $\ln W = \frac1{12}\ln\sin^2 z$). Differentiating by $x_4$:

$$
\partial_4\ln\lvert f_0\rvert = \partial_4\ln f_t = -a_4' + \frac{b_4'}{2b_4} = h_4, \qquad \partial_4\ln f_i = a_4'
$$

(only $\pm a_4$ and $\frac12\ln b_4$ depend on $x_4$; their derivatives are $\pm a_4'$ and $\frac12 b_4'/b_4$). Differentiating by $x_0$:

$$
\partial_0\ln f_t = \frac1{12}\cdot\frac{2\sin z\cos z}{\sin^2 z}\cdot 6H = H\cot z, \qquad \partial_0\ln f_i = 0
$$

(the chain rule: the derivative of $\ln\sin^2 z$ with respect to $z$ is $2\sin z\cos z/\sin^2 z$, and $dz/dx_0 = 6H$; 3-space has no warp factor, so $f_i$ does not depend on $x_0$),

$$
\partial_0\ln\lvert f_0\rvert = 6H\,\frac{-1/\sin^2 z}{\cot z} = -\frac{6H}{\sin z\cos z} = -\frac{12H}{\sin 2z}
$$

(the chain rule; the derivative of $\cot z$ is $-1/\sin^2 z$; $\cot z = \cos z/\sin z$; the double-angle formula $\sin 2z = 2\sin z\cos z$).

**The 21 symbols.** Insert these into the four cases. Case (a) gives one symbol, for $\lambda = x0$:

$$
\Gamma^{x0}{}_{x0\,x0} = -\frac{12H}{\sin 2z} = -\frac{12H}{\sin(12Hx_0)} .
$$

Case (b) gives, with $\nu = x4$ or $\nu = x0$,

$$
\Gamma^{x0}{}_{x0\,x4} = h_4,\qquad \Gamma^{x_i}{}_{x_i\,x4} = a_4',\qquad \Gamma^{x_t}{}_{x_t\,x4} = h_4,\qquad \Gamma^{x_t}{}_{x_t\,x0} = H\cot z ,
$$

and nothing for $\lambda = x4$ ($f_4 = 1$) or for $\Gamma^{x_i}{}_{x_i\,x0}$ ($\partial_0 f_i = 0$). Case (c) with $\lambda = x4$ ($\eta_{44} = -1$, $f_4 = 1$) gives $\Gamma^{x4}{}_{\mu\mu} = \eta_{\mu\mu}f_\mu\partial_4 f_\mu = \eta_{\mu\mu}f_\mu^2\,\partial_4\ln\lvert f_\mu\rvert$, that is

$$
\Gamma^{x4}{}_{x0\,x0} = e^{-2a_4}b_4\cot^2 z\;h_4,\qquad \Gamma^{x4}{}_{x_i\,x_i} = e^{2a_4}a_4', \qquad \Gamma^{x4}{}_{x_t\,x_t} = -e^{-2a_4}b_4W^2\,h_4
$$

($f_0^2 = e^{-2a_4}b_4\cot^2 z$, $f_i^2 = e^{2a_4}$, $f_t^2 = e^{-2a_4}b_4W^2$; $\eta_{tt} = -1$ gives the sign of the last one). Case (c) with $\lambda = x0$ ($\eta_{00} = +1$) needs $\partial_0 f_\mu \neq 0$, which only the extra times have:

$$
\Gamma^{x0}{}_{x_t\,x_t} = -(+1)(-1)\frac{f_t\,\partial_0 f_t}{f_0^2} = \frac{f_t^2\,H\cot z}{s_b^2\cot^2 z} = \frac{s_b^2W^2\,H\cot z}{s_b^2\cot^2 z} = HW^2\tan z
$$

($\partial_0 f_t = H\cot z\,f_t$; $s_b^2$ cancels; $\cot z/\cot^2 z = \tan z$). Every other symbol vanishes. Counting with $\mu \le \nu$: $\Gamma^{x0}{}_{x0x0}$, $\Gamma^{x0}{}_{x0x4}$ and $\Gamma^{x4}{}_{x0x0}$ once each, and three each of the six families $\Gamma^{x_i}{}_{x_ix4}$, $\Gamma^{x_t}{}_{x_tx4}$, $\Gamma^{x_t}{}_{x0x_t}$, $\Gamma^{x4}{}_{x_ix_i}$, $\Gamma^{x4}{}_{x_tx_t}$, $\Gamma^{x0}{}_{x_tx_t}$: $3 + 6 \cdot 3 = 21$. Every nonzero symbol carries an index $x0$ or $x4$, and the 3-space directions meet only the time. In words: moving forward in time a 3-space direction grows at the rate $a_4'$ ($\Gamma^{x1}{}_{x1x4} = a_4'$), while the hidden direction and an extra time change at the common rate $h_4$ ($\Gamma^{x0}{}_{x0x4} = \Gamma^{x5}{}_{x4x5} = h_4$): on the history of the record, $h_4 = -H/3$, they shrink at one third of the rate at which 3-space grows. Moving along the hidden direction only the extra times change ($\Gamma^{x5}{}_{x0x5} = H\cot z$, the warp). Chapter 3, Section 3.23, derives the same 21 symbols.

| statement | status | where it is verified |
| --- | --- | --- |
| the 21 independent nonzero Christoffel symbols above | PROVED | `field-theory.json`, formula `christoffel_nonzero`; `wolfram-field-theory.json`, check `christoffel_count`; `python-field-theory.json`, check `christoffel_symmetric_metric_compatible`; Notebook 06a, In [9] |

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

**But the plane is flat, and the connection can be removed.** The **curvature of the spinor connection** is $F_{r\varphi} = \partial_r\Omega_\varphi - \partial_\varphi\Omega_r + \Omega_r\Omega_\varphi - \Omega_\varphi\Omega_r$; here $\Omega_\varphi$ is constant and $\Omega_r = 0$, so every term vanishes: $F_{r\varphi} = 0$. And with the spinor rotation $U(\varphi) = \cos\frac\varphi2 + i\sin\frac\varphi2\,\sigma_3$ (Chapter 5: a rotation by the angle $\varphi$ acts on spinors through the half angle),

$$
\partial_\varphi U = -\tfrac12\sin\tfrac\varphi2 + \tfrac i2\cos\tfrac\varphi2\,\sigma_3 = \tfrac i2\sigma_3\Big(\cos\tfrac\varphi2 + i\sin\tfrac\varphi2\,\sigma_3\Big) = \tfrac i2\sigma_3\,U
$$

(differentiate each entry; then factor out $\frac i2\sigma_3$, using $\sigma_3\sigma_3 = 1$ and $i \cdot i = -1$), so $-(\partial_\varphi U)U^{-1} = -\frac i2\sigma_3 = \Omega_\varphi$.

**Which rotation removes it.** Section 6.15 will derive how the spinor connection changes when the frame is changed and the spinor components change by a spin transformation $R$: $\Omega'_\varphi = R\,\Omega_\varphi R^{-1} - (\partial_\varphi R)R^{-1}$. The Cartesian frame (the unit directions along $x$ and $y$) does not turn, so its connection is 0, and the rule with $R = U$ turns this 0 into $-(\partial_\varphi U)U^{-1} = \Omega_\varphi$: $U$ is the spinor rotation that carries the Cartesian frame into the polar frame. The way back is the inverse rotation $U^{-1} = \cos\frac\varphi2 - i\sin\frac\varphi2\,\sigma_3$ (multiply out: $UU^{-1} = \cos^2\frac\varphi2 + \sin^2\frac\varphi2\,\sigma_3\sigma_3 = 1$, because the two mixed terms cancel). Its derivative is

$$
\partial_\varphi U^{-1} = -\tfrac12\sin\tfrac\varphi2 - \tfrac i2\cos\tfrac\varphi2\,\sigma_3 = -\tfrac i2\sigma_3\Big(\cos\tfrac\varphi2 - i\sin\tfrac\varphi2\,\sigma_3\Big) = -\tfrac i2\sigma_3\,U^{-1}
$$

(differentiate each entry; then factor out $-\frac i2\sigma_3$, using $\sigma_3\sigma_3 = 1$ and $i \cdot i = -1$), so $(\partial_\varphi U^{-1})\,U = -\frac i2\sigma_3$. The matrix $\sigma_3$ commutes with $U$ and $U^{-1}$ (both are built from $1$ and $\sigma_3$), so $U^{-1}\Omega_\varphi U = \Omega_\varphi U^{-1}U = \Omega_\varphi$. The rule with $R = U^{-1}$ (whose inverse is $U$) therefore gives

$$
\Omega'_\varphi = U^{-1}\,\Omega_\varphi\,U - (\partial_\varphi U^{-1})\,U = -\tfrac i2\sigma_3 - \Big(-\tfrac i2\sigma_3\Big) = 0 ,
$$

and $\Omega'_r = 0$, because $U$ does not depend on $r$. (The rule with $R = U$ would instead give $-\frac i2\sigma_3 - \frac i2\sigma_3 = -i\sigma_3$: the rotation $U$ turns the polar frame further, not back.) In a flat space the spin connection is only the turning of the chosen frame, and the spinor rotation $U^{-1}$ removes it. At $\varphi = 2\pi$ the frame is back where it started, but $U(2\pi) = \cos\pi = -1$: a spinor turns by half the angle, the double cover of Chapter 5. Notebook 06a checks all of this in In [5] and draws it in figure 1. PROVED (exact; the notebook's checks are its own, the plane is not a Revision record).

**Two lessons.** First, a nonzero spin connection, and even a nonzero $\sum_\mu\gamma^\mu\Omega_\mu$, does not mean that space is curved; it may only record how the chosen frame turns. Second, the test of curvature is $F_{\mu\nu}$, not $\Omega_\mu$. Both lessons return in Sections 6.16 and 6.17.

### 6.6 The spin connection of the corrected metric: ten components

**A diagonal vielbein, in general.** Let $e^a{}_\mu = f_a\delta^a_\mu$ and $e_b{}^\nu = \delta_b^\nu/f_b$. In the formula of Section 6.4 only $\nu = a$ survives in the outer sum and only $\lambda = b$ in the inner sum:

$$
\omega_\mu{}^a{}_b = f_a\Big(\partial_\mu\frac{\delta_b^a}{f_b} + \Gamma^a{}_{\mu b}\frac{1}{f_b}\Big) .
$$

For $a = b$ this is $f_a\big(-\partial_\mu f_a/f_a^2 + \Gamma^a{}_{\mu a}/f_a\big) = \Gamma^a{}_{\mu a} - \partial_\mu f_a/f_a = 0$, by cases (a) and (b) of Section 6.3. For $a \neq b$ only the second term remains, $(f_a/f_b)\Gamma^a{}_{\mu b}$, and by case (d) it can be nonzero only when $\mu = a$ or $\mu = b$:

$$
\omega_a{}^a{}_b = \frac{f_a}{f_b}\,\frac{\partial_bf_a}{f_a} = \frac{\partial_bf_a}{f_b}, \qquad \omega_b{}^a{}_b = \frac{f_a}{f_b}\Big(-\eta_{aa}\eta_{bb}\frac{f_b\,\partial_af_b}{f_a^2}\Big) = -\eta_{aa}\eta_{bb}\,\frac{\partial_af_b}{f_a}
$$

(no sums; case (b) with $\lambda = a$, $\nu = b$, and case (c) with $\lambda = a$, $\mu = b$). Lowering with $\eta_{aa}$ gives the two forms

$$
\omega_{a\,ab} = \eta_{aa}\,\frac{\partial_bf_a}{f_b}, \qquad \omega_{b\,ab} = -\eta_{bb}\,\frac{\partial_af_b}{f_a} \qquad (a \neq b,\ \text{no sum}) ,
$$

and the antisymmetry of Section 6.4 can be seen directly: the second form with the letters $a$ and $b$ exchanged reads $\omega_{a\,ba} = -\eta_{aa}\partial_bf_a/f_b = -\omega_{a\,ab}$. So: **in a diagonal vielbein, $\omega_{\mu ab}$ is nonzero only when $\mu$ is one of the two frame indices, and then $\omega_{\mu\,\mu b} = \eta_{\mu\mu}\,\partial_bf_\mu/f_b$.**

**The corrected metric.** The factors depend on $x_0$ and $x_4$ only, so in $\omega_{\mu\,\mu b} = \eta_{\mu\mu}\partial_bf_\mu/f_b$ the index $b$ must be $x0$ or $x4$. From Section 6.3, $\partial_4f_0 = h_4f_0$, $\partial_4f_i = a_4'f_i$, $\partial_4f_t = h_4f_t$, $\partial_0f_t = H\cot z\,f_t$ and $\partial_0f_i = 0$, with $f_0 = s_b\cot z$ and $f_4 = 1$. Go through the directions $\mu$ one at a time.

$\mu = x0$, $b = x4$:

$$
\omega_{x0\,x0\,x4} = (+1)\frac{\partial_4f_0}{f_4} = h_4f_0 = h_4\,s_b\cot z
$$

(the factor $s_b$ of the hidden direction changes with the time at the rate $h_4$; $f_4 = 1$).

$\mu = x_i$, $b = x4$ ($b = x0$ gives nothing, because $\partial_0f_i = 0$):

$$
\omega_{x_i\,x_i\,x4} = (+1)\frac{a_4'f_i}{1} = a_4'\,e^{a_4} .
$$

$\mu = x_t$, $b = x4$ and $b = x0$ ($\eta_{tt} = -1$):

$$
\omega_{x_t\,x_t\,x4} = (-1)\frac{h_4f_t}{1} = -h_4\,s_bW, \qquad \omega_{x_t\,x_t\,x0} = (-1)\frac{H\cot z\,f_t}{s_b\cot z} = -HW
$$

($f_t = s_bW$; in the second, $s_b\cot z$ cancels against $f_t = s_bW$ up to the factor $W$).

$\mu = x4$: every candidate contains $\partial_bf_4 = 0$ ($f_4 = 1$) or, in the form $\omega_{b\,ab}$ with $b = x4$, $\partial_af_4 = 0$; so $\omega_{x4\,ab} = 0$.

The record lists the components with the smaller index first, $a < b$ in the order $x0, \dots, x7$; for the extra times this is $\omega_{x_t\,x4\,x_t} = -\omega_{x_t\,x_t\,x4} = h_4s_bW$ and $\omega_{x_t\,x0\,x_t} = -\omega_{x_t\,x_t\,x0} = HW$. Altogether there are $1 + 3 + 3 + 3 = 10$ independent nonzero components:

| $\mu$ | pair $(a, b)$ | $\omega_{\mu ab}$ | kind of pair |
| --- | --- | --- | --- |
| $x0$ | $(x0, x4)$ | $h_4\,s_b\cot z$ | boost (space-like with time-like) |
| $x_i$ ($i = 1, 2, 3$) | $(x_i, x4)$ | $a_4'\,e^{a_4}$ | boost (space-like with time-like) |
| $x_t$ ($t = 5, 6, 7$) | $(x0, x_t)$ | $H\,W$ | boost (space-like with time-like) |
| $x_t$ | $(x4, x_t)$ | $h_4\,s_bW$ | rotation (two time-like) |

Each component is a rate times a factor that never vanishes between the degenerate points: the rate is $a_4'$ (3-space), $h_4 = b_4'/(2b_4) - a_4'$ (the hidden block) or $H$ (the warp of the extra times), the factor $e^{a_4}$, $s_b\cot z$, $s_bW$ or $W$. So the part made by the time dependence vanishes only if $a_4$ and $b_4$ are both constant, and the part made by the warp vanishes only if $H = 0$, which is not a metric of the family (the entries $g_{tt}$ would vanish and $g_{00}$ would grow without bound; record check `degenerate_at_H_0`). **For every admissible $H > 0$ the spin connection of the diagonal vielbein is nonzero.** Note the signs: the hidden direction and an extra time turn towards the time with the same rate $h_4$, which is negative on the history of the record ($-H/3$), because they shrink together while 3-space grows. A dated comparison: in the metric of 2026-10-14 (withdrawn on 2026-10-16) 3-space carried the warp as well, and there were 12 components, with no $\omega_{x0\,ab}$; in the corrected metric 3-space has no component along the hidden direction, and the hidden direction itself follows the extra times in time. Figure 06a.4 shows the arrays $\omega_{x0\,ab}$, $\omega_{x1\,ab}$ and $\omega_{x5\,ab}$ at a sample point.

| statement | status | where it is verified |
| --- | --- | --- |
| exactly 10 independent nonzero $\omega_{\mu ab}$, with the values of the table | PROVED | `field-theory.json`, formula `omega_nonzero`; `wolfram-field-theory.json`, check `omega_components`; Notebook 06a, In [11] |
| each is a rate ($a_4'$, $h_4$ or $H$) times a nonvanishing factor; the connection vanishes only for constant $a_4$ and $b_4$ and $H = 0$ | PROVED | Notebook 06a, In [11]; `wolfram-field-theory.json`, check `Omega_vanishes_iff_a4prime_b4prime_and_H_vanish`; `python-field-theory.json`, check `nontriviality_Omega_zero_iff_flat` |

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

**The corrected metric.** With the table of Section 6.6 and $S^{ab} = \frac12\gamma^a\gamma^b$:

$$
\begin{aligned}
\Omega_{x0} &= \tfrac12 h_4\,s_b\cot z\;\gamma^{(x0)}\gamma^{(x4)}, \qquad \Omega_{x_i} = \tfrac12 a_4'\,e^{a_4}\;\gamma^{(x_i)}\gamma^{(x4)}, \qquad \Omega_{x4} = 0,\\
\Omega_{x_t} &= \tfrac12 W\big(h_4\,s_b\;\gamma^{(x4)}\gamma^{(x_t)} + H\;\gamma^{(x0)}\gamma^{(x_t)}\big)
\end{aligned}
$$

(each component of the table times its generator; the record writes exactly these, formula `Omega_components`). No frame direction turns when one moves along the time. Moving along the hidden direction the hidden frame direction tilts towards the time, because the length $s_b\cot z$ of a step $dx_0$ changes with the time; moving along a 3-space direction the 3-space frame direction tilts towards the time for the same reason with the rate $a_4'$; moving along an extra time its frame direction turns towards the time (rate $h_4s_bW$) and towards the hidden direction (rate $HW$). A boost generator is a **symmetric** matrix and a rotation generator an **antisymmetric** one: the transpose of a product reverses the order, and the author's gammas satisfy $(\gamma^a)^T = \eta_{aa}\gamma^a$ (Chapter 5), so

$$
(\gamma^a\gamma^b)^T = (\gamma^b)^T(\gamma^a)^T = \eta_{aa}\eta_{bb}\,\gamma^b\gamma^a = -\eta_{aa}\eta_{bb}\,\gamma^a\gamma^b \qquad (a \neq b) ,
$$

which is $+\gamma^a\gamma^b$ for a boost pair ($\eta_{aa}\eta_{bb} = -1$, 16 pairs) and $-\gamma^a\gamma^b$ for a rotation pair (12 pairs). So $\Omega_{x0}$ and $\Omega_{x_i}$ are symmetric matrices (boosts), and $\Omega_{x_t}$ is an antisymmetric rotation part plus a symmetric boost part; $\Omega_{x5}$ has 32 nonzero entries of 256 (Notebook 06a, In [13]). Figure 06a.5 shows $\Omega_{x0}$, $\Omega_{x1}$ and $\Omega_{x5}$.

**The covariant constancy, checked.** With these $\Omega_\mu$ the defining property holds for all 64 pairs $(\mu, c)$ and $D_\mu\gamma^\nu = 0$ for all 64 pairs $(\mu, \nu)$ (Notebook 06a, In [13]).

| statement | status | where it is verified |
| --- | --- | --- |
| $\Omega_{x0}$, $\Omega_{x_i}$, $\Omega_{x_t}$ as above; $\Omega_{x4} = 0$, $\Omega_{x0} \neq 0$ | PROVED | Notebook 06a, In [13]; `field-theory.json`, formula `Omega_components`; `python-field-theory.json`, check `Omega_x4_vanishes_Omega_x0_does_not`; `wolfram-field-theory.json`, check `Omega_components` |
| the defining property for all 64 pairs | PROVED | Notebook 06a, In [13]; `wolfram-field-theory.json`, check `S_rotates_gamma_with_omega` |
| $D_\mu\gamma^\nu = 0$ for all 64 pairs | PROVED | `python-field-theory.json`, check `covariant_constancy_D_mu_gamma_nu`; `wolfram-field-theory.json`, check `gamma_covariantly_constant` |
| uniqueness up to a multiple of $1$ | PROVED (above, with the commutant of Chapter 5) | `python-algebra.json`, check `pin_commutant_dimension_1` (in `Revision/algebra/reports`) |

### 6.8 The contraction $\gamma^\mu\Omega_\mu$, direction by direction

The field equation contains $\sum_\mu\gamma^\mu D_\mu\Psi = \sum_\mu\gamma^\mu\partial_\mu\Psi + \big(\sum_\mu\gamma^\mu\Omega_\mu\big)\Psi$, so the spin connection enters it only through the one $16 \times 16$ matrix $\sum_\mu\gamma^\mu\Omega_\mu$. We compute it one direction at a time.

**The hidden direction**, $\mu = x0$. With $\gamma^{x0} = \gamma^{(x0)}/f_0$ and $f_0 = s_b\cot z$:

$$
\gamma^{x0}\Omega_{x0} = \frac{\gamma^{(x0)}}{f_0}\;\tfrac12 h_4f_0\,\gamma^{(x0)}\gamma^{(x4)} = \tfrac12 h_4\,\gamma^{(x0)}\gamma^{(x0)}\gamma^{(x4)} = \tfrac12 h_4\,\gamma^{(x4)}
$$

(the formulas of Sections 6.2 and 6.7, with $s_b\cot z = f_0$; the factor $f_0$ cancels; $\gamma^{(x0)}\gamma^{(x0)} = \eta_{00}1 = +1$ by the Clifford relation).

**A 3-space direction**, $\mu = x1$ (the same for $x2$ and $x3$). With $\gamma^{x1} = \gamma^{(x1)}/f_1$ and $f_1 = e^{a_4}$:

$$
\gamma^{x1}\Omega_{x1} = \frac{\gamma^{(x1)}}{f_1}\;\tfrac12 a_4'f_1\,\gamma^{(x1)}\gamma^{(x4)} = \tfrac12 a_4'\,\gamma^{(x1)}\gamma^{(x1)}\gamma^{(x4)} = \tfrac12 a_4'\,\gamma^{(x4)}
$$

(the factor $f_1$ cancels; $\gamma^{(x1)}\gamma^{(x1)} = +1$).

**An extra time**, $\mu = x5$ (the same for $x6$ and $x7$). With $\gamma^{x5} = \gamma^{(x5)}/f_5$, $f_5 = s_bW$:

$$
\gamma^{x5}\Omega_{x5} = \frac{\gamma^{(x5)}}{s_bW}\;\tfrac12 W\big(h_4s_b\,\gamma^{(x4)}\gamma^{(x5)} + H\,\gamma^{(x0)}\gamma^{(x5)}\big) = \tfrac12 h_4\,\gamma^{(x5)}\gamma^{(x4)}\gamma^{(x5)} + \frac{H}{2s_b}\,\gamma^{(x5)}\gamma^{(x0)}\gamma^{(x5)}
$$

(the factor $W$ cancels; in the first term $s_b$ cancels as well). Now $\gamma^{(x5)}\gamma^{(x4)}\gamma^{(x5)} = -\gamma^{(x4)}\gamma^{(x5)}\gamma^{(x5)} = -\gamma^{(x4)}(-1) = \gamma^{(x4)}$ (two different gammas anticommute; $\gamma^{(x5)}\gamma^{(x5)} = \eta_{55}1 = -1$), and in the same way $\gamma^{(x5)}\gamma^{(x0)}\gamma^{(x5)} = \gamma^{(x0)}$. With $1/s_b = e^{a_4}b_4^{-1/2}$:

$$
\gamma^{x5}\Omega_{x5} = \tfrac12 h_4\,\gamma^{(x4)} + \tfrac12He^{a_4}b_4^{-1/2}\,\gamma^{(x0)} .
$$

**The time.** $\Omega_{x4} = 0$, so $\gamma^{x4}\Omega_{x4} = 0$.

**The sum.** Writing each term as $\alpha_\mu\gamma^{(x4)} + \beta_\mu\gamma^{(x0)}$:

| direction $\mu$ | $\alpha_\mu$ (coefficient of $\gamma^{(x4)}$) | $\beta_\mu$ (coefficient of $\gamma^{(x0)}$) |
| --- | --- | --- |
| $x0$ (hidden) | $\frac12h_4$ | $0$ |
| $x1$, $x2$, $x3$ (inflating) | $\frac12 a_4'$ each | $0$ |
| $x4$ (time) | $0$ | $0$ |
| $x5$, $x6$, $x7$ (deflating) | $\frac12h_4$ each | $\frac12He^{a_4}b_4^{-1/2}$ each |
| total | $\frac32a_4' + 2h_4 = \frac{b_4'}{b_4} - \frac{a_4'}{2}$ | $\frac32He^{a_4}b_4^{-1/2}$ |

The total of the first column, line by line: $\frac32a_4' + 4\cdot\frac12h_4 = \frac32a_4' + 2\big(\frac{b_4'}{2b_4} - a_4'\big)$ (one $x0$ and three extra times, each $\frac12h_4$; the definition of $h_4$) $= \frac32a_4' + \frac{b_4'}{b_4} - 2a_4' = \frac{b_4'}{b_4} - \frac{a_4'}{2}$ (multiply out; collect the $a_4'$ terms). So

$$
\sum_\mu\gamma^\mu\Omega_\mu = c_g\,\gamma^{(x0)} + v_g\,\gamma^{(x4)}, \qquad c_g = \tfrac32He^{a_4}b_4^{-1/2}, \qquad v_g = \frac{b_4'}{b_4} - \frac{a_4'}{2} .
$$

**In words.** Along the time direction the three inflating 3-space directions push with $+\frac32a_4'$, and the four directions of the hidden block, which change at the common rate $h_4$, push with $2h_4 = -2a_4' + b_4'/b_4$. These do not cancel: the sum keeps $-\frac12a_4'$ and the whole $b_4'/b_4$. Along the hidden direction only the three extra times push, each with $\frac12H/s_b$: their warp factor $W$ depends on $x_0$, while 3-space has no warp and the hidden direction's own factor gives no $\gamma^{(x0)}$ term. The result contains no $x_0$, but it contains $a_4$, through $e^{a_4}$ and $a_4'$: the coefficient $c_g$ is $\frac32H$ divided by the hidden scale $s_b$, so it grows as the hidden block deflates. On the history of the Revision record, $a_4' = H$, $b_4'/b_4 = \frac43H$ and $e^{a_4}b_4^{-1/2} = e^{Hx_4}e^{-2Hx_4/3} = e^{Hx_4/3}$, so

$$
\sum_\mu\gamma^\mu\Omega_\mu = \tfrac32He^{Hx_4/3}\,\gamma^{(x0)} + \tfrac56H\,\gamma^{(x4)}
$$

($v_g = \frac43H - \frac12H = \frac56H$). A dated comparison: for the metric of 2026-10-14, withdrawn on 2026-10-16, the same computation gave $3H\gamma^{(x0)} + \frac34(b_4'/b_4)\gamma^{(x4)}$, with no $a_4$ at all; the record keeps this comparison in its scope check `gammaOmega_sees_the_hidden_block`.

**Reading off the coefficients with traces.** Notebook 06a finds $\alpha_\mu$ and $\beta_\mu$ with traces (the **trace** of a square matrix is the sum of its diagonal entries). For two different gammas $\mathrm{tr}(\gamma^a\gamma^b) = 0$, while $\mathrm{tr}(\gamma^{(x4)}\gamma^{(x4)}) = \mathrm{tr}(-1) = -16$ and $\mathrm{tr}(\gamma^{(x0)}\gamma^{(x0)}) = +16$ (Chapter 4). So for $M = \alpha\gamma^{(x4)} + \beta\gamma^{(x0)}$:

$$
\mathrm{tr}(M\gamma^{(x4)}) = \alpha(-16) + \beta\cdot 0, \qquad \mathrm{tr}(M\gamma^{(x0)}) = \alpha\cdot0 + \beta\cdot16 ,
$$

hence $\alpha = -\mathrm{tr}(M\gamma^{(x4)})/16$ and $\beta = \mathrm{tr}(M\gamma^{(x0)})/16$. The notebook then checks that $M - \alpha\gamma^{(x4)} - \beta\gamma^{(x0)}$ is the zero matrix, so that nothing else is hidden in $M$.

| statement | status | where it is verified |
| --- | --- | --- |
| the eight terms $\gamma^\mu\Omega_\mu$ (no sum) of the table | PROVED | `field-theory.json`, formula `gammaOmega_per_direction`; `wolfram-field-theory.json`, check `gammaOmega_per_direction`; `python-field-theory.json`, check `per_direction_terms`; Notebook 06a, In [15] |
| $\gamma^\mu\Omega_\mu = c_g\gamma^{(x0)} + v_g\gamma^{(x4)}$ for every $H > 0$, $a_4$ and $b_4$; $\frac32He^{Hx_4/3}\gamma^{(x0)} + \frac56H\gamma^{(x4)}$ on the history of the record | PROVED | `field-theory.json`, formula `gammaOmega_total`; `wolfram-field-theory.json`, check `gammaOmega_total`; `python-field-theory.json`, check `gamma_mu_Omega_mu_equals_hidden_block_terms`; lead report, check `gamma_Omega_equals_hidden_block_terms`; Notebook 06a, In [15] |

### 6.9 Why the time term is half the rate of the 7-volume: the divergence form

The result of Section 6.8 is not an accident of the algebra. Two facts explain it without computing $\Omega_\mu$ at all.

**Fact 1: for each $\mu$ separately, $\gamma^\mu\Omega_\mu + \Omega_\mu\gamma^\mu = 0$ (no sum).** In the diagonal vielbein $\Omega_\mu$ contains only generators $S^{(\mu)b}$ with $b \neq \mu$ (Section 6.6: $\omega_{\mu ab}$ is nonzero only when $\mu$ is one of the two frame indices), and $\gamma^\mu$ is a multiple of $\gamma^{(\mu)}$. For one such generator:

$$
\gamma^{(\mu)}\,\tfrac12\gamma^{(\mu)}\gamma^{(b)} = \tfrac12\eta_{\mu\mu}\gamma^{(b)}, \qquad \tfrac12\gamma^{(\mu)}\gamma^{(b)}\,\gamma^{(\mu)} = -\tfrac12\gamma^{(\mu)}\gamma^{(\mu)}\gamma^{(b)} = -\tfrac12\eta_{\mu\mu}\gamma^{(b)}
$$

(the Clifford relation; in the second product the two different gammas $\gamma^{(b)}$ and $\gamma^{(\mu)}$ are exchanged at the cost of a sign). The two products are opposite, so they anticommute, and so do the combinations.

**The divergence form.** Take the covariant constancy $D_\mu\gamma^\nu = 0$ of Section 6.7, put $\nu = \mu$ and sum over $\mu$:

$$
\sum_\mu\partial_\mu\gamma^\mu + \sum_{\mu,\lambda}\Gamma^\mu{}_{\mu\lambda}\gamma^\lambda + \sum_\mu\big(\Omega_\mu\gamma^\mu - \gamma^\mu\Omega_\mu\big) = 0 .
$$

The contracted Christoffel symbol of a diagonal metric is $\sum_\mu\Gamma^\mu{}_{\mu\lambda} = \sum_\mu\partial_\lambda\ln\lvert f_\mu\rvert = \partial_\lambda\ln\lvert\prod_\mu f_\mu\rvert = \partial_\lambda\ln\sqrt{\lvert g\rvert}$ (cases (a) and (b) of Section 6.3; the logarithm of a product is the sum of the logarithms; Section 6.2). So the first two sums are

$$
\sum_\lambda\Big(\partial_\lambda\gamma^\lambda + \frac{\partial_\lambda\sqrt{\lvert g\rvert}}{\sqrt{\lvert g\rvert}}\gamma^\lambda\Big) = \frac{1}{\sqrt{\lvert g\rvert}}\sum_\lambda\partial_\lambda\big(\sqrt{\lvert g\rvert}\,\gamma^\lambda\big)
$$

(the product rule read backwards). By Fact 1, $\Omega_\mu\gamma^\mu = -\gamma^\mu\Omega_\mu$, so the third sum is $-2\sum_\mu\gamma^\mu\Omega_\mu$. Solving for the contraction:

$$
\sum_\mu\gamma^\mu\Omega_\mu = \frac{1}{2\sqrt{\lvert g\rvert}}\sum_\mu\partial_\mu\big(\sqrt{\lvert g\rvert}\,\gamma^\mu\big) .
$$

The right side is built from the volume factor and the vielbein alone. Because the constant sign $G$ appears in the numerator and in the denominator, the signed product $f_0f_1\cdots f_7$ may be used in place of $\sqrt{\lvert g\rvert}$.

**Fact 2: the product structure.** For the diagonal vielbein $\big(\prod_c f_c\big)\gamma^\mu = \big(\prod_c f_c\big)\gamma^{(\mu)}/f_\mu = \big(\prod_{c\neq\mu}f_c\big)\gamma^{(\mu)}$ (no sum over $\mu$). The term $\partial_\mu$ of this product can be nonzero only if the product depends on its own coordinate $x_\mu$, that is only for $\mu = x0$ or $\mu = x4$. For the hidden direction:

$$
\prod_{c\neq x0}f_c = e^{3a_4}\cdot1\cdot e^{-3a_4}b_4^{3/2}W^3 = b_4^{3/2}W^3
$$

(Section 6.2: three 3-space factors, the time factor 1 and three extra-time factors). Its derivative uses $\partial_0W = H\cot z\,W$ (Section 6.3) and the power rule, $\partial_0W^3 = 3W^2\,\partial_0W = 3H\cot z\,W^3$, so

$$
\frac{1}{2f_0\cdots f_7}\,\partial_0\big(b_4^{3/2}W^3\big)\;\gamma^{(x0)} = \frac{3H\cot z\;b_4^{3/2}W^3}{2e^{-a_4}b_4^2\cot z\,W^3}\,\gamma^{(x0)} = \tfrac32He^{a_4}b_4^{-1/2}\,\gamma^{(x0)} = c_g\,\gamma^{(x0)}
$$

($b_4$ does not depend on $x_0$; then cancel $\cot z\,W^3$ and $b_4^{3/2}$, with $1/(e^{-a_4}b_4^{1/2}) = e^{a_4}b_4^{-1/2}$). The hidden term comes from the warp $W^3$ of the three extra times; the hidden factor $\cot z$ itself cancels. For the time:

$$
\prod_{c\neq x4}f_c = f_0f_1\cdots f_7 = e^{-a_4}b_4^2\cot z\,W^3
$$

($f_4 = 1$, so the product without $x4$ is the whole product), and

$$
\frac{1}{2f_0\cdots f_7}\,\partial_4\big(f_0\cdots f_7\big)\;\gamma^{(x4)} = \tfrac12\,\partial_4\ln\big(e^{-a_4}b_4^2\big)\,\gamma^{(x4)} = \tfrac12\Big(-a_4' + \frac{2b_4'}{b_4}\Big)\gamma^{(x4)} = v_g\,\gamma^{(x4)}
$$

(a derivative divided by its function is the derivative of the logarithm; the factor $\cot z\,W^3$ does not depend on $x_4$; then Section 6.2). **The term along the time is half the rate at which the proper 7-volume of a slice grows**, which is the deeper reason for the result of Section 6.8: the inflation of 3-space ($e^{3a_4}$) and the deflation of the extra times ($e^{-3a_4}$) cancel in the 7-volume, but the deflation of the hidden direction ($e^{-a_4}$) does not, and $b_4$ enters four times. On the history of the record the 7-volume grows like $e^{5Hx_4/3}$ and $v_g = \frac56H$. So the divergence form gives $c_g\gamma^{(x0)} + v_g\gamma^{(x4)}$ again, by a second and much shorter route. Notebook 06a checks Fact 1 for every $\mu$, the divergence form and the eight products (In [18]), and once more with a calculator's method, a central difference (In [19]).

| statement | status | where it is verified |
| --- | --- | --- |
| $\{\gamma^\mu, \Omega_\mu\} = 0$ for each $\mu$ | PROVED | Notebook 06a, In [18]; `python-field-theory.json`, check `anticommutator_gamma_Omega_vanishes` |
| the divergence form equals $c_g\gamma^{(x0)} + v_g\gamma^{(x4)}$; $v_g$ is half the rate of the 7-volume | PROVED | `python-field-theory.json`, check `divergence_of_sqrtg_gamma`; `wolfram-field-theory.json`, check `gammaOmega_divergence_form`; lead report, check `gamma_Omega_divergence_formula` |
| the central differences reproduce $\frac32$ (the coefficient $c_g$ divided by $e^{a_4}b_4^{-1/2}$, with $H = 1$) to $2 \times 10^{-7}$ over both halves of a cell, and $v_g$ (for the illustrative $b_4 = e^{4x_4/3}(1 + \frac12\sin x_4)$) to $2 \times 10^{-10}$ | COMPUTED (Notebook 06a, In [19]; step $h = 10^{-5}$; the largest deviation lies at the ends of the grid next to the tips, where the third derivative is largest) | Notebook 06a only |

### 6.10 The Dirac operator written out, non-triviality and the negative control

**The Dirac operator.** Combine $\gamma^\mu = \gamma^{(\mu)}/f_\mu$ with the contraction:

$$
\sum_\mu\gamma^\mu D_\mu\Psi = \sum_a\frac{1}{f_a}\gamma^{(a)}\partial_a\Psi + c_g\,\gamma^{(x0)}\Psi + v_g\,\gamma^{(x4)}\Psi ,
$$

that is, with the factors written out,

$$
\begin{aligned}
&e^{a_4}b_4^{-1/2}\tan z\,\gamma^{(x0)}\partial_0\Psi + e^{-a_4}\big(\gamma^{(x1)}\partial_1 + \gamma^{(x2)}\partial_2 + \gamma^{(x3)}\partial_3\big)\Psi + \gamma^{(x4)}\partial_4\Psi \\
&\quad + e^{a_4}b_4^{-1/2}W^{-1}\big(\gamma^{(x5)}\partial_5 + \gamma^{(x6)}\partial_6 + \gamma^{(x7)}\partial_7\big)\Psi + \tfrac32He^{a_4}b_4^{-1/2}\gamma^{(x0)}\Psi + \Big(\frac{b_4'}{b_4} - \frac{a_4'}{2}\Big)\gamma^{(x4)}\Psi .
\end{aligned}
$$

This is the left side of the field equation of both fields; the right side is $(m + U'(S))\Psi$ with $S = \bar\Psi\Psi$ (Chapter 7). The Revision record writes exactly this operator (formula `field_equation` of `field-theory.json`) and all sixteen component equations (formula `field_equation_components`), and Notebook 06a compares each of them with its own computation (In [20]). The two hidden terms combine into $e^{a_4}b_4^{-1/2}\big(\tan z\,\partial_0 + \frac32H\big)\gamma^{(x0)}$, the hidden-direction operator of Section 6.24. **Where the deflation enters.** It enters $\gamma^\mu\Omega_\mu$ through $c_g$ and $v_g$, and it enters every derivative term through the factors $1/f_a$: as 3-space inflates the 3-space derivatives are weighted less and less ($e^{-a_4}$), and as the hidden block deflates the hidden and extra-time derivatives are weighted more and more ($e^{a_4}b_4^{-1/2} = 1/s_b$, which is $e^{Hx_4/3}$ on the history). Figure 06a.9 draws these factors.

**The block form.** In the chiral split $\Psi = (\psi_-, \psi_+)$ (components 1 to 8 and 9 to 16, Chapter 5) every gamma of the author has zero blocks on the diagonal, $\gamma^{(xa)} = \begin{pmatrix}0 & \bar\tau_a\\ \tau_a & 0\end{pmatrix}$, and $\gamma^{(x0)}$ has the $8 \times 8$ identity in both off-diagonal blocks. So $c_g\gamma^{(x0)}$ maps the first eight components onto the last eight and back with the factor $c_g$, which is why its picture (figure 06a.7) shows the value $c_g = 1.77$ on two diagonal lines at the sample point. Record: formula `field_equation_blocks`; `wolfram-field-theory.json`, check `block_form`.

**Non-triviality.** Write $M = c_g\gamma^{(x0)} + v_g\gamma^{(x4)}$ for the term of the field equation. Line by line,

$$
MM = c_g^2\gamma^{(x0)}\gamma^{(x0)} + c_gv_g\big(\gamma^{(x0)}\gamma^{(x4)} + \gamma^{(x4)}\gamma^{(x0)}\big) + v_g^2\gamma^{(x4)}\gamma^{(x4)} = \big(c_g^2 - v_g^2\big)\,1
$$

(multiply out; $(\gamma^{(x0)})^2 = \eta_{00}1 = 1$, $(\gamma^{(x4)})^2 = \eta_{44}1 = -1$, and the middle bracket is the anticommutator of two different gammas, which is 0). When $c_g^2 - v_g^2 \neq 0$, $M\Psi = 0$ gives $\Psi = MM\Psi/(c_g^2 - v_g^2) = 0$ (multiply from the left by $M$ and divide by the number). So **the term vanishes only for $\Psi = 0$, except at times where $c_g = \pm v_g$**. There $M = c_g(\gamma^{(x0)} \pm \gamma^{(x4)})$ is not zero but squares to zero, and its rank is 8: it sends an 8-dimensional set of nonzero fields to zero (`python-field-theory.json`, check `gravity_term_square`; Notebook 06a, In [20], computes both ranks exactly, [8, 8]). On the history of the Revision record $c_g = \frac32He^{Hx_4/3}$ and $v_g = \frac56H$, so

$$
c_g^2 - v_g^2 = \tfrac94H^2e^{2Hx_4/3} - \tfrac{25}{36}H^2 = H^2\Big(\tfrac94e^{2Hx_4/3} - \tfrac{25}{36}\Big) .
$$

Since $v_g > 0$ and $c_g > 0$, only $c_g = v_g$ is possible: $\frac32e^{Hx_4/3} = \frac56$, that is $e^{Hx_4/3} = \frac59$ (divide by $\frac32$) and $x_4 = 3\ln(5/9)/H \approx -1.7634/H$ (take the logarithm and multiply by $3/H$). Before this time $c_g < v_g$ and after it $c_g > v_g$, because $c_g$ grows with $x_4$; at $x_4 = 0$, $MM = H^2(\frac94 - \frac{25}{36})\,1 = \frac{14}{9}H^2\,1$. So on the history the exception occurs exactly once, at a negative time before the first slice $a_4 = 0$ of the record's Kohn-Sham work, and for every $x_4 > -1.7634/H$, in particular on all the slices $a_4 = 0, 0.5, 1, 1.5, 2$ of the record, the term vanishes only for $\Psi = 0$ (PROVED; `wolfram-field-theory.json`, checks `nontriviality_1_dirac16complex` and `nontriviality_2_dirac16complex00`, for the two fields, which record $MM$ on the history; the time $-1.7634/H$ is COMPUTED by Notebook 06a, In [20], from the record's formula). Section 6.29 states precisely how far these statements reach.

**The negative control: a hidden block that GROWS.** Does the term see in which direction the hidden block changes, or would it look the same if the block grew? Change only the sign of $a_4$ in the hidden scale, so that the hidden direction and the extra times grow like 3-space: $s_b \to e^{+a_4}b_4^{1/2}$, factors $f_0 = e^{a_4}b_4^{1/2}\cot z$ and $f_t = e^{a_4}b_4^{1/2}W$ (the lead's control). Use the divergence form of Section 6.9. The product of all eight factors is now

$$
f_0\cdots f_7 = e^{a_4}b_4^{1/2}\cot z\cdot e^{3a_4}\cdot1\cdot e^{3a_4}b_4^{3/2}W^3 = e^{7a_4}b_4^2\cot z\,W^3
$$

(the exponents add, $1 + 3 + 3 = 7$), so the time term is

$$
\tfrac12\,\partial_4\ln\big(e^{7a_4}b_4^2\big)\,\gamma^{(x4)} = \Big(\tfrac72a_4' + \frac{b_4'}{b_4}\Big)\gamma^{(x4)}
$$

(the derivative of the logarithm, as in Section 6.9), and the product without $x0$ is $e^{6a_4}b_4^{3/2}W^3$, so the hidden term is

$$
\frac{3H\cot z\,e^{6a_4}b_4^{3/2}W^3}{2e^{7a_4}b_4^2\cot z\,W^3}\,\gamma^{(x0)} = \tfrac32He^{-a_4}b_4^{-1/2}\,\gamma^{(x0)}
$$

(the same steps as in Section 6.9). Together:

$$
\sum_\mu\gamma^\mu\Omega_\mu\Big|_{\text{control}} = \tfrac32He^{-a_4}b_4^{-1/2}\,\gamma^{(x0)} + \Big(\frac{b_4'}{b_4} + \tfrac72a_4'\Big)\gamma^{(x4)} .
$$

**The coefficient of $a_4'$ along the time is $+\frac72$ instead of $-\frac12$**, and the hidden coefficient is $\frac32H$ divided by the new hidden scale $e^{a_4}b_4^{1/2}$ instead of $\frac32H$ divided by $s_b$; on the history it falls like $\frac32He^{-5Hx_4/3}$ instead of growing like $\frac32He^{Hx_4/3}$. The term sees the direction in which the hidden block changes. PROVED; lead report, check `negative_control_growing_block`; Notebook 06a, In [22], and figure 10.

| statement | status | where it is verified |
| --- | --- | --- |
| the Dirac operator written out; all 16 components | PROVED | `field-theory.json`, formulas `field_equation` and `field_equation_components`; `wolfram-field-theory.json`, checks `Dirac_operator_explicit_G` and `Dirac_operator_explicit_C`; Notebook 06a, In [20] |
| $MM = (c_g^2 - v_g^2)\,1$: the term vanishes only for $\Psi = 0$ unless $c_g = \pm v_g$, where $M$ has rank 8; on the history once, at $x_4 = 3\ln(5/9)/H \approx -1.7634/H$ | PROVED, in the diagonal vielbein (scope: Section 6.29); the time COMPUTED by Notebook 06a, In [20] | `python-field-theory.json`, check `gravity_term_square`; `wolfram-field-theory.json`, checks `nontriviality_1_dirac16complex`, `nontriviality_2_dirac16complex00` |
| negative control: $\frac32He^{-a_4}b_4^{-1/2}\gamma^{(x0)} + (b_4'/b_4 + \frac72a_4')\gamma^{(x4)}$ for a growing hidden block | PROVED | lead report, check `negative_control_growing_block`; Notebook 06a, In [22] |

### 6.11 Example: Notebook 06a

Notebook 06a puts Sections 6.2 to 6.10 to work with exact algebra. It reads the author's eight gammas from the record `Revision/algebra/gammas.json`, checks the Clifford relations, and defines four general functions (Christoffel symbols, canonical spin connection, spinor connection, curved gammas) that work in any number of dimensions. It first applies them to the polar plane of Section 6.5 and draws the turning frame and the half-angle spinor rotation. Then it builds the corrected metric with arbitrary functions $a_4(x_4)$ and $b_4(x_4)$ and with the warp factor $W$ written as a function that knows only its derivative rule $\partial_0W = H\cot z\,W$, so that every result holds for every real $z$; and it computes, exactly: the vielbein, the volume factor, the 21 Christoffel symbols, the 10 components of the spin connection, the 512 equations of the vielbein postulate, $\Omega_\mu$, the covariant constancy of the gammas, the eight terms $\gamma^\mu\Omega_\mu$ and their sum $c_g\gamma^{(x0)} + v_g\gamma^{(x4)}$, the divergence form, the Dirac operator for sixteen arbitrary component functions, the square of the term and the time at which it degenerates on the history, and the negative control. It compares every result that the Revision records also contain with the records (all for the corrected metric), evaluates the contraction on the history of the record, draws ten figures, needs no Rust, runs in about a minute and ends with the line ALL 40 CHECKS PASSED (notebook 06a).

<!-- NOTEBOOK 06a -->

### 6.14 Line-by-line walk-through of Notebook 06a

The notebook has 24 code cells, In [1] to In [24]. This section explains every line of every one of them, in order: a line or a small group of lines is quoted and then explained. A line that starts with `#` is a **comment**, which Python skips; it is there for the reader. In a quoted figure cell a line `...` stands for the remaining lines of a long caption; every caption is printed in full under its figure in Section 6.13, and a paragraph "What Figure 06a.k shows" after the code says what to look for and why. The words of the notebook are those of its section 3 (Section 6.13), which Sections 6.1 to 6.7 defined. The printed output of In [k] is shown in Section 6.13 under the label Out [k].

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
NAMES = fixture["coordinates"]  # ["x0", ..., "x7"], the names of the directions
ETA = fixture["eta"]  # the frame metric: +1 space-like, -1 time-like
```

`GAMMA_FILE` names the Revision record of the gammas. `read_text` reads the file as text and `json.loads` turns the text into Python objects: `fixture` is a dictionary whose keys are the names stored in the record. `fixture["coordinates"]` is the list `["x0", ..., "x7"]`, and `fixture["eta"]` the list of the diagonal entries of $\eta$.

```python
# Each gamma is stored as 16 rows of 16 whole numbers; sp.Matrix makes it an exact
# sympy matrix.  gamma[a] is the gamma of the direction NAMES[a].
gamma = [sp.Matrix(rows) for rows in fixture["gamma"]]
I16 = sp.eye(16)  # the 16 x 16 identity matrix
Z16 = sp.zeros(16, 16)  # the 16 x 16 zero matrix
say(f"directions: {NAMES}")
say(f"eta (frame metric): {ETA}")
```

Each gamma is stored as 16 rows of 16 whole numbers; `sp.Matrix(rows)` turns it into an exact sympy matrix. The **list comprehension** `[... for rows in ...]` builds the list of the eight matrices in one line, so `gamma[0]` is $\gamma^{(x0)}$, `gamma[1]` is $\gamma^{(x1)}$ and `gamma[4]` is $\gamma^{(x4)}$ (Python counts from 0, and the record lists the gammas in the order $x0, \dots, x7$). `sp.eye(16)` is the identity matrix and `sp.zeros(16, 16)` the zero matrix. The two `say` lines print the directions and the signs of $\eta$, the first two output lines.

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

**In [3], the helpers and the records.**

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
def read_formulas(path):
    """The formulas of a record as a dictionary key -> text (or list of texts)."""
    data = json.loads(repository_file(path).read_text(encoding="utf-8"))
    return {item["key"]: item["wl"] for item in data["formulas"]}
```

`read_formulas(path)` reads a record that holds a list `formulas`, each with a key and the formula as Wolfram text (`wl`; a list of texts for a formula with several parts, such as the sixteen component equations of In [20]). The **dictionary comprehension** `{item["key"]: item["wl"] for item in ...}` builds the dictionary from key to text in one line.

```python
THEORY_FILE = "Revision/theory/field-theory.json"  # the record, corrected metric
FORMULAS = read_formulas(THEORY_FILE)
# The roots of sin^2 z as the record writes them, and the same root as a power of
# warp = W = (sin^2 z)^(1/12):  |sin z|^(1/3) = (sin^2 z)^(1/6) = W^2.
ROOTS = (("(Sin[6*H*x0]^2)^(1/12)", "warp"), ("(Sin[6*H*x0]^2)^(1/6)", "warp^2"),
         ("(Sin[6*H*x0]^2)^(1/4)", "warp^3"), ("Abs[Sin[6*H*x0]]^(1/3)", "warp^2"))
```

`THEORY_FILE` names the record of the field theory, written for the corrected metric, and `FORMULAS` holds its formulas. The record writes the warp factor and its powers as roots of $\sin^2 z$: $(\sin^2 z)^{1/12} = W$, $(\sin^2 z)^{1/6} = W^2$, $(\sin^2 z)^{1/4} = W^3$, and in one formula $\lvert\sin z\rvert^{1/3}$, which is $(\sin^2 z)^{1/6} = W^2$ as well (because $\lvert\sin z\rvert = (\sin^2 z)^{1/2}$ and $\frac12\cdot\frac13 = \frac16$). The **tuple** `ROOTS` (a fixed list written with round brackets) pairs each of these texts with the same root written as a power of the name `warp`.

```python
def wolfram_to_sympy(text, names):
    """A text in Wolfram notation as a sympy expression.  names maps the record's
    symbol names (texts) to the symbols and functions of this notebook."""
    # The roots first, then a4', a4'', a4(x4) and the same for b4, which the record
    # writes as Derivative[1][a4][x4], Derivative[2][a4][x4], a4[x4], ...
    for long_form, short_form in ROOTS + (("Derivative[1][a4][x4]", "a4p"),
                                          ("Derivative[2][a4][x4]", "a4pp"),
                                          ("Derivative[1][b4][x4]", "b4p"),
                                          ("Derivative[2][b4][x4]", "b4pp"),
                                          ("a4[x4]", "a4"), ("b4[x4]", "b4")):
        text = text.replace(long_form, short_form)
    if "Sin[6*H*x0]^2" in text or "Abs[" in text:  # a root that was not translated
        raise ValueError(f"cannot translate {text}")
    expr = parse_mathematica(text)
    return expr.subs({sp.Symbol(name): value for name, value in names.items()},
                     simultaneous=True)
```

`wolfram_to_sympy(text, names)` turns a text in Wolfram notation into a sympy expression. The loop first replaces the four roots by powers of `warp`, then $a_4'$, $a_4''$ and $a_4(x_4)$, which the record writes as `Derivative[1][a4][x4]`, `Derivative[2][a4][x4]` and `a4[x4]`, and the same for $b_4$, by the short names `a4p`, `a4pp`, `b4p`, `b4pp`, `a4` and `b4` (`text.replace(old, new)` replaces every occurrence; the derivatives come before `a4[x4]`, which they contain; `ROOTS + (...)` joins two tuples). If a root of $\sin^2 z$ or an absolute value is still left, the text holds a form the notebook does not know, and `raise ValueError` stops the notebook instead of reading it wrongly. `parse_mathematica` reads the text, and `.subs({...}, simultaneous=True)` replaces each plain symbol of the record by the symbol or function of the notebook that the dictionary `names` gives for it, all at the same time. In this way the record's twelfth root becomes the function $W$ of In [7], which knows its derivative for every real $z$.

```python
def record_formula(key, names):
    """The formula key of the record field-theory.json as a sympy expression."""
    return wolfram_to_sympy(FORMULAS[key], names)
```

`record_formula(key, names)` does this for one formula of the record, the one stored under `key`.

```python
REPORT_PY = "Revision/theory/reports/python-field-theory.json"
REPORT_WL = "Revision/theory/reports/wolfram-field-theory.json"
REPORT_LEAD = "Revision/lead_checks/reports/emt-divergence-and-spin-connection.json"
PARAMETERS = "Revision/kohn_sham/results/parameters.json"
physics = json.loads(repository_file(PARAMETERS).read_text(encoding="utf-8"))["physics"]
A_value, beta = physics["historyA"], physics["historyBeta"]  # the record's history
b4_zero = physics["historyB4AtZero"]  # the value b4(0)
A_EXACT, BETA = sp.nsimplify(A_value), sp.nsimplify(beta)  # 1 and 4/3 as fractions
B4_ZERO = sp.nsimplify(b4_zero)  # b4(0) = 1 as an exact number
```

Names for the three Revision reports that the notebook reproduces (the sympy report, the WolframScript report and the lead's report); then the history of the Revision record from `parameters.json`: `physics` is the part of the record with the physical parameters, `A_value` the slope $A$, `beta` the exponent $\beta$ of $b_4 = b_4(0)\,e^{\beta AHx_4}$ and `b4_zero` the value $b_4(0)$; `sp.nsimplify` writes the stored decimal numbers 1.0, 1.333333333333333 and 1.0 as the exact fractions $1$, $4/3$ and $1$, so that the algebra below stays exact.

```python
say(f"{len(FORMULAS)} formulas read from {THEORY_FILE}")
say(f"history of the record: slope A = {A_value}, beta = {beta:.6f}, b4(0) = "
    f"{b4_zero} (a4 = A H x4, b4 = b4(0) e^(beta A H x4))")
check(A_EXACT == 1 and BETA == sp.Rational(4, 3) and B4_ZERO == 1,
      "the history of the record has A = 1, beta = 4/3 and b4(0) = 1",
      record=f"{PARAMETERS}, physics.historyA, historyBeta and historyB4AtZero")
```

Two output lines, 33 formulas read from Revision/theory/field-theory.json and the history (slope A = 1.0, beta = 1.333333, b4(0) = 1.0; in an f-string `{beta:.6f}` prints a number with six decimals), and the check that the history has $A = 1$, $\beta = 4/3$ and $b_4(0) = 1$, which names the three keys of the record.

**In [4], four general formulas as Python functions.** The four functions work for any number of dimensions and any vielbein, so the same code serves the plane and the eight-dimensional corrected metric.

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
removed = U.inv() * plane_Omega[1] * U - U.inv().diff(phi) * U  # frame change U^-1
check(F_rphi == sp.zeros(2, 2) and matrix_is_zero(pure_gauge)
      and matrix_is_zero(removed),
      "polar plane: flat (F_rphi = 0), Omega_phi = -(dU/dphi) U^-1, U^-1 removes it")
```

`F_rphi` is the curvature $\partial_r\Omega_\varphi - \partial_\varphi\Omega_r + [\Omega_r, \Omega_\varphi]$ (`.diff(r)` differentiates every entry). `U` is the spinor rotation $\cos\frac\varphi2 + i\sin\frac\varphi2\,\sigma_3$, and `pure_gauge` is $-(\partial_\varphi U)U^{-1} - \Omega_\varphi$ (`U.inv()` is the inverse matrix): it vanishes when $\Omega_\varphi$ is what the rule $R\,\Omega R^{-1} - (\partial_\varphi R)R^{-1}$ of a change of frame makes from the connection 0 of the Cartesian frame with $R = U$. `removed` is that rule applied to $\Omega_\varphi$ with $R = U^{-1}$, whose inverse is $U$: $U^{-1}\Omega_\varphi U - (\partial_\varphi U^{-1})U$, the connection of the frame obtained by turning the polar frame back with $U^{-1}$ (Section 6.5 worked it by hand). The fifth check requires all three to be zero: the plane is flat, its spin connection is only the turning of the frame, and the inverse rotation $U^{-1}$ removes it. The cell prints five PASS lines.

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

The right panel draws the entry $U_{11} = \cos\frac\varphi2 + i\sin\frac\varphi2$ of the spinor rotation $U$ (the rotation that carries the Cartesian frame into the polar frame; its inverse $U^{-1}$ removes the connection, Section 6.5) for 400 values of $\varphi$ from $0$ to $4\pi$: its real part $\cos(\varphi/2)$ as a solid line and its imaginary part $\sin(\varphi/2)$ dashed (the style string of two minus signs). The horizontal axis shows $\varphi/\pi$, so the full turn is at 2 and the double turn at 4. In the labels `\\` is a single backslash for matplotlib's formula typesetting.

```python
save_figure(fig, "polar_frame_and_spin_rotation",
            "Warm-up in the flat plane. Left: the unit radial direction (black) and "
            ...
            "rotation is $-1$, and only at $4\\pi$ is it $+1$ again.")
```

`save_figure` saves the figure with its caption, shows it and prints one line with the name of the saved file, `06a_1_polar_frame_and_spin_rotation.png` in the folder `Revision/textbook/figures`.

**What Figure 06a.1 shows.** On the left, the black and orange arrows turn together as one goes around the circle: the polar frame at the angle $\varphi$ is the Cartesian frame turned by $\varphi$. That turning is exactly what $\omega_{\varphi01} = -1$ records, although the plane is flat; the spinor rotation $U(\varphi)$ performs the same turning on spinors, and its inverse $U^{-1}$ turns it back and removes the connection. On the right, the solid curve $\cos(\varphi/2)$ reaches $-1$ at $\varphi = 2\pi$ (the value 2 on the axis), where the dashed curve is 0: after one full turn the spinor rotation is $-1$, and only at $4\pi$ is it $+1$ again. A spinor turns by half the angle of its frame.

**In [7], the corrected metric and its vielbein** (Section 6.2).

```python
x = sp.symbols("x0:8", real=True)  # x[0] = x0, ..., x[4] = x4, ..., x[7] = x7
x0, x4 = x[0], x[4]  # the hidden direction and the time
H = sp.Symbol("H", positive=True)  # the author's constant H > 0
a4 = sp.Function("a4")(x4)  # the metric function a4(x4): any function of the time
b4 = sp.Function("b4", positive=True)(x4)  # the metric function b4(x4) > 0
z = 6 * H * x0  # the hidden coordinate z = 6 H x0, every real value
```

`sp.symbols("x0:8", real=True)` makes the eight real symbols `x0`, ..., `x7` in one call and returns them as a tuple `x`, so `x[0]` is $x_0$ and `x[4]` is $x_4$; the second line gives the two that the metric depends on their own names. `H` is a positive symbol. `sp.Function("a4")(x4)` is an unknown function $a_4$ of $x_4$ (nothing else is assumed about it), and `b4` is an unknown function that sympy knows to be positive. `z` is the expression $6Hx_0$; no range is assumed for it, so $z$ takes every real value.

```python
class W(sp.Function):
    """The warp factor W(x0) = (sin(6 H x0)^2)^(1/12) > 0 of the extra times."""

    def fdiff(self, argindex=1):
        """dW/dx0 = H cot(6 H x0) W, for every real z = 6 H x0 with sin z != 0."""
        return H * sp.cot(6 * H * self.args[0]) * self

    def _eval_is_positive(self):
        return True  # the positive root
```

This defines the warp factor $W(x_0) = (\sin^2 z)^{1/12}$ as a new sympy function. A **class** is a blueprint for a kind of object; `class W(sp.Function)` makes a new kind of sympy function, of which `W(x0)` is one value. sympy knows nothing about `W` except the two facts given here: the method `fdiff` (the derivative of the function with respect to its argument) returns $H\cot(6Hx_0)\,W$, and `_eval_is_positive` says that $W$ is positive. Why not write $(\sin^2 z)^{1/12}$ directly? Because sympy then has to handle the root of $\sin^2 z$ in every simplification, which is slow, and simplifications of roots are valid only for some values of $z$ unless sympy is told much more. The derivative rule is all that the spin connection and the curvature need, and it holds for every real $z$ with $\sin z \neq 0$ (the next line checks it), so every result of the notebook holds for every real $z$, on both halves of every cell.

```python
G = sp.Symbol("G", real=True)  # the sign of cot z (+1 or -1): |cot z| = G cot z
explicit = (sp.sin(z) ** 2) ** sp.Rational(1, 12)  # the twelfth root, written out
check(is_zero(sp.diff(explicit, x0) - H * sp.cot(z) * explicit),
      "the derivative of (sin^2 z)^(1/12) is H cot z (sin^2 z)^(1/12): the rule of W")
```

`G` is a real symbol for the sign of $\cot z$, used to compare with the record, which writes $\lvert\cot z\rvert$ as `rftSig` times $\cot z$. `explicit` is the twelfth root written out, and the check proves exactly that its derivative is $H\cot z$ times itself, the rule given to $W$: the derivative of $(\sin^2 z)^{1/12}$ is $\frac1{12}(\sin^2 z)^{-11/12}\cdot2\sin z\cos z\cdot6H = H\frac{\cos z}{\sin z}(\sin^2 z)^{1/12}$ (the power rule and the chain rule twice; $\frac{2\cdot6}{12} = 1$ and $(\sin^2 z)^{-11/12} = (\sin^2 z)^{1/12}/\sin^2 z$).

```python
s_b = sp.exp(-a4) * sp.sqrt(b4)  # the hidden scale e^(-a4) b4^(1/2)
f = ([s_b * sp.cot(z)] + [sp.exp(a4)] * 3 + [sp.Integer(1)]
     + [s_b * W(x0)] * 3)  # f_0, ..., f_7
g = sp.diag(*[ETA[a] * f[a] ** 2 for a in range(8)])  # g_aa = eta_aa f_a^2
e = sp.diag(*f)  # the diagonal vielbein e^a_mu = f_a delta^a_mu
```

`s_b` is the hidden scale $e^{-a_4}b_4^{1/2}$ (`sp.sqrt` is the square root). `f` is the list of the eight vielbein factors of Section 6.2: `[s_b * sp.cot(z)]` is the list with the one entry $f_0 = s_b\cot z$, `[sp.exp(a4)] * 3` the list of three entries $e^{a_4}$, and `+` joins lists. `g` is the diagonal matrix with the entries $\eta_{aa}f_a^2$ (`sp.diag(*list)` puts the entries of the list on the diagonal), and `e` the diagonal vielbein.

```python
# The names under which the records write symbols, and our symbols for them:
RECORD_NAMES = {"H": H, "x4": x4, "x0": x0, "a4": a4, "b4": b4, "warp": W(x0),
                "rftSig": G, "a4p": sp.Derivative(a4, x4),
                "a4pp": sp.Derivative(a4, (x4, 2)), "b4p": sp.Derivative(b4, x4),
                "b4pp": sp.Derivative(b4, (x4, 2))}
```

The dictionary `RECORD_NAMES` says which symbol or function of the notebook each name of the record stands for: `"warp"` is $W(x_0)$ (In [3] turned the record's roots into powers of `warp`), `"rftSig"` is the sign $G$, and the derivatives are written with `sp.Derivative` (`(x4, 2)` means the second derivative).

```python
metric_record = sp.Matrix([list(row) for row in record_formula("metric", RECORD_NAMES)])
check(matrix_is_zero(g - metric_record)
      and record_passed(REPORT_WL, "metric_is_the_corrected_metric")
      and record_passed(REPORT_PY, "metric_from_vielbein_equals_SPEC"),
      "eta_aa f_a^2 is the corrected metric (all 64 entries)",
      record=f"{THEORY_FILE}, formula metric")
```

The record's formula `metric` is a list of eight rows; `sp.Matrix([list(row) for row in ...])` makes it a sympy matrix. The check requires $g$ minus the record's matrix to vanish in all 64 entries, and the two reports to record their metric checks as passed.

```python
f_record = record_formula("vielbein_diagonal", RECORD_NAMES)
check(all(is_zero(f[a] - f_record[a]) for a in range(8))
      and record_passed(REPORT_LEAD, "vielbein_reproduces_metric"),
      "the eight vielbein factors of the record",
      record=f"{THEORY_FILE}, formula vielbein_diagonal")
```

The record's eight vielbein factors are read as a list; the check requires them to equal the notebook's, factor by factor, and the lead's independent report to record `vielbein_reproduces_metric` as passed.

```python
volume = sp.simplify(sp.prod(f))  # f_0 f_1 ... f_7, with the sign of cot z
say(f"f_0 f_1 ... f_7 = {volume}")
volume_record = record_formula("sqrt_det_g", RECORD_NAMES)
check(is_zero(G * volume - volume_record) and is_zero(volume**2 - g.det())
      and record_passed(REPORT_WL, "sqrt_det_g")
      and record_passed(REPORT_PY, "sqrt_det_g"),
      "sqrt|det g| = G f_0 f_1 ... f_7 = e^(-a4) b4^2 |cot z| (sin^2 z)^(1/4)",
      record=f"{THEORY_FILE}, formula sqrt_det_g")
```

`sp.prod(f)` multiplies the eight factors, and `sp.simplify` writes the product in a short form; the cell prints it as `f_0 f_1 ... f_7 = W(x0)**3*b4(x4)**2*exp(-a4(x4))*cot(6*H*x0)`, which is $e^{-a_4}b_4^2\cot z\,W^3$ of Section 6.2 (`**` is the power in Python). The check requires $G$ times this product to equal the record's `sqrt_det_g`, the square of the product to equal the determinant of $g$ (`g.det()`), and both reports to record `sqrt_det_g` as passed. The cell prints the rule check, three more PASS lines with their records, and the product.

**In [8], figure 2: the vielbein factors.**

```python
X4_SYMBOL = sp.Symbol("t", real=True)  # the time x4 as a plain symbol for numbers
history = {a4: A_EXACT * X4_SYMBOL,  # the record's history with H = 1, b4(0) = 1
           b4: B4_ZERO * sp.exp(BETA * A_EXACT * X4_SYMBOL)}


def explicit_warp(expr):
    """expr with W(x0) replaced by the explicit |sin z|^(1/6) (for numbers)."""
    return sp.sympify(expr).subs(W(x0), sp.Abs(sp.sin(z)) ** sp.Rational(1, 6))
```

For numbers the history is inserted with $H = 1$: `X4_SYMBOL` is a plain symbol $t$ for the time, and `history` replaces $a_4$ by $A\,t$ and $b_4$ by $b_4(0)\,e^{\beta At}$ with the record's values $A = 1$, $\beta = 4/3$, $b_4(0) = 1$. `explicit_warp` replaces the function $W(x_0)$ by the explicit $\lvert\sin z\rvert^{1/6}$, so that a number can be computed (`sp.Abs` is the absolute value).

```python
# the eight factors and the volume factor (positive at z = pi/4) at z = 6 x0 = pi/4
f_of_time = sp.lambdify(X4_SYMBOL, [explicit_warp(fa.subs(history)).subs(
    {H: 1, x0: sp.pi / 24}) for fa in f + [volume]])
times = np.linspace(-2.0, 2.0, 201)
values = [np.broadcast_to(v, times.shape) for v in f_of_time(times)]
```

`f + [volume]` is the list of the eight factors and the product of In [7]. In each, the history is inserted, $W$ is written out, and $H = 1$, $x_0 = \pi/24$ ($z = \pi/4$) are set; `sp.lambdify(X4_SYMBOL, [...])` turns the list of expressions into one Python function of $t$ that computes all nine numbers quickly with numpy. `times` holds 201 times from $-2$ to $2$, and `np.broadcast_to` turns a constant result (such as $f_4 = 1$) into an array of the same length.

```python
fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10.0, 4.4))
ax_left.semilogy(times, values[1], label="$f_1 = f_2 = f_3 = e^{a_4}$ (3-space)")
ax_left.semilogy(times, values[0], "--", label="$f_0 = s_b\\cot z$ (hidden)")
ax_left.semilogy(times, values[5], "-.",
                 label="$f_5 = f_6 = f_7 = s_bW$ (extra times)")
ax_left.semilogy(times, values[4], ":", color="black", label="$f_4 = 1$ (time)")
ax_left.semilogy(times, values[8], color="gray", linewidth=2.5, alpha=0.6,
                 label="$\\sqrt{|\\det g|}$ (7-volume factor)")
ax_left.set_xlabel("time $x_4$ (units $1/H$), history $a_4 = x_4$, "
                   "$b_4 = e^{4x_4/3}$")
ax_left.set_ylabel("factor at $z = \\pi/4$ (logarithmic axis)")
ax_left.set_title("Inflating 3-space, deflating hidden block")
ax_left.legend(fontsize=7)
```

The left panel draws, on a logarithmic vertical axis (`semilogy`, on which an exponential function is a straight line), the 3-space factor $e^{a_4}$ (solid), the hidden factor $s_b\cot z$ (dashed), the extra-time factor $s_bW$ (dash-dotted), the time factor 1 (dotted, black) and the volume factor (thick gray line, `alpha=0.6` makes it partly transparent).

```python
zz = np.linspace(0.02, np.pi - 0.02, 400)  # z inside one cell (0, pi)
ax_right.plot(zz, np.abs(np.sin(zz)) ** (1 / 6), label="$W = (\\sin^2 z)^{1/12}$")
ax_right.plot(zz, np.abs(1 / np.tan(zz)), "--", label="$|f_0|/s_b = |\\cot z|$")
ax_right.plot(zz, np.abs(1 / np.tan(zz)) * np.abs(np.sin(zz)) ** 0.5, ":",
              color="black", label="$\\sqrt{|\\det g|}/(e^{-a_4}b_4^2)$")
ax_right.axvline(np.pi / 2, color="gray", linewidth=0.8)  # the fold
ax_right.set_ylim(0.0, 3.0)
ax_right.set_xlabel("hidden angle $z = 6 H x_0$ (radians), fold at $\\pi/2$")
ax_right.set_ylabel("factor (pure number)")
ax_right.set_title("Dependence on the hidden direction")
ax_right.legend(fontsize=8, loc="upper center")
```

The right panel draws three functions of the hidden angle over one cell, $0.02 \le z \le \pi - 0.02$: the warp factor $W = \lvert\sin z\rvert^{1/6}$, the hidden factor divided by $s_b$, $\lvert\cot z\rvert$, and the volume factor divided by $e^{-a_4}b_4^2$, $\lvert\cot z\rvert\,\lvert\sin z\rvert^{1/2}$; `axvline` draws a vertical line at the fold $z = \pi/2$, and the vertical axis is cut at 3.

```python
save_figure(fig, "vielbein_factors",
            "The factors $f_a$ of the diagonal vielbein of the corrected metric. "
            ...
            "which both vanish at the fold $z = \\pi/2$ (vertical line).")
```

The figure is saved as `06a_2_vielbein_factors.png`.

**What Figure 06a.2 shows.** On the left, the 3-space factor rises along a straight line (on a logarithmic axis an exponential is a straight line), while the hidden factor and the extra-time factor fall along two parallel straight lines with one third of that slope: on the history $s_b = e^{-x_4/3}$, so the hidden direction and the extra times deflate together. The time factor is 1, and the gray volume factor rises with the slope $\frac53$: the 7-volume grows like $e^{5x_4/3}$ (Section 6.2). On the right, as functions of the hidden angle: $W$ rises from 0 at the tips to 1 at the fold, while $\lvert\cot z\rvert$ and the volume factor fall from very large values at the tips to 0 at the fold, symmetrically on the two halves of the cell.

**In [9], the 21 Christoffel symbols** (Section 6.3).

```python
Gam = christoffel(g, x)
independent = {(l, m, n): Gam[l][m][n] for l in range(8) for m in range(8)
               for n in range(m, 8) if Gam[l][m][n] != 0}
report("number of independent nonzero Christoffel symbols", len(independent))
```

`christoffel(g, x)` computes all $8 \cdot 8 \cdot 8 = 512$ symbols. The dictionary `independent` keeps those with $m \le n$ (`range(m, 8)`) that are not zero, under the key `(l, m, n)`. `report` prints their number, 21.

```python
def as_dictionary(entries):
    """{l, m, n, value} entries of a record (numbered from 1) -> {(l, m, n): value}
    with Python's numbers 0 to 7."""
    return {(int(l) - 1, int(m) - 1, int(n) - 1): value for l, m, n, value in entries}


record_gamma = as_dictionary(record_formula("christoffel_nonzero", RECORD_NAMES))
same = set(record_gamma) == set(independent) and all(
    is_zero(independent[key] - record_gamma[key]) for key in independent)
```

The record's list `christoffel_nonzero` has entries $\{l, m, n, \text{value}\}$ with the directions numbered from 1 in the order $x0, \dots, x7$ (the number 1 is $x0$); `as_dictionary` subtracts 1 to get Python's positions. `set(record_gamma) == set(independent)` requires the same 21 keys on both sides (a **set** is a collection without order), and `all(...)` requires every value to agree exactly.

```python
for key in [(1, 1, 4), (5, 4, 5), (0, 0, 4), (5, 0, 5), (4, 5, 5), (0, 5, 5),
            (0, 0, 0)]:
    l, m, n = key
    say(f"Gamma^{NAMES[l]}_{NAMES[m]}{NAMES[n]} = {independent[key]}")
check(len(independent) == 21 and same and record_passed(REPORT_WL, "christoffel_count"),
      "the 21 independent nonzero Christoffel symbols equal the record",
      record=f"{THEORY_FILE}, formula christoffel_nonzero")
```

Seven symbols are printed, one per line: $\Gamma^{x1}{}_{x1x4} = a_4'$ (3-space grows at the rate $a_4'$), $\Gamma^{x5}{}_{x4x5}$ and $\Gamma^{x0}{}_{x0x4}$, both equal to $-a_4' + b_4'/(2b_4) = h_4$ (the extra time and the hidden direction change at the same rate), $\Gamma^{x5}{}_{x0x5} = H\cot z$ (the warp), $\Gamma^{x4}{}_{x5x5}$, printed as `(b4(x4)*Derivative(a4(x4), x4) - Derivative(b4(x4), x4)/2)*W(x0)**2*exp(-2*a4(x4))`, which is $-e^{-2a_4}b_4W^2h_4$, $\Gamma^{x0}{}_{x5x5} = HW^2\tan z$ and $\Gamma^{x0}{}_{x0x0} = -12H/\sin(12Hx_0)$: exactly the values of Section 6.3. The check requires 21 symbols, agreement with the record, and the WolframScript report's `christoffel_count` as passed.

**In [10], figure 3: where the Christoffel symbols live.**

```python
SAMPLE = {H: 1, x0: sp.pi / 24}  # H = 1 and z = 6 H x0 = pi/4
B4_SAMPLE = sp.exp(sp.Rational(2, 3))  # b4 at a4 = 1/2 on the history, b4(0) = 1


def at_sample(expr):
    """The decimal value of expr at the sample point H = 1, z = pi/4 on the history
    of the record: a4 = 1/2, a4' = 1, a4'' = 0, b4 = e^(2/3), b4' = (4/3) b4,
    b4'' = (16/9) b4 (derivatives are replaced first, then the functions)."""
    expr = sp.sympify(expr)
    rate = sp.Rational(4, 3)  # b4'/b4 = beta a4'
    for function, second, first in ((a4, 0, 1),
                                     (b4, rate**2 * B4_SAMPLE, rate * B4_SAMPLE)):
        expr = expr.subs(sp.Derivative(function, (x4, 2)), second)
        expr = expr.subs(sp.Derivative(function, x4), first)
    expr = explicit_warp(expr.subs({a4: sp.Rational(1, 2), b4: B4_SAMPLE}))
    return complex(sp.N(expr.subs(SAMPLE)))
```

The **sample point** of the figures is $H = 1$, $z = \pi/4$ ($x_0 = \pi/24$) on the history of the record at $a_4 = \frac12$: there $a_4' = 1$, $a_4'' = 0$, $b_4 = e^{2/3}$ (because $b_4 = e^{4a_4/3}$), $b_4' = \frac43b_4$ and $b_4'' = \frac{16}{9}b_4$ (the chain rule once and twice). `at_sample` inserts these values: first the second and the first derivatives (if the functions were replaced first, their derivatives would become derivatives of a constant, which are zero), then $a_4$ and $b_4$, then the explicit warp factor, and `sp.N` computes the decimal number, returned as a complex number (`complex(...)`; all values here are real, and `.real` below takes the real part).

```python
fig, axes = plt.subplots(2, 4, figsize=(10.0, 5.6))
for l, ax in enumerate(axes.flat):
    signs = np.array([[np.sign(at_sample(Gam[l][m][n]).real) for n in range(8)]
                      for m in range(8)])
    ax.imshow(signs, cmap="RdBu_r", vmin=-1.5, vmax=1.5)
    ax.set_title(f"$\\Gamma^{{x{l}}}{{}}_{{mn}}$", fontsize=9)
    ax.set_xticks(range(8), [f"{k}" for k in range(8)], fontsize=7)
    ax.set_yticks(range(8), [f"{k}" for k in range(8)], fontsize=7)
    ax.set_xlabel("$n$ (x-number)", fontsize=7)
    ax.set_ylabel("$m$ (x-number)", fontsize=7)
    ax.grid(False)
fig.suptitle("Signs of the Christoffel symbols at a sample point "
             "(red +, blue -, white 0)", fontsize=10)
fig.tight_layout()
```

`plt.subplots(2, 4)` makes eight small panels in two rows, one for each upper index `l`; `enumerate(axes.flat)` numbers them 0 to 7. For each panel an $8 \times 8$ table of the signs $+1$, $-1$ or $0$ of $\Gamma^l{}_{mn}$ at the sample point is computed (`np.sign`) and drawn by `imshow` as a picture whose squares are coloured with the colour map `"RdBu_r"` (red for positive, blue for negative, white for zero). The tick labels number the rows and columns 0 to 7, the numbers of the directions $x0$ to $x7$; `ax.grid(False)` removes the grid lines; `fig.suptitle` puts a title above all panels and `fig.tight_layout()` arranges them without overlap. In the title string the doubled braces `{{` and `}}` print single braces inside an f-string.

```python
save_figure(fig, "christoffel_pattern",
            "Where the Christoffel symbols $\\Gamma^l{}_{mn}$ of the corrected metric "
            ...
            "$\\Gamma^l{}_{mn} = \\Gamma^l{}_{nm}$.")
```

The figure is saved as `06a_3_christoffel_pattern.png`.

**What Figure 06a.3 shows.** Every coloured square lies in row 0 or 4, in column 0 or 4, or in a panel $l = x0$ or $l = x4$: every nonzero symbol carries an index $x0$ or $x4$, because the metric depends only on the hidden coordinate and on the time. Each grid is mirror-symmetric about its diagonal, because $\Gamma^l{}_{mn} = \Gamma^l{}_{nm}$. In the panels $l = x1, x2, x3$ the two squares with the index 4 are red ($a_4' > 0$: 3-space grows), and there is no square with the index 0 (3-space has no warp). In the panels $l = x5, x6, x7$ the two squares with the index 4 are blue ($h_4 = -1 + \frac23 = -\frac13$ at the sample point: the extra times shrink), and the two squares with the index 0 are red ($H\cot z = 1$). The panel $l = x0$ has blue squares $(0, 4)$ and $(4, 0)$ (the hidden direction shrinks at the same rate $h_4$), red squares for the three extra times ($HW^2\tan z$) and one blue square at $(0, 0)$ ($-12H/\sin 2z = -12$). The panel $l = x4$ has red squares on the diagonal for the three 3-space directions ($e^{2a_4}a_4'$) and for the three extra times ($-e^{-2a_4}b_4W^2h_4 > 0$), and a blue square at $(0, 0)$ ($e^{-2a_4}b_4\cot^2 z\,h_4 < 0$), as the signs derived in Section 6.3 say.

**In [11], the spin connection** (Sections 6.4 and 6.6).

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

The nonzero components with $a < b$ are collected and printed, one line each (a long line continues, indented, on the next): ten lines, for example

```text
omega_x0,x0x4 = (-2*b4(x4)*Derivative(a4(x4), x4) + Derivative(b4(x4),
    x4))*exp(-a4(x4))*cot(6*H*x0)/(2*sqrt(b4(x4)))
```

which is $\big(\frac{b_4'}{2b_4} - a_4'\big)e^{-a_4}b_4^{1/2}\cot z = h_4\,s_b\cot z$ (multiply numerator and denominator by $1/b_4$: $\frac{-2b_4a_4' + b_4'}{2b_4^{1/2}} = b_4^{1/2}\big(\frac{b_4'}{2b_4} - a_4'\big)$), the line `omega_x1,x1x4 = exp(a4(x4))*Derivative(a4(x4), x4)`, which is $a_4'e^{a_4}$, the line `omega_x5,x0x5 = H*W(x0)` and the line of $\omega_{x5\,x4x5} = h_4s_bW$: exactly the table of Section 6.6.

```python
omega_record = as_dictionary(record_formula("omega_nonzero", RECORD_NAMES))
check(len(omega_nonzero) == 10 and set(omega_record) == set(omega_nonzero)
      and all(is_zero(omega_nonzero[k] - omega_record[k]) for k in omega_nonzero),
      "the 10 independent nonzero omega_mu ab equal the record",
      record=f"{THEORY_FILE}, formula omega_nonzero")
```

The record's list `omega_nonzero` has entries $\{\mu, a, b, \text{value}\}$, numbered from 1 as before. The check requires exactly 10 components, the same keys as the record and the same values.

```python
a4p, b4p = sp.Derivative(a4, x4), sp.Derivative(b4, x4)
h4 = b4p / (2 * b4) - a4p  # the rate of the hidden scale s_b
```

`a4p` and `b4p` are short names for $a_4'$ and $b_4'$, and `h4` is the rate $h_4 = b_4'/(2b_4) - a_4'$.

```python
rates = (a4p, h4, H)  # 3-space, the hidden block, the warp
factors = [sign * phys for sign in (1, -1)
           for phys in (sp.exp(a4), s_b * sp.cot(z), s_b * W(x0), W(x0))]
# value / (rate * factor) must simplify to exactly 1 for one choice of each.
shape_ok = all(any(sp.simplify(value / (rate * phys)) == 1 for rate in rates
                   for phys in factors) for value in omega_nonzero.values())
check(shape_ok and record_passed(REPORT_WL, "omega_components")
      and record_passed(REPORT_WL, "Omega_vanishes_iff_a4prime_b4prime_and_H_vanish"),
      "every nonzero omega is a4', h4 or H times +-e^(a4), s_b cot z, s_b W or W",
      record=f"{REPORT_WL}, checks omega_components and "
             "Omega_vanishes_iff_a4prime_b4prime_and_H_vanish")
```

The last check confirms the structure stated in Section 6.6: every nonzero component is one of the three rates $a_4'$, $h_4$ or $H$ (`rates`) times one of the factors $\pm e^{a_4}$, $\pm s_b\cot z$, $\pm s_bW$ or $\pm W$ (`factors`, built by a list comprehension over the two signs and the four factors). For each component, `any(...)` tries all $3 \cdot 8 = 24$ products and is true when the quotient simplifies to exactly 1 for one of them. Since none of the factors vanishes between the degenerate points, a component vanishes only when its rate does; the check also requires the two record checks that state this. The cell prints three PASS lines with their records and the ten components.

**In [12], figure 4: the spin connection as heat maps.**

```python
fig, axes = plt.subplots(1, 3, figsize=(12.0, 4.0))
for ax, mu in zip(axes, (0, 1, 5)):  # the directions x0, x1 and x5
    table = np.array([[at_sample(omega[mu][a][b]).real for b in range(8)]
                      for a in range(8)])
    limit = np.abs(table).max()
    image = ax.imshow(table, cmap="RdBu_r", vmin=-limit, vmax=limit)
    for a in range(8):
        for b in range(8):
            if table[a, b] != 0:  # white digits on the dark squares
                dark = abs(table[a, b]) > 0.6 * limit
                ax.text(b, a, f"{table[a, b]:.2f}", ha="center", va="center",
                        fontsize=6, color="white" if dark else "black")
    ax.set_xticks(range(8), NAMES, fontsize=7)
    ax.set_yticks(range(8), NAMES, fontsize=7)
    ax.set_xlabel("frame index $b$")
    ax.set_ylabel("frame index $a$")
    ax.set_title(f"$\\omega_{{x{mu}\\,ab}}$ at the sample point")
    ax.grid(False)
    fig.colorbar(image, ax=ax, shrink=0.75)
fig.tight_layout()
```

Three panels, for $\mu = x0$, $x1$ and $x5$ (`zip(axes, (0, 1, 5))` pairs each panel with its direction). For each, `table` is the $8 \times 8$ array of the numbers $\omega_{\mu ab}$ at the sample point, and `imshow` draws it with a colour scale from $-$`limit` to `limit`, the largest absolute value, so that zero is white. Every nonzero entry is also printed as a number with two decimals (`f"{value:.2f}"`), in white on the dark squares (more than 0.6 of the largest value) and in black elsewhere, so that it can be read. The tick labels name the frame directions, `fig.colorbar` adds the colour scale beside each panel, and `fig.tight_layout()` arranges the panels without overlap.

```python
save_figure(fig, "omega_heat_maps",
            "The canonical spin connection $\\omega_{\\mu ab}$ of the diagonal "
            ...
            "positive rate $a_4' = 1$.")
```

The figure is saved as `06a_4_omega_heat_maps.png`.

**What Figure 06a.4 shows.** For $\mu = x0$ the only nonzero squares are $(x0, x4) = -0.28$ and its mirror image $(x4, x0) = 0.28$: the antisymmetry. The number is $h_4s_b\cot z = -\frac13e^{-1/6}\cdot1 = -0.282$ at the sample point, where $s_b = e^{-1/2}e^{1/3} = e^{-1/6} = 0.8465$ and $\cot z = 1$. For $\mu = x1$ the only nonzero squares are $(x1, x4) = 1.65$ and $(x4, x1) = -1.65$: $a_4'e^{a_4} = e^{1/2} = 1.649$. For $\mu = x5$ the nonzero squares are $(x0, x5) = 0.94$, which is $HW = (\frac12)^{1/12} = 0.944$ (since $\sin^2(\pi/4) = \frac12$), and $(x4, x5) = -0.27$, which is $h_4s_bW = -\frac13\cdot0.8465\cdot0.944 = -0.266$, with their mirror images. The hidden direction and the extra time turn towards the time with the same negative rate $h_4 = -\frac13$ (blue), the 3-space direction with the positive rate $a_4' = 1$ (red): the hidden block shrinks while 3-space grows. The extra time also turns towards the hidden direction, because its warp factor depends on $x_0$.

**In [13], the spinor connection and the covariant constancy** (Section 6.7).

```python
Omega = spinor_connection(omega, S)  # eight 16 x 16 matrices
gup = curved_gammas(e, gamma)  # gamma^mu = gamma^a / f_a for mu = a
check(Omega[4] == Z16 and not matrix_is_zero(Omega[0]),
      "Omega_x4 = 0 and Omega_x0 is not zero",
      record=f"{REPORT_PY}, check Omega_x4_vanishes_Omega_x0_does_not")
```

`Omega` is the list of the eight matrices $\Omega_\mu = \sum_{a<b}\omega_{\mu ab}S^{ab}$, and `gup` the list of the eight curved gammas $\gamma^\mu = \gamma^{(\mu)}/f_\mu$. The first check requires $\Omega_{x4}$ to be the zero matrix (`Omega[4] == Z16`, an exact comparison) and $\Omega_{x0}$ not to be zero (`not matrix_is_zero(...)`): the time has no connection, the hidden direction has one, because its factor $s_b\cot z$ changes with the time.

```python
closed = ([h4 * s_b * sp.cot(z) * gamma[0] * gamma[4] / 2]
          + [a4p * sp.exp(a4) * gamma[i] * gamma[4] / 2 for i in (1, 2, 3)] + [Z16]
          + [W(x0) * (h4 * s_b * gamma[4] * gamma[t] + H * gamma[0] * gamma[t]) / 2
             for t in (5, 6, 7)])  # the record's Omega_components, typed in
check(all(matrix_is_zero(Omega[mu] - closed[mu]) for mu in range(8))
      and record_passed(REPORT_WL, "Omega_components"),
      "the eight Omega_mu are the closed forms of the record",
      record=f"{THEORY_FILE}, formula Omega_components")
```

`closed` is the record's formula `Omega_components` typed in as matrices, in the order $x0, \dots, x7$. The first matrix, for the hidden direction, is $\frac12h_4s_b\cot z\,\gamma^{(x0)}\gamma^{(x4)}$; the next three, for the 3-space directions $i = 1, 2, 3$, are $\frac12a_4'e^{a_4}\gamma^{(x_i)}\gamma^{(x4)}$; the fifth, for the time, is the zero matrix; and the last three, for the extra times $t = 5, 6, 7$, are $\frac12W(h_4s_b\gamma^{(x4)}\gamma^{(x_t)} + H\gamma^{(x0)}\gamma^{(x_t)})$ (two list comprehensions joined with `+`). The check requires all eight matrices to agree with the computed ones exactly, and the WolframScript report to record `Omega_components` as passed.

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
check(constancy_ok and record_passed(REPORT_WL, "gamma_covariantly_constant")
      and record_passed(REPORT_PY, "covariant_constancy_D_mu_gamma_nu"),
      "D_mu gamma^nu = 0 for all 64 pairs (mu, nu)",
      record=f"{REPORT_WL}, check gamma_covariantly_constant")
```

The covariant constancy $D_\mu\gamma^\nu = \partial_\mu\gamma^\nu + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}\gamma^\lambda + [\Omega_\mu, \gamma^\nu] = 0$ for all 64 pairs $(\mu, \nu)$ (`.diff(x[mu])` differentiates every entry of the matrix), together with the two record checks that state the same.

```python
say(f"Omega_x5 has {sum(1 for v in Omega[5] if v != 0)} nonzero entries of 256")
```

The last line counts the nonzero entries of $\Omega_{x5}$ and prints Omega_x5 has 32 nonzero entries of 256: its two generators, $\gamma^{(x4)}\gamma^{(x5)}$ and $\gamma^{(x0)}\gamma^{(x5)}$, each have 16 nonzero entries, in different places. The cell prints four PASS lines with their records and this line.

**In [14], figure 5: the spinor connection as heat maps.**

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
fig, axes = plt.subplots(1, 3, figsize=(12.0, 3.9))
for ax, mu in zip(axes, (0, 1, 5)):  # the directions x0, x1 and x5
    table = np.array([[at_sample(v).real for v in row] for row in Omega[mu].tolist()])
    limit = np.abs(table).max()
    image = ax.imshow(table, cmap="RdBu_r", vmin=-limit, vmax=limit)
    ax.set_xticks(range(0, 16, 3), [str(k + 1) for k in range(0, 16, 3)])
    ax.set_yticks(range(0, 16, 3), [str(k + 1) for k in range(0, 16, 3)])
    ax.set_xlabel("column (spinor component 1 to 16)")
    ax.set_ylabel("row (spinor component)")
    ax.set_title(f"$\\Omega_{{x{mu}}}$ at the sample point")
    ax.grid(False)
    fig.colorbar(image, ax=ax, shrink=0.75)
fig.tight_layout()
```

Three heat maps, for $\Omega_{x0}$, $\Omega_{x1}$ and $\Omega_{x5}$, built as in In [12] but from the 16 x 16 matrices (`.tolist()` gives the rows; each entry is evaluated at the sample point). Every third row and column is labelled with its spinor component, numbered 1 to 16 (`range(0, 16, 3)` is 0, 3, 6, ..., 15, and `str(k + 1)` the label).

```python
save_figure(fig, "spinor_connection_heat_maps",
            "The spinor connection $\\Omega_{x0}$ (left), $\\Omega_{x1}$ (middle) "
            ...
            "last eight.")
```

The figure is saved as `06a_5_spinor_connection_heat_maps.png`.

**What Figure 06a.5 shows.** Each matrix has its colours only in the upper-left and the lower-right $8 \times 8$ blocks: a generator is a product of two gammas, an even product, and maps the first eight components to the first eight and the last eight to the last eight (the two chiral halves of Chapter 5). $\Omega_{x0}$ and $\Omega_{x1}$ are boosts: their squares appear in mirror pairs of the same colour (symmetric matrices), with the entries $\pm\frac12h_4s_b\cot z = \pm0.14$ and $\pm\frac12a_4'e^{a_4} = \pm0.82$ at the sample point. $\Omega_{x5}$ has one set of squares in mirror pairs of opposite colours (the antisymmetric rotation part in the plane of $x4$ and $x5$, entries $\pm\frac12h_4s_bW = \pm0.13$) and another set in mirror pairs of the same colour (the symmetric boost part in the plane of $x0$ and $x5$, entries $\pm\frac12HW = \pm0.47$).

**In [15], the contraction, direction by direction** (Section 6.8).

```python
per_direction = []  # (alpha_mu, beta_mu) for mu = x0 ... x7
decomposed = True
for mu in range(8):
    M = (gup[mu] * Omega[mu]).applyfunc(sp.simplify)
    alpha = sp.simplify(-(M * gamma[4]).trace() / 16)  # coefficient of gamma^(x4)
    beta = sp.simplify((M * gamma[0]).trace() / 16)  # coefficient of gamma^(x0)
    decomposed = decomposed and matrix_is_zero(M - alpha * gamma[4] - beta * gamma[0])
    per_direction.append((alpha, beta))
    say(f"gamma^{NAMES[mu]} Omega_{NAMES[mu]} = ({alpha}) gamma^(x4) "
        f"+ ({beta}) gamma^(x0)")
```

For each $\mu$ the product $M = \gamma^\mu\Omega_\mu$ is simplified entry by entry (`applyfunc(sp.simplify)`), its coefficients $\alpha$ and $\beta$ are read off with the traces of Section 6.8 (`.trace()`), and `matrix_is_zero(M - alpha * gamma[4] - beta * gamma[0])` confirms that nothing else is left. Eight output lines print the terms, for example

```text
gamma^x5 Omega_x5 = (-Derivative(a4(x4), x4)/2 + Derivative(b4(x4), x4)/(4*b4(x4)))
    gamma^(x4) + (H*exp(a4(x4))/(2*sqrt(b4(x4)))) gamma^(x0)
```

which is $\frac12h_4\gamma^{(x4)} + \frac12He^{a_4}b_4^{-1/2}\gamma^{(x0)}$, the row of an extra time in Section 6.8; the line of $x0$ has the same coefficient of $\gamma^{(x4)}$ and the coefficient 0 of $\gamma^{(x0)}$, and the lines of $x1, x2, x3$ show $\frac12a_4'$ and 0.

```python
c_g = sp.Rational(3, 2) * H * sp.exp(a4) / sp.sqrt(b4)  # coefficient of gamma^(x0)
v_g = b4p / b4 - a4p / 2  # coefficient of gamma^(x4)
warp_term = H * sp.exp(a4) / (2 * sp.sqrt(b4))  # beta of an extra time
predicted = ([(h4 / 2, 0)] + [(a4p / 2, 0)] * 3 + [(0, 0)]
             + [(h4 / 2, warp_term)] * 3)  # x0, x1..x3, x4, x5..x7
check(decomposed and all(is_zero(per_direction[k][0] - predicted[k][0])
                         and is_zero(per_direction[k][1] - predicted[k][1])
                         for k in range(8))
      and record_passed(REPORT_PY, "per_direction_terms")
      and record_passed(REPORT_WL, "gammaOmega_per_direction"),
      "the eight terms gamma^mu Omega_mu (no sum)",
      record=f"{REPORT_WL}, check gammaOmega_per_direction")
table_record = record_formula("gammaOmega_per_direction", RECORD_NAMES)
check(all(is_zero(per_direction[k][0] - table_record[k][1])
          and is_zero(per_direction[k][1] - table_record[k][2]) for k in range(8)),
      "the eight terms equal the record's table",
      record=f"{THEORY_FILE}, formula gammaOmega_per_direction")
```

`c_g` and `v_g` are the two coefficients of the result, $\frac32He^{a_4}b_4^{-1/2}$ and $b_4'/b_4 - a_4'/2$; `warp_term` is $\frac12He^{a_4}b_4^{-1/2}$, the $\beta$ of one extra time; and `predicted` is the table of Section 6.8 in the order $x0, \dots, x7$. The first check compares the eight computed rows with it and requires the sympy report to record `per_direction_terms` and the WolframScript report `gammaOmega_per_direction` as passed. The record lists the table `gammaOmega_per_direction` as $\{\mu, \alpha_\mu, \beta_\mu\}$; the second check compares all eight rows with it (`table_record[k][1]` is the record's $\alpha$, `[k][2]` its $\beta$).

```python
space_part = sp.simplify(sum(per_direction[k][0] for k in (1, 2, 3)))
block_part = sp.simplify(sum(per_direction[k][0] for k in (0, 5, 6, 7)))
hidden = sp.simplify(sum(beta for _, beta in per_direction))
report("x4 part from the inflating x1, x2, x3", space_part)
report("x4 part from the hidden block x0, x5, x6, x7", block_part)
report("x0 part from all directions", hidden)
check(is_zero(space_part - 3 * a4p / 2) and is_zero(block_part - 2 * h4)
      and is_zero(space_part + block_part - v_g) and is_zero(hidden - c_g),
      "x4 parts: 3-space (3/2) a4', hidden block 2 h4, together v_g; x0 part c_g",
      record=f"{REPORT_PY}, check per_direction_terms")
```

Three partial sums are printed: the coefficient of $\gamma^{(x4)}$ from the three 3-space directions, `3*Derivative(a4(x4), x4)/2`, that is $\frac32a_4'$; from the four directions of the hidden block, `-2*Derivative(a4(x4), x4) + Derivative(b4(x4), x4)/b4(x4)`, that is $2h_4$; and the coefficient of $\gamma^{(x0)}$ from all directions, `3*H*exp(a4(x4))/(2*sqrt(b4(x4)))`, that is $c_g$. The check requires these three values and that the two parts along the time add up to $v_g$.

```python
slash = sum((gup[mu] * Omega[mu] for mu in range(8)), Z16)
gravity_term = c_g * gamma[0] + v_g * gamma[4]
total_text = FORMULAS["gammaOmega_total"].replace(chr(34), "")  # gamma[x0], gamma[x4]
total_record = wolfram_to_sympy(total_text.replace("gamma[x0]", "G0")
                                .replace("gamma[x4]", "G4"), RECORD_NAMES)
G0, G4 = sp.Symbol("G0"), sp.Symbol("G4")  # the record's gamma[x0], gamma[x4]
record_matrix = (total_record.coeff(G0) * gamma[0]
                 + total_record.coeff(G4) * gamma[4])
check(matrix_is_zero(slash - gravity_term) and matrix_is_zero(slash - record_matrix)
      and record_passed(REPORT_WL, "gammaOmega_total")
      and record_passed(REPORT_PY, "gamma_mu_Omega_mu_equals_hidden_block_terms")
      and record_passed(REPORT_LEAD, "gamma_Omega_equals_hidden_block_terms"),
```

`slash` is the whole sum $\sum_\mu\gamma^\mu\Omega_\mu$ and `gravity_term` the matrix $c_g\gamma^{(x0)} + v_g\gamma^{(x4)}$. The record writes the total as a formula with the symbols `gamma["x0"]` and `gamma["x4"]`; the line with `total_text` removes the double quotes (`chr(34)` is the character `"`), the two names are replaced by the plain symbols `G0` and `G4`, the text is read, and `.coeff(G0)` and `.coeff(G4)` take out the two coefficients, which are multiplied by the gamma matrices. The check requires the computed sum to equal both $c_g\gamma^{(x0)} + v_g\gamma^{(x4)}$ and the record's matrix, and the three reports (sympy, WolframScript and the lead's) to record the result as passed.

```python
      "gamma^mu Omega_mu = (3/2) H e^(a4) b4^(-1/2) gamma^(x0) + (b4'/b4 - a4'/2) "
      "gamma^(x4) exactly",
      record=f"{THEORY_FILE}, formula gammaOmega_total; {REPORT_LEAD}, check "
             "gamma_Omega_equals_hidden_block_terms")
on_history = {b4p: BETA * A_EXACT * H * b4, a4p: A_EXACT * H}  # the derivatives
history_values = {a4: A_EXACT * H * x4, b4: B4_ZERO * sp.exp(BETA * A_EXACT * H * x4)}
slash_history = slash.subs(on_history).subs(history_values)
check(matrix_is_zero(slash_history - sp.Rational(3, 2) * H * sp.exp(H * x4 / 3)
                     * gamma[0] - sp.Rational(5, 6) * H * gamma[4]),
      "on the history of the record: gamma^mu Omega_mu = (3/2) H e^(H x4/3) "
      "gamma^(x0) + (5/6) H gamma^(x4)")
```

On the history of the record, `on_history` replaces the derivatives, $b_4' = \beta AHb_4$ and $a_4' = AH$, and `history_values` the functions, $a_4 = AHx_4$ and $b_4 = b_4(0)e^{\beta AHx_4}$ (the derivatives first, for the reason given in In [10]). The last check requires the sum to become $\frac32He^{Hx_4/3}\gamma^{(x0)} + \frac56H\gamma^{(x4)}$. The cell prints the eight terms, the three partial sums and five PASS lines.

**In [16], figure 6: the eight terms as bars.**

```python
a4_part = [float(sp.simplify(alpha.subs(b4p, 0) / a4p))  # the part with a4'
           for alpha, _ in per_direction]
b4_part = [float(sp.simplify(alpha.subs(a4p, 0) / (b4p / b4)))
           for alpha, _ in per_direction]  # the part with b4'/b4
beta_units = [float(sp.simplify(beta / (H * sp.exp(a4) / sp.sqrt(b4))))
              for _, beta in per_direction]  # beta / (H e^a4 b4^(-1/2))
```

Three lists of eight numbers for the bars. `a4_part` is the part of each $\alpha_\mu$ proportional to $a_4'$, in units of $a_4'$: `alpha.subs(b4p, 0)` sets $b_4' = 0$, which leaves only that part, and the division by $a_4'$ gives a pure number, which `float` turns into a decimal number. `b4_part` is the part proportional to $b_4'/b_4$, in units of $b_4'/b_4$ (set $a_4' = 0$ and divide). `beta_units` is each $\beta_\mu$ in units of $He^{a_4}b_4^{-1/2}$.

```python
positions = np.arange(8)
fig, axes = plt.subplots(1, 3, figsize=(12.0, 4.2), sharey=True)
colors = ["tab:blue"] + ["tab:red"] * 3 + ["gray"] + ["tab:blue"] * 3
panels = [(a4_part, "$\\gamma^{(x4)}$, part / $a_4'$"),
          (b4_part, "$\\gamma^{(x4)}$, part / $(b_4'/b_4)$"),
          (beta_units, "$\\gamma^{(x0)}$ / $(He^{a_4}b_4^{-1/2})$")]
for ax, (heights, title) in zip(axes, panels):
    ax.bar(positions, heights, color=colors, width=0.6)
    ax.set_title(f"{title}: total {sum(heights):g}", fontsize=10)
    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.set_xticks(positions, NAMES)
    ax.set_xlabel("direction $\\mu$")
axes[0].set_ylabel("coefficient (in the unit named in the title)")
```

Three bar charts side by side with a common vertical axis (`sharey=True`), one bar per direction, coloured blue for the hidden block ($x0$ and the extra times), red for 3-space and gray for the time; each title ends with the total of its bars (`{sum(heights):g}` prints the number in its shortest form). A black zero line, the direction names under the bars, and the axis label.

```python
save_figure(fig, "gamma_omega_per_direction",
            "The eight terms $\\gamma^\\mu\\Omega_\\mu$ (no sum) of the diagonal "
            ...
            "(b_4'/b_4 - a_4'/2)\\gamma^{(x4)}$.")
```

The figure is saved as `06a_6_gamma_omega_per_direction.png`.

**What Figure 06a.6 shows.** On the left, three red bars of height $+\frac12$ (3-space grows) and four blue bars of height $-\frac12$ (the hidden direction and the three extra times shrink): total $-\frac12$, the $a_4'$ part of $v_g$. In the middle, four blue bars of height $\frac14$: the $b_4'/b_4$ parts come from the four directions of the hidden block, total 1. On the right, three blue bars of height $\frac12$ for the extra times: only their warp makes the hidden term, total $\frac32$, so $c_g = \frac32He^{a_4}b_4^{-1/2}$. The gray direction $x4$ contributes nothing, because $\Omega_{x4} = 0$; the direction $x0$ contributes along the time but not along itself.

**In [17], figure 7: the block form and the sum as pictures** (Section 6.10).

```python
I8, Z8 = sp.eye(8), sp.zeros(8, 8)  # 8 x 8 identity and zero matrices
blocks_ok = True
for entry in FORMULAS["field_equation_blocks"]:  # eight texts {"xa", tb, t}
    name, tb, t = json.loads(entry.replace("{", "[").replace("}", "]"))
    a = NAMES.index(name)  # the position of the direction xa (0 ... 7)
    # gamma^(xa) must be the block matrix with the zero blocks on the diagonal
    blocks_ok = blocks_ok and gamma[a] == sp.BlockMatrix(
        [[Z8, sp.Matrix(tb)], [sp.Matrix(t), Z8]]).as_explicit()
check(blocks_ok and len(FORMULAS["field_equation_blocks"]) == 8
      and record_passed(REPORT_WL, "block_form"),
      "the eight gammas have the block form of the record",
      record=f"{THEORY_FILE}, formula field_equation_blocks")
```

The record's formula `field_equation_blocks` holds eight texts, one per direction, each of the form `{"xa", tb, t}` with the name of the direction and the two off-diagonal $8 \times 8$ blocks $\bar\tau_a$ and $\tau_a$ written with braces. Replacing every brace by a square bracket turns the text into JSON, which `json.loads` reads as three objects: the name and two lists of rows. `NAMES.index(name)` finds the position of the direction, and `sp.BlockMatrix([[Z8, tb], [t, Z8]]).as_explicit()` assembles the 16 x 16 matrix with zero blocks on the diagonal. The check requires every gamma to equal its block matrix, eight entries in the record, and the WolframScript report's `block_form` as passed.

```python
check(gamma[0] == sp.BlockMatrix([[Z8, I8], [I8, Z8]]).as_explicit(),
      "gamma^(x0) has the 8 x 8 identity in its two off-diagonal blocks")
```

The second check: $\gamma^{(x0)}$ has the $8 \times 8$ identity in both off-diagonal blocks, so $c_g\gamma^{(x0)}$ shows the value $c_g$ on two diagonal lines.

```python
panels = [
    ("sum over $x1, x2, x3$", sum((gup[k] * Omega[k] for k in (1, 2, 3)), Z16)),
    ("sum over $x0, x5, x6, x7$", sum((gup[k] * Omega[k] for k in (0, 5, 6, 7)), Z16)),
    ("total $\\gamma^\\mu\\Omega_\\mu$", slash),
    ("$c_g\\gamma^{(x0)} + v_g\\gamma^{(x4)}$", gravity_term),
]
fig, axes = plt.subplots(2, 2, figsize=(8.0, 7.6))
for ax, (title, matrix) in zip(axes.flat, panels):
    table = np.array([[at_sample(v).real for v in row] for row in matrix.tolist()])
    image = ax.imshow(table, cmap="RdBu_r", vmin=-2.0, vmax=2.0)
    ax.set_title(title, fontsize=10)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)
fig.colorbar(image, ax=axes, shrink=0.7, label="entry value")
```

Four pictures in a grid of 2 by 2: the sum of the three 3-space terms, the sum of the four terms of the hidden block, the total and $c_g\gamma^{(x0)} + v_g\gamma^{(x4)}$, each evaluated at the sample point and drawn with one common colour scale from $-2$ to $2$ (one colour bar for all four, `ax=axes`); `set_xticks([])` removes the tick labels.

```python
save_figure(fig, "gamma_omega_sum",
            "The sum as pictures of 16 x 16 matrices at the sample point "
            ...
            "$v_g = 5/6$. The two bottom pictures are identical.")
```

The figure is saved as `06a_7_gamma_omega_sum.png`.

**What Figure 06a.7 shows.** Top left, the three 3-space terms give the pattern of $\gamma^{(x4)}$ with the entries $\pm\frac32a_4' = \pm1.5$. Top right, the four terms of the hidden block give the same pattern with the opposite colours and the paler entries $\pm2h_4 = \mp\frac23$, and in addition the value $c_g = \frac32e^{1/6} = 1.77$ (dark red) on two diagonal lines in the off-diagonal blocks. Bottom left, the total: the diagonal lines with $1.77$ and the pattern of $\gamma^{(x4)}$ with the entries $\pm(\frac32 - \frac23) = \pm\frac56$; bottom right, $c_g\gamma^{(x0)} + v_g\gamma^{(x4)}$ with $v_g = \frac56$, identical to it. The two $\gamma^{(x4)}$ parts do not cancel: what is left is the part $v_g = \frac56$, half the rate of the 7-volume.

**In [18], the divergence form** (Section 6.9).

```python
anticommutes = all(matrix_is_zero(gup[mu] * Omega[mu] + Omega[mu] * gup[mu])
                   for mu in range(8))
check(anticommutes, "{gamma^mu, Omega_mu} = 0 for each mu separately",
      record=f"{REPORT_PY}, check anticommutator_gamma_Omega_vanishes")
```

Fact 1: $\gamma^\mu\Omega_\mu + \Omega_\mu\gamma^\mu = 0$ for each $\mu$ separately.

```python
sqrt_g = volume  # f_0 ... f_7; the sign G of cot z cancels in the formula
divergence = sum(((sqrt_g * gup[mu]).diff(x[mu]) for mu in range(8)), Z16) / (2 * sqrt_g)
check(matrix_is_zero(divergence - gravity_term)
      and record_passed(REPORT_WL, "gammaOmega_divergence_form")
      and record_passed(REPORT_PY, "divergence_of_sqrtg_gamma")
      and record_passed(REPORT_LEAD, "gamma_Omega_divergence_formula"),
      "(1/(2 sqrt|g|)) d_mu (sqrt|g| gamma^mu) = c_g gamma^(x0) + v_g gamma^(x4)",
      record=f"{REPORT_WL}, check gammaOmega_divergence_form")
```

`sqrt_g` is the signed product $f_0\cdots f_7$ of In [7]; as Section 6.9 explained, the constant sign $G$ cancels between numerator and denominator, so the signed product may stand for $\sqrt{\lvert g\rvert}$. `divergence` is $\frac{1}{2\sqrt{\lvert g\rvert}}\sum_\mu\partial_\mu(\sqrt{\lvert g\rvert}\gamma^\mu)$, computed entry by entry. The check requires it to equal $c_g\gamma^{(x0)} + v_g\gamma^{(x4)}$, and the three reports to record the divergence form as passed.

```python
products = [sp.simplify(sp.prod([f[c] for c in range(8) if c != b])) for b in range(8)]
for b in (0, 4):
    say(f"product of the f_c with c != {NAMES[b]}: {products[b]}")
own_coordinate = [sp.simplify(sp.diff(products[b], x[b]) / (2 * sqrt_g))
                  for b in range(8)]
say("(1/(2 sqrt|g|)) d_b (product without b), b = x0 ... x7: "
    f"{own_coordinate}")
expected_own = [c_g, 0, 0, 0, v_g, 0, 0, 0]
check(all(is_zero(own_coordinate[b] - expected_own[b]) for b in range(8)),
      "only the hidden direction (c_g) and the time (v_g) contribute")
```

Fact 2: `products[b]` is the product of the seven factors other than $f_b$. Two of them are printed: for $b = x0$, `W(x0)**3*b4(x4)**(3/2)`, that is $b_4^{3/2}W^3$, and for $b = x4$ the whole product $e^{-a_4}b_4^2\cot z\,W^3$. `own_coordinate[b]` is the derivative of `products[b]` by its own coordinate $x_b$, divided by $2\sqrt{\lvert g\rvert}$; the list is printed, `[3*H*exp(a4(x4))/(2*sqrt(b4(x4))), 0, 0, 0, -Derivative(a4(x4), x4)/2 + Derivative(b4(x4), x4)/b4(x4), 0, 0, 0]`, and the last check requires it to be $[c_g, 0, 0, 0, v_g, 0, 0, 0]$: only the hidden direction and the time contribute, with exactly the two terms derived by hand in Section 6.9. The cell prints three PASS lines with their records and three output lines.

**In [19], figure 8: the divergence form with a calculator's method.**

```python
H_value = 1.0
z_values = np.concatenate([np.linspace(0.06, np.pi / 2 - 0.06, 200),
                           np.linspace(np.pi / 2 + 0.06, np.pi - 0.06, 200)])
x0_values = z_values / (6 * H_value)  # both halves of the cell 0 < z < pi
step = 1e-5  # the step h of the central difference
```

A **central difference** approximates a derivative by numbers: $u'(x) \approx \frac{u(x + h) - u(x - h)}{2h}$ for a small step $h$. Its error is about $\frac{h^2}{6}u'''(x)$ (the Taylor series of $u(x \pm h)$: the terms with $u$ and $u''$ cancel in the difference, and the first term left over is the one with $u'''$). `z_values` are 400 hidden angles on the two halves of the cell, $0.06 \le z \le \pi/2 - 0.06$ and $\pi/2 + 0.06 \le z \le \pi - 0.06$ (`np.concatenate` joins the two arrays), which avoids the fold and the tips; with $H = 1$, `x0_values` are the corresponding $x_0 = z/6$. The step is $h = 10^{-5}$.

```python
def hidden_density(x0_value):
    return np.abs(np.sin(6 * H_value * x0_value)) ** 0.5  # (sin^2 z)^(1/4) = W^3


derivative = (hidden_density(x0_values + step)
              - hidden_density(x0_values - step)) / (2 * step)
ratio = derivative / (2 * hidden_density(x0_values) / np.tan(z_values))  # 3H/2
```

`hidden_density` is the function $W^3 = (\sin^2 z)^{1/4} = \lvert\sin z\rvert^{1/2}$ of $x_0$, the part of the product $\prod_{c\neq x0}f_c = b_4^{3/2}W^3$ that depends on $x_0$ (Section 6.9). `derivative` is its central difference, and `ratio` is that derivative divided by $2\cot z\,W^3$ (`/ np.tan(z_values)` multiplies by $\cot z$): by Section 6.9 this is $c_g$ divided by $e^{a_4}b_4^{-1/2}$, which must be $\frac32H = 1.5$ at every $z$.

```python
x4_values = np.linspace(-6.0, 6.0, 300)


def b4_history(x4_value):  # an illustrative b4(x4) > 0: the history with a wobble
    return np.exp(4.0 * x4_value / 3.0) * (1.0 + 0.5 * np.sin(x4_value))


def time_density(x4_value):
    return np.exp(-x4_value) * b4_history(x4_value) ** 2  # e^(-a4) b4^2, a4 = x4


time_derivative = (time_density(x4_values + step)
                   - time_density(x4_values - step)) / (2 * step)
time_ratio = time_derivative / (2 * time_density(x4_values))  # d ln(e^-a4 b4^2) / 2
# v_g = b4'/b4 - a4'/2 = 4/3 + (1/2) cos x4 / (1 + (1/2) sin x4) - 1/2
exact_time = (4.0 / 3.0 + 0.5 * np.cos(x4_values) / (1.0 + 0.5 * np.sin(x4_values))
              - 0.5)
```

For the time direction the notebook takes $a_4 = x_4$ and, instead of the history, an illustrative $b_4 = e^{4x_4/3}(1 + \frac12\sin x_4)$ with a wobble, so that $v_g$ is not a constant and the test is not trivial. `time_density` is $e^{-a_4}b_4^2$, the part of $\sqrt{\lvert g\rvert}$ that depends on $x_4$, and `time_ratio` is half the central difference of its logarithm, $\partial_4(e^{-a_4}b_4^2)/(2e^{-a_4}b_4^2)$, at 300 times from $-6$ to $6$. `exact_time` is the exact $v_g = b_4'/b_4 - a_4'/2$ for this $b_4$: with the product rule, $b_4'/b_4 = \frac43 + \frac{\frac12\cos x_4}{1 + \frac12\sin x_4}$, and $a_4' = 1$.

```python
report("largest |central difference - 3H/2| over the cell",
       f"{np.max(np.abs(ratio - 1.5)):.0e}")
report("largest |central difference - v_g| over the grid",
       f"{np.max(np.abs(time_ratio - exact_time)):.0e}")
check(np.max(np.abs(ratio - 1.5)) < 1e-6
      and np.max(np.abs(time_ratio - exact_time)) < 1e-6,
      "the numerical derivatives give c_g / (e^a4 b4^(-1/2)) = 3H/2 and v_g")
```

Two key numbers are printed with one significant digit (`:.0e`): the largest deviation of `ratio` from 1.5 over the cell, 2e-07, and the largest deviation of `time_ratio` from the exact $v_g$, 2e-10. The first is larger because near the tips the function $\lvert\sin z\rvert^{1/2}$ bends strongly: at $z = 0.06$ its third derivative by $x_0$ is about $6^3\cdot\frac38z^{-5/2} \approx 9\times10^4$, so the error of the derivative is about $\frac{h^2}{6}\cdot9\times10^4 \approx 1.5\times10^{-6}$, which divided by $2\cot z\,W^3 \approx 8$ gives about $2\times10^{-7}$ (COMPUTED). The check requires both deviations to be smaller than $10^{-6}$.

```python
fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
for half in (slice(0, 200), slice(200, 400)):  # the two halves, drawn separately
    ax_left.plot(z_values[half], ratio[half], color="tab:blue")
ax_left.plot([], [], color="tab:blue",
             label="$\\partial_{x0}(\\sin^2 z)^{1/4}/(2\\cot z\\,(\\sin^2 z)^{1/4})$")
ax_left.axvline(np.pi / 2, color="gray", linewidth=0.8)  # the fold
ax_left.set_ylim(0.0, 2.4)
ax_left.set_xlabel("hidden angle $z = 6Hx_0$ (radians), fold at $\\pi/2$")
ax_left.set_ylabel("$c_g/(e^{a_4}b_4^{-1/2})$ (units of $H$)")
ax_left.set_title("Hidden direction: the constant $3H/2$")
ax_left.legend(fontsize=8, loc="lower center")
```

The left panel draws `ratio` versus $z$, each half of the cell as its own curve (a `slice(0, 200)` takes the first 200 values), so that no line is drawn across the fold; an empty plot makes the legend entry, and a vertical line marks the fold.

```python
ax_right.plot(x4_values, time_ratio, label="central difference, "
              "$b_4 = e^{4x_4/3}(1 + \\frac{1}{2}\\sin x_4)$")
ax_right.plot(x4_values, exact_time, ":", color="black", linewidth=2.5,
              label="exact $b_4'/b_4 - a_4'/2$")
ax_right.plot(x4_values, np.full_like(x4_values, 5.0 / 6.0), "--", color="gray",
              label="history $b_4 = e^{4x_4/3}$: exactly $5/6$")
ax_right.set_ylim(-0.6, 1.9)  # room for the legend below the curves
ax_right.set_xlabel("time $x_4$ (units $1/H$), $a_4 = x_4$")
ax_right.set_ylabel("coefficient $v_g$ of $\\gamma^{(x4)}$")
ax_right.set_title("Time direction: $v_g = b_4'/b_4 - a_4'/2$")
ax_right.legend(fontsize=8, loc="lower center")
```

The right panel draws the central differences (solid), the exact $v_g$ (thick dotted black line) and, for comparison, the constant $\frac56$ of the history of the record (dashed gray; `np.full_like` makes an array of the same length filled with one value).

```python
save_figure(fig, "divergence_form",
            "The divergence form of $\\gamma^\\mu\\Omega_\\mu$, with $H = 1$, checked "
            ...
            "term is half the rate of the 7-volume $e^{-a_4}b_4^2$.")
```

The figure is saved as `06a_8_divergence_form.png`.

**What Figure 06a.8 shows.** On the left, the two curves are flat at 1.5 on both halves of the cell: the coefficient of $\gamma^{(x0)}$, divided by $e^{a_4}b_4^{-1/2}$, is the constant $\frac32H$ at every hidden angle, as the divergence form says. On the right, the solid central differences lie on the dotted exact curve $v_g$, which oscillates with the illustrative $b_4$ between $\frac56 - \frac1{\sqrt3} = 0.26$ and $\frac56 + \frac1{\sqrt3} = 1.41$ (the extremes of $\frac{\cos x_4}{2 + \sin x_4}$ lie where $\sin x_4 = -\frac12$), around the dashed value $\frac56$ of the history of the record. The term along the time is half the rate of the 7-volume $e^{-a_4}b_4^2$, whatever the function $b_4$.

**In [20], the Dirac operator and non-triviality** (Section 6.10).

```python
import re  # text patterns, to rename the record's symbols
```

`re` is Python's module for **regular expressions**, text patterns used below to rename the record's symbols.

```python
psi = sp.Matrix([sp.Function(f"psi{A}")(*x) for A in range(1, 17)])  # 16 functions
D = [psi.diff(x[mu]) + Omega[mu] * psi for mu in range(8)]  # D_mu Psi
dirac = sum((gup[mu] * D[mu] for mu in range(8)), sp.zeros(16, 1))
written_out = sum((gamma[a] * psi.diff(x[a]) / f[a] for a in range(8)),
                  sp.zeros(16, 1)) + gravity_term * psi
check(all(is_zero(v) for v in dirac - written_out)
      and record_passed(REPORT_WL, "Dirac_operator_explicit_C")
      and record_passed(REPORT_WL, "Dirac_operator_explicit_G"),
      "gamma^mu D_mu Psi = sum_a (1/f_a) gamma^a d_a Psi + c_g gamma^(x0) Psi + "
      "v_g gamma^(x4) Psi",
      record=f"{REPORT_WL}, checks Dirac_operator_explicit_C and _G")
```

`psi` is a column of sixteen unknown functions $\psi_1, \dots, \psi_{16}$ of all eight coordinates (`*x` passes the eight symbols as eight arguments). `D` is the list of the eight covariant derivatives $D_\mu\Psi = \partial_\mu\Psi + \Omega_\mu\Psi$, and `dirac` the Dirac operator $\sum_\mu\gamma^\mu D_\mu\Psi$, a column of sixteen expressions. `written_out` is the form of Section 6.10, $\sum_a\frac{1}{f_a}\gamma^{(a)}\partial_a\Psi + (c_g\gamma^{(x0)} + v_g\gamma^{(x4)})\Psi$. The check requires all sixteen differences to vanish exactly, for sixteen arbitrary functions, and the WolframScript report to record the explicit operator as passed for both fields.

```python
# Rename the derivatives d psi_B / d x_k and then the functions psi_B as plain
# symbols dPsi<B>x<k> and Psi<B> (derivatives first: renaming psi_B first would
# turn its derivatives into derivatives of a constant symbol, which are zero).
rename_derivatives = {sp.Derivative(psi[B], x[k]): sp.Symbol(f"dPsi{B + 1}x{k}")
                      for B in range(16) for k in range(8)}
rename_functions = {psi[B]: sp.Symbol(f"Psi{B + 1}") for B in range(16)}
```

To compare with the records' sixteen equations, the derivatives $\partial\psi_B/\partial x_k$ are renamed as plain symbols `dPsi<B>x<k>` (with the number $k$ of the coordinate $x_k$, 0 to 7) and the functions as `Psi<B>`. The order matters, as the comment says: renaming the functions first would turn their derivatives into derivatives of constants, which are zero.

```python
def same_components(equations):
    """True when the 16 left sides of the record equal ours."""
    same = True
    for A, equation in enumerate(equations):
        left = equation.split("==")[0]  # the record: left side == V*Psi[A]
        left = left.replace(chr(34), "")  # chr(34) is the double-quote character
        # dd[x4, Psi[14]] (the derivative of Psi_14 by x4) becomes dPsi14x4:
        left = re.sub(r"dd\[x(\d), Psi\[(\d+)\]\]", r"dPsi\2x\1", left)
        left = re.sub(r"Psi\[(\d+)\]", r"Psi\1", left)
        record_left = wolfram_to_sympy(left, RECORD_NAMES)
        mine = dirac[A].subs(rename_derivatives).subs(rename_functions)
        same = same and is_zero(mine - record_left)
    return same
```

`same_components(equations)` compares the sixteen equations of the record with the notebook's; the text in triple quotes under `def` (a **docstring**) says what it returns. For each record equation (`enumerate` numbers them from 0) the text left of `==` is taken (the right side is $V\Psi_A$ and not needed). `chr(34)` is the double-quote character, which is removed. The pattern `dd\[x(\d), Psi\[(\d+)\]\]` matches texts such as `dd[x4, Psi[14]]`, the derivative of $\psi_{14}$ by $x_4$; `\d` is a digit, `\d+` one or more digits, the parentheses capture them, and `re.sub` replaces the match by `dPsi14x4` (`\2` and `\1` insert the captured numbers). The second pattern turns `Psi[9]` into `Psi9`. The text is read with `wolfram_to_sympy`, and the notebook's component `A` with the same renaming must agree with it exactly.

```python
check(same_components(FORMULAS["field_equation_components"]),
      "all 16 components of the Dirac operator equal the record",
      record=f"{THEORY_FILE}, formula field_equation_components")
```

The check applies this comparison to the record's formula `field_equation_components`: all sixteen components agree.

```python
square = (gravity_term * gravity_term - (c_g**2 - v_g**2) * I16)
ranks = [(gamma[0] + sign * gamma[4]).rank() for sign in (1, -1)]
report("ranks of gamma^(x0) + gamma^(x4) and gamma^(x0) - gamma^(x4)", ranks)
both_fields = all(record_passed(REPORT_WL, name) for name in [
    "nontriviality_1_dirac16complex", "nontriviality_2_dirac16complex00"])
check(matrix_is_zero(square) and gamma[0] * gamma[0] == I16 and ranks == [8, 8]
      and both_fields and record_passed(REPORT_PY, "gravity_term_square"),
      "M M = (c_g^2 - v_g^2) 1: M Psi = 0 only for Psi = 0 unless c_g = +-v_g, "
      "and there M has rank 8",
      record=f"{REPORT_PY}, check gravity_term_square; {REPORT_WL}, checks "
             "nontriviality_1_dirac16complex and nontriviality_2_dirac16complex00")
```

`square` is $MM - (c_g^2 - v_g^2)1$ for $M = c_g\gamma^{(x0)} + v_g\gamma^{(x4)}$; it must be the zero matrix (Section 6.10). `ranks` holds the ranks of $\gamma^{(x0)} \pm \gamma^{(x4)}$ (`.rank()` computes the rank exactly, the number of independent rows), the form of $M$ where $c_g = \pm v_g$; it is printed, [8, 8]. The check requires the square, $(\gamma^{(x0)})^2 = 1$, both ranks 8, and the three record checks of the non-triviality as passed.

```python
square_history = sp.simplify((c_g**2 - v_g**2).subs(on_history).subs(history_values))
zero_time = sp.solve(sp.Eq(sp.Rational(3, 2) * sp.exp(H * x4 / 3),
                           sp.Rational(5, 6)), x4)  # c_g = v_g on the history
say(f"on the history c_g^2 - v_g^2 = {sp.expand(square_history)}")
report("the one time of the history with c_g = v_g, x4 H",
       f"{float(zero_time[0].subs(H, 1)):.4f}")
check(is_zero(square_history - H**2 * (sp.Rational(9, 4) * sp.exp(2 * H * x4 / 3)
                                      - sp.Rational(25, 36)))
      and len(zero_time) == 1 and is_zero(zero_time[0] - 3 * sp.log(
          sp.Rational(5, 9)) / H),
      "on the history c_g^2 - v_g^2 = H^2 ((9/4) e^(2 H x4/3) - 25/36), zero only "
      "at x4 = 3 ln(5/9)/H")
```

On the history the square is $c_g^2 - v_g^2$ with the history inserted (derivatives first); `sp.solve(sp.Eq(...), x4)` solves the equation $\frac32e^{Hx_4/3} = \frac56$, that is $c_g = v_g$ on the history divided by $H$, for $x_4$. The cell prints `on the history c_g^2 - v_g^2 = 9*H**2*exp(2*H*x4/3)/4 - 25*H**2/36` and the time of the solution with $H = 1$ and four decimals, $-1.7634$. The last check requires the square to be $H^2(\frac94e^{2Hx_4/3} - \frac{25}{36})$ and the equation to have exactly one solution, $x_4 = 3\ln(5/9)/H$. The cell prints three PASS lines with their records, the ranks, and the two lines on the history.

**In [21], figure 9: the factors in front of the derivatives.**

```python
fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
coefficient = [sp.lambdify(X4_SYMBOL, explicit_warp((1 / fa).subs(history)).subs(
    {H: 1, x0: sp.pi / 24})) for fa in f]
ax_left.semilogy(times, coefficient[1](times),
                 label="$1/f_1 = e^{-a_4}$ (3-space derivatives)")
ax_left.semilogy(times, coefficient[0](times), "--",
                 label="$1/f_0 = e^{a_4}b_4^{-1/2}\\tan z$ (hidden derivative)")
ax_left.semilogy(times, coefficient[5](times), "-.",
                 label="$1/f_5 = e^{a_4}b_4^{-1/2}/W$ (extra-time derivatives)")
ax_left.semilogy(times, np.ones_like(times), ":", color="black",
                 label="$1/f_4 = 1$ (time derivative)")
ax_left.set_xlabel("time $x_4$ (units $1/H$), history $a_4 = x_4$, "
                   "$b_4 = e^{4x_4/3}$")
ax_left.set_ylabel("factor in front of the derivative (log axis)")
ax_left.set_title("Where the deflation enters the field equation")
ax_left.legend(fontsize=7)
```

`coefficient` is a list of eight Python functions of the time, the factors $1/f_a$ on the history at $z = \pi/4$ with $H = 1$ (built as in In [8]). The left panel draws four of them on a logarithmic axis: $1/f_1 = e^{-a_4}$ in front of the 3-space derivatives, $1/f_0 = e^{a_4}b_4^{-1/2}\tan z$ in front of the hidden derivative, $1/f_5 = e^{a_4}b_4^{-1/2}/W$ in front of the extra-time derivatives, and $1/f_4 = 1$ in front of the time derivative (`np.ones_like` makes an array of ones).

```python
zz = np.linspace(0.03, np.pi - 0.03, 600)  # one cell
ax_right.semilogy(zz, np.abs(np.tan(zz)), label="$|1/f_0| = |\\tan z|$ (hidden)")
ax_right.semilogy(zz, np.abs(np.sin(zz)) ** (-1 / 6), "--",
                  label="$1/W = (\\sin^2 z)^{-1/12}$ (extra times)")
ax_right.axvline(np.pi / 2, color="gray", linewidth=0.8)  # the fold
ax_right.set_xlabel("hidden angle $z = 6Hx_0$ (radians), fold at $\\pi/2$")
ax_right.set_ylabel("factor at $x_4 = 0$ (log axis)")
ax_right.set_title("Dependence on the hidden direction")
ax_right.legend(fontsize=8, loc="upper left")
```

The right panel draws the two factors that depend on the hidden angle, $\lvert\tan z\rvert$ (the hidden factor divided by $e^{a_4}b_4^{-1/2}$) and $1/W = \lvert\sin z\rvert^{-1/6}$, at $x_4 = 0$ over one cell, on a logarithmic axis, with the fold marked.

```python
save_figure(fig, "derivative_coefficients",
            "The factors $1/f_a$ in front of the derivatives in the Dirac operator "
            ...
            "extra times.")
```

The figure is saved as `06a_9_derivative_coefficients.png`.

**What Figure 06a.9 shows.** On the left, the factor in front of the 3-space derivatives falls like $e^{-x_4}$ (3-space inflates, so a coordinate step means more and more length), while the two factors of the hidden block rise together like $e^{x_4/3}$, at one third of that rate (the hidden block deflates). This is how the deflation enters every derivative term of the field equation, besides the two terms $c_g$ and $v_g$. On the right, the hidden factor $\lvert\tan z\rvert$ is small near the tips and grows without bound at the fold, while $1/W$ is large only very near the tips.

**In [22], the negative control** (Section 6.10).

```python
f_control = ([sp.exp(a4) * sp.sqrt(b4) * sp.cot(z)] + [sp.exp(a4)] * 3
             + [sp.Integer(1)] + [sp.exp(a4) * sp.sqrt(b4) * W(x0)] * 3)  # GROWING
g_control = sp.diag(*[ETA[a] * f_control[a] ** 2 for a in range(8)])
e_control = sp.diag(*f_control)
Gam_control = christoffel(g_control, x)
omega_control = spin_connection(e_control, Gam_control, x, ETA)
Omega_control = spinor_connection(omega_control, S)
gup_control = curved_gammas(e_control, gamma)
slash_control = sum((gup_control[mu] * Omega_control[mu] for mu in range(8)), Z16)
```

The control metric: the same eight factors, except that the hidden scale is $e^{+a_4}b_4^{1/2}$ instead of $e^{-a_4}b_4^{1/2}$, so that the hidden direction and the three extra times grow like 3-space. The whole chain of In [7] to In [15] is repeated for it with the same four functions: metric, Christoffel symbols, spin connection, spinor connection, curved gammas and the contraction.

```python
alpha_control = sp.simplify(-(slash_control * gamma[4]).trace() / 16)
beta_control = sp.simplify((slash_control * gamma[0]).trace() / 16)
report("control: coefficient of gamma^(x4)", alpha_control)
report("control: coefficient of gamma^(x0)", beta_control)
```

The two coefficients of the control contraction, found with traces, are printed: `7*Derivative(a4(x4), x4)/2 + Derivative(b4(x4), x4)/b4(x4)`, that is $\frac72a_4' + b_4'/b_4$, and `3*H*exp(-a4(x4))/(2*sqrt(b4(x4)))`, that is $\frac32He^{-a_4}b_4^{-1/2}$.

```python
lead = json.loads(repository_file(REPORT_LEAD).read_text(encoding="utf-8"))
detail = [c["detail"] for c in lead["checks"]
          if c["name"] == "negative_control_growing_block"][0]
check(matrix_is_zero(slash_control - alpha_control * gamma[4] - beta_control * gamma[0])
      and is_zero(alpha_control - b4p / b4 - sp.Rational(7, 2) * a4p)
      and is_zero(beta_control - sp.Rational(3, 2) * H * sp.exp(-a4) / sp.sqrt(b4))
      and "+7/2 instead of -1/2" in detail
      and record_passed(REPORT_LEAD, "negative_control_growing_block"),
      "control with a growing hidden block: (b4'/b4 + (7/2) a4') gamma^(x4) + "
      "(3/2) H e^(-a4) b4^(-1/2) gamma^(x0)",
      record=f"{REPORT_LEAD}, check negative_control_growing_block")
```

The lead's report is read, and `detail` is the text of its check `negative_control_growing_block` (the list comprehension collects the details of all checks with that name, and `[0]` takes the one). The check requires the contraction to have no other part, the two coefficients to be those derived in Section 6.10, the lead's text to contain the words "+7/2 instead of -1/2", and the lead's check to be recorded as passed. The cell prints the two coefficients and one PASS line with its record.

**In [23], figure 10: the negative control as pictures.**

```python
rates = np.linspace(-2.0, 2.0, 81)  # values of a4'
rate_symbol = sp.Symbol("rate")
author_alpha = sp.lambdify(rate_symbol, sp.simplify(v_g.subs(b4p, 0)).subs(
    a4p, rate_symbol))  # the part with a4'
```

For the left panel the part of the $\gamma^{(x4)}$ coefficient proportional to $a_4'$ is turned into a function of a plain symbol `rate`: set $b_4' = 0$, then replace $a_4'$ by `rate`; this gives $-\frac12\,$rate for the corrected metric (`author_alpha`) and $+\frac72\,$rate for the control (`control_alpha`), evaluated at 81 rates from $-2$ to $2$.

```python
control_alpha = sp.lambdify(rate_symbol, sp.simplify(alpha_control.subs(
    b4p, 0)).subs(a4p, rate_symbol))
fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
ax_left.plot(rates, np.broadcast_to(author_alpha(rates), rates.shape),
             label="author: deflating hidden block ($-a_4'/2$)")
ax_left.plot(rates, np.broadcast_to(control_alpha(rates), rates.shape), "--",
             label="control: growing hidden block ($+7a_4'/2$)")
ax_left.set_xlabel("rate $a_4'$ (units of $H$)")
ax_left.set_ylabel("$a_4'$ part of the $\\gamma^{(x4)}$ coefficient (units of $H$)")
ax_left.set_title("The time-direction term")
ax_left.legend(fontsize=8)
```

The two straight lines are drawn (`np.broadcast_to` as in In [8]).

```python
history_numbers = {H: 1, x4: X4_SYMBOL}
author_beta = sp.lambdify(X4_SYMBOL, c_g.subs(history_values).subs(history_numbers))
control_beta = sp.lambdify(X4_SYMBOL, beta_control.subs(history_values).subs(
    history_numbers))
ax_right.semilogy(times, author_beta(times), label="author: $\\frac{3}{2} e^{x_4/3}$")
ax_right.semilogy(times, control_beta(times), "--",
                  label="control: $\\frac{3}{2} e^{-5x_4/3}$")
ax_right.set_xlabel("time $x_4$ (units $1/H$), history $a_4 = x_4$, "
                    "$b_4 = e^{4x_4/3}$")
ax_right.set_ylabel("coefficient of $\\gamma^{(x0)}$ (units of $H$, log axis)")
ax_right.set_title("The hidden-direction term")
ax_right.legend(fontsize=8)
```

For the right panel the coefficient of $\gamma^{(x0)}$ is evaluated on the history with $H = 1$, for the corrected metric ($c_g = \frac32e^{x_4/3}$) and for the control ($\frac32e^{-x_4}e^{-2x_4/3} = \frac32e^{-5x_4/3}$), and drawn on a logarithmic axis. In the labels `\\frac{3}{2}` is the fraction $\frac32$ in matplotlib's formula typesetting.

```python
save_figure(fig, "negative_control",
            "The negative control. Left: the part proportional to $a_4'$ of the "
            ...
            "which direction the hidden block changes.")
```

The figure is saved as `06a_10_negative_control.png`.

**What Figure 06a.10 shows.** On the left, the line of the corrected metric falls with the slope $-\frac12$ and the line of the control rises with the slope $\frac72$: the part of the time term that comes from $a_4'$ has the opposite sign and seven times the size when the hidden block grows instead of shrinking. On the right, two straight lines on the logarithmic axis: the hidden term of the corrected metric rises like $e^{x_4/3}$ because the hidden block shrinks, that of the control falls like $e^{-5x_4/3}$ because its hidden block grows; in both cases it is $\frac32H$ divided by the scale factor of the hidden block. The term sees in which direction the hidden block changes.

**In [24], the last checks.**

```python
cited = {
    REPORT_PY: ["clifford_relations", "gammas_real", "metric_from_vielbein_equals_SPEC",
                "sqrt_det_g", "christoffel_symmetric_metric_compatible",
                "vielbein_postulate", "spin_connection_antisymmetric",
                "spinor_connection_real", "nontriviality_Omega_zero_iff_flat",
                "Omega_x4_vanishes_Omega_x0_does_not",
                "covariant_constancy_D_mu_gamma_nu",
                "gamma_mu_Omega_mu_equals_hidden_block_terms", "per_direction_terms",
                "gravity_term_square", "anticommutator_gamma_Omega_vanishes",
                "divergence_of_sqrtg_gamma"],
    REPORT_WL: ["metric_is_the_corrected_metric", "vielbein_inverse", "sqrt_det_g",
                "christoffel_count", "vielbein_postulate", "omega_antisymmetric",
                "omega_components", "Omega_components", "S_rotates_gamma_with_omega",
                "gamma_covariantly_constant", "gammaOmega_total",
                "gammaOmega_per_direction", "gammaOmega_divergence_form",
                "Dirac_operator_explicit_C", "Dirac_operator_explicit_G",
                "nontriviality_1_dirac16complex", "nontriviality_2_dirac16complex00",
                "Omega_vanishes_iff_a4prime_b4prime_and_H_vanish", "block_form"],
    REPORT_LEAD: ["fixture_clifford", "vielbein_reproduces_metric",
                  "gamma_Omega_equals_hidden_block_terms",
                  "gamma_Omega_divergence_formula", "negative_control_growing_block"],
}
count = sum(len(names) for names in cited.values())
check(all(record_passed(path, name) for path, names in cited.items()
          for name in names),
      f"the {count} cited record checks are recorded as passed")
```

The dictionary `cited` lists every check of the three Revision reports that a statement of this notebook reproduces: 16 checks of the sympy report, 19 of the WolframScript report and 5 of the lead's report. The check requires all 40 to be recorded as passed and prints their number.

```python
expected = [f"06a_{k}_{name}.png" for k, name in enumerate([
    "polar_frame_and_spin_rotation", "vielbein_factors", "christoffel_pattern",
    "omega_heat_maps", "spinor_connection_heat_maps", "gamma_omega_per_direction",
    "gamma_omega_sum", "divergence_form", "derivative_coefficients",
    "negative_control"], 1)]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in expected),
      "all ten figure files exist")
all_checks_passed()
```

`expected` lists the ten figure file names, `06a_1_polar_frame_and_spin_rotation.png` to `06a_10_negative_control.png` (`enumerate(..., 1)` numbers from 1), and the second check requires all of them to exist in the folder `Revision/textbook/figures` (`output_file` is the folder into which the notebook wrote them). `all_checks_passed()` prints the last line, ALL 40 CHECKS PASSED (notebook 06a).

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

### 6.16 A boost in the plane of $x4$ and $x0$

**The boost.** Mix the time $x4$ (time-like) and the hidden direction $x0$ (space-like) with the **rapidity** $b$:

$$
e'^{(x4)} = \cosh b\;e^{(x4)} + \sinh b\;e^{(x0)}, \qquad e'^{(x0)} = \sinh b\;e^{(x4)} + \cosh b\;e^{(x0)},
$$

and keep the other six frame directions. Here $\cosh b = (e^b + e^{-b})/2$ and $\sinh b = (e^b - e^{-b})/2$ (Chapter 5), with $\cosh^2b - \sinh^2b = 1$. The matrix $\Lambda(b)$ is the identity except in the rows and columns of $x4$ and $x0$, where it is $\begin{pmatrix}\cosh b & \sinh b\\ \sinh b & \cosh b\end{pmatrix}$. In these two rows and columns $\eta$ is $\mathrm{diag}(-1, +1)$, and

$$
\Lambda^T\eta\Lambda = \begin{pmatrix}\cosh b & \sinh b\\ \sinh b & \cosh b\end{pmatrix}\begin{pmatrix}-\cosh b & -\sinh b\\ \sinh b & \cosh b\end{pmatrix}
$$

($\Lambda$ is symmetric, so $\Lambda^T = \Lambda$; and $\eta\Lambda$ is $\Lambda$ with the sign of its first row changed)

$$
= \begin{pmatrix}-\cosh^2b + \sinh^2b & -\cosh b\sinh b + \sinh b\cosh b\\ -\sinh b\cosh b + \cosh b\sinh b & -\sinh^2b + \cosh^2b\end{pmatrix} = \begin{pmatrix}-1 & 0\\ 0 & 1\end{pmatrix}
$$

(multiply row by column; then $\cosh^2 - \sinh^2 = 1$). So $\Lambda(b)$ keeps $\eta$ for every $b$, and $e' = \Lambda(b)e$ is a vielbein of the corrected metric. A rotation moves a direction along a circle; a boost moves it along a **hyperbola**, keeping $t^2 - y^2$ (figure 06b.1). Now let the rapidity depend on the time, $b = b(x_4)$, an arbitrary function with the derivative $b' = db/dx_4$. The Revision record checks the case of a constant rate, $b = \beta x_4 + b_0$ with two constants $\beta$ and $b_0$, and the general case; Notebook 06b works with the general function.

**The spinor boost.** Put $X = \gamma^{(x4)}\gamma^{(x0)}$. Then

$$
X^2 = \gamma^{(x4)}\gamma^{(x0)}\gamma^{(x4)}\gamma^{(x0)} = -\gamma^{(x4)}\gamma^{(x4)}\gamma^{(x0)}\gamma^{(x0)} = -(-1)(+1) = 1
$$

(exchange the two middle factors at the cost of a sign; then the Clifford relation twice). With $c = \cosh\frac b2$ and $s = \sinh\frac b2$ define $R = c - sX$; its inverse is $R^{-1} = c + sX$, because $(c - sX)(c + sX) = c^2 - s^2X^2 = c^2 - s^2 = 1$. Chapter 5 showed that $R$ is the spinor boost $\exp(-\frac b2X)$ in the plane $(x4, x0)$. $X$ anticommutes with $\gamma^{(x4)}$ and with $\gamma^{(x0)}$ (moving either through the product of two gammas meets one equal and one different factor: one sign) and commutes with the other six gammas (two signs). Hence $R^{-1}\gamma^cR = \gamma^c$ for the six other directions, and for $x4$:

$$
R^{-1}\gamma^{(x4)} = (c + sX)\gamma^{(x4)} = \gamma^{(x4)}(c - sX) = \gamma^{(x4)}R
$$

(move $\gamma^{(x4)}$ to the left through $X$ at the cost of a sign), so

$$
\begin{aligned}
R^{-1}\gamma^{(x4)}R &= \gamma^{(x4)}R^2 = \gamma^{(x4)}\big(c^2 + s^2 - 2cs\,X\big) \\
&= \cosh b\,\gamma^{(x4)} - \sinh b\,\gamma^{(x4)}X = \cosh b\,\gamma^{(x4)} + \sinh b\,\gamma^{(x0)}
\end{aligned}
$$

(multiply out $(c - sX)^2$ with $X^2 = 1$; the half-angle formulas $c^2 + s^2 = \cosh b$ and $2cs = \sinh b$ of Chapter 5; and $\gamma^{(x4)}X = \gamma^{(x4)}\gamma^{(x4)}\gamma^{(x0)} = -\gamma^{(x0)}$). In the same way $R^{-1}\gamma^{(x0)}R = \gamma^{(x0)}(\cosh b - \sinh b\,X) = \sinh b\,\gamma^{(x4)} + \cosh b\,\gamma^{(x0)}$, using $\gamma^{(x0)}X = \gamma^{(x0)}\gamma^{(x4)}\gamma^{(x0)} = -\gamma^{(x4)}$. These are the two rows of $\Lambda(b)$: **$R$ covers the boost.**

**The contraction in the boosted frame.** By Sections 6.15 and 6.8, $\sum_\mu\gamma'^\mu\Omega'_\mu = R\big(c_g\gamma^{(x0)} + v_g\gamma^{(x4)}\big)R^{-1} - \sum_\mu\gamma'^\mu(\partial_\mu R)R^{-1}$. The first term, line by line:

$$
R\gamma^{(x0)} = (c - sX)\gamma^{(x0)} = \gamma^{(x0)}(c + sX) = \gamma^{(x0)}R^{-1},
$$

$$
R\gamma^{(x0)}R^{-1} = \gamma^{(x0)}(c + sX)^2 = \gamma^{(x0)}(\cosh b + \sinh b\,X) = \cosh b\,\gamma^{(x0)} - \sinh b\,\gamma^{(x4)}
$$

(the same steps as before). Call $v = \cosh b\,\gamma^{(x0)} - \sinh b\,\gamma^{(x4)}$, and $w = R\gamma^{(x4)}R^{-1} = \gamma^{(x4)}(\cosh b + \sinh b\,X) = \cosh b\,\gamma^{(x4)} - \sinh b\,\gamma^{(x0)}$ (the same steps once more); the first term is $c_g\,v + v_g\,w$. The second term: $R$ depends on $x_4$ only, through $b(x_4)$, so only $\mu = x4$ contributes:

$$
\partial_4R = \tfrac{b'}2\big(s - cX\big), \qquad (\partial_4R)R^{-1} = \tfrac{b'}2(s - cX)(c + sX) = \tfrac{b'}2\big(sc + s^2X - c^2X - csX^2\big) = -\tfrac{b'}2X
$$

(the chain rule, $\frac{d}{db}\cosh\frac b2 = \frac12\sinh\frac b2$ and $\frac{d}{db}\sinh\frac b2 = \frac12\cosh\frac b2$; multiply out; $X^2 = 1$, so $sc - cs = 0$ and $(s^2 - c^2)X = -X$). Its trace is 0, because $X$ is a product of two different gammas. With $\gamma'^{x4} = R\gamma^{(x4)}R^{-1} = w$ ($f_4 = 1$):

$$
\gamma'^{x4}(\partial_4R)R^{-1} = -\tfrac{b'}2\big(\cosh b\,\gamma^{(x4)}X - \sinh b\,\gamma^{(x0)}X\big) = -\tfrac{b'}2\big(-\cosh b\,\gamma^{(x0)} + \sinh b\,\gamma^{(x4)}\big) = \tfrac{b'}2\,v
$$

($\gamma^{(x4)}X = -\gamma^{(x0)}$ and $\gamma^{(x0)}X = -\gamma^{(x4)}$). Subtracting:

$$
\sum_\mu\gamma'^\mu\Omega'_\mu = c_g\,v + v_g\,w - \tfrac{b'}2\,v = \Big(c_g - \frac{b'}{2}\Big)\big(\cosh b\,\gamma^{(x0)} - \sinh b\,\gamma^{(x4)}\big) + v_g\big(\cosh b\,\gamma^{(x4)} - \sinh b\,\gamma^{(x0)}\big) .
$$

At $b = 0$ for all times (no boost) this is $c_g\gamma^{(x0)} + v_g\gamma^{(x4)}$ again. For the constant rate $b = \beta x_4 + b_0$ the first coefficient is $c_g - \beta/2$, the record's formula; since $c_g = \frac32He^{a_4}b_4^{-1/2}$ changes with the time, a constant rate removes the first part only at the one time where $\beta = 2c_g$ (on the history, $\beta = 3H$ removes it at $x_4 = 0$, where $c_g = \frac32H$). **The rapidity with $b' = 2c_g = 3He^{a_4}b_4^{-1/2}$ removes the term $c_g\gamma^{(x0)}$ at every time and for all functions $a_4$, $b_4$**; on the history $b' = 3He^{Hx_4/3}$, so $b = 9(e^{Hx_4/3} - 1)$ with $b(0) = 0$ (the antiderivative; check: $\frac{d}{dx_4}9e^{Hx_4/3} = 3He^{Hx_4/3}$). What remains is $v_g\,w$.

**No boost removes the term $v_g$.** For any rapidity function write the contraction as $c_0\gamma^{(x0)} + c_4\gamma^{(x4)}$; collecting the terms of $v$ and $w$, $c_0 = (c_g - \frac{b'}2)\cosh b - v_g\sinh b$ and $c_4 = -(c_g - \frac{b'}2)\sinh b + v_g\cosh b$. Then

$$
\cosh b\,c_4 + \sinh b\,c_0 = \Big(c_g - \frac{b'}2\Big)\big(-\cosh b\sinh b + \sinh b\cosh b\big) + v_g\big(\cosh^2b - \sinh^2b\big) = v_g
$$

(multiply out; the first bracket is 0 and the second is 1). So the contraction vanishes only where $v_g = 0$, that is $b_4'/b_4 = a_4'/2$ ($b_4$ proportional to $e^{a_4/2}$); for general $a_4$ and $b_4$, and on the history of the record, where $v_g = \frac56H$, no boost in this plane removes it: there the remaining contraction is $\frac56H\,w$. The rescaling of Section 6.18 removes the whole contraction.

**But the spinor connection does not vanish.** For $b' = 2c_g$: $\Omega'_{x4} = R\Omega_{x4}R^{-1} - (\partial_4R)R^{-1} = 0 + c_g\,X = c_g\gamma^{(x4)}\gamma^{(x0)}$, which is not zero; $\Omega'_{x0} = R\Omega_{x0}R^{-1}$ (because $R$ does not depend on $x_0$) and $\Omega'_{x_i}$, $\Omega'_{x_t}$ are not zero because $\Omega_{x0}$, $\Omega_{x_i}$, $\Omega_{x_t}$ are not zero and $R$ is invertible. In this frame the field equation $\sum_\mu\gamma'^\mu D'_\mu\Psi' = (m + U')\Psi'$ keeps only the term $v_g\,w\,\Psi'$ ($\frac56H\,w\,\Psi'$ on the history of the record): the term $c_g\gamma^{(x0)}$ has gone, although the spinor connection is present in all eight directions. The canonical spin connection of the boosted frame has 14 independent nonzero components (Notebook 06b, In [7], COMPUTED exactly).

| statement | status | where it is verified |
| --- | --- | --- |
| the boosted frame gives the corrected metric; its canonical connection obeys the vielbein postulate | PROVED | Notebook 06b, In [7]; `python-scope.json` and `wolfram-scope.json`, checks `boosted_frame_reproduces_metric`, `boosted_frame_canonical_connection` |
| $\gamma'^\mu\Omega'_\mu = (c_g - \frac{b'}2)(\cosh b\,\gamma^{(x0)} - \sinh b\,\gamma^{(x4)}) + v_g(\cosh b\,\gamma^{(x4)} - \sinh b\,\gamma^{(x0)})$ | PROVED (for every $b(x_4)$ above; the record for $b = \beta x_4 + b_0$) | Notebook 06b, In [8]; both scope reports, check `boosted_frame_gammaOmega_formula` |
| for $b' = 2c_g$ the contraction is $v_g\,w$, $\frac56H\,w$ on the history: the boost removes only the $c_g$ term; $\Omega'_\mu \neq 0$ for all eight $\mu$ | PROVED | Notebook 06b, In [10]; both scope reports, check `boosted_frame_removes_only_the_H_term` |
| for every rapidity function $b(x_4)$, $\cosh b\,c_4 + \sinh b\,c_0 = v_g$: no boost in this plane removes the term $v_g$ | PROVED (above) | Notebook 06b, In [8]; `wolfram-scope.json`, check `boosted_frame_removes_only_the_H_term` |
| $R$ covers the boost; the pieces $c_gv + v_gw$ and $\frac{b'}2v$ | PROVED (above) | Notebook 06b, In [12] (its own checks) |

### 6.17 What no frame can remove: the curvature

Sections 6.5 and 6.16 taught the same lesson twice: the spin connection, and even its contraction, can look different, or vanish, in another frame. What does not depend on the frame is **curvature**.

**The Riemann and Ricci tensors.** Chapter 3 defined the Riemann tensor

$$
R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \sum_\lambda\big(\Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}\big),
$$

the Ricci tensor $R_{\sigma\nu} = \sum_\rho R^\rho{}_{\sigma\rho\nu}$, its mixed form $R^\mu{}_\nu = \sum_\sigma g^{\mu\sigma}R_{\sigma\nu}$ and the Ricci scalar $R = \sum_\mu R^\mu{}_\mu$. A space is flat exactly when the Riemann tensor vanishes everywhere. With the second index raised, $R^{ab}{}_{cd} = g^{bb}R^a{}_{bcd}$ (no sum, for the diagonal metric), the **curvature of the coordinate plane** of $a$ and $b$ is $K(a, b) = R^{ab}{}_{ab}$ (Chapter 3, Section 3.24, writes it $\sigma(a, b)$).

**Only the 28 plane curvatures.** For the corrected metric every component $R^{ab}{}_{cd}$ vanishes unless $\{c, d\} = \{a, b\}$: the Riemann tensor consists of the 28 numbers $K(a, b)$, each appearing four times ($R^{ab}{}_{ab} = R^{ba}{}_{ba} = K$, $R^{ab}{}_{ba} = R^{ba}{}_{ab} = -K$), 112 nonzero entries in all, and none of them depends on $x_0$ (PROVED; `curvature.json`, list `riemannMixedNonzero`; `python-lovelock-report.json`, check `mixed_riemann_only_sectional`; Notebook 06b, In [13]; Chapter 3, Section 3.24, computes all 28 by hand). Two of them by hand, as examples. For the plane of $x1$ and $x2$ put $\rho = x1$, $\sigma = \nu = x2$, $\mu = x1$ in the formula:

$$
R^{x1}{}_{x2x1x2} = \partial_1\Gamma^{x1}{}_{x2x2} - \partial_2\Gamma^{x1}{}_{x1x2} + \sum_\lambda\Gamma^{x1}{}_{x1\lambda}\Gamma^\lambda{}_{x2x2} - \sum_\lambda\Gamma^{x1}{}_{x2\lambda}\Gamma^\lambda{}_{x1x2} = 0 - 0 + a_4'\cdot e^{2a_4}a_4' - 0
$$

($\Gamma^{x1}{}_{x2x2} = 0$ and $\Gamma^{x1}{}_{x1x2} = 0$ because $f_1$ and $f_2$ do not depend on $x_1$ or $x_2$; in the first sum only $\lambda = x4$ survives, with $\Gamma^{x1}{}_{x1x4} = a_4'$ and $\Gamma^{x4}{}_{x2x2} = e^{2a_4}a_4'$ from Section 6.3; every $\Gamma^{x1}{}_{x2\lambda}$ vanishes), so $K(x1, x2) = g^{22}R^{x1}{}_{x2x1x2} = e^{-2a_4}\cdot e^{2a_4}a_4'^2 = a_4'^2$. For the plane of $x1$ and $x4$ put $\sigma = \nu = x4$:

$$
R^{x1}{}_{x4x1x4} = \partial_1\Gamma^{x1}{}_{x4x4} - \partial_4\Gamma^{x1}{}_{x1x4} + \sum_\lambda\Gamma^{x1}{}_{x1\lambda}\Gamma^\lambda{}_{x4x4} - \sum_\lambda\Gamma^{x1}{}_{x4\lambda}\Gamma^\lambda{}_{x1x4} = 0 - a_4'' + 0 - a_4'\cdot a_4'
$$

(every $\Gamma^\lambda{}_{x4x4}$ vanishes because $f_4 = 1$; in the last sum only $\lambda = x1$ survives), so $K(x1, x4) = g^{44}R^{x1}{}_{x4x1x4} = (-1)(-a_4'' - a_4'^2) = a_4'^2 + a_4''$. In the same way (Chapter 3, Section 3.24) the 28 planes fall into six kinds:

| planes | number | $K(a, b)$ | on the history |
| --- | --- | --- | --- |
| two 3-space directions | 3 | $a_4'^2$ | $H^2$ |
| a 3-space direction and the time | 3 | $a_4'^2 + a_4''$ | $H^2$ |
| a 3-space direction and a direction of the hidden block | 12 | $a_4'h_4$ | $-\frac13H^2$ |
| a direction of the hidden block and the time | 4 | $h_4^2 + h_4'$ | $\frac19H^2$ |
| two directions of the hidden block | 6 | $h_4^2 - H^2e^{2a_4}/b_4$ | $\frac19H^2 - H^2e^{2Hx_4/3}$ |

(the last column with $a_4' = H$, $a_4'' = 0$, $h_4 = -\frac13H$, $h_4' = 0$ and $e^{2a_4}/b_4 = e^{2Hx_4 - 4Hx_4/3} = e^{2Hx_4/3}$). The planes $(x0, x1)$ and $(x1, x5)$ are of the same kind, and so are $(x0, x5)$ and $(x5, x6)$: the hidden direction behaves exactly like an extra time, and in the six planes of the hidden block the warp contributes $-H^2/s_b^2$, the curvature $-H^2$ of the block of Chapter 3, Section 3.9, divided by the square of its scale factor.

**The Ricci tensor.** The mixed Ricci tensor is the sum of the plane curvatures, $R^a{}_a = \sum_{b\neq a}K(a, b)$, and it is **diagonal**: its 56 components off the diagonal vanish, because there are no other Riemann components. For a 3-space direction, line by line:

$$
R^{x1}{}_{x1} = K(x1, x2) + K(x1, x3) + K(x1, x4) + 4\,a_4'h_4 = 2a_4'^2 + a_4'^2 + a_4'' + 4a_4'\Big(\frac{b_4'}{2b_4} - a_4'\Big)
$$

(two 3-space planes, the plane with the time, and four planes with the hidden block; then the table and the definition of $h_4$)

$$
= -a_4'^2 + a_4'' + \frac{2a_4'b_4'}{b_4}
$$

(multiply out; $3a_4'^2 - 4a_4'^2 = -a_4'^2$). On the history this is $-H^2 + \frac83H^2 = \frac53H^2$. For the time, $R^{x4}{}_{x4} = 3(a_4'^2 + a_4'') + 4(h_4^2 + h_4')$, which is $3H^2 + \frac49H^2 = \frac{31}{9}H^2$ on the history. For the hidden direction and for each extra time (they share one value),

$$
R^{x0}{}_{x0} = R^{x_t}{}_{x_t} = 3a_4'h_4 + (h_4^2 + h_4') + 3\Big(h_4^2 - \frac{H^2e^{2a_4}}{b_4}\Big) ,
$$

which on the history is $-H^2 + \frac19H^2 + \frac13H^2 - 3H^2e^{2Hx_4/3} = -\big(\frac59 + 3e^{2Hx_4/3}\big)H^2$ (insert the table; $-1 + \frac19 + \frac39 = -\frac59$). The Ricci scalar is the sum of the eight diagonal components, $R = 4R^{x0}{}_{x0} + 3R^{x1}{}_{x1} + R^{x4}{}_{x4}$, on the history

$$
R = -\big(\tfrac{20}{9} + 12e^{2Hx_4/3}\big)H^2 + 5H^2 + \tfrac{31}{9}H^2 = H^2\Big(\frac{56}{9} - 12e^{2Hx_4/3}\Big)
$$

($-\frac{20}{9} + \frac{45}{9} + \frac{31}{9} = \frac{56}{9}$). These agree with the record's formulas (`field-theory.json`, formulas `ricci_mixed_nonzero` and `ricci_scalar`, written out for general $a_4$ and $b_4$; Notebook 06b, In [14], prints them). The Einstein tensor $G^\mu{}_\nu = R^\mu{}_\nu - \frac12\delta^\mu_\nu R$ is diagonal as well (`curvature.json`, key `einsteinMixed`). A dated comparison: the metric of 2026-10-14, withdrawn on 2026-10-16, had two Ricci components off the diagonal and the value $R^{x0}{}_{x0} = -6H^2$ for every $b_4$; the corrected metric has neither.

**The flat member.** For $a_4 = 0$ and $b_4 = H^2x_4^2$ ($x_4 > 0$) every plane curvature vanishes: $a_4' = a_4'' = 0$ kills the first three kinds; $h_4 = b_4'/(2b_4) = \frac{2H^2x_4}{2H^2x_4^2} = \frac1{x_4}$ and $h_4' = -\frac1{x_4^2}$ give $h_4^2 + h_4' = 0$; and $h_4^2 - H^2e^0/(H^2x_4^2) = \frac1{x_4^2} - \frac1{x_4^2} = 0$. So this member of the family is 8-dimensional flat space in unusual coordinates (the record calls it Milne form), and on the history of the record the metric is curved ($K(x1, x2) = H^2 \neq 0$). PROVED; `wolfram-field-theory.json`, check `flat_member_and_curvature`; `python-field-theory.json`, check `curvature_and_flat_member`; Notebook 06b, In [14]. On the flat member the contraction of the diagonal vielbein is not zero: $c_g = \frac32He^0(H^2x_4^2)^{-1/2} = \frac{3}{2x_4}$ and $v_g = \frac{2}{x_4}$ (insert $a_4 = 0$ and $b_4 = H^2x_4^2$). There it is purely the turning of the chosen frame, as in the polar plane of Section 6.5.

**The term sees the hidden block.** The contraction $c_g\gamma^{(x0)} + v_g\gamma^{(x4)}$ contains $a_4$, through $e^{a_4}$ in $c_g$ and $a_4'$ in $v_g$: it follows the deflation of the hidden block (record scope check `gammaOmega_sees_the_hidden_block`, both scope reports; Notebook 06b, In [14]).

**The curvature of the spinor connection.** The commutator of two covariant derivatives of a spinor, line by line:

$$
D_\mu D_\nu\Psi = \partial_\mu\big(\partial_\nu\Psi + \Omega_\nu\Psi\big) + \Omega_\mu\big(\partial_\nu\Psi + \Omega_\nu\Psi\big) = \partial_\mu\partial_\nu\Psi + (\partial_\mu\Omega_\nu)\Psi + \Omega_\nu\partial_\mu\Psi + \Omega_\mu\partial_\nu\Psi + \Omega_\mu\Omega_\nu\Psi
$$

(the definition twice; the product rule). Subtract the same with $\mu$ and $\nu$ exchanged: $\partial_\mu\partial_\nu\Psi$ and the two middle terms are symmetric and cancel, and

$$
\big(D_\mu D_\nu - D_\nu D_\mu\big)\Psi = F_{\mu\nu}\Psi, \qquad F_{\mu\nu} = \partial_\mu\Omega_\nu - \partial_\nu\Omega_\mu + [\Omega_\mu, \Omega_\nu] .
$$

**Theorem (quoted, and checked exactly for this metric).** $F_{\mu\nu} = \frac12\sum_{a,b}R_{ab\mu\nu}S^{ab}$, where $R_{ab\mu\nu}$ is the Riemann tensor with its first two indices turned into frame indices (for the diagonal vielbein $R_{ab\mu\nu} = \eta_{aa}f_a R^a{}_{b\mu\nu}/f_b$). The general proof is a standard but long computation that this book does not reproduce; for the corrected metric the identity is PROVED by exact computation in all 28 coordinate planes (`wolfram-field-theory.json`, check `spin_curvature_equals_Riemann`, and `python-field-theory.json`, check `spinor_curvature_equals_riemann`; Notebook 06b, In [16]). The spinor curvature is the Riemann curvature acting on spinors. Because only the plane curvatures exist, each $F_{\mu\nu}$ is a single generator: with $R^\mu{}_{\nu\mu\nu} = g_{\nu\nu}K(\mu, \nu) = \eta_{\nu\nu}f_\nu^2K(\mu, \nu)$,

$$
R_{\mu\nu\mu\nu} = \eta_{\mu\mu}\frac{f_\mu}{f_\nu}\,\eta_{\nu\nu}f_\nu^2K(\mu, \nu) = \eta_{\mu\mu}\eta_{\nu\nu}f_\mu f_\nu K(\mu, \nu), \qquad F_{\mu\nu} = \eta_{\mu\mu}\eta_{\nu\nu}f_\mu f_\nu K(\mu, \nu)\,S^{\mu\nu}
$$

(the frame form of the diagonal vielbein; the two terms $(a, b) = (\mu, \nu)$ and $(\nu, \mu)$ of the sum are equal, which uses up the factor $\frac12$). Its size, the square root of the sum of the squares of its 256 entries, is $2\lvert f_\mu f_\nu K(\mu, \nu)\rvert$, because $S^{\mu\nu} = \frac12\gamma^{(\mu)}\gamma^{(\nu)}$ has 16 entries $\pm\frac12$ ($\sqrt{16\cdot\frac14} = 2$).

**It cannot be removed by a change of frame.** By Section 6.15, $D'_\mu(R\Psi) = R\,D_\mu\Psi$ for every spinor. Apply it twice, the second time to the spinor $D_\nu\Psi$: $D'_\mu D'_\nu(R\Psi) = D'_\mu(R\,D_\nu\Psi) = R\,D_\mu D_\nu\Psi$. Subtracting the same with $\mu$ and $\nu$ exchanged gives $F'_{\mu\nu}R\Psi = R\,F_{\mu\nu}\Psi$ for every $\Psi$, so

$$
F'_{\mu\nu} = R\,F_{\mu\nu}\,R^{-1} .
$$

An invertible $R$ can change the entries of $F_{\mu\nu}$ but cannot make a nonzero matrix zero. If some frame had $\Omega'_\mu = 0$ for all $\mu$, its $F'_{\mu\nu}$ would vanish, hence $F_{\mu\nu}$ in every frame, hence the Riemann tensor, which contradicts $K(x1, x2) = H^2$ on the history of the record. **Wherever the metric is curved, no frame makes the spin connection vanish**; on the flat member it can be removed, as in the polar plane. At the sample point of Notebook 06b (the history at $a_4 = \frac12$, $z = \pi/4$, $H = 1$) all 28 planes are curved; the largest size, $5.437$, belongs to the three planes inside 3-space ($2f_1^2K = 2e\cdot1$), and the smallest, $0.178$, to the three planes of the time with an extra time ($2f_5\cdot\frac19$ with $f_5 = s_bW = 0.799$), closely followed by the plane of the hidden direction and the time, $0.188$ (Notebook 06b, In [17], COMPUTED, and figure 5). In the boosted frame with $b' = 2c_g$, where the $c_g$ term of the contraction vanished, $F'_{x0\,x5} = RF_{x0\,x5}R^{-1}$ is not zero (In [16]).

| statement | status | where it is verified |
| --- | --- | --- |
| only the 28 plane curvatures are nonzero (112 entries $R^{ab}{}_{cd}$), free of $x_0$; the table of the six kinds | PROVED ($K(x1, x2)$ and $K(x1, x4)$ by hand above, all in Section 3.24) | `curvature.json`, list `riemannMixedNonzero`; `python-lovelock-report.json`, check `mixed_riemann_only_sectional`; Notebook 06b, In [13] |
| the Ricci and Einstein tensors are diagonal; $R^{x0}{}_{x0} = R^{x_t}{}_{x_t}$; on the history $R = H^2(\frac{56}{9} - 12e^{2Hx_4/3})$ | PROVED | `field-theory.json`, formulas `ricci_mixed_nonzero`, `ricci_scalar`; `wolfram-field-theory.json`, checks `ricci_mixed_components`, `ricci_scalar`; `curvature.json`, key `einsteinMixed`; Notebook 06b, In [14] |
| flat for $a_4 = 0$, $b_4 = H^2x_4^2$; curved on the history | PROVED | `wolfram-field-theory.json`, check `flat_member_and_curvature`; `python-field-theory.json`, check `curvature_and_flat_member`; Notebook 06b, In [14] |
| $\gamma^\mu\Omega_\mu$ contains $a_4$ | PROVED | both scope reports, check `gammaOmega_sees_the_hidden_block`; Notebook 06b, In [14] |
| $F_{\mu\nu} = \frac12R_{ab\mu\nu}S^{ab} = \eta_{\mu\mu}\eta_{\nu\nu}f_\mu f_\nu K(\mu, \nu)S^{\mu\nu}$ in all 28 planes | PROVED for this metric (general theorem quoted) | `wolfram-field-theory.json`, check `spin_curvature_equals_Riemann`; `python-field-theory.json`, check `spinor_curvature_equals_riemann`; Notebook 06b, In [16] |
| $F' = RFR^{-1}$; in the boosted frame $F'_{x0\,x5} \neq 0$ | PROVED | Notebook 06b, In [16]; both scope reports, check `boosted_frame_curvature_nonzero` |
| the sizes $\lVert F_{\mu\nu}\rVert$ at the sample point, from $0.178$ to $5.437$ | COMPUTED | Notebook 06b, In [17] |

### 6.18 Changing the field variable: the rescaling $\Psi = e^{a_4/2}b_4^{-1}(\sin^2 z)^{-1/8}\,\chi$

A frame change is one way to remove part of the term $\gamma^\mu\Omega_\mu$; a change of the field variable removes all of it. Keep the diagonal vielbein, and write the field as a known function times a new field,

$$
\Psi = w_r\,\chi, \qquad w_r = e^{a_4/2}b_4^{-1}(\sin^2 z)^{-1/8} = e^{a_4/2}b_4^{-1}W^{-3/2} .
$$

This is the weight of the Revision record (`python-scope.json` and `wolfram-scope.json`, check `rescaling_removes_the_connection_term`). Its square is $w_r^2 = e^{a_4}b_4^{-2}W^{-3}$, the inverse of $e^{-a_4}b_4^2W^3$, which is the volume factor in the coordinates $(y, x_1, \dots, x_7)$ of Chapter 3, Section 3.9 ($W^3 = e^{3Hy}$ there): $\chi$ is the field multiplied by the square root of that volume factor. On the history of the record $w_r = e^{Hx_4/2}e^{-4Hx_4/3}W^{-3/2} = e^{-5Hx_4/6}W^{-3/2}$: the weight falls with the time like $e^{-5Hx_4/6}$. The Kohn-Sham states of the Revision record (Chapter 14) are written with exactly this factor.

**The derivation.** By the product rule, $\partial_\mu(w_r\chi) = (\partial_\mu w_r)\chi + w_r\,\partial_\mu\chi$, so

$$
\sum_\mu\gamma^\mu D_\mu\Psi = w_r\sum_\mu\gamma^\mu\partial_\mu\chi + \Big(\sum_\mu\gamma^\mu\partial_\mu w_r + w_r\sum_\mu\gamma^\mu\Omega_\mu\Big)\chi
$$

($w_r$ is a number at each point and commutes with every matrix). Only $x_0$ and $x_4$ appear in $w_r$, with $\gamma^{x0} = e^{a_4}b_4^{-1/2}\tan z\,\gamma^{(x0)}$ and $\gamma^{x4} = \gamma^{(x4)}$, and $\sum_\mu\gamma^\mu\Omega_\mu = c_g\gamma^{(x0)} + v_g\gamma^{(x4)}$ (Section 6.8), so the bracket is

$$
\big(e^{a_4}b_4^{-1/2}\tan z\,\partial_0w_r + c_g\,w_r\big)\gamma^{(x0)} + \big(\partial_4w_r + v_g\,w_r\big)\gamma^{(x4)} .
$$

Now, with the rule $\partial_0W = H\cot z\,W$ of Section 6.3 and the power rule,

$$
\partial_0W^{-3/2} = -\tfrac32W^{-5/2}\,H\cot z\,W = -\tfrac32H\cot z\,W^{-3/2}, \qquad\text{so}\qquad \partial_0w_r = -\tfrac32H\cot z\,w_r ,
$$

and

$$
e^{a_4}b_4^{-1/2}\tan z\,\partial_0w_r = -\tfrac32He^{a_4}b_4^{-1/2}\tan z\cot z\,w_r = -c_g\,w_r
$$

($\tan z\cot z = 1$). In the same way $\partial_4\ln w_r = \frac{a_4'}2 - \frac{b_4'}{b_4}$ (the logarithm of a product; the derivatives of $\frac12a_4$ and $-\ln b_4$), so $\partial_4w_r = (\frac{a_4'}2 - \frac{b_4'}{b_4})w_r = -v_g\,w_r$. Both brackets are zero, $(-c_gw_r + c_gw_r)\gamma^{(x0)} + (-v_gw_r + v_gw_r)\gamma^{(x4)} = 0$:

$$
\sum_\mu\gamma^\mu D_\mu(w_r\chi) = w_r\sum_\mu\gamma^\mu\partial_\mu\chi .
$$

**The rescaled field equation.** The bilinear is $S[\Psi] = \Psi^\dagger C\Psi$; $w_r$ is real and positive, so

$$
S[w_r\chi] = w_r^2\,\chi^\dagger C\chi = e^{a_4}b_4^{-2}W^{-3}\,S[\chi] = \frac{e^{a_4}\,S[\chi]}{b_4^2\lvert\sin z\rvert^{1/2}}
$$

($W^{-3} = (\sin^2 z)^{-1/4} = \lvert\sin z\rvert^{-1/2}$). For the potential $U = \frac\lambda2S^2$, $U'(S) = \lambda S$, and the field equation $\sum_\mu\gamma^\mu D_\mu\Psi = (m + \lambda S[\Psi])\Psi$ becomes, after division by $w_r$,

$$
\sum_\mu\gamma^\mu\partial_\mu\chi = \Big(m + \frac{\lambda\,e^{a_4}S[\chi]}{b_4^2\lvert\sin z\rvert^{1/2}}\Big)\chi .
$$

For $U = 0$ ($\lambda = 0$) the term $\gamma^\mu\Omega_\mu$ is removed completely. For $U \neq 0$ it reappears in another form: as the coupling $\lambda e^{a_4}S[\chi]/(b_4^2\lvert\sin z\rvert^{1/2})$, which depends on the hidden coordinate and on the time. What remains of gravity in the equation of $\chi$ are the vielbein factors $1/f_a$ in front of every derivative. The record's exact solution family (i-b) (`field-theory.json`, formula `exact_solutions`) contains the same weight.

| statement | status | where it is verified |
| --- | --- | --- |
| $\sum_\mu\gamma^\mu D_\mu(w_r\chi) = w_r\sum_\mu\gamma^\mu\partial_\mu\chi$ for $w_r = e^{a_4/2}b_4^{-1}(\sin^2 z)^{-1/8}$ and any 16 functions $\chi$ | PROVED | Notebook 06b, In [18]; `python-scope.json` and `wolfram-scope.json`, check `rescaling_removes_the_connection_term` |
| $S[w_r\chi] = e^{a_4}b_4^{-2}\lvert\sin z\rvert^{-1/2}S[\chi]$; the rescaled equation with $U = \frac\lambda2S^2$ | PROVED | Notebook 06b, In [18]; both scope reports, check `rescaled_equation_quadratic_potential` |

### 6.19 Example: Notebook 06b

Notebook 06b checks Sections 6.15 to 6.18 with exact algebra, for arbitrary functions $a_4(x_4)$ and $b_4(x_4)$ and every real $z$. It rebuilds the tools of Notebook 06a (so that it runs on its own), recomputes the diagonal vielbein and its contraction $c_g\gamma^{(x0)} + v_g\gamma^{(x4)}$ as a control, builds the boost matrix and checks that it keeps $\eta$, and draws the boosted frame on its hyperbolas. It then computes the canonical spin connection of the boosted frame with an arbitrary rapidity function $b(x_4)$, checks the vielbein postulate, the formula $(c_g - \frac{b'}2)(\cosh b\,\gamma^{(x0)} - \sinh b\,\gamma^{(x4)}) + v_g(\cosh b\,\gamma^{(x4)} - \sinh b\,\gamma^{(x0)})$, the invariant $\cosh b\,c_4 + \sinh b\,c_0 = v_g$ and the removal of the $c_g$ term (and of nothing else) for $b' = 2c_g$, and explains it with the explicit spinor boost $R$. It computes the Riemann tensor (only the 28 plane curvatures), the Ricci and Einstein tensors, the flat member, the spinor curvature in all 28 planes, and finally the rescaling. It compares every result that the Revision records also contain with the records (the record `field-theory.json`, its two reports, the two scope reports and the curvature record, all for the corrected metric), draws six figures, needs no Rust, runs in a few minutes and ends with the line ALL 29 CHECKS PASSED (notebook 06b).

<!-- NOTEBOOK 06b -->

### 6.22 Line-by-line walk-through of Notebook 06b

The notebook has 20 code cells, In [1] to In [20]; this section explains every line of every one of them. As in Section 6.14, a line `...` in a quoted figure cell stands for the remaining lines of a long caption, printed in full in Section 6.21, and the output of In [k] is printed there under the label Out [k].

**In [1], the set-up cell.** Its comment lines are the run instructions of Section 6.20. Its code is, line for line, the set-up code of Notebook 06a explained at the beginning of Section 6.14, with the single difference

```python
NOTEBOOK_ID = "06b"  # this notebook: chapter 06, example b
```

so that the figures are named `06b_<k>_<name>.png` and the captions file is `Revision/textbook/figures/06b.captions.json`. It prints one line, Set-up of notebook 06b complete: repository folder found, helpers defined.

**In [2], the tools and the history.**

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
NAMES = fixture["coordinates"]  # ["x0", ..., "x7"]
ETA = fixture["eta"]  # +1 space-like, -1 time-like
gamma = [sp.Matrix(rows) for rows in fixture["gamma"]]  # gamma[a] = gamma^(xa)
C = sp.Matrix(fixture["C"])  # the author's C (Dirac adjoint Psibar = Psi^dagger C)
I16, Z16 = sp.eye(16), sp.zeros(16, 16)
```

The record `Revision/algebra/gammas.json` is read as in Notebook 06a: the direction names, the signs of $\eta$, and the eight gammas as exact matrices. New is `C`, the author's matrix $C$ of the Dirac adjoint $\bar\Psi = \Psi^\dagger C$ stored in the same record (Chapter 5); In [18] needs it for the bilinear $S = \Psi^\dagger C\Psi$. `I16, Z16 = ...` gives two names at once (the identity and the zero matrix).

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
CURVATURE = "Revision/gkd_lovelock/results/curvature.json"
CURVATURE_PY = "Revision/gkd_lovelock/results/python-lovelock-report.json"
PARAMETERS = "Revision/kohn_sham/results/parameters.json"
physics = json.loads(repository_file(PARAMETERS).read_text(encoding="utf-8"))["physics"]
A_EXACT = sp.nsimplify(physics["historyA"])  # the slope A of the history, 1
BETA_B4 = sp.nsimplify(physics["historyBeta"])  # the exponent of b4, 4/3
B4_ZERO = sp.nsimplify(physics["historyB4AtZero"])  # b4(0) = 1
check(A_EXACT == 1 and BETA_B4 == sp.Rational(4, 3) and B4_ZERO == 1,
      "the history of the record: a4 = A H x4, b4 = b4(0) e^(4 A H x4/3), A = 1, "
      "b4(0) = 1",
      record=f"{PARAMETERS}, physics.historyA, historyBeta and historyB4AtZero")
```

Names for the Revision files that the notebook reproduces: the two scope reports (sympy and WolframScript), the two field-theory reports, the formula file `field-theory.json`, the curvature record `curvature.json` of the Revision Lovelock work and its independent sympy report, and the parameters of the Kohn-Sham work. From the last, the history: the slope $A = 1$, the exponent $\beta = \frac43$ of $b_4$ and $b_4(0) = 1$, as exact fractions; the check names the three keys. The cell prints two PASS lines.

**In [3], the four general functions.** They are the functions of Notebook 06a, In [4], written a little more compactly.

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

The canonical spin connection with the first index lowered. Here it matters that the function accepts ANY vielbein matrix `e`, not only a diagonal one: In [7] gives it the boosted vielbein, which has off-diagonal entries in the rows and columns of $x4$ and $x0$, and then the inverse `E = e.inv()` and the sums over `nu` and `lam` really have several terms.

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


say("defined: christoffel, spin_connection, spinor_connection, curved_gammas")
```

The curved gammas, and one output line that names the four functions.

**In [4], the diagonal vielbein again (the control).**

```python
x = sp.symbols("x0:8", real=True)  # x[0] = x0, ..., x[4] = x4, ..., x[7] = x7
x0, x4 = x[0], x[4]
H = sp.Symbol("H", positive=True)
a4 = sp.Function("a4")(x4)  # any function of the time
b4 = sp.Function("b4", positive=True)(x4)  # any positive function of the time
a4p, b4p = sp.Derivative(a4, x4), sp.Derivative(b4, x4)
z = 6 * H * x0


class W(sp.Function):
    """The warp factor W(x0) = (sin(6 H x0)^2)^(1/12) > 0 of the extra times."""

    def fdiff(self, argindex=1):
        """dW/dx0 = H cot(6 H x0) W, for every real z = 6 H x0 with sin z != 0."""
        return H * sp.cot(6 * H * self.args[0]) * self

    def _eval_is_positive(self):
        return True  # the positive root
```

The symbols of Notebook 06a, In [7]: the coordinates, $H > 0$, the two unknown functions $a_4$ and $b_4 > 0$, the short names `a4p`, `b4p` for their derivatives, $z = 6Hx_0$, and the warp factor $W$ as a function that knows only its derivative rule $\partial_0W = H\cot z\,W$ and its sign, so that every result holds for every real $z$.

```python
s_b = sp.exp(-a4) * sp.sqrt(b4)  # the hidden scale
f = ([s_b * sp.cot(z)] + [sp.exp(a4)] * 3 + [sp.Integer(1)]
     + [s_b * W(x0)] * 3)  # f_0, ..., f_7
g = sp.diag(*[ETA[a] * f[a] ** 2 for a in range(8)])  # the corrected metric
e = sp.diag(*f)  # the diagonal vielbein
on_history = {b4p: BETA_B4 * A_EXACT * H * b4, a4p: A_EXACT * H}  # the derivatives
history_values = {a4: A_EXACT * H * x4, b4: B4_ZERO * sp.exp(BETA_B4 * A_EXACT * H * x4)}
```

The hidden scale $s_b$, the eight factors of the diagonal vielbein, the corrected metric and the vielbein, as in Notebook 06a; and the two substitutions of the history, first for the derivatives ($b_4' = \beta AHb_4$, $a_4' = AH$) and then for the functions ($a_4 = AHx_4$, $b_4 = b_4(0)e^{\beta AHx_4}$).

```python
Gam = christoffel(g, x)
omega = spin_connection(e, Gam, x, ETA)
Omega = spinor_connection(omega, S)
gup = curved_gammas(e, gamma)
slash = sum((gup[mu] * Omega[mu] for mu in range(8)), Z16)
```

The Christoffel symbols, the spin connection, the spinor connection, the curved gammas and the contraction of the diagonal vielbein.

```python
c_g = sp.Rational(3, 2) * H * sp.exp(a4) / sp.sqrt(b4)  # coefficient of gamma^(x0)
v_g = b4p / b4 - a4p / 2  # coefficient of gamma^(x4)
slash_history = slash.subs(on_history).subs(history_values)
check(matrix_is_zero(slash - c_g * gamma[0] - v_g * gamma[4])
      and matrix_is_zero(slash_history - sp.Rational(3, 2) * H * sp.exp(H * x4 / 3)
                         * gamma[0] - sp.Rational(5, 6) * H * gamma[4]),
      "control: the diagonal vielbein gives gamma^mu Omega_mu = c_g gamma^(x0) + "
      "v_g gamma^(x4), on the history (3/2) H e^(H x4/3) gamma^(x0) + (5/6) H "
      "gamma^(x4)",
      record=f"{SCOPE_PY}, check rescaling_removes_the_connection_term")
```

The control check: the contraction is $c_g\gamma^{(x0)} + v_g\gamma^{(x4)}$, and on the history $\frac32He^{Hx_4/3}\gamma^{(x0)} + \frac56H\gamma^{(x4)}$, the result of Notebook 06a. The record line names the scope check `rescaling_removes_the_connection_term`, whose text begins with exactly this control. One PASS line.

**In [5], the boost matrix** (Section 6.16).

```python
def boost(b):
    """The 8 x 8 boost matrix Lambda(b) in the plane of x0 (index 0) and x4 (4)."""
    L = sp.eye(8)
    L[0, 0], L[0, 4], L[4, 0], L[4, 4] = sp.cosh(b), sp.sinh(b), sp.sinh(b), sp.cosh(b)
    return L
```

`boost(b)` returns the $8 \times 8$ identity with the four entries of the rows and columns 0 ($x0$) and 4 ($x4$) replaced by $\cosh b$, $\sinh b$, $\sinh b$, $\cosh b$. The four assignments are made in one line (a tuple of four places receives a tuple of four values).

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
    c_b, s_b_value = np.cosh(b_value), np.sinh(b_value)
    ax.annotate("", xy=(c_b, s_b_value), xytext=(0, 0), arrowprops=dict(
        arrowstyle="-|>", color="tab:blue", alpha=alpha, linewidth=1.6))
    ax.annotate("", xy=(s_b_value, c_b), xytext=(0, 0), arrowprops=dict(
        arrowstyle="-|>", color="tab:orange", alpha=alpha, linewidth=1.6))
    ax.text(c_b + 0.04, s_b_value - 0.12, f"$b = {b_value:g}$", fontsize=8,
            color="tab:blue")
    ax.text(s_b_value - 0.30, c_b + 0.06, f"$b = {b_value:g}$", fontsize=8,
            color="tab:orange")
```

For the three rapidities $b = 0$, $0.5$ and $1$ two arrows are drawn from the origin with `annotate` (an annotation with an empty text and an arrow): the boosted time direction $(\cosh b, \sinh b)$ in blue and the boosted hidden direction $(\sinh b, \cosh b)$ in orange, the larger rapidities fainter (`alpha` is the opacity), and beside each arrow its rapidity (`{b_value:g}` prints the number in its shortest form). The name `s_b_value` is used for $\sinh b$ because the name `s_b` already holds the hidden scale.

```python
ax.set_xlim(-0.4, 2.3)
ax.set_ylim(-0.25, 2.3)
ax.set_aspect("equal")
ax.set_xlabel("component along $e^{(x4)}$ (time), $t$")
ax.set_ylabel("component along $e^{(x0)}$ (hidden direction), $y$")
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

The figure is saved as `06b_1_boost_hyperbolas.png`.

**What Figure 06b.1 shows.** At $b = 0$ the two arrows point along the axes. As $b$ grows, the blue arrow (the time direction) moves along its hyperbola away from the horizontal axis and the orange arrow (the hidden direction) along its hyperbola away from the vertical axis: both tilt symmetrically towards the light line, and both get longer on the paper, while their $\eta$-lengths stay $-1$ and $+1$. They remain perpendicular in the sense of $\eta$ ($-\cosh b\sinh b + \sinh b\cosh b = 0$). A boost never brings the arrows back, unlike a rotation.

**In [7], the boosted vielbein and its spin connection.**

```python
b = sp.Function("b", real=True)(x4)  # the rapidity: any function of the time
bp = sp.Derivative(b, x4)  # its rate b'
L = boost(b)
e_boosted = L * e  # e'^a_mu = sum_c Lambda^a_c e^c_mu
check(matrix_is_zero(e_boosted.T * eta_matrix * e_boosted - g),
      "the boosted vielbein gives the corrected metric (64 entries)",
      record=f"{SCOPE_PY}, check boosted_frame_reproduces_metric")
```

The rapidity is an unknown real function $b(x_4)$ of the time, with the derivative `bp` $= b'$. `L` is the boost with this rapidity, and `e_boosted` the new vielbein $e' = \Lambda e$ (the matrix product). The first check requires $e'^T\eta e' = g$ in all 64 entries.

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

The canonical spin connection of the boosted frame, computed by the general function (with the same Christoffel symbols `Gam`, because the metric is the same). Then the vielbein postulate in all 512 components and the antisymmetry, as in Notebook 06a, In [11], but with the boosted vielbein; one check for both. This is a slow step of the notebook: many entries contain $\cosh b$ and $\sinh b$, and sympy must simplify them.

```python
Omega_b = spinor_connection(omega_b, S)  # Omega'_mu
gup_b = curved_gammas(e_boosted, gamma)  # gamma'^mu
count_b = sum(1 for mu in range(8) for a in range(8) for c in range(a + 1, 8)
              if omega_b[mu][a][c] != 0)
say(f"nonzero components omega'_mu ab with a < b: {count_b}")
```

The boosted spinor connection $\Omega'_\mu$, the boosted curved gammas $\gamma'^\mu$, and the number of nonzero components $\omega'_{\mu ab}$ with $a < b$, printed: 14 (COMPUTED exactly; the diagonal vielbein has 10). The cell prints two PASS lines and this number.

**In [8], the contraction in the boosted frame** (Section 6.16).

```python
slash_b = sum((gup_b[mu] * Omega_b[mu] for mu in range(8)), Z16)
v = sp.cosh(b) * gamma[0] - sp.sinh(b) * gamma[4]  # R gamma^(x0) R^-1 (Section 11)
w = sp.cosh(b) * gamma[4] - sp.sinh(b) * gamma[0]  # R gamma^(x4) R^-1
formula = (c_g - bp / 2) * v + v_g * w
```

`slash_b` is the contraction $\sum_\mu\gamma'^\mu\Omega'_\mu$ of the boosted frame. `v` and `w` are the two matrices of Section 6.16, $v = \cosh b\,\gamma^{(x0)} - \sinh b\,\gamma^{(x4)}$ and $w = \cosh b\,\gamma^{(x4)} - \sinh b\,\gamma^{(x0)}$, and `formula` is the result derived there, $(c_g - \frac{b'}{2})v + v_gw$.

```python
beta, b0 = sp.symbols("beta b0", real=True)  # a constant rate and a start value
constant_rate = {bp: beta}  # b' = beta for b = beta x4 + b0
record_form = ((c_g - beta / 2) * v + v_g * w).subs(b, beta * x4 + b0)
check(matrix_is_zero(slash_b - formula)
      and matrix_is_zero(slash_b.subs(constant_rate).subs(b, beta * x4 + b0)
                         - record_form),
      "gamma'^mu Omega'_mu = (c_g - b'/2) v + v_g w for every rapidity b(x4)",
      record=f"{SCOPE_PY}, check boosted_frame_gammaOmega_formula")
```

The first check requires the computed contraction to equal the formula for the arbitrary function $b(x_4)$, and also, for the record's case of a constant rate, that replacing $b'$ by a constant $\beta$ and $b$ by $\beta x_4 + b_0$ gives the record's form $(c_g - \frac\beta2)v + v_gw$ (`constant_rate` replaces the derivative first).

```python
c0 = sp.simplify((slash_b * gamma[0]).trace() / 16)  # coefficient of gamma^(x0)
c4 = sp.simplify(-(slash_b * gamma[4]).trace() / 16)  # coefficient of gamma^(x4)
check(is_zero(sp.cosh(b) * c4 + sp.sinh(b) * c0 - v_g)
      and matrix_is_zero(formula.subs(bp, 0).subs(b, 0) - c_g * gamma[0]
                         - v_g * gamma[4]),
      "cosh b c4 + sinh b c0 = v_g for every rapidity; no boost gives c_g gamma^(x0) "
      "+ v_g gamma^(x4)",
      record=f"{SCOPE_WL}, check boosted_frame_removes_only_the_H_term")
```

`c0` and `c4` are the coefficients of $\gamma^{(x0)}$ and $\gamma^{(x4)}$ in the contraction, found with traces as in Notebook 06a. The second check proves the invariant of Section 6.16, $\cosh b\,c_4 + \sinh b\,c_0 = v_g$ for every rapidity function (so the contraction can vanish only where $v_g = 0$), and that with no boost at all ($b' = 0$, then $b = 0$) the formula gives back $c_g\gamma^{(x0)} + v_g\gamma^{(x4)}$. The record line names the WolframScript scope check, which states the invariant for any rapidity function. Two PASS lines.

**In [9], figure 2: the contraction in three frames.**

```python
times = np.linspace(-0.5, 0.5, 101)
t_symbol = sp.Symbol("t", real=True)
c_g_history = c_g.subs(history_values)  # (3/2) H e^(H x4/3)
v_g_history = v_g.subs(on_history).subs(history_values)  # (5/6) H
frames = [("no boost, $b = 0$", sp.Integer(0), "-"),
          ("constant rate, $b = 3x_4$", 3 * H * x4, "--"),
          ("$b = 9(e^{x_4/3} - 1)$, $b' = 2c_g$", 9 * (sp.exp(H * x4 / 3) - 1), "-.")]
```

101 times from $-\frac12$ to $\frac12$, a plain symbol `t_symbol` for numbers, and $c_g$ and $v_g$ on the history: $c_g = \frac32He^{Hx_4/3}$ and $v_g = \frac56H$ (the derivatives are replaced first). `frames` lists three rapidity functions with a label and a line style each: no boost, $b = 0$; the constant rate $b = 3Hx_4$; and $b = 9(e^{Hx_4/3} - 1)$, whose derivative is $b' = 3He^{Hx_4/3} = 2c_g$ on the history (Section 6.16).

```python
fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10.0, 4.2), sharey=True)
for label, rapidity_function, style in frames:
    rate = sp.diff(rapidity_function, x4)
    coefficient_x0 = ((c_g_history - rate / 2) * sp.cosh(rapidity_function)
                      - v_g_history * sp.sinh(rapidity_function))
    coefficient_x4 = (-(c_g_history - rate / 2) * sp.sinh(rapidity_function)
                      + v_g_history * sp.cosh(rapidity_function))
    c0_numbers = sp.lambdify(t_symbol, coefficient_x0.subs({H: 1, x4: t_symbol}))
    c4_numbers = sp.lambdify(t_symbol, coefficient_x4.subs({H: 1, x4: t_symbol}))
    ax_left.plot(times, np.broadcast_to(c0_numbers(times), times.shape), style,
                 label=label)
```

For each frame the rate $b'$ is computed with `sp.diff`, and the two coefficients of Section 6.16, $c_0 = (c_g - \frac{b'}2)\cosh b - v_g\sinh b$ and $c_4 = -(c_g - \frac{b'}2)\sinh b + v_g\cosh b$, are turned into numerical functions of the time with $H = 1$ and drawn in the left and the right panel (the two panels share one vertical axis, `sharey=True`).

```python
    ax_right.plot(times, np.broadcast_to(c4_numbers(times), times.shape), style,
                  label=label)
ax_left.set_title("coefficient $c_0$ of $\\gamma^{(x0)}$")
ax_right.set_title("coefficient $c_4$ of $\\gamma^{(x4)}$")
for ax in (ax_left, ax_right):
    ax.axhline(0.0, color="black", linewidth=0.6)
    ax.set_xlabel("time $x_4$ (units $1/H$), history $a_4 = x_4$")
    ax.legend(fontsize=8)
ax_left.set_ylabel("coefficient in $\\gamma'^\\mu\\Omega'_\\mu$ (units of $H$)")
```

Titles, a zero line, the axis labels and the legends.

```python
save_figure(fig, "boosted_contraction",
            "The contraction $\\gamma'^\\mu\\Omega'_\\mu = c_0\\gamma^{(x0)} + "
            ...
            "value.")
```

The figure is saved as `06b_2_boosted_contraction.png`.

**What Figure 06b.2 shows.** Without boost (solid) the coefficients are $c_0 = c_g = \frac32e^{x_4/3}$, slowly rising from $1.27$ to $1.77$ over the plotted times, and the constant $c_4 = v_g = \frac56$: the value of the diagonal vielbein on the history. The constant rate $b = 3x_4$ (dashed) makes $c_0$ vanish only at $x_4 = 0$, where $c_g = \frac32$; elsewhere it is not zero. The rapidity with $b' = 2c_g$ (dash-dotted) gives $c_0 = -\frac56\sinh b$ and $c_4 = \frac56\cosh b$ at every time: the term $c_g\gamma^{(x0)}$ is gone, and what remains is $v_g\,w$, never zero ($\cosh b \ge 1$). The same metric, a different frame, a different value of $\gamma^\mu\Omega_\mu$; no frame makes both coefficients vanish.

**In [10], removing the $c_g$ term.**

```python
B4_SAMPLE = sp.exp(sp.Rational(2, 3))  # b4 at a4 = 1/2 on the history, b4(0) = 1
B_SAMPLE = 9 * (sp.exp(sp.Rational(1, 6)) - 1)  # the rapidity 9 (e^(x4/3) - 1)


def at_sample(expr):
    """The decimal value of expr at H = 1, z = pi/4, x4 = 1/2 on the history of the
    record (a4 = 1/2, a4' = 1, a4'' = 0, b4 = e^(2/3), b4' = (4/3) b4, b4'' =
    (16/9) b4) with the rapidity b = 9 (e^(x4/3) - 1): b = 9 (e^(1/6) - 1),
    b' = 3 e^(1/6), b'' = e^(1/6) (derivatives first, then the functions)."""
    rate = sp.Rational(4, 3)  # b4'/b4
    expr = sp.sympify(expr).subs(sp.Derivative(b, (x4, 2)), sp.exp(sp.Rational(1, 6)))
    expr = expr.subs(bp, 3 * sp.exp(sp.Rational(1, 6))).subs(b, B_SAMPLE)
    expr = expr.subs(sp.Derivative(a4, (x4, 2)), 0)
    expr = expr.subs(sp.Derivative(b4, (x4, 2)), rate**2 * B4_SAMPLE)
    expr = expr.subs({a4p: 1, b4p: rate * B4_SAMPLE})
    expr = expr.subs({a4: sp.Rational(1, 2), b4: B4_SAMPLE})
    expr = expr.subs(W(x0), sp.Abs(sp.sin(z)) ** sp.Rational(1, 6))  # explicit W
    expr = expr.subs({H: 1, x4: sp.Rational(1, 2), x0: sp.pi / 24})
    return float(sp.N(expr))
```

The sample point of the figures: $H = 1$, $z = \pi/4$ and the time $x_4 = \frac12$ on the history ($a_4 = \frac12$, $a_4' = 1$, $a_4'' = 0$, $b_4 = e^{2/3}$, $b_4' = \frac43b_4$, $b_4'' = \frac{16}{9}b_4$), with the rapidity $b = 9(e^{x_4/3} - 1)$ of In [9], so that $b = 9(e^{1/6} - 1) = 1.632$, $b' = 3e^{1/6}$ and $b'' = e^{1/6}$. `at_sample` replaces the derivatives before the functions (for the reason given in Notebook 06a, In [10]), then writes out $W$, then sets the numbers, and returns a decimal number.

```python
def sample_table(matrix):
    return np.array([[at_sample(v) for v in row] for row in matrix.tolist()])
```

`sample_table` turns a matrix into an array of its decimal values at the sample point.

```python
removing = {bp: 2 * c_g}  # the rate b' = 2 c_g = 3 H e^(a4) b4^(-1/2)
slash_removed = slash_b.subs(removing)
Omega_removed = [M.subs(removing) for M in Omega_b]
nonzero = [NAMES[mu] for mu in range(8)
           if np.abs(sample_table(Omega_removed[mu])).max() > 1e-9]
say(f"Omega'_mu is nonzero for mu = {nonzero}")
check(matrix_is_zero(slash_removed - v_g * w) and nonzero == NAMES,
      "b' = 2 c_g: gamma'^mu Omega'_mu = v_g w, only the v_g term remains; "
      "Omega'_mu nonzero for all eight mu",
      record=f"{SCOPE_PY}, check boosted_frame_removes_only_the_H_term")
```

`removing` replaces $b'$ by $2c_g$, the rate of Section 6.16 (for every $a_4$ and $b_4$, not only on the history). With it, `slash_removed` is the contraction and `Omega_removed` the list of the eight $\Omega'_\mu$. The list `nonzero` collects the names of the directions whose $\Omega'_\mu$ has an entry larger than $10^{-9}$ at the sample point (a function that is not zero at one point is not the zero function), and is printed: all eight names. The check requires the contraction to be exactly $v_g\,w$ and $\Omega'_\mu$ to be nonzero for all eight $\mu$. One output line and one PASS line.

**In [11], figure 3: the boosted connection as heat maps.**

```python
panels = [("$\\Omega'_{x4}$", Omega_removed[4]), ("$\\Omega'_{x0}$", Omega_removed[0]),
          ("$\\gamma'^\\mu\\Omega'_\\mu$ (only the $v_g$ term)", slash_removed)]
tables = [sample_table(M) for _, M in panels]
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

Three heat maps side by side: $\Omega'_{x4}$, $\Omega'_{x0}$ and the contraction, each evaluated at the sample point and drawn with its own symmetric colour scale; `max(..., 1.0)` keeps the scale at least $\pm1$, so that a matrix with small entries is not drawn with an exaggerated scale.

```python
save_figure(fig, "boosted_connection_heat_maps",
            "The boosted vielbein with the rapidity rate $b' = 2c_g$ at the sample "
            ...
            "removed the term $c_g\\gamma^{(x0)}$.")
```

The figure is saved as `06b_3_boosted_connection_heat_maps.png`.

```python
check(np.abs(tables[2] - sample_table(v_g * w)).max() < 1e-12
      and np.abs(tables[2]).max() > 0.1 and np.abs(tables[0]).max() > 0.1,
      "at the sample point Omega'_x4 is nonzero and the contraction is the v_g term")
```

A check at the sample point: the contraction's table equals that of $v_g\,w$ to $10^{-12}$, and both the contraction and $\Omega'_{x4}$ have entries larger than $0.1$, so neither panel is blank. One PASS line.

**What Figure 06b.3 shows.** At the sample point of the history (rapidity $b = 1.632$). The left panel, $\Omega'_{x4}$, is coloured, although $\Omega_{x4} = 0$ in the diagonal vielbein: in the boosted frame the frame turns with the time, at the rate $b' = 2c_g$, and $\Omega'_{x4} = c_g\gamma^{(x4)}\gamma^{(x0)}$ with $c_g = 1.77$ (Section 6.16), a signed permutation matrix times $1.77$ whose squares lie in the two diagonal blocks. The middle panel, $\Omega'_{x0} = R\,\Omega_{x0}R^{-1}$, is pale: $\Omega_{x0} = \frac12h_4s_b\cot z\,\gamma^{(x0)}\gamma^{(x4)} = -\frac12h_4s_b\cot z\,X$ is a multiple of $X$, which commutes with $R$, so $\Omega'_{x0} = \Omega_{x0}$, with the entries $\pm0.14$ on a colour scale from $-1$ to $1$. The right panel is not white: the contraction is the term $\frac56(\cosh b\,\gamma^{(x4)} - \sinh b\,\gamma^{(x0)})$, with the entries $\pm\frac56\cosh 1.632 = \pm2.21$ of $\gamma^{(x4)}$ and $-\frac56\sinh 1.632 = -2.05$ of $\gamma^{(x0)}$ in the two off-diagonal blocks. The boost has removed the term $c_g\gamma^{(x0)}$, not the term $v_g$; the spinor connection itself is present in both frames.

**In [12], local spin covariance, checked** (Sections 6.15 and 6.16).

```python
X = gamma[4] * gamma[0]  # gamma^(x4) gamma^(x0)
check(X * X == I16, "X = gamma^(x4) gamma^(x0) squares to the identity")
R = sp.cosh(b / 2) * I16 - sp.sinh(b / 2) * X  # the spinor boost
R_inv = sp.cosh(b / 2) * I16 + sp.sinh(b / 2) * X
check(matrix_is_zero(R * R_inv - I16), "R R^-1 = 1")
```

$X = \gamma^{(x4)}\gamma^{(x0)}$ and the check $X^2 = 1$; the spinor boost $R = \cosh\frac b2 - \sinh\frac b2X$ and its inverse $\cosh\frac b2 + \sinh\frac b2X$, and the check $RR^{-1} = 1$.

```python
covers = all(matrix_is_zero(R_inv * gamma[a] * R
                            - sum((L[a, c] * gamma[c] for c in range(8)), Z16))
             for a in range(8))
check(covers, "R^-1 gamma^a R = Lambda^a_c gamma^c: R covers the boost")
```

The covering relation $R^{-1}\gamma^aR = \sum_c\Lambda^a{}_c\gamma^c$ for all eight $a$ (`L[a, c]` is $\Lambda^a{}_c$ for the rapidity function $b(x_4)$).

```python
gammas_turn = all(matrix_is_zero(gup_b[mu] - R * gup[mu] * R_inv) for mu in range(8))
connection_rule = all(matrix_is_zero(Omega_b[mu] - (R * Omega[mu] * R_inv
                                                   - R.diff(x[mu]) * R_inv))
                      for mu in range(8))
check(gammas_turn and connection_rule,
      "gamma'^mu = R gamma^mu R^-1 and Omega'_mu = R Omega_mu R^-1 - (d_mu R) R^-1")
```

The theorem of Section 6.15 for this boost: $\gamma'^\mu = R\gamma^\mu R^{-1}$ and $\Omega'_\mu = R\Omega_\mu R^{-1} - (\partial_\mu R)R^{-1}$ for all eight $\mu$ (`R.diff(x[mu])` differentiates every entry of $R$; only $\mu = x4$ gives a nonzero derivative).

```python
turned = R * slash * R_inv
extra = sum((gup_b[mu] * R.diff(x[mu]) * R_inv for mu in range(8)), Z16)
check(matrix_is_zero(R * gamma[0] * R_inv - v)
      and matrix_is_zero(R * gamma[4] * R_inv - w)
      and matrix_is_zero(turned - c_g * v - v_g * w)
      and matrix_is_zero(extra - bp / 2 * v),
      "R g0 R^-1 = v, R g4 R^-1 = w; turned term c_g v + v_g w; extra term "
      "(b'/2) v")
```

The pieces of the derivation of Section 6.16: $R\gamma^{(x0)}R^{-1} = v$ and $R\gamma^{(x4)}R^{-1} = w$; the turned contraction $R(c_g\gamma^{(x0)} + v_g\gamma^{(x4)})R^{-1} = c_gv + v_gw$; and the extra term $\sum_\mu\gamma'^\mu(\partial_\mu R)R^{-1} = \frac{b'}2v$. The cell prints five PASS lines (the notebook's own checks).

**In [13], the Riemann tensor** (Section 6.17).

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

All components with $\mu < \nu$ are computed (the others follow from the antisymmetry $R^\rho{}_{\sigma\nu\mu} = -R^\rho{}_{\sigma\mu\nu}$, which the two assignments use). `value != 0` first skips the components that are zero without any work. The RESULT line prints the number of nonzero components with $\mu < \nu$: 56 (`//` is division without remainder; the dictionary holds every component twice). These are the 28 planes with $R^a{}_{bab}$ and $R^b{}_{aab}$ each.

```python
raised = {key: value / g[key[1], key[1]] for key, value in riemann.items()}  # R^ab_cd
record = json.loads(repository_file(CURVATURE).read_text(encoding="utf-8"))


def from_record(text):
    """A component of the curvature record (Wolfram notation) as a sympy expression."""
    for long_form, short_form in (("Derivative[1][a4][x4]", "a4p"),
                                  ("Derivative[2][a4][x4]", "a4pp"),
                                  ("Derivative[1][b4][x4]", "b4p"),
                                  ("Derivative[2][b4][x4]", "b4pp"),
                                  ("a4[x4]", "a4"), ("b4[x4]", "b4")):
        text = text.replace(long_form, short_form)
    names = {"H": H, "a4": a4, "b4": b4, "a4p": a4p, "b4p": b4p,
             "a4pp": sp.Derivative(a4, (x4, 2)), "b4pp": sp.Derivative(b4, (x4, 2))}
    return parse_mathematica(text).subs({sp.Symbol(k): v for k, v in names.items()},
                                        simultaneous=True)
```

`raised` holds the components with the second index raised, $R^{ab}{}_{cd} = R^a{}_{bcd}/g_{bb}$ (the metric is diagonal; `key[1]` is the second index). `record` is the curvature record `curvature.json`, and `from_record` reads one of its components, written in Wolfram notation, with the same renaming of $a_4'$, $a_4''$, $b_4'$, $b_4''$ and of the functions as in Notebook 06a.

```python
record_riemann = {(NAMES.index(item["up"][0]), NAMES.index(item["up"][1]),
                   NAMES.index(item["down"][0]), NAMES.index(item["down"][1])):
                  from_record(item["value"]) for item in record["riemannMixedNonzero"]}
planes_only = all({c, d} == {a, bb} for (a, bb, c, d) in raised)
check(planes_only and len(raised) == 112 and set(raised) == set(record_riemann)
      and all(is_zero(raised[k] - record_riemann[k]) for k in raised)
      and all(is_zero(sp.diff(value, x0)) for value in record_riemann.values())
      and record_passed(CURVATURE_PY, "mixed_riemann_only_sectional")
```

The record lists its nonzero components as items with the two upper indices `up`, the two lower indices `down` (direction names) and the value; `NAMES.index` turns the names into positions. `planes_only` is true when every computed component $R^{ab}{}_{cd}$ has $\{c, d\} = \{a, b\}$ (two sets are equal when they hold the same elements in any order). The check requires this, exactly 112 such components, the same keys and the same values as the record, no dependence on $x_0$ (`sp.diff(value, x0)` must be zero for every record value), and the two checks of the independent report of the record as passed.

```python
      and record_passed(CURVATURE_PY, "rust_riemann_agrees"),
      "only the 28 plane curvatures K(a, b) are nonzero (112 entries R^ab_cd), free "
      "of x0, equal to the record",
      record=f"{CURVATURE}, riemannMixedNonzero; {CURVATURE_PY}, check "
             "mixed_riemann_only_sectional")
K = {(a, bb): record_riemann[(a, bb, a, bb)] for a in range(8) for bb in range(a + 1, 8)}
for a, bb in [(0, 1), (0, 4), (0, 5), (1, 2), (1, 4), (1, 5), (4, 5), (5, 6)]:
    say(f"K({NAMES[a]}, {NAMES[bb]}) = {K[(a, bb)]}")
```

`K` is the dictionary of the 28 plane curvatures $K(a, b) = R^{ab}{}_{ab}$ with $a < b$, taken from the record (which the check has just shown to equal the computation). Eight are printed, one of each kind and the two pairs that coincide: `K(x0, x1)` and `K(x1, x5)` are both $a_4'(\frac{b_4'}{2b_4} - a_4') = a_4'h_4$; `K(x0, x4)` and `K(x4, x5)` are both $a_4'^2 - a_4'' - a_4'b_4'/b_4 + b_4''/(2b_4) - b_4'^2/(4b_4^2)$, which is $h_4^2 + h_4'$ multiplied out; `K(x0, x5)` and `K(x5, x6)` are both $-H^2e^{2a_4}/b_4 + h_4^2$; `K(x1, x2)` is $a_4'^2$ and `K(x1, x4)` is $a_4'^2 + a_4''$. This is the table of Section 6.17. The cell prints the number, one PASS line with its record and the eight curvatures.

**In [14], the Ricci and Einstein tensors and the flat member** (Section 6.17).

```python
ricci_lower = sp.Matrix(8, 8, lambda sg, nu: sum(
    riemann.get((r, sg, r, nu), 0) for r in range(8)))  # R_sigma nu
ricci_mixed = g.inv() * ricci_lower  # R^mu_nu = g^mu sigma R_sigma nu
ricci_scalar = sum(ricci_mixed[a, a] for a in range(8))
```

The Ricci tensor $R_{\sigma\nu} = \sum_r R^r{}_{\sigma r\nu}$ as an $8 \times 8$ matrix (`sp.Matrix(8, 8, function)` fills each entry with the value of the function of its row and its column; `riemann.get(key, 0)` gives 0 for a missing key), the mixed Ricci tensor $R^\mu{}_\nu = \sum_\sigma g^{\mu\sigma}R_{\sigma\nu}$ as the matrix product with the inverse metric, and the Ricci scalar, the sum of its diagonal.

```python
names = {"H": H, "x0": x0, "x4": x4, "a4": a4, "b4": b4, "a4p": a4p, "b4p": b4p,
         "a4pp": sp.Derivative(a4, (x4, 2)), "b4pp": sp.Derivative(b4, (x4, 2))}
FORMULAS = {item["key"]: item["wl"] for item in json.loads(
    repository_file(THEORY_FILE).read_text(encoding="utf-8"))["formulas"]}
# the record's list {mu, nu, value}: R^mu_nu, directions numbered from 1 (x0 is 1)
ricci_record = {(int(m) - 1, int(n) - 1): value
                for m, n, value in from_record(FORMULAS["ricci_mixed_nonzero"])}
```

The record's names for the reader, the formulas of `field-theory.json`, and the record's list `ricci_mixed_nonzero` of the nonzero mixed Ricci components as a dictionary with Python's positions.

```python
off_diagonal = all(is_zero(ricci_mixed[m, n]) for m in range(8) for n in range(8)
                   if m != n)
einstein = ricci_mixed - sp.eye(8) * ricci_scalar / 2  # G^mu_nu
einstein_record = {(NAMES.index(k.split(",")[0]), NAMES.index(k.split(",")[1])):
                   from_record(item["mathematica"])
                   for k, item in record["einsteinMixed"].items()}
check(off_diagonal and set(ricci_record) == {(a, a) for a in range(8)}
      and all(is_zero(ricci_mixed[k] - ricci_record[k]) for k in ricci_record)
      and is_zero(ricci_scalar - from_record(FORMULAS["ricci_scalar"]))
      and len(einstein_record) == 64
      and all(is_zero(einstein[k] - einstein_record[k]) for k in einstein_record)
      and record_passed(REPORT_WL, "ricci_mixed_components")
      and record_passed(CURVATURE_PY, "rust_ricci_einstein_scalar_agree"),
      "the mixed Ricci and Einstein tensors are diagonal (56 components off the "
      "diagonal vanish) and equal the records",
      record=f"{THEORY_FILE}, formulas ricci_mixed_nonzero and ricci_scalar; "
             f"{CURVATURE}, einsteinMixed")
```

`off_diagonal` is true when all 56 components off the diagonal vanish exactly. `einstein` is $G^\mu{}_\nu = R^\mu{}_\nu - \frac12\delta^\mu_\nu R$ (`sp.eye(8)` is $\delta^\mu_\nu$), and `einstein_record` the record's 64 components of the Einstein tensor (`curvature.json` stores them under keys such as `"x0,x0"`, which `split(",")` divides into the two names). The check requires: no component off the diagonal; the record's list to contain exactly the eight diagonal components; all of them, the Ricci scalar and all 64 Einstein components to agree with the records; and the two record checks as passed.

```python
for a in (0, 1, 4):
    say(f"R^{NAMES[a]}_{NAMES[a]} = {ricci_record[(a, a)]}")
```

Three of the diagonal components are printed: $R^{x0}{}_{x0}$ (the same as for the extra times), $R^{x1}{}_{x1} = -a_4'^2 + a_4'' + 2a_4'b_4'/b_4$ and $R^{x4}{}_{x4} = 7a_4'^2 - a_4'' - 4a_4'b_4'/b_4 + 2b_4''/b_4 - (b_4'/b_4)^2$, the general formulas behind the history values of Section 6.17.

```python
def on_member(expr, a4_value, b4_value):
    """expr for the given functions a4 and b4 (derivatives carried out)."""
    return sp.simplify(sp.sympify(expr).subs({a4: a4_value, b4: b4_value}).doit())
```

`on_member(expr, a4_value, b4_value)` inserts given functions for $a_4$ and $b_4$; `.doit()` then carries out the derivatives, which `subs` leaves written as derivatives of the inserted functions.

```python
flat = [on_member(K[key], 0, H**2 * x4**2) for key in K]  # the flat member
on_hist = {key: on_member(K[key], A_EXACT * H * x4,
                          B4_ZERO * sp.exp(BETA_B4 * A_EXACT * H * x4)) for key in K}
R_history = on_member(from_record(FORMULAS["ricci_scalar"]), A_EXACT * H * x4,
                      B4_ZERO * sp.exp(BETA_B4 * A_EXACT * H * x4))
say(f"on the history: R = {sp.factor(R_history)}")
```

`flat` holds the 28 plane curvatures of the member $a_4 = 0$, $b_4 = H^2x_4^2$; `on_hist` the 28 plane curvatures on the history of the record; and `R_history` the Ricci scalar on the history, printed in factored form (`sp.factor`): `-4*H**2*(27*exp(2*H*x4/3) - 14)/9`, which is $H^2(\frac{56}{9} - 12e^{2Hx_4/3})$ multiplied out.

```python
check(all(value == 0 for value in flat) and is_zero(on_hist[(1, 2)] - H**2)
      and is_zero(R_history - H**2 * (sp.Rational(56, 9) - 12 * sp.exp(2 * H * x4 / 3)))
      and record_passed(REPORT_WL, "flat_member_and_curvature")
      and record_passed(REPORT_PY, "curvature_and_flat_member"),
      "flat for a4 = 0, b4 = H^2 x4^2 (all 28 plane curvatures vanish); curved on the "
      "history, R = H^2 (56/9 - 12 e^(2 H x4/3))",
      record=f"{REPORT_WL}, check flat_member_and_curvature")
```

The check requires all 28 curvatures of the flat member to be exactly zero, $K(x1, x2) = H^2$ on the history, the Ricci scalar on the history as stated, and the two record checks as passed.

```python
check(any(entry.has(a4) for entry in slash)
      and record_passed(SCOPE_PY, "gammaOmega_sees_the_hidden_block")
      and record_passed(SCOPE_WL, "gammaOmega_sees_the_hidden_block"),
      "gamma^mu Omega_mu contains a4: it sees the deflation of the hidden block",
      record=f"{SCOPE_PY}, check gammaOmega_sees_the_hidden_block")
```

The last check: some entry of the contraction `slash` of In [4] contains the function $a_4$ (`.has(a4)`), the record's scope check `gammaOmega_sees_the_hidden_block` in both scope reports. The cell prints three PASS lines with their records, three Ricci components and the Ricci scalar on the history.

**In [15], figure 4: the Ricci tensor on the history.**

```python
t_values = np.linspace(-2.0, 2.0, 161)
history_numbers = {H: 1, x4: t_symbol}
ricci_history = [sp.lambdify(t_symbol, on_member(ricci_record[(a, a)], x4,
                                                 sp.exp(sp.Rational(4, 3) * x4))
                             .subs(history_numbers)) for a in range(8)]
R_numbers = sp.lambdify(t_symbol, R_history.subs(history_numbers))
```

161 times from $-2$ to $2$. `ricci_history` is a list of eight numerical functions of the time: each diagonal Ricci component of the record on the history with $H = 1$ ($a_4 = x_4$, $b_4 = e^{4x_4/3}$); `R_numbers` is the Ricci scalar.

```python
fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
values = [float(np.broadcast_to(ricci_history[a](0.5), ())) for a in range(8)]
colors = ["tab:blue"] + ["tab:red"] * 3 + ["gray"] + ["tab:blue"] * 3
ax_left.bar(range(8), values, color=colors, width=0.6)
ax_left.axhline(0.0, color="black", linewidth=0.8)
ax_left.set_xticks(range(8), [f"$R^{{{n}}}{{}}_{{{n}}}$" for n in NAMES], fontsize=8)
ax_left.set_ylabel("value (units of $H^2$)")
ax_left.set_title("Ricci components on the history at $x_4 = 1/2$")
```

The left panel: the eight components at $x_4 = \frac12$ as bars, blue for the hidden block, red for 3-space, gray for the time (`float(np.broadcast_to(value, ()))` turns a result that may be a constant into one decimal number). The tick labels are $R^{x0}{}_{x0}$, ..., written in matplotlib's formula typesetting (the tripled braces print one brace around a value inserted by the f-string).

```python
for a, label, style in ((0, "$R^{x0}{}_{x0} = R^{x5}{}_{x5}$", "-"),
                        (1, "$R^{x1}{}_{x1}$", "--"),
                        (4, "$R^{x4}{}_{x4}$", ":")):
    ax_right.plot(t_values, np.broadcast_to(ricci_history[a](t_values),
                                            t_values.shape), style, label=label)
ax_right.plot(t_values, R_numbers(t_values), "-.", color="gray",
              label="Ricci scalar $R$")
ax_right.axhline(0.0, color="black", linewidth=1.2, label="flat member: all zero")
ax_right.set_ylim(-20.0, 8.0)
ax_right.set_xlabel("time $x_4$ (units $1/H$), history $a_4 = x_4$, "
                    "$b_4 = e^{4x_4/3}$")
ax_right.set_ylabel("value (units of $H^2$)")
ax_right.set_title("Curved on the history")
ax_right.legend(fontsize=7, loc="lower left")
```

The right panel: three components and the Ricci scalar versus the time, and a black line at zero, the value of every curvature component on the flat member; the vertical axis is cut at $-20$ and $8$.

```python
save_figure(fig, "ricci_components",
            "The mixed Ricci tensor of the corrected metric, which is diagonal, on "
            ...
            "zero (black line). The metric is curved on the history.")
```

The figure is saved as `06b_4_ricci_components.png`.

**What Figure 06b.4 shows.** On the left, at $x_4 = \frac12$: the four blue bars of the hidden block at $-(\frac59 + 3e^{1/3}) = -4.74$, the three red 3-space bars at $\frac53 = 1.67$, and the gray time bar at $\frac{31}{9} = 3.44$. On the right, the 3-space and the time components are constant on the history, while the component of the hidden block falls like $-3e^{2x_4/3}$: the curvature of the block grows as it shrinks (its warp term is $-H^2/s_b^2$). The Ricci scalar $R = \frac{56}{9} - 12e^{2x_4/3}$ falls through zero at $x_4 = \frac32\ln\frac{14}{27} = -0.985$ and leaves the plotted range below $-20$ near $x_4 = 1.4$. Only the flat member lies on the black line: on the history the metric is curved.

**In [16], the spinor curvature** (Section 6.17).

```python
def spinor_curvature(Om, mu, nu):
    return (Om[nu].diff(x[mu]) - Om[mu].diff(x[nu])
            + Om[mu] * Om[nu] - Om[nu] * Om[mu])
```

`spinor_curvature(Om, mu, nu)` is $F_{\mu\nu} = \partial_\mu\Omega_\nu - \partial_\nu\Omega_\mu + [\Omega_\mu, \Omega_\nu]$ for any list of spinor connections `Om`.

```python
F = {}
theorem_ok, plane_ok = True, True
for mu in range(8):
    for nu in range(mu + 1, 8):
        F[(mu, nu)] = spinor_curvature(Omega, mu, nu)
        from_riemann = sum((ETA[a] * f[a] * riemann[(a, c, mu, nu)] / f[c] * S[a][c] / 2
                            for a in range(8) for c in range(8)
                            if (a, c, mu, nu) in riemann), Z16)
        theorem_ok = theorem_ok and matrix_is_zero(F[(mu, nu)] - from_riemann)
        plane = ETA[mu] * ETA[nu] * f[mu] * f[nu] * K[(mu, nu)] * S[mu][nu]
        plane_ok = plane_ok and matrix_is_zero(from_riemann - plane)
```

For each of the 28 coordinate planes $\mu < \nu$: `F[(mu, nu)]` is the spinor curvature of the diagonal vielbein; `from_riemann` is $\frac12\sum_{a,c}R_{ac\mu\nu}S^{ac}$ with the frame components $R_{ac\mu\nu} = \eta_{aa}f_aR^a{}_{c\mu\nu}/f_c$ of the diagonal vielbein; and `plane` is the single generator $\eta_{\mu\mu}\eta_{\nu\nu}f_\mu f_\nu K(\mu, \nu)S^{\mu\nu}$ derived in Section 6.17. `theorem_ok` and `plane_ok` collect the two comparisons.

```python
check(theorem_ok and record_passed(REPORT_WL, "spin_curvature_equals_Riemann")
      and record_passed(REPORT_PY, "spinor_curvature_equals_riemann"),
      "F_mu nu = (1/2) R_ab mu nu S^ab in all 28 coordinate planes",
      record=f"{REPORT_WL}, check spin_curvature_equals_Riemann")
check(plane_ok, "F_mu nu = eta_mumu eta_nunu f_mu f_nu K(mu, nu) S^mu nu: one "
      "generator per plane")
```

Two checks: the theorem $F_{\mu\nu} = \frac12R_{ab\mu\nu}S^{ab}$ in all 28 planes (with the two record checks), and the one-generator form (the notebook's own check).

```python
F05_boosted = spinor_curvature(Omega_removed, 0, 5)
R_removed, R_inv_removed = R.subs(removing), R_inv.subs(removing)
check(matrix_is_zero(F05_boosted - R_removed * F[(0, 5)] * R_inv_removed)
      and np.abs(sample_table(F05_boosted)).max() > 0.1,
      "boosted (b' = 2 c_g): F'_x0x5 = R F_x0x5 R^-1, nonzero",
      record=f"{SCOPE_PY}, check boosted_frame_curvature_nonzero")
```

In the boosted frame with $b' = 2c_g$, `F05_boosted` is $F'_{x0\,x5}$ computed from the boosted spinor connection of In [10]; the check requires it to equal $R\,F_{x0\,x5}R^{-1}$ (Section 6.17) and to have an entry larger than 0.1 at the sample point, so it is not zero: the boost that removed the $c_g$ term did not remove the curvature. The cell prints three PASS lines, two with their records.

**In [17], figure 5: the size of the spinor curvature.**

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
            ax.text(nu, mu, f"{norms[mu, nu]:.2f}", ha="center", va="center",
                    fontsize=7, color="white" if dark else "black")
ax.set_xticks(range(8), NAMES)
ax.set_yticks(range(8), NAMES)
ax.set_xlabel("coordinate $\\nu$")
ax.set_ylabel("coordinate $\\mu$")
ax.set_title("Size of the spinor curvature $\\|F_{\\mu\\nu}\\|$")
ax.grid(False)
fig.colorbar(image, ax=ax, shrink=0.8, label="$\\|F_{\\mu\\nu}\\|$ (units of $H^2$)")
```

The array is drawn as a heat map in shades of purple, every nonzero size is printed in its square with two decimals (white digits on the dark squares), and the rows and columns are labelled with the coordinate names.

```python
save_figure(fig, "spinor_curvature_norms",
            "The size $\\|F_{\\mu\\nu}\\|$, the square root of the sum of the squares "
            ...
            "change of frame removes.")
```

The figure is saved as `06b_5_spinor_curvature_norms.png`.

```python
report("largest |F_mu nu| at the sample point (units of H^2)", f"{norms.max():.3f}")
report("smallest |F_mu nu| at the sample point (units of H^2)",
       f"{norms[norms > 0].min():.3f}")
curved = [pair for pair in F if norms[pair] > 1e-9]  # the curved planes
check(len(curved) == 28, "at the sample point all 28 coordinate planes are curved")
```

Two RESULT lines print the largest and the smallest nonzero size, $5.437$ and $0.178$ (in units of $H^2$; `norms[norms > 0]` keeps the positive entries), and the check requires all 28 planes to be curved at the sample point. The cell prints the two numbers and one PASS line.

**What Figure 06b.5 shows.** At the sample point of the history. Only the diagonal is white: all 28 planes are curved. The darkest squares, $5.44 = 2e\cdot1$, are the three planes inside 3-space ($2f_1^2K(x1, x2)$ with $f_1 = e^{1/2}$ and $K = a_4'^2 = 1$), followed by the planes of 3-space with the time, $3.30 = 2e^{1/2}$. The planes of the hidden direction with an extra time have $1.74$ and the planes of two extra times $1.64$ (both $\lvert K\rvert = e^{1/3} - \frac19 = 1.28$, times $2f_0f_5$ or $2f_5^2$); the planes of 3-space with the hidden direction have $0.93$ and with an extra time $0.88$ ($\lvert K\rvert = \frac13$); and the weakest are the planes of the time with an extra time, $0.18$, and with the hidden direction, $0.19$ ($K = \frac19$). Whatever the numbers in another frame, $F' = RFR^{-1}$ can never turn a coloured square white: this curvature is a property of the metric.

**In [18], the rescaling** (Section 6.18).

```python
w_r = sp.exp(a4 / 2) / b4 * W(x0) ** sp.Rational(-3, 2)  # the weight
bracket = sum((gup[mu] * sp.diff(w_r, x[mu]) for mu in range(8)), Z16) + w_r * slash
chi = sp.Matrix([sp.Function(f"chi{A}")(*x) for A in range(1, 17)])
psi = w_r * chi
dirac_psi = sum((gup[mu] * (psi.diff(x[mu]) + Omega[mu] * psi) for mu in range(8)),
                sp.zeros(16, 1))
dirac_chi = sum((gup[mu] * chi.diff(x[mu]) for mu in range(8)), sp.zeros(16, 1))
check(matrix_is_zero(bracket) and all(is_zero(v) for v in dirac_psi - w_r * dirac_chi),
      "gamma^mu D_mu (w chi) = w gamma^mu d_mu chi for w = e^(a4/2) b4^(-1) "
      "(sin^2 z)^(-1/8)",
      record=f"{SCOPE_PY}, check rescaling_removes_the_connection_term")
```

`w_r` is the weight $e^{a_4/2}b_4^{-1}W^{-3/2}$ (`W(x0) ** sp.Rational(-3, 2)` is $W^{-3/2} = (\sin^2 z)^{-1/8}$). `bracket` is the matrix $\sum_\mu\gamma^\mu\partial_\mu w_r + w_r\sum_\mu\gamma^\mu\Omega_\mu$ of Section 6.18, which must vanish. To check the statement on fields as well, `chi` is a column of sixteen unknown functions of the eight coordinates, `psi` $= w_r\chi$, `dirac_psi` the Dirac operator $\sum_\mu\gamma^\mu D_\mu\Psi$ and `dirac_chi` the plain $\sum_\mu\gamma^\mu\partial_\mu\chi$. The check requires the bracket to be zero and $\sum_\mu\gamma^\mu D_\mu\Psi = w_r\sum_\mu\gamma^\mu\partial_\mu\chi$ in all sixteen components.

```python
chi_conj = sp.Matrix([sp.conjugate(v) for v in chi])  # complex conjugates
S_psi = (w_r * chi_conj).T * C * (w_r * chi)  # Psi^dagger C Psi (w is real)
S_chi = chi_conj.T * C * chi
check(is_zero(S_psi[0, 0] - sp.exp(a4) / b4**2 * W(x0) ** (-3) * S_chi[0, 0]),
      "S[w chi] = e^(a4) b4^(-2) |sin z|^(-1/2) S[chi]",
      record=f"{SCOPE_PY}, check rescaled_equation_quadratic_potential")
```

The bilinear: `chi_conj` holds the complex conjugates of the sixteen functions (`sp.conjugate`), so `(w_r * chi_conj).T * C * (w_r * chi)` is $\Psi^\dagger C\Psi$ for $\Psi = w_r\chi$ (the weight is real, so its conjugate is itself), a $1 \times 1$ matrix whose entry `[0, 0]` is the number. The check requires $S[w_r\chi] = e^{a_4}b_4^{-2}W^{-3}S[\chi]$, which is $e^{a_4}b_4^{-2}\lvert\sin z\rvert^{-1/2}S[\chi]$. Two PASS lines with their records.

**In [19], figure 6: the rescaling as a picture.**

```python
z_values = np.linspace(0.05, np.pi - 0.05, 300)  # one cell, without the ends
u_symbol = sp.Symbol("u", real=True)  # x0 as a plain symbol for numbers
at_start = {a4: 0, b4: 1}  # a4 = 0, b4 = 1: the time x4 = 0 of the history


def numbers(expr):
    """A numerical function of x0 (as u) with H = 1 at a4 = 0, b4 = 1."""
    expr = sp.simplify(expr.subs(at_start).subs(W(x0), sp.Abs(sp.sin(z)) ** sp.Rational(
        1, 6)))
    return sp.lambdify(u_symbol, expr.subs({H: 1}).subs(x0, u_symbol))
```

300 hidden angles over one cell without its ends; a plain symbol `u` for $x_0$; and the time $x_4 = 0$ of the history, where $a_4 = 0$ and $b_4 = 1$. `numbers(expr)` turns an expression into a numerical function of $x_0$ there, with $H = 1$ and the explicit warp factor.

```python
weight = numbers(w_r)
term_derivative = numbers(sp.diff(w_r, x0) / f[0])
term_connection = numbers(c_g * w_r)
u_values = z_values / 6.0  # x0 = z / (6 H) with H = 1
first, second = term_derivative(u_values), term_connection(u_values)
```

Three functions: the weight; the derivative term of the coefficient of $\gamma^{(x0)}\chi$, $\partial_0w_r/f_0$ (the factor $1/f_0$ of $\gamma^{x0}$ times the derivative of the weight); and the connection term $c_gw_r$. They are evaluated at $x_0 = z/6$.

```python
fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
ax_left.plot(z_values, weight(u_values), label="$W^{-3/2} = (\\sin^2 z)^{-1/8}$")
ax_left.axvline(np.pi / 2, color="gray", linewidth=0.8)  # the fold
ax_left.set_xlabel("hidden angle $z = 6Hx_0$ (radians), fold at $\\pi/2$")
ax_left.set_ylabel("weight (pure number)")
ax_left.set_title("The rescaling weight")
ax_left.legend(fontsize=8)
ax_right.plot(z_values, first, label="$\\partial_{x0} w_r/f_0$")
ax_right.plot(z_values, second, "--",
              label="$c_g w_r$ (from $\\gamma^\\mu\\Omega_\\mu$)")
ax_right.plot(z_values, first + second, ":", color="black", label="sum")
ax_right.axvline(np.pi / 2, color="gray", linewidth=0.8)
ax_right.set_xlabel("hidden angle $z = 6Hx_0$ (radians), fold at $\\pi/2$")
ax_right.set_ylabel("coefficient of $\\gamma^{(x0)}\\chi$ (units of $H$)")
ax_right.set_title("The two terms cancel")
ax_right.legend(fontsize=8)
```

The left panel draws the weight with the fold marked; the right panel the two terms and their sum.

```python
save_figure(fig, "rescaling",
            "The rescaling $\\Psi = w_r\\chi$ with $w_r = e^{a_4/2}b_4^{-1}"
            ...
            "$e^{a_4/2}b_4^{-1}$, no term $v_g\\gamma^{(x4)}$).")
```

The figure is saved as `06b_6_rescaling.png`.

```python
check(np.max(np.abs(first + second)) < 1e-12, "the two terms cancel at all 300 points")
```

The check: the two terms cancel at all 300 points to better than $10^{-12}$. The cell prints the file name and one PASS line.

**What Figure 06b.6 shows.** At the time $x_4 = 0$ of the history. On the left, the weight $(\sin^2 z)^{-1/8} = \lvert\sin z\rvert^{-1/4}$ is large near the tips ($2.1$ at $z = 0.05$) and falls to 1 at the fold, symmetrically on the two halves of the cell. On the right, the derivative term $\partial_0w_r/f_0 = -c_gw_r$ (solid) is the mirror image of the connection term $c_gw_r$ (dashed) about the zero line, from $\mp3.2$ near the tips to $\mp1.5$ at the fold, and their sum (dotted) lies on zero everywhere: in the variable $\chi$ the field equation has no term $c_g\gamma^{(x0)}$ (and, by the factor $e^{a_4/2}b_4^{-1}$ of the weight, no term $v_g\gamma^{(x4)}$).

**In [20], the last checks.**

```python
scope_names = ["boosted_frame_reproduces_metric", "boosted_frame_canonical_connection",
               "boosted_frame_gammaOmega_formula",
               "boosted_frame_removes_only_the_H_term",
               "boosted_frame_curvature_nonzero",
               "rescaling_removes_the_connection_term",
               "rescaled_equation_quadratic_potential",
               "gammaOmega_sees_the_hidden_block"]
cited = {SCOPE_PY: scope_names, SCOPE_WL: scope_names,
         REPORT_PY: ["spinor_curvature_equals_riemann", "curvature_and_flat_member"],
         REPORT_WL: ["ricci_scalar", "ricci_mixed_components",
                     "flat_member_and_curvature", "spin_curvature_equals_Riemann"],
         CURVATURE_PY: ["mixed_riemann_only_sectional", "rust_riemann_agrees",
                        "rust_ricci_einstein_scalar_agree", "k1_offdiagonal_vanishes"]}
count = sum(len(v) for v in cited.values())
check(all(record_passed(path, name) for path, names in cited.items()
          for name in names), f"the {count} cited record checks are recorded as passed")
```

The cited record checks: the eight scope checks of this notebook in both scope reports, two checks of the sympy report and four of the WolframScript report, and four checks of the independent report of the curvature record (among them that the Lovelock tensor $E_{(1)}$, the Einstein tensor, has no component off the diagonal). The check requires all 26 to be recorded as passed.

```python
expected = [f"06b_{k}_{name}.png" for k, name in enumerate([
    "boost_hyperbolas", "boosted_contraction", "boosted_connection_heat_maps",
    "ricci_components", "spinor_curvature_norms", "rescaling"], 1)]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in expected),
      "all six figure files exist")
all_checks_passed()
```

The six figure files must exist, and the last line is printed: ALL 29 CHECKS PASSED (notebook 06b).

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

(the same steps without $\eta$, Section 6.7). The factor $\frac12(\eta_{aa} + \eta_{bb})$ is $+1$ for a pair of two space-like directions (**space-space**), $-1$ for a pair of two time-like directions (**time-time**) and $0$ for a boost pair. In the author's frame metric there are $\binom42 = 6$ space-space pairs among $x0, x1, x2, x3$, 6 time-time pairs among $x4, x5, x6, x7$, and $4 \cdot 4 = 16$ boost pairs. Writing $\Omega^{ss}_\mu$, $\Omega^{tt}_\mu$ and $\Omega^{st}_\mu$ for the parts of $\Omega_\mu$ that come from the three kinds of pairs:

$$
\Omega^{nb}_\mu = \Omega^{ss}_\mu - \Omega^{tt}_\mu, \qquad \Omega_\mu = \Omega^{ss}_\mu + \Omega^{tt}_\mu + \Omega^{st}_\mu .
$$

**The mixed contraction keeps the 6 space-space parts, reverses the sign of the 6 time-time parts and deletes all 16 boost parts.** In a space whose metric is positive (every $\eta_{aa} = +1$) the factor is always $+1$ and the two contractions agree: in the polar plane of Section 6.5 both give $\Omega_\varphi = -\frac i2\sigma_3$. The mistake cannot be seen in the usual textbook examples; in signature (4,4) it deletes 16 of the 28 parts.

**Where it is total: the Milne wedge.** Take the flat plane with one time $t$ and one space direction $y$, $ds^2 = -dt^2 + dy^2$, and in the part $t > \lvert y\rvert$ the coordinates $\tau = \sqrt{t^2 - y^2}$ and $\theta$ with $t = \tau\cosh\theta$, $y = \tau\sinh\theta$ (in this paragraph $t$ and $y$ are these two flat coordinates, not an extra time or the hidden coordinate of Chapter 3). Line by line, $dt = \cosh\theta\,d\tau + \tau\sinh\theta\,d\theta$ and $dy = \sinh\theta\,d\tau + \tau\cosh\theta\,d\theta$ (the product rule and $\frac{d}{d\theta}\cosh\theta = \sinh\theta$, $\frac{d}{d\theta}\sinh\theta = \cosh\theta$), so

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

The plane is flat, but the frame is boosted by the rapidity $\theta$ as one moves along $\theta$, and the correct spinor connection records this: $\Omega_\theta = -(\partial_\theta U)U^{-1}$ for the spinor boost $U(\theta) = \cosh\frac\theta2 + \sinh\frac\theta2\,\gamma^0\gamma^1 = \mathrm{diag}(e^{\theta/2}, e^{-\theta/2})$ (since $\partial_\theta U = \frac12\gamma^0\gamma^1U$). As in the polar plane of Section 6.5, the rule $\Omega' = R\,\Omega R^{-1} - (\partial_\theta R)R^{-1}$ of Section 6.15 with $R = U$ makes this $\Omega_\theta$ from the connection 0 of the frame of $t$ and $y$, so $U$ carries that frame into the Milne frame; the inverse boost $U^{-1} = \mathrm{diag}(e^{-\theta/2}, e^{\theta/2})$ removes the connection: $\gamma^0\gamma^1$ commutes with $U$, so $U^{-1}\Omega_\theta U = \Omega_\theta$, and $(\partial_\theta U^{-1})U = -\frac12\gamma^0\gamma^1$, hence $\Omega'_\theta = -\frac12\gamma^0\gamma^1 + \frac12\gamma^0\gamma^1 = 0$. The mixed contraction deletes the whole connection. It also violates the divergence form of Section 6.9: with $\sqrt{\lvert g\rvert} = \tau$, $\gamma^\tau = \gamma^0$ and $\gamma^\theta = \gamma^1/\tau$,

$$
\frac{1}{2\tau}\Big(\partial_\tau(\tau\gamma^0) + \partial_\theta\big(\tau\cdot\tfrac{\gamma^1}{\tau}\big)\Big) = \frac{\gamma^0}{2\tau}, \qquad \gamma^\theta\Omega_\theta = \frac{\gamma^1}{\tau}\Big(-\tfrac12\gamma^0\gamma^1\Big) = \frac{1}{2\tau}\gamma^0\gamma^1\gamma^1 = \frac{\gamma^0}{2\tau}
$$

(in the second: exchange $\gamma^1$ and $\gamma^0$ at the cost of a sign; $(\gamma^1)^2 = 1$). The correct value equals the divergence form; the mixed contraction gives 0.

**The corrected metric.** Of the 10 components of Section 6.6 none belongs to a space-space pair: the pairs of $x0$ with a 3-space direction would be space-space pairs, but 3-space has no warp, so these components are zero. The three components $(x4, x_t)$ are time-time pairs (sign reversed), and the seven others, $(x0, x4)$, the three $(x_i, x4)$ and the three $(x0, x_t)$, are boost pairs (deleted). So, with $f_t = s_bW$,

$$
\Omega^{nb}_{x0} = 0, \qquad \Omega^{nb}_{x_i} = 0, \qquad \Omega^{nb}_{x4} = 0, \qquad \Omega^{nb}_{x_t} = -h_4f_t\,S^{x4\,x_t},
$$

compared with $\Omega_{x0} = h_4f_0S^{x0x4}$, $\Omega_{x_i} = a_4'f_iS^{x_ix4}$ and $\Omega_{x_t} = h_4f_tS^{x4x_t} + HW\,S^{x0x_t}$ (Section 6.7). The contraction, by the steps of Section 6.8:

$$
\gamma^{x_t}\Omega^{nb}_{x_t} = \frac{\gamma^{(x_t)}}{f_t}\,(-h_4f_t)\,\tfrac12\gamma^{(x4)}\gamma^{(x_t)} = -\tfrac{h_4}2\,\gamma^{(x_t)}\gamma^{(x4)}\gamma^{(x_t)} = -\tfrac{h_4}2\,\gamma^{(x4)}
$$

($f_t$ cancels; $\gamma^{(x_t)}\gamma^{(x4)}\gamma^{(x_t)} = \gamma^{(x4)}$ as in Section 6.8). Summed over the three extra times:

$$
\sum_\mu\gamma^\mu\Omega^{nb}_\mu = -\tfrac32h_4\,\gamma^{(x4)} = \tfrac32\Big(a_4' - \frac{b_4'}{2b_4}\Big)\gamma^{(x4)} \quad\text{instead of}\quad \sum_\mu\gamma^\mu\Omega_\mu = c_g\,\gamma^{(x0)} + v_g\,\gamma^{(x4)} ;
$$

on the history of the record, where $a_4' = H$ and $\frac{b_4'}{2b_4} = \frac23H$, this is $\frac{H}{2}\gamma^{(x4)}$ instead of $\frac32He^{Hx_4/3}\gamma^{(x0)} + \frac56H\gamma^{(x4)}$. The whole hidden term $c_g\gamma^{(x0)}$ is lost, because it came from the deleted boost pairs $(x0, x_t)$, and the time term changes from $b_4'/b_4 - a_4'/2$ to $\frac32a_4' - \frac34b_4'/b_4$.

**The gammas are no longer covariantly constant.** Replace $\Omega_\mu$ by $\Omega^{nb}_\mu$ in $D_\mu\gamma^\nu$:

$$
D^{nb}_\mu\gamma^\nu = \partial_\mu\gamma^\nu + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}\gamma^\lambda + [\Omega^{nb}_\mu, \gamma^\nu] = D_\mu\gamma^\nu + [\Omega^{nb}_\mu - \Omega_\mu, \gamma^\nu] = [\Omega^{nb}_\mu - \Omega_\mu, \gamma^\nu]
$$

(add and subtract $[\Omega_\mu, \gamma^\nu]$; then $D_\mu\gamma^\nu = 0$, Section 6.7). By the vector rule $[S^{ab}, \gamma^c] = \eta^{bc}\gamma^a - \eta^{ac}\gamma^b$, the commutator with a generator $S^{ab}$ is nonzero only when $c$ is $a$ or $b$. Go through the directions. For $\mu = x0$ the difference is the deleted boost part, $-h_4f_0S^{x0x4}$, and

$$
\begin{aligned}
[-h_4f_0S^{x0x4}, \gamma^{x0}] &= -h_4\big(\eta^{x4x0}\gamma^{(x0)} - \eta^{x0x0}\gamma^{(x4)}\big) = h_4\,\gamma^{(x4)},\\
[-h_4f_0S^{x0x4}, \gamma^{x4}] &= -h_4f_0\big(\eta^{x4x4}\gamma^{(x0)} - \eta^{x0x4}\gamma^{(x4)}\big) = h_4f_0\,\gamma^{(x0)}
\end{aligned}
$$

($\gamma^{x0} = \gamma^{(x0)}/f_0$, so $f_0$ cancels in the first; $\eta^{x4x0} = 0$, $\eta^{x0x0} = 1$, $\eta^{x4x4} = -1$): two violated pairs. For $\mu = x_i$ the difference is $-a_4'f_iS^{x_ix4}$, and in the same way $[\ldots, \gamma^{x_i}] = a_4'\gamma^{(x4)}$ and $[\ldots, \gamma^{x4}] = a_4'f_i\gamma^{(x_i)}$: two violated pairs for each 3-space direction. For $\mu = x_t$ the difference is $-h_4f_tS^{x4x_t} - (h_4f_tS^{x4x_t} + HWS^{x0x_t}) = -2h_4f_tS^{x4x_t} - HWS^{x0x_t}$ (the time-time part counted twice, because its sign was reversed, and the deleted boost part), and the vector rule gives

$$
\begin{aligned}
[\ldots, \gamma^{x_t}] &= 2h_4\,\gamma^{(x4)} + \frac{H}{s_b}\,\gamma^{(x0)}, \qquad [\ldots, \gamma^{x4}] = -2h_4f_t\,\gamma^{(x_t)},\\
[\ldots, \gamma^{x0}] &= \frac{HW}{f_0}\,\gamma^{(x_t)} = \frac{HW\tan z}{s_b}\,\gamma^{(x_t)}
\end{aligned}
$$

(with $\eta^{x_tx_t} = -1$, $W/f_t = 1/s_b$ and $f_0 = s_b\cot z$): three violated pairs for each extra time, and $\mu = x4$ violates none ($\Omega^{nb}_{x4} = \Omega_{x4} = 0$). Altogether $2 + 3 \cdot 2 + 3 \cdot 3 = 17$ of the 64 pairs. Each violated matrix is a multiple of one gamma (16 nonzero entries), except $2h_4\gamma^{(x4)} + \frac{H}{s_b}\gamma^{(x0)}$, which has 32 because $\gamma^{(x4)}$ and $\gamma^{(x0)}$ have their nonzero entries in different places; so there are $14 \cdot 16 + 3 \cdot 32 = 320$ nonzero entries. The defining property $[\Omega^{nb}_\mu, \gamma^a] = -\sum_b\omega_\mu{}^a{}_b\gamma^b$ fails in the same 17 pairs $(\mu, a)$, because its failure is the commutator of the same differences with the frame gammas. Notebook 06c finds exactly these numbers (In [13]; COMPUTED exactly by the notebook, not a Revision record), and its figure 5 shows the 17 pairs.

| statement | status | where it is verified |
| --- | --- | --- |
| $\Omega^{nb}_\mu = \sum_{a<b}\frac12(\eta_{aa} + \eta_{bb})\omega_{\mu ab}S^{ab} = \Omega^{ss}_\mu - \Omega^{tt}_\mu$ | PROVED (above) | Notebook 06c, In [4] and In [8] (its own exact checks) |
| polar plane: the contractions agree; Milne wedge: $\Omega_\theta = -\frac12\gamma^0\gamma^1$, $\Omega^{nb} = 0$ | PROVED (above) | Notebook 06c, In [6] |
| the record does not use the mixed contraction | the record's statement | `Revision/SPEC.md`, section 3 (checked as text by Notebook 06c, In [2]) |
| corrected metric: none of the 10 components kept, 3 reversed, 7 deleted; $\gamma^\mu\Omega^{nb}_\mu = \frac32(a_4' - \frac{b_4'}{2b_4})\gamma^{(x4)}$; 17 violated pairs, 320 entries | PROVED above and COMPUTED exactly by Notebook 06c; not a Revision result (it describes the contraction the record does not use) | Notebook 06c, In [8], In [10] and In [13] |

### 6.24 Why only the value $\frac32H$ is right

Two facts single out the correct value $c_g\gamma^{(x0)} + v_g\gamma^{(x4)}$, whose hidden part is $\frac32H$ divided by the hidden scale, among all candidates.

**The divergence form.** Section 6.9 showed that the correct contraction equals $\frac{1}{2\sqrt{\lvert g\rvert}}\sum_\mu\partial_\mu(\sqrt{\lvert g\rvert}\gamma^\mu)$, a quantity built from the volume factor and the vielbein alone. The mixed contraction, $\frac32(a_4' - \frac{b_4'}{2b_4})\gamma^{(x4)}$, does not equal it.

**The hidden-direction operator.** For fields that depend on $x_0$ only, the part of the Dirac operator along the hidden direction is $\gamma^{(x0)}\big(\frac{1}{f_0}\partial_0 + \beta\big)$, where $\beta$ is the coefficient of $\gamma^{(x0)}$ in the contraction ($\beta = c_g$ for the correct one, $\beta = 0$ for the mixed one). Take out the factor $\frac{1}{f_0} = e^{a_4}b_4^{-1/2}\tan z$:

$$
\frac{1}{f_0}\partial_0 + \beta = \frac{1}{f_0}\big(\partial_0 + f_0\beta\big) = \frac{1}{f_0}\big(\partial_0 + c\cot z\big), \qquad c = s_b\,\beta
$$

($f_0 = s_b\cot z$), with $c = s_bc_g = \frac32H$ for the correct contraction and $c = 0$ for the mixed one. Write $A_cq = \partial_0q + c\cot z\,q$ for a function $q(x_0)$. An operator $A$ is called **antisymmetric for the weight $w(x_0)$** when $\int w\,p\,(Aq)\,dx_0 = -\int w\,(Ap)\,q\,dx_0$ for all functions $p$, $q$, up to **boundary terms** (values at the ends of the interval). This is the property that makes $iA$ a Hermitian operator in quantum theory (Chapter 10). The natural weight for the operator $\frac1{f_0}A_c$ is the volume factor $\sqrt{\lvert g\rvert}$; moving the factor $\frac1{f_0}$ into it gives the weight $\sqrt{\lvert g\rvert}/\lvert f_0\rvert = b_4^{3/2}W^3$ for $A_c$ (Section 6.2; the sign $G$ is constant on each half of a cell and does not matter), and along the hidden direction $b_4^{3/2}$ is a constant factor, which multiplies every line below and is left out, so the weight is $W^3 = (\sin^2 z)^{1/4}$. Compute, line by line, for two functions $p(x_0)$, $q(x_0)$ (primes are derivatives by $x_0$ here):

$$
\partial_0(W^3p\,q) = 3H\cot z\,W^3\;p\,q + W^3\,(p'q + p\,q')
$$

(the product rule; $\partial_0W^3 = 3W^2\,\partial_0W = 3H\cot z\,W^3$, Section 6.9),

$$
W^3\,\big(p\,A_cq + (A_cp)\,q\big) = W^3\,(p\,q' + p'q) + 2c\cot z\,W^3\;p\,q
$$

(insert $A_c$; the two terms $c\cot z\,pq$ add). Subtracting the first line from the second:

$$
W^3\,\big(p\,A_cq + (A_cp)\,q\big) - \partial_0(W^3p\,q) = (2c - 3H)\cot z\,W^3\;p\,q .
$$

For $c = \frac32H$ the right side vanishes: integrated over $x_0$, $\int W^3p\,A_{3H/2}q\,dx_0 = -\int W^3(A_{3H/2}p)\,q\,dx_0 + \big[W^3p\,q\big]$, so $A_{3H/2}$ is antisymmetric for the weight $W^3$ up to the boundary term. This is the record's formula `hidden_direction_hermiticity`. For the mixed value $c = 0$, which is the same as no spin-connection term at all, the term $-3H\cot z\,W^3p\,q$ remains, which is not a boundary term (it has no derivative in front), so no boundary condition can remove it. Only $c = \frac32H$, the value of the correct contraction, works.

**Scope of this argument.** The boundary term $[W^3p\,q]$ vanishes at the tips $\sin z = 0$, where $W = 0$, but not at the fold $\cos z = 0$, where $W = 1$; there a boundary condition is needed. Which condition is right is not decided in this chapter (it is the one point left OPEN here); Chapter 14 treats the conditions at the fold, which are ASSUMED there, and the record says the same (`wolfram-field-theory.json`, check `good_sector_hermiticity_curved`: Hermiticity needs a boundary condition at the degenerate points $z = \pi/2 + n\pi$). And the role of $\frac32H$ depends on the variables. For the rescaled field of Section 6.18, $q = W^{-3/2}\tilde q$, line by line,

$$
A_{3H/2}\big(W^{-3/2}\tilde q\big) = W^{-3/2}\Big(\tilde q' - \tfrac32H\cot z\,\tilde q\Big) + \tfrac32H\cot z\,W^{-3/2}\tilde q = W^{-3/2}\,\tilde q'
$$

(the product rule with $\partial_0W^{-3/2} = -\frac32H\cot z\,W^{-3/2}$; the two terms with $H$ cancel), and the weight becomes $W^3\cdot W^{-3/2}\cdot W^{-3/2} = 1$: in these variables the operator is the plain derivative with the constant weight, antisymmetric without any $H$ term. The record says so in the same formula ("for this measure and these variables"). PROVED; `field-theory.json`, formula `hidden_direction_hermiticity` (written without the factor $b_4^{3/2}$, which is constant along $x_0$); `wolfram-field-theory.json`, check `good_sector_hermiticity_curved`; Notebook 06c, In [15].

### 6.25 Example: Notebook 06c

Notebook 06c checks Sections 6.23 and 6.24 with exact algebra, for arbitrary functions $a_4(x_4)$ and $b_4(x_4)$ and every real $z$. It reads the author's gammas and the formulas of the record `field-theory.json` (for the corrected metric), and checks that `Revision/SPEC.md` contains the record's statement about the mixed contraction. It defines the general formulas again, now with the MIXED spin connection, a separate lowering function and a contraction over all ordered pairs. It sorts the 28 frame pairs into their three kinds and checks the key step of the derivation for all of them; works the polar plane and the Milne wedge; computes, for the corrected metric, the correct and the mixed spinor connections and their contractions direction by direction, also on the history of the record; counts where the covariant constancy of the gammas breaks; and checks the divergence form and the antisymmetry of the hidden-direction operator for two arbitrary functions. Every correct result is compared with the Revision records; the results about the mixed contraction are the notebook's own and are labelled so. It draws six figures, needs no Rust, runs in less than a minute and ends with the line ALL 28 CHECKS PASSED (notebook 06c).

<!-- NOTEBOOK 06c -->

### 6.28 Line-by-line walk-through of Notebook 06c

The notebook has 17 code cells, In [1] to In [17]; this section explains every line of every one of them. A line `...` in a quoted figure cell stands for the remaining lines of a long caption, printed in full in Section 6.27, where the output of In [k] is printed under the label Out [k].

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
NAMES = fixture["coordinates"]  # ["x0", ..., "x7"]
ETA = fixture["eta"]  # +1 space-like, -1 time-like
gamma = [sp.Matrix(rows) for rows in fixture["gamma"]]  # gamma[a] = gamma^(xa)
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
THEORY_FILE = "Revision/theory/field-theory.json"  # the record, corrected metric
FORMULAS = {item["key"]: item["wl"] for item in json.loads(
    repository_file(THEORY_FILE).read_text(encoding="utf-8"))["formulas"]}
REPORT_PY = "Revision/theory/reports/python-field-theory.json"
REPORT_WL = "Revision/theory/reports/wolfram-field-theory.json"
PARAMETERS = "Revision/kohn_sham/results/parameters.json"
physics = json.loads(repository_file(PARAMETERS).read_text(encoding="utf-8"))["physics"]
A_EXACT = sp.nsimplify(physics["historyA"])  # the slope A of the history, 1
BETA_B4 = sp.nsimplify(physics["historyBeta"])  # the exponent of b4, 4/3
B4_ZERO = sp.nsimplify(physics["historyB4AtZero"])  # b4(0) = 1
```

The formulas of the record `field-theory.json` (for the corrected metric) as a dictionary from key to Wolfram text, the names of the two field-theory reports, and the history of the record from `parameters.json` ($A = 1$, $\beta = \frac43$, $b_4(0) = 1$ as exact fractions), as in Notebook 06a.

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

The figure is saved as `06c_1_pair_kinds.png`.

**What Figure 06c.1 shows.** Green squares ($+1$, kept) fill the pairs among $x0, x1, x2, x3$, orange squares ($-1$, sign reversed) the pairs among $x4, x5, x6, x7$, and gray squares (0, deleted) form two $4 \times 4$ rectangles: every space-like direction paired with every time-like direction. Counting the upper half: 6 green, 6 orange, 16 gray. The mixed contraction deletes more than half of the spin connection; for the corrected metric, whose 10 components lie in gray squares (7) and orange squares (3) only, it keeps nothing at all (In [8]).

**In [6], the polar plane and the Milne wedge** (Section 6.23).

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
removed = U.inv() * milne_Omega[1] * U - U.inv().diff(theta) * U  # frame change U^-1
check(matrix_is_zero(-U.diff(theta) * U.inv() - milne_Omega[1])
      and matrix_is_zero(removed),
      "Milne: Omega_theta = -(dU/dtheta) U^-1 for the spinor boost U; U^-1 removes it")
```

The spinor boost $U(\theta) = \cosh\frac\theta2 + \sinh\frac\theta2\,\gamma^0\gamma^1$. `removed` is the rule $R\,\Omega_\theta R^{-1} - (\partial_\theta R)R^{-1}$ of a change of frame (Section 6.15) with $R = U^{-1}$, whose inverse is $U$. The check requires $\Omega_\theta = -(\partial_\theta U)U^{-1}$ (the same rule with $R = U$ applied to the connection 0 of the frame of $t$ and $y$: $U$ carries that frame into the Milne frame) and `removed` to be zero (the inverse boost $U^{-1}$ removes the connection), as worked by hand in Section 6.23.

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
            "$\\theta$: real and unbounded, unlike a spinor rotation.")
```

The figure is saved as `06c_2_milne_frame_and_spin_boost.png`.

**What Figure 06c.2 shows.** On the left, the frame at $\theta = 0$ is upright (time up, space to the right); moving along $\theta$ the blue and orange arrows tilt symmetrically towards the dashed light lines, as in figure 1 of Notebook 06b: the frame is boosted along $\theta$, and the correct spin connection $\omega_{\theta01} = -1$ records this rate, although the plane is flat. On the right, the entries $e^{\pm\theta/2}$ of the spinor boost $U(\theta)$, which carries the frame of $t$ and $y$ into the Milne frame (its inverse removes the connection), grow or fall without bound and never return, unlike the spinor rotation of figure 1 of Notebook 06a, which came back after $4\pi$. The mixed contraction would delete this whole connection.

**In [8], the corrected metric: the correct and the notebook's spinor connection** (Section 6.23).

```python
from sympy.parsing.mathematica import parse_mathematica  # reads Wolfram notation
```

The reader of Wolfram notation.

```python
x = sp.symbols("x0:8", real=True)  # x[0] = x0, ..., x[4] = x4, ..., x[7] = x7
x0, x4 = x[0], x[4]  # the hidden direction and the time
H = sp.Symbol("H", positive=True)  # the author's constant H > 0
a4 = sp.Function("a4")(x4)  # any function of the time
b4 = sp.Function("b4", positive=True)(x4)  # any positive function of the time
a4p, b4p = sp.Derivative(a4, x4), sp.Derivative(b4, x4)  # a4' and b4'
h4 = b4p / (2 * b4) - a4p  # the rate of the hidden scale
z = 6 * H * x0  # the hidden coordinate


class W(sp.Function):
    """The warp factor W(x0) = (sin(6 H x0)^2)^(1/12) > 0 of the extra times."""

    def fdiff(self, argindex=1):
        """dW/dx0 = H cot(6 H x0) W, for every real z = 6 H x0 with sin z != 0."""
        return H * sp.cot(6 * H * self.args[0]) * self

    def _eval_is_positive(self):
        return True  # the positive root


s_b = sp.exp(-a4) * sp.sqrt(b4)  # the hidden scale
f = ([s_b * sp.cot(z)] + [sp.exp(a4)] * 3 + [sp.Integer(1)]
     + [s_b * W(x0)] * 3)  # f_0, ..., f_7
g = sp.diag(*[ETA[a] * f[a] ** 2 for a in range(8)])  # the corrected metric
e = sp.diag(*f)  # the diagonal vielbein
on_history = {b4p: BETA_B4 * A_EXACT * H * b4, a4p: A_EXACT * H}  # the derivatives
history_values = {a4: A_EXACT * H * x4, b4: B4_ZERO * sp.exp(BETA_B4 * A_EXACT * H * x4)}
```

The corrected metric exactly as in Notebook 06a, In [7]: the coordinates, $H > 0$, the functions $a_4$ and $b_4 > 0$ with their derivatives `a4p` and `b4p`, the rate $h_4 = b_4'/(2b_4) - a_4'$ of the hidden scale, $z = 6Hx_0$, the warp factor $W$ as a function that knows only its derivative rule (so that every result holds for every real $z$), the hidden scale $s_b$, the eight vielbein factors, the metric and the vielbein; and the two substitutions of the history (derivatives first).

```python
Gam = christoffel(g, x)
mixed = mixed_spin_connection(e, Gam, x)  # omega_mu^a_b
omega = lower_first_index(mixed, ETA)  # omega_mu ab
```

The Christoffel symbols, the mixed connection $\omega_\mu{}^a{}_b$ and the lowered connection $\omega_{\mu ab}$.

```python
names = {sp.Symbol("H"): H, sp.Symbol("x0"): x0, sp.Symbol("x4"): x4,
         sp.Symbol("a4"): a4, sp.Symbol("b4"): b4, sp.Symbol("a4p"): a4p,
         sp.Symbol("b4p"): b4p, sp.Symbol("warp"): W(x0)}


def from_record(text):
    """A formula of the record (Wolfram notation) as a sympy expression."""
    for long_form, short_form in (("(Sin[6*H*x0]^2)^(1/12)", "warp"),
                                  ("Derivative[1][a4][x4]", "a4p"),
                                  ("Derivative[1][b4][x4]", "b4p"),
                                  ("a4[x4]", "a4"), ("b4[x4]", "b4")):
        text = text.replace(long_form, short_form)
    if "Sin[6*H*x0]^2" in text:  # a root that was not translated
        raise ValueError(f"cannot translate {text}")
    return parse_mathematica(text).subs(names, simultaneous=True)
```

`names` says which symbol or function of the notebook each name of the record stands for, and `from_record` reads a formula of the record: it gives the record's twelfth root $(\sin^2 z)^{1/12}$ the name `warp` (which becomes $W(x_0)$), the derivatives and the functions their short names, refuses a root it does not know (`raise ValueError`), and replaces the names by the notebook's symbols.

```python
omega_record = {(int(m) - 1, int(a) - 1, int(b) - 1): value
                for m, a, b, value in from_record(FORMULAS["omega_nonzero"])}
nonzero = {(mu, a, b): omega[mu][a][b] for mu in range(8) for a, b in pairs
           if omega[mu][a][b] != 0}
check(set(nonzero) == set(omega_record)
      and all(is_zero(nonzero[k] - omega_record[k]) for k in nonzero)
      and record_passed(REPORT_WL, "omega_components"),
      "the 10 nonzero lowered components omega_mu ab equal the record",
      record=f"{THEORY_FILE}, formula omega_nonzero")
```

The record's list `omega_nonzero` as a dictionary with Python's positions (the record numbers the directions from 1), and the nonzero lowered components with $a < b$ (`pairs` is the list of In [4]). The check requires the same 10 keys, the same values, and the WolframScript report's `omega_components` as passed.

```python
ACTION = {1: "kept", -1: "sign reversed", 0: "deleted"}
for (mu, a, b) in sorted(nonzero):
    k = int(factor[a][b])
    say(f"omega_{NAMES[mu]},{NAMES[a]}{NAMES[b]}: {KIND[k]} pair, {ACTION[k]}")
```

For each of the ten components (sorted by their keys) one line is printed with the kind of its pair and what the mixed contraction does to it: `omega_x0,x0x4: boost pair, deleted`, the three lines of 3-space, `omega_x1,x1x4: boost pair, deleted` and its two copies, and for each extra time `omega_x5,x0x5: boost pair, deleted` and `omega_x5,x4x5: time-time pair, sign reversed`. No line says kept.

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

The check of the identity of Section 6.23 for all eight $\mu$: $\Omega_\mu$ is the sum of its three parts, and $\Omega^{nb}_\mu = \Omega^{ss}_\mu - \Omega^{tt}_\mu$. (For the corrected metric $\Omega^{ss}_\mu = 0$ for every $\mu$.) The cell prints ten lines and two PASS lines.

**In [9], the closed forms.**

```python
closed_ok = (matrix_is_zero(Omega_nb[0]) and matrix_is_zero(Omega_nb[4])
             and matrix_is_zero(Omega[0] - h4 * s_b * sp.cot(z) * S[0][4]))
for i in (1, 2, 3):  # the 3-space directions x1, x2, x3
    closed_ok = closed_ok and matrix_is_zero(Omega_nb[i])  # pair (xi, x4) deleted
    closed_ok = closed_ok and matrix_is_zero(Omega[i] - a4p * sp.exp(a4) * S[i][4])
f_t = s_b * W(x0)  # the factor of the extra times
for t in (5, 6, 7):  # the extra times x5, x6, x7
    closed_ok = closed_ok and matrix_is_zero(
        Omega_nb[t] + h4 * f_t * S[4][t])  # pair (x4, xt) reversed
    closed_ok = closed_ok and matrix_is_zero(
        Omega[t] - h4 * f_t * S[4][t] - H * W(x0) * S[0][t])
check(closed_ok, "the closed forms of Omega_mu and Omega^nb_mu for all eight mu")
```

The closed forms of Section 6.23, matrix by matrix: $\Omega^{nb}_{x0} = 0$ and $\Omega^{nb}_{x4} = 0$ and the correct $\Omega_{x0} = h_4s_b\cot z\,S^{x0x4}$; for $i = 1, 2, 3$, $\Omega^{nb}_{x_i} = 0$ (the boost pair $(x_i, x4)$ is deleted) and the correct $\Omega_{x_i} = a_4'e^{a_4}S^{x_ix4}$; for $t = 5, 6, 7$, with $f_t = s_bW$, $\Omega^{nb}_{x_t} = -h_4f_tS^{x4x_t}$ (the time-time pair reversed, the boost pair $(x0, x_t)$ deleted) and the correct $\Omega_{x_t} = h_4f_tS^{x4x_t} + HW\,S^{x0x_t}$. `closed_ok` collects the comparisons (each `and` keeps it true only while all are true); one PASS line.

**In [10], the contraction direction by direction** (Section 6.23).

```python
gup = curved_gammas(e, gamma)  # gamma^mu = gamma^a / f_a for mu = a
```

The curved gammas $\gamma^\mu = \gamma^{(\mu)}/f_\mu$.

```python
def split(M):
    """(alpha, beta, rest is zero) for M = alpha gamma^(x4) + beta gamma^(x0)."""
    alpha = sp.simplify(-(M * gamma[4]).trace() / 16)  # coefficient of gamma^(x4)
    beta = sp.simplify((M * gamma[0]).trace() / 16)  # coefficient of gamma^(x0)
    return alpha, beta, matrix_is_zero(M - alpha * gamma[4] - beta * gamma[0])
```

`split(M)` finds the coefficients of $\gamma^{(x4)}$ and $\gamma^{(x0)}$ in a matrix $M$ with the traces of Section 6.8 and returns them together with the answer to the question whether nothing else is left.

```python
correct_terms = [split(gup[mu] * Omega[mu]) for mu in range(8)]
notebook_terms = [split(gup[mu] * Omega_nb[mu]) for mu in range(8)]
for mu in range(8):
    say(f"{NAMES[mu]}: correct ({correct_terms[mu][0]}, {correct_terms[mu][1]}), "
        f"notebook ({notebook_terms[mu][0]}, {notebook_terms[mu][1]})")
```

The eight terms $\gamma^\mu\Omega_\mu$ (no sum) of both contractions, split, and printed one line per direction: for $x0$ the correct term is $(\frac12h_4, 0)$ and the notebook's $(0, 0)$; for $x1, x2, x3$ the correct one is $(\frac12a_4', 0)$ and the notebook's $(0, 0)$; for $x4$ both are $(0, 0)$; for $x5, x6, x7$ the correct one is $(\frac12h_4, \frac12He^{a_4}b_4^{-1/2})$ and the notebook's $(-\frac12h_4, 0)$, printed as `(Derivative(a4(x4), x4)/2 - Derivative(b4(x4), x4)/(4*b4(x4)), 0)`.

```python
want_nb = [(0, 0)] * 5 + [(-h4 / 2, 0)] * 3  # x0, ..., x4, then x5, x6, x7
check(all(term[2] for term in correct_terms + notebook_terms)
      and all(is_zero(notebook_terms[mu][0] - want_nb[mu][0])
              and is_zero(notebook_terms[mu][1] - want_nb[mu][1]) for mu in range(8)),
      "notebook's terms: zero for x0 ... x4; -(h4/2) gamma^(x4) for x5, x6, x7")
```

The check requires that every term of both contractions is of the form $\alpha\gamma^{(x4)} + \beta\gamma^{(x0)}$ and that the notebook's terms are those derived in Section 6.23 (`want_nb`).

```python
slash = sum((gup[mu] * Omega[mu] for mu in range(8)), Z16)
slash_nb = sum((gup[mu] * Omega_nb[mu] for mu in range(8)), Z16)
c_g = sp.Rational(3, 2) * H * sp.exp(a4) / sp.sqrt(b4)  # correct gamma^(x0) term
v_g = b4p / b4 - a4p / 2  # correct gamma^(x4) term
```

The two totals, and the two coefficients $c_g$ and $v_g$ of the correct one.

```python
def record_total(formulas):
    """The record's gammaOmega_total as a 16 x 16 matrix."""
    text = formulas["gammaOmega_total"].replace(chr(34), "")  # gamma[x0], gamma[x4]
    total = from_record(text.replace("gamma[x0]", "G0").replace("gamma[x4]", "G4"))
    G0, G4 = sp.Symbol("G0"), sp.Symbol("G4")
    return total.coeff(G0) * gamma[0] + total.coeff(G4) * gamma[4]


check(matrix_is_zero(slash - record_total(FORMULAS))
      and matrix_is_zero(slash - c_g * gamma[0] - v_g * gamma[4])
      and record_passed(REPORT_PY, "gamma_mu_Omega_mu_equals_hidden_block_terms"),
      "correct: gamma^mu Omega_mu = c_g gamma^(x0) + v_g gamma^(x4)",
      record=f"{THEORY_FILE}, formula gammaOmega_total")
```

`record_total` reads the record's formula `gammaOmega_total` as in Notebook 06a, In [15] (the double quotes removed, the names `gamma[x0]` and `gamma[x4]` replaced by plain symbols whose coefficients are then multiplied by the matrices). The check requires the correct total to equal the record and $c_g\gamma^{(x0)} + v_g\gamma^{(x4)}$, and the sympy report to record the result as passed.

```python
report("notebook: coefficient of gamma^(x0)", sum(t[1] for t in notebook_terms))
report("notebook: coefficient of gamma^(x4)",
       sp.simplify(sum(t[0] for t in notebook_terms)))
check(matrix_is_zero(slash_nb + 3 * h4 / 2 * gamma[4]),
      "notebook: gamma^mu Omega^nb_mu = (3/2)(a4' - b4'/(2 b4)) gamma^(x4), no "
      "gamma^(x0) term")
```

Two RESULT lines print the notebook's total: the coefficient of $\gamma^{(x0)}$ is 0, and that of $\gamma^{(x4)}$ is `3*Derivative(a4(x4), x4)/2 - 3*Derivative(b4(x4), x4)/(4*b4(x4))`, that is $\frac32a_4' - \frac34b_4'/b_4$. The check requires $\sum_\mu\gamma^\mu\Omega^{nb}_\mu = -\frac32h_4\gamma^{(x4)}$ exactly.

```python
history_nb = slash_nb.subs(on_history).subs(history_values)
history_correct = slash.subs(on_history).subs(history_values)
check(matrix_is_zero(history_correct - sp.Rational(3, 2) * H * sp.exp(H * x4 / 3)
                     * gamma[0] - sp.Rational(5, 6) * H * gamma[4])
      and matrix_is_zero(history_nb - H / 2 * gamma[4]),
      "on the history of the record: correct (3/2) H e^(H x4/3) gamma^(x0) + "
      "(5/6) H gamma^(x4), notebook (H/2) gamma^(x4)")
```

On the history of the record: the correct total must be $\frac32He^{Hx_4/3}\gamma^{(x0)} + \frac56H\gamma^{(x4)}$ and the notebook's $\frac{H}{2}\gamma^{(x4)}$. The cell prints eight lines, two RESULT lines and four PASS lines.

**In [11], figure 3: the terms of both contractions as bars.**

```python
positions = np.arange(8)
width = 0.38  # the width of one bar; two bars side by side per direction
unit_x0 = H * sp.exp(a4) / sp.sqrt(b4)  # the unit of the gamma^(x0) coefficient
panels = [  # (title, function of a term (alpha, beta, ok) giving the bar height)
    ("$a_4'$ part of the $\\gamma^{(x4)}$ coefficient / $a_4'$",
     lambda t: float(sp.simplify(t[0].subs(b4p, 0) / a4p))),
    ("$b_4'$ part of the $\\gamma^{(x4)}$ coefficient / $(b_4'/b_4)$",
     lambda t: float(sp.simplify(t[0].subs(a4p, 0) / (b4p / b4)))),
    ("$\\gamma^{(x0)}$ coefficient / $(He^{a_4}b_4^{-1/2})$",
     lambda t: float(sp.simplify(t[1] / unit_x0)))]
```

`positions` are the eight directions and `width` the width of one bar (two bars stand side by side per direction). `panels` lists the three panels, each with its title and a small function (a **lambda**, a function written in one line, `lambda t: ...`) that turns a term `t` $= (\alpha, \beta, \ldots)$ into the height of its bar: the part of $\alpha$ proportional to $a_4'$ in units of $a_4'$ (set $b_4' = 0$ and divide), the part proportional to $b_4'/b_4$ in units of $b_4'/b_4$, and $\beta$ in units of $He^{a_4}b_4^{-1/2}$, as in Notebook 06a, In [16].

```python
fig, axes = plt.subplots(1, 3, figsize=(12.6, 4.2), sharey=True)
for ax, (title, height) in zip(axes, panels):
    correct_bars = [height(t) for t in correct_terms]
    notebook_bars = [height(t) for t in notebook_terms]
    ax.bar(positions - width / 2, correct_bars, width, color="tab:blue",
           label=f"correct (total {sum(correct_bars):g})")
    ax.bar(positions + width / 2, notebook_bars, width, color="lightskyblue",
           label=f"notebook (total {sum(notebook_bars):g})")
    ax.set_title(title, fontsize=9)
    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.set_xticks(positions, NAMES)
    ax.set_xlabel("direction $\\mu$ of the term $\\gamma^\\mu\\Omega_\\mu$")
    ax.set_ylim(-0.8, 0.8)
    ax.legend(fontsize=8, loc="lower left")
axes[0].set_ylabel("coefficient")
```

For each panel the eight correct bars (dark blue) and the eight notebook bars (light blue) are drawn beside each other, shifted by half a bar width to the left and to the right; each legend entry carries the total of its eight bars.

```python
save_figure(fig, "per_direction_comparison",
            "The eight terms $\\gamma^\\mu\\Omega_\\mu$ (no sum) of the corrected "
            ...
            "it loses the whole term $\\gamma^{(x0)}$.")
```

The figure is saved as `06c_3_per_direction_comparison.png`.

**What Figure 06c.3 shows.** On the left, the dark bars are $+\frac12$ for $x1, x2, x3$ and $-\frac12$ for $x0, x5, x6, x7$ (total $-\frac12$, the $a_4'$ part of $v_g$), while the light bars are zero everywhere except $+\frac12$ for the three extra times (total $\frac32$): the deleted boost parts of 3-space and of the hidden direction and the reversed time-time parts of the extra times change the time term completely. In the middle, the dark bars are $\frac14$ for the four directions of the hidden block (total 1) and the light bars $-\frac14$ for the extra times only (total $-\frac34$). On the right, the three dark bars of height $\frac12$ add to $\frac32$, the hidden term $c_g$; the light bars are all zero: the boost parts $(x0, x_t)$ of the extra times, which make the hidden term, are deleted.

**In [12], figure 4: the two totals as pictures.**

```python
SAMPLE = {H: 1, x0: sp.pi / 24}  # H = 1 and z = 6 H x0 = pi/4
B4_SAMPLE = sp.exp(sp.Rational(2, 3))  # b4 at a4 = 1/2 on the history, b4(0) = 1


def at_sample(expr):
    """The decimal value of expr at H = 1, z = pi/4 with the values of the history at
    a4 = 1/2: a4' = 1, b4 = e^(2/3), b4' = (4/3) b4 (derivatives first), with the
    explicit warp factor |sin z|^(1/6)."""
    expr = sp.sympify(expr).subs({a4p: 1, b4p: sp.Rational(4, 3) * B4_SAMPLE})
    expr = expr.subs({a4: sp.Rational(1, 2), b4: B4_SAMPLE})
    expr = expr.subs(W(x0), sp.Abs(sp.sin(z)) ** sp.Rational(1, 6))
    return float(sp.N(expr.subs(SAMPLE)))


def sample_table(matrix):
    """The matrix as an array of decimal numbers at the sample point."""
    return np.array([[at_sample(v) for v in row] for row in matrix.tolist()])
```

The sample point of Notebook 06a: $H = 1$, $z = \pi/4$, and the history at $a_4 = \frac12$ ($a_4' = 1$, $b_4 = e^{2/3}$, $b_4' = \frac43b_4$). `at_sample` inserts the derivatives first, then the functions and the explicit warp factor, and returns a decimal number; `sample_table` turns a matrix into an array of such numbers.

```python
fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.2))
for ax, (title, matrix) in zip(axes, (
        ("correct: $\\gamma^\\mu\\Omega_\\mu$", slash),
        ("notebook: $\\gamma^\\mu\\Omega^{nb}_\\mu$", slash_nb))):
    image = ax.imshow(sample_table(matrix), cmap="RdBu_r", vmin=-2.0, vmax=2.0)
    ax.set_title(title)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)
fig.colorbar(image, ax=axes, shrink=0.85, label="entry value")
```

The two totals as 16 x 16 heat maps with one common colour scale from $-2$ to $2$.

```python
save_figure(fig, "contraction_heat_maps",
            "The total $\\gamma^\\mu\\Omega_\\mu$ as a 16 x 16 heat map at the sample "
            ...
            "diagonal lines.")
```

The figure is saved as `06c_4_contraction_heat_maps.png`.

**What Figure 06c.4 shows.** On the left, the correct $c_g\gamma^{(x0)} + v_g\gamma^{(x4)}$: the value $c_g = \frac32e^{1/6} = 1.77$ (dark red) on two diagonal lines in the off-diagonal blocks, and the paler pattern of $\gamma^{(x4)}$ with entries $\pm\frac56$. On the right, the notebook's $\frac12\gamma^{(x4)}$: only the pattern of $\gamma^{(x4)}$, with entries $\pm0.5$, and nothing on the two diagonal lines. With the mixed contraction the term $c_g\gamma^{(x0)}$ would be missing from the field equation.

**In [13], the covariant constancy breaks** (Section 6.23).

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

For all 64 pairs $(\mu, \nu)$: `common` is the part that both versions of $D_\mu\gamma^\nu$ share, $\partial_\mu\gamma^\nu + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}\gamma^\lambda$; `D_correct` adds the commutator with $\Omega_\mu$, `D_nb` the commutator with $\Omega^{nb}_\mu$. `correct_ok` collects whether every correct one vanishes, and `identity_ok` whether every notebook one equals $[\Omega^{nb}_\mu - \Omega_\mu, \gamma^\nu]$ (Section 6.23). For each pair the nonzero entries of `D_nb` are counted (`not is_zero(v)` for each of the 256 entries); a pair with at least one is stored in the dictionary `violation`, and `entries` adds up the counts.

```python
check(correct_ok and record_passed(REPORT_WL, "gamma_covariantly_constant"),
      "correct: D_mu gamma^nu = 0 for all 64 pairs",
      record=f"{REPORT_WL}, check gamma_covariantly_constant")
check(identity_ok, "D^nb_mu gamma^nu = [Omega^nb_mu - Omega_mu, gamma^nu], all 64")
```

Two checks: the correct connection makes all 64 matrices vanish (with the record), and the identity of Section 6.23 holds for all 64 pairs.

```python
report("pairs (mu, nu) with D^nb_mu gamma^nu not zero", len(violation))
report("nonzero entries of these 16 x 16 matrices", entries)
say("violated pairs: " + ", ".join(f"({NAMES[m]},{NAMES[n]})"
                                   for m, n in sorted(violation)))
check(len(violation) == 17 and entries == 320,
      "notebook: D^nb_mu gamma^nu is not zero in 17 of 64 pairs (320 entries)")
```

Two RESULT lines print the number of violated pairs, 17, and of their nonzero entries, 320, and one line lists the pairs: `(x0,x0), (x0,x4)`, for each 3-space direction $(x_i, x_i)$ and $(x_i, x4)$, and for each extra time $(x_t, x0)$, $(x_t, x4)$ and $(x_t, x_t)$ (`", ".join(...)` writes the list with commas). The check requires exactly these counts, the ones derived by hand in Section 6.23.

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

The defining property $[\Omega_\mu, \gamma^a] + \sum_b\omega_\mu{}^a{}_b\gamma^b = 0$ is tested with the mixed components for both connections: `failures` lists the 17 pairs $(\mu, a)$ where it fails for $\Omega^{nb}$ (printed as a RESULT line), and the check requires at least one failure and none for the correct $\Omega_\mu$. The cell prints three RESULT lines, the list of pairs and four PASS lines.

**In [14], figure 5: where the constancy breaks.**

```python
size = np.zeros((8, 8))
for (mu, nu), matrix in violation.items():
    size[mu, nu] = np.abs(sample_table(matrix)).max()  # the largest entry
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

For each violated pair the largest absolute entry of $D^{nb}_\mu\gamma^\nu$ at the sample point is stored in an $8 \times 8$ array (all other squares stay 0), drawn in shades of orange, and printed in its square with two decimals (white digits on the dark squares).

```python
save_figure(fig, "constancy_violation",
            "Where the notebook's contraction breaks the covariant constancy of the "
            ...
            "all 64 matrices vanish exactly.")
```

The figure is saved as `06c_5_constancy_violation.png`.

**What Figure 06c.5 shows.** The row $x4$ is white, because $\Omega^{nb}_{x4} = \Omega_{x4} = 0$. The row $x0$ has two squares: $(x0, x0) = 0.33$, which is $\lvert h_4\rvert = \frac13$, and $(x0, x4) = 0.28$, which is $\lvert h_4\rvert f_0 = \frac13\cdot0.8465$. Each 3-space row has two squares: $(x_i, x_i) = 1.00$, which is $a_4' = 1$, and $(x_i, x4) = 1.65$, which is $a_4'f_1 = e^{1/2}$. Each extra-time row has three: $(x_t, x_t) = 1.18$, the larger of $2\lvert h_4\rvert = \frac23$ and $H/s_b = e^{1/6} = 1.18$; $(x_t, x4) = 0.53$, which is $2\lvert h_4\rvert f_5 = \frac23\cdot0.799$; and $(x_t, x0) = 1.12$, which is $HW\tan z/s_b = 0.944\cdot1/0.8465$. All values are those derived in Section 6.23. With the correct connection the whole grid would be white.

**In [15], why only the correct value is right** (Section 6.24).

```python
sqrt_g = sp.prod(f)  # f_0 ... f_7; the constant sign of cot z cancels below
divergence = sum(((sqrt_g * gup[mu]).diff(x[mu]) for mu in range(8)), Z16) / (2 * sqrt_g)
check(matrix_is_zero(divergence - slash) and not matrix_is_zero(divergence - slash_nb),
      "the divergence form equals the correct contraction, not the notebook's",
      record=f"{REPORT_WL}, check gammaOmega_divergence_form")
```

`sqrt_g` is the signed product $f_0\cdots f_7$ (its constant sign cancels in the formula, Section 6.9), and `divergence` the divergence form $\frac{1}{2\sqrt{\lvert g\rvert}}\sum_\mu\partial_\mu(\sqrt{\lvert g\rvert}\gamma^\mu)$. The check requires it to equal the correct contraction and not the notebook's.

```python
c_correct = sp.simplify(s_b * sum(t[1] for t in correct_terms))  # c = s_b beta
c_notebook = sp.simplify(s_b * sum(t[1] for t in notebook_terms))
report("c of the correct contraction", c_correct)
report("c of the notebook's contraction", c_notebook)
```

$c = s_b\beta$, where $\beta$ is the total coefficient of $\gamma^{(x0)}$ (the sum of the second entries of the eight terms of In [10]); two RESULT lines print $c = $ `3*H/2` for the correct contraction and $c = 0$ for the notebook's.

```python
p = sp.Function("p")(x0)  # two arbitrary functions of x0
q = sp.Function("q")(x0)
c = sp.Symbol("c", real=True)  # the coefficient in the operator A_c


def A(u):
    """The hidden-direction operator A_c u = du/dx0 + c cot z u."""
    return u.diff(x0) + c * sp.cot(z) * u


weight = W(x0) ** 3  # (sin^2 z)^(1/4)
```

Two arbitrary functions $p(x_0)$ and $q(x_0)$, a real symbol $c$, the operator $A_cu = \partial_0u + c\cot z\,u$ of Section 6.24, and the weight $W^3 = (\sin^2 z)^{1/4}$.

```python
leftover = weight * (p * A(q) + A(p) * q) - sp.diff(weight * p * q, x0)
check(is_zero(leftover - (2 * c - 3 * H) * sp.cot(z) * weight * p * q),
      "W^3 (p A_c q + (A_c p) q) - d0(W^3 p q) = (2c - 3H) cot z W^3 p q")
```

`leftover` is $W^3(p\,A_cq + (A_cp)\,q) - \partial_0(W^3p\,q)$, and the check proves exactly that it equals $(2c - 3H)\cot z\,W^3p\,q$ for every $c$ and all functions $p$, $q$: the identity derived line by line in Section 6.24 (sympy differentiates $W^3$ with the rule of $W$).

```python
record_text = FORMULAS["hidden_direction_hermiticity"]
check(is_zero(c_correct - 3 * H / 2) and is_zero(leftover.subs(c, c_correct))
      and "(d0 + (3/2) H Cot[z])" in record_text
      and "= d0 ((Sin[z]^2)^(1/4) p q)" in record_text
      and record_passed(REPORT_WL, "good_sector_hermiticity_curved"),
      "c = 3H/2: A_c is antisymmetric for the weight (sin^2 z)^(1/4) up to "
      "d0(W^3 p q)",
      record=f"{THEORY_FILE}, formula hidden_direction_hermiticity")
```

For the correct $c = \frac32H$ the leftover vanishes: $A_{3H/2}$ is antisymmetric for the weight $(\sin^2 z)^{1/4}$ up to the boundary term. The check also requires the record's formula `hidden_direction_hermiticity` to contain the operator `(d0 + (3/2) H Cot[z])` and the boundary term `= d0 ((Sin[z]^2)^(1/4) p q)`, and the WolframScript report's `good_sector_hermiticity_curved` as passed.

```python
check(c_notebook == 0
      and is_zero(leftover.subs(c, c_notebook) + 3 * H * sp.cot(z) * weight * p * q),
      "c = 0 (notebook): the leftover -3 H cot z (sin^2 z)^(1/4) p q remains")
```

For the notebook's $c = 0$ the leftover is $-3H\cot z\,(\sin^2 z)^{1/4}p\,q$, which no boundary term can absorb. The cell prints two RESULT lines and four PASS lines.

**In [16], figure 6: the leftover term.**

```python
zz = np.linspace(0.05, np.pi - 0.05, 400)  # one cell, without its ends
fig, ax = plt.subplots(figsize=(7.0, 4.2))
ax.axhline(0.0, color="gray", linewidth=0.6, zorder=1)  # the zero line, underneath
ax.axvline(np.pi / 2, color="gray", linewidth=0.6, zorder=1)  # the fold
for value, style, width, label in ((1.5, "-", 2.5, "correct $c = 3H/2$"),
                                   (0.75, "--", 1.5, "half of it, $c = 3H/4$"),
                                   (0.0, ":", 1.5, "notebook $c = 0$")):
    ax.plot(zz, (2 * value - 3) * np.abs(np.sin(zz)) ** 0.5 / np.tan(zz), style,
            linewidth=width, label=label, zorder=3)  # drawn above the zero line
ax.set_ylim(-8.0, 8.0)
ax.set_xlabel("hidden angle $z = 6Hx_0$ (radians), fold at $\\pi/2$")
ax.set_ylabel("leftover coefficient $(2c/H - 3)\\cot z\\,(\\sin^2 z)^{1/4}$")
ax.set_title("Only $c = 3H/2$ makes the hidden operator antisymmetric")
ax.legend(fontsize=8)
```

400 hidden angles over one cell without its ends; a thin gray zero line and a vertical line at the fold, drawn underneath the curves (`zorder=1`); and for $c = \frac32H$ (thick solid), $c = \frac34H$ (dashed) and $c = 0$ (dotted), with $H = 1$, the coefficient $(2c/H - 3)\cot z\,\lvert\sin z\rvert^{1/2}$ of $H\,p\,q$ in the leftover, drawn above them (`zorder=3`). The vertical axis is cut at $\pm8$.

```python
save_figure(fig, "hermiticity_defect",
            "The term that spoils the antisymmetry of the hidden-direction operator "
            ...
            "the solid line lies on the zero line.")
```

The figure is saved as `06c_6_hermiticity_defect.png`.

**What Figure 06c.6 shows.** The thick solid line of the correct value $c = \frac32H$ lies on the zero line for every $z$: nothing is left but the boundary term. The dashed line of half the value and the dotted line of the notebook's value $c = 0$ run from large negative values near the tip $z = 0$ through zero at the fold to large positive values near the tip $z = \pi$ (the factor $\cot z$ changes its sign at the fold); the dotted line is twice the dashed one. Only the correct coefficient makes the hidden-direction operator antisymmetric for the volume weight $(\sin^2 z)^{1/4}$.

**In [17], the last checks.**

```python
cited = {
    REPORT_PY: ["clifford_relations", "gammas_real", "vielbein_postulate",
                "spin_connection_antisymmetric", "covariant_constancy_D_mu_gamma_nu",
                "gamma_mu_Omega_mu_equals_hidden_block_terms",
                "divergence_of_sqrtg_gamma"],
    REPORT_WL: ["omega_components", "S_rotates_gamma_with_omega",
                "gamma_covariantly_constant", "gammaOmega_total",
                "gammaOmega_divergence_form", "good_sector_hermiticity_curved"],
}
count = sum(len(names) for names in cited.values())
check(all(record_passed(path, name) for path, names in cited.items()
          for name in names),
      f"the {count} cited record checks are recorded as passed")
```

The 13 cited checks of the two field-theory reports (seven of the sympy report and six of the WolframScript report) must be recorded as passed.

```python
expected = [f"06c_{k}_{name}.png" for k, name in enumerate([
    "pair_kinds", "milne_frame_and_spin_boost", "per_direction_comparison",
    "contraction_heat_maps", "constancy_violation", "hermiticity_defect"], 1)]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in expected),
      "all six figure files exist")
all_checks_passed()
```

The six figure files must exist, and the last line is printed: ALL 28 CHECKS PASSED (notebook 06c).

### 6.29 The exact scope of the statement that gravity enters the field equations

The author asked that the field equations of both fields "always possess non-zero contributions from gravity (through the canonical spin-connection, unless we are in flat 4+4 spacetime)". This chapter has proved several exact statements, and they must be read together. The Revision record states the conclusion in its own correction (in `Revision/README.md`): the non-triviality tests [1] and [2] hold in a qualified sense. Here is that sense, statement by statement.

**What is true in the diagonal vielbein.** $\sum_\mu\gamma^\mu D_\mu\Psi - \sum_\mu\gamma^\mu\partial_\mu\Psi = \big(c_g\gamma^{(x0)} + v_g\gamma^{(x4)}\big)\Psi$ with $c_g = \frac32He^{a_4}b_4^{-1/2}$ and $v_g = b_4'/b_4 - a_4'/2$. The matrix is nonzero for every $H > 0$ and all functions $a_4$, $b_4$ (because $c_g > 0$), and it sends a nonzero field to zero only at times where $c_g = \pm v_g$; on the history of the record that happens once, at $x_4 = 3\ln(5/9)/H \approx -1.7634/H$, before the first slice of the record's Kohn-Sham work, and never afterwards (Sections 6.8 and 6.10). The record's non-triviality checks `nontriviality_1_dirac16complex` and `nontriviality_2_dirac16complex00` of `wolfram-field-theory.json` and the check `gravity_term_square` of `python-field-theory.json` state this for every $a_4$ and $b_4$, with the exception $c_g = \pm v_g$.

**Where the term comes from.** The Lagrangian of Chapter 7 contains the symmetric kinetic term $\frac12\sum_\mu\big(\bar\Psi\gamma^\mu D_\mu\Psi - (D_\mu\bar\Psi)\gamma^\mu\Psi\big)$. Insert $D_\mu\Psi = \partial_\mu\Psi + \Omega_\mu\Psi$ and $D_\mu\bar\Psi = \partial_\mu\bar\Psi - \bar\Psi\Omega_\mu$ (Section 6.7):

$$
\tfrac12\sum_\mu\big(\bar\Psi\gamma^\mu\partial_\mu\Psi - (\partial_\mu\bar\Psi)\gamma^\mu\Psi\big) + \tfrac12\sum_\mu\bar\Psi\big(\gamma^\mu\Omega_\mu + \Omega_\mu\gamma^\mu\big)\Psi
$$

(multiply out; the two $\Omega$ terms collect into one). By Fact 1 of Section 6.9 the last bracket vanishes for each $\mu$ separately. **In the corrected metric and the diagonal vielbein the canonical spin connection drops out of the Lagrangian completely.** The term $c_g\gamma^{(x0)} + v_g\gamma^{(x4)}$ comes back in the field equation from the volume factor and the vielbein: vary the connection-free term $\sqrt{\lvert g\rvert}\,\frac12\sum_\mu(\bar\Psi\gamma^\mu\partial_\mu\Psi - (\partial_\mu\bar\Psi)\gamma^\mu\Psi)$ with respect to $\bar\Psi$ by the Euler-Lagrange rule of Chapter 7 (the derivative by $\bar\Psi$ minus $\sum_\mu\partial_\mu$ of the derivative by $\partial_\mu\bar\Psi$, the two treated as independent):

$$
\tfrac12\sqrt{\lvert g\rvert}\sum_\mu\gamma^\mu\partial_\mu\Psi - \sum_\mu\partial_\mu\Big(-\tfrac12\sqrt{\lvert g\rvert}\,\gamma^\mu\Psi\Big) = \sqrt{\lvert g\rvert}\sum_\mu\gamma^\mu\partial_\mu\Psi + \tfrac12\sum_\mu\partial_\mu\big(\sqrt{\lvert g\rvert}\,\gamma^\mu\big)\Psi
$$

(the product rule on the second term). Divided by $\sqrt{\lvert g\rvert}$ the last term is the divergence form of Section 6.9, $\sum_\mu\gamma^\mu\Omega_\mu\Psi = \big(c_g\gamma^{(x0)} + v_g\gamma^{(x4)}\big)\Psi$. The record calls it the **half-density term** (volume and vielbein divergence). Chapter 7 carries out the variation for both statistics with every sign. Records: both scope reports, check `connection_free_lagrangian_same_equations`; `wolfram-field-theory.json`, checks `L_spin_connection_drops_out_G` and `L_spin_connection_drops_out_C`.

**What depends on choices.** The value of $\gamma^\mu\Omega_\mu$ belongs to the diagonal vielbein: in the frame boosted in the plane of $x4$ and $x0$ with $b' = 2c_g$ the term $c_g\gamma^{(x0)}$ vanishes identically and only $v_g(\cosh b\,\gamma^{(x4)} - \sinh b\,\gamma^{(x0)})$ remains; no boost in that plane removes this part unless $v_g = 0$ (Section 6.16). It also belongs to the field variable $\Psi$: for $\chi = e^{-a_4/2}b_4(\sin^2 z)^{1/8}\,\Psi$ the term is absent for $U = 0$ and becomes the coupling $\lambda e^{a_4}S[\chi]/(b_4^2\lvert\sin z\rvert^{1/2})$ for $U = \frac\lambda2S^2$ (Section 6.18).

**What does not depend on any choice.**

- Wherever the metric is curved, the spin connection vanishes in no frame: its curvature is the Riemann curvature, $F_{\mu\nu} = \frac12R_{ab\mu\nu}S^{ab}$, and on the history of the record the metric is curved ($K(x1, x2) = H^2$, $R = H^2(\frac{56}{9} - 12e^{2Hx_4/3})$; Section 6.17). The metric is flat only for special functions, such as $a_4 = 0$, $b_4 = H^2x_4^2$; there the connection is a pure effect of the frame, the case the author excluded with the words "unless we are in flat 4+4 spacetime".
- The vielbein enters every derivative term of the field equation through the factors $e^{-a_4}$, $e^{a_4}b_4^{-1/2}\tan z$ and $e^{a_4}b_4^{-1/2}W^{-1}$; this is where the inflation of 3-space and the exponential deflation of the hidden block act on the fields (Section 6.10).
- The spin connection reaches the energy-momentum tensor of the fields: for a configuration $\Phi$ that depends on the time only, the connection part of the kinetic term $K^{x4}{}_{x5}$ is $\frac12HW\,\bar\Phi\gamma^{(x4)}\gamma^{(x0)}\gamma^{(x5)}\Phi$, which is not identically zero, while that of $K^{x4}{}_{x1}$ vanishes because 3-space does not depend on $x_0$ (both scope reports, check `spin_connection_in_the_energy_momentum_tensor`; Chapter 9 treats the energy-momentum tensor).

**In one sentence.** Gravity enters the field equations of both fields in every frame and every choice of field variables, through the vielbein factors and through a spin connection whose curvature cannot be removed where the metric is curved; the particular matrix $c_g\gamma^{(x0)} + v_g\gamma^{(x4)}$ ($\frac32He^{Hx_4/3}\gamma^{(x0)} + \frac56H\gamma^{(x4)}$ on the history of the record) is the form this takes in the diagonal vielbein with the variable $\Psi$, and it is a property of these choices, not of the physics alone. Chapter 8 returns to this scope and adds the question of well-posedness.

| statement | status | where it is verified |
| --- | --- | --- |
| the connection drops out of the symmetric Lagrangian; the field equations are those of the connection-free symmetric Lagrangian, with the half-density term | PROVED | both scope reports, check `connection_free_lagrangian_same_equations`; `wolfram-field-theory.json`, checks `L_spin_connection_drops_out_G`, `L_spin_connection_drops_out_C` |
| the value of $\gamma^\mu\Omega_\mu$ is frame-dependent and removable by a rescaling | PROVED | Sections 6.16 and 6.18 (Notebook 06b; both scope reports) |
| the spin connection vanishes in no frame where the metric is curved; the metric is curved on the history and flat for special $a_4$, $b_4$ | PROVED | Section 6.17 |
| the connection enters the energy-momentum tensor through the extra times | PROVED | both scope reports, check `spin_connection_in_the_energy_momentum_tensor` |

### 6.30 What we proved, what we computed, what we assumed

**PROVED** (exact; derived in this chapter line by line, confirmed by exact checks of the notebooks named, and, where stated, by the Revision record):

- The diagonal vielbein $f = (s_b\cot z,\ e^{a_4}\ (\times3),\ 1,\ s_bW\ (\times3))$, $s_b = e^{-a_4}b_4^{1/2}$, $W = (\sin^2 z)^{1/12}$, reproduces the corrected metric; $\sqrt{\lvert\det g\rvert} = e^{-a_4}b_4^2\lvert\cot z\rvert(\sin^2 z)^{1/4}$, so the 7-volume grows at the rate $-a_4' + 2b_4'/b_4$; the curved gammas obey $\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu = 2g^{\mu\nu}$; every $\Lambda e$ with $\Lambda^T\eta\Lambda = \eta$ is another vielbein (Section 6.2; Notebook 06a, In [7]; the formulas `metric`, `vielbein_diagonal` and `sqrt_det_g` of `field-theory.json`; the checks `metric_from_vielbein_equals_SPEC` and `sqrt_det_g` of the sympy report, `metric_is_the_corrected_metric` and `sqrt_det_g` of the WolframScript report, and `vielbein_reproduces_metric` of the lead's report).
- The 21 independent nonzero Christoffel symbols (Section 6.3; Notebook 06a, In [9]; formula `christoffel_nonzero` of `field-theory.json`, check `christoffel_count`).
- The vielbein postulate has exactly one solution, the canonical spin connection, and its lowered form is antisymmetric; for the corrected metric it has exactly 10 independent nonzero components, each a rate ($a_4'$, $h_4$ or $H$) times a nonvanishing factor, so it vanishes only for constant $a_4$, $b_4$ and $H = 0$ (Sections 6.4 and 6.6; Notebook 06a, In [11]; formula `omega_nonzero` of `field-theory.json`; checks `vielbein_postulate`, `spin_connection_antisymmetric`, `omega_components`, `Omega_vanishes_iff_a4prime_b4prime_and_H_vanish`).
- $\Omega_\mu = \frac12\sum_{a,b}\omega_{\mu ab}S^{ab}$ is the unique traceless solution of the defining property; it makes the curved gammas covariantly constant; $\Omega_{x4} = 0$ and $\Omega_{x0} = \frac12h_4s_b\cot z\,\gamma^{(x0)}\gamma^{(x4)} \neq 0$ (Section 6.7; Notebook 06a, In [13]; the formula `Omega_components` of the record; the checks `S_rotates_gamma_with_omega` and `gamma_covariantly_constant` of the WolframScript report, and the checks `covariant_constancy_D_mu_gamma_nu` and `Omega_x4_vanishes_Omega_x0_does_not` of the sympy report).
- $\gamma^\mu\Omega_\mu = c_g\gamma^{(x0)} + v_g\gamma^{(x4)}$ in the diagonal vielbein, for every $H > 0$, $a_4$ and $b_4$, and $\frac32He^{Hx_4/3}\gamma^{(x0)} + \frac56H\gamma^{(x4)}$ on the history of the record: along the time 3-space pushes $+\frac32a_4'$ and the four directions of the hidden block $2h_4$, together half the rate of the 7-volume; along the hidden direction only the warp of the three extra times pushes; equivalently, the divergence form (Sections 6.8 and 6.9; Notebook 06a, In [15] and In [18]; in the record the formulas `gammaOmega_per_direction` and `gammaOmega_total`; in the WolframScript report the checks of the same two names and the check `gammaOmega_divergence_form`; in the sympy report the checks `per_direction_terms`, `gamma_mu_Omega_mu_equals_hidden_block_terms` and `divergence_of_sqrtg_gamma`; and in the lead's report the checks `gamma_Omega_equals_hidden_block_terms` and `gamma_Omega_divergence_formula`).
- The Dirac operator written out, all sixteen components; the term $M\Psi$ with $MM = (c_g^2 - v_g^2)\,1$ vanishes only for $\Psi = 0$ unless $c_g = \pm v_g$, where $M$ has rank 8; on the history $MM = H^2(\frac94e^{2Hx_4/3} - \frac{25}{36})\,1$, zero only at $x_4 = 3\ln(5/9)/H$ (Section 6.10; Notebook 06a, In [20]; the checks `Dirac_operator_explicit_G` and `Dirac_operator_explicit_C`, `nontriviality_1_dirac16complex` and `nontriviality_2_dirac16complex00` of the WolframScript report and `gravity_term_square` of the sympy report).
- The negative control: with a hidden block that grows like 3-space the contraction is $\frac32He^{-a_4}b_4^{-1/2}\gamma^{(x0)} + (b_4'/b_4 + \frac72a_4')\gamma^{(x4)}$; the term sees in which direction the hidden block changes (Section 6.10; Notebook 06a, In [22]; lead report, check `negative_control_growing_block`).
- Local spin covariance $\Omega'_\mu = R\Omega_\mu R^{-1} - (\partial_\mu R)R^{-1}$, $\gamma'^\mu = R\gamma^\mu R^{-1}$, $F' = RFR^{-1}$ (Sections 6.15 and 6.17; Notebook 06b, In [12] and In [16]).
- In the frame boosted in the plane of $x4$ and $x0$ with any rapidity $b(x_4)$, $\gamma'^\mu\Omega'_\mu = (c_g - \frac{b'}2)(\cosh b\,\gamma^{(x0)} - \sinh b\,\gamma^{(x4)}) + v_g(\cosh b\,\gamma^{(x4)} - \sinh b\,\gamma^{(x0)})$; for $b' = 2c_g$ only the term $v_g$ remains, no boost in this plane removes it, and $\Omega'_\mu \neq 0$ for all eight $\mu$ (Section 6.16; Notebook 06b, In [8] and In [10]; both scope reports, checks `boosted_frame_gammaOmega_formula`, `boosted_frame_removes_only_the_H_term`).
- The Riemann tensor of the corrected metric consists of the 28 plane curvatures, free of $x_0$; the Ricci and Einstein tensors are diagonal, with $R^{x0}{}_{x0} = R^{x_t}{}_{x_t}$; on the history $R^{x1}{}_{x1} = \frac53H^2$, $R^{x4}{}_{x4} = \frac{31}{9}H^2$, $R^{x0}{}_{x0} = -(\frac59 + 3e^{2Hx_4/3})H^2$ and $R = H^2(\frac{56}{9} - 12e^{2Hx_4/3})$; the metric is flat for $a_4 = 0$, $b_4 = H^2x_4^2$ and curved on the history; $\gamma^\mu\Omega_\mu$ contains $a_4$; $F_{\mu\nu} = \frac12R_{ab\mu\nu}S^{ab} = \eta_{\mu\mu}\eta_{\nu\nu}f_\mu f_\nu K(\mu, \nu)S^{\mu\nu}$ in all 28 planes; $F'_{x0x5} \neq 0$ in the boosted frame (Section 6.17, whose table names the records that prove the same; Notebook 06b, In [13], In [14] and In [16]).
- The rescaling $\Psi = e^{a_4/2}b_4^{-1}(\sin^2 z)^{-1/8}\,\chi$ removes the term; with $U = \frac\lambda2S^2$ it becomes $\lambda e^{a_4}S[\chi]/(b_4^2\lvert\sin z\rvert^{1/2})$ (Section 6.18; Notebook 06b, In [18]; both scope reports, checks `rescaling_removes_the_connection_term`, `rescaled_equation_quadratic_potential`).
- The mixed contraction equals $\Omega^{ss} - \Omega^{tt}$: it keeps 6, reverses 6 and deletes 16 of the 28 parts; it agrees with the correct one in the polar plane and deletes the whole connection in the Milne wedge (Section 6.23; Notebook 06c, In [4], In [6], In [8]).
- Only $c = \frac32H$ makes the hidden-direction operator antisymmetric for the weight $(\sin^2 z)^{1/4}$ (times the constant $b_4^{3/2}$ along $x0$), up to the boundary term $[(\sin^2 z)^{1/4}p\,q]$ (Section 6.24; Notebook 06c, In [15]; formula `hidden_direction_hermiticity`; check `good_sector_hermiticity_curved`).
- In the diagonal vielbein the canonical connection drops out of the symmetric Lagrangian, and $\gamma^\mu\Omega_\mu$ is the half-density term of its field equation (Section 6.29; both scope reports, check `connection_free_lagrangian_same_equations`).

**COMPUTED** (by the notebooks):

- The central differences of Notebook 06a, In [19], reproduce the constant $\frac32$ (the hidden coefficient divided by $e^{a_4}b_4^{-1/2}$, $H = 1$) to $2 \times 10^{-7}$ over both halves of a cell, the size expected for the step $h = 10^{-5}$ next to the tips, and $v_g$ for the illustrative $b_4 = e^{4x_4/3}(1 + \frac12\sin x_4)$ to $2 \times 10^{-10}$.
- The single time of the history at which the term degenerates, $x_4H = 3\ln(5/9) = -1.7634$ (Notebook 06a, In [20], from the record's formula).
- The figures at the sample points, on the history of the record: in Notebook 06a $H = 1$, $z = \pi/4$, $a_4 = \frac12$, $a_4' = 1$, $b_4 = e^{2/3}$, $b_4'/b_4 = \frac43$, for example $\omega_{x0\,x0x4} = -0.28$, $\omega_{x1\,x1x4} = 1.65$, $\omega_{x5\,x0x5} = 0.94$, $\omega_{x5\,x4x5} = -0.27$ and $c_g = 1.77$; in Notebook 06b the same values with $a_4'' = 0$, the sizes of the spinor curvature from $0.178$ to $5.437$ (in units of $H^2$; In [17]), all 28 planes curved there.
- Exact counts made by the notebooks themselves, not stated in the Revision record: 14 nonzero components of the boosted spin connection (Notebook 06b, In [7]); 56 nonzero Riemann components $R^\rho{}_{\sigma\mu\nu}$ with $\mu < \nu$ (Notebook 06b, In [13]); for the mixed contraction, $\frac32(a_4' - \frac{b_4'}{2b_4})\gamma^{(x4)}$ with no term $\gamma^{(x0)}$, 17 violated pairs with 320 nonzero entries, and 17 pairs in which its defining property fails (Notebook 06c, In [10] and In [13]). These last describe a contraction that the record does not use.

**ASSUMED**: the corrected metric of 2026-10-16 and the roles of the author's coordinates (the input of the theory); the history of the record, $a_4 = AHx_4$ and $b_4 = b_4(0)\,e^{\beta AHx_4}$ with $A = 1$, $\beta = \frac43$ and $b_4(0) = 1$ (read from `parameters.json`; the prescribed background of Chapter 3), used in the checks on the history and in the figures (with $H = 1$), and the illustrative $b_4 = e^{4x_4/3}(1 + \frac12\sin x_4)$ in figure 8 of Notebook 06a (no general result depends on them); two standard theorems quoted without proof: Jacobi's formula for the derivative of a determinant (Section 6.15) and the general identity $F_{\mu\nu} = \frac12R_{ab\mu\nu}S^{ab}$, which is however checked exactly for the corrected metric (Section 6.17); and the record's statement about the author's notebook contraction (Section 6.23), which this book takes from `Revision/SPEC.md`.

**HYPOTHESIS and OPEN**: this chapter states no hypothesis. The boundary condition at the fold $\cos z = 0$, needed for the antisymmetry of the hidden-direction operator, is not fixed here (Section 6.24); Chapter 14 treats the conditions at the fold, which are ASSUMED there. Nothing in this chapter concerns the creation of universes or matter and antimatter.

### 6.31 Exercises

**Exercise 1 (the sphere).** The unit sphere has the metric $ds^2 = d\theta^2 + \sin^2\theta\,d\varphi^2$ ($0 < \theta < \pi$), the frame metric $\eta = \mathrm{diag}(1, 1)$, the vielbein factors $f_\theta = 1$, $f_\varphi = \sin\theta$, and the gammas $\gamma^0 = \sigma_1$, $\gamma^1 = \sigma_2$. Compute the Christoffel symbols, the spin connection, $\Omega_\mu$, $\sum_\mu\gamma^\mu\Omega_\mu$ (check it with the divergence form) and $F_{\theta\varphi}$. Is the sphere flat?

*Answer.* Case (c) of Section 6.3: $\Gamma^\theta{}_{\varphi\varphi} = -f_\varphi\partial_\theta f_\varphi/f_\theta^2 = -\sin\theta\cos\theta$; case (b): $\Gamma^\varphi{}_{\varphi\theta} = \partial_\theta\ln\sin\theta = \cot\theta$; all others vanish. By Section 6.6 the only nonzero component is $\omega_{\varphi\,10} = \eta_{11}\,\partial_\theta f_\varphi/f_\theta = \cos\theta$, so $\omega_{\varphi\,01} = -\cos\theta$. With $S^{01} = \frac12\sigma_1\sigma_2 = \frac i2\sigma_3$: $\Omega_\varphi = -\cos\theta\,S^{01} = -\frac i2\cos\theta\,\sigma_3$ and $\Omega_\theta = 0$. With $\gamma^\varphi = \sigma_2/\sin\theta$: $\sum_\mu\gamma^\mu\Omega_\mu = \frac{\sigma_2}{\sin\theta}\big(-\frac i2\cos\theta\,\sigma_3\big) = -\frac{i\cot\theta}{2}\sigma_2\sigma_3 = -\frac{i\cot\theta}{2}\,i\sigma_1 = \frac{\cot\theta}{2}\sigma_1$. Divergence form with $\sqrt{\lvert g\rvert} = \sin\theta$: $\frac{1}{2\sin\theta}\big(\partial_\theta(\sin\theta\,\sigma_1) + \partial_\varphi(\sin\theta\cdot\sigma_2/\sin\theta)\big) = \frac{\cos\theta}{2\sin\theta}\sigma_1$, the same. Finally $F_{\theta\varphi} = \partial_\theta\Omega_\varphi - \partial_\varphi\Omega_\theta + [\Omega_\theta, \Omega_\varphi] = \partial_\theta\big(-\frac i2\cos\theta\,\sigma_3\big) = \frac i2\sin\theta\,\sigma_3 \neq 0$. The sphere is curved: unlike the polar plane of Section 6.5, here no change of frame can remove the spin connection (Section 6.17). (Check with the formula of Section 6.17: the plane curvature of the unit sphere is $K(\theta, \varphi) = 1$, so $F_{\theta\varphi} = \eta_{00}\eta_{11}f_\theta f_\varphi K\,S^{01} = \sin\theta\cdot\frac i2\sigma_3$.)

**Exercise 2 (an extra time by hand).** Compute $\omega_{x6\,ab}$ for the corrected metric with the formula of Section 6.6 and then $\gamma^{x6}\Omega_{x6}$, without looking at Section 6.8. Why is the coefficient of $\gamma^{(x4)}$ negative on the history of the record?

*Answer.* $f_6 = s_bW$ has $\partial_4f_6 = h_4f_6$ (the rate of $s_b$; $W$ does not depend on $x_4$) and $\partial_0f_6 = H\cot z\,f_6$ (the rule of $W$; $s_b$ does not depend on $x_0$). With $\omega_{\mu\,\mu b} = \eta_{\mu\mu}\partial_bf_\mu/f_b$ and $\eta_{66} = -1$: $\omega_{x6\,x6\,x4} = (-1)h_4f_6/1 = -h_4f_6$, hence $\omega_{x6\,x4\,x6} = h_4f_6$; and $\omega_{x6\,x6\,x0} = (-1)H\cot z\,f_6/(s_b\cot z) = -HW$, hence $\omega_{x6\,x0\,x6} = HW$. So $\Omega_{x6} = h_4f_6\,S^{x4x6} + HW\,S^{x0x6}$ and

$$
\gamma^{x6}\Omega_{x6} = \frac{\gamma^{(x6)}}{f_6}\Big(\frac{h_4f_6}2\gamma^{(x4)}\gamma^{(x6)} + \frac{HW}2\gamma^{(x0)}\gamma^{(x6)}\Big) = \frac{h_4}2\gamma^{(x6)}\gamma^{(x4)}\gamma^{(x6)} + \frac{H}{2s_b}\gamma^{(x6)}\gamma^{(x0)}\gamma^{(x6)} .
$$

Since $\gamma^{(x6)}\gamma^{(x4)}\gamma^{(x6)} = -\gamma^{(x4)}(\gamma^{(x6)})^2 = \gamma^{(x4)}$ and likewise $\gamma^{(x6)}\gamma^{(x0)}\gamma^{(x6)} = \gamma^{(x0)}$, $\gamma^{x6}\Omega_{x6} = \frac{h_4}2\gamma^{(x4)} + \frac12He^{a_4}b_4^{-1/2}\gamma^{(x0)}$. On the history $h_4 = \frac23H - H = -\frac13H < 0$, so the coefficient $-\frac H6$ is negative: the extra time shrinks there ($f_6 \propto e^{-Hx_4/3}$) while a 3-space direction grows. The hidden direction contributes the same $\frac{h_4}2$ along the time, because it shrinks at the same rate.

**Exercise 3 (a general deflation rate).** Replace the hidden scale by $e^{-ka_4}b_4^{1/2}$ with a constant $k$, in the hidden factor and in the three extra-time factors (the corrected metric has $k = 1$, the negative control $k = -1$). Use the divergence form to find both coefficients of $\sum_\mu\gamma^\mu\Omega_\mu$. For which $k$ does the part with $a_4'$ vanish, and what does that mean for the 7-volume?

*Answer.* The product of the eight factors is

$$
e^{-ka_4}b_4^{1/2}\cot z\cdot e^{3a_4}\cdot1\cdot e^{-3ka_4}b_4^{3/2}W^3 = e^{(3-4k)a_4}b_4^2\cot z\,W^3
$$

(the exponents add). The time coefficient is half the derivative of its logarithm, $\frac12\partial_4\big((3 - 4k)a_4 + 2\ln b_4\big) = \frac{3 - 4k}{2}a_4' + \frac{b_4'}{b_4}$: for $k = 1$ it is $-\frac12a_4' + b_4'/b_4 = v_g$, for $k = -1$ it is $\frac72a_4' + b_4'/b_4$, the negative control of Section 6.10. The part with $a_4'$ vanishes only for $k = \frac34$: then the growth $e^{3a_4}$ of the three 3-space directions is exactly balanced by the shrinking $e^{-4ka_4} = e^{-3a_4}$ of the four directions of the hidden block, and the 7-volume changes with the time only through $b_4$. The hidden coefficient is $\frac{1}{2f_0\cdots f_7}\partial_0\big(e^{3a_4}e^{-3ka_4}b_4^{3/2}W^3\big) = \frac{3H\cot z\,e^{(3-3k)a_4}b_4^{3/2}W^3}{2e^{(3-4k)a_4}b_4^2\cot z\,W^3} = \frac32He^{ka_4}b_4^{-1/2}$: $\frac32H$ divided by the hidden scale, for every $k$.

**Exercise 4 (the boosted contraction in numbers).** Take $H = 1$ and the constant rapidity rate $b = 3x_4$ on the history of the record ($c_g = \frac32e^{x_4/3}$, $v_g = \frac56$). Give the coefficients $c_0$ of $\gamma^{(x0)}$ and $c_4$ of $\gamma^{(x4)}$ in $\gamma'^\mu\Omega'_\mu$ at $x_4 = 0$ and at $x_4 = \frac13$, and check the invariant of Section 6.16. Which constant rate $\beta$ (with $b = \beta x_4$) gives $c_0 = -3$ at $x_4 = 0$, and what is $c_4$ there?

*Answer.* By Section 6.16, $c_0 = (c_g - \frac{b'}2)\cosh b - v_g\sinh b$ and $c_4 = -(c_g - \frac{b'}2)\sinh b + v_g\cosh b$ with $b' = 3$. At $x_4 = 0$: $b = 0$ and $c_g = \frac32$, so $c_0 = 0$ and $c_4 = \frac56$; this rate removes the $c_g$ term at this one time. At $x_4 = \frac13$: $b = 1$, $\cosh 1 = 1.54308$, $\sinh 1 = 1.17520$, $c_g = \frac32e^{1/9} = 1.67628$, so $c_g - \frac32 = 0.17628$ and $c_0 = 0.17628\cdot1.54308 - 0.83333\cdot1.17520 = -0.70732$, $c_4 = -0.17628\cdot1.17520 + 0.83333\cdot1.54308 = 1.07874$. The invariant: $\cosh 1\cdot c_4 + \sinh 1\cdot c_0 = 1.66459 - 0.83125 = 0.83334 = \frac56$ up to rounding. At $x_4 = 0$ the coefficient of $\gamma^{(x0)}$ is $c_g - \frac\beta2 = \frac32 - \frac\beta2$, which equals $-3$ for $\beta = 9$; the coefficient of $\gamma^{(x4)}$ is $v_g\cosh 0 = \frac56$ for every rate. A frame can thus give the coefficient of $\gamma^{(x0)}$ any value at one instant; that value is not a property of the metric, while the combination $\cosh b\,c_4 + \sinh b\,c_0 = v_g$ is the same in every frame of this family.

**Exercise 5 (rescaling with a general power).** Let $\Psi = (\sin^2 z)^{\alpha/2}\,\chi$ with a constant $\alpha$ (and no factor depending on the time) in the diagonal vielbein. Show that $\sum_\mu\gamma^\mu D_\mu\Psi = (\sin^2 z)^{\alpha/2}\big(\sum_\mu\gamma^\mu\partial_\mu\chi + \frac32H(4\alpha + 1)e^{a_4}b_4^{-1/2}\gamma^{(x0)}\chi + v_g\gamma^{(x4)}\chi\big)$. Which $\alpha$ removes the term with $\gamma^{(x0)}$, which leaves it unchanged, and what removes the term with $\gamma^{(x4)}$?

*Answer.* By the product rule, and because only $x_0$ appears in the factor,

$$
\sum_\mu\gamma^\mu D_\mu\big((\sin^2 z)^{\alpha/2}\chi\big) = (\sin^2 z)^{\alpha/2}\sum_\mu\gamma^\mu\partial_\mu\chi + \Big(\gamma^{x0}\partial_0(\sin^2 z)^{\alpha/2} + (\sin^2 z)^{\alpha/2}\big(c_g\gamma^{(x0)} + v_g\gamma^{(x4)}\big)\Big)\chi .
$$

With $(\sin^2 z)^{\alpha/2} = W^{6\alpha}$ and the rule of $W$, $\partial_0W^{6\alpha} = 6\alpha W^{6\alpha - 1}H\cot z\,W = 6\alpha H\cot z\,W^{6\alpha}$ (the power rule), and with $\gamma^{x0} = e^{a_4}b_4^{-1/2}\tan z\,\gamma^{(x0)}$,

$$
\gamma^{x0}\partial_0(\sin^2 z)^{\alpha/2} = 6\alpha H e^{a_4}b_4^{-1/2}\tan z\cot z\,(\sin^2 z)^{\alpha/2}\gamma^{(x0)} = 6\alpha He^{a_4}b_4^{-1/2}(\sin^2 z)^{\alpha/2}\gamma^{(x0)}
$$

($\tan z\cot z = 1$). Adding $c_g = \frac32He^{a_4}b_4^{-1/2}$ gives $(6\alpha + \frac32)He^{a_4}b_4^{-1/2} = \frac32H(4\alpha + 1)e^{a_4}b_4^{-1/2}$ in front of $\gamma^{(x0)}$, which is the formula. $\alpha = -\frac14$ removes the term with $\gamma^{(x0)}$ (the factor $(\sin^2 z)^{-1/8}$ of Section 6.18), and $\alpha = 0$ leaves it unchanged; the term with $\gamma^{(x4)}$ is removed by the further factor $e^{a_4/2}b_4^{-1}$, whose logarithmic derivative is $-v_g$ (Section 6.18). The record's exact solution family contains both: its solutions (i-a) carry the factor $(\sin^2 z)^{\alpha/2}$, and the case (i-b) is $\alpha = -\frac14$ (`field-theory.json`, formula `exact_solutions`; the scope check `rescaled_equation_quadratic_potential` names the coefficient $\frac32H(4\alpha + 1)e^{a_4}b_4^{-1/2}$).

**Exercise 6 (mixed components).** Using $\omega_\mu{}^b{}_a = -\eta_{aa}\eta_{bb}\,\omega_\mu{}^a{}_b$ (Section 6.4), show that the mixed components of a time-time pair are antisymmetric and those of a boost pair symmetric. Then compute $\Omega^{nb}_{x2}$ and $\Omega^{nb}_{x7}$ for the corrected metric.

*Answer.* For a time-time pair $\eta_{aa}\eta_{bb} = (-1)(-1) = +1$, so $\omega_\mu{}^b{}_a = -\omega_\mu{}^a{}_b$: antisymmetric. For a boost pair $\eta_{aa}\eta_{bb} = -1$, so $\omega_\mu{}^b{}_a = +\omega_\mu{}^a{}_b$: symmetric, and in $\frac12\sum_{a,b}\omega_\mu{}^a{}_bS^{ab}$ its two terms cancel because $S^{ba} = -S^{ab}$. For $x2$ the only nonzero component is that of the pair $(x2, x4)$, a boost pair (deleted): $\Omega^{nb}_{x2} = 0$, while $\Omega_{x2} = a_4'e^{a_4}S^{x2x4}$. For $x7$ the pair $(x4, x7)$ is time-time (sign reversed) and $(x0, x7)$ a boost pair (deleted): $\Omega^{nb}_{x7} = -\omega_{x7\,x4x7}S^{x4x7} = -h_4s_bW\,S^{x4x7}$, while $\Omega_{x7} = h_4s_bW\,S^{x4x7} + HW\,S^{x0x7}$.

**Exercise 7 (the hidden operator in numbers).** Take $p = q = 1$ (constant functions) and integrate the identity of Section 6.24 over the half cell $0 \le x_0 \le \pi/(12H)$. Compare the left side with the boundary term for $c = \frac32H$ and for $c = 0$.

*Answer.* With $p = q = 1$, $A_c1 = c\cot z$, so the left side is $\int_0^{\pi/(12H)}W^3\cdot2c\cot z\,dx_0 = 2c\int_0^{\pi/(12H)}\cot(6Hx_0)\sin^{1/2}(6Hx_0)\,dx_0 = 2c\cdot\frac{1}{3H} = \frac{2c}{3H}$ (on the half cell $W^3 = \sin^{1/2}z$; the integral is the 7-volume integral of Chapter 3, Section 3.6; the constant factor $b_4^{3/2}$ is left out on both sides). The boundary term is $[W^3p\,q]_{z=0}^{z=\pi/2} = 1 - 0 = 1$ ($W = 1$ at the fold and $W = 0$ at the tip). For $c = \frac32H$ the left side is 1, equal to the boundary term: nothing else is left. For $c = 0$ it is 0, and the difference $0 - 1 = -1$ is the integral of the leftover $-3H\cot z\,W^3$, $-3H\cdot\frac{1}{3H} = -1$, which no boundary term can absorb. Note that the boundary term comes entirely from the fold, where the antisymmetry needs a boundary condition (Section 6.24).

**Exercise 8 (which pairs break).** Without a computer, explain why $D^{nb}_{x1}\gamma^{x2} = 0$ although $\Omega^{nb}_{x1} \neq \Omega_{x1}$, why the row $x4$ of figure 5 of Notebook 06c is white, and why the row $x0$ is not.

*Answer.* By Section 6.23, $D^{nb}_{x1}\gamma^{x2} = [\Omega^{nb}_{x1} - \Omega_{x1}, \gamma^{x2}] = -a_4'f_1[S^{x1x4}, \gamma^{(x2)}]/f_2$. By the vector rule $[S^{ab}, \gamma^c] = \eta^{bc}\gamma^a - \eta^{ac}\gamma^b$, which vanishes when $c$ is neither $a$ nor $b$; here $c = x2$ is neither $x1$ nor $x4$, so the commutator is zero. The row $x4$ is white because $\Omega_{x4} = 0$ (Section 6.6) and also $\Omega^{nb}_{x4} = 0$ (it is built from the same components, all zero for $\mu = x4$), so their difference vanishes and $D^{nb}_{x4}\gamma^\nu = D_{x4}\gamma^\nu = 0$ for every $\nu$. The row $x0$ is not white, because in the corrected metric $\Omega_{x0} = h_4s_b\cot z\,S^{x0x4} \neq 0$ comes from a boost pair, which the mixed contraction deletes: the difference $-h_4f_0S^{x0x4}$ breaks the constancy in the columns $x0$ and $x4$.
