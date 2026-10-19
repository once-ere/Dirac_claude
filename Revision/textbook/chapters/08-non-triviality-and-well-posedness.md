## 8. Non-triviality, its exact scope, and well-posedness

When the author coupled the fields dirac16complex and dirac16complex00 to their primordial gravitational field, they asked for a test: the field equations must contain gravity through the canonical spin connection, unless spacetime is flat. This chapter answers that request exactly, and it answers a second question that every field equation must face before anyone can trust its solutions: does the equation decide the future from the present in a stable way? Both answers are more interesting than a plain yes. In the natural (diagonal) frame of the author's corrected metric the gravitational term of the field equation is $G\Psi = (c_g\gamma^{(0)} + v_g\gamma^{(4)})\Psi$ with $c_g = \frac32He^{a_4}b_4^{-1/2}$ and $v_g = b_4'/b_4 - a_4'/2$; but a different, equally valid frame removes its part $c_g\gamma^{(0)}$, and a change of the field variables removes all of it; what no choice removes is the spin connection itself wherever spacetime is curved, because its curvature is the curvature of spacetime. And the field equation, with its four time-like directions, is not a well-posed evolution equation: waves along the three extra times grow, with growth rates that have no upper bound, and the deflation of the hidden direction and the extra times pushes every such wave whose extra-time momentum outweighs its hidden momentum into growth. (This is proved exactly in flat 4+4 space and, for the author's metric, with coefficients frozen at one point; carrying it over to the author's varying coefficients needs a standard theorem that this chapter quotes without proof. Section 8.18 gives each status.) Even without any dependence on the extra times, the fields that do not depend on the hidden direction grow when nothing is imposed at the fold where the two halves of a cell meet. Four notebooks compute every statement anew from the definitions and reproduce the Revision record: Notebook 08c (the term in two frames), Notebook 08a (the growth rates), Notebook 08b (the onset of growth along the deflating history) and Notebook 08d (the rescaling, the exact families and the fold).

### 8.1 What this chapter does

**Why we need this chapter.** The author's task, quoted in the file `Revision/README.md` of the repository, says of the two Lagrangians: "[1]- the Lagrangian for dirac16complex must be non-trivial (i.e., the Euler-Lagrange equations for dirac16complex always possess non-zero contributions from gravity (through the canonical spin-connection, unless we are in flat 4+4 spacetime), must be self consistent, must be checked and verified)", and "[2]" asks the same of dirac16complex00 (the request also asks that the equations be self-consistent; Section 7.23 gives the six exact senses of that word in the Revision record, (i) to (vi), and where each is proved, and this chapter treats sense (ii), the evolution, in full in Sections 8.16 to 8.19). Two questions hide in this request. First: what exactly is "the contribution from gravity through the canonical spin connection", and which part of it is a property of the field equation itself rather than of the way we chose to write the equation down? Second: a field equation is useful only if, given the field now, it determines the field later, and determines it stably, so that a tiny change now makes only a tiny change later. Is that true here? This chapter answers both questions exactly, and says precisely where each answer stops.

**The answers in brief.** Each item carries its label (the labels are explained at the end of this section).

- In the diagonal frame of the author's corrected metric the gravitational term of the field equation is $\gamma^\mu\Omega_\mu\Psi = G\Psi$ with $G = c_g\gamma^{(0)} + v_g\gamma^{(4)}$, $c_g = \frac32He^{a_4}b_4^{-1/2}$ and $v_g = b_4'/b_4 - a_4'/2$, for all functions $a_4(x_4)$ and $b_4(x_4) > 0$. Direction by direction: the pieces $+\frac12a_4'$ of the three 3-space directions cancel the pieces $-\frac12a_4'$ of the three extra times; the hidden direction and the three extra times share the rate $h_4 = b_4'/(2b_4) - a_4'$ of their common scale factor $e^{-a_4}b_4^{1/2}$; and only the three extra times give pieces along $\gamma^{(0)}$, $\frac12He^{a_4}b_4^{-1/2}$ each. The term is not zero for any field $\Psi \neq 0$ wherever $c_g^2 \neq v_g^2$; on the history of the record $GG = H^2(\frac94e^{2Hx_4/3} - \frac{25}{36})I_{16}$, which is positive at every time $x_4 \geq 0$ (PROVED; Sections 8.4 to 8.6).
- The spin connection vanishes only in the formal limit $a_4' = 0$, $b_4' = 0$ and $H = 0$, which is not a member of the author's family of metrics (PROVED; Section 8.6).
- Unlike the withdrawn metric of 2026-10-14, the term sees the deflation: its $\gamma^{(0)}$ coefficient is $\frac32H$ times the inverse scale factor $e^{a_4}b_4^{-1/2}$ of the block of the hidden direction and the extra times, which grows as the block shrinks. The corrected metric is flat for the special history $a_4 = 0$, $b_4 = H^2x_4^2$ (there the term is a pure frame effect) and curved on the history of the record (PROVED; Section 8.7).
- The value $G$ belongs to one frame and to one choice of field variables. In a frame boosted in the $(x_4, x_0)$ plane with a rapidity $b(x_4)$ whose rate is $b' = 2c_g$ the part $c_g\gamma^{(0)}$ is gone, and only $v_g(\cosh b\,\gamma^{(4)} - \sinh b\,\gamma^{(0)})$ is left; no boost of this kind removes the part $v_g$. The rescaling $\Psi = e^{a_4/2}b_4^{-1}(\sin^2 z)^{-1/8}\chi$ removes the whole term in the diagonal frame (PROVED; Sections 8.9 and 8.30).
- What no choice removes: the spin connection itself vanishes in no frame wherever the metric is curved, because its curvature is the curvature of spacetime; and the frame factors $e^{a_4}b_4^{-1/2}\tan z$, $e^{-a_4}$ and $e^{a_4}b_4^{-1/2}(\sin^2 z)^{-1/12}$ multiply every derivative in the field equation except the one along the time $x_4$ (whose factor is $1/f_4 = 1$). This is the exact, frame-independent content of the tests [1] and [2] (PROVED; Sections 8.7 and 8.10). The Revision record states this as a correction for the author: the tests hold in this qualified sense.
- The field equation can be solved for the time derivative $\partial_4\Psi$, but its initial-value problem is NOT well posed for data that depend on the extra times $x_5, x_6, x_7$: such waves grow, and their growth rates have no upper bound (PROVED in flat 4+4 space and, for the author's metric, with frozen coefficients, a MODEL; for the author's varying coefficients it follows from the Lax-Mizohata theorem, a standard theorem quoted without proof, so that step is ASSUMED; Sections 8.16 to 8.19).
- Along the deflating history of the record ($a_4 = AHx_4$ and $b_4 = b_4(0)e^{(4/3)AHx_4}$, on which the hidden direction and the extra times shrink together like $e^{-AHx_4/3}$) the frame momenta of a wave along an extra time and along the hidden direction grow at the same rate. A wave starts to grow at a finite time exactly when $D = (\sin^2 z)^{-1/6}k_{x_5}^2 - \tan^2 z\,k_{x_0}^2 > 0$ (its extra-time momentum outweighs its hidden momentum), so every wave along an extra time without hidden momentum eventually grows, while a wave with $D \leq 0$ never does (PROVED with frozen coefficients; followed numerically through the onset in a labelled model, COMPUTED; Sections 8.24 and 8.25).
- Even without extra-time dependence, the hidden direction has the fold $z = \pi/2$, where the two halves of a cell meet; the Revision record imposes no boundary condition there, and the fields that do not depend on $x_0$ grow wherever $m < c_g$, which on the history happens for every mass after a finite time; their norm is fed through the fold. Which boundary condition is physical is OPEN (Sections 8.31 and 8.32).

**What the chapter does, section by section.** Section 8.2 sets the stage. Sections 8.3 to 8.11 compute the spin connection, the gravitational term, its frame dependence and the curvature, with Notebook 08c as the worked example (Sections 8.12 to 8.15). Sections 8.16 to 8.19 define well-posedness and show, with plane waves, that it fails; Notebook 08a is the example (Sections 8.20 to 8.23). Sections 8.24 and 8.25 follow waves along the deflating history; Notebook 08b is the example (Sections 8.26 to 8.29). Sections 8.30 to 8.32 change the field variables, study two exact families of solutions and the fold of the hidden direction; Notebook 08d is the example (Sections 8.33 to 8.36). Section 8.37 collects the exact scope in one table, Section 8.38 lists what we proved, computed and assumed, and Section 8.39 has the exercises.

**The four notebooks.**

| notebook | what it computes | checks and figures | Revision records it reproduces |
| --- | --- | --- | --- |
| 08c | the metric from the diagonal frame, its 21 Christoffel symbols and the canonical spin connection of the diagonal frame and of a boosted frame, from the definitions; what cancels and what survives in $\gamma^\mu\Omega_\mu$; the connection vanishes only in the formal limit; the Ricci tensor, the flat member and the curved history; the term in two frames; the curvature in both frames; the connection in the energy-momentum tensor | 37 checks, 5 figures | `python-field-theory.json`, `wolfram-field-theory.json`, `python-scope.json` (all in `Revision/theory/reports/`), `Revision/kohn_sham/results/parameters.json` |
| 08a | the mode matrix of a plane wave and its square; the growth rates of the extra-time waves; the Hadamard amplification; the Krein form | 30 checks, 6 figures | `python-scope.json`, `wolfram-scope.json`, `python-field-theory.json`, `wolfram-field-theory.json`, `Revision/algebra/reports/python-algebra.json`, `Revision/pairing/reports/python-pairing.json` |
| 08b | the scale factors and the volume along the deflating history; the frame momenta of a wave with extra-time, hidden and space momentum and its onset time; which waves reach the onset; one wave followed through the onset with RK4 and compared with WKB formulas | 29 checks, 5 figures | `parameters.json`, `python-field-theory.json`, `python-scope.json`, `Revision/dark_sector/dirac16complex/reports/derivation-checks.json` |
| 08d | the spin connection verified; the rescaling that removes the term; two exact families of solutions, their norms and their growth; the growing modes that do not depend on $x_0$; the boundary term at the fold | 27 checks, 5 figures | `python-field-theory.json`, `wolfram-field-theory.json`, `Revision/theory/field-theory.json`, `python-scope.json`, `parameters.json` |

The chapter places the notebooks in the order in which it uses them: 08c, 08a, 08b, 08d.

**How this chapter relates to Chapter 6.** Chapter 6 introduces the vielbein, the canonical spin connection of the corrected metric, the contraction $\gamma^\mu\Omega_\mu$, and, with its Notebook 06b, a first look at the boosted frame, the curvature and the rescaling; it also proves local spin covariance in general. This chapter recomputes everything it needs, so that it can be read on its own, and goes further: what cancels and what survives direction by direction, the proof that the connection vanishes only in the formal limit, the boosted term derived from the uniqueness of the connection, the curvature compared in two frames, the exact families with their growing finite-norm members, the flux through the fold, and, above all, the question of well-posedness, which Chapter 6 does not treat.

**The corrected metric.** The author's metric of the Revision record is the corrected metric of 2026-10-16 (Chapter 3; `Revision/SPEC.md`, section 1), a diagonal metric with $g_{00} = e^{-2a_4}b_4\cot^2 z$, $g_{11} = g_{22} = g_{33} = e^{2a_4}$, $g_{44} = -1$ and $g_{55} = g_{66} = g_{77} = -e^{-2a_4}b_4(\sin^2 z)^{1/6}$, with two functions $a_4(x_4)$ and $b_4(x_4) > 0$ of the time ($b_4$ is never 1). Every exact statement of this chapter holds for all functions $a_4$ and $b_4$ and every real $z$ between the degenerate points, and the four notebooks check them in that generality. The numerical examples use the history of the record, $a_4 = AHx_4$ and $b_4 = b_4(0)e^{\beta AHx_4}$ with $\beta = \frac43$, $b_4(0) = 1$ and $A = H = 1$ (`Revision/kohn_sham/results/parameters.json`, keys `historyA`, `historyBeta` and `historyB4AtZero`). The metric of 2026-10-14, withdrawn on 2026-10-16 (it had the factor $\sin^{1/3}z$ in 3-space, $g_{00} = \cot^2 z$ and a $Z_2$ brane at $z = \pi/2$), appears in this chapter only as dated history, where a comparison helps.

**Labels.** As everywhere in the book, every statement carries one of five labels. **PROVED** means exact: derived here line by line and confirmed by an exact check of a notebook, and, where the Revision record proves the same, the record file and its check are named. **COMPUTED** means a number obtained numerically by a notebook, with its measured accuracy. **ASSUMED** marks the inputs we choose or quote: standard theorems quoted without proof (each is named where it is used), the deflating history $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$, which the Revision record calls a PRESCRIBED BACKGROUND (it is not a solution of the author's field equations without a source: it needs a diagonal source that grows with the time, Chapter 12), and two approximations that the notebooks label MODEL (frozen coefficients, and the local-frame model of Section 8.25). **OPEN** marks questions this record does not answer. No HYPOTHESIS enters this chapter. Nothing in this chapter concerns pairs of universes, their creation, or matter and antimatter; those questions belong to Chapters 18 to 21, which state precisely what is and what is not proved about them.

### 8.2 The stage: coordinates, metric, frame and the field equation

**Coordinates.** A point of the author's spacetime has eight coordinates, named as the author names them, the hidden one first: $x_0$ is the **hidden** space direction; $x_1, x_2, x_3$ are ordinary 3-space; $x_4$ is the time in which everything evolves; $x_5, x_6, x_7$ are the three **extra times**, directions that behave like time (they are time-like) and that deflate exponentially. We write $z = 6Hx_0$, where $H > 0$ is a constant of the author; $z$ takes every real value. The metric repeats in $z$ with the period $\pi$; one **cell** $0 < z < \pi$ has two **halves**, $0 < z < \pi/2$ and $\pi/2 < z < \pi$, which meet at the **fold** $z = \pi/2$ (where $\cos z = 0$); at the **tips** $z = 0$ and $z = \pi$ the factor $\sin z$ vanishes. In formulas the letter $i$ always stands for one of the 3-space directions $x_1, x_2, x_3$ and the letter $t$ for one of the extra times $x_5, x_6, x_7$. In Python, lists are counted from 0, like the author's coordinates: position $k$ holds $x_k$, so position 0 is the hidden coordinate $x_0$ and position 4 the time $x_4$.

**The metric.** The author's corrected metric is diagonal (Chapter 3). We write it with eight **scale factors** $f_0, \dots, f_7$:

$$
g = \mathrm{diag}\big(f_0^2,\ f_1^2,\ f_2^2,\ f_3^2,\ -f_4^2,\ -f_5^2,\ -f_6^2,\ -f_7^2\big),
$$

$$
\begin{aligned}
f_0 &= e^{-a_4}b_4^{1/2}\cot z, \qquad f_1 = f_2 = f_3 = e^{a_4}, \qquad f_4 = 1, \\
f_5 &= f_6 = f_7 = e^{-a_4}b_4^{1/2}W, \qquad W = (\sin^2 z)^{1/12} .
\end{aligned}
$$

The **warp factor** $W$ is the positive twelfth root of $\sin^2 z$, defined for every real $z$; $W^2 = (\sin^2 z)^{1/6}$ and $W^3 = (\sin^2 z)^{1/4}$. The factor $f_0$ keeps the sign of $\cot z$ (positive on the first half of a cell, negative on the second); only its square enters the metric. A small step $dx_\mu$ along the direction $x_\mu$ has the proper length (the length measured with the metric) $|f_\mu|\,|dx_\mu|$. The two **metric functions** $a_4(x_4)$ and $b_4(x_4) > 0$ depend on the time. When $a_4$ increases, the 3-space factor $e^{a_4}$ grows (3-space **inflates**); it does not depend on $x_0$ at all (3-space has no warp). The hidden direction and the extra times share the factor $s_b = e^{-a_4}b_4^{1/2}$, which changes at the rate

$$
h_4 = \frac{d}{dx_4}\ln\big(e^{-a_4}b_4^{1/2}\big) = \frac{b_4'}{2b_4} - a_4' ;
$$

they **deflate** (shrink) together where $h_4 < 0$. On the history of the record $h_4 = \frac23AH - AH = -\frac{AH}{3}$ and $e^{-a_4}b_4^{1/2} = e^{-AHx_4/3}$. We write $a_4' = da_4/dx_4$, $a_4'' = d^2a_4/dx_4^2$, and in the same way $b_4'$ and $b_4''$. With the **frame metric** $\eta = \mathrm{diag}(+1, +1, +1, +1, -1, -1, -1, -1)$ (in the order $x_0, \dots, x_7$) every diagonal entry is $g_{\mu\mu} = \eta_{\mu\mu}f_\mu^2$. The signs say which directions are space-like ($+$: $x_0, x_1, x_2, x_3$) and which are time-like ($-$: $x_4, x_5, x_6, x_7$); there are four of each, the signature (4,4), wherever $\sin z\cos z \neq 0$. The metric degenerates at the folds ($\cos z = 0$: $g_{00} = 0$) and at the tips ($\sin z = 0$: $g_{tt} = 0$); every statement of this chapter is made between these points.

**The volume factor.** The product of the eight factors, line by line:

$$
\begin{aligned}
f_0f_1\cdots f_7 &= e^{-a_4}b_4^{1/2}\cot z\cdot e^{3a_4}\cdot 1\cdot e^{-3a_4}b_4^{3/2}W^3 \\
&= e^{-a_4}b_4^2\cot z\,(\sin^2 z)^{1/4} .
\end{aligned}
$$

The first line inserts the eight factors ($f_1f_2f_3 = e^{3a_4}$, $f_5f_6f_7 = e^{-3a_4}b_4^{3/2}W^3$); the second multiplies the powers ($e^{-a_4}e^{3a_4}e^{-3a_4} = e^{-a_4}$, $b_4^{1/2}b_4^{3/2} = b_4^2$) and uses $W^3 = (\sin^2 z)^{1/4}$. Its size is the **volume factor**

$$
\sqrt{|g|} = e^{-a_4}b_4^2\,|\cot z|\,(\sin^2 z)^{1/4}, \qquad \partial_4\sqrt{|g|} = \Big(2\frac{b_4'}{b_4} - a_4'\Big)\sqrt{|g|}
$$

(PROVED; `Revision/theory/reports/python-field-theory.json`, check `sqrt_det_g`, and `wolfram-field-theory.json`, check of the same name). The inflation $e^{3a_4}$ of 3-space and the factor $e^{-3a_4}$ of the extra times cancel, and the hidden direction leaves $e^{-a_4}b_4^{1/2}$; the second formula is the derivative of $\ln(e^{-a_4}b_4^2) = -a_4 + 2\ln b_4$. The value $H = 0$ is not a member of the author's family: at fixed $x_0 \neq 0$ the factor $(\sin^2 z)^{1/6}$ goes to $0$ and $\cot^2 z$ to infinity, so the metric degenerates (`Revision/theory/reports/wolfram-field-theory.json`, check `degenerate_at_H_0`). Every statement of this chapter assumes $H > 0$.

**The diagonal frame.** A **frame** (also called a **vielbein**) is a set of eight vectors, one for each direction $a = 0, \dots, 7$, that have length 1 and are perpendicular to each other when measured with the metric. Its components $e^a{}_\mu$ (frame direction $a$, coordinate direction $\mu$) obey $\sum_a \eta_{aa}e^a{}_\mu e^a{}_\nu = g_{\mu\nu}$. The **diagonal frame** is $e^a{}_\mu = f_a\delta^a_\mu$, where $\delta^a_\mu$ is 1 for $a = \mu$ and 0 otherwise; its inverse is $E_a{}^\mu = \delta^\mu_a/f_a$. Indeed $\sum_a\eta_{aa}f_a\delta^a_\mu f_a\delta^a_\nu$ is zero for $\mu \neq \nu$ and $\eta_{\mu\mu}f_\mu^2 = g_{\mu\mu}$ for $\mu = \nu$ (PROVED; `python-field-theory.json`, check `metric_from_vielbein_equals_SPEC`).

**The gamma matrices.** The book uses the author's eight **real** $16 \times 16$ gamma matrices (Chapter 4), stored in the Revision file `Revision/algebra/gammas.json` in the order $x_0, \dots, x_7$; we write them $\gamma^{(0)}, \dots, \gamma^{(7)}$ ($\gamma^{(4)}$ means the gamma of the direction $x_4$, and so on). Their entries are $0$, $1$ and $-1$. They obey the **Clifford relations**

$$
\gamma^{(a)}\gamma^{(b)} + \gamma^{(b)}\gamma^{(a)} = 2\eta^{ab}\,I_{16},
$$

where $I_{16}$ is the $16 \times 16$ unit matrix and $\eta^{ab} = \eta_{ab}$ (PROVED; `Revision/algebra/reports/python-algebra.json`, check `clifford_relation`). Two consequences are used in almost every line of this chapter: the square of each gamma is $\eta_{aa}I_{16}$, that is $+I_{16}$ for $x_0, x_1, x_2, x_3$ and $-I_{16}$ for $x_4, x_5, x_6, x_7$; and two different gammas **anticommute**, $\gamma^{(a)}\gamma^{(b)} = -\gamma^{(b)}\gamma^{(a)}$ for $a \neq b$. A third fact: the gammas of the space-like directions are symmetric matrices and those of the time-like directions antisymmetric, $(\gamma^{(a)})^T = \eta_{aa}\gamma^{(a)}$ (the $T$ means the transpose: rows become columns). The **coordinate gammas** are $\gamma^\mu = \sum_a E_a{}^\mu\gamma^{(a)}$; in the diagonal frame $\gamma^\mu = \gamma^{(\mu)}/f_\mu$. The matrix $C = \gamma^{(0)}\gamma^{(1)}\gamma^{(2)}\gamma^{(3)}$ (Chapter 5) and the matrix $B = -iC\gamma^{(4)}$ (Chapters 5 and 10) appear in the notebooks; $B$ is Hermitian, $B^2 = I_{16}$, with eight eigenvalues $+1$ and eight $-1$.

**The two fields and their field equation.** dirac16complex is a column $\Psi$ of 16 complex **anticommuting** (Grassmann) components; dirac16complex00 is a column of 16 ordinary complex numbers (Chapter 7). Their Lagrangians have the same form, and so do their field equations (Chapter 7 derives them):

$$
\gamma^\mu D_\mu\Psi = \big(m + U'(S)\big)\Psi, \qquad D_\mu\Psi = \partial_\mu\Psi + \Omega_\mu\Psi .
$$

Here $\partial_\mu$ is the partial derivative with respect to $x_\mu$, the sum over $\mu = 0, \dots, 7$ is understood (a repeated upper and lower index is summed), $m$ is the mass, $S = \bar\Psi\Psi = \Psi^\dagger C\Psi$ is the scalar built from the field and its **Dirac adjoint** $\bar\Psi = \Psi^\dagger C$ (the dagger means: transpose and take the complex conjugate of every entry), $U(S) = \frac{\lambda}{2}S^2$ is the potential, and $U'(S) = \lambda S$. The matrices $\Omega_\mu$ are the **spinor connection**, built from the canonical spin connection in Section 8.4. Everything in this chapter is a statement about this matrix equation; it holds for both fields (for the Grassmann field, "$\Psi \neq 0$" means a configuration that is not identically zero). Written out in the diagonal frame the equation reads (`Revision/theory/field-theory.json`, formula key `field_equation`; Section 8.5 derives the last two terms on the left):

$$
\begin{aligned}
&e^{a_4}b_4^{-1/2}\tan z\,\gamma^{(0)}\partial_0\Psi + e^{-a_4}\big(\gamma^{(1)}\partial_1 + \gamma^{(2)}\partial_2 + \gamma^{(3)}\partial_3\big)\Psi + \gamma^{(4)}\partial_4\Psi \\
&\quad + e^{a_4}b_4^{-1/2}(\sin^2 z)^{-1/12}\big(\gamma^{(5)}\partial_5 + \gamma^{(6)}\partial_6 + \gamma^{(7)}\partial_7\big)\Psi + c_g\gamma^{(0)}\Psi + v_g\gamma^{(4)}\Psi = \big(m + U'(S)\big)\Psi ,
\end{aligned}
$$

$$
c_g = \tfrac32He^{a_4}b_4^{-1/2}, \qquad v_g = \frac{b_4'}{b_4} - \frac{a_4'}{2} .
$$

The derivative terms are $\sum_\mu\gamma^\mu\partial_\mu\Psi = \sum_\mu(\gamma^{(\mu)}/f_\mu)\partial_\mu\Psi$, with $1/f_0 = e^{a_4}b_4^{-1/2}\tan z$, $1/f_i = e^{-a_4}$, $1/f_4 = 1$ and $1/f_t = e^{a_4}b_4^{-1/2}(\sin^2 z)^{-1/12}$. These factors are the **frame factors**: they carry the metric into every derivative term.

**Units.** $H$, $m$ and every momentum are measured in one unit, an inverse length, and the coordinates in its inverse; every printed number is a pure number in this unit. The examples use $H = m = 1$, the values of the Kohn-Sham record (Notebook 08d also uses $m = 2$).

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

**The boost in the $(x_4, x_0)$ plane.** The **hyperbolic functions** are $\cosh b = (e^b + e^{-b})/2$ and $\sinh b = (e^b - e^{-b})/2$. They obey

$$
\cosh^2 b - \sinh^2 b = \frac{(e^b + e^{-b})^2 - (e^b - e^{-b})^2}{4} = \frac{4e^be^{-b}}{4} = 1 ,
$$

where the middle step expands both squares ($e^{2b} + 2 + e^{-2b}$ minus $e^{2b} - 2 + e^{-2b}$ leaves $4$). The **boost** with **rapidity** $b$ mixes the time-like frame vector of $x_4$ and the space-like frame vector of $x_0$:

$$
e'^{(4)} = \cosh b\;e^{(4)} + \sinh b\;e^{(0)}, \qquad e'^{(0)} = \sinh b\;e^{(4)} + \cosh b\;e^{(0)},
$$

and keeps the other six. It keeps the frame metric: the two mixed vectors enter the metric as $-e'^{(4)}e'^{(4)} + e'^{(0)}e'^{(0)}$ (products of components at the same $\mu$ and $\nu$), and

$$
\begin{aligned}
-e'^{(4)}e'^{(4)} + e'^{(0)}e'^{(0)} &= -\big(\cosh^2 b\,e^{(4)}e^{(4)} + 2\cosh b\sinh b\,e^{(4)}e^{(0)} + \sinh^2 b\,e^{(0)}e^{(0)}\big) \\
&\quad + \big(\sinh^2 b\,e^{(4)}e^{(4)} + 2\sinh b\cosh b\,e^{(4)}e^{(0)} + \cosh^2 b\,e^{(0)}e^{(0)}\big) \\
&= -(\cosh^2 b - \sinh^2 b)\,e^{(4)}e^{(4)} + (\cosh^2 b - \sinh^2 b)\,e^{(0)}e^{(0)} \\
&= -e^{(4)}e^{(4)} + e^{(0)}e^{(0)} .
\end{aligned}
$$

The first two lines multiply out the two squares (here $e^{(4)}e^{(0)}$ stands for the symmetric combination of the two orders), the third collects the terms (the mixed terms cancel), and the fourth uses $\cosh^2 b - \sinh^2 b = 1$. The rapidity may change from point to point; we take it to be any function $b(x_4)$ of the time (for example $b = \beta x_4 + b_0$ with two constants: the **rapidity rate** $\beta$ and $b_0$), a different boost at every time. Every such frame describes the author's metric exactly (PROVED; `Revision/theory/reports/python-scope.json`, check `boosted_frame_reproduces_metric`, and the same check of `wolfram-scope.json`).

**The principle.** A change of frame changes the spin connection and the coordinate gammas, and the field changes with it, $\Psi' = S\Psi$ with an invertible $16 \times 16$ matrix $S(x)$ (Section 8.9 finds $S$ for the boost). A statement about the field equation is a property of the equation itself only if it holds in every frame. A statement that holds in one frame only describes how we chose to write the equation.

### 8.4 The Christoffel symbols and the canonical spin connection of the diagonal frame

**Christoffel symbols.** The **Christoffel symbols** $\Gamma^\lambda{}_{\mu\nu}$ say how the coordinate directions turn from point to point (Chapter 3). For a diagonal metric they are

$$
\Gamma^\lambda{}_{\mu\nu} = \frac{1}{2g_{\lambda\lambda}}\big(\partial_\mu g_{\lambda\nu} + \partial_\nu g_{\lambda\mu} - \partial_\lambda g_{\mu\nu}\big),
$$

and they are symmetric in the two lower indices. The corrected metric depends only on $x_4$ (through $a_4$ and $b_4$) and on $x_0$ (through $z$), and $dz/dx_0 = 6H$. Two rules give every symbol. First, for a diagonal metric only two shapes survive: $\Gamma^\mu{}_{\mu\nu}$ (the upper index equal to one lower index) and $\Gamma^\lambda{}_{\mu\mu}$ with $\lambda \neq \mu$; every other choice of indices meets an off-diagonal entry of $g$ in each of the three terms, and those are zero. Second, line by line,

$$
\begin{aligned}
\Gamma^\mu{}_{\mu\nu} &= \frac{\partial_\nu g_{\mu\mu}}{2g_{\mu\mu}} = \frac{2\eta_{\mu\mu}f_\mu\,\partial_\nu f_\mu}{2\eta_{\mu\mu}f_\mu^2} = \partial_\nu\ln|f_\mu| \quad (\text{no sum over } \mu), \\
\Gamma^\lambda{}_{\mu\mu} &= -\frac{\partial_\lambda g_{\mu\mu}}{2g_{\lambda\lambda}} \quad (\lambda \neq \mu).
\end{aligned}
$$

The first line keeps the one term of the formula that survives for $\lambda = \mu \neq \nu$ (for $\lambda = \mu = \nu$ the three terms are $\partial_\mu g_{\mu\mu} + \partial_\mu g_{\mu\mu} - \partial_\mu g_{\mu\mu}$, which gives the same formula) and differentiates $g_{\mu\mu} = \eta_{\mu\mu}f_\mu^2$ by the chain rule; the second keeps the one term that survives for $\lambda \neq \mu = \nu$. We need two derivatives of the hidden factors, each by the chain rule with $dz/dx_0 = 6H$:

$$
\begin{aligned}
\partial_0\ln|\cot z| &= 6H\cdot\frac{-1/\sin^2 z}{\cot z} = -\frac{6H}{\sin z\cos z} = -\frac{12H}{\sin(12Hx_0)}, \\
\partial_0\ln W &= \frac{1}{12}\cdot\frac{2\sin z\cos z\cdot 6H}{\sin^2 z} = H\cot z ,
\end{aligned}
$$

using $\frac{d}{dz}\cot z = -1/\sin^2 z$, $2\sin z\cos z = \sin 2z$ and, for $W = (\sin^2 z)^{1/12}$, $\ln W = \frac{1}{12}\ln\sin^2 z$. With $s_b = e^{-a_4}b_4^{1/2}$ and $h_4 = \partial_4\ln s_b$ the rules give exactly 21 independent nonzero symbols (PROVED; `python-field-theory.json`, check `christoffel_symmetric_metric_compatible`, and `wolfram-field-theory.json`, check `christoffel_count`; formula key `christoffel_nonzero`):

| symbol | value | rule |
| --- | --- | --- |
| $\Gamma^{x_0}{}_{x_0x_0}$ | $-12H/\sin(12Hx_0)$ | $\partial_0\ln\lvert\cot z\rvert$ |
| $\Gamma^{x_0}{}_{x_0x_4}$ | $h_4$ | $\partial_4\ln s_b$ |
| $\Gamma^{x_i}{}_{x_ix_4}$ | $a_4'$ | $\partial_4\ln e^{a_4}$ |
| $\Gamma^{x_t}{}_{x_tx_4}$ | $h_4$ | $\partial_4\ln s_b$ |
| $\Gamma^{x_t}{}_{x_tx_0}$ | $H\cot z$ | $\partial_0\ln W$ |
| $\Gamma^{x_4}{}_{x_0x_0}$ | $e^{-2a_4}b_4\cot^2 z\;h_4$ | $\partial_4 g_{00}/2$ |
| $\Gamma^{x_4}{}_{x_ix_i}$ | $e^{2a_4}a_4'$ | $\partial_4 g_{ii}/2$ |
| $\Gamma^{x_4}{}_{x_tx_t}$ | $-e^{-2a_4}b_4(\sin^2 z)^{1/6}\,h_4$ | $\partial_4 g_{tt}/2$ |
| $\Gamma^{x_0}{}_{x_tx_t}$ | $H(\sin^2 z)^{1/6}\tan z$ | $-\partial_0 g_{tt}/(2g_{00})$ |

Each of the rows with an $i$ or a $t$ stands for three symbols; so the count is $1 + 1 + 3 + 3 + 3 + 1 + 3 + 3 + 3 = 21$. The rows with $x_4$ as the upper index use $g_{44} = -1$, so $-\partial_4 g_{\mu\mu}/(2g_{44}) = \partial_4 g_{\mu\mu}/2$, and $\partial_4 g_{\mu\mu} = 2(\partial_4\ln|f_\mu|)g_{\mu\mu}$: this gives $h_4g_{00}$, $a_4'g_{ii}$ and $h_4g_{tt}$. The last row: $\partial_0 g_{tt} = 2(\partial_0\ln W)g_{tt} = 2H\cot z\,g_{tt}$, so $-\partial_0 g_{tt}/(2g_{00}) = -H\cot z\,g_{tt}/g_{00} = H\cot z\,s_b^2W^2/(s_b^2\cot^2 z) = HW^2\tan z$. Two facts are worth noticing. The hidden direction follows the extra times in time: $\Gamma^{x_0}{}_{x_0x_4} = \Gamma^{x_t}{}_{x_tx_4} = h_4$. And 3-space does not see $x_0$: no symbol mixes $x_i$ with $x_0$.

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

- $a = b$: $\omega_\mu{}^a{}_a = f_a\partial_\mu(1/f_a) + \Gamma^a{}_{\mu a} = -\partial_\mu\ln|f_a| + \partial_\mu\ln|f_a| = 0$, by the derivative of $1/f$ ($f\,\partial(1/f) = -\partial f/f$) and the first rule above.
- $a \neq b$: $\delta^a_b = 0$, so $\omega_\mu{}^a{}_b = (f_a/f_b)\,\Gamma^a{}_{\mu b}$.

So a component with $a \neq b$ is nonzero exactly when the Christoffel symbol $\Gamma^a{}_{\mu b}$ is. Reading the table with $a \neq b$: for $\mu = x_4$ every symbol $\Gamma^a{}_{x_4b}$ with $a \neq b$ vanishes, so $\omega_{x_4} = 0$; for $\mu = x_0$ the symbols are $\Gamma^{x_0}{}_{x_0x_4}$ and $\Gamma^{x_4}{}_{x_0x_0}$; for $\mu = x_i$ they are $\Gamma^{x_i}{}_{x_ix_4}$ and $\Gamma^{x_4}{}_{x_ix_i}$; for $\mu = x_t$ they are $\Gamma^{x_t}{}_{x_tx_4}$, $\Gamma^{x_4}{}_{x_tx_t}$, $\Gamma^{x_t}{}_{x_tx_0}$ and $\Gamma^{x_0}{}_{x_tx_t}$. We compute one member of each antisymmetric pair, with $a < b$, line by line:

- $\omega_{x_0}{}^{(0)}{}_{(4)} = (f_0/f_4)\,\Gamma^{x_0}{}_{x_0x_4} = s_b\cot z\cdot h_4$, and lowering with $\eta_{00} = +1$: $\omega_{x_0\,(0)(4)} = h_4\,s_b\cot z$.
- $\omega_{x_i}{}^{(i)}{}_{(4)} = (f_i/f_4)\,\Gamma^{x_i}{}_{x_ix_4} = e^{a_4}\cdot a_4'$, and lowering with $\eta_{ii} = +1$: $\omega_{x_i\,(i)(4)} = a_4'e^{a_4}$.
- $\omega_{x_t}{}^{(4)}{}_{(t)} = (f_4/f_t)\,\Gamma^{x_4}{}_{x_tx_t} = \frac{1}{s_bW}\cdot\big(-s_b^2W^2h_4\big) = -h_4\,s_bW$, and lowering with $\eta_{44} = -1$: $\omega_{x_t\,(4)(t)} = h_4\,s_b\,W$.
- $\omega_{x_t}{}^{(0)}{}_{(t)} = (f_0/f_t)\,\Gamma^{x_0}{}_{x_tx_t} = \frac{s_b\cot z}{s_bW}\cdot HW^2\tan z = HW$ (because $\cot z\tan z = 1$), and lowering with $\eta_{00} = +1$: $\omega_{x_t\,(0)(t)} = HW$.

Antisymmetry can be seen on one example: $\omega_{x_i}{}^{(4)}{}_{(i)} = (f_4/f_i)\Gamma^{x_4}{}_{x_ix_i} = e^{-a_4}\cdot e^{2a_4}a_4' = a_4'e^{a_4}$, and lowering with $\eta_{44} = -1$ gives $\omega_{x_i\,(4)(i)} = -a_4'e^{a_4} = -\omega_{x_i\,(i)(4)}$. With three values of $i$ and three of $t$ this gives exactly $1 + 3 + 3 + 3 = 10$ independent nonzero components $\omega_{\mu ab}$ with $a < b$ (PROVED; `Revision/theory/reports/wolfram-field-theory.json`, check `omega_components`; formula key `omega_nonzero`).

**The spinor connection.** The **generators** $S^{ab} = \frac14[\gamma^{(a)}, \gamma^{(b)}]$, with the **commutator** $[A, B] = AB - BA$, are, for $a \neq b$, $S^{ab} = \frac14(\gamma^{(a)}\gamma^{(b)} - \gamma^{(b)}\gamma^{(a)}) = \frac14(2\gamma^{(a)}\gamma^{(b)}) = \frac12\gamma^{(a)}\gamma^{(b)}$ (because the two gammas anticommute). The spinor connection is $\Omega_\mu = \frac12\sum_{a,b}\omega_{\mu ab}S^{ab} = \sum_{a<b}\omega_{\mu ab}S^{ab}$ (the pairs $(a, b)$ and $(b, a)$ give equal terms, because both $\omega_{\mu ab}$ and $S^{ab}$ change sign). Inserting the components:

$$
\begin{aligned}
\Omega_{x_0} &= \omega_{x_0(0)(4)}S^{04} = \tfrac12\,h_4\,s_b\cot z\;\gamma^{(0)}\gamma^{(4)}, \\
\Omega_{x_i} &= \omega_{x_i(i)(4)}S^{i4} = \tfrac12\,a_4'e^{a_4}\,\gamma^{(i)}\gamma^{(4)}, \\
\Omega_{x_t} &= \omega_{x_t(0)(t)}S^{0t} + \omega_{x_t(4)(t)}S^{4t} = \tfrac12\,W\big(h_4\,s_b\,\gamma^{(4)}\gamma^{(t)} + H\,\gamma^{(0)}\gamma^{(t)}\big), \\
\Omega_{x_4} &= 0 .
\end{aligned}
$$

These are the formulas of the record (`Revision/theory/field-theory.json`, formula key `Omega_components`; `python-field-theory.json`, check `Omega_x4_vanishes_Omega_x0_does_not`). Two exact properties of this connection are used below. It makes the gammas **covariantly constant**: $\partial_\mu\gamma^\nu + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}\gamma^\lambda + [\Omega_\mu, \gamma^\nu] = 0$ for all 64 pairs $(\mu, \nu)$ (PROVED; `python-field-theory.json`, check `covariant_constancy_D_mu_gamma_nu`). And its **curvature** $F_{\mu\nu} = \partial_\mu\Omega_\nu - \partial_\nu\Omega_\mu + [\Omega_\mu, \Omega_\nu]$ equals $\frac14\sum_{\rho,\sigma}R_{\rho\sigma\mu\nu}\gamma^\rho\gamma^\sigma$, where $R_{\rho\sigma\mu\nu}$ is the Riemann tensor of the metric with its first index lowered (PROVED; `python-field-theory.json`, check `spinor_curvature_equals_riemann`, and `wolfram-field-theory.json`, check `spin_curvature_equals_Riemann`).

### 8.5 What cancels and what survives: the term $\gamma^\mu\Omega_\mu = G$

The gravitational term of the field equation is $\gamma^\mu D_\mu\Psi - \gamma^\mu\partial_\mu\Psi = \gamma^\mu\Omega_\mu\Psi$. We compute the matrix $\gamma^\mu\Omega_\mu$ direction by direction (no sum), then add.

**The hidden direction $x_0$.** Line by line:

$$
\begin{aligned}
\gamma^{x_0}\Omega_{x_0} &= \frac{\gamma^{(0)}}{s_b\cot z}\cdot\tfrac12\,h_4\,s_b\cot z\;\gamma^{(0)}\gamma^{(4)} \\
&= \tfrac12h_4\,\gamma^{(0)}\gamma^{(0)}\gamma^{(4)} = \tfrac12h_4\,\gamma^{(4)} .
\end{aligned}
$$

The first line inserts $\gamma^{x_0} = \gamma^{(0)}/f_0$ and $\Omega_{x_0}$; the second cancels the factor $s_b\cot z$ against its inverse (its sign cancels too) and uses $(\gamma^{(0)})^2 = +I_{16}$.

**A 3-space direction $x_i$.** Line by line:

$$
\gamma^{x_i}\Omega_{x_i} = \frac{\gamma^{(i)}}{e^{a_4}}\cdot\tfrac12 a_4'e^{a_4}\,\gamma^{(i)}\gamma^{(4)} = \tfrac12 a_4'\,\gamma^{(i)}\gamma^{(i)}\gamma^{(4)} = \tfrac12 a_4'\,\gamma^{(4)} .
$$

The first step inserts $\gamma^{x_i} = \gamma^{(i)}/f_i$ and $\Omega_{x_i}$; the second cancels the scale factor; the third uses $(\gamma^{(i)})^2 = +I_{16}$ (a space-like direction).

**An extra time $x_t$.** Line by line:

$$
\begin{aligned}
\gamma^{x_t}\Omega_{x_t} &= \frac{\gamma^{(t)}}{s_bW}\cdot\tfrac12W\big(h_4\,s_b\,\gamma^{(4)}\gamma^{(t)} + H\,\gamma^{(0)}\gamma^{(t)}\big) \\
&= \tfrac12h_4\,\gamma^{(t)}\gamma^{(4)}\gamma^{(t)} + \frac{H}{2s_b}\,\gamma^{(t)}\gamma^{(0)}\gamma^{(t)} \\
&= -\tfrac12h_4\,\gamma^{(4)}\gamma^{(t)}\gamma^{(t)} - \frac{H}{2s_b}\,\gamma^{(0)}\gamma^{(t)}\gamma^{(t)} \\
&= \tfrac12h_4\,\gamma^{(4)} + \tfrac12He^{a_4}b_4^{-1/2}\,\gamma^{(0)} .
\end{aligned}
$$

The first line inserts $\gamma^{x_t} = \gamma^{(t)}/f_t$ and $\Omega_{x_t}$; the second cancels $W$ in both terms and $s_b$ in the first; the third moves the first $\gamma^{(t)}$ to the right past $\gamma^{(4)}$ and past $\gamma^{(0)}$, which changes the sign once (they anticommute); the fourth uses $(\gamma^{(t)})^2 = -I_{16}$ (a time-like direction) in both terms and $1/s_b = e^{a_4}b_4^{-1/2}$.

**The time $x_4$.** $\Omega_{x_4} = 0$, so $\gamma^{x_4}\Omega_{x_4} = 0$.

**The sum.** The coefficient of $\gamma^{(4)}$ is, line by line,

$$
\begin{aligned}
\tfrac12h_4 + 3\cdot\tfrac12a_4' + 3\cdot\tfrac12h_4 &= 2h_4 + \tfrac32a_4' \\
&= \frac{b_4'}{b_4} - 2a_4' + \tfrac32a_4' = \frac{b_4'}{b_4} - \frac{a_4'}{2} = v_g .
\end{aligned}
$$

The first line adds the hidden direction, the three 3-space directions and the three extra times; the second inserts $h_4 = b_4'/(2b_4) - a_4'$ and collects. The coefficient of $\gamma^{(0)}$ is $3\cdot\frac12He^{a_4}b_4^{-1/2} = c_g$: only the three extra times contribute. Hence

$$
\gamma^\mu\Omega_\mu = G = c_g\gamma^{(0)} + v_g\gamma^{(4)}, \qquad c_g = \tfrac32He^{a_4}b_4^{-1/2}, \qquad v_g = \frac{b_4'}{b_4} - \frac{a_4'}{2},
$$

for all functions $a_4(x_4)$ and $b_4(x_4)$, every $H > 0$ and every point between the degenerate points; it does not depend on $x_0$. This is PROVED, and the Revision record proves it in two independent reports:

- the sympy report `python-field-theory.json`, with the checks `per_direction_terms` and `gamma_mu_Omega_mu_equals_hidden_block_terms`;
- the Wolfram report `wolfram-field-theory.json`, with the checks `gammaOmega_per_direction` and `gammaOmega_total`.

What cancels and what survives, in words. Split each $\gamma^{(4)}$ piece into its part with $a_4'$ and its part with $b_4'/b_4$. The three 3-space directions give $+\frac12a_4'$ each and the three extra times $-\frac12a_4'$ each: these six cancel exactly, because 3-space carries $e^{a_4}$ and the extra times carry $e^{-a_4}$. The hidden direction adds one more $-\frac12a_4'$, because it carries $e^{-a_4}$ too: that is the $-\frac12a_4'$ of $v_g$. The four directions of the hidden block give $\frac14b_4'/b_4$ each, because each carries $b_4^{1/2}$: together $b_4'/b_4$. So $v_g$ is half the rate at which the volume factor changes in time, $v_g = \frac12\partial_4\ln\sqrt{|g|} = \frac12(2b_4'/b_4 - a_4')$, as the divergence form below shows again. On the history of the record (with $b_4(0) = 1$) $c_g = \frac32He^{AHx_4}e^{-\frac23AHx_4} = \frac32He^{AHx_4/3}$ and $v_g = \frac43AH - \frac12AH = \frac56AH$. In the withdrawn metric of 2026-10-14 the same computation gave $3H\gamma^{(0)} + \frac34(b_4'/b_4)\gamma^{(4)}$ (the record keeps this value for comparison in the detail of the check `gamma_mu_Omega_mu_equals_hidden_block_terms`).

**The divergence form.** The same matrix has a second, shorter formula. The first rule of Section 8.4, summed over $\mu$, gives $\sum_\mu\Gamma^\mu{}_{\mu\nu} = \partial_\nu\ln|f_0\cdots f_7| = \partial_\nu\ln\sqrt{|g|}$. Now sum the covariant constancy of Section 8.4 over $\mu = \nu$:

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

For the author's metric only $\mu = x_0$ and $\mu = x_4$ contribute. Write $\sqrt{|g|} = \sigma f_0f_1\cdots f_7$, where $\sigma = \pm1$ is the sign of $\cot z$ (constant on each half of a cell). First, line by line,

$$
\begin{aligned}
\sqrt{|g|}\,\gamma^{x_0} &= \sigma f_0\cdots f_7\,\frac{\gamma^{(0)}}{f_0} = \sigma f_1\cdots f_7\,\gamma^{(0)} = \sigma b_4^{3/2}(\sin^2 z)^{1/4}\,\gamma^{(0)}, \\
\partial_0\big(\sqrt{|g|}\,\gamma^{x_0}\big) &= \sigma b_4^{3/2}\cdot\tfrac14(\sin^2 z)^{-3/4}\cdot 2\sin z\cos z\cdot 6H\,\gamma^{(0)} = 3H\sigma b_4^{3/2}\cot z\,(\sin^2 z)^{1/4}\,\gamma^{(0)}, \\
\frac{1}{2\sqrt{|g|}}\,\partial_0\big(\sqrt{|g|}\,\gamma^{x_0}\big) &= \frac{3H\sigma b_4^{3/2}\cot z\,(\sin^2 z)^{1/4}}{2\sigma e^{-a_4}b_4^2\cot z\,(\sin^2 z)^{1/4}}\,\gamma^{(0)} = \tfrac32He^{a_4}b_4^{-1/2}\,\gamma^{(0)} = c_g\gamma^{(0)} .
\end{aligned}
$$

The first line divides out $f_0$ and multiplies the seven other factors ($e^{3a_4}e^{-3a_4}b_4^{3/2}W^3$); the second differentiates $(\sin^2 z)^{1/4}$ by the power rule and the chain rule and writes $(\sin^2 z)^{-3/4}\sin z\cos z = \cot z\,(\sin^2 z)^{1/4}$; the third divides by $2\sqrt{|g|} = 2\sigma e^{-a_4}b_4^2\cot z\,(\sin^2 z)^{1/4}$, and $\sigma$, $\cot z$ and $(\sin^2 z)^{1/4}$ cancel. Second, $\sqrt{|g|}\gamma^{x_4} = \sqrt{|g|}\,\gamma^{(4)}$ ($f_4 = 1$), so $\frac{1}{2\sqrt{|g|}}\partial_4(\sqrt{|g|}\gamma^{(4)}) = \frac12(2b_4'/b_4 - a_4')\gamma^{(4)} = v_g\gamma^{(4)}$ by the derivative of the volume factor in Section 8.2. The other six terms vanish because nothing depends on $x_1, x_2, x_3, x_5, x_6, x_7$ (PROVED; `python-field-theory.json`, check `divergence_of_sqrtg_gamma`, and `wolfram-field-theory.json`, check `gammaOmega_divergence_form`). In words: the term is half the divergence of the coordinate gammas weighted with the volume factor, a **half-density term**.

### 8.6 Non-triviality: the connection vanishes only in the formal flat limit

**The connection is zero only in the formal limit.** Each of the 10 components of Section 8.4 is one of three numbers times a factor. Three components (3-space) are $a_4'$ times the factor $e^{a_4}$. Four (the hidden direction and the three extra times) are the rate $h_4 = b_4'/(2b_4) - a_4'$ times one of the factors $s_b\cot z$ and $s_bW$. Three (the extra times) are $H$ times the factor $W$. The factors are never zero between the degenerate points: an exponential is never zero, $b_4 > 0$, $W > 0$, and $\cot z \neq 0$ away from the folds. The 28 matrices $S^{ab}$ with $a < b$ are **linearly independent**: no combination of them with coefficients that are not all zero gives the zero matrix (Notebook 08c checks it: written as 28 rows of $16 \times 16 = 256$ numbers they have rank 28). So, line by line:

1. $\Omega_\mu = \sum_{a<b}\omega_{\mu ab}S^{ab}$ is zero exactly when all its coefficients $\omega_{\mu ab}$ are zero (linear independence).
2. If $a_4' \neq 0$, the three components of the form $a_4'\times$(factor) are not zero; if $h_4 \neq 0$, the four of the form $h_4\times$(factor) are not zero; if $H \neq 0$, the three of the form $H\times$(factor) are not zero.
3. Therefore $\Omega_\mu = 0$ for every $\mu$ if and only if $a_4' = 0$, $h_4 = 0$ and $H = 0$. With $a_4' = 0$, the condition $h_4 = 0$ says $b_4' = 0$; so the condition is $a_4' = 0$, $b_4' = 0$ and $H = 0$.

The case $H = 0$ is a formal limit; it is not a member of the author's family (Section 8.2). For every metric of the family the canonical spin connection of the diagonal frame is therefore not zero. This is PROVED; in the Revision record it is the check `nontriviality_Omega_zero_iff_flat` of the sympy report `python-field-theory.json` and the check `Omega_vanishes_iff_a4prime_b4prime_and_H_vanish` of the Wolfram report `wolfram-field-theory.json`. (Whether a different frame can remove the connection is a different question, answered in Section 8.10: it can exactly where the metric is flat, and the corrected metric is flat for one special history.)

**The term is not zero for any field that is not zero.** Suppose $G\Psi = 0$ at some point, and multiply from the left by $G$: $GG\Psi = 0$. Line by line,

$$
\begin{aligned}
GG &= c_g^2(\gamma^{(0)})^2 + v_g^2(\gamma^{(4)})^2 + c_gv_g\big(\gamma^{(0)}\gamma^{(4)} + \gamma^{(4)}\gamma^{(0)}\big) \\
&= \big(c_g^2 - v_g^2\big)I_{16} .
\end{aligned}
$$

The first line multiplies out $(c_g\gamma^{(0)} + v_g\gamma^{(4)})^2$; the second uses $(\gamma^{(0)})^2 = I_{16}$, $(\gamma^{(4)})^2 = -I_{16}$, and that two different gammas anticommute, so the bracket is zero. Where $c_g^2 \neq v_g^2$ the number $c_g^2 - v_g^2$ is not zero, so $GG\Psi = 0$ gives $\Psi = 0$. So in the diagonal frame the gravitational term $G\Psi$ is nonzero wherever the field is nonzero and $c_g^2 \neq v_g^2$ (PROVED; `python-field-theory.json`, check `gravity_term_square`; `wolfram-field-theory.json`, checks `nontriviality_1_dirac16complex` and `nontriviality_2_dirac16complex00`). Note that $G$ itself is never the zero matrix, because $c_g > 0$. On the history of the record, line by line,

$$
\begin{aligned}
c_g^2 - v_g^2 &= \tfrac94H^2e^{2AHx_4/3} - \tfrac{25}{36}A^2H^2 \\
&= H^2\big(\tfrac94e^{2Hx_4/3} - \tfrac{25}{36}\big) \quad (A = 1),
\end{aligned}
$$

by squaring the two coefficients found in Section 8.5. At $x_4 = 0$ this is $H^2(\frac{81}{36} - \frac{25}{36}) = \frac{14}{9}H^2 > 0$, and it grows with $x_4$; it vanishes only at $e^{2Hx_4/3} = \frac{25}{81}$, that is at the negative time $x_4 = \frac{3}{2H}\ln\frac{25}{81} \approx -1.763/H$. At a time where $c_g = \pm v_g$ the matrix $G = c_g(\gamma^{(0)} \pm \gamma^{(4)})$ has the square 0 and rank 8, and $G\Psi$ vanishes for the fields of an 8-dimensional subspace (the same check).

**What this proves, and what it does not.** Read literally, in the diagonal frame and for the field variables $\Psi$, the tests [1] and [2] hold: the field equations always contain the nonzero gravitational term $G\Psi$ (at every time $x_4 \geq 0$ of the record's history), and the spin connection of this frame vanishes only in the formal limit. Sections 8.7 to 8.10 and 8.30 make precise which parts of this statement survive a change of frame or of variables.

### 8.7 The term sees the deflating hidden block; the curvature and the flat member

**The term contains $a_4$.** The coefficient $c_g = \frac32He^{a_4}b_4^{-1/2}$ of $\gamma^{(0)}$ is $\frac32H$ times $1/s_b$, the inverse scale factor of the block of the hidden direction and the extra times: as the block deflates, $c_g$ grows (like $e^{AHx_4/3}$ on the history). And $v_g$ contains $a_4'$. So the term sees the deflation (PROVED; `Revision/theory/reports/python-scope.json`, check `gammaOmega_sees_the_hidden_block`). In the withdrawn metric of 2026-10-14 the term contained no $a_4$ at all; there, 3-space and the extra times carried the same warp and the hidden direction had no time dependence. Along the deflating history the separate pieces of the connection change in different ways: the component $\omega_{x_1\,(1)(4)} = a_4'e^{a_4}$ of the inflating direction grows like $e^{a_4}$, the components with $h_4$ of the hidden direction and of an extra time shrink like $s_b = e^{-AHx_4/3}$, and the component $\omega_{x_5\,(0)(5)} = HW$ stays constant. Contracted with the coordinate gammas, which carry the inverse factors, the pieces with $a_4'$ and $h_4$ become constant, while the pieces with $H$ become $\frac12H/s_b$ and grow; Notebook 08c draws this (Figure 08c.2).

**The Ricci tensor of the corrected metric.** The mixed Ricci tensor $R^\mu{}_\nu$ (Chapter 3) is diagonal and does not depend on $x_0$. With $k = e^{2a_4}/b_4$ and $u = b_4'/b_4$ its entries are

$$
\begin{aligned}
R^{x_0}{}_{x_0} = R^{x_t}{}_{x_t} &= -3H^2k + (a_4')^2 - a_4'' - \tfrac52a_4'u + \tfrac12\frac{b_4''}{b_4} + \tfrac12u^2, \\
R^{x_i}{}_{x_i} &= -(a_4')^2 + a_4'' + 2a_4'u, \qquad R^{x_4}{}_{x_4} = 7(a_4')^2 - a_4'' - 4a_4'u + 2\frac{b_4''}{b_4} - u^2,
\end{aligned}
$$

and the Ricci scalar is their sum, $R = 4R^{x_0}{}_{x_0} + 3R^{x_i}{}_{x_i} + R^{x_4}{}_{x_4}$. Adding term by term: $4\cdot(-3H^2k) = -12H^2k$; the $(a_4')^2$ terms give $4 - 3 + 7 = 8$; the $a_4''$ terms give $-4 + 3 - 1 = -2$; the $a_4'u$ terms give $-10 + 6 - 4 = -8$; the $b_4''/b_4$ terms give $2 + 2 = 4$; and the $u^2$ terms give $2 - 1 = 1$:

$$
R = -12H^2\frac{e^{2a_4}}{b_4} + 8(a_4')^2 - 2a_4'' - 8a_4'\frac{b_4'}{b_4} + 4\frac{b_4''}{b_4} + \Big(\frac{b_4'}{b_4}\Big)^2
$$

(PROVED; `wolfram-field-theory.json`, checks `ricci_mixed_components` and `ricci_scalar`, and `python-field-theory.json`, check `curvature_and_flat_member`; Notebook 08c computes every entry from the Christoffel symbols). The hidden direction and the extra times have the same entry: they form one block, a space of constant curvature $-H^2$ in the hidden coordinate of Section 8.24, scaled by $e^{-2a_4}b_4$.

**The flat member.** For the special history $a_4 = 0$, $b_4 = H^2x_4^2$ ($x_4 > 0$) every component of the Riemann tensor vanishes: the corrected metric is then 8-dimensional flat space written in unusual coordinates (PROVED; `wolfram-field-theory.json`, check `flat_member_and_curvature`; Notebook 08c checks all 1792 components with $\mu < \nu$). Two entries show how it happens. There $a_4' = a_4'' = 0$, $u = 2/x_4$, $b_4''/b_4 = 2/x_4^2$ and $k = 1/(H^2x_4^2)$, so $R^{x_4}{}_{x_4} = 2\cdot\frac{2}{x_4^2} - \frac{4}{x_4^2} = 0$ and $R^{x_0}{}_{x_0} = -\frac{3}{x_4^2} + \frac{1}{x_4^2} + \frac{2}{x_4^2} = 0$. Yet in the diagonal frame the term is not zero there: $c_g = \frac32H(H^2x_4^2)^{-1/2} = \frac{3}{2x_4}$ and $v_g = \frac{2}{x_4}$, so $G = \frac{3}{2x_4}\gamma^{(0)} + \frac{2}{x_4}\gamma^{(4)} \neq 0$. On this member the term is a pure frame effect: a suitable frame removes the whole connection (Section 8.10). This is the case "flat 4+4 spacetime" of the test [1].

**The history of the record is curved.** On the history $a_4' = AH$, $a_4'' = 0$ and $u = \frac43AH$, so $R^{x_i}{}_{x_i} = -A^2H^2 + 2\cdot AH\cdot\frac43AH = \frac53A^2H^2 \neq 0$ at every time: the metric is curved there, at every point (PROVED; the same checks, and Notebook 08c prints $R^{x_1}{}_{x_1} = 5H^2/3$ for $A = 1$).

**Where else the deflation enters.** It enters the field equation through the frame factors of the derivative terms (Section 8.2): the 3-space derivatives carry $e^{-a_4}$, which shrinks as 3-space inflates, and the derivatives along the hidden direction and the extra times carry $e^{a_4}b_4^{-1/2}\tan z$ and $e^{a_4}b_4^{-1/2}(\sin^2 z)^{-1/12}$, which grow as the block deflates (like $e^{AHx_4/3}$ on the history). Sections 8.24 and 8.25 show what this growth does to waves.

### 8.8 The connection drops out of the Lagrangian but not out of the field equation

**An anticommutation for each direction.** For each $\mu$ separately (no sum), $\{\gamma^\mu, \Omega_\mu\} = 0$. Each $\Omega_\mu$ is a combination of products $\gamma^{(\mu)}\gamma^{(b)}$ or $\gamma^{(b)}\gamma^{(\mu)}$ that contain the gamma of the same direction $\mu$ and one other gamma; so it suffices to check, for $b \neq \mu$,

$$
\gamma^{(\mu)}\big(\gamma^{(\mu)}\gamma^{(b)}\big) + \big(\gamma^{(\mu)}\gamma^{(b)}\big)\gamma^{(\mu)} = \eta_{\mu\mu}\gamma^{(b)} - \gamma^{(\mu)}\gamma^{(\mu)}\gamma^{(b)} = \eta_{\mu\mu}\gamma^{(b)} - \eta_{\mu\mu}\gamma^{(b)} = 0 ,
$$

using $(\gamma^{(\mu)})^2 = \eta_{\mu\mu}I_{16}$ in the first term, moving $\gamma^{(\mu)}$ to the left past $\gamma^{(b)}$ in the second (one sign change), and then the square again. For $\mu = x_0$ the product is $\gamma^{(0)}\gamma^{(4)}$; for $\mu = x_i$ it is $\gamma^{(i)}\gamma^{(4)}$; for $\mu = x_t$ the products are $\gamma^{(4)}\gamma^{(t)} = -\gamma^{(t)}\gamma^{(4)}$ and $\gamma^{(0)}\gamma^{(t)} = -\gamma^{(t)}\gamma^{(0)}$, each of the checked kind up to a sign; for $\mu = x_4$ the connection is zero. (PROVED; `python-scope.json`, check `connection_free_lagrangian_same_equations`, and `python-field-theory.json`, check `anticommutator_gamma_Omega_vanishes`.)

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

The first line differentiates the terms that contain $\bar\Psi$ without a derivative ($\partial S/\partial\bar\Psi = \Psi$ and $\partial U/\partial\bar\Psi = U'(S)\Psi$); the second differentiates the one term that contains $\partial_\mu\bar\Psi$; the third subtracts the derivative of the second line, using the product rule $\partial_\mu(\sqrt{|g|}\gamma^\mu\Psi) = \partial_\mu(\sqrt{|g|}\gamma^\mu)\Psi + \sqrt{|g|}\gamma^\mu\partial_\mu\Psi$; the fourth collects the two halves of $\gamma^\mu\partial_\mu\Psi$. Setting it to zero and using the divergence form of Section 8.5 gives exactly $\gamma^\mu\partial_\mu\Psi + G\Psi = (m + U')\Psi$, the field equation of Section 8.2. (The record proves the same for the Grassmann field with left derivatives: `python-field-theory.json`, check `grassmann_euler_lagrange_psibar_variation`.)

So the gravitational term $G\Psi$ is at the same time the term that the canonical spin connection produces and the half-density term that the volume factor produces when a Lagrangian without any spin connection is varied (PROVED; `python-scope.json`, check `connection_free_lagrangian_same_equations`, both engines). This is the first hint that the value $G$ is not a deep property of gravity's coupling: the next two sections make that precise.

### 8.9 Another frame: the boosted frame and its term

Take the boosted frame of Section 8.3, with any rapidity $b(x_4)$. Its canonical spin connection (computed from the definition of Section 8.4 with the new frame) satisfies the vielbein postulate and is antisymmetric (PROVED; `python-scope.json`, check `boosted_frame_canonical_connection`). The record then finds, exactly, for all functions $a_4$ and $b_4$, every $H > 0$ and every real $z$, for the rapidity $b = \beta x_4 + b_0$:

$$
\gamma'^\mu\Omega'_\mu = \Big(c_g - \frac{\beta}{2}\Big)\big(\cosh b\,\gamma^{(0)} - \sinh b\,\gamma^{(4)}\big) + v_g\big(\cosh b\,\gamma^{(4)} - \sinh b\,\gamma^{(0)}\big)
$$

(PROVED; `python-scope.json`, check `boosted_frame_gammaOmega_formula`, and the same check of `wolfram-scope.json`). For a general rapidity $b(x_4)$ the constant $\beta$ is replaced by the rate $b' = db/dx_4$ at each time; Notebook 08c computes that general formula from the definitions, with sympy. Here we derive it by a shorter route that also explains it.

**Step 1: the matrix that moves the gammas.** Let $J = \gamma^{(4)}\gamma^{(0)}$. Its square is $J^2 = \gamma^{(4)}\gamma^{(0)}\gamma^{(4)}\gamma^{(0)} = -\gamma^{(4)}\gamma^{(4)}\gamma^{(0)}\gamma^{(0)} = -(-I_{16})(I_{16}) = I_{16}$ (anticommute the middle pair, then use the two squares). For a matrix with $J^2 = I_{16}$ the exponential series splits into even and odd powers, and $e^{\theta J} = \cosh\theta\,I_{16} + \sinh\theta\,J$. Define

$$
S = e^{-(b/2)J} = \cosh\tfrac b2\,I_{16} - \sinh\tfrac b2\,J, \qquad S^{-1} = e^{(b/2)J} = \cosh\tfrac b2\,I_{16} + \sinh\tfrac b2\,J .
$$

**Step 2: what $S$ does to each gamma.** $J$ commutes with $\gamma^{(a)}$ for $a \neq 4, 0$ (moving $\gamma^{(a)}$ past the two factors of $J$ changes the sign twice), so $S\gamma^{(a)}S^{-1} = \gamma^{(a)}$ for those six directions. $J$ anticommutes with $\gamma^{(4)}$ and with $\gamma^{(0)}$. To see it for $\gamma^{(4)}$, move $\gamma^{(4)}$ from the left of $J = \gamma^{(4)}\gamma^{(0)}$ to its right: passing the factor $\gamma^{(4)}$ (itself) changes nothing, and passing the factor $\gamma^{(0)}$ changes the sign once, so $\gamma^{(4)}J = \gamma^{(4)}\gamma^{(4)}\gamma^{(0)} = -\gamma^{(4)}\gamma^{(0)}\gamma^{(4)} = -J\gamma^{(4)}$. For $\gamma^{(0)}$ it is the same with the roles exchanged: passing $\gamma^{(4)}$ changes the sign once and passing $\gamma^{(0)}$ changes nothing, so $\gamma^{(0)}J = \gamma^{(0)}\gamma^{(4)}\gamma^{(0)} = -\gamma^{(4)}\gamma^{(0)}\gamma^{(0)} = -J\gamma^{(0)}$. Because $\gamma^{(4)}$ anticommutes with $J$, it turns every power $J^n$ into $(-J)^n$ when it is moved past it, so $\gamma^{(4)}e^{\theta J} = e^{-\theta J}\gamma^{(4)}$ for every number $\theta$; in particular $S\gamma^{(4)} = e^{-(b/2)J}\gamma^{(4)} = \gamma^{(4)}e^{(b/2)J} = \gamma^{(4)}S^{-1}$, and line by line

$$
\begin{aligned}
S\gamma^{(4)}S^{-1} &= \gamma^{(4)}S^{-1}S^{-1} = \gamma^{(4)}e^{bJ} = \gamma^{(4)}\big(\cosh b\,I_{16} + \sinh b\,\gamma^{(4)}\gamma^{(0)}\big) \\
&= \cosh b\,\gamma^{(4)} + \sinh b\,(\gamma^{(4)})^2\gamma^{(0)} = \cosh b\,\gamma^{(4)} - \sinh b\,\gamma^{(0)} .
\end{aligned}
$$

The first line moves $S$ to the right of $\gamma^{(4)}$ (it becomes $S^{-1}$), multiplies the two exponentials ($e^{(b/2)J}e^{(b/2)J} = e^{bJ}$) and writes out $e^{bJ}$; the second multiplies out and uses $(\gamma^{(4)})^2 = -I_{16}$. In the same way $S\gamma^{(0)}S^{-1} = \gamma^{(0)}e^{bJ} = \cosh b\,\gamma^{(0)} + \sinh b\,\gamma^{(0)}\gamma^{(4)}\gamma^{(0)} = \cosh b\,\gamma^{(0)} - \sinh b\,\gamma^{(4)}$ (here $\gamma^{(0)}\gamma^{(4)}\gamma^{(0)} = -\gamma^{(4)}(\gamma^{(0)})^2 = -\gamma^{(4)}$).

**Step 3: the coordinate gammas of the boosted frame.** The boosted frame is $e' = Le$, with the boost matrix $L$; its inverse is $E' = EL^{-1}$ (the inverse of a product is the product of the inverses in reverse order), and $L^{-1}$ is the boost with $-b$. So $\gamma'^\mu = \sum_a E'_a{}^\mu\gamma^{(a)} = \sum_b E_b{}^\mu\tilde\gamma^{(b)}$, where $\tilde\gamma^{(4)} = \cosh b\,\gamma^{(4)} - \sinh b\,\gamma^{(0)}$, $\tilde\gamma^{(0)} = \cosh b\,\gamma^{(0)} - \sinh b\,\gamma^{(4)}$ and $\tilde\gamma^{(a)} = \gamma^{(a)}$ otherwise. By Step 2, $\tilde\gamma^{(b)} = S\gamma^{(b)}S^{-1}$ for every $b$, and therefore $\gamma'^\mu = S\gamma^\mu S^{-1}$.

**Step 4: the connection of the boosted frame.** Chapter 6 proves in general (in its section on local spin covariance) that the canonical spinor connection of the turned frame is $S\Omega_\mu S^{-1} - (\partial_\mu S)S^{-1}$. Here is a shorter argument for the same result. It rests on two facts: the canonical spin connection of every frame makes that frame's coordinate gammas covariantly constant (a consequence of the vielbein postulate), and it is a combination of the $S^{ab}$, so its trace (the sum of its diagonal entries) is zero. Both are established in Chapter 6; we quote them here, and the direct computation of the record and of Notebook 08c confirms their consequence. We show that $\Omega'_\mu = S\Omega_\mu S^{-1} - (\partial_\mu S)S^{-1}$ has both properties, and that only one matrix has them. First, covariant constancy, line by line (with $\partial_\mu S^{-1} = -S^{-1}(\partial_\mu S)S^{-1}$, which follows from differentiating $SS^{-1} = I_{16}$):

$$
\begin{aligned}
\partial_\mu\gamma'^\nu &= (\partial_\mu S)\gamma^\nu S^{-1} + S(\partial_\mu\gamma^\nu)S^{-1} - S\gamma^\nu S^{-1}(\partial_\mu S)S^{-1}, \\
[\Omega'_\mu, \gamma'^\nu] &= S[\Omega_\mu, \gamma^\nu]S^{-1} - (\partial_\mu S)\gamma^\nu S^{-1} + S\gamma^\nu S^{-1}(\partial_\mu S)S^{-1}, \\
\partial_\mu\gamma'^\nu + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}\gamma'^\lambda + [\Omega'_\mu, \gamma'^\nu] &= S\Big(\partial_\mu\gamma^\nu + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}\gamma^\lambda + [\Omega_\mu, \gamma^\nu]\Big)S^{-1} = 0 .
\end{aligned}
$$

The first line is the product rule for $S\gamma^\nu S^{-1}$; the second inserts $\Omega'_\mu$ and $\gamma'^\nu$ into the commutator and multiplies out; the third adds the two lines and the Christoffel term ($\Gamma$ belongs to the metric, the same in both frames), sees the four terms with $\partial_\mu S$ cancel in pairs, and uses the covariant constancy of the diagonal frame. Second, the trace: $\mathrm{tr}(S\Omega_\mu S^{-1}) = \mathrm{tr}\,\Omega_\mu = 0$, and $(\partial_\mu S)S^{-1}$ is a multiple of $J$ (Step 5 below), whose trace is zero (the trace of a product of two different gammas is zero: $\mathrm{tr}(\gamma^{(4)}\gamma^{(0)}) = \mathrm{tr}(\gamma^{(0)}\gamma^{(4)}) = -\mathrm{tr}(\gamma^{(4)}\gamma^{(0)})$, by the cyclic rule of the trace and then anticommutation). Third, uniqueness: if two traceless matrices $\Omega'_1$, $\Omega'_2$ both make the $\gamma'^\nu$ covariantly constant, their difference commutes with every $\gamma'^\nu$; then $S^{-1}(\Omega'_1 - \Omega'_2)S$ commutes with every $\gamma^{(a)}$, so it is a multiple of $I_{16}$ (the gammas form an irreducible representation, Chapter 5; `Revision/algebra/reports/python-algebra.json`, check `pin_commutant_dimension_1`), and a traceless multiple of $I_{16}$ is zero. Hence the canonical connection of the boosted frame is $\Omega'_\mu = S\Omega_\mu S^{-1} - (\partial_\mu S)S^{-1}$.

**Step 5: the term.** Line by line:

$$
\begin{aligned}
\gamma'^\mu\Omega'_\mu &= S\gamma^\mu S^{-1}\big(S\Omega_\mu S^{-1} - (\partial_\mu S)S^{-1}\big) = S\big(\gamma^\mu\Omega_\mu - \gamma^\mu S^{-1}\partial_\mu S\big)S^{-1}, \\
S^{-1}\partial_\mu S &= -\tfrac{b'}{2}J \ \text{for}\ \mu = x_4, \quad 0 \ \text{otherwise}, \\
\gamma^{x_4}S^{-1}\partial_4 S &= \gamma^{(4)}\big(-\tfrac{b'}{2}\gamma^{(4)}\gamma^{(0)}\big) = -\tfrac{b'}{2}(\gamma^{(4)})^2\gamma^{(0)} = \tfrac{b'}{2}\gamma^{(0)}, \\
\gamma'^\mu\Omega'_\mu &= S\big(G - \tfrac{b'}{2}\gamma^{(0)}\big)S^{-1} = \Big(c_g - \frac{b'}{2}\Big)\,S\gamma^{(0)}S^{-1} + v_g\,S\gamma^{(4)}S^{-1} \\
&= \Big(c_g - \frac{b'}{2}\Big)\big(\cosh b\,\gamma^{(0)} - \sinh b\,\gamma^{(4)}\big) + v_g\big(\cosh b\,\gamma^{(4)} - \sinh b\,\gamma^{(0)}\big) .
\end{aligned}
$$

The first line inserts Steps 3 and 4 and cancels $S^{-1}S$; the second differentiates $S = e^{-(b/2)J}$ by the chain rule (only $b$ depends on the coordinates, and only on $x_4$; $S$ commutes with $J$); the third uses $\gamma^{x_4} = \gamma^{(4)}$ ($f_4 = 1$) and $(\gamma^{(4)})^2 = -I_{16}$; the fourth and fifth use $\gamma^\mu\Omega_\mu = G = c_g\gamma^{(0)} + v_g\gamma^{(4)}$ (Section 8.5) and Step 2. For $b = \beta x_4 + b_0$, $b' = \beta$, and this is the record's formula.

**The consequence.** For a rapidity whose rate is $b' = 2c_g = 3He^{a_4}b_4^{-1/2}$ at every time, the part with $c_g$ is identically zero, for every $H > 0$ and all functions $a_4$ and $b_4$, although the metric is the author's curved metric. On the history (with $H = 1$) such a rapidity is $b = 9(e^{x_4/3} - 1)$, because its derivative is $3e^{x_4/3} = 2c_g$. What is left is the part $v_g$:

$$
\gamma'^\mu\Omega'_\mu = v_g\big(\cosh b\,\gamma^{(4)} - \sinh b\,\gamma^{(0)}\big)
$$

(PROVED; `python-scope.json`, check `boosted_frame_removes_only_the_H_term`, both engines). No boost in the $(x_4, x_0)$ plane removes this part. Write the term as $c_0\gamma^{(0)} + c_4\gamma^{(4)}$, with $\kappa_b = c_g - b'/2$; then $c_0 = \kappa_b\cosh b - v_g\sinh b$ and $c_4 = -\kappa_b\sinh b + v_g\cosh b$. Line by line,

$$
\begin{aligned}
\cosh b\,c_4 + \sinh b\,c_0 &= -\kappa_b\cosh b\sinh b + v_g\cosh^2 b + \kappa_b\sinh b\cosh b - v_g\sinh^2 b \\
&= v_g\big(\cosh^2 b - \sinh^2 b\big) = v_g ,
\end{aligned}
$$

for every rapidity: the terms with $\kappa_b$ cancel, and $\cosh^2 b - \sinh^2 b = 1$ (Section 8.3). So $c_0 = c_4 = 0$ would need $v_g = 0$, that is $b_4'/b_4 = a_4'/2$ (`python-scope.json`, check `boosted_frame_gammaOmega_formula`). The connection itself is not zero in the frame with $b' = 2c_g$: $\Omega'_\mu \neq 0$ for every $\mu = x_0, \dots, x_7$ (check `boosted_frame_removes_only_the_H_term`). So the sentence "the field equation contains the gravitational term $c_g\gamma^{(0)}\Psi$" is true in the diagonal frame and false in this frame: the part $c_g\gamma^{(0)}$ is a statement about one frame, not about the field equation as such. The part $v_g$ survives every boost of this kind, but a change of the field variables removes it too (Section 8.30). In the boosted frame gravity enters the field equation through the boosted frame vectors $E'_a{}^\mu$ and through the part $v_g$.

### 8.10 What no frame removes: the curvature of the connection

**The curvature in two frames.** The curvature of the spinor connection equals the Riemann tensor contracted with two coordinate gammas, $F_{\mu\nu} = \frac14\sum_{\rho,\sigma}R_{\rho\sigma\mu\nu}\gamma^\rho\gamma^\sigma$ (Section 8.4). This identity holds in every frame (a standard theorem, quoted without proof here as in Chapter 6, so ASSUMED in general; the record proves it for this metric in the diagonal frame, and Notebook 08c checks it in the diagonal frame and in the frame boosted with $b' = 2c_g$ for $(\mu, \nu) = (x_5, x_0)$). Chapter 6 also derives the relation below directly from local spin covariance, without this identity. The Riemann tensor belongs to the metric and is the same in both frames, and $\gamma'^\rho = S\gamma^\rho S^{-1}$ (Section 8.9). Hence, line by line,

$$
F'_{\mu\nu} = \tfrac14\sum_{\rho,\sigma}R_{\rho\sigma\mu\nu}\,S\gamma^\rho S^{-1}S\gamma^\sigma S^{-1} = S\Big(\tfrac14\sum_{\rho,\sigma}R_{\rho\sigma\mu\nu}\gamma^\rho\gamma^\sigma\Big)S^{-1} = SF_{\mu\nu}S^{-1} .
$$

The first step inserts $\gamma'^\rho = S\gamma^\rho S^{-1}$ twice; the second cancels $S^{-1}S$ in the middle and takes $S$ and $S^{-1}$ out of the sum (the numbers $R_{\rho\sigma\mu\nu}$ commute with matrices); the third recognises $F_{\mu\nu}$.

**One component, computed by hand.** In the diagonal frame, $F_{x_5x_0} = \partial_5\Omega_{x_0} - \partial_0\Omega_{x_5} + [\Omega_{x_5}, \Omega_{x_0}]$. Line by line:

$$
\begin{aligned}
\partial_5\Omega_{x_0} &= 0, \qquad \partial_0\Omega_{x_5} = \tfrac12H\cot z\,W\big(h_4s_b\,\gamma^{(4)}\gamma^{(5)} + H\gamma^{(0)}\gamma^{(5)}\big), \\
[\gamma^{(4)}\gamma^{(5)}, \gamma^{(0)}\gamma^{(4)}] &= 2\gamma^{(0)}\gamma^{(5)}, \qquad [\gamma^{(0)}\gamma^{(5)}, \gamma^{(0)}\gamma^{(4)}] = 2\gamma^{(4)}\gamma^{(5)}, \\
[\Omega_{x_5}, \Omega_{x_0}] &= \tfrac12W\cdot\tfrac12h_4s_b\cot z\,\big(h_4s_b\cdot 2\gamma^{(0)}\gamma^{(5)} + H\cdot 2\gamma^{(4)}\gamma^{(5)}\big), \\
F_{x_5x_0} &= \tfrac12\cot z\,W\big(h_4^2s_b^2 - H^2\big)\,\gamma^{(0)}\gamma^{(5)} .
\end{aligned}
$$

The first line uses that nothing depends on $x_5$, and $\partial_0W = H\cot z\,W$ (Section 8.4; $h_4s_b$ does not depend on $x_0$). The second line computes two commutators by moving gammas: $\gamma^{(4)}\gamma^{(5)}\gamma^{(0)}\gamma^{(4)} = \gamma^{(4)}\gamma^{(4)}\gamma^{(5)}\gamma^{(0)} = -\gamma^{(5)}\gamma^{(0)} = \gamma^{(0)}\gamma^{(5)}$ (two sign changes to bring the last $\gamma^{(4)}$ forward, then $(\gamma^{(4)})^2 = -I_{16}$, then one anticommutation) and $\gamma^{(0)}\gamma^{(4)}\gamma^{(4)}\gamma^{(5)} = -\gamma^{(0)}\gamma^{(5)}$, whose difference is $2\gamma^{(0)}\gamma^{(5)}$; likewise $\gamma^{(0)}\gamma^{(5)}\gamma^{(0)}\gamma^{(4)} = -\gamma^{(5)}\gamma^{(4)} = \gamma^{(4)}\gamma^{(5)}$ and $\gamma^{(0)}\gamma^{(4)}\gamma^{(0)}\gamma^{(5)} = -\gamma^{(4)}\gamma^{(5)}$. The third line inserts $\Omega_{x_5}$ and $\Omega_{x_0}$ of Section 8.4 into the commutator and uses the second line. The fourth subtracts the first line from the third: the two terms with $\gamma^{(4)}\gamma^{(5)}$ are $-\frac12H\cot z\,Wh_4s_b$ and $+\frac12W\cot z\,h_4s_bH$, which cancel, and the terms with $\gamma^{(0)}\gamma^{(5)}$ collect to $\frac12\cot z\,W(h_4^2s_b^2 - H^2)$. Notebook 08c finds exactly this ($c_{45} = 0$ and $c_{05} = \frac12\cot z\,W(h_4^2e^{-2a_4}b_4 - H^2)$, with $s_b^2 = e^{-2a_4}b_4$).

**When it vanishes, and when not.** On the flat member $a_4 = 0$, $b_4 = H^2x_4^2$ we have $s_b = Hx_4$ and $h_4 = 1/x_4$, so $h_4s_b = H$ and $F_{x_5x_0} = 0$, as it must (all of the curvature vanishes there). On the history of the record ($A = H = 1$) $h_4 = -\frac13$ and $s_b^2 = e^{-2x_4/3}$, so $h_4^2s_b^2 - H^2 = \frac19e^{-2x_4/3} - 1$, which vanishes only at the single time $x_4 = -3\ln 3$; at $H = 1$, $z = \pi/4$, $x_4 = 0.5$ (where $\cot z = 1$ and $W = 2^{-1/12}$) the coefficient is $c_{05} = \frac12\cdot2^{-1/12}(\frac19e^{-1/3} - 1) = -0.434$, the value Notebook 08c prints. In the frame boosted with $b' = 2c_g$, $F'_{x_5x_0} = SF_{x_5x_0}S^{-1} = c_{05}\,(S\gamma^{(0)}S^{-1})(S\gamma^{(5)}S^{-1}) = c_{05}(\cosh b\,\gamma^{(0)}\gamma^{(5)} - \sinh b\,\gamma^{(4)}\gamma^{(5)})$ by Step 2 of Section 8.9, which is not zero either.

**Two frames, one curvature.** The square of $F_{x_5x_0}$ is the same in both frames: $(\gamma^{(0)}\gamma^{(5)})^2 = -(\gamma^{(0)})^2(\gamma^{(5)})^2 = I_{16}$, $(\gamma^{(4)}\gamma^{(5)})^2 = -(\gamma^{(4)})^2(\gamma^{(5)})^2 = -I_{16}$, and the two products anticommute, so $F'^2 = c_{05}^2(\cosh^2 b - \sinh^2 b)I_{16} = c_{05}^2I_{16} = F^2$. It must be so: $F'^2 = SF^2S^{-1}$, and $F^2$ is a multiple of $I_{16}$.

**The connection vanishes in no frame where the metric is curved.** If the connection $\Omega'_\mu$ vanished at all points of a region in some frame, its curvature would vanish there; but $F' = SFS^{-1}$ with an invertible $S$, and $F = \frac14R\gamma\gamma$ is zero only where the Riemann tensor is. On the history of the record the metric is curved at every point ($R^{x_1}{}_{x_1} = \frac53H^2$, Section 8.7). So on the history the spin connection vanishes in no frame (PROVED; `python-scope.json`, check `boosted_frame_curvature_nonzero`, both engines, which argues in general: the curvature of the connection is $\frac12R_{ab\mu\nu}S^{ab}$ in every frame). On the flat member, by contrast, all gravitational effects are removable: there the metric is flat 8-dimensional space in unusual coordinates, and in its Cartesian coordinates and frame the connection vanishes and the field equation is the flat 4+4 equation, as the test [1] requires.

**The frame-independent content of non-triviality.** Putting Sections 8.6 to 8.10 together: wherever the metric is curved (on the history of the record, everywhere) the canonical spin connection is nonzero in every frame, because its curvature is the curvature of spacetime; and the frame factors $e^{a_4}b_4^{-1/2}\tan z$, $e^{-a_4}$ and $e^{a_4}b_4^{-1/2}(\sin^2 z)^{-1/12}$, none of which is identically 1, multiply every derivative term of the field equation except the one along the time $x_4$ (the derivatives along $x_0, x_1, x_2, x_3, x_5, x_6, x_7$; the factor of $\partial_4$ is $1/f_4 = 1$). These two facts do not depend on any choice. The value $G$ of the term $\gamma^\mu\Omega_\mu$ does: its part $c_g\gamma^{(0)}$ depends on the frame, and all of it on the field variables (Section 8.30).

### 8.11 The connection in the energy-momentum tensor

The spin connection drops out of the Lagrangian (Section 8.8), but it does reach the energy-momentum tensor, the source of gravity (Chapter 9). For a field that depends only on the time, $\Phi = \Phi(x_4)$, the entries $K^{x_4}{}_{x_1} = \frac12\big(\bar\Phi\gamma^{x_4}D_{x_1}\Phi - (D_{x_1}\bar\Phi)\gamma^{x_4}\Phi\big)$ and $K^{x_4}{}_{x_5}$ (the same with $x_5$) have no derivative part ($\partial_1\Phi = \partial_5\Phi = 0$), and their connection parts are $\frac12\bar\Phi\{\gamma^{x_4}, \Omega_{x_1}\}\Phi$ and $\frac12\bar\Phi\{\gamma^{x_4}, \Omega_{x_5}\}\Phi$. Line by line, with $\gamma^{x_4} = \gamma^{(4)}$:

$$
\begin{aligned}
\gamma^{(4)}\gamma^{(1)}\gamma^{(4)} + \gamma^{(1)}\gamma^{(4)}\gamma^{(4)} &= -\gamma^{(1)}\gamma^{(4)}\gamma^{(4)} + \gamma^{(1)}\gamma^{(4)}\gamma^{(4)} = 0, \\
\gamma^{(4)}\gamma^{(4)}\gamma^{(5)} + \gamma^{(4)}\gamma^{(5)}\gamma^{(4)} &= \gamma^{(4)}\gamma^{(4)}\gamma^{(5)} - \gamma^{(4)}\gamma^{(4)}\gamma^{(5)} = 0, \\
\gamma^{(4)}\gamma^{(0)}\gamma^{(5)} + \gamma^{(0)}\gamma^{(5)}\gamma^{(4)} &= \gamma^{(4)}\gamma^{(0)}\gamma^{(5)} + \gamma^{(4)}\gamma^{(0)}\gamma^{(5)} = 2\gamma^{(4)}\gamma^{(0)}\gamma^{(5)}, \\
\tfrac12\{\gamma^{x_4}, \Omega_{x_1}\} &= \tfrac12\cdot\tfrac12a_4'e^{a_4}\cdot 0 = 0, \\
\tfrac12\{\gamma^{x_4}, \Omega_{x_5}\} &= \tfrac12\cdot\tfrac12W\big(h_4s_b\cdot 0 + H\cdot 2\gamma^{(4)}\gamma^{(0)}\gamma^{(5)}\big) = \tfrac12HW\,\gamma^{(4)}\gamma^{(0)}\gamma^{(5)} .
\end{aligned}
$$

The first line moves the first $\gamma^{(4)}$ past $\gamma^{(1)}$ (one sign): $\{\gamma^{(4)}, \gamma^{(1)}\gamma^{(4)}\} = 0$; the second moves $\gamma^{(5)}$ past $\gamma^{(4)}$ in the second product (one sign): $\{\gamma^{(4)}, \gamma^{(4)}\gamma^{(5)}\} = 0$; the third moves $\gamma^{(4)}$ in the second product to the front past two gammas (two signs); the fourth and fifth insert $\Omega_{x_1}$ and $\Omega_{x_5}$ of Section 8.4. So the connection part of $K^{x_4}{}_{x_1}$ vanishes (3-space does not depend on $x_0$, so $\Omega_{x_1}$ has no part with $H$), while that of $K^{x_4}{}_{x_5}$ is $\frac12H(\sin^2 z)^{1/12}\,\bar\Phi\gamma^{(4)}\gamma^{(0)}\gamma^{(5)}\Phi$ (the part with $a_4'$ and $b_4'$ cancels exactly). The bilinear matrix $C\gamma^{(4)}\gamma^{(0)}\gamma^{(5)}$ is not the zero matrix, so this entry is not zero in general (PROVED; `python-scope.json`, check `spin_connection_in_the_energy_momentum_tensor`, both engines). Chapter 9 uses the energy-momentum tensor with its connection parts.

### 8.12 Example: the term in two frames, computed from the definitions

Notebook 08c puts Sections 8.3 to 8.11 to work, exactly, with sympy, for symbolic functions $a_4(x_4)$, $b_4(x_4)$ and $b(x_4)$ and a symbolic $H$. It builds the scale factors and the metric and compares them with the record; computes all Christoffel symbols (21 independent nonzero ones) and the canonical spin connection of the diagonal frame and checks the vielbein postulate for all 512 components; shows that the connection vanishes only for $a_4' = 0$, $b_4' = 0$ and $H = 0$; computes $\gamma^\mu\Omega_\mu$ direction by direction and draws what cancels and what survives; computes the Ricci tensor, the flat member and the curvature on the history; builds the boosted frame and finds $\gamma'^\mu\Omega'_\mu$; computes the spinor curvature in both frames; and checks the connection part of the energy-momentum tensor. It needs no Rust and runs in a few minutes; the times measured on the build computer, which depend on how busy that computer is, are recorded in the notebook's provenance file `Revision/textbook/notebooks/08c_frame_dependence.PROVENANCE.md`. It ends with the line ALL 37 CHECKS PASSED (notebook 08c).

<!-- NOTEBOOK 08c -->

### 8.15 Line-by-line walk-through of Notebook 08c

The notebook has 14 code cells, In [1] to In [14]. This section explains every line of every one of them, in order: a line or a small group of lines is quoted exactly and then explained. A line that starts with `#` is a **comment**, which Python skips; it is there for the reader. In the quoted code a line `...)` stands for the remaining lines of a long figure caption; every caption is printed in full under its figure in Section 8.14, and a paragraph "What Figure 08c.k shows" after the code says what to look for. Because Notebook 08c is the first notebook of this chapter, its set-up cell and its two record helpers are explained here in full; the walk-throughs of Notebooks 08a, 08b and 08d refer back to this explanation.

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

`check_record` is the notebook's check for a result that the Revision record also states. `isinstance(check_names, str)` asks whether a single name (a string) was given; then `names` is the list with that one name, otherwise the given list. The check passes only if the notebook's own computation (`condition`) is true AND the record says the same: the first named check must hold every piece of text (typically a formula or a number that this notebook computed itself and turned into text), and the further names need only be recorded as passed. `" and ".join(names)` joins the names with the word "and". So every `PASS` line that this helper prints is followed by a line `reproduces <report>, check <name>`.

```python
gammas_record = json.loads(
    repository_file("Revision/algebra/gammas.json").read_text(encoding="utf-8"))
G = [sp.Matrix(rows) for rows in gammas_record["gamma"]]  # gamma^(x0) ... (x7)
ETA = gammas_record["eta"]  # [1, 1, 1, 1, -1, -1, -1, -1]
C = sp.Matrix(gammas_record["C"])  # C = gamma^(x0) gamma^(x1) gamma^(x2) gamma^(x3)
THEORY = "Revision/theory/reports/python-field-theory.json"  # the sympy record
WOLFRAM = "Revision/theory/reports/wolfram-field-theory.json"  # the Wolfram record
```

`gammas_record` holds the content of `Revision/algebra/gammas.json`. `G` is the list of the eight gammas as exact sympy matrices (`sp.Matrix(rows)` turns a list of 16 rows of 16 integers into a matrix), so `G[0]` is $\gamma^{(0)}$ and `G[4]` is $\gamma^{(4)}$. `ETA` is the list of the signs $\eta_{aa}$ and `C` the matrix $C$. `THEORY` and `WOLFRAM` are short names for the two field-theory reports.

```python
x = sp.symbols("x0:8", real=True)  # the coordinates; x[k] is xk
x0, x4 = x[0], x[4]  # the hidden direction and the time
H = sp.Symbol("H", positive=True)
a4 = sp.Function("a4")(x4)  # the first metric function: ANY function of x4
b4 = sp.Function("b4", positive=True)(x4)  # the second one: ANY positive function
a4p, b4p = sp.diff(a4, x4), sp.diff(b4, x4)  # a4' and b4'
z = 6 * H * x0  # every real value
```

`sp.symbols("x0:8", real=True)` makes the eight real symbols `x0`, ..., `x7` (the range `0:8` means 0 to 7), stored in the tuple `x`, so `x[k]` is $x_k$. `H` is a positive symbol. `sp.Function("a4")(x4)` is an unknown function $a_4$ of the time, about which nothing else is assumed: every result is therefore true for every history. `b4` is an unknown positive function of the time. `sp.diff(a4, x4)` is the derivative $a_4'$, which sympy prints as `Derivative(a4(x4), x4)`. `z` is $6Hx_0$; no range is assumed for it.

```python
class W(sp.Function):
    """The warp factor W(x0) = (sin(6 H x0)^2)^(1/12) > 0 of the extra times."""

    def fdiff(self, argindex=1):
        """dW/dx0 = H cot(6 H x0) W, for every real z = 6 H x0 with sin z != 0."""
        return H * sp.cot(6 * H * self.args[0]) * self

    def _eval_is_positive(self):
        return True  # the positive root
```

A **class** defines a new kind of object. `W` is a new sympy function, the warp factor $W(x_0) = (\sin^2 z)^{1/12}$, defined by two rules only. The method `fdiff` tells sympy its derivative: whenever sympy differentiates `W(x0)` with respect to $x_0$, it uses $dW/dx_0 = H\cot(6Hx_0)\,W$ (`self` is the expression `W(x0)` itself, and `self.args[0]` is its argument `x0`). The method `_eval_is_positive` tells sympy that $W$ is positive. Working with this short symbol instead of the explicit root keeps the expressions small, and sympy never has to decide the sign of $\sin z$.

```python
def is_zero(expr):
    """True when sympy shows that expr is exactly zero (two simplifications)."""
    expr = sp.sympify(expr)
    if expr == 0:
        return True
    simpler = sp.simplify(expr)
    return simpler == 0 or sp.simplify(sp.fu(simpler)) == 0
```

`is_zero` decides whether an expression is exactly zero. `sp.sympify` turns plain numbers into sympy numbers; an expression that is already the number 0 is zero at once; otherwise `sp.simplify` tries to simplify it, and if that does not give 0, the trigonometric simplifier `sp.fu` is applied and the result simplified once more. An answer True is a proof (sympy reached 0 by exact rules).

```python
explicit_W = sp.Abs(sp.sin(z)) ** sp.Rational(1, 6)  # (sin^2 z)^(1/12) = |sin z|^(1/6)
check(is_zero(sp.diff(explicit_W, x0) - H * sp.cot(z) * explicit_W),
      "the derivative of (sin^2 z)^(1/12) is H cot z (sin^2 z)^(1/12): the rule of W")
```

`explicit_W` is the warp factor written out, $|\sin z|^{1/6}$ (for real $z$ this is $(\sin^2 z)^{1/12}$). The check differentiates it with sympy's own rules and compares with the rule given to `W`: the difference simplifies to zero, so the short symbol is safe.

```python
s_b = sp.exp(-a4) * sp.sqrt(b4)  # the scale of the hidden block e^(-a4) b4^(1/2)
f = [s_b * sp.cot(z)] + [sp.exp(a4)] * 3 + [sp.Integer(1)] \
    + [s_b * W(x0)] * 3  # the scale factors f_0, ..., f_7
g = [ETA[a] * f[a] ** 2 for a in range(8)]  # the diagonal entries g_aa
```

`s_b` is $e^{-a_4}b_4^{1/2}$, the common factor of the hidden block. `f` is the list of the eight scale factors of Section 8.2: $f_0 = s_b\cot z$, then $e^{a_4}$ three times (the list `[sp.exp(a4)] * 3` repeats one entry three times), then 1, then $s_bW$ three times; the backslash at the end of the line continues the statement on the next line. `g` is the list of the diagonal entries $g_{aa} = \eta_{aa}f_a^2$ (a **list comprehension**: the expression in front of `for` is evaluated for every `a` from 0 to 7).

```python
sixth = (sp.sin(z) ** 2) ** sp.Rational(1, 6)  # (sin^2 z)^(1/6), sympy: |sin z|^(1/3)
authors_metric = [b4 * sp.exp(-2 * a4) * sp.cot(z) ** 2] + [sp.exp(2 * a4)] * 3 \
    + [-1] + [-b4 * sp.exp(-2 * a4) * sixth] * 3  # the corrected metric, typed in
# The record prints each entry as sympy writes it, e.g. "g_x4x4 = -1".
metric_texts = [f"g_x{a}x{a} = {sp.sstr(authors_metric[a])}" for a in range(8)]
say(metric_texts[0])
say(metric_texts[5])
```

`sixth` is $(\sin^2 z)^{1/6}$, which sympy writes as `Abs(sin(6*H*x0))**(1/3)`. `authors_metric` is the corrected metric typed in exactly as the Revision SPEC gives it. `metric_texts` turns its eight entries into texts like `g_x4x4 = -1` with `sp.sstr` (sympy's plain-text form); the record prints its entries in the same form. The two `say` lines print the entries of $x_0$ and $x_5$:

```text
g_x0x0 = b4(x4)*exp(-2*a4(x4))*cot(6*H*x0)**2
g_x5x5 = -b4(x4)*exp(-2*a4(x4))*Abs(sin(6*H*x0))**(1/3)
```

```python
check_record(all(is_zero(g[a].subs(W(x0), explicit_W) - authors_metric[a])
                 for a in range(8)),
             "eta_aa f_a^2 is the corrected metric (all 8 diagonal entries)",
             THEORY, "metric_from_vielbein_equals_SPEC", *metric_texts)
```

For each of the eight entries the check replaces `W(x0)` by the explicit root (`.subs(old, new)` substitutes) and asks whether $\eta_{aa}f_a^2$ minus the typed-in entry is zero. The record's check `metric_from_vielbein_equals_SPEC` must contain all eight texts (`*metric_texts` hands the list over as eight separate pieces).

```python
volume = sp.prod(f)  # f_0 f_1 ... f_7: it has the sign of cot z
check_record(is_zero(volume - sp.exp(-a4) * b4**2 * sp.cot(z) * W(x0) ** 3)
             and is_zero(volume**2 - sp.prod(g))
             and is_zero(sp.diff(volume, x4) - (2 * b4p / b4 - a4p) * volume),
             "f0 ... f7 = e^(-a4) b4^2 cot z W^3, so sqrt|g| = e^(-a4) b4^2 |cot z| "
             "(sin^2 z)^(1/4), d4 sqrt|g| = (2 b4'/b4 - a4') sqrt|g|",
             THEORY, "sqrt_det_g", "e^-a4 b4^2 |cot z| (sin^2 z)^(1/4)",
             "d_x4 sqrt|g| = (2 b4'/b4 - a4') sqrt|g|")
```

`sp.prod(f)` multiplies the eight scale factors; the product has the sign of $\cot z$. The check proves three things: the product equals $e^{-a_4}b_4^2\cot z\,W^3$ (Section 8.2), its square equals the product of the eight $g_{aa}$ (so its size is $\sqrt{|g|}$), and its derivative with respect to $x_4$ is $(2b_4'/b_4 - a_4')$ times itself. Output of the cell:

```text
PASS the derivative of (sin^2 z)^(1/12) is H cot z (sin^2 z)^(1/12): the rule of W
g_x0x0 = b4(x4)*exp(-2*a4(x4))*cot(6*H*x0)**2
g_x5x5 = -b4(x4)*exp(-2*a4(x4))*Abs(sin(6*H*x0))**(1/3)
PASS eta_aa f_a^2 is the corrected metric (all 8 diagonal entries)
     reproduces Revision/theory/reports/python-field-theory.json, check
    metric_from_vielbein_equals_SPEC
PASS f0 ... f7 = e^(-a4) b4^2 cot z W^3, so sqrt|g| = e^(-a4) b4^2 |cot z| (sin^2
    z)^(1/4), d4 sqrt|g| = (2 b4'/b4 - a4') sqrt|g|
     reproduces Revision/theory/reports/python-field-theory.json, check sqrt_det_g
```

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

`Gam` is a list of 8 lists of 8 lists of 8 zeros, so that `Gam[lam][mu][nu]` holds $\Gamma^\lambda{}_{\mu\nu}$ (the `_` is a loop variable whose value is not used). The three nested loops visit all $8^3 = 512$ index triples. For a diagonal metric the bracket of the formula of Section 8.4 has at most three nonzero terms: $\partial_\mu g_{\lambda\nu}$ needs $\lambda = \nu$, $\partial_\nu g_{\lambda\mu}$ needs $\lambda = \mu$, and $\partial_\lambda g_{\mu\nu}$ needs $\mu = \nu$; the three `if` statements add exactly these (`+=` adds to a variable, `-=` subtracts). When the bracket is not zero, it is divided by $2g_{\lambda\lambda}$ and simplified.

```python
independent = sum(1 for lam in range(8) for mu in range(8) for nu in range(mu, 8)
                  if Gam[lam][mu][nu] != 0)
report("independent nonzero Christoffel symbols", independent)
for lam, mu, nu in ((0, 0, 0), (0, 0, 4), (0, 5, 5), (5, 0, 5), (1, 1, 4), (5, 4, 5)):
    say(f"Gamma^x{lam}_x{mu} x{nu} = {Gam[lam][mu][nu]}")
```

`independent` counts the nonzero symbols with $\mu \le \nu$ (the inner range starts at `mu`), because the symbols are symmetric in the two lower indices. `report` prints the count, and the loop prints six of the symbols, one from each kind of row of the table in Section 8.4 that the text derives.

```python
check_record(independent == 21, "21 independent nonzero Christoffel symbols",
             THEORY, "christoffel_symmetric_metric_compatible",
             f"{independent} independent nonzero symbols")
check_record(independent == 21, "the same count in the independent Wolfram verifier",
             WOLFRAM, "christoffel_count",
             f"the Levi-Civita connection has {independent} independent nonzero "
             "symbols")
```

The count must be 21, and both verifiers of the record must state the same number in the given words. Output:

```text
RESULT independent nonzero Christoffel symbols = 21
Gamma^x0_x0 x0 = -12*H/sin(12*H*x0)
Gamma^x0_x0 x4 = -Derivative(a4(x4), x4) + Derivative(b4(x4), x4)/(2*b4(x4))
Gamma^x0_x5 x5 = H*W(x0)**2*tan(6*H*x0)
Gamma^x5_x0 x5 = H*cot(6*H*x0)
Gamma^x1_x1 x4 = Derivative(a4(x4), x4)
Gamma^x5_x4 x5 = -Derivative(a4(x4), x4) + Derivative(b4(x4), x4)/(2*b4(x4))
PASS 21 independent nonzero Christoffel symbols
     reproduces Revision/theory/reports/python-field-theory.json, check
    christoffel_symmetric_metric_compatible
PASS the same count in the independent Wolfram verifier
     reproduces Revision/theory/reports/wolfram-field-theory.json, check
    christoffel_count
```

The six printed symbols are the table's $\Gamma^{x_0}{}_{x_0x_0} = -12H/\sin(12Hx_0)$, $\Gamma^{x_0}{}_{x_0x_4} = h_4$ (sympy writes $h_4$ as $-a_4' + b_4'/(2b_4)$), $\Gamma^{x_0}{}_{x_5x_5} = HW^2\tan z$, $\Gamma^{x_5}{}_{x_0x_5} = H\cot z$, $\Gamma^{x_1}{}_{x_1x_4} = a_4'$ and $\Gamma^{x_5}{}_{x_4x_5} = h_4$.

**In [4], the canonical spin connection of the diagonal frame.**

```python
S_AB = [[(G[a] * G[c] - G[c] * G[a]) / 4 for c in range(8)] for a in range(8)]
```

`S_AB[a][c]` is the generator $S^{ac} = \frac14[\gamma^{(a)}, \gamma^{(c)}]$, for all 64 pairs (it is the zero matrix for $a = c$).

```python
def boost(b):
    """The boost by the rapidity b in the frame plane (x4, x0), and its inverse."""
    L, L_inverse = sp.eye(8), sp.eye(8)
    L[4, 4] = L[0, 0] = L_inverse[4, 4] = L_inverse[0, 0] = sp.cosh(b)
    L[4, 0] = L[0, 4] = sp.sinh(b)
    L_inverse[4, 0] = L_inverse[0, 4] = -sp.sinh(b)
    return L, L_inverse
```

`boost(b)` returns the boost matrix $L$ of Section 8.3 and its inverse as $8 \times 8$ sympy matrices. `sp.eye(8)` is the unit matrix; the entries $(4,4)$ and $(0,0)$ become $\cosh b$, the entries $(4,0)$ and $(0,4)$ become $\sinh b$ in $L$ and $-\sinh b$ in the inverse (the boost with $-b$). A chained assignment like `L[4, 4] = L[0, 0] = ... = sp.cosh(b)` gives all the named entries the same value.

```python
def frame(b):
    """Vielbein e[a, mu], inverse E[mu, a], connection omega[mu, a, c] (mixed),
    Omega_mu and gamma^mu of the diagonal frame boosted by the rapidity b."""
    L, L_inverse = boost(b)
    e = L * sp.diag(*f)
    E = sp.diag(*[1 / value for value in f]) * L_inverse
```

`frame(b)` computes everything for the frame boosted by the rapidity `b`. `sp.diag(*f)` is the diagonal matrix with the eight scale factors, so `e = L * sp.diag(*f)` is the boosted vielbein $e'^a{}_\mu$ (row $a$, column $\mu$); for `b` equal to 0, $L$ is the unit matrix and `e` is the diagonal frame. `E` is its inverse $E_a{}^\mu$, stored with the coordinate index first (`E[mu, a]`).

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

The loops compute the mixed connection $\omega_\mu{}^a{}_c = \sum_\nu e^a{}_\nu(\partial_\mu E_c{}^\nu + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}E_c{}^\lambda)$ of Section 8.4, component by component, and store it in the dictionary `omega` under the key `(mu, a, c)`. `continue` skips a value of $\nu$ for which $e^a{}_\nu$ is zero (the term would be zero anyway), and the inner test skips products with a zero factor; both only save time.

```python
    Omega = []
    for mu in range(8):
        matrix = sp.zeros(16, 16)
        for a in range(8):
            for c in range(a + 1, 8):  # (1/2) sum over all a, c = sum over a < c
                matrix += ETA[a] * omega[mu, a, c] * S_AB[a][c]
        Omega.append(matrix)
```

For each direction $\mu$ the spinor connection $\Omega_\mu = \sum_{a<c}\omega_{\mu ac}S^{ac}$ is built as a $16 \times 16$ matrix (`sp.zeros(16, 16)` is the zero matrix): the lowered component is $\omega_{\mu ac} = \eta_{aa}\omega_\mu{}^a{}_c$, hence the factor `ETA[a]`. The comment recalls why the sum over $a < c$ equals half the sum over all pairs (Section 8.4).

```python
    gamma_up = [sum((E[mu, a] * G[a] for a in range(8)), sp.zeros(16, 16))
                for mu in range(8)]
    return {"e": e, "E": E, "omega": omega, "Omega": Omega, "gamma": gamma_up}
```

`gamma_up` is the list of the coordinate gammas $\gamma^\mu = \sum_aE_a{}^\mu\gamma^{(a)}$; `sum(..., sp.zeros(16, 16))` adds matrices, starting from the zero matrix. The function returns everything in a dictionary.

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

`postulate_failures` evaluates the vielbein postulate $\partial_\mu e^a{}_\nu - \sum_\lambda\Gamma^\lambda{}_{\mu\nu}e^a{}_\lambda + \sum_c\omega_\mu{}^a{}_ce^c{}_\nu$ for all 512 triples $(a, \mu, \nu)$ and counts the components that `is_zero` does not show to be zero (`0 if ... else 1` is a conditional expression).

```python
def antisymmetric(fr):
    """omega_mu,ac = eta_aa omega_mu^a_c is antisymmetric in a, c for every mu."""
    return all(is_zero(ETA[a] * fr["omega"][mu, a, c] + ETA[c] * fr["omega"][mu, c, a])
               for mu in range(8) for a in range(8) for c in range(8))
```

`antisymmetric` checks $\omega_{\mu ac} + \omega_{\mu ca} = 0$ for all $8^3$ triples, with $\omega_{\mu ac} = \eta_{aa}\omega_\mu{}^a{}_c$.

```python
diagonal = frame(sp.Integer(0))
check_record(postulate_failures(diagonal) == 0 and antisymmetric(diagonal),
             "diagonal frame: vielbein postulate (512 components), omega antisymmetric",
             THEORY, ["vielbein_postulate", "spin_connection_antisymmetric"],
             "(512 components)")
```

`frame(sp.Integer(0))` is the diagonal frame (the rapidity is the exact number 0). The check requires zero failures of the postulate and the antisymmetry, and both checks of the sympy record (`vielbein_postulate` must mention the 512 components).

```python
nonzero = [(mu, a, c) for mu in range(8) for a in range(8) for c in range(a + 1, 8)
           if not is_zero(diagonal["omega"][mu, a, c])]
omega_diagonal = diagonal["omega"]
for mu, a, c in nonzero:
    say(f"omega_x{mu},(x{a})(x{c}) = "
        f"{sp.simplify(ETA[a] * omega_diagonal[mu, a, c])}")
```

`nonzero` lists the triples $(\mu, a, c)$ with $a < c$ whose component is not zero; `omega_diagonal` is a short name for the connection of the diagonal frame. The loop prints each nonzero lowered component $\omega_{\mu ac}$.

```python
check_record(len(nonzero) == 10, "10 independent nonzero components omega_mu,ab (a < b)",
             WOLFRAM, "omega_components",
             f"exactly {len(nonzero)} independent nonzero omega_mu,ab "
             "(a < b in the order x0..x7)")
```

There must be exactly 10, as the Wolfram verifier states. Output:

```text
PASS diagonal frame: vielbein postulate (512 components), omega antisymmetric
     reproduces Revision/theory/reports/python-field-theory.json, checks
    vielbein_postulate and spin_connection_antisymmetric
omega_x0,(x0)(x4) = (-2*b4(x4)*Derivative(a4(x4), x4) + Derivative(b4(x4),
    x4))*exp(-a4(x4))*cot(6*H*x0)/(2*sqrt(b4(x4)))
omega_x1,(x1)(x4) = exp(a4(x4))*Derivative(a4(x4), x4)
omega_x2,(x2)(x4) = exp(a4(x4))*Derivative(a4(x4), x4)
omega_x3,(x3)(x4) = exp(a4(x4))*Derivative(a4(x4), x4)
omega_x5,(x0)(x5) = H*W(x0)
omega_x5,(x4)(x5) = (-2*b4(x4)*Derivative(a4(x4), x4) + Derivative(b4(x4),
    x4))*W(x0)*exp(-a4(x4))/(2*sqrt(b4(x4)))
omega_x6,(x0)(x6) = H*W(x0)
omega_x6,(x4)(x6) = (-2*b4(x4)*Derivative(a4(x4), x4) + Derivative(b4(x4),
    x4))*W(x0)*exp(-a4(x4))/(2*sqrt(b4(x4)))
omega_x7,(x0)(x7) = H*W(x0)
omega_x7,(x4)(x7) = (-2*b4(x4)*Derivative(a4(x4), x4) + Derivative(b4(x4),
    x4))*W(x0)*exp(-a4(x4))/(2*sqrt(b4(x4)))
PASS 10 independent nonzero components omega_mu,ab (a < b)
     reproduces Revision/theory/reports/wolfram-field-theory.json, check omega_components
```

These are the ten components of Section 8.4: $\omega_{x_0\,(0)(4)} = h_4s_b\cot z$ (sympy writes $h_4s_b$ as $(-2b_4a_4' + b_4')e^{-a_4}/(2\sqrt{b_4})$), the three $\omega_{x_i\,(i)(4)} = a_4'e^{a_4}$, and for each extra time $\omega_{x_t\,(0)(t)} = HW$ and $\omega_{x_t\,(4)(t)} = h_4s_bW$.

**In [5], non-triviality: the connection vanishes only in the formal limit.**

```python
A1 = sp.Symbol("A1", real=True)  # a letter that stands for a4'
h4 = sp.Symbol("h4", real=True)  # a letter for h4 = b4'/(2 b4) - a4'
allowed = [sign * factor for sign in (1, -1)
           for factor in (sp.exp(a4), s_b * sp.cot(z), s_b * W(x0), W(x0))]
kinds = []  # for each component: "A1", "h4" or "H" (that rate times a factor)
```

`A1` and `h4` are plain real symbols that stand for $a_4'$ and $h_4$. `allowed` is the list of the eight possible factors $\pm e^{a_4}$, $\pm s_b\cot z$, $\pm s_bW$, $\pm W$ of Section 8.6 (the double `for` runs over the two signs and the four factors). `kinds` will record, for each nonzero component, which of the three rates it carries.

```python
for mu, a, c in nonzero:
    value = sp.simplify(ETA[a] * omega_diagonal[mu, a, c])
    value = value.subs(b4p, 2 * (h4 + a4p) * b4).subs(a4p, A1)
    found = [str(coupling) for coupling in (A1, h4, H) for factor in allowed
             if is_zero(value - coupling * factor)]  # which shape fits
    kinds.append(found[0] if len(found) == 1 else "no shape")
```

For each nonzero component the cell takes the lowered value, replaces $b_4'$ by $2(h_4 + a_4')b_4$ (which is the definition of $h_4$ solved for $b_4'$) and then $a_4'$ by the letter `A1`. Then it tries all 3 times 8 products rate times factor and collects, in `found`, the rates for which the difference is zero. Exactly one fit is expected; it is appended to `kinds` (otherwise the text "no shape", which would make the check below fail).

```python
n_A1, n_h4, n_H = kinds.count("A1"), kinds.count("h4"), kinds.count("H")
report("components of the form a4' x factor, h4 x factor and H x factor",
       f"{n_A1}, {n_h4}, {n_H}")
S_rows = np.array([[float(v) for v in S_AB[a][c]] for a in range(8)
                   for c in range(a + 1, 8)])  # 28 rows of 256 numbers
rank_S = int(np.linalg.matrix_rank(S_rows))
report("rank of the 28 matrices S^ab written as rows of 256 numbers", rank_S)
```

`kinds.count(...)` counts each kind, and `report` prints the three numbers. `S_rows` is a numpy array with one row of 256 floating-point numbers for each of the 28 generators $S^{ac}$ with $a < c$ (iterating over a sympy matrix gives its 256 entries row by row), and `np.linalg.matrix_rank` computes its rank, the number of independent rows.

```python
# a4' != 0 makes the three "A1" components nonzero, h4 != 0 the four "h4" ones and
# H != 0 the three "H" ones; with independent S^ab, Omega vanishes for every mu only
# when a4' = 0, h4 = 0 (so b4' = 0) and H = 0.
shapes_ok = n_A1 == 3 and n_h4 == 4 and n_H == 3 and rank_S == 28
check_record(shapes_ok, "Omega_mu = 0 for every mu iff a4' = 0, b4' = 0 and H = 0 "
             "(formal limit)", THEORY, "nontriviality_Omega_zero_iff_flat",
             "the S^ab are linearly independent",
             "every Omega_mu vanishes iff a4' = 0, a4' - b4'/(2 b4) = 0 (i.e. b4' = 0) "
             "AND H = 0")
check_record(shapes_ok, "the same in the independent Wolfram verifier", WOLFRAM,
             "Omega_vanishes_iff_a4prime_b4prime_and_H_vanish",
             "so all x4-parts vanish iff a4 and b4 are both constant, and for H > 0 "
             "the spin connection never vanishes")
```

The comment states the argument of Section 8.6. `shapes_ok` is true when the counts are 3, 4 and 3 and the rank is 28; then $\Omega_\mu = 0$ for every $\mu$ only if $a_4' = 0$, $h_4 = 0$ (so $b_4' = 0$) and $H = 0$. Both verifiers of the record state the same conclusion. Output:

```text
RESULT components of the form a4' x factor, h4 x factor and H x factor = 3, 4, 3
RESULT rank of the 28 matrices S^ab written as rows of 256 numbers = 28
PASS Omega_mu = 0 for every mu iff a4' = 0, b4' = 0 and H = 0 (formal limit)
     reproduces Revision/theory/reports/python-field-theory.json, check
    nontriviality_Omega_zero_iff_flat
PASS the same in the independent Wolfram verifier
     reproduces Revision/theory/reports/wolfram-field-theory.json, check
    Omega_vanishes_iff_a4prime_b4prime_and_H_vanish
```

**In [6], what cancels and what survives.**

```python
per_direction = [(diagonal["gamma"][mu] * diagonal["Omega"][mu]).applyfunc(sp.simplify)
                 for mu in range(8)]
coefficient_4 = [sp.simplify(-(G[4] * M).trace() / 16) for M in per_direction]
coefficient_0 = [sp.simplify((G[0] * M).trace() / 16) for M in per_direction]
```

`per_direction` is the list of the eight matrices $\gamma^{x_\mu}\Omega_{x_\mu}$ (no sum), each entry simplified (`applyfunc` applies a function to every entry). `coefficient_4` and `coefficient_0` are their coefficients of $\gamma^{(4)}$ and $\gamma^{(0)}$, found with traces: for $M = c_0\gamma^{(0)} + c_4\gamma^{(4)}$, $\mathrm{tr}(\gamma^{(0)}M) = 16c_0$ and $\mathrm{tr}(\gamma^{(4)}M) = -16c_4$, because $(\gamma^{(0)})^2 = I_{16}$, $(\gamma^{(4)})^2 = -I_{16}$, $\mathrm{tr}\,I_{16} = 16$, and the trace of a product of two different gammas is zero.

```python
nothing_else = all(
    all(is_zero(entry) for entry in
        per_direction[mu] - coefficient_4[mu] * G[4] - coefficient_0[mu] * G[0])
    for mu in range(8))
for mu in range(8):
    say(f"gamma^x{mu} Omega_x{mu} = ({coefficient_4[mu]}) gamma^(x4) "
        f"+ ({coefficient_0[mu]}) gamma^(x0)")
check(nothing_else, "each gamma^mu Omega_mu (no sum) is a combination of gamma^(x4) "
      "and gamma^(x0)")
```

`nothing_else` checks that each matrix minus its two parts is the zero matrix, so nothing else is left; the loop prints the two coefficients of each direction, and the check records the result.

```python
rate_h4 = b4p / (2 * b4) - a4p  # h4, the rate of the hidden block
B1 = sp.Symbol("B1", real=True)  # the record's letter for b4'/b4


def in_record_notation(expr):
    return sp.simplify(expr.subs(b4p, B1 * b4).subs(a4p, A1))


hidden_sum = in_record_notation(coefficient_4[0] + sum(coefficient_4[5:8]))  # 2 h4
space_sum = in_record_notation(sum(coefficient_4[1:4]))  # 3*A1/2
extra_sum_0 = sp.simplify(sum(coefficient_0))  # 3 H e^a4 b4^(-1/2) / 2
say(f"sums: hidden block (x0, x5, x6, x7) {hidden_sum}, 3-space {space_sum}, "
    f"gamma^(x0) part {extra_sum_0}")
```

`rate_h4` is $h_4$ written with $a_4'$ and $b_4'$. `in_record_notation` rewrites an expression with the record's letters `B1` for $b_4'/b_4$ and `A1` for $a_4'$. The three sums are the $\gamma^{(4)}$ coefficients of the hidden block ($x_0$ and the three extra times, positions 0 and 5 to 7; `coefficient_4[5:8]` is the part of the list from position 5 up to, not including, 8), of 3-space, and the total $\gamma^{(0)}$ coefficient; they are printed.

```python
expected_4 = [rate_h4 / 2] + [a4p / 2] * 3 + [0] + [rate_h4 / 2] * 3
expected_0 = [0] * 5 + [H * sp.exp(a4) / (2 * sp.sqrt(b4))] * 3
check_record(all(is_zero(coefficient_4[mu] - expected_4[mu])
                 and is_zero(coefficient_0[mu] - expected_0[mu]) for mu in range(8)),
             "per direction: h4/2, a4'/2 (x3), 0, and h4/2 with H e^a4 b4^(-1/2)/2 "
             "(x3)", THEORY, "per_direction_terms",
             "gamma^(x0) Omega_(x0) = (h4/2) gamma^(x4)",
             "gamma^(xi) Omega_(xi) = (a4'/2) gamma^(x4) (i = 1,2,3)",
             "gamma^(xt) Omega_(xt) = (h4/2) gamma^(x4) + (H/2) e^a4 b4^(-1/2) "
             "gamma^(x0) (t = 5,6,7)", "gamma^(x4) Omega_(x4) = 0")
```

`expected_4` and `expected_0` are the values of Section 8.5 direction by direction: $\frac12h_4$, $\frac12a_4'$ three times, 0, $\frac12h_4$ three times; and $0$ five times, then $\frac12He^{a_4}b_4^{-1/2}$ three times. The record's check `per_direction_terms` must state the four formulas.

```python
total = sum(per_direction, sp.zeros(16, 16))
c_g = sp.Rational(3, 2) * H * sp.exp(a4) / sp.sqrt(b4)  # (3/2) H e^a4 b4^(-1/2)
v_g = b4p / b4 - a4p / 2  # b4'/b4 - a4'/2
G_term = c_g * G[0] + v_g * G[4]  # the gravitational term of the diagonal frame
check_record(all(is_zero(entry) for entry in total - G_term),
             "gamma^mu Omega_mu = c_g gamma^(x0) + v_g gamma^(x4) in the diagonal "
             "frame", THEORY, "gamma_mu_Omega_mu_equals_hidden_block_terms",
             "gamma^mu Omega_mu = (3/2) H e^a4 b4^(-1/2) gamma^(x0) + (b4'/b4 - "
             "a4'/2) gamma^(x4) exactly")
```

`total` is the sum of the eight matrices, $\gamma^\mu\Omega_\mu$. `c_g` and `v_g` are the two coefficients of Section 8.5, and `G_term` is $G = c_g\gamma^{(0)} + v_g\gamma^{(4)}$. The check proves that every entry of `total - G_term` is zero, and that the record states the formula.

```python
parameters = json.loads(repository_file(
    "Revision/kohn_sham/results/parameters.json").read_text(encoding="utf-8"))
A_history = sp.nsimplify(parameters["physics"]["historyA"])  # a4 = A H x4
beta_4 = sp.nsimplify(parameters["physics"]["historyBeta"])  # b4 = e^(beta_4 A H x4)
b4_zero = sp.nsimplify(parameters["physics"]["historyB4AtZero"])  # b4(0)
history = {a4: A_history * H * x4, b4: b4_zero * sp.exp(beta_4 * A_history * H * x4)}
square_history = sp.simplify((c_g**2 - v_g**2).subs(history).doit())
say(f"c_g^2 - v_g^2 on the history: {square_history}")
```

The cell reads the history of the Kohn-Sham record: `sp.nsimplify` turns the stored floating-point numbers into exact fractions (1.333333333333333 becomes 4/3). `history` is a dictionary that replaces $a_4$ by $AHx_4$ and $b_4$ by $b_4(0)e^{\beta_4AHx_4}$ (it is used with `.subs(history)`; `.doit()` then carries out the derivatives of the inserted functions). `square_history` is $c_g^2 - v_g^2$ on the history, printed below.

```python
ranks = [(G[0] + sign * G[4]).rank() for sign in (1, -1)]  # c_g = +-v_g: G ~ these
check_record(all(is_zero(entry) for entry in G_term * G_term
                 - (c_g**2 - v_g**2) * sp.eye(16))
             and is_zero(square_history - H**2 * (sp.Rational(9, 4)
                                                  * sp.exp(2 * H * x4 / 3)
                                                  - sp.Rational(25, 36)))
             and ranks == [8, 8],
             "G G = (c_g^2 - v_g^2) 1, H^2 ((9/4) e^(2 H x4/3) - 25/36) on the "
             "history; rank 8 where c_g = +-v_g", THEORY, "gravity_term_square",
             "M M = (cg^2 - vg^2) I16 exactly",
             "M M = H^2 ((9/4) e^(2 H x4/3) - 25/36) I16 > 0", "(ranks [8, 8])")
```

`ranks` holds the ranks of $\gamma^{(0)} + \gamma^{(4)}$ and $\gamma^{(0)} - \gamma^{(4)}$, the shape of $G$ at a time where $c_g = \pm v_g$. The check proves $GG = (c_g^2 - v_g^2)I_{16}$ entry by entry, the value $H^2(\frac94e^{2Hx_4/3} - \frac{25}{36})$ on the history, and the ranks 8 and 8 (the record's check `gravity_term_square` calls the matrix $M$).

```python
sign_cot = sp.Symbol("sigma", real=True)  # the sign of cot z: sqrt|g| = sigma f0...f7
sqrt_g = sign_cot * volume
divergence = sum((sp.diff(sqrt_g * diagonal["gamma"][mu], x[mu]) for mu in range(8)),
                 sp.zeros(16, 16)) / (2 * sqrt_g)
check_record(all(is_zero(entry) for entry in divergence - G_term),
             "(1/(2 sqrt|g|)) d_mu(sqrt|g| gamma^mu) = c_g gamma^(x0) + v_g "
             "gamma^(x4) (divergence form)", THEORY, "divergence_of_sqrtg_gamma",
             "(1/2)(1/sqrt|g|) d_mu(sqrt|g| gamma^mu) = (3/2) H e^a4 b4^(-1/2) "
             "gamma^(x0) + (b4'/b4 - a4'/2) gamma^(x4) = gamma^mu Omega_mu")
```

`sign_cot` is a symbol $\sigma$ for the sign of $\cot z$, so that `sqrt_g` $= \sigma f_0\cdots f_7$ is the positive volume factor. `divergence` is $\frac{1}{2\sqrt{|g|}}\sum_\mu\partial_\mu(\sqrt{|g|}\gamma^\mu)$, computed for all eight directions; the check proves that it equals $G$ (the symbol $\sigma$ cancels, as in Section 8.5).

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

The last check proves $\gamma^\mu\Omega_\mu + \Omega_\mu\gamma^\mu = 0$ for each $\mu$ separately (Section 8.8): the connection drops out of the symmetrised Lagrangian.

```python
names = [f"$x_{mu}$" for mu in range(8)] + ["sum"]
a4_parts = [float(sp.simplify(c4.subs(b4p, 0) / a4p)) for c4 in coefficient_4]
b4_parts = [float(sp.simplify(c4.subs(a4p, 0) / (b4p / b4))) for c4 in coefficient_4]
values_0 = [float(sp.simplify(c0 / (H * sp.exp(a4) / sp.sqrt(b4))))
            for c0 in coefficient_0]  # in units of H e^a4 b4^(-1/2)
for values in (a4_parts, b4_parts, values_0):
    values.append(sum(values))
positions = np.arange(9)
colours = ["tab:green"] + ["tab:blue"] * 3 + ["gray"] + ["tab:red"] * 3 + ["black"]
```

Now the figure. `names` are the tick labels $x_0, \dots, x_7$ and "sum". `a4_parts` is, for each direction, the part of the $\gamma^{(4)}$ coefficient that is proportional to $a_4'$, in units of $a_4'$: setting $b_4' = 0$ leaves it, and dividing by $a_4'$ gives a number, which `float` turns into a floating-point number. `b4_parts` is the part proportional to $b_4'/b_4$ in units of $b_4'/b_4$, and `values_0` the $\gamma^{(0)}$ coefficients in units of $He^{a_4}b_4^{-1/2}$. The loop appends to each list its sum. `positions` are the nine bar positions 0 to 8, and `colours` gives the hidden direction green, 3-space blue, the time gray, the extra times red and the sum black.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
left.bar(positions - 0.2, a4_parts, width=0.38, color="tab:purple",
         label="part with $a_4'$ (units of $a_4'$)")
left.bar(positions + 0.2, b4_parts, width=0.38, color="tab:orange",
         label="part with $b_4'/b_4$ (units of $b_4'/b_4$)")
left.set_title("coefficient of $\\gamma^{(4)}$")
left.set_ylabel("coefficient")
left.legend(fontsize=8, loc="lower left")
right.bar(positions, values_0, color=colours)
right.set_title("coefficient of $\\gamma^{(0)}$, units of $He^{a_4}b_4^{-1/2}$")
for panel in (left, right):
    panel.axhline(0.0, color="black", linewidth=0.8)
    panel.set_xticks(positions)
    panel.set_xticklabels(names)
    panel.set_xlabel("direction $\\mu$ of $\\gamma^{\\mu}\\Omega_{\\mu}$")
```

`plt.subplots(1, 2, figsize=(10.0, 4.0))` makes a figure with two panels side by side, 10 by 4 inches. The left panel shows two bars per direction, shifted by $\mp0.2$, purple for the $a_4'$ part and orange for the $b_4'/b_4$ part; the right panel shows the $\gamma^{(0)}$ coefficients. The loop draws a black zero line in both panels and puts the names under the bars.

```python
save_figure(fig, "cancel_and_survive",
            "The term $\\gamma^\\mu\\Omega_\\mu$ of the field equation in the "
...)
```

`save_figure` saves the figure as `Revision/textbook/figures/08c_1_cancel_and_survive.png` with the caption printed under Figure 08c.1. Output of the cell:

```text
gamma^x0 Omega_x0 = (-Derivative(a4(x4), x4)/2 + Derivative(b4(x4), x4)/(4*b4(x4)))
    gamma^(x4) + (0) gamma^(x0)
gamma^x1 Omega_x1 = (Derivative(a4(x4), x4)/2) gamma^(x4) + (0) gamma^(x0)
gamma^x2 Omega_x2 = (Derivative(a4(x4), x4)/2) gamma^(x4) + (0) gamma^(x0)
gamma^x3 Omega_x3 = (Derivative(a4(x4), x4)/2) gamma^(x4) + (0) gamma^(x0)
gamma^x4 Omega_x4 = (0) gamma^(x4) + (0) gamma^(x0)
gamma^x5 Omega_x5 = (-Derivative(a4(x4), x4)/2 + Derivative(b4(x4), x4)/(4*b4(x4)))
    gamma^(x4) + (H*exp(a4(x4))/(2*sqrt(b4(x4)))) gamma^(x0)
gamma^x6 Omega_x6 = (-Derivative(a4(x4), x4)/2 + Derivative(b4(x4), x4)/(4*b4(x4)))
    gamma^(x4) + (H*exp(a4(x4))/(2*sqrt(b4(x4)))) gamma^(x0)
gamma^x7 Omega_x7 = (-Derivative(a4(x4), x4)/2 + Derivative(b4(x4), x4)/(4*b4(x4)))
    gamma^(x4) + (H*exp(a4(x4))/(2*sqrt(b4(x4)))) gamma^(x0)
PASS each gamma^mu Omega_mu (no sum) is a combination of gamma^(x4) and gamma^(x0)
sums: hidden block (x0, x5, x6, x7) -2*A1 + B1, 3-space 3*A1/2, gamma^(x0) part
    3*H*exp(a4(x4))/(2*sqrt(b4(x4)))
PASS per direction: h4/2, a4'/2 (x3), 0, and h4/2 with H e^a4 b4^(-1/2)/2 (x3)
     reproduces Revision/theory/reports/python-field-theory.json, check
    per_direction_terms
PASS gamma^mu Omega_mu = c_g gamma^(x0) + v_g gamma^(x4) in the diagonal frame
     reproduces Revision/theory/reports/python-field-theory.json, check
    gamma_mu_Omega_mu_equals_hidden_block_terms
c_g^2 - v_g^2 on the history: H**2*(81*exp(2*H*x4/3) - 25)/36
PASS G G = (c_g^2 - v_g^2) 1, H^2 ((9/4) e^(2 H x4/3) - 25/36) on the history; rank 8
    where c_g = +-v_g
     reproduces Revision/theory/reports/python-field-theory.json, check
    gravity_term_square
PASS (1/(2 sqrt|g|)) d_mu(sqrt|g| gamma^mu) = c_g gamma^(x0) + v_g gamma^(x4) (divergence
    form)
     reproduces Revision/theory/reports/python-field-theory.json, check
    divergence_of_sqrtg_gamma
PASS {gamma^mu, Omega_mu} = 0 for each mu: Omega drops out of the Lagrangian
     reproduces Revision/theory/reports/python-scope.json, check
    connection_free_lagrangian_same_equations
Figure 08c.1 saved as Revision/textbook/figures/08c_1_cancel_and_survive.png
```

**What Figure 08c.1 shows.** Left: the purple bars are $-\frac12$ (hidden direction), $+\frac12$ three times (3-space), 0 (time) and $-\frac12$ three times (extra times), with the sum $-\frac12$; the orange bars are $\frac14$ for each of the four directions of the hidden block and 0 for the others, with the sum 1. So $v_g = b_4'/b_4 - \frac12a_4'$: the six pieces $\pm\frac12a_4'$ of 3-space and of the extra times cancel, and what is left comes from the hidden block. Right: only the three red bars of the extra times are nonzero, $\frac12$ each, and the black sum is $\frac32$: $c_g = \frac32He^{a_4}b_4^{-1/2}$.

**In [7], the term sees the hidden block; the curvature and the flat member.**

```python
def riemann(rho, sigma, mu, nu, symbols=None):
    """R^rho_sigma,mu,nu from the Christoffel symbols (not simplified)."""
    Gs = Gam if symbols is None else symbols
    value = sp.diff(Gs[rho][nu][sigma], x[mu]) - sp.diff(Gs[rho][mu][sigma], x[nu])
    for lam in range(8):
        value += Gs[rho][mu][lam] * Gs[lam][nu][sigma] \
            - Gs[rho][nu][lam] * Gs[lam][mu][sigma]
    return value
```

`riemann(rho, sigma, mu, nu)` computes $R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \sum_\lambda(\Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma})$ from the Christoffel symbols `Gam`, or from another table given as `symbols` (used below for the flat member). The result is not simplified here.

```python
ricci_low = [[sum(riemann(rho, s, rho, n) for rho in range(8)) for n in range(8)]
             for s in range(8)]  # R_sn = R^rho_s,rho,n
ricci = [[ricci_low[mu][nu] / g[mu] for nu in range(8)] for mu in range(8)]  # R^mu_nu
off_diagonal_zero = all(is_zero(ricci[mu][nu]) for mu in range(8) for nu in range(8)
                        if mu != nu)
```

`ricci_low[s][n]` is the Ricci tensor $R_{\sigma\nu} = \sum_\rho R^\rho{}_{\sigma\rho\nu}$, and `ricci[mu][nu]` its mixed form $R^\mu{}_\nu = g^{\mu\mu}R_{\mu\nu}$ (for a diagonal metric $g^{\mu\mu} = 1/g_{\mu\mu}$). `off_diagonal_zero` is true when the 56 entries off the diagonal are zero.

```python
a4pp, u, v = sp.diff(a4, x4, 2), b4p / b4, sp.diff(b4, x4, 2) / b4
k_ratio = sp.exp(2 * a4) / b4  # k = e^(2 a4)/b4
block = (-3 * H**2 * k_ratio + a4p**2 - a4pp - sp.Rational(5, 2) * a4p * u + v / 2
         + u**2 / 2)  # R^x0_x0 = R^xt_xt
expected = ([block] + [-a4p**2 + a4pp + 2 * a4p * u] * 3
            + [7 * a4p**2 - a4pp - 4 * a4p * u + 2 * v - u**2] + [block] * 3)
check_record(off_diagonal_zero and all(is_zero(ricci[a][a] - expected[a])
                                       for a in range(8)),
             "R^mu_nu is diagonal and its eight entries equal the record",
             WOLFRAM, "ricci_mixed_components", "R^mu_nu is DIAGONAL",
             "R^x0_x0 = R^xt_xt = -3 Cb + a4'^2 - a4'' - (5/2) a4' b4'/b4 + (1/2) "
             "b4''/b4 + (1/2)(b4'/b4)^2 (t = 5, 6, 7",
             "R^xi_xi = -a4'^2 + a4'' + 2 a4' b4'/b4 (i = 1, 2, 3)",
             "R^x4_x4 = 7 a4'^2 - a4'' - 4 a4' b4'/b4 + 2 b4''/b4 - (b4'/b4)^2")
```

`a4pp` is $a_4''$, `u` is $b_4'/b_4$, `v` is $b_4''/b_4$ and `k_ratio` is $k = e^{2a_4}/b_4$. `block` is the common entry $R^{x_0}{}_{x_0} = R^{x_t}{}_{x_t}$ of Section 8.7, and `expected` the list of all eight diagonal entries. The check compares the computed diagonal with this list and requires the Wolfram record to state the same formulas (it writes `Cb` for $H^2k$; one piece ends in the middle of the record's sentence, at "(t = 5, 6, 7").

```python
ricci_scalar = sum(ricci[a][a] for a in range(8))
check_record(is_zero(ricci_scalar - (-12 * H**2 * k_ratio + 8 * a4p**2 - 2 * a4pp
                                     - 8 * a4p * u + 4 * v + u**2)),
             "Ricci scalar R = -12 H^2 e^(2 a4)/b4 + 8 a4'^2 - 2 a4'' - 8 a4' "
             "b4'/b4 + 4 b4''/b4 + (b4'/b4)^2", THEORY, "curvature_and_flat_member",
             "= -12 H^2 e^(2 a4)/b4 + 8 a4'^2 - 2 a4'' - 8 a4' b4'/b4 + 4 b4''/b4 + "
             "(b4'/b4)^2")
```

The Ricci scalar is the sum of the diagonal entries; the check proves the formula of Section 8.7.

```python
flat = {a4: 0, b4: H**2 * x4**2}  # the special history of the flat member
Gam_flat = [[[sp.simplify(Gam[l][m][n].subs(flat).doit()) for n in range(8)]
             for m in range(8)] for l in range(8)]
flat_ok = all(is_zero(riemann(rho, s, mu, nu, Gam_flat)) for rho in range(8)
              for s in range(8) for mu in range(8) for nu in range(mu + 1, 8))
G_flat = sp.simplify((c_g * G[0] + v_g * G[4]).subs(flat).doit())
say(f"G on the flat member: ({sp.simplify(c_g.subs(flat).doit())}) gamma^(x0) + "
    f"({sp.simplify(v_g.subs(flat).doit())}) gamma^(x4)")
space_history = sp.simplify(ricci[1][1].subs(history).doit())
say(f"R^x1_x1 on the history: {space_history}")
```

`flat` is the special history $a_4 = 0$, $b_4 = H^2x_4^2$. `Gam_flat` is the table of Christoffel symbols for it (substituted, the derivatives carried out with `doit`, and simplified). `flat_ok` is true when all $8 \cdot 8 \cdot 28 = 1792$ components $R^\rho{}_{\sigma\mu\nu}$ with $\mu < \nu$ vanish (the others follow from $R^\rho{}_{\sigma\nu\mu} = -R^\rho{}_{\sigma\mu\nu}$, and those with $\mu = \nu$ are zero). `G_flat` is the term $G$ on this member, printed with its two coefficients, and `space_history` is $R^{x_1}{}_{x_1}$ on the history of the record, also printed.

```python
check_record(flat_ok and G_flat != sp.zeros(16, 16)
             and is_zero(space_history - sp.Rational(5, 3) * H**2),
             "flat for a4 = 0, b4 = H^2 x4^2 (all Riemann components vanish, G != 0 "
             "there); curved on the history (R^x1_x1 = 5 H^2/3)",
             WOLFRAM, "flat_member_and_curvature",
             "the corrected metric is FLAT for a4 = 0, b4 = H^2 x4^2 (all 4096 "
             "R^r_smn vanish", "R != 0 (curved)")
check_record(total.has(a4) and not is_zero(ricci[4][4]),
             "gamma^mu Omega_mu contains a4 (e^a4 and a4'), and R^x4_x4 is not zero",
             "Revision/theory/reports/python-scope.json",
             "gammaOmega_sees_the_hidden_block", "contains a4 (e^a4 and a4')",
             "R^x4_x4 = 7 a4'^2 - a4'' - 4 a4' b4'/b4 + 2 b4''/b4 - (b4'/b4)^2")
```

The first check requires flatness, a nonzero term $G$ on the flat member, and $R^{x_1}{}_{x_1} = \frac53H^2$ on the history, together with the record's words. The second requires that $\gamma^\mu\Omega_\mu$ contains $a_4$ (`total.has(a4)` asks whether the function $a_4$ occurs in it) and that $R^{x_4}{}_{x_4}$ is not zero, as the scope record states.

```python
check(A_history == 1 and beta_4 == sp.Rational(4, 3) and b4_zero == 1,
      "the history of the record: A = 1, beta_4 = 4/3, b4(0) = 1",
      record="Revision/kohn_sham/results/parameters.json, physics.historyA, "
             "physics.historyBeta and physics.historyB4AtZero")
```

This check confirms the numbers of the history that the notebook uses: $A = 1$, $\beta_4 = \frac43$ and $b_4(0) = 1$.

```python
def along_history(expr):
    """A numpy function of x4 for expr with H = 1, the history, z = pi/4."""
    concrete = sp.sympify(expr).subs(W(x0), explicit_W).subs(history).doit()
    concrete = concrete.subs({H: 1, x0: sp.pi / 24})  # z = 6 x0 = pi/4
    return sp.lambdify(x4, concrete, "numpy")
```

`along_history` turns a symbolic expression into a numpy function of $x_4$ for the figure: it replaces `W(x0)` by the explicit root, inserts the history, puts $H = 1$ and $x_0 = \pi/24$ (so that $z = \pi/4$), and `sp.lambdify(x4, ...)` makes a Python function that evaluates the expression for arrays of numbers.

```python
times = np.linspace(0.0, 4.0, 201)
pieces = {"3-space: $\\omega_{x_1,(1)(4)} = a_4'e^{a_4}$": omega_diagonal[1, 1, 4],
          "hidden: $|\\omega_{x_0,(0)(4)}| = |h_4|e^{-a_4}b_4^{1/2}\\cot z$":
              omega_diagonal[0, 0, 4],
          "extra time: $|\\omega_{x_5,(4)(5)}| = |h_4|e^{-a_4}b_4^{1/2}W$":
              -ETA[4] * omega_diagonal[5, 4, 5],
          "extra time: $\\omega_{x_5,(0)(5)} = HW$": omega_diagonal[5, 0, 5]}
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
for (label, expr), style in zip(pieces.items(), ("-", "--", "-.", ":")):
    left.plot(times, np.abs(along_history(expr)(times)) * np.ones_like(times),
              style, label=label)
left.set_yscale("log")
left.set_xlabel("time $x_4$")
left.set_ylabel("size of the component")
left.set_title("Pieces of the connection")
left.legend(fontsize=7)
```

`times` holds 201 times from 0 to 4. `pieces` is a dictionary label: expression with four components of the connection: $\omega_{x_1\,(1)(4)}$, the hidden-direction component $\omega_{x_0\,(0)(4)}$, the extra-time component $\omega_{x_5\,(4)(5)}$ (the factor `-ETA[4]` $= 1$ lowers the index with $\eta_{44} = -1$ and changes the sign of the mixed component) and $\omega_{x_5\,(0)(5)}$. `zip` pairs each piece with a line style. The left panel draws the size of each piece on a logarithmic axis; the factor `np.ones_like(times)` turns a constant (a piece that does not depend on $x_4$ gives a single number) into an array of the right length.

```python
c_g_path = along_history(c_g)(times) * np.ones_like(times)
space_part = along_history(sum(coefficient_4[1:4]))(times) * np.ones_like(times)
block_part = along_history(coefficient_4[0] + sum(coefficient_4[5:8]))(times) \
    * np.ones_like(times)
right.plot(times, c_g_path, color="tab:red",
           label="$c_g = \\frac{3}{2}He^{a_4}b_4^{-1/2}$")
right.plot(times, space_part, color="tab:blue", label="3-space: $\\frac{3}{2}a_4'$")
right.plot(times, block_part, color="tab:green", label="hidden block: $2h_4$")
right.plot(times, space_part + block_part, color="black",
           label="$v_g = \\frac{3}{2}a_4' + 2h_4 = \\frac{5}{6}H$")
right.axhline(0.0, color="black", linewidth=0.6)
right.set_xlabel("time $x_4$")
right.set_ylabel("coefficient")
right.set_title("The parts of the term")
right.legend(fontsize=8);
```

`c_g_path` is $c_g$ along the history; `space_part` is the 3-space part $\frac32a_4'$ of $v_g$ and `block_part` the hidden-block part $2h_4$ (the $\gamma^{(4)}$ coefficients of $x_0$ and of the three extra times). The right panel draws them and their sum $v_g$, with a zero line. The last line ends with `;` so that Jupyter prints nothing for it.

```python
save_figure(fig, "pieces_along_history",
            "Along the canonical history $a_4 = x_4$, $b_4 = e^{4x_4/3}$ of the "
...)
```

The figure is saved as `08c_2_pieces_along_history.png`. Output of the cell:

```text
PASS R^mu_nu is diagonal and its eight entries equal the record
     reproduces Revision/theory/reports/wolfram-field-theory.json, check
    ricci_mixed_components
PASS Ricci scalar R = -12 H^2 e^(2 a4)/b4 + 8 a4'^2 - 2 a4'' - 8 a4' b4'/b4 + 4 b4''/b4 +
    (b4'/b4)^2
     reproduces Revision/theory/reports/python-field-theory.json, check
    curvature_and_flat_member
G on the flat member: (3/(2*Abs(x4))) gamma^(x0) + (2/x4) gamma^(x4)
R^x1_x1 on the history: 5*H**2/3
PASS flat for a4 = 0, b4 = H^2 x4^2 (all Riemann components vanish, G != 0 there); curved
    on the history (R^x1_x1 = 5 H^2/3)
     reproduces Revision/theory/reports/wolfram-field-theory.json, check
    flat_member_and_curvature
PASS gamma^mu Omega_mu contains a4 (e^a4 and a4'), and R^x4_x4 is not zero
     reproduces Revision/theory/reports/python-scope.json, check
    gammaOmega_sees_the_hidden_block
PASS the history of the record: A = 1, beta_4 = 4/3, b4(0) = 1
     reproduces Revision/kohn_sham/results/parameters.json, physics.historyA,
    physics.historyBeta and physics.historyB4AtZero
Figure 08c.2 saved as Revision/textbook/figures/08c_2_pieces_along_history.png
```

The flat member has $c_g = 3/(2|x_4|)$ and $v_g = 2/x_4$ (sympy keeps the absolute value from $\sqrt{x_4^2}$), and on the history $R^{x_1}{}_{x_1} = 5H^2/3$, as in Section 8.7.

**What Figure 08c.2 shows.** Left (logarithmic axis, $z = \pi/4$, $H = 1$): the component of the inflating direction $x_1$ rises like $e^{x_4}$; the two components with the rate $h_4 = -\frac13$ (hidden direction and extra time $x_5$) fall like $e^{-x_4/3}$; and $HW = 2^{-1/12} \approx 0.944$ is a horizontal line. Right: $c_g = \frac32e^{x_4/3}$ rises from 1.5; the 3-space part $\frac32$ and the hidden-block part $-\frac23$ are constant, and their sum $v_g = \frac56$ is constant too.

**In [8], the boosted frame.**

```python
rapidity = sp.Function("b")(x4)  # any rapidity b(x4)
rate_b = sp.diff(rapidity, x4)  # b'
boosted = frame(rapidity)
e_b = boosted["e"]
```

`rapidity` is an unknown function $b(x_4)$ and `rate_b` its derivative $b'$. `frame(rapidity)` computes the boosted frame, its inverse, its canonical connection, its spinor connections and its coordinate gammas, all with the unknown function $b$; `e_b` is its vielbein.

```python
same_metric = all(
    is_zero(sum(ETA[a] * e_b[a, mu] * e_b[a, nu] for a in range(8))
            - (g[mu] if mu == nu else 0)) for mu in range(8) for nu in range(8))
SCOPE = "Revision/theory/reports/python-scope.json"  # the record of these checks
check_record(same_metric and all(is_zero(v) for v in e_b * boosted["E"] - sp.eye(8)),
             "the boosted frame gives the same metric (64 entries); e' E' = 1",
             SCOPE, "boosted_frame_reproduces_metric",
             "equals the corrected metric for all 64 (mu, nu)")
```

`same_metric` checks $\sum_a\eta_{aa}e'^a{}_\mu e'^a{}_\nu = g_{\mu\nu}$ for all 64 pairs (the conditional expression gives $g_{\mu\mu}$ on the diagonal and 0 off it). The check also proves $e'E' = I_8$, and requires the scope record's words.

```python
failures = postulate_failures(boosted)  # the number of nonzero components
check_record(failures == 0 and antisymmetric(boosted),
             "boosted frame: vielbein postulate (512 components), omega' antisymmetric",
             SCOPE, "boosted_frame_canonical_connection",
             f"holds for all 512 (a, mu, nu) ({failures} failures)")
```

The vielbein postulate holds for all 512 components of the boosted frame (zero failures), and the boosted connection is antisymmetric; the record's detail must contain the same count of failures, 0.

```python
total_boosted = sum((boosted["gamma"][mu] * boosted["Omega"][mu] for mu in range(8)),
                    sp.zeros(16, 16))
v_boost = sp.cosh(rapidity) * G[0] - sp.sinh(rapidity) * G[4]
w_boost = sp.cosh(rapidity) * G[4] - sp.sinh(rapidity) * G[0]
formula = (c_g - rate_b / 2) * v_boost + v_g * w_boost
c0 = (c_g - rate_b / 2) * sp.cosh(rapidity) - v_g * sp.sinh(rapidity)
c4 = -(c_g - rate_b / 2) * sp.sinh(rapidity) + v_g * sp.cosh(rapidity)
beta, b0 = sp.symbols("beta b0", real=True)  # a rapidity beta x4 + b0
linear = {rapidity: beta * x4 + b0}
formula_linear = (c_g - beta / 2) * v_boost.subs(linear) + v_g * w_boost.subs(linear)
```

`total_boosted` is $\gamma'^\mu\Omega'_\mu$. `v_boost` and `w_boost` are the two matrices $\cosh b\,\gamma^{(0)} - \sinh b\,\gamma^{(4)}$ and $\cosh b\,\gamma^{(4)} - \sinh b\,\gamma^{(0)}$ of Section 8.9, and `formula` is the derived result: $(c_g - b'/2)$ times the first matrix plus $v_g$ times the second. `c0` and `c4` are its coefficients of $\gamma^{(0)}$ and $\gamma^{(4)}$. `beta` and `b0` are two real constants, `linear` the substitution $b = \beta x_4 + b_0$, and `formula_linear` the record's form of the formula for that rapidity.

```python
check_record(all(is_zero(entry) for entry in total_boosted - formula)
             and all(is_zero(entry) for entry in formula - c0 * G[0] - c4 * G[4])
             and is_zero(sp.cosh(rapidity) * c4 + sp.sinh(rapidity) * c0 - v_g)
             and all(is_zero(entry) for entry in formula.subs(linear).doit()
                     - formula_linear),
             "gamma'^mu Omega'_mu = (c_g - b'/2) v + v_g w; cosh b c4 + sinh b c0 = "
             "v_g", SCOPE, "boosted_frame_gammaOmega_formula",
             "gamma'^mu Omega'_mu = (cg - beta/2) (cosh b gamma^(x0) - sinh b "
             "gamma^(x4)) + vg (cosh b gamma^(x4) - sinh b gamma^(x0))",
             "cosh b c4 + sinh b c0 = vg for every beta")
```

The check proves four things: the computed $\gamma'^\mu\Omega'_\mu$ equals the formula entry by entry, for every function $b$; the formula equals $c_0\gamma^{(0)} + c_4\gamma^{(4)}$; $\cosh b\,c_4 + \sinh b\,c_0 = v_g$; and for $b = \beta x_4 + b_0$ the formula is the record's.

```python
removing = {rate_b: 2 * c_g}  # the rapidity rate b' = 2 c_g
nonzero_Omega = [mu for mu in range(8) if not all(
    is_zero(boosted["omega"][mu, a, c].subs(removing))
    for a in range(8) for c in range(a + 1, 8))]
nonzero_text = ", ".join(f"x{mu}" for mu in nonzero_Omega)  # "x0, x1, ..."
say("b' = 2 c_g: Omega'_mu is nonzero for mu = " + nonzero_text)
```

`removing` replaces $b'$ by $2c_g$. `nonzero_Omega` lists the directions $\mu$ for which some component $\omega'_{\mu ac}$ ($a < c$) of the boosted connection is not zero after this replacement; since the $S^{ac}$ are independent (rank 28, In [5]), these are exactly the directions with $\Omega'_\mu \neq 0$. They are printed.

```python
check_record(all(is_zero(entry) for entry in total_boosted.subs(removing)
                 - v_g * w_boost)
             and nonzero_Omega == list(range(8)),
             "b' = 2 c_g: gamma'^mu Omega'_mu = v_g w, only the v_g part; Omega'_mu != "
             "0 for every mu", SCOPE, "boosted_frame_removes_only_the_H_term",
             "with a rapidity b(x4) of rate b' = 2 cg = 3 H e^a4 b4^(-1/2)",
             "is vg (cosh b gamma^(x4) - sinh b gamma^(x0))",
             f"Omega'_mu itself is nonzero for mu = {nonzero_text}")
```

The check proves that with $b' = 2c_g$ the term is $v_g\,$`w_boost` and that $\Omega'_\mu \neq 0$ for all eight directions; the record's detail must name the same directions. Output of the cell:

```text
PASS the boosted frame gives the same metric (64 entries); e' E' = 1
     reproduces Revision/theory/reports/python-scope.json, check
    boosted_frame_reproduces_metric
PASS boosted frame: vielbein postulate (512 components), omega' antisymmetric
     reproduces Revision/theory/reports/python-scope.json, check
    boosted_frame_canonical_connection
PASS gamma'^mu Omega'_mu = (c_g - b'/2) v + v_g w; cosh b c4 + sinh b c0 = v_g
     reproduces Revision/theory/reports/python-scope.json, check
    boosted_frame_gammaOmega_formula
b' = 2 c_g: Omega'_mu is nonzero for mu = x0, x1, x2, x3, x4, x5, x6, x7
PASS b' = 2 c_g: gamma'^mu Omega'_mu = v_g w, only the v_g part; Omega'_mu != 0 for every
    mu
     reproduces Revision/theory/reports/python-scope.json, check
    boosted_frame_removes_only_the_H_term
```

**In [9], the size of the term in four frames.**

```python
def term_on_history(rapidity_expr, *extra):
    """A numpy function of x4 (and of the extra symbols given): the 16 x 16 matrix
    gamma'^mu Omega'_mu for the given rapidity b(x4), on the history with H = 1."""
    concrete = formula.subs(rapidity, rapidity_expr).doit()
    concrete = concrete.subs(history).doit().subs(H, 1)
    return sp.lambdify((x4, *extra), concrete, "numpy")
```

`term_on_history` inserts a rapidity into the formula of In [8] (which the check there proved equal to the computed matrix), then the history and $H = 1$, and makes a numpy function of $x_4$ and of any further symbols given in `extra` (`*extra` collects them; `(x4, *extra)` is the tuple of all arguments).

```python
def size(matrix):
    """sqrt(tr(M^T M)/16): the size of a 16 x 16 matrix, 1 for gamma^(x0)."""
    matrix = np.array(matrix, dtype=float)
    return np.sqrt(np.trace(matrix.T @ matrix) / 16)
```

`size` computes $\sqrt{\mathrm{tr}(M^TM)/16}$ of a $16 \times 16$ matrix: `np.array(..., dtype=float)` turns it into floating-point numbers, `matrix.T` is the transpose, `@` is matrix multiplication and `np.trace` the sum of the diagonal. For $M = c_0\gamma^{(0)} + c_4\gamma^{(4)}$ this is $\sqrt{c_0^2 + c_4^2}$ (Exercise 5 of Section 8.39).

```python
frames = {"diagonal frame, $b = 0$": sp.Integer(0),
          "constant rate, $b = 3x_4$": 3 * x4,
          "half: $b = \\frac{9}{2}(e^{x_4/3} - 1)$":
              sp.Rational(9, 2) * (sp.exp(x4 / 3) - 1),
          "removing: $b = 9(e^{x_4/3} - 1)$": 9 * (sp.exp(x4 / 3) - 1)}
terms = {label: term_on_history(expr) for label, expr in frames.items()}
beta_values = np.linspace(0.0, 8.0, 161)
linear_term = term_on_history(beta * x4, beta)  # rate beta, b(0) = 0: of x4, beta
sizes_beta = [size(linear_term(0.0, value)) for value in beta_values]
diagonal_size = size(terms["diagonal frame, $b = 0$"](0.0))
removing_size = size(terms["removing: $b = 9(e^{x_4/3} - 1)$"](0.0))
```

`frames` holds four rapidities: zero (the diagonal frame), the constant rate $b = 3x_4$, half of the removing rapidity, and the removing rapidity $b = 9(e^{x_4/3} - 1)$, whose derivative $3e^{x_4/3}$ is $2c_g$ on the history. `terms` holds the numpy function of each. `linear_term` is the term for the rapidity $\beta x_4$ (so $b(0) = 0$), as a function of $x_4$ and $\beta$, and `sizes_beta` its size at $x_4 = 0$ for 161 rates $\beta$ from 0 to 8. `diagonal_size` and `removing_size` are the sizes at $x_4 = 0$ in the diagonal and in the removing frame.

```python
report("size at x4 = 0: diagonal frame, removing frame",
       f"{diagonal_size:.6f}, {removing_size:.6f}")
check(abs(diagonal_size - np.sqrt(106.0) / 6) < 1e-12
      and abs(removing_size - 5.0 / 6.0) < 1e-12
      and min(sizes_beta) >= 5.0 / 6.0 - 1e-12,
      "on the history at x4 = 0: size sqrt(106)/6 in the diagonal frame, at least "
      "v_g = 5/6 for every rate beta, and 5/6 for b' = 2 c_g")
```

The two sizes are printed. The check compares them with $\sqrt{(3/2)^2 + (5/6)^2} = \sqrt{106}/6$ and $v_g = \frac56$ (at $x_4 = 0$ the rapidity is 0, so $\cosh b = 1$), and requires every size on the $\beta$ grid to be at least $\frac56$: at $x_4 = 0$ the size is $\sqrt{(c_g - \beta/2)^2 + v_g^2} \geq v_g$.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
left.plot(beta_values, sizes_beta)
left.plot([0.0, 3.0], [diagonal_size, removing_size], "o", color="black")
left.annotate("diagonal frame: $c_g\\gamma^{(0)} + v_g\\gamma^{(4)}$",
              (0.0, diagonal_size), (0.4, 2.6))
left.annotate("$\\beta = 2c_g$: only $v_g\\gamma^{(4)}$", (3.0, removing_size),
              (3.4, 0.3))
left.set_xlabel("rapidity rate $\\beta = b'(0)$ (units of $H$)")
left.set_ylabel("size of $\\gamma'^\\mu\\Omega'_\\mu$ (units of $H$)")
left.set_title("At $x_4 = 0$, $b(0) = 0$")
left.set_ylim(0.0, 3.2)
```

The left panel draws the size against $\beta$, marks the two values with black dots (`"o"`) and labels them with `annotate(text, point, text position)`; `set_ylim` fixes the vertical range.

```python
times = np.linspace(0.0, 1.0, 101)
for label, function in terms.items():
    right.plot(times, [size(function(t)) for t in times], label=label)
right.set_yscale("log")
right.set_xlabel("time $x_4$ (units of $1/H$)")
right.set_ylabel("size (units of $H$)")
right.set_title("Against time, on the history")
right.legend(fontsize=8);
```

The right panel draws, for 101 times from 0 to 1, the size of the term in each of the four frames, on a logarithmic axis, with a legend.

```python
save_figure(fig, "boost_size",
            "The size $\\sqrt{\\mathrm{tr}(M^TM)/16}$ of the term $M = "
...)
```

The figure is saved as `08c_3_boost_size.png`. Output:

```text
RESULT size at x4 = 0: diagonal frame, removing frame = 1.715938, 0.833333
PASS on the history at x4 = 0: size sqrt(106)/6 in the diagonal frame, at least v_g = 5/6
    for every rate beta, and 5/6 for b' = 2 c_g
Figure 08c.3 saved as Revision/textbook/figures/08c_3_boost_size.png
```

**What Figure 08c.3 shows.** Left: a curve with its lowest point $\frac56$ at $\beta = 3$ and the value $1.716$ at $\beta = 0$; it rises again on both sides (at $\beta = 8$ it is $\sqrt{2.5^2 + (5/6)^2} \approx 2.64$). Right (logarithmic axis): the diagonal frame's size grows slowly with $c_g$, from 1.716 to about 2.3 at $x_4 = 1$; the removing frame starts at $\frac56$ and grows fastest, like $\frac56\sqrt{\cosh 2b}$, to about 21 at $x_4 = 1$, because its rapidity keeps growing; the frame with $b = 3x_4$ starts at $\frac56$ too (its rate equals $2c_g$ only at $x_4 = 0$) and grows to about 3.4; the half frame starts at $\sqrt{0.75^2 + (5/6)^2} \approx 1.12$, falls to about 0.47 near $x_4 = 0.68$ and rises again. No curve reaches zero: no frame of this family removes the term.

**In [10], the matrices themselves.**

```python
maps = [("diagonal frame", terms["diagonal frame, $b = 0$"](0.3)),
        ("boosted, $b = 3x_4$", terms["constant rate, $b = 3x_4$"](0.3)),
        ("boosted, $b' = 2c_g$", terms["removing: $b = 9(e^{x_4/3} - 1)$"](0.3))]
```

`maps` holds three titles and three matrices: the term at $x_4 = 0.3$ in the diagonal frame, in the frame with $b = 3x_4$, and in the removing frame.

```python
fig, panels = plt.subplots(1, 3, figsize=(11.0, 3.9))
for panel, (title, matrix) in zip(panels, maps):
    image = panel.imshow(np.array(matrix, dtype=float), cmap="RdBu_r", vmin=-2.0,
                         vmax=2.0)
    panel.set_title(title, fontsize=10)
    panel.set_xticks([0, 5, 10, 15])
    panel.set_yticks([0, 5, 10, 15])
    panel.set_xlabel("column")
    panel.grid(False)  # no grid lines over the coloured squares
panels[0].set_ylabel("row")
fig.colorbar(image, ax=list(panels), shrink=0.8, label="entry (units of $H$)")
```

Three panels side by side (11 by 3.9 inches). `imshow` draws each matrix as a picture of $16 \times 16$ coloured squares with the colour map `RdBu_r` (red for positive, blue for negative, white for zero) and the fixed range from $-2$ to $2$, so that the three maps are comparable; the ticks mark rows and columns 0, 5, 10, 15, and `grid(False)` removes the grid lines. One colour bar serves all three panels.

```python
save_figure(fig, "heat_maps",
            "The $16 \\times 16$ matrix $\\gamma^\\mu\\Omega_\\mu$ of the field "
...)
```

The figure is saved as `08c_4_heat_maps.png`. Output:

```text
Figure 08c.4 saved as Revision/textbook/figures/08c_4_heat_maps.png
```

**What Figure 08c.4 shows.** Left: 32 coloured squares, sixteen of the value $c_g = 1.658$ (the pattern of $\gamma^{(0)}$) and sixteen of $\pm\frac56$ (the pattern of $\gamma^{(4)}$). Middle and right: the same 32 positions with other values, because the boost mixes the two patterns; in the right panel the coefficients are $-v_g\sinh b$ for $\gamma^{(0)}$ and $v_g\cosh b$ for $\gamma^{(4)}$ with $b = 0.946$, that is $-0.912$ and $1.235$: the part $c_g$ is gone, the part $v_g$ is not.

**In [11], the curvature in two frames.**

```python
def spinor_curvature(fr):
    """F_x5x0 = d_5 Omega_0 - d_0 Omega_5 + [Omega_5, Omega_0]."""
    O5, O0 = fr["Omega"][5], fr["Omega"][0]
    return sp.diff(O0, x[5]) - sp.diff(O5, x[0]) + O5 * O0 - O0 * O5
```

`spinor_curvature` computes $F_{x_5x_0} = \partial_5\Omega_{x_0} - \partial_0\Omega_{x_5} + \Omega_{x_5}\Omega_{x_0} - \Omega_{x_0}\Omega_{x_5}$ for the spinor connection of a frame.

```python
def riemann_side(fr):
    """(1/4) sum R_rho,sigma,x5,x0 gamma^rho gamma^sigma in the frame fr."""
    result = sp.zeros(16, 16)
    for rho in range(8):
        for sigma in range(8):
            value = g[rho] * riemann(rho, sigma, 5, 0)  # lower the first index
            if not is_zero(value):
                result += value * fr["gamma"][rho] * fr["gamma"][sigma] / 4
    return result
```

`riemann_side` computes $\frac14\sum_{\rho,\sigma}R_{\rho\sigma x_5x_0}\gamma^\rho\gamma^\sigma$ with the coordinate gammas of a frame: the first index of the Riemann tensor is lowered with $g_{\rho\rho}$, and terms whose coefficient is zero are skipped.

```python
P05, P45 = G[0] * G[5], G[4] * G[5]  # gamma^(0) gamma^(5) and gamma^(4) gamma^(5)


def two_coefficients(F):
    """c05, c45 with F = c05 P05 + c45 P45 (P05^2 = 1, P45^2 = -1), and whether
    nothing else is left."""
    c05 = sp.simplify((P05 * F).trace() / 16)
    c45 = sp.simplify(-(P45 * F).trace() / 16)
    return c05, c45, all(is_zero(v) for v in F - c05 * P05 - c45 * P45)
```

`P05` and `P45` are the products $\gamma^{(0)}\gamma^{(5)}$ and $\gamma^{(4)}\gamma^{(5)}$, whose squares are $I_{16}$ and $-I_{16}$. `two_coefficients` finds $c_{05}$ and $c_{45}$ with $F = c_{05}P_{05} + c_{45}P_{45}$ from traces, exactly as In [6] found $c_0$ and $c_4$, and reports whether nothing else is left.

```python
frame_removing = {"Omega": [M.subs(removing) for M in boosted["Omega"]],
                  "gamma": boosted["gamma"]}  # the frame with b' = 2 c_g
F_diagonal = spinor_curvature(diagonal)
F_boosted = spinor_curvature(frame_removing)
```

`frame_removing` is the boosted frame with $b' = 2c_g$ inserted into its spinor connections (only $\Omega'_{x_4}$ contains $b'$). `F_diagonal` and `F_boosted` are the two curvatures.

```python
check_record(all(is_zero(v) for v in F_diagonal - riemann_side(diagonal)),
             "diagonal frame: F_x5x0 = (1/4) R_rho,sigma,x5,x0 gamma^rho gamma^sigma",
             THEORY, "spinor_curvature_equals_riemann",
             "= (1/4) R_{rho sigma mu nu} gamma^rho gamma^sigma")
check(all(is_zero(v) for v in F_boosted - riemann_side(frame_removing)),
      "boosted frame (b' = 2 c_g): F'_x5x0 = (1/4) R gamma'^rho gamma'^sigma")
```

The two checks prove $F = \frac14R\gamma\gamma$ in both frames for $(\mu, \nu) = (x_5, x_0)$; the first is also the record's check.

```python
c05, c45, only_two = two_coefficients(F_diagonal)
c05_b, c45_b, only_two_b = two_coefficients(F_boosted)
say(f"diagonal frame: c05 = {c05}")
say(f"diagonal frame: c45 = {c45}")
say(f"boosted frame:  c05 = {c05_b}")
say(f"boosted frame:  c45 = {c45_b}")
expected_c05 = sp.cot(z) * W(x0) * (rate_h4**2 * sp.exp(-2 * a4) * b4 - H**2) / 2
check(only_two and only_two_b and is_zero(c45) and is_zero(c05 - expected_c05),
      "in both frames F_x5x0 = c05 g0 g5 + c45 g4 g5; diagonal: c45 = 0, c05 = "
      "(1/2) cot z W (h4^2 e^(-2 a4) b4 - H^2)")
```

The coefficients of both frames are computed and printed. `expected_c05` is $\frac12\cot z\,W(h_4^2e^{-2a_4}b_4 - H^2)$, the hand computation of Section 8.10. The check proves that in both frames nothing but the two products appears, that $c_{45} = 0$ in the diagonal frame, and that $c_{05}$ is the expected value.

```python
check(is_zero(c05_b**2 - c45_b**2 - c05**2)
      and is_zero(expected_c05.subs(flat).doit()),
      "F^2 = F'^2 = c05^2 I16 in both frames; c05 = 0 on the flat member")
```

This check proves $c_{05}'^2 - c_{45}'^2 = c_{05}^2$ (so $F'^2 = F^2$) and that $c_{05}$ vanishes on the flat member.

```python
entries_nonzero = sum(1 for v in F_boosted if not is_zero(v))
report("nonzero entries of F'_x5x0 in the frame boosted with b' = 2 c_g",
       entries_nonzero)
check_record(entries_nonzero > 0, "b' = 2 c_g: the spinor curvature F'_x5x0 is not "
             "zero", SCOPE, "boosted_frame_curvature_nonzero",
             "the spinor curvature F'_x5x0 = d_x5 Omega'_x0 - d_x0 Omega'_x5 + "
             "[Omega'_x5, Omega'_x0] is nonzero for general a4, b4")
```

`entries_nonzero` counts the nonzero entries of $F'_{x_5x_0}$ in the removing frame; it is printed, and the check requires it to be positive, as the record states. Output:

```text
PASS diagonal frame: F_x5x0 = (1/4) R_rho,sigma,x5,x0 gamma^rho gamma^sigma
     reproduces Revision/theory/reports/python-field-theory.json, check
    spinor_curvature_equals_riemann
PASS boosted frame (b' = 2 c_g): F'_x5x0 = (1/4) R gamma'^rho gamma'^sigma
diagonal frame: c05 = (-4*H**2*b4(x4)*exp(2*a4(x4)) + (2*b4(x4)*Derivative(a4(x4), x4) -
    Derivative(b4(x4), x4))**2)*W(x0)*exp(-2*a4(x4))*cot(6*H*x0)/(8*b4(x4))
diagonal frame: c45 = 0
boosted frame:  c05 = -(4*H**2*b4(x4)*exp(2*a4(x4)) - 4*b4(x4)**2*Derivative(a4(x4),
    x4)**2 + 4*b4(x4)*Derivative(a4(x4), x4)*Derivative(b4(x4), x4) - Derivative(b4(x4),
    x4)**2)*W(x0)*exp(-2*a4(x4))*cosh(b(x4))/(8*b4(x4)*tan(6*H*x0))
boosted frame:  c45 = (4*H**2*b4(x4)*exp(2*a4(x4)) - 4*b4(x4)**2*Derivative(a4(x4),
    x4)**2 + 4*b4(x4)*Derivative(a4(x4), x4)*Derivative(b4(x4), x4) - Derivative(b4(x4),
    x4)**2)*W(x0)*exp(-2*a4(x4))*sinh(b(x4))/(8*b4(x4)*tan(6*H*x0))
PASS in both frames F_x5x0 = c05 g0 g5 + c45 g4 g5; diagonal: c45 = 0, c05 = (1/2) cot z
    W (h4^2 e^(-2 a4) b4 - H^2)
PASS F^2 = F'^2 = c05^2 I16 in both frames; c05 = 0 on the flat member
RESULT nonzero entries of F'_x5x0 in the frame boosted with b' = 2 c_g = 32
PASS b' = 2 c_g: the spinor curvature F'_x5x0 is not zero
     reproduces Revision/theory/reports/python-scope.json, check
    boosted_frame_curvature_nonzero
```

The boosted coefficients are $c_{05}\cosh b$ and $-c_{05}\sinh b$ (sympy writes $\cot z$ as $1/\tan z$ there): $F' = c_{05}(\cosh b\,\gamma^{(0)}\gamma^{(5)} - \sinh b\,\gamma^{(4)}\gamma^{(5)})$, as Section 8.10 derived from $F' = SFS^{-1}$. The 32 nonzero entries are the 16 of each product.

**In [12], the curvature at one point of the history.**

```python
point = {H: 1, x0: sp.pi / 24, x4: sp.Rational(1, 2)}  # z = pi/4, x4 = 0.5


def at_point(matrix):
    """The numbers of a symbolic matrix at H = 1 on the history, z = pi/4, x4 = 0.5,
    for the removing rapidity b = 9 (e^(x4/3) - 1)."""
    concrete = matrix.subs(rapidity, 9 * (sp.exp(x4 / 3) - 1)).doit()
    concrete = concrete.subs(W(x0), explicit_W).subs(history).doit()
    return np.array(concrete.subs(point).evalf(), dtype=float)
```

`point` sets $H = 1$, $x_0 = \pi/24$ ($z = \pi/4$) and $x_4 = \frac12$. `at_point` inserts the removing rapidity, the explicit warp factor and the history into a symbolic matrix, then the point, evaluates it numerically (`evalf`) and returns a numpy array.

```python
F_numbers = [("diagonal frame: $F_{x_5x_0}$", at_point(F_diagonal)),
             ("boosted, $b' = 2c_g$: $F'_{x_5x_0}$", at_point(F_boosted))]
c05_number = float(expected_c05.subs(W(x0), explicit_W).subs(history).doit()
                   .subs(point))
b_number = 9 * (np.exp(0.5 / 3) - 1)  # the rapidity at x4 = 0.5
P05_number, P45_number = (np.array(P, dtype=float) for P in (P05, P45))
report("c05 at the point and the rapidity there", f"{c05_number:.6f}, {b_number:.6f}")
ranks = [int(np.linalg.matrix_rank(matrix)) for _, matrix in F_numbers]
report("rank of F_x5x0 at the point (diagonal, boosted)", ranks)
```

`F_numbers` holds the two curvature matrices at the point with their panel titles. `c05_number` is $c_{05}$ there and `b_number` the rapidity $9(e^{1/6} - 1)$. `P05_number` and `P45_number` are the two products as floating-point arrays (a **generator expression** in round brackets, unpacked into two names). Both numbers are printed, then the ranks of the two matrices.

```python
squares_ok = all(np.allclose(matrix @ matrix, c05_number**2 * np.eye(16), atol=1e-12)
                 for _, matrix in F_numbers)
form_ok = np.allclose(F_numbers[1][1], c05_number * (np.cosh(b_number) * P05_number
                                                     - np.sinh(b_number) * P45_number),
                      atol=1e-12)
check(ranks == [16, 16] and squares_ok and form_ok,
      "on the history: F and F' have rank 16, F^2 = F'^2 = c05^2 1, F' = c05 (cosh b "
      "g0 g5 - sinh b g4 g5)")
```

The check requires rank 16 for both, $F^2 = F'^2 = c_{05}^2I_{16}$ to $10^{-12}$ (`np.allclose` compares entry by entry within the tolerance `atol`), and the boosted matrix to equal $c_{05}(\cosh b\,P_{05} - \sinh b\,P_{45})$.

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
```

Two panels; each matrix gets its own symmetric colour range from $-$`largest` to `largest` (its largest entry in size) and its own colour bar.

```python
save_figure(fig, "curvature_maps",
            "The spinor curvature $F_{x_5x_0} = \\partial_5\\Omega_0 - "
...)
```

The figure is saved as `08c_5_curvature_maps.png`. Output:

```text
RESULT c05 at the point and the rapidity there = -0.434364, 1.632244
RESULT rank of F_x5x0 at the point (diagonal, boosted) = [16, 16]
PASS on the history: F and F' have rank 16, F^2 = F'^2 = c05^2 1, F' = c05 (cosh b g0 g5
    - sinh b g4 g5)
Figure 08c.5 saved as Revision/textbook/figures/08c_5_curvature_maps.png
```

**What Figure 08c.5 shows.** Left: sixteen squares of the value $-0.434$ and its negative in the pattern of $\gamma^{(0)}\gamma^{(5)}$, all others white. Right: 32 squares, the entries $c_{05}\cosh b = -1.153$ in the pattern of $\gamma^{(0)}\gamma^{(5)}$ and $-c_{05}\sinh b = 1.069$ in the pattern of $\gamma^{(4)}\gamma^{(5)}$, with their signs ($b = 1.632$). Neither matrix is zero: the frame in which the term lost its part $c_g$ still has a curved connection.

**In [13], the connection in the energy-momentum tensor.**

```python
g4_up = diagonal["gamma"][4]  # gamma^x4 = gamma^(x4), because f_4 = 1
part_1 = (g4_up * diagonal["Omega"][1] + diagonal["Omega"][1] * g4_up) / 2
part_5 = (g4_up * diagonal["Omega"][5] + diagonal["Omega"][5] * g4_up) / 2
target = H * W(x0) * G[4] * G[0] * G[5] / 2
```

`g4_up` is $\gamma^{x_4} = \gamma^{(4)}$. `part_1` and `part_5` are $\frac12\{\gamma^{x_4}, \Omega_{x_1}\}$ and $\frac12\{\gamma^{x_4}, \Omega_{x_5}\}$ in the diagonal frame, and `target` is $\frac12HW\gamma^{(4)}\gamma^{(0)}\gamma^{(5)}$ of Section 8.11.

```python
check_record(all(is_zero(v) for v in part_1)
             and all(is_zero(v) for v in part_5 - target)
             and C * G[4] * G[0] * G[5] != sp.zeros(16, 16),
             "(1/2){gamma^x4, Omega_x1} = 0, (1/2){gamma^x4, Omega_x5} = (1/2) H W "
             "g4 g0 g5, and C g4 g0 g5 != 0",
             SCOPE, "spin_connection_in_the_energy_momentum_tensor",
             "is (1/2) Phibar {gamma^x4, Omega_x1} Phi = 0 (3-space does not depend "
             "on x0)", "(1/2) H (sin^2 z)^(1/12) Phibar gamma^(x4) gamma^(x0) "
             "gamma^(x5) Phi (the a4', b4' part cancels exactly)",
             "C gamma^(x4) gamma^(x0) gamma^(x5) != 0")
```

The check proves that `part_1` is zero, that `part_5` equals the target, and that $C\gamma^{(4)}\gamma^{(0)}\gamma^{(5)}$ is not the zero matrix, and it requires the scope record to say the same. Output:

```text
PASS (1/2){gamma^x4, Omega_x1} = 0, (1/2){gamma^x4, Omega_x5} = (1/2) H W g4 g0 g5, and C
    g4 g0 g5 != 0
     reproduces Revision/theory/reports/python-scope.json, check
    spin_connection_in_the_energy_momentum_tensor
```

**In [14], the last check.**

```python
for name in ("08c_1_cancel_and_survive.png", "08c_2_pieces_along_history.png",
             "08c_3_boost_size.png", "08c_4_heat_maps.png", "08c_5_curvature_maps.png"):
    check(output_file(f"{FIGURE_FOLDER}/{name}").is_file(),
          f"the figure file {name} exists")
all_checks_passed()
```

The loop checks that each of the five figure files exists (`is_file()`), and `all_checks_passed()` prints the final line. Output:

```text
PASS the figure file 08c_1_cancel_and_survive.png exists
PASS the figure file 08c_2_pieces_along_history.png exists
PASS the figure file 08c_3_boost_size.png exists
PASS the figure file 08c_4_heat_maps.png exists
PASS the figure file 08c_5_curvature_maps.png exists
ALL 37 CHECKS PASSED (notebook 08c)
```

### 8.16 Well-posedness: what a good evolution equation must do

**The initial-value problem.** A field equation that contains the time derivative $\partial_4\Psi$ is used like this: one gives the field on the slice $x_4 = 0$ (a seven-dimensional set with the coordinates $x_1, x_2, x_3, x_5, x_6, x_7, x_0$), the **data**, and asks for the field at later times. This is the **initial-value problem**, also called the **Cauchy problem**. The French mathematician Jacques Hadamard called such a problem **well posed** if three things hold: a solution exists; it is unique; and it depends **continuously** on the data, which means: for every later time and every tolerance, data that are close enough to each other give solutions that stay within that tolerance of each other up to that time. "Close" is measured by a **norm**, a number that measures the size of a function (for example its largest value, or the square root of the integral of its square). The third condition is what makes an equation useful for prediction: data are never known exactly, and an equation in which an arbitrarily small error of the data can produce an arbitrarily large error of the solution predicts nothing.

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
&= \big(\partial_1^2 + \partial_2^2 + \partial_3^2 + \partial_0^2 - \partial_4^2 - \partial_5^2 - \partial_6^2 - \partial_7^2\big)\Psi .
\end{aligned}
$$

The first line multiplies out (the gammas are constant matrices); the second separates the terms with $a = b$ from the pairs $a \neq b$, using $\partial_a\partial_b = \partial_b\partial_a$; the third uses $(\gamma^{(a)})^2 = \eta_{aa}I_{16}$ and the anticommutation of different gammas. On the other side, applying the operator to $m\Psi$ gives $m\sum_a\gamma^{(a)}\partial_a\Psi = m^2\Psi$. Solving for the second time derivative:

$$
\partial_4^2\Psi = \big(\partial_1^2 + \partial_2^2 + \partial_3^2 + \partial_0^2 - \partial_5^2 - \partial_6^2 - \partial_7^2 - m^2\big)\Psi .
$$

The three extra-time derivatives enter with the sign of the toy example. This is the root of everything that follows.

**Non-characteristic slices.** In the author's metric the field equation of Section 8.2 can be solved for $\partial_4\Psi$. Write it as $\gamma^{(4)}\partial_4\Psi + R + v_g\gamma^{(4)}\Psi = V\Psi$, where $R$ holds the derivative terms along the seven other directions and the term $c_g\gamma^{(0)}\Psi$, and $V = m + U'(S)$. Multiplying from the left by $\gamma^{(4)}$ and using $(\gamma^{(4)})^2 = -I_{16}$ gives $-\partial_4\Psi + \gamma^{(4)}R - v_g\Psi = \gamma^{(4)}V\Psi$, so

$$
\partial_4\Psi = -\gamma^{(4)}\Big[V\Psi - \sum_{a\neq 4}\frac{1}{f_a}\gamma^{(a)}\partial_a\Psi - c_g\gamma^{(0)}\Psi\Big] - v_g\Psi
$$

(PROVED; `Revision/theory/reports/wolfram-field-theory.json`, check `evolution_form_G`; formula key `evolution_form`). The last term, $-v_g\Psi$, only multiplies the solution by the factor $e^{a_4/2}b_4^{-1}$ as the time goes on (Section 8.30). A slice is called **non-characteristic** when the matrix in front of the time derivative is invertible, as here: the equation then tells how the field changes in time from its values on the slice. This is necessary for a good evolution equation, but not sufficient: the toy example can be solved for $\partial_4^2\varphi$ too. Sections 8.17 and 8.18 show that the field equation fails the third condition of Hadamard: exactly in flat 4+4 space and with frozen coefficients, and, through a standard theorem quoted without proof, in the author's metric itself (Section 8.18 states each status).

### 8.17 Plane waves with frozen coefficients and the mode matrix

**Frozen coefficients.** In the author's metric the frame factors $1/f_a$ change from point to point and in time. Near one point and for a short time one may replace them by their values at that point; this is the method of **frozen coefficients**, a device for studying an equation near one point (labelled MODEL in the notebooks, ASSUMED in the five-label scheme). It does not say that the extra times stop deflating: along the history of the record they deflate, together with the hidden direction, and Section 8.24 follows a wave along that history. In flat 4+4 space the coefficients are constant and nothing is frozen. With frozen coefficients the factors are absorbed into the **frame momenta** $k_a$, and the term $G = c_g\gamma^{(0)} + v_g\gamma^{(4)}$ is left out; it contains no derivative, so it does not change the behaviour of short waves, and it is absent exactly in the field variables $\chi$ of Section 8.30.

**Plane waves.** A **plane wave** is a field $\Psi = u\,e^{i(k_1x_1 + k_2x_2 + k_3x_3 + k_5x_5 + k_6x_6 + k_7x_7 + k_0x_0) - iEx_4}$ with a constant column $u$ of 16 complex numbers. The number $k_a$ is the **momentum** (or wave number) along $x_a$: radians of phase per unit length; $E$ is the **frequency**. Inserting it into $\sum_a\gamma^{(a)}\partial_a\Psi = m\Psi$, line by line:

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
K^2 &= \sum_{a\neq4}k_a^2(\gamma^{(a)})^2 + \sum_{a<b}k_ak_b\big(\gamma^{(a)}\gamma^{(b)} + \gamma^{(b)}\gamma^{(a)}\big) = \big(k_1^2 + k_2^2 + k_3^2 + k_0^2 - k_5^2 - k_6^2 - k_7^2\big)I_{16} .
\end{aligned}
$$

The first line uses $(-1)^2 = 1$ and moves $(im + K)$ past $\gamma^{(4)}$; the second uses $(\gamma^{(4)})^2 = -I_{16}$ and multiplies out (the number $im$ commutes with $K$); the third line computes $K^2$ as in Section 8.16. Hence

$$
h_k^2 = E^2\,I_{16}, \qquad E^2 = m^2 + k_1^2 + k_2^2 + k_3^2 + k_0^2 - k_5^2 - k_6^2 - k_7^2
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

**From frozen coefficients to the author's metric (an ASSUMED step).** In the author's metric the frame factors change from point to point, and a plane wave is not an exact solution of the field equation; so the argument above, by itself, proves nothing about the field equation in that metric. The step is made by a standard theorem of the theory of partial differential equations, the **Lax-Mizohata theorem** (P. D. Lax, 1957; S. Mizohata, 1961), which this book quotes without proof, so it is ASSUMED here. It says: if the initial-value problem of a linear system of first-order equations with smooth coefficients is well posed near a point, then at that point the frequencies of its **principal part** (the derivative terms alone, with their coefficients taken at that point) are real for every real momentum. For the field equation with $U = 0$ (then the equation is linear) the principal part at a point is the mode matrix of Section 8.17 without the mass term, with the frame momenta of that point: a wave with the coordinate momentum $q_a$ along $x_a$ has there the frame momentum $k_a = q_a/f_a$, with the frame factors of that point (the term $G$ contains no derivative, so it does not belong to the principal part). By the formula of Section 8.17 with $m = 0$, its frequencies obey $E^2 = k_1^2 + k_2^2 + k_3^2 + k_0^2 - k_5^2 - k_6^2 - k_7^2$, which is negative for a wave along an extra time alone ($k_5 \neq 0$, all other momenta zero), at every point. So, granted the theorem, the initial-value problem of the field equation in the author's metric is not well posed for data that depend on the extra times. Status: the statements in flat 4+4 space and with frozen coefficients are PROVED, and they are what the Revision record checks; the step to the author's varying coefficients rests on the quoted theorem (ASSUMED) and is not checked by the record; for $U \neq 0$ nothing more is claimed.

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
ETA = gammas_record["eta"]  # [1, 1, 1, 1, -1, -1, -1, -1] in the order x0 ... x7
# B = -i C gamma^(x4) is stored as its real part and its imaginary part.
B = np.array(gammas_record["B"]["re"]) + 1j * np.array(gammas_record["B"]["im"])
I16 = np.eye(16, dtype=int)  # the 16 x 16 unit matrix
say(f"eta = {ETA}; each gamma is a {GAMMA[0].shape[0]} x {GAMMA[0].shape[1]} matrix")
```

The gammas are read from the record and turned into numpy arrays of whole numbers (`dtype=int`), so that the products below are exact. `ETA` is the list of the eight signs. The matrix $B$ is complex; the record stores its real part (`"re"`) and its imaginary part (`"im"`) separately, and the line adds them, `1j` being Python's imaginary unit $i$. `np.eye(16, dtype=int)` is the unit matrix. The `say` line prints the signs and the shape of a gamma (`.shape` gives the number of rows and columns): `eta = [1, 1, 1, 1, -1, -1, -1, -1]; each gamma is a 16 x 16 matrix`.

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
check_record(np.array_equal(GAMMA[4] @ GAMMA[4], -I16),
             "(gamma^(x4))^2 = -1: the slices x4 = const are non-characteristic",
             "Revision/theory/reports/wolfram-field-theory.json", "evolution_form_G",
             "the slices x4 = const are non-characteristic")
```

`B.conj().T` is the conjugate transpose $B^\dagger$; `np.allclose` compares two arrays up to rounding. The first check confirms $B^\dagger = B$ and $B^2 = I_{16}$. The second confirms $(\gamma^{(4)})^2 = -I_{16}$, which is the reason the field equation can be solved for $\partial_4\Psi$ (Section 8.16), together with the Wolfram record's check `evolution_form_G`. Output: the line about `eta` and three PASS lines, two with `reproduces` lines.

**In [3], the mode matrix and its square, exactly.**

```python
m = sp.Symbol("m", real=True)  # the mass
k = {a: sp.Symbol(f"k{a}", real=True) for a in (0, 1, 2, 3, 5, 6, 7)}  # momenta
G = [sp.Matrix(rows) for rows in gammas_record["gamma"]]  # the gammas, exact
B_exact = sp.I * sp.Matrix(gammas_record["B"]["im"])  # B is purely imaginary
g4 = G[4]  # gamma^(x4)
```

The mass and the seven momenta are exact symbols (a dictionary that maps each direction number $a$ to the symbol $k_a$; there is no $k_4$). `G` holds the gammas as exact sympy matrices. The real part of $B$ is zero (because $C\gamma^{(4)}$ is real), so `B_exact` is $i$ times the stored imaginary part. `g4` is $\gamma^{(4)}$.

```python
momentum_part = sp.zeros(16, 16)
for a, k_a in k.items():  # a runs over 0, 1, 2, 3, 5, 6, 7
    momentum_part += k_a * g4 * G[a]  # k_a gamma^(x4) gamma^(xa)
h = -sp.I * m * g4 - momentum_part  # the mode matrix h_k
E2 = m**2 + k[0]**2 + k[1]**2 + k[2]**2 + k[3]**2 - k[5]**2 - k[6]**2 - k[7]**2
say(f"E^2 = {E2}")
```

`k.items()` gives the pairs (direction, symbol); `G[a]` is the gamma of direction $x_a$ (lists count from 0, like the coordinates). The loop adds up $\sum_{a\neq4}k_a\gamma^{(4)}\gamma^{(a)}$, and `h` is the mode matrix $h_k = -im\gamma^{(4)} - \gamma^{(4)}\sum_ak_a\gamma^{(a)}$ of Section 8.17 (`sp.I` is the exact $i$). `E2` is the expected $E^2$; it is printed in sympy's order: `E^2 = k1**2 + k2**2 + k3**2 - k5**2 - k6**2 - k7**2 + k8**2 + m**2`.

```python
square_minus_E2 = (h * h - E2 * sp.eye(16)).applyfunc(sp.expand)
square_ok = square_minus_E2 == sp.zeros(16, 16)
# The two independent Revision verifiers print E^2 in their own notations: sympy
# writes powers with **, the Wolfram verifier with ^. Both texts must hold this E^2.
E2_sympy_text = sp.sstr(E2)  # "k0**2 + k1**2 + ... + m**2"
E2_wolfram_text = E2_sympy_text.replace("**", "^")  # "k0^2 + k1^2 + ... + m^2"
```

The matrix $h_k^2 - E^2I_{16}$ is computed and every entry multiplied out (`sp.expand`); `square_ok` is true when all 256 entries are exactly zero. The two texts are $E^2$ as the sympy record writes it and as the Wolfram record writes it (`replace` swaps `**` for `^`).

```python
check_record(square_ok,
             "h_k^2 = E^2 I16, E^2 = m^2 + k0^2 + k1^2 + k2^2 + k3^2 - k5^2 - k6^2 "
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
extra_time_part = -(k[5] * g4 * G[5] + k[6] * g4 * G[6] + k[7] * g4 * G[7])
check((anti - extra_time_part).applyfunc(sp.expand) == sp.zeros(16, 16),
      "the anti-Hermitian part of h_k is the extra-time part")
anti_square = (anti * anti).applyfunc(sp.expand)
check(anti_square == (-(k[5]**2 + k[6]**2 + k[7]**2) * sp.eye(16)).applyfunc(
    sp.expand), "its square is -(k5^2 + k6^2 + k7^2) I16")
```

Every matrix is the sum of its Hermitian part $(h + h^\dagger)/2$ and its anti-Hermitian part $(h - h^\dagger)/2$. The first check shows that the anti-Hermitian part is exactly the extra-time part $-\gamma^{(4)}(k_5\gamma^{(5)} + k_6\gamma^{(6)} + k_7\gamma^{(7)})$ (Section 8.17). The second shows that its square is $-(k_5^2 + k_6^2 + k_7^2)I_{16}$; a matrix whose square is a negative number times $I_{16}$ is the zero matrix only when that number is zero, so $h_k$ is Hermitian exactly when there is no extra-time momentum. Output: two PASS lines.

**In [5], the exact example $m = 1$, $k_5 = 2$.**

```python
sample = {m: 1, k[5]: 2, k[0]: 0, k[1]: 0, k[2]: 0, k[3]: 0, k[6]: 0, k[7]: 0}
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
    g4n = GAMMA[4]
    result = -1j * mass * g4n.astype(complex)
    for a, k_a in momenta.items():  # a is the direction: GAMMA[a] is gamma^(xa)
        result = result - k_a * (g4n @ GAMMA[a])
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
             "(0, 0, 0, 0, 2, 0, 0): w^2 = -3, eigenspace dimensions "
             f"[{V_grow.shape[1]}, {V_grow.shape[1]}], B-form identically zero: True")
```

The eigenspace of the growing frequency $+i\sqrt3$ ($m = 1$, $k_5 = 2$) has 8 basis columns. The $8 \times 8$ matrix `form_grow` holds every value $v^\dagger Bu$ for two basis columns; the check requires dimension 8 and all 64 values below $10^{-12}$ (the Krein-neutrality of Section 8.19), and the pairing record's text for the same sample (it lists the momenta in the order $k_1, k_2, k_3, k_5, k_6, k_7, k_0$ and calls the frequency $w$).

```python
V_real = eigenspace(mode_matrix(1.0, {0: 2.0, 1: 2.0}), 3.0)
form_real = np.linalg.eigvalsh(V_real.conj().T @ B @ V_real)  # Hermitian 8 x 8
inertia = (int(np.sum(form_real > 1e-9)), int(np.sum(form_real < -1e-9)))
report("Krein inertia of the eigenspace of E = 3 (m = 1, k0 = k1 = 2)", inertia)
check_record(V_real.shape[1] == 8 and inertia == (4, 4),
             "m = 1, k0 = k1 = 2: the eigenspace of E = 3 has Krein inertia (4, 4)",
             "Revision/pairing/reports/python-pairing.json",
             "Q.one_particle_Krein_inertia",
             f"w = 3: dim {V_real.shape[1]}, Krein inertia ({inertia[0]},{inertia[1]})")
```

For the good-sector wave $m = 1$, $k_1 = k_0 = 2$ ($E^2 = 1 + 4 + 4 = 9$) the eigenspace of $E = 3$ is found; the Krein form restricted to it is a Hermitian $8 \times 8$ matrix, whose eigenvalues `np.linalg.eigvalsh` computes. Counting the positive and the negative ones gives the inertia, printed as `(4, 4)`; the check also requires the pairing record's text.

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
good = mode_matrix(1.3, {0: 2.2, 1: 0.4, 2: -1.1, 3: 0.7})  # no k5, k6, k7
good_eigenvalues = np.linalg.eigvals(good)
E_good = np.sqrt(1.3**2 + 0.4**2 + 1.1**2 + 0.7**2 + 2.2**2)
check_record(np.allclose(good, good.conj().T) and np.allclose(good @ B, B @ good)
             and np.max(np.abs(np.abs(good_eigenvalues) - E_good)) < 1e-12
             and np.max(np.abs(good_eigenvalues.imag)) < 1e-12,
             "good sector: h_k Hermitian, [B, h_k] = 0, eigenvalues real +-E",
             "Revision/theory/reports/python-field-theory.json",
             "good_sector_spectrum_and_B_sectors", "h is Hermitian", "[B, h] = 0")
```

A good-sector mode matrix with $m = 1.3$ and four space momenta (no extra-time momentum). The check requires: $h_k$ Hermitian, commuting with $B$, every eigenvalue of size $E = \sqrt{m^2 + k_1^2 + k_2^2 + k_3^2 + k_0^2}$ and with imaginary part below $10^{-12}$, so the eigenvalues are $\pm E$, real; and the record's texts.

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

### 8.24 The deflating history pushes extra-time waves into growth

Sections 8.17 to 8.19 froze the coefficients. In the author's metric they are not frozen: the hidden direction and the extra times deflate together, and this changes the momenta that a wave has along them. This section follows the change exactly.

**The hidden coordinate $y$.** A second way to label the points of the hidden direction, on each half of a cell, is $y = \ln|\sin z|/(6H) = \ln(\sin^2 z)/(12H)$. At the fold $z = \pi/2$, $|\sin z| = 1$ and $y = 0$; towards a tip, $\sin z \to 0$ and $y \to -\infty$. Two facts make $y$ useful, each derived in one line. First, $|\sin z| = e^{6Hy}$ (undo the logarithm), so $(\sin^2 z)^{1/12} = e^{Hy}$ and $(\sin^2 z)^{1/6} = e^{2Hy}$. Second, $dy/dx_0 = \frac{1}{12H}\cdot\frac{2\sin z\cos z\cdot 6H}{\sin^2 z} = \cot z$ (chain rule with $dz/dx_0 = 6H$), so $\cot^2 z\,dx_0^2 = dy^2$. The author's corrected metric therefore reads

$$
ds^2 = e^{2a_4}(dx_1^2 + dx_2^2 + dx_3^2) - dx_4^2 + e^{-2a_4}b_4\big(dy^2 - e^{2Hy}(dx_5^2 + dx_6^2 + dx_7^2)\big) :
$$

the hidden direction and the three extra times form one block with the common factor $e^{-2a_4}b_4$, a space of constant curvature $-H^2$ (`Revision/SPEC.md`, section 1), and a step $dy$ has the proper length $e^{-a_4}b_4^{1/2}|dy|$. The Kohn-Sham record cuts the tip at $y = -L$ with $L = 3$ (`Revision/kohn_sham/results/parameters.json`, entry `physics.L_tipCutoff`).

**The history.** The examples use the history $a_4 = AHx_4$, $b_4 = b_4(0)e^{\beta AHx_4}$ with $A = 1$, $\beta = \frac43$, $b_4(0) = 1$ and $H = m = 1$, the canonical history of the Kohn-Sham record (`parameters.json`, entries `physics.historyA`, `physics.historyBeta`, `physics.historyB4AtZero`, `physics.H`, `physics.m`). It is ASSUMED: the record calls it a PRESCRIBED BACKGROUND, chosen and not solved for. It needs a diagonal source with equal hidden and extra-time pressures that grows with the time, and the Kohn-Sham states along it do not satisfy the source conditions of the $a_4$ and $b_4$ equations (Chapters 12 and 17). Along it the 3-space scale factor $e^{a_4}$ grows like $e^{AHx_4}$, and the factor of the hidden block shrinks like $e^{-\delta x_4}$, with the **deflation rate** $\delta = (1 - \frac\beta2)AH = \frac{AH}{3}$, because $e^{-a_4}b_4^{1/2} = e^{-AHx_4 + \frac\beta2AHx_4}$. The 7-volume factor $\sqrt{|g|} = e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}$ grows like $e^{-a_4}b_4^2 = e^{(2\beta - 1)AHx_4} = e^{5AHx_4/3}$.

**Wave numbers that do not change.** The coefficients of the field equation in the author's metric do not depend on $x_1, x_2, x_3, x_5, x_6, x_7$. So a field of the form $\Psi = e^{i(q_1x_1 + q_5x_5)}\psi(x_4, y)$ keeps this form for all times: every derivative $\partial_1$ or $\partial_5$ acting on it gives the factor $iq_1$ or $iq_5$, the common exponential divides out, and the equation for $\psi$ contains neither $x_1$ nor $x_5$. The numbers $q_1$ and $q_5$ are **coordinate wave numbers**: radians of phase per unit of the coordinate. They are exact constants of the motion. Along $y$ the coefficients change (through $e^{Hy}$), so there a wave $e^{iq_yy}$ with a **local wave number** $q_y$ is a notion with frozen coefficients in $y$ only. In the coordinate $x_0$ the same local wave is $e^{ik_{x_0}x_0}$ with $k_{x_0} = q_y\,dy/dx_0 = q_y\cot z$, so $q_y = \tan z\,k_{x_0}$.

**Frame momenta that do change.** A frame momentum counts radians per unit of PROPER length; a coordinate length $\Delta x_a$ has the proper length $f_a\Delta x_a$, so $k_{(a)} = q_a/f_a$. Line by line:

1. $k_{(1)} = q_1/f_1 = q_1e^{-a_4}$, because $f_1 = e^{a_4}$ (3-space carries no factor of $y$);
2. $k_{(5)} = q_5/f_5 = q_5e^{a_4}b_4^{-1/2}e^{-Hy}$, because $f_5 = e^{-a_4}b_4^{1/2}(\sin^2 z)^{1/12} = e^{-a_4}b_4^{1/2}e^{Hy}$; on the history $k_{(5)} = q_5e^{\delta x_4}e^{-Hy}$;
3. $k_{(0)} = q_ye^{a_4}b_4^{-1/2}$, because a step $dy$ has the proper length $e^{-a_4}b_4^{1/2}|dy|$; on the history $k_{(0)} = q_ye^{\delta x_4}$: the hidden frame momentum grows at the same rate as $k_{(5)}$;
4. with frozen coefficients at the time $x_4$ (Section 8.17), $E^2 = m^2 + k_{(1)}^2 + k_{(0)}^2 - k_{(5)}^2 = m^2 + q_1^2e^{-2a_4} - D\,\frac{e^{2a_4}}{b_4}$, with $D = q_5^2e^{-2Hy} - q_y^2$.

The fourth line inserts the first three and collects the two terms with $e^{2a_4}/b_4$. In the coordinate wave numbers of the author, $q_5 = k_{x_5}$, $e^{-2Hy} = (\sin^2 z)^{-1/6}$ and $q_y = \tan z\,k_{x_0}$, so

$$
D = (\sin^2 z)^{-1/6}\,k_{x_5}^2 - \tan^2 z\,k_{x_0}^2 .
$$

As the block deflates ($a_4 - \frac12\ln b_4$ grows), a fixed number of wiggles per unit of $x_5$ means more and more wiggles per unit of proper length: the frame momentum $k_{(5)}$ grows like $e^{a_4}b_4^{-1/2}$ (like $e^{\delta x_4}$ on the history), and so does $k_{(0)}$, while $k_{(1)}$ shrinks like $e^{-a_4}$ because 3-space inflates (PROVED; the dark-sector record of the corrected metric states the same mass shell and the equal rates $d\ln k_{(5)}/da_4 = d\ln k_{(0)}/da_4 = 1 - \beta/2$: `Revision/dark_sector/dirac16complex/reports/derivation-checks.json`, checks `flat_mode_mass_shell` and `extra_time_momentum_blueshift`).

**Which waves start to grow.** As the time goes on, the last term of $E^2$ grows like $e^{2\delta x_4}$ and the middle one decays like $e^{-2AHx_4}$. If $D > 0$, $E^2$ must turn negative; if $D \le 0$, $E^2 \ge m^2$ at every time and the wave never grows. On the history write $X = e^{2\delta x_4}$. Then $e^{2a_4}/b_4 = X$ and, since $2AH = 3\cdot2\delta$, $e^{-2a_4} = e^{-2AHx_4} = X^{-3}$; so $E^2 = m^2 + q_1^2/X^3 - DX$. For $D > 0$ it decreases as a function of $X > 0$ (its derivative $-3q_1^2/X^4 - D$ is negative), so along the history (where $X$ grows with the time) $E^2$ crosses zero exactly once and stays negative afterwards; the moment of the crossing is the **onset**. To find it, line by line:

$$
\begin{aligned}
0 &= m^2 + \frac{q_1^2}{X^3} - DX, \\
0 &= DX^4 - m^2X^3 - q_1^2, \\
x_4^\ast &= \frac{\ln X^\ast}{2\delta} .
\end{aligned}
$$

The first line sets $E^2 = 0$; the second multiplies by $-X^3$ (allowed, $X > 0$). This equation of degree four has exactly one positive root $X^\ast$: its coefficients $D, -m^2, 0, 0, -q_1^2$ change sign once, so by **Descartes' rule of signs** (the number of positive roots is at most the number of sign changes of the coefficients, and differs from it by an even number) there is exactly one. Notebook 08b finds the root with numpy's root finder for polynomials and compares it with a search by halving intervals. The third line undoes $X = e^{2\delta x_4}$. For a wave without space momentum, $q_1 = 0$, the second line gives $X^\ast = m^2/D$ and $x_4^\ast = \frac{1}{2\delta}\ln\frac{m^2}{D}$; without hidden momentum as well, $D = q_5^2e^{-2Hy}$ and the onset time simplifies to

$$
x_4^\ast = \frac{\ln(m/q_5) + Hy}{\delta} = \frac{3\big(Hy + \ln(m/q_5)\big)}{AH} .
$$

At $y = 0$ with $A = H = m = 1$ this is $3\ln(1/q_5)$: $x_4^\ast = 3\ln 20 = 8.987197$ for $q_5 = 0.05$ and $3\ln 10 = 6.907755$ for $q_5 = 0.1$ (Notebook 08b prints both). With the hidden momentum $q_y = 0.05$ the wave $q_5 = 0.1$ has $D = 0.0075$ and $x_4^\ast = \frac32\ln(1/0.0075) = 7.339278$: a hidden momentum delays the onset, and once $q_y^2 \ge q_5^2e^{-2Hy}$ it prevents it.

**The statement, with its condition.** Every wave with $D > 0$ reaches the onset at a finite time, and after the onset its growth rate $\kappa = \sqrt{k_{(5)}^2 - m^2 - k_{(1)}^2 - k_{(0)}^2} = \sqrt{De^{2\delta x_4} - m^2 - q_1^2e^{-2AHx_4}}$ keeps increasing without bound. In particular every wave along an extra time WITHOUT hidden momentum ($q_y = 0$, so $D = q_5^2e^{-2Hy} > 0$) eventually starts to grow, and a smaller $q_5$ only delays the onset, logarithmically. A wave whose hidden momentum outweighs its extra-time momentum ($D \le 0$) never grows. (PROVED with frozen coefficients at each instant. The Revision record states the local-frame statement as "every extra-time mode eventually enters the growing regime", `Revision/theory/reports/python-field-theory.json`, check `extra_time_modes_grow`; its argument follows the extra-time frame momentum alone, so the sentence holds exactly for the waves with $D > 0$, which include all waves without hidden momentum. In the withdrawn metric of 2026-10-14 the hidden direction did not deflate, and there the sentence held for every extra-time wave.) For any history the same holds whenever $a_4 - \frac12\ln b_4$ grows without bound. Restricting the theory to the good sector, the fields that do not depend on the extra times, removes this growth; it is a choice, not a consequence of the equations, and Section 8.32 shows that the good sector has growing modes of its own unless a boundary condition is imposed at the fold.

### 8.25 Following one wave through the onset: the local-frame model and WKB

**The local-frame model (labelled MODEL; ASSUMED).** The field also depends on $y$, and the factor $e^{-Hy}$ in $k_{(5)}$ makes the exact equation couple neighbouring values of $y$. The **local-frame model** holds the hidden position fixed (it freezes the coefficients in $y$ only), works in the variables $\chi$ of Section 8.30 (in which the term $G$ is absent exactly), takes no momentum along the hidden direction, and keeps the exact time dependence of the frame momenta:

$$
i\,\frac{du}{dx_4} = h(x_4)\,u, \qquad h(x_4) = -im\gamma^{(4)} - \gamma^{(4)}\big(k_{(1)}(x_4)\gamma^{(1)} + k_{(5)}(x_4)\gamma^{(5)}\big).
$$

Its solutions are not exact solutions of the field equation; they show how a wave behaves near one hidden position as the block deflates. The position enters only through $q_5e^{-Hy}$, so the runs use $y = 0$. At every instant $h(x_4)^2 = E^2(x_4)I_{16}$ with the $E^2$ of Section 8.24 (Section 8.17 with the frame momenta of that instant).

**A clean starting column.** Take $q_1 = 0$. The matrix $C = \gamma^{(0)}\gamma^{(1)}\gamma^{(2)}\gamma^{(3)}$ commutes with $\gamma^{(4)}$ and with $\gamma^{(5)}$ (moving either of them through the four factors of $C$ changes the sign four times), hence with $h(x_4)$. A column $u$ can therefore be an eigenvector of $h(0)$ for the positive frequency $E_0 = \sqrt{m^2 - q_5^2}$ and at the same time of $C$ for the eigenvalue $\sigma = +1$ or $-1$ ($C$ is real, symmetric, and $C^2 = I_{16}$). For such a column of size $u^\dagger u = 1$ the Krein form is $u^\dagger Bu = \sigma E_0/m$. Line by line:

1. $B = -iC\gamma^{(4)} = C(-i\gamma^{(4)})$, and since $C$ is Hermitian with $Cu = \sigma u$, $u^\dagger C = \sigma u^\dagger$; so $u^\dagger Bu = \sigma\,u^\dagger(-i\gamma^{(4)})u$.
2. $E_0 = E_0u^\dagger u = u^\dagger h(0)u = m\,u^\dagger(-i\gamma^{(4)})u - q_5\,u^\dagger\gamma^{(4)}\gamma^{(5)}u$ (at $x_4 = 0$, $a_4 = 0$ and $b_4 = b_4(0) = 1$, so $k_{(5)} = q_5$ at $y = 0$).
3. $-i\gamma^{(4)}$ is Hermitian, so $u^\dagger(-i\gamma^{(4)})u$ is real; $\gamma^{(4)}\gamma^{(5)}$ is real and antisymmetric, so $u^\dagger\gamma^{(4)}\gamma^{(5)}u$ is purely imaginary (its complex conjugate is $u^T\gamma^{(4)}\gamma^{(5)}u^\ast = u^\dagger(\gamma^{(4)}\gamma^{(5)})^Tu = -u^\dagger\gamma^{(4)}\gamma^{(5)}u$, a number being equal to its own transpose).
4. $E_0$ is real, so the imaginary term vanishes, $u^\dagger(-i\gamma^{(4)})u = E_0/m$, and by line 1, $u^\dagger Bu = \sigma E_0/m$.

The notebook builds such columns with two **projectors** (matrices $P$ with $P^2 = P$): $\Lambda_+ = \frac12(I_{16} + h(0)/E_0)$ keeps the part of a column with eigenvalue $+E_0$, and $\frac12(I_{16} + \sigma C)$ the part with $C = \sigma$; they commute, so their product applied to the first unit column gives a column with both properties.

**The leading WKB approximation.** After the onset write $Q = k_{(5)} = q_5e^{\delta x_4}$ (at $y = 0$) and $\kappa = \sqrt{Q^2 - m^2}$. When $\kappa$ changes slowly, the wave follows the growing eigenvalue of $-ih$ at each instant; this is the **WKB approximation** (after Wentzel, Kramers and Brillouin). Line by line:

1. At each instant the growing eigenvalue of $-ih$ is $+\kappa$, so the size grows at the rate $\frac{d}{dx_4}\ln(u^\dagger u) \approx 2\kappa$, and $\ln(u^\dagger u) \approx 2W + $ const with $W(x_4) = \int\kappa\,dx_4$.
2. Since $dQ/dx_4 = \delta Q$, the substitution $dx_4 = dQ/(\delta Q)$ gives $W = \frac{1}{\delta}\int\frac{\sqrt{Q^2 - m^2}}{Q}\,dQ$.
3. This integral is $W = \frac{1}{\delta}\big(\sqrt{Q^2 - m^2} - m\arccos\frac mQ\big)$. To check it, differentiate the bracket with respect to $Q$: $\frac{d}{dQ}\sqrt{Q^2 - m^2} = \frac{Q}{\kappa}$, and $\frac{d}{dQ}\arccos\frac mQ = -\frac{1}{\sqrt{1 - m^2/Q^2}}\cdot\big(-\frac{m}{Q^2}\big) = \frac{m}{Q\kappa}$; so the derivative of the bracket is $\frac{Q}{\kappa} - \frac{m^2}{Q\kappa} = \frac{Q^2 - m^2}{Q\kappa} = \frac{\kappa}{Q}$, the integrand.

**The first-order WKB correction.** The matrices $A_4 = -i\gamma^{(4)}$ and $N = -i\gamma^{(4)}\gamma^{(5)}$ are Hermitian, square to $I_{16}$ ($(-i\gamma^{(4)})^2 = -(\gamma^{(4)})^2 = I_{16}$; $(\gamma^{(4)}\gamma^{(5)})^2 = -(\gamma^{(4)})^2(\gamma^{(5)})^2 = -I_{16}$, so $N^2 = I_{16}$) and anticommute, and with $q_1 = 0$, $h = mA_4 - iQN$. Line by line:

1. Take a column $w$ with $A_4w = w$; then $A_4(Nw) = -NA_4w = -Nw$, and $h$ maps the plane spanned by $w$ and $Nw$ into itself: $hw = mw - iQNw$ and $h(Nw) = -mNw - iQw$. For $u = v_1w + v_2Nw$ the equation $du/dx_4 = -ihu$ becomes $v' = \begin{pmatrix}-im & -Q \\ -Q & im\end{pmatrix}v$ (there are 8 such planes).
2. This symmetric $2 \times 2$ matrix has the eigenvalues $\pm\kappa$ (its determinant condition is $(-im - \lambda)(im - \lambda) - Q^2 = \lambda^2 + m^2 - Q^2 = 0$) and, for $+\kappa$, the eigenvector $r = (Q, -\kappa - im)$ (the first row gives $(-im - \kappa)Q - Q(-\kappa - im) = 0$).
3. Keep only the growing part, $v \approx c\,r$. Then $v' = c'r + cr' \approx \kappa cr$; multiplying from the left by the row $r^T$ and writing $n = r^Tr$ gives $c'n + c\,r^Tr' = \kappa cn$, and $r^Tr' = n'/2$ (the derivative of $r^Tr$ is $2r^Tr'$ for a symmetric product). So $c'/c = \kappa - n'/(2n)$.
4. $n = Q^2 + (\kappa + im)^2 = Q^2 + \kappa^2 - m^2 + 2im\kappa = 2\kappa(\kappa + im)$, using $Q^2 - m^2 = \kappa^2$; its size is $|n| = 2\kappa\sqrt{\kappa^2 + m^2} = 2\kappa Q$.
5. Integrating line 3, $\ln c = W - \frac12\ln n + $ const, so $|c|^2 \propto e^{2W}/|n| = e^{2W}/(2\kappa Q)$. The size of the column is $|c|^2r^\dagger r = |c|^2(Q^2 + \kappa^2 + m^2) = |c|^2\cdot 2Q^2$, so $u^\dagger u \propto e^{2W}Q/\kappa$, and
$$
\ln(u^\dagger u) \approx 2W + \ln\frac{Q}{\kappa} + \text{const}, \qquad \frac{d}{dx_4}\ln(u^\dagger u) \approx 2\kappa - \frac{\delta\,m^2}{\kappa^2},
$$
because $\frac{d}{dx_4}\ln Q = \delta$ and $\frac{d}{dx_4}\ln\kappa = \frac{Q}{\kappa^2}\frac{dQ}{dx_4} = \delta\frac{Q^2}{\kappa^2}$, whose difference is $\delta\frac{\kappa^2 - Q^2}{\kappa^2} = -\frac{\delta m^2}{\kappa^2}$.

**What the computation shows (COMPUTED).** Both approximations fail at the onset itself, where $\kappa \to 0$, so Notebook 08b compares increases over a window from $1.5/\delta = 4.5$ to $3/\delta = 9$ time units after the onset (the unknown constants drop out of increases). For $q_5 = 0.05$ the RK4 solution of the model increases $\ln(u^\dagger u)$ by 93.0724 over the window; the leading WKB formula gives 93.0985 (relative difference $2.81 \times 10^{-4}$) and the first-order formula 93.0742 (relative difference $1.97 \times 10^{-5}$); for $q_5 = 0.1$ the numbers are 93.0714, 93.0975 and 93.0732. Late in the run the growth rate computed from the solution is 40.11371 and the first-order prediction 40.11373 (relative agreement better than $10^{-5}$). The RK4 solution itself is accurate to $10^{-8}$ (relative), and halving the step divides its error by 15.89, close to the value 16 of a fourth-order method. Before the onset the size does not stay exactly 1: with extra-time momentum the mode matrix is not Hermitian, so the Hilbert norm is not conserved (Section 8.19), and the size $u^\dagger u$, which starts at 1, has grown to 2.00 ($q_5 = 0.05$) and 1.99 ($q_5 = 0.1$) when the onset is reached. Nine time units after the onset $\ln(u^\dagger u) = 111.245745$ for $q_5 = 0.05$, that is $u^\dagger u \approx 2.06 \times 10^{48}$, while the Krein form stays constant to rounding (its change divided by $\max(u^\dagger u, 1)$ stays below $10^{-9}$). Because the rate $2\kappa \approx 2q_5e^{\delta x_4}$ itself grows exponentially, the growth is faster than any exponential. These numbers are the same as in the withdrawn metric of 2026-10-14, because along the history the extra-time frame momentum grows at the same rate $\delta = AH/3$ in both metrics and the model takes no hidden momentum.

### 8.26 Example: the onset of growth along the deflating history

Notebook 08b puts Sections 8.24 and 8.25 to work along the prescribed history of the Kohn-Sham record. It reads $A$, $\beta$, $b_4(0)$, $H$, $m$ and $L$ from the record and computes the deflation rate $\delta = AH/3$; checks exactly that $dy/dx_0 = \cot z$, $e^{Hy} = (\sin^2 z)^{1/12}$ and that the product of the eight scale factors is $e^{-a_4}b_4^2\cot z\,(\sin^2 z)^{1/4}$ for all values of $a_4$ and $b_4$; draws the scale factors and the 7-volume along the history; computes the three frame momenta and the exact onset time and compares it with a numerical root search; reproduces the mass shell and the equal growth rates of the dark-sector record; shows that the onset time is finite for every $q_5 > 0$ without hidden momentum and that a wave reaches the onset exactly when $D > 0$; builds the model's mode matrix, checks $h(x_4)^2 = E^2(x_4)I_{16}$ against the record's formula, chooses clean starting columns, follows two waves through the onset with RK4 (with a convergence test), and compares with both WKB formulas; and checks the Krein form. It needs no Rust and runs in well under a minute; the times measured on the build computer, which depend on how busy that computer is, are recorded in the notebook's provenance file `Revision/textbook/notebooks/08b_deflation_onset.PROVENANCE.md`. It ends with the line ALL 29 CHECKS PASSED (notebook 08b).

<!-- NOTEBOOK 08b -->

### 8.29 Line-by-line walk-through of Notebook 08b

The notebook has 12 code cells, In [1] to In [12]. The conventions are those of Section 8.15; captions shortened to `...)` are printed in full in Section 8.28.

**In [1], the set-up cell.** It is the set-up cell explained in Section 8.15, with the line `NOTEBOOK_ID = "08b"  # this notebook: chapter 08, example b`; its comment lines are the run instructions of Section 8.27. Output: `Set-up of notebook 08b complete: repository folder found, helpers defined.`

**In [2], the record helpers and the history of the Kohn-Sham record.**

```python
import numpy as np  # arrays of numbers, matrices, linear algebra
import sympy as sp  # exact algebra with symbols

REPORTS = {}  # report file -> {check name: (verdict, detail)}, each read once
```

The imports of numpy and sympy and the empty table `REPORTS`, as in Notebook 08c (Section 8.15).

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


def check_record(condition, title, report_file, check_name, *pieces):
    """check() for a result that reproduces the Revision check check_name: it passes
    only if condition is true AND the report records check_name as passed, with
    every piece of text (values computed here) in its detail."""
    on_record = record_says(report_file, check_name, *pieces)
    check(condition and on_record, title,
          record=f"{report_file}, check {check_name}")
```

The two record helpers. `record_says` is word for word that of Notebook 08c; `check_record` is the simpler form that takes exactly one check name: it passes only if the notebook's own computation (`condition`) is true and the report records `check_name` as passed with every given piece of text in its detail, and it prints the line `reproduces <report>, check <name>`.

```python
parameters = json.loads(repository_file(
    "Revision/kohn_sham/results/parameters.json").read_text(encoding="utf-8"))
H = parameters["physics"]["H"]  # the author's constant H
mass = parameters["physics"]["m"]  # the mass m
A = parameters["physics"]["historyA"]  # the history a4 = A H x4
beta = parameters["physics"]["historyBeta"]  # and b4 = b4(0) e^(beta A H x4)
b4_zero = parameters["physics"]["historyB4AtZero"]  # b4(0)
L_tip = parameters["physics"]["L_tipCutoff"]  # the record cuts the tip at y = -L
say("history: " + parameters["theoryInputs"]["adiabaticityHistory"])
say("status: " + parameters["conventions"]["history"].split(". ")[0] + ".")
```

The cell reads the parameters of the Kohn-Sham record, `Revision/kohn_sham/results/parameters.json`, and takes from its section `physics` the constant $H$, the mass $m$ (called `mass`, because the short name `m` is used for other things in some notebooks), the history constants $A$, $\beta$ and $b_4(0)$, and the tip cutoff $L$. The two `say` lines print how the record describes the history and the first sentence of its status (`split(". ")[0]` cuts the text at the first full stop followed by a blank).

```python
check(H == 1.0 and mass == 1.0 and A == 1.0 and sp.nsimplify(beta) == sp.Rational(4, 3)
      and b4_zero == 1.0 and L_tip == 3.0,
      "the canonical history: A = 1, beta = 4/3, b4(0) = 1, H = 1, m = 1, L = 3",
      record="Revision/kohn_sham/results/parameters.json, physics.historyA, "
             "physics.historyBeta, physics.historyB4AtZero, physics.H, physics.m, "
             "physics.L_tipCutoff")
```

The check confirms the values $H = m = A = 1$, $\beta = \frac43$ (compared exactly after `sp.nsimplify` turns the stored $1.333333333333333$ into $\frac43$), $b_4(0) = 1$ and $L = 3$, and names the record entries it reproduces.

```python
def a4_of(x4):
    """The prescribed deflating history a4 = A H x4."""
    return A * H * x4


def b4_of(x4):
    """The prescribed history b4 = b4(0) e^(beta A H x4)."""
    return b4_zero * np.exp(beta * A * H * x4)
```

The history as two Python functions of the time: $a_4 = AHx_4$ and $b_4 = b_4(0)e^{\beta AHx_4}$ (`np.exp` works for single numbers and for whole arrays of times).

```python
delta = (1 - beta / 2) * A * H  # the deflation rate: e^(-a4) b4^(1/2) = e^(-delta x4)
report("deflation rate delta = (1 - beta/2) A H", f"{delta:.12f}")
check(abs(delta - 1 / 3) < 1e-15 and abs(A * H / delta - 3) < 1e-14,
      "the hidden block shrinks like e^(-x4/3) on the history: delta = A H/3")
```

The deflation rate $\delta = (1 - \beta/2)AH$ of Section 8.24 is computed and printed with twelve decimals; the check confirms $\delta = \frac13$ and $AH/\delta = 3$ to rounding. Output of the cell:

```text
history: a4 = A H x4 (A = 1 canonical), b4 = b4(0) e^{beta A H x4} (beta = 4/3, b4(0) =
    1), a4' = A H, b4'/b4 = beta A H, f = e^{(beta/2 - 1) a4} = e^{-a4/3}; slices a4,0 =
    a4(x4), b4,0 = e^{beta a4,0}; PRESCRIBED BACKGROUND (see historyStatus)
status: PRESCRIBED BACKGROUND: the history a4 = H x4, b4 = e^{(4/3) H x4} is prescribed,
    not solved for.
PASS the canonical history: A = 1, beta = 4/3, b4(0) = 1, H = 1, m = 1, L = 3
     reproduces Revision/kohn_sham/results/parameters.json, physics.historyA,
    physics.historyBeta, physics.historyB4AtZero, physics.H, physics.m,
    physics.L_tipCutoff
RESULT deflation rate delta = (1 - beta/2) A H = 0.333333333333
PASS the hidden block shrinks like e^(-x4/3) on the history: delta = A H/3
```

**In [3], the scale factors and the volume.**

```python
x0, H_symbol = sp.symbols("x0 H", positive=True)
a4_symbol = sp.Symbol("a4", real=True)
b4_symbol = sp.Symbol("b4", positive=True)  # the second function of the metric
z = 6 * H_symbol * x0
y_of_x0 = sp.log(sp.sin(z) ** 2) / (12 * H_symbol)  # y = ln|sin z|/(6 H)
check(sp.simplify(sp.diff(y_of_x0, x0) - sp.cot(z)) == 0, "dy/dx0 = cot z")
twelfth = (sp.sin(z) ** 2) ** sp.Rational(1, 12)  # (sin^2 z)^(1/12)
check(sp.simplify(sp.exp(H_symbol * y_of_x0) - twelfth) == 0,
      "e^(H y) = (sin^2 z)^(1/12)")
```

Exact symbols: $x_0$ and $H$ positive, $a_4$ real and $b_4$ positive (here plain symbols, because only their values at one time matter). `y_of_x0` is $y = \ln(\sin^2 z)/(12H)$, which equals $\ln|\sin z|/(6H)$ and is defined for every real $z$ with $\sin z \neq 0$. The first check proves $dy/dx_0 = \cot z$, the second $e^{Hy} = (\sin^2 z)^{1/12}$ (`twelfth` is the warp factor written out).

```python
s_b = sp.exp(-a4_symbol) * sp.sqrt(b4_symbol)  # the factor of the hidden block
factors = ([s_b * sp.cot(z)] + [sp.exp(a4_symbol)] * 3 + [sp.Integer(1)]
           + [s_b * twelfth] * 3)  # f_0, ..., f_7 of the diagonal frame
volume = sp.prod(factors)  # f_0 f_1 ... f_7 (it has the sign of cot z)
expected = sp.exp(-a4_symbol) * b4_symbol**2 * sp.cot(z) * (sp.sin(z) ** 2) ** (
    sp.Rational(1, 4))
check_record(sp.simplify(volume - expected) == 0,
             "f0 f1 ... f7 = e^(-a4) b4^2 cot z (sin^2 z)^(1/4): sqrt|g| = its size",
             "Revision/theory/reports/python-field-theory.json", "sqrt_det_g",
             "e^-a4 b4^2 |cot z| (sin^2 z)^(1/4)")
```

`factors` is the list of the eight scale factors of Section 8.2, with $s_b = e^{-a_4}b_4^{1/2}$, and `volume` their product. The check proves that the product is $e^{-a_4}b_4^2\cot z\,(\sin^2 z)^{1/4}$, whose size is the volume factor $\sqrt{|g|}$, as the record's check `sqrt_det_g` states.

```python
times = np.linspace(0.0, 6.0, 601)
hidden_scale = np.exp(-a4_of(times)) * np.sqrt(b4_of(times))  # e^(-a4) b4^(1/2)
fig, ax = plt.subplots()
ax.plot(times, np.exp(a4_of(times)), color="tab:blue",
        label="3-space $e^{a_4}$ (every $y$)")
ax.plot(times, hidden_scale, color="tab:green", linewidth=2.5, alpha=0.5,
        label="hidden direction $e^{-a_4}b_4^{1/2}$ (per unit of $y$)")
```

For the figure: 601 times from 0 to 6, the factor $e^{-a_4}b_4^{1/2}$ of the hidden block along the history, and a figure with one panel (`plt.subplots()` without arguments). The blue line is the 3-space factor $e^{a_4}$, the same at every hidden position; the thick, half-transparent green line (`alpha=0.5`) is the hidden direction's factor per unit of $y$.

```python
for y, style in ((0.0, "-"), (-1.0, "--")):
    warp = np.exp(H * y)  # (sin^2 z)^(1/12) = e^(H y)
    ax.plot(times, hidden_scale * warp, style, color="tab:red",
            label=f"extra times $e^{{-a_4}}b_4^{{1/2}}e^{{Hy}}$, $y = {y}$")
    ax.plot(times, np.exp(-a4_of(times)) * b4_of(times) ** 2 * warp**3, style,
            color="black", linewidth=0.8,
            label=f"7-volume $e^{{-a_4}}b_4^2e^{{3Hy}}$, $y = {y}$")
```

For two hidden positions, the fold $y = 0$ (solid) and $y = -1$ (dashed), the cell draws the extra-time factor $e^{-a_4}b_4^{1/2}e^{Hy}$ in red and the 7-volume factor per unit of the coordinates $x_1, x_2, x_3, y, x_5, x_6, x_7$, $e^{-a_4}b_4^2e^{3Hy}$, in black. (Per unit of $y$ the hidden factor is $e^{-a_4}b_4^{1/2}$, and $e^{3a_4}$ of 3-space times $(e^{-a_4}b_4^{1/2}e^{Hy})^3$ of the extra times times $e^{-a_4}b_4^{1/2}$ gives $e^{-a_4}b_4^2e^{3Hy}$.) In the labels, doubled curly brackets `{{` and `}}` inside an f-string print single brackets.

```python
ax.set_yscale("log")
ax.set_xlabel("time $x_4$ (units of $1/m$)")
ax.set_ylabel("scale factor")
ax.set_title("Scale factors along the history $a_4 = x_4$, $b_4 = e^{4x_4/3}$")
ax.legend(fontsize=7, loc="upper left");
save_figure(fig, "scale_factors",
...)
```

A logarithmic vertical axis, labels, a title, a small legend, and Figure 08b.1. Output of the cell:

```text
PASS dy/dx0 = cot z
PASS e^(H y) = (sin^2 z)^(1/12)
PASS f0 f1 ... f7 = e^(-a4) b4^2 cot z (sin^2 z)^(1/4): sqrt|g| = its size
     reproduces Revision/theory/reports/python-field-theory.json, check sqrt_det_g
Figure 08b.1 saved as Revision/textbook/figures/08b_1_scale_factors.png
```

**What Figure 08b.1 shows.** On a logarithmic axis every exponential is a straight line. The blue line rises from 1 to $e^6 \approx 403$ at $x_4 = 6$ (3-space inflates like $e^{x_4}$). The green line falls from 1 to $e^{-2} \approx 0.135$ (the hidden block deflates like $e^{-x_4/3}$); the solid red line of the extra times at $y = 0$ lies on it, and the dashed red line at $y = -1$ lies parallel to it, lower by the factor $e^{-1}$: the extra times and the hidden direction shrink at the same rate. The black lines rise like $e^{5x_4/3}$, to $e^{10} \approx 22026$ at $x_4 = 6$ for $y = 0$: the 7-volume grows, although the hidden block deflates, because 3-space inflates faster.

**In [4], frame momenta and the onset of growth.**

```python
def frame_momenta(x4, q1, q5, qy, y):
    """(k_(1), k_(0), k_(5)) of the wave exp(i (q1 x1 + q5 x5 + qy y)) at time x4
    and hidden position y (qy is a local wave number along y)."""
    stretch = np.exp(a4_of(x4)) / np.sqrt(b4_of(x4))  # e^(a4) b4^(-1/2)
    return (q1 * np.exp(-a4_of(x4)), qy * stretch,
            q5 * stretch * np.exp(-H * y))  # e^(-H y) = (sin^2 z)^(-1/12)
```

`frame_momenta` returns the three frame momenta of Section 8.24 for a wave with the coordinate wave numbers $q_1$, $q_5$ and the local hidden wave number $q_y$ at the time $x_4$ and the hidden position $y$: $k_{(1)} = q_1e^{-a_4}$, $k_{(0)} = q_ye^{a_4}b_4^{-1/2}$ and $k_{(5)} = q_5e^{a_4}b_4^{-1/2}e^{-Hy}$ (`stretch` is the inverse scale factor $e^{a_4}b_4^{-1/2}$ of the hidden block).

```python
def local_E2(x4, q1, q5, qy, y):
    """E^2 = m^2 + k_(1)^2 + k_(0)^2 - k_(5)^2 with frozen coefficients."""
    k1, k0, k5 = frame_momenta(x4, q1, q5, qy, y)
    return mass**2 + k1**2 + k0**2 - k5**2
```

`local_E2` is $E^2 = m^2 + k_{(1)}^2 + k_{(0)}^2 - k_{(5)}^2$ with frozen coefficients (Section 8.17).

```python
def onset_time(q1, q5, qy, y):
    """The time at which E^2 = 0: X = e^(2 delta x4) is the positive root of
    D X^4 - m^2 X^3 - q1^2 = 0 with D = q5^2 e^(-2 H y) - qy^2 (no onset if D <= 0)."""
    D = q5**2 * np.exp(-2 * H * y) - qy**2
    if D <= 0:
        return np.inf  # E^2 >= m^2 at every time: the wave never grows
    coefficients = [D, -mass**2, 0.0, 0.0, -q1**2]
    roots = np.roots(coefficients)  # the four roots (complex numbers)
    X = max(r.real for r in roots if abs(r.imag) < 1e-9 * abs(r) and r.real > 0)
    for _ in range(2):  # two Newton steps polish the root
        value = np.polyval(coefficients, X)
        slope = np.polyval(np.polyder(coefficients), X)
        X -= value / slope
    return np.log(X) / (2 * delta)
```

`onset_time` finds the onset of Section 8.24. `D` is $q_5^2e^{-2Hy} - q_y^2$; for $D \le 0$ there is no onset, and the function returns `np.inf`, numpy's infinity. Otherwise `coefficients` lists the coefficients of $DX^4 - m^2X^3 + 0X^2 + 0X - q_1^2$ from the highest power down, `np.roots` returns its four roots as complex numbers, and the generator expression keeps the real positive ones (imaginary part tiny compared with the size); `max` takes the largest, which is the only one. Two steps of **Newton's method**, $X \to X - p(X)/p'(X)$ with the polynomial `np.polyval(coefficients, X)` and its derivative (`np.polyder`), make the root accurate to the last digits. The onset time is $\ln(X^\ast)/(2\delta)$.

```python
def bisection(q1, q5, qy, y, low=-30.0, high=40.0):
    """The time at which E^2 changes sign, by halving [low, high] 200 times."""
    for _ in range(200):
        middle = (low + high) / 2
        if local_E2(middle, q1, q5, qy, y) > 0:  # still oscillating: onset is later
            low = middle
        else:
            high = middle
    return (low + high) / 2
```

`bisection` finds the same time without the polynomial: it starts with the interval from $-30$ to $40$, looks at the middle, keeps the half in which $E^2$ changes sign (if $E^2 > 0$ at the middle, the wave still oscillates there, so the onset is later), and halves 200 times; the default values `low=-30.0, high=40.0` are used when no others are given.

```python
waves = [(q1, q5, qy, y) for q1 in (0.0, 0.5, 1.0, 3.0)
         for q5 in (0.01, 0.05, 0.1, 0.4) for qy in (0.0, 0.004)
         for y in (0.0, -1.0, -3.0)]  # 96 waves, all with D > 0
worst = max(abs(onset_time(*w) - bisection(*w)) for w in waves)
check(worst < 1e-10, "the onset time from the polynomial equals the bisection "
      f"result ({len(waves)} waves with D > 0)")
```

`waves` is a list of 96 waves (4 values of $q_1$, 4 of $q_5$, 2 of $q_y$ and 3 hidden positions; with $q_y \le 0.004$ and $q_5 \ge 0.01$ every one has $D > 0$). `onset_time(*w)` unpacks the four numbers of a wave into the four arguments. The largest difference between the two methods must be below $10^{-10}$.

```python
D_example = 0.1**2 - 0.05**2  # q5 = 0.1, qy = 0.05, y = 0
check(abs(onset_time(0.0, 0.05, 0.0, 0.0) - 3 * np.log(1 / 0.05)) < 1e-12 and
      abs(onset_time(0.0, 0.1, 0.05, 0.0) - 1.5 * np.log(1 / D_example)) < 1e-12,
      "q1 = 0, y = 0: onset = 3 ln(m/q5) without and (3/2) ln(m^2/D) with qy")
```

The two simple forms of Section 8.24: for $q_1 = q_y = 0$, $y = 0$ the onset is $3\ln(m/q_5)$; for $q_1 = 0$, $y = 0$ with hidden momentum it is $\frac32\ln(m^2/D)$, checked for $q_5 = 0.1$, $q_y = 0.05$, where $D = 0.0075$ (`D_example`).

```python
for q5 in (0.05, 0.1):
    report(f"onset time for q1 = 0, q5 = {q5}, qy = 0, y = 0",
           f"{onset_time(0.0, q5, 0.0, 0.0):.6f}")
report("onset time for q1 = 0, q5 = 0.1, qy = 0.05, y = 0",
       f"{onset_time(0.0, 0.1, 0.05, 0.0):.6f}")
```

Three onset times are printed: for $q_5 = 0.05$ and $0.1$ without hidden momentum ($3\ln 20$ and $3\ln 10$), and for $q_5 = 0.1$, $q_y = 0.05$.

```python
# The dark-sector record writes the mass shell with the warp factors set to 1
# (y = 0): omega^2 = M^2 + k^2 e^(-2 a4) + l^2 e^(2 a4)/b4 - q^2 e^(2 a4)/b4.
M_s, k_s, l_s, q_s, a_s = sp.symbols("M k l q a4", real=True)
b_s = sp.exp(sp.nsimplify(beta) * a_s)  # b4 = e^(beta a4) on the history
shell = M_s**2 + k_s**2 * sp.exp(-2 * a_s) + (l_s**2 - q_s**2) * sp.exp(2 * a_s) / b_s
samples = [(0.3, 0.2, 0.1, 0.25), (1.7, 0.0, 0.05, 0.1)]  # (x4, q1, qy, q5)
shell_ok = all(abs(local_E2(t, q1, q5, qy, 0.0) - float(shell.subs(
    {M_s: mass, k_s: q1, l_s: qy, q_s: q5, a_s: a4_of(t)}))) < 1e-12
               for t, q1, qy, q5 in samples)
check_record(shell_ok, "E^2 at y = 0 is the mass shell of the dark-sector record",
             "Revision/dark_sector/dirac16complex/reports/derivation-checks.json",
             "flat_mode_mass_shell",
             "omega^2 = M^2 + k^2 e^(-2a4) + l^2 e^(2a4)/b4 - q^2 e^(2a4)/b4")
```

The dark-sector record of the corrected metric writes the same mass shell with the warp factors set to 1 (that is at $y = 0$), with its own letters: $M$ the mass, $k$ the 3-momentum, $l$ the hidden momentum and $q$ the extra-time momentum, and on the history $b_4 = e^{\beta a_4}$. `shell` is its formula, built with sympy. For two sample waves (`samples` holds time, $q_1$, $q_y$, $q_5$) the notebook's `local_E2` is compared with the record's formula evaluated with `subs` at the same values; the check requires agreement to $10^{-12}$ and the record's text of the formula.

```python
q_p = q_s * sp.exp(a_s) / sp.sqrt(b_s)  # the frame momentum along an extra time
l_p = l_s * sp.exp(a_s) / sp.sqrt(b_s)  # and along the hidden direction
rates = [sp.simplify(sp.diff(sp.log(p), a_s)) for p in (q_p, l_p)]
say(f"d ln q_p/d a4 = {rates[0]}, d ln l_p/d a4 = {rates[1]}")
check_record(rates[0] == rates[1] == 1 - sp.nsimplify(beta) / 2 == sp.Rational(1, 3),
             "the extra-time and the hidden frame momenta grow at the same rate 1/3",
             "Revision/dark_sector/dirac16complex/reports/derivation-checks.json",
             "extra_time_momentum_blueshift",
             "d ln q_p/d a4 = d ln l_p/d a4 = 1 - beta/2")
```

`q_p` and `l_p` are the record's frame momenta along an extra time and along the hidden direction, $qe^{a_4}b_4^{-1/2}$ and $le^{a_4}b_4^{-1/2}$. Their growth rates per unit of $a_4$, $d\ln q_p/da_4$ and $d\ln l_p/da_4$, are computed exactly and printed; the check requires both to equal $1 - \beta/2 = \frac13$ (a chained comparison `a == b == c == d` is true only when all are equal), as the record's check `extra_time_momentum_blueshift` states. Output of the cell:

```text
PASS the onset time from the polynomial equals the bisection result (96 waves with D > 0)
PASS q1 = 0, y = 0: onset = 3 ln(m/q5) without and (3/2) ln(m^2/D) with qy
RESULT onset time for q1 = 0, q5 = 0.05, qy = 0, y = 0 = 8.987197
RESULT onset time for q1 = 0, q5 = 0.1, qy = 0, y = 0 = 6.907755
RESULT onset time for q1 = 0, q5 = 0.1, qy = 0.05, y = 0 = 7.339278
PASS E^2 at y = 0 is the mass shell of the dark-sector record
     reproduces Revision/dark_sector/dirac16complex/reports/derivation-checks.json, check
    flat_mode_mass_shell
d ln q_p/d a4 = 1/3, d ln l_p/d a4 = 1/3
PASS the extra-time and the hidden frame momenta grow at the same rate 1/3
     reproduces Revision/dark_sector/dirac16complex/reports/derivation-checks.json, check
    extra_time_momentum_blueshift
```

The third onset is $\frac32\ln(1/0.0075) = 7.339278$: the hidden momentum $q_y = 0.05$ delays the onset of the wave $q_5 = 0.1$ by about 0.43 time units.

**In [5], the frame momenta and $E^2$ along the history.**

```python
times = np.linspace(0.0, 15.0, 1501)  # long enough for the onsets
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
k1_path, k0_path, k5_path = frame_momenta(times, 0.1, 0.1, 0.05, 0.0)
```

1501 times from 0 to 15, a figure with two panels, and the three frame momenta of the wave $q_1 = q_5 = 0.1$, $q_y = 0.05$ at $y = 0$ for all times at once (the function works on arrays).

```python
left.plot(times, k5_path, color="tab:red",
          label="extra time: $k_{(5)} = q_5e^{a_4}b_4^{-1/2}$")
left.plot(times, k0_path, color="tab:green",
          label="hidden: $k_{(0)} = q_ye^{a_4}b_4^{-1/2}$")
left.plot(times, k1_path, color="tab:blue", label="3-space: $k_{(1)} = q_1e^{-a_4}$")
left.axhline(mass, color="black", linewidth=0.8, linestyle=":", label="$m$")
left.set_yscale("log")
left.set_xlabel("time $x_4$")
left.set_ylabel("frame momentum (units of $m$)")
left.set_title("$q_1 = q_5 = 0.1$, $q_y = 0.05$, $y = 0$")
left.legend(fontsize=8)
```

The left panel draws $k_{(5)}$ (red), $k_{(0)}$ (green) and $k_{(1)}$ (blue) on a logarithmic axis, with a dotted line at the mass.

```python
for q1, q5, style in ((0.0, 0.02, "-"), (0.0, 0.05, "-"), (0.0, 0.1, "-"),
                      (0.0, 0.2, "-"), (1.0, 0.05, "--")):
    right.plot(times, local_E2(times, q1, q5, 0.0, 0.0), style,
               label=f"$q_1 = {q1}$, $q_5 = {q5}$")
    t_star = onset_time(q1, q5, 0.0, 0.0)
    right.plot([t_star], [0.0], "o", color="black", markersize=4)
right.axhline(0.0, color="black", linewidth=0.8)
right.set_ylim(-4.0, 2.5)
right.set_xlabel("time $x_4$")
right.set_ylabel("$E^2 = m^2 + k_{(1)}^2 - k_{(5)}^2$")
right.set_title("Local $E^2$ along the history, $q_y = 0$, $y = 0$")
right.legend(fontsize=8, loc="lower left");
```

The right panel draws the local $E^2$ of five waves without hidden momentum: four with $q_1 = 0$ (solid) and one with $q_1 = 1$, $q_5 = 0.05$ (dashed), and marks each onset time with a black dot at $E^2 = 0$ (`"o"` draws a dot, `markersize` its size). `set_ylim(-4.0, 2.5)` fixes the vertical range.

```python
save_figure(fig, "frame_momenta",
            "Left: the frame momenta of one wave with coordinate wave numbers "
...)
```

Figure 08b.2. Output:

```text
Figure 08b.2 saved as Revision/textbook/figures/08b_2_frame_momenta.png
```

**What Figure 08b.2 shows.** Left: on the logarithmic axis the red line $k_{(5)} = 0.1e^{x_4/3}$ rises from 0.1 to $0.1e^5 \approx 14.8$ at $x_4 = 15$, and the green line $k_{(0)} = 0.05e^{x_4/3}$ rises parallel to it, from 0.05 to about 7.4: the two grow at the same rate, because the hidden direction deflates with the extra times. The blue line $k_{(1)} = 0.1e^{-x_4}$ falls steeply. Right: each $E^2$ curve starts near $m^2 = 1$ and falls, slowly at first and then steeply; the solid curves cross zero at $3\ln(1/q_5)$: $3\ln 5 \approx 4.83$ ($q_5 = 0.2$), $3\ln 10 \approx 6.91$, $3\ln 20 \approx 8.99$ and $3\ln 50 \approx 11.74$ ($q_5 = 0.02$). The dashed curve ($q_1 = 1$) starts near 2, but its space term dies away like $e^{-2x_4}$, and its onset is almost that of the same wave without space momentum.

**In [6], which waves reach the onset.**

```python
q5_grid = np.logspace(-4.0, 0.0, 200)  # 10^-4 ... 1, equally spaced on a log axis
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
all_finite_and_decreasing = True
for q1, y, style in ((0.0, 0.0, "-"), (0.0, -1.0, "--"), (0.0, -L_tip, ":"),
                     (1.0, 0.0, "-.")):
    onsets = np.array([onset_time(q1, q5, 0.0, y) for q5 in q5_grid])
    all_finite_and_decreasing &= bool(np.all(np.isfinite(onsets))
                                      and np.all(np.diff(onsets) < 0))
    left.plot(q5_grid, onsets, style, label=f"$q_1 = {q1}$, $y = {y}$")
```

`np.logspace(-4.0, 0.0, 200)` gives 200 values of $q_5$ from $10^{-4}$ to $1$, equally spaced on a logarithmic axis. For four cases without hidden momentum (three hidden positions, including the tip cutoff $y = -L = -3$, and one wave with $q_1 = 1$) the onset times are computed for the whole grid. `np.isfinite` is true for an ordinary number (not infinite); `np.diff` gives the differences of neighbours, which must all be negative (the onset time decreases as $q_5$ grows). `&=` keeps the variable true only while every case passes. Each case is drawn in the left panel.

```python
left.set_xscale("log")
left.set_xlabel("coordinate wave number $q_5$ along the extra time $x_5$")
left.set_ylabel("onset time $x_4^\\ast$ (units of $1/m$)")
left.set_title("No hidden momentum: every wave reaches the onset")
left.legend(fontsize=8)
check_record(all_finite_and_decreasing,
             "q_y = 0: the onset time is finite for every q5 > 0 on the grid and "
             "decreases with q5", "Revision/theory/reports/python-field-theory.json",
             "extra_time_modes_grow",
             "every extra-time mode eventually enters the growing regime",
             "e^{-a4/3}")
```

A logarithmic horizontal axis, labels, a title and a legend; then the check, which requires the record's sentence "every extra-time mode eventually enters the growing regime" and its statement that the hidden block shrinks like `e^{-a4/3}` on the history. The check's own title says exactly what this notebook verifies: the case $q_y = 0$. Section 8.24 explains why the record's sentence must be read with this condition.

```python
times = np.linspace(0.0, 15.0, 1501)
D_condition_ok = True
for qy, style in ((0.0, "-"), (0.05, "-"), (0.08, "-"), (0.1, "--"), (0.12, ":")):
    E2_path = local_E2(times, 0.0, 0.1, qy, 0.0)
    D = 0.1**2 - qy**2
    right.plot(times, E2_path, style, label=f"$q_y = {qy}$, $D = {D:.4f}$")
    if D > 0:  # crosses zero once, at the onset time, and stays negative
        t_star = onset_time(0.0, 0.1, qy, 0.0)
        right.plot([t_star], [0.0], "o", color="black", markersize=4)
        sign_change = np.where(np.diff(np.sign(E2_path)) != 0)[0]
        D_condition_ok &= (len(sign_change) == 1
                           and abs(times[sign_change[0]] - t_star) < 0.011)
    else:  # never below m^2
        D_condition_ok &= bool(np.all(E2_path >= mass**2 - 1e-12))
```

The right panel follows the wave $q_5 = 0.1$ at $y = 0$ with five hidden momenta $q_y = 0, 0.05, 0.08, 0.1, 0.12$. For each, `E2_path` is the local $E^2$ along the history and `D` is printed in the label with four decimals. If $D > 0$, the onset time is marked with a black dot, and `sign_change` lists the positions where the sign of $E^2$ changes between neighbouring times (`np.sign` gives $+1$, $0$ or $-1$; `np.where(...)[0]` the positions where a condition holds): there must be exactly one, within 0.011 of the computed onset time (the grid step is 0.01). If $D \le 0$, $E^2$ must stay at least $m^2$ at every time.

```python
right.axhline(0.0, color="black", linewidth=0.8)
right.set_ylim(-3.0, 3.0)
right.set_xlabel("time $x_4$")
right.set_ylabel("$E^2 = m^2 + k_{(0)}^2 - k_{(5)}^2$")
right.set_title("$q_5 = 0.1$, $y = 0$: hidden momentum $q_y$")
right.legend(fontsize=7, loc="lower right");
check(D_condition_ok, "a wave reaches the onset exactly when D = q5^2 e^(-2 H y) - "
      "qy^2 > 0 (five hidden momenta)")
```

Labels, a zero line, and the check of the $D$ condition.

```python
save_figure(fig, "onset_times",
            "Left: the onset time $x_4^\\ast$ at which a wave with coordinate wave "
...)
```

Figure 08b.3. Output:

```text
PASS q_y = 0: the onset time is finite for every q5 > 0 on the grid and decreases with q5
     reproduces Revision/theory/reports/python-field-theory.json, check
    extra_time_modes_grow
PASS a wave reaches the onset exactly when D = q5^2 e^(-2 H y) - qy^2 > 0 (five hidden
    momenta)
Figure 08b.3 saved as Revision/textbook/figures/08b_3_onset_times.png
```

**What Figure 08b.3 shows.** Left: the onset time (vertical, units of $1/m$) against $q_5$ (horizontal, logarithmic). Each curve is a falling, nearly straight line: on a logarithmic $q_5$ axis, $x_4^\ast = 3(Hy + \ln(m/q_5))/(AH)$ falls by 3 for every factor $e$ in $q_5$. At $q_5 = 10^{-4}$ and $y = 0$ the onset is at $3\ln 10^4 \approx 27.6$; the curve for $y = -1$ lies three units lower and that for $y = -3$ nine units lower (for large $q_5$ these are negative: such waves grow already at $x_4 = 0$); the curve with $q_1 = 1$ lies on top of the $y = 0$ curve except at the largest $q_5$. No curve goes to infinity: without hidden momentum the onset always comes. Right: the solid curves ($q_y = 0, 0.05, 0.08$; $D = 0.0100, 0.0075, 0.0036$) cross zero at $6.91$, $7.34$ and $\frac32\ln(1/0.0036) \approx 8.44$: a hidden momentum delays the onset. The dashed curve ($q_y = 0.1$, $D = 0$) is the horizontal line $E^2 = 1$, and the dotted curve ($q_y = 0.12$, $D < 0$) rises: these waves never grow.

**In [7], the model's mode matrix and the starting columns.**

```python
gammas_record = json.loads(
    repository_file("Revision/algebra/gammas.json").read_text(encoding="utf-8"))
GAMMA = [np.array(rows, dtype=int) for rows in gammas_record["gamma"]]
C = np.array(gammas_record["C"], dtype=int)  # C = g^(x0) g^(x1) g^(x2) g^(x3)
B = np.array(gammas_record["B"]["re"]) + 1j * np.array(gammas_record["B"]["im"])
g4 = GAMMA[4].astype(complex)  # gamma^(x4)
g4g1 = (GAMMA[4] @ GAMMA[1]).astype(complex)  # gamma^(x4) gamma^(x1)
g4g5 = (GAMMA[4] @ GAMMA[5]).astype(complex)  # gamma^(x4) gamma^(x5)
check(np.array_equal(C @ GAMMA[4], GAMMA[4] @ C) and
      np.array_equal(C @ GAMMA[5], GAMMA[5] @ C),
      "C commutes with gamma^(x4) and gamma^(x5)")
```

The gammas, $C$ and $B$ are read from `Revision/algebra/gammas.json` (the matrix $B$ is stored as its real and imaginary parts, `B["re"]` and `B["im"]`; `1j` is the imaginary unit $i$ in Python). The three matrices of the model, $\gamma^{(4)}$, $\gamma^{(4)}\gamma^{(1)}$ and $\gamma^{(4)}\gamma^{(5)}$, are prepared as complex arrays (`astype(complex)`). The check confirms that $C$ commutes with $\gamma^{(4)}$ and $\gamma^{(5)}$ (Section 8.25; `np.array_equal` compares two integer arrays exactly).

```python
def h_local(x4, q1, q5, y):
    """The mode matrix of the local-frame model at time x4 (no hidden momentum)."""
    k1, _, k5 = frame_momenta(x4, q1, q5, 0.0, y)
    return -1j * mass * g4 - k1 * g4g1 - k5 * g4g5
```

`h_local` is the model's mode matrix $h(x_4) = -im\gamma^{(4)} - k_{(1)}(x_4)\gamma^{(4)}\gamma^{(1)} - k_{(5)}(x_4)\gamma^{(4)}\gamma^{(5)}$, without hidden momentum (the hidden frame momentum returned by `frame_momenta` is not used, hence the name `_`).

```python
# At every instant h(x4)^2 = E^2(x4) I16, where E^2 is the frozen-coefficient E^2 of
# the record with k1 = k_(1)(x4), k5 = k_(5)(x4) and all other momenta 0.
m_s = sp.Symbol("m", real=True)
k_s = {a: sp.Symbol(f"k{a}", real=True) for a in (0, 1, 2, 3, 5, 6, 7)}
E2_record = m_s**2 + sum(k_s[a] ** 2 for a in (0, 1, 2, 3)) \
    - sum(k_s[a] ** 2 for a in (5, 6, 7))
```

`E2_record` is the record's general formula $E^2 = m^2 + k_1^2 + k_2^2 + k_3^2 + k_0^2 - k_5^2 - k_6^2 - k_7^2$, built with exact symbols (`k_s` is a dictionary of the seven momentum symbols).

```python
squares_ok = True
for x4 in (0.0, 1.0, 2.0, 3.0, 4.0):
    k1_now, _, k5_now = frame_momenta(x4, 0.3, 0.1, 0.0, 0.0)  # q1 = 0.3, q5 = 0.1
    values = {symbol: 0 for symbol in k_s.values()}  # every momentum 0 ...
    values.update({m_s: mass, k_s[1]: k1_now, k_s[5]: k5_now})  # ... but these
    E2_now = float(E2_record.subs(values))
    h_now = h_local(x4, 0.3, 0.1, 0.0)
    squares_ok &= bool(np.allclose(h_now @ h_now, E2_now * np.eye(16), atol=1e-12)
                       and abs(E2_now - local_E2(x4, 0.3, 0.1, 0.0, 0.0)) < 1e-12)
check_record(squares_ok, "x4 = 0, 1, 2, 3, 4: h(x4)^2 = E^2(x4) I16 (q1 = 0.3, "
             "q5 = 0.1)", "Revision/theory/reports/python-scope.json",
             "extra_time_growth_rates_unbounded", f"h_k^2 = ({sp.sstr(E2_record)}) I16")
```

At five instants, for the wave $q_1 = 0.3$, $q_5 = 0.1$, the record's formula is evaluated with the frame momenta of that instant (a dictionary sets every momentum to 0, and `update` then sets the mass, $k_1$ and $k_5$), and the square of the model's matrix is compared with $E^2I_{16}$ to $10^{-12}$; the value must also agree with `local_E2`. The check requires the record's text with the general $E^2$ (`sp.sstr(E2_record)` writes the formula as sympy prints it).

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

`starting_column` applies the two projectors of Section 8.25, $\frac12(I + \sigma C)$ and $\frac12(I + h(0)/E_0)$ (together the factor $\frac14$), to the first unit column (a column of zeros with a 1 in position 0) and divides by its length (`np.linalg.norm`).

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

Two starting columns are made, for $q_5 = 0.05$ with $\sigma = +1$ and for $q_5 = 0.1$ with $\sigma = -1$, and stored in the dictionary `starts`. For each, `np.vdot(u0, B @ u0)` computes $u^\dagger Bu$ (`vdot` conjugates its first argument), the RESULT line prints $E_0$ and the Krein form, and the check confirms to $10^{-14}$ the three properties: eigenvector of $h(0)$ for $E_0$, eigenvector of $C$ for $\sigma$, Krein form $\sigma E_0/m$. Output:

```text
PASS C commutes with gamma^(x4) and gamma^(x5)
PASS x4 = 0, 1, 2, 3, 4: h(x4)^2 = E^2(x4) I16 (q1 = 0.3, q5 = 0.1)
     reproduces Revision/theory/reports/python-scope.json, check
    extra_time_growth_rates_unbounded
RESULT q5 = 0.05: E0, Krein form of the start = 0.998749218, +0.998749218
PASS q5 = 0.05: h(0) u = E0 u, C u = +u, Krein form = +E0/m
RESULT q5 = 0.1: E0, Krein form of the start = 0.994987437, -0.994987437
PASS q5 = 0.1: h(0) u = E0 u, C u = -u, Krein form = -E0/m
```

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

`rk4_history` solves the model with RK4 and records, after every step, the time, the Hilbert norm $u^\dagger u$ and the Krein form $u^\dagger Bu$ (`u0.copy()` makes a copy, so that the starting column itself is not changed). The inner function `rate` is the right-hand side $-ih(x_4)v$; unlike In [8] of Notebook 08a the matrix now depends on the time.

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
    x4_end = onset_time(0.0, q5, 0.0, 0.0) + 3.0 / delta  # 9 units after the onset
    runs[q5] = rk4_history(starts[q5], q5, x4_end, 36000)
    at_onset = np.searchsorted(runs[q5][0], onset_time(0.0, q5, 0.0, 0.0))  # index
    report(f"q5 = {q5}: u^dagger u at the onset", f"{runs[q5][1][at_onset]:.2f}")
    final_size = runs[q5][1][-1]  # u^dagger u at the end of the run
    report(f"q5 = {q5}: ln(u^dagger u) at the onset + 9", f"{np.log(final_size):.6f}")
```

Each wave is followed from $x_4 = 0$ to $3/\delta = 9$ time units after its onset with 36000 steps; the results are stored in `runs` (for each wave the four results of `rk4_history`: `runs[q5][0]` is the array of the times, `runs[q5][1]` the array of the sizes $u^\dagger u$). `np.searchsorted(times, t)` is the position of the first recorded time that is not earlier than `t`, here the first step at or after the onset; the first RESULT line of each wave prints the size $u^\dagger u$ there, with two decimals. The second RESULT line prints $\ln(u^\dagger u)$ at the end of the run.

```python
x4_end = onset_time(0.0, 0.05, 0.0, 0.0) + 3.0 / delta
end_18000 = rk4_history(starts[0.05], 0.05, x4_end, 18000)[3]
end_72000 = rk4_history(starts[0.05], 0.05, x4_end, 72000)[3]
end_36000 = runs[0.05][3]
ratio = np.linalg.norm(end_18000 - end_36000) / np.linalg.norm(end_36000 - end_72000)
relative_error = np.linalg.norm(end_36000 - end_72000) / np.linalg.norm(end_72000)
report("RK4 error ratio (18000 vs 36000) / (36000 vs 72000) steps", f"{ratio:.2f}")
```

The run with $q_5 = 0.05$ is repeated with 18000 and 72000 steps (`[3]` takes the final column), the ratio of the differences of the final columns and the relative error of the 36000-step run are computed, and the ratio is printed.

```python
check(14.0 < ratio < 18.0, "RK4 converges with order 4 (error ratio near 16)")
check(relative_error < 1e-8, "the 36000-step run is accurate to 1e-8 (relative)")
```

The convergence test. For a fourth-order method the difference between 18000 and 36000 steps is about $2^4 = 16$ times the difference between 36000 and 72000 steps; the check requires the ratio between 14 and 18. The difference between 36000 and 72000 steps, relative to the length of the column, estimates the error of the 36000-step run; it must be below $10^{-8}$. Output:

```text
RESULT q5 = 0.05: u^dagger u at the onset = 2.00
RESULT q5 = 0.05: ln(u^dagger u) at the onset + 9 = 111.245745
RESULT q5 = 0.1: u^dagger u at the onset = 1.99
RESULT q5 = 0.1: ln(u^dagger u) at the onset + 9 = 111.221594
RESULT RK4 error ratio (18000 vs 36000) / (36000 vs 72000) steps = 15.89
PASS RK4 converges with order 4 (error ratio near 16)
PASS the 36000-step run is accurate to 1e-8 (relative)
```

The size started at 1; at the onset it is 2.00 ($q_5 = 0.05$) and 1.99 ($q_5 = 0.1$): before the onset it grows only slowly (the mode matrix is not Hermitian, so the size is not conserved; Section 8.19). Nine time units after the onset $\ln(u^\dagger u) = 111.245745$, that is $u^\dagger u \approx 2.06 \times 10^{48}$. The error ratio is 15.89.

**In [9], the WKB formulas and the comparison.**

```python
def Q_of(x4, q5):
    return q5 * np.exp(delta * x4)  # the frame momentum k_(5) at y = 0


def kappa_of(x4, q5):
    return np.sqrt(Q_of(x4, q5) ** 2 - mass**2)


def W_of(x4, q5):
    Q = Q_of(x4, q5)
    return (np.sqrt(Q**2 - mass**2) - mass * np.arccos(mass / Q)) / delta
```

The three functions of Section 8.25: $Q = q_5e^{\delta x_4}$, $\kappa = \sqrt{Q^2 - m^2}$ and $W = \frac{1}{\delta}(\sqrt{Q^2 - m^2} - m\arccos(m/Q))$ (`np.arccos` is the inverse cosine).

```python
comparison = {}
for q5 in (0.05, 0.1):
    x4s, hilbert, krein, _ = runs[q5]
    start = np.searchsorted(x4s, onset_time(0.0, q5, 0.0, 0.0) + 1.5 / delta)
    xa, xb = x4s[start], x4s[-1]
    increase = np.log(hilbert[-1]) - np.log(hilbert[start])
    leading = 2 * (W_of(xb, q5) - W_of(xa, q5))
    first = leading + np.log(Q_of(xb, q5) / kappa_of(xb, q5)) \
        - np.log(Q_of(xa, q5) / kappa_of(xa, q5))
    comparison[q5] = (xa, increase, leading, first)
```

For each run the window starts at the first recorded time $1.5/\delta = 4.5$ units after the onset and ends at the last time. `increase` is the increase of $\ln(u^\dagger u)$ over the window in the RK4 solution; `leading` is the leading WKB increase $2(W(x_b) - W(x_a))$; `first` adds the first-order correction $\ln(Q/\kappa)$ at the two ends. The four numbers are stored for the plot.

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
predicted = 2 * kappa_late - delta * mass**2 / kappa_late**2
report("q5 = 0.05: computed late rate, predicted 2 kappa - delta m^2/kappa^2",
       f"{late_rate:.5f}, {predicted:.5f}")
check(abs(late_rate - predicted) / predicted < 1e-5,
      "the late growth rate equals 2 kappa - delta m^2/kappa^2 to 1e-5")
```

The growth rate at the end of the run is computed by a **centred difference**, the change of $\ln(u^\dagger u)$ over the last two steps divided by their length, which approximates the derivative at the middle point; the first-order prediction $2\kappa - \delta m^2/\kappa^2$ is evaluated at that middle point; the check requires a relative agreement better than $10^{-5}$. Output:

```text
q5 = 0.05: window 13.4874 to 17.9872; increase of ln(u^dagger u) 93.0724, leading WKB
    93.0985 (relative difference 2.81e-04), first order 93.0742 (relative difference
    1.97e-05)
PASS q5 = 0.05: leading WKB agrees to 2e-3 over the window
PASS q5 = 0.05: first-order WKB is better and agrees to 5e-4
q5 = 0.1: window 11.4081 to 15.9078; increase of ln(u^dagger u) 93.0714, leading WKB
    93.0975 (relative difference 2.81e-04), first order 93.0732 (relative difference
    1.97e-05)
PASS q5 = 0.1: leading WKB agrees to 2e-3 over the window
PASS q5 = 0.1: first-order WKB is better and agrees to 5e-4
RESULT q5 = 0.05: computed late rate, predicted 2 kappa - delta m^2/kappa^2 = 40.11371,
    40.11373
PASS the late growth rate equals 2 kappa - delta m^2/kappa^2 to 1e-5
```

**In [10], the growth of the size along the history.**

```python
fig, ax = plt.subplots()
for q5, colour in ((0.05, "tab:blue"), (0.1, "tab:orange")):
    x4s, hilbert, _, _ = runs[q5]
    xa, _, _, _ = comparison[q5]
    ax.plot(x4s, np.log(hilbert), color=colour, label=f"RK4, $q_5 = {q5}$")
    after = x4s >= onset_time(0.0, q5, 0.0, 0.0) + 0.05
    shift = np.log(hilbert[np.searchsorted(x4s, xa)]) - 2 * W_of(xa, q5)
    ax.plot(x4s[after], 2 * W_of(x4s[after], q5) + shift, "--", color="black",
            linewidth=0.9)
    ax.axvline(onset_time(0.0, q5, 0.0, 0.0), color=colour, linestyle=":",
               linewidth=0.9)
```

For both runs: $\ln(u^\dagger u)$ of the RK4 solution; the leading WKB curve $2W$, drawn from 0.05 units after the onset (`after` is a true/false array that selects those times) and shifted by a constant so that it agrees with the solution at the window start; and a dotted vertical line at the onset (`axvline`).

```python
ax.plot([], [], "--", color="black", linewidth=0.9, label="WKB $2W$ + const")
ax.set_xlabel("time $x_4$ (units of $1/m$)")
ax.set_ylabel("$\\ln(u^\\dagger u)$")
ax.set_title("A wave along an extra time, $a_4 = x_4$, $b_4 = e^{4x_4/3}$, $y = 0$")
ax.legend();
save_figure(fig, "growth_along_history",
            "The natural logarithm of the size $u^\\dagger u$ of a wave with "
...)
```

An empty dashed line for the legend, labels, and Figure 08b.4; the cell prints only the figure line:

```text
Figure 08b.4 saved as Revision/textbook/figures/08b_4_growth_along_history.png
```

**What Figure 08b.4 shows.** The natural logarithm of $u^\dagger u$ (vertical, pure number) against the time $x_4$ (units of $1/m$) for the two waves $q_5 = 0.05$ (blue) and $q_5 = 0.1$ (orange). Before its onset (dotted vertical line at $3\ln 10 \approx 6.91$ or $3\ln 20 \approx 8.99$) each curve rises only slowly, from 0 to about 0.7 ($\ln 2.00 = 0.69$, $\ln 1.99 = 0.69$): the wave oscillates and its size only about doubles. After the onset the curve bends upwards ever more steeply and reaches about 111 nine units later (a factor of about $10^{48}$), following the black dashed WKB curve. The student should see the switch from oscillation to growth at the predicted time, and growth that accelerates.

**In [11], the growth rate and the Krein form.**

```python
x4s, hilbert, krein, _ = runs[0.05]
step = x4s[1] - x4s[0]
computed_rate = (np.log(hilbert[2:]) - np.log(hilbert[:-2])) / (2 * step)
middle = x4s[1:-1]
after = middle > onset_time(0.0, 0.05, 0.0, 0.0) + 0.02
drift = np.abs(krein - krein[0]) / np.maximum(hilbert, 1.0)
check(drift.max() < 1e-9, "the Krein form is conserved (drift below 1e-9)")
check(hilbert[-1] > 1e40, "the Hilbert norm grows by more than 10^40")
```

For the run with $q_5 = 0.05$: the growth rate at every inner time by centred differences (`hilbert[2:]` drops the first two values, `hilbert[:-2]` the last two, so the two arrays are shifted by two steps; `middle` are the middle times); `after` selects the times just after the onset; `drift` is the change of the Krein form divided by $\max(u^\dagger u, 1)$. The checks require the drift below $10^{-9}$ and a final size above $10^{40}$.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
fig.subplots_adjust(wspace=0.35)  # room for the label of the right panel
left.plot(middle, computed_rate, color="tab:blue", label="RK4 (centred differences)")
left.plot(middle[after], 2 * kappa_of(middle[after], 0.05), "--", color="black",
          label="$2\\kappa$")
left.plot(middle[after], 2 * kappa_of(middle[after], 0.05)
          - delta * mass**2 / kappa_of(middle[after], 0.05) ** 2, ":", color="tab:red",
          label="$2\\kappa - \\delta m^2/\\kappa^2$")
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
...)
```

The right panel draws the drift on a logarithmic axis (`semilogy`); a logarithm cannot show an exact zero, so zeros are raised to $10^{-18}$ (`np.maximum`). The figure is Figure 08b.5. Output:

```text
PASS the Krein form is conserved (drift below 1e-9)
PASS the Hilbert norm grows by more than 10^40
Figure 08b.5 saved as Revision/textbook/figures/08b_5_rate_and_krein.png
```

**What Figure 08b.5 shows.** Left: the growth rate $d\ln(u^\dagger u)/dx_4$ (units of $m$) against the time $x_4$ (units of $1/m$): small before the onset at $x_4 \approx 9$ (it stays below 1; on the vertical scale up to 45 this looks almost flat), then rising ever more steeply to about 40; the black dashed curve $2\kappa$ and the red dotted curve $2\kappa - \delta m^2/\kappa^2$ start at the onset, where both fail ($\kappa \to 0$), and the computed rate approaches the red curve as $\kappa$ grows. Right: the change of the Krein form relative to $\max(u^\dagger u, 1)$, on a logarithmic axis: it stays at the level of rounding errors (the drops to $10^{-18}$ are exact zeros), far below $10^{-9}$. The student should see that the rate itself grows exponentially (growth faster than any exponential) while the Krein form is conserved.

**In [12], the last check.**

```python
for name in ("08b_1_scale_factors.png", "08b_2_frame_momenta.png",
             "08b_3_onset_times.png", "08b_4_growth_along_history.png",
             "08b_5_rate_and_krein.png"):
    check(output_file(f"{FIGURE_FOLDER}/{name}").is_file(),
          f"the figure file {name} exists")
all_checks_passed()
```

Five checks that the figure files exist, and the last line. The 29 checks come from the cells as follows: two in In [2], three in In [3], four in In [4], two in In [6], four in In [7], two in In [8], five in In [9], two in In [11] and five here (In [5] and In [10] have none). Output:

```text
PASS the figure file 08b_1_scale_factors.png exists
PASS the figure file 08b_2_frame_momenta.png exists
PASS the figure file 08b_3_onset_times.png exists
PASS the figure file 08b_4_growth_along_history.png exists
PASS the figure file 08b_5_rate_and_krein.png exists
ALL 29 CHECKS PASSED (notebook 08b)
```

### 8.30 Changing the field variables: the rescaling $\Psi = e^{a_4/2}b_4^{-1}(\sin^2 z)^{-1/8}\,\chi$

Section 8.9 changed the frame. This section keeps the diagonal frame and changes the field variables instead: we write the field as a known function times a new field, $\Psi = R\,\chi$ with $R = e^{a_4/2}b_4^{-1}(\sin^2 z)^{-1/8}$, and ask which equation $\chi$ obeys.

**The derivatives of the factor.** $R$ depends only on $x_0$ and $x_4$. Line by line:

$$
\begin{aligned}
\partial_0(\sin^2 z)^{-1/8} &= -\tfrac18(\sin^2 z)^{-9/8}\cdot 2\sin z\cos z\cdot 6H = -\tfrac32H\cot z\,(\sin^2 z)^{-1/8}, \\
\frac{1}{f_0}\,\partial_0R &= e^{a_4}b_4^{-1/2}\tan z\cdot\big(-\tfrac32H\cot z\big)R = -\tfrac32He^{a_4}b_4^{-1/2}\,R = -c_g\,R , \\
\partial_4R &= \Big(\frac{a_4'}{2} - \frac{b_4'}{b_4}\Big)R = -v_g\,R .
\end{aligned}
$$

The first line is the power rule for $(\cdot)^{-1/8}$ and the chain rule (the derivative of $\sin^2 z$ with respect to $z$ is $2\sin z\cos z$, and $dz/dx_0 = 6H$), followed by $(\sin^2 z)^{-9/8}\sin z\cos z = (\sin^2 z)^{-1/8}\cos z/\sin z$; the second multiplies by $1/f_0 = e^{a_4}b_4^{-1/2}\tan z$ and uses $\tan z\cot z = 1$; the third differentiates $e^{a_4/2}b_4^{-1}$ with the chain rule and the power rule ($\partial_4e^{a_4/2} = \frac12a_4'e^{a_4/2}$, $\partial_4b_4^{-1} = -b_4'b_4^{-2}$).

**The term disappears.** For $\mu \neq x_0, x_4$, $\partial_\mu(R\chi) = R\,\partial_\mu\chi$, because $R$ does not depend on $x_\mu$. For $\mu = x_0$ and $\mu = x_4$ the product rule gives $\partial_\mu(R\chi) = (\partial_\mu R)\chi + R\,\partial_\mu\chi$. So, line by line,

$$
\begin{aligned}
\gamma^\mu D_\mu(R\chi) &= \sum_\mu\gamma^\mu\partial_\mu(R\chi) + GR\chi \\
&= R\sum_\mu\gamma^\mu\partial_\mu\chi + \gamma^{(0)}\frac{\partial_0R}{f_0}\chi + \gamma^{(4)}(\partial_4R)\chi + \big(c_g\gamma^{(0)} + v_g\gamma^{(4)}\big)R\chi \\
&= R\sum_\mu\gamma^\mu\partial_\mu\chi + \big(-c_gR + c_gR\big)\gamma^{(0)}\chi + \big(-v_gR + v_gR\big)\gamma^{(4)}\chi = R\sum_\mu\gamma^\mu\partial_\mu\chi .
\end{aligned}
$$

The first line uses $\gamma^\mu D_\mu = \gamma^\mu\partial_\mu + \gamma^\mu\Omega_\mu$ and $\gamma^\mu\Omega_\mu = G$ (Section 8.5); the second applies the product rule, with $\gamma^{x_0} = \gamma^{(0)}/f_0$ and $\gamma^{x_4} = \gamma^{(4)}$ ($f_4 = 1$); the third inserts the two derivatives of $R$. For every column $\chi$ of 16 functions the spin-connection term is gone: in the variables $\chi$ the derivative part of the field equation is $R\,\gamma^\mu\partial_\mu\chi$, with no term $G$ (PROVED; `Revision/theory/reports/python-scope.json`, check `rescaling_removes_the_connection_term`, both engines). The frame factors $e^{a_4}b_4^{-1/2}\tan z$, $e^{-a_4}$ and $e^{a_4}b_4^{-1/2}(\sin^2 z)^{-1/12}$ stay: they are part of $\gamma^\mu$.

**The potential.** $S$ is quadratic in the field and $R$ is real, so $S[R\chi] = (R\chi)^\dagger C(R\chi) = R^2\,\chi^\dagger C\chi = e^{a_4}b_4^{-2}(\sin^2 z)^{-1/4}S[\chi] = e^{a_4}S[\chi]/(b_4^2|\sin z|^{1/2})$ (because $(\sin^2 z)^{1/4} = |\sin z|^{1/2}$). With $U = \frac\lambda2S^2$, $U'(S[\Psi]) = \lambda S[\Psi]$. The field equation $\gamma^\mu D_\mu\Psi = (m + \lambda S[\Psi])\Psi$ becomes $R\,\gamma^\mu\partial_\mu\chi = \big(m + \lambda e^{a_4}S[\chi]/(b_4^2|\sin z|^{1/2})\big)R\chi$, and dividing by $R > 0$:

$$
\gamma^\mu\partial_\mu\chi = \Big(m + \frac{\lambda\,e^{a_4}S[\chi]}{b_4^2|\sin z|^{1/2}}\Big)\chi .
$$

For $U = 0$ the term $G$ is removed completely; for $U \neq 0$ it reappears in a new form, as the coupling $\lambda e^{a_4}S[\chi]/(b_4^2|\sin z|^{1/2})$, which depends on $x_0$ and on the time (PROVED; `python-scope.json`, check `rescaled_equation_quadratic_potential`, both engines).

**The weight moves into the measure.** The norm of a field along the hidden direction is $\int\sqrt{|g|}\,\Psi^\dagger\Psi\,dx_0$. In the new variables, line by line,

$$
\sqrt{|g|}\,\Psi^\dagger\Psi\,dx_0 = e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}\cdot e^{a_4}b_4^{-2}(\sin^2 z)^{-1/4}\,\chi^\dagger\chi\,dx_0 = |\cot z|\,\chi^\dagger\chi\,dx_0 = \chi^\dagger\chi\,|dy| ,
$$

by inserting $\sqrt{|g|}$ and $R^2$, cancelling, and using $dy = \cot z\,dx_0$ (Section 8.24). So the norm of $\Psi$ is the plain $y$-integral of $\chi^\dagger\chi$: the factor $e^{a_4/2}b_4^{-1}$ takes the changing volume $e^{-a_4}b_4^2$ out of the norm, and $(\sin^2 z)^{-1/8}$ its dependence on $x_0$.

**The scope of "the field equation contains $G$".** Together with Section 8.9: the value $G$ belongs to one frame (the diagonal one) AND to one choice of field variables ($\Psi$). A boosted frame removes its part $c_g\gamma^{(0)}$, and the rescaling removes all of it. Interpretation (labelled as such, not a theorem): in the variables $\Psi$ with the measure $\sqrt{|g|}\,dx_0$ the part $c_g$ makes the hidden-direction operator $e^{a_4}b_4^{-1/2}(\tan z\,\partial_0 + \frac32H)\gamma^{(0)}$ antisymmetric up to a boundary term, and the part $v_g$ compensates the change of the volume in time (Section 8.32); in the variables $\chi$ with the measure $|dy|$ the plain derivative has the same property without any such term. The role of $G$ therefore depends on the variables and the measure.

### 8.31 The fold, the tips, and two exact families of solutions

**The fold and the tips.** Proper length along the hidden direction is $\sqrt{g_{00}}\,dx_0$, which is $e^{-a_4}b_4^{1/2}|\cot z|\,dx_0$, that is $e^{-a_4}b_4^{1/2}$ times $|dy|$. A **tip** ($z \to 0$ or $z \to \pi$) is $y \to -\infty$: infinitely far from every point. The **fold** $z = \pi/2$ is $y = 0$: at the finite proper distance $e^{-a_4}b_4^{1/2}|y|$ from the point $y$. At the fold $g_{00} = e^{-2a_4}b_4\cot^2 z = 0$ and $\sqrt{|g|} = 0$: the surface is degenerate, and the two halves of a cell meet there. The Revision record claims nothing about it and imposes no boundary condition there. (The Kohn-Sham record ASSUMES fold conditions at $y = 0$ for its own model, Chapter 14; the corrected metric has no orbifold, no brane and no mirror copy. This chapter imposes no boundary condition.)

**The reduction.** For $U = 0$ and a field $\Psi = F\,(\sin^2 z)^{\alpha/2}\,\Phi(x_4)$, with $F = e^{a_4/2}b_4^{-1}$, a real exponent $\alpha$ and a column $\Phi$ of 16 functions of the time, the field equation reduces to an equation in $x_4$ alone. Write $P = (\sin^2 z)^{\alpha/2}$, $K = \gamma^{(4)}\gamma^{(0)}$ and $\mu_A = (4\alpha + 1)c_g = \frac32H(4\alpha + 1)e^{a_4}b_4^{-1/2}$. First the two factor rules, line by line:

$$
\begin{aligned}
\frac{1}{f_0}\,\partial_0P &= e^{a_4}b_4^{-1/2}\tan z\cdot\tfrac\alpha2(\sin^2 z)^{\alpha/2 - 1}\cdot2\sin z\cos z\cdot 6H = 6H\alpha\,e^{a_4}b_4^{-1/2}\,P = 4\alpha c_g\,P, \\
\partial_4F &= -v_g\,F .
\end{aligned}
$$

The first line uses the power rule and the chain rule, then $\tan z\cdot(\sin^2 z)^{-1}\sin z\cos z = 1$, then $6H = 4\cdot\frac32H$; the second is the third line of Section 8.30 without the factor of $z$. Now, line by line (only $\mu = x_0$ and $\mu = x_4$ act on $\Psi$):

$$
\begin{aligned}
\gamma^\mu D_\mu\Psi - m\Psi &= \gamma^{(0)}\frac{\partial_0\Psi}{f_0} + \gamma^{(4)}\partial_4\Psi + \big(c_g\gamma^{(0)} + v_g\gamma^{(4)}\big)\Psi - m\Psi \\
&= FP\Big[4\alpha c_g\gamma^{(0)}\Phi + \gamma^{(4)}\big(\Phi' - v_g\Phi\big) + c_g\gamma^{(0)}\Phi + v_g\gamma^{(4)}\Phi - m\Phi\Big] \\
&= FP\Big[\gamma^{(4)}\Phi' + \mu_A\gamma^{(0)}\Phi - m\Phi\Big] \\
&= FP\,\gamma^{(4)}\Big[\Phi' - \big(-m\gamma^{(4)} + \mu_AK\big)\Phi\Big] .
\end{aligned}
$$

The first line writes out the operator; the second inserts $\Psi = FP\Phi$ and the factor rules; the third collects ($4\alpha c_g + c_g = \mu_A$, and the two terms $\mp v_g\gamma^{(4)}\Phi$ cancel); the fourth checks by multiplying out: $\gamma^{(4)}(m\gamma^{(4)}\Phi) = -m\Phi$ and $-\gamma^{(4)}\mu_A\gamma^{(4)}\gamma^{(0)}\Phi = \mu_A\gamma^{(0)}\Phi$, by $(\gamma^{(4)})^2 = -I_{16}$. So $\Psi$ solves the field equation exactly when

$$
\Phi' = \big(-m\gamma^{(4)} + \mu_AK\big)\Phi
$$

(PROVED; `Revision/theory/reports/wolfram-field-theory.json`, check `solution_matrix_square`). The matrix facts used below: $K^2 = \gamma^{(4)}\gamma^{(0)}\gamma^{(4)}\gamma^{(0)} = -(\gamma^{(4)})^2(\gamma^{(0)})^2 = I_{16}$ (one anticommutation of the middle pair, then the two squares), and $K\gamma^{(4)} = \gamma^{(4)}\gamma^{(0)}\gamma^{(4)} = -\gamma^{(4)}\gamma^{(4)}\gamma^{(0)} = -\gamma^{(4)}K$ (one anticommutation of the last two factors).

**Two families in closed form.** (i-a) $m = 0$, every $\alpha$: $\Phi = (\cosh I + \sinh I\,K)\chi_0$ with a constant column $\chi_0$ and $I' = \mu_A$. Indeed $\Phi' = I'(\sinh I + \cosh I\,K)\chi_0$ and $\mu_AK\Phi = \mu_A(\cosh I\,K + \sinh I\,K^2)\chi_0 = \mu_A(\sinh I + \cosh I\,K)\chi_0$, equal because $I' = \mu_A$ and $K^2 = I_{16}$. (i-b) $\alpha = -\frac14$ (then $\mu_A = 0$), every $m$: $\Phi = (\cos(mx_4) - \sin(mx_4)\gamma^{(4)})\chi_0$. Indeed $\Phi' = -m(\sin(mx_4) + \cos(mx_4)\gamma^{(4)})\chi_0$ and $-m\gamma^{(4)}\Phi = -m(\cos(mx_4)\gamma^{(4)} - \sin(mx_4)(\gamma^{(4)})^2)\chi_0 = -m(\cos(mx_4)\gamma^{(4)} + \sin(mx_4))\chi_0$, the same. Both families solve the field equation for ALL functions $a_4$ and $b_4$ (PROVED; `Revision/theory/reports/python-field-theory.json`, check `exact_solution_family_x4_x0`; Wolfram checks `exact_solution_x4_x0_m0_G` and `exact_solution_x4_x0_quarter_G`). The member $\alpha = -\frac14$ is the rescaled field of Section 8.30 with $\chi$ independent of $x_0$: there is no $H$ in it. For $m \neq 0$ and $\alpha \neq -\frac14$ the matrices $M(x_4) = -m\gamma^{(4)} + \mu_AK$ of two different times do not commute, $[M_1, M_2] = 2m(\mu_1 - \mu_2)\gamma^{(4)}K \neq 0$ when $\mu_A$ changes, so the solution is not an exponential of an integral, and the record knows no closed form for general $a_4$, $b_4$.

**Which members have a finite norm.** The norm of a member on the first half of a cell ($0 < z < \pi/2$, where $\sin z > 0$ and $\cot z > 0$) is $\Phi^\dagger\Phi$ times an integral over $x_0$, line by line:

$$
\begin{aligned}
\int_0^{\pi/(12H)}\sqrt{|g|}\,F^2(\sin^2 z)^\alpha\,dx_0 &= \int_0^{\pi/(12H)}\cot z\,\sin^{2\alpha + 1/2}z\,dx_0 = \Big[\frac{\sin^pz}{6Hp}\Big]_0^{\pi/(12H)} \\
&= \frac{1}{6Hp} = \frac{1}{3H(4\alpha + 1)} \qquad (p = 2\alpha + \tfrac12 > 0).
\end{aligned}
$$

The first step inserts $\sqrt{|g|} = e^{-a_4}b_4^2\cot z\,\sin^{1/2}z$ and $F^2 = e^{a_4}b_4^{-2}$, which cancel except for the factors of $z$; the second uses the antiderivative $\sin^pz/(6Hp)$ (its derivative is $p\sin^{p-1}z\cos z\cdot6H/(6Hp) = \cot z\sin^pz$); the third evaluates it at the fold ($\sin z = 1$) and at the tip ($\sin^pz \to 0$ exactly when $p > 0$), and writes $6Hp = 3H(4\alpha + 1)$. For $p \le 0$ the integral diverges at the tip; for $p = 0$ ($\alpha = -\frac14$) the antiderivative is $\ln(\sin z)/(6H)$, which goes to $-\infty$. So the members with a finite norm are exactly those with $\alpha > -\frac14$, and the member without $H$, $\alpha = -\frac14$, has an infinite norm. For $\alpha = 0$ the factor is $1/(3H)$, the value the record gives (`python-scope.json`, check `good_sector_x0_independent_modes_without_boundary_condition`).

**When the members grow.** With frozen time the matrix $M = -m\gamma^{(4)} + \mu_AK$ has, line by line,

$$
M^2 = m^2(\gamma^{(4)})^2 - m\mu_A\big(\gamma^{(4)}K + K\gamma^{(4)}\big) + \mu_A^2K^2 = (\mu_A^2 - m^2)\,I_{16},
$$

by multiplying out, $(\gamma^{(4)})^2 = -I_{16}$, $K\gamma^{(4)} = -\gamma^{(4)}K$ and $K^2 = I_{16}$. So the instantaneous growth rate is $\sqrt{\mu_A^2 - m^2}$ wherever $\mu_A^2 > m^2$. On the history $\mu_A = \frac32H(4\alpha + 1)e^{Hx_4/3}$ grows without bound for every $\alpha \neq -\frac14$, so it overtakes every mass $m > 0$, at the time where $\frac32H|4\alpha + 1|e^{Hx_4/3} = m$, that is

$$
x_4 = \frac3H\ln\frac{2m}{3H|4\alpha + 1|} .
$$

For $m = 0$ the exact family (i-a) grows like $e^{I(x_4)}$ with $I(x_4) = \int_0^{x_4}\mu_A\,ds = \frac32H(4\alpha + 1)\cdot\frac3H\big(e^{Hx_4/3} - 1\big) = \frac92(4\alpha + 1)\big(e^{Hx_4/3} - 1\big)$, faster than any exponential. So every member with a finite norm starts to grow after a finite time, for every mass (PROVED with frozen time; the formulas for $\mu_A$ on the history, the onset time and $I$ are PROVED exactly and checked by Notebook 08d; the record states the case $\alpha = 0$).

### 8.32 The boundary term at the fold and the growing modes of the good sector

**The fields that do not depend on $x_0$.** Such a field of the good sector depends only on $x_4$, and its field equation is $\gamma^{(4)}\partial_4\Psi + c_g\gamma^{(0)}\Psi + v_g\gamma^{(4)}\Psi = m\Psi$. Line by line: multiplying from the left by $\gamma^{(4)}$ (as in Section 8.16) gives $-\partial_4\Psi + c_g\gamma^{(4)}\gamma^{(0)}\Psi - v_g\Psi = m\gamma^{(4)}\Psi$; solving for $\partial_4\Psi$ and multiplying by $i$ gives

$$
i\,\partial_4\Psi = \big(A - iv_g\big)\Psi, \qquad A = -im\gamma^{(4)} + ic_g\gamma^{(4)}\gamma^{(0)} .
$$

For $\Psi = F\chi$ with $F = e^{a_4/2}b_4^{-1}$ the term $-iv_g$ is absorbed by the factor ($i\partial_4(F\chi) = F(i\partial_4\chi - iv_g\chi)$, by $\partial_4F = -v_gF$), and $i\,\partial_4\chi = A\chi$; this is the reduced equation of Section 8.31 at $\alpha = 0$, because $A = i(-m\gamma^{(4)} + c_gK)$. Its square is $A^2 = -M^2 = (m^2 - c_g^2)I_{16}$, so wherever $m < c_g$ its eigenvalues are $\pm i\sqrt{c_g^2 - m^2}$, eight each, and half of the modes grow; at $m = H = 1$ and $x_4 = 0$ on the history ($c_g = \frac32$) they are $\pm\frac{\sqrt5}{2}i$. $A$ is not Hermitian (its second term is anti-Hermitian, see below). These modes have the finite norm factor $1/(3H)$ (the case $\alpha = 0$ above). On the history $c_g = \frac32He^{Hx_4/3}$ grows, so every mass falls below it at late times: for $m = 2$, $H = 1$ at $x_4 = 3\ln\frac43 \approx 0.863$. (PROVED; `python-scope.json`, check `good_sector_x0_independent_modes_without_boundary_condition`, both engines.) So even the good sector, without any extra-time dependence, contains growing modes of finite norm, as long as nothing is imposed at the fold.

**The mode operator.** For fields of $x_4$ and $x_0$ (and $U = 0$) the same steps, with the term $\gamma^{(0)}e^{a_4}b_4^{-1/2}\tan z\,\partial_0\Psi$ in addition, give $i\,\partial_4\Psi = h\Psi$ with the **mode operator**

$$
\begin{aligned}
h &= -im\gamma^{(4)} + i\gamma^{(4)}\gamma^{(0)}e^{a_4}b_4^{-1/2}\big(\tan z\,\partial_0 + \tfrac32H\big) - iv_g = A + P\,\partial_0 - iv_g, \\
P &= ie^{a_4}b_4^{-1/2}\tan z\,\gamma^{(4)}\gamma^{(0)} .
\end{aligned}
$$

**Four matrix facts.** Let $M_0 = i\gamma^{(4)}\gamma^{(0)}$ and write $\sqrt{|g|} = \sigma e^{-a_4}b_4^2\cot z\,W^3$ with $\sigma = \pm1$ the sign of $\cot z$ (Section 8.5). The real matrix $\gamma^{(4)}\gamma^{(0)}$ is symmetric: $(\gamma^{(4)}\gamma^{(0)})^T = (\gamma^{(0)})^T(\gamma^{(4)})^T = \gamma^{(0)}(-\gamma^{(4)}) = \gamma^{(4)}\gamma^{(0)}$. Hence:

1. $P^\dagger = -ie^{a_4}b_4^{-1/2}\tan z\,(\gamma^{(4)}\gamma^{(0)})^T = -P$: the coefficient of $\partial_0$ is anti-Hermitian.
2. $\sqrt{|g|}\,P = \sigma e^{-a_4}b_4^2\cot z\,W^3\cdot ie^{a_4}b_4^{-1/2}\tan z\,\gamma^{(4)}\gamma^{(0)} = \sigma b_4^{3/2}W^3\,M_0$.
3. $(-im\gamma^{(4)})^\dagger = im(\gamma^{(4)})^T = -im\gamma^{(4)}$ (Hermitian) and $(ic_g\gamma^{(4)}\gamma^{(0)})^\dagger = -ic_g\gamma^{(4)}\gamma^{(0)}$ (anti-Hermitian), so $A - A^\dagger = 2ic_g\gamma^{(4)}\gamma^{(0)} = 2c_gM_0$, and $\sqrt{|g|}\,(A - A^\dagger) = 3H\sigma b_4^{3/2}\cot z\,W^3\,M_0 = \partial_0\big(\sigma b_4^{3/2}W^3\big)\,M_0$, because $2c_g\cdot e^{-a_4}b_4^2 = 3Hb_4^{3/2}$ and $\partial_0W^3 = 3W^2\cdot H\cot z\,W$.
4. The number $-iv_g$ is imaginary ($v_g$ is real), so its difference with its complex conjugate is $-2iv_g$, and $\sqrt{|g|}\cdot(-2iv_g) = -i\,\partial_4\sqrt{|g|}$, because $\partial_4\sqrt{|g|} = 2v_g\sqrt{|g|}$ (Section 8.2).

**The boundary identity.** For any two columns $u(x_0)$, $v(x_0)$, line by line (a prime is $\partial_0$ here):

$$
\begin{aligned}
\sqrt{|g|}\big[u^\dagger(hv) - (hu)^\dagger v\big] &= \sqrt{|g|}\,u^\dagger(A - A^\dagger)v + \sqrt{|g|}\big[u^\dagger Pv' - u'^\dagger P^\dagger v\big] - 2iv_g\sqrt{|g|}\,u^\dagger v \\
&= \sqrt{|g|}\,u^\dagger(A - A^\dagger)v + \sqrt{|g|}\big[u^\dagger Pv' + u'^\dagger Pv\big] - 2iv_g\sqrt{|g|}\,u^\dagger v \\
&= \partial_0\big(\sigma b_4^{3/2}W^3\big)\,u^\dagger M_0v + \sigma b_4^{3/2}W^3\big[u^\dagger M_0v' + u'^\dagger M_0v\big] - i\,(\partial_4\sqrt{|g|})\,u^\dagger v \\
&= \partial_0\big(\sigma b_4^{3/2}(\sin^2 z)^{1/4}\,u^\dagger M_0v\big) - i\,(\partial_4\sqrt{|g|})\,u^\dagger v .
\end{aligned}
$$

The first line inserts $h = A + P\partial_0 - iv_g$ and uses $(hu)^\dagger = u^\dagger A^\dagger + u'^\dagger P^\dagger + iv_gu^\dagger$; the second uses fact 1; the third uses facts 3, 2 and 4; the fourth recognises the product rule for the three factors $\sigma b_4^{3/2}W^3$, $u^\dagger$ and $v$ ($M_0$ is constant, $b_4$ does not depend on $x_0$) and writes $W^3 = (\sin^2 z)^{1/4}$. (PROVED; `python-scope.json`, check `good_sector_hermiticity_up_to_the_brane_flux`, both engines; the word "brane" in the check's name is a leftover of the withdrawn metric of 2026-10-14, and the corrected metric has no brane: the boundary term sits at the fold.) Integrated over the hidden direction, the left side is the failure of $h$ to be symmetric for the inner product $\int\sqrt{|g|}\,u^\dagger v\,dx_0$. On the right side, the first term gives the **boundary term** (or **flux**) $[\sigma b_4^{3/2}(\sin^2 z)^{1/4}u^\dagger M_0v]$, taken between a tip and the fold; the second term is the change of the volume factor in time, which the next paragraph shows to be compensated. At a tip $\sin z \to 0$; at the fold $|\sin z| = 1$, and the flux need not vanish: for a column with $\gamma^{(4)}\gamma^{(0)}u = u$ (such columns exist, because $(\gamma^{(4)}\gamma^{(0)})^2 = I_{16}$ and the matrix is not $\pm I_{16}$), $u^\dagger M_0u = i\,u^\dagger u \neq 0$; the record's example has $u^\dagger u = 2$ and $u^\dagger M_0u = 2i$.

**The norm changes only through the fold.** For a solution of $i\,\partial_4\Psi = h\Psi$ let $N(x_4) = \int_0^{\pi/(12H)}\sqrt{|g|}\,\Psi^\dagger\Psi\,dx_0$ (the first half of a cell, $\sigma = +1$). Line by line:

$$
\begin{aligned}
\frac{dN}{dx_4} &= \int\Big[(\partial_4\sqrt{|g|})\,\Psi^\dagger\Psi + \sqrt{|g|}\big((\partial_4\Psi)^\dagger\Psi + \Psi^\dagger\partial_4\Psi\big)\Big]dx_0 \\
&= \int(\partial_4\sqrt{|g|})\,\Psi^\dagger\Psi\,dx_0 - i\int\sqrt{|g|}\big[\Psi^\dagger(h\Psi) - (h\Psi)^\dagger\Psi\big]dx_0 \\
&= \int(\partial_4\sqrt{|g|})\,\Psi^\dagger\Psi\,dx_0 - i\big[b_4^{3/2}(\sin^2 z)^{1/4}\,\Psi^\dagger M_0\Psi\big]_{\text{tip}}^{\text{fold}} - \int(\partial_4\sqrt{|g|})\,\Psi^\dagger\Psi\,dx_0 \\
&= -i\,b_4^{3/2}\,\Psi^\dagger M_0\Psi\big|_{z=\pi/2} = b_4^{3/2}\,\Psi^\dagger\gamma^{(4)}\gamma^{(0)}\Psi\big|_{z=\pi/2} .
\end{aligned}
$$

The first line differentiates under the integral with the product rule ($\sqrt{|g|}$ depends on $x_4$ through $a_4$ and $b_4$); the second inserts the equation, $\partial_4\Psi = -ih\Psi$, and collects the factors $\mp i$; the third uses the boundary identity with $u = v = \Psi$ (the integral of a derivative is the difference of its end values, and $-i\cdot(-i) = -1$ in the last term); the fourth cancels the two integrals and uses $\sin z = 0$ at the tip, $\sin z = 1$ at the fold and $-i\cdot i = 1$. The norm of a solution changes ONLY by the flux through the fold: the term $-iv_g$ of $h$ exactly compensates the change of the volume. For a field $\Psi = F\chi(x_4)$ that does not depend on $x_0$, $N = \chi^\dagger\chi/(3H)$ and the flux is $b_4^{3/2}F^2\chi^\dagger\gamma^{(4)}\gamma^{(0)}\chi = e^{a_4}b_4^{-1/2}\chi^\dagger\gamma^{(4)}\gamma^{(0)}\chi$. Notebook 08d follows such a mode with $m = 2$, $H = 1$ along the history from $x_4 = 0$ to 4, through its onset at $3\ln\frac43$: its norm grows by the factor $N(4)/N(0) = 1.569834 \times 10^8$, and $dN/dx_4$ equals the flux at every time to $5.9 \times 10^{-10}$ (relative; COMPUTED).

**What this means (labelled).** Interpretation: the growth of the good-sector modes is fed through the fold. A boundary condition at $z = \pi/2$ that stops the flux would make $h$ symmetric and would change the spectrum; which condition is physical is OPEN (the Kohn-Sham record ASSUMES fold conditions for its own model). Without one, the initial-value problem of the good sector has growing solutions: this is the second way, besides the extra-time waves of Sections 8.17 to 8.25, in which the field equation as recorded fails to define a stable evolution.

### 8.33 Example: the rescaling and the modes of the hidden direction

Notebook 08d puts Sections 8.30 to 8.32 to work, exactly, with sympy, for symbolic functions $a_4$ and $b_4$. It takes the spin connection of the diagonal frame from the record's formula and verifies it (the gammas are covariantly constant, and $\gamma^\mu\Omega_\mu = G$); proves the rescaling for sixteen arbitrary component functions and the new coupling of the potential; draws the rescaling factor and the hidden coordinate $y$ with the tip cutoff of the Kohn-Sham record; verifies the reduction and the two exact families for symbolic $\alpha$, $m$, $H$ and all functions $a_4$ and $b_4$, and maps which members have a finite norm and when they grow along the history; checks the matrix $A$ of the modes that do not depend on $x_0$ and the action of the mode operator on $F\chi$; proves the boundary identity on explicit columns; and follows a growing mode whose norm changes exactly by the flux through the fold. It needs no Rust and runs in one to three minutes; the times measured on the build computer, which depend on how busy that computer is, are recorded in the notebook's provenance file `Revision/textbook/notebooks/08d_rescaling_modes.PROVENANCE.md`. It ends with the line ALL 27 CHECKS PASSED (notebook 08d).

<!-- NOTEBOOK 08d -->

### 8.36 Line-by-line walk-through of Notebook 08d

The notebook has 12 code cells, In [1] to In [12]. The conventions are those of Section 8.15; captions shortened to `...)` are printed in full in Section 8.35.

**In [1], the set-up cell.** It is the set-up cell explained in Section 8.15, with the line `NOTEBOOK_ID = "08d"  # this notebook: chapter 08, example d`; its comment lines are the run instructions of Section 8.34. Output: `Set-up of notebook 08d complete: repository folder found, helpers defined.`

**In [2], the spin connection from the record, verified.**

```python
import numpy as np  # numbers and matrices (for the plots)
import sympy as sp  # exact algebra with symbols

REPORTS = {}  # report file -> {check name: (verdict, detail)}, each read once


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


def check_record(condition, title, report_file, check_name, *pieces):
    """check() for a result that reproduces the Revision check check_name: it passes
    only if condition is true AND the report records check_name as passed, with
    every piece of text (values computed here) in its detail."""
    on_record = record_says(report_file, check_name, *pieces)
    check(condition and on_record, title,
          record=f"{report_file}, check {check_name}")
```

The imports, the table `REPORTS` and the two record helpers, exactly as in Notebook 08b (Section 8.29): `check_record` takes one check name.

```python
THEORY = "Revision/theory/reports/python-field-theory.json"  # the sympy records
SCOPE = "Revision/theory/reports/python-scope.json"
gammas_record = json.loads(
    repository_file("Revision/algebra/gammas.json").read_text(encoding="utf-8"))
G = [sp.Matrix(rows) for rows in gammas_record["gamma"]]  # gamma^(x0) ... (x7)
ETA = gammas_record["eta"]  # [1, 1, 1, 1, -1, -1, -1, -1]
C = sp.Matrix(gammas_record["C"])  # C = gamma^(x0) gamma^(x1) gamma^(x2) gamma^(x3)
theory = json.loads(
    repository_file("Revision/theory/field-theory.json").read_text(encoding="utf-8"))
formulas = {entry["key"]: entry for entry in theory["formulas"]}
say("record Omega_components: " + formulas["Omega_components"]["wl"])
```

`THEORY` and `SCOPE` are short names for two Revision reports. The gammas and $C$ are read as in Notebook 08c. `theory` holds the formula record `Revision/theory/field-theory.json`, whose list `formulas` has one entry per formula with a `key` and the formula in the Wolfram language (`wl`); `formulas` turns the list into a dictionary by key, and the `say` line prints the record's formula of the spinor connection (`g[xi]` is $\gamma^{(x_i)}$, `h4` the rate $h_4$, `sb` the factor $e^{-a_4}b_4^{1/2}$).

```python
x = sp.symbols("x0:8", real=True)  # the coordinates; x[k] is xk
x0, x4 = x[0], x[4]  # the hidden direction and the time
H = sp.Symbol("H", positive=True)
m = sp.Symbol("m", real=True)
a4 = sp.Function("a4", real=True)(x4)  # any real function of the time x4
b4 = sp.Function("b4", positive=True)(x4)  # any positive function of x4
a4_prime, b4_prime = sp.diff(a4, x4), sp.diff(b4, x4)
z = 6 * H * x0  # every real value
```

The coordinates, $H$, the mass $m$, the two unknown functions $a_4(x_4)$ (real) and $b_4(x_4)$ (positive), their derivatives, and $z = 6Hx_0$, as in Notebook 08c.

```python
class W(sp.Function):
    """The warp factor W(x0) = (sin(6 H x0)^2)^(1/12) > 0 of the extra times."""

    def fdiff(self, argindex=1):
        """dW/dx0 = H cot(6 H x0) W, for every real z = 6 H x0 with sin z != 0."""
        return H * sp.cot(6 * H * self.args[0]) * self

    def _eval_is_positive(self):
        return True  # the positive root


def is_zero(expr):
    """True when sympy shows that expr is exactly zero (two simplifications)."""
    expr = sp.sympify(expr)
    if expr == 0:
        return True
    simpler = sp.simplify(expr)
    return simpler == 0 or sp.simplify(sp.fu(simpler)) == 0
```

The warp factor `W` with its derivative rule and its positivity, and the helper `is_zero`, both as in Notebook 08c (Section 8.15).

```python
explicit = (sp.sin(z) ** 2) ** sp.Rational(1, 12)  # the twelfth root, written out
check(is_zero(sp.diff(explicit, x0) - H * sp.cot(z) * explicit),
      "the derivative of (sin^2 z)^(1/12) is H cot z (sin^2 z)^(1/12): the rule of W")
```

The derivative rule of `W` is checked against the explicit $(\sin^2 z)^{1/12}$, whose derivative sympy computes itself.

```python
s_b = sp.exp(-a4) * sp.sqrt(b4)  # the scale of the hidden block e^(-a4) b4^(1/2)
f = [s_b * sp.cot(z)] + [sp.exp(a4)] * 3 + [sp.Integer(1)] \
    + [s_b * W(x0)] * 3  # the frame factors f_0, ..., f_7
g = [ETA[a] * f[a] ** 2 for a in range(8)]  # the diagonal metric
gamma_up = [G[mu] / f[mu] for mu in range(8)]  # gamma^mu = gamma^(mu) / f_mu
h4 = b4_prime / (2 * b4) - a4_prime  # the rate of the hidden block
Omega = [sp.zeros(16, 16) for _ in range(8)]  # Omega_x4 stays zero
Omega[0] = h4 * s_b * sp.cot(z) * G[0] * G[4] / 2  # the hidden direction x0
for i in (1, 2, 3):  # x1, x2, x3 (inflating)
    Omega[i] = a4_prime * sp.exp(a4) * G[i] * G[4] / 2
for t in (5, 6, 7):  # x5, x6, x7 (deflating extra times)
    Omega[t] = W(x0) * (h4 * s_b * G[4] * G[t] + H * G[0] * G[t]) / 2
```

`s_b`, the scale factors `f`, the metric entries `g` and the coordinate gammas $\gamma^\mu = \gamma^{(\mu)}/f_\mu$ of the diagonal frame; `h4` is the rate $h_4 = b_4'/(2b_4) - a_4'$. `Omega` is the list of the eight spinor connections typed in from the record's formula (Section 8.4): $\Omega_{x_0} = \frac12h_4s_b\cot z\,\gamma^{(0)}\gamma^{(4)}$, $\Omega_{x_i} = \frac12a_4'e^{a_4}\gamma^{(i)}\gamma^{(4)}$, $\Omega_{x_t} = \frac12W(h_4s_b\gamma^{(4)}\gamma^{(t)} + H\gamma^{(0)}\gamma^{(t)})$ and $\Omega_{x_4} = 0$ (the list starts with eight zero matrices, and the entry of $x_4$ is left zero).

```python
Gam = [[[sp.Integer(0)] * 8 for _ in range(8)] for _ in range(8)]
for lam in range(8):  # Christoffel symbols of the diagonal metric
    for mu in range(8):
        for nu in range(8):
            value = 0
            if lam == nu:
                value += sp.diff(g[lam], x[mu])
            if lam == mu:
                value += sp.diff(g[lam], x[nu])
            if mu == nu:
                value -= sp.diff(g[mu], x[lam])
            if value != 0:
                Gam[lam][mu][nu] = sp.simplify(value / (2 * g[lam]))
```

The Christoffel symbols of the diagonal metric, computed as in Notebook 08c (Section 8.15, In [3]).

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

`constant` is true when the covariant derivative $\partial_\mu\gamma^\nu + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}\gamma^\lambda + \Omega_\mu\gamma^\nu - \gamma^\nu\Omega_\mu$ is the zero matrix for all 64 pairs $(\mu, \nu)$. Since only one connection made of the $S^{ab}$ has this property (Section 8.9, Step 4), this check verifies the typed-in formula; it reproduces the record's check `covariant_constancy_D_mu_gamma_nu`.

```python
c_g = sp.Rational(3, 2) * H * sp.exp(a4) / sp.sqrt(b4)  # (3/2) H e^a4 b4^(-1/2)
v_g = b4_prime / b4 - a4_prime / 2  # b4'/b4 - a4'/2
gamma_Omega = sum((gamma_up[mu] * Omega[mu] for mu in range(8)), sp.zeros(16, 16))
check_record(all(is_zero(v) for v in gamma_Omega - c_g * G[0] - v_g * G[4]),
             "gamma^mu Omega_mu = c_g gamma^(x0) + v_g gamma^(x4) (diagonal frame)",
             THEORY, "gamma_mu_Omega_mu_equals_hidden_block_terms",
             "gamma^mu Omega_mu = (3/2) H e^a4 b4^(-1/2) gamma^(x0) + (b4'/b4 - "
             "a4'/2) gamma^(x4) exactly")
```

`c_g` and `v_g` are the two coefficients of Section 8.5, and `gamma_Omega` is $\gamma^\mu\Omega_\mu$ computed from the typed-in connection. The check proves that it equals $c_g\gamma^{(0)} + v_g\gamma^{(4)}$ entry by entry, as the record states. Output of the cell:

```text
record Omega_components: Omega_x0 = (1/2) h4 sb Cot[6 H x0] g[x0].g[x4]; Omega_xi = (1/2)
    a4'[x4] E^a4[x4] g[xi].g[x4] (i = 1, 2, 3); Omega_xt = (1/2) (Sin[6 H x0]^2)^(1/12)
    (h4 sb g[x4].g[xt] + H g[x0].g[xt]) (t = 5, 6, 7); Omega_x4 = 0; g[xa] = gamma^(xa)
    (frame gammas of the fixture)
PASS the derivative of (sin^2 z)^(1/12) is H cot z (sin^2 z)^(1/12): the rule of W
PASS the record's Omega_mu makes every gamma^nu covariantly constant (64 pairs)
     reproduces Revision/theory/reports/python-field-theory.json, check
    covariant_constancy_D_mu_gamma_nu
PASS gamma^mu Omega_mu = c_g gamma^(x0) + v_g gamma^(x4) (diagonal frame)
     reproduces Revision/theory/reports/python-field-theory.json, check
    gamma_mu_Omega_mu_equals_hidden_block_terms
```

**In [3], the rescaling removes the term.**

```python
R = sp.exp(a4 / 2) / b4 * W(x0) ** sp.Rational(-3, 2)  # the rescaling factor
check_record(is_zero(sp.diff(R, x0) / f[0] + c_g * R)
             and is_zero(sp.diff(R, x4) + v_g * R),
             "(1/f0) d0 R = -c_g R and d4 R = -v_g R for R = e^(a4/2) b4^(-1) "
             "(sin^2 z)^(-1/8)", SCOPE, "rescaling_removes_the_connection_term",
             "the x0 terms: e^a4 b4^(-1/2) tan z (-(3/2) H cot z) + cg = 0; "
             "the x4 terms: a4'/2 - b4'/b4 + vg = 0")
```

`R` is the rescaling factor $e^{a_4/2}b_4^{-1}(\sin^2 z)^{-1/8}$, written with the warp factor as $e^{a_4/2}b_4^{-1}W^{-3/2}$ (because $W^{-3/2} = (\sin^2 z)^{-3/24} = (\sin^2 z)^{-1/8}$). The check proves the two one-line identities of Section 8.30, $(1/f_0)\partial_0R = -c_gR$ and $\partial_4R = -v_gR$, and requires the record's text of the same two identities.

```python
chi = sp.Matrix([sp.Function(f"chi{A}")(*x) for A in range(1, 17)])  # arbitrary
Psi = R * chi
D_Psi = sum((gamma_up[mu] * (sp.diff(Psi, x[mu]) + Omega[mu] * Psi)
             for mu in range(8)), sp.zeros(16, 1))  # gamma^mu D_mu Psi
D_chi = sum((gamma_up[mu] * sp.diff(chi, x[mu]) for mu in range(8)),
            sp.zeros(16, 1))  # gamma^mu d_mu chi (no connection)
check_record(all(is_zero(v) for v in D_Psi - R * D_chi),
             "gamma^mu D_mu (R chi) = R gamma^mu d_mu chi for 16 arbitrary functions",
             SCOPE, "rescaling_removes_the_connection_term",
             "In the variables chi the field equation has no spin-connection term: "
             "gamma^mu d_mu chi = (m + U'(S)) chi")
```

`chi` is a column of sixteen ARBITRARY functions $\chi_1, \dots, \chi_{16}$ of all eight coordinates (`sp.Function(f"chi{A}")(*x)` makes an unknown function named `chi1`, ..., `chi16` of $x_0, \dots, x_7$; `*x` hands over the eight coordinates). `Psi` is $R\chi$. `D_Psi` is $\gamma^\mu D_\mu\Psi = \sum_\mu\gamma^\mu(\partial_\mu\Psi + \Omega_\mu\Psi)$ and `D_chi` is $\gamma^\mu\partial_\mu\chi$, without connection (`sp.zeros(16, 1)` is a zero column to start the sums). The check proves that $\gamma^\mu D_\mu(R\chi) - R\,\gamma^\mu\partial_\mu\chi$ is zero in all sixteen components, for every $\chi$: in the variables $\chi$ the field equation has no spin-connection term.

```python
lam, S_chi = sp.symbols("lambda S_chi", real=True)  # S_chi stands for S[chi]
S_Psi = R**2 * S_chi  # S[R chi] = (R chi)^dagger C (R chi) = R^2 S[chi]
abs_sin = sp.Abs(sp.sin(z))  # |sin z|
coupling = sp.exp(a4) * S_chi / (b4**2 * abs_sin ** sp.Rational(1, 2))
check_record(is_zero((lam * S_Psi).subs(W(x0), abs_sin ** sp.Rational(1, 6))
                     - lam * coupling),
             "U = (lambda/2) S^2: lambda S[Psi] = lambda e^a4 S[chi]/(b4^2 "
             "|sin z|^(1/2)) (the new coupling)", SCOPE,
             "rescaled_equation_quadratic_potential",
             "S[Psi] = Psi^dagger C Psi = e^a4 b4^(-2) |sin z|^(-1/2) S[chi]",
             "gamma^mu d_mu chi = (m + lambda e^a4 S[chi]/(b4^2 |sin z|^(1/2))) chi")
```

The potential. `S_chi` is a real symbol that stands for $S[\chi] = \chi^\dagger C\chi$; since $R$ is real, $S[R\chi] = R^2S[\chi]$ (`S_Psi`). `coupling` is the new coupling of Section 8.30 without the factor $\lambda$. The check replaces `W(x0)` by $|\sin z|^{1/6}$ and proves $\lambda S[\Psi] = \lambda e^{a_4}S[\chi]/(b_4^2|\sin z|^{1/2})$, with the record's texts.

```python
sigma = sp.Symbol("sigma", real=True)  # the sign of cot z (+1 or -1)
sqrt_g = sigma * sp.exp(-a4) * b4**2 * sp.cot(z) * W(x0) ** 3  # the volume factor
y_of_x0 = sp.log(sp.sin(z) ** 2) / (12 * H)  # y = ln|sin z|/(6 H)
check(is_zero(sqrt_g * R**2 - sigma * sp.cot(z)) and
      is_zero(sp.diff(y_of_x0, x0) - sp.cot(z)),
      "sqrt|g| R^2 = |cot z| = |dy/dx0|: the norm of Psi is the y-norm of chi")
```

`sigma` is the sign $\sigma$ of $\cot z$, so that `sqrt_g` $= \sigma e^{-a_4}b_4^2\cot z\,W^3$ is the volume factor; `y_of_x0` is the hidden coordinate. The check proves $\sqrt{|g|}R^2 = \sigma\cot z = |\cot z|$ and $dy/dx_0 = \cot z$: the norm of $\Psi$ is the $y$-integral of $\chi^\dagger\chi$. Output of the cell:

```text
PASS (1/f0) d0 R = -c_g R and d4 R = -v_g R for R = e^(a4/2) b4^(-1) (sin^2 z)^(-1/8)
     reproduces Revision/theory/reports/python-scope.json, check
    rescaling_removes_the_connection_term
PASS gamma^mu D_mu (R chi) = R gamma^mu d_mu chi for 16 arbitrary functions
     reproduces Revision/theory/reports/python-scope.json, check
    rescaling_removes_the_connection_term
PASS U = (lambda/2) S^2: lambda S[Psi] = lambda e^a4 S[chi]/(b4^2 |sin z|^(1/2)) (the new
    coupling)
     reproduces Revision/theory/reports/python-scope.json, check
    rescaled_equation_quadratic_potential
PASS sqrt|g| R^2 = |cot z| = |dy/dx0|: the norm of Psi is the y-norm of chi
```

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

The cell reads $H$ and the tip cutoff $L$ from the Kohn-Sham record and computes $z_{\rm cut} = \arcsin(e^{-6HL})$, where $y = -L$ (Section 8.31); both are printed, and the check confirms $H = 1$ and $y(z_{\rm cut}) = -L$ to $10^{-12}$.

```python
zs = np.linspace(0.01, np.pi - 0.01, 600)  # one cell, tips at 0 and pi
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
left.plot(zs, (np.sin(zs) ** 2) ** (-1 / 8), label="rescaling $(\\sin^2 z)^{-1/8}$")
left.plot(zs, np.abs(np.sin(zs)) ** -0.5, "--", label="coupling $|\\sin z|^{-1/2}$")
left.axvline(np.pi / 2, color="gray", linewidth=0.8)  # the fold
left.set_yscale("log")
left.set_xlabel("$z = 6Hx_0$ over one cell (fold at $\\pi/2$)")
left.set_ylabel("factor (units $e^{a_4/2}b_4^{-1}$, $e^{a_4}b_4^{-2}$)")
left.set_title("$\\Psi = e^{a_4/2}b_4^{-1}(\\sin^2 z)^{-1/8}\\chi$")
left.legend(loc="upper center")
```

600 values of $z$ across one cell, from $0.01$ to $\pi - 0.01$, and two panels. The left panel draws the factor $(\sin^2 z)^{-1/8}$ of the rescaling (solid) and the factor $|\sin z|^{-1/2}$ of the new coupling (dashed) on a logarithmic axis, with a gray line at the fold $z = \pi/2$.

```python
mantissa, exponent = f"{z_cut:.1e}".split("e")  # "1.5e-08" -> "1.5" and "-08"
exponent = int(exponent)  # -8, for the caption
z_log = np.logspace(-10.0, np.log10(np.pi / 2), 400)  # 10^-10 ... pi/2, log spaced
right.semilogx(z_log, np.log(np.sin(z_log)) / (6 * H_record), color="tab:green")
right.axhline(-L_tip, color="gray", linestyle=":", linewidth=0.9)
right.plot([z_cut], [-L_tip], "o", color="black")  # where y reaches the cutoff
right.text(2e-8, -L_tip + 0.15, "tip cutoff $y = -L$ of the Kohn-Sham record",
           fontsize=8)
right.set_xlabel("$z = 6Hx_0$ (logarithmic axis), first half of a cell")
right.set_ylabel("$y = \\ln|\\sin z|/(6H)$")
right.set_title("The hidden coordinate $y$, $H = 1$")
```

`f"{z_cut:.1e}"` writes $z_{\rm cut}$ as `1.5e-08`, and `split("e")` cuts this text into the mantissa `1.5` and the exponent `-08`, which `int` turns into the number $-8$; both are used in the caption. The right panel draws $y = \ln|\sin z|/(6H)$ against 400 values of $z$ from $10^{-10}$ to $\pi/2$ on a logarithmic $z$ axis (`semilogx`), with a dotted line at $y = -L$, a black dot where $y$ reaches it, and a short text (`right.text(x, y, text)` writes the text at the point $(x, y)$).

```python
save_figure(fig, "rescaling_factors",
            "Left, on a logarithmic axis, against $z = 6Hx_0$ across one cell from "
...)
```

Figure 08d.1; the end of its caption is an f-string that inserts the cutoff and the computed $z_{\rm cut}$. Output:

```text
RESULT H and the tip cutoff L of the Kohn-Sham record = 1.0, 3.0
RESULT z at the tip cutoff, arcsin(e^(-6 H L)) = 1.522998e-08
PASS the record has H = 1, and y(z_cut) = -L
     reproduces Revision/kohn_sham/results/parameters.json, physics.H,
    physics.L_tipCutoff
Figure 08d.1 saved as Revision/textbook/figures/08d_1_rescaling_factors.png
```

**What Figure 08d.1 shows.** Left: both factors equal 1 at the fold and rise towards the tips, the same on both halves of the cell (the curves are symmetric about $z = \pi/2$); at $z = 0.01$ the rescaling factor is $(0.01^2)^{-1/8} \approx 3.2$ and the coupling factor $0.01^{-1/2} = 10$. Right: on the logarithmic $z$ axis $y$ is almost a straight line, because $\sin z \approx z$ for small $z$; it rises from about $-3.8$ at $z = 10^{-10}$ to 0 at the fold. The cutoff $y = -3$ of the Kohn-Sham record is reached only at $z = \arcsin(e^{-18}) \approx 1.5 \times 10^{-8}$.

**In [5], two exact families of solutions.**

```python
K = G[4] * G[0]  # K = gamma^(x4) gamma^(x0)
F = sp.exp(a4 / 2) / b4  # the scalar factor F = e^(a4/2) b4^(-1)
alpha = sp.Symbol("alpha", real=True)
mu_A = (4 * alpha + 1) * c_g  # (3/2) H (4 alpha + 1) e^a4 b4^(-1/2)
power = W(x0) ** (6 * alpha)  # (sin^2 z)^(alpha/2) = W^(6 alpha)
```

`K` is $\gamma^{(4)}\gamma^{(0)}$, `F` is $e^{a_4/2}b_4^{-1}$, `alpha` a real symbol, `mu_A` the coefficient $\mu_A = (4\alpha + 1)c_g$, and `power` is $(\sin^2 z)^{\alpha/2}$ written as $W^{6\alpha}$ (because $(\sin^2 z)^{1/12\cdot6\alpha} = (\sin^2 z)^{\alpha/2}$).

```python
K_facts = (K * K == sp.eye(16) and K * G[4] + G[4] * K == sp.zeros(16, 16)
           and K.T * C + C * K == sp.zeros(16, 16))
factor_rules = (is_zero(sp.diff(F, x4) / F + v_g)
                and is_zero(sp.diff(power, x0) / f[0] - 4 * alpha * c_g * power))
```

`K_facts` holds the three matrix facts $K^2 = I_{16}$, $K\gamma^{(4)} + \gamma^{(4)}K = 0$ and $K^TC + CK = 0$ (the last says that the bilinear $\chi^\dagger C\chi$ is unchanged by the time evolution of the massless family; the record states it too). `factor_rules` holds $F'/F = -v_g$ and $(1/f_0)\partial_0(\sin^2 z)^{\alpha/2} = 4\alpha c_g(\sin^2 z)^{\alpha/2}$ (Section 8.31).

```python
Phi = sp.Matrix([sp.Function(f"phi{A}")(x4) for A in range(1, 17)])  # arbitrary
Psi_red = F * power * Phi
left_side = sum((gamma_up[mu] * (sp.diff(Psi_red, x[mu]) + Omega[mu] * Psi_red)
                 for mu in range(8)), sp.zeros(16, 1)) - m * Psi_red
right_side = F * power * G[4] * (sp.diff(Phi, x4) - (-m * G[4] + mu_A * K) * Phi)
check_record(K_facts and factor_rules
             and all(is_zero(v) for v in left_side - right_side),
             "K^2 = 1, {K, g4} = 0, K^T C + C K = 0; Psi = F (sin^2 z)^(alpha/2) Phi "
             "solves the equation iff Phi' = (-m g4 + mu_A K) Phi",
             "Revision/theory/reports/wolfram-field-theory.json",
             "solution_matrix_square",
             "K = gamma^(x4) gamma^(x0) satisfies K^2 = I16, {K, gamma^(x4)} = 0",
             "chi' = (-V gamma^(x4) + muA K) chi, muA = (3/2) H (4 al + 1) E^a4 "
             "b4^(-1/2)")
```

`Phi` is a column of sixteen arbitrary functions of the time. `left_side` is $\gamma^\mu D_\mu\Psi - m\Psi$ for $\Psi = F(\sin^2 z)^{\alpha/2}\Phi$, computed with all eight directions and the connection of In [2]; `right_side` is the reduced form $F(\sin^2 z)^{\alpha/2}\gamma^{(4)}[\Phi' - (-m\gamma^{(4)} + \mu_AK)\Phi]$. The check proves that the two are equal for every $\Phi$, together with the matrix facts and the factor rules, and requires the Wolfram record's text of the reduction (it writes `V` for the mass and `al` for $\alpha$).

```python
I_x4 = sp.Function("I")(x4)  # any function with I' = mu_A
chi0 = sp.Matrix(sp.symbols("q1:17"))  # 16 arbitrary constants
family_a = F * power * (sp.cosh(I_x4) * chi0 + sp.sinh(I_x4) * (K * chi0))
residual_a = sum((gamma_up[mu] * (sp.diff(family_a, x[mu]) + Omega[mu] * family_a)
                  for mu in range(8)), sp.zeros(16, 1))
residual_a = residual_a.subs(sp.Derivative(I_x4, x4), mu_A)  # I' = mu_A
check_record(all(is_zero(v) for v in residual_a),
             "(i-a) m = 0: F (sin^2 z)^(alpha/2) (cosh I + sinh I K) chi0 with I' = "
             "mu_A solves the equation", THEORY, "exact_solution_family_x4_x0",
             "(i-a) m = 0, alpha arbitrary: Psi = F (sin^2 z)^(alpha/2) (cosh I + "
             "sinh I K) chi with I' = (3/2) H (4 alpha + 1) e^a4 b4^(-1/2) solves "
             "gamma^mu D_mu Psi = 0 exactly")
```

Family (i-a): `I_x4` is an unknown function $I(x_4)$, `chi0` a column of sixteen constant symbols $q_1, \dots, q_{16}$, and `family_a` is $F(\sin^2 z)^{\alpha/2}(\cosh I + \sinh I\,K)\chi_0$. `residual_a` is $\gamma^\mu D_\mu\Psi$ for it ($m = 0$), with every $I'$ replaced by $\mu_A$ (`subs(sp.Derivative(I_x4, x4), mu_A)`); the check proves that it is zero.

```python
family_b = F * W(x0) ** sp.Rational(-3, 2) * (sp.cos(m * x4) * chi0
                                              - sp.sin(m * x4) * (G[4] * chi0))
residual_b = sum((gamma_up[mu] * (sp.diff(family_b, x[mu]) + Omega[mu] * family_b)
                  for mu in range(8)), sp.zeros(16, 1)) - m * family_b
check_record(all(is_zero(v) for v in residual_b),
             "(i-b) alpha = -1/4: F (sin^2 z)^(-1/8) (cos(m x4) - sin(m x4) g4) chi0 "
             "solves the equation", THEORY, "exact_solution_family_x4_x0",
             "(i-b) alpha = -1/4, m arbitrary: Psi = F (sin^2 z)^(-1/8) (cos(m x4) - "
             "sin(m x4) gamma^(x4)) chi solves gamma^mu D_mu Psi = m Psi exactly")
```

Family (i-b): $\alpha = -\frac14$, that is the factor $W^{-3/2} = (\sin^2 z)^{-1/8}$, and the time factor $\cos(mx_4) - \sin(mx_4)\gamma^{(4)}$; the check proves $\gamma^\mu D_\mu\Psi - m\Psi = 0$ for every mass.

```python
mu_1, mu_2 = sp.symbols("mu1 mu2", real=True)  # the values of mu_A at two times
M_1, M_2 = -m * G[4] + mu_1 * K, -m * G[4] + mu_2 * K
square_ok = (M_1 * M_1 - (mu_1**2 - m**2) * sp.eye(16)).applyfunc(sp.expand) \
    == sp.zeros(16, 16)
commutator_ok = (M_1 * M_2 - M_2 * M_1 - 2 * m * (mu_1 - mu_2) * G[4] * K).applyfunc(
    sp.expand) == sp.zeros(16, 16)
check_record(square_ok and commutator_ok,
             "M^2 = (mu_A^2 - m^2) I16; [M(1), M(2)] = 2 m (mu1 - mu2) g4 K is not 0",
             THEORY, "exact_solution_family_x4_x0",
             "For m != 0 and alpha != -1/4 the reduced system chi' = (-m gamma^(x4) + "
             "muA K) chi has no closed form for general a4, b4 (muA varies with x4)")
```

`mu_1` and `mu_2` stand for the values of $\mu_A$ at two times, and `M_1`, `M_2` for the matrices $M = -m\gamma^{(4)} + \mu_AK$ there. The check proves $M^2 = (\mu_A^2 - m^2)I_{16}$ and $[M_1, M_2] = 2m(\mu_1 - \mu_2)\gamma^{(4)}K$, which is not zero when $m \neq 0$ and $\mu_A$ changes: the matrices of different times do not commute, so the solution is not simply an exponential, and the record states that no closed form is known for general $a_4$, $b_4$. Output:

```text
PASS K^2 = 1, {K, g4} = 0, K^T C + C K = 0; Psi = F (sin^2 z)^(alpha/2) Phi solves the
    equation iff Phi' = (-m g4 + mu_A K) Phi
     reproduces Revision/theory/reports/wolfram-field-theory.json, check
    solution_matrix_square
PASS (i-a) m = 0: F (sin^2 z)^(alpha/2) (cosh I + sinh I K) chi0 with I' = mu_A solves
    the equation
     reproduces Revision/theory/reports/python-field-theory.json, check
    exact_solution_family_x4_x0
PASS (i-b) alpha = -1/4: F (sin^2 z)^(-1/8) (cos(m x4) - sin(m x4) g4) chi0 solves the
    equation
     reproduces Revision/theory/reports/python-field-theory.json, check
    exact_solution_family_x4_x0
PASS M^2 = (mu_A^2 - m^2) I16; [M(1), M(2)] = 2 m (mu1 - mu2) g4 K is not 0
     reproduces Revision/theory/reports/python-field-theory.json, check
    exact_solution_family_x4_x0
```

**In [6], which members have a finite norm, and when they grow.**

```python
p = 2 * alpha + sp.Rational(1, 2)  # the power of sin z in the norm density
antiderivative = sp.sin(z) ** p / (6 * H * p)
density = sp.cot(z) * sp.sin(z) ** p  # first half of a cell: sin z > 0, cot z > 0
log_antiderivative = sp.log(sp.sin(z)) / (6 * H)  # the case p = 0
eps = sp.Symbol("epsilon", positive=True)
norm_factor = (antiderivative.subs(x0, sp.pi / (12 * H))
               - antiderivative.subs(x0, 0)).subs(alpha, 0)  # the case alpha = 0
say(f"norm factor of the member alpha = 0: {sp.sstr(sp.simplify(norm_factor))}")
norm_ok = (is_zero(sp.diff(antiderivative, x0) - density)
           and is_zero(sp.diff(log_antiderivative, x0) - sp.cot(z))
           and sp.limit(log_antiderivative.subs(x0, eps), eps, 0, "+") == -sp.oo
           and sp.simplify(norm_factor - 1 / (3 * H)) == 0)
check_record(norm_ok, "norm factor 1/(3 H (4 alpha + 1)) for alpha > -1/4, 1/(3 H) "
             "at alpha = 0; infinite at alpha = -1/4", SCOPE,
             "good_sector_x0_independent_modes_without_boundary_condition",
             "int_0^(pi/(12 H)) cot(6 H x0) sin(6 H x0)^(1/2) dx0 = "
             f"{sp.sstr(sp.simplify(norm_factor))}")
```

`p` is the power $2\alpha + \frac12$ of $\sin z$ in the norm density, `antiderivative` is $\sin^pz/(6Hp)$ and `density` is $\cot z\sin^pz$ (first half of a cell); `log_antiderivative` is $\ln(\sin z)/(6H)$, the antiderivative for $p = 0$. `norm_factor` is the integral from the tip to the fold for $\alpha = 0$ (the antiderivative at $x_0 = \pi/(12H)$ minus its value at 0), printed. `norm_ok` collects four facts: the antiderivative is right; the logarithmic one is right; the latter goes to $-\infty$ at the tip (`sp.limit(..., eps, 0, "+")` is the limit as $\epsilon$ decreases to 0, so the norm of the member $\alpha = -\frac14$ is infinite); and the factor for $\alpha = 0$ is $1/(3H)$, the value that the record gives for the $x_0$-independent modes.

```python
# The record's numbers as exact fractions (nsimplify turns 1.3333333333333333 into 4/3):
A_record = sp.nsimplify(parameters["physics"]["historyA"])  # a4 = A H x4 ...
beta_record = sp.nsimplify(parameters["physics"]["historyBeta"])  # b4 = e^(beta ...)
b4_zero = sp.nsimplify(parameters["physics"]["historyB4AtZero"])  # b4(0) = 1
history = {a4: A_record * H * x4, b4: b4_zero * sp.exp(beta_record * A_record * H * x4)}
mu_history = sp.simplify(mu_A.subs(history).doit())
say(f"mu_A on the history: {mu_history}")
```

The history as exact fractions, and $\mu_A$ on it, printed.

```python
m_positive = sp.Symbol("m", positive=True)
onset = 3 * sp.log(2 * m_positive / (3 * H * (4 * alpha + 1))) / H  # mu_A = m there
s_var = sp.Symbol("s", real=True)
I_history = sp.integrate(mu_history.subs(x4, s_var), (s_var, 0, x4))
check(is_zero(mu_history - sp.Rational(3, 2) * H * (4 * alpha + 1) * sp.exp(H * x4 / 3))
      and is_zero(mu_history.subs(x4, onset) - m_positive),
      "on the history mu_A = (3/2) H (4 alpha + 1) e^(H x4/3); it reaches every m > 0 "
      "at x4 = (3/H) ln(2 m/(3 H (4 alpha + 1)))")
I_expected = sp.Rational(9, 2) * (4 * alpha + 1) * (sp.exp(H * x4 / 3) - 1)
check(is_zero(I_history - I_expected),
      "m = 0: I(x4) = (9/2)(4 alpha + 1)(e^(H x4/3) - 1), so e^I grows faster than "
      "any exponential")
```

`onset` is the time $\frac3H\ln\big(2m/(3H(4\alpha + 1))\big)$ at which $\mu_A = m$ (with a positive mass symbol), and `I_history` is $\int_0^{x_4}\mu_A\,ds$, computed by sympy's `integrate`. The two checks prove $\mu_A = \frac32H(4\alpha + 1)e^{Hx_4/3}$ on the history, $\mu_A = m$ at the onset, and $I(x_4) = \frac92(4\alpha + 1)(e^{Hx_4/3} - 1)$.

```python
times = np.linspace(-3.0, 6.0, 451)
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
for a_value, style in ((0.0, "-"), (0.5, "--"), (1.0, ":")):
    left.semilogy(times, 1.5 * (4 * a_value + 1) * np.exp(times / 3), style,
                  label=f"$\\mu_A$, $\\alpha = {a_value:g}$")
for mass_value in (1.0, 2.0, 4.0):
    left.axhline(mass_value, color="gray", linewidth=0.8)
    left.text(-2.9, mass_value * 1.08, f"$m = {mass_value:g}$", fontsize=8)
left.set_xlabel("time $x_4$ (units of $1/H$)")
left.set_ylabel("$\\mu_A = \\frac{3}{2}H(4\\alpha + 1)e^{Hx_4/3}$ (units of $H$)")
left.set_title("The coefficient overtakes every mass")
left.legend(fontsize=8, loc="lower right")
```

The left panel draws $\mu_A$ for $\alpha = 0, 0.5, 1$ against 451 times from $-3$ to $6$ on a logarithmic axis, and gray lines with labels for the masses $m = 1, 2, 4$.

```python
late = np.linspace(0.0, 15.0, 301)
for a_value, style in ((0.0, "-"), (0.5, "--"), (1.0, ":")):
    exponent_I = 4.5 * (4 * a_value + 1) * (np.exp(late / 3) - 1)
    right.semilogy(late[1:], exponent_I[1:] / np.log(10.0), style,
                   label=f"$\\alpha = {a_value:g}$")
right.semilogy(late[1:], late[1:] / np.log(10.0), color="gray", linewidth=0.8,
               label="$e^{x_4}$ for comparison")
right.set_xlabel("time $x_4$ (units of $1/H$)")
right.set_ylabel("$\\log_{10}$ of the growth factor $e^{I}$")
right.set_title("$m = 0$: the exact members (i-a)")
right.legend(fontsize=8);
```

The right panel draws, for 301 times from 0 to 15, the base-10 logarithm of the growth factor $e^{I}$ of the massless members, $I/\ln 10$, for the same three exponents, and for comparison the exponential $e^{x_4}$ (gray), all on a logarithmic axis (the first time, 0, is left out with `[1:]`, because the logarithm of 0 does not exist).

```python
save_figure(fig, "family_growth",
            "Left: the coefficient $\\mu_A = \\frac32H(4\\alpha + 1)e^{Hx_4/3}$ of "
...)
```

Figure 08d.2. Output:

```text
norm factor of the member alpha = 0: 1/(3*H)
PASS norm factor 1/(3 H (4 alpha + 1)) for alpha > -1/4, 1/(3 H) at alpha = 0; infinite
    at alpha = -1/4
     reproduces Revision/theory/reports/python-scope.json, check
    good_sector_x0_independent_modes_without_boundary_condition
mu_A on the history: 3*H*(4*alpha + 1)*exp(H*x4/3)/2
PASS on the history mu_A = (3/2) H (4 alpha + 1) e^(H x4/3); it reaches every m > 0 at x4
    = (3/H) ln(2 m/(3 H (4 alpha + 1)))
PASS m = 0: I(x4) = (9/2)(4 alpha + 1)(e^(H x4/3) - 1), so e^I grows faster than any
    exponential
Figure 08d.2 saved as Revision/textbook/figures/08d_2_family_growth.png
```

**What Figure 08d.2 shows.** Left: on the logarithmic axis the three lines $\mu_A = 1.5e^{x_4/3}$, $4.5e^{x_4/3}$ and $7.5e^{x_4/3}$ ($\alpha = 0, 0.5, 1$) are straight and rising; each crosses every gray mass line, the line $\alpha = 0$ for example at $x_4 = 3\ln\frac23 \approx -1.22$ ($m = 1$), $3\ln\frac43 \approx 0.86$ ($m = 2$) and $3\ln\frac83 \approx 2.94$ ($m = 4$). Right: the logarithm of $\log_{10}e^{I}$ approaches straight lines, so $\log_{10}e^I$ itself grows exponentially: at $x_4 = 15$ the member $\alpha = 0$ has grown by the factor $10^{288}$ ($I = 4.5(e^5 - 1) \approx 663$), while $e^{x_4}$ reaches only $10^{6.5}$ and its gray curve bends down.

**In [7], when the members start to grow.**

```python
masses = np.linspace(0.05, 6.0, 240)
A_grid, M_grid = np.meshgrid(np.linspace(-1.0, 1.5, 251), masses)
coefficient = 1.5 * np.abs(4 * A_grid + 1)  # |mu_A| at x4 = 0, H = 1
with np.errstate(divide="ignore"):
    onset_grid = 3 * np.log(M_grid / coefficient)  # the time at which mu_A^2 = m^2
```

A grid of 240 masses from 0.05 to 6 and 251 exponents from $-1$ to $1.5$ (`np.meshgrid` makes two arrays with the exponent and the mass at every grid point). `coefficient` is $|\mu_A|$ at $x_4 = 0$ for $H = 1$, and `onset_grid` the time $3\ln(m/|\mu_A(0)|)$ at which $|\mu_A| = m$; at $\alpha = -\frac14$ the coefficient is 0 and the division gives infinity, and `np.errstate(divide="ignore")` keeps numpy from printing a warning about it.

```python
fig, ax = plt.subplots(figsize=(6.6, 4.8))
shown = np.clip(onset_grid, -6.0, 9.0)
image = ax.pcolormesh(M_grid, A_grid, shown, cmap="viridis", shading="auto")
fig.colorbar(image, ax=ax, label="onset time $x_4$ (units of $1/H$)")
ax.contour(M_grid, A_grid, onset_grid, levels=[0.0], colors="white", linewidths=1.0)
ax.axhspan(-1.0, -0.25, facecolor="none", edgecolor="white", hatch="//",
           linewidth=0.0)
ax.axhline(-0.25, color="black", linewidth=1.2)
ax.axhline(0.0, color="tab:red", linewidth=1.2)
ax.text(0.2, -0.6, "infinite norm at the tip", fontsize=9, color="white",
        bbox={"facecolor": "black", "alpha": 0.5, "edgecolor": "none"})
ax.text(3.2, 0.05, "$\\alpha = 0$", fontsize=8, color="tab:red")
ax.set_xlabel("mass $m$ (units of $H$)")
ax.set_ylabel("exponent $\\alpha$")
ax.set_title("When the members start to grow on the history")
```

One panel. `pcolormesh` colours the plane with the onset time, clipped to the range from $-6$ to $9$ (`np.clip`); `contour(..., levels=[0.0])` draws the white curve where the onset is at $x_4 = 0$; `axhspan` hatches the band $\alpha \le -\frac14$; the black line marks $\alpha = -\frac14$ and the red line $\alpha = 0$; two texts label them (`bbox` puts a dark box behind the white text).

```python
finite = np.isfinite(onset_grid) | (np.abs(4 * A_grid + 1) < 1e-12)
early = float(np.mean((onset_grid < 0.0) & (A_grid > -0.25)))
report("fraction of the rectangle with finite norm that grows already at x4 = 0",
       f"{early:.4f}")
check(bool(np.all(finite)), "every drawn member with alpha != -1/4 starts to grow "
      "at a finite time")
save_figure(fig, "growing_finite_norm",
...)
```

`finite` is true where the onset time is finite or the exponent is $-\frac14$; `early` is the fraction of the grid points with a finite norm ($\alpha > -\frac14$) whose onset is before $x_4 = 0$, printed. The check requires every drawn member with $\alpha \neq -\frac14$ to start growing at a finite time. Figure 08d.3. Output:

```text
RESULT fraction of the rectangle with finite norm that grows already at x4 = 0 = 0.4983
PASS every drawn member with alpha != -1/4 starts to grow at a finite time
Figure 08d.3 saved as Revision/textbook/figures/08d_3_growing_finite_norm.png
```

**What Figure 08d.3 shows.** The colour (the onset time) changes smoothly across the plane: dark (early onset) at small masses and at large $|4\alpha + 1|$, bright (late onset) at large masses near the line $\alpha = -\frac14$, where $|\mu_A|$ is small. Left of the white curve the members grow already at $x_4 = 0$ (about half of the drawn finite-norm rectangle, 0.4983). The hatched band below $\alpha = -\frac14$ has an infinite norm at the tip; on the black line the members never grow. Every point with a finite norm has a finite onset time.

**In [8], the $x_0$-independent modes of the good sector.**

```python
def h_of(column):
    """The mode operator h applied to a column of functions of x4 and x0 (U = 0)."""
    return (-sp.I * m * G[4] * column
            + sp.I * G[4] * G[0] * sp.exp(a4) / sp.sqrt(b4)
            * (sp.tan(z) * sp.diff(column, x0) + sp.Rational(3, 2) * H * column)
            - sp.I * v_g * column)
```

`h_of` applies the mode operator $h = -im\gamma^{(4)} + i\gamma^{(4)}\gamma^{(0)}e^{a_4}b_4^{-1/2}(\tan z\,\partial_0 + \frac32H) - iv_g$ of Section 8.32 to a column of functions of $x_4$ and $x_0$ (`sp.I` is the imaginary unit).

```python
A_mat = -sp.I * m * G[4] + sp.I * c_g * G[4] * G[0]  # the matrix A(x4)
chi_t = sp.Matrix([sp.Function(f"c{n}")(x4) for n in range(1, 17)])  # arbitrary
Psi_t = F * chi_t  # an x0-independent field
action_ok = all(is_zero(v) for v in h_of(Psi_t) - (A_mat - sp.I * v_g * sp.eye(16))
                * Psi_t)
reduced_ok = all(is_zero(v) for v in sp.I * sp.diff(Psi_t, x4) - h_of(Psi_t)
                 - F * (sp.I * sp.diff(chi_t, x4) - A_mat * chi_t))
check(action_ok and reduced_ok, "h Psi = (A - i v_g) Psi on x0-independent Psi, and "
      "i d4 Psi = h Psi is i d4 chi = A chi for Psi = F chi")
```

`A_mat` is $A = -im\gamma^{(4)} + ic_g\gamma^{(4)}\gamma^{(0)}$; `chi_t` a column of sixteen arbitrary functions of the time and `Psi_t` $= F\chi$, an $x_0$-independent field. The check proves $h\Psi = (A - iv_g)\Psi$ and that $i\partial_4\Psi = h\Psi$ is equivalent to $i\partial_4\chi = A\chi$ (the difference of the two equations is $F$ times the difference of the reduced ones).

```python
m_s, cg_s = sp.symbols("m c_g", real=True)  # the mass and c_g as plain real numbers
A_plain = -sp.I * m_s * G[4] + sp.I * cg_s * G[4] * G[0]
A_zero = A_plain.subs({m_s: 1, cg_s: sp.Rational(3, 2)})  # m = H = 1 at x4 = 0
dimension = 16 - (A_zero - sp.sqrt(5) / 2 * sp.I * sp.eye(16)).rank()
report("dimension of the eigenspace of +sqrt(5)/2 i at m = H = 1, x4 = 0", dimension)
cg_history = sp.simplify(c_g.subs(history).doit())
say(f"c_g on the history: {cg_history}")
```

`A_plain` is the same matrix with plain real symbols for $m$ and $c_g$, and `A_zero` its value at $m = 1$, $c_g = \frac32$ (that is $m = H = 1$ at $x_4 = 0$). `dimension` is the dimension of the eigenspace of $\frac{\sqrt5}{2}i$, 16 minus the rank of $A - \frac{\sqrt5}{2}i\,I_{16}$, printed; `cg_history` is $c_g$ on the history, printed too.

```python
all_true = (A_plain != A_plain.H
            and (A_plain * A_plain - (m_s**2 - cg_s**2) * sp.eye(16)).applyfunc(
                sp.expand) == sp.zeros(16, 16)
            and A_zero * A_zero == -sp.Rational(5, 4) * sp.eye(16) and dimension == 8
            and is_zero(cg_history - sp.Rational(3, 2) * H * sp.exp(H * x4 / 3)))
check_record(all_true, "A = -i m g4 + i c_g g4 g0 is not Hermitian, A^2 = (m^2 - c_g^2) "
             "I16; c_g = (3/2) H e^(H x4/3) on the history; +-sqrt(5)/2 i at m = H = 1",
             SCOPE, "good_sector_x0_independent_modes_without_boundary_condition",
             "so Psi = e^(a4/2) b4^(-1) chi with i d4 chi = A chi",
             "A = -i m gamma^(x4) + i cg gamma^(x4) gamma^(x0), which is not "
             "Hermitian, and A^2 = (m^2 - cg^2) I16 exactly",
             "cg = (3/2) H e^(H x4/3) grows, so every mass falls below it at late x4")
```

`all_true` collects: $A$ is not equal to its conjugate transpose (`.H`), so it is not Hermitian; $A^2 = (m^2 - c_g^2)I_{16}$; at $m = 1$, $c_g = \frac32$ the square is $-\frac54I_{16}$ and the eigenspace has dimension 8; and $c_g = \frac32He^{Hx_4/3}$ on the history. The check requires the record's three texts. Output:

```text
PASS h Psi = (A - i v_g) Psi on x0-independent Psi, and i d4 Psi = h Psi is i d4 chi = A
    chi for Psi = F chi
RESULT dimension of the eigenspace of +sqrt(5)/2 i at m = H = 1, x4 = 0 = 8
c_g on the history: 3*H*exp(H*x4/3)/2
PASS A = -i m g4 + i c_g g4 g0 is not Hermitian, A^2 = (m^2 - c_g^2) I16; c_g = (3/2) H
    e^(H x4/3) on the history; +-sqrt(5)/2 i at m = H = 1
     reproduces Revision/theory/reports/python-scope.json, check
    good_sector_x0_independent_modes_without_boundary_condition
```

**In [9], the eigenvalues of $A$ along the history.**

```python
g4_number = np.array(G[4], dtype=float)  # gamma^(x4) as numbers
g4g0_number = np.array(G[4] * G[0], dtype=float)  # gamma^(x4) gamma^(x0), real symmetric


def cg_of(x4_value):
    """c_g = (3/2) H e^(H x4/3) on the history, H = 1."""
    return 1.5 * np.exp(x4_value / 3)


def A_number(mass_value, x4_value):
    """The matrix A = -i m gamma^(x4) + i c_g gamma^(x4) gamma^(x0) at time x4."""
    return -1j * mass_value * g4_number + 1j * cg_of(x4_value) * g4g0_number
```

The two matrices $\gamma^{(4)}$ and $\gamma^{(4)}\gamma^{(0)}$ as floating-point arrays, $c_g = \frac32e^{x_4/3}$ on the history ($H = 1$) as a function, and the matrix $A$ for a given mass and time.

```python
path_times = np.linspace(-2.0, 3.0, 51)
points = np.concatenate([np.linalg.eigvals(A_number(2.0, t)) for t in path_times])
expected_size = np.repeat(np.sqrt(np.abs(4.0 - cg_of(path_times) ** 2)), 16)
onset_m2 = 3 * np.log(4.0 / 3.0)  # c_g = m = 2
report("time at which c_g = m = 2 on the history, 3 ln(4/3)", f"{onset_m2:.6f}")
check(np.max(np.abs(np.abs(points) - expected_size)) < 1e-9,
      "the eigenvalues of A(x4) are +-sqrt(m^2 - c_g^2) at every time (m = 2)")
```

For $m = 2$ and 51 times from $-2$ to $3$ the sixteen eigenvalues of $A$ are computed (`np.linalg.eigvals`) and joined into one array (`np.concatenate`); `expected_size` is $\sqrt{|m^2 - c_g^2|}$, repeated sixteen times for each time (`np.repeat`). The onset time $3\ln(4/3)$, where $c_g = m = 2$, is printed, and the check requires the size of every eigenvalue to be $\sqrt{|m^2 - c_g^2|}$ to $10^{-9}$.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
fig.subplots_adjust(wspace=0.55)  # room for the colour bar and the right label
dots = left.scatter(points.real, points.imag, c=np.repeat(path_times, 16),
                    cmap="plasma", s=20)
fig.colorbar(dots, ax=left, label="time $x_4$ (units of $1/H$)")
left.set_aspect("equal")
left.set_xlim(-4.0, 4.0)
left.set_ylim(-4.0, 4.0)
left.set_xlabel("real part")
left.set_ylabel("imaginary part")
left.set_title("Eigenvalues of $A(x_4)$, $m = 2$, $H = 1$")
```

The left panel draws the eigenvalues in the complex plane as dots (`scatter`), coloured by the time with the colour map `plasma` and a colour bar; `set_aspect("equal")` makes the two axes equally scaled.

```python
fine = np.linspace(-3.0, 6.0, 901)
for mass_value, style in ((0.5, "-"), (1.0, "--"), (2.0, ":"), (4.0, "-.")):
    rate = np.sqrt(np.maximum(cg_of(fine) ** 2 - mass_value**2, 0.0))
    right.plot(fine, rate, style, label=f"$m = {mass_value:g}$")
right.set_xlabel("time $x_4$ (units of $1/H$)")
right.set_ylabel("growth rate $\\sqrt{c_g^2 - m^2}$ (units of $H$)")
right.set_title("Every mass is overtaken")
right.legend();
```

The right panel draws the instantaneous growth rate $\sqrt{c_g^2 - m^2}$ (zero while $c_g < m$; `np.maximum(..., 0.0)` keeps the square root real) against 901 times from $-3$ to $6$ for four masses.

```python
save_figure(fig, "good_sector_modes",
            "Left: the eigenvalues $\\pm\\sqrt{m^2 - c_g^2}$ of the matrix $A = "
...)
```

Figure 08d.4. Output:

```text
RESULT time at which c_g = m = 2 on the history, 3 ln(4/3) = 0.863046
PASS the eigenvalues of A(x4) are +-sqrt(m^2 - c_g^2) at every time (m = 2)
Figure 08d.4 saved as Revision/textbook/figures/08d_4_good_sector_modes.png
```

**What Figure 08d.4 shows.** Left: the dots of the early times lie on the real axis near $\pm1.85$ (at $x_4 = -2$, $c_g = 1.5e^{-2/3} \approx 0.77$ and $\sqrt{4 - 0.59} \approx 1.85$) and move inwards as the time grows; they meet at 0 at $x_4 \approx 0.863$ and then move out along the imaginary axis, to about $\pm3.55i$ at $x_4 = 3$ ($c_g = 1.5e \approx 4.08$). Right: the curve of $m = 0.5$ is positive from the start ($c_g > 0.5$ already at $x_4 = -3$); those of $m = 1$, 2 and 4 leave zero at $3\ln\frac23 \approx -1.22$, $0.86$ and $3\ln\frac83 \approx 2.94$ and then rise like $c_g$. Every mass is overtaken.

**In [10], the boundary term at the fold.**

```python
M0 = sp.I * G[4] * G[0]
P = sp.I * sp.exp(a4) / sp.sqrt(b4) * sp.tan(z) * G[4] * G[0]  # the matrix of d0
real_rates = {sp.conjugate(a4_prime): a4_prime, sp.conjugate(b4_prime): b4_prime}
flux_weight = sigma * b4 ** sp.Rational(3, 2) * W(x0) ** 3  # sigma b4^(3/2) W^3
```

`M0` is $M_0 = i\gamma^{(4)}\gamma^{(0)}$ and `P` the coefficient $P = ie^{a_4}b_4^{-1/2}\tan z\,\gamma^{(4)}\gamma^{(0)}$ of $\partial_0$ in $h$. `real_rates` tells sympy that $a_4'$ and $b_4'$ are real: it replaces their complex conjugates (which appear when a conjugate transpose is taken) by themselves. `flux_weight` is $\sigma b_4^{3/2}W^3$.

```python
fact_1 = (P + P.H).applyfunc(sp.simplify) == sp.zeros(16, 16)
fact_2 = all(is_zero(v) for v in sqrt_g * P - flux_weight * M0)
fact_3 = all(is_zero(v) for v in sqrt_g * (A_mat - A_mat.H)
             - sp.diff(flux_weight, x0) * M0)
fact_4 = is_zero((sqrt_g * (-sp.I * v_g - sp.conjugate(-sp.I * v_g))
                  + sp.I * sp.diff(sqrt_g, x4)).xreplace(real_rates))
```

The four matrix facts of Section 8.32: $P + P^\dagger = 0$; $\sqrt{|g|}P = \sigma b_4^{3/2}W^3M_0$; $\sqrt{|g|}(A - A^\dagger) = \partial_0(\sigma b_4^{3/2}W^3)M_0$; and $\sqrt{|g|}(-iv_g - (-iv_g)^\ast) = -i\partial_4\sqrt{|g|}$.

```python
u_col = sp.Matrix([(A_ + 1) + sp.I * (2 * A_ - 3) * x0 + (A_ - 5) * x0**2 / 3
                   for A_ in range(16)])  # a column of polynomials in x0
v_col = sp.Matrix([(3 - A_) * x0 + sp.I * (A_ + 2) + sp.I * A_ * x0**3 / 7
                   for A_ in range(16)])
left_flux = (sqrt_g * ((u_col.H * h_of(v_col))[0] - (h_of(u_col).H * v_col)[0])
             ).xreplace(real_rates)
right_flux = (sp.diff(flux_weight * (u_col.H * M0 * v_col)[0], x0)
              - sp.I * sp.diff(sqrt_g, x4) * (u_col.H * v_col)[0])
```

Two explicit columns `u_col` and `v_col` of sixteen polynomials in $x_0$ with complex coefficients (built with a list comprehension over $A = 0, \dots, 15$). `left_flux` is $\sqrt{|g|}[u^\dagger(hv) - (hu)^\dagger v]$ (`(u_col.H * h_of(v_col))[0]` is the single entry of the $1 \times 1$ matrix $u^\dagger(hv)$), and `right_flux` the right side of the boundary identity, $\partial_0(\sigma b_4^{3/2}W^3u^\dagger M_0v) - i(\partial_4\sqrt{|g|})u^\dagger v$.

```python
u0 = (G[4] * G[0] - sp.eye(16)).nullspace()[0]  # gamma^(4) gamma^(0) u0 = u0
flux = sp.simplify((u0.H * M0 * u0)[0])
size_u0 = (u0.H * u0)[0]
report("u0^dagger M0 u0 and u0^dagger u0", f"{flux}, {size_u0}")
```

`u0` is a column with $\gamma^{(4)}\gamma^{(0)}u_0 = u_0$: the first basis vector of the null space of $\gamma^{(4)}\gamma^{(0)} - I_{16}$ (`nullspace()` returns a list of independent columns $v$ with $(\gamma^{(4)}\gamma^{(0)} - I_{16})v = 0$). `flux` is $u_0^\dagger M_0u_0$ and `size_u0` is $u_0^\dagger u_0$; both are printed.

```python
# The record states the same identity and the same flux (sympy writes i as I):
check_record(fact_1 and fact_2 and fact_3 and fact_4
             and is_zero(left_flux - right_flux) and flux == 2 * sp.I and size_u0 == 2,
             "sqrt|g| (u^dagger h v - (h u)^dagger v) = d0(sigma b4^(3/2) (sin^2 "
             "z)^(1/4) u^dagger M0 v) - i (d4 sqrt|g|) u^dagger v; at the fold "
             "u0^dagger M0 u0 = 2 i", SCOPE,
             "good_sector_hermiticity_up_to_the_brane_flux",
             "sqrt|g| [u^dagger (h v) - (h u)^dagger v] = d_x0(sgn b4^(3/2) (sin^2 "
             "z)^(1/4) u^dagger M0 v) - i (d_x4 sqrt|g|) u^dagger v",
             f"u^dagger M0 u = {sp.sstr(flux)} (|u|^2 = {sp.sstr(size_u0)})")
```

The check requires the four facts, the identity for the two columns, the values $u_0^\dagger M_0u_0 = 2i$ and $u_0^\dagger u_0 = 2$, and the record's texts (sympy writes $i$ as `I`, so the record's detail contains `2*I`). Output:

```text
RESULT u0^dagger M0 u0 and u0^dagger u0 = 2*I, 2
PASS sqrt|g| (u^dagger h v - (h u)^dagger v) = d0(sigma b4^(3/2) (sin^2 z)^(1/4) u^dagger
    M0 v) - i (d4 sqrt|g|) u^dagger v; at the fold u0^dagger M0 u0 = 2 i
     reproduces Revision/theory/reports/python-scope.json, check
    good_sector_hermiticity_up_to_the_brane_flux
```

**In [11], a growing mode is fed through the fold.**

```python
rng = np.random.default_rng(12345)  # fixed seed: the same column in every run
chi_start = rng.normal(size=16)  # a real column (the equation is real)
chi_start = chi_start / np.linalg.norm(chi_start)


def rate_of(x4_value, column, mass_value=2.0):
    """d chi/dx4 = (-m gamma^(x4) + c_g gamma^(x4) gamma^(x0)) chi on the history."""
    return (-mass_value * g4_number + cg_of(x4_value) * g4g0_number) @ column
```

A fixed random column: `np.random.default_rng(12345)` is numpy's random-number generator with the fixed seed 12345 (so that every run uses the same numbers), `rng.normal(size=16)` draws sixteen numbers from the normal distribution, and the column is divided by its length. `rate_of` is the right-hand side of $d\chi/dx_4 = -iA\chi = (-m\gamma^{(4)} + c_g\gamma^{(4)}\gamma^{(0)})\chi$ on the history, with $m = 2$ (a real equation, so real columns suffice).

```python
steps = 4000
step = 4.0 / steps
times = np.linspace(0.0, 4.0, steps + 1)
states = [chi_start]
for n in range(steps):  # the classical RK4 method
    t_n, u = times[n], states[-1]
    s1 = rate_of(t_n, u)
    s2 = rate_of(t_n + step / 2, u + step / 2 * s1)
    s3 = rate_of(t_n + step / 2, u + step / 2 * s2)
    s4 = rate_of(t_n + step, u + step * s3)
    states.append(u + step / 6 * (s1 + 2 * s2 + 2 * s3 + s4))
states = np.array(states)
```

RK4 with 4000 steps of length 0.001 from $x_4 = 0$ to 4; `states` collects the columns (`states[-1]` is the last one), and `np.array(states)` turns the list into a $4001 \times 16$ array.

```python
norms = np.einsum("ij,ij->i", states, states) / 3.0  # N = chi^dagger chi/(3 H)
fluxes = np.exp(times / 3) * np.einsum("ij,jk,ik->i", states, g4g0_number, states)
# dN/dx4 by the five-point difference formula (its error shrinks like step^4):
slopes = (-norms[4:] + 8 * norms[3:-1] - 8 * norms[1:-3] + norms[:-4]) / (12 * step)
inner = fluxes[2:-2]  # the flux at the same times
agreement = np.max(np.abs(slopes - inner) / np.maximum(np.abs(inner), 1.0))
```

`norms` is $N = \chi^\dagger\chi/(3H)$ at every time (`np.einsum("ij,ij->i", states, states)` adds the squares of each row) and `fluxes` the flux $e^{a_4}b_4^{-1/2}\chi^\dagger\gamma^{(4)}\gamma^{(0)}\chi$ through the fold ($e^{x_4/3}$ on the history; the `einsum` computes $\chi^T(\gamma^{(4)}\gamma^{(0)})\chi$ row by row). `slopes` is $dN/dx_4$ by the five-point difference formula $\big(-N(x_4 + 2s) + 8N(x_4 + s) - 8N(x_4 - s) + N(x_4 - 2s)\big)/(12s)$ with the step $s$, whose error shrinks like $s^4$, for the times from the third to the third last (the shifted slices `norms[4:]`, `norms[3:-1]`, `norms[1:-3]`, `norms[:-4]` are $N(x_4 + 2s)$, $N(x_4 + s)$, $N(x_4 - s)$, $N(x_4 - 2s)$), `inner` the flux at the same times, and `agreement` the largest relative difference (relative to $\max(|{\rm flux}|, 1)$).

```python
report("largest relative difference of dN/dx4 and the flux", f"{agreement:.1e}")
check(agreement < 1e-8, "dN/dx4 equals the flux through the fold at every x4 (to the "
      "accuracy of the difference formula)")
report("N(4) / N(0)", f"{norms[-1] / norms[0]:.6e}")
check(norms[-1] / norms[0] > 1e4, "the norm grows by more than a factor 10^4")
```

The agreement and the growth factor $N(4)/N(0)$ are printed; the checks require an agreement better than $10^{-8}$ and growth by more than $10^4$.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
left.semilogy(times, norms)
left.axvline(3 * np.log(4.0 / 3.0), color="gray", linestyle=":", linewidth=0.9)
left.set_xlabel("time $x_4$ (units of $1/H$)")
left.set_ylabel("norm $N(x_4)$")
left.set_title("The $x_0$-independent mode, $m = 2$, $H = 1$")
right.plot(times[2:-2], slopes, label="$dN/dx_4$ (five-point differences)")
right.plot(times[::200], fluxes[::200], "o", color="black", markersize=4,
           label="flux at the fold $z = \\pi/2$")
right.axhline(0.0, color="black", linewidth=0.8)
right.set_yscale("symlog", linthresh=1.0)  # linear between -1 and 1, log outside
right.set_ylim(-1.5, 3.0e9)
right.set_xlabel("time $x_4$ (units of $1/H$)")
right.set_ylabel("rate (units of $H$)")
right.set_title("Rate of change of the norm = flux")
right.legend();
```

Two panels: the norm on a logarithmic axis with a dotted line at the onset $3\ln(4/3)$; and $dN/dx_4$ (line) with the flux at every 200th time (dots) on a `symlog` axis, which is linear between $-1$ and $1$ (`linthresh=1.0`) and logarithmic outside, so that it can show negative and very large values together.

```python
save_figure(fig, "norm_and_flux",
            "An $x_0$-independent mode of the good sector, $\\Psi = e^{a_4/2}"
...)
```

Figure 08d.5. Output:

```text
RESULT largest relative difference of dN/dx4 and the flux = 5.9e-10
PASS dN/dx4 equals the flux through the fold at every x4 (to the accuracy of the
    difference formula)
RESULT N(4) / N(0) = 1.569834e+08
PASS the norm grows by more than a factor 10^4
Figure 08d.5 saved as Revision/textbook/figures/08d_5_norm_and_flux.png
```

The difference formula agrees with the flux to $5.9 \times 10^{-10}$ (relative), and the norm grows by the factor $1.57 \times 10^8$ in four time units.

**What Figure 08d.5 shows.** Left: the norm starts at $\frac13$ (a unit column gives $N = 1/(3H)$), dips slightly during the first tenth of a time unit (the flux is negative there), rises to about 2 at the onset (the dotted line at $x_4 \approx 0.86$) and then ever more steeply on the logarithmic axis, to about $5 \times 10^7$ at $x_4 = 4$. Right: the line $dN/dx_4$ and the black dots of the flux at the fold coincide at every time, from about $-0.5$ at $x_4 = 0$ to about $6 \times 10^8$ at $x_4 = 4$: the norm changes only through the fold.

**In [12], the last check.**

```python
for name in ("08d_1_rescaling_factors.png", "08d_2_family_growth.png",
             "08d_3_growing_finite_norm.png", "08d_4_good_sector_modes.png",
             "08d_5_norm_and_flux.png"):
    check(output_file(f"{FIGURE_FOLDER}/{name}").is_file(),
          f"the figure file {name} exists")
all_checks_passed()
```

Five checks that the figure files exist, and the last line. The 27 checks come from the cells as follows: three in In [2], four in In [3], one in In [4], four in In [5], three in In [6], one in In [7], two in In [8], one in In [9], one in In [10], two in In [11] and five here. Output:

```text
PASS the figure file 08d_1_rescaling_factors.png exists
PASS the figure file 08d_2_family_growth.png exists
PASS the figure file 08d_3_growing_finite_norm.png exists
PASS the figure file 08d_4_good_sector_modes.png exists
PASS the figure file 08d_5_norm_and_flux.png exists
ALL 27 CHECKS PASSED (notebook 08d)
```

### 8.37 The exact scope of non-triviality and of the evolution, in one table

Every statement of the chapter in one place. The last column names the Revision check, the short name of its report file in brackets, and the notebook that reproduces it. The report files are these:

```text
Revision/theory/reports/python-field-theory.json     (python-field-theory)
Revision/theory/reports/wolfram-field-theory.json    (wolfram-field-theory)
Revision/theory/reports/python-scope.json            (python-scope)
Revision/theory/reports/wolfram-scope.json           (wolfram-scope)
Revision/pairing/reports/python-pairing.json         (python-pairing)
Revision/dark_sector/dirac16complex/reports/derivation-checks.json   (dark-sector)
```

Every exact statement holds for all functions $a_4$ and $b_4 > 0$ and every real $z$ between the degenerate points; the rows that need the history say so. The other half of the author's requirement, that the field equations be self-consistent, is treated in Section 7.23, in the six senses (i) to (vi) of the record; this chapter treats sense (ii), the evolution, in full.

| statement | status | Revision check; notebook |
| --- | --- | --- |
| the corrected metric from the diagonal frame; $\sqrt{\lvert g\rvert} = e^{-a_4}b_4^2\lvert\cot z\rvert(\sin^2 z)^{1/4}$; 21 Christoffel symbols; 10 components of the spin connection | PROVED | `metric_from_vielbein_equals_SPEC`, `sqrt_det_g`, `christoffel_symmetric_metric_compatible` (python-field-theory); `christoffel_count`, `omega_components` (wolfram-field-theory); 08c |
| diagonal frame: $\gamma^\mu\Omega_\mu = G = c_g\gamma^{(0)} + v_g\gamma^{(4)}$, $c_g = \frac32He^{a_4}b_4^{-1/2}$, $v_g = b_4'/b_4 - a_4'/2$; the $\pm\frac12a_4'$ pieces of 3-space and of the extra times cancel, the hidden block shares the rate $h_4$, the extra times give the $\gamma^{(0)}$ pieces | PROVED | `gamma_mu_Omega_mu_equals_hidden_block_terms`, `per_direction_terms` (python-field-theory); `gammaOmega_total`, `gammaOmega_per_direction` (wolfram-field-theory); 08c, 08d |
| $GG = (c_g^2 - v_g^2)I_{16}$, so $G\Psi \neq 0$ for every $\Psi \neq 0$ where $c_g^2 \neq v_g^2$ (on the history $H^2(\frac94e^{2Hx_4/3} - \frac{25}{36}) > 0$ for $x_4 \geq 0$) | PROVED | `gravity_term_square` (python-field-theory); `nontriviality_1_dirac16complex`, `nontriviality_2_dirac16complex00` (wolfram-field-theory); 08c |
| $\Omega_\mu = 0$ for every $\mu$ only if $a_4' = 0$, $b_4' = 0$ and $H = 0$ (not a member of the family) | PROVED | `nontriviality_Omega_zero_iff_flat` (python-field-theory); `Omega_vanishes_iff_a4prime_b4prime_and_H_vanish` (wolfram-field-theory); 08c |
| the term sees the deflating hidden block; the metric is flat for $a_4 = 0$, $b_4 = H^2x_4^2$ and curved on the history ($R^{x_1}{}_{x_1} = \frac53H^2$) | PROVED | `gammaOmega_sees_the_hidden_block` (python-scope); `ricci_mixed_components`, `flat_member_and_curvature` (wolfram-field-theory); `curvature_and_flat_member` (python-field-theory); 08c |
| the connection drops out of the Lagrangian; the term is the half-density term | PROVED | `connection_free_lagrangian_same_equations` (python-scope); `divergence_of_sqrtg_gamma` (python-field-theory); 08c |
| boosted frame: $\gamma'^\mu\Omega'_\mu = (c_g - \frac{b'}{2})(\cosh b\,\gamma^{(0)} - \sinh b\,\gamma^{(4)}) + v_g(\cosh b\,\gamma^{(4)} - \sinh b\,\gamma^{(0)})$; for $b' = 2c_g$ only the part $v_g$ is left, and no boost of this kind removes it | PROVED | `boosted_frame_gammaOmega_formula`, `boosted_frame_removes_only_the_H_term` (python-scope, wolfram-scope); 08c |
| where the metric is curved the spin connection vanishes in no frame: its curvature is the Riemann tensor | PROVED | `boosted_frame_curvature_nonzero` (python-scope); `spinor_curvature_equals_riemann` (python-field-theory); 08c |
| the connection enters the energy-momentum tensor ($K^{x_4}{}_{x_5}$, not $K^{x_4}{}_{x_1}$) | PROVED | `spin_connection_in_the_energy_momentum_tensor` (python-scope); 08c |
| the rescaling $\Psi = e^{a_4/2}b_4^{-1}(\sin^2 z)^{-1/8}\chi$ removes the term; for $U \neq 0$ it becomes $\lambda e^{a_4}S[\chi]/(b_4^2\lvert\sin z\rvert^{1/2})$ | PROVED | `rescaling_removes_the_connection_term`, `rescaled_equation_quadratic_potential` (python-scope); 08d |
| the slices $x_4 = $ const are non-characteristic | PROVED | `evolution_form_G` (wolfram-field-theory); 08a |
| $h_k^2 = E^2I_{16}$; the growth rates of extra-time waves have no upper bound; in flat 4+4 space and with frozen coefficients the Cauchy problem is not well posed in Hadamard's sense | PROVED | `extra_time_growth_rates_unbounded` (python-scope, wolfram-scope); 08a |
| in the author's metric itself (varying coefficients, $U = 0$) the Cauchy problem is not well posed for data that depend on the extra times | ASSUMED (a quoted theorem) | not checked by the record; the Lax-Mizohata theorem, quoted without proof, applied to the frequencies of the principal part (Section 8.18) |
| the Krein form is conserved; growing eigenspaces are Krein-neutral; real-frequency eigenspaces have inertia (4,4) | PROVED | `mode_hamiltonian_B_selfadjoint_dispersion` (python-field-theory); `Q.one_particle_complex_frequency_Krein_neutral`, `Q.one_particle_Krein_inertia_proof` (python-pairing); 08a |
| along the deflating history the extra-time and the hidden frame momenta grow at the same rate; a wave reaches the onset of growth exactly when $D = (\sin^2 z)^{-1/6}k_{x_5}^2 - \tan^2 z\,k_{x_0}^2 > 0$, so every extra-time wave without hidden momentum does (frozen coefficients at each instant) | PROVED | `extra_time_modes_grow` (python-field-theory; its wording holds for $D > 0$); `flat_mode_mass_shell`, `extra_time_momentum_blueshift` (dark-sector); 08b |
| through the onset the growth follows the WKB formulas and is faster than any exponential (local-frame model) | COMPUTED | 08b: agreement $2.81 \times 10^{-4}$ (leading), $1.97 \times 10^{-5}$ (first order), late rate $10^{-5}$ |
| the reduction and the two exact families ($m = 0$ with every $\alpha$; $\alpha = -\frac14$ with every $m$); finite norm exactly for $\alpha > -\frac14$; on the history every finite-norm member grows after a finite time | PROVED | `solution_matrix_square` (wolfram-field-theory); `exact_solution_family_x4_x0` (python-field-theory); 08d |
| the $x_0$-independent good-sector modes grow wherever $m < c_g$ (every mass, on the history, after a finite time); the mode operator is symmetric only up to the flux at the fold (its term $-iv_g$ compensates the changing volume) | PROVED | `good_sector_x0_independent_modes_without_boundary_condition`, `good_sector_hermiticity_up_to_the_brane_flux` (python-scope); 08d |
| the norm of a growing mode changes exactly by the flux through the fold | COMPUTED | 08d: $dN/dx_4$ equals the flux to $5.9 \times 10^{-10}$; $N(4)/N(0) = 1.57 \times 10^8$ |
| the history $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$ ($A = 1$, $b_4(0) = 1$), on which the hidden block deflates at the rate $\delta = AH/3$ | ASSUMED | prescribed background; it needs a diagonal source with $p_0 = p_t$ that grows with the time (Chapter 12; `Revision/kohn_sham/results/parameters.json`) |
| frozen coefficients; the local-frame model | ASSUMED | labelled MODEL in 08a and 08b |
| which boundary condition at the fold $z = \pi/2$ is physical; a well-posed formulation of the full field equation | OPEN | none imposed in the record |

### 8.38 What we proved, what we computed, what we assumed

**PROVED in this chapter, line by line** (and in the Revision record, with the file and check named in the section):

- The corrected metric from the diagonal frame, and its volume factor $\sqrt{|g|}$ with its derivative in time (Section 8.2). The 21 Christoffel symbols from two rules; the canonical spin connection of the diagonal frame: the rule $\omega_\mu{}^a{}_b = (f_a/f_b)\Gamma^a{}_{\mu b}$ for $a \neq b$, its 10 independent nonzero components (with the rate $h_4 = b_4'/(2b_4) - a_4'$ shared by the hidden direction and the extra times), and the spinor connections $\Omega_{x_0}$, $\Omega_{x_i}$, $\Omega_{x_t}$, $\Omega_{x_4} = 0$ (Section 8.4).
- $\gamma^\mu\Omega_\mu = G = c_g\gamma^{(0)} + v_g\gamma^{(4)}$, direction by direction: the pieces $\pm\frac12a_4'$ of 3-space and of the extra times cancel, the hidden direction adds $-\frac12a_4'$, the four directions of the hidden block add $\frac14b_4'/b_4$ each, and the three extra times give $\frac12He^{a_4}b_4^{-1/2}$ each along $\gamma^{(0)}$; and the divergence form $\gamma^\mu\Omega_\mu = \frac{1}{2\sqrt{|g|}}\partial_\mu(\sqrt{|g|}\gamma^\mu)$ (Section 8.5).
- $\Omega_\mu = 0$ for every $\mu$ if and only if $a_4' = 0$, $b_4' = 0$ and $H = 0$; $GG = (c_g^2 - v_g^2)I_{16}$, so $G\Psi \neq 0$ for every $\Psi \neq 0$ where $c_g^2 \neq v_g^2$, which on the history holds at every $x_4 \geq 0$ (Section 8.6). The term sees the deflating block; the Ricci scalar as the sum of the Ricci components; the flat member $a_4 = 0$, $b_4 = H^2x_4^2$ (two entries checked by hand) and $R^{x_1}{}_{x_1} = \frac53H^2$ on the history (Section 8.7).
- $\{\gamma^\mu, \Omega_\mu\} = 0$ for each $\mu$; the connection drops out of the Lagrangian, and the Euler-Lagrange equation of the connection-free symmetric Lagrangian contains the same term as its half-density term (Section 8.8).
- The boost keeps the metric; the spin transformation $S = e^{-(b/2)\gamma^{(4)}\gamma^{(0)}}$ moves the gammas of the boosted frame; the connection of the boosted frame and the formula $\gamma'^\mu\Omega'_\mu = (c_g - \frac{b'}{2})(\cosh b\,\gamma^{(0)} - \sinh b\,\gamma^{(4)}) + v_g(\cosh b\,\gamma^{(4)} - \sinh b\,\gamma^{(0)})$; for $b' = 2c_g$ only the part $v_g$ is left, and $\cosh b\,c_4 + \sinh b\,c_0 = v_g$ for every rapidity, so no boost of this kind removes it (Sections 8.3 and 8.9).
- $F' = SFS^{-1}$; the component $F_{x_5x_0} = \frac12\cot z\,W(h_4^2e^{-2a_4}b_4 - H^2)\gamma^{(0)}\gamma^{(5)}$ computed by hand; it vanishes on the flat member; its square is the same in both frames; the connection vanishes in no frame where the metric is curved (Section 8.10). The connection parts of $K^{x_4}{}_{x_1}$ (zero) and of $K^{x_4}{}_{x_5}$ ($\frac12HW\gamma^{(4)}\gamma^{(0)}\gamma^{(5)}$) (Section 8.11).
- The Hadamard toy example; the second-order form with the extra-time derivatives of the "wrong" sign; the evolution form with the terms $c_g$ and $v_g$ (Section 8.16). The mode matrix, $h_k^2 = E^2I_{16}$, its eigenvalues $\pm E$ eight each, its anti-Hermitian part (Section 8.17). Unbounded growth rates ($\kappa \ge K - c$), the closed solution in time, and the failure of continuous dependence in every Sobolev norm, in flat 4+4 space and with frozen coefficients (Section 8.18); the frequencies of the principal part, which are not real for a wave along an extra time at any point of the author's metric (Section 8.18). Conservation of the Krein form and the Krein-neutrality of the growing eigenspaces (Section 8.19).
- Conserved coordinate wave numbers; frame momenta along the extra times and the hidden direction that grow at the same rate; the deflation rate $\delta = AH/3$ on the history; the condition $D > 0$ for the onset; the exact onset time (the one positive root of an equation of degree four) and its finiteness for every $q_5 > 0$ without hidden momentum (Section 8.24). The Krein form $\sigma E_0/m$ of the starting columns and the leading and first-order WKB formulas (Section 8.25).
- The rescaling $\Psi = e^{a_4/2}b_4^{-1}(\sin^2 z)^{-1/8}\chi$ removes the term for every field, and turns the quadratic potential into $\lambda e^{a_4}S[\chi]/(b_4^2|\sin z|^{1/2})$; the norm becomes $\int\chi^\dagger\chi\,|dy|$ (Section 8.30). The reduction of the field equation for $F(\sin^2 z)^{\alpha/2}\Phi(x_4)$, the two exact families for all functions $a_4$ and $b_4$, the finite-norm condition $\alpha > -\frac14$ with the factor $1/(3H(4\alpha + 1))$, $M^2 = (\mu_A^2 - m^2)I_{16}$, the onset time and the double-exponential growth of the massless members on the history (Section 8.31). The matrix $A$ and its growing modes; the boundary identity with the term of the changing volume; the change of the norm only through the flux at the fold (Section 8.32).

**PROVED in the Revision record and used here without its proof:** the Clifford relations and the reality and symmetry of the author's gammas (Chapter 4); the irreducibility of the 16-dimensional representation (commutant dimension 1; Chapter 5); the vielbein postulate and the covariant constancy of the gammas in the diagonal frame (recomputed by the notebooks); the curvature identity $F = \frac14R\gamma\gamma$ in the diagonal frame (checked by Notebook 08c for one component in two frames); the Ricci components in full (computed by Notebook 08c); $Bh_k = h_k^\dagger B$; the Krein inertia (4,4) of every real-frequency eigenspace; the Euler-Lagrange equations of the Grassmann field; and the direct computation of the boosted frame's connection.

**COMPUTED by the notebooks** (every exact statement is also checked there, and every number reproduces the record where they overlap): Notebook 08c, 37 checks, computes everything of Sections 8.4 to 8.11 exactly with sympy, including the boosted frame for an arbitrary rapidity, the Riemann tensor of the flat member (1792 components) and the curvature in both frames, and at one point of the history ($z = \pi/4$, $x_4 = 0.5$) $c_{05} = -0.434364$, the rapidity $1.632244$ and ranks 16; the size of the term at $x_4 = 0$ is $1.715938$ in the diagonal frame and $0.833333$ in the removing frame. Notebook 08a, 30 checks, confirms $h_k^2 = E^2$ exactly, the growth rates against the eigenvalues to $10^{-10}$, the closed formula against RK4 to $10^{-9}$, the Hadamard ratio (first above $10^6$ at $K = 13.9, 19.9, 27.1, 44.2$ for $s = 0, 2, 4, 8$), the Krein drift below $10^{-12}$. Notebook 08b, 29 checks, confirms the deflation rate $\delta = \frac13$, the onset times against bisection to $10^{-10}$ for 96 waves, the mass shell and the equal rates of the dark-sector record, the condition $D > 0$ for five hidden momenta, RK4 with the error ratio 15.89 and accuracy $10^{-8}$, the WKB agreement ($2.81 \times 10^{-4}$, $1.97 \times 10^{-5}$, late rate $10^{-5}$), the slow growth of the size before the onset (to $u^\dagger u = 2.00$ and $1.99$ at the onset), and growth to $u^\dagger u \approx 2.06 \times 10^{48}$ nine time units after the onset, with the Krein drift below $10^{-9}$. Notebook 08d, 27 checks, proves the rescaling for arbitrary functions, the reduction and the families for symbolic $\alpha$, the boundary identity on explicit columns, and finds $N(4)/N(0) = 1.569834 \times 10^8$ for the mode with $m = 2$, with $dN/dx_4$ equal to the flux to $5.9 \times 10^{-10}$. Run times: 08a and 08b run in well under a minute, 08d in one to three minutes and 08c in a few minutes; the provenance file of each notebook (in the folder `Revision/textbook/notebooks`, named after the notebook, for example `08c_frame_dependence.PROVENANCE.md`) records the times measured on the build computer in its build and check runs, which depend on how busy that computer is.

**ASSUMED, chosen, or an interpretation.** The history $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$ with $A = H = m = 1$ and $b_4(0) = 1$ is a PRESCRIBED BACKGROUND (the Kohn-Sham record's own label; it needs a diagonal source with $p_0 = p_t$ that grows with the time, Chapter 12); every exact identity of the chapter holds for all functions $a_4$ and $b_4$. Frozen coefficients (Sections 8.17 to 8.19) and the local-frame model (Section 8.25) are labelled MODEL: they describe a wave near one point, not exact solutions of the field equation in the author's metric. Facts taken from Chapter 6 (where local spin covariance is proved): the canonical spin connection of every frame makes its gammas covariantly constant and is a combination of the $S^{ab}$. Standard theorems quoted without proof: the Lax-Mizohata theorem, which carries the failure of well-posedness from frozen coefficients to the author's varying coefficients (Section 8.18; so that conclusion is ASSUMED, not PROVED, and the record does not check it); the general curvature identity $F = \frac14R\gamma\gamma$ in every frame (proved for this metric by the record); Descartes' rule of signs; the trace of a matrix is the sum of its eigenvalues; the dimension of an eigenspace is 16 minus the rank of $h - \lambda I$. Treating $\bar\Psi$ and $\Psi$ as independent variables in the Euler-Lagrange equations is the method of Chapter 7. Two statements are interpretations, labelled as such: that the role of the term $G$ depends on the variables and the measure (Section 8.30), and that the growth of the good-sector modes is "fed through the fold" (Section 8.32).

**OPEN.** Which boundary condition at the fold $z = \pi/2$ is physical (the Kohn-Sham record ASSUMES fold conditions for its own model; this record imposes none). Whether and how the full field equation can be given a well-posed evolution: restricting to the good sector removes the extra-time growth but is a choice, not a consequence, and even the good sector needs a boundary condition at the fold. A positive-norm quantum theory of the full field with the growing modes present, and a stable vacuum, are not constructed (Chapter 10 states what is). Whether the frame-dependent term $c_g\gamma^{(0)}$ has any observable effect is not claimed.

### 8.39 Exercises

**Exercise 1.** Compute $\gamma^{x_6}\Omega_{x_6}$ directly from $\Omega_{x_6} = \frac12W(h_4s_b\,\gamma^{(4)}\gamma^{(6)} + H\gamma^{(0)}\gamma^{(6)})$, with $s_b = e^{-a_4}b_4^{1/2}$ and $h_4 = b_4'/(2b_4) - a_4'$, line by line.

*Answer.* $\gamma^{x_6} = \gamma^{(6)}/f_6$ with $f_6 = s_bW$. Then $\gamma^{x_6}\Omega_{x_6} = \frac12h_4\,\gamma^{(6)}\gamma^{(4)}\gamma^{(6)} + \frac{H}{2s_b}\gamma^{(6)}\gamma^{(0)}\gamma^{(6)}$ (the factor $W$ cancels in both terms, $s_b$ in the first). Anticommuting the first $\gamma^{(6)}$ past $\gamma^{(4)}$: $\gamma^{(6)}\gamma^{(4)}\gamma^{(6)} = -\gamma^{(4)}(\gamma^{(6)})^2 = -\gamma^{(4)}(-I_{16}) = \gamma^{(4)}$; in the same way $\gamma^{(6)}\gamma^{(0)}\gamma^{(6)} = \gamma^{(0)}$. So $\gamma^{x_6}\Omega_{x_6} = \frac12h_4\gamma^{(4)} + \frac12He^{a_4}b_4^{-1/2}\gamma^{(0)} = \big(\frac14\frac{b_4'}{b_4} - \frac12a_4'\big)\gamma^{(4)} + \frac12He^{a_4}b_4^{-1/2}\gamma^{(0)}$, the value of every extra time in Section 8.5.

**Exercise 2.** On the history of the record ($A = H = 1$, $b_4(0) = 1$) compute $c_g$, $v_g$ and the number $c_g^2 - v_g^2$ at $x_4 = 0$ and at $x_4 = 3$, and find the time at which $GG = 0$. What is $G$ there?

*Answer.* $c_g = \frac32e^{a_4}b_4^{-1/2} = \frac32e^{x_4}e^{-2x_4/3} = \frac32e^{x_4/3}$ and $v_g = \frac43 - \frac12 = \frac56$. At $x_4 = 0$: $c_g = 1.5$, $c_g^2 - v_g^2 = 2.25 - 0.694444 = 1.555556 = \frac{14}{9}$. At $x_4 = 3$: $c_g = \frac32e = 4.077423$, $c_g^2 - v_g^2 = 16.625376 - 0.694444 = 15.930932$. $GG = 0$ needs $\frac94e^{2x_4/3} = \frac{25}{36}$, so $e^{2x_4/3} = \frac{25}{81}$ and $x_4 = \frac32\ln\frac{25}{81} = -1.763360$; there $c_g = v_g = \frac56$ and $G = \frac56(\gamma^{(0)} + \gamma^{(4)})$, a matrix with square 0 and rank 8, which annihilates an 8-dimensional subspace of fields.

**Exercise 3.** (a) Show that $\varphi = \epsilon\cosh(Kx_4)\cos(Kx_5)$ solves $\partial_4^2\varphi = -\partial_5^2\varphi$. (b) For data of largest value $\epsilon$, compute the ratio of the largest value of the solution at $x_4 = 1$ to $\epsilon$ for $K = 10$ and $K = 20$. (c) Show that $\varphi = \epsilon\cos(Kx_4)\cos(Kx_1)$ solves the ordinary wave equation $\partial_4^2\varphi = \partial_1^2\varphi$, and compare.

*Answer.* (a) Section 8.16: both sides equal $\epsilon K^2\cosh(Kx_4)\cos(Kx_5)$. (b) The ratio is $\cosh K$: $\cosh 10 = 11013.2$ and $\cosh 20 = 2.4258 \times 10^8$. Doubling $K$ multiplies the amplification by about $e^{10} \approx 22000$; data of the same size give ever larger solutions. (c) $\partial_4^2\varphi = -\epsilon K^2\cos(Kx_4)\cos(Kx_1) = \partial_1^2\varphi$; the largest value stays $\epsilon$ at every time, for every $K$: the ordinary wave equation depends continuously on its data.

**Exercise 4.** With frozen coefficients and $m = 1$, decide whether the waves oscillate or grow, and give the frequency or the growth rate: (a) $k_1 = 2$, $k_5 = 3$; (b) $k_5 = 2$, $k_0 = 1$; (c) $k_6 = k_7 = 0.5$. (d) With $k_1 = 4$, how large must $k_5$ be for growth? Compare with Figure 08a.1.

*Answer.* $E^2 = m^2 + k_1^2 + k_2^2 + k_3^2 + k_0^2 - k_5^2 - k_6^2 - k_7^2$. (a) $E^2 = 1 + 4 - 9 = -4$: growth with $\kappa = 2$. (b) $E^2 = 1 + 1 - 4 = -2$: growth with $\kappa = \sqrt2 = 1.414214$. (c) $E^2 = 1 - 0.25 - 0.25 = 0.5$: oscillation with $E = \pm0.707107$. (d) Growth needs $k_5^2 > 1 + 16 = 17$, that is $k_5 > \sqrt{17} = 4.123106$; in the right panel of Figure 08a.1 the dotted curve ($k_1 = 4$) leaves zero there.

**Exercise 5.** (a) Show that the size $\sqrt{\mathrm{tr}(M^TM)/16}$ of $M = c_0\gamma^{(0)} + c_4\gamma^{(4)}$ is $\sqrt{c_0^2 + c_4^2}$. (b) Write the term of the boosted frame as $M = \kappa_b(\cosh b\,\gamma^{(0)} - \sinh b\,\gamma^{(4)}) + v_g(\cosh b\,\gamma^{(4)} - \sinh b\,\gamma^{(0)})$ with $\kappa_b = c_g - b'/2$. Show that its size squared is $(\kappa_b^2 + v_g^2)\cosh 2b - 2\kappa_bv_g\sinh 2b$. (c) On the history with $H = 1$ evaluate the size for the diagonal frame at $x_4 = 0$, for the rapidity $b = 3x_4$ at $x_4 = 0$ and $x_4 = 0.5$, and for the removing rapidity $b = 9(e^{x_4/3} - 1)$ at $x_4 = 0.5$. Compare with Figure 08c.3.

*Answer.* (a) $(\gamma^{(0)})^T = \gamma^{(0)}$ and $(\gamma^{(4)})^T = -\gamma^{(4)}$, so $M^T = c_0\gamma^{(0)} - c_4\gamma^{(4)}$ and $M^TM = c_0^2(\gamma^{(0)})^2 - c_4^2(\gamma^{(4)})^2 + c_0c_4(\gamma^{(0)}\gamma^{(4)} - \gamma^{(4)}\gamma^{(0)}) = (c_0^2 + c_4^2)I_{16} + 2c_0c_4\gamma^{(0)}\gamma^{(4)}$ (anticommutation in the last step). The trace of $\gamma^{(0)}\gamma^{(4)}$ is zero, so $\mathrm{tr}(M^TM)/16 = c_0^2 + c_4^2$. (b) Here $c_0 = \kappa_b\cosh b - v_g\sinh b$ and $c_4 = v_g\cosh b - \kappa_b\sinh b$. Squaring and adding, $c_0^2 + c_4^2 = (\kappa_b^2 + v_g^2)(\cosh^2 b + \sinh^2 b) - 4\kappa_bv_g\sinh b\cosh b$, and $\cosh^2 b + \sinh^2 b = \frac{(e^b + e^{-b})^2 + (e^b - e^{-b})^2}{4} = \frac{e^{2b} + e^{-2b}}{2} = \cosh 2b$, $2\sinh b\cosh b = \sinh 2b$. (c) $c_g = \frac32e^{x_4/3}$, $v_g = \frac56$. Diagonal frame at $x_4 = 0$: $b = 0$, $\kappa_b = 1.5$, size $\sqrt{2.25 + 0.694444} = \sqrt{106}/6 = 1.715938$. Rapidity $b = 3x_4$ ($b' = 3$): at $x_4 = 0$, $\kappa_b = 0$ and $b = 0$, size $v_g = 0.833333$; at $x_4 = 0.5$, $c_g = 1.772041$, $\kappa_b = 0.272041$, $b = 1.5$, and the size is $\sqrt{0.768451\cosh 3 - 0.453401\sinh 3} = 1.787284$. Removing rapidity at $x_4 = 0.5$: $b = 9(e^{1/6} - 1) = 1.632244$ and $\kappa_b = 0$, so the size is $v_g\sqrt{\cosh 2b} = 3.016443$. In the right panel of Figure 08c.3 the curves pass through these values at $x_4 = 0.5$: the removing frame already above the others, the diagonal frame at $\sqrt{c_g^2 + v_g^2} = 1.958$.

**Exercise 6.** Use $F'_{x_5x_0} = SF_{x_5x_0}S^{-1}$ with $F_{x_5x_0} = c_{05}\gamma^{(0)}\gamma^{(5)}$ (Section 8.10) to show that $F' = c_{05}(\cosh b\,\gamma^{(0)}\gamma^{(5)} - \sinh b\,\gamma^{(4)}\gamma^{(5)})$ and $F'^2 = c_{05}^2I_{16}$, and compute the two kinds of entries of $F'$ at the point of Figure 08c.5.

*Answer.* $S\gamma^{(0)}\gamma^{(5)}S^{-1} = (S\gamma^{(0)}S^{-1})(S\gamma^{(5)}S^{-1}) = (\cosh b\,\gamma^{(0)} - \sinh b\,\gamma^{(4)})\gamma^{(5)}$ by Step 2 of Section 8.9 ($S$ leaves $\gamma^{(5)}$ unchanged), which gives the formula. Squaring: $(\gamma^{(0)}\gamma^{(5)})^2 = I_{16}$, $(\gamma^{(4)}\gamma^{(5)})^2 = -I_{16}$, and the cross terms cancel because $\gamma^{(0)}\gamma^{(5)}\gamma^{(4)}\gamma^{(5)} = \gamma^{(0)}\gamma^{(4)}$ and $\gamma^{(4)}\gamma^{(5)}\gamma^{(0)}\gamma^{(5)} = \gamma^{(4)}\gamma^{(0)} = -\gamma^{(0)}\gamma^{(4)}$; so $F'^2 = c_{05}^2(\cosh^2 b - \sinh^2 b)I_{16} = c_{05}^2I_{16}$. At $H = 1$, $z = \pi/4$, $x_4 = 0.5$: $c_{05} = \frac12\cdot2^{-1/12}(\frac19e^{-1/3} - 1) = -0.434364$ and $b = 1.632244$, so the entries are $\pm c_{05}\cosh b = \mp1.153417$ in the pattern of $\gamma^{(0)}\gamma^{(5)}$ and $\pm(-c_{05}\sinh b) = \pm1.068503$ in the pattern of $\gamma^{(4)}\gamma^{(5)}$; the common square is $c_{05}^2 = 0.188672$.

**Exercise 7.** Along $a_4 = x_4$, $b_4 = e^{4x_4/3}$ with $m = H = 1$, compute the onset times of the waves (a) $q_1 = 0$, $q_5 = 0.01$, $q_y = 0$, $y = 0$; (b) the same at $y = -3$; (c) $q_1 = 0$, $q_5 = 10^{-4}$, $q_y = 0$, $y = 0$; (d) $q_1 = 1$, $q_5 = 0.05$, $q_y = 0$, $y = 0$; (e) $q_1 = 0$, $q_5 = 0.1$, $y = 0$ with $q_y = 0.08$ and with $q_y = 0.1$.

*Answer.* For $q_1 = q_y = 0$, $x_4^\ast = 3(Hy + \ln(m/q_5))/(AH) = 3(y + \ln(1/q_5))$. (a) $3\ln 100 = 13.815511$. (b) $3(-3 + 4.605170) = 4.815511$. (c) $3\ln 10^4 = 27.631021$, the left end of the top curve in the left panel of Figure 08b.3. (d) $D = q_5^2 = 0.0025$, and $X^\ast$ is the positive root of $0.0025X^4 - X^3 - 1 = 0$. Without the last term the root is $X = 400$; the term $-1$ moves it by about $1/p'(400) = 1/(4\cdot 0.0025\cdot 400^3 - 3\cdot 400^2) = 1/160000$, so $X^\ast = 400.00000625$, and $x_4^\ast = \frac{\ln X^\ast}{2\delta} = \frac32\ln X^\ast = 8.98719684$, later by only $2.3 \times 10^{-8}$ than the $8.98719682$ of the same wave without space momentum: the space term dies away like $e^{-2a_4}$, three times faster than the hidden block shrinks, and hardly matters. (e) With $q_y = 0.08$, $D = 0.01 - 0.0064 = 0.0036 > 0$ and $x_4^\ast = \frac32\ln(1/0.0036) = 8.440232$; with $q_y = 0.1$, $D = 0$ and $E^2 = 1$ at every time: no onset (the dashed curve of the right panel of Figure 08b.3).

**Exercise 8.** For the rescaling $\Psi = e^{pa_4}b_4^q(\sin^2 z)^r\chi$ with any real powers $p$, $q$ and $r$, find the term that replaces $G$ in the equation for $\chi$, and the powers that remove it. What does the norm density $\sqrt{|g|}\,\Psi^\dagger\Psi$ become for those powers?

*Answer.* $\frac{1}{f_0}\partial_0(\sin^2 z)^r = e^{a_4}b_4^{-1/2}\tan z\cdot r(\sin^2 z)^{r-1}\cdot2\sin z\cos z\cdot6H = 12Hr\,e^{a_4}b_4^{-1/2}(\sin^2 z)^r = 8r\,c_g(\sin^2 z)^r$, and $\partial_4(e^{pa_4}b_4^q) = (pa_4' + qb_4'/b_4)e^{pa_4}b_4^q$. As in Section 8.30, $\gamma^\mu D_\mu(e^{pa_4}b_4^q(\sin^2 z)^r\chi) = e^{pa_4}b_4^q(\sin^2 z)^r\big(\gamma^\mu\partial_\mu\chi + (1 + 8r)c_g\gamma^{(0)}\chi + [(1 + q)b_4'/b_4 + (p - \frac12)a_4']\gamma^{(4)}\chi\big)$, so the term becomes $(1 + 8r)c_g\gamma^{(0)} + [(1 + q)b_4'/b_4 + (p - \frac12)a_4']\gamma^{(4)}$. It vanishes for all functions $a_4$, $b_4$ exactly when $r = -\frac18$, $q = -1$ and $p = \frac12$: the rescaling of Section 8.30. For $p = q = r = 0$ it is the original $G$. For those powers the norm density is $e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}\cdot e^{a_4}b_4^{-2}(\sin^2 z)^{-1/4}\chi^\dagger\chi = |\cot z|\,\chi^\dagger\chi$, so the norm is $\int\chi^\dagger\chi\,|dy|$. (The reduction of Section 8.31 is this computation with $p = \frac12$, $q = -1$ and $r = \alpha/2$: its $\mu_A = (4\alpha + 1)c_g$ is the factor $(1 + 8r)c_g$.)

**Exercise 9.** For $H = 1$ take the member $\alpha = \frac14$ of the families. Compute $\mu_A$ on the history, the norm factor, the time at which a member of mass $m = 1$ starts to grow and its instantaneous growth rate at $x_4 = 0$, and the growth factor $e^{I}$ of the massless member at $x_4 = 3$.

*Answer.* $4\alpha + 1 = 2$, so $\mu_A = 2c_g = 3e^{a_4}b_4^{-1/2}$, which is $3e^{x_4/3}$ on the history. The norm factor is $\frac{1}{3H(4\alpha + 1)} = \frac16$, finite (the member varies along $x_0$ like $(\sin^2 z)^{1/8}$). For $m = 1$ the growth starts where $\mu_A = 1$: $x_4 = 3\ln\frac{2m}{3H(4\alpha + 1)} = 3\ln\frac13 = -3.295837$, so at $x_4 = 0$ the member grows already, with the instantaneous rate $\sqrt{\mu_A^2 - m^2} = \sqrt{9 - 1} = 2\sqrt2 = 2.828427$. For $m = 0$: $I(x_4) = \frac92\cdot2\cdot(e^{x_4/3} - 1) = 9(e^{x_4/3} - 1)$, so $I(3) = 9(e - 1) = 15.464536$ and $e^{I} = 5.2 \times 10^6$ after three units of time; after six units $I = 9(e^2 - 1) = 57.5$ and $e^I \approx 10^{25}$.

**Exercise 10.** Prove the Krein-neutrality of a growing eigenvector algebraically: if $h_ku = i\kappa u$ with $\kappa > 0$ and $Bh_k = h_k^\dagger B$, then $u^\dagger Bu = 0$.

*Answer.* Compute $u^\dagger Bh_ku$ in two ways. First, $h_ku = i\kappa u$ gives $u^\dagger Bh_ku = i\kappa\,u^\dagger Bu$. Second, $Bh_k = h_k^\dagger B$ gives $u^\dagger Bh_ku = u^\dagger h_k^\dagger Bu = (h_ku)^\dagger Bu = (i\kappa u)^\dagger Bu = -i\kappa\,u^\dagger Bu$ (the dagger conjugates the number $i\kappa$). Equating: $i\kappa\,u^\dagger Bu = -i\kappa\,u^\dagger Bu$, so $2i\kappa\,u^\dagger Bu = 0$, and since $\kappa \neq 0$, $u^\dagger Bu = 0$. The same computation with two eigenvectors $u$, $v$ of $i\kappa$ gives $v^\dagger Bu = 0$: the Krein form vanishes on the whole eigenspace. For a real eigenvalue $E$ the two sides are $E\,u^\dagger Bu$ and $E\,u^\dagger Bu$, and nothing follows; that is why the real-frequency eigenspaces can carry the inertia (4,4).
