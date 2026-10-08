## 17. The a4 equations with the Kohn-Sham source: a prescribed background

Chapters 14 to 16 computed the Kohn-Sham states of the field dirac16complex in the author's primordial universe, at five instants of the history $a_4 = Hx_4$ along which 3-space inflates and the three extra times deflate exponentially. Chapter 12 derived the field equations that gravity imposes on the function $a_4(x_4)$. This chapter puts the two together. It asks one question: if the energy and momentum of the Kohn-Sham gas are put on the right-hand side of the field equations of gravity, is the history $a_4 = Hx_4$ a solution? The answer is no, and the chapter proves exactly why. Two complete notebooks repeat every step: Notebook 17a tests the three conditions that the field equations impose on every source against all 75 recorded Kohn-Sham states, and Notebook 17b shows that the failure is forced by the conservation of energy and momentum itself.

### 17.1 What this chapter does, and why

**The question.** In Einstein's theory, and in its generalisation used in this book, matter and geometry are tied together: the curvature of the metric equals a constant times the energy and momentum of the matter. In Chapters 14 and 15 we did something weaker. We took the author's metric with the history $a_4 = Hx_4$ as GIVEN, and we computed how a gas of dirac16complex quanta settles into its lowest state at five instants of that history. We never asked whether the gas, through its own energy and momentum, would make the metric that it moves in. This chapter asks that question.

**Why it matters.** If the answer were yes, the history $a_4 = Hx_4$, with the gas in it, would be a solution of the coupled equations of gravity and matter: a possible universe of this theory. Every energy, pressure and equation of state computed along it would then be a prediction of the theory. If the answer is no, the history is a **prescribed background**: a stage that we chose, on which the gas moves as a **test field** whose own gravity is ignored. Its energies and pressures are still well-defined numbers, but they describe a gas in a chosen geometry, not a self-consistent universe. The Revision record states the answer in `Revision/field_equations_a4/reports/ks-source-conditions.json`: no recorded Kohn-Sham state is an admissible source, and the history is a prescribed background without back-reaction. This chapter derives that statement from the beginning and checks every number of it.

**What is derived, in order.**

- The field equations of $a_4$ and the most general source they allow (Section 17.3).
- The three **source conditions**: no dependence on the hidden coordinate $x_8$ (C1, Section 17.4), the algebraic condition $p_3 + p_t = 2p_8$ (C2, Section 17.5), and, for the linear history $a_4 = AHx_4 + a_0$, equal pressures and a constant energy density (C3, Section 17.6).
- What the 75 recorded Kohn-Sham states are and which numbers of them we use (Section 17.7); then Notebook 17a, which evaluates C1, C2 and C3 on all of them (Sections 17.8 to 17.11).
- Why the states fail: every source of the field equations must be conserved, and what the Kohn-Sham states conserve (Section 17.12); the conservation law in the hidden coordinate $y$ (Section 17.13); for a conserved source C2 says exactly that the hidden pressure $p_8$ is flat (Section 17.14); the integrated form and the averaged ratio (Section 17.15); the energy exchange along the history and the propagation of the constraint, which turn C3 into $p_3 = p_t$ (Section 17.16).
- The field equations averaged over the hidden direction: the moment equations, which of them can hold together, their first integral, and what can and cannot be integrated with the Kohn-Sham source, within a stated approximation (Section 17.17); then Notebook 17b (Sections 17.18 to 17.21).
- What "prescribed background" means, and what remains open (Section 17.22); the summary of statuses (Section 17.23); exercises with complete answers (Section 17.24).

**The two notebooks.**

| notebook | what it computes | PASS lines | figures |
| --- | --- | --- | --- |
| 17a | the three source conditions derived from the record, evaluated on the 75 recorded Kohn-Sham states | 16 | 7 |
| 17b | the conservation law in the author's metric; why a conserved source fails C2 and C3; the averaged equations and their first integral | 20 | 6 |

Neither needs Rust: both read the stored results of the Revision Rust solver and the Revision reports, and compute everything else with numpy and sympy.

**The status of every statement.** As everywhere in this book, every statement carries one of five labels: PROVED (exact, with the verifier file and check name), COMPUTED (numerical, with its measured error), ASSUMED, HYPOTHESIS, OPEN. In this chapter:

- PROVED: the three source conditions (Sections 17.4 to 17.6), the conservation law and its consequences (Sections 17.12 to 17.16), the moment equations and their first integral (Section 17.17), and the absence of a solution without matter in Einstein gravity.
- COMPUTED: every statement about the 75 recorded states (Notebooks 17a and 17b), each with the record file it reproduces.
- ASSUMED: the history $a_4 = Hx_4$ on which the Kohn-Sham states were computed (it is the prescribed background); the good sector, the Z2 mirror at the brane and the tip cutoff of the Kohn-Sham model (Chapter 14); in Section 17.17, the approximation that keeps only two of the averaged field equations (it is stated there with its error).
- OPEN: what metric the Kohn-Sham gas would produce with back-reaction, and whether any state of dirac16complex is an admissible source of the author's metric (Section 17.22).
- HYPOTHESIS: none in this chapter.

**Honesty about what this chapter is not.** Nothing in this chapter concerns the creation of universes, pairs of universes, or matter and antimatter. In particular the sign changes that appear in it (a pressure that changes sign along the hidden direction, the states with couplings $+\lambda$ and $-\lambda$ in figure 4 of Notebook 17b) are properties of particular recorded states; they are not the pairing theorems of Chapters 18 to 20.

### 17.2 The words and symbols of this chapter

Each word is defined in plain terms here; the later sections make each definition precise with formulas.

- **Coordinates** $x_1, \dots, x_8$, in the author's order: $x_1, x_2, x_3$ are ordinary 3-space, which inflates; $x_4$ is the time; $x_5, x_6, x_7$ are the three **extra times**, which behave like time and **deflate exponentially**; $x_8$ is the hidden space direction. The angle $z = 6Hx_8$ runs from $0$ to $\pi/2$; $H > 0$ is a constant of the author's metric, with the unit of an inverse length.
- **Prime**: on $a_4$ it means the derivative with respect to the time, $a_4' = da_4/dx_4$, $a_4'' = d^2a_4/dx_4^2$; the code writes them `ad1` and `ad2`. On a function of the hidden coordinate it means $d/dy$; we always say which.
- **Hidden coordinate** $y = \ln(\sin z)/(6H)$: a second way to number the points of the hidden direction, used by the Kohn-Sham computations. It grows when $x_8$ grows. $y = 0$ is the end $z = \pi/2$, called the **brane**; $y \to -\infty$ is the end $z \to 0$, called the **tip**. The Kohn-Sham computations stop at $y = -L = -3$, the **tip cutoff**; the region $-3 \le y \le 0$ is the **patch**.
- **Metric**, **scale factor**: the table $g_{\mu\nu}$ that turns coordinate steps into squared lengths, and the number $\sqrt{|g_{\mu\mu}|}$ by which a step along one direction must be multiplied to give a length.
- **Field equations of gravity**: $\sum_{k=1}^{3}\alpha_kE_{(k)}{}^\mu{}_\nu + \Lambda\,\delta^\mu_\nu = \kappa\,T^\mu{}_\nu$. On the left are the three **Lovelock tensors** $E_{(1)}$ (the Einstein tensor), $E_{(2)}$ (the Gauss-Bonnet tensor) and $E_{(3)}$, built from the curvature of the metric, weighted by the **couplings** $\alpha_1, \alpha_2, \alpha_3$, and the **cosmological constant** $\Lambda$. $\kappa > 0$ measures the strength of gravity. **Einstein gravity** is $\alpha_1 = 1$, $\alpha_2 = \alpha_3 = 0$. The symbol $\delta^\mu_\nu$ is 1 when $\mu = \nu$ and 0 otherwise.
- **Energy-momentum tensor** $T^\mu{}_\nu$, also called the **source**: an $8 \times 8$ table at every point that says how much energy and momentum the matter has and how they flow. Its diagonal parts are the **energy density** $\rho = -T^{x_4}{}_{x_4}$ and the **pressures** $p_3$ (each direction of 3-space), $p_t$ (each extra time) and $p_8$ (the hidden direction); its possible **mixed** parts are $q_{48} = T^{x_4}{}_{x_8}$ and $q_{84} = T^{x_8}{}_{x_4}$.
- **Admissible source**: a source for which the field equations of the author's metric can hold. **Source conditions** C1, C2, C3: the three conditions that an admissible source must meet (Sections 17.4 to 17.6).
- **Linear member**: the history $a_4 = AHx_4 + a_0$ with constants $A$ (the **slope**) and $a_0$. For $A > 0$ the extra-time scale factor $e^{-a_4}$ shrinks exponentially. The history of the Kohn-Sham computations is $A = 1$, $a_0 = 0$.
- **Slice**: one instant of the history, labelled by the value $a_{4,0}$ of $a_4$ there; the Kohn-Sham states were computed at the five slices $a_{4,0} = 0, 0.5, 1, 1.5, 2$.
- **Kohn-Sham state**: a many-quantum state of dirac16complex computed with the Kohn-Sham method (Chapters 13 to 15). A recorded state is named like `N136_lamm2_a20`: particle number $N = 136$, coupling $\lambda = -\lambda_2$ (`lamm2`; `lamm1` is $-\lambda_1$, `lam0` is $\lambda = 0$, `lamp1` is $+\lambda_1$, `lamp2` is $+\lambda_2$), slice $a_{4,0} = 2.0$ (`a20`).
- Words of the Kohn-Sham method used again here (Chapters 13 to 15 define them in full): an **orbital** is the wave of one quantum, and an **eigen-orbital** one that solves the Kohn-Sham equation with a definite energy; the **Fermi level** is the energy that separates the occupied orbitals from the empty ones; a state is **self-consistent** when the potentials computed from its own density are the potentials its orbitals were computed with; the **good sector** is the set of orbitals that do not depend on the extra times $x_5, x_6, x_7$; the **Z2 mirror** is the ASSUMED rule that the hidden direction continues beyond the brane as a mirror image of the computed patch, with the field there fixed by the field on the computed side (Chapter 14 states the rule; record `Revision/kohn_sham/ks-theory.json`, key `boundaryConditions.brane`).
- More words of the Kohn-Sham computations: a **shell** is a group of orbitals with the same energy, and a **closed shell** is a particle number $N$ that fills every orbital up to some energy completely and none above it (so the ground state is unique); the **first-order mean-field potential** is the potential that one quantum feels from the others when the interaction is counted once, to first order in the coupling $\lambda$, with the density of the free gas; **fixed occupations** means that the same orbitals stay filled when $a_4$ is changed a little, even if their energies move.
- **Least squares**: the straight line through a set of points that makes the sum of the squared vertical distances of the points from the line as small as possible.
- **Moment** of a field equation: the equation multiplied by the volume weight $e^{6Hy}$ and integrated over the patch; it involves the source only through its weighted means $\bar\rho$, $\bar p_3$, $\bar p_t$, $\bar p_8$. **First integral**: an equation with only first derivatives that every solution of a second-order equation obeys. **Cubic Hermite interpolation**: between two tabulated points, the cubic polynomial with the given values and the given slopes at both ends. **Turning point**: the value of $a_4$ where $a_4'$ reaches 0. **Branch point**: a value of $a_4'$ where $F(a_4') = 0$, so that the evolution equation cannot be solved for $a_4''$.
- **Profile**: a component of the source as a function of $y$, stored at 151 points. **Proper density**: an amount per unit of proper volume, the volume that rulers measure.
- **max|T|**: the largest absolute value of $\rho$, $p_3$, $p_t$ and $p_8$ of a state over the whole patch. We divide by it to compare states of very different size.
- **Integral over the patch** $\int X$: the total amount of a density $X$ in the computed region, $2\,\mathrm{Vol}_7\int_{-3}^{0}e^{6Hy}X\,dy$ (Section 17.7). **Weighted mean** $\bar X$: the integral divided by the proper volume of the patch.
- **Covariant divergence** $\nabla_\mu T^\mu{}_\nu$: the curved-space form of "the change of a quantity in time plus its outflow through the walls of a small box". **Conservation**: zero covariant divergence. **Christoffel symbols** $\Gamma^\lambda{}_{\mu\nu}$: combinations of first derivatives of the metric that say how the coordinate directions turn and stretch from point to point. **Bianchi identity**: the left-hand side of the field equations has zero covariant divergence for every metric.
- **Constraint**: the $x_4$ component of the field equations (it contains $a_4'$ but no $a_4''$). **Evolution equation**: the 3-space component minus the extra-time component, $a_4''F(a_4') = \kappa(p_3 - p_t)$.
- **Prescribed background**: a metric that is chosen, not solved for. **Test field**: matter that moves in a prescribed background while its own gravity is ignored. **Back-reaction**: the effect of the matter's own gravity on the metric; a test field has none.
- **Finite difference**: an estimate of a derivative from neighbouring values in a table. Its **order of accuracy** $p$: its error falls like $h^p$ when the step $h$ shrinks. **Simpson's rule**: an estimate of an integral from equally spaced values, of order 4.
- **Heat map**: a table drawn as coloured squares, one colour per value. **Symmetric logarithmic axis**: an axis that is logarithmic for large positive and large negative values and linear in a narrow band around zero, so that both signs and many orders of magnitude can be shown.
- **sha256 fingerprint**: a 64-digit code computed from the bytes of a file; two files with the same fingerprint are, for all practical purposes, identical.
- **Units**: as in the Revision runs, $H = 1$ and the fermion mass $m = 1$. Lengths are in units of $1/H$; energy densities and pressures (energy per unit of 7-dimensional volume) in units of $m^8$; integrals over the patch (energies) in units of $m$.

### 17.3 The field equations of a4 and their source

**The metric.** The author's metric is diagonal; in the order $x_1, \dots, x_8$ its entries are

$$
\begin{aligned}
g = \mathrm{diag}\big(&e^{2a_4}\sin^{1/3}z,\ e^{2a_4}\sin^{1/3}z,\ e^{2a_4}\sin^{1/3}z,\ -1, \\
&-e^{-2a_4}\sin^{1/3}z,\ -e^{-2a_4}\sin^{1/3}z,\ -e^{-2a_4}\sin^{1/3}z,\ \cot^2 z\big),
\end{aligned}
$$

with $z = 6Hx_8$ and one free function $a_4(x_4)$. The 3-space scale factor is $e^{a_4}\sin^{1/6}z$ and the extra-time scale factor $e^{-a_4}\sin^{1/6}z$: when $a_4$ grows, 3-space inflates and the extra times deflate.

**The source.** Chapter 12 allowed the most general source that the symmetry of the metric suggests:

$$
T^\mu{}_\nu = \mathrm{diag}\big(p_3, p_3, p_3, -\rho, p_t, p_t, p_t, p_8\big) + q_{48}\ (\mu = x_4, \nu = x_8) + q_{84}\ (\mu = x_8, \nu = x_4),
$$

where every one of $\rho, p_3, p_t, p_8, q_{48}, q_{84}$ may a priori depend on $x_4$ and on $x_8$.

**The left-hand sides.** The Revision record `Revision/field_equations_a4/a4-equations.json` (key `lovelockTensors`) stores every component of the three Lovelock tensors of the author's metric. Writing $a' = a_4'$ and $a'' = a_4''$ for short, the components we need are:

$$
\begin{aligned}
E_{(1)}{}^{x_1}{}_{x_1} &= 15H^2 - 3a'^2 + a'', \qquad E_{(1)}{}^{x_5}{}_{x_5} = 15H^2 - 3a'^2 - a'', \\
E_{(1)}{}^{x_8}{}_{x_8} &= 15H^2 - 3a'^2, \qquad E_{(1)}{}^{x_4}{}_{x_4} = 3a'^2 + 21H^2,
\end{aligned}
$$

$$
\begin{aligned}
E_{(2)}{}^{x_1}{}_{x_1} &= 12a'^4 + 168a'^2H^2 - 180H^4 + a''\big(-24a'^2 - 40H^2\big), \\
E_{(2)}{}^{x_5}{}_{x_5} &= 12a'^4 + 168a'^2H^2 - 180H^4 - a''\big(-24a'^2 - 40H^2\big), \\
E_{(2)}{}^{x_8}{}_{x_8} &= 12a'^4 + 168a'^2H^2 - 180H^4, \\
E_{(2)}{}^{x_4}{}_{x_4} &= -36a'^4 - 120a'^2H^2 - 420H^4,
\end{aligned}
$$

$$
\begin{aligned}
E_{(3)}{}^{x_1}{}_{x_1} &= -72a'^6 - 648a'^4H^2 - 1944a'^2H^4 + 360H^6 \\
&\quad + a''\big(360a'^4 + 432a'^2H^2 + 360H^4\big), \\
E_{(3)}{}^{x_5}{}_{x_5} &= -72a'^6 - 648a'^4H^2 - 1944a'^2H^4 + 360H^6 \\
&\quad - a''\big(360a'^4 + 432a'^2H^2 + 360H^4\big), \\
E_{(3)}{}^{x_8}{}_{x_8} &= -72a'^6 - 648a'^4H^2 - 1944a'^2H^4 + 360H^6, \\
E_{(3)}{}^{x_4}{}_{x_4} &= 360a'^6 + 648a'^4H^2 + 1080a'^2H^4 + 2520H^6 .
\end{aligned}
$$

We have only regrouped the record's terms: in each $x_1x_1$ and $x_5x_5$ component we collected the terms that contain $a''$ (Exercise 1 asks you to check this against the record's formulas term by term). The components $x_2x_2$ and $x_3x_3$ equal $x_1x_1$, the components $x_6x_6$ and $x_7x_7$ equal $x_5x_5$, and every off-diagonal component, $x_4x_8$ included, is zero (record: `allOtherComponents`; PROVED, Wolfram report `Revision/field_equations_a4/reports/wolfram-a4-report.json`, check `independent_components`; sympy report `Revision/field_equations_a4/reports/python-a4-report.json`, check `other_components_vanish`).

**A pattern.** Look at the three blocks. For every order $k$ there are two polynomials, $P_k$ in $a'$ and $H$ and $Q_k$ in $a'$ and $H$, such that

$$
E_{(k)}{}^{x_1}{}_{x_1} = P_k + a''Q_k, \qquad E_{(k)}{}^{x_5}{}_{x_5} = P_k - a''Q_k, \qquad E_{(k)}{}^{x_8}{}_{x_8} = P_k ,
$$

namely $P_1 = 15H^2 - 3a'^2$, $Q_1 = 1$; $P_2 = 12a'^4 + 168a'^2H^2 - 180H^4$, $Q_2 = -24a'^2 - 40H^2$; $P_3 = -72a'^6 - 648a'^4H^2 - 1944a'^2H^4 + 360H^6$, $Q_3 = 360a'^4 + 432a'^2H^2 + 360H^4$. We write the weighted sums as

$$
e_{hh} = \sum_{k=1}^{3}\alpha_kE_{(k)}{}^{h}{}_{h}\ (\text{no sum over } h), \qquad \mathcal P = \sum_{k=1}^{3}\alpha_kP_k, \qquad \mathcal Q = \sum_{k=1}^{3}\alpha_kQ_k ,
$$

so that $e_{11} = \mathcal P + a''\mathcal Q$, $e_{55} = \mathcal P - a''\mathcal Q$ and $e_{88} = \mathcal P$.

**The equations.** With these abbreviations the 64 field equations reduce to four diagonal equations and two mixed ones:

$$
\begin{aligned}
&\text{constraint } (x_4): & e_{44} + \Lambda &= -\kappa\rho, \\
&\text{3-space } (x_1 = x_2 = x_3): & \mathcal P + a''\mathcal Q + \Lambda &= \kappa p_3, \\
&\text{extra times } (x_5 = x_6 = x_7): & \mathcal P - a''\mathcal Q + \Lambda &= \kappa p_t, \\
&\text{hidden } (x_8): & \mathcal P + \Lambda &= \kappa p_8, \\
&\text{mixed } (x_4x_8 \text{ and } x_8x_4): & 0 &= \kappa q_{48}, \quad 0 = \kappa q_{84} .
\end{aligned}
$$

The minus sign in the constraint comes from $T^{x_4}{}_{x_4} = -\rho$. Subtracting the extra-time equation from the 3-space equation gives the **evolution equation**:

$$
(\mathcal P + a''\mathcal Q + \Lambda) - (\mathcal P - a''\mathcal Q + \Lambda) = \kappa p_3 - \kappa p_t
$$

(rule: subtract the two equations side by side)

$$
2a''\mathcal Q = \kappa(p_3 - p_t), \qquad\text{that is}\qquad a_4''\,F(a_4') = \kappa(p_3 - p_t),\quad F = 2\mathcal Q
$$

(rule: $\mathcal P$ and $\Lambda$ cancel; $a''\mathcal Q - (-a''\mathcal Q) = 2a''\mathcal Q$). Written out, $F = 2\alpha_1 - \alpha_2(48a'^2 + 80H^2) + \alpha_3(720a'^4 + 864a'^2H^2 + 720H^4)$, the record's `evolution_F` (PROVED: checks `evolution_factorises` of the sympy report and `evolution_factorises_a4pp_times_F` of the Wolfram report). In Einstein gravity $F = 2$ and the evolution equation is $2a_4'' = \kappa(p_3 - p_t)$.

### 17.4 Condition C1: a source must not depend on x8

**The argument.** Read the left-hand side of each equation of Section 17.3. It is built from $a_4'(x_4)$, $a_4''(x_4)$, the constant $H$ and the constants $\alpha_k$ and $\Lambda$; it contains no $x_8$, not even through $\cot z$ or $\sin z$. (The metric itself depends on $x_8$ through $z$; these components of the Lovelock tensors, with one index up and one down, do not. PROVED: Wolfram report, checks `P1_structure`, `P2_structure`, `P3_structure`, which state that each tensor $P_{(k)}$ is diagonal and free of $x_8$; the record defines $E_{(k)} = -P_{(k)}/2^{k+1}$, a constant multiple, so the same holds for $E_{(k)}$ (record `a4-equations.json`, key `conventions.lovelock`); reproduced in Notebook 17a, In [4].) Now take the hidden equation at two points with the same time $x_4$ and two different hidden coordinates $x_8$ and $\tilde x_8$:

$$
\kappa\,p_8(x_4, x_8) = \mathcal P(x_4) + \Lambda = \kappa\,p_8(x_4, \tilde x_8)
$$

(rule: the hidden equation at both points; its left-hand side is the same number at both, because it does not depend on $x_8$)

$$
p_8(x_4, x_8) = p_8(x_4, \tilde x_8)
$$

(rule: divide by $\kappa$, which is not zero). The same three lines with the constraint, the 3-space and the extra-time equations give the same for $\rho$, $p_3$ and $p_t$. The mixed equations say $q_{48} = q_{84} = 0$ outright. So:

**C1.** Every component of an admissible source is independent of $x_8$, and the mixed components $q_{48}$ and $q_{84}$ vanish. (PROVED; record `Revision/field_equations_a4/a4-equations.json`, key `generalSource.x8_dependence`.)

**The same in the coordinate $y$.** The Kohn-Sham states are stored as functions of $y = \ln(\sin z)/(6H)$. By the chain rule

$$
\frac{dy}{dx_8} = \frac{1}{6H}\cdot\frac{\cos z}{\sin z}\cdot 6H = \cot z ,
$$

(rule: the chain rule; the derivative of $\ln u$ is $1/u$ times the derivative of $u$, the derivative of $\sin z$ is $\cos z$, and $dz/dx_8 = 6H$) and $\cot z > 0$ for $0 < z < \pi/2$. So $y$ grows strictly with $x_8$: every value of $y$ belongs to exactly one value of $x_8$. A function that takes different values at two values of $y$ takes different values at the two corresponding values of $x_8$. "Depends on $y$" and "depends on $x_8$" are the same statement.

**How the record measures it.** For a state with a nonzero source the record computes the **spread** of the energy density,

$$
\frac{\max_y\rho - \min_y\rho}{\max|T|} ,
$$

which is $0$ exactly when $\rho$ does not depend on $y$. C1 needs $0$; the record calls a state dependent on $x_8$ when the spread exceeds its tolerance $10^{-6}$.

### 17.5 Condition C2: the algebraic condition

**The derivation.** Add the 3-space and the extra-time equations and subtract twice the hidden equation:

$$
(\mathcal P + a''\mathcal Q + \Lambda) + (\mathcal P - a''\mathcal Q + \Lambda) - 2(\mathcal P + \Lambda) = \kappa p_3 + \kappa p_t - 2\kappa p_8
$$

(rule: add and subtract the equations side by side; the same operation on both sides keeps an equation true)

$$
(\mathcal P + \mathcal P - 2\mathcal P) + (a''\mathcal Q - a''\mathcal Q) + (\Lambda + \Lambda - 2\Lambda) = \kappa(p_3 + p_t - 2p_8)
$$

(rule: collect equal kinds of terms on the left; take out the common factor $\kappa$ on the right)

$$
0 = \kappa(p_3 + p_t - 2p_8)
$$

(rule: each bracket on the left is zero). Divided by $\kappa \ne 0$:

**C2.** Every admissible source has $p_3 + p_t = 2p_8$ at every point and every time. (PROVED; Wolfram report, check `algebraic_identity_x1_plus_x5_minus_2x8`; sympy report, check `algebraic_identity`; reproduced in Notebook 17a, In [4].)

**Remarks.** C2 holds for every choice of the couplings $\alpha_k$, of $\Lambda$ and of the history $a_4$: it is a condition on the matter alone. It does not involve the energy density. For Einstein gravity the identity behind it is a two-line computation: $(15H^2 - 3a'^2 + a'') + (15H^2 - 3a'^2 - a'') - 2(15H^2 - 3a'^2) = 30H^2 - 6a'^2 - 30H^2 + 6a'^2 = 0$. We call

$$
V = p_3 + p_t - 2p_8
$$

the **violation** of C2. The record measures its size by $\max_y|V|/\max|T|$ and, for a source averaged over the hidden direction, by the ratio $R = (\int p_3 + \int p_t)/(2\int p_8)$, which an averaged source satisfying C2 would have equal to 1.

### 17.6 Condition C3: what the linear member demands

**The linear member.** For $a_4 = AHx_4 + a_0$:

$$
a_4' = AH, \qquad a_4'' = 0
$$

(rule: the derivative of $AHx_4 + a_0$ is the constant $AH$, and the derivative of a constant is $0$).

**The pressures are equal.** The evolution equation of Section 17.3 becomes

$$
0\cdot F(AH) = \kappa(p_3 - p_t) \quad\Longrightarrow\quad p_3 = p_t
$$

(rule: insert $a_4'' = 0$; zero times any number is zero; divide by $\kappa$). With C2:

$$
p_3 + p_3 = 2p_8 \quad\Longrightarrow\quad p_8 = p_3
$$

(rule: insert $p_t = p_3$ into $p_3 + p_t = 2p_8$ and divide by 2). So $p_3 = p_t = p_8$; we call the common value $p$.

**The energy density and the pressure are constant.** In the constraint, $e_{44} = \sum_k\alpha_kE_{(k)}{}^{x_4}{}_{x_4}$ contains only $a'$ and $H$ (Section 17.3), and $a' = AH$ is a constant. So $-\kappa\rho = e_{44}(AH) + \Lambda$ is the same number at every time. In the same way the hidden equation gives $\kappa p = \mathcal P(AH) + \Lambda$, the same number at every time.

**C3.** Along the linear member $a_4 = AHx_4 + a_0$ an admissible source has $p_3 = p_t = p_8$, and $\rho$ and these pressures do not change with $x_4$. (PROVED; sympy and Wolfram reports, check `linear_member_equal_pressures`; reproduced in Notebook 17a, In [4].) In Einstein gravity the record gives the values: $\kappa\rho = -(21 + 3A^2)H^2 - \Lambda$ and $\kappa p = (15 - 3A^2)H^2 + \Lambda$ (record `a4-equations.json`, keys `linearMember.rhoEinstein` and `linearMember.pEinstein`). For the history of the Kohn-Sham computations, $A = 1$, this is $\kappa\rho = -24H^2 - \Lambda$ and $\kappa p = 12H^2 + \Lambda$.

**What C3 asks of a gas.** A gas on the linear history must keep its energy density constant while 3-space inflates and the extra times deflate, and it must push equally hard along 3-space, along the extra times and along the hidden direction, at every instant. Section 17.16 shows that the first demand follows from the second: once the pressures $p_3$ and $p_t$ are equal, conservation keeps $\rho$ constant.

**No source at all.** Could the empty source $T = 0$ be admissible? In Einstein gravity the constraint and the hidden equation read $3a'^2 + 21H^2 + \Lambda = -\kappa\rho$ and $15H^2 - 3a'^2 + \Lambda = \kappa p_8$. With $\rho = p_8 = 0$:

$$
(3a'^2 + 21H^2 + \Lambda) - (15H^2 - 3a'^2 + \Lambda) = 0 - 0
$$

(rule: subtract the second equation from the first, with $\rho = p_8 = 0$ on the right)

$$
6a'^2 + 6H^2 = 0
$$

(rule: $\Lambda - \Lambda = 0$, $3a'^2 + 3a'^2 = 6a'^2$, $21H^2 - 15H^2 = 6H^2$). A square of a real number is never negative, and $6H^2 > 0$ for $H > 0$, so the left side is positive: there is no solution. (PROVED; Wolfram report, check `einstein_no_vacuum_solution`; reproduced in Notebook 17a, In [19].) The author's metric always needs matter.

### 17.7 The recorded Kohn-Sham states as a candidate source

**What was computed.** The Revision Rust solver (Chapter 15) computed, at each slice $a_{4,0}$ of the history $a_4 = Hx_4$, the self-consistent Kohn-Sham ground state of $N$ quanta of dirac16complex in the author's metric with $a_4$ held at its slice value $a_{4,0}$ (the stationary-slice, adiabatic ansatz of Chapter 14; between the slices the extra times keep deflating). It used the good sector (no dependence on the extra times), the Z2 mirror at the brane and the tip cutoff at $y = -3$, all ASSUMED (Chapter 14). The recorded states are all combinations of

- three particle numbers: $N = 8$ (the eight brane zero modes, the levels of zero 3-momentum and zero energy) and the closed shells $N = 136$ and $N = 688$ (record `Revision/kohn_sham/results/parameters.json`, key `particleNumbers`);
- five couplings: $\lambda = 0$, $\pm\lambda_1$ and $\pm\lambda_2$, chosen for each $N$ so that the largest first-order mean-field potential along the whole history is about $0.1\,m$ and $0.3\,m$ (the same file, key `couplingCalibration`; $\lambda$ is rounded to four digits, so the recorded values lie very slightly above: for $N = 8$, $\lambda_1 = 0.01946$ and $\lambda_2 = 0.05838$ give $0.1000011\,m$ and $0.3000034\,m$);
- five slices: $a_{4,0} = 0, 0.5, 1, 1.5, 2$.

That makes $3 \times 5 \times 5 = 75$ states.

**What is stored for each state.** A **profile** file `Revision/kohn_sham/results/ground/profiles/<name>.csv` with the proper densities at the 151 points $y = -3, -2.98, \dots, 0$ (step $0.02$), among them the four columns `rho`, `p3`, `p_t`, `p8`; and a row of the table `Revision/kohn_sham/results/ground/emt-integrals.csv` with the integrals over the patch, the values at the brane and at the tip, and check columns of the solver.

**Why the profiles can be compared with the field equations directly.** The field equations use $T^\mu{}_\nu$ with one index up and one down. In the frame of rulers (the diagonal vielbein of Chapter 6) a component is $T^a{}_b = e^a{}_\mu\,e_b{}^\nu\,T^\mu{}_\nu$, and for a diagonal vielbein a diagonal component picks up one factor and its inverse: $T^a{}_a = T^\mu{}_\mu$ (no sum). So the proper densities of the profiles are exactly the $\rho$, $p_3$, $p_t$, $p_8$ of the field equations.

**The Kohn-Sham source in words.** The record `Revision/kohn_sham/ks-theory.json` (key `emt`) gives the four components as sums over the occupied orbitals. Two facts matter here. First, $p_t = e_{\rm int}$, the interaction energy density: in the good sector no orbital moves along the extra times, so there is no extra-time kinetic pressure; for $\lambda = 0$ the interaction vanishes and $p_t = 0$ exactly. Second, $p_3$ is the kinetic pressure of the motion along 3-space plus $e_{\rm int}$, so for a gas whose quanta move along 3-space $p_3$ is in general not zero; for the recorded states with $\lambda = 0$ its integral over the patch is positive at every slice (Notebook 17a, In [16] and figure 7). The mixed component, there written $T^{x_4}{}_y$, vanishes for every eigen-orbital (key `emt.offDiagonal`), so the Kohn-Sham states meet the part $q_{48} = q_{84} = 0$ of C1. The question is the dependence on $x_8$, and conditions C2 and C3.

**The integral over the patch.** A small region of the hidden direction between $y$ and $y + dy$, times the coordinate box of 3-space and of the extra times, has the proper 7-volume

$$
dV_7 = \sqrt{|g|}\;d^3x\,d^3x_t\,dy = e^{6Hy}\,\ell^3v_t\,dy = \mathrm{Vol}_7\,e^{6Hy}\,dy
$$

(rule: in the coordinate $y$ the product of the seven scale factors other than that of the time is $(e^{a_4}e^{Hy})^3(e^{-a_4}e^{Hy})^3\cdot 1 = e^{6Hy}$, Chapter 14; the coordinate box of 3-space is a cube of side $\ell$ and that of the extra times has the coordinate volume $v_t$). The runs use $\ell = 8\pi$ (from the momentum spacing $\Delta k = 2\pi/\ell = 0.25$) and $v_t = 1$, so $\mathrm{Vol}_7 = (8\pi)^3 = 512\pi^3 \approx 15875.2$ (record `parameters.json`, key `physics.Vol7`). The total amount of a density $X$ in the patch and its mirror copy is therefore

$$
\int X \;=\; 2\,\mathrm{Vol}_7\int_{-3}^{0}e^{6Hy}\,X(y)\,dy ,
$$

the columns `int_rho`, `int_p3`, `int_p_t`, `int_p8` of the table. The factor 2 counts the mirror copy of the ASSUMED Z2 brane. For $X = \rho$ the integral is the energy $E$ of the Kohn-Sham state (`ks-theory.json`, key `emt.integrated`). The proper volume of the patch and its copy is

$$
2\,\mathrm{Vol}_7\int_{-L}^{0}e^{6Hy}\,dy = 2\,\mathrm{Vol}_7\left[\frac{e^{6Hy}}{6H}\right]_{-L}^{0} = 2\,\mathrm{Vol}_7\,\frac{1 - e^{-6HL}}{6H}
$$

(rule: an antiderivative of $e^{cy}$ is $e^{cy}/c$; then the fundamental theorem of calculus, upper value minus lower value, with $e^0 = 1$). The **weighted mean** of $X$ is the amount divided by the volume:

$$
\bar X = \frac{\int X}{2\,\mathrm{Vol}_7\,(1 - e^{-6HL})/(6H)} .
$$

Note how fast the weight $e^{6Hy}$ falls toward the tip: at $y = -L = -3$ (with $H = 1$) it is $e^{-18} \approx 1.5 \times 10^{-8}$.

**The prediction of the conditions.** C1 asks for flat profiles, C2 for $V = 0$ at every point (or, averaged, $R = 1$), C3 for a constant $\int\rho$ along the history and equal pressures. Notebook 17a checks each against the record.

### 17.8 Example: the three conditions tested on 75 recorded states

The first notebook derives the three conditions from the Lovelock components stored in the record, with exact computer algebra; reads the 75 recorded states; and reproduces every number of the five checks of `Revision/field_equations_a4/reports/ks-source-conditions.json`. It prints 16 PASS lines and draws seven figures: the hidden coordinate and the energy profiles; a heat map of the spread of $\rho$ (C1); the violation profiles and a heat map of their size (C2); three points of one state as bars; the averaged ratio $R$; and the integrals along the history (C3). It runs in about 15 seconds on a typical laptop and needs no Rust.

<!-- NOTEBOOK 17a -->

### 17.11 Line-by-line walk-through of Notebook 17a

The notebook has 20 code cells, In [1] to In [20]. This section explains every line of every one of them, in order: a line or a small group of lines is quoted, then explained. Where a line repeats a pattern already explained, we say so and explain only what is new. Each figure is described after the cell that draws it.

**In [1], the set-up cell.** Every line that starts with `#` is a **comment**: Python skips it. The comment lines at the top of the cell are the complete run instructions of Section 17.9, so that the notebook file carries its own instructions even when it is copied without the book. The code starts after the comment line that announces THE SET-UP (the same in every notebook of this book; it computes no physics).

```python
import json  # reads and writes JSON files (text files that hold names and numbers)
import os  # reads the environment variable TEXTBOOK_OUTPUT_ROOT (explained below)
import textwrap  # breaks long printed text into lines of at most 89 characters
from pathlib import Path  # file and folder paths that work on Windows, macOS and Linux
```

`import` loads a **module**, a part of Python or of an installed package, so that the code may use it. `json`, `os`, `textwrap` and `pathlib` come with Python. `from pathlib import Path` takes the single name `Path` out of the module `pathlib`; a `Path` is the address of a file or folder, written the same way on every operating system. The text after `#` on each line is a comment.

```python
import matplotlib  # the plotting package
import matplotlib.pyplot as plt  # its drawing functions, called plt by convention
from IPython.display import Image, display  # shows a saved picture below a cell
```

These load the plotting package matplotlib, its drawing functions under the short name `plt`, and the two functions `Image` and `display` of IPython (the part of Jupyter that runs Python), which show a picture file below a cell.

```python
NOTEBOOK_ID = "17a"  # this notebook: chapter 17, example a
```

A **variable** is a name for a value. This line gives the name `NOTEBOOK_ID` to the **string** (a text in quotation marks) `"17a"`. The figure files and the last line of the notebook are named after it.

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

`def` defines a **function**: a named piece of code that runs each time it is called. The text in triple quotation marks under the `def` line is its **docstring**, a description that Python stores but does not run. `Path.cwd()` is the folder in which Jupyter runs the notebook, and `.resolve()` writes it as a complete address. `here.parents` lists the folders above it; `[here, *here.parents]` is a **list** (an ordered collection in square brackets) that starts with `here` and continues with those folders (the star unpacks one list into another). The `for` loop visits the folders one after the other. The operator `/` joins a folder and a name into a longer path, and `.is_file()` is true when that file exists. The first folder that contains `Revision/textbook/requirements.txt` is the repository, and `return` hands it back to the caller. If no folder does, `raise` stops the notebook with a `FileNotFoundError` whose message says what to do.

```python
# The repository folder.  It is never printed: it differs from computer to computer,
# and the printed output of a notebook must not.
REPO = find_repository_root()
# Every file is WRITTEN below OUTPUT_ROOT.  OUTPUT_ROOT is the repository folder unless
# the environment variable TEXTBOOK_OUTPUT_ROOT names another folder; the book's
# checking tool sets it, so that a check run writes into a scratch folder instead.
OUTPUT_ROOT = Path(os.environ.get("TEXTBOOK_OUTPUT_ROOT", str(REPO)))
```

The first code line calls the function and names its result `REPO`. The second chooses where files are written: `os.environ` holds the **environment variables** of the program (named texts it receives from the computer), and `.get(name, default)` returns the value of `TEXTBOOK_OUTPUT_ROOT` if it is set and `str(REPO)` (the repository folder as a string) otherwise. When you run the notebook the variable is not set, so files go into the repository; the book's checking tool sets it to a scratch folder.

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

Two small functions. `repository_file` gives the full path of a file of the repository, for reading a Revision record. `output_file` gives the full path at which to write a file; `path.parent.mkdir(parents=True, exist_ok=True)` first creates the folder of the file and every missing folder above it, and does nothing if they exist.

```python
def say(text):
    """Print text in lines of at most 89 characters (the width of a page of the book)."""
    print(textwrap.fill(str(text), width=89, subsequent_indent="    "))
```

`say` prints a text in lines of at most 89 characters; `textwrap.fill` breaks the text at blanks and starts every line after the first with four blanks. That is why long printed lines of this notebook continue on an indented second line.

```python
matplotlib.rcdefaults()  # ignore personal matplotlib settings: same figures everywhere
plt.rcParams.update({"figure.figsize": (7.0, 4.2), "font.size": 10.0,
                     "axes.grid": True, "grid.alpha": 0.3})
```

`matplotlib.rcdefaults()` returns to the built-in settings of matplotlib, so that the figures are the same on every computer. `plt.rcParams.update({...})` then sets the default size of a figure (7.0 by 4.2 inches), the size of its letters (10 points) and a faint grid (`grid.alpha` 0.3 means 30 per cent opaque). The braces make a **dictionary**: pairs `key: value`.

```python
FIGURE_FOLDER = "Revision/textbook/figures"  # where the figures are saved
CAPTION_FILE = f"{FIGURE_FOLDER}/{NOTEBOOK_ID}.captions.json"  # their captions
FIGURE_NUMBERS = {}  # figure name -> its number k (file name <id>_<k>_<name>.png)
CAPTIONS = {}  # figure file name -> caption, written to CAPTION_FILE after every figure
# Start with an empty captions file ({} is an empty JSON dictionary); save_figure fills
# it.  newline="\n" writes the same line ends on Windows, macOS and Linux.
output_file(CAPTION_FILE).write_text("{}\n", encoding="utf-8", newline="\n")
```

A string that starts with `f` is an **f-string**: a name in braces is replaced by its value, so `CAPTION_FILE` is `"Revision/textbook/figures/17a.captions.json"`. `FIGURE_NUMBERS` and `CAPTIONS` start as empty dictionaries. The last line writes an empty JSON dictionary and a line end into the captions file; `encoding="utf-8"` fixes how letters are stored as bytes and `newline="\n"` stores the same line end on every system.

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

`setdefault(name, value)` returns the number already stored for this figure name, or stores and returns `len(FIGURE_NUMBERS) + 1`, one more than the number of figures so far: the figures are numbered 1, 2, 3, and a cell run twice keeps its number. The file name joins the notebook id, the number and the name, for example `17a_1_rho_profiles.png`. `fig.savefig` writes a PNG picture with 150 dots per inch, cuts away the empty margin and stores no program name, so that two runs write the same bytes. `plt.close(fig)` removes the figure from memory, because Jupyter would otherwise draw it a second time. The caption is stored, the whole dictionary is written to the captions file (`json.dumps` turns it into JSON text with sorted keys), `display(Image(...))` shows the saved picture below the cell, and the last line prints where it was saved.

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

`PASSED` starts as an empty list. `check` is the function behind every check of the notebook. If `condition` is false, `raise AssertionError(...)` stops the notebook with an error that names the check. Otherwise the name is appended to `PASSED`, the line PASS name is printed, and, when `record` is given, a second line names the Revision record that the check reproduces. `record=None` makes that argument optional.

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

`report` prints a key number as a line that starts with RESULT; `(f" {unit}" if unit else "")` adds the unit only when one is given. `all_checks_passed` prints the last line of the notebook; `len(PASSED)` is the number of checks that passed. The last statement prints the one output line of In [1]: Set-up of notebook 17a complete.

**In [2], the Revision records and the helpers that read them.**

```python
import csv  # reads tables stored as CSV files (comma-separated values)

import numpy as np  # arrays of numbers
import sympy as sp  # exact algebra with symbols
```

`csv` comes with Python and reads tables stored as text with commas between the entries. numpy (short name `np`) works with **arrays**, tables of numbers on which arithmetic acts entry by entry. sympy (short name `sp`) does exact algebra with symbols.

```python
SOURCE_REPORT = "Revision/field_equations_a4/reports/ks-source-conditions.json"
EQUATIONS = "Revision/field_equations_a4/a4-equations.json"  # the a4 equations
PY_A4 = "Revision/field_equations_a4/reports/python-a4-report.json"  # sympy checks
WL_A4 = "Revision/field_equations_a4/reports/wolfram-a4-report.json"  # Wolfram
GROUND = "Revision/kohn_sham/results/ground"  # the 75 Kohn-Sham ground states
```

Five names for the Revision records used below: the record on the Kohn-Sham source conditions (the record this notebook reproduces), the record of the $a_4$ equations, its two verification reports (sympy and Wolfram), and the folder of the recorded Kohn-Sham ground states.

```python
def read_json(relative):
    """Read a JSON file of the repository (a Revision record)."""
    return json.loads(repository_file(relative).read_text(encoding="utf-8"))


def record_entry(report_file, name):
    """The entry {name, verdict, detail} of a check of a report, None if absent."""
    for entry in read_json(report_file)["checks"]:
        if entry["name"] == name:
            return entry
    return None
```

`read_json` reads a JSON file of the repository as text and turns it into Python dictionaries and lists (`json.loads`). Every Revision report has a list `checks` whose entries have a `name`, a `verdict` (PASS or FAIL) and a `detail` text. `record_entry` walks through that list and returns the entry with the given name; `None` (Python's "nothing") if there is none.

```python
def reproduces(condition, name, report_file, record_names):
    """A check that also requires the named checks of the report to be PASS."""
    found = all((record_entry(report_file, n) or {}).get("verdict") == "PASS"
                for n in record_names)
    names_text = ", ".join(record_names)  # the check names, separated by commas
    check(condition and found, name, record=f"{report_file}, check {names_text}")
```

`reproduces` is the check used whenever a result of the notebook reproduces a Revision record. `all(... for n in record_names)` is true when the expression holds for every name in the list. For one name, `record_entry(...) or {}` is the entry, or an empty dictionary if the entry is missing; `.get("verdict")` reads its verdict (or `None`). So `found` is true only when every named check of the report exists and has the verdict PASS. `", ".join(...)` joins the names with commas. The check passes only when the notebook's own `condition` holds AND the record agrees; its second printed line names the report and the checks.

```python
def tex_number(value, digits=2):
    """A number for a caption in powers of ten: 0.0123 -> 1.2 \\times 10^{-2}."""
    mantissa, exponent = f"{value:.{digits - 1}e}".split("e")
    return f"{mantissa} \\times 10^{{{int(exponent)}}}"
```

`tex_number` writes a number in powers of ten for the captions. The format `.1e` (here `digits - 1 = 1`) writes `0.0123` as `1.2e-02`; `.split("e")` cuts this text at the letter e into `"1.2"` and `"-02"`; `int("-02")` is the whole number $-2$. The result is the text `1.2 \times 10^{-2}`, which the book prints as $1.2 \times 10^{-2}$. (In a Python string a backslash is written twice, and in an f-string a brace is written twice, so `{{{...}}}` gives one literal brace around the value.)

```python
source_record = read_json(SOURCE_REPORT)
summary = source_record["summary"]  # how many checks the record has, how many pass
passed, total = summary["pass"], summary["checks"]
report("checks of the record ks-source-conditions.json", f"{passed} of {total} PASS")
say("its conclusion: " + source_record["conclusion"])
check(summary == {"checks": 5, "pass": 5, "fail": 0},
      "the record on the Kohn-Sham source conditions has 5 checks, all PASS")
```

The record is read; its `summary` dictionary says how many checks it has and how many passed. `passed, total = a, b` gives two names at once. The cell prints the count and the record's conclusion, and checks that the record has 5 checks, all PASS. Output: RESULT checks of the record ks-source-conditions.json = 5 of 5 PASS, the record's conclusion (no recorded Kohn-Sham state is an admissible source; C1 and C2 fail for every nonzero state, C2 also after integration over $x_8$; the history is a prescribed background without back-reaction), and the first PASS line.

**In [3], the Lovelock components of the record as sympy expressions.**

```python
equations = read_json(EQUATIONS)
ad1, ad2 = sp.symbols("ad1 ad2", real=True)  # a4' and a4'' (the record's names)
H = sp.symbols("H", positive=True)  # the constant H of the metric
NAMES = {"ad1": ad1, "ad2": ad2, "H": H}  # how the record's names become symbols
```

The record of the $a_4$ equations is read. `sp.symbols` makes sympy **symbols**, letters that sympy computes with exactly: `ad1` and `ad2` stand for $a_4'$ and $a_4''$ and are declared real numbers; `H` is declared positive. `NAMES` tells sympy which symbol each name of the record means.

```python
def parse(text):
    """A formula of the record (Wolfram Language text) as a sympy expression."""
    return sp.sympify(text.replace("^", "**"), locals=NAMES)
```

The record stores its formulas as text in the Wolfram Language, where a power is written `^`; Python writes `**`. `parse` replaces the one by the other and lets `sp.sympify` read the text as a sympy expression, with the names of `NAMES`.

```python
COMPONENTS = ("x1x1", "x4x4", "x5x5", "x8x8", "x4x8")
E = {k: {c: parse(equations["lovelockTensors"][f"E{k}"][c]["input"])
         for c in COMPONENTS}
     for k in (1, 2, 3)}  # E[k][component]: the Lovelock tensor of order k
for c in COMPONENTS:
    say(f"E_(1)^{c[:2]}_{c[2:]} = {E[1][c]}")
```

`COMPONENTS` is a **tuple** (a fixed list in round brackets) of the five components needed. The next line is a **dictionary comprehension** inside another: for each order $k = 1, 2, 3$ and each component `c` it reads the record's text `equations["lovelockTensors"]["E1"]["x1x1"]["input"]` (and so on) and parses it. `E[2]["x5x5"]` is then $E_{(2)}{}^{x_5}{}_{x_5}$. The loop prints the five components of Einstein's tensor; `c[:2]` is the first two characters of the name (`x1`) and `c[2:]` the rest. Output: `E_(1)^x1_x1 = 15*H**2 - 3*ad1**2 + ad2`, `E_(1)^x4_x4 = 21*H**2 + 3*ad1**2`, `E_(1)^x5_x5 = 15*H**2 - 3*ad1**2 - ad2`, `E_(1)^x8_x8 = 15*H**2 - 3*ad1**2` and `E_(1)^x4_x8 = 0`, the Einstein components of Section 17.3.

**In [4], the three conditions on the left-hand sides.**

```python
allowed = {ad1, ad2, H}  # the only symbols a left-hand side may contain
no_x8 = all(E[k][c].free_symbols <= allowed for k in E for c in COMPONENTS)
reproduces(no_x8 and all(E[k]["x4x8"] == 0 for k in E),
           "C1: the left-hand sides are free of x8 and the x4-x8 one is 0",
           WL_A4, ["P1_structure", "P2_structure", "P3_structure"])
```

`{ad1, ad2, H}` is a **set**, a collection without order. `.free_symbols` is the set of symbols that an expression contains, and `<=` between sets means "is contained in". So `no_x8` is true when no component of any order contains anything but $a_4'$, $a_4''$ and $H$. (A dependence on $x_8$ would have to appear as a symbol such as `x8` or `cc`.) Together with "every $x_4x_8$ component is zero" this is the left-hand side of C1 (Section 17.4); the check also requires the three structure checks of the Wolfram report to be PASS.

```python
identity = [sp.expand(E[k]["x1x1"] + E[k]["x5x5"] - 2 * E[k]["x8x8"]) for k in E]
say(f"E^x1_x1 + E^x5_x5 - 2 E^x8_x8 for k = 1, 2, 3: {identity}")
reproduces(all(value == 0 for value in identity),
           "C2: E^x1_x1 + E^x5_x5 = 2 E^x8_x8 for every order k",
           WL_A4, ["algebraic_identity_x1_plus_x5_minus_2x8"])
```

For each order, `sp.expand` multiplies out $E^{x_1}{}_{x_1} + E^{x_5}{}_{x_5} - 2E^{x_8}{}_{x_8}$ and collects equal terms. The printed list is `[0, 0, 0]`: the identity behind C2 (Section 17.5) holds for each order separately.

```python
linear = {ad2: 0}  # the linear member: a4'' = 0 (and a4' = A H, a constant)
equal = all(sp.expand((E[k]["x1x1"] - E[k]["x8x8"]).subs(linear)) == 0
            and sp.expand((E[k]["x5x5"] - E[k]["x8x8"]).subs(linear)) == 0
            for k in E)
rho_side = all(E[k]["x4x4"].free_symbols <= {ad1, H} for k in E)
reproduces(equal and rho_side,
           "C3: for a4'' = 0 the pressures are equal and rho is constant",
           PY_A4, ["linear_member_equal_pressures"])
```

`.subs(linear)` replaces $a_4''$ by 0. Then `equal` is true when, for every order, the $x_1$ and $x_5$ components both equal the $x_8$ component; so the three pressure equations have the same left-hand side and give $p_3 = p_t = p_8$. `rho_side` is true when the $x_4$ components contain only $a_4'$ and $H$; with $a_4' = AH$ constant the constraint then gives a constant $\rho$. That is C3 (Section 17.6), reproduced from the sympy report. Output: three PASS lines, each followed by the record it reproduces.

**In [5], the recorded Kohn-Sham states.**

```python
COLUMNS = ("rho", "p3", "p_t", "p8")  # the four diagonal components of the source


def read_profile(path):
    """A profile table as a dictionary: column name -> numpy array (151 values)."""
    data = np.genfromtxt(path, delimiter=",", names=True)
    return {name: data[name] for name in data.dtype.names}
```

`COLUMNS` names the four columns of a profile file that hold the source. `np.genfromtxt` reads a table of numbers from a text file; `delimiter=","` says that commas separate the entries, and `names=True` that the first line holds the column names. `data.dtype.names` lists them, and the function returns a dictionary from each name to its column, an array of 151 numbers.

```python
files = sorted(repository_file(f"{GROUND}/profiles").glob("*.csv"),
               key=lambda path: path.name)  # in alphabetical order, as the record
profiles = {path.stem: read_profile(path) for path in files}
```

`.glob("*.csv")` finds every file whose name ends in `.csv` in the folder of profiles; `sorted(..., key=lambda path: path.name)` puts them in alphabetical order of their names (a `lambda` is a one-line function without a name; here it returns the file name). `path.stem` is the file name without `.csv`, the name of the state, such as `N136_lam0_a10`. So `profiles["N136_lam0_a10"]["p8"]` is the hidden pressure of that state at the 151 points.

```python
with repository_file(f"{GROUND}/emt-integrals.csv").open(
        encoding="utf-8", newline="") as handle:
    integrals = {row["id"]: row for row in csv.DictReader(handle)}
physics = read_json("Revision/kohn_sham/results/parameters.json")["physics"]
```

`with ... as handle:` opens the table of integrals and closes it again at the end of the indented block. `csv.DictReader` reads it row by row, each row as a dictionary from the column name to the entry (as text); `integrals` maps the state name in the column `id` to its row. `physics` is the part of the solver's parameter record with $H$, the tip cutoff and $\mathrm{Vol}_7$.

```python
scale = {sid: float(max(np.max(np.abs(prof[c])) for c in COLUMNS))
         for sid, prof in profiles.items()}  # max|T| of every state
zero = [sid for sid in profiles if scale[sid] == 0.0]  # T = 0 everywhere
nonzero = [sid for sid in profiles if scale[sid] > 0.0]
```

For each state (`sid`, the state's name, and `prof`, its profile), `np.abs` takes absolute values entry by entry, `np.max` the largest of a column, and `max(...)` the largest of the four columns: this is max|T|. A **list comprehension** `[sid for sid in profiles if ...]` collects the names that satisfy a condition: `zero` holds the states whose tensor vanishes everywhere, `nonzero` the others.

```python
y = profiles["N136_lam0_a10"]["y"]  # the grid of the hidden coordinate
same_grid = all(np.array_equal(prof["y"], y) for prof in profiles.values())
report("states read", len(profiles))
report("states with a nonzero tensor", len(nonzero))
report("grid of y", f"{len(y)} points from {y[0]:g} to {y[-1] + 0.0:g}, "
       f"step {y[1] - y[0]:.2f}")
```

`y` is the column of grid points of one state; `np.array_equal` checks that every state uses exactly the same points. `y[0]` is the first point and `y[-1]` the last (a negative index counts from the end). The last point is stored as $-0$ (a zero with a minus sign, which a computer can hold); adding `0.0` turns it into $+0$, so that it prints as 0. The format `:g` writes a number in its shortest form and `:.2f` with two decimals.

```python
H_value, L_cut, VOL7 = physics["H"], physics["L_tipCutoff"], physics["Vol7"]
report("H, tip cutoff L, Vol_7", f"{H_value:g}, {L_cut:g}, {VOL7:.6g}")
say("ks-theory.json, emt.offDiagonal: "
    + read_json("Revision/kohn_sham/ks-theory.json")["emt"]["offDiagonal"])
check(len(profiles) == 75 and len(nonzero) == 70 and len(zero) == 5 and same_grid
      and sorted(integrals) == sorted(profiles),
      "75 states on one grid (70 nonzero, 5 zero); every state has its integrals")
```

The three numbers of the run are read and printed; `:.6g` keeps six significant digits. The cell prints the Kohn-Sham theory record's statement on the mixed component, and checks the counts, the common grid, and that the table of integrals has exactly the same states (`sorted` of a dictionary is the sorted list of its keys). Output: 75 states, 70 with a nonzero tensor, 151 points from $-3$ to $0$ with step $0.02$; $H = 1$, $L = 3$, $\mathrm{Vol}_7 = 15875.2$; the statement that $T^{x_4}{}_y = 0$ for eigen-orbitals; and a PASS line.

**In [6], the hidden coordinate and the energy profiles (figure 1).**

```python
SLICES = {"a00": 0.0, "a05": 0.5, "a10": 1.0, "a15": 1.5, "a20": 2.0}  # a4,0
SHADES = ["#86b6ef", "#5598e7", "#2a78d6", "#1c5cab", "#104281"]  # light -> dark
history136 = [f"N136_lam0_{tag}" for tag in SLICES]  # N = 136, lambda = 0
```

`SLICES` maps the slice tag of a state name to the value $a_{4,0}$. `SHADES` are five colours from light to dark blue, written as **hexadecimal colour codes** (two digits each for red, green and blue). `history136` lists the five states with $N = 136$, $\lambda = 0$; a loop over a dictionary visits its keys in the order they were written.

```python
falls = [float(np.max(profiles[s]["rho"]) / np.min(profiles[s]["rho"]))
         for s in history136]  # how much rho changes along y, slice by slice
check(all(float(np.min(profiles[s]["rho"])) > 0.0 for s in history136),
      "N = 136, lambda = 0: rho is positive at every point of every slice")
```

For each of the five states, `falls` holds the ratio of the largest to the smallest value of $\rho$ along $y$. The check confirms that $\rho$ is positive everywhere for these states, which a logarithmic axis needs (the logarithm of zero or of a negative number does not exist). Output: the PASS line.

```python
z = np.logspace(-9, np.log10(np.pi / 2), 400)  # z from 1e-9 to pi/2
z_tip = float(np.arcsin(np.exp(-18.0)))  # where y = -3 (6 H y = -18 with H = 1)
```

`np.logspace(a, b, 400)` gives 400 numbers from $10^a$ to $10^b$, equally spaced on a logarithmic scale: here from $10^{-9}$ to $\pi/2$. The tip cutoff $y = -3$ sits where $\sin z = e^{6Hy} = e^{-18}$, that is $z = \arcsin(e^{-18})$, about $1.5 \times 10^{-8}$.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.8))
left.plot(z, np.log(np.sin(z)) / 6.0, color="#2a78d6", lw=2.0)
left.axvspan(z_tip, np.pi / 2, color="#1baf7a", alpha=0.15,
             label="computed patch, $-3 \\leq y \\leq 0$")
left.axhline(-3.0, color="0.4", ls="--", lw=1.0)
left.set_xscale("log")
left.set_xlabel("$z = 6Hx_8$ (logarithmic axis)")
left.set_ylabel("hidden coordinate $y$ (units of $1/H$)")
left.set_title("$y = \\ln(\\sin z)/(6H)$, $H = 1$")
left.legend(loc="lower right", fontsize=8)
```

`plt.subplots(1, 2, ...)` makes a figure with one row of two panels (called **axes** in matplotlib), 9.0 by 3.8 inches; the two panels are named `left` and `right`. The left panel draws $y = \ln(\sin z)/6$ (with $H = 1$) against $z$; `lw` is the line width. `axvspan` shades the vertical band from the tip cutoff to $\pi/2$, the computed patch, with 15 per cent opacity; `axhline` draws a dashed grey horizontal line (the line style `ls` given as two hyphens) at $y = -3$. `set_xscale("log")` makes the horizontal axis logarithmic. The labels and the title are written with `$...$`, which matplotlib prints as mathematics (a backslash is written twice inside a Python string). `legend` shows the label of the shaded band.

```python
for shade, sid, a40 in zip(SHADES, history136, SLICES.values()):
    right.plot(y, profiles[sid]["rho"] / scale[sid], color=shade, lw=1.8,
               label=f"$a_{{4,0}} = {a40:g}$")
right.axhline(1e-3, color="0.4", ls=":", lw=1.2,
              label="admissible: constant (example)")
right.set_yscale("log")
right.set_xlabel("hidden coordinate $y$ (tip $-3$, brane $0$)")
right.set_ylabel("$\\rho(y)$ / max|T|")
right.set_title("$N = 136$, $\\lambda = 0$")
right.legend(fontsize=7, loc="upper right")
fig.tight_layout()
```

`zip` walks through three lists side by side: a colour, a state name and its slice value. Each pass draws $\rho(y)$ divided by max|T| of the state. A dotted line (`ls=":"`) at $10^{-3}$ shows, as an example, what an admissible profile looks like: a constant. `set_yscale("log")` makes the vertical axis logarithmic. `fig.tight_layout()` arranges the panels so that their labels do not overlap.

```python
save_figure(fig, "rho_profiles",
            "Left: the hidden coordinate $y = \\ln(\\sin z)/(6H)$ against $z = 6Hx_8$ "
            "(logarithmic axis, $H = 1$); the shaded band is the computed patch from "
            "the tip cutoff $y = -3$ to the brane $y = 0$, which covers $z$ from "
            f"${z_tip / 1e-8:.1f} \\times 10^{{-8}}$ to $\\pi/2$. Right: the energy "
            "density $\\rho(y)$ of the Kohn-Sham state $N = 136$, $\\lambda = 0$ "
            "divided by the largest component of the state, at the five slices "
            "$a_{4,0} = 0$ to $2$ (logarithmic vertical axis). The largest value of "
            f"$\\rho$ is {min(falls):.0f} to ${tex_number(max(falls))}$ times its "
            "smallest "
            "value, depending on the slice, while condition C1 of the field "
            "equations demands a horizontal line such as the dotted one.")
```

`save_figure` saves the figure and records the caption. The caption is written as twelve strings next to each other, one per line inside the round brackets; Python joins strings written next to each other into one string, so the twelve lines make one caption. Most of them are plain strings. Two start with `f` and contain computed numbers in braces: `z_tip / 1e-8` written with one decimal (`:.1f`) gives 1.5, so the text reads $1.5 \times 10^{-8}$ (the doubled braces `{{-8}}` print one pair of braces, which the book's mathematics needs); `min(falls)` with no decimals (`:.0f`) gives 319, and `tex_number(max(falls))` gives $1.1 \times 10^{5}$. The backslashes are doubled because a single backslash in a Python string starts a special character. Output: figure 17a.1 and the line Figure 17a.1 saved as Revision/textbook/figures/17a_1_rho_profiles.png.

**What figure 17a.1 shows.** Left: the curve $y(z)$ is a straight line on the logarithmic $z$ axis, because $y = \ln(\sin z)/6 \approx \ln(z)/6$ for small $z$; the shaded patch $-3 \le y \le 0$ covers $z$ from $1.5 \times 10^{-8}$ to $\pi/2$, almost the whole hidden direction. Right: the energy density of the five states $N = 136$, $\lambda = 0$ on a logarithmic axis. Near the tip it is about a tenth of max|T|; toward the brane it falls by two to five powers of ten, the more the later the slice (the largest value is 319 to $1.1 \times 10^5$ times the smallest). Condition C1 demands a horizontal line such as the dotted example. The student should see at a glance that C1 fails, and by a huge margin.

**In [7], condition C1 measured.**

```python
TOL = 1e-6  # the relative tolerance of the record
spread = {sid: float(np.max(profiles[sid]["rho"]) - np.min(profiles[sid]["rho"]))
          / scale[sid] for sid in nonzero}
smallest = min(spread, key=spread.get)  # the state that depends least on x8
largest = max(spread, key=spread.get)  # the state that depends most on x8
report("smallest spread of rho / max|T|", f"{spread[smallest]:.6g} ({smallest})")
report("largest spread of rho / max|T|", f"{spread[largest]:.6g} ({largest})")
```

`TOL` is the record's tolerance. `spread` holds, for each of the 70 nonzero states, the spread of $\rho$ divided by max|T| (Section 17.4). `min(spread, key=spread.get)` returns the name whose value is smallest (`spread.get` looks a value up by its name), and `max` the largest. Output: the smallest spread is 0.0497329 (state `N136_lamm2_a20`), the largest 0.995037 (`N8_lamm1_a00`).

```python
detail = record_entry(SOURCE_REPORT, "ks_profiles_depend_on_x8")["detail"]
text = f">= {spread[smallest]:.6g} (smallest: {smallest})"  # as the record prints it
reproduces(all(value > TOL for value in spread.values()) and text in detail
           and "75 ground-state profiles" in detail
           and "70 with a nonzero" in detail,
           "C1 fails: every nonzero state depends on x8",
           SOURCE_REPORT, ["ks_profiles_depend_on_x8"])
```

`detail` is the record's text for its check `ks_profiles_depend_on_x8`. `text` is our smallest value written exactly as the record writes it; `text in detail` is true when the record contains this text. The check passes when every spread exceeds the tolerance and the record states our numbers and counts. Output: PASS C1 fails: every nonzero state depends on x8, reproducing the record's check. (COMPUTED; the smallest spread, 0.0497, is fifty thousand times the tolerance.)

**In [8], the map of C1 (figure 2).**

```python
from matplotlib.colors import LogNorm  # a logarithmic colour scale

TAGS = [("m2", "-\\lambda_2"), ("m1", "-\\lambda_1"), ("0", "0"),
        ("p1", "+\\lambda_1"), ("p2", "+\\lambda_2")]  # the couplings, in order
ROWS = [(n, tag, label) for n in (8, 136, 688) for tag, label in TAGS]
```

`LogNorm` turns values into colours on a logarithmic scale. `TAGS` pairs each coupling tag of the state names with its mathematical label. `ROWS` lists the 15 rows of the map: each particle number with each coupling.

```python
def describe(sid):
    """The state name N136_lamm2_a20 written as N = 136, lambda = -lambda_2, ..."""
    n, lam, slice_tag = sid.split("_")
    label = dict(TAGS)[lam[3:]]  # lam[3:] is m2, m1, 0, p1 or p2
    return (f"$N = {n[1:]}$, $\\lambda = {label}$, "
            f"$a_{{4,0}} = {SLICES[slice_tag]:g}$")
```

`describe` turns a state name into mathematics for a caption. `sid.split("_")` cuts `N136_lamm2_a20` at the underscores into `N136`, `lamm2` and `a20`. `n[1:]` drops the letter N; `lam[3:]` drops `lam` and leaves `m2`; `dict(TAGS)` turns the list of pairs into a dictionary, which gives $-\lambda_2$; `SLICES["a20"]` is 2.0, printed as 2.

```python
def state_table(values):
    """A 15 x 5 array of values[state] (NaN for the states with T = 0)."""
    table = np.full((len(ROWS), len(SLICES)), np.nan)
    for i, (n, tag, _) in enumerate(ROWS):
        for j, slice_tag in enumerate(SLICES):
            sid = f"N{n}_lam{tag}_{slice_tag}"
            if sid in values:
                table[i, j] = values[sid]
    return table
```

`state_table` arranges a value per state into a table of 15 rows and 5 columns. `np.full(shape, np.nan)` starts with every entry equal to NaN ("not a number", the computer's mark for a missing value). `enumerate` counts the rows $i = 0, 1, \dots$ while it walks through them; `_` is a name for a part we do not need. The state name is rebuilt from the row and column, and its value is entered if it exists; the five states with $T = 0$ stay NaN.

```python
def draw_table(ax, table, norm, fmt):
    """Draw a state table as a heat map with the value written in every cell."""
    cmap = plt.get_cmap("viridis").copy()
    cmap.set_bad("#d9d9d9")  # grey for NaN (the states with T = 0)
    image = ax.imshow(np.ma.masked_invalid(table), cmap=cmap, norm=norm,
                      aspect="auto")
```

`draw_table` draws such a table as a heat map. `viridis` is a colour scale from dark purple through blue and green to yellow; `.copy()` makes a private copy, and `set_bad` colours missing entries grey. `np.ma.masked_invalid` marks the NaN entries as missing; `ax.imshow` draws the table as coloured squares with the given colour scale `norm`; `aspect="auto"` lets the squares stretch to fill the panel.

```python
    for i in range(table.shape[0]):
        for j in range(table.shape[1]):
            value = table[i, j]
            if np.isnan(value):
                ax.text(j, i, "T = 0", ha="center", va="center", fontsize=7)
                continue
            light = norm(value) > 0.6  # yellow-green cells: black text reads best
            ax.text(j, i, format(value, fmt), ha="center", va="center", fontsize=7,
                    color="black" if light else "white")
```

Two loops visit every square (`table.shape[0]` is the number of rows, `table.shape[1]` of columns). A missing entry is labelled `T = 0` and `continue` jumps to the next square. Otherwise the value is written in the middle of its square (`ha` and `va` are the horizontal and vertical alignment) with the format `fmt`; `norm(value)` is the position of the value on the colour scale between 0 and 1, and on the light upper part the text is black, elsewhere white.

```python
    ax.set_xticks(range(len(SLICES)), [f"{a:g}" for a in SLICES.values()])
    ax.set_yticks(range(len(ROWS)),
                  [f"$N = {n}$, $\\lambda = {label}$" for n, _, label in ROWS],
                  fontsize=7)
    ax.set_xlabel("slice $a_{4,0}$")
    ax.grid(False)
    return image
```

The column marks are labelled with the slice values and the row marks with $N$ and $\lambda$; the grid of the default settings is switched off over the heat map; the drawn image is returned, so that a colour bar can be attached to it.

```python
n8_spread = [value for sid, value in spread.items() if sid.startswith("N8_")]
low8, high8 = f"{min(n8_spread):.3f}", f"{max(n8_spread):.3f}"  # three decimals
n8_text = (f"all have the spread ${low8}$" if low8 == high8  # equal when rounded
           else f"have spreads of ${low8}$ to ${high8}$")
```

The spreads of the 20 nonzero $N = 8$ states are collected; their smallest and largest are written with three decimals. If the two texts agree, the caption says that all have the same spread; otherwise it gives the range. (This is a conditional expression, `a if condition else b`.)

```python
fig, ax = plt.subplots(figsize=(6.4, 6.0))
image = draw_table(ax, state_table(spread), LogNorm(0.04, 1.0), ".3f")
fig.colorbar(image, ax=ax, label="spread of $\\rho$ / max|T| (C1 needs 0)")
ax.set_title("Condition C1: dependence on the hidden direction")
```

A single panel; the spread table is drawn with a logarithmic colour scale from 0.04 to 1 and three decimals in each square; a **colour bar** beside it translates colours into values; the title names the condition.

```python
save_figure(fig, "c1_map",
            "The spread $(\\max_y \\rho - \\min_y \\rho)/\\max|T|$ of the energy "
            "density along the hidden coordinate for all 75 recorded Kohn-Sham "
            "ground states: rows are the particle numbers $N = 8, 136, 688$ with "
            "the five couplings, columns the slices $a_{4,0}$ (logarithmic colour "
            "scale, pure numbers). "
            "Condition C1 needs $0$ in every cell; the smallest value is "
            f"${spread[smallest]:.4f}$ ({describe(smallest)}), and the $N = 8$ "
            f"states, made of brane zero modes, {n8_text}, almost the whole "
            "size of the tensor. Grey cells: the five states with no source at all.")
```

The caption, joined from its strings as in In [6], inserts three computed pieces: the smallest spread with four decimals (`:.4f`), 0.0497; the state written by `describe`, ($N = 136$, $\lambda = -\lambda_2$, $a_{4,0} = 2$); and the $N = 8$ text, "all have the spread $0.995$". Output: figure 17a.2 and its saved line.

**What figure 17a.2 shows.** Rows: $N = 8, 136, 688$, each with the couplings $-\lambda_2$ to $+\lambda_2$; columns: the five slices; colour and number: the spread of $\rho$ divided by max|T| (a pure number). C1 needs 0 in every square. The $N = 8$ rows are yellow, 0.995 everywhere: their energy density varies by almost the whole size of their tensor. The $N = 136$ and $N = 688$ rows lie between 0.05 and 0.42, largest at the first slice. The grey row, $N = 8$ with $\lambda = 0$, has no source at all. No square is close to 0.

**In [9], condition C2 point by point.**

```python
violation = {sid: profiles[sid]["p3"] + profiles[sid]["p_t"]
             - 2.0 * profiles[sid]["p8"] for sid in nonzero}  # V(y)
size = {sid: float(np.max(np.abs(violation[sid]))) / scale[sid] for sid in nonzero}
low = min(size, key=size.get)  # the state closest to C2
high = max(size, key=size.get)  # the state farthest from C2
report("smallest max|V| / max|T|", f"{size[low]:.6g} ({low})")
report("largest max|V| / max|T|", f"{size[high]:.6g} ({high})")
```

For each nonzero state, `violation` is the array $V(y) = p_3 + p_t - 2p_8$ at the 151 points (numpy adds and multiplies arrays entry by entry), and `size` its largest absolute value divided by max|T|. Output: the smallest size is 2.09192 (`N136_lamp2_a20`) and the largest 3.99006 (`N8_lamm1_a00`).

```python
detail = record_entry(SOURCE_REPORT, "ks_profiles_violate_algebraic_condition")[
    "detail"]
text = f"between {size[low]:.6g} ({low}) and {size[high]:.6g} ({high})"
reproduces(all(value > TOL for value in size.values()) and text in detail,
           "C2 fails point by point for every nonzero state",
           SOURCE_REPORT, ["ks_profiles_violate_algebraic_condition"])
```

As in In [7]: the record's text must contain our two numbers and states exactly. Output: PASS C2 fails point by point for every nonzero state, reproducing the record's check. (COMPUTED.) A violation of 2 to 4 times the largest component is not a small error: the two sides of C2 are not even of the same size.

**In [10], the violation profiles (figure 3).**

```python
plotted = [f"N{n}_lam0_{tag}" for n in (136, 688) for tag in SLICES]
signs = {sid: np.sign(violation[sid]) for sid in plotted}  # +1, -1 (or 0)
changes = {sid: int(np.sum(signs[sid][1:] * signs[sid][:-1] < 0)) for sid in plotted}
```

`plotted` lists the ten states with $\lambda = 0$ and $N = 136$ or $688$. `np.sign` gives $+1$, $-1$ or $0$ for each entry. `signs[sid][1:]` is the array without its first entry and `signs[sid][:-1]` without its last, so their product, entry by entry, is the product of the signs of neighbouring points; it is negative exactly where $V$ changes sign between two neighbours. `np.sum(... < 0)` counts these places (true counts as 1).

```python
at_tip = [abs(float(violation[sid][0])) / scale[sid] for sid in plotted]
at_brane = [abs(float(violation[sid][-1])) / scale[sid] for sid in plotted]
say(f"sign changes of the ten plotted profiles: {sorted(set(changes.values()))}")
check(all(count == 1 for count in changes.values())
      and min(at_brane) > 0.0,
      "each plotted V(y) changes sign exactly once and is nonzero at the brane")
```

`at_tip` and `at_brane` hold $|V|/\max|T|$ at the first point ($y = -3$) and at the last ($y = 0$). `set(...)` keeps each different count once, and `sorted` puts them in order. Output: `sign changes of the ten plotted profiles: [1]`, and a PASS line: every plotted profile changes sign exactly once and is not zero at the brane.

```python
fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.8), sharey=True)
for ax, n in zip(axes, (136, 688)):
    for shade, (tag, a40) in zip(SHADES, SLICES.items()):
        sid = f"N{n}_lam0_{tag}"
        ax.plot(y, violation[sid] / scale[sid], color=shade, lw=1.8,
                label=f"$a_{{4,0}} = {a40:g}$")
    ax.axhline(0.0, color="#e34948", ls="--", lw=1.2, label="C2: $V = 0$")
    ax.set_yscale("symlog", linthresh=1e-7)
    ax.set_yticks([-1e-1, -1e-3, -1e-5, -1e-7, 0.0, 1e-7, 1e-5, 1e-3, 1e-1, 1e1])
    ax.set_xlabel("hidden coordinate $y$")
    ax.set_title(f"$N = {n}$, $\\lambda = 0$")
axes[0].set_ylabel("$V = p_3 + p_t - 2p_8$, divided by max|T|")
axes[1].legend(fontsize=7, loc="upper right")
fig.tight_layout()
```

Two panels that share their vertical axis (`sharey=True`), one per particle number. In each, the five violation profiles divided by max|T| are drawn in the five shades, and a red dashed line marks $V = 0$, the value C2 demands. `set_yscale("symlog", linthresh=1e-7)` makes the vertical axis symmetric logarithmic: linear between $-10^{-7}$ and $10^{-7}$, logarithmic beyond, in both directions. `set_yticks` chooses the marks. `axes[0]` is the left panel and `axes[1]` the right one.

```python
save_figure(fig, "violation_profiles",
            "The violation profiles $V(y) = p_3 + p_t - 2p_8$ of the Kohn-Sham ground "
            "states with $\\lambda = 0$, divided by the largest component of each "
            "state, for $N = 136$ (left) and $N = 688$ (right) at the five slices "
            "$a_{4,0}$ (horizontal axis: the hidden coordinate $y$; vertical axis "
            "symmetric logarithmic, linear between $-10^{-7}$ and $10^{-7}$). "
            "Condition C2 of the field equations demands the dashed line $V = 0$; "
            f"instead $|V|$ is {min(at_tip):.2f} to {max(at_tip):.2f} times max|T| "
            "at the tip, every profile changes sign exactly once, and at the brane "
            f"$|V|$/max|T| is still between ${tex_number(min(at_brane))}$ and "
            f"${tex_number(max(at_brane))}$, small but not zero.")
```

The caption, joined from its strings as in In [6], inserts the range of $|V|/\max|T|$ at the tip with two decimals, 2.36 to 2.37, and at the brane in powers of ten, $7.1 \times 10^{-7}$ to $4.0 \times 10^{-3}$. Output: figure 17a.3 and its saved line.

**What figure 17a.3 shows.** Horizontal axis: $y$ from the tip cutoff to the brane (units of $1/H$); vertical axis: $V/\max|T|$, a pure number, on the symmetric logarithmic scale. Every profile starts at the tip with $V$ about 2.4 times max|T| and positive, drops steeply through zero once, near $y \approx -2.2$ (for the first slice at $y \approx -2.05$ when $N = 136$ and $y \approx -1.75$ when $N = 688$), stays negative, and rises toward zero at the brane without reaching it. C2 demands the red dashed line. Section 17.14 will explain the single change of sign: $V$ is the slope of $p_8$, and $p_8$ has one maximum.

**In [11], the map of C2 (figure 4).**

```python
from matplotlib.colors import Normalize  # a linear colour scale

fig, ax = plt.subplots(figsize=(6.4, 6.0))
image = draw_table(ax, state_table(size), Normalize(2.0, 4.0), ".3f")
fig.colorbar(image, ax=ax, label="max$|p_3 + p_t - 2p_8|$ / max|T| (C2 needs 0)")
ax.set_title("Condition C2: $p_3 + p_t = 2p_8$ point by point")
save_figure(fig, "c2_map",
            "The size $\\max_y|p_3 + p_t - 2p_8|/\\max|T|$ of the violation of "
            "condition C2 for all 75 recorded Kohn-Sham ground states (rows: particle "
            "number and coupling; columns: the slice $a_{4,0}$; linear colour scale, "
            "pure numbers). C2 needs $0$; every nonzero state violates it by "
            f"${size[low]:.2f}$ to ${size[high]:.2f}$ times its largest component. "
            "The $N = 8$ states, made of brane zero modes, have the same value at "
            "every slice; grey cells: no source.")
```

`Normalize` is imported first (a `from ... import` line may stand anywhere in a cell). The same heat map as In [8], now of `size` with a linear colour scale (`Normalize`) from 2 to 4, with its colour bar and title; the caption, joined from its strings as in In [6], inserts the range with two decimals, 2.09 to 3.99. Output: figure 17a.4 and its saved line.

**What figure 17a.4 shows.** The same rows and columns as figure 17a.2; colour and number: $\max_y|V|/\max|T|$, a pure number. C2 needs 0. The $N = 8$ rows show 3.990 in every square (the same state at every slice, In [18]); the $N = 136$ and $N = 688$ rows lie between 2.09 and 2.50. Every nonzero state violates C2 by more than twice its own largest component.

**In [12], a worked example: three points of one state.**

```python
example = profiles["N136_lam0_a10"]
POINTS = (-3.0, -1.5, 0.0)  # tip, middle, brane
detail = record_entry(SOURCE_REPORT, "ks_profiles_violate_algebraic_condition")[
    "detail"]
rows = []
```

The state $N = 136$, $\lambda = 0$, $a_{4,0} = 1$, which the record uses as its example; the three values of $y$ the record quotes; the record's text; and an empty list for the results.

```python
for target in POINTS:
    i = int(np.argmin(np.abs(example["y"] - target)))  # nearest grid point
    values = {c: float(example[c][i]) for c in ("y",) + COLUMNS}
    values["V"] = values["p3"] + values["p_t"] - 2.0 * values["p8"]
    rows.append(values)
    text = ("y = {y:.6g}: rho = {rho:.6g}, p3 = {p3:.6g}, p_t = {p_t:.6g}, "
            "p8 = {p8:.6g}, p3 + p_t - 2 p8 = {V:.6g}").format(**values)
    say(text)
    values["in_record"] = text in detail  # the record prints the same text?
```

For each target value of $y$: `np.abs(example["y"] - target)` is the distance of every grid point from it, and `np.argmin` the position of the smallest distance, the nearest grid point $i$. `values` collects $y$, $\rho$, $p_3$, $p_t$, $p_8$ there (`("y",) + COLUMNS` joins two tuples) and $V$. `"...".format(**values)` fills the named places `{y:.6g}` and so on from the dictionary, with six significant digits as the record prints them. The line is printed, and `in_record` notes whether the record contains exactly this text.

```python
reproduces(all(r["in_record"] for r in rows) and all(r["V"] != 0 for r in rows),
           "the three example points of N136_lam0_a10 equal the record",
           SOURCE_REPORT, ["ks_profiles_violate_algebraic_condition"])
```

The check passes when the record contains all three lines and $V \ne 0$ at all three points. Output:

| point | $\rho$ | $p_3$ | $p_t$ | $p_8$ | $V = p_3 + p_t - 2p_8$ |
| --- | --- | --- | --- | --- | --- |
| tip, $y = -3$ | 43.0702 | 158.268 | $-0$ | $-431.733$ | 1021.73 |
| middle, $y = -1.5$ | 0.707818 | 0.498835 | 0 | 0.643324 | $-0.787813$ |
| brane, $y = -0$ | 0.00211576 | 0.000391237 | $-0$ | 0.000942049 | $-0.00149286$ |

(units of $m^8$), and the PASS line. A printed $-0$ is a zero stored with a minus sign; it equals 0. Check one line by hand: at the tip $V = 158.268 + 0 - 2 \times (-431.733) = 158.268 + 863.466 = 1021.734$, which rounds to the printed 1021.73. (COMPUTED; the record's check `ks_profiles_violate_algebraic_condition` prints the same three lines.)

**In [13], the two sides of C2 as bars (figure 5).**

```python
fig, axes = plt.subplots(1, 3, figsize=(9.0, 3.4))
for ax, values, where in zip(axes, rows, ("tip", "middle", "brane")):
    sides = [values["p3"] + values["p_t"], 2.0 * values["p8"]]
    bars = ax.bar(["$p_3 + p_t$", "$2p_8$"], sides, color=["#2a78d6", "#eb6834"])
```

Three panels, one per point. In each, `sides` holds the two sides of C2, and `ax.bar` draws them as a blue and an orange bar with mathematical labels under them; `bars` keeps the two drawn bars.

```python
    for bar, value in zip(bars, sides):
        ax.annotate(f"{value:.4g}", (bar.get_x() + bar.get_width() / 2, value),
                    ha="center", va="bottom" if value >= 0 else "top", fontsize=8)
    ax.axhline(0.0, color="0.3", lw=0.8)
    y_here = values["y"] + 0.0  # + 0.0 turns -0 into 0
    ax.set_title(f"{where}: $y = {y_here:g}$", fontsize=10)
    ax.margins(y=0.18)
```

`ax.annotate` writes the value of each bar, with four significant digits, at the middle of the bar's top (`bar.get_x()` is its left edge and `bar.get_width()` its width), above a positive bar and below a negative one. A thin line marks zero; the title names the point; `margins(y=0.18)` leaves 18 per cent of free space above and below, so that the numbers fit.

```python
axes[0].set_ylabel("pressure (units of $m^8$)")
fig.suptitle("$N = 136$, $\\lambda = 0$, $a_{4,0} = 1$: the two sides of C2")
fig.tight_layout()
tip, middle, brane = rows
factors = [2.0 * r["p8"] / (r["p3"] + r["p_t"]) for r in (middle, brane)]
tip_left, tip_right = tip["p3"] + tip["p_t"], 2.0 * tip["p8"]  # the two sides
```

`suptitle` writes a title over the whole figure. `tip, middle, brane = rows` gives the three dictionaries names. `factors` holds $2p_8/(p_3 + p_t)$ at the middle and at the brane, and `tip_left`, `tip_right` the two sides at the tip.

```python
save_figure(fig, "three_points",
            "The two sides of condition C2, $p_3 + p_t$ (blue) and $2p_8$ (orange), "
            "of the Kohn-Sham state $N = 136$, $\\lambda = 0$, $a_{4,0} = 1$ at the "
            "tip $y = -3$, in the middle $y = -1.5$ and at the brane $y = 0$ "
            "(vertical axes: proper pressure in units of $m^8$, each panel with its "
            "own scale). C2 demands equal bars; near the tip the two sides even have "
            f"opposite signs (${tip_left:.1f}$ against "
            f"${tip_right:.1f}$), in the middle $2p_8$ is {factors[0]:.2f} "
            f"times $p_3 + p_t$ and at the brane {factors[1]:.2f} times.")
```

The caption, joined from its strings as in In [6], inserts the two sides at the tip with one decimal, 158.3 against $-863.5$, and the two factors with two decimals, 2.58 and 4.82. Output: figure 17a.5 and its saved line.

**What figure 17a.5 shows.** Three panels for the tip, the middle and the brane of the state $N = 136$, $\lambda = 0$, $a_{4,0} = 1$; vertical axes: pressure in units of $m^8$, each with its own scale. C2 demands two bars of equal height in each panel. At the tip the two sides do not even have the same sign; in the middle $2p_8$ is 2.58 times $p_3 + p_t$ (since $1.286648/0.498835 = 2.579$); at the brane it is 4.82 times. Exercise 2 repeats this arithmetic.

**In [14], condition C2 after integration over x8.**

```python
def integral(sid, column):
    """The integral 2 Vol_7 int e^{6Hy} X dy of column X from the record's table."""
    return float(integrals[sid][column])
```

`integral` reads one integral of a state from the table, as a number (`float` turns the text into a number).

```python
ratio = {sid: (integral(sid, "int_p3") + integral(sid, "int_p_t"))
         / (2.0 * integral(sid, "int_p8"))
         for sid in nonzero if integral(sid, "int_p8") != 0.0}
closest = min(ratio, key=lambda sid: abs(ratio[sid] - 1.0))
report("ratio closest to 1", f"{ratio[closest]:.6g} ({closest})")
report("range of the ratio", f"{min(ratio.values()):.4f} to {max(ratio.values()):.4f}")
```

`ratio` holds $R = (\int p_3 + \int p_t)/(2\int p_8)$ for every nonzero state (skipping, as a precaution, a state with $\int p_8 = 0$, which would make the division impossible; there is none). `closest` is the state whose ratio is nearest to 1: the `lambda` returns the distance from 1. Output: the ratio closest to 1 is 0.414328 (`N688_lamm2_a00`), and all ratios lie between 0.1072 and 0.4143.

```python
history_text = ", ".join(f"{sid}: {ratio[sid]:.6g}" for sid in
                         ("N136_lam0_a00", "N136_lam0_a10", "N136_lam0_a20"))
say("the history N = 136, lambda = 0: " + history_text)
detail = record_entry(SOURCE_REPORT, "ks_integrals_violate_algebraic_condition")[
    "detail"]
reproduces(len(ratio) == len(nonzero)
           and all(abs(r - 1.0) > TOL for r in ratio.values())
           and f"(closest to 1: {ratio[closest]:.6g} at {closest})" in detail
           and history_text in detail,
           "C2 fails also after integration over x8, for every nonzero state",
           SOURCE_REPORT, ["ks_integrals_violate_algebraic_condition"])
```

The ratios of three states of the history are printed as the record prints them: 0.339767, 0.25969 and 0.239714 at the slices 0, 1 and 2. The check requires a ratio for every nonzero state, every ratio away from 1, and the record's text to contain our numbers. Output: PASS C2 fails also after integration over x8, for every nonzero state. (COMPUTED.) So even a source averaged over the hidden direction, a "dimensionally reduced" source, would violate C2.

**In [15], the averaged ratio (figure 6).**

```python
N_COLOURS = {8: "#1baf7a", 136: "#2a78d6", 688: "#eb6834"}
STYLES = {"m2": ("v", ":"), "m1": ("<", "-."), "0": ("o", "-"),
          "p1": (">", "--"), "p2": ("^", (0, (1, 3)))}  # marker, line style
fig, ax = plt.subplots()
```

A colour for each particle number (green, blue, orange), and for each coupling a marker (a triangle pointing down, left, a circle, right, up) and a line style (dotted, dash-dot, solid, dashed, and `(0, (1, 3))`, which means dots of length 1 separated by gaps of 3). One panel of the default size.

```python
for n, tag, label in ROWS:
    ids = [f"N{n}_lam{tag}_{s}" for s in SLICES]
    if ids[0] not in ratio:
        continue  # N = 8, lambda = 0: no source
    marker, style = STYLES[tag]
    ax.plot(list(SLICES.values()), [ratio[sid] for sid in ids], marker=marker,
            ls=style, color=N_COLOURS[n], lw=1.3, ms=4)
```

For each of the 15 rows the five state names of the series are built; the series without a source is skipped; the ratio is drawn against the slice values, with the marker and line style of the coupling and the colour of the particle number (`ms` is the marker size).

```python
ax.axhline(1.0, color="#e34948", ls="--", lw=1.4)
ax.text(1.0, 0.95, "C2 after integration needs 1", color="#e34948", ha="center",
        va="top", fontsize=9)
for n, colour in N_COLOURS.items():
    ax.plot([], [], color=colour, lw=2.0, label=f"$N = {n}$")
for tag, label in TAGS:
    marker, style = STYLES[tag]
    ax.plot([], [], color="0.3", marker=marker, ls=style, label=f"$\\lambda = {label}$")
```

A red dashed line at 1 with a short text under it. The two loops draw nothing (`ax.plot([], [])` has no points) but create the entries of the legend: one per colour and one per marker and line style.

```python
ax.set_xlabel("slice $a_{4,0}$")
ax.set_ylabel("$(\\int p_3 + \\int p_t) / (2\\int p_8)$")
ax.set_ylim(0.0, 1.1)
ax.legend(fontsize=7, ncol=2, loc="center right")
near = max(max(ratio[f"N{n}_lam{tag}_{s}"] for tag, _ in TAGS)
           - min(ratio[f"N{n}_lam{tag}_{s}"] for tag, _ in TAGS)
           for n in (136, 688) for s in SLICES)  # spread over the couplings
```

Axis labels, the vertical range 0 to 1.1, a legend in two columns. `near` is, over the ten combinations of $N \in \{136, 688\}$ and a slice, the largest difference between the five couplings' ratios (the inner `max(...) - min(...)` is the difference for one combination, the outer `max` the largest of the ten).

```python
save_figure(fig, "integrated_ratio",
            "The ratio $(\\int p_3 + \\int p_t)/(2\\int p_8)$ of the pressures "
            "integrated over the patch with the proper-volume weight, for every "
            "nonzero recorded Kohn-Sham state, against the slice $a_{4,0}$ "
            "(colours: particle number; line styles and markers: coupling; pure "
            "numbers). A source averaged over $x_8$ would need the value $1$ (red "
            "dashed line); the states lie between "
            f"${min(ratio.values()):.3f}$ and ${max(ratio.values()):.3f}$, so even "
            "the average violates condition C2. For $N = 136$ and $N = 688$ the "
            "five couplings give almost the same ratio (they differ by at most "
            f"${near:.4f}$ at one slice), so their lines lie on top of each other.")
```

The caption, joined from its strings as in In [6], inserts the range of the ratios with three decimals, 0.107 to 0.414, and `near` with four decimals, 0.0045. Output: figure 17a.6 and its saved line.

**What figure 17a.6 shows.** Horizontal axis: the slice $a_{4,0}$; vertical axis: $R$, a pure number. A source averaged over $x_8$ would need the red dashed line at 1. The $N = 8$ states lie flat between 0.107 and 0.110 (the same value at every slice; the four nonzero couplings differ slightly); the $N = 136$ states fall from 0.34 to 0.24 and the $N = 688$ states from 0.41 to 0.25 along the history; the five couplings of each of these two $N$ lie on top of each other. All points are far below 1. Section 17.15 explains why: by the integrated conservation law, $R = b_8/\bar p_8$ exactly, where $b_8 = [p_8(0) - e^{-6HL}p_8(-L)]/(1 - e^{-6HL})$ is the brane value of $p_8$ with a tip term; for $N = 136$ and $688$ the tip term supplies at most a few per cent of $R$, for $N = 8$ about a third.

**In [16], condition C3 along the history.**

```python
HISTORY = ["N136_lam0_a00", "N136_lam0_a10", "N136_lam0_a20",
           "N688_lam0_a00", "N688_lam0_a10", "N688_lam0_a20"]
pieces = []
for sid in HISTORY:
    r, p3, pt = (integral(sid, c) for c in ("int_rho", "int_p3", "int_p_t"))
    pieces.append(f"{sid}: int rho = {r:.6g}, int p3 = {p3:.6g}, int p_t = {pt:.6g}")
    say(pieces[-1])
```

The six states that the record tests. For each, the three integrals are read (the round brackets with `for` make a **generator**, whose three values are given the names `r`, `p3`, `pt`), written as the record writes them, stored, and printed (`pieces[-1]` is the line just added).

```python
rho_constant = all(
    abs(integral(a, "int_rho") - integral(b, "int_rho"))
    <= TOL * abs(integral(a, "int_rho"))
    for a, b in (("N136_lam0_a00", "N136_lam0_a10"),
                 ("N688_lam0_a00", "N688_lam0_a10")))
p_equal = all(abs(integral(s, "int_p3") - integral(s, "int_p_t"))
              <= TOL * max(abs(integral(s, "int_p3")), 1.0) for s in HISTORY)
```

`rho_constant` is true only if the energy at slice 1 equals the energy at slice 0, within the relative tolerance, for both particle numbers; `p_equal` only if $\int p_3 = \int p_t$ for all six states (with the tolerance taken relative to $\int p_3$, or absolute when that is below 1). These are the record's own tests of C3.

```python
detail = record_entry(SOURCE_REPORT, "ks_history_is_a_prescribed_background")[
    "detail"]
reproduces(not rho_constant and not p_equal and "; ".join(pieces) in detail,
           "C3 fails: along the history rho changes and p3 differs from p_t",
           SOURCE_REPORT, ["ks_history_is_a_prescribed_background"])
```

The check passes when both C3 tests fail and the record prints the same six lines, joined by semicolons. Output:

| state | $\int\rho$ | $\int p_3$ | $\int p_t$ |
| --- | --- | --- | --- |
| `N136_lam0_a00` | 80.2822 | 23.8133 | 0 |
| `N136_lam0_a10` | 32.3841 | 10.0397 | 0 |
| `N136_lam0_a20` | 12.4451 | 4.06205 | 0 |
| `N688_lam0_a00` | 680.441 | 199.305 | 0 |
| `N688_lam0_a10` | 279.425 | 84.3387 | 0 |
| `N688_lam0_a20` | 110.387 | 35.1354 | 0 |

(units of $m$), and PASS C3 fails: along the history rho changes and p3 differs from p_t. (COMPUTED; record check `ks_history_is_a_prescribed_background`.)

**In [17], the integrals along the history (figure 7).**

```python
PARTS = [("int_rho", "$\\int\\rho$", "#2a78d6", "o"),
         ("int_p3", "$\\int p_3$", "#eb6834", "s"),
         ("int_p_t", "$\\int p_t$", "#1baf7a", "^"),
         ("int_p8", "$\\int p_8$", "#4a3aa7", "D")]
fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.8))
for ax, n in zip(axes, (136, 688)):
    ids = [f"N{n}_lam0_{s}" for s in SLICES]
    for column, label, colour, marker in PARTS:
        ax.plot(list(SLICES.values()), [integral(sid, column) for sid in ids],
                color=colour, marker=marker, lw=1.8, label=label)
    ax.set_xlabel("slice $a_{4,0}$ (the history $a_4 = Hx_4$)")
    ax.set_title(f"$N = {n}$, $\\lambda = 0$")
axes[0].set_ylabel("$2\\,\\mathrm{Vol}_7\\int e^{6Hy} X\\,dy$ (units of $m$)")
axes[1].legend(fontsize=8)
fig.tight_layout()
```

`PARTS` lists, for each of the four integrals, its column, its label, a colour and a marker (circle, square, triangle, diamond). Two panels, one per particle number; in each, the four integrals of the five states with $\lambda = 0$ are drawn against the slice.

```python
drop = [integral(f"N{n}_lam0_a00", "int_rho") / integral(f"N{n}_lam0_a20", "int_rho")
        for n in (136, 688)]
```

`drop` is the factor by which the energy falls from the first to the last slice: $80.2822/12.4451 = 6.45$ for $N = 136$ and $680.441/110.387 = 6.16$ for $N = 688$.

```python
save_figure(fig, "history_integrals",
            "The energy density and the three pressures of the Kohn-Sham states with "
            "$\\lambda = 0$, integrated over the patch with the proper-volume weight, "
            "at the five slices of the history $a_4 = Hx_4$ (left $N = 136$, right "
            "$N = 688$; vertical axis in units of $m$ with $H = 1$; along the "
            "history 3-space inflates as $e^{a_4}$ and the extra times deflate as "
            "$e^{-a_4}$). The linear member "
            "needs a constant $\\rho$ and equal pressures (condition C3); instead "
            f"$\\int\\rho$ falls by a factor of {drop[0]:.2f} ($N = 136$) and "
            f"{drop[1]:.2f} ($N = 688$) from $a_{{4,0}} = 0$ to $2$, $\\int p_3$ stays "
            "above $\\int p_t = 0$, and $\\int p_8$ is different again.")
```

The caption, joined from its strings as in In [6], inserts both factors with two decimals. In the f-string the subscript is written `a_{{4,0}}`, because inside an f-string a single brace would start a computed piece; the doubled braces print as one pair. Output: figure 17a.7 and its saved line.

**What figure 17a.7 shows.** Horizontal axis: the slice $a_{4,0}$ of the history $a_4 = Hx_4$ (3-space inflates as $e^{a_4}$, the extra times deflate as $e^{-a_4}$); vertical axis: the integrals over the patch in units of $m$. C3 needs a horizontal blue line ($\int\rho$ constant) and the three pressure lines on top of each other. Instead $\int\rho$ falls by a factor of about 6 over the history, $\int p_3$ (orange) lies well above $\int p_t = 0$ (green, on the axis: without interaction the extra times carry no pressure), and $\int p_8$ (purple) is different again. Section 17.16 shows that the fall of the energy is exactly the work done by the unbalanced pressure, $\int p_3 > \int p_t$.

**In [18], the states N = 8.**

```python
same, p3_equals_pt, p8_differs = True, True, True
for tag in ("m2", "m1", "p1", "p2"):
    first = profiles[f"N8_lam{tag}_a00"]
    for slice_tag in SLICES:
        prof = profiles[f"N8_lam{tag}_{slice_tag}"]
        same = same and all(np.array_equal(prof[c], first[c]) for c in COLUMNS)
    p3_equals_pt = p3_equals_pt and np.array_equal(first["p3"], first["p_t"])
    p8_differs = p8_differs and float(np.max(np.abs(first["p8"] - first["p3"]))) > 0
```

Three flags start true. For each nonzero coupling of $N = 8$, the profiles of all five slices are compared with the first, column by column and bit for bit (`np.array_equal`); then the cell tests $p_3 = p_t$ exactly and $p_8 \ne p_3$ somewhere. The `and` keeps a flag true only if it stays true for every case.

```python
int_p3_n8 = integral("N8_lamp1_a00", "int_p3")  # N = 8, lambda = +lambda_1
int_p8_n8 = integral("N8_lamp1_a00", "int_p8")
say(f"N = 8, lambda = +lambda_1: int p3 = {int_p3_n8:.6g}, int p8 = {int_p8_n8:.6g}")
check(same and p3_equals_pt and p8_differs,
      "N = 8: the same state at every slice, p3 = p_t, but p8 differs from p3")
```

Two integrals of one $N = 8$ state are printed as an example: $\int p_3 = -0.000977659$ and $\int p_8 = -0.00889138$, so $p_8$ is not $p_3$. Output: that line and a PASS line. Why these states do not change: the eight zero modes have zero 3-momentum, and the slice enters the Kohn-Sham equations only through the redshifted momentum $ke^{-a_{4,0}}$ (the exact rescaling identity of Chapter 14), so for $k = 0$ nothing changes. They satisfy the part "constant $\rho$ and $p_3 = p_t$" of C3, but they fail C1 and C2 (In [7] and In [9]) and have $p_8 \ne p_3$.

**In [19], the states with no source at all.**

```python
kappa, rho, p8, Lam = sp.symbols("kappa rho p8 Lam", real=True)
NAMES.update({"kappa": kappa, "rho": rho, "p8": p8, "Lam": Lam})


def equation(text):
    """An equation (left == right) of the record as the expression left - right."""
    left, right = text.split("==")
    return parse(left) - parse(right)
```

Four more real symbols ($\kappa$, $\rho$, $p_8$, $\Lambda$) are made and added to the names that `parse` knows (`update` adds pairs to a dictionary). The record writes an equation as `left == right`; `equation` cuts the text at `==` and returns left minus right, which is zero exactly when the equation holds.

```python
einstein = equations["einstein"]
x4_equation = equation(einstein["constraint_x4"]["input"]).subs({rho: 0})
x8_equation = equation(einstein["hidden_x8"]["input"]).subs({p8: 0})
difference = sp.expand(x4_equation - x8_equation)  # Lambda cancels
say(f"x4 equation minus x8 equation with rho = p8 = 0: {difference} = 0")
say(f"is the left side positive for real a4' and H > 0? {difference.is_positive}")
```

The record's Einstein constraint `3*ad1^2 + 21*H^2 + Lam == -(kappa*rho)` and hidden equation `-3*ad1^2 + 15*H^2 + Lam == kappa*p8` become expressions with $\rho = 0$ and $p_8 = 0$; their difference, multiplied out, is the derivation of Section 17.6. `.is_positive` asks sympy whether the expression is positive for all allowed values of its symbols ($a_4'$ real, $H$ positive); sympy answers `True`. Output: `6*H**2 + 6*ad1**2 = 0` and `True`.

```python
reproduces(difference == 6 * ad1 ** 2 + 6 * H ** 2 and difference.is_positive is True,
           "Einstein gravity: no source at all (T = 0) has no solution for H > 0",
           WL_A4, ["einstein_no_vacuum_solution"])
detail = record_entry(SOURCE_REPORT, "ks_zero_source_states_listed")["detail"]
reproduces(", ".join(zero) in detail and f"{len(zero)} states" in detail,
           "the five states with T = 0 are those listed by the record",
           SOURCE_REPORT, ["ks_zero_source_states_listed"])
```

The first check confirms the difference and its positivity (PROVED; Wolfram report, check `einstein_no_vacuum_solution`). The second confirms that the record lists exactly our five states with $T = 0$: `N8_lam0_a00`, `N8_lam0_a05`, `N8_lam0_a10`, `N8_lam0_a15`, `N8_lam0_a20`. These eight zero modes have zero energy and, without interaction, no source at all; by the first check, "no source" is not admissible either. Output: two PASS lines with their records.

**In [20], the last check.**

```python
names = ["rho_profiles", "c1_map", "violation_profiles", "c2_map", "three_points",
         "integrated_ratio", "history_integrals"]
paths = [output_file(f"{FIGURE_FOLDER}/17a_{k}_{name}.png")
         for k, name in enumerate(names, 1)]
check(all(path.is_file() for path in paths),
      "every figure file of this notebook exists")
all_checks_passed()
```

The seven figure names; `enumerate(names, 1)` counts them from 1, so the paths are `17a_1_rho_profiles.png` to `17a_7_history_integrals.png` in the folder where the notebook wrote them. The check confirms that every file exists, and `all_checks_passed()` prints the last line. Output: PASS every figure file of this notebook exists and ALL 16 CHECKS PASSED (notebook 17a).

**The count.** The 16 PASS lines are: one in In [2], three in In [4], one each in In [5], In [6], In [7], In [9], In [10], In [12], In [14], In [16], In [18], two in In [19], and one in In [20]. Ten of them reproduce a Revision record and name it.

### 17.12 Why the states fail: every source must be conserved

Notebook 17a shows THAT the recorded Kohn-Sham states fail all three conditions. We now ask WHY. The answer comes from one of the deepest facts about the field equations of gravity.

**The Bianchi identity.** For every metric, the left-hand side of the field equations has zero covariant divergence:

$$
\nabla_\mu E_{(k)}{}^\mu{}_\nu = 0 \quad (k = 1, 2, 3,\ \text{every } \nu), \qquad \nabla_\mu\big(\Lambda\,\delta^\mu_\nu\big) = 0 .
$$

The first statement is a theorem about the Lovelock tensors; for the author's metric with an arbitrary $a_4(x_4)$ it is PROVED in the record (checks `E1_divergence_free`, `E2_divergence_free`, `E3_divergence_free` of both the Wolfram and the sympy report). The second holds because $\Lambda$ is a constant and the covariant derivative of $\delta^\mu_\nu$ is zero (the table $\delta^\mu_\nu$, 1 on the diagonal and 0 elsewhere, is the same in every coordinate system).

**The consequence.** Take the covariant divergence of both sides of the field equations:

$$
\sum_k\alpha_k\nabla_\mu E_{(k)}{}^\mu{}_\nu + \nabla_\mu\big(\Lambda\,\delta^\mu_\nu\big) = \kappa\,\nabla_\mu T^\mu{}_\nu
$$

(rule: the same operation on both sides of an equation keeps it true; the divergence of a sum is the sum of the divergences, and a constant factor comes out)

$$
0 = \kappa\,\nabla_\mu T^\mu{}_\nu
$$

(rule: the Bianchi identity makes every term on the left zero). Since $\kappa \ne 0$: **every source of the field equations is conserved**, $\nabla_\mu T^\mu{}_\nu = 0$. Conservation is NECESSARY.

**What the Kohn-Sham states conserve.** A field that obeys its own TIME-DEPENDENT field equation in a given metric has a conserved energy-momentum tensor (Section 9.9: it is the Noether identity, which follows from the invariance of the action under a change of coordinates). The Kohn-Sham states are not such solutions: each one solves the instantaneous problem of one slice (the stationary-slice ansatz of Chapter 14), so the Noether argument does not apply to them, and the record proves exactly this much:

- along the hidden direction they are conserved at every point (the $y$ law of Section 17.13, for every self-consistent state: `Revision/kohn_sham/reports/ks-theory-python.json`, check `emt_y_conservation_selfconsistent`; the Rust solver checks it on its grid of points and integrated over the patch: `Revision/kohn_sham/reports/ks-rust-solver.json`, checks `emt_y_conservation_pointwise` and `emt_y_conservation_integrated`);
- in the time direction only the TOTAL energy of the patch obeys the energy-change law (the same theory report, check `emt_x4_component`, which states the law for the energy of the 7-volume; the solver compares the derivative of that energy with respect to $a_4$, computed by finite differences in $a_4$, with the law: check `emt_energy_change_dE_da4`). Point by point the time law fails: the instantaneous states carry no energy flux along the hidden direction (their mixed component vanishes), so nothing moves energy from one value of $y$ to another, and the energy at a given $y$ changes along the history differently from what the pressures there demand (Section 17.16 shows the numbers).

**So conservation is not SUFFICIENT.** Even a source that obeyed every conservation law could fail the field equations, and the Kohn-Sham states, which obey the hidden law everywhere and the time law for their total energy, do fail. The next four sections show precisely what the field equations of the author's metric demand beyond conservation, and why the Kohn-Sham states cannot give it.

### 17.13 The conservation law in the coordinate y

**The covariant divergence.** For any metric and any table $T^\mu{}_\nu$,

$$
\nabla_\mu T^\mu{}_\nu = \sum_\mu\partial_\mu T^\mu{}_\nu + \sum_{\mu,\lambda}\Gamma^\mu{}_{\mu\lambda}\,T^\lambda{}_\nu - \sum_{\mu,\lambda}\Gamma^\lambda{}_{\mu\nu}\,T^\mu{}_\lambda ,
$$

with the Christoffel symbols

$$
\Gamma^\lambda{}_{\mu\nu} = \frac12\sum_\sigma g^{\lambda\sigma}\big(\partial_\mu g_{\sigma\nu} + \partial_\nu g_{\sigma\mu} - \partial_\sigma g_{\mu\nu}\big),
$$

where $\partial_\mu$ is the partial derivative with respect to the coordinate $x_\mu$ and $g^{\lambda\sigma}$ is the inverse metric (the summation index is called $\sigma$ here, because $\kappa$ is the strength of gravity). The first sum is the ordinary "change plus outflow"; the two others correct for the stretching and turning of the coordinate directions.

**A lemma for a diagonal metric.** Write the diagonal entries as $g_{\mu\mu} = \eta_{\mu\mu}f_\mu^2$ with signs $\eta_{\mu\mu} = \pm 1$ and positive scale factors $f_\mu$. For a diagonal metric the inverse is diagonal, $g^{\lambda\lambda} = 1/g_{\lambda\lambda}$, so only $\sigma = \lambda$ survives in the sum:

$$
\Gamma^\lambda{}_{\mu\nu} = \frac{1}{2g_{\lambda\lambda}}\big(\partial_\mu g_{\lambda\nu} + \partial_\nu g_{\lambda\mu} - \partial_\lambda g_{\mu\nu}\big) \quad (\text{no sum over } \lambda).
$$

Now set $\lambda = \mu$:

$$
\Gamma^\mu{}_{\mu\nu} = \frac{1}{2g_{\mu\mu}}\big(\partial_\mu g_{\mu\nu} + \partial_\nu g_{\mu\mu} - \partial_\mu g_{\mu\nu}\big)
$$

(rule: replace $\lambda$ by $\mu$ everywhere)

$$
= \frac{\partial_\nu g_{\mu\mu}}{2g_{\mu\mu}}
$$

(rule: the first and the third term in the bracket are equal and cancel)

$$
= \frac{\eta_{\mu\mu}\,2f_\mu\,\partial_\nu f_\mu}{2\,\eta_{\mu\mu}f_\mu^2} = \frac{\partial_\nu f_\mu}{f_\mu} = \partial_\nu\ln f_\mu
$$

(rule: $g_{\mu\mu} = \eta_{\mu\mu}f_\mu^2$ and the chain rule $\partial_\nu(f_\mu^2) = 2f_\mu\,\partial_\nu f_\mu$; cancel $2\eta_{\mu\mu}f_\mu$; the derivative of $\ln f$ is $f'/f$).

**The divergence of a diagonal tensor.** (Section 9.9 derived this formula for every diagonal metric and applied it in the coordinate $x_8$; here we apply it in the coordinate $y$, and we repeat the short derivation so that this section can be read on its own.) Let $T^\mu{}_\nu$ be diagonal ($T^\mu{}_\nu = 0$ for $\mu \ne \nu$). In the three sums of the divergence only the terms with a diagonal entry survive: in the first only $\mu = \nu$; in the second only $\lambda = \nu$; in the third only $\lambda = \mu$. So

$$
\nabla_\mu T^\mu{}_\nu = \partial_\nu T^\nu{}_\nu + \sum_\mu\Gamma^\mu{}_{\mu\nu}\,T^\nu{}_\nu - \sum_\mu\Gamma^\mu{}_{\mu\nu}\,T^\mu{}_\mu
$$

(rule: drop the zero terms; no sum over $\nu$)

$$
= \partial_\nu T^\nu{}_\nu + \sum_\mu\big(\partial_\nu\ln f_\mu\big)\big(T^\nu{}_\nu - T^\mu{}_\mu\big)
$$

(rule: the lemma, and the two sums combined into one).

**The author's metric in the coordinate $y$.** In the coordinate $y$ the metric is (Chapter 14)

$$
ds^2 = e^{2Hy}\big[e^{2a_4}(dx_1^2 + dx_2^2 + dx_3^2) - e^{-2a_4}(dx_5^2 + dx_6^2 + dx_7^2)\big] - dx_4^2 + dy^2 ,
$$

so the scale factors are $f_i = e^{a_4 + Hy}$ for 3-space, $f_4 = 1$, $f_t = e^{-a_4 + Hy}$ for the extra times and $f_y = 1$. Their logarithms are $\ln f_i = a_4 + Hy$, $\ln f_t = -a_4 + Hy$, $\ln f_4 = \ln f_y = 0$, and their derivatives:

$$
\partial_4\ln f_i = a_4', \quad \partial_4\ln f_t = -a_4', \quad \partial_y\ln f_i = \partial_y\ln f_t = H, \quad \text{all others } 0 .
$$

Take a diagonal source $T = \mathrm{diag}(p_3, p_3, p_3, -\rho, p_t, p_t, p_t, p_8)$ whose entries depend on $x_4$ and $y$.

**The component $\nu = y$.** Here $T^y{}_y = p_8$. The three 3-space directions contribute $H(p_8 - p_3)$ each, the three extra times $H(p_8 - p_t)$ each, and $x_4$ and $y$ contribute nothing (their weight $\partial_y\ln f$ is zero):

$$
\nabla_\mu T^\mu{}_y = \partial_y p_8 + 3H(p_8 - p_3) + 3H(p_8 - p_t)
$$

(rule: the formula above with $\nu = y$)

$$
= p_8' + 6Hp_8 - 3H(p_3 + p_t)
$$

(rule: multiply out and collect; the prime on $p_8$ is $\partial/\partial y$).

**The component $\nu = x_4$.** Here $T^{x_4}{}_{x_4} = -\rho$:

$$
\nabla_\mu T^\mu{}_{x_4} = \partial_4(-\rho) + 3a_4'(-\rho - p_3) + 3(-a_4')(-\rho - p_t)
$$

(rule: the formula with $\nu = x_4$; 3-space has weight $a_4'$ and entry $p_3$, the extra times weight $-a_4'$ and entry $p_t$)

$$
= -\partial_4\rho - 3a_4'\rho - 3a_4'p_3 + 3a_4'\rho + 3a_4'p_t = -\partial_4\rho - 3a_4'(p_3 - p_t)
$$

(rule: multiply out; $-3a_4'\rho + 3a_4'\rho = 0$; factor out $-3a_4'$).

**The other six components** contain only derivatives with respect to $x_1, x_2, x_3, x_5, x_6, x_7$, of which nothing depends, and weights $\partial_{x_1}\ln f = 0$; they vanish identically.

**The conservation law.** A diagonal source in the author's metric is conserved exactly when

$$
\partial_4\rho = -3a_4'\,(p_3 - p_t) \qquad\text{and}\qquad p_8' + 6Hp_8 = 3H(p_3 + p_t).
$$

(PROVED: `Revision/kohn_sham/reports/ks-theory-python.json`, checks `emt_y_conservation_selfconsistent` and `emt_x4_component`; recorded in `Revision/kohn_sham/ks-theory.json`, keys `emt.conservationY` and `emt.energyChange`; derived again with sympy in Notebook 17b, In [9].)

**The same in the author's coordinate $x_8$.** The record of the $a_4$ equations writes the law in the coordinate $x_8$, for the general source with mixed entries (key `generalSource`, equations `conservation_x4` and `conservation_x8`):

$$
\begin{aligned}
\nabla_\mu T^\mu{}_{x_4} &= -\partial_4\rho - 3a_4'(p_3 - p_t) + \partial_8 q_{84} - 6H\tan z\;q_{84}, \\
\nabla_\mu T^\mu{}_{x_8} &= \partial_8 p_8 + 3H\cot z\,\big(2p_8 - p_3 - p_t\big) + \partial_4 q_{48}
\end{aligned}
$$

(PROVED: Wolfram and sympy reports, check `conservation_components`; sympy report, check `json_conservation`; derived again in Notebook 17b, In [7] and In [8]). With $q_{48} = q_{84} = 0$ the two forms agree. By the chain rule of Section 17.4, $\partial_8 = (dy/dx_8)\,\partial_y = \cot z\,\partial_y$, so

$$
\partial_8 p_8 + 3H\cot z\,(2p_8 - p_3 - p_t) = \cot z\,\big[p_8' + 6Hp_8 - 3H(p_3 + p_t)\big]
$$

(rule: write $\partial_8 p_8 = \cot z\,p_8'$ and take out the common factor $\cot z$; $3H\cdot 2p_8 = 6Hp_8$). Since $\cot z > 0$ on the patch, the $x_8$ law and the $y$ law say the same.

### 17.14 For a conserved source, C2 says that p8 is flat

**The key step.** Take a conserved diagonal source and solve the $y$ law for $p_3 + p_t$:

$$
p_3 + p_t = \frac{p_8' + 6Hp_8}{3H}
$$

(rule: divide both sides of $p_8' + 6Hp_8 = 3H(p_3 + p_t)$ by $3H$, which is not zero). Insert this into the violation of C2:

$$
V = p_3 + p_t - 2p_8
$$

(rule: the definition of $V$, Section 17.5)

$$
= \frac{p_8' + 6Hp_8}{3H} - 2p_8
$$

(rule: replace $p_3 + p_t$ by its value from the conservation law)

$$
= \frac{p_8'}{3H} + 2p_8 - 2p_8 = \frac{p_8'}{3H}
$$

(rule: split the fraction, $6Hp_8/(3H) = 2p_8$, and cancel). So, for EVERY conserved diagonal source,

$$
p_3 + p_t - 2p_8 = \frac{1}{3H}\,\frac{\partial p_8}{\partial y} .
$$

(PROVED: Notebook 17b, In [10], with sympy, from the conservation law of In [9].)

**What it means.**

- For a conserved source, C2 holds at a point exactly when $p_8$ is flat there ($\partial p_8/\partial y = 0$). C2 is not an extra demand on top of conservation: it is the $p_8$ part of C1. A conserved source that meets C1 meets C2 automatically.
- For the Kohn-Sham states the violation of C2 is, point by point, the slope of their hidden pressure divided by $3H$. Their $p_8$ changes by several powers of ten along $y$ (figure 2 of Notebook 17b: the largest $|p_8|$ is 2933 to $2.3 \times 10^{6}$ times the smallest, for $N = 136$, $\lambda = 0$), so $V$ cannot be small.
- The single change of sign of $V$ in figure 17a.3 is now clear: $V$ is zero exactly where $p_8$ has its maximum. The Kohn-Sham $p_8$ is negative near the tip, rises steeply, has one maximum (near $y \approx -2.2$ for most slices), and then falls toward the brane; so $V > 0$ on the tip side of the maximum and $V < 0$ on the brane side.
- The identity is COMPUTED on all 70 nonzero states with fourth-order finite differences of the stored profiles: $|p_8'/(3H) - V|$ is at most $1.05 \times 10^{-4}$ of max|T|, and the difference falls like the fourth power of the step, as an error of the differences must (Notebook 17b, In [11] and In [13]).

**A conserved profile that is not flat.** Exercise 6 shows that, when $p_3 + p_t = P$ is a constant, every conserved $p_8$ has the form $p_8 = P/2 + c\,e^{-6Hy}$ with a constant $c$, and only $c = 0$ satisfies C2. Conservation allows many profiles; the field equations of the author's metric allow only the flat one.

### 17.15 The integrated law and the averaged condition

**The integrated law.** Multiply the $y$ law by $e^{6Hy}$:

$$
e^{6Hy}p_8' + 6He^{6Hy}p_8 = 3H\,e^{6Hy}(p_3 + p_t)
$$

(rule: multiply both sides by the positive number $e^{6Hy}$)

$$
\frac{d}{dy}\big(e^{6Hy}p_8\big) = 3H\,e^{6Hy}(p_3 + p_t)
$$

(rule: the product rule read backwards, $(e^{6Hy}p_8)' = e^{6Hy}p_8' + 6He^{6Hy}p_8$). Integrate from the tip cutoff $y = -L$ to the brane $y = 0$:

$$
e^{0}\,p_8(0) - e^{-6HL}\,p_8(-L) = 3H\int_{-L}^{0}e^{6Hy}(p_3 + p_t)\,dy
$$

(rule: the fundamental theorem of calculus, the integral of a derivative is the difference of the values at the ends). Multiply by $2\,\mathrm{Vol}_7$ and use the notation $\int X$ of Section 17.7:

$$
2\,\mathrm{Vol}_7\big[p_8(0) - e^{-6HL}p_8(-L)\big] = 3H\Big(\int p_3 + \int p_t\Big) .
$$

(PROVED from the $y$ law. COMPUTED on the 70 nonzero states with the brane values, tip values and integrals of the record's table: the two sides agree to a relative difference of at most $1.421 \times 10^{-11}$; the solver's own relative difference of the same two sides, column `ycons_integrated_rel` (computed from its unrounded numbers and divided by the largest of the terms involved), is at most $1.422 \times 10^{-11}$, the value of the solver check `emt_y_conservation_integrated`; Notebook 17b, In [14].)

**Why the averaged ratio is not 1.** The averaged form of C2 asks for $R = (\int p_3 + \int p_t)/(2\int p_8) = 1$. By the definition of the weighted mean (Section 17.7),

$$
\int p_8 = 2\,\mathrm{Vol}_7\,\bar p_8\,\frac{1 - e^{-6HL}}{6H} .
$$

Divide the integrated law by $2\int p_8$:

$$
R = \frac{\int p_3 + \int p_t}{2\int p_8} = \frac{2\,\mathrm{Vol}_7\big[p_8(0) - e^{-6HL}p_8(-L)\big]/(3H)}{2\cdot 2\,\mathrm{Vol}_7\,\bar p_8\,(1 - e^{-6HL})/(6H)}
$$

(rule: the numerator from the integrated law divided by $3H$; the denominator from the line above)

$$
= \frac{p_8(0) - e^{-6HL}\,p_8(-L)}{(1 - e^{-6HL})\,\bar p_8}
$$

(rule: cancel $2\,\mathrm{Vol}_7$; $\frac{1/(3H)}{2/(6H)} = \frac{6H}{6H} = 1$). We call the numerator, divided by $1 - e^{-6HL}$, the **boundary value** of $p_8$,

$$
b_8 = \frac{p_8(0) - e^{-6HL}\,p_8(-L)}{1 - e^{-6HL}}, \qquad R = \frac{b_8}{\bar p_8} \quad\text{exactly.}
$$

The averaged C2 asks that the boundary value of the hidden pressure equal its weighted mean. That is true for a flat $p_8$ and false for the Kohn-Sham states: the weight $e^{6Hy}$ puts almost all of the mean in the last stretch before the brane (at $y = -1$ the weight is already $e^{-6} \approx 0.0025$), and there the Kohn-Sham $p_8$ falls toward the brane, so its boundary value lies below its mean.

**Is the tip term small?** The factor $e^{-6HL} = e^{-18} \approx 1.5 \times 10^{-8}$ is tiny, but near the tip $|p_8|$ is enormous, so the answer depends on the state. Notebook 17b, In [15], measures the share $1 - p_8(0)/b_8$ of $R$ that the tip term supplies: from $4.1 \times 10^{-5}$ to $0.039$ for $N = 136$, from $5.3 \times 10^{-6}$ to $0.025$ for $N = 688$, but $0.31$ to $0.33$ for the 20 nonzero $N = 8$ states. So $R \approx p_8(\text{brane})/\bar p_8$ is a fair description of the states with 3-momentum and a poor one for the brane zero modes: for them the brane value alone would give ratios from $0.074$ (the caption of figure 17b.4), and the tip term raises them to the values $R = 0.107$ to $0.110$ of figure 17a.6. The exact formula reproduces every ratio of Notebook 17a to a relative difference of $1.4 \times 10^{-11}$ (Notebook 17b, In [15]); Exercise 5 computes one by hand.

### 17.16 The time direction: energy exchange and the propagation of the constraint

**The energy-change law.** For a source that does not depend on $x_8$, the $x_4$ law of Section 17.13 reads

$$
\rho' = -3a_4'\,(p_3 - p_t)
$$

(the prime is $d/dx_4$). In words: while 3-space inflates ($a_4' > 0$), a 3-space pressure $p_3$ takes energy out of the source, and while the extra times deflate, an extra-time pressure $p_t$ puts energy in. The volume of the seven directions other than the time is constant (the factors $e^{3a_4}$ and $e^{-3a_4}$ cancel), so, unlike a gas in an ordinary expanding universe, there is no term with $\rho$ itself: only the difference of the two pressures moves the energy. This is the first law of thermodynamics, "change of energy equals minus pressure times change of volume", applied to the two families of directions (an interpretation of the PROVED identity; Section 9.10 works it out).

**For the Kohn-Sham gas** the record states only the integrated version (`Revision/kohn_sham/ks-theory.json`, key `emt.energyChange`): the energy $E = \int\rho$ of the state changes as

$$
\frac{dE}{dx_4} = -3a_4'\Big(\int p_3 - \int p_t\Big) .
$$

Along the history $a_4 = AHx_4 + a_0$ the slice is $a_{4,0} = a_4(x_4)$, so by the chain rule

$$
\frac{dE}{dx_4} = \frac{dE}{da_{4,0}}\cdot\frac{da_4}{dx_4} = AH\,\frac{dE}{da_{4,0}}
$$

(rule: the chain rule; $da_4/dx_4 = AH$), and dividing the two expressions for $dE/dx_4$ by $AH \ne 0$,

$$
\frac{dE}{da_{4,0}} = -3\Big(\int p_3 - \int p_t\Big) .
$$

(Solver check `emt_energy_change_dE_da4` of the report named in Section 17.12: the derivative that the solver computes from extra self-consistent states at $a_4 \pm \delta$ and $a_4 \pm 2\delta$ around each slice, with $\delta = 0.002$ and fixed occupations, agrees with the right-hand side in all 75 cases; the difference, divided by the larger of the sum of the absolute orbital energies and $m$, is at most $1.505 \times 10^{-10}$.) For $\lambda = 0$, $\int p_t = 0$ and $\int p_3 > 0$, so the energy must FALL along the history. For $N = 136$ at the first slice the rate is $-3 \times 23.8133 = -71.44$ (units of $m$ per unit of $a_{4,0}$). Over the whole history the energy falls from $80.2822$ to $12.4451$; Simpson's rule applied to the five recorded rates reproduces the change $-67.8372$ to a relative error of $2.1 \times 10^{-4}$, and for all ten series that change, to at most $2.2 \times 10^{-4}$ (COMPUTED; Notebook 17b, In [18]; Exercise 7).

**Point by point the time law fails.** Notebook 17b, In [20], tests $\partial\rho/\partial a_4 = -3(p_3 - p_t)$ at every grid point of the slice $a_{4,0} = 1$, with a fourth-order difference in $a_4$ over the five slices. For $N = 136$, $\lambda = 0$ it finds at the tip $\partial\rho/\partial a_4 = 82.97$ against $-3(p_3 - p_t) = -474.8$ (opposite signs: the energy density near the tip GROWS along the history while its pressure says it should fall), in the middle ($y = -1.5$) $-0.4505$ against $-1.497$, and at the brane $-0.002068$ against $-0.001174$. In all ten series with 3-momentum the ratio of the two sides at the tip is negative ($-0.327$ to $-0.106$), while the two sides integrated over the patch with the weight $e^{6Hy}$ agree to $1.3 \times 10^{-3}$, the accuracy of a difference with step $0.5$ (COMPUTED). The reason is the one given in Section 17.12: an instantaneous state has no energy flux $q_{84}$ along $y$, so the energy of each layer of the patch cannot be balanced by flow into its neighbours; only the total is balanced. A genuinely time-dependent state of the gas would need such a flux, $q_{84} \ne 0$, and C1 forbids it: a further reason why the history is only a prescribed background.

**The constraint propagates.** Write the constraint and the evolution equation of Section 17.3 as two expressions that must vanish:

$$
\mathcal C = e_{44}(a_4') + \Lambda + \kappa\rho, \qquad \mathcal E = a_4''\,F(a_4') - \kappa(p_3 - p_t) .
$$

First a fact about $e_{44}$: its derivative with respect to $a' = a_4'$ is

$$
\frac{de_{44}}{da'} = \alpha_1\cdot 6a' + \alpha_2\big(-144a'^3 - 240a'H^2\big) + \alpha_3\big(2160a'^5 + 2592a'^3H^2 + 2160a'H^4\big)
$$

(rule: differentiate each term of $E_{(k)}{}^{x_4}{}_{x_4}$ of Section 17.3; the derivative of $a'^n$ is $na'^{n-1}$)

$$
= 6a'\big[\alpha_1 - \alpha_2(24a'^2 + 40H^2) + \alpha_3(360a'^4 + 432a'^2H^2 + 360H^4)\big] = 6a'\mathcal Q = 3a'F
$$

(rule: take out the common factor $6a'$; the bracket is $\mathcal Q$ of Section 17.3, and $F = 2\mathcal Q$). Now differentiate $\mathcal C$ along the time, for a source that depends on $x_4$ only:

$$
\frac{d\mathcal C}{dx_4} = \frac{de_{44}}{da'}\,a_4'' + \kappa\rho'
$$

(rule: the chain rule for $e_{44}(a_4'(x_4))$; $\Lambda$ is constant)

$$
= 3a_4'F\,a_4'' - 3\kappa a_4'(p_3 - p_t)
$$

(rule: the fact above, and the energy-change law $\rho' = -3a_4'(p_3 - p_t)$)

$$
= 3a_4'\big[a_4''F - \kappa(p_3 - p_t)\big] = 3a_4'\,\mathcal E
$$

(rule: take out the common factor $3a_4'$). (PROVED: Wolfram report, check `constraint_propagation_bianchi`; sympy report, check `bianchi_x4`; reproduced for all couplings in Notebook 17b, In [17].)

**What it means.** If the evolution equation holds at all times ($\mathcal E = 0$), a constraint that holds at one time holds at all times: this is how the Bianchi identity keeps the field equations consistent. Along the linear member ($a_4'' = 0$, $a_4' = AH$) it gives

$$
\frac{d\mathcal C}{dx_4} = -3AH\kappa\,(p_3 - p_t) .
$$

A conserved source with $p_3 \ne p_t$ therefore makes the constraint drift: even if it held at one instant, it would fail at the next. The constraint of the linear member can hold at all times only if $p_3 = p_t$; then $\rho' = 0$ and, with C2, $p_8 = p_3$. For a conserved source along the linear member, C3 therefore reduces to the single demand $p_3 = p_t$: the constant $\rho$ then follows from conservation, and $p_8 = p_3$ from C2. The Kohn-Sham gas at $\lambda = 0$ has $p_t = 0$ and $\int p_3 > 0$: its energy falls along the history, which the linear member forbids.

**Summary of Sections 17.12 to 17.16.** For a conserved diagonal source in the author's metric:

| condition | what it says in general | what it says for a conserved source | the Kohn-Sham states |
| --- | --- | --- | --- |
| C1 | no component depends on $x_8$ | $\rho$, $p_3$, $p_t$ flat; $p_8$ flat is C2 | fail: profiles vary by powers of ten |
| C2 | $p_3 + p_t = 2p_8$ | $p_8$ flat | fail: $V = p_8'/(3H)$ is large |
| C3 | $p_3 = p_t = p_8$, $\rho$ constant | $p_3 = p_t$ (then $\rho$ constant, $p_8 = p_3$) | fail: $\int p_3 > \int p_t$, $E$ falls by a factor of about 6 |

The Kohn-Sham source is conserved along the hidden direction at every point ($y$ law), and in the time direction only for the total energy of the patch ($dE/dx_4$ law); it is NOT ADMISSIBLE.

### 17.17 The equations averaged over the hidden direction: what can and cannot be integrated

Sections 17.4 to 17.16 show that the field equations of the author's metric cannot hold, point by point, with any recorded Kohn-Sham state as the source. The Revision record `Revision/field_equations_a4/ks_source/` (script `ks_source_a4.py`, report `reports/ks-source-a4.json` with 23 checks, all PASS) asks the next questions. How far is the source from one that does not depend on $x_8$? Which weaker, averaged equations can it satisfy? And what do those averaged equations say about $a_4(x_4)$, in particular about the exponential deflation of the extra times? This section derives the answers; Notebook 17b, In [21] to In [23], reproduces the numbers it needs.

**The $x_8$ identity once more.** The record proves for every Lovelock order $k$ that $E_{(k)}{}^{x_1}{}_{x_1} + E_{(k)}{}^{x_5}{}_{x_5} - 2E_{(k)}{}^{x_8}{}_{x_8} = 0$ (check `A1_lovelock_identity_x1_plus_x5_equals_2x8`; it is the identity behind C2 in Section 17.5), and that the $y$ law of Section 17.13 gives, for a source that obeys it, $p_3 + p_t - 2p_8 = p_8'(y)/(3H)$ exactly (check `A6_x8_conservation_in_y`; it is Section 17.14). The record then evaluates the $y$ law on all 70 nonzero profiles with fourth-order differences and finds it satisfied to $6.63404 \times 10^{-5}$ of the largest term (check `B2_x8_conservation_on_every_profile`). This refines the wording of the first record `ks-source-conditions.json` (check `B0_wave1_report_verified`): the recorded states do NOT violate the conservation identity of the hidden direction; what they violate is $p_3 + p_t = 2p_8$, which is that identity combined with the independence of $x_8$ (PROVED and COMPUTED, as stated).

**How far from an $x_8$-independent source? The projection mismatch.** Among all functions that do not depend on $y$, which one is closest to a profile $X(y)$? Measure the distance with the volume weight, $D(c) = \int_{-L}^{0}e^{6Hy}\,(X - c)^2\,dy$ for a constant $c$. Its derivative with respect to $c$ is

$$
\frac{dD}{dc} = -2\int_{-L}^{0}e^{6Hy}\,(X - c)\,dy
$$

(rule: differentiate under the integral sign; the derivative of $(X - c)^2$ with respect to $c$ is $-2(X - c)$), and it vanishes when

$$
\int_{-L}^{0}e^{6Hy}X\,dy = c\int_{-L}^{0}e^{6Hy}\,dy, \qquad c = \frac{\int_{-L}^{0}e^{6Hy}X\,dy}{\int_{-L}^{0}e^{6Hy}\,dy} = \bar X
$$

(rule: split the integral, take the constant $c$ out, divide by the positive number $\int e^{6Hy}dy$). So the closest flat profile is the weighted mean $\bar X$ of Section 17.7; it is called the **orthogonal projection** of $X$ on the flat functions. The record measures the remaining part in two ways: $\mu_1 = \int e^{6Hy}|X - \bar X|\,dy/\int e^{6Hy}|X|\,dy$ (the **L1 measure**) and $\mu = \sqrt{D(\bar X)/D(0)}$ (the **L2 measure**); both are 0 for a flat profile. Over the 70 nonzero states the energy density has $\mu_1$ between $0.583068$ and $0.763572$ and $\mu$ between $0.754082$ and $1$ (check `B4_hidden_direction_mismatch`; the record prefers the L1 measure, because the L2 measure is dominated by the large values near the tip and so depends more on the tip cutoff). At least about 58 per cent of the energy density deviates from its average: the source is not close to an $x_8$-independent one (COMPUTED).

**The moment equations.** Take any one of the field equations of Section 17.3, say the constraint $e_{44} + \Lambda = -\kappa\rho$, multiply it by $e^{6Hy}$ and integrate over the patch:

$$
\int_{-L}^{0}e^{6Hy}\,(e_{44} + \Lambda)\,dy = -\kappa\int_{-L}^{0}e^{6Hy}\rho\,dy
$$

(rule: the same operation on both sides keeps an equation true)

$$
(e_{44} + \Lambda)\,W = -\kappa\,\bar\rho\,W, \qquad W = \int_{-L}^{0}e^{6Hy}\,dy = \frac{1 - e^{-6HL}}{6H}
$$

(rule: the left side does not depend on $y$ and comes out of the integral; on the right, the integral is $W\bar\rho$ by the definition of the weighted mean)

$$
e_{44} + \Lambda = -\kappa\,\bar\rho
$$

(rule: divide by $W > 0$). Each field equation gives in this way its **moment**: the same equation with every component of the source replaced by its weighted mean. Every exact solution would satisfy all of them, so they are NECESSARY conditions, weaker than the field equations themselves (PROVED: it is one line of algebra). The combination $x_1 + x_5 - 2x_8$ of the moments reads $0 = \kappa(\bar p_3 + \bar p_t - 2\bar p_8)$, the averaged C2. The record measures its failure by the relative defect $|\bar p_3 + \bar p_t - 2\bar p_8|/(|\bar p_3| + |\bar p_t| + 2|\bar p_8|)$, which lies between $0.414086$ (`N688_lamm2_a00`) and $0.806379$ over the 70 nonzero states (check `C1_averaged_algebraic_condition_fails`; reproduced in Notebook 17b, In [21]). No choice of $\kappa \ne 0$ satisfies all the moments: even after averaging, the Kohn-Sham source is not admissible (COMPUTED).

**Which moments can hold together.** Write $P(X) = \sum_k\alpha_kE_{(k)}{}^{x_4}{}_{x_4}$ evaluated at $a_4'^2 = X$ (the $x_4$ components contain $a_4'$ only through its square, Section 17.3). In Einstein gravity $P(X) = 3X + 21H^2$. The record proves $3F(a_4') = 2\,dP/dX$ at $X = a_4'^2$ for all couplings (check `A3_F_equals_two_thirds_dP_dX`; in Einstein gravity $3 \times 2 = 2 \times 3$), the fact $de_{44}/da' = 3a'F$ of Section 17.16 in another form. The averaged source obeys the averaged energy relation $d\bar\rho/da_4 = -3(\bar p_3 - \bar p_t)$, because the time law holds for the total energy of the patch (check `C2_averaged_energy_relation`: the solver's derivative agrees with it to $1.53537 \times 10^{-10}$, Simpson's rule over the slices to $2.70425 \times 10^{-4}$, and there are no Fermi-level crossings along the history). Then the derivation of Section 17.16 goes through with the averages:

$$
\frac{d}{dx_4}\Big[P(a_4'^2) + \Lambda + \kappa\bar\rho(a_4)\Big] = 3a_4'\Big[a_4''F(a_4') - \kappa(\bar p_3 - \bar p_t)\Big]
$$

(PROVED: check `A4_constraint_propagation_with_averaged_source`). So the $x_4$ moment (the constraint) and the $x_1 - x_5$ moment (the evolution equation) are consistent with each other. The $x_8$ moment is not. In Einstein gravity the $x_4$ and $x_8$ moments read

$$
3a_4'^2 + 21H^2 + \Lambda = -\kappa\bar\rho, \qquad 15H^2 - 3a_4'^2 + \Lambda = \kappa\bar p_8 ;
$$

adding them gives

$$
36H^2 + 2\Lambda = \kappa(\bar p_8 - \bar\rho)
$$

(rule: add the two equations side by side and move $-\kappa\bar\rho$ to the right; $3a_4'^2 - 3a_4'^2 = 0$, $21H^2 + 15H^2 = 36H^2$). The left side is a constant, so $\bar p_8 - \bar\rho$ would have to stay constant along the history. In the ten series with 3-momentum it changes by $0.909317$ to $0.915045$ of its largest value (check `C3_x8_moment_inconsistent_with_history`): every set of moments that contains the $x_8$ moment is inconsistent for them (COMPUTED). For the $N = 8$ states the averages do not change along the history, but their averaged C2 still fails.

**The approximation, stated.** The record therefore keeps the consistent pair, the $x_4$ moment and the $x_1 - x_5$ moment, and drops the $x_8$ moment and the $x_1 + x_5 - 2x_8$ moment. This is an APPROXIMATION (ASSUMED), and its error is not small: the dropped averaged C2 fails by the defects $0.41$ to $0.81$ quoted above, and the dropped $x_8$ moment, evaluated along the solved histories, fails by $0.109607$ to $1.87301$ of the largest term of that equation (check `D7_dropped_x8_moment_residual_and_adiabaticity`). Everything below holds only within this approximation, for the $T = 0$ instantaneous states at the computed slices $0 \le a_4 \le 2$.

**The first integral.** For $a_4' \ne 0$ the pair is equivalent to the single first-order equation $P(a_4'^2) + \Lambda = -\kappa\bar\rho(a_4)$ (the bracket of the identity above is constant, and the constraint makes the constant zero). In Einstein gravity, with the initial rate $a_4'(0) = H$ (the rate of the history on which the states were computed) and the **source strength** $\sigma_0 = \kappa\bar\rho(0)/H^2$, the constraint at $a_4 = 0$ fixes $\Lambda$:

$$
3H^2 + 21H^2 + \Lambda = -\sigma_0H^2 \quad\Longrightarrow\quad \Lambda = -24H^2 - \sigma_0H^2
$$

(rule: insert $a_4' = H$ and $\kappa\bar\rho(0) = \sigma_0H^2$; move the numbers to the right). Insert this $\Lambda$ into the constraint at a later $a_4$:

$$
3a_4'^2 + 21H^2 - 24H^2 - \sigma_0H^2 = -\kappa\bar\rho(a_4) = -\sigma_0H^2\,\frac{\bar\rho(a_4)}{\bar\rho(0)}
$$

(rule: $\kappa = \sigma_0H^2/\bar\rho(0)$ by the definition of $\sigma_0$)

$$
\Big(\frac{a_4'}{H}\Big)^2 = 1 + \frac{\sigma_0}{3}\Big(1 - \frac{\bar\rho(a_4)}{\bar\rho(0)}\Big)
$$

(rule: move $-3H^2 - \sigma_0H^2$ to the right, divide by $3H^2$). (PROVED; the record reproduces it at every slice of every Einstein case to $1.6946 \times 10^{-15}$, check `D2_einstein_first_integral`.) The gas changes $a_4'^2$ only through the fraction $1 - \bar\rho(a_4)/\bar\rho(0)$ of its averaged energy density that it has lost. Over the computed range the record finds that $a_4'^2$ changes by at most $0.281661\,|\sigma_0|H^2$ (check `D5_einstein_sign_of_the_effect`; among the four integrated series with 3-momentum listed below, the largest change belongs to $N = 136$, $\lambda = 0$, whose lost fraction at $a_4 = 2$ is therefore $3 \times 0.281661 = 0.845$).

**What can be integrated, and what it gives.** The record integrates the pair for three theories of gravity (Einstein, $\alpha_1 = 1$; Einstein-Gauss-Bonnet, $\alpha_2H^2 = 1/80$; a cubic Lovelock case, $\alpha_2H^2 = 1/80$, $\alpha_3H^4 = 1/4000$), five series of states (the four series with 3-momentum $N = 136$, $\lambda = 0$ and $N = 688$, $\lambda = 0, \pm\lambda_2$, and the series $N = 8$, $+\lambda_2$; record table `results/ks-source-a4-cases.csv`) and seven parameter choices ($\sigma_0 = \pm 10, \pm 1, \pm 1/10$, and $\Lambda = 0$), by two methods: the first integral, and a fourth-order Runge-Kutta integration of the evolution equation with a separately interpolated source. The two agree to $5.49953 \times 10^{-4}$ (check `D1_two_integration_methods_agree`). Between the slices $\bar\rho$ is taken from the cubic Hermite interpolant with the exact slopes $-3(\bar p_3 - \bar p_t)$. The results (COMPUTED, within the approximation):

- For $N = 136$, $\lambda = 0$ in Einstein gravity, $a_4'(2)/a_4'(0) = 1.95362$ for $\sigma_0 = 10$, $1.1321$ for $\sigma_0 = 1$ and $0.847549$ for $\sigma_0 = -1$. A positive $\kappa\bar\rho$ speeds the deflation of the extra times up; a negative one slows it down (Notebook 17b, In [22], reproduces these three numbers from the first integral; figure 17b.6).
- With $\Lambda = 0$ the constraint at $a_4 = 0$ needs $\sigma_0 = -24$ in Einstein gravity ($\sigma_0 < 0$ in all three theories), and the deflation HALTS: $a_4'$ reaches 0 at the turning point $a_4 = 0.149623$ (Einstein), $0.0724197$ (Einstein-Gauss-Bonnet), $0.102772$ (cubic), after which $a_4$ decreases and the extra times re-inflate (check `D3_lambda_zero_cases_halt`; Notebook 17b, In [22], finds the Einstein value, and $0.397998$ for $\sigma_0 = -10$, by bisection).
- In Einstein-Gauss-Bonnet gravity $F = 1 - \tfrac35 a_4'^2/H^2$ vanishes at $a_4'^2 = \tfrac53H^2$ (check `D0_gravity_branches`; in Einstein gravity $F = 2$ and in the cubic case $F > 0$ never vanish). For $\sigma_0 > 0$ the first integral drives $a_4'^2$ up to this **branch point**, where the evolution equation cannot be solved for $a_4''$: for $N = 136$, $\lambda = 0$ at $a_4 = 0.249607$ ($\sigma_0 = 1$) and $0.0226924$ ($\sigma_0 = 10$) (check `D6_branch_points_only_for_egb`).
- For the $N = 8$ states the averages do not change with $a_4$ and $\bar p_3 = \bar p_t$, so the evolution equation gives $a_4'' = 0$: exactly the linear member $a_4 = A_0Hx_4 + a_0$, with the rate $A_0$ chosen initially and $\Lambda$ absorbing $\kappa\bar\rho$ (check `D4_constant_source_gives_linear_member`); their averaged C2 still fails.

**What cannot be integrated, or was not computed.** The full coupled problem, the author's metric with the Kohn-Sham source, has no solution at all (C1 fails), so nothing about $a_4$ is DERIVED from it (PROVED, Sections 17.4 to 17.14). The $x_8$ moment cannot be kept (shown above). Not computed (OPEN): the source beyond $a_4 = 2$, where no Kohn-Sham states exist (the record states only a CONDITIONAL: if $\bar\rho$ tended to 0 there, Einstein gravity would give $a_4'^2 \to (-\Lambda - 21H^2)/3$, a late-time exponential deflation at a rate set by $\Lambda$ and $H$ alone); thermal states (only the $T = 0$ ground states are used); the time-dependent, non-adiabatic problem; and a source with the profile the equations require, or a metric with $x_8$-dependent warp functions that could carry the Kohn-Sham profile.

**So, does the dirac16complex source drive the exponential deflation of the extra times?** Exactly: the question has no solution to examine, because no recorded Kohn-Sham state is an admissible source. Within the stated approximation: no. The equations are unchanged under $x_4 \to -x_4$, because $F$ and $P$ contain $a_4'$ only through even powers (check `A3_F_equals_two_thirds_dP_dX`); that reversal turns deflation of the extra times into inflation, so the sign of the rate and its size are initial data, and $\Lambda$ is fixed by them through the constraint. The gas only modifies a deflation that is already there, by a bounded amount set by the energy it loses; with $\Lambda = 0$ it even stops it. Exponential deflation at a constant rate is allowed (the $N = 8$ states give exactly the linear member) but not selected. This is the answer of the record `Revision/field_equations_a4/ks_source/README.md`, reproduced here step by step.

### 17.18 Example: the conservation laws, the averaged equations, and why the states fail

The second notebook makes Sections 17.12 to 17.17 concrete. It first checks that the Kohn-Sham source rests on the author's eight real $16 \times 16$ gamma matrices, the very file that the Rust solver read; then it derives with sympy the covariant divergence of a general source in the author's metric, in the coordinate $x_8$ and in the coordinate $y$, and compares it with the two Revision records; it proves $V = p_8'/(3H)$ and $d\mathcal C/dx_4 = 3a_4'\mathcal E$; and it tests the identities on the 75 recorded states, point by point with a convergence study, integrated over the patch, and along the deflating history, where it also shows that the time law fails point by point; finally it computes the hidden-direction averages, the defect of the averaged C2 and the first integral of the averaged equations of Einstein gravity, and reproduces the record's rates and turning points. It prints 20 PASS lines and draws six figures. It runs in about 20 seconds on a typical laptop and needs no Rust.

<!-- NOTEBOOK 17b -->

### 17.21 Line-by-line walk-through of Notebook 17b

The notebook has 24 code cells, In [1] to In [24]. As in Section 17.11, every line or small group of lines is quoted and explained, and each figure is described after the cell that draws it.

**In [1], the set-up cell.** It is the set-up cell of Notebook 17a, word for word, except for two things: the comment lines at the top hold the run instructions of Notebook 17b (Section 17.19), and the line `NOTEBOOK_ID = "17b"` names this notebook. Every line is explained in Section 17.11 under In [1]. The cell prints its one line, Set-up of notebook 17b complete: repository folder found, helpers defined.

**In [2], the Revision records and the helpers.**

```python
import csv  # reads tables stored as CSV files (comma-separated values)
import hashlib  # computes the sha256 fingerprint of a file

import numpy as np  # arrays of numbers
import sympy as sp  # exact algebra with symbols
```

As in Notebook 17a, plus `hashlib`, a module of Python that computes fingerprints of data (In [4]).

```python
GAMMAS = "Revision/algebra/gammas.json"  # the eight real 16 x 16 gammas
ALGEBRA = "Revision/algebra/reports/python-algebra.json"  # their checks
EQUATIONS = "Revision/field_equations_a4/a4-equations.json"  # the a4 equations
PY_A4 = "Revision/field_equations_a4/reports/python-a4-report.json"  # sympy
WL_A4 = "Revision/field_equations_a4/reports/wolfram-a4-report.json"  # Wolfram
SOURCE_REPORT = "Revision/field_equations_a4/reports/ks-source-conditions.json"
KS_SOURCE = "Revision/field_equations_a4/ks_source/reports/ks-source-a4.json"
KS_THEORY = "Revision/kohn_sham/ks-theory.json"  # the Kohn-Sham theory record
KS_PY = "Revision/kohn_sham/reports/ks-theory-python.json"  # its sympy checks
KS_RUST = "Revision/kohn_sham/reports/ks-rust-solver.json"  # the solver checks
GROUND = "Revision/kohn_sham/results/ground"  # the 75 Kohn-Sham ground states
```

Eleven names for the Revision records used below: the author's gamma matrices and the report of their checks; the record of the $a_4$ equations and its two reports; the record on the Kohn-Sham source conditions; the report of the $a_4$ equations with the Kohn-Sham source (Section 17.17); the Kohn-Sham theory record, its sympy report and the report of the Rust solver; and the folder of the recorded states.

```python
def read_json(relative):
    """Read a JSON file of the repository (a Revision record)."""
    return json.loads(repository_file(relative).read_text(encoding="utf-8"))


def record_entry(report_file, name):
    """The entry {name, verdict, detail} of a check of a report, None if absent."""
    for entry in read_json(report_file)["checks"]:
        if entry["name"] == name:
            return entry
    return None


def reproduces(condition, name, report_file, record_names):
    """A check that also requires the named checks of the report to be PASS."""
    found = all((record_entry(report_file, n) or {}).get("verdict", "").upper()
                == "PASS" for n in record_names)  # some reports write "pass"
    names_text = ", ".join(record_names)  # the check names, separated by commas
    check(condition and found, name, record=f"{report_file}, check {names_text}")


def tex_number(value, digits=2):
    """A number for a caption in powers of ten: 0.0123 -> 1.2 \\times 10^{-2}."""
    mantissa, exponent = f"{value:.{digits - 1}e}".split("e")
    return f"{mantissa} \\times 10^{{{int(exponent)}}}"
```

The four helpers of Notebook 17a (Section 17.11, In [2]), with one change in `reproduces`: `.get("verdict", "")` returns an empty string when an entry has no verdict, and `.upper()` turns the verdict into capital letters, because the report of the algebra writes its verdicts as `pass` while the other reports write `PASS`.

```python
REPORTS = [ALGEBRA, PY_A4, WL_A4, SOURCE_REPORT, KS_SOURCE, KS_PY, KS_RUST]
every_pass = True
for report_file in REPORTS:
    verdicts = [entry["verdict"].upper()
                for entry in read_json(report_file)["checks"]]
    passed = verdicts.count("PASS")  # how many checks of this report passed
    every_pass = every_pass and passed == len(verdicts)
    report(report_file.split("/")[-1], f"{passed} of {len(verdicts)} checks PASS")
check(every_pass, "every check of the seven Revision reports used here is PASS")
```

For each of the seven reports the cell collects the verdicts, counts the PASS among them (`.count`), keeps `every_pass` true only if all passed, and prints the file name (`split("/")[-1]`, the part after the last slash) with the count. Output: seven RESULT lines, one per report, each of the form "name of the report = $n$ of $n$ checks PASS", and the line PASS every check of the seven Revision reports used here is PASS. The numbers $n$ are the numbers of checks that the reports held when the notebook was executed; they are printed in the notebook text above. The notebook does not require particular counts, because a report may gain checks when the Revision record is extended: the check asks only that every check of every report passes.

**In [3], the eight gamma matrices are real signed permutation matrices.**

```python
gamma_record = read_json(GAMMAS)
entries = [v for matrix in gamma_record["gamma"] for row in matrix for v in row]
real_integers = all(isinstance(v, int) for v in entries)  # no complex entries
gamma = [np.array(matrix, dtype=float) for matrix in gamma_record["gamma"]]
eta = np.array(gamma_record["eta"], dtype=float)  # +1 or -1 for x1, ..., x8
```

The record `gammas.json` stores the eight matrices as lists of rows of numbers. The list comprehension with three `for` parts walks through every matrix, every row of it and every entry of the row, and collects all $8 \times 16 \times 16 = 2048$ entries. `isinstance(v, int)` is true when an entry is a whole number; a complex entry would be stored differently, so `real_integers` confirms that the matrices are REAL. Then each matrix becomes a numpy array of decimal numbers (`dtype=float`), and `eta` holds the eight signs of the frame metric.

```python
shapes = sorted({matrix.shape for matrix in gamma})  # should be one shape only
values = sorted({int(v) for v in entries})  # the entries that occur
one_per_line = all(np.all(np.count_nonzero(matrix, axis=0) == 1)
                   and np.all(np.count_nonzero(matrix, axis=1) == 1)
                   for matrix in gamma)  # one nonzero entry per row and column
```

`matrix.shape` is the pair (rows, columns); a set keeps each different shape once. `values` is the sorted set of the different entries. `np.count_nonzero(matrix, axis=0)` counts the nonzero entries of every column and `axis=1` of every row; `one_per_line` is true when every column and every row of every matrix holds exactly one nonzero entry: then each matrix is a **signed permutation matrix**, which moves the 16 components of a spinor into a new order and changes some of their signs.

```python
report("number of gamma matrices", len(gamma))
report("their shapes", shapes)
report("the entries that occur", values)
report("eta in the order x1, ..., x8", [int(v) for v in eta])
reproduces(len(gamma) == 8 and shapes == [(16, 16)] and real_integers
           and values == [-1, 0, 1] and one_per_line,
           "eight real 16 x 16 signed permutation matrices",
           ALGEBRA, ["reality_signed_permutations"])
```

Output: 8 matrices, the single shape (16, 16), the entries $-1$, $0$, $1$, $\eta = (1, 1, 1, -1, -1, -1, -1, 1)$ in the order $x_1, \dots, x_8$, and the PASS line, reproducing the algebra report's check `reality_signed_permutations`.

**In [4], the Clifford relation and the fingerprint of the file.**

```python
identity16 = np.eye(16)  # the 16 x 16 unit matrix
deviation = 0.0  # the largest deviation from the Clifford relation
for a in range(8):
    for b in range(8):
        anticommutator = gamma[a] @ gamma[b] + gamma[b] @ gamma[a]
        target = 2.0 * eta[a] * identity16 if a == b else 0.0 * identity16
        deviation = max(deviation, float(np.max(np.abs(anticommutator - target))))
report("largest deviation from the Clifford relation, 64 pairs", deviation)
reproduces(deviation == 0.0, "the Clifford relation holds exactly for all 64 pairs",
           ALGEBRA, ["clifford_relation"])
```

`np.eye(16)` is the unit matrix. The two loops visit all $8 \times 8 = 64$ ordered pairs $(a, b)$; `@` is matrix multiplication. The **anticommutator** $\gamma^a\gamma^b + \gamma^b\gamma^a$ is compared with $2\eta^{aa}$ times the unit matrix when $a = b$ and with the zero matrix otherwise, and `deviation` keeps the largest difference of any entry. Products and sums of matrices of whole numbers are exact in the computer, so the deviation must be exactly 0. Output: RESULT ... = 0.0 and the PASS line (algebra report, check `clifford_relation`).

```python
fingerprint = hashlib.sha256(repository_file(GAMMAS).read_bytes()).hexdigest()
report("sha256 of gammas.json, first 16 digits", fingerprint[:16])
solver_detail = record_entry(KS_RUST, "gamma_fixture_numeric")["detail"]
reproduces(f"(sha256 {fingerprint[:16]})" in solver_detail,
           "the Rust Kohn-Sham solver read exactly this file of gammas",
           KS_RUST, ["gamma_fixture_numeric", "block_reduction_numeric"])
```

`read_bytes()` reads the file as raw bytes, `hashlib.sha256(...)` computes its fingerprint and `.hexdigest()` writes it as 64 hexadecimal digits (the digits 0 to 9 and the letters a to f). The Rust solver printed the first 16 digits of the fingerprint of the file it read into its check `gamma_fixture_numeric`; the check passes when the solver's text contains exactly ours, and when the solver's check `block_reduction_numeric` passed (it confirms that the solver's $2 \times 2$ blocks are the 16-component Hamiltonian written in another basis). Output: the 16 digits `95d8cbdd0682fd30` and PASS the Rust Kohn-Sham solver read exactly this file of gammas. So the Kohn-Sham source of this chapter was computed with the author's eight real $16 \times 16$ matrices and no others.

**In [5], the eight matrices as heat maps (figure 1).**

```python
LABELS = ["x_1", "x_2", "x_3", "x_4", "x_5", "x_6", "x_7", "x_8"]
fig, axes = plt.subplots(2, 4, figsize=(9.6, 5.4))
for a, ax in enumerate(axes.flat):
    image = ax.imshow(gamma[a], cmap="RdBu_r", vmin=-1.0, vmax=1.0)
    sign = "+1" if eta[a] > 0 else "-1"  # the square of this gamma matrix
    ax.set_title(f"$\\gamma^{{({LABELS[a]})}}$, square ${sign}$", fontsize=10)
```

A figure of two rows of four panels; `axes.flat` walks through the eight panels row by row, and `enumerate` numbers them $a = 0, \dots, 7$ (the matrix of $x_{a+1}$). `imshow` draws the matrix with the colour scale `RdBu_r` (red, white, blue reversed: red for $+1$, white for $0$, blue for $-1$), fixed between $-1$ and $1$ by `vmin` and `vmax`. The title names the matrix and the sign of its square, $(\gamma^a)^2 = \eta^{aa}$ times the unit matrix.

```python
    ax.set_xticks([0, 15], ["1", "16"])  # column numbers 1 and 16
    ax.set_yticks([0, 15], ["1", "16"])  # row numbers 1 and 16
    ax.tick_params(labelsize=7)  # small numbers, so that they do not collide
    ax.grid(False)  # no grid lines over the entries
fig.colorbar(image, ax=axes, shrink=0.75, label="matrix entry", ticks=[-1, 0, 1])
nonzero_count = int(sum(np.count_nonzero(matrix) for matrix in gamma))
```

Only the first and the last row and column are numbered (Python counts from 0, the book from 1); one colour bar serves all eight panels (`ax=axes`, shrunk to 75 per cent). `nonzero_count` counts the nonzero entries of all eight matrices: `np.count_nonzero` counts them in one matrix, and `sum` adds the eight counts.

```python
save_figure(fig, "eight_gammas",
            "The author's eight real $16 \\times 16$ gamma matrices "
            "$\\gamma^{(x_1)}$ to $\\gamma^{(x_8)}$ as heat maps (rows 1 to 16 down, "
            "columns 1 to 16 across; red $+1$, blue $-1$, white $0$). Each row and "
            "each column holds exactly one nonzero entry, so the eight matrices "
            f"have {nonzero_count} nonzero entries in all; the squares are $+1$ "
            "for the space-like directions $x_1, x_2, x_3, x_8$ and $-1$ for the "
            "time $x_4$ and the deflating extra times $x_5, x_6, x_7$. These are "
            "the matrices with which the Kohn-Sham source of this chapter was "
            "computed.")
```

The caption is joined from its strings, as in Notebook 17a, In [6]; its one computed piece is `nonzero_count`, $8 \times 16 = 128$. Output: figure 17b.1 and its saved line.

**What figure 17b.1 shows.** Eight $16 \times 16$ tables, rows 1 to 16 downwards and columns 1 to 16 across, entries coloured red ($+1$), blue ($-1$) or white ($0$). Every panel has exactly 16 coloured squares, one in each row and each column; the patterns and the signs differ from matrix to matrix (some lie along the diagonal from the lower left to the upper right, others in two blocks away from the diagonal). The squares are $+1$ for the space-like directions $x_1, x_2, x_3, x_8$ and $-1$ for the time $x_4$ and the deflating extra times $x_5, x_6, x_7$. The student should see that these are honest real matrices of whole numbers, the same that the Kohn-Sham source was computed with.

**In [6], the hidden coordinate y, derived.**

```python
H = sp.symbols("H", positive=True)  # the constant H of the metric
X8 = sp.symbols("x8", positive=True)  # the author's hidden coordinate
z = 6 * H * X8  # the angle z = 6 H x8
y_of_x8 = sp.log(sp.sin(z)) / (6 * H)  # the hidden coordinate y
dy_dx8 = sp.simplify(sp.diff(y_of_x8, X8))  # chain rule
g_yy = sp.simplify(sp.cot(z) ** 2 / dy_dx8 ** 2)  # g88 times (dx8/dy)^2
say(f"dy/dx8 = {dy_dx8},  g_yy = {g_yy}")
```

Symbols for $H$ and $x_8$, both positive; the angle $z$ and $y = \ln(\sin z)/(6H)$ as sympy expressions. `sp.diff` differentiates with respect to $x_8$ (sympy applies the chain rule) and `sp.simplify` simplifies: the result is $\cot z$, printed as `1/tan(6*H*x8)`. The metric entry in the new coordinate is $g_{yy} = g_{88}\,(dx_8/dy)^2 = \cot^2 z/\cot^2 z = 1$ (rule: a length $\sqrt{g_{88}}\,dx_8$ is the same in both coordinates, and $dx_8 = dy/(dy/dx_8)$). Output: `dy/dx8 = 1/tan(6*H*x8),  g_yy = 1`.

```python
s, c, a4_value = sp.symbols("s c a4", positive=True)  # s = sin z, c = cos z
y_of_s = sp.log(s) / (6 * H)  # y written with s = sin z
warp = sp.simplify(sp.exp(2 * H * y_of_s))  # e^{2Hy} in terms of s
say(f"e^(2Hy) = {warp}  (the warp factor sin^(1/3) z)")
```

To let sympy simplify powers safely, $\sin z$ and $\cos z$ are replaced by positive symbols $s$ and $c$ (both are positive on the patch), and $a_4$ by a positive symbol (only for this simplification; any value would do, since it cancels). Then $e^{2Hy} = e^{2H\ln(s)/(6H)} = e^{\ln(s)/3} = s^{1/3}$ (rule: $e^{\ln s} = s$ and $e^{k\ln s} = s^k$). Output: `e^(2Hy) = s**(1/3)`: the warp factor $\sin^{1/3}z$ is $e^{2Hy}$.

```python
factors = ([sp.exp(2 * a4_value) * s ** sp.Rational(1, 3)] * 3 + [1]
           + [sp.exp(-2 * a4_value) * s ** sp.Rational(1, 3)] * 3)  # |g_ii|, i < 8
root_x8 = sp.simplify(sp.sqrt(sp.prod(factors) * (c / s) ** 2))  # g88 = cot^2 z
root_y = sp.simplify(sp.sqrt(sp.prod(factors) * 1))  # g_yy = 1
say(f"sqrt|det g| in the x8 chart = {root_x8};  in the y chart = {root_y}")
```

`factors` lists the absolute values of the seven diagonal entries other than $g_{88}$ (`[x] * 3` repeats an entry three times; `sp.Rational(1, 3)` is the exact fraction 1/3). `sp.prod` multiplies them: $e^{6a_4}s\cdot 1\cdot e^{-6a_4}s = s^2$. Times $g_{88} = \cot^2 z = (c/s)^2$ this is $c^2$, whose square root is $c = \cos z$; times $g_{yy} = 1$ it is $s^2$, whose square root is $s = \sin z = e^{6Hy}$. Output: `sqrt|det g| in the x8 chart = c;  in the y chart = s`.

```python
reproduces(sp.simplify(dy_dx8 - sp.cot(z)) == 0 and g_yy == 1
           and warp == s ** sp.Rational(1, 3) and root_x8 == c and root_y == s,
           "dy/dx8 = cot z, g_yy = 1, sin^(1/3) z = e^(2Hy), sqrt|g| = cos z or e^(6Hy)",
           KS_PY, ["geometry_hidden_coordinate", "geometry_sqrt_det",
                   "geometry_warped_form"])
```

The check collects the four results and reproduces three checks of the Kohn-Sham theory report. Output: the PASS line.

**In [7], the covariant divergence of a general source in the coordinate x8.**

```python
def christoffel(metric, chart):
    """All Gamma^l_{mn} of a diagonal metric, as a nested list [l][m][n]."""
    inverse = [1 / metric[k, k] for k in range(8)]  # diagonal: g^kk = 1 / g_kk
    return [[[sp.simplify(inverse[l] * (sp.diff(metric[l, m], chart[n])
                                        + sp.diff(metric[l, n], chart[m])
                                        - sp.diff(metric[m, n], chart[l])) / 2)
              for n in range(8)] for m in range(8)] for l in range(8)]
```

`christoffel` computes all $8 \times 8 \times 8 = 512$ symbols $\Gamma^l{}_{mn}$ of a diagonal metric with the formula of Section 17.13, $\Gamma^l{}_{mn} = \frac{1}{2g_{ll}}(\partial_m g_{ln} + \partial_n g_{lm} - \partial_l g_{mn})$. `chart` is the list of the eight coordinates; `metric[l, m]` is an entry of the sympy matrix; the three nested list comprehensions build a list of lists of lists, so that `G[l][m][n]` is $\Gamma^l{}_{mn}$.

```python
def divergence(T, metric, chart):
    """The 8 components nabla_mu T^mu_nu of a table T[mu, nu] = T^mu_nu."""
    G = christoffel(metric, chart)
    result = []
    for nu in range(8):
        total = 0
        for mu in range(8):
            total += sp.diff(T[mu, nu], chart[mu])  # d_mu T^mu_nu
            for lam in range(8):
                total += G[mu][mu][lam] * T[lam, nu]  # Gamma^mu_{mu lam} T^lam_nu
                total -= G[lam][mu][nu] * T[mu, lam]  # Gamma^lam_{mu nu} T^mu_lam
        result.append(sp.simplify(total))
    return result
```

`divergence` programs the definition of Section 17.13 term by term, without the shortcut of the lemma: for each $\nu$ it adds $\partial_\mu T^\mu{}_\nu$, adds $\Gamma^\mu{}_{\mu\lambda}T^\lambda{}_\nu$ and subtracts $\Gamma^\lambda{}_{\mu\nu}T^\mu{}_\lambda$ over all $\mu$ and $\lambda$ (`+=` adds to the running total, `-=` subtracts), simplifies, and appends the result. The table may be any $8 \times 8$ matrix, with mixed entries too.

```python
coords = sp.symbols("x1:9", real=True)  # x1, ..., x8 (the x8 chart)
x4, x8 = coords[3], coords[7]
a4 = sp.Function("a4")(x4)  # the free function of the metric
zz = 6 * H * x8  # z = 6 H x8
wz = sp.sin(zz) ** sp.Rational(1, 3)  # the warp factor sin^(1/3) z
metric_x8 = sp.diag(*([sp.exp(2 * a4) * wz] * 3 + [-1]
                      + [-sp.exp(-2 * a4) * wz] * 3 + [sp.cot(zz) ** 2]))
```

`sp.symbols("x1:9")` makes the eight symbols `x1` to `x8` (the range 1:9 stops before 9); position 3 is $x_4$ and position 7 is $x_8$. `sp.Function("a4")(x4)` is an unknown function $a_4(x_4)$, which sympy differentiates as $a_4'$. `sp.diag(*list)` builds the diagonal matrix of the author's metric from the list of its eight entries (the star passes the entries one by one).

```python
names = ("rho", "p3", "pt", "p8", "q48", "q84")
rho, p3, pt, p8, q48, q84 = (sp.Function(n)(x4, x8) for n in names)
T_x8 = sp.diag(p3, p3, p3, -rho, pt, pt, pt, p8)  # the diagonal part
T_x8[3, 7] = q48  # T^x4_x8
T_x8[7, 3] = q84  # T^x8_x4
div_x8 = divergence(T_x8, metric_x8, coords)
```

The six parts of the most general source are unknown functions of $x_4$ and $x_8$. The table is the diagonal matrix with the two mixed entries placed in row $x_4$, column $x_8$ and the reverse. `div_x8` is the list of the eight components of its divergence.

```python
notation = {sp.Derivative(f, v): sp.Symbol(f"d{v.name[1]}{f.func.__name__}")
            for f in (rho, p3, pt, p8, q48, q84) for v in (x4, x8)}
notation[sp.Derivative(a4, x4)] = sp.Symbol("ad1")  # a4'


def in_record_notation(expression):
    """Write derivatives as d4rho, d8p8, ... and functions as plain symbols."""
    expression = expression.subs(notation)
    return expression.subs({f: sp.Symbol(f.func.__name__)
                            for f in (rho, p3, pt, p8, q48, q84)})
```

To print the result in the record's notation, each partial derivative is replaced by a short symbol: `v.name[1]` is the digit of the coordinate (`4` or `8`) and `f.func.__name__` the name of the function, so $\partial\rho/\partial x_4$ becomes `d4rho` and $\partial p_8/\partial x_8$ becomes `d8p8`; $a_4'$ becomes `ad1`. `in_record_notation` makes these replacements and then writes each function as a plain symbol.

```python
cc = sp.Symbol("cc")  # the record writes cot z as cc


def readable(expression):
    """A component as a sum of source symbols times simplified coefficients."""
    plain = sp.expand(in_record_notation(expression))
    sources = sorted(plain.free_symbols - {H, x8, sp.Symbol("ad1")}, key=str)
    total = sp.Integer(0)  # the sum, built term by term
    for symbol, factor in sp.collect(plain, sources, evaluate=False).items():
        factor = factor.subs(sp.sin(2 * zz), 2 * sp.sin(zz) * sp.cos(zz))
        factor = sp.simplify(factor.subs(sp.tan(zz), sp.sin(zz) / sp.cos(zz)))
        factor = sp.simplify(factor.subs(sp.sin(zz), sp.cos(zz) / cc))
        total += factor * symbol  # sin z = cos z / cot z
    return total.subs(sp.tan(zz), 1 / cc)
```

`readable` writes a component as a sum "coefficient times source quantity", with the coefficients in terms of `cc` $= \cot z$ as in the record. After multiplying out, `sources` is the sorted list of the source symbols that occur (all symbols except $H$, $x_8$ and `ad1`; `key=str` sorts by name). `sp.collect(..., evaluate=False)` returns a dictionary from each source symbol to its coefficient. Each coefficient is rewritten with $\sin 2z = 2\sin z\cos z$ and $\tan z = \sin z/\cos z$, simplified, and then written with $\sin z = \cos z/\cot z$, so that only $\cot z$ remains; the terms are added up, and a remaining $\tan z$ is written as $1/\cot z$.

```python
for nu, component in enumerate(div_x8):
    say(f"nabla_mu T^mu_x{nu + 1} = {readable(component)}")
```

The eight components are printed. Output: six zeros, and

`nabla_mu T^mu_x4 = -6*H*q84/cc - 3*ad1*p3 + 3*ad1*pt - d4rho + d8q84`,

`nabla_mu T^mu_x8 = -3*H*cc*p3 + 6*H*cc*p8 - 3*H*cc*pt + d4q48 + d8p8`,

which are the two laws of Section 17.13 in the coordinate $x_8$ (since $1/\cot z = \tan z$).

**In [8], comparison with the record.**

```python
equations = read_json(EQUATIONS)
RECORD_NAMES = {"ad1": sp.Derivative(a4, x4), "H": H, "cc": sp.cot(zz),
                "rho": rho, "p3": p3, "pt": pt, "p8": p8, "q48": q48, "q84": q84}
RECORD_NAMES.update({str(symbol): derivative
                     for derivative, symbol in notation.items()})
```

`RECORD_NAMES` translates the names of the record's text back into sympy objects: `ad1` into the derivative $a_4'$, `cc` into $\cot z$, the source names into the functions, and (through `update` with the dictionary `notation` read backwards) `d4rho` into $\partial\rho/\partial x_4$ and so on.

```python
def record_equation(text):
    """An equation left == right of the record as the expression left - right."""
    left, right = text.replace("^", "**").split("==")
    return (sp.sympify(left, locals=RECORD_NAMES)
            - sp.sympify(right, locals=RECORD_NAMES))
```

As `equation` in Notebook 17a: the record's text `left == right` becomes the expression left minus right.

```python
same = []
for key, nu in (("conservation_x4", 3), ("conservation_x8", 7)):
    recorded = record_equation(equations["generalSource"][key]["input"])
    difference = sp.simplify((div_x8[nu] - recorded).rewrite(sp.cos))
    same.append(difference == 0)
    say(f"{key}: ours minus the record = {difference}")
zero_components = all(div_x8[nu] == 0 for nu in (0, 1, 2, 4, 5, 6))
reproduces(all(same) and zero_components,
           "our divergence equals the record: x4 and x8 laws, six zero components",
           PY_A4, ["conservation_components", "json_conservation"])
```

For the record's two laws (positions 3 and 7 are $x_4$ and $x_8$) the difference between our component and the record's is rewritten with cosines only (`.rewrite(sp.cos)`) and simplified; sympy finds 0 (one term needs the identity $\tan z + \cot z = 2/\sin 2z$, which the rewriting handles). Output: `conservation_x4: ours minus the record = 0`, the same for `conservation_x8`, and the PASS line reproducing the sympy report's checks `conservation_components` and `json_conservation`. (PROVED.)

**In [9], the conservation law in the coordinate y.**

```python
yc = sp.symbols("y", real=True)  # the hidden coordinate y
chart_y = list(coords[:7]) + [yc]  # x1, ..., x7, y
wy = sp.exp(2 * H * yc)  # the warp factor e^{2Hy} = sin^(1/3) z
metric_y = sp.diag(*([sp.exp(2 * a4) * wy] * 3 + [-1]
                     + [-sp.exp(-2 * a4) * wy] * 3 + [1]))
```

The coordinate $y$ replaces $x_8$ (`coords[:7]` are the first seven coordinates); the metric is the warped form of Section 17.13, with $g_{yy} = 1$.

```python
RHO, P3, PT, P8 = (sp.Function(n)(x4, yc) for n in ("rho", "p3", "pt", "p8"))
T_y = sp.diag(P3, P3, P3, -RHO, PT, PT, PT, P8)  # a diagonal source T(x4, y)
div_y = divergence(T_y, metric_y, chart_y)
law_x4 = -sp.diff(RHO, x4) - 3 * sp.diff(a4, x4) * (P3 - PT)
law_y = sp.diff(P8, yc) + 6 * H * P8 - 3 * H * (P3 + PT)
```

A diagonal source whose four parts are unknown functions of $x_4$ and $y$ (capital names, to keep them apart from those of In [7]); its divergence with the same helper; and the two laws of Section 17.13 typed in by hand, for comparison.

```python
derivatives = {sp.Derivative(RHO, x4): sp.Symbol("d4rho"),
               sp.Derivative(P8, yc): sp.Symbol("dyp8"),
               sp.Derivative(a4, x4): sp.Symbol("ad1")}  # short names
functions = {f: sp.Symbol(f.func.__name__) for f in (RHO, P3, PT, P8)}


def short(expression):
    """Write the derivatives as d4rho, dyp8, ad1 and the functions as symbols."""
    return expression.subs(derivatives).subs(functions)
```

Short names for printing, as in In [7]: `dyp8` is $\partial p_8/\partial y$.

```python
say(f"nabla_mu T^mu_x4 = {short(div_y[3])}")
say(f"nabla_mu T^mu_y = {short(div_y[7])}")
others_zero = all(div_y[nu] == 0 for nu in (0, 1, 2, 4, 5, 6))
theory = read_json(KS_THEORY)["emt"]  # the energy-momentum part of the record
say("ks-theory.json, emt.conservationY: " + theory["conservationY"])
reproduces(sp.simplify(div_y[3] - law_x4) == 0 and sp.simplify(div_y[7] - law_y) == 0
           and others_zero
           and "6H p8 = 3H (p3 + p_t)" in theory["conservationY"],
           "in the y chart: the x4 law and dp8/dy + 6H p8 = 3H (p3 + p_t)",
           KS_PY, ["emt_y_conservation_selfconsistent", "emt_x4_component"])
```

The two surviving components are printed, the six others are confirmed to vanish, the record's statement of the $y$ law is printed, and the check requires our components to equal the hand-typed laws and the record to state the same law. Output: `nabla_mu T^mu_x4 = -3*ad1*p3 + 3*ad1*pt - d4rho`, `nabla_mu T^mu_y = -3*H*p3 + 6*H*p8 - 3*H*pt + dyp8`, the record's line `p8' + 6H p8 = 3H (p3 + p_t) for every self-consistent state`, and the PASS line. (PROVED.)

**In [10], the key identity.**

```python
p3_from_law = sp.solve(sp.Eq(law_y, 0), P3)[0]  # p3 from the y conservation law
V = P3 + PT - 2 * P8  # the violation of C2
V_conserved = sp.simplify(V.subs(P3, p3_from_law))
say(f"p3 from the conservation law: {short(p3_from_law)}")
say(f"V = p3 + p_t - 2 p8 for a conserved source: {short(V_conserved)}")
check(sp.simplify(V_conserved - sp.diff(P8, yc) / (3 * H)) == 0,
      "PROVED: for a conserved source V = p3 + p_t - 2 p8 = (dp8/dy) / (3H)")
```

`sp.Eq(law_y, 0)` is the equation "the $y$ law equals 0", and `sp.solve(..., P3)` solves it for $p_3$; it returns a list of solutions, of which `[0]` takes the first (and only) one: $p_3 = 2p_8 - p_t + p_8'/(3H)$. Inserting it into $V$ gives $p_8'/(3H)$, the derivation of Section 17.14. Output: `p3 from the conservation law: 2*p8 - pt + dyp8/(3*H)`, `V = p3 + p_t - 2 p8 for a conserved source: dyp8/(3*H)` and the PASS line. (PROVED.)

**In [11], the identity on the recorded states.**

```python
COLUMNS = ("rho", "p3", "p_t", "p8")  # the four diagonal components


def read_profile(path):
    """A profile table as a dictionary: column name -> numpy array (151 values)."""
    data = np.genfromtxt(path, delimiter=",", names=True)
    return {name: data[name] for name in data.dtype.names}


files = sorted(repository_file(f"{GROUND}/profiles").glob("*.csv"),
               key=lambda path: path.name)
profiles = {path.stem: read_profile(path) for path in files}
with repository_file(f"{GROUND}/emt-integrals.csv").open(
        encoding="utf-8", newline="") as handle:
    integrals = {row["id"]: row for row in csv.DictReader(handle)}
physics = read_json("Revision/kohn_sham/results/parameters.json")["physics"]
H_value, L_cut, VOL7 = physics["H"], physics["L_tipCutoff"], physics["Vol7"]
scale = {sid: float(max(np.max(np.abs(prof[c])) for c in COLUMNS))
         for sid, prof in profiles.items()}  # max|T| of every state
nonzero = [sid for sid in profiles if scale[sid] > 0.0]
y = profiles["N136_lam0_a10"]["y"]  # the common grid of y
h = float(y[1] - y[0])  # the grid step
```

These lines read the 75 profiles, the table of integrals and the parameters, and compute max|T| and the list of nonzero states, exactly as Notebook 17a did (Section 17.11, In [5]). The only new line is the grid step `h`, the distance between two neighbouring grid points, $0.02$.

```python
def slope(values, s=1):
    """dv/dy at the points i = 2s, ..., 150 - 2s (fourth order, step s h)."""
    v = values
    return (-v[4 * s:] + 8 * v[3 * s:-s] - 8 * v[s:-3 * s] + v[:-4 * s]) / (12 * h * s)
```

`slope` estimates the derivative of a tabulated function with the **fourth-order central difference** of step $\delta = sh$:

$$
f'(y) \approx \frac{-f(y + 2\delta) + 8f(y + \delta) - 8f(y - \delta) + f(y - 2\delta)}{12\,\delta} .
$$

Why fourth order? Expand each value in a Taylor series around $y$: $f(y \pm \delta) = f \pm \delta f' + \tfrac{\delta^2}{2}f'' \pm \tfrac{\delta^3}{6}f''' + \tfrac{\delta^4}{24}f'''' \pm \tfrac{\delta^5}{120}f^{(5)} + \dots$, and the same with $2\delta$. Line by line:

$$
8\big[f(y + \delta) - f(y - \delta)\big] = 16\delta f' + \tfrac{16}{6}\delta^3f''' + \tfrac{16}{120}\delta^5f^{(5)} + \dots
$$

(rule: in the difference the even powers cancel and the odd powers double)

$$
-\big[f(y + 2\delta) - f(y - 2\delta)\big] = -4\delta f' - \tfrac{16}{6}\delta^3f''' - \tfrac{64}{120}\delta^5f^{(5)} - \dots
$$

(rule: the same with $2\delta$: $2\cdot 2\delta = 4\delta$, $2(2\delta)^3/6 = 16\delta^3/6$, $2(2\delta)^5/120 = 64\delta^5/120$)

$$
\text{sum} = 12\delta f' - \tfrac{48}{120}\delta^5f^{(5)} + \dots, \qquad \frac{\text{sum}}{12\delta} = f' - \frac{\delta^4}{30}f^{(5)} + \dots
$$

(rule: add; the $\delta^3$ terms cancel; divide by $12\delta$, and $\tfrac{48}{120\cdot 12} = \tfrac{1}{30}$). The error is proportional to $\delta^4$: halving the step divides it by 16. In the code, for the array `v` of 151 values, `v[4*s:]` are the values $f(y_i + 2\delta)$ for the points $i = 2s, \dots, 150 - 2s$, `v[3*s:-s]` the values $f(y_i + \delta)$, `v[s:-3*s]` the values $f(y_i - \delta)$ and `v[:-4*s]` the values $f(y_i - 2\delta)$; all four arrays have $151 - 4s$ entries, and the formula acts on them entry by entry. The first and last $2s$ points have no neighbours on one side and get no slope.

```python
def violation(prof):
    """V(y) = p3 + p_t - 2 p8 of a profile."""
    return prof["p3"] + prof["p_t"] - 2.0 * prof["p8"]


residual = {sid: float(np.max(np.abs(slope(profiles[sid]["p8"]) / (3 * H_value)
                                      - violation(profiles[sid])[2:-2])))
            / scale[sid] for sid in nonzero}
worst = max(residual, key=residual.get)  # the state with the largest difference
```

`violation` returns $V(y)$ of a profile. For each nonzero state, `residual` is the largest difference between $p_8'/(3H)$ (from `slope` with $s = 1$) and $V$ at the inner points (`[2:-2]` drops two points at each end, to match), divided by max|T|. `worst` is the state with the largest value.

```python
report("states with a nonzero tensor", len(nonzero))
report("grid step h", f"{h:.2f}")
report("largest |(dp8/dy)/(3H) - V| / max|T| over 70 states", f"{residual[worst]:.2e}",
       f"({worst})")
check(len(nonzero) == 70 and residual[worst] < 1e-3,
      "V = (dp8/dy)/(3H) on every state to 1e-3 of max|T| (fourth-order differences)")
```

The third `report` passes the state's name in brackets as its third argument, the place of the unit, so that it is printed after the number. `:.2e` writes a number with two decimals in the computer's power-of-ten form, `1.05e-04` for $1.05 \times 10^{-4}$. Output: 70 states, $h = 0.02$, the largest difference $1.05 \times 10^{-4}$ of max|T| (state `N8_lamm1_a00`), and the PASS line. (COMPUTED; the bound $10^{-3}$ was fixed before the run. The solver, on its own grid of 900 steps of $3/900 = 1/300$ (six times finer than the stored grid of 150 steps of $0.02$), checks the same law with fourth-order differences to a relative residual of at most $1.951 \times 10^{-8}$: `Revision/kohn_sham/reports/ks-rust-solver.json`, check `emt_y_conservation_pointwise`; the number of steps is the record `Revision/kohn_sham/results/parameters.json`, key `numerics.rk4Steps`.)

**In [12], the identity drawn (figure 2).**

```python
SLICES = {"a00": 0.0, "a05": 0.5, "a10": 1.0, "a15": 1.5, "a20": 2.0}  # a4,0
SHADES = ["#86b6ef", "#5598e7", "#2a78d6", "#1c5cab", "#104281"]  # light to dark
history136 = [f"N136_lam0_{tag}" for tag in SLICES]
fig, (left, right) = plt.subplots(1, 2, figsize=(9.6, 4.0))
for shade, sid, a40 in zip(SHADES, history136, SLICES.values()):
    left.plot(y, profiles[sid]["p8"] / scale[sid], color=shade, lw=1.8,
              label=f"$a_{{4,0}} = {a40:g}$")
left.set_yscale("symlog", linthresh=1e-6)
left.set_xlabel("hidden coordinate $y$ (tip $-3$, brane $0$)")
left.set_ylabel("$p_8(y)$ / max|T|")
left.set_title("$N = 136$, $\\lambda = 0$: $p_8$ is far from flat")
left.legend(fontsize=7, loc="upper right")
```

The slices, shades and the history $N = 136$, $\lambda = 0$ as in Notebook 17a. The left panel draws $p_8/\max|T|$ of the five states on a symmetric logarithmic axis, linear between $-10^{-6}$ and $10^{-6}$.

```python
example = profiles["N136_lam0_a10"]
inner = y[2:-2]  # the points where the slope is known
right.plot(y, violation(example) / scale["N136_lam0_a10"], color="#2a78d6",
           lw=2.0, label="$V = p_3 + p_t - 2p_8$")
right.plot(inner[::5], (slope(example["p8"]) / (3 * H_value))[::5]
           / scale["N136_lam0_a10"], "o", color="#eb6834", ms=3.5,
           label="$p_8'(y)/(3H)$")
right.axhline(0.0, color="#e34948", ls="--", lw=1.0, label="C2: $V = 0$")
right.set_yscale("symlog", linthresh=1e-6)
right.set_xlabel("hidden coordinate $y$")
right.set_ylabel("divided by max|T|")
right.set_title("$a_{4,0} = 1$: the two sides of the identity")
right.legend(fontsize=7, loc="upper right")
fig.tight_layout()
```

The right panel draws, for the slice $a_{4,0} = 1$, the violation $V$ as a blue line over all points and $p_8'/(3H)$ as orange dots at every fifth inner point (`[::5]` takes every fifth entry), both divided by max|T|, with the red dashed line $V = 0$ and the same kind of axis.

```python
p8_range = [float(np.max(np.abs(profiles[s]["p8"])) / np.min(np.abs(profiles[s]["p8"])))
            for s in history136]  # how far p8 is from flat, per slice
```

`p8_range` holds, per slice, the largest $|p_8|$ divided by the smallest.

```python
save_figure(fig, "slope_identity",
            "Left: the hidden-direction pressure $p_8(y)$ of the Kohn-Sham states "
            "$N = 136$, $\\lambda = 0$ at the five slices $a_{4,0} = 0$ to $2$, "
            "divided by the largest component of each state (horizontal axis: the "
            "hidden coordinate $y$; vertical axis symmetric logarithmic, linear "
            "between $-10^{-6}$ and $10^{-6}$); the largest $|p_8|$ is "
            f"{min(p8_range):.0f} to ${tex_number(max(p8_range))}$ times the "
            "smallest, while "
            "condition C2 of a conserved source demands a flat $p_8$. Right: for "
            "$a_{4,0} = 1$ the violation $V = p_3 + p_t - 2p_8$ (blue line) and the "
            "slope $p_8'(y)/(3H)$ from fourth-order differences (orange dots) lie "
            "on top of each other, as the conservation law demands; the dashed "
            "line is the value $0$ that C2 needs.")
```

The caption, joined from its strings, inserts the range of `p8_range`: the smallest with no decimals, 2933, and the largest in powers of ten, $2.3 \times 10^{6}$. The prime in the text $p_8'(y)$ is an ordinary character of a string written in double quotation marks. Output: figure 17b.2 and its saved line.

**What figure 17b.2 shows.** Left: horizontal axis $y$ (units of $1/H$), vertical axis $p_8/\max|T|$ (a pure number, symmetric logarithmic). At the tip $p_8$ is negative and as large as max|T| (the $-10^0$ at the lower left); it rises steeply, crosses zero between $y \approx -2.6$ and $y \approx -2.35$, reaches a maximum and falls toward the brane by several powers of ten. For C2, by Section 17.14, every curve would have to be horizontal. Right: the blue line $V$ and the orange dots $p_8'/(3H)$ lie on top of each other along the whole patch, positive on the tip side of the maximum of $p_8$ and negative on the brane side: the student sees the identity $V = p_8'/(3H)$ at work, and why $V$ changes sign once.

**In [13], the differences have order 4 (figure 3).**

```python
STEPS = np.array([1, 2, 3, 5, 6])  # the step is s h
POINTS = [30, 60, 90, 120]  # grid indices of y = -2.4, -1.8, -1.2, -0.6
STUDY = ["N8_lamp1_a00", "N136_lam0_a10", "N136_lamp2_a20", "N688_lam0_a10",
         "N688_lamm2_a00"]
```

Five step multipliers $s$; four grid points (index $i$ is $y = -3 + 0.02\,i$: index 30 is $y = -2.4$, and so on); five states of all three particle numbers.

```python
def difference_at_points(sid, s):
    """max over POINTS of |(dp8/dy)/(3H) - V| / max|T| with the step s h."""
    prof = profiles[sid]
    derivative = slope(prof["p8"], s) / (3 * H_value)  # index i - 2s is point i
    return max(abs(float(derivative[i - 2 * s] - violation(prof)[i]))
               for i in POINTS) / scale[sid]
```

For one state and one step: the slope array starts at the grid point $2s$, so its entry `i - 2*s` belongs to the grid point $i$; the function returns the largest difference $|p_8'/(3H) - V|$ at the four points, divided by max|T|.

```python
errors = {sid: np.array([difference_at_points(sid, s) for s in STEPS])
          for sid in STUDY}
orders = {sid: float(np.polyfit(np.log(STEPS * h), np.log(errors[sid]), 1)[0])
          for sid in STUDY}  # the slope of the straight-line fit
for sid in STUDY:
    say(f"{sid}: differences " + ", ".join(f"{e:.1e}" for e in errors[sid])
        + f";  fitted order {orders[sid]:.2f}")
check(all(3.8 < order < 4.2 for order in orders.values()),
      "the differences fall like (step)^4: they are errors of the differences")
```

`errors` holds the five differences of each state. If the difference is an error of order 4, it is $C\delta^4$ with a constant $C$, so $\ln(\text{difference}) = \ln C + 4\ln\delta$: a straight line of slope 4 in the logarithms. `np.polyfit(x, y, 1)` fits a straight line $y \approx c_1x + c_0$ by least squares and returns $[c_1, c_0]$; `[0]` takes the slope. Output: one line per state, for example `N136_lam0_a10: differences 4.6e-07, 7.5e-06, 3.8e-05, 3.0e-04, 6.5e-04; fitted order 4.04`; the fitted orders are 4.08, 4.04, 4.02, 4.04 and 4.04; and the PASS line. (COMPUTED.) Had the conservation law failed, the differences would stop falling at the size of the failure; instead they fall like $\delta^4$ down to $5 \times 10^{-7}$ of max|T| at the smallest step.

```python
fig, ax = plt.subplots(figsize=(6.4, 4.4))
for sid in STUDY:
    ax.loglog(STEPS * h, errors[sid], "o-", lw=1.4, ms=4,
              label=f"{sid} (order {orders[sid]:.2f})")
reference = errors["N136_lam0_a10"][0] * (STEPS / STEPS[0]) ** 4.0
ax.loglog(STEPS * h, reference, "k--", lw=1.0, label="slope 4 (reference)")
ax.set_xlabel("step of the difference $s h$ (units of $1/H$)")
ax.set_ylabel("max $|p_8'/(3H) - V|$ / max|T|")
ax.legend(fontsize=7)
```

`ax.loglog` draws with both axes logarithmic; `"o-"` means circles joined by lines, and each state's legend entry carries its fitted order. The black dashed reference line (the format string is the letter k, for black, and two hyphens, for dashes) starts at the first point of the state `N136_lam0_a10` and grows like the fourth power of the step: `STEPS / STEPS[0]` is the step relative to the smallest one, and `** 4.0` raises it to the fourth power.

```python
save_figure(fig, "difference_order",
            "The difference between $p_8'(y)/(3H)$, computed with fourth-order "
            "differences of step $sh$ ($h = 0.02$, $s = 1, 2, 3, 5, 6$), and the "
            "violation $V = p_3 + p_t - 2p_8$, at the four points $y = -2.4$, "
            "$-1.8$, $-1.2$, $-0.6$, divided by the largest component of the state, "
            "for five recorded Kohn-Sham states (logarithmic axes; the step in units "
            "of $1/H$). The fitted slopes lie between "
            f"{min(orders.values()):.2f} and {max(orders.values()):.2f}, the order "
            "4 of the differences: the small differences are errors of the finite "
            "differences, and the conservation law itself holds.")
```

The caption, joined from its strings, inserts the smallest and the largest fitted order with two decimals, 4.02 and 4.08. Output: figure 17b.3 and its saved line.

**What figure 17b.3 shows.** Horizontal axis: the step $sh$ from 0.02 to 0.12 (units of $1/H$); vertical axis: the largest difference divided by max|T| (pure number); both logarithmic. Five straight lines, parallel to the dashed reference of slope 4: the differences are pure errors of the finite differences, and the conservation law itself holds for the recorded states.

**In [14], the integrated law.**

```python
def number(sid, column):
    """A number of the record's table of integrals."""
    return float(integrals[sid][column])


tip_weight = float(np.exp(-6.0 * H_value * L_cut))  # e^{-6HL}, about 1.5e-8
integrated = {}
for sid in nonzero:
    left_side = 2 * VOL7 * (number(sid, "p8_brane") - tip_weight * number(sid, "p8_tip"))
    right_side = 3 * H_value * (number(sid, "int_p3") + number(sid, "int_p_t"))
    integrated[sid] = abs(left_side - right_side) / abs(right_side)
worst_integrated = max(integrated, key=integrated.get)
report("largest relative difference of the integrated law",
       f"{integrated[worst_integrated]:.3e} ({worst_integrated})")
```

`number` reads a number of the table. `tip_weight` is $e^{-6HL} = e^{-18}$. For each nonzero state the two sides of the integrated law of Section 17.15 are computed from the table's columns `p8_brane`, `p8_tip`, `int_p3` and `int_p_t`, and their relative difference is stored. Output: the largest relative difference is $1.421 \times 10^{-11}$ (state `N8_lamm2_a00`).

```python
column = {sid: number(sid, "ycons_integrated_rel") for sid in nonzero}
column_worst = max(column, key=column.get)  # the solver's own largest value
report("largest value of the column ycons_integrated_rel",
       f"{column[column_worst]:.3e} ({column_worst})")
solver = record_entry(KS_RUST, "emt_y_conservation_integrated")["detail"]
say("the solver record: " + solver)
```

The table also has a column `ycons_integrated_rel`: the solver's own relative difference of the same two sides, computed from its unrounded internal numbers and divided by the largest of the terms involved (the integral, the boundary term, the tip term and the size of the cancelling terms), not by the right side alone as our number is; so the two are close cousins, not the same quantity by definition. Its largest value is $1.422 \times 10^{-11}$, also at `N8_lamm2_a00`, against our $1.421 \times 10^{-11}$. The text of the solver's check `emt_y_conservation_integrated` is printed: 75 cases, worst value $1.422 \times 10^{-11}$ (`N8_lamp2_a00`), tolerance $10^{-7}$, no failures.

```python
named = solver.split("worst value ")[1].split("(")[1].split(")")[0]  # its state
tie = abs(column[named] - column[column_worst]) < 1e-15  # mirror states tie
report("the state named by the record and its column value",
       f"{named}, {column[named]:.3e}")
reproduces(integrated[worst_integrated] < 1e-10 and tie
           and f"worst value {column[column_worst]:.3e}" in solver,
           "the integrated conservation law holds for all 70 states",
           KS_RUST, ["emt_y_conservation_integrated"])
```

The state named by the record is cut out of its text: after `worst value `, after the next `(`, before the next `)`. The record names `N8_lamp2_a00`, our maximum is `N8_lamm2_a00`: the two states with $N = 8$ and $\lambda = \pm\lambda_2$ have tensors of opposite sign and equal size (the record's table: for example $\int\rho = \mp 0.00286265$), so their relative differences are equal, and `tie` confirms it to $10^{-15}$. The check passes when our largest difference is below $10^{-10}$, the tie holds and the record's worst value equals the column's. Output: the state and its value, and the PASS line. (COMPUTED. The pair $\pm\lambda$ of these zero-mode states is a property of these particular recorded states; it is not one of the pairing theorems of Chapters 18 to 20.)

**In [15], why the averaged ratio is not 1.**

```python
mean_p8 = {sid: number(sid, "int_p8") / (2 * VOL7 * (1 - tip_weight) / (6 * H_value))
           for sid in nonzero}  # the weighted mean of p8
ratio = {sid: (number(sid, "int_p3") + number(sid, "int_p_t"))
         / (2 * number(sid, "int_p8")) for sid in nonzero}  # as in Notebook 17a
boundary = {sid: (number(sid, "p8_brane") - tip_weight * number(sid, "p8_tip"))
            / (1 - tip_weight) for sid in nonzero}  # the boundary value b8
from_brane = {sid: boundary[sid] / mean_p8[sid] for sid in nonzero}  # R = b8/mean
brane_only = {sid: number(sid, "p8_brane") / mean_p8[sid] for sid in nonzero}
tip_share = {sid: 1.0 - brane_only[sid] / from_brane[sid] for sid in nonzero}
```

Six dictionaries: the weighted mean $\bar p_8$ of Section 17.7; the ratio $R$ as Notebook 17a computed it; the boundary value $b_8 = [p_8(0) - e^{-6HL}p_8(-L)]/(1 - e^{-6HL})$ of Section 17.15; $R$ computed the other way, $b_8/\bar p_8$; the ratio that the brane value alone would give, $p_8(0)/\bar p_8$; and the share of $R$ that the tip term supplies, $1 - p_8(0)/b_8$ (the quotient of the last two ratios, subtracted from 1).

```python
agreement = max(abs(from_brane[sid] / ratio[sid] - 1.0) for sid in nonzero)
closest = min(ratio, key=lambda sid: abs(ratio[sid] - 1.0))
report("largest relative difference of the two forms of R", f"{agreement:.1e}")
report("R closest to 1", f"{ratio[closest]:.6g} ({closest})")
for n in (8, 136, 688):
    shares = [tip_share[sid] for sid in nonzero if sid.startswith(f"N{n}_")]
    report(f"share of R from the tip term, N = {n}",
           f"{min(shares):.2g} to {max(shares):.2g}")
detail = record_entry(SOURCE_REPORT, "ks_integrals_violate_algebraic_condition")[
    "detail"]
reproduces(agreement < 1e-9
           and f"(closest to 1: {ratio[closest]:.6g} at {closest})" in detail,
           "R = b8 / mean of p8 (b8: brane value with the tip term), 70 states",
           SOURCE_REPORT, ["ks_integrals_violate_algebraic_condition"])
```

`agreement` is the largest relative difference of the two forms of $R$ over all nonzero states. The loop collects, for each particle number, the tip shares of its states (`startswith` tests the beginning of the name) and prints the smallest and the largest with two significant digits (`.2g`). Output: $1.4 \times 10^{-11}$; the ratio closest to 1 is again 0.414328 (`N688_lamm2_a00`), the record's number; the tip shares, $0.31$ to $0.33$ for $N = 8$, $4.1 \times 10^{-5}$ to $0.039$ for $N = 136$ and $5.3 \times 10^{-6}$ to $0.025$ for $N = 688$; and the PASS line. (COMPUTED. So the tip term matters little for the states with 3-momentum but supplies about a third of $R$ for the brane zero modes $N = 8$, Section 17.15.)

**In [16], the boundary value against the mean (figure 4).**

```python
N_COLOURS = {8: "#1baf7a", 136: "#2a78d6", 688: "#eb6834"}
fig, ax = plt.subplots(figsize=(6.4, 5.0))
for n, colour in N_COLOURS.items():
    for positive in (True, False):
        ids = [sid for sid in nonzero if sid.startswith(f"N{n}_")
               and (mean_p8[sid] > 0) == positive]  # one sign at a time
        if not ids:
            continue
        ax.loglog([abs(mean_p8[sid]) for sid in ids],
                  [abs(boundary[sid]) for sid in ids], "o",
                  ms=5 if positive else 10,  # rings around the mirror states
                  color=colour, mfc=colour if positive else "none",
                  label=f"$N = {n}$" + ("" if positive else ", mean $< 0$"))
```

For each particle number and each sign of $\bar p_8$, the states of that kind are collected (`(mean > 0) == positive` selects one sign); an empty group is skipped. The points are drawn on logarithmic axes, which need positive numbers, so absolute values are used: horizontal $|\bar p_8|$, vertical the boundary value $|b_8|$ of In [15]. Their ratio is exactly $R$. States with a positive mean get small filled circles; states with a negative mean get larger rings (`mfc`, the marker face colour, is `"none"`, so only the outline is drawn).

```python
line = np.array([1e-7, 1.0])  # the range of the diagonal
ax.loglog(line, line, "--", color="#e34948", lw=1.2,
          label="averaged C2: boundary value = mean")
ax.set_xlabel("weighted mean $|\\bar p_8|$ (units of $m^8$)")
ax.set_ylabel("boundary value $|b_8|$ (units of $m^8$)")
ax.legend(fontsize=8, loc="upper left")
negative = sorted(sid for sid in nonzero if mean_p8[sid] < 0)  # mean of p8 < 0
say("states with a negative mean of p8: " + ", ".join(negative))
expected = sorted(sid for sid in nonzero if sid.startswith("N8_lamp"))
```

The red dashed diagonal is where the boundary value equals the mean, the averaged C2 ($R = 1$). The cell prints the states with a negative mean, and `expected` lists the ten $N = 8$ states with $\lambda > 0$ (their names start with `N8_lamp`).

```python
plotted = {sid: boundary[sid] / mean_p8[sid] for sid in nonzero}  # = R
save_figure(fig, "brane_and_mean",
            "The boundary value $b_8 = (p_8(0) - e^{-6HL}p_8(-L))/(1 - e^{-6HL})$ "
            "of the hidden-direction pressure against its weighted mean, for the "
            ...)
check(negative == expected and all(0.0 < plotted[sid] < 1.0 for sid in nonzero),
      "every point lies below the diagonal; mean of p8 < 0 only for N = 8, "
      "lambda > 0")
```

`plotted` holds the ratio of the vertical to the horizontal value of every point, $b_8/\bar p_8$, which is $R$. The caption is quoted shortened (it is printed in full under the figure); joined from its strings, it inserts the range of the plotted ratios with three decimals, 0.107 to 0.414, and the range that the brane value alone would give, 0.074 to 0.414 (`min` and `max` of the dictionaries `plotted` and `brane_only`). The check confirms that the states with a negative mean are exactly the expected ten, and that every plotted ratio lies strictly between 0 and 1 (Python allows the chained comparison `0.0 < r < 1.0`). Output: the list `N8_lamp1_a00` to `N8_lamp2_a20`, figure 17b.4 with its saved line, and then the PASS line (the check comes after the figure).

**What figure 17b.4 shows.** Both axes logarithmic, in units of $m^8$. The averaged C2 would put every point on the dashed diagonal. All 70 points lie below it: the boundary value of $p_8$ is between about a tenth and four tenths of its mean, the ratios $R$ = 0.107 to 0.414 of Notebook 17a. For the $N = 136$ and $N = 688$ states the boundary value is practically the brane value; for the $N = 8$ states the brane value alone would be only 0.074 of the mean, and the tip term raises the ratio to about 0.11 (near the tip $p_8$ has the sign opposite to its mean, so $-e^{-6HL}p_8(-L)$ has the sign of the mean). The blue ($N = 136$) and orange ($N = 688$) points form two short chains, one point per slice (the couplings overlap); the 20 nonzero $N = 8$ states, equal at every slice, fall on only two places, where the filled points of $-\lambda_1$ and $-\lambda_2$ sit inside the rings of $+\lambda_1$ and $+\lambda_2$ (same size, opposite sign: for $+\lambda$ the mean and the brane value of $p_8$ are negative, while $p_8$ at the tip is positive).

**In [17], the constraint propagates.**

```python
ad1, ad2 = sp.symbols("ad1 ad2", real=True)  # a4' and a4''
alpha = sp.symbols("alpha1:4", real=True)  # the Lovelock couplings
kappa, p3s, pts = sp.symbols("kappa p3 pt", real=True)  # kappa and the pressures
LOCALS = {"ad1": ad1, "ad2": ad2, "H": H, "alpha1": alpha[0], "alpha2": alpha[1],
          "alpha3": alpha[2]}


def parse(text):
    """A formula of the record (Wolfram Language text) as a sympy expression."""
    return sp.sympify(text.replace("^", "**"), locals=LOCALS)
```

New symbols: $a_4'$ and $a_4''$, the three couplings (`"alpha1:4"` makes `alpha1`, `alpha2`, `alpha3`), $\kappa$ and two pressures (named `p3s` and `pts` in the code, to keep them apart from the functions of In [7]). `parse` reads a formula of the record, as in Notebook 17a.

```python
E44 = sum(alpha[k - 1] * parse(equations["lovelockTensors"][f"E{k}"]["x4x4"]["input"])
          for k in (1, 2, 3))  # sum_k alpha_k E_(k)^x4_x4
F = parse(equations["generalSource"]["evolution_F"]["input"])
rho_dot = -3 * ad1 * (p3s - pts)  # the x4 conservation law
constraint_dot = sp.diff(E44, ad1) * ad2 + kappa * rho_dot  # chain rule
evolution = ad2 * F - kappa * (p3s - pts)
```

`E44` is $e_{44} = \sum_k\alpha_kE_{(k)}{}^{x_4}{}_{x_4}$ from the record, `F` the record's $F$, `rho_dot` the energy-change law, `constraint_dot` the derivative $d\mathcal C/dx_4 = (de_{44}/da')\,a_4'' + \kappa\rho'$ of Section 17.16, and `evolution` the expression $\mathcal E$.

```python
say(f"d/d(a4') of the x4 component: {sp.factor(sp.diff(E44, ad1))}")
say(f"3 a4' F: {sp.factor(3 * ad1 * F)}")
reproduces(sp.expand(constraint_dot - 3 * ad1 * evolution) == 0,
           "PROVED: dC/dx4 = 3 (da4/dx4) times the evolution equation, any alpha_k",
           WL_A4, ["constraint_propagation_bianchi"])
linear = sp.expand(constraint_dot.subs({ad2: 0, ad1: sp.Symbol("A") * H}))
say(f"along the linear member a4 = A H x4: dC/dx4 = {sp.factor(linear)}")
```

`sp.factor` writes an expression as a product of factors. The two printed lines show $de_{44}/da'$ and $3a'F$; they are the same, $6a'(\alpha_1 - 24\alpha_2a'^2 - 40\alpha_2H^2 + 360\alpha_3a'^4 + 432\alpha_3a'^2H^2 + 360\alpha_3H^4)$, the fact derived by hand in Section 17.16. The check confirms $d\mathcal C/dx_4 - 3a_4'\mathcal E = 0$ for all couplings (PROVED; Wolfram report, check `constraint_propagation_bianchi`). Then $a_4'' = 0$ and $a_4' = AH$ are inserted. Output: the two factored lines, the PASS line and `along the linear member a4 = A H x4: dC/dx4 = -3*A*H*kappa*(p3 - pt)`.

**In [18], the energy exchange along the history.**

```python
history = read_json("Revision/kohn_sham/results/adiabatic/history.json")
no_crossing = all(not series["fermiLevelCrossings"] for series in history["series"])
TAGS = ["lamm2", "lamm1", "lam0", "lamp1", "lamp2"]  # the five couplings
simpson_error, energies, drives = {}, {}, {}
```

The solver's record of the history lists, for each of the 15 series, the places where a level crosses the Fermi level between slices; `not series["fermiLevelCrossings"]` is true when that list is empty. Comparing the energies of different slices is fair only if each state is followed continuously, so `no_crossing` must be true. `TAGS` are the coupling parts of the names; three empty dictionaries will collect the results.

```python
for n in (8, 136, 688):
    for tag in TAGS:
        ids = [f"N{n}_{tag}_{s}" for s in SLICES]
        E = np.array([number(sid, "int_rho") for sid in ids])  # E at the slices
        drive = np.array([-3 * (number(sid, "int_p3") - number(sid, "int_p_t"))
                          for sid in ids])  # dE/da4 at the slices
        simpson = 0.5 / 3 * (drive[0] + 4 * drive[1] + 2 * drive[2]
                             + 4 * drive[3] + drive[4])  # step 0.5, from 0 to 2
        energies[(n, tag)], drives[(n, tag)] = E, drive
        change = E[-1] - E[0]
        simpson_error[(n, tag)] = (abs(simpson - change) / abs(change)
                                   if change != 0.0 else abs(simpson))
```

For each of the 15 series: the energies $E = \int\rho$ at the five slices; the rates $dE/da_{4,0} = -3(\int p_3 - \int p_t)$ of Section 17.16; and **Simpson's rule** for the integral of the rate from $a_{4,0} = 0$ to 2. On one pair of steps of width $h$, Simpson's rule is $\int_a^{a+2h}f \approx \tfrac{h}{3}[f(a) + 4f(a + h) + f(a + 2h)]$ (the exact integral of the parabola through the three points; its error falls like $h^4$). With $h = 0.5$ on $[0, 1]$ and on $[1, 2]$ and the two added, the middle value $f(1)$ appears twice: $\tfrac{0.5}{3}[f_0 + 4f_1 + 2f_2 + 4f_3 + f_4]$. The results are stored under the key `(n, tag)` (a tuple can be a key of a dictionary). The relative error compares Simpson's integral with the recorded change $E(2) - E(0)$; when the change is zero (the $N = 8$ series) the absolute value is stored instead.

```python
moving = [key for key in simpson_error if key[0] != 8]
largest = max(simpson_error[key] for key in moving)
unchanged = all(np.all(energies[(8, tag)] == energies[(8, tag)][0])
                and np.all(drives[(8, tag)] == 0.0) for tag in TAGS)
```

The ten series with $N = 136$ or $688$ move; `largest` is their largest relative error. `unchanged` confirms that every $N = 8$ series has the same energy at every slice and zero rate (their $p_3 = p_t$, Notebook 17a, In [18]).

```python
for n in (136, 688):
    E, error = energies[(n, "lam0")], simpson_error[(n, "lam0")]
    say(f"N = {n}, lambda = 0: E(0) = {E[0]:.6g}, E(2) = {E[-1]:.6g}, "
        f"change {E[-1] - E[0]:.6g}, relative Simpson error {error:.1e}")
report("largest relative Simpson error, N = 136 and 688", f"{largest:.1e}")
reproduces(no_crossing and largest < 1e-3 and unchanged,
           "E(2) - E(0) = integral of -3 (int p3 - int p_t) along the history",
           KS_RUST, ["emt_energy_change_dE_da4"])
```

Output: for $N = 136$, $\lambda = 0$: $E(0) = 80.2822$, $E(2) = 12.4451$, change $-67.8372$, relative Simpson error $2.1 \times 10^{-4}$; for $N = 688$: $680.441$, $110.387$, $-570.055$, $2.2 \times 10^{-4}$; the largest relative error of the ten moving series, $2.2 \times 10^{-4}$; and the PASS line, which also requires the solver's check `emt_energy_change_dE_da4` (the same law with tiny steps of $a_4$) to be PASS. (COMPUTED. The remaining error is that of Simpson's rule with only five slices, not of the law: the solver checks the law with steps of $0.002$ in $a_4$ to $1.5 \times 10^{-10}$, measured as in Section 17.16.)

**In [19], the energy along the history (figure 5).**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(9.6, 4.0))
slice_values = np.array(list(SLICES.values()))
for n, marker in ((136, "o"), (688, "s")):
    E, drive = energies[(n, "lam0")], drives[(n, "lam0")]
    to_one = E[0] + 0.5 / 3 * (drive[0] + 4 * drive[1] + drive[2])  # 0 to 1
    to_two = to_one + 0.5 / 3 * (drive[2] + 4 * drive[3] + drive[4])  # 1 to 2
    left.plot(slice_values, E / E[0], marker=marker, color=N_COLOURS[n], lw=1.6,
              label=f"$N = {n}$: recorded $E$")
    left.plot([1.0, 2.0], [to_one / E[0], to_two / E[0]], "x", color="black",
              ms=9, mew=1.6)
```

For $N = 136$ (circles) and $N = 688$ (squares) with $\lambda = 0$, the left panel draws $E/E(0)$ at the five slices, and black crosses (`"x"`, with marker edge width `mew`) at the energies predicted from $E(0)$ by one Simpson step to $a_{4,0} = 1$ and a second to $a_{4,0} = 2$.

```python
left.plot([], [], "x", color="black", label="from $E(0)$ by Simpson")
left.axhline(1.0, color="#e34948", ls="--", lw=1.2, label="C3: constant energy")
left.set_xlabel("slice $a_{4,0}$ (history $a_4 = Hx_4$)")
left.set_ylabel("$E(a_{4,0}) / E(0)$")
left.set_ylim(0.0, 1.1)
left.legend(fontsize=7, loc="lower left")
```

A legend entry for the crosses (an empty plot, as in Notebook 17a, In [15]), the red dashed line of the constant energy that C3 needs, labels, the vertical range and the legend.

```python
keys = [(n, tag) for n in (136, 688) for tag in TAGS]
labels = [f"{n}, {tag[3:]}" for n, tag in keys]  # N and the coupling tag
right.bar(range(len(keys)), [simpson_error[key] * 1e4 for key in keys],
          color=[N_COLOURS[n] for n, _ in keys])
right.set_xticks(range(len(keys)), labels, rotation=60, fontsize=7)
right.set_xlabel("series ($N$, coupling: m2 $= -\\lambda_2$, ..., p2 $= +\\lambda_2$)")
right.set_ylabel("relative Simpson error ($10^{-4}$)")
fig.tight_layout()
```

The right panel draws one bar per moving series: its relative Simpson error times $10^4$, coloured by $N$; the bars are labelled with $N$ and the coupling tag (`tag[3:]` drops `lam`), turned by 60 degrees.

```python
fall = [energies[(n, "lam0")][0] / energies[(n, "lam0")][-1] for n in (136, 688)]
```

`fall` is the factor by which the energy falls from the first to the last slice, for $N = 136$ and $N = 688$.

```python
save_figure(fig, "energy_exchange",
            "Left: the total energy $E = \\int\\rho$ of the Kohn-Sham states with "
            "$\\lambda = 0$ along the history $a_4 = Hx_4$, divided by its value at "
            "$a_{4,0} = 0$ (circles $N = 136$, squares $N = 688$; pure numbers), "
            "the values predicted from $E(0)$ by integrating "
            "$dE/da_4 = -3(\\int p_3 - \\int p_t)$ with Simpson's rule (crosses), "
            "and the constant energy that condition C3 of the linear member needs "
            f"(dashed). The energy falls by factors of {fall[0]:.2f} and "
            f"{fall[1]:.2f}: as 3-space inflates and the extra times deflate, the "
            "gas with $p_3 > p_t = 0$ gives up energy. Right: the relative error of "
            "Simpson's rule for $E(2) - E(0)$ in all ten moving series, in units of "
            f"$10^{{-4}}$ (largest ${tex_number(largest)}$): the energy-change law "
            "holds to "
            "the accuracy of the five slices.")
```

The caption, joined from its strings, inserts the two factors with two decimals, 6.45 and 6.16, and the largest relative Simpson error of In [18] in powers of ten, $2.2 \times 10^{-4}$ (`$10^{{-4}}$` in an f-string prints as $10^{-4}$). Output: figure 17b.5 and its saved line.

**What figure 17b.5 shows.** Left: horizontal axis the slice $a_{4,0}$; vertical axis $E/E(0)$, a pure number. The recorded energies of $N = 136$ and $N = 688$ fall to about 0.4 at $a_{4,0} = 1$ and to about 0.16 at $a_{4,0} = 2$, and the crosses predicted from $E(0)$ by the energy-change law sit on them; C3 would need the dashed line at 1. As 3-space inflates and the extra times deflate, the gas, with $p_t = 0$ and $\int p_3 > 0$ (the caption's short form is $p_3 > p_t = 0$), gives up energy, exactly as the energy law of the patch demands. Right: the relative Simpson errors of the ten moving series, between about 1.9 and 2.2 in units of $10^{-4}$: the energy-change law holds to the accuracy that five slices allow.

**In [20], the time law tested point by point.**

```python
def change_with_a4(n, tag):
    """d rho / d a4 at the slice a4,0 = 1 at every y (fourth order, step 0.5)."""
    v = [profiles[f"N{n}_{tag}_{s}"]["rho"] for s in SLICES]  # rho at 5 slices
    return (v[0] - 8 * v[1] + 8 * v[3] - v[4]) / (12 * 0.5)
```

`change_with_a4` collects, for one series, the five profiles of $\rho$ at the slices $a_{4,0} = 0, 0.5, 1, 1.5, 2$ (each an array of 151 values, one per grid point $y$) and applies the fourth-order central difference of In [11] in the variable $a_4$, centred on the middle slice $a_{4,0} = 1$ with the step $\delta = 0.5$: $[f(0) - 8f(0.5) + 8f(1.5) - f(2)]/(12 \times 0.5)$, the formula of In [11] with $f(1 - 2\delta) = f(0)$, $f(1 - \delta) = f(0.5)$, $f(1 + \delta) = f(1.5)$ and $f(1 + 2\delta) = f(2)$ (the middle value $f(1)$ does not enter). Because the arrays are subtracted element by element, the result is $\partial\rho/\partial a_4$ at every grid point at once.

```python
weight = np.exp(6 * H_value * y)  # the volume weight e^(6Hy) on the grid


def patch_integral(values):
    """Simpson's rule for the integral of e^(6Hy) times values over the patch."""
    f = weight * values
    return h / 3 * (f[0] + f[-1] + 4 * f[1:-1:2].sum() + 2 * f[2:-1:2].sum())
```

`weight` is $e^{6Hy}$ at the 151 grid points. `patch_integral` is Simpson's rule on the grid of step $h = 0.02$ (150 intervals, an even number): the two end values once, the values at odd positions (`f[1:-1:2]`, every second value from index 1 to the last but one) four times, the values at even inner positions (`f[2:-1:2]`) twice, all times $h/3$.

```python
tip_ratio, integral_gap = {}, {}
for n, tag in moving:
    middle = profiles[f"N{n}_{tag}_a10"]  # the slice a4,0 = 1
    left_side = change_with_a4(n, tag)  # d rho / d a4 at every y
    right_side = -3 * (middle["p3"] - middle["p_t"])  # what the law needs there
    tip_ratio[(n, tag)] = float(left_side[0] / right_side[0])  # at y = -3
    integral_gap[(n, tag)] = float(abs(patch_integral(left_side)
                                       / patch_integral(right_side) - 1.0))
```

For each of the ten moving series of In [18] (`moving`, $N = 136$ and $688$): the left side $\partial\rho/\partial a_4$ and the right side $-3(p_3 - p_t)$ of the pointwise law at the slice $a_{4,0} = 1$ (along the history $a_4' = H = 1$, so $\partial\rho/\partial x_4 = \partial\rho/\partial a_4$). `tip_ratio` stores their ratio at the first grid point, the tip $y = -3$ (index 0); `integral_gap` stores the relative difference of the two sides after both are integrated over the patch with the weight $e^{6Hy}$, which is the law for the energy of the patch.

```python
slice_one = profiles["N136_lam0_a10"]
rate136 = change_with_a4(136, "lam0")
for index, place in ((0, "-3 (tip)"), (75, "-1.5"), (150, "0 (brane)")):
    needed = -3 * (slice_one["p3"][index] - slice_one["p_t"][index])
    say(f"N = 136, lambda = 0, a4,0 = 1, y = {place}: d rho/d a4 = "
        f"{rate136[index]:.4g}, -3 (p3 - p_t) = {needed:.4g}")
```

For the canonical state $N = 136$, $\lambda = 0$, the two sides are printed at three grid points: index 0 ($y = -3$), 75 ($y = -3 + 75 \times 0.02 = -1.5$) and 150 ($y = 0$), with four significant digits (`.4g`). Output: at the tip $82.97$ against $-474.8$; in the middle $-0.4505$ against $-1.497$; at the brane $-0.002068$ against $-0.001174$.

```python
report("ratio of the two sides at the tip, 10 series",
       f"{min(tip_ratio.values()):.3f} to {max(tip_ratio.values()):.3f}")
report("largest relative difference of the two patch integrals",
       f"{max(integral_gap.values()):.1e}")
reproduces(all(r < 0.0 for r in tip_ratio.values())
           and max(integral_gap.values()) < 5e-3,
           "the x4 law fails point by point, holds for the energy of the patch",
           KS_PY, ["emt_x4_component"])
```

Output: the tip ratios lie between $-0.327$ and $-0.106$ (negative in every series: the two sides have opposite signs), and the patch integrals agree to $1.3 \times 10^{-3}$. The check passes when every tip ratio is negative and the integrals agree to better than $5 \times 10^{-3}$ (the accuracy that a difference with the step $0.5$ allows), and the theory report's check `emt_x4_component`, which states the law for the energy of the 7-volume, is PASS. (COMPUTED; Section 17.16 explains the result.)

**In [21], the hidden-direction averages and the averaged C2.**

```python
MOMENTS = "Revision/field_equations_a4/ks_source/results/ks-source-moments.csv"
W = (1 - tip_weight) / (6 * H_value)  # the integral of e^(6Hy) over the patch


def mean(sid, column):
    """The weighted average of a column, from the record's integral."""
    return number(sid, f"int_{column}") / (2 * VOL7 * W)
```

`MOMENTS` names the record's table of hidden-direction averages (one row per state). `W` is $\int_{-L}^{0}e^{6Hy}dy = (1 - e^{-6HL})/(6H)$ of Section 17.17. `mean` turns a column `int_X` of the table of integrals into the weighted mean $\bar X = \int X/(2\,\mathrm{Vol}_7W)$ of Section 17.7.

```python
with repository_file(MOMENTS).open(encoding="utf-8", newline="") as handle:
    moments = {row["id"]: row for row in csv.DictReader(handle)}
agree = max(abs(mean(sid, "rho") / float(moments[sid]["rho_bar"]) - 1.0)
            for sid in nonzero)
```

The record's table is read into a dictionary by state name, as the table of integrals was in In [11]. `agree` is the largest relative difference between our $\bar\rho$ and the record's column `rho_bar` over the 70 nonzero states (the record computes its averages with Simpson's rule on the profiles, we from the solver's integrals, so they agree only to the accuracy of that rule).

```python
defect = {}
for sid in nonzero:
    p3b, ptb, p8b = (mean(sid, column) for column in ("p3", "p_t", "p8"))
    defect[sid] = abs(p3b + ptb - 2 * p8b) / (abs(p3b) + abs(ptb) + 2 * abs(p8b))
low, high = min(defect, key=defect.get), max(defect, key=defect.get)
```

For each state the three averaged pressures are computed (the parentheses make a **generator**, which produces the three values one after the other, and the three names receive them in order), and the relative defect of the averaged C2 of Section 17.17 is stored. `low` and `high` are the states with the smallest and the largest defect.

```python
report("largest relative difference of rho_bar from the record", f"{agree:.1e}")
report("defect of the averaged C2",
       f"{defect[low]:.6g} ({low}) to {defect[high]:.6g}")
detail = record_entry(KS_SOURCE, "C1_averaged_algebraic_condition_fails")["detail"]
reproduces(agree < 1e-6
           and f"[{defect[low]:.6g} ({low}), {defect[high]:.6g}]" in detail,
           "the averaged C2 fails by a defect of order 1 in all 70 states",
           KS_SOURCE, ["C1_averaged_algebraic_condition_fails"])
```

Output: $\bar\rho$ agrees with the record to $6.7 \times 10^{-8}$; the defect runs from $0.414086$ (`N688_lamm2_a00`) to $0.806379$. The check passes when the averages agree to $10^{-6}$ and the text of the record's check contains exactly this range, written as the record writes it, `[0.414086 (N688_lamm2_a00), 0.806379]`. (COMPUTED.)

**In [22], the first integral and the turning points.**

```python
CASES = "Revision/field_equations_a4/ks_source/results/ks-source-a4-cases.csv"
series = "N136_lam0"  # the canonical series
ids = [f"{series}_{s}" for s in SLICES]  # its five states
rho_bar = np.array([mean(sid, "rho") for sid in ids])
rho_slope = np.array([-3 * (mean(sid, "p3") - mean(sid, "p_t")) for sid in ids])
```

`CASES` names the record's table of integrated histories. For the series $N = 136$, $\lambda = 0$ the cell collects $\bar\rho$ at the five slices and its slope $d\bar\rho/da_4 = -3(\bar p_3 - \bar p_t)$ there (the averaged energy relation of Section 17.17).

```python
def rho_between(a):
    """rho_bar(a4) between the slices: cubic Hermite with the exact slopes."""
    k = min(int(a / 0.5), 3)  # the interval [0.5 k, 0.5 k + 0.5] that holds a
    t = (a - 0.5 * k) / 0.5  # the position inside it, from 0 to 1
    return ((2 * t**3 - 3 * t**2 + 1) * rho_bar[k]
            + (t**3 - 2 * t**2 + t) * 0.5 * rho_slope[k]
            + (-2 * t**3 + 3 * t**2) * rho_bar[k + 1]
            + (t**3 - t**2) * 0.5 * rho_slope[k + 1])
```

`rho_between` is the cubic Hermite interpolant. `int(a / 0.5)` is the number of the interval of length 0.5 that contains $a$ (`min(..., 3)` keeps $a = 2$ in the last interval), and `t` runs from 0 at its left end to 1 at its right end. The four cubic polynomials in `t` are the standard Hermite weights: at $t = 0$ they are $1, 0, 0, 0$ and at $t = 1$ they are $0, 0, 1, 0$, so the curve passes through both tabulated values; their derivatives are chosen so that the slope of the curve (with respect to $a$, hence the factor $0.5$, the interval length) equals the given slopes at both ends. `t**3` is $t^3$.

```python
def rate_squared(a, sigma0):
    """(a4'/H)^2 at a4 = a from the Einstein first integral, a4'(0) = H."""
    return 1.0 + sigma0 / 3.0 * (1.0 - rho_between(a) / rho_bar[0])
```

The first integral of Section 17.17, $(a_4'/H)^2 = 1 + (\sigma_0/3)(1 - \bar\rho(a_4)/\bar\rho(0))$.

```python
def turning_point(sigma0):
    """The a4 in [0, 0.5] where (a4'/H)^2 reaches 0, by bisection."""
    low_end, high_end = 0.0, 0.5
    for _ in range(60):  # each step halves the interval
        centre = (low_end + high_end) / 2
        if rate_squared(centre, sigma0) > 0.0:
            low_end = centre
        else:
            high_end = centre
    return low_end
```

**Bisection**: start with an interval whose left end has $(a_4'/H)^2 > 0$ and whose right end has $(a_4'/H)^2 < 0$; test the centre and keep the half in which the sign still changes. After 60 halvings the interval is $0.5/2^{60} \approx 4 \times 10^{-19}$ long, far below the precision of the numbers. (`_` is the name Python programmers give a loop variable that is not used.)

```python
with repository_file(CASES).open(encoding="utf-8", newline="") as handle:
    cases = {(row["gravity"], row["series"], row["case"]): row
             for row in csv.DictReader(handle)}
rate_gap, turn_gap, halts = 0.0, 0.0, {}
```

The record's table is read into a dictionary whose key is the triple (gravity, series, case), for example `("einstein", "N136_lam0", "sigma0 = 1")`. Two numbers will hold the largest relative differences from the record, and `halts` the turning points.

```python
for sigma0 in (10, 1, -1):
    ours = rate_squared(2.0, sigma0) ** 0.5  # a4'/H at a4 = 2
    theirs = float(cases[("einstein", series, f"sigma0 = {sigma0}")]["rate_a20"])
    rate_gap = max(rate_gap, abs(ours / theirs - 1.0))
    say(f"sigma0 = {sigma0:3d}: a4'/H at a4 = 2 is {ours:.6g} (record {theirs:.6g})")
```

For $\sigma_0 = 10, 1, -1$ the rate at $a_4 = 2$ (`** 0.5` is the square root) is compared with the record's column `rate_a20`, the rate $a_4'/H$ at the slice $a_4 = 2$ (`{sigma0:3d}` prints the integer in a field of three characters, so the lines line up). Output: $1.95362$, $1.1321$ and $0.847549$, each equal to the record's value.

```python
for sigma0, case in ((-10, "sigma0 = -10"), (-24, "Lambda = 0")):
    halts[sigma0] = turning_point(sigma0)
    theirs = float(cases[("einstein", series, case)]["a4_end"])
    turn_gap = max(turn_gap, abs(halts[sigma0] / theirs - 1.0))
    say(f"{case}: the deflation halts at a4 = {halts[sigma0]:.6g} "
        f"(record {theirs:.6g})")
```

For $\sigma_0 = -10$ and for $\Lambda = 0$ (which needs $\sigma_0 = -24$, Section 17.17) the turning point is found and compared with the record's column `a4_end`, where the record's integration stopped. Output: $0.397998$ and $0.149623$, equal to the record's values.

```python
reproduces(rate_gap < 1e-8, "Einstein first integral: a4'/H at a4 = 2 as recorded",
           KS_SOURCE, ["D2_einstein_first_integral"])
reproduces(turn_gap < 1e-6, "turning points for sigma0 = -10 and Lambda = 0",
           KS_SOURCE, ["D3_lambda_zero_cases_halt"])
```

Two checks: the rates agree with the record to $10^{-8}$ and the turning points to $10^{-6}$ (relative), and the record's checks `D2_einstein_first_integral` and `D3_lambda_zero_cases_halt` are PASS. Output: two PASS lines. (COMPUTED, within the ASSUMED approximation of Section 17.17. The agreement is not a test of the physics of the approximation, only of its arithmetic: the notebook and the record use the same first integral and the same interpolant.)

**In [23], the first integral drawn (figure 6).**

```python
grid = np.linspace(0.0, 2.0, 401)  # a4 from 0 to 2 in steps of 0.005
STRENGTHS = [(10, "#eb6834"), (1, "#f2a541"), (-1, "#5598e7"), (-10, "#1c5cab"),
             (-24, "#104281")]  # sigma0 and its colour
fig, ax = plt.subplots(figsize=(6.4, 4.4))
```

`np.linspace(0.0, 2.0, 401)` gives 401 equally spaced values of $a_4$ from 0 to 2; `STRENGTHS` pairs each source strength with a colour (warm for $\sigma_0 > 0$, blue for $\sigma_0 < 0$).

```python
for sigma0, colour in STRENGTHS:
    values = np.array([rate_squared(a, sigma0) for a in grid])
    keep = values >= 0.0  # a4'^2 cannot be negative: a4 turns back there
    label = ("$\\Lambda = 0$ ($\\sigma_0 = -24$)" if sigma0 == -24
             else f"$\\sigma_0 = {sigma0}$")
    x_values, rates = grid[keep], np.sqrt(values[keep])
    if sigma0 in halts:  # end the curve exactly at its turning point
        x_values, rates = np.append(x_values, halts[sigma0]), np.append(rates, 0.0)
    ax.plot(x_values, rates, color=colour, lw=1.8, label=label)
```

For each strength the cell computes $(a_4'/H)^2$ on the grid and keeps only the points where it is not negative (`keep` is an array of True and False; `grid[keep]` picks the values where it is True): beyond a turning point $a_4$ would decrease again, which this picture of $a_4'$ against an increasing $a_4$ does not show. The label is written in LaTeX. For the two strengths with a turning point the point $(a_4^*, 0)$ is appended (`np.append`), so that the curve ends exactly there; then the curve of $a_4'/H$ (the square root) is drawn.

```python
ax.plot(list(halts.values()), [0.0, 0.0], "kx", ms=8, mew=1.6,
        label="turning points ($a_4' = 0$)")
ax.axhline(1.0, color="#e34948", ls="--", lw=1.2,
           label="linear member $a_4 = Hx_4$")
ax.set_xlabel("$a_4$ (the extra times scale as $e^{-a_4}$)")
ax.set_ylabel("$a_4'/H$")
ax.legend(fontsize=7, loc="upper left")
end_rates = {s: rate_squared(2.0, s) ** 0.5 for s in (10, 1, -1)}
```

Black crosses mark the two turning points; the red dashed line is the constant rate of the history $a_4 = Hx_4$; then the axis labels and the legend. `end_rates` holds the rates at $a_4 = 2$ for the caption.

```python
save_figure(fig, "first_integral",
            "The rate $a_4'/H$ of the deflation of the extra times against $a_4$ "
            "(pure numbers), from the first integral of the averaged $a_4$ "
            ...)
```

The caption, quoted shortened (it is printed in full under the figure), inserts the rates $1.954$, $1.132$ and $0.848$ and the turning points $0.398$ and $0.150$ with three decimals. Output: figure 17b.6 and its saved line.

**What figure 17b.6 shows.** Horizontal axis: $a_4$ from 0 to 2 (pure number; the extra-time scale factor is proportional to $e^{-a_4}$); vertical axis: $a_4'/H$ (pure number). All five curves start at 1, the chosen initial rate. With $\sigma_0 = 10$ the rate grows to $1.954$ at $a_4 = 2$, with $\sigma_0 = 1$ to $1.132$, with $\sigma_0 = -1$ it falls to $0.848$; the curves flatten toward the right because the gas has already given up most of its averaged energy there (only the lost fraction enters the first integral). With $\sigma_0 = -10$ and with $\Lambda = 0$ the rate drops steeply to 0 at $a_4 = 0.398$ and $0.150$ (crosses): the deflation halts and the extra times would then re-inflate. None of the curves is selected by the equations: the starting value 1 is a choice, and the dashed line, the history on which the Kohn-Sham states were computed, is a solution of the approximate equations only for a source that does not change, like the $N = 8$ states. (COMPUTED within the ASSUMED approximation of Section 17.17.)

**In [24], the last check.**

```python
figure_names = ["eight_gammas", "slope_identity", "difference_order",
                "brane_and_mean", "energy_exchange", "first_integral"]
paths = [output_file(f"{FIGURE_FOLDER}/17b_{k}_{name}.png")
         for k, name in enumerate(figure_names, 1)]
check(all(path.is_file() for path in paths),
      "every figure file of this notebook exists")
all_checks_passed()
```

As In [20] of Notebook 17a, for the six figures. Output: PASS every figure file of this notebook exists and ALL 20 CHECKS PASSED (notebook 17b).

**The count.** The 20 PASS lines are: one each in In [2] and In [3], two in In [4], one each in In [6], In [8], In [9], In [10], In [11], In [13], In [14], In [15], In [16], In [17], In [18], In [20] and In [21], two in In [22], and one in In [24]. Fourteen of them reproduce a Revision record and name it.

### 17.22 What a prescribed background is, and what remains open

**What the record establishes.** In the words of the record `Revision/field_equations_a4/reports/ks-source-conditions.json`: no Kohn-Sham state recorded in `Revision/kohn_sham` is an admissible source of the author's metric; C1 and C2 fail for every nonzero state (C2 also after integration over $x_8$), and the Kohn-Sham history uses the linear member as a prescribed background, without back-reaction. The record of the $a_4$ equations says the same (`Revision/field_equations_a4/a4-equations.json`, key `fields.dirac16complex.kohnSham`), and so does the Kohn-Sham theory record (`Revision/kohn_sham/ks-theory.json`, key `adiabaticity.historyStatus`). Sections 17.12 to 17.16 add the reason: the Kohn-Sham source is conserved along the hidden direction at every point, and in the time direction for the total energy of the patch (not point by point); but its hidden pressure is far from flat and its 3-space pressure is not balanced by an equal extra-time pressure ($\int p_3 > \int p_t$ along the history), and for a conserved source these are exactly the failures of C2 and C3. Section 17.17 adds that averaging over the hidden direction does not rescue it: the averaged C2 still fails, and the averaged equations can be integrated only after two of them are dropped, an approximation whose error is of order 1.

**What "prescribed background" means.** A prescribed background is a metric chosen by hand, in which matter is placed and studied while its own gravity is ignored. The matter is then a **test field**, and the effect it would have on the metric, its **back-reaction**, is left out. This is a common and useful approximation in physics, much like computing the motion of a cork on a river whose flow is given: the cork follows the flow, and nobody asks how the cork changes the river. Quantum fields in a given expanding universe are usually studied this way. The approximation is good when the matter is too dilute to change the metric noticeably; whether that holds here cannot be decided without the back-reaction itself.

**What follows for the other chapters.** Every number computed along the history $a_4 = Hx_4$ in Chapters 14 to 16 (the Kohn-Sham levels, the energies and gaps, the temperatures, the energy densities, pressures and equations of state) is a property of a test gas in a chosen geometry. It is correctly computed (COMPUTED, with the accuracies stated there), but it is not a consequence of the coupled field equations of gravity and matter. Any equation of state derived from it, in particular for the dark-sector hypotheses discussed in Chapter 22, inherits this status: it describes the gas in the prescribed background, not a self-consistent universe.

**What this chapter does NOT say.**

- It does not say that the author's metric cannot be a solution of the field equations. Chapter 12 shows what source the linear member requires, and builds exact examples with a condensate of the commuting field dirac16complex00, whose pressures are equal and do not depend on $x_8$ (a computation of the book, Section 12.26).
- It does not say that no state of dirac16complex can be an admissible source. Only the 75 recorded Kohn-Sham states are tested. The record of the $a_4$ equations states what such a state would need: $p_3 + p_t = 2p_8$, every expectation value independent of $x_8$, and every off-diagonal expectation value zero (keys `fields.dirac16complex.kohnSham` and `fields.dirac16complex.offDiagonal`); for the linear member, in addition, equal expectation values of the 3-space and the extra-time kinetic terms (key `fields.dirac16complex.homogeneousSingleMode`). It also states that no state with unequal kinetic terms that meets the other conditions, and so would drive $a_4''$, is constructed in the Revision record (key `fields.dirac16complex.evolution`); and the many-quantum states of dirac16complex that the Revision record does construct, the Kohn-Sham states, fail the conditions (this chapter). Whether an admissible state exists is OPEN.
- It does not say what metric the Kohn-Sham gas would produce. That needs back-reaction, which nobody has computed. It is OPEN.
- It says nothing about the creation of universes, about pairs of universes of masses $+m$ and $-m$, or about matter and antimatter. Those questions are treated, with the precise statement of what is proved and what is not, in Chapters 18 to 21.

**What back-reaction would require.** By C1, a source that depends on $x_8$ cannot sit on the right-hand side of the field equations of a metric whose left-hand side does not depend on $x_8$. A self-consistent treatment therefore needs a metric with more freedom: functions of both the time $x_4$ and the hidden coordinate (for example separate warp factors for 3-space and for the extra times that depend on $y$), the Kohn-Sham equations in that metric, and the field equations, all solved together. Beyond that, the Kohn-Sham states themselves are instantaneous (adiabatic) states; the time-dependent problem along the history is also OPEN. Chapter 22 describes how a student could attack both.

### 17.23 What we proved, what we computed, what we assumed

**PROVED** (exact; each with the record file and check, and the notebook cell that reproduces it):

| statement | where verified | notebook |
| --- | --- | --- |
| C1: the left-hand sides are diagonal and free of $x_8$, so a source must be independent of $x_8$ with $q_{48} = q_{84} = 0$ | `wolfram-a4-report.json`: `P1_structure`, `P2_structure`, `P3_structure`, `independent_components` | 17a, In [4] |
| C2: $p_3 + p_t = 2p_8$ for every source | `wolfram-a4-report.json`: `algebraic_identity_x1_plus_x5_minus_2x8`; `python-a4-report.json`: `algebraic_identity` | 17a, In [4] |
| C3: the linear member needs $p_3 = p_t = p_8$ and constant $\rho$ | `python-a4-report.json` and `wolfram-a4-report.json`: `linear_member_equal_pressures` | 17a, In [4] |
| Einstein gravity: $T = 0$ has no solution for $H > 0$ | `wolfram-a4-report.json`: `einstein_no_vacuum_solution` | 17a, In [19] |
| the Bianchi identity: every source must be conserved | both reports: `E1_divergence_free`, `E2_divergence_free`, `E3_divergence_free` | (Section 17.12) |
| the conservation law in the coordinates $x_8$ and $y$ | `python-a4-report.json`: `conservation_components`, `json_conservation`; `ks-theory-python.json`: `emt_y_conservation_selfconsistent`, `emt_x4_component` | 17b, In [7] to In [9] |
| for a conserved source $p_3 + p_t - 2p_8 = p_8'(y)/(3H)$ | derived in Section 17.14 | 17b, In [10] |
| $d\mathcal C/dx_4 = 3a_4'\,\mathcal E$ for all couplings; along the linear member $-3AH\kappa(p_3 - p_t)$ | `wolfram-a4-report.json`: `constraint_propagation_bianchi`; `python-a4-report.json`: `bianchi_x4` | 17b, In [17] |
| the moment equations; $3F = 2\,dP/dX$; the constraint propagates with the averaged source; the Einstein first integral | `ks-source-a4.json`: `A1_lovelock_identity_x1_plus_x5_equals_2x8`, `A3_F_equals_two_thirds_dP_dX`, `A4_constraint_propagation_with_averaged_source`, `A6_x8_conservation_in_y`, `D2_einstein_first_integral` | (Section 17.17); 17b, In [22] |

(The report files lie in `Revision/field_equations_a4/reports/`, `Revision/field_equations_a4/ks_source/reports/` and `Revision/kohn_sham/reports/`.)

**COMPUTED** (numerical, on the 75 recorded Kohn-Sham states; each reproduces the record named):

| result | measured value | record and check | notebook |
| --- | --- | --- | --- |
| every nonzero state depends on $x_8$ | spread of $\rho$ at least 0.0497329 of $\max\lvert T\rvert$ | `ks-source-conditions.json`: `ks_profiles_depend_on_x8` | 17a, In [7] |
| C2 fails point by point | $\max\lvert V\rvert/\max\lvert T\rvert$ from 2.09192 to 3.99006 | `ks_profiles_violate_algebraic_condition` | 17a, In [9], In [12] |
| C2 fails after integration over $x_8$ | $R$ from 0.1072 to 0.4143 (closest to 1: 0.414328) | `ks_integrals_violate_algebraic_condition` | 17a, In [14] |
| C3 fails along the history | $\int\rho$ falls by factors 6.45 and 6.16; $\int p_3 > \int p_t = 0$ | `ks_history_is_a_prescribed_background` | 17a, In [16], In [17] |
| five states have no source at all | $N = 8$, $\lambda = 0$, all slices | `ks_zero_source_states_listed` | 17a, In [19] |
| the source rests on the author's real gammas | Clifford deviation exactly 0; sha256 prefix 95d8cbdd0682fd30 | `python-algebra.json`: `reality_signed_permutations`, `clifford_relation`; `ks-rust-solver.json`: `gamma_fixture_numeric` | 17b, In [3], In [4] |
| $V = p_8'/(3H)$ on the stored grid | at most $1.05 \times 10^{-4}$ of $\max\lvert T\rvert$; fitted order 4.02 to 4.08 | (the book's own test) | 17b, In [11], In [13] |
| the integrated conservation law | relative difference at most $1.421 \times 10^{-11}$ | `ks-rust-solver.json`: `emt_y_conservation_integrated` | 17b, In [14] |
| $R$ equals the boundary value $b_8$ of $p_8$ over its mean | agreement to $1.4 \times 10^{-11}$; tip share $0.31$ to $0.33$ for $N = 8$, at most $0.039$ otherwise | `ks_integrals_violate_algebraic_condition` | 17b, In [15] |
| the energy-change law of the patch along the history | Simpson's rule to at most $2.2 \times 10^{-4}$ | `ks-rust-solver.json`: `emt_energy_change_dE_da4` | 17b, In [18] |
| the time law fails point by point | tip ratio of the two sides $-0.327$ to $-0.106$; patch integrals agree to $1.3 \times 10^{-3}$ | `ks-theory-python.json`: `emt_x4_component` | 17b, In [20] |
| the averaged C2 fails | defect $0.414086$ to $0.806379$ | `ks-source-a4.json`: `C1_averaged_algebraic_condition_fails` | 17b, In [21] |
| first integral, Einstein, $N = 136$, $\lambda = 0$ (within the approximation) | $a_4'(2)/H = 1.95362$, $1.1321$, $0.847549$ for $\sigma_0 = 10, 1, -1$; halts at $a_4 = 0.397998$ ($\sigma_0 = -10$) and $0.149623$ ($\Lambda = 0$) | `ks-source-a4.json`: `D2_einstein_first_integral`, `D3_lambda_zero_cases_halt` | 17b, In [22] |

**ASSUMED.**

- The history $a_4 = Hx_4$ ($A = 1$) on which the Kohn-Sham states were computed: it is a PRESCRIBED BACKGROUND, chosen and not solved for (this chapter shows that it is not a solution with the Kohn-Sham source).
- The ingredients of the Kohn-Sham model (Chapter 14): the good sector without extra-time dependence, the Z2 mirror at the brane, the tip cutoff $y = -3$, the box of 3-space and the chosen particle numbers and couplings.
- In Section 17.17 only: the truncation of the averaged equations to the $x_4$ moment and the $x_1 - x_5$ moment (an approximation whose error, the dropped residuals, is of order 1), the initial rate $a_4'(0) = H$, and the interpolation of $\bar\rho$ between the slices.
- The overall sign convention $\sigma_T = +1$ of the source (record `a4-equations.json`, key `fields.emtConvention`). It does not affect C1, C2 or C3, which do not change when every component of $T$ changes sign.

**HYPOTHESIS.** None in this chapter.

**OPEN.** What metric the Kohn-Sham gas would produce with back-reaction; whether any state of dirac16complex is an admissible source of the author's metric; the time-dependent (non-adiabatic) evolution of the gas along the history; the source beyond $a_4 = 2$ and at nonzero temperature.

### 17.24 Exercises

**Exercise 1 (the pattern of the Lovelock components).** The record stores $E_{(2)}{}^{x_1}{}_{x_1} = 12a'^4 - 24a'^2a'' + 168a'^2H^2 - 40a''H^2 - 180H^4$, $E_{(2)}{}^{x_5}{}_{x_5} = 12a'^4 + 24a'^2a'' + 168a'^2H^2 + 40a''H^2 - 180H^4$ and $E_{(2)}{}^{x_8}{}_{x_8} = 12a'^4 + 168a'^2H^2 - 180H^4$. (a) Show that they have the form $P_2 + a''Q_2$, $P_2 - a''Q_2$, $P_2$, and find $P_2$ and $Q_2$. (b) Verify C2 for $k = 2$. (c) Find the Gauss-Bonnet part of $F$.

*Answer.* (a) In $E_{(2)}{}^{x_1}{}_{x_1}$ the terms without $a''$ are $12a'^4 + 168a'^2H^2 - 180H^4$, which is exactly $E_{(2)}{}^{x_8}{}_{x_8}$; call it $P_2$. The terms with $a''$ are $-24a'^2a'' - 40a''H^2 = a''(-24a'^2 - 40H^2)$ (rule: take out the common factor $a''$); call the bracket $Q_2 = -24a'^2 - 40H^2$. In $E_{(2)}{}^{x_5}{}_{x_5}$ the terms without $a''$ are again $P_2$, and the terms with $a''$ are $+24a'^2a'' + 40a''H^2 = -a''Q_2$. (b) $(P_2 + a''Q_2) + (P_2 - a''Q_2) - 2P_2 = 0$: the $a''$ terms cancel and $P_2 + P_2 - 2P_2 = 0$. (c) $E_{(2)}{}^{x_1}{}_{x_1} - E_{(2)}{}^{x_5}{}_{x_5} = 2a''Q_2 = a''(-48a'^2 - 80H^2)$, so the Gauss-Bonnet part of $F$ is $\alpha_2(-48a'^2 - 80H^2)$, as in the record's `evolution_F`.

**Exercise 2 (the two sides of C2 at three points).** Use the three lines printed by Notebook 17a, In [12], for the state $N = 136$, $\lambda = 0$, $a_{4,0} = 1$. (a) Compute $V$ in the middle and at the brane. (b) Compute $2p_8/(p_3 + p_t)$ at both points. (c) At the tip, compute $V/\max|T|$, given that the largest component of this state is $|p_8|$ at the tip (figure 2 of Notebook 17b shows $p_8/\max|T| = -1$ there).

*Answer.* (a) Middle: $V = 0.498835 + 0 - 2 \times 0.643324 = 0.498835 - 1.286648 = -0.787813$. Brane: $V = 0.000391237 + 0 - 2 \times 0.000942049 = 0.000391237 - 0.001884098 = -0.001492861$, printed as $-0.00149286$. (b) Middle: $1.286648/0.498835 = 2.579$, the 2.58 of figure 17a.5; brane: $0.001884098/0.000391237 = 4.816$, the 4.82. (c) $\max|T| = 431.733$, so $V/\max|T| = 1021.73/431.733 = 2.367$, inside the range 2.36 to 2.37 quoted in the caption of figure 17a.3.

**Exercise 3 (the two forms of the hidden conservation law).** Starting from the record's law in the coordinate $x_8$ for a diagonal source, $\partial_8 p_8 + 3H\cot z\,(2p_8 - p_3 - p_t) = 0$, derive the law in the coordinate $y$. Why may you divide by $\cot z$?

*Answer.* By the chain rule, $\partial_8 p_8 = (dy/dx_8)\,dp_8/dy = \cot z\,p_8'$, because $dy/dx_8 = \cot z$ (Section 17.4). The law becomes $\cot z\,p_8' + 3H\cot z\,(2p_8 - p_3 - p_t) = 0$, that is $\cot z\,[p_8' + 6Hp_8 - 3H(p_3 + p_t)] = 0$ (rule: take out the common factor; $3H\cdot 2p_8 = 6Hp_8$). On the patch $0 < z < \pi/2$ both $\cos z$ and $\sin z$ are positive, so $\cot z > 0$ and we may divide by it: $p_8' + 6Hp_8 = 3H(p_3 + p_t)$.

**Exercise 4 (C2 and C1 for a conserved source).** A conserved diagonal source in the author's metric has $p_8 = 5$ at every point (units of $m^8$, $H = 1$) and $p_t = 1$. (a) What is $p_3$? (b) Does it satisfy C2? (c) Can a conserved source with a flat $p_8$ still fail C1?

*Answer.* (a) The $y$ law with $p_8' = 0$: $0 + 6 \times 5 = 3(p_3 + 1)$, so $p_3 + 1 = 10$ and $p_3 = 9$. (b) $p_3 + p_t = 10 = 2p_8$: yes, as Section 17.14 predicts for a flat $p_8$. (c) Yes. C1 also asks that $\rho$, $p_3$ and $p_t$ do not depend on $x_8$. The hidden law fixes only the sum $p_3 + p_t$ and says nothing about $\rho$. For example $p_8 = 5$, $p_t = 1 + \sin y$ and $p_3 = 9 - \sin y$ satisfy the hidden law ($6 \times 5 = 3 \times 10$) and C2, but $p_3$ and $p_t$ depend on $y$, so C1 fails. C2 is only the $p_8$ part of C1.

**Exercise 5 (the averaged ratio by hand).** For the state $N = 136$, $\lambda = 0$, $a_{4,0} = 0$ the record's table `Revision/kohn_sham/results/ground/emt-integrals.csv` gives $\int p_3 = 23.8133$, $\int p_t = 0$, $\int p_8 = 35.0435$, $p_8(\text{brane}) = 0.00224994$ and $p_8(\text{tip}) = -6.59995$; and $\mathrm{Vol}_7 = 15875.2$, $H = 1$, $L = 3$. (a) Compute $R$ from the integrals. (b) Compute the weighted mean $\bar p_8$. (c) Compute $R$ from the brane and tip values and the mean, with the formula of Section 17.15. (d) Check the integrated conservation law.

*Answer.* (a) $R = (23.8133 + 0)/(2 \times 35.0435) = 23.8133/70.0870 = 0.33977$, the 0.339767 of the record. (b) The volume factor is $2\,\mathrm{Vol}_7(1 - e^{-18})/6 = 31750.4 \times (1 - 1.5 \times 10^{-8})/6 = 5291.73$ (the $e^{-18}$ changes nothing at this precision), so $\bar p_8 = 35.0435/5291.73 = 0.0066223$. (c) $e^{-18} \times (-6.59995) = -1.005 \times 10^{-7}$, so the numerator is $0.00224994 + 0.0000001005 = 0.00225004$, and $R = 0.00225004/0.0066223 = 0.33977$: the same number, as the conservation law demands. The brane value is about a third of the mean. (d) Left side: $2\,\mathrm{Vol}_7 \times 0.00225004 = 31750.4 \times 0.00225004 = 71.440$; right side: $3H \times 23.8133 = 71.440$. They agree to the digits given.

**Exercise 6 (every conserved profile with a constant sum).** Suppose $p_3 + p_t = P$ is a constant. (a) Find every $p_8(y)$ that satisfies the $y$ law. (b) Which of them satisfies C2? (c) Write the answer in the coordinate $z$.

*Answer.* (a) The law is $p_8' + 6Hp_8 = 3HP$. Multiply by $e^{6Hy}$: $(e^{6Hy}p_8)' = 3HPe^{6Hy}$ (rule: the product rule read backwards). Integrate: $e^{6Hy}p_8 = 3HP\,e^{6Hy}/(6H) + c = \tfrac{P}{2}e^{6Hy} + c$ with a constant $c$ (rule: an antiderivative of $e^{6Hy}$ is $e^{6Hy}/(6H)$; integration adds a constant). Divide by $e^{6Hy}$: $p_8 = \tfrac{P}{2} + c\,e^{-6Hy}$. Check: $p_8' = -6Hc\,e^{-6Hy}$, and $p_8' + 6Hp_8 = -6Hce^{-6Hy} + 3HP + 6Hce^{-6Hy} = 3HP$. (b) $V = p_8'/(3H) = -2c\,e^{-6Hy}$, which is zero everywhere only for $c = 0$: only the flat profile $p_8 = P/2$ satisfies C2. (c) Since $e^{6Hy} = \sin z$, $p_8 = P/2 + c/\sin z$: every non-flat conserved profile grows like $1/\sin z$ toward the tip.

**Exercise 7 (Simpson's rule along the history).** The record's table gives, for $N = 136$, $\lambda = 0$ at $a_{4,0} = 0, 0.5, 1, 1.5, 2$: $\int p_3 = 23.8133$, $15.4903$, $10.0397$, $6.44655$, $4.06205$ and $\int p_t = 0$; and $E(0) = 80.2822$, $E(2) = 12.4451$. (a) Compute the five rates $dE/da_{4,0}$. (b) Integrate them with Simpson's rule from 0 to 2 and compare with $E(2) - E(0)$. (c) Do the same with the trapezoidal rule, $h[\tfrac12f_0 + f_1 + f_2 + f_3 + \tfrac12f_4]$, and compare.

*Answer.* (a) $dE/da_{4,0} = -3\int p_3$: $-71.4399$, $-46.4709$, $-30.1191$, $-19.33965$, $-12.18615$. (b) $\tfrac{0.5}{3}[-71.4399 + 4(-46.4709) + 2(-30.1191) + 4(-19.33965) - 12.18615] = \tfrac16(-71.4399 - 185.8836 - 60.2382 - 77.3586 - 12.18615) = \tfrac16(-407.10645) = -67.8511$. The recorded change is $12.4451 - 80.2822 = -67.8371$ (Notebook 17b prints $-67.8372$, because it subtracts the unrounded numbers of the table). The difference is $0.0140$, a relative error of $0.0140/67.837 = 2.1 \times 10^{-4}$, the value of Notebook 17b, In [18]. (c) $0.5[-35.71995 - 46.4709 - 30.1191 - 19.33965 - 6.093075] = 0.5 \times (-137.7427) = -68.8713$, a relative error of $1.034/67.837 = 1.5 \times 10^{-2}$, about seventy times larger: Simpson's rule, of order 4, is far better than the trapezoidal rule, of order 2, with the same five values.

**Exercise 8 (the order of the finite differences).** For the state `N136_lam0_a10` Notebook 17b, In [13], found the difference $4.6 \times 10^{-7}$ of max|T| at the step $0.02$. Predict the differences at the steps $0.04$, $0.06$ and $0.10$ if the error is of order 4, and compare with the printed values $7.5 \times 10^{-6}$, $3.8 \times 10^{-5}$ and $3.0 \times 10^{-4}$.

*Answer.* An error of order 4 is $C\delta^4$, so doubling the step multiplies it by $2^4 = 16$: $16 \times 4.6 \times 10^{-7} = 7.4 \times 10^{-6}$. Tripling: $3^4 = 81$, $81 \times 4.6 \times 10^{-7} = 3.7 \times 10^{-5}$. Five times: $5^4 = 625$, $625 \times 4.6 \times 10^{-7} = 2.9 \times 10^{-4}$. The predictions agree with the printed values to within a few per cent, and the printed values are a little larger, more so for the larger steps (for the step $0.10$ the printed $3.0 \times 10^{-4}$ was at least $2.95 \times 10^{-4}$ before rounding, while every number that rounds to $4.6 \times 10^{-7}$, at most $4.65 \times 10^{-7}$, gives at most $625 \times 4.65 \times 10^{-7} = 2.91 \times 10^{-4}$: the rounding cannot explain the gap). The excess is the next term of the error: a fourth-order difference has the error $C\delta^4 + D\delta^6 + \dots$, and the term $D\delta^6$, small beside $C\delta^4$ for small $\delta$, grows faster with the step. That is why the fitted order is $4.04$ and not exactly $4.00$. A failure of the conservation law would show up as a floor below which the differences stop falling; there is none.

**Exercise 9 (the constraint in Einstein gravity).** In Einstein gravity $\mathcal C = 3a_4'^2 + 21H^2 + \Lambda + \kappa\rho$ and $\mathcal E = 2a_4'' - \kappa(p_3 - p_t)$. (a) Show by hand that $d\mathcal C/dx_4 = 3a_4'\,\mathcal E$ for a source that obeys $\rho' = -3a_4'(p_3 - p_t)$. (b) For the linear member with $A = 1$ and the Kohn-Sham gas at $\lambda = 0$, what is the sign of $d\mathcal C/dx_4$, and what does it mean?

*Answer.* (a) $d\mathcal C/dx_4 = 6a_4'a_4'' + \kappa\rho'$ (rule: the chain rule for $a_4'^2$; $H$ and $\Lambda$ are constants) $= 6a_4'a_4'' - 3\kappa a_4'(p_3 - p_t)$ (rule: insert the conservation law) $= 3a_4'[2a_4'' - \kappa(p_3 - p_t)] = 3a_4'\,\mathcal E$ (rule: take out $3a_4'$). (b) With $a_4'' = 0$ and $a_4' = H$: $d\mathcal C/dx_4 = -3H\kappa(p_3 - p_t)$. At $\lambda = 0$ the gas has $p_t = 0$ exactly, and its $p_3$ is not zero (at the three points of In [12] of Notebook 17a it is positive, and its integral $\int p_3$ is positive at every slice, In [16]). Wherever $p_3 \ne 0$, $d\mathcal C/dx_4 \ne 0$, and integrated over the patch it is negative: even if the constraint held at one slice, it would be violated at the next. The linear member cannot carry this gas as its source.

**Exercise 10 (the size of the patch).** (a) Compute $e^{-18}$ from $e^{-6} \approx 0.0024788$, and the angle $z$ of the tip cutoff. (b) What fraction of the proper volume of the patch lies in $-1 \le y \le 0$?

*Answer.* (a) $e^{-18} = (e^{-6})^3 \approx 0.0024788^3 = 1.523 \times 10^{-8}$ (rule: $e^{3u} = (e^u)^3$). The tip cutoff has $\sin z = e^{6Hy} = e^{-18}$; for so small a number $\arcsin u \approx u$, so $z \approx 1.5 \times 10^{-8}$, the value in the caption of figure 17a.1. (b) The proper volume between $y = a$ and $y = 0$ is proportional to $\int_a^0 e^{6y}dy = (1 - e^{6a})/6$. For $a = -1$: $(1 - e^{-6})/6$; for the whole patch, $a = -3$: $(1 - e^{-18})/6$. The fraction is $(1 - 0.0024788)/(1 - 1.5 \times 10^{-8}) = 0.9975$: more than 99.7 per cent of the volume lies within one unit of the brane. That is why the weighted mean $\bar p_8$ is decided near the brane, and why the tip, where the profiles are largest, matters so little in the integrals.
