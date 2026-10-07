## 9. The energy-momentum tensor, pressures, equations of state, conservation identities

Gravity has to be told where the energy is. In Einstein's theory, and in the Einstein-Lovelock theory that Chapter 12 uses for the author's metric, the right-hand side of the field equations is a table of numbers called the energy-momentum tensor. It says, at every point, how much energy there is in a unit of volume, how hard the matter pushes in each direction (the pressures), and how energy and momentum flow. This chapter builds that table for the field dirac16complex00 in the author's primordial metric, splits it into a kinetic part and a potential part, defines the energy density, the pressures of 3-space, of the extra times and of the hidden direction, and the equations of state, and derives the two exact conservation identities that the table obeys: one along the time $x_4$, which describes how energy flows between the inflating 3-space and the deflating extra times, and one along the hidden direction $x_8$. Three notebooks compute every statement anew from the Revision record: Notebook 09a builds the tensor at one point and derives the two identities, Notebook 09b studies the condensates (fields that depend on the time only) and their equations of state, and Notebook 09c computes the complete tensor of a condensate, including the entries off the diagonal that the spin connection creates.

### 9.1 What this chapter does

**Why we need this chapter.** Cosmologists describe the matter of the universe, at each moment, by two numbers: the **energy density** $\rho$ (energy per unit volume) and the **pressure** $p$ (the push per unit area, which is also energy per unit volume). Their ratio $w = p/\rho$ is called the **equation of state**. Three values are famous: dust (matter at rest whose particles do not push on each other) has $w = 0$, radiation (light) has $w = 1/3$, and a cosmological constant (the simplest model of dark energy) has $w = -1$. The author's hypotheses say that the fields dirac16complex and dirac16complex00 might provide a time-varying equation of state for dark energy or dark matter. Before anyone can test such a statement, one must know exactly what $\rho$ and $p$ are for these fields in the author's eight-dimensional metric. That is what this chapter derives.

**What it does.** In eight dimensions there is one energy density and seven pressures, one for each direction other than the time $x_4$. They come in three families: the pressure $p_3$ of the three directions of ordinary space, the pressure $p_t$ of the three extra times, and the pressure $p_8$ of the hidden direction. The chapter

- defines the energy-momentum tensor by the response of the action to a change of the metric, and derives from this definition, line by line, its diagonal entries $T^\mu{}_\mu = L_0 - K_\mu$ (Section 9.5);
- states the complete tensor and proves that it is real and symmetric (Section 9.6);
- splits the energy density and the pressures into kinetic and potential parts and defines the equations of state (Section 9.7);
- derives the trace identity and the values that the field equation imposes (Section 9.8);
- derives the covariant divergence of a diagonal tensor in the author's metric and from it the two conservation identities (Sections 9.9 to 9.11);
- shows where the spin connection, which drops out of the Lagrangian, does enter the tensor (Section 9.12);
- builds the exact condensates, computes their equation of state $w = x/(2 + x)$ with $x = \lambda S/m$, and shows that the energy of the commuting field has no lower bound (Sections 9.18 to 9.21);
- computes the complete tensor of a condensate, with 42 entries off the diagonal, and the exact condensates whose tensor is diagonal (Section 9.26).

**What it does not do.** The equation of state that an observer living in 3-space would infer (after integrating over the hidden direction and the extra times), its change in time and any comparison with supernova data are not part of the Revision record: they are OPEN, and this chapter claims nothing about them. The quantised field dirac16complex obeys the same formulas as operators; this chapter computes numbers only for the commuting field dirac16complex00 (Section 9.13).

**Labels.** As everywhere in the book, every statement carries one of five labels: PROVED (exact; the Revision report file and the name of its check are given), COMPUTED (a number of a notebook, with its accuracy), ASSUMED, HYPOTHESIS, OPEN.

### 9.2 The stage: coordinates, metric and the field dirac16complex00

**Coordinates.** The eight coordinates are named as the author names them: $x_1, x_2, x_3$ are ordinary 3-space; $x_4$ is the time in which everything evolves; $x_5, x_6, x_7$ are the three **extra times**, which behave like time and deflate exponentially; $x_8$ is the **hidden** space direction. We write $z = 6Hx_8$, where $H > 0$ is the author's constant; $z$ lies between $0$ and $\pi/2$. In formulas the letter $i$ always stands for one of the 3-space directions $x_1, x_2, x_3$, and the letter $t$ for one of the extra times $x_5, x_6, x_7$.

**The metric.** The author's metric is diagonal (Chapter 3). We write it with eight positive **vielbein factors** $f_1, \dots, f_8$:

$$
g = \mathrm{diag}\big(f_1^2,\, f_2^2,\, f_3^2,\, -f_4^2,\, -f_5^2,\, -f_6^2,\, -f_7^2,\, f_8^2\big),
$$

$$
f_1 = f_2 = f_3 = e^{a_4}\sin^{1/6}z, \quad f_4 = 1, \quad f_5 = f_6 = f_7 = e^{-a_4}\sin^{1/6}z, \quad f_8 = \cot z .
$$

So $g_{x_1x_1} = e^{2a_4}\sin^{1/3}z$, $g_{x_4x_4} = -1$, $g_{x_5x_5} = -e^{-2a_4}\sin^{1/3}z$ and $g_{x_8x_8} = \cot^2 z$, exactly the author's entries. A small step $dx_\mu$ along the direction $x_\mu$ has the proper length $f_\mu\,|dx_\mu|$; that is the meaning of $f_\mu$. With the frame metric $\eta = \mathrm{diag}(+1, +1, +1, -1, -1, -1, -1, +1)$ in the order $x_1, \dots, x_8$ every entry is $g_{\mu\mu} = \eta_{\mu\mu}f_\mu^2$. The function $a_4(x_4)$ grows with the time: then the 3-space factor $e^{a_4}$ grows (3-space inflates) and the extra-time factor $e^{-a_4}$ shrinks (the extra times deflate). We write $a_4' = da_4/dx_4$. The examples of this chapter take $a_4 = AHx_4$ with $A = 1$ (the deflating history that the Kohn-Sham part of the book uses as a prescribed background) and, in Notebook 09c, the curved history $a_4 = 0.3x_4 + 0.05x_4^2$; every identity of the chapter holds for every function $a_4$. Which $a_4$ the field equations of gravity allow, and with which source, is the subject of Chapter 12.

**The volume factor.** The product of the eight factors is the volume factor $\sqrt{|g|}$ (the square root of the absolute value of the determinant of the diagonal matrix $g$, which is the product of its diagonal entries):

$$
\begin{aligned}
\sqrt{|g|} &= f_1 f_2 f_3\, f_4\, f_5 f_6 f_7\, f_8 \\
&= \big(e^{a_4}\sin^{1/6}z\big)^3 \cdot 1 \cdot \big(e^{-a_4}\sin^{1/6}z\big)^3 \cdot \cot z \\
&= e^{3a_4}\sin^{1/2}z \cdot e^{-3a_4}\sin^{1/2}z \cdot \frac{\cos z}{\sin z} \\
&= \cos z .
\end{aligned}
$$

The first line is the definition; the second inserts the factors; the third multiplies the powers ($(e^{a_4})^3 = e^{3a_4}$, $(\sin^{1/6}z)^3 = \sin^{1/2}z$) and writes $\cot z = \cos z/\sin z$; the fourth uses $e^{3a_4}e^{-3a_4} = 1$ and $\sin^{1/2}z\,\sin^{1/2}z = \sin z$. The volume factor does not depend on the time $x_4$: the growth of 3-space and the shrinking of the extra times cancel exactly (PROVED; `Revision/theory/reports/python-field-theory.json`, check `sqrt_det_g_equals_cos_z`).

**The gamma matrices.** The book uses the author's eight **real** $16 \times 16$ gamma matrices (Chapter 4), stored in the Revision fixture `Revision/algebra/gammas.json` in the order $x_1, \dots, x_8$. We write them $\gamma^{(1)}, \dots, \gamma^{(8)}$ ($\gamma^{(4)}$ means $\gamma^{(x_4)}$, and so on). They obey the Clifford relations $\gamma^{(a)}\gamma^{(b)} + \gamma^{(b)}\gamma^{(a)} = 2\eta^{ab}\cdot 1$. Two consequences are used again and again in this chapter: the square of each gamma is $\eta_{aa}$ times the unit matrix ($+1$ for $x_1, x_2, x_3, x_8$ and $-1$ for $x_4, \dots, x_7$), and two different gammas anticommute, $\gamma^{(a)}\gamma^{(b)} = -\gamma^{(b)}\gamma^{(a)}$ for $a \neq b$. The matrix $C = \gamma^{(8)}\gamma^{(1)}\gamma^{(2)}\gamma^{(3)}$ (Chapter 5) is real and symmetric, $C^2 = 1$, and every product $C\gamma^{(a)}$ is antisymmetric: $(C\gamma^{(a)})^T = -C\gamma^{(a)}$ (PROVED; `Revision/algebra/reports/python-algebra.json`, checks `clifford_relation`, `C_real_symmetric_involution` and `C_gamma_antisymmetric`). The **coordinate gammas** are $\gamma^\mu = \gamma^{(\mu)}/f_\mu$ (no sum), and with a lower index $\gamma_\mu = g_{\mu\mu}\gamma^\mu = \eta_{\mu\mu}f_\mu\gamma^{(\mu)}$.

**The field.** dirac16complex00 is a column $\Phi$ of 16 ordinary (commuting) complex numbers at every point (Chapter 7). Its **Dirac adjoint** is the row $\bar\Phi = \Phi^\dagger C$ (the dagger means: transpose and take the complex conjugate of every entry), and the **scalar** is the number $S = \bar\Phi\Phi = \Phi^\dagger C\Phi$. The potential is $U(S) = \frac{\lambda}{2}S^2$, so $U'(S) = \lambda S$; $m$ is the mass.

**The spin connection and the covariant derivative** (Chapter 6). For the diagonal vielbein of this metric the spin connection is

$$
\begin{aligned}
\Omega_{x_i} &= \tfrac12 f_i\,\big(a_4'\,\gamma^{(i)}\gamma^{(4)} + H\,\gamma^{(i)}\gamma^{(8)}\big), \qquad i = 1, 2, 3, \\
\Omega_{x_t} &= -\tfrac12 f_t\,\big(a_4'\,\gamma^{(4)}\gamma^{(t)} + H\,\gamma^{(t)}\gamma^{(8)}\big), \qquad t = 5, 6, 7, \\
\Omega_{x_4} &= \Omega_{x_8} = 0,
\end{aligned}
$$

with $f_i = e^{a_4}\sin^{1/6}z$ and $f_t = e^{-a_4}\sin^{1/6}z$ (Revision record `Revision/theory/field-theory.json`, formula `Omega_components`). The covariant derivatives are $D_\mu\Phi = \partial_\mu\Phi + \Omega_\mu\Phi$ and $D_\mu\bar\Phi = \partial_\mu\bar\Phi - \bar\Phi\,\Omega_\mu$, where $\partial_\mu$ is the partial derivative with respect to $x_\mu$.

**The Lagrangian.** The Lagrangian density is $\mathcal{L} = \sqrt{|g|}\,L_0$ with

$$
L_0 = \tfrac12\sum_\mu\big(\bar\Phi\gamma^\mu D_\mu\Phi - (D_\mu\bar\Phi)\gamma^\mu\Phi\big) - mS - U(S),
$$

and its Euler-Lagrange equation is the **field equation** $\gamma^\mu D_\mu\Phi = V\Phi$ with the **effective mass** $V = m + U'(S) = m + \lambda S$ (Chapter 7). Written out in the author's metric (record formula `field_equation`) it reads

$$
\sum_{a=1}^{8}\frac{1}{f_a}\,\gamma^{(a)}\partial_a\Phi + 3H\gamma^{(8)}\Phi = V\Phi ,
$$

and because $(\gamma^{(4)})^2 = -1$ and $f_4 = 1$ it can be solved for the time derivative (the **evolution form**; multiply by $-\gamma^{(4)}$):

$$
\partial_4\Phi = -\gamma^{(4)}\Big[V\Phi - \sum_{a \neq 4}\frac{1}{f_a}\,\gamma^{(a)}\partial_a\Phi - 3H\gamma^{(8)}\Phi\Big].
$$

A configuration that satisfies the field equation is said to be **on shell**; one that need not satisfy it is **off shell**. Some identities of this chapter hold off shell (for every configuration), others only on shell; each statement says which.

### 9.3 Two exact facts about the spin connection of this metric

Two facts about $\Omega_\mu$ decide where the spin connection appears in the energy-momentum tensor. Both are proved here line by line.

**Fact 1: for every direction separately, $\gamma^\mu\Omega_\mu + \Omega_\mu\gamma^\mu = 0$ (no sum).** For $x_4$ and $x_8$ this is clear, because $\Omega_{x_4} = \Omega_{x_8} = 0$. Take a 3-space direction $x_i$:

$$
\begin{aligned}
\gamma^{x_i}\Omega_{x_i} &= \frac{1}{f_i}\gamma^{(i)}\cdot\tfrac12 f_i\big(a_4'\gamma^{(i)}\gamma^{(4)} + H\gamma^{(i)}\gamma^{(8)}\big) \\
&= \tfrac12\big(a_4'\,\gamma^{(i)}\gamma^{(i)}\gamma^{(4)} + H\,\gamma^{(i)}\gamma^{(i)}\gamma^{(8)}\big) \\
&= \tfrac12\big(a_4'\gamma^{(4)} + H\gamma^{(8)}\big).
\end{aligned}
$$

The first line inserts $\gamma^{x_i} = \gamma^{(i)}/f_i$ and the formula for $\Omega_{x_i}$; the second cancels $1/f_i$ against $f_i$ and multiplies out the bracket; the third uses $\gamma^{(i)}\gamma^{(i)} = \eta_{ii} = +1$. In the other order:

$$
\begin{aligned}
\Omega_{x_i}\gamma^{x_i} &= \tfrac12\big(a_4'\,\gamma^{(i)}\gamma^{(4)}\gamma^{(i)} + H\,\gamma^{(i)}\gamma^{(8)}\gamma^{(i)}\big) \\
&= \tfrac12\big(-a_4'\,\gamma^{(i)}\gamma^{(i)}\gamma^{(4)} - H\,\gamma^{(i)}\gamma^{(i)}\gamma^{(8)}\big) \\
&= -\tfrac12\big(a_4'\gamma^{(4)} + H\gamma^{(8)}\big).
\end{aligned}
$$

The first line is the same insertion; the second exchanges the last two gammas of each product, which costs a minus sign because different gammas anticommute ($\gamma^{(4)}\gamma^{(i)} = -\gamma^{(i)}\gamma^{(4)}$, $\gamma^{(8)}\gamma^{(i)} = -\gamma^{(i)}\gamma^{(8)}$); the third uses $\gamma^{(i)}\gamma^{(i)} = 1$ again. Adding the two results gives zero. Now an extra time $x_t$, with $\Omega_{x_t} = -\frac12 f_t(a_4'\gamma^{(4)}\gamma^{(t)} + H\gamma^{(t)}\gamma^{(8)})$:

$$
\begin{aligned}
\gamma^{x_t}\Omega_{x_t} &= -\tfrac12\big(a_4'\,\gamma^{(t)}\gamma^{(4)}\gamma^{(t)} + H\,\gamma^{(t)}\gamma^{(t)}\gamma^{(8)}\big) \\
&= -\tfrac12\big(-a_4'\,\gamma^{(t)}\gamma^{(t)}\gamma^{(4)} + H\,\gamma^{(t)}\gamma^{(t)}\gamma^{(8)}\big) \\
&= -\tfrac12\big(a_4'\gamma^{(4)} - H\gamma^{(8)}\big) = -\tfrac{a_4'}{2}\gamma^{(4)} + \tfrac{H}{2}\gamma^{(8)} .
\end{aligned}
$$

The first line inserts $\gamma^{x_t} = \gamma^{(t)}/f_t$ and cancels $f_t$; the second exchanges $\gamma^{(4)}$ and $\gamma^{(t)}$ in the first product (a minus sign); the third uses $\gamma^{(t)}\gamma^{(t)} = \eta_{tt} = -1$ in both products and multiplies out. In the same way

$$
\Omega_{x_t}\gamma^{x_t} = -\tfrac12\big(a_4'\,\gamma^{(4)}\gamma^{(t)}\gamma^{(t)} + H\,\gamma^{(t)}\gamma^{(8)}\gamma^{(t)}\big) = -\tfrac12\big(-a_4'\gamma^{(4)} + H\gamma^{(8)}\big) = \tfrac{a_4'}{2}\gamma^{(4)} - \tfrac{H}{2}\gamma^{(8)},
$$

where the middle step uses $\gamma^{(t)}\gamma^{(t)} = -1$ in the first product and, in the second, $\gamma^{(8)}\gamma^{(t)} = -\gamma^{(t)}\gamma^{(8)}$ followed by $\gamma^{(t)}\gamma^{(t)} = -1$ (two minus signs). The sum is again zero. Fact 1 is PROVED (Revision record `Revision/field_equations_a4/reports/wolfram-a4-report.json`, check `gamma_mu_anticommutes_with_Omega_mu_no_sum`).

**Fact 2: summed over the directions, $\gamma^\mu\Omega_\mu = 3H\gamma^{(8)}$.** Add the results above over the three 3-space directions and the three extra times (the directions $x_4$ and $x_8$ give zero):

$$
\sum_\mu\gamma^\mu\Omega_\mu = 3\cdot\tfrac12\big(a_4'\gamma^{(4)} + H\gamma^{(8)}\big) + 3\cdot\big(-\tfrac{a_4'}{2}\gamma^{(4)} + \tfrac{H}{2}\gamma^{(8)}\big) = \big(\tfrac{3a_4'}{2} - \tfrac{3a_4'}{2}\big)\gamma^{(4)} + \big(\tfrac{3H}{2} + \tfrac{3H}{2}\big)\gamma^{(8)} = 3H\gamma^{(8)} .
$$

The terms with $a_4'$ cancel: the three inflating directions and the three deflating directions contribute equal and opposite amounts. The cancellation is due to the deflation. The lead's independent check computes the same sum for a metric in which the extra times inflate like 3-space and finds that a term $3a_4'\gamma^{(4)}$ survives (PROVED; `Revision/lead_checks/reports/emt-divergence-and-spin-connection.json`, checks `gamma_Omega_equals_3H_gamma8` and `negative_control_inflating_extra_times`; also `Revision/theory/reports/python-field-theory.json`, check `gamma_mu_Omega_mu_equals_3H_gamma_x8`).

**What Fact 1 does to the Lagrangian.** Insert $D_\mu\Phi = \partial_\mu\Phi + \Omega_\mu\Phi$ and $D_\mu\bar\Phi = \partial_\mu\bar\Phi - \bar\Phi\Omega_\mu$ into one term of $L_0$:

$$
\begin{aligned}
\tfrac12\big(\bar\Phi\gamma^\mu D_\mu\Phi - (D_\mu\bar\Phi)\gamma^\mu\Phi\big) &= \tfrac12\big(\bar\Phi\gamma^\mu\partial_\mu\Phi - \partial_\mu\bar\Phi\,\gamma^\mu\Phi\big) + \tfrac12\,\bar\Phi\big(\gamma^\mu\Omega_\mu + \Omega_\mu\gamma^\mu\big)\Phi \\
&= \frac{1}{2f_\mu}\big(\bar\Phi\gamma^{(\mu)}\partial_\mu\Phi - \partial_\mu\bar\Phi\,\gamma^{(\mu)}\Phi\big) = K_\mu .
\end{aligned}
$$

The first line collects the terms with $\Omega_\mu$ (the term $+\bar\Phi\Omega_\mu\gamma^\mu\Phi$ comes from $-(-\bar\Phi\Omega_\mu)\gamma^\mu\Phi$); the second drops them by Fact 1 and writes $\gamma^\mu = \gamma^{(\mu)}/f_\mu$. The number $K_\mu$ (no sum) is called the **kinetic term of the direction** $x_\mu$: the part of the Lagrangian that holds the derivative along $x_\mu$. So

$$
L_0 = \sum_\mu K_\mu - mS - U(S), \qquad K_\mu = \frac{1}{2f_\mu}\big(\bar\Phi\gamma^{(\mu)}\partial_\mu\Phi - \partial_\mu\bar\Phi\,\gamma^{(\mu)}\Phi\big).
$$

The spin connection has disappeared from the Lagrangian; it reaches the field equation only through Fact 2 (the term $3H\gamma^{(8)}\Phi$), and the energy-momentum tensor only off its diagonal (Section 9.12).

### 9.4 What an energy-momentum tensor is

**A table of $8 \times 8$ numbers.** The energy-momentum tensor $T^\nu{}_\mu$ is, at every point, a table of 64 numbers, one for each ordered pair of directions $(\nu, \mu)$. We write the upper index $\nu$ as the row and the lower index $\mu$ as the column. The entries on the diagonal ($\nu = \mu$) are the energy density and the pressures; the entries off the diagonal ($\nu \neq \mu$) describe flows: the entries with one index $x_4$ hold the density of momentum and the flow of energy along the other direction, and the entries with two indices other than $x_4$ hold shearing stresses. Lowering the upper index with the metric gives $T_{\nu\mu} = g_{\nu\nu}T^\nu{}_\mu$ (the metric is diagonal, so no sum is needed).

**A familiar example.** In ordinary four-dimensional flat space with the coordinates $(x_1, x_2, x_3, x_4)$, $x_4$ the time and the metric $\mathrm{diag}(1, 1, 1, -1)$, a gas at rest with energy density $\rho$ and pressure $p$ has $T^\nu{}_\mu = \mathrm{diag}(p, p, p, -\rho)$. The minus sign in front of $\rho$ comes from $g_{x_4x_4} = -1$: lowering the index gives $T_{x_4x_4} = g_{x_4x_4}T^{x_4}{}_{x_4} = \rho$, the energy density, as in every book on relativity.

**The conventions of the book** (Revision record, `Revision/SPEC.md` section 4; record formula `equation_of_state_definitions`): the energy density and the pressures are

$$
\rho = -T^{x_4}{}_{x_4}, \qquad p_\mu = T^\mu{}_\mu \;\; (\text{no sum}, \; \mu \neq x_4), \qquad p_3 = T^{x_1}{}_{x_1}, \quad p_t = T^{x_5}{}_{x_5}, \quad p_8 = T^{x_8}{}_{x_8},
$$

and the **equations of state** are the ratios

$$
w_3 = \frac{p_3}{\rho}, \qquad w_t = \frac{p_t}{\rho}, \qquad w_8 = \frac{p_8}{\rho} .
$$

For a configuration that looks the same in the three directions of 3-space, $T^{x_1}{}_{x_1} = T^{x_2}{}_{x_2} = T^{x_3}{}_{x_3} = p_3$, and likewise $p_t$ for the extra times. Along an extra time, which is time-like, the entry $T^{x_t}{}_{x_t}$ is called a pressure by definition; it has no everyday meaning.

**The definition.** The **action** is the integral of the Lagrangian density over the eight coordinates, $S_{\rm act} = \int\mathcal{L}\,d^8x$. The energy-momentum tensor is defined by how the action responds when the metric is changed a little, everywhere inside a bounded region:

$$
\delta S_{\rm act} = \tfrac12\int\sqrt{|g|}\;T^{\mu\nu}\,\delta g_{\mu\nu}\;d^8x
$$

for every small change $\delta g_{\mu\nu}$ (record normalisation; `Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md` section 8). Here $\delta$ means "the first-order change": if a quantity changes from $Q$ to $Q + \varepsilon Q_1 + \varepsilon^2 Q_2 + \dots$ when a small number $\varepsilon$ is switched on, then $\delta Q = \varepsilon Q_1$, and the terms with $\varepsilon^2$ and higher powers are dropped. For a spinor field the metric is changed through the vielbein factors, with the 16 components of $\Phi$ held fixed (the record's definition is $T^\nu{}_\mu = e^b{}_\mu\,\frac{1}{\sqrt{|g|}}\,\delta S_{\rm act}/\delta e^b{}_\nu$; check `T_vielbein_variation_closed_form_C` of `Revision/theory/reports/wolfram-field-theory.json` computes it for all 64 entries).

### 9.5 The diagonal entries, derived from the definition

We now derive the diagonal entries from the definition, using only the product rule and the first terms of a power series.

**The change.** Choose one direction $x_b$ and a small function $\varepsilon(x)$ that vanishes outside a bounded region. Change the vielbein factor of that direction, $f_b \to f_b\,(1 + \varepsilon)$, keep the other seven factors and keep $\Phi$ fixed. The metric is still diagonal. Its entry $g_{bb}$ changes by

$$
\delta g_{bb} = \eta_{bb}\big(f_b^2(1 + \varepsilon)^2 - f_b^2\big) = \eta_{bb}f_b^2\,(2\varepsilon + \varepsilon^2) \;\to\; 2\,g_{bb}\,\varepsilon .
$$

The first step writes the new entry minus the old one; the second multiplies out $(1 + \varepsilon)^2 = 1 + 2\varepsilon + \varepsilon^2$; the arrow keeps the first order and uses $\eta_{bb}f_b^2 = g_{bb}$. Every other entry is unchanged.

**What the definition says.** Insert this change into the definition. Only the term $\mu = \nu = b$ of the double sum survives:

$$
\delta S_{\rm act} = \tfrac12\int\sqrt{|g|}\;T^{bb}\cdot 2g_{bb}\,\varepsilon\;d^8x = \int\sqrt{|g|}\;T^b{}_b\;\varepsilon\;d^8x \qquad(\text{no sum over } b),
$$

because lowering the second index with the diagonal metric gives $T^{bb}g_{bb} = T^b{}_b$.

**What the Lagrangian says.** For every diagonal vielbein, not only the author's, the spin connection drops out of the Lagrangian (the Revision record proves this for an arbitrary diagonal vielbein; `Revision/theory/reports/python-field-theory.json`, check `commuting_emt_equals_vielbein_variation_diagonal`). So, with the same kinetic terms as in Section 9.3,

$$
\mathcal{L} = \big(f_1 f_2\cdots f_8\big)\Big[\sum_a\frac{1}{2f_a}X_a - mS - U(S)\Big], \qquad X_a = \bar\Phi\gamma^{(a)}\partial_a\Phi - \partial_a\bar\Phi\,\gamma^{(a)}\Phi .
$$

The numbers $X_a$, $S$ and $U(S)$ contain no vielbein factor ($\Phi$ is held fixed and the frame gammas $\gamma^{(a)}$ are constant matrices), so only two places change: the product $f_1\cdots f_8$ becomes $(1 + \varepsilon)f_1\cdots f_8$, and the coefficient $1/(2f_b)$ becomes $1/(2f_b(1 + \varepsilon))$. To first order $1/(1 + \varepsilon) = 1 - \varepsilon$ (the series $1/(1 + \varepsilon) = 1 - \varepsilon + \varepsilon^2 - \dots$, cut after the first order). Therefore, with $K_a = X_a/(2f_a)$,

$$
\begin{aligned}
\mathcal{L} \;\to\; & (1 + \varepsilon)\sqrt{|g|}\,\Big[\sum_{a \neq b}K_a + (1 - \varepsilon)K_b - mS - U\Big] \\
= \; & (1 + \varepsilon)\sqrt{|g|}\,\big[L_0 - \varepsilon K_b\big] \\
= \; & \sqrt{|g|}\,\big[L_0 + \varepsilon L_0 - \varepsilon K_b\big] + (\text{terms with } \varepsilon^2),
\end{aligned}
$$

where the second line uses $\sum_a K_a - mS - U = L_0$, and the third multiplies out. The first-order change is $\delta\mathcal{L} = \sqrt{|g|}\,(L_0 - K_b)\,\varepsilon$, hence

$$
\delta S_{\rm act} = \int\sqrt{|g|}\;\big(L_0 - K_b\big)\,\varepsilon\;d^8x .
$$

**Comparison.** The two expressions for $\delta S_{\rm act}$ agree for every small function $\varepsilon$. If $\int A\,\varepsilon\,d^8x = \int B\,\varepsilon\,d^8x$ for every such $\varepsilon$, then $A = B$ at every point (choose $\varepsilon$ concentrated near any point you like; this is the fundamental lemma of the calculus of variations). So

$$
T^b{}_b = L_0 - K_b \qquad (\text{no sum}, \; b = x_1, \dots, x_8).
$$

This is the record's formula (PROVED; `Revision/theory/reports/wolfram-field-theory.json`, check `T_diagonal_components_C`, and `Revision/theory/field-theory.json`, formula `EMT_diagonal`). It holds off shell: the derivation never used the field equation.

### 9.6 The whole tensor: its formula, its reality and its symmetry

**The formula.** The off-diagonal entries need a change of the vielbein that is not diagonal, and with it the change of the spin connection; this calculation is long, and the Revision record carries it out exactly for all 64 entries (checks `T_vielbein_variation_closed_form_C` and `T_symmetric_part_Belinfante_C` of `Revision/theory/reports/wolfram-field-theory.json`; the sympy record compares all 64 entries of a general first-order vielbein variation with the formula below, `commuting_emt_equals_general_vielbein_variation_on_shell`). Its result, the symmetric (Belinfante) energy-momentum tensor, is (record formula `T_symmetric`)

$$
T^\nu{}_\mu = \delta^\nu_\mu\,L_0 - \tfrac14\Big(\bar\Phi\gamma^\nu D_\mu\Phi - D_\mu\bar\Phi\,\gamma^\nu\Phi + \bar\Phi\gamma_\mu D^\nu\Phi - D^\nu\bar\Phi\,\gamma_\mu\Phi\Big),
$$

where $\delta^\nu_\mu$ is 1 for $\nu = \mu$ and 0 otherwise, $\gamma_\mu = g_{\mu\mu}\gamma^\mu$ and $D^\nu = g^{\nu\nu}D_\nu$ with $g^{\nu\nu} = 1/g_{\nu\nu}$. We take this formula from the record (status PROVED there) and check two of its consequences here.

**Its diagonal agrees with Section 9.5.** Set $\nu = \mu$. Then $\gamma_\mu D^\mu = g_{\mu\mu}\gamma^\mu g^{\mu\mu}D_\mu = \gamma^\mu D_\mu$, so the last two terms in the bracket equal the first two, and

$$
\begin{aligned}
T^\mu{}_\mu &= L_0 - \tfrac14\cdot 2\big(\bar\Phi\gamma^\mu D_\mu\Phi - D_\mu\bar\Phi\,\gamma^\mu\Phi\big) \\
&= L_0 - \tfrac12\big(\bar\Phi\gamma^\mu\partial_\mu\Phi - \partial_\mu\bar\Phi\,\gamma^\mu\Phi\big) - \tfrac12\,\bar\Phi\{\gamma^\mu, \Omega_\mu\}\Phi \\
&= L_0 - K_\mu .
\end{aligned}
$$

The first line uses $\delta^\mu_\mu = 1$ and the equality of the two pairs; the second inserts the covariant derivatives as in Section 9.3 ($\{A, B\} = AB + BA$ is the anticommutator); the third uses Fact 1 and the definition of $K_\mu$. This is the result of Section 9.5, as it must be.

**Symmetry.** Multiply by $g_{\nu\nu}$. Because $g_{\nu\nu}\gamma^\nu = \gamma_\nu$ and $g_{\nu\nu}D^\nu = D_\nu$,

$$
T_{\nu\mu} = g_{\nu\nu}T^\nu{}_\mu = g_{\nu\mu}L_0 - \tfrac14\Big(\bar\Phi\gamma_\nu D_\mu\Phi - D_\mu\bar\Phi\,\gamma_\nu\Phi + \bar\Phi\gamma_\mu D_\nu\Phi - D_\nu\bar\Phi\,\gamma_\mu\Phi\Big),
$$

and this expression is unchanged when $\nu$ and $\mu$ are exchanged (the first pair of terms becomes the second pair and the reverse; $g_{\nu\mu}$ is symmetric). So the lowered tensor is symmetric, $T_{\nu\mu} = T_{\mu\nu}$, while the mixed table $T^\nu{}_\mu$ is in general not symmetric as printed (PROVED; `Revision/theory/reports/python-field-theory.json`, check `commuting_emt_symmetric`).

**Reality.** Every entry is a real number. The proof needs three facts. (a) $D_\nu\bar\Phi = (D_\nu\Phi)^\dagger C$: indeed $(D_\nu\Phi)^\dagger C = \partial_\nu\Phi^\dagger C + \Phi^\dagger\Omega_\nu^T C$ ($\Omega_\nu$ is real, so its dagger is its transpose), and $\Omega_\nu^T C = -C\Omega_\nu$, because $\Omega_\nu$ is a sum of products $\gamma^{(a)}\gamma^{(b)}$ with $a \neq b$ and real coefficients, and $(\gamma^{(a)}\gamma^{(b)})^T C = \gamma^{(b)T}\gamma^{(a)T}C = -\gamma^{(b)T}C\gamma^{(a)} = C\gamma^{(b)}\gamma^{(a)} = -C\gamma^{(a)}\gamma^{(b)}$ (each step uses $\gamma^{(a)T}C = -C\gamma^{(a)}$, the transpose of the antisymmetry of $C\gamma^{(a)}$, and the last step the anticommutation of different gammas); so $(D_\nu\Phi)^\dagger C = \partial_\nu\bar\Phi - \bar\Phi\Omega_\nu = D_\nu\bar\Phi$. (b) Call $Y = \bar\Phi\gamma_\mu D_\nu\Phi = \Phi^\dagger(C\gamma_\mu)D_\nu\Phi$, a single number. Its complex conjugate is $Y^* = \Phi^T(C\gamma_\mu)(D_\nu\Phi)^*$ (the matrix $C\gamma_\mu$ is real); a single number equals its own transpose, so $Y^* = (D_\nu\Phi)^\dagger(C\gamma_\mu)^T\Phi = -(D_\nu\Phi)^\dagger C\gamma_\mu\Phi = -D_\nu\bar\Phi\,\gamma_\mu\Phi$, by the antisymmetry of $C\gamma_\mu$ and by (a). (c) Hence each pair in the bracket has the form $Y + Y^*$, which is twice the real part of $Y$, a real number. The same argument with $\partial$ in place of $D$ shows that each $K_\mu$ is real, and $S^* = \Phi^T C\Phi^* = \Phi^\dagger C^T\Phi = S$ shows that $S$ is real. So $L_0$ and all 64 entries are real (PROVED; `Revision/theory/reports/wolfram-field-theory.json`, check `L_real_C`; Notebook 09a confirms it numerically).

### 9.7 Energy density, pressures, kinetic and potential parts, equations of state

**The energy density.** With $\mu = x_4$ in $T^\mu{}_\mu = L_0 - K_\mu$:

$$
\begin{aligned}
\rho &= -T^{x_4}{}_{x_4} = -\big(L_0 - K_4\big) \\
&= -\Big(\sum_\mu K_\mu - mS - U - K_4\Big) \\
&= -\sum_{\mu \neq x_4}K_\mu + mS + U(S).
\end{aligned}
$$

The first line is the definition and Section 9.5; the second inserts $L_0 = \sum_\mu K_\mu - mS - U$; the third removes $K_4$ from the sum, where it cancels, and distributes the minus sign.

**The pressures.** For every direction $\mu \neq x_4$, in the same way,

$$
p_\mu = T^\mu{}_\mu = L_0 - K_\mu = \sum_{\nu \neq \mu}K_\nu - mS - U(S).
$$

**Kinetic and potential parts.** The terms with derivatives (the $K$'s) form the **kinetic part**; the terms without derivatives, $mS + U(S)$, form the **potential part**. The record's split (formula `EMT_kinetic_potential`) gives:

| quantity | kinetic part | potential part | total |
| --- | --- | --- | --- |
| energy density $\rho = -T^{x_4}{}_{x_4}$ | $-\sum_{\mu \neq x_4}K_\mu$ | $mS + U$ | $-\sum_{\mu \neq x_4}K_\mu + mS + U$ |
| 3-space pressure $p_3 = T^{x_1}{}_{x_1}$ | $\sum_{\mu \neq x_1}K_\mu$ | $-(mS + U)$ | $\sum_{\mu \neq x_1}K_\mu - mS - U$ |
| extra-time pressure $p_t = T^{x_5}{}_{x_5}$ | $\sum_{\mu \neq x_5}K_\mu$ | $-(mS + U)$ | $\sum_{\mu \neq x_5}K_\mu - mS - U$ |
| hidden pressure $p_8 = T^{x_8}{}_{x_8}$ | $\sum_{\mu \neq x_8}K_\mu$ | $-(mS + U)$ | $\sum_{\mu \neq x_8}K_\mu - mS - U$ |

Four remarks.

- The time derivative $\partial_4\Phi$ does not occur in $\rho$: the kinetic term $K_4$ cancels. As for Dirac's electron field, the field equation is of first order in time, and its energy is fixed by the derivatives along the other seven directions and by the potential.
- Each kinetic term carries the weight $1/f_\mu$: $e^{-a_4}\sin^{-1/6}z$ along 3-space (it shrinks as 3-space inflates), $1$ along the time, $e^{a_4}\sin^{-1/6}z$ along the extra times (it grows as they deflate) and $\tan z$ along the hidden direction. Figure 09a.1 of Notebook 09a draws these weights.
- The potential part is the same, $-(mS + U)$, in all seven pressures, and $+(mS + U)$ in the energy density.
- Neither the $K_\mu$ nor $S$ has a fixed sign, so $\rho$ can be negative (Section 9.21).

All of this is PROVED in the record (`Revision/theory/reports/wolfram-field-theory.json`, check `T_diagonal_components_C`; `Revision/theory/field-theory.json`, formulas `EMT_diagonal` and `EMT_kinetic_potential`) and holds off shell.

### 9.8 The trace, and what the field equation adds

**The trace off shell.** The **trace** is the sum of the diagonal entries. Summing $T^\mu{}_\mu = L_0 - K_\mu$ over the eight directions:

$$
\begin{aligned}
\sum_\mu T^\mu{}_\mu &= 8L_0 - \sum_\mu K_\mu \\
&= 8\Big(\sum_\mu K_\mu - mS - U\Big) - \sum_\mu K_\mu \\
&= 7\sum_\mu K_\mu - 8\big(mS + U\big).
\end{aligned}
$$

The first line adds eight copies of $L_0$ and subtracts every $K_\mu$ once; the second inserts $L_0$; the third collects the kinetic terms (PROVED; check `EMT_trace_C` of `Revision/theory/reports/wolfram-field-theory.json`).

**The kinetic sum.** Define the **field-equation expression** $E = \gamma^\mu D_\mu\Phi - V\Phi$ and its adjoint $\bar E = (D_\mu\bar\Phi)\gamma^\mu + V\bar\Phi$ (sums over $\mu$); a configuration is on shell exactly when $E = 0$, and then $\bar E = 0$ too. Multiply $E$ by $\bar\Phi$ from the left and $\bar E$ by $\Phi$ from the right:

$$
\bar\Phi E = \sum_\mu\bar\Phi\gamma^\mu D_\mu\Phi - VS, \qquad \bar E\Phi = \sum_\mu D_\mu\bar\Phi\,\gamma^\mu\Phi + VS .
$$

Subtract the second from the first and use Section 9.3 (the sum of the differences $\bar\Phi\gamma^\mu D_\mu\Phi - D_\mu\bar\Phi\gamma^\mu\Phi$ is $2\sum_\mu K_\mu$):

$$
\bar\Phi E - \bar E\Phi = 2\sum_\mu K_\mu - 2VS, \qquad\text{so}\qquad \sum_\mu K_\mu = VS + \tfrac12\big(\bar\Phi E - \bar E\Phi\big).
$$

This **kinetic-sum identity** holds off shell (PROVED; check `kinetic_sum_on_shell_C`).

**On shell.** With $E = 0$ and $\bar E = 0$, line by line:

$$
\begin{aligned}
\sum_\mu K_\mu &= VS = \big(m + U'(S)\big)S, \\
L_0 &= \sum_\mu K_\mu - mS - U = mS + SU' - mS - U = SU'(S) - U(S), \\
\sum_\mu T^\mu{}_\mu &= 7\big(m + U'\big)S - 8\big(mS + U\big) = -mS + 7SU'(S) - 8U(S).
\end{aligned}
$$

The first line is the kinetic sum with $E = \bar E = 0$; the second inserts it into $L_0$ and cancels $mS$; the third inserts it into the trace. For $U = \frac{\lambda}{2}S^2$, $SU' = \lambda S^2$ and $8U = 4\lambda S^2$, so the trace on shell is $-mS + 7\lambda S^2 - 4\lambda S^2 = -mS + 3\lambda S^2$ (PROVED; `Revision/theory/reports/python-field-theory.json`, check `commuting_trace_on_shell`).

### 9.9 The covariant divergence of a diagonal tensor

**Why a divergence.** In flat space, energy that is not created or destroyed obeys a **conservation law**: the change in time of the energy density equals minus the outflow through the walls. In curved space the derivatives must be corrected by the **Christoffel symbols** $\Gamma^\lambda{}_{\mu\nu}$, which say how the coordinate directions turn and stretch from point to point (Chapter 3). The corrected derivative summed over the upper index is the **covariant divergence**

$$
\nabla_\mu T^\mu{}_\nu = \sum_\mu\partial_\mu T^\mu{}_\nu + \sum_{\mu,\lambda}\Gamma^\mu{}_{\mu\lambda}\,T^\lambda{}_\nu - \sum_{\mu,\lambda}\Gamma^\lambda{}_{\mu\nu}\,T^\mu{}_\lambda ,
$$

one number for each of the eight values of $\nu$. **Conservation** means $\nabla_\mu T^\mu{}_\nu = 0$ for all eight. On every solution of the field equation the tensor is conserved: this is a theorem, proved in the record from the invariance of the action under a change of coordinates (the Noether identity; PROVED, `Revision/theory/reports/wolfram-field-theory.json`, checks `Noether_identity_diffeomorphisms_C` and `conservation_on_shell_general`; `Revision/theory/reports/python-field-theory.json`, check `commuting_emt_conservation_on_shell`, with a negative control `commuting_emt_conservation_negative_control`). We do not repeat that proof. We ask instead: what does conservation say about a tensor of the simplest kind?

**The Christoffel symbols of the author's metric.** For a metric the symbols are $\Gamma^\lambda{}_{\mu\nu} = \frac12\sum_\rho g^{\lambda\rho}(\partial_\mu g_{\rho\nu} + \partial_\nu g_{\rho\mu} - \partial_\rho g_{\mu\nu})$. For a diagonal metric only $\rho = \lambda$ survives and

$$
\Gamma^\lambda{}_{\mu\nu} = \frac{1}{2g_{\lambda\lambda}}\big(\partial_\mu g_{\lambda\nu} + \partial_\nu g_{\lambda\mu} - \partial_\lambda g_{\mu\nu}\big) \qquad (\text{no sum over } \lambda).
$$

The symbol is symmetric in $\mu$ and $\nu$. Four of them, computed line by line (the entries depend only on $x_4$, through $a_4$, and on $x_8$, through $z = 6Hx_8$, whose derivative is $dz/dx_8 = 6H$):

- $\Gamma^{x_1}{}_{x_1x_4} = \frac{1}{2g_{11}}\partial_4 g_{11} = \frac12\,\partial_4\ln g_{11} = \frac12\,\partial_4\big(2a_4 + \tfrac13\ln\sin z\big) = a_4'$; the first step keeps the only nonzero derivative, the second uses $\partial(\ln Q) = \partial Q/Q$, the third writes $\ln g_{11} = 2a_4 + \frac13\ln\sin z$, and the last differentiates ($\sin z$ does not depend on $x_4$).
- $\Gamma^{x_4}{}_{x_1x_1} = \frac{1}{2g_{44}}\big(-\partial_4 g_{11}\big) = \frac{1}{-2}\big(-2a_4'e^{2a_4}\sin^{1/3}z\big) = a_4'\,e^{2a_4}\sin^{1/3}z$; only the third term of the bracket survives ($g_{41} = 0$), $g_{44} = -1$, and the chain rule gives $\partial_4 e^{2a_4} = 2a_4'e^{2a_4}$.
- $\Gamma^{x_8}{}_{x_1x_1} = \frac{1}{2g_{88}}\big(-\partial_8 g_{11}\big) = -\frac{\tan^2 z}{2}\,e^{2a_4}\cdot\tfrac13\sin^{-2/3}z\cos z\cdot 6H = -H e^{2a_4}\,\frac{\sin^{4/3}z}{\cos z}$; here $1/g_{88} = \tan^2 z$, the chain rule gives $\partial_8\sin^{1/3}z = \frac13\sin^{-2/3}z\cos z\cdot 6H$, and $\tan^2 z\,\sin^{-2/3}z\cos z = \sin^{4/3}z/\cos z$.
- $\Gamma^{x_8}{}_{x_8x_8} = \frac12\,\partial_8\ln\cot^2 z = \partial_8\ln\cot z = 6H\cdot\frac{-1/\sin^2 z}{\cot z} = -\frac{6H}{\sin z\cos z} = -\frac{12H}{\sin(12Hx_8)}$, using $\frac{d}{dz}\cot z = -1/\sin^2 z$ and $2\sin z\cos z = \sin 2z$.

The same three-line computations give all the others. The complete list of the nonzero symbols with $\mu \le \nu$ is (25 symbols: four for each of the six directions $x_i$ and $x_t$, and one more):

| symbol | value | symbol | value |
| --- | --- | --- | --- |
| $\Gamma^{x_i}{}_{x_ix_4}$ | $a_4'$ | $\Gamma^{x_t}{}_{x_4x_t}$ | $-a_4'$ |
| $\Gamma^{x_i}{}_{x_ix_8}$ | $H\cot z$ | $\Gamma^{x_t}{}_{x_tx_8}$ | $H\cot z$ |
| $\Gamma^{x_4}{}_{x_ix_i}$ | $a_4'e^{2a_4}\sin^{1/3}z$ | $\Gamma^{x_4}{}_{x_tx_t}$ | $a_4'e^{-2a_4}\sin^{1/3}z$ |
| $\Gamma^{x_8}{}_{x_ix_i}$ | $-He^{2a_4}\sin^{4/3}z/\cos z$ | $\Gamma^{x_8}{}_{x_tx_t}$ | $He^{-2a_4}\sin^{4/3}z/\cos z$ |
| $\Gamma^{x_8}{}_{x_8x_8}$ | $-6H/(\sin z\cos z)$ | (none) | (none) |

(PROVED; `Revision/theory/field-theory.json`, formula `christoffel_nonzero`, and `Revision/theory/reports/wolfram-field-theory.json`, check `christoffel_count`. Notebook 09a computes the 25 symbols with sympy and compares them with the record one by one.)

**A lemma for diagonal metrics.** Set $\lambda = \mu$ in the formula above (no sum):

$$
\Gamma^\mu{}_{\mu\nu} = \frac{1}{2g_{\mu\mu}}\big(\partial_\mu g_{\mu\nu} + \partial_\nu g_{\mu\mu} - \partial_\mu g_{\mu\nu}\big) = \frac{\partial_\nu g_{\mu\mu}}{2g_{\mu\mu}} = \frac{2\eta_{\mu\mu}f_\mu\,\partial_\nu f_\mu}{2\eta_{\mu\mu}f_\mu^2} = \partial_\nu\ln f_\mu .
$$

The first and the third term of the bracket cancel; then $g_{\mu\mu} = \eta_{\mu\mu}f_\mu^2$ and the chain rule $\partial_\nu f_\mu^2 = 2f_\mu\partial_\nu f_\mu$; finally $\partial_\nu f_\mu/f_\mu = \partial_\nu\ln f_\mu$. Summed over $\mu$ this gives $\sum_\mu\Gamma^\mu{}_{\mu\nu} = \partial_\nu\ln(f_1\cdots f_8) = \partial_\nu\ln\sqrt{|g|}$.

**The divergence of a diagonal tensor.** Now let $T^\mu{}_\nu$ be diagonal: $T^\mu{}_\nu = 0$ for $\mu \neq \nu$. In each of the three sums of the divergence only the terms with a diagonal entry survive:

- first sum: only $\mu = \nu$, giving $\partial_\nu T^\nu{}_\nu$;
- second sum: only $\lambda = \nu$, giving $\sum_\mu\Gamma^\mu{}_{\mu\nu}T^\nu{}_\nu = \sum_\mu(\partial_\nu\ln f_\mu)\,T^\nu{}_\nu$;
- third sum: only $\lambda = \mu$, giving $\sum_\mu\Gamma^\mu{}_{\mu\nu}T^\mu{}_\mu = \sum_\mu(\partial_\nu\ln f_\mu)\,T^\mu{}_\mu$.

Both corrections use only the lemma. Subtracting the third from the second:

$$
\nabla_\mu T^\mu{}_\nu = \partial_\nu T^\nu{}_\nu + \sum_\mu\big(\partial_\nu\ln f_\mu\big)\big(T^\nu{}_\nu - T^\mu{}_\mu\big) \qquad (\text{diagonal } T, \text{ no sum over } \nu).
$$

This formula holds for every diagonal metric and every diagonal tensor. We apply it to the author's metric and to

$$
T^\mu{}_\nu = \mathrm{diag}\big(p_3, p_3, p_3, -\rho, p_t, p_t, p_t, p_8\big),
$$

whose four entries are any functions of $x_4$ and $x_8$. The logarithmic derivatives we need are, from $\ln f_i = a_4 + \frac16\ln\sin z$, $\ln f_t = -a_4 + \frac16\ln\sin z$, $\ln f_4 = 0$ and $\ln f_8 = \ln\cot z$:

$$
\partial_4\ln f_i = a_4', \quad \partial_4\ln f_t = -a_4', \quad \partial_4\ln f_4 = \partial_4\ln f_8 = 0, \qquad \partial_8\ln f_i = \partial_8\ln f_t = \tfrac16\cdot\frac{\cos z}{\sin z}\cdot 6H = H\cot z, \quad \partial_8\ln f_4 = 0 .
$$

**The component $\nu = x_4$.** Here $T^{x_4}{}_{x_4} = -\rho$:

$$
\begin{aligned}
\nabla_\mu T^\mu{}_{x_4} &= \partial_4(-\rho) + 3a_4'\big(-\rho - p_3\big) + 3\big(-a_4'\big)\big(-\rho - p_t\big) \\
&= -\partial_4\rho - 3a_4'\rho - 3a_4'p_3 + 3a_4'\rho + 3a_4'p_t \\
&= -\partial_4\rho - 3a_4'\big(p_3 - p_t\big).
\end{aligned}
$$

The first line takes the three 3-space directions (weight $a_4'$, entry $p_3$) and the three extra times (weight $-a_4'$, entry $p_t$); the directions $x_4$ and $x_8$ have weight 0. The second multiplies out; the third cancels $\mp 3a_4'\rho$ and factors.

**The component $\nu = x_8$.** Here $T^{x_8}{}_{x_8} = p_8$. The direction $\mu = x_8$ gives $(p_8 - p_8) = 0$ whatever its weight, and $\mu = x_4$ has weight 0:

$$
\nabla_\mu T^\mu{}_{x_8} = \partial_8 p_8 + 3H\cot z\,\big(p_8 - p_3\big) + 3H\cot z\,\big(p_8 - p_t\big) = \partial_8 p_8 + 3H\cot z\,\big(2p_8 - p_3 - p_t\big).
$$

**The other six components.** For $\nu = x_1$ (and likewise $x_2, x_3, x_5, x_6, x_7$) every term contains a derivative $\partial_1$ of something that depends only on $x_4$ and $x_8$; all vanish: $\nabla_\mu T^\mu{}_{x_1} = 0$ identically.

These are exactly the record's statements (PROVED; `Revision/theory/field-theory.json`, formula `energy_exchange`; `Revision/theory/reports/wolfram-field-theory.json` and `python-field-theory.json`, check `energy_exchange_equation`; independently `Revision/lead_checks/reports/emt-divergence-and-spin-connection.json`, checks `divergence_x4_component`, `divergence_x8_component` and `divergence_other_components_zero`). Notebook 09a derives them again with sympy, from the 25 Christoffel symbols and the general divergence formula, without using the lemma.

### 9.10 The x4 identity: energy exchange between 3-space and the extra times

Conservation of a diagonal tensor along $x_4$ is therefore

$$
\frac{\partial\rho}{\partial x_4} = -3a_4'\,\big(p_3 - p_t\big).
$$

**What it says.** On a deflating history ($a_4' > 0$) the energy density falls when the 3-space pressure exceeds the extra-time pressure, rises when it is smaller, and stays constant only when $p_3 = p_t$. Energy flows between 3-space and the extra times. Reversing the history ($a_4' \to -a_4'$: the extra times inflate and 3-space deflates) reverses the flow. Note what is absent: in ordinary cosmology the energy density of a gas always falls as space expands, $d\rho/dt = -3\,(\dot a/a)\,(\rho + p)$ with the scale factor $a$, because the volume grows. Here the volume factor $\sqrt{|g|} = \cos z$ does not change with $x_4$, so no term with $\rho$ itself appears; only the difference of the two pressures drives the energy.

**A first-law reading (an interpretation, not an extra result).** At fixed $x_8$ take a small box of coordinate size 1 along each of the seven directions other than $x_4$. Its 3-space volume is $V_3 = f_1f_2f_3 = e^{3a_4}\sin^{1/2}z$, its extra-time volume $V_t = f_5f_6f_7 = e^{-3a_4}\sin^{1/2}z$, and its 7-volume $V_7 = V_3V_tf_8 = \cos z$ does not change with $x_4$. The first law of thermodynamics says that the energy of a box changes by minus the pressure times the change of its volume. Applied separately to the two families of directions, with each change of volume taken relative to the volume of its family,

$$
\frac{d}{dx_4}\big(\rho V_7\big) = -p_3\,\frac{V_7}{V_3}\frac{dV_3}{dx_4} - p_t\,\frac{V_7}{V_t}\frac{dV_t}{dx_4} .
$$

Divide by the constant $V_7$ and insert $\frac{1}{V_3}\frac{dV_3}{dx_4} = 3a_4'$ and $\frac{1}{V_t}\frac{dV_t}{dx_4} = -3a_4'$ (the logarithmic derivatives of $e^{\pm3a_4}$): the result is $d\rho/dx_4 = -3a_4'p_3 + 3a_4'p_t$, the conservation identity. While 3-space inflates ($dV_3 > 0$), a positive $p_3$ takes energy out of the box; while the extra times deflate ($dV_t < 0$), a positive $p_t$ puts energy in. Notebook 09a checks with sympy that this reading is exactly the identity, and Figure 09a.4 draws the three volumes.

**Toy fluids (an ILLUSTRATION, not solutions of the field equations of this book).** Suppose a source had pressures proportional to its energy density, $p_3 = w_3\rho$ and $p_t = w_t\rho$ with constants $w_3$, $w_t$, on the history $a_4 = AHx_4$ ($a_4' = AH$). The identity becomes $d\rho/dx_4 = -3AH(w_3 - w_t)\,\rho$: the rate of change of $\rho$ is a constant times $\rho$. The function $\rho_0e^{cx_4}$ has the derivative $c\,\rho_0e^{cx_4}$, so the solution with $\rho(0) = \rho_0$ is

$$
\rho(x_4) = \rho_0\,e^{-3AH(w_3 - w_t)x_4} .
$$

With $A = 1$, $H = 0.25$ and $w_3 - w_t = 1/3$, at $x_4 = 8$ the exponent is $-3\cdot 0.25\cdot\frac13\cdot 8 = -2$ and $\rho(8)/\rho(0) = e^{-2} = 0.135335$, the number that Notebook 09b computes with the Runge-Kutta method. The condensates of Section 9.18 have $p_3 = p_t$ and exchange no energy at all.

### 9.11 The x8 identity: the balance along the hidden direction

Conservation along $x_8$ is

$$
\frac{\partial p_8}{\partial x_8} = -3H\cot z\,\big(2p_8 - p_3 - p_t\big).
$$

It is a balance of pressures, like the balance of pressure and weight in a column of air: a change of the hidden pressure along $x_8$ must be paid for by the difference between $p_8$ and the mean of the other two pressures.

**Entries that do not depend on $x_8$.** Then the left side is zero, and because $\cot z > 0$ for $0 < z < \pi/2$ the bracket must vanish:

$$
p_8 = \tfrac12\big(p_3 + p_t\big).
$$

The field equations of gravity force the same condition, $p_3 + p_t = 2p_8$, for every source of the author's metric (Chapter 12): the two sides are consistent.

**All solutions when $p_3 + p_t = P$ is a constant.** Write $q = p_8 - P/2$. Then $2p_8 - P = 2q$, and with $dz = 6H\,dx_8$ the identity becomes

$$
6H\frac{dq}{dz} = -3H\cot z\cdot 2q, \qquad\text{that is}\qquad \frac{dq}{dz} + \cot z\;q = 0 .
$$

Multiply by $\sin z$: $\sin z\,\frac{dq}{dz} + \cos z\;q = \frac{d}{dz}\big(q\sin z\big) = 0$ (the product rule read backwards). So $q\sin z$ is a constant $c$, and every solution is

$$
p_8 = \frac{P}{2} + \frac{c}{\sin z} .
$$

Only $c = 0$ gives a profile independent of $x_8$; every other profile grows in size like $1/\sin z$ towards the tip $z = 0$ (Figure 09a.5).

**In the Kohn-Sham coordinate.** The Kohn-Sham solver of Chapter 15 uses the hidden coordinate $y = \ln(\sin z)/(6H)$, for which $dy/dx_8 = \frac{1}{6H}\cdot\frac{\cos z}{\sin z}\cdot 6H = \cot z$. By the chain rule $\partial_8 p_8 = \cot z\,dp_8/dy$, so the $x_8$ component of the divergence is $\cot z\,\big[dp_8/dy + 6Hp_8 - 3H(p_3 + p_t)\big]$, the form that solver checks (PROVED; `Revision/lead_checks/reports/emt-divergence-and-spin-connection.json`, checks `ks_coordinate_jacobian` and `ks_coordinate_form`).

### 9.12 Where the spin connection does enter the tensor

The spin connection drops out of the Lagrangian and of the diagonal entries (Fact 1). It does enter entries off the diagonal. Take a **homogeneous** configuration: one that depends on the time $x_4$ only, so that $\partial_\mu\Phi = 0$ for every $\mu \neq x_4$. Consider the piece

$$
K^{x_4}{}_{x_1} = \tfrac12\big(\bar\Phi\gamma^{x_4}D_{x_1}\Phi - D_{x_1}\bar\Phi\,\gamma^{x_4}\Phi\big)
$$

of the entry $T^{x_4}{}_{x_1}$. Line by line:

$$
\begin{aligned}
K^{x_4}{}_{x_1} &= \tfrac12\big(\bar\Phi\gamma^{(4)}\Omega_{x_1}\Phi + \bar\Phi\,\Omega_{x_1}\gamma^{(4)}\Phi\big) = \tfrac12\,\bar\Phi\{\gamma^{(4)}, \Omega_{x_1}\}\Phi, \\
\{\gamma^{(4)}, \gamma^{(1)}\gamma^{(4)}\} &= \gamma^{(4)}\gamma^{(1)}\gamma^{(4)} + \gamma^{(1)}\gamma^{(4)}\gamma^{(4)} = -\gamma^{(1)}\gamma^{(4)}\gamma^{(4)} + \gamma^{(1)}\gamma^{(4)}\gamma^{(4)} = 0, \\
\{\gamma^{(4)}, \gamma^{(1)}\gamma^{(8)}\} &= \gamma^{(4)}\gamma^{(1)}\gamma^{(8)} + \gamma^{(1)}\gamma^{(8)}\gamma^{(4)} = 2\gamma^{(4)}\gamma^{(1)}\gamma^{(8)}, \\
K^{x_4}{}_{x_1} &= \tfrac12\cdot\tfrac12 f_1\big(a_4'\cdot 0 + H\cdot 2\,\bar\Phi\gamma^{(4)}\gamma^{(1)}\gamma^{(8)}\Phi\big) = \tfrac12\,e^{a_4}\sin^{1/6}z\;H\;\bar\Phi\gamma^{(4)}\gamma^{(1)}\gamma^{(8)}\Phi .
\end{aligned}
$$

The first line uses $\partial_1\Phi = 0$, so $D_{x_1}\Phi = \Omega_{x_1}\Phi$ and $D_{x_1}\bar\Phi = -\bar\Phi\Omega_{x_1}$, and $\gamma^{x_4} = \gamma^{(4)}$ ($f_4 = 1$). The second moves $\gamma^{(4)}$ past $\gamma^{(1)}$ (a minus sign). The third moves $\gamma^{(4)}$ in the second product to the front past $\gamma^{(8)}$ and then past $\gamma^{(1)}$ (two minus signs, so no sign change). The fourth inserts $\Omega_{x_1} = \frac12f_1(a_4'\gamma^{(1)}\gamma^{(4)} + H\gamma^{(1)}\gamma^{(8)})$ and the two anticommutators. The $a_4'$ part cancels, the $H$ part survives, and the three-gamma bilinear $\bar\Phi\gamma^{(4)}\gamma^{(1)}\gamma^{(8)}\Phi$ is not zero in general: the canonical spin connection contributes to the energy-momentum tensor even though it drops out of the Lagrangian (PROVED; `Revision/theory/reports/python-scope.json` and `wolfram-scope.json`, check `spin_connection_in_the_energy_momentum_tensor`). Section 9.26 and Notebook 09c compute all such entries of a condensate.

### 9.13 The same tensor for dirac16complex

Everything in Sections 9.3 to 9.12 is algebra with the bilinears $\bar\Phi M\Phi$ and $\bar\Phi M\partial\Phi$, in which the row $\bar\Phi$ always stands to the left of the column. For the anticommuting field dirac16complex (Chapter 7) the same formulas hold, with every bilinear an even element of the Grassmann algebra; the Revision record verifies them in its checks ending in `_G` (for example `T_diagonal_components_G`, `EMT_trace_G`, `kinetic_sum_on_shell_G` and `grassmann_homogeneous_on_shell_rho_p`; PROVED). After canonical quantisation (Chapter 10) the tensor becomes an operator: every bilinear is replaced by the normal-ordered product of the quantised field, $\hat T^\nu{}_\mu = {:}T^\nu{}_\mu[\hat\Psi, \hat{\bar\Psi}]{:}$, and numbers are expectation values in a state (record `Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.md`, section 12). Two limits of the record must be stated: for $\lambda \neq 0$ the operator form of the on-shell identity $\sum_\mu\langle{:}K_\mu{:}\rangle = \langle{:}(m + U')S{:}\rangle$ is not verified by any Revision check (OPEN), and numerical expectation values of the tensor for many-fermion states are computed only in the Kohn-Sham approximation of Part IV. This chapter therefore computes numbers only for the commuting field dirac16complex00.

### 9.14 Example: the tensor at one point and the two identities

The first worked example puts Sections 9.3 to 9.12 on the computer. At one point of the deflating history ($H = 0.25$, $a_4 = AHx_4$ with $A = 1$, so $a_4 = 0.5$ and $a_4' = 0.25$ at $x_4 = 2$, and $z = \pi/4$) it builds the coordinate gammas and the spin connection from the Revision fixture and formula, draws a configuration of dirac16complex00 at random, computes its 64 entries $T^\nu{}_\mu$ literally from the formula of Section 9.6, and checks every identity of Sections 9.5 to 9.8, first off shell and then after putting the configuration on shell with the evolution form. It checks the connection term of Section 9.12. Then it switches to exact symbols: it computes the 25 Christoffel symbols with sympy, compares them with the record, derives the eight components of the divergence of a diagonal tensor and compares them with the record's formula `energy_exchange` and with the lead's checks, checks the first-law reading and the profiles of the $x_8$ balance, and draws five figures.

<!-- NOTEBOOK 09a -->

### 9.17 Line-by-line walk-through of Notebook 09a

The notebook has 21 code cells, In [1] to In [21]. This section explains every line of every one of them, in order. Code that is printed again here is quoted exactly, except that a long figure caption is shortened to "..." (it is printed in full in Section 9.16, under its figure).

**In [1], the set-up cell.** Every line that starts with `#` is a **comment**, which Python skips. The first part of the cell, down to the lines of `-` and `=` signs, is the complete run instructions of Section 9.15 again, as comments, so that the notebook file carries its own instructions. The code starts after the heading THE SET-UP; it computes no physics and is the same in every notebook of the book, except for the name of the notebook.

```python
import json  # reads and writes JSON files (text files that hold names and numbers)
import os  # reads the environment variable TEXTBOOK_OUTPUT_ROOT (explained below)
import textwrap  # breaks long printed text into lines of at most 89 characters
from pathlib import Path  # file and folder paths that work on Windows, macOS and Linux

import matplotlib  # the plotting package
import matplotlib.pyplot as plt  # its drawing functions, called plt by convention
from IPython.display import Image, display  # shows a saved picture below a cell

NOTEBOOK_ID = "09a"  # this notebook: chapter 09, example a
```

`import` loads a **module** (a part of Python or of an installed package) so that the cell can use it; `from pathlib import Path` takes only the name `Path`, the address of a file or folder, written the same way on every operating system. `plt` is the usual short name of matplotlib's drawing functions, and `Image` and `display` show a saved picture below a cell. The last line gives the **variable** `NOTEBOOK_ID` the **string** (a text in quotes) `"09a"`; the figure files are named after it.

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

`def` defines a **function**, a named piece of code that runs when it is called (the notebook's version also has a **docstring**, the text in triple quotes under the `def` line, which only documents it; it is left out here). Jupyter runs a notebook in the folder that holds it, `Path.cwd()`, and `.resolve()` writes it as a complete address. The `for` loop walks up from that folder through its parents; the operator `/` joins folder and file names, and `.is_file()` asks whether the file exists. The first folder that contains `Revision/textbook/requirements.txt` is the repository, and `return` hands it back. If none qualifies, `raise` stops the notebook with an error message that says what to do.

```python
REPO = find_repository_root()
OUTPUT_ROOT = Path(os.environ.get("TEXTBOOK_OUTPUT_ROOT", str(REPO)))


def repository_file(relative):
    return REPO / relative


def output_file(relative):
    path = OUTPUT_ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def say(text):
    print(textwrap.fill(str(text), width=89, subsequent_indent="    "))
```

`REPO` is the repository folder; it is never printed, because it differs from computer to computer. `OUTPUT_ROOT` is where files are written: the repository, unless the **environment variable** `TEXTBOOK_OUTPUT_ROOT` (a named text that the computer hands to a program) names another folder; the book's checking tool sets it, so that a check never changes the repository. `repository_file` gives the path of a repository file for reading; `output_file` gives the path at which to write a file and first creates its folder (`mkdir`, where `exist_ok=True` does nothing if the folder exists). `say` prints a text in lines of at most 89 characters (the width of a page of the book), indenting the continuation lines by four blanks. (The docstrings of these three functions are left out here.)

```python
matplotlib.rcdefaults()  # ignore personal matplotlib settings: same figures everywhere
plt.rcParams.update({"figure.figsize": (7.0, 4.2), "font.size": 10.0,
                     "axes.grid": True, "grid.alpha": 0.3})

FIGURE_FOLDER = "Revision/textbook/figures"  # where the figures are saved
CAPTION_FILE = f"{FIGURE_FOLDER}/{NOTEBOOK_ID}.captions.json"  # their captions
FIGURE_NUMBERS = {}  # figure name -> its number k (file name <id>_<k>_<name>.png)
CAPTIONS = {}  # figure file name -> caption, written to CAPTION_FILE after every figure
output_file(CAPTION_FILE).write_text("{}\n", encoding="utf-8", newline="\n")
```

The first two lines make every figure look the same on every computer: the built-in settings, a figure size of 7.0 by 4.2 inches, 10-point letters and a faint grid. The braces `{...}` make a **dictionary** (pairs `key: value`). A string that starts with `f` is an **f-string**: each name in braces is replaced by its value, so `CAPTION_FILE` is `"Revision/textbook/figures/09a.captions.json"`. The last line starts that file as an empty dictionary `{}`; `newline="\n"` writes the same line end on every operating system.

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

`save_figure` (shown without its docstring and its comment lines) numbers the figures 1, 2, 3, ... in the order of their first appearance (`setdefault` returns the number stored for a name, or stores and returns the next one), saves the picture as a PNG file at 150 dots per inch with the empty margin cut away and without a program name inside the file (so that two runs write the same bytes), closes it, stores the caption in the captions file (`json.dumps` turns the dictionary into text with the keys sorted), shows the saved picture below the cell and prints one line saying where it was saved.

```python
PASSED = []  # the names of the checks that passed, in order


def check(condition, name, record=None):
    if not condition:
        raise AssertionError(f"check failed: {name}")
    PASSED.append(name)
    say(f"PASS {name}")
    if record is not None:
        say(f"     reproduces {record}")


def report(label, value, unit=""):
    say(f"RESULT {label} = {value}" + (f" {unit}" if unit else ""))


def all_checks_passed():
    print(f"ALL {len(PASSED)} CHECKS PASSED (notebook {NOTEBOOK_ID})")


say(f"Set-up of notebook {NOTEBOOK_ID} complete: repository folder found, helpers "
    "defined.")
```

`PASSED` is an empty **list** (an ordered collection, in square brackets). `check` is the function behind every check: `condition` is either `True` or `False`; if it is false, the notebook stops with an `AssertionError` that names the check; if it is true, the name is appended to `PASSED` and the line `PASS name` is printed, followed, when the check reproduces a Revision record, by a line `reproduces <file>, check <name>`. (An `if` statement is used instead of Python's `assert`, which Python started with the option `-O` would skip.) `report` prints a key number as a line that starts with `RESULT`. `all_checks_passed` prints the last line of the notebook with the number of checks that passed. The cell prints one line: `Set-up of notebook 09a complete: repository folder found, helpers defined.`

**In [2], the gamma matrices and the matrix C.**

```python
import numpy as np  # arrays of numbers, matrices, linear algebra

fixture = json.loads(
    repository_file("Revision/algebra/gammas.json").read_text(encoding="utf-8"))
# gamma[a] is the frame matrix gamma^(x_(a+1)): gamma[0] = x1, ..., gamma[7] = x8.
gamma = [np.array(rows, dtype=float) for rows in fixture["gamma"]]
eta = np.array(fixture["eta"], dtype=float)  # (+1, +1, +1, -1, -1, -1, -1, +1)
C = np.array(fixture["C"], dtype=float)  # gamma^(x8) gamma^(x1) gamma^(x2) gamma^(x3)
I16 = np.eye(16)  # the 16 x 16 unit matrix
NAMES = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]  # the author's coordinates
```

numpy is the package for arrays of numbers. `read_text` reads the fixture file as text, and `json.loads` turns the text into Python objects: here a dictionary whose entry `"gamma"` is a list of eight matrices, each a list of 16 rows of 16 numbers. The line `gamma = [... for rows in fixture["gamma"]]` is a **list comprehension**: it builds a list by evaluating the expression before `for` for each item; `np.array(rows, dtype=float)` turns one matrix into a numpy array of real (floating-point) numbers. Python counts from 0, so `gamma[0]` is $\gamma^{(1)}$, `gamma[3]` is $\gamma^{(4)}$ and `gamma[7]` is $\gamma^{(8)}$. The eight matrices are real; their entries are the whole numbers 0, 1 and $-1$. `eta` holds the eight diagonal entries of $\eta$, `C` the matrix $C$, `I16` the $16 \times 16$ unit matrix, and `NAMES` the names of the coordinates for printing.

```python
def recorded(path, name):
    """The verdict (PASS or FAIL) of the check name in the Revision report path."""
    report_data = json.loads(repository_file(path).read_text(encoding="utf-8"))
    for item in report_data["checks"]:
        if item["name"] == name:
            return item["verdict"].upper()  # some reports write "pass"
    raise KeyError(f"{path} has no check {name}")
```

A Revision report is a JSON file with a list `"checks"`; each check has a `"name"` and a `"verdict"`. `recorded` opens the report, looks for the check of the given name and returns its verdict in capital letters (`.upper()`, because some reports write `pass`). If the name is missing it stops with a `KeyError`. Every check of the notebook that reproduces a record also asks the record for its own verdict, so a notebook check passes only when the record agrees.

```python
ALGEBRA = "Revision/algebra/reports/python-algebra.json"
# {gamma^a, gamma^b} = gamma^a gamma^b + gamma^b gamma^a must be 2 eta^ab times 1.
clifford = all(np.array_equal(gamma[a] @ gamma[b] + gamma[b] @ gamma[a],
                              2 * eta[a] * (a == b) * I16)
               for a in range(8) for b in range(8))
check(clifford and recorded(ALGEBRA, "clifford_relation") == "PASS",
      "the 64 Clifford relations {gamma^a, gamma^b} = 2 eta^ab",
      record=f"{ALGEBRA}, check clifford_relation")
```

The operator `@` is the matrix product. `(a == b)` is `True` (counted as 1) when $a = b$ and `False` (counted as 0) otherwise, so `2 * eta[a] * (a == b) * I16` is $2\eta^{ab}\cdot 1$ (for this diagonal $\eta$, $\eta^{aa} = \eta_{aa}$). `np.array_equal` asks whether two arrays are equal entry by entry, exactly: the gammas hold whole numbers, so no rounding occurs. `all(... for a in range(8) for b in range(8))` is true only when the comparison holds for all 64 pairs; `range(8)` is 0, 1, ..., 7. The check passes when all 64 Clifford relations hold and the record's check `clifford_relation` passed.

```python
# C is symmetric, C times C is 1, and every C gamma^a is antisymmetric.
c_ok = np.array_equal(C, C.T) and np.array_equal(C @ C, I16) and all(
    np.array_equal((C @ g).T, -(C @ g)) for g in gamma)
check(c_ok and recorded(ALGEBRA, "C_real_symmetric_involution") == "PASS"
      and recorded(ALGEBRA, "C_gamma_antisymmetric") == "PASS",
      "C is real symmetric, C^2 = 1, every C gamma^a is antisymmetric",
      record=f"{ALGEBRA}, checks C_real_symmetric_involution and "
             "C_gamma_antisymmetric")
```

`.T` is the transpose. The three conditions are $C^T = C$, $C^2 = 1$ and $(C\gamma^{(a)})^T = -C\gamma^{(a)}$ for each of the eight gammas (`for g in gamma` takes them in turn): the facts used in Sections 9.6 and 9.18. The cell prints the two PASS lines with their record lines.

**In [3], the author's metric at one point.**

```python
H = 0.25  # the author's constant H
A = 1.0  # the history a4 = A H x4; A > 0: the extra times deflate
m = 1.0  # the mass m of the field
lam = 0.5  # the strength lambda of the potential U(S) = (lambda/2) S^2
X4 = 2.0  # the time x4 of the point
a4 = A * H * X4  # a4 at the point: 0.5
a4p = A * H  # its derivative da4/dx4 (written a4p, "a4 prime"): 0.25
z = np.pi / 4  # z = 6 H x8 at the point
```

These lines choose the numbers of the example: $H = 0.25$, the deflating history $a_4 = AHx_4$ with $A = 1$, the mass $m = 1$, the strength $\lambda = 0.5$ (written `lam`, because `lambda` is a reserved word of Python), the time $x_4 = 2$, hence $a_4 = 0.5$ and $a_4' = AH = 0.25$, and $z = \pi/4$ (`np.pi` is $\pi$). They are choices, not results.

```python
def frame_factors(a4_value, z_value):
    """The eight factors f_a of the diagonal vielbein, in the order x1, ..., x8."""
    space = np.exp(a4_value) * np.sin(z_value) ** (1 / 6)  # e^a4 sin^(1/6) z
    extra = np.exp(-a4_value) * np.sin(z_value) ** (1 / 6)  # e^(-a4) sin^(1/6) z
    return np.array([space] * 3 + [1.0] + [extra] * 3 + [1 / np.tan(z_value)])


f = frame_factors(a4, z)
g_diag = eta * f ** 2  # the diagonal entries g_mumu = eta_mumu f_mu^2
```

`frame_factors` returns the eight factors $f_a$ of Section 9.2. `**` means "to the power", so `np.sin(z_value) ** (1 / 6)` is $\sin^{1/6}z$. `[space] * 3` is a list of three copies of `space`, and `+` joins lists, so the returned array is $(f_1, f_1, f_1, 1, f_5, f_5, f_5, \cot z)$ with $\cot z = 1/\tan z$. Then `f` holds the factors at the point, and `g_diag` the eight diagonal entries $g_{\mu\mu} = \eta_{\mu\mu}f_\mu^2$; arithmetic on arrays acts entry by entry.

```python
authors = np.array([np.exp(2 * a4) * np.sin(z) ** (1 / 3)] * 3 + [-1.0]
                   + [-np.exp(-2 * a4) * np.sin(z) ** (1 / 3)] * 3
                   + [1 / np.tan(z) ** 2])
THEORY_PY = "Revision/theory/reports/python-field-theory.json"
check(np.allclose(g_diag, authors, rtol=1e-14, atol=0)
      and recorded(THEORY_PY, "metric_from_vielbein_equals_SPEC") == "PASS",
      "eta_aa f_a^2 is the author's metric at the point",
      record=f"{THEORY_PY}, check metric_from_vielbein_equals_SPEC")
check(abs(np.prod(f) - np.cos(z)) < 1e-14
      and recorded(THEORY_PY, "sqrt_det_g_equals_cos_z") == "PASS",
      "the volume factor f1 f2 ... f8 equals cos z",
      record=f"{THEORY_PY}, check sqrt_det_g_equals_cos_z")
for name, value in zip(NAMES, f):
    report(f"f_{name}", f"{value:.6f}")
```

`authors` writes the author's eight metric entries directly. `np.allclose(x, y, rtol=1e-14, atol=0)` is true when every entry of `x` differs from the entry of `y` by less than $10^{-14}$ times its size (a relative tolerance; floating-point numbers carry about 16 significant digits). The second check compares the product of the eight factors (`np.prod`) with $\cos z$, the computation of Section 9.2. `zip(NAMES, f)` pairs each name with its factor, and `report` prints each with six decimals (the format `:.6f`): $f_{x_1} = e^{0.5}\sin^{1/6}(\pi/4) = 1.6487 \cdot 0.9439 = 1.556186$, $f_{x_4} = 1$, $f_{x_5} = e^{-0.5}\cdot 0.9439 = 0.572489$ and $f_{x_8} = \cot(\pi/4) = 1$.

**In [4], the weights of the kinetic terms (Figure 09a.1).**

```python
from matplotlib.ticker import NullFormatter  # a tick label that prints nothing

a4_axis = np.linspace(-2.0, 2.0, 401)  # values of a4 for the left panel
z_axis = np.linspace(0.02, 1.50, 400)  # values of z for the right panel
fig, (left, right) = plt.subplots(1, 2, figsize=(9.6, 3.9))
weights_a4 = np.array([1 / frame_factors(value, z) for value in a4_axis])
weights_z = np.array([1 / frame_factors(a4, value) for value in z_axis])
```

`np.linspace(a, b, n)` makes `n` equally spaced numbers from `a` to `b`. `plt.subplots(1, 2, ...)` makes a figure with one row of two panels, named `left` and `right`, 9.6 by 3.9 inches. `weights_a4` is a table with one row per value of $a_4$ and eight columns, the weights $1/f_\mu$ at $z = \pi/4$; `weights_z` is the same against $z$ at $a_4 = 0.5$.

```python
for panel, axis, weights in ((left, a4_axis, weights_a4), (right, z_axis, weights_z)):
    panel.plot(axis, weights[:, 0], label="3-space $x_1, x_2, x_3$")
    panel.plot(axis, weights[:, 3], "--", label="time $x_4$")
    panel.plot(axis, weights[:, 4], label="extra times $x_5, x_6, x_7$")
    panel.plot(axis, weights[:, 7], ":", label="hidden direction $x_8$")
    panel.set_yscale("log")  # equal factors are equal distances on this axis
    panel.yaxis.set_minor_formatter(NullFormatter())  # no labels on minor ticks
    panel.set_ylabel("weight $1/f_\\mu$")
```

The loop runs twice, once per panel. `weights[:, 0]` is column 0 of the table (all rows), the weight of $x_1$; columns 3, 4 and 7 are $x_4$, $x_5$ and $x_8$. The style string of two hyphens draws a dashed line and `":"` a dotted one; `label` is the name in the legend; text between dollar signs is typeset as mathematics, and a backslash inside a Python string is written twice. On a **logarithmic axis** equal ratios are equal distances, so a function $e^{\pm a_4}$ appears as a straight line. The minor ticks get no labels.

```python
ticks = [0.03, 0.1, 0.2, 0.5, 1, 2, 5, 10]  # plain numbers on the vertical axes
left.set_yticks(ticks[2:7], [str(t) for t in ticks[2:7]])
right.set_yticks(ticks, [str(t) for t in ticks])
left.set_xlabel("$a_4$ (at $z = \\pi/4$)")
right.set_xlabel("$z = 6 H x_8$ (at $a_4 = 0.5$)")
left.set_title("Weights against $a_4$")
right.set_title("Weights against $z$")
left.legend(fontsize=8)
save_figure(fig, "kinetic_weights",
            "The weights $1/f_\\mu$ with which a derivative along each direction "
            ...)
```

These lines put plain numbers on the vertical axes (`ticks[2:7]` is the part of the list from position 2 up to, not including, position 7), label the axes, set the titles, draw the legend in the left panel and save the figure as `09a_1_kinetic_weights.png` with its caption. **What Figure 09a.1 shows.** Both panels plot the weight $1/f_\mu$ (a pure number) on a logarithmic vertical axis. Left, against $a_4$: the 3-space weight $e^{-a_4}\sin^{-1/6}z$ falls and the extra-time weight $e^{a_4}\sin^{-1/6}z$ rises, two straight lines of opposite slope; the time weight 1 and the hidden weight $\tan(\pi/4) = 1$ lie on top of each other. The student should see that as the extra times deflate, derivatives along them count more and more in $\rho$ and in the pressures. Right, against $z$: the hidden weight $\tan z$ grows without bound near $z = \pi/2$.

**In [5], the spin connection at the point.**

```python
def spin_connection(a4_value, a4p_value, z_value):
    """The eight 16 x 16 matrices Omega_mu of the record's formula Omega_components."""
    s = np.sin(z_value) ** (1 / 6)  # sin^(1/6) z
    omega = [np.zeros((16, 16)) for _ in range(8)]  # Omega_x4 = Omega_x8 = 0
    for i in range(3):  # the three 3-space directions x1, x2, x3
        omega[i] = 0.5 * np.exp(a4_value) * s * (
            a4p_value * gamma[i] @ gamma[3] + H * gamma[i] @ gamma[7])
    for t in range(4, 7):  # the three extra times x5, x6, x7
        omega[t] = -0.5 * np.exp(-a4_value) * s * (
            a4p_value * gamma[3] @ gamma[t] + H * gamma[t] @ gamma[7])
    return omega
```

The function writes the formula of Section 9.2 literally. It starts with eight zero matrices (`np.zeros((16, 16))`; the name `_` is used for a loop counter that is not needed), which stay zero for $x_4$ and $x_8$, then fills the 3-space entries $\Omega_{x_i} = \frac12e^{a_4}\sin^{1/6}z\,(a_4'\gamma^{(i)}\gamma^{(4)} + H\gamma^{(i)}\gamma^{(8)})$ at the indices 0, 1, 2 and the extra-time entries $\Omega_{x_t} = -\frac12e^{-a_4}\sin^{1/6}z\,(a_4'\gamma^{(4)}\gamma^{(t)} + H\gamma^{(t)}\gamma^{(8)})$ at the indices 4, 5, 6 (`range(4, 7)` is 4, 5, 6).

```python
Omega = spin_connection(a4, a4p, z)
gamma_up = [gamma[mu] / f[mu] for mu in range(8)]  # coordinate gammas gamma^mu
gamma_down = [g_diag[mu] * gamma_up[mu] for mu in range(8)]  # gamma_mu
# {gamma^mu, Omega_mu} for each mu separately: the largest entry of all eight.
anti = max(np.abs(gamma_up[mu] @ Omega[mu] + Omega[mu] @ gamma_up[mu]).max()
           for mu in range(8))
A4_REPORT = "Revision/field_equations_a4/reports/wolfram-a4-report.json"
check(anti < 1e-14
      and recorded(A4_REPORT, "gamma_mu_anticommutes_with_Omega_mu_no_sum") == "PASS",
      "{gamma^mu, Omega_mu} = 0 for each direction mu (no sum)",
      record=f"{A4_REPORT}, check gamma_mu_anticommutes_with_Omega_mu_no_sum")
```

`Omega` holds the eight matrices at the point; `gamma_up` the coordinate gammas $\gamma^\mu = \gamma^{(\mu)}/f_\mu$ and `gamma_down` the lowered ones $\gamma_\mu = g_{\mu\mu}\gamma^\mu$. For each direction the cell computes the anticommutator $\gamma^\mu\Omega_\mu + \Omega_\mu\gamma^\mu$ and takes the largest absolute value of its 256 entries (`np.abs(...).max()`); `anti` is the largest of these eight numbers. Fact 1 of Section 9.3 says it is zero; the check allows rounding errors below $10^{-14}$.

```python
total = sum(gamma_up[mu] @ Omega[mu] for mu in range(8))  # gamma^mu Omega_mu, summed
LEAD = "Revision/lead_checks/reports/emt-divergence-and-spin-connection.json"
check(np.abs(total - 3 * H * gamma[7]).max() < 1e-14
      and recorded(THEORY_PY, "gamma_mu_Omega_mu_equals_3H_gamma_x8") == "PASS"
      and recorded(LEAD, "gamma_Omega_equals_3H_gamma8") == "PASS",
      "gamma^mu Omega_mu = 3 H gamma^(x8) at the point",
      record=f"{THEORY_PY}, check gamma_mu_Omega_mu_equals_3H_gamma_x8; {LEAD}, "
             "check gamma_Omega_equals_3H_gamma8")
```

`sum(...)` adds the eight products $\gamma^\mu\Omega_\mu$, and the check compares the result with $3H\gamma^{(8)} = 0.75\,\gamma^{(8)}$: Fact 2, which the theory record and the lead's independent check both state.

**In [6], the Dirac adjoint and the energy-momentum tensor.**

```python
def bar(vector):
    """The Dirac adjoint: the row vector vector^dagger C."""
    return vector.conj() @ C
```

`.conj()` takes the complex conjugate of every entry. For a one-dimensional numpy array, `@` with a matrix on its right treats the array as a row, so `vector.conj() @ C` is the row $\Phi^\dagger C = \bar\Phi$.

```python
def energy_momentum(phi, dphi, f_values, gup, gdown, omega):
    """S, U, L0, the kinetic terms K_mu and the tensor T (T[nu, mu] = T^nu_mu)."""
    g_values = eta * f_values ** 2  # g_mumu
    S = (bar(phi) @ phi).real  # S = Phibar Phi (a real number)
    U = lam / 2 * S ** 2  # U(S) = (lambda/2) S^2
    D = [dphi[mu] + omega[mu] @ phi for mu in range(8)]  # D_mu Phi
    Dbar = [bar(dphi[mu]) - bar(phi) @ omega[mu] for mu in range(8)]  # D_mu Phibar
    L0 = 0.5 * sum(bar(phi) @ gup[mu] @ D[mu] - Dbar[mu] @ gup[mu] @ phi
                   for mu in range(8)) - m * S - U
```

The arguments are the 16 values `phi` of $\Phi$ at the point, the $8 \times 16$ table `dphi` whose row `mu` holds $\partial_\mu\Phi$, the factors, the coordinate gammas with upper and lower index, and the spin connection. `S` is $\bar\Phi\Phi$; it is real (Section 9.6), and `.real` keeps the real part, dropping a rounding remainder. `D` and `Dbar` are the lists of the eight covariant derivatives $D_\mu\Phi = \partial_\mu\Phi + \Omega_\mu\Phi$ and $D_\mu\bar\Phi = \partial_\mu\bar\Phi - \bar\Phi\Omega_\mu$ (`bar(dphi[mu])` is $\partial_\mu\bar\Phi$, because $C$ is the same at every point). `L0` is the formula of Section 9.2, with the spin connection included: the cell computes it the long way, and a later check compares it with $\sum_\mu K_\mu - mS - U$.

```python
    T = np.zeros((8, 8), dtype=complex)
    for nu in range(8):
        for mu in range(8):
            bracket = (bar(phi) @ gup[nu] @ D[mu] - Dbar[mu] @ gup[nu] @ phi
                       # gamma_mu D^nu = gamma_mu D_nu / g_nunu
                       + (bar(phi) @ gdown[mu] @ D[nu]
                          - Dbar[nu] @ gdown[mu] @ phi) / g_values[nu])
            T[nu, mu] = (nu == mu) * L0 - bracket / 4
```

The two loops fill the $8 \times 8$ table `T`, row `nu` and column `mu`, with the formula of Section 9.6: `bracket` is $\bar\Phi\gamma^\nu D_\mu\Phi - D_\mu\bar\Phi\gamma^\nu\Phi + \bar\Phi\gamma_\mu D^\nu\Phi - D^\nu\bar\Phi\gamma_\mu\Phi$, where $D^\nu = D_\nu/g_{\nu\nu}$ is the division by `g_values[nu]`, and `(nu == mu) * L0` is $\delta^\nu_\mu L_0$. The table is complex at first (`dtype=complex`), because the field is complex; it must come out real.

```python
    # K_mu = (1/(2 f_mu)) (Phibar gamma^(mu) d_mu Phi - d_mu Phibar gamma^(mu) Phi)
    K = np.array([(bar(phi) @ gamma[mu] @ dphi[mu] - bar(dphi[mu]) @ gamma[mu] @ phi)
                  / (2 * f_values[mu]) for mu in range(8)])
    return S, U, L0, K, T
```

`K` holds the eight kinetic terms computed from their own formula, with ordinary derivatives and frame gammas and without any spin connection, so that the record's statements $T^\mu{}_\mu = L_0 - K_\mu$ and $L_0 = \sum_\mu K_\mu - mS - U$ can be tested independently. The function returns five results; the cell prints nothing.

**In [7], a random configuration and its tensor.**

```python
rng = np.random.default_rng(12345)  # a fixed seed: the same numbers in every run
Phi = rng.normal(size=16) + 1j * rng.normal(size=16)  # the 16 values of Phi
dPhi = rng.normal(size=(8, 16)) + 1j * rng.normal(size=(8, 16))  # d_mu Phi
S, U, L0, K, T = energy_momentum(Phi, dPhi, f, gamma_up, gamma_down, Omega)
```

`np.random.default_rng(12345)` makes a generator of random numbers; the fixed **seed** 12345 makes it produce the same numbers in every run, so the notebook's output never changes. `rng.normal(size=16)` draws 16 numbers from the bell-shaped normal distribution; `1j` is Python's imaginary unit $i$, so `Phi` is a random complex column, and `dPhi` a random $8 \times 16$ table of first derivatives. The **jet** at the point, the values of the field and of its eight first derivatives, is all the tensor needs; it need not satisfy the field equation. The last line computes everything and names the five results.

```python
largest_imaginary = max(np.abs(T.imag).max(), np.abs(K.imag).max(), abs(L0.imag))
check(largest_imaginary < 1e-12, "every entry of T, every K_mu and L0 are real")
T, K, L0 = T.real, K.real, L0.real  # keep the real parts
T_low = g_diag[:, None] * T  # T_numu = g_nunu T^nu_mu
check(np.abs(T_low - T_low.T).max() < 1e-12
      and recorded(THEORY_PY, "commuting_emt_symmetric") == "PASS",
      "T_numu is symmetric (64 entries, 28 pairs compared)",
      record=f"{THEORY_PY}, check commuting_emt_symmetric")
report("S = Phibar Phi", f"{S:.6f}")
report("L0", f"{L0:.6f}")
```

`.imag` is the imaginary part. The first check confirms the reality of Section 9.6: the largest imaginary part is rounding noise, below $10^{-12}$. Then only the real parts are kept. `g_diag[:, None] * T` multiplies row $\nu$ of the table by $g_{\nu\nu}$ (`[:, None]` turns the eight numbers into a column, which numpy repeats across the eight columns of `T`), giving $T_{\nu\mu}$; the second check compares it with its transpose, the symmetry of Section 9.6 (the 56 entries off the diagonal form 28 pairs). The cell prints $S = -6.527875$ (negative: $S$ has no fixed sign) and $L_0 = 13.616346$.

**In [8], the heat map of the tensor (Figure 09a.2).**

```python
fig, ax = plt.subplots(figsize=(6.6, 5.6))
largest = np.abs(T).max()  # the colour scale runs from -largest to +largest
picture = ax.imshow(T, cmap="RdBu_r", vmin=-largest, vmax=largest)
for nu in range(8):
    for mu in range(8):
        # white digits on dark squares, black digits on light ones
        colour = "white" if abs(T[nu, mu]) > 0.6 * largest else "black"
        ax.text(mu, nu, f"{T[nu, mu]:.1f}", ha="center", va="center", fontsize=7,
                color=colour)
```

`ax.imshow` draws the table as a **heat map**, a grid of coloured squares: row $\nu$ from top to bottom, column $\mu$ from left to right. The colour map `"RdBu_r"` runs from blue (negative) through white (zero) to red (positive), with a scale symmetric about zero. The loops write each value with one decimal in its square (`ha` and `va` centre the text), white on dark squares and black on light ones (`x if condition else y` chooses one of two values).

```python
ax.set_xticks(range(8), [f"${n[0]}_{n[1]}$" for n in NAMES])
ax.set_yticks(range(8), [f"${n[0]}_{n[1]}$" for n in NAMES])
ax.set_xlabel("lower index $\\mu$ (column)")
ax.set_ylabel("upper index $\\nu$ (row)")
ax.set_title("$T^\\nu{}_\\mu$ of one random configuration at one point")
ax.grid(False)  # no grid lines across the squares
fig.colorbar(picture, ax=ax, label="value of $T^\\nu{}_\\mu$ (energy per volume)")
save_figure(fig, "tensor_heat_map", ...)
```

The tick labels turn a name such as `"x1"` into $x_1$ (`n[0]` is its letter, `n[1]` its digit). The colour bar beside the map says which value each colour means. **What Figure 09a.2 shows.** The 64 entries of the tensor of one random configuration, in units of energy per unit volume. The diagonal holds $-\rho$ at $(x_4, x_4)$ and the seven pressures; every square off the diagonal is coloured, because a random configuration has flows of energy and momentum in every direction. The student should notice that the printed table is not symmetric: the upper index is raised with the metric, and only $g_{\nu\nu}T^\nu{}_\mu$ is symmetric.

**In [9], the diagonal entries.**

```python
THEORY_WL = "Revision/theory/reports/wolfram-field-theory.json"
check(np.abs(np.diag(T) - (L0 - K)).max() < 1e-12
      and abs(L0 - (K.sum() - m * S - U)) < 1e-12
      and recorded(THEORY_WL, "T_diagonal_components_C") == "PASS",
      "T^mu_mu = L0 - K_mu for all eight mu, and L0 = sum K - m S - U",
      record=f"{THEORY_WL}, check T_diagonal_components_C")
```

`np.diag(T)` is the list of the eight diagonal entries, and `L0 - K` the list of the numbers $L_0 - K_\mu$. The check confirms Section 9.5 for all eight directions, and that the $L_0$ computed with the spin connection equals $\sum_\mu K_\mu - mS - U$ computed without it (Section 9.3).

```python
potential = m * S + U  # the potential energy density m S + U(S)
# kinetic part of T^mu_mu: the sum of the K_nu with nu different from mu
kinetic_parts = np.array([K.sum() - K[mu] for mu in range(8)])
rho = -T[3, 3]  # the energy density
rho_kin = -(K.sum() - K[3])  # minus the sum of the K_mu with mu different from x4
check(abs(rho - (rho_kin + potential)) < 1e-12
      and np.abs(np.diag(T) - (kinetic_parts - potential)).max() < 1e-12,
      "rho = rho_kin + rho_pot and p_mu = (sum of the other K) - (m S + U)")
```

These lines build the split of Section 9.7: `potential` is $mS + U$; `kinetic_parts[mu]` is $\sum_{\nu \neq \mu}K_\nu$; `rho` is $-T^{x_4}{}_{x_4}$ (row and column 3 are $x_4$); `rho_kin` is $-\sum_{\mu \neq x_4}K_\mu$. The check confirms $\rho = \rho_{\rm kin} + \rho_{\rm pot}$ and, for every direction, that the diagonal entry is its kinetic part minus $mS + U$.

```python
report("rho = -T^x4_x4", f"{rho:.6f}")
report("rho_kin", f"{rho_kin:.6f}")
report("rho_pot = m S + U", f"{potential:.6f}")
for mu in (0, 1, 2, 4, 5, 6, 7):
    report(f"pressure T^{NAMES[mu]}_{NAMES[mu]}", f"{T[mu, mu]:.6f}")
```

The cell prints $\rho = -7.531406$, made of $\rho_{\rm kin} = -11.656818$ and $\rho_{\rm pot} = 4.125412$ (indeed $-11.656818 + 4.125412 = -7.531406$), and the seven pressures, from $T^{x_7}{}_{x_7} = -1.976597$ to $T^{x_2}{}_{x_2} = 21.578866$. The energy density of this random configuration is negative, and the three 3-space pressures differ from each other (as do the three extra-time pressures): a random configuration is not isotropic.

**In [10], the diagonal entries and their two parts (Figure 09a.3).**

```python
positions = np.arange(8)  # one group of bars per direction
fig, ax = plt.subplots(figsize=(8.0, 4.2))
ax.bar(positions - 0.27, kinetic_parts, width=0.27, label="kinetic part")
ax.bar(positions, [-potential] * 8, width=0.27, label="potential part $-(mS + U)$")
ax.bar(positions + 0.27, np.diag(T), width=0.27, label="total $T^\\mu{}_\\mu$")
ax.axhline(0.0, color="black", linewidth=0.8)
ax.set_xticks(positions, [f"${n[0]}_{n[1]}$" for n in NAMES])
ax.set_xlabel("direction $\\mu$")
ax.set_ylabel("value (energy per unit volume)")
ax.set_title("Diagonal entries $T^\\mu{}_\\mu$ and their two parts")
ax.legend(fontsize=8)
save_figure(fig, "diagonal_parts", ...)
```

`np.arange(8)` is 0, 1, ..., 7. `ax.bar(x, heights, width=...)` draws bars; the three calls place three bars side by side for each direction, shifted by $-0.27$, 0 and $+0.27$. `ax.axhline(0.0, ...)` draws a horizontal line at zero. **What Figure 09a.3 shows.** For each of the eight directions: the kinetic part $\sum_{\nu \neq \mu}K_\nu$ (left bar), the potential part $-(mS + U)$ (middle bar, the same in every group) and their sum $T^\mu{}_\mu$ (right bar), in units of energy per unit volume. The group at $x_4$ shows $-\rho$. The student should see that only the kinetic parts make the directions differ.

**In [11], the trace, the kinetic sum, and the configuration put on shell.**

```python
V = m + lam * S  # V = m + U'(S), with U'(S) = lambda S
E = sum(gamma_up[mu] @ (dPhi[mu] + Omega[mu] @ Phi) for mu in range(8)) - V * Phi
E_bar = sum((bar(dPhi[mu]) - bar(Phi) @ Omega[mu]) @ gamma_up[mu]
            for mu in range(8)) + V * bar(Phi)
```

These lines compute the effective mass $V = m + \lambda S$, the field-equation expression $E = \gamma^\mu D_\mu\Phi - V\Phi$ (a column of 16 numbers) and its adjoint $\bar E = (D_\mu\bar\Phi)\gamma^\mu + V\bar\Phi$ (a row), exactly as defined in Section 9.8.

```python
check(abs(np.trace(T) - (7 * K.sum() - 8 * (m * S + U))) < 1e-11
      and recorded(THEORY_WL, "EMT_trace_C") == "PASS",
      "trace: sum of T^mu_mu = 7 sum K - 8 (m S + U), off shell",
      record=f"{THEORY_WL}, check EMT_trace_C")
kinetic_sum = V * S + 0.5 * (bar(Phi) @ E - E_bar @ Phi)
check(abs(K.sum() - kinetic_sum) < 1e-11
      and recorded(THEORY_WL, "kinetic_sum_on_shell_C") == "PASS",
      "sum K = V S + (1/2)(Phibar E - Ebar Phi), off shell",
      record=f"{THEORY_WL}, check kinetic_sum_on_shell_C")
report("|E| of the random configuration (it is off shell)",
       f"{np.linalg.norm(E):.6f}")
```

`np.trace(T)` is the sum of the diagonal. The two checks confirm, for the random (off-shell) configuration, the trace identity and the kinetic-sum identity of Section 9.8. `np.linalg.norm(E)` is the length of the column $E$, the square root of the sum of the squared sizes of its 16 entries; it is 19.335808, far from zero: the random configuration does not satisfy the field equation.

```python
# The evolution form of the field equation gives d4 Phi from the other derivatives.
rest = sum(gamma[a] @ dPhi[a] / f[a] for a in range(8) if a != 3)
dPhi_on = dPhi.copy()
dPhi_on[3] = -gamma[3] @ (V * Phi - rest - 3 * H * gamma[7] @ Phi)
E_on = sum(gamma_up[mu] @ (dPhi_on[mu] + Omega[mu] @ Phi) for mu in range(8)) - V * Phi
S_on, U_on, L0_on, K_on, T_on = energy_momentum(Phi, dPhi_on, f, gamma_up, gamma_down,
                                                Omega)
check(np.abs(E_on).max() < 1e-12, "with d4 Phi from the evolution form, E = 0")
```

Now the configuration is put on shell at the point. `rest` is $\sum_{a \neq 4}\frac{1}{f_a}\gamma^{(a)}\partial_a\Phi$ (the `if a != 3` in the comprehension skips $x_4$). `dPhi.copy()` makes a separate copy of the table, so that the random one is kept, and its row 3 is replaced by the evolution form of Section 9.2, $\partial_4\Phi = -\gamma^{(4)}[V\Phi - \text{rest} - 3H\gamma^{(8)}\Phi]$. The value of $\Phi$ and the other seven derivatives are unchanged, so $S$ and $V$ are unchanged. The field-equation expression is computed again, and the tensor of the new jet; the check confirms that now $E = 0$ up to rounding.

```python
check(abs(K_on.real.sum() - V * S) < 1e-11
      and abs(L0_on.real - (S * lam * S - U)) < 1e-11
      and abs(np.trace(T_on.real) - (-m * S + 3 * lam * S ** 2)) < 1e-10
      and recorded(THEORY_PY, "commuting_trace_on_shell") == "PASS",
      "on shell: sum K = V S, L0 = S U' - U, trace = -m S + 3 lambda S^2",
      record=f"{THEORY_PY}, check commuting_trace_on_shell")
report("trace on shell, -m S + 3 lambda S^2", f"{np.trace(T_on.real):.6f}")
```

The check confirms the three on-shell values of Section 9.8: $\sum_\mu K_\mu = VS$, $L_0 = SU' - U$ (here `S * lam * S` is $S\,U'(S)$) and the trace $-mS + 3\lambda S^2$, which is printed: $70.447596$. By hand: $-1\cdot(-6.527875) + 3\cdot 0.5\cdot 6.527875^2 = 6.527875 + 63.919721 = 70.447596$.

**In [12], the spin connection in the entry $T^{x_4}{}_{x_1}$.**

```python
dPhi_hom = np.zeros((8, 16), dtype=complex)  # homogeneous: only d4 Phi is nonzero
dPhi_hom[3] = rng.normal(size=16) + 1j * rng.normal(size=16)
D_x1 = dPhi_hom[0] + Omega[0] @ Phi  # D_x1 Phi = Omega_x1 Phi here
Dbar_x1 = bar(dPhi_hom[0]) - bar(Phi) @ Omega[0]  # D_x1 Phibar = -Phibar Omega_x1
K_41 = 0.5 * (bar(Phi) @ gamma_up[3] @ D_x1 - Dbar_x1 @ gamma_up[3] @ Phi)
expected = 0.5 * np.exp(a4) * np.sin(z) ** (1 / 6) * H * (
    bar(Phi) @ gamma[3] @ gamma[0] @ gamma[7] @ Phi)
```

A homogeneous jet has only the time derivative: the table `dPhi_hom` is zero except row 3, which is drawn at random. Then $D_{x_1}\Phi = \Omega_{x_1}\Phi$ and $D_{x_1}\bar\Phi = -\bar\Phi\Omega_{x_1}$ (the derivative parts are zero), `K_41` is $K^{x_4}{}_{x_1} = \frac12(\bar\Phi\gamma^{x_4}D_{x_1}\Phi - D_{x_1}\bar\Phi\gamma^{x_4}\Phi)$, and `expected` is the result of Section 9.12, $\frac12e^{a_4}\sin^{1/6}z\,H\,\bar\Phi\gamma^{(4)}\gamma^{(1)}\gamma^{(8)}\Phi$.

```python
SCOPE_PY = "Revision/theory/reports/python-scope.json"
SCOPE_WL = "Revision/theory/reports/wolfram-scope.json"
check(abs(K_41 - expected) < 1e-12 and abs(K_41) > 0.01
      and recorded(SCOPE_PY, "spin_connection_in_the_energy_momentum_tensor") == "PASS"
      and recorded(SCOPE_WL, "spin_connection_in_the_energy_momentum_tensor") == "PASS",
      "K^x4_x1 of a homogeneous configuration is the nonzero connection term",
      record=f"{SCOPE_PY} and {SCOPE_WL}, check "
             "spin_connection_in_the_energy_momentum_tensor")
report("K^x4_x1 (homogeneous configuration)", f"{K_41.real:.6f}")
```

The check requires the two numbers to agree and, so that the test is not empty, the result to be clearly nonzero (larger than 0.01 in size). It prints $K^{x_4}{}_{x_1} = -0.203311$.

**In [13], the Christoffel symbols with sympy.**

```python
import sympy as sp  # exact algebra and calculus with symbols

x = sp.symbols("x1:9", real=True)  # the coordinates x1, ..., x8 (x[0] ... x[7])
Hs = sp.symbols("H", positive=True)  # the author's constant, as a symbol
a4_function = sp.Function("a4")(x[3])  # a general function a4(x4)
zs = 6 * Hs * x[7]  # z = 6 H x8
space_entry = sp.exp(2 * a4_function) * sp.sin(zs) ** sp.Rational(1, 3)
extra_entry = -sp.exp(-2 * a4_function) * sp.sin(zs) ** sp.Rational(1, 3)
g = sp.diag(*([space_entry] * 3 + [-1] + [extra_entry] * 3 + [sp.cot(zs) ** 2]))
```

From here on the notebook computes exactly, with symbols instead of numbers. `sp.symbols("x1:9", real=True)` makes the eight real symbols $x_1, \dots, x_8$, stored as `x[0]` to `x[7]`; `Hs` is the symbol $H$, declared positive. `sp.Function("a4")(x[3])` is an unknown function $a_4(x_4)$: the results hold for every history. `sp.Rational(1, 3)` is the exact fraction $1/3$ (the Python number `1 / 3` would be rounded). `sp.diag(*list)` builds the diagonal matrix with the list on its diagonal (the star hands the items of the list over as separate arguments): the author's metric, symbol by symbol.

```python
christoffel = {}  # (lambda, mu, nu) -> Gamma^lambda_mu nu, only the nonzero ones
for l in range(8):
    for i in range(8):
        for j in range(i, 8):  # mu <= nu
            value = sp.simplify((sp.diff(g[l, j], x[i]) + sp.diff(g[l, i], x[j])
                                 - sp.diff(g[i, j], x[l])) / (2 * g[l, l]))
            if value != 0:
                christoffel[(l, i, j)] = value
say(f"{len(christoffel)} nonzero Christoffel symbols with mu <= nu")
```

The three loops take every $\lambda$ (`l`) and every pair $\mu \le \nu$ (`i`, `j`; `range(i, 8)` starts at `i`) and compute the diagonal-metric formula of Section 9.9, $\frac{1}{2g_{\lambda\lambda}}(\partial_\mu g_{\lambda\nu} + \partial_\nu g_{\lambda\mu} - \partial_\lambda g_{\mu\nu})$; `sp.diff(expr, x[i])` is the partial derivative and `sp.simplify` brings the result to a simplest form. The nonzero symbols are stored in the dictionary `christoffel` under the key `(l, i, j)`. There are $8 \cdot 36 = 288$ expressions to simplify, which takes a few seconds. The cell prints `25 nonzero Christoffel symbols with mu <= nu`, the count of Section 9.9.

**In [14], comparison with the record's list.**

```python
a4s, a4ps = sp.symbols("a4 a4p", real=True)  # plain symbols for a4 and da4/dx4


def plain(expression):
    """Replace da4/dx4 by the symbol a4p and a4(x4) by the symbol a4."""
    return expression.subs(sp.Derivative(a4_function, x[3]), a4ps).subs(
        a4_function, a4s)
```

The record writes $a_4$ and $a_4'$ as plain names. `plain` makes our symbols comparable: `.subs(old, new)` replaces every occurrence of `old` by `new`; the derivative is replaced first (replacing $a_4(x_4)$ first would destroy it).

```python
WOLFRAM_TO_SYMPY = [  # (Wolfram text, sympy text), applied in this order
    ("Derivative[1][a4][x4]", "a4p"), ("Derivative[1, 0][rho][x4, x8]", "rho_4"),
    ("Derivative[0, 1][p8][x4, x8]", "p8_8"), ("[x4, x8]", ""), ("a4[x4]", "a4"),
    ("Sin[", "sin("), ("Cos[", "cos("), ("Cot[", "cot("), ("Sec[", "sec("),
    ("Csc[", "csc("), ("E^", "E**"), ("^", "**"), ("[", "("), ("]", ")"),
    ("{", "["), ("}", "]")]


def from_wolfram(text):
    """Translate a formula of the record from the Wolfram Language into sympy."""
    for old, new in WOLFRAM_TO_SYMPY:
        text = text.replace(old, new)
    return text
```

The record's formulas are written in the Wolfram Language, which uses square brackets for the arguments of functions (`Sin[z]`), `^` for powers and braces for lists. `from_wolfram` translates such a text into sympy's notation by plain text replacements, in the order of the list: the long derivative names first, then the function names, then the single brackets and braces.

```python
FORMULAS = {item["key"]: item["wl"] for item in json.loads(repository_file(
    "Revision/theory/field-theory.json").read_text(encoding="utf-8"))["formulas"]}
NAMES_SYMPY = {"a4": a4s, "a4p": a4ps, "H": Hs, "x8": x[7], "E": sp.E}
record_list = sp.sympify(from_wolfram(FORMULAS["christoffel_nonzero"]),
                         locals=NAMES_SYMPY)
# The record counts the coordinates 1 ... 8; Python counts 0 ... 7.
record_symbols = {(int(e[0]) - 1, int(e[1]) - 1, int(e[2]) - 1): e[3]
                  for e in record_list}
```

`FORMULAS` is a **dictionary comprehension**: it maps the key of every formula of the record file to its Wolfram text. `sp.sympify(text, locals=...)` reads a translated text as a sympy expression, with the names `a4`, `a4p`, `H`, `x8` and `E` (Euler's number $e$) bound to our symbols. The record's list consists of entries $\{\lambda, \mu, \nu, \Gamma^\lambda{}_{\mu\nu}\}$ with the coordinates counted from 1; `record_symbols` stores them under keys counted from 0.

```python
same = sorted(record_symbols) == sorted(christoffel) and all(
    sp.simplify(plain(christoffel[key]) - record_symbols[key]) == 0
    for key in christoffel)
check(len(christoffel) == 25 and same
      and recorded(THEORY_WL, "christoffel_count") == "PASS",
      "25 nonzero Christoffel symbols, equal to the record's list one by one",
      record=f"{THEORY_WL}, check christoffel_count (formula christoffel_nonzero)")
for (l, i, j), value in sorted(christoffel.items()):
    print(f"Gamma^{NAMES[l]}_({NAMES[i]} {NAMES[j]}) = {plain(value)}")
```

`same` is true when both dictionaries have the same 25 keys (`sorted` lists the keys in order) and, for each key, the difference of the two symbols simplifies to exactly 0. The loop prints the 25 symbols in order; sympy writes $\cot$ as `1/tan` and $\sec z$ as `1/cos`. The printed list is the table of Section 9.9; for example `Gamma^x8_(x8 x8) = -12*H/sin(12*H*x8)`.

**In [15], the covariant divergence of a diagonal tensor.**

```python
rho_f, p3_f, pt_f, p8_f = [sp.Function(n)(x[3], x[7]) for n in ("rho", "p3", "pt",
                                                                 "p8")]
T_diag = sp.diag(p3_f, p3_f, p3_f, -rho_f, pt_f, pt_f, pt_f, p8_f)  # T^mu_nu


def gamma_symbol(l, i, j):
    """Gamma^l_ij for any order of i and j (zero when it is not in the list)."""
    return christoffel.get((l, min(i, j), max(i, j)), 0)
```

`rho_f`, `p3_f`, `pt_f` and `p8_f` are four unknown functions of $x_4$ and $x_8$, and `T_diag` is the diagonal tensor $\mathrm{diag}(p_3, p_3, p_3, -\rho, p_t, p_t, p_t, p_8)$ of Section 9.9. `gamma_symbol(l, i, j)` returns $\Gamma^l{}_{ij}$ for either order of `i` and `j` (the symbol is symmetric, and the dictionary stores only $i \le j$); `.get(key, 0)` returns 0 for a symbol that is not stored.

```python
divergence = []
for nu in range(8):
    value = sum(sp.diff(T_diag[mu, nu], x[mu]) for mu in range(8))
    value += sum(gamma_symbol(mu, mu, l) * T_diag[l, nu]
                 for mu in range(8) for l in range(8))
    value -= sum(gamma_symbol(l, mu, nu) * T_diag[mu, l]
                 for mu in range(8) for l in range(8))
    divergence.append(sp.simplify(value))
nonzero = [NAMES[nu] for nu in range(8) if divergence[nu] != 0]
say("components of the divergence that are not identically zero: nu = "
    + ", ".join(nonzero))
```

For each $\nu$ the loop builds the three sums of the general formula of Section 9.9 literally (without the lemma): $\sum_\mu\partial_\mu T^\mu{}_\nu$, plus $\sum_{\mu,\lambda}\Gamma^\mu{}_{\mu\lambda}T^\lambda{}_\nu$, minus $\sum_{\mu,\lambda}\Gamma^\lambda{}_{\mu\nu}T^\mu{}_\lambda$ (`+=` adds to `value`, `-=` subtracts from it), simplifies the result and appends it to the list. `", ".join(...)` writes the names of the nonzero components separated by commas. The cell prints `nu = x4, x8`: the other six components vanish identically.

**In [16], comparison with the record's identities.**

```python
rho_4, p8_8, p3s, pts, p8s = sp.symbols("rho_4 p8_8 p3 pt p8", real=True)


def plain_t(expression):
    """Write the derivatives and functions as the plain symbols of the record."""
    expression = expression.subs({sp.Derivative(rho_f, x[3]): rho_4,
                                  sp.Derivative(p8_f, x[7]): p8_8})
    expression = expression.subs({p3_f: p3s, pt_f: pts, p8_f: p8s,
                                  rho_f: sp.Symbol("rho", real=True)})
    return plain(expression)
```

`plain_t` writes our results with the record's plain names: $\partial_4\rho$ as `rho_4`, $\partial_8p_8$ as `p8_8`, and the four functions as plain symbols; `.subs` also accepts a dictionary of replacements.

```python
NAMES_T = dict(NAMES_SYMPY, rho_4=rho_4, p8_8=p8_8, p3=p3s, pt=pts, p8=p8s)
record_divergence = sp.sympify(from_wolfram(FORMULAS["energy_exchange"][0]),
                               locals=NAMES_T)
agree = all(sp.simplify(plain_t(divergence[n]) - record_divergence[n]) == 0
            for n in range(8))
x4_line = -rho_4 - 3 * a4ps * (p3s - pts)
x8_line = p8_8 + 3 * Hs * sp.cot(zs) * (2 * p8s - p3s - pts)
```

`NAMES_T` extends the dictionary of names. The record's formula `energy_exchange` is a list of three texts; the first one (`[0]`) is the list of all eight components of the divergence, which `record_divergence` reads. `agree` is true when each of our eight components equals the record's, exactly. `x4_line` and `x8_line` are the two results of Section 9.9, typed by hand.

```python
check(agree and recorded(THEORY_WL, "energy_exchange_equation") == "PASS"
      and recorded(THEORY_PY, "energy_exchange_equation") == "PASS",
      "the eight components agree with the record formula energy_exchange",
      record=f"{THEORY_WL} and {THEORY_PY}, check energy_exchange_equation")
check(sp.simplify(plain_t(divergence[3]) - x4_line) == 0
      and recorded(LEAD, "divergence_x4_component") == "PASS",
      "nabla_mu T^mu_x4 = -d4 rho - 3 a4p (p3 - p_t)",
      record=f"{LEAD}, check divergence_x4_component")
check(sp.simplify(plain_t(divergence[7]) - x8_line) == 0
      and recorded(LEAD, "divergence_x8_component") == "PASS",
      "nabla_mu T^mu_x8 = d8 p8 + 3 H cot z (2 p8 - p3 - p_t)",
      record=f"{LEAD}, check divergence_x8_component")
check(all(divergence[n] == 0 for n in (0, 1, 2, 4, 5, 6))
      and recorded(LEAD, "divergence_other_components_zero") == "PASS",
      "the components x1, x2, x3, x5, x6, x7 vanish identically",
      record=f"{LEAD}, check divergence_other_components_zero")
print("nabla_mu T^mu_x4 =", x4_line)  # rho_4 = d rho/d x4
print("nabla_mu T^mu_x8 =", x8_line)  # p8_8 = d p8/d x8
```

Four checks: all eight components agree with the record's formula (whose check passed in both engines); the $x_4$ component and the $x_8$ component equal the hand-derived lines (and the lead's independent checks passed); and the other six components are zero. The last two lines print the two identities in sympy's spelling, `-3*a4p*(p3 - pt) - rho_4` and `3*H*(-p3 + 2*p8 - pt)*cot(6*H*x8) + p8_8`.

**In [17], the first-law reading.**

```python
f_space = sp.exp(a4_function) * sp.sin(zs) ** sp.Rational(1, 6)  # f1 = f2 = f3
f_extra = sp.exp(-a4_function) * sp.sin(zs) ** sp.Rational(1, 6)  # f5 = f6 = f7
V3 = f_space ** 3  # e^(3 a4) sin^(1/2) z
Vt = f_extra ** 3  # e^(-3 a4) sin^(1/2) z
V7 = V3 * Vt * sp.cot(zs)  # times f8 = cot z (and f4 = 1)
check(sp.simplify(V7 - sp.cos(zs)) == 0, "V3 Vt f8 = cos z, independent of x4")
```

These lines build the three volumes of Section 9.10 with symbols and check $V_7 = \cos z$ exactly.

```python
first_law = (sp.diff(rho_f * V7, x[3]) + p3_f * V7 / V3 * sp.diff(V3, x[3])
             + pt_f * V7 / Vt * sp.diff(Vt, x[3]))
# The first law says first_law = 0; it must be -V7 times the x4 divergence.
check(sp.simplify(first_law + V7 * divergence[3]) == 0,
      "d(rho V7)/dx4 + p3 (V7/V3) dV3/dx4 + p_t (V7/Vt) dVt/dx4 = -V7 nabla_mu T^mu_x4")
```

`first_law` is the first law of Section 9.10 with everything on one side, $\frac{d}{dx_4}(\rho V_7) + p_3\frac{V_7}{V_3}\frac{dV_3}{dx_4} + p_t\frac{V_7}{V_t}\frac{dV_t}{dx_4}$. The check shows that it equals $-V_7$ times the $x_4$ component of the divergence: setting one to zero is the same as setting the other to zero. The reading is an interpretation of an exact identity, not an extra result.

**In [18], the volumes along the history (Figure 09a.4).**

```python
x4_axis = np.linspace(0.0, 8.0, 401)  # the time x4
growth = np.exp(3 * A * H * x4_axis)  # V3(x4)/V3(0) = e^(3 A H x4)
fig, ax = plt.subplots()
ax.plot(x4_axis, growth, label="3-space volume $V_3$ (inflates)")
ax.plot(x4_axis, 1 / growth, "--", label="extra-time volume $V_t$ (deflates)")
ax.plot(x4_axis, growth / growth, ":", color="black",
        label="7-volume $V_7 = V_3 V_t \\cot z$ (constant)")
ax.set_yscale("log")
ax.set_xlabel("time $x_4$")
ax.set_ylabel("volume divided by its value at $x_4 = 0$")
ax.set_title("Volumes along the history $a_4 = A H x_4$ ($A = 1$, $H = 0.25$)")
ax.legend()
save_figure(fig, "volumes_first_law", ...)
```

On the history $a_4 = AHx_4$ the ratio $V_3(x_4)/V_3(0)$ is $e^{3AHx_4}$, the ratio for $V_t$ is its inverse, and the ratio for $V_7$ is 1 (`growth / growth`). **What Figure 09a.4 shows.** The three volume ratios (pure numbers) against the time $x_4$ from 0 to 8 on a logarithmic axis: $V_3$ rises along a straight line to $e^{6} \approx 403$, $V_t$ falls along the mirror line to $e^{-6}$, and $V_7$ stays at 1. The student should see that the extra times deflate, exponentially, and that their shrinking exactly compensates the growth of 3-space; this is why the energy density changes only through the difference $p_3 - p_t$.

**In [19], the x8 identity with sympy.**

```python
P, c = sp.symbols("P c", real=True)  # P = p3 + p_t (a constant) and the constant c
profile = P / 2 + c / sp.sin(zs)  # p8 as a function of x8 (through z)
balance = sp.diff(profile, x[7]) + 3 * Hs * sp.cot(zs) * (2 * profile - P)
check(sp.simplify(balance) == 0,
      "p8 = P/2 + c/sin z solves the x8 identity for every c")
```

`balance` is the $x_8$ component of the divergence for $p_8 = P/2 + c/\sin z$ and $p_3 + p_t = P$; the check confirms that it is zero for every $c$, the solution found in Section 9.11.

```python
y = sp.symbols("y", real=True)
dy_dx8 = sp.diff(sp.log(sp.sin(zs)) / (6 * Hs), x[7])  # y = ln(sin z)/(6 H)
check(sp.simplify(dy_dx8 - sp.cot(zs)) == 0
      and recorded(LEAD, "ks_coordinate_jacobian") == "PASS",
      "y = ln(sin z)/(6 H) has dy/dx8 = cot z",
      record=f"{LEAD}, check ks_coordinate_jacobian")
```

This check differentiates $y = \ln(\sin z)/(6H)$ with respect to $x_8$ and confirms $dy/dx_8 = \cot z$.

```python
z_of_y = sp.asin(sp.exp(6 * Hs * y))  # sin z = e^(6 H y), z between 0 and pi/2
P8, P3, PT = [sp.Function(n)(y) for n in ("P8", "P3", "PT")]
in_x8 = sp.cot(z_of_y) * sp.diff(P8, y) + 3 * Hs * sp.cot(z_of_y) * (2 * P8 - P3 - PT)
in_y = sp.cot(z_of_y) * (sp.diff(P8, y) + 6 * Hs * P8 - 3 * Hs * (P3 + PT))
check(sp.simplify(in_x8 - in_y) == 0
      and recorded(LEAD, "ks_coordinate_form") == "PASS",
      "x8 component = cot z [p8'(y) + 6 H p8 - 3 H (p3 + p_t)]",
      record=f"{LEAD}, check ks_coordinate_form")
```

Solving $\sin z = e^{6Hy}$ for $z$ gives $z = \arcsin(e^{6Hy})$ (`sp.asin`). `P8`, `P3` and `PT` are the three pressures as functions of $y$. `in_x8` is the $x_8$ component with $\partial_8p_8 = \cot z\,dp_8/dy$, and `in_y` the form of Section 9.11; the check confirms that they are the same expression.

**In [20], the pressure profiles of the x8 balance (Figure 09a.5).**

```python
z_grid = np.linspace(0.1, np.pi / 2 - 0.01, 2001)  # z from 0.1 to just below pi/2
x8_grid = z_grid / (6 * H)  # the matching x8 = z/(6 H)
fig, ax = plt.subplots()
worst = 0.0  # the largest relative residual of the balance on the grid
for c_value in (-0.2, -0.1, 0.0, 0.1, 0.2):
    p8_values = 0.5 + c_value / np.sin(z_grid)  # P = 1
    slope = np.gradient(p8_values, x8_grid)  # d p8/d x8, by finite differences
    rhs = -3 * H / np.tan(z_grid) * (2 * p8_values - 1.0)
```

The grid has 2001 values of $z$ between 0.1 and $\pi/2 - 0.01$, and the matching $x_8 = z/(6H)$. For each of five constants $c$ the loop computes the profile $p_8 = 1/2 + c/\sin z$ (so $P = 1$), its slope $dp_8/dx_8$ by **finite differences** (`np.gradient` approximates a derivative by the difference of neighbouring values divided by their distance), and the right-hand side $-3H\cot z\,(2p_8 - 1)$ of the balance.

```python
    # The size of the terms; 1 (the size of P) is added, so that for the flat
    # profile c = 0, whose terms are zero, rounding noise is not divided by zero.
    scale = 1.0 + np.abs(slope).max() + np.abs(rhs).max()
    # [5:-5] leaves out five points at each end, where np.gradient is less exact.
    worst = max(worst, np.abs(slope - rhs)[5:-5].max() / scale)
    style = "-" if c_value == 0.0 else "--"
    ax.plot(z_grid, p8_values, style, label=f"$c = {c_value:g}$")  # g: short form
check(worst < 1e-4, "the drawn profiles satisfy the x8 balance on the grid")
```

The residual, slope minus right-hand side, is divided by the size of the terms; `[5:-5]` drops five points at each end of the grid, and `worst` keeps the largest relative residual of the five profiles. The profile with $c = 0$ is drawn solid, the others dashed; the format `:g` writes a number in its shortest form. The check requires the residual to be below $10^{-4}$: it measures the error of the finite differences, not a failure of the identity.

```python
ax.set_ylim(-2.0, 3.0)
ax.set_xlabel("$z = 6 H x_8$")
ax.set_ylabel("$p_8$ (with $p_3 + p_t = 1$)")
ax.set_title("Pressure profiles allowed by the balance along $x_8$")
ax.legend()
save_figure(fig, "hidden_balance", ...)
report("largest relative residual of the balance on the grid", f"{worst:.1e}")
```

These lines fix the vertical range, label the axes, save the figure and print the residual, $2.3 \cdot 10^{-5}$ (the format `.1e` writes one decimal and a power of ten). **What Figure 09a.5 shows.** The hidden pressure $p_8$ (energy per unit volume) against $z$ from 0.1 to just below $\pi/2$ for five values of $c$. Only the solid line $c = 0$ is flat, at $p_8 = P/2 = 0.5$; every other profile grows in size like $1/\sin z$ towards the tip $z = 0$, upwards for $c > 0$ and downwards for $c < 0$. The student should see that an $x_8$-independent tensor must have $p_8 = (p_3 + p_t)/2$.

**In [21], the last check.**

```python
captions = json.loads(output_file(CAPTION_FILE).read_text(encoding="utf-8"))
expected_files = ["09a_1_kinetic_weights.png", "09a_2_tensor_heat_map.png",
                  "09a_3_diagonal_parts.png", "09a_4_volumes_first_law.png",
                  "09a_5_hidden_balance.png"]
check(sorted(captions) == expected_files and all(
    output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in expected_files),
    "the five figures of this notebook are saved and captioned")
all_checks_passed()
```

The cell reads the captions file back, checks that it holds exactly the five figure names (sorted) and that the five files exist, and prints the last line, `ALL 27 CHECKS PASSED (notebook 09a)`: two checks each in In [2], In [3], In [5], In [7] and In [9], four in In [11], one each in In [12] and In [14], four in In [16], two in In [17], three in In [19], and one each in In [20] and In [21].
