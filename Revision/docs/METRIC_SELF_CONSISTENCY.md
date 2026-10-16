# The self-consistency of the primordial metric with diagonal sources

## The issue raised by the author on 2026-10-16, why the metric of 2026-10-14 is not self-consistent with diagonal sources, the corrected metric, its field equations and what it changes for the fields (version 2; the time-warped metric of version 1 is withdrawn)

## Abstract

A diagonal metric solves the Einstein (or Einstein-Lovelock) field equations $\sum_k \alpha_k E_{(k)}{}^\mu{}_\nu + \Lambda\,\delta^\mu_\nu = \kappa\,T^\mu{}_\nu$ only if every off-diagonal component of the left-hand side equals the corresponding component of the source. The author's notebook states the same as a warning: all off-diagonal source terms must vanish for the earlier solutions for $\Psi_{16}$ to be valid. Throughout, $x_0$ is the hidden coordinate, which is space-like, and $x_4$ is the time. The variable $z = 6Hx_0$ takes every real value, and the author's $\sin^{1/3}z$ means $(\sin^2 z)^{1/6}$, the positive branch. The corrected metric that this document proposes is

$$
\begin{aligned}
ds^2 = {} & e^{-2a_4}b_4\cot^2 z\,dx_0^2 + e^{2a_4}\big(dx_1^2 + dx_2^2 + dx_3^2\big) - dx_4^2 \\
& - e^{-2a_4}b_4\,(\sin^2 z)^{1/6}\big(dx_5^2 + dx_6^2 + dx_7^2\big) .
\end{aligned}
$$

This document records what the Revision computation found.

1. The metric of 2026-10-14 has, at every Lovelock order, the off-diagonal component $E_{(k)}{}^{x_4}{}_{x_0} \propto \cot z\,b_4'/b_4$. In Einstein gravity it is $\frac32 H\cot z\,b_4'/b_4$, so a diagonal source forces $b_4' = 0$.
2. Version 1 of this document removed that component with $g_{44} = -(\sin^2 z)^{1/6}$. That lapse oscillates along $x_0$ and vanishes at $z = n\pi$, so version 1 is withdrawn.
3. With $g_{44} = -1$ fixed, consider the family $g_{00} = b_4^{2p}e^{2qa_4}\cot^2 z$, $g_{ii} = e^{2a_4}(\sin^2 z)^{3\alpha}$, $g_{tt} = -e^{-2a_4}b_4(\sin^2 z)^{3\beta}$. The off-diagonal terms come from mixed curvature, proportional to $\alpha\big((q-1)a_4' + pu\big)$ for 3-space and to $\beta\big((q+1)a_4' + (p-\frac12)u\big)$ for the extra times, with $u = b_4'/b_4$. The author's two warps ($\alpha = \beta = 1/6$) cannot both be kept. The only member that keeps both, $g_{00} = b_4^{1/2}\cot^2 z$, makes the Einstein tensor diagonal but not the Gauss-Bonnet tensor.
4. The corrected metric (above) keeps the warp of the extra times and gives the hidden direction the scale factor of the extra times. It has no mixed Riemann component. Every off-diagonal component of the Einstein, Gauss-Bonnet and cubic Lovelock tensors vanishes identically, for all $a_4(x_4)$, $b_4(x_4) > 0$ and every real $z$. Every diagonal component is independent of $x_0$. Each of these statements is PROVED twice, with sympy and with Wolfram.
5. The block $(x_0, x_5, x_6, x_7)$ is $e^{-2a_4}b_4$ times a 4-dimensional space of constant curvature $-H^2$, so the hidden direction shrinks together with the deflating extra times.
6. The field equations are ordinary differential equations in $x_4$. The record's history $a_4 = Hx_4$, $b_4 = e^{(4/3)Hx_4}$ needs a diagonal, conserved source. That source has $p_0 = p_t$ and grows with the magnitude $H^2e^{2a_4}/b_4 = H^2e^{(2/3)Hx_4}$ of the curvature of the shrinking block.
7. The gravity term of the Dirac operator is $\frac32 He^{a_4}b_4^{-1/2}\gamma^{(x_0)} + (b_4'/b_4 - a_4'/2)\gamma^{(x_4)}$, independent of $x_0$.

The off-diagonal components of the energy-momentum tensor of the fields themselves (the spin-connection bilinears) remain a condition on the source. The recomputation of the field theory and of every primordial object for the corrected metric is OPEN.

## 1. The issue

### 1.1 The author's statement

On 2026-10-16 the author wrote: "a diagonal form for the metric of the primordial gravitational field is only self-consistent if all off-diagonal terms of all source terms in the Einstein field equations ARE ZERO. This is not the case here." The author's notebook `WaveFunctionUniverse-4+4-Einstein-Lovelock.nb` carries the same warning next to the sources of the metric. That notebook is a scratch notebook of the author. It was read to understand the issue, and none of its definitions or conventions is used in the Revision record. The warning says that the universe sources are to be added to the Einstein or Einstein-Lovelock field equations, and that all their off-diagonal terms must vanish for the diagonal metric, and the earlier solutions for $\Psi_{16}$, to be valid. The notebook uses the metric without $b_4$, the metric before 2026-10-14.

The order of 2026-10-16 asks for three things: the simplest modification of the metric that is probably self-consistent with the Einstein field equations, this document, and the recomputation of every primordial object of the record.

### 1.2 Coordinates and conventions

The coordinates are the author's $x_0, x_1, \dots, x_7$:

- $x_0$ is the hidden direction, a hypothetical space-like coordinate;
- $x_1, x_2, x_3$ are 3-space;
- $x_4$ is the time;
- $x_5, x_6, x_7$ are the three extra times, time-like and deflating.

$H > 0$ is the author's constant, and

$$
z = 6Hx_0,\qquad -\infty < z < \infty ,
$$

so $\sin z$ and $\cos z$ take both signs. The author's factor $\sin^{1/3}z$ means $(\sin^2 z)^{1/6} \ge 0$, the positive branch, which is what the author uses in their notebooks. Likewise $\sin^{1/6}z$ means $(\sin^2 z)^{1/12}$.

Every metric of this document is diagonal and depends on $x_0$ and $x_4$ only; we write $g_{ii}$ for $i = 1, 2, 3$ and $g_{tt}$ for $t = 5, 6, 7$. The Riemann tensor $R^a{}_{bcd}$ is in the sign convention of Misner, Thorne and Wheeler, with $R^{ab}{}_{cd} = g^{be}R^a{}_{ecd}$. The Lovelock tensors are

$$
E_{(k)}{}^h{}_j = -\frac{1}{2^{k+1}}\,\delta^{h h_1 \dots h_{2k}}_{j j_1 \dots j_{2k}}\,R^{j_1 j_2}{}_{h_1 h_2}\cdots R^{j_{2k-1} j_{2k}}{}_{h_{2k-1} h_{2k}} ,
$$

with the generalized Kronecker delta. $E_{(1)}$ is the Einstein tensor, $E_{(2)}$ the Gauss-Bonnet tensor and $E_{(3)}$ the cubic Lovelock tensor. The field equations are $\sum_{k=1}^{3}\alpha_k E_{(k)}{}^\mu{}_\nu + \Lambda\,\delta^\mu_\nu = \kappa\,T^\mu{}_\nu$, with the conventions of `Revision/field_equations_a4/a4-equations.json`. The author's weights are $\alpha_k = w_k/H^{2k}$ with $w = (1, 1/32, 1/1152)$. We write $a_4' = da_4/dx_4$ and $u = b_4'/b_4$.

Both programs of this record reduce every expression to an exact normal form that is valid for every real $z$:

- $\sin z$ and $\cos z$ keep their signs;
- $w = (\sin^2 z)^{1/12} > 0$;
- numerators and denominators are reduced modulo $\cos^2 z + \sin^2 z - 1$ and $w^{12} - \sin^2 z$.

No assumption on the sign of $\sin z$ or $\cos z$ is made. Version 1 restricted $z$ to $0 < z < \pi/2$; that restriction is withdrawn.

### 1.3 The author's rules for the remedy

The author added these rules on 2026-10-16:

- $x_0$ is space-like and $x_4$ is the time;
- $g_{44}$ cannot oscillate;
- $-\infty < z < \infty$;
- $\sin^{1/3}z = (\sin^2 z)^{1/6}$, the positive branch.

## 2. Where off-diagonal terms come from

### 2.1 The geometry

Write the diagonal metric as $g = \mathrm{diag}(\eta_{\mu\mu}f_\mu^2)$, with factors that depend on $x_0$ and $x_4$ only. Every Riemann component is then of the form $R^{ab}{}_{ab}$ (a sectional curvature), except the mixed components $R^{x_0 c}{}_{x_4 c}$ and $R^{x_4 c}{}_{x_0 c}$ with $c \notin \{x_0, x_4\}$. When the factors separate, $f_c = A_c(x_4)B_c(x_0)$, the mixed component is proportional to

$$
\partial_0\ln f_c\;\big(\partial_4\ln f_c - \partial_4\ln f_0\big) - \partial_4\ln f_c\;\partial_0\ln f_4 .
$$

The off-diagonal components of every Lovelock tensor are built from these mixed components, multiplied by sectional curvatures of the remaining directions. The only ones that can be nonzero are $E_{(k)}{}^{x_4}{}_{x_0}$ and $E_{(k)}{}^{x_0}{}_{x_4}$.

In the metric of 2026-10-14 the factors are:

- $f_0^2 = \cot^2 z$ and $f_4 = 1$, which do not depend on the other variable;
- $f_i = e^{a_4}(\sin^2 z)^{1/12}$ and $f_t = e^{-a_4}b_4^{1/2}(\sin^2 z)^{1/12}$, all six with $\partial_0\ln f_c = H\cot z$ for every real $z$.

The mixed component of a 3-space direction is proportional to $a_4'$, and that of an extra time to $-a_4' + u/2$. The Einstein tensor adds the six; the terms with $a_4'$ cancel and those with $u$ do not:

$$
E_{(1)}{}^{x_4}{}_{x_0} = \frac32\,H\cot z\,\frac{b_4'}{b_4} .
$$

The Gauss-Bonnet and cubic components are $\cot z\,u$ times polynomials in $a_4'$, $u$ and $H$. With the weights $\alpha_k$ the sum is $\cot z\,u\,Q$, with the record's factor $Q$. This is PROVED: the check `record_metric_offdiagonal_reproduced` reproduces `generalSource.offDiagonal_x4x0` of the record, frozen in `Revision/metric_warped/reference_2026_10_14/a4-offdiagonal-x4x0.json`, for every real $z$. A diagonal source therefore forces $u = 0$ in Einstein gravity. With the author's weights on the history $a_4 = Hx_4$ it allows only $d\ln b_4/da_4 \in \{0, 4/3\}$, the values where $Q = 0$.

### 2.2 The fields

In the record of the metric of 2026-10-14 (commit 04fa2e7: `Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md` and the textbook, chapter 9), the energy-momentum tensor of the fields has off-diagonal components of two kinds:

- Components with one index $x_0$ and one index $x_4$, $T^{x_4}{}_{x_0} = -\frac14(B_{40} - \cot z\,B_{04})$, built from derivatives along $x_0$ and $x_4$. They vanish for configurations that depend on $x_4$ only (check `commuting_T_x4x0_homogeneous`).
- Components produced by the spin connection, which drops out of the Lagrangian but not out of the tensor. An example is $K^{x_4}{}_{x_1} = \frac12 e^{a_4}\sin^{1/6}z\,H\,\bar\Phi\gamma^{(4)}\gamma^{(1)}\gamma^{(0)}\Phi$ for a configuration that depends on $x_4$ only (check `spin_connection_in_the_energy_momentum_tensor`). For a generic condensate, 42 of the 56 off-diagonal components are not zero; special condensates (the textbook's witnesses) make all of them vanish.

These components belong to the source. No diagonal metric removes them. A self-consistent diagonal metric needs a source whose off-diagonal components vanish; a source without this property needs a metric that is not diagonal in the corresponding directions.

### 2.3 What follows for the metric of 2026-10-14

- Einstein gravity: a diagonal source forces $b_4' = 0$, which the author excluded ("b4 is never 1").
- The author's weights: on the history $a_4 = Hx_4$ a diagonal source allows only one branch with $b_4$ not constant, namely $d\ln b_4/da_4 = 4/3$. Its source is the constant $\kappa(\rho, p_3, p_t, p_0) = (-2/27, -2/9, -22/27, -14/27)$. The check `condensate_cannot_source_branch` of the dark-sector record of that metric shows that no condensate can be that source.

The metric of 2026-10-14 is therefore self-consistent with diagonal sources only on one tuned branch of one theory. The remedy must remove the geometric off-diagonal term for every history, at every Lovelock order and for every real $z$, while keeping $g_{44} = -1$. The field's own off-diagonal terms remain a condition on the source.

## 3. The remedy: the corrected metric

### 3.1 Version 1 and why it is withdrawn

Version 1 of this document (commit 7897829) changed one entry, $g_{44} = -1 \to -\sin^{1/3}z$, so that all seven directions $x_1, \dots, x_7$ carried the same factor; that removed every off-diagonal term. It had three faults, which the author pointed out on 2026-10-16:

- Its text spoke of "the time direction, which may depend on $x_0$", as if $x_0$ were time-like. In fact $x_0$ is a hypothetical space-like coordinate and $x_4$ is the time.
- It used $z$ and the proper coordinate $y$ before defining them.
- It restricted $z$ to $0 < z < \pi/2$.

For real $z$, $g_{44} = -(\sin^2 z)^{1/6}$ is periodic in $x_0$ with period $\pi/(6H)$, equal to $-1$ at $z = \pi/2$ and to $0$ at $z = n\pi$. The lapse of the time would oscillate along the hidden direction and vanish periodically (check `version_1_g44_oscillates`), but $g_{44}$ cannot oscillate. Version 1 is withdrawn. Every metric below keeps $g_{44} = -1$.

### 3.2 The family with $g_{44} = -1$ and its conditions

With $g_{44} = -1$ we have $\partial_0\ln f_4 = 0$, and the mixed component of section 2.1 reduces to $\partial_0\ln f_c\,(\partial_4\ln f_c - \partial_4\ln f_0)$. It vanishes in two cases: the direction $c$ does not depend on $x_0$, or $f_c$ changes in $x_4$ at the rate of $f_0$. Consider the family

$$
g_{00} = b_4^{2p}e^{2qa_4}\cot^2 z,\qquad g_{ii} = e^{2a_4}(\sin^2 z)^{3\alpha},\qquad g_{44} = -1,\qquad g_{tt} = -e^{-2a_4}b_4\,(\sin^2 z)^{3\beta},
$$

with real $p$, $q$, $\alpha$, $\beta$. It contains the metric of 2026-10-14 ($p = q = 0$, $\alpha = \beta = 1/6$). For every real $z$ the only mixed components are

$$
\begin{aligned}
R^{x_0 x_i}{}_{x_4 x_i} &= 18H\tan z\,e^{-2qa_4}b_4^{-2p}\;\alpha\big((q-1)a_4' + p\,u\big), \\
R^{x_0 x_t}{}_{x_4 x_t} &= 18H\tan z\,e^{-2qa_4}b_4^{-2p}\;\beta\big((q+1)a_4' + (p - \tfrac12)\,u\big).
\end{aligned}
$$

This is PROVED with Wolfram (the exact factors) and with sympy (the proportionality), in the check `family_g44_fixed_conditions`. Both components vanish for all $a_4$, $b_4$ if and only if

$$
\big[\alpha = 0 \ \text{or}\ (q, p) = (1, 0)\big]\quad\text{and}\quad\big[\beta = 0 \ \text{or}\ (q, p) = (-1, \tfrac12)\big].
$$

So the author's two warps, $\alpha = \beta = 1/6$, cannot both be kept with vanishing mixed curvature. The Einstein tensor sees only the sum: $E_{(1)}{}^{x_4}{}_{x_0}$ is proportional to $\alpha\big((q-1)a_4' + pu\big) + \beta\big((q+1)a_4' + (p-\frac12)u\big)$ (check `family_einstein_condition`). With both warps it vanishes for all $a_4$, $b_4$ exactly when $q = 0$ and $p = 1/4$; section 3.6 shows that this member fails at the Gauss-Bonnet order.

### 3.3 The corrected metric

Keeping the warp of the extra times ($\beta = 1/6$) and dropping that of 3-space ($\alpha = 0$) gives $q = -1$, $p = 1/2$:

$$
\begin{aligned}
ds^2 = {} & e^{-2a_4}\,b_4\cot^2 z\,dx_0^2 + e^{2a_4}\big(dx_1^2 + dx_2^2 + dx_3^2\big) - dx_4^2 \\
& - e^{-2a_4}\,b_4\,(\sin^2 z)^{1/6}\big(dx_5^2 + dx_6^2 + dx_7^2\big) .
\end{aligned}
$$

This is the **corrected metric** of 2026-10-16. The functions $a_4(x_4)$ and $b_4(x_4) > 0$ are free.

- $g_{00} \ge 0$, $g_{ii} > 0$, $g_{44} = -1$ and $g_{tt} < 0$ for every real $z$. The signature is $(4,4)$ wherever $\sin z\cos z \neq 0$.
- As in the author's metric, $g_{00}$ vanishes where $\cos z = 0$ and $g_{tt}$ where $\sin z = 0$. The correction adds no new degenerate points; 3-space no longer has any.
- Compared with the metric of 2026-10-14, two entries change and the extra times stay as they were. In $g_{00} = \cot^2 z \to e^{-2a_4}b_4\cot^2 z$, the hidden direction gets the scale factor $e^{-a_4}b_4^{1/2}$ of the extra times. In $g_{ii}$, 3-space loses the factor $(\sin^2 z)^{1/6}$. $g_{44} = -1$ and $g_{tt}$ are unchanged.
- The diagonal vielbein is $f_0 = e^{-a_4}b_4^{1/2}\cot z$ (with its sign), $f_i = e^{a_4}$, $f_4 = 1$ and $f_t = e^{-a_4}b_4^{1/2}(\sin^2 z)^{1/12}$. The volume factor is $\sqrt{|g|} = e^{-a_4}b_4^2\,|\cot z|\,(\sin^2 z)^{1/4}$ (check `corrected_metric_entries`).
- $b_4$ enters the curvature through $H^2e^{2a_4}/b_4$ as well as through $u$. Its normalization $b_4(0)$ is therefore physical in the corrected metric; the record uses $b_4(0) = 1$.

### 3.4 The block of constant curvature

Wherever $\sin z \neq 0$, define the proper coordinate of the hidden direction

$$
y = \frac{\ln|\sin z|}{6H} \le 0,\qquad dy = \cot z\,dx_0,\qquad (\sin^2 z)^{1/6} = e^{2Hy} .
$$

$y$ is monotonic on each interval $n\pi/2 < z < (n+1)\pi/2$. Every statement of the record is made in $x_0$, for every real $z$. In $y$ the corrected metric reads

$$
ds^2 = -dx_4^2 + e^{2a_4}\big(dx_1^2+dx_2^2+dx_3^2\big) + e^{-2a_4}b_4\,\Big(dy^2 - e^{2Hy}\big(dx_5^2+dx_6^2+dx_7^2\big)\Big).
$$

The bracket is a 4-dimensional metric of signature $(1,3)$ with constant curvature $-H^2$. Check `hidden_block_constant_curvature` shows $R^{ab}{}_{ab} = -H^2$ for its six pairs and no other component, for every real $z$. The corrected metric is therefore a product over the time line with two fibers: flat 3-space with scale factor $e^{a_4}$, and this block with scale factor $e^{-a_4}b_4^{1/2}$. A warped product over a line has no curvature components that mix the line with a fiber (B. O'Neill, *Semi-Riemannian Geometry*, chapter 7), and with two fibers the same holds fiber by fiber. The block, being of constant curvature, has no mixed components of its own. The hidden direction shrinks together with the deflating extra times: on the record's history its proper size scales as $e^{-a_4}b_4^{1/2} = e^{-Hx_4/3}$.

### 3.5 Every off-diagonal component vanishes

In the corrected metric $\partial_0\ln f_i = 0$ and $\partial_4\ln f_t = \partial_4\ln f_0$, so the expression of section 2.1 vanishes for every $c$. There is no mixed Riemann component at all: check `corrected_mixed_riemann_vanish` finds 28 nonzero components, all of the form $R^{ab}{}_{ab}$. The off-diagonal components of every Lovelock tensor are built from mixed components, so all 56 off-diagonal components of $E_{(1)}$, $E_{(2)}$ and $E_{(3)}$ vanish identically, for all $a_4(x_4)$, $b_4(x_4) > 0$, $H$ and every real $z$. Every diagonal component is independent of $x_0$ (check `corrected_offdiagonal_all_orders`, sympy and Wolfram). For a diagonal source that depends on $x_4$ only, the field equations are therefore ordinary differential equations in $x_4$, at every Lovelock order.

### 3.6 The alternatives that were not chosen

- **Alternative K.** It keeps the warp of 3-space instead ($\alpha = 1/6$, $\beta = 0$, so $q = 1$, $p = 0$): $g_{00} = e^{2a_4}\cot^2 z$, $g_{ii} = e^{2a_4}(\sin^2 z)^{1/6}$, $g_{tt} = -e^{-2a_4}b_4$. It is diagonal at every order and free of $x_0$ on the diagonal (check `alternatives`). But the hidden direction would expand with 3-space, as $e^{a_4}$. The corrected metric keeps it shrinking with the extra times. The choice between the two is a physical one, and it is offered to the author.
- **The Einstein-only change.** The member $g_{00} = b_4^{1/2}\cot^2 z$ keeps both warps and makes the Einstein tensor diagonal. But its Gauss-Bonnet component is $E_{(2)}{}^{x_4}{}_{x_0} = -\frac32 H\cot z\,b_4'(4a_4'b_4 - b_4')^2/b_4^3 \neq 0$ (check `alternatives`). It is self-consistent with diagonal sources only for Einstein gravity.
- **A metric with off-diagonal entries.** Such a metric could absorb off-diagonal sources. The sources of section 2.2 have off-diagonal components in many directions: 3-space with time, 3-space with the extra times, and the hidden direction with the others. Absorbing them would need off-diagonal metric entries in all these directions and would give up the homogeneity and isotropy of 3-space and of the extra times. That is not a simple modification, and it is not pursued.

## 4. The field equations of the corrected metric

### 4.1 The Einstein tensor

The Ricci tensor is diagonal and independent of $x_0$ (check `ricci_tensor`, sympy and Wolfram). Write $C = H^2e^{2a_4}/b_4$; at each time the hidden block has the constant curvature $-C$. The Einstein tensor is

$$
\begin{aligned}
E_{(1)}{}^{x_4}{}_{x_4} &= 6C + 3a_4'^2 - \tfrac32 u^2, \\
E_{(1)}{}^{x_i}{}_{x_i} &= 6C - 5a_4'^2 + 6a_4'u + 2a_4'' - 2\frac{b_4''}{b_4} - \tfrac12 u^2, \\
E_{(1)}{}^{x_0}{}_{x_0} = E_{(1)}{}^{x_t}{}_{x_t} &= 3C - 3a_4'^2 + \tfrac32 a_4'u - \tfrac32\frac{b_4''}{b_4},
\end{aligned}
$$

and the Ricci scalar is $R = -12C + 8a_4'^2 - 2a_4'' - 8a_4'u + 4b_4''/b_4 + u^2$. These are the keys `einstein_diagonal` and `ricci_scalar_mathematica` of the results file `warped-metric.json`. The hidden direction and the extra times have equal components, because they form one block. The Gauss-Bonnet and cubic components are diagonal and independent of $x_0$ as well (section 3.5).

### 4.2 Conservation

For a diagonal tensor $T = \mathrm{diag}(p_0, p_3, p_3, p_3, -\rho, p_t, p_t, p_t)$ whose entries depend on $x_0$ and $x_4$, the corrected metric gives (check `divergence_of_diagonal_tensor`)

$$
\begin{aligned}
\nabla_\mu T^\mu{}_{x_4} &= -\partial_4\rho - 3a_4'(\rho + p_3) - 3h(\rho + p_t) - h(\rho + p_0),\qquad h = \frac{b_4'}{2b_4} - a_4', \\
\nabla_\mu T^\mu{}_{x_0} &= \partial_0 p_0 + 3H\cot z\,(p_0 - p_t),
\end{aligned}
$$

and the six other components vanish identically. Each expanding direction dilutes $\rho$ plus its own pressure, at the rate $a_4'$ for 3-space and $h$ for the block. For entries independent of $x_0$, the $x_0$ balance requires $p_0 = p_t$.

### 4.3 The record's history and its source

The Revision record uses the prescribed history $a_4 = AHx_4$, $b_4 = e^{\beta AHx_4}$ with $A = 1$, $\beta = 4/3$. On it the extra times and the hidden direction deflate as $e^{(\beta/2 - 1)a_4} = e^{-a_4/3}$. In the metric of 2026-10-14 this history was singled out by the off-diagonal condition $Q = 0$. In the corrected metric every history has a diagonal left-hand side, and the record keeps this one for continuity, as a prescribed background. For Einstein gravity its source $\kappa T - \Lambda\delta = E_{(1)}$ is

$$
\begin{aligned}
-\kappa\rho - \Lambda &= 6H^2e^{(2-\beta)AHx_4} - \tfrac32 A^2H^2(\beta^2 - 2), \\
\kappa p_3 - \Lambda &= 6H^2e^{(2-\beta)AHx_4} - \tfrac12 A^2H^2(5\beta^2 - 12\beta + 10), \\
\kappa p_0 - \Lambda = \kappa p_t - \Lambda &= 3H^2e^{(2-\beta)AHx_4} - \tfrac32 A^2H^2(\beta^2 - \beta + 2) .
\end{aligned}
$$

At $A = 1$, $\beta = 4/3$ it takes the values of the following table. This is the key `history_source` of `warped-metric.json`, reproduced by Wolfram in `history_source_equals_sympy`.

| left-hand side $E_{(1)}{}^\mu{}_\mu$ | Einstein gravity |
| --- | --- |
| $\mu = x_4$: $-\kappa\rho - \Lambda$ | $\frac13 H^2\big(18e^{2Hx_4/3} + 1\big)$ |
| $\mu = x_1, x_2, x_3$: $\kappa p_3 - \Lambda$ | $\frac19 H^2\big(54e^{2Hx_4/3} - 13\big)$ |
| $\mu = x_5, x_6, x_7$: $\kappa p_t - \Lambda$ | $\frac13 H^2\big(9e^{2Hx_4/3} - 11\big)$ |
| $\mu = x_0$: $\kappa p_0 - \Lambda$ | $\frac13 H^2\big(9e^{2Hx_4/3} - 11\big)$ |

With the author's weights the left-hand side is $\sum_k\alpha_kE_{(k)}{}^\mu{}_\mu$, and in the units of the weights it is

$$
\begin{aligned}
-\kappa\rho - \Lambda &= -\tfrac{9}{16}e^{4Hx_4/3} + \tfrac{161}{24}e^{2Hx_4/3} + \tfrac{121}{432}, \\
\kappa p_3 - \Lambda &= -\tfrac{9}{16}e^{4Hx_4/3} + \tfrac{1601}{216}e^{2Hx_4/3} - \tfrac{5359}{3888}, \\
\kappa p_0 - \Lambda = \kappa p_t - \Lambda &= \tfrac{79}{16}e^{2Hx_4/3} - \tfrac{497}{144} .
\end{aligned}
$$

Properties of this source:

- It is diagonal, isotropic in 3-space and in the extra times, and independent of $x_0$.
- It has $p_0 = p_t$, as section 4.2 requires.
- It satisfies $\nabla_\mu T^\mu{}_\nu = 0$ (check `history_source_conserved`).
- Unlike the source of version 1, it is not constant. It grows with the magnitude $C = H^2e^{(2-\beta)AHx_4}$ of the curvature of the shrinking block, and for $\beta = 2$, where the block does not shrink, it would be constant.

The history remains a PRESCRIBED background: no field of the record is shown to be its source.

### 4.4 A check with flat space

The choice $a_4 = 0$, $b_4 = H^2x_4^2$ makes every Riemann component of the corrected metric vanish (check `milne_flat_check`). This is 8-dimensional flat space in Milne form: the block of constant curvature $-H^2$, scaled by $Hx_4$. It is a consistency check of the formulas with $b_4$ not constant, not a physical history, since 3-space does not expand.

## 5. What the corrected metric changes for the fields

### 5.1 The vielbein, the volume and the gravity term

With the vielbein of section 3.3, the gravity term of the Dirac operator, $\gamma^\mu\Omega_\mu = \sum_a\gamma^{(a)}\frac{1}{2V}\partial_a\big(V/f_a\big)$ with $V = f_0 f_1\cdots f_7$, is

$$
\gamma^\mu\Omega_\mu = \frac32\,H\,e^{a_4}b_4^{-1/2}\,\gamma^{(x_0)} + \Big(\frac{b_4'}{b_4} - \frac{a_4'}{2}\Big)\gamma^{(x_4)}
$$

for every real $z$ (check `dirac_gravity_term`, sympy and Wolfram). In the metric of 2026-10-14 it was $3H\gamma^{(x_0)} + \frac34(b_4'/b_4)\gamma^{(x_4)}$. On the record's history it is $\frac32 He^{Hx_4/3}\gamma^{(x_0)} + \frac56 H\gamma^{(x_4)}$: the hidden coefficient grows as the hidden direction shrinks. The record proves, for every diagonal vielbein, that $\{\gamma^\mu, \Omega_\mu\} = 0$ holds for each direction separately, which still removes the spin connection from the Lagrangian.

### 5.2 Configurations that depend on $x_4$ only

Both coefficients of the gravity term, and the derivative term $\gamma^{(x_4)}\partial_4$, are independent of $x_0$. For a configuration $\Phi(x_4)$ the field equation is therefore an ordinary differential equation in $x_4$ for every mass $m$ and coupling $\lambda$; the obstruction that version 1 produced, with condensates only at $m = \pm\frac72 H$, does not arise. The solutions, the energy-momentum tensor and the quantisation are recomputed in the field-theory record. At this commit that recomputation is OPEN.

### 5.3 The field's own off-diagonal components

The spin connection of the corrected metric is not zero. For a diagonal vielbein, $\Omega_{x_c}$ is a sum of terms $\partial_b f_c/f_b\;\gamma^{(c)}\gamma^{(b)}$, and with the vielbein of section 3.3 (derived here; the field-theory record recomputes it):

- $\Omega_{x_i}$ is proportional to $a_4'\gamma^{(i)}\gamma^{(4)}$;
- $\Omega_{x_t}$ has a term in $\gamma^{(t)}\gamma^{(4)}$ and one in $\gamma^{(t)}\gamma^{(0)}$;
- $\Omega_{x_0}$ is proportional to $\gamma^{(0)}\gamma^{(4)}$;
- $\Omega_{x_4} = 0$, because $f_4 = 1$.

Its bilinears enter the energy-momentum tensor as in section 2.2. A self-consistent source must have vanishing off-diagonal components. This is a condition on the configurations of the fields, or on the quantum states whose expectation values are the source, and the recomputation of the field-theory record for the corrected metric states it component by component. At this commit that condition is OPEN for the corrected metric.

## 6. Consequences for the Revision record

The corrected metric replaces the metric of 2026-10-14 in `Revision/SPEC.md` section 1, following the author's order of 2026-10-16 to recompute all primordial objects. Everything that depends on the metric must be recomputed with it:

- the field theory of both fields: spin connection, field equation, energy-momentum tensor, conservation, exact solutions and quantisation;
- the field equations for $a_4$ and $b_4$: Lovelock tensors, sources and the history's source;
- the lead's checks;
- the generalized-Kronecker-delta record;
- the dark sector;
- the Kohn-Sham record, where the hidden direction now carries the factor $e^{-a_4}b_4^{1/2}$;
- the pairing theorems;
- the notebooks, the documents and the textbook.

The state at this commit:

- Only this record (`Revision/metric_warped/`) and this document use the corrected metric.
- The field-theory files of commit d02ff19 (`Revision/theory/wolfram/RevisionFieldTheory.wl` and `verify_field_theory.wls`) still use the withdrawn version 1.
- The other records still use the metric of 2026-10-14.

The author asked for the metric to be fixed first and for the repository to be repaired later. The metric of 2026-10-14 and its results remain in the repository as the earlier record, quoted only for comparison.

## 7. What is proved, computed, assumed and open

### 7.1 Proved (exact symbolic computation, twice: sympy and Wolfram, for every real $z$)

- The metric of 2026-10-14 has the off-diagonal pair $(x_4, x_0)$ at every Lovelock order, equal to the record's $\cot z\,u\,Q$.
- Version 1 ($g_{44} = -(\sin^2 z)^{1/6}$) has a lapse that oscillates along $x_0$.
- In the family of section 3.2 with $g_{44} = -1$ the mixed components are $18H\tan z\,e^{-2qa_4}b_4^{-2p}$ times $\alpha\big((q-1)a_4' + pu\big)$ and $\beta\big((q+1)a_4' + (p-\frac12)u\big)$. The Einstein condition with both warps is $q = 0$, $p = 1/4$.
- The corrected metric has no mixed Riemann component. Every off-diagonal component of $E_{(1)}$, $E_{(2)}$ and $E_{(3)}$ vanishes identically, and every diagonal component is independent of $x_0$. Its block $(x_0, x_5, x_6, x_7)$ has constant curvature $-H^2$.
- The Ricci tensor, the divergence of a diagonal tensor, the history's source and its conservation, the volume factor and the gravity term of the Dirac operator. The flat check is done with sympy.
- Alternative K is diagonal at every order. The Einstein-only change $g_{00} = b_4^{1/2}\cot^2 z$ has $E_{(2)}{}^{x_4}{}_{x_0} \neq 0$.

### 7.2 Computed

Nothing numerical: every statement of this document is an exact identity.

### 7.3 Assumed

- The history $a_4 = Hx_4$, $b_4 = b_4(0)e^{(4/3)Hx_4}$ with $b_4(0) = 1$ is a prescribed background, kept for continuity with the record. Its source is computed, not derived from a field.
- "Simplest" is understood as the smallest change within the family of section 3.2 ($g_{44} = -1$, the author's warp $(\sin^2 z)^{1/6}$, powers of $e^{a_4}$ and $b_4$ in $g_{00}$) that removes the mixed curvature for every history, and with it the off-diagonal terms at every order. The corrected metric changes two entries. No single-entry change with $g_{44} = -1$ in this family achieves it. By the Einstein condition of section 3.2, changing only $g_{ii}$ or only $g_{tt}$ cannot make the Einstein tensor diagonal. Changing only $g_{00}$ does so only for $g_{00} = b_4^{1/2}\cot^2 z$, which fails at the Gauss-Bonnet order. Members whose off-diagonal terms cancel without the mixed curvature vanishing, metrics with several functions of $x_0$, and metrics that are not diagonal are not exhausted.

### 7.4 Open

- The choice between the corrected metric (the hidden direction shrinks with the extra times) and alternative K (it expands with 3-space) is the author's.
- Which configurations of dirac16complex00, and which quantum states of dirac16complex, have an energy-momentum tensor without off-diagonal components in the corrected metric, and whether any of them can be the source of a history (section 5.3).
- The recomputation of every primordial object for the corrected metric (section 6).
- A history of the author's theory that is driven by the fields themselves.

## 8. Reproduction

Run from the repository root (each run stays below 60 s):

```text
python Revision/metric_warped/python/derive_warped_metric.py
wolframscript -file Revision/metric_warped/wolfram/verify_warped_metric.wls
python scripts/build_provenance_pdf.py Revision/docs/METRIC_SELF_CONSISTENCY.md \
    --developer-layout --specifications Revision/pdf-specifications.json
python -m unittest Revision/tests/test_metric_self_consistency_publication.py -v
```

| command | checks | time |
| --- | --- | --- |
| `derive_warped_metric.py` | 14 of 14 PASS | 16 s |
| `verify_warped_metric.wls` | 13 of 13 PASS | 37 s |
| `build_provenance_pdf.py` | the PDF build | 6 s |

The last lines of the two programs begin with `python_warped_metric=OK` and `wolfram_warped_metric=OK`. Two runs of each program give byte-identical outputs. The provenance of the record, with the sha256 of every input and output, is `Revision/metric_warped/WARPED_METRIC_PROVENANCE.md`.

## 9. Verification records

| report | checks |
| --- | --- |
| `Revision/metric_warped/reports/python-warped-metric-report.json` | 14 of 14 PASS |
| `Revision/metric_warped/reports/wolfram-warped-metric-report.json` | 13 of 13 PASS |

| check | sympy | Wolfram |
| --- | --- | --- |
| `corrected_metric_entries` | PASS | PASS |
| `record_metric_offdiagonal_reproduced` | PASS | PASS |
| `version_1_g44_oscillates` | PASS | PASS |
| `family_g44_fixed_conditions` | PASS | PASS |
| `family_einstein_condition` | PASS | PASS |
| `corrected_mixed_riemann_vanish` | PASS | PASS |
| `corrected_offdiagonal_all_orders` | PASS | PASS |
| `hidden_block_constant_curvature` | PASS | PASS |
| `ricci_tensor` | PASS | PASS |
| `divergence_of_diagonal_tensor` | PASS | PASS |
| `history_source_conserved` | PASS | |
| `history_source_equals_sympy` | | PASS |
| `dirac_gravity_term` | PASS | PASS |
| `milne_flat_check` | PASS | |
| `alternatives` | PASS | PASS |
