## 12. The field equations for a4: Einstein and Einstein-Lovelock

The author's metric contains exactly one unknown function, $a_4(x_4)$. This chapter derives, step by step, the equations that gravity imposes on that function: first by hand, as far as the algebra stays short, and then completely with four notebooks. We will find that the equations split into a constraint, an evolution equation, a hidden-direction equation and conditions on the matter; that no empty universe of this form exists; that the exponentially deflating history needs a source of a very unusual kind; that the equations do not care whether the extra times deflate or inflate; and that a condensate of the commuting field dirac16complex00 can be such a source exactly.

### 12.1 What this chapter does, and why

In Chapter 3 we met the author's metric: a rule that turns small steps $dx_1, \dots, dx_8$ into squared lengths. Three of its directions, $x_1, x_2, x_3$, are ordinary 3-space; $x_4$ is the time; $x_5, x_6, x_7$ are the three **extra times**, which behave like time; $x_8$ is the **hidden** space direction. Lengths along 3-space are multiplied by $e^{a_4}$ and lengths along the extra times by $e^{-a_4}$. When $a_4$ grows with the time $x_4$, 3-space inflates and the extra times **deflate exponentially**. That is the author's picture of the primordial universe.

A metric is not free. Einstein's great idea is that matter tells space how to curve: the curvature of the metric, collected into a tensor, equals a constant times the energy and momentum of the matter. The equations that say this are called the **field equations of gravity**. For the author's metric they become equations for the single function $a_4(x_4)$, and they answer questions such as:

- Can the author's metric exist with no matter at all? (No: Section 12.11.)
- If $a_4$ is given, what matter must be present? (The **required source**: Sections 12.8 to 12.12.)
- If the matter is given, how does $a_4$ evolve? (The evolution equation: Sections 12.9 and 12.21.)
- Do the equations prefer extra times that deflate? (No; deflation is a choice of sign: Section 12.12.)
- Can a field of this theory be the required source exactly, with the extra times deflating? (Yes, in three exact examples of the commuting field dirac16complex00, computed by this book: Section 12.26.)

We use the most general gravity theory that keeps the field equations of second order in eight dimensions, **Einstein-Lovelock gravity**, and its special case, Einstein gravity. Every formula comes from the Revision record (the folders `Revision/field_equations_a4`, `Revision/gkd_lovelock` and `Revision/lead_checks` of the repository) or from the book's own notebooks, which reproduce the record wherever the two overlap and say so in a PASS line. The four notebooks of the chapter are: Notebook 12a, which derives all the equations from the metric with exact computer algebra; Notebook 12b, which computes the source that the linear history $a_4 = AHx_4 + a_0$ requires; Notebook 12c, which integrates the evolution equation for prescribed sources; and Notebook 12d, which builds exact solutions of the coupled equations of gravity and of the field dirac16complex00, using the author's eight real 16 by 16 gamma matrices.

### 12.2 The words and symbols of this chapter

Each word below is defined in plain terms; the later sections make every definition precise with formulas.

- **Coordinates** $x_1, \dots, x_8$: the eight numbers that name a point, in the author's order. $x_1, x_2, x_3$: ordinary 3-space. $x_4$: the time. $x_5, x_6, x_7$: the three extra times (time-like, they deflate exponentially). $x_8$: the hidden direction. In the Python code the positions 0 to 7 of a list stand for $x_1$ to $x_8$; so position 3 is the time $x_4$ and position 7 the hidden $x_8$.
- **Hidden angle** $z = 6Hx_8$: the metric depends on $x_8$ only through $z$, which runs from $0$ to $\pi/2$ (the **patch**). $H > 0$ is a constant of the author's metric with the unit of an inverse length.
- **Prime**: $a_4' = da_4/dx_4$ and $a_4'' = d^2a_4/dx_4^2$. The code writes them as the symbols `ad1` and `ad2`.
- **Metric** $g_{\mu\nu}$: the table of numbers that turns coordinate steps into squared lengths, $ds^2 = \sum_{\mu,\nu} g_{\mu\nu}\,dx_\mu dx_\nu$. The author's metric is **diagonal**: only $g_{11}, g_{22}, \dots, g_{88}$ are not zero. Its inverse $g^{\mu\nu}$ is then diagonal too, with $g^{\mu\mu} = 1/g_{\mu\mu}$.
- **Signature**: the signs of the diagonal entries, here $(+,+,+,-,-,-,-,+)$: four space-like and four time-like directions, written (4,4).
- **Scale factor**: the number by which lengths along a direction are multiplied; for a diagonal metric it is $\sqrt{|g_{\mu\mu}|}$.
- **Index up, index down**: a tensor is a table of numbers labelled by indices; an upper index and a lower index transform in opposite ways. $T^\mu{}_\nu$ has one of each and is called **mixed**. The diagonal metric moves an index up or down by multiplying by $g^{\mu\mu}$ or $g_{\mu\mu}$.
- **Sum convention**: in this chapter a sum is always written out with $\sum$ or said in words, except in the definitions of Section 12.7 and in the formulas quoted from the record, where an index that appears once up and once down is summed over its eight values; "no sum" marks the exceptions.
- **Christoffel symbol** $\Gamma^a{}_{bc}$: a combination of first derivatives of the metric that says how the coordinate directions turn from point to point.
- **Riemann tensor** $R^{ab}{}_{mn}$: the curvature, built from the Christoffel symbols and their derivatives. **Pair curvature** $K_{ab} = R^{ab}{}_{ab}$ (no sum): the curvature of the plane spanned by the directions $a$ and $b$ (a name used in this chapter).
- **Ricci tensor** $R^h{}_j$, **Ricci scalar** $R$, **Einstein tensor** $G^h{}_j$: sums of Riemann components defined in Section 12.6.
- **Generalized Kronecker delta** (GKD): a sign, $+1$, $-1$ or $0$, attached to two lists of indices (Section 12.7). **Lovelock tensors** $E_{(1)}, E_{(2)}, E_{(3)}$: the three curvature tensors built with the GKD; $E_{(1)}$ is the Einstein tensor and $E_{(2)}$ the **Gauss-Bonnet** tensor.
- **Couplings**: $\alpha_1, \alpha_2, \alpha_3$ weigh the three Lovelock tensors; $\Lambda$ is the **cosmological constant**; $\kappa > 0$ measures the strength of gravity. **Einstein gravity**: $\alpha_1 = 1$, $\alpha_2 = \alpha_3 = 0$. **Einstein-Gauss-Bonnet gravity**: $\alpha_1 = 1$, $\alpha_3 = 0$.
- **Energy-momentum tensor** $T^\mu{}_\nu$, also called the **source**: the energy and momentum of the matter. Its parts are the **energy density** $\rho = -T^{x_4}{}_{x_4}$, the **pressures** $p_3$ (3-space), $p_t$ (extra times), $p_8$ (hidden direction), and the **mixed components** $q_{48} = T^{x_4}{}_{x_8}$ and $q_{84} = T^{x_8}{}_{x_4}$.
- **Anisotropic stress**: the difference $p_3 - p_t$ between the 3-space pressure and the extra-time pressure.
- **Equation of state** $w = p/\rho$: pressure divided by energy density.
- **Field equations**: the equations of gravity, $\sum_k \alpha_k E_{(k)}{}^\mu{}_\nu + \Lambda\delta^\mu_\nu = \kappa T^\mu{}_\nu$ (Section 12.8). Their four independent parts are the **constraint** (time, $x_4$), the 3-space equation, the extra-time equation and the **hidden equation** ($x_8$). The **evolution equation** is the 3-space equation minus the extra-time equation; the **algebraic condition** is $p_3 + p_t = 2p_8$.
- **Divergence** $\nabla_\mu T^\mu{}_\nu$: the curved-space form of "the change of a quantity in time plus its outflow"; zero divergence means **conservation**. The **Bianchi identity** says that the left-hand side of the field equations has zero divergence for every metric.
- **Vacuum**: no matter, $T^\mu{}_\nu = 0$.
- **Null vector**: a direction of zero length, such as the frame direction $x_4 + x_8$ (time-like plus space-like). The **null energy condition** along it is $\rho + p_8 \ge 0$; ordinary matter satisfies it. Matter with $\rho > 0$ and $w < -1$ violates it and is called **phantom**.
- **Linear member**: the history $a_4 = AHx_4 + a_0$ with a constant **slope** $A$. For $A > 0$ the extra times deflate as $e^{-AHx_4}$. The author's metric leaves $a_4(x_4)$ free, and the author requires only that the extra times deflate ($A > 0$); the **canonical history** $A = 1$ is the choice of the Revision record (ASSUMED, a prescribed background; Section 12.12).
- **Prescribed source**: a source chosen by hand to see what the equations do. It is ASSUMED, not derived from a field.
- **Condensate**: a solution of a field equation that depends on the time $x_4$ only.
- **Status labels**: PROVED (exact, with the verifier file and check name), COMPUTED (numerical, with its measured accuracy), ASSUMED, HYPOTHESIS, OPEN.

### 12.3 The author's metric, its determinant and the volume of seven directions

The author's metric is diagonal. With the abbreviation $s = \sin^{1/3} z$ and $z = 6Hx_8$ its eight diagonal entries are

$$
g = \mathrm{diag}\big(e^{2a_4}s,\ e^{2a_4}s,\ e^{2a_4}s,\ -1,\ -e^{-2a_4}s,\ -e^{-2a_4}s,\ -e^{-2a_4}s,\ \cot^2 z\big),
$$

in the order $x_1, \dots, x_8$ (record check `metric_is_SPEC_section_1` of `Revision/field_equations_a4/reports/wolfram-a4-report.json`). The scale factors are $\sqrt{|g_{11}|} = e^{a_4}\sin^{1/6}z$ for 3-space, $\sqrt{|g_{44}|} = 1$ for the time, $\sqrt{|g_{55}|} = e^{-a_4}\sin^{1/6}z$ for the extra times and $\sqrt{g_{88}} = \cot z$ for the hidden direction. When $a_4$ grows, the first grows and the third shrinks.

The **determinant** of the metric measures volume. We compute it line by line; after each line we name the rule that produced it.

$$
\det g = g_{11}\,g_{22}\,g_{33}\,g_{44}\,g_{55}\,g_{66}\,g_{77}\,g_{88}
$$

(the determinant of a diagonal matrix is the product of its diagonal entries)

$$
= \big(e^{2a_4}s\big)^3\cdot(-1)\cdot\big(-e^{-2a_4}s\big)^3\cdot\cot^2 z
$$

(the entries inserted; three equal factors written as a cube)

$$
= (-1)\,(-1)^3\; e^{6a_4}\,e^{-6a_4}\; s^6\,\cot^2 z
$$

(the power of a product is the product of the powers, $(xy)^3 = x^3y^3$, and $(e^{u})^3 = e^{3u}$)

$$
= s^6\cot^2 z
$$

($(-1)(-1)^3 = (-1)^4 = 1$ and $e^{6a_4}e^{-6a_4} = e^{0} = 1$)

$$
= \sin^2 z\,\cot^2 z = \cos^2 z
$$

($s^6 = (\sin^{1/3}z)^6 = \sin^2 z$, and $\cot z = \cos z/\sin z$). On the patch $0 < z < \pi/2$ the cosine is positive, so

$$
\sqrt{|\det g|} = \cos z .
$$

This is PROVED (record `Revision/field_equations_a4/reports/wolfram-a4-report.json`, check `sqrt_abs_det_g_is_cos_z`; reproduced in Notebook 12a, In [4]). The function $a_4$ has dropped out. The reason is visible in the fourth line: the volume factor $e^{3a_4}$ of the three inflating 3-space directions and the factor $e^{-3a_4}$ of the three deflating extra times multiply to 1. The volume of the seven directions other than the time stays constant: what 3-space gains, the extra times lose.

### 12.4 The Christoffel symbols of the author's metric

**Definition.** For any metric the Christoffel symbols are

$$
\Gamma^a{}_{bc} = \frac12\sum_{d=1}^{8} g^{ad}\big(\partial_b g_{dc} + \partial_c g_{db} - \partial_d g_{bc}\big),
$$

where $\partial_b$ is the partial derivative with respect to the coordinate $x_b$. They are symmetric in the two lower indices, $\Gamma^a{}_{bc} = \Gamma^a{}_{cb}$, because exchanging $b$ and $c$ exchanges the first two terms in the bracket.

**The formula for a diagonal metric.** We simplify the definition for our metric, line by line.

$$
\Gamma^a{}_{bc} = \frac{1}{2g_{aa}}\big(\partial_b g_{ac} + \partial_c g_{ab} - \partial_a g_{bc}\big)
$$

(the inverse metric is diagonal, so in the sum over $d$ only $d = a$ survives, and $g^{aa} = 1/g_{aa}$; no sum over $a$)

$$
\Gamma^a{}_{bc} = \frac{1}{2g_{aa}}\big(\delta_{ac}\,\partial_b g_{aa} + \delta_{ab}\,\partial_c g_{aa} - \delta_{bc}\,\partial_a g_{bb}\big)
$$

(an entry $g_{ac}$ of a diagonal matrix is $g_{aa}$ when $c = a$ and 0 otherwise; the Kronecker delta $\delta_{ac}$ is 1 when $a = c$ and 0 otherwise). This is the formula that Notebook 12a programs in In [5].

**The derivatives of the metric.** The metric depends on $x_4$ (through $a_4$) and on $x_8$ (through $z$) only; every other partial derivative is zero. By the chain rule $\partial_8 = (dz/dx_8)\,\partial_z = 6H\,\partial_z$. Then:

- $\partial_4 g_{11} = 2a_4'\,e^{2a_4}s = 2a_4'\,g_{11}$ (chain rule: the derivative of $e^{2a_4(x_4)}$ is $2a_4'e^{2a_4}$); the same for $g_{22}, g_{33}$.
- $\partial_4 g_{55} = -2a_4'\,g_{55}$ (the exponent is $-2a_4$); the same for $g_{66}, g_{77}$.
- $\partial_8 g_{11} = 6H\,e^{2a_4}\,\tfrac13\sin^{-2/3}z\,\cos z = 2H\cot z\; g_{11}$ (power rule for $\sin^{1/3}z$, then $\sin^{-2/3}z\cos z = \sin^{1/3}z\cdot\cos z/\sin z$); likewise $\partial_8 g_{55} = 2H\cot z\; g_{55}$.
- $\partial_8 g_{88} = 6H\cdot 2\cot z\cdot\big(-1/\sin^2 z\big) = -12H\cot z/\sin^2 z$ (chain rule, with $d\cot z/dz = -1/\sin^2 z$).
- $g_{44} = -1$ is constant.

**The symbols.** Inserting these into the diagonal formula:

- $\Gamma^{x_1}{}_{x_1x_4} = \partial_4 g_{11}/(2g_{11}) = a_4'$ (the term with $\delta_{ac}$, $a = c = x_1$, $b = x_4$).
- $\Gamma^{x_5}{}_{x_5x_4} = \partial_4 g_{55}/(2g_{55}) = -a_4'$: the same symbol with the opposite sign, because the extra times deflate where 3-space inflates.
- $\Gamma^{x_1}{}_{x_1x_8} = \Gamma^{x_5}{}_{x_5x_8} = 2H\cot z\,g_{11}/(2g_{11}) = H\cot z$ (sympy prints it as `H/tan(z)`).
- $\Gamma^{x_4}{}_{x_1x_1} = -\partial_4 g_{11}/(2g_{44}) = -2a_4'g_{11}/(-2) = a_4'\,e^{2a_4}\sin^{1/3}z$ (the term with $\delta_{bc}$, $b = c = x_1$, $a = x_4$).
- $\Gamma^{x_4}{}_{x_5x_5} = -\partial_4 g_{55}/(2g_{44}) = -a_4'\,g_{55} = a_4'\,e^{-2a_4}\sin^{1/3}z$.
- $\Gamma^{x_8}{}_{x_1x_1} = -\partial_8 g_{11}/(2g_{88}) = -H\tan z\;g_{11} = -H e^{2a_4}\sin^{4/3}z/\cos z$ (using $\cot z/\cot^2 z = \tan z = \sin z/\cos z$).
- $\Gamma^{x_8}{}_{x_5x_5} = -H\tan z\;g_{55} = H e^{-2a_4}\sin^{4/3}z/\cos z$.
- $\Gamma^{x_8}{}_{x_8x_8} = \partial_8 g_{88}/(2g_{88}) = -6H/(\sin z\cos z) = -12H/\sin 2z$ (using $\sin 2z = 2\sin z\cos z$).

The same holds with $x_1$ replaced by $x_2$ or $x_3$ and $x_5$ by $x_6$ or $x_7$. **Counting**: for each of the six directions $i \in \{x_1, x_2, x_3, x_5, x_6, x_7\}$ there are $\Gamma^i{}_{ix_4}$, $\Gamma^i{}_{x_4i}$, $\Gamma^i{}_{ix_8}$, $\Gamma^i{}_{x_8i}$, $\Gamma^{x_4}{}_{ii}$ and $\Gamma^{x_8}{}_{ii}$: $6 \times 6 = 36$ symbols, plus $\Gamma^{x_8}{}_{x_8x_8}$: 37 nonzero symbols of the 512, of which 25 are different. Every other symbol is zero; for example $\Gamma^{e}{}_{x_4x_4} = 0$ for every $e$, because $g_{44}$ is constant and no other entry has an index pair $(x_4, x_4)$. This is PROVED by Notebook 12a (In [5], checks "37 nonzero Christoffel symbols (25 distinct, 12 of them twice)" and the symmetry check; In [6] prints the 25 distinct symbols; the record computes the same symbols in `Revision/field_equations_a4/wolfram/FieldEquationsA4.wl`).

### 12.5 The curvature computed by hand

**Definition (the convention of Misner, Thorne and Wheeler, MTW).**

$$
R^a{}_{bmn} = \partial_m\Gamma^a{}_{bn} - \partial_n\Gamma^a{}_{bm} + \sum_{e}\Gamma^a{}_{me}\Gamma^e{}_{bn} - \sum_{e}\Gamma^a{}_{ne}\Gamma^e{}_{bm},
\qquad R^{ab}{}_{mn} = g^{bb}\,R^a{}_{bmn}\ \ (\text{no sum}).
$$

The tensor $R^{ab}{}_{mn}$ changes sign when $a$ and $b$ are exchanged, and when $m$ and $n$ are exchanged (record check `riemann_pair_antisymmetry`). So it is zero when $a = b$ or $m = n$, and the **pair curvature** $K_{ab} = R^{ab}{}_{ab}$ (no sum) is symmetric, $K_{ba} = R^{ba}{}_{ba} = (-1)(-1)R^{ab}{}_{ab} = K_{ab}$. The eight directions form $8 \cdot 7/2 = 28$ pairs. We compute four pair curvatures by hand.

**The pair (3-space direction, time).** Take $a = x_1$, $b = x_4$, $m = x_1$, $n = x_4$:

$$
R^{x_1}{}_{x_4x_1x_4} = \partial_1\Gamma^{x_1}{}_{x_4x_4} - \partial_4\Gamma^{x_1}{}_{x_4x_1} + \sum_e\Gamma^{x_1}{}_{x_1e}\Gamma^e{}_{x_4x_4} - \sum_e\Gamma^{x_1}{}_{x_4e}\Gamma^e{}_{x_4x_1}
$$

(the definition with these indices)

$$
= 0 - a_4'' + 0 - a_4'\cdot a_4'
$$

(nothing depends on $x_1$; $\Gamma^{x_1}{}_{x_4x_1} = a_4'$ has the derivative $a_4''$; every $\Gamma^e{}_{x_4x_4}$ is zero; in the last sum only $e = x_1$ survives, with $\Gamma^{x_1}{}_{x_4x_1} = a_4'$ twice)

$$
R^{x_1x_4}{}_{x_1x_4} = g^{44}\,R^{x_1}{}_{x_4x_1x_4} = (-1)\big(-a_4'' - (a_4')^2\big) = (a_4')^2 + a_4''
$$

(raise the index $x_4$ with $g^{44} = 1/g_{44} = -1$). The same steps with $\Gamma^{x_5}{}_{x_4x_5} = -a_4'$ give for an extra time and the time $K_{x_5x_4} = (a_4')^2 - a_4''$: the second derivative enters with the opposite sign.

**The pair (3-space direction, hidden direction).** With $a = m = x_1$ and $b = n = x_8$:

$$
R^{x_1}{}_{x_8x_1x_8} = \partial_1\Gamma^{x_1}{}_{x_8x_8} - \partial_8\Gamma^{x_1}{}_{x_8x_1} + \sum_e\Gamma^{x_1}{}_{x_1e}\Gamma^e{}_{x_8x_8} - \sum_e\Gamma^{x_1}{}_{x_8e}\Gamma^e{}_{x_8x_1}
$$

(the definition)

$$
= 0 - 6H\frac{d}{dz}\big(H\cot z\big) + \Gamma^{x_1}{}_{x_1x_8}\Gamma^{x_8}{}_{x_8x_8} - \Gamma^{x_1}{}_{x_8x_1}\Gamma^{x_1}{}_{x_8x_1}
$$

($\Gamma^{x_1}{}_{x_8x_8} = 0$; $\partial_8 = 6H\,d/dz$; of the $\Gamma^e{}_{x_8x_8}$ only $e = x_8$ is nonzero, and $\Gamma^{x_1}{}_{x_8e}$ is nonzero only for $e = x_1$)

$$
= \frac{6H^2}{\sin^2 z} + H\cot z\cdot\Big(-\frac{6H}{\sin z\cos z}\Big) - H^2\cot^2 z
$$

($d\cot z/dz = -1/\sin^2 z$, and the symbols of Section 12.4 inserted)

$$
= \frac{6H^2}{\sin^2 z} - \frac{6H^2}{\sin^2 z} - H^2\cot^2 z = -H^2\cot^2 z
$$

($\cot z/(\sin z\cos z) = 1/\sin^2 z$, because $\cot z = \cos z/\sin z$)

$$
K_{x_1x_8} = g^{88}\,R^{x_1}{}_{x_8x_1x_8} = \frac{1}{\cot^2 z}\big(-H^2\cot^2 z\big) = -H^2
$$

(raise $x_8$ with $g^{88} = 1/\cot^2 z$). The angle $z$ has disappeared: the curvature of this plane is the same constant $-H^2$ everywhere.

**Two 3-space directions.** With $a = m = x_1$, $b = n = x_2$ the two derivative terms vanish ($\Gamma^{x_1}{}_{x_2x_2} = \Gamma^{x_1}{}_{x_2x_1} = 0$), and so does the last sum (every $\Gamma^{x_1}{}_{x_2e}$ is zero):

$$
R^{x_1}{}_{x_2x_1x_2} = \Gamma^{x_1}{}_{x_1x_4}\Gamma^{x_4}{}_{x_2x_2} + \Gamma^{x_1}{}_{x_1x_8}\Gamma^{x_8}{}_{x_2x_2}
$$

(the two values of $e$ for which $\Gamma^{x_1}{}_{x_1e}$ is not zero)

$$
= a_4'\cdot a_4'\,g_{22} + H\cot z\cdot\big(-H\tan z\,g_{22}\big) = \big((a_4')^2 - H^2\big)\,g_{22}
$$

(the symbols of Section 12.4, and $\cot z\tan z = 1$), so $K_{x_1x_2} = g^{22}R^{x_1}{}_{x_2x_1x_2} = (a_4')^2 - H^2$.

**A 3-space direction and an extra time.** With $b = n = x_5$ the same two terms give $\Gamma^{x_1}{}_{x_1x_4}\Gamma^{x_4}{}_{x_5x_5} + \Gamma^{x_1}{}_{x_1x_8}\Gamma^{x_8}{}_{x_5x_5} = (a_4')^2e^{-2a_4}s + H^2e^{-2a_4}s$, and raising with $g^{55} = -e^{2a_4}/s$ gives $K_{x_1x_5} = -\big((a_4')^2 + H^2\big)$.

**All 28 pairs.** The computation of Notebook 12a (In [9]) confirms these values and gives the rest; the 28 pair curvatures fall into seven groups:

| the pair | number of pairs | pair curvature $K$ |
| --- | --- | --- |
| two 3-space directions | 3 | $(a_4')^2 - H^2$ |
| two extra times | 3 | $(a_4')^2 - H^2$ |
| a 3-space direction and an extra time | 9 | $-(a_4')^2 - H^2$ |
| a 3-space direction and the time | 3 | $(a_4')^2 + a_4''$ |
| an extra time and the time | 3 | $(a_4')^2 - a_4''$ |
| any of the six above directions and $x_8$ | 6 | $-H^2$ |
| the time and $x_8$ | 1 | $0$ |

Besides these 27 nonzero diagonal components there are 12 nonzero **off-diagonal** ones. They connect a pair that contains the time with the pair in which the time is replaced by $x_8$; for example

$$
R^{x_1x_4}{}_{x_1x_8} = R^{x_4x_5}{}_{x_5x_8} = Ha_4'\cot z,\qquad R^{x_1x_8}{}_{x_1x_4} = R^{x_5x_8}{}_{x_4x_5} = -\frac{Ha_4'}{\cot z} .
$$

Together: 39 nonzero components with $a < b$ and $m < n$, and $4 \times 39 = 156$ of the 4096 components $R^{ab}{}_{mn}$ (each one appears with its four orderings). Three facts follow: no component contains the warp factor $\sin^{1/3}z$ or $e^{a_4}$; every component is a polynomial in $H$, $a_4'$, $a_4''$ and $\cot z$, divided at most by $\cot z$; and the antisymmetries hold. All three are PROVED. The sympy report of the record, `Revision/field_equations_a4/reports/python-a4-report.json`, has the checks `mixed_riemann_free_of_warp_and_a4`, `riemann_entries_laurent` and `riemann_pair_antisymmetry`; the Wolfram report has `mixed_riemann_free_of_warp_and_a4` (whose detail includes the Laurent form in $\cot z$) and `riemann_pair_antisymmetry`; and Notebook 12a reproduces them in In [8].

### 12.6 The Ricci tensor, the Ricci scalar and the Einstein tensor by hand

**Definitions.**

$$
R^h{}_j = \sum_{a} R^{ah}{}_{aj},\qquad R = \sum_h R^h{}_h,\qquad G^h{}_j = R^h{}_j - \tfrac12\,\delta^h_j\,R .
$$

**A rule for the diagonal.** For $h = j$ the definition gives $R^h{}_h = \sum_a R^{ah}{}_{ah} = \sum_{a \ne h} K_{ah}$: the sum of the pair curvatures of the seven pairs that contain $h$. Summing over $h$ counts every pair twice (once from each of its two directions), so $R = 2\sum_{\text{pairs}} K$. Therefore

$$
G^h{}_h = \sum_{\text{pairs containing } h} K - \sum_{\text{all 28 pairs}} K = -\sum_{\text{pairs not containing } h} K ,
$$

(the definition of $G$ with the two sums inserted; the pairs that contain $h$ cancel). With the table of Section 12.5 everything follows by counting.

**The Ricci scalar.** Adding the seven groups, with their numbers of pairs:

$$
\sum_{\text{pairs}} K = 3\big((a_4')^2 - H^2\big) + 3\big((a_4')^2 - H^2\big) - 9\big((a_4')^2 + H^2\big) + 3\big((a_4')^2 + a_4''\big) + 3\big((a_4')^2 - a_4''\big) - 6H^2 + 0
$$

(the table, row by row)

$$
= (3 + 3 - 9 + 3 + 3)(a_4')^2 + (-3 - 3 - 9 - 6)H^2 + (3 - 3)a_4'' = 3(a_4')^2 - 21H^2
$$

(collect the terms with $(a_4')^2$, with $H^2$ and with $a_4''$), so $R = 6(a_4')^2 - 42H^2$, the RESULT line of Notebook 12a, In [11].

**The time component.** The pairs that do not contain $x_4$ are all rows of the table except the three rows with the time:

$$
G^{x_4}{}_{x_4} = -\Big[3\big((a_4')^2 - H^2\big) + 3\big((a_4')^2 - H^2\big) - 9\big((a_4')^2 + H^2\big) - 6H^2\Big]
$$

(the rule)

$$
= -\big[-3(a_4')^2 - 21H^2\big] = 3(a_4')^2 + 21H^2
$$

($3 + 3 - 9 = -3$ and $-3 - 3 - 9 - 6 = -21$).

**The hidden component.** The pairs without $x_8$ are the first five rows: $(3 + 3 - 9 + 3 + 3)(a_4')^2 + (-3 - 3 - 9)H^2 + (3 - 3)a_4'' = 3(a_4')^2 - 15H^2$, so $G^{x_8}{}_{x_8} = 15H^2 - 3(a_4')^2$.

**The 3-space component.** The pairs without $x_1$: one pair of two 3-space directions ($x_2x_3$), three of two extra times, six of a 3-space direction ($x_2$ or $x_3$) and an extra time, two of a 3-space direction and the time, three of an extra time and the time, five with $x_8$ (the six minus $x_1x_8$), and the time with $x_8$:

$$
\sum = (1 + 3 - 6 + 2 + 3)(a_4')^2 + (-1 - 3 - 6 - 5)H^2 + (2 - 3)a_4'' = 3(a_4')^2 - 15H^2 - a_4'',
$$

so $G^{x_1}{}_{x_1} = a_4'' - 3(a_4')^2 + 15H^2$. **The extra-time component** is found in the same way (three 3-space pairs, one extra-time pair, six mixed pairs, three space-time pairs, two extra-time-time pairs, five with $x_8$): $\sum = 3(a_4')^2 - 15H^2 + a_4''$ and $G^{x_5}{}_{x_5} = -a_4'' - 3(a_4')^2 + 15H^2$.

These four components are PROVED (record `Revision/field_equations_a4/reports/python-a4-report.json` and the Wolfram report, check `einstein_components`; reproduced in Notebook 12a, In [12]).

**Why the mixed component $G^{x_4}{}_{x_8}$ vanishes.** For $h = x_4$, $j = x_8$ the sum $R^{x_4}{}_{x_8} = \sum_a R^{ax_4}{}_{ax_8}$ picks up the off-diagonal Riemann components. For a 3-space direction, $R^{x_1x_4}{}_{x_1x_8} = Ha_4'\cot z$. For an extra time, $R^{x_5x_4}{}_{x_5x_8} = -R^{x_4x_5}{}_{x_5x_8} = -Ha_4'\cot z$ (exchange of the upper pair). So

$$
G^{x_4}{}_{x_8} = R^{x_4}{}_{x_8} = 3Ha_4'\cot z - 3Ha_4'\cot z = 0 .
$$

The three inflating 3-space directions and the three deflating extra times contribute equal and opposite amounts. The same happens for $G^{x_8}{}_{x_4}$, and every other off-diagonal component has no nonzero term at all. So the Einstein tensor is diagonal and does not depend on $x_8$ (PROVED: record `Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json`, checks `einstein_off_diagonal_zero`, `einstein_isotropy`, `einstein_x8_independent`; reproduced in Notebook 12a, In [12]).

### 12.7 The Lovelock tensors: the Einstein tensor and its two companions

**The generalized Kronecker delta.** For two lists of $n$ indices, $\delta^{h_1\dots h_n}_{j_1\dots j_n}$ is the determinant of the $n$ by $n$ matrix whose entry in row $r$ and column $c$ is the ordinary Kronecker delta $\delta^{h_r}_{j_c}$. Two equal upper indices give two equal rows and the determinant 0. Otherwise it is $+1$ if the lower list is an even rearrangement of the upper list (an even number of exchanges turns one into the other), $-1$ if it is an odd one, and $0$ if the two lists do not hold the same indices (Chapter 1 and Chapter 11 prove this).

**The Lovelock tensors** (formula (4.38) of the book by Lovelock and Rund, as programmed in the record, with a sum over every repeated index):

$$
P_{(k)}{}^h{}_j = \delta^{h\,h_1\dots h_{2k}}_{j\,j_1\dots j_{2k}}\;R^{j_1j_2}{}_{h_1h_2}\cdots R^{j_{2k-1}j_{2k}}{}_{h_{2k-1}h_{2k}},\qquad
E_{(k)}{}^h{}_j = -\frac{P_{(k)}{}^h{}_j}{2^{k+1}} .
$$

**Only $k = 1, 2, 3$.** For $k = 4$ the delta has $2k + 1 = 9$ upper indices taking only 8 values; two must be equal, so $P_{(4)} = 0$ (PROVED: Wolfram record, check `P4_vanishes_pigeonhole`; Notebook 12a, In [14]). In eight dimensions there are exactly three Lovelock tensors.

**$E_{(1)}$ is the Einstein tensor.** For $h = j$ the delta $\delta^{h\,h_1h_2}_{h\,j_1j_2}$ is not zero only when $h_1 \ne h_2$, both differ from $h$, and $\{j_1, j_2\} = \{h_1, h_2\}$. So only diagonal Riemann components enter:

$$
P_{(1)}{}^h{}_h = \sum_{h_1 \ne h_2;\ h_1, h_2 \ne h}\Big(\delta^{h\,h_1h_2}_{h\,h_1h_2}R^{h_1h_2}{}_{h_1h_2} + \delta^{h\,h_1h_2}_{h\,h_2h_1}R^{h_2h_1}{}_{h_1h_2}\Big)
$$

(the two possible orders of the lower indices)

$$
= \sum_{h_1 \ne h_2;\ h_1, h_2 \ne h}\big(K_{h_1h_2} + (-1)(-K_{h_1h_2})\big) = 4\sum_{\text{pairs not containing } h} K
$$

(one exchange gives the delta $-1$ and the Riemann component $-K$; each unordered pair appears twice as an ordered one). Hence $E_{(1)}{}^h{}_h = -P_{(1)}{}^h{}_h/4 = -\sum_{\text{pairs not containing } h}K = G^h{}_h$, the rule of Section 12.6. The record checks it in all 64 components (PROVED: Wolfram check `P1_direct_equals_minus_4_Einstein`, sympy check `P1_equals_minus_4_Einstein`; Notebook 12a, In [16]).

**$E_{(2)}$ and $E_{(3)}$.** For $k = 2, 3$ products of two or three Riemann components appear. Now the off-diagonal components also contribute: in a product such as $R^{x_1x_4}{}_{x_1x_8}\,R^{x_5x_8}{}_{x_4x_5}$ the factors $\cot z$ and $1/\cot z$ cancel. There are 690 contributing index lists for $k = 2$ and 4410 for $k = 3$ (Notebook 12a, In [15]); this bookkeeping is a job for the computer. The record's result, computed with the GKD in Rust (`Revision/gkd_lovelock/results/lovelock-tensors.json`), recomputed in Wolfram and in sympy, and reproduced by Notebook 12a in all 64 components of each tensor, is (record `Revision/field_equations_a4/a4-equations.json`, key `lovelockTensors`):

$$
\begin{aligned}
E_{(1)}{}^{x_1}{}_{x_1} &= -3 (a_4')^2+a_4''+15 H^2, \qquad E_{(1)}{}^{x_4}{}_{x_4} = 3 (a_4')^2+21 H^2, \\
E_{(1)}{}^{x_5}{}_{x_5} &= -3 (a_4')^2-a_4''+15 H^2, \qquad E_{(1)}{}^{x_8}{}_{x_8} = 15 H^2-3 (a_4')^2, \\
E_{(2)}{}^{x_1}{}_{x_1} &= 12 (a_4')^4-24 (a_4')^2 a_4''+168 (a_4')^2 H^2-40 a_4'' H^2-180 H^4, \\
E_{(2)}{}^{x_4}{}_{x_4} &= -36 (a_4')^4-120 (a_4')^2 H^2-420 H^4, \\
E_{(2)}{}^{x_5}{}_{x_5} &= 12 (a_4')^4+24 (a_4')^2 a_4''+168 (a_4')^2 H^2+40 a_4'' H^2-180 H^4, \\
E_{(2)}{}^{x_8}{}_{x_8} &= 12 (a_4')^4+168 (a_4')^2 H^2-180 H^4,
\end{aligned}
$$

$$
\begin{aligned}
E_{(3)}{}^{x_1}{}_{x_1} &= -72 (a_4')^6+360 (a_4')^4 a_4''-648 (a_4')^4 H^2+432 (a_4')^2 a_4'' H^2 \\
&\quad -1944 (a_4')^2 H^4+360 a_4'' H^4+360 H^6, \\
E_{(3)}{}^{x_4}{}_{x_4} &= 360 (a_4')^6+648 (a_4')^4 H^2+1080 (a_4')^2 H^4+2520 H^6, \\
E_{(3)}{}^{x_5}{}_{x_5} &= -72 (a_4')^6-360 (a_4')^4 a_4''-648 (a_4')^4 H^2-432 (a_4')^2 a_4'' H^2 \\
&\quad -1944 (a_4')^2 H^4-360 a_4'' H^4+360 H^6, \\
E_{(3)}{}^{x_8}{}_{x_8} &= -72 (a_4')^6-648 (a_4')^4 H^2-1944 (a_4')^2 H^4+360 H^6 ,
\end{aligned}
$$

with $x_2, x_3$ equal to $x_1$, $x_6, x_7$ equal to $x_5$, and every off-diagonal component zero. All of this is PROVED: the components computed from the curvature equal the Rust GKD record monomial by monomial (checks `P1_equals_gkd_branch_monomials` to `P3_equals_gkd_branch_monomials` of the sympy report and `P1_direct_equals_gkd_branch_monomials` to `P3_direct_equals_gkd_branch_monomials` of the Wolfram report); each $E_{(k)}$ is diagonal, free of $x_8$ and has zero divergence (checks `P1_structure` to `P3_structure` and `E1_divergence_free` to `E3_divergence_free` in both reports); and $E_{(2)}$ equals the classical Gauss-Bonnet tensor of Lanczos, which uses no GKD (Notebook 12a, In [18], for every $a_4$; for the linear member also record `Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json`, checks `gauss_bonnet_rho_alpha2` and `gauss_bonnet_p_alpha2`). That every divergence-free tensor built from the metric and its first and second derivatives is a combination of these tensors is Lovelock's theorem (D. Lovelock, J. Math. Phys. 12, 498 (1971)), which this book quotes and does not prove.

### 12.8 The source and the independent field equations

**The field equations of Einstein-Lovelock gravity** are

$$
\sum_{k=1}^{3}\alpha_k\,E_{(k)}{}^\mu{}_\nu + \Lambda\,\delta^\mu_\nu = \kappa\,T^\mu{}_\nu ,
$$

64 equations, one for each pair $(\mu, \nu)$. The left-hand side is built from the metric; the right-hand side is the source. We allow the most general source that the symmetry of the problem suggests:

$$
T^\mu{}_\nu = \mathrm{diag}\big(p_3, p_3, p_3, -\rho, p_t, p_t, p_t, p_8\big) + q_{48}\ (\mu = x_4, \nu = x_8) + q_{84}\ (\mu = x_8, \nu = x_4) .
$$

The minus sign in $T^{x_4}{}_{x_4} = -\rho$ comes from $g^{44} = -1$: the energy density is the component $T_{44}$ with both indices down, and raising the first index multiplies it by $g^{44}$ (the convention of the record; the pressures are $p_\mu = T^\mu{}_\mu$, no sum).

**Reduction.** Three facts of Section 12.7 reduce the 64 equations.

1. Every off-diagonal left-hand side is zero. So the off-diagonal equations read $0 = \kappa T^\mu{}_\nu$: the source must have $q_{48} = q_{84} = 0$ and no other mixed component.
2. The left-hand sides of $x_1, x_2, x_3$ are equal, and so are those of $x_5, x_6, x_7$. So the source must have one pressure for 3-space and one for the extra times, as assumed.
3. No left-hand side depends on $x_8$. So no part of the source may depend on $x_8$.

What remains are four equations. With the abbreviations $e_{hh} = \sum_k \alpha_k E_{(k)}{}^h{}_h$ (no $\Lambda$; Notebook 12a calls them `e11`, `e44`, `e55`, `e88`):

$$
\begin{aligned}
&\text{constraint } (x_4): & e_{44} + \Lambda &= -\kappa\rho, \\
&\text{3-space } (x_1 = x_2 = x_3): & e_{11} + \Lambda &= \kappa p_3, \\
&\text{extra times } (x_5 = x_6 = x_7): & e_{55} + \Lambda &= \kappa p_t, \\
&\text{hidden } (x_8): & e_{88} + \Lambda &= \kappa p_8 .
\end{aligned}
$$

This is PROVED (Wolfram record, check `independent_components`; sympy record, check `other_components_vanish`; reproduced in Notebook 12a, In [21]).

### 12.9 The constraint, the evolution equation and the algebraic condition

**Einstein gravity first.** With $\alpha_1 = 1$, $\alpha_2 = \alpha_3 = 0$ the four abbreviations are the Einstein components of Section 12.6:

$$
e_{44} = 3(a_4')^2 + 21H^2,\quad e_{11} = a_4'' - 3(a_4')^2 + 15H^2,\quad e_{55} = -a_4'' - 3(a_4')^2 + 15H^2,\quad e_{88} = 15H^2 - 3(a_4')^2 .
$$

The time and hidden components contain $a_4'$ but no $a_4''$: they are first-order equations. Subtracting the extra-time equation from the 3-space equation removes $\Lambda$:

$$
e_{11} - e_{55} = \kappa(p_3 - p_t)
$$

(3-space equation minus extra-time equation)

$$
\big(a_4'' - 3(a_4')^2 + 15H^2\big) - \big(-a_4'' - 3(a_4')^2 + 15H^2\big) = \kappa(p_3 - p_t)
$$

(the components inserted)

$$
2a_4'' = \kappa(p_3 - p_t)
$$

(the terms $-3(a_4')^2$ and $15H^2$ cancel). This is the **evolution equation**: the second derivative of $a_4$ is driven by the anisotropic stress, nothing else. Adding the two equations instead:

$$
e_{11} + e_{55} = 30H^2 - 6(a_4')^2 = 2\,e_{88}
$$

(the $a_4''$ cancel; $30H^2 - 6(a_4')^2 = 2(15H^2 - 3(a_4')^2)$), so the 3-space equation plus the extra-time equation minus twice the hidden equation reads $0 = \kappa(p_3 + p_t - 2p_8)$: the **algebraic condition** $p_3 + p_t = 2p_8$. It is not an equation for $a_4$ at all; it is a condition that every source must meet.

**Einstein-Lovelock gravity.** The same two combinations work for every coupling. From the components of Section 12.7, the Gauss-Bonnet part of $e_{11} - e_{55}$ is

$$
E_{(2)}{}^{x_1}{}_{x_1} - E_{(2)}{}^{x_5}{}_{x_5} = -48(a_4')^2a_4'' - 80H^2a_4'' = a_4''\big(-48(a_4')^2 - 80H^2\big)
$$

(the terms without $a_4''$ are equal in both and cancel; the others double), and the third-order part is $a_4''\big(720(a_4')^4 + 864(a_4')^2H^2 + 720H^4\big)$. So the evolution equation is

$$
a_4''\,F(a_4') = \kappa(p_3 - p_t),\qquad F = 2\alpha_1 - \alpha_2\big(48(a_4')^2 + 80H^2\big) + \alpha_3\big(720(a_4')^4 + 864(a_4')^2H^2 + 720H^4\big),
$$

and $e_{11} + e_{55} = 2e_{88}$ holds identically for each $k$ (check for $k = 2$: $2\cdot 12(a_4')^4 + 2\cdot 168(a_4')^2H^2 - 2\cdot 180H^4$ on both sides). All of this is PROVED; the checks are listed here:

| statement | sympy record | Wolfram record |
| --- | --- | --- |
| $e_{11} - e_{55} = a_4''F(a_4')$ | `evolution_factorises` | `evolution_factorises_a4pp_times_F` |
| $F$ is not identically zero | `evolution_F_not_identically_zero` | `evolution_F_not_identically_zero` |
| $e_{11} + e_{55} = 2e_{88}$ | `algebraic_identity` | `algebraic_identity_x1_plus_x5_minus_2x8` |
| no $a_4''$ in $e_{44}$ and $e_{88}$ | `constraint_and_x8_first_order` | `x8_component_contains_no_a4pp` |

Notebook 12a reproduces them in In [22] and In [23]. $F$ vanishes for every $a_4'$ and $H$ only when all three couplings are zero. But for Einstein-Gauss-Bonnet gravity with $\alpha_2 > 0$, $F = 2 - 80\alpha_2H^2 - 48\alpha_2(a_4')^2$ is zero at $(a_4')^2 = (1 - 40\alpha_2H^2)/(24\alpha_2)$; there the evolution equation cannot be solved for $a_4''$ (figure 4 of Notebook 12a; Section 12.21).

**What each equation does.** Given $a_4'$ at one time, the constraint fixes the energy density $\rho$ at that time, and the hidden equation fixes $p_8$. Given the anisotropic stress, the evolution equation fixes $a_4''$ and so the future of $a_4$. The algebraic condition then fixes $p_3$ and $p_t$ from $p_8$ and the stress: $p_3 = p_8 + \tfrac12(p_3 - p_t)$, $p_t = p_8 - \tfrac12(p_3 - p_t)$.

### 12.10 The Bianchi identity and the conservation law

**The identity.** Each Lovelock tensor has zero divergence for every metric (PROVED for the author's metric with an arbitrary $a_4$: record checks `E1_divergence_free`, `E2_divergence_free`, `E3_divergence_free` in both reports; Notebook 12a, In [19]). Since $\Lambda\delta^\mu_\nu$ has zero divergence too, the field equations can hold only if the source has zero divergence.

**The divergence of the general source.** We compute it for the source of Section 12.8, whose parts $\rho, p_3, p_t, p_8, q_{48}, q_{84}$ may now depend on $x_4$ and $x_8$, from the definition of the covariant divergence (Section 9.9):

$$
\nabla_\mu T^\mu{}_\nu = \sum_\mu\partial_\mu T^\mu{}_\nu + \sum_{\mu,\lambda}\Gamma^\mu{}_{\mu\lambda}\,T^\lambda{}_\nu - \sum_{\mu,\lambda}\Gamma^\lambda{}_{\mu\nu}\,T^\mu{}_\lambda .
$$

Two sums of Christoffel symbols are needed first. From the list of Section 12.4:

$$
\sum_\mu\Gamma^\mu{}_{\mu x_4} = 3a_4' + 3(-a_4') + 0 + 0 = 0
$$

(the three 3-space directions give $\Gamma^{x_1}{}_{x_1x_4} = a_4'$ each, the three extra times $\Gamma^{x_5}{}_{x_5x_4} = -a_4'$ each, and $\Gamma^{x_4}{}_{x_4x_4} = \Gamma^{x_8}{}_{x_8x_4} = 0$), and

$$
\sum_\mu\Gamma^\mu{}_{\mu x_8} = 6H\cot z - \frac{6H}{\sin z\cos z} = 6H\,\frac{\cos^2 z - 1}{\sin z\cos z} = -\frac{6H\sin z}{\cos z} = -6H\tan z
$$

(the six directions $x_1, x_2, x_3, x_5, x_6, x_7$ give $H\cot z$ each, $\Gamma^{x_8}{}_{x_8x_8} = -6H/(\sin z\cos z)$ and $\Gamma^{x_4}{}_{x_4x_8} = 0$; then the common denominator $\sin z\cos z$, with $\cot z = \cos^2 z/(\sin z\cos z)$, and $\cos^2 z - 1 = -\sin^2 z$). This is $\partial_8\ln\cos z = 6H\cdot(-\sin z/\cos z)$, the logarithmic derivative of $\sqrt{|\det g|} = \cos z$ (Section 12.3), as the lemma of Section 9.9 says.

**The component $\nu = x_4$.** The column $T^\lambda{}_{x_4}$ has only the entries $T^{x_4}{}_{x_4} = -\rho$ and $T^{x_8}{}_{x_4} = q_{84}$, and the entries $T^\mu{}_\lambda$ that are not zero are the eight diagonal ones and the two mixed ones $T^{x_4}{}_{x_8} = q_{48}$, $T^{x_8}{}_{x_4} = q_{84}$. So the three sums of the definition become

$$
\begin{aligned}
\nabla_\mu T^\mu{}_{x_4} &= \partial_4 T^{x_4}{}_{x_4} + \partial_8 T^{x_8}{}_{x_4} + \Big(\sum_\mu\Gamma^\mu{}_{\mu x_4}\Big)T^{x_4}{}_{x_4} + \Big(\sum_\mu\Gamma^\mu{}_{\mu x_8}\Big)T^{x_8}{}_{x_4} \\
&\quad - \sum_\mu\Gamma^\mu{}_{\mu x_4}T^\mu{}_\mu - \Gamma^{x_8}{}_{x_4x_4}T^{x_4}{}_{x_8} - \Gamma^{x_4}{}_{x_8x_4}T^{x_8}{}_{x_4}
\end{aligned}
$$

(the definition with $\nu = x_4$, keeping only the nonzero entries of $T$; in the next-to-last sum the diagonal entry $T^\mu{}_\mu$ has $\lambda = \mu$)

$$
= -\partial_4\rho + \partial_8 q_{84} + 0 - 6H\tan z\,q_{84} - \big(3a_4'\,p_3 - 3a_4'\,p_t\big) - 0 - 0
$$

(the entries inserted; the two sums of symbols above; on the diagonal $\Gamma^{x_1}{}_{x_1x_4} = a_4'$ multiplies $p_3$ three times and $\Gamma^{x_5}{}_{x_5x_4} = -a_4'$ multiplies $p_t$ three times, while $\Gamma^{x_4}{}_{x_4x_4} = \Gamma^{x_8}{}_{x_8x_4} = 0$; and $\Gamma^{x_8}{}_{x_4x_4} = \Gamma^{x_4}{}_{x_8x_4} = 0$ by Section 12.4)

$$
= -\partial_4\rho - 3a_4'(p_3 - p_t) + \partial_8 q_{84} - 6H\tan z\,q_{84}
$$

(the terms reordered and $3a_4'$ taken out of the bracket).

**The component $\nu = x_8$.** In the same way, with the column $T^{x_4}{}_{x_8} = q_{48}$, $T^{x_8}{}_{x_8} = p_8$:

$$
\begin{aligned}
\nabla_\mu T^\mu{}_{x_8} &= \partial_4 T^{x_4}{}_{x_8} + \partial_8 T^{x_8}{}_{x_8} + \Big(\sum_\mu\Gamma^\mu{}_{\mu x_4}\Big)T^{x_4}{}_{x_8} + \Big(\sum_\mu\Gamma^\mu{}_{\mu x_8}\Big)T^{x_8}{}_{x_8} \\
&\quad - \sum_\mu\Gamma^\mu{}_{\mu x_8}T^\mu{}_\mu - \Gamma^{x_8}{}_{x_4x_8}T^{x_4}{}_{x_8} - \Gamma^{x_4}{}_{x_8x_8}T^{x_8}{}_{x_4}
\end{aligned}
$$

(the definition with $\nu = x_8$, keeping only the nonzero entries of $T$)

$$
= \partial_4 q_{48} + \partial_8 p_8 + 0 - 6H\tan z\,p_8 - \Big(3H\cot z\,p_3 + 3H\cot z\,p_t - \frac{6H}{\sin z\cos z}\,p_8\Big) - 0 - 0
$$

(the entries inserted; on the diagonal the six directions give $H\cot z$ times their pressure, $\Gamma^{x_4}{}_{x_4x_8} = 0$, and $\Gamma^{x_8}{}_{x_8x_8} = -6H/(\sin z\cos z)$ multiplies $p_8$; $\Gamma^{x_8}{}_{x_4x_8} = 0$ because $g_{88}$ does not depend on $x_4$, and $\Gamma^{x_4}{}_{x_8x_8} = -\partial_4 g_{88}/(2g_{44}) = 0$ for the same reason)

$$
= \partial_8 p_8 + \Big(\frac{6H}{\sin z\cos z} - \frac{6H\sin z}{\cos z}\Big)p_8 - 3H\cot z\,(p_3 + p_t) + \partial_4 q_{48}
$$

(the two terms with $p_8$ collected, $\tan z = \sin z/\cos z$)

$$
\begin{aligned}
&= \partial_8 p_8 + 6H\cot z\,p_8 - 3H\cot z\,(p_3 + p_t) + \partial_4 q_{48} \\
&= \partial_8 p_8 + 3H\cot z\,(2p_8 - p_3 - p_t) + \partial_4 q_{48}
\end{aligned}
$$

($\frac{6H}{\sin z\cos z} - \frac{6H\sin^2 z}{\sin z\cos z} = 6H\,\frac{1 - \sin^2 z}{\sin z\cos z} = 6H\,\frac{\cos z}{\sin z}$; then $3H\cot z$ taken out).

**The six other components.** For $\nu = x_1$ every term is zero: the column $T^\lambda{}_{x_1}$ has only $T^{x_1}{}_{x_1} = p_3$, which does not depend on $x_1$; $\sum_\mu\Gamma^\mu{}_{\mu x_1} = 0$, because no entry of the metric depends on $x_1$; and every symbol $\Gamma^\lambda{}_{\mu x_1}$ that multiplies a nonzero entry $T^\mu{}_\lambda$ is zero ($\Gamma^{x_1}{}_{x_1x_1} = 0$, and none of the nonzero symbols of Section 12.4 has exactly one index equal to $x_1$). The same holds for $x_2, x_3, x_5, x_6, x_7$.

These are the record's formulas (PROVED: record `Revision/lead_checks/reports/emt-divergence-and-spin-connection.json`, checks `divergence_x4_component`, `divergence_x8_component` and `divergence_other_components_zero`; Notebook 12a, In [25], which reproduces the first two of them and the sympy record's check `conservation_components`):

$$
\begin{aligned}
\nabla_\mu T^\mu{}_{x_4} &= -\partial_4\rho - 3a_4'(p_3 - p_t) + \partial_8 q_{84} - 6H\tan z\,q_{84}, \\
\nabla_\mu T^\mu{}_{x_8} &= \partial_8 p_8 + 3H\cot z\,(2p_8 - p_3 - p_t) + \partial_4 q_{48},
\end{aligned}
$$

and zero for the six other components. With the conditions of Section 12.8 (no $x_8$ dependence, $q_{48} = q_{84} = 0$) the first says $\rho' = -3a_4'(p_3 - p_t)$ and the second repeats the algebraic condition.

**The constraint propagates.** In Einstein gravity we can see directly why the constraint stays true along a solution:

$$
-\kappa\rho = 3(a_4')^2 + 21H^2 + \Lambda
$$

(the constraint)

$$
-\kappa\rho' = 6a_4'a_4''
$$

(differentiate with respect to $x_4$: chain rule for $(a_4')^2$; $H$ and $\Lambda$ are constants)

$$
-\kappa\rho' = 3a_4'\cdot 2a_4'' = 3a_4'\,\kappa(p_3 - p_t)
$$

(the evolution equation $2a_4'' = \kappa(p_3 - p_t)$ inserted)

$$
\rho' = -3a_4'(p_3 - p_t)
$$

(divided by $-\kappa$). So the constraint, differentiated, is $3a_4'$ times the evolution equation, exactly when the source obeys the conservation law. The record proves the same for every coupling, $\tfrac{d}{dx_4}e_{44} = 3a_4'(e_{11} - e_{55})$ (checks `constraint_propagation_bianchi` and `bianchi_x4`; Notebook 12a, In [23]). For the Gauss-Bonnet part, for example, $\tfrac{d}{dx_4}\big(-36(a_4')^4 - 120(a_4')^2H^2\big) = -144(a_4')^3a_4'' - 240a_4'a_4''H^2 = 3a_4'\cdot a_4''\big(-48(a_4')^2 - 80H^2\big)$.

**What the conservation law means.** The law $\rho' = -3a_4'(p_3 - p_t)$ is the first law of thermodynamics, $dE = -p\,dV$, for the two kinds of directions. The total volume of the seven directions other than the time is constant (Section 12.3), so the energy density can change only through the work of the pressures. The volume of 3-space grows like $e^{3a_4}$, so its logarithm grows at the rate $3a_4'$, and the pressure $p_3$ contributes $-3a_4'p_3$ per unit volume and time. The volume of the extra times shrinks like $e^{-3a_4}$, at the rate $-3a_4'$, and the pressure $p_t$ contributes $+3a_4'p_t$. The total is $-3a_4'(p_3 - p_t)$: energy flows between 3-space and the extra times, and the energy density stays constant when the two pressures are equal. (This reading is an interpretation of the PROVED identity.)

### 12.11 Einstein gravity: no empty universe, and the null energy condition along x8

In Einstein gravity the constraint and the hidden equation read

$$
3(a_4')^2 + 21H^2 + \Lambda = -\kappa\rho,\qquad -3(a_4')^2 + 15H^2 + \Lambda = \kappa p_8 .
$$

**The null energy condition fails.** Subtracting the first from the second:

$$
\big(-3(a_4')^2 + 15H^2 + \Lambda\big) - \big(3(a_4')^2 + 21H^2 + \Lambda\big) = \kappa p_8 + \kappa\rho
$$

(second equation minus first)

$$
\kappa(\rho + p_8) = -6(a_4')^2 - 6H^2 = -6\big((a_4')^2 + H^2\big)
$$

($\Lambda$ cancels; $15 - 21 = -6$). For $H > 0$ the right-hand side is negative for every $a_4$ and every $\Lambda$, so $\rho + p_8 < 0$ (with $\kappa > 0$). In the frame of the vielbein (the directions of unit length of Chapter 6) the energy-momentum tensor has $T_{\hat4\hat4} = \rho$ and $T_{\hat8\hat8} = p_8$, and the vector $k$ with frame components $k^{\hat4} = k^{\hat8} = 1$ (all others 0) has zero length, $\eta(k,k) = -1 + 1 = 0$: a **null vector**. Then $T(k, k) = T_{\hat4\hat4} + 2T_{\hat4\hat8} + T_{\hat8\hat8} = \rho + 0 + p_8$. Every source of the author's metric in Einstein gravity violates the null energy condition along this null direction (PROVED: sympy and Wolfram records, check `einstein_null_energy_x8`; Notebook 12a, In [26]).

**No vacuum.** A vacuum needs $\rho = p_8 = 0$, so $6\big((a_4')^2 + H^2\big) = 0$, which no real $a_4'$ satisfies when $H > 0$. If one allows complex numbers, the vacuum equations have exactly the two solutions $a_4' = \pm iH$, $\Lambda = -18H^2$ (from $(a_4')^2 = -H^2$ and $\Lambda = 3(a_4')^2 - 15H^2$), which are not real histories (PROVED: Wolfram record, check `einstein_no_vacuum_solution`; lead's record `Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json`, check `no_vacuum_for_H_positive`; Notebook 12a, In [26] and figure 5). The author's metric is never empty space: it always needs matter, and that matter is of an unusual kind.

**Every coupling.** For Einstein-Lovelock gravity the same combination factorises: $\kappa(\rho + p_8) = -6\big((a_4')^2 + H^2\big)\,V$, with $V = \alpha_1 - 8\alpha_2\big((a_4')^2 + 5H^2\big) + \alpha_3\big(72(a_4')^4 + 144(a_4')^2H^2 + 360H^4\big)$ (PROVED by Notebook 12a, In [29], from the record's components). The null energy condition can hold only where $V \le 0$, and a vacuum needs $V = 0$. With the Einstein term at its usual weight, $\alpha_1 = 1$, this needs Lovelock couplings beyond Einstein's. The bracket $8\big((a_4')^2 + 5H^2\big)$ that multiplies $-\alpha_2$ and the bracket $72(a_4')^4 + 144(a_4')^2H^2 + 360H^4$ that multiplies $\alpha_3$ are both positive, so $V \le 0$ needs a positive Gauss-Bonnet coupling $\alpha_2$ or a negative third-order coupling $\alpha_3$, large enough. For example, with $\alpha_3 = 0$:

$$
V \le 0 \iff 1 \le 8\alpha_2\big((a_4')^2 + 5H^2\big) \iff \alpha_2 \ge \frac{1}{8\big((a_4')^2 + 5H^2\big)}
$$

(the definition of $V$ with $\alpha_1 = 1$ and $\alpha_3 = 0$; then division by the positive bracket). With $\alpha_2 = 0$, at a moment where $a_4' = 0$: $V = 1 + 360\alpha_3H^4 \le 0$ exactly when $\alpha_3H^4 \le -1/360$; for instance $\alpha_3H^4 = -1/300$ gives $V = 1 - 360/300 = -0.2$.

### 12.12 The linear member: the extra times deflate by a choice of sign

**The history.** The simplest history is $a_4 = AHx_4 + a_0$ with constants $A$ and $a_0$. Then $a_4' = AH$ and $a_4'' = 0$, the 3-space scale factor grows like $e^{AHx_4}$ and the extra-time scale factor shrinks like $e^{-AHx_4}$: for $A > 0$ the extra times deflate exponentially, at the rate $AH$. The author's metric does not fix the slope: the author requires only that the extra times deflate, $A > 0$. The Revision record takes $A = 1$ as its canonical history (ASSUMED, a prescribed background: the record `Revision/kohn_sham/results/parameters.json` writes "a4 = A H x4 (A = 1 canonical)" and calls it a PRESCRIBED BACKGROUND); this chapter calls $A = 1$ the **canonical history**.

**The source it requires.** Line by line:

- evolution equation with $a_4'' = 0$: $0 = \kappa(p_3 - p_t)$, so $p_3 = p_t$;
- algebraic condition: $p_3 + p_t = 2p_8$ with $p_3 = p_t$ gives $p_8 = p_3$; so all three pressures are equal, $p_3 = p_t = p_8 =: p$;
- constraint and hidden equation with $a_4' = AH$ give constant $\rho$ and $p$.

In Einstein gravity:

$$
\kappa\rho = -(21 + 3A^2)H^2 - \Lambda,\qquad \kappa p = (15 - 3A^2)H^2 + \Lambda,\qquad \kappa(\rho + p) = -6(1 + A^2)H^2 .
$$

For all three couplings the record's formulas are (PROVED: record checks `linear_member_equal_pressures` and `json_linear_member`; Notebook 12a, In [28], and Notebook 12b, In [3] to In [5]):

$$
\begin{aligned}
\kappa\rho &= \alpha_1(-3A^2 - 21)H^2 + \alpha_2(36A^4 + 120A^2 + 420)H^4 \\
&\quad + \alpha_3(-360A^6 - 648A^4 - 1080A^2 - 2520)H^6 - \Lambda, \\
\kappa p &= \alpha_1(15 - 3A^2)H^2 + \alpha_2(12A^4 + 168A^2 - 180)H^4 \\
&\quad + \alpha_3(-72A^6 - 648A^4 - 1944A^2 + 360)H^6 + \Lambda .
\end{aligned}
$$

**Deflation is a choice of sign.** The slope enters only as $A^2$, $A^4$ and $A^6$. Replacing $A$ by $-A$ changes nothing: the equations accept extra times that deflate ($A > 0$) and extra times that inflate ($A < 0$) on exactly the same footing, and $A = 0$ (a static metric) as well. That the author's extra times deflate is a choice of sign, an initial condition; it is not a consequence of the field equations (PROVED: Notebook 12a, In [28], and Notebook 12b, In [4]; record key `theoremLinear` of `Revision/field_equations_a4/a4-equations.json`). This symmetry relates two histories of the metric of one universe. It is not the pairing of universes of masses $+m$ and $-m$, which is the subject of Chapters 18 to 20, and it says nothing about how a universe could be created.

**The canonical history in numbers.** For $A = 1$ and $\Lambda = 0$ (units $H = \kappa = 1$): $\kappa\rho = -24$, $\kappa p = 12$, $w = p/\rho = -1/2$ (Notebook 12b, In [5]). The energy density is negative. A positive energy density needs $-(21 + 3A^2)H^2 - \Lambda > 0$, that is $\Lambda < -(21 + 3A^2)H^2$, and then:

$$
\kappa(\rho + p) = -6(1 + A^2)H^2 < 0 \;\Rightarrow\; p < -\rho \;\Rightarrow\; \frac{p}{\rho} < -1
$$

(the sum of the two formulas; then divide by $\rho > 0$, which keeps the direction of the inequality). A positive energy density comes only with $w < -1$: the source is phantom (PROVED: Notebook 12b, In [8], checks for $\Lambda = -30H^2$, $-40H^2$, $-60H^2$ and the identity $w + 1 = (\rho + p)/\rho$).

**The Gauss-Bonnet vacuum.** With $\alpha_1 = 1$, $\alpha_3 = 0$ the record factorises $\kappa(\rho + p) = -6(A^2 + 1)H^2\,V$ with $V = 1 - 8\alpha_2H^2(A^2 + 5)$ (record checks `linear_member_vacuum_factor`, `einstein_gauss_bonnet_vacuum_linear`). A vacuum needs $V = 0$, that is

$$
A^2 = \frac{1 - 40\alpha_2H^2}{8\alpha_2H^2},
$$

a real slope only for $0 < \alpha_2H^2 \le 1/40$, and then the $\Lambda$ that makes $\rho = 0$ (Notebook 12b, In [10] and In [11], figures 5 and 6). At the edge $\alpha_2H^2 = 1/40$ the vacuum is static, $A = 0$, with $\Lambda = -21H^2 + 420H^2/40 = -10.5H^2$. With the third-order coupling the vacuum condition is, for each $A$, a straight line in the plane of $\alpha_2H^2$ and $\alpha_3H^4$ (Notebook 12b, In [12], figure 7). Whether nature has such couplings is not known; the Revision record makes no claim about their values.

### 12.13 Example: the field equations derived by computer algebra

The first notebook repeats everything of Sections 12.3 to 12.12 with exact computer algebra, starting from nothing but the metric, and compares every result with the Revision record. It computes the 37 Christoffel symbols, the 156 nonzero Riemann components, the Einstein tensor and the three Lovelock tensors (with its own GKD), checks them against the Rust program of the GKD record in all 64 components and against the classical Gauss-Bonnet formula, writes and reduces the field equations, checks the Bianchi identity and the conservation law, and specialises to Einstein gravity and to the linear member. It runs in about 20 seconds, prints 59 PASS lines and draws five figures. It needs no Rust.

<!-- NOTEBOOK 12a -->

### 12.16 Line-by-line walk-through of Notebook 12a

The notebook has 30 code cells, In [1] to In [30]. This section explains every line of every one of them, in order. A line or a group of lines is quoted, then explained. Where a cell repeats a pattern already explained, we say so and explain only what is new.

**In [1], the set-up cell.** Every line that starts with `#` is a **comment**, which Python skips. The first comment lines of the cell are the complete run instructions of Section 12.14, so that the notebook file carries its own instructions. The code starts after the line that announces THE SET-UP (the same in every notebook of this book; it computes no physics).

```python
import json  # reads and writes JSON files (text files that hold names and numbers)
import os  # reads the environment variable TEXTBOOK_OUTPUT_ROOT (explained below)
import textwrap  # breaks long printed text into lines of at most 89 characters
from pathlib import Path  # file and folder paths that work on Windows, macOS and Linux
```

`import` loads a **module**, a part of Python or of a package, so that the code can use it. `json`, `os`, `textwrap` and `pathlib` come with Python. `from pathlib import Path` takes the one name `Path` out of `pathlib`; a `Path` is the address of a file or folder, written the same way on every operating system.

```python
import matplotlib  # the plotting package
import matplotlib.pyplot as plt  # its drawing functions, called plt by convention
from IPython.display import Image, display  # shows a saved picture below a cell
```

These load the plotting package matplotlib, its drawing functions under the short name `plt`, and the two functions `Image` and `display` of IPython (the part of Jupyter that runs Python), which show a picture file below a cell.

```python
NOTEBOOK_ID = "12a"  # this notebook: chapter 12, example a
```

A **variable** is a name for a value; this line gives the name `NOTEBOOK_ID` to the **string** (a text in quotes) `"12a"`. The figure files are named after it.

```python
def find_repository_root():
    here = Path.cwd().resolve()  # the folder in which this notebook runs
    for folder in [here, *here.parents]:  # this folder, its parent, its grandparent ...
        if (folder / "Revision" / "textbook" / "requirements.txt").is_file():
            return folder
    raise FileNotFoundError(
        "The repository folder was not found: open this notebook inside the folder "
        "Revision/textbook/notebooks of the repository Dirac_claude")
```

`def` defines a **function**, a named piece of code that runs when it is called. (In the notebook the function also has a **docstring**, the text in triple quotes under the `def` line, which says what it does; it is left out here.) `Path.cwd()` is the folder in which Jupyter runs the notebook and `.resolve()` writes it as a complete address. `here.parents` is the list of the folders above it; `[here, *here.parents]` is the list that starts with `here` and continues with them (the star unpacks a list into another list). The `for` loop visits these folders one after the other. The operator `/` joins a folder and a name into a longer path, and `.is_file()` is true when that file exists. The first folder that contains `Revision/textbook/requirements.txt` is the repository, and `return` hands it back. If none does, `raise` stops the notebook with a `FileNotFoundError` whose message says what to do.

```python
REPO = find_repository_root()
OUTPUT_ROOT = Path(os.environ.get("TEXTBOOK_OUTPUT_ROOT", str(REPO)))
```

The first line calls the function and names its result `REPO`; it is never printed, because it differs from computer to computer while the printed output of a notebook must not. The second line chooses where files are written: `os.environ` holds the **environment variables** of the program (named texts it receives from the computer), and `.get(name, default)` returns the value of `TEXTBOOK_OUTPUT_ROOT` if it is set and `str(REPO)` otherwise. When you run the notebook it is not set, so files go into the repository; the book's checking tool sets it to a scratch folder.

```python
def repository_file(relative):
    return REPO / relative


def output_file(relative):
    path = OUTPUT_ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    return path
```

Two small functions (docstrings left out). `repository_file` gives the full path of a repository file, for reading a Revision record. `output_file` gives the full path at which to write a file; `path.parent.mkdir(parents=True, exist_ok=True)` first creates its folder and any missing folder above it, and does nothing if it exists.

```python
def say(text):
    print(textwrap.fill(str(text), width=89, subsequent_indent="    "))
```

`say` prints a text in lines of at most 89 characters (the width of a page of the book); `textwrap.fill` breaks the text at blanks and starts every line after the first with four blanks.

```python
matplotlib.rcdefaults()  # ignore personal matplotlib settings: same figures everywhere
plt.rcParams.update({"figure.figsize": (7.0, 4.2), "font.size": 10.0,
                     "axes.grid": True, "grid.alpha": 0.3})
```

`matplotlib.rcdefaults()` returns to the built-in settings, so that the figures are the same on every computer. `plt.rcParams.update({...})` sets the size of a figure (7.0 by 4.2 inches), the size of its letters (10 points) and a faint grid (`grid.alpha` 0.3 means 30 per cent opaque). The braces make a **dictionary**: pairs `key: value`.

```python
FIGURE_FOLDER = "Revision/textbook/figures"  # where the figures are saved
CAPTION_FILE = f"{FIGURE_FOLDER}/{NOTEBOOK_ID}.captions.json"  # their captions
FIGURE_NUMBERS = {}  # figure name -> its number k (file name <id>_<k>_<name>.png)
CAPTIONS = {}  # figure file name -> caption, written to CAPTION_FILE after every figure
output_file(CAPTION_FILE).write_text("{}\n", encoding="utf-8", newline="\n")
```

A string that starts with `f` is an **f-string**: a name in braces is replaced by its value, so `CAPTION_FILE` is `"Revision/textbook/figures/12a.captions.json"`. `FIGURE_NUMBERS` and `CAPTIONS` start as empty dictionaries. The last line writes an empty JSON dictionary and a line end into the captions file (the comment lines above it in the notebook say so); `encoding="utf-8"` fixes how letters are stored and `newline="\n"` stores the same line end on every system.

```python
def save_figure(fig, name, caption):
    number = FIGURE_NUMBERS.setdefault(name, len(FIGURE_NUMBERS) + 1)
    file_name = f"{NOTEBOOK_ID}_{number}_{name}.png"
    relative = f"{FIGURE_FOLDER}/{file_name}"
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

(Shown without its docstring and its three comment lines.) `setdefault(name, value)` returns the number already stored for this figure name, or stores and returns one more than the number of figures so far: the figures are numbered 1, 2, 3, and a cell run twice keeps its number. The file name is the notebook id, the number and the name, for example `12a_1_riemann_matrix.png`. `fig.savefig` writes a PNG file with 150 dots per inch, cuts away the empty margin and stores no program name, so that two runs write the same bytes. `plt.close(fig)` removes the figure from memory, because Jupyter would otherwise draw it a second time. The caption is stored, the whole dictionary is written to the captions file (`json.dumps` turns it into JSON text with sorted keys), `display(Image(...))` shows the saved picture, and the last line prints where it was saved.

```python
PASSED = []  # the names of the checks that passed, in order


def check(condition, name, record=None):
    if not condition:
        raise AssertionError(f"check failed: {name}")
    PASSED.append(name)
    say(f"PASS {name}")
    if record is not None:
        say(f"     reproduces {record}")
```

`PASSED` is an empty **list** (an ordered collection in square brackets). `check` is the function behind every check: if `condition` is false (`False`), `raise AssertionError(...)` stops the notebook with an error naming the check (an `if` is used instead of the statement `assert`, because Python started with the option that optimises skips every `assert`); otherwise the name is appended to `PASSED` and the line PASS name is printed, followed by a second line naming the Revision record when `record` is given. `record=None` makes that argument optional.

```python
def report(label, value, unit=""):
    say(f"RESULT {label} = {value}" + (f" {unit}" if unit else ""))


def all_checks_passed():
    print(f"ALL {len(PASSED)} CHECKS PASSED (notebook {NOTEBOOK_ID})")


say(f"Set-up of notebook {NOTEBOOK_ID} complete: repository folder found, helpers "
    "defined.")
```

`report` prints a key number as a line that starts with RESULT; `(f" {unit}" if unit else "")` adds the unit when one is given. `all_checks_passed` prints the last line of the notebook; `len(PASSED)` is the number of checks that passed. The last statement prints the one output line of In [1].

**In [2], the Revision records.**

```python
import contextlib  # redirect_stdout: send printed lines into a buffer
import io  # StringIO: a text buffer in memory
```

Two modules of Python: `contextlib` provides `redirect_stdout`, which sends everything that `print` writes into another place, and `io` provides `StringIO`, a text buffer held in memory.

```python
PY = "Revision/field_equations_a4/reports/python-a4-report.json"  # sympy record
WL = "Revision/field_equations_a4/reports/wolfram-a4-report.json"  # Wolfram record
LEAD = "Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json"  # lead check
EMT = "Revision/lead_checks/reports/emt-divergence-and-spin-connection.json"
EQUATIONS = "Revision/field_equations_a4/a4-equations.json"  # the equations
LOVELOCK = "Revision/gkd_lovelock/results/lovelock-tensors.json"  # Rust GKD output
```

Six short names for the six record files the notebook reads: the sympy report and the Wolfram report of the field equations, the lead's two independent reports, the equations themselves (written by the Wolfram verifier) and the Lovelock tensors written by the Rust program `lovelock_gkd`.

```python
def read_json(relative):
    return json.loads(repository_file(relative).read_text(encoding="utf-8"))


def record_verdict(report_file, name):
    for entry in read_json(report_file)["checks"]:
        if entry["name"] == name:
            return entry["verdict"]
    return None
```

`read_json` reads a file of the repository as text and turns it into Python dictionaries and lists with `json.loads`. Every report holds a list under the key `"checks"`; each entry is a dictionary with a `"name"` and a `"verdict"`. `record_verdict` walks through that list and returns the verdict of the check with the given name, or `None` if there is no such check.

```python
def reproduces(condition, name, report_file, record_name):
    found = record_verdict(report_file, record_name) == "PASS"
    lines = io.StringIO()  # a text buffer
    with contextlib.redirect_stdout(lines):  # print() now writes into the buffer
        check(condition and found, name, record=f"{report_file}, check {record_name}")
    print(lines.getvalue(), end="")  # all lines at once
```

`reproduces` is a check that passes only when two things are true: the notebook's own result (`condition`) and the record's verdict PASS for the named check (`found`). `with contextlib.redirect_stdout(lines):` makes every `print` inside the indented block write into the buffer `lines` instead of the screen; after the block, `print(lines.getvalue(), end="")` prints the collected PASS and reproduces lines with one call (`end=""` adds no extra line end), so the two lines always stay together.

```python
for report_file in (PY, WL, LEAD, EMT):
    verdicts = [entry["verdict"] for entry in read_json(report_file)["checks"]]
    passed = verdicts.count("PASS")  # how many checks of the record passed
    say(f"{report_file}: {passed} of {len(verdicts)} checks PASS")
    check(len(verdicts) > 0 and passed == len(verdicts),
          f"every check of the record {Path(report_file).name} passed")
```

For each of the four reports, a **list comprehension** collects the verdicts of all its checks, `.count("PASS")` counts the PASS verdicts, and `say` prints this count together with the number of checks of the report. `check` then requires that the report has at least one check and that every one of them passed; `Path(report_file).name` is the last part of the path, the file name, which names the report in the PASS line. So Out [2] shows, for each of the four reports by name, how many checks it has and that all of them passed, followed by a PASS line. This text does not repeat the counts: a report may gain checks when its record is extended, and Out [2] always shows the counts of the reports the notebook was run with.

**In [3], the metric.**

```python
import itertools  # loops over all combinations of indices

import numpy as np  # arrays of numbers, used for the plots
import sympy as sp  # exact algebra with symbols
```

`itertools` (part of Python) produces combinations of indices; `numpy` (as `np`) computes with arrays of floating-point numbers; `sympy` (as `sp`) computes exactly with symbols.

```python
H = sp.symbols("H", positive=True)  # the constant H of the metric, H > 0
z = sp.symbols("z", positive=True)  # the hidden angle z = 6 H x8, 0 < z < pi/2
x4 = sp.symbols("x4", real=True)  # the time x4
a4 = sp.Function("a4")(x4)  # the unknown function a4(x4)
NAMES = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]  # positions 0..7
N = 8  # the number of dimensions
warp = sp.sin(z) ** sp.Rational(1, 3)  # the warp factor sin(z)^(1/3)
```

`sp.symbols` makes a symbol, a letter that stands for any number; `positive=True` and `real=True` tell sympy what kind of number, which lets it simplify safely (for example $\sqrt{H^2} = H$ for $H > 0$). `sp.Function("a4")(x4)` is an unknown function of $x_4$: sympy can differentiate it without knowing it. `NAMES` lists the coordinates in the author's order; `N = 8`. `sp.Rational(1, 3)` is the exact fraction $1/3$ (the floating-point number 0.333... would introduce rounding), and `**` means "to the power".

```python
g = ([sp.exp(2 * a4) * warp] * 3  # g11 = g22 = g33: 3-space, factor e^(2 a4)
     + [sp.Integer(-1)]  # g44 = -1: the time x4
     + [-sp.exp(-2 * a4) * warp] * 3  # g55 = g66 = g77: extra times, e^(-2 a4)
     + [sp.cot(z) ** 2])  # g88 = cot(z)^2: the hidden direction
for name, entry in zip(NAMES, g):
    say(f"g[{name},{name}] = {entry}")
```

A list times 3 repeats it three times, and `+` joins lists; so `g` is the list of the eight diagonal entries of Section 12.3, in the order $x_1, \dots, x_8$. `zip(NAMES, g)` pairs each name with its entry, and the loop prints the eight lines of Out [3].

**In [4], signature and determinant.**

```python
point = {a4: 0, z: sp.pi / 4}  # any point of the patch gives the same signs
signs = [int(sp.sign(entry.subs(point))) for entry in g]
say(f"signs of the diagonal entries: {signs}")
check(signs == [1, 1, 1, -1, -1, -1, -1, 1],
      "the signature is (4,4): eta = diag(+,+,+,-,-,-,-,+) in the order x1..x8")
```

`entry.subs(point)` replaces $a_4$ by 0 and $z$ by $\pi/4$ in an entry; `sp.sign` gives $+1$ or $-1$ and `int` makes it a Python integer. The check compares the list of signs with the signature (4,4).

```python
det_g = sp.Mul(*g)  # the product of the eight diagonal entries
say(f"det g = {sp.simplify(det_g)}")
reproduces(sp.simplify(det_g - sp.cos(z) ** 2) == 0,
           "det g = cos(z)^2, so sqrt|det g| = cos z, independent of a4",
           WL, "sqrt_abs_det_g_is_cos_z")
```

`sp.Mul(*g)` multiplies all entries of the list (the star passes the eight entries as eight separate arguments). `sp.simplify` reduces the product to `cos(z)**2`, the result of Section 12.3, and `reproduces` checks that $\det g - \cos^2 z$ simplifies to 0 and that the Wolfram record has the same check.

**In [5], the Christoffel symbols.**

```python
def d(expr, mu):
    if mu == 3:
        return sp.diff(expr, x4)
    if mu == 7:
        return 6 * H * sp.diff(expr, z)
    return sp.Integer(0)  # nothing depends on x1, x2, x3, x5, x6, x7
```

The function `d` is the partial derivative with respect to the coordinate at position `mu` (docstring left out): for position 3 ($x_4$) it is `sp.diff(expr, x4)`; for position 7 ($x_8$) it is $6H\,\partial/\partial z$ (the chain rule of Section 12.4); for every other position it is zero, because nothing depends on those coordinates.

```python
Gamma = [[[sp.Integer(0)] * N for _ in range(N)] for _ in range(N)]  # 512 zeros
for a, b, c in itertools.product(range(N), repeat=3):  # every index triple
    value = 0
    if a == c:
        value += d(g[a], b)
    if a == b:
        value += d(g[a], c)
    if b == c:
        value -= d(g[b], a)
    Gamma[a][b][c] = value / (2 * g[a])  # Gamma^a_bc of a diagonal metric
```

The first line makes a nested list of $8 \times 8 \times 8 = 512$ exact zeros, `Gamma[a][b][c]` (the underscore `_` is a loop variable whose value is not used). `itertools.product(range(N), repeat=3)` produces all 512 triples $(a, b, c)$. The body is the diagonal formula of Section 12.4: the three `if` lines add $\delta_{ac}\partial_b g_{aa}$, add $\delta_{ab}\partial_c g_{aa}$ and subtract $\delta_{bc}\partial_a g_{bb}$ (`+=` adds to a variable, `-=` subtracts), and the last line divides by $2g_{aa}$.

```python
nonzero = [(a, b, c) for a, b, c in itertools.product(range(N), repeat=3)
           if Gamma[a][b][c] != 0]
say(f"{len(nonzero)} of the 512 Christoffel symbols are not zero")
check(len(nonzero) == 37,
      "37 nonzero Christoffel symbols (25 distinct, 12 of them twice)")
check(all(Gamma[a][b][c] == Gamma[a][c][b] for a, b, c in nonzero),
      "Gamma^a_bc = Gamma^a_cb (symmetric in the two lower indices)")
```

The list comprehension keeps the triples whose symbol is not zero (`!=` means "is not equal to"); `len` counts them: 37, as counted in Section 12.4. `all(...)` is true when the condition holds for every triple of the list; the second check is the symmetry in the two lower indices.

**In [6], the symbols printed.**

```python
ad1, ad2, ad3 = sp.symbols("ad1 ad2 ad3", real=True)


def derivatives_as_symbols(expr):
    expr = expr.subs(sp.Derivative(a4, (x4, 3)), ad3)  # highest derivative first
    expr = expr.subs(sp.Derivative(a4, (x4, 2)), ad2)
    return expr.subs(sp.Derivative(a4, x4), ad1)


def readable(expr):
    return sp.simplify(derivatives_as_symbols(expr))
```

Three plain symbols stand for $a_4'$, $a_4''$ and $a_4'''$. `derivatives_as_symbols` replaces the derivatives of the function $a_4$ by them, the highest derivative first (a second derivative contains the first derivative inside it, so replacing the first derivative first could break it). `readable` also simplifies, for printing.

```python
for a, b, c in nonzero:
    if b <= c:  # print each symmetric pair once
        say(f"Gamma^{NAMES[a]}_{NAMES[b]}{NAMES[c]} = {readable(Gamma[a][b][c])}")
```

The loop prints each of the 25 distinct symbols once (`b <= c` skips the second member of each symmetric pair). Out [6] shows exactly the symbols derived by hand in Section 12.4, for example `Gamma^x5_x4x5 = -ad1` and `Gamma^x8_x8x8 = -12*H/sin(2*z)`.

**In [7], the Riemann tensor.**

```python
cz = sp.symbols("cz", positive=True)  # cz = cot z > 0 on the patch
TRIG = {sp.sin(z): 1 / sp.sqrt(1 + cz ** 2), sp.cos(z): cz / sp.sqrt(1 + cz ** 2),
        sp.tan(z): 1 / cz, sp.cot(z): cz}  # every function of z through cot z
```

A positive symbol `cz` stands for $\cot z$, and the dictionary `TRIG` says how to write each function of $z$ through it: from $\cot z = \cos z/\sin z$ and $\sin^2 z + \cos^2 z = 1$ follow $\sin z = 1/\sqrt{1 + \cot^2 z}$ and $\cos z = \cot z/\sqrt{1 + \cot^2 z}$ on the patch.

```python
def clean(expr):
    expr = sp.expand_trig(derivatives_as_symbols(expr)).subs(TRIG)
    return sp.expand(sp.cancel(sp.powsimp(sp.expand(expr), force=True)))
```

`clean` brings an expression to one canonical form (docstring left out): derivatives become `ad1`, `ad2`, `ad3`; `sp.expand_trig` writes $\sin 2z$ as $2\sin z\cos z$; `.subs(TRIG)` writes every function of $z$ through `cz`; `sp.expand` multiplies out; `sp.powsimp(..., force=True)` combines powers of the same base (so that $e^{2a_4}e^{-2a_4}$ becomes 1 and powers of $1 + \cot^2 z$ combine); `sp.cancel` cancels common factors of numerator and denominator; the last `sp.expand` multiplies out again. Two expressions that are equal then look equal.

```python
R = {}  # R[(a, b, m, n)] = R^{ab}_{mn}; only the components that are not zero
for a, b, m, n in itertools.product(range(N), repeat=4):
    if a == b or m == n:
        continue  # antisymmetry: zero when the two indices of a pair are equal
    value = (d(Gamma[a][b][n], m) - d(Gamma[a][b][m], n)
             + sum(Gamma[a][m][e] * Gamma[e][b][n] - Gamma[a][n][e] * Gamma[e][b][m]
                   for e in range(N)))  # R^a_bmn in the MTW convention
    if value != 0:
        value = clean(value / g[b])  # raise the index b: multiply by g^bb
        if value != 0:
            R[(a, b, m, n)] = value
```

`R` starts as an empty dictionary; its keys will be index lists $(a, b, m, n)$. The loop runs over all $8^4 = 4096$ index lists; `continue` skips those with $a = b$ or $m = n$, which are zero by antisymmetry. The expression for `value` is the definition of Section 12.5 term by term: two derivatives and the sum over $e$ of the two products (`sum(... for e in range(N))` adds the expression for $e = 0, \dots, 7$). If the result is not zero, dividing by $g_{bb}$ raises the index $b$ (multiplication by $g^{bb} = 1/g_{bb}$), `clean` simplifies, and a component that is still not zero is stored.

```python
ordered = {key: value for key, value in R.items()
           if key[0] < key[1] and key[2] < key[3]}  # a < b and m < n
report("nonzero components R^ab_mn of the 4096", len(R))
report("nonzero components with a < b and m < n", len(ordered))
```

A **dictionary comprehension** keeps the components with $a < b$ and $m < n$ (`key[0]` is the first index of the key). The two RESULT lines report 156 and 39 (Section 12.5).

**In [8], four facts about the curvature.**

```python
reproduces(len(R) == 156, "156 nonzero components R^ab_mn of the 4096",
           PY, "mixed_riemann_free_of_warp_and_a4")
reproduces(len(ordered) == 39, "39 nonzero components with a < b and m < n",
           WL, "mixed_riemann_free_of_warp_and_a4")
```

The two counts, compared with the sympy and the Wolfram record (both records state the counts in the detail of the named check).

```python
free = all(not v.has(a4) and not v.has(z) and not v.has(sp.exp) for v in R.values())
reproduces(free, "R^ab_mn is free of the warp factor and of e^(a4)",
           PY, "mixed_riemann_free_of_warp_and_a4")
```

`v.has(x)` is true when the expression `v` contains `x` anywhere. The condition says that no component contains the function $a_4$, the angle $z$ (so no warp factor) or an exponential.

```python
laurent = all(sp.expand(v * cz).is_polynomial(H, ad1, ad2, cz) for v in R.values())
reproduces(laurent, "every R^ab_mn is a Laurent polynomial in cot z",
           PY, "riemann_entries_laurent")
```

Multiplying a component by $\cot z$ must give a polynomial in $H$, $a_4'$, $a_4''$ and $\cot z$; then the component itself is a polynomial divided at most by $\cot z$, a **Laurent polynomial** in $\cot z$.

```python
antisymmetric = all(R.get((b, a, m, n)) == -v and R.get((a, b, n, m)) == -v
                    for (a, b, m, n), v in R.items())
reproduces(antisymmetric, "R^ab_mn = -R^ba_mn = -R^ab_nm",
           PY, "riemann_pair_antisymmetry")
```

`R.get(key)` returns the stored value or `None` if the key is absent. For every stored component the exchanged components must be stored with the opposite value.

**In [9], the 39 components grouped.**

```python
def pair_name(a, b):
    return NAMES[a] + NAMES[b]


groups = {}  # printed value -> the components that have it
for (a, b, m, n), value in ordered.items():
    label = f"{pair_name(a, b)}|{pair_name(m, n)}"
    groups.setdefault(str(value), []).append(label)
for value, members in groups.items():
    say(f"{value} ({len(members)}): " + " ".join(members))
```

`pair_name` joins two coordinate names, for example `x1x4`. The first loop files each component under its printed value: `groups.setdefault(str(value), [])` returns the list stored for this value, creating an empty one the first time, and `.append(label)` adds the label `x1x4|x1x4`. The second loop prints each value, the number of its members and the members joined by blanks. Out [9] is the table of Section 12.5: seven groups, of which two are the off-diagonal ones with `cz`.

**In [10], figure 1: the Riemann tensor as a heat map.**

```python
PAIRS28 = [(a, b) for a in range(N) for b in range(a + 1, N)]  # the 28 pairs
SAMPLE = {H: 1, ad1: sp.Rational(3, 5), ad2: sp.Rational(3, 10),
          cz: 1 / sp.sqrt(3)}  # H = 1, a4' = 0.6, a4'' = 0.3, z = pi/3
table = np.zeros((28, 28))
for i, (a, b) in enumerate(PAIRS28):
    for j, (m, n) in enumerate(PAIRS28):
        if (a, b, m, n) in R:
            table[i, j] = float(R[(a, b, m, n)].subs(SAMPLE))
```

`PAIRS28` lists the 28 pairs $a < b$. `SAMPLE` is a sample point at which the exact components are evaluated: $H = 1$, $a_4' = 0.6$, $a_4'' = 0.3$ and $\cot z = 1/\sqrt3$, that is $z = \pi/3$. `np.zeros((28, 28))` is a 28 by 28 table of zeros. `enumerate` gives each pair together with its position `i` (or `j`); for every stored component the table entry becomes its value at the sample point, converted to a floating-point number by `float`.

```python
limit = np.abs(table).max()  # the same scale for both signs
labels = [pair_name(a, b) for a, b in PAIRS28]
fig, ax = plt.subplots(figsize=(7.5, 6.6))
image = ax.imshow(table, cmap="RdBu_r", vmin=-limit, vmax=limit)
```

`limit` is the largest absolute value in the table. `plt.subplots` makes a figure and one pair of axes, 7.5 by 6.6 inches. `ax.imshow` draws the table as coloured squares with the colour map `RdBu_r` (blue for negative, white for zero, red for positive); `vmin=-limit, vmax=limit` make the scale symmetric, so that white means exactly zero.

```python
ax.set_xticks(range(28))
ax.set_xticklabels(labels, rotation=90, fontsize=6)
ax.set_yticks(range(28))
ax.set_yticklabels(labels, fontsize=6)
ax.set_xlabel("lower index pair $(m, n)$")
ax.set_ylabel("upper index pair $(a, b)$")
ax.grid(False)
ax.set_title("Riemann tensor $R^{ab}{}_{mn}$ at $H=1$, $a_4'=0.6$, "
             "$a_4''=0.3$, $z=\\pi/3$")
fig.colorbar(image, ax=ax, shrink=0.8, label="value (units of $H^2$)")
```

These lines put a tick at each of the 28 positions on both axes and label it with the pair name (turned by 90 degrees on the horizontal axis), name the axes, switch off the grid (it would cover the squares), set the title (text between dollar signs is typeset as mathematics; a doubled backslash in a Python string is one backslash) and add a colour bar that translates colours into values.

```python
save_figure(fig, "riemann_matrix",
            "The Riemann tensor $R^{ab}{}_{mn}$ of the author's metric as a 28 by "
            ...)
```

`save_figure` saves the figure as `12a_1_riemann_matrix.png` with its caption (printed in full in the notebook text; Python joins strings written next to each other into one). **What the figure shows.** Almost all the colour sits on the diagonal: the 27 pair curvatures of Section 12.5 (the diagonal square of $x_4x_8$ is white, because that pair curvature is zero). The few coloured squares off the diagonal are the 12 components that couple, for example, $x_1x_4$ with $x_1x_8$; they are proportional to $Ha_4'$ and would vanish for a constant $a_4$.

**In [11], Ricci, Ricci scalar and Einstein tensor.**

```python
Ricci = [[sp.expand(sum(R.get((a, h, a, j), 0) for a in range(N)))
          for j in range(N)] for h in range(N)]  # R^h_j
ricci_scalar = sp.expand(sum(Ricci[h][h] for h in range(N)))
G = [[sp.expand(Ricci[h][j] - (ricci_scalar / 2 if h == j else 0))
      for j in range(N)] for h in range(N)]  # G^h_j
```

The three definitions of Section 12.6. `R.get((a, h, a, j), 0)` returns 0 for a component that is not stored. `Ricci[h][j]` is the sum over $a$; `ricci_scalar` the sum of the diagonal; `G` subtracts half the Ricci scalar on the diagonal only (`x if condition else y` chooses between two values).

```python
report("Ricci scalar R", ricci_scalar)
for h in range(N):
    say(f"G^{NAMES[h]}_{NAMES[h]} = {G[h][h]}")
```

The RESULT line shows $R = 6(a_4')^2 - 42H^2$ and the loop prints the eight diagonal components: exactly those derived by hand in Section 12.6.

**In [12], the Einstein tensor compared with the records.**

```python
reproduces(all(G[h][j] == 0 for h in range(N) for j in range(N) if h != j),
           "G^h_j is diagonal (in particular G^x4_x8 = G^x8_x4 = 0)",
           LEAD, "einstein_off_diagonal_zero")
reproduces(G[0][0] == G[1][1] == G[2][2] and G[4][4] == G[5][5] == G[6][6],
           "G^x1_x1 = G^x2_x2 = G^x3_x3 and G^x5_x5 = G^x6_x6 = G^x7_x7",
           LEAD, "einstein_isotropy")
reproduces(not any(G[h][j].has(cz) for h in range(N) for j in range(N)),
           "every component of G is independent of x8",
           LEAD, "einstein_x8_independent")
```

Three structural checks against the lead's record: every off-diagonal component is zero (the cancellation of Section 12.6), the components are equal within 3-space and within the extra times (Python allows the chain `x == y == z`), and no component contains $\cot z$ (`any` is true when at least one element is true; `not any` when none is).

```python
expected = {3: 3 * ad1 ** 2 + 21 * H ** 2, 0: ad2 - 3 * ad1 ** 2 + 15 * H ** 2,
            4: -ad2 - 3 * ad1 ** 2 + 15 * H ** 2, 7: -3 * ad1 ** 2 + 15 * H ** 2}
reproduces(all(sp.expand(G[i][i] - v) == 0 for i, v in expected.items()),
           "the four Einstein components agree with the record",
           PY, "einstein_components")
```

The dictionary `expected` holds the four distinct components, keyed by their positions (3 for $x_4$, 0 for $x_1$, 4 for $x_5$, 7 for $x_8$); the check requires each difference to expand to zero.

**In [13], figure 2: the Einstein components.**

```python
u = np.linspace(-3.0, 3.0, 301)  # a4'/H
fig, ax = plt.subplots()
ax.plot(u, 3 * u ** 2 + 21, label="$G^{x_4}{}_{x_4}$ (constraint)")
ax.plot(u, 15 - 3 * u ** 2, color="black",
        label="$G^{x_8}{}_{x_8}$ $=$ $G^{x_1}{}_{x_1}$ $=$ $G^{x_5}{}_{x_5}$ "
              "at $a_4''=0$")
ax.plot(u, 15 - 3 * u ** 2 + 1, "--", label="$G^{x_1}{}_{x_1}$ at $a_4''=H^2$")
ax.plot(u, 15 - 3 * u ** 2 - 1, "--", label="$G^{x_5}{}_{x_5}$ at $a_4''=H^2$")
```

`np.linspace(-3.0, 3.0, 301)` makes 301 equally spaced values of $a_4'/H$ from $-3$ to 3 (step 0.02). In units $H = 1$ the four formulas of Section 12.6 are evaluated on the whole array at once and drawn with `ax.plot(x, y, ...)`; the string of two hyphens makes a dashed line, and `label=` names the curve in the legend.

```python
ax.set_xlabel("$a_4'/H$")
ax.set_ylabel("component of $G^\\mu{}_\\nu$ (units of $H^2$)")
ax.set_title("The Einstein tensor of the author's metric")
ax.legend(fontsize=8)
save_figure(fig, "einstein_components",
            ...)
```

Axis labels, title, legend, and `save_figure` with the caption printed in the notebook text. **What the figure shows.** The time component is a parabola that opens upwards and never falls below $21H^2$; the hidden component opens downwards. The two dashed curves lie a distance $H^2$ above and below the black one: only the difference of the 3-space and the extra-time components feels $a_4''$, which is why the evolution equation of Section 12.9 is their difference.

**In [14], the generalized Kronecker delta.**

```python
def gkd(upper, lower):
    if len(set(upper)) != len(upper) or sorted(upper) != sorted(lower):
        return 0
    position = [upper.index(index) for index in lower]  # where each one sits
    inversions = sum(1 for i in range(len(position))
                     for j in range(i + 1, len(position))
                     if position[i] > position[j])
    return -1 if inversions % 2 else 1
```

`set(upper)` keeps each index once, so `len(set(upper)) != len(upper)` detects a repeated index; `sorted(upper) != sorted(lower)` detects two lists that do not hold the same indices; in both cases the delta is 0. Otherwise `position` lists where each lower index sits in the upper list (`upper.index(x)` is the position of `x`): this is the rearrangement. `inversions` counts the pairs of positions $i < j$ that appear in the wrong order. An even number of inversions means an even rearrangement (sign $+1$), an odd number an odd one ($-1$); `inversions % 2` is the remainder after division by 2.

```python
say(f"gkd([1, 2], [1, 2]) = {gkd([1, 2], [1, 2])}, gkd([1, 2], [2, 1]) = "
    f"{gkd([1, 2], [2, 1])}, gkd([1, 1], [1, 1]) = {gkd([1, 1], [1, 1])}")
nine = list(range(8)) + [0]  # nine indices from eight values: one repeats
reproduces(gkd(nine, nine) == 0 and gkd(list(range(8)), list(range(8))) == 1,
           "a GKD of 9 indices in 8 dimensions is 0: P_(4) = 0",
           WL, "P4_vanishes_pigeonhole")
```

Three small examples are printed: 1, $-1$ and 0. Then a list of nine indices made of the eight values 0 to 7 and a repeated 0: its delta is 0, while the delta of the eight different indices with themselves is 1. This is the pigeonhole argument of Section 12.7.

**In [15], the three Lovelock tensors.**

```python
tz = sp.symbols("tz", positive=True)  # tz = tan z = 1/cot z
GENERATORS = (H, ad1, ad2, cz, tz)
# xreplace replaces exactly the expression 1/cz by tz and leaves cz itself alone:
FACTORS = [(key, sp.Poly(value.xreplace({1 / cz: tz}), *GENERATORS))
           for key, value in ordered.items()]  # the 39 components as polynomials
```

To multiply thousands of products quickly, each of the 39 components is stored as a sympy **polynomial** (`sp.Poly`) in the five generators $H$, $a_4'$, $a_4''$, $\cot z$ and a new symbol $t = \tan z$, listed in `GENERATORS`. The comment line says what the next line does: `value.xreplace({1 / cz: tz})` replaces exactly the expression $1/\cot z$ by $t$ and leaves every $\cot z$ itself unchanged, so that no division is left and the component is a polynomial. `FACTORS` is the list of pairs (index list, polynomial).

```python
def lovelock(k):
    zero = sp.Poly(0, *GENERATORS)
    P = [[zero] * N for _ in range(N)]
    L = zero
    terms = 0
```

The function `lovelock(k)` (docstring left out) starts with the zero polynomial, an 8 by 8 table `P` of zeros, a zero scalar `L` and a counter `terms`.

```python
    for factors in itertools.product(FACTORS, repeat=k):
        lower = [i for key, _ in factors for i in key[0:2]]  # upper indices of R
        upper = [i for key, _ in factors for i in key[2:4]]  # lower indices of R
        if len(set(lower)) < 2 * k or len(set(upper)) < 2 * k:
            continue  # a repeated index: the GKD is zero
        terms += 1
```

`itertools.product(FACTORS, repeat=k)` produces every list of $k$ components ($39^k$ lists). For each, `lower` collects the two upper indices of each Riemann factor (`key[0:2]` is the first two entries of the key): in the formula of Section 12.7 these are the lower indices $j_1 \dots j_{2k}$ of the delta. `upper` collects the lower indices of the factors, the upper indices $h_1 \dots h_{2k}$ of the delta. A list with a repeated index is skipped, because its delta is zero; the others are counted.

```python
        product = sp.Poly(4 ** k, *GENERATORS)  # the factor 4^k
        for _, poly in factors:
            product = product * poly
        L = L + gkd(upper, lower) * product
        for h, j in itertools.product(range(N), repeat=2):
            sign = gkd([h] + upper, [j] + lower)
            if sign:
                P[h][j] = P[h][j] + sign * product
```

The product of the $k$ factors is multiplied by $4^k$: each factor stands for its four orderings ($b < a$ or $n < m$ as well), which give the same contribution (the text cell before the cell explains why). The product, with the sign of the delta, is added to the scalar `L` and, for every pair $(h, j)$ with a nonzero delta `gkd([h] + upper, [j] + lower)`, to `P[h][j]` (`if sign:` is true for $+1$ and $-1$, false for 0).

```python
    back = {tz: 1 / cz}  # tan z back to 1/cot z
    P = [[sp.expand(P[h][j].as_expr().subs(back)) for j in range(N)]
         for h in range(N)]
    return P, sp.expand(L.as_expr().subs(back)), terms
```

At the end `.as_expr()` turns each polynomial back into an ordinary expression, $t$ is replaced by $1/\cot z$ again, and the function returns the table, the scalar and the count.

```python
P, Lscalar, E = {}, {}, {}
for k in (1, 2, 3):
    P[k], Lscalar[k], terms = lovelock(k)
    E[k] = [[sp.expand(-P[k][h][j] / 2 ** (k + 1)) for j in range(N)]
            for h in range(N)]  # E_(k) = -P_(k)/2^(k+1)
    say(f"k = {k}: {terms} lists of index pairs contribute; L_({k}) = {Lscalar[k]}")
```

For $k = 1, 2, 3$ the cell computes $P_{(k)}$, $L_{(k)}$ and the number of contributing lists, forms $E_{(k)} = -P_{(k)}/2^{k+1}$ and prints a line. Out [15] shows 39, 690 and 4410 contributing lists and the three Lovelock scalars; for example $L_{(1)} = 12(a_4')^2 - 84H^2$, which is twice the Ricci scalar.

**In [16], the Lovelock tensors compared with the records.**

```python
reproduces(all(sp.expand(E[1][h][j] - G[h][j]) == 0
               for h in range(N) for j in range(N)),
           "E_(1) = G in all 64 components (P_(1) = -4 G)",
           PY, "P1_equals_minus_4_Einstein")
lovelock_json = read_json(LOVELOCK)
```

The first check is the statement $E_{(1)} = G$ of Section 12.7 in all 64 components. The next line reads the Rust record.

```python
for k in (1, 2, 3):
    Ek = E[k]
    structure = (all(Ek[h][j] == 0 for h in range(N) for j in range(N) if h != j)
                 and Ek[0][0] == Ek[1][1] == Ek[2][2]
                 and Ek[4][4] == Ek[5][5] == Ek[6][6]
                 and not any(Ek[h][h].has(cz) for h in range(N)))
    reproduces(structure, f"E_({k}) diagonal, free of x8, isotropic in each group",
               PY, f"P{k}_structure")
```

For each $k$: the tensor is diagonal, equal within 3-space and within the extra times, and free of $\cot z$; compared with the record checks `P1_structure`, `P2_structure`, `P3_structure`.

```python
    trace = sp.expand(sum(P[k][h][h] for h in range(N)) - (8 - 2 * k) * Lscalar[k])
    reproduces(trace == 0, f"trace identity sum_h P_({k})^h_h = (8 - {2 * k}) L_({k})",
               PY, f"P{k}_trace_identity")
```

The trace identity $\sum_h P_{(k)}{}^h{}_h = (8 - 2k)L_{(k)}$: summing the delta with $h = j$ over the $8 - 2k$ values of $h$ that are not among the other $2k$ indices gives $8 - 2k$ times the scalar.

```python
    text = lovelock_json[f"L{k}"].replace("Derivative[1][a4][x4]", "ad1")
    rust = sp.sympify(text.replace("^", "**"), locals={"H": H, "ad1": ad1})
    reproduces(sp.expand(rust - Lscalar[k]) == 0,
               f"L_({k}) equals the Rust GKD program", PY, f"L{k}_equals_gkd_branch")
```

The Rust record stores each scalar as a text in the Wolfram Language; `.replace` turns the Wolfram name of the derivative into `ad1` and the power sign `^` into `**`, and `sp.sympify` turns the text into a sympy expression (`locals` says which names are our symbols). The scalars must agree. Out [16] shows the ten PASS lines.

**In [17], all 192 components compared with the Rust and Wolfram records.**

```python
symbols_of_monomial = (H, ad1, ad2, ad3, sp.Symbol("ad4"), sp.Symbol("Ee"),
                       sp.Symbol("Ss"), cz)  # the order of the exponents


def from_monomials(monomials):
    total = sp.Integer(0)
    for numerator, denominator, exponents in monomials:
        term = sp.Rational(numerator, denominator)
        for symbol, power in zip(symbols_of_monomial, exponents):
            term *= symbol ** power
        total += term
    return total
```

The Rust program stores each component as a list of **monomials**: a fraction (numerator, denominator) and the eight exponents of $H$, $a_4'$, $a_4''$, $a_4'''$, $a_4''''$, $e^{a_4}$, $\sin^{1/3}z$ and $\cot z$, in this order. `from_monomials` rebuilds the expression: each term is the fraction times every symbol to its power (`*=` multiplies a variable), and the terms are added.

```python
for k in (1, 2, 3):
    block = lovelock_json[f"P{k}_mixed_up_h_down_j"]
    same = all(sp.expand(from_monomials(block[f"{NAMES[h]},{NAMES[j]}"]["monomials"])
                         - P[k][h][j]) == 0 for h in range(N) for j in range(N))
    reproduces(same, f"all 64 components of P_({k}) equal the Rust GKD record",
               PY, f"P{k}_equals_gkd_branch_monomials")
```

For each $k$ the record's block is a dictionary keyed by `"x1,x1"` and so on; every one of the 64 rebuilt components must equal the notebook's. A component of the record that contained $e^{a_4}$, the warp or a third derivative would differ, so the check also confirms that none does.

```python
equations_json = read_json(EQUATIONS)
LOCALS = {"ad1": ad1, "ad2": ad2, "H": H}


def parse(text, names=None):
    return sp.sympify(text.replace("^", "**"), locals=names or LOCALS)
```

The Wolfram record is read; `parse` turns one of its texts into a sympy expression (`names or LOCALS` uses the dictionary `names` when one is given and `LOCALS` otherwise; docstring left out).

```python
POSITIONS = {"x1x1": (0, 0), "x4x4": (3, 3), "x5x5": (4, 4), "x8x8": (7, 7),
             "x4x8": (3, 7), "x8x4": (7, 3)}
same = all(sp.expand(parse(equations_json["lovelockTensors"][f"E{k}"][key]["input"])
                     - E[k][h][j]) == 0
           for k in (1, 2, 3) for key, (h, j) in POSITIONS.items())
reproduces(same, "E_(1), E_(2), E_(3) equal the Wolfram record a4-equations.json",
           PY, "json_lovelock_components")
```

The record stores six components of each tensor (the four distinct diagonal ones and the two mixed ones $x_4x_8$, $x_8x_4$), each with an `"input"` text. All 18 must equal the notebook's.

**In [18], an independent route to the Gauss-Bonnet tensor.**

```python
def contract(mu, nu):
    term_a = ricci_scalar * Ricci[mu][nu]
    term_b = sum(Ricci[mu][a] * Ricci[a][nu] for a in range(N))
    term_c = sum(R.get((mu, a, nu, b), 0) * Ricci[b][a]
                 for a in range(N) for b in range(N))
    term_d = sum(R.get((mu, a, b, c), 0) * R.get((b, c, nu, a), 0)
                 for a in range(N) for b in range(N) for c in range(N))
    return 2 * (term_a - 2 * term_b - 2 * term_c + term_d)
```

The bracket of the Lanczos formula printed in the text cell before the cell, term by term: $R\,R^\mu{}_\nu$, $\sum_a R^\mu{}_aR^a{}_\nu$, $\sum_{a,b}R^{\mu a}{}_{\nu b}R^b{}_a$ and $\sum_{a,b,c}R^{\mu a}{}_{bc}R^{bc}{}_{\nu a}$, combined with the factors 2, $-4$, $-4$ and 2 (docstring left out).

```python
gauss_bonnet_scalar = (ricci_scalar ** 2
                       - 4 * sum(Ricci[a][b] * Ricci[b][a]
                                 for a in range(N) for b in range(N))
                       + sum(v * R.get((m, n, a, b), 0)
                             for (a, b, m, n), v in R.items()))
lanczos = [[sp.expand(contract(mu, nu)
                      - (gauss_bonnet_scalar / 2 if mu == nu else 0))
            for nu in range(N)] for mu in range(N)]
check(all(sp.expand(lanczos[h][j] - E[2][h][j]) == 0
          for h in range(N) for j in range(N)),
      "E_(2) (GKD) equals the classical Gauss-Bonnet tensor for every a4")
```

The Gauss-Bonnet scalar $R^2 - 4R^a{}_bR^b{}_a + R^{ab}{}_{cd}R^{cd}{}_{ab}$ (the last sum multiplies each stored component by the one with the two pairs exchanged); the Lanczos tensor subtracts half of it on the diagonal. The check compares all 64 components with $E_{(2)}$ from the GKD: two entirely different routes give the same tensor for every $a_4$.

```python
A = sp.symbols("A", real=True)  # the slope of the linear member, a4' = A H
LINEAR = {ad1: A * H, ad2: 0}
reproduces(sp.expand(lanczos[3][3].subs(LINEAR)
                     + H ** 4 * (36 * A ** 4 + 120 * A ** 2 + 420)) == 0,
           "linear member: Gauss-Bonnet H^x4_x4 = -H^4 (36 A^4 + 120 A^2 + 420)",
           LEAD, "gauss_bonnet_rho_alpha2")
reproduces(sp.expand(lanczos[0][0].subs(LINEAR)
                     - 12 * H ** 4 * (A ** 4 + 14 * A ** 2 - 15)) == 0,
           "linear member: Gauss-Bonnet H^x1_x1 = 12 H^4 (A^4 + 14 A^2 - 15)",
           LEAD, "gauss_bonnet_p_alpha2")
```

For the linear member ($a_4' = AH$, $a_4'' = 0$) the time and 3-space components are compared with the numbers of the lead's independent computation.

**In [19], the Bianchi identity.**

```python
def divergence(T):
    return [clean(sum(d(T[m][n], m) for m in range(N))
                  + sum(Gamma[m][m][l] * T[l][n] for m in range(N) for l in range(N))
                  - sum(Gamma[l][m][n] * T[m][l] for m in range(N) for l in range(N)))
            for n in range(N)]
```

The covariant divergence of a mixed tensor, $\nabla_\mu T^\mu{}_\nu = \sum_\mu\partial_\mu T^\mu{}_\nu + \sum_{\mu,l}\Gamma^\mu{}_{\mu l}T^l{}_\nu - \sum_{\mu,l}\Gamma^l{}_{\mu\nu}T^\mu{}_l$, for each $\nu$; the result is a list of eight cleaned expressions (docstring left out).

```python
AS_FUNCTIONS = {ad2: sp.Derivative(a4, (x4, 2)), ad1: sp.Derivative(a4, x4)}
for k in (1, 2, 3):
    Ek_functions = [[E[k][h][j].subs(AS_FUNCTIONS) for j in range(N)]
                    for h in range(N)]
    reproduces(all(value == 0 for value in divergence(Ek_functions)),
               f"nabla_mu E_({k})^mu_nu = 0 for nu = x1..x8",
               PY, f"E{k}_divergence_free")
```

The symbols `ad1`, `ad2` are plain letters, which `sp.diff` would treat as constants; so they are written back as derivatives of the function $a_4(x_4)$ before the divergence is taken. For each $k$ all eight components of the divergence must vanish: the Bianchi identity of Section 12.10.

**In [20], figure 3: the three Lovelock tensors as heat maps.**

```python
fig, axes = plt.subplots(1, 3, figsize=(12.0, 4.4))
for ax, k in zip(axes, (1, 2, 3)):
    values = np.array([[float(E[k][h][j].subs(SAMPLE)) for j in range(N)]
                       for h in range(N)])
    scale = np.abs(values).max()
    ax.imshow(values, cmap="RdBu_r", vmin=-scale, vmax=scale)
```

`plt.subplots(1, 3, ...)` makes one row of three axes. For each tensor the 64 components are evaluated at the sample point of In [10] into an 8 by 8 array and drawn with its own symmetric colour scale.

```python
    for h in range(N):  # write each diagonal value into its cell
        value = values[h, h]
        text = f"{value:.0f}" if abs(value) >= 100 else f"{value:.1f}"
        ink = "white" if abs(value) > 0.6 * scale else "black"  # readable on dark
        ax.text(h, h, text, ha="center", va="center", fontsize=6.5, color=ink)
```

Each diagonal value is written into its cell: as a whole number (`:.0f`) when it is at least 100 and with one decimal (`:.1f`) otherwise, in white on dark cells and black on light ones; `ha` and `va` centre the text.

```python
    ax.set_xticks(range(N))
    ax.set_xticklabels(NAMES, fontsize=7)
    ax.set_yticks(range(N))
    ax.set_yticklabels(NAMES, fontsize=7)
    ax.grid(False)
    ax.set_title(f"$E_{{({k})}}{{}}^h{{}}_j$")
fig.suptitle("The three Lovelock tensors at $H=1$, $a_4'=0.6$, $a_4''=0.3$ "
             "(row $h$, column $j$)")
save_figure(fig, "lovelock_heat_maps",
            ...)
```

Ticks labelled $x_1$ to $x_8$, no grid, a title per panel (in an f-string a doubled brace prints one brace, so the title is the mathematics $E_{(k)}{}^h{}_j$), a title for the whole figure, and `save_figure`. **What the figure shows.** All three tensors are diagonal with only four different values, one each for 3-space, the time, the extra times and the hidden direction: the structure that reduces the 64 field equations to four.

**In [21], the field equations.**

```python
alpha1, alpha2, alpha3 = sp.symbols("alpha1 alpha2 alpha3", real=True)
Lam, kappa = sp.symbols("Lam kappa", real=True)  # Lambda and kappa
rho, p3, pt, p8, q48, q84 = sp.symbols("rho p3 pt p8 q48 q84", real=True)
ALPHA = {1: alpha1, 2: alpha2, 3: alpha3}
```

Symbols for the couplings, $\Lambda$ (named `Lam`, because `lambda` is a word of Python), $\kappa$ and the six parts of the source; `ALPHA` finds the coupling of each $k$.

```python
LHS = [[sp.expand(sum(ALPHA[k] * E[k][h][j] for k in (1, 2, 3))
                  + (Lam if h == j else 0)) for j in range(N)] for h in range(N)]
T = [[sp.Integer(0)] * N for _ in range(N)]
for i, value in enumerate([p3, p3, p3, -rho, pt, pt, pt, p8]):
    T[i][i] = value  # the diagonal of the source
T[3][7], T[7][3] = q48, q84  # the two mixed components x4-x8 and x8-x4
```

`LHS` is the left-hand side $\sum_k\alpha_kE_{(k)}{}^h{}_j + \Lambda\delta^h_j$ of Section 12.8. `T` is the source: zeros, then the diagonal from the list, then the two mixed components (two variables can be set in one line).

```python
off_diagonal_zero = all(LHS[h][j] == 0 for h in range(N) for j in range(N)
                        if h != j)
groups_equal = (LHS[0][0] == LHS[1][1] == LHS[2][2]
                and LHS[4][4] == LHS[5][5] == LHS[6][6])
reproduces(off_diagonal_zero and groups_equal,
           "every off-diagonal left-hand side is 0; four independent components",
           WL, "independent_components")
```

The two facts of the reduction: every off-diagonal left-hand side is zero, and the left-hand sides are equal within the two groups.

```python
e11, e44, e55, e88 = (sp.expand(LHS[i][i] - Lam) for i in (0, 3, 4, 7))
say(f"constraint (x4): {e44} + Lam = -kappa*rho")
say(f"hidden (x8): {e88} + Lam = kappa*p8")
```

The four abbreviations $e_{11}, e_{44}, e_{55}, e_{88}$ (the diagonal without $\Lambda$; a parenthesised generator expression yields the four values, which are unpacked into four names). The constraint and the hidden equation are printed for all three couplings; set $\alpha_2 = \alpha_3 = 0$, $\alpha_1 = 1$ in Out [21] and you read off $3(a_4')^2 + 21H^2$ and $15H^2 - 3(a_4')^2$.

**In [22], the evolution equation.**

```python
F = sp.expand(sp.cancel((e11 - e55) / ad2))  # (e11 - e55)/a4''
report("F(a4')", F)
reproduces(not F.has(ad2) and sp.expand(ad2 * F - (e11 - e55)) == 0,
           "evolution: e11 - e55 = a4'' F(a4') = kappa (p3 - pt)",
           PY, "evolution_factorises")
```

$(e_{11} - e_{55})/a_4''$ is simplified by `sp.cancel`; the result $F$ contains no $a_4''$, and $a_4''F$ gives back $e_{11} - e_{55}$ exactly. Out [22] prints $F$, the polynomial of Section 12.9.

```python
coefficients = sp.Poly(F, ad1, H).coeffs()  # every coefficient must vanish
solutions = sp.solve(coefficients, [alpha1, alpha2, alpha3], dict=True)
reproduces(solutions == [{alpha1: 0, alpha2: 0, alpha3: 0}],
           "F vanishes identically only for alpha1 = alpha2 = alpha3 = 0",
           PY, "evolution_F_not_identically_zero")
```

Read as a polynomial in $a_4'$ and $H$, $F$ has coefficients that depend on the couplings (`.coeffs()` lists them). $F$ is zero for every $a_4'$ and $H$ only if every coefficient is zero; `sp.solve` solves these equations for the couplings and finds only $\alpha_1 = \alpha_2 = \alpha_3 = 0$.

```python
reproduces(sp.expand(e11 + e55 - 2 * e88) == 0,
           "e11 + e55 = 2 e88 identically: the source needs p3 + pt = 2 p8",
           PY, "algebraic_identity")
reproduces(not e44.has(ad2) and not e88.has(ad2),
           "the x4 (constraint) and x8 components contain a4' but not a4''",
           PY, "constraint_and_x8_first_order")
```

The algebraic identity of Section 12.9, and the first-order character of the constraint and of the hidden equation.

**In [23], constraint propagation and the record's equations.**

```python
reproduces(sp.expand(sp.diff(e44, ad1) * ad2 - 3 * ad1 * (e11 - e55)) == 0,
           "d/dx4 e44 = 3 a4' (e11 - e55) (constraint propagation)",
           PY, "bianchi_x4")
```

$e_{44}$ depends on $x_4$ only through $a_4'$, so by the chain rule its derivative with respect to $x_4$ is $(\partial e_{44}/\partial a_4')\,a_4''$, written `sp.diff(e44, ad1) * ad2`. It must equal $3a_4'(e_{11} - e_{55})$: the identity of Section 12.10.

```python
general = equations_json["generalSource"]
NAMES_RECORD = {"ad1": ad1, "ad2": ad2, "H": H, "alpha1": alpha1, "alpha2": alpha2,
                "alpha3": alpha3, "Lam": Lam, "kappa": kappa, "rho": rho, "p3": p3,
                "pt": pt, "p8": p8, "AA": A}


def parse_equation(text):
    left, right = text.split(" == ")
    return sp.expand(parse(left, NAMES_RECORD) - parse(right, NAMES_RECORD))
```

The record's general equations are read; `NAMES_RECORD` maps every name used in the record to our symbols (the record writes the slope as `AA`). `parse_equation` splits a text `left == right` at the equality sign and returns left minus right (docstring left out).

```python
mine = {"constraint_x4": e44 + Lam + kappa * rho,
        "space_x1_eq_x2_eq_x3": e11 + Lam - kappa * p3,
        "extraTime_x5_eq_x6_eq_x7": e55 + Lam - kappa * pt,
        "hidden_x8": e88 + Lam - kappa * p8,
        "evolution_x1_minus_x5": ad2 * F - kappa * (p3 - pt),
        "algebraic_condition": p3 + pt - 2 * p8}
same = all(sp.expand(parse_equation(general[key]["input"]) - value) == 0
           for key, value in mine.items())
same = same and sp.expand(parse(general["evolution_F"]["input"], NAMES_RECORD)
                          - F) == 0
reproduces(same, "the six equations and F equal the record a4-equations.json",
           PY, "json_general_source_equations")
```

The notebook's own six equations, each written as left minus right under the record's key, are compared with the record's, and so is $F$.

**In [24], figure 4: the factor F.**

```python
F_numeric = sp.lambdify((ad1, alpha1, alpha2, alpha3), F.subs(H, 1), "numpy")
u = np.linspace(-3.0, 3.0, 601)  # a4'/H
cases = [(1, 0.0, 0.0, "Einstein: $\\alpha_1=1$"),
         (1, 0.005, 0.0, "$\\alpha_2H^2=0.005$"),
         (1, 0.01, 0.0, "$\\alpha_2H^2=0.01$"),
         (1, 0.02, 0.0, "$\\alpha_2H^2=0.02$"),
         (1, 0.01, 0.0005, "$\\alpha_2H^2=0.01$, $\\alpha_3H^4=0.0005$")]
```

`sp.lambdify` turns the exact formula (with $H = 1$) into a fast numpy function of $a_4'$ and the three couplings. `u` holds 601 values of $a_4'/H$. `cases` lists five sets of couplings with their legend labels.

```python
fig, ax = plt.subplots()
for a1, a2, a3, label in cases:
    values = F_numeric(u, a1, a2, a3) * np.ones_like(u) / 2
    ax.plot(u, values, label=label)
for a2 in (0.005, 0.01, 0.02):  # the zeros of F for Gauss-Bonnet gravity
    root = np.sqrt((1 - 40 * a2) / (24 * a2))
    ax.plot([-root, root], [0, 0], "o", color="black", markersize=4)
ax.axhline(0.0, color="black", linewidth=0.8)
```

For each case $F/2$ is computed on the whole array and drawn. In Einstein gravity $F = 2$ does not depend on $a_4'$, but the function still returns an array of 601 values, all equal to 2: the formula that `sp.lambdify` turned into Python contains terms such as `720*ad1**4*alpha3`, and with `alpha3` equal to `0.0` such a term is the array `u**4` times zero. Multiplying by `np.ones_like(u)` (an array of ones of the same length) is therefore only a safeguard: a formula with no $a_4'$ left in it (for example after a simplification) would make the function return the single number 2, and the factor would turn that into an array of the right length as well. The second loop marks the two zeros $\pm\sqrt{(1 - 40\alpha_2)/(24\alpha_2)}$ of each Gauss-Bonnet curve (Section 12.9) with black dots; `ax.axhline` draws the horizontal line $F = 0$.

```python
ax.set_xlabel("$a_4'/H$")
ax.set_ylabel("$F(a_4')/2$")
ax.set_title("The factor $F$ of the evolution equation $a_4''F = \\kappa(p_3-p_t)$")
ax.legend(fontsize=8)
save_figure(fig, "evolution_factor",
            ...)
```

Labels, title, legend and `save_figure`. **What the figure shows.** In Einstein gravity $F/2 = 1$ everywhere. With a positive Gauss-Bonnet coupling $F$ falls like a downward parabola and crosses zero at the black dots, sooner for larger $\alpha_2$; beyond the dots the evolution equation changes sign, and at the dots it cannot be solved for $a_4''$ (Notebook 12c, section 12 of the notebook, integrates into such a point). The third-order coupling adds a positive $(a_4')^4$ term that lifts the curve again.

**In [25], the conservation law of a general source.**

```python
source = {name: sp.Function(name)(x4, z)
          for name in ("rho", "p3", "pt", "p8", "q48", "q84")}  # f(x4, z)
Tgeneral = [[sp.Integer(0)] * N for _ in range(N)]
for i, name in enumerate(["p3", "p3", "p3", "rho", "pt", "pt", "pt", "p8"]):
    Tgeneral[i][i] = source[name]
Tgeneral[3][3] = -source["rho"]  # T^x4_x4 = -rho
Tgeneral[3][7], Tgeneral[7][3] = source["q48"], source["q84"]
divT = divergence(Tgeneral)
```

Now the six parts of the source are unknown functions of $x_4$ and $z$ (so of $x_8$), made with `sp.Function(name)(x4, z)`. The tensor is filled as in In [21] (the time entry is first set to $\rho$ by the loop and then corrected to $-\rho$), and its divergence is computed with the function of In [19].

```python
a4p = sp.Derivative(a4, x4)  # a4' as a derivative, for the comparison
expect_x4 = (-d(source["rho"], 3) - 3 * a4p * (source["p3"] - source["pt"])
             + d(source["q84"], 7) - 6 * H * sp.tan(z) * source["q84"])
expect_x8 = (d(source["p8"], 7) + d(source["q48"], 3)
             + 3 * H * sp.cot(z) * (2 * source["p8"] - source["p3"] - source["pt"]))
```

The two expected components of Section 12.10, written with the function `d` (so that $\partial_8 = 6H\,\partial_z$ is used consistently) and with $a_4'$ as a derivative.

```python
reproduces(clean(divT[3] - expect_x4) == 0, "nabla_mu T^mu_x4 as in the record",
           EMT, "divergence_x4_component")
reproduces(clean(divT[7] - expect_x8) == 0, "nabla_mu T^mu_x8 as in the record",
           EMT, "divergence_x8_component")
reproduces(all(divT[n] == 0 for n in (0, 1, 2, 4, 5, 6)),
           "nabla_mu T^mu_nu = 0 identically for the six other nu",
           PY, "conservation_components")
```

The $x_4$ and $x_8$ components equal the expected ones, and the six others vanish.

**In [26], Einstein gravity: no vacuum and the null energy condition.**

```python
EINSTEIN = {alpha1: 1, alpha2: 0, alpha3: 0}
null_x8 = sp.expand((e88 - e44).subs(EINSTEIN))  # kappa (rho + p8)
report("Einstein: kappa (rho + p8)", null_x8)
reproduces(sp.expand(null_x8 + 6 * ad1 ** 2 + 6 * H ** 2) == 0,
           "Einstein: kappa (rho + p8) = -6 (a4'^2 + H^2) < 0",
           PY, "einstein_null_energy_x8")
```

From the constraint $\kappa\rho = -(e_{44} + \Lambda)$ and the hidden equation $\kappa p_8 = e_{88} + \Lambda$ follows $\kappa(\rho + p_8) = e_{88} - e_{44}$; with the Einstein couplings this is $-6H^2 - 6(a_4')^2$, the result of Section 12.11.

```python
vacuum = [LHS[i][i].subs(EINSTEIN) for i in (0, 3, 4, 7)]  # T = 0
real_solutions = sp.solve(vacuum, [Lam, ad1, ad2], dict=True)  # ad1, ad2 real
say(f"real solutions of the vacuum equations: {real_solutions}")
```

With $T = 0$ the four left-hand sides must vanish. `sp.solve` looks for $\Lambda$, $a_4'$, $a_4''$; because `ad1` and `ad2` were declared real, it returns only real solutions, and there are none (`[]`).

```python
w1, w2 = sp.symbols("w1 w2")  # a4' and a4'' again, now allowed to be complex
as_complex = [value.subs({ad1: w1, ad2: w2}) for value in vacuum]
complex_solutions = sorted(sp.solve(as_complex, [Lam, w1, w2], dict=True), key=str)
say(f"solutions when a4' = w1 and a4'' = w2 may be complex: {complex_solutions}")
imaginary = all(not solution[w1].is_real for solution in complex_solutions)
reproduces(real_solutions == [] and len(complex_solutions) == 2 and imaginary,
           "Einstein: no real vacuum solution for H > 0 and any Lambda",
           LEAD, "no_vacuum_for_H_positive")
```

To see what the equations would want, $a_4'$ and $a_4''$ are replaced by symbols without the property real. Now sympy finds exactly two solutions, $\Lambda = -18H^2$, $a_4' = \pm iH$, $a_4'' = 0$ (sorted by their printed text, so that the order is the same in every run). Both slopes are imaginary (`.is_real` is false), as derived in Section 12.11.

```python
einstein_record = equations_json["einstein"]
mine_einstein = {"constraint_x4": e44.subs(EINSTEIN) + Lam + kappa * rho,
                 "hidden_x8": e88.subs(EINSTEIN) + Lam - kappa * p8,
                 "evolution": 2 * ad2 - kappa * (p3 - pt)}
same = all(sp.expand(parse_equation(einstein_record[key]["input"]) - value) == 0
           for key, value in mine_einstein.items())
reproduces(same, "the Einstein equations equal the record", PY, "json_einstein")
```

The Einstein constraint, hidden equation and evolution equation are compared with the record's.

**In [27], figure 5: why there is no vacuum.**

```python
u = np.linspace(-3.0, 3.0, 301)  # a4'/H
lam_constraint = -(3 * u ** 2 + 21)  # Lambda/H^2 that the x4 equation needs
lam_hidden = 3 * u ** 2 - 15  # Lambda/H^2 that the x8 equation needs
fig, ax = plt.subplots()
ax.plot(u, lam_constraint, label="$\\Lambda$ needed by the constraint ($x_4$)")
ax.plot(u, lam_hidden, label="$\\Lambda$ needed by the hidden equation ($x_8$)")
ax.fill_between(u, lam_constraint, lam_hidden, color="grey", alpha=0.25,
                label="gap $6(a_4')^2+6H^2=-\\kappa(\\rho+p_8)$")
```

With $\rho = 0$ the constraint needs $\Lambda = -(3(a_4')^2 + 21H^2)$, and with $p_8 = 0$ the hidden equation needs $\Lambda = 3(a_4')^2 - 15H^2$. Both are drawn against $a_4'/H$; `ax.fill_between` shades the region between them in grey (25 per cent opaque).

```python
ax.set_xlabel("$a_4'/H$")
ax.set_ylabel("$\\Lambda/H^2$")
ax.set_title("Einstein gravity: the vacuum equations have no common solution")
ax.legend(fontsize=8, loc="upper center")  # the empty area above the curves
save_figure(fig, "no_vacuum_gap",
            ...)
```

Labels, title, the legend placed in the empty upper middle, and `save_figure`. **What the figure shows.** The two curves never meet: the lower one is never above $-21H^2$, the upper one never below $-15H^2$. Their vertical distance, $6(a_4')^2 + 6H^2$, is at its smallest, $6H^2$, at $a_4' = 0$; it is exactly $-\kappa(\rho + p_8)$, the violation of the null energy condition.

**In [28], the linear member.**

```python
reproduces(sp.expand((e11 - e88).subs(LINEAR)) == 0
           and sp.expand((e55 - e88).subs(LINEAR)) == 0,
           "linear member: p3 = pt = p8 = p (any alpha_k)",
           PY, "linear_member_equal_pressures")
```

With $a_4' = AH$, $a_4'' = 0$ (the dictionary `LINEAR` of In [18]) the 3-space, extra-time and hidden left-hand sides are equal, so the three pressures are equal, for every coupling.

```python
rho_linear = sp.expand(-(e44 + Lam).subs(LINEAR) / kappa)  # from the constraint
p_linear = sp.expand((e88 + Lam).subs(LINEAR) / kappa)  # from the hidden equation
say(f"kappa rho = {sp.expand(kappa * rho_linear)}")
say(f"kappa p = {sp.expand(kappa * p_linear)}")
```

The required $\rho$ and $p$ follow from the constraint and the hidden equation; $\kappa\rho$ and $\kappa p$ are printed: the general formulas of Section 12.12.

```python
check(not rho_linear.has(x4) and not p_linear.has(x4),
      "linear member: rho and p are constants")
check(sp.expand(rho_linear.subs(A, -A) - rho_linear) == 0
      and sp.expand(p_linear.subs(A, -A) - p_linear) == 0,
      "rho and p are even in A: A -> -A is a symmetry (deflation is a choice)")
```

Neither contains $x_4$, so both are constants; and replacing $A$ by $-A$ changes neither: deflation is a choice of sign.

**In [29], the vacuum factor.**

```python
V = sp.expand(sp.cancel((e44 - e88).subs(LINEAR) / (6 * (A ** 2 + 1) * H ** 2)))
report("vacuum factor V", V)
reproduces(V.is_polynomial(A) and sp.expand(6 * (A ** 2 + 1) * H ** 2 * V
                                             - (e44 - e88).subs(LINEAR)) == 0,
           "e44 - e88 = 6 (A^2 + 1) H^2 V with a polynomial V",
           PY, "linear_member_vacuum_factor")
```

$e_{44} - e_{88} = -\kappa(\rho + p)$ is divided by $6(A^2 + 1)H^2$; the quotient $V$ is a polynomial in $A$ (no remainder), printed in the RESULT line.

```python
V_gauss_bonnet = sp.expand(V.subs({alpha1: 1, alpha3: 0}))
reproduces(sp.expand(V_gauss_bonnet - (1 - 8 * alpha2 * H ** 2 * (A ** 2 + 5))) == 0,
           "Gauss-Bonnet: V = 1 - 8 alpha2 H^2 (A^2 + 5)",
           PY, "einstein_gauss_bonnet_vacuum_linear")
V_any = V.subs(A, ad1 / H)  # the same polynomial with A H -> a4'
check(sp.expand((e88 - e44) + 6 * (ad1 ** 2 + H ** 2) * V_any) == 0,
      "for every a4: kappa (rho + p8) = -6 (a4'^2 + H^2) V(a4')")
```

For Einstein-Gauss-Bonnet gravity $V = 1 - 8\alpha_2H^2(A^2 + 5)$. Because $e_{44}$ and $e_{88}$ contain no $a_4''$, the same factorisation holds for every history once $AH$ is replaced by $a_4'$: the last check (Section 12.11).

```python
linear_record = equations_json["linearMember"]
same = (sp.expand(parse(linear_record["rho"]["input"], NAMES_RECORD) - rho_linear)
        == 0
        and sp.expand(parse(linear_record["p"]["input"], NAMES_RECORD) - p_linear)
        == 0
        and sp.expand(parse(linear_record["vacuumFactor"]["input"], NAMES_RECORD)
                      - V) == 0)
reproduces(same, "rho, p and V of the linear member equal the record",
           PY, "json_linear_member")
```

$\rho$, $p$ and $V$ are compared with the record's linear-member formulas.

**In [30], the last check.**

```python
figure_names = ["12a_1_riemann_matrix.png", "12a_2_einstein_components.png",
                "12a_3_lovelock_heat_maps.png", "12a_4_evolution_factor.png",
                "12a_5_no_vacuum_gap.png"]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_names),
      "all five figure files exist")
all_checks_passed()
```

The five figure files must exist, and the last line prints ALL 59 CHECKS PASSED (notebook 12a): 4 checks in In [2], 2 in In [4], 2 in In [5], 5 in In [8], 4 in In [12], 1 in In [14], 10 in In [16], 4 in In [17], 3 in In [18], 3 in In [19], 1 in In [21], 4 in In [22], 2 in In [23], 3 in In [25], 3 in In [26], 3 in In [28], 4 in In [29] and 1 in In [30].

### 12.17 Example: the source that the linear member requires

The second notebook takes the field equations from the record and asks, for the linear member $a_4 = AHx_4 + a_0$, what source they require, as a function of the slope $A$, of the cosmological constant and of the Lovelock couplings. It draws the signs of $\rho$ and $p$, shows that a positive energy density in Einstein gravity comes only with $w < -1$, finds the Gauss-Bonnet and third-order vacua, and writes the two conditions that a homogeneous condensate of dirac16complex00 must meet to be the source. It runs in about 15 seconds, prints 24 PASS lines and draws eight figures.

<!-- NOTEBOOK 12b -->

### 12.20 Line-by-line walk-through of Notebook 12b

The notebook has 15 code cells, In [1] to In [15].

**In [1], the set-up cell.** It is the set-up cell of Notebook 12a, word for word, except for two things: the comment lines at the top hold the run instructions of Notebook 12b (Section 12.18), and the line `NOTEBOOK_ID = "12b"` names this notebook. Every line is explained in Section 12.16 under In [1]; the cell prints its one line, Set-up of notebook 12b complete.

**In [2], the Revision records.** The first lines are those of In [2] of Notebook 12a: the imports of `contextlib` and `io`, the short names `PY`, `WL`, `LEAD` and `EQUATIONS` of four record files, and the three helpers `read_json`, `record_verdict` and `reproduces` (Section 12.16, In [2]). New are the last three lines:

```python
record = read_json(EQUATIONS)
title = record["title"]  # the title stored in the record
say(f"read {EQUATIONS}: {title}")
```

The record of the field equations is read once into the dictionary `record`, which the later cells use; its title is printed to show which file was read.

**In [3], the required source for every coupling.**

```python
import numpy as np  # arrays of numbers for the plots
import sympy as sp  # exact algebra with symbols

H = sp.symbols("H", positive=True)  # the constant H of the metric
A = sp.symbols("A", real=True)  # the slope of the linear member
ad1, ad2 = sp.symbols("ad1 ad2", real=True)  # a4' and a4''
alpha1, alpha2, alpha3 = sp.symbols("alpha1 alpha2 alpha3", real=True)
Lam, kappa = sp.symbols("Lam kappa", real=True)  # Lambda and kappa
NAMES = {"ad1": ad1, "ad2": ad2, "H": H, "AA": A, "alpha1": alpha1,
         "alpha2": alpha2, "alpha3": alpha3, "Lam": Lam, "kappa": kappa}
```

The imports and symbols as in Notebook 12a; `NAMES` tells the parser which names of the record mean which symbols (the record calls the slope `AA`).

```python
def parse(text):
    return sp.sympify(text.replace("^", "**"), locals=NAMES)
```

`parse` turns a formula of the record, written in the Wolfram Language, into a sympy expression: the power sign `^` becomes `**` and `sp.sympify` reads the text (docstring left out).

```python
ALPHA = {1: alpha1, 2: alpha2, 3: alpha3}
lovelock = record["lovelockTensors"]
side = {key: sum(ALPHA[k] * parse(lovelock[f"E{k}"][key]["input"]) for k in (1, 2, 3))
        for key in ("x1x1", "x4x4", "x5x5", "x8x8")}  # sum_k alpha_k E_(k)
```

For each of the four distinct diagonal components the dictionary comprehension forms $\sum_k\alpha_kE_{(k)}$ from the record's three tensors: `side["x4x4"]` is $e_{44}$ of Section 12.8, and so on.

```python
LINEAR = {ad1: A * H, ad2: 0}  # a4' = A H, a4'' = 0
kappa_rho = sp.expand(-(side["x4x4"] + Lam).subs(LINEAR))
kappa_p3 = sp.expand((side["x1x1"] + Lam).subs(LINEAR))
kappa_pt = sp.expand((side["x5x5"] + Lam).subs(LINEAR))
kappa_p8 = sp.expand((side["x8x8"] + Lam).subs(LINEAR))
say(f"kappa rho = {kappa_rho}")
say(f"kappa p8 = {kappa_p8}")
```

The linear member is substituted, and the four field equations of Section 12.8 are solved for the source: $\kappa\rho = -(e_{44} + \Lambda)$, $\kappa p_3 = e_{11} + \Lambda$, and so on. Out [3] prints $\kappa\rho$ and $\kappa p_8$: the general formulas of Section 12.12.

**In [4], equal pressures and the symmetry A to minus A.**

```python
reproduces(sp.expand(kappa_p3 - kappa_p8) == 0 and sp.expand(kappa_pt - kappa_p8) == 0,
           "linear member: p3 = pt = p8 = p", PY, "linear_member_equal_pressures")
kappa_p = kappa_p8  # the common pressure, times kappa
```

The three pressures agree for every coupling; the common value is named `kappa_p`.

```python
linear_record = record["linearMember"]
same = (sp.expand(kappa * parse(linear_record["rho"]["input"]) - kappa_rho) == 0
        and sp.expand(kappa * parse(linear_record["p"]["input"]) - kappa_p) == 0)
reproduces(same, "kappa rho and kappa p equal the record", PY, "json_linear_member")
```

The record stores $\rho$ and $p$ themselves (divided by $\kappa$); multiplied by `kappa` they must equal the notebook's $\kappa\rho$ and $\kappa p$.

```python
check(sp.expand(kappa_rho.subs(A, -A) - kappa_rho) == 0
      and sp.expand(kappa_p.subs(A, -A) - kappa_p) == 0,
      "A -> -A leaves rho and p unchanged: deflation is a choice of sign")
reproduces(sp.expand(sp.diff(kappa_rho, alpha1) + 3 * H ** 2 * (A ** 2 + 7)) == 0,
           "the alpha1 part of kappa rho is -3 H^2 (A^2 + 7)",
           LEAD, "einstein_linear_rho_alpha1")
```

Replacing $A$ by $-A$ changes nothing (Section 12.12). The part of $\kappa\rho$ that multiplies $\alpha_1$ is its derivative with respect to $\alpha_1$ (the formula is linear in the couplings); it must be $-3H^2(A^2 + 7)$, as the lead's independent computation found.

**In [5], Einstein gravity.**

```python
EINSTEIN = {alpha1: 1, alpha2: 0, alpha3: 0}
rho_e = sp.expand(kappa_rho.subs(EINSTEIN))  # kappa rho in Einstein gravity
p_e = sp.expand(kappa_p.subs(EINSTEIN))  # kappa p in Einstein gravity
report("Einstein: kappa rho", rho_e)
report("Einstein: kappa p", p_e)
```

The Einstein couplings are substituted and $\kappa\rho = -3A^2H^2 - 21H^2 - \Lambda$ and $\kappa p = -3A^2H^2 + 15H^2 + \Lambda$ are printed.

```python
same = (sp.expand(kappa * parse(linear_record["rhoEinstein"]["input"]) - rho_e) == 0
        and sp.expand(kappa * parse(linear_record["pEinstein"]["input"]) - p_e) == 0
        and sp.expand(kappa * parse(linear_record["rhoPlusPEinstein"]["input"])
                      - (rho_e + p_e)) == 0)
reproduces(same and sp.expand(rho_e + p_e + 6 * (1 + A ** 2) * H ** 2) == 0,
           "Einstein: kappa (rho + p) = -6 (1 + A^2) H^2 < 0", PY,
           "json_linear_member")
```

The three Einstein formulas of the record ($\rho$, $p$, $\rho + p$) are compared, and the sum $\kappa(\rho + p) = -6(1 + A^2)H^2$ is checked.

```python
UNITS = {H: 1, Lam: 0, A: 1}
rho_1, p_1 = rho_e.subs(UNITS), p_e.subs(UNITS)
report("Einstein, Lambda = 0, A = 1: kappa rho", rho_1, "H^2")
report("Einstein, Lambda = 0, A = 1: kappa p", p_1, "H^2")
report("Einstein, Lambda = 0, A = 1: w = p/rho", sp.Rational(p_1, rho_1))
check(rho_1 == -24 and p_1 == 12, "A = 1, Lambda = 0: kappa rho = -24, kappa p = 12")
```

The canonical history $A = 1$ without cosmological constant, in units $H = 1$: $\kappa\rho = -24$, $\kappa p = 12$, and the exact fraction `sp.Rational(p_1, rho_1)` $= -1/2$.

**In [6], figure 1: the Einstein source against A.**

```python
rho_f = sp.lambdify((A, Lam), rho_e.subs(H, 1), "numpy")  # numbers from formulas
p_f = sp.lambdify((A, Lam), p_e.subs(H, 1), "numpy")
a_values = np.linspace(-3.0, 3.0, 301)
```

`sp.lambdify` makes numpy functions of $A$ and $\Lambda$ from the exact formulas with $H = 1$; `a_values` holds 301 slopes from $-3$ to 3.

```python
fig, ax = plt.subplots()
ax.axvspan(0, 3, color="tab:green", alpha=0.08)  # the deflating half, A > 0
ax.plot(a_values, rho_f(a_values, 0.0), label="$\\kappa\\rho/H^2$")
ax.plot(a_values, p_f(a_values, 0.0), label="$\\kappa p/H^2$")
ax.plot(a_values, rho_f(a_values, 0.0) + p_f(a_values, 0.0), ":", color="black",
        label="$\\kappa(\\rho+p)/H^2=-6(1+A^2)$")
ax.axhline(0.0, color="black", linewidth=0.8)
```

`ax.axvspan(0, 3, ...)` shades the vertical strip $0 < A < 3$ in a faint green: the deflating half. The three curves are $\kappa\rho$, $\kappa p$ and their sum (dotted, `":"`) at $\Lambda = 0$; `axhline` draws the zero line.

```python
ax.text(1.5, 15, "$A>0$: extra times deflate", ha="center", fontsize=9)
ax.text(-1.5, 15, "$A<0$: extra times inflate", ha="center", fontsize=9)
ax.set_xlabel("slope $A$ of $a_4 = AHx_4 + a_0$")
ax.set_ylabel("required source (units of $H^2/\\kappa$)")
ax.set_title("Einstein gravity, $\\Lambda = 0$: the source of the linear member")
ax.legend(fontsize=8, loc="lower center")
save_figure(fig, "einstein_source",
            ...)
```

`ax.text(x, y, text, ...)` writes a text at the point $(x, y)$ of the plot; the two texts name the halves. Labels, title, legend and `save_figure` as before. **What the figure shows.** Every curve is symmetric about $A = 0$: the deflating half is the mirror image of the inflating half. The energy density is a downward parabola that never rises above $-21H^2/\kappa$; the pressure is positive for $|A| < \sqrt5$; their sum lies below zero everywhere.

**In [7], figure 2: the signs of rho and p.**

```python
a_grid, lam_grid = np.meshgrid(np.linspace(-3, 3, 241), np.linspace(-60, 30, 241))
rho_grid = rho_f(a_grid, lam_grid)
p_grid = p_f(a_grid, lam_grid)
region = np.where(rho_grid > 0, 0, np.where(p_grid < 0, 1, 2))  # three regions
```

`np.meshgrid` makes two 241 by 241 arrays that together hold every point of a grid in the plane of $A$ (from $-3$ to 3) and $\Lambda/H^2$ (from $-60$ to 30); the functions of In [6] evaluate $\kappa\rho$ and $\kappa p$ at all of them at once. `np.where(condition, x, y)` takes `x` where the condition holds and `y` elsewhere; the nested use labels each point 0 ($\rho > 0$), 1 ($\rho \le 0$, $p < 0$) or 2 ($\rho \le 0$, $p \ge 0$).

```python
fig, ax = plt.subplots()
colours = matplotlib.colors.ListedColormap(["#f4a582", "#d1e5f0", "#92c5de"])
ax.pcolormesh(a_grid, lam_grid, region, cmap=colours, shading="auto")
ax.plot(a_values, -(21 + 3 * a_values ** 2), color="black",
        label="$\\rho = 0$: $\\Lambda = -(21+3A^2)H^2$")
ax.plot(a_values, 3 * a_values ** 2 - 15, "--", color="black",
        label="$p = 0$: $\\Lambda = (3A^2-15)H^2$")
```

`ListedColormap` makes a colour map of three colours (written as hexadecimal colour codes), one per region, and `ax.pcolormesh` colours the grid with it. The solid curve is the border $\rho = 0$, the dashed one the border $p = 0$ (Section 12.12).

```python
ax.text(0, -50, "$\\rho > 0$, $p < 0$: $w < -1$", ha="center")
ax.text(0, -18, "$\\rho < 0$, $p < 0$", ha="center")
ax.text(0, 5, "$\\rho < 0$, $p > 0$", ha="center")
ax.set_xlim(-3, 3)
ax.set_ylim(-60, 30)
ax.set_xlabel("slope $A$")
ax.set_ylabel("$\\Lambda/H^2$")
ax.set_title("Einstein gravity: the signs of the required $\\rho$ and $p$")
ax.legend(fontsize=8, loc="upper center")
save_figure(fig, "source_regions",
            ...)
```

Three texts name the regions; `set_xlim` and `set_ylim` fix the ranges of the axes. **What the figure shows.** Below the solid curve the energy density is positive, but there the pressure is negative and $w < -1$. Above the dashed curve the pressure is positive and the energy density negative. In the band between both are negative. No colour stands for "both positive", and since the two curves never touch, no point is a vacuum.

**In [8], figure 3: positive energy forces w below minus 1.**

```python
w_e = sp.simplify(p_e / rho_e)  # w = p/rho in Einstein gravity
say(f"Einstein: w = p/rho = {w_e}")
check(sp.simplify(w_e + 1 - (rho_e + p_e) / rho_e) == 0,
      "w + 1 = (rho + p)/rho, so rho > 0 and rho + p < 0 give w < -1")
```

The equation of state $w = p/\rho$ is printed, and the identity $w + 1 = (\rho + p)/\rho$ (add $\rho/\rho = 1$ to $p/\rho$) is checked; with $\rho > 0$ and $\rho + p < 0$ it gives $w + 1 < 0$.

```python
fig, ax = plt.subplots()
for lam in (-30.0, -40.0, -60.0):
    rho_values = rho_f(a_values, lam)
    keep = rho_values > 1.0  # where the energy density is clearly positive
    w_values = np.where(keep, p_f(a_values, lam) / np.where(keep, rho_values, 1.0),
                        np.nan)  # nan: not drawn
    ax.plot(a_values, w_values, label=f"$\\Lambda = {lam:.0f}\\,H^2$")
    check(np.nanmax(w_values) < -1.0, f"Lambda = {lam:.0f} H^2: w < -1 where rho > 0")
```

For three cosmological constants the energy density is computed on the 301 slopes; `keep` is an array of true and false values that marks where $\kappa\rho > 1$ (clearly positive). There $w = p/\rho$ is computed; elsewhere `np.nan` (not a number) is stored, which matplotlib does not draw. The inner `np.where(keep, rho_values, 1.0)` avoids a division by a value near zero outside the kept points. `np.nanmax` is the largest value that is not `nan`; it must be below $-1$.

```python
ax.axhline(-1.0, color="black", linewidth=0.8)
ax.set_ylim(-6, 0)
ax.set_xlabel("slope $A$")
ax.set_ylabel("$w = p/\\rho$")
ax.set_title("Einstein gravity: where $\\rho > 0$ the source has $w < -1$")
ax.legend(fontsize=8)
save_figure(fig, "phantom_w",
            ...)
```

The line $w = -1$, the range of the vertical axis, labels, legend and `save_figure`. **What the figure shows.** Each curve is drawn only for slopes small enough that $\kappa\rho > H^2$ (for $\Lambda = -30H^2$ the energy density is positive for $|A| < \sqrt3$, from $21 + 3A^2 < 30$), and each lies entirely below $w = -1$: a positive energy density of the author's metric is always phantom.

**In [9], figure 4: the Gauss-Bonnet coupling.**

```python
reproduces(sp.expand(sp.diff(kappa_rho, alpha2)
                     - H ** 4 * (36 * A ** 4 + 120 * A ** 2 + 420)) == 0,
           "the alpha2 part of kappa rho is H^4 (36 A^4 + 120 A^2 + 420)",
           LEAD, "gauss_bonnet_rho_alpha2")
reproduces(sp.expand(sp.diff(kappa_p, alpha2)
                     - 12 * H ** 4 * (A ** 4 + 14 * A ** 2 - 15)) == 0,
           "the alpha2 part of kappa p is 12 H^4 (A^4 + 14 A^2 - 15)",
           LEAD, "gauss_bonnet_p_alpha2")
```

The parts of $\kappa\rho$ and $\kappa p$ that multiply $\alpha_2$ are compared with the lead's classical Gauss-Bonnet computation.

```python
symbols_numeric = (A, Lam, alpha1, alpha2, alpha3)
rho_l = sp.lambdify(symbols_numeric, kappa_rho.subs(H, 1), "numpy")  # any coupling
p_l = sp.lambdify(symbols_numeric, kappa_p.subs(H, 1), "numpy")
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
for a2 in (0.0, 0.01, 0.025, 0.04):
    label = f"$\\alpha_2H^2 = {a2}$"
    left.plot(a_values, rho_l(a_values, 0, 1, a2, 0), label=label)
    right.plot(a_values, p_l(a_values, 0, 1, a2, 0), label=label)
```

Numpy functions of the slope, $\Lambda$ and the three couplings. A figure with two panels side by side (`left` and `right`); for four values of $\alpha_2H^2$, with $\Lambda = 0$, $\alpha_1 = 1$, $\alpha_3 = 0$, the energy density is drawn on the left and the pressure on the right.

```python
for ax, name in ((left, "\\kappa\\rho/H^2"), (right, "\\kappa p/H^2")):
    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.set_xlabel("slope $A$")
    ax.set_ylabel(f"${name}$")
    ax.legend(fontsize=8)
left.set_title("energy density, $\\Lambda = 0$")
right.set_title("pressure, $\\Lambda = 0$")
save_figure(fig, "gauss_bonnet_source",
            ...)
```

The same zero line, labels and legend for both panels, then titles and `save_figure`.

```python
rho_gb_0 = sp.expand(kappa_rho.subs({alpha1: 1, alpha3: 0, Lam: 0, A: 0}))
check(sp.expand(rho_gb_0 - (420 * alpha2 * H ** 4 - 21 * H ** 2)) == 0,
      "Gauss-Bonnet, Lambda = 0, A = 0: kappa rho = (420 alpha2 H^2 - 21) H^2")
p_gb_1 = [sp.expand(kappa_p.subs({alpha1: 1, alpha3: 0, Lam: 0, A: s}))
          for s in (1, -1)]
check(p_gb_1 == [12 * H ** 2, 12 * H ** 2],
      "Gauss-Bonnet, Lambda = 0, A = +1 or -1: kappa p = 12 H^2 for every alpha2")
```

Two facts that the figure shows, checked exactly: at $A = 0$ the energy density is $(420\alpha_2H^2 - 21)H^2$, and at $A = \pm1$ the pressure is $12H^2$ whatever $\alpha_2$ is, because the Gauss-Bonnet part $12H^4(1 + 14 - 15)$ vanishes there. (These two PASS lines appear after the figure in Out [9], because they are printed after `save_figure`.) **What the figure shows.** The Gauss-Bonnet term adds $\alpha_2H^4(36A^4 + 120A^2 + 420) > 0$ to $\kappa\rho$: for $\alpha_2H^2 = 0.025$ and $0.04$ the energy density becomes positive at large $|A|$ without any cosmological constant. All pressure curves cross at $A = \pm1$.

**In [10], figure 5: the null energy condition and the vacuum curve.**

```python
V = parse(linear_record["vacuumFactor"]["input"])  # the record vacuum factor
reproduces(sp.expand(kappa_rho + kappa_p + 6 * (A ** 2 + 1) * H ** 2 * V) == 0,
           "kappa (rho + p) = -6 (A^2 + 1) H^2 V for every coupling",
           PY, "linear_member_vacuum_factor")
V_gb = sp.expand(V.subs({alpha1: 1, alpha3: 0}))
reproduces(sp.expand(V_gb - (1 - 8 * alpha2 * H ** 2 * (A ** 2 + 5))) == 0,
           "Gauss-Bonnet: V = 1 - 8 alpha2 H^2 (A^2 + 5)",
           PY, "einstein_gauss_bonnet_vacuum_linear")
```

The record's vacuum factor $V$ is read and the factorisation $\kappa(\rho + p) = -6(A^2 + 1)H^2V$ is checked, then its Gauss-Bonnet form.

```python
a_grid, g_grid = np.meshgrid(np.linspace(-3, 3, 241), np.linspace(0.0, 0.06, 241))
V_grid = 1 - 8 * g_grid * (a_grid ** 2 + 5)  # V with H = 1
fig, ax = plt.subplots()
ax.pcolormesh(a_grid, g_grid, np.sign(V_grid), cmap="coolwarm", shading="auto",
              vmin=-2, vmax=2)
```

A grid in the plane of $A$ and $\alpha_2H^2$ (from 0 to 0.06); $V$ on the grid; `np.sign` is $+1$, $0$ or $-1$, and the colour map `coolwarm` with the range $-2$ to 2 shows the two signs in muted blue and red.

```python
g_curve = np.linspace(0.0025, 1 / 40, 200)  # alpha2 H^2 on the vacuum curve
a_curve = np.sqrt((1 - 40 * g_curve) / (8 * g_curve))
ax.plot(a_curve, g_curve, color="black", label="vacuum $V = 0$, $A > 0$ (deflating)")
ax.plot(-a_curve, g_curve, "--", color="black", label="vacuum $V = 0$, $A < 0$")
```

The vacuum curve $A^2 = (1 - 40\alpha_2H^2)/(8\alpha_2H^2)$, drawn for $\alpha_2H^2$ from $0.0025$ to $1/40$, with its deflating branch $A > 0$ (solid) and the mirror branch (dashed).

```python
ax.text(0, 0.006, "$V > 0$: NEC violated", ha="center")
ax.text(0, 0.045, "$V < 0$: NEC holds", ha="center")
ax.set_xlim(-3, 3)
ax.set_xlabel("slope $A$")
ax.set_ylabel("$\\alpha_2 H^2$")
ax.set_title("Einstein-Gauss-Bonnet: the sign of $V$ and the vacuum curve")
ax.legend(fontsize=8, loc="upper right")
save_figure(fig, "null_energy_map",
            ...)
```

Texts naming the two regions (NEC is the null energy condition), labels and `save_figure`. **What the figure shows.** Below the curve $V > 0$ and the required source violates the null energy condition, as in Einstein gravity; above it a sufficiently large Gauss-Bonnet coupling allows a source that satisfies it. On the curve itself a vacuum is possible; the curve reaches $A = 0$ at $\alpha_2H^2 = 1/40$.

**In [11], figure 6: the Gauss-Bonnet vacua.**

```python
A2_vacuum = (1 - 40 * alpha2 * H ** 2) / (8 * alpha2 * H ** 2)  # A^2 on V = 0
GB = {alpha1: 1, alpha3: 0}
rho_gb = sp.expand(kappa_rho.subs(GB))
Lam_vacuum = sp.solve(rho_gb, Lam)[0]  # the Lambda that makes rho = 0
Lam_on_curve = sp.simplify(Lam_vacuum.subs(A ** 2, A2_vacuum))
say(f"Lambda of the vacuum: {Lam_on_curve}")
```

$A^2$ on the vacuum curve; $\kappa\rho$ of Einstein-Gauss-Bonnet gravity; `sp.solve(rho_gb, Lam)` solves $\kappa\rho = 0$ for $\Lambda$ and returns a list with one solution, of which `[0]` takes the first. Then $A^2$ is replaced by its value on the curve (sympy also replaces $A^4 = (A^2)^2$) and the result is simplified: $\Lambda = 720H^4\alpha_2 - 36H^2 + 3/(16\alpha_2)$, printed in Out [11].

```python
p_on_curve = sp.simplify((kappa_p.subs(GB).subs(Lam, Lam_vacuum)).subs(A ** 2,
                                                                   A2_vacuum))
check(p_on_curve == 0,
      "Gauss-Bonnet vacuum: with V = 0 and Lambda from rho = 0, also p = 0")
at_edge = Lam_on_curve.subs({alpha2: sp.Rational(1, 40), H: 1})
report("vacuum at alpha2 H^2 = 1/40: Lambda/H^2", at_edge)
check(at_edge == sp.Rational(-21, 2), "at alpha2 H^2 = 1/40: A = 0, Lambda = -10.5 H^2")
```

With this $\Lambda$ and on the curve the pressure vanishes as well: a true vacuum. At the edge $\alpha_2H^2 = 1/40$ the cosmological constant is exactly $-21/2$ (in units $H^2$).

```python
lam_vac_f = sp.lambdify(alpha2, Lam_on_curve.subs(H, 1), "numpy")
g_curve = np.linspace(0.004, 1 / 40, 200)
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
left.plot(g_curve, np.sqrt((1 - 40 * g_curve) / (8 * g_curve)), label="$A > 0$")
left.plot(g_curve, -np.sqrt((1 - 40 * g_curve) / (8 * g_curve)), "--",
          label="$A < 0$")
left.set_xlabel("$\\alpha_2 H^2$")
left.set_ylabel("slope $A$ of the vacuum")
left.legend(fontsize=8)
right.plot(g_curve, lam_vac_f(g_curve))
right.set_xlabel("$\\alpha_2 H^2$")
right.set_ylabel("$\\Lambda/H^2$ of the vacuum")
fig.suptitle("Einstein-Gauss-Bonnet gravity: the vacuum linear members")
save_figure(fig, "gauss_bonnet_vacuum",
            ...)
```

The two branches $\pm A$ of the vacuum slope on the left and the vacuum's cosmological constant on the right, for $\alpha_2H^2$ from 0.004 to $1/40$. **What the figure shows.** The smaller the Gauss-Bonnet coupling, the faster the vacuum deflates (or inflates) the extra times; at $1/40$ the vacuum is static with $\Lambda = -10.5H^2$.

**In [12], figure 7: the third-order vacuum lines.**

```python
V_one = sp.expand(V.subs({alpha1: 1, H: 1}))  # V with alpha1 = 1, H = 1
alpha3_line = sp.solve(V_one, alpha3)[0]  # alpha3 H^4 on the vacuum line
say(f"vacuum line: alpha3 H^4 = {sp.factor(alpha3_line)}")
check(alpha3_line.subs({A: 1, alpha2: sp.Rational(1, 48)}) == 0,
      "A = 1, alpha2 H^2 = 1/48: the vacuum line passes through alpha3 = 0")
line_f = sp.lambdify((A, alpha2), alpha3_line, "numpy")
```

$V = 0$ is solved for $\alpha_3$ (with $\alpha_1 = H = 1$): for fixed $A$ the solution is linear in $\alpha_2$, a straight line, printed in factored form by `sp.factor`. One point is checked: $A = 1$, $\alpha_2H^2 = 1/48$ gives $\alpha_3 = 0$, because $V = 1 - 8\cdot\tfrac1{48}\cdot 6 = 0$.

```python
g_values = np.linspace(0.0, 0.08, 201)
fig, ax = plt.subplots()
for slope in (0, 1, 2, 3):
    label = "$A = 0$" if slope == 0 else f"$A = \\pm{slope}$"
    ax.plot(g_values, line_f(slope, g_values), label=label)
ax.axhline(0.0, color="black", linewidth=0.8)
ax.set_xlabel("$\\alpha_2 H^2$")
ax.set_ylabel("$\\alpha_3 H^4$")
ax.set_title("Third-order Lovelock gravity: the vacuum lines $V = 0$")
ax.legend(fontsize=8)
save_figure(fig, "third_order_vacua",
            ...)
```

The lines for $A = 0, 1, 2, 3$ (each serves $\pm A$). **What the figure shows.** Each line crosses the axis $\alpha_3 = 0$ at the Gauss-Bonnet vacuum of that slope; with a positive $\alpha_3$ a vacuum exists at larger $\alpha_2$.

**In [13], a condensate of dirac16complex00 as the source.**

```python
m, lam, S = sp.symbols("m lam S", real=True)  # mass, coupling lambda, density S
rho_condensate = m * S + lam * S ** 2 / 2  # rho = m S + U, U = (lambda/2) S^2
p_condensate = lam * S ** 2 / 2  # p = S U' - U
```

The mass $m$, the self-coupling $\lambda$ (named `lam`) and the density $S$ of a condensate; its energy density $mS + U$ and pressure $SU' - U$ with $U = \tfrac\lambda2S^2$, $U' = \lambda S$, so $SU' - U = \lambda S^2 - \tfrac\lambda2S^2 = \tfrac\lambda2S^2$ (the record's formulas, Section 12.26).

```python
condition_rho = sp.expand(kappa * rho_condensate - rho_e)  # = 0
condition_p = sp.expand(kappa * p_condensate - p_e)  # = 0
first = sp.expand(kappa * m * S + 36 * H ** 2 + 2 * Lam)  # kappa m S = -(36 H^2 + 2 L)
second = sp.expand(6 * (A ** 2 + 1) * H ** 2 + kappa * S * (m + lam * S))
reproduces(sp.expand(condition_rho - condition_p - first) == 0
           and sp.expand(condition_rho + condition_p - second) == 0,
           "condensate, Einstein: kappa m S = -(36 H^2 + 2 Lambda) and "
           "6 (A^2 + 1) H^2 = -kappa S (m + lambda S)",
           PY, "condensate_einstein_quadratic_U")
```

The two Einstein equations for this source are `condition_rho = 0` and `condition_p = 0`. Their difference is the first condition and their sum the second; the derivation is written out in Section 12.26.

```python
UNIT = {H: 1, kappa: 1}
S_solution = sp.solve(first.subs(UNIT), S)[0]
A2_solution = sp.expand(sp.solve(second.subs(UNIT), A ** 2)[0].subs(S, S_solution))
say(f"S = {S_solution},  A^2 = {A2_solution}")
```

In units $H = \kappa = 1$ the first condition gives $S = -2(\Lambda + 18)/m$, and the second, solved for $A^2$ with this $S$, gives $A^2$ as a function of $m$, $\lambda$ and $\Lambda$ (printed in Out [13]); for $\Lambda = 0$ it is $5 - 216\lambda/m^2$.

```python
example_1 = A2_solution.subs({m: 5, lam: 0, Lam: 0})
example_2 = A2_solution.subs({m: -15, lam: sp.Rational(25, 6), Lam: 0})
report("m = 5, lambda = 0, Lambda = 0: A^2", example_1)
report("m = -15, lambda = 25/6, Lambda = 0: A^2", example_2)
check(example_1 == 5 and example_2 == 1, "the two worked examples: A^2 = 5 and A^2 = 1")
```

Two worked examples: $m = 5$, $\lambda = 0$ gives $A^2 = 5$; $m = -15$, $\lambda = 25/6$ gives $A^2 = 5 - 216\cdot\tfrac{25}{6}/225 = 5 - 4 = 1$, the slope of the canonical history.

```python
effective = []  # the effective mass M = m + lambda S of each example
for mass, coupling in ((5, 0), (-15, sp.Rational(25, 6))):
    S_value = S_solution.subs({m: mass, Lam: 0})  # the density the example needs
    effective.append(mass + coupling * S_value)
    report(f"m = {mass}, lambda = {coupling}: S and M = m + lambda S",
           f"{S_value}, {effective[-1]}")
check(effective == [5, -5], "the examples need M = 5 (S < 0) and M = -5 (S > 0)")
```

For each example the density it needs ($S = -36/5$ and $12/5$) and the effective mass $M = m + \lambda S$ ($5$ and $-5$) are printed; `effective[-1]` is the last entry of the list.

**In [14], figure 8: the off-diagonal conditions and the slope of a condensate.**

```python
condensate = record["fields"]["dirac16complex00"]
entries = condensate["offDiagonalKinetic"]
bilinears = sorted({term["bilinear"] for entry in entries for term in entry["terms"]})
report("off-diagonal kinetic components of the condensate", len(entries))
report("distinct three-gamma bilinears", len(bilinears))
reproduces(len(entries) == 42 and len(bilinears) == 15,
           "42 off-diagonal components, multiples of 15 three-gamma bilinears",
           WL, "condensate_offdiagonal_are_three_gamma_bilinears")
```

The record lists every nonzero off-diagonal kinetic component of a condensate, each with the bilinear it multiplies. A **set comprehension** (braces) keeps each bilinear once, `sorted` puts them in order: 42 components, 15 distinct three-gamma bilinears.

```python
a2_f = sp.lambdify((m, lam), A2_solution.subs(Lam, 0), "numpy")
fig, ax = plt.subplots()
for mass, upper in ((5, 1.0), (-15, 6.0)):
    lam_values = np.linspace(0.0, upper, 200)
    ax.plot(lam_values, a2_f(mass, lam_values), label=f"$m = {mass}$")
ax.plot([0], [5], "o", color="black")
ax.plot([25 / 6], [1], "s", color="black")
```

$A^2$ as a numpy function of $m$ and $\lambda$ at $\Lambda = 0$, drawn against $\lambda$ for $m = 5$ (up to $\lambda = 1$) and $m = -15$ (up to 6); a circle and a square mark the two worked examples.

```python
arrow = {"arrowstyle": "->"}  # a thin arrow from the text to the point
ax.annotate("$m=5$, $\\lambda=0$: $A^2=5$", (0, 5), (0.5, 5.8), fontsize=8,
            arrowprops=arrow)
ax.annotate("$m=-15$, $\\lambda=25/6$: $A^2=1$", (25 / 6, 1), (3.6, 2.6),
            fontsize=8, arrowprops=arrow)
ax.set_ylim(-4.2, 6.6)
ax.axhline(0.0, color="black", linewidth=0.8)
ax.set_xlabel("self-coupling $\\lambda$ (units $H = \\kappa = 1$)")
ax.set_ylabel("$A^2$ required by the condensate")
ax.set_title("A dirac16complex00 condensate as the source, Einstein, $\\Lambda=0$")
ax.legend(fontsize=8)
save_figure(fig, "condensate_slope",
            ...)
```

`ax.annotate(text, point, text_position, ...)` writes a text with an arrow to a point. **What the figure shows.** Both lines fall linearly, $A^2 = 5 - 216\lambda/m^2$, the line of the light mass $m = 5$ much faster; a real slope exists only while $A^2 \ge 0$, that is $\lambda \le 5m^2/216$.

**In [15], the last check.**

```python
figure_names = ["einstein_source", "source_regions", "phantom_w",
                "gauss_bonnet_source", "null_energy_map", "gauss_bonnet_vacuum",
                "third_order_vacua", "condensate_slope"]
paths = [output_file(f"{FIGURE_FOLDER}/12b_{k}_{name}.png")
         for k, name in enumerate(figure_names, 1)]
check(all(path.is_file() for path in paths), "all eight figure files exist")
all_checks_passed()
```

`enumerate(figure_names, 1)` numbers the names from 1, which gives the eight file names; all must exist. The last line is ALL 24 CHECKS PASSED (notebook 12b): 4 checks in In [4], 2 in In [5], 4 in In [8], 4 in In [9], 2 in In [10], 2 in In [11], 1 in In [12], 3 in In [13], 1 in In [14] and 1 in In [15].

### 12.21 Solving the evolution equation for a prescribed stress

**The idea.** If the anisotropic stress $\Delta = p_3 - p_t$ is known as a function of time (or of the state), the evolution equation $a_4''F(a_4') = \kappa\Delta$ is an **ordinary differential equation** for $a_4(x_4)$, and with the starting values $a_4(0)$ and $a_4'(0)$ it has one solution, which a computer can follow step by step. We prescribe the stress by hand: it is ASSUMED, chosen to see what the equations do. The Revision record constructs no state of either field that produces these stresses, and Section 12.22 recalls why the Kohn-Sham states of the repository are not admissible sources at all.

**A first-order system.** Write $v = a_4'$. Then

$$
\frac{d}{dx_4}a_4 = v,\qquad \frac{d}{dx_4}v = \frac{\kappa\Delta}{F(v)},\qquad \frac{d}{dx_4}(\kappa\rho) = -3v\,\kappa\Delta .
$$

The first line is the definition of $v$, the second the evolution equation divided by $F$, the third the conservation law of Section 12.10. The third is not needed for $a_4$; Notebook 12c integrates it alongside, so that the energy density obtained from conservation can be compared with the one the constraint gives: a numerical test of the Bianchi identity.

**The Runge-Kutta method of fourth order (RK4)**, from Chapter 2: for $dy/dx = f(x, y)$ one step of size $h$ computes $k_1 = f(x, y)$, $k_2 = f(x + h/2, y + hk_1/2)$, $k_3 = f(x + h/2, y + hk_2/2)$, $k_4 = f(x + h, y + hk_3)$ and $y_{\text{new}} = y + \tfrac h6(k_1 + 2k_2 + 2k_3 + k_4)$. Its error after a fixed time shrinks like $h^4$: halving the step divides it by about 16.

**No stress.** With $\Delta = 0$: $a_4'' = 0$, so $a_4' = A H$ is constant and $a_4 = AHx_4 + a_0$: the linear member.

**A pulse of stress (Einstein gravity).** We start on the canonical history ($a_4(0) = 0$, $a_4'(0) = H$; units $H = 1$) and prescribe $\kappa\Delta(x_4) = \kappa\Delta_0\,e^{-((x_4 - x_c)/w)^2}$ with centre $x_c = 3$, width $w = 0.5$ and height $\kappa\Delta_0 = 2/(w\sqrt\pi)$. With $F = 2$:

$$
a_4'(x_4) = 1 + \int_0^{x_4} a_4''(s)\,ds = 1 + \frac{\kappa\Delta_0}{2}\int_0^{x_4} e^{-((s - x_c)/w)^2}\,ds
$$

(the fundamental theorem of calculus, then $a_4'' = \kappa\Delta/2$)

$$
= 1 + \frac{\kappa\Delta_0\,w}{2}\int_{-x_c/w}^{(x_4 - x_c)/w} e^{-t^2}\,dt
$$

(substitution $t = (s - x_c)/w$, $ds = w\,dt$; the limits $s = 0$ and $s = x_4$ become $t = -x_c/w$ and $t = (x_4 - x_c)/w$)

$$
= 1 + \frac{\kappa\Delta_0\,w\sqrt\pi}{4}\Big(\operatorname{erf}\frac{x_4 - x_c}{w} + \operatorname{erf}\frac{x_c}{w}\Big)
$$

(the **error function** $\operatorname{erf}(u) = \tfrac{2}{\sqrt\pi}\int_0^u e^{-t^2}dt$ gives $\int_{u_0}^{u_1}e^{-t^2}dt = \tfrac{\sqrt\pi}{2}(\operatorname{erf}u_1 - \operatorname{erf}u_0)$, and erf is odd, $\operatorname{erf}(-u) = -\operatorname{erf}u$)

$$
= 1 + \tfrac12\Big(\operatorname{erf}\frac{x_4 - x_c}{w} + \operatorname{erf}\frac{x_c}{w}\Big)
$$

($\kappa\Delta_0\,w\sqrt\pi/4 = 2/4 = 1/2$). At $x_4 = 0$ the bracket is zero and $a_4' = 1$. Long after the pulse $\operatorname{erf}((x_4 - x_c)/w) \to 1$, and $\operatorname{erf}(x_c/w) = \operatorname{erf}(6)$ differs from 1 by less than $10^{-15}$, so $a_4' \to 2$: the pulse moves the history from the linear member $A = 1$ to $A = 2$, and the extra times deflate at every time, only faster afterwards. Integrating once more with $\int\operatorname{erf}(t)\,dt = t\operatorname{erf}(t) + e^{-t^2}/\sqrt\pi$ gives $a_4$ exactly (Notebook 12c, In [7]).

**A relaxing stress.** Now the stress depends on the state: $\kappa\Delta = -2\eta\,(a_4' - H)$ with a constant $\eta > 0$, starting on the faster member $a_4'(0) = 2H$ (units $H = 1$). Then

$$
a_4'' = \frac{\kappa\Delta}{2} = -\eta\,(a_4' - 1)
$$

(Einstein, $F = 2$). The excess $u = a_4' - 1$ obeys $u' = a_4'' = -\eta u$ with $u(0) = 1$, whose solution is $u = e^{-\eta x_4}$ (the derivative of $e^{-\eta x_4}$ is $-\eta e^{-\eta x_4}$). So

$$
a_4' = 1 + e^{-\eta x_4},\qquad a_4 = x_4 + \frac{1 - e^{-\eta x_4}}{\eta}
$$

(integrate from 0, with $a_4(0) = 0$). The rate relaxes from $2H$ to $H$; the extra times keep deflating, first at the rate $2H$, later at the rate $H$. The conservation law gives $\kappa\rho' = -3a_4'\kappa\Delta = 6\eta\,a_4'(a_4' - 1) > 0$: the energy density rises. With $\Lambda = 0$ (the value Notebook 12c uses) the constraint gives $\kappa\rho = -3(a_4')^2 - 21H^2$, so $\kappa\rho$ rises from $-33H^2$ (at the rate $2H$, the value of the linear member $A = 2$) towards $-24H^2$ (the value of $A = 1$).

**A constant stress in Einstein-Gauss-Bonnet gravity: the equation breaks down.** With $\alpha_1 = 1$, $\alpha_3 = 0$ and $H = 1$, $F(v) = 2 - 80\alpha_2 - 48\alpha_2v^2$. Define $G(v) = (2 - 80\alpha_2)v - 16\alpha_2v^3$; its derivative is $G'(v) = 2 - 80\alpha_2 - 48\alpha_2v^2 = F(v)$. Then, along a solution with a constant stress $\kappa\Delta$,

$$
\frac{d}{dx_4}G\big(a_4'(x_4)\big) = G'(a_4')\,a_4'' = F(a_4')\,a_4'' = \kappa\Delta
$$

(chain rule, then the evolution equation), and integrating from 0:

$$
G\big(a_4'(x_4)\big) = G\big(a_4'(0)\big) + \kappa\Delta\,x_4 .
$$

The right-hand side grows without limit, but $G$ has a largest value at the **critical rate** $v_c = \sqrt{(2 - 80\alpha_2)/(48\alpha_2)}$, where $G' = F = 0$. So the rate reaches $v_c$ at the finite time

$$
x_4^{\star} = \frac{G(v_c) - G\big(a_4'(0)\big)}{\kappa\Delta},
$$

and there $a_4'' = \kappa\Delta/F$ becomes infinite: beyond $x_4^{\star}$ no solution with a smooth $a_4'$ exists. For $\kappa\Delta = 0.5$ and $a_4'(0) = 1$: $\alpha_2 = 0.005$ gives $v_c = 2.5820$ and $x_4^{\star} = 2.4682$; $\alpha_2 = 0.01$ gives $v_c = 1.5811$ and $x_4^{\star} = 0.4498$ (Notebook 12c, In [13]; Exercise 8 repeats the second by hand). In Einstein gravity ($F = 2$) the same stress simply makes the rate grow linearly, $a_4' = 1 + 0.25x_4$, for ever.

### 12.22 Example: four prescribed histories integrated with RK4

The third notebook programs RK4, tests it, and integrates the evolution equation for the four prescribed stresses of Section 12.21. It compares every numerical history with its exact solution, measures the order of convergence of RK4, compares the energy density from the conservation law with the one from the constraint, and finds the Gauss-Bonnet breakdown at the predicted time. Along every history with the deflating sign the extra times deflate exponentially at every time. At the end it reads the record's verdict on the Kohn-Sham states and recomputes the record's numbers. The record `Revision/field_equations_a4/reports/ks-source-conditions.json` (every one of its checks PASS; Notebook 12c, In [15]) finds that every recorded Kohn-Sham state with a nonzero energy-momentum tensor depends on $x_8$ and violates $p_3 + p_t = 2p_8$, even after integration over $x_8$ (check `ks_integrals_violate_algebraic_condition`). Notebook 12c, In [16], recomputes the record's numbers from the Kohn-Sham table `Revision/kohn_sham/results/ground/emt-integrals.csv` and asserts that they equal the record: of the 75 recorded states, 70 have a nonzero energy-momentum tensor; for these the ratio $(\int p_3 + \int p_t)/(2\int p_8)$, which equals 1 for every admissible source, is nowhere closer to 1 than 0.414328, and for $N = 136$ particles and $\lambda = 0$ it is 0.339767, 0.25969 and 0.239714 at the slices $a_{4,0} = 0, 1, 2$ (COMPUTED from the record's table, equal to the record). So the Kohn-Sham history $a_4 = AHx_4$ of Chapters 14 and 15 is a PRESCRIBED background, not a solution of these equations with the Kohn-Sham source (Chapter 17). The notebook runs in about 15 seconds, prints 30 PASS lines and draws six figures.

<!-- NOTEBOOK 12c -->

### 12.25 Line-by-line walk-through of Notebook 12c

The notebook has 17 code cells, In [1] to In [17].

**In [1], the set-up cell.** As in Notebook 12a (Section 12.16, In [1]), except that the comments hold the run instructions of Notebook 12c (Section 12.23) and `NOTEBOOK_ID = "12c"`.

**In [2], the records and the Lovelock components as functions.**

```python
import contextlib  # redirect_stdout: send printed lines into a buffer
import io  # StringIO: a text buffer in memory
import math  # the error function erf, for an exact solution

import matplotlib.ticker  # control of the tick labels of an axis
import numpy as np  # arrays of numbers
import sympy as sp  # exact algebra, used here only to read the record formulas
```

Besides the modules met before: `math`, Python's module of mathematical functions (it has the error function `math.erf`), and `matplotlib.ticker`, which controls the labels of axis ticks.

```python
PY = "Revision/field_equations_a4/reports/python-a4-report.json"  # sympy record
WL = "Revision/field_equations_a4/reports/wolfram-a4-report.json"  # Wolfram record
EQUATIONS = "Revision/field_equations_a4/a4-equations.json"  # the equations
KS = "Revision/field_equations_a4/reports/ks-source-conditions.json"
```

Short names of four record files; `KS` is the record on the Kohn-Sham sources. The three helpers `read_json`, `record_verdict` and `reproduces` that follow are those of Notebook 12a, In [2] (Section 12.16).

```python
record = read_json(EQUATIONS)
H, ad1, ad2 = sp.symbols("H ad1 ad2", real=True)
a1, a2, a3 = sp.symbols("alpha1 alpha2 alpha3", real=True)
LOCALS = {"H": H, "ad1": ad1, "ad2": ad2, "alpha1": a1, "alpha2": a2, "alpha3": a3}


def from_record(text):
    return sp.sympify(text.replace("^", "**"), locals=LOCALS).subs(H, 1)
```

The record is read; the symbols for $H$, $a_4'$, $a_4''$ and the couplings are made (in this notebook the Python names of the couplings are `a1`, `a2`, `a3`, so that the name `alpha2` stays free for a plain number later); `from_record` parses a formula of the record and sets $H = 1$ (docstring left out).

```python
lovelock = record["lovelockTensors"]
weights = {1: a1, 2: a2, 3: a3}


def lovelock_sum(component):
    return sum(weights[k] * from_record(lovelock[f"E{k}"][component]["input"])
               for k in (1, 2, 3))


e44 = lovelock_sum("x4x4")  # the time component (constraint)
e88 = lovelock_sum("x8x8")  # the hidden component
F_expr = from_record(record["generalSource"]["evolution_F"]["input"])
```

`lovelock_sum` forms $\sum_k\alpha_kE_{(k)}$ for one component of the record. It gives $e_{44}$ and $e_{88}$ of Section 12.8; $F$ is read directly from the record.

```python
rho_side = sp.lambdify((ad1, a1, a2, a3), e44, "numpy")
p8_side = sp.lambdify((ad1, a1, a2, a3), e88, "numpy")
F_of = sp.lambdify((ad1, a1, a2, a3), F_expr, "numpy")
say(f"F(a4') with H = 1: {F_expr}")
EINSTEIN = (1.0, 0.0, 0.0)  # alpha1, alpha2, alpha3 of Einstein gravity
```

Three fast numpy functions of the rate $v = a_4'$ and the couplings: `rho_side` is $e_{44}$ (so $\kappa\rho = -(e_{44} + \Lambda)$), `p8_side` is $e_{88}$ (so $\kappa p_8 = e_{88} + \Lambda$) and `F_of` is $F$. $F$ is printed. `EINSTEIN` is a **tuple** (a fixed list in round brackets) of the Einstein couplings; `F_of(v, *EINSTEIN)` passes its three numbers as three arguments.

**In [3], a test of the functions.**

```python
rates = np.array([-2.0, -0.5, 0.0, 1.0, 3.0])  # a few values of a4'
ok = (np.allclose(F_of(rates, *EINSTEIN), 2.0)
      and np.allclose(rho_side(rates, *EINSTEIN), 3 * rates ** 2 + 21)
      and np.allclose(p8_side(rates, *EINSTEIN), 15 - 3 * rates ** 2))
reproduces(ok, "Einstein: F = 2, E44 = 3 a4'^2 + 21, E88 = 15 - 3 a4'^2 (H = 1)",
           PY, "einstein_components")
```

At five rates the three functions must give the Einstein values of Section 12.9 (`np.allclose` compares arrays up to rounding).

**In [4], the RK4 solver and its test.**

```python
def rk4(rhs, y0, h, steps, stop=None):
    xs = [0.0]
    ys = [np.array(y0, dtype=float)]
    for n in range(steps):
        x, y = xs[-1], ys[-1]
        k1 = rhs(x, y)
        k2 = rhs(x + h / 2, y + h / 2 * k1)
        k3 = rhs(x + h / 2, y + h / 2 * k2)
        k4 = rhs(x + h, y + h * k3)
        xs.append((n + 1) * h)  # (n + 1) h avoids adding up rounding errors
        ys.append(y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4))
        if stop is not None and stop(ys[-1]):
            break
    return np.array(xs), np.array(ys)
```

`rk4` solves $dy/dx = $ `rhs(x, y)` from $x = 0$ with the starting value `y0`, by at most `steps` steps of size `h` (docstring left out). The lists `xs` and `ys` hold the points reached; `[-1]` is the last one. The four lines `k1` to `k4` and the update are the RK4 formulas of Section 12.21, applied to the whole array `y` at once. The new $x$ is computed as $(n + 1)h$ rather than by adding $h$ again and again, which would accumulate rounding errors. If a function `stop` is given and returns true for the new point, `break` ends the loop early. The function returns the points as arrays: `ys[n, 0]` is the first component at step $n$.

```python
x_test, y_test = rk4(lambda x, y: -y, [1.0], 0.05, 20)
error_test = abs(y_test[-1, 0] - math.exp(-1.0))
say(f"y' = -y: RK4 with h = 0.05 gives y(1) = {y_test[-1, 0]:.10f}; "
    f"exact {math.exp(-1.0):.10f}")
check(error_test < 1e-7, "RK4 solves y' = -y to better than 1e-7 with 20 steps")
```

A test with a known answer: $y' = -y$, $y(0) = 1$, whose solution is $e^{-x}$. `lambda x, y: -y` is a one-line function without a name. Twenty steps of 0.05 reach $x = 1$; the result 0.3678794611 differs from $e^{-1} = 0.3678794412$ by $2 \times 10^{-8}$.

**In [5], no stress: the linear member.**

```python
def history(stress, rate0, h, steps, couplings=EINSTEIN, Lam=0.0, stop=None):
    def rhs(x, y):
        push = stress(x, y)  # kappa (p3 - pt) at this time
        return np.array([y[1], push / F_of(y[1], *couplings), -3.0 * y[1] * push])

    rho0 = -(rho_side(rate0, *couplings) + Lam)  # kappa rho at x4 = 0
    return rk4(rhs, [0.0, rate0, rho0], h, steps, stop)
```

`history` integrates the first-order system of Section 12.21 for a given stress function (docstring left out). Inside it, `rhs` is the right-hand side for the state $y = (a_4, v, \kappa\rho)$: $dy_0/dx = v$, $dy_1/dx = \kappa\Delta/F(v)$, $dy_2/dx = -3v\,\kappa\Delta$. The starting energy density is taken from the constraint, $\kappa\rho = -(e_{44} + \Lambda)$ at the starting rate. The defaults are Einstein gravity and $\Lambda = 0$.

```python
def no_stress(x, y):
    return 0.0  # Delta = 0: an isotropic source


linear = {}  # slope A -> (x4, solution)
for slope in (2.0, 1.0, -1.0):  # deflating A = 2, 1 and the mirror image A = -1
    linear[slope] = history(no_stress, slope, 0.01, 300)
    x4, y = linear[slope]
    error = np.max(np.abs(y[:, 0] - slope * x4))  # compare with a4 = A x4
    check(error < 1e-12, f"Delta = 0, A = {slope:g}: a4 = A H x4 exactly")
```

With zero stress, three histories of 300 steps of 0.01 (up to $x_4 = 3$) are integrated, starting at the rates $A = 2$, $1$ and $-1$; `y[:, 0]` is the column of $a_4$ values, which must equal $Ax_4$ (the format `:g` prints 2.0 as 2).

```python
x4, y = linear[1.0]
report("A = 1, Lambda = 0: kappa rho along the history", f"{y[-1, 2]:.6f}", "H^2")
product = np.exp(3 * y[:, 0]) * np.exp(-3 * y[:, 0])  # e^(3 a4) e^(-3 a4)
check(np.max(np.abs(product - 1.0)) < 1e-12,
      "the 7-volume factor e^(3 a4) e^(-3 a4) stays 1")
```

For $A = 1$ the energy density at the end is $-24$, the value of Section 12.12, and the 7-volume factor stays 1.

**In [6], figure 1: the linear histories and the scale factors.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
for slope, style, words in ((2.0, "-", "deflating"), (1.0, "-.", "deflating"),
                            (-1.0, "--", "mirror image")):
    x4, y = linear[slope]
    left.plot(x4, y[:, 0], style, label=f"$A = {slope:g}$ ({words})")
left.set_xlabel("time $x_4$ (units $1/H$)")
left.set_ylabel("$a_4$")
left.set_title("$\\Delta = 0$: $a_4 = AHx_4$")
left.legend(fontsize=8)
```

Two panels. The left one draws the three histories with three line styles (solid, dash-dotted, dashed).

```python
x4, y = linear[1.0]
right.semilogy(x4, np.exp(y[:, 0]), label="3-space $e^{a_4}$ (inflates)")
right.semilogy(x4, np.exp(-y[:, 0]), "--", label="extra times $e^{-a_4}$ (deflate)")
right.semilogy(x4, np.exp(3 * y[:, 0]) * np.exp(-3 * y[:, 0]), ":", color="black",
               label="$e^{3a_4}e^{-3a_4} = 1$")
right.set_xlabel("time $x_4$ (units $1/H$)")
right.set_ylabel("scale factor")
right.set_title("$A = 1$: the scale factors")
right.legend(fontsize=8)
save_figure(fig, "linear_member",
            ...)
```

`semilogy` draws with a logarithmic vertical axis, on which an exponential is a straight line. **What the figure shows.** On the left three straight lines of slopes 2, 1 and $-1$. On the right $e^{a_4}$ rises and $e^{-a_4}$ falls along straight lines of equal and opposite slope, and the product of their cubes is the flat line 1.

**In [7], the pulse.**

```python
X_C, WIDTH = 3.0, 0.5  # the centre and the width of the pulse
PUSH = 2.0 / (WIDTH * math.sqrt(math.pi))  # kappa Delta_0
RATE_START = 1.0  # a4'(0)/H: the canonical deflating history A = 1


def pulse(x, y):
    return PUSH * math.exp(-((x - X_C) / WIDTH) ** 2)  # kappa Delta(x4)
```

The constants of the pulse of Section 12.21 and the stress function itself (it ignores the state `y`).

```python
def exact_pulse(x):
    scale = PUSH * WIDTH * math.sqrt(math.pi) / 4  # = 1/2
    t, t0 = (x - X_C) / WIDTH, -X_C / WIDTH  # the argument now and at x4 = 0

    def antiderivative(s):  # an antiderivative of erf
        return s * math.erf(s) + math.exp(-s * s) / math.sqrt(math.pi)

    rate = RATE_START + scale * (math.erf(t) + math.erf(X_C / WIDTH))
    a4 = RATE_START * x + scale * (WIDTH * (antiderivative(t) - antiderivative(t0))
                                   + x * math.erf(X_C / WIDTH))
    return a4, rate
```

The exact solution (docstring left out): `rate` is the formula for $a_4'$ derived in Section 12.21; `a4` is its integral from 0, in which $\int_0^{x}\operatorname{erf}((s - x_c)/w)\,ds = w\,(\text{antiderivative}(t) - \text{antiderivative}(t_0))$ by the same substitution as before.

```python
x4_pulse, y_pulse = history(pulse, RATE_START, 0.01, 800)
exact = np.array([exact_pulse(x) for x in x4_pulse])  # columns: a4, a4'
error_a4 = np.max(np.abs(y_pulse[:, 0] - exact[:, 0]))
error_rate = np.max(np.abs(y_pulse[:, 1] - exact[:, 1]))
say(f"largest error: a4 {error_a4:.0e}, a4' {error_rate:.0e}")
check(error_a4 < 1e-8 and error_rate < 1e-8,
      "pulse: RK4 (h = 0.01) agrees with the exact solution to 1e-8")
```

800 steps of 0.01 up to $x_4 = 8$; the exact values at the same points; the largest differences are $9 \times 10^{-11}$ for $a_4$ and $10^{-10}$ for $a_4'$ (COMPUTED).

```python
check(np.min(y_pulse[:, 1]) >= 1.0 - 1e-12,
      "the rate a4' never falls below H: the extra times deflate at every time")
report("rate a4'/H after the pulse (x4 = 8)", f"{y_pulse[-1, 1]:.10f}")
check(abs(y_pulse[-1, 1] - 2.0) < 1e-8,
      "after the pulse a4' = 2 H: the deflating linear member A = 2")
```

The rate never falls below 1 (the stress is never negative), and at the end it is 2.0000000000.

**In [8], figure 2: the pulse history in four panels.**

```python
fig, axes = plt.subplots(2, 2, figsize=(10.0, 7.0))
stress_values = np.array([pulse(x, None) for x in x4_pulse])
axes[0, 0].plot(x4_pulse, stress_values)
axes[0, 0].set_ylabel("$\\kappa(p_3 - p_t)$ (units $H^2$)")
axes[0, 0].set_title("the prescribed stress pulse")
```

A 2 by 2 grid of panels; `axes[0, 0]` is the top left one. The stress is evaluated at every time (`None` stands for the unused state) and drawn.

```python
every = slice(0, None, 40)  # every 40th point for the exact markers
axes[0, 1].plot(x4_pulse, y_pulse[:, 1], label="RK4")
axes[0, 1].plot(x4_pulse[every], exact[every, 1], "o", markersize=3, label="exact")
axes[0, 1].set_ylabel("$a_4'/H$")
axes[0, 1].set_title("the rate $a_4'$")
axes[0, 1].legend(fontsize=8)
axes[1, 0].plot(x4_pulse, y_pulse[:, 0], label="RK4")
axes[1, 0].plot(x4_pulse[every], exact[every, 0], "o", markersize=3, label="exact")
axes[1, 0].set_ylabel("$a_4$")
axes[1, 0].set_title("$a_4$")
axes[1, 0].legend(fontsize=8)
```

`slice(0, None, 40)` selects every 40th entry of an array. The top right panel draws the RK4 rate as a line and the exact rate as dots; the bottom left one does the same for $a_4$.

```python
axes[1, 1].semilogy(x4_pulse, np.exp(y_pulse[:, 0]), label="3-space $e^{a_4}$")
axes[1, 1].semilogy(x4_pulse, np.exp(-y_pulse[:, 0]), "--",
                    label="extra times $e^{-a_4}$")
axes[1, 1].set_ylabel("scale factor")
axes[1, 1].set_title("the scale factors")
axes[1, 1].legend(fontsize=8)
for ax in axes[1]:
    ax.set_xlabel("time $x_4$ (units $1/H$)")
fig.tight_layout()
save_figure(fig, "stress_pulse",
            ...)
```

The bottom right panel draws both scale factors on a logarithmic axis; `axes[1]` is the bottom row, whose panels get the label of the time axis; `fig.tight_layout()` spaces the panels so that labels do not overlap. **What the figure shows.** The rate climbs from 1 to 2 while the pulse acts and stays there; $a_4$ bends from slope 1 to slope 2; on the logarithmic axis $e^{-a_4}$ falls along a straight line that becomes twice as steep after the pulse: the extra times deflate at every time.

**In [9], figure 3: the required source and the test of conservation.**

```python
def as_power_of_ten(value):
    mantissa, exponent = f"{value:.0e}".split("e")
    return f"${mantissa} \\times 10^{{{int(exponent)}}}$"
```

A small helper for the caption (docstring left out): the format `.0e` writes a number with one digit, for example `2e-11`; splitting at the letter e gives the digit and the exponent, which are put into mathematics as $2 \times 10^{-11}$ (a tripled brace in an f-string prints one brace around the value).

```python
rate = y_pulse[:, 1]
rho_constraint = -(rho_side(rate, *EINSTEIN) + 0.0)  # kappa rho, Lambda = 0
p8_values = p8_side(rate, *EINSTEIN) + 0.0  # kappa p8
p3_values = p8_values + stress_values / 2  # kappa p3
pt_values = p8_values - stress_values / 2  # kappa pt
mismatch = np.abs(y_pulse[:, 2] - rho_constraint)  # conservation versus constraint
say(f"largest difference of the two energy densities: {mismatch.max():.0e}")
```

Along the pulse history the four parts of the source follow from the field equations (Section 12.9; the `+ 0.0` is $\Lambda = 0$ written out): $\kappa\rho$ from the constraint, $\kappa p_8$ from the hidden equation, and $p_3$, $p_t$ from $p_8$ and the stress. `mismatch` is the difference between the energy density carried along by the conservation law (the third column of the state) and the constraint's: at most $2 \times 10^{-11}$.

```python
reproduces(mismatch.max() < 1e-8,
           "the energy density from conservation equals the constraint along x4",
           WL, "constraint_propagation_bianchi")
check(abs(rho_constraint[0] + 24) < 1e-6 and abs(p8_values[0] - 12) < 1e-6,
      "before the pulse: kappa rho = -24, kappa p = 12 (the linear member A = 1)")
check(abs(rho_constraint[-1] + 33) < 1e-6 and abs(p8_values[-1] - 3) < 1e-6,
      "after the pulse: kappa rho = -33, kappa p = 3 (the linear member A = 2)")
```

The agreement is the numerical form of the record's constraint propagation (Section 12.10). The source starts at the values of $A = 1$ and ends at those of $A = 2$: $-(3\cdot 4 + 21) = -33$ and $15 - 12 = 3$.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
left.plot(x4_pulse, rho_constraint, label="$\\kappa\\rho$")
left.plot(x4_pulse, p3_values, label="$\\kappa p_3$")
left.plot(x4_pulse, pt_values, "--", label="$\\kappa p_t$")
left.plot(x4_pulse, p8_values, ":", color="black", label="$\\kappa p_8$")
left.set_xlabel("time $x_4$ (units $1/H$)")
left.set_ylabel("required source (units $H^2$)")
left.set_title("the source of the pulse history")
left.legend(fontsize=8)
right.semilogy(x4_pulse, np.maximum(mismatch, 1e-16))  # exact zeros at 1e-16
right.set_xlabel("time $x_4$ (units $1/H$)")
right.set_ylabel("$|\\kappa\\rho$ conserved $-$ $\\kappa\\rho$ constraint$|$")
right.set_title("conservation agrees with the constraint")
save_figure(fig, "required_source",
            ...)
```

The four source curves on the left; the mismatch on a logarithmic axis on the right, where a value of exactly zero (whose logarithm does not exist) is drawn at $10^{-16}$ by `np.maximum`. The caption, passed to `save_figure`, contains the measured mismatch written by `as_power_of_ten`. **What the figure shows.** Outside the pulse all three pressures coincide; during it $p_3$ and $p_t$ split symmetrically about $p_8$, and $\rho$ falls from $-24$ to $-33$. The mismatch stays at the level of the RK4 error.

**In [10], the relaxing stress.**

```python
damped = {}  # eta -> (x4, solution)
for eta in (0.25, 0.5, 1.0):
    def friction(x, y, eta=eta):
        return -2.0 * eta * (y[1] - 1.0)  # kappa Delta = -2 eta (a4' - H)

    x4, y = history(friction, 2.0, 0.01, 1000)  # start on A = 2
    damped[eta] = (x4, y)
```

For three values of $\eta$ the stress $\kappa\Delta = -2\eta(a_4' - 1)$ depends on the state. The argument `eta=eta` stores the current value of $\eta$ in the function; without it all three functions would use the last value of the loop. Each history has 1000 steps of 0.01, up to $x_4 = 10$.

```python
    exact_a4 = x4 + (1.0 / eta) * (1.0 - np.exp(-eta * x4))
    error = np.max(np.abs(y[:, 0] - exact_a4))
    mismatch = np.max(np.abs(y[:, 2] + rho_side(y[:, 1], *EINSTEIN)))
    check(error < 1e-9 and mismatch < 1e-8,
          f"eta = {eta}: a4 = x4 + (1 - e^(-eta x4))/eta, conservation holds")
    check(np.min(y[:, 1]) > 1.0,
          f"eta = {eta}: the rate a4' stays above H (the extra times deflate)")
    report(f"eta = {eta}: rate a4'/H at x4 = 10", f"{y[-1, 1]:.6f}")
```

The exact $a_4$ of Section 12.21 is compared, and conservation against the constraint as in In [9]. The rate stays above 1 and at $x_4 = 10$ equals $1 + e^{-10\eta}$: 1.082085, 1.006738 and 1.000045.

**In [11], figure 4: the relaxing histories.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
x4 = damped[0.25][0]
for slope, style, power in ((2.0, ":", "-2x_4"), (1.0, "-.", "-x_4")):
    left.plot(x4, slope * np.ones_like(x4), style, color="black",
              label=f"linear member $A = {slope:g}$")  # the two linear members
    right.semilogy(x4, np.exp(-slope * x4), style, color="black",
                   label=f"$A = {slope:g}$: $e^{{{power}}}$")
for eta, (x4, y) in damped.items():
    left.plot(x4, y[:, 1], label=f"$\\eta = {eta}$")
    right.semilogy(x4, np.exp(-y[:, 0]), label=f"$\\eta = {eta}$")
```

The two linear members $A = 2$ and $A = 1$ in black (constant rates on the left; $e^{-2x_4}$ and $e^{-x_4}$ on the right, the exponent written into the label by the f-string), then the three relaxing histories: their rates on the left and their extra-time scale factors on the right.

```python
left.set_ylim(0.0, 2.3)
left.set_xlabel("time $x_4$ (units $1/H$)")
left.set_ylabel("$a_4'/H$")
left.set_title("the deflation rate relaxes from $2H$ to $H$")
left.legend(fontsize=8)
right.set_xlabel("time $x_4$ (units $1/H$)")
right.set_ylabel("extra-time scale factor $e^{-a_4}$")
right.set_title("the extra times keep deflating")
right.legend(fontsize=8)
save_figure(fig, "damped_deflation",
            ...)
```

Labels and `save_figure`. **What the figure shows.** Each rate falls from 2 towards 1, faster for larger $\eta$. On the logarithmic axis each scale factor starts along the steeper black line and ends parallel to the flatter one: the deflation slows down but never stops.

**In [12], figure 5: the convergence of RK4.**

```python
def relaxing_unit(x, y):
    return -2.0 * (y[1] - 1.0)  # kappa Delta = -2 eta (a4' - H) with eta = 1


exact_end = 8.0 + (1.0 - math.exp(-8.0))  # the exact a4(8) for eta = 1
steps_list = [20, 40, 80, 160, 320]  # h = 8/steps = 0.4, 0.2, 0.1, 0.05, 0.025
sizes, errors = [], []
for steps in steps_list:
    x4, y = history(relaxing_unit, 2.0, 8.0 / steps, steps)
    sizes.append(8.0 / steps)
    errors.append(abs(y[-1, 0] - exact_end))
```

The relaxing history with $\eta = 1$ is integrated to $x_4 = 8$ five times, with 20, 40, 80, 160 and 320 steps, and the error of $a_4(8)$ is stored for each step size.

```python
orders = [math.log2(errors[i] / errors[i + 1]) for i in range(len(errors) - 1)]
for i, (size, error) in enumerate(zip(sizes, errors)):
    order = f"{orders[i - 1]:.2f}" if i > 0 else "-"
    say(f"h = {size:<6} error of a4(8) = {error:.2e}   measured order {order}")
check(all(3.7 < q < 4.3 for q in orders),
      "RK4 converges with order 4 (measured orders between 3.7 and 4.3)")
```

If the error is $Ch^q$, then halving $h$ divides it by $2^q$, and $q = \log_2(e_h/e_{h/2})$ (`math.log2` is the logarithm to base 2). The table prints each step (`:<6` pads it to six characters), its error with two decimals in powers of ten, and the measured order: 4.24, 4.12, 4.06, 4.03 (COMPUTED). The check requires every order to lie between 3.7 and 4.3.

```python
fig, ax = plt.subplots()
ax.loglog(sizes, errors, "o-", label="error of $a_4(8)$")
reference = errors[-1] * (np.array(sizes) / sizes[-1]) ** 4
ax.loglog(sizes, reference, "--", color="black", label="slope 4: $C h^4$")
ax.set_xticks(sizes)  # one tick at each step size used
ax.set_xticklabels([f"{size:g}" for size in sizes])
ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())  # no extra labels
ax.set_xlabel("step size $h$ (units $1/H$)")
ax.set_ylabel("absolute error")
ax.set_title("RK4 on the relaxing history: fourth-order convergence")
ax.legend(fontsize=8)
save_figure(fig, "rk4_convergence",
            ...)
```

`loglog` uses logarithmic scales on both axes, where $Ch^4$ is a straight line of slope 4. The reference line passes through the last measured point. The ticks of the horizontal axis are put at the five step sizes; `NullFormatter` removes the labels of the small extra ticks that a logarithmic axis would add. **What the figure shows.** The five points lie on the reference line: the method is of fourth order.

**In [13], the Gauss-Bonnet breakdown.**

```python
STRESS, RATE0 = 0.5, 1.0  # kappa Delta and the starting rate a4'(0) = H (A = 1)


def constant_stress(x, y):
    return STRESS
```

A constant stress $\kappa\Delta = 0.5$, starting on the canonical history.

```python
breakdown = {}  # alpha2 -> (x4, solution, predicted breakdown time)
for alpha2 in (0.005, 0.01):
    couplings = (1.0, alpha2, 0.0)

    def G(v, alpha2=alpha2):
        return (2 - 80 * alpha2) * v - 16 * alpha2 * v ** 3  # dG/dv = F

    critical = math.sqrt((2 - 80 * alpha2) / (48 * alpha2))  # F(critical) = 0
    x_star = (G(critical) - G(RATE0)) / STRESS  # the breakdown time
```

For two Gauss-Bonnet couplings: the function $G$ of Section 12.21, the critical rate where $F = 0$ and the predicted breakdown time $x_4^{\star}$.

```python
    def near_zero(y, couplings=couplings):
        return F_of(y[1], *couplings) < 0.05  # stop before F reaches zero

    x4, y = history(constant_stress, RATE0, 0.001, 20000, couplings,
                    stop=near_zero)
    breakdown[alpha2] = (x4, y, x_star)
```

`near_zero` tells `rk4` to stop when $F$ falls below 0.05, before the division by $F$ explodes. The integration uses the small step 0.001, because $a_4''$ grows steeply near the breakdown.

```python
    residual = np.max(np.abs(G(y[:, 1]) - G(RATE0) - STRESS * x4))
    check(residual < 1e-6, f"alpha2 = {alpha2}: G(a4') = G(a4'(0)) + kappa Delta x4")
    check(abs(x4[-1] - x_star) < 0.01,
          f"alpha2 = {alpha2}: F reaches 0 near the predicted time x4*")
    report(f"alpha2 = {alpha2}: critical rate, breakdown time x4*",
           f"{critical:.4f} H, {x_star:.4f}/H")
```

Along the numerical history the integrated relation $G(a_4') = G(a_4'(0)) + \kappa\Delta x_4$ must hold, and the integration must stop within 0.01 of $x_4^{\star}$. The RESULT lines give 2.5820 and 2.4682 for $\alpha_2 = 0.005$, and 1.5811 and 0.4498 for $\alpha_2 = 0.01$.

**In [14], figure 6: the breakdown compared with Einstein gravity.**

```python
x_einstein, y_einstein = history(constant_stress, RATE0, 0.01, 500)
check(np.max(np.abs(y_einstein[:, 1] - (RATE0 + STRESS * x_einstein / 2))) < 1e-12,
      "Einstein: a4' = 1 + 0.25 x4 for the constant stress")
```

In Einstein gravity ($F = 2$) the same stress gives $a_4' = 1 + 0.25x_4$ up to $x_4 = 5$, exactly.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
left.plot(x_einstein, y_einstein[:, 1], color="black", label="Einstein")
right.plot(x_einstein, F_of(y_einstein[:, 1], *EINSTEIN) * np.ones_like(x_einstein),
           color="black", label="Einstein")
for alpha2, (x4, y, x_star) in breakdown.items():
    line = left.plot(x4, y[:, 1], label=f"$\\alpha_2H^2 = {alpha2}$")[0]
    left.axvline(x_star, linestyle="--", color=line.get_color(), linewidth=0.8)
    right.plot(x4, F_of(y[:, 1], 1.0, alpha2, 0.0), color=line.get_color(),
               label=f"$\\alpha_2H^2 = {alpha2}$")
```

The Einstein rate and $F = 2$ in black. `F_of(y_einstein[:, 1], *EINSTEIN)` is already an array with one value 2 per time, because the formula of $F$ still contains the rate in terms multiplied by the couplings $\alpha_2 = \alpha_3 = 0$; multiplying by `np.ones_like(x_einstein)`, an array of ones of the same length, is only a safeguard, as in Notebook 12a, In [24] (Section 12.16): a formula with no rate left in it would give the single number 2. For each Gauss-Bonnet history the rate is drawn; `plot` returns a list of drawn lines, and `[0]` takes the line, whose colour `get_color()` is reused for a dashed vertical line at $x_4^{\star}$ (`axvline`) and for the curve of $F$ on the right.

```python
left.set_xlabel("time $x_4$ (units $1/H$)")
left.set_ylabel("$a_4'/H$")
left.set_title("the rate under a constant stress")
left.legend(fontsize=8)
right.axhline(0.0, color="black", linewidth=0.8)
right.set_xlabel("time $x_4$ (units $1/H$)")
right.set_ylabel("$F(a_4')$")
right.set_title("$F$ along the history")
right.legend(fontsize=8)
save_figure(fig, "gauss_bonnet_breakdown",
            ...)
```

**What the figure shows.** In Einstein gravity the rate rises along a straight line for ever. With the Gauss-Bonnet coupling it bends upwards ever more steeply and reaches the dashed line, the predicted $x_4^{\star}$, where $F$ (right) drops to zero: the evolution equation breaks down at a finite time.

**In [15], the record on the Kohn-Sham states.**

```python
ks = read_json(KS)
say("record: " + ks["conclusion"])
detail = {entry["name"]: entry["detail"] for entry in ks["checks"]}
verdicts = [entry["verdict"] for entry in ks["checks"]]
passed = verdicts.count("PASS")  # how many checks of the record passed
say(f"{KS}: {passed} of {len(verdicts)} checks PASS")
check(len(verdicts) > 0 and passed == len(verdicts) == ks["summary"]["checks"]
      and "ks_history_is_a_prescribed_background" in detail,
      "record: no Kohn-Sham state is an admissible source (every check PASS)")
```

The record is read and its conclusion printed. `detail` is made by a **dictionary comprehension**: a dictionary that maps the name of each check of the record to its detail text, which the next cell reads. The verdicts are counted as in Notebook 12a, In [2], and the count is printed with the name of the report. The check requires that the report has checks, that all of them passed, that the report's own summary counts the same number (a chained comparison `a == b == c` is true when $a = b$ and $b = c$), and that the check stating the prescribed background is present (`in` tests whether a name is a key of the dictionary).

**In [16], the record's numbers recomputed from the Kohn-Sham table.**

```python
import csv  # reads tables of comma-separated values
import re  # regular expressions: find a pattern in a text

TABLE = "Revision/kohn_sham/results/ground/emt-integrals.csv"
with repository_file(TABLE).open(encoding="utf-8", newline="") as handle:
    table = {row["id"]: row for row in csv.DictReader(handle)}
INTEGRALS = ("int_rho", "int_p3", "int_p_t", "int_p8")  # 2 Vol_7 int e^(6Hy) T dy
```

`csv` and `re` come with Python. The `with` block opens the table of the Kohn-Sham record and closes it again at the end of the block. `csv.DictReader` reads the table line by line: its first line holds the names of the columns, and every further line becomes a dictionary from column name to text. `table` maps the name of each state (column `id`) to its row. `INTEGRALS` names the four columns of the integrated energy density and pressures.

```python
zero = sorted(name for name, row in table.items()
              if all(float(row[column]) == 0.0 for column in INTEGRALS))
nonzero = [name for name in table if name not in zero]
report("Kohn-Sham states in the table", len(table))
report("states with a nonzero energy-momentum tensor", len(nonzero))
say("states with a zero energy-momentum tensor: " + ", ".join(zero))
```

`zero` lists, in alphabetical order, the states whose four integrals are all exactly zero (`float` turns a text such as `0.000000000000000e0` into the number 0; `all` is true when every one of its values is true); `nonzero` holds the other states. Out [16] reports 75 states, 70 of them with a nonzero energy-momentum tensor, and names the five others: the five slices of the state with $N = 8$ particles and $\lambda = 0$.

```python
counted = re.search(r"(\d+) ground-state profiles .*?\((\d+) with a nonzero",
                    detail["ks_profiles_depend_on_x8"])
reproduces(counted is not None
           and counted.groups() == (str(len(table)), str(len(nonzero))),
           f"{len(nonzero)} of the {len(table)} states have a nonzero tensor",
           KS, "ks_profiles_depend_on_x8")
listed = detail["ks_zero_source_states_listed"].rsplit(": ", 1)[-1].split(", ")
reproduces(sorted(listed) == zero,
           "the states with a zero tensor are the ones the record lists",
           KS, "ks_zero_source_states_listed")
```

The record writes its two counts into the detail text of its check `ks_profiles_depend_on_x8`, in the words "75 ground-state profiles ... (70 with a nonzero energy-momentum tensor)". `re.search` looks for a **pattern** in that text: `\d+` matches one or more digits, round brackets around a part of the pattern **capture** what that part matches, `.*?` matches any text up to the next part of the pattern, and `\(` matches a round bracket itself. `counted.groups()` returns the two captured numbers as texts, which must equal our two counts. The detail text of the check `ks_zero_source_states_listed` ends, after its last colon, with the list of the states whose tensor is zero: `rsplit(": ", 1)[-1]` takes the text after the last colon and space, and `split(", ")` cuts it at the commas. Both comparisons are made with `reproduces`, so the record's checks must also have the verdict PASS.

```python
ratio = {}  # r = (int p3 + int p_t)/(2 int p8) of every nonzero state
for name in nonzero:
    row = table[name]
    if float(row["int_p8"]) != 0.0:
        ratio[name] = ((float(row["int_p3"]) + float(row["int_p_t"]))
                       / (2 * float(row["int_p8"])))
closest = min(ratio, key=lambda name: abs(ratio[name] - 1.0))
report(f"closest to 1: r of {closest}", f"{ratio[closest]:.6g}")
HISTORY = ["N136_lam0_a00", "N136_lam0_a10", "N136_lam0_a20"]  # N = 136, lambda = 0
for name in HISTORY:
    slice_a4 = float(table[name]["a4"])  # the slice a4,0 of this state
    report(f"N = 136, lambda = 0, a4,0 = {slice_a4:g}: r", f"{ratio[name]:.6g}")
```

For every nonzero state with $\int p_8 \ne 0$ the ratio $r = (\int p_3 + \int p_t)/(2\int p_8)$ is computed. `min(ratio, key=...)` returns the name whose ratio has the smallest distance $|r - 1|$ from 1 (`lambda name: ...` is a small function written in one line). The format `.6g` prints six significant digits, as the record does, and `:g` prints the slice $a_{4,0}$ (column `a4`) without trailing zeros. Out [16] shows the state closest to 1, N688_lamm2_a00, with $r = 0.414328$, and for the history $N = 136$, $\lambda = 0$ the ratios 0.339767, 0.25969 and 0.239714 at $a_{4,0} = 0, 1, 2$: far from the required 1 at every slice.

```python
text = detail["ks_integrals_violate_algebraic_condition"]
tolerance = float(ks["tolerance"].split()[-1])  # "relative 1e-06" gives 1e-06
best = re.search(r"closest to 1: (\S+) at (\w+)", text)
reproduces(len(ratio) == len(nonzero) and abs(ratio[closest] - 1.0) > tolerance
           and best is not None
           and best.groups() == (f"{ratio[closest]:.6g}", closest),
           "r differs from 1 for every nonzero state; the closest as recorded",
           KS, "ks_integrals_violate_algebraic_condition")
found = [re.search(name + r": (\S+?)[,\s]", text) for name in HISTORY]
reproduces(all(item is not None and item.group(1) == f"{ratio[name]:.6g}"
               for item, name in zip(found, HISTORY)),
           "r of N = 136, lambda = 0 at a4,0 = 0, 1, 2 equals the record",
           KS, "ks_integrals_violate_algebraic_condition")
```

The record's tolerance is read from its text "relative 1e-06" (`split()` cuts the text at the spaces, `[-1]` takes the last part). The first check requires a ratio for every nonzero state, that even the closest one differs from 1 by more than the tolerance, and that the record names the same closest state with the same six digits (`\S+` matches characters that are not spaces, `\w+` letters, digits and underscores). The second check finds in the record's text, for each state of the history, the number after its name and a colon (`\S+?` takes as few characters as possible, up to the comma or space that `[,\s]` matches) and requires it to be exactly our number printed with six digits; `zip` walks through the two lists side by side. A change of the Kohn-Sham record, or of its checker, that moved any of these numbers would stop the notebook here.

**In [17], the last check.**

```python
figure_names = ["linear_member", "stress_pulse", "required_source",
                "damped_deflation", "rk4_convergence", "gauss_bonnet_breakdown"]
paths = [output_file(f"{FIGURE_FOLDER}/12c_{k}_{name}.png")
         for k, name in enumerate(figure_names, 1)]
check(all(path.is_file() for path in paths), "all six figure files exist")
all_checks_passed()
```

The same pattern as In [15] of Notebook 12b (Section 12.20): `figure_names` lists the short names of the six figures in the order in which they were drawn, `enumerate(figure_names, 1)` numbers them from 1, which gives the six file names `12c_1_linear_member.png` to `12c_6_gauss_bonnet_breakdown.png`, and `output_file` gives the path where each was written. `path.is_file()` is true when the file exists, and `all` requires this of every one of the six. `all_checks_passed()` prints the last line, ALL 30 CHECKS PASSED (notebook 12c): 1 check in In [3], 1 in In [4], 4 in In [5], 3 in In [7], 3 in In [9], 6 in In [10], 1 in In [12], 4 in In [13], 1 in In [14], 1 in In [15], 4 in In [16] and 1 in In [17].

### 12.26 A condensate of dirac16complex00 as an exact source

The previous examples prescribed the source. Can a field of this theory be the source, exactly? The Revision record proves three facts about the commuting field dirac16complex00 (Chapter 7), and leaves one question open. This section derives what the last notebook needs.

**The field and its equation.** dirac16complex00 is a column $\Phi$ of 16 complex numbers at every point, which transform as a Pin(4,4) spinor. The gamma matrices are the author's eight real 16 by 16 matrices $\gamma^{(x_1)}, \dots, \gamma^{(x_8)}$ of the record `Revision/algebra/gammas.json` (built from the author's formulas in Chapter 4), which satisfy the Clifford relation $\gamma^{(a)}\gamma^{(b)} + \gamma^{(b)}\gamma^{(a)} = 2\eta^{ab}$ with $\eta = \mathrm{diag}(+,+,+,-,-,-,-,+)$ (record checks `authorT16_clifford`; Notebook 12d, In [3]). The adjoint is $\bar\Phi = \Phi^\dagger C$ with the real symmetric matrix $C = \gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)}$, $C^2 = 1$, and $C\gamma^{(a)}$ antisymmetric for every $a$ (record check `authorT16_C_properties`). The density $S = \bar\Phi\Phi$ is a real number. With the potential $U = \tfrac\lambda2S^2$ the field equation of the record is

$$
\gamma^\mu D_\mu\Phi = (m + \lambda S)\,\Phi = M\,\Phi,\qquad D_\mu = \partial_\mu + \Omega_\mu,
$$

where $M = m + \lambda S$ is the **effective mass**, $\gamma^\mu = \gamma^{(\mu)}/\sqrt{|g_{\mu\mu}|}$ are the gammas of the curved metric and $\Omega_\mu$ is the spin connection of Chapter 6. For the author's metric, with the author's gammas, the spin connection enters the equation only through one term (PROVED: sympy record, check `authorT16_gravity_term`; lead's record, check `gamma_Omega_equals_3H_gamma8`; Notebook 12d, In [5]):

$$
\sum_\mu\gamma^\mu\Omega_\mu = 3H\gamma^{(x_8)} .
$$

**The condensate equation.** For a condensate, $\Phi = \Phi(x_4)$, only the derivative along $x_4$ survives, and $\gamma^{x_4} = \gamma^{(x_4)}$ because $g_{44} = -1$. Line by line:

$$
\gamma^{(x_4)}\Phi' + 3H\gamma^{(x_8)}\Phi = M\Phi
$$

(the field equation for $\Phi(x_4)$, with the spin-connection term inserted)

$$
\gamma^{(x_4)}\Phi' = \big(M - 3H\gamma^{(x_8)}\big)\Phi
$$

(subtract $3H\gamma^{(x_8)}\Phi$ from both sides)

$$
\Phi' = -\gamma^{(x_4)}\big(M - 3H\gamma^{(x_8)}\big)\Phi =: \mathcal{A}\,\Phi
$$

(multiply from the left by $-\gamma^{(x_4)}$, since $(-\gamma^{(x_4)})\gamma^{(x_4)} = -\eta^{44} = 1$). The 16 by 16 matrix $\mathcal{A}$ contains neither $a_4$ nor $z$: the condensate does not feel the deflation (record check `condensate_equation_x8_consistent`).

**Its square.** Line by line:

$$
\mathcal{A}^2 = \gamma^{(x_4)}\big(M - 3H\gamma^{(x_8)}\big)\gamma^{(x_4)}\big(M - 3H\gamma^{(x_8)}\big)
$$

(the two minus signs multiply to plus)

$$
= \gamma^{(x_4)}\gamma^{(x_4)}\big(M + 3H\gamma^{(x_8)}\big)\big(M - 3H\gamma^{(x_8)}\big)
$$

(move the middle $\gamma^{(x_4)}$ to the left: $\gamma^{(x_8)}\gamma^{(x_4)} = -\gamma^{(x_4)}\gamma^{(x_8)}$ by the Clifford relation, so $(M - 3H\gamma^{(x_8)})\gamma^{(x_4)} = \gamma^{(x_4)}(M + 3H\gamma^{(x_8)})$)

$$
= (-1)\big(M^2 - 3HM\gamma^{(x_8)} + 3HM\gamma^{(x_8)} - 9H^2(\gamma^{(x_8)})^2\big) = -\big(M^2 - 9H^2\big)
$$

($(\gamma^{(x_4)})^2 = -1$, $(\gamma^{(x_8)})^2 = +1$; the middle terms cancel). So for $M^2 > 9H^2$, with the frequency $w = \sqrt{M^2 - 9H^2}$, the condensate oscillates. If $\mathcal{A}v = \mu v$ for a nonzero vector $v$, then $\mu^2v = \mathcal{A}^2v = -w^2v$, so every eigenvalue of $\mathcal{A}$ is $+iw$ or $-iw$. Both occur, each 8 times: $\mathcal{A}$ is real, so its characteristic polynomial $\det(\mu - \mathcal{A})$ has real coefficients, and the non-real root $iw$ comes together with its complex conjugate $-iw$, with the same multiplicity; the 16 roots therefore split as $8 + 8$ (Exercise 10 gives a second proof with the trace; Notebook 12d, In [7], counts eight and eight numerically). Every vector $u$ is a sum of eigenvectors of the two kinds, $u = u_- + u_+$ with $u_- = \tfrac12\big(u + \tfrac{i}{w}\mathcal{A}u\big)$ and $u_+ = \tfrac12\big(u - \tfrac{i}{w}\mathcal{A}u\big)$: indeed $\mathcal{A}u_- = \tfrac12\big(\mathcal{A}u + \tfrac{i}{w}\mathcal{A}^2u\big) = \tfrac12(\mathcal{A}u - iwu) = -iw\,u_-$ (with $\mathcal{A}^2 = -w^2$), and in the same way $\mathcal{A}u_+ = +iw\,u_+$. An eigenvector $\Phi_0$ with $\mathcal{A}\Phi_0 = -iw\Phi_0$ gives the solution $\Phi(x_4) = e^{-iwx_4}\Phi_0$ (its derivative is $-iw\Phi = \mathcal{A}\Phi$). For $M = \pm5H$, $w = 4H$. The hidden-direction term moves the threshold of oscillation from $|M| = 0$ to $|M| = 3H$ (Notebook 12d, In [6] and figure 1).

**The density is constant.** Line by line:

$$
S' = (\Phi')^\dagger C\Phi + \Phi^\dagger C\Phi' = \Phi^\dagger\big(\mathcal{A}^TC + C\mathcal{A}\big)\Phi
$$

(product rule; $(\mathcal{A}\Phi)^\dagger = \Phi^\dagger\mathcal{A}^\dagger$, and $\mathcal{A}^\dagger = \mathcal{A}^T$ because $\mathcal{A}$ is real). Now $\mathcal{A} = -M\gamma^{(x_4)} + 3H\gamma^{(x_4)}\gamma^{(x_8)}$, and $C\gamma^{(a)}$ antisymmetric means $(\gamma^{(a)})^TC = -C\gamma^{(a)}$ (transpose $(C\gamma^{(a)})^T = (\gamma^{(a)})^TC^T$ and $C^T = C$). Hence $(\gamma^{(x_4)})^TC + C\gamma^{(x_4)} = 0$, and

$$
(\gamma^{(x_4)}\gamma^{(x_8)})^TC = (\gamma^{(x_8)})^T(\gamma^{(x_4)})^TC = -(\gamma^{(x_8)})^TC\gamma^{(x_4)} = C\gamma^{(x_8)}\gamma^{(x_4)} = -C\gamma^{(x_4)}\gamma^{(x_8)}
$$

(transpose of a product reverses the order; the rule above twice; the Clifford relation), so $\mathcal{A}^TC + C\mathcal{A} = 0$ and $S' = 0$ (record check `authorT16_condensate_S_constant`).

**Its energy-momentum tensor.** The record writes the source as $T^\mu{}_\nu = \sigma_T\big(-K^{(\mu}{}_{\nu)} + \delta^\mu_\nu L\big)$ with the kinetic tensor $K^\mu{}_\nu = \tfrac12\big(\bar\Phi\gamma^\mu D_\nu\Phi - (D_\nu\bar\Phi)\gamma^\mu\Phi\big)$, its symmetrised form $K^{(\mu}{}_{\nu)}$, and the on-shell Lagrangian $L = \sum_\mu K^\mu{}_\mu - mS - U$. The overall sign $\sigma_T = +1$ is the record's declared convention and is not fixed by a Revision check: it is ASSUMED. For a condensate the record proves that the diagonal of $K$ is $K^{x_4}{}_{x_4} = MS$ and zero in the seven other directions, and that $K^{x_4}{}_{x_8} = 0$ (check `authorT16_condensate_kinetic_diagonal`). Then, line by line:

$$
L = MS - mS - \tfrac\lambda2S^2 = (m + \lambda S)S - mS - \tfrac\lambda2S^2 = \tfrac\lambda2S^2
$$

(the definition, $M = m + \lambda S$, and $\lambda S^2 - \tfrac\lambda2S^2 = \tfrac\lambda2S^2$), and

$$
\rho = -T^{x_4}{}_{x_4} = K^{x_4}{}_{x_4} - L = MS - \tfrac\lambda2S^2 = mS + \tfrac\lambda2S^2,\qquad p_3 = p_t = p_8 = L = \tfrac\lambda2S^2 .
$$

So the condensate supplies exactly what the linear member needs: equal pressures and constant $\rho$ and $p$. But the 42 nonzero off-diagonal components of $K$ are multiples of 15 **three-gamma bilinears** $\bar\Phi\gamma^{(a)}\gamma^{(b)}\gamma^{(c)}\Phi$: the six with $\{a, b, c\} = \{i, x_4, x_8\}$ ($i$ a 3-space direction or an extra time) and the nine with $\{i, j, x_4\}$ ($i$ in 3-space, $j$ an extra time). The off-diagonal field equations $0 = \kappa T^\mu{}_\nu$ need all 15 to vanish (Wolfram record, check `condensate_offdiagonal_are_three_gamma_bilinears`). The record shows that condensates with all 15 zero exist (checks `condensate_diagonal_witness_exact` and `authorT16_condensate_witness`), and it proves that such a condensate allows only the linear member (key `theoremLinear` of `Revision/field_equations_a4/a4-equations.json`), under exact hypotheses. *Hypotheses*: $\Phi$ is a homogeneous condensate as above (classical, commuting) that solves its field equation and satisfies the off-diagonal conditions (all 15 bilinears zero); $a_4$ is twice continuously differentiable; the couplings are not all zero, $(\alpha_1, \alpha_2, \alpha_3) \ne (0, 0, 0)$. *Conclusion*: $a_4 = AHx_4 + a_0$ with real constants $A$ and $a_0$. *Proof*: the condensate has $p_3 = p_t$, so the evolution equation gives $a_4''F(a_4') = 0$ at every time. Suppose $a_4'' \ne 0$ at some time. Since $a_4''$ is continuous, $a_4'' \ne 0$ on a whole interval around it, so $F(a_4') = 0$ there: $a_4'$ takes only values among the roots of $F$. $F$ is a polynomial in $a_4'$ that is not identically zero when the couplings are not all zero (record check `evolution_F_not_identically_zero`), so it has finitely many roots. A continuous function on an interval that takes only finitely many values is constant there (between two different values it would have to pass through all the values in between). So $a_4'$ is constant on the interval and $a_4'' = 0$ there, a contradiction. Hence $a_4'' = 0$ at every time, $a_4' = AH$ is constant and $a_4 = AHx_4 + a_0$.

**The two Einstein conditions.** For the linear member the Einstein equations with this source are the time equation and seven equal equations (Section 12.12):

$$
(21 + 3A^2)H^2 + \Lambda = -\kappa\rho,\qquad (15 - 3A^2)H^2 + \Lambda = \kappa p .
$$

Subtracting the second from the first:

$$
(21 + 3A^2 - 15 + 3A^2)H^2 = -\kappa(\rho + p) \;\Rightarrow\; \kappa MS = -6(A^2 + 1)H^2
$$

($\Lambda$ cancels; $\rho + p = mS + \lambda S^2 = (m + \lambda S)S = MS$). Adding them:

$$
(21 + 3A^2 + 15 - 3A^2)H^2 + 2\Lambda = -\kappa(\rho - p) \;\Rightarrow\; \kappa mS = -(36H^2 + 2\Lambda)
$$

($\rho - p = mS$). These are the record's two conditions (PROVED: check `condensate_einstein_quadratic_U` in both reports; Notebook 12b, In [13], and Notebook 12d, In [13]). The first says that a real slope needs $\kappa MS \le -6H^2$: the density and the effective mass must have opposite signs. Given $A$, $\Lambda$ and $M$ they fix $S = -6(A^2 + 1)H^2/(\kappa M)$, then $m = -(36H^2 + 2\Lambda)/(\kappa S)$, then $\lambda = (M - m)/S$.

**What the record leaves open.** The record's document `Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md` says: "This record contains no check that combines a witness with the Einstein conditions." Notebook 12d makes that combination. It needs condensates with all 15 bilinears zero AND a density of the required sign and size. It builds them from two eigenvectors $v_1$, $v_2$ of $\mathcal{A}$ with the same frequency (the record's recipe; Section 12.30, In [8], explains how they are found) as the family $\Phi_0(t) = v_1 + t\,c\,v_2$ with a real parameter $t$ and $c = \overline{v_1^\dagger Cv_2}$ (the bar is the complex conjugate). Its density, with $\sigma = v_1^\dagger Cv_2$ and the notebook's finding $v_1^\dagger Cv_1 = v_2^\dagger Cv_2 = 0$:

$$
S(t) = v_1^\dagger Cv_1 + t\,c\,v_1^\dagger Cv_2 + t\,\bar c\,v_2^\dagger Cv_1 + t^2|c|^2\,v_2^\dagger Cv_2 = t\,\bar\sigma\sigma + t\,\sigma\bar\sigma = 2t\,|\sigma|^2
$$

(expand the product; $c = \bar\sigma$; $v_2^\dagger Cv_1 = \bar\sigma$ because $C$ is real and symmetric). So every real density, positive or negative, occurs. With the record's $H = \kappa = 1$ and $\sigma = -128/25 - 96i/25$ at $M = -5$: $|\sigma|^2 = (128^2 + 96^2)/625 = 1024/25$ and $S(t) = 2048t/25$ (Notebook 12d, In [9]).

**Three exact solutions** (units $H = \kappa = 1$):

| example | $A$ | $\Lambda$ | $M$ | $S$ | $m$ | $\lambda$ | $(\rho, p)$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | $1$ | $0$ | $-5$ | $12/5$ | $-15$ | $25/6$ | $(-24, 12)$ |
| 2 | $\sqrt5$ | $0$ | $5$ | $-36/5$ | $5$ | $0$ | $(-36, 0)$ |
| 3 | $1$ | $-30$ | $-5$ | $12/5$ | $10$ | $-25/4$ | $(6, -18)$ |

The equations of state $w = p/\rho$ are $-1/2$, $0$ and $-3$. Example 1 by hand: $S = -6(1 + 1)/(-5) = 12/5$; $m = -36/S = -36\cdot5/12 = -15$; $\lambda = (M - m)/S = (-5 + 15)\cdot5/12 = 25/6$; $\rho = mS + \tfrac\lambda2S^2 = -36 + \tfrac{25}{12}\cdot\tfrac{144}{25} = -36 + 12 = -24$; $p = 12$. Examples 1 and 3 have the canonical history $a_4 = Hx_4$: the extra times deflate as $e^{-Hx_4}$. Notebook 12d checks, exactly and for every time and every value of the hidden coordinate, all 16 components of the field equation and all 64 components of the Einstein equations, for $+A$ and for $-A$ (In [15]).

**Status.** These three solutions are PROVED for the stated numbers by exact computer algebra, under ASSUMED inputs: Einstein gravity, the sign convention $\sigma_T = +1$, the classical commuting field dirac16complex00 (not the quantised dirac16complex), and the chosen values of $\Lambda$, $m$ and $\lambda$. They are a computation of this book, not a Revision record. The equations do not select the sign of $A$: the same condensate solves them with $-A$. With $\Lambda = 0$ the energy density is negative; a positive one (example 3) needs $\Lambda < -(21 + 3A^2)H^2$ and then has $w < -1$. Not shown: whether such a condensate is stable, how it could arise, anything about the quantised field, and anything about the creation of universes.

### 12.27 Example: three exact solutions of the coupled equations

The last notebook rebuilds, with exact rational and complex-rational arithmetic and the author's eight real gamma matrices, the spin-connection term, the condensate equation and its solution, builds the family of condensates with all 15 three-gamma bilinears zero, computes their complete energy-momentum tensor in the author's metric with an arbitrary $a_4(x_4)$, solves the two Einstein conditions and checks the three exact solutions of Section 12.26 component by component. It runs in about 25 seconds, prints 40 PASS lines and draws six figures.

<!-- NOTEBOOK 12d -->

### 12.30 Line-by-line walk-through of Notebook 12d

The notebook has 20 code cells, In [1] to In [20].

**In [1], the set-up cell.** As in Notebook 12a (Section 12.16, In [1]), except that the comments hold the run instructions of Notebook 12d (Section 12.28) and `NOTEBOOK_ID = "12d"`.

**In [2], the records and the open question.** After the imports of `contextlib` and `io` the cell names six record files:

```python
GAMMAS = "Revision/algebra/gammas.json"  # the author's gamma matrices
EQUATIONS = "Revision/field_equations_a4/a4-equations.json"  # the a4 equations
PY = "Revision/field_equations_a4/reports/python-a4-report.json"  # sympy record
WL = "Revision/field_equations_a4/reports/wolfram-a4-report.json"  # Wolfram record
EMT = "Revision/lead_checks/reports/emt-divergence-and-spin-connection.json"
DOC = "Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md"  # the record's document
```

These are the gamma matrices, the equations of gravity, the three reports and the record's document on the field dirac16complex00. Then follow the three helpers of Notebook 12a, In [2], which Section 12.16 explains.

```python
OPEN_SENTENCE = ("This record contains no check that combines a witness with the "
                 "Einstein conditions")
document = repository_file(DOC).read_text(encoding="utf-8")
say(f"{DOC} says: \"{OPEN_SENTENCE}.\"")
check(OPEN_SENTENCE in document, "the record leaves this combination open")
```

The sentence of the record's document that states the open question is stored (two strings in brackets are joined into one), the document is read as text, the sentence is printed (`\"` is a quotation mark inside a string), and the check requires the document to contain it. If someone changes the document, this check fails and the notebook must be revised.

**In [3], the author's gamma matrices and C.**

```python
import itertools  # loops over all combinations of indices

import numpy as np  # floating-point arrays, used only for the plots
import sympy as sp  # exact algebra

NAMES = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]  # positions 0..7
ETA = [1, 1, 1, -1, -1, -1, -1, 1]  # the frame metric eta, x1..x8
I16, Z16 = sp.eye(16), sp.zeros(16, 16)  # the 16 by 16 unit and zero matrices
```

The imports; the coordinate names; the diagonal of the frame metric $\eta$; the exact 16 by 16 unit matrix `sp.eye(16)` and zero matrix.

```python
fixture = read_json(GAMMAS)
gamma = [sp.Matrix([[sp.Rational(x) for x in row] for row in matrix])
         for matrix in fixture["gamma"]]  # gamma[a] = gamma^(x_(a+1))
```

The record stores the eight gammas as lists of 16 rows of 16 entries, each written as text; `sp.Rational(x)` turns each text into an exact number and `sp.Matrix` makes a matrix. `gamma[0]` is $\gamma^{(x_1)}$, ..., `gamma[7]` is $\gamma^{(x_8)}$: the author's eight real 16 by 16 matrices.

```python
clifford = all(gamma[a] * gamma[b] + gamma[b] * gamma[a]
               == 2 * ETA[a] * (1 if a == b else 0) * I16
               for a in range(8) for b in range(8))
reproduces(clifford, "the author's gammas satisfy the Clifford relation",
           PY, "authorT16_clifford")
```

For all 64 pairs: $\gamma^{(a)}\gamma^{(b)} + \gamma^{(b)}\gamma^{(a)}$ (for sympy matrices `*` is the matrix product) must equal $2\eta^{ab}$ times the unit matrix, that is $2\eta^{aa}$ on the diagonal $a = b$ and 0 otherwise.

```python
C = gamma[7] * gamma[0] * gamma[1] * gamma[2]  # C = g^(x8) g^(x1) g^(x2) g^(x3)
stored_C = sp.Matrix([[sp.Rational(x) for x in row] for row in fixture["C"]])
properties = (C == stored_C and C == C.T and C * C == I16
              and all((C * g).T == -(C * g) for g in gamma))
reproduces(properties, "C is the record's C, real symmetric, C^2 = 1, C gamma "
           "antisymmetric", PY, "authorT16_C_properties")
```

$C$ is the product of the four space-like gammas; it must equal the $C$ stored in the record, be symmetric (`C.T` is the transpose), square to 1 and make every $C\gamma^{(a)}$ antisymmetric (Section 12.26).

**In [4], the spin connection.**

```python
H = sp.symbols("H", positive=True)  # the constant H of the metric
z = sp.symbols("z", positive=True)  # z = 6 H x8 in (0, pi/2)
x4 = sp.symbols("x4", real=True)  # the time
a4 = sp.Function("a4")(x4)  # an arbitrary function a4(x4)
cz = sp.symbols("cz", positive=True)  # cot z > 0 on the patch
ad1, ad2 = sp.symbols("ad1 ad2", real=True)  # a4' and a4''
s6 = sp.sin(z) ** sp.Rational(1, 6)  # the warp sin(z)^(1/6) of a length
E = [sp.exp(a4) * s6] * 3 + [sp.Integer(1)] + [sp.exp(-a4) * s6] * 3 + [sp.cot(z)]
g = [ETA[a] * E[a] ** 2 for a in range(8)]  # g_aa = eta_aa E_a^2
```

Symbols as in Notebook 12a. `E` lists the eight scale factors $E_a = \sqrt{|g_{aa}|}$ (the diagonal **vielbein** of Chapter 6), and the metric is rebuilt from them as $g_{aa} = \eta_{aa}E_a^2$; $a_4$ is an arbitrary function, so every result holds for every history.

```python
TRIG = {sp.sin(z): 1 / sp.sqrt(1 + cz ** 2), sp.cos(z): cz / sp.sqrt(1 + cz ** 2),
        sp.tan(z): 1 / cz, sp.cot(z): cz}  # every function of z through cot z


def clean(expr):
    expr = expr.subs(sp.Derivative(a4, (x4, 2)), ad2).subs(sp.Derivative(a4, x4), ad1)
    expr = sp.expand_trig(expr).subs(TRIG)
    return sp.expand(sp.cancel(sp.powsimp(sp.expand(expr), force=True)))


def d(expr, mu):
    if mu == 3:
        return sp.diff(expr, x4)
    if mu == 7:
        return 6 * H * sp.diff(expr, z)  # d/dx8 = (dz/dx8) d/dz = 6 H d/dz
    return sp.Integer(0)  # nothing depends on x1, x2, x3, x5, x6, x7
```

The same tools as in Notebook 12a, In [5] and In [7] (docstrings left out): `clean` writes derivatives as `ad1`, `ad2` (the second derivative first) and every function of $z$ through $\cot z$; `d` is the partial derivative.

```python
Gamma = [[[sp.Integer(0)] * 8 for _ in range(8)] for _ in range(8)]
for a, b, c in itertools.product(range(8), repeat=3):  # diagonal-metric formula
    value = 0
    if a == c:
        value += d(g[a], b)
    if a == b:
        value += d(g[a], c)
    if b == c:
        value -= d(g[b], a)
    Gamma[a][b][c] = value / (2 * g[a])
S_ab = [[(gamma[a] * gamma[b] - gamma[b] * gamma[a]) / 4 for b in range(8)]
        for a in range(8)]
```

The Christoffel symbols exactly as in Notebook 12a, In [5]; then the 64 matrices $S^{ab} = \tfrac14(\gamma^{(a)}\gamma^{(b)} - \gamma^{(b)}\gamma^{(a)})$, the generators of the spinor transformations (Chapter 5).

```python
omega = [[[clean(ETA[a] * E[a] * Gamma[a][mu][b] / E[b]) if a != b else 0
           for b in range(8)] for a in range(8)] for mu in range(8)]
antisymmetric = all(sp.expand(omega[mu][a][b] + omega[mu][b][a]) == 0
                    for mu in range(8) for a in range(8) for b in range(8))
check(antisymmetric, "omega_mu ab = -omega_mu ba (canonical spin connection)")
```

The canonical spin connection of the diagonal vielbein, $\omega_{\mu\,ab} = \eta_{aa}(E_a/E_b)\,\Gamma^a{}_{\mu b}$ for $a \ne b$ and 0 for $a = b$ (the text cell before the cell derives it from the definition). The check confirms that it is antisymmetric in $a$ and $b$, as a connection of this kind must be.

```python
Omega = [sum((omega[mu][a][b] * S_ab[a][b] / 2 for a in range(8) for b in range(8)
              if omega[mu][a][b] != 0), Z16) for mu in range(8)]
for mu in range(8):
    terms = sum(1 for a in range(8) for b in range(8) if omega[mu][a][b] != 0)
    say(f"Omega_{NAMES[mu]}: {terms} nonzero entries omega_mu ab")
```

$\Omega_\mu = \tfrac12\sum_{a,b}\omega_{\mu\,ab}S^{ab}$ for each $\mu$; `sum(..., Z16)` starts the sum at the zero matrix (a sum of matrices must start from a matrix). The loop prints how many $\omega_{\mu\,ab}$ are not zero: four for each 3-space direction and extra time (the pairs with $x_4$ and with $x_8$, in both orders), none for $x_4$ and $x_8$.

**In [5], the term 3H gamma8.**

```python
gamma_curved = [gamma[mu] / E[mu] for mu in range(8)]  # gamma^mu = gamma^(mu)/E_mu
reproduces(Omega[3] == Z16 and Omega[7] == Z16, "Omega_x4 = Omega_x8 = 0",
           PY, "authorT16_Omega_x4_x8_zero")
```

The curved gammas $\gamma^\mu = \gamma^{(\mu)}/E_\mu$; the spin connection along the time and along $x_8$ is zero.

```python
anticommute = all((gamma_curved[mu] * Omega[mu] + Omega[mu] * gamma_curved[mu])
                  .applyfunc(clean) == Z16 for mu in range(8))
reproduces(anticommute, "{gamma^mu, Omega_mu} = 0 for each mu (no sum)",
           PY, "authorT16_anticommutator_no_sum")
```

For each $\mu$ separately $\gamma^\mu\Omega_\mu + \Omega_\mu\gamma^\mu = 0$; `.applyfunc(clean)` applies `clean` to every entry of the matrix. (A line that starts with a dot continues the expression of the line above, inside the brackets.)

```python
gravity_term = sum((gamma_curved[mu] * Omega[mu] for mu in range(8)), Z16)
gravity_term = gravity_term.applyfunc(clean)
reproduces(gravity_term == 3 * H * gamma[7], "gamma^mu Omega_mu = 3 H gamma^(x8)",
           PY, "authorT16_gravity_term")
reproduces(gravity_term == 3 * H * gamma[7], "the same, the lead's independent check",
           EMT, "gamma_Omega_equals_3H_gamma8")
```

The sum $\sum_\mu\gamma^\mu\Omega_\mu$ equals $3H\gamma^{(x_8)}$: no $a_4$ and no $z$ remain, because the time-direction terms of the three inflating and the three deflating directions cancel. Two records confirm it.

**In [6], the condensate equation.**

```python
MM = sp.symbols("M", real=True)  # the effective mass M = m + lambda S


def condensate_matrix(M_value, H_value):
    return -gamma[3] * (M_value * I16 - 3 * H_value * gamma[7])


A_sym = condensate_matrix(MM, H)
```

`condensate_matrix` builds $\mathcal{A} = -\gamma^{(x_4)}(M - 3H\gamma^{(x_8)})$ of Section 12.26 for given $M$ and $H$ (docstring left out); `A_sym` is the matrix with the symbols $M$ and $H$.

```python
reduced = (gamma[3] * A_sym + gravity_term - MM * I16).applyfunc(sp.expand)
reproduces(reduced == Z16 and not A_sym.has(z),
           "gamma^(x4) A + 3 H gamma^(x8) = M: the equation is Phi' = A Phi",
           WL, "condensate_equation_x8_consistent")
check((A_sym * A_sym + (MM ** 2 - 9 * H ** 2) * I16).applyfunc(sp.expand) == Z16,
      "A^2 = -(M^2 - 9 H^2): every condensate oscillates with w = sqrt(M^2 - 9 H^2)")
reproduces((C * A_sym + A_sym.T * C).applyfunc(sp.expand) == Z16,
           "C A + A^T C = 0: S is constant along x4", PY,
           "authorT16_condensate_S_constant")
```

Three facts derived in Section 12.26: inserting $\Phi' = \mathcal{A}\Phi$ into the field equation gives $\gamma^{(x_4)}\mathcal{A} + 3H\gamma^{(x_8)} = M$ (and $\mathcal{A}$ is free of $z$); $\mathcal{A}^2 = -(M^2 - 9H^2)$; and $C\mathcal{A} + \mathcal{A}^TC = 0$, so $S$ is constant.

**In [7], figure 1: the frequency of a condensate.**

```python
m_axis = np.linspace(-8.0, 8.0, 801)  # M/H
fig, ax = plt.subplots()
ax.plot(m_axis[m_axis <= -3.0], np.sqrt(m_axis[m_axis <= -3.0] ** 2 - 9.0),
        color="tab:blue", label="$w = \\sqrt{M^2 - 9H^2}$")
ax.plot(m_axis[m_axis >= 3.0], np.sqrt(m_axis[m_axis >= 3.0] ** 2 - 9.0),
        color="tab:blue")
ax.axvspan(-3.0, 3.0, color="grey", alpha=0.2, label="$|M| < 3H$: no oscillation")
```

801 masses from $-8$ to 8 (units $H = 1$); `m_axis[m_axis <= -3.0]` keeps the entries not above $-3$ (an array of true and false values used as an index), and the two branches of $w = \sqrt{M^2 - 9}$ are drawn; the grey band marks $|M| < 3$.

```python
worst = 0.0  # the largest deviation of a numerical eigenvalue from +-i w
upper = []  # for each mass: how many eigenvalues have a positive imaginary part
for M_value in (-7.0, -5.0, -4.0, 4.0, 5.0, 7.0):
    matrix = np.array(condensate_matrix(M_value, 1).tolist(), dtype=float)
    eigenvalues = np.linalg.eigvals(matrix)
    w_value = np.sqrt(M_value ** 2 - 9.0)
    worst = max(worst, np.max(np.abs(np.abs(eigenvalues.imag) - w_value)),
                np.max(np.abs(eigenvalues.real)))
    upper.append(int(np.sum(eigenvalues.imag > 0)))  # the ones near +i w
    ax.plot([M_value] * 16, np.abs(eigenvalues.imag), "o", color="black",
            markersize=4, zorder=3)  # zorder 3: drawn on top of the red squares
```

For six masses the exact matrix is converted to a floating-point array and its 16 eigenvalues are computed numerically with `np.linalg.eigvals`. `worst` records the largest distance of an imaginary part (in absolute value) from $w$ and the largest real part. `eigenvalues.imag > 0` is an array of true and false values, one for each eigenvalue; `np.sum` counts the true ones (true counts as 1), and `upper.append` stores this count, the number of eigenvalues near $+iw$, for each mass. The absolute imaginary parts are drawn as black dots at the mass (`[M_value] * 16` repeats the mass 16 times; `zorder=3` draws them above the other marks).

```python
ax.plot([], [], "o", color="black", markersize=4,
        label="$|\\mathrm{Im}|$ of the eigenvalues of $\\mathcal{A}$")
ax.plot([-5, 5], [4, 4], "s", color="tab:red", markersize=7,
        label="$M = \\pm5H$: $w = 4H$")
ax.set_xlabel("effective mass $M/H$")
ax.set_ylabel("frequency $w/H$")
ax.set_title("The frequency of a homogeneous condensate")
ax.legend(fontsize=8, loc="upper center")
say(f"largest deviation of a numerical eigenvalue from +-i w: {worst:.0e}")
say(f"eigenvalues near +i w, for each of the six masses: {upper}")
check(worst < 1e-9 and upper == [8] * 6,
      "the 16 eigenvalues of A are +i w and -i w, eight of each (six masses)")
save_figure(fig, "condensate_frequency",
            ...)
```

An empty plot with a label gives the dots one legend entry; red squares mark $M = \pm5$, $w = 4$. The largest deviation, $10^{-14}$, and the six counts, all 8, are printed; the check requires a deviation below $10^{-9}$ and the count 8 at every mass (`[8] * 6` is the list of six eights), so eight eigenvalues are near $+iw$ and the other eight near $-iw$. **What the figure shows.** All dots lie on the curve $w = \sqrt{M^2 - 9H^2}$; each dot stands for all 16 eigenvalues of its mass, because the absolute value of the imaginary part does not distinguish $+iw$ from $-iw$. Inside the grey band there is no oscillation, so the examples use $M = \pm5H$.

**In [8], the family of condensates with the 15 bilinears zero.**

```python
t = sp.symbols("t", real=True)  # the free real parameter of the family
TRIPLES = list(itertools.combinations(range(8), 3))  # all 56 sets {a, b, c}
NEEDED = sorted({tuple(sorted((i, 3, 7))) for i in (0, 1, 2, 4, 5, 6)}
                | {tuple(sorted((i, j, 3))) for i in (0, 1, 2) for j in (4, 5, 6)})
```

The real parameter $t$. `itertools.combinations(range(8), 3)` lists the 56 sets of three different positions in increasing order. `NEEDED` is the set (braces) of the 15 triples whose bilinears the field equations need to vanish: $\{i, x_4, x_8\}$ for the six directions $i$, joined (`|`) with $\{i, j, x_4\}$ for $i$ in 3-space and $j$ an extra time; each triple is sorted, and the whole is sorted into a list.

```python
def witness_parts(M_value, H_value):
    w_value = sp.sqrt(M_value ** 2 - 9 * H_value ** 2)
    A_value = condensate_matrix(M_value, H_value)
    spaces = []
    for sign in (-1, 1):  # the eigenvalue of g^(x1)g^(x5) = g^(x2)g^(x6) = ...
        stack = sp.Matrix.vstack(A_value + sp.I * w_value * I16,
                                 gamma[0] * gamma[4] - sign * I16,
                                 gamma[1] * gamma[5] - sign * I16,
                                 gamma[2] * gamma[6] - sign * I16)
        spaces.append(stack.nullspace())  # all solutions of stack * v = 0
    v1, v2 = spaces[0][0], spaces[1][0]
    c = sp.conjugate(sp.expand((v1.H * C * v2)[0]))  # c = conj(v1^dagger C v2)
    return spaces, v1, v2, c, w_value, A_value
```

The record's recipe (docstring left out). `sp.Matrix.vstack` stacks four 16 by 16 matrices into one 64 by 16 matrix; a column $v$ with `stack * v = 0` satisfies four equations at once: $\mathcal{A}v = -iwv$ (`sp.I` is $i$), and $\gamma^{(x_1)}\gamma^{(x_5)}v = \gamma^{(x_2)}\gamma^{(x_6)}v = \gamma^{(x_3)}\gamma^{(x_7)}v = \pm v$ (each of these products squares to 1, so its eigenvalues are $\pm1$). `.nullspace()` returns a list of columns that span all solutions, computed exactly. $v_1$ is the first solution with the sign $-1$, $v_2$ with $+1$. `v1.H` is the conjugate transpose $v_1^\dagger$, and `[0]` takes the single entry of the 1 by 1 product; $c$ is its complex conjugate.

```python
def bilinear(phi, matrix):
    return sp.expand((phi.H * C * matrix * phi)[0])


def three_gamma(triple):
    a, b, c = triple
    return gamma[a] * gamma[b] * gamma[c]
```

`bilinear` computes $\bar\Phi X\Phi = \Phi^\dagger CX\Phi$ for a matrix $X$; `three_gamma` builds $\gamma^{(a)}\gamma^{(b)}\gamma^{(c)}$ for a triple (docstrings left out).

```python
spaces, v1, v2, c, w, A_witness = witness_parts(-5, 1)
phi_t = (v1 + t * c * v2).applyfunc(sp.expand)  # the family Phi_0(t)
check([len(space) for space in spaces] == [1, 1],
      "the two null spaces are one-dimensional (v1 and v2 are unique)")
report("frequency w at M = -5 H", w, "H")
check((A_witness * phi_t + sp.I * w * phi_t).applyfunc(sp.expand)
      == sp.zeros(16, 1), "A Phi_0(t) = -i w Phi_0(t) for every t")
needed_values = [bilinear(phi_t, three_gamma(triple)) for triple in NEEDED]
check(len(NEEDED) == 15 and all(value == 0 for value in needed_values),
      "the 15 three-gamma bilinears vanish for every real t")
```

The recipe at $M = -5$, $H = 1$, and the family $\Phi_0(t) = v_1 + t\,c\,v_2$ with $t$ kept as a symbol. Each solution space is one-dimensional, so $v_1$ and $v_2$ are unique up to a factor; the frequency is $w = 4$; every member of the family is an eigenvector of $\mathcal{A}$ with the eigenvalue $-iw$; and the 15 needed bilinears are zero as expressions in $t$, so for every real $t$.

**In [9], the density of the family.**

```python
S_t = bilinear(phi_t, I16)  # S(t) = Phi_0(t)^dagger C Phi_0(t)
cross = sp.expand((v1.H * C * v2)[0])  # v1^dagger C v2
report("v1^dagger C v2", cross)
report("S(t)", S_t)
check(bilinear(v1, I16) == 0 and bilinear(v2, I16) == 0
      and sp.expand(S_t - 2 * t * cross * sp.conjugate(cross)) == 0,
      "S(t) = 2 t |v1^dagger C v2|^2: every real density occurs")
```

The density of the family, the cross term $\sigma = v_1^\dagger Cv_2 = -128/25 - 96i/25$, and $S(t) = 2048t/25$; the check confirms $v_1^\dagger Cv_1 = v_2^\dagger Cv_2 = 0$ and $S(t) = 2t|\sigma|^2$ (derived in Section 12.26).

```python
_, u1, u2, c_plus, w_plus, A_plus = witness_parts(5, 1)  # the record's M = +5
phi_plus = (u1 + c_plus * u2).applyfunc(sp.expand)  # t = 1
S_plus = bilinear(phi_plus, I16)
ok_plus = ((A_plus * phi_plus + sp.I * w_plus * phi_plus).applyfunc(sp.expand)
           == sp.zeros(16, 1)
           and all(bilinear(phi_plus, three_gamma(tr)) == 0 for tr in NEEDED)
           and S_plus != 0 and sp.im(S_plus) == 0)
reproduces(ok_plus, "M = +5, H = 1: a witness with S real, not 0, 15 bilinears 0",
           PY, "authorT16_condensate_witness")
```

The recipe repeated at $M = +5$, where the record ran it with the author's gammas, at $t = 1$ (the record's witness; `_` receives the unused first value): it is an eigenvector, its 15 bilinears vanish and its density is a real number different from 0 (`sp.im` is the imaginary part).

**In [10], figure 2: all 56 three-gamma bilinears.**

```python
phi_one = phi_t.subs(t, 1)  # Phi_0(1)
all_values = [bilinear(phi_one, three_gamma(triple)) for triple in TRIPLES]
check(all(sp.im(value) == 0 for value in all_values),
      "all 56 three-gamma bilinears of Phi_0(1) are real numbers")
nonzero = [triple for triple, value in zip(TRIPLES, all_values) if value != 0]
say("nonzero bilinears: " + ", ".join(
    "".join(NAMES[i][1] for i in triple) for triple in nonzero))
check(all(3 not in triple and 7 not in triple for triple in nonzero),
      "every nonzero one avoids x4 and x8")
```

All 56 bilinears of the member $t = 1$ are computed and are real. The nonzero ones are printed as digit strings (`NAMES[i][1]` is the second character of `"x1"`, the digit): 123, 127, 136, 167, 235, 257, 356, 567, all built from 3-space directions and extra times (positions 3 and 7, $x_4$ and $x_8$, never occur).

```python
labels = ["".join(NAMES[i][1] for i in triple) for triple in TRIPLES]
numbers = np.array([float(value) for value in all_values])
is_needed = np.array([triple in NEEDED for triple in TRIPLES])
fig, ax = plt.subplots(figsize=(11.0, 4.2))
positions = np.arange(len(TRIPLES))
ax.bar(positions[~is_needed], numbers[~is_needed], color="tab:blue",
       label="other bilinears")
ax.plot(positions[is_needed], numbers[is_needed], "x", color="tab:red",
        markersize=8, label="the 15 the field equations need to vanish")
```

Labels, values and a true/false array marking the needed triples. `np.arange(56)` is 0 to 55; `~is_needed` is the opposite array. The other 41 bilinears are drawn as blue bars (`ax.bar`), the 15 needed ones as red crosses.

```python
ax.axhline(0.0, color="black", linewidth=0.8)
ax.set_xticks(positions)
ax.set_xticklabels(labels, rotation=90, fontsize=6.5)
ax.set_xlabel("directions $abc$ of $\\bar\\Phi\\gamma^{(a)}\\gamma^{(b)}"
              "\\gamma^{(c)}\\Phi$ (digits: $x_1$ = 1, ..., $x_8$ = 8)")
ax.set_ylabel("value of the bilinear")
ax.set_title("The 56 three-gamma bilinears of the condensate $\\Phi_0(1)$, "
             "$M = -5H$")
ax.legend(fontsize=8)
save_figure(fig, "three_gamma_bilinears",
            ...)
```

Axis, tick labels turned by 90 degrees, titles and `save_figure`. **What the figure shows.** Every red cross sits on zero; only eight blue bars rise, at triples without $x_4$ and $x_8$, which no field equation constrains.

**In [11], the complete kinetic tensor.**

```python
UNIT_H = {H: 1}  # the examples use H = 1
Omega_1 = [matrix.subs(UNIT_H) for matrix in Omega]
gamma_1 = [matrix.subs(UNIT_H) for matrix in gamma_curved]
g_1 = [entry.subs(UNIT_H) for entry in g]
```

The spin connection, the curved gammas and the metric with $H = 1$; $a_4$ and $z$ stay arbitrary.

```python
def D_phi(nu):
    return (A_witness if nu == 3 else Z16) + Omega_1[nu]


def D_phibar(nu):
    return (A_witness.T * C if nu == 3 else Z16) - C * Omega_1[nu]
```

The matrices that give the covariant derivatives (docstrings left out): $D_\nu\Phi = \partial_\nu\Phi + \Omega_\nu\Phi$, with $\partial_4\Phi = \mathcal{A}\Phi$ and no other derivative; and $D_\nu\bar\Phi = \partial_\nu\bar\Phi - \bar\Phi\Omega_\nu = \Phi^\dagger(\mathcal{A}^TC\,\delta_{\nu 4} - C\Omega_\nu)$, because $\partial_4\bar\Phi = (\mathcal{A}\Phi)^\dagger C = \Phi^\dagger\mathcal{A}^TC$.

```python
K = [[(phi_t.H * ((C * gamma_1[mu] * D_phi(nu) - D_phibar(nu) * gamma_1[mu]) / 2)
       * phi_t)[0] for nu in range(8)] for mu in range(8)]
K_sym = [[clean((K[mu][nu] + (g_1[nu] / g_1[mu]) * K[nu][mu]) / 2)
          for nu in range(8)] for mu in range(8)]
```

All 64 components $K^\mu{}_\nu = \tfrac12\big(\bar\Phi\gamma^\mu D_\nu\Phi - (D_\nu\bar\Phi)\gamma^\mu\Phi\big)$ as bilinears of $\Phi_0(t)$ (the phase $e^{-iwx_4}$ cancels between $\Phi^\dagger$ and $\Phi$). The symmetrised tensor: lower the upper index ($K_{\mu\nu} = g_{\mu\mu}K^\mu{}_\nu$), average with the exchanged component, raise again; this gives $\tfrac12\big(K^\mu{}_\nu + (g_{\nu\nu}/g_{\mu\mu})K^\nu{}_\mu\big)$.

```python
off_diagonal = all(K_sym[mu][nu] == 0 for mu in range(8) for nu in range(8)
                   if mu != nu)
reproduces(off_diagonal, "every off-diagonal K^(mu nu) vanishes, for every a4, a4', z",
           WL, "condensate_diagonal_witness_exact")
diagonal = [K_sym[mu][mu] for mu in range(8)]
say(f"diagonal of K: {diagonal}")
reproduces(all(diagonal[mu] == 0 for mu in range(8) if mu != 3)
           and sp.expand(diagonal[3] - (-5) * S_t) == 0,
           "K^x4_x4 = M S and every other diagonal entry is 0",
           PY, "authorT16_condensate_kinetic_diagonal")
```

Every off-diagonal component is zero for the whole family, every $a_4$ and every $z$; the diagonal is $[0, 0, 0, -2048t/5, 0, 0, 0, 0]$, that is $K^{x_4}{}_{x_4} = MS = -5\cdot 2048t/25$.

**In [12], the energy-momentum tensor of the family.**

```python
m, lam = sp.symbols("m lambda", real=True)  # the mass and the self-coupling


def source_tensor(K_matrix, S_value, m_value, lam_value):
    L_value = (sum(K_matrix[mu][mu] for mu in range(8)) - m_value * S_value
               - lam_value * S_value ** 2 / 2)
    return [[sp.expand(-K_matrix[mu][nu] + (L_value if mu == nu else 0))
             for nu in range(8)] for mu in range(8)]
```

`source_tensor` builds $T^\mu{}_\nu = -K^{(\mu}{}_{\nu)} + \delta^\mu_\nu L$ with $L = \sum_\mu K^\mu{}_\mu - mS - \tfrac\lambda2S^2$ ($\sigma_T = +1$; docstring left out).

```python
on_shell = {m: -5 - lam * S_t}  # M = m + lambda S = -5
T_family = source_tensor(K_sym, S_t, m, lam)
rho_family = sp.expand(-T_family[3][3].subs(on_shell))
pressures = [sp.expand(T_family[mu][mu].subs(on_shell)) for mu in (0, 4, 7)]
check(sp.expand(rho_family - ((-5 - lam * S_t) * S_t + lam * S_t ** 2 / 2)) == 0
      and all(sp.expand(p - lam * S_t ** 2 / 2) == 0 for p in pressures),
      "rho = m S + (lambda/2) S^2 and p3 = pt = p8 = (lambda/2) S^2 on shell")
```

On shell the mass is fixed by $M = m + \lambda S = -5$. The check confirms $\rho = mS + \tfrac\lambda2S^2$ and $p_3 = p_t = p_8 = \tfrac\lambda2S^2$ (Section 12.26).

**In [13], the two Einstein conditions.**

```python
A, Lam, kappa = sp.symbols("A Lambda kappa", real=True)
record = read_json(EQUATIONS)
E1 = record["lovelockTensors"]["E1"]  # the Einstein tensor G = E_(1)
LINEAR = {"ad1": A * H, "ad2": 0, "H": H}  # a4' = A H, a4'' = 0


def from_record(key):
    return sp.sympify(E1[key]["input"].replace("^", "**"), locals=LINEAR)
```

Symbols for the slope, $\Lambda$ and $\kappa$; the Einstein tensor of the record. `LINEAR` is used as the dictionary of names for the parser, so that reading a formula already replaces `ad1` by $AH$ and `ad2` by 0 (docstring left out).

```python
G_time, G_space = from_record("x4x4"), from_record("x1x1")
G_extra, G_hidden = from_record("x5x5"), from_record("x8x8")
check(sp.expand(G_space - G_hidden) == 0 and sp.expand(G_extra - G_hidden) == 0,
      "linear member: G^x1_x1 = G^x5_x5 = G^x8_x8 (the record's components)")
```

The four Einstein components for the linear member; the seven non-time ones are equal.

```python
S_sym, rho_sym, p_sym = sp.symbols("S rho p", real=True)
time_equation = G_time + Lam + kappa * rho_sym  # = 0
space_equation = G_hidden + Lam - kappa * p_sym  # = 0
condensate = {rho_sym: m * S_sym + lam * S_sym ** 2 / 2, p_sym: lam * S_sym ** 2 / 2}
first = sp.expand(kappa * (m + lam * S_sym) * S_sym + 6 * (A ** 2 + 1) * H ** 2)
second = sp.expand(kappa * m * S_sym + 36 * H ** 2 + 2 * Lam)
reproduces(sp.expand((time_equation - space_equation).subs(condensate) - first) == 0
           and sp.expand((time_equation + space_equation).subs(condensate)
                         - second) == 0,
           "Einstein: kappa M S = -6 (A^2 + 1) H^2 and kappa m S = -(36 H^2 + 2 Lambda)",
           PY, "condensate_einstein_quadratic_U")
```

The time equation and the common equation of the other directions, written as expressions that must vanish; with the condensate's $\rho$ and $p$, their difference and sum are the two conditions of Section 12.26.

```python
M_value = sp.symbols("M_value", real=True)
S_needed = sp.solve(kappa * M_value * S_sym + 6 * (A ** 2 + 1) * H ** 2, S_sym)[0]
m_needed = sp.solve(second, m)[0]
say(f"S = {S_needed},  m = {m_needed},  lambda = (M - m)/S")
```

The first condition solved for $S$ and the second for $m$; $\lambda$ then follows as $(M - m)/S$.

**In [14], figure 3: which condensates can drive a linear member.**

```python
m_left = np.linspace(-10.0, -0.01, 1000)  # M/H < 0
m_right = np.linspace(0.01, 10.0, 1000)  # M/H > 0
fig, ax = plt.subplots(figsize=(7.0, 5.2))
# grey: kappa M S > -6, where A^2 = -kappa M S/6 - 1 would be negative
ax.fill_between(m_left, -12.0, np.minimum(-6.0 / m_left, 12.0), color="grey",
                alpha=0.25, linewidth=0.0)
ax.fill_between(m_right, np.maximum(-6.0 / m_right, -12.0), 12.0, color="grey",
                alpha=0.25, linewidth=0.0, label="no real slope $A$")
```

Masses on either side of zero (the hyperbolas are not defined at $M = 0$); `figsize=(7.0, 5.2)` makes the figure 7 inches wide and 5.2 high. The comment line states the rule for the grey region: the first condition of Section 12.26, $\kappa MS = -6(A^2 + 1)$ (units $H = 1$), solved for the slope gives $A^2 = -\kappa MS/6 - 1$, and this is negative, so that no real $A$ exists, exactly when $\kappa MS > -6$. A real slope therefore needs $\kappa MS \le -6$. For $M < 0$ this means $\kappa S \ge -6/M$, so the region below the curve $\kappa S = -6/M$ is shaded grey; for $M > 0$ it means $\kappa S \le -6/M$, so the region above is shaded. `np.minimum` and `np.maximum` keep the curves inside the plotted range $\pm12$.

```python
ax.axvspan(-3.0, 3.0, facecolor="none", edgecolor="black", hatch="//",
           linewidth=0.0, label="$|M| < 3H$: no oscillating condensate")
for slope_squared, style in ((0, ":"), (1, "-"), (4, "--"), (5, "-.")):
    level = 6.0 * (slope_squared + 1)
    label = f"$A^2 = {slope_squared}$"
    ax.plot(m_left, -level / m_left, style, color="tab:blue", label=label)
    ax.plot(m_right, -level / m_right, style, color="tab:blue")
```

The hatched band $|M| < 3$, where no condensate oscillates. Then the hyperbolas $\kappa MS = -6(A^2 + 1)$ for $A^2 = 0, 1, 4, 5$, on both sides.

```python
ax.plot([-5], [12 / 5], "o", color="tab:red", markersize=8,
        label="examples 1 and 3: $M = -5H$, $\\kappa S = 12/5$")
ax.plot([5], [-36 / 5], "s", color="tab:green", markersize=8,
        label="example 2: $M = 5H$, $\\kappa S = -36/5$")
ax.set_xlim(-10, 10)
ax.set_ylim(-12, 12)
ax.set_xlabel("effective mass $M/H$")
ax.set_ylabel("$\\kappa S$ (units $H = 1$)")
ax.set_title("Which condensates can drive a linear member (Einstein gravity)")
ax.legend(fontsize=7.5, loc="lower left")
save_figure(fig, "allowed_sources",
            ...)
```

The three examples are marked. **What the figure shows.** Allowed condensates lie in the upper left and lower right quarters, where $S$ and $M$ have opposite signs and outside the grey; the red circle lies on the hyperbola $A^2 = 1$ and the green square on $A^2 = 5$.

**In [15], the three exact solutions.**

```python
EXAMPLES = [  # name, A, Lambda, M (with H = kappa = 1)
    ("example 1", sp.Integer(1), sp.Integer(0), -5),
    ("example 2", sp.sqrt(5), sp.Integer(0), 5),
    ("example 3", sp.Integer(1), sp.Integer(-30), -5),
]
UNITS = {H: 1, kappa: 1}
solutions = {}  # name -> the numbers of the solution
```

The three examples of Section 12.26 by their slope, cosmological constant and effective mass; $\sqrt5$ is kept exact as `sp.sqrt(5)`.

```python
for name, slope, cosmological, M_example in EXAMPLES:
    S_value = sp.nsimplify(S_needed.subs(UNITS).subs({M_value: M_example,
                                                    A: slope}))
    m_value = m_needed.subs(UNITS).subs({S_sym: S_value, Lam: cosmological})
    lam_value = (M_example - m_value) / S_value
```

For each example: the density from the first condition (`sp.nsimplify` writes the result in its simplest exact form), the mass from the second, the self-coupling from $\lambda = (M - m)/S$.

```python
    spaces_e, v1_e, v2_e, c_e, w_e, A_e = witness_parts(M_example, 1)
    S_of_t = bilinear((v1_e + t * c_e * v2_e).applyfunc(sp.expand), I16)
    t_value = sp.solve(S_of_t - S_value, t)[0]
    phi0 = (v1_e + t_value * c_e * v2_e).applyfunc(sp.expand)
    phi = phi0 * sp.exp(-sp.I * w_e * x4)  # the condensate Phi(x4)
```

The family at this mass; the member whose density is the required one ($S(t)$ is linear in $t$, so `sp.solve` gives one $t$: $15/512$ for examples 1 and 3, $-45/512$ for example 2); the condensate $\Phi(x_4) = e^{-iwx_4}\Phi_0$.

```python
    # 1. the field equation, with the full spin-connection sum of section 7:
    residual = (gamma[3] * sp.diff(phi, x4) + gravity_term.subs(UNIT_H) * phi
                - (m_value + lam_value * S_value) * phi).applyfunc(sp.simplify)
    field_ok = residual == sp.zeros(16, 1) and bilinear(phi0, I16) == S_value
```

The 16 components of the field equation $\gamma^\mu D_\mu\Phi - (m + \lambda S)\Phi$: the only derivative is along $x_4$, where $\gamma^{x_4} = \gamma^{(x_4)}$, plus the spin-connection term of In [5] at $H = 1$. Every component must simplify to zero, at every time, and the density must be the required one. (The comment refers to section 7 of the notebook.)

```python
    # 2. the Einstein equations, all 64 components, for +A and for -A:
    K_e = K_sym if M_example == -5 else None
    if K_e is None:  # example 2 has its own condensate matrix A (M = +5)
        K_raw = [[(phi0.H * ((C * gamma_1[mu] * ((A_e if nu == 3 else Z16)
                                                 + Omega_1[nu])
                              - ((A_e.T * C if nu == 3 else Z16) - C * Omega_1[nu])
                              * gamma_1[mu]) / 2) * phi0)[0]
                  for nu in range(8)] for mu in range(8)]
        K_e = [[clean((K_raw[mu][nu] + (g_1[nu] / g_1[mu]) * K_raw[nu][mu]) / 2)
                for nu in range(8)] for mu in range(8)]
    else:
        K_e = [[entry.subs(t, t_value) for entry in row] for row in K_e]
    T_e = source_tensor(K_e, S_value, m_value, lam_value)
```

For $M = -5$ the kinetic tensor of In [11] is reused with the found $t$. For example 2 ($M = +5$) it is computed afresh exactly as in In [11], with the matrix $\mathcal{A}$ of $M = +5$. Then the energy-momentum tensor (with $\kappa = 1$ it is $\kappa T$).

```python
    einstein_ok = {}
    for sign in (1, -1):
        G_diag = [G_space] * 3 + [G_time] + [G_extra] * 3 + [G_hidden]
        values = {A: sign * slope, H: 1}
        einstein_ok[sign] = all(
            sp.simplify((G_diag[mu].subs(values) + cosmological if mu == nu else 0)
                        - T_e[mu][nu]) == 0
            for mu in range(8) for nu in range(8))
```

For the slope $+A$ and for $-A$ all 64 components of $G^\mu{}_\nu + \Lambda\delta^\mu_\nu - \kappa T^\mu{}_\nu$ must simplify to zero (off the diagonal the left-hand side is 0, so $T$ must vanish there). Since $T$ contains no $x_4$ and no $z$, this holds at every time and every value of the hidden coordinate.

```python
    rho_e, p_e = -T_e[3][3], T_e[0][0]
    solutions[name] = {"A": slope, "Lambda": cosmological, "M": M_example,
                       "S": S_value, "m": m_value, "lambda": lam_value, "t": t_value,
                       "rho": rho_e, "p": p_e, "phi0": phi0, "w": w_e, "T": T_e}
    say(f"{name}: A = {slope}, Lambda = {cosmological}, M = {M_example}, "
        f"S = {S_value}, t = {t_value}, m = {m_value}, lambda = {lam_value}, "
        f"rho = {rho_e}, p = {p_e}")
    check(field_ok, f"{name}: the 16 components of the field equation hold exactly")
    check(einstein_ok[1], f"{name}: all 64 Einstein components hold exactly")
    check(einstein_ok[-1], f"{name}: they hold as well with -A (A enters as A^2)")
```

The energy density and pressure are read off, all numbers are stored for the later cells, printed in one line, and the three checks of the example are made. Out [15] shows the table of Section 12.26 and nine PASS lines.

**In [16], the numbers compared with the table.**

```python
table = {"example 1": (sp.Rational(12, 5), -15, sp.Rational(25, 6), -24, 12),
         "example 2": (sp.Rational(-36, 5), 5, 0, -36, 0),
         "example 3": (sp.Rational(12, 5), 10, sp.Rational(-25, 4), 6, -18)}
for name, (S_v, m_v, lam_v, rho_v, p_v) in table.items():
    sol = solutions[name]
    same = (sol["S"] == S_v and sol["m"] == m_v and sol["lambda"] == lam_v
            and sol["rho"] == rho_v and sol["p"] == p_v)
    formula = 5 + sol["Lambda"] / 3 - sol["lambda"] * sol["S"] ** 2 / 6
    check(same and sp.simplify(formula - sol["A"] ** 2) == 0,
          f"{name}: the numbers of the table and A^2 = 5 + Lambda/3 - lambda S^2/6")
    report(f"{name}: w = p/rho", sol["p"] / sol["rho"])
```

The computed numbers must equal the table of Section 12.26, and $A^2$ must equal Notebook 12b's formula $5 + \Lambda/3 - \lambda S^2/6$ (Exercise 7 derives it). The equations of state are $-1/2$, $0$ and $-3$.

**In [17], figure 4: both sides of the Einstein equations for example 3.**

```python
sol = solutions["example 3"]
G_diag = [G_space] * 3 + [G_time] + [G_extra] * 3 + [G_hidden]
left_side = np.array([[float(G_diag[mu].subs({A: 1, H: 1}) + sol["Lambda"])
                       if mu == nu else 0.0 for nu in range(8)] for mu in range(8)])
right_side = np.array([[float(sol["T"][mu][nu]) for nu in range(8)]
                       for mu in range(8)])
check(np.max(np.abs(left_side - right_side)) == 0.0,
      "example 3: the two 8 by 8 tables are equal entry by entry")
```

The two sides as 8 by 8 arrays of numbers; they agree exactly (the difference is 0.0, not merely small, because both come from exact numbers).

```python
fig, axes = plt.subplots(1, 3, figsize=(12.0, 4.4))
scale = np.abs(right_side).max()
panels = ((left_side, "$G^\\mu{}_\\nu + \\Lambda\\delta^\\mu_\\nu$"),
          (right_side, "$\\kappa T^\\mu{}_\\nu$ of the condensate"),
          (left_side - right_side, "difference"))
for ax, (values, title) in zip(axes, panels):
    ax.imshow(values, cmap="RdBu_r", vmin=-scale, vmax=scale)
    for mu in range(8):
        value = values[mu, mu]
        ink = "white" if abs(value) > 0.6 * scale else "black"  # readable on dark
        ax.text(mu, mu, f"{value:.0f}", ha="center", va="center", fontsize=7,
                color=ink)
```

Three heat maps with one common scale (left side, right side, difference), drawn as in Notebook 12a, In [20], with the diagonal values written in.

```python
    ax.set_xticks(range(8))
    ax.set_xticklabels(NAMES, fontsize=7)
    ax.set_yticks(range(8))
    ax.set_yticklabels(NAMES, fontsize=7)
    ax.grid(False)
    ax.set_title(title, fontsize=9)
fig.suptitle("Example 3 ($A = 1$, $\\Lambda = -30H^2$): the Einstein equations hold "
             "component by component")
save_figure(fig, "tensor_equality",
            ...)
```

**What the figure shows.** The two tables are identical: $-6$ at $x_4$ (minus the energy density 6) and $-18$ at the seven other diagonal places, white everywhere else; the difference is white throughout.

**In [18], figure 5: the solution in time.**

```python
sol = solutions["example 1"]
phi_numbers = np.array([complex(entry) for entry in sol["phi0"]])
biggest = np.argsort(-np.abs(phi_numbers), kind="stable")[:3]  # three components
times = np.linspace(0.0, 3.0, 601)  # x4 in units 1/H
```

$\Phi_0$ of example 1 as 16 complex floating-point numbers. `np.argsort` lists the positions in the order of the sorted values; sorting $-|\Phi_0|$ puts the largest first, `kind="stable"` keeps equal values in their original order (so that every computer chooses the same three), and `[:3]` keeps the first three positions.

```python
density = []
for x_value in times:  # S from the numbers, at every time (it must stay 12/5)
    phi_x = phi_numbers * np.exp(-4j * x_value)
    density.append((phi_x.conj() @ np.array(C.tolist(), dtype=float) @ phi_x).real)
density = np.array(density)
check(np.max(np.abs(density - 12 / 5)) < 1e-12,
      "example 1: S(x4) = 12/5 at every time (numerically)")
```

At 601 times the condensate $\Phi = e^{-4ix_4}\Phi_0$ is formed (`4j` is $4i$ in Python), and $S = \Phi^\dagger C\Phi$ is computed with `@`, the matrix product of numpy, and `.conj()`, the complex conjugate. It stays $12/5$ up to rounding.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
for index in sorted(biggest):
    left.plot(times, (phi_numbers[index] * np.exp(-4j * times)).real,
              label=f"Re $\\Phi_{{{index + 1}}}(x_4)$")
left.plot(times, density, color="black", linewidth=2.0,
          label="$S = \\bar\\Phi\\Phi = 12/5$")
left.set_ylim(-1.35, 4.0)  # room for the legend above the curves
left.set_xlabel("time $x_4$ (units $1/H$)")
left.set_ylabel("value")
left.set_title("example 1: the condensate oscillates, $S$ stays constant")
left.legend(fontsize=8, loc="upper center", ncol=2)
```

The real parts of the three largest components (numbered from 1 in the label) and the constant density; `ncol=2` arranges the legend in two columns.

```python
for name, style in (("example 1", "-"), ("example 2", "--")):
    slope = float(solutions[name]["A"])
    right.semilogy(times, np.exp(slope * times), style, color="tab:orange",
                   label=f"3-space $e^{{a_4}}$, {name}")
    right.semilogy(times, np.exp(-slope * times), style, color="tab:blue",
                   label=f"extra times $e^{{-a_4}}$, {name}")
right.set_xlabel("time $x_4$ (units $1/H$)")
right.set_ylabel("scale factor")
right.set_title("3-space inflates, the extra times deflate")
right.legend(fontsize=8)
save_figure(fig, "solution_in_time",
            ...)
```

The scale factors of examples 1 and 2 on a logarithmic axis. **What the figure shows.** The components oscillate with the period $2\pi/4 \approx 1.57$ while $S$ stays flat; the extra-time scale factor falls along straight lines of slope $-1$ (example 1) and $-\sqrt5$ (example 2): exponential deflation, driven by the condensate.

**In [19], figure 6: the family in the cosmological constant.**

```python
lam_axis = sp.symbols("Lambda_axis", real=True)
S_one = sp.Rational(12, 5)
m_family = -(36 + 2 * lam_axis) / S_one
lam_family = (-5 - m_family) / S_one
rho_family_line = m_family * S_one + lam_family * S_one ** 2 / 2
p_family_line = lam_family * S_one ** 2 / 2
check(sp.expand(rho_family_line - (-24 - lam_axis)) == 0
      and sp.expand(p_family_line - (12 + lam_axis)) == 0
      and m_family.subs(lam_axis, 0) == solutions["example 1"]["m"]
      and m_family.subs(lam_axis, -30) == solutions["example 3"]["m"],
      "A = 1 family: kappa rho = -24 - Lambda, kappa p = 12 + Lambda")
```

For $A = 1$, $M = -5$, $S = 12/5$ every $\Lambda$ gives a solution with $m = -(36 + 2\Lambda)/S$ and $\lambda = (M - m)/S$; then $\kappa\rho = -24 - \Lambda$ and $\kappa p = 12 + \Lambda$, and examples 1 and 3 are members.

```python
axis = np.linspace(-45.0, 15.0, 301)
functions = [sp.lambdify(lam_axis, f, "numpy") for f in
             (m_family, lam_family, rho_family_line, p_family_line)]
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
left.plot(axis, functions[0](axis), label="mass $m/H$")
left.plot(axis, functions[1](axis), "--", label="self-coupling $\\lambda$")
right.plot(axis, functions[2](axis), label="$\\kappa\\rho/H^2$")
right.plot(axis, functions[3](axis), "--", label="$\\kappa p/H^2$")
```

The four formulas as numpy functions of $\Lambda$, drawn from $-45$ to 15: parameters on the left, the source on the right.

```python
for ax in (left, right):
    ax.axvspan(-45.0, -24.0, color="tab:green", alpha=0.1)
    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.set_xlabel("cosmological constant $\\Lambda/H^2$")
for name, marker in (("example 1", "o"), ("example 3", "s")):
    sol = solutions[name]
    x_value = float(sol["Lambda"])
    left.plot([x_value] * 2, [float(sol["m"]), float(sol["lambda"])], marker,
              color="black")
    right.plot([x_value] * 2, [float(sol["rho"]), float(sol["p"])], marker,
               color="black", label=name)
left.set_title("the condensate's parameters ($A = 1$, $M = -5H$)")
right.set_title("the source it provides")
left.legend(fontsize=8)
right.legend(fontsize=8)
save_figure(fig, "family_in_lambda",
            ...)
```

The green band $\Lambda < -24$ in both panels, the zero lines, and black markers for the two examples. **What the figure shows.** Along the family $\rho + p = -12$ never changes; the energy density becomes positive only in the green band, and there $p < -\rho$: $w < -1$.

**In [20], the last check.**

```python
figure_names = ["condensate_frequency", "three_gamma_bilinears", "allowed_sources",
                "tensor_equality", "solution_in_time", "family_in_lambda"]
paths = [output_file(f"{FIGURE_FOLDER}/12d_{k}_{name}.png")
         for k, name in enumerate(figure_names, 1)]
check(all(path.is_file() for path in paths), "all six figure files exist")
all_checks_passed()
```

As in In [15] of Notebook 12b (Section 12.20): `figure_names` lists the short names of the six figures in the order in which they were drawn, `enumerate(figure_names, 1)` numbers them from 1, which gives the six file names `12d_1_condensate_frequency.png` to `12d_6_family_in_lambda.png`, and `output_file` gives the path where each was written. `path.is_file()` is true when the file exists, and `all` requires this of every one of the six. `all_checks_passed()` prints the last line, ALL 40 CHECKS PASSED (notebook 12d): 1 check in In [2], 2 in In [3], 1 in In [4], 4 in In [5], 3 in In [6], 1 in In [7], 3 in In [8], 2 in In [9], 2 in In [10], 2 in In [11], 1 in In [12], 2 in In [13], 9 in In [15], 3 in In [16], 1 in In [17], 1 in In [18], 1 in In [19] and 1 in In [20].

### 12.31 What we proved, what we computed, what we assumed

**PROVED** (exact). The table names, for each statement, the checks of the Revision record that verify it and the notebook cell of this chapter that reproduces them. "Sympy report" and "Wolfram report" are the two reports of the field equations in the folder `Revision/field_equations_a4/reports`; "lead's reports" are `einstein-gauss-bonnet-a4.json` and `emt-divergence-and-spin-connection.json` in `Revision/lead_checks/reports`.

| statement | where it is verified |
| --- | --- |
| $\sqrt{\lvert\det g\rvert} = \cos z$, independent of $a_4$: the 7-volume is constant | Wolfram report, `sqrt_abs_det_g_is_cos_z`; Notebook 12a, In [4] |
| 37 nonzero Christoffel symbols; 156 nonzero Riemann components, free of the warp and of $e^{a_4}$, polynomials in $\cot z$ and $1/\cot z$ | Notebook 12a, In [5]; sympy report, `mixed_riemann_free_of_warp_and_a4`, `riemann_entries_laurent`; In [8] |
| the Einstein tensor is diagonal, isotropic in 3-space and in the extra times, independent of $x_8$, with the four components of Section 12.6 | lead's report, `einstein_off_diagonal_zero`, `einstein_isotropy`, `einstein_x8_independent`; sympy report, `einstein_components`; In [12] |
| the three Lovelock tensors from the GKD equal the Rust record in all 64 components; $E_{(1)} = G$; each is divergence-free; $P_{(4)} = 0$ | sympy report, `P1_equals_gkd_branch_monomials` to `P3_equals_gkd_branch_monomials`, `P1_equals_minus_4_Einstein`, `E1_divergence_free` to `E3_divergence_free`; Wolfram report, `P4_vanishes_pigeonhole`; In [14] to In [19] |
| $E_{(2)}$ equals the classical Gauss-Bonnet tensor | Notebook 12a, In [18] (every $a_4$); lead's report, `gauss_bonnet_rho_alpha2`, `gauss_bonnet_p_alpha2` (linear member) |
| the field equations reduce to the constraint, the evolution equation $a_4''F(a_4') = \kappa(p_3 - p_t)$, the hidden equation and the conditions $p_3 + p_t = 2p_8$, no $x_8$ dependence, no mixed components | Wolfram report, `independent_components`; sympy report, `evolution_factorises`, `evolution_F_not_identically_zero`, `algebraic_identity`; In [21] and In [22] |
| the constraint propagates; the source obeys $\rho' = -3a_4'(p_3 - p_t)$ | sympy report, `bianchi_x4`, `conservation_components`; Wolfram report, `constraint_propagation_bianchi`; lead's report, `divergence_x4_component`, `divergence_x8_component`; In [23] and In [25] |
| Einstein gravity: no vacuum for $H > 0$; every source has $\kappa(\rho + p_8) = -6((a_4')^2 + H^2) < 0$ | sympy report, `einstein_null_energy_x8`; Wolfram report, `einstein_no_vacuum_solution`; lead's report, `no_vacuum_for_H_positive`; In [26] |
| the linear member needs $p_3 = p_t = p_8$ and constant $\rho$, $p$; $A$ enters only as $A^2$: the deflation of the extra times is a choice of sign | sympy report, `linear_member_equal_pressures`, `json_linear_member`; Notebook 12a, In [28]; Notebook 12b, In [4] |
| Einstein gravity: a positive energy density of the linear member needs $\Lambda < -(21 + 3A^2)H^2$ and has $w < -1$ | Notebook 12b, In [5] and In [8] |
| Einstein-Gauss-Bonnet gravity: among the linear members, vacua exist exactly for $0 < \alpha_2H^2 \le 1/40$ | sympy report, `linear_member_vacuum_factor`, `einstein_gauss_bonnet_vacuum_linear`; Notebook 12b, In [10] and In [11] |
| with the author's eight real 16 by 16 gammas: $\sum_\mu\gamma^\mu\Omega_\mu = 3H\gamma^{(x_8)}$; a condensate obeys $\Phi' = \mathcal{A}\Phi$, $\mathcal{A}^2 = -(M^2 - 9H^2)$, with constant $S$, $\rho = mS + \tfrac\lambda2S^2$, $p_3 = p_t = p_8 = \tfrac\lambda2S^2$ | sympy report, `authorT16_gravity_term`, `authorT16_condensate_S_constant`, `authorT16_condensate_kinetic_diagonal`; lead's report, `gamma_Omega_equals_3H_gamma8`; Notebook 12d, In [5] to In [12] |
| in Einstein gravity a condensate is a source of the linear member only if $\kappa MS = -6(A^2 + 1)H^2$ and $\kappa mS = -(36H^2 + 2\Lambda)$ | sympy and Wolfram reports, `condensate_einstein_quadratic_U`; Notebook 12b, In [13]; Notebook 12d, In [13] |
| three exact solutions of the coupled equations of Einstein gravity and dirac16complex00, two with the extra times deflating as $e^{-Hx_4}$: all 16 field-equation components and all 64 Einstein components hold, for $+A$ and $-A$ | Notebook 12d, In [15]: a computation of this book, not a Revision record, under the assumptions listed below |

**COMPUTED** (numerical, with measured accuracy; Notebook 12c): RK4 integrations of the evolution equation for prescribed stresses, agreeing with the exact solutions to $9 \times 10^{-11}$ (pulse, step 0.01) and to better than $10^{-9}$, the bound of the check (relaxing stress); measured convergence orders 4.24, 4.12, 4.06, 4.03; the energy density from conservation agrees with the constraint to $2 \times 10^{-11}$; the Gauss-Bonnet breakdown is reached at the predicted times $x_4^{\star} = 2.4682/H$ ($\alpha_2H^2 = 0.005$) and $0.4498/H$ ($\alpha_2H^2 = 0.01$) within 0.01; the eigenvalues of $\mathcal{A}$ agree with $\pm iw$ to $10^{-14}$, eight of each sign (Notebook 12d, In [7]); the ratio $(\int p_3 + \int p_t)/(2\int p_8)$ of the 70 recorded Kohn-Sham states with a nonzero energy-momentum tensor, recomputed from the record's table `Revision/kohn_sham/results/ground/emt-integrals.csv` and equal to the record, is nowhere closer to the required 1 than 0.414328 (Notebook 12c, In [16]).

**ASSUMED**: the stresses of Notebook 12c (test inputs; no field of the theory is known to produce them); Einstein gravity and the sign convention $\sigma_T = +1$ of the energy-momentum tensor in Notebook 12d; the classical commuting field dirac16complex00 (not the quantised dirac16complex) as the source there; the chosen values of $\Lambda$, $m$, $\lambda$ and of the Lovelock couplings; Lovelock's theorem is quoted from the literature, not proved.

**HYPOTHESIS**: none is used in this chapter.

**OPEN**: whether the condensates of Notebook 12d are stable and how they could arise; whether any state of the quantised field dirac16complex is an admissible source (the recorded Kohn-Sham states are not: `Revision/field_equations_a4/reports/ks-source-conditions.json`, every one of its checks PASS, its numbers recomputed in Notebook 12c, In [15] and In [16]); the values of $\alpha_2$, $\alpha_3$, $\Lambda$ and $\kappa$ in nature. Nothing in this chapter concerns the creation of universes, in pairs or otherwise, or the asymmetry between matter and antimatter: the symmetry $A \to -A$ relates two histories of one metric and is not the pairing of universes of masses $+m$ and $-m$, whose exact statement and limits are the subject of Chapters 18 to 21.

### 12.32 Exercises

**Exercise 1.** Compute $\Gamma^{x_5}{}_{x_5x_8}$ and $\Gamma^{x_8}{}_{x_5x_5}$ by hand from the diagonal formula of Section 12.4.

*Answer.* $g_{55} = -e^{-2a_4}\sin^{1/3}z$, and $\partial_8 g_{55} = 6H\cdot(-e^{-2a_4})\tfrac13\sin^{-2/3}z\cos z = 2H\cot z\;g_{55}$. First symbol ($a = c = x_5$, $b = x_8$, the term with $\delta_{ac}$): $\Gamma^{x_5}{}_{x_5x_8} = \partial_8 g_{55}/(2g_{55}) = H\cot z$. Second ($b = c = x_5$, $a = x_8$, the term with $\delta_{bc}$): $\Gamma^{x_8}{}_{x_5x_5} = -\partial_8 g_{55}/(2g_{88}) = -2H\cot z\,g_{55}/(2\cot^2 z) = -H\tan z\;g_{55} = He^{-2a_4}\sin^{1/3}z\,\tan z = He^{-2a_4}\sin^{4/3}z/\cos z$. Both agree with Out [6] of Notebook 12a.

**Exercise 2.** Compute the pair curvature $K_{x_5x_6}$ of two extra times by hand.

*Answer.* With $a = m = x_5$, $b = n = x_6$ the derivative terms vanish ($\Gamma^{x_5}{}_{x_6x_6} = \Gamma^{x_5}{}_{x_6x_5} = 0$, because $g_{55}$ does not depend on $x_6$), and so does the last sum. The remaining sum has $e = x_4$ and $e = x_8$: $R^{x_5}{}_{x_6x_5x_6} = \Gamma^{x_5}{}_{x_5x_4}\Gamma^{x_4}{}_{x_6x_6} + \Gamma^{x_5}{}_{x_5x_8}\Gamma^{x_8}{}_{x_6x_6} = (-a_4')(-a_4'g_{66}) + H\cot z\,(-H\tan z\,g_{66}) = \big((a_4')^2 - H^2\big)g_{66}$ (Section 12.4: $\Gamma^{x_4}{}_{x_6x_6} = -a_4'g_{66}$ and $\Gamma^{x_8}{}_{x_6x_6} = -H\tan z\,g_{66}$). Raising with $g^{66} = 1/g_{66}$: $K_{x_5x_6} = (a_4')^2 - H^2$, the same as for two 3-space directions (the table of Section 12.5).

**Exercise 3.** Use the rule $G^h{}_h = -\sum_{\text{pairs not containing } h}K$ to compute all diagonal components of the Einstein tensor for the canonical history $a_4 = Hx_4$, and from them the required $\kappa\rho$, $\kappa p$ and $w$ for $\Lambda = 0$.

*Answer.* With $a_4' = H$, $a_4'' = 0$ the pair curvatures are: two 3-space directions or two extra times $0$; 3-space with extra time $-2H^2$; 3-space or extra time with the time $H^2$; with $x_8$ $-H^2$; time with $x_8$ $0$. Pairs without $x_4$: $9\cdot(-2H^2) + 6\cdot(-H^2) = -24H^2$, so $G^{x_4}{}_{x_4} = 24H^2$. Pairs without $x_8$: $9\cdot(-2H^2) + 6\cdot H^2 = -12H^2$, so $G^{x_8}{}_{x_8} = 12H^2$. Pairs without $x_1$: six mixed pairs ($-12H^2$), five time pairs ($+5H^2$), five with $x_8$ ($-5H^2$): $-12H^2$, so $G^{x_1}{}_{x_1} = 12H^2$, and the same for an extra time. Then $\kappa\rho = -G^{x_4}{}_{x_4} = -24H^2$, $\kappa p = 12H^2$, $w = 12/(-24) = -1/2$, as in Notebook 12b, In [5]. Check with the formulas: $3H^2 + 21H^2 = 24H^2$ and $15H^2 - 3H^2 = 12H^2$.

**Exercise 4.** In Einstein gravity, for the canonical history ($A = 1$), which cosmological constant makes the required energy density zero? What are then the pressure and $\rho + p$? Is this a vacuum?

*Answer.* $\kappa\rho = -24H^2 - \Lambda = 0$ gives $\Lambda = -24H^2$. Then $\kappa p = 12H^2 + \Lambda = -12H^2$ and $\kappa(\rho + p) = -12H^2$, as the formula $-6(1 + A^2)H^2$ says. The pressure is not zero, so this is not a vacuum: a source with zero energy density and negative pressure is still needed.

**Exercise 5.** In Einstein-Gauss-Bonnet gravity, find the coupling $\alpha_2H^2$ for which the canonical history $A = 1$ is a vacuum, and the cosmological constant it needs. Check that the pressure vanishes too.

*Answer.* $V = 1 - 8\alpha_2H^2(A^2 + 5) = 1 - 48\alpha_2H^2 = 0$ gives $\alpha_2H^2 = 1/48$ (the point checked in Notebook 12b, In [12]). With $\alpha_1 = 1$, $\alpha_3 = 0$: $\kappa\rho = -(21 + 3)H^2 + \alpha_2H^4(36 + 120 + 420) - \Lambda = -24H^2 + 576H^2/48 - \Lambda = -12H^2 - \Lambda$, which is zero for $\Lambda = -12H^2$. The pressure: $\kappa p = (15 - 3)H^2 + 12\alpha_2H^4(1 + 14 - 15) + \Lambda = 12H^2 + 0 - 12H^2 = 0$. (The formula of Notebook 12b, $\Lambda = 720H^4\alpha_2 - 36H^2 + 3/(16\alpha_2)$, gives $15H^2 - 36H^2 + 9H^2 = -12H^2$ as well.)

**Exercise 6.** Show, for Einstein gravity, that if the constraint holds at every time and the source obeys the conservation law $\rho' = -3a_4'(p_3 - p_t)$, then the evolution equation holds wherever $a_4' \ne 0$.

*Answer.* Differentiate the constraint $-\kappa\rho = 3(a_4')^2 + 21H^2 + \Lambda$: $-\kappa\rho' = 6a_4'a_4''$. Insert the conservation law on the left: $3a_4'\kappa(p_3 - p_t) = 6a_4'a_4''$. Where $a_4' \ne 0$ divide by $3a_4'$: $\kappa(p_3 - p_t) = 2a_4''$, the evolution equation. (Where $a_4' = 0$ the division is not allowed, and the evolution equation is an independent statement.)

**Exercise 7.** A condensate with $U = \tfrac\lambda2S^2$ is the source of the linear member in Einstein gravity. Derive Notebook 12b's formula $A^2 = 5 + \Lambda/3 - \lambda S^2/6$ (units $H = \kappa = 1$) and check it on example 3 of Section 12.26.

*Answer.* The two conditions read $MS = -6(A^2 + 1)$ and $mS = -(36 + 2\Lambda)$. Since $M = m + \lambda S$: $MS = mS + \lambda S^2 = -(36 + 2\Lambda) + \lambda S^2$. So $-6(A^2 + 1) = -36 - 2\Lambda + \lambda S^2$, hence $A^2 + 1 = 6 + \Lambda/3 - \lambda S^2/6$ and $A^2 = 5 + \Lambda/3 - \lambda S^2/6$. Example 3: $\Lambda = -30$, $\lambda = -25/4$, $S = 12/5$: $5 - 10 + \tfrac{25}{4}\cdot\tfrac{144}{25}\cdot\tfrac16 = 5 - 10 + 6 = 1 = A^2$.

**Exercise 8.** In Einstein-Gauss-Bonnet gravity with $\alpha_2H^2 = 0.01$, a constant stress $\kappa\Delta = 0.5H^2$ acts from $a_4'(0) = H$. Compute the critical rate and the breakdown time (units $H = 1$).

*Answer.* $F(v) = 2 - 0.8 - 0.48v^2 = 1.2 - 0.48v^2$ vanishes at $v_c = \sqrt{1.2/0.48} = \sqrt{2.5} \approx 1.5811$. $G(v) = 1.2v - 0.16v^3$: $G(v_c) = 1.2\cdot1.58114 - 0.16\cdot3.95285 \approx 1.89737 - 0.63246 = 1.26491$ (using $v_c^3 = 2.5\,v_c$), and $G(1) = 1.2 - 0.16 = 1.04$. So $x_4^{\star} = (1.26491 - 1.04)/0.5 \approx 0.4498$, the value of Notebook 12c, In [13].

**Exercise 9.** For the relaxing stress of Section 12.21, by how much does the extra-time scale factor $e^{-a_4}$ end up smaller than on the history $a_4 = x_4$, for $\eta = 0.5$?

*Answer.* $a_4 - x_4 = (1 - e^{-\eta x_4})/\eta \to 1/\eta = 2$ for large $x_4$. So $e^{-a_4} = e^{-x_4}e^{-(a_4 - x_4)} \to e^{-x_4}e^{-2}$: the extra times end up smaller by the factor $e^{-2} \approx 0.135$ than on the canonical history, because they deflated faster at first.

**Exercise 10.** Show that $\mathcal{A} = -\gamma^{(x_4)}(M - 3H\gamma^{(x_8)})$ has the eigenvalues $\pm i\sqrt{M^2 - 9H^2}$ when $M^2 > 9H^2$ and $\pm\sqrt{9H^2 - M^2}$ when $M^2 < 9H^2$. What is the period of the condensate for $M = -5H$?

*Answer.* If $\mathcal{A}v = \mu v$ for a nonzero $v$, then $\mathcal{A}^2v = \mu^2v$; with $\mathcal{A}^2 = -(M^2 - 9H^2)$ (Section 12.26) this gives $\mu^2 = 9H^2 - M^2$. For $M^2 > 9H^2$ the right-hand side is negative and $\mu$ is one of $\pm i\sqrt{M^2 - 9H^2}$; for $M^2 < 9H^2$ it is positive and $\mu$ is one of $\pm\sqrt{9H^2 - M^2}$, real: solutions grow or decay. This shows only that no other value occurs; that both signs occur, each 8 times, follows from the **trace** (the sum of the diagonal entries), which equals the sum of the 16 eigenvalues, each counted as often as it occurs. Write $\mathcal{A} = -M\gamma^{(x_4)} + 3H\gamma^{(x_4)}\gamma^{(x_8)}$. Then $\mathrm{tr}\,\gamma^{(x_4)} = \mathrm{tr}\big(\gamma^{(x_8)}\gamma^{(x_8)}\gamma^{(x_4)}\big) = \mathrm{tr}\big(\gamma^{(x_8)}\gamma^{(x_4)}\gamma^{(x_8)}\big) = -\mathrm{tr}\big(\gamma^{(x_8)}\gamma^{(x_8)}\gamma^{(x_4)}\big) = -\mathrm{tr}\,\gamma^{(x_4)}$, so $\mathrm{tr}\,\gamma^{(x_4)} = 0$ (first $(\gamma^{(x_8)})^2 = 1$; then $\mathrm{tr}(XY) = \mathrm{tr}(YX)$ with $X = \gamma^{(x_8)}$, which moves the first factor to the end; then the Clifford relation $\gamma^{(x_4)}\gamma^{(x_8)} = -\gamma^{(x_8)}\gamma^{(x_4)}$; then $(\gamma^{(x_8)})^2 = 1$ again). In the same way $\mathrm{tr}\big(\gamma^{(x_4)}\gamma^{(x_8)}\big) = \mathrm{tr}\big(\gamma^{(x_8)}\gamma^{(x_4)}\big) = -\mathrm{tr}\big(\gamma^{(x_4)}\gamma^{(x_8)}\big) = 0$. So $\mathrm{tr}\,\mathcal{A} = 0$. If $n_+$ eigenvalues equal $+\mu_0$ and $n_-$ equal $-\mu_0$, with $\mu_0 \ne 0$ (here $M^2 \ne 9H^2$), then $n_+ + n_- = 16$ and $\mathrm{tr}\,\mathcal{A} = (n_+ - n_-)\mu_0 = 0$, hence $n_+ = n_- = 8$. For $M^2 > 9H^2$ this also follows from $\mathcal{A}$ being real (Section 12.26). For $M = -5H$: $w = \sqrt{25 - 9}\,H = 4H$, and $e^{-iwx_4}$ repeats after $x_4 = 2\pi/w = \pi/(2H) \approx 1.57/H$.
