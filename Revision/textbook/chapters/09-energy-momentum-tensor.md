## 9. The energy-momentum tensor, pressures, equations of state, conservation identities

Gravity has to be told where the energy is. In Einstein's theory, and in the Einstein-Lovelock theory that Chapter 12 uses for the author's metric, the right-hand side of the field equations is a table of numbers called the energy-momentum tensor. It says, at every point, how much energy there is in a unit of volume, how hard the matter pushes in each direction (the pressures), and how energy and momentum flow. This chapter builds that table for the field dirac16complex00 in the author's corrected metric of 2026-10-16, splits it into a kinetic part and a potential part, defines the energy density, the pressures of 3-space, of the extra times and of the hidden direction, and the equations of state, and derives the two exact conservation identities that the table obeys: one along the time $x_4$, which says how the inflating 3-space and the deflating block of the hidden direction and the extra times each change the energy density, and how the growth of the proper 7-volume dilutes it, and one along the hidden direction $x_0$, which balances the pressure of the hidden direction against the pressure of the extra times. Three notebooks compute every statement anew from the Revision record: Notebook 09a builds the tensor at one point and derives the two identities, Notebook 09b studies the condensates (fields that depend on the time only) and their equations of state, and Notebook 09c computes the complete tensor of a condensate, including the entries off the diagonal that the spin connection and the gravitational term of the field equation create.

### 9.1 What this chapter does

**Why we need this chapter.** Cosmologists describe the matter of the universe, at each moment, by two numbers: the **energy density** $\rho$ (energy per unit volume) and the **pressure** $p$ (the push per unit area, which is also energy per unit volume). Their ratio $w = p/\rho$ is called the **equation of state**. Three values are famous: dust (matter at rest whose particles do not push on each other) has $w = 0$, radiation (light) has $w = 1/3$, and a cosmological constant (the simplest model of dark energy) has $w = -1$. **Dark energy** is the name for the unknown cause of the observed speeding-up of the expansion of the universe, and **dark matter** for the unseen matter that is detected only through its gravity. The author's two hypotheses, called Hypothesis (for dirac16complex) and Hypothesis00 (for dirac16complex00), say that these fields might provide a time-varying equation of state for dark energy or dark matter (they are HYPOTHESES; the Revision record investigates them and establishes neither, Chapter 22; this chapter does not test them). Before anyone can test such a statement, one must know exactly what $\rho$ and $p$ are for these fields in the author's eight-dimensional metric. That is what this chapter derives.

**What it does.** In eight dimensions there is one energy density and seven pressures, one for each direction other than the time $x_4$. They come in three families: the pressure $p_3$ of the three directions of ordinary space, the pressure $p_t$ of the three extra times, and the pressure $p_0$ of the hidden direction. The chapter

- defines the energy-momentum tensor by the response of the action to a change of the metric, and derives from this definition, line by line, its diagonal entries $T^\mu{}_\mu = L_0 - K_\mu$ (Section 9.5);
- states the tensor that a variation of the vielbein gives and its symmetric part, the complete tensor used in this book, says when the two agree, and proves that the complete tensor is real and that its lowered form is symmetric (Section 9.6);
- splits the energy density and the pressures into kinetic and potential parts and defines the equations of state (Section 9.7);
- derives the trace identity and the values that the field equation imposes (Section 9.8);
- derives the 21 Christoffel symbols of the corrected metric, the covariant divergence of a diagonal tensor and from it the two conservation identities (Sections 9.9 to 9.11);
- shows where the spin connection, which drops out of the Lagrangian, does enter the tensor (Section 9.12);
- builds the condensates (the record reduces them to a linear system of 16 equations, which the notebook solves numerically), shows that their scalar is diluted like $e^{a_4}b_4^{-2}$, the inverse of the growth of the 7-volume, computes their equation of state $w = x/(2 + x)$ with $x = \lambda S/m$, which therefore changes in time, shows that the growing gravitational coefficient of the deflating history makes every condensate grow at late times, and that the energy of the commuting field has no lower bound (Sections 9.18 to 9.21);
- computes the complete tensor of a condensate, with 36 entries off the diagonal, and the exact condensates whose tensor is diagonal on the histories along which $e^{2a_4}/b_4$ is constant (Section 9.26).

**What it does not do.** The equation of state that an observer living in 3-space would infer (after integrating over the hidden direction and the extra times), its change in time and any comparison with supernova data (the measured brightness of distant exploding stars, from which astronomers infer the equation of state of dark energy) are not computed in this chapter (Section 9.19 quotes the record's result for a condensate). The Revision record computes them in `Revision/dark_sector/` (written up in `Revision/docs/DARK_SECTOR_HYPOTHESES.md`; COMPUTED, and taught in Chapter 22) under an ASSUMED normalisation of the observer's energy density over the extra times and the hidden direction (three definitions, called A, B and C), compares them with the supernova fit values of a document of the author (the record calls them the Unite values), and establishes neither hypothesis. Which normalisation, if any, describes a physical observer, and a fit to the supernova data themselves, are OPEN. The anticommuting field dirac16complex obeys the same formulas in its Grassmann algebra; for the quantised field the record defines the tensor as a normal-ordered operator, on a positive space of states constructed only for single good-sector momenta with frozen coefficients, and for $\lambda \neq 0$ it verifies the operator form of the on-shell identity only in a finite model under Wick ordering (Section 9.13 explains these words and states these limits exactly); this chapter computes numbers only for the commuting field dirac16complex00.

**Labels.** As everywhere in the book, every statement carries one of five labels: PROVED (exact; the Revision report file and the name of its check are given), COMPUTED (a number of a notebook, with its accuracy), ASSUMED, HYPOTHESIS, OPEN.

### 9.2 The stage: coordinates, metric and the field dirac16complex00

**Coordinates.** The eight coordinates are named and ordered as the author names them: $x_0$ is the **hidden** space direction, listed first; $x_1, x_2, x_3$ are ordinary 3-space; $x_4$ is the time in which everything evolves; $x_5, x_6, x_7$ are the three **extra times**, which behave like time and deflate exponentially on the history of the record. We write $z = 6Hx_0$, where $H > 0$ is the author's constant; $z$ takes every real value. In formulas the letter $i$ always stands for one of the 3-space directions $x_1, x_2, x_3$, and the letter $t$ for one of the extra times $x_5, x_6, x_7$.

**The metric.** The author's corrected metric of 2026-10-16 (Chapter 3; the metric of 2026-10-14 was withdrawn on 2026-10-16) is diagonal. We write it with eight **vielbein factors** $f_0, \dots, f_7$:

$$
g = \mathrm{diag}\big(f_0^2,\, f_1^2,\, f_2^2,\, f_3^2,\, -f_4^2,\, -f_5^2,\, -f_6^2,\, -f_7^2\big),
$$

$$
\begin{aligned}
&f_0 = s_b\cot z, \quad f_1 = f_2 = f_3 = e^{a_4}, \quad f_4 = 1, \quad f_5 = f_6 = f_7 = s_bW, \\
&s_b = e^{-a_4}b_4^{1/2}, \qquad W = (\sin^2 z)^{1/12} .
\end{aligned}
$$

Here $a_4(x_4)$ and $b_4(x_4) > 0$ are the two functions of the time in the author's metric (Chapter 3); $s_b$ is the **hidden scale**, the time-dependent factor that the hidden direction and the three extra times share, and $W = |\sin z|^{1/6}$ is the **warp factor** of the extra times, the positive twelfth root of $\sin^2 z$, defined for every real $z$. The factor $f_0$ keeps the sign of $\cot z$; only its square enters the metric. So $g_{x_0x_0} = e^{-2a_4}b_4\cot^2 z$, $g_{x_1x_1} = e^{2a_4}$, $g_{x_4x_4} = -1$ and $g_{x_5x_5} = -e^{-2a_4}b_4(\sin^2 z)^{1/6}$, exactly the author's entries (PROVED; `Revision/theory/reports/python-field-theory.json`, check `metric_from_vielbein_equals_SPEC`). A small step $dx_\mu$ along the direction $x_\mu$ has the proper length $|f_\mu|\,|dx_\mu|$; that is the meaning of $f_\mu$. With the frame metric $\eta = \mathrm{diag}(+1, +1, +1, +1, -1, -1, -1, -1)$ in the order $x_0, \dots, x_7$ every entry is $g_{\mu\mu} = \eta_{\mu\mu}f_\mu^2$: four space-like and four time-like directions, the signature (4,4), wherever $\sin z\cos z \neq 0$. The metric degenerates at the **folds** $\cos z = 0$ (for example $z = \pi/2$; there $g_{x_0x_0} = 0$, and the two halves $z < \pi/2$ and $z > \pi/2$ of a cell meet) and at the **tips** $\sin z = 0$ (there $g_{x_tx_t} = 0$); every statement of this chapter is made between these points. Every formula of this chapter holds for all functions $a_4$ and $b_4$, and the record's energy-momentum checks are made with both functions general (`Revision/theory/reports/wolfram-field-theory.json`).

**The two rates.** We write $a_4' = da_4/dx_4$, $b_4' = db_4/dx_4$ and $u = b_4'/b_4$. When $a_4$ grows, the 3-space factor $e^{a_4}$ grows (3-space **inflates**) at the rate $a_4'$; it does not depend on $x_0$ at all (3-space has no warp). The hidden direction and the extra times change together, at the rate

$$
h_4 = \frac{d}{dx_4}\ln s_b = \frac{d}{dx_4}\Big(-a_4 + \tfrac12\ln b_4\Big) = -a_4' + \frac{b_4'}{2b_4} = \frac{u}{2} - a_4' ;
$$

the first step is the definition of the rate of a scale factor, the second takes the logarithm of $s_b = e^{-a_4}b_4^{1/2}$ ($\ln(e^{-a_4}) = -a_4$, $\ln(b_4^{1/2}) = \frac12\ln b_4$), the third differentiates ($\frac{d}{dx_4}\ln b_4 = b_4'/b_4$). They **deflate** (shrink) together where $h_4 < 0$. We call the four directions $x_0, x_5, x_6, x_7$ the **block**. The examples of this chapter take the history of the record, $a_4 = AHx_4$ and $b_4 = b_4(0)\,e^{\beta AHx_4}$ with $A = 1$ and $\beta = \frac43$ (the prescribed background that the Kohn-Sham part of the book uses; Chapter 12 shows that it needs a source). On it $a_4' = AH$, $u = \beta AH = \frac43AH$ and $h_4 = \frac23AH - AH = -\frac{AH}{3}$: with $b_4(0) = 1$ the hidden scale is $s_b = e^{-AHx_4/3}$, and the block shrinks at a third of the rate at which 3-space grows. Notebook 09c also uses a curved history, $a_4 = 0.3x_4 + 0.05x_4^2$ and $b_4 = e^{0.4x_4 - 0.02x_4^2}$; every identity of the chapter holds for all functions $a_4$ and $b_4$. Which $a_4$ and $b_4$ the field equations of gravity allow, and with which source, is the subject of Chapter 12.

**The volume factor.** The absolute value of the product of the eight factors is the volume factor $\sqrt{|g|}$ (the square root of the absolute value of the determinant of the diagonal matrix $g$, which is the product of its diagonal entries):

$$
\begin{aligned}
\sqrt{|g|} &= |f_0|\, f_1 f_2 f_3\, f_4\, f_5 f_6 f_7 \\
&= s_b|\cot z| \cdot \big(e^{a_4}\big)^3 \cdot 1 \cdot \big(s_bW\big)^3 \\
&= s_b^4\, e^{3a_4}\,|\cot z|\,W^3 \\
&= e^{-4a_4}b_4^2\,e^{3a_4}\,|\cot z|\,(\sin^2 z)^{1/4} \\
&= e^{-a_4}b_4^2\,|\cot z|\,(\sin^2 z)^{1/4} .
\end{aligned}
$$

The first line is the definition ($|g| = \prod_\mu f_\mu^2$, whose square root is $\prod_\mu|f_\mu|$, and only $f_0$ can be negative); the second inserts the factors; the third collects the powers of $s_b$ ($s_b \cdot s_b^3 = s_b^4$); the fourth uses $s_b^4 = (e^{-a_4})^4(b_4^{1/2})^4 = e^{-4a_4}b_4^2$ and $W^3 = (\sin^2 z)^{3/12} = (\sin^2 z)^{1/4}$; the fifth uses $e^{-4a_4}e^{3a_4} = e^{-a_4}$ (PROVED; `Revision/theory/reports/python-field-theory.json`, check `sqrt_det_g`). The volume factor vanishes at the folds (where $\cot z = 0$). Its rate of change in time is

$$
\partial_4\ln\sqrt{|g|} = \partial_4\big(-a_4 + 2\ln b_4\big) = -a_4' + 2u = 3a_4' + 4h_4 ;
$$

the first step keeps the terms of $\ln\sqrt{|g|}$ that depend on $x_4$, the second differentiates, and the third checks $3a_4' + 4(\frac{u}{2} - a_4') = 2u - a_4'$: three 3-space directions at the rate $a_4'$ and four block directions at the rate $h_4$. On the history $2u - a_4' = \frac83AH - AH = \frac53AH$: at fixed $x_0$ the proper 7-volume grows like $e^{(5/3)AHx_4}$, although the block shrinks, because 3-space grows faster.

**The gamma matrices.** The book uses the author's eight **real** $16 \times 16$ gamma matrices (Chapter 4), stored in the Revision fixture `Revision/algebra/gammas.json` in the order $x_0, \dots, x_7$. We write them $\gamma^{(0)}, \dots, \gamma^{(7)}$ ($\gamma^{(4)}$ means $\gamma^{(x_4)}$, and so on). They obey the Clifford relations $\gamma^{(a)}\gamma^{(b)} + \gamma^{(b)}\gamma^{(a)} = 2\eta^{ab}\cdot 1$. Two consequences are used again and again in this chapter: the square of each gamma is $\eta_{aa}$ times the unit matrix ($+1$ for $x_0, x_1, x_2, x_3$ and $-1$ for $x_4, \dots, x_7$), and two different gammas anticommute, $\gamma^{(a)}\gamma^{(b)} = -\gamma^{(b)}\gamma^{(a)}$ for $a \neq b$. The matrix $C = \gamma^{(0)}\gamma^{(1)}\gamma^{(2)}\gamma^{(3)}$ (Chapter 5) is real and symmetric, $C^2 = 1$, and every product $C\gamma^{(a)}$ is antisymmetric: $(C\gamma^{(a)})^T = -C\gamma^{(a)}$ (PROVED; `Revision/algebra/reports/python-algebra.json`, checks `clifford_relation`, `C_real_symmetric_involution` and `C_gamma_antisymmetric`). The **coordinate gammas** are $\gamma^\mu = \gamma^{(\mu)}/f_\mu$ (no sum), and with a lower index $\gamma_\mu = g_{\mu\mu}\gamma^\mu = \eta_{\mu\mu}f_\mu\gamma^{(\mu)}$.

**The field.** dirac16complex00 is a column $\Phi$ of 16 ordinary (commuting) complex numbers at every point (Chapter 7). Its **Dirac adjoint** is the row $\bar\Phi = \Phi^\dagger C$ (the dagger means: transpose and take the complex conjugate of every entry), and the **scalar** is the number $S = \bar\Phi\Phi = \Phi^\dagger C\Phi$. A number of the form $\bar\Phi M\Phi$, with a fixed $16 \times 16$ matrix $M$, is called a **bilinear** of the field (it contains the field twice: once in the row $\bar\Phi$ and once in the column $\Phi$); $S$ is the simplest bilinear, with $M = 1$. The potential is $U(S) = \frac{\lambda}{2}S^2$, so $U'(S) = \lambda S$; $m$ is the mass.

**The spin connection and the covariant derivative** (Chapters 6 and 8). For the diagonal vielbein of the corrected metric the spin connection is

$$
\begin{aligned}
\Omega_{x_0} &= \tfrac12 h_4\,s_b\cot z\;\gamma^{(0)}\gamma^{(4)}, \qquad \Omega_{x_i} = \tfrac12 a_4'\,e^{a_4}\;\gamma^{(i)}\gamma^{(4)} \quad (i = 1, 2, 3), \qquad \Omega_{x_4} = 0, \\
\Omega_{x_t} &= \tfrac12 W\big(h_4\,s_b\;\gamma^{(4)}\gamma^{(t)} + H\;\gamma^{(0)}\gamma^{(t)}\big) \quad (t = 5, 6, 7)
\end{aligned}
$$

(Revision record `Revision/theory/field-theory.json`, formula `Omega_components`; `Revision/theory/reports/wolfram-field-theory.json`, check `Omega_components`). Each component is a rate times a factor: the 3-space directions tilt towards the time with the rate $a_4'$, the hidden direction and the extra times with the common rate $h_4$ of the block, and the extra times turn towards the hidden direction with the rate $H$ of their warp. The covariant derivatives are $D_\mu\Phi = \partial_\mu\Phi + \Omega_\mu\Phi$ and $D_\mu\bar\Phi = \partial_\mu\bar\Phi - \bar\Phi\,\Omega_\mu$, where $\partial_\mu$ is the partial derivative with respect to $x_\mu$.

**The Lagrangian.** The Lagrangian density is $\mathcal{L} = \sqrt{|g|}\,L_0$ with

$$
L_0 = \tfrac12\sum_\mu\big(\bar\Phi\gamma^\mu D_\mu\Phi - (D_\mu\bar\Phi)\gamma^\mu\Phi\big) - mS - U(S),
$$

and its Euler-Lagrange equation is the **field equation** $\gamma^\mu D_\mu\Phi = V\Phi$ with the **effective mass** $V = m + U'(S) = m + \lambda S$ (Chapter 7). Written out in the corrected metric (record formula `field_equation`; the sum $\gamma^\mu\Omega_\mu$ is Fact 2 of Section 9.3) it reads

$$
\sum_{a=0}^{7}\frac{1}{f_a}\,\gamma^{(a)}\partial_a\Phi + c_g\gamma^{(0)}\Phi + v_g\gamma^{(4)}\Phi = V\Phi , \qquad c_g = \tfrac32He^{a_4}b_4^{-1/2}, \qquad v_g = \frac{b_4'}{b_4} - \frac{a_4'}{2},
$$

with the **gravitational coefficients** $c_g$ (of the hidden direction) and $v_g$ (of the time). Because $(\gamma^{(4)})^2 = -1$ and $f_4 = 1$ it can be solved for the time derivative (the **evolution form**, record formula `evolution_form`): multiply by $-\gamma^{(4)}$, which turns $\gamma^{(4)}\partial_4\Phi$ into $\partial_4\Phi$ and $v_g\gamma^{(4)}\Phi$ into $v_g\Phi$, and move every other term to the right:

$$
\partial_4\Phi = -\gamma^{(4)}\Big[V\Phi - \sum_{a \neq 4}\frac{1}{f_a}\,\gamma^{(a)}\partial_a\Phi - c_g\gamma^{(0)}\Phi\Big] - v_g\Phi .
$$

A configuration that satisfies the field equation is said to be **on shell**; one that need not satisfy it is **off shell**. Some identities of this chapter hold off shell (for every configuration), others only on shell; each statement says which.

### 9.3 Two exact facts about the spin connection of this metric

Two facts about $\Omega_\mu$ decide where the spin connection appears in the energy-momentum tensor. Both are proved here line by line.

**Fact 1: for every direction separately, $\gamma^\mu\Omega_\mu + \Omega_\mu\gamma^\mu = 0$ (no sum).** For $x_4$ this is clear, because $\Omega_{x_4} = 0$. Take the hidden direction $x_0$:

$$
\begin{aligned}
\gamma^{x_0}\Omega_{x_0} &= \frac{\gamma^{(0)}}{s_b\cot z}\cdot\tfrac12 h_4\,s_b\cot z\;\gamma^{(0)}\gamma^{(4)} = \tfrac12 h_4\,\gamma^{(0)}\gamma^{(0)}\gamma^{(4)} = \tfrac12 h_4\,\gamma^{(4)}, \\
\Omega_{x_0}\gamma^{x_0} &= \tfrac12 h_4\,\gamma^{(0)}\gamma^{(4)}\gamma^{(0)} = -\tfrac12 h_4\,\gamma^{(0)}\gamma^{(0)}\gamma^{(4)} = -\tfrac12 h_4\,\gamma^{(4)} .
\end{aligned}
$$

The first line inserts $\gamma^{x_0} = \gamma^{(0)}/f_0$ and $\Omega_{x_0}$, cancels the factor $s_b\cot z$ against its inverse (its sign cancels too) and uses $\gamma^{(0)}\gamma^{(0)} = \eta_{00} = +1$; the second does the same insertion in the other order, exchanges the last two gammas, which costs a minus sign because different gammas anticommute, and uses $\gamma^{(0)}\gamma^{(0)} = 1$ again. The sum is zero. A 3-space direction $x_i$, with $\gamma^{x_i} = \gamma^{(i)}/e^{a_4}$:

$$
\begin{aligned}
\gamma^{x_i}\Omega_{x_i} &= \frac{\gamma^{(i)}}{e^{a_4}}\cdot\tfrac12 a_4'e^{a_4}\,\gamma^{(i)}\gamma^{(4)} = \tfrac12 a_4'\,\gamma^{(i)}\gamma^{(i)}\gamma^{(4)} = \tfrac12 a_4'\,\gamma^{(4)}, \\
\Omega_{x_i}\gamma^{x_i} &= \tfrac12 a_4'\,\gamma^{(i)}\gamma^{(4)}\gamma^{(i)} = -\tfrac12 a_4'\,\gamma^{(i)}\gamma^{(i)}\gamma^{(4)} = -\tfrac12 a_4'\,\gamma^{(4)},
\end{aligned}
$$

by the same three rules ($e^{a_4}$ cancels; one exchange of different gammas; $\gamma^{(i)}\gamma^{(i)} = +1$). The sum is zero. Now an extra time $x_t$, with $\gamma^{x_t} = \gamma^{(t)}/(s_bW)$:

$$
\begin{aligned}
\gamma^{x_t}\Omega_{x_t} &= \frac{\gamma^{(t)}}{s_bW}\cdot\tfrac12W\big(h_4\,s_b\,\gamma^{(4)}\gamma^{(t)} + H\,\gamma^{(0)}\gamma^{(t)}\big) \\
&= \tfrac12 h_4\,\gamma^{(t)}\gamma^{(4)}\gamma^{(t)} + \frac{H}{2s_b}\,\gamma^{(t)}\gamma^{(0)}\gamma^{(t)} \\
&= -\tfrac12 h_4\,\gamma^{(4)}\gamma^{(t)}\gamma^{(t)} - \frac{H}{2s_b}\,\gamma^{(0)}\gamma^{(t)}\gamma^{(t)} \\
&= \tfrac12 h_4\,\gamma^{(4)} + \tfrac12He^{a_4}b_4^{-1/2}\,\gamma^{(0)} .
\end{aligned}
$$

The first line inserts $\gamma^{x_t}$ and $\Omega_{x_t}$; the second cancels $W$ (and, in the first term, $s_b$); the third exchanges the first two gammas of each product (one minus sign each); the fourth uses $\gamma^{(t)}\gamma^{(t)} = \eta_{tt} = -1$ in both products and $1/s_b = e^{a_4}b_4^{-1/2}$. In the other order,

$$
\Omega_{x_t}\gamma^{x_t} = \tfrac12 h_4\,\gamma^{(4)}\gamma^{(t)}\gamma^{(t)} + \frac{H}{2s_b}\,\gamma^{(0)}\gamma^{(t)}\gamma^{(t)} = -\tfrac12 h_4\,\gamma^{(4)} - \tfrac12He^{a_4}b_4^{-1/2}\,\gamma^{(0)},
$$

where the products need no exchange and $\gamma^{(t)}\gamma^{(t)} = -1$ gives both minus signs. The sum is again zero, for all values of $h_4$ and $H$. Fact 1 is PROVED (Revision record `Revision/field_equations_a4/reports/wolfram-a4-report.json`, check `gamma_mu_anticommutes_with_Omega_mu_no_sum`), and so are the three values of $\gamma^\mu\Omega_\mu$ per direction found on the way (`Revision/theory/reports/python-field-theory.json`, check `per_direction_terms`; `Revision/theory/reports/wolfram-field-theory.json`, check `gammaOmega_per_direction`).

**Fact 2: summed over the directions, $\gamma^\mu\Omega_\mu = c_g\gamma^{(0)} + v_g\gamma^{(4)}$.** Add the results above: one hidden direction, three 3-space directions, three extra times (the direction $x_4$ gives zero):

$$
\begin{aligned}
\sum_\mu\gamma^\mu\Omega_\mu &= \tfrac12h_4\gamma^{(4)} + 3\cdot\tfrac12a_4'\gamma^{(4)} + 3\cdot\big(\tfrac12h_4\gamma^{(4)} + \tfrac12He^{a_4}b_4^{-1/2}\gamma^{(0)}\big) \\
&= \big(\tfrac32a_4' + 2h_4\big)\gamma^{(4)} + \tfrac32He^{a_4}b_4^{-1/2}\gamma^{(0)} \\
&= \Big(\frac{b_4'}{b_4} - \frac{a_4'}{2}\Big)\gamma^{(4)} + \tfrac32He^{a_4}b_4^{-1/2}\gamma^{(0)} = c_g\gamma^{(0)} + v_g\gamma^{(4)} .
\end{aligned}
$$

The first line adds the four kinds of contributions; the second collects the coefficients ($\frac12h_4 + 3\cdot\frac12h_4 = 2h_4$); the third inserts $h_4 = \frac{u}{2} - a_4'$, so that $\frac32a_4' + 2h_4 = \frac32a_4' + u - 2a_4' = u - \frac{a_4'}{2}$. Two readings. The term along the time is half the rate of the 7-volume: $v_g = \frac12(2u - a_4') = \frac12\partial_4\ln\sqrt{|g|}$ (Section 9.2); the three inflating 3-space directions contribute $+\frac32a_4'$ and the four directions of the block $2h_4$. The term along the hidden direction comes from the warp of the three extra times alone. On the history $c_g = \frac32He^{AHx_4/3}$ (in the unit $b_4(0) = 1$), which grows as the block deflates, and $v_g = \frac43AH - \frac12AH = \frac56AH$; at the point of Notebook 09a ($H = 0.25$, $A = 1$, $x_4 = 2$) they are $c_g = 0.375\,e^{1/6} = 0.443010$ and $v_g = 0.208333$ (COMPUTED in Notebook 09a, In [5]). All three statements are PROVED in the Revision record:

| statement | Revision report | check |
| --- | --- | --- |
| $\sum_\mu\gamma^\mu\Omega_\mu = c_g\gamma^{(0)} + v_g\gamma^{(4)}$ | `Revision/theory/reports/python-field-theory.json` | `gamma_mu_Omega_mu_equals_hidden_block_terms` |
| the same, computed independently by the lead | `Revision/lead_checks/reports/emt-divergence-and-spin-connection.json` | `gamma_Omega_equals_hidden_block_terms` |
| with a block that grew like 3-space the $a_4'$ coefficient would be $+\frac72$ instead of $-\frac12$ | `Revision/lead_checks/reports/emt-divergence-and-spin-connection.json` | `negative_control_growing_block` |

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

The spin connection has disappeared from the Lagrangian; it reaches the field equation only through Fact 2 (the terms $c_g\gamma^{(0)}\Phi + v_g\gamma^{(4)}\Phi$), and the energy-momentum tensor only off its diagonal (Section 9.12).

### 9.4 What an energy-momentum tensor is

**A table of $8 \times 8$ numbers.** The energy-momentum tensor $T^\nu{}_\mu$ is, at every point, a table of 64 numbers, one for each ordered pair of directions $(\nu, \mu)$. We write the upper index $\nu$ as the row and the lower index $\mu$ as the column. The entries on the diagonal ($\nu = \mu$) are the energy density and the pressures; the entries off the diagonal ($\nu \neq \mu$) describe flows: the entries with one index $x_4$ hold the density of momentum and the flow of energy along the other direction, and the entries with two indices other than $x_4$ hold shearing stresses. Lowering the upper index with the metric gives $T_{\nu\mu} = g_{\nu\nu}T^\nu{}_\mu$ (the metric is diagonal, so no sum is needed).

**A familiar example.** In ordinary four-dimensional flat space with the coordinates $(x_1, x_2, x_3, x_4)$, $x_4$ the time and the metric $\mathrm{diag}(1, 1, 1, -1)$, a gas at rest with energy density $\rho$ and pressure $p$ has $T^\nu{}_\mu = \mathrm{diag}(p, p, p, -\rho)$. The minus sign in front of $\rho$ comes from $g_{x_4x_4} = -1$: lowering the index gives $T_{x_4x_4} = g_{x_4x_4}T^{x_4}{}_{x_4} = \rho$, the energy density, as in every book on relativity.

**The conventions of the book** (Revision record, `Revision/SPEC.md` section 4; record formula `equation_of_state_definitions`): the energy density and the pressures are

$$
\rho = -T^{x_4}{}_{x_4}, \qquad p_\mu = T^\mu{}_\mu \;\; (\text{no sum}, \; \mu \neq x_4), \qquad p_3 = T^{x_1}{}_{x_1}, \quad p_t = T^{x_5}{}_{x_5}, \quad p_0 = T^{x_0}{}_{x_0},
$$

and the **equations of state** are the ratios

$$
w_3 = \frac{p_3}{\rho}, \qquad w_t = \frac{p_t}{\rho}, \qquad w_0 = \frac{p_0}{\rho} .
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
\mathcal{L} = \big(f_0 f_1\cdots f_7\big)\Big[\sum_a\frac{1}{2f_a}X_a - mS - U(S)\Big], \qquad X_a = \bar\Phi\gamma^{(a)}\partial_a\Phi - \partial_a\bar\Phi\,\gamma^{(a)}\Phi .
$$

The numbers $X_a$, $S$ and $U(S)$ contain no vielbein factor ($\Phi$ is held fixed and the frame gammas $\gamma^{(a)}$ are constant matrices), so only two places change: the product $f_0\cdots f_7$ becomes $(1 + \varepsilon)f_0\cdots f_7$, and the coefficient $1/(2f_b)$ becomes $1/(2f_b(1 + \varepsilon))$. To first order $1/(1 + \varepsilon) = 1 - \varepsilon$ (the series $1/(1 + \varepsilon) = 1 - \varepsilon + \varepsilon^2 - \dots$, cut after the first order). Therefore, with $K_a = X_a/(2f_a)$,

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
T^b{}_b = L_0 - K_b \qquad (\text{no sum}, \; b = x_0, \dots, x_7).
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
| hidden pressure $p_0 = T^{x_0}{}_{x_0}$ | $\sum_{\mu \neq x_0}K_\mu$ | $-(mS + U)$ | $\sum_{\mu \neq x_0}K_\mu - mS - U$ |

Four remarks.

- The time derivative $\partial_4\Phi$ does not occur in $\rho$: the kinetic term $K_4$ cancels. As for Dirac's electron field, the field equation is of first order in time, and its energy is fixed by the derivatives along the other seven directions and by the potential.
- Each kinetic term carries the weight $1/f_\mu$: $e^{-a_4}$ along 3-space (it shrinks as 3-space inflates, and it does not depend on $z$), $1$ along the time, $e^{a_4}b_4^{-1/2}(\sin^2 z)^{-1/12}$ along the extra times and $e^{a_4}b_4^{-1/2}\tan z$ along the hidden direction (both grow as the block deflates, on the history like $e^{AHx_4/3}$; the hidden weight grows without bound towards the fold $z = \pi/2$). Figure 09a.1 of Notebook 09a draws the sizes of these weights.
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

**The Christoffel symbols of the corrected metric.** For a metric the symbols are $\Gamma^\lambda{}_{\mu\nu} = \frac12\sum_\rho g^{\lambda\rho}(\partial_\mu g_{\rho\nu} + \partial_\nu g_{\rho\mu} - \partial_\rho g_{\mu\nu})$. For a diagonal metric only $\rho = \lambda$ survives and

$$
\Gamma^\lambda{}_{\mu\nu} = \frac{1}{2g_{\lambda\lambda}}\big(\partial_\mu g_{\lambda\nu} + \partial_\nu g_{\lambda\mu} - \partial_\lambda g_{\mu\nu}\big) \qquad (\text{no sum over } \lambda).
$$

The symbol is symmetric in $\mu$ and $\nu$. The entries of the metric depend only on $x_4$ (through $a_4$ and $b_4$) and on $x_0$ (through $z = 6Hx_0$, whose derivative is $dz/dx_0 = 6H$). Two derivatives are used again and again: with $g_{00} = s_b^2\cot^2 z$ and $g_{tt} = -s_b^2W^2$,

$$
\partial_4 g_{00} = 2s_b\,(\partial_4 s_b)\cot^2 z = 2h_4\,g_{00}, \qquad \partial_4 g_{tt} = 2h_4\,g_{tt}, \qquad \partial_0 g_{tt} = 2\,(\partial_0\ln W)\,g_{tt} = 2H\cot z\;g_{tt} ;
$$

the first is the product rule with $\partial_4 s_b = h_4 s_b$ (the definition of $h_4$ in Section 9.2), the second is the same for $g_{tt}$, and the third uses $\partial_0 Q = (\partial_0\ln Q)\,Q$ and $\partial_0\ln W = \frac{1}{12}\,\partial_0\ln\sin^2 z = \frac{1}{12}\cdot\frac{2\sin z\cos z}{\sin^2 z}\cdot 6H = H\cot z$ (the chain rule with $dz/dx_0 = 6H$). Six symbols, computed line by line:

- $\Gamma^{x_1}{}_{x_1x_4} = \frac{1}{2g_{11}}\partial_4 g_{11} = \frac12\,\partial_4\ln g_{11} = \frac12\,\partial_4\big(2a_4\big) = a_4'$; the first step keeps the only nonzero derivative, the second uses $\partial(\ln Q) = \partial Q/Q$, the third writes $\ln g_{11} = \ln e^{2a_4} = 2a_4$ (3-space has no warp), and the last differentiates.
- $\Gamma^{x_4}{}_{x_1x_1} = \frac{1}{2g_{44}}\big(-\partial_4 g_{11}\big) = \frac{1}{-2}\big(-2a_4'e^{2a_4}\big) = a_4'\,e^{2a_4}$; only the third term of the bracket survives ($g_{41} = 0$), $g_{44} = -1$, and the chain rule gives $\partial_4 e^{2a_4} = 2a_4'e^{2a_4}$.
- $\Gamma^{x_4}{}_{x_0x_0} = \frac{1}{2g_{44}}\big(-\partial_4 g_{00}\big) = \frac12\,\partial_4 g_{00} = h_4\,g_{00} = h_4\,e^{-2a_4}b_4\cot^2 z$; only the third term survives ($g_{40} = 0$), $g_{44} = -1$ turns $-\frac{1}{2}\cdot(-1)$ into $+\frac12$, and $\partial_4 g_{00} = 2h_4 g_{00}$. In the corrected metric the hidden direction changes in time, so this symbol is not zero.
- $\Gamma^{x_0}{}_{x_0x_0} = \frac12\,\partial_0\ln g_{00} = \partial_0\ln|\cot z| = 6H\cdot\frac{-1/\sin^2 z}{\cot z} = -\frac{6H}{\sin z\cos z} = -\frac{12H}{\sin(12Hx_0)}$; the first step is the diagonal formula with $\lambda = \mu = \nu$ (all three terms are $\partial_0 g_{00}$, with signs $+, +, -$), the second drops $s_b^2$, which does not depend on $x_0$, and uses $\frac12\ln\cot^2 z = \ln|\cot z|$, the third uses $\frac{d}{dz}\cot z = -1/\sin^2 z$ and the chain rule, the fourth $\cot z = \cos z/\sin z$, the fifth $2\sin z\cos z = \sin 2z$ with $2z = 12Hx_0$.
- $\Gamma^{x_4}{}_{x_5x_5} = \frac{1}{2g_{44}}\big(-\partial_4 g_{55}\big) = \frac12\,\partial_4 g_{55} = h_4\,g_{55} = -h_4\,e^{-2a_4}b_4(\sin^2 z)^{1/6}$; as for $\Gamma^{x_4}{}_{x_0x_0}$, now with $\partial_4 g_{55} = 2h_4 g_{55}$ and $g_{55} = -e^{-2a_4}b_4(\sin^2 z)^{1/6}$.
- $\Gamma^{x_0}{}_{x_5x_5} = \frac{1}{2g_{00}}\big(-\partial_0 g_{55}\big) = -\frac{H\cot z\;g_{55}}{g_{00}} = \frac{H\cot z\;s_b^2W^2}{s_b^2\cot^2 z} = HW^2\tan z = H(\sin^2 z)^{1/6}\tan z$; only the third term survives, $\partial_0 g_{55} = 2H\cot z\,g_{55}$, then $g_{55} = -s_b^2W^2$ and $g_{00} = s_b^2\cot^2 z$, and $s_b^2$ cancels and $\cot z/\cot^2 z = \tan z$.

The three remaining kinds, $\Gamma^{x_0}{}_{x_0x_4}$, $\Gamma^{x_t}{}_{x_0x_t}$ and $\Gamma^{x_t}{}_{x_4x_t}$, have the form of the first bullet, a logarithmic derivative of one diagonal entry; the lemma below gives each of them in one line, and Exercise 1 works two of them out in full. The directions $x_2, x_3$ give the same values as $x_1$, and $x_6, x_7$ the same values as $x_5$, because their entries of the metric are equal. The complete list of the nonzero symbols with $\mu \le \nu$ is (21 symbols; why there are exactly 21 is shown after the lemma below):

| symbol | value | symbol | value |
| --- | --- | --- | --- |
| $\Gamma^{x_0}{}_{x_0x_0}$ | $-12H/\sin(12Hx_0)$ | $\Gamma^{x_0}{}_{x_0x_4}$ | $h_4$ |
| $\Gamma^{x_4}{}_{x_0x_0}$ | $h_4\,e^{-2a_4}b_4\cot^2 z$ | $\Gamma^{x_0}{}_{x_tx_t}$ | $HW^2\tan z$ |
| $\Gamma^{x_i}{}_{x_ix_4}$ | $a_4'$ | $\Gamma^{x_4}{}_{x_ix_i}$ | $a_4'\,e^{2a_4}$ |
| $\Gamma^{x_t}{}_{x_4x_t}$ | $h_4$ | $\Gamma^{x_4}{}_{x_tx_t}$ | $-h_4\,e^{-2a_4}b_4W^2$ |
| $\Gamma^{x_t}{}_{x_0x_t}$ | $H\cot z$ | (none) | (none) |

Here $W^2 = (\sin^2 z)^{1/6}$. Each row with an $i$ or a $t$ stands for three symbols, so the count is $1 + 1 + 1 + 3 + 3 + 3 + 3 + 3 + 3 = 21$ (PROVED; `Revision/theory/field-theory.json`, formula `christoffel_nonzero`, and `Revision/theory/reports/wolfram-field-theory.json`, check `christoffel_count`. Notebook 09a computes the 21 symbols with sympy, for both signs of $\sin z$, and compares them with the record one by one.) Two things are worth noticing. The hidden direction follows the extra times in time: $\Gamma^{x_0}{}_{x_0x_4} = \Gamma^{x_t}{}_{x_4x_t} = h_4$. And 3-space does not see $x_0$: no symbol mixes $x_i$ with $x_0$.

**A lemma for diagonal metrics.** Set $\lambda = \mu$ in the formula above (no sum):

$$
\Gamma^\mu{}_{\mu\nu} = \frac{1}{2g_{\mu\mu}}\big(\partial_\mu g_{\mu\nu} + \partial_\nu g_{\mu\mu} - \partial_\mu g_{\mu\nu}\big) = \frac{\partial_\nu g_{\mu\mu}}{2g_{\mu\mu}} = \frac{2\eta_{\mu\mu}f_\mu\,\partial_\nu f_\mu}{2\eta_{\mu\mu}f_\mu^2} = \partial_\nu\ln|f_\mu| .
$$

The first and the third term of the bracket cancel; then $g_{\mu\mu} = \eta_{\mu\mu}f_\mu^2$ and the chain rule $\partial_\nu f_\mu^2 = 2f_\mu\partial_\nu f_\mu$; finally $\partial_\nu f_\mu/f_\mu = \partial_\nu\ln|f_\mu|$, which holds for a negative $f_\mu$ as well (the factor $f_0$ is negative where $\cot z < 0$). Summed over $\mu$ this gives $\sum_\mu\Gamma^\mu{}_{\mu\nu} = \partial_\nu\ln(|f_0|f_1\cdots f_7) = \partial_\nu\ln\sqrt{|g|}$. For example, $\Gamma^{x_5}{}_{x_0x_5} = \partial_0\ln f_5 = \partial_0\big(\ln s_b + \ln W\big) = 0 + H\cot z$, because $s_b$ does not depend on $x_0$ and $\partial_0\ln W = H\cot z$; and $\Gamma^{x_5}{}_{x_4x_5} = \partial_4\ln f_5 = \partial_4\ln s_b + \partial_4\ln W = h_4 + 0$, because $W$ does not depend on $x_4$.

**Why there are exactly 21 symbols.** Sort the symbols by how many of the three indices $\lambda, \mu, \nu$ are equal, and use the diagonal formula. Remember that the entries of the metric depend only on $x_4$ and $x_0$, that $g_{44} = -1$ is a constant, that $g_{00} = s_b^2\cot^2 z$ depends on both, that $g_{ii} = e^{2a_4}$ depends on $x_4$ only, and that $g_{tt} = -s_b^2W^2$ depends on both.

- Three different indices: every entry in the bracket, $g_{\lambda\nu}$, $g_{\lambda\mu}$ and $g_{\mu\nu}$, lies off the diagonal and is zero, so the symbol is zero.
- $\mu = \nu \neq \lambda$: the first two terms of the bracket contain $g_{\lambda\mu} = 0$, so $\Gamma^\lambda{}_{\mu\mu} = -\partial_\lambda g_{\mu\mu}/(2g_{\lambda\lambda})$. It is nonzero only when $g_{\mu\mu}$ depends on $x_\lambda$, so $\lambda$ is $x_4$ or $x_0$. For $\lambda = x_4$ the entries $g_{00}$, $g_{ii}$ and $g_{tt}$ depend on $x_4$ ($g_{44}$ is constant): $1 + 3 + 3 = 7$ symbols. For $\lambda = x_0$ only $g_{tt}$ depends on $x_0$ among the entries with $\mu \neq x_0$: 3 symbols. That makes 10.
- $\lambda$ equal to exactly one of $\mu$, $\nu$ (stored as $\Gamma^\lambda{}_{\lambda\nu}$ or $\Gamma^\lambda{}_{\nu\lambda}$, whichever has the smaller index first): by the lemma it is $\partial_\nu\ln|f_\lambda|$ with $\nu \neq \lambda$, nonzero only when $f_\lambda$ depends on $x_\nu$: for $\lambda = x_0$ with $\nu = x_4$ (1 symbol), for $\lambda = x_i$ with $\nu = x_4$ (3), for $\lambda = x_t$ with $\nu = x_4$ and with $\nu = x_0$ (6), and never for $\lambda = x_4$, because $f_4 = 1$. That makes another 10.
- All three equal: $\Gamma^\lambda{}_{\lambda\lambda} = \partial_\lambda\ln|f_\lambda|$ by the lemma, nonzero only for $\lambda = x_0$, since $f_0$ is the only factor that depends on its own coordinate. One symbol.

The total is $10 + 10 + 1 = 21$, the count of the table and of the record. The count is for general functions $a_4$ and $b_4$, as in the record; for special ones a symbol can vanish (for example the four symbols with the value $h_4$ and the four with a factor $h_4$ vanish at a moment where $h_4 = 0$, when the block neither grows nor shrinks).

**The divergence of a diagonal tensor.** Now let $T^\mu{}_\nu$ be diagonal: $T^\mu{}_\nu = 0$ for $\mu \neq \nu$. In each of the three sums of the divergence only the terms with a diagonal entry survive:

- first sum: only $\mu = \nu$, giving $\partial_\nu T^\nu{}_\nu$;
- second sum: only $\lambda = \nu$, giving $\sum_\mu\Gamma^\mu{}_{\mu\nu}T^\nu{}_\nu = \sum_\mu(\partial_\nu\ln|f_\mu|)\,T^\nu{}_\nu$;
- third sum: only $\lambda = \mu$, giving $\sum_\mu\Gamma^\mu{}_{\mu\nu}T^\mu{}_\mu = \sum_\mu(\partial_\nu\ln|f_\mu|)\,T^\mu{}_\mu$.

Both corrections use only the lemma. Subtracting the third from the second:

$$
\nabla_\mu T^\mu{}_\nu = \partial_\nu T^\nu{}_\nu + \sum_\mu\big(\partial_\nu\ln|f_\mu|\big)\big(T^\nu{}_\nu - T^\mu{}_\mu\big) \qquad (\text{diagonal } T, \text{ no sum over } \nu).
$$

This formula holds for every diagonal metric and every diagonal tensor. We apply it to the corrected metric and to

$$
T^\mu{}_\nu = \mathrm{diag}\big(p_0, p_3, p_3, p_3, -\rho, p_t, p_t, p_t\big) \qquad (\text{in the order } x_0, \dots, x_7),
$$

whose four entries are any functions of $x_4$ and $x_0$. The logarithmic derivatives we need are, from $\ln|f_0| = \ln s_b + \ln|\cot z|$, $\ln f_i = a_4$, $\ln f_4 = 0$ and $\ln f_t = \ln s_b + \ln W$:

$$
\begin{aligned}
&\partial_4\ln|f_0| = h_4, \qquad \partial_4\ln f_i = a_4', \qquad \partial_4\ln f_4 = 0, \qquad \partial_4\ln f_t = h_4, \\
&\partial_0\ln f_i = 0, \qquad \partial_0\ln f_4 = 0, \qquad \partial_0\ln f_t = H\cot z .
\end{aligned}
$$

(We shall not need $\partial_0\ln|f_0|$: in the component $\nu = x_0$ it multiplies $p_0 - p_0 = 0$.)

**The component $\nu = x_4$.** Here $T^{x_4}{}_{x_4} = -\rho$:

$$
\begin{aligned}
\nabla_\mu T^\mu{}_{x_4} &= \partial_4(-\rho) + h_4\big(-\rho - p_0\big) + 3a_4'\big(-\rho - p_3\big) + 3h_4\big(-\rho - p_t\big) \\
&= -\partial_4\rho - 3a_4'\big(\rho + p_3\big) - 3h_4\big(\rho + p_t\big) - h_4\big(\rho + p_0\big).
\end{aligned}
$$

The first line takes the hidden direction (weight $h_4$, entry $p_0$), the three 3-space directions (weight $a_4'$, entry $p_3$) and the three extra times (weight $h_4$, entry $p_t$); the direction $x_4$ has weight 0. The second takes the minus signs out of the brackets and orders the terms.

**The component $\nu = x_0$.** Here $T^{x_0}{}_{x_0} = p_0$. The direction $\mu = x_0$ gives $(p_0 - p_0) = 0$ whatever its weight, the directions $x_4$ and $x_i$ have weight 0, and only the three extra times remain:

$$
\nabla_\mu T^\mu{}_{x_0} = \partial_0 p_0 + 3H\cot z\,\big(p_0 - p_t\big).
$$

**The other six components.** For $\nu = x_1$ (and likewise $x_2, x_3, x_5, x_6, x_7$) every term contains a derivative $\partial_1$ of something that depends only on $x_4$ and $x_0$; all vanish: $\nabla_\mu T^\mu{}_{x_1} = 0$ identically.

These are exactly the record's statements (PROVED; the table lists the record files and checks). Notebook 09a derives them again with sympy, from the 21 Christoffel symbols and the general divergence formula, without using the lemma.

| statement | Revision record | formula or check |
| --- | --- | --- |
| all eight components of the divergence of a diagonal tensor | `Revision/theory/field-theory.json` | formula `energy_exchange` |
| the same, verified with the Wolfram Language and with sympy | `Revision/theory/reports/wolfram-field-theory.json` and `python-field-theory.json` | `energy_exchange_equation` |
| the $x_4$ component, computed independently by the lead | `Revision/lead_checks/reports/emt-divergence-and-spin-connection.json` | `divergence_x4_component` |
| the $x_0$ component, computed independently by the lead | the same report | `divergence_x0_component` |
| the other six components vanish | the same report | `divergence_other_components_zero` |

### 9.10 The x4 identity: energy exchange between 3-space and the block

Conservation of a diagonal tensor along $x_4$ is therefore

$$
\frac{\partial\rho}{\partial x_4} = -3a_4'\,\big(\rho + p_3\big) - 3h_4\,\big(\rho + p_t\big) - h_4\,\big(\rho + p_0\big).
$$

**What it says.** In ordinary cosmology the energy density of a gas falls as space expands, $d\rho/dt = -3\,(\dot a/a)\,(\rho + p)$ with the scale factor $a$: each of the three expanding directions dilutes $\rho$ plus the pressure of that direction at the rate $\dot a/a$. The identity has exactly this form, once for every direction: each 3-space direction changes $\rho$ by $-a_4'(\rho + p_3)$, each extra time by $-h_4(\rho + p_t)$, and the hidden direction by $-h_4(\rho + p_0)$. On the deflating history $h_4 < 0$, so the four shrinking directions of the block push the energy density up while the three inflating 3-space directions pull it down. Collecting the terms shows the two effects separately:

$$
\begin{aligned}
\frac{\partial\rho}{\partial x_4} &= -\big(3a_4' + 4h_4\big)\rho - 3a_4'p_3 - 3h_4p_t - h_4p_0 \\
&= -\big(3a_4' + 4h_4\big)\rho - 3a_4'p_3 - h_4\big(3p_t + p_0\big).
\end{aligned}
$$

The first line multiplies out and collects the four terms with $\rho$; the second collects the two terms with $h_4$. The first term is a **dilution** with the rate $3a_4' + 4h_4 = \partial_4\ln\sqrt{|g|}$ of the proper 7-volume (Section 9.2); the second is the **work** of the inflating 3-space, the third the work of the deflating block. For entries that do not depend on $x_0$ the $x_0$ identity of Section 9.11 requires $p_0 = p_t$, and then, adding and subtracting $3a_4'p_t$,

$$
\frac{\partial\rho}{\partial x_4} = -\big(3a_4' + 4h_4\big)\big(\rho + p_t\big) - 3a_4'\big(p_3 - p_t\big) ;
$$

(check: the right side is $-(3a_4' + 4h_4)\rho - 3a_4'p_t - 4h_4p_t - 3a_4'p_3 + 3a_4'p_t$, which is the previous line with $p_0 = p_t$). The last term is an **exchange** between 3-space and the block: on a history with $a_4' > 0$ it lowers the energy density when the 3-space pressure exceeds the block pressure and raises it when it is smaller; reversing the history ($A \to -A$ turns $a_4'$, $u$ and $h_4$ into their negatives) reverses every term. A source with $p_3 = p_t = p_0$ exchanges no energy and is only diluted. The derivation above and the sympy computation of Notebook 09a hold for all functions $a_4$ and $b_4$ (PROVED; record formula `energy_exchange` of `Revision/theory/field-theory.json`, the checks of the table at the end of Section 9.9).

**On the history.** With $a_4' = AH$, $h_4 = -\frac{AH}{3}$ and $3a_4' + 4h_4 = 3AH - \frac43AH = \frac53AH$ the identity reads $d\rho/dx_4 = -3AH(\rho + p_3) + AH(\rho + p_t) + \frac{AH}{3}(\rho + p_0)$, and with $p_0 = p_t$ it is $d\rho/dx_4 = -\frac53AH(\rho + p_t) - 3AH(p_3 - p_t)$.

**A first-law reading (an interpretation, not an extra result).** At fixed $x_0$ take a small box of coordinate size 1 along each of the seven directions other than $x_4$. Its 3-space volume is $V_3 = f_1f_2f_3 = e^{3a_4}$, its extra-time volume $V_t = f_5f_6f_7 = s_b^3W^3 = e^{-3a_4}b_4^{3/2}(\sin^2 z)^{1/4}$, its hidden length $V_0 = |f_0| = e^{-a_4}b_4^{1/2}|\cot z|$, and its 7-volume $V_7 = V_3V_tV_0 = e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4} = \sqrt{|g|}$. The first law of thermodynamics says that the energy of a box changes by minus the pressure times the change of its volume. Applied separately to the three families of directions, with each change of volume taken relative to the volume of its family,

$$
\frac{d}{dx_4}\big(\rho V_7\big) = -p_3\,\frac{V_7}{V_3}\frac{dV_3}{dx_4} - p_t\,\frac{V_7}{V_t}\frac{dV_t}{dx_4} - p_0\,\frac{V_7}{V_0}\frac{dV_0}{dx_4} .
$$

Divide by $V_7$. The left side becomes $\frac{d\rho}{dx_4} + \rho\,\frac{1}{V_7}\frac{dV_7}{dx_4} = \frac{d\rho}{dx_4} + (3a_4' + 4h_4)\rho$ (the product rule, and the rate of $V_7 = \sqrt{|g|}$ from Section 9.2), and the logarithmic derivatives on the right are $\frac{1}{V_3}\frac{dV_3}{dx_4} = 3a_4'$, $\frac{1}{V_t}\frac{dV_t}{dx_4} = 3h_4$ and $\frac{1}{V_0}\frac{dV_0}{dx_4} = h_4$. So $\frac{d\rho}{dx_4} = -(3a_4' + 4h_4)\rho - 3a_4'p_3 - 3h_4p_t - h_4p_0$, the conservation identity. While 3-space inflates ($dV_3 > 0$), a positive $p_3$ takes energy out of the box; while the block deflates ($dV_t < 0$, $dV_0 < 0$), positive $p_t$ and $p_0$ put energy in; and the growth of the 7-volume dilutes the energy density. Notebook 09a checks with sympy, for both signs of $\sin z$, that this reading is exactly the identity, and Figure 09a.4 draws the four volumes along the history: $V_3$ grows like $e^{3AHx_4}$, $V_t$ shrinks like $e^{-AHx_4}$, $V_0$ like $e^{-AHx_4/3}$, and $V_7$ grows like $e^{(5/3)AHx_4}$.

**Toy fluids (an ILLUSTRATION, not solutions of the field equations of this book).** Suppose a source had pressures proportional to its energy density, $p_3 = w_3\rho$ and $p_t = p_0 = w_t\rho$ with constants $w_3$, $w_t$, on the history ($p_0 = p_t$ is what the $x_0$ identity requires of entries that do not depend on $x_0$). With $\Delta w = w_3 - w_t$ the identity becomes

$$
\begin{aligned}
\frac{d\rho}{dx_4} &= -3AH(1 + w_3)\rho - 4\big(\tfrac{\beta}{2} - 1\big)AH(1 + w_t)\rho \\
&= -AH\big(3\Delta w + 3(1 + w_t) + (2\beta - 4)(1 + w_t)\big)\rho \\
&= -AH\big(3\Delta w + (2\beta - 1)(1 + w_t)\big)\rho = -AH\big(3\Delta w + \tfrac53(1 + w_t)\big)\rho .
\end{aligned}
$$

The first line inserts the pressures, $a_4' = AH$ and $h_4 = (\frac{\beta}{2} - 1)AH$ (the rate of $s_b = e^{(\beta/2 - 1)AHx_4}$); the second writes $1 + w_3 = \Delta w + (1 + w_t)$; the third collects $3 + 2\beta - 4 = 2\beta - 1$ and inserts $\beta = \frac43$. The rate of change of $\rho$ is a constant times $\rho$. The function $\rho_0e^{cx_4}$ has the derivative $c\,\rho_0e^{cx_4}$, so the solution with $\rho(0) = \rho_0$ is

$$
\rho(x_4) = \rho_0\,e^{-AH(3\Delta w + \frac53 + \frac53w_t)x_4} .
$$

With $A = 1$, $H = 0.25$, $\Delta w = 1/3$ and $w_t = 0$, at $x_4 = 8$ the exponent is $-0.25\cdot(1 + \frac53)\cdot 8 = -\frac{16}{3}$ and $\rho(8)/\rho(0) = e^{-16/3} = 0.004828$, the number that Notebook 09b computes with the Runge-Kutta method. With $w_t = 0$ the work and the dilution balance exactly at $\Delta w = -\frac59$. The condensates of Section 9.18 have $p_3 = p_t = p_0$: they exchange no energy and are only diluted, $d\rho/dx_4 = -(3a_4' + 4h_4)(\rho + p)$.

### 9.11 The x0 identity: the balance along the hidden direction

Conservation along $x_0$ is

$$
\frac{\partial p_0}{\partial x_0} = -3H\cot z\,\big(p_0 - p_t\big).
$$

It is a balance of pressures, like the balance of pressure and weight in a column of air: a change of the hidden pressure along $x_0$ must be paid for by the difference between $p_0$ and the extra-time pressure. The 3-space pressure does not take part, because nothing in 3-space depends on $x_0$; the extra times do, through their warp $W$.

**Entries that do not depend on $x_0$.** Then the left side is zero, and because $\cot z \neq 0$ between the folds the bracket must vanish:

$$
p_0 = p_t .
$$

What do the field equations of gravity say about the same pressures (Chapter 12 derives these equations)? In the corrected metric every Lovelock tensor is diagonal, free of $x_0$, and has equal hidden and extra-time entries, $E_{(k)}{}^{x_0}{}_{x_0} = E_{(k)}{}^{x_t}{}_{x_t}$. The field equations therefore require three things of a source: every off-diagonal entry vanishes, every diagonal entry is independent of $x_0$, and $\kappa(p_0 - p_t) = 0$, that is $p_0 = p_t$ (PROVED; the table names the record's entries and checks). Conservation and gravity ask for the same thing. This is no accident: the Lovelock tensors have zero divergence for every metric (Chapter 3), so their diagonal, $x_0$-independent table obeys the two identities of this chapter too, and with no $x_0$ dependence the $x_0$ identity is exactly $E_{(k)}{}^{x_0}{}_{x_0} = E_{(k)}{}^{x_t}{}_{x_t}$.

**The source of the record's history.** For the history $a_4 = Hx_4$, $b_4 = e^{(4/3)Hx_4}$ (that is $A = 1$ and $b_4(0) = 1$) the record of the corrected metric lists the source that the field equations require, as the diagonal table $\kappa T - \Lambda$ (the coupling $\kappa$ times the tensor, minus the cosmological constant $\Lambda$ on the diagonal). For Einstein's theory alone it is, with $k = e^{2a_4}/b_4 = e^{(2/3)Hx_4}$,

$$
-\rho = \frac{H^2}{3}\big(18k + 1\big), \qquad p_3 = \frac{H^2}{9}\big(54k - 13\big), \qquad p_t = p_0 = \frac{H^2}{3}\big(9k - 11\big),
$$

where $\rho$ and the pressures here stand for the entries of $\kappa T - \Lambda$. It is diagonal, free of $x_0$ and has $p_0 = p_t$, so the $x_0$ identity holds. Is the $x_4$ identity satisfied? The constant $\Lambda$ changes $\rho$ by $+\Lambda$ and every pressure by $-\Lambda$, so $\rho + p_3$, $\rho + p_t$ and $\partial_4\rho$ do not see it, and we may test the listed entries directly. Line by line, with $dk/dx_4 = \frac23Hk$, $a_4' = H$ and $h_4 = -\frac{H}{3}$:

$$
\begin{aligned}
\frac{d\rho}{dx_4} &= -\frac{H^2}{3}\cdot 18\cdot\frac23Hk = -4H^3k, \\
\rho + p_3 &= -6H^2k - \frac{H^2}{3} + 6H^2k - \frac{13H^2}{9} = -\frac{16H^2}{9}, \\
\rho + p_t &= -6H^2k - \frac{H^2}{3} + 3H^2k - \frac{11H^2}{3} = -3H^2k - 4H^2, \\
-3a_4'\big(\rho + p_3\big) - 4h_4\big(\rho + p_t\big) &= \frac{16H^3}{3} + \frac{4H}{3}\big(-3H^2k - 4H^2\big) = \frac{16H^3}{3} - 4H^3k - \frac{16H^3}{3} = -4H^3k .
\end{aligned}
$$

The first line differentiates $\rho = -\frac{H^2}{3}(18k + 1)$ with the chain rule; the second and the third add the entries; the fourth inserts them into the right side of the identity with $p_0 = p_t$ (so that $3h_4(\rho + p_t) + h_4(\rho + p_0) = 4h_4(\rho + p_t)$) and multiplies out. The two sides agree: the source of the history obeys both identities. It grows with $x_4$, like $H^2k = H^2e^{2a_4}/b_4$, it is anisotropic ($p_3 \neq p_t$), and it is a PRESCRIBED background, not a vacuum and not a field of this book (Chapter 12). Notebook 09a checks the same for the source of the author's Lovelock weights.

| statement | Revision record | entry or check |
| --- | --- | --- |
| the field equations need $p_0 = p_t$ and no off-diagonal source | `Revision/field_equations_a4/reports/wolfram-a4-report.json` and `python-a4-report.json` | `independent_components` |
| $\sum_k\alpha_k(E_{(k)}{}^{x_0}{}_{x_0} - E_{(k)}{}^{x_5}{}_{x_5}) = 0$ identically | `Revision/field_equations_a4/a4-equations.json` | entry `generalSource.hiddenEqualsExtraTimes` |
| every diagonal source entry must be independent of $x_0$ | `Revision/field_equations_a4/a4-equations.json` | entry `generalSource.x0_dependence` |
| the source of the history (Einstein, author's weights) | `Revision/metric_warped/results/warped-metric.json` | key `history_source` |
| the same source, found by the field-equations record | the two reports of `Revision/field_equations_a4/reports` | `author_weights_history_source` |

**All solutions when $p_t = P$ is a constant.** Write $q = p_0 - P$. Then $p_0 - p_t = q$, and with $dz = 6H\,dx_0$ the identity becomes

$$
6H\frac{dq}{dz} = -3H\cot z\;q, \qquad\text{that is}\qquad \frac{dq}{dz} + \tfrac12\cot z\;q = 0 .
$$

Multiply by $(\sin^2 z)^{1/4}$, whose derivative is $\frac14(\sin^2 z)^{-3/4}\cdot 2\sin z\cos z = \frac12(\sin^2 z)^{1/4}\cot z$ (the chain rule): $(\sin^2 z)^{1/4}\frac{dq}{dz} + \frac12(\sin^2 z)^{1/4}\cot z\;q = \frac{d}{dz}\big(q\,(\sin^2 z)^{1/4}\big) = 0$ (the product rule read backwards). So $q\,(\sin^2 z)^{1/4}$ is a constant $c$, and every solution is

$$
p_0 = P + \frac{c}{(\sin^2 z)^{1/4}} = P + \frac{c}{|\sin z|^{1/2}} .
$$

Only $c = 0$ gives a profile independent of $x_0$, and it has $p_0 = p_t$; every other profile is flat at the fold (where $\cot z = 0$) and grows in size like $|\sin z|^{-1/2}$ towards the tips $z = 0$ and $z = \pi$, where the extra times degenerate (Figure 09a.5).

**In the Kohn-Sham coordinate.** The Kohn-Sham solver of Chapter 15 uses the hidden coordinate $y = \ln|\sin z|/(6H)$, for which $dy/dx_0 = \frac{1}{6H}\cdot\frac{\cos z}{\sin z}\cdot 6H = \cot z$ (the chain rule; $\frac{d}{dz}\ln|\sin z| = \cos z/\sin z$ for both signs of $\sin z$). By the chain rule $\partial_0 p_0 = \cot z\,dp_0/dy$, so the $x_0$ component of the divergence is $\cot z\,\big[dp_0/dy + 3H(p_0 - p_t)\big]$, the form that solver checks (PROVED; `Revision/lead_checks/reports/emt-divergence-and-spin-connection.json`, checks `ks_coordinate_jacobian` and `ks_coordinate_form`). Since $|\sin z| = e^{6Hy}$, the profiles above are $p_0 = P + c\,e^{-3Hy}$ in this coordinate.

### 9.12 Where the spin connection does enter the tensor

The spin connection drops out of the Lagrangian and of the diagonal entries (Fact 1). It does enter entries off the diagonal, but not all of them. Take a **homogeneous** configuration: one that depends on the time $x_4$ only, so that $\partial_\mu\Phi = 0$ for every $\mu \neq x_4$. Consider the pieces

$$
K^{x_4}{}_{\mu} = \tfrac12\big(\bar\Phi\gamma^{x_4}D_{\mu}\Phi - D_{\mu}\bar\Phi\,\gamma^{x_4}\Phi\big) \qquad (\mu = x_1 \text{ and } \mu = x_5)
$$

of the entries $T^{x_4}{}_{x_1}$ and $T^{x_4}{}_{x_5}$. Because $\partial_\mu\Phi = 0$, $D_\mu\Phi = \Omega_\mu\Phi$ and $D_\mu\bar\Phi = -\bar\Phi\Omega_\mu$, and $\gamma^{x_4} = \gamma^{(4)}$ ($f_4 = 1$), so $K^{x_4}{}_\mu = \frac12\bar\Phi\{\gamma^{(4)}, \Omega_\mu\}\Phi$ ($\{A, B\} = AB + BA$ is the anticommutator). Line by line:

$$
\begin{aligned}
\{\gamma^{(4)}, \gamma^{(1)}\gamma^{(4)}\} &= \gamma^{(4)}\gamma^{(1)}\gamma^{(4)} + \gamma^{(1)}\gamma^{(4)}\gamma^{(4)} = -\gamma^{(1)}\gamma^{(4)}\gamma^{(4)} + \gamma^{(1)}\gamma^{(4)}\gamma^{(4)} = 0, \\
K^{x_4}{}_{x_1} &= \tfrac12\cdot\tfrac12a_4'e^{a_4}\;\bar\Phi\{\gamma^{(4)}, \gamma^{(1)}\gamma^{(4)}\}\Phi = 0, \\
\{\gamma^{(4)}, \gamma^{(4)}\gamma^{(5)}\} &= \gamma^{(4)}\gamma^{(4)}\gamma^{(5)} + \gamma^{(4)}\gamma^{(5)}\gamma^{(4)} = \gamma^{(4)}\gamma^{(4)}\gamma^{(5)} - \gamma^{(4)}\gamma^{(4)}\gamma^{(5)} = 0, \\
\{\gamma^{(4)}, \gamma^{(0)}\gamma^{(5)}\} &= \gamma^{(4)}\gamma^{(0)}\gamma^{(5)} + \gamma^{(0)}\gamma^{(5)}\gamma^{(4)} = 2\gamma^{(4)}\gamma^{(0)}\gamma^{(5)}, \\
K^{x_4}{}_{x_5} &= \tfrac12\cdot\tfrac12W\big(h_4s_b\cdot 0 + H\cdot 2\,\bar\Phi\gamma^{(4)}\gamma^{(0)}\gamma^{(5)}\Phi\big) = \tfrac12HW\;\bar\Phi\gamma^{(4)}\gamma^{(0)}\gamma^{(5)}\Phi .
\end{aligned}
$$

The first line moves the first $\gamma^{(4)}$ past $\gamma^{(1)}$ (one minus sign). The second inserts $\Omega_{x_1} = \frac12a_4'e^{a_4}\gamma^{(1)}\gamma^{(4)}$ and the first line. The third moves $\gamma^{(5)}$ past $\gamma^{(4)}$ in the second product (one minus sign). The fourth moves $\gamma^{(4)}$ in the second product to the front, past $\gamma^{(5)}$ and then past $\gamma^{(0)}$ (two minus signs, so no change of sign). The fifth inserts $\Omega_{x_5} = \frac12W(h_4s_b\gamma^{(4)}\gamma^{(5)} + H\gamma^{(0)}\gamma^{(5)})$ and the last two lines. So the connection part of the flow along 3-space vanishes (3-space does not depend on $x_0$, so $\Omega_{x_1}$ has no part with $H$), and the part with $h_4$ cancels along the extra time as well; but the part with $H$ survives, and the three-gamma bilinear $\bar\Phi\gamma^{(4)}\gamma^{(0)}\gamma^{(5)}\Phi$ is not zero in general: the canonical spin connection contributes to the energy-momentum tensor even though it drops out of the Lagrangian (PROVED; `Revision/theory/reports/python-scope.json` and `wolfram-scope.json`, check `spin_connection_in_the_energy_momentum_tensor`). Notebook 09a evaluates both pieces for a random homogeneous configuration at its point: $K^{x_4}{}_{x_1}$ is zero up to rounding ($1.1 \cdot 10^{-16}$) and $K^{x_4}{}_{x_5} = -0.981914$ (In [12]). Section 9.26 and Notebook 09c compute all such entries of a condensate, and show that the whole flow $T^{x_4}{}_{x_1}$ of a condensate comes from the gravitational term $c_g\gamma^{(0)}$ of the field equation instead.

### 9.13 The same tensor for dirac16complex

Everything in Sections 9.3 to 9.12 is algebra with the bilinears $\bar\Phi M\Phi$ and $\bar\Phi M\partial\Phi$, in which the row $\bar\Phi$ always stands to the left of the column. For the anticommuting field dirac16complex (Chapter 7) the same formulas hold, with every bilinear an even element of the Grassmann algebra (a sum of products of two anticommuting numbers; such a product commutes with every element of the algebra, as an ordinary number does); the Revision record verifies them (PROVED; for example the checks `T_diagonal_components_G`, `EMT_trace_G` and `kinetic_sum_on_shell_G` of `Revision/theory/reports/wolfram-field-theory.json` and the check `grassmann_homogeneous_on_shell_rho_p` of `Revision/theory/reports/python-field-theory.json`). After canonical quantisation (Chapter 10; the field becomes an **operator**, a rule that acts on the quantum states) the record defines the tensor as an operator too: every bilinear is replaced by the **normal-ordered** product of the quantised field (the product rearranged so that the operators that remove a particle stand to the right of those that create one, which gives the empty state the energy zero; Chapter 10 defines it exactly), $\hat T^\nu{}_\mu = {:}T^\nu{}_\mu[\hat\Psi, \hat{\bar\Psi}]{:}$, normal ordered with respect to the waves of the **good sector** (the waves that do not depend on the extra times $x_5, x_6, x_7$), and the numbers are **expectation values** (the average value that measurements of the operator give in a given quantum state) (record `Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.md`, section 12). Three limits of the record must be stated.

1. The space of quantum states with positive norms on which this normal ordering rests (the positive **Fock space** of Chapter 10, built from states with definite numbers of particles) is constructed and checked only for single good-sector momenta with frozen coefficients, that is, for plane waves of a flat frame at one point, in which the deflation of the extra times does not enter (PROVED for these examples; the table below names the checks). In the author's curved metric the record imposes no boundary condition at the folds $z = \pi/2 + n\pi$, where the two halves of a cell meet, and without one the good sector has complex frequencies (waves that grow or decay in time instead of oscillating), for $U = 0$ wherever $m^2 < c_g^2$ with $c_g = \frac32He^{a_4}b_4^{-1/2}$ (PROVED); on the record's history $c_g$ grows, so every mass falls below it at late times (Section 9.20 meets the same growth in the condensates). A space of states with positive norms for the full field is not established (OPEN).
2. For $\lambda \neq 0$ the operator form of the on-shell identity $\sum_\mu\langle{:}K_\mu{:}\rangle = \langle{:}(m + U')S{:}\rangle$ is verified only in a finite model: the Fock space of one good-sector plane-wave mode set with frozen coefficients (flat frame, volume 1, 16 modes, $2^{16}$ states). There it holds as an exact operator identity, for the solution of the interacting operator field equation, if and only if the potential and the tensor are both **Wick ordered** (the whole product of field operators is normal ordered at once: the potential as $\frac{\lambda}{2}{:}SS{:}$, not as $\frac{\lambda}{2}{:}S{:}\,{:}S{:}$, and the tensor as a Wick product, not by subtracting its value in the empty state); with every other ordering tested it fails, already in expectation values (PROVED in that model; its report, named in the table below, passes 21 of 21 checks). For the field on a whole slice (many momenta), for the curved $x_0$ dependence and for the extra-time sector the operator identity is OPEN (the field-equations record of Chapter 12 ASSUMES it), and symmetry and conservation of the quartic operator are not verified.
3. Numerical expectation values of the tensor for many-fermion states are computed only in the Kohn-Sham approximation of Part IV. The finite model of limit 2 gives exact values on the **occupation states** of its one mode set at rest (momentum $k = 0$). An occupation state has each of the 16 modes either empty or holding one **quantum** (one excitation of the quantised field); Chapter 10 splits the 16 modes into 8 particle modes and 8 **antiparticle** modes (an antiparticle has the opposite charge of a particle, and both have positive energy). On an occupation state with $n$ quanta, particles and antiparticles counted together, $\rho = mn + \frac{\lambda}{2}n(n - 1)$ and $p = \frac{\lambda}{2}n(n - 1)$, so that $\langle{:}U(S){:}\rangle = \frac{\lambda}{2}n(n - 1)$ differs from $U(\langle{:}S{:}\rangle) = \frac{\lambda}{2}n^2$ for $n \geq 1$ and $\lambda \neq 0$ (PROVED in that model; the table below names the check). For example, one particle and one antiparticle at rest ($n = 2$) give $\rho = 2m + \lambda$ and $p = \lambda$, and two particles and one antiparticle ($n = 3$) give $\rho = 3m + 3\lambda$ and $p = 3\lambda$. The model gives no numerical expectation value for a physical many-fermion state.

The records of the three limits:

| statement | Revision report | check |
| --- | --- | --- |
| positive Fock space for single good-sector momenta with frozen coefficients | `Revision/theory/reports/wolfram-field-theory.json` | `mode_hamiltonian_good_sector`, `Fock_space_good_sector_example` |
| the same with sympy, for another momentum | `Revision/theory/reports/python-field-theory.json` | `good_sector_positive_fock_realisation` |
| complex frequencies of the curved good sector without a boundary condition at the folds | `Revision/theory/reports/wolfram-scope.json` and `python-scope.json` | `good_sector_hermiticity_up_to_the_brane_flux`, `good_sector_x0_independent_modes_without_boundary_condition` |
| finite model, $\lambda \neq 0$: the identity holds when both are Wick ordered | `Revision/theory/fock_quartic/reports/fock-quartic.json` | `trace_identity_operator_identity_wick` |
| finite model: it fails for every other ordering tested | the same report | `trace_identity_fails_for_every_other_combination` |
| finite model, occupation states with $n$ quanta at rest: $\rho = mn + \frac{\lambda}{2}n(n - 1)$, $p = \frac{\lambda}{2}n(n - 1)$ | the same report | `homogeneous_expectation_values_are_not_U_of_expectation` |

This chapter therefore computes numbers only for the commuting field dirac16complex00.

### 9.14 Example: the tensor at one point and the two identities

The first worked example puts Sections 9.3 to 9.12 on the computer. At one point of the history ($H = 0.25$, $a_4 = AHx_4$ with $A = 1$ and $b_4 = b_4(0)e^{\beta AHx_4}$ with $\beta = \frac43$, so $a_4 = 0.5$, $a_4' = 0.25$, $b_4 = e^{2/3}$ in the unit $b_4(0)$, $b_4'/b_4 = \frac13$ and $h_4 = -\frac{1}{12}$ at $x_4 = 2$, and $z = \pi/4$) it builds the vielbein factors, the coordinate gammas and the spin connection of the corrected metric from the Revision fixture and formula, checks Facts 1 and 2 of Section 9.3, draws a configuration of dirac16complex00 at random, computes its 64 entries $T^\nu{}_\mu$ literally from the formula of Section 9.6, and checks every identity of Sections 9.5 to 9.8, first off shell and then after putting the configuration on shell with the evolution form. It checks the connection terms of Section 9.12. Then it switches to exact symbols: it computes the 21 Christoffel symbols with sympy for both signs of $\sin z$, compares them with the record, derives the eight components of the divergence of a diagonal tensor and compares them with the record's formula `energy_exchange` and with the lead's checks, checks the first-law reading and the profiles of the $x_0$ balance, checks that the source of the record's history obeys both identities, and draws five figures.

<!-- NOTEBOOK 09a -->

### 9.17 Line-by-line walk-through of Notebook 09a

The notebook has 22 code cells, In [1] to In [22]. This section explains every line of every one of them, in order. Code that is printed again here is quoted exactly, except that a long figure caption is shortened to a line "...)" (it is printed in full in Section 9.16, under its figure) and that, in In [1], the texts in triple quotes that document a function (its docstring) and the comment lines inside the function `save_figure` are left out; from In [2] on every line is quoted, docstrings included.

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

**In [2], the gamma matrices, the matrix C and the report helper.**

```python
import numpy as np  # arrays of numbers, matrices, linear algebra

fixture = json.loads(
    repository_file("Revision/algebra/gammas.json").read_text(encoding="utf-8"))
# gamma[a] is the frame matrix gamma^(xa): gamma[0] = x0, ..., gamma[7] = x7.
gamma = [np.array(rows, dtype=float) for rows in fixture["gamma"]]
eta = np.array(fixture["eta"], dtype=float)  # (+1, +1, +1, +1, -1, -1, -1, -1)
C = np.array(fixture["C"], dtype=float)  # gamma^(x0) gamma^(x1) gamma^(x2) gamma^(x3)
I16 = np.eye(16)  # the 16 x 16 unit matrix
NAMES = ["x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7"]  # the author's coordinates
```

`numpy` is the package for arrays of numbers; `np` is its usual short name. `json.loads` turns the text of the Revision fixture `Revision/algebra/gammas.json` into Python lists and dictionaries; `repository_file` (In [1]) gives its path, and `.read_text(encoding="utf-8")` reads it. The fixture stores the eight gamma matrices under the key `"gamma"`, as lists of 16 rows of 16 numbers; the **list comprehension** `[... for rows in ...]` turns each of them into a numpy array of floating-point numbers (`dtype=float`), so that `gamma[0]` is $\gamma^{(0)}$ and `gamma[4]` is $\gamma^{(4)}$. `eta` holds the eight diagonal entries of the frame metric, `C` the matrix $C = \gamma^{(0)}\gamma^{(1)}\gamma^{(2)}\gamma^{(3)}$, `I16` the $16 \times 16$ unit matrix, and `NAMES` the names of the eight coordinates, used in labels and printed lines.

```python
def recorded(path, name):
    """The verdict (PASS or FAIL) of the check name in the Revision report path."""
    report_data = json.loads(repository_file(path).read_text(encoding="utf-8"))
    for item in report_data["checks"]:
        if item["name"] == name:
            return item["verdict"].upper()  # some reports write "pass"
    raise KeyError(f"{path} has no check {name}")
```

The helper `recorded(path, name)` opens a Revision report, walks through its list `"checks"` with a `for` loop, and returns the verdict of the check whose name is `name`, in capital letters (`.upper()`, because some reports write `pass`). If no check has that name, `raise KeyError(...)` stops the notebook with the message "... has no check ...", the symptom that the troubleshooting list of the run instructions explains. Every check of this notebook that reproduces a Revision check asks the report for its verdict, so a changed or failed record is noticed.

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

The first check: for all 64 ordered pairs $(a, b)$ the anticommutator $\gamma^{(a)}\gamma^{(b)} + \gamma^{(b)}\gamma^{(a)}$ must equal $2\eta^{ab}$ times the unit matrix. `@` is matrix multiplication; `(a == b)` is `True` (counted as 1) on the diagonal and `False` (0) off it, so `2 * eta[a] * (a == b) * I16` is $2\eta^{ab}\cdot 1$; `np.array_equal` compares two arrays exactly (the entries are integers, so no rounding occurs); `all(...)` is `True` only if every one of the 64 comparisons is. The check also requires the record's verdict of `clifford_relation`. It prints `PASS the 64 Clifford relations {gamma^a, gamma^b} = 2 eta^ab` and the line naming the record.

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

The second check: $C$ equals its transpose `C.T`, $C \cdot C = 1$, and every product $C\gamma^{(a)}$ is antisymmetric, together with the record's verdicts of `C_real_symmetric_involution` and `C_gamma_antisymmetric`. These are the properties of $C$ that Section 9.6 uses to prove that the tensor is real. The cell prints the two PASS lines.

**In [3], the corrected metric at one point.**

```python
H = 0.25  # the author's constant H
A = 1.0  # the history a4 = A H x4; A > 0: 3-space inflates, the block deflates
m = 1.0  # the mass m of the field
lam = 0.5  # the strength lambda of the potential U(S) = (lambda/2) S^2
beta = 4 / 3  # the history b4 = b4(0) e^(beta A H x4), in the unit b4(0)
X4 = 2.0  # the time x4 of the point
a4 = A * H * X4  # a4 at the point: 0.5
a4p = A * H  # its derivative da4/dx4 (written a4p, "a4 prime"): 0.25
b4 = np.exp(beta * A * H * X4)  # b4 at the point: e^(2/3)
b4p = beta * A * H * b4  # db4/dx4, so that b4p/b4 = 1/3
z = np.pi / 4  # z = 6 H x0 at the point
```

The parameters of the example: the author's constant $H = 0.25$, the history constant $A = 1$, the mass $m = 1$, the strength $\lambda = 0.5$ of the potential (written `lam`, because `lambda` is a word reserved by Python), the exponent $\beta = \frac43$ of $b_4 = b_4(0)e^{\beta AHx_4}$, and the time $x_4 = 2$ of the point. From them: $a_4 = AHx_4 = 0.5$, its derivative $a_4' = AH = 0.25$ (written `a4p`), $b_4 = e^{\beta AHx_4} = e^{2/3}$ in the unit $b_4(0)$, its derivative $b_4' = \beta AH\,b_4$ (so that $b_4'/b_4 = \frac13$), and $z = \pi/4$.

```python
def frame_factors(a4_value, b4_value, z_value):
    """The eight factors f_a of the diagonal vielbein, in the order x0, ..., x7."""
    block = np.exp(-a4_value) * np.sqrt(b4_value)  # e^(-a4) b4^(1/2)
    hidden = block / np.tan(z_value)  # e^(-a4) b4^(1/2) cot z (signed)
    extra = block * np.abs(np.sin(z_value)) ** (1 / 6)  # times (sin^2 z)^(1/12)
    return np.array([hidden] + [np.exp(a4_value)] * 3 + [1.0] + [extra] * 3)
```

The function `frame_factors` returns the eight vielbein factors of Section 9.2 as one numpy array, in the order $x_0, \dots, x_7$: `block` is the hidden scale $s_b = e^{-a_4}b_4^{1/2}$; `hidden` is $f_0 = s_b\cot z$, computed as `block / np.tan(z_value)` (it keeps the sign of $\cot z$); `extra` is $f_t = s_bW$ with $W = |\sin z|^{1/6} = (\sin^2 z)^{1/12}$; and the list `[hidden] + [np.exp(a4_value)] * 3 + [1.0] + [extra] * 3` puts them in order (`[x] * 3` repeats an entry three times, `+` joins lists).

```python
f = frame_factors(a4, b4, z)
g_diag = eta * f ** 2  # the diagonal entries g_mumu = eta_mumu f_mu^2
# The corrected metric written out: e^(-2 a4) b4 cot^2 z, e^(2 a4), -1,
# -e^(-2 a4) b4 (sin^2 z)^(1/6).
authors = np.array([np.exp(-2 * a4) * b4 / np.tan(z) ** 2] + [np.exp(2 * a4)] * 3
                   + [-1.0] + [-np.exp(-2 * a4) * b4 * (np.sin(z) ** 2) ** (1 / 6)] * 3)
```

`f` holds the factors at the point and `g_diag` the diagonal entries $g_{\mu\mu} = \eta_{\mu\mu}f_\mu^2$ (numpy multiplies two arrays entry by entry). `authors` writes the four different entries of the corrected metric directly from the author's formula: $e^{-2a_4}b_4\cot^2 z$, $e^{2a_4}$ three times, $-1$, and $-e^{-2a_4}b_4(\sin^2 z)^{1/6}$ three times.

```python
THEORY_PY = "Revision/theory/reports/python-field-theory.json"
check(np.allclose(g_diag, authors, rtol=1e-14, atol=0)
      and recorded(THEORY_PY, "metric_from_vielbein_equals_SPEC") == "PASS",
      "eta_aa f_a^2 is the corrected metric at the point",
      record=f"{THEORY_PY}, check metric_from_vielbein_equals_SPEC")
```

`np.allclose(..., rtol=1e-14, atol=0)` asks that every entry agree to a relative accuracy of $10^{-14}$, which leaves room only for rounding. Together with the record's verdict of `metric_from_vielbein_equals_SPEC` this is the PASS line `eta_aa f_a^2 is the corrected metric at the point`.

```python
volume = np.exp(-a4) * b4 ** 2 * abs(1 / np.tan(z)) * (np.sin(z) ** 2) ** (1 / 4)
check(abs(abs(np.prod(f)) - volume) < 1e-14
      and recorded(THEORY_PY, "sqrt_det_g") == "PASS",
      "|f0 f1 ... f7| equals e^(-a4) b4^2 |cot z| (sin^2 z)^(1/4)",
      record=f"{THEORY_PY}, check sqrt_det_g")
```

`volume` is the volume factor $\sqrt{|g|} = e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}$ of Section 9.2, and the check compares it with the absolute value of the product of the eight factors, `abs(np.prod(f))`, together with the record's verdict of `sqrt_det_g`.

```python
for name, value in zip(NAMES, f):
    report(f"f_{name}", f"{value:.6f}")
report("sqrt|g| at the point", f"{volume:.6f}")
```

`zip(NAMES, f)` walks through the names and the factors in pairs, and `report` prints one RESULT line for each, with six decimals (`:.6f`): `f_x0 = 0.846482`, `f_x1 = f_x2 = f_x3 = 1.648721` ($e^{0.5}$), `f_x4 = 1.000000`, `f_x5 = f_x6 = f_x7 = 0.798972`, and `sqrt|g| at the point = 1.934882`. Check two of them by hand: $s_b = e^{-0.5}e^{1/3} = e^{-1/6} = 0.846482$ and $\cot(\pi/4) = 1$, so $f_0 = 0.846482$; and $\sqrt{|g|} = e^{-0.5}e^{4/3}\cdot 1\cdot(1/2)^{1/4} = e^{5/6}\cdot 0.840896 = 2.300976\cdot 0.840896 = 1.934882$.

**In [4], the weights of the kinetic terms.**

```python
from matplotlib.ticker import NullFormatter  # a tick label that prints nothing

a4_axis = np.linspace(-2.0, 2.0, 401)  # values of a4 for the left panel
z_axis = np.linspace(0.02, np.pi - 0.02, 400)  # values of z for the right panel
fig, (left, right) = plt.subplots(1, 2, figsize=(9.6, 3.9))
# along the history b4 = e^(beta a4) (since a4 = A H x4 and b4 = e^(beta A H x4))
weights_a4 = np.abs([1 / frame_factors(value, np.exp(beta * value), z)
                     for value in a4_axis])
weights_z = np.abs([1 / frame_factors(a4, b4, value) for value in z_axis])
```

`NullFormatter` is a matplotlib helper that prints nothing; it is used below to hide the labels of the small ticks of a logarithmic axis. `np.linspace(-2.0, 2.0, 401)` makes 401 equally spaced values of $a_4$ from $-2$ to $2$, and `z_axis` 400 values of $z$ from $0.02$ to $\pi - 0.02$ (the ends are left out, because the hidden weight is infinite at $z = 0$ and $z = \pi$). `plt.subplots(1, 2, figsize=(9.6, 3.9))` makes a figure with two panels side by side, 9.6 by 3.9 inches. `weights_a4` holds, for every $a_4$ of the left axis, the sizes `np.abs(1 / frame_factors(...))` of the eight weights $1/f_\mu$ along the history: there $b_4 = e^{\beta a_4}$ (because $a_4 = AHx_4$ and $b_4 = e^{\beta AHx_4}$), at $z = \pi/4$. `weights_z` holds the same for every $z$ of the right axis, at the point's $a_4$ and $b_4$. Each is an array with one row per value and one column per direction.

```python
for panel, axis, weights in ((left, a4_axis, weights_a4), (right, z_axis, weights_z)):
    panel.plot(axis, weights[:, 1], label="3-space $x_1, x_2, x_3$")
    panel.plot(axis, weights[:, 4], "--", label="time $x_4$")
    panel.plot(axis, weights[:, 5], label="extra times $x_5, x_6, x_7$")
    panel.plot(axis, weights[:, 0], ":", label="hidden direction $x_0$")
    panel.set_yscale("log")  # equal factors are equal distances on this axis
    panel.yaxis.set_minor_formatter(NullFormatter())  # no labels on minor ticks
    panel.set_ylabel("size of the weight $|1/f_\\mu|$")
```

The `for` loop draws the same four curves in both panels: column 1 (3-space), column 4 (the time, dashed), column 5 (the extra times) and column 0 (the hidden direction, dotted); `weights[:, 1]` means "every row, column 1". The vertical axis is logarithmic (`set_yscale("log")`: equal factors are equal distances), and the small ticks get no labels.

```python
right.axvline(np.pi / 2, color="gray", linewidth=0.8)  # the fold z = pi/2
ticks = [0.03, 0.1, 0.2, 0.5, 1, 2, 5, 10, 30]  # plain numbers on the vertical axes
left.set_yticks(ticks[2:8], [str(t) for t in ticks[2:8]])
right.set_yticks(ticks, [str(t) for t in ticks])
right.set_ylim(0.02, 50.0)
```

A thin gray vertical line marks the fold $z = \pi/2$ in the right panel. The tick positions are chosen by hand and labelled with plain numbers (`str(t)` turns a number into text); the left panel uses the values from $0.2$ to $10$ (`ticks[2:8]`, the entries 2 to 7 of the list), the right one all of them, and its vertical range is fixed from $0.02$ to $50$.

```python
left.set_xlabel("$a_4$ (history: $b_4 = e^{4a_4/3}$; $z = \\pi/4$)")
right.set_xlabel("$z = 6 H x_0$ (at $a_4 = 0.5$, $b_4 = e^{2/3}$; fold at $\\pi/2$)")
left.set_title("Weights along the history")
right.set_title("Weights against $z$")
left.legend(fontsize=8)
```

Axis labels, panel titles and the legend (the list of curve names) of the left panel. In matplotlib labels a backslash must be doubled in a normal Python string, so `\\mu` produces the letter $\mu$ and `\\pi` the letter $\pi$.

```python
save_figure(fig, "kinetic_weights",
            "The sizes of the weights $1/f_\\mu$ with which a derivative along each "
...)
```

`save_figure` saves the picture as `Revision/textbook/figures/09a_1_kinetic_weights.png` with its caption (printed in full under Figure 09a.1 in Section 9.16) and prints `Figure 09a.1 saved as Revision/textbook/figures/09a_1_kinetic_weights.png`. The student should see, on the left, the 3-space weight falling like $e^{-a_4}$ and the extra-time and hidden weights rising together like $e^{a_4/3}$ (their ratio is the constant $(\sin^2 z)^{-1/12}/\tan z$ at $z = \pi/4$, $2^{1/12} = 1.06$), and, on the right, the hidden weight growing without bound at the fold while the 3-space weight stays flat and the extra-time weight grows towards the tips $z = 0$ and $z = \pi$, where $W \to 0$.

**In [5], the spin connection at the point.**

```python
def spin_connection(a4_value, a4p_value, b4_value, b4p_value, z_value):
    """The eight 16 x 16 matrices Omega_mu of the record's formula Omega_components."""
    s_b = np.exp(-a4_value) * np.sqrt(b4_value)  # e^(-a4) b4^(1/2)
    h4 = b4p_value / (2 * b4_value) - a4p_value  # the rate of the block
    root = np.abs(np.sin(z_value)) ** (1 / 6)  # (sin^2 z)^(1/12)
    omega = [np.zeros((16, 16)) for _ in range(8)]  # Omega_x4 stays 0
    omega[0] = 0.5 * h4 * s_b / np.tan(z_value) * gamma[0] @ gamma[4]
    for i in range(1, 4):  # the three 3-space directions x1, x2, x3
        omega[i] = 0.5 * a4p_value * np.exp(a4_value) * gamma[i] @ gamma[4]
    for t in range(5, 8):  # the three extra times x5, x6, x7
        omega[t] = 0.5 * root * (h4 * s_b * gamma[4] @ gamma[t]
                                 + H * gamma[0] @ gamma[t])
    return omega
```

The function `spin_connection` builds the eight matrices $\Omega_\mu$ of the record's formula `Omega_components` (Section 9.2). `s_b` is the hidden scale, `h4` the rate $h_4 = b_4'/(2b_4) - a_4'$ of the block, and `root` the warp factor $W = (\sin^2 z)^{1/12}$. `omega` starts as a list of eight zero matrices, so $\Omega_{x_4}$ stays zero. Then `omega[0]` $= \frac12h_4s_b\cot z\,\gamma^{(0)}\gamma^{(4)}$ (the division by `np.tan(z_value)` is the factor $\cot z$), the loop over $i = 1, 2, 3$ sets $\Omega_{x_i} = \frac12a_4'e^{a_4}\gamma^{(i)}\gamma^{(4)}$, and the loop over $t = 5, 6, 7$ sets $\Omega_{x_t} = \frac12W(h_4s_b\gamma^{(4)}\gamma^{(t)} + H\gamma^{(0)}\gamma^{(t)})$; `range(5, 8)` runs through 5, 6, 7.

```python
Omega = spin_connection(a4, a4p, b4, b4p, z)
gamma_up = [gamma[mu] / f[mu] for mu in range(8)]  # coordinate gammas gamma^mu
gamma_down = [g_diag[mu] * gamma_up[mu] for mu in range(8)]  # gamma_mu
```

`Omega` holds the eight matrices at the point. `gamma_up` holds the coordinate gammas $\gamma^\mu = \gamma^{(\mu)}/f_\mu$ and `gamma_down` the gammas with a lower index, $\gamma_\mu = g_{\mu\mu}\gamma^\mu$.

```python
# {gamma^mu, Omega_mu} for each mu separately: the largest entry of all eight.
anti = max(np.abs(gamma_up[mu] @ Omega[mu] + Omega[mu] @ gamma_up[mu]).max()
           for mu in range(8))
A4_REPORT = "Revision/field_equations_a4/reports/wolfram-a4-report.json"
check(anti < 1e-14
      and recorded(A4_REPORT, "gamma_mu_anticommutes_with_Omega_mu_no_sum") == "PASS",
      "{gamma^mu, Omega_mu} = 0 for each direction mu (no sum)",
      record=f"{A4_REPORT}, check gamma_mu_anticommutes_with_Omega_mu_no_sum")
```

Fact 1 of Section 9.3: for each direction separately the anticommutator $\gamma^\mu\Omega_\mu + \Omega_\mu\gamma^\mu$ is computed, its largest entry in size is taken (`np.abs(...).max()`), and `max(...)` keeps the largest of the eight. It must be below $10^{-14}$ (zero up to rounding), and the record's verdict of `gamma_mu_anticommutes_with_Omega_mu_no_sum` must be PASS. One PASS line.

```python
h4 = b4p / (2 * b4) - a4p  # -1/12 at the point
c_g = 1.5 * H * np.exp(a4) / np.sqrt(b4)  # the coefficient of gamma^(x0)
v_g = b4p / b4 - a4p / 2  # the coefficient of gamma^(x4)
```

The rate $h_4$ at the point ($\frac16 - \frac14 = -\frac{1}{12}$) and the two gravitational coefficients of the field equation, $c_g = \frac32He^{a_4}b_4^{-1/2}$ and $v_g = b_4'/b_4 - a_4'/2$.

```python
# the record's value of gamma^mu Omega_mu for each direction (no sum)
per_direction = ([0.5 * h4 * gamma[4]] + [0.5 * a4p * gamma[4]] * 3 + [0 * I16]
                 + [0.5 * h4 * gamma[4] + c_g / 3 * gamma[0]] * 3)
THEORY_WL = "Revision/theory/reports/wolfram-field-theory.json"
check(max(np.abs(gamma_up[mu] @ Omega[mu] - per_direction[mu]).max()
          for mu in range(8)) < 1e-14
      and recorded(THEORY_PY, "per_direction_terms") == "PASS"
      and recorded(THEORY_WL, "gammaOmega_per_direction") == "PASS",
      "gamma^mu Omega_mu per direction: h4/2, a4'/2 (x3), 0, h4/2 + c_g/3 (x3)",
      record=f"{THEORY_PY}, check per_direction_terms; {THEORY_WL}, check "
             "gammaOmega_per_direction")
```

The three values of $\gamma^\mu\Omega_\mu$ per direction found in Section 9.3: $\frac12h_4\gamma^{(4)}$ for $x_0$, $\frac12a_4'\gamma^{(4)}$ for each of the three 3-space directions, the zero matrix `0 * I16` for $x_4$, and $\frac12h_4\gamma^{(4)} + \frac{c_g}{3}\gamma^{(0)}$ for each of the three extra times ($\frac{c_g}{3} = \frac12He^{a_4}b_4^{-1/2}$). The check compares the eight products `gamma_up[mu] @ Omega[mu]` with this list and asks both records, the sympy check `per_direction_terms` and the Wolfram check `gammaOmega_per_direction`.

```python
total = sum(gamma_up[mu] @ Omega[mu] for mu in range(8))  # gamma^mu Omega_mu, summed
LEAD = "Revision/lead_checks/reports/emt-divergence-and-spin-connection.json"
check(np.abs(total - c_g * gamma[0] - v_g * gamma[4]).max() < 1e-14
      and recorded(THEORY_PY, "gamma_mu_Omega_mu_equals_hidden_block_terms") == "PASS"
      and recorded(LEAD, "gamma_Omega_equals_hidden_block_terms") == "PASS",
      "gamma^mu Omega_mu = c_g gamma^(x0) + v_g gamma^(x4) at the point",
      record=f"{THEORY_PY}, check gamma_mu_Omega_mu_equals_hidden_block_terms; "
             f"{LEAD}, check gamma_Omega_equals_hidden_block_terms")
```

Fact 2: the sum of the eight products must be $c_g\gamma^{(0)} + v_g\gamma^{(4)}$, as the record (`gamma_mu_Omega_mu_equals_hidden_block_terms`) and the lead's independent check (`gamma_Omega_equals_hidden_block_terms`) state.

```python
report("h4 = b4'/(2 b4) - a4'", f"{h4:.6f}")
report("c_g = (3/2) H e^a4 b4^(-1/2)", f"{c_g:.6f}")
report("v_g = b4'/b4 - a4'/2", f"{v_g:.6f}")
```

The three numbers are printed: `h4 = b4'/(2 b4) - a4' = -0.083333`, `c_g = (3/2) H e^a4 b4^(-1/2) = 0.443010` and `v_g = b4'/b4 - a4'/2 = 0.208333`. By hand: $c_g = 0.375\,e^{0.5 - 1/3} = 0.375\,e^{1/6} = 0.375\cdot 1.181360 = 0.443010$, and $v_g = \frac13 - \frac18 = \frac{5}{24} = 0.208333$.

**In [6], the energy-momentum tensor from the jet.**

```python
def bar(vector):
    """The Dirac adjoint: the row vector vector^dagger C."""
    return vector.conj() @ C
```

`bar` returns the Dirac adjoint $\bar\Phi = \Phi^\dagger C$ of a column: `vector.conj()` takes the complex conjugate of every entry, and `@ C` multiplies the row by $C$ from the right (for a one-dimensional array numpy does not distinguish rows from columns, so no transpose is needed).

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

`energy_momentum` follows the formula of Section 9.6 literally. It receives the 16 values `phi` of $\Phi$, the eight columns `dphi` of the derivatives $\partial_\mu\Phi$, the factors, the coordinate gammas with upper and lower index and the spin connection. It computes $g_{\mu\mu}$, the scalar $S = \bar\Phi\Phi$ (its real part; it is real anyway), the potential $U = \frac{\lambda}{2}S^2$, the eight columns $D_\mu\Phi = \partial_\mu\Phi + \Omega_\mu\Phi$, the eight rows $D_\mu\bar\Phi = \partial_\mu\bar\Phi - \bar\Phi\Omega_\mu$ (with $\partial_\mu\bar\Phi$ = `bar(dphi[mu])`), and the Lagrangian $L_0 = \frac12\sum_\mu(\bar\Phi\gamma^\mu D_\mu\Phi - D_\mu\bar\Phi\gamma^\mu\Phi) - mS - U$.

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

The 64 entries: for every row $\nu$ and column $\mu$ the bracket of Section 9.6 is formed. Its first pair is $\bar\Phi\gamma^\nu D_\mu\Phi - D_\mu\bar\Phi\gamma^\nu\Phi$; its second pair is $\bar\Phi\gamma_\mu D^\nu\Phi - D^\nu\bar\Phi\gamma_\mu\Phi$, with $D^\nu = D_\nu/g_{\nu\nu}$ (the comment line says so). Then `T[nu, mu]` is $\delta^\nu_\mu L_0$ minus a quarter of the bracket; `(nu == mu)` supplies the $\delta$. The array has `dtype=complex`, because the products of complex columns are complex numbers before their imaginary parts are seen to vanish.

```python
    # K_mu = (1/(2 f_mu)) (Phibar gamma^(mu) d_mu Phi - d_mu Phibar gamma^(mu) Phi)
    K = np.array([(bar(phi) @ gamma[mu] @ dphi[mu] - bar(dphi[mu]) @ gamma[mu] @ phi)
                  / (2 * f_values[mu]) for mu in range(8)])
    return S, U, L0, K, T
```

The eight kinetic terms $K_\mu = \frac{1}{2f_\mu}(\bar\Phi\gamma^{(\mu)}\partial_\mu\Phi - \partial_\mu\bar\Phi\gamma^{(\mu)}\Phi)$ are computed from their own formula, with the frame gammas and without the spin connection, so that In [9] can compare them with the diagonal of the tensor. The function returns $S$, $U$, $L_0$, the eight $K_\mu$ and the table $T$; the cell prints nothing.

**In [7], a random configuration and its tensor.**

```python
rng = np.random.default_rng(12345)  # a fixed seed: the same numbers in every run
Phi = rng.normal(size=16) + 1j * rng.normal(size=16)  # the 16 values of Phi
dPhi = rng.normal(size=(8, 16)) + 1j * rng.normal(size=(8, 16))  # d_mu Phi
# np.roll moves the last row to the front: the eight rows are the derivatives along
# x0, x1, ..., x7, and the numbers are those of the earlier edition of this notebook.
dPhi = np.roll(dPhi, 1, axis=0)
```

`np.random.default_rng(12345)` makes a random-number generator with the fixed **seed** 12345, so every run draws the same numbers. `rng.normal(size=16)` draws 16 numbers from the normal (bell-curve) distribution; with `1j` ($i$ in Python) the cell builds 16 complex values of $\Phi$ and an $8 \times 16$ array of complex derivatives. `np.roll(dPhi, 1, axis=0)` moves the last row to the front; as the comment says, this only reorders the rows so that the numbers are those of the earlier edition of this notebook, with row $\mu$ the derivative along $x_\mu$.

```python
S, U, L0, K, T = energy_momentum(Phi, dPhi, f, gamma_up, gamma_down, Omega)
largest_imaginary = max(np.abs(T.imag).max(), np.abs(K.imag).max(), abs(L0.imag))
check(largest_imaginary < 1e-12, "every entry of T, every K_mu and L0 are real")
T, K, L0 = T.real, K.real, L0.real  # keep the real parts
```

The tensor of this configuration. Every entry of $T$, every $K_\mu$ and $L_0$ must be real (Section 9.6): the largest imaginary part must be below $10^{-12}$, and the check `every entry of T, every K_mu and L0 are real` prints PASS. Then the real parts are kept.

```python
T_low = g_diag[:, None] * T  # T_numu = g_nunu T^nu_mu
check(np.abs(T_low - T_low.T).max() < 1e-12
      and recorded(THEORY_PY, "commuting_emt_symmetric") == "PASS",
      "T_numu is symmetric (64 entries, 28 pairs compared)",
      record=f"{THEORY_PY}, check commuting_emt_symmetric")
```

`g_diag[:, None] * T` multiplies row $\nu$ of $T$ by $g_{\nu\nu}$ (`[:, None]` turns the eight numbers into a column, so that numpy multiplies row by row): this is $T_{\nu\mu} = g_{\nu\nu}T^\nu{}_\mu$. It must equal its transpose, as Section 9.6 proved, and the record's verdict of `commuting_emt_symmetric` must be PASS.

```python
report("S = Phibar Phi", f"{S:.6f}")
report("L0", f"{L0:.6f}")
```

Two RESULT lines: `S = Phibar Phi = -6.527875` and `L0 = 10.663991`. $S$ is negative for this random column: the scalar has no sign (Section 9.21).

**In [8], the heat map of the tensor.**

```python
fig, ax = plt.subplots(figsize=(6.6, 5.6))
largest = np.abs(T).max()  # the colour scale runs from -largest to +largest
picture = ax.imshow(T, cmap="RdBu_r", vmin=-largest, vmax=largest)
```

A figure of 6.6 by 5.6 inches. `largest` is the largest entry in size, and `ax.imshow` draws the $8 \times 8$ table as coloured squares, with the colour map `RdBu_r` (red for positive, blue for negative numbers, white near zero) running from $-$`largest` to $+$`largest`.

```python
for nu in range(8):
    for mu in range(8):
        # white digits on dark squares, black digits on light ones
        colour = "white" if abs(T[nu, mu]) > 0.6 * largest else "black"
        ax.text(mu, nu, f"{T[nu, mu]:.1f}", ha="center", va="center", fontsize=7,
                color=colour)
```

The two loops write the value of each entry, with one decimal (`:.1f`), in the middle of its square; the digits are white on dark squares (more than 0.6 of the largest size) and black on light ones, so that they can always be read.

```python
ax.set_xticks(range(8), [f"${n[0]}_{n[1]}$" for n in NAMES])
ax.set_yticks(range(8), [f"${n[0]}_{n[1]}$" for n in NAMES])
ax.set_xlabel("lower index $\\mu$ (column)")
ax.set_ylabel("upper index $\\nu$ (row)")
ax.set_title("$T^\\nu{}_\\mu$ of one random configuration at one point")
ax.grid(False)  # no grid lines across the squares
fig.colorbar(picture, ax=ax, label="value of $T^\\nu{}_\\mu$ (energy per volume)")
```

The tick labels are the names of the directions written as math, $x_0, \dots, x_7$ (`n[0]` is the letter `x`, `n[1]` the digit); the axis labels say that the column is the lower index and the row the upper index; `ax.grid(False)` removes the grid lines of the book's style, which would cross the squares; `fig.colorbar` adds the colour scale with its label.

```python
save_figure(fig, "tensor_heat_map",
            "Heat map of the energy-momentum tensor $T^\\nu{}_\\mu$ of a random "
...)
```

The picture is saved as Figure 09a.2 (`09a_2_tensor_heat_map.png`) and the cell prints the line `Figure 09a.2 saved as ...`. In it the student sees a full table: a random configuration has flows of energy and momentum in every direction; the mixed table is not symmetric as printed, because the upper index is raised with the metric, while $g_{\nu\nu}T^\nu{}_\mu$ is symmetric (In [7]).

**In [9], the diagonal entries and their parts.**

```python
check(np.abs(np.diag(T) - (L0 - K)).max() < 1e-12
      and abs(L0 - (K.sum() - m * S - U)) < 1e-12
      and recorded(THEORY_WL, "T_diagonal_components_C") == "PASS",
      "T^mu_mu = L0 - K_mu for all eight mu, and L0 = sum K - m S - U",
      record=f"{THEORY_WL}, check T_diagonal_components_C")
```

The formula of Section 9.5, $T^\mu{}_\mu = L_0 - K_\mu$, for all eight directions at once (`np.diag(T)` is the array of the eight diagonal entries, and `L0 - K` subtracts each $K_\mu$ from $L_0$), and $L_0 = \sum_\mu K_\mu - mS - U$ (`K.sum()` adds the eight kinetic terms), together with the record's verdict of `T_diagonal_components_C`.

```python
potential = m * S + U  # the potential energy density m S + U(S)
# kinetic part of T^mu_mu: the sum of the K_nu with nu different from mu
kinetic_parts = np.array([K.sum() - K[mu] for mu in range(8)])
rho = -T[4, 4]  # the energy density
rho_kin = -(K.sum() - K[4])  # minus the sum of the K_mu with mu different from x4
check(abs(rho - (rho_kin + potential)) < 1e-12
      and np.abs(np.diag(T) - (kinetic_parts - potential)).max() < 1e-12,
      "rho = rho_kin + rho_pot and p_mu = (sum of the other K) - (m S + U)")
```

The split of Section 9.7: `potential` is $mS + U$; `kinetic_parts` holds, for each direction $\mu$, the sum of the kinetic terms of the other seven directions, $\sum_\nu K_\nu - K_\mu$; `rho` is $\rho = -T^{x_4}{}_{x_4}$ and `rho_kin` is $\rho_{\rm kin} = -\sum_{\mu \neq x_4}K_\mu$. The check asks $\rho = \rho_{\rm kin} + \rho_{\rm pot}$ and $p_\mu = (\text{the sum of the other } K) - (mS + U)$ for every diagonal entry.

```python
report("rho = -T^x4_x4", f"{rho:.6f}")
report("rho_kin", f"{rho_kin:.6f}")
report("rho_pot = m S + U", f"{potential:.6f}")
for mu in (0, 1, 2, 3, 5, 6, 7):
    report(f"pressure T^{NAMES[mu]}_{NAMES[mu]}", f"{T[mu, mu]:.6f}")
```

The cell prints `rho = -T^x4_x4 = -4.579050`, `rho_kin = -8.704462`, `rho_pot = m S + U = 4.125412` and the seven pressures: $T^{x_0}{}_{x_0} = 1.397139$, $T^{x_1}{}_{x_1} = 10.233713$, $T^{x_2}{}_{x_2} = 18.179608$, $T^{x_3}{}_{x_3} = 17.255533$, $T^{x_5}{}_{x_5} = 6.595341$, $T^{x_6}{}_{x_6} = 12.790979$, $T^{x_7}{}_{x_7} = -0.508841$. The energy density of this configuration is negative; the potential part is $mS + U = -6.527875 + 0.25\cdot 6.527875^2 = -6.527875 + 10.653288 = 4.125413$, the printed $4.125412$ up to the rounding of $S$ to six decimals; the three 3-space pressures differ, and so do the three extra-time pressures, because a random configuration is not isotropic.

**In [10], the bar chart of the diagonal entries.**

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
```

`positions` holds the numbers 0 to 7, one group of bars per direction. Three calls of `ax.bar` draw, side by side (shifted by $\mp0.27$), the kinetic part of each diagonal entry, the potential part $-(mS + U)$ (the same in every direction, `[-potential] * 8`) and the total $T^\mu{}_\mu$. A black horizontal line marks zero; the ticks are labelled $x_0, \dots, x_7$.

```python
save_figure(fig, "diagonal_parts",
            "The eight diagonal entries $T^\\mu{}_\\mu$ (right bar of each group) "
...)
```

The figure is saved as Figure 09a.3 (`09a_3_diagonal_parts.png`). At $x_4$ the student sees $-\rho$ (positive here, because $\rho < 0$); elsewhere the seven pressures, each the sum of a kinetic bar and the common potential bar.

**In [11], the trace, the kinetic sum and the configuration on shell.**

```python
V = m + lam * S  # V = m + U'(S), with U'(S) = lambda S
E = sum(gamma_up[mu] @ (dPhi[mu] + Omega[mu] @ Phi) for mu in range(8)) - V * Phi
E_bar = sum((bar(dPhi[mu]) - bar(Phi) @ Omega[mu]) @ gamma_up[mu]
            for mu in range(8)) + V * bar(Phi)
```

The effective mass $V = m + \lambda S$, the field-equation expression $E = \gamma^\mu D_\mu\Phi - V\Phi$ (a column) and its adjoint $\bar E = (D_\mu\bar\Phi)\gamma^\mu + V\bar\Phi$ (a row) of Section 9.8, both for the random configuration.

```python
check(abs(np.trace(T) - (7 * K.sum() - 8 * (m * S + U))) < 1e-11
      and recorded(THEORY_WL, "EMT_trace_C") == "PASS",
      "trace: sum of T^mu_mu = 7 sum K - 8 (m S + U), off shell",
      record=f"{THEORY_WL}, check EMT_trace_C")
```

The trace identity of Section 9.8, $\sum_\mu T^\mu{}_\mu = 7\sum_\mu K_\mu - 8(mS + U)$, off shell (`np.trace(T)` adds the diagonal entries), with the record's verdict of `EMT_trace_C`.

```python
kinetic_sum = V * S + 0.5 * (bar(Phi) @ E - E_bar @ Phi)
check(abs(K.sum() - kinetic_sum) < 1e-11
      and recorded(THEORY_WL, "kinetic_sum_on_shell_C") == "PASS",
      "sum K = V S + (1/2)(Phibar E - Ebar Phi), off shell",
      record=f"{THEORY_WL}, check kinetic_sum_on_shell_C")
report("|E| of the random configuration (it is off shell)",
       f"{np.linalg.norm(E):.6f}")
```

The kinetic-sum identity $\sum_\mu K_\mu = VS + \frac12(\bar\Phi E - \bar E\Phi)$, off shell, with the record's verdict of `kinetic_sum_on_shell_C`, and a RESULT line with the length of the column $E$: `|E| of the random configuration (it is off shell) = 18.019312` (`np.linalg.norm` is the square root of the sum of the squared sizes of the entries). The random configuration is far from a solution, so both identities are tested where the terms with $E$ do not vanish.

```python
# The evolution form of the field equation gives d4 Phi from the other derivatives.
rest = sum(gamma[a] @ dPhi[a] / f[a] for a in range(8) if a != 4)
dPhi_on = dPhi.copy()
dPhi_on[4] = -gamma[4] @ (V * Phi - rest - c_g * gamma[0] @ Phi) - v_g * Phi
E_on = sum(gamma_up[mu] @ (dPhi_on[mu] + Omega[mu] @ Phi) for mu in range(8)) - V * Phi
S_on, U_on, L0_on, K_on, T_on = energy_momentum(Phi, dPhi_on, f, gamma_up, gamma_down,
                                                Omega)
```

Now the configuration is put on shell at the point. `rest` is $\sum_{a \neq 4}\frac{1}{f_a}\gamma^{(a)}\partial_a\Phi$; `dPhi_on` is a copy of the derivatives in which row 4 is replaced by the evolution form of Section 9.2, $\partial_4\Phi = -\gamma^{(4)}[V\Phi - \sum_{a \neq 4}\frac{1}{f_a}\gamma^{(a)}\partial_a\Phi - c_g\gamma^{(0)}\Phi] - v_g\Phi$. `E_on` is the field-equation expression of the new jet, and `energy_momentum` gives its tensor and kinetic terms. The values of $\Phi$ are unchanged, so $S$, $V$ and $U$ stay the same.

```python
check(np.abs(E_on).max() < 1e-12, "with d4 Phi from the evolution form, E = 0")
check(abs(K_on.real.sum() - V * S) < 1e-11
      and abs(L0_on.real - (S * lam * S - U)) < 1e-11
      and abs(np.trace(T_on.real) - (-m * S + 3 * lam * S ** 2)) < 1e-10
      and recorded(THEORY_PY, "commuting_trace_on_shell") == "PASS",
      "on shell: sum K = V S, L0 = S U' - U, trace = -m S + 3 lambda S^2",
      record=f"{THEORY_PY}, check commuting_trace_on_shell")
report("trace on shell, -m S + 3 lambda S^2", f"{np.trace(T_on.real):.6f}")
```

Two checks: $E = 0$ to $10^{-12}$ (the evolution form solves the field equation exactly, which tests the terms $c_g\gamma^{(0)}$ and $v_g\gamma^{(4)}$ of Fact 2), and the on-shell values of Section 9.8, $\sum_\mu K_\mu = VS$, $L_0 = SU' - U = \lambda S^2 - U$ and the trace $-mS + 3\lambda S^2$, with the record's verdict of `commuting_trace_on_shell`. The RESULT line `trace on shell, -m S + 3 lambda S^2 = 70.447596` agrees with the formula: $6.527875 + 3\cdot 0.5\cdot 42.613152 = 6.527875 + 63.919728 = 70.447603$, up to the rounding of $S$ to six decimals.

**In [12], where the spin connection enters.**

```python
dPhi_hom = np.zeros((8, 16), dtype=complex)  # homogeneous: only d4 Phi is nonzero
dPhi_hom[4] = rng.normal(size=16) + 1j * rng.normal(size=16)
```

A homogeneous configuration at the point: the same 16 values of $\Phi$ and a jet whose only nonzero derivative is a new random column $\partial_4\Phi$ (row 4).

```python
def flow_piece(mu):
    """K^x4_mu = (1/2)(Phibar gamma^x4 D_mu Phi - D_mu Phibar gamma^x4 Phi)."""
    D_mu = dPhi_hom[mu] + Omega[mu] @ Phi  # D_mu Phi = Omega_mu Phi here
    Dbar_mu = bar(dPhi_hom[mu]) - bar(Phi) @ Omega[mu]  # = -Phibar Omega_mu here
    return 0.5 * (bar(Phi) @ gamma_up[4] @ D_mu - Dbar_mu @ gamma_up[4] @ Phi)
```

`flow_piece(mu)` computes $K^{x_4}{}_\mu = \frac12(\bar\Phi\gamma^{x_4}D_\mu\Phi - D_\mu\bar\Phi\gamma^{x_4}\Phi)$ of Section 9.12 for this configuration; for $\mu \neq x_4$ the derivative is zero, so $D_\mu\Phi = \Omega_\mu\Phi$ and $D_\mu\bar\Phi = -\bar\Phi\Omega_\mu$, as the comments say.

```python
K_41, K_45 = flow_piece(1), flow_piece(5)
expected = 0.5 * H * np.abs(np.sin(z)) ** (1 / 6) * (
    bar(Phi) @ gamma[4] @ gamma[0] @ gamma[5] @ Phi)
```

The two pieces along $x_1$ and $x_5$, and the record's value of the second, $\frac12HW\,\bar\Phi\gamma^{(4)}\gamma^{(0)}\gamma^{(5)}\Phi$ (an expression in parentheses may continue on the next line).

```python
SCOPE_PY = "Revision/theory/reports/python-scope.json"
SCOPE_WL = "Revision/theory/reports/wolfram-scope.json"
check(abs(K_41) < 1e-12 and abs(K_45 - expected) < 1e-12 and abs(K_45) > 0.01
      and recorded(SCOPE_PY, "spin_connection_in_the_energy_momentum_tensor") == "PASS"
      and recorded(SCOPE_WL, "spin_connection_in_the_energy_momentum_tensor") == "PASS",
      "homogeneous configuration: K^x4_x1 = 0, K^x4_x5 is the nonzero connection term",
      record=f"{SCOPE_PY} and {SCOPE_WL}, check "
             "spin_connection_in_the_energy_momentum_tensor")
```

The check: $K^{x_4}{}_{x_1} = 0$, $K^{x_4}{}_{x_5}$ equals the record's value, and it is not small (larger than 0.01 in size, so the comparison is not between two zeros); both scope reports must give PASS for `spin_connection_in_the_energy_momentum_tensor`.

```python
report("K^x4_x1 (homogeneous configuration)", f"{abs(K_41):.1e}")
report("K^x4_x5 (homogeneous configuration)", f"{K_45.real:.6f}")
```

The cell prints `K^x4_x1 (homogeneous configuration) = 1.1e-16`, which is zero up to rounding (the size of the last binary digit of the numbers involved), and `K^x4_x5 (homogeneous configuration) = -0.981914`.

**In [13], the Christoffel symbols with sympy.**

```python
import sympy as sp  # exact algebra and calculus with symbols

x = sp.symbols("x0:8", real=True)  # the coordinates x0, ..., x7 (x[0] ... x[7])
Hs = sp.symbols("H", positive=True)  # the author's constant, as a symbol
a4_function = sp.Function("a4")(x[4])  # a general function a4(x4)
b4_function = sp.Function("b4", positive=True)(x[4])  # a general positive b4(x4)
zs = 6 * Hs * x[0]  # z = 6 H x0
SIGNS = (1, -1)  # the sign s of sin z
```

From here on the notebook computes exactly with symbols. `sympy` is the package for exact algebra; `sp` is its short name. `sp.symbols("x0:8", real=True)` makes the eight real symbols $x_0, \dots, x_7$, so that `x[0]` is $x_0$; `Hs` is the symbol $H$, declared positive; `a4_function` and `b4_function` are general functions $a_4(x_4)$ and $b_4(x_4)$, the second declared positive; `zs` is $z = 6Hx_0$; `SIGNS` holds the two signs $s = \pm1$ of $\sin z$.

```python
def metric_for_sign(s):
    """The corrected metric where s sin z > 0, written without an absolute value."""
    block = sp.exp(-2 * a4_function) * b4_function  # e^(-2 a4) b4
    root = (s * sp.sin(zs)) ** sp.Rational(1, 3)  # (sin^2 z)^(1/6), positive
    return sp.diag(*([block * sp.cot(zs) ** 2] + [sp.exp(2 * a4_function)] * 3
                     + [-1] + [-block * root] * 3))
```

`metric_for_sign(s)` writes the corrected metric where $s\sin z > 0$. There $(\sin^2 z)^{1/6} = |\sin z|^{1/3} = (s\sin z)^{1/3}$, a positive number raised to the power $\frac13$, which sympy handles without an absolute value (`sp.Rational(1, 3)` is the exact fraction $\frac13$). `sp.diag` builds the diagonal $8 \times 8$ matrix from the list of its entries.

```python
christoffel = {}  # s -> {(lambda, mu, nu): Gamma^lambda_mu nu}, the nonzero ones
for s in SIGNS:
    g = metric_for_sign(s)
    christoffel[s] = {}
    for l in range(8):
        for i in range(8):
            for j in range(i, 8):  # mu <= nu
                value = sp.simplify((sp.diff(g[l, j], x[i]) + sp.diff(g[l, i], x[j])
                                     - sp.diff(g[i, j], x[l])) / (2 * g[l, l]))
                if value != 0:
                    christoffel[s][(l, i, j)] = value
    say(f"sign of sin z = {s:+d}: {len(christoffel[s])} nonzero Christoffel symbols "
        "with mu <= nu")
```

For each sign the triple loop runs over $\lambda$ (`l`), $\mu$ (`i`) and $\nu \geq \mu$ (`j`) and computes the diagonal formula of Section 9.9, $\Gamma^\lambda{}_{\mu\nu} = (\partial_\mu g_{\lambda\nu} + \partial_\nu g_{\lambda\mu} - \partial_\lambda g_{\mu\nu})/(2g_{\lambda\lambda})$, with `sp.diff` for the partial derivatives and `sp.simplify` to bring the result to its simplest form, so that a symbol that is zero is recognised as zero. The nonzero symbols are stored in a dictionary under the key $(\lambda, \mu, \nu)$. This is the slowest cell of the notebook ($8 \cdot 36 = 288$ expressions for each sign). It prints `sign of sin z = +1: 21 nonzero Christoffel symbols with mu <= nu` and the same line for $-1$.

**In [14], comparison with the record's list.**

```python
a4s, a4ps = sp.symbols("a4 a4p", real=True)  # plain symbols for a4 and da4/dx4
b4s = sp.Symbol("b4", positive=True)  # plain symbol for b4
b4ps = sp.Symbol("b4p", real=True)  # plain symbol for db4/dx4
```

Plain symbols `a4`, `a4p`, `b4` and `b4p` for $a_4$, $a_4'$, $b_4$ and $b_4'$, so that formulas can be compared without the function notation.

```python
def plain(expression):
    """Replace the derivatives and the functions a4(x4), b4(x4) by plain symbols."""
    expression = expression.subs({sp.Derivative(a4_function, x[4]): a4ps,
                                  sp.Derivative(b4_function, x[4]): b4ps})
    return expression.subs({a4_function: a4s, b4_function: b4s})
```

`plain` replaces in an expression the derivatives $da_4/dx_4$ and $db_4/dx_4$ by `a4p` and `b4p` (first, while the functions are still there) and then the functions $a_4(x_4)$ and $b_4(x_4)$ by `a4` and `b4`.

```python
WOLFRAM_TO_SYMPY = [  # (Wolfram text, sympy text), applied in this order
    ("Abs[Sin[6*H*x0]]", "(s*sin(6*H*x0))"),  # |sin z| = s sin z
    ("Derivative[1][a4][x4]", "a4p"), ("Derivative[1][b4][x4]", "b4p"),
    ("Derivative[1, 0][rho][x4, x0]", "rho_4"),
    ("Derivative[0, 1][p0][x4, x0]", "p0_0"), ("[x4, x0]", ""), ("a4[x4]", "a4"),
    ("b4[x4]", "b4"),
    ("Sin[", "sin("), ("Cos[", "cos("), ("Tan[", "tan("), ("Cot[", "cot("),
    ("Csc[", "csc("), ("E^", "E**"), ("^", "**"), ("[", "("), ("]", ")"),
    ("{", "["), ("}", "]")]
```

The record writes its formulas in the Wolfram Language. This list of pairs (old text, new text) translates them into sympy's notation by plain replacements, applied in order: $|\sin z|$ becomes `(s*sin(6*H*x0))` for the sign $s$, the Wolfram derivatives become the plain names `a4p`, `b4p`, `rho_4` ($\partial_4\rho$) and `p0_0` ($\partial_0p_0$), the arguments `[x4, x0]` and `[x4]` are dropped, the function names `Sin[`, `Cos[`, ... become `sin(`, `cos(`, ..., the power sign `^` becomes `**`, square brackets become round ones, and the braces of a Wolfram list become the square brackets of a Python list. The order matters: `E^` must be replaced before `^`, and the long patterns before the short ones.

```python
def from_wolfram(text):
    """Translate a formula of the record from the Wolfram Language into sympy."""
    for old, new in WOLFRAM_TO_SYMPY:
        text = text.replace(old, new)
    return text
```

`from_wolfram` applies the replacements one after the other with the string method `replace`.

```python
FORMULAS = {item["key"]: item["wl"] for item in json.loads(repository_file(
    "Revision/theory/field-theory.json").read_text(encoding="utf-8"))["formulas"]}
NAMES_SYMPY = {"a4": a4s, "a4p": a4ps, "b4": b4s, "b4p": b4ps, "H": Hs, "x0": x[0],
               "E": sp.E}
```

`FORMULAS` is a dictionary from the key of each formula of `Revision/theory/field-theory.json` to its Wolfram text (`"wl"`). `NAMES_SYMPY` tells sympy which symbol each plain name means; `"E": sp.E` makes the Wolfram constant `E` Euler's number $e$.

```python
same = True
for s in SIGNS:
    record_list = sp.sympify(from_wolfram(FORMULAS["christoffel_nonzero"]),
                             locals=dict(NAMES_SYMPY, s=s))
    # The record counts the positions 1 ... 8 (x0 ... x7); Python counts 0 ... 7.
    record_symbols = {(int(e[0]) - 1, int(e[1]) - 1, int(e[2]) - 1): e[3]
                      for e in record_list}
    same = same and sorted(record_symbols) == sorted(christoffel[s]) and all(
        sp.simplify(plain(christoffel[s][key]) - record_symbols[key]) == 0
        for key in christoffel[s])
```

For each sign the record's list `christoffel_nonzero` is translated and read by `sp.sympify` (which turns a text into a sympy expression, here a list of entries `{l, i, j, value}`); the record counts the positions from 1 to 8, Python from 0 to 7, hence the `- 1`. `same` stays `True` only if the two dictionaries have the same keys (`sorted` puts them in order) and every symbol of the notebook, written with plain names, minus the record's symbol simplifies to zero.

```python
check(all(len(christoffel[s]) == 21 for s in SIGNS) and same
      and recorded(THEORY_WL, "christoffel_count") == "PASS",
      "21 nonzero Christoffel symbols for each sign, equal to the record's list",
      record=f"{THEORY_WL}, check christoffel_count (formula christoffel_nonzero)")
```

The check: 21 symbols for each sign, the same as the record's, and the record's verdict of `christoffel_count`.

```python
for (l, i, j), value in sorted(christoffel[1].items()):
    print(f"Gamma^{NAMES[l]}_({NAMES[i]} {NAMES[j]}) = {plain(value)}")
```

The 21 symbols for $\sin z > 0$ are printed, sorted by their keys, one per line; among them

```text
Gamma^x0_(x0 x0) = -12*H/sin(12*H*x0)
Gamma^x0_(x0 x4) = -a4p + b4p/(2*b4)
Gamma^x0_(x5 x5) = H*sin(6*H*x0)**(4/3)/cos(6*H*x0)
Gamma^x4_(x0 x0) = (-a4p*b4 + b4p/2)*exp(-2*a4)*cot(6*H*x0)**2
Gamma^x5_(x0 x5) = H/tan(6*H*x0)
```

that is $-12H/\sin(12Hx_0)$, $h_4$, $H(\sin^2 z)^{1/6}\tan z = H\sin^{4/3}z/\cos z$ (for $\sin z > 0$), $h_4e^{-2a_4}b_4\cot^2 z$ and $H\cot z$: the table of Section 9.9.

**In [15], the divergence of a diagonal tensor.**

```python
rho_f, p3_f, pt_f, p0_f = [sp.Function(n)(x[4], x[0]) for n in ("rho", "p3", "pt",
                                                                 "p0")]
T_diag = sp.diag(p0_f, p3_f, p3_f, p3_f, -rho_f, pt_f, pt_f, pt_f)  # T^mu_nu
```

Four general functions $\rho$, $p_3$, $p_t$, $p_0$ of $x_4$ and $x_0$ (the expression in brackets continues on the next line), and the diagonal tensor $\mathrm{diag}(p_0, p_3, p_3, p_3, -\rho, p_t, p_t, p_t)$ in the order $x_0, \dots, x_7$.

```python
def divergence_of(symbols):
    """The eight components nabla_mu T^mu_nu of T_diag for the given symbols."""
    def gamma_symbol(l, i, j):
        """Gamma^l_ij for any order of i and j (zero when it is not stored)."""
        return symbols.get((l, min(i, j), max(i, j)), 0)
```

`divergence_of(symbols)` computes the eight components for a dictionary of Christoffel symbols. Inside it, `gamma_symbol(l, i, j)` returns $\Gamma^l{}_{ij}$ for either order of $i$ and $j$ (the dictionary stores only $i \le j$; `min` and `max` put the two indices in that order), and 0 for a symbol that is not stored (`.get(key, 0)`).

```python
    components = []
    for nu in range(8):
        value = sum(sp.diff(T_diag[mu, nu], x[mu]) for mu in range(8))
        value += sum(gamma_symbol(mu, mu, l) * T_diag[l, nu]
                     for mu in range(8) for l in range(8))
        value -= sum(gamma_symbol(l, mu, nu) * T_diag[mu, l]
                     for mu in range(8) for l in range(8))
        components.append(sp.simplify(value))
    return components
```

For each $\nu$ the three sums of the definition of Section 9.9: $\sum_\mu\partial_\mu T^\mu{}_\nu$, plus $\sum_{\mu,\lambda}\Gamma^\mu{}_{\mu\lambda}T^\lambda{}_\nu$, minus $\sum_{\mu,\lambda}\Gamma^\lambda{}_{\mu\nu}T^\mu{}_\lambda$; `+=` and `-=` add to and subtract from `value`. The lemma of Section 9.9 is not used: every symbol enters as computed.

```python
divergence = {s: divergence_of(christoffel[s]) for s in SIGNS}
for s in SIGNS:
    nonzero = [NAMES[nu] for nu in range(8) if divergence[s][nu] != 0]
    say(f"sign of sin z = {s:+d}: components of the divergence that are not "
        "identically zero: nu = " + ", ".join(nonzero))
```

The divergence for both signs, and one printed line per sign that names the components which are not identically zero: `nu = x0, x4` for both signs.

**In [16], comparison with the record and with the two lines of Section 9.9.**

```python
rho_4, p0_0, p3s, pts, p0s = sp.symbols("rho_4 p0_0 p3 pt p0", real=True)
rho_s = sp.Symbol("rho", real=True)  # the plain symbol for rho
```

Plain symbols for $\partial_4\rho$ (`rho_4`), $\partial_0p_0$ (`p0_0`), $p_3$, $p_t$, $p_0$ and $\rho$.

```python
def plain_t(expression):
    """Write the derivatives and functions as the plain symbols of the record."""
    expression = expression.subs({sp.Derivative(rho_f, x[4]): rho_4,
                                  sp.Derivative(p0_f, x[0]): p0_0})
    expression = expression.subs({p3_f: p3s, pt_f: pts, p0_f: p0s, rho_f: rho_s})
    return plain(expression)
```

`plain_t` writes a component with these plain names: first the two derivatives, then the four functions, then (with `plain`) the metric functions.

```python
NAMES_T = dict(NAMES_SYMPY, rho_4=rho_4, p0_0=p0_0, p3=p3s, pt=pts, p0=p0s, rho=rho_s)
record_divergence = sp.sympify(from_wolfram(FORMULAS["energy_exchange"][0]),
                               locals=NAMES_T)
h4s = b4ps / (2 * b4s) - a4ps  # the rate h4 of the block, with plain symbols
x4_line = (-rho_4 - 3 * a4ps * (rho_s + p3s) - 3 * h4s * (rho_s + pts)
           - h4s * (rho_s + p0s))
x0_line = p0_0 + 3 * Hs * sp.cot(zs) * (p0s - pts)
```

The record's formula `energy_exchange` is a list of three Wolfram expressions, of which the first (`[0]`) is the list of the eight components; it is translated and read. `h4s` is $h_4$ in plain symbols, and `x4_line` and `x0_line` are the two lines derived in Section 9.9: $-\partial_4\rho - 3a_4'(\rho + p_3) - 3h_4(\rho + p_t) - h_4(\rho + p_0)$ and $\partial_0p_0 + 3H\cot z\,(p_0 - p_t)$.

```python
agree = all(sp.simplify(plain_t(divergence[s][n]) - record_divergence[n]) == 0
            for s in SIGNS for n in range(8))
check(agree and recorded(THEORY_WL, "energy_exchange_equation") == "PASS"
      and recorded(THEORY_PY, "energy_exchange_equation") == "PASS",
      "the eight components agree with the record formula energy_exchange",
      record=f"{THEORY_WL} and {THEORY_PY}, check energy_exchange_equation")
```

All eight components of both signs must equal the record's, and both field-theory reports must give PASS for `energy_exchange_equation`.

```python
check(all(sp.simplify(plain_t(divergence[s][4]) - x4_line) == 0 for s in SIGNS)
      and recorded(LEAD, "divergence_x4_component") == "PASS",
      "nabla_mu T^mu_x4 = -d4 rho - 3 a4' (rho + p3) - 3 h4 (rho + p_t) "
      "- h4 (rho + p0)",
      record=f"{LEAD}, check divergence_x4_component")
check(all(sp.simplify(plain_t(divergence[s][0]) - x0_line) == 0 for s in SIGNS)
      and recorded(LEAD, "divergence_x0_component") == "PASS",
      "nabla_mu T^mu_x0 = d0 p0 + 3 H cot z (p0 - p_t)",
      record=f"{LEAD}, check divergence_x0_component")
check(all(divergence[s][n] == 0 for s in SIGNS for n in (1, 2, 3, 5, 6, 7))
      and recorded(LEAD, "divergence_other_components_zero") == "PASS",
      "the components x1, x2, x3, x5, x6, x7 vanish identically",
      record=f"{LEAD}, check divergence_other_components_zero")
```

Three more checks, each with a check of the lead's independent report: the $x_4$ component equals `x4_line`, the $x_0$ component equals `x0_line`, and the components $x_1, x_2, x_3, x_5, x_6, x_7$ vanish identically, for both signs.

```python
say(f"nabla_mu T^mu_x4 = {x4_line}")  # rho_4 = d rho/d x4, b4p = d b4/d x4
say(f"nabla_mu T^mu_x0 = {x0_line}")  # p0_0 = d p0/d x0
```

The two lines are printed in sympy's notation (the first one is wrapped, with $3h_4 = -3a_4' + \frac{3b_4'}{2b_4}$):

```text
nabla_mu T^mu_x4 = -3*a4p*(p3 + rho) - rho_4 - (-3*a4p + 3*b4p/(2*b4))*(pt + rho) - (-a4p
    + b4p/(2*b4))*(p0 + rho)
nabla_mu T^mu_x0 = 3*H*(p0 - pt)*cot(6*H*x0) + p0_0
```

**In [17], the first law.**

```python
first_law_holds = True
for s in SIGNS:
    block = sp.exp(-a4_function) * sp.sqrt(b4_function)  # e^(-a4) b4^(1/2)
    V3 = sp.exp(3 * a4_function)  # f1 f2 f3 = e^(3 a4)
    Vt = block ** 3 * (s * sp.sin(zs)) ** sp.Rational(1, 2)  # f5 f6 f7
    V0 = block * sp.cot(zs)  # f0, signed (its sign cancels below)
    V7 = V3 * Vt * V0  # sign(cot z) times sqrt|g|
    signed_volume = (sp.exp(-a4_function) * b4_function ** 2 * sp.cot(zs)
                     * (s * sp.sin(zs)) ** sp.Rational(1, 2))
```

For each sign of $\sin z$ the volumes of the first-law reading of Section 9.10 are written with symbols: `block` is $s_b$, $V_3 = e^{3a_4}$, $V_t = s_b^3(s\sin z)^{1/2}$ (that is $s_b^3W^3$), $V_0 = f_0 = s_b\cot z$, kept with its sign, and $V_7 = V_3V_tV_0$; `signed_volume` is $\mathrm{sign}(\cot z)\sqrt{|g|} = e^{-a_4}b_4^2\cot z\,(s\sin z)^{1/2}$.

```python
    first_law = (sp.diff(rho_f * V7, x[4]) + p3_f * V7 / V3 * sp.diff(V3, x[4])
                 + pt_f * V7 / Vt * sp.diff(Vt, x[4])
                 + p0_f * V7 / V0 * sp.diff(V0, x[4]))
    # The first law says first_law = 0; it must be -V7 times the x4 divergence.
    first_law_holds = (first_law_holds
                       and sp.simplify(V7 - signed_volume) == 0
                       and sp.simplify(first_law + V7 * divergence[s][4]) == 0)
```

`first_law` is $\frac{d}{dx_4}(\rho V_7) + p_3\frac{V_7}{V_3}\frac{dV_3}{dx_4} + p_t\frac{V_7}{V_t}\frac{dV_t}{dx_4} + p_0\frac{V_7}{V_0}\frac{dV_0}{dx_4}$, which the first law says is zero. The cell asks two exact equalities: $V_7$ is the signed volume, and `first_law` is $-V_7$ times the $x_4$ component of the divergence of In [15]; so the first law holds exactly when the conservation identity holds. The sign of $V_0$ appears on both sides and cancels.

```python
check(first_law_holds,
      "V3 Vt V0 = sign(cot z) sqrt|g|, and the first law is the x4 identity")
```

One PASS line: `V3 Vt V0 = sign(cot z) sqrt|g|, and the first law is the x4 identity`.

**In [18], the volumes along the history.**

```python
x4_axis = np.linspace(0.0, 8.0, 401)  # the time x4
a4_history = A * H * x4_axis  # a4 along the history
b4_history = np.exp(beta * A * H * x4_axis)  # b4 along the history (unit b4(0))
V3_ratio = np.exp(3 * a4_history)  # V3(x4)/V3(0) = e^(3 a4)
block_ratio = np.exp(-a4_history) * np.sqrt(b4_history)  # e^(-a4) b4^(1/2)
Vt_ratio = block_ratio ** 3  # the three extra times
V0_ratio = block_ratio  # the hidden direction
V7_ratio = V3_ratio * Vt_ratio * V0_ratio  # e^(-a4) b4^2
```

401 times from 0 to 8, the history $a_4 = AHx_4$, $b_4 = e^{\beta AHx_4}$, and the four volumes divided by their values at $x_4 = 0$: $V_3 \propto e^{3a_4}$, the block factor $s_b$, $V_t \propto s_b^3$, $V_0 \propto s_b$ and $V_7 = V_3V_tV_0$ (the factors of $z$ are constants and cancel in the ratios).

```python
fig, ax = plt.subplots()
ax.plot(x4_axis, V3_ratio, label="3-space volume $V_3$ (inflates)")
ax.plot(x4_axis, Vt_ratio, "--", label="extra-time volume $V_t$ (deflates)")
ax.plot(x4_axis, V0_ratio, "-.", label="hidden length $V_0$ (deflates)")
ax.plot(x4_axis, V7_ratio, ":", color="black",
        label="7-volume $V_7 = V_3 V_t V_0 = \\sqrt{|g|}$")
ax.set_yscale("log")
ax.set_xlabel("time $x_4$")
ax.set_ylabel("volume divided by its value at $x_4 = 0$")
ax.set_title("Volumes along the history ($A = 1$, $\\beta = 4/3$, $H = 0.25$)")
ax.legend(fontsize=8)
```

Four curves on a logarithmic vertical axis, with labels, a title and a legend.

```python
save_figure(fig, "volumes_first_law",
            "The 3-space volume $V_3 = e^{3a_4}$ (solid), the extra-time volume "
...)
```

The figure is saved as Figure 09a.4 (`09a_4_volumes_first_law.png`). On the logarithmic axis each curve is a straight line: $V_3$ rises with the slope $3AH = 0.75$ (a factor $e^6 = 403$ at $x_4 = 8$), $V_t$ falls with the slope $AH$ (a factor $e^{-2} = 0.135$), $V_0$ with $AH/3$ (a factor $e^{-2/3} = 0.513$), and $V_7$ rises with $\frac53AH$ (a factor $e^{10/3} = 28.0$).

**In [19], the profiles of the x0 balance and the hidden coordinate y.**

```python
P, c = sp.symbols("P c", real=True)  # P = p_t (a constant) and the constant c
y = sp.symbols("y", real=True)
P0, PT = [sp.Function(n)(y) for n in ("P0", "PT")]  # p0 and p_t as functions of y
profiles_hold, jacobian_holds, y_form_holds = True, True, True
```

Symbols for the constant pressure $P$ and the constant $c$, the coordinate $y$, two general functions $p_0(y)$ and $p_t(y)$ (named `P0` and `PT`), and three flags that stay `True` while every test passes.

```python
for s in SIGNS:
    profile = P + c * (s * sp.sin(zs)) ** sp.Rational(-1, 2)  # p0 = P + c |sin z|^(-1/2)
    balance = sp.diff(profile, x[0]) + 3 * Hs * sp.cot(zs) * (profile - P)
    profiles_hold = profiles_hold and sp.simplify(balance) == 0
```

For each sign: the profile $p_0 = P + c\,(s\sin z)^{-1/2}$ of Section 9.11 (that is $P + c(\sin^2 z)^{-1/4}$) is put into the balance $\partial_0p_0 + 3H\cot z\,(p_0 - P)$, which must simplify to zero.

```python
    y_of_x0 = sp.log(s * sp.sin(zs)) / (6 * Hs)  # y = ln|sin z|/(6 H)
    jacobian_holds = (jacobian_holds
                      and sp.simplify(sp.diff(y_of_x0, x[0]) - sp.cot(zs)) == 0)
    in_x0 = (sp.diff(P0.subs(y, y_of_x0), x[0])
             + 3 * Hs * sp.cot(zs) * (P0.subs(y, y_of_x0) - PT.subs(y, y_of_x0)))
    in_y = sp.cot(zs) * (sp.diff(P0, y).subs(y, y_of_x0)
                         + 3 * Hs * (P0.subs(y, y_of_x0) - PT.subs(y, y_of_x0)))
    y_form_holds = y_form_holds and sp.simplify(in_x0 - in_y) == 0
```

The hidden coordinate $y = \ln|\sin z|/(6H) = \ln(s\sin z)/(6H)$: its derivative must be $\cot z$, and the $x_0$ component written with $p_0(y(x_0))$ and $p_t(y(x_0))$ must equal $\cot z\,[p_0'(y) + 3H(p_0 - p_t)]$ (`.subs(y, y_of_x0)` puts $y(x_0)$ in place of $y$; sympy applies the chain rule in `sp.diff`).

```python
check(profiles_hold, "p0 = P + c (sin^2 z)^(-1/4) solves the x0 identity for every c")
check(jacobian_holds and recorded(LEAD, "ks_coordinate_jacobian") == "PASS",
      "y = ln|sin z|/(6 H) has dy/dx0 = cot z",
      record=f"{LEAD}, check ks_coordinate_jacobian")
check(y_form_holds and recorded(LEAD, "ks_coordinate_form") == "PASS",
      "x0 component = cot z [p0'(y) + 3 H (p0 - p_t)]",
      record=f"{LEAD}, check ks_coordinate_form")
```

Three PASS lines; the second and the third reproduce the lead's checks `ks_coordinate_jacobian` and `ks_coordinate_form`.

**In [20], the drawn profiles.**

```python
z_grid = np.linspace(0.1, np.pi - 0.1, 2001)  # z across the fold at pi/2
x0_grid = z_grid / (6 * H)  # the matching x0 = z/(6 H)
fig, ax = plt.subplots()
worst = 0.0  # the largest relative residual of the balance on the grid
```

2001 values of $z$ from $0.1$ to $\pi - 0.1$, across the fold, the matching $x_0 = z/(6H)$, an empty figure, and `worst`, the largest relative residual found so far.

```python
for c_value in (-0.4, -0.2, 0.0, 0.2, 0.4):
    p0_values = 1.0 + c_value * (np.sin(z_grid) ** 2) ** (-1 / 4)  # P = 1
    slope = np.gradient(p0_values, x0_grid)  # d p0/d x0, by finite differences
    rhs = -3 * H / np.tan(z_grid) * (p0_values - 1.0)
    # The size of the terms; 1 (the size of P) is added, so that for the flat
    # profile c = 0, whose terms are zero, rounding noise is not divided by zero.
    scale = 1.0 + np.abs(slope).max() + np.abs(rhs).max()
    # [5:-5] leaves out five points at each end, where np.gradient is less exact.
    worst = max(worst, np.abs(slope - rhs)[5:-5].max() / scale)
    style = "-" if c_value == 0.0 else "--"
    ax.plot(z_grid, p0_values, style, label=f"$c = {c_value:g}$")  # g: short form
```

For five values of $c$ the profile with $P = 1$ is computed; `np.gradient` approximates $\partial_0p_0$ by finite differences on the grid (Chapter 2), `rhs` is the right side $-3H\cot z\,(p_0 - p_t)$ of the balance; `scale` is the size of the terms (plus 1, as the comment explains), and the largest difference between the two sides, without five points at each end where `np.gradient` is less exact, divided by `scale`, updates `worst`. The profile $c = 0$ is drawn solid, the others dashed; `:g` writes a number in its shortest form.

```python
check(worst < 1e-4, "the drawn profiles satisfy the x0 balance on the grid")
ax.axvline(np.pi / 2, color="gray", linewidth=0.8)  # the fold
ax.set_ylim(-0.5, 2.5)
ax.set_xlabel("$z = 6 H x_0$ (fold at $\\pi/2$)")
ax.set_ylabel("$p_0$ (with $p_t = 1$)")
ax.set_title("Pressure profiles allowed by the balance along $x_0$")
ax.legend(fontsize=8)
```

The check asks a relative residual below $10^{-4}$ (the error of the finite differences); a gray line marks the fold; the vertical range is fixed from $-0.5$ to $2.5$; labels, title and legend.

```python
save_figure(fig, "hidden_balance",
            "The hidden-direction pressure profiles $p_0 = P + c\\,(\\sin^2 z)^{-1/4}$ "
...)
report("largest relative residual of the balance on the grid", f"{worst:.1e}")
```

The figure is saved as Figure 09a.5 (`09a_5_hidden_balance.png`), and the RESULT line `largest relative residual of the balance on the grid = 5.0e-05` is printed. The student sees the flat line $p_0 = 1 = p_t$ for $c = 0$ and four profiles that are flat at the fold and grow in size towards $z = 0.1$ and $z = \pi - 0.1$, symmetric about the fold.

**In [21], the source of the record's history.**

```python
WARPED = "Revision/metric_warped/results/warped-metric.json"
sources = json.loads(repository_file(WARPED).read_text(encoding="utf-8"))[
    "history_source"]
x4s = sp.Symbol("x4", real=True)  # the time as a plain symbol
a4p_history, h4_history = Hs, sp.Rational(4, 3) * Hs / 2 - Hs  # H and -H/3
sources_conserved = True
```

The record of the corrected metric is read and its entry `history_source` kept; `x4s` is the time as a plain symbol; on the history $a_4' = H$ and $h_4 = \frac23H - H = -\frac{H}{3}$, written exactly with `sp.Rational(4, 3)`.

```python
for key in ("einstein_A1_beta43", "author_weights_A1_beta43"):
    entry = {name: sp.sympify(text, locals={"H": Hs, "x4": x4s})
             for name, text in sources[key].items()}
    rho_h, p3_h, pt_h, p0_h = -entry["-rho"], entry["p3"], entry["p_t"], entry["p0"]
    x4_identity = (-sp.diff(rho_h, x4s) - 3 * a4p_history * (rho_h + p3_h)
                   - 3 * h4_history * (rho_h + pt_h) - h4_history * (rho_h + p0_h))
    sources_conserved = (sources_conserved and sp.simplify(x4_identity) == 0
                         and sp.simplify(p0_h - pt_h) == 0)
    if key == "einstein_A1_beta43":
        say(f"Einstein: rho = {rho_h}, p3 = {p3_h}, p_t = p0 = {pt_h}")
```

For the two listed sources, Einstein's theory and the author's Lovelock weights, the four entries (texts in sympy's notation) are read by `sp.sympify`; the record stores $-\rho$, so $\rho$ is its negative. The $x_4$ identity of Section 9.10 is formed and must simplify to zero, and $p_0 - p_t$ must vanish. For the Einstein source the cell prints

```text
Einstein: rho = -H**2*(18*exp(2*H*x4/3) + 1)/3, p3 = H**2*(54*exp(2*H*x4/3) - 13)/9, p_t
    = p0 = H**2*(9*exp(2*H*x4/3) - 11)/3
```

the source checked by hand in Section 9.11.

```python
A4_PY = "Revision/field_equations_a4/reports/python-a4-report.json"
check(sources_conserved
      and recorded(A4_REPORT, "author_weights_history_source") == "PASS"
      and recorded(A4_PY, "author_weights_history_source") == "PASS",
      "the history source (Einstein, author's weights) obeys the x4 identity",
      record=f"{A4_REPORT} and {A4_PY}, check author_weights_history_source")
```

The check, with the verdicts of `author_weights_history_source` in both field-equations reports.

```python
check(recorded(A4_REPORT, "independent_components") == "PASS"
      and recorded(A4_PY, "independent_components") == "PASS",
      "the field equations need p0 = p_t and no off-diagonal source",
      record=f"{A4_REPORT} and {A4_PY}, check independent_components")
```

A last record check: both field-equations reports state that the field equations need $p_0 = p_t$ and no off-diagonal source (`independent_components`), the condition that the $x_0$ identity gives for entries free of $x_0$.

**In [22], the last check.**

```python
captions = json.loads(output_file(CAPTION_FILE).read_text(encoding="utf-8"))
expected_files = ["09a_1_kinetic_weights.png", "09a_2_tensor_heat_map.png",
                  "09a_3_diagonal_parts.png", "09a_4_volumes_first_law.png",
                  "09a_5_hidden_balance.png"]
```

The captions file `09a.captions.json` (`CAPTION_FILE`, In [1]) is read back, and `expected_files` lists the five figure files of this notebook.

```python
check(sorted(captions) == expected_files and all(
    output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in expected_files),
    "the five figures of this notebook are saved and captioned")
all_checks_passed()
```

The check: the captions file names exactly these five files, and each of them exists. Then `all_checks_passed()` prints the last line, `ALL 29 CHECKS PASSED (notebook 09a)`.

### 9.18 Condensates: solutions that depend on the time only

A **condensate** (also called a **homogeneous configuration**) is a field that is the same at every place: it depends on the time $x_4$ only, not on $x_0, x_1, x_2, x_3, x_5, x_6, x_7$. Condensates are the simplest candidates for a smooth cosmological fluid, and the record reduces their field equation to a linear system of 16 equations.

**The field equation of a condensate.** In the explicit field equation of Section 9.2 every derivative term with $a \neq 4$ vanishes, and $f_4 = 1$:

$$
\gamma^{(4)}\partial_4\Phi + c_g\gamma^{(0)}\Phi + v_g\gamma^{(4)}\Phi = V\Phi, \qquad V = m + \lambda S, \qquad c_g = \tfrac32He^{a_4}b_4^{-1/2}, \qquad v_g = \frac{b_4'}{b_4} - \frac{a_4'}{2} .
$$

**Removing the dilution.** Write $\Phi = F\chi$ with the factor $F = e^{a_4/2}b_4^{-1}$. Line by line:

$$
\begin{aligned}
\frac{dF}{dx_4} &= \frac{d}{dx_4}\Big(\frac{a_4}{2} - \ln b_4\Big)\cdot F = \Big(\frac{a_4'}{2} - \frac{b_4'}{b_4}\Big)F = -v_g\,F, \\
\partial_4\Phi &= F\chi' + F'\chi = F\big(\chi' - v_g\chi\big), \\
\gamma^{(4)}\partial_4\Phi + v_g\gamma^{(4)}\Phi &= F\big(\gamma^{(4)}\chi' - v_g\gamma^{(4)}\chi + v_g\gamma^{(4)}\chi\big) = F\gamma^{(4)}\chi' .
\end{aligned}
$$

The first line uses $F' = (\ln F)'\,F$ with $\ln F = \frac{a_4}{2} - \ln b_4$, and differentiates; the second is the product rule, with $\chi' = d\chi/dx_4$; the third inserts the second and $\Phi = F\chi$: the two terms with $v_g$ cancel. So the factor $F$ absorbs the term $v_g\gamma^{(4)}$ of the field equation. Divide the field equation by $F$ and multiply it from the left by $-\gamma^{(4)}$. Because $(\gamma^{(4)})^2 = -1$, the first term becomes $\chi'$, the term with $c_g$ becomes $-c_g\gamma^{(4)}\gamma^{(0)}\chi$, and the right side $-V\gamma^{(4)}\chi$. Moving the second term to the right:

$$
\chi' = M\chi, \qquad M = -V\gamma^{(4)} + c_g\gamma^{(4)}\gamma^{(0)} .
$$

The coordinate $x_0$ does not appear: a condensate solves the field equation at every $x_0$ between the degenerate points. The functions $a_4$ and $b_4$ appear in the factor $F$, in $c_g$, and, through $S$, in $V$ (the record's entry and check are named in the table at the end of this section).

**The scalar of $\chi$ is constant, and $S$ is diluted.** The equation is nonlinear, because $V$ contains $S = \Phi^\dagger C\Phi$. Consider first the number $\chi^\dagger C\chi$. By the product rule,

$$
\frac{d}{dx_4}\big(\chi^\dagger C\chi\big) = (M\chi)^\dagger C\chi + \chi^\dagger CM\chi = \chi^\dagger\big(M^TC + CM\big)\chi ,
$$

where the last step uses $(M\chi)^\dagger = \chi^\dagger M^\dagger$ and $M^\dagger = M^T$ ($M$ is real, because $V$ and $c_g$ are real numbers). Now compute $M^TC$. From the antisymmetry of $C\gamma^{(a)}$ and the symmetry of $C$: $\gamma^{(a)T}C = (C\gamma^{(a)})^T = -C\gamma^{(a)}$. Hence

$$
\begin{aligned}
\gamma^{(4)T}C &= -C\gamma^{(4)}, \\
\big(\gamma^{(4)}\gamma^{(0)}\big)^TC &= \gamma^{(0)T}\gamma^{(4)T}C = -\gamma^{(0)T}C\gamma^{(4)} = C\gamma^{(0)}\gamma^{(4)} = -C\gamma^{(4)}\gamma^{(0)}, \\
M^TC &= -V\gamma^{(4)T}C + c_g\big(\gamma^{(4)}\gamma^{(0)}\big)^TC = VC\gamma^{(4)} - c_gC\gamma^{(4)}\gamma^{(0)} = -CM .
\end{aligned}
$$

The first line is the rule just stated; the second applies it twice (the transpose of a product is the product of the transposes in reverse order) and then uses $\gamma^{(0)}\gamma^{(4)} = -\gamma^{(4)}\gamma^{(0)}$; the third inserts both. So $M^TC + CM = 0$ for all values of $V$ and $c_g$, and $\chi^\dagger C\chi$ keeps its initial value $S_0 = \chi_0^\dagger C\chi_0$, where $\chi_0 = \chi(0)$ is the value at $x_4 = 0$. The scalar of the field is therefore

$$
S = \Phi^\dagger C\Phi = F^2\,\chi^\dagger C\chi = e^{a_4}b_4^{-2}\,S_0 :
$$

$e^{-a_4}b_4^2S$ is constant, and $S$ is **diluted** at exactly the rate at which the volume factor $\sqrt{|g|} = e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}$ of Section 9.2 grows, so that $S\sqrt{|g|}$ does not change in time. On the history, with $b_4(0) = 1$, $e^{a_4}b_4^{-2} = e^{AHx_4 - \frac83AHx_4} = e^{-(5/3)AHx_4}$. Then $V = m + \lambda S_0e^{a_4}b_4^{-2}$ is a known function of the time, and the equation $\chi' = M\chi$ is linear: once $S_0$ is fixed by the initial value, $M = M(x_4)$ no longer depends on $\chi$.

**The square of $M$.** Multiply out $M^2 = (-V\gamma^{(4)} + c_g\gamma^{(4)}\gamma^{(0)})(-V\gamma^{(4)} + c_g\gamma^{(4)}\gamma^{(0)})$:

$$
\begin{aligned}
M^2 &= V^2\gamma^{(4)}\gamma^{(4)} - c_gV\big(\gamma^{(4)}\gamma^{(4)}\gamma^{(0)} + \gamma^{(4)}\gamma^{(0)}\gamma^{(4)}\big) + c_g^2\gamma^{(4)}\gamma^{(0)}\gamma^{(4)}\gamma^{(0)} \\
&= -V^2 - c_gV\big(-\gamma^{(0)} + \gamma^{(0)}\big) + c_g^2\cdot 1 \\
&= \big(c_g^2 - V^2\big)\cdot 1 = k^2\cdot 1, \qquad k^2 = c_g^2 - V^2 .
\end{aligned}
$$

The first line multiplies out the four products; the second uses $\gamma^{(4)}\gamma^{(4)} = -1$, then $\gamma^{(4)}\gamma^{(0)}\gamma^{(4)} = -\gamma^{(4)}\gamma^{(4)}\gamma^{(0)} = \gamma^{(0)}$, and $\gamma^{(4)}\gamma^{(0)}\gamma^{(4)}\gamma^{(0)} = -\gamma^{(4)}\gamma^{(4)}\gamma^{(0)}\gamma^{(0)} = -(-1)(+1) = 1$; the third collects. This holds at every moment, with the values of $V$ and $c_g$ at that moment. (The letter $k$ of this chapter is this number; it is not the ratio $e^{2a_4}/b_4$ that the record also calls $k$, and which Section 9.26 writes out.)

**When the matrices of two moments commute.** Let $M_1$ and $M_2$ be the matrices at two moments, with the values $V_1, c_1$ and $V_2, c_2$. With the same three products as above,

$$
\begin{aligned}
M_1M_2 &= -V_1V_2 + V_1c_2\gamma^{(0)} - c_1V_2\gamma^{(0)} + c_1c_2, \\
M_2M_1 &= -V_1V_2 + V_2c_1\gamma^{(0)} - c_2V_1\gamma^{(0)} + c_1c_2, \\
M_1M_2 - M_2M_1 &= 2\big(V_1c_2 - V_2c_1\big)\gamma^{(0)} .
\end{aligned}
$$

The first line multiplies out ($-V_1\gamma^{(4)}\cdot c_2\gamma^{(4)}\gamma^{(0)} = +V_1c_2\gamma^{(0)}$ and $c_1\gamma^{(4)}\gamma^{(0)}\cdot(-V_2\gamma^{(4)}) = -c_1V_2\gamma^{(0)}$); the second exchanges the labels 1 and 2; the third subtracts. The two matrices commute only if $V/c_g$ has the same value at the two moments. When they do not commute, the solution is not the exponential of one matrix.

**The exact solution when $M$ is constant.** If $V$ and $c_g$ are both constant, which happens for $\lambda = 0$ (then $V = m$) on a history along which $e^{2a_4}/b_4$ keeps a constant value $k_0$ (then $c_g = \frac32H\sqrt{k_0}$; Section 9.26 uses these histories), $M$ is a constant matrix. For a number $k$ the exponential series $e^{kx} = \sum_n (kx)^n/n!$ splits into its even and odd terms, $\cosh(kx) = \sum_j (kx)^{2j}/(2j)!$ and $\sinh(kx) = \sum_j (kx)^{2j+1}/(2j+1)!$. The same series with the matrix $Mx_4$ in place of $kx$ defines the **matrix exponential** $e^{Mx_4}$, and $e^{Mx_4}\chi_0$ solves $\chi' = M\chi$ with $\chi(0) = \chi_0$. Because $M^2 = k^2$, every even power is $M^{2j} = k^{2j}$ and every odd power is $M^{2j+1} = k^{2j}M$, so the even terms sum to $\cosh(kx_4)$ and the odd terms to $\frac{\sinh(kx_4)}{k}M$:

$$
\Phi(x_4) = F\Big(\cosh(kx_4) + \frac{\sinh(kx_4)}{k}\,M\Big)\chi_0 .
$$

A direct check, without series: at $x_4 = 0$ the bracket is 1; its derivative is $k\sinh(kx_4) + \cosh(kx_4)M$; and $M$ times the bracket is $\cosh(kx_4)M + \frac{\sinh(kx_4)}{k}M^2 = \cosh(kx_4)M + k\sinh(kx_4)$ (using $M^2 = k^2$), the same. Three cases:

- $k^2 < 0$, that is $|V| > c_g$: $k = i\omega$ with $\omega = \sqrt{V^2 - c_g^2}$; since $\cosh(i\omega x) = \cos(\omega x)$ and $\sinh(i\omega x)/(i\omega) = \sin(\omega x)/\omega$, the column $\chi$ **oscillates** with the angular frequency $\omega$;
- $k^2 > 0$, that is $|V| < c_g$: the column contains $e^{kx_4}$ and **grows**;
- $k^2 = 0$: the limit $\chi = \chi_0 + x_4M\chi_0$.

In every case the field itself carries the factor $F = e^{a_4/2}b_4^{-1}$.

**On the record's history there is no closed formula.** There $c_g = \frac32He^{AHx_4/3}$ grows (in the unit $b_4(0) = 1$), and for $\lambda \neq 0$ also $V$ changes; $V/c_g$ is not constant, so by the commutator above the matrices of different moments do not commute, and the record gives no closed formula. It proves instead that **every** solution $\chi$ of the linear system $\chi' = M(x_4)\chi$ with $V = m + \lambda S_0e^{a_4}b_4^{-2}$ gives an exact solution $\Phi = e^{a_4/2}b_4^{-1}\chi$ of the nonlinear field equation, for all functions $a_4$ and $b_4$ (PROVED; record formula `exact_solutions` of `Revision/theory/field-theory.json`, and the checks in the table). Notebook 09b solves the 16 linear equations with the Runge-Kutta method of Chapter 2 and checks the field equation on the result (COMPUTED). At each moment the sign of $k^2 = c_g(x_4)^2 - V(x_4)^2$ says whether the column oscillates ($|V| > c_g$) or grows ($|V| < c_g$) at that moment; as $S$ is diluted, $V$ approaches $m$, while $c_g$ grows without bound.

| statement | Revision report | check |
| --- | --- | --- |
| $M^2 = k^2\cdot 1$ and $M^TC + CM = 0$ | `Revision/theory/reports/wolfram-field-theory.json` | `solution_matrix_square` |
| the condensate equation is free of $x_0$ and has the solutions $\Phi = e^{a_4/2}b_4^{-1}\chi$ | `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `condensate_equation_x0_consistent` |
| the same, as an entry of the field-equations record | `Revision/field_equations_a4/a4-equations.json` | entry `fields.dirac16complex00.homogeneousCondensate` |
| every solution of $\chi' = M(x_4)\chi$ gives the solution $\Phi = e^{a_4/2}b_4^{-1}\chi$, with $S = e^{a_4}b_4^{-2}S_0$ | `Revision/theory/reports/wolfram-field-theory.json` | `exact_solution_nonlinear_homogeneous_C` |
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

In the first line all seven kinetic terms vanish; in the second the only kinetic term left in the sum is $K_4$ (because $\mu \neq x_4$), which is $VS = (m + U')S$. The pressure is the same in all seven directions, $p_3 = p_t = p_0 = p$. The kinetic part of the energy density is zero, the kinetic part of every pressure is $VS$, the potential parts are $\pm(mS + U)$. For $U = \frac{\lambda}{2}S^2$, with $SU' = \lambda S^2$:

$$
\rho = mS + \tfrac{\lambda}{2}S^2, \qquad p = \lambda S^2 - \tfrac{\lambda}{2}S^2 = \tfrac{\lambda}{2}S^2 .
$$

(PROVED; `Revision/theory/reports/python-field-theory.json`, check `commuting_homogeneous_on_shell_rho_p`; record formula `EMT_homogeneous_on_shell`, which notes that the factor $e^{a_4/2}b_4^{-1}$ of $\Phi$ and $\bar\Phi$ cancels in $K_4$.) The trace is $-\rho + 7p = -mS - \frac{\lambda}{2}S^2 + \frac{7\lambda}{2}S^2 = -mS + 3\lambda S^2$, as Section 9.8 requires. Because $S = e^{a_4}b_4^{-2}S_0$ is diluted, $\rho$ and $p$ change in time. This agrees with the identity of Section 9.10: with $p_3 = p_t = p_0 = p$ the work terms reduce to the dilution, and the identity requires $d\rho/dx_4 = -(3a_4' + 4h_4)(\rho + p)$. Indeed, line by line,

$$
\begin{aligned}
\frac{dS}{dx_4} &= \big(a_4' - 2u\big)\,S = -\big(3a_4' + 4h_4\big)\,S, \\
\frac{d\rho}{dx_4} &= \big(m + \lambda S\big)\frac{dS}{dx_4} = -\big(3a_4' + 4h_4\big)\big(mS + \lambda S^2\big) = -\big(3a_4' + 4h_4\big)\big(\rho + p\big),
\end{aligned}
$$

where the first line differentiates $S = e^{a_4}b_4^{-2}S_0$ ($\ln S = a_4 - 2\ln b_4 + \ln S_0$) and uses $2u - a_4' = 3a_4' + 4h_4$ (Section 9.2); the second applies the chain rule to $\rho = mS + \frac{\lambda}{2}S^2$, inserts the first line, and uses $\rho + p = mS + \lambda S^2$. A condensate exchanges no energy between 3-space and the block; it is only diluted.

**No $x_4$-$x_0$ flow.** The record gives the entry (formula `EMT_offdiagonal_x4_x0`)

$$
\begin{aligned}
T^{x_4}{}_{x_0} &= -\tfrac14\big(B_{40} - e^{-a_4}b_4^{1/2}\cot z\,B_{04}\big), \\
B_{40} &= \bar\Phi\gamma^{(4)}\partial_0\Phi - \partial_0\bar\Phi\,\gamma^{(4)}\Phi, \qquad B_{04} = \bar\Phi\gamma^{(0)}\partial_4\Phi - \partial_4\bar\Phi\,\gamma^{(0)}\Phi .
\end{aligned}
$$

For a condensate $B_{40} = 0$ (no $x_0$ derivative). For $B_{04}$ write $\Phi = F\chi$: then $\partial_4\Phi = F(M - v_g)\chi$, and $\partial_4\bar\Phi = F\big((M - v_g)\chi\big)^\dagger C = F\chi^\dagger(M^TC - v_gC) = -F\bar\chi(M + v_g)$ with $\bar\chi = \chi^\dagger C$ (the rule $M^TC = -CM$), so

$$
\begin{aligned}
B_{04} &= F^2\Big(\bar\chi\gamma^{(0)}\big(M - v_g\big)\chi + \bar\chi\big(M + v_g\big)\gamma^{(0)}\chi\Big) = F^2\,\bar\chi\{\gamma^{(0)}, M\}\chi \\
&= F^2\,\bar\chi\big(-V\{\gamma^{(0)}, \gamma^{(4)}\} + c_g\{\gamma^{(0)}, \gamma^{(4)}\gamma^{(0)}\}\big)\chi = 0 .
\end{aligned}
$$

The first line inserts the two derivatives (the two terms with $v_g$ cancel); the second inserts $M$, and both anticommutators vanish: $\{\gamma^{(0)}, \gamma^{(4)}\} = 2\eta^{04} = 0$ and $\{\gamma^{(0)}, \gamma^{(4)}\gamma^{(0)}\} = \gamma^{(0)}\gamma^{(4)}\gamma^{(0)} + \gamma^{(4)}\gamma^{(0)}\gamma^{(0)} = -\gamma^{(4)} + \gamma^{(4)} = 0$. So $T^{x_4}{}_{x_0} = 0$, and $T^{x_0}{}_{x_4} = -e^{2a_4}b_4^{-1}\tan^2 z\,T^{x_4}{}_{x_0} = 0$ (PROVED; check `commuting_T_x4x0_homogeneous`). The other entries off the diagonal are not zero in general (Section 9.26).

**The equation of state.** For $S \neq 0$, divide the numerator and the denominator of $p/\rho$ by $mS/2$:

$$
w = \frac{p}{\rho} = \frac{\frac{\lambda}{2}S^2}{mS + \frac{\lambda}{2}S^2} = \frac{\lambda S/m}{2 + \lambda S/m} = \frac{x}{2 + x}, \qquad x = \frac{\lambda S}{m} .
$$

(The record writes it $w = \lambda S/(2m + \lambda S)$.) It depends on $m$, $\lambda$ and $S$ only through $x$, and the effective mass is $V = m + \lambda S = m(1 + x)$. Because $S = e^{a_4}b_4^{-2}S_0$, the number $x = \lambda S_0e^{a_4}b_4^{-2}/m$ changes in time: on the history it falls like $e^{-(5/3)AHx_4}$, so every condensate with $\lambda \neq 0$ drifts towards $x = 0$ and $w = 0$ as the 7-volume grows. The table gives the value of $w$ at the moment at which $x$ has the value of its first column. Its special values, each by elementary algebra:

| $x = \lambda S/m$ | $w$ | why |
| --- | --- | --- |
| $x = 0$ ($\lambda = 0$) | $w = 0$ (like dust) | $p = 0$ |
| $x = 1$ | $w = 1/3$ (like radiation) | $1/(2 + 1)$ |
| $x = -1$ | $w = -1$ (like a cosmological constant) | $-1/(2 - 1)$; here $V = m(1 + x) = 0$ |
| $-2 < x < -1$ | $w < -1$ (called **phantom**) | $2 + x > 0$, and $x < -(2 + x)$ means $x < -1$ |
| $x = -2$ | not defined | $\rho = mS(1 + x/2) = 0$ |
| $x < -2$ (with $m > 0$, $S > 0$) | $w > 1$ | $\rho < 0$ and $p < 0$; $x/(2 + x) > 1$ means $x < 2 + x$ after multiplying by the negative $2 + x$ |
| $x \to \pm\infty$ | $w \to 1$ | $x/(2 + x) = 1/(1 + 2/x)$ |

**What these numbers are, and what they are not.** They are the ratios $p/\rho$ of the eight-dimensional tensor of exact solutions, at one moment (COMPUTED in Notebook 09b on twelve condensates at $x_4 = 1.3$; the formula is PROVED in the record). They are not the equation of state that an observer in 3-space would infer: that observer sees neither the extra times nor the hidden direction as space, and to relate the two one must integrate over $x_5, x_6, x_7, x_0$ and follow the deflation. This chapter makes no such computation. The Revision dark-sector record makes it, for the corrected metric, under an ASSUMED normalisation of the observer's energy density (the definitions A, B and C of Chapter 22): on the record's history $b_4 = b_4(0)\,e^{(4/3)Hx_4}$ a homogeneous condensate of either field is diluted ($e^{-a_4}b_4^2S$ is constant), and the equation of state $w_{\rm eff}$ that the observer infers is $\frac59\,w$ under A and B and $\frac59\,w - \frac49$ under C, where $w = p/\rho$ is the ratio of this table, which drifts in time as $\lambda S/m$ falls like $e^{-(5/3)a_4}$ (PROVED in that record: `Revision/dark_sector/dirac16complex/reports/derivation-checks.json`, check `condensate_w_eff`, and `Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json`, check `condensate_observer`; `Revision/docs/DARK_SECTOR_HYPOTHESES.md`, sections 5.1 and 6.1). The same record proves that no condensate can be the source that the record's history requires: every condensate has $p_3 = p_t = p_0$ and an $S$ that decays like $e^{-(5/3)a_4}$, while the required source of Section 9.11 has $p_3 \neq p_0$ and grows (`Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json`, check `condensate_cannot_source_history`). Which definition, if any, describes a physical observer, and a fit to supernova data, are OPEN. In particular, the phantom range $w < -1$ of this table is not a claim about dark energy: the commuting field has negative energies (Section 9.21), and any use of them for a phantom equation of state is a HYPOTHESIS, not a result (the record finds the observer's reading $w_{\rm eff}$ under C below $-1$ exactly while $\lambda S/m$ lies between $-2$ and $-1$, check `condensate_phantom_interval` of the same report, for a value of $\lambda S/m$ that is chosen, not derived; Chapter 22).

### 9.20 Where condensates oscillate and where they grow

With $V = m(1 + x)$ the number $k^2 = c_g^2 - V^2 = c_g^2 - m^2(1 + x)^2$ is positive exactly when $|1 + x| < c_g/|m|$. In the plane of the two pure numbers $x$ and $c_g/|m|$ the condensates that grow at a given moment fill the wedge between the lines $c_g/|m| = |1 + x|$; outside it they oscillate at that moment. The equation of state depends on $x$ alone, so every line of constant $w$ is vertical in this plane. At $x = -1$ ($w = -1$) the effective mass vanishes and $k^2 = c_g^2 > 0$: every condensate with $w = -1$ lies in the growing wedge at that moment. Along the history a condensate does not stay at one point of the map: it moves in two ways at once. Its $x$ falls like $e^{-(5/3)AHx_4}$, so the point moves horizontally towards $x = 0$; and $c_g/|m|$ grows like $e^{AHx_4/3}$, so the point moves upwards, because the block deflates. Since $|1 + x|$ approaches 1 while $c_g/|m|$ grows without bound, **every condensate enters the growing wedge and grows at late times**. This is the record's statement for the good-sector waves that do not depend on $x_0$, whose matrix is the same (PROVED; `Revision/theory/reports/python-scope.json` and `wolfram-scope.json`, check `good_sector_x0_independent_modes_without_boundary_condition`: imaginary frequencies wherever $m^2 < c_g^2$, and $c_g$ grows on the history).

The two condensates of Notebook 09b have $m = 1$, $H = 0.25$ and $S_0 = 1$, on the history with $A = 1$ and $\beta = \frac43$, where $e^{a_4}b_4^{-2} = e^{-5x_4/12}$, $V = 1 + \lambda e^{-5x_4/12}$ and $c_g = \frac32\cdot 0.25\,e^{x_4/12} = 0.375\,e^{x_4/12}$, which grows from $0.375$ at $x_4 = 0$ to $1.4226$ at $x_4 = 16$:

- $\lambda = 0.5$ ("oscillating first"): $V$ falls from $1.5$ at $x_4 = 0$ to $1.0006$ at $x_4 = 16$. At $x_4 = 0$, $k^2 = 0.140625 - 2.25 = -2.109375$, so the column oscillates with $\omega = \sqrt{2.109375} = 1.4524$ (period $2\pi/\omega = 4.33$). The rising $c_g$ passes the falling $V$ at $x_4 = 11.8136$ (found by bisection), and after that moment the condensate grows (COMPUTED; Figure 09b.2, left).
- $\lambda = -0.8$ ("growing first"): $V$ rises from $0.2$, below $c_g = 0.375$, where $k^2 = 0.140625 - 0.04 = 0.100625$ and $k = 0.3172$, so it grows at first; $V$ passes $c_g$ at $x_4 = 0.6776$, and the condensate oscillates; $c_g$ catches up with $V$ again at $x_4 = 11.6963$, and it grows again (COMPUTED; Figure 09b.2, right).

In both cases $e^{-a_4}b_4^2S = \chi^\dagger C\chi$ stays exactly at 1, while $S$ itself falls like $e^{-5x_4/12}$. A growing $\chi$ with a constant $\chi^\dagger C\chi$ is possible because $C$ has eight eigenvalues $+1$ and eight $-1$: the growth happens along directions in which the indefinite form $\chi^\dagger C\chi$ does not grow. Whether growing condensates are acceptable physically is the question of well-posedness and boundary conditions discussed in Chapter 8; this chapter only computes their tensor.

### 9.21 The energy of the commuting field has no lower bound

**$S$ has no sign.** $C$ is real and symmetric with $C^2 = 1$, so its eigenvalues are $+1$ or $-1$; the record writes $C = \mathrm{diag}(-\sigma, \sigma)$ (the block $-\sigma$ in the upper left corner, $\sigma$ in the lower right, zeros elsewhere) with a real symmetric $8 \times 8$ matrix $\sigma$ that obeys $\sigma^2 = 1$ and has trace 0. The eigenvalues of $\sigma$ are therefore $+1$ or $-1$ (if $\sigma v = \mu v$ then $v = \sigma^2v = \mu^2v$, so $\mu^2 = 1$), and because the trace of a symmetric matrix is the sum of its eigenvalues, trace 0 means four eigenvalues $+1$ and four $-1$. The block $-\sigma$ has the same eigenvalues with the signs exchanged, again four of each. So $C$ has eight eigenvalues $+1$ and eight $-1$ (PROVED; see the table at the end of this section). For an eigenvector $\chi$ with eigenvalue $-1$, $S_0 = \chi^\dagger C\chi = -\chi^\dagger\chi < 0$. A condensate with $\lambda = 0$ has $\rho = mS_0$: for $m > 0$ its energy density is negative whenever $S_0 < 0$.

**Plane waves of positive frequency with negative energy.** Take flat 4+4 space (all $f_a = 1$, no spin connection), $U = 0$, and a **plane wave** $\Phi = u\,e^{i(k_1x_1 + k_2x_2 + k_3x_3 + k_0x_0 - Ex_4)}$ with a constant column $u$, no dependence on the extra times, and a positive frequency $E$. Then $\partial_a\Phi = ik_a\Phi$ for $a = 0, 1, 2, 3$, $\partial_4\Phi = -iE\Phi$, and $\partial_a\bar\Phi = -ik_a\bar\Phi$ (complex conjugation turns $i$ into $-i$). Line by line:

$$
\begin{aligned}
K_a &= \tfrac12\big(\bar\Phi\gamma^{(a)}(ik_a\Phi) - (-ik_a\bar\Phi)\gamma^{(a)}\Phi\big) = ik_a\,\bar\Phi\gamma^{(a)}\Phi \qquad (a = 0, 1, 2, 3), \\
\rho &= -\sum_{a \neq x_4}K_a + mS = \bar\Phi\Big(m - i\sum_a k_a\gamma^{(a)}\Big)\Phi, \\
mu &= -iE\gamma^{(4)}u + i\sum_a k_a\gamma^{(a)}u \quad\Longrightarrow\quad \Big(m - i\sum_a k_a\gamma^{(a)}\Big)\Phi = -iE\gamma^{(4)}\Phi, \\
\rho &= \bar\Phi\big(-iE\gamma^{(4)}\big)\Phi = E\,\Phi^\dagger\big(-iC\gamma^{(4)}\big)\Phi = E\,\Phi^\dagger B\Phi = E\,u^\dagger Bu .
\end{aligned}
$$

The first line inserts the derivatives into $K_a$ (the two terms are equal); the second inserts $K_a$ into $\rho$ (Section 9.7, with $U = 0$; the extra-time terms are zero); the third is the flat field equation $\sum_a\gamma^{(a)}\partial_a\Phi = m\Phi$ for the plane wave, rearranged; the fourth inserts it, writes $\bar\Phi = \Phi^\dagger C$, uses the matrix $B = -iC\gamma^{(4)}$ of Chapter 5, and the fact that the exponential factor has size 1. $B$ is Hermitian with $B^2 = 1$, with eight eigenvalues $+1$ and eight $-1$. The field equation multiplied by $-i\gamma^{(4)}$ reads $Eu = hu$ with the matrix $h = m\beta + \sum_a k_a\alpha^a$, $\beta = -i\gamma^{(4)}$, $\alpha^a = -\gamma^{(4)}\gamma^{(a)}$; for $m = 2$ and $(k_0, k_1, k_2, k_3) = (4, 1, 2, 0)$, $h^2 = (4 + 16 + 1 + 4 + 0)\cdot 1 = 25$, so $E = \pm 5$. The record proves that $h$ commutes with $B$ and that on the 8-dimensional space of solutions with $E = 5$ the form $u^\dagger Bu$ has four positive and four negative directions (**Krein inertia** (4,4)): there are unit columns $u$ with $Bu = -u$, whose waves have $\rho = -5$, and with $Bu = +u$, whose waves have $\rho = +5$ (PROVED; the table lists the checks). Multiplying such a wave by a large constant makes $\rho$ as negative as we like: the classical energy of dirac16complex00 has no lower bound, already for $U = 0$.

| statement | Revision report | check |
| --- | --- | --- |
| $h$ commutes with $B$; waves with $\rho = -5$ and $\rho = +5$ at $E = 5$ | `Revision/theory/reports/python-scope.json` and `wolfram-scope.json` | `commuting_field_energy_unbounded_below` |
| every space of solutions of one real frequency has Krein inertia (4,4) | `Revision/pairing/reports/python-pairing.json` | `Q.one_particle_Krein_inertia_proof` |
| $C$ has eight eigenvalues $+1$ and eight $-1$ | `Revision/algebra/reports/python-algebra.json` and `wolfram-algebra.json` | `C_equals_notebook_sigma16`, `sigma8_involution` |

This is the classical form of the **spin-statistics** problem of a commuting field with a first-order Lagrangian. The **spin-statistics rule** of ordinary four-dimensional quantum field theory says that particles of half-integer **spin** (the spin is the intrinsic angular momentum of a particle, measured in units of Planck's constant divided by $2\pi$; the electron has spin $\frac12$), which are the fermions of Chapter 7, must be described by anticommuting fields; described by commuting fields, as dirac16complex00 is, the energy of a spinor field has no lower bound, and this is exactly what the plane waves above show. (The rule is a theorem of ordinary four-dimensional physics; this book does not prove it, and for 4+4 dimensions it claims only the statements of this section.) It must be remembered in every reading of the author's Hypothesis00 (for example a phantom equation of state), and it is why the anticommuting, quantised field dirac16complex is treated separately (Chapter 10). In Part V the chirality map $\Gamma$ sends every solution with parameters $(m, \lambda)$ to a solution with $(-m, -\lambda)$ and reverses the sign of the energy-momentum tensor (theorem T1; PROVED, `Revision/pairing/reports/python-pairing.json`, checks `T1.metric.commuting.euler_lagrange_map` and `T1.metric.commuting.emt`; Chapter 18 gives the proof). That theorem is an exact map between sets of solutions: it does not prove that any universe is created, in pairs or otherwise, and it gives no creation process, rate or amplitude.

### 9.22 Example: condensates

The second worked example builds the condensates of Section 9.18 on the history $a_4 = AHx_4$, $b_4 = e^{\beta AHx_4}$ ($A = 1$, $\beta = \frac43$, in the unit $b_4(0)$) and measures their energy-momentum tensor. It first shows with 20000 random columns that $S_0 = \chi^\dagger C\chi$ takes both signs; checks $M^2 = k^2$ and $M^TC + CM = 0$ for 24 pairs $(V, c_g)$; solves $\chi' = M(x_4)\chi$ with the Runge-Kutta method for the condensates with $\lambda = 0.5$ ("oscillating first") and $\lambda = -0.8$ ("growing first"), with $m = 1$, $H = 0.25$ and $S_0 = 1$, from $x_4 = 0$ to 16, finds the moments at which $k^2$ changes sign, and checks the field equation with the terms $c_g\gamma^{(0)}$ and $v_g\gamma^{(4)}$ and the dilution $S = e^{a_4}b_4^{-2}S_0$ at 1601 times; computes from the solutions $K_4$, $\rho$, $p$ and $B_{04}$ and checks the values of Section 9.19; measures $w = p/\rho$ on twelve condensates at $x_4 = 1.3$ and compares it with $x/(2 + x)$; draws the map of Section 9.20 with the paths of the two condensates; confirms that a condensate is only diluted, $d\rho/dx_4 = -(3a_4' + 4h_4)(\rho + p)$, and, as an ILLUSTRATION only, solves the work and dilution of toy fluids with the Runge-Kutta method; and reproduces the negative energies of Section 9.21. It draws seven figures.

<!-- NOTEBOOK 09b -->

### 9.25 Line-by-line walk-through of Notebook 09b

The notebook has 20 code cells, In [1] to In [20]. As in Section 9.17, long figure captions are shortened to a line "...)"; the captions are printed in full in Section 9.24, under their figures. Every other line of every code cell is quoted, in order.

**In [1], the set-up cell.** It is word for word the set-up cell of Notebook 09a, explained line by line in Section 9.17, with two differences: its comment lines are the run instructions of Notebook 09b (Section 9.23), and its line `NOTEBOOK_ID = "09b"` names this notebook, so the figures are saved as `09b_<k>_<name>.png` and their captions in `09b.captions.json`. It prints `Set-up of notebook 09b complete: repository folder found, helpers defined.`

**In [2], the matrices C and B, and the sign of S.**

```python
import numpy as np  # arrays of numbers, matrices, linear algebra

fixture = json.loads(
    repository_file("Revision/algebra/gammas.json").read_text(encoding="utf-8"))
gamma = [np.array(rows, dtype=float) for rows in fixture["gamma"]]  # x0, ..., x7
C = np.array(fixture["C"], dtype=float)  # gamma^(x0) gamma^(x1) gamma^(x2) gamma^(x3)
B = (np.array(fixture["B"]["re"], dtype=float)  # B = -i C gamma^(x4), stored as its
     + 1j * np.array(fixture["B"]["im"], dtype=float))  # real and imaginary parts
I16 = np.eye(16)  # the 16 x 16 unit matrix
g4, g0 = gamma[4], gamma[0]  # gamma^(x4) and gamma^(x0)
```

The fixture is read as in Notebook 09a. Besides the gammas and $C$ the cell takes the matrix $B = -iC\gamma^{(4)}$ of Chapter 5, which the fixture stores as two real arrays, its real part `"re"` and its imaginary part `"im"`; `1j` is $i$, so `B` is the complex matrix. `g4` and `g0` are short names for $\gamma^{(4)}$ and $\gamma^{(0)}$, the two gammas of the condensate equation.

```python
def recorded(path, name):
    """The verdict (PASS or FAIL) of the check name in the Revision report path."""
    report_data = json.loads(repository_file(path).read_text(encoding="utf-8"))
    for item in report_data["checks"]:
        if item["name"] == name:
            return item["verdict"].upper()  # some reports write "pass"
    raise KeyError(f"{path} has no check {name}")
```

The helper `recorded(path, name)` returns the verdict of a check of a Revision report, exactly as in Notebook 09a (Section 9.17, In [2]).

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

`np.linalg.eigvalsh` returns the eigenvalues of a symmetric matrix in ascending order. The check asks for eight eigenvalues $-1$ followed by eight $+1$ (to $10^{-12}$), together with the record's verdicts: $C = \mathrm{diag}(-\sigma, \sigma)$ (`C_equals_notebook_sigma16`) with $\sigma^2 = 1$ and trace 0 (`sigma8_involution`), the facts of Section 9.21.

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

A generator with the fixed seed 2026 draws 20000 random complex columns of length 16 (an array of 20000 rows); `np.linalg.norm(chis, axis=1)` computes the length of each row and `/=` divides each row by its length, so every column has length 1. `np.einsum("ni,ij,nj->n", ...)` computes $S_0 = \chi^\dagger C\chi$ for all rows at once: the letters name the indices, and the indices that do not appear after `->` are summed over (here $i$ and $j$), once for each row $n$. `np.mean(S0_values < 0)` is the fraction of the rows with $S_0 < 0$ (`True` counts as 1). The check: $S_0$ takes both signs and lies between $-1$ and $1$ (because the eigenvalues of $C$ are $\pm1$ and each column has length 1). It prints `RESULT fraction of the 20000 random chi with S0 < 0 = 0.4983`.

**In [3], the histogram of S0.**

```python
fig, ax = plt.subplots()
ax.hist(S0_values, bins=60, range=(-1.0, 1.0), color="tab:blue", edgecolor="white")
ax.axvline(0.0, color="black", linewidth=1.0)
ax.set_xlabel("$S_0 = \\chi^\\dagger C \\chi$ for a random $\\chi$ of length 1")
ax.set_ylabel("number of the 20000 random $\\chi$")
ax.set_title("The scalar $S = \\bar\\Phi\\Phi$ has no sign")
```

`ax.hist` counts the 20000 values in 60 equal intervals between $-1$ and $1$ and draws one bar per interval; a black vertical line marks zero.

```python
save_figure(fig, "sign_of_s",
            "Histogram of $S_0 = \\chi^\\dagger C\\chi$ for 20000 random complex "
...)
```

The figure is saved as Figure 09b.1 (`09b_1_sign_of_s.png`). The student sees bars spread symmetrically about zero: about half of the random condensates with $\lambda = 0$ have a negative energy density $\rho = mS_0e^{a_4}b_4^{-2}$.

**In [4], the matrix M and its square.**

```python
def condensate_matrix(V, c):
    """M = -V gamma^(x4) + c gamma^(x4) gamma^(x0) and k^2 = c^2 - V^2."""
    return -V * g4 + c * g4 @ g0, c ** 2 - V ** 2
```

`condensate_matrix(V, c)` returns the matrix $M = -V\gamma^{(4)} + c\,\gamma^{(4)}\gamma^{(0)}$ of Section 9.18 and the number $k^2 = c^2 - V^2$; a function may return two values at once, separated by a comma.

```python
THEORY_WL = "Revision/theory/reports/wolfram-field-theory.json"
THEORY_PY = "Revision/theory/reports/python-field-theory.json"
A4_WL = "Revision/field_equations_a4/reports/wolfram-a4-report.json"
worst_square, worst_c = 0.0, 0.0  # the largest deviations found
for V_test in (-2.0, -0.5, 0.0, 0.75, 1.5, 3.0):
    for c_test in (0.1, 0.375, 1.0, 2.5):
        M_test, k2_test = condensate_matrix(V_test, c_test)
        worst_square = max(worst_square, np.abs(M_test @ M_test - k2_test * I16).max())
        worst_c = max(worst_c, np.abs(M_test.T @ C + C @ M_test).max())
```

The names of three reports, and two numbers that hold the largest deviations found. For 6 values of $V$ and 4 values of $c$ (24 pairs, with negative, zero and positive $V$) the cell computes the largest entry of $M^2 - k^2\cdot 1$ and of $M^TC + CM$.

```python
check(worst_square < 1e-12 and worst_c < 1e-12
      and recorded(THEORY_WL, "solution_matrix_square") == "PASS"
      and recorded(A4_WL, "condensate_equation_x0_consistent") == "PASS",
      "M^2 = (c^2 - V^2) times 1 and M^T C + C M = 0 for 24 pairs (V, c)",
      record=f"{THEORY_WL}, check solution_matrix_square; {A4_WL}, check "
             "condensate_equation_x0_consistent")
```

Both must be below $10^{-12}$; the record's verdicts `solution_matrix_square` and `condensate_equation_x0_consistent` complete the check. One PASS line.

**In [5], the history and the function that solves the condensate equation.**

```python
m, H = 1.0, 0.25  # the mass and the author's constant
A, beta = 1.0, 4 / 3  # the history a4 = A H x4, b4 = b4(0) e^(beta A H x4)
a4p, u = A * H, beta * A * H  # a4' = 1/4 and b4'/b4 = 1/3 on the history
h4 = u / 2 - a4p  # the rate of the block: -1/12 (it deflates)
v_g = u - a4p / 2  # the coefficient of gamma^(x4) in the field equation: 5/24
```

The parameters: $m = 1$, $H = 0.25$, the history constants $A = 1$ and $\beta = \frac43$; on the history $a_4' = AH = 0.25$, $u = b_4'/b_4 = \beta AH = \frac13$, the rate of the block $h_4 = \frac{u}{2} - a_4' = -\frac{1}{12}$ and the coefficient $v_g = u - \frac{a_4'}{2} = \frac{5}{24}$ (all constants on this history).

```python
rng = np.random.default_rng(7)
while True:  # draw until S0 > 0 (the first draw usually succeeds)
    chi = rng.normal(size=16) + 1j * rng.normal(size=16)
    S0 = (chi.conj() @ C @ chi).real
    if S0 > 0:
        break
chi = chi / np.sqrt(S0)  # now chi^dagger C chi = 1
```

A generator with the seed 7 draws random columns until one has $S_0 = \chi^\dagger C\chi > 0$ (`while True:` repeats until `break` leaves the loop; the first draw usually succeeds). Dividing the column by $\sqrt{S_0}$ makes $\chi^\dagger C\chi = 1$ (both $\chi^\dagger$ and $\chi$ are divided by $\sqrt{S_0}$).

```python
def a4_of(x4):
    """a4 = A H x4 on the history."""
    return A * H * x4
```

`a4_of(x4)` returns $a_4 = AHx_4$.

```python
def b4_of(x4):
    """b4 = e^(beta A H x4) on the history, in the unit b4(0)."""
    return np.exp(beta * A * H * x4)
```

`b4_of(x4)` returns $b_4 = e^{\beta AHx_4}$ in the unit $b_4(0)$.

```python
def F_of(x4):
    """The factor F = e^(a4/2) b4^(-1) of Phi = F chi."""
    return np.exp(a4_of(x4) / 2) / b4_of(x4)
```

`F_of(x4)` returns the factor $F = e^{a_4/2}b_4^{-1}$ of $\Phi = F\chi$.

```python
def dilution(x4):
    """e^(a4) b4^(-2) = F^2, so that S = S0 e^(a4) b4^(-2)."""
    return np.exp(a4_of(x4)) / b4_of(x4) ** 2
```

`dilution(x4)` returns $e^{a_4}b_4^{-2} = F^2$, so that $S = S_0\cdot$ `dilution`; on this history it is $e^{-5x_4/12}$.

```python
def c_g_of(x4):
    """The gravitational coefficient c_g = (3/2) H e^(a4) b4^(-1/2)."""
    return 1.5 * H * np.exp(a4_of(x4)) / np.sqrt(b4_of(x4))
```

`c_g_of(x4)` returns the gravitational coefficient $c_g = \frac32He^{a_4}b_4^{-1/2}$, on this history $0.375\,e^{x_4/12}$.

```python
def condensate(chi0, lam, x4_end, steps):
    """RK4 for chi' = M(x4) chi with V = m + lam S0 e^a4 b4^-2 and c = c_g(x4);
    returns the times, Phi = F chi, dPhi/dx4 = F (M chi - v_g chi) and chi."""
    S0_value = (chi0.conj() @ C @ chi0).real  # constant along the solution
    step = x4_end / steps

    def rate(x4, column):  # M(x4) chi
        V = m + lam * S0_value * dilution(x4)
        return condensate_matrix(V, c_g_of(x4))[0] @ column
```

`condensate(chi0, lam, x4_end, steps)` solves $\chi' = M(x_4)\chi$ from $x_4 = 0$ to `x4_end` with `steps` equal steps. `S0_value` is $S_0 = \chi_0^\dagger C\chi_0$, constant along the solution (Section 9.18), and `step` the length of one step. The inner function `rate(x4, column)` returns $M(x_4)\chi$, with the effective mass $V = m + \lambda S_0e^{a_4}b_4^{-2}$ and $c = c_g(x_4)$; `[0]` takes the first of the two values that `condensate_matrix` returns, the matrix.

```python
    times_out, columns = [0.0], [chi0.astype(complex)]
    column = columns[0]
    for n in range(steps):
        x4 = n * step
        s1 = rate(x4, column)
        s2 = rate(x4 + step / 2, column + step / 2 * s1)
        s3 = rate(x4 + step / 2, column + step / 2 * s2)
        s4 = rate(x4 + step, column + step * s3)
        column = column + step / 6 * (s1 + 2 * s2 + 2 * s3 + s4)
        times_out.append((n + 1) * step)
        columns.append(column)
```

The Runge-Kutta method of fourth order (RK4, Chapter 2): from the column at the time $x_4$ it computes four slopes, $s_1$ at the start of the step, $s_2$ and $s_3$ in its middle (each using the previous slope to step half-way), $s_4$ at its end, and moves on by the weighted average $\frac{h}{6}(s_1 + 2s_2 + 2s_3 + s_4)$ with the step $h$. The times and the columns are collected in two lists; `chi0.astype(complex)` makes sure the columns are complex.

```python
    times_out, columns = np.array(times_out), np.array(columns)
    factor = F_of(times_out)  # F at every time
    derivatives = np.array([rate(t, c) - v_g * c for t, c in zip(times_out, columns)])
    return (times_out, factor[:, None] * columns, factor[:, None] * derivatives,
            columns)
```

The lists become arrays. The field and its derivative follow from $\Phi = F\chi$ and $\partial_4\Phi = F(M\chi - v_g\chi)$ (Section 9.18: $F' = -v_gF$); `factor[:, None]` multiplies row by row. The function returns the times, $\Phi$, $\partial_4\Phi$ and $\chi$.

```python
S0_now = (chi.conj() @ C @ chi).real  # 1 up to rounding
report("S0 = chi^dagger C chi after the division", f"{S0_now:.6f}")
```

The cell prints `RESULT S0 = chi^dagger C chi after the division = 1.000000`.

**In [6], two condensates and the moments at which they change their behaviour.**

```python
EXAMPLES = {"oscillating first": 0.5, "growing first": -0.8}  # name -> lambda
```

The two examples: their names and their values of $\lambda$.

```python
def k_squared(x4, lam):
    """k^2 = c_g^2 - V^2 at the time x4 for a condensate with S0 = 1."""
    return c_g_of(x4) ** 2 - (m + lam * dilution(x4)) ** 2
```

`k_squared(x4, lam)` returns $k^2 = c_g^2 - V^2$ at the time $x_4$ for $S_0 = 1$.

```python
def sign_change(lam, low, high):
    """The time between low and high at which k^2 changes sign (bisection)."""
    for _ in range(60):
        middle = (low + high) / 2
        if np.sign(k_squared(middle, lam)) == np.sign(k_squared(low, lam)):
            low = middle  # the sign change lies in the upper half
        else:
            high = middle  # the sign change lies in the lower half
    return (low + high) / 2
```

`sign_change(lam, low, high)` finds the time between `low` and `high` at which $k^2$ changes sign, by **bisection**: it halves the interval 60 times, each time keeping the half in which the sign changes (if $k^2$ has the same sign at the middle as at the lower end, the change lies in the upper half). After 60 halvings the interval is $2^{-60}$ times its first length, far below the rounding of the numbers.

```python
CHANGES = {"oscillating first": [sign_change(0.5, 5.0, 16.0)],
           "growing first": [sign_change(-0.8, 0.0, 3.0),
                             sign_change(-0.8, 5.0, 16.0)]}
```

The moments: one for $\lambda = 0.5$, searched between $x_4 = 5$ and 16, and two for $\lambda = -0.8$, between 0 and 3 and between 5 and 16.

```python
solutions = {}  # name -> (times, Phi, dPhi/dx4, chi)
for name, lam in EXAMPLES.items():
    times, phis, dphis, columns = condensate(chi, lam, 16.0, 1600)
    S_values = np.einsum("ti,ij,tj->t", phis.conj(), C, phis).real
    S_expected = dilution(times)  # S0 e^(a4) b4^(-2) with S0 = 1
    worst_residual = 0.0
```

For each example the condensate is solved from $x_4 = 0$ to 16 with 1600 steps (step 0.01); $S = \bar\Phi\Phi$ is computed at every step with `np.einsum` and compared below with $S_0e^{a_4}b_4^{-2}$.

```python
    for x4, phi, dphi, S_now in zip(times, phis, dphis, S_values):
        residual = (g4 @ dphi + c_g_of(x4) * g0 @ phi + v_g * g4 @ phi
                    - (m + lam * S_now) * phi)
        worst_residual = max(worst_residual,
                             np.abs(residual).max() / np.abs(phi).max())
    solutions[name] = (times, phis, dphis, columns)
```

At each of the 1601 times the residual of the field equation $\gamma^{(4)}\partial_4\Phi + c_g\gamma^{(0)}\Phi + v_g\gamma^{(4)}\Phi - (m + \lambda S)\Phi$ is computed, with the $S$ of the solution itself, and its largest entry divided by the largest entry of $\Phi$ updates `worst_residual`. The solution is stored.

```python
    report(f"{name}: lambda = {lam}, V = m + lambda S at x4 = 0 and 16",
           f"{m + lam:.4f} and {m + lam * S_expected[-1]:.4f}")
    report(f"{name}: k^2 changes sign at x4",
           ", ".join(f"{t:.4f}" for t in CHANGES[name]))
    check(worst_residual < 1e-9,
          f"{name}: the field equation holds at 1601 times")
    check(np.abs(S_values / S_expected - 1).max() < 1e-9,
          f"{name}: S = e^a4 b4^-2 S0 at 1601 times (e^-a4 b4^2 S stays 1)")
```

Two RESULT lines and two checks per example. The printed RESULT lines are

```text
RESULT oscillating first: lambda = 0.5, V = m + lambda S at x4 = 0 and 16 = 1.5000 and
    1.0006
RESULT oscillating first: k^2 changes sign at x4 = 11.8136
RESULT growing first: lambda = -0.8, V = m + lambda S at x4 = 0 and 16 = 0.2000 and
    0.9990
RESULT growing first: k^2 changes sign at x4 = 0.6776, 11.6963
```

(the long lines are wrapped). The checks: the field equation holds to $10^{-9}$ (relative) at all 1601 times, and $S = e^{a_4}b_4^{-2}S_0$ to $10^{-9}$ (relative), that is $e^{-a_4}b_4^2S$ stays 1.

```python
    coarse = condensate(chi, lam, 16.0, 800)[1][-1]  # twice the step
    rk4_change = np.abs(coarse - phis[-1]).max() / np.abs(phis[-1]).max()
    report(f"{name}: change of Phi(16) when the RK4 step is halved",
           f"{rk4_change:.1e}")
    check(rk4_change < 1e-7,
          f"{name}: halving the RK4 step changes Phi(16) by less than 1e-7")
```

The accuracy of RK4: the condensate is solved again with 800 steps (twice the step), and the relative change of $\Phi(16)$ is printed, `2.5e-08` and `1.9e-09`; it must be below $10^{-7}$. RK4 has an error proportional to the fourth power of the step, so halving the step divides the error by about 16, and the error of the finer solution is about a fifteenth of this change.

```python
report("c_g at x4 = 0 and 16", f"{c_g_of(0.0):.4f} and {c_g_of(16.0):.4f}")
check(recorded(THEORY_WL, "exact_solution_nonlinear_homogeneous_C") == "PASS"
      and recorded(THEORY_PY, "exact_nonlinear_homogeneous_solution") == "PASS",
      "both condensates are the record's homogeneous solutions",
      record=f"{THEORY_WL}, check exact_solution_nonlinear_homogeneous_C; "
             f"{THEORY_PY}, check exact_nonlinear_homogeneous_solution")
```

The cell prints `c_g at x4 = 0 and 16 = 0.3750 and 1.4226` and checks the record's verdicts for the exact homogeneous solutions (`exact_solution_nonlinear_homogeneous_C`, `exact_nonlinear_homogeneous_solution`): every solution of the linear system is a solution of the field equation, so both condensates are exact solutions, computed here to the accuracy of RK4.

**In [7], the figure of the two condensates.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(9.6, 3.9))
times, phis, _, _ = solutions["oscillating first"]
S_values = np.einsum("ti,ij,tj->t", phis.conj(), C, phis).real
```

Two panels; the left one shows the condensate with $\lambda = 0.5$. `_` is the usual Python name for a value that is not needed.

```python
for component in (0, 5, 10):  # three of the 16 components (rows 1, 6 and 11)
    left.plot(times, phis[:, component].real,
              label=f"Re $\\Phi_{{{component + 1}}}$")
left.plot(times, S_values, "k--", label="$S = \\bar\\Phi\\Phi$")
left.axvline(CHANGES["oscillating first"][0], color="black", linestyle=":",
             linewidth=0.9)
left.set_xlabel("time $x_4$")
left.set_ylabel("value")
left.set_ylim(-0.8, 1.35)  # room for the legend above the curves
left.set_title("Oscillating first: $\\lambda = 0.5$")
left.legend(fontsize=7, loc="upper center", ncol=4)
```

The real parts of the components 1, 6 and 11 of $\Phi$ (Python counts from 0, hence `component + 1` in the label; the triple braces of the f-string produce one brace around the number in the label), $S$ as a dashed black curve, and a dotted vertical line at the moment $x_4 = 11.8136$ at which $k^2$ changes sign. The vertical range leaves room for the legend in four columns.

```python
times, phis, _, columns = solutions["growing first"]
right.plot(times, np.einsum("ti,ti->t", columns.conj(), columns).real,
           label="$\\chi^\\dagger\\chi = F^{-2}\\Phi^\\dagger\\Phi$")
right.plot(times, np.einsum("ti,ti->t", phis.conj(), phis).real, "--",
           label="$\\Phi^\\dagger\\Phi$")
for moment in CHANGES["growing first"]:
    right.axvline(moment, color="black", linestyle=":", linewidth=0.9)
right.set_yscale("log")
right.set_xlabel("time $x_4$")
right.set_title("Growing first: $\\lambda = -0.8$")
right.legend(fontsize=8)
```

The right panel shows the condensate with $\lambda = -0.8$: the size $\chi^\dagger\chi$ of the column and the size $\Phi^\dagger\Phi = F^2\chi^\dagger\chi$ of the field (dashed), on a logarithmic axis, with dotted lines at the two moments at which $k^2$ changes sign.

```python
save_figure(fig, "condensate_solutions",
            "Two condensates $\\Phi = e^{a_4/2}b_4^{-1}\\chi$ of dirac16complex00 with "
...)
```

The figure is saved as Figure 09b.2 (`09b_2_condensate_solutions.png`). Left, the student sees oscillations whose size shrinks with the factor $F = e^{-5x_4/24}$ and whose period grows as $c_g$ approaches $V$; after the dotted line the components grow. Right, $\chi^\dagger\chi$ rises slightly until $x_4 = 0.68$ (the growth rate $k$ is small there), oscillates until $x_4 = 11.70$ and then grows strongly, to about 3000 at $x_4 = 16$; $\Phi^\dagger\Phi$ is $\chi^\dagger\chi$ times $e^{-5x_4/12}$, so on the logarithmic axis it is the same curve tilted downwards by a straight line: the field itself first shrinks with the dilution and grows only near the end.

**In [8], the energy density and the pressures of the condensates.**

```python
def homogeneous_tensor(phi, dphi, lam):
    """S, U, K4, rho, p and B04 of a condensate at one time."""
    S = (phi.conj() @ C @ phi).real
    U = lam / 2 * S ** 2
    K4 = 0.5 * (phi.conj() @ C @ g4 @ dphi - dphi.conj() @ C @ g4 @ phi)
    L0 = K4.real - m * S - U  # the other seven kinetic terms are zero
    B04 = phi.conj() @ C @ g0 @ dphi - dphi.conj() @ C @ g0 @ phi
    return S, U, K4, K4.real - L0, L0, B04  # rho = K4 - L0, p = L0
```

`homogeneous_tensor(phi, dphi, lam)` computes, at one time, $S$, $U$, $K_4 = \frac12(\bar\Phi\gamma^{(4)}\Phi' - \bar\Phi'\gamma^{(4)}\Phi)$ (here $\bar\Phi\gamma^{(4)}\Phi'$ is written `phi.conj() @ C @ g4 @ dphi`, because $\bar\Phi = \Phi^\dagger C$), the Lagrangian $L_0 = K_4 - mS - U$ (the other seven kinetic terms are zero), and $B_{04} = \bar\Phi\gamma^{(0)}\Phi' - \bar\Phi'\gamma^{(0)}\Phi$. It returns them together with $\rho = K_4 - L_0$ (because $\rho = -T^{x_4}{}_{x_4} = -(L_0 - K_4)$) and $p = L_0$ (because $p_\mu = L_0 - K_\mu = L_0$ for $\mu \neq x_4$).

```python
for name, lam in EXAMPLES.items():
    times, phis, dphis, _ = solutions[name]
    S_expected = dilution(times)
    rhos, ps, worst = [], [], 0.0
    for phi, dphi in zip(phis, dphis):
        S, U, K4, rho, p, B04 = homogeneous_tensor(phi, dphi, lam)
        size = (phi.conj() @ phi).real  # for relative tolerances
        worst = max(worst, abs(K4.imag) / size,
                    abs(K4.real - (m + lam * S) * S) / size, abs(B04) / size)
        rhos.append(rho)
        ps.append(p)
    rhos, ps = np.array(rhos), np.array(ps)
```

For each condensate and each of the 1601 times the cell computes these quantities and records the worst of three relative deviations: the imaginary part of $K_4$, the difference $K_4 - VS$, and $B_{04}$, each divided by $\Phi^\dagger\Phi$.

```python
    check(worst < 1e-12, f"{name}: K4 is real, K4 = V S, and B04 = 0 (T^x4_x0 = 0)")
    check(np.abs(rhos / (m * S_expected + lam / 2 * S_expected ** 2) - 1).max()
          < 1e-9 and np.abs(ps / (lam / 2 * S_expected ** 2) - 1).max() < 1e-9,
          f"{name}: rho = m S + lambda S^2/2, p = lambda S^2/2, S = e^a4 b4^-2 S0")
    trace_error = np.abs(-rhos + 7 * ps - (-m * S_expected + 3 * lam
                                            * S_expected ** 2)).max()
    check(trace_error < 1e-9,
          f"{name}: trace -rho + 7 p = -m S + 3 lambda S^2 at every step")
```

Three checks per condensate: $K_4$ is real, $K_4 = VS$ and $B_{04} = 0$, so that $T^{x_4}{}_{x_0} = 0$ (Section 9.19); $\rho = mS + \frac{\lambda}{2}S^2$ and $p = \frac{\lambda}{2}S^2$ with $S = e^{a_4}b_4^{-2}S_0$ at every time, to $10^{-9}$ (relative); and the trace $-\rho + 7p = -mS + 3\lambda S^2$.

```python
    for index, label in ((0, "x4 = 0"), (800, "x4 = 8"), (-1, "x4 = 16")):
        report(f"{name}: rho, p, w at {label}",
               f"{rhos[index]:.6f}, {ps[index]:.3e}, {ps[index] / rhos[index]:.6f}")
```

The values at $x_4 = 0$, 8 and 16 (index 800 is the time 8; index $-1$ is the last entry). The printed lines are, for $\lambda = 0.5$: `1.250000, 2.500e-01, 0.200000`, `0.035992, 3.182e-04, 0.008840` and `0.001273, 4.049e-07, 0.000318`; for $\lambda = -0.8$: `0.600000, -4.000e-01, -0.666667`, `0.035165, -5.091e-04, -0.014476` and `0.001272, -6.478e-07, -0.000509`. At $x_4 = 0$, with $S = 1$: $\rho = 1 + 0.25 = 1.25$ and $p = 0.25$, and $\rho = 1 - 0.4 = 0.6$ and $p = -0.4$. Both equations of state drift towards 0 as $S$ is diluted.

```python
check(recorded(THEORY_PY, "commuting_homogeneous_on_shell_rho_p") == "PASS"
      and recorded(THEORY_PY, "commuting_T_x4x0_homogeneous") == "PASS"
      and recorded(THEORY_PY, "commuting_trace_on_shell") == "PASS",
      "these are the record's homogeneous values and its vanishing x4-x0 component",
      record=f"{THEORY_PY}, checks commuting_homogeneous_on_shell_rho_p, "
             "commuting_T_x4x0_homogeneous and commuting_trace_on_shell")
```

The record's verdicts for these values (`commuting_homogeneous_on_shell_rho_p`), for the vanishing $x_4$-$x_0$ entry (`commuting_T_x4x0_homogeneous`) and for the trace (`commuting_trace_on_shell`).

**In [9], the energy density and the pressure against S.**

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

For $\lambda = 0.5$ and 401 values of $S$ from $-6$ to 2: $\rho = mS + U$, $p = SU' - U = \frac{\lambda}{2}S^2$, the kinetic part of the pressure $p_{\rm kin} = VS$ and its potential part $p_{\rm pot} = -(mS + U)$; the check asks $p = p_{\rm kin} + p_{\rm pot}$ at every drawn $S$.

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
```

Four curves, two black dots at the zeros $S = 0$ and $S = -2m/\lambda = -4$ of $\rho$ (`"ko"` means black circles), a line at zero, labels, title, legend.

```python
save_figure(fig, "energy_and_pressure",
            "Energy density $\\rho = mS + \\lambda S^2/2$ (solid), pressure "
...)
```

The figure is saved as Figure 09b.3 (`09b_3_energy_and_pressure.png`): a parabola $\rho$ that is negative between $S = -4$ and $S = 0$, a parabola $p \geq 0$, and its two parts.

**In [10], the equation of state of actual solutions.**

```python
x_measured = np.array([-3.5, -3.0, -2.5, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0, 3.0,
                       4.0])  # values of x = lambda S/m at the time x4 = 1.3
S_then = dilution(1.3)  # S at x4 = 1.3 for S0 = 1: e^(-0.5417)
rho_measured, p_measured = [], []  # rho and p of each of the twelve condensates
```

Twelve values of $x = \lambda S/m$; `S_then` is $S$ at $x_4 = 1.3$ for $S_0 = 1$, that is $e^{-(5/12)\cdot 1.3} = e^{-0.5417}$; two empty lists.

```python
for x_value in x_measured:
    lam_x = x_value * m / S_then  # lambda S(1.3) / m = x
    _, phis, dphis, _ = condensate(chi, lam_x, 1.3, 1300)
    S, U, K4, rho, p, B04 = homogeneous_tensor(phis[-1], dphis[-1], lam_x)
    rho_measured.append(rho)
    p_measured.append(p)
rho_measured, p_measured = np.array(rho_measured), np.array(p_measured)
w_measured = p_measured / rho_measured  # the equation of state of each condensate
w_formula = x_measured / (2 + x_measured)
```

For each $x$ the value $\lambda = x\,m/S(1.3)$ makes $\lambda S/m = x$ at the time 1.3; the condensate is solved with RK4 up to that time (1300 steps), and $\rho$ and $p$ are computed from its last column and derivative with `homogeneous_tensor`. Only afterwards is the ratio $w = p/\rho$ formed and compared with the formula.

```python
check(np.abs(w_measured - w_formula).max() < 1e-9,
      "w = p/rho of 12 condensates at x4 = 1.3 equals x/(2 + x), x = lambda S/m")
at_minus_one = w_measured[list(x_measured).index(-1.0)]
check(abs(at_minus_one + 1.0) < 1e-9,
      "w = -1 where the effective mass m + lambda S vanishes (x = -1)")
below = x_measured < -2  # the three condensates with x < -2
check(np.all(rho_measured[below] < 0) and np.all(p_measured[below] < 0)
      and np.all(w_measured[below] > 1),
      "for x < -2: rho < 0, p < 0 and w > 1")
```

Three checks: $p/\rho = x/(2 + x)$ for all twelve, to $10^{-9}$; $w = -1$ at $x = -1$ (`list(x_measured).index(-1.0)` finds the position of $-1$ in the list); and for the three values $x < -2$ both $\rho$ and $p$ are negative and $w > 1$ (`below` is an array of `True` and `False` that selects those entries).

```python
for x_value, w_value in zip(x_measured, w_measured):
    say(f"x = lambda S/m = {x_value:5.1f}:  w = p/rho = {w_value: .6f}")
```

Twelve printed lines (`5.1f` writes the number in five places with one decimal; `: .6f` leaves a blank where a minus sign would stand): $w = 2.333333$, $3.000000$, $5.000000$ for $x = -3.5, -3, -2.5$; $-3.000000$ for $x = -1.5$ (phantom); $-1.000000$ for $x = -1$; $-0.333333$, $0$, $0.2$, $0.333333$ (like radiation, $x = 1$), $0.5$, $0.6$, $0.666667$ for $x = -0.5, 0, 0.5, 1, 2, 3, 4$.

**In [11], the figure of the equation of state.**

```python
fig, ax = plt.subplots()
for piece in (np.linspace(-6.0, -2.05, 300), np.linspace(-1.95, 6.0, 500)):
    ax.plot(piece, piece / (2 + piece), color="tab:blue")  # two branches
```

The curve $w = x/(2 + x)$ in two pieces, left and right of $x = -2$, where it is not defined (a single curve would draw a false vertical line across the gap).

```python
ax.plot(x_measured, w_measured, "o", color="tab:red",
        label="measured on condensates at $x_4 = 1.3$")
ax.axvline(-2.0, color="gray", linestyle=":", label="$\\rho = 0$ ($x = -2$)")
ax.axhline(-1.0, color="tab:green", linestyle="--", label="$w = -1$")
ax.axhline(0.0, color="black", linewidth=0.8)
ax.axhspan(-6.0, -1.0, xmin=0.0, xmax=1.0, color="tab:green", alpha=0.08)
ax.set_ylim(-6.0, 6.0)
ax.set_xlabel("$x = \\lambda S / m$")
ax.set_ylabel("$w = p/\\rho$")
ax.set_title("Equation of state of a condensate: $w = x/(2 + x)$")
ax.legend(fontsize=8, loc="upper right")
```

The twelve measured values as red points, a dotted line at $x = -2$, a dashed line at $w = -1$, a line at zero, the phantom band $w < -1$ shaded faintly (`axhspan` fills a horizontal band, `alpha=0.08` makes it nearly transparent), the vertical range from $-6$ to 6, labels, title and legend.

```python
save_figure(fig, "equation_of_state",
            "Equation of state $w = p/\\rho$ of a condensate of dirac16complex00 "
...)
```

The figure is saved as Figure 09b.4 (`09b_4_equation_of_state.png`); the red points lie on the curve.

**In [12], the map of oscillating and growing condensates.**

```python
x_grid = np.linspace(-3.0, 2.0, 701)  # x = lambda S/m
h_grid = np.linspace(0.0, 2.0, 301)  # c_g/|m|
X, Hgrid = np.meshgrid(x_grid, h_grid)  # every pair (x, c_g/|m|) of the two grids
growing_region = (np.abs(1 + X) < Hgrid).astype(float)  # 1 where c_g^2 > V^2
```

A grid of 701 values of $x$ and 301 values of $c_g/|m|$; `np.meshgrid` makes the two arrays of all pairs. `growing_region` is 1 where $|1 + x| < c_g/|m|$ (then $k^2 > 0$) and 0 elsewhere (`.astype(float)` turns `True` and `False` into 1 and 0).

```python
fig, ax = plt.subplots()
ax.contourf(X, Hgrid, growing_region, levels=[-0.5, 0.5, 1.5],
            colors=["#dbe9f6", "#f6d5d5"])
for label, x_line in (("$w = -1$", -1.0), ("$w = 0$", 0.0), ("$w = 1/3$", 1.0)):
    ax.axvline(x_line, color="black", linestyle="--", linewidth=0.8)
    ax.text(x_line + 0.05, 1.88, label, fontsize=8)
```

`contourf` fills the regions with two colours, light blue where the value is near 0 (oscillating) and light red where it is near 1 (growing); the levels $-0.5$, $0.5$, $1.5$ separate the two values. Three dashed vertical lines mark the equations of state $w = -1$ ($x = -1$), $w = 0$ ($x = 0$) and $w = 1/3$ ($x = 1$), each labelled near the top.

```python
path_times = np.linspace(0.0, 16.0, 1601)
paths = {name: (lam_value * dilution(path_times) / m,  # x(x4) with S0 = 1
                c_g_of(path_times) / abs(m))  # c_g(x4)/|m|
         for name, lam_value in EXAMPLES.items()}
for name, (path_x, path_h) in paths.items():
    ax.plot(path_x, path_h, color="black", linewidth=1.2)
    ax.annotate("", xy=(path_x[-1], path_h[-1]), xytext=(path_x[-40], path_h[-40]),
                arrowprops={"arrowstyle": "->", "color": "black"})
    ax.plot([path_x[0]], [path_h[0]], "ko")
    ax.text(path_x[0] - 0.25, path_h[0] - 0.13, name, fontsize=8)
ax.text(-2.8, 0.3, "oscillating", fontsize=9)
ax.text(-2.4, 1.6, "growing", fontsize=9)
```

The paths of the two condensates of In [6] from $x_4 = 0$ to 16: $x(x_4) = \lambda S_0e^{a_4}b_4^{-2}/m$ and $c_g(x_4)/|m|$ (a dictionary comprehension builds both paths). Each path is drawn as a black curve with an arrow at its end (`annotate` with an empty text draws an arrow from the 40th point before the end to the end), a black dot at its start and its name; two texts name the regions.

```python
ax.set_xlabel("$x = \\lambda S / m$")
ax.set_ylabel("$c_g/|m|$")
ax.set_title("Condensates: oscillating (blue) or growing (red)")
ax.grid(False)
```

Labels and title; no grid lines across the coloured regions.

```python
save_figure(fig, "regime_map",
            "Map of the condensates of dirac16complex00 in the plane of "
...)
```

The figure is saved as Figure 09b.5 (`09b_5_regime_map.png`). The student sees the red wedge opening upwards from the point $x = -1$ on the horizontal axis, and the two paths moving towards $x = 0$ and upwards until both end inside the wedge.

```python
inside = {name: np.abs(1 + path_x) < path_h for name, (path_x, path_h) in paths.items()}
entries = {name: path_times[1:][np.diff(inside[name].astype(int)) != 0]
           for name in EXAMPLES}  # the grid times just after each change
```

`inside` marks, for each path, the times at which it lies in the wedge; `np.diff` of the marks (as integers) is nonzero exactly where a path crosses the boundary of the wedge, and `entries` keeps the grid times just after each crossing.

```python
check(not inside["oscillating first"][0] and len(entries["oscillating first"]) == 1
      and abs(entries["oscillating first"][0] - CHANGES["oscillating first"][0])
      < 0.011,
      "lambda = 0.5: starts oscillating, enters the growing wedge once")
check(bool(inside["growing first"][0]) and len(entries["growing first"]) == 2
      and np.abs(entries["growing first"] - CHANGES["growing first"]).max() < 0.011,
      "lambda = -0.8: starts in the wedge, leaves it and enters it again")
```

Two checks: the condensate with $\lambda = 0.5$ starts outside the wedge and crosses its boundary once, within 0.011 of the moment found by bisection in In [6] (the grid step is 0.01); the condensate with $\lambda = -0.8$ starts inside and crosses twice, at the two moments of In [6].

**In [13], a condensate is only diluted.**

```python
times, phis, dphis, _ = solutions["oscillating first"]
rho_and_p = np.array([homogeneous_tensor(phi, dphi, 0.5)[3:5]
                      for phi, dphi in zip(phis, dphis)])
rho_at_times, p_at_times = rho_and_p[:, 0], rho_and_p[:, 1]
slope = np.gradient(rho_at_times, times)  # d rho/dx4 by finite differences
dilution_rate = 3 * a4p + 4 * h4  # 5/12 on this history
diluted = -dilution_rate * (rho_at_times + p_at_times)  # -(3 a4' + 4 h4)(rho + p)
```

For the condensate with $\lambda = 0.5$ the cell computes $\rho$ and $p$ at every step (`[3:5]` takes the fourth and the fifth value that `homogeneous_tensor` returns), the slope $d\rho/dx_4$ by finite differences (`np.gradient`), the dilution rate $3a_4' + 4h_4 = \frac34 - \frac13 = \frac{5}{12}$, and the right side $-(3a_4' + 4h_4)(\rho + p)$ of Section 9.19.

```python
# [2:-2] leaves out two points at each end, where np.gradient is less exact.
check(np.abs(slope - diluted)[2:-2].max() < 1e-4 * np.abs(diluted).max()
      and recorded(THEORY_WL, "energy_exchange_equation") == "PASS"
      and recorded(THEORY_PY, "energy_exchange_equation") == "PASS",
      "condensate (p3 = p_t = p0): d rho/dx4 = -(3 a4' + 4 h4)(rho + p)",
      record=f"{THEORY_WL} and {THEORY_PY}, check energy_exchange_equation")
```

The slope must agree with the right side to $10^{-4}$ of its largest size, without two points at each end, where `np.gradient` is less exact; the record's verdicts of `energy_exchange_equation` complete the check.

```python
report("dilution rate 3 a4' + 4 h4 = 2 b4'/b4 - a4'", f"{dilution_rate:.6f}")
```

It prints `RESULT dilution rate 3 a4' + 4 h4 = 2 b4'/b4 - a4' = 0.416667`, that is $\frac{5}{12}$.

**In [14], toy fluids (an ILLUSTRATION).**

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

`rk4(rate, y0, step, count)` solves $dy/dx = \mathrm{rate}(y)$ for a number $y$ with `count` RK4 steps and returns the path, the same method as in In [5] for a single number.

```python
def toy_rate(delta, w_t, sign=1.0):
    """The rate of rho of a toy fluid; sign -1 reverses the history (A -> -A)."""
    return -sign * A * H * (3 * delta + (2 * beta - 1) * (1 + w_t))
```

`toy_rate(delta, w_t, sign)` is the constant rate $-AH\big(3\Delta w + (2\beta - 1)(1 + w_t)\big)$ of Section 9.10; `sign=-1.0` reverses the history ($A \to -A$).

```python
STEP, COUNT = 0.05, 160  # x4 from 0 to 8
toy_times = STEP * np.arange(COUNT + 1)
DELTAS = (-5 / 9, -1 / 3, 0.0, 1 / 3, 2 / 3)  # Delta w = w3 - w_t, with w_t = 0
toy = {}  # Delta w -> rho(x4)/rho0 along the history
errors = {STEP: 0.0, STEP / 2: 0.0}  # the largest relative error for two steps
```

The step 0.05 and 160 steps (from $x_4 = 0$ to 8), the times, the five values of $\Delta w$ (with $w_t = 0$), a dictionary for the paths, and a dictionary of the largest relative errors for the two steps 0.05 and 0.025.

```python
for delta in DELTAS:
    for step in errors:
        count = round(8.0 / step)  # the number of steps from x4 = 0 to 8
        path = rk4(lambda r, d=delta: toy_rate(d, 0.0) * r, 1.0, step, count)
        exact = np.exp(toy_rate(delta, 0.0) * step * np.arange(count + 1))
        errors[step] = max(errors[step], np.abs(path / exact - 1).max())
        if step == STEP:
            toy[delta] = path
```

For each $\Delta w$ and each step the equation $d\rho/dx_4 = \mathrm{rate}\cdot\rho$ is solved from $\rho(0) = 1$ and compared with the exact exponential. The `lambda r, d=delta: ...` is a small unnamed function of `r`; `d=delta` freezes the current value of `delta` inside it. The paths with the step 0.05 are kept.

```python
check(errors[STEP] < 1e-6,
      "RK4 (step 0.05) reproduces the exponential rho of 5 toy fluids")
ratio = errors[STEP] / errors[STEP / 2]  # RK4: half the step, 1/16 of the error
check(14 < ratio < 18, "halving the RK4 step divides the error by about 2^4 = 16")
report("largest relative RK4 error, step 0.05", f"{errors[STEP]:.2e}")
report("error ratio of the steps 0.05 and 0.025", f"{ratio:.2f}")
```

Two checks: the error with the step 0.05 is below $10^{-6}$, and halving the step divides it by a number between 14 and 18 (RK4: about $2^4 = 16$). The printed values are `2.80e-07` and `16.31`.

```python
reversed_path = rk4(lambda r: toy_rate(1 / 3, 0.0, -1.0) * r, 1.0, STEP, COUNT)
check(np.abs(reversed_path * toy[1 / 3] - 1).max() < 1e-8,
      "A -> -A reverses the energy flow (the product of the two paths is 1)")
report("toy fluid Delta w = 1/3, w_t = 0: rho(8)/rho(0)", f"{toy[1 / 3][-1]:.6f}")
```

The reversed history for $\Delta w = \frac13$: the product of the two paths must be 1 at every time, because the two exponents are opposite. The last line prints `toy fluid Delta w = 1/3, w_t = 0: rho(8)/rho(0) = 0.004828`, the number $e^{-16/3}$ of Section 9.10.

**In [15], the figure of the energy exchange.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(9.6, 3.9))
fig.subplots_adjust(wspace=0.35)  # more room between the two panels
for delta in DELTAS:
    left.plot(toy_times, toy[delta], label=f"toy, $\\Delta w = {delta:+.2f}$")
left.plot(times[times <= 8.0], rho_at_times[times <= 8.0] / rho_at_times[0], "k:",
          linewidth=2.0, label="condensate ($p_3 = p_t = p_0$)")
left.set_yscale("log")
left.set_xlabel("time $x_4$")
left.set_ylabel("$\\rho(x_4) / \\rho(0)$")
left.set_title("Energy density along the history ($w_t = 0$)")
left.legend(fontsize=7)
```

Two panels with more room between them. Left: the five toy fluids and, dotted, the energy density of the condensate with $\lambda = 0.5$ divided by its first value, for $x_4 \le 8$ (`times <= 8.0` selects those entries), on a logarithmic axis.

```python
rho_toy = rk4(lambda r: toy_rate(-1 / 3, 2 / 3) * r, 1.0, STEP, COUNT)
work_space = -3 * a4p * (1 / 3) * rho_toy  # -3 a4' p3 with p3 = rho/3
work_block = -4 * h4 * (2 / 3) * rho_toy  # -h4 (3 p_t + p0) with p_t = p0 = 2 rho/3
dilution_toy = -dilution_rate * rho_toy  # -(3 a4' + 4 h4) rho
```

The toy fluid with $(w_3, w_t) = (\frac13, \frac23)$, that is $\Delta w = -\frac13$, and its three terms: the work of 3-space $-3a_4'p_3$ with $p_3 = \rho/3$, the work of the block $-h_4(3p_t + p_0) = -4h_4p_t$ with $p_t = p_0 = \frac23\rho$, and the dilution $-(3a_4' + 4h_4)\rho$.

```python
right.plot(toy_times, work_space, label="3-space: $-3a_4' p_3$")
right.plot(toy_times, work_block, "--", label="block: $-h_4(3p_t + p_0)$")
right.plot(toy_times, dilution_toy, "-.",
           label="dilution: $-(3a_4' + 4h_4)\\rho$")
right.plot(toy_times, np.gradient(rho_toy, toy_times), ":", color="black",
           label="$d\\rho/dx_4$ (finite differences)")
right.axhline(0.0, color="black", linewidth=0.8)
right.set_xlabel("time $x_4$")
right.set_ylabel("rate of change of $\\rho$")
right.set_title("Toy fluid $(w_3, w_t) = (1/3, 2/3)$")
right.legend(fontsize=7)
```

The three terms and the slope $d\rho/dx_4$ of the path (finite differences) are drawn in the right panel, with a line at zero, labels, title and legend.

```python
save_figure(fig, "energy_exchange",
            "Energy exchange and dilution along the history $a_4 = AHx_4$, "
...)
```

The figure is saved as Figure 09b.6 (`09b_6_energy_exchange.png`). Left, straight lines on the logarithmic axis: $\rho$ falls fastest for the largest $\Delta w$, stays constant for $\Delta w = -\frac59$ and falls everywhere else; the condensate curve is not straight, because $\rho + p$ is not proportional to $\rho$. Right, the work of 3-space is negative, the work of the deflating block positive, and the three terms add up to the dotted slope.

```python
# [2:-2] leaves out two points at each end, where np.gradient is less exact.
check(np.abs(np.gradient(rho_toy, toy_times)
             - (work_space + work_block + dilution_toy))[2:-2].max() < 1e-3,
      "d rho/dx4 equals the sum of the three terms on the drawn path")
```

The check: the slope of the drawn path equals the sum of the three terms to $10^{-3}$ (the error of the finite differences).

**In [16], plane waves in flat space.**

```python
m_flat, E_flat = 2.0, 5.0
momentum = {0: 4.0, 1: 1.0, 2: 2.0, 3: 0.0}  # k0, k1, k2, k3 (x5, x6, x7: zero)
beta_matrix = -1j * g4  # Dirac's beta; the name beta is the history's exponent
h = m_flat * beta_matrix + sum(k_a * (-g4 @ gamma[a]) for a, k_a in momentum.items())
```

The example of the record: $m = 2$, $E = 5$, the momenta $k_0 = 4$, $k_1 = 1$, $k_2 = 2$, $k_3 = 0$ (a dictionary from the direction to its momentum), Dirac's matrix $\beta = -i\gamma^{(4)}$ (called `beta_matrix`, because `beta` is the exponent of the history), and $h = m\beta + \sum_ak_a\alpha^a$ with $\alpha^a = -\gamma^{(4)}\gamma^{(a)}$ of Section 9.21.

```python
check(np.abs(h - h.conj().T).max() < 1e-12 and np.abs(h @ h - 25 * I16).max() < 1e-12
      and np.abs(B @ h - h @ B).max() < 1e-12,
      "h is Hermitian, h^2 = 25, and h commutes with B")
```

$h$ equals its conjugate transpose (it is Hermitian), $h^2 = 25$ times the unit matrix ($m^2 + k_0^2 + k_1^2 + k_2^2 + k_3^2 = 4 + 16 + 1 + 4 = 25$), and $h$ commutes with $B$.

```python
energies, vectors = np.linalg.eigh(h)  # eigenvalues in ascending order
U5 = vectors[:, energies > 0]  # the eight columns with eigenvalue +5
form = U5.conj().T @ B @ U5  # u^dagger B u on the eigenspace, as an 8 x 8 matrix
inertia, directions = np.linalg.eigh(form)
```

`np.linalg.eigh` returns the eigenvalues of a Hermitian matrix in ascending order and the eigenvectors as columns. `U5` keeps the eight columns with eigenvalue $+5$; `form` is the $8 \times 8$ matrix of $u^\dagger Bu$ on that space, and its eigenvalues `inertia` and eigenvectors `directions` give the positive and negative directions of the form.

```python
PAIRING = "Revision/pairing/reports/python-pairing.json"
check(np.allclose(energies, [-5.0] * 8 + [5.0] * 8, atol=1e-12)
      and np.allclose(inertia, [-1.0] * 4 + [1.0] * 4, atol=1e-12)
      and recorded(PAIRING, "Q.one_particle_Krein_inertia_proof") == "PASS",
      "E = +-5 (eight each); u^dagger B u has inertia (4,4) on the E = 5 space",
      record=f"{PAIRING}, check Q.one_particle_Krein_inertia_proof (every real "
             "frequency)")
```

The check: eigenvalues $-5$ and $+5$, eight each, and the form has the eigenvalues $-1$ (four times) and $+1$ (four times), Krein inertia (4,4), with the record's verdict of `Q.one_particle_Krein_inertia_proof`.

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

`flat_energy_density(u)` computes $\rho = -\sum_{a \neq x_4}K_a + mS$ for the plane wave $u\,e^{i(k\cdot x - Ex_4)}$ from its kinetic terms, with $\partial_a\Phi = ik_a\Phi$ (the exponential factor has size 1 and drops out of every bilinear).

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

Column 0 of `directions` has the eigenvalue $-1$ of the form and column 7 the eigenvalue $+1$. For each, `u` is the corresponding unit vector of the eigenspace; the check confirms that the plane wave solves the flat field equation $\sum_a\gamma^{(a)}\partial_a\Phi = m\Phi$ (with $\partial_4\Phi = -iE\Phi$) and that $Bu = \mp u$. Its energy density is stored.

```python
SCOPE_PY = "Revision/theory/reports/python-scope.json"
SCOPE_WL = "Revision/theory/reports/wolfram-scope.json"
check(abs(rho_pair[0] + 5.0) < 1e-12 and abs(rho_pair[1] - 5.0) < 1e-12
      and recorded(SCOPE_PY, "commuting_field_energy_unbounded_below") == "PASS"
      and recorded(SCOPE_WL, "commuting_field_energy_unbounded_below") == "PASS",
      "rho = -5 for B u = -u and rho = +5 for B u = +u (|u| = 1)",
      record=f"{SCOPE_PY} and {SCOPE_WL}, check commuting_field_energy_unbounded_below")
```

The check of the record's values $\rho = -5$ and $\rho = +5$ (`commuting_field_energy_unbounded_below`, both scope reports).

**In [18], 5000 random waves.**

```python
samples = rng.normal(size=(5000, 8)) + 1j * rng.normal(size=(5000, 8))
samples /= np.linalg.norm(samples, axis=1)[:, None]
us = samples @ U5.T  # 5000 random unit vectors of the eigenspace
charges = np.einsum("ni,ij,nj->n", us.conj(), B, us).real  # u^dagger B u
rho_samples = np.array([flat_energy_density(u) for u in us])
```

5000 random complex combinations of the eight columns of `U5`, each of length 1 (`samples @ U5.T` makes each row a unit vector of the eigenspace, because the columns of `U5` are orthonormal); their values $u^\dagger Bu$ and their energy densities.

```python
check(np.abs(rho_samples - E_flat * charges).max() < 1e-12
      and rho_samples.min() < 0 < rho_samples.max(),
      "rho = E u^dagger B u for all 5000 random u of the eigenspace; both signs")
report("smallest and largest rho of the 5000 samples",
       f"{rho_samples.min():.4f} and {rho_samples.max():.4f}")
```

The check: $\rho = E\,u^\dagger Bu$ for all 5000, and both signs occur. It prints `smallest and largest rho of the 5000 samples = -4.7554 and 4.3825`; these two numbers are extremes of random samples, computed through many sums of products, and on another computer their last digits can differ at the level of rounding, while every check passes.

**In [19], the histogram of the energy densities.**

```python
fig, ax = plt.subplots()
ax.hist(rho_samples, bins=50, range=(-5.0, 5.0), color="tab:purple", edgecolor="white")
ax.axvline(0.0, color="black", linewidth=1.0)
ax.set_xlabel("energy density $\\rho = E\\,u^\\dagger B u$ of the plane wave")
ax.set_ylabel("number of the 5000 random $u$")
ax.set_title("Waves of positive frequency $E = 5$: $\\rho$ has both signs")
```

A histogram of the 5000 values in 50 intervals between $-5$ and $5$, with a line at zero.

```python
save_figure(fig, "energy_sign",
            "Histogram of the energy density $\\rho = -\\sum_{a \\neq x_4} K_a + mS$ "
...)
```

The figure is saved as Figure 09b.7 (`09b_7_energy_sign.png`): the values fill the interval from $-5$ to $5$, crowding near the middle, about half of them negative.

**In [20], the last check.**

```python
captions = json.loads(output_file(CAPTION_FILE).read_text(encoding="utf-8"))
expected_files = ["09b_1_sign_of_s.png", "09b_2_condensate_solutions.png",
                  "09b_3_energy_and_pressure.png", "09b_4_equation_of_state.png",
                  "09b_5_regime_map.png", "09b_6_energy_exchange.png",
                  "09b_7_energy_sign.png"]
```

The captions file is read back, and the seven expected figure files are listed.

```python
check(sorted(captions) == expected_files and all(
    output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in expected_files),
    "the seven figures of this notebook are saved and captioned")
all_checks_passed()
```

The check that the captions file names exactly these seven files and that each exists; the last line prints `ALL 35 CHECKS PASSED (notebook 09b)`.

### 9.26 The full tensor of a condensate

A condensate has the same pressure in all seven directions. That does not yet make it a **perfect fluid at rest**, which has a diagonal energy-momentum tensor: Section 9.12 showed that the spin connection puts entries off the diagonal. For a condensate $\partial_\mu\Phi = 0$ for $\mu \neq x_4$, but $D_\mu\Phi = \Omega_\mu\Phi$ is not zero along the hidden direction, 3-space and the extra times, because $\Omega_{x_0}$, $\Omega_{x_i}$ and $\Omega_{x_t}$ are not zero; and its time derivative $\partial_4\Phi = (M - v_g)\Phi$ contains the gravitational part $c_g\gamma^{(4)}\gamma^{(0)}$ of $M$ (Section 9.18, with $\Phi = F\chi$ and $F' = -v_gF$).

**The structure, from the record.** Off the diagonal the tensor of Section 9.6 is $T^\nu{}_\mu = -K^{(\nu}{}_{\mu)}$ with

$$
K^\nu{}_\mu = \tfrac12\big(\bar\Phi\gamma^\nu D_\mu\Phi - D_\mu\bar\Phi\,\gamma^\nu\Phi\big), \qquad K^{(\nu}{}_{\mu)} = \tfrac12\big(K^\nu{}_\mu + g^{\nu\nu}g_{\mu\mu}K^\mu{}_\nu\big),
$$

because the first pair of terms in the bracket of Section 9.6 is $2K^\nu{}_\mu$ and the second pair is $g_{\mu\mu}g^{\nu\nu}\cdot 2K^\mu{}_\nu$ (move the metric factors of $\gamma_\mu = g_{\mu\mu}\gamma^\mu$ and $D^\nu = g^{\nu\nu}D_\nu$ in front). The Revision record proves three facts for every condensate, for all functions $a_4$, $b_4$ and every real $z$ (PROVED; the table names the record files and checks; the coefficients themselves are stored in the record file `Revision/field_equations_a4/a4-equations.json` under the entry `offDiagonalKinetic`):

| statement | Revision report | check |
| --- | --- | --- |
| the diagonal of the tensor of a condensate, and $T^{x_4}{}_{x_0} = T^{x_0}{}_{x_4} = 0$ | `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `condensate_kinetic_tensor_diagonal` |
| the same, with the author's gammas | `Revision/field_equations_a4/reports/python-a4-report.json` | `authorT16_condensate_kinetic_diagonal` |
| the entries off the diagonal are combinations of 24 three-gamma bilinears | `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `condensate_offdiagonal_are_three_gamma_bilinears` |
| the same, with the author's gammas | `Revision/field_equations_a4/reports/python-a4-report.json` | `authorT16_condensate_offdiagonal_three_gamma` |
| the stored coefficients are the computed ones, in two representations of the gammas | `Revision/field_equations_a4/reports/python-a4-report.json` | `json_offdiagonal_coefficients`, `offdiagonal_coefficients_representation_independent` |

The three facts are:

- the diagonal is $T^{x_4}{}_{x_4} = -VS + L_0$ and $T^\mu{}_\mu = L_0$ otherwise (Section 9.19), and $T^{x_4}{}_{x_0} = T^{x_0}{}_{x_4} = 0$;
- exactly 36 of the 56 entries off the diagonal are nonzero in general: the 6 entries between the hidden direction and 3-space ($x_0$-$x_i$, both orders), the 6 flows between the time and 3-space ($x_i$-$x_4$), the 18 entries between 3-space and the extra times ($x_i$-$x_t$) and the 6 flows between the time and the extra times ($x_4$-$x_t$); the 20 others vanish ($x_4$-$x_0$, $x_0$-$x_t$, and the entries inside 3-space and inside the extra times);
- each nonzero entry is a fixed combination of one or two of 24 **three-gamma bilinears** $B(a\,b\,c) = \bar\Phi\gamma^{(a)}\gamma^{(b)}\gamma^{(c)}\Phi$, with coefficients that depend on $H$, $a_4$, $a_4'$, $b_4$, $b_4'/b_4$ and $z$ but not on $V$: the pairs $x_0$-$x_i$ and $x_i$-$x_4$ carry $B(x_0\,x_i\,x_4)$ (three bilinears), the pairs $x_4$-$x_t$ carry $B(x_0\,x_4\,x_t)$ (three), and the pairs $x_i$-$x_t$ carry the two bilinears $B(x_0\,x_i\,x_t)$ and $B(x_i\,x_4\,x_t)$ (nine of each).

**One entry, line by line: the stress between 3-space and the hidden direction.** Take $T^{x_1}{}_{x_0}$. Neither $K^{x_1}{}_{x_0}$ nor $K^{x_0}{}_{x_1}$ contains a derivative of $\Phi$ (there is none along $x_0$ or $x_1$), so, exactly as in Section 9.12, each is $\frac12\bar\Phi\{\gamma^\nu, \Omega_\mu\}\Phi$. The anticommutator of a gamma with a product of two other gammas is twice the product of the three, $\{\gamma^{(a)}, \gamma^{(b)}\gamma^{(c)}\} = 2\gamma^{(a)}\gamma^{(b)}\gamma^{(c)}$ (moving $\gamma^{(a)}$ from the right end to the front, past two gammas, costs two minus signs). With $\gamma^{x_1} = \gamma^{(1)}/e^{a_4}$ and $\gamma^{x_0} = \gamma^{(0)}/(s_b\cot z)$:

$$
\begin{aligned}
K^{x_1}{}_{x_0} &= \tfrac12\cdot\frac{1}{e^{a_4}}\cdot\tfrac12h_4s_b\cot z\;\bar\Phi\{\gamma^{(1)}, \gamma^{(0)}\gamma^{(4)}\}\Phi = -\tfrac12e^{-a_4}h_4s_b\cot z\;B(x_0\,x_1\,x_4), \\
K^{x_0}{}_{x_1} &= \tfrac12\cdot\frac{1}{s_b\cot z}\cdot\tfrac12a_4'e^{a_4}\;\bar\Phi\{\gamma^{(0)}, \gamma^{(1)}\gamma^{(4)}\}\Phi = \frac{a_4'e^{a_4}}{2s_b\cot z}\;B(x_0\,x_1\,x_4), \\
g^{11}g_{00}K^{x_0}{}_{x_1} &= e^{-2a_4}\cdot s_b^2\cot^2 z\cdot\frac{a_4'e^{a_4}}{2s_b\cot z}\;B(x_0\,x_1\,x_4) = \tfrac12e^{-a_4}a_4's_b\cot z\;B(x_0\,x_1\,x_4), \\
T^{x_1}{}_{x_0} &= -\tfrac12\Big(K^{x_1}{}_{x_0} + g^{11}g_{00}K^{x_0}{}_{x_1}\Big) = -\tfrac14e^{-a_4}s_b\cot z\,\big(a_4' - h_4\big)\,B(x_0\,x_1\,x_4) \\
&= -\tfrac18e^{-2a_4}b_4^{1/2}\cot z\,\Big(4a_4' - \frac{b_4'}{b_4}\Big)\,B(x_0\,x_1\,x_4) .
\end{aligned}
$$

The first line inserts $\gamma^{x_1}$ and $\Omega_{x_0} = \frac12h_4s_b\cot z\,\gamma^{(0)}\gamma^{(4)}$, replaces the anticommutator by $2\gamma^{(1)}\gamma^{(0)}\gamma^{(4)} = -2\gamma^{(0)}\gamma^{(1)}\gamma^{(4)}$ (one exchange to reach the order $0, 1, 4$), and cancels the factors 2. The second inserts $\gamma^{x_0}$ and $\Omega_{x_1} = \frac12a_4'e^{a_4}\gamma^{(1)}\gamma^{(4)}$; its anticommutator is $2\gamma^{(0)}\gamma^{(1)}\gamma^{(4)}$, already in order. The third multiplies by $g^{11}g_{00} = e^{-2a_4}\,s_b^2\cot^2 z$ and cancels. The fourth adds the first and the third line and multiplies by $-\frac12$. The fifth uses $a_4' - h_4 = a_4' - \frac{u}{2} + a_4' = \frac12(4a_4' - u)$ and $e^{-a_4}s_b = e^{-2a_4}b_4^{1/2}$. The record lists the symmetrised $K^{x_1}{}_{x_0}$ with the coefficient

$$
-\frac18\,\frac{b_4^{1/2}(-1 + \sin^2 z)(4a_4' - u)}{\cos z\;e^{2a_4}\sin z} = \frac18e^{-2a_4}b_4^{1/2}\cot z\,(4a_4' - u)
$$

(because $-1 + \sin^2 z = -\cos^2 z$), and $T = -K$: the same. At the point $a_4 = 0.5$, $a_4' = 0.25$, $b_4 = e^{2/3}$, $u = \frac13$, $z = \pi/4$ the coefficient of $K$ is $\frac18e^{-1}e^{1/3}\cdot 1\cdot(1 - \frac13) = \frac{1}{12}e^{-2/3} = 0.042785$, the number that Notebook 09c prints for $K^{x_1}{}_{x_0}$ in In [9]. What the formula says: $4a_4' - u = 0$ exactly when $a_4' = \frac{u}{2} - a_4' = h_4$, that is when 3-space and the block change at the same rate. On the deflating history they do not ($a_4' = AH$, $h_4 = -\frac{AH}{3}$), and the six entries between 3-space and the hidden direction are nonzero; at a moment with $4a_4' = b_4'/b_4$, or on a static history, they vanish and 30 off-diagonal entries remain (Notebook 09c, In [5] and In [7]).

**A second entry: the momentum flow $T^{x_4}{}_{x_1}$.** Section 9.12 showed $K^{x_4}{}_{x_1} = 0$. The flow comes from the other piece, $g^{44}g_{11}K^{x_1}{}_{x_4}$, which contains the time derivative of the condensate. At one point, with $\Omega_{x_4} = 0$ (so $D_{x_4} = \partial_4$), $\partial_4\Phi = (M - v_g)\Phi$ and $\partial_4\bar\Phi = \big((M - v_g)\Phi\big)^\dagger C = \Phi^\dagger(M^TC - v_gC) = -\bar\Phi(M + v_g)$ (Section 9.18: $M^TC = -CM$), line by line:

$$
\begin{aligned}
K^{x_1}{}_{x_4} &= \tfrac12\big(\bar\Phi\gamma^{x_1}(M - v_g)\Phi + \bar\Phi(M + v_g)\gamma^{x_1}\Phi\big) \\
&= \frac{1}{2e^{a_4}}\,\bar\Phi\{\gamma^{(1)}, M\}\Phi, \\
\{\gamma^{(1)}, M\} &= -V\{\gamma^{(1)}, \gamma^{(4)}\} + c_g\{\gamma^{(1)}, \gamma^{(4)}\gamma^{(0)}\} \\
&= 0 + 2c_g\,\gamma^{(1)}\gamma^{(4)}\gamma^{(0)} = 2c_g\,\gamma^{(0)}\gamma^{(1)}\gamma^{(4)}, \\
K^{x_1}{}_{x_4} &= c_ge^{-a_4}\,B(x_0\,x_1\,x_4) = \tfrac32Hb_4^{-1/2}\,B(x_0\,x_1\,x_4), \\
T^{x_4}{}_{x_1} &= -\tfrac12\Big(K^{x_4}{}_{x_1} + g^{44}g_{11}K^{x_1}{}_{x_4}\Big) \\
&= -\tfrac12\Big(0 + (-1)\,e^{2a_4}\cdot\tfrac32Hb_4^{-1/2}\Big)B(x_0\,x_1\,x_4) = \tfrac34He^{2a_4}b_4^{-1/2}\,B(x_0\,x_1\,x_4) .
\end{aligned}
$$

The first two lines insert the two derivatives into the definition of $K^{x_1}{}_{x_4}$ and $\gamma^{x_1} = \gamma^{(1)}/e^{a_4}$; the two terms with $v_g$ cancel and leave the anticommutator. The third and the fourth insert $M = -V\gamma^{(4)} + c_g\gamma^{(4)}\gamma^{(0)}$: two different gammas anticommute, so $\{\gamma^{(1)}, \gamma^{(4)}\} = 0$, the anticommutator with a product of two other gammas is twice the product of the three, and two exchanges bring $\gamma^{(1)}\gamma^{(4)}\gamma^{(0)}$ into the order $0, 1, 4$ (two minus signs). The fifth collects, with $c_ge^{-a_4} = \frac32He^{a_4}b_4^{-1/2}e^{-a_4} = \frac32Hb_4^{-1/2}$. The last two add the two pieces with $g^{44}g_{11} = (1/g_{44})\,g_{11} = (-1)\,e^{2a_4}$. The record lists the symmetrised $K^{x_4}{}_{x_1}$ with the coefficient $-\frac34He^{2a_4}b_4^{-1/2}$ (and $T = -K$); at the point of Notebook 09c ($H = 1$) it is $-0.75\,e^{2/3} = -1.460801$, printed in In [9]. Three things follow. The effective mass $V$ has dropped out. The coefficient contains $H$ and neither $a_4'$ nor $b_4'$, so the 12 momentum flows remain on a static history. And the whole flow comes from the term $c_g\gamma^{(4)}\gamma^{(0)}$ of $M$, that is from the gravitational term $c_g\gamma^{(0)}$ of the field equation (Fact 2 of Section 9.3): without that term a condensate would have no momentum flow along 3-space at all. Notebook 09c uses this as its negative control.

**Condensates with a diagonal tensor.** The record also constructs exact condensates for which all 24 bilinears vanish, so that their tensor is diagonal: a perfect fluid at rest, with $T^{x_4}{}_{x_4} = -VS + L_0$ and pressure $L_0$. They live on the histories along which the ratio $e^{2a_4}/b_4$ keeps a constant value $k_0$ (the record calls this ratio $k$, written `kk`), that is $b_4 = e^{2a_4}/k_0$ with any function $a_4$. On such a history $u = 2a_4'$, so $h_4 = \frac{u}{2} - a_4' = 0$: the block neither grows nor shrinks, and $c_g = \frac32He^{a_4}b_4^{-1/2} = \frac32H\sqrt{k_0}$ is a constant. With $\lambda = 0$ the effective mass $V = m$ is constant too, and so is $M$ (Section 9.18). The construction uses the three matrices $P_1 = \gamma^{(1)}\gamma^{(5)}$, $P_2 = \gamma^{(2)}\gamma^{(6)}$, $P_3 = \gamma^{(3)}\gamma^{(7)}$, which pair each 3-space direction with an extra time. Each squares to 1 ($\gamma^{(1)}\gamma^{(5)}\gamma^{(1)}\gamma^{(5)} = -\gamma^{(1)}\gamma^{(1)}\gamma^{(5)}\gamma^{(5)} = -(1)(-1) = 1$), they commute with each other and with $M$ (moving a product of two gammas past another gamma with a different index costs two minus signs), and each anticommutes with $C$ ($C = \gamma^{(0)}\gamma^{(1)}\gamma^{(2)}\gamma^{(3)}$ contains $\gamma^{(k)}$ but not $\gamma^{(k+4)}$, so moving $P_k$ through $C$ costs three minus signs for $\gamma^{(k)}$ and four for $\gamma^{(k+4)}$). When $V^2 > c_g^2$, let $\omega = \sqrt{V^2 - c_g^2} = \sqrt{V^2 - \frac94H^2k_0}$; then $M^2 = -\omega^2$ (Section 9.18, with $k^2 = c_g^2 - V^2 = -\omega^2$). Four steps build the condensate.

- **Step 1: two spaces of dimension 8.** For any column $u$ put $u_- = \frac12\big(u + \frac{i}{\omega}Mu\big)$ and $u_+ = \frac12\big(u - \frac{i}{\omega}Mu\big)$. Then $u_- + u_+ = u$, and $Mu_- = \frac12\big(Mu + \frac{i}{\omega}M^2u\big) = \frac12\big(Mu - i\omega u\big) = -i\omega\,u_-$ (insert $M^2 = -\omega^2$, then take out the factor $-i\omega$, using $-i\omega\cdot\frac{i}{\omega} = 1$); in the same way $Mu_+ = +i\omega\,u_+$. So every column is the sum of a column of the space $E_-$ of the eigenvalue $-i\omega$ and a column of the space $E_+$ of the eigenvalue $+i\omega$; a nonzero column cannot lie in both (it cannot have two different eigenvalues), so the dimensions of $E_-$ and $E_+$ add up to 16. $M$ is real, so for $Mu = -i\omega u$ the complex conjugate column $\bar u$ obeys $M\bar u = \overline{Mu} = \overline{-i\omega u} = +i\omega\,\bar u$: complex conjugation carries $E_-$ into $E_+$ and $E_+$ into $E_-$, and it keeps independent columns independent, so the two spaces have the same dimension, $16/2 = 8$.
- **Step 2: eight sectors.** $P_1$, $P_2$, $P_3$ commute with $M$, so they map $E_-$ into itself (if $Mu = -i\omega u$ then $M(P_ku) = P_kMu = -i\omega\,P_ku$). Because $P_k^2 = 1$, the matrix $\frac12(1 + \varepsilon P_k)$, for a sign $\varepsilon = \pm1$, keeps the columns with $P_ku = \varepsilon u$ and sends those with $P_ku = -\varepsilon u$ to zero (it is a **projector**), and $\frac12\big(1 + \frac{i}{\omega}M\big)$, which turns $u$ into $u_-$, keeps $E_-$ and sends $E_+$ to zero. For three signs $\varepsilon_1, \varepsilon_2, \varepsilon_3$ the product $\Pi = \frac12\big(1 + \frac{i}{\omega}M\big)\cdot\frac12(1 + \varepsilon_1P_1)\cdot\frac12(1 + \varepsilon_2P_2)\cdot\frac12(1 + \varepsilon_3P_3)$ of these four commuting projectors keeps exactly the columns of $E_-$ with $P_1 = \varepsilon_1$, $P_2 = \varepsilon_2$, $P_3 = \varepsilon_3$ (a **sector** of $E_-$; there are $2^3 = 8$ of them) and sends every other column to zero; it obeys $\Pi^2 = \Pi$.
- **Step 3: every sector has dimension 1.** For a matrix with $\Pi^2 = \Pi$ every column splits as $u = \Pi u + (u - \Pi u)$, a part that $\Pi$ keeps ($\Pi\Pi u = \Pi u$) and a part that it sends to zero ($\Pi(u - \Pi u) = 0$). In a basis made of kept and of removed columns $\Pi$ is diagonal with entries 1 and 0, so its **trace** (the sum of its diagonal entries, which is the same in every basis because $\mathrm{tr}(AB) = \mathrm{tr}(BA)$) is the dimension of the kept space. Multiply out $\Pi$: it is $\frac1{16}$ times the unit matrix plus terms that are each a number times a product of 1 to 8 different frame gammas (the indices of $P_k$ are $k$ and $k + 4$, those of $M = -V\gamma^{(4)} + c_g\gamma^{(4)}\gamma^{(0)}$ are 4 and 0: all different). A product $X$ of $n$ different frame gammas has trace 0: choose a gamma $\gamma^{(b)}$ among its factors if $n$ is even, and one that is not among them if $n$ is odd (then $n \le 7$, so one is left); moving $\gamma^{(b)}$ through $X$ costs $n - 1$ minus signs in the first case and $n$ in the second, an odd number either way, so $X\gamma^{(b)} = -\gamma^{(b)}X$; then $\mathrm{tr}X = \mathrm{tr}\big(X\gamma^{(b)}(\gamma^{(b)})^{-1}\big) = \mathrm{tr}\big((\gamma^{(b)})^{-1}X\gamma^{(b)}\big) = -\mathrm{tr}\big((\gamma^{(b)})^{-1}\gamma^{(b)}X\big) = -\mathrm{tr}X$ (the inverse exists because $(\gamma^{(b)})^2 = \pm1$; the second step is $\mathrm{tr}(AB) = \mathrm{tr}(BA)$), and a number equal to minus itself is 0. Only the unit matrix contributes, $\mathrm{tr}\,\Pi = 16/16 = 1$, and every one of the eight sectors of $E_-$ has dimension 1.
- **Step 4: the condensate.** Take a unit column $v_1$ (a column of length 1) in the sector $P_1 = P_2 = P_3 = -1$ and a unit column $v_2$ in the sector $P_1 = P_2 = P_3 = +1$. By Step 3 each is unique up to a factor $e^{i\theta}$ of size 1. Put $c = \overline{v_1^\dagger Cv_2}$ (the bar over a number means its complex conjugate) and $\Phi_0 = v_1 + cv_2$, a column of $E_-$. Other choices of the factors change nothing that matters: replacing $v_1$ by $e^{i\alpha}v_1$ and $v_2$ by $e^{i\beta}v_2$ replaces $c$ by $e^{i(\alpha - \beta)}c$ and $\Phi_0$ by $e^{i\alpha}\Phi_0$, which leaves every bilinear unchanged. Since $M\Phi_0 = -i\omega\Phi_0$, the column $\chi = e^{-i\omega x_4}\Phi_0$ solves $\chi' = M\chi$, and $\Phi = e^{a_4/2}b_4^{-1}e^{-i\omega x_4}\Phi_0$ is an exact condensate that oscillates with the angular frequency $\omega$ and is diluted by the 7-volume.

A **witness** is an explicit example that proves that something exists. For three choices of $(V, H, k_0)$ the record builds this condensate with exact arithmetic and proves that all 24 of its bilinears vanish; since the time dependence of $\Phi$ is a common number factor, they vanish at every moment, and with them every off-diagonal entry, at every point of every history with $e^{2a_4}/b_4 = k_0$. Each of the three is a witness: it proves that condensates with a diagonal tensor exist on these histories (for histories along which $e^{2a_4}/b_4$ changes, the record does not decide). The record's three witnesses have $(V, H, k_0) = (5, 1, 4)$, $(5, \frac43, 4)$ and $(-5, 1, 4)$, so $c_g = \frac32\cdot 1\cdot 2 = 3$, $\frac32\cdot\frac43\cdot 2 = 4$ and $3$, and $\omega = \sqrt{25 - 9} = 4$, $\sqrt{25 - 16} = 3$ and $4$ (PROVED; `Revision/field_equations_a4/reports/wolfram-a4-report.json`, check `condensate_witness_constant_k_exact`, and `python-a4-report.json`, check `authorT16_condensate_witness`; record entry `fields.dirac16complex00.offDiagonalWitness`; the record writes the effective mass $V$ as $M$ and the frequency as w). For $\lambda = 0$ the pressure $L_0 = SU' - U$ is zero: these witnesses are dust at rest. Notebook 09c builds the same three, confirms numerically the dimensions 8 and 1 of Steps 1 and 3, and checks the diagonal tensor at 36 points. Their $S$ is never negative: $C$ anticommutes with $P_1$, which is real and symmetric, so for $P_1v_1 = -v_1$

$$
v_1^\dagger Cv_1 = -v_1^\dagger CP_1v_1 = v_1^\dagger P_1Cv_1 = (P_1v_1)^\dagger Cv_1 = -v_1^\dagger Cv_1 ,
$$

hence $v_1^\dagger Cv_1 = 0$ (a number equal to minus itself is zero), and likewise $v_2^\dagger Cv_2 = 0$; with $s = v_1^\dagger Cv_2$ one has $v_2^\dagger Cv_1 = \bar s$ ($C$ is real and symmetric) and $c = \bar s$, so $S = \Phi_0^\dagger C\Phi_0 = 0 + c\,s + \bar c\,\bar s + 0 = 2|s|^2 \ge 0$. (The first step replaces $v_1$ by $-P_1v_1$, the second uses $CP_1 = -P_1C$, the third $P_1^\dagger = P_1$, the fourth $P_1v_1 = -v_1$.) For the three witnesses, with $v_1$ and $v_2$ of length 1, Notebook 09c finds $S = 1.28$, $0.72$, $1.28$, that is $S = 2\omega^2/V^2$ (an observation for these three, COMPUTED, not proved); the record's verifier uses columns that are not of length 1, and its three values $51200$, $28800$, $51200$ are $40000$ times these.

**What this means for the field equations of gravity.** The field equations of $a_4$ and $b_4$ (Chapter 12) have one equation for each of the 64 entries. For every entry off the diagonal the gravitational side (the left-hand side) vanishes identically in the corrected metric, so the equation reads $0 = \kappa T^\nu{}_\mu$, and for a coupling $\kappa \neq 0$ every off-diagonal entry of the source must vanish (PROVED; the table below). A condensate whose 24 bilinears all vanish, such as a witness, meets these conditions at every moment, and the record states the conditions for a condensate in exactly this form, as the vanishing of the 24 bilinears. At a single moment the entries give fewer conditions than 24: the lowered tensor is symmetric, so the two entries of each pair are proportional ($g_{\nu\nu}T^\nu{}_\mu = g_{\mu\mu}T^\mu{}_\nu$), and the 18 pairs give one condition each: $B(x_0\,x_i\,x_4) = 0$ (from the pairs $x_i$-$x_4$, whose coefficient $\frac34He^{2a_4}b_4^{-1/2}$ never vanishes), $B(x_0\,x_4\,x_t) = 0$, and for each of the nine pairs $x_i$-$x_t$ one combination of $B(x_0\,x_i\,x_t)$ and $B(x_i\,x_4\,x_t)$ (from the record's two coefficients of the entry $K^{x_i}{}_{x_t}$, $-\frac14HWe^{-a_4}$ and $-\frac18b_4^{1/2}(4a_4' - u)We^{-2a_4}$, the combination $2He^{a_4}B(x_0\,x_i\,x_t) + b_4^{1/2}(4a_4' - u)B(x_i\,x_4\,x_t) = 0$). Whether the record's form, all 24 bilinears zero, follows when these conditions must hold at every moment of a history is not derived in this book.

The diagonal conditions of Section 9.11 hold for every condensate: its entries do not depend on $x_0$, and $p_0 = p_t$. But the field equations also fix the difference $p_3 - p_0$, and a condensate has $p_3 = p_0$. The record finds (PROVED, check `condensate_source_equal_pressures`; record entry `fields.dirac16complex00.asSource`): a source with $p_3 = p_t = p_0$ needs $\sum_k\alpha_k\big(E_{(k)}{}^{x_1}{}_{x_1} - E_{(k)}{}^{x_0}{}_{x_0}\big) = 0$; on the exponential histories $a_4 = AHx_4$, $b_4 = b_4(0)e^{\beta AHx_4}$ Einstein's theory allows no such history, and the author's Lovelock weights allow only histories with a constant $e^{2a_4}/b_4$ (with $\beta = 2$ and $k_0 = (16 + 2A^2)/(2 + A^2)$, or the static history $A = 0$ with $k_0 = 8$), where the remaining equations further require $U(S) = c - mS$ on the range of $S$ for $A \neq 0$ and fix $S_0$ for $A = 0$; histories that are not exponential are not decided. In particular no condensate can be the source of the record's history with $\beta = \frac43$ (Section 9.19).

| statement | Revision record | entry or check |
| --- | --- | --- |
| the off-diagonal equations read $0 = \kappa T^\nu{}_\mu$ | `Revision/field_equations_a4/a4-equations.json` | entry `generalSource.offDiagonal` |
| their left-hand sides vanish identically; $p_0 = p_t$ | `Revision/field_equations_a4/reports/wolfram-a4-report.json` and `python-a4-report.json` | `independent_components` |
| the conditions on the 24 bilinears of a condensate | `Revision/field_equations_a4/a4-equations.json` | entry `fields.dirac16complex00.offDiagonalConditions` |
| the diagonal witnesses on the histories with constant $e^{2a_4}/b_4$ | `Revision/field_equations_a4/a4-equations.json` | entry `fields.dirac16complex00.offDiagonalWitness` |
| a condensate as the source: equal pressures | `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `condensate_source_equal_pressures` |

**Conservation of the full tensor.** The Noether identity proves $\nabla_\mu T^\mu{}_\nu = 0$ for every solution, the 36 off-diagonal entries included (Section 9.9). Notebook 09c tests it numerically on a condensate along the curved history $a_4 = 0.3x_4 + 0.05x_4^2$, $b_4 = e^{0.4x_4 - 0.02x_4^2}$, with a **negative control**: a configuration built so that the test must fail, which shows that the test can detect an error. The control is the condensate of an equation without the gravitational part $c_g\gamma^{(4)}\gamma^{(0)}$ ($M = -V\gamma^{(4)}$). Its $S$ is also $e^{a_4}b_4^{-2}S_0$ and its $K_4 = \frac12\bar\Phi\{\gamma^{(4)}, M\}\Phi = \frac12(-V)(-2)S = VS$ is the same as for the true condensate, so its energy density and pressures are unchanged; but it does not solve the field equation of the corrected metric. The notebook finds that its energy balance ($x_4$), its hidden balance ($x_0$) and its three extra-time balances still hold, while its three momentum balances along 3-space fail (COMPUTED): its momentum flow $T^{x_4}{}_{x_i}$ is zero (the flow comes only from $c_g$, as shown above), while the stresses between 3-space and the hidden direction and the extra times, which come from the spin connection, remain.

### 9.27 Example: the full tensor of a condensate

The third worked example computes all 64 entries of the tensor of exact condensates in the corrected metric. It shows the tensor of a generic condensate (effective mass $V = 5$, $H = 1$, at the point $a_4 = 0.5$, $a_4' = 0.25$, $b_4 = e^{2/3}$, $b_4'/b_4 = \frac13$, $z = \pi/4$) as a heat map and counts its nonzero off-diagonal entries (36, also at $z = 2$ beyond the fold, and 30 when $4a_4' = b_4'/b_4$ or on a static history); shows how four entries depend on $a_4'$; checks that each of the 36 entries is a fixed combination of its bilinears, that 24 bilinears occur, and that the combination is exactly minus the record's coefficients times the bilinears; builds the record's three witnesses on the histories with constant $e^{2a_4}/b_4$, checks the dimensions 8 and 1 of their construction, checks that their tensor is diagonal at 36 points and that their $S = 2|v_1^\dagger Cv_2|^2$, and reproduces the record's frequencies and values of $S$; and tests the conservation of the full tensor with finite differences along a curved history, with the negative control. In this notebook the matrix of the condensate equation is called $A = -V\gamma^{(4)} + c_g\gamma^{(4)}\gamma^{(0)}$; it is the matrix $M$ of Section 9.18 (the record writes it $B$ and uses the letter $M$ for the effective mass $V$), and it has nothing to do with the constant $A$ of the history $a_4 = AHx_4$. The angular frequency of the witnesses is called $\omega$ (in the code `freq`), to keep it apart from the equation of state $w$. The notebook draws five figures.

<!-- NOTEBOOK 09c -->

### 9.30 Line-by-line walk-through of Notebook 09c

The notebook has 20 code cells, In [1] to In [20]. As in Section 9.17, long figure captions are shortened to a line "...)"; the captions are printed in full in Section 9.29, under their figures. Every other line of every code cell is quoted, in order.

**In [1], the set-up cell.** It is word for word the set-up cell of Notebook 09a, explained line by line in Section 9.17, except that its comment lines are the run instructions of Notebook 09c (Section 9.28) and its line `NOTEBOOK_ID = "09c"` names this notebook. It prints `Set-up of notebook 09c complete: repository folder found, helpers defined.`

**In [2], the gammas and two report helpers.**

```python
import numpy as np  # arrays of numbers, matrices, linear algebra

fixture = json.loads(
    repository_file("Revision/algebra/gammas.json").read_text(encoding="utf-8"))
gamma = [np.array(rows, dtype=float) for rows in fixture["gamma"]]  # x0, ..., x7
eta = np.array(fixture["eta"], dtype=float)  # (+1, +1, +1, +1, -1, -1, -1, -1)
C = np.array(fixture["C"], dtype=float)  # gamma^(x0) gamma^(x1) gamma^(x2) gamma^(x3)
I16 = np.eye(16)  # the 16 x 16 unit matrix
g4, g0 = gamma[4], gamma[0]  # gamma^(x4) and gamma^(x0)
NAMES = ["x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7"]  # the author's coordinates
```

The fixture is read as in Notebook 09a: the eight gammas, the frame metric $\eta$, the matrix $C$, the unit matrix, the short names `g4` and `g0` for $\gamma^{(4)}$ and $\gamma^{(0)}$, and the names of the coordinates.

```python
def record_entry(path, name):
    """The entry (name, verdict, detail) of the check name in the report path."""
    report_data = json.loads(repository_file(path).read_text(encoding="utf-8"))
    for item in report_data["checks"]:
        if item["name"] == name:
            return item
    raise KeyError(f"{path} has no check {name}")
```

`record_entry(path, name)` returns the whole entry of one check of a Revision report (a dictionary with its name, its verdict and its detail text); In [13] reads numbers out of the detail text.

```python
def recorded(path, name):
    """The verdict (PASS or FAIL) of the check name in the Revision report path."""
    return record_entry(path, name)["verdict"].upper()  # some reports write "pass"
```

`recorded(path, name)` returns only the verdict, in capital letters.

```python
say("The gammas, C and the two report helpers are ready.")
```

The cell prints `The gammas, C and the two report helpers are ready.`

**In [3], the geometry at one point.**

```python
def frame_factors(a4, b4, z):
    """The eight factors f_a of the diagonal vielbein, in the order x0, ..., x7."""
    block = np.exp(-a4) * np.sqrt(b4)  # e^(-a4) b4^(1/2)
    extra = block * np.abs(np.sin(z)) ** (1 / 6)  # times (sin^2 z)^(1/12)
    return np.array([block / np.tan(z)] + [np.exp(a4)] * 3 + [1.0] + [extra] * 3)
```

`frame_factors(a4, b4, z)` returns the eight vielbein factors of the corrected metric, in the order $x_0, \dots, x_7$: $s_b\cot z$ (computed as `block / np.tan(z)`), $e^{a_4}$ three times, 1, and $s_bW$ three times, with $s_b = e^{-a_4}b_4^{1/2}$ (`block`) and $W = |\sin z|^{1/6}$.

```python
def spin_connection(a4, a4p, b4, u, z, H):
    """The eight matrices Omega_mu (record formula Omega_components), u = b4'/b4."""
    s_b = np.exp(-a4) * np.sqrt(b4)  # e^(-a4) b4^(1/2)
    h4 = u / 2 - a4p  # the rate of the block of x0 and the extra times
    root = np.abs(np.sin(z)) ** (1 / 6)  # (sin^2 z)^(1/12)
    omega = [np.zeros((16, 16)) for _ in range(8)]  # Omega_x4 stays 0
    omega[0] = 0.5 * h4 * s_b / np.tan(z) * g0 @ g4
    for i in range(1, 4):  # the three 3-space directions x1, x2, x3
        omega[i] = 0.5 * a4p * np.exp(a4) * gamma[i] @ g4
    for t in range(5, 8):  # the three extra times x5, x6, x7
        omega[t] = 0.5 * root * (h4 * s_b * g4 @ gamma[t] + H * g0 @ gamma[t])
    return omega
```

`spin_connection(a4, a4p, b4, u, z, H)` returns the eight matrices $\Omega_\mu$ of the record's formula `Omega_components`, as in Notebook 09a (Section 9.17, In [5]), but with $u = b_4'/b_4$ as an argument instead of $b_4'$, so that $h_4 = \frac{u}{2} - a_4'$, and with $H$ as an argument, because this notebook uses two values of $H$.

```python
say("frame_factors and spin_connection are defined.")
```

It prints `frame_factors and spin_connection are defined.`

**In [4], the tensor at a point.**

```python
def bar(vector):
    """The Dirac adjoint vector^dagger C."""
    return vector.conj() @ C
```

`bar` returns the Dirac adjoint $\bar\Phi = \Phi^\dagger C$ of a column.

```python
def energy_momentum(phi, dphi, m, lam, a4, a4p, b4, u, z, H):
    """The 64 entries T[nu, mu] = T^nu_mu at one point (real parts)."""
    f = frame_factors(a4, b4, z)
    g_values = eta * f ** 2  # g_mumu
    omega = spin_connection(a4, a4p, b4, u, z, H)
    gup = [gamma[mu] / f[mu] for mu in range(8)]  # gamma^mu
    S = (bar(phi) @ phi).real
    D = [dphi[mu] + omega[mu] @ phi for mu in range(8)]  # D_mu Phi
    Dbar = [bar(dphi[mu]) - bar(phi) @ omega[mu] for mu in range(8)]  # D_mu Phibar
    L0 = 0.5 * sum(bar(phi) @ gup[mu] @ D[mu] - Dbar[mu] @ gup[mu] @ phi
                   for mu in range(8)) - m * S - lam / 2 * S ** 2
```

`energy_momentum(phi, dphi, m, lam, a4, a4p, b4, u, z, H)` computes the tensor of Section 9.6 from the jet at one point, like the function of Notebook 09a, but it builds the geometry itself from the point: the factors, $g_{\mu\mu}$, the spin connection and the coordinate gammas $\gamma^\mu$; then $S$, the columns $D_\mu\Phi$, the rows $D_\mu\bar\Phi$ and $L_0$ with $U = \frac{\lambda}{2}S^2$.

```python
    T = np.zeros((8, 8), dtype=complex)
    for nu in range(8):
        for mu in range(8):
            bracket = (bar(phi) @ gup[nu] @ D[mu] - Dbar[mu] @ gup[nu] @ phi
                       + g_values[mu] / g_values[nu]  # gamma_mu D^nu
                       * (bar(phi) @ gup[mu] @ D[nu] - Dbar[nu] @ gup[mu] @ phi))
            T[nu, mu] = (nu == mu) * L0 - bracket / 4
```

The 64 entries. Here the second pair of the bracket is written with the upper gammas: $\bar\Phi\gamma_\mu D^\nu\Phi = \frac{g_{\mu\mu}}{g_{\nu\nu}}\bar\Phi\gamma^\mu D_\nu\Phi$, because $\gamma_\mu = g_{\mu\mu}\gamma^\mu$ and $D^\nu = D_\nu/g_{\nu\nu}$ (the comment marks the factor).

```python
    if np.abs(T.imag).max() > 1e-9 * max(1.0, np.abs(T).max()):
        raise ValueError("the tensor is not real")  # it must be real
    return T.real
```

The tensor of a configuration of the commuting field is real (Section 9.6); if an imaginary part were larger than rounding noise ($10^{-9}$ of the largest entry, or of 1), `raise ValueError` would stop the notebook. The function returns the real parts.

```python
say("bar and energy_momentum are defined.")
```

It prints `bar and energy_momentum are defined.`

**In [5], the tensor of a generic condensate.**

```python
V, H = 5.0, 1.0  # effective mass (m = 5, lambda = 0) and the author's constant
POINT = {"a4": 0.5, "a4p": 0.25, "b4": np.exp(2 / 3), "u": 1 / 3,
         "z": np.pi / 4}  # a point of the deflating history (u = b4'/b4)
rng = np.random.default_rng(11)  # a fixed seed
chi = rng.normal(size=16) + 1j * rng.normal(size=16)
chi /= np.linalg.norm(chi)  # length 1
```

The effective mass $V = 5$ (with $m = 5$ and $\lambda = 0$, so $V = m$ exactly), $H = 1$, the point of the deflating history in a dictionary (`POINT`: $a_4 = 0.5$, $a_4' = 0.25$, $b_4 = e^{2/3}$, $u = \frac13$, $z = \pi/4$; it is the history $a_4 = AHx_4$, $b_4 = e^{(4/3)AHx_4}$ with $A = 0.25$ at $x_4 = 2$, because $H = 1$ here), and a random complex column of length 1 drawn with the seed 11.

```python
def condensate_tensor(column, a4, a4p, b4, u, z, V_value=V, H_value=H):
    """T of the condensate (lambda = 0, m = V_value) whose jet at the point is
    Phi = column, d4 Phi = (A - v_g) column, A = -V gamma^(x4) + c_g g^(x4) g^(x0)."""
    c_g = 1.5 * H_value * np.exp(a4) / np.sqrt(b4)  # (3/2) H e^a4 b4^(-1/2)
    v_g = u - a4p / 2  # b4'/b4 - a4'/2
    A_value = -V_value * g4 + c_g * g4 @ g0
    dphi = np.zeros((8, 16), dtype=complex)
    dphi[4] = A_value @ column - v_g * column  # the only nonzero derivative
    return energy_momentum(column, dphi, V_value, 0.0, a4, a4p, b4, u, z, H_value)
```

`condensate_tensor(column, a4, a4p, b4, u, z, V_value, H_value)` returns the tensor of the condensate whose jet at the point is $\Phi$ = the column and $\partial_4\Phi = (A - v_g)\Phi$ (Section 9.26: $\partial_4\Phi = (M - v_g)\Phi$; this notebook calls the matrix $A$), with $c_g = \frac32He^{a_4}b_4^{-1/2}$, $v_g = u - \frac{a_4'}{2}$ and $A = -V\gamma^{(4)} + c_g\gamma^{(4)}\gamma^{(0)}$; all other derivatives are zero. The last two arguments have the default values $V$ and $H$ (`V_value=V`), used when they are not given. Any other column with the same $S$ belongs to the same condensate at another time, so one column is enough.

```python
def off_diagonal_pairs(T):
    """The ordered pairs (nu, mu), nu != mu, whose entry is not zero."""
    tolerance = 1e-10 * max(1.0, np.abs(T).max())
    return [(nu, mu) for nu in range(8) for mu in range(8)
            if nu != mu and abs(T[nu, mu]) > tolerance]
```

`off_diagonal_pairs(T)` lists the ordered pairs $(\nu, \mu)$ with $\nu \neq \mu$ whose entry is larger in size than $10^{-10}$ times the largest entry (or than $10^{-10}$, if all entries are smaller than 1): these are the nonzero off-diagonal entries.

```python
T_generic = condensate_tensor(chi, **POINT)
S_chi = (bar(chi) @ chi).real
expected_diagonal = np.zeros(8)
expected_diagonal[4] = -V * S_chi
A4_WL = "Revision/field_equations_a4/reports/wolfram-a4-report.json"
A4_PY = "Revision/field_equations_a4/reports/python-a4-report.json"
check(np.abs(np.diag(T_generic) - expected_diagonal).max() < 1e-12
      and abs(T_generic[4, 0]) < 1e-12 and abs(T_generic[0, 4]) < 1e-12
      and recorded(A4_WL, "condensate_kinetic_tensor_diagonal") == "PASS"
      and recorded(A4_PY, "authorT16_condensate_kinetic_diagonal") == "PASS",
      "diagonal (0, 0, 0, 0, -V S, 0, 0, 0) and T^x4_x0 = T^x0_x4 = 0",
      record=f"{A4_WL}, check condensate_kinetic_tensor_diagonal; {A4_PY}, check "
             "authorT16_condensate_kinetic_diagonal")
```

The tensor of the generic condensate and $S$ of the column. For $\lambda = 0$ on shell $L_0 = SU' - U = 0$, so the record's diagonal (Section 9.26) is $(0, 0, 0, 0, -VS, 0, 0, 0)$. The check compares the diagonal with it, asks $T^{x_4}{}_{x_0} = T^{x_0}{}_{x_4} = 0$, and asks both field-equations reports (`condensate_kinetic_tensor_diagonal`, `authorT16_condensate_kinetic_diagonal`).

```python
pairs = off_diagonal_pairs(T_generic)
SPACE, EXTRA = (1, 2, 3), (5, 6, 7)  # x1, x2, x3 and x5, x6, x7
groups_of_record = ([(0, i) for i in SPACE] + [(i, 4) for i in SPACE]
                    + [(i, t) for i in SPACE for t in EXTRA] + [(4, t) for t in EXTRA])
expected_pairs = sorted(groups_of_record + [(b, a) for a, b in groups_of_record])
beyond_fold = off_diagonal_pairs(condensate_tensor(chi, **dict(POINT, z=2.0)))
check(sorted(pairs) == expected_pairs and sorted(beyond_fold) == expected_pairs,
      "36 nonzero off-diagonal entries: x0-xi, xi-x4, xi-xt, x4-xt (also at z = 2)")
```

`pairs` are the nonzero off-diagonal entries found. `groups_of_record` lists the 18 unordered pairs of Section 9.26 ($x_0$-$x_i$, $x_i$-$x_4$, $x_i$-$x_t$, $x_4$-$x_t$), and `expected_pairs` adds the reversed pairs: 36 ordered pairs. The check asks that the nonzero entries are exactly these, at the point and also at $z = 2.0$, beyond the fold (`dict(POINT, z=2.0)` is a copy of the point with another $z$; `**` hands a dictionary to a function as named arguments).

```python
hidden_space = sorted([(0, i) for i in SPACE] + [(i, 0) for i in SPACE])
pairs_equal_rates = off_diagonal_pairs(condensate_tensor(
    chi, POINT["a4"], POINT["u"] / 4, POINT["b4"], POINT["u"], POINT["z"]))
pairs_still = off_diagonal_pairs(condensate_tensor(
    chi, POINT["a4"], 0.0, POINT["b4"], 0.0, POINT["z"]))
check(sorted(set(pairs) - set(pairs_equal_rates)) == hidden_space
      and sorted(pairs_still) == sorted(pairs_equal_rates)
      and len(pairs_equal_rates) == 30,
      "with 4 a4' = b4'/b4, or with a4' = b4' = 0, the six x0-xi entries vanish")
```

The six entries between 3-space and the hidden direction contain $4a_4' - b_4'/b_4$ (Section 9.26). The check computes the nonzero entries again at a moment with $a_4' = \frac{u}{4}$ (so $4a_4' = b_4'/b_4$) and at a moment with $a_4' = 0$ and $u = 0$ (a static moment): in both cases exactly these six disappear (`set(pairs) - set(pairs_equal_rates)` is the set of the pairs that are lost), and 30 remain.

```python
report("S of the random column", f"{S_chi:.6f}")
report("T^x4_x4 = -V S", f"{T_generic[4, 4]:.6f}")
off_part = T_generic - np.diag(np.diag(T_generic))  # the 56 off-diagonal entries
report("largest off-diagonal entry in size", f"{np.abs(off_part).max():.6f}")
```

Three RESULT lines: `S of the random column = 0.293667`, `T^x4_x4 = -V S = -1.468334` (that is $-5\cdot 0.293667$), and `largest off-diagonal entry in size = 0.691254` (`np.diag(np.diag(T))` is the diagonal part of the table, so `off_part` keeps only the 56 entries off the diagonal).

**In [6], the heat map of the generic condensate.**

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
```

`heat_map(ax, T, title, largest)` draws a table as coloured squares, as in Notebook 09a, with two decimals in each square; a tiny negative number that would be printed as `-0.00` is printed as `0.00`.

```python
    ticks = [f"${n[0]}_{n[1]}$" for n in NAMES]
    ax.set_xticks(range(8), ticks)
    ax.set_yticks(range(8), ticks)
    ax.set_xlabel("lower index $\\mu$ (column)")
    ax.set_ylabel("upper index $\\nu$ (row)")
    ax.set_title(title)
    ax.grid(False)
    return picture
```

Tick labels $x_0, \dots, x_7$, axis labels, the title, no grid; the function returns the picture, which the colour bar needs.

```python
SCALE = 2.0  # the colour scale runs from -2 to 2 in both heat maps of this notebook
fig, ax = plt.subplots(figsize=(6.6, 5.6))
picture = heat_map(ax, T_generic, "Generic condensate: $T^\\nu{}_\\mu$", SCALE)
fig.colorbar(picture, ax=ax, label="value (energy per unit volume)", extend="both")
```

Both heat maps of this notebook use the colour scale from $-2$ to $2$ (`SCALE`), so that they can be compared; `extend="both"` gives the colour bar pointed ends, which mark that larger values get the darkest colours.

```python
save_figure(fig, "generic_condensate",
            "Heat map of the 64 entries $T^\\nu{}_\\mu$ (row $\\nu$, column $\\mu$, "
...)
```

The figure is saved as Figure 09c.1 (`09c_1_generic_condensate.png`). The student sees $-VS = -1.47$ alone on the diagonal and 36 coloured squares off it, in the rows and columns that pair 3-space with $x_0$, with $x_4$ and with the extra times, and $x_4$ with the extra times; the squares $(x_4, x_0)$, $(x_0, x_t)$ and those inside 3-space and inside the extra times are white (zero).

**In [7], how four entries depend on the rate a4'.**

```python
rates = np.linspace(-1.0, 1.0, 41)  # values of a4p
zero_rate = POINT["u"] / 4  # 4 a4p - u vanishes here: 1/12
entries = np.array([[T[4, 1], T[4, 7], T[1, 0], T[1, 7]] for T in (
    condensate_tensor(chi, POINT["a4"], rate, POINT["b4"], POINT["u"], POINT["z"])
    for rate in rates)])
middle = 20  # rates[20] = 0
```

41 values of $a_4'$ from $-1$ to 1; `zero_rate` is $\frac{u}{4} = \frac{1}{12}$, where $4a_4' - u$ vanishes; for each rate the tensor of the same condensate is computed at the same point (with $b_4'/b_4 = \frac13$ kept), and four entries are kept: $T^{x_4}{}_{x_1}$, $T^{x_4}{}_{x_7}$, $T^{x_1}{}_{x_0}$ and $T^{x_1}{}_{x_7}$. `middle = 20` is the index of the rate 0.

```python
check(np.abs(entries[:, :2] - entries[middle, :2]).max() < 1e-12
      and np.abs(entries[middle, :2]).min() > 0.01,
      "T^x4_x1 and T^x4_x7 do not depend on a4p and are not zero")
```

The two momentum flows must not change with $a_4'$ and must not be zero (Section 9.26: $T^{x_4}{}_{x_1} = \frac34He^{2a_4}b_4^{-1/2}B(x_0\,x_1\,x_4)$ contains only $H$; the flows along the extra times come from $c_g$ and from the part $H\gamma^{(0)}\gamma^{(t)}$ of $\Omega_{x_t}$).

```python
slope_hidden = entries[-1, 2] / (rates[-1] - zero_rate)
slope_extra = (entries[-1, 3] - entries[0, 3]) / (rates[-1] - rates[0])
at_zero_rate = entries[0, 3] + slope_extra * (zero_rate - rates[0])  # the H part
check(np.abs(entries[:, 2] - slope_hidden * (rates - zero_rate)).max() < 1e-12
      and np.abs(entries[:, 3] - at_zero_rate
                 - slope_extra * (rates - zero_rate)).max() < 1e-12
      and min(abs(slope_hidden), abs(slope_extra), abs(at_zero_rate)) > 1e-3,
      "T^x1_x0 is proportional to 4 a4p - b4'/b4, T^x1_x7 is linear in a4p")
```

`slope_hidden` is the slope of $T^{x_1}{}_{x_0}$ if it is proportional to $a_4' - \frac{1}{12}$; `slope_extra` is the slope of the straight line through the end values of $T^{x_1}{}_{x_7}$, and `at_zero_rate` its value at $a_4' = \frac{1}{12}$ (its part from $H$). The check: $T^{x_1}{}_{x_0}$ equals `slope_hidden` times $(a_4' - \frac{1}{12})$ at all 41 rates, $T^{x_1}{}_{x_7}$ lies on its straight line, and the three numbers are not small.

```python
report("T^x4_x1 and T^x4_x7", f"{entries[middle, 0]:.6f} and {entries[middle, 1]:.6f}")
report("slope of T^x1_x0, slope of T^x1_x7, T^x1_x7 at a4p = 1/12",
       f"{slope_hidden:.6f}, {slope_extra:.6f}, {at_zero_rate:.6f}")
```

The printed values: `T^x4_x1 and T^x4_x7 = 0.448182 and -0.441267`, and `slope of T^x1_x0, slope of T^x1_x7, T^x1_x7 at a4p = 1/12 = -0.078760, 0.035754, -0.079234`. The first slope can be checked with the formula of Section 9.26: the slope of $-\frac18e^{-2a_4}b_4^{1/2}\cot z\,(4a_4' - u)\,B$ is $-\frac12e^{-2a_4}b_4^{1/2}\cot z\,B = -\frac12e^{-2/3}B$, and with $B = B(x_0\,x_1\,x_4) = 0.448182/1.460801 = 0.306806$ (from $T^{x_4}{}_{x_1} = 1.460801\,B$) this is $-0.5\cdot 0.513417\cdot 0.306806 = -0.078760$.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(9.6, 3.9))
fig.subplots_adjust(wspace=0.35)
left.plot(rates, entries[:, 0], label="$T^{x_4}{}_{x_1}$ (momentum flow)")
left.plot(rates, entries[:, 1], "--", label="$T^{x_4}{}_{x_7}$ (momentum flow)")
left.axhline(0.0, color="black", linewidth=0.8)
left.set_xlabel("rate $a_4'$ (with $b_4'/b_4 = 1/3$)")
left.set_ylabel("entry (energy per unit volume)")
left.set_title("Come from $H$: independent of $a_4'$")
left.legend(fontsize=8)
```

Two panels; the left one draws the two momentum flows against $a_4'$, with a line at zero.

```python
right.plot(rates, entries[:, 2], label="$T^{x_1}{}_{x_0}$")
right.plot(rates, entries[:, 3], "--", label="$T^{x_1}{}_{x_7}$")
right.axhline(0.0, color="black", linewidth=0.8)
right.axvline(zero_rate, color="gray", linestyle=":", linewidth=0.9)
right.set_xlabel("rate $a_4'$ (with $b_4'/b_4 = 1/3$)")
right.set_title("Contain $4a_4' - b_4'/b_4$")
right.legend(fontsize=8)
```

The right panel draws $T^{x_1}{}_{x_0}$ and $T^{x_1}{}_{x_7}$ with a dotted vertical line at $a_4' = \frac{1}{12}$.

```python
save_figure(fig, "offdiagonal_entries",
            "Four off-diagonal entries of the generic condensate of the previous "
...)
```

The figure is saved as Figure 09c.2 (`09c_2_offdiagonal_entries.png`): two horizontal lines on the left; on the right two straight lines, of which the solid one passes through zero at the dotted line and the dashed one does not.

**In [8], each entry is a combination of its bilinears.**

```python
def bilinear_sets(nu, mu):
    """The direction triples (a, b, c) of the bilinears that carry T^nu_mu."""
    low, high = sorted((nu, mu))
    if low == 0:  # x0-xi
        return [(0, high, 4)]
    if high == 4:  # xi-x4
        return [(0, low, 4)]
    if low == 4:  # x4-xt
        return [(0, 4, high)]
    return [(0, low, high), (low, 4, high)]  # xi-xt: two bilinears
```

`bilinear_sets(nu, mu)` returns the direction triples of the bilinears that carry the entry $T^\nu{}_\mu$ (Section 9.26): `sorted` puts the two indices in increasing order; a pair with $x_0$ carries $B(x_0\,x_i\,x_4)$, a pair $x_i$-$x_4$ the same bilinear, a pair $x_4$-$x_t$ the bilinear $B(x_0\,x_4\,x_t)$, and a pair $x_i$-$x_t$ the two bilinears $B(x_0\,x_i\,x_t)$ and $B(x_i\,x_4\,x_t)$.

```python
def bilinear(column, directions):
    """B(a b c) = Phibar gamma^(a) gamma^(b) gamma^(c) Phi."""
    a, b, c = directions
    return bar(column) @ gamma[a] @ gamma[b] @ gamma[c] @ column
```

`bilinear(column, directions)` computes $B(a\,b\,c) = \bar\Phi\gamma^{(a)}\gamma^{(b)}\gamma^{(c)}\Phi$ for a column.

```python
columns = [rng.normal(size=16) + 1j * rng.normal(size=16) for _ in range(4)]
tensors = [condensate_tensor(column, **POINT) for column in columns]
worst_residual, used = 0.0, set()
```

Four more random columns and their tensors at the point; `used` collects the triples that occur (a `set` keeps each triple once).

```python
for nu, mu in pairs:
    sets = bilinear_sets(nu, mu)
    used.update(sets)
    # one row per column: the bilinears of the entry, and the entry itself
    matrix = np.array([[bilinear(column, d) for d in sets] for column in columns])
    values = np.array([T[nu, mu] for T in tensors])
    numbers = np.linalg.lstsq(matrix, values, rcond=None)[0]  # least squares
    residual = np.abs(matrix @ numbers - values).max() / np.abs(values).max()
    worst_residual = max(worst_residual, residual)
```

For each of the 36 nonzero entries: a small table with one row per column, holding the values of the entry's one or two bilinears, and the values of the entry itself. `np.linalg.lstsq` finds the numbers $c_1$ (and $c_2$) for which $c_1B_1 + c_2B_2$ comes closest to the entry for all four columns at once (least squares); if the entry is such a combination with numbers that do not depend on the column, the remaining difference is zero. The relative residual updates `worst_residual`.

```python
check(worst_residual < 1e-9 and len(used) == 24
      and recorded(A4_WL, "condensate_offdiagonal_are_three_gamma_bilinears") == "PASS"
      and recorded(A4_PY, "authorT16_condensate_offdiagonal_three_gamma") == "PASS",
      "each of the 36 entries is a fixed combination of its bilinears (24 in all)",
      record=f"{A4_WL}, check condensate_offdiagonal_are_three_gamma_bilinears; "
             f"{A4_PY}, check authorT16_condensate_offdiagonal_three_gamma")
```

The check: every residual below $10^{-9}$, 24 triples in all, and the verdicts of both reports (`condensate_offdiagonal_are_three_gamma_bilinears`, `authorT16_condensate_offdiagonal_three_gamma`).

```python
for directions in sorted(used):
    say("bilinear B(" + " ".join(NAMES[d] for d in directions) + ")")
```

The 24 bilinears are printed one per line, sorted by their three indices: first the twelve with $x_0$ and a 3-space direction ($B(x_0\,x_i\,x_4)$ and $B(x_0\,x_i\,x_t)$; for each $i$ the third index runs through $x_4, x_5, x_6, x_7$), then the three $B(x_0\,x_4\,x_t)$ and the nine $B(x_i\,x_4\,x_t)$, from `bilinear B(x0 x1 x4)` to `bilinear B(x3 x4 x7)`.

**In [9], the coefficients of the record.**

```python
import re  # regular expressions: patterns that find pieces of a text

import sympy as sp  # exact algebra with symbols
```

`re` is Python's module for **regular expressions**, patterns that find pieces of a text; `sympy` reads the record's formulas.

```python
A4_RECORD = "Revision/field_equations_a4/a4-equations.json"
record_entries = json.loads(repository_file(A4_RECORD).read_text(encoding="utf-8"))[
    "fields"]["dirac16complex00"]["offDiagonalKinetic"]
a4v, ad1, uu, H_symbol, sv, cv, ww = sp.symbols("a4v ad1 uu H sv cv ww", real=True)
bb = sp.Symbol("bb", positive=True)  # b4
AT_POINT = {a4v: POINT["a4"], ad1: POINT["a4p"], bb: POINT["b4"], uu: POINT["u"],
            H_symbol: H, sv: np.sin(POINT["z"]), cv: np.cos(POINT["z"]),
            ww: np.abs(np.sin(POINT["z"])) ** (1 / 6)}
NAMES_RECORD = {"E": sp.E, "a4v": a4v, "ad1": ad1, "bb": bb, "uu": uu, "H": H_symbol,
                "sv": sv, "cv": cv, "ww": ww, "sqrt": sp.sqrt}
```

The record's 36 entries `offDiagonalKinetic` of the commuting field are read. The plain symbols carry the record's names (`a4v` $= a_4$, `ad1` $= a_4'$, `bb` $= b_4$, `uu` $= u$, `H`, `sv` $= \sin z$, `cv` $= \cos z$, `ww` $= W$); `AT_POINT` gives each its value at the point, and `NAMES_RECORD` tells sympy what the names in the texts mean (`sqrt` is the square root).

```python
worst_coefficient, groups, record_pairs = 0.0, {}, []
for item in record_entries:
    # "K^x1_x4 (symmetrised)": upper index x1 (row nu), lower index x4 (column mu)
    nu, mu = [int(digit) for digit in re.findall(r"x(\d)", item["component"])]
    record_pairs.append((nu, mu))
    predicted = np.zeros(5, dtype=complex)  # for the generic and the four columns
    for term in item["terms"]:  # one or two terms
        directions = tuple(int(d) for d in re.findall(r"x(\d)", term["bilinear"]))
        formula = term["coefficient"]["input"]  # the Wolfram Language text
        text = formula.replace("E^", "E**").replace("^", "**")
        text = text.replace("Sqrt[", "sqrt(").replace("]", ")")  # Sqrt[bb] -> sqrt(bb)
        coefficient = float(sp.sympify(text, locals=NAMES_RECORD).subs(AT_POINT))
        predicted -= coefficient * np.array([bilinear(column, directions)
                                             for column in [chi] + columns])
        groups.setdefault(formula, (nu, mu, directions, coefficient))
    for n, T in enumerate([T_generic] + tensors):
        worst_coefficient = max(worst_coefficient, abs(T[nu, mu] - predicted[n]))
```

For each entry of the record: the two digits after the letters `x` in its name (such as `K^x1_x4 (symmetrised)`) give the row $\nu$ and the column $\mu$ (`re.findall(r"x(\d)", ...)` finds every digit that follows an `x`); for each of its one or two terms the bilinear's three directions are read the same way, its coefficient is translated from the Wolfram Language (`E^` becomes `E**`, `^` becomes `**`, `Sqrt[bb]` becomes `sqrt(bb)`), evaluated at the point, and minus the coefficient times the bilinear is added to the prediction for the five columns (the generic one and the four of In [8]), because off the diagonal $T = -K^{(\nu}{}_{\mu)}$. `groups` keeps the first entry of each different coefficient text. Then the five tensors are compared with the predictions.

```python
check(len(record_entries) == 36 and sorted(record_pairs) == sorted(pairs)
      and len(groups) == 10 and worst_coefficient < 1e-12
      and recorded(A4_PY, "json_offdiagonal_coefficients") == "PASS"
      and recorded(A4_PY, "offdiagonal_coefficients_representation_independent")
      == "PASS",
      "all 36 entries are -(record coefficients) x bilinears, for 5 columns",
      record=f"{A4_RECORD}, offDiagonalKinetic; {A4_PY}, checks "
             "json_offdiagonal_coefficients and "
             "offdiagonal_coefficients_representation_independent")
```

The check: 36 entries, at exactly the 36 pairs found in In [5], 10 different coefficient formulas, agreement to $10^{-12}$ for all five columns, and the verdicts of the record's checks `json_offdiagonal_coefficients` and `offdiagonal_coefficients_representation_independent`.

```python
for nu, mu, directions, coefficient in groups.values():
    say(f"K^{NAMES[nu]}_{NAMES[mu]}: coefficient {coefficient:+.6f} of B("
        + " ".join(NAMES[d] for d in directions) + ")")
```

One line for each of the ten groups:

```text
K^x0_x1: coefficient +0.162311 of B(x0 x1 x4)
K^x1_x0: coefficient +0.042785 of B(x0 x1 x4)
K^x1_x4: coefficient +0.537398 of B(x0 x1 x4)
K^x1_x5: coefficient -0.143122 of B(x0 x1 x5)
K^x1_x5: coefficient -0.040383 of B(x1 x4 x5)
K^x4_x1: coefficient -1.460801 of B(x0 x1 x4)
K^x4_x5: coefficient -0.943874 of B(x0 x4 x5)
K^x5_x1: coefficient +0.609450 of B(x0 x1 x5)
K^x5_x1: coefficient +0.171963 of B(x1 x4 x5)
K^x5_x4: coefficient -1.478600 of B(x0 x4 x5)
```

The second is the value $\frac{1}{12}e^{-2/3}$ derived in Section 9.26, the third is $\frac34e^{-1/3}$, the sixth $-\frac34e^{2/3}$ (Section 9.26) and the seventh $-HW = -2^{-1/12}$. The other 26 entries repeat these coefficients with other directions $x_i$ and $x_t$.

**In [10], the witnesses and the dimensions of their construction.**

```python
import itertools  # all combinations and all sign choices of a list

P = [gamma[i] @ gamma[i + 4] for i in range(1, 4)]  # gamma^(x1) gamma^(x5), ...
```

`itertools` provides all combinations and sign choices of a list. `P` holds $P_1 = \gamma^{(1)}\gamma^{(5)}$, $P_2 = \gamma^{(2)}\gamma^{(6)}$, $P_3 = \gamma^{(3)}\gamma^{(7)}$.

```python
def witness(V_w, H_w, k0):
    """The frequency omega (here freq), A, the unit vectors v1, v2 and the column
    Phi0 of the record's diagonal witness for (V_w, H_w) on a history with k = k0."""
    c_w = 1.5 * H_w * np.sqrt(k0)  # c_g = (3/2) H sqrt(k0), a constant
    A_w = -V_w * g4 + c_w * g4 @ g0  # d4 chi = A chi
    freq = np.sqrt(V_w ** 2 - c_w ** 2)  # the frequency omega
    # The null space of A + i omega: the rows of the third SVD factor whose
    # singular value is zero, complex conjugated and written as columns.
    _, singular, rows = np.linalg.svd(A_w + 1j * freq * I16)
    space = rows[singular < 1e-9].conj().T  # 16 x 8: the eigenspace for -i omega
```

`witness(V_w, H_w, k0)` builds the record's witness for one triple: $c_g = \frac32H\sqrt{k_0}$, the constant matrix $A = -V\gamma^{(4)} + c_g\gamma^{(4)}\gamma^{(0)}$ and $\omega = \sqrt{V^2 - c_g^2}$ (called `freq`). The space of the eigenvalue $-i\omega$ is the null space of $A + i\omega$ (the columns that this matrix sends to zero). `np.linalg.svd` (the **singular value decomposition**) writes a matrix as $U\,\mathrm{diag}(\sigma)\,W^\dagger$ with unitary $U$, $W$; the rows of $W^\dagger$ whose singular value $\sigma$ is zero, conjugated and written as columns, span the null space. `space` is a $16 \times 8$ array.

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

For each sign the projector $\frac18(1 \pm P_1)(1 \pm P_2)(1 \pm P_3)$ keeps the columns with $P_1 = P_2 = P_3 = \pm1$; applied to the eight columns of the space it leaves one direction (Step 3 of Section 9.26), and a second singular value decomposition gives it as a unit column; if there were more than one, the notebook would stop. Then $c = \overline{v_1^\dagger Cv_2}$ and $\Phi_0 = v_1 + cv_2$.

```python
WITNESSES = [(5.0, 1.0, 4.0), (5.0, 4 / 3, 4.0), (-5.0, 1.0, 4.0)]  # (V, H, k0)
witnesses = {triple: witness(*triple) for triple in WITNESSES}  # (V, H, k0) -> five
for (V_w, H_w, k0), found in witnesses.items():
    say(f"witness (V, H, k0) = ({V_w:g}, {H_w:.4g}, {k0:g}): frequency omega = "
        f"{found[0]:.6f}")
```

The three witnesses of the record, and one printed line each: `witness (V, H, k0) = (5, 1, 4): frequency omega = 4.000000`, `(5, 1.333, 4): ... 3.000000` and `(-5, 1, 4): ... 4.000000`.

```python
def product_of(indices):
    """The product gamma^(a) gamma^(b) ... of the frame gammas with these indices."""
    result = I16
    for index in indices:
        result = result @ gamma[index]
    return result
```

`product_of(indices)` multiplies the frame gammas with the given indices in order.

```python
subsets = [chosen for size in range(1, 9)
           for chosen in itertools.combinations(range(8), size)]  # 255 index sets
traceless = all(abs(np.trace(product_of(chosen))) < 1e-12 for chosen in subsets)
```

All $2^8 - 1 = 255$ products of 1 to 8 different gammas (`itertools.combinations(range(8), size)` lists every choice of `size` different indices in increasing order) must have trace 0 (Step 3).

```python
dimensions_hold = True
for (V_w, H_w, k0), (freq, A_w, v1, v2, phi0) in witnesses.items():
    # the dimension of the space of -i omega: 16 minus the rank of A + i omega
    dimension = 16 - np.linalg.matrix_rank(A_w + 1j * freq * I16, tol=1e-9)
    for signs in itertools.product((-1, 1), repeat=3):  # the eight sectors
        keeper = (I16 + 1j / freq * A_w) / 2  # keeps the space of -i omega
        for sign, P_k in zip(signs, P):
            keeper = keeper @ (I16 + sign * P_k) / 2  # keeps P_k = sign
        dimensions_hold = dimensions_hold and abs(np.trace(keeper) - 1) < 1e-12
    dimensions_hold = dimensions_hold and dimension == 8
```

For each witness: the dimension of the space of $-i\omega$ is 16 minus the rank of $A + i\omega$ (`matrix_rank` counts the independent columns), and for each of the eight sign choices (`itertools.product((-1, 1), repeat=3)`) the matrix $\frac12(1 + \frac{i}{\omega}A)\prod_k\frac12(1 \pm P_k)$ that keeps one sector must have trace 1.

```python
check(len(subsets) == 255 and traceless and dimensions_hold,
      "255 gamma products have trace 0; space of -i omega: dim 8; each sector: dim 1")
```

One PASS line for the three facts: 255 products of trace 0, dimension 8, and dimension 1 for every sector.

**In [11], the witnesses have a diagonal tensor.**

```python
grid = [(a4, a4p, z) for a4 in (-1.0, 0.0, 0.5) for a4p in (-0.5, 0.0, 0.25, 1.0)
        for z in (0.3, 1.3, 2.4)]  # 3 x 4 x 3 = 36 points
witness_columns = {}  # (V, H, k0) -> Phi0
unit_S = {}  # (V, H, k0) -> S of Phi0 built from v1 and v2 of length 1
```

The 36 points: three values of $a_4$, four of $a_4'$, three of $z$ (the last beyond the fold); two dictionaries for the columns and their $S$.

```python
for (V_w, H_w, k0), (freq, A_w, v1, v2, phi0) in witnesses.items():
    S_w = (bar(phi0) @ phi0).real
    largest_bilinear = max(abs(bilinear(phi0, d)) for d in used)
    worst_off = 0.0  # the largest off-diagonal entry at the 36 points
    for a4, a4p, z in grid:  # b4 = e^(2 a4)/k0 and b4'/b4 = 2 a4': k stays k0
        T = condensate_tensor(phi0, a4, a4p, np.exp(2 * a4) / k0, 2 * a4p, z,
                              V_w, H_w)
        worst_off = max(worst_off, np.abs(T - np.diag(np.diag(T))).max())
```

For each witness: $S$ of $\Phi_0$, the largest of its 24 bilinears in size, and the largest off-diagonal entry of its tensor at the 36 points, on the histories with $e^{2a_4}/b_4 = k_0$: there $b_4 = e^{2a_4}/k_0$ and $b_4'/b_4 = 2a_4'$. At each point the jet is $\Phi_0$ with $\partial_4\Phi = (A - v_g)\Phi_0 = (-i\omega - v_g)\Phi_0$.

```python
    check(np.abs(A_w @ phi0 + 1j * freq * phi0).max() < 1e-12
          and largest_bilinear < 1e-12 and abs(S_w) > 0.1 and worst_off < 1e-12,
          f"witness ({V_w:g}, {H_w:.4g}, {k0:g}): omega = {freq:g}, the 24 "
          "bilinears vanish, S != 0, T diagonal at 36 points")
```

The check for each witness: $A\Phi_0 = -i\omega\Phi_0$, all 24 bilinears vanish, $S \neq 0$, and the tensor is diagonal at all 36 points.

```python
    witness_columns[(V_w, H_w, k0)] = phi0
    unit_S[(V_w, H_w, k0)] = S_w
    report(f"witness ({V_w:g}, {H_w:.4g}, {k0:g}): omega, and S for unit v1, v2",
           f"{freq:g} and {S_w:.6f}")
```

The column and its $S$ are stored, and one RESULT line is printed per witness: `omega, and S for unit v1, v2 = 4 and 1.280000`, `3 and 0.720000`, `4 and 1.280000`.

**In [12], why S of a witness is never negative.**

```python
anticommute = all(np.abs(C @ P_k + P_k @ C).max() < 1e-12 for P_k in P)
symmetric = all(np.array_equal(P_k, P_k.T) for P_k in P)  # real: P^dagger = P^T
steps_hold, observation = True, True
```

$C$ anticommutes with each $P_k$, and each $P_k$ is symmetric (real, so its dagger is its transpose).

```python
for (V_w, H_w, k0), (freq, A_w, v1, v2, phi0) in witnesses.items():
    s = bar(v1) @ v2  # s = v1^dagger C v2
    S_unit = unit_S[(V_w, H_w, k0)]  # S of Phi0 with unit v1, v2 (previous cell)
    steps_hold = (steps_hold and abs(bar(v1) @ v1) < 1e-12
                  and abs(bar(v2) @ v2) < 1e-12
                  and abs(S_unit - 2 * abs(s) ** 2) < 1e-12)
    observation = observation and abs(S_unit - 2 * freq ** 2 / V_w ** 2) < 1e-12
```

For each witness the steps of Section 9.26 are checked with numbers: $v_1^\dagger Cv_1 = 0$, $v_2^\dagger Cv_2 = 0$ and $S = 2|v_1^\dagger Cv_2|^2$; and the observation $S = 2\omega^2/V^2$ ($2\cdot 16/25 = 1.28$ and $2\cdot 9/25 = 0.72$).

```python
check(anticommute and symmetric and steps_hold,
      "C P_k = -P_k C, P_k symmetric, v^dagger C v = 0, so S = 2 |v1^dagger C v2|^2")
check(observation,
      "observed: S = 2 omega^2 / V^2 for the three witnesses (unit v1, v2)")
```

Two PASS lines; the second is labelled "observed", because it is an observation for these three witnesses, not a proof.

**In [13], the numbers of the record.**

```python
detail = record_entry(A4_WL, "condensate_witness_constant_k_exact")["detail"]
# the frequencies, which the record writes "w = sqrt(M^2 - (9/4) H^2 k0) = {4, 3, 4}"
freq_text = re.search(r"k0\) = \{([^}]*)\}", detail).group(1)  # "4, 3, 4"
S_text = re.search(r"S = \{([^}]*)\}", detail).group(1)  # the three S values
record_freq = np.array([float(value) for value in freq_text.split(",")])
record_S = np.array([float(value) for value in S_text.split(",")])
our_freq = np.array([witnesses[triple][0] for triple in WITNESSES])
our_S = np.array([unit_S[triple] for triple in WITNESSES])
```

The detail text of the record's check `condensate_witness_constant_k_exact` contains the frequencies, written `w = sqrt(M^2 - (9/4) H^2 k0) = {4, 3, 4}`, and the values `S = {...}`. `re.search` finds the first place where a pattern matches: `\{([^}]*)\}` matches an opening brace, then any characters except a closing brace (kept as group 1), then the closing brace; a backslash makes a brace or a parenthesis an ordinary character. `.split(",")` cuts the text at the commas, and `float` turns each piece into a number.

```python
check(np.abs(our_freq - record_freq).max() < 1e-12
      and recorded(A4_WL, "condensate_witness_constant_k_exact") == "PASS"
      and recorded(A4_PY, "authorT16_condensate_witness") == "PASS",
      f"omega = {freq_text} for the three witnesses, as in the record",
      record=f"{A4_WL}, check condensate_witness_constant_k_exact; {A4_PY}, check "
             "authorT16_condensate_witness")
```

The frequencies must agree exactly, with the verdicts of both reports. The PASS line reads `omega = 4, 3, 4 for the three witnesses, as in the record`.

```python
quotients = record_S / our_S  # S of the record divided by S of unit v1, v2
check(np.abs(quotients / quotients[0] - 1).max() < 1e-9 and np.all(record_S > 0),
      f"S = {S_text} of the record are one common multiple of ours",
      record=f"{A4_WL}, check condensate_witness_constant_k_exact")
report("S of the record divided by S of unit v1, v2 (all three)",
       f"{quotients[0]:.1f}")
```

The three quotients of the record's $S$ by ours must be one and the same number, and the record's values positive. The PASS line reads `S = 51200, 28800, 51200 of the record are one common multiple of ours`, and the RESULT line `S of the record divided by S of unit v1, v2 (all three) = 40000.0`: the record's columns $v_1$, $v_2$ are not of length 1, and the common factor is the product of their squared lengths.

**In [14], the heat map of a witness.**

```python
WITNESS_POINT = {"a4": 0.5, "a4p": 0.25, "b4": np.exp(1.0) / 4, "u": 0.5,
                 "z": np.pi / 4}  # a point of a history with k = e^(2 a4)/b4 = 4
T_witness = condensate_tensor(witness_columns[(5.0, 1.0, 4.0)], **WITNESS_POINT)
```

A point of the history with $k_0 = 4$: $a_4 = 0.5$, $a_4' = 0.25$, $b_4 = e^{2a_4}/4 = e/4$, $b_4'/b_4 = 2a_4' = 0.5$, $z = \pi/4$; the tensor of the witness $(5, 1, 4)$ there.

```python
fig, ax = plt.subplots(figsize=(6.6, 5.6))
picture = heat_map(ax, T_witness, "Witness condensate: $T^\\nu{}_\\mu$", SCALE)
fig.colorbar(picture, ax=ax, label="value (energy per unit volume)", extend="both")
```

The heat map with the same colour scale as Figure 09c.1.

```python
save_figure(fig, "witness_condensate",
            "Heat map of the 64 entries $T^\\nu{}_\\mu$ of the exact witness "
...)
```

The figure is saved as Figure 09c.3 (`09c_3_witness_condensate.png`): one coloured square, $T^{x_4}{}_{x_4} = -VS = -5\cdot 1.28 = -6.4$ (beyond the colour scale, so in the darkest blue), and every other square white.

```python
check(len(off_diagonal_pairs(T_witness)) == 0 and abs(T_witness[4, 4]) > 0.1,
      "the drawn witness tensor is diagonal with T^x4_x4 = -V S != 0")
```

The check that the drawn tensor has no nonzero off-diagonal entry and a nonzero $T^{x_4}{}_{x_4}$.

**In [15], the Christoffel symbols for the conservation test.**

```python
x = sp.symbols("x0:8", real=True)  # sympy was imported in section 8
Hs = sp.symbols("H", positive=True)
a4_function = sp.Function("a4")(x[4])
b4_function = sp.Function("b4", positive=True)(x[4])
zs = 6 * Hs * x[0]
block = sp.exp(-2 * a4_function) * b4_function  # e^(-2 a4) b4
g = sp.diag(*([block * sp.cot(zs) ** 2] + [sp.exp(2 * a4_function)] * 3 + [-1]
              + [-block * sp.sin(zs) ** sp.Rational(1, 3)] * 3))  # sin z > 0
```

The corrected metric with symbols, for $\sin z > 0$ (then $(\sin^2 z)^{1/6} = \sin^{1/3}z$; the test points lie between $z = 0$ and $z = \pi$, on both sides of the fold).

```python
history = {  # a4(x4) and b4(x4) of the test
    a4_function: sp.Rational(3, 10) * x[4] + sp.Rational(1, 20) * x[4] ** 2,
    b4_function: sp.exp(sp.Rational(2, 5) * x[4] - sp.Rational(1, 50) * x[4] ** 2)}
```

The curved history of the test, $a_4 = 0.3x_4 + 0.05x_4^2$ and $b_4 = e^{0.4x_4 - 0.02x_4^2}$, written with exact fractions.

```python
christoffel = {}  # (l, i, j) with i <= j -> a numpy function of (x4, x0, H)
for l in range(8):
    for i in range(8):
        for j in range(i, 8):
            value = sp.simplify((sp.diff(g[l, j], x[i]) + sp.diff(g[l, i], x[j])
                                 - sp.diff(g[i, j], x[l])) / (2 * g[l, l]))
            if value != 0:  # put the history in, then make a numpy function
                christoffel[(l, i, j)] = sp.lambdify(
                    (x[4], x[0], Hs), value.subs(history).doit(), "numpy")
```

The 21 nonzero Christoffel symbols, computed as in Notebook 09a; the history is put in (`.subs(history)`, and `.doit()` carries out the derivatives that then appear), and `sp.lambdify` turns each symbol into a numpy function of $(x_4, x_0, H)$ that computes it quickly.

```python
check(len(christoffel) == 21, "21 nonzero Christoffel symbols (i <= j)")
```

One PASS line: 21 symbols.

**In [16], the condensates of the test and the divergence.**

```python
m9, lam9, H9 = 1.0, 0.5, 0.25  # the parameters of this section
chi9 = rng.normal(size=16) + 1j * rng.normal(size=16)
chi9 /= np.linalg.norm(chi9)  # the column chi at the time of a test point
S9 = (bar(chi9) @ chi9).real  # S0 = chi^dagger C chi, constant along chi
```

The parameters $m = 1$, $\lambda = 0.5$, $H = 0.25$, a random unit column $\chi$ (drawn with the generator of In [5], which continues its sequence), and $S_0 = \chi^\dagger C\chi$.

```python
def a4_of(x4):
    return 0.3 * x4 + 0.05 * x4 ** 2
```

$a_4(x_4) = 0.3x_4 + 0.05x_4^2$.

```python
def a4p_of(x4):
    return 0.3 + 0.1 * x4
```

Its derivative $a_4' = 0.3 + 0.1x_4$.

```python
def b4_of(x4):
    return np.exp(0.4 * x4 - 0.02 * x4 ** 2)
```

$b_4(x_4) = e^{0.4x_4 - 0.02x_4^2}$.

```python
def u_of(x4):
    return 0.4 - 0.04 * x4  # b4'/b4
```

$u = b_4'/b_4 = 0.4 - 0.04x_4$, the derivative of the exponent.

```python
def A_of(kind, x4):
    """A(x4) of the true condensate or of the control (no c_g g^(x4) g^(x0))."""
    V_now = m9 + lam9 * S9 * np.exp(a4_of(x4)) / b4_of(x4) ** 2  # m + lambda S
    A_now = -V_now * g4
    c_now = 1.5 * H9 * np.exp(a4_of(x4)) / np.sqrt(b4_of(x4))  # c_g at x4
    return A_now + c_now * g4 @ g0 if kind == "true" else A_now
```

`A_of(kind, x4)` returns the matrix of the condensate equation at the time $x_4$: with $V = m + \lambda S_0e^{a_4}b_4^{-2}$ and $c_g = \frac32He^{a_4}b_4^{-1/2}$ it is $-V\gamma^{(4)} + c_g\gamma^{(4)}\gamma^{(0)}$ for the true condensate and $-V\gamma^{(4)}$ for the control (`... if kind == "true" else ...` chooses one of two values).

```python
def flow(kind, column, x_from, x_to, count=50):
    """RK4 for chi' = A(x4) chi from x_from to x_to with count steps."""
    step = (x_to - x_from) / count
    x4, column = x_from, column.astype(complex)
    for _ in range(count):
        s1 = A_of(kind, x4) @ column
        s2 = A_of(kind, x4 + step / 2) @ (column + step / 2 * s1)
        s3 = A_of(kind, x4 + step / 2) @ (column + step / 2 * s2)
        s4 = A_of(kind, x4 + step) @ (column + step * s3)
        column = column + step / 6 * (s1 + 2 * s2 + 2 * s3 + s4)
        x4 += step
    return column
```

`flow(kind, column, x_from, x_to, count)` carries the column from one time to another with 50 RK4 steps, as in Notebook 09b; the step may be negative (towards earlier times).

```python
def condensate(kind, x4_base):
    """field(x4) -> (Phi, dPhi/dx4) of the condensate with chi(x4_base) = chi9."""
    def field(x4):
        column = chi9 if x4 == x4_base else flow(kind, chi9, x4_base, x4)
        factor = np.exp(a4_of(x4) / 2) / b4_of(x4)  # F = e^(a4/2) b4^(-1)
        v_g = u_of(x4) - a4p_of(x4) / 2  # b4'/b4 - a4'/2
        return factor * column, factor * (A_of(kind, x4) @ column - v_g * column)
    return field
```

`condensate(kind, x4_base)` returns a function `field(x4)` that gives $\Phi$ and $\partial_4\Phi$ at any time: the column is $\chi$ at the base time and is carried by `flow` to other times; then $\Phi = F\chi$ and $\partial_4\Phi = F(A\chi - v_g\chi)$ with $F = e^{a_4/2}b_4^{-1}$ and $v_g = u - \frac{a_4'}{2}$. Only the times $x_4$ and $x_4 \pm h$ near the base time are ever asked for, so each call of `flow` covers a short distance.

```python
def tensor_at(field, x4, x0):
    phi, d4 = field(x4)
    dphi = np.zeros((8, 16), dtype=complex)
    dphi[4] = d4
    return energy_momentum(phi, dphi, m9, lam9, a4_of(x4), a4p_of(x4),
                           b4_of(x4), u_of(x4), 6 * H9 * x0, H9)
```

`tensor_at(field, x4, x0)` computes the 64 entries at a point of the history: the jet has only the time derivative, and the point's $a_4$, $a_4'$, $b_4$, $u$ and $z = 6Hx_0$ are handed to `energy_momentum`.

```python
def divergence(field, x4, x0, h):
    """The eight components of nabla_mu T^mu_nu, with central differences of step h,
    and the size of the tensor (its largest entry)."""
    T = tensor_at(field, x4, x0)
    d4T = (tensor_at(field, x4 + h, x0) - tensor_at(field, x4 - h, x0)) / (2 * h)
    d0T = (tensor_at(field, x4, x0 + h) - tensor_at(field, x4, x0 - h)) / (2 * h)
    G = np.zeros((8, 8, 8))  # G[l, i, j] = Gamma^l_ij
    for (l, i, j), function in christoffel.items():
        G[l, i, j] = G[l, j, i] = function(x4, x0, H9)
    result = np.zeros(8)
    for nu in range(8):
        result[nu] = (d4T[4, nu] + d0T[0, nu]  # d_mu T^mu_nu (only x4 and x0)
                      + np.einsum("mml,l->", G, T[:, nu])  # Gamma^mu_mu l T^l_nu
                      - np.einsum("lm,ml->", G[:, :, nu], T))  # Gamma^l_mu nu T^mu_l
    return result, np.abs(T).max()
```

`divergence(field, x4, x0, h)` computes the eight components of $\nabla_\mu T^\mu{}_\nu$ (Section 9.9) with the derivatives replaced by central finite differences of step $h$, $\partial_4T \approx (T(x_4 + h) - T(x_4 - h))/(2h)$ and the same in $x_0$ (the tensor of a condensate depends on $x_4$ and $x_0$ only, so these are the only derivatives). `G[l, i, j]` holds $\Gamma^l{}_{ij}$ in both orders of $i$ and $j$. The two corrections are written with `np.einsum`: `"mml,l->"` sums $\Gamma^\mu{}_{\mu\lambda}T^\lambda{}_\nu$ over $\mu$ and $\lambda$, and `"lm,ml->"` sums $\Gamma^\lambda{}_{\mu\nu}T^\mu{}_\lambda$. The function also returns the size of the tensor (its largest entry).

```python
report("effective mass V = m + lambda S at x4 = 1",
       f"{m9 + lam9 * S9 * np.exp(a4_of(1.0)) / b4_of(1.0) ** 2:.6f}")
report("c_g at x4 = 1", f"{1.5 * H9 * np.exp(a4_of(1.0)) / np.sqrt(b4_of(1.0)):.6f}")
```

Two RESULT lines: `effective mass V = m + lambda S at x4 = 1 = 1.005001` and `c_g at x4 = 1 = 0.440067` ($0.375\,e^{0.35 - 0.19} = 0.375\,e^{0.16}$).

**In [17], the conservation test.**

```python
steps = 0.2 / 2.0 ** np.arange(11)  # 0.2, 0.1, ..., about 0.0002
X4_TEST, X0_TEST = 1.0, 0.5 / (6 * H9)  # x4 = 1 and z = 0.5
TRUE, CONTROL = condensate("true", X4_TEST), condensate("control", X4_TEST)
true_sizes, control_sizes = [], []
```

Eleven steps $h$ from 0.2 down to $0.2/2^{10} \approx 0.0002$, the test point $x_4 = 1$, $z = 0.5$ (so $x_0 = 0.5/(6H)$), the true condensate and the control with their column fixed at $x_4 = 1$, and two empty lists.

```python
for h in steps:
    div_true, size_true = divergence(TRUE, X4_TEST, X0_TEST, h)
    div_control, _ = divergence(CONTROL, X4_TEST, X0_TEST, h)
    true_sizes.append(np.abs(div_true).max())
    control_sizes.append(np.abs(div_control).max())
true_sizes, control_sizes = np.array(true_sizes), np.array(control_sizes)
```

For each step the largest of the eight components of the divergence is recorded, for both configurations.

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

Three checks. For the true condensate each halving of $h$ (from 0.2 to 0.003125) divides the result by a number between 3.6 and 4.4: the error of central differences falls like $h^2$, and the exact divergence is zero. At $h = 0.2/2^8$ the divergence is below $10^{-6}$ of the tensor's size. For the control the last two values agree to $10^{-3}$ (it has reached its limit) and the limit is larger than $10^{-2}$ of the tensor's size: it is not conserved.

```python
for x4_point, z_point in ((2.0, 1.0), (0.5, 2.2)):
    x0_point = z_point / (6 * H9)
    other = condensate("true", x4_point)  # chi9 at the time x4_point
    coarse, size_other = divergence(other, x4_point, x0_point, 1e-3)
    fine, _ = divergence(other, x4_point, x0_point, 1e-4)
    shrink = np.abs(coarse).max() / np.abs(fine).max()  # about 10^2 for an h^2 error
    check(90 < shrink < 110 and np.abs(fine).max() < 1e-5 * size_other,
          f"true condensate conserved at x4 = {x4_point}, z = {z_point} "
          "(h = 0.001 and 0.0001)")
```

Two more points of the true condensate, one beyond the fold ($z = 2.2$), each with its own column fixed at its own time: from $h = 0.001$ to $h = 0.0001$ the divergence must shrink about a hundredfold ($10^2$, because of $h^2$) and end below $10^{-5}$ of the tensor's size.

```python
WL = "Revision/theory/reports/wolfram-field-theory.json"
check(recorded(WL, "exact_solution_nonlinear_homogeneous_C") == "PASS"
      and recorded(WL, "conservation_on_shell_general") == "PASS",
      "the record proves the conservation that these numbers confirm",
      record=f"{WL}, checks exact_solution_nonlinear_homogeneous_C and "
             "conservation_on_shell_general")
```

The record's verdicts of the exact statements that these numbers confirm.

```python
for h, t_size, c_size in zip(steps[::2], true_sizes[::2], control_sizes[::2]):
    say(f"h = {h:.5f}:  true condensate {t_size:.2e},  control {c_size:.4f}")
```

Every second step is printed (`[::2]` takes every second entry): `h = 0.20000:  true condensate 6.77e-03,  control 0.0505`, then $3.93\cdot 10^{-4}$ and $0.0440$ at $h = 0.05$, $2.44\cdot 10^{-5}$ and $0.0436$ at $h = 0.0125$, $1.53\cdot 10^{-6}$ at $h = 0.00313$, $9.54\cdot 10^{-8}$ at $h = 0.00078$ and $5.96\cdot 10^{-9}$ at $h = 0.00020$, while the control stays at $0.0436$. Each step here is a quarter of the previous one, and the true values fall by a factor of about 16.

**In [18], the convergence figure.**

```python
fig, ax = plt.subplots()
ax.loglog(steps, true_sizes, "o-", label="true condensate")
ax.loglog(steps, control_sizes, "s-",
          label="control (no $c_g\\gamma^{(4)}\\gamma^{(0)}$ part)")
ax.loglog(steps, true_sizes[0] * (steps / steps[0]) ** 2, "k:",
          label="proportional to $h^2$")
ax.set_xlabel("finite-difference step $h$")
ax.set_ylabel("largest $|\\nabla_\\mu T^\\mu{}_\\nu|$")
ax.set_title("Conservation of the full tensor of a condensate")
ax.legend()
```

`ax.loglog` draws with both axes logarithmic: circles for the true condensate, squares for the control, and a dotted line proportional to $h^2$ through the first circle, for comparison.

```python
save_figure(fig, "conservation_convergence",
            "The largest of the eight components of the covariant divergence "
...)
```

The figure is saved as Figure 09c.4 (`09c_4_conservation_convergence.png`): the circles follow the dotted line (a straight line of slope 2 on these axes), the squares level off near $0.044$.

**In [19], the eight components of the divergence.**

```python
div_true, size_true = divergence(TRUE, X4_TEST, X0_TEST, 1e-3)
div_control, _ = divergence(CONTROL, X4_TEST, X0_TEST, 1e-3)
positions = np.arange(8)
```

The eight components at $h = 0.001$ for both configurations, and the bar positions.

```python
fig, ax = plt.subplots()
floor = 1e-16  # zero components are drawn at this height on the logarithmic axis
ax.bar(positions - 0.2, np.abs(div_true) + floor, width=0.4, label="true condensate")
ax.bar(positions + 0.2, np.abs(div_control) + floor, width=0.4,
       label="control (no $c_g\\gamma^{(4)}\\gamma^{(0)}$ part)")
ax.set_yscale("log")
ax.set_ylim(1e-16, 10.0)
ax.set_xticks(positions, [f"$\\nu = {n[0]}_{n[1]}$" for n in NAMES], fontsize=8)
ax.set_ylabel("$|\\nabla_\\mu T^\\mu{}_\\nu|$ (with $h = 0.001$)")
ax.set_title("The eight components of the divergence")
ax.legend(fontsize=8)
```

Two bars per component on a logarithmic axis; a component that is exactly zero would have no height on such an axis, so $10^{-16}$ (`floor`) is added to every bar. The ticks read $\nu = x_0, \dots, \nu = x_7$.

```python
save_figure(fig, "divergence_components",
            "The eight components $|\\nabla_\\mu T^\\mu{}_\\nu|$, $\\nu = x_0, \\dots, "
...)
```

The figure is saved as Figure 09c.5 (`09c_5_divergence_components.png`).

```python
space_components = [1, 2, 3]  # nu = x1, x2, x3
others = [0, 4, 5, 6, 7]  # nu = x0, x4, x5, x6, x7
check(np.abs(div_control).max() > 1e3 * np.abs(div_true).max()
      and np.abs(div_control[space_components]).min() > 1e-3
      and np.abs(div_control[others]).max() < 1e-6 * size_true,
      "control: its three 3-space momentum components are nonzero (over 1000 times "
      "the true condensate's), its x0, x4, x5, x6, x7 components vanish up to the "
      "h^2 error")
```

The check: the control's largest component exceeds the true condensate's by more than a factor 1000, its three components along 3-space are all larger than $10^{-3}$, and its other five components are below $10^{-6}$ of the tensor's size, like those of the true condensate.

```python
report("control: |components| nu = x1, x2, x3 (h = 0.001)",
       ", ".join(f"{abs(value):.4f}" for value in div_control[space_components]))
report("true condensate: largest |component| (h = 0.001)",
       f"{np.abs(div_true).max():.1e}")
```

Two RESULT lines: `control: |components| nu = x1, x2, x3 (h = 0.001) = 0.0436, 0.0324, 0.0187` and `true condensate: largest |component| (h = 0.001) = 1.6e-07`. The control breaks only the momentum balance along 3-space, as Section 9.26 explains.

**In [20], the last check.**

```python
captions = json.loads(output_file(CAPTION_FILE).read_text(encoding="utf-8"))
expected_files = ["09c_1_generic_condensate.png", "09c_2_offdiagonal_entries.png",
                  "09c_3_witness_condensate.png",
                  "09c_4_conservation_convergence.png",
                  "09c_5_divergence_components.png"]
```

The captions file is read back, and the five expected figure files are listed.

```python
check(sorted(captions) == expected_files and all(
    output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in expected_files),
    "the five figures of this notebook are saved and captioned")
all_checks_passed()
```

The check that the captions file names exactly these five files and that each exists; the last line prints `ALL 25 CHECKS PASSED (notebook 09c)`.

### 9.31 What we proved, what we computed, what we assumed

**PROVED in this chapter, line by line** (and in the Revision record, with the file and check named in the section):

- For the corrected metric, the volume factor $\sqrt{|g|} = e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}$ and its rate $\partial_4\ln\sqrt{|g|} = 2u - a_4' = 3a_4' + 4h_4$ (Section 9.2); for its diagonal vielbein, $\{\gamma^\mu, \Omega_\mu\} = 0$ for each direction, the three values of $\gamma^\mu\Omega_\mu$ per direction, and $\sum_\mu\gamma^\mu\Omega_\mu = c_g\gamma^{(0)} + v_g\gamma^{(4)}$ with $c_g = \frac32He^{a_4}b_4^{-1/2}$ and $v_g = b_4'/b_4 - a_4'/2 = \frac12\partial_4\ln\sqrt{|g|}$ (Section 9.3).
- From the definition of the energy-momentum tensor by the variation of the action, the diagonal entries $T^\mu{}_\mu = L_0 - K_\mu$ (Section 9.5); the reality of every entry and the symmetry of $T_{\nu\mu}$ (Section 9.6).
- $\rho = -\sum_{\mu \neq x_4}K_\mu + mS + U$, $p_\mu = \sum_{\nu \neq \mu}K_\nu - mS - U$, with their kinetic and potential parts (Section 9.7); the trace $7\sum_\mu K_\mu - 8(mS + U)$ and the kinetic-sum identity off shell, and on shell $\sum_\mu K_\mu = (m + U')S$, $L_0 = SU' - U$ and the trace $-mS + 3\lambda S^2$ (Section 9.8).
- The 21 Christoffel symbols of the corrected metric and why there are 21; the lemma $\Gamma^\mu{}_{\mu\nu} = \partial_\nu\ln|f_\mu|$; the divergence of a diagonal tensor; the two conservation identities $\partial_4\rho = -3a_4'(\rho + p_3) - 3h_4(\rho + p_t) - h_4(\rho + p_0)$ and $\partial_0p_0 = -3H\cot z\,(p_0 - p_t)$; the vanishing of the other six components (Section 9.9); the split of the $x_4$ identity into a dilution with the rate of the 7-volume, the work of 3-space and the work of the block, and, for $p_0 = p_t$, into a dilution and an exchange $-3a_4'(p_3 - p_t)$ (Section 9.10); $p_0 = p_t$ for entries independent of $x_0$, the conservation of the Einstein source of the record's history, the profiles $p_0 = P + c\,(\sin^2 z)^{-1/4}$ and the form in the coordinate $y$ (Section 9.11).
- The connection terms $K^{x_4}{}_{x_1} = 0$ and $K^{x_4}{}_{x_5} = \frac12HW\,\bar\Phi\gamma^{(4)}\gamma^{(0)}\gamma^{(5)}\Phi$ of a homogeneous configuration (Section 9.12), and the entries $T^{x_1}{}_{x_0} = -\frac18e^{-2a_4}b_4^{1/2}\cot z\,(4a_4' - b_4'/b_4)\,B(x_0\,x_1\,x_4)$ and $T^{x_4}{}_{x_1} = \frac34He^{2a_4}b_4^{-1/2}\,B(x_0\,x_1\,x_4)$ of a condensate, equal to the record's coefficients (Section 9.26).
- The condensates $\Phi = e^{a_4/2}b_4^{-1}\chi$ with $\chi' = M\chi$, the constancy of $\chi^\dagger C\chi$, the dilution $S = e^{a_4}b_4^{-2}S_0$, $M^2 = (c_g^2 - V^2)\cdot 1$, the commutator $M_1M_2 - M_2M_1 = 2(V_1c_2 - V_2c_1)\gamma^{(0)}$ and the exact solution for a constant $M$; their $\rho = mS + U$ and $p = SU' - U$ in all seven directions, $T^{x_4}{}_{x_0} = 0$, $d\rho/dx_4 = -(3a_4' + 4h_4)(\rho + p)$, and $w = x/(2 + x)$ with its special values; that every condensate enters the growing wedge on the record's history (Sections 9.18 to 9.20); $\rho = E\,u^\dagger Bu$ for plane waves of flat space (Section 9.21); in the construction of the witnesses, the dimension 8 of the space of the eigenvalue $-i\omega$, the dimension 1 of each of its eight sectors, and $S = 2|v_1^\dagger Cv_2|^2 \ge 0$; and that at a single moment the off-diagonal conditions of gravity on a condensate are 15 conditions on its 24 bilinears (Section 9.26).

**PROVED in the Revision record and used here without its proof:** the components of the spin connection; the vielbein-variation tensor with its spin-density term; the complete (Belinfante) tensor as its symmetric part for every configuration, and the equality of the two tensors on shell in all 64 entries (off shell, in general, only the 8 diagonal entries agree); the drop-out of the spin connection from the Lagrangian of every diagonal vielbein; the conservation $\nabla_\mu T^\mu{}_\nu = 0$ of every solution (Noether identity); the same formulas for the Grassmann field dirac16complex; the positive Fock realisation of the quantised field for single good-sector momenta with frozen coefficients, and the complex frequencies of the curved good sector without a boundary condition at the folds (for $U = 0$ wherever $m^2 < c_g^2$); in the finite Fock model of one good-sector mode set with frozen coefficients, the operator form of the on-shell identity for $\lambda \neq 0$ when the potential and the tensor are both Wick ordered, its failure for every other ordering tested, and the exact values $\rho = mn + \frac{\lambda}{2}n(n - 1)$ and $p = \frac{\lambda}{2}n(n - 1)$ on the occupation states with $n$ quanta at rest (Section 9.13); every solution of the linear system $\chi' = M(x_4)\chi$ is an exact condensate; the 36 off-diagonal entries of a condensate as combinations of 24 bilinears with the listed coefficients; the diagonal witnesses on the histories with constant $e^{2a_4}/b_4$ with $\omega = 4, 3, 4$; the Krein inertia (4,4) of the plane waves; the field equations of gravity require every off-diagonal entry of the source to vanish, $p_0 = p_t$ and no dependence on $x_0$; the source of the record's history; a condensate as a source needs equal 3-space and hidden pressures on the gravitational side, which no exponential history allows in Einstein's theory and only the histories with constant $e^{2a_4}/b_4$ allow for the author's weights (with further conditions), and no condensate can source the record's history (Sections 9.11, 9.19 and 9.26); and, in the dark-sector record, the equation of state $w_{\rm eff}$ that a 3-space observer infers for a homogeneous condensate: $\frac59\,w$ under the definitions A and B of the observer's energy density and $\frac59\,w - \frac49$ under C, with the drifting ratio $w = p/\rho$ (Section 9.19; the definitions themselves are ASSUMED).

**COMPUTED by the notebooks** (every number reproduces the record where they overlap): Notebook 09a, 29 checks, confirms the tensor identities at one point to $10^{-11}$ or better, the three values of $\gamma^\mu\Omega_\mu$ per direction and their sum, re-derives the 21 Christoffel symbols and the two identities exactly for both signs of $\sin z$, checks the first-law reading and the sources of the record's history, and checks the $x_0$ profiles on a grid to a relative residual of $5.0 \cdot 10^{-5}$; Notebook 09b, 35 checks, confirms the condensates at 1601 times to $10^{-9}$, finds the moments $x_4 = 11.8136$, $0.6776$ and $11.6963$ at which the two condensates change between oscillating and growing, measures $w$ on twelve exact solutions (agreement with $x/(2 + x)$ to $10^{-9}$), confirms the dilution rate $\frac{5}{12}$, solves the toy fluids with RK4 (relative error $2.80 \cdot 10^{-7}$, error ratio $16.31$ for a halved step) and reproduces $\rho = \pm 5$; Notebook 09c, 25 checks, confirms the 36 entries against the record's coefficients to $10^{-12}$, the dimensions 8 and 1 of the construction of the witnesses, the diagonal tensor of the witnesses at 36 points, the record's frequencies exactly and its values of $S$ up to one common factor (40000), and the conservation of the full tensor along a curved history (an error falling like $h^2$, down to $5.96 \cdot 10^{-9}$), with a negative control that breaks only the three momentum balances along 3-space (components $0.0436$, $0.0324$, $0.0187$). The observation $S = 2\omega^2/V^2$ for the three witnesses is COMPUTED, not proved.

**ASSUMED, chosen, or an interpretation.** The sign conventions $\rho = -T^{x_4}{}_{x_4}$ and $p_\mu = T^\mu{}_\mu$ are definitions. The history $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$ ($A = 1$) is a PRESCRIBED background; it and the curved history $a_4 = 0.3x_4 + 0.05x_4^2$, $b_4 = e^{0.4x_4 - 0.02x_4^2}$ and every parameter value of the examples are choices; every identity holds for every history. The first-law reading of the $x_4$ identity is an interpretation, not an extra result. The toy fluids are an ILLUSTRATION, not solutions of the field equations. The normalisations A, B and C of the observer's energy density, quoted in Section 9.19 from the dark-sector record, are ASSUMPTIONS of that record.

**OPEN.** Which normalisation of the observer's energy density over the extra times and the hidden direction, if any, describes a physical observer in 3-space, and a fit to supernova data (the Revision record computes the equation of state that such an observer would infer, its change in time, fits of the CPL form $w(a) = w_0 + w_a(1 - a)$, a straight line in the 3-space scale factor $a$ named after Chevallier, Polarski and Linder, and the comparison with the Unite values, all under the ASSUMED definitions A, B and C; Chapter 22, COMPUTED); the operator (normal-ordered) form of the on-shell kinetic-sum identity $\sum_\mu\langle{:}K_\mu{:}\rangle = \langle{:}(m + U')S{:}\rangle$ for $\lambda \neq 0$ for the field on a whole slice (Section 9.13; it is verified only in the finite Fock model of one good-sector mode set with frozen coefficients, and there only under Wick ordering), and with it the operator form of the on-shell values of $L_0$ and of the trace, and the symmetry and conservation of the quartic operator; a space of quantum states with positive norms for the full quantised field; whether the record's statement of the off-diagonal conditions of a condensate (all 24 bilinears zero) follows from the 15 conditions of one moment holding along a whole history (not derived in this book); condensates with a diagonal tensor on histories along which $e^{2a_4}/b_4$ changes, and condensates as sources on histories that are not exponential (not decided in the record). Any reading of the negative energies of the commuting field as a phantom dark energy is a HYPOTHESIS, not a result.

**Not claimed.** Nothing in this chapter concerns the creation of universes or the matter-antimatter asymmetry. The only link to Part V is the sign reversal of the tensor under the chirality map $\Gamma$ (theorem T1, Section 9.21), an exact map between sets of solutions in a fixed gravitational field; it proves no creation process, rate or amplitude (Chapters 18 to 21 state what the pairing theorems prove and what they do not).

### 9.32 Exercises

**Exercise 1.** Use the lemma $\Gamma^\mu{}_{\mu\nu} = \partial_\nu\ln|f_\mu|$ of Section 9.9 to compute $\Gamma^{x_5}{}_{x_4x_5}$, $\Gamma^{x_5}{}_{x_0x_5}$ and $\Gamma^{x_0}{}_{x_0x_4}$, and compare with the table.

*Answer.* $\ln f_5 = \ln\big(e^{-a_4}b_4^{1/2}(\sin^2 z)^{1/12}\big) = -a_4 + \frac12\ln b_4 + \frac{1}{12}\ln\sin^2 z$. Differentiating with respect to $x_4$: only the first two terms depend on $x_4$, so $\Gamma^{x_5}{}_{x_4x_5} = -a_4' + \frac{b_4'}{2b_4} = h_4$. Differentiating with respect to $x_0$ with the chain rule ($dz/dx_0 = 6H$): $\Gamma^{x_5}{}_{x_0x_5} = \frac{1}{12}\cdot\frac{2\sin z\cos z}{\sin^2 z}\cdot 6H = H\cot z$. Finally $\ln|f_0| = -a_4 + \frac12\ln b_4 + \ln|\cot z|$, and its derivative with respect to $x_4$ is again $-a_4' + \frac{b_4'}{2b_4} = h_4$. The table lists $\Gamma^{x_t}{}_{x_4x_t} = h_4$, $\Gamma^{x_t}{}_{x_0x_t} = H\cot z$ and $\Gamma^{x_0}{}_{x_0x_4} = h_4$ (the symbols are symmetric in their lower indices).

**Exercise 2.** Suppose the block grew like 3-space, with the factors $|f_0| = e^{a_4}b_4^{1/2}|\cot z|$ and $f_5 = f_6 = f_7 = e^{a_4}b_4^{1/2}W$ (this is not the author's metric). Use the divergence formula for a diagonal tensor to find the $x_4$ identity for entries with $p_0 = p_t$, and the rate of the 7-volume. Compare with Section 9.10.

*Answer.* Now $\partial_4\ln|f_0| = \partial_4\ln f_t = a_4' + \frac{u}{2}$, which we call $g$, while $\partial_4\ln f_i = a_4'$ and $\partial_4\ln f_4 = 0$. With $T^{x_4}{}_{x_4} = -\rho$ the formula gives $\nabla_\mu T^\mu{}_{x_4} = -\partial_4\rho + g(-\rho - p_0) + 3a_4'(-\rho - p_3) + 3g(-\rho - p_t)$, and with $p_0 = p_t$ conservation is $\partial_4\rho = -3a_4'(\rho + p_3) - 4g(\rho + p_t)$. The 7-volume grows at the rate $3a_4' + 4g = 7a_4' + 2u$: all seven directions expand on a history with $a_4' > 0$ and $u > 0$, and every term dilutes. In the author's corrected metric the block shrinks at the rate $h_4 = \frac{u}{2} - a_4'$, negative on the history, so the four block terms $-4h_4(\rho + p_t)$ push the energy density up, and the 7-volume grows only at the rate $3a_4' + 4h_4 = 2u - a_4'$.

**Exercise 3.** A condensate has $m = 1$ and $S = 1$. Compute $\rho$, $p$, $w$ and the trace in two ways for $\lambda = 0.5$ and for $\lambda = -0.8$, and compare with the numbers printed by Notebook 09b at $x_4 = 0$.

*Answer.* $\lambda = 0.5$: $\rho = mS + \frac{\lambda}{2}S^2 = 1 + 0.25 = 1.25$; $p = \frac{\lambda}{2}S^2 = 0.25$; $w = 0.25/1.25 = 0.2$ (also $x/(2 + x)$ with $x = 0.5$: $0.5/2.5 = 0.2$). Trace: $-\rho + 7p = -1.25 + 1.75 = 0.5$, and $-mS + 3\lambda S^2 = -1 + 1.5 = 0.5$. $\lambda = -0.8$: $\rho = 1 - 0.4 = 0.6$, $p = -0.4$, $w = -0.4/0.6 = -0.666667$ (and $x/(2 + x) = -0.8/1.2$); trace $-0.6 - 2.8 = -3.4 = -1 - 2.4$. Notebook 09b prints (In [8]) `1.250000, 2.500e-01, 0.200000` and `0.600000, -4.000e-01, -0.666667`.

**Exercise 4.** For $m > 0$ and $\lambda \neq 0$, find the value of $S$ for which a condensate has $w = -1$, compute its $\rho$ and $p$, and decide the sign of $\rho$. Does this condensate oscillate or grow at that moment?

*Answer.* $w = -1$ requires $x = \lambda S/m = -1$, that is $S = -m/\lambda$. Then $\rho = mS + \frac{\lambda}{2}S^2 = -\frac{m^2}{\lambda} + \frac{\lambda}{2}\cdot\frac{m^2}{\lambda^2} = -\frac{m^2}{\lambda} + \frac{m^2}{2\lambda} = -\frac{m^2}{2\lambda}$ and $p = \frac{\lambda}{2}S^2 = \frac{m^2}{2\lambda}$, so indeed $p = -\rho$. The energy density is positive only for $\lambda < 0$ (then $S = -m/\lambda > 0$); for $\lambda > 0$ it is negative. The effective mass is $V = m + \lambda S = 0$, so $k^2 = c_g^2 - 0 = c_g^2 > 0$: at that moment the condensate lies in the growing wedge and its column grows at the rate $k = c_g = \frac32He^{a_4}b_4^{-1/2}$. (Because $S$ is diluted, $x$ drifts, and $w = -1$ holds only at one moment.)

**Exercise 5.** A toy fluid (an illustration) has $w_3 - w_t = 1/3$ and $w_t = 0$ on the history $a_4 = AHx_4$, $b_4 = e^{(4/3)AHx_4}$ with $H = 0.25$. Compute $\rho(8)/\rho(0)$ for $A = 1$ and for $A = -1$, and their product.

*Answer.* By Section 9.10, $\rho(x_4)/\rho(0) = e^{-AH(3\Delta w + \frac53(1 + w_t))x_4}$. For $A = 1$ the exponent at $x_4 = 8$ is $-0.25\cdot(1 + \frac53)\cdot 8 = -\frac{16}{3}$, so the ratio is $e^{-16/3} = 0.004828$, the number of Notebook 09b (In [14]). For $A = -1$ every rate changes sign ($a_4'$, $u$ and $h_4$ are all proportional to $A$), the exponent is $+\frac{16}{3}$ and the ratio is $e^{16/3} = 207.13$. The product is $e^{-16/3}e^{16/3} = 1$: reversing the history reverses the energy flow, which is the check of In [14].

**Exercise 6.** Suppose $p_t = P$ is a constant and the hidden pressure $p_0$ stays finite as $z \to 0$. Show that $p_0 = P$ everywhere. What does the condition mean in the coordinate $y$?

*Answer.* By Section 9.11 every solution of the $x_0$ balance is $p_0 = P + c\,(\sin^2 z)^{-1/4}$ with a constant $c$. As $z \to 0$, $\sin^2 z \to 0$, so $c\,(\sin^2 z)^{-1/4}$ grows without bound unless $c = 0$. A finite $p_0$ therefore needs $c = 0$, and then $p_0 = P$ at every $z$. In the coordinate $y = \ln|\sin z|/(6H)$ the profiles are $p_0 = P + c\,e^{-3Hy}$, and $z \to 0$ is $y \to -\infty$, where $e^{-3Hy}$ grows without bound; again only $c = 0$ stays finite.

**Exercise 7.** Show that the kinetic term $K_\mu$ is a real number.

*Answer.* Let $Y = \bar\Phi\gamma^{(\mu)}\partial_\mu\Phi = \Phi^\dagger(C\gamma^{(\mu)})\partial_\mu\Phi$. Since $C\gamma^{(\mu)}$ is real, $Y^* = \Phi^T(C\gamma^{(\mu)})(\partial_\mu\Phi)^*$. A single number equals its transpose, so $Y^* = (\partial_\mu\Phi)^\dagger(C\gamma^{(\mu)})^T\Phi$; since $C\gamma^{(\mu)}$ is antisymmetric, $Y^* = -(\partial_\mu\Phi)^\dagger C\gamma^{(\mu)}\Phi = -\partial_\mu\bar\Phi\,\gamma^{(\mu)}\Phi$ (because $\partial_\mu\bar\Phi = (\partial_\mu\Phi)^\dagger C$). Hence $\bar\Phi\gamma^{(\mu)}\partial_\mu\Phi - \partial_\mu\bar\Phi\gamma^{(\mu)}\Phi = Y + Y^*$, which is twice the real part of $Y$, and $K_\mu = (Y + Y^*)/(2f_\mu)$ is real.

**Exercise 8.** Use the derivation of Section 9.26 to show that the entry $T^{x_1}{}_{x_0}$ of a condensate vanishes at every moment at which 3-space and the block change at the same rate, decide whether this happens on the record's history, and evaluate the record's coefficient of $K^{x_1}{}_{x_0}$ at $a_4 = 0.5$, $a_4' = 0.25$, $b_4 = e^{2/3}$, $b_4'/b_4 = \frac13$, $z = \pi/4$. Which number of Notebook 09c does it reproduce?

*Answer.* Section 9.26 gives $T^{x_1}{}_{x_0} = -\frac14e^{-a_4}s_b\cot z\,(a_4' - h_4)\,B(x_0\,x_1\,x_4)$, which is zero exactly when $a_4' = h_4$, that is when 3-space (rate $a_4'$) and the block (rate $h_4$) change at the same rate; with $h_4 = \frac{u}{2} - a_4'$ this is $4a_4' = u$. On the record's history $a_4' = AH$ and $h_4 = -\frac{AH}{3}$, so $a_4' - h_4 = \frac43AH \neq 0$ (equivalently $4a_4' - u = \frac83AH$): the entry is not zero there. At the given point the coefficient of $K^{x_1}{}_{x_0} = -T^{x_1}{}_{x_0}$ is $\frac18e^{-2a_4}b_4^{1/2}\cot z\,(4a_4' - u) = \frac18e^{-1}e^{1/3}\cdot 1\cdot\frac23 = \frac{1}{12}e^{-2/3} = \frac{0.513417}{12} = 0.042785$. Notebook 09c prints `K^x1_x0: coefficient +0.042785 of B(x0 x1 x4)` in In [9], and In [7] shows that $T^{x_1}{}_{x_0}$ is proportional to $a_4' - \frac{1}{12}$ when $b_4'/b_4 = \frac13$ is kept.

**Exercise 9.** For the plane wave of Section 9.21 with $m = 2$ and $(k_0, k_1, k_2, k_3) = (4, 1, 2, 0)$, find the positive frequency $E$ and the energy density of a wave whose unit column satisfies $Bu = -u$. What is the energy density of the same wave multiplied by 10?

*Answer.* $h^2 = (m^2 + k_0^2 + k_1^2 + k_2^2 + k_3^2)\cdot 1 = (4 + 16 + 1 + 4 + 0)\cdot 1 = 25$, so $E = 5$. With $\rho = E\,u^\dagger Bu$ and $u^\dagger Bu = -u^\dagger u = -1$: $\rho = -5$. Multiplying the wave by 10 multiplies every bilinear by $10^2 = 100$: $\rho = -500$. There is no lower bound.

**Exercise 10.** On the record's history with $A = 1$, $H = 0.25$ and $b_4(0) = 1$, compute $S(16)/S_0$, $\rho(16)$, $p(16)$ and $w(16)$ of the condensate with $m = 1$, $\lambda = 0.5$ and $S_0 = 1$, and compare with Notebook 09b. Show that $S\sqrt{|g|}$ does not change in time.

*Answer.* $S = e^{a_4}b_4^{-2}S_0 = e^{AHx_4 - \frac83AHx_4} = e^{-\frac53\cdot 0.25\cdot 16} = e^{-20/3} = 0.0012726$. Then $\rho = mS + \frac{\lambda}{2}S^2 = 0.0012726 + 0.25\cdot 1.6196\cdot 10^{-6} = 0.0012730$, $p = \frac{\lambda}{2}S^2 = 4.049\cdot 10^{-7}$ and $w = p/\rho = 0.000318$. Notebook 09b prints `0.001273, 4.049e-07, 0.000318` at $x_4 = 16$ (In [8]). At fixed $x_0$, $\sqrt{|g|} = e^{-a_4}b_4^2\cdot|\cot z|(\sin^2 z)^{1/4}$, so $S\sqrt{|g|} = e^{a_4}b_4^{-2}S_0\cdot e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4} = S_0|\cot z|(\sin^2 z)^{1/4}$, which does not depend on $x_4$: the scalar is diluted exactly by the growth of the 7-volume.
