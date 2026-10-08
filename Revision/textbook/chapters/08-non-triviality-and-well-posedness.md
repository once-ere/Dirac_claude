## 8. Non-triviality, its exact scope, and well-posedness

When the author coupled the fields dirac16complex and dirac16complex00 to his primordial gravitational field, he asked for a test: the field equations must contain gravity through the canonical spin connection, unless spacetime is flat. This chapter answers that request exactly, and it answers a second question that every field equation must face before anyone can trust its solutions: does the equation decide the future from the present in a stable way? Both answers are more interesting than a plain yes. The gravitational term of the field equation is $3H\gamma^{(8)}\Psi$ in the natural frame, but a different, equally valid frame makes it vanish, and a change of the field variables removes it too; what no choice removes is the spin connection itself, because its curvature is the curvature of spacetime. And the field equation, with its four time-like directions, is not a well-posed evolution equation: waves along the three extra times grow, with growth rates that have no upper bound, and the deflation of the extra times pushes every such wave into growth. (This is proved exactly in flat 4+4 space and, for the author's metric, with coefficients frozen at one point; carrying it over to the author's varying coefficients needs a standard theorem that this chapter quotes without proof. Section 8.18 gives each status.) Four notebooks compute every statement anew from the definitions and reproduce the Revision record: Notebook 08c (the term in two frames), Notebook 08a (the growth rates), Notebook 08b (the onset of growth along the deflating history) and Notebook 08d (the rescaling and the two ends of the hidden direction).

### 8.1 What this chapter does

**Why we need this chapter.** The author's task, quoted in the file `Revision/README.md` of the repository, says of the two Lagrangians: "[1]- the Lagrangian for dirac16complex must be non-trivial (i.e., the Euler-Lagrange equations for dirac16complex always possess non-zero contributions from gravity (through the canonical spin-connection, unless we are in flat 4+4 spacetime), must be self consistent, must be checked and verified)", and "[2]" asks the same of dirac16complex00. Two questions hide in this request. First: what exactly is "the contribution from gravity through the canonical spin connection", and which part of it is a property of the field equation itself rather than of the way we chose to write the equation down? Second: a field equation is useful only if, given the field now, it determines the field later, and determines it stably, so that a tiny change now makes only a tiny change later. Is that true here? This chapter answers both questions exactly, and says precisely where each answer stops.

**The answers in brief.** Each item carries its label (the labels are explained at the end of this section).

- In the diagonal frame of the author's metric the gravitational term of the field equation is $\gamma^\mu\Omega_\mu\Psi = 3H\gamma^{(8)}\Psi$, for every history $a_4(x_4)$. The time-direction pieces of the three inflating and the three deflating directions cancel; the six hidden-direction pieces add up to $3H$. The term is not zero for any field $\Psi \neq 0$ (PROVED; Sections 8.4 to 8.6).
- The spin connection vanishes only in the formal flat limit $a_4' = 0$ and $H = 0$, which is not a member of the author's family of metrics (PROVED; Section 8.6).
- The value $3H\gamma^{(8)}$ belongs to one frame and to one choice of field variables. In a frame boosted in the $(x_4, x_8)$ plane with the rapidity $6Hx_4$ the term is identically zero, and the rescaling $\Psi = \sin^{-1/2}z\,\chi$ removes it in the diagonal frame (PROVED; Sections 8.9 and 8.30).
- What no choice removes: the spin connection itself vanishes in no frame, because its curvature is the curvature of spacetime, which is not zero for $H > 0$; and the frame factors $e^{\mp a_4}\sin^{-1/6}z$ and $\tan z$ multiply every derivative in the field equation except the one along the time $x_4$ (whose factor is $1/f_4 = 1$). This is the exact, frame-independent content of the tests [1] and [2] (PROVED; Sections 8.7 and 8.10). The Revision record states this as a correction for the author: the tests hold in this qualified sense.
- The field equation can be solved for the time derivative $\partial_4\Psi$, but its initial-value problem is NOT well posed for data that depend on the extra times $x_5, x_6, x_7$: such waves grow, and their growth rates have no upper bound (PROVED in flat 4+4 space and, for the author's metric, with frozen coefficients, a MODEL; for the author's varying coefficients it follows from the Lax-Mizohata theorem, a standard theorem quoted without proof, so that step is ASSUMED; Sections 8.16 to 8.19).
- Along the deflating history every wave along an extra time eventually starts to grow (PROVED with frozen coefficients; followed numerically through the onset in a labelled model, COMPUTED; Sections 8.24 and 8.25).
- Even without extra-time dependence, the hidden direction has an open end at $z = \pi/2$; there the Revision record imposes no boundary condition, and fields that do not depend on $x_8$ grow when $m < 3H$, fed through that end. Which boundary condition is physical is OPEN (Sections 8.31 and 8.32).

**What the chapter does, section by section.** Section 8.2 sets the stage. Sections 8.3 to 8.11 compute the spin connection, the gravitational term, its frame dependence and the curvature, with Notebook 08c as the worked example (Sections 8.12 to 8.15). Sections 8.16 to 8.19 define well-posedness and show, with plane waves, that it fails; Notebook 08a is the example (Sections 8.20 to 8.23). Sections 8.24 and 8.25 follow waves along the deflating history; Notebook 08b is the example (Sections 8.26 to 8.29). Sections 8.30 to 8.32 change the field variables and study the two ends of the hidden direction; Notebook 08d is the example (Sections 8.33 to 8.36). Section 8.37 collects the exact scope in one table, Section 8.38 lists what we proved, computed and assumed, and Section 8.39 has the exercises.

**The four notebooks.**

| notebook | what it computes | checks and figures | Revision records it reproduces |
| --- | --- | --- | --- |
| 08c | the Christoffel symbols and the canonical spin connection of the diagonal frame and of a boosted frame, from the definitions; what cancels and what survives in $\gamma^\mu\Omega_\mu$; the connection vanishes only in flat space; the term in two frames; the curvature in both frames; the connection in the energy-momentum tensor | 32 checks, 5 figures | `python-field-theory.json`, `wolfram-field-theory.json`, `python-scope.json` (all in `Revision/theory/reports/`), `Revision/kohn_sham/results/parameters.json` |
| 08a | the mode matrix of a plane wave and its square; the growth rates of the extra-time waves; the Hadamard amplification; the Krein form | 30 checks, 6 figures | `python-scope.json`, `wolfram-scope.json`, `python-field-theory.json`, `wolfram-field-theory.json`, `Revision/algebra/reports/python-algebra.json`, `Revision/pairing/reports/python-pairing.json` |
| 08b | the scale factors along the deflating history; the frame momenta of a wave and its onset time; one wave followed through the onset with RK4 and compared with WKB formulas | 25 checks, 5 figures | `parameters.json`, `python-field-theory.json`, `python-scope.json` |
| 08d | the rescaling that removes the term; an exact family of solutions; the growing modes that do not depend on $x_8$; the boundary term at the patch end | 23 checks, 5 figures | `python-field-theory.json`, `Revision/theory/field-theory.json`, `python-scope.json`, `parameters.json` |

The chapter places the notebooks in the order in which it uses them: 08c, 08a, 08b, 08d.

**How this chapter relates to Chapter 6.** Chapter 6 introduces the vielbein, the canonical spin connection, the contraction $\gamma^\mu\Omega_\mu = 3H\gamma^{(8)}$, and, with its Notebook 06b, a first look at the boosted frame, the curvature and the rescaling; it also proves local spin covariance in general. This chapter recomputes everything it needs, so that it can be read on its own, and goes further: what cancels and what survives direction by direction, the proof that the connection vanishes only in the flat limit, the boosted term derived from the uniqueness of the connection, the curvature compared in two frames, the exact family with its growing finite-norm members, the flux through the patch end, and, above all, the question of well-posedness, which Chapter 6 does not treat.

**Labels.** As everywhere in the book, every statement carries one of five labels. **PROVED** means exact: derived here line by line and confirmed by an exact check of a notebook, and, where the Revision record proves the same, the record file and its check are named. **COMPUTED** means a number obtained numerically by a notebook, with its measured accuracy. **ASSUMED** marks the inputs we choose or quote: standard theorems quoted without proof (each is named where it is used), the deflating history $a_4 = AHx_4$, which the Revision record calls a PRESCRIBED BACKGROUND, and two approximations that the notebooks label MODEL (frozen coefficients, and the local-frame model of Section 8.25). **OPEN** marks questions this record does not answer. No HYPOTHESIS enters this chapter. Nothing in this chapter concerns pairs of universes, their creation, or matter and antimatter; those questions belong to Chapters 18 to 21, which state precisely what is and what is not proved about them.

### 8.2 The stage: coordinates, metric, frame and the field equation

**Coordinates.** A point of the author's spacetime has eight coordinates, named as the author names them: $x_1, x_2, x_3$ are ordinary 3-space; $x_4$ is the time in which everything evolves; $x_5, x_6, x_7$ are the three **extra times**, directions that behave like time (they are time-like) and that deflate exponentially; $x_8$ is the **hidden** space direction. We write $z = 6Hx_8$, where $H > 0$ is a constant of the author; $z$ runs from $0$ (the **tip**) to $\pi/2$ (the **patch end**). In formulas the letter $i$ always stands for one of the 3-space directions $x_1, x_2, x_3$ and the letter $t$ for one of the extra times $x_5, x_6, x_7$. In Python, lists are counted from 0, so position 0 holds $x_1$, position 3 the time $x_4$ and position 7 the hidden coordinate $x_8$.

**The metric.** The author's metric is diagonal (Chapter 3). We write it with eight positive **scale factors** $f_1, \dots, f_8$:

$$
g = \mathrm{diag}\big(f_1^2,\ f_2^2,\ f_3^2,\ -f_4^2,\ -f_5^2,\ -f_6^2,\ -f_7^2,\ f_8^2\big),
$$

$$
f_1 = f_2 = f_3 = e^{a_4}\sin^{1/6}z, \quad f_4 = 1, \quad f_5 = f_6 = f_7 = e^{-a_4}\sin^{1/6}z, \quad f_8 = \cot z .
$$

A small step $dx_\mu$ along the direction $x_\mu$ has the proper length (the length measured with the metric) $f_\mu|dx_\mu|$. The function $a_4(x_4)$, the **metric function**, increases with the time: then the 3-space factor $e^{a_4}$ grows (3-space **inflates**) and the extra-time factor $e^{-a_4}$ shrinks (the extra times **deflate**). We write $a_4' = da_4/dx_4$ and $a_4'' = d^2a_4/dx_4^2$. With the **frame metric** $\eta = \mathrm{diag}(+1, +1, +1, -1, -1, -1, -1, +1)$ (in the order $x_1, \dots, x_8$) every diagonal entry is $g_{\mu\mu} = \eta_{\mu\mu}f_\mu^2$. The signs say which directions are space-like ($+$: $x_1, x_2, x_3, x_8$) and which are time-like ($-$: $x_4, x_5, x_6, x_7$); there are four of each, the signature (4,4). The product of the eight factors is the volume factor, $\sqrt{|g|} = f_1f_2\cdots f_8 = \cos z$; it does not depend on the time, because the inflation $e^{3a_4}$ of 3-space and the deflation $e^{-3a_4}$ of the extra times cancel (PROVED; `Revision/theory/reports/python-field-theory.json`, check `sqrt_det_g_equals_cos_z`). The value $H = 0$ is not a member of the author's family: at fixed $x_8$ the factor $\sin^{1/3}z$ goes to $0$ and $\cot^2 z$ to infinity, so the metric degenerates (`Revision/theory/reports/wolfram-field-theory.json`, check `degenerate_at_H_0`). Every statement of this chapter assumes $H > 0$ and $0 < z < \pi/2$.

**The diagonal frame.** A **frame** (also called a **vielbein**) is a set of eight vectors, one for each direction $a = 1, \dots, 8$, that have length 1 and are perpendicular to each other when measured with the metric. Its components $e^a{}_\mu$ (frame direction $a$, coordinate direction $\mu$) obey $\sum_a \eta_{aa}e^a{}_\mu e^a{}_\nu = g_{\mu\nu}$. The **diagonal frame** is $e^a{}_\mu = f_a\delta^a_\mu$, where $\delta^a_\mu$ is 1 for $a = \mu$ and 0 otherwise; its inverse is $E_a{}^\mu = \delta^\mu_a/f_a$. Indeed $\sum_a\eta_{aa}f_a\delta^a_\mu f_a\delta^a_\nu$ is zero for $\mu \neq \nu$ and $\eta_{\mu\mu}f_\mu^2 = g_{\mu\mu}$ for $\mu = \nu$.

**The gamma matrices.** The book uses the author's eight **real** $16 \times 16$ gamma matrices (Chapter 4), stored in the Revision file `Revision/algebra/gammas.json` in the order $x_1, \dots, x_8$; we write them $\gamma^{(1)}, \dots, \gamma^{(8)}$ ($\gamma^{(4)}$ means the gamma of the direction $x_4$, and so on). Their entries are $0$, $1$ and $-1$. They obey the **Clifford relations**

$$
\gamma^{(a)}\gamma^{(b)} + \gamma^{(b)}\gamma^{(a)} = 2\eta^{ab}\,I_{16},
$$

where $I_{16}$ is the $16 \times 16$ unit matrix and $\eta^{ab} = \eta_{ab}$ (PROVED; `Revision/algebra/reports/python-algebra.json`, check `clifford_relation`). Two consequences are used in almost every line of this chapter: the square of each gamma is $\eta_{aa}I_{16}$, that is $+I_{16}$ for $x_1, x_2, x_3, x_8$ and $-I_{16}$ for $x_4, x_5, x_6, x_7$; and two different gammas **anticommute**, $\gamma^{(a)}\gamma^{(b)} = -\gamma^{(b)}\gamma^{(a)}$ for $a \neq b$. A third fact: the gammas of the space-like directions are symmetric matrices and those of the time-like directions antisymmetric, $(\gamma^{(a)})^T = \eta_{aa}\gamma^{(a)}$ (the $T$ means the transpose: rows become columns). The **coordinate gammas** are $\gamma^\mu = \sum_a E_a{}^\mu\gamma^{(a)}$; in the diagonal frame $\gamma^\mu = \gamma^{(\mu)}/f_\mu$. The matrix $C = \gamma^{(8)}\gamma^{(1)}\gamma^{(2)}\gamma^{(3)}$ (Chapter 5) and the matrix $B = -iC\gamma^{(4)}$ (Chapters 5 and 10) appear in the notebooks; $B$ is Hermitian, $B^2 = I_{16}$, with eight eigenvalues $+1$ and eight $-1$.

**The two fields and their field equation.** dirac16complex is a column $\Psi$ of 16 complex **anticommuting** (Grassmann) components; dirac16complex00 is a column of 16 ordinary complex numbers (Chapter 7). Their Lagrangians have the same form, and so do their field equations (Chapter 7 derives them):

$$
\gamma^\mu D_\mu\Psi = \big(m + U'(S)\big)\Psi, \qquad D_\mu\Psi = \partial_\mu\Psi + \Omega_\mu\Psi .
$$

Here $\partial_\mu$ is the partial derivative with respect to $x_\mu$, the sum over $\mu = 1, \dots, 8$ is understood (a repeated upper and lower index is summed), $m$ is the mass, $S = \bar\Psi\Psi = \Psi^\dagger C\Psi$ is the scalar built from the field and its **Dirac adjoint** $\bar\Psi = \Psi^\dagger C$ (the dagger means: transpose and take the complex conjugate of every entry), $U(S) = \frac{\lambda}{2}S^2$ is the potential, and $U'(S) = \lambda S$. The matrices $\Omega_\mu$ are the **spinor connection**, built from the canonical spin connection in Section 8.4. Everything in this chapter is a statement about this matrix equation; it holds for both fields (for the Grassmann field, "$\Psi \neq 0$" means a configuration that is not identically zero). Written out in the diagonal frame the equation reads (`Revision/theory/field-theory.json`, formula key `field_equation`; Section 8.5 derives the last term on the left):

$$
\begin{aligned}
&e^{-a_4}\sin^{-1/6}z\,\big(\gamma^{(1)}\partial_1 + \gamma^{(2)}\partial_2 + \gamma^{(3)}\partial_3\big)\Psi + \gamma^{(4)}\partial_4\Psi \\
&\quad + e^{a_4}\sin^{-1/6}z\,\big(\gamma^{(5)}\partial_5 + \gamma^{(6)}\partial_6 + \gamma^{(7)}\partial_7\big)\Psi + \tan z\,\gamma^{(8)}\partial_8\Psi + 3H\gamma^{(8)}\Psi = \big(m + U'(S)\big)\Psi .
\end{aligned}
$$

The derivative terms are $\sum_\mu\gamma^\mu\partial_\mu\Psi = \sum_\mu(\gamma^{(\mu)}/f_\mu)\partial_\mu\Psi$, with $1/f_i = e^{-a_4}\sin^{-1/6}z$, $1/f_4 = 1$, $1/f_t = e^{a_4}\sin^{-1/6}z$ and $1/f_8 = \tan z$. These factors are the **frame factors**: they carry the metric into every derivative term.

**Units.** $H$, $m$ and every momentum are measured in one unit, an inverse length, and the coordinates in its inverse; every printed number is a pure number in this unit. The examples use $H = m = 1$, the values of the Kohn-Sham record.

### 8.3 Frames, and why a frame is not unique

**Why spinors need a frame.** The gamma matrices are attached to the eight orthonormal frame directions, not to the coordinates: the Clifford relations $\{\gamma^{(a)}, \gamma^{(b)}\} = 2\eta^{ab}$ involve the fixed numbers $\eta^{ab}$, while the metric $g_{\mu\nu}$ changes from point to point. (The curly bracket $\{A, B\} = AB + BA$ is the **anticommutator**.) To write a spinor field equation in curved space one therefore needs a frame at every point, and the frame vectors turn from point to point; the canonical spin connection measures how they turn (Section 8.4).

**A frame is not unique.** At every point one may replace the eight frame vectors by combinations of them, $e'^a{}_\mu = \sum_b\Lambda^a{}_b e^b{}_\mu$, with a matrix $\Lambda$ that keeps the frame metric: $\sum_a\eta_{aa}\Lambda^a{}_b\Lambda^a{}_c = \eta_{bc}$. The new frame describes the same metric. Line by line:

$$
\begin{aligned}
\sum_a\eta_{aa}e'^a{}_\mu e'^a{}_\nu &= \sum_a\eta_{aa}\Big(\sum_b\Lambda^a{}_b e^b{}_\mu\Big)\Big(\sum_c\Lambda^a{}_c e^c{}_\nu\Big) \\
&= \sum_{b,c}\Big(\sum_a\eta_{aa}\Lambda^a{}_b\Lambda^a{}_c\Big)e^b{}_\mu e^c{}_\nu \\
&= \sum_{b,c}\eta_{bc}\,e^b{}_\mu e^c{}_\nu = g_{\mu\nu} .
\end{aligned}
$$

The first line inserts the new frame; the second reorders the finite sums; the third uses the condition on $\Lambda$ and then the frame condition of the old frame.

**The boost in the $(x_4, x_8)$ plane.** The **hyperbolic functions** are $\cosh b = (e^b + e^{-b})/2$ and $\sinh b = (e^b - e^{-b})/2$. They obey

$$
\cosh^2 b - \sinh^2 b = \frac{(e^b + e^{-b})^2 - (e^b - e^{-b})^2}{4} = \frac{4e^be^{-b}}{4} = 1 ,
$$

where the middle step expands both squares ($e^{2b} + 2 + e^{-2b}$ minus $e^{2b} - 2 + e^{-2b}$ leaves $4$). The **boost** with **rapidity** $b$ mixes the time-like frame vector of $x_4$ and the space-like frame vector of $x_8$:

$$
e'^{(4)} = \cosh b\;e^{(4)} + \sinh b\;e^{(8)}, \qquad e'^{(8)} = \sinh b\;e^{(4)} + \cosh b\;e^{(8)},
$$

and keeps the other six. It keeps the frame metric: the two mixed vectors enter the metric as $-e'^{(4)}e'^{(4)} + e'^{(8)}e'^{(8)}$ (products of components at the same $\mu$ and $\nu$), and

$$
\begin{aligned}
-e'^{(4)}e'^{(4)} + e'^{(8)}e'^{(8)} &= -\big(\cosh^2 b\,e^{(4)}e^{(4)} + 2\cosh b\sinh b\,e^{(4)}e^{(8)} + \sinh^2 b\,e^{(8)}e^{(8)}\big) \\
&\quad + \big(\sinh^2 b\,e^{(4)}e^{(4)} + 2\sinh b\cosh b\,e^{(4)}e^{(8)} + \cosh^2 b\,e^{(8)}e^{(8)}\big) \\
&= -(\cosh^2 b - \sinh^2 b)\,e^{(4)}e^{(4)} + (\cosh^2 b - \sinh^2 b)\,e^{(8)}e^{(8)} \\
&= -e^{(4)}e^{(4)} + e^{(8)}e^{(8)} .
\end{aligned}
$$

The first two lines multiply out the two squares (here $e^{(4)}e^{(8)}$ stands for the symmetric combination of the two orders), the third collects the terms (the mixed terms cancel), and the fourth uses $\cosh^2 b - \sinh^2 b = 1$. The rapidity may change from point to point; we take $b = \beta x_4 + b_0$ with two constants $\beta$ (the **rapidity rate**) and $b_0$, a different boost at every time. Every such frame describes the author's metric exactly (PROVED; `Revision/theory/reports/python-scope.json`, check `boosted_frame_reproduces_metric`, and the same check of `wolfram-scope.json`).

**The principle.** A change of frame changes the spin connection and the coordinate gammas, and the field changes with it, $\Psi' = S\Psi$ with an invertible $16 \times 16$ matrix $S(x)$ (Section 8.9 finds $S$ for the boost). A statement about the field equation is a property of the equation itself only if it holds in every frame. A statement that holds in one frame only describes how we chose to write the equation.

### 8.4 The Christoffel symbols and the canonical spin connection of the diagonal frame

**Christoffel symbols.** The **Christoffel symbols** $\Gamma^\lambda{}_{\mu\nu}$ say how the coordinate directions turn from point to point (Chapter 3). For a diagonal metric they are

$$
\Gamma^\lambda{}_{\mu\nu} = \frac{1}{2g_{\lambda\lambda}}\big(\partial_\mu g_{\lambda\nu} + \partial_\nu g_{\lambda\mu} - \partial_\lambda g_{\mu\nu}\big),
$$

and they are symmetric in the two lower indices. The author's metric depends only on $x_4$ (through $a_4$) and on $x_8$ (through $z$), and $dz/dx_8 = 6H$. It has 25 independent nonzero symbols (PROVED; `Revision/theory/reports/python-field-theory.json`, check `christoffel_symmetric_metric_compatible`):

| symbol | value | symbol | value |
| --- | --- | --- | --- |
| $\Gamma^{x_i}{}_{x_ix_4}$ | $a_4'$ | $\Gamma^{x_i}{}_{x_ix_8}$ | $H\cot z$ |
| $\Gamma^{x_t}{}_{x_tx_4}$ | $-a_4'$ | $\Gamma^{x_t}{}_{x_tx_8}$ | $H\cot z$ |
| $\Gamma^{x_4}{}_{x_ix_i}$ | $e^{2a_4}\sin^{1/3}z\,a_4'$ | $\Gamma^{x_4}{}_{x_tx_t}$ | $e^{-2a_4}\sin^{1/3}z\,a_4'$ |
| $\Gamma^{x_8}{}_{x_ix_i}$ | $-e^{2a_4}H\sin^{4/3}z/\cos z$ | $\Gamma^{x_8}{}_{x_tx_t}$ | $e^{-2a_4}H\sin^{4/3}z/\cos z$ |
| $\Gamma^{x_8}{}_{x_8x_8}$ | $-6H/(\sin z\cos z)$ | | |

(each of the eight entries of the first four rows stands for three symbols, one for each value of $i$ or of $t$: 24 symbols, plus the last one: 25). Chapter 3 derives all of them from the metric, and Notebook 08c computes all of them again; here we repeat the three that this chapter needs most. First, $\Gamma^{x_1}{}_{x_1x_4}$: only the term $\partial_4 g_{11}$ survives, and $g_{11} = e^{2a_4}\sin^{1/3}z$ has $\partial_4 g_{11} = 2a_4'g_{11}$ (chain rule), so $\Gamma^{x_1}{}_{x_1x_4} = 2a_4'g_{11}/(2g_{11}) = a_4'$. Second, $\Gamma^{x_1}{}_{x_1x_8} = \partial_8 g_{11}/(2g_{11})$, and $\partial_8\sin^{1/3}z = \frac13\sin^{-2/3}z\cos z\cdot 6H$, so $\Gamma^{x_1}{}_{x_1x_8} = \frac12\cdot\frac13\cdot\frac{\cos z}{\sin z}\cdot 6H = H\cot z$. Third, $\Gamma^{x_5}{}_{x_5x_4} = \partial_4 g_{55}/(2g_{55})$ with $g_{55} = -e^{-2a_4}\sin^{1/3}z$, $\partial_4 g_{55} = -2a_4'g_{55}$, so $\Gamma^{x_5}{}_{x_5x_4} = -a_4'$: the sign is opposite to that of 3-space because the extra times deflate. A useful rule follows the same way: for a diagonal metric, $\Gamma^\mu{}_{\mu\nu} = \partial_\nu g_{\mu\mu}/(2g_{\mu\mu}) = \partial_\nu\ln f_\mu$ (no sum over $\mu$), because $g_{\mu\mu} = \eta_{\mu\mu}f_\mu^2$ gives $\partial_\nu g_{\mu\mu}/(2g_{\mu\mu}) = 2\eta_{\mu\mu}f_\mu\partial_\nu f_\mu/(2\eta_{\mu\mu}f_\mu^2) = \partial_\nu f_\mu/f_\mu$.

**The canonical spin connection.** The **canonical spin connection** of a frame is (Chapter 6)

$$
\omega_\mu{}^a{}_b = \sum_\nu e^a{}_\nu\Big(\partial_\mu E_b{}^\nu + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}E_b{}^\lambda\Big), \qquad \omega_{\mu ab} = \eta_{aa}\,\omega_\mu{}^a{}_b .
$$

It obeys the **vielbein postulate** $\partial_\mu e^a{}_\nu - \sum_\lambda\Gamma^\lambda{}_{\mu\nu}e^a{}_\lambda + \sum_b\omega_\mu{}^a{}_b e^b{}_\nu = 0$, and $\omega_{\mu ab}$ is antisymmetric in $a, b$ (PROVED for the diagonal frame; `python-field-theory.json`, checks `vielbein_postulate` and `spin_connection_antisymmetric`). For the diagonal frame we compute it line by line:

$$
\begin{aligned}
\omega_\mu{}^a{}_b &= \sum_\nu f_a\delta^a_\nu\Big(\partial_\mu\frac{\delta^\nu_b}{f_b} + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}\frac{\delta^\lambda_b}{f_b}\Big) \\
&= f_a\Big(\partial_\mu\frac{\delta^a_b}{f_b} + \frac{\Gamma^a{}_{\mu b}}{f_b}\Big) .
\end{aligned}
$$

The first line inserts $e^a{}_\nu = f_a\delta^a_\nu$ and $E_b{}^\nu = \delta^\nu_b/f_b$; the second carries out the sums (the delta keeps only $\nu = a$ and $\lambda = b$). Two cases:

- $a = b$: $\omega_\mu{}^a{}_a = f_a\partial_\mu(1/f_a) + \Gamma^a{}_{\mu a} = -\partial_\mu\ln f_a + \partial_\mu\ln f_a = 0$, by the derivative of $1/f$ ($f\,\partial(1/f) = -\partial f/f$) and the rule $\Gamma^a{}_{\mu a} = \partial_\mu\ln f_a$ above.
- $a \neq b$: $\delta^a_b = 0$, so $\omega_\mu{}^a{}_b = (f_a/f_b)\,\Gamma^a{}_{\mu b}$.

So a component with $a \neq b$ is nonzero exactly when the Christoffel symbol $\Gamma^a{}_{\mu b}$ is. The table shows that for $\mu = x_4$ and $\mu = x_8$ every symbol $\Gamma^a{}_{\mu b}$ with $a \neq b$ vanishes (the nonzero symbols with a lower index $x_4$ or $x_8$ all have $a = b$, like $\Gamma^{x_i}{}_{x_ix_4}$), so $\omega_{x_4} = \omega_{x_8} = 0$. For $\mu = x_i$ the symbols with $a \neq b$ are $\Gamma^{x_i}{}_{x_ix_4}$, $\Gamma^{x_i}{}_{x_ix_8}$, $\Gamma^{x_4}{}_{x_ix_i}$ and $\Gamma^{x_8}{}_{x_ix_i}$; for $\mu = x_t$ the same with $t$. We compute one member of each antisymmetric pair, with $a < b$, line by line:

- $\omega_{x_i}{}^{(i)}{}_{(4)} = (f_i/f_4)\,\Gamma^{x_i}{}_{x_ix_4} = e^{a_4}\sin^{1/6}z\cdot a_4'$, and lowering with $\eta_{ii} = +1$: $\omega_{x_i\,(i)(4)} = a_4'e^{a_4}\sin^{1/6}z$.
- $\omega_{x_i}{}^{(i)}{}_{(8)} = (f_i/f_8)\,\Gamma^{x_i}{}_{x_ix_8} = e^{a_4}\sin^{1/6}z\,\tan z\cdot H\cot z = He^{a_4}\sin^{1/6}z$ (because $\tan z\cot z = 1$), so $\omega_{x_i\,(i)(8)} = He^{a_4}\sin^{1/6}z$.
- $\omega_{x_t}{}^{(4)}{}_{(t)} = (f_4/f_t)\,\Gamma^{x_4}{}_{x_tx_t} = e^{a_4}\sin^{-1/6}z\cdot e^{-2a_4}\sin^{1/3}z\,a_4' = a_4'e^{-a_4}\sin^{1/6}z$, and lowering with $\eta_{44} = -1$: $\omega_{x_t\,(4)(t)} = -a_4'e^{-a_4}\sin^{1/6}z$.
- $\omega_{x_t}{}^{(t)}{}_{(8)} = (f_t/f_8)\,\Gamma^{x_t}{}_{x_tx_8} = e^{-a_4}\sin^{1/6}z\,\tan z\cdot H\cot z = He^{-a_4}\sin^{1/6}z$, and lowering with $\eta_{tt} = -1$: $\omega_{x_t\,(t)(8)} = -He^{-a_4}\sin^{1/6}z$.

Antisymmetry can be seen on one example: $\omega_{x_i}{}^{(4)}{}_{(i)} = (f_4/f_i)\Gamma^{x_4}{}_{x_ix_i} = e^{-a_4}\sin^{-1/6}z\cdot e^{2a_4}\sin^{1/3}z\,a_4' = a_4'e^{a_4}\sin^{1/6}z$, and lowering with $\eta_{44} = -1$ gives $\omega_{x_i\,(4)(i)} = -a_4'e^{a_4}\sin^{1/6}z = -\omega_{x_i\,(i)(4)}$. With three values of $i$ and three of $t$ this gives exactly 12 independent nonzero components $\omega_{\mu ab}$ with $a < b$ (PROVED; `Revision/theory/reports/wolfram-field-theory.json`, check `omega_components`).

**The spinor connection.** The **generators** $S^{ab} = \frac14[\gamma^{(a)}, \gamma^{(b)}]$, with the **commutator** $[A, B] = AB - BA$, are, for $a \neq b$, $S^{ab} = \frac14(\gamma^{(a)}\gamma^{(b)} - \gamma^{(b)}\gamma^{(a)}) = \frac14(2\gamma^{(a)}\gamma^{(b)}) = \frac12\gamma^{(a)}\gamma^{(b)}$ (because the two gammas anticommute). The spinor connection is $\Omega_\mu = \frac12\sum_{a,b}\omega_{\mu ab}S^{ab} = \sum_{a<b}\omega_{\mu ab}S^{ab}$ (the pairs $(a, b)$ and $(b, a)$ give equal terms, because both $\omega_{\mu ab}$ and $S^{ab}$ change sign). Inserting the components:

$$
\begin{aligned}
\Omega_{x_i} &= \omega_{x_i(i)(4)}S^{i4} + \omega_{x_i(i)(8)}S^{i8} = \tfrac12 e^{a_4}\sin^{1/6}z\,\big(a_4'\gamma^{(i)}\gamma^{(4)} + H\gamma^{(i)}\gamma^{(8)}\big), \\
\Omega_{x_t} &= \omega_{x_t(4)(t)}S^{4t} + \omega_{x_t(t)(8)}S^{t8} = -\tfrac12 e^{-a_4}\sin^{1/6}z\,\big(a_4'\gamma^{(4)}\gamma^{(t)} + H\gamma^{(t)}\gamma^{(8)}\big), \\
\Omega_{x_4} &= \Omega_{x_8} = 0 .
\end{aligned}
$$

These are the formulas of the record (`Revision/theory/field-theory.json`, formula key `Omega_components`). Two exact properties of this connection are used below. It makes the gammas **covariantly constant**: $\partial_\mu\gamma^\nu + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}\gamma^\lambda + [\Omega_\mu, \gamma^\nu] = 0$ for all 64 pairs $(\mu, \nu)$ (PROVED; `python-field-theory.json`, check `covariant_constancy_D_mu_gamma_nu`). And its **curvature** $F_{\mu\nu} = \partial_\mu\Omega_\nu - \partial_\nu\Omega_\mu + [\Omega_\mu, \Omega_\nu]$ equals $\frac14\sum_{\rho,\sigma}R_{\rho\sigma\mu\nu}\gamma^\rho\gamma^\sigma$, where $R_{\rho\sigma\mu\nu}$ is the Riemann tensor of the metric with its first index lowered (PROVED; `python-field-theory.json`, check `spinor_curvature_equals_riemann`, and `wolfram-field-theory.json`, check `spin_curvature_equals_Riemann`).

### 8.5 What cancels and what survives: the term $\gamma^\mu\Omega_\mu = 3H\gamma^{(8)}$

The gravitational term of the field equation is $\gamma^\mu D_\mu\Psi - \gamma^\mu\partial_\mu\Psi = \gamma^\mu\Omega_\mu\Psi$. We compute the matrix $\gamma^\mu\Omega_\mu$ direction by direction (no sum), then add.

**A 3-space direction $x_i$.** Line by line:

$$
\begin{aligned}
\gamma^{x_i}\Omega_{x_i} &= \frac{\gamma^{(i)}}{e^{a_4}\sin^{1/6}z}\cdot\tfrac12 e^{a_4}\sin^{1/6}z\,\big(a_4'\gamma^{(i)}\gamma^{(4)} + H\gamma^{(i)}\gamma^{(8)}\big) \\
&= \tfrac12\big(a_4'\gamma^{(i)}\gamma^{(i)}\gamma^{(4)} + H\gamma^{(i)}\gamma^{(i)}\gamma^{(8)}\big) \\
&= \tfrac12 a_4'\gamma^{(4)} + \tfrac12 H\gamma^{(8)} .
\end{aligned}
$$

The first line inserts $\gamma^{x_i} = \gamma^{(i)}/f_i$ and $\Omega_{x_i}$; the second cancels the scale factor against its inverse; the third uses $(\gamma^{(i)})^2 = +I_{16}$ (a space-like direction).

**An extra time $x_t$.** Line by line:

$$
\begin{aligned}
\gamma^{x_t}\Omega_{x_t} &= \frac{\gamma^{(t)}}{e^{-a_4}\sin^{1/6}z}\cdot\Big(-\tfrac12 e^{-a_4}\sin^{1/6}z\Big)\big(a_4'\gamma^{(4)}\gamma^{(t)} + H\gamma^{(t)}\gamma^{(8)}\big) \\
&= -\tfrac12\big(a_4'\gamma^{(t)}\gamma^{(4)}\gamma^{(t)} + H\gamma^{(t)}\gamma^{(t)}\gamma^{(8)}\big) \\
&= -\tfrac12\big(-a_4'\gamma^{(4)}\gamma^{(t)}\gamma^{(t)} + H\gamma^{(t)}\gamma^{(t)}\gamma^{(8)}\big) \\
&= -\tfrac12\big(a_4'\gamma^{(4)} - H\gamma^{(8)}\big) = -\tfrac12 a_4'\gamma^{(4)} + \tfrac12 H\gamma^{(8)} .
\end{aligned}
$$

The first line inserts $\gamma^{x_t} = \gamma^{(t)}/f_t$ and $\Omega_{x_t}$; the second cancels the scale factors; the third moves $\gamma^{(t)}$ to the right past $\gamma^{(4)}$, which changes the sign (they anticommute); the fourth uses $(\gamma^{(t)})^2 = -I_{16}$ (a time-like direction) in both terms.

**The time $x_4$ and the hidden direction $x_8$.** $\Omega_{x_4} = \Omega_{x_8} = 0$, so $\gamma^{x_4}\Omega_{x_4} = \gamma^{x_8}\Omega_{x_8} = 0$.

**The sum.** The coefficient of $\gamma^{(4)}$ is $3\cdot\frac12 a_4' + 3\cdot(-\frac12 a_4') = 0$: the three inflating directions and the three deflating extra times cancel exactly. The coefficient of $\gamma^{(8)}$ is $6\cdot\frac12 H = 3H$: the six directions that carry the warp $\sin^{1/6}z$ add up. Hence

$$
\gamma^\mu\Omega_\mu = 3H\gamma^{(8)}
$$

for every history $a_4(x_4)$, every $H > 0$ and every point. This is PROVED, and the Revision record proves it twice: the sympy report `python-field-theory.json` has the checks `time_terms_cancel_hidden_term_survives` and `gamma_mu_Omega_mu_equals_3H_gamma_x8`, and the independent Wolfram report `wolfram-field-theory.json` has the checks `gammaOmega_x4_terms_cancel` and `gammaOmega_equals_3H_gamma_x8`. The cancellation happens because 3-space inflates at exactly the rate at which the extra times deflate: the same balance makes the volume factor $\cos z$ independent of the time. Exercise 2 of Section 8.39 shows what would happen if the extra times inflated too.

**The divergence form.** The same matrix has a second, shorter formula. The rule $\Gamma^\mu{}_{\mu\nu} = \partial_\nu\ln f_\mu$ of Section 8.4, summed over $\mu$, gives $\sum_\mu\Gamma^\mu{}_{\mu\nu} = \partial_\nu\ln(f_1\cdots f_8) = \partial_\nu\ln\sqrt{|g|}$. Now sum the covariant constancy of Section 8.4 over $\mu = \nu$:

$$
\begin{aligned}
0 &= \sum_\mu\Big(\partial_\mu\gamma^\mu + \sum_\lambda\Gamma^\mu{}_{\mu\lambda}\gamma^\lambda + \Omega_\mu\gamma^\mu - \gamma^\mu\Omega_\mu\Big) \\
&= \sum_\mu\partial_\mu\gamma^\mu + \sum_\lambda(\partial_\lambda\ln\sqrt{|g|})\gamma^\lambda + \sum_\mu(\Omega_\mu\gamma^\mu - \gamma^\mu\Omega_\mu) \\
&= \frac{1}{\sqrt{|g|}}\sum_\mu\partial_\mu\big(\sqrt{|g|}\gamma^\mu\big) - 2\sum_\mu\gamma^\mu\Omega_\mu .
\end{aligned}
$$

The first line is the covariant constancy with $\nu = \mu$, summed; the second uses the summed rule for the Christoffel symbols; the third combines the first two sums by the product rule ($\partial(\sqrt{|g|}\gamma) = \sqrt{|g|}\,\partial\gamma + (\partial\sqrt{|g|})\gamma$, divided by $\sqrt{|g|}$) and uses $\Omega_\mu\gamma^\mu = -\gamma^\mu\Omega_\mu$ for each $\mu$ (Section 8.8 proves this anticommutation). Therefore

$$
\gamma^\mu\Omega_\mu = \frac{1}{2\sqrt{|g|}}\sum_\mu\partial_\mu\big(\sqrt{|g|}\gamma^\mu\big) .
$$

For the author's metric only $\mu = x_8$ contributes: $\sqrt{|g|}\gamma^{x_8} = \cos z\tan z\,\gamma^{(8)} = \sin z\,\gamma^{(8)}$, whose $x_8$ derivative is $6H\cos z\,\gamma^{(8)}$, and dividing by $2\cos z$ gives $3H\gamma^{(8)}$ again; the term with $\mu = x_4$ is $\partial_4(\cos z\,\gamma^{(4)}) = 0$ because $\cos z$ does not depend on the time, and the other six vanish because nothing depends on $x_1, x_2, x_3, x_5, x_6, x_7$ (PROVED; `python-field-theory.json`, check `divergence_of_sqrtg_gamma`). In words: the term is half the divergence of the coordinate gammas weighted with the volume factor, a **half-density term**.

### 8.6 Non-triviality: the connection vanishes only in flat space

**The connection is zero only in the flat limit.** Each of the 12 components of Section 8.4 is $a_4'$ times one of the factors $\pm e^{\pm a_4}\sin^{1/6}z$ (six components), or $H$ times one of them (the other six). These factors are never zero for $0 < z < \pi/2$: an exponential is never zero, and $\sin z > 0$ there. The 28 matrices $S^{ab}$ with $a < b$ are **linearly independent**: no combination of them with coefficients that are not all zero gives the zero matrix (Notebook 08c checks it: written as 28 rows of $16 \times 16 = 256$ numbers they have rank 28). So, line by line:

1. $\Omega_\mu = \sum_{a<b}\omega_{\mu ab}S^{ab}$ is zero exactly when all its coefficients $\omega_{\mu ab}$ are zero (linear independence).
2. If $a_4' \neq 0$, the six components of the form $a_4'\times$(factor) are not zero; if $H \neq 0$, the six of the form $H\times$(factor) are not zero.
3. Therefore $\Omega_\mu = 0$ for every $\mu$ if and only if $a_4' = 0$ and $H = 0$.

The case $H = 0$ is the formal flat limit; it is not a member of the author's family (Section 8.2). For every metric of the family the canonical spin connection is therefore not zero. This is PROVED; in the Revision record it is the check `nontriviality_Omega_zero_iff_flat` of the sympy report `python-field-theory.json` and the check `Omega_vanishes_iff_a4prime_and_H_vanish` of the Wolfram report `wolfram-field-theory.json`.

**The term is not zero for any field that is not zero.** Suppose $3H\gamma^{(8)}\Psi = 0$ at some point. Multiply from the left by $\gamma^{(8)}/(3H)$ (allowed, since $H > 0$): $\gamma^{(8)}\gamma^{(8)}\Psi = 0$, and $(\gamma^{(8)})^2 = I_{16}$ gives $\Psi = 0$. So in the diagonal frame the gravitational term $3H\gamma^{(8)}\Psi$ is nonzero wherever the field is nonzero (PROVED; `wolfram-field-theory.json`, checks `nontriviality_1_dirac16complex` and `nontriviality_2_dirac16complex00`).

**What this proves, and what it does not.** Read literally, in the diagonal frame and for the field variables $\Psi$, the tests [1] and [2] hold: the field equations always contain the nonzero gravitational term $3H\gamma^{(8)}\Psi$, and the spin connection vanishes only in flat 4+4 space. Sections 8.7 to 8.10 and 8.30 make precise which parts of this statement survive a change of frame or of variables.

### 8.7 The deflation is invisible in the term, but not in the curvature

**No $a_4$ in the term.** The result $\gamma^\mu\Omega_\mu = 3H\gamma^{(8)}$ contains neither $a_4$ nor $a_4'$ nor $a_4''$: the deflation of the extra times leaves no trace in this term (PROVED; `Revision/theory/reports/python-scope.json`, check `gammaOmega_blind_to_the_deflation`). Along the deflating history the separate pieces do change: the components $\omega_{x_1\,(1)(4)}$ and $\omega_{x_1\,(1)(8)}$ of the inflating direction grow like $e^{a_4}$, those of a deflating extra time shrink like $e^{-a_4}$. Contracted with the coordinate gammas, which carry the inverse factors, each piece becomes constant, and the pieces then cancel; Notebook 08c draws this (Figure 08c.2).

**The geometry of the $a_4$ sector is curved.** The mixed Ricci tensor of the author's metric (Chapter 3) is diagonal, with

$$
R^{x_i}{}_{x_i} = a_4'' - 6H^2, \quad R^{x_4}{}_{x_4} = 6(a_4')^2, \quad R^{x_t}{}_{x_t} = -a_4'' - 6H^2, \quad R^{x_8}{}_{x_8} = -6H^2,
$$

and the Ricci scalar is $R = 3(a_4'' - 6H^2) + 6(a_4')^2 + 3(-a_4'' - 6H^2) - 6H^2 = 6\big((a_4')^2 - 7H^2\big)$ (adding the eight diagonal entries: the $a_4''$ terms cancel and $-18H^2 - 18H^2 - 6H^2 = -42H^2$). (PROVED; `wolfram-field-theory.json`, check `ricci_mixed_components`, and `python-field-theory.json`, check `curvature_nonzero_flat_only_formally`.) Since $R^{x_8}{}_{x_8} = -6H^2 < 0$ for every $H > 0$ and every $a_4$, the metric is never flat (`wolfram-field-theory.json`, check `never_flat_for_H_positive`). And $R^{x_4}{}_{x_4} = 6(a_4')^2$ is not zero whenever $a_4$ changes: the deflation is real curvature, which the term $\gamma^\mu\Omega_\mu$ does not see.

**Where the deflation does enter.** It enters the field equation through the frame factors of the derivative terms (Section 8.2): the 3-space derivatives carry $e^{-a_4}\sin^{-1/6}z$, which shrinks as 3-space inflates, and the extra-time derivatives carry $e^{a_4}\sin^{-1/6}z$, which grows as the extra times deflate. Sections 8.24 and 8.25 show what this growth does to waves along the extra times.

### 8.8 The connection drops out of the Lagrangian but not out of the field equation

**An anticommutation for each direction.** For each $\mu$ separately (no sum), $\{\gamma^\mu, \Omega_\mu\} = 0$. For $\mu = x_i$ it suffices to check the two products in $\Omega_{x_i}$ against $\gamma^{(i)}$:

$$
\begin{aligned}
\gamma^{(i)}\big(\gamma^{(i)}\gamma^{(4)}\big) + \big(\gamma^{(i)}\gamma^{(4)}\big)\gamma^{(i)} &= \gamma^{(4)} + \gamma^{(i)}\gamma^{(4)}\gamma^{(i)} = \gamma^{(4)} - \gamma^{(4)}\gamma^{(i)}\gamma^{(i)} = \gamma^{(4)} - \gamma^{(4)} = 0,
\end{aligned}
$$

using $(\gamma^{(i)})^2 = I_{16}$, then moving $\gamma^{(i)}$ past $\gamma^{(4)}$ (one sign change), then $(\gamma^{(i)})^2 = I_{16}$ again. For the second product the same three steps read $\gamma^{(i)}\gamma^{(i)}\gamma^{(8)} + \gamma^{(i)}\gamma^{(8)}\gamma^{(i)} = \gamma^{(8)} - \gamma^{(8)}\gamma^{(i)}\gamma^{(i)} = \gamma^{(8)} - \gamma^{(8)} = 0$. For $\mu = x_t$ the products are $\gamma^{(4)}\gamma^{(t)}$ and $\gamma^{(t)}\gamma^{(8)}$: $\gamma^{(t)}\gamma^{(4)}\gamma^{(t)} + \gamma^{(4)}\gamma^{(t)}\gamma^{(t)} = -\gamma^{(4)}\gamma^{(t)}\gamma^{(t)} + \gamma^{(4)}\gamma^{(t)}\gamma^{(t)} = 0$, and $\gamma^{(t)}\gamma^{(t)}\gamma^{(8)} + \gamma^{(t)}\gamma^{(8)}\gamma^{(t)} = \gamma^{(t)}\gamma^{(t)}\gamma^{(8)} - \gamma^{(t)}\gamma^{(t)}\gamma^{(8)} = 0$. For $\mu = x_4, x_8$ the connection is zero. (PROVED; `python-scope.json`, check `connection_free_lagrangian_same_equations`, and `python-field-theory.json`, check `anticommutator_gamma_Omega_vanishes`.)

**The connection drops out of the Lagrangian.** The kinetic part of the Lagrangian (Chapter 7) is $\sqrt{|g|}\cdot\frac12\big(\bar\Psi\gamma^\mu D_\mu\Psi - (D_\mu\bar\Psi)\gamma^\mu\Psi\big)$ with $D_\mu\bar\Psi = \partial_\mu\bar\Psi - \bar\Psi\Omega_\mu$. Its connection part is, line by line,

$$
\tfrac12\big(\bar\Psi\gamma^\mu\Omega_\mu\Psi - (-\bar\Psi\Omega_\mu)\gamma^\mu\Psi\big) = \tfrac12\bar\Psi\big(\gamma^\mu\Omega_\mu + \Omega_\mu\gamma^\mu\big)\Psi = \tfrac12\bar\Psi\{\gamma^\mu, \Omega_\mu\}\Psi = 0 .
$$

The first step keeps only the $\Omega$ parts of the two covariant derivatives; the second collects them between $\bar\Psi$ and $\Psi$; the third is the anticommutation just proved, for each $\mu$. So in this metric the Lagrangian with the canonical spin connection equals the Lagrangian with the connection left out (PROVED; `python-scope.json`, check `connection_free_lagrangian_same_equations`).

**But the field equation keeps the term.** Take the connection-free symmetric Lagrangian of the commuting field, $\mathcal{L}_0 = \sqrt{|g|}\big[\frac12(\bar\Psi\gamma^\mu\partial_\mu\Psi - \partial_\mu\bar\Psi\gamma^\mu\Psi) - mS - U(S)\big]$, and vary it with respect to $\bar\Psi$, treating the components of $\bar\Psi$ and of $\Psi$ as independent variables (Chapter 7 explains why this is allowed). The Euler-Lagrange expression is $\partial\mathcal{L}_0/\partial\bar\Psi - \sum_\mu\partial_\mu\big(\partial\mathcal{L}_0/\partial(\partial_\mu\bar\Psi)\big)$. Line by line:

$$
\begin{aligned}
\frac{\partial\mathcal{L}_0}{\partial\bar\Psi} &= \sqrt{|g|}\big[\tfrac12\gamma^\mu\partial_\mu\Psi - m\Psi - U'(S)\Psi\big], \\
\frac{\partial\mathcal{L}_0}{\partial(\partial_\mu\bar\Psi)} &= -\tfrac12\sqrt{|g|}\gamma^\mu\Psi, \\
\frac{\partial\mathcal{L}_0}{\partial\bar\Psi} - \sum_\mu\partial_\mu\Big(\frac{\partial\mathcal{L}_0}{\partial(\partial_\mu\bar\Psi)}\Big) &= \sqrt{|g|}\big[\tfrac12\gamma^\mu\partial_\mu\Psi - (m + U')\Psi\big] + \tfrac12\sum_\mu\partial_\mu\big(\sqrt{|g|}\gamma^\mu\big)\Psi + \tfrac12\sqrt{|g|}\gamma^\mu\partial_\mu\Psi \\
&= \sqrt{|g|}\Big[\gamma^\mu\partial_\mu\Psi + \frac{1}{2\sqrt{|g|}}\sum_\mu\partial_\mu\big(\sqrt{|g|}\gamma^\mu\big)\Psi - (m + U')\Psi\Big] .
\end{aligned}
$$

The first line differentiates the terms that contain $\bar\Psi$ without a derivative ($\partial S/\partial\bar\Psi = \Psi$ and $\partial U/\partial\bar\Psi = U'(S)\Psi$); the second differentiates the one term that contains $\partial_\mu\bar\Psi$; the third subtracts the derivative of the second line, using the product rule $\partial_\mu(\sqrt{|g|}\gamma^\mu\Psi) = \partial_\mu(\sqrt{|g|}\gamma^\mu)\Psi + \sqrt{|g|}\gamma^\mu\partial_\mu\Psi$; the fourth collects the two halves of $\gamma^\mu\partial_\mu\Psi$. Setting it to zero and using the divergence form of Section 8.5 gives exactly $\gamma^\mu\partial_\mu\Psi + 3H\gamma^{(8)}\Psi = (m + U')\Psi$, the field equation of Section 8.2. (The record proves the same for the Grassmann field with left derivatives: `python-field-theory.json`, check `grassmann_euler_lagrange_psibar_variation`.)

So the gravitational term $3H\gamma^{(8)}\Psi$ is at the same time the term that the canonical spin connection produces and the half-density term that the volume factor produces when a Lagrangian without any spin connection is varied (PROVED; `python-scope.json`, check `connection_free_lagrangian_same_equations`, both engines). This is the first hint that the value $3H\gamma^{(8)}$ is not a deep property of gravity's coupling: the next two sections make that precise.

### 8.9 Another frame: the boosted frame and its term

Take the boosted frame of Section 8.3, with rapidity $b = \beta x_4 + b_0$. Its canonical spin connection (computed from the definition of Section 8.4 with the new frame) satisfies the vielbein postulate and is antisymmetric (PROVED; `python-scope.json`, check `boosted_frame_canonical_connection`). The record then finds, exactly, for every $a_4$, every $H > 0$ and every $\beta$:

$$
\gamma'^\mu\Omega'_\mu = \frac{6H - \beta}{2}\big(\cosh b\,\gamma^{(8)} - \sinh b\,\gamma^{(4)}\big)
$$

(PROVED; `python-scope.json`, check `boosted_frame_gammaOmega_formula`, and the same check of `wolfram-scope.json`). Notebook 08c computes it from the definitions, with sympy. Here we derive it by a shorter route that also explains it.

**Step 1: the matrix that moves the gammas.** Let $J = \gamma^{(4)}\gamma^{(8)}$. Its square is $J^2 = \gamma^{(4)}\gamma^{(8)}\gamma^{(4)}\gamma^{(8)} = -\gamma^{(4)}\gamma^{(4)}\gamma^{(8)}\gamma^{(8)} = -(-I_{16})(I_{16}) = I_{16}$ (anticommute the middle pair, then use the two squares). For a matrix with $J^2 = I_{16}$ the exponential series splits into even and odd powers, and $e^{\theta J} = \cosh\theta\,I_{16} + \sinh\theta\,J$. Define

$$
S = e^{-(b/2)J} = \cosh\tfrac b2\,I_{16} - \sinh\tfrac b2\,J, \qquad S^{-1} = e^{(b/2)J} = \cosh\tfrac b2\,I_{16} + \sinh\tfrac b2\,J .
$$

**Step 2: what $S$ does to each gamma.** $J$ commutes with $\gamma^{(a)}$ for $a \neq 4, 8$ (moving $\gamma^{(a)}$ past the two factors of $J$ changes the sign twice), so $S\gamma^{(a)}S^{-1} = \gamma^{(a)}$ for those six directions. $J$ anticommutes with $\gamma^{(4)}$ and with $\gamma^{(8)}$. To see it for $\gamma^{(4)}$, move $\gamma^{(4)}$ from the left of $J = \gamma^{(4)}\gamma^{(8)}$ to its right: passing the factor $\gamma^{(4)}$ (itself) changes nothing, and passing the factor $\gamma^{(8)}$ changes the sign once, so $\gamma^{(4)}J = \gamma^{(4)}\gamma^{(4)}\gamma^{(8)} = -\gamma^{(4)}\gamma^{(8)}\gamma^{(4)} = -J\gamma^{(4)}$. For $\gamma^{(8)}$ it is the same with the roles exchanged: passing $\gamma^{(4)}$ changes the sign once and passing $\gamma^{(8)}$ changes nothing, so $\gamma^{(8)}J = \gamma^{(8)}\gamma^{(4)}\gamma^{(8)} = -\gamma^{(4)}\gamma^{(8)}\gamma^{(8)} = -J\gamma^{(8)}$. Because $\gamma^{(4)}$ anticommutes with $J$, it turns every power $J^n$ into $(-J)^n$ when it is moved past it, so $\gamma^{(4)}e^{\theta J} = e^{-\theta J}\gamma^{(4)}$ for every number $\theta$; in particular $S\gamma^{(4)} = e^{-(b/2)J}\gamma^{(4)} = \gamma^{(4)}e^{(b/2)J} = \gamma^{(4)}S^{-1}$, and line by line

$$
\begin{aligned}
S\gamma^{(4)}S^{-1} &= \gamma^{(4)}S^{-1}S^{-1} = \gamma^{(4)}e^{bJ} = \gamma^{(4)}\big(\cosh b\,I_{16} + \sinh b\,\gamma^{(4)}\gamma^{(8)}\big) \\
&= \cosh b\,\gamma^{(4)} + \sinh b\,(\gamma^{(4)})^2\gamma^{(8)} = \cosh b\,\gamma^{(4)} - \sinh b\,\gamma^{(8)} .
\end{aligned}
$$

The first line moves $S$ to the right of $\gamma^{(4)}$ (it becomes $S^{-1}$), multiplies the two exponentials ($e^{(b/2)J}e^{(b/2)J} = e^{bJ}$) and writes out $e^{bJ}$; the second multiplies out and uses $(\gamma^{(4)})^2 = -I_{16}$. In the same way $S\gamma^{(8)}S^{-1} = \gamma^{(8)}e^{bJ} = \cosh b\,\gamma^{(8)} + \sinh b\,\gamma^{(8)}\gamma^{(4)}\gamma^{(8)} = \cosh b\,\gamma^{(8)} - \sinh b\,\gamma^{(4)}$ (here $\gamma^{(8)}\gamma^{(4)}\gamma^{(8)} = -\gamma^{(4)}(\gamma^{(8)})^2 = -\gamma^{(4)}$).

**Step 3: the coordinate gammas of the boosted frame.** The boosted frame is $e' = Le$, with the boost matrix $L$; its inverse is $E' = EL^{-1}$ (the inverse of a product is the product of the inverses in reverse order), and $L^{-1}$ is the boost with $-b$. So $\gamma'^\mu = \sum_a E'_a{}^\mu\gamma^{(a)} = \sum_b E_b{}^\mu\tilde\gamma^{(b)}$, where $\tilde\gamma^{(4)} = \cosh b\,\gamma^{(4)} - \sinh b\,\gamma^{(8)}$, $\tilde\gamma^{(8)} = \cosh b\,\gamma^{(8)} - \sinh b\,\gamma^{(4)}$ and $\tilde\gamma^{(a)} = \gamma^{(a)}$ otherwise. By Step 2, $\tilde\gamma^{(b)} = S\gamma^{(b)}S^{-1}$ for every $b$, and therefore $\gamma'^\mu = S\gamma^\mu S^{-1}$.

**Step 4: the connection of the boosted frame.** Chapter 6 proves in general (in its section on local spin covariance) that the canonical spinor connection of the turned frame is $S\Omega_\mu S^{-1} - (\partial_\mu S)S^{-1}$. Here is a shorter argument for the same result. It rests on two facts: the canonical spin connection of every frame makes that frame's coordinate gammas covariantly constant (a consequence of the vielbein postulate), and it is a combination of the $S^{ab}$, so its trace (the sum of its diagonal entries) is zero. Both are established in Chapter 6; we quote them here, and the direct computation of the record and of Notebook 08c confirms their consequence. We show that $\Omega'_\mu = S\Omega_\mu S^{-1} - (\partial_\mu S)S^{-1}$ has both properties, and that only one matrix has them. First, covariant constancy, line by line (with $\partial_\mu S^{-1} = -S^{-1}(\partial_\mu S)S^{-1}$, which follows from differentiating $SS^{-1} = I_{16}$):

$$
\begin{aligned}
\partial_\mu\gamma'^\nu &= (\partial_\mu S)\gamma^\nu S^{-1} + S(\partial_\mu\gamma^\nu)S^{-1} - S\gamma^\nu S^{-1}(\partial_\mu S)S^{-1}, \\
[\Omega'_\mu, \gamma'^\nu] &= S[\Omega_\mu, \gamma^\nu]S^{-1} - (\partial_\mu S)\gamma^\nu S^{-1} + S\gamma^\nu S^{-1}(\partial_\mu S)S^{-1}, \\
\partial_\mu\gamma'^\nu + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}\gamma'^\lambda + [\Omega'_\mu, \gamma'^\nu] &= S\Big(\partial_\mu\gamma^\nu + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}\gamma^\lambda + [\Omega_\mu, \gamma^\nu]\Big)S^{-1} = 0 .
\end{aligned}
$$

The first line is the product rule for $S\gamma^\nu S^{-1}$; the second inserts $\Omega'_\mu$ and $\gamma'^\nu$ into the commutator and multiplies out; the third adds the two lines and the Christoffel term ($\Gamma$ belongs to the metric, the same in both frames), sees the four terms with $\partial_\mu S$ cancel in pairs, and uses the covariant constancy of the diagonal frame. Second, the trace: $\mathrm{tr}(S\Omega_\mu S^{-1}) = \mathrm{tr}\,\Omega_\mu = 0$, and $(\partial_\mu S)S^{-1}$ is a multiple of $J$ (Step 5 below), whose trace is zero (the trace of a product of two different gammas is zero: $\mathrm{tr}(\gamma^{(4)}\gamma^{(8)}) = \mathrm{tr}(\gamma^{(8)}\gamma^{(4)}) = -\mathrm{tr}(\gamma^{(4)}\gamma^{(8)})$, by the cyclic rule of the trace and then anticommutation). Third, uniqueness: if two traceless matrices $\Omega'_1$, $\Omega'_2$ both make the $\gamma'^\nu$ covariantly constant, their difference commutes with every $\gamma'^\nu$; then $S^{-1}(\Omega'_1 - \Omega'_2)S$ commutes with every $\gamma^{(a)}$, so it is a multiple of $I_{16}$ (the gammas form an irreducible representation, Chapter 5; `Revision/algebra/reports/python-algebra.json`, check `pin_commutant_dimension_1`), and a traceless multiple of $I_{16}$ is zero. Hence the canonical connection of the boosted frame is $\Omega'_\mu = S\Omega_\mu S^{-1} - (\partial_\mu S)S^{-1}$.

**Step 5: the term.** Line by line:

$$
\begin{aligned}
\gamma'^\mu\Omega'_\mu &= S\gamma^\mu S^{-1}\big(S\Omega_\mu S^{-1} - (\partial_\mu S)S^{-1}\big) = S\big(\gamma^\mu\Omega_\mu - \gamma^\mu S^{-1}\partial_\mu S\big)S^{-1}, \\
S^{-1}\partial_\mu S &= -\tfrac{\beta}{2}J \ \text{for}\ \mu = x_4, \quad 0 \ \text{otherwise}, \\
\gamma^{x_4}S^{-1}\partial_4 S &= \gamma^{(4)}\big(-\tfrac{\beta}{2}\gamma^{(4)}\gamma^{(8)}\big) = -\tfrac{\beta}{2}(\gamma^{(4)})^2\gamma^{(8)} = \tfrac{\beta}{2}\gamma^{(8)}, \\
\gamma'^\mu\Omega'_\mu &= S\big(3H\gamma^{(8)} - \tfrac{\beta}{2}\gamma^{(8)}\big)S^{-1} = \frac{6H - \beta}{2}\,S\gamma^{(8)}S^{-1} = \frac{6H - \beta}{2}\big(\cosh b\,\gamma^{(8)} - \sinh b\,\gamma^{(4)}\big) .
\end{aligned}
$$

The first line inserts Steps 3 and 4 and cancels $S^{-1}S$; the second differentiates $S = e^{-(b/2)J}$ with $\partial_4 b = \beta$ (only $b$ depends on the coordinates, and only on $x_4$); the third uses $\gamma^{x_4} = \gamma^{(4)}$ ($f_4 = 1$) and $(\gamma^{(4)})^2 = -I_{16}$; the fourth uses $\gamma^\mu\Omega_\mu = 3H\gamma^{(8)}$ (Section 8.5) and Step 2. This is the record's formula.

**The consequence.** For $\beta = 6H$, that is with the rapidity $b = 6Hx_4 + b_0$, the term $\gamma'^\mu\Omega'_\mu$ is identically zero, for every $H > 0$ and every history $a_4$, although the metric is the author's curved metric (PROVED; `python-scope.json`, check `boosted_frame_gammaOmega_vanishes`, both engines). The connection itself is not zero in that frame: $\Omega'_\mu \neq 0$ for $\mu = x_1, \dots, x_7$ (zero only for $x_8$; the same check). So the sentence "the field equation contains the gravitational term $3H\gamma^{(8)}\Psi$" is true in the diagonal frame and false in this frame: it is a statement about one frame, not about the field equation as such. In the boosted frame gravity enters the field equation through the boosted frame vectors $E'_a{}^\mu$ alone.

### 8.10 What no frame removes: the curvature of the connection

**The curvature in two frames.** The curvature of the spinor connection equals the Riemann tensor contracted with two coordinate gammas, $F_{\mu\nu} = \frac14\sum_{\rho,\sigma}R_{\rho\sigma\mu\nu}\gamma^\rho\gamma^\sigma$ (Section 8.4). This identity holds in every frame (a standard theorem, quoted without proof here as in Chapter 6, so ASSUMED in general; the record proves it for this metric in the diagonal frame, and Notebook 08c checks it in the diagonal and in the boosted frame for $(\mu, \nu) = (x_1, x_8)$). Chapter 6 also derives the relation below directly from local spin covariance, without this identity. The Riemann tensor belongs to the metric and is the same in both frames, and $\gamma'^\rho = S\gamma^\rho S^{-1}$ (Section 8.9). Hence, line by line,

$$
F'_{\mu\nu} = \tfrac14\sum_{\rho,\sigma}R_{\rho\sigma\mu\nu}\,S\gamma^\rho S^{-1}S\gamma^\sigma S^{-1} = S\Big(\tfrac14\sum_{\rho,\sigma}R_{\rho\sigma\mu\nu}\gamma^\rho\gamma^\sigma\Big)S^{-1} = SF_{\mu\nu}S^{-1} .
$$

**It is never zero.** In the diagonal frame Notebook 08c finds $F_{x_1x_8} = c_{14}\,\gamma^{(1)}\gamma^{(4)} + c_{18}\,\gamma^{(1)}\gamma^{(8)}$ with

$$
c_{14} = -\frac{Ha_4'e^{a_4}\cos z}{2\sin^{5/6}z}, \qquad c_{18} = -\frac{H^2e^{a_4}\cos z}{2\sin^{5/6}z} .
$$

The coefficient $c_{18}$ is never zero for $H > 0$ and $0 < z < \pi/2$, and $\gamma^{(1)}\gamma^{(4)}$ and $\gamma^{(1)}\gamma^{(8)}$ are linearly independent, so $F_{x_1x_8} \neq 0$ for every history $a_4$. Since $S$ is invertible, $F'_{x_1x_8} = SF_{x_1x_8}S^{-1} \neq 0$ too. If the connection $\Omega'_\mu$ vanished at all points of a region in some frame, its curvature would vanish there; it does not. So the spin connection vanishes in no frame of this kind (PROVED; `python-scope.json`, check `boosted_frame_curvature_nonzero`, both engines, which argues in general: the curvature of the connection is $\frac12R_{ab\mu\nu}S^{ab}$ in every frame, and the metric is curved for $H > 0$).

**Two frames, one curvature.** The square of $F_{x_1x_8}$ is the same in both frames, $F^2 = (c_{14}^2 - c_{18}^2)I_{16} = H^2\big((a_4')^2 - H^2\big)e^{2a_4}\cos^2 z/(4\sin^{5/3}z)\cdot I_{16}$: the products $\gamma^{(1)}\gamma^{(4)}$ and $\gamma^{(1)}\gamma^{(8)}$ square to $+I_{16}$ and $-I_{16}$ and anticommute, so the cross terms cancel, and $F'^2 = SF^2S^{-1} = F^2$ because $F^2$ is a multiple of $I_{16}$. On the canonical history $a_4 = x_4$ (where $a_4' = H = 1$) this square is zero although $F$ is not: $F$ is then **nilpotent** (its square is the zero matrix, like the $2 \times 2$ matrix with rows $(0, 1)$ and $(0, 0)$), and in the boosted frame with $\beta = 6H$ it is $F' = e^{-b}F$ (Exercise 6 of Section 8.39 derives this).

**The frame-independent content of non-triviality.** Putting Sections 8.6 to 8.10 together: the canonical spin connection is nonzero in every frame, because its curvature is the curvature of spacetime, which is nonzero for every $H > 0$; and the frame factors $e^{\mp a_4}\sin^{-1/6}z$ and $\tan z$, none of which is identically 1, multiply every derivative term of the field equation except the one along the time $x_4$ (the derivatives along $x_1, x_2, x_3, x_5, x_6, x_7, x_8$; the factor of $\partial_4$ is $1/f_4 = 1$). These two facts do not depend on any choice. The value $3H\gamma^{(8)}$ of the term $\gamma^\mu\Omega_\mu$ does.

### 8.11 The connection in the energy-momentum tensor

The spin connection drops out of the Lagrangian (Section 8.8), but it does reach the energy-momentum tensor, the source of gravity (Chapter 9). For a field that depends only on the time, $\Phi = \Phi(x_4)$, the entry $K^{x_4}{}_{x_1} = \frac12\big(\bar\Phi\gamma^{x_4}D_{x_1}\Phi - (D_{x_1}\bar\Phi)\gamma^{x_4}\Phi\big)$ has no derivative part ($\partial_1\Phi = 0$), and its connection part is $\frac12\bar\Phi\{\gamma^{x_4}, \Omega_{x_1}\}\Phi$. Line by line, with $\gamma^{x_4} = \gamma^{(4)}$ and $\Omega_{x_1} = \frac12f_1(a_4'\gamma^{(1)}\gamma^{(4)} + H\gamma^{(1)}\gamma^{(8)})$, $f_1 = e^{a_4}\sin^{1/6}z$:

$$
\begin{aligned}
\gamma^{(4)}\gamma^{(1)}\gamma^{(4)} + \gamma^{(1)}\gamma^{(4)}\gamma^{(4)} &= -\gamma^{(1)}\gamma^{(4)}\gamma^{(4)} + \gamma^{(1)}\gamma^{(4)}\gamma^{(4)} = 0, \\
\gamma^{(4)}\gamma^{(1)}\gamma^{(8)} + \gamma^{(1)}\gamma^{(8)}\gamma^{(4)} &= \gamma^{(4)}\gamma^{(1)}\gamma^{(8)} + \gamma^{(4)}\gamma^{(1)}\gamma^{(8)} = 2\gamma^{(4)}\gamma^{(1)}\gamma^{(8)}, \\
\tfrac12\{\gamma^{x_4}, \Omega_{x_1}\} &= \tfrac12\cdot\tfrac12 f_1\big(a_4'\cdot 0 + H\cdot 2\gamma^{(4)}\gamma^{(1)}\gamma^{(8)}\big) = \tfrac12 e^{a_4}\sin^{1/6}z\,H\,\gamma^{(4)}\gamma^{(1)}\gamma^{(8)} .
\end{aligned}
$$

The first line moves the first $\gamma^{(4)}$ past $\gamma^{(1)}$ (one sign) and finds that the $a_4'$ part cancels; the second moves $\gamma^{(4)}$ in the second product to the front past two gammas (two signs); the third collects. The bilinear matrix $C\gamma^{(4)}\gamma^{(1)}\gamma^{(8)}$ is not the zero matrix, so this entry is not zero in general (PROVED; `python-scope.json`, check `spin_connection_in_the_energy_momentum_tensor`, both engines). Chapter 9 uses this entry (Section 9.12).

### 8.12 Example: the term in two frames, computed from the definitions

Notebook 08c puts Sections 8.3 to 8.11 to work, exactly, with sympy, for a symbolic history $a_4(x_4)$ and symbolic $H$, $\beta$, $b_0$. It builds the scale factors and the metric and compares them with the record; computes all Christoffel symbols and the canonical spin connection of the diagonal frame and checks the vielbein postulate for all 512 components; shows that the connection vanishes only for $a_4' = 0$ and $H = 0$; computes $\gamma^\mu\Omega_\mu$ direction by direction and draws what cancels and what survives; computes the Ricci components and shows that the term contains no $a_4$; builds the boosted frame and finds $\gamma'^\mu\Omega'_\mu$; computes the spinor curvature in both frames; and checks the connection part of the energy-momentum tensor. It needs no Rust and runs in one to two minutes; the times measured on the build computer, which depend on how busy that computer is, are recorded in the notebook's provenance file `Revision/textbook/notebooks/08c_frame_dependence.PROVENANCE.md`. It ends with the line ALL 32 CHECKS PASSED (notebook 08c).

<!-- NOTEBOOK 08c -->

### 8.15 Line-by-line walk-through of Notebook 08c

The notebook has 14 code cells, In [1] to In [14]. This section explains every line of every one of them, in order: a line or a small group of lines is quoted exactly and then explained. A line that starts with `#` is a **comment**, which Python skips; it is there for the reader. In the quoted code a line `...` stands for the remaining lines of a long figure caption; every caption is printed in full under its figure in Section 8.14, and a paragraph "What Figure 08c.k shows" after the code says what to look for. Because Notebook 08c is the first notebook of this chapter, its set-up cell and its two record helpers are explained here in full; the walk-throughs of Notebooks 08a, 08b and 08d refer back to this explanation.

**In [1], the set-up cell.** The first part of the cell, down to the two lines of `-` and `=` signs, is the complete run instructions of Section 8.13 again, as comment lines, so that the notebook file carries its own instructions. The code starts below the line that announces THE SET-UP. It computes no physics, and it is the same in every notebook of the book except for one line, the notebook's name.

```python
import json  # reads and writes JSON files (text files that hold names and numbers)
import os  # reads the environment variable TEXTBOOK_OUTPUT_ROOT (explained below)
import textwrap  # breaks long printed text into lines of at most 89 characters
from pathlib import Path  # file and folder paths that work on Windows, macOS and Linux
```

`import` loads a **module** (a part of Python or of an installed package) so that the cell can use it. `json` reads and writes the text format JSON, in which the Revision record stores its results (a JSON file holds names and values: numbers, texts, lists and dictionaries); `os` gives access to the computer's environment; `textwrap` breaks long text into lines; `from pathlib import Path` takes the single name `Path` out of the module `pathlib`. A `Path` is the address of a file or a folder, written the same way on every operating system.

```python
import matplotlib  # the plotting package
import matplotlib.pyplot as plt  # its drawing functions, called plt by convention
from IPython.display import Image, display  # shows a saved picture below a cell

NOTEBOOK_ID = "08c"  # this notebook: chapter 08, example c
```

These lines load the plotting package matplotlib, its drawing functions under the short name `plt`, and the two functions `Image` and `display` of IPython (the part of Jupyter that runs Python), which show a picture file below a cell. A **variable** is a name for a value; the last line gives the name `NOTEBOOK_ID` to the **string** (a text in quotes) `"08c"`. The figure files are named after it.

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

`def` defines a **function**: a named piece of code that runs when it is called. The text in triple quotes under the `def` line is its **docstring**, a description that Python stores but does not run. `Path.cwd()` is the folder in which the notebook runs, and `.resolve()` writes it as a complete address. `here.parents` is the list of the folders above it, and `[here, *here.parents]` is the list that starts with `here` and continues with all of them (the star unpacks one list into another). The `for` loop takes these folders one after the other; the operator `/` joins a folder and a name into a longer path; `.is_file()` is true when that file exists. The first folder that holds `Revision/textbook/requirements.txt` is the repository, and `return` hands it back. If no folder does, `raise` stops the notebook with a `FileNotFoundError` whose message says what to do.

```python
# The repository folder.  It is never printed: it differs from computer to computer,
# and the printed output of a notebook must not.
REPO = find_repository_root()
# Every file is WRITTEN below OUTPUT_ROOT.  OUTPUT_ROOT is the repository folder unless
# the environment variable TEXTBOOK_OUTPUT_ROOT names another folder; the book's
# checking tool sets it, so that a check run writes into a scratch folder instead.
OUTPUT_ROOT = Path(os.environ.get("TEXTBOOK_OUTPUT_ROOT", str(REPO)))
```

`REPO` is the repository folder found by the function. An **environment variable** is a named text that the computer hands to every program it starts; `os.environ.get(name, default)` returns its value, or the default when it is not set. So `OUTPUT_ROOT`, the folder below which files are written, is the repository, unless the book's checking tool names a scratch folder; then a check run never changes the repository.

```python
def repository_file(relative):
    """The path of the repository file relative, for READING (a Revision record)."""
    return REPO / relative


def output_file(relative):
    """The path at which to WRITE the repository file relative (its folder is made)."""
    path = OUTPUT_ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def say(text):
    """Print text in lines of at most 89 characters (the width of a page of the book)."""
    print(textwrap.fill(str(text), width=89, subsequent_indent="    "))
```

`repository_file` gives the path of a repository file for reading. `output_file` gives the path at which to write a file and first creates its folder: `path.parent` is the folder of the file, and `mkdir(parents=True, exist_ok=True)` makes it together with any missing folders above it and does nothing if it exists already. `say` prints a text broken into lines of at most 89 characters; `str(text)` turns any value into a string first, and the continuation lines are indented by four blanks.

```python
matplotlib.rcdefaults()  # ignore personal matplotlib settings: same figures everywhere
plt.rcParams.update({"figure.figsize": (7.0, 4.2), "font.size": 10.0,
                     "axes.grid": True, "grid.alpha": 0.3})
```

matplotlib reads personal settings from the computer it runs on; `rcdefaults()` throws them away, so that every computer draws the same figures. `rcParams` is matplotlib's dictionary of settings (a **dictionary** is a table of pairs key: value in curly brackets); the update sets the standard figure size (7 by 4.2 inches), the font size, and a faint grid in every plot.

```python
FIGURE_FOLDER = "Revision/textbook/figures"  # where the figures are saved
CAPTION_FILE = f"{FIGURE_FOLDER}/{NOTEBOOK_ID}.captions.json"  # their captions
FIGURE_NUMBERS = {}  # figure name -> its number k (file name <id>_<k>_<name>.png)
CAPTIONS = {}  # figure file name -> caption, written to CAPTION_FILE after every figure
# Start with an empty captions file ({} is an empty JSON dictionary); save_figure fills
# it.  newline="\n" writes the same line ends on Windows, macOS and Linux.
output_file(CAPTION_FILE).write_text("{}\n", encoding="utf-8", newline="\n")
```

A string that starts with `f` is an **f-string**: the names in curly brackets are replaced by their values, so `CAPTION_FILE` is `Revision/textbook/figures/08c.captions.json`. `FIGURE_NUMBERS` and `CAPTIONS` start as empty dictionaries. The last line writes the text `{}` and a line end into the captions file, in the character encoding UTF-8 and with the line end `\n` on every operating system.

```python
def save_figure(fig, name, caption):
    """Save the figure fig as Revision/textbook/figures/<id>_<k>_<name>.png, record its
    caption in CAPTION_FILE, show the saved picture below the cell and close the figure.
    k counts the figures of the notebook 1, 2, 3, ...; a cell run again keeps its k."""
    number = FIGURE_NUMBERS.setdefault(name, len(FIGURE_NUMBERS) + 1)
    file_name = f"{NOTEBOOK_ID}_{number}_{name}.png"
    relative = f"{FIGURE_FOLDER}/{file_name}"
```

`setdefault(name, value)` returns the number already stored for this name, or stores and returns `value`, here one more than the number of figures so far; so the figures are numbered 1, 2, 3, ... in the order in which they are first saved, and a cell that is run twice keeps its number. The next two lines build the file name, for example `08c_1_cancel_and_survive.png`, and its path relative to the repository.

```python
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

`fig.savefig` writes the picture as a PNG file with the options explained in the comments. `plt.close(fig)` removes the figure from matplotlib's memory, so that Jupyter does not draw it again at the end of the cell. The caption is stored in the dictionary, and the whole dictionary is written into the captions file as JSON text (`json.dumps` turns it into a string; `indent=1` puts every entry on its own line and `sort_keys=True` sorts the entries, so that the file is always the same). `display(Image(...))` shows the saved picture below the cell; the `metadata` tells the book's tools which figure it is. The last line prints, for example, `Figure 08c.1 saved as Revision/textbook/figures/08c_1_cancel_and_survive.png`.

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

`PASSED` is an empty **list** (a sequence of values in square brackets). `check` is the notebook's test: if the condition is false, `raise AssertionError` stops the notebook with a message that names the check; otherwise the name is appended to `PASSED` and a line `PASS name` is printed, followed, when the argument `record` is given, by a line `reproduces ...` that names the Revision record and its check. `None` is Python's value for "nothing given".

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

`report` prints a key number as a line that starts with `RESULT`; the expression `(f" {unit}" if unit else "")` adds the unit only when one is given. `all_checks_passed` prints the last line of the notebook, with `len(PASSED)`, the number of checks that passed. The last statement prints the only output of the cell, `Set-up of notebook 08c complete: repository folder found, helpers defined.`

**In [2], the record helpers, the gammas, the symbols and the metric.**

```python
import numpy as np  # numbers and matrices (for the plots)
import sympy as sp  # exact algebra with symbols

REPORTS = {}  # report file -> {check name: (verdict, detail)}, each read once
```

numpy (short name `np`) computes with arrays of floating-point numbers; sympy (short name `sp`) computes exactly with symbols, fractions and functions. `REPORTS` is an empty dictionary that will hold each Revision report after it has been read once.

```python
def record_says(report_file, check_name, *pieces):
    """True when the Revision report records the check check_name with the verdict
    pass and its detail text contains every given piece of text."""
    if report_file not in REPORTS:  # read the report the first time it is needed
        data = json.loads(repository_file(report_file).read_text(encoding="utf-8"))
        REPORTS[report_file] = {entry["name"]: (entry["verdict"].lower(),
                                                entry["detail"])
                                for entry in data["checks"]}
    verdict, detail = REPORTS[report_file][check_name]
    return verdict == "pass" and all(piece in detail for piece in pieces)
```

A Revision report is a JSON file with a list `checks`; each entry has a `name`, a `verdict` (`PASS` or `FAIL`, written in capitals by some verifiers and in small letters by others) and a `detail` text. `*pieces` collects any number of further arguments into a tuple (a fixed list). The first time a report is needed, `json.loads` turns its text into Python values, and the **dictionary comprehension** in curly brackets builds the table name: (verdict in small letters, detail) for every entry. Then the function looks up the check and returns true only if its verdict is `pass` and every piece of text occurs in the detail (`piece in detail` asks whether one string is part of another; `all(...)` is true when every item is). A check name that the report does not contain makes the lookup fail with an error, which also stops the notebook.

```python
def check_record(condition, title, report_file, check_names, *pieces):
    """check() for a result that reproduces Revision checks (one name or a list of
    names): it passes only if condition is true AND the report records every one
    of them as passed, with every piece of text in the detail of the first one."""
    names = [check_names] if isinstance(check_names, str) else list(check_names)
    on_record = record_says(report_file, names[0], *pieces) and all(
        record_says(report_file, name) for name in names[1:])
    word = "check" if len(names) == 1 else "checks"
    check(condition and on_record, title,
          record=f"{report_file}, {word} " + " and ".join(names))
```

`check_record` is `check` for a result that the Revision record also contains. `isinstance(check_names, str)` asks whether a single name (a string) was given; then it is put into a one-element list, otherwise the given names are turned into a list. The record must report the first check as passed with every piece of text in its detail, and every further check as passed. The check passes only if the notebook's own computation (`condition`) holds AND the record says so; the `record=` line then names the file and the check or checks (`" and ".join(names)` joins the names with the word `and`). So a PASS line with a `reproduces` line means two independent things agree: this notebook's computation and the Revision verifier.

```python
gammas_record = json.loads(
    repository_file("Revision/algebra/gammas.json").read_text(encoding="utf-8"))
G = [sp.Matrix(rows) for rows in gammas_record["gamma"]]  # gamma^(x1) ... (x8)
ETA = gammas_record["eta"]  # [1, 1, 1, -1, -1, -1, -1, 1]
C = sp.Matrix(gammas_record["C"])  # C = gamma^(x8) gamma^(x1) gamma^(x2) gamma^(x3)
```

The file `gammas.json` of the Revision record holds the eight gamma matrices as lists of rows of whole numbers, the frame metric `eta` and the matrix `C`. The **list comprehension** `[sp.Matrix(rows) for rows in ...]` turns each gamma into an exact sympy matrix; `G[0]` is $\gamma^{(1)}$, `G[3]` is $\gamma^{(4)}$ and `G[7]` is $\gamma^{(8)}$.

```python
x = sp.symbols("x1:9", real=True)  # the coordinates; x[0] is x1, x[7] is x8
H = sp.Symbol("H", positive=True)
beta, b0 = sp.symbols("beta b0", real=True)  # the boost: rapidity beta x4 + b0
a4 = sp.Function("a4")(x[3])  # the metric function: ANY function of x4
z = 6 * H * x[7]
sixth = sp.sin(z) ** sp.Rational(1, 6)  # sin(z)^(1/6)
```

`sp.symbols("x1:9")` makes the eight symbols `x1`, ..., `x8` (the range 1 to 8; the end 9 is not included); `real=True` tells sympy they are real numbers, and `positive=True` that $H > 0$. `sp.Function("a4")(x[3])` is an unknown function $a_4(x_4)$: nothing is assumed about it, so every check below holds for every history. `z` is the expression $6Hx_8$ and `sixth` the expression $\sin^{1/6}z$ (`sp.Rational(1, 6)` is the exact fraction $1/6$, not the decimal number $0.1666\ldots$).

```python
f = [sp.exp(a4) * sixth] * 3 + [sp.Integer(1)] + [sp.exp(-a4) * sixth] * 3 \
    + [sp.cot(z)]  # the scale factors f_1, ..., f_8
g = [ETA[a] * f[a] ** 2 for a in range(8)]  # the diagonal entries g_aa
third = sp.sin(z) ** sp.Rational(1, 3)
authors_metric = [sp.exp(2 * a4) * third] * 3 + [-1] \
    + [-sp.exp(-2 * a4) * third] * 3 + [sp.cot(z) ** 2]
```

`[value] * 3` is a list with three copies of the value, and `+` joins lists; so `f` is the list of the eight scale factors of Section 8.2 (the backslash at the end of a line continues the statement on the next line). `g` holds the diagonal entries $g_{aa} = \eta_{aa}f_a^2$ (`range(8)` runs through 0, 1, ..., 7). `authors_metric` is the author's metric typed directly from his formula, as a second, independent copy.

```python
def is_zero(expr):
    """True when sympy shows that expr is exactly zero (two simplifications)."""
    expr = sp.sympify(expr)
    if expr == 0:
        return True
    simpler = sp.simplify(expr)
    return simpler == 0 or sp.simplify(sp.fu(simpler)) == 0
```

`is_zero` decides whether an exact expression is zero. `sp.sympify` turns plain Python numbers into sympy numbers; if the expression is already the number 0, the answer is yes. Otherwise sympy's general simplifier `sp.simplify` is tried, and if that does not reach 0, the trigonometric simplifier `sp.fu` followed by `simplify` again. (An answer "no" would only mean that sympy did not find a proof; every check of the notebook that uses `is_zero` needs the answer "yes", or that a quantity is NOT zero; for the latter the notebook also prints the expression, so that the reader can see it.)

```python
# The record prints each entry as sympy writes it, e.g. "g_x8x8 = cot(6*H*x8)**2".
metric_texts = [f"g_x{a + 1}x{a + 1} = {sp.sstr(authors_metric[a])}" for a in range(8)]
say(metric_texts[0])
say(metric_texts[4])
check_record(all(is_zero(g[a] - authors_metric[a]) for a in range(8)),
             "eta_aa f_a^2 is the author's metric (all 8 diagonal entries)",
             "Revision/theory/reports/python-field-theory.json",
             "metric_from_vielbein_equals_SPEC", *metric_texts)
check_record(is_zero(sp.prod(f) - sp.cos(z)), "sqrt|g| = f1 f2 ... f8 = cos z",
             "Revision/theory/reports/python-field-theory.json",
             "sqrt_det_g_equals_cos_z", "cos(6 H x8)")
```

`sp.sstr` writes an expression as sympy's text (powers with `**`). The list `metric_texts` holds the eight entries in the form in which the record prints them, for example `g_x1x1 = exp(2*a4(x4))*sin(6*H*x8)**(1/3)`; two of them are printed. The first check compares the eight entries $\eta_{aa}f_a^2$ with the author's entries exactly, and it requires the record's check `metric_from_vielbein_equals_SPEC` to contain all eight texts (`*metric_texts` passes the list as eight separate arguments). The second check multiplies the eight scale factors (`sp.prod`) and compares with $\cos z$. Output: the two entries and two PASS lines, each with its `reproduces` line.

**In [3], the Christoffel symbols.**

```python
Gam = [[[sp.Integer(0)] * 8 for _ in range(8)] for _ in range(8)]
for lam in range(8):
    for mu in range(8):
        for nu in range(8):
            value = 0  # the bracket of the formula; g is diagonal, so only these
            if lam == nu:  # three cases contribute
                value += sp.diff(g[lam], x[mu])
            if lam == mu:
                value += sp.diff(g[lam], x[nu])
            if mu == nu:
                value -= sp.diff(g[mu], x[lam])
            if value != 0:
                Gam[lam][mu][nu] = sp.simplify(value / (2 * g[lam]))
```

`Gam` is an $8 \times 8 \times 8$ table of exact zeros (a list of 8 lists of 8 lists of 8 zeros; `_` is a loop name that is not used). The three nested loops run over all 512 index triples. For a diagonal metric $g_{\lambda\nu}$ is nonzero only for $\lambda = \nu$, so the bracket $\partial_\mu g_{\lambda\nu} + \partial_\nu g_{\lambda\mu} - \partial_\lambda g_{\mu\nu}$ of the formula of Section 8.4 has at most the three terms that the three `if` lines add (`sp.diff(expr, x[mu])` is the exact partial derivative; `+=` adds to a variable, `-=` subtracts). If the bracket is not zero, the symbol is the bracket divided by $2g_{\lambda\lambda}$, simplified.

```python
independent = sum(1 for lam in range(8) for mu in range(8) for nu in range(mu, 8)
                  if Gam[lam][mu][nu] != 0)
report("independent nonzero Christoffel symbols", independent)
for lam, mu, nu in ((0, 0, 3), (4, 3, 4), (0, 0, 7), (7, 7, 7)):
    say(f"Gamma^x{lam + 1}_x{mu + 1} x{nu + 1} = {Gam[lam][mu][nu]}")
check_record(independent == 25, "25 independent nonzero Christoffel symbols",
             "Revision/theory/reports/python-field-theory.json",
             "christoffel_symmetric_metric_compatible",
             f"{independent} independent nonzero symbols")
```

The **generator expression** counts 1 for every nonzero symbol with $\mu \le \nu$ (the symbols are symmetric in the two lower indices, so the pairs with $\nu < \mu$ are not new); the count is printed as a RESULT line: 25. The loop prints four symbols (index positions from 0, printed as names from 1): $\Gamma^{x_1}{}_{x_1x_4} = a_4'$, which sympy writes `Derivative(a4(x4), x4)`; $\Gamma^{x_5}{}_{x_4x_5} = -a_4'$; $\Gamma^{x_1}{}_{x_1x_8} = H/\tan z = H\cot z$; and $\Gamma^{x_8}{}_{x_8x_8} = -12H/\sin(2z)$, which is the table's $-6H/(\sin z\cos z)$ because $\sin 2z = 2\sin z\cos z$. The check requires 25 and the record's text "25 independent nonzero symbols".

**In [4], the frame, its connection and the vielbein postulate.**

```python
S_AB = [[(G[a] * G[c] - G[c] * G[a]) / 4 for c in range(8)] for a in range(8)]


def boost(b):
    """The boost by the rapidity b in the frame plane (x4, x8), and its inverse."""
    L, L_inverse = sp.eye(8), sp.eye(8)
    L[3, 3] = L[7, 7] = L_inverse[3, 3] = L_inverse[7, 7] = sp.cosh(b)
    L[3, 7] = L[7, 3] = sp.sinh(b)
    L_inverse[3, 7] = L_inverse[7, 3] = -sp.sinh(b)
    return L, L_inverse
```

`S_AB[a][c]` is the generator $S^{ac} = \frac14[\gamma^{(a)}, \gamma^{(c)}]$ for all 64 pairs (the letter `c` is used for the second frame index because `b` is the rapidity). `boost(b)` starts from two $8 \times 8$ unit matrices (`sp.eye(8)`) and fills the entries of the $(x_4, x_8)$ plane (rows and columns 3 and 7): $\cosh b$ on the diagonal and $\sinh b$ off it for the boost $L$ of Section 8.3, and $-\sinh b$ off the diagonal for its inverse, the boost with $-b$ (multiply the two: $\cosh^2 b - \sinh^2 b = 1$ on the diagonal, $-\cosh b\sinh b + \sinh b\cosh b = 0$ off it).

```python
def frame(b):
    """Vielbein e[a, mu], inverse E[mu, a], connection omega[mu, a, c] (mixed),
    Omega_mu and gamma^mu of the diagonal frame boosted by the rapidity b."""
    L, L_inverse = boost(b)
    e = L * sp.diag(*f)
    E = sp.diag(*[1 / value for value in f]) * L_inverse
```

`frame(b)` builds everything for the frame boosted by $b$ (for $b = 0$, the diagonal frame). `sp.diag(*f)` is the diagonal matrix with the scale factors on its diagonal, the diagonal frame $e^a{}_\mu = f_a\delta^a_\mu$; multiplying by $L$ from the left combines its rows, the frame vectors, exactly as in Section 8.3. The inverse is the product of the inverses in reverse order: the diagonal matrix of the $1/f_a$ times $L^{-1}$; `E[mu, a]` is $E_a{}^\mu$.

```python
    omega = {}
    for mu in range(8):
        for a in range(8):
            for c in range(8):
                value = 0  # e^a_nu (d_mu E_c^nu + Gamma^nu_mu,lam E_c^lam)
                for nu in range(8):
                    if e[a, nu] == 0:
                        continue  # skip the terms that are zero anyway
                    term = sp.diff(E[nu, c], x[mu])
                    for lam in range(8):
                        if Gam[nu][mu][lam] != 0 and E[lam, c] != 0:
                            term += Gam[nu][mu][lam] * E[lam, c]
                    value += e[a, nu] * term
                omega[mu, a, c] = sp.simplify(value)
```

This is the definition of the canonical spin connection of Section 8.4, $\omega_\mu{}^a{}_c = \sum_\nu e^a{}_\nu(\partial_\mu E_c{}^\nu + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}E_c{}^\lambda)$, written as four nested loops. `continue` jumps to the next $\nu$ when $e^a{}_\nu = 0$, and the inner `if` skips products with a zero factor; both only save time. The result is stored in the dictionary `omega` under the key `(mu, a, c)`; it is the connection with the first frame index up (the "mixed" form).

```python
    Omega = []
    for mu in range(8):
        matrix = sp.zeros(16, 16)
        for a in range(8):
            for c in range(a + 1, 8):  # (1/2) sum over all a, c = sum over a < c
                matrix += ETA[a] * omega[mu, a, c] * S_AB[a][c]
        Omega.append(matrix)
    gamma_up = [sum((E[mu, a] * G[a] for a in range(8)), sp.zeros(16, 16))
                for mu in range(8)]
    return {"e": e, "E": E, "omega": omega, "Omega": Omega, "gamma": gamma_up}
```

For each $\mu$ the spinor connection $\Omega_\mu = \sum_{a<c}\omega_{\mu ac}S^{ac}$ is built from a $16 \times 16$ zero matrix (`sp.zeros(16, 16)`); `ETA[a] * omega[mu, a, c]` lowers the first frame index, $\omega_{\mu ac} = \eta_{aa}\omega_\mu{}^a{}_c$. The coordinate gammas are $\gamma^\mu = \sum_a E_a{}^\mu\gamma^{(a)}$ (the sum starts from the zero matrix given as the second argument of `sum`). The function returns a dictionary with the five objects.

```python
def postulate_failures(fr):
    """How many of the 512 components of the vielbein postulate are not zero."""
    failures = 0
    for a in range(8):
        for mu in range(8):
            for nu in range(8):
                value = sp.diff(fr["e"][a, nu], x[mu]) \
                    - sum(Gam[lam][mu][nu] * fr["e"][a, lam] for lam in range(8)) \
                    + sum(fr["omega"][mu, a, c] * fr["e"][c, nu] for c in range(8))
                failures += 0 if is_zero(value) else 1
    return failures
```

`postulate_failures` evaluates the vielbein postulate $\partial_\mu e^a{}_\nu - \sum_\lambda\Gamma^\lambda{}_{\mu\nu}e^a{}_\lambda + \sum_c\omega_\mu{}^a{}_c e^c{}_\nu$ for all $8 \times 8 \times 8 = 512$ index triples and counts the ones that are not zero (`0 if ... else 1` is 0 when the component vanishes and 1 otherwise).

```python
def antisymmetric(fr):
    """omega_mu,ac = eta_aa omega_mu^a_c is antisymmetric in a, c for every mu."""
    return all(is_zero(ETA[a] * fr["omega"][mu, a, c] + ETA[c] * fr["omega"][mu, c, a])
               for mu in range(8) for a in range(8) for c in range(8))


diagonal = frame(sp.Integer(0))
check_record(postulate_failures(diagonal) == 0 and antisymmetric(diagonal),
             "diagonal frame: vielbein postulate (512 components), omega antisymmetric",
             "Revision/theory/reports/python-field-theory.json",
             ["vielbein_postulate", "spin_connection_antisymmetric"],
             "(512 components)")
```

`antisymmetric` checks $\omega_{\mu ac} + \omega_{\mu ca} = 0$ for all 512 triples. Then the diagonal frame is built with $b = 0$ (`sp.Integer(0)` is sympy's exact zero) and the first check of the cell requires zero failures, antisymmetry, and the two record checks `vielbein_postulate` (whose detail must contain "(512 components)") and `spin_connection_antisymmetric`.

```python
nonzero = [(mu, a, c) for mu in range(8) for a in range(8) for c in range(a + 1, 8)
           if not is_zero(diagonal["omega"][mu, a, c])]
omega_diagonal = diagonal["omega"]
for mu, a, c in nonzero:
    say(f"omega_x{mu + 1},(x{a + 1})(x{c + 1}) = "
        f"{sp.simplify(ETA[a] * omega_diagonal[mu, a, c])}")
check_record(len(nonzero) == 12, "12 independent nonzero components omega_mu,ab (a < b)",
             "Revision/theory/reports/wolfram-field-theory.json", "omega_components",
             f"exactly {len(nonzero)} independent nonzero omega_mu,ab (a < b)")
```

`nonzero` lists every index triple $(\mu, a, c)$ with $a < c$ whose component is not zero, and the loop prints each lowered component $\omega_{\mu ac}$. The output shows exactly the 12 components of Section 8.4, in sympy's notation: for $x_1, x_2, x_3$ the pair `exp(a4(x4))*sin(6*H*x8)**(1/6)*Derivative(a4(x4), x4)` and `H*exp(a4(x4))*sin(6*H*x8)**(1/6)`, and for $x_5, x_6, x_7$ the same with $e^{-a_4}$ and a minus sign. The check requires 12 and the Wolfram record's text with the number 12.

**In [5], the connection vanishes only in flat space.**

```python
a4_prime = sp.diff(a4, x[3])  # a4' = d a4 / d x4
A1 = sp.Symbol("A1", real=True)  # a letter that stands for a4'
allowed = [sign * sp.exp(power * a4) * sixth for sign in (1, -1) for power in (1, -1)]
kinds = []  # for each component: "A1" (a4' times a factor) or "H" (H times a factor)
```

`a4_prime` is $a_4'$. `A1` is a plain symbol that the cell puts in place of $a_4'$ (the Revision record writes `A1` for $a_4'$). `allowed` is the list of the four factors $\pm e^{\pm a_4}\sin^{1/6}z$ (two loops: two signs times two powers). `kinds` will record, for each of the 12 components, which shape it has.

```python
for mu, a, c in nonzero:
    value = sp.simplify(ETA[a] * omega_diagonal[mu, a, c]).subs(a4_prime, A1)
    found = [str(coupling) for coupling in (A1, H) for factor in allowed
             if is_zero(value - coupling * factor)]  # which shape fits
    kinds.append(found[0] if len(found) == 1 else "no shape")
n_A1, n_H = kinds.count("A1"), kinds.count("H")
report("components of the form a4' x factor and H x factor", f"{n_A1}, {n_H}")
```

For each nonzero component, `.subs(a4_prime, A1)` replaces $a_4'$ by the letter `A1`, and `found` lists the names of the couplings ($a_4'$ or $H$) for which the component equals coupling times one allowed factor. Exactly one shape must fit; otherwise the component is marked `"no shape"`. `count` counts the two kinds. Output: `RESULT components of the form a4' x factor and H x factor = 6, 6`.

```python
S_rows = np.array([[float(v) for v in S_AB[a][c]] for a in range(8)
                   for c in range(a + 1, 8)])  # 28 rows of 256 numbers
rank_S = int(np.linalg.matrix_rank(S_rows))
report("rank of the 28 matrices S^ab written as rows of 256 numbers", rank_S)
```

Each of the 28 generators $S^{ac}$ with $a < c$ is written as one row of its 256 entries (iterating over a sympy matrix gives its entries row by row; `float` turns each into a decimal number). `np.linalg.matrix_rank` computes the **rank** of the $28 \times 256$ array: the number of independent rows. Output: 28, so the 28 generators are linearly independent.

```python
# a4' != 0 makes the six "A1" components nonzero, H != 0 the six "H" components;
# with independent S^ab, Omega vanishes for every mu only when a4' = 0 and H = 0.
check_record(n_A1 == 6 and n_H == 6 and rank_S == 28,
             "Omega_mu = 0 for every mu iff a4' = 0 and H = 0 (formal flat limit)",
             "Revision/theory/reports/python-field-theory.json",
             "nontriviality_Omega_zero_iff_flat",
             "the S^ab are linearly independent",
             "every Omega_mu vanishes iff a4' = 0 AND H = 0")
```

The comment repeats the three-line argument of Section 8.6, and the check combines its three ingredients (six components of each kind, rank 28) with the record's check `nontriviality_Omega_zero_iff_flat`, whose detail must contain the two quoted sentences.

**In [6], what cancels and what survives.**

```python
per_direction = [(diagonal["gamma"][mu] * diagonal["Omega"][mu]).applyfunc(sp.simplify)
                 for mu in range(8)]
coefficient_4 = [sp.simplify(-(G[3] * M).trace() / 16) for M in per_direction]
coefficient_8 = [sp.simplify((G[7] * M).trace() / 16) for M in per_direction]
```

`per_direction[mu]` is the product $\gamma^{x_\mu}\Omega_{x_\mu}$ (no sum); `.applyfunc(sp.simplify)` simplifies each of its 256 entries. The **trace** (`.trace()`) of a matrix is the sum of its diagonal entries. If $M = c_4\gamma^{(4)} + c_8\gamma^{(8)}$, then $\mathrm{tr}(\gamma^{(8)}M) = c_4\,\mathrm{tr}(\gamma^{(8)}\gamma^{(4)}) + c_8\,\mathrm{tr}(I_{16}) = 16c_8$ and $\mathrm{tr}(\gamma^{(4)}M) = c_4\,\mathrm{tr}(-I_{16}) + c_8\,\mathrm{tr}(\gamma^{(4)}\gamma^{(8)}) = -16c_4$, because the trace of a product of two different gammas is zero (Section 8.9, Step 4). So the two lists hold the coefficients $c_4$ and $c_8$ of every direction.

```python
nothing_else = all(
    all(is_zero(entry) for entry in
        per_direction[mu] - coefficient_4[mu] * G[3] - coefficient_8[mu] * G[7])
    for mu in range(8))
for mu in range(8):
    say(f"gamma^x{mu + 1} Omega_x{mu + 1} = ({coefficient_4[mu]}) gamma^(x4) "
        f"+ ({coefficient_8[mu]}) gamma^(x8)")
check(nothing_else, "each gamma^mu Omega_mu (no sum) is a combination of gamma^(x4) "
      "and gamma^(x8)")
```

`nothing_else` subtracts $c_4\gamma^{(4)} + c_8\gamma^{(8)}$ from each product and asks whether every entry of the remainder is zero: the trace formula is valid only if nothing else is left. The loop prints the eight products: $(a_4'/2)\gamma^{(4)} + (H/2)\gamma^{(8)}$ for $x_1, x_2, x_3$; zero for $x_4$ and $x_8$; $(-a_4'/2)\gamma^{(4)} + (H/2)\gamma^{(8)}$ for $x_5, x_6, x_7$, exactly the results of Section 8.5. The check prints its PASS line.

```python
THEORY = "Revision/theory/reports/python-field-theory.json"  # the sympy record
# The record writes A1 for a4'; the partial sums in the record's notation:
inflating_sum = sp.simplify(sum(coefficient_4[:3])).subs(a4_prime, A1)  # 3*A1/2
deflating_sum = sp.simplify(sum(coefficient_4[4:7])).subs(a4_prime, A1)  # -3*A1/2
hidden_sum = sp.simplify(sum(coefficient_8))  # 3*H
say(f"sums: inflating {inflating_sum}, deflating {deflating_sum}, hidden {hidden_sum}")
```

`THEORY` is a short name for the path of the sympy field-theory report. `coefficient_4[:3]` is the part of the list with positions 0, 1, 2 (the directions $x_1, x_2, x_3$) and `coefficient_4[4:7]` the part with positions 4, 5, 6 ($x_5, x_6, x_7$). The three partial sums are printed in the record's notation: `sums: inflating 3*A1/2, deflating -3*A1/2, hidden 3*H`.

```python
check_record([sp.simplify(c4 / a4_prime) for c4 in coefficient_4]
             == [sp.Rational(1, 2)] * 3 + [0] + [-sp.Rational(1, 2)] * 3 + [0]
             and [sp.simplify(c8 / H) for c8 in coefficient_8]
             == [sp.Rational(1, 2)] * 3 + [0] + [sp.Rational(1, 2)] * 3 + [0],
             "per direction: +a4'/2 and -a4'/2 cancel, six times H/2 add up",
             THEORY, "time_terms_cancel_hidden_term_survives",
             f"inflating sum {inflating_sum}, deflating sum {deflating_sum}",
             f"the six hidden-direction terms add to {hidden_sum} gamma^(x8)")
```

The coefficients of $\gamma^{(4)}$ are divided by $a_4'$ and must be exactly $\frac12$ for $x_1, x_2, x_3$, then $0$ for $x_4$, $-\frac12$ for $x_5, x_6, x_7$ and $0$ for $x_8$; the coefficients of $\gamma^{(8)}$ are divided by $H$ and must be $\frac12$ for the same six directions and $0$ for $x_4$ and $x_8$. The record's check must contain the printed partial sums.

```python
total = sum(per_direction, sp.zeros(16, 16))
check_record(all(is_zero(entry) for entry in total - 3 * H * G[7]),
             "gamma^mu Omega_mu = 3 H gamma^(x8) in the diagonal frame",
             THEORY, "gamma_mu_Omega_mu_equals_3H_gamma_x8",
             "gamma^mu Omega_mu = 3 H gamma^(x8) exactly")
# gamma^(x8) squares to 1, so it is invertible: 3 H gamma^(x8) Psi = 0 only for
# Psi = 0. The gravitational term is not zero for any field Psi that is not zero.
check_record(G[7] * G[7] == sp.eye(16),
             "(gamma^(x8))^2 = 1: 3 H gamma^(x8) Psi != 0 for every Psi != 0 (H > 0)",
             "Revision/theory/reports/wolfram-field-theory.json",
             "nontriviality_1_dirac16complex",
             "every Psi != 0 (gamma^(x8) is invertible)")
```

`total` adds the eight products: the matrix $\gamma^\mu\Omega_\mu$. The first check compares it entry by entry with $3H\gamma^{(8)}$. The second checks $(\gamma^{(8)})^2 = I_{16}$, the argument of Section 8.6 that $3H\gamma^{(8)}\Psi = 0$ only for $\Psi = 0$, together with the Wolfram record's non-triviality check.

```python
sqrt_g = sp.cos(z)
divergence = sum((sp.diff(sqrt_g * diagonal["gamma"][mu], x[mu]) for mu in range(8)),
                 sp.zeros(16, 16)) / (2 * sqrt_g)
check_record(all(is_zero(entry) for entry in divergence - 3 * H * G[7]),
             "(1/(2 sqrt|g|)) d_mu(sqrt|g| gamma^mu) = 3 H gamma^(x8) (divergence "
             "form)", THEORY, "divergence_of_sqrtg_gamma",
             "= 3 H gamma^(x8) = gamma^mu Omega_mu")
```

`divergence` is the half-density term $\frac{1}{2\sqrt{|g|}}\sum_\mu\partial_\mu(\sqrt{|g|}\gamma^\mu)$ of Section 8.5, computed with $\sqrt{|g|} = \cos z$ (sympy differentiates a matrix entry by entry); the check compares it with $3H\gamma^{(8)}$.

```python
check_record(all(all(is_zero(entry) for entry in
                     diagonal["gamma"][mu] * diagonal["Omega"][mu]
                     + diagonal["Omega"][mu] * diagonal["gamma"][mu])
                 for mu in range(8)),
             "{gamma^mu, Omega_mu} = 0 for each mu: Omega drops out of the Lagrangian",
             "Revision/theory/reports/python-scope.json",
             "connection_free_lagrangian_same_equations",
             "{gamma^mu, Omega_mu} = 0 for each mu separately")
```

This check computes the anticommutator $\{\gamma^\mu, \Omega_\mu\}$ for each of the eight directions separately and requires every entry to be zero: the fact of Section 8.8 that removes the connection from the Lagrangian.

```python
names = [f"$x_{mu + 1}$" for mu in range(8)] + ["sum"]
values_4 = [float(sp.simplify(c4 / a4_prime)) for c4 in coefficient_4]
values_8 = [float(sp.simplify(c8 / H)) for c8 in coefficient_8]
values_4.append(sum(values_4))
values_8.append(sum(values_8))
colours = ["tab:blue"] * 3 + ["gray"] + ["tab:red"] * 3 + ["gray", "black"]
```

For the bar chart: nine bar labels (the directions, written as LaTeX for matplotlib, and `"sum"`), the coefficients in units of $a_4'$ and of $H$ as decimal numbers, each list extended by its sum (`append` adds one element at the end), and nine colours (blue for 3-space, red for the extra times, gray for $x_4$ and $x_8$, black for the sum).

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0), sharey=True)
left.bar(names, values_4, color=colours)
left.set_title("coefficient of $\\gamma^{(4)}$, in units of $a_4'$")
left.set_ylabel("coefficient")
right.bar(names, values_8, color=colours)
right.set_title("coefficient of $\\gamma^{(8)}$, in units of $H$")
for panel in (left, right):
    panel.axhline(0.0, color="black", linewidth=0.8)
    panel.set_xlabel("direction $\\mu$ of $\\gamma^{\\mu}\\Omega_{\\mu}$")
save_figure(fig, "cancel_and_survive",
            "The term $\\gamma^\\mu\\Omega_\\mu$ of the field equation in the "
            ...
            "history $a_4$ and every $H > 0$.")
```

`plt.subplots(1, 2, ...)` makes a figure with one row of two panels (axes), `left` and `right`, 10 by 4 inches, with a shared vertical axis. `bar` draws one bar per label with the given heights and colours. The titles and labels are LaTeX text between dollar signs (in a Python string a backslash is written twice). `axhline(0.0, ...)` draws a horizontal line at zero in both panels. `save_figure` saves the figure as Figure 08c.1 with its caption.

**What Figure 08c.1 shows.** Two bar charts with the eight directions $x_1, \dots, x_8$ and their sum on the horizontal axis; the vertical axis is a pure number. Left: the coefficient of $\gamma^{(4)}$ in units of $a_4'$: three blue bars at $+\frac12$ (3-space), a gray bar at 0 ($x_4$), three red bars at $-\frac12$ (the extra times), a gray bar at 0 ($x_8$), and a black sum bar at 0. Right: the coefficient of $\gamma^{(8)}$ in units of $H$: six bars at $+\frac12$ and a sum bar at $3$. The student should see the cancellation of the time-direction pieces (because the extra times deflate at the rate at which 3-space inflates) and the addition of the six hidden-direction pieces. The values are exact and hold for every history.

**In [7], the curvature, and the pieces along the history.**

```python
def riemann(rho, sigma, mu, nu):
    """R^rho_sigma,mu,nu from the Christoffel symbols (not simplified)."""
    value = sp.diff(Gam[rho][nu][sigma], x[mu]) - sp.diff(Gam[rho][mu][sigma], x[nu])
    for lam in range(8):
        value += Gam[rho][mu][lam] * Gam[lam][nu][sigma] \
            - Gam[rho][nu][lam] * Gam[lam][mu][sigma]
    return value
```

`riemann` evaluates the Riemann tensor $R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \sum_\lambda(\Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma})$ (Chapter 3) for one index quadruple.

```python
ricci = [sum(riemann(rho, a, rho, a) for rho in range(8)) / g[a] for a in range(8)]
a4_second = sp.diff(a4, x[3], 2)
expected = [a4_second - 6 * H**2] * 3 + [6 * a4_prime**2] \
    + [-a4_second - 6 * H**2] * 3 + [-6 * H**2]
check_record(all(is_zero(ricci[a] - expected[a]) for a in range(8)),
             "R^x1_x1 = a4'' - 6H^2, R^x4_x4 = 6 a4'^2, R^x5_x5 = -a4'' - 6H^2, "
             "R^x8_x8 = -6H^2", "Revision/theory/reports/wolfram-field-theory.json",
             "ricci_mixed_components", "R^1_1 = R^2_2 = R^3_3 = a4'' - 6 H^2",
             "R^4_4 = 6 a4'^2", "R^5_5 = R^6_6 = R^7_7 = -a4'' - 6 H^2",
             "R^8_8 = -6 H^2")
```

The Ricci tensor is $R_{aa} = \sum_\rho R^\rho{}_{a\rho a}$, and for a diagonal metric its mixed form is $R^a{}_a = R_{aa}/g_{aa}$; `ricci` holds the eight diagonal entries. `sp.diff(a4, x[3], 2)` is $a_4''$. The check compares them with the values of Section 8.7 and with the four texts of the Wolfram record.

```python
ricci_scalar = sp.factor(sp.simplify(sum(ricci)).subs(a4_prime, A1))  # A1 for a4'
say(f"Ricci scalar in the record's notation: R = {ricci_scalar}")
check_record(is_zero(sum(ricci) - 6 * (a4_prime**2 - 7 * H**2)),
             "Ricci scalar R = 6 (a4'^2 - 7 H^2): curved for every H > 0",
             THEORY, "curvature_nonzero_flat_only_formally",
             f"Ricci scalar R = {sp.sstr(ricci_scalar)}")
check_record(not total.applyfunc(sp.simplify).has(a4) and not is_zero(ricci[3]),
             "gamma^mu Omega_mu contains no a4, although R^x4_x4 = 6 a4'^2 is not zero",
             "Revision/theory/reports/python-scope.json",
             "gammaOmega_blind_to_the_deflation",
             "contains neither e^a4 nor a4' nor a4''", "R^x4_x4 = 6 a4'^2")
```

The Ricci scalar is the sum of the eight entries; `sp.factor` writes it as a product, and it is printed as `R = 6*(A1**2 - 7*H**2)`. The first check compares it with $6((a_4')^2 - 7H^2)$ and with the record's text. The second check asks whether the simplified matrix $\gamma^\mu\Omega_\mu$ contains the function $a_4$ at all (`.has(a4)` is true if $a_4$ or a derivative of it occurs anywhere in it) and requires that $R^{x_4}{}_{x_4}$ is not zero.

```python
parameters = json.loads(repository_file(
    "Revision/kohn_sham/results/parameters.json").read_text(encoding="utf-8"))
A_history = parameters["physics"]["historyA"]  # the canonical history a4 = A H x4
history = sp.Lambda(x[3], A_history * x[3])  # with H = 1: a4 = x4
```

The parameters of the Revision Kohn-Sham record hold the constant $A$ of the canonical history $a_4 = AHx_4$ (here $A = 1$), the prescribed background of the book's Kohn-Sham chapters. `sp.Lambda(x[3], A_history * x[3])` is the function $x_4 \mapsto Ax_4$, which is $a_4$ when $H = 1$.

```python
def along_history(expr):
    """A numpy function of x4 for expr with H = 1, a4 = A x4, z = pi/4."""
    concrete = expr.replace(sp.Function("a4"), history).doit()
    concrete = concrete.subs({H: 1, x[7]: sp.pi / 24})  # z = 6 x8 = pi/4
    return sp.lambdify(x[3], concrete, "numpy")
```

`along_history` turns an exact expression into a numerical function of the time: `replace` puts the history in place of the unknown function $a_4$, `doit()` carries out the derivatives that then become computable ($a_4' = A$), `subs` puts in $H = 1$ and $x_8 = \pi/24$, so that $z = 6x_8 = \pi/4$, and `sp.lambdify` makes a numpy function of $x_4$.

```python
times = np.linspace(0.0, 4.0, 201)
pieces = {"$\\omega_{x_1,(1)(4)} = a_4'e^{a_4}\\sin^{1/6}z$": diagonal["omega"][0, 0, 3],
          "$\\omega_{x_1,(1)(8)} = He^{a_4}\\sin^{1/6}z$": diagonal["omega"][0, 0, 7],
          "$|\\omega_{x_5,(4)(5)}| = a_4'e^{-a_4}\\sin^{1/6}z$":
              -ETA[3] * diagonal["omega"][4, 3, 4],
          "$|\\omega_{x_5,(5)(8)}| = He^{-a_4}\\sin^{1/6}z$":
              ETA[4] * diagonal["omega"][4, 4, 7]}
```

`np.linspace(0.0, 4.0, 201)` is an array of 201 equally spaced times from 0 to 4. The dictionary `pieces` maps four legend labels to four components of the connection: the two of the inflating direction $x_1$ and the two of the extra time $x_5$ (the factors `-ETA[3]` and `ETA[4]` turn the stored mixed components into the sizes named in the labels; the plot takes absolute values anyway).

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
for (label, expr), style in zip(pieces.items(), ("-", "--", "-", "--")):
    left.plot(times, np.abs(along_history(expr)(times)) * np.ones_like(times),
              style, label=label)
left.set_yscale("log")
left.set_xlabel("time $x_4$")
left.set_ylabel("size of the component")
left.set_title("Pieces of the connection")
left.legend(fontsize=7)
```

`zip` pairs each (label, expression) with a line style: one minus sign in quotes for a solid line, two minus signs for a dashed one. Each component is evaluated along the history at the 201 times; `np.abs` takes the size, and multiplying by `np.ones_like(times)` (an array of ones) makes sure that an expression that happens to be constant is still drawn as a full curve. The vertical axis is logarithmic (`set_yscale("log")`), so an exponential is a straight line.

```python
inflating = along_history(sum(coefficient_4[:3]))(times) * np.ones_like(times)
deflating = along_history(sum(coefficient_4[4:7]))(times) * np.ones_like(times)
right.plot(times, inflating, color="tab:blue", label="$x_1, x_2, x_3$: $+3a_4'/2$")
right.plot(times, deflating, color="tab:red", label="$x_5, x_6, x_7$: $-3a_4'/2$")
right.plot(times, inflating + deflating, color="black", label="sum: $0$")
right.set_ylim(-2.0, 2.0)
right.set_xlabel("time $x_4$")
right.set_ylabel("coefficient of $\\gamma^{(4)}$")
right.set_title("Their contraction: constant, cancels")
right.legend(fontsize=8);
save_figure(fig, "pieces_along_history",
            "Along the canonical history $a_4 = x_4$ of the Kohn-Sham record ($A = "
            ...
            "sums stay constant, and they cancel exactly (black).")
```

The right panel draws the two partial sums of the $\gamma^{(4)}$ coefficients (3-space and extra times) along the history, and their sum; `set_ylim` fixes the vertical range. The semicolon after `right.legend(fontsize=8)` stops Jupyter from printing the value of that line (it would print an object with a memory address that changes from run to run). The figure is saved as Figure 08c.2. The cell prints three PASS lines, each with its `reproduces` line, and the figure line.

**What Figure 08c.2 shows.** Both panels have the time $x_4$ (units of $1/H$, with $H = 1$) on the horizontal axis, along the history $a_4 = x_4$ at $z = \pi/4$. Left, on a logarithmic vertical axis, four components of the canonical spin connection (pure numbers in units of $H$): the two of the inflating direction $x_1$ rise along a straight line (they grow like $e^{a_4}$), the two of the deflating extra time $x_5$ fall along a straight line (they shrink like $e^{-a_4}$); the dashed and the solid curves coincide because here $a_4' = AH = 1 = H$. Right: the coefficient of $\gamma^{(4)}$ in $\gamma^\mu\Omega_\mu$, summed over 3-space (blue, $+\frac32$) and over the extra times (red, $-\frac32$), and their sum (black, 0): three horizontal lines. The student should see that the pieces of the connection change exponentially while their contraction with the coordinate gammas does not change at all, and cancels: the deflation is invisible in the term.

**In [8], the boosted frame.**

```python
rapidity = beta * x[3] + b0
boosted = frame(rapidity)
e_b = boosted["e"]
same_metric = all(
    is_zero(sum(ETA[a] * e_b[a, mu] * e_b[a, nu] for a in range(8))
            - (g[mu] if mu == nu else 0)) for mu in range(8) for nu in range(8))
SCOPE = "Revision/theory/reports/python-scope.json"  # the record of these checks
check_record(same_metric and all(is_zero(v) for v in e_b * boosted["E"] - sp.eye(8)),
             "the boosted frame gives the same metric (64 entries); e' E' = 1",
             SCOPE, "boosted_frame_reproduces_metric",
             "equals the author's metric for all 64 (mu, nu)")
```

The rapidity is the expression $b = \beta x_4 + b_0$ with symbolic $\beta$ and $b_0$, and `frame(rapidity)` builds the boosted frame, its connection and its gammas exactly. `same_metric` checks, for all 64 pairs $(\mu, \nu)$, that $\sum_a\eta_{aa}e'^a{}_\mu e'^a{}_\nu$ is $g_{\mu\mu}$ on the diagonal and 0 off it (the expression `(g[mu] if mu == nu else 0)` chooses). The check also verifies that $E'$ is the inverse of $e'$ ($e'E' = I_8$). `SCOPE` is a short name for the path of the scope report.

```python
failures = postulate_failures(boosted)  # the number of nonzero components
check_record(failures == 0 and antisymmetric(boosted),
             "boosted frame: vielbein postulate (512 components), omega' antisymmetric",
             SCOPE, "boosted_frame_canonical_connection",
             f"holds for all 512 (a, mu, nu) ({failures} failures)")
```

The vielbein postulate and the antisymmetry for the boosted frame; the record's text must contain the same number of failures, 0.

```python
total_boosted = sum((boosted["gamma"][mu] * boosted["Omega"][mu] for mu in range(8)),
                    sp.zeros(16, 16))
formula = (6 * H - beta) / 2 * (sp.cosh(rapidity) * G[7] - sp.sinh(rapidity) * G[3])
check_record(all(is_zero(entry) for entry in total_boosted - formula),
             "gamma'^mu Omega'_mu = ((6H - beta)/2) (cosh b gamma^(x8) - sinh b "
             "gamma^(x4))", SCOPE, "boosted_frame_gammaOmega_formula",
             "gamma'^mu Omega'_mu = ((6 H - beta)/2) (cosh b gamma^(x8) - sinh b "
             "gamma^(x4))")
```

`total_boosted` is $\gamma'^\mu\Omega'_\mu$ computed from the definitions; `formula` is the result of Section 8.9; the check compares all 256 entries.

```python
at_6H = {beta: 6 * H}
nonzero_Omega = [mu for mu in range(8) if not all(
    is_zero(ETA[a] * boosted["omega"][mu, a, c].subs(at_6H))
    for a in range(8) for c in range(a + 1, 8))]
nonzero_text = ", ".join(f"x{mu + 1}" for mu in nonzero_Omega)  # "x1, x2, ..."
say("beta = 6H: Omega'_mu is nonzero for mu = " + nonzero_text)
```

`at_6H` is the substitution $\beta = 6H$. `nonzero_Omega` lists the directions $\mu$ for which at least one component $\omega'_{\mu ac}$ is not zero at $\beta = 6H$; because the $S^{ac}$ are linearly independent (In [5]), these are exactly the directions with $\Omega'_\mu \neq 0$. The line printed: `beta = 6H: Omega'_mu is nonzero for mu = x1, x2, x3, x4, x5, x6, x7`.

```python
check_record(all(is_zero(entry.subs(at_6H)) for entry in total_boosted - formula)
             and formula.subs(at_6H) == sp.zeros(16, 16)
             and nonzero_Omega == [0, 1, 2, 3, 4, 5, 6],
             "beta = 6H: gamma'^mu Omega'_mu = 0 identically, Omega'_mu != 0 for "
             "x1..x7", SCOPE, "boosted_frame_gammaOmega_vanishes", "IDENTICALLY ZERO",
             f"nonzero for mu = {nonzero_text} (zero only for x8)")
```

The last check of the cell: at $\beta = 6H$ the computed term equals the formula, the formula is the zero matrix, and the connection is nonzero in the seven directions $x_1, \dots, x_7$; the record must say "IDENTICALLY ZERO" and list the same directions. The cell prints four PASS lines and the line about $\Omega'_\mu$.

**In [9], the size of the term in the boosted frames.**

```python
term = sp.lambdify((beta, x[3], b0), formula.subs(H, 1), "numpy")


def size(matrix):
    """sqrt(tr(M^T M)/16): the size of a 16 x 16 matrix, 1 for gamma^(x8)."""
    matrix = np.array(matrix, dtype=float)
    return np.sqrt(np.trace(matrix.T @ matrix) / 16)
```

`term` is a numerical function of $(\beta, x_4, b_0)$ that returns the $16 \times 16$ matrix $\gamma'^\mu\Omega'_\mu$ at $H = 1$, from the formula that In [8] proved equal to the computed matrix. `size` measures a matrix by $\sqrt{\mathrm{tr}(M^TM)/16}$: $\mathrm{tr}(M^TM)$ is the sum of the squares of all 256 entries, so the size is the square root of that sum divided by 16 (for $\gamma^{(8)}$, a matrix with sixteen entries 1 and no others, it is 1); `@` is numpy's matrix product and `.T` the transpose.

```python
beta_values = np.linspace(0.0, 12.0, 241)
sizes_beta = [size(term(bv, 0.0, 0.0)) for bv in beta_values]
check(abs(size(term(0.0, 0.0, 0.0)) - 3.0) < 1e-12 and size(term(6.0, 0.7, 0.3)) == 0,
      "size 3 in the diagonal frame (3 H gamma^(x8), H = 1), 0 for beta = 6H")
```

The sizes at 241 rapidity rates from 0 to 12, at $x_4 = 0$, $b_0 = 0$. The check: the diagonal frame ($\beta = 0$) gives size 3 to $10^{-12}$ (the term is $3\gamma^{(8)}$), and $\beta = 6H = 6$ gives exactly 0 at another point ($x_4 = 0.7$, $b_0 = 0.3$), because the factor $(6H - \beta)/2$ is exactly zero.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
left.plot(beta_values, sizes_beta)
left.plot([0.0, 6.0], [3.0, 0.0], "o", color="black")
left.annotate("diagonal frame: $3H\\gamma^{(8)}$", (0.0, 3.0), (1.0, 3.3))
left.annotate("$\\beta = 6H$: zero", (6.0, 0.0), (6.6, 0.4))
left.set_xlabel("rapidity rate $\\beta$ (units of $H$)")
left.set_ylabel("size of $\\gamma'^\\mu\\Omega'_\\mu$ (units of $H$)")
left.set_title("At $x_4 = 0$, $b_0 = 0$")
left.set_ylim(-0.2, 4.0)
```

The left panel draws the size against $\beta$, marks the two special points with black dots (`"o"`), and writes a text next to each (`annotate(text, point, text position)`).

```python
times = np.linspace(0.0, 0.5, 101)
for bv in (0.0, 3.0, 6.0, 9.0):
    right.plot(times, [size(term(bv, t, 0.0)) for t in times],
               label=f"$\\beta = {bv:g}H$")
right.set_yscale("symlog", linthresh=0.1)
right.set_xlabel("time $x_4$ (units of $1/H$)")
right.set_ylabel("size (units of $H$)")
right.set_title("Against time, $b_0 = 0$")
right.legend(fontsize=8);
save_figure(fig, "boost_size",
            "The size $\\sqrt{\\mathrm{tr}(M^TM)/16}$ of the term $M = "
            ...
            "every one of these frames.")
```

The right panel draws the size against the time from 0 to 0.5 for four rapidity rates (`{bv:g}` prints a number without unnecessary zeros, so `6.0` becomes `6`). The vertical axis is **symmetric logarithmic** (`"symlog"`): linear between $-0.1$ and $0.1$ and logarithmic outside, so that the curve at exactly 0 can be drawn together with the growing ones. The figure is Figure 08c.3. Output: one PASS line and the figure line.

**What Figure 08c.3 shows.** Left: the size of $\gamma'^\mu\Omega'_\mu$ (units of $H$) against the rapidity rate $\beta$ (units of $H$) at $x_4 = 0$: a V-shaped line, $|6H - \beta|/2$, from 3 at $\beta = 0$ (the diagonal frame, black dot) down to 0 at $\beta = 6H$ (black dot) and up again. Right: the size against the time $x_4$ (units of $1/H$) for $\beta = 0, 3H, 6H, 9H$: constant 3 for the diagonal frame, growing for $\beta = 3H$ and $9H$ (the factor $\sqrt{\cosh 2b}$ of Exercise 5 in Section 8.39), and zero at all times for $\beta = 6H$. The student should see that the same metric and the same field equation give, in different frames, terms of every size including zero.

**In [10], the term as colour maps.**

```python
maps = [("diagonal frame", term(0.0, 0.3, 0.0)),
        ("boosted, $\\beta = 3H$", term(3.0, 0.3, 0.0)),
        ("boosted, $\\beta = 6H$", term(6.0, 0.3, 0.0))]
fig, panels = plt.subplots(1, 3, figsize=(11.0, 3.9))
```

Three (title, matrix) pairs at $x_4 = 0.3$, $b_0 = 0$, and a figure with three panels.

```python
for panel, (title, matrix) in zip(panels, maps):
    image = panel.imshow(np.array(matrix, dtype=float), cmap="RdBu_r", vmin=-3.5,
                         vmax=3.5)
    panel.set_title(title, fontsize=10)
    panel.set_xticks([0, 5, 10, 15])
    panel.set_yticks([0, 5, 10, 15])
    panel.set_xlabel("column")
    panel.grid(False)  # no grid lines over the coloured squares
panels[0].set_ylabel("row")
fig.colorbar(image, ax=list(panels), shrink=0.8, label="entry (units of $H$)")
save_figure(fig, "heat_maps",
            "The $16 \\times 16$ matrix $\\gamma^\\mu\\Omega_\\mu$ of the field "
            ...
            "matrix. Same metric, same field equation, different frames.")
```

`imshow` draws a matrix as a grid of coloured squares; the colour map `"RdBu_r"` runs from blue (negative) through white (zero) to red (positive), on the same scale $-3.5$ to $3.5$ in all three panels (`vmin`, `vmax`). The ticks mark rows and columns 0, 5, 10, 15. One colour bar serves all three panels. The figure is Figure 08c.4; the cell prints only the figure line.

**What Figure 08c.4 shows.** Three $16 \times 16$ colour maps (rows and columns numbered from 0; entries in units of $H$). Left, the diagonal frame: $3H\gamma^{(8)}$, sixteen red squares of value 3, in rows 0 to 7 at columns 8 to 15 and in rows 8 to 15 at columns 0 to 7, along two diagonal lines ($\gamma^{(8)}$ has the entries 1 at the places (row, column) = $(k, k + 8)$ and $(k + 8, k)$, $k = 0, \dots, 7$, and no others). Middle, the frame boosted with $\beta = 3H$ at $b = 0.9$: $\frac{3H}{2}(\cosh b\,\gamma^{(8)} - \sinh b\,\gamma^{(4)})$, more nonzero entries of both signs. Right, $\beta = 6H$: a white square, the zero matrix. The student should see one metric and one field equation producing three different matrices in three frames.

**In [11], the spinor curvature in two frames.**

```python
def spinor_curvature(fr):
    """F_x1x8 = d_1 Omega_8 - d_8 Omega_1 + [Omega_1, Omega_8]."""
    O1, O8 = fr["Omega"][0], fr["Omega"][7]
    return sp.diff(O8, x[0]) - sp.diff(O1, x[7]) + O1 * O8 - O8 * O1
```

`spinor_curvature` computes the curvature component $F_{x_1x_8} = \partial_1\Omega_8 - \partial_8\Omega_1 + [\Omega_1, \Omega_8]$ of a frame.

```python
def riemann_side(fr):
    """(1/4) sum R_rho,sigma,x1,x8 gamma^rho gamma^sigma in the frame fr."""
    result = sp.zeros(16, 16)
    for rho in range(8):
        for sigma in range(8):
            value = g[rho] * riemann(rho, sigma, 0, 7)  # lower the first index
            if value != 0:
                result += value * fr["gamma"][rho] * fr["gamma"][sigma] / 4
    return result
```

`riemann_side` computes the other side of the identity of Section 8.10, $\frac14\sum_{\rho,\sigma}R_{\rho\sigma x_1x_8}\gamma^\rho\gamma^\sigma$ with the coordinate gammas of the given frame; for a diagonal metric, lowering the first index multiplies by $g_{\rho\rho}$.

```python
P14, P18 = G[0] * G[3], G[0] * G[7]  # gamma^(1) gamma^(4) and gamma^(1) gamma^(8)


def two_coefficients(F):
    """c14, c18 with F = c14 P14 + c18 P18 (P14^2 = 1, P18^2 = -1), and whether
    nothing else is left."""
    c14 = sp.simplify((P14 * F).trace() / 16)
    c18 = sp.simplify(-(P18 * F).trace() / 16)
    return c14, c18, all(is_zero(v) for v in F - c14 * P14 - c18 * P18)
```

`P14` and `P18` are the products $\gamma^{(1)}\gamma^{(4)}$ and $\gamma^{(1)}\gamma^{(8)}$. Their squares are $+I_{16}$ and $-I_{16}$ ($\gamma^{(1)}\gamma^{(4)}\gamma^{(1)}\gamma^{(4)} = -(\gamma^{(1)})^2(\gamma^{(4)})^2 = -(1)(-1) = 1$, and $\gamma^{(1)}\gamma^{(8)}\gamma^{(1)}\gamma^{(8)} = -(\gamma^{(1)})^2(\gamma^{(8)})^2 = -1$), and the trace of their product is zero, so the two coefficients are found by traces exactly as in In [6]; the third returned value says whether $F$ is exactly $c_{14}P_{14} + c_{18}P_{18}$.

```python
zero_frame = {"Omega": [M.subs(at_6H) for M in boosted["Omega"]],  # beta = 6H
              "gamma": [M.subs(at_6H) for M in boosted["gamma"]]}
F_diagonal = spinor_curvature(diagonal)
F_zero = spinor_curvature(zero_frame)
check_record(all(is_zero(v) for v in F_diagonal - riemann_side(diagonal)),
             "diagonal frame: F_x1x8 = (1/4) R_rho,sigma,x1,x8 gamma^rho gamma^sigma",
             THEORY, "spinor_curvature_equals_riemann",
             "= (1/4) R_{rho sigma mu nu} gamma^rho gamma^sigma")
check(all(is_zero(v) for v in F_zero - riemann_side(zero_frame)),
      "boosted frame (beta = 6H): F'_x1x8 = (1/4) R gamma'^rho gamma'^sigma")
```

`zero_frame` is the boosted frame at $\beta = 6H$, the frame in which $\gamma'^\mu\Omega'_\mu = 0$ (only its connection and gammas are needed). The two curvatures are computed, and the identity $F = \frac14 R\gamma\gamma$ is checked in both frames; the first check also requires the record's check `spinor_curvature_equals_riemann`.

```python
c14, c18, only_two = two_coefficients(F_diagonal)
c14_b, c18_b, only_two_b = two_coefficients(F_zero)
say(f"diagonal frame: c14 = {c14}")
say(f"diagonal frame: c18 = {c18}")
say(f"boosted frame:  c14 = {c14_b}")
say(f"boosted frame:  c18 = {c18_b}")
check(only_two and only_two_b,
      "in both frames F_x1x8 = c14 gamma^(1) gamma^(4) + c18 gamma^(1) gamma^(8)")
```

The four coefficients are printed in sympy's notation. In the diagonal frame they are $c_{14} = -Ha_4'e^{a_4}\cos z/(2\sin^{5/6}z)$ and $c_{18} = -H^2e^{a_4}\cos z/(2\sin^{5/6}z)$, the values quoted in Section 8.10; in the boosted frame they contain $\cosh(6Hx_4 + b_0)$ and $\sinh(6Hx_4 + b_0)$. The check confirms that nothing else is left in either frame.

```python
kappa_F = H**2 * (a4_prime**2 - H**2) * sp.exp(2 * a4) * sp.cos(z) ** 2 \
    / (4 * sp.sin(z) ** sp.Rational(5, 3))
check(is_zero(c14**2 - c18**2 - kappa_F) and is_zero(c14_b**2 - c18_b**2 - kappa_F),
      "F^2 = F'^2 = H^2 (a4'^2 - H^2) e^(2 a4) cos^2 z / (4 sin^(5/3) z) I16 in "
      "both frames")
```

`kappa_F` is the number $H^2((a_4')^2 - H^2)e^{2a_4}\cos^2 z/(4\sin^{5/3}z)$ of Section 8.10, and the check confirms that $c_{14}^2 - c_{18}^2$ equals it in both frames: the square of the curvature is the same in both frames.

```python
entries_nonzero = sum(1 for v in F_zero if not is_zero(v))
report("nonzero entries of F'_x1x8 in the frame with gamma'^mu Omega'_mu = 0",
       entries_nonzero)
check_record(entries_nonzero > 0, "beta = 6H: the spinor curvature F'_x1x8 is not "
             "zero", "Revision/theory/reports/python-scope.json",
             "boosted_frame_curvature_nonzero",
             "F'_x1x8 = d_x1 Omega'_x8 - d_x8 Omega'_x1 + [Omega'_x1, Omega'_x8] is "
             "nonzero")
```

The number of nonzero entries of $F'_{x_1x_8}$ in the frame where the term vanishes is counted and printed: 32. The last check of the cell requires at least one, together with the record's check `boosted_frame_curvature_nonzero`. The cell prints five PASS lines (two with `reproduces` lines), the four coefficients and the RESULT line.

**In [12], the curvature as colour maps.**

```python
def at_point(matrix):
    """The numbers of a symbolic matrix at H = 1, a4 = x4, z = pi/4, x4 = 0.5."""
    concrete = matrix.replace(sp.Function("a4"), history).doit()
    concrete = concrete.subs({H: 1, x[7]: sp.pi / 24, x[3]: sp.Rational(1, 2), b0: 0})
    return np.array(concrete.evalf(), dtype=float)
```

`at_point` puts the history, $H = 1$, $z = \pi/4$, $x_4 = \frac12$ and $b_0 = 0$ into a symbolic matrix, evaluates it as decimal numbers (`evalf`) and returns a numpy array.

```python
F_numbers = [("diagonal frame: $F_{x_1x_8}$", at_point(F_diagonal)),
             ("boosted, $\\beta = 6H$: $F'_{x_1x_8}$", at_point(F_zero))]
report("largest entry of F_x1x8 at the point (diagonal, boosted)",
       ", ".join(f"{np.abs(matrix).max():.6f}" for _, matrix in F_numbers))
ranks = [int(np.linalg.matrix_rank(matrix)) for _, matrix in F_numbers]
squares = [np.abs(matrix @ matrix).max() for _, matrix in F_numbers]
report("rank of F_x1x8 at the point (diagonal, boosted)", ranks)
```

The two curvature matrices at the point. The first RESULT line prints the largest entry of each (`:.6f` prints six decimals): 0.778093 and 0.038739. `ranks` holds their ranks and `squares` the largest entry of each square $F^2$; the second RESULT line prints the ranks, `[8, 8]`.

```python
check(ranks == [8, 8] and max(squares) < 1e-14 and
      np.allclose(F_numbers[1][1], np.exp(-3.0) * F_numbers[0][1], atol=1e-14),
      "a4 = x4: F and F' have rank 8 and square 0, and F' = e^(-3) F at x4 = 0.5")
```

On this history $a_4' = H$, so $c_{14}^2 - c_{18}^2 = 0$ and $F^2 = 0$: the check requires rank 8 for both, squares below $10^{-14}$ (rounding), and $F' = e^{-3}F$ entry by entry ($b = 6Hx_4 = 3$; `np.allclose` compares two arrays within the tolerance `atol`). Indeed $0.778093\cdot e^{-3} = 0.038739$.

```python
fig, panels = plt.subplots(1, 2, figsize=(10.0, 4.2))
for panel, (title, matrix) in zip(panels, F_numbers):
    largest = np.abs(matrix).max()  # each panel has its own colour scale
    image = panel.imshow(matrix, cmap="RdBu_r", vmin=-largest, vmax=largest)
    fig.colorbar(image, ax=panel, shrink=0.85, label="entry (units of $H^2$)")
    panel.set_title(title, fontsize=10)
    panel.set_xticks([0, 5, 10, 15])
    panel.set_yticks([0, 5, 10, 15])
    panel.set_xlabel("column")
    panel.grid(False)  # no grid lines over the coloured squares
panels[0].set_ylabel("row")
save_figure(fig, "curvature_maps",
            "The spinor curvature $F_{x_1x_8} = \\partial_1\\Omega_8 - "
            ...
            "vanish. On this history both matrices have rank 8 and square zero.")
```

Two colour maps, each with its own symmetric colour scale from minus to plus its largest entry and its own colour bar. The figure is Figure 08c.5. Output: two RESULT lines, one PASS line, the figure line.

**What Figure 08c.5 shows.** Two $16 \times 16$ colour maps of the curvature $F_{x_1x_8}$ (entries in units of $H^2$) at $H = 1$, $z = \pi/4$, $x_4 = 0.5$ on the history $a_4 = x_4$. Left: the diagonal frame, entries up to 0.778. Right: the frame boosted with $\beta = 6H$, where the term of the field equation is zero; the pattern is the same and the entries are $e^{-3}$ times smaller (up to 0.0387; the colour scales differ). The student should see that the curvature is not zero in the frame in which the term vanishes: no frame can make the spin connection vanish.

**In [13], the connection in the energy-momentum tensor.**

```python
g4_up, Omega_1 = diagonal["gamma"][3], diagonal["Omega"][0]
connection_part = (g4_up * Omega_1 + Omega_1 * g4_up) / 2
target = sp.exp(a4) * sixth * H * G[3] * G[0] * G[7] / 2
check_record(all(is_zero(v) for v in connection_part - target)
             and C * G[3] * G[0] * G[7] != sp.zeros(16, 16),
             "(1/2){gamma^x4, Omega_x1} = (1/2) e^a4 sin^(1/6) z H gamma^(4) "
             "gamma^(1) gamma^(8), and C gamma^(4) gamma^(1) gamma^(8) != 0",
             "Revision/theory/reports/python-scope.json",
             "spin_connection_in_the_energy_momentum_tensor",
             "(1/2) e^a4 sin^(1/6) z H Phibar gamma^(x4) gamma^(x1) gamma^(x8) Phi",
             "C gamma^(x4) gamma^(x1) gamma^(x8) != 0")
```

`connection_part` is $\frac12\{\gamma^{x_4}, \Omega_{x_1}\}$ in the diagonal frame, `target` the result of Section 8.11. The check compares them entry by entry, requires the bilinear matrix $C\gamma^{(4)}\gamma^{(1)}\gamma^{(8)}$ to be nonzero (`!=` means "is not equal to"), and requires the record's check with its two texts. Output: one PASS line with its `reproduces` line.

**In [14], the last check.**

```python
for name in ("08c_1_cancel_and_survive.png", "08c_2_pieces_along_history.png",
             "08c_3_boost_size.png", "08c_4_heat_maps.png", "08c_5_curvature_maps.png"):
    check(output_file(f"{FIGURE_FOLDER}/{name}").is_file(),
          f"the figure file {name} exists")
all_checks_passed()
```

The loop checks that each of the five figure files exists, and the last line prints the count. The checks come from the cells as follows: two in In [2], one in In [3], two in In [4], one in In [5], six in In [6], three in In [7], four in In [8], one in In [9], five in In [11], one each in In [12] and In [13], and five here; together 32, and the last line reads `ALL 32 CHECKS PASSED (notebook 08c)`.

### 8.16 Well-posedness: what a good evolution equation must do

**The initial-value problem.** A field equation that contains the time derivative $\partial_4\Psi$ is used like this: one gives the field on the slice $x_4 = 0$ (a seven-dimensional set with the coordinates $x_1, x_2, x_3, x_5, x_6, x_7, x_8$), the **data**, and asks for the field at later times. This is the **initial-value problem**, also called the **Cauchy problem**. The French mathematician Jacques Hadamard called such a problem **well posed** if three things hold: a solution exists; it is unique; and it depends **continuously** on the data, which means: for every later time and every tolerance, data that are close enough to each other give solutions that stay within that tolerance of each other up to that time. "Close" is measured by a **norm**, a number that measures the size of a function (for example its largest value, or the square root of the integral of its square). The third condition is what makes an equation useful for prediction: data are never known exactly, and an equation in which an arbitrarily small error of the data can produce an arbitrarily large error of the solution predicts nothing.

**A toy example with two time directions.** Take a function $\varphi(x_4, x_5)$ of the time $x_4$ and of one extra time $x_5$, and the equation

$$
\partial_4^2\varphi = -\partial_5^2\varphi .
$$

Compare it with the ordinary wave equation $\partial_4^2\varphi = +\partial_1^2\varphi$ along a space direction: the only difference is the minus sign, which appears because $x_5$ is time-like like $x_4$ (we show below that the field equation of this book has exactly this sign). The function $\varphi = \epsilon\cosh(Kx_4)\cos(Kx_5)$, with any numbers $\epsilon > 0$ and $K > 0$, solves it. Line by line:

$$
\begin{aligned}
\partial_4^2\varphi &= \epsilon K^2\cosh(Kx_4)\cos(Kx_5) = K^2\varphi, \\
\partial_5^2\varphi &= -\epsilon K^2\cosh(Kx_4)\cos(Kx_5) = -K^2\varphi, \\
-\partial_5^2\varphi &= K^2\varphi = \partial_4^2\varphi .
\end{aligned}
$$

The first line differentiates twice with respect to $x_4$ ($\frac{d}{dx}\cosh(Kx) = K\sinh(Kx)$ and $\frac{d}{dx}\sinh(Kx) = K\cosh(Kx)$); the second twice with respect to $x_5$ ($\frac{d^2}{dx^2}\cos(Kx) = -K^2\cos(Kx)$); the third compares. Its data are $\varphi(0, x_5) = \epsilon\cos(Kx_5)$ and $\partial_4\varphi(0, x_5) = 0$ (because $\cosh 0 = 1$ and $\sinh 0 = 0$): their largest value is $\epsilon$, as small as we like. At the time $x_4 = 1$ the largest value of the solution is $\epsilon\cosh K$. The ratio, $\cosh K$, grows without bound as $K$ grows ($\cosh 10 = 11013.2$, $\cosh 20 = 2.43 \times 10^8$). So however small we require the data to be, some data of that size produce a solution larger than any given number after one unit of time: the solution does not depend continuously on the data, and the problem is not well posed. For the ordinary wave equation the same data give $\epsilon\cos(Kx_4)\cos(Kx_1)$, which never exceeds $\epsilon$.

**The same sign in our field equation.** In flat 4+4 space (all frame factors equal to 1, no gravitational term, $U = 0$) the field equation is $\sum_a\gamma^{(a)}\partial_a\Psi = m\Psi$. Applying the operator twice, line by line:

$$
\begin{aligned}
\Big(\sum_a\gamma^{(a)}\partial_a\Big)\Big(\sum_b\gamma^{(b)}\partial_b\Big)\Psi &= \sum_{a,b}\gamma^{(a)}\gamma^{(b)}\partial_a\partial_b\Psi \\
&= \sum_a(\gamma^{(a)})^2\partial_a^2\Psi + \sum_{a<b}\big(\gamma^{(a)}\gamma^{(b)} + \gamma^{(b)}\gamma^{(a)}\big)\partial_a\partial_b\Psi \\
&= \big(\partial_1^2 + \partial_2^2 + \partial_3^2 + \partial_8^2 - \partial_4^2 - \partial_5^2 - \partial_6^2 - \partial_7^2\big)\Psi .
\end{aligned}
$$

The first line multiplies out (the gammas are constant matrices); the second separates the terms with $a = b$ from the pairs $a \neq b$, using $\partial_a\partial_b = \partial_b\partial_a$; the third uses $(\gamma^{(a)})^2 = \eta_{aa}I_{16}$ and the anticommutation of different gammas. On the other side, applying the operator to $m\Psi$ gives $m\sum_a\gamma^{(a)}\partial_a\Psi = m^2\Psi$. Solving for the second time derivative:

$$
\partial_4^2\Psi = \big(\partial_1^2 + \partial_2^2 + \partial_3^2 + \partial_8^2 - \partial_5^2 - \partial_6^2 - \partial_7^2 - m^2\big)\Psi .
$$

The three extra-time derivatives enter with the sign of the toy example. This is the root of everything that follows.

**Non-characteristic slices.** In the author's metric the field equation of Section 8.2 can be solved for $\partial_4\Psi$. Write it as $\gamma^{(4)}\partial_4\Psi + R = V\Psi$, where $R$ holds all the other terms on the left and $V = m + U'(S)$. Multiplying from the left by $\gamma^{(4)}$ and using $(\gamma^{(4)})^2 = -I_{16}$ gives $-\partial_4\Psi + \gamma^{(4)}R = \gamma^{(4)}V\Psi$, so

$$
\partial_4\Psi = -\gamma^{(4)}\Big[V\Psi - \sum_{a\neq 4}\frac{1}{f_a}\gamma^{(a)}\partial_a\Psi - 3H\gamma^{(8)}\Psi\Big]
$$

(PROVED; `Revision/theory/reports/wolfram-field-theory.json`, check `evolution_form_G`). A slice is called **non-characteristic** when the matrix in front of the time derivative is invertible, as here: the equation then tells how the field changes in time from its values on the slice. This is necessary for a good evolution equation, but not sufficient: the toy example can be solved for $\partial_4^2\varphi$ too. Sections 8.17 and 8.18 show that the field equation fails the third condition of Hadamard: exactly in flat 4+4 space and with frozen coefficients, and, through a standard theorem quoted without proof, in the author's metric itself (Section 8.18 states each status).

### 8.17 Plane waves with frozen coefficients and the mode matrix

**Frozen coefficients.** In the author's metric the frame factors $1/f_a$ change from point to point and in time. Near one point and for a short time one may replace them by their values at that point; this is the method of **frozen coefficients**, a device for studying an equation near one point (labelled MODEL in the notebooks, ASSUMED in the five-label scheme). It does not say that the extra times stop deflating: in the author's metric they always deflate, and Section 8.24 follows a wave along the deflating history. In flat 4+4 space the coefficients are constant and nothing is frozen. With frozen coefficients the factors are absorbed into the **frame momenta** $k_a$, and the term $3H\gamma^{(8)}$ is left out; it is absent exactly in the field variables $\chi$ of Section 8.30.

**Plane waves.** A **plane wave** is a field $\Psi = u\,e^{i(k_1x_1 + k_2x_2 + k_3x_3 + k_5x_5 + k_6x_6 + k_7x_7 + k_8x_8) - iEx_4}$ with a constant column $u$ of 16 complex numbers. The number $k_a$ is the **momentum** (or wave number) along $x_a$: radians of phase per unit length; $E$ is the **frequency**. Inserting it into $\sum_a\gamma^{(a)}\partial_a\Psi = m\Psi$, line by line:

1. $\gamma^{(4)}(-iE)u + \sum_{a\neq4}ik_a\gamma^{(a)}u = mu$, because $\partial_4$ of the exponential gives the factor $-iE$ and $\partial_a$ gives $ik_a$ (the common exponential is divided out).
2. Multiply from the left by $\gamma^{(4)}$ and use $(\gamma^{(4)})^2 = -I_{16}$: $iEu + i\sum_{a\neq4}k_a\gamma^{(4)}\gamma^{(a)}u = m\gamma^{(4)}u$.
3. Multiply by $-i$ (and $(-i)(i) = 1$) and solve for $Eu$: $Eu = h_ku$ with the **mode matrix**

$$
h_k = -im\gamma^{(4)} - \gamma^{(4)}\sum_{a\neq4}k_a\gamma^{(a)} .
$$

So $E$ is an **eigenvalue** of $h_k$ and $u$ an **eigenvector**: $h_ku = Eu$ with $u \neq 0$. The set of all eigenvectors of one eigenvalue (with the zero column) is its **eigenspace**, and the number of independent ones is its **dimension**.

**The square of the mode matrix.** Write $K = \sum_{a\neq4}k_a\gamma^{(a)}$, so that $h_k = -\gamma^{(4)}(im + K)$. Since $\gamma^{(4)}$ anticommutes with every $\gamma^{(a)}$ in $K$, $K\gamma^{(4)} = -\gamma^{(4)}K$ and therefore $(im + K)\gamma^{(4)} = \gamma^{(4)}(im - K)$. Line by line:

$$
\begin{aligned}
h_k^2 &= \gamma^{(4)}(im + K)\gamma^{(4)}(im + K) = \gamma^{(4)}\gamma^{(4)}(im - K)(im + K) \\
&= -\big((im)^2 + imK - imK - K^2\big) = m^2 + K^2, \\
K^2 &= \sum_{a\neq4}k_a^2(\gamma^{(a)})^2 + \sum_{a<b}k_ak_b\big(\gamma^{(a)}\gamma^{(b)} + \gamma^{(b)}\gamma^{(a)}\big) = \big(k_1^2 + k_2^2 + k_3^2 + k_8^2 - k_5^2 - k_6^2 - k_7^2\big)I_{16} .
\end{aligned}
$$

The first line uses $(-1)^2 = 1$ and moves $(im + K)$ past $\gamma^{(4)}$; the second uses $(\gamma^{(4)})^2 = -I_{16}$ and multiplies out (the number $im$ commutes with $K$); the third line computes $K^2$ as in Section 8.16. Hence

$$
h_k^2 = E^2\,I_{16}, \qquad E^2 = m^2 + k_1^2 + k_2^2 + k_3^2 + k_8^2 - k_5^2 - k_6^2 - k_7^2
$$

(PROVED; `Revision/theory/reports/python-scope.json` and `wolfram-scope.json`, check `extra_time_growth_rates_unbounded`). The extra-time momenta enter with a MINUS sign, because the extra times are time-like. Every eigenvalue $\lambda$ of $h_k$ obeys $\lambda^2 = E^2$ (apply $h_k^2 = E^2$ to an eigenvector), so the eigenvalues are $+E$ and $-E$. The **trace** of $h_k$ (the sum of its diagonal entries, which is also the sum of its eigenvalues, each counted as often as it occurs) is zero, because the trace of $\gamma^{(4)}$ and of each product of two different gammas is zero. With $n_+$ eigenvalues $+E$ and $n_-$ eigenvalues $-E$, $n_+ + n_- = 16$ and $n_+E - n_-E = 0$; for $E \neq 0$ this gives $n_+ = n_- = 8$.

**When is the mode matrix Hermitian?** A matrix is **Hermitian** if it equals its conjugate transpose, $M^\dagger = M$, and **anti-Hermitian** if $M^\dagger = -M$. A Hermitian matrix has only real eigenvalues. The gammas are real with $(\gamma^{(a)})^T = \eta_{aa}\gamma^{(a)}$. So $(-i\gamma^{(4)})^\dagger = i(\gamma^{(4)})^T = -i\gamma^{(4)}$: the mass term is Hermitian. For $a \neq 4$, $(\gamma^{(4)}\gamma^{(a)})^T = (\gamma^{(a)})^T(\gamma^{(4)})^T = \eta_{aa}\gamma^{(a)}(-\gamma^{(4)}) = \eta_{aa}\gamma^{(4)}\gamma^{(a)}$ (the last step anticommutes the two gammas). For a space-like direction ($\eta_{aa} = +1$) the real matrix $\gamma^{(4)}\gamma^{(a)}$ is symmetric, hence Hermitian; for an extra time ($\eta_{aa} = -1$) it is antisymmetric, hence anti-Hermitian. So the anti-Hermitian part of $h_k$ is exactly its extra-time part, $-\gamma^{(4)}(k_5\gamma^{(5)} + k_6\gamma^{(6)} + k_7\gamma^{(7)})$, and $h_k$ is Hermitian exactly when $k_5 = k_6 = k_7 = 0$. Fields that do not depend on the extra times are called the **good sector**. In the good sector every frequency is real, and $h_k$ commutes with $B$ (PROVED; `python-field-theory.json`, check `good_sector_spectrum_and_B_sectors`).

**An exact example.** Take $m = 1$, $k_5 = 2$ and all other momenta 0. Then $E^2 = 1 - 4 = -3$, and the eigenvalues are $E = \pm i\sqrt3$, eight each (PROVED; `python-field-theory.json`, check `extra_time_modes_grow`, whose detail lists the eigenvalues `-sqrt(3)*I` and `sqrt(3)*I`).

### 8.18 Growth without bound: the Cauchy problem is not well posed

**Growth.** When $E^2 < 0$, the frequencies are $E = \pm i\kappa$ with the **growth rate** $\kappa = \sqrt{-E^2} > 0$. A wave $u\,e^{-iEx_4}$ with $E = i\kappa$ behaves in time like $e^{-i(i\kappa)x_4} = e^{\kappa x_4}$: it grows exponentially (and the one with $E = -i\kappa$ decays). In the example above, $\kappa = \sqrt3$. With an extra-time momentum $k_5 = K$ and a space momentum $k_1$ (all others 0), $E^2 = m^2 + k_1^2 - K^2$, and the waves grow as soon as $K^2 > m^2 + k_1^2$, with

$$
\kappa = \sqrt{K^2 - m^2 - k_1^2} .
$$

**No upper bound.** Write $c^2 = m^2 + k_1^2$ with $c \ge 0$. For $K \ge c$ the rate satisfies $\kappa \ge K - c$: both sides are not negative, and squaring, $(K - c)^2 = K^2 - 2Kc + c^2 \le K^2 - c^2 = \kappa^2$ is the same as $2c^2 \le 2Kc$, which holds because $c \le K$. So $\kappa$ grows at least like $K$, without bound: for every rate, however large, some extra-time waves grow faster (PROVED; `python-scope.json`, check `extra_time_growth_rates_unbounded`, both engines; Notebook 08a prints $\kappa = 999.9995$ for $m = 1$, $K = 1000$).

**The solution in time.** The equation in time of a plane wave is $i\,du/dx_4 = h_ku$, solved by $u(x_4) = e^{-ih_kx_4}u(0)$, where the **matrix exponential** is the series $e^{A} = I + A + A^2/2! + A^3/3! + \dots$. Because $h_k^2 = E^2I_{16}$, every even power is $h_k^{2j} = E^{2j}I_{16}$ and every odd power $h_k^{2j+1} = E^{2j}h_k$. Sorting the series:

$$
\begin{aligned}
e^{-ih_kx_4} &= \sum_{j\ge0}\frac{(-i)^{2j}E^{2j}x_4^{2j}}{(2j)!}I_{16} + \sum_{j\ge0}\frac{(-i)^{2j+1}E^{2j}x_4^{2j+1}}{(2j+1)!}h_k \\
&= \sum_{j\ge0}\frac{(-1)^j(Ex_4)^{2j}}{(2j)!}I_{16} - \frac{i}{E}\sum_{j\ge0}\frac{(-1)^j(Ex_4)^{2j+1}}{(2j+1)!}h_k \\
&= \cos(Ex_4)\,I_{16} - i\,\frac{\sin(Ex_4)}{E}\,h_k .
\end{aligned}
$$

The first line separates even and odd powers; the second uses $(-i)^{2j} = (-1)^j$ and $(-i)^{2j+1} = -i(-1)^j$ and takes $1/E$ out of the odd sum; the third recognises the series of the cosine and of the sine. For $E = i\kappa$ this is $\cosh(\kappa x_4)I_{16} - i\frac{\sinh(\kappa x_4)}{\kappa}h_k$ (because $\cos(i\theta) = \cosh\theta$ and $\sin(i\theta)/i = \sinh\theta$), and for $E = 0$ it is the limit $I_{16} - ih_kx_4$.

**Hadamard's third condition fails.** Take as data at $x_4 = 0$ one growing wave, $\epsilon\,e^{iKx_5}u_+$, where $u_+$ is an eigenvector of $h_k$ (with $k_5 = K$) for the eigenvalue $+i\kappa$, of size $u_+^\dagger u_+ = 1$. At the time $x_4$ the solution is $\epsilon\,e^{\kappa x_4}e^{iKx_5}u_+$. To measure the data we may even use a norm that punishes wiggly data: the **Sobolev norm of order $s$** counts, for one wave of momentum $K$ and amplitude $\epsilon$, the size $\epsilon(1 + K^2)^{s/2}$ (each order of derivative brings a factor of about $K$). The ratio of the size of the solution at $x_4 = 1$ to the size of the data is then

$$
\frac{\epsilon\,e^{\kappa}}{\epsilon(1 + K^2)^{s/2}} = e^{\kappa}(1 + K^2)^{-s/2}, \qquad \ln(\text{ratio}) = \kappa - \tfrac{s}{2}\ln(1 + K^2) \ge K - c - \tfrac{s}{2}\ln(1 + K^2),
$$

the same for every $\epsilon$. The right-hand side grows without bound as $K$ grows, because the logarithm grows more slowly than any multiple of $K$. So for every order $s$ data as small as we like give, after one unit of time, solutions as large as we like: the solution does not depend continuously on the data. So, in flat 4+4 space and with frozen coefficients, the initial-value problem is NOT well posed in the sense of Hadamard for data that depend on the extra times, although the slices $x_4 = $ const are non-characteristic (PROVED in this setting; `python-scope.json`, check `extra_time_growth_rates_unbounded`, both engines, whose detail names exactly this setting: "flat 4+4 space (or frozen coefficients)"). With $m = 1$ the ratio first exceeds $10^6$ at $K = 13.9$ for $s = 0$, at $K = 19.9$ for $s = 2$, at $K = 27.1$ for $s = 4$ and at $K = 44.2$ for $s = 8$ (COMPUTED by Notebook 08a on a grid of step 0.1): a stronger norm only delays the rise.

**From frozen coefficients to the author's metric (an ASSUMED step).** In the author's metric the frame factors change from point to point, and a plane wave is not an exact solution of the field equation; so the argument above, by itself, proves nothing about the field equation in that metric. The step is made by a standard theorem of the theory of partial differential equations, the **Lax-Mizohata theorem** (P. D. Lax, 1957; S. Mizohata, 1961), which this book quotes without proof, so it is ASSUMED here. It says: if the initial-value problem of a linear system of first-order equations with smooth coefficients is well posed near a point, then at that point the frequencies of its **principal part** (the derivative terms alone, with their coefficients taken at that point) are real for every real momentum. For the field equation with $U = 0$ (then the equation is linear) the principal part at a point is the mode matrix of Section 8.17 without the mass term, with the frame momenta of that point: a wave with the coordinate momentum $q_a$ along $x_a$ has there the frame momentum $k_a = q_a/f_a$, with the frame factors of that point (the term $3H\gamma^{(8)}$ contains no derivative, so it does not belong to the principal part). By the formula of Section 8.17 with $m = 0$, its frequencies obey $E^2 = k_1^2 + k_2^2 + k_3^2 + k_8^2 - k_5^2 - k_6^2 - k_7^2$, which is negative for a wave along an extra time alone ($k_5 \neq 0$, all other momenta zero), at every point. So, granted the theorem, the initial-value problem of the field equation in the author's metric is not well posed for data that depend on the extra times. Status: the statements in flat 4+4 space and with frozen coefficients are PROVED, and they are what the Revision record checks; the step to the author's varying coefficients rests on the quoted theorem (ASSUMED) and is not checked by the record; for $U \neq 0$ nothing more is claimed.

### 8.19 The Krein form is conserved; the growing waves carry Krein form zero

**Two ways to measure a column.** The ordinary size of a column $u$ is the **Hilbert norm** $u^\dagger u = |u_1|^2 + \dots + |u_{16}|^2$. The **Krein form** is $u^\dagger Bu$ with the matrix $B = -iC\gamma^{(4)}$ of the record ($B^\dagger = B$, $B^2 = I_{16}$, eight eigenvalues $+1$ and eight $-1$; Chapters 5 and 10). Because $B$ has negative eigenvalues, $u^\dagger Bu$ can be negative or zero for $u \neq 0$. Chapter 10 explains why the canonical quantisation of dirac16complex forces this indefinite form; here we need only one property.

**The Krein form is conserved.** The mode matrix satisfies $Bh_k = h_k^\dagger B$ for every momentum (PROVED; `python-field-theory.json`, check `mode_hamiltonian_B_selfadjoint_dispersion`; a matrix with this property is called **self-adjoint for the Krein form**). For a solution of $du/dx_4 = -ih_ku$, line by line:

$$
\begin{aligned}
\frac{d}{dx_4}\big(u^\dagger Bu\big) &= \Big(\frac{du}{dx_4}\Big)^\dagger Bu + u^\dagger B\frac{du}{dx_4} = (-ih_ku)^\dagger Bu + u^\dagger B(-ih_ku) \\
&= i\,u^\dagger h_k^\dagger Bu - i\,u^\dagger Bh_ku = i\,u^\dagger\big(h_k^\dagger B - Bh_k\big)u = 0 .
\end{aligned}
$$

The first step is the product rule; the second inserts the equation; the third uses $(-ih_ku)^\dagger = u^\dagger h_k^\dagger(-i)^* = i\,u^\dagger h_k^\dagger$; the last uses $Bh_k = h_k^\dagger B$. The Hilbert norm is not conserved: the same computation gives $\frac{d}{dx_4}(u^\dagger u) = i\,u^\dagger(h_k^\dagger - h_k)u$, which is not zero when $h_k$ is not Hermitian, that is when there is extra-time momentum.

**The growing waves carry Krein form zero.** Let $u$ and $v$ be two eigenvectors of $h_k$ for the same growing eigenvalue $i\kappa$. Then $u(x_4) = e^{\kappa x_4}u$ and $v(x_4) = e^{\kappa x_4}v$ solve the equation, and the computation above, done with two different columns, shows that $v(x_4)^\dagger Bu(x_4) = e^{2\kappa x_4}\,v^\dagger Bu$ is constant in time. A constant that equals $e^{2\kappa x_4}$ times a fixed number, with $\kappa > 0$, must be zero: $v^\dagger Bu = 0$. So the Krein form vanishes identically on the eigenspace of a growing frequency: the eigenspace is **Krein-neutral** (PROVED by the argument just given; the pairing record proves the same and checks it on exact samples, `Revision/pairing/reports/python-pairing.json`, check `Q.one_particle_complex_frequency_Krein_neutral`). On an eigenspace of a real frequency $E \neq 0$, by contrast, the Krein form has four positive and four negative directions: its **inertia** is (4,4) (PROVED in the pairing record for every real frequency; `python-pairing.json`, checks `Q.one_particle_Krein_inertia_proof` and, for an exact sample, `Q.one_particle_Krein_inertia`). This is how the Hilbert norm can grow while the Krein form stays constant: the positive and the negative parts of the Krein form grow together and cancel.

### 8.20 Example: growth rates and Hadamard ill-posedness

Notebook 08a puts Sections 8.16 to 8.19 to work. It reads the author's gammas, checks the 64 Clifford relations and $(\gamma^{(4)})^2 = -I_{16}$; builds the mode matrix with symbolic mass and momenta and proves $h_k^2 = E^2I_{16}$ exactly, comparing with both Revision verifiers; finds the anti-Hermitian part; checks the exact example $m = 1$, $k_5 = 2$; computes the growth rate against the extra-time momentum and maps it in the plane of $k_1$ and $k_5$; solves the equation in time in two independent ways (the closed formula and RK4); computes the Hadamard amplification for four Sobolev orders; checks the conservation of the Krein form, the Krein-neutral growing eigenspace and the inertia (4,4) of a real-frequency eigenspace; and follows the eigenvalues into the complex plane. It needs no Rust and runs in well under a minute; the times measured on the build computer, which depend on how busy that computer is, are recorded in the notebook's provenance file `Revision/textbook/notebooks/08a_growth_rates.PROVENANCE.md`. It ends with the line ALL 30 CHECKS PASSED (notebook 08a).

<!-- NOTEBOOK 08a -->

### 8.23 Line-by-line walk-through of Notebook 08a

The notebook has 13 code cells, In [1] to In [13]. As in Section 8.15, each line or small group of lines is quoted and explained, and a line `...` in quoted code stands for the remaining lines of a figure caption, which is printed in full under its figure in Section 8.22.

**In [1], the set-up cell.** It is the set-up cell explained line by line in Section 8.15, with one difference: the line `NOTEBOOK_ID = "08a"  # this notebook: chapter 08, example a`. Its comment lines are the run instructions of Section 8.21. Output: `Set-up of notebook 08a complete: repository folder found, helpers defined.`

**In [2], the record helpers and the author's gamma matrices.**

```python
import numpy as np  # arrays of numbers, matrices, linear algebra
import sympy as sp  # exact algebra with symbols

REPORTS = {}  # report file -> {check name: (verdict, detail)}, each read once
```

The two packages and the empty table of reports, as in Section 8.15.

```python
def record_says(report_file, check_name, *pieces):
    ...
    verdict, detail = REPORTS[report_file][check_name]
    return verdict == "pass" and all(piece in detail for piece in pieces)


def check_record(condition, title, report_file, check_name, *pieces):
    """check() for a result that reproduces the Revision check check_name: it passes
    only if condition is true AND the report records check_name as passed, with
    every piece of text (values computed here) in its detail."""
    on_record = record_says(report_file, check_name, *pieces)
    check(condition and on_record, title,
          record=f"{report_file}, check {check_name}")
```

`record_says` is exactly the function of Notebook 08c (its body, shortened here to `...`, is quoted and explained in Section 8.15). `check_record` is the simpler form of the 08c helper: it takes one check name only. It passes only if the notebook's own condition is true AND the record reports the check as passed with every given piece of text in its detail.

```python
gammas_record = json.loads(
    repository_file("Revision/algebra/gammas.json").read_text(encoding="utf-8"))
# The record stores every matrix as a list of rows of whole numbers.
GAMMA = [np.array(rows, dtype=int) for rows in gammas_record["gamma"]]
ETA = gammas_record["eta"]  # [1, 1, 1, -1, -1, -1, -1, 1] in the order x1 ... x8
# B = -i C gamma^(x4) is stored as its real part and its imaginary part.
B = np.array(gammas_record["B"]["re"]) + 1j * np.array(gammas_record["B"]["im"])
I16 = np.eye(16, dtype=int)  # the 16 x 16 unit matrix
say(f"eta = {ETA}; each gamma is a {GAMMA[0].shape[0]} x {GAMMA[0].shape[1]} matrix")
```

The gammas are read from the record and turned into numpy arrays of whole numbers (`dtype=int`), so that the products below are exact. `ETA` is the list of the eight signs. The matrix $B$ is complex; the record stores its real part (`"re"`) and its imaginary part (`"im"`) separately, and the line adds them, `1j` being Python's imaginary unit $i$. `np.eye(16, dtype=int)` is the unit matrix. The `say` line prints the signs and the shape of a gamma (`.shape` gives the number of rows and columns): `eta = [1, 1, 1, -1, -1, -1, -1, 1]; each gamma is a 16 x 16 matrix`.

```python
clifford_ok = all(
    np.array_equal(GAMMA[a] @ GAMMA[b] + GAMMA[b] @ GAMMA[a],
                   2 * ETA[a] * (a == b) * I16)  # (a == b) is 1 or 0
    for a in range(8) for b in range(8))
check_record(clifford_ok, "the 64 Clifford relations {gamma^a, gamma^b} = 2 eta^ab I16",
             "Revision/algebra/reports/python-algebra.json", "clifford_relation",
             "for all 64 ordered pairs")
```

For all 64 ordered pairs $(a, b)$ the anticommutator $\gamma^{(a)}\gamma^{(b)} + \gamma^{(b)}\gamma^{(a)}$ (`@` is the matrix product) is compared, entry by entry and exactly (`np.array_equal`), with $2\eta_{aa}I_{16}$ when $a = b$ and the zero matrix otherwise: in arithmetic, the truth value `(a == b)` counts as 1 or 0. The check also requires the algebra record's check `clifford_relation`.

```python
check(np.allclose(B, B.conj().T) and np.allclose(B @ B, np.eye(16)),
      "B is Hermitian and B^2 = 1")
# (gamma^(x4))^2 = -1: the field equation can be solved for d4 Psi (multiply it by
# -gamma^(x4)), so the slices x4 = const are non-characteristic.
check_record(np.array_equal(GAMMA[3] @ GAMMA[3], -I16),
             "(gamma^(x4))^2 = -1: the slices x4 = const are non-characteristic",
             "Revision/theory/reports/wolfram-field-theory.json", "evolution_form_G",
             "the slices x4 = const are non-characteristic")
```

`B.conj().T` is the conjugate transpose $B^\dagger$; `np.allclose` compares two arrays up to rounding. The first check confirms $B^\dagger = B$ and $B^2 = I_{16}$. The second confirms $(\gamma^{(4)})^2 = -I_{16}$, which is the reason the field equation can be solved for $\partial_4\Psi$ (Section 8.16), together with the Wolfram record's check `evolution_form_G`. Output: the line about `eta` and three PASS lines, two with `reproduces` lines.

**In [3], the mode matrix and its square, exactly.**

```python
m = sp.Symbol("m", real=True)  # the mass
k = {a: sp.Symbol(f"k{a}", real=True) for a in (1, 2, 3, 5, 6, 7, 8)}  # momenta
G = [sp.Matrix(rows) for rows in gammas_record["gamma"]]  # the gammas, exact
B_exact = sp.I * sp.Matrix(gammas_record["B"]["im"])  # B is purely imaginary
g4 = G[3]  # gamma^(x4)
```

The mass and the seven momenta are exact symbols (a dictionary that maps each direction number $a$ to the symbol $k_a$; there is no $k_4$). `G` holds the gammas as exact sympy matrices. The real part of $B$ is zero (because $C\gamma^{(4)}$ is real), so `B_exact` is $i$ times the stored imaginary part. `g4` is $\gamma^{(4)}$.

```python
momentum_part = sp.zeros(16, 16)
for a, k_a in k.items():  # a runs over 1, 2, 3, 5, 6, 7, 8
    momentum_part += k_a * g4 * G[a - 1]  # k_a gamma^(x4) gamma^(xa)
h = -sp.I * m * g4 - momentum_part  # the mode matrix h_k
E2 = m**2 + k[1]**2 + k[2]**2 + k[3]**2 + k[8]**2 - k[5]**2 - k[6]**2 - k[7]**2
say(f"E^2 = {E2}")
```

`k.items()` gives the pairs (direction, symbol); `G[a - 1]` is the gamma of direction $x_a$ (lists count from 0). The loop adds up $\sum_{a\neq4}k_a\gamma^{(4)}\gamma^{(a)}$, and `h` is the mode matrix $h_k = -im\gamma^{(4)} - \gamma^{(4)}\sum_ak_a\gamma^{(a)}$ of Section 8.17 (`sp.I` is the exact $i$). `E2` is the expected $E^2$; it is printed in sympy's order: `E^2 = k1**2 + k2**2 + k3**2 - k5**2 - k6**2 - k7**2 + k8**2 + m**2`.

```python
square_minus_E2 = (h * h - E2 * sp.eye(16)).applyfunc(sp.expand)
square_ok = square_minus_E2 == sp.zeros(16, 16)
# The two independent Revision verifiers print E^2 in their own notations: sympy
# writes powers with **, the Wolfram verifier with ^. Both texts must hold this E^2.
E2_sympy_text = sp.sstr(E2)  # "k1**2 + k2**2 + ... + m**2"
E2_wolfram_text = E2_sympy_text.replace("**", "^")  # "k1^2 + k2^2 + ... + m^2"
```

The matrix $h_k^2 - E^2I_{16}$ is computed and every entry multiplied out (`sp.expand`); `square_ok` is true when all 256 entries are exactly zero. The two texts are $E^2$ as the sympy record writes it and as the Wolfram record writes it (`replace` swaps `**` for `^`).

```python
check_record(square_ok,
             "h_k^2 = E^2 I16, E^2 = m^2 + k1^2 + k2^2 + k3^2 + k8^2 - k5^2 - k6^2 "
             "- k7^2", "Revision/theory/reports/python-scope.json",
             "extra_time_growth_rates_unbounded", f"h_k^2 = ({E2_sympy_text}) I16")
check_record(square_ok, "the same E^2 in the independent Wolfram verifier",
             "Revision/theory/reports/wolfram-scope.json",
             "extra_time_growth_rates_unbounded", f"h_k^2 = ({E2_wolfram_text}) I16")
check(sp.expand(h.trace()) == 0, "the trace of h_k is 0 (eigenvalues +E, -E, 8 each)")
```

Two checks of the same exact statement against the two independent Revision verifiers, whose details must contain exactly this $E^2$ in their notations; and the check that the trace of $h_k$ is zero, which, with $h_k^2 = E^2$, gives eight eigenvalues $+E$ and eight $-E$ (Section 8.17).

```python
krein = (B_exact * h - h.H * B_exact).applyfunc(sp.expand)  # .H: conjugate transpose
check_record(krein == sp.zeros(16, 16), "B h_k = h_k^dagger B (Krein self-adjoint)",
             "Revision/theory/reports/python-field-theory.json",
             "mode_hamiltonian_B_selfadjoint_dispersion", "B h = h^dagger B")
```

`h.H` is sympy's conjugate transpose $h_k^\dagger$. The check confirms $Bh_k = h_k^\dagger B$ for symbolic mass and momenta, the property that conserves the Krein form (Section 8.19). Output: the line with $E^2$ and four PASS lines, three with `reproduces` lines.

**In [4], when is the mode matrix Hermitian?**

```python
anti = ((h - h.H) / 2).applyfunc(sp.expand)  # the anti-Hermitian part of h_k
extra_time_part = -(k[5] * g4 * G[4] + k[6] * g4 * G[5] + k[7] * g4 * G[6])
check((anti - extra_time_part).applyfunc(sp.expand) == sp.zeros(16, 16),
      "the anti-Hermitian part of h_k is the extra-time part")
anti_square = (anti * anti).applyfunc(sp.expand)
check(anti_square == (-(k[5]**2 + k[6]**2 + k[7]**2) * sp.eye(16)).applyfunc(
    sp.expand), "its square is -(k5^2 + k6^2 + k7^2) I16")
```

Every matrix is the sum of its Hermitian part $(h + h^\dagger)/2$ and its anti-Hermitian part $(h - h^\dagger)/2$. The first check shows that the anti-Hermitian part is exactly the extra-time part $-\gamma^{(4)}(k_5\gamma^{(5)} + k_6\gamma^{(6)} + k_7\gamma^{(7)})$ (Section 8.17). The second shows that its square is $-(k_5^2 + k_6^2 + k_7^2)I_{16}$; a matrix whose square is a negative number times $I_{16}$ is the zero matrix only when that number is zero, so $h_k$ is Hermitian exactly when there is no extra-time momentum. Output: two PASS lines.

**In [5], the exact example $m = 1$, $k_5 = 2$.**

```python
sample = {m: 1, k[5]: 2, k[1]: 0, k[2]: 0, k[3]: 0, k[6]: 0, k[7]: 0, k[8]: 0}
h_sample = h.subs(sample)  # an exact matrix of numbers
check(h_sample * h_sample == -3 * sp.eye(16), "m = 1, k5 = 2: h^2 = -3 I16")
dimension = 16 - (h_sample - sp.I * sp.sqrt(3) * sp.eye(16)).rank()
report("dimension of the eigenspace of +i sqrt(3)", dimension)
```

The substitution puts in $m = 1$, $k_5 = 2$ and zero for the other momenta. The check confirms $h^2 = -3I_{16}$. The dimension of the eigenspace of $+i\sqrt3$ is the number of independent solutions of $(h - i\sqrt3 I)u = 0$, which is 16 minus the rank of that matrix (a standard fact of linear algebra, Chapter 1); sympy computes the rank exactly. RESULT: 8.

```python
eigenvalues = np.linalg.eigvals(np.array(h_sample, dtype=complex))
# Round to 9 digits and count how often each value occurs (sorted, so the printed
# order is always the same).
rounded = sorted({complex(0.0, round(v.imag, 9)) for v in eigenvalues},
                 key=lambda v: v.imag)  # the real parts are zero (checked below)
for value in rounded:
    count = int(np.sum(np.abs(eigenvalues - value) < 1e-6))
    say(f"eigenvalue {value.imag:+.9f} i occurs {count} times")
```

numpy computes the 16 eigenvalues numerically (`np.linalg.eigvals`, on a complex array). The **set** in curly brackets keeps each rounded value once; `sorted(..., key=lambda v: v.imag)` orders them by their imaginary part (a `lambda` is a one-line function). For each distinct value the loop counts how many eigenvalues lie within $10^{-6}$ of it (`np.sum` of true values counts them) and prints, for example, `eigenvalue -1.732050808 i occurs 8 times` (`:+.9f` prints the sign and nine decimals).

```python
# The record lists the exact eigenvalues as sympy writes them, sorted as text:
exact_text = sorted(str(sign * sp.sqrt(3) * sp.I) for sign in (1, -1))
say("exact eigenvalues as sympy writes them: " + ", ".join(exact_text))
check_record(dimension == 8 and np.max(np.abs(eigenvalues.real)) < 1e-9
             and all(abs(abs(v.imag) - 3**0.5) < 1e-9 for v in eigenvalues),
             "m = 1, k5 = 2: eigenvalues +i sqrt(3) and -i sqrt(3), 8 each",
             "Revision/theory/reports/python-field-theory.json",
             "extra_time_modes_grow", f"m = 1, k5 = 2: eigenvalues {exact_text}")
```

`exact_text` is the list of the two exact eigenvalues as sympy writes them, `-sqrt(3)*I` and `sqrt(3)*I`, sorted as texts. The check requires the eigenspace dimension 8, real parts below $10^{-9}$, every imaginary part within $10^{-9}$ of $\pm\sqrt3$, and the record's text that starts with `m = 1, k5 = 2: eigenvalues` followed by this list (the f-string writes the Python list with its square brackets and quotation marks, exactly as the record does). Output: two PASS lines, one RESULT line, the two counted eigenvalues and the exact text.

**In [6], the growth rate against the extra-time momentum.**

```python
def mode_matrix(mass, momenta):
    """h_k = -i m gamma^(x4) - gamma^(x4) sum_a k_a gamma^(xa); momenta: {a: k_a}."""
    g4n = GAMMA[3]
    result = -1j * mass * g4n.astype(complex)
    for a, k_a in momenta.items():
        result = result - k_a * (g4n @ GAMMA[a - 1])
    return result


def growth_rate(mass, K, k1=0.0):
    """kappa = sqrt(K^2 - m^2 - k1^2) where positive, else 0 (numpy arrays too)."""
    return np.sqrt(np.maximum(K**2 - mass**2 - k1**2, 0.0))
```

`mode_matrix` builds the numerical mode matrix for a mass and a dictionary of momenta, for example `{5: 2.0}` for $k_5 = 2$ (`.astype(complex)` makes the integer matrix complex, so that $-i$ can multiply it). `growth_rate` is the formula $\kappa = \sqrt{K^2 - m^2 - k_1^2}$ of Section 8.18 where the bracket is positive, and 0 where it is not (`np.maximum` takes the larger of the bracket and 0, entry by entry, so the function also works on whole arrays of $K$).

```python
K_values = np.linspace(0.0, 6.0, 61)  # extra-time momenta 0, 0.1, ..., 6
numerical = np.array([np.max(np.linalg.eigvals(mode_matrix(1.0, {5: K})).imag)
                      for K in K_values])  # the largest growth rate, m = 1
deviation = np.abs(numerical - growth_rate(1.0, K_values))
at_threshold = np.abs(K_values - 1.0) < 1e-12  # K = m exactly, where h_k^2 = 0
check(np.max(deviation[~at_threshold]) < 1e-10 and np.max(deviation) < 1e-6,
      "growth rate from the eigenvalues = sqrt(K^2 - m^2) (m = 1)")
```

For 61 momenta $K = 0, 0.1, \dots, 6$ the largest imaginary part of the 16 eigenvalues of $h_k$ (with $m = 1$, $k_5 = K$) is the numerical growth rate. `deviation` holds the differences from the formula. `at_threshold` marks the single point $K = 1 = m$, where $h_k^2 = 0$: a matrix whose square is zero has the double eigenvalue 0, which a computer finds only to about $10^{-8}$. `~` means "not", so `deviation[~at_threshold]` are the deviations at the other 60 points; the check requires them below $10^{-10}$, and the one at the threshold below $10^{-6}$.

```python
report("growth rate at m = 1, K = 2 (sqrt 3)", f"{growth_rate(1.0, 2.0):.9f}")
report("growth rate at m = 1, K = 1000", f"{growth_rate(1.0, 1000.0):.6f}")
check_record(growth_rate(1.0, 1000.0) > 999.0 and growth_rate(1.0, 1e6) > 999999.0,
             "the growth rate has no upper bound (kappa/K tends to 1)",
             "Revision/theory/reports/python-scope.json",
             "extra_time_growth_rates_unbounded", "which has no upper bound")
```

Two RESULT lines: the rate $\sqrt3 = 1.732050808$ at $K = 2$, and $999.999500$ at $K = 1000$. The check illustrates the unbounded growth at $K = 1000$ and $K = 10^6$ (`1e6`), and requires the record's words "which has no upper bound"; the proof is the inequality $\kappa \ge K - c$ of Section 8.18.

```python
K_fine = np.linspace(0.0, 6.0, 601)
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.2), sharey=True)
for mass, style in ((0.5, "-"), (1.0, "--"), (2.0, ":")):
    left.plot(K_fine, growth_rate(mass, K_fine), style, label=f"$m = {mass}$")
left.plot(K_values[::3], numerical[::3], "o", markersize=4, color="black",
          label="eigenvalues, $m = 1$")
left.plot(K_fine, K_fine, color="gray", linewidth=0.8, label="$\\kappa = K$")
left.set_xlabel("extra-time momentum $K = k_5$")
left.set_ylabel("growth rate $\\kappa$")
left.set_title("$k_1 = 0$: three masses")
left.legend(loc="upper left")
```

The left panel draws the formula for three masses on a fine grid (601 points) with solid, dashed and dotted lines; the black dots are every third numerical rate of $m = 1$ (`[::3]` takes every third element); the gray line is $\kappa = K$, which every curve approaches.

```python
for k1, style in ((0.0, "-"), (2.0, "--"), (4.0, ":")):
    right.plot(K_fine, growth_rate(1.0, K_fine, k1), style, label=f"$k_1 = {k1}$")
right.plot(K_fine, K_fine, color="gray", linewidth=0.8, label="$\\kappa = K$")
right.set_xlabel("extra-time momentum $K = k_5$")
right.set_title("$m = 1$: three space momenta $k_1$")
right.legend(loc="upper left")
save_figure(fig, "growth_rate_vs_momentum",
            "The growth rate $\\kappa = \\sqrt{K^2 - m^2 - k_1^2}$ of the growing "
            ...
            "$\\kappa = K$, so the rate has no upper bound.")
```

The right panel draws the formula for $m = 1$ and three space momenta, with the same gray line. The figure is Figure 08a.1. Output: one PASS line, two RESULT lines, one PASS line with its `reproduces` line, and the figure line.

**What Figure 08a.1 shows.** Both panels plot the growth rate $\kappa$ (vertical) against the extra-time momentum $K = k_5$ (horizontal), both in the same unit, an inverse length. Left: masses $m = 0.5, 1, 2$; each curve is zero up to the threshold $K = m$, then rises steeply and bends towards the gray line $\kappa = K$; the black dots, the numerical eigenvalues for $m = 1$, lie exactly on the dashed curve. Right: $m = 1$ with $k_1 = 0, 2, 4$: a space momentum moves the threshold to $K = \sqrt{1 + k_1^2}$ but does not stop the rise. The student should see that every curve approaches $\kappa = K$, so the rate has no upper bound.

**In [7], where the waves oscillate and where they grow.**

```python
k1_grid, k5_grid = np.meshgrid(np.linspace(-5.0, 5.0, 201), np.linspace(-5.0, 5.0, 201))
E2_grid = 1.0 + k1_grid**2 - k5_grid**2  # m = 1
kappa_grid = np.sqrt(np.maximum(-E2_grid, 0.0))
growing_fraction = float(np.mean(E2_grid < 0.0))
report("fraction of the grid where the waves grow", f"{growing_fraction:.4f}")
check(abs(kappa_grid[100, 100]) == 0.0 and abs(kappa_grid[200, 100] - 24**0.5) < 1e-12,
      "kappa = 0 at k = 0 and kappa = sqrt(24) at k1 = 0, k5 = 5")
```

`np.meshgrid` makes two $201 \times 201$ arrays: at row $r$ and column $c$, `k1_grid` holds the $c$-th value of $k_1$ and `k5_grid` the $r$-th value of $k_5$, each running from $-5$ to $5$ in steps of $0.05$. `E2_grid` is $E^2 = 1 + k_1^2 - k_5^2$ at every grid point and `kappa_grid` the growth rate. `np.mean` of the true/false array `E2_grid < 0.0` is the fraction of grid points where the waves grow: RESULT 0.4439. The check tests two points: row 100, column 100 is $k_1 = k_5 = 0$, where $\kappa = 0$; row 200, column 100 is $k_5 = 5$, $k_1 = 0$, where $\kappa = \sqrt{25 - 1} = \sqrt{24}$.

```python
fig, ax = plt.subplots(figsize=(6.0, 5.0))
shown = np.where(E2_grid < 0.0, kappa_grid, np.nan)  # nan: not coloured (white)
image = ax.pcolormesh(k1_grid, k5_grid, shown, cmap="viridis", shading="auto")
fig.colorbar(image, ax=ax, label="growth rate $\\kappa$")
lines = ax.contour(k1_grid, k5_grid, kappa_grid, levels=[1, 2, 3, 4], colors="white",
                   linewidths=0.8)
ax.clabel(lines, fmt="%d", fontsize=8)
ax.contour(k1_grid, k5_grid, E2_grid, levels=[0.0], colors="black", linewidths=1.2)
ax.text(2.6, 0.0, "oscillation\n$E^2 > 0$", ha="center", va="center")
ax.set_xlabel("space momentum $k_1$")
ax.set_ylabel("extra-time momentum $k_5$")
ax.set_title("Growth rate of the waves, $m = 1$")
save_figure(fig, "growth_map",
            "The growth rate $\\kappa$ in the plane of the space momentum $k_1$ "
            ...
            "makes the waves grow.")
```

`np.where(condition, a, b)` takes `a` where the condition holds and `b` elsewhere; `np.nan` ("not a number") is left uncoloured, so the oscillating region stays white. `pcolormesh` colours the grid with the colour map `"viridis"`; `contour` draws the curves of equal growth rate $\kappa = 1, 2, 3, 4$ in white, and `clabel` writes their values on them (`"%d"`: as whole numbers); a second `contour` draws the border $E^2 = 0$ in black; `text` writes a label at $(2.6, 0)$ (`\n` starts a new line). The figure is Figure 08a.2. Output: one RESULT line, one PASS line, the figure line.

**What Figure 08a.2 shows.** The plane of the space momentum $k_1$ (horizontal) and the extra-time momentum $k_5$ (vertical), both from $-5$ to $5$ in units of the inverse length, for $m = 1$. The white region around the horizontal axis is where $E^2 = 1 + k_1^2 - k_5^2 > 0$: the waves oscillate. Above and below it, bounded by the black hyperbola $k_5^2 - k_1^2 = 1$, the colour shows the growth rate, with white contour lines at $\kappa = 1, 2, 3, 4$. The student should see that the two coloured regions reach to infinity: however large $k_1$ is, a large enough $k_5$ makes the waves grow.

**In [8], solving in time, in two independent ways.**

```python
def evolve(hk, E2_value, x4, u0):
    """u(x4) = (cos(E x4) - i sin(E x4)/E h_k) u0, with E = sqrt(E^2) (complex)."""
    if E2_value == 0.0:
        return u0 - 1j * x4 * (hk @ u0)  # the limit E -> 0
    E = np.sqrt(complex(E2_value))  # E is imaginary when E^2 < 0
    return np.cos(E * x4) * u0 - 1j * np.sin(E * x4) / E * (hk @ u0)
```

`evolve` is the closed formula of Section 8.18: for $E^2 = 0$ the limit $u_0 - ix_4h_ku_0$, otherwise $\cos(Ex_4)u_0 - i\frac{\sin(Ex_4)}{E}h_ku_0$, where `np.sqrt(complex(...))` gives the imaginary $E = i\kappa$ when $E^2 < 0$ (numpy's cosine and sine of an imaginary number are then the hyperbolic functions).

```python
def rk4(hk, x4_end, u0, steps):
    """The classical RK4 method for du/dx4 = -i h_k u from 0 to x4_end."""
    step = x4_end / steps
    u = u0.astype(complex)
    for _ in range(steps):
        s1 = -1j * (hk @ u)
        s2 = -1j * (hk @ (u + step / 2 * s1))
        s3 = -1j * (hk @ (u + step / 2 * s2))
        s4 = -1j * (hk @ (u + step * s3))
        u = u + step / 6 * (s1 + 2 * s2 + 2 * s3 + s4)
    return u
```

`rk4` is the classical fourth-order Runge-Kutta method of Chapter 2 for $du/dx_4 = -ih_ku$: in each step it evaluates the right-hand side four times (at the start, twice at the middle, at the end) and advances with the weighted average $\frac16(s_1 + 2s_2 + 2s_3 + s_4)$. It knows nothing of the closed formula, so the two are independent.

```python
rng = np.random.default_rng(12345)  # fixed seed: the same numbers in every run
u_start = rng.normal(size=16) + 1j * rng.normal(size=16)
u_start = u_start / np.sqrt(np.vdot(u_start, u_start).real)  # u^dagger u = 1
```

A random-number generator with the fixed **seed** 12345 produces the same "random" numbers in every run. The starting column has 16 complex entries whose real and imaginary parts are drawn from the normal (bell-shaped) distribution; dividing by $\sqrt{u^\dagger u}$ makes its size 1 (`np.vdot(a, b)` is $a^\dagger b$).

```python
worst = 0.0
for K in (0.5, 1.0, 2.0, 3.0):
    hk = mode_matrix(1.0, {5: K})
    exact = evolve(hk, 1.0 - K**2, 3.0, u_start)
    stepped = rk4(hk, 3.0, u_start, 3000)
    relative = np.linalg.norm(exact - stepped) / np.linalg.norm(exact)
    worst = max(worst, relative)
    say(f"K = {K}: u^dagger u at x4 = 3 is {np.vdot(exact, exact).real:.6e}")
check(worst < 1e-9, "the closed formula and RK4 agree at x4 = 3 (relative < 1e-9)")
```

For four extra-time momenta (with $m = 1$, so $E^2 = 1 - K^2$) the wave is followed to $x_4 = 3$ both ways, RK4 with 3000 steps. The relative difference (the length of the difference divided by the length of the exact column; `np.linalg.norm` is the length $\sqrt{u^\dagger u}$) is recorded, and the largest one must be below $10^{-9}$. The printed sizes at $x_4 = 3$ (`:.6e` prints in powers of ten) are $1.347676$ for $K = 0.5$ (oscillation), $20.06346$ for $K = 1$ ($E = 0$, growth like a power of $x_4$), $1.880098 \times 10^4$ for $K = 2$ and $1.086955 \times 10^7$ for $K = 3$ (COMPUTED). Output: four lines and one PASS line.

**In [9], the size of a wave in time.**

```python
x4_values = np.linspace(0.0, 3.0, 301)
fig, ax = plt.subplots()
for K in (0.5, 1.0, 2.0, 3.0, 5.0):
    hk = mode_matrix(1.0, {5: K})
    sizes = [np.vdot(v, v).real for v in
             (evolve(hk, 1.0 - K**2, x4, u_start) for x4 in x4_values)]
    ax.plot(x4_values, np.log(sizes), label=f"$K = {K}$")
```

For five momenta the size $u^\dagger u$ is computed with the closed formula at 301 times from 0 to 3, and its natural logarithm is drawn (`np.log`).

```python
    if K > 1.0:  # the asymptotic straight line of slope 2 kappa
        kappa = growth_rate(1.0, K)
        ax.plot(x4_values, np.log(sizes[-1]) + 2 * kappa * (x4_values - 3.0), "--",
                color="gray", linewidth=0.8)
# An empty line that only adds the dashed straight lines to the legend:
ax.plot([], [], "--", color="gray", linewidth=0.8, label="slope $2\\kappa$")
ax.set_xlabel("time $x_4$")
ax.set_ylabel("$\\ln(u^\\dagger u)$")
ax.set_title("Size of a wave in time, $m = 1$")
ax.legend();
save_figure(fig, "norm_in_time",
            "The natural logarithm of the size $u^\\dagger u$ of a wave against the "
            ...
            "$2\\kappa$ (gray dashed), $2\\sqrt3$, $2\\sqrt8$ and $2\\sqrt{24}$.")
```

For the growing waves a gray dashed straight line of slope $2\kappa$ is drawn through the last point (`sizes[-1]` is the last element): $u^\dagger u$ grows like $e^{2\kappa x_4}$ (the size squared of $e^{\kappa x_4}$), so its logarithm becomes a straight line of slope $2\kappa$. The empty plot only adds the gray line to the legend. The figure is Figure 08a.3; the cell prints only the figure line.

**What Figure 08a.3 shows.** The natural logarithm of $u^\dagger u$ (a pure number) against the time $x_4$ (units of $1/m$), for $m = 1$ and $K = 0.5, 1, 2, 3, 5$, all started from the same column of size 1 ($\ln 1 = 0$). For $K = 0.5$ the curve stays near 0 (oscillation); for $K = 1$ it rises slowly (a power of $x_4$); for $K = 2, 3, 5$ it soon runs along a straight line of slope $2\sqrt3$, $2\sqrt8$ and $2\sqrt{24}$ (gray dashed). The student should see exponential growth whose rate increases with the extra-time momentum.

**In [10], Hadamard's amplification.**

```python
def growing_eigenvector(mass, K):
    """A unit eigenvector of h_k (k5 = K) for the eigenvalue +i kappa."""
    hk = mode_matrix(mass, {5: K})
    kappa = growth_rate(mass, K)
    # The null space of h_k - i kappa I: the right singular vector of the smallest
    # singular value (numpy sorts the singular values from large to small).
    _, _, vh = np.linalg.svd(hk - 1j * kappa * np.eye(16))
    u_plus = vh[-1].conj()
    return hk, kappa, u_plus / np.linalg.norm(u_plus)
```

`growing_eigenvector` finds a column $u_+$ with $h_ku_+ = i\kappa u_+$. The **singular value decomposition** (`np.linalg.svd`) writes a matrix $A$ as $U\Sigma V^\dagger$ with a list of numbers $\Sigma$ (the singular values, sorted from large to small) and two matrices $U$ and $V$ whose columns have length 1 and are perpendicular; a column of $V$ whose singular value is zero solves $Au = 0$. numpy returns $V^\dagger$ as `vh`, so the last row of `vh`, conjugated, is the last column of $V$. The column is divided by its length.

```python
hk, kappa, u_plus = growing_eigenvector(1.0, 4.0)
later = evolve(hk, 1.0 - 4.0**2, 1.0, u_plus)
check(np.linalg.norm(hk @ u_plus - 1j * kappa * u_plus) < 1e-12
      and abs(np.linalg.norm(later) - np.exp(kappa)) < 1e-9 * np.exp(kappa),
      "a growing eigenvector grows exactly like e^(kappa x4) (K = 4)")
```

For $m = 1$, $K = 4$ ($\kappa = \sqrt{15}$) the check confirms that $u_+$ is an eigenvector to $10^{-12}$ and that its length at $x_4 = 1$ is $e^\kappa$ to a relative $10^{-9}$.

```python
K_axis = np.linspace(0.0, 200.0, 2001)
fig, ax = plt.subplots()
for s in (0, 2, 4, 8):
    log_ratio = (growth_rate(1.0, K_axis) - s / 2 * np.log(1 + K_axis**2)) / np.log(10)
    ax.plot(K_axis, log_ratio, label=f"$s = {s}$")
    crossing = K_axis[np.argmax(log_ratio > 6.0)]  # first K with ratio above 10^6
    report(f"s = {s}: first K (step 0.1) with ratio above 10^6", f"{crossing:.1f}")
    check(log_ratio[-1] > 50.0, f"s = {s}: the ratio exceeds 10^50 at K = 200")
```

For $K$ from 0 to 200 in steps of 0.1 and four Sobolev orders, `log_ratio` is the base-10 logarithm of the amplification, $(\kappa - \frac s2\ln(1 + K^2))/\ln 10$ (Section 8.18). `np.argmax` of a true/false array gives the position of the first true value, so `crossing` is the first $K$ at which the ratio exceeds $10^6$; it is printed (13.9, 19.9, 27.1, 44.2). Each check requires the ratio to exceed $10^{50}$ at $K = 200$ (`log_ratio[-1]` is the last value).

```python
ax.axhline(0.0, color="black", linewidth=0.8)
ax.set_xlabel("extra-time momentum $K$")
ax.set_ylabel("$\\log_{10}$(solution at $x_4 = 1$ / data)")
ax.set_title("Amplification after one unit of time, $m = 1$")
ax.legend();
save_figure(fig, "hadamard_ratio",
            "The base-10 logarithm of the amplification, the size of the solution "
            ...
            "solutions and the problem is not well posed in the sense of Hadamard.")
```

Axis labels, a black line at 0 (amplification 1), and Figure 08a.4. Output: one PASS line, four RESULT lines with four PASS lines, the figure line.

**What Figure 08a.4 shows.** The base-10 logarithm of the amplification after one unit of time (vertical; a pure number) against the extra-time momentum $K$ from 0 to 200 (horizontal, units of $m$), for the Sobolev orders $s = 0, 2, 4, 8$. The curves of the larger orders first dip below 0 (for $s = 8$ down to about $-4$, back above 0 near $K = 26$, where $\sqrt{K^2 - 1} = 4\ln(1 + K^2)$), because a strong norm punishes the wiggles of the data; then every curve rises along a nearly straight line of slope about $1/\ln 10 \approx 0.43$, without bound (at $K = 200$ the values lie between about 68 and 87). The student should see that a stronger norm only delays the rise: arbitrarily small data give arbitrarily large solutions, the failure of Hadamard's third condition.

**In [11], the Krein form.**

```python
hk = mode_matrix(1.0, {5: 2.0})
times = np.linspace(0.0, 4.0, 401)
path = [evolve(hk, 1.0 - 4.0, x4, u_start) for x4 in times]
hilbert = np.array([np.vdot(v, v).real for v in path])  # u^dagger u
krein_values = np.array([np.vdot(v, B @ v) for v in path])  # u^dagger B u
drift = np.max(np.abs(krein_values - krein_values[0]) / np.maximum(hilbert, 1.0))
report("Krein form at x4 = 0", f"{krein_values[0].real:+.9f}")
report("u^dagger u at x4 = 4", f"{hilbert[-1]:.6e}")
imaginary = np.max(np.abs(krein_values.imag) / np.maximum(hilbert, 1.0))
check(drift < 1e-12 and imaginary < 1e-12,
      "the Krein form u^dagger B u is constant (drift / max(u^dagger u, 1) < 1e-12)")
```

The random column of In [8] is followed with $m = 1$, $K = 2$ to $x_4 = 4$ at 401 times; `hilbert` holds $u^\dagger u$ and `krein_values` holds $u^\dagger Bu$. The **drift** is the largest change of the Krein form, divided by $\max(u^\dagger u, 1)$: rounding errors grow with the size of the numbers, so the change is measured relative to it. The two RESULT lines print the Krein form at the start, $+0.129919115$, and $u^\dagger u = 6.006621 \times 10^5$ at $x_4 = 4$. The check requires the drift and the imaginary part of the Krein form (a Hermitian form gives real values) below $10^{-12}$.

```python
def eigenspace(hk, value):
    """An orthonormal basis (columns) of the eigenspace of hk for value."""
    _, singular, vh = np.linalg.svd(hk - value * np.eye(16))
    return vh[singular < 1e-9].conj().T
```

`eigenspace` returns, as columns, all right singular vectors of $h_k - \lambda I$ whose singular value is below $10^{-9}$: an **orthonormal basis** (columns of length 1, perpendicular to each other) of the eigenspace of $\lambda$. `vh[singular < 1e-9]` selects the rows of `vh` with small singular values.

```python
V_grow = eigenspace(mode_matrix(1.0, {5: 2.0}), 1j * 3**0.5)
form_grow = V_grow.conj().T @ B @ V_grow  # the Krein form on that eigenspace
check_record(V_grow.shape[1] == 8 and np.max(np.abs(form_grow)) < 1e-12,
             "m = 1, k5 = 2: the 8-dim eigenspace of +i sqrt(3) is Krein-neutral",
             "Revision/pairing/reports/python-pairing.json",
             "Q.one_particle_complex_frequency_Krein_neutral",
             "(0, 0, 0, 2, 0, 0, 0): w^2 = -3, eigenspace dimensions "
             f"[{V_grow.shape[1]}, {V_grow.shape[1]}], B-form identically zero: True")
```

The eigenspace of the growing frequency $+i\sqrt3$ ($m = 1$, $k_5 = 2$) has 8 basis columns. The $8 \times 8$ matrix `form_grow` holds every value $v^\dagger Bu$ for two basis columns; the check requires dimension 8 and all 64 values below $10^{-12}$ (the Krein-neutrality of Section 8.19), and the pairing record's text for the same sample (it lists the momenta in the order $k_1, k_2, k_3, k_5, k_6, k_7, k_8$ and calls the frequency $w$).

```python
V_real = eigenspace(mode_matrix(1.0, {1: 2.0, 8: 2.0}), 3.0)
form_real = np.linalg.eigvalsh(V_real.conj().T @ B @ V_real)  # Hermitian 8 x 8
inertia = (int(np.sum(form_real > 1e-9)), int(np.sum(form_real < -1e-9)))
report("Krein inertia of the eigenspace of E = 3 (m = 1, k1 = k8 = 2)", inertia)
check_record(V_real.shape[1] == 8 and inertia == (4, 4),
             "m = 1, k1 = k8 = 2: the eigenspace of E = 3 has Krein inertia (4, 4)",
             "Revision/pairing/reports/python-pairing.json",
             "Q.one_particle_Krein_inertia",
             f"w = 3: dim {V_real.shape[1]}, Krein inertia ({inertia[0]},{inertia[1]})")
```

For the good-sector wave $m = 1$, $k_1 = k_8 = 2$ ($E^2 = 1 + 4 + 4 = 9$) the eigenspace of $E = 3$ is found; the Krein form restricted to it is a Hermitian $8 \times 8$ matrix, whose eigenvalues `np.linalg.eigvalsh` computes. Counting the positive and the negative ones gives the inertia, printed as `(4, 4)`; the check also requires the pairing record's text.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
left.plot(times, np.log(hilbert))
left.set_xlabel("time $x_4$")
left.set_ylabel("$\\ln(u^\\dagger u)$")
left.set_title("Hilbert norm: grows")
right.plot(times, krein_values.real)
right.axhline(krein_values[0].real, color="gray", linestyle="--", linewidth=0.8)
right.set_ylim(krein_values[0].real - 0.5, krein_values[0].real + 0.5)
right.set_xlabel("time $x_4$")
right.set_ylabel("$u^\\dagger B u$")
right.set_title("Krein form: constant")
save_figure(fig, "krein_norm",
            "One wave with $m = 1$ and extra-time momentum $K = 2$ followed from "
            ...
            "positive and the negative parts of the Krein form grow together.")
```

Left: $\ln(u^\dagger u)$ against the time. Right: the Krein form, with a gray dashed line at its starting value and a vertical range of $\pm 0.5$ around it. The figure is Figure 08a.5. Output: three RESULT lines, three PASS lines (two with `reproduces` lines), the figure line.

**What Figure 08a.5 shows.** One wave ($m = 1$, $K = 2$) from $x_4 = 0$ to $4$ (units of $1/m$). Left: the logarithm of its Hilbert norm rises, after a short start, along a straight line of slope $2\sqrt3$, to about $\ln(6.0 \times 10^5) \approx 13.3$. Right: its Krein form (a pure number) is a flat line on the gray dashed line at $0.1299$. The student should see the ordinary size growing by almost six powers of ten while the Krein form does not move, possible because the growing waves carry Krein form zero.

**In [12], the good sector, and the eigenvalue paths.**

```python
good = mode_matrix(1.3, {1: 0.4, 2: -1.1, 3: 0.7, 8: 2.2})  # no k5, k6, k7
good_eigenvalues = np.linalg.eigvals(good)
E_good = np.sqrt(1.3**2 + 0.4**2 + 1.1**2 + 0.7**2 + 2.2**2)
check_record(np.allclose(good, good.conj().T) and np.allclose(good @ B, B @ good)
             and np.max(np.abs(np.abs(good_eigenvalues) - E_good)) < 1e-12
             and np.max(np.abs(good_eigenvalues.imag)) < 1e-12,
             "good sector: h_k Hermitian, [B, h_k] = 0, eigenvalues real +-E",
             "Revision/theory/reports/python-field-theory.json",
             "good_sector_spectrum_and_B_sectors", "h is Hermitian", "[B, h] = 0")
```

A good-sector mode matrix with $m = 1.3$ and four space momenta (no extra-time momentum). The check requires: $h_k$ Hermitian, commuting with $B$, every eigenvalue of size $E = \sqrt{m^2 + k_1^2 + k_2^2 + k_3^2 + k_8^2}$ and with imaginary part below $10^{-12}$, so the eigenvalues are $\pm E$, real; and the record's texts.

```python
path_values = np.linspace(0.0, 2.5, 26)  # the momenta 0, 0.1, ..., 2.5
colours = np.repeat(path_values, 16)  # each matrix has 16 eigenvalues
fig, panels = plt.subplots(1, 2, figsize=(10.0, 4.6), sharey=True)
for panel, direction, name in ((panels[0], 1, "space momentum $k_1$ (good sector)"),
                               (panels[1], 5, "extra-time momentum $K = k_5$")):
    points = np.concatenate([np.linalg.eigvals(mode_matrix(1.0, {direction: p}))
                             for p in path_values])
    dots = panel.scatter(points.real, points.imag, c=colours, cmap="plasma", s=22)
```

For 26 momenta from 0 to 2.5, the 16 eigenvalues of $h_k$ ($m = 1$) are computed with the momentum along $x_1$ (left panel) or along $x_5$ (right panel); `np.concatenate` joins the 26 lists into one. `np.repeat(path_values, 16)` repeats each momentum 16 times, so that every eigenvalue gets the colour of its momentum. `scatter` draws them as dots in the complex plane (real part horizontal, imaginary part vertical).

```python
    panel.set_xlim(-3.0, 3.0)
    panel.set_ylim(-3.0, 3.0)
    panel.set_aspect("equal")
    panel.set_xlabel("real part of the eigenvalue $E$")
    panel.set_title(name)
panels[0].set_ylabel("imaginary part of the eigenvalue $E$")
fig.colorbar(dots, ax=panels, label="momentum (0 to 2.5)")
save_figure(fig, "eigenvalue_paths",
            "The eigenvalues $E$ of the mode matrix for $m = 1$ in the complex "
            ...
            "leave along the imaginary axis as $\\pm i\\sqrt{K^2 - 1}$: growth.")
```

Equal ranges and equal scales on both axes (`set_aspect("equal")`), labels, one colour bar for both panels, and Figure 08a.6. Output: one PASS line with its `reproduces` line, the figure line.

**What Figure 08a.6 shows.** The eigenvalues $E$ of the mode matrix for $m = 1$ in the complex plane (horizontal: real part; vertical: imaginary part; units of $m$), coloured from dark (momentum 0) to bright (momentum 2.5). Left, a growing space momentum: the eigenvalues $\pm\sqrt{1 + k_1^2}$ start at $\pm1$ and move outwards along the real axis; they stay real. Right, a growing extra-time momentum: the eigenvalues $\pm\sqrt{1 - K^2}$ move inwards along the real axis, meet at 0 for $K = 1$, and then leave along the imaginary axis as $\pm i\sqrt{K^2 - 1}$. The student should see the moment at which oscillation turns into growth.

**In [13], the last check.**

```python
for name in ("08a_1_growth_rate_vs_momentum.png", "08a_2_growth_map.png",
             "08a_3_norm_in_time.png", "08a_4_hadamard_ratio.png",
             "08a_5_krein_norm.png", "08a_6_eigenvalue_paths.png"):
    check(output_file(f"{FIGURE_FOLDER}/{name}").is_file(),
          f"the figure file {name} exists")
all_checks_passed()
```

Six checks that the figure files exist, and the last line. The 30 checks come from the cells as follows: three in In [2], four in In [3], two each in In [4], In [5] and In [6], one each in In [7] and In [8], five in In [10], three in In [11], one in In [12] and six here (In [9] has none). The last line reads `ALL 30 CHECKS PASSED (notebook 08a)`.

### 8.24 The deflating history pushes every extra-time wave into growth

Sections 8.17 to 8.19 froze the coefficients. In the author's metric they are not frozen: the extra times deflate, and this changes the momentum that a wave has along them. This section follows the change exactly.

**The hidden coordinate $y$.** A second way to label the points of the hidden direction is $y = \ln(\sin z)/(6H)$. At the patch end $z = \pi/2$, $\sin z = 1$ and $y = 0$; towards the tip $z \to 0$, $\sin z \to 0$ and $y \to -\infty$. Two facts make $y$ useful, each derived in one line. First, $\sin z = e^{6Hy}$ (undo the logarithm), so $\sin^{1/6}z = e^{Hy}$ and $\sin^{1/3}z = e^{2Hy}$. Second, $dy/dx_8 = \frac{1}{6H}\cdot\frac{\cos z}{\sin z}\cdot 6H = \cot z$ (chain rule with $dz/dx_8 = 6H$), so $\cot^2 z\,dx_8^2 = dy^2$. The author's metric therefore reads

$$
ds^2 = e^{2Hy}\big(e^{2a_4}(dx_1^2 + dx_2^2 + dx_3^2) - e^{-2a_4}(dx_5^2 + dx_6^2 + dx_7^2)\big) - dx_4^2 + dy^2 ,
$$

and $y$ measures proper length along the hidden direction. The Kohn-Sham record cuts the tip at $y = -L$ with $L = 3$ (`Revision/kohn_sham/results/parameters.json`, entry `physics.L_tipCutoff`).

**The history.** The examples use the history $a_4 = AHx_4$ with $A = 1$ and $H = m = 1$, the canonical history of the Kohn-Sham record (`parameters.json`, entries `physics.historyA`, `physics.H`, `physics.m`). It is ASSUMED: the record calls it a PRESCRIBED BACKGROUND, chosen and not solved for, because the Kohn-Sham states along it do not satisfy the source conditions of the $a_4$ equations (Chapter 17). Along it the 3-space scale factor $e^{a_4}e^{Hy}$ grows exponentially, the extra-time scale factor $e^{-a_4}e^{Hy}$ shrinks exponentially, and the product of the six, $e^{6Hy} = \sin z$, does not change.

**Wave numbers that do not change.** The coefficients of the field equation in the author's metric do not depend on $x_1, x_2, x_3, x_5, x_6, x_7$. So a field of the form $\Psi = e^{i(q_1x_1 + q_5x_5)}\psi(x_4, y)$ keeps this form for all times: every derivative $\partial_1$ or $\partial_5$ acting on it gives the factor $iq_1$ or $iq_5$, the common exponential divides out, and the equation for $\psi$ contains neither $x_1$ nor $x_5$. The numbers $q_1$ and $q_5$ are **coordinate wave numbers**: radians of phase per unit of the coordinate. They are exact constants of the motion.

**Frame momenta that do change.** A frame momentum counts radians per unit of PROPER length; a coordinate length $\Delta x_a$ has the proper length $f_a\Delta x_a$, so $k_{(a)} = q_a/f_a$. Line by line:

1. $k_{(1)} = q_1/f_1 = q_1e^{-a_4}e^{-Hy}$, because $f_1 = e^{a_4}\sin^{1/6}z = e^{a_4}e^{Hy}$;
2. $k_{(5)} = q_5/f_5 = q_5e^{a_4}e^{-Hy}$, because $f_5 = e^{-a_4}\sin^{1/6}z = e^{-a_4}e^{Hy}$;
3. with frozen coefficients at the time $x_4$ (Section 8.17), $E^2 = m^2 + k_{(1)}^2 - k_{(5)}^2 = m^2 + q_1^2e^{-2Hy}e^{-2a_4} - q_5^2e^{-2Hy}e^{2a_4}$.

As the extra times deflate ($a_4$ grows), a fixed number of wiggles per unit of $x_5$ means more and more wiggles per unit of proper length: the frame momentum $k_{(5)}$ grows like $e^{a_4}$, while $k_{(1)}$ shrinks like $e^{-a_4}$ because 3-space inflates.

**The onset of growth.** Write $X = e^{2a_4}$ and $w = e^{-Hy}$. Then $e^{-2a_4} = 1/X$ and $E^2 = m^2 + q_1^2w^2/X - q_5^2w^2X$. As a function of $X > 0$ it decreases: its derivative $-q_1^2w^2/X^2 - q_5^2w^2$ is negative for $q_5 \neq 0$. So along the history (where $X$ grows with the time) $E^2$ crosses zero exactly once and stays negative afterwards; the moment of the crossing is the **onset**. To find it, line by line:

$$
\begin{aligned}
0 &= m^2 + \frac{q_1^2w^2}{X} - q_5^2w^2X, \\
0 &= q_5^2w^2X^2 - m^2X - q_1^2w^2, \\
X^\ast &= \frac{m^2 + \sqrt{m^4 + 4q_1^2q_5^2w^4}}{2q_5^2w^2}, \\
x_4^\ast &= \frac{\ln X^\ast}{2AH} .
\end{aligned}
$$

The first line sets $E^2 = 0$; the second multiplies by $-X$ (allowed, $X > 0$); the third is the quadratic formula, with the root that is positive (the other root, with the minus sign, is not positive, because the square root is at least $m^2$, and $X = e^{2a_4}$ must be positive); the fourth undoes $X = e^{2a_4} = e^{2AHx_4}$. For a wave without space momentum, $q_1 = 0$, the third line is $X^\ast = m^2/(q_5^2w^2)$, and the onset time simplifies to

$$
x_4^\ast = \frac{\ln(m/q_5) - \ln w}{AH} = \frac{Hy + \ln(m/q_5)}{AH} .
$$

At $y = 0$ with $A = H = m = 1$ this is $\ln(1/q_5)$: $x_4^\ast = \ln 20 = 2.995732$ for $q_5 = 0.05$ and $\ln 10 = 2.302585$ for $q_5 = 0.1$ (Notebook 08b prints both). The onset time is finite for every $q_5 > 0$: a smaller wave number only delays it, logarithmically. So every wave along an extra time eventually stops oscillating and starts to grow, and after the onset its growth rate $\kappa = \sqrt{k_{(5)}^2 - m^2 - k_{(1)}^2}$ keeps increasing, since $k_{(5)}$ grows without bound (PROVED with frozen coefficients at each instant; this is the local-frame statement of the record, `Revision/theory/reports/python-field-theory.json`, check `extra_time_modes_grow`: "every extra-time mode eventually enters the growing regime"). Restricting the theory to the good sector, the fields that do not depend on the extra times, removes this growth; it is a choice, not a consequence of the equations.

### 8.25 Following one wave through the onset: the local-frame model and WKB

**The local-frame model (labelled MODEL; ASSUMED).** The field also depends on $y$, and the factor $e^{-Hy}$ in the frame momenta makes the exact equation couple neighbouring values of $y$. The **local-frame model** holds the hidden position fixed (it freezes the coefficients in $y$ only), works in the variables $\chi$ of Section 8.30 (in which the term $3H\gamma^{(8)}$ is absent exactly), takes no momentum along the hidden direction, and keeps the exact time dependence of the frame momenta:

$$
i\,\frac{du}{dx_4} = h(x_4)\,u, \qquad h(x_4) = -im\gamma^{(4)} - \gamma^{(4)}\big(k_{(1)}(x_4)\gamma^{(1)} + k_{(5)}(x_4)\gamma^{(5)}\big).
$$

Its solutions are not exact solutions of the field equation; they show how a wave behaves near one hidden position as the extra times deflate. The position enters only through $q_5e^{-Hy}$, so the runs use $y = 0$. At every instant $h(x_4)^2 = E^2(x_4)I_{16}$ with the $E^2$ of Section 8.24 (Section 8.17 with the frame momenta of that instant).

**A clean starting column.** Take $q_1 = 0$. The matrix $C = \gamma^{(8)}\gamma^{(1)}\gamma^{(2)}\gamma^{(3)}$ commutes with $\gamma^{(4)}$ and with $\gamma^{(5)}$ (moving either of them through the four factors of $C$ changes the sign four times), hence with $h(x_4)$. A column $u$ can therefore be an eigenvector of $h(0)$ for the positive frequency $E_0 = \sqrt{m^2 - q_5^2}$ and at the same time of $C$ for the eigenvalue $\sigma = +1$ or $-1$ ($C$ is real, symmetric, and $C^2 = I_{16}$). For such a column of size $u^\dagger u = 1$ the Krein form is $u^\dagger Bu = \sigma E_0/m$. Line by line:

1. $B = -iC\gamma^{(4)} = C(-i\gamma^{(4)})$, and since $C$ is Hermitian with $Cu = \sigma u$, $u^\dagger C = \sigma u^\dagger$; so $u^\dagger Bu = \sigma\,u^\dagger(-i\gamma^{(4)})u$.
2. $E_0 = E_0u^\dagger u = u^\dagger h(0)u = m\,u^\dagger(-i\gamma^{(4)})u - q_5\,u^\dagger\gamma^{(4)}\gamma^{(5)}u$ (at $x_4 = 0$, $a_4 = 0$ and $k_{(5)} = q_5$ at $y = 0$).
3. $-i\gamma^{(4)}$ is Hermitian, so $u^\dagger(-i\gamma^{(4)})u$ is real; $\gamma^{(4)}\gamma^{(5)}$ is real and antisymmetric, so $u^\dagger\gamma^{(4)}\gamma^{(5)}u$ is purely imaginary (its complex conjugate is $u^T\gamma^{(4)}\gamma^{(5)}u^\ast = u^\dagger(\gamma^{(4)}\gamma^{(5)})^Tu = -u^\dagger\gamma^{(4)}\gamma^{(5)}u$, a number being equal to its own transpose).
4. $E_0$ is real, so the imaginary term vanishes, $u^\dagger(-i\gamma^{(4)})u = E_0/m$, and by line 1, $u^\dagger Bu = \sigma E_0/m$.

The notebook builds such columns with two **projectors** (matrices $P$ with $P^2 = P$): $\Lambda_+ = \frac12(I_{16} + h(0)/E_0)$ keeps the part of a column with eigenvalue $+E_0$, and $\frac12(I_{16} + \sigma C)$ the part with $C = \sigma$; they commute, so their product applied to the first unit column gives a column with both properties.

**The leading WKB approximation.** After the onset write $Q = k_{(5)} = q_5e^{AHx_4}$ (at $y = 0$) and $\kappa = \sqrt{Q^2 - m^2}$. When $\kappa$ changes slowly, the wave follows the growing eigenvalue of $-ih$ at each instant; this is the **WKB approximation** (after Wentzel, Kramers and Brillouin). Line by line:

1. At each instant the growing eigenvalue of $-ih$ is $+\kappa$, so the size grows at the rate $\frac{d}{dx_4}\ln(u^\dagger u) \approx 2\kappa$, and $\ln(u^\dagger u) \approx 2W + $ const with $W(x_4) = \int\kappa\,dx_4$.
2. Since $dQ/dx_4 = AH\,Q$, the substitution $dx_4 = dQ/(AHQ)$ gives $W = \frac{1}{AH}\int\frac{\sqrt{Q^2 - m^2}}{Q}\,dQ$.
3. This integral is $W = \frac{1}{AH}\big(\sqrt{Q^2 - m^2} - m\arccos\frac mQ\big)$. To check it, differentiate the bracket with respect to $Q$: $\frac{d}{dQ}\sqrt{Q^2 - m^2} = \frac{Q}{\kappa}$, and $\frac{d}{dQ}\arccos\frac mQ = -\frac{1}{\sqrt{1 - m^2/Q^2}}\cdot\big(-\frac{m}{Q^2}\big) = \frac{m}{Q\kappa}$; so the derivative of the bracket is $\frac{Q}{\kappa} - \frac{m^2}{Q\kappa} = \frac{Q^2 - m^2}{Q\kappa} = \frac{\kappa}{Q}$, the integrand.

**The first-order WKB correction.** The matrices $A_4 = -i\gamma^{(4)}$ and $M = -i\gamma^{(4)}\gamma^{(5)}$ are Hermitian, square to $I_{16}$ ($(-i\gamma^{(4)})^2 = -(\gamma^{(4)})^2 = I_{16}$; $(\gamma^{(4)}\gamma^{(5)})^2 = -(\gamma^{(4)})^2(\gamma^{(5)})^2 = -I_{16}$, so $M^2 = I_{16}$) and anticommute, and with $q_1 = 0$, $h = mA_4 - iQM$. Line by line:

1. Take a column $w$ with $A_4w = w$; then $A_4(Mw) = -MA_4w = -Mw$, and $h$ maps the plane spanned by $w$ and $Mw$ into itself: $hw = mw - iQMw$ and $h(Mw) = -mMw - iQw$. For $u = v_1w + v_2Mw$ the equation $du/dx_4 = -ihu$ becomes $v' = \begin{pmatrix}-im & -Q \\ -Q & im\end{pmatrix}v$ (there are 8 such planes).
2. This symmetric $2 \times 2$ matrix has the eigenvalues $\pm\kappa$ (its determinant condition is $(-im - \lambda)(im - \lambda) - Q^2 = \lambda^2 + m^2 - Q^2 = 0$) and, for $+\kappa$, the eigenvector $r = (Q, -\kappa - im)$ (the first row gives $(-im - \kappa)Q - Q(-\kappa - im) = 0$).
3. Keep only the growing part, $v \approx c\,r$. Then $v' = c'r + cr' \approx \kappa cr$; multiplying from the left by the row $r^T$ and writing $n = r^Tr$ gives $c'n + c\,r^Tr' = \kappa cn$, and $r^Tr' = n'/2$ (the derivative of $r^Tr$ is $2r^Tr'$ for a symmetric product). So $c'/c = \kappa - n'/(2n)$.
4. $n = Q^2 + (\kappa + im)^2 = Q^2 + \kappa^2 - m^2 + 2im\kappa = 2\kappa(\kappa + im)$, using $Q^2 - m^2 = \kappa^2$; its size is $|n| = 2\kappa\sqrt{\kappa^2 + m^2} = 2\kappa Q$.
5. Integrating line 3, $\ln c = W - \frac12\ln n + $ const, so $|c|^2 \propto e^{2W}/|n| = e^{2W}/(2\kappa Q)$. The size of the column is $|c|^2r^\dagger r = |c|^2(Q^2 + \kappa^2 + m^2) = |c|^2\cdot 2Q^2$, so $u^\dagger u \propto e^{2W}Q/\kappa$, and
$$
\ln(u^\dagger u) \approx 2W + \ln\frac{Q}{\kappa} + \text{const}, \qquad \frac{d}{dx_4}\ln(u^\dagger u) \approx 2\kappa - \frac{AH\,m^2}{\kappa^2},
$$
because $\frac{d}{dx_4}\ln Q = AH$ and $\frac{d}{dx_4}\ln\kappa = \frac{Q}{\kappa^2}\frac{dQ}{dx_4} = AH\frac{Q^2}{\kappa^2}$, whose difference is $AH\frac{\kappa^2 - Q^2}{\kappa^2} = -\frac{AHm^2}{\kappa^2}$.

**What the computation shows (COMPUTED).** Both approximations fail at the onset itself, where $\kappa \to 0$, so Notebook 08b compares increases over a window from 1.5 to 3 time units after the onset (the unknown constants drop out of increases). For $q_5 = 0.05$ the RK4 solution of the model increases $\ln(u^\dagger u)$ by 31.0009 over the window; the leading WKB formula gives 31.0328 (relative difference $1.03 \times 10^{-3}$) and the first-order formula 31.0085 (relative difference $2.48 \times 10^{-4}$); for $q_5 = 0.1$ the numbers are 30.9993, 31.0312 and 31.0069. Late in the run the growth rate computed from the solution is 40.09851 and the first-order prediction 40.09868 (agreement to $10^{-5}$). The RK4 solution itself is accurate to $10^{-8}$ (relative), and halving the step divides its error by 15.89, close to the value 16 of a fourth-order method. Before the onset the size does not stay exactly 1: with extra-time momentum the mode matrix is not Hermitian, so the Hilbert norm is not conserved (Section 8.19), and the size $u^\dagger u$, which starts at 1, has grown to 1.52 ($q_5 = 0.05$) and 1.54 ($q_5 = 0.1$) when the onset is reached. Three time units after the onset $\ln(u^\dagger u) = 37.071$ for $q_5 = 0.05$, that is $u^\dagger u \approx 1.26 \times 10^{16}$, while the Krein form stays constant to rounding (its change divided by $\max(u^\dagger u, 1)$ stays below $10^{-9}$). Because the rate $2\kappa \approx 2q_5e^{AHx_4}$ itself grows exponentially, the growth is faster than any exponential.

### 8.26 Example: the onset of growth along the deflating history

Notebook 08b puts Sections 8.24 and 8.25 to work along the prescribed history of the Kohn-Sham record. It reads $A$, $H$, $m$ and $L$ from the record; checks exactly that $dy/dx_8 = \cot z$, $e^{Hy} = \sin^{1/6}z$ and that the product of the scale factors is $\cos z$ for every $a_4$; draws the scale factors along the history; computes the frame momenta and the exact onset time and compares it with a numerical root search; shows that the onset time is finite for every $q_5 > 0$; builds the model's mode matrix, checks $h(x_4)^2 = E^2(x_4)I_{16}$ against the record's formula, chooses clean starting columns, follows two waves through the onset with RK4 (with a convergence test), and compares with both WKB formulas; and checks the Krein form. It needs no Rust and runs in well under a minute; the times measured on the build computer, which depend on how busy that computer is, are recorded in the notebook's provenance file `Revision/textbook/notebooks/08b_deflation_onset.PROVENANCE.md`. It ends with the line ALL 25 CHECKS PASSED (notebook 08b).

<!-- NOTEBOOK 08b -->

### 8.29 Line-by-line walk-through of Notebook 08b

The notebook has 12 code cells, In [1] to In [12]. The conventions are those of Section 8.15; captions shortened to `...` are printed in full in Section 8.28.

**In [1], the set-up cell.** It is the set-up cell explained in Section 8.15, with the line `NOTEBOOK_ID = "08b"  # this notebook: chapter 08, example b`; its comment lines are the run instructions of Section 8.27. Output: `Set-up of notebook 08b complete: repository folder found, helpers defined.`

**In [2], the record helpers and the history of the Kohn-Sham record.** The cell starts with the imports of numpy and sympy, the empty table `REPORTS` and the two helpers `record_says` and `check_record`, word for word those of Notebook 08a (Section 8.23; `check_record` takes one check name). Then:

```python
parameters = json.loads(repository_file(
    "Revision/kohn_sham/results/parameters.json").read_text(encoding="utf-8"))
H = parameters["physics"]["H"]  # the author's constant H
mass = parameters["physics"]["m"]  # the mass m
A = parameters["physics"]["historyA"]  # the history a4 = A H x4
L_tip = parameters["physics"]["L_tipCutoff"]  # the record cuts the tip at y = -L
```

The parameters of the Kohn-Sham record are read; the four numbers are taken from its part `physics` (a dictionary inside the dictionary; two square brackets reach into it).

```python
say("history: " + parameters["theoryInputs"]["adiabaticityHistory"])
say("status: " + parameters["conventions"]["history"].split(". ")[0] + ".")
check(H == 1.0 and mass == 1.0 and A == 1.0 and L_tip == 3.0,
      "the canonical history: A = 1, H = 1, m = 1, tip cutoff L = 3",
      record="Revision/kohn_sham/results/parameters.json, physics.historyA, "
             "physics.H, physics.m, physics.L_tipCutoff")
```

The first line prints the record's description of the history: `a4 = A H x4 (A = 1 canonical), a4' = A H; slices a4,0 = a4(x4); PRESCRIBED BACKGROUND (see historyStatus)`. The second prints the first sentence of the record's statement of its status (`split(". ")` cuts the text at every full stop followed by a blank, `[0]` takes the first piece, and the full stop is added back): `PRESCRIBED BACKGROUND: the history a4 = A H x4 is prescribed, not solved for.` The check confirms the four values and names the record entries it reproduces.

```python
def a4_of(x4):
    """The prescribed deflating history a4 = A H x4."""
    return A * H * x4
```

`a4_of` returns $a_4 = AHx_4$; it works for a single time and for a whole numpy array of times. Output of the cell: the two lines and one PASS line with its `reproduces` line.

**In [3], the scale factors and the constant volume.**

```python
x8, H_symbol = sp.symbols("x8 H", positive=True)
a4_symbol = sp.Symbol("a4", real=True)
z = 6 * H_symbol * x8
y_of_x8 = sp.log(sp.sin(z)) / (6 * H_symbol)  # the hidden coordinate y
check(sp.simplify(sp.diff(y_of_x8, x8) - sp.cot(z)) == 0, "dy/dx8 = cot z")
check(sp.simplify(sp.exp(H_symbol * y_of_x8) - sp.sin(z) ** sp.Rational(1, 6)) == 0,
      "e^(H y) = sin(z)^(1/6)")
```

Exact symbols for $x_8$, $H$ and $a_4$ (here a plain number-like symbol, because only its value enters). `y_of_x8` is $y = \ln(\sin z)/(6H)$. The two checks are the two facts of Section 8.24: $dy/dx_8 = \cot z$ and $e^{Hy} = \sin^{1/6}z$.

```python
space_factor = sp.exp(a4_symbol) * sp.sin(z) ** sp.Rational(1, 6)  # x1, x2, x3
extra_factor = sp.exp(-a4_symbol) * sp.sin(z) ** sp.Rational(1, 6)  # x5, x6, x7
volume = space_factor**3 * 1 * extra_factor**3 * sp.cot(z)  # x4 has the factor 1
check_record(sp.simplify(volume - sp.cos(z)) == 0,
             "sqrt|g| = product of the scale factors = cos z, for every a4",
             "Revision/theory/reports/python-field-theory.json",
             "sqrt_det_g_equals_cos_z", "cos(6 H x8)")
```

The product of the eight scale factors is compared with $\cos z$ for a symbolic $a_4$, together with the record's check, whose detail contains `cos(6 H x8)`.

```python
times = np.linspace(0.0, 6.0, 601)
fig, ax = plt.subplots()
for y, style in ((0.0, "-"), (-1.0, "--")):
    warp = np.exp(H * y)  # sin^(1/6) z = e^(H y)
    ax.plot(times, np.exp(a4_of(times)) * warp, style, color="tab:blue",
            label=f"3-space $e^{{a_4}}e^{{Hy}}$, $y = {y}$")
    ax.plot(times, np.exp(-a4_of(times)) * warp, style, color="tab:red",
            label=f"extra times $e^{{-a_4}}e^{{Hy}}$, $y = {y}$")
    ax.plot(times, np.full_like(times, warp**6), style, color="black",
            linewidth=0.8, label=f"product of the six, $e^{{6Hy}}$, $y = {y}$")
```

601 times from 0 to 6. For the two hidden positions $y = 0$ (solid lines) and $y = -1$ (dashed), the cell draws the 3-space factor $e^{a_4}e^{Hy}$ (blue), the extra-time factor $e^{-a_4}e^{Hy}$ (red) and the product of the six, $e^{6Hy}$ (black; `np.full_like(times, value)` is an array of the same length filled with the value). In an f-string a curly bracket that must appear in the text is written twice, so `e^{{a_4}}` prints as `e^{a_4}`.

```python
ax.set_yscale("log")
ax.set_xlabel("time $x_4$ (units of $1/m$)")
ax.set_ylabel("scale factor")
ax.set_title("Scale factors along the history $a_4 = x_4$")
ax.legend(fontsize=7, loc="upper left");
save_figure(fig, "scale_factors",
            "The scale factors of the author's metric along the prescribed "
            ...
            "change in time.")
```

A logarithmic vertical axis, labels, a small legend, and Figure 08b.1. Output: three PASS lines (one with its `reproduces` line) and the figure line.

**What Figure 08b.1 shows.** The scale factors (pure numbers, logarithmic vertical axis) against the time $x_4$ from 0 to 6 (units of $1/m$), along $a_4 = x_4$, at $y = 0$ (solid) and $y = -1$ (dashed). Blue: 3-space, a rising straight line from $e^{Hy}$ to $e^{6}e^{Hy}$. Red: the extra times, a falling straight line from $e^{Hy}$ to $e^{-6}e^{Hy}$. Black: the product of the six, a horizontal line at $e^{6Hy}$ (1 at $y = 0$, $e^{-6}$ at $y = -1$). The student should see exponential inflation of 3-space, exponential deflation of the extra times, and a product that does not change in time.

**In [4], frame momenta and the onset.**

```python
def frame_momenta(x4, q1, q5, y):
    """(k_(1), k_(5)) of the wave exp(i (q1 x1 + q5 x5)) at time x4 and position y."""
    w = np.exp(-H * y)  # e^(-H y) = sin^(-1/6) z
    return q1 * np.exp(-a4_of(x4)) * w, q5 * np.exp(a4_of(x4)) * w


def local_E2(x4, q1, q5, y):
    """E^2 = m^2 + k_(1)^2 - k_(5)^2 with frozen coefficients."""
    k1, k5 = frame_momenta(x4, q1, q5, y)
    return mass**2 + k1**2 - k5**2
```

`frame_momenta` returns the pair $(k_{(1)}, k_{(5)})$ of Section 8.24, lines 1 and 2; `local_E2` returns $E^2$ of line 3 (a function may return two values, which the caller unpacks into two names).

```python
def onset_time(q1, q5, y):
    """The exact time at which E^2 = 0 (positive root of the quadratic in X)."""
    w = np.exp(-H * y)
    X = (mass**2 + np.sqrt(mass**4 + 4 * q1**2 * q5**2 * w**4)) / (2 * q5**2 * w**2)
    return np.log(X) / (2 * A * H)
```

`onset_time` is the formula $x_4^\ast = \ln(X^\ast)/(2AH)$ with the positive root $X^\ast$ of Section 8.24.

```python
def bisection(q1, q5, y, low=-30.0, high=30.0):
    """The time at which E^2 changes sign, by halving [low, high] 200 times."""
    for _ in range(200):
        middle = (low + high) / 2
        if local_E2(middle, q1, q5, y) > 0:  # still oscillating: onset is later
            low = middle
        else:
            high = middle
    return (low + high) / 2
```

`bisection` finds the same time independently, by the **bisection method**: start with an interval $[-30, 30]$ in which $E^2$ changes sign; look at the middle; if $E^2$ is still positive there, the onset is later and the middle becomes the new left end, otherwise the new right end; after 200 halvings the interval is far smaller than the rounding of the numbers, and its middle is returned. (`low=-30.0` gives a default value used when the caller does not pass one.)

```python
worst = max(abs(onset_time(q1, q5, y) - bisection(q1, q5, y))
            for q1 in (0.0, 0.5, 1.0, 3.0) for q5 in (0.01, 0.05, 0.1, 0.4)
            for y in (0.0, -1.0, -3.0))
check(worst < 1e-12, "the exact onset time equals the bisection result (48 waves)")
check(abs(onset_time(0.0, 0.05, 0.0) - np.log(1 / 0.05)) < 1e-14,
      "q1 = 0, y = 0: onset time = ln(m/q5)")
for q5 in (0.05, 0.1):
    report(f"onset time for q1 = 0, q5 = {q5}, y = 0", f"{onset_time(0.0, q5, 0.0):.6f}")
```

The two methods are compared for $4 \times 4 \times 3 = 48$ waves (four values of $q_1$, four of $q_5$, three positions); the largest difference must be below $10^{-12}$. The second check is the simple form $x_4^\ast = \ln(m/q_5)$ for $q_1 = 0$, $y = 0$ (with $m = 1$). The RESULT lines print 2.995732 ($\ln 20$) and 2.302585 ($\ln 10$). Output: two PASS lines and two RESULT lines.

**In [5], the frame momenta and the local $E^2$ along the history.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
k1_path, k5_path = frame_momenta(times, 0.1, 0.1, 0.0)
left.plot(times, k5_path, color="tab:red", label="extra time: $k_{(5)} = q_5e^{a_4}$")
left.plot(times, k1_path, color="tab:blue", label="3-space: $k_{(1)} = q_1e^{-a_4}$")
left.axhline(mass, color="black", linewidth=0.8, linestyle=":", label="$m$")
left.set_yscale("log")
left.set_xlabel("time $x_4$")
left.set_ylabel("frame momentum (units of $m$)")
left.set_title("$q_1 = q_5 = 0.1$, $y = 0$")
left.legend(fontsize=8)
```

The left panel draws the two frame momenta of the wave with $q_1 = q_5 = 0.1$ at $y = 0$ along the 601 times, on a logarithmic axis, with a dotted line at the mass.

```python
for q1, q5, style in ((0.0, 0.02, "-"), (0.0, 0.05, "-"), (0.0, 0.1, "-"),
                      (0.0, 0.2, "-"), (1.0, 0.05, "--")):
    right.plot(times, local_E2(times, q1, q5, 0.0), style,
               label=f"$q_1 = {q1}$, $q_5 = {q5}$")
    t_star = onset_time(q1, q5, 0.0)
    right.plot([t_star], [0.0], "o", color="black", markersize=4)
right.axhline(0.0, color="black", linewidth=0.8)
right.set_ylim(-4.0, 2.5)
right.set_xlabel("time $x_4$")
right.set_ylabel("$E^2 = m^2 + k_{(1)}^2 - k_{(5)}^2$")
right.set_title("Local $E^2$ along the history, $y = 0$")
right.legend(fontsize=8, loc="lower left");
save_figure(fig, "frame_momenta",
            "Left: the frame momenta of one wave with coordinate wave numbers "
            ...
            "onset is almost that of the same wave with $q_1 = 0$.")
```

The right panel draws the local $E^2$ of five waves (four with $q_1 = 0$, one dashed with $q_1 = 1$) and marks each onset time with a black dot on the zero line. The figure is Figure 08b.2; the cell prints only the figure line.

**What Figure 08b.2 shows.** Left: the frame momenta (units of $m$, logarithmic axis) against the time $x_4$ for $q_1 = q_5 = 0.1$ at $y = 0$: the red line $k_{(5)} = 0.1e^{x_4}$ rises and crosses the dotted mass line at $x_4 = \ln 10 \approx 2.3$; the blue line $k_{(1)} = 0.1e^{-x_4}$ falls. Right: the local $E^2$ (units of $m^2$) of five waves: each starts near 1, decreases, crosses zero once at its onset (black dot) and stays negative; smaller $q_5$ cross later. The dashed wave with $q_1 = 1$ starts at $E^2 = 1 + 1 - 0.0025 \approx 2$, but its space term dies away like $e^{-2a_4}$, and its onset (2.997) is almost that of the wave with $q_1 = 0$, $q_5 = 0.05$ (2.996). The student should see that the deflation drives every wave from oscillation into growth.

**In [6], every wave along an extra time reaches the onset.**

```python
q5_grid = np.logspace(-4.0, 0.0, 200)  # 10^-4 ... 1, equally spaced on a log axis
fig, ax = plt.subplots()
all_finite_and_decreasing = True
for q1, y, style in ((0.0, 0.0, "-"), (0.0, -1.0, "--"), (0.0, -L_tip, ":"),
                     (1.0, 0.0, "-.")):
    onsets = onset_time(q1, q5_grid, y)
    all_finite_and_decreasing &= bool(np.all(np.isfinite(onsets))
                                      and np.all(np.diff(onsets) < 0))
    ax.plot(q5_grid, onsets, style, label=f"$q_1 = {q1}$, $y = {y}$")
```

`np.logspace(-4.0, 0.0, 200)` gives 200 values of $q_5$ from $10^{-4}$ to $1$, equally spaced on a logarithmic axis. For four cases (three hidden positions, including the tip cutoff $y = -3$, and one wave with $q_1 = 1$) the onset times are computed for the whole grid at once. `np.isfinite` is true for an ordinary number (not infinite, not "not a number"); `np.diff` gives the differences of neighbours, which must all be negative (the onset time decreases as $q_5$ grows). `&=` keeps the variable true only while every case passes.

```python
ax.set_xscale("log")
ax.set_xlabel("coordinate wave number $q_5$ along the extra time $x_5$")
ax.set_ylabel("onset time $x_4^\\ast$ (units of $1/m$)")
ax.set_title("Every extra-time wave reaches the onset")
ax.legend();
save_figure(fig, "onset_times",
            "The onset time $x_4^\\ast$ at which a wave with coordinate wave number "
            ...
            "$x_4 = 0$.")
check_record(all_finite_and_decreasing,
             "the onset time is finite for every q5 > 0 on the grid and decreases "
             "with q5", "Revision/theory/reports/python-field-theory.json",
             "extra_time_modes_grow",
             "every extra-time mode eventually enters the growing regime")
```

A logarithmic horizontal axis, labels, Figure 08b.3, and the check, which requires the record's sentence "every extra-time mode eventually enters the growing regime". Output: the figure line and one PASS line with its `reproduces` line.

**What Figure 08b.3 shows.** The onset time $x_4^\ast$ (vertical, units of $1/m$) against the coordinate wave number $q_5$ from $10^{-4}$ to 1 (horizontal, logarithmic). Each curve is a falling, nearly straight line: on a logarithmic $q_5$ axis, $x_4^\ast = (Hy + \ln(m/q_5))/(AH)$ is a straight line of slope $-1$ per factor $e$. At $q_5 = 10^{-4}$ and $y = 0$ the onset is at $\ln 10^4 \approx 9.2$; the curve for $y = -1$ lies one unit lower and that for $y = -3$ three units lower (for large $q_5$ these are negative: such waves grow already at $x_4 = 0$); the curve with $q_1 = 1$ lies on top of the $y = 0$ curve except at the largest $q_5$. The student should see that no curve goes to infinity: however small $q_5$ is, the onset comes.

**In [7], the model's mode matrix and the starting columns.**

```python
gammas_record = json.loads(
    repository_file("Revision/algebra/gammas.json").read_text(encoding="utf-8"))
GAMMA = [np.array(rows, dtype=int) for rows in gammas_record["gamma"]]
C = np.array(gammas_record["C"], dtype=int)  # C = g^(x8) g^(x1) g^(x2) g^(x3)
B = np.array(gammas_record["B"]["re"]) + 1j * np.array(gammas_record["B"]["im"])
g4 = GAMMA[3].astype(complex)  # gamma^(x4)
g4g1 = (GAMMA[3] @ GAMMA[0]).astype(complex)  # gamma^(x4) gamma^(x1)
g4g5 = (GAMMA[3] @ GAMMA[4]).astype(complex)  # gamma^(x4) gamma^(x5)
check(np.array_equal(C @ GAMMA[3], GAMMA[3] @ C) and
      np.array_equal(C @ GAMMA[4], GAMMA[4] @ C),
      "C commutes with gamma^(x4) and gamma^(x5)")
```

The gammas, $C$ and $B$ are read as in Notebook 08a; the three matrices of the model, $\gamma^{(4)}$, $\gamma^{(4)}\gamma^{(1)}$ and $\gamma^{(4)}\gamma^{(5)}$, are prepared as complex arrays. The check confirms that $C$ commutes with $\gamma^{(4)}$ and $\gamma^{(5)}$ (Section 8.25).

```python
def h_local(x4, q1, q5, y):
    """The mode matrix of the local-frame model at time x4."""
    k1, k5 = frame_momenta(x4, q1, q5, y)
    return -1j * mass * g4 - k1 * g4g1 - k5 * g4g5
```

`h_local` is the model's mode matrix $h(x_4) = -im\gamma^{(4)} - k_{(1)}(x_4)\gamma^{(4)}\gamma^{(1)} - k_{(5)}(x_4)\gamma^{(4)}\gamma^{(5)}$.

```python
# At every instant h(x4)^2 = E^2(x4) I16, where E^2 is the frozen-coefficient E^2 of
# the record with k1 = k_(1)(x4), k5 = k_(5)(x4) and all other momenta 0.
m_s = sp.Symbol("m", real=True)
k_s = {a: sp.Symbol(f"k{a}", real=True) for a in (1, 2, 3, 5, 6, 7, 8)}
E2_record = m_s**2 + sum(k_s[a] ** 2 for a in (1, 2, 3, 8)) \
    - sum(k_s[a] ** 2 for a in (5, 6, 7))
```

`E2_record` is the record's general formula $E^2 = m^2 + k_1^2 + k_2^2 + k_3^2 + k_8^2 - k_5^2 - k_6^2 - k_7^2$, built with exact symbols.

```python
squares_ok = True
for x4 in (0.0, 1.0, 2.0, 3.0, 4.0):
    k1_now, k5_now = frame_momenta(x4, 0.3, 0.1, 0.0)  # q1 = 0.3, q5 = 0.1, y = 0
    values = {symbol: 0 for symbol in k_s.values()}  # every momentum 0 ...
    values.update({m_s: mass, k_s[1]: k1_now, k_s[5]: k5_now})  # ... but these
    E2_now = float(E2_record.subs(values))
    h_now = h_local(x4, 0.3, 0.1, 0.0)
    squares_ok &= bool(np.allclose(h_now @ h_now, E2_now * np.eye(16), atol=1e-12)
                       and abs(E2_now - local_E2(x4, 0.3, 0.1, 0.0)) < 1e-12)
check_record(squares_ok, "x4 = 0, 1, 2, 3, 4: h(x4)^2 = E^2(x4) I16 (q1 = 0.3, "
             "q5 = 0.1)", "Revision/theory/reports/python-scope.json",
             "extra_time_growth_rates_unbounded", f"h_k^2 = ({sp.sstr(E2_record)}) I16")
```

At five instants, for the wave $q_1 = 0.3$, $q_5 = 0.1$, the record's formula is evaluated with the frame momenta of that instant (a dictionary sets every momentum to 0, and `update` then sets the mass, $k_1$ and $k_5$), and the square of the model's matrix is compared with $E^2I_{16}$ to $10^{-12}$; the value must also agree with `local_E2`. The check requires the record's text with the general $E^2$.

```python
def starting_column(q5, sign):
    """A unit column with h(0) u = E0 u and C u = sign u (q1 = 0, y = 0)."""
    h0 = h_local(0.0, 0.0, q5, 0.0)
    E0 = np.sqrt(mass**2 - q5**2)
    first = np.zeros(16, dtype=complex)
    first[0] = 1.0  # the first unit column
    u = (np.eye(16) + h0 / E0) @ ((np.eye(16) + sign * C) @ first) / 4
    return u / np.linalg.norm(u), h0, E0
```

`starting_column` applies the two projectors of Section 8.25, $\frac12(I + \sigma C)$ and $\frac12(I + h(0)/E_0)$ (together the factor $\frac14$), to the first unit column (a column of zeros with a 1 in position 0) and divides by the length.

```python
starts = {}
for q5, sign in ((0.05, +1), (0.1, -1)):
    u0, h0, E0 = starting_column(q5, sign)
    starts[q5] = u0
    krein0 = np.vdot(u0, B @ u0)  # u^dagger B u
    report(f"q5 = {q5}: E0, Krein form of the start",
           f"{E0:.9f}, {krein0.real:+.9f}")
    sign_text = "+" if sign > 0 else "-"  # the sign as a character
    check(np.linalg.norm(h0 @ u0 - E0 * u0) < 1e-14 and
          np.linalg.norm(C @ u0 - sign * u0) < 1e-14 and
          abs(krein0 - sign * E0 / mass) < 1e-14,
          f"q5 = {q5}: h(0) u = E0 u, C u = {sign_text}u, "
          f"Krein form = {sign_text}E0/m")
```

Two starting columns are made, for $q_5 = 0.05$ with $\sigma = +1$ and for $q_5 = 0.1$ with $\sigma = -1$, and stored in the dictionary `starts`. For each, the RESULT line prints $E_0$ and the Krein form ($0.998749218$ and $+0.998749218$; $0.994987437$ and $-0.994987437$), and the check confirms to $10^{-14}$ the three properties: eigenvector of $h(0)$ for $E_0$, eigenvector of $C$ for $\sigma$, Krein form $\sigma E_0/m$. Output: three PASS lines (one with its `reproduces` line) and two RESULT lines.

**In [8], RK4 through the onset.**

```python
def rk4_history(u0, q5, x4_end, steps):
    """RK4 for du/dx4 = -i h(x4) u (q1 = 0, y = 0); returns the times, u^dagger u,
    u^dagger B u after every step, and the final column."""
    step = x4_end / steps
    u = u0.copy()
    times_out = [0.0]
    hilbert = [np.vdot(u, u).real]
    krein = [np.vdot(u, B @ u)]

    def rate(x4, v):  # the right-hand side -i h(x4) v
        return -1j * (h_local(x4, 0.0, q5, 0.0) @ v)
```

`rk4_history` solves the model with RK4 and records, after every step, the time, the Hilbert norm and the Krein form (`u0.copy()` makes a copy, so that the starting column itself is not changed). The inner function `rate` is the right-hand side $-ih(x_4)v$; unlike In [8] of Notebook 08a the matrix now depends on the time.

```python
    for n in range(steps):
        x4 = n * step
        s1 = rate(x4, u)
        s2 = rate(x4 + step / 2, u + step / 2 * s1)
        s3 = rate(x4 + step / 2, u + step / 2 * s2)
        s4 = rate(x4 + step, u + step * s3)
        u = u + step / 6 * (s1 + 2 * s2 + 2 * s3 + s4)
        times_out.append((n + 1) * step)
        hilbert.append(np.vdot(u, u).real)
        krein.append(np.vdot(u, B @ u))
    return np.array(times_out), np.array(hilbert), np.array(krein), u
```

The classical RK4 step for an equation whose right-hand side depends on the time: the four slopes are taken at the start, twice at the middle and at the end of the step. The function returns three arrays and the final column.

```python
runs = {}
for q5 in (0.05, 0.1):
    x4_end = onset_time(0.0, q5, 0.0) + 3.0
    runs[q5] = rk4_history(starts[q5], q5, x4_end, 12000)
    at_onset = np.searchsorted(runs[q5][0], onset_time(0.0, q5, 0.0))  # its index
    report(f"q5 = {q5}: u^dagger u at the onset", f"{runs[q5][1][at_onset]:.2f}")
    final_size = runs[q5][1][-1]  # u^dagger u at the end of the run
    report(f"q5 = {q5}: ln(u^dagger u) at the onset + 3", f"{np.log(final_size):.6f}")
```

Each wave is followed from $x_4 = 0$ to three time units after its onset with 12000 steps; the results are stored in `runs` (for each wave the four results of `rk4_history`: `runs[q5][0]` is the array of the times, `runs[q5][1]` the array of the sizes $u^\dagger u$). `np.searchsorted(runs[q5][0], onset_time(0.0, q5, 0.0))` is the position of the first recorded time that is not earlier than the onset time, that is the first step at or after the onset; the first RESULT line of each wave prints the size $u^\dagger u$ there, with two decimals: 1.52 for $q_5 = 0.05$ and 1.54 for $q_5 = 0.1$. The size started at 1, so before the onset it grows only slowly, by about half (the mode matrix is not Hermitian, so the size is not conserved; Section 8.19). The second RESULT line of each wave prints $\ln(u^\dagger u)$ at the end of the run: 37.071245 and 37.113916.

```python
x4_end = onset_time(0.0, 0.05, 0.0) + 3.0
end_6000 = rk4_history(starts[0.05], 0.05, x4_end, 6000)[3]
end_24000 = rk4_history(starts[0.05], 0.05, x4_end, 24000)[3]
end_12000 = runs[0.05][3]
ratio = np.linalg.norm(end_6000 - end_12000) / np.linalg.norm(end_12000 - end_24000)
relative_error = np.linalg.norm(end_12000 - end_24000) / np.linalg.norm(end_24000)
report("RK4 error ratio (6000 vs 12000) / (12000 vs 24000) steps", f"{ratio:.2f}")
check(14.0 < ratio < 18.0, "RK4 converges with order 4 (error ratio near 16)")
check(relative_error < 1e-8, "the 12000-step run is accurate to 1e-8 (relative)")
```

The convergence test: the run with $q_5 = 0.05$ is repeated with 6000 and 24000 steps (`[3]` takes the final column). For a fourth-order method the difference between 6000 and 12000 steps is about $2^4 = 16$ times the difference between 12000 and 24000 steps; the ratio printed is 15.89, and the check requires it between 14 and 18. The difference between 12000 and 24000 steps, relative to the length of the column, estimates the error of the 12000-step run; it must be below $10^{-8}$. Output of the whole cell: five RESULT lines and two PASS lines.

**In [9], the WKB formulas and the comparison.**

```python
def Q_of(x4, q5):
    return q5 * np.exp(a4_of(x4))  # the frame momentum k_(5) at y = 0


def kappa_of(x4, q5):
    return np.sqrt(Q_of(x4, q5) ** 2 - mass**2)


def W_of(x4, q5):
    Q = Q_of(x4, q5)
    return (np.sqrt(Q**2 - mass**2) - mass * np.arccos(mass / Q)) / (A * H)
```

The three functions of Section 8.25: $Q = q_5e^{a_4}$, $\kappa = \sqrt{Q^2 - m^2}$ and $W = \frac{1}{AH}(\sqrt{Q^2 - m^2} - m\arccos(m/Q))$ (`np.arccos` is the inverse cosine).

```python
comparison = {}
for q5 in (0.05, 0.1):
    x4s, hilbert, krein, _ = runs[q5]
    start = np.searchsorted(x4s, onset_time(0.0, q5, 0.0) + 1.5)  # window start
    xa, xb = x4s[start], x4s[-1]
    increase = np.log(hilbert[-1]) - np.log(hilbert[start])
    leading = 2 * (W_of(xb, q5) - W_of(xa, q5))
    first = leading + np.log(Q_of(xb, q5) / kappa_of(xb, q5)) \
        - np.log(Q_of(xa, q5) / kappa_of(xa, q5))
    comparison[q5] = (xa, increase, leading, first)
```

For each run the window starts at the first recorded time 1.5 units after the onset (`np.searchsorted` finds the position at which a value would be inserted into a sorted array) and ends at the last time. `increase` is the increase of $\ln(u^\dagger u)$ over the window in the RK4 solution; `leading` is the leading WKB increase $2(W(x_b) - W(x_a))$; `first` adds the first-order correction $\ln(Q/\kappa)$ at the two ends. The four numbers are stored for the plot.

```python
    say(f"q5 = {q5}: window {xa:.4f} to {xb:.4f}; increase of ln(u^dagger u) "
        f"{increase:.4f}, leading WKB {leading:.4f} (relative difference "
        f"{abs(increase - leading) / increase:.2e}), first order {first:.4f} "
        f"(relative difference {abs(increase - first) / increase:.2e})")
    check(abs(increase - leading) / increase < 2e-3,
          f"q5 = {q5}: leading WKB agrees to 2e-3 over the window")
    check(abs(increase - first) < abs(increase - leading) and
          abs(increase - first) / increase < 5e-4,
          f"q5 = {q5}: first-order WKB is better and agrees to 5e-4")
```

The comparison is printed (the numbers quoted in Section 8.25), and two checks per wave require the leading formula to agree to $2 \times 10^{-3}$ and the first-order formula to be better and to agree to $5 \times 10^{-4}$.

```python
x4s, hilbert, _, _ = runs[0.05]
step = x4s[1] - x4s[0]
late_rate = (np.log(hilbert[-1]) - np.log(hilbert[-3])) / (2 * step)  # centred
kappa_late = kappa_of(x4s[-2], 0.05)  # kappa at the middle of the centred difference
predicted = 2 * kappa_late - A * H * mass**2 / kappa_late**2
report("q5 = 0.05: computed late rate, predicted 2 kappa - m^2/kappa^2",
       f"{late_rate:.5f}, {predicted:.5f}")
check(abs(late_rate - predicted) / predicted < 1e-5,
      "the late growth rate equals 2 kappa - A H m^2/kappa^2 to 1e-5")
```

The growth rate at the end of the run is computed by a **centred difference**, the change of $\ln(u^\dagger u)$ over the last two steps divided by their length, which approximates the derivative at the middle point; the first-order prediction is evaluated at that middle point. RESULT: 40.09851 and 40.09868; the check requires a relative agreement better than $10^{-5}$. Output: two comparison texts, five PASS lines and one RESULT line.

**In [10], the growth of the size along the history.**

```python
fig, ax = plt.subplots()
for q5, colour in ((0.05, "tab:blue"), (0.1, "tab:orange")):
    x4s, hilbert, _, _ = runs[q5]
    xa, _, _, _ = comparison[q5]
    ax.plot(x4s, np.log(hilbert), color=colour, label=f"RK4, $q_5 = {q5}$")
    after = x4s >= onset_time(0.0, q5, 0.0) + 0.05
    shift = np.log(hilbert[np.searchsorted(x4s, xa)]) - 2 * W_of(xa, q5)
    ax.plot(x4s[after], 2 * W_of(x4s[after], q5) + shift, "--", color="black",
            linewidth=0.9)
    ax.axvline(onset_time(0.0, q5, 0.0), color=colour, linestyle=":", linewidth=0.9)
```

For both runs: $\ln(u^\dagger u)$ of the RK4 solution; the leading WKB curve $2W$, drawn from 0.05 units after the onset (`after` is a true/false array that selects those times) and shifted by a constant so that it agrees with the solution at the window start; and a dotted vertical line at the onset (`axvline`).

```python
ax.plot([], [], "--", color="black", linewidth=0.9, label="WKB $2W$ + const")
ax.set_xlabel("time $x_4$ (units of $1/m$)")
ax.set_ylabel("$\\ln(u^\\dagger u)$")
ax.set_title("A wave along an extra time, $a_4 = x_4$, $y = 0$")
ax.legend();
save_figure(fig, "growth_along_history",
            "The natural logarithm of the size $u^\\dagger u$ of a wave with "
            ...
            "the WKB curve $2W$ (black dashed, matched 1.5 units after the onset).")
```

An empty dashed line for the legend, labels, and Figure 08b.4; the cell prints only the figure line.

**What Figure 08b.4 shows.** The natural logarithm of $u^\dagger u$ (vertical, pure number) against the time $x_4$ (units of $1/m$) for the two waves $q_5 = 0.05$ (blue) and $q_5 = 0.1$ (orange). Before its onset (dotted vertical line at $\ln 10 \approx 2.30$ or $\ln 20 \approx 3.00$) each curve rises only slowly, from 0 to about 0.4 ($\ln 1.52 = 0.42$, $\ln 1.54 = 0.43$): the wave oscillates and its size grows only by about half, because with extra-time momentum the mode matrix is not Hermitian and the size is not conserved. After the onset the curve bends upwards ever more steeply and reaches about 37 three units later (a factor of about $10^{16}$), following the black dashed WKB curve. The student should see the switch from oscillation to growth at the predicted time, and growth that accelerates.

**In [11], the growth rate and the Krein form.**

```python
x4s, hilbert, krein, _ = runs[0.05]
step = x4s[1] - x4s[0]
computed_rate = (np.log(hilbert[2:]) - np.log(hilbert[:-2])) / (2 * step)
middle = x4s[1:-1]
after = middle > onset_time(0.0, 0.05, 0.0) + 0.02
drift = np.abs(krein - krein[0]) / np.maximum(hilbert, 1.0)
check(drift.max() < 1e-9, "the Krein form is conserved (drift below 1e-9)")
check(hilbert[-1] > 1e15, "the Hilbert norm grows by more than 10^15")
```

For the run with $q_5 = 0.05$: the growth rate at every inner time by centred differences (`hilbert[2:]` drops the first two values, `hilbert[:-2]` the last two, so the two arrays are shifted by two steps; `middle` are the middle times); `after` selects the times just after the onset; `drift` is the change of the Krein form divided by $\max(u^\dagger u, 1)$. The checks require the drift below $10^{-9}$ and a final size above $10^{15}$.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
fig.subplots_adjust(wspace=0.35)  # room for the label of the right panel
left.plot(middle, computed_rate, color="tab:blue", label="RK4 (centred differences)")
left.plot(middle[after], 2 * kappa_of(middle[after], 0.05), "--", color="black",
          label="$2\\kappa$")
left.plot(middle[after], 2 * kappa_of(middle[after], 0.05)
          - mass**2 / kappa_of(middle[after], 0.05) ** 2, ":", color="tab:red",
          label="$2\\kappa - m^2/\\kappa^2$")
left.set_ylim(-5.0, 45.0)
left.set_xlabel("time $x_4$")
left.set_ylabel("growth rate $d\\ln(u^\\dagger u)/dx_4$")
left.set_title("Growth rate, $q_5 = 0.05$")
left.legend(fontsize=8)
```

The left panel draws the computed growth rate with the two WKB rates (`subplots_adjust(wspace=0.35)` widens the gap between the panels).

```python
right.semilogy(x4s[1:], np.maximum(drift[1:], 1e-18), color="tab:green")
right.set_xlabel("time $x_4$")
right.set_ylabel("$|\\Delta(u^\\dagger Bu)| / \\max(u^\\dagger u, 1)$")
right.set_title("Krein form: change (rounding only)")
save_figure(fig, "rate_and_krein",
            "Left: the growth rate $d\\ln(u^\\dagger u)/dx_4$ of the wave with "
            ...
            "$10^{-9}$.")
```

The right panel draws the drift on a logarithmic axis (`semilogy`); a logarithm cannot show an exact zero, so zeros are raised to $10^{-18}$ (`np.maximum`). The figure is Figure 08b.5. Output: two PASS lines and the figure line.

**What Figure 08b.5 shows.** Left: the growth rate $d\ln(u^\dagger u)/dx_4$ (units of $m$) against the time $x_4$ (units of $1/m$): small before the onset at $x_4 \approx 3$ (it starts at 0 and stays below 1; on the vertical scale up to 45 this looks almost flat), then rising ever more steeply to about 40; the black dashed curve $2\kappa$ and the red dotted curve $2\kappa - m^2/\kappa^2$ start at the onset, where both fail ($\kappa \to 0$), and the computed rate approaches the red curve as $\kappa$ grows. Right: the change of the Krein form relative to $\max(u^\dagger u, 1)$, on a logarithmic axis: it stays below about $10^{-14}$ (the drops to $10^{-18}$ are exact zeros), the level of rounding errors. The student should see that the rate itself grows exponentially (growth faster than any exponential) while the Krein form is conserved.

**In [12], the last check.**

```python
for name in ("08b_1_scale_factors.png", "08b_2_frame_momenta.png",
             "08b_3_onset_times.png", "08b_4_growth_along_history.png",
             "08b_5_rate_and_krein.png"):
    check(output_file(f"{FIGURE_FOLDER}/{name}").is_file(),
          f"the figure file {name} exists")
all_checks_passed()
```

Five checks that the figure files exist, and the last line. The 25 checks come from the cells as follows: one in In [2], three in In [3], two in In [4], one in In [6], four in In [7], two in In [8], five in In [9], two in In [11] and five here (In [5] and In [10] have none). The last line reads `ALL 25 CHECKS PASSED (notebook 08b)`.

### 8.30 Changing the field variables: the rescaling $\Psi = \sin^{-1/2}z\,\chi$

Section 8.9 changed the frame. This section keeps the diagonal frame and changes the field variables instead: we write the field as a known function times a new field, $\Psi = w\,\chi$ with $w = \sin^{-1/2}z$, and ask which equation $\chi$ obeys.

**The derivative of the factor.** $w$ depends only on $x_8$. Line by line:

$$
\begin{aligned}
\partial_8 w &= -\tfrac12\sin^{-3/2}z\cdot\cos z\cdot 6H = -3H\sin^{-3/2}z\cos z, \\
\tan z\,\partial_8 w &= \frac{\sin z}{\cos z}\cdot\big(-3H\sin^{-3/2}z\cos z\big) = -3H\sin^{-1/2}z = -3H\,w .
\end{aligned}
$$

The first line is the chain rule (the power rule for $\sin^{-1/2}$, the derivative $\cos z$ of $\sin z$, and $dz/dx_8 = 6H$); the second multiplies by $\tan z = \sin z/\cos z$ and combines the powers of $\sin z$ ($\sin z\cdot\sin^{-3/2}z = \sin^{-1/2}z$).

**The term disappears.** For $\mu \neq 8$, $\partial_\mu(w\chi) = w\,\partial_\mu\chi$, because $w$ does not depend on $x_\mu$. For $\mu = 8$ the product rule gives $\partial_8(w\chi) = (\partial_8 w)\chi + w\,\partial_8\chi$. So, line by line,

$$
\begin{aligned}
\gamma^\mu D_\mu(w\chi) &= \sum_\mu\gamma^\mu\partial_\mu(w\chi) + 3H\gamma^{(8)}w\chi \\
&= w\sum_\mu\gamma^\mu\partial_\mu\chi + \tan z\,\gamma^{(8)}(\partial_8 w)\chi + 3H\gamma^{(8)}w\chi \\
&= w\sum_\mu\gamma^\mu\partial_\mu\chi + \big(-3Hw + 3Hw\big)\gamma^{(8)}\chi = w\sum_\mu\gamma^\mu\partial_\mu\chi .
\end{aligned}
$$

The first line uses $\gamma^\mu D_\mu = \gamma^\mu\partial_\mu + \gamma^\mu\Omega_\mu$ and $\gamma^\mu\Omega_\mu = 3H\gamma^{(8)}$ (Section 8.5); the second applies the two derivative rules, with $\gamma^{x_8} = \tan z\,\gamma^{(8)}$; the third inserts $\tan z\,\partial_8 w = -3Hw$. For every column $\chi$ of 16 functions the spin-connection term is gone: in the variables $\chi$ the derivative part of the field equation is $w\,\gamma^\mu\partial_\mu\chi$, with no term $3H\gamma^{(8)}$ (PROVED; `Revision/theory/reports/python-scope.json`, check `rescaling_removes_the_connection_term`, both engines). The frame factors $e^{\mp a_4}\sin^{-1/6}z$ and $\tan z$ stay: they are part of $\gamma^\mu$.

**The potential.** $S$ is quadratic in the field and $w$ is real, so $S[w\chi] = (w\chi)^\dagger C(w\chi) = w^2\,\chi^\dagger C\chi = S[\chi]/\sin z$ (because $w^2 = \sin^{-1}z$). With $U = \frac\lambda2S^2$, $U'(S[\Psi]) = \lambda S[\Psi] = \lambda S[\chi]/\sin z$. The field equation $\gamma^\mu D_\mu\Psi = (m + \lambda S[\Psi])\Psi$ becomes $w\,\gamma^\mu\partial_\mu\chi = (m + \lambda S[\chi]/\sin z)\,w\chi$, and dividing by $w > 0$:

$$
\gamma^\mu\partial_\mu\chi = \Big(m + \frac{\lambda S[\chi]}{\sin z}\Big)\chi .
$$

For $U = 0$ the term $3H\gamma^{(8)}$ is removed completely; for $U \neq 0$ it reappears in a new form, as the $x_8$-dependent coupling $\lambda S[\chi]/\sin z$ (PROVED; `python-scope.json`, check `rescaled_equation_quadratic_potential`, both engines).

**The weight moves into the measure.** The norm of a field along the hidden direction is $\int\cos z\,\Psi^\dagger\Psi\,dx_8$ ($\cos z = \sqrt{|g|}$ is the volume factor). In the new variables $\cos z\,\Psi^\dagger\Psi\,dx_8 = \cos z\,w^2\,\chi^\dagger\chi\,dx_8 = \cot z\,\chi^\dagger\chi\,dx_8 = \chi^\dagger\chi\,dy$, by $dy = \cot z\,dx_8$ (Section 8.24). So the norm of $\Psi$ is the plain $y$-integral of $\chi^\dagger\chi$.

**The scope of "the field equation contains $3H\gamma^{(8)}$".** Together with Section 8.9: the value $3H\gamma^{(8)}$ belongs to one frame (the diagonal one) AND to one choice of field variables ($\Psi$). A boosted frame removes it, and so does the rescaling. Interpretation (labelled as such, not a theorem): in the variables $\Psi$ with the measure $\cos z\,dx_8$ the term makes the hidden-direction operator $\tan z\,\partial_8 + 3H$ antisymmetric up to a boundary term (Section 8.32); in the variables $\chi$ with the measure $dy$ the plain $\partial_y$ has the same property without any $H$ term. The role of $3H$ therefore depends on the variables and the measure.

### 8.31 The two ends of the hidden direction and an exact family of solutions

**The two ends.** Proper length along the hidden direction is $\sqrt{g_{88}}\,dx_8 = \cot z\,dx_8 = dy$. The **tip** $z \to 0$ is $y \to -\infty$: infinitely far from every point. The **patch end** $z = \pi/2$ is $y = 0$: at the finite proper distance $|y|$ from the point $y$. At the patch end $g_{88} = \cot^2 z = 0$ and $\sqrt{|g|} = \cos z = 0$: the surface is degenerate, and the Revision record claims nothing about it and imposes no boundary condition there. (The Kohn-Sham record ASSUMES a **$Z_2$ brane** at $z = \pi/2$. A **brane** is a boundary surface of spacetime, here the surface $z = \pi/2$ where the author's coordinate patch ends; "$Z_2$" says that the patch is glued there to a mirror copy of itself, and the mirror fixes a boundary condition for the field at that surface. Chapter 14 works it out. This chapter does not use it.)

**An exact family.** For $U = 0$ and a field that depends only on $x_4$ and $x_8$, the field equation of Section 8.2 is $\gamma^{(4)}\partial_4\Psi + \tan z\,\gamma^{(8)}\partial_8\Psi + 3H\gamma^{(8)}\Psi = m\Psi$. The record gives a family of exact solutions (`Revision/theory/reports/python-field-theory.json`, check `exact_solution_family_x4_x8`):

$$
\Psi = \sin^\alpha z\;e^{Mx_4}\chi_0, \qquad M = -m\gamma^{(4)} + c\,\gamma^{(4)}\gamma^{(8)}, \qquad c = 3H(2\alpha + 1),
$$

with any real exponent $\alpha$ and any constant column $\chi_0$. We derive it line by line. First, $M^2$:

$$
\begin{aligned}
M^2 &= m^2(\gamma^{(4)})^2 - mc\big((\gamma^{(4)})^2\gamma^{(8)} + \gamma^{(4)}\gamma^{(8)}\gamma^{(4)}\big) + c^2\gamma^{(4)}\gamma^{(8)}\gamma^{(4)}\gamma^{(8)} \\
&= -m^2 - mc\big(-\gamma^{(8)} + \gamma^{(8)}\big) - c^2(\gamma^{(4)})^2(\gamma^{(8)})^2 \\
&= (c^2 - m^2)\,I_{16} = k^2I_{16}, \qquad k^2 = 9H^2(2\alpha + 1)^2 - m^2 .
\end{aligned}
$$

The first line multiplies out; the second uses $(\gamma^{(4)})^2 = -I_{16}$, $\gamma^{(4)}\gamma^{(8)}\gamma^{(4)} = -(\gamma^{(4)})^2\gamma^{(8)} = \gamma^{(8)}$ and, in the last term, one anticommutation and the two squares. As in Section 8.18, $M^2 = k^2I_{16}$ makes the exponential series collapse: $e^{Mx_4} = \cosh(kx_4)I_{16} + \frac{\sinh(kx_4)}{k}M$. Second, the equation. With $s = \sin z$: $\partial_8 s^\alpha = \alpha s^{\alpha-1}\cos z\cdot 6H$, so $\tan z\,\partial_8 s^\alpha = 6H\alpha\,s^\alpha$; and $\partial_4 e^{Mx_4} = Me^{Mx_4}$. Inserting, and dividing by the common factor $s^\alpha$:

$$
\begin{aligned}
&\gamma^{(4)}Me^{Mx_4}\chi_0 + 6H\alpha\,\gamma^{(8)}e^{Mx_4}\chi_0 + 3H\gamma^{(8)}e^{Mx_4}\chi_0 = \big(\gamma^{(4)}M + c\,\gamma^{(8)}\big)e^{Mx_4}\chi_0, \\
&\gamma^{(4)}M = -m(\gamma^{(4)})^2 + c(\gamma^{(4)})^2\gamma^{(8)} = m - c\,\gamma^{(8)}, \\
&\big(\gamma^{(4)}M + c\,\gamma^{(8)}\big)e^{Mx_4}\chi_0 = m\,e^{Mx_4}\chi_0 .
\end{aligned}
$$

The first line collects the two $\gamma^{(8)}$ terms ($6H\alpha + 3H = 3H(2\alpha + 1) = c$); the second multiplies out $\gamma^{(4)}M$; the third inserts it: the left side equals $m\Psi$ after the factor $s^\alpha$ is put back. So every member solves the field equation, for every history $a_4$ (nothing in the solution depends on $a_4$, because the term $3H\gamma^{(8)}$ does not; PROVED).

**Which members grow.** A member grows like $e^{kx_4}$ when $k^2 > 0$, that is when $3H|2\alpha + 1| > m$, and oscillates when $k^2 < 0$. The member $\alpha = -\frac12$ has $c = 0$, $M = -m\gamma^{(4)}$ without any $H$, and $k^2 = -m^2$: it oscillates with the frequency $m$. It is the rescaled field of Section 8.30, $\Psi = \sin^{-1/2}z\,\chi$ with $\chi$ independent of $x_8$ (PROVED; `python-scope.json`, check `rescaled_equation_quadratic_potential`, whose detail states this member). The member $\alpha = 0$, the fields that do not depend on $x_8$, has $k^2 = 9H^2 - m^2$ and grows exactly when $m < 3H$.

**Which members have a finite norm.** The norm of a member along the hidden direction is a function of $x_4$ times the integral of $\cos z\,\sin^{2\alpha}z$ over $x_8$ from the tip to the patch end (where $z = 6Hx_8 = \pi/2$, that is $x_8 = \pi/(12H)$). We substitute $s = \sin z$, so that $ds = 6H\cos z\,dx_8$. Line by line:

$$
\int_0^{\pi/(12H)}\cos z\,\sin^{2\alpha}z\,dx_8 = \frac{1}{6H}\int_0^1 s^{2\alpha}\,ds = \frac{1}{6H}\Big[\frac{s^{2\alpha+1}}{2\alpha + 1}\Big]_0^1 = \frac{1}{6H(2\alpha + 1)} \quad (2\alpha + 1 > 0).
$$

The first step changes the variable ($s$ runs from 0 to 1 as $x_8$ runs over the patch); the second takes the antiderivative of a power; the third evaluates it, and $s^{2\alpha+1} \to 0$ at $s = 0$ exactly when $2\alpha + 1 > 0$. For $2\alpha + 1 \le 0$ the integral diverges at the tip; at $\alpha = -\frac12$ it is $\int ds/s$, which grows like $\ln(1/\epsilon)$ as the lower limit $\epsilon$ goes to 0. So the member without $H$ has an infinite norm, and the growing members with a finite norm are those with $2\alpha + 1 > m/(3H)$ and $\alpha > -\frac12$.

**For every mass some member grows and has a finite norm.** Take $\alpha = m/(3H)$, which is $> -\frac12$. Then $2\alpha + 1 = (2m + 3H)/(3H)$, $c = 2m + 3H$, and $k^2 = (2m + 3H)^2 - m^2 = (2m + 3H - m)(2m + 3H + m) = (m + 3H)(3m + 3H) = 3(m + H)(m + 3H) > 0$ (a difference of two squares). The record states the case $\alpha = 0$, $m < 3H$; the statement for every mass is this book's own exact consequence of the record's family, proved here and checked by Notebook 08d (PROVED).

### 8.32 The boundary term at the patch end and the growing modes of the good sector

**The fields that do not depend on $x_8$.** Such a field of the good sector depends only on $x_4$, and the field equation, multiplied by $\gamma^{(4)}$ as in Section 8.16, becomes $i\,\partial_4\Psi = A\Psi$ with the constant matrix $A = -im\gamma^{(4)} + 3iH\gamma^{(4)}\gamma^{(8)}$, which is $i$ times the matrix $M$ of the family at $\alpha = 0$. Its square is $A^2 = -M^2 = (m^2 - 9H^2)I_{16}$, so for $m < 3H$ its eigenvalues are $\pm i\sqrt{9H^2 - m^2}$, eight each, and half of the modes grow; at $m = H = 1$ the eigenvalues are $\pm 2\sqrt2\,i$. $A$ is not Hermitian (its second term is anti-Hermitian, see below). These modes have the finite norm factor $\int_0^{\pi/(12H)}\cos(6Hx_8)\,dx_8 = \frac{1}{6H}$ (the case $\alpha = 0$ above). (PROVED; `python-scope.json`, check `good_sector_x8_independent_modes_without_boundary_condition`, both engines.) So even the good sector, without any extra-time dependence, contains growing modes of finite norm, as long as nothing is imposed at the patch end.

**The mode operator.** For fields of $x_4$ and $x_8$ (and $U = 0$), multiplying the field equation $\gamma^{(4)}\partial_4\Psi + \gamma^{(8)}(\tan z\,\partial_8 + 3H)\Psi = m\Psi$ from the left by $\gamma^{(4)}$ gives $-\partial_4\Psi + \gamma^{(4)}\gamma^{(8)}(\tan z\,\partial_8 + 3H)\Psi = m\gamma^{(4)}\Psi$, and multiplying by $-i$ and rearranging: $i\,\partial_4\Psi = h\Psi$ with the **mode operator**

$$
h = -im\gamma^{(4)} + i\gamma^{(4)}\gamma^{(8)}\big(\tan z\,\partial_8 + 3H\big) = A + P\,\partial_8, \qquad P = i\tan z\,\gamma^{(4)}\gamma^{(8)} .
$$

**Three matrix facts.** Let $M_8 = i\gamma^{(4)}\gamma^{(8)}$. The real matrix $\gamma^{(4)}\gamma^{(8)}$ is symmetric: $(\gamma^{(4)}\gamma^{(8)})^T = (\gamma^{(8)})^T(\gamma^{(4)})^T = \gamma^{(8)}(-\gamma^{(4)}) = \gamma^{(4)}\gamma^{(8)}$. Hence:

1. $P^\dagger = -i\tan z\,(\gamma^{(4)}\gamma^{(8)})^T = -P$: the coefficient of $\partial_8$ is anti-Hermitian.
2. $\cos z\,P = i\sin z\,\gamma^{(4)}\gamma^{(8)} = \sin z\,M_8$.
3. $(-im\gamma^{(4)})^\dagger = im(\gamma^{(4)})^T = -im\gamma^{(4)}$ (Hermitian) and $(3iH\gamma^{(4)}\gamma^{(8)})^\dagger = -3iH\gamma^{(4)}\gamma^{(8)}$ (anti-Hermitian), so $A - A^\dagger = 6iH\gamma^{(4)}\gamma^{(8)} = 6H\,M_8$, and $\cos z\,(A - A^\dagger) = 6H\cos z\,M_8 = (\partial_8\sin z)\,M_8$.

**The boundary identity.** For any two columns $u(x_8)$, $v(x_8)$, line by line (a prime is $\partial_8$ here):

$$
\begin{aligned}
\cos z\big[u^\dagger(hv) - (hu)^\dagger v\big] &= \cos z\,u^\dagger(A - A^\dagger)v + \cos z\big[u^\dagger Pv' - u'^\dagger P^\dagger v\big] \\
&= \cos z\,u^\dagger(A - A^\dagger)v + \cos z\big[u^\dagger Pv' + u'^\dagger Pv\big] \\
&= (\partial_8\sin z)\,u^\dagger M_8v + \sin z\big[u^\dagger M_8v' + u'^\dagger M_8v\big] = \partial_8\big(\sin z\,u^\dagger M_8v\big) .
\end{aligned}
$$

The first line inserts $h = A + P\partial_8$ and uses $(hu)^\dagger = u^\dagger A^\dagger + u'^\dagger P^\dagger$; the second uses fact 1; the third uses facts 3 and 2 and then recognises the product rule for the three factors $\sin z$, $u^\dagger$ and $v$ ($M_8$ is constant). (PROVED; `python-scope.json`, check `good_sector_hermiticity_up_to_the_brane_flux`, both engines.) Integrated over the hidden direction, the left side is the failure of $h$ to be symmetric for the norm $\int\cos z\,u^\dagger v\,dx_8$, and the right side gives the **boundary term** (or **flux**) $[\sin z\,u^\dagger M_8v]$, taken between the tip and the patch end. At the tip $\sin z \to 0$; at the patch end $\sin z = 1$, and the flux need not vanish: for a column with $\gamma^{(4)}\gamma^{(8)}u = u$ (such columns exist, because $(\gamma^{(4)}\gamma^{(8)})^2 = -(\gamma^{(4)})^2(\gamma^{(8)})^2 = I_{16}$ and the matrix is not $\pm I_{16}$), $u^\dagger M_8u = i\,u^\dagger u \neq 0$; the record's example has $u^\dagger u = 2$ and $u^\dagger M_8u = 2i$.

**The norm changes only through the patch end.** For a solution of $i\,\partial_4\Psi = h\Psi$ let $N(x_4) = \int_0^{\pi/(12H)}\cos z\,\Psi^\dagger\Psi\,dx_8$. Line by line:

$$
\begin{aligned}
\frac{dN}{dx_4} &= \int\cos z\big[(\partial_4\Psi)^\dagger\Psi + \Psi^\dagger\partial_4\Psi\big]dx_8 = \int\cos z\big[(-ih\Psi)^\dagger\Psi + \Psi^\dagger(-ih\Psi)\big]dx_8 \\
&= -i\int\cos z\big[\Psi^\dagger(h\Psi) - (h\Psi)^\dagger\Psi\big]dx_8 = -i\big[\sin z\,\Psi^\dagger M_8\Psi\big]_{\text{tip}}^{\text{end}} \\
&= -i\,\Psi^\dagger M_8\Psi\big|_{z=\pi/2} = \Psi^\dagger\gamma^{(4)}\gamma^{(8)}\Psi\big|_{z=\pi/2} .
\end{aligned}
$$

The first line differentiates under the integral and inserts the equation; the second collects the factors $\mp i$ and uses the boundary identity with $u = v = \Psi$ (the integral of a derivative is the difference of its end values); the third uses $\sin z = 0$ at the tip and $1$ at the end, and $-i\cdot i = 1$. The norm of a solution changes ONLY by the flux through the patch end. For a field that does not depend on $x_8$, $N = \Psi^\dagger\Psi/(6H)$. Notebook 08d follows such a growing mode at $m = H = 1$: its norm first dips (the flux is briefly negative) and then grows by a factor $N(1.5)/N(0) = 2094.786$ in $1.5$ time units, and $dN/dx_4$ equals the flux at every time to rounding (COMPUTED).

**What this means (labelled).** Interpretation: the growth of the good-sector modes is fed through the patch end. A boundary condition at $z = \pi/2$ that stops the flux would make $h$ symmetric and would change the spectrum; which condition is physical is OPEN. Without one, the initial-value problem of the good sector has growing solutions: this is the second way, besides the extra-time waves of Sections 8.17 to 8.25, in which the field equation as recorded fails to define a stable evolution.

### 8.33 Example: the rescaling and the modes of the hidden direction

Notebook 08d puts Sections 8.30 to 8.32 to work, exactly, with sympy. It takes the spin connection of the diagonal frame from the record's formula and verifies it (the gammas are covariantly constant); proves the rescaling for sixteen arbitrary component functions; draws the rescaling factor and the hidden coordinate $y$ with the tip cutoff of the Kohn-Sham record; verifies the exact family for symbolic $\alpha$, $m$, $H$ and every $a_4$, and maps which members grow and which have a finite norm; checks the matrix $A$ of the modes that do not depend on $x_8$; proves the boundary identity on explicit columns; and follows a growing mode whose norm changes exactly by the flux through the patch end. It needs no Rust and runs in one to two minutes; the times measured on the build computer, which depend on how busy that computer is, are recorded in the notebook's provenance file `Revision/textbook/notebooks/08d_rescaling_modes.PROVENANCE.md`. It ends with the line ALL 23 CHECKS PASSED (notebook 08d).

<!-- NOTEBOOK 08d -->

### 8.36 Line-by-line walk-through of Notebook 08d

The notebook has 12 code cells, In [1] to In [12]. The conventions are those of Section 8.15; captions shortened to `...` are printed in full in Section 8.35.

**In [1], the set-up cell.** It is the set-up cell explained in Section 8.15, with the line `NOTEBOOK_ID = "08d"  # this notebook: chapter 08, example d`; its comment lines are the run instructions of Section 8.34. Output: `Set-up of notebook 08d complete: repository folder found, helpers defined.`

**In [2], the spin connection from the record, verified.** The cell starts with the imports of numpy and sympy, the empty table `REPORTS` and the helpers `record_says` and `check_record`, word for word those of Notebook 08a (Section 8.23; `check_record` takes one check name). Then:

```python
THEORY = "Revision/theory/reports/python-field-theory.json"  # the sympy records
SCOPE = "Revision/theory/reports/python-scope.json"
gammas_record = json.loads(
    repository_file("Revision/algebra/gammas.json").read_text(encoding="utf-8"))
G = [sp.Matrix(rows) for rows in gammas_record["gamma"]]  # gamma^(x1) ... (x8)
ETA = gammas_record["eta"]  # [1, 1, 1, -1, -1, -1, -1, 1]
C = sp.Matrix(gammas_record["C"])  # C = gamma^(x8) gamma^(x1) gamma^(x2) gamma^(x3)
B = sp.Matrix(gammas_record["B"]["re"]) + sp.I * sp.Matrix(gammas_record["B"]["im"])
```

Short names for the paths of the two sympy reports, and the gammas, the signs, $C$ and $B$ as exact sympy matrices.

```python
theory = json.loads(
    repository_file("Revision/theory/field-theory.json").read_text(encoding="utf-8"))
formulas = {entry["key"]: entry for entry in theory["formulas"]}
say("record Omega_components: " + formulas["Omega_components"]["wl"])
```

The formula file of the field-theory record holds a list `formulas`, each with a `key` and the formula as text; the dictionary comprehension makes a table key: entry. The `say` line prints the record's formula of the spinor connection in the Wolfram language (`g[xi]` is $\gamma^{(x_i)}$, `a4'[x4]` is $a_4'$, `E^a4[x4]` is $e^{a_4}$), which the next lines enter in sympy.

```python
x = sp.symbols("x1:9", real=True)  # the coordinates; x[3] is x4, x[7] is x8
H = sp.Symbol("H", positive=True)
m = sp.Symbol("m", real=True)
a4 = sp.Function("a4")(x[3])  # any function of the time x4
a4_prime = sp.diff(a4, x[3])
z = 6 * H * x[7]
sixth = sp.sin(z) ** sp.Rational(1, 6)
f = [sp.exp(a4) * sixth] * 3 + [sp.Integer(1)] + [sp.exp(-a4) * sixth] * 3 \
    + [sp.cot(z)]
g = [ETA[a] * f[a] ** 2 for a in range(8)]  # the diagonal metric
gamma_up = [G[mu] / f[mu] for mu in range(8)]  # gamma^mu = gamma^(mu) / f_mu
```

The symbols, the unknown history $a_4(x_4)$ and its derivative, $z$, $\sin^{1/6}z$, the scale factors, the diagonal metric and the coordinate gammas $\gamma^\mu = \gamma^{(\mu)}/f_\mu$ of the diagonal frame, as in Notebook 08c.

```python
Omega = [sp.zeros(16, 16) for _ in range(8)]
for i in (0, 1, 2):  # x1, x2, x3 (inflating)
    Omega[i] = sp.exp(a4) * sixth * (a4_prime * G[i] * G[3] + H * G[i] * G[7]) / 2
for t in (4, 5, 6):  # x5, x6, x7 (deflating extra times)
    Omega[t] = -sp.exp(-a4) * sixth * (a4_prime * G[3] * G[t] + H * G[t] * G[7]) / 2
```

The record's formula entered in sympy: $\Omega_{x_i} = \frac12e^{a_4}\sin^{1/6}z(a_4'\gamma^{(i)}\gamma^{(4)} + H\gamma^{(i)}\gamma^{(8)})$, $\Omega_{x_t} = -\frac12e^{-a_4}\sin^{1/6}z(a_4'\gamma^{(4)}\gamma^{(t)} + H\gamma^{(t)}\gamma^{(8)})$, and zero for $x_4$ and $x_8$ (the starting zero matrices are kept). These are the formulas derived in Section 8.4.

```python
def is_zero(expr):
    ...


Gam = [[[sp.Integer(0)] * 8 for _ in range(8)] for _ in range(8)]
for lam in range(8):  # Christoffel symbols of the diagonal metric
    ...
                Gam[lam][mu][nu] = sp.simplify(value / (2 * g[lam]))
```

`is_zero` and the Christoffel symbols are computed exactly as in Notebook 08c (In [2] and In [3]; the lines shortened to `...` here are the same lines, explained in Section 8.15).

```python
constant = all(
    all(is_zero(v) for v in sp.diff(gamma_up[nu], x[mu])
        + sum((Gam[nu][mu][lam] * gamma_up[lam] for lam in range(8)), sp.zeros(16, 16))
        + Omega[mu] * gamma_up[nu] - gamma_up[nu] * Omega[mu])
    for mu in range(8) for nu in range(8))
check_record(constant, "the record's Omega_mu makes every gamma^nu covariantly "
             "constant (64 pairs)", THEORY, "covariant_constancy_D_mu_gamma_nu",
             "= 0 for all 64 (mu, nu)")
```

For all 64 pairs $(\mu, \nu)$ the covariant derivative of the coordinate gamma, $\partial_\mu\gamma^\nu + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}\gamma^\lambda + \Omega_\mu\gamma^\nu - \gamma^\nu\Omega_\mu$, is computed and every entry must vanish. This verifies the record's connection independently of the definition used in Notebook 08c: covariant constancy fixes the connection (Section 8.9, Step 4).

```python
gamma_Omega = sum((gamma_up[mu] * Omega[mu] for mu in range(8)), sp.zeros(16, 16))
check_record(all(is_zero(v) for v in gamma_Omega - 3 * H * G[7]),
             "gamma^mu Omega_mu = 3 H gamma^(x8) (diagonal frame)",
             THEORY, "gamma_mu_Omega_mu_equals_3H_gamma_x8",
             "gamma^mu Omega_mu = 3 H gamma^(x8) exactly")
```

The sum $\gamma^\mu\Omega_\mu$, compared with $3H\gamma^{(8)}$. Output: the formula line and two PASS lines with their `reproduces` lines.

**In [3], the rescaling removes the term.**

```python
w = sp.sin(z) ** sp.Rational(-1, 2)  # the rescaling factor sin(z)^(-1/2)
check_record(is_zero(sp.tan(z) * sp.diff(w, x[7]) + 3 * H * w),
             "tan z d8 sin(z)^(-1/2) = -3 H sin(z)^(-1/2)", SCOPE,
             "rescaling_removes_the_connection_term",
             "(tan z (-3 H sin^(-1/2) z) + 3 H sin^(-1/2) z) gamma^(x8) chi = 0")
```

The one-line identity $\tan z\,\partial_8w = -3Hw$ of Section 8.30, with the record's text of the same identity.

```python
chi = sp.Matrix([sp.Function(f"chi{A}")(*x) for A in range(1, 17)])  # arbitrary
Psi = w * chi
D_Psi = sum((gamma_up[mu] * (sp.diff(Psi, x[mu]) + Omega[mu] * Psi)
             for mu in range(8)), sp.zeros(16, 1))  # gamma^mu D_mu Psi
D_chi = sum((gamma_up[mu] * sp.diff(chi, x[mu]) for mu in range(8)),
            sp.zeros(16, 1))  # gamma^mu d_mu chi (no connection)
check_record(all(is_zero(v) for v in D_Psi - w * D_chi),
             "gamma^mu D_mu (w chi) = w gamma^mu d_mu chi for 16 arbitrary functions",
             SCOPE, "rescaling_removes_the_connection_term",
             "the field equation has no spin-connection term: gamma^mu d_mu chi = "
             "(m + U'(S)) chi")
```

`chi` is a column of sixteen unknown functions $\chi_1, \dots, \chi_{16}$ of all eight coordinates (`*x` passes the eight symbols as arguments); nothing is assumed about them. `Psi` is $w\chi$; `D_Psi` is $\gamma^\mu D_\mu\Psi$ with the connection, `D_chi` is $\gamma^\mu\partial_\mu\chi$ without it (both start from a $16 \times 1$ zero column). The check requires $\gamma^\mu D_\mu(w\chi) - w\gamma^\mu\partial_\mu\chi = 0$ in all 16 components, the statement of Section 8.30 for every field.

```python
lam, S_chi = sp.symbols("lambda S_chi", real=True)  # S_chi stands for S[chi]
S_Psi = w**2 * S_chi  # S[w chi] = (w chi)^dagger C (w chi) = w^2 S[chi]
check_record(is_zero(lam * S_Psi - lam * S_chi / sp.sin(z)),
             "U = (lambda/2) S^2: lambda S[Psi] = lambda S[chi]/sin z (the new "
             "coupling)", SCOPE, "rescaled_equation_quadratic_potential",
             "gamma^mu d_mu chi = (m + lambda S[chi]/sin z) chi")
y_of_x8 = sp.log(sp.sin(z)) / (6 * H)
check(is_zero(sp.cos(z) * w**2 - sp.cot(z)) and
      is_zero(sp.diff(y_of_x8, x[7]) - sp.cot(z)),
      "cos z w^2 = cot z = dy/dx8: the norm of Psi is the y-norm of chi")
```

The potential: with a symbol `S_chi` for $S[\chi]$, $\lambda S[\Psi] = \lambda w^2S[\chi]$ is compared with $\lambda S[\chi]/\sin z$. The measure: $\cos z\,w^2 = \cot z = dy/dx_8$. Output: four PASS lines, three with `reproduces` lines.

**In [4], the rescaling factors and the hidden coordinate.**

```python
parameters = json.loads(repository_file(
    "Revision/kohn_sham/results/parameters.json").read_text(encoding="utf-8"))
H_record = parameters["physics"]["H"]  # the author's constant H of the record
L_tip = parameters["physics"]["L_tipCutoff"]  # the record cuts the tip at y = -L
z_cut = np.arcsin(np.exp(-6 * H_record * L_tip))  # the z at which y = -L
report("H and the tip cutoff L of the Kohn-Sham record", f"{H_record}, {L_tip}")
report("z at the tip cutoff, arcsin(e^(-6 H L))", f"{z_cut:.6e}")
check(H_record == 1.0 and abs(np.log(np.sin(z_cut)) / (6 * H_record) + L_tip) < 1e-12,
      "the record has H = 1, and y(z_cut) = -L",
      record="Revision/kohn_sham/results/parameters.json, physics.H, "
             "physics.L_tipCutoff")
```

$H$ and the tip cutoff $L$ are read from the Kohn-Sham record. The cutoff $y = -L$ means $\ln(\sin z) = -6HL$, so $\sin z = e^{-6HL}$ and $z_{\rm cut} = \arcsin(e^{-6HL})$ (`np.arcsin` is the inverse sine). The RESULT lines print `1.0, 3.0` and $z_{\rm cut} = 1.522998 \times 10^{-8}$; the check confirms $H = 1$ and that $y(z_{\rm cut}) = -L$ to $10^{-12}$.

```python
zs = np.linspace(0.01, np.pi / 2, 400)
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
left.plot(zs, np.sin(zs) ** -0.5, label="rescaling factor $\\sin^{-1/2}z$")
left.plot(zs, 1 / np.sin(zs), "--", label="coupling factor $1/\\sin z$")
left.set_yscale("log")
left.set_xlabel("$z = 6Hx_8$ (tip at 0, patch end at $\\pi/2$)")
left.set_ylabel("factor")
left.set_title("The rescaling $\\Psi = \\sin^{-1/2}z\\,\\chi$")
left.legend()
```

The left panel draws the two factors $\sin^{-1/2}z$ and $1/\sin z$ for 400 values of $z$ from 0.01 to $\pi/2$ on a logarithmic axis.

```python
mantissa, exponent = f"{z_cut:.1e}".split("e")  # "1.5e-08" -> "1.5" and "-08"
exponent = int(exponent)  # -8, for the caption
z_log = np.logspace(-10.0, np.log10(np.pi / 2), 400)  # 10^-10 ... pi/2, log spaced
right.semilogx(z_log, np.log(np.sin(z_log)) / (6 * H_record), color="tab:green")
right.axhline(-L_tip, color="gray", linestyle=":", linewidth=0.9)
right.plot([z_cut], [-L_tip], "o", color="black")  # where y reaches the cutoff
right.text(2e-8, -L_tip + 0.15, "tip cutoff $y = -L$ of the Kohn-Sham record",
           fontsize=8)
```

The cutoff value is written with one decimal in powers of ten and split at the letter `e` into the two parts that the caption prints (`1.5` and `-8`). The right panel draws $y = \ln(\sin z)/(6H)$ for 400 values of $z$ from $10^{-10}$ to $\pi/2$, equally spaced on a logarithmic axis (`semilogx`; `np.log10` is the base-10 logarithm), a dotted line at $y = -L$, a black dot where $y$ reaches it, and a label.

```python
right.set_xlabel("$z = 6Hx_8$ (logarithmic axis)")
right.set_ylabel("$y = \\ln(\\sin z)/(6H)$")
right.set_title("The hidden coordinate $y$, $H = 1$")
save_figure(fig, "rescaling_factors",
            "Left, on a logarithmic axis, against $z = 6Hx_8$ from the tip (near 0) "
            ...
            "lies in a tiny neighbourhood of the tip.")
```

Labels, a title, and Figure 08d.1; the caption is an f-string, so the values read from the record ($y = -3$, $\arcsin(e^{-18}) \approx 1.5 \times 10^{-8}$) are put in when the cell runs. Output: two RESULT lines, one PASS line with its `reproduces` line, the figure line.

**What Figure 08d.1 shows.** Left: the two factors (pure numbers, logarithmic vertical axis) against $z$ from 0.01 to $\pi/2$: the rescaling factor $\sin^{-1/2}z$ falls from 10 to 1, the coupling factor $1/\sin z$ from 100 to 1; both equal 1 at the patch end and grow without bound towards the tip. Right: the hidden coordinate $y$ (vertical, units of $1/H$) against $z$ on a logarithmic axis from $10^{-10}$ to $\pi/2$: an almost straight line from about $-3.84$ up to 0 (because $\sin z \approx z$ for small $z$, $y \approx \ln(z)/6$ is a straight line on this axis), with the cutoff $y = -3$ reached at $z \approx 1.5 \times 10^{-8}$. The student should see that almost the whole range of $y$ used by the Kohn-Sham record lies in a tiny neighbourhood of the tip.

**In [5], the exact family.**

```python
alpha = sp.Symbol("alpha", real=True)
c = 3 * H * (2 * alpha + 1)
k = sp.sqrt(c**2 - m**2)  # k^2 = 9 H^2 (2 alpha + 1)^2 - m^2
M = -m * G[3] + c * G[3] * G[7]
check_record((M * M - (c**2 - m**2) * sp.eye(16)).applyfunc(sp.expand)
             == sp.zeros(16, 16)
             and (M.T * C + C * M).applyfunc(sp.expand) == sp.zeros(16, 16),
             "M^2 = (9 H^2 (2 alpha + 1)^2 - m^2) I16 and M^T C + C M = 0",
             THEORY, "exact_solution_family_x4_x8",
             "M = -m gamma^(x4) + 3 H (2 alpha + 1) gamma^(x4) gamma^(x8)",
             "k^2 = 9 H^2 (2 alpha + 1)^2 - m^2", "(M^2 = k^2 I16, M^T C + C M = 0")
```

The exponent $\alpha$, the number $c = 3H(2\alpha + 1)$, $k$ and the matrix $M$ of Section 8.31. The check confirms $M^2 = (c^2 - m^2)I_{16}$ (derived in Section 8.31) and $M^TC + CM = 0$; the second property means that the scalar $S = \Psi^\dagger C\Psi$ of a member does not change in time, because $\frac{d}{dx_4}(e^{M^Tx_4}Ce^{Mx_4}) = e^{M^Tx_4}(M^TC + CM)e^{Mx_4} = 0$ ($M$ is real). The record's detail must contain the three texts.

```python
chi0 = sp.Matrix(sp.symbols("q1:17"))  # 16 arbitrary constants
family = sp.sin(z) ** alpha * (sp.cosh(k * x[3]) * chi0
                               + sp.sinh(k * x[3]) / k * (M * chi0))
residual = sum((gamma_up[mu] * (sp.diff(family, x[mu]) + Omega[mu] * family)
                for mu in range(8)), sp.zeros(16, 1)) - m * family
check_record(all(is_zero(v) for v in residual),
             "Psi = sin(z)^alpha (cosh(k x4) + sinh(k x4)/k M) chi0 solves the field "
             "equation", THEORY, "exact_solution_family_x4_x8",
             "solves gamma^mu D_mu Psi = m Psi exactly for every a4(x4) and every "
             "alpha")
```

$\chi_0$ is a column of sixteen symbols `q1`, ..., `q16` (arbitrary constants). `family` is the member $\sin^\alpha z(\cosh(kx_4)\chi_0 + \frac{\sinh(kx_4)}{k}M\chi_0)$, and `residual` is $\gamma^\mu D_\mu\Psi - m\Psi$ with the full connection, summed over all eight directions; every entry must vanish, for symbolic $\alpha$, $m$, $H$ and every $a_4$.

```python
M_half = M.subs(alpha, -sp.Rational(1, 2))
check_record(not M_half.has(H)
             and sp.expand(k.subs(alpha, -sp.Rational(1, 2)) ** 2) == -m**2,
             "alpha = -1/2: M = -m gamma^(x4) has no H and k^2 = -m^2 (oscillation)",
             SCOPE, "rescaled_equation_quadratic_potential",
             "= -m gamma^(x4) and k^2 = -m^2 (no H)")
```

At $\alpha = -\frac12$, $M$ contains no $H$ and $k^2 = -m^2$: the rescaled field of Section 8.30. Output: three PASS lines with their `reproduces` lines.

**In [6], which members grow and which have a finite norm.**

```python
s, p, eps = sp.symbols("s p epsilon", positive=True)
check(sp.integrate(s ** (p - 1), (s, 0, 1)) == 1 / p and
      sp.limit(sp.integrate(1 / s, (s, eps, 1)), eps, 0, "+") == sp.oo,
      "int_0^1 s^(2 alpha) ds = 1/(2 alpha + 1) for 2 alpha + 1 > 0; diverges at -1/2")
```

With $p = 2\alpha + 1 > 0$, sympy integrates $s^{p-1} = s^{2\alpha}$ from 0 to 1 and finds $1/p$; and the integral of $1/s$ from $\epsilon$ to 1 goes to infinity (`sp.oo`) as $\epsilon \to 0$ from above (`"+"`): the two integrals of Section 8.31.

```python
k2_every_mass = sp.factor(sp.expand((c**2 - m**2).subs(alpha, m / (3 * H))))
say(f"k^2 at alpha = m/(3H): {k2_every_mass}")
check(sp.expand(k2_every_mass - 3 * (m + H) * (m + 3 * H)) == 0,
      "alpha = m/(3H) > -1/2 gives k^2 = 3 (m + H)(m + 3H) > 0 for every m > 0")
```

At $\alpha = m/(3H)$ sympy factors $k^2$ and prints `3*(H + m)*(3*H + m)`; the check compares with $3(m + H)(m + 3H)$.

```python
alphas = np.linspace(-2.0, 1.0, 601)
fig, ax = plt.subplots()
for mass, style in ((1.0, "-"), (2.0, "--"), (4.0, ":")):
    ax.plot(alphas, 9 * (2 * alphas + 1) ** 2 - mass**2, style, label=f"$m = {mass:g}H$")
    ax.plot([-0.5, 0.0], [-mass**2, 9 - mass**2], "o", color="black", markersize=4)
ax.axhline(0.0, color="black", linewidth=0.8)
ax.axvspan(-2.0, -0.5, color="gray", alpha=0.15)
ax.text(-1.4, 66, "infinite norm\nat the tip", fontsize=8)
ax.text(0.05, 66, "grows where\n$k^2 > 0$", fontsize=8)
```

For three masses ($H = 1$) the parabola $k^2 = 9(2\alpha + 1)^2 - m^2$ is drawn against $\alpha$ from $-2$ to 1, with black dots at $\alpha = -\frac12$ ($k^2 = -m^2$) and $\alpha = 0$ ($k^2 = 9 - m^2$); `axvspan` shades the band $\alpha \le -\frac12$ light gray (here `alpha=0.15` is matplotlib's transparency, not the exponent).

```python
ax.set_ylim(-20.0, 80.0)
ax.set_xlabel("exponent $\\alpha$ of $\\sin^{\\alpha}z$")
ax.set_ylabel("$k^2 = 9H^2(2\\alpha + 1)^2 - m^2$ (units of $H^2$)")
ax.set_title("The exact family $\\sin^\\alpha z\\,e^{Mx_4}\\chi_0$, $H = 1$")
ax.legend(loc="upper center");
save_figure(fig, "family_k_squared",
            "The number $k^2 = 9H^2(2\\alpha + 1)^2 - m^2$ of the exact family of "
            ...
            "finite norm grows.")
```

The vertical range, labels, and Figure 08d.2. Output: two PASS lines, the factored $k^2$, the figure line.

**What Figure 08d.2 shows.** The number $k^2$ (vertical, units of $H^2$) against the exponent $\alpha$ (horizontal) for $m = H, 2H, 4H$: three upward parabolas with their lowest point $-m^2$ at $\alpha = -\frac12$ (black dots at $-1$, $-4$, $-16$); at $\alpha = 0$ the dots are at $8$, $5$ and $-7$. The shaded band $\alpha \le -\frac12$ is where the norm diverges at the tip. The student should see that to the right of the band every parabola eventually becomes positive: for every mass, some members with a finite norm grow; and that the $x_8$-independent member $\alpha = 0$ grows for $m = H$ and $2H$ but not for $4H$.

**In [7], the plane of mass and exponent.**

```python
masses = np.linspace(0.0, 6.0, 301)
A_grid, M_grid = np.meshgrid(np.linspace(-1.0, 1.5, 251), masses)
grows = 9 * (2 * A_grid + 1) ** 2 - M_grid**2 > 0
finite = A_grid > -0.5
region = np.where(grows & finite, 2, np.where(grows, 1, 0))  # 2, 1 or 0
```

A grid of 301 masses (0 to $6H$) and 251 exponents ($-1$ to $1.5$). `grows` and `finite` are true/false arrays; `&` is "and" for such arrays. `region` is 2 where a member grows with a finite norm, 1 where it grows with an infinite norm, and 0 where it oscillates.

```python
fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.contourf(M_grid, A_grid, region, levels=[-0.5, 0.5, 1.5, 2.5],
            colors=["white", "#d9d9d9", "#9ecae1"])
ax.plot(masses, (masses / 3 - 1) / 2, color="black", linewidth=1.0)
ax.axhline(-0.5, color="gray", linestyle="--", linewidth=0.9)
ax.axhline(0.0, color="tab:red", linewidth=1.2)
ax.plot([3.0], [0.0], "o", color="tab:red")
ax.text(0.2, 1.2, "grows, finite norm", fontsize=9)
ax.text(4.2, -0.2, "oscillates", fontsize=9)
ax.text(0.2, -0.9, "grows, infinite norm", fontsize=9)
ax.text(3.1, 0.05, "$\\alpha = 0$: grows for $m < 3H$", fontsize=8, color="tab:red")
ax.set_xlabel("mass $m$ (units of $H$)")
ax.set_ylabel("exponent $\\alpha$")
ax.set_title("Members of the family that grow and have a finite norm")
```

`contourf` fills the three regions with white, light gray and light blue (colours given as hexadecimal codes, `"#9ecae1"`). The black line is $2\alpha + 1 = m/(3H)$, that is $\alpha = (m/3 - 1)/2$ for $H = 1$; the gray dashed line is $\alpha = -\frac12$; the red line is $\alpha = 0$, with a red dot at $m = 3H$; four labels.

```python
fraction = float(np.mean(grows & finite))
report("fraction of the drawn (m, alpha) rectangle that grows with finite norm",
       f"{fraction:.4f}")
check(all(np.any(grows[i] & finite[i]) for i in range(len(masses))),
      "for every drawn mass some alpha gives a growing finite-norm member")
save_figure(fig, "growing_finite_norm",
            "The plane of the mass $m$ (horizontal, units of $H$) and the exponent "
            ...
            "every mass has growing finite-norm members.")
```

The fraction of the drawn rectangle where members grow with a finite norm is printed (0.5996). The check requires, for each of the 301 masses (each row `i` of the grid), at least one exponent with a growing finite-norm member (`np.any` is true when at least one entry is). Figure 08d.3. Output: one RESULT line, one PASS line, the figure line.

**What Figure 08d.3 shows.** The plane of the mass $m$ (horizontal, 0 to $6H$) and the exponent $\alpha$ (vertical, $-1$ to $1.5$). Light blue, above the rising black line $2\alpha + 1 = m/(3H)$: growing members with a finite norm. Light gray, a wedge below the dashed line $\alpha = -\frac12$ at small masses: growing members whose norm diverges at the tip. White: oscillating members. The red line $\alpha = 0$ lies in the blue region exactly for $m < 3H$ (red dot). The student should see that every vertical line (every mass) meets the blue region.

**In [8], the modes that do not depend on $x_8$.**

```python
A = -sp.I * m * G[3] + 3 * sp.I * H * G[3] * G[7]
A_squared = (A * A).applyfunc(sp.expand)
A_one = A.subs({m: 1, H: 1})
dimension = 16 - (A_one - 2 * sp.sqrt(2) * sp.I * sp.eye(16)).rank()
norm_factor = sp.integrate(sp.cos(6 * H * x[7]), (x[7], 0, sp.pi / (12 * H)))
report("dimension of the eigenspace of +2 sqrt(2) i at m = H = 1", dimension)
report("int_0^(pi/(12H)) cos(6 H x8) dx8", norm_factor)
```

The matrix $A = -im\gamma^{(4)} + 3iH\gamma^{(4)}\gamma^{(8)}$ of Section 8.32, its square, its value at $m = H = 1$, the dimension of the eigenspace of $+2\sqrt2\,i$ (16 minus a rank, as in Notebook 08a), and the norm factor $\int_0^{\pi/(12H)}\cos(6Hx_8)\,dx_8$ integrated exactly. RESULT lines: 8 and `1/(6*H)`.

```python
all_true = ((A - sp.I * M.subs(alpha, 0)).applyfunc(sp.expand) == sp.zeros(16, 16)
            and A != A.H
            and A_squared == ((m**2 - 9 * H**2) * sp.eye(16)).applyfunc(sp.expand)
            and A_one * A_one == -8 * sp.eye(16) and A_one.trace() == 0
            and dimension == 8 and sp.simplify(norm_factor - 1 / (6 * H)) == 0)
# The record states the same matrix, square, eigenvalues and norm in its text:
check_record(all_true,
             "A = -i m g4 + 3 i H g4 g8: not Hermitian, A^2 = (m^2 - 9H^2) I16, "
             "eigenvalues +-2 sqrt(2) i at m = H = 1, finite norm 1/(6H)",
             SCOPE, "good_sector_x8_independent_modes_without_boundary_condition",
             f"cos(6 H x8) dx8 = {sp.sstr(norm_factor)})",
             "A = -i m gamma^(x4) + 3 i H gamma^(x4) gamma^(x8)",
             "A^2 = (m^2 - 9 H^2) I16 exactly",
             f"the eigenvalues are +-2 sqrt(2) i ({dimension} each)")
```

Seven facts in one condition: $A = iM$ at $\alpha = 0$; $A$ is not Hermitian ($A \neq A^\dagger$); $A^2 = (m^2 - 9H^2)I_{16}$; at $m = H = 1$, $A^2 = -8I_{16}$ and the trace is 0 (so the eigenvalues are $\pm 2\sqrt2\,i$, eight each, as in Section 8.17); the eigenspace dimension is 8; and the norm factor is $1/(6H)$. The record's detail must contain the four texts. Output: two RESULT lines and one PASS line with its `reproduces` line.

**In [9], the eigenvalues of $A$ against the mass.**

```python
A_number = sp.lambdify((m, H), A, "numpy")
mass_path = np.linspace(0.0, 5.0, 51)
points = np.concatenate([np.linalg.eigvals(np.array(A_number(mv, 1.0), dtype=complex))
                         for mv in mass_path])
largest_growth = max(abs(points.imag))
report("largest |imaginary part| on the path (reached at m = 0)",
       f"{largest_growth:.9f}")
check(abs(largest_growth - 3.0) < 1e-9, "at m = 0 the growth rate is 3H")
```

`A_number` is a numerical function of $m$ and $H$. For 51 masses from 0 to 5 (with $H = 1$) the 16 eigenvalues are computed and joined; the largest imaginary part, reached at $m = 0$ where the eigenvalues are $\pm 3i$, is printed as 3.000000000, and the check requires $3H$ to $10^{-9}$.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
dots = left.scatter(points.real, points.imag, c=np.repeat(mass_path, 16),
                    cmap="plasma", s=20)
fig.colorbar(dots, ax=left, label="mass $m$ (units of $H$)")
left.set_aspect("equal")
left.set_xlim(-4.5, 4.5)
left.set_ylim(-4.5, 4.5)
left.set_xlabel("real part")
left.set_ylabel("imaginary part")
left.set_title("Eigenvalues of $A$, $H = 1$")
```

The left panel draws the eigenvalues in the complex plane, coloured by the mass, with equal scales on both axes.

```python
mass_fine = np.linspace(0.0, 5.0, 501)  # a finer grid for the smooth curves
for a_value, style in ((0.0, "-"), (0.5, "--"), (1.0, ":")):
    rate = np.sqrt(np.maximum(9 * (2 * a_value + 1) ** 2 - mass_fine**2, 0.0))
    right.plot(mass_fine, rate, style, label=f"$\\alpha = {a_value:g}$")
right.axvline(3.0, color="gray", linewidth=0.8)
right.set_xlabel("mass $m$ (units of $H$)")
right.set_ylabel("growth rate $k$ (units of $H$)")
right.set_title("Growth rates of the family")
right.legend();
save_figure(fig, "patch_end_modes",
            "Left: the eigenvalues $\\pm\\sqrt{m^2 - 9H^2}$ of the matrix $A = "
            ...
            "line).")
```

The right panel draws the growth rate $k = \sqrt{9(2\alpha + 1)^2 - m^2}$ (0 where the bracket is negative) of the members $\alpha = 0, 0.5, 1$ against the mass, with a gray vertical line at $m = 3H$. Figure 08d.4. Output: one RESULT line, one PASS line, the figure line.

**What Figure 08d.4 shows.** Left: the eigenvalues of $A$ (units of $H$) in the complex plane, coloured by the mass from 0 to $5H$: for small masses they sit on the imaginary axis at $\pm 3i$ (dark), move towards 0 as $m$ grows, meet at 0 for $m = 3H$, and then move out along the real axis to $\pm 4$ at $m = 5H$ ($\sqrt{25 - 9} = 4$). Right: the growth rates (units of $H$) against the mass: the member $\alpha = 0$ falls from 3 to 0 at $m = 3H$ (gray line) and stays 0; the members $\alpha = 0.5$ and $\alpha = 1$ start at 6 and 9 and still grow at $m = 5H$ (about 3.3 and 7.5). The student should see that the $x_8$-independent modes stop growing above $m = 3H$, but members that vary along $x_8$ do not.

**In [10], the boundary term at the patch end.**

```python
M8 = sp.I * G[3] * G[7]
d8_coefficient = sp.I * sp.tan(z) * G[3] * G[7]  # the matrix in front of d8 in h
fact_1 = all(is_zero(v) for v in sp.cos(z) * d8_coefficient - sp.sin(z) * M8)
fact_2 = all(is_zero(v) for v in sp.cos(z) * (A - A.H) - sp.diff(sp.sin(z), x[7]) * M8)
fact_3 = (d8_coefficient + d8_coefficient.H).applyfunc(sp.simplify) == sp.zeros(16, 16)
```

$M_8 = i\gamma^{(4)}\gamma^{(8)}$ and the coefficient $P$ of $\partial_8$ in $h$. The three facts of Section 8.32, in the order of the notebook: $\cos z\,P = \sin z\,M_8$; $\cos z\,(A - A^\dagger) = (\partial_8\sin z)M_8$; and $P + P^\dagger = 0$.

```python
X8 = x[7]
u_col = sp.Matrix([(A_ + 1) + sp.I * (2 * A_ - 3) * X8 + (A_ - 5) * X8**2 / 3
                   for A_ in range(16)])  # a column of polynomials in x8
v_col = sp.Matrix([(3 - A_) * X8 + sp.I * (A_ + 2) + sp.I * A_ * X8**3 / 7
                   for A_ in range(16)])


def h_of(column):
    """The mode operator h applied to a column of functions of x8 (U = 0)."""
    return -sp.I * m * G[3] * column + sp.I * G[3] * G[7] * (
        sp.tan(z) * sp.diff(column, X8) + 3 * H * column)
```

Two explicit columns of polynomials in $x_8$ with complex coefficients that differ from entry to entry (the loop variable `A_` runs from 0 to 15; its name has an underscore so that it does not overwrite the matrix `A`), and the mode operator $h$ applied to a column.

```python
left_side = sp.cos(z) * ((u_col.H * h_of(v_col))[0] - (h_of(u_col).H * v_col)[0])
right_side = sp.diff(sp.sin(z) * (u_col.H * M8 * v_col)[0], X8)
u0 = (G[3] * G[7] - sp.eye(16)).nullspace()[0]  # gamma^(4) gamma^(8) u0 = u0
flux = sp.simplify((u0.H * M8 * u0)[0])
size_u0 = (u0.H * u0)[0]
report("u0^dagger M8 u0 and u0^dagger u0", f"{flux}, {size_u0}")
```

The two sides of the boundary identity for these columns (a row times a column is a $1 \times 1$ matrix, and `[0]` takes its entry). `nullspace()` returns a list of independent columns $u$ with $(\gamma^{(4)}\gamma^{(8)} - I)u = 0$; the first one is `u0`. RESULT: $u_0^\dagger M_8u_0 = 2i$ (sympy writes `2*I`) and $u_0^\dagger u_0 = 2$.

```python
# The record states the same identity and the same flux (sympy writes i as I):
check_record(fact_1 and fact_2 and fact_3 and is_zero(left_side - right_side)
             and flux == 2 * sp.I and size_u0 == 2,
             "cos z (u^dagger h v - (h u)^dagger v) = d8(sin z u^dagger M8 v); at "
             "z = pi/2 the flux u0^dagger M8 u0 = 2 i is not zero",
             SCOPE, "good_sector_hermiticity_up_to_the_brane_flux",
             "cos z [u^dagger (h v) - (h u)^dagger v] = d_x8(sin z u^dagger M8 v)",
             f"u^dagger M8 u = {sp.sstr(flux)} (|u|^2 = {sp.sstr(size_u0)})")
```

The check combines the three facts, the identity for the two columns, and the flux; the record's detail must contain the identity and the same flux. (The record proves the identity for all columns; here it is confirmed on one explicit pair, and the three facts are what make it general, Section 8.32.) Output: one RESULT line and one PASS line with its `reproduces` line.

**In [11], a growing mode is fed through the patch end.**

```python
A_num = np.array(A_number(1.0, 1.0), dtype=complex)  # m = H = 1
g4g8 = np.array(G[3] * G[7], dtype=float)  # real symmetric
rng = np.random.default_rng(12345)  # fixed seed: the same column in every run
chi_start = rng.normal(size=16) + 1j * rng.normal(size=16)
chi_start = chi_start / np.linalg.norm(chi_start)
omega = np.sqrt(complex(1.0 - 9.0))  # A^2 = (m^2 - 9 H^2) = -8: omega = 2 sqrt(2) i
times = np.linspace(0.0, 1.5, 151)
```

The matrix $A$ at $m = H = 1$, the real symmetric matrix $\gamma^{(4)}\gamma^{(8)}$, a random starting column of size 1 (fixed seed, as in Notebook 08a), the frequency $\omega = \sqrt{m^2 - 9H^2} = \sqrt{-8} = 2\sqrt2\,i$ (here the name `omega` is a frequency, not the spin connection), and 151 times from 0 to 1.5.

```python
norms, slopes, fluxes = [], [], []
for x4 in times:
    state = np.cos(omega * x4) * chi_start \
        - 1j * np.sin(omega * x4) / omega * (A_num @ chi_start)  # e^(-i A x4) chi
    norms.append(np.vdot(state, state).real / 6.0)  # N = Psi^dagger Psi / (6 H)
    slopes.append(2 * np.vdot(state, -1j * (A_num @ state)).real / 6.0)  # dN/dx4
    fluxes.append(np.vdot(state, g4g8 @ state).real)  # flux at z = pi/2
norms, slopes, fluxes = map(np.array, (norms, slopes, fluxes))
```

At each time the mode $\Psi = e^{-iAx_4}\chi_0$ is computed with the closed formula of Section 8.18 (valid because $A^2 = \omega^2I_{16}$). Three numbers are recorded: the norm $N = \Psi^\dagger\Psi/(6H)$; its rate of change $dN/dx_4 = 2\,\mathrm{Re}\big(\Psi^\dagger(-iA\Psi)\big)/(6H)$ (the derivative of $\Psi^\dagger\Psi$ is twice the real part of $\Psi^\dagger\partial_4\Psi$, and $\partial_4\Psi = -iA\Psi$); and the flux $\Psi^\dagger\gamma^{(4)}\gamma^{(8)}\Psi$ at the patch end (a field that does not depend on $x_8$ has the same value there). `map(np.array, ...)` turns the three lists into arrays.

```python
agreement = np.max(np.abs(slopes - fluxes) / np.maximum(np.abs(fluxes), 1.0))
check(agreement < 1e-12, "dN/dx4 equals the flux through the patch end at every x4")
report("N(1.5) / N(0)", f"{norms[-1] / norms[0]:.6e}")
check(norms[-1] / norms[0] > 100.0, "the norm grows by more than a factor 100")
```

The check requires $dN/dx_4$ to equal the flux at all 151 times, to $10^{-12}$ relative to $\max(|\text{flux}|, 1)$: the result of Section 8.32. The RESULT line prints $N(1.5)/N(0) = 2.094786 \times 10^3$, and the second check requires growth by more than 100.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
left.semilogy(times, norms)
left.set_xlabel("time $x_4$ (units of $1/H$)")
left.set_ylabel("norm $N(x_4)$")
left.set_title("The $x_8$-independent mode, $m = H = 1$")
right.plot(times, slopes, label="$dN/dx_4$")
right.plot(times[::10], fluxes[::10], "o", color="black", markersize=4,
           label="flux at $z = \\pi/2$")
right.axhline(0.0, color="black", linewidth=0.8)
right.set_yscale("symlog", linthresh=1.0)  # linear between -1 and 1, log outside
right.set_ylim(-1.5, 3.0e3)
right.set_xlabel("time $x_4$ (units of $1/H$)")
right.set_ylabel("rate (units of $H$)")
right.set_title("Rate of change of the norm = flux")
right.legend();
save_figure(fig, "norm_and_flux",
            "An $x_8$-independent mode of the good sector, $\\Psi = e^{-iAx_4}"
            ...
            "condition.")
```

Left: the norm on a logarithmic axis. Right: $dN/dx_4$ as a line and every tenth flux value as a black dot, on a symmetric logarithmic axis that is linear between $-1$ and 1, so that the short negative phase is visible. Figure 08d.5. Output: two PASS lines, one RESULT line, the figure line.

**What Figure 08d.5 shows.** Left: the norm $N$ (logarithmic vertical axis) against the time $x_4$ from 0 to 1.5 (units of $1/H$): it starts at $1/6$, dips a little during the first tenth of a unit, and then rises along a straight line (growth like $e^{4\sqrt2\,x_4}$, twice the rate $2\sqrt2$ of the column) to about 350. Right: the rate of change $dN/dx_4$ (line) and the flux through the patch end (dots), in units of $H$: slightly negative at the start, zero near $x_4 \approx 0.05$, then rising to about 2000. The student should see the dots lie exactly on the line: the norm changes only through the patch end, where the Revision record imposes no boundary condition.

**In [12], the last check.**

```python
for name in ("08d_1_rescaling_factors.png", "08d_2_family_k_squared.png",
             "08d_3_growing_finite_norm.png", "08d_4_patch_end_modes.png",
             "08d_5_norm_and_flux.png"):
    check(output_file(f"{FIGURE_FOLDER}/{name}").is_file(),
          f"the figure file {name} exists")
all_checks_passed()
```

Five checks that the figure files exist, and the last line. The 23 checks come from the cells as follows: two in In [2], four in In [3], one in In [4], three in In [5], two in In [6], one each in In [7], In [8], In [9] and In [10], two in In [11] and five here. The last line reads `ALL 23 CHECKS PASSED (notebook 08d)`.

### 8.37 The exact scope of non-triviality and of the evolution, in one table

Every statement of the chapter in one place. The last column names the Revision check, the short name of its report file in brackets, and the notebook that reproduces it. The report files are these:

```text
Revision/theory/reports/python-field-theory.json     (python-field-theory)
Revision/theory/reports/wolfram-field-theory.json    (wolfram-field-theory)
Revision/theory/reports/python-scope.json            (python-scope)
Revision/theory/reports/wolfram-scope.json           (wolfram-scope)
Revision/pairing/reports/python-pairing.json         (python-pairing)
```

| statement | status | Revision check; notebook |
| --- | --- | --- |
| diagonal frame: $\gamma^\mu\Omega_\mu = 3H\gamma^{(8)}$ for every $a_4$; the $\pm a_4'/2$ pieces cancel, six pieces $H/2$ add | PROVED | `gamma_mu_Omega_mu_equals_3H_gamma_x8`, `time_terms_cancel_hidden_term_survives` (python-field-theory); 08c |
| $3H\gamma^{(8)}\Psi \neq 0$ for every $\Psi \neq 0$ | PROVED | `nontriviality_1_dirac16complex`, `nontriviality_2_dirac16complex00` (wolfram-field-theory); 08c |
| $\Omega_\mu = 0$ for every $\mu$ only if $a_4' = 0$ and $H = 0$ (not a member of the family) | PROVED | `nontriviality_Omega_zero_iff_flat` (python-field-theory); 08c |
| the term contains no $a_4$, although $R^{x_4}{}_{x_4} = 6(a_4')^2$ | PROVED | `gammaOmega_blind_to_the_deflation` (python-scope); 08c |
| the connection drops out of the Lagrangian; the term is the half-density term | PROVED | `connection_free_lagrangian_same_equations` (python-scope); 08c |
| boosted frame: $\gamma'^\mu\Omega'_\mu = \frac{6H - \beta}{2}(\cosh b\,\gamma^{(8)} - \sinh b\,\gamma^{(4)})$, zero for $\beta = 6H$ | PROVED | `boosted_frame_gammaOmega_formula`, `boosted_frame_gammaOmega_vanishes` (python-scope, wolfram-scope); 08c |
| the spin connection vanishes in no frame: its curvature is the Riemann tensor, nonzero for $H > 0$ | PROVED | `boosted_frame_curvature_nonzero` (python-scope); `spinor_curvature_equals_riemann` (python-field-theory); 08c |
| the connection enters the energy-momentum tensor | PROVED | `spin_connection_in_the_energy_momentum_tensor` (python-scope); 08c |
| the rescaling $\Psi = \sin^{-1/2}z\,\chi$ removes the term; for $U \neq 0$ it becomes $\lambda S[\chi]/\sin z$ | PROVED | `rescaling_removes_the_connection_term`, `rescaled_equation_quadratic_potential` (python-scope); 08d |
| the slices $x_4 = $ const are non-characteristic | PROVED | `evolution_form_G` (wolfram-field-theory); 08a |
| $h_k^2 = E^2I_{16}$; the growth rates of extra-time waves have no upper bound; in flat 4+4 space and with frozen coefficients the Cauchy problem is not well posed in Hadamard's sense | PROVED | `extra_time_growth_rates_unbounded` (python-scope, wolfram-scope); 08a |
| in the author's metric itself (varying coefficients, $U = 0$) the Cauchy problem is not well posed for data that depend on the extra times | ASSUMED (a quoted theorem) | not checked by the record; the Lax-Mizohata theorem, quoted without proof, applied to the frequencies of the principal part (Section 8.18) |
| the Krein form is conserved; growing eigenspaces are Krein-neutral; real-frequency eigenspaces have inertia (4,4) | PROVED | `mode_hamiltonian_B_selfadjoint_dispersion` (python-field-theory); `Q.one_particle_complex_frequency_Krein_neutral`, `Q.one_particle_Krein_inertia_proof` (python-pairing); 08a |
| along the deflating history every extra-time wave reaches the onset of growth (frozen coefficients at each instant) | PROVED | `extra_time_modes_grow` (python-field-theory); 08b |
| through the onset the growth follows the WKB formulas and is faster than any exponential (local-frame model) | COMPUTED | 08b: agreement $1.03 \times 10^{-3}$ (leading), $2.48 \times 10^{-4}$ (first order), late rate $10^{-5}$ |
| the exact family $\sin^\alpha z\,e^{Mx_4}\chi_0$; for every mass a growing member with finite norm | PROVED | `exact_solution_family_x4_x8` (python-field-theory); 08d |
| the $x_8$-independent good-sector modes grow for $m < 3H$; the mode operator is symmetric only up to the flux at $z = \pi/2$ | PROVED | `good_sector_x8_independent_modes_without_boundary_condition`, `good_sector_hermiticity_up_to_the_brane_flux` (python-scope); 08d |
| the history $a_4 = AHx_4$ ($A = 1$) | ASSUMED | prescribed background (`Revision/kohn_sham/results/parameters.json`) |
| frozen coefficients; the local-frame model | ASSUMED | labelled MODEL in 08a and 08b |
| which boundary condition at $z = \pi/2$ is physical; a well-posed formulation of the full field equation | OPEN | none imposed in the record |

### 8.38 What we proved, what we computed, what we assumed

**PROVED in this chapter, line by line** (and in the Revision record, with the file and check named in the section):

- The canonical spin connection of the diagonal frame: the rule $\omega_\mu{}^a{}_b = (f_a/f_b)\Gamma^a{}_{\mu b}$ for $a \neq b$, its 12 independent nonzero components, and the spinor connections $\Omega_{x_i}$, $\Omega_{x_t}$, $\Omega_{x_4} = \Omega_{x_8} = 0$ (Section 8.4).
- $\gamma^\mu\Omega_\mu = 3H\gamma^{(8)}$, direction by direction: the time-direction pieces of the three inflating and the three deflating directions cancel, the six hidden-direction pieces add; and the divergence form $\gamma^\mu\Omega_\mu = \frac{1}{2\sqrt{|g|}}\partial_\mu(\sqrt{|g|}\gamma^\mu)$ (Section 8.5).
- $\Omega_\mu = 0$ for every $\mu$ if and only if $a_4' = 0$ and $H = 0$; $3H\gamma^{(8)}\Psi \neq 0$ for every $\Psi \neq 0$ (Section 8.6). The term contains no $a_4$, while $R^{x_4}{}_{x_4} = 6(a_4')^2$ and $R = 6((a_4')^2 - 7H^2)$ (Section 8.7).
- $\{\gamma^\mu, \Omega_\mu\} = 0$ for each $\mu$; the connection drops out of the Lagrangian, and the Euler-Lagrange equation of the connection-free symmetric Lagrangian contains the same term as its half-density term (Section 8.8).
- The boost keeps the metric; the spin transformation $S = e^{-(b/2)\gamma^{(4)}\gamma^{(8)}}$ moves the gammas of the boosted frame; the connection of the boosted frame and the formula $\gamma'^\mu\Omega'_\mu = \frac{6H - \beta}{2}(\cosh b\,\gamma^{(8)} - \sinh b\,\gamma^{(4)})$, zero for $\beta = 6H$ (Sections 8.3 and 8.9).
- $F' = SFS^{-1}$; $F_{x_1x_8} \neq 0$ in every frame of this kind; the square of the curvature is the same in both frames (Section 8.10). The connection part $\frac12 e^{a_4}\sin^{1/6}z\,H\,\gamma^{(4)}\gamma^{(1)}\gamma^{(8)}$ of $K^{x_4}{}_{x_1}$ (Section 8.11).
- The Hadamard toy example; the second-order form with the extra-time derivatives of the "wrong" sign; the evolution form (Section 8.16). The mode matrix, $h_k^2 = E^2I_{16}$, its eigenvalues $\pm E$ eight each, its anti-Hermitian part (Section 8.17). Unbounded growth rates ($\kappa \ge K - c$), the closed solution in time, and the failure of continuous dependence in every Sobolev norm, in flat 4+4 space and with frozen coefficients (Section 8.18); the frequencies of the principal part, which are not real for a wave along an extra time at any point of the author's metric (Section 8.18). Conservation of the Krein form and the Krein-neutrality of the growing eigenspaces (Section 8.19).
- Conserved coordinate wave numbers, growing frame momenta, the exact onset time and its finiteness for every $q_5 > 0$ (Section 8.24). The Krein form $\sigma E_0/m$ of the starting columns and the leading and first-order WKB formulas (Section 8.25).
- The rescaling removes the term for every field, and turns the quadratic potential into $\lambda S[\chi]/\sin z$; the norm becomes $\int\chi^\dagger\chi\,dy$ (Section 8.30). The exact family, its growth condition, its finite-norm condition, and a growing finite-norm member for every mass (Section 8.31). The matrix $A$ and its growing modes; the boundary identity; the change of the norm only through the flux at the patch end (Section 8.32).

**PROVED in the Revision record and used here without its proof:** the Clifford relations and the reality and symmetry of the author's gammas (Chapter 4); the irreducibility of the 16-dimensional representation (commutant dimension 1; Chapter 5); the 25 Christoffel symbols and the Ricci components (Chapter 3); the vielbein postulate and the covariant constancy of the gammas in the diagonal frame; the curvature identity $F = \frac14R\gamma\gamma$ in the diagonal frame; $Bh_k = h_k^\dagger B$; the Krein inertia (4,4) of every real-frequency eigenspace; the Euler-Lagrange equations of the Grassmann field; and the direct computation of the boosted frame's connection.

**COMPUTED by the notebooks** (every exact statement is also checked there, and every number reproduces the record where they overlap): Notebook 08c, 32 checks, computes everything of Sections 8.4 to 8.11 exactly with sympy, including the curvature in both frames, and at one point of the history $a_4 = x_4$ the largest curvature entries 0.778093 and 0.038739 ($= e^{-3}\cdot 0.778093$) and ranks 8. Notebook 08a, 30 checks, confirms $h_k^2 = E^2$ exactly, the growth rates against the eigenvalues to $10^{-10}$, the closed formula against RK4 to $10^{-9}$, the Hadamard ratio (first above $10^6$ at $K = 13.9, 19.9, 27.1, 44.2$ for $s = 0, 2, 4, 8$), the Krein drift below $10^{-12}$. Notebook 08b, 25 checks, confirms the onset times against bisection to $10^{-12}$, RK4 with the error ratio 15.89 and accuracy $10^{-8}$, the WKB agreement ($1.03 \times 10^{-3}$, $2.48 \times 10^{-4}$, late rate $10^{-5}$), the slow growth of the size before the onset (to $u^\dagger u = 1.52$ and $1.54$ at the onset), and growth to $u^\dagger u \approx 1.26 \times 10^{16}$ with the Krein drift below $10^{-9}$. Notebook 08d, 23 checks, proves the rescaling for arbitrary functions, the family for symbolic $\alpha$, the boundary identity on explicit columns, and finds $N(1.5)/N(0) = 2094.786$ with $dN/dx_4$ equal to the flux to $10^{-12}$. Run times: 08a and 08b run in well under a minute, 08c and 08d in one to two minutes; the provenance file of each notebook (in the folder `Revision/textbook/notebooks`, named after the notebook, for example `08c_frame_dependence.PROVENANCE.md`) records the times measured on the build computer in its build and check runs, which depend on how busy that computer is.

**ASSUMED, chosen, or an interpretation.** The history $a_4 = AHx_4$ with $A = H = m = 1$ is a PRESCRIBED BACKGROUND (the Kohn-Sham record's own label); every exact identity of the chapter holds for every history. Frozen coefficients (Sections 8.17 to 8.19) and the local-frame model (Section 8.25) are labelled MODEL: they describe a wave near one point, not exact solutions of the field equation in the author's metric. Facts taken from Chapter 6 (where local spin covariance is proved): the canonical spin connection of every frame makes its gammas covariantly constant and is a combination of the $S^{ab}$. Standard theorems quoted without proof: the Lax-Mizohata theorem, which carries the failure of well-posedness from frozen coefficients to the author's varying coefficients (Section 8.18; so that conclusion is ASSUMED, not PROVED, and the record does not check it); the general curvature identity $F = \frac14R\gamma\gamma$ in every frame (proved for this metric by the record); the trace of a matrix is the sum of its eigenvalues; the dimension of an eigenspace is 16 minus the rank of $h - \lambda I$. Treating $\bar\Psi$ and $\Psi$ as independent variables in the Euler-Lagrange equations is the method of Chapter 7. Two statements are interpretations, labelled as such: that the role of the term $3H$ depends on the variables and the measure (Section 8.30), and that the growth of the good-sector modes is "fed through the patch end" (Section 8.32).

**OPEN.** Which boundary condition at the patch end $z = \pi/2$ is physical (the Kohn-Sham record ASSUMES a $Z_2$ brane there; this record imposes none). Whether and how the full field equation can be given a well-posed evolution: restricting to the good sector removes the extra-time growth but is a choice, not a consequence, and even the good sector needs a boundary condition. A positive-norm quantum theory of the full field with the growing modes present, and a stable vacuum, are not constructed (Chapter 10 states what is). Whether the frame-dependent term $3H\gamma^{(8)}$ has any observable effect is not claimed.

### 8.39 Exercises

**Exercise 1.** Compute $\gamma^{x_6}\Omega_{x_6}$ directly from $\Omega_{x_6} = -\frac12e^{-a_4}\sin^{1/6}z\,(a_4'\gamma^{(4)}\gamma^{(6)} + H\gamma^{(6)}\gamma^{(8)})$, line by line.

*Answer.* $\gamma^{x_6} = \gamma^{(6)}/f_6$ with $f_6 = e^{-a_4}\sin^{1/6}z$. Then $\gamma^{x_6}\Omega_{x_6} = -\frac12(a_4'\gamma^{(6)}\gamma^{(4)}\gamma^{(6)} + H\gamma^{(6)}\gamma^{(6)}\gamma^{(8)})$ (the scale factors cancel). Anticommuting $\gamma^{(6)}$ past $\gamma^{(4)}$: $\gamma^{(6)}\gamma^{(4)}\gamma^{(6)} = -\gamma^{(4)}(\gamma^{(6)})^2 = -\gamma^{(4)}(-I_{16}) = \gamma^{(4)}$; and $(\gamma^{(6)})^2 = -I_{16}$. So $\gamma^{x_6}\Omega_{x_6} = -\frac12(a_4'\gamma^{(4)} - H\gamma^{(8)}) = -\frac12a_4'\gamma^{(4)} + \frac12H\gamma^{(8)}$, the value of every extra time in Section 8.5.

**Exercise 2.** Suppose the extra times inflated like 3-space, $f_5 = f_6 = f_7 = e^{+a_4}\sin^{1/6}z$ (this is NOT the author's metric). Compute $\gamma^{x_t}\Omega_{x_t}$ and $\gamma^\mu\Omega_\mu$, and confirm the result with the divergence form.

*Answer.* Now $g_{tt} = -e^{2a_4}\sin^{1/3}z$, so $\Gamma^{x_t}{}_{x_tx_4} = \partial_4\ln f_t = +a_4'$ and $\Gamma^{x_4}{}_{x_tx_t} = -\partial_4g_{tt}/(2g_{44}) = -(2a_4'g_{tt})/(-2) = a_4'g_{tt} = -a_4'f_t^2$. By the rule of Section 8.4, $\omega_{x_t}{}^{(4)}{}_{(t)} = (f_4/f_t)\Gamma^{x_4}{}_{x_tx_t} = -a_4'f_t$, and lowering with $\eta_{44} = -1$, $\omega_{x_t\,(4)(t)} = +a_4'f_t$ (the opposite sign of the author's metric). The $H$ component is unchanged, $\omega_{x_t\,(t)(8)} = -Hf_t$. So $\Omega_{x_t} = \frac12f_t(a_4'\gamma^{(4)}\gamma^{(t)} - H\gamma^{(t)}\gamma^{(8)})$, and $\gamma^{x_t}\Omega_{x_t} = \frac12(a_4'\gamma^{(t)}\gamma^{(4)}\gamma^{(t)} - H(\gamma^{(t)})^2\gamma^{(8)}) = \frac12(a_4'\gamma^{(4)} + H\gamma^{(8)})$, the same as a 3-space direction. The six directions then give $\gamma^\mu\Omega_\mu = 3a_4'\gamma^{(4)} + 3H\gamma^{(8)}$: nothing cancels. Divergence form: $\sqrt{|g|} = e^{6a_4}\cos z$, so $\frac{1}{2\sqrt{|g|}}\partial_4(\sqrt{|g|}\gamma^{(4)}) = \frac{6a_4'e^{6a_4}\cos z}{2e^{6a_4}\cos z}\gamma^{(4)} = 3a_4'\gamma^{(4)}$, and $\frac{1}{2\sqrt{|g|}}\partial_8(e^{6a_4}\sin z\,\gamma^{(8)}) = 3H\gamma^{(8)}$. The cancellation of Section 8.5 happens because in the author's metric the volume factor does not depend on the time.

**Exercise 3.** (a) Show that $\varphi = \epsilon\cosh(Kx_4)\cos(Kx_5)$ solves $\partial_4^2\varphi = -\partial_5^2\varphi$. (b) For data of largest value $\epsilon$, compute the ratio of the largest value of the solution at $x_4 = 1$ to $\epsilon$ for $K = 10$ and $K = 20$. (c) Show that $\varphi = \epsilon\cos(Kx_4)\cos(Kx_1)$ solves the ordinary wave equation $\partial_4^2\varphi = \partial_1^2\varphi$, and compare.

*Answer.* (a) Section 8.16: both sides equal $\epsilon K^2\cosh(Kx_4)\cos(Kx_5)$. (b) The ratio is $\cosh K$: $\cosh 10 = 11013.2$ and $\cosh 20 = 2.4258 \times 10^8$. Doubling $K$ multiplies the amplification by about $e^{10} \approx 22000$; data of the same size give ever larger solutions. (c) $\partial_4^2\varphi = -\epsilon K^2\cos(Kx_4)\cos(Kx_1) = \partial_1^2\varphi$; the largest value stays $\epsilon$ at every time, for every $K$: the ordinary wave equation depends continuously on its data.

**Exercise 4.** With frozen coefficients and $m = 1$, decide whether the waves oscillate or grow, and give the frequency or the growth rate: (a) $k_1 = 2$, $k_5 = 3$; (b) $k_5 = 2$, $k_8 = 1$; (c) $k_6 = k_7 = 0.5$. (d) With $k_1 = 4$, how large must $k_5$ be for growth? Compare with Figure 08a.1.

*Answer.* $E^2 = m^2 + k_1^2 + k_2^2 + k_3^2 + k_8^2 - k_5^2 - k_6^2 - k_7^2$. (a) $E^2 = 1 + 4 - 9 = -4$: growth with $\kappa = 2$. (b) $E^2 = 1 + 1 - 4 = -2$: growth with $\kappa = \sqrt2 = 1.414214$. (c) $E^2 = 1 - 0.25 - 0.25 = 0.5$: oscillation with $E = \pm0.707107$. (d) Growth needs $k_5^2 > 1 + 16 = 17$, that is $k_5 > \sqrt{17} = 4.123106$; in the right panel of Figure 08a.1 the dotted curve ($k_1 = 4$) leaves zero there.

**Exercise 5.** Show that the size $\sqrt{\mathrm{tr}(M^TM)/16}$ of $M = c\,(\cosh b\,\gamma^{(8)} - \sinh b\,\gamma^{(4)})$ is $|c|\sqrt{\cosh 2b}$. Evaluate it for the boosted frame with $\beta = 3H$, $H = 1$, $b_0 = 0$ at $x_4 = 0$, $0.3$ and $0.5$, and for $\beta = 9H$ at $x_4 = 0.5$, and compare with Figure 08c.3.

*Answer.* $(\gamma^{(8)})^T = \gamma^{(8)}$ and $(\gamma^{(4)})^T = -\gamma^{(4)}$, so $M^T = c(\cosh b\,\gamma^{(8)} + \sinh b\,\gamma^{(4)})$ and $M^TM = c^2\big(\cosh^2 b\,(\gamma^{(8)})^2 - \sinh^2 b\,(\gamma^{(4)})^2 + \cosh b\sinh b\,(\gamma^{(4)}\gamma^{(8)} - \gamma^{(8)}\gamma^{(4)})\big) = c^2\big((\cosh^2 b + \sinh^2 b)I_{16} + 2\cosh b\sinh b\,\gamma^{(4)}\gamma^{(8)}\big)$. The trace of $\gamma^{(4)}\gamma^{(8)}$ is zero, so $\mathrm{tr}(M^TM)/16 = c^2(\cosh^2 b + \sinh^2 b) = c^2\cosh 2b$ (because $\cosh^2 b + \sinh^2 b = \frac{(e^b + e^{-b})^2 + (e^b - e^{-b})^2}{4} = \frac{e^{2b} + e^{-2b}}{2}$). For $\beta = 3H$, $c = (6 - 3)/2 = 1.5$ and $b = 3x_4$: at $x_4 = 0$ the size is $1.5$; at $x_4 = 0.3$ ($b = 0.9$) it is $1.5\sqrt{\cosh 1.8} = 2.644204$; at $x_4 = 0.5$ ($b = 1.5$) it is $1.5\sqrt{\cosh 3} = 4.759437$. For $\beta = 9H$, $|c| = 1.5$, $b = 4.5$: $1.5\sqrt{\cosh 9} = 95.477587$. The orange and red curves of the right panel of Figure 08c.3 end near 4.8 and 95.

**Exercise 6.** On the history $a_4 = x_4$ ($a_4' = H = 1$), use the coefficients $c_{14}$, $c_{18}$ printed by Notebook 08c in both frames to show that $F' = e^{-b}F$ and $F^2 = 0$; check the largest entries 0.778093 and 0.038739 at $x_4 = 0.5$.

*Answer.* Write $Q = e^{a_4}\cos z/(2\sin^{5/6}z)$. Diagonal frame: $c_{14} = -Ha_4'Q = -H^2Q$ and $c_{18} = -H^2Q$, equal. Boosted frame ($b = 6Hx_4 + b_0$): $c_{14}' = H(H\sinh b - a_4'\cosh b)Q = H^2(\sinh b - \cosh b)Q = -H^2e^{-b}Q$ and $c_{18}' = -H(H\cosh b - a_4'\sinh b)Q = -H^2(\cosh b - \sinh b)Q = -H^2e^{-b}Q$, using $\cosh b - \sinh b = e^{-b}$. Both coefficients are $e^{-b}$ times the diagonal ones, and both frames use the same matrices $\gamma^{(1)}\gamma^{(4)}$, $\gamma^{(1)}\gamma^{(8)}$, so $F' = e^{-b}F$. Since $c_{14} = c_{18}$, $F^2 = (c_{14}^2 - c_{18}^2)I_{16} = 0$. At $x_4 = 0.5$, $b_0 = 0$: $b = 3$ and $0.778093\cdot e^{-3} = 0.778093 \times 0.049787 = 0.038739$, the printed value.

**Exercise 7.** Along $a_4 = x_4$ with $m = H = 1$, compute the onset times of the waves (a) $q_1 = 0$, $q_5 = 0.01$, $y = 0$; (b) the same at $y = -3$; (c) $q_1 = 0$, $q_5 = 10^{-4}$, $y = 0$; (d) $q_1 = 1$, $q_5 = 0.05$, $y = 0$.

*Answer.* For $q_1 = 0$, $x_4^\ast = (Hy + \ln(m/q_5))/(AH) = y + \ln(1/q_5)$. (a) $\ln 100 = 4.605170$. (b) $-3 + 4.605170 = 1.605170$. (c) $\ln 10^4 = 9.210340$, the left end of the top curve in Figure 08b.3. (d) $w = 1$, $X^\ast = (1 + \sqrt{1 + 4\cdot 1\cdot 0.0025})/(2\cdot 0.0025) = (1 + \sqrt{1.01})/0.005 = 400.997512$, and $x_4^\ast = \frac12\ln X^\ast = 2.996978$, slightly later than the 2.995732 of the same wave without space momentum: the space term dies away like $e^{-2a_4}$ and hardly matters.

**Exercise 8.** For the rescaling $\Psi = \sin^p z\,\chi$ with any real power $p$, find the term that replaces $3H\gamma^{(8)}$ in the equation for $\chi$, and the power that removes it. What does the norm become for that power?

*Answer.* $\tan z\,\partial_8\sin^p z = \tan z\cdot p\sin^{p-1}z\cos z\cdot 6H = 6Hp\sin^p z$. As in Section 8.30, $\gamma^\mu D_\mu(\sin^p z\,\chi) = \sin^p z\big(\gamma^\mu\partial_\mu\chi + (6Hp + 3H)\gamma^{(8)}\chi\big)$, so the term becomes $3H(2p + 1)\gamma^{(8)}$. It vanishes exactly for $p = -\frac12$. For $p = 0$ it is the original $3H\gamma^{(8)}$. For $p = -\frac12$ the norm is $\int\cos z\,\sin^{-1}z\,\chi^\dagger\chi\,dx_8 = \int\chi^\dagger\chi\,dy$. (The exact family of Section 8.31 is this computation with $\chi = e^{Mx_4}\chi_0$: its $c = 3H(2\alpha + 1)$ is the same factor.)

**Exercise 9.** For $m = H = 1$ take the member $\alpha = m/(3H) = \frac13$ of the exact family. Compute $k^2$ in two ways, the growth factor of $e^{Mx_4}$ over one unit of time for large $k x_4$, and the norm factor $\int_0^{\pi/(12H)}\cos z\sin^{2\alpha}z\,dx_8$.

*Answer.* $k^2 = 9H^2(2\alpha + 1)^2 - m^2 = 9\cdot(5/3)^2 - 1 = 25 - 1 = 24$, and also $3(m + H)(m + 3H) = 3\cdot 2\cdot 4 = 24$. So $k = 2\sqrt6 = 4.898979$, and the member grows by the factor $e^{k} = 134.15$ per unit of time once $\cosh$ and $\sinh$ are both close to $\frac12e^{kx_4}$. The norm factor is $\frac{1}{6H(2\alpha + 1)} = \frac{1}{6\cdot 5/3} = 0.1$: finite. This member varies along $x_8$ like $\sin^{1/3}z$. Unlike the $x_8$-independent member, whose growth needs $m < 3H$, the members $\alpha = m/(3H)$ grow for every mass.

**Exercise 10.** Prove the Krein-neutrality of a growing eigenvector algebraically: if $h_ku = i\kappa u$ with $\kappa > 0$ and $Bh_k = h_k^\dagger B$, then $u^\dagger Bu = 0$.

*Answer.* Compute $u^\dagger Bh_ku$ in two ways. First, $h_ku = i\kappa u$ gives $u^\dagger Bh_ku = i\kappa\,u^\dagger Bu$. Second, $Bh_k = h_k^\dagger B$ gives $u^\dagger Bh_ku = u^\dagger h_k^\dagger Bu = (h_ku)^\dagger Bu = (i\kappa u)^\dagger Bu = -i\kappa\,u^\dagger Bu$ (the dagger conjugates the number $i\kappa$). Equating: $i\kappa\,u^\dagger Bu = -i\kappa\,u^\dagger Bu$, so $2i\kappa\,u^\dagger Bu = 0$, and since $\kappa \neq 0$, $u^\dagger Bu = 0$. The same computation with two eigenvectors $u$, $v$ of $i\kappa$ gives $v^\dagger Bu = 0$: the Krein form vanishes on the whole eigenspace. For a real eigenvalue $E$ the two sides are $E\,u^\dagger Bu$ and $E\,u^\dagger Bu$, and nothing follows; that is why the real-frequency eigenspaces can carry the inertia (4,4).
