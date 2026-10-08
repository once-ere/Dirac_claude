## 9. The energy-momentum tensor, pressures, equations of state, conservation identities

Gravity has to be told where the energy is. In Einstein's theory, and in the Einstein-Lovelock theory that Chapter 12 uses for the author's metric, the right-hand side of the field equations is a table of numbers called the energy-momentum tensor. It says, at every point, how much energy there is in a unit of volume, how hard the matter pushes in each direction (the pressures), and how energy and momentum flow. This chapter builds that table for the field dirac16complex00 in the author's primordial metric, splits it into a kinetic part and a potential part, defines the energy density, the pressures of 3-space, of the extra times and of the hidden direction, and the equations of state, and derives the two exact conservation identities that the table obeys: one along the time $x_4$, which describes how energy flows between the inflating 3-space and the deflating extra times, and one along the hidden direction $x_8$. Three notebooks compute every statement anew from the Revision record: Notebook 09a builds the tensor at one point and derives the two identities, Notebook 09b studies the condensates (fields that depend on the time only) and their equations of state, and Notebook 09c computes the complete tensor of a condensate, including the entries off the diagonal that the spin connection creates.

### 9.1 What this chapter does

**Why we need this chapter.** Cosmologists describe the matter of the universe, at each moment, by two numbers: the **energy density** $\rho$ (energy per unit volume) and the **pressure** $p$ (the push per unit area, which is also energy per unit volume). Their ratio $w = p/\rho$ is called the **equation of state**. Three values are famous: dust (matter at rest whose particles do not push on each other) has $w = 0$, radiation (light) has $w = 1/3$, and a cosmological constant (the simplest model of dark energy) has $w = -1$. **Dark energy** is the name for the unknown cause of the observed speeding-up of the expansion of the universe, and **dark matter** for the unseen matter that is detected only through its gravity. The author's two hypotheses, called Hypothesis (for dirac16complex) and Hypothesis00 (for dirac16complex00), say that these fields might provide a time-varying equation of state for dark energy or dark matter (they are HYPOTHESES, to be investigated; this chapter does not test them). Before anyone can test such a statement, one must know exactly what $\rho$ and $p$ are for these fields in the author's eight-dimensional metric. That is what this chapter derives.

**What it does.** In eight dimensions there is one energy density and seven pressures, one for each direction other than the time $x_4$. They come in three families: the pressure $p_3$ of the three directions of ordinary space, the pressure $p_t$ of the three extra times, and the pressure $p_8$ of the hidden direction. The chapter

- defines the energy-momentum tensor by the response of the action to a change of the metric, and derives from this definition, line by line, its diagonal entries $T^\mu{}_\mu = L_0 - K_\mu$ (Section 9.5);
- states the tensor that a variation of the vielbein gives and its symmetric part, the complete tensor used in this book, says when the two agree, and proves that the complete tensor is real and that its lowered form is symmetric (Section 9.6);
- splits the energy density and the pressures into kinetic and potential parts and defines the equations of state (Section 9.7);
- derives the trace identity and the values that the field equation imposes (Section 9.8);
- derives the covariant divergence of a diagonal tensor in the author's metric and from it the two conservation identities (Sections 9.9 to 9.11);
- shows where the spin connection, which drops out of the Lagrangian, does enter the tensor (Section 9.12);
- builds the exact condensates, computes their equation of state $w = x/(2 + x)$ with $x = \lambda S/m$, and shows that the energy of the commuting field has no lower bound (Sections 9.18 to 9.21);
- computes the complete tensor of a condensate, with 42 entries off the diagonal, and the exact condensates whose tensor is diagonal (Section 9.26).

**What it does not do.** The equation of state that an observer living in 3-space would infer (after integrating over the hidden direction and the extra times), its change in time and any comparison with supernova data (the measured brightness of distant exploding stars, from which astronomers infer the equation of state of dark energy) are not part of the Revision record: they are OPEN, and this chapter claims nothing about them. The anticommuting field dirac16complex obeys the same formulas in its Grassmann algebra; for the quantised field the record defines the tensor as a normal-ordered operator, on a positive space of states constructed only for single good-sector momenta with frozen coefficients, and for $\lambda \neq 0$ it verifies the operator form of the on-shell identity only in a finite model under Wick ordering (Section 9.13 explains these words and states these limits exactly); this chapter computes numbers only for the commuting field dirac16complex00.

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

**The field.** dirac16complex00 is a column $\Phi$ of 16 ordinary (commuting) complex numbers at every point (Chapter 7). Its **Dirac adjoint** is the row $\bar\Phi = \Phi^\dagger C$ (the dagger means: transpose and take the complex conjugate of every entry), and the **scalar** is the number $S = \bar\Phi\Phi = \Phi^\dagger C\Phi$. A number of the form $\bar\Phi M\Phi$, with a fixed $16 \times 16$ matrix $M$, is called a **bilinear** of the field (it contains the field twice: once in the row $\bar\Phi$ and once in the column $\Phi$); $S$ is the simplest bilinear, with $M = 1$. The potential is $U(S) = \frac{\lambda}{2}S^2$, so $U'(S) = \lambda S$; $m$ is the mass.

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

The terms with $a_4'$ cancel: the three inflating directions and the three deflating directions contribute equal and opposite amounts. The cancellation is due to the deflation. The lead's independent check computes the same sum for a metric in which the extra times inflate like 3-space and finds that a term $3a_4'\gamma^{(4)}$ survives. Both statements are PROVED in the Revision record:

| statement | Revision report | check |
| --- | --- | --- |
| $\sum_\mu\gamma^\mu\Omega_\mu = 3H\gamma^{(8)}$ | `Revision/theory/reports/python-field-theory.json` | `gamma_mu_Omega_mu_equals_3H_gamma_x8` |
| the same, computed independently by the lead | `Revision/lead_checks/reports/emt-divergence-and-spin-connection.json` | `gamma_Omega_equals_3H_gamma8` |
| with inflating extra times a term $3a_4'\gamma^{(4)}$ survives | `Revision/lead_checks/reports/emt-divergence-and-spin-connection.json` | `negative_control_inflating_extra_times` |

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

For a configuration that looks the same in the three directions of 3-space (such a configuration is called **isotropic** in 3-space), $T^{x_1}{}_{x_1} = T^{x_2}{}_{x_2} = T^{x_3}{}_{x_3} = p_3$, and likewise $p_t$ for a configuration isotropic in the extra times. Along an extra time, which is time-like, the entry $T^{x_t}{}_{x_t}$ is called a pressure by definition; it has no everyday meaning.

**The definition.** The **action** is the integral of the Lagrangian density over the eight coordinates, $S_{\rm act} = \int\mathcal{L}\,d^8x$. The energy-momentum tensor is defined by how the action responds when the metric is changed a little, everywhere inside a bounded region:

$$
\delta S_{\rm act} = \tfrac12\int\sqrt{|g|}\;T^{\mu\nu}\,\delta g_{\mu\nu}\;d^8x
$$

for every small change $\delta g_{\mu\nu}$ (record normalisation; `Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md` section 8). Here $\delta$ means "the first-order change": if a quantity changes from $Q$ to $Q + \varepsilon Q_1 + \varepsilon^2 Q_2 + \dots$ when a small number $\varepsilon$ is switched on, then $\delta Q = \varepsilon Q_1$, and the terms with $\varepsilon^2$ and higher powers are dropped. For a spinor field the metric is changed through the vielbein factors, with the 16 components of $\Phi$ held fixed (the record's definition is $T^\nu{}_\mu = e^b{}_\mu\,\frac{1}{\sqrt{|g|}}\,\delta S_{\rm act}/\delta e^b{}_\nu$; check `T_vielbein_variation_closed_form_C` of `Revision/theory/reports/wolfram-field-theory.json` computes it for all 64 entries).

**What the definition fixes, and what it does not.** The metric is symmetric, $g_{\mu\nu} = g_{\nu\mu}$, so every change $\delta g_{\mu\nu}$ is symmetric too. Split any table $T^{\mu\nu}$ into its symmetric part $\frac12(T^{\mu\nu} + T^{\nu\mu})$ and its antisymmetric part $A^{\mu\nu} = \frac12(T^{\mu\nu} - T^{\nu\mu})$. In the double sum $\sum_{\mu,\nu}A^{\mu\nu}\,\delta g_{\mu\nu}$ the term $(\mu, \nu)$ and the term $(\nu, \mu)$ cancel, because $A^{\nu\mu} = -A^{\mu\nu}$ while $\delta g_{\nu\mu} = \delta g_{\mu\nu}$; so the antisymmetric part never enters the formula above, and the formula fixes only the **symmetric part** of $T^{\mu\nu}$. The vielbein carries more information than the metric (it also fixes the orientation of the frame), and the tensor obtained by varying the vielbein can have an antisymmetric part as well. Section 9.6 states what that part is and which tensor this book uses.

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

**The tensor from the vielbein variation.** The off-diagonal entries need a change of the vielbein that is not diagonal, and with it the change of the spin connection; this calculation is long, and the Revision record carries it out exactly for all 64 entries (PROVED; `Revision/theory/reports/wolfram-field-theory.json`, check `T_vielbein_variation_closed_form_C`; record formula `T_variation` of `Revision/theory/field-theory.json`). Its result, which we call the **variation tensor** $T_{\rm var}$, is

$$
T_{\rm var}{}^\nu{}_\mu = \delta^\nu_\mu\,L_0 - \tfrac12\Big(\bar\Phi\gamma^\nu D_\mu\Phi - D_\mu\bar\Phi\,\gamma^\nu\Phi\Big) - \tfrac14\sum_{\rho,\lambda}g_{\mu\rho}\,\nabla_\lambda\Big(\bar\Phi\{\gamma^\lambda, \Sigma^{\nu\rho}\}\Phi\Big), \qquad \Sigma^{\nu\rho} = \tfrac14\big(\gamma^\nu\gamma^\rho - \gamma^\rho\gamma^\nu\big),
$$

where $\delta^\nu_\mu$ is 1 for $\nu = \mu$ and 0 otherwise, $\{A, B\} = AB + BA$ is the anticommutator and $\nabla_\lambda$ is the covariant derivative (the derivative corrected by Christoffel symbols, Section 9.9). The last term comes from the change of the spin connection; the record calls the bilinear in it the totally antisymmetric **spin density** (it changes sign when two of its three indices are exchanged). We take this formula from the record and do not derive it. Because of its last term, the variation tensor is in general not symmetric: its lowered form $g_{\nu\nu}T_{\rm var}{}^\nu{}_\mu$ has an antisymmetric part.

**Its symmetric part: the Belinfante tensor.** The record proves that the symmetric part of the variation tensor (with both indices raised, $\frac12(T_{\rm var}^{\nu\rho} + T_{\rm var}^{\rho\nu})$) is, for all 36 pairs $\nu \le \rho$ and for every configuration, solution or not, the **symmetric (Belinfante) energy-momentum tensor** (named after the physicist F. J. Belinfante, who showed how to make the energy-momentum tensor of a spinor field symmetric) (PROVED; same report, check `T_symmetric_part_Belinfante_C`; record formula `T_symmetric`):

$$
T^\nu{}_\mu = \delta^\nu_\mu\,L_0 - \tfrac14\Big(\bar\Phi\gamma^\nu D_\mu\Phi - D_\mu\bar\Phi\,\gamma^\nu\Phi + \bar\Phi\gamma_\mu D^\nu\Phi - D^\nu\bar\Phi\,\gamma_\mu\Phi\Big),
$$

where $\gamma_\mu = g_{\mu\mu}\gamma^\mu$ and $D^\nu = g^{\nu\nu}D_\nu$ with $g^{\nu\nu} = 1/g_{\nu\nu}$.

**When the two tensors agree.** On the diagonal they always agree: the diagonal of an antisymmetric table is zero, so $T_{\rm var}{}^\mu{}_\mu = T^\mu{}_\mu$ for every configuration (the 8 entries of Section 9.5). Off the diagonal they differ by the antisymmetric part of $T_{\rm var}$, and the record proves that this difference is proportional to the field equation: on every solution of the field equation the variation tensor is symmetric and equals $T^\nu{}_\mu$ in all 64 entries, while for a configuration that is not a solution, in general, only the 8 diagonal entries agree (PROVED; `Revision/theory/reports/python-field-theory.json`, check `commuting_emt_equals_general_vielbein_variation_on_shell`, which compares all 64 entries of a general first-order vielbein variation around the author's metric). The reason is the invariance of the action under a rotation of the frame at fixed metric (local Lorentz invariance, in the record's words).

**Which tensor the book uses.** This book, like the record's formulas for the energy density and the pressures, uses the symmetric tensor $T^\nu{}_\mu$ above as "the" energy-momentum tensor: on a solution it is the variation tensor, and for a configuration that is not a solution it is the symmetric part of the variation tensor. Notebook 09a evaluates it for random values of $\Phi$ and its derivatives, which do not solve the field equation; that is why its table $T_{\nu\mu}$ comes out symmetric, while the variation tensor of values that do not solve the field equation is in general not symmetric. Notebooks 09b and 09c evaluate it on exact solutions, where the two tensors are the same. We check two consequences of the formula here.

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

one number for each of the eight values of $\nu$. **Conservation** means $\nabla_\mu T^\mu{}_\nu = 0$ for all eight. On every solution of the field equation the tensor is conserved: this is a theorem, proved in the record from the invariance of the action under a change of coordinates (the **Noether identity**; PROVED, see the table below). We do not repeat that proof. We ask instead: what does conservation say about a tensor of the simplest kind?

| statement | Revision report | check |
| --- | --- | --- |
| the Noether identity of coordinate invariance (off shell) | `Revision/theory/reports/wolfram-field-theory.json` | `Noether_identity_diffeomorphisms_C` |
| $\nabla_\mu T^\mu{}_\nu = 0$ for every solution | `Revision/theory/reports/wolfram-field-theory.json` | `conservation_on_shell_general` |
| the same for dirac16complex00, exact, all eight $\nu$ | `Revision/theory/reports/python-field-theory.json` | `commuting_emt_conservation_on_shell` |
| a wrong tensor is not conserved (negative control) | `Revision/theory/reports/python-field-theory.json` | `commuting_emt_conservation_negative_control` |

**The Christoffel symbols of the author's metric.** For a metric the symbols are $\Gamma^\lambda{}_{\mu\nu} = \frac12\sum_\rho g^{\lambda\rho}(\partial_\mu g_{\rho\nu} + \partial_\nu g_{\rho\mu} - \partial_\rho g_{\mu\nu})$. For a diagonal metric only $\rho = \lambda$ survives and

$$
\Gamma^\lambda{}_{\mu\nu} = \frac{1}{2g_{\lambda\lambda}}\big(\partial_\mu g_{\lambda\nu} + \partial_\nu g_{\lambda\mu} - \partial_\lambda g_{\mu\nu}\big) \qquad (\text{no sum over } \lambda).
$$

The symbol is symmetric in $\mu$ and $\nu$. Six of them, computed line by line (the entries depend only on $x_4$, through $a_4$, and on $x_8$, through $z = 6Hx_8$, whose derivative is $dz/dx_8 = 6H$):

- $\Gamma^{x_1}{}_{x_1x_4} = \frac{1}{2g_{11}}\partial_4 g_{11} = \frac12\,\partial_4\ln g_{11} = \frac12\,\partial_4\big(2a_4 + \tfrac13\ln\sin z\big) = a_4'$; the first step keeps the only nonzero derivative, the second uses $\partial(\ln Q) = \partial Q/Q$, the third writes $\ln g_{11} = 2a_4 + \frac13\ln\sin z$, and the last differentiates ($\sin z$ does not depend on $x_4$).
- $\Gamma^{x_4}{}_{x_1x_1} = \frac{1}{2g_{44}}\big(-\partial_4 g_{11}\big) = \frac{1}{-2}\big(-2a_4'e^{2a_4}\sin^{1/3}z\big) = a_4'\,e^{2a_4}\sin^{1/3}z$; only the third term of the bracket survives ($g_{41} = 0$), $g_{44} = -1$, and the chain rule gives $\partial_4 e^{2a_4} = 2a_4'e^{2a_4}$.
- $\Gamma^{x_8}{}_{x_1x_1} = \frac{1}{2g_{88}}\big(-\partial_8 g_{11}\big) = -\frac{\tan^2 z}{2}\,e^{2a_4}\cdot\tfrac13\sin^{-2/3}z\cos z\cdot 6H = -H e^{2a_4}\,\frac{\sin^{4/3}z}{\cos z}$; here $1/g_{88} = \tan^2 z$, the chain rule gives $\partial_8\sin^{1/3}z = \frac13\sin^{-2/3}z\cos z\cdot 6H$, and $\tan^2 z\,\sin^{-2/3}z\cos z = \sin^{4/3}z/\cos z$.
- $\Gamma^{x_8}{}_{x_8x_8} = \frac12\,\partial_8\ln\cot^2 z = \partial_8\ln\cot z = 6H\cdot\frac{-1/\sin^2 z}{\cot z} = -\frac{6H}{\sin z\cos z} = -\frac{12H}{\sin(12Hx_8)}$, using $\frac{d}{dz}\cot z = -1/\sin^2 z$ and $2\sin z\cos z = \sin 2z$.
- $\Gamma^{x_4}{}_{x_5x_5} = \frac{1}{2g_{44}}\big(-\partial_4 g_{55}\big) = \frac{1}{-2}\big(-2a_4'e^{-2a_4}\sin^{1/3}z\big) = a_4'\,e^{-2a_4}\sin^{1/3}z$; only the third term of the bracket survives ($g_{45} = 0$), $g_{44} = -1$, and the chain rule gives $\partial_4 g_{55} = \partial_4\big(-e^{-2a_4}\sin^{1/3}z\big) = -(-2a_4')e^{-2a_4}\sin^{1/3}z = 2a_4'e^{-2a_4}\sin^{1/3}z$ (two minus signs: the one of the entry and the one of the exponent $-2a_4$).
- $\Gamma^{x_8}{}_{x_5x_5} = \frac{1}{2g_{88}}\big(-\partial_8 g_{55}\big) = \frac{\tan^2 z}{2}\,e^{-2a_4}\cdot\tfrac13\sin^{-2/3}z\cos z\cdot 6H = H e^{-2a_4}\,\frac{\sin^{4/3}z}{\cos z}$; here $-\partial_8 g_{55} = +\partial_8\big(e^{-2a_4}\sin^{1/3}z\big)$ because the entry $g_{55}$ carries a minus sign, and the rest is the computation of $\Gamma^{x_8}{}_{x_1x_1}$; the sign is opposite to that of $\Gamma^{x_8}{}_{x_1x_1}$ because $g_{55}$ and $g_{11}$ have opposite signs.

The three remaining kinds, $\Gamma^{x_i}{}_{x_ix_8}$, $\Gamma^{x_t}{}_{x_4x_t}$ and $\Gamma^{x_t}{}_{x_tx_8}$, have the form of the first bullet, a logarithmic derivative of one diagonal entry; the lemma below gives each of them in one line, and Exercise 1 works two of them out in full. The directions $x_2, x_3$ give the same values as $x_1$, and $x_6, x_7$ the same values as $x_5$, because their entries of the metric are equal. The complete list of the nonzero symbols with $\mu \le \nu$ is (25 symbols: four for each of the six directions $x_i$ and $x_t$, and one more; why there are exactly 25 is shown after the lemma below):

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

The first and the third term of the bracket cancel; then $g_{\mu\mu} = \eta_{\mu\mu}f_\mu^2$ and the chain rule $\partial_\nu f_\mu^2 = 2f_\mu\partial_\nu f_\mu$; finally $\partial_\nu f_\mu/f_\mu = \partial_\nu\ln f_\mu$. Summed over $\mu$ this gives $\sum_\mu\Gamma^\mu{}_{\mu\nu} = \partial_\nu\ln(f_1\cdots f_8) = \partial_\nu\ln\sqrt{|g|}$. For example, $\Gamma^{x_1}{}_{x_1x_8} = \partial_8\ln f_1 = \partial_8\big(a_4 + \frac16\ln\sin z\big) = \frac16\cdot\frac{\cos z}{\sin z}\cdot 6H = H\cot z$, by the chain rule with $dz/dx_8 = 6H$.

**Why there are exactly 25 symbols.** Sort the symbols by how many of the three indices $\lambda, \mu, \nu$ are equal, and use the diagonal formula. Remember that the entries of the metric depend only on $x_4$ and $x_8$, that $g_{44} = -1$ is a constant, and that $g_{88} = \cot^2 z$ does not depend on $x_4$.

- Three different indices: every entry in the bracket, $g_{\lambda\nu}$, $g_{\lambda\mu}$ and $g_{\mu\nu}$, lies off the diagonal and is zero, so the symbol is zero.
- $\mu = \nu \neq \lambda$: the first two terms of the bracket contain $g_{\lambda\mu} = 0$, so $\Gamma^\lambda{}_{\mu\mu} = -\partial_\lambda g_{\mu\mu}/(2g_{\lambda\lambda})$. It is nonzero only when $g_{\mu\mu}$ depends on $x_\lambda$: $\lambda$ is $x_4$ or $x_8$, and $\mu$ is one of the six directions $x_i$, $x_t$, whose entries depend on both ($\mu = x_4$ is excluded because $g_{44}$ is constant, and $\mu = x_8$ with $\lambda = x_4$ because $g_{88}$ does not depend on $x_4$). That makes $2 \cdot 6 = 12$ symbols.
- $\lambda$ equal to exactly one of $\mu$, $\nu$ (stored as $\Gamma^\lambda{}_{\lambda\nu}$ or $\Gamma^\lambda{}_{\nu\lambda}$, whichever has the smaller index first): by the lemma it is $\partial_\nu\ln f_\lambda$, nonzero only when $f_\lambda$ depends on $x_\nu$, that is for $\lambda$ one of the six directions $x_i$, $x_t$ and $\nu = x_4$ or $x_8$ ($f_4 = 1$ is constant, and $f_8 = \cot z$ does not depend on $x_4$). That makes another $6 \cdot 2 = 12$ symbols.
- All three equal: $\Gamma^\lambda{}_{\lambda\lambda} = \partial_\lambda\ln f_\lambda$ by the lemma, nonzero only for $\lambda = x_8$, since $f_8 = \cot z$ is the only factor that depends on its own coordinate. One symbol.

The total is $12 + 12 + 1 = 25$, the count of the table and of the record.

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
\begin{aligned}
&\partial_4\ln f_i = a_4', \qquad \partial_4\ln f_t = -a_4', \qquad \partial_4\ln f_4 = \partial_4\ln f_8 = 0, \\
&\partial_8\ln f_i = \partial_8\ln f_t = \tfrac16\cdot\frac{\cos z}{\sin z}\cdot 6H = H\cot z, \qquad \partial_8\ln f_4 = 0 .
\end{aligned}
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

These are exactly the record's statements (PROVED; the table lists the record files and checks). Notebook 09a derives them again with sympy, from the 25 Christoffel symbols and the general divergence formula, without using the lemma.

| statement | Revision record | formula or check |
| --- | --- | --- |
| all eight components of the divergence of a diagonal tensor | `Revision/theory/field-theory.json` | formula `energy_exchange` |
| the same, verified with the Wolfram Language and with sympy | `Revision/theory/reports/wolfram-field-theory.json` and `python-field-theory.json` | `energy_exchange_equation` |
| the $x_4$ component, computed independently by the lead | `Revision/lead_checks/reports/emt-divergence-and-spin-connection.json` | `divergence_x4_component` |
| the $x_8$ component, computed independently by the lead | the same report | `divergence_x8_component` |
| the other six components vanish | the same report | `divergence_other_components_zero` |

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

The field equations of gravity force the same condition, $p_3 + p_t = 2p_8$, for every source with which the author's metric solves them (Chapter 12 derives these equations). Add the record's 3-space equation (right-hand side $\kappa p_3$) and its extra-time equation (right-hand side $\kappa p_t$): every term with $a_4''$ appears in the two left-hand sides with opposite signs and cancels, and what remains is exactly twice the left-hand side of the hidden equation (right-hand side $\kappa p_8$). Hence $\kappa(p_3 + p_t) = 2\kappa p_8$, and for a coupling $\kappa \neq 0$, $p_3 + p_t = 2p_8$ (PROVED; the table names the record's entries and checks). The conservation identity and the field equations of gravity are therefore consistent.

| statement | Revision record | entry or check |
| --- | --- | --- |
| the 3-space, extra-time and hidden equations | `Revision/field_equations_a4/a4-equations.json` | entry `generalSource`: `space_x1_eq_x2_eq_x3`, `extraTime_x5_eq_x6_eq_x7`, `hidden_x8` |
| the condition $p_3 + p_t = 2p_8$ | `Revision/field_equations_a4/a4-equations.json` | `generalSource.algebraic_condition` |
| the identity of the Lovelock tensors behind it | `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `algebraic_identity_x1_plus_x5_minus_2x8` |
| the same, verified independently with sympy | `Revision/field_equations_a4/reports/python-a4-report.json` | `algebraic_identity` |

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

Everything in Sections 9.3 to 9.12 is algebra with the bilinears $\bar\Phi M\Phi$ and $\bar\Phi M\partial\Phi$, in which the row $\bar\Phi$ always stands to the left of the column. For the anticommuting field dirac16complex (Chapter 7) the same formulas hold, with every bilinear an even element of the Grassmann algebra (a sum of products of two anticommuting numbers; such a product commutes with every element of the algebra, as an ordinary number does); the Revision record verifies them in its checks ending in `_G` (for example `T_diagonal_components_G`, `EMT_trace_G`, `kinetic_sum_on_shell_G` and `grassmann_homogeneous_on_shell_rho_p`; PROVED). After canonical quantisation (Chapter 10; the field becomes an **operator**, a rule that acts on the quantum states) the record defines the tensor as an operator too: every bilinear is replaced by the **normal-ordered** product of the quantised field (the product rearranged so that the operators that remove a particle stand to the right of those that create one, which gives the empty state the energy zero; Chapter 10 defines it exactly), $\hat T^\nu{}_\mu = {:}T^\nu{}_\mu[\hat\Psi, \hat{\bar\Psi}]{:}$, normal ordered with respect to the waves of the **good sector** (the waves that do not depend on the extra times $x_5, x_6, x_7$), and the numbers are **expectation values** (the average value that measurements of the operator give in a given quantum state) (record `Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.md`, section 12). Three limits of the record must be stated.

1. The space of quantum states with positive norms on which this normal ordering rests (the positive **Fock space** of Chapter 10, built from states with definite numbers of particles) is constructed and checked only for single good-sector momenta with frozen coefficients, that is, for plane waves of a flat frame at one point, in which the deflation of the extra times does not enter (PROVED for these examples; `Revision/theory/reports/wolfram-field-theory.json`, checks `mode_hamiltonian_good_sector` and `Fock_space_good_sector_example`, and `Revision/theory/reports/python-field-theory.json`, check `good_sector_positive_fock_realisation`). In the author's curved metric the record imposes no boundary condition at the patch end $z = \pi/2$, and without one the good sector has complex frequencies (waves that grow or decay in time instead of oscillating), for $U = 0$ whenever $m^2 < 9H^2$ (PROVED; `Revision/theory/reports/wolfram-scope.json` and `python-scope.json`, checks `good_sector_hermiticity_up_to_the_brane_flux` and `good_sector_x8_independent_modes_without_boundary_condition`). A space of states with positive norms for the full field is not established (OPEN).
2. For $\lambda \neq 0$ the operator form of the on-shell identity $\sum_\mu\langle{:}K_\mu{:}\rangle = \langle{:}(m + U')S{:}\rangle$ is verified only in a finite model: the Fock space of one good-sector plane-wave mode set with frozen coefficients (flat frame, volume 1, 16 modes, $2^{16}$ states). There it holds as an exact operator identity, for the solution of the interacting operator field equation, if and only if the potential and the tensor are both **Wick ordered** (the whole product of field operators is normal ordered at once: the potential as $\frac{\lambda}{2}{:}SS{:}$, not as $\frac{\lambda}{2}{:}S{:}\,{:}S{:}$, and the tensor as a Wick product, not by subtracting its value in the empty state); with every other ordering tested it fails, already in expectation values (PROVED in that model; `Revision/theory/fock_quartic/reports/fock-quartic.json`, 21 of 21 checks, among them `trace_identity_operator_identity_wick` and `trace_identity_fails_for_every_other_combination`). For the field on a whole slice (many momenta), for the curved $x_8$ dependence and for the extra-time sector the operator identity is OPEN (the field-equations record of Chapter 12 ASSUMES it), and symmetry and conservation of the quartic operator are not verified.
3. Apart from the exact values on the occupation states of that one mode set, numerical expectation values of the tensor for many-fermion states are computed only in the Kohn-Sham approximation of Part IV.

This chapter therefore computes numbers only for the commuting field dirac16complex00.

### 9.14 Example: the tensor at one point and the two identities

The first worked example puts Sections 9.3 to 9.12 on the computer. At one point of the deflating history ($H = 0.25$, $a_4 = AHx_4$ with $A = 1$, so $a_4 = 0.5$ and $a_4' = 0.25$ at $x_4 = 2$, and $z = \pi/4$) it builds the coordinate gammas and the spin connection from the Revision fixture and formula, draws a configuration of dirac16complex00 at random, computes its 64 entries $T^\nu{}_\mu$ literally from the formula of Section 9.6, and checks every identity of Sections 9.5 to 9.8, first off shell and then after putting the configuration on shell with the evolution form. It checks the connection term of Section 9.12. Then it switches to exact symbols: it computes the 25 Christoffel symbols with sympy, compares them with the record, derives the eight components of the divergence of a diagonal tensor and compares them with the record's formula `energy_exchange` and with the lead's checks, checks the first-law reading and the profiles of the $x_8$ balance, and draws five figures.

<!-- NOTEBOOK 09a -->

### 9.17 Line-by-line walk-through of Notebook 09a

The notebook has 21 code cells, In [1] to In [21]. This section explains every line of every one of them, in order. Code that is printed again here is quoted exactly, except that a long figure caption is shortened to a line "...)" (it is printed in full in Section 9.16, under its figure) and that the texts in triple quotes that document a function (its docstring, explained under In [1]) and the comment lines inside the function `save_figure` are left out.

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
# Every file is WRITTEN below OUTPUT_ROOT.  OUTPUT_ROOT is the repository folder unless
# the environment variable TEXTBOOK_OUTPUT_ROOT names another folder; the book's
# checking tool sets it, so that a check run writes into a scratch folder instead.
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

`REPO` is the repository folder; it is never printed, because it differs from computer to computer. `OUTPUT_ROOT` is where files are written: the repository, unless the **environment variable** `TEXTBOOK_OUTPUT_ROOT` (a named text that the computer hands to a program) names another folder; the book's checking tool sets it, so that a check never changes the repository. `repository_file` gives the path of a repository file for reading; `output_file` gives the path at which to write a file and first creates its folder (`mkdir`, where `exist_ok=True` does nothing if the folder exists). `say` prints a text in lines of at most 89 characters (the width of a page of the book), indenting the continuation lines by four blanks. (The comment lines above `REPO` and `OUTPUT_ROOT` and the docstrings of the three functions are left out here; they say the same in words.)

```python
matplotlib.rcdefaults()  # ignore personal matplotlib settings: same figures everywhere
plt.rcParams.update({"figure.figsize": (7.0, 4.2), "font.size": 10.0,
                     "axes.grid": True, "grid.alpha": 0.3})

FIGURE_FOLDER = "Revision/textbook/figures"  # where the figures are saved
CAPTION_FILE = f"{FIGURE_FOLDER}/{NOTEBOOK_ID}.captions.json"  # their captions
FIGURE_NUMBERS = {}  # figure name -> its number k (file name <id>_<k>_<name>.png)
CAPTIONS = {}  # figure file name -> caption, written to CAPTION_FILE after every figure
# Start with an empty captions file ({} is an empty JSON dictionary); save_figure fills
# it.  newline="\n" writes the same line ends on Windows, macOS and Linux.
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
# The author's metric written out: e^(2 a4) sin^(1/3) z, -1, -e^(-2 a4) sin^(1/3) z,
# cot^2 z.
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

The two comment lines say what the next line builds: `authors` writes the author's eight metric entries directly, copied from the author's matrix and not from the factors $f_a$, so that the comparison is a real test. `np.allclose(x, y, rtol=1e-14, atol=0)` is true when every entry of `x` differs from the entry of `y` by less than $10^{-14}$ times its size (a relative tolerance; floating-point numbers carry about 16 significant digits). The second check compares the product of the eight factors (`np.prod`) with $\cos z$, the computation of Section 9.2. `zip(NAMES, f)` pairs each name with its factor, and `report` prints each with six decimals (the format `:.6f`): $f_{x_1} = e^{0.5}\sin^{1/6}(\pi/4) = 1.6487213 \cdot 0.9438743 = 1.556186$, $f_{x_4} = 1$, $f_{x_5} = e^{-0.5}\sin^{1/6}(\pi/4) = 0.6065307 \cdot 0.9438743 = 0.572489$ and $f_{x_8} = \cot(\pi/4) = 1$ (each factor written with seven decimals and each product rounded to six, the precision that the notebook prints; with factors rounded to four decimals the sixth decimal of a product would come out wrong).

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

`.imag` is the imaginary part. The first check confirms the reality of Section 9.6: the largest imaginary part is rounding noise, below $10^{-12}$. Then only the real parts are kept. `g_diag[:, None] * T` multiplies row $\nu$ of the table by $g_{\nu\nu}$ (`[:, None]` turns the eight numbers into a column, which numpy repeats across the eight columns of `T`), giving $T_{\nu\mu}$; the second check compares it with its transpose, the symmetry of Section 9.6 (the 56 entries off the diagonal form 28 pairs). The random values do not solve the field equation, and the table is symmetric because the notebook computes the symmetric (Belinfante) tensor; the tensor of the vielbein variation is in general not symmetric for values that do not solve the field equation (Section 9.6). The cell prints $S = -6.527875$ (negative: $S$ has no fixed sign) and $L_0 = 13.616346$.

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
save_figure(fig, "tensor_heat_map",
            "Heat map of the energy-momentum tensor $T^\\nu{}_\\mu$ of a random "
            ...)
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
save_figure(fig, "diagonal_parts",
            "The eight diagonal entries $T^\\mu{}_\\mu$ (right bar of each group) "
            ...)
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

The check confirms the three on-shell values of Section 9.8: $\sum_\mu K_\mu = VS$, $L_0 = SU' - U$ (here `S * lam * S` is $S\,U'(S)$) and the trace $-mS + 3\lambda S^2$, which is printed: $70.447596$. By hand, with the value of $S$ that the notebook holds before rounding, $S = -6.5278747$: $-1\cdot(-6.5278747) + 3\cdot 0.5\cdot 6.5278747^2 = 6.527875 + 63.919721 = 70.447596$. (With the printed, rounded value $S = -6.527875$ the second term would come out as $63.919728$ and the sum as $70.447603$; the difference of $7 \cdot 10^{-6}$ is the effect of rounding $S$ in its seventh digit, multiplied by the slope $|{-1} + 3S| \approx 20.6$ of the trace as a function of $S$.)

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
save_figure(fig, "volumes_first_law",
            "The 3-space volume $V_3 = e^{3a_4}\\sin^{1/2}z$ (solid), the "
            ...)
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
save_figure(fig, "hidden_balance",
            "The hidden-direction pressure profiles $p_8 = P/2 + c/\\sin z$ that "
            ...)
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

### 9.18 Condensates: exact solutions that depend on the time only

A **condensate** (also called a **homogeneous configuration**) is a field that is the same at every place: it depends on the time $x_4$ only, not on $x_1, x_2, x_3, x_5, x_6, x_7, x_8$. Condensates are the simplest candidates for a smooth cosmological fluid, and the field equation can be solved for them exactly.

**The field equation of a condensate.** In the explicit field equation of Section 9.2 every derivative term with $a \neq 4$ vanishes, and $f_4 = 1$:

$$
\gamma^{(4)}\partial_4\Phi + 3H\gamma^{(8)}\Phi = V\Phi, \qquad V = m + \lambda S .
$$

Multiply from the left by $-\gamma^{(4)}$. Because $(\gamma^{(4)})^2 = -1$, the first term becomes $-\gamma^{(4)}\gamma^{(4)}\partial_4\Phi = \partial_4\Phi$, the second $-3H\gamma^{(4)}\gamma^{(8)}\Phi$, and the right side $-V\gamma^{(4)}\Phi$. Moving the second term to the right:

$$
\partial_4\Phi = M\Phi, \qquad M = -V\gamma^{(4)} + 3H\gamma^{(4)}\gamma^{(8)} .
$$

Neither $a_4$ nor $x_8$ appears: the same condensate solves the field equation on every history $a_4(x_4)$, the deflating one included. (This is the effect of Section 9.3: the connection enters only as $3H\gamma^{(8)}$, which contains no $a_4$.)

**The scalar $S$ is constant.** The equation is nonlinear, because $V$ contains $S = \Phi^\dagger C\Phi$. But $S$ does not change. By the product rule,

$$
\frac{dS}{dx_4} = (\partial_4\Phi)^\dagger C\Phi + \Phi^\dagger C\,\partial_4\Phi = (M\Phi)^\dagger C\Phi + \Phi^\dagger CM\Phi = \Phi^\dagger\big(M^TC + CM\big)\Phi ,
$$

where the last step uses $(M\Phi)^\dagger = \Phi^\dagger M^\dagger$ and $M^\dagger = M^T$ ($M$ is real). Now compute $M^TC$. From the antisymmetry of $C\gamma^{(a)}$ and the symmetry of $C$: $\gamma^{(a)T}C = (C\gamma^{(a)})^T = -C\gamma^{(a)}$. Hence

$$
\begin{aligned}
\gamma^{(4)T}C &= -C\gamma^{(4)}, \\
\big(\gamma^{(4)}\gamma^{(8)}\big)^TC &= \gamma^{(8)T}\gamma^{(4)T}C = -\gamma^{(8)T}C\gamma^{(4)} = C\gamma^{(8)}\gamma^{(4)} = -C\gamma^{(4)}\gamma^{(8)}, \\
M^TC &= -V\gamma^{(4)T}C + 3H\big(\gamma^{(4)}\gamma^{(8)}\big)^TC = VC\gamma^{(4)} - 3HC\gamma^{(4)}\gamma^{(8)} = -CM .
\end{aligned}
$$

The first line is the rule just stated; the second applies it twice (the transpose of a product is the product of the transposes in reverse order) and then uses $\gamma^{(8)}\gamma^{(4)} = -\gamma^{(4)}\gamma^{(8)}$; the third inserts both. So $M^TC + CM = 0$ and $dS/dx_4 = 0$: $S$ keeps its initial value $S_0 = \chi^\dagger C\chi$, where $\chi = \Phi(0)$. Then $V = m + \lambda S_0$ is a constant, and $M$ is a constant matrix.

**The square of $M$.** Multiply out $M^2 = (-V\gamma^{(4)} + 3H\gamma^{(4)}\gamma^{(8)})(-V\gamma^{(4)} + 3H\gamma^{(4)}\gamma^{(8)})$:

$$
\begin{aligned}
M^2 &= V^2\gamma^{(4)}\gamma^{(4)} - 3HV\big(\gamma^{(4)}\gamma^{(4)}\gamma^{(8)} + \gamma^{(4)}\gamma^{(8)}\gamma^{(4)}\big) + 9H^2\gamma^{(4)}\gamma^{(8)}\gamma^{(4)}\gamma^{(8)} \\
&= -V^2 - 3HV\big(-\gamma^{(8)} + \gamma^{(8)}\big) + 9H^2\cdot 1 \\
&= \big(9H^2 - V^2\big)\cdot 1 = k^2\cdot 1, \qquad k^2 = 9H^2 - V^2 .
\end{aligned}
$$

The first line multiplies out the four products; the second uses $\gamma^{(4)}\gamma^{(4)} = -1$, then $\gamma^{(4)}\gamma^{(8)}\gamma^{(4)} = -\gamma^{(4)}\gamma^{(4)}\gamma^{(8)} = \gamma^{(8)}$, and $\gamma^{(4)}\gamma^{(8)}\gamma^{(4)}\gamma^{(8)} = -\gamma^{(4)}\gamma^{(4)}\gamma^{(8)}\gamma^{(8)} = -(-1)(+1) = 1$; the third collects.

**The solution.** For a number $k$ the exponential series $e^{kx} = \sum_n (kx)^n/n!$ splits into its even and odd terms, $\cosh(kx) = \sum_j (kx)^{2j}/(2j)!$ and $\sinh(kx) = \sum_j (kx)^{2j+1}/(2j+1)!$. The same series with the matrix $Mx_4$ in place of $kx$ defines the **matrix exponential** $e^{Mx_4}$, and $e^{Mx_4}\chi$ solves $\partial_4\Phi = M\Phi$ with $\Phi(0) = \chi$. Because $M^2 = k^2$, every even power is $M^{2j} = k^{2j}$ and every odd power is $M^{2j+1} = k^{2j}M$, so the even terms sum to $\cosh(kx_4)$ and the odd terms to $\frac{\sinh(kx_4)}{k}M$:

$$
\Phi(x_4) = \Big(\cosh(kx_4) + \frac{\sinh(kx_4)}{k}\,M\Big)\chi .
$$

A direct check, without series: at $x_4 = 0$ this is $\chi$; its derivative is $\big(k\sinh(kx_4) + \cosh(kx_4)M\big)\chi$; and $M\Phi = \big(\cosh(kx_4)M + \frac{\sinh(kx_4)}{k}M^2\big)\chi = \big(\cosh(kx_4)M + k\sinh(kx_4)\big)\chi$ (using $M^2 = k^2$), the same. Three cases:

- $k^2 < 0$, that is $|V| > 3H$: $k = i\omega$ with $\omega = \sqrt{V^2 - 9H^2}$; since $\cosh(i\omega x) = \cos(\omega x)$ and $\sinh(i\omega x)/(i\omega) = \sin(\omega x)/\omega$, the condensate **oscillates** with the angular frequency $\omega$;
- $k^2 > 0$, that is $|V| < 3H$: the solution contains $e^{kx_4}$ and **grows**;
- $k^2 = 0$: the limit $\Phi = \chi + x_4M\chi$.

These are the record's exact nonlinear homogeneous solutions (PROVED; record formula `exact_solutions` of `Revision/theory/field-theory.json`, and the checks in the table).

| statement | Revision report | check |
| --- | --- | --- |
| $M^2 = k^2\cdot 1$ and $M^TC + CM = 0$ | `Revision/theory/reports/wolfram-field-theory.json` | `solution_matrix_square` |
| the condensate solves the field equation, $S = S_0$, and its $\rho$, $p$ | `Revision/theory/reports/wolfram-field-theory.json` | `exact_solution_nonlinear_homogeneous_C` |
| the same, verified independently with sympy | `Revision/theory/reports/python-field-theory.json` | `exact_nonlinear_homogeneous_solution` |

### 9.19 The energy density, pressure and equation of state of a condensate

**The kinetic terms.** For a condensate $\partial_\mu\Phi = 0$ for $\mu \neq x_4$, so every kinetic term except $K_4$ is zero. On shell the kinetic sum of Section 9.8 gives $\sum_\mu K_\mu = VS$, hence $K_4 = VS$.

**Energy density and pressures.** Insert into Section 9.7:

$$
\begin{aligned}
\rho &= -\sum_{\mu \neq x_4}K_\mu + mS + U = 0 + mS + U(S), \\
p_\mu &= \sum_{\nu \neq \mu}K_\nu - mS - U = K_4 - mS - U = (m + U')S - mS - U = S\,U'(S) - U(S) \qquad (\mu \neq x_4).
\end{aligned}
$$

In the first line all seven kinetic terms vanish; in the second the only kinetic term left in the sum is $K_4$ (because $\mu \neq x_4$), which is $VS = (m + U')S$. The pressure is the same in all seven directions, $p_3 = p_t = p_8 = p$. The kinetic part of the energy density is zero, the kinetic part of every pressure is $VS$, the potential parts are $\pm(mS + U)$. For $U = \frac{\lambda}{2}S^2$, with $SU' = \lambda S^2$:

$$
\rho = mS + \tfrac{\lambda}{2}S^2, \qquad p = \lambda S^2 - \tfrac{\lambda}{2}S^2 = \tfrac{\lambda}{2}S^2 .
$$

(PROVED; `Revision/theory/reports/python-field-theory.json`, check `commuting_homogeneous_on_shell_rho_p`; record formula `EMT_homogeneous_on_shell`.) The trace is $-\rho + 7p = -mS - \frac{\lambda}{2}S^2 + \frac{7\lambda}{2}S^2 = -mS + 3\lambda S^2$, as Section 9.8 requires. Because $S$ is constant, $\rho$ and $p$ are constant in time; this agrees with the energy exchange of Section 9.10, since $p_3 = p_t$ gives $d\rho/dx_4 = 0$.

**No $x_4$-$x_8$ flow.** The record gives the entry (formula `EMT_offdiagonal_x4_x8`)

$$
T^{x_4}{}_{x_8} = -\tfrac14\big(B_{48} - \cot z\,B_{84}\big), \qquad B_{48} = \bar\Phi\gamma^{(4)}\partial_8\Phi - \partial_8\bar\Phi\,\gamma^{(4)}\Phi, \qquad B_{84} = \bar\Phi\gamma^{(8)}\partial_4\Phi - \partial_4\bar\Phi\,\gamma^{(8)}\Phi .
$$

For a condensate $B_{48} = 0$ (no $x_8$ derivative). For $B_{84}$: $\partial_4\Phi = M\Phi$ and $\partial_4\bar\Phi = (M\Phi)^\dagger C = \Phi^\dagger M^TC = -\Phi^\dagger CM = -\bar\Phi M$, so

$$
B_{84} = \bar\Phi\gamma^{(8)}M\Phi + \bar\Phi M\gamma^{(8)}\Phi = \bar\Phi\{\gamma^{(8)}, M\}\Phi = \bar\Phi\big(-V\{\gamma^{(8)}, \gamma^{(4)}\} + 3H\{\gamma^{(8)}, \gamma^{(4)}\gamma^{(8)}\}\big)\Phi = 0,
$$

because $\{\gamma^{(8)}, \gamma^{(4)}\} = 2\eta^{84} = 0$ and $\{\gamma^{(8)}, \gamma^{(4)}\gamma^{(8)}\} = \gamma^{(8)}\gamma^{(4)}\gamma^{(8)} + \gamma^{(4)}\gamma^{(8)}\gamma^{(8)} = -\gamma^{(4)} + \gamma^{(4)} = 0$. So $T^{x_4}{}_{x_8} = 0$, and $T^{x_8}{}_{x_4} = -\tan^2 z\,T^{x_4}{}_{x_8} = 0$ (PROVED; check `commuting_T_x4x8_homogeneous`). The other entries off the diagonal are not zero in general (Section 9.26).

**The equation of state.** For $S \neq 0$, divide the numerator and the denominator of $p/\rho$ by $mS/2$:

$$
w = \frac{p}{\rho} = \frac{\frac{\lambda}{2}S^2}{mS + \frac{\lambda}{2}S^2} = \frac{\lambda S/m}{2 + \lambda S/m} = \frac{x}{2 + x}, \qquad x = \frac{\lambda S}{m} .
$$

(The record writes it $w = \lambda S/(2m + \lambda S)$.) It depends on $m$, $\lambda$ and $S$ only through $x$, and the effective mass is $V = m + \lambda S = m(1 + x)$. Its special values, each by elementary algebra:

| $x = \lambda S/m$ | $w$ | why |
| --- | --- | --- |
| $x = 0$ ($\lambda = 0$) | $w = 0$ (like dust) | $p = 0$ |
| $x = 1$ | $w = 1/3$ (like radiation) | $1/(2 + 1)$ |
| $x = -1$ | $w = -1$ (like a cosmological constant) | $-1/(2 - 1)$; here $V = m(1 + x) = 0$ |
| $-2 < x < -1$ | $w < -1$ (called **phantom**) | $2 + x > 0$, and $x < -(2 + x)$ means $x < -1$ |
| $x = -2$ | not defined | $\rho = mS(1 + x/2) = 0$ |
| $x < -2$ (with $m > 0$, $S > 0$) | $w > 1$ | $\rho < 0$ and $p < 0$; $x/(2 + x) > 1$ means $x < 2 + x$ after multiplying by the negative $2 + x$ |
| $x \to \pm\infty$ | $w \to 1$ | $x/(2 + x) = 1/(1 + 2/x)$ |

**What these numbers are, and what they are not.** They are the ratios $p/\rho$ of the eight-dimensional tensor of exact solutions, constant in time (COMPUTED in Notebook 09b on twelve exact solutions; the formula is PROVED in the record). They are not the equation of state that an observer in 3-space would infer: that observer sees neither the extra times nor the hidden direction as space, and to relate the two one must integrate over $x_5, x_6, x_7, x_8$ and follow the deflation. The Revision record contains no such computation, so the observer's $w$, its time dependence and any comparison with the supernova values are OPEN. In particular, the phantom range $w < -1$ of this table is not a claim about dark energy: the commuting field has negative energies (Section 9.21), and any use of them for a phantom equation of state is a HYPOTHESIS to be examined, not a result.

### 9.20 Where condensates oscillate and where they grow

With $V = m(1 + x)$ the number $k^2 = 9H^2 - V^2 = 9H^2 - m^2(1 + x)^2$ is positive exactly when $|1 + x| < 3H/|m|$. In the plane of the two pure numbers $x$ and $3H/|m|$ the growing condensates fill the wedge between the lines $3H/|m| = |1 + x|$; outside it they oscillate. The equation of state depends on $x$ alone, so every line of constant $w$ is vertical in this plane. At $x = -1$ ($w = -1$) the effective mass vanishes, $k^2 = 9H^2 > 0$, and the condensate grows like $e^{3Hx_4}$: every condensate with $w = -1$ grows (for $H > 0$).

The two condensates of Notebook 09b have $m = 1$, $H = 0.25$ (so $3H = 0.75$) and $S_0 = 1$:

- $\lambda = 0.5$: $V = 1.5 > 0.75$, $k^2 = 0.5625 - 2.25 = -1.6875$; it oscillates with $\omega = \sqrt{1.6875} = 1.299$, that is with the period $2\pi/\omega = 4.84$;
- $\lambda = -0.5$: $V = 0.5 < 0.75$, $k^2 = 0.5625 - 0.25 = 0.3125$, $k = 0.559$; it grows: for large $x_4$ its size $\Phi^\dagger\Phi$ grows like $e^{2kx_4}$, and the exponential factor alone reaches $e^{2 \cdot 0.559 \cdot 12} \approx 7 \cdot 10^5$ at $x_4 = 12$ (Figure 09b.2 shows a growth by more than a factor 100000).

In both cases $S$ stays exactly at 1. A growing $\Phi$ with a constant $S = \Phi^\dagger C\Phi$ is possible because $C$ has eight eigenvalues $+1$ and eight $-1$: the growth happens along directions in which the indefinite form $\Phi^\dagger C\Phi$ does not grow. Whether growing condensates are acceptable physically is the question of well-posedness and boundary conditions discussed in Chapter 8; this chapter only computes their tensor.

### 9.21 The energy of the commuting field has no lower bound

**$S$ has no sign.** $C$ is real and symmetric with $C^2 = 1$, so its eigenvalues are $+1$ or $-1$; the record writes $C = \mathrm{diag}(-\sigma, \sigma)$ (the block $-\sigma$ in the upper left corner, $\sigma$ in the lower right, zeros elsewhere) with a real symmetric $8 \times 8$ matrix $\sigma$ that obeys $\sigma^2 = 1$ and has trace 0. The eigenvalues of $\sigma$ are therefore $+1$ or $-1$ (if $\sigma v = \mu v$ then $v = \sigma^2v = \mu^2v$, so $\mu^2 = 1$), and because the trace of a symmetric matrix is the sum of its eigenvalues, trace 0 means four eigenvalues $+1$ and four $-1$. The block $-\sigma$ has the same eigenvalues with the signs exchanged, again four of each. So $C$ has eight eigenvalues $+1$ and eight $-1$ (PROVED; see the table at the end of this section). For an eigenvector $\chi$ with eigenvalue $-1$, $S_0 = \chi^\dagger C\chi = -\chi^\dagger\chi < 0$. A condensate with $\lambda = 0$ has $\rho = mS_0$: for $m > 0$ its energy density is negative whenever $S_0 < 0$.

**Plane waves of positive frequency with negative energy.** Take flat 4+4 space (all $f_a = 1$, no spin connection), $U = 0$, and a **plane wave** $\Phi = u\,e^{i(k_1x_1 + k_2x_2 + k_3x_3 + k_8x_8 - Ex_4)}$ with a constant column $u$, no dependence on the extra times, and a positive frequency $E$. Then $\partial_a\Phi = ik_a\Phi$ for $a = 1, 2, 3, 8$, $\partial_4\Phi = -iE\Phi$, and $\partial_a\bar\Phi = -ik_a\bar\Phi$ (complex conjugation turns $i$ into $-i$). Line by line:

$$
\begin{aligned}
K_a &= \tfrac12\big(\bar\Phi\gamma^{(a)}(ik_a\Phi) - (-ik_a\bar\Phi)\gamma^{(a)}\Phi\big) = ik_a\,\bar\Phi\gamma^{(a)}\Phi \qquad (a = 1, 2, 3, 8), \\
\rho &= -\sum_{a \neq x_4}K_a + mS = \bar\Phi\Big(m - i\sum_a k_a\gamma^{(a)}\Big)\Phi, \\
mu &= -iE\gamma^{(4)}u + i\sum_a k_a\gamma^{(a)}u \quad\Longrightarrow\quad \Big(m - i\sum_a k_a\gamma^{(a)}\Big)\Phi = -iE\gamma^{(4)}\Phi, \\
\rho &= \bar\Phi\big(-iE\gamma^{(4)}\big)\Phi = E\,\Phi^\dagger\big(-iC\gamma^{(4)}\big)\Phi = E\,\Phi^\dagger B\Phi = E\,u^\dagger Bu .
\end{aligned}
$$

The first line inserts the derivatives into $K_a$ (the two terms are equal); the second inserts $K_a$ into $\rho$ (Section 9.7, with $U = 0$; the extra-time terms are zero); the third is the flat field equation $\sum_a\gamma^{(a)}\partial_a\Phi = m\Phi$ for the plane wave, rearranged; the fourth inserts it, writes $\bar\Phi = \Phi^\dagger C$, uses the matrix $B = -iC\gamma^{(4)}$ of Chapter 5, and the fact that the exponential factor has size 1. $B$ is Hermitian with $B^2 = 1$, with eight eigenvalues $+1$ and eight $-1$. The field equation multiplied by $-i\gamma^{(4)}$ reads $Eu = hu$ with the matrix $h = m\beta + \sum_a k_a\alpha^a$, $\beta = -i\gamma^{(4)}$, $\alpha^a = -\gamma^{(4)}\gamma^{(a)}$; for $m = 2$ and $(k_1, k_2, k_3, k_8) = (1, 2, 0, 4)$, $h^2 = (4 + 1 + 4 + 0 + 16)\cdot 1 = 25$, so $E = \pm 5$. The record proves that $h$ commutes with $B$ and that on the 8-dimensional space of solutions with $E = 5$ the form $u^\dagger Bu$ has four positive and four negative directions (**Krein inertia** (4,4)): there are unit columns $u$ with $Bu = -u$, whose waves have $\rho = -5$, and with $Bu = +u$, whose waves have $\rho = +5$ (PROVED; the table lists the checks). Multiplying such a wave by a large constant makes $\rho$ as negative as we like: the classical energy of dirac16complex00 has no lower bound, already for $U = 0$.

| statement | Revision report | check |
| --- | --- | --- |
| $h$ commutes with $B$; waves with $\rho = -5$ and $\rho = +5$ at $E = 5$ | `Revision/theory/reports/python-scope.json` and `wolfram-scope.json` | `commuting_field_energy_unbounded_below` |
| every space of solutions of one real frequency has Krein inertia (4,4) | `Revision/pairing/reports/python-pairing.json` | `Q.one_particle_Krein_inertia_proof` |
| $C$ has eight eigenvalues $+1$ and eight $-1$ | `Revision/algebra/reports/python-algebra.json` and `wolfram-algebra.json` | `C_equals_notebook_sigma16`, `sigma8_involution` |

This is the classical form of the **spin-statistics** problem of a commuting field with a first-order Lagrangian. The **spin-statistics rule** of ordinary four-dimensional quantum field theory says that particles of half-integer **spin** (the spin is the intrinsic angular momentum of a particle, measured in units of Planck's constant divided by $2\pi$; the electron has spin $\frac12$), which are the fermions of Chapter 7, must be described by anticommuting fields; described by commuting fields, as dirac16complex00 is, the energy of a spinor field has no lower bound, and this is exactly what the plane waves above show. (The rule is a theorem of ordinary four-dimensional physics; this book does not prove it, and for 4+4 dimensions it claims only the statements of this section.) It must be remembered in every reading of the author's Hypothesis00 (for example a phantom equation of state), and it is why the anticommuting, quantised field dirac16complex is treated separately (Chapter 10). In Part V the chirality map $\Gamma$ sends every solution with parameters $(m, \lambda)$ to a solution with $(-m, -\lambda)$ and reverses the sign of the energy-momentum tensor (theorem T1; PROVED, `Revision/pairing/reports/python-pairing.json`, checks `T1.metric.commuting.euler_lagrange_map` and `T1.metric.commuting.emt`; Chapter 18 gives the proof). That theorem is an exact map between sets of solutions: it does not prove that any universe is created, in pairs or otherwise, and it gives no creation process, rate or amplitude.

### 9.22 Example: condensates

The second worked example builds the exact condensates of Section 9.18 and measures their energy-momentum tensor. It first shows with 20000 random columns that $S_0 = \chi^\dagger C\chi$ takes both signs; checks $M^2 = k^2$ and $M^TC + CM = 0$ for 18 pairs $(V, H)$; builds one oscillating ($\lambda = 0.5$) and one growing ($\lambda = -0.5$) condensate with $m = 1$, $H = 0.25$ and $S_0 = 1$ and checks the field equation and the constancy of $S$ at 401 times; computes from the solutions $K_4$, $\rho$, $p$ and $B_{84}$ and checks the values of Section 9.19; measures $w = p/\rho$ on twelve exact solutions and compares it with $x/(2 + x)$; draws the map of Section 9.20; confirms that a condensate keeps its energy density along the deflating history and, as an ILLUSTRATION only, solves the energy exchange of toy fluids with the Runge-Kutta method; and reproduces the negative energies of Section 9.21. It draws seven figures.

<!-- NOTEBOOK 09b -->

### 9.25 Line-by-line walk-through of Notebook 09b

The notebook has 20 code cells, In [1] to In [20]. As in Section 9.17, long figure captions are shortened to a line "...)" and docstrings are left out here; the captions are printed in full in Section 9.24.

**In [1], the set-up cell.** It is word for word the set-up cell of Notebook 09a, explained line by line in Section 9.17, with two differences: its comment lines are the run instructions of Notebook 09b (Section 9.23), and its line `NOTEBOOK_ID = "09b"` names this notebook, so the figures are saved as `09b_<k>_<name>.png` and their captions in `09b.captions.json`. It prints `Set-up of notebook 09b complete: repository folder found, helpers defined.`

**In [2], the matrices C and B, and the sign of S.**

```python
import numpy as np  # arrays of numbers, matrices, linear algebra

fixture = json.loads(
    repository_file("Revision/algebra/gammas.json").read_text(encoding="utf-8"))
gamma = [np.array(rows, dtype=float) for rows in fixture["gamma"]]  # x1, ..., x8
C = np.array(fixture["C"], dtype=float)  # gamma^(x8) gamma^(x1) gamma^(x2) gamma^(x3)
B = (np.array(fixture["B"]["re"], dtype=float)  # B = -i C gamma^(x4), stored as its
     + 1j * np.array(fixture["B"]["im"], dtype=float))  # real and imaginary parts
I16 = np.eye(16)  # the 16 x 16 unit matrix
g4, g8 = gamma[3], gamma[7]  # gamma^(x4) and gamma^(x8)
```

As in Notebook 09a, the fixture gives the eight real gammas (`gamma[0]` is $\gamma^{(1)}$, ..., `gamma[7]` is $\gamma^{(8)}$) and $C$. The matrix $B = -iC\gamma^{(4)}$ is complex; JSON has no complex numbers, so the fixture stores its real part and its imaginary part separately, and the cell adds them as `re + 1j * im`. The last line gives $\gamma^{(4)}$ and $\gamma^{(8)}$ the short names `g4` and `g8` (two names assigned at once from two values).

```python
def recorded(path, name):
    """The verdict (PASS or FAIL) of the check name in the Revision report path."""
    report_data = json.loads(repository_file(path).read_text(encoding="utf-8"))
    for item in report_data["checks"]:
        if item["name"] == name:
            return item["verdict"].upper()  # some reports write "pass"
    raise KeyError(f"{path} has no check {name}")
```

The same helper as in Notebook 09a: the verdict of one check of a Revision report.

```python
ALGEBRA_PY = "Revision/algebra/reports/python-algebra.json"
ALGEBRA_WL = "Revision/algebra/reports/wolfram-algebra.json"
eigenvalues_C = np.linalg.eigvalsh(C)  # C is symmetric: eigvalsh, sorted ascending
check(np.allclose(eigenvalues_C, [-1.0] * 8 + [1.0] * 8, atol=1e-12)
      and recorded(ALGEBRA_PY, "C_equals_notebook_sigma16") == "PASS"
      and recorded(ALGEBRA_WL, "sigma8_involution") == "PASS",
      "C has eight eigenvalues -1 and eight eigenvalues +1",
      record=f"{ALGEBRA_PY}, check C_equals_notebook_sigma16; {ALGEBRA_WL}, check "
             "sigma8_involution")
```

An **eigenvalue** of a matrix $M$ is a number $\mu$ for which $Mv = \mu v$ has a solution column $v \neq 0$ (an **eigenvector**). `np.linalg.eigvalsh` computes the eigenvalues of a symmetric (or Hermitian) matrix and returns them sorted from the smallest to the largest. The check compares them with eight $-1$ followed by eight $+1$ (the list `[-1.0] * 8 + [1.0] * 8`), with an absolute tolerance of $10^{-12}$: the fact of Section 9.21.

```python
rng = np.random.default_rng(2026)  # a fixed seed: the same numbers in every run
chis = rng.normal(size=(20000, 16)) + 1j * rng.normal(size=(20000, 16))
chis /= np.linalg.norm(chis, axis=1)[:, None]  # every row now has length 1
# S0 = chi^dagger C chi for every row at once (einsum sums over the indices i, j).
S0_values = np.einsum("ni,ij,nj->n", chis.conj(), C, chis).real
negative_share = float(np.mean(S0_values < 0))  # the fraction of negative S0
check(S0_values.min() < 0 < S0_values.max() and np.abs(S0_values).max() <= 1 + 1e-12,
      "S0 = chi^dagger C chi takes both signs and lies between -1 and 1")
report("fraction of the 20000 random chi with S0 < 0", f"{negative_share:.4f}")
```

`chis` is a table of 20000 random complex columns $\chi$, one per row. `np.linalg.norm(chis, axis=1)` computes the length of each row, and `/=` divides each row by its length (the `[:, None]` makes the 20000 lengths a column so that each row is divided by its own length): every $\chi$ now has length 1. `np.einsum("ni,ij,nj->n", ...)` is Einstein's summation written as a recipe: for every row $n$ it computes $\sum_{i,j}\chi^*_{ni}C_{ij}\chi_{nj} = \chi_n^\dagger C\chi_n$, all 20000 values of $S_0$ at once. `S0_values < 0` is an array of `True` and `False`, and its mean (`np.mean`, with `True` counted as 1) is the fraction of negative values. The check requires values of both signs (`a < 0 < b` means $a < 0$ and $0 < b$) and all values between $-1$ and $1$, as they must be for a unit column and eigenvalues $\pm 1$. It prints the fraction 0.4983: about half.

**In [3], the histogram of $S_0$ (Figure 09b.1).**

```python
fig, ax = plt.subplots()
ax.hist(S0_values, bins=60, range=(-1.0, 1.0), color="tab:blue", edgecolor="white")
ax.axvline(0.0, color="black", linewidth=1.0)
ax.set_xlabel("$S_0 = \\chi^\\dagger C \\chi$ for a random $\\chi$ of length 1")
ax.set_ylabel("number of the 20000 random $\\chi$")
ax.set_title("The scalar $S = \\bar\\Phi\\Phi$ has no sign")
save_figure(fig, "sign_of_s",
            "Histogram of $S_0 = \\chi^\\dagger C\\chi$ for 20000 random complex "
            ...)
```

A **histogram** is a bar chart that counts how many numbers fall into each of a row of equal intervals: `ax.hist` uses 60 intervals between $-1$ and $1$. `ax.axvline(0.0, ...)` draws a vertical line at zero. **What Figure 09b.1 shows.** The number of random unit columns (vertical axis) whose $S_0$ falls into each interval (horizontal axis, a pure number between $-1$ and $1$). The histogram is symmetric about zero, roughly a hill: about half of the values are negative. The student should see that $S$ has no sign; for a condensate with $\lambda = 0$, $\rho = mS_0$ has the sign of $S_0$.

**In [4], the matrix M and its square.**

```python
def condensate_matrix(V, H):
    """M = -V gamma^(x4) + 3 H gamma^(x4) gamma^(x8) and k^2 = 9 H^2 - V^2."""
    return -V * g4 + 3 * H * g4 @ g8, 9 * H ** 2 - V ** 2
```

The function returns two results, the matrix $M$ of Section 9.18 and the number $k^2 = 9H^2 - V^2$.

```python
THEORY_WL = "Revision/theory/reports/wolfram-field-theory.json"
THEORY_PY = "Revision/theory/reports/python-field-theory.json"
worst_square, worst_c = 0.0, 0.0  # the largest deviations found
for V_test in (-2.0, -0.5, 0.0, 0.75, 1.5, 3.0):
    for H_test in (0.1, 0.25, 1.0):
        M_test, k2_test = condensate_matrix(V_test, H_test)
        worst_square = max(worst_square, np.abs(M_test @ M_test - k2_test * I16).max())
        worst_c = max(worst_c, np.abs(M_test.T @ C + C @ M_test).max())
check(worst_square < 1e-12 and worst_c < 1e-12
      and recorded(THEORY_WL, "solution_matrix_square") == "PASS",
      "M^2 = (9 H^2 - V^2) times 1 and M^T C + C M = 0 for 18 pairs (V, H)",
      record=f"{THEORY_WL}, check solution_matrix_square")
```

For six values of $V$ and three of $H$ (18 pairs) the loops compute the largest entry of $M^2 - k^2\cdot 1$ and of $M^TC + CM$, and keep the largest over all pairs. The check confirms the two facts derived in Section 9.18 up to rounding.

**In [5], one column $\chi$ with $S_0 = 1$, and the solution formula.**

```python
m, H = 1.0, 0.25  # the mass and the author's constant
rng = np.random.default_rng(7)
while True:  # draw until S0 > 0 (the first draw usually succeeds)
    chi = rng.normal(size=16) + 1j * rng.normal(size=16)
    S0 = (chi.conj() @ C @ chi).real
    if S0 > 0:
        break
chi = chi / np.sqrt(S0)  # now chi^dagger C chi = 1
```

The cell fixes $m = 1$ and $H = 0.25$, starts a new random generator with the seed 7, and repeats (`while True:` loops until `break`) drawing a random column until its $S_0$ is positive. Dividing $\chi$ by $\sqrt{S_0}$ divides $S_0 = \chi^\dagger C\chi$ by $S_0$, so afterwards $S_0 = 1$.

```python
def condensate(x4, chi_value, M, k2):
    """Phi(x4) and dPhi/dx4 of the exact condensate with Phi(0) = chi_value."""
    if k2 == 0.0:  # cosh(k x4) -> 1 and sinh(k x4)/k -> x4 when k -> 0
        return chi_value + x4 * M @ chi_value, M @ chi_value
    k = np.sqrt(complex(k2))  # k is imaginary when k2 < 0
    phi = np.cosh(k * x4) * chi_value + np.sinh(k * x4) / k * (M @ chi_value)
    dphi = k * np.sinh(k * x4) * chi_value + np.cosh(k * x4) * (M @ chi_value)
    return phi, dphi
```

`condensate` returns $\Phi(x_4) = (\cosh(kx_4) + \frac{\sinh(kx_4)}{k}M)\chi$ and its derivative $\Phi'(x_4) = k\sinh(kx_4)\chi + \cosh(kx_4)M\chi$ (Section 9.18). The special case $k^2 = 0$ uses the limit $\Phi = \chi + x_4M\chi$. `complex(k2)` turns $k^2$ into a complex number, so that `np.sqrt` returns an imaginary $k$ when $k^2 < 0$ (for a real negative number it would fail); numpy computes $\cosh$ and $\sinh$ of complex arguments correctly.

```python
S0_now = (chi.conj() @ C @ chi).real  # 1 up to rounding
report("S0 = chi^dagger C chi after the division", f"{S0_now:.6f}")
```

The cell prints `1.000000`.

**In [6], two exact condensates and the field equation at 401 times.**

```python
times = np.linspace(0.0, 12.0, 401)  # the times x4 at which the solution is tested
EXAMPLES = {"oscillating": 0.5, "growing": -0.5}  # name -> lambda
solutions = {}  # name -> (Phi at every time, S at every time)
for name, lam in EXAMPLES.items():
    V = m + lam * 1.0  # S0 = 1
    M, k2 = condensate_matrix(V, H)
    phis, S_values, worst_residual = [], [], 0.0
```

The two examples are stored in a dictionary from their names to their $\lambda$; `.items()` gives the pairs. For each, $V = m + \lambda S_0$ with $S_0 = 1$, and $M$, $k^2$ follow. Three empty containers collect the values of $\Phi$, the values of $S$ and the largest residual.

```python
    for x4 in times:
        phi, dphi = condensate(x4, chi, M, k2)
        S_now = (phi.conj() @ C @ phi).real
        residual = g4 @ dphi + 3 * H * g8 @ phi - (m + lam * S_now) * phi
        # The residual relative to the size of the solution at this time.  Rounding
        # errors grow with the solution (S is a difference of large numbers when
        # Phi grows), so the tolerance below is 1e-9, not 1e-15.
        worst_residual = max(worst_residual,
                             np.abs(residual).max() / max(1.0, np.abs(phi).max()))
        phis.append(phi)
        S_values.append(S_now)
    solutions[name] = (np.array(phis), np.array(S_values))
```

At each of the 401 times the inner loop evaluates the solution, its $S$, and the **residual** of the field equation $\gamma^{(4)}\Phi' + 3H\gamma^{(8)}\Phi - (m + \lambda S)\Phi$, which must vanish; note that it uses $S$ computed at that time, so the test also covers the nonlinearity. The residual is divided by the size of the solution (at least 1), because rounding errors grow with a growing solution. The values are appended (`.append`) to the lists and finally stored in `solutions`.

```python
    report(f"{name}: lambda = {lam}, V = m + lambda S0", f"{V:.4f}")
    report(f"{name}: k^2 = 9 H^2 - V^2", f"{k2:.4f}")
    check(worst_residual < 1e-9,
          f"{name}: the field equation holds at 401 times")
    check(np.abs(np.array(S_values) - 1.0).max() < 1e-9,
          f"{name}: S stays equal to S0 = 1 at 401 times")
check(recorded(THEORY_WL, "exact_solution_nonlinear_homogeneous_C") == "PASS"
      and recorded(THEORY_PY, "exact_nonlinear_homogeneous_solution") == "PASS",
      "both condensates are the record's exact nonlinear homogeneous solution",
      record=f"{THEORY_WL}, check exact_solution_nonlinear_homogeneous_C; "
             f"{THEORY_PY}, check exact_nonlinear_homogeneous_solution")
```

For each example the cell prints $V$ and $k^2$ (oscillating: $V = 1.5$, $k^2 = -1.6875$; growing: $V = 0.5$, $k^2 = 0.3125$, the numbers of Section 9.20) and checks the field equation and the constancy of $S$ at all 401 times; after the loop, one more check confirms that the record proved these solutions exactly. Five PASS lines in all.

**In [7], the two condensates (Figure 09b.2).**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(9.6, 3.9))
phis, S_values = solutions["oscillating"]
for component in (0, 5, 10):  # three of the 16 components (rows 1, 6 and 11)
    left.plot(times, phis[:, component].real,
              label=f"Re $\\Phi_{{{component + 1}}}$")
left.plot(times, S_values, "k--", label="$S = \\bar\\Phi\\Phi$")
left.set_xlabel("time $x_4$")
left.set_ylabel("value")
left.set_ylim(-0.8, 1.35)  # room for the legend above the curves
left.set_title("Oscillating: $\\lambda = 0.5$, $V = 1.5$")
left.legend(fontsize=7, loc="upper center", ncol=4)
```

The left panel draws the real parts (`.real`) of the components 1, 6 and 11 of the oscillating condensate against the time, and $S$ as a black dashed line (the style string is the letter `k`, which means black, followed by two hyphens). In the f-string, a doubled brace prints a single brace, so the label of component 1 reads Re $\Phi_1$. The legend is placed at the top in four columns.

```python
phis, S_values = solutions["growing"]
right.plot(times, np.einsum("ti,ti->t", phis.conj(), phis).real,
           label="$\\Phi^\\dagger\\Phi$")
right.plot(times, S_values, "k--", label="$S = \\bar\\Phi\\Phi$")
right.set_yscale("log")
right.set_xlabel("time $x_4$")
right.set_title("Growing: $\\lambda = -0.5$, $V = 0.5$")
right.legend(fontsize=8)
save_figure(fig, "condensate_solutions",
            "Two exact condensates of dirac16complex00 with $m = 1$, $H = 0.25$ and "
            ...)
```

The right panel draws, for the growing condensate, the size $\Phi^\dagger\Phi = \sum_i|\Phi_i|^2$ at every time (the recipe `"ti,ti->t"` sums over the components `i` for each time `t`) and $S$, on a logarithmic axis. **What Figure 09b.2 shows.** Left: three components oscillate with the period $2\pi/\omega = 4.84$ while $S$ stays at 1. Right: $\Phi^\dagger\Phi$ rises, soon along a straight line on the logarithmic axis, like $e^{2kx_4}$ with $k = 0.559$, by more than a factor 100000, while $S$ stays exactly 1. The student should see that a constant $S$ does not mean a constant field: the indefinite form $\Phi^\dagger C\Phi$ can stay fixed while the field grows.

**In [8], the energy density and pressure of the condensates.**

```python
def homogeneous_tensor(phi, dphi, lam):
    """K4, rho, p and B84 of a condensate at one time."""
    S = (phi.conj() @ C @ phi).real
    U = lam / 2 * S ** 2
    K4 = 0.5 * (phi.conj() @ C @ g4 @ dphi - dphi.conj() @ C @ g4 @ phi)
    L0 = K4.real - m * S - U  # the other seven kinetic terms are zero
    B84 = phi.conj() @ C @ g8 @ dphi - dphi.conj() @ C @ g8 @ phi
    return S, U, K4, K4.real - L0, L0, B84  # rho = K4 - L0, p = L0
```

The function computes from $\Phi$ and $\Phi'$ at one time: $S$, $U$, the kinetic term $K_4 = \frac12(\bar\Phi\gamma^{(4)}\Phi' - \bar\Phi'\gamma^{(4)}\Phi)$ (with $f_4 = 1$; `phi.conj() @ C` is $\bar\Phi$), $L_0 = K_4 - mS - U$ (the other seven kinetic terms vanish), and $B_{84} = \bar\Phi\gamma^{(8)}\Phi' - \bar\Phi'\gamma^{(8)}\Phi$. It returns six values; the fourth is $\rho = -T^{x_4}{}_{x_4} = -(L_0 - K_4) = K_4 - L_0$ and the fifth is $p = T^\mu{}_\mu = L_0 - K_\mu = L_0$ for every $\mu \neq x_4$.

```python
values = {}  # name -> (rho, p) of the condensate
for name, lam in EXAMPLES.items():
    V = m + lam * 1.0
    M, k2 = condensate_matrix(V, H)
    rhos, ps, worst = [], [], 0.0
    for x4 in times:
        phi, dphi = condensate(x4, chi, M, k2)
        S, U, K4, rho, p, B84 = homogeneous_tensor(phi, dphi, lam)
        size = max(1.0, (phi.conj() @ phi).real)  # for relative tolerances
        worst = max(worst, abs(K4.imag) / size, abs(K4.real - V * S) / size,
                    abs(B84) / size)
        rhos.append(rho)
        ps.append(p)
    rhos, ps = np.array(rhos), np.array(ps)
    values[name] = (rhos.mean(), ps.mean())
```

For both condensates and all 401 times the loop evaluates the tensor and keeps the largest of three numbers that must vanish: the imaginary part of $K_4$, the difference $K_4 - VS$, and $B_{84}$, each relative to the size $\Phi^\dagger\Phi$ (at least 1). The energy densities and pressures are collected, and their means are stored.

```python
    check(worst < 1e-12, f"{name}: K4 is real, K4 = V S, and B84 = 0 (T^x4_x8 = 0)")
    check(np.abs(rhos - (m + lam / 2)).max() < 1e-9
          and np.abs(ps - lam / 2).max() < 1e-9,
          f"{name}: rho = m S + lambda S^2/2 and p = lambda S^2/2 at 401 times")
    check(abs(-values[name][0] + 7 * values[name][1] - (-m + 3 * lam)) < 1e-9,
          f"{name}: trace -rho + 7 p = -m S + 3 lambda S^2")
    report(f"{name}: rho", f"{values[name][0]:.6f}")
    report(f"{name}: p (all seven directions)", f"{values[name][1]:.6f}")
    report(f"{name}: w = p/rho", f"{values[name][1] / values[name][0]:.6f}")
```

Three checks per condensate: $K_4$ is real and equals $VS$ and $B_{84} = 0$ (so $T^{x_4}{}_{x_8} = 0$, Section 9.19); $\rho = m + \lambda/2$ and $p = \lambda/2$ at all 401 times (the values $mS + \frac{\lambda}{2}S^2$ and $\frac{\lambda}{2}S^2$ with $S = 1$); and the trace $-\rho + 7p = -mS + 3\lambda S^2$. The printed values are: oscillating, $\rho = 1.25$, $p = 0.25$, $w = 0.2$; growing, $\rho = 0.75$, $p = -0.25$, $w = -0.333333$. (By hand: $1 + 0.5/2 = 1.25$, $0.5/2 = 0.25$, $0.25/1.25 = 0.2$; $1 - 0.25 = 0.75$, $-0.25/0.75 = -1/3$.)

```python
check(recorded(THEORY_PY, "commuting_homogeneous_on_shell_rho_p") == "PASS"
      and recorded(THEORY_PY, "commuting_T_x4x8_homogeneous") == "PASS"
      and recorded(THEORY_PY, "commuting_trace_on_shell") == "PASS",
      "these are the record's homogeneous values and its vanishing x4-x8 component",
      record=f"{THEORY_PY}, checks commuting_homogeneous_on_shell_rho_p, "
             "commuting_T_x4x8_homogeneous and commuting_trace_on_shell")
```

The last check confirms that the record proved these statements exactly. Seven PASS lines in all.

**In [9], energy density and pressure against $S$ (Figure 09b.3).**

```python
lam = 0.5
S_axis = np.linspace(-6.0, 2.0, 401)
rho_axis = m * S_axis + lam / 2 * S_axis ** 2  # rho = m S + U
p_axis = lam / 2 * S_axis ** 2  # p = S U' - U
p_kin = (m + lam * S_axis) * S_axis  # V S
p_pot = -(m * S_axis + lam / 2 * S_axis ** 2)  # -(m S + U)
check(np.abs(p_kin + p_pot - p_axis).max() < 1e-12,
      "p = p_kin + p_pot = V S - (m S + U) at every drawn S")
```

With $m = 1$ and $\lambda = 0.5$ these lines tabulate, for 401 values of $S$ from $-6$ to 2, the energy density, the pressure and its two parts, and check that the parts add up to the pressure.

```python
fig, ax = plt.subplots()
ax.plot(S_axis, rho_axis, label="energy density $\\rho = mS + \\lambda S^2/2$")
ax.plot(S_axis, p_axis, label="pressure $p = \\lambda S^2/2$")
ax.plot(S_axis, p_kin, "--", label="kinetic part of $p$: $(m + \\lambda S)S$")
ax.plot(S_axis, p_pot, ":", label="potential part of $p$: $-(mS + U)$")
ax.plot([0.0, -2 * m / lam], [0.0, 0.0], "ko", label="$\\rho = 0$")
ax.axhline(0.0, color="black", linewidth=0.8)
ax.set_xlabel("$S = \\bar\\Phi\\Phi$")
ax.set_ylabel("energy per unit volume")
ax.set_title("Condensate: $\\rho$ and $p$ against $S$ ($m = 1$, $\\lambda = 0.5$)")
ax.legend(fontsize=8)
save_figure(fig, "energy_and_pressure",
            "Energy density $\\rho = mS + \\lambda S^2/2$ (solid), pressure "
            ...)
```

Four curves and two black dots (`"ko"`: black circles) at the zeros $S = 0$ and $S = -2m/\lambda = -4$ of $\rho$. **What Figure 09b.3 shows.** Against $S$ (horizontal, a pure number) in units of energy per unit volume: the energy density, a parabola through 0 and $-4$ with its lowest point $-1$ at $S = -2$; the pressure, a parabola that touches zero at $S = 0$; the kinetic part of the pressure (dashed) and its potential part (dotted). The student should see that the energy density is negative for $-4 < S < 0$ and that the pressure is the sum of a kinetic and a potential part that partly cancel.

**In [10], the equation of state of twelve exact condensates.**

```python
x_measured = np.array([-3.5, -3.0, -2.5, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0, 3.0,
                       4.0])  # values of x = lambda S/m (here lambda = x)
rho_measured, p_measured = [], []  # rho and p of each of the twelve condensates
for x_value in x_measured:
    V = m + x_value * 1.0  # lambda = x_value, S0 = 1
    M, k2 = condensate_matrix(V, H)
    phi, dphi = condensate(1.3, chi, M, k2)
    S, U, K4, rho, p, B84 = homogeneous_tensor(phi, dphi, x_value)
    rho_measured.append(rho)
    p_measured.append(p)
rho_measured, p_measured = np.array(rho_measured), np.array(p_measured)
w_measured = p_measured / rho_measured  # the equation of state of each condensate
w_formula = x_measured / (2 + x_measured)
```

With $m = 1$ and $S_0 = 1$ the number $x = \lambda S/m$ equals $\lambda$, so the cell builds, for twelve values of $x$, the exact condensate with $\lambda = x$, takes $\Phi$ and $\Phi'$ at the time $x_4 = 1.3$, and computes $\rho$ and $p$ from them as in In [8]; the formula $w = x/(2 + x)$ is used only afterwards, for the comparison. The value $x = -2$ is left out, because there $\rho = 0$.

```python
check(np.abs(w_measured - w_formula).max() < 1e-9,
      "w = p/rho of 12 exact condensates equals x/(2 + x), x = lambda S/m")
at_minus_one = w_measured[list(x_measured).index(-1.0)]
check(abs(at_minus_one + 1.0) < 1e-12,
      "w = -1 exactly where the effective mass m + lambda S vanishes (x = -1)")
below = x_measured < -2  # the three condensates with x < -2
check(np.all(rho_measured[below] < 0) and np.all(p_measured[below] < 0)
      and np.all(w_measured[below] > 1),
      "for x < -2: rho < 0, p < 0 and w > 1")
for x_value, w_value in zip(x_measured, w_measured):
    say(f"x = lambda S/m = {x_value:5.1f}:  w = p/rho = {w_value: .6f}")
```

Three checks: the twelve measured values agree with $x/(2 + x)$; the value at $x = -1$ (`list(...).index(-1.0)` finds its position) is $-1$; and the three condensates with $x < -2$ (`below` is an array of `True`/`False` that selects them) have negative $\rho$, negative $p$ and $w > 1$ (`np.all` is true when every selected value satisfies the condition). The loop prints the table: for example $x = -1.5$ gives $w = -3$, $x = 1$ gives $w = 1/3$, $x = -2.5$ gives $w = 5$. The format `{x_value:5.1f}` prints with one decimal in five places and `{w_value: .6f}` leaves a blank in place of a plus sign, so the columns line up.

**In [11], the equation of state against x (Figure 09b.4).**

```python
fig, ax = plt.subplots()
for piece in (np.linspace(-6.0, -2.05, 300), np.linspace(-1.95, 6.0, 500)):
    ax.plot(piece, piece / (2 + piece), color="tab:blue")  # two branches
ax.plot(x_measured, w_measured, "o", color="tab:red",
        label="measured on exact condensates")
ax.axvline(-2.0, color="gray", linestyle=":", label="$\\rho = 0$ ($x = -2$)")
ax.axhline(-1.0, color="tab:green", linestyle="--", label="$w = -1$")
ax.axhline(0.0, color="black", linewidth=0.8)
ax.axhspan(-6.0, -1.0, xmin=0.0, xmax=1.0, color="tab:green", alpha=0.08)
ax.set_ylim(-6.0, 6.0)
ax.set_xlabel("$x = \\lambda S / m$")
ax.set_ylabel("$w = p/\\rho$")
ax.set_title("Equation of state of a condensate: $w = x/(2 + x)$")
ax.legend(fontsize=8, loc="upper right")
save_figure(fig, "equation_of_state",
            "Equation of state $w = p/\\rho$ of a condensate of dirac16complex00 "
            ...)
```

The curve $w = x/(2 + x)$ is drawn in two pieces that stop short of $x = -2$, where it jumps from $+\infty$ to $-\infty$. The twelve measured values are red dots; a dotted vertical line marks $x = -2$, a dashed horizontal line $w = -1$, and `ax.axhspan` shades the band $w < -1$ faintly (`alpha=0.08` is 8 per cent opaque). **What Figure 09b.4 shows.** The equation of state (vertical) against $x$ (horizontal), both pure numbers. The red dots lie on the curve. The student should read off: $w = 0$ at $x = 0$; $w = -1$ at $x = -1$; the phantom band $w < -1$ for $-2 < x < -1$; $w > 1$ for $x < -2$, where $\rho$ and $p$ are both negative; and $w \to 1$ for large $x$. This is the eight-dimensional ratio, not the equation of state an observer in 3-space would infer (OPEN).

**In [12], where condensates oscillate and where they grow (Figure 09b.5).**

```python
x_grid = np.linspace(-4.0, 3.0, 701)  # x = lambda S/m
h_grid = np.linspace(0.0, 3.0, 301)  # h = 3 H/|m|
X, Hgrid = np.meshgrid(x_grid, h_grid)  # every pair (x, h) of the two grids
growing_region = (np.abs(1 + X) < Hgrid).astype(float)  # 1 where k^2 > 0
fig, ax = plt.subplots()
ax.contourf(X, Hgrid, growing_region, levels=[-0.5, 0.5, 1.5],
            colors=["#dbe9f6", "#f6d5d5"])
```

`np.meshgrid` makes two tables that together list every pair $(x, h)$ of the two grids, with $h = 3H/|m|$. The condition $|1 + x| < h$ of Section 9.20 is evaluated at every pair and turned into 1 (growing) or 0 (oscillating) by `.astype(float)`. `ax.contourf` colours the plane by these values: the levels $-0.5$, $0.5$, $1.5$ separate 0 from 1, and the two colours are a light blue and a light red, given as hexadecimal colour codes.

```python
for label, x_line in (("$w = -1$", -1.0), ("$w = 0$", 0.0), ("$w = 1/3$", 1.0)):
    ax.axvline(x_line, color="black", linestyle="--", linewidth=0.8)
    ax.text(x_line + 0.05, 2.8, label, fontsize=8)
for name, lam_value in EXAMPLES.items():
    ax.plot([lam_value * 1.0 / m], [3 * H / abs(m)], "ko")
    ax.text(lam_value / m + 0.08, 3 * H / abs(m) - 0.15, name, fontsize=8)
ax.text(-3.8, 0.3, "oscillating ($k^2 < 0$)", fontsize=9)
ax.text(-2.9, 2.3, "growing\n($k^2 > 0$)", fontsize=9)
ax.set_xlabel("$x = \\lambda S / m$")
ax.set_ylabel("$3H/|m|$")
ax.set_title("Condensates: oscillating (blue) or growing (red)")
ax.grid(False)
save_figure(fig, "regime_map",
            "Map of the condensates of dirac16complex00 in the plane of "
            ...)
```

The first loop draws the vertical lines of constant $w$ at $x = -1$, 0 and 1 with their labels; the second marks the two condensates of In [6] as black dots at $(x, 3H/|m|) = (0.5, 0.75)$ and $(-0.5, 0.75)$ with their names; two more labels name the regions (`\n` starts a new line). **What Figure 09b.5 shows.** The plane of $x$ (horizontal) and $3H/|m|$ (vertical), both pure numbers: a red wedge with its tip at $x = -1$ on the horizontal axis, opening upwards, where condensates grow, and the blue rest, where they oscillate. The student should see that the line $w = -1$ runs through the middle of the wedge: every condensate with $w = -1$ grows.

```python
for name, lam_value in EXAMPLES.items():
    grows = abs(1 + lam_value / m) < 3 * H / abs(m)
    check(grows == (name == "growing"),
          f"the {name} condensate lies in the {name} region of the map")
```

The two checks confirm that the map puts each condensate of In [6] into the region of its name.

**In [13], a condensate keeps its energy along the deflating history.**

```python
A = 1.0  # the deflating history a4 = A H x4
M, k2 = condensate_matrix(m + 0.5 * 1.0, H)  # the oscillating condensate, S0 = 1
# rho at every time; homogeneous_tensor returns (S, U, K4, rho, p, B84): index 3.
# The condensate does not contain a4, so these are its values on this history too.
rho_at_times = np.array([homogeneous_tensor(*condensate(x4, chi, M, k2), 0.5)[3]
                         for x4 in times])
check(np.abs(rho_at_times - rho_at_times[0]).max() < 1e-9,
      "the condensate has p3 = p_t, so its rho is constant along the history")
```

`A = 1` names the deflating history $a_4 = AHx_4$. The oscillating condensate does not contain $a_4$ (Section 9.18), so it is a solution on this history too. `condensate(...)` returns the pair $(\Phi, \Phi')$, and the star in `homogeneous_tensor(*condensate(...), 0.5)` hands the two over as the first two arguments; `[3]` picks the fourth result, $\rho$. The check confirms that $\rho$ is the same at all 401 times, as $p_3 = p_t$ and the identity of Section 9.10 require.

**In [14], toy fluids solved with the Runge-Kutta method (an ILLUSTRATION).**

```python
def rk4(rate, y0, step, count):
    """Solve dy/dx = rate(y) from y(0) = y0 with count Runge-Kutta steps."""
    y, path = y0, [y0]
    for _ in range(count):
        s1 = rate(y)
        s2 = rate(y + step / 2 * s1)
        s3 = rate(y + step / 2 * s2)
        s4 = rate(y + step * s3)
        y = y + step / 6 * (s1 + 2 * s2 + 2 * s3 + s4)
        path.append(y)
    return np.array(path)
```

The **Runge-Kutta method** of fourth order (RK4, Chapter 2) solves an equation $dy/dx = \text{rate}(y)$ step by step: from the value $y$ it evaluates four slopes (at the start, twice at the middle of the step, and at the end) and moves on by the step times their weighted mean $(s_1 + 2s_2 + 2s_3 + s_4)/6$. The function returns the whole path, the starting value included.

```python
STEP, COUNT = 0.05, 160  # x4 from 0 to 8
toy_times = STEP * np.arange(COUNT + 1)
DELTAS = (-2 / 3, -1 / 3, 0.0, 1 / 3, 2 / 3)  # Delta w = w3 - w_t
toy = {}  # Delta w -> rho(x4)/rho0 along A = +1
errors = {STEP: 0.0, STEP / 2: 0.0}  # the largest relative error for two steps
```

160 steps of 0.05 cover $x_4$ from 0 to 8; `toy_times` holds the 161 times. Five toy fluids are labelled by $\Delta w = w_3 - w_t$. `toy` will hold their paths, and `errors` the largest relative error for the step 0.05 and for half of it.

```python
for delta in DELTAS:
    for step in errors:
        count = round(8.0 / step)  # the number of steps from x4 = 0 to 8
        path = rk4(lambda r, d=delta: -3 * A * H * d * r, 1.0, step, count)
        exact = np.exp(-3 * A * H * delta * step * np.arange(count + 1))
        errors[step] = max(errors[step], np.abs(path / exact - 1).max())
        if step == STEP:
            toy[delta] = path
```

For each toy fluid and each of the two steps, the cell solves $d\rho/dx_4 = -3AH\,\Delta w\,\rho$ from $\rho(0) = 1$ (Section 9.10). `lambda r, d=delta: ...` is a short nameless function of `r`; the extra argument `d=delta` freezes the current value of `delta` inside it. `exact` is the exact solution $e^{-3AH\Delta w\,x_4}$ at the same times, and the largest relative error of the path is kept. The paths with the step 0.05 are stored for the figure.

```python
check(errors[STEP] < 1e-7,
      "RK4 (step 0.05) reproduces rho0 exp(-3 A H Delta w x4) for 5 toy fluids")
ratio = errors[STEP] / errors[STEP / 2]  # RK4: half the step, 1/16 of the error
check(14 < ratio < 18, "halving the RK4 step divides the error by about 2^4 = 16")
report("largest relative RK4 error, step 0.05", f"{errors[STEP]:.2e}")
report("error ratio of the steps 0.05 and 0.025", f"{ratio:.2f}")
```

The first check requires the error with the step 0.05 to be below $10^{-7}$ (it is $1.33 \cdot 10^{-8}$). The error of a fourth-order method is proportional to the fourth power of the step, so halving the step must divide it by about $2^4 = 16$; the measured ratio is 16.17, and the second check accepts 14 to 18.

```python
reversed_path = rk4(lambda r: -3 * (-A) * H * (1 / 3) * r, 1.0, STEP, COUNT)
check(np.abs(reversed_path * toy[1 / 3] - 1).max() < 1e-8,
      "A -> -A reverses the energy flow (the product of the two paths is 1)")
report("toy fluid Delta w = 1/3: rho(8)/rho(0) along A = 1", f"{toy[1 / 3][-1]:.6f}")
```

The reversed history ($A \to -A$: the extra times inflate and 3-space deflates) gives the path $e^{+3AH\Delta w\,x_4}$, the inverse of the original: the check requires their product to be 1 at every time. The cell prints $\rho(8)/\rho(0) = 0.135335 = e^{-2}$ for $\Delta w = 1/3$, the number computed by hand in Section 9.10. (`toy[1 / 3][-1]` is the last value of the path; the index $-1$ counts from the end.)

**In [15], the energy exchange (Figure 09b.6).**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(9.6, 3.9))
fig.subplots_adjust(wspace=0.35)  # more room between the two panels
for delta in DELTAS:
    left.plot(toy_times, toy[delta], label=f"toy, $\\Delta w = {delta:+.2f}$")
left.plot(times[times <= 8.0], rho_at_times[times <= 8.0] / rho_at_times[0], "k:",
          linewidth=2.0, label="condensate ($p_3 = p_t$)")
left.set_yscale("log")
left.set_xlabel("time $x_4$")
left.set_ylabel("$\\rho(x_4) / \\rho(0)$")
left.set_title("Energy density along $a_4 = AHx_4$ ($A = 1$)")
left.legend(fontsize=7)
```

The left panel draws the five toy paths (the format `+.2f` prints the sign and two decimals) and, as a thick black dotted line, the condensate's $\rho(x_4)/\rho(0)$ for the times up to 8 (`times <= 8.0` selects them), on a logarithmic axis.

```python
rho_toy = toy[-1 / 3]  # Delta w = -1/3: w3 = 1/3, w_t = 2/3
work_space = -3 * A * H * (1 / 3) * rho_toy  # -3 a4' p3 with p3 = rho/3
work_extra = 3 * A * H * (2 / 3) * rho_toy  # +3 a4' p_t with p_t = 2 rho/3
right.plot(toy_times, work_space, label="3-space: $-3a_4' p_3$")
right.plot(toy_times, work_extra, "--", label="extra times: $+3a_4' p_t$")
right.plot(toy_times, np.gradient(rho_toy, toy_times), ":", color="black",
           label="$d\\rho/dx_4$ (finite differences)")
right.axhline(0.0, color="black", linewidth=0.8)
right.set_xlabel("time $x_4$")
right.set_ylabel("rate of change of $\\rho$")
right.set_title("Toy fluid $(w_3, w_t) = (1/3, 2/3)$")
right.legend(fontsize=7)
save_figure(fig, "energy_exchange",
            "Energy exchange along the deflating history $a_4 = AHx_4$, $A = 1$, "
            ...)
```

For the toy fluid with $w_3 = 1/3$ and $w_t = 2/3$ the right panel draws the two terms of $d\rho/dx_4 = -3a_4'p_3 + 3a_4'p_t$ separately, and the slope of the path by finite differences. **What Figure 09b.6 shows.** Left, the energy density divided by its starting value (a pure number, logarithmic axis) against $x_4$ from 0 to 8: the toy fluids with $p_3 > p_t$ ($\Delta w > 0$) lose energy, those with $p_3 < p_t$ gain energy, $\Delta w = 0$ and the exact condensate stay constant. Right, rates in units of energy per unit volume per unit time: the 3-space term is negative (inflating 3-space takes energy out), the extra-time term is positive and twice as large (the deflating extra times put energy in), and the dotted slope is their sum. The student should see the energy exchange of Section 9.10 at work, remembering that the toy fluids are an illustration, not solutions.

```python
# [2:-2] leaves out two points at each end, where np.gradient is less exact.
check(np.abs(np.gradient(rho_toy, toy_times) - (work_space + work_extra))[2:-2].max()
      < 1e-3, "d rho/dx4 equals the sum of the two work terms on the drawn path")
```

The check confirms that the finite-difference slope equals the sum of the two terms within $10^{-3}$.

**In [16], negative energies: the plane waves of flat space.**

```python
m_flat, E_flat = 2.0, 5.0
momentum = {0: 1.0, 1: 2.0, 2: 0.0, 7: 4.0}  # k1, k2, k3, k8 (x5, x6, x7: zero)
beta = -1j * g4
h = m_flat * beta + sum(k_a * (-g4 @ gamma[a]) for a, k_a in momentum.items())
check(np.abs(h - h.conj().T).max() < 1e-12 and np.abs(h @ h - 25 * I16).max() < 1e-12
      and np.abs(B @ h - h @ B).max() < 1e-12,
      "h is Hermitian, h^2 = 25, and h commutes with B")
```

The cell sets up the example of Section 9.21: $m = 2$, the momenta $(k_1, k_2, k_3, k_8) = (1, 2, 0, 4)$ stored in a dictionary from the index of the direction to its momentum, $\beta = -i\gamma^{(4)}$ and $h = m\beta + \sum_a k_a\alpha^a$ with $\alpha^a = -\gamma^{(4)}\gamma^{(a)}$. The check confirms that $h$ is **Hermitian** (equal to its own dagger, `h.conj().T`), that $h^2 = 25$ and that $hB = Bh$.

```python
energies, vectors = np.linalg.eigh(h)  # eigenvalues in ascending order
U5 = vectors[:, energies > 0]  # the eight columns with eigenvalue +5
form = U5.conj().T @ B @ U5  # u^dagger B u on the eigenspace, as an 8 x 8 matrix
inertia, directions = np.linalg.eigh(form)
```

`np.linalg.eigh` returns the eigenvalues of a Hermitian matrix in ascending order and, as the columns of a second matrix, unit eigenvectors that are perpendicular to each other. `energies > 0` selects the eight columns with $E = +5$: `U5` is a $16 \times 8$ matrix whose columns span the space of solutions with $E = 5$. Every unit column of that space is $u = U_5c$ with a unit column $c$ of eight numbers, and then $u^\dagger Bu = c^\dagger(U_5^\dagger BU_5)c$: the $8 \times 8$ matrix `form` describes the form $u^\dagger Bu$ on the space. Its eigenvalues `inertia` and unit eigenvectors `directions` give its positive and negative directions.

```python
PAIRING = "Revision/pairing/reports/python-pairing.json"
check(np.allclose(energies, [-5.0] * 8 + [5.0] * 8, atol=1e-12)
      and np.allclose(inertia, [-1.0] * 4 + [1.0] * 4, atol=1e-12)
      and recorded(PAIRING, "Q.one_particle_Krein_inertia_proof") == "PASS",
      "E = +-5 (eight each); u^dagger B u has inertia (4,4) on the E = 5 space",
      record=f"{PAIRING}, check Q.one_particle_Krein_inertia_proof (every real "
             "frequency)")
```

The check confirms the frequencies $\pm 5$, eight each, and that the form has four eigenvalues $-1$ and four $+1$: Krein inertia (4,4), which the pairing record proves for every real frequency.

**In [17], the energy density of two plane waves.**

```python
def flat_energy_density(u):
    """rho = -sum over a != x4 of K_a + m S for the plane wave u e^(i(k.x - E x4))."""
    S = (u.conj() @ C @ u).real
    kinetic = 0.0
    for a, k_a in momentum.items():  # d_a Phi = i k_a Phi
        d_u = 1j * k_a * u
        kinetic += 0.5 * (u.conj() @ C @ gamma[a] @ d_u - d_u.conj() @ C @ gamma[a] @ u)
    return (-kinetic + m_flat * S).real
```

The function computes $\rho = -\sum_{a \neq x_4}K_a + mS$ from its definition (Section 9.7, flat space, $U = 0$), with $\partial_a\Phi = ik_a\Phi$; the common exponential factor has size 1 and drops out of every bilinear, so the column $u$ can stand for $\Phi$.

```python
rho_pair = []
# column 0 of directions has the eigenvalue -1 of the form, column 7 the value +1
for column, b_value in ((0, -1.0), (7, 1.0)):
    u = U5 @ directions[:, column]  # a unit vector of the eigenspace, B u = b_value u
    d4_u = -1j * E_flat * u  # d4 Phi = -i E Phi
    field = (g4 @ d4_u + sum(gamma[a] @ (1j * k_a * u) for a, k_a in momentum.items())
             - m_flat * u)  # sum_a gamma^(a) d_a Phi - m Phi
    check(np.abs(field).max() < 1e-12 and np.abs(B @ u - b_value * u).max() < 1e-12,
          f"the plane wave with B u = {b_value:+.0f} u solves the field equation")
    rho_pair.append(flat_energy_density(u))
```

For the two extreme directions of the form (the first eigenvector, eigenvalue $-1$, and the last, eigenvalue $+1$) the loop builds the unit column $u$ of the solution space, checks that the plane wave solves the flat field equation $\sum_a\gamma^{(a)}\partial_a\Phi = m\Phi$ and that $Bu = \mp u$, and computes its energy density.

```python
SCOPE_PY = "Revision/theory/reports/python-scope.json"
SCOPE_WL = "Revision/theory/reports/wolfram-scope.json"
check(abs(rho_pair[0] + 5.0) < 1e-12 and abs(rho_pair[1] - 5.0) < 1e-12
      and recorded(SCOPE_PY, "commuting_field_energy_unbounded_below") == "PASS"
      and recorded(SCOPE_WL, "commuting_field_energy_unbounded_below") == "PASS",
      "rho = -5 for B u = -u and rho = +5 for B u = +u (|u| = 1)",
      record=f"{SCOPE_PY} and {SCOPE_WL}, check commuting_field_energy_unbounded_below")
```

The check confirms the record's values: the wave with $Bu = -u$ has $\rho = -5$, the wave with $Bu = +u$ has $\rho = +5$, both at the positive frequency $E = 5$, in agreement with $\rho = E\,u^\dagger Bu$ of Section 9.21.

**In [18], 5000 random waves of positive frequency.**

```python
samples = rng.normal(size=(5000, 8)) + 1j * rng.normal(size=(5000, 8))
samples /= np.linalg.norm(samples, axis=1)[:, None]
us = samples @ U5.T  # 5000 random unit vectors of the eigenspace
charges = np.einsum("ni,ij,nj->n", us.conj(), B, us).real  # u^dagger B u
rho_samples = np.array([flat_energy_density(u) for u in us])
check(np.abs(rho_samples - E_flat * charges).max() < 1e-12
      and rho_samples.min() < 0 < rho_samples.max(),
      "rho = E u^dagger B u for all 5000 random u of the eigenspace; both signs")
report("smallest and largest rho of the 5000 samples",
       f"{rho_samples.min():.4f} and {rho_samples.max():.4f}")
```

5000 random unit columns $c$ of eight numbers give 5000 random unit columns $u = U_5c$ of the solution space (`samples @ U5.T` computes all of them at once, one per row). For each, `charges` holds $u^\dagger Bu$ and `rho_samples` the energy density computed from the kinetic terms. The check confirms $\rho = E\,u^\dagger Bu$ every time and that both signs occur. The smallest and largest values are $-4.3821$ and $4.4892$.

**In [19], the histogram of the 5000 energy densities (Figure 09b.7).**

```python
fig, ax = plt.subplots()
ax.hist(rho_samples, bins=50, range=(-5.0, 5.0), color="tab:purple", edgecolor="white")
ax.axvline(0.0, color="black", linewidth=1.0)
ax.set_xlabel("energy density $\\rho = E\\,u^\\dagger B u$ of the plane wave")
ax.set_ylabel("number of the 5000 random $u$")
ax.set_title("Waves of positive frequency $E = 5$: $\\rho$ has both signs")
save_figure(fig, "energy_sign",
            "Histogram of the energy density $\\rho = -\\sum_{a \\neq x_4} K_a + mS$ "
            ...)
```

**What Figure 09b.7 shows.** The number of waves (vertical) whose energy density, in units of energy per unit volume, falls into each of 50 intervals between $-5$ and 5 (horizontal). The values are spread symmetrically about zero, and about half are negative. The possible values fill the whole interval from $-5$ (reached for $Bu = -u$) to 5 (for $Bu = u$), but random columns seldom come near the two ends. The student should see that for this commuting field a positive frequency does not mean a positive energy.

**In [20], the last check.**

```python
captions = json.loads(output_file(CAPTION_FILE).read_text(encoding="utf-8"))
expected_files = ["09b_1_sign_of_s.png", "09b_2_condensate_solutions.png",
                  "09b_3_energy_and_pressure.png", "09b_4_equation_of_state.png",
                  "09b_5_regime_map.png", "09b_6_energy_exchange.png",
                  "09b_7_energy_sign.png"]
check(sorted(captions) == expected_files and all(
    output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in expected_files),
    "the seven figures of this notebook are saved and captioned")
all_checks_passed()
```

As in Notebook 09a: the seven figures exist and are captioned, and the last line is `ALL 33 CHECKS PASSED (notebook 09b)`: two checks in In [2], one in In [4], five in In [6], seven in In [8], one in In [9], three in In [10], two in In [12], one in In [13], three in In [14], one in In [15], two in In [16], three in In [17], one in In [18] and one in In [20].

### 9.26 The full tensor of a condensate

A condensate has the same pressure in all seven directions. That does not yet make it a **perfect fluid at rest**, which has a diagonal energy-momentum tensor: Section 9.12 showed that the spin connection puts entries off the diagonal. For a condensate $\partial_\mu\Phi = 0$ for $\mu \neq x_4$, but $D_\mu\Phi = \Omega_\mu\Phi$ is not zero along 3-space and the extra times, because $\Omega_{x_i}$ and $\Omega_{x_t}$ are not zero.

**The structure, from the record.** Off the diagonal the tensor of Section 9.6 is $T^\nu{}_\mu = -K^{(\nu}{}_{\mu)}$ with

$$
K^\nu{}_\mu = \tfrac12\big(\bar\Phi\gamma^\nu D_\mu\Phi - D_\mu\bar\Phi\,\gamma^\nu\Phi\big), \qquad K^{(\nu}{}_{\mu)} = \tfrac12\big(K^\nu{}_\mu + g^{\nu\nu}g_{\mu\mu}K^\mu{}_\nu\big),
$$

because the first pair of terms in the bracket of Section 9.6 is $2K^\nu{}_\mu$ and the second pair is $g_{\mu\mu}g^{\nu\nu}\cdot 2K^\mu{}_\nu$ (move the metric factors of $\gamma_\mu$ and $D^\nu$ in front). The Revision record proves three facts for every exact condensate (PROVED; the table names the record files and checks; the coefficients themselves are stored in the record file `Revision/field_equations_a4/a4-equations.json` under the entry `offDiagonalKinetic`):

| statement | Revision report | check |
| --- | --- | --- |
| the diagonal of the tensor of a condensate | `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `condensate_kinetic_tensor_diagonal` |
| the same, with the author's gammas | `Revision/field_equations_a4/reports/python-a4-report.json` | `authorT16_condensate_kinetic_diagonal` |
| the entries off the diagonal are multiples of three-gamma bilinears | `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `condensate_offdiagonal_are_three_gamma_bilinears` |
| the same, with the author's gammas | `Revision/field_equations_a4/reports/python-a4-report.json` | `authorT16_condensate_offdiagonal_three_gamma` |
| the stored coefficients are the computed ones | `Revision/field_equations_a4/reports/python-a4-report.json` | `json_offdiagonal_coefficients` |

The three facts are:

- the diagonal is $T^{x_4}{}_{x_4} = -VS + L_0$ and $T^\mu{}_\mu = L_0$ otherwise (Section 9.19), and $T^{x_4}{}_{x_8} = T^{x_8}{}_{x_4} = 0$;
- exactly 42 of the 56 entries off the diagonal are nonzero in general: the 12 flows $T^{x_4}{}_{x_j}$ and $T^{x_j}{}_{x_4}$ ($x_j$ any of the six directions $x_1, x_2, x_3, x_5, x_6, x_7$), whose coefficients contain $H$ and not $a_4'$; the 18 entries $T^{x_i}{}_{x_t}$ and $T^{x_t}{}_{x_i}$ between 3-space and the extra times; and the 12 entries $T^{x_j}{}_{x_8}$ and $T^{x_8}{}_{x_j}$; the last 30 are proportional to $a_4'$ (the 14 entries inside 3-space, inside the extra times, and $x_4$-$x_8$ vanish);
- each nonzero entry is a fixed number (depending on $a_4$, $a_4'$, $z$ and $H$, not on $V$) times one of 15 **three-gamma bilinears** $B_{abc} = \bar\Phi\gamma^{(a)}\gamma^{(b)}\gamma^{(c)}\Phi$, with $\{a, b, c\} = \{j, 4, 8\}$ (six of them) or $\{i, 4, t\}$ with $i$ in 3-space and $t$ an extra time (nine of them).

**One entry, line by line.** Take $T^{x_1}{}_{x_5}$. Both $K^{x_1}{}_{x_5}$ and $K^{x_5}{}_{x_1}$ contain no derivative of $\Phi$ (there is none along $x_1$ or $x_5$), so, exactly as in Section 9.12, each is $\frac12\bar\Phi\{\gamma^\nu, \Omega_\mu\}\Phi$. With $\gamma^{x_1} = \gamma^{(1)}/f_1$, $\gamma^{x_5} = \gamma^{(5)}/f_5$ and the anticommutators of a gamma with a product of two other gammas, $\{\gamma^{(a)}, \gamma^{(b)}\gamma^{(c)}\} = 2\gamma^{(a)}\gamma^{(b)}\gamma^{(c)}$ (move $\gamma^{(a)}$ from the right end to the front past two gammas: two minus signs):

$$
\begin{aligned}
K^{x_1}{}_{x_5} &= \tfrac12\cdot\frac{1}{f_1}\cdot\Big(-\frac{f_5}{2}\Big)\,\bar\Phi\big(a_4'\{\gamma^{(1)}, \gamma^{(4)}\gamma^{(5)}\} + H\{\gamma^{(1)}, \gamma^{(5)}\gamma^{(8)}\}\big)\Phi \\
&= -\frac{f_5}{2f_1}\big(a_4'B_{145} + HB_{158}\big), \\
K^{x_5}{}_{x_1} &= \tfrac12\cdot\frac{1}{f_5}\cdot\frac{f_1}{2}\,\bar\Phi\big(a_4'\{\gamma^{(5)}, \gamma^{(1)}\gamma^{(4)}\} + H\{\gamma^{(5)}, \gamma^{(1)}\gamma^{(8)}\}\big)\Phi \\
&= \frac{f_1}{2f_5}\big(a_4'B_{145} - HB_{158}\big), \\
g^{11}g_{55}K^{x_5}{}_{x_1} &= \frac{1}{f_1^2}\big(-f_5^2\big)\frac{f_1}{2f_5}\big(a_4'B_{145} - HB_{158}\big) = -\frac{f_5}{2f_1}\big(a_4'B_{145} - HB_{158}\big), \\
T^{x_1}{}_{x_5} &= -\tfrac12\Big(K^{x_1}{}_{x_5} + g^{11}g_{55}K^{x_5}{}_{x_1}\Big) = \tfrac12\cdot\frac{f_5}{2f_1}\cdot 2a_4'B_{145} = \tfrac12\,e^{-2a_4}\,a_4'\;\bar\Phi\gamma^{(1)}\gamma^{(4)}\gamma^{(5)}\Phi .
\end{aligned}
$$

The first line inserts $\gamma^{x_1} = \gamma^{(1)}/f_1$ and $\Omega_{x_5}$; the second replaces each anticommutator by twice the product of its three gammas, which are already in the order $1, 4, 5$ and $1, 5, 8$, and cancels the factors 2 and $\frac12$. The third line inserts $\gamma^{x_5} = \gamma^{(5)}/f_5$ and $\Omega_{x_1}$; the fourth does the same and reorders the three gammas into the order $1, 4, 5$ and $1, 5, 8$ ($\gamma^{(5)}\gamma^{(1)}\gamma^{(4)} = \gamma^{(1)}\gamma^{(4)}\gamma^{(5)}$ after two exchanges; $\gamma^{(5)}\gamma^{(1)}\gamma^{(8)} = -\gamma^{(1)}\gamma^{(5)}\gamma^{(8)}$ after one). The fifth multiplies by $g^{11}g_{55} = (1/f_1^2)(-f_5^2)$; the sixth adds, so that the $H$ terms cancel and the $a_4'$ terms double, and uses $f_5/f_1 = e^{-2a_4}$. The entry is proportional to the deflation rate $a_4'$: it exists only because the extra times deflate (or, for $a_4' < 0$, inflate). The coefficient $\frac12e^{-2a_4}a_4'$ is exactly the record's (its table lists $K^{x_i}{}_{x_t}$ with the coefficient $-\frac12e^{-2a_4}a_4'$, and $T = -K$); at $a_4 = 0.5$, $a_4' = 0.25$ it is $0.5\cdot e^{-1}\cdot 0.25 = 0.045985$, the number Notebook 09c prints for $T^{x_1}{}_{x_5}$.

**A second entry: the momentum flow $T^{x_4}{}_{x_1}$.** Section 9.12 computed the piece $K^{x_4}{}_{x_1} = \frac12f_1H\,\bar\Phi\gamma^{(4)}\gamma^{(1)}\gamma^{(8)}\Phi$, with the coefficient $\frac12$. The record's coefficient of the whole entry is $\frac74$. The difference is the second piece of the symmetrised tensor, $g^{44}g_{11}K^{x_1}{}_{x_4}$, which contains the time derivative of the condensate. Line by line, with $\partial_4\Phi = M\Phi$ and $\partial_4\bar\Phi = -\bar\Phi M$ (Section 9.19) and $\Omega_{x_4} = 0$, so that $D_{x_4} = \partial_4$:

$$
\begin{aligned}
K^{x_4}{}_{x_1} &= \tfrac12 f_1H\,\bar\Phi\gamma^{(4)}\gamma^{(1)}\gamma^{(8)}\Phi = -\tfrac12 f_1H\,B_{148}, \\
K^{x_1}{}_{x_4} &= \tfrac12\big(\bar\Phi\gamma^{x_1}M\Phi + \bar\Phi M\gamma^{x_1}\Phi\big) = \frac{1}{2f_1}\,\bar\Phi\{\gamma^{(1)}, M\}\Phi, \\
\{\gamma^{(1)}, M\} &= -V\{\gamma^{(1)}, \gamma^{(4)}\} + 3H\{\gamma^{(1)}, \gamma^{(4)}\gamma^{(8)}\} = 0 + 6H\,\gamma^{(1)}\gamma^{(4)}\gamma^{(8)}, \\
K^{x_1}{}_{x_4} &= \frac{3H}{f_1}\,B_{148}, \qquad g^{44}g_{11}K^{x_1}{}_{x_4} = (-1)\,f_1^2\cdot\frac{3H}{f_1}\,B_{148} = -3f_1H\,B_{148}, \\
T^{x_4}{}_{x_1} &= -\tfrac12\Big(K^{x_4}{}_{x_1} + g^{44}g_{11}K^{x_1}{}_{x_4}\Big) = -\tfrac12\Big(-\tfrac12 - 3\Big)f_1H\,B_{148} = \tfrac74\,e^{a_4}\sin^{1/6}z\;H\,B_{148} .
\end{aligned}
$$

The first line is the result of Section 9.12, with $\gamma^{(4)}\gamma^{(1)}\gamma^{(8)} = -\gamma^{(1)}\gamma^{(4)}\gamma^{(8)}$ (one exchange). The second inserts the derivatives of the condensate into the definition of $K^{x_1}{}_{x_4}$ and $\gamma^{x_1} = \gamma^{(1)}/f_1$. The third inserts $M = -V\gamma^{(4)} + 3H\gamma^{(4)}\gamma^{(8)}$: two different gammas anticommute, so $\{\gamma^{(1)}, \gamma^{(4)}\} = 0$, and the anticommutator with a product of two other gammas is twice the product of the three. The fourth collects, and multiplies by $g^{44}g_{11} = (1/g_{44})\,g_{11} = (-1)f_1^2$. The fifth adds the two pieces, with $-\frac12(-\frac12 - 3) = \frac74$, and writes $f_1 = e^{a_4}\sin^{1/6}z$. Three things follow. The effective mass $V$ has dropped out. The coefficient contains $H$ and not $a_4'$, so the 12 momentum flows remain when $a_4' = 0$. And the larger part, $3$ of the $\frac72$ inside the bracket, comes from the term $3H\gamma^{(4)}\gamma^{(8)}$ of $M$, that is from the gravitational term $3H\gamma^{(8)}$ of the field equation (Fact 2 of Section 9.3). At $a_4 = 0.5$, $z = \pi/4$, $H = 1$ the coefficient is $\frac74\cdot 1.6487213\cdot 0.9438743 = 2.723325$ (rounded to six decimals); the record writes the symmetrised $K$ with the coefficient $-2.723325$, and Notebook 09c prints `T^x4_x1 = -(-2.723325) x its bilinear`.

**Condensates with a diagonal tensor.** The record also constructs exact condensates for which all 15 bilinears vanish, so that their tensor is diagonal at every point of every history: a perfect fluid at rest, with $T^{x_4}{}_{x_4} = -VS + L_0$ and pressure $L_0$. The construction uses the three matrices $P_1 = \gamma^{(1)}\gamma^{(5)}$, $P_2 = \gamma^{(2)}\gamma^{(6)}$, $P_3 = \gamma^{(3)}\gamma^{(7)}$, which pair each 3-space direction with an extra time. Each squares to 1 ($\gamma^{(1)}\gamma^{(5)}\gamma^{(1)}\gamma^{(5)} = -\gamma^{(1)}\gamma^{(1)}\gamma^{(5)}\gamma^{(5)} = -(1)(-1) = 1$), they commute with each other and with $M$ (moving a product of two gammas past another gamma with a different index costs two minus signs), and each anticommutes with $C$ ($C = \gamma^{(8)}\gamma^{(1)}\gamma^{(2)}\gamma^{(3)}$ contains $\gamma^{(k)}$ but not $\gamma^{(k+4)}$, so moving $P_k$ through $C$ costs three minus signs for $\gamma^{(k)}$ and four for $\gamma^{(k+4)}$). When $V^2 > 9H^2$, let $\omega = \sqrt{V^2 - 9H^2}$; then $M^2 = -\omega^2$ (Section 9.18, with $k^2 = 9H^2 - V^2 = -\omega^2$). Four steps build the condensate.

- **Step 1: two spaces of dimension 8.** For any column $u$ put $u_- = \frac12\big(u + \frac{i}{\omega}Mu\big)$ and $u_+ = \frac12\big(u - \frac{i}{\omega}Mu\big)$. Then $u_- + u_+ = u$, and $Mu_- = \frac12\big(Mu + \frac{i}{\omega}M^2u\big) = \frac12\big(Mu - i\omega u\big) = -i\omega\,u_-$ (insert $M^2 = -\omega^2$, then take out the factor $-i\omega$, using $-i\omega\cdot\frac{i}{\omega} = 1$); in the same way $Mu_+ = +i\omega\,u_+$. So every column is the sum of a column of the space $E_-$ of the eigenvalue $-i\omega$ and a column of the space $E_+$ of the eigenvalue $+i\omega$; a nonzero column cannot lie in both (it cannot have two different eigenvalues), so the dimensions of $E_-$ and $E_+$ add up to 16. $M$ is real, so for $Mu = -i\omega u$ the complex conjugate column $\bar u$ obeys $M\bar u = \overline{Mu} = \overline{-i\omega u} = +i\omega\,\bar u$: complex conjugation carries $E_-$ into $E_+$ and $E_+$ into $E_-$, and it keeps independent columns independent, so the two spaces have the same dimension, $16/2 = 8$.
- **Step 2: eight sectors.** $P_1$, $P_2$, $P_3$ commute with $M$, so they map $E_-$ into itself (if $Mu = -i\omega u$ then $M(P_ku) = P_kMu = -i\omega\,P_ku$). Because $P_k^2 = 1$, the matrix $\frac12(1 + \varepsilon P_k)$, for a sign $\varepsilon = \pm1$, keeps the columns with $P_ku = \varepsilon u$ and sends those with $P_ku = -\varepsilon u$ to zero (it is a **projector**), and $\frac12\big(1 + \frac{i}{\omega}M\big)$, which turns $u$ into $u_-$, keeps $E_-$ and sends $E_+$ to zero. For three signs $\varepsilon_1, \varepsilon_2, \varepsilon_3$ the product $\Pi = \frac12\big(1 + \frac{i}{\omega}M\big)\cdot\frac12(1 + \varepsilon_1P_1)\cdot\frac12(1 + \varepsilon_2P_2)\cdot\frac12(1 + \varepsilon_3P_3)$ of these four commuting projectors keeps exactly the columns of $E_-$ with $P_1 = \varepsilon_1$, $P_2 = \varepsilon_2$, $P_3 = \varepsilon_3$ (a **sector** of $E_-$; there are $2^3 = 8$ of them) and sends every other column to zero; it obeys $\Pi^2 = \Pi$.
- **Step 3: every sector has dimension 1.** For a matrix with $\Pi^2 = \Pi$ every column splits as $u = \Pi u + (u - \Pi u)$, a part that $\Pi$ keeps ($\Pi\Pi u = \Pi u$) and a part that it sends to zero ($\Pi(u - \Pi u) = 0$). In a basis made of kept and of removed columns $\Pi$ is diagonal with entries 1 and 0, so its **trace** (the sum of its diagonal entries, which is the same in every basis because $\mathrm{tr}(AB) = \mathrm{tr}(BA)$) is the dimension of the kept space. Multiply out $\Pi$: it is $\frac1{16}$ times the unit matrix plus terms that are each a number times a product of 1 to 8 different frame gammas (the indices of $P_k$ are $k$ and $k + 4$, those of $M = -V\gamma^{(4)} + 3H\gamma^{(4)}\gamma^{(8)}$ are 4 and 8: all different). A product $X$ of $n$ different frame gammas has trace 0: choose a gamma $\gamma^{(b)}$ among its factors if $n$ is even, and one that is not among them if $n$ is odd (then $n \le 7$, so one is left); moving $\gamma^{(b)}$ through $X$ costs $n - 1$ minus signs in the first case and $n$ in the second, an odd number either way, so $X\gamma^{(b)} = -\gamma^{(b)}X$; then $\mathrm{tr}X = \mathrm{tr}\big(X\gamma^{(b)}(\gamma^{(b)})^{-1}\big) = \mathrm{tr}\big((\gamma^{(b)})^{-1}X\gamma^{(b)}\big) = -\mathrm{tr}\big((\gamma^{(b)})^{-1}\gamma^{(b)}X\big) = -\mathrm{tr}X$ (the inverse exists because $(\gamma^{(b)})^2 = \pm1$; the second step is $\mathrm{tr}(AB) = \mathrm{tr}(BA)$), and a number equal to minus itself is 0. Only the unit matrix contributes, $\mathrm{tr}\,\Pi = 16/16 = 1$, and every one of the eight sectors of $E_-$ has dimension 1.
- **Step 4: the condensate.** Take a unit column $v_1$ (a column of length 1) in the sector $P_1 = P_2 = P_3 = -1$ and a unit column $v_2$ in the sector $P_1 = P_2 = P_3 = +1$. By Step 3 each is unique up to a factor $e^{i\theta}$ of size 1. Put $c = \overline{v_1^\dagger Cv_2}$ (the bar over a number means its complex conjugate) and $\Phi_0 = v_1 + cv_2$, a column of $E_-$. Other choices of the factors change nothing that matters: replacing $v_1$ by $e^{i\alpha}v_1$ and $v_2$ by $e^{i\beta}v_2$ replaces $c$ by $e^{i(\alpha - \beta)}c$ and $\Phi_0$ by $e^{i\alpha}\Phi_0$, which leaves every bilinear unchanged. Since $M\Phi_0 = -i\omega\Phi_0$, the column $\Phi = e^{-i\omega x_4}\Phi_0$ solves $\partial_4\Phi = M\Phi$: an exact condensate that oscillates with the angular frequency $\omega$.

A **witness** is an explicit example that proves that something exists. For three choices of $(V, H)$ the record builds this condensate with exact arithmetic and proves that all 15 of its bilinears vanish (and with them every off-diagonal entry, for every $a_4$ and $a_4'$); each of the three is a witness: it proves that condensates with a diagonal tensor exist. Notebook 09c builds the same three and confirms numerically the dimensions 8 and 1 of Steps 1 and 3. The record's three witnesses have $(V, H) = (5, 1)$, $(5, 4/3)$ and $(-5, 1)$, so $\omega = \sqrt{25 - 9} = 4$, $\sqrt{25 - 16} = 3$ and $4$ (PROVED; check `condensate_diagonal_witness_exact`; the record writes the effective mass $V$ as $M$ and the frequency as w). Their $S$ is never negative: $C$ anticommutes with $P_1$, which is real and symmetric, so for $P_1v_1 = -v_1$

$$
v_1^\dagger Cv_1 = -v_1^\dagger CP_1v_1 = v_1^\dagger P_1Cv_1 = (P_1v_1)^\dagger Cv_1 = -v_1^\dagger Cv_1 ,
$$

hence $v_1^\dagger Cv_1 = 0$ (a number equal to minus itself is zero), and likewise $v_2^\dagger Cv_2 = 0$; with $s = v_1^\dagger Cv_2$ one has $v_2^\dagger Cv_1 = \bar s$ ($C$ is real and symmetric) and $c = \bar s$, so $S = \Phi_0^\dagger C\Phi_0 = 0 + c\,s + \bar c\,\bar s + 0 = 2|s|^2 \ge 0$. (The first step replaces $v_1$ by $-P_1v_1$, the second uses $CP_1 = -P_1C$, the third $P_1^\dagger = P_1$, the fourth $P_1v_1 = -v_1$.)

**What this means for the field equations of gravity.** The field equations of $a_4$ (Chapter 12) have one equation for each of the 64 entries. For every entry off the diagonal the gravitational side (the left-hand side) vanishes identically, so the equation reads $0 = \kappa T^\nu{}_\mu$, and for a coupling $\kappa \neq 0$ every off-diagonal entry of the source must vanish (PROVED; the table below names the record's entries and checks). For a condensate the record turns this into conditions on the 15 bilinears: the six $B_{j48}$ must vanish, and on a deflating history ($a_4' \neq 0$) the nine $B_{i4t}$ as well. So on a deflating history a condensate meets the off-diagonal conditions only if all 15 bilinears vanish, as for the witnesses.

| statement | Revision record | entry or check |
| --- | --- | --- |
| the off-diagonal equations read $0 = \kappa T^\nu{}_\mu$ | `Revision/field_equations_a4/a4-equations.json` | `generalSource.offDiagonal_x4x8`, `generalSource.offDiagonal_x8x4`, `generalSource.offDiagonal_other` |
| their left-hand sides vanish identically | `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `independent_components` |
| the same, verified independently with sympy | `Revision/field_equations_a4/reports/python-a4-report.json` | `other_components_vanish` |
| the conditions on the 15 bilinears of a condensate | `Revision/field_equations_a4/a4-equations.json` | `fields.dirac16complex00.offDiagonalConditions` |
| the evolution equation $a_4''F(a_4') = \kappa(p_3 - p_t)$ | `Revision/field_equations_a4/a4-equations.json` | `generalSource.evolution_x1_minus_x5`, `generalSource.evolution_F` |
| the left-hand side factorises as $a_4''F(a_4')$ | `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `evolution_factorises_a4pp_times_F` |
| $F$ is not the zero polynomial unless $\alpha_1 = \alpha_2 = \alpha_3 = 0$ | both reports of the folder `Revision/field_equations_a4/reports` | `evolution_F_not_identically_zero` |
| the theorem of the linear history | `Revision/field_equations_a4/a4-equations.json` | `fields.dirac16complex00.theoremLinear` |
| the linear history: $A$ enters only through even powers | `Revision/field_equations_a4/a4-equations.json` | `linearMember` |

**The theorem of the linear history** (PROVED; record entry `theoremLinear`, see the table). Its hypotheses are four: (1) $\Phi$ is a homogeneous condensate of the commuting field that solves its field equation; (2) it meets the off-diagonal conditions above; (3) $a_4$ is twice continuously differentiable ($a_4'$ and $a_4''$ exist and are continuous functions of $x_4$); (4) the three Lovelock couplings $\alpha_1, \alpha_2, \alpha_3$ of Chapter 12 are not all zero. Its conclusion: if the author's metric with this $a_4$ solves the field equations of gravity with the condensate as the source, then $a_4 = AHx_4 + a_0$ with real constants $A$ and $a_0$. The argument uses, besides (3) and (4), the equality $p_3 = p_t$ of a condensate and one equation of the record:

- the evolution equation, the 3-space equation minus the extra-time equation, is $a_4''\,F(a_4') = \kappa(p_3 - p_t)$ with $F = 2\alpha_1 - 48(a_4')^2\alpha_2 + 720(a_4')^4\alpha_3 - 80\alpha_2H^2 + 864(a_4')^2\alpha_3H^2 + 720\alpha_3H^4$ (see the table);
- a condensate has $p_3 = p_t$ (Section 9.19: all seven pressures equal $SU' - U$), so $a_4''\,F(a_4') = 0$ at every time;
- $F$ is a polynomial in $a_4'$ that is not the zero polynomial: its coefficient of $(a_4')^4$ is $720\alpha_3$; if $\alpha_3 = 0$, its coefficient of $(a_4')^2$ is $-48\alpha_2$; if $\alpha_2 = \alpha_3 = 0$, its constant term is $2\alpha_1$; by (4) one of these is not zero, so $F$ has at most four roots (see the table);
- suppose $a_4'' \neq 0$ at some time; since $a_4''$ is continuous it stays different from zero on a small interval around that time, where $a_4'$ is then strictly increasing or strictly decreasing and takes infinitely many different values; but $a_4''F(a_4') = 0$ forces $F(a_4') = 0$ on that interval, so $F$ would have infinitely many roots, which is impossible; hence $a_4'' = 0$ at every time;
- so $a_4'$ is a constant, which we write $AH$, and integrating once more gives $a_4 = AHx_4 + a_0$.

**Deflation is a choice of sign.** The equations of the linear history contain $A$ only through $A^2$, $A^4$ and $A^6$ (record entry `linearMember`), so they do not change when $A$ is replaced by $-A$: extra times that deflate ($A > 0$, the author's history), extra times that inflate ($A < 0$) and the static case ($A = 0$) are allowed on exactly the same footing. That the author's extra times deflate is a choice of sign, an initial condition; the equations do not select it (record entry `theoremLinear`; Chapter 12).

**What is and is not known about a condensate as the source.** The Revision record contains no check that combines a witness with the remaining equations of gravity for definite values of $\kappa$, $\Lambda$, $m$, $\lambda$ and $A$. Chapter 12 makes that combination for Einstein gravity: Notebook 12d constructs, with exact arithmetic, condensates whose 15 bilinears vanish and chooses $m$, $\lambda$ and $\Lambda$ so that all the Einstein equations hold on the deflating history $a_4 = Hx_4$; that is a computation of the book under stated ASSUMED inputs, not a Revision record, and Chapter 12 gives its status. For Einstein-Lovelock gravity with $\alpha_2$ or $\alpha_3$ different from zero no such solution is constructed, in the record or in this book (OPEN).

**Conservation of the full tensor.** The Noether identity proves $\nabla_\mu T^\mu{}_\nu = 0$ for every solution, the 42 off-diagonal entries included (Section 9.9). Notebook 09c tests it numerically on a condensate along the curved history $a_4 = 0.3x_4 + 0.05x_4^2$, with a **negative control**: a configuration built so that the test must fail, which shows that the test can detect an error. The control is the condensate of an equation without the gravitational term $3H\gamma^{(8)}$ ($M = -V\gamma^{(4)}$). Its $S$ is constant and its $K_4 = \frac12\bar\Phi\{\gamma^{(4)}, M\}\Phi = \frac12(-V)(-2)S = VS$ is the same as for the true condensate, so its energy density and pressures, and with them the energy balance ($x_4$) and the hidden balance ($x_8$), are unchanged; but it does not solve the field equation of the author's metric, and its six momentum balances along 3-space and the extra times fail.

### 9.27 Example: the full tensor of a condensate

The third worked example computes all 64 entries of the tensor of exact condensates. It shows the tensor of a generic condensate (effective mass $V = 5$, $H = 1$, at the point $a_4 = 0.5$, $a_4' = 0.25$, $z = \pi/4$) as a heat map and counts its nonzero off-diagonal entries (42, and 12 when $a_4' = 0$); shows how three entries depend on $a_4'$; checks that each of the 42 entries is a fixed multiple of one of 15 bilinears and that the multiple is exactly minus the record's coefficient; builds the record's three witnesses, checks the dimensions 8 and 1 of their construction, checks that their tensor is diagonal at 36 points and that their $S = 2|v_1^\dagger Cv_2|^2$, and reproduces the record's frequencies and values of $S$; and tests the conservation of the full tensor with finite differences along a curved history, with the negative control. In this notebook the matrix of the condensate equation is called $A = -\gamma^{(4)}(V - 3H\gamma^{(8)})$; it is the matrix $M$ of Section 9.18 (multiply out: $-V\gamma^{(4)} + 3H\gamma^{(4)}\gamma^{(8)}$), and it has nothing to do with the constant $A$ of the history $a_4 = AHx_4$. The angular frequency of the witnesses is called $\omega$ (in the code `freq`), to keep it apart from the equation of state $w$. The notebook draws five figures.

<!-- NOTEBOOK 09c -->

### 9.30 Line-by-line walk-through of Notebook 09c

The notebook has 20 code cells, In [1] to In [20]. As in Section 9.17, long figure captions are shortened to a line "...)" and docstrings are left out here; the captions are printed in full in Section 9.29.

**In [1], the set-up cell.** It is word for word the set-up cell of Notebook 09a, explained line by line in Section 9.17, except that its comment lines are the run instructions of Notebook 09c (Section 9.28) and its line `NOTEBOOK_ID = "09c"` names this notebook. It prints `Set-up of notebook 09c complete: repository folder found, helpers defined.`

**In [2], the gammas and two report helpers.**

```python
import numpy as np  # arrays of numbers, matrices, linear algebra

fixture = json.loads(
    repository_file("Revision/algebra/gammas.json").read_text(encoding="utf-8"))
gamma = [np.array(rows, dtype=float) for rows in fixture["gamma"]]  # x1, ..., x8
eta = np.array(fixture["eta"], dtype=float)  # (+1, +1, +1, -1, -1, -1, -1, +1)
C = np.array(fixture["C"], dtype=float)  # gamma^(x8) gamma^(x1) gamma^(x2) gamma^(x3)
I16 = np.eye(16)  # the 16 x 16 unit matrix
g4, g8 = gamma[3], gamma[7]  # gamma^(x4) and gamma^(x8)
NAMES = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]  # the author's coordinates
```

These lines read the eight real gammas, $\eta$ and $C$ from the fixture, as in In [2] of Notebooks 09a and 09b, and name $\gamma^{(4)}$, $\gamma^{(8)}$, the unit matrix and the coordinates.

```python
def record_entry(path, name):
    """The entry (name, verdict, detail) of the check name in the report path."""
    report_data = json.loads(repository_file(path).read_text(encoding="utf-8"))
    for item in report_data["checks"]:
        if item["name"] == name:
            return item
    raise KeyError(f"{path} has no check {name}")


def recorded(path, name):
    """The verdict (PASS or FAIL) of the check name in the Revision report path."""
    return record_entry(path, name)["verdict"].upper()  # some reports write "pass"


say("The gammas, C and the two report helpers are ready.")
```

`record_entry` returns the whole entry of one check of a report (its name, its verdict and its **detail**, a text in which the record writes what it computed); In [13] reads numbers out of a detail text. `recorded` returns only the verdict, as in the other notebooks. The cell prints one line.

**In [3], the geometry at a point.**

```python
def frame_factors(a4, z):
    """The eight factors f_a of the diagonal vielbein, in the order x1, ..., x8."""
    space = np.exp(a4) * np.sin(z) ** (1 / 6)  # 3-space: e^a4 sin^(1/6) z
    extra = np.exp(-a4) * np.sin(z) ** (1 / 6)  # extra times: e^(-a4) sin^(1/6) z
    return np.array([space] * 3 + [1.0] + [extra] * 3 + [1 / np.tan(z)])


def spin_connection(a4, a4p, z, H):
    """The eight matrices Omega_mu (record formula Omega_components)."""
    s = np.sin(z) ** (1 / 6)  # sin^(1/6) z
    omega = [np.zeros((16, 16)) for _ in range(8)]  # Omega_x4 = Omega_x8 = 0
    for i in range(3):  # the three 3-space directions x1, x2, x3
        omega[i] = 0.5 * np.exp(a4) * s * (a4p * gamma[i] @ g4 + H * gamma[i] @ g8)
    for t in range(4, 7):  # the three extra times x5, x6, x7
        omega[t] = -0.5 * np.exp(-a4) * s * (a4p * g4 @ gamma[t] + H * gamma[t] @ g8)
    return omega


say("frame_factors and spin_connection are defined.")
```

The same two functions as in In [3] and In [5] of Notebook 09a (explained in Section 9.17), with one change: $H$ is now an argument of `spin_connection`, because this notebook uses several values of $H$.

**In [4], the Dirac adjoint and the tensor at a point.**

```python
def bar(vector):
    """The Dirac adjoint vector^dagger C."""
    return vector.conj() @ C


def energy_momentum(phi, dphi, m, lam, a4, a4p, z, H):
    """The 64 entries T[nu, mu] = T^nu_mu at one point (real parts)."""
    f = frame_factors(a4, z)
    g_values = eta * f ** 2  # g_mumu
    omega = spin_connection(a4, a4p, z, H)
    gup = [gamma[mu] / f[mu] for mu in range(8)]  # gamma^mu
    S = (bar(phi) @ phi).real
    D = [dphi[mu] + omega[mu] @ phi for mu in range(8)]  # D_mu Phi
    Dbar = [bar(dphi[mu]) - bar(phi) @ omega[mu] for mu in range(8)]  # D_mu Phibar
    L0 = 0.5 * sum(bar(phi) @ gup[mu] @ D[mu] - Dbar[mu] @ gup[mu] @ phi
                   for mu in range(8)) - m * S - lam / 2 * S ** 2
```

`bar` is the Dirac adjoint, as before. This `energy_momentum` takes the jet and the parameters $m$, $\lambda$, $a_4$, $a_4'$, $z$ and $H$, and builds everything at the point itself: the factors, the metric entries, the spin connection, the coordinate gammas, $S$, the covariant derivatives and $L_0$, each line as in In [6] of Notebook 09a.

```python
    T = np.zeros((8, 8), dtype=complex)
    for nu in range(8):
        for mu in range(8):
            bracket = (bar(phi) @ gup[nu] @ D[mu] - Dbar[mu] @ gup[nu] @ phi
                       + g_values[mu] / g_values[nu]  # gamma_mu D^nu
                       * (bar(phi) @ gup[mu] @ D[nu] - Dbar[nu] @ gup[mu] @ phi))
            T[nu, mu] = (nu == mu) * L0 - bracket / 4
    if np.abs(T.imag).max() > 1e-9 * max(1.0, np.abs(T).max()):
        raise ValueError("the tensor is not real")  # it must be real
    return T.real


say("bar and energy_momentum are defined.")
```

The 64 entries are the formula of Section 9.6, with $\gamma_\mu D^\nu$ written as $(g_{\mu\mu}/g_{\nu\nu})\gamma^\mu D_\nu$. The function stops with a `ValueError` if the imaginary parts exceed rounding noise (the tensor must be real, Section 9.6), and otherwise returns the real parts.

**In [5], the tensor of a generic condensate.**

```python
V, H = 5.0, 1.0  # effective mass (m = 5, lambda = 0) and the author's constant
POINT = {"a4": 0.5, "a4p": 0.25, "z": np.pi / 4}  # a point of a deflating history
rng = np.random.default_rng(11)  # a fixed seed
chi = rng.normal(size=16) + 1j * rng.normal(size=16)
chi /= np.linalg.norm(chi)  # length 1
```

The example has $V = 5$ (with $m = 5$ and $\lambda = 0$) and $H = 1$, so $V^2 > 9H^2$ and the condensate oscillates. `POINT` is a dictionary with the point $a_4 = 0.5$, $a_4' = 0.25$, $z = \pi/4$. The column $\chi$ is random (seed 11) and divided by its length.

```python
def condensate_tensor(column, a4, a4p, z, V_value=V, H_value=H):
    """T of the condensate (lambda = 0, m = V_value) whose jet at the point is
    Phi = column and d4 Phi = A column, A = -gamma^(x4) (V - 3 H gamma^(x8))."""
    A_value = -g4 @ (V_value * I16 - 3 * H_value * g8)
    dphi = np.zeros((8, 16), dtype=complex)
    dphi[3] = A_value @ column  # the only nonzero derivative
    return energy_momentum(column, dphi, V_value, 0.0, a4, a4p, z, H_value)
```

The jet of a condensate at a point is $\Phi = \chi$ and $\partial_4\Phi = A\chi$ (the solution at $x_4 = 0$; at any other time the solution is another column with the same $S$, so nothing is lost), all other derivatives zero. `V_value=V` gives an argument a **default value**, used when the call leaves it out. With $\lambda = 0$ the mass $m$ equals $V$.

```python
def off_diagonal_pairs(T):
    """The ordered pairs (nu, mu), nu != mu, whose entry is not zero."""
    tolerance = 1e-10 * max(1.0, np.abs(T).max())
    return [(nu, mu) for nu in range(8) for mu in range(8)
            if nu != mu and abs(T[nu, mu]) > tolerance]
```

This function lists the pairs $(\nu, \mu)$ off the diagonal whose entry is larger than rounding noise ($10^{-10}$ times the largest entry, or $10^{-10}$).

```python
T_generic = condensate_tensor(chi, **POINT)
S_chi = (bar(chi) @ chi).real
expected_diagonal = np.zeros(8)
expected_diagonal[3] = -V * S_chi
A4_WL = "Revision/field_equations_a4/reports/wolfram-a4-report.json"
A4_PY = "Revision/field_equations_a4/reports/python-a4-report.json"
check(np.abs(np.diag(T_generic) - expected_diagonal).max() < 1e-12
      and abs(T_generic[3, 7]) < 1e-12 and abs(T_generic[7, 3]) < 1e-12
      and recorded(A4_WL, "condensate_kinetic_tensor_diagonal") == "PASS"
      and recorded(A4_PY, "authorT16_condensate_kinetic_diagonal") == "PASS",
      "diagonal (0, 0, 0, -V S, 0, 0, 0, 0) and T^x4_x8 = T^x8_x4 = 0",
      record=f"{A4_WL}, check condensate_kinetic_tensor_diagonal; {A4_PY}, check "
             "authorT16_condensate_kinetic_diagonal")
```

`**POINT` hands the three entries of the dictionary over as the named arguments `a4`, `a4p` and `z`. With $\lambda = 0$, $L_0 = SU' - U = 0$ on shell, so the diagonal of Section 9.26 is $(0, 0, 0, -VS, 0, 0, 0, 0)$; the check confirms it, and $T^{x_4}{}_{x_8} = T^{x_8}{}_{x_4} = 0$.

```python
pairs = off_diagonal_pairs(T_generic)
# the same condensate and point with a4p = 0 (a4 not changing at this moment)
pairs_constant_a4 = off_diagonal_pairs(
    condensate_tensor(chi, POINT["a4"], 0.0, POINT["z"]))
check(len(pairs) == 42, "a generic condensate has 42 nonzero off-diagonal entries")
momentum_flows = sorted([(3, i) for i in (0, 1, 2, 4, 5, 6)]
                        + [(i, 3) for i in (0, 1, 2, 4, 5, 6)])
check(sorted(pairs_constant_a4) == momentum_flows,
      "with a4p = 0 only the 12 flows T^x4_xj, T^xj_x4 (j = 1, 2, 3, 5, 6, 7) remain")
report("S of the random column", f"{S_chi:.6f}")
report("T^x4_x4 = -V S", f"{T_generic[3, 3]:.6f}")
```

The cell counts the nonzero entries off the diagonal (42) and repeats the count with $a_4' = 0$: then exactly the 12 pairs $(x_4, x_j)$ and $(x_j, x_4)$ with $x_j$ one of the six directions of 3-space and the extra times remain (`momentum_flows`). It prints $S = 0.293667$ and $T^{x_4}{}_{x_4} = -VS = -1.468334$.

**In [6], the heat map of the generic condensate (Figure 09c.1).**

```python
def heat_map(ax, T, title, largest):
    """Draw T as coloured squares with the value printed in each."""
    picture = ax.imshow(T, cmap="RdBu_r", vmin=-largest, vmax=largest)
    for nu in range(8):
        for mu in range(8):
            text = f"{T[nu, mu]:.2f}"
            if text == "-0.00":  # a tiny negative number: print it as 0.00
                text = "0.00"
            # white digits on dark squares, black digits on light ones
            colour = "white" if abs(T[nu, mu]) > 0.6 * largest else "black"
            ax.text(mu, nu, text, ha="center", va="center", fontsize=6,
                    color=colour)
    ticks = [f"${n[0]}_{n[1]}$" for n in NAMES]
    ax.set_xticks(range(8), ticks)
    ax.set_yticks(range(8), ticks)
    ax.set_xlabel("lower index $\\mu$ (column)")
    ax.set_ylabel("upper index $\\nu$ (row)")
    ax.set_title(title)
    ax.grid(False)
    return picture
```

`heat_map` draws a table as in In [8] of Notebook 09a, with two decimals in each square; a rounding remainder such as $-0.0000001$ would print as `-0.00`, which the `if` replaces by `0.00`. The function returns the picture, for the colour bar.

```python
SCALE = 2.0  # the colour scale runs from -2 to 2 in both heat maps of this notebook
fig, ax = plt.subplots(figsize=(6.6, 5.6))
picture = heat_map(ax, T_generic, "Generic condensate: $T^\\nu{}_\\mu$", SCALE)
fig.colorbar(picture, ax=ax, label="value (energy per unit volume)", extend="both")
save_figure(fig, "generic_condensate",
            "Heat map of the 64 entries $T^\\nu{}_\\mu$ (row $\\nu$, column $\\mu$, "
            ...)
```

Both heat maps of the notebook use the fixed colour scale from $-2$ to 2, so they can be compared; `extend="both"` adds arrows to the colour bar for values beyond the scale. **What Figure 09c.1 shows.** The 64 entries of the generic condensate's tensor, in units of energy per unit volume. The only diagonal entry that is not zero is $-VS = -1.47$ at $(x_4, x_4)$; 42 squares off the diagonal are coloured, all of them produced by the spin connection; the squares $(x_4, x_8)$ and $(x_8, x_4)$ are zero, and so are the squares inside 3-space and inside the extra times. The student should see that equal pressures do not make a condensate a perfect fluid.

**In [7], the dependence on the deflation rate (Figure 09c.2).**

```python
rates = np.linspace(-1.0, 1.0, 41)  # values of a4p
entries = np.array([[T[3, 0], T[0, 4], T[0, 7]] for T in (
    condensate_tensor(chi, POINT["a4"], rate, POINT["z"]) for rate in rates)])
check(np.abs(entries[:, 0] - entries[20, 0]).max() < 1e-12 and abs(entries[20, 0]) > 0.1,
      "T^x4_x1 does not depend on a4p and is not zero")
slopes = entries[-1, 1:] / rates[-1]  # the slope of each of the other two entries
check(np.abs(entries[:, 1:] - np.outer(rates, slopes)).max() < 1e-12
      and np.abs(slopes).min() > 1e-3,
      "T^x1_x5 and T^x1_x8 are proportional to a4p (zero only at a4p = 0)")
report("T^x4_x1", f"{entries[20, 0]:.6f}")
report("slopes d T^x1_x5/d a4p and d T^x1_x8/d a4p",
       f"{slopes[0]:.6f} and {slopes[1]:.6f}")
```

For 41 values of $a_4'$ from $-1$ to 1 the cell computes the tensor of the same condensate at the same point and keeps three entries: $T^{x_4}{}_{x_1}$ (`T[3, 0]`), $T^{x_1}{}_{x_5}$ (`T[0, 4]`) and $T^{x_1}{}_{x_8}$ (`T[0, 7]`). The first check confirms that $T^{x_4}{}_{x_1}$ is the same for every $a_4'$ (it equals its value at the middle of the list, `entries[20, 0]`, where $a_4' = 0$) and is not zero. The second computes the slopes of the other two entries from the last value ($a_4' = 1$) and confirms that each entry is its slope times $a_4'$ at all 41 values (`np.outer(rates, slopes)` is the table of all products), with slopes that are not zero. It prints $T^{x_4}{}_{x_1} = 0.835532$ and the slopes $-0.012942$ and $-0.049288$.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(9.6, 3.9))
fig.subplots_adjust(wspace=0.35)
left.plot(rates, entries[:, 0], label="$T^{x_4}{}_{x_1}$ (momentum flow)")
left.set_ylim(0.0, 1.2 * entries[20, 0])
left.set_xlabel("deflation rate $a_4'$")
left.set_ylabel("entry (energy per unit volume)")
left.set_title("Comes from $H$: independent of $a_4'$")
left.legend(fontsize=8)
right.plot(rates, entries[:, 1], label="$T^{x_1}{}_{x_5}$")
right.plot(rates, entries[:, 2], "--", label="$T^{x_1}{}_{x_8}$")
right.axhline(0.0, color="black", linewidth=0.8)
right.set_xlabel("deflation rate $a_4'$")
right.set_title("Proportional to $a_4'$")
right.legend(fontsize=8)
save_figure(fig, "offdiagonal_entries",
            "Three off-diagonal entries of the generic condensate of the previous "
            ...)
```

**What Figure 09c.2 shows.** Left: the momentum flow $T^{x_4}{}_{x_1}$ (energy per unit volume) against $a_4'$ is a horizontal line at $0.835532$, the value printed by the cell: it comes from the $H$ part of the spin connection and from the term $3H\gamma^{(4)}\gamma^{(8)}$ of the condensate's time derivative (Section 9.26). Right: $T^{x_1}{}_{x_5}$ (solid) and $T^{x_1}{}_{x_8}$ (dashed) are straight lines through zero. The student should see that 30 of the 42 entries exist only because $a_4' \neq 0$, as the hand computation of $T^{x_1}{}_{x_5}$ in Section 9.26 showed.

**In [8], the 15 three-gamma bilinears.**

```python
def bilinear_directions(nu, mu):
    """The three directions (a, b, c) of the bilinear that carries T^nu_mu."""
    directions = {nu, mu}
    if 3 in directions and 7 not in directions:
        directions.add(7)  # add x8
    elif 7 in directions and 3 not in directions:
        directions.add(3)  # add x4
    elif 3 not in directions and 7 not in directions:
        directions.add(3)  # add x4
    return tuple(sorted(directions))


def bilinear(column, directions):
    a, b, c = directions
    return bar(column) @ gamma[a] @ gamma[b] @ gamma[c] @ column
```

`bilinear_directions` encodes the rule of the record: the bilinear of the entry $(\nu, \mu)$ has the directions $\nu$, $\mu$ and the missing one of $x_4$, $x_8$ (or $x_4$ when neither occurs). `{nu, mu}` is a **set** (a collection without order and without repetitions); `.add` puts an element in; `elif` means "else if"; `tuple(sorted(...))` returns the three directions in increasing order. `bilinear` computes $\bar\Phi\gamma^{(a)}\gamma^{(b)}\gamma^{(c)}\Phi$.

```python
columns = [rng.normal(size=16) + 1j * rng.normal(size=16) for _ in range(3)]
tensors = [condensate_tensor(column, **POINT) for column in columns]
worst_ratio, used = 0.0, set()
for nu, mu in pairs:
    directions = bilinear_directions(nu, mu)
    used.add(directions)
    ratios = [tensors[n][nu, mu] / bilinear(columns[n], directions) for n in range(3)]
    worst_ratio = max(worst_ratio,
                      max(abs(r - ratios[0]) for r in ratios) / abs(ratios[0]))
```

Three more random columns give three more condensates at the same point. For each of the 42 pairs the loop divides the entry by its bilinear for each of the three columns; if the entry is a fixed multiple of the bilinear, the three ratios are equal. `worst_ratio` keeps the largest relative spread, and `used` collects the bilinears that occur.

```python
check(worst_ratio < 1e-9 and len(used) == 15
      and recorded(A4_WL, "condensate_offdiagonal_are_three_gamma_bilinears") == "PASS"
      and recorded(A4_PY, "authorT16_condensate_offdiagonal_three_gamma") == "PASS",
      "each of the 42 entries is a fixed multiple of one of 15 three-gamma bilinears",
      record=f"{A4_WL}, check condensate_offdiagonal_are_three_gamma_bilinears; "
             f"{A4_PY}, check authorT16_condensate_offdiagonal_three_gamma")
for directions in sorted(used):
    say("bilinear Phibar gamma^(" + ") gamma^(".join(NAMES[d] for d in directions)
        + ") Phi")
```

The check confirms equal ratios and exactly 15 bilinears; the loop prints them: the nine $\bar\Phi\gamma^{(x_i)}\gamma^{(x_4)}\gamma^{(x_t)}\Phi$ and the six $\bar\Phi\gamma^{(x_j)}\gamma^{(x_4)}\gamma^{(x_8)}\Phi$ (written with the directions in increasing order).

**In [9], the coefficients of the record.**

```python
import re  # regular expressions: patterns that find pieces of a text

import sympy as sp  # exact algebra with symbols

A4_RECORD = "Revision/field_equations_a4/a4-equations.json"
record_entries = json.loads(repository_file(A4_RECORD).read_text(encoding="utf-8"))[
    "fields"]["dirac16complex00"]["offDiagonalKinetic"]
cc, a4v, ad1, H_symbol = sp.symbols("cc a4v ad1 H", real=True)
AT_POINT = {cc: 1 / np.tan(POINT["z"]), a4v: POINT["a4"], ad1: POINT["a4p"],
            H_symbol: H}
worst_coefficient, groups = 0.0, {}  # groups: formula text -> its first entry
```

A **regular expression** is a pattern that finds pieces of a text; the module `re` provides them. The record file holds, under `fields`, `dirac16complex00`, `offDiagonalKinetic`, the list of the 42 entries with their bilinears and coefficients. The coefficients are Wolfram-Language formulas in the names `cc` ($\cot z$), `a4v` ($a_4$), `ad1` ($a_4'$) and `H`; `AT_POINT` gives these names the values of the point.

```python
for item in record_entries:
    # "K^x1_x4 (symmetrised)": upper index x1 (row nu), lower index x4 (column mu)
    nu, mu = [int(digit) - 1 for digit in re.findall(r"x(\d)", item["component"])]
    term = item["terms"][0]  # every entry of the record has exactly one term
    directions = [int(digit) - 1 for digit in re.findall(r"x(\d)", term["bilinear"])]
    formula = term["coefficient"]["input"]  # the Wolfram Language text
```

For each entry of the record, `re.findall(r"x(\d)", text)` finds every `x` followed by a digit and returns the digits (`\d` means one digit, the parentheses mark the part to return; the `r` before the string keeps the backslash). The component name gives $\nu$ and $\mu$ and the bilinear's name gives its three directions, all counted from 0. `formula` is the coefficient's text.

```python
    coefficient = float(sp.sympify(
        formula.replace("E^", "E**").replace("^", "**"),
        locals={"E": sp.E, "cc": cc, "a4v": a4v, "ad1": ad1, "H": H_symbol},
    ).subs(AT_POINT))
    for column, T in zip([chi] + columns, [T_generic] + tensors):
        predicted = -coefficient * bilinear(column, tuple(directions))
        worst_coefficient = max(worst_coefficient, abs(T[nu, mu] - predicted))
    groups.setdefault(formula, (nu, mu, coefficient))
```

The formula is translated (`E^x` becomes `E**x`, and `^` becomes `**`), read by sympy, evaluated at the point (`.subs(AT_POINT)`) and turned into an ordinary number (`float`). For the generic column and the three random columns, the entry predicted by the record is minus the coefficient times the bilinear (off the diagonal $T = -K^{(\nu}{}_{\mu)}$, Section 9.26); the largest difference from the computed entry is kept. `groups` remembers the first entry of each distinct formula.

```python
check(len(record_entries) == 42 and len(groups) == 10 and worst_coefficient < 1e-12
      and recorded(A4_PY, "json_offdiagonal_coefficients") == "PASS"
      and recorded(A4_PY, "offdiagonal_coefficients_representation_independent")
      == "PASS",
      "all 42 entries are -(record coefficient) x bilinear, for 4 columns",
      record=f"{A4_RECORD}, offDiagonalKinetic; {A4_PY}, checks "
             "json_offdiagonal_coefficients and "
             "offdiagonal_coefficients_representation_independent")
for nu, mu, coefficient in groups.values():
    say(f"T^{NAMES[nu]}_{NAMES[mu]} = -({coefficient:+.6f}) x its bilinear")
```

The check confirms 42 entries in the record, ten distinct coefficient formulas, and agreement within $10^{-12}$ for all 42 entries and four columns. The loop prints one entry of each group; for example `T^x1_x5 = -(-0.045985) x its bilinear`, the coefficient derived by hand in Section 9.26, and `T^x4_x1 = -(-2.723325) x its bilinear`, from the record's coefficient $-\frac74e^{a_4}H\sin^{1/6}z$ ($\frac74\cdot 1.6487213\cdot 0.9438743 = 2.723325$, rounded to six decimals), also derived by hand in Section 9.26. Each printed line names one entry of its group; the other entries of the group have the same coefficient with another 3-space index $x_i$ or extra-time index $x_t$.

**In [10], the record's witnesses.**

```python
import itertools  # all combinations and all sign choices of a list

P = [gamma[i] @ gamma[i + 4] for i in range(3)]  # gamma^(x1) gamma^(x5), ...
```

The module `itertools` of Python's standard library provides the two tools used at the end of the cell: all combinations of a list and all choices of signs. `P` is the list of the three matrices $P_1 = \gamma^{(1)}\gamma^{(5)}$, $P_2 = \gamma^{(2)}\gamma^{(6)}$, $P_3 = \gamma^{(3)}\gamma^{(7)}$ of Section 9.26.

```python
def witness(V_w, H_w):
    """The frequency omega (here freq), A, the unit vectors v1, v2 and the column
    Phi0 of the record's diagonal witness for (V_w, H_w)."""
    A_w = -g4 @ (V_w * I16 - 3 * H_w * g8)  # d4 Phi = A Phi
    freq = np.sqrt(V_w ** 2 - 9 * H_w ** 2)  # the frequency omega
    # The null space of A + i omega: the rows of the third SVD factor whose
    # singular value is zero, complex conjugated and written as columns.
    _, singular, rows = np.linalg.svd(A_w + 1j * freq * I16)
    space = rows[singular < 1e-9].conj().T  # 16 x 8: the eigenspace for -i omega
```

The function builds the matrix $A$ and the angular frequency $\omega = \sqrt{V^2 - 9H^2}$. The columns $v$ with $Av = -i\omega v$ are the solutions of $(A + i\omega)v = 0$, the **null space** of $A + i\omega$. The **singular value decomposition** (`np.linalg.svd`) writes any matrix as a product $U\,\mathrm{diag}(s)\,W$ of two matrices with perpendicular unit rows or columns and a list of non-negative numbers $s$, the singular values; the rows of $W$ whose singular value is zero span the null space (after complex conjugation, written as columns). `rows[singular < 1e-9]` selects these rows; there are eight.

```python
    found = []
    for sign in (-1, 1):
        projector = (I16 + sign * P[0]) @ (I16 + sign * P[1]) @ (I16 + sign * P[2]) / 8
        left_vectors, values, _ = np.linalg.svd(projector @ space)
        if np.sum(values > 1e-9) != 1:
            raise ValueError("the joint eigenvector is not unique")
        found.append(left_vectors[:, 0])  # a unit vector
    v1, v2 = found
    c = np.conj(bar(v1) @ v2)  # c = conj(v1^dagger C v2)
    return freq, A_w, v1, v2, v1 + c * v2
```

Because $P_k^2 = 1$, the matrix $\frac12(1 \pm P_k)$ keeps the part of a column with $P_k = \pm1$ and removes the rest (a **projector**); the product of the three, $\frac18(1 \pm P_1)(1 \pm P_2)(1 \pm P_3)$, keeps exactly the columns with $P_1 = P_2 = P_3 = \pm1$. Applied to the eight columns of the eigenspace it leaves a single direction (the check `np.sum(values > 1e-9) != 1` stops the notebook otherwise), and the first left factor of its singular value decomposition is a unit column along it: $v_1$ for the sign $-1$, $v_2$ for $+1$. Then $c = \overline{v_1^\dagger Cv_2}$ and $\Phi_0 = v_1 + cv_2$. The function returns five results.

```python
WITNESSES = [(5.0, 1.0), (5.0, 4 / 3), (-5.0, 1.0)]  # the record's (V, H)
witnesses = {pair: witness(*pair) for pair in WITNESSES}  # (V, H) -> the five
for (V_w, H_w), found in witnesses.items():
    say(f"witness (V, H) = ({V_w:g}, {H_w:.4g}): frequency omega = "
        f"sqrt(V^2 - 9 H^2) = {found[0]:.6f}")
```

The record's three pairs $(V, H)$; `witness(*pair)` hands the two numbers over as two arguments. The cell prints the frequencies 4, 3 and 4 ($H = 4/3$ is printed as `1.333` by the format `.4g`, four significant digits).

```python
def product_of(indices):
    """The product gamma^(a) gamma^(b) ... of the frame gammas with these indices."""
    result = I16
    for index in indices:
        result = result @ gamma[index]
    return result


subsets = [chosen for size in range(1, 9)
           for chosen in itertools.combinations(range(8), size)]  # 255 index sets
traceless = all(abs(np.trace(product_of(chosen))) < 1e-12 for chosen in subsets)
```

The rest of the cell checks Steps 1 and 3 of the construction in Section 9.26 with numbers. `product_of` multiplies the frame gammas whose indices it is given, from left to right, starting from the unit matrix. `itertools.combinations(range(8), size)` lists every choice of `size` different indices out of $0, \dots, 7$, each in increasing order; for `size` from 1 to 8 these are $8 + 28 + 56 + 70 + 56 + 28 + 8 + 1 = 255 = 2^8 - 1$ choices. `np.trace` adds the diagonal entries of a matrix, and `traceless` is true when every one of the 255 products has trace 0 up to rounding, the lemma of Step 3.

```python
dimensions_hold = True
for (V_w, H_w), (freq, A_w, v1, v2, phi0) in witnesses.items():
    # the dimension of the space of -i omega: 16 minus the rank of A + i omega
    dimension = 16 - np.linalg.matrix_rank(A_w + 1j * freq * I16, tol=1e-9)
    for signs in itertools.product((-1, 1), repeat=3):  # the eight sectors
        keeper = (I16 + 1j / freq * A_w) / 2  # keeps the space of -i omega
        for sign, P_k in zip(signs, P):
            keeper = keeper @ (I16 + sign * P_k) / 2  # keeps P_k = sign
        dimensions_hold = dimensions_hold and abs(np.trace(keeper) - 1) < 1e-12
    dimensions_hold = dimensions_hold and dimension == 8
check(len(subsets) == 255 and traceless and dimensions_hold,
      "255 gamma products have trace 0; space of -i omega: dim 8; each sector: dim 1")
```

For each witness, the **rank** of a matrix (`np.linalg.matrix_rank`, the number of its independent columns, counted here with the tolerance $10^{-9}$ for rounding) gives the dimension of the space of the eigenvalue $-i\omega$: the columns $v$ with $(A + i\omega)v = 0$ form a space of dimension $16$ minus the rank of $A + i\omega$ (Step 1 says 8). `itertools.product((-1, 1), repeat=3)` lists the eight choices of three signs $(\varepsilon_1, \varepsilon_2, \varepsilon_3)$; for each, `keeper` is the matrix $\Pi = \frac12(1 + \frac{i}{\omega}A)\cdot\frac12(1 + \varepsilon_1P_1)\cdot\frac12(1 + \varepsilon_2P_2)\cdot\frac12(1 + \varepsilon_3P_3)$ of Step 2, built factor by factor (`1j / freq * A_w` is $\frac{i}{\omega}A$), and its trace must be 1 (Step 3). The check confirms the 255 traces, the dimension 8 and the 24 sector traces (eight sectors for each of the three witnesses), and prints `PASS 255 gamma products have trace 0; space of -i omega: dim 8; each sector: dim 1`.

**In [11], the witnesses are condensates with a diagonal tensor.**

```python
grid = [(a4, a4p, z) for a4 in (-1.0, 0.0, 0.5) for a4p in (-0.5, 0.0, 0.25, 1.0)
        for z in (0.3, 0.8, 1.3)]  # 3 x 4 x 3 = 36 points
witness_columns = {}  # (V, H) -> Phi0
unit_S = {}  # (V, H) -> S of Phi0 built from v1 and v2 of length 1
for (V_w, H_w), (freq, A_w, v1, v2, phi0) in witnesses.items():
    S_w = (bar(phi0) @ phi0).real
    largest_bilinear = max(abs(bilinear(phi0, d)) for d in used)
    worst_off = 0.0  # the largest off-diagonal entry at the 36 points
    for a4, a4p, z in grid:
        T = condensate_tensor(phi0, a4, a4p, z, V_w, H_w)
        worst_off = max(worst_off, np.abs(T - np.diag(np.diag(T))).max())
```

`grid` lists 36 points: every combination of three values of $a_4$, four of $a_4'$ (deflating, static and inflating) and three of $z$. For each witness the loop computes $S$, the largest of its 15 bilinears, and, at the 36 points, the largest entry off the diagonal of its tensor (`np.diag(np.diag(T))` is the diagonal matrix made of the diagonal of `T`, so `T - np.diag(np.diag(T))` keeps only the entries off the diagonal).

```python
    check(np.abs(A_w @ phi0 + 1j * freq * phi0).max() < 1e-12
          and largest_bilinear < 1e-12 and abs(S_w) > 0.1 and worst_off < 1e-12,
          f"witness (V, H) = ({V_w:g}, {H_w:.4g}): omega = {freq:g}, the 15 "
          "bilinears vanish, S != 0, T diagonal at 36 points")
    witness_columns[(V_w, H_w)] = phi0
    unit_S[(V_w, H_w)] = S_w
    report(f"witness ({V_w:g}, {H_w:.4g}): omega, and S for unit v1, v2",
           f"{freq:g} and {S_w:.6f}")
```

Each check confirms four things: $A\Phi_0 = -i\omega\Phi_0$, so $\Phi = e^{-i\omega x_4}\Phi_0$ is an exact condensate; all 15 bilinears vanish; $S \neq 0$; and the tensor is diagonal at all 36 points. The cell prints $S = 1.28$, $0.72$ and $1.28$.

**In [12], why $S$ of a witness is never negative.**

```python
anticommute = all(np.abs(C @ P_k + P_k @ C).max() < 1e-12 for P_k in P)
symmetric = all(np.array_equal(P_k, P_k.T) for P_k in P)  # real: P^dagger = P^T
steps_hold, observation = True, True
for (V_w, H_w), (freq, A_w, v1, v2, phi0) in witnesses.items():
    s = bar(v1) @ v2  # s = v1^dagger C v2
    S_unit = unit_S[(V_w, H_w)]  # S of Phi0 with unit v1, v2 (previous cell)
    steps_hold = (steps_hold and abs(bar(v1) @ v1) < 1e-12
                  and abs(bar(v2) @ v2) < 1e-12
                  and abs(S_unit - 2 * abs(s) ** 2) < 1e-12)
    observation = observation and abs(S_unit - 2 * freq ** 2 / V_w ** 2) < 1e-12
```

These lines check each step of the proof of Section 9.26: $CP_k = -P_kC$ and $P_k$ symmetric for the three $P_k$; and, for each witness, $v_1^\dagger Cv_1 = 0$, $v_2^\dagger Cv_2 = 0$ and $S = 2|v_1^\dagger Cv_2|^2$. `observation` tests a further formula, $S = 2\omega^2/V^2$.

```python
check(anticommute and symmetric and steps_hold,
      "C P_k = -P_k C, P_k symmetric, v^dagger C v = 0, so S = 2 |v1^dagger C v2|^2")
check(observation,
      "observed: S = 2 omega^2 / V^2 for the three witnesses (unit v1, v2)")
```

The first check confirms the steps of the proof. The second confirms the observation $S = 2\omega^2/V^2$ for these three witnesses ($2\cdot 16/25 = 1.28$ and $2\cdot 9/25 = 0.72$); this formula is COMPUTED for three cases and not proved here.

**In [13], the numbers of the record.**

```python
detail = record_entry(A4_WL, "condensate_diagonal_witness_exact")["detail"]
# the frequencies, which the record writes "w = sqrt(M^2 - 9 H^2) = {4, 3, 4}"
freq_text = re.search(r"9 H\^2\) = \{([^}]*)\}", detail).group(1)  # "4, 3, 4"
S_text = re.search(r"S = \{([^}]*)\}", detail).group(1)  # the three S values
record_freq = np.array([float(value) for value in freq_text.split(",")])
record_S = np.array([float(value) for value in S_text.split(",")])
our_freq = np.array([witnesses[pair][0] for pair in WITNESSES])
our_S = np.array([unit_S[pair] for pair in WITNESSES])
```

The record's Wolfram report writes the witnesses' numbers into the detail text of its check `condensate_diagonal_witness_exact`. `re.search(pattern, text)` finds the first place where the pattern matches, and `.group(1)` returns the part inside the first parentheses of the pattern. In the first pattern a backslash makes `^`, `)`, `{` and `}` ordinary characters, and `[^}]*` means "any characters except a closing brace"; so `freq_text` is the text between the braces after `9 H^2) =`, namely `4, 3, 4`, and `S_text` the text between the braces after `S =`. `.split(",")` cuts each text at the commas and `float` turns the pieces into numbers. `our_freq` and `our_S` are the notebook's values in the same order.

```python
check(np.abs(our_freq - record_freq).max() < 1e-12
      and recorded(A4_WL, "condensate_diagonal_witness_exact") == "PASS"
      and recorded(A4_PY, "authorT16_condensate_witness") == "PASS",
      f"omega = {freq_text} for the three witnesses, as in the record",
      record=f"{A4_WL}, check condensate_diagonal_witness_exact; {A4_PY}, check "
             "authorT16_condensate_witness")
quotients = record_S / our_S  # S of the record divided by S of unit v1, v2
check(np.abs(quotients / quotients[0] - 1).max() < 1e-9 and np.all(record_S > 0),
      f"S = {S_text} of the record are one common multiple of ours",
      record=f"{A4_WL}, check condensate_diagonal_witness_exact")
report("S of the record divided by S of unit v1, v2 (all three)",
       f"{quotients[0]:.1f}")
```

The frequencies must agree exactly: $\omega = \sqrt{V^2 - 9H^2}$ does not depend on any choice. The values of $S$ cannot agree, because the record builds the witnesses with exact columns $v_1$, $v_2$ that are not of length 1, and $S = 2|v_1^\dagger Cv_2|^2$ grows with their lengths (multiplying $v_1$ by a number $a$ and $v_2$ by $b$ multiplies $S$ by $|a|^2|b|^2$). So the second check divides each recorded $S$ by ours and requires the three quotients to be one and the same number; the record's values are then reproduced up to one common factor, which the cell prints. The factor is not physics: it is the product of the squared lengths of the record's columns, a choice of the record's verifier, and it changes whenever the verifier picks other columns. The Wolfram report `Revision/field_equations_a4/reports/wolfram-a4-report.json` in its version of 2026-10-08 (52 checks), whose verifier builds the columns from the author's gamma matrices, lists $S = 51200, 28800, 51200$; the quotients are $51200/1.28 = 40000$ for the first and the third witness and $28800/0.72 = 40000$ for the second, and the cell prints 40000.0. The version of 2026-10-01 (47 checks) built its columns from another set of $16 \times 16$ gamma matrices that obey the same Clifford relations and listed $S = 204800, 115200, 204800$, the common factor $160000$ (the record file `Revision/field_equations_a4/README.md` states both): the factor changed with the columns, while the frequencies, $S \neq 0$ and the vanishing of the 15 bilinears did not. The notebook reads the numbers from the report, so a later version of the report that lists other values of $S$ makes the cell print those values and their quotient instead.

**In [14], the heat map of a witness (Figure 09c.3).**

```python
T_witness = condensate_tensor(witness_columns[(5.0, 1.0)], **POINT)
fig, ax = plt.subplots(figsize=(6.6, 5.6))
picture = heat_map(ax, T_witness, "Witness condensate: $T^\\nu{}_\\mu$", SCALE)
fig.colorbar(picture, ax=ax, label="value (energy per unit volume)", extend="both")
save_figure(fig, "witness_condensate",
            "Heat map of the 64 entries $T^\\nu{}_\\mu$ of the exact witness "
            ...)
check(len(off_diagonal_pairs(T_witness)) == 0 and abs(T_witness[3, 3]) > 0.1,
      "the drawn witness tensor is diagonal with T^x4_x4 = -V S != 0")
```

The witness with $(V, H) = (5, 1)$ is drawn at the same point and with the same colour scale as the generic condensate. **What Figure 09c.3 shows.** All 64 entries, in units of energy per unit volume: only the square $(x_4, x_4)$ is coloured, with $-VS = -5\cdot 1.28 = -6.40$ (beyond the colour scale, so it has the darkest blue); every other entry is zero, the pressure included ($\lambda = 0$). The student should compare it with Figure 09c.1: this condensate is a perfect fluid at rest. The check confirms that no entry off the diagonal is nonzero.

**In [15], the Christoffel symbols along a curved history.**

```python
x = sp.symbols("x1:9", real=True)  # sympy was imported in section 8
Hs = sp.symbols("H", positive=True)
a4_function = sp.Function("a4")(x[3])
zs = 6 * Hs * x[7]
space_entry = sp.exp(2 * a4_function) * sp.sin(zs) ** sp.Rational(1, 3)
extra_entry = -sp.exp(-2 * a4_function) * sp.sin(zs) ** sp.Rational(1, 3)
g = sp.diag(*([space_entry] * 3 + [-1] + [extra_entry] * 3 + [sp.cot(zs) ** 2]))
history = sp.Rational(3, 10) * x[3] + sp.Rational(1, 20) * x[3] ** 2  # a4(x4)
```

The metric with symbols, as in In [13] of Notebook 09a, and the history $a_4 = \frac{3}{10}x_4 + \frac{1}{20}x_4^2$ with exact fractions. It is curved (not linear), increasing for $x_4 > -3$: the extra times deflate at a growing rate $a_4' = 0.3 + 0.1x_4$.

```python
christoffel = {}  # (l, i, j) with i <= j -> a numpy function of (x4, x8, H)
for l in range(8):
    for i in range(8):
        for j in range(i, 8):
            value = sp.simplify((sp.diff(g[l, j], x[i]) + sp.diff(g[l, i], x[j])
                                 - sp.diff(g[i, j], x[l])) / (2 * g[l, l]))
            if value != 0:  # put the history in, then make a numpy function
                christoffel[(l, i, j)] = sp.lambdify(
                    (x[3], x[7], Hs), value.subs(a4_function, history).doit(), "numpy")
check(len(christoffel) == 25, "25 nonzero Christoffel symbols (i <= j)")
```

The 25 symbols are computed as in Notebook 09a. Then the history is put in (`.subs(a4_function, history)` replaces $a_4(x_4)$; `.doit()` carries out the derivative $a_4'$ that is now a derivative of a known function), and `sp.lambdify((x4, x8, H), expression, "numpy")` turns the exact expression into a fast numpy function of the three numbers. The check confirms the count, 25.

**In [16], the test condensate, the control and the divergence.**

```python
m9, lam9, H9 = 1.0, 0.5, 0.25  # the parameters of this section
chi9 = rng.normal(size=16) + 1j * rng.normal(size=16)
chi9 /= np.linalg.norm(chi9)
V9 = m9 + lam9 * (bar(chi9) @ chi9).real  # the effective mass
M_TRUE = -V9 * g4 + 3 * H9 * g4 @ g8  # the true condensate: M^2 = 9 H^2 - V^2
M_CONTROL = -V9 * g4  # without the term 3 H gamma^(x8): M^2 = -V^2
K2_TRUE, K2_CONTROL = 9 * H9 ** 2 - V9 ** 2, -V9 ** 2
```

The test uses $m = 1$, $\lambda = 0.5$, $H = 0.25$ and a new random unit column. The true condensate has the matrix $M$ of Section 9.18; the control leaves out $3H\gamma^{(4)}\gamma^{(8)}$, so its matrix squares to $-V^2$ (the same computation as in Section 9.18 with $H = 0$).

```python
def field(M, k2, x4):
    """Phi(x4) and dPhi/dx4 = M Phi(x4) for Phi(0) = chi9 (M^2 = k2)."""
    k = np.sqrt(complex(k2))
    phi = np.cosh(k * x4) * chi9 + np.sinh(k * x4) / k * (M @ chi9)
    return phi, M @ phi


def tensor_at(M, k2, x4, x8):
    phi, d4 = field(M, k2, x4)
    dphi = np.zeros((8, 16), dtype=complex)
    dphi[3] = d4
    return energy_momentum(phi, dphi, m9, lam9, 0.3 * x4 + 0.05 * x4 ** 2,
                           0.3 + 0.1 * x4, 6 * H9 * x8, H9)
```

`field` returns $\Phi(x_4)$ and $\partial_4\Phi = M\Phi$ for either matrix. `tensor_at` returns the 64 entries at the point $(x_4, x_8)$ of the curved history: $a_4 = 0.3x_4 + 0.05x_4^2$, $a_4' = 0.3 + 0.1x_4$ and $z = 6Hx_8$.

```python
def divergence(M, k2, x4, x8, h):
    """The eight components of nabla_mu T^mu_nu, with central differences of step h,
    and the size of the tensor (its largest entry)."""
    T = tensor_at(M, k2, x4, x8)
    d4T = (tensor_at(M, k2, x4 + h, x8) - tensor_at(M, k2, x4 - h, x8)) / (2 * h)
    d8T = (tensor_at(M, k2, x4, x8 + h) - tensor_at(M, k2, x4, x8 - h)) / (2 * h)
```

The tensor of a condensate depends on $x_4$ and $x_8$ only, so its divergence needs $\partial_4T$ and $\partial_8T$. They are replaced by **central finite differences**, $\partial F \approx (F(x + h) - F(x - h))/(2h)$, whose error falls like $h^2$ as the step $h$ shrinks (the Taylor series: the terms of first and third order of $F(x + h)$ and $F(x - h)$ cancel in the difference, up to the error term $\frac{h^2}{6}F'''$).

```python
    G = np.zeros((8, 8, 8))  # G[l, i, j] = Gamma^l_ij
    for (l, i, j), function in christoffel.items():
        G[l, i, j] = G[l, j, i] = function(x4, x8, H9)
    result = np.zeros(8)
    for nu in range(8):
        result[nu] = (d4T[3, nu] + d8T[7, nu]  # d_mu T^mu_nu (only x4 and x8)
                      + np.einsum("mml,l->", G, T[:, nu])  # Gamma^mu_mu l T^l_nu
                      - np.einsum("lm,ml->", G[:, :, nu], T))  # Gamma^l_mu nu T^mu_l
    return result, np.abs(T).max()


report("effective mass V = m + lambda S of the test condensate", f"{V9:.6f}")
```

`G` is the $8 \times 8 \times 8$ table of all Christoffel symbols at the point (both orders of the lower indices are filled). For each $\nu$ the divergence is the formula of Section 9.9: the first sum has only the terms $\partial_4T^{x_4}{}_\nu$ and $\partial_8T^{x_8}{}_\nu$; `np.einsum("mml,l->", G, T[:, nu])` is $\sum_{\mu,\lambda}\Gamma^\mu{}_{\mu\lambda}T^\lambda{}_\nu$ (a repeated letter is summed; `->` with nothing after it means "sum everything to one number"), and `np.einsum("lm,ml->", G[:, :, nu], T)` is $\sum_{\lambda,\mu}\Gamma^\lambda{}_{\mu\nu}T^\mu{}_\lambda$. All entries off the diagonal are included. The function returns the eight components and the size of the tensor. The cell prints $V = 0.883522$.

**In [17], the divergence as the step shrinks.**

```python
steps = 0.2 / 2.0 ** np.arange(11)  # 0.2, 0.1, ..., about 0.0002
X4_TEST, X8_TEST = 1.0, 0.5 / (6 * H9)  # x4 = 1 and z = 0.5
true_sizes, control_sizes = [], []
for h in steps:
    div_true, size_true = divergence(M_TRUE, K2_TRUE, X4_TEST, X8_TEST, h)
    div_control, _ = divergence(M_CONTROL, K2_CONTROL, X4_TEST, X8_TEST, h)
    true_sizes.append(np.abs(div_true).max())
    control_sizes.append(np.abs(div_control).max())
true_sizes, control_sizes = np.array(true_sizes), np.array(control_sizes)
```

Eleven steps $h = 0.2/2^n$, $n = 0, \dots, 10$, from 0.2 down to about 0.0002. At the point $x_4 = 1$, $z = 0.5$ the loop computes the largest of the eight components of the divergence for the true condensate and for the control.

```python
ratios = true_sizes[:6] / true_sizes[1:7]  # halving h from 0.2 to 0.003125
check(np.all((ratios > 3.6) & (ratios < 4.4)),
      "true condensate: halving h divides the divergence by about 4 (error h^2)")
check(true_sizes[8] < 1e-6 * size_true,
      "true condensate: the divergence falls below 1e-6 of the tensor's size")
check(abs(control_sizes[-1] / control_sizes[-2] - 1) < 1e-3
      and control_sizes[-1] > 1e-2 * size_true,
      "control: the divergence tends to a nonzero value (it is not conserved)")
```

Three checks. If the exact divergence of the true condensate is zero, what remains is the error of the finite differences, proportional to $h^2$: halving $h$ must divide it by about 4 (`&` means "and" for arrays; the ratios of six successive halvings must lie between 3.6 and 4.4). At $h = 0.2/2^8 \approx 0.00078$ it must be below $10^{-6}$ of the size of the tensor. For the control the divergence must settle at a nonzero value: its last two values agree to $10^{-3}$ and exceed $10^{-2}$ of the size of the tensor.

```python
for x4_point, z_point in ((2.0, 1.0), (0.5, 1.2)):
    x8_point = z_point / (6 * H9)
    coarse, size_other = divergence(M_TRUE, K2_TRUE, x4_point, x8_point, 1e-3)
    fine, _ = divergence(M_TRUE, K2_TRUE, x4_point, x8_point, 1e-4)
    shrink = np.abs(coarse).max() / np.abs(fine).max()  # about 10^2 for an h^2 error
    check(90 < shrink < 110 and np.abs(fine).max() < 1e-5 * size_other,
          f"true condensate conserved at x4 = {x4_point}, z = {z_point} "
          "(h = 0.001 and 0.0001)")
```

Two more points of the history. Dividing the step by 10 must divide an error proportional to $h^2$ by about 100, and the finer result must be below $10^{-5}$ of the size of the tensor.

```python
WL = "Revision/theory/reports/wolfram-field-theory.json"
check(recorded(WL, "exact_solution_nonlinear_homogeneous_C") == "PASS"
      and recorded(WL, "conservation_on_shell_general") == "PASS",
      "the record proves the conservation that these numbers confirm",
      record=f"{WL}, checks exact_solution_nonlinear_homogeneous_C and "
             "conservation_on_shell_general")
for h, t_size, c_size in zip(steps[::2], true_sizes[::2], control_sizes[::2]):
    say(f"h = {h:.5f}:  true condensate {t_size:.2e},  control {c_size:.4f}")
```

The last check confirms that the record proves the conservation exactly. The loop prints every second step (`[::2]` takes every second entry): the true condensate's divergence falls from $5.06 \cdot 10^{-3}$ at $h = 0.2$ to $4.47 \cdot 10^{-9}$ at $h = 0.0002$, by about 16 for each factor 4 in $h$, while the control's settles at 0.0676. Six PASS lines in all.

**In [18], the convergence (Figure 09c.4).**

```python
fig, ax = plt.subplots()
ax.loglog(steps, true_sizes, "o-", label="true condensate")
ax.loglog(steps, control_sizes, "s-", label="control (no $3H\\gamma^{(8)}$ term)")
ax.loglog(steps, true_sizes[0] * (steps / steps[0]) ** 2, "k:",
          label="proportional to $h^2$")
ax.set_xlabel("finite-difference step $h$")
ax.set_ylabel("largest $|\\nabla_\\mu T^\\mu{}_\\nu|$")
ax.set_title("Conservation of the full tensor of a condensate")
ax.legend()
save_figure(fig, "conservation_convergence",
            "The largest of the eight components of the covariant divergence "
            ...)
```

`ax.loglog` draws with logarithmic scales on both axes; `"o-"` draws circles joined by lines, `"s-"` squares. The dotted line is proportional to $h^2$. **What Figure 09c.4 shows.** The largest component of the divergence (energy per unit volume per unit length) against the step $h$, both axes logarithmic. The circles of the true condensate fall along the dotted $h^2$ line over six powers of ten, so the exact divergence is zero; the squares of the control stay near 0.07. The student should see how a convergence plot separates an error of the method (which shrinks with $h$) from a real failure (which does not).

**In [19], the eight components (Figure 09c.5).**

```python
div_true, _ = divergence(M_TRUE, K2_TRUE, X4_TEST, X8_TEST, 1e-3)
div_control, _ = divergence(M_CONTROL, K2_CONTROL, X4_TEST, X8_TEST, 1e-3)
positions = np.arange(8)
fig, ax = plt.subplots()
floor = 1e-16  # zero components are drawn at this height on the logarithmic axis
ax.bar(positions - 0.2, np.abs(div_true) + floor, width=0.4, label="true condensate")
ax.bar(positions + 0.2, np.abs(div_control) + floor, width=0.4,
       label="control (no $3H\\gamma^{(8)}$ term)")
ax.set_yscale("log")
ax.set_ylim(1e-16, 10.0)
ax.set_xticks(positions, [f"$\\nu = {n[0]}_{n[1]}$" for n in NAMES], fontsize=8)
ax.set_ylabel("$|\\nabla_\\mu T^\\mu{}_\\nu|$ (with $h = 0.001$)")
ax.set_title("The eight components of the divergence")
ax.legend(fontsize=8)
save_figure(fig, "divergence_components",
            "The eight components $|\\nabla_\\mu T^\\mu{}_\\nu|$, $\\nu = x_1, \\dots, "
            ...)
```

At $h = 0.001$ the cell draws the size of each of the eight components for both configurations as bars on a logarithmic axis; $10^{-16}$ is added so that an exact zero, which a logarithmic axis cannot show, is drawn at the bottom. **What Figure 09c.5 shows.** For $\nu = x_1, \dots, x_8$: the true condensate's bars all lie at the level of the finite-difference error, below $10^{-6}$; the control's bars for the six momentum components $\nu = x_1, x_2, x_3, x_5, x_6, x_7$ stand between about 0.01 and 0.07, while its components $\nu = x_4$ and $x_8$ vanish. The student should see what Section 9.26 explained: the control keeps the energy and hidden balances (its $\rho$ and pressures are those of the true condensate) but breaks the momentum balances; the gravitational term $3H\gamma^{(8)}$ is needed for the conservation of the tensor.

```python
momentum = [0, 1, 2, 4, 5, 6]  # the components nu = x1, x2, x3, x5, x6, x7
check(np.abs(div_control).max() > 1e3 * np.abs(div_true).max()
      and np.abs(div_control[momentum]).min() > 1e-3
      and max(abs(div_control[3]), abs(div_control[7])) < 1e-9,
      "control: its six momentum components are nonzero (over 1000 times the true "
      "condensate's), its x4 and x8 components vanish")
```

The check confirms what the figure shows: the control's divergence is more than 1000 times the true condensate's, each of its six momentum components exceeds $10^{-3}$, and its $x_4$ and $x_8$ components are below $10^{-9}$.

**In [20], the last check.**

```python
captions = json.loads(output_file(CAPTION_FILE).read_text(encoding="utf-8"))
expected_files = ["09c_1_generic_condensate.png", "09c_2_offdiagonal_entries.png",
                  "09c_3_witness_condensate.png",
                  "09c_4_conservation_convergence.png",
                  "09c_5_divergence_components.png"]
check(sorted(captions) == expected_files and all(
    output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in expected_files),
    "the five figures of this notebook are saved and captioned")
all_checks_passed()
```

The five figures exist and are captioned, and the last line is `ALL 25 CHECKS PASSED (notebook 09c)`: three checks in In [5], two in In [7], one each in In [8], In [9] and In [10], three in In [11], two in In [12], two in In [13], one each in In [14] and In [15], six in In [17], and one each in In [19] and In [20].

### 9.31 What we proved, what we computed, what we assumed

**PROVED in this chapter, line by line** (and in the Revision record, with the file and check named in the section):

- For the diagonal vielbein of the author's metric, $\{\gamma^\mu, \Omega_\mu\} = 0$ for each direction and $\sum_\mu\gamma^\mu\Omega_\mu = 3H\gamma^{(8)}$; the $a_4'$ terms cancel because the extra times deflate (Section 9.3).
- From the definition of the energy-momentum tensor by the variation of the action, the diagonal entries $T^\mu{}_\mu = L_0 - K_\mu$ (Section 9.5); the reality of every entry and the symmetry of $T_{\nu\mu}$ (Section 9.6).
- $\rho = -\sum_{\mu \neq x_4}K_\mu + mS + U$, $p_\mu = \sum_{\nu \neq \mu}K_\nu - mS - U$, with their kinetic and potential parts (Section 9.7); the trace $7\sum_\mu K_\mu - 8(mS + U)$ and the kinetic-sum identity off shell, and on shell $\sum_\mu K_\mu = (m + U')S$, $L_0 = SU' - U$ and the trace $-mS + 3\lambda S^2$ (Section 9.8).
- The 25 Christoffel symbols; the lemma $\Gamma^\mu{}_{\mu\nu} = \partial_\nu\ln f_\mu$; the divergence of a diagonal tensor; the two conservation identities $\partial_4\rho = -3a_4'(p_3 - p_t)$ and $\partial_8p_8 = -3H\cot z\,(2p_8 - p_3 - p_t)$; the vanishing of the other six components (Section 9.9); the profiles $p_8 = P/2 + c/\sin z$ and the form in the coordinate $y$ (Section 9.11).
- The connection term $K^{x_4}{}_{x_1} = \frac12e^{a_4}\sin^{1/6}z\,H\,\bar\Phi\gamma^{(4)}\gamma^{(1)}\gamma^{(8)}\Phi$ of a homogeneous configuration (Section 9.12) and the entries $T^{x_1}{}_{x_5} = \frac12e^{-2a_4}a_4'\,\bar\Phi\gamma^{(1)}\gamma^{(4)}\gamma^{(5)}\Phi$ and $T^{x_4}{}_{x_1} = \frac74e^{a_4}\sin^{1/6}z\,H\,\bar\Phi\gamma^{(1)}\gamma^{(4)}\gamma^{(8)}\Phi$ of a condensate (Section 9.26), equal to the record's coefficients.
- The exact condensates, the constancy of $S$, $M^2 = 9H^2 - V^2$; their $\rho = mS + U$, $p = SU' - U$ in all seven directions, $T^{x_4}{}_{x_8} = 0$, and $w = x/(2 + x)$ with its special values (Sections 9.18 to 9.20); $\rho = E\,u^\dagger Bu$ for plane waves of flat space (Section 9.21); in the construction of the witnesses, the dimension 8 of the space of the eigenvalue $-i\omega$ and the dimension 1 of each of its eight sectors, and $S = 2|v_1^\dagger Cv_2|^2 \ge 0$ (Section 9.26); the argument of the theorem of the linear history from the record's evolution equation (Section 9.26).

**PROVED in the Revision record and used here without its proof:** the vielbein-variation tensor with its spin-density term; the complete (Belinfante) tensor as its symmetric part for every configuration, and the equality of the two tensors on shell in all 64 entries (off shell, in general, only the 8 diagonal entries agree); the drop-out of the spin connection from the Lagrangian of every diagonal vielbein; the conservation $\nabla_\mu T^\mu{}_\nu = 0$ of every solution (Noether identity); the same formulas for the Grassmann field dirac16complex; the positive Fock realisation of the quantised field for single good-sector momenta with frozen coefficients, and the complex frequencies of the curved good sector without a boundary condition at $z = \pi/2$ (for $U = 0$ whenever $m^2 < 9H^2$); in the finite Fock model of one good-sector mode set with frozen coefficients, the operator form of the on-shell identity for $\lambda \neq 0$ when the potential and the tensor are both Wick ordered, and its failure for every other ordering tested (Section 9.13); the 42 off-diagonal entries of a condensate as multiples of 15 bilinears with the listed coefficients, the diagonal witnesses with $\omega = 4, 3, 4$; the Krein inertia (4,4) of the plane waves; the vanishing of every off-diagonal entry of the source and the condition $p_3 + p_t = 2p_8$, both imposed by the field equations of gravity; and the theorem that a condensate source that meets the off-diagonal conditions allows only the linear history $a_4 = AHx_4 + a_0$ (under its four hypotheses, Section 9.26), with either sign of $A$.

**COMPUTED by the notebooks** (every number reproduces the record where they overlap): Notebook 09a, 27 checks, confirms the tensor identities at one point to $10^{-11}$ or better, re-derives the 25 Christoffel symbols and the two identities exactly, and checks the $x_8$ profiles on a grid to a relative residual of $2.3 \cdot 10^{-5}$; Notebook 09b, 33 checks, confirms the condensates at 401 times to $10^{-9}$, measures $w$ on twelve exact solutions (agreement with $x/(2 + x)$ to $10^{-9}$), solves the toy fluids with RK4 (relative error $1.33 \cdot 10^{-8}$, error ratio 16.17 for a halved step) and reproduces $\rho = \pm 5$; Notebook 09c, 25 checks, confirms the 42 entries against the record's coefficients to $10^{-12}$, the dimensions 8 and 1 of the construction of the witnesses, the diagonal tensor of the witnesses at 36 points, the record's frequencies exactly and its values of $S$ up to one common factor (40000 for the Wolfram report of 2026-10-08), and the conservation of the full tensor along a curved history (an error falling like $h^2$, down to $4.5 \cdot 10^{-9}$), with a negative control. The observation $S = 2\omega^2/V^2$ for the three witnesses is COMPUTED, not proved.

**ASSUMED, chosen, or an interpretation.** The sign conventions $\rho = -T^{x_4}{}_{x_4}$ and $p_\mu = T^\mu{}_\mu$ are definitions. The histories $a_4 = AHx_4$ ($A = 1$) and $a_4 = 0.3x_4 + 0.05x_4^2$ and every parameter value of the examples are choices; every identity holds for every history. The first-law reading of the $x_4$ identity is an interpretation, not an extra result. The toy fluids are an ILLUSTRATION, not solutions of the field equations.

**OPEN.** The equation of state that an observer in 3-space would infer, its change in time, fits of the CPL form $w(a) = w_0 + w_a(1 - a)$ (a straight line in the 3-space scale factor $a$, named after Chevallier, Polarski and Linder) and any comparison with supernova data; the operator (normal-ordered) form of the on-shell kinetic-sum identity $\sum_\mu\langle{:}K_\mu{:}\rangle = \langle{:}(m + U')S{:}\rangle$ for $\lambda \neq 0$ for the field on a whole slice (Section 9.13; it is verified only in the finite Fock model of one good-sector mode set with frozen coefficients, and there only under Wick ordering), and with it the operator form of the on-shell values of $L_0$ and of the trace, and the symmetry and conservation of the quartic operator; a space of quantum states with positive norms for the full quantised field (positive Fock spaces are constructed only for single good-sector momenta with frozen coefficients); a condensate that realises the deflating history together with all the field equations of Einstein-Lovelock gravity with $\alpha_2$ or $\alpha_3$ different from zero, for definite values of the constants (for Einstein gravity Chapter 12 constructs such solutions, under the ASSUMED inputs it states). Any reading of the negative energies of the commuting field as a phantom dark energy is a HYPOTHESIS, not a result.

**Not claimed.** Nothing in this chapter concerns the creation of universes or the matter-antimatter asymmetry. The only link to Part V is the sign reversal of the tensor under the chirality map $\Gamma$ (theorem T1, Section 9.21), an exact map between sets of solutions in a fixed gravitational field; it proves no creation process, rate or amplitude (Chapters 18 to 21 state what the pairing theorems prove and what they do not).

### 9.32 Exercises

**Exercise 1.** Use the lemma $\Gamma^\mu{}_{\mu\nu} = \partial_\nu\ln f_\mu$ of Section 9.9 to compute $\Gamma^{x_5}{}_{x_5x_4}$ and $\Gamma^{x_5}{}_{x_5x_8}$, and compare with the table.

*Answer.* $\ln f_5 = \ln\big(e^{-a_4}\sin^{1/6}z\big) = -a_4 + \frac16\ln\sin z$. Differentiating with respect to $x_4$: only $-a_4$ depends on $x_4$, so $\Gamma^{x_5}{}_{x_5x_4} = -a_4'$. Differentiating with respect to $x_8$ with the chain rule ($dz/dx_8 = 6H$): $\Gamma^{x_5}{}_{x_5x_8} = \frac16\cdot\frac{\cos z}{\sin z}\cdot 6H = H\cot z$. The table lists $\Gamma^{x_t}{}_{x_4x_t} = -a_4'$ (the symbol is symmetric in its lower indices) and $\Gamma^{x_t}{}_{x_tx_8} = H\cot z$.

**Exercise 2.** Suppose the extra times inflated like 3-space, with the factors $f_5 = f_6 = f_7 = e^{+a_4}\sin^{1/6}z$ (this is not the author's metric). Use the divergence formula for a diagonal tensor to find the $x_4$ identity, and explain the difference from Section 9.10.

*Answer.* Now $\partial_4\ln f_\mu = a_4'$ for all six directions $x_1, x_2, x_3, x_5, x_6, x_7$, and 0 for $x_4$ and $x_8$. With $T^{x_4}{}_{x_4} = -\rho$:
$\nabla_\mu T^\mu{}_{x_4} = -\partial_4\rho + 3a_4'(-\rho - p_3) + 3a_4'(-\rho - p_t) = -\partial_4\rho - 3a_4'(2\rho + p_3 + p_t)$.
Conservation gives $\partial_4\rho = -3a_4'(2\rho + p_3 + p_t)$. This has the form of the familiar cosmological law $d\rho/dt = -3(\dot a/a)(\rho + p)$, once for each family of three directions: the volume $\sqrt{|g|} = e^{6a_4}\cos z$ grows, and the energy density is diluted. In the author's metric the volume is constant, the two terms $\mp 3a_4'\rho$ cancel, and only the difference $p_3 - p_t$ remains.

**Exercise 3.** A condensate has $m = 1$, $S = 1$ and $\lambda = 0.5$. Compute $\rho$, $p$, $w$ and the trace in two ways. Repeat for $\lambda = -0.5$, and compare with the numbers printed by Notebook 09b.

*Answer.* $\lambda = 0.5$: $\rho = mS + \frac{\lambda}{2}S^2 = 1 + 0.25 = 1.25$; $p = \frac{\lambda}{2}S^2 = 0.25$; $w = 0.25/1.25 = 0.2$ (also $x/(2 + x)$ with $x = 0.5$: $0.5/2.5 = 0.2$). Trace: $-\rho + 7p = -1.25 + 1.75 = 0.5$, and $-mS + 3\lambda S^2 = -1 + 1.5 = 0.5$. $\lambda = -0.5$: $\rho = 1 - 0.25 = 0.75$, $p = -0.25$, $w = -1/3$ (and $x/(2 + x) = -0.5/1.5$); trace $-0.75 - 1.75 = -2.5 = -1 - 1.5$. Notebook 09b prints $\rho = 1.25$, $p = 0.25$, $w = 0.2$ and $\rho = 0.75$, $p = -0.25$, $w = -0.333333$.

**Exercise 4.** For $m > 0$ and $\lambda \neq 0$, find the value of $S$ for which a condensate has $w = -1$, compute its $\rho$ and $p$, and decide the sign of $\rho$. Does this condensate oscillate or grow?

*Answer.* $w = -1$ requires $x = \lambda S/m = -1$, that is $S = -m/\lambda$. Then $\rho = mS + \frac{\lambda}{2}S^2 = -\frac{m^2}{\lambda} + \frac{\lambda}{2}\cdot\frac{m^2}{\lambda^2} = -\frac{m^2}{\lambda} + \frac{m^2}{2\lambda} = -\frac{m^2}{2\lambda}$ and $p = \frac{\lambda}{2}S^2 = \frac{m^2}{2\lambda}$, so indeed $p = -\rho$. The energy density is positive only for $\lambda < 0$ (then $S = -m/\lambda > 0$); for $\lambda > 0$ it is negative. The effective mass is $V = m + \lambda S = 0$, so $k^2 = 9H^2 - 0 = 9H^2 > 0$: the condensate grows, like $e^{3Hx_4}$.

**Exercise 5.** A toy fluid (an illustration) has $w_3 - w_t = 1/3$ on the history $a_4 = AHx_4$ with $H = 0.25$. Compute $\rho(8)/\rho(0)$ for $A = 1$ and for $A = -1$, and their product.

*Answer.* $\rho(x_4)/\rho(0) = e^{-3AH(w_3 - w_t)x_4}$. For $A = 1$ the exponent at $x_4 = 8$ is $-3\cdot 0.25\cdot\frac13\cdot 8 = -2$, so the ratio is $e^{-2} = 0.135335$, the number of Notebook 09b. For $A = -1$ it is $e^{2} = 7.389056$. The product is $e^{-2}e^{2} = 1$: reversing the history reverses the energy flow.

**Exercise 6.** Suppose $p_3 + p_t = P$ is a constant and the hidden pressure $p_8$ stays finite as $z \to 0$. Show that $p_8 = P/2$ everywhere.

*Answer.* By Section 9.11 every solution of the $x_8$ balance is $p_8 = P/2 + c/\sin z$ with a constant $c$. As $z \to 0$, $\sin z \to 0$, so $c/\sin z$ grows without bound unless $c = 0$. A finite $p_8$ therefore needs $c = 0$, and then $p_8 = P/2$ at every $z$.

**Exercise 7.** Show that the kinetic term $K_\mu$ is a real number.

*Answer.* Let $Y = \bar\Phi\gamma^{(\mu)}\partial_\mu\Phi = \Phi^\dagger(C\gamma^{(\mu)})\partial_\mu\Phi$. Since $C\gamma^{(\mu)}$ is real, $Y^* = \Phi^T(C\gamma^{(\mu)})(\partial_\mu\Phi)^*$. A single number equals its transpose, so $Y^* = (\partial_\mu\Phi)^\dagger(C\gamma^{(\mu)})^T\Phi$; since $C\gamma^{(\mu)}$ is antisymmetric, $Y^* = -(\partial_\mu\Phi)^\dagger C\gamma^{(\mu)}\Phi = -\partial_\mu\bar\Phi\,\gamma^{(\mu)}\Phi$ (because $\partial_\mu\bar\Phi = (\partial_\mu\Phi)^\dagger C$). Hence $\bar\Phi\gamma^{(\mu)}\partial_\mu\Phi - \partial_\mu\bar\Phi\gamma^{(\mu)}\Phi = Y + Y^*$, which is twice the real part of $Y$, and $K_\mu = (Y + Y^*)/(2f_\mu)$ is real.

**Exercise 8.** Use the derivation of Section 9.26 to show that the entry $T^{x_1}{}_{x_5}$ of a condensate vanishes at every moment at which $a_4' = 0$, and evaluate its coefficient at $a_4 = 0.5$, $a_4' = 0.25$. Which number of Notebook 09c does it reproduce?

*Answer.* Section 9.26 gives $T^{x_1}{}_{x_5} = \frac12e^{-2a_4}a_4'\,\bar\Phi\gamma^{(1)}\gamma^{(4)}\gamma^{(5)}\Phi$, which is zero when $a_4' = 0$ (the $H$ terms of $K^{x_1}{}_{x_5}$ and of $g^{11}g_{55}K^{x_5}{}_{x_1}$ cancel exactly). At $a_4 = 0.5$, $a_4' = 0.25$ the coefficient is $\frac12e^{-1}\cdot 0.25 = 0.5\cdot 0.367879\cdot 0.25 = 0.045985$. Notebook 09c prints `T^x1_x5 = -(-0.045985) x its bilinear` in In [9], and In [7] shows that $T^{x_1}{}_{x_5}$ is proportional to $a_4'$.

**Exercise 9.** For the plane wave of Section 9.21 with $m = 2$ and $(k_1, k_2, k_3, k_8) = (1, 2, 0, 4)$, find the positive frequency $E$ and the energy density of a wave whose unit column satisfies $Bu = -u$. What is the energy density of the same wave multiplied by 10?

*Answer.* $h^2 = (m^2 + k_1^2 + k_2^2 + k_3^2 + k_8^2)\cdot 1 = (4 + 1 + 4 + 0 + 16)\cdot 1 = 25$, so $E = 5$. With $\rho = E\,u^\dagger Bu$ and $u^\dagger Bu = -u^\dagger u = -1$: $\rho = -5$. Multiplying the wave by 10 multiplies every bilinear by $10^2 = 100$: $\rho = -500$. There is no lower bound.
