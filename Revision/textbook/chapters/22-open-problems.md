## 22. Open problems and how a student could attack them

Every earlier chapter of this book marked the questions it could not answer with the label OPEN, and every starting point it could not derive with the label ASSUMED. This last chapter of Part V collects the most important of them and treats each one as a research problem for a student who has worked through Chapters 0 to 21. For each problem it says exactly what is asked, what the Revision record already proves or computes about it, why it is hard, what a first step could be, and in which files of the repository the work would start. For one of the problems, the question of how fast the three extra times $x_5, x_6, x_7$ may deflate before the instantaneous Kohn-Sham states of Chapters 14 and 15 stop describing the gas, the chapter carries out the first step completely, with Notebook 22a, as an example of what such a step looks like in practice. Nothing in this chapter is claimed to be solved.

### 22.1 What this chapter does

**Why a chapter of open problems.** A theory is finished when every question it raises has an answer. The theory of this book is not finished, and the honesty rule of Chapter 0 forbids pretending that it is. The Revision record proves some statements exactly (the pairing theorems, the field equations for $a_4$, the exact reduction of the Kohn-Sham problem), computes others numerically with measured errors (the Kohn-Sham states along the deflating history), and leaves the rest open. An open problem is not a failure of the record: it is the place where new work can begin, and pushing against the edges of a theory is one of the best ways to understand it. This chapter lists the edges.

**The five parts of each problem.** For each problem the chapter gives:

1. **the question**, put as precisely as possible, together with what would count as an answer;
2. **what is known**, every statement with its label and with the record file and check that verify it;
3. **why it is hard**: which obstacle is known, and which step nobody has taken;
4. **a first step** that a student could take with what this book teaches;
5. **where to start**: the files of the repository that already exist.

**The problems.**

| problem | sections | status | where it arose |
| --- | --- | --- | --- |
| 1. The creation question: are universes created, in pairs or otherwise? | 22.4 | OPEN; the pairing maps T1, T2, Q, T3 and the corollary C1 are PROVED | Chapters 18 to 20 |
| 2. Beyond the instantaneous Kohn-Sham states: the time-dependent problem | 22.5 to 22.13 | OPEN; a first estimate for the free field is COMPUTED in Notebook 22a | Chapters 14 and 15 |
| 3. The back-reaction of the gas on $a_4$ | 22.14 | OPEN; no recorded Kohn-Sham state is an admissible source | Chapters 12 and 17 |
| 4. The Z2 brane and its junction conditions | 22.15 | the Z2 mirror is ASSUMED; its junction conditions are OPEN | Chapters 14, 18 and 19 |
| 5. The dark-sector hypotheses | 22.16 | HYPOTHESIS, being investigated; no result is claimed | Chapters 9 and 12 |
| 6. Matter and antimatter | 22.17 | not solved by the theory as built; every scenario is a HYPOTHESIS | Chapter 21 |
| 7. Smaller open items | 22.18 | OPEN, CHOSEN or CONVENTION, as listed there | several chapters |

The problems are linked. The time-dependent problem (Problem 2) needs the history of $a_4$, which the back-reaction (Problem 3) would determine; both T2 and T3 of Chapters 18 and 19 rest on the Z2 brane (Problem 4); any statement about the dark sector (Problem 5) needs an equation of state that is a consequence of the coupled equations, that is, Problem 3 again; and a creation process (Problem 1) would need a dynamical geometry, which none of the equations of the record provides. A student is well advised to start with a problem whose first step is a finite calculation: Problem 2, whose first step this chapter carries out, or the first steps of Problems 3 and 4.

**The notebook of this chapter.** Notebook 22a is the worked example of Problem 2. It reads the adiabaticity measure $Q$ of the 75 recorded ground states, shows that $Q$ grows exactly in proportion to the deflation rate, reproduces the record's $Q$ with the solver's shooting method written again in Python, collapses every slice and every momentum shell onto one curve with the exact rescaling identity, measures the jumps into the negative-energy branch, and solves the exact time evolution of one sector of the free field for deflation rates from $0.25$ to $251$. It draws eight figures, needs no Rust, and ends with the line ALL 20 CHECKS PASSED (notebook 22a).

**The status of every statement.** Every statement carries one of the five labels of Chapter 0: PROVED (exact, with the record file and check where the Revision record verifies it), COMPUTED (a number of a numerical computation, with its measured uncertainty and the file or notebook cell that holds it), ASSUMED (a starting point that is not derived), HYPOTHESIS (an idea that is stated and examined but not established) and OPEN (a question nobody has answered). Three special cases of ASSUMED, used as in Chapters 14 to 17, appear here as well: PRESCRIBED BACKGROUND (the history $a_4 = AHx_4$, given and not solved for), CHOSEN (a numerical or boundary choice, such as the tip of the hidden direction) and CONVENTION (a rule fixed by agreement, such as which levels count as particles). A few derivations of this chapter are the book's own and are not checked by a Revision verifier; each of them is written out line by line and says so.

**What this chapter does not do.** It does not solve any of the problems it lists. In particular, and in the words of the honesty rule: that the big bang creates universes in pairs is NOT proved, and no creation process, rate, amplitude or big-bang dynamics follows from the equations of the record (Section 22.4); the theory as built does NOT solve the matter-antimatter problem (Section 22.17); and no result about the dark sector is claimed (Section 22.16).

**Notation and units.** The author's coordinates are $x_1, \dots, x_8$: $x_1, x_2, x_3$ are ordinary 3-space, which inflates with the scale factor $e^{a_4}\sin^{1/6}z$; $x_4$ is the time; $x_5, x_6, x_7$ are the three extra times, which deflate exponentially with the scale factor $e^{-a_4}\sin^{1/6}z$; $x_8$ is the hidden space direction, with $z = 6Hx_8$ between $0$ and $\pi/2$. The signature is (4,4): $\eta = \mathrm{diag}(+1,+1,+1,-1,-1,-1,-1,+1)$ in the order $x_1, \dots, x_8$. The hidden coordinate of the Kohn-Sham chapters is $y = \ln(\sin z)/(6H)$; it runs from the **tip** $y = -L$ (with $L = 3$) to the **brane** $y = 0$. A **slice** is one instant of the history, and $a_{4,0}$ is the value of $a_4$ there; the record's history is $a_4 = AHx_4$ with $A = 1$. In all numbers $H = 1$ and $m = 1$, so energies and momenta are in units of $m$, lengths and times in units of $1/H$. A state of the record is named like N688_lamm2_a00: $N = 688$ quanta, the coupling $-\lambda_2$ (the tags lam0, lamp1, lamm1, lamp2, lamm2 stand for $\lambda = 0, +\lambda_1, -\lambda_1, +\lambda_2, -\lambda_2$), the slice $a_{4,0} = 0.0$ (the two digits are ten times the slice).

### 22.2 The words of this chapter

Most words of this chapter were defined in earlier chapters; they are repeated here in plain words so that the chapter can be read on its own.

- **Open problem**: a question that neither the Revision record nor this book answers, put precisely enough that one can recognise an answer.
- **Test field** and **back-reaction**: a field that is computed in a gravitational field given in advance, which the field itself does not change, is a test field. The change of the gravitational field caused by the energy and momentum of the field is its back-reaction. All Kohn-Sham results of the record are test-field results.
- **Prescribed background**: the history $a_4 = AHx_4$ used by the Kohn-Sham chapters. It is given, not solved for: the computed Kohn-Sham states cannot be its source in the field equations for $a_4$ (Chapter 17).
- **Rate** $A$ and **e-fold**: on the history $a_4 = AHx_4$ the extra-time scale factor $e^{-a_4}\sin^{1/6}z$ shrinks by the factor $e = 2.718\ldots$ (one e-fold) in the time $1/(AH)$; the rate $A$ is the number of e-folds per unit of time $1/H$.
- **Instantaneous** (or **adiabatic**) **state**: the ground state of the Kohn-Sham Hamiltonian of one slice, computed as if the slice lasted forever. The word **adiabatic** also describes an evolution that is so slow that every particle stays in its instantaneous level.
- **Time-dependent Kohn-Sham problem**: the problem in which the orbitals evolve in the time $x_4$ under the Hamiltonian of each moment, with the potentials recomputed at every moment from the evolving densities.
- **Sector**: one momentum shell $n_2$ (3-momentum of length $k = 0.25\sqrt{n_2}$), one block type $j = \pm1$ and one brane parity (even or odd). The exact evolution never moves a particle from one sector to another. The **Fermi shell** of a state is its highest occupied shell.
- **Level**, **orbital** and **label**: a level $\varepsilon$ and its orbital $\varphi$ solve $h\varphi = \varepsilon\varphi$ for the Hamiltonian $h$ of one slice. The label $n$ is the integer that numbers the levels of one sector in order: $n = 0$ is the **band level** (bound to the brane; the occupied level of the Fermi shell), $n = 1, 2, \ldots$ are the **bulk levels** above it, and $n = -1, -2, \ldots$ are the levels of negative energy, the **negative branch**, which the record's filling convention treats as the normal-ordered sea that holds no particles.
- **Amplitude** and **probability**: when an orbital is written as a sum $\sum_n c_n\varphi_n$ of instantaneous orbitals, the complex number $c_n$ is the amplitude of level $n$ and $|c_n|^2$ the probability to find the particle in level $n$.
- **Basis**: a set of orbitals in which every orbital is written as a sum. A **truncated** basis keeps only some of them; a computation **converges** when its result stops changing as more are kept.
- **Dressing**: the small admixture of other levels that a particle carries while the background keeps moving. **Adiabaticity measure** $Q$: the size of this admixture to first order (Section 22.7). $G = Q/A$ is $Q$ per unit rate.
- **Redshifted momentum** $q = ke^{-a_{4,0}}$: the 3-momentum as the deflating history sees it (Section 22.7).
- **Sudden limit**: the limit of an infinitely fast change, in which the orbital has no time to change at all (Section 22.8). **Breakdown**: the instantaneous picture breaks down when the probability that a particle is NOT in its instantaneous level stops being small.
- **Brane**: the end $y = 0$ (that is $z = \pi/2$) of the hidden direction. **Z2 mirror** (or **orbifold**): the construction that continues the universe beyond the brane by its mirror image. **Kink**: a point where a function is continuous but its slope jumps. **Junction condition**: the rule that ties the jump of the slopes of the metric (or of a field) across a surface to the energy and momentum concentrated on that surface. **Tension**: the energy per unit area of a surface, which acts like a negative pressure along it.
- **Equation of state** $w$: the ratio $p/\rho$ of a pressure to the energy density. **CPL parametrisation**: the formula $w(a) = w_0 + w_a(1 - a)$ for an equation of state that changes with the scale factor $a$ of the observed universe. **Phantom**: $w < -1$.
- **Null energy condition** along a direction: $\rho + p \ge 0$, with $p$ the pressure of that direction.
- **Einstein-Hilbert Lagrangian**: the Lagrangian density $\sqrt{|g|}R$ of the geometry, with $R$ the Ricci scalar; varying its action with respect to the metric gives Einstein's equations without a source.
- **Quantum cosmology** and **wave function of the universe**: a quantum theory in which a few numbers that describe the whole geometry, such as a scale factor, are quantum variables; its wave function is a function of these numbers. The **Wheeler-DeWitt equation** is the equation this wave function must obey. The **tunnelling proposal** and the **no-boundary proposal** are two proposed boundary conditions that pick one solution of it; they are named in this chapter, not used.
- **Bogoliubov method**: a way to count the quanta of a field that a changing background creates: one compares the modes of the field before and after the change, and the part of a positive-energy mode of the start that has turned into negative-energy modes of the end measures the creation. It is quoted in this chapter, not derived or applied.
- **Hypothesis**: an idea that is stated and examined but not established; here, every scenario that goes beyond what the record proves or computes.

### 22.3 How to work on an open problem

The Revision record answered every question it did answer by one procedure, and a student who attacks an open problem should follow it, because it is what makes an answer trustworthy.

1. **Write the question down precisely**, with what would count as an answer and what would not. The specification `Revision/SPEC.md` is an example: section 7 asks for instantaneous Kohn-Sham states and says in the same sentence that the time-dependent problem is OPEN.
2. **Derive the result by hand**, line by line, as this book does.
3. **Verify every exact statement with two programs that share no code.** The record uses a Wolfram Language verifier and an independent Python checker built on sympy for each exact statement, each writing a report with a name, a verdict and a detail for every check. Include **negative controls**: inputs that must fail, so that a check that passes everything is caught.
4. **Compute every number with two independent methods** and compare them with tolerances fixed before the comparison, as the cross-check of Chapter 16 does. Repeat every run to show that it gives the same bytes.
5. **Never weaken a check to make it pass.** A failing check is information; the task is to find out why it fails (Chapter 16 tells how the first cross-check failed and what it found).
6. **Write down what is proved, what is computed, what is assumed and what is not claimed**, and label every statement.

The tools that already exist, and that the first steps below use, are these:

| tool | what it does | where |
| --- | --- | --- |
| exact verifiers (Wolfram Language) | prove identities with exact numbers and symbols and write a report | the files ending in `.wls` in the folders `Revision/algebra/wolfram`, `Revision/theory/wolfram`, `Revision/pairing/wolfram`, `Revision/field_equations_a4/wolfram` |
| independent exact checkers (Python, sympy) | the same statements without Wolfram code | the files whose names start with `check_` in the folders `Revision/algebra/python`, `Revision/theory/python`, `Revision/pairing/python`, `Revision/field_equations_a4/python` |
| the lead's checks | three further independent checks (the energy-momentum divergence, the Einstein and Gauss-Bonnet equations for $a_4$, charge conjugation and the U(1) charge) | the folder `Revision/lead_checks` |
| the Kohn-Sham theory | the exact reduction, the functional, the boundary conditions, the adiabaticity measure | `Revision/kohn_sham/ks-theory.json` with the verifiers in `Revision/kohn_sham/theory` |
| the Rust Kohn-Sham solver | shooting with RK4 and a Pruefer count, self-consistency, the adiabaticity table | the crate `Revision/kohn_sham/solver` |
| the reference solver and the cross-check | a second method and the comparison with tolerances fixed in advance | `Revision/kohn_sham/reference/run_reference.py`, `Revision/kohn_sham/checker/crosscheck_ks.py` |
| the source-condition checker | the Kohn-Sham states as sources of the equations for $a_4$ | `Revision/field_equations_a4/python/check_ks_source_conditions.py` |
| the notebooks of this book | every example, built and checked byte for byte | `Revision/textbook/notebooks` and the tool `Revision/textbook/tools/nbkit.py` |

### 22.4 Problem 1: the creation question

**The question.** The author asked for a proof "that Universes of masses {+mass, -mass} are created in pairs" (`Revision/README.md`), and the request for this book repeats it as "the big bang creates universes in pairs". As an open problem the question is: is there a theory in which the creation of a universe, or of a pair of universes of masses $+m$ and $-m$, is a process with a computable amplitude, probability or rate; and if so, what is it, and does it create pairs? An answer would be such a theory together with the computed number; a correspondence between solutions, however exact, is not an answer, because it says nothing about whether either solution comes into being.

**What is known.**

- PROVED (Chapter 18; `Revision/pairing/reports/wolfram-pairing.json` and `Revision/pairing/reports/python-pairing.json`): theorem T1, the chirality map $\Gamma$: $\mathcal{L}_{m,\lambda}[\Gamma\Psi] = -\mathcal{L}_{-m,-\lambda}[\Psi]$, so $\Gamma$ maps every solution with $(m, \lambda)$ to a solution with $(-m, -\lambda)$, with the energy-momentum tensor $T \to -T$ and the current $J \to -J$, in every gravitational field taken as a fixed background, for both fields.
- PROVED (same reports): theorem T2, $\Gamma$ combined with a Pin(4,4) reflection of character $-1$, maps $(m, \lambda)$ to $(-m, \lambda)$ with $\mathcal{L} \to +\mathcal{L}$; in the author's field it is the mirror across the Z2 brane (an ASSUMED construction), and the partner has EQUAL, not opposite, energy-momentum.
- PROVED (same reports): the quantum reading Q for dirac16complex: the chirality image carries the Krein metric $-B$ and is the same quantum system written in other variables; two universes quantised independently of each other carry $+B$ each, and their generators add without cancelling.
- PROVED (Chapter 19): theorem T3, every self-consistent instantaneous Kohn-Sham state with $(m, \lambda, \theta)$ has a partner with $(-m, +\lambda, \pi - \theta)$ with equal levels, occupations, energies and energy-momentum profiles (ASSUMED Z2 brane). The two reports are `wolfram-t3.json` and `python-t3.json` in the folder `Revision/pairing/kohn_sham/reports`.
- PROVED (Chapter 20): corollary C1, a T1 pair taken as the complete classical source of the author's metric is a zero source, and in Einstein gravity the author's metric then has no solution for $H > 0$. The derivation is short and is given below.
- The record itself lists what these theorems do not establish: the report `Revision/pairing/reports/python-pairing.json` holds, under its key `not_established`, twelve items. Among them: no creation process (nothing in these equations produces a universe, a pair of universes or a change of the number of universes); no rate, probability or amplitude (no wave function of the universe, path integral or tunnelling computation is part of the theorems); no dynamical necessity (a single universe of mass $+m$ is an equally valid solution without its partner); the vanishing total energy-momentum of a T1 pair is not a cancellation between two independently quantised universes; and the gravitational back-reaction is not part of the theorems.
- OPEN: whether any universe is CREATED, in pairs or otherwise. The equations of the record are field equations on a gravitational field that is given, and their canonical quantisation; no creation process, rate, amplitude or big-bang dynamics follows from them.

**Corollary C1 in Einstein gravity, line by line.** The field equations for $a_4$ in Einstein gravity (Chapter 12; `Revision/field_equations_a4/a4-equations.json`, key `einstein`) contain the $x_4$ component and the $x_8$ component

$$
3(a_4')^2 + 21H^2 + \Lambda = -\kappa\rho, \qquad -3(a_4')^2 + 15H^2 + \Lambda = \kappa p_8 ,
$$

where $a_4' = da_4/dx_4$, $\Lambda$ is the cosmological constant, $\kappa$ the gravitational coupling, $\rho$ the energy density and $p_8$ the pressure of the source along $x_8$. By T1 the two members of a pair have $T' = -T$, so the total source $T + T'$ vanishes: $\rho = 0$ and $p_8 = 0$.

$$
3(a_4')^2 + 21H^2 + \Lambda = 0, \qquad -3(a_4')^2 + 15H^2 + \Lambda = 0 .
$$

Rule: insert $\rho = 0$ and $p_8 = 0$ into the two components.

$$
36H^2 + 2\Lambda = 0 .
$$

Rule: add the two equations; the terms $3(a_4')^2$ and $-3(a_4')^2$ cancel.

$$
6(a_4')^2 + 6H^2 = 0 .
$$

Rule: subtract the second equation from the first; $\Lambda$ cancels.

$$
(a_4')^2 = -H^2 .
$$

Rule: divide by 6 and subtract $H^2$ from both sides.

The square of a real number is never negative, and $-H^2 < 0$ for $H > 0$. So no real history $a_4(x_4)$ exists: the only solutions of the two equations are the complex slopes $a_4' = \pm iH$ with $\Lambda = -18H^2$. PROVED: `Revision/field_equations_a4/reports/wolfram-a4-report.json`, check `einstein_no_vacuum_solution`; `Revision/field_equations_a4/reports/python-a4-report.json`, check `einstein_no_vacuum`; and independently `Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json`, check `no_vacuum_for_H_positive`, which also lists the complex solutions. The consequence: a T1 pair cannot by itself be the source of the author's universe in Einstein gravity. This is a statement about sources in one common geometry; it is not a derivation that a geometry, or a pair, is created.

**Why it is hard.**

- *The geometry has no dynamics of its own in the record.* Every theorem of Chapters 18 to 20 is a statement about fields in a gravitational field that is given (hypothesis H1 of T1). Without a dynamical geometry there is no process "a universe appears", and no state "no universe" from which it could appear.
- *A universe is not a particle in a fixed background.* To speak of the creation of universes one needs a quantum theory in which the geometry itself is a quantum variable, such as the quantum cosmology of a few variables of the metric (the Wheeler-DeWitt equation, the tunnelling and the no-boundary proposals). In plain words: **quantum cosmology** treats a few numbers that describe the whole geometry, such as a scale factor, as quantum variables; its **wave function of the universe** is a function of these numbers, and the **Wheeler-DeWitt equation** is the equation that this wave function must obey, the analogue for a geometry of the Schroedinger equation of a particle. That equation alone does not fix the wave function; it needs a boundary condition, and the **tunnelling proposal** (A. Vilenkin) and the **no-boundary proposal** (J. B. Hartle and S. W. Hawking) are two proposed boundary conditions of this kind. They are named here, not used. None of these is formulated for this 8-dimensional theory, and in signature (4,4) both the classical and the quantum side bring their own difficulties: modes with momentum along the extra times grow instead of oscillating (Chapter 8), and the quantised field has an indefinite (Krein) inner product (Chapter 10).
- *Nothing forces the partner to exist.* T1, T2 and T3 relate the solutions of two parameter sets. A single universe of mass $+m$ is an equally valid solution.
- *The cancelling pair has no home in Einstein gravity.* By C1 a T1 pair as the complete source of one common geometry leaves no solution for $H > 0$. A T2 pair does not cancel at all: its two members carry equal energy-momentum.

**A first step.** (a) Redo the derivation of C1 above, and its version for Einstein-Gauss-Bonnet gravity, in which vacuum solutions of the linear form $a_4 = AHx_4 + a_0$ exist exactly for $0 < \alpha_2H^2 \le 1/40$ (Chapter 12; checks `linear_member_vacuum_factor` and `einstein_gauss_bonnet_vacuum_linear` of both reports in `Revision/field_equations_a4/reports`). (b) Prepare the classical side of a reduced quantum model. From the four independent components of the Einstein tensor in the record (`Revision/field_equations_a4/a4-equations.json`, key `lovelockTensors.E1`) the student can compute the Ricci scalar of the author's metric; this is a derivation of this book, from the record's components, which no Revision verifier checks for $R$ itself. The trace of the Einstein tensor adds three 3-space components, the time component, three extra-time components and the hidden component:

$$
G^\mu{}_\mu = 3\big(-3(a_4')^2 + a_4'' + 15H^2\big) + \big(3(a_4')^2 + 21H^2\big) + 3\big(-3(a_4')^2 - a_4'' + 15H^2\big) + \big(-3(a_4')^2 + 15H^2\big) .
$$

Rule: the trace is the sum of the eight diagonal components $G^{x_1}{}_{x_1} + \dots + G^{x_8}{}_{x_8}$, and the record gives $G^{x_1}{}_{x_1} = G^{x_2}{}_{x_2} = G^{x_3}{}_{x_3}$ and $G^{x_5}{}_{x_5} = G^{x_6}{}_{x_6} = G^{x_7}{}_{x_7}$.

$$
G^\mu{}_\mu = -18(a_4')^2 + 126H^2 .
$$

Rule: collect terms: $(a_4')^2$ appears with $-9 + 3 - 9 - 3 = -18$, $a_4''$ with $3 - 3 = 0$, and $H^2$ with $45 + 21 + 45 + 15 = 126$.

$$
G^\mu{}_\mu = R - \tfrac{8}{2}R = -3R .
$$

Rule: $G^\mu{}_\nu = R^\mu{}_\nu - \tfrac12 R\,\delta^\mu_\nu$; the trace of $R^\mu{}_\nu$ is $R$, and the trace of $\delta^\mu_\nu$ in eight dimensions is 8.

$$
R = 6(a_4')^2 - 42H^2 .
$$

Rule: divide $-18(a_4')^2 + 126H^2 = -3R$ by $-3$.

The second derivative $a_4''$ has dropped out: the inflation of 3-space and the deflation of the extra times enter with opposite signs. The **Einstein-Hilbert Lagrangian** is the Lagrangian density $\sqrt{|g|}R$ of the geometry itself: when its action is varied with respect to the components of the metric, the Euler-Lagrange equations (Chapter 7) are Einstein's equations without a source (with a source, the Lagrangian of the matter is added). With $\sqrt{|g|} = \cos z$ independent of $a_4$ (Chapter 12), the Einstein-Hilbert Lagrangian $\sqrt{|g|}R$ of the author's metric contains $a_4$ only through $(a_4')^2$, which is the starting point of a reduced quantum model with the one variable $a_4$. Quantising such a model is a HYPOTHESIS-level programme of quantum cosmology; even if it is carried out, it gives a wave function of $a_4$, not a process that changes the number of universes, and both the boundary condition of that wave function and the meaning of "two universes" in it would have to be supplied. (c) Study the one kind of creation that could occur within the record's own equations, the creation of quanta of the field inside ONE universe by the changing background (OPEN: the record computes no such process), which in ordinary Dirac theory is the jump of a particle from a filled negative level to an empty positive one (the Bogoliubov method, introduced for expanding universes by L. Parker, Phys. Rev. 183, 1057 (1969); quoted, not derived here). Notebook 22a measures how strongly the deflating background couples the negative branch to the positive one in the free field (Section 22.13); whether such jumps mean the creation of pairs of quanta in the 4+4 quantisation with its Krein metric is OPEN, and they have nothing to do with the creation of universes.

**Where to start.** The proofs and their limits: `Revision/docs/PAIR_CREATION_PROOFS.md` (its section 11 lists what is proved and what is not), `Revision/pairing/pairing-theory.json` (key `not_established`), the verifiers `Revision/pairing/wolfram/verify_pairing.wls` and `Revision/pairing/python/check_pairing.py`; the equations for $a_4$: `Revision/field_equations_a4/a4-equations.json` with its two verifiers; the lead's check `Revision/lead_checks/einstein_gauss_bonnet_a4.py`, which has its own curvature code.

### 22.5 Problem 2: beyond the instantaneous Kohn-Sham states

**The question.** Chapters 14 and 15 computed instantaneous Kohn-Sham states: at each slice $a_{4,0}$ of the history $a_4 = AHx_4$ the solver finds the ground state of the Hamiltonian of that one instant, as if the background stood still. But the background does not stand still: the three extra times deflate, 3-space inflates, and the Hamiltonian changes with $x_4$. The open problem has two levels. First: how fast would the extra times have to deflate before the instantaneous states stop describing the gas, and what happens then? Second: solve the self-consistent time-dependent Kohn-Sham problem, in which the orbitals evolve in $x_4$ and the potentials follow the evolving densities. An answer to the first is an estimate of the breakdown rate with a measured error; an answer to the second is a solver for the time-dependent problem, checked like the solvers of Chapters 15 and 16.

**What is known.**

- PROVED: the reduction of the field equation to the hidden coordinate is exact also when $a_4$ depends on $x_4$; in each sector the orbital obeys $i\,\partial\chi/\partial x_4 = h(x_4)\chi$ with a Hermitian $h$, and the momentum, the block and the brane parity are conserved, so particles can only jump between levels of the same sector. The record states this in `Revision/kohn_sham/ks-theory.json` under the keys `sectorAndAnsatz.exactReduction` and `adiabaticity.exactEvolution`, and both theory reports in the folder `Revision/kohn_sham/reports` verify it with their check `hamiltonian_16_hermitian`.
- PROVED: the identity behind the adiabaticity measure $Q$ (Sections 22.6 and 22.7); check `adiabatic_offdiagonal_identity` of the report `ks-theory-python.json` in the same folder.
- COMPUTED: at the record's rate $A = 1$ the largest $Q$ of each of the 75 ground states is at most $0.0935$ (largest value $0.0934532$, state N688_lamm2_a00), and $Q = 0$ exactly for $N = 8$; the column `transition_probability_estimate_Q2` gives $Q^2$, at most $0.0087335$ (the record's name for $Q^2$; Section 22.7 explains how this book reads it). The table is `adiabaticity.csv` in the folder `Revision/kohn_sham/results/adiabatic`.
- COMPUTED: for the 15 series of the record (three particle numbers, five couplings) the set of occupied levels does not change between neighbouring slices (the tables `fermi-level-crossings.csv` and `history.json` of the same folder). But the record also shows that this is not always so: for $N = 696$ at $\lambda = 0$ the brane-band levels redshift below the $k = 0$ bulk level along the history, the instantaneous ground state changes its occupied levels, and the state continued adiabatically from $a_{4,0} = 0$ lies above the instantaneous ground state by $3.657$, $6.053$, $7.612$ and $8.623$ (units of $m$) at the slices $0.5$, $1$, $1.5$ and $2$. This is the table `crossing-demo.csv` of the same folder, checked by `adiabatic_crossing_flag_demonstration` of the solver's report `Revision/kohn_sham/reports/ks-rust-solver.json`.
- PRESCRIBED BACKGROUND: the history itself (`Revision/kohn_sham/results/adiabatic/history.json`, key `status`).
- OPEN: the non-adiabatic (time-dependent) problem (`Revision/kohn_sham/ks-theory.json`, key `adiabaticity.caveat`).

**Why it is hard.** With interaction the effective mass $M = m + \tfrac{15}{16}\lambda S$ and the potential $v = -\lambda n/16$ depend on the densities of all occupied orbitals of all sectors (Chapter 14), so the evolution of one sector depends on all the others at every moment, and a gas of 688 quanta occupies many sectors. The functional itself is a question: the simplest choice, the ground-state functional evaluated with the densities of each moment, is the adiabatic approximation of time-dependent density functional theory, whose foundation in ordinary quantum mechanics is the theorem of E. Runge and E. K. U. Gross (Phys. Rev. Lett. 52, 997 (1984); quoted, not derived here); nobody has established its analogue for the 4+4 field with its Krein metric. When levels of different sectors cross the Fermi level, the instantaneous ground state and the evolved state part ways, as the case $N = 696$ shows. The negative branch is coupled to the positive one by the moving background, and how such jumps are to be read in the quantised theory is OPEN. And the history is prescribed: a full answer would also need Problem 3.

**A first step: an estimate in the free field.** In the free field ($\lambda = 0$) the mass is $M = m$ and $v = 0$ in every sector, so the sectors do not influence each other and the evolution equation of one sector is the complete, exact time evolution of the free field in that sector. That makes an exact first step possible. Sections 22.6 to 22.8 derive the equations it needs, Notebook 22a solves them (Sections 22.9 to 22.12), and Section 22.13 collects what it found and how a student could go on.

### 22.6 The amplitude equations, line by line

**The setting.** Take one sector. Its orbital is a pair of complex functions $\chi(y, x_4) = (\chi_1, \chi_2)$ on $-L \le y \le 0$. Its evolution equation is (`Revision/kohn_sham/ks-theory.json`, keys `adiabaticity.exactEvolution` and `blockEquation.hamiltonian`)

$$
i\,\frac{\partial\chi}{\partial x_4} = h\,\chi, \qquad h = j\Big[-i\sigma_1\frac{d}{dy} + M\sigma_2 + \kappa k\sigma_3\Big] + v, \qquad \kappa = e^{-Hy - a_4(x_4)} ,
$$

where $j = \pm1$ is the block type, $k$ the length of the 3-momentum, and $\sigma_1$, $\sigma_2$, $\sigma_3$ the Pauli matrices

$$
\sigma_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad \sigma_2 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad \sigma_3 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} .
$$

The factor $\kappa k$ is the 3-momentum as the orbital feels it: 3-space has the scale factor $e^{Hy + a_4}$ in the hidden coordinate (Chapter 14), and a fixed coordinate momentum $k$ corresponds to the physical momentum $k$ divided by that scale factor. As the history goes on, $a_4$ grows and $\kappa k$ shrinks: the momenta redshift.

**The inner product and Hermiticity.** For two orbitals $\varphi$ and $\psi$ write $\langle\varphi|\psi\rangle = \int_{-L}^{0}\varphi^\dagger\psi\,dy$, where $\varphi^\dagger$ is the row of the complex conjugates of the components of $\varphi$. An operator $h$ is **Hermitian** when $\langle\varphi|h\psi\rangle = \langle h\varphi|\psi\rangle$ for all orbitals that obey the boundary conditions; the Kohn-Sham $h$ is (checks `hamiltonian_16_hermitian` and `bc_self_adjoint_boundary_term` of `Revision/kohn_sham/reports/ks-theory-python.json`). Its first consequence is that the total probability does not change. Write $\dot\chi = \partial\chi/\partial x_4$:

$$
\frac{d}{dx_4}\langle\chi|\chi\rangle = \langle\dot\chi|\chi\rangle + \langle\chi|\dot\chi\rangle .
$$

Rule: the product rule, applied inside the integral to $\chi^\dagger\chi$.

$$
\frac{d}{dx_4}\langle\chi|\chi\rangle = \langle -ih\chi|\chi\rangle + \langle\chi|-ih\chi\rangle = i\langle h\chi|\chi\rangle - i\langle\chi|h\chi\rangle .
$$

Rule: the evolution equation gives $\dot\chi = -ih\chi$; a factor $-i$ in the left slot comes out complex-conjugated as $+i$ (the left slot carries the dagger), in the right slot as $-i$.

$$
\frac{d}{dx_4}\langle\chi|\chi\rangle = 0 .
$$

Rule: $h$ is Hermitian, so the two terms are equal and cancel.

**The instantaneous orbitals.** At each slice the levels $\varepsilon_n$ and orbitals $\varphi_n$ solve $h\varphi_n = \varepsilon_n\varphi_n$ with the boundary conditions of the record (the regular tip, $b(-L) = 0$; the even brane parity, $b(0) = 0$, or the odd one). They are **orthonormal**: $\langle\varphi_m|\varphi_n\rangle = 1$ for $m = n$ and $0$ otherwise. In the free field they depend on $x_4$ only through $a_4$, so we write $\varphi_n(y; a_4)$ and $\varepsilon_n(a_4)$. In the **real form** of the record (`Revision/kohn_sham/ks-theory.json`, key `blockEquation.realForm`) every orbital can be written $\varphi = (a, ib)$ with two real functions $a(y)$ and $b(y)$, which obey for $j = +1$

$$
a' = Ma - (\kappa k + \varepsilon - v)\,b, \qquad b' = (\varepsilon - v - \kappa k)\,a - Mb ,
$$

where the prime is $d/dy$; in the free field $M = 1$ and $v = 0$. Then $\varphi^\dagger\varphi = a^2 + b^2$, and for two orbitals $\varphi_m^\dagger\sigma_3\varphi_n = a_ma_n - b_mb_n$.

**The equations for the amplitudes.** Write $\partial_a$ for the derivative with respect to $a_4$ at fixed $y$, and a dot for $d/dx_4$.

Line 1. Assume that the instantaneous orbitals form a basis, and write the evolving orbital as

$$
\chi(y, x_4) = \sum_n c_n(x_4)\,\varphi_n\big(y; a_4(x_4)\big) .
$$

Rule: the expansion in a basis; the amplitudes $c_n$ carry the time dependence that the orbitals of the slice do not. (A computer keeps finitely many levels; Notebook 22a keeps 20 and measures what the others would change.)

Line 2.

$$
i\dot\chi = i\sum_n\Big[\dot c_n\,\varphi_n + c_n\,\dot a_4\,\partial_a\varphi_n\Big] .
$$

Rule: the product rule for each term $c_n\varphi_n$, and the chain rule for $\varphi_n$, which depends on $x_4$ through $a_4(x_4)$: $d\varphi_n/dx_4 = \dot a_4\,\partial_a\varphi_n$.

Line 3.

$$
h\chi = \sum_n c_n\,\varepsilon_n\,\varphi_n .
$$

Rule: $h$ acts on each term (it is linear), and $h\varphi_n = \varepsilon_n\varphi_n$.

Line 4. Set line 2 equal to line 3, multiply from the left by $\varphi_m^\dagger$ and integrate over $y$:

$$
i\dot c_m + i\dot a_4\sum_n K_{mn}c_n = \varepsilon_m c_m, \qquad K_{mn} = \langle\varphi_m|\partial_a\varphi_n\rangle .
$$

Rule: by orthonormality $\langle\varphi_m|\varphi_n\rangle$ is 1 for $n = m$ and 0 otherwise, so of the first and the last sum only the term $n = m$ survives; the middle sum keeps all terms and defines the numbers $K_{mn}$.

Line 5.

$$
\dot c_m = -i\varepsilon_m c_m - \dot a_4\sum_n K_{mn}c_n .
$$

Rule: subtract $i\dot a_4\sum_n K_{mn}c_n$ from both sides and multiply by $-i$ (because $1/i = -i$). This is the equation that Notebook 22a integrates. It says that the amplitudes turn with the frequencies $\varepsilon_m$ and are mixed by the motion of the background, with the strength $\dot a_4 K_{mn}$.

Line 6. To compute $K_{mn}$ for $m \ne n$, differentiate the eigenvalue equation $h\varphi_n = \varepsilon_n\varphi_n$ with respect to $a_4$:

$$
(\partial_a h)\varphi_n + h\,\partial_a\varphi_n = (\partial_a\varepsilon_n)\varphi_n + \varepsilon_n\,\partial_a\varphi_n .
$$

Rule: the product rule on both sides.

$$
\langle\varphi_m|\partial_a h|\varphi_n\rangle + \varepsilon_m K_{mn} = 0 + \varepsilon_n K_{mn} .
$$

Rule: multiply from the left by $\varphi_m^\dagger$ and integrate; $h$ is Hermitian and its levels are real, so $\langle\varphi_m|h\psi\rangle = \langle h\varphi_m|\psi\rangle = \varepsilon_m\langle\varphi_m|\psi\rangle$ with $\psi = \partial_a\varphi_n$; and $\langle\varphi_m|\varphi_n\rangle = 0$ for $m \ne n$.

$$
K_{mn} = \frac{\langle m|\partial_a h|n\rangle}{\varepsilon_n - \varepsilon_m} \qquad (m \ne n) .
$$

Rule: subtract $\varepsilon_m K_{mn}$ and divide by $\varepsilon_n - \varepsilon_m$, which is not zero for different levels of one sector; $\langle m|X|n\rangle$ is short for $\langle\varphi_m|X\varphi_n\rangle$. PROVED: check `adiabatic_offdiagonal_identity` of `Revision/kohn_sham/reports/ks-theory-python.json`.

Line 7. $K_{nn} = 0$:

$$
1 = \langle\varphi_n|\varphi_n\rangle = \int(a_n^2 + b_n^2)\,dy \quad\Longrightarrow\quad 0 = 2\int(a_n\partial_a a_n + b_n\partial_a b_n)\,dy = 2K_{nn} .
$$

Rule: differentiate the normalisation with respect to $a_4$ (the derivative of the constant 1 is 0); with $\varphi_n = (a_n, ib_n)$ and real $a_n$, $b_n$ the integrand of $K_{nn}$ is $a_n\partial_a a_n + (-ib_n)(i\partial_a b_n) = a_n\partial_a a_n + b_n\partial_a b_n$.

Line 8. In the free field only $\kappa$ depends on $a_4$, and

$$
\partial_a\kappa = \partial_a e^{-Hy - a_4} = -\kappa, \qquad \partial_a h = -j\kappa k\,\sigma_3 .
$$

Rule: the derivative of $e^{-a_4}$ with respect to $a_4$ is $-e^{-a_4}$; $M = 1$ and $v = 0$ do not depend on $a_4$. PROVED: the record states $\partial_a h_j = -j\kappa k\sigma_3$ for frozen potentials (`Revision/kohn_sham/ks-theory.json`, key `adiabaticity.derivative`) and verifies it with the check `adiabatic_hellmann_feynman` of `Revision/kohn_sham/reports/ks-theory-python.json`. Lines 1 to 5 and line 7 are derivations of this book, which no Revision check covers.

$$
\langle m|\partial_a h|n\rangle = -k\,e^{-a_4}\int_{-L}^{0}e^{-Hy}\,(a_ma_n - b_mb_n)\,dy \qquad (j = +1) .
$$

Rule: $\kappa = e^{-Hy}e^{-a_4}$ (the rule $e^{s + t} = e^se^t$), and $\varphi_m^\dagger\sigma_3\varphi_n = a_ma_n - b_mb_n$ in the real form.

**The total probability in the amplitudes.** By orthonormality $\langle\chi|\chi\rangle = \sum_n|c_n|^2$, and it is 1 at all times by the conservation law above. Notebook 22a uses this as a test of its numerics: the computed $\sum_n|c_n|^2$ must stay 1.

### 22.7 What the adiabaticity measure Q measures, and two exact rules

**The dressing.** Let the history run at the constant rate $\dot a_4 = AH$, and let the particle be in level 0. If the other amplitudes are small, only the term $n = 0$ matters on the right of line 5 ("first order"), and over a short time the levels and the numbers $K_{m0}$ hardly change. The amplitude of level 0 then turns as $c_0 = e^{-i\varepsilon_0x_4}$. Try, for every $m \ne 0$, an amplitude that turns together with it, $c_m = \alpha_m e^{-i\varepsilon_0x_4}$ with a constant $\alpha_m$:

$$
-i\varepsilon_0\,\alpha_m e^{-i\varepsilon_0x_4} = -i\varepsilon_m\,\alpha_m e^{-i\varepsilon_0x_4} - AH\,K_{m0}\,e^{-i\varepsilon_0x_4} .
$$

Rule: the left side is $\dot c_m$ (the derivative of $e^{-i\varepsilon_0x_4}$ is $-i\varepsilon_0e^{-i\varepsilon_0x_4}$); the right side is line 5 with only $n = 0$ kept and $\dot a_4 = AH$.

$$
i(\varepsilon_m - \varepsilon_0)\,\alpha_m = -AH\,K_{m0} .
$$

Rule: divide by $e^{-i\varepsilon_0x_4}$, which is never zero, and add $i\varepsilon_m\alpha_m$ to both sides.

$$
\alpha_m = \frac{iAH\,K_{m0}}{\varepsilon_m - \varepsilon_0} .
$$

Rule: divide by $i(\varepsilon_m - \varepsilon_0)$ and use $-1/i = i$.

$$
|\alpha_m| = AH\,\frac{|\langle m|\partial_a h|0\rangle|}{(\varepsilon_0 - \varepsilon_m)^2} .
$$

Rule: insert line 6, $K_{m0} = \langle m|\partial_a h|0\rangle/(\varepsilon_0 - \varepsilon_m)$, and take the absolute value ($|i| = 1$).

This is exactly the record's adiabaticity measure $Q_{0m}$ (`Revision/kohn_sham/ks-theory.json`, key `adiabaticity.measure`: $Q_{nm} = AH|\langle n|\partial_a h|m\rangle|/(\varepsilon_n - \varepsilon_m)^2$ for $n$ occupied and $m$ empty in the same sector). So $Q$ has a plain meaning: it is the amplitude, and $Q^2$ the probability, of the admixture of level $m$ that a particle carries while the background moves, as long as $Q$ is much smaller than 1. This admixture is the dressing. It is not a transition: when the motion stops slowly, the dressing disappears again. The record itself calls $Q^2$ the leading-order transition probability (`Revision/kohn_sham/ks-theory.json`, key `adiabaticity.measure`). For a constant rate this book reads it instead as the probability of the dressing; this reading is a derivation of this book, not of the record, and Notebook 22a tests it numerically in In [14]: at $A = 0.3$ the exact evolution, started in the dressed state, agrees with $\sum_m Q_{0m}^2$ within 15 percent. Only when the motion is started or stopped abruptly is $Q^2$ of the size of a real transition: the abrupt start at $A = 1$ in Figure 22a.6 (right) leaves up to about three times the dressing.

**Exact rule 1: Q grows in proportion to the rate.** The levels, orbitals and matrix elements of a slice depend only on $a_{4,0}$, not on how fast $a_4$ changes. The rate enters $Q$ only through the factor $AH$. Hence $Q(A) = A\,Q(A = 1)$ exactly, and the naive criterion "breakdown when $Q$ reaches 1" puts the breakdown at the rate $A = 1/Q_{max}$, where $Q_{max}$ is the record's largest $Q$ at $A = 1$.

**Exact rule 2: one variable is enough.** In the free field $a_4$ enters $h$ only through the product

$$
\kappa k = e^{-Hy - a_{4,0}}\,k = e^{-Hy}\,\big(k\,e^{-a_{4,0}}\big) = e^{-Hy}\,q, \qquad q = k\,e^{-a_{4,0}} .
$$

Rule: $e^{s + t} = e^se^t$, and the factors are regrouped. So the Hamiltonian of momentum $k$ at the slice $a_{4,0}$ is the Hamiltonian of momentum $q$ at the slice 0: same levels, same orbitals. This is the rescaling identity of the record (`Revision/kohn_sham/ks-theory.json`, key `rescalingIdentity`; PROVED: check `rescaling_identity` of `Revision/kohn_sham/reports/ks-theory-python.json`; COMPUTED by the solver: check `free_rescaling_relation_and_band_monotone` of `Revision/kohn_sham/reports/ks-rust-solver.json`, which finds the two sides equal to 0.0). By line 8 the matrix element is $-q\int e^{-Hy}(a_ma_n - b_mb_n)\,dy$ with the orbitals of momentum $q$ at slice 0. Therefore, for $\lambda = 0$,

$$
\frac{Q}{A} = G(q) ,
$$

one function of one variable for every shell and every slice. We call $q$ the **redshifted momentum**. As the history goes on, the $q$ of every shell slides from $k$ towards 0.

### 22.8 The sudden limit, two histories and three estimates of the breakdown

**The adiabatic and the sudden limit.** At a very small rate the particle stays in its instantaneous level, up to the dressing (the **adiabatic limit**). At a very large rate the opposite happens. Suppose that $a_4$ jumps from the value $s_1$ to the value $s_2$ in a time interval of length $\tau$, and let $\tau$ go to zero. Integrating $\dot\chi = -ih\chi$ over the interval changes $\chi$ by at most $\tau$ times the largest size of $h\chi$ on it, which goes to zero with $\tau$. So just after the jump the orbital is still the orbital $\varphi_0(s_1)$ of the start. Expanded in the orbitals of the new slice,

$$
\varphi_0(s_1) = \sum_n\langle\varphi_n(s_2)|\varphi_0(s_1)\rangle\,\varphi_n(s_2) ,
$$

Rule: the expansion of line 1 at the slice $s_2$; the amplitudes follow by multiplying with $\varphi_n(s_2)^\dagger$ and integrating (orthonormality).

and the probability that the particle is no longer in level 0 is

$$
P_{sudden} = 1 - \big|\langle\varphi_0(s_2)|\varphi_0(s_1)\rangle\big|^2 = 1 - \Big(\int_{-L}^{0}\big(a_0(s_2)a_0(s_1) + b_0(s_2)b_0(s_1)\big)\,dy\Big)^2 .
$$

Rule: the probability of level 0 is the square of the absolute value of its amplitude, and the probabilities of all levels add up to 1; in the real form the overlap is a real integral. The sudden limit depends only on how much the band orbital itself changes between the two slices. In the language of line 5, an infinitely fast passage is line 5 without the term $-i\varepsilon_mc_m$, which has no time to act; Notebook 22a computes the sudden limit both ways.

**Time measured in units of the passage.** Let a passage from $a_4 = 0$ to $a_4 = 2$ (the span of the record's slices) last the time $T$, and write $x_4 = Tu$ with $u$ running from 0 to 1. Then

$$
\frac{dc_m}{du} = T\,\frac{dc_m}{dx_4} = -iT\varepsilon_m c_m - \frac{da_4}{du}\sum_n K_{mn}c_n .
$$

Rule: the chain rule, $dc/du = (dx_4/du)(dc/dx_4) = T\,dc/dx_4$, applied to line 5, and $T\dot a_4 = da_4/du$ by the same rule.

**The smooth passage.** The first history of Notebook 22a is

$$
a_4(u) = 2\Big[u - \frac{\sin(2\pi u)}{2\pi}\Big] .
$$

At $u = 0$ it is 0 and at $u = 1$ it is 2, because $\sin 0 = \sin 2\pi = 0$. Its rate:

$$
\frac{da_4}{du} = 2\big[1 - \cos(2\pi u)\big] = 4\sin^2(\pi u) .
$$

Rule: the derivative of $\sin(2\pi u)/(2\pi)$ is $\cos(2\pi u)$; then the identity $1 - \cos 2\theta = 2\sin^2\theta$ with $\theta = \pi u$.

$$
\frac{da_4}{dx_4} = \frac{1}{T}\,\frac{da_4}{du} = \frac{4}{T}\sin^2(\pi u) .
$$

Rule: the chain rule with $du/dx_4 = 1/T$. The rate starts at 0, rises to its peak $4/T$ at $u = 1/2$ (where $\sin^2(\pi/2) = 1$) and falls back to 0. With $H = 1$ the peak rate is $A = 4/T$, so a passage with peak rate $A$ lasts $T = 4/A$. Because the rate vanishes at both ends, the particle carries no dressing at the start and at the end: whatever probability has left level 0 at the end is a real transition.

**The constant rate.** The second history is the record's kind, $a_4 = 2u$, with the constant rate $da_4/dx_4 = 2/T = A$, so $T = 2/A$. Here the particle carries the dressing all the time, and the test is whether the exact evolution reproduces the first-order dressing $\sum_m Q_{0m}^2$ of Section 22.7.

**First order for the smooth passage.** Write $c_m = d_m\,e^{-iT\int_0^u\varepsilon_m\,du'}$, which removes the fast turning of each amplitude, and keep on the right of the $u$-equation only $c_0 = e^{-iT\int_0^u\varepsilon_0\,du'}$:

$$
\frac{dd_m}{du} = -\frac{da_4}{du}\,K_{m0}\,e^{iT\int_0^u(\varepsilon_m - \varepsilon_0)\,du'} .
$$

Rule: the product rule gives $dc_m/du = (dd_m/du - iT\varepsilon_m d_m)\,e^{-iT\int\varepsilon_m}$; the term $-iT\varepsilon_m c_m$ of the equation cancels the second part; dividing by $e^{-iT\int\varepsilon_m}$ and inserting $c_0$ gives the right side.

$$
d_m(1) = -\int_0^1\frac{da_4}{du}\,K_{m0}\,e^{iT\int_0^u(\varepsilon_m - \varepsilon_0)\,du'}\,du, \qquad P^{(1)} = \sum_{m \ne 0}|d_m(1)|^2 .
$$

Rule: integrate from $u = 0$, where $d_m = 0$ (the particle starts in level 0), to $u = 1$; $|c_m| = |d_m|$ because the exponential has absolute value 1. For a slow passage (large $T$) the fast-turning exponential makes the integral small: the transitions die out. This is a derivation of this book; Notebook 22a tests it against the exact evolution.

**Three estimates of the breakdown.** The instantaneous picture breaks down when the probability $P$ that a particle is not in its instantaneous level stops being small. Notebook 22a compares three estimates of the rate at which that happens:

1. the naive estimate: $Q$ reaches 1, that is $A = 1/Q_{max}$ (exact rule 1);
2. the first-order estimate: the dressing probability $(AQ_0)^2$ reaches the sudden value $P_{sudden}$ of the passage from $a_{4,0} = 0$ to $2$, that is $A = \sqrt{P_{sudden}}/Q_0$, where $Q_0$ is the record's largest $Q$ of the free state $N = 688$ at the slice 0;
3. the exact evolution: the rate $A_{1/2}$ at which the exact $P$ of the smooth passage reaches half of $P_{sudden}$.

### 22.9 Example: when does the instantaneous picture break down (Notebook 22a)

Notebook 22a carries out the first step of Problem 2. It reads the table `Revision/kohn_sham/results/adiabatic/adiabaticity.csv` (the largest $Q$ of each of the 75 ground states), `Revision/kohn_sham/results/adiabatic/history.json` (the status of the history), `Revision/kohn_sham/results/ground/levels` (the level tables), `Revision/kohn_sham/results/parameters.json` (the units and numerical parameters) and `Revision/kohn_sham/ks-theory.json`. It writes the solver's shooting method again in Python for the free block, reproduces the record's levels and $Q$, draws the one curve $G(q)$ of exact rule 2, measures the jumps into the negative branch, and integrates the amplitude equation of Section 22.6 in a basis of 20 instantaneous levels for the smooth passage and the constant rate of Section 22.8. Everything that is computed beyond the record is computed for the free field ($\lambda = 0$) and for one sector: $j = +1$, even brane parity, the Fermi shell $n_2 = 11$ of $N = 688$. It needs only numpy and matplotlib, takes about a minute (the recorded build and check runs of 2026-10-08 took 32 and 30 seconds; on a machine busy with other jobs the same run has taken up to 110 seconds), draws eight figures and ends with the line ALL 20 CHECKS PASSED (notebook 22a).

<!-- NOTEBOOK 22a -->

### 22.12 Line-by-line walk-through of Notebook 22a

The notebook has 17 code cells, In [1] to In [17]. This section explains every line of every one of them, in order. In the notebook each code cell is preceded by a text cell that says what the cell does; the printed output of each cell is in Section 22.11 under the label Out [k], and the eight figures are shown there with their captions. For each figure this section adds what the student should see and why.

**In [1], the set-up cell.** It is the same in every notebook of the book except for the notebook's name. Its first 231 lines repeat the complete run instructions of Section 22.10 as **comment lines**: every line that starts with `#` is skipped by Python and is there only so that the notebook file carries its own instructions. A line of dashes and the title THE SET-UP between two lines of `=` signs mark where the code begins.

```python
import json  # reads and writes JSON files (text files that hold names and numbers)
import os  # reads the environment variable TEXTBOOK_OUTPUT_ROOT (explained below)
import textwrap  # breaks long printed text into lines of at most 89 characters
from pathlib import Path  # file and folder paths that work on Windows, macOS and Linux

import matplotlib  # the plotting package
import matplotlib.pyplot as plt  # its drawing functions, called plt by convention
from IPython.display import Image, display  # shows a saved picture below a cell

NOTEBOOK_ID = "22a"  # this notebook: chapter 22, example a
```

`import` loads a **module** (a part of Python or of an installed package) so that the cell can use it; the text after `#` on each line is a comment that says what the module is for. `json` reads the text format JSON in which most Revision records are stored. `os` gives access to the operating system, here to read an environment variable. `textwrap` breaks long printed text into lines. `from pathlib import Path` takes the single name `Path` out of the module `pathlib`; a `Path` is the address of a file or folder, written the same way on every operating system. `matplotlib` is the plotting package and `matplotlib.pyplot` its drawing functions, called `plt` by convention. `Image` and `display` show a saved picture below a cell. The last line gives the name `NOTEBOOK_ID` to the **string** (a text in quotes) `"22a"`; the figure files are named after it.

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

`def` defines a **function**: a named piece of code that runs when it is called. The text in triple quotes under the `def` line is its **docstring**, a description that Python keeps but does not run. `Path.cwd()` is the folder in which the notebook runs, and `.resolve()` writes it as a complete address. The list `[here, *here.parents]` holds this folder followed by its parent, the parent of that, and so on (the star unpacks the parents into the list), and the `for` loop takes them one after the other. The operator `/` joins a folder and a name into a longer path, and `.is_file()` is true when that file exists. The first folder that holds `Revision/textbook/requirements.txt` is the repository, and `return` hands it back; if no folder does, `raise` stops the notebook with an error message that says what to do.

```python
# The repository folder.  It is never printed: it differs from computer to computer,
# and the printed output of a notebook must not.
REPO = find_repository_root()
# Every file is WRITTEN below OUTPUT_ROOT.  OUTPUT_ROOT is the repository folder unless
# the environment variable TEXTBOOK_OUTPUT_ROOT names another folder; the book's
# checking tool sets it, so that a check run writes into a scratch folder instead.
OUTPUT_ROOT = Path(os.environ.get("TEXTBOOK_OUTPUT_ROOT", str(REPO)))


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

`REPO` is the repository folder; it is never printed, because it differs from computer to computer while the printed output must be the same everywhere. `os.environ.get(name, default)` reads an **environment variable** (a named text that a program receives from the computer) or returns the default; when you run the notebook the variable TEXTBOOK_OUTPUT_ROOT is not set, so `OUTPUT_ROOT` is the repository, while the book's checking tool sets it to a scratch folder so that a check never changes the repository. `repository_file` gives the full path of a repository file for reading; `output_file` gives the full path at which to write one, after creating its folder (`mkdir` with `parents=True` creates missing parent folders as well, and `exist_ok=True` makes it do nothing if the folder exists). `say` prints a text in lines of at most 89 characters, continuation lines indented by four blanks.

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

`matplotlib.rcdefaults()` returns to the built-in plotting settings, so that the figures are the same on every computer, and `plt.rcParams.update` sets the default figure size (7.0 by 4.2 inches), the letter size (10 points) and a faint grid. The braces `{...}` make a **dictionary**: pairs of a key and a value, written `key: value`. A string that starts with `f` is an **f-string**: every name in braces is replaced by its value, so `CAPTION_FILE` is `"Revision/textbook/figures/22a.captions.json"`. `FIGURE_NUMBERS` and `CAPTIONS` start as empty dictionaries. The last line writes an empty dictionary `{}` into the captions file; `newline="\n"` stores the same line end on every operating system.

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

`save_figure` numbers the figures 1, 2, 3, ... in the order in which they are saved (`setdefault` returns the number already stored for this name, or stores one more than the count so far), saves the figure as a PNG file with 150 dots per inch, cut to its content and without the program's name inside (so that two runs write the same bytes), closes it, records its caption in the captions file (`json.dumps` turns the dictionary into JSON text, one entry per line, keys sorted), shows the saved picture below the cell, and prints where it was saved. The caption given to it is the caption that the book prints under the figure.

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


def report(label, value, unit=""):
    """Print a key number as a line "RESULT <label> = <value> <unit>"."""
    say(f"RESULT {label} = {value}" + (f" {unit}" if unit else ""))


def all_checks_passed():
    """Print the last line of the notebook: how many checks passed."""
    print(f"ALL {len(PASSED)} CHECKS PASSED (notebook {NOTEBOOK_ID})")


say(f"Set-up of notebook {NOTEBOOK_ID} complete: repository folder found, helpers "
    "defined.")
```

`PASSED` is an empty **list** (an ordered collection, in square brackets). `check` is the function behind every check of the notebook: if the statement `condition` is false, `raise AssertionError(...)` stops the notebook with an error that names the check; if it is true, the name is appended to `PASSED` and the line PASS followed by the name is printed, and a second line names the Revision record when the argument `record` is given (`None` is Python's word for "nothing"). Python's own `assert` statement is not used, because Python started with the option `-O` skips it. `report` prints a key number as a line that starts with RESULT. `all_checks_passed` prints the last line of the notebook with the number of checks that passed (`len` is the length of a list). The last statement prints the one output line of In [1].

**In [2], the record: Q of the 75 ground states.**

```python
import csv  # reads the tables (CSV files) of the Revision record
import math  # exp, sqrt and log of single numbers

import numpy as np  # arrays of numbers and their arithmetic
from numpy.polynomial import chebyshev  # Chebyshev polynomials (section 11)
```

Four more modules: `csv` reads tables stored as CSV files (comma-separated values: one line per row, the entries separated by commas); `math` computes the exponential, square root and logarithm of single numbers; `numpy`, called `np`, holds **arrays** (tables of numbers of any shape) and computes with whole arrays at once; and `chebyshev` evaluates sums of Chebyshev polynomials, which In [9] uses.

```python
ADIABATIC = "Revision/kohn_sham/results/adiabatic/adiabaticity.csv"
HISTORY = "Revision/kohn_sham/results/adiabatic/history.json"
THEORY = "Revision/kohn_sham/ks-theory.json"
SLICES = [0.0, 0.5, 1.0, 1.5, 2.0]  # the slices a4,0 of the record
TAGS = ["lam0", "lamp1", "lamm1", "lamp2", "lamm2"]  # 0, +-lambda_1, +-lambda_2
PALETTE = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300",
           "#4a3aa7", "#e34948"]  # the colours of the figures, in a fixed order
```

Three names for the repository paths of the records the cell reads; the five slices of the record; the five coupling tags; and eight colours, written as hexadecimal codes, which every figure uses in this fixed order (blue, orange, green, yellow, pink, dark green, violet, red).

```python
def state_id(n, a4, tag="lam0"):
    """The record's name of a ground state, for example N688_lam0_a05."""
    return f"N{n}_{tag}_a{round(10 * a4):02d}"
```

`state_id` builds the record's name of a state: for $n = 688$, $a_4 = 0.5$ and the default tag lam0 it returns `N688_lam0_a05`. Inside the braces of the f-string, `round(10 * a4)` turns the slice into the whole number 5, and the format `:02d` writes it with two digits, padded by a zero.

```python
with open(repository_file(ADIABATIC), newline="", encoding="utf-8") as handle:
    record = {row["id"]: row for row in csv.DictReader(handle)}
history = json.loads(repository_file(HISTORY).read_text(encoding="utf-8"))
theory = json.loads(repository_file(THEORY).read_text(encoding="utf-8"))
```

`with open(...) as handle:` opens the table and closes it again when the indented line has run. `csv.DictReader` reads it row by row, each row a dictionary from the column names of the first line (`id`, `N`, `lambda_tag`, `Q_max`, `Q_max_pair`, ...) to the texts of that row. The braces with `for` inside make a **dictionary comprehension**: `record` maps each state's name (column `id`) to its row. `json.loads` turns the text of the two JSON files into Python dictionaries.

```python
q_max = {(n, tag, a4): float(record[state_id(n, a4, tag)]["Q_max"])
         for n in (8, 136, 688) for tag in TAGS for a4 in SLICES}
largest = max(q_max.values())
n8_zero = all(q_max[(8, tag, a4)] == 0.0 for tag in TAGS for a4 in SLICES)
```

`q_max` maps every triple (particle number, tag, slice), a **tuple** written in round brackets, to the number in the column `Q_max` of that state; `float` turns the text into a number. The two lines of the comprehension run over the 3 particle numbers, the 5 tags and the 5 slices: 75 states. `largest` is the largest of all 75 values. `all(...)` is true when every one of the 25 values for $N = 8$ is exactly zero.

```python
report("ground states in the record", len(record))
report("largest Q_max at the rate A = 1", f"{largest:.10f}")
say("The record's measure: " + theory["adiabaticity"]["measure"])
```

Out [2] shows 75 states and the largest value $0.0934532439$, printed with ten digits after the point (format `.10f`), and then the record's own definition of $Q$ from the key `adiabaticity.measure` of `ks-theory.json`: the formula derived in Section 22.7, with the remark that $Q^2$ is the leading-order transition probability.

```python
check(history["status"].startswith("PRESCRIBED BACKGROUND")
      and theory["adiabaticity"]["historyStatus"].startswith("PRESCRIBED BACKGROUND"),
      "the history a4 = A H x4 is labelled a PRESCRIBED BACKGROUND",
      record=f"{HISTORY}, key status, and {THEORY}, adiabaticity.historyStatus")
check(len(record) == 75 and largest <= 0.0935 and n8_zero,
      "75 states, Q_max <= 0.0935, and Q_max = 0 exactly for N = 8",
      record=f"{ADIABATIC}, column Q_max")
```

The first check requires that both records begin their statement of the history with the words PRESCRIBED BACKGROUND (`startswith` tests the beginning of a string): the notebook works on a background that is given, not solved for, and says so. The second check requires the 75 rows, the bound $0.0935$ and the exact zeros for $N = 8$. Those zeros have a reason: the eight quanta of $N = 8$ occupy only the zero modes at $k = 0$, and at $k = 0$ the derivative $\partial_a h = -j\kappa k\sigma_3$ of Section 22.6 vanishes.

**In [3], Q grows in proportion to the rate (Figure 22a.1).**

```python
naive = {key: 1.0 / value for key, value in q_max.items() if value > 0.0}
weakest = min(naive, key=naive.get)  # the state that reaches Q = 1 first
rates = np.geomspace(0.1, 100.0, 200)  # rates A for the right panel
```

By exact rule 1 of Section 22.7, $Q$ reaches 1 at the rate $A = 1/Q_{max}$. `naive` maps every state with $Q_{max} > 0$ (the 50 states with $N = 136$ and $688$) to this rate. `min(naive, key=naive.get)` returns the key whose value is smallest: the state that would reach $Q = 1$ first. `np.geomspace(0.1, 100.0, 200)` makes 200 rates from $0.1$ to $100$, equally spaced on a logarithmic scale (each one the same factor larger than the one before).

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.2), layout="constrained")
for colour, marker, n in ((PALETTE[0], "o", 136), (PALETTE[1], "s", 688)):
    band = np.array([[naive[(n, tag, a4)] for a4 in SLICES] for tag in TAGS])
    left.fill_between(SLICES, band.min(axis=0), band.max(axis=0), color=colour,
                      alpha=0.25, lw=0)  # the spread over the five couplings
    left.plot(SLICES, band[0], "-", color=colour, marker=marker, ms=8, lw=2.0,
              label=f"$N = {n}$")
```

`plt.subplots(1, 2, ...)` makes a figure with two panels side by side, `left` and `right`, 10 by 4.2 inches, with the layout adjusted automatically. For $N = 136$ (blue circles) and $N = 688$ (orange squares) the loop builds `band`, an array with one row per tag and one column per slice. `fill_between` shades the area between the smallest and the largest value of each column (`axis=0` takes the minimum down the columns), that is, the spread over the five couplings, a quarter opaque (`alpha=0.25`) and without border (`lw=0`). `left.plot` draws the first row, the free state lam0, as a line with markers of size 8.

```python
left.axhline(1.0, color="0.3", lw=1.2, ls=":")
left.text(0.05, 1.12, "the record's rate $A = 1$", fontsize=8, color="0.3")
left.set_yscale("log")
left.set_ylim(0.7, 50.0)
left.set_xlabel("slice $a_{4,0}$")
left.set_ylabel("naive breakdown rate $1/Q_{max}$")
left.set_title("Rate at which $Q$ would reach 1")
left.legend(fontsize=8)
```

A dotted horizontal line at $A = 1$, the record's rate, with a small label; a logarithmic vertical axis from $0.7$ to $50$; the axis labels, the title and the legend. Text between dollar signs is set as mathematics by matplotlib.

```python
for colour, a4 in zip(PALETTE, SLICES):
    right.plot(rates, rates * q_max[(688, "lam0", a4)], color=colour, lw=2.0,
               label=f"$a_{{4,0}} = {a4}$")
right.axhline(1.0, color="0.3", lw=1.2, ls=":")
right.axvline(1.0, color="0.3", lw=1.2, ls="--")
right.text(1.08, 0.012, "record: $A = 1$", fontsize=8, color="0.3")
right.set_xscale("log")
right.set_yscale("log")
right.set_xlabel("rate $A$ (e-folds of the extra times per unit time $1/H$)")
right.set_ylabel("$Q = A\\,Q_{max}$")
right.set_title("$N = 688$, $\\lambda = 0$: $Q$ grows like $A$")
right.legend(fontsize=8)
```

`zip` pairs the first five colours with the five slices. For each slice the right panel draws $Q = A\,Q_{max}$ of the free state $N = 688$ against the 200 rates. In the f-string the doubled braces `{{4,0}}` print single braces, so the label reads $a_{4,0} = 0.5$ and so on. A dotted line marks $Q = 1$, a dashed vertical line the record's rate; both axes are logarithmic. In a normal Python string a backslash starts an escape, so `\\,` and `\\lambda` are written with two backslashes to give matplotlib the single backslash of `\,` (a thin space) and of `\lambda`.

```python
save_figure(fig, "naive_rates",
            "Left: the naive breakdown rate $1/Q_{max}$ (vertical axis, logarithmic) "
            "of the ground states $N = 136$ (blue circles) and $N = 688$ (orange "
            "squares) against the slice $a_{4,0}$ (horizontal axis); the lines are "
            "the free states, the shaded bands the spread over the five couplings, "
            "the dotted line the record's rate $A = 1$. Right: $Q = A\\,Q_{max}$ "
            "against the rate $A$ for the free state $N = 688$ at the five slices "
            "(both axes logarithmic); $Q$ reaches 1 (dotted) only above $A = 10$. "
            "The naive estimate says the record's history is at least ten times "
            "too slow to break the instantaneous picture.")
report(f"naive breakdown rate 1/Q_max of {state_id(weakest[0], weakest[2], weakest[1])}",
       f"{naive[weakest]:.4f}")
check(naive[weakest] > 10.0,
      "every recorded state keeps Q below 1 up to the rate A = 10",
      record=f"{ADIABATIC}, column Q_max")
```

`save_figure` saves Figure 22a.1 with its caption (Python joins strings written next to each other into one). The report names the weakest state, N688_lamm2_a00 (the tuple `weakest` is (688, "lamm2", 0.0), so `weakest[0]` is the particle number, `weakest[2]` the slice and `weakest[1]` the tag), and its naive breakdown rate $10.7005$ (Out [3]). The check requires that every recorded state keeps $Q$ below 1 up to the rate $A = 10$.

*What the student should see in Figure 22a.1, and why.* On the left every point lies far above the dotted line: the naive breakdown rate is between $10.7$ (N688_lamm2_a00) and $27.8$ (N136_lamm2_a20; $26.05$ for the free state N136 at the slice 2), so by this measure the record's history is at least ten times too slow to disturb the instantaneous picture. Both curves rise with the slice: as the history goes on, the momentum of the Fermi shell redshifts, $q = ke^{-a_{4,0}}$ falls, and $Q/A$ falls with it (Figure 22a.2 shows why). The shaded bands are thin: the five couplings change $Q_{max}$ by at most about ten percent. On the right the five lines are straight with slope 1 on the logarithmic axes, which is exact rule 1: ten times the rate gives ten times $Q$. They cross the dotted line $Q = 1$ between $A = 10.7$ and $A = 18.9$.

**In [4], the solver's shooting method, vectorised.**

```python
PARAMETERS = json.loads(repository_file("Revision/kohn_sham/results/parameters.json")
                        .read_text(encoding="utf-8"))
L = PARAMETERS["physics"]["L_tipCutoff"]  # the tip cutoff y = -L
STEPS = PARAMETERS["numerics"]["rk4Steps"]  # RK4 steps from the tip to the brane
POINTS = 2 * STEPS + 1  # the fine grid: step ends and step midpoints
STEP = L / STEPS  # the length of one RK4 step in y
```

The cell reads the record's parameter file and takes from it the tip cutoff $L = 3$ and the number of RK4 steps, 900, with which the Rust solver integrates from the tip $y = -L$ to the brane $y = 0$. RK4 evaluates the equation at the start, the middle and the end of every step, so the notebook keeps a **fine grid** of $2 \cdot 900 + 1 = 1801$ points: the 901 step ends and the 900 midpoints. One step has the length $3/900 = 1/300$.

```python
Y = -L * ((POINTS - 1 - np.arange(POINTS)) / (POINTS - 1))  # y from -L to 0
EW = np.exp(-Y)  # e^{-Hy} with H = 1, so kappa k = q e^{-y} with q = k e^{-a4,0}
SIMPSON = np.full(POINTS, 2.0 * STEP / 6.0)  # Simpson weights on the fine grid:
SIMPSON[1::2] = 4.0 * STEP / 6.0  # midpoints carry 4/6 of a step,
SIMPSON[0] = SIMPSON[-1] = STEP / 6.0  # the two ends 1/6
```

`np.arange(POINTS)` is the array $0, 1, \ldots, 1800$; the formula turns it into the 1801 values of $y$, from $-3$ at index 0 to $0$ at the last index, equally spaced. `EW` holds $e^{-y}$ at every point: with $H = 1$ the momentum term of Section 22.6 is $\kappa k = qe^{-y}$ (exact rule 2). `SIMPSON` holds the weights of **Simpson's rule**: the integral of a function over one step is $\tfrac{h}{6}(f_{start} + 4f_{middle} + f_{end})$ with $h$ the step length, and adding these over all steps gives every midpoint the weight $4h/6$, every inner step end $2h/6$ (it belongs to two steps), and the two outer ends $h/6$. `np.full` fills an array with one value, `SIMPSON[1::2]` selects every second entry starting at index 1 (the midpoints), and the index `-1` means the last entry. An integral is then `np.sum(SIMPSON * f)`.

```python
check(PARAMETERS["physics"]["H"] == 1.0 and PARAMETERS["physics"]["m"] == 1.0
      and L == 3.0 and STEPS == 900 and PARAMETERS["physics"]["dk"] == 0.25,
      "the record's units H = m = 1, tip cutoff L = 3, lattice step 0.25, 900 steps",
      record="Revision/kohn_sham/results/parameters.json, physics and numerics")
```

The check requires the record's units $H = m = 1$, $L = 3$, the lattice step $\Delta k = 0.25$ of the 3-momenta and 900 steps, the numbers on which everything below relies (Out [4]).

```python
def shoot(eps, q, store=False):
    """Integrate the free block equation from the tip to the brane for the arrays
    eps (energies) and q (redshifted momenta) at once.  Returns the phase
    Phi = theta(0) and, if store is True, the list of (a, b) at the step ends."""
    a, b = np.ones_like(eps), np.zeros_like(eps)  # tip: b(-L) = 0, a(-L) = 1
    theta, raw = np.zeros_like(eps), np.zeros_like(eps)  # the angle, last atan2
    ends = [(a, b)] if store else None
```

`shoot` solves the real form of the free block equation of Section 22.6 ($j = +1$, $M = 1$, $v = 0$), $a' = a - (qe^{-y} + \varepsilon)b$, $b' = (\varepsilon - qe^{-y})a - b$, for a trial energy $\varepsilon$, from the tip to the brane. It is **vectorised**: `eps` and `q` are arrays, and every line acts on all their entries at once, so one call solves hundreds of cases. At the tip it starts with $a = 1$, $b = 0$ (`np.ones_like` and `np.zeros_like` make arrays of ones and zeros of the same shape as `eps`); $b(-L) = 0$ is the record's regular tip condition, and the size of $a$ is irrelevant because the equation is linear. `theta` will hold the **Pruefer angle**, the angle of the point $(a, b)$ in the plane, followed continuously; `raw` holds the angle of the previous step; `ends` collects the values $(a, b)$ at the step ends when `store` is true.

```python
    for i in range(STEPS):
        k0, k1, k2 = q * EW[2 * i], q * EW[2 * i + 1], q * EW[2 * i + 2]
        p1a, p1b = a - (k0 + eps) * b, (eps - k0) * a - b  # (a', b') at the start
        aa, bb = a + 0.5 * STEP * p1a, b + 0.5 * STEP * p1b
        p2a, p2b = aa - (k1 + eps) * bb, (eps - k1) * aa - bb  # at the midpoint
        aa, bb = a + 0.5 * STEP * p2a, b + 0.5 * STEP * p2b
        p3a, p3b = aa - (k1 + eps) * bb, (eps - k1) * aa - bb  # midpoint again
        aa, bb = a + STEP * p3a, b + STEP * p3b
        p4a, p4b = aa - (k2 + eps) * bb, (eps - k2) * aa - bb  # at the end
        a = a + STEP / 6.0 * (p1a + 2.0 * p2a + 2.0 * p3a + p4a)  # the RK4 step
        b = b + STEP / 6.0 * (p1b + 2.0 * p2b + 2.0 * p3b + p4b)
```

The loop takes the 900 steps. `k0`, `k1`, `k2` are $qe^{-y}$ at the start, the middle and the end of step `i` (fine-grid indices $2i$, $2i + 1$, $2i + 2$). Then comes the classical **Runge-Kutta rule of order 4** (RK4, Chapter 2): the first slope `p1` from the equation at the start; a half step with it to the midpoint and the second slope `p2` there; a half step with `p2` and the third slope `p3`, again at the midpoint; a full step with `p3` and the fourth slope `p4` at the end; and the new values as the start plus one step times the weighted mean $(p_1 + 2p_2 + 2p_3 + p_4)/6$. Each line computes the two components $a$ and $b$ side by side.

```python
        new = np.arctan2(b, a)  # the angle of the point (a, b), in (-pi, pi]
        turn = new - raw  # how far the angle turned in this step, brought back
        turn = np.where(turn > np.pi, turn - 2.0 * np.pi, turn)  # into (-pi, pi]
        turn = np.where(turn <= -np.pi, turn + 2.0 * np.pi, turn)
        theta, raw = theta + turn, new  # the angle, followed continuously
        if store:
            ends.append((a, b))
    return theta, ends
```

`np.arctan2(b, a)` is the angle of the point $(a, b)$, between $-\pi$ and $\pi$. When the point circles around the origin this angle jumps by $2\pi$ as it passes $\pi$; the next three lines remove such jumps: the turn of one step is brought back into the range $(-\pi, \pi]$ (`np.where(condition, x, y)` takes `x` where the condition holds and `y` elsewhere), and adding the turns gives the angle followed continuously. The steps are short, so the true turn of one step is far below $\pi$ and this is safe. At the brane, $\Phi = \theta(0)$ is the phase of the orbital. Chapter 15 showed for the Rust solver why this counts levels: $\Phi$ grows with $\varepsilon$, and $b(0) = 0$, the even brane condition, holds exactly when $\Phi$ is a whole multiple of $\pi$; the level with label $n$ is the energy with $\Phi = n\pi$. The function returns the phases and, if asked, the stored values.

```python
def levels(labels, q):
    """The level with label n (Phi = n pi) for every pair (label, q): bisection on
    [-40, 40], halving the bracket until it is shorter than 1e-13."""
    target = np.pi * np.asarray(labels, dtype=float)
    q = np.asarray(q, dtype=float)
    low, high = np.full(q.shape, -40.0), np.full(q.shape, 40.0)
    while np.max(high - low) > 1e-13:  # 50 halvings of the length 80
        middle = 0.5 * (low + high)
        above = shoot(middle, q)[0] > target  # Phi grows with eps
        low, high = np.where(above, low, middle), np.where(above, middle, high)
    return 0.5 * (low + high)
```

`levels` finds, for every pair of a label $n$ and a momentum $q$, the energy at which $\Phi = n\pi$, by **bisection** (Chapter 2): every level lies in the bracket $[-40, 40]$; the phase is computed in the middle of the bracket; if it is above the target, the level lies in the lower half, otherwise in the upper half; the bracket is halved until it is shorter than $10^{-13}$, the root tolerance of the Rust solver. Starting from the length 80 this takes 50 halvings, because $80/2^{50} \approx 7 \times 10^{-14}$. All pairs are bisected together, one vectorised call of `shoot` per halving. The answer is the middle of the last bracket.

```python
def orbitals(eps, q):
    """The normalised orbitals (a, b) on the fine grid, one row per (eps, q)."""
    ends = shoot(eps, q, store=True)[1]
    a_e = np.array([pair[0] for pair in ends]).T  # rows: orbitals; columns: ends
    b_e = np.array([pair[1] for pair in ends]).T
    kap = q[:, None] * EW[None, 0::2]  # kappa k at the step ends
    da = a_e - (kap + eps[:, None]) * b_e  # the derivatives at the step ends
    db = (eps[:, None] - kap) * a_e - b_e
```

`orbitals` integrates again at the found levels, this time storing $a$ and $b$ at the 901 step ends, and arranges them as arrays with one row per orbital and one column per step end (`.T` transposes, that is, exchanges rows and columns). `q[:, None] * EW[None, 0::2]` multiplies a column of momenta with a row of the values $e^{-y}$ at the step ends (`0::2` takes every second fine-grid point from index 0), which gives the table $qe^{-y}$ for every orbital and every step end; `None` adds a dimension of length 1 so that numpy repeats the column and the row (**broadcasting**). `da` and `db` are the derivatives $a'$ and $b'$ from the block equation at every step end.

```python
    a, b = np.zeros((len(eps), POINTS)), np.zeros((len(eps), POINTS))
    a[:, 0::2], b[:, 0::2] = a_e, b_e
    # cubic Hermite midpoint: (left + right)/2 + STEP (left' - right')/8
    a[:, 1::2] = 0.5 * (a_e[:, :-1] + a_e[:, 1:]) + STEP / 8.0 * (da[:, :-1] - da[:, 1:])
    b[:, 1::2] = 0.5 * (b_e[:, :-1] + b_e[:, 1:]) + STEP / 8.0 * (db[:, :-1] - db[:, 1:])
    norm = np.sqrt(np.sum(SIMPSON * (a * a + b * b), axis=1))  # Simpson's rule
    return a / norm[:, None], b / norm[:, None]
```

The orbitals are needed on the whole fine grid. The step ends are copied into the even columns. The midpoints are filled by **cubic Hermite interpolation**: the cubic polynomial with the values $f_0$, $f_1$ and the slopes $f_0'$, $f_1'$ at the two ends of a step of length $h$ has, in the middle, the value $(f_0 + f_1)/2 + h(f_0' - f_1')/8$ (Exercise 3 of Section 22.20 derives it); `a_e[:, :-1]` are the left ends of all steps and `a_e[:, 1:]` the right ends. This is what the Rust solver does. Finally each orbital is **normalised**: its norm $\sqrt{\int(a^2 + b^2)\,dy}$ is computed with Simpson's rule (`axis=1` sums along each row), and both components are divided by it, so that $\int(a^2 + b^2)\,dy = 1$.

```python
def couplings(q, a, b):
    """The matrix <m| d_a h |n> = -q int e^{-y} (a_m a_n - b_m b_n) dy of the
    orbitals (rows of a and b) of one sector at the redshifted momentum q."""
    weight = SIMPSON * EW  # Simpson weights times e^{-y}
    return -q * ((a * weight) @ a.T - (b * weight) @ b.T)
```

`couplings` computes the matrix of line 8 of Section 22.6 in its rescaled form (exact rule 2), $\langle m|\partial_a h|n\rangle = -q\int e^{-y}(a_ma_n - b_mb_n)\,dy$, for all pairs of orbitals of one sector at once. `@` is the matrix product: `(a * weight) @ a.T` has in row $m$ and column $n$ the sum over the grid of $a_m\,w\,a_n$, which is the Simpson integral of $e^{-y}a_ma_n$.

```python
def per_unit_rate(eps, matrix):
    """G[n, m] = |<n| d_a h |m>| / (eps_n - eps_m)^2 = Q / A (0 for n = m)."""
    gap = eps[:, None] - eps[None, :]
    safe = np.where(gap == 0.0, 1.0, gap)  # 1 on the diagonal: no division by 0
    return np.where(gap == 0.0, 0.0, np.abs(matrix) / safe ** 2)
```

`per_unit_rate` turns the levels and the coupling matrix into the table $G_{nm} = |\langle n|\partial_a h|m\rangle|/(\varepsilon_n - \varepsilon_m)^2$, which is $Q/A$ by Section 22.7. `gap` is the table of all differences of levels; on the diagonal it is zero, so `safe` puts 1 there before dividing, and the result is set to 0 there.

**In [5], the Fermi shells of the record, solved again.**

```python
LEVELS = "Revision/kohn_sham/results/ground/levels"
SHELL = {136: 4, 688: 11}  # the Fermi shell n2 of each N
fermi = [(n, a4) for n in (136, 688) for a4 in SLICES]  # the ten free states
q_fermi = np.array([0.25 * math.sqrt(SHELL[n]) * math.exp(-a4) for n, a4 in fermi])
eps_fermi = levels(np.tile([0, 1, 2], 10), np.repeat(q_fermi, 3)).reshape(10, 3)
```

In the record the largest $Q$ of every free state is the jump from the band level to the first bulk level of its Fermi shell: $n_2 = 4$, $k = 0.25\sqrt4 = 0.5$, for $N = 136$, and $n_2 = 11$, $k = 0.25\sqrt{11} = 0.829$, for $N = 688$. `fermi` lists the ten free states (two particle numbers, five slices) and `q_fermi` their redshifted momenta $q = ke^{-a_{4,0}}$. `np.tile([0, 1, 2], 10)` repeats the labels ten times and `np.repeat(q_fermi, 3)` repeats each momentum three times, so the two arrays list the 30 pairs (label, $q$); one call of `levels` solves all 30, and `.reshape(10, 3)` arranges them as ten rows of three levels. Every level is solved at the slice 0 with the redshifted momentum, as exact rule 2 allows.

```python
worst_level, compared = 0.0, 0
for (n, a4), row in zip(fermi, eps_fermi):
    path = repository_file(f"{LEVELS}/{state_id(n, a4)}.csv")
    with open(path, newline="", encoding="utf-8") as handle:
        for entry in csv.DictReader(handle):
            sector = (int(entry["n2"]), int(entry["j"]), entry["parity"])
            if sector == (SHELL[n], 1, "even") and int(entry["label"]) <= 2:
                difference = float(entry["eps"]) - row[int(entry["label"])]
                worst_level = max(worst_level, abs(difference))
                compared += 1
```

For each of the ten states the loop opens the record's level table (for example `N688_lam0_a00.csv`, one row per level with the columns `n2`, `j`, `parity`, `label`, `eps`, ...), picks the rows of the Fermi-shell sector with $j = +1$ and even parity and a label of at most 2, and compares the recorded level with the one just computed; `worst_level` keeps the largest difference and `compared` counts the comparisons.

```python
a_f, b_f = orbitals(eps_fermi[:, :2].ravel(), np.repeat(q_fermi, 2))
worst_q, same_pair, q_free = 0.0, True, {}
say("   N  a4,0        q      eps_0      eps_1   Q (here)   Q_max (record)")
```

`eps_fermi[:, :2]` takes the labels 0 and 1 of every row and `.ravel()` lines them up into one array of 20 levels; `orbitals` returns their 20 orbitals, two consecutive rows per state. The last line prints the header of the table of Out [5].

```python
for i, (n, a4) in enumerate(fermi):
    matrix = couplings(q_fermi[i], a_f[2 * i:2 * i + 2], b_f[2 * i:2 * i + 2])
    gap = eps_fermi[i, 1] - eps_fermi[i, 0]
    q_free[(n, a4)] = abs(matrix[0, 1]) / gap ** 2  # Q at the rate A = 1
    row = record[state_id(n, a4)]
    for value, column in ((q_free[(n, a4)], "Q_max"), (gap, "Q_max_delta_eps"),
                          (abs(matrix[0, 1]), "Q_max_matrix_element")):
        worst_q = max(worst_q, abs(value / float(row[column]) - 1.0))
```

`enumerate` numbers the states $i = 0, \ldots, 9$. For each one, `couplings` gives the $2 \times 2$ matrix of the band orbital and the first bulk orbital (rows $2i$ and $2i + 1$), `gap` is $\varepsilon_1 - \varepsilon_0$, and $Q = |\langle 0|\partial_a h|1\rangle|/(\varepsilon_1 - \varepsilon_0)^2$ at the rate $A = 1$ (with $H = 1$). The inner loop compares three numbers with the record's three columns, $Q$, the energy difference and the matrix element, as relative differences, and keeps the largest.

```python
    pair = f"{SHELL[n]}:+1:even:0 -> {SHELL[n]}:+1:even:1"
    same_pair = same_pair and row["Q_max_pair"] == pair
    recorded = float(row["Q_max"])
    say(f"{n:4d}  {a4:4.1f}  {q_fermi[i]:7.4f}  {eps_fermi[i, 0]:9.6f}"
        f"  {eps_fermi[i, 1]:9.6f}  {q_free[(n, a4)]:.7f}  {recorded:.7f}")
```

The record names the pair of levels of its largest $Q$ in the column `Q_max_pair`, written as shell, block type, parity and label of both levels; `same_pair` stays true only if every state names the band level and the first bulk level of its Fermi shell. The last statement prints one row of the table: the formats `4d`, `4.1f`, `7.4f`, `9.6f` and `.7f` give whole numbers of width 4 and numbers with 1, 4, 6 and 7 digits after the point.

```python
report("levels compared with the record", compared)
report("largest |eps(here) - eps(record)|", f"{worst_level:.1e}")
report("largest relative difference of Q, delta eps, matrix element", f"{worst_q:.1e}")
check(compared == 30 and worst_level < 1e-12,
      "the 30 levels of the Fermi-shell sectors equal the record's within 1e-12",
      record=f"{LEVELS}/N136_lam0_a*.csv and N688_lam0_a*.csv, column eps")
check(worst_q < 1e-9,
      "Q_max, its energy difference and matrix element reproduced within 1e-9",
      record=f"{ADIABATIC}, columns Q_max, Q_max_delta_eps, Q_max_matrix_element; "
             "computed at the slice 0 with q = k e^(-a4,0), the rescaling identity "
             "of Revision/kohn_sham/reports/ks-rust-solver.json, check "
             "free_rescaling_relation_and_band_monotone")
check(same_pair,
      "the recorded pair is band level -> first bulk level of the Fermi shell",
      record=f"{ADIABATIC}, column Q_max_pair")
```

Out [5] shows the table and the results: 30 levels compared, the largest difference $8.8 \times 10^{-14}$, and the largest relative difference of $Q$, of the energy difference and of the matrix element $1.3 \times 10^{-13}$. For example, for $N = 688$ at the slice 0 the band level is $\varepsilon_0 = 1.247113$, the first bulk level $\varepsilon_1 = 3.500518$, and $Q = 0.0934506$ both here and in the record. The three checks require the 30 levels within $10^{-12}$, the three columns within $10^{-9}$ (relative), and the recorded pair. Because every level was computed at the slice 0 with the momentum $ke^{-a_{4,0}}$, the agreement at all five slices is at the same time a test of the rescaling identity, which the second check names.

**In [6], one curve for every slice and every shell.**

```python
Q_GRID = np.geomspace(0.02, 6.0, 61)  # redshifted momenta q (units of m)
CURVE = np.arange(-3, 5)  # the labels -3 ... 4 of the sector
BAND = 3  # the position of label 0 in CURVE
q_rows = np.repeat(Q_GRID, len(CURVE))  # one row per (q, label)
curve_eps = levels(np.tile(CURVE, len(Q_GRID)), q_rows)
curve_a, curve_b = orbitals(curve_eps, q_rows)
curve_eps = curve_eps.reshape(len(Q_GRID), len(CURVE))
```

By exact rule 2 the free $Q/A$ of a sector is one function $G(q)$. The cell computes it at 61 momenta from $0.02$ to $6$, equally spaced on a logarithmic scale. `CURVE` holds the eight labels $-3, -2, \ldots, 4$, and label 0 sits at position 3 of this array (`BAND`). The $61 \times 8 = 488$ levels and orbitals are computed in one call each and the levels are arranged as 61 rows of 8.

```python
G = np.array([per_unit_rate(curve_eps[i], couplings(
    Q_GRID[i], curve_a[8 * i:8 * i + 8], curve_b[8 * i:8 * i + 8]))
    for i in range(len(Q_GRID))])  # G[i, n, m]: Q per unit rate at Q_GRID[i]
del curve_a, curve_b  # the orbitals are no longer needed
```

For each momentum the eight orbitals give an $8 \times 8$ coupling matrix and from it the table $G_{nm}$; `G` stacks the 61 tables into one array with three indices: the momentum, $n$ and $m$. `del` deletes the orbitals (488 rows of 1801 numbers each) to free memory.

```python
g01 = G[:, BAND, BAND + 1]  # band level -> first bulk level
top = int(np.argmax(g01))
fine_q = np.linspace(Q_GRID[top - 1], Q_GRID[top + 1], 41)  # around the top
fine_eps = levels(np.tile([0, 1], 41), np.repeat(fine_q, 2)).reshape(41, 2)
fine_a, fine_b = orbitals(fine_eps.ravel(), np.repeat(fine_q, 2))
fine_g = np.array([per_unit_rate(fine_eps[i], couplings(
    fine_q[i], fine_a[2 * i:2 * i + 2], fine_b[2 * i:2 * i + 2]))[0, 1]
    for i in range(41)])
g_star, q_star = float(fine_g.max()), float(fine_q[int(np.argmax(fine_g))])
```

`g01` is the curve of the band jump, $G_{01}(q)$. `np.argmax` gives the position of its largest value on the coarse grid. Around it, between the two neighbouring grid points, `np.linspace` makes 41 equally spaced momenta, and the labels 0 and 1 are solved again there; `fine_g` is $G_{01}$ on this fine grid, and its largest value $G^*$ and the momentum $q^*$ where it is reached are kept.

```python
report("largest Q per unit rate of the band jump, G*", f"{g_star:.5f}")
report("at the redshifted momentum q*", f"{q_star:.3f}")
report("naive breakdown rate of the band level, 0.02 <= q <= 6, 1/G*",
       f"{1.0 / g_star:.3f}")
report("largest G of the jumps band -> bulk 2, 3, 4 on the grid",
       ", ".join(f"{G[:, BAND, BAND + m].max():.5f}" for m in (2, 3, 4)))
```

Out [6]: $G^* = 0.09979$ at $q^* = 2.128$, and $1/G^* = 10.021$. The last line prints, for the jumps from the band level to the second, third and fourth bulk levels, the largest value on the 61 momenta of the grid: `G[:, BAND, BAND + m]` is the column of the jump to label $m$, `.max()` its largest entry, and `", ".join(...)` writes the three numbers separated by commas; Out [6] shows $0.00640$, $0.00249$ and $0.00087$. What this establishes, and only this: every shell at every slice whose redshifted momentum lies between $0.02$ and $6$ sits somewhere on the one curve, and that includes every state of the record (their $q$ lie between $0.5e^{-2} = 0.068$ and $0.829$). For all of them the jump from the band level to the first bulk level never has $Q/A$ above $G^*$, the jumps to the second, third and fourth bulk levels stay below $0.0065$, $0.0025$ and $0.0009$, and so the naive breakdown rate of the band level is at least $1/G^* = 10.021$ (COMPUTED here, free field, for the labels up to 4). Beyond $q = 6$ the curve was not computed, and nothing is claimed there.

**In [7], drawing the one curve (Figure 22a.2).**

```python
fig, ax = plt.subplots(figsize=(7.5, 4.5))
ax.plot(Q_GRID, g01, color="black", lw=2.0, label="$G_{01}$: band -> 1st bulk")
ax.plot(Q_GRID, G[:, BAND, BAND + 2], color="0.45", lw=1.5, ls="--",
        label="$G_{02}$: band -> 2nd bulk")
q_low, q_high = float(q_fermi.min()), float(q_fermi.max())
ax.axvspan(q_low, q_high, color="0.85", alpha=0.6, lw=0)  # the recorded range
```

One panel, $7.5$ by $4.5$ inches. The black line is $G_{01}$, the grey dashed line $G_{02}$ (band level to second bulk level). `axvspan` shades the range of momenta that the record's Fermi shells cover, from the smallest to the largest of the ten values of `q_fermi`.

```python
for colour, marker, n in ((PALETTE[0], "o", 136), (PALETTE[1], "s", 688)):
    for tag in TAGS:
        xs = [0.25 * math.sqrt(SHELL[n]) * math.exp(-a4) for a4 in SLICES]
        ys = [q_max[(n, tag, a4)] for a4 in SLICES]
        ax.plot(xs, ys, marker, color=colour, ms=8, mfc="none", mew=1.5,
                label=f"record, $N = {n}$" if tag == "lam0" else None)
ax.plot([q_star], [g_star], "*", color=PALETTE[3], ms=16, mec="black",
        label=f"top: $G^* = {g_star:.4f}$ at $q = {q_star:.2f}$")
```

For both particle numbers and all five couplings the record's $Q_{max}$ (at $A = 1$, so equal to $Q/A$) is drawn as open markers (`mfc="none"`: no fill; `mew`: the width of the marker's edge) at the redshifted momentum of its Fermi shell; only the free states get a legend entry (the expression `... if tag == "lam0" else None` gives the label or nothing). A yellow star with a black edge marks the top of the curve.

```python
ax.set_xscale("log")
ax.set_xlabel("redshifted momentum $q = k\\,e^{-a_{4,0}}$ (units of $m$)")
ax.set_ylabel("$G = Q/A$ (pure number)")
ax.set_title("Every slice and every shell on one curve ($\\lambda = 0$)")
ax.legend(fontsize=8, loc="upper left")
save_figure(fig, "one_curve",
            "The adiabaticity measure per unit rate, $G = Q/A$ (vertical axis, pure "
            "number), of the jump from the band level to the first (black) and "
            "second (grey, dashed) bulk level of a free sector, against the "
            "redshifted momentum $q = k e^{-a_{4,0}}$ (horizontal axis, "
            "logarithmic, units of $m$). Open symbols: the recorded $Q_{max}$ of "
            "the 50 states with $N = 136$ (circles) and $N = 688$ (squares), each "
            "at the $q$ of its Fermi shell; the five couplings overlap. The grey "
            "band is the range of the record; the star is the top of the curve, "
            "the largest $Q/A$ of the jump to the first bulk level for every "
            "shell and slice with $0.02 \\le q \\le 6$ (all states of the record).")
```

A logarithmic horizontal axis, the labels, the title, the legend in the upper left corner, and `save_figure` saves Figure 22a.2. In the caption, `\\le` gives matplotlib's and the book's sign $\le$ (less than or equal); the doubled backslash is needed in a normal Python string, as explained for In [3].

```python
spread = max(abs(q_max[(n, tag, a4)] / q_max[(n, "lam0", a4)] - 1.0)
             for n in (136, 688) for tag in TAGS for a4 in SLICES)
report("largest relative change of Q_max by the interaction", f"{spread:.4f}")
check(largest < g_star < 0.1,
      "the top of the curve lies above every recorded Q_max and below 0.1")
check(spread < 0.15, "the interaction changes Q_max by less than 15 percent",
      record=f"{ADIABATIC}, column Q_max, all couplings")
```

`spread` is the largest relative difference between the $Q_{max}$ of an interacting state and that of the free state with the same particle number and slice: $0.0980$, that is, $9.8$ percent (Out [7]). The first check requires $Q_{max} < G^* < 0.1$ for all recorded states (Python allows the chain `a < b < c`); the second that the interaction changes $Q_{max}$ by less than 15 percent.

*What the student should see in Figure 22a.2, and why.* The black curve rises from about $0.011$ at $q = 0.02$ to its top $0.0998$ at $q = 2.13$ and falls slowly beyond. All ten free states of the record lie exactly on it, at five different slices and two different shells: this is exact rule 2 at work, the deflating history moves each shell along the one curve towards smaller $q$. The interacting states lie close to the curve; the largest scatter is at the smallest $q$ (the shell of $N = 136$ at the slice 2), where the interaction changes $Q$ by up to ten percent. The whole recorded range (grey) lies left of the top, which is why $Q$ falls along the history in Figure 22a.1. The dashed curve of the second bulk level stays below $0.007$ and touches zero near $q = 1.1$, where its matrix element passes through zero: the band level couples mainly to its nearest neighbour.

**In [8], jumps across the gap into the negative branch (Figure 22a.3).**

```python
def g_pair(n, m):
    """G of the jump from label n to label m along Q_GRID."""
    return G[:, BAND + n, BAND + m]


sea = np.max([g_pair(n, m) for n in (-3, -2, -1) for m in (1, 2, 3, 4)], axis=0)
sea_top = int(np.argmax(sea))
```

The record's $Q$ counts only jumps between levels of positive energy, because its filling convention treats the negative branch as the normal-ordered sea, which holds no particles. But the moving background couples the two branches through the same matrix elements, and the table `G` already contains them. `g_pair(n, m)` returns the curve of the jump from label $n$ to label $m$ (the label is shifted by `BAND` to its position in the array). `sea` is, at each momentum, the largest of the twelve jumps from a negative level ($-3$, $-2$, $-1$) to a bulk level ($1$ to $4$), and `sea_top` the position of its maximum.

```python
fig, ax = plt.subplots(figsize=(7.5, 4.5))
ax.plot(Q_GRID, g01, color="black", lw=2.0, label="band 0 -> bulk 1 (record's Q)")
for colour, style, (n, m) in zip(PALETTE, ("-", "--", "-.", ":"),
                                 ((-1, 1), (-1, 2), (-2, 1), (-1, 0))):
    kind = "band" if m == 0 else "bulk"
    ax.plot(Q_GRID, g_pair(n, m), color=colour, lw=2.0, ls=style,
            label=f"negative {n} -> {kind} {m}")
```

The black band jump of In [7] for comparison, and four jumps across the gap, each with its own colour and line style (solid, dashed, dash-dotted, dotted): from $-1$ to the bulk levels 1 and 2, from $-2$ to bulk 1, and from $-1$ to the band level 0.

```python
ax.set_xscale("log")
ax.set_xlabel("redshifted momentum $q = k\\,e^{-a_{4,0}}$ (units of $m$)")
ax.set_ylabel("$G = Q/A$ (pure number)")
ax.set_title("Jumps across the gap between the two branches ($\\lambda = 0$)")
ax.legend(fontsize=8)
save_figure(fig, "across_the_gap",
            "The adiabaticity measure per unit rate $G = Q/A$ (vertical axis) of "
            "jumps from the negative levels $-1$ and $-2$ of a free sector to the "
            "bulk levels 1 and 2 and to the band level 0 (coloured), compared "
            "with the band jump of the record (black), against the redshifted "
            "momentum $q$ (horizontal axis, logarithmic, units of $m$). The jumps "
            "across the gap stay below 0.05 per unit rate; the strongest of them "
            "($-1 \\to$ bulk 1) peaks near $q = 0.11$ at 0.049 and exceeds the "
            "band jump only below $q$ of about 0.1; their reading as pair "
            "creation of the field is OPEN.")
report("largest G of a jump negative level -> bulk level", f"{sea[sea_top]:.5f}")
report("at the redshifted momentum", f"{Q_GRID[sea_top]:.4f}")
check(sea[sea_top] < 0.5 * g_star,
      "every jump across the gap is weaker than half the top of the band jump")
```

The axes, the title, the legend and Figure 22a.3; in its caption `\\to` gives the arrow $\to$. Out [8] gives the strongest jump from a negative to a bulk level, $G = 0.04887$ at $q = 0.1107$, and the check requires it to be below half of $G^*$.

*What the student should see in Figure 22a.3, and why.* The strongest jump across the gap, from $-1$ to bulk 1 (blue), rises to its peak $0.0489$ near $q = 0.11$ and falls on both sides; below about $q = 0.1$ it is stronger than the band jump of the record, above it is weaker, and at large $q$ it is far weaker. The other jumps across the gap stay below $0.025$; the jumps from $-1$ to the band level and from $-2$ to bulk 1 pass through zero near $q = 0.15$. So in the free field the moving background does couple the negative branch to the positive one, at a strength comparable to the band jump at small momenta. In ordinary Dirac theory a jump from a filled negative level to an empty positive one is the creation of a particle-antiparticle pair OF THE FIELD, inside one universe. Whether that reading holds in the 4+4 quantisation with its Krein metric is OPEN, and it has nothing to do with the creation of universes.

**In [9], the Fermi-shell sector along the recorded span.**

```python
K11 = 0.25 * math.sqrt(11.0)  # the Fermi-shell momentum of N = 688 (units of m)
END = 2.0  # the recorded span of slices, a4,0 = 0 ... 2
NODES = 56  # Chebyshev nodes on the span
BASIS = np.arange(-9, 11)  # 20 labels: nine negative, the band level, ten bulk
SIZE, ZERO = len(BASIS), 9  # ZERO: the position of label 0 (the band level)
```

For the time evolution the levels and the matrix $K_{mn}$ are needed at every instant, not only at five slices. The cell takes the Fermi-shell sector of $N = 688$ ($n_2 = 11$, $k = 0.829$, $j = +1$, even parity; its band level holds 96 quanta, the degeneracy $4 \cdot 24$ of the shell in the record's level table), the span $a_{4,0} = 0$ to $2$, 56 interpolation nodes, and a basis of 20 labels, $-9$ to $10$; label 0 is at position 9.

```python
angles = np.pi * (np.arange(NODES) + 0.5) / NODES  # theta_j of the nodes
nodes_s = 0.5 * END * (1.0 + np.cos(angles))  # the nodes as slices a4,0
q_nodes = np.repeat(K11 * np.exp(-nodes_s), SIZE)  # one row per (node, label)
node_eps = levels(np.tile(BASIS, NODES), q_nodes)
node_a, node_b = orbitals(node_eps, q_nodes)
node_eps = node_eps.reshape(NODES, SIZE)
```

The **Chebyshev nodes** are the slices $s_j = 1 + \cos\theta_j$ with $\theta_j = \pi(j + \tfrac12)/56$, $j = 0, \ldots, 55$ (`0.5 * END` is 1). They crowd towards the two ends of the span, which is what makes polynomial interpolation through them accurate. At each node the 20 levels and orbitals are solved: $56 \cdot 20 = 1120$ levels in one call, each at the slice 0 with the momentum $ke^{-s_j}$.

```python
node_m = np.array([couplings(K11 * math.exp(-s), node_a[SIZE * i:SIZE * (i + 1)],
                             node_b[SIZE * i:SIZE * (i + 1)])
                   for i, s in enumerate(nodes_s)])
del node_a, node_b  # the orbitals are no longer needed
```

At each node the $20 \times 20$ matrix $\langle m|\partial_a h|n\rangle$ of the 20 orbitals of that node; `node_m` stacks the 56 matrices. The orbitals are then deleted.

```python
def chebyshev_coefficients(values):
    """c_k = (2/NODES) sum_j values_j cos(k theta_j), c_0 halved: the polynomial
    through the values at the nodes (one column per function)."""
    table = np.cos(np.outer(np.arange(NODES), angles))  # cos(k theta_j)
    coefficients = 2.0 / NODES * table @ values.reshape(NODES, -1)
    coefficients[0] *= 0.5
    return coefficients
```

A function $f$ on the span is approximated by the polynomial $\sum_{k=0}^{55}c_kT_k(x)$, where $x = s - 1$ runs from $-1$ to $1$ and $T_k$ is the Chebyshev polynomial of degree $k$, defined by $T_k(\cos\theta) = \cos(k\theta)$. The coefficients that make the polynomial pass exactly through the values at the 56 nodes are $c_k = \tfrac{2}{56}\sum_jf(s_j)\cos(k\theta_j)$, with $c_0$ halved. `np.outer` makes the table of all products $k\theta_j$, and the matrix product with the values computes all sums at once; `values.reshape(NODES, -1)` arranges any array of values as 56 rows (one per node) and as many columns as there are functions (`-1` lets numpy count them).

```python
FIT_EPS = chebyshev_coefficients(node_eps)  # 20 levels
FIT_M = chebyshev_coefficients(node_m)  # 400 matrix elements


def interpolated(s):
    """Levels (one row per point s) and coupling matrices from the fits."""
    x = 2.0 * np.asarray(s, dtype=float) / END - 1.0  # a4,0 = 0 ... 2 -> -1 ... 1
    eps = chebyshev.chebval(x, FIT_EPS).T
    matrix = chebyshev.chebval(x, FIT_M).T.reshape(len(x), SIZE, SIZE)
    return eps, matrix
```

Coefficients for the 20 levels and for the $20 \cdot 20 = 400$ matrix elements. `interpolated` maps the slices to $x = 2s/2 - 1$, evaluates all the polynomials there with `chebval`, which returns one row per function and one column per point, transposes, and arranges the matrix elements again as $20 \times 20$ matrices, one per point.

```python
test_s = np.array([0.03, 0.25, 0.77, 1.31, 1.97])  # five points between the nodes
test_q = np.repeat(K11 * np.exp(-test_s), SIZE)
test_eps = levels(np.tile(BASIS, 5), test_q)
test_a, test_b = orbitals(test_eps, test_q)
fit_eps, fit_m = interpolated(test_s)
error_eps = float(np.max(np.abs(fit_eps - test_eps.reshape(5, SIZE))))
error_m = max(float(np.max(np.abs(fit_m[i] - couplings(
    K11 * math.exp(-s), test_a[SIZE * i:SIZE * (i + 1)],
    test_b[SIZE * i:SIZE * (i + 1)])))) for i, s in enumerate(test_s))
```

The test of the interpolation: at five slices that are not nodes, the levels and matrices are solved directly and compared with the interpolated ones; `error_eps` and `error_m` are the largest differences.

```python
slice_eps, slice_m = interpolated(SLICES)
slice_q = [abs(slice_m[i, ZERO, ZERO + 1]) / (slice_eps[i, ZERO + 1]
           - slice_eps[i, ZERO]) ** 2 for i in range(5)]
worst_slice = max(abs(slice_q[i] / q_max[(688, "lam0", a4)] - 1.0)
                  for i, a4 in enumerate(SLICES))
```

A second test: $Q$ of the band jump computed from the interpolated levels and matrices at the five slices of the record, compared with the record's $Q_{max}$ of the free state $N = 688$.

```python
report("largest interpolation error of a level", f"{error_eps:.1e}")
report("largest interpolation error of a matrix element", f"{error_m:.1e}")
report("largest relative difference of the interpolated Q to the record",
       f"{worst_slice:.1e}")
check(error_eps < 1e-9 and error_m < 1e-7,
      "the Chebyshev fits reproduce levels within 1e-9 and couplings within 1e-7")
check(worst_slice < 1e-8, "the interpolated Q at the five slices equals the record's",
      record=f"{ADIABATIC}, column Q_max of N688_lam0_a00 ... a20")
```

Out [9]: the interpolation reproduces the levels to $7.3 \times 10^{-11}$ and the matrix elements to $6.4 \times 10^{-9}$, and the interpolated $Q$ at the five slices agrees with the record to $1.4 \times 10^{-13}$ (relative). The two checks require $10^{-9}$, $10^{-7}$ and $10^{-8}$.

**In [10], the levels of the sector and how fast the band orbital turns (Figure 22a.4).**

```python
s_plot = np.linspace(0.0, END, 201)
eps_plot, m_plot = interpolated(s_plot)
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.4), layout="constrained")
for i, label in enumerate(BASIS):
    if label == 0:
        left.plot(s_plot, eps_plot[:, i], color=PALETTE[3], lw=3.0,
                  label="band level 0 (occupied)")
    else:
        colour = PALETTE[0] if label > 0 else PALETTE[1]
        left.plot(s_plot, eps_plot[:, i], color=colour, lw=1.0)
```

201 slices across the span, the interpolated levels and matrices there, and two panels. On the left every one of the 20 levels is drawn against the slice: the band level thick and yellow, the bulk levels blue and the negative levels orange.

```python
left.plot([], [], color=PALETTE[0], lw=1.0, label="bulk levels 1 ... 10")
left.plot([], [], color=PALETTE[1], lw=1.0, label="negative levels -1 ... -9")
left.set_xlabel("slice $a_{4,0}$")
left.set_ylabel("level $\\varepsilon$ (units of $m$)")
left.set_title("Sector $n_2 = 11$, $j = +1$, even, of $N = 688$")
left.legend(fontsize=8, loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=3)
```

Two empty plots (`[]`, no points) create one legend entry each for the nineteen thin lines; the legend is placed below the panel in three columns (`bbox_to_anchor` gives its position relative to the panel).

```python
for colour, style, label in zip(PALETTE, ("-", "--", "-.", ":"), (1, 2, -1, -2)):
    m = ZERO + label
    turn = np.abs(m_plot[:, m, ZERO]) / np.abs(eps_plot[:, ZERO] - eps_plot[:, m])
    right.plot(s_plot, turn, color=colour, ls=style, lw=2.0, label=f"$m = {label}$")
right.set_xlabel("slice $a_{4,0}$")
right.set_ylabel("$|K_{m0}|$ (per e-fold)")
right.set_title("How fast the band orbital turns towards level $m$")
right.legend(fontsize=8)
```

On the right, for the levels $m = 1, 2, -1, -2$, the number $|K_{m0}| = |\langle m|\partial_a h|0\rangle|/|\varepsilon_0 - \varepsilon_m|$ of line 6 of Section 22.6. It says how far the band orbital turns towards level $m$ per unit change of $a_4$, that is, per e-fold of the extra times.

```python
save_figure(fig, "sector_levels",
            "Left: the 20 instantaneous levels (vertical axis, units of $m$) of the "
            "free Fermi-shell sector of $N = 688$ against the slice $a_{4,0}$ "
            "(horizontal axis): the occupied band level (thick) falls as the 3-"
            "momentum redshifts, the bulk levels above it and the negative levels "
            "below it move towards their values at $k = 0$. Right: $|K_{m0}|$, how "
            "far the band orbital turns towards level $m$ per e-fold (vertical "
            "axis), for $m = 1, 2, -1, -2$; all are below 0.25, so the band orbital "
            "changes slowly.")
```

`save_figure` saves Figure 22a.4. This cell prints nothing else.

*What the student should see in Figure 22a.4, and why.* On the left the band level falls from $1.247$ at the slice 0 to $0.206$ at the slice 2 (the values of Out [5]): as $q$ redshifts towards 0 it approaches the zero mode, the level $\varepsilon = 0$ of the brane-bound orbital at $k = 0$. The bulk levels fall and the negative levels rise, all towards their values at $k = 0$; the gap between the band level and the first bulk level stays above 1.6 (at the slice 2 it is $1.823448 - 0.205760 = 1.617688$, Out [5]). On the right $|K_{10}|$ falls from $0.21$ to about $0.09$ along the span; the turning towards the negative level $-1$ starts at about $0.08$ and passes through zero near the slice $1.8$; the others stay below about $0.035$. All are well below 1: the band orbital changes slowly per e-fold, which is why the instantaneous picture works as well as it does.

**In [11], the exact time evolution in the basis of instantaneous levels.**

```python
U_STEPS = 4000  # the finest number of RK4 steps of one passage, u = 0 ... 1
U = np.linspace(0.0, 1.0, 2 * U_STEPS + 1)  # the fine grid: step ends, midpoints
CHOICES = [200, 400, 500, 1000, 2000, 4000]  # step numbers that divide U_STEPS
OFF = ~np.eye(SIZE, dtype=bool)  # every pair n != m
SPAN = float(np.ptp(node_eps))  # the largest energy difference of the basis
```

The passage is integrated in the variable $u = x_4/T$ of Section 22.8, from 0 to 1, with RK4. The finest integration uses 4000 steps; `U` is its fine grid of 8001 points (step ends and midpoints), on which the levels and matrices are tabulated once. A coarser integration may use 200, 400, 500, 1000 or 2000 steps; these numbers divide 4000, so their step ends and midpoints are points of the same fine grid. `np.eye(SIZE, dtype=bool)` is the $20 \times 20$ table that is true on the diagonal, and `~` turns true into false and back, so `OFF` selects the pairs $m \ne n$. `np.ptp` ("peak to peak") is the largest value minus the smallest: `SPAN` is the largest difference between any two levels of the basis at any node, $24.89$ (Out [11]).

```python
def frame(s):
    """Levels e[i, n] and the matrix k[i, m, n] = <m| d_a n> at the slices s[i]."""
    e, matrix = interpolated(s)
    gap = e[:, None, :] - e[:, :, None]  # gap[i, m, n] = eps_n - eps_m
    k = np.zeros_like(matrix)
    k[:, OFF] = matrix[:, OFF] / gap[:, OFF]  # line 6 of section 4; K_nn = 0
    return e, k
```

`frame` gives, at a list of slices, the levels and the matrices $K_{mn} = \langle m|\partial_a h|n\rangle/(\varepsilon_n - \varepsilon_m)$ (line 6 of Section 22.6; the comment refers to section 4 of the notebook, which derives it), with $K_{nn} = 0$ (line 7). The array `gap` holds $\varepsilon_n - \varepsilon_m$ in position $[i, m, n]$, which the two `None` arrange by broadcasting; only the off-diagonal entries are divided.

```python
def steps_needed(duration):
    """The smallest step number of CHOICES with duration * SPAN / steps <= 0.2."""
    for steps in CHOICES:
        if duration * SPAN / steps <= 0.2:
            return steps
    return CHOICES[-1]
```

In the variable $u$ the amplitudes turn with the frequencies $T\varepsilon_m$, so in one step of length $1/N$ a phase changes by up to about $T \cdot \mathrm{SPAN}/N$. `steps_needed` returns the smallest step number of `CHOICES` that keeps this below $0.2$ radian, and the finest one when none does.

```python
def passage(duration, e, k, rate, start, steps, keep=0):
    """RK4 for dc/du = -i duration e(u) c - rate(u) k(u) c from u = 0 to 1.
    e, k and rate are given on the fine grid U. Returns the final amplitudes and,
    if keep > 0, the list of the amplitudes after every keep steps."""
    stride = U_STEPS // steps  # fine-grid points per half step
    h = 1.0 / steps
    c = start.astype(complex)
    kept = [c]
```

`passage` integrates the equation $dc/du = -iT\varepsilon(u)c - (da_4/du)K(u)c$ of Section 22.8 for the vector $c$ of the 20 amplitudes. The arguments are the duration $T$, the levels `e` and matrices `k` on the fine grid, the rate $da_4/du$ on the fine grid, the starting amplitudes, the number of steps, and how often to keep the amplitudes. A step of length $h = 1/N$ spans $2 \cdot 4000/N$ intervals of the fine grid, so half a step spans `stride` $= 4000/N$ of them (`//` is division of whole numbers). `astype(complex)` makes the amplitudes complex numbers.

```python
    def slope(i, c):
        return -1j * duration * e[i] * c - rate[i] * (k[i] @ c)

    for step in range(steps):
        i = 2 * stride * step  # the start of this step on the fine grid
        s1 = slope(i, c)
        s2 = slope(i + stride, c + 0.5 * h * s1)
        s3 = slope(i + stride, c + 0.5 * h * s2)
        s4 = slope(i + 2 * stride, c + h * s3)
        c = c + h / 6.0 * (s1 + 2.0 * s2 + 2.0 * s3 + s4)
        if keep and (step + 1) % keep == 0:
            kept.append(c)
    return c, kept
```

`slope(i, c)` is the right side of the equation at the fine-grid point $i$; `1j` is Python's $i$, and `e[i] * c` multiplies each amplitude by its own level. Each step is the RK4 rule of In [4], with the slopes at the start (fine point $i$), twice at the middle ($i + $ `stride`) and at the end ($i + 2\,$`stride`). After every `keep` steps the amplitudes are stored (`%` is the remainder of a division). The function returns the final amplitudes and the stored ones.

```python
S_SMOOTH = END * (U - np.sin(2.0 * np.pi * U) / (2.0 * np.pi))  # a4 along it
RATE_SMOOTH = 2.0 * END * np.sin(np.pi * U) ** 2  # its derivative d a4 / d u
E_SMOOTH, K_SMOOTH = frame(S_SMOOTH)
S_LINEAR = END * U  # the constant rate: a4 = END u
RATE_LINEAR = np.full_like(U, END)
E_LINEAR, K_LINEAR = frame(S_LINEAR)
```

The two histories of Section 22.8 on the fine grid: the smooth passage $a_4 = 2[u - \sin(2\pi u)/(2\pi)]$ with $da_4/du = 4\sin^2(\pi u)$, and the constant rate $a_4 = 2u$ with $da_4/du = 2$; for each, `frame` tabulates the levels and the matrices $K$ at all 8001 points.

```python
START = np.zeros(SIZE, dtype=complex)
START[ZERO] = 1.0  # the particle starts in the band level
report("largest energy difference of the basis", f"{SPAN:.4f}", "m")
```

The starting amplitudes: 1 for the band level, 0 for the 19 others. The report prints `SPAN` with its unit $m$.

**In [12], a smooth passage at every rate.**

```python
RATES = 10.0 ** np.linspace(-0.6, 2.4, 31)  # peak rates A from 0.25 to 251
excited, norm_error = [], 0.0
for rate in RATES:
    duration = 2.0 * END / rate  # T = 4/A: the peak rate is A
    c, _ = passage(duration, E_SMOOTH, K_SMOOTH, RATE_SMOOTH, START,
                   steps_needed(duration))
    excited.append(1.0 - abs(c[ZERO]) ** 2)  # probability to have left level 0
    norm_error = max(norm_error, abs(float(np.vdot(c, c).real) - 1.0))
excited = np.array(excited)
```

31 peak rates $A = 10^{-0.6}, \ldots, 10^{2.4}$, that is from $0.251$ to $251$, ten per factor 10; the seventh is 1 (up to rounding in the last digit: the computer stores $1.0000000000000002$) and the eleventh $10^{0.4} = 2.51$. For each the passage lasts $T = 4/A$ (Section 22.8), and the probability that the particle has left the band level at the end is $P = 1 - |c_0|^2$. It counts every other level of the basis, the negative ones included. `np.vdot(c, c)` is $\sum_n|c_n|^2$, the total probability, and `norm_error` keeps its largest distance from 1. The underscore `_` receives the stored amplitudes, which are not needed here.

```python
c, _ = passage(0.0, E_SMOOTH, K_SMOOTH, RATE_SMOOTH, START, 400)  # infinitely fast
sudden_basis = 1.0 - abs(c[ZERO]) ** 2
q_ends = np.array([K11, K11 * math.exp(-END)])  # the band level at a4,0 = 0 and 2
ends_a, ends_b = orbitals(levels([0, 0], q_ends), q_ends)
overlap = float(np.sum(SIMPSON * (ends_a[0] * ends_a[1] + ends_b[0] * ends_b[1])))
sudden = 1.0 - overlap ** 2  # the sudden limit from the two orbitals directly
```

The sudden limit, twice. First in the basis: with the duration $T = 0$ the term $-iT\varepsilon c$ vanishes and only the transport by $K$ remains, which is the infinitely fast passage of Section 22.8. Second directly: the band orbitals at the slices 0 and 2 (momenta $k$ and $ke^{-2}$), their overlap $\int(a_0a_2 + b_0b_2)\,dy$ by Simpson's rule, and $P_{sudden} = 1 - \mathrm{overlap}^2$.

```python
du = 1.0 / (2 * U_STEPS)  # the spacing of the fine grid U
gaps = E_SMOOTH - E_SMOOTH[:, [ZERO]]  # eps_m - eps_0 along the passage
phase = np.vstack([np.zeros((1, SIZE)), np.cumsum(0.5 * (gaps[1:] + gaps[:-1]) * du,
                                                  axis=0)])  # trapezoid rule
weights = np.full(len(U), 2.0 * du / 3.0)  # Simpson weights on U
weights[1::2] = 4.0 * du / 3.0
weights[0] = weights[-1] = du / 3.0
drive = (weights * RATE_SMOOTH)[:, None] * K_SMOOTH[:, :, ZERO]  # da4/du K_m0
first = np.array([float(np.sum(np.abs(np.sum(drive * np.exp(
    1j * (2.0 * END / rate) * phase), axis=0)) ** 2)) for rate in RATES])
```

The first-order estimate $P^{(1)} = \sum_m|d_m(1)|^2$ of Section 22.8. `gaps` holds $\varepsilon_m - \varepsilon_0$ at every fine point (`[:, [ZERO]]` keeps the column as a column, so the subtraction works row by row). `phase` is $\int_0^u(\varepsilon_m - \varepsilon_0)\,du'$ at every fine point, built by the **trapezoid rule**: each interval adds its length times the mean of the values at its two ends, and `np.cumsum` adds these up one after the other (`np.vstack` puts the starting row of zeros on top). `weights` are Simpson's weights for the 8000 intervals of length `du` of the grid `U` (here written for pairs of intervals: $du/3$, $4du/3$, $2du/3$). `drive` holds $(da_4/du)K_{m0}$ times the weights, one column per level $m$. For each rate the integral $d_m(1)$ is the weighted sum of `drive` times $e^{iT\cdot\mathrm{phase}}$ with $T = 4/A$; the absolute squares are added over $m$. The column $m = 0$ contributes nothing, because $K_{00} = 0$.

```python
above = int(np.argmax(excited >= 0.5 * sudden))  # first rate past half the limit
x0, x1 = math.log(RATES[above - 1]), math.log(RATES[above])
y0, y1 = excited[above - 1] - 0.5 * sudden, excited[above] - 0.5 * sudden
rate_half = math.exp(x0 - y0 * (x1 - x0) / (y1 - y0))  # straight line in log A
```

`excited >= 0.5 * sudden` is an array of true and false, and `np.argmax` of it is the position of the first true: the first rate at which $P$ has reached half the sudden limit. Between that rate and the one before, the difference $P - P_{sudden}/2$ is replaced by a straight line in $\ln A$, and its zero is $A_{1/2}$: the line through $(x_0, y_0)$ and $(x_1, y_1)$ crosses zero at $x = x_0 - y_0(x_1 - x_0)/(y_1 - y_0)$, and $A_{1/2} = e^x$.

```python
report("largest |total probability - 1|", f"{norm_error:.1e}")
report("sudden limit: overlap / basis", f"{sudden:.6f} / {sudden_basis:.6f}")
report("P at A = 0.25, 1, 2.51, 251",
       ", ".join(f"{excited[i]:.3e}" for i in (0, 6, 10, 30)))
report("rate at which P reaches half the sudden limit, A_1/2", f"{rate_half:.3f}")
check(norm_error < 1e-9, "the evolution keeps the total probability 1 within 1e-9")
check(abs(sudden_basis / sudden - 1.0) < 1e-3,
      "the sudden limit of the 20-level basis equals the direct overlap within 0.1%")
check(abs(excited[-1] / sudden - 1.0) < 1e-3 and excited[0] < 1e-6
      and bool(np.all(excited <= sudden * (1.0 + 1e-3))),
      "P rises from below 1e-6 at A = 0.25 to the sudden limit at A = 251, never above")
```

Out [12]: the total probability stays 1 to $1.2 \times 10^{-11}$; the sudden limit is $0.074906$ from the overlap and $0.074902$ in the basis; $P$ is $1.04 \times 10^{-7}$ at $A = 0.25$, $0.0138$ at $A = 1$, $0.0590$ at $A = 2.51$ and $0.0749$ at $A = 251$; and $A_{1/2} = 1.508$. (`", ".join(...)` writes the four numbers separated by commas; the format `.3e` writes a number with three digits after the point and a power of ten.) The three checks require the conservation of probability, the agreement of the two sudden limits within $0.1$ percent, and that $P$ rises from below $10^{-6}$ to the sudden limit without ever exceeding it by more than $0.1$ percent. That $P$ never exceeds the sudden limit is a COMPUTED finding for this sector and this passage, not a theorem.

**In [13], drawing the smooth passage (Figure 22a.5).**

```python
fig, ax = plt.subplots(figsize=(7.5, 4.6))
ax.plot(RATES, excited, "o-", color=PALETTE[0], ms=5, lw=2.0,
        label="exact evolution (20 levels)")
ax.plot(RATES, first, "--", color=PALETTE[1], lw=2.0, label="first order")
ax.axhline(sudden, color="0.3", ls=":", lw=1.5, label="sudden limit")
```

The exact $P$ (blue, with markers), the first-order estimate (orange, dashed) and the sudden limit (dotted horizontal line).

```python
for value, style, text, height in ((1.0, "--", "record", 2e-7),
                                   (rate_half, "-", "$A_{1/2}$", 2e-5),
                                   (naive[weakest], "-.", "$1/Q_{max}$", 2e-7)):
    ax.axvline(value, color="0.45", ls=style, lw=1.2)
    ax.text(value * 1.06, height, text, fontsize=9, color="0.3")
```

Three vertical lines with labels: the record's rate $A = 1$ (dashed), $A_{1/2}$ (solid) and the naive breakdown rate $1/Q_{max} = 10.70$ of In [3] (dash-dotted); each label is placed a little to the right of its line, at the given height.

```python
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_ylim(1e-8, 0.3)
ax.set_xlabel("peak rate $A$ (e-folds per unit time $1/H$)")
ax.set_ylabel("$P$: probability to have left the band level")
ax.set_title("Smooth passage $a_{4,0} = 0 \\to 2$, free Fermi shell of $N = 688$")
ax.legend(fontsize=8, loc="lower right")
save_figure(fig, "smooth_passage",
            "The probability $P$ that the particle of the band level has left it "
            "at the end of a smooth passage from $a_{4,0} = 0$ to $2$ (vertical "
            "axis, logarithmic), against the peak rate $A$ (horizontal axis, "
            "logarithmic): exact evolution in the basis of 20 instantaneous levels "
            "(blue), the first-order estimate (orange, dashed) and the sudden limit "
            "(dotted). Vertical lines: the record's rate $A = 1$, the rate "
            "$A_{1/2}$ at which $P$ reaches half the sudden limit, and the naive "
            "breakdown rate $1/Q_{max}$. The gas stops following its level near "
            "$A = 1$, about seven times below the naive estimate ($A_{1/2} = 1.5$ "
            "against $1/Q_{max} = 10.7$), but $P$ never exceeds the sudden limit "
            "of about 7.5 percent.")
```

Both axes logarithmic, the vertical one from $10^{-8}$ to $0.3$; labels, title and legend; Figure 22a.5.

*What the student should see in Figure 22a.5, and why.* At small rates $P$ is tiny ($10^{-7}$ at $A = 0.25$) and rises very steeply, by about five powers of ten up to $A = 1$: a slow passage leaves the particle in its level, and the fast-turning phases of Section 22.8 suppress the transitions the more strongly the slower the passage. Near $A = 1$, where $P = 0.0138$, the rise slows down, and from about $A = 5$ on the curve is nearly flat at the sudden limit $0.0749$: there the passage is so fast that the orbital has no time to adapt at all. The first-order estimate follows the exact curve up to about $A = 1$ (with the same small wiggles, which come from the oscillating phases) and then overshoots the sudden limit, because at large rates the amplitudes are no longer small. The three vertical lines tell the story of the breakdown: the gas stops following its level near $A_{1/2} = 1.51$, about seven times below the naive estimate $10.7$; but however fast the passage, at most about $7.5$ percent of the particles leave the band level over the recorded span.

**In [14], a constant rate: the dressing that Q measures (Figure 22a.6).**

```python
MARKS = np.arange(0, 2 * U_STEPS + 1, 2 * U_STEPS // 100)  # 101 points of U


def dressed(rate):
    """Level 0 with the first-order admixtures i A K_m0 / (eps_m - eps_0)."""
    e, k = E_LINEAR[0], K_LINEAR[0]
    c = START.copy()
    for m in range(SIZE):
        if m != ZERO:
            c[m] = 1j * rate * k[m, ZERO] / (e[m] - e[ZERO])
    return c / np.linalg.norm(c)
```

`MARKS` are 101 points of the fine grid, every 80th, at $u = 0, 0.01, \ldots, 1$. `dressed(rate)` builds the dressed state of Section 22.7 at the start of the constant-rate history: amplitude 1 for the band level and $\alpha_m = iAK_{m0}/(\varepsilon_m - \varepsilon_0)$ for every other level (with $H = 1$), divided by its length `np.linalg.norm(c)` $= \sqrt{\sum|c_n|^2}$ so that the total probability is 1.

```python
def dressing(rate):
    """The first-order estimate sum_m Q_0m^2 at the 101 marks."""
    e, k = E_LINEAR[MARKS], K_LINEAR[MARKS]
    total = np.zeros(len(MARKS))
    for m in range(SIZE):
        if m != ZERO:  # Q_0m = A |K_m0| / |eps_m - eps_0|
            total += (rate * k[:, m, ZERO] / (e[:, m] - e[:, ZERO])) ** 2
    return total
```

`dressing(rate)` is the first-order dressing probability $\sum_{m \ne 0}Q_{0m}^2$ at the 101 marks, with $Q_{0m} = A|K_{m0}|/|\varepsilon_m - \varepsilon_0|$, which equals the formula of Section 22.7 by line 6. The sum runs over all 19 other levels of the basis, the negative ones included; the matrix $K$ is real, so its square needs no absolute value.

```python
runs = {}
for rate in (0.3, 1.0, 3.0):
    duration = END / rate  # T = 2/A for the constant rate A
    steps = steps_needed(duration)
    _, kept = passage(duration, E_LINEAR, K_LINEAR, RATE_LINEAR, dressed(rate),
                      steps, keep=steps // 100)
    runs[rate] = np.array([1.0 - abs(c[ZERO]) ** 2 for c in kept])
steps = steps_needed(END)
_, kept = passage(END, E_LINEAR, K_LINEAR, RATE_LINEAR, START, steps, keep=steps // 100)
bare = np.array([1.0 - abs(c[ZERO]) ** 2 for c in kept])
s_marks = S_LINEAR[MARKS]
```

For the constant rates $A = 0.3$, $1$ and $3$ the history lasts $T = 2/A$; the evolution starts in the dressed state, and the amplitudes are kept after every hundredth of the steps, which gives the same 101 points as `MARKS`. `runs[rate]` holds $P = 1 - |c_0|^2$ at these points. At $A = 1$ ($T = 2$) a second run starts in the bare level 0 instead: that is an abrupt start of the motion. `s_marks` are the values of $a_4$ at the marks.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.2), layout="constrained")
for colour, rate in zip(PALETTE, (0.3, 1.0, 3.0)):
    left.plot(s_marks, runs[rate], color=colour, lw=2.0, label=f"exact, $A = {rate}$")
    left.plot(s_marks, dressing(rate), color=colour, lw=1.5, ls="--")
left.plot([], [], color="0.4", ls="--", label="first order $\\sum_m Q_{0m}^2$")
left.set_yscale("log")
left.set_ylim(3e-5, 0.3)
left.set_xlabel("$a_4$ along the constant-rate history")
left.set_ylabel("$P$: probability outside the band level")
left.set_title("Dressed start: exact against first order")
left.legend(fontsize=8, loc="lower left")
```

The left panel: for each rate the exact $P$ (solid) and the first-order dressing (dashed, same colour) against $a_4$; one empty plot gives the legend entry for the dashed lines; a logarithmic vertical axis from $3 \times 10^{-5}$ to $0.3$.

```python
right.plot(s_marks, runs[1.0], color=PALETTE[1], lw=2.0, label="dressed start")
right.plot(s_marks, bare, color=PALETTE[0], lw=2.0, ls="-.", label="bare start")
right.plot(s_marks, dressing(1.0), color="0.4", lw=1.5, ls="--",
           label="first order $\\sum_m Q_{0m}^2$")
right.set_xlabel("$a_4$ along the constant-rate history")
right.set_ylabel("$P$")
right.set_title("$A = 1$: dressed and bare start")
right.legend(fontsize=8)
```

The right panel, with a linear vertical axis: at $A = 1$ the dressed start, the bare start and the first-order dressing.

```python
save_figure(fig, "constant_rate",
            "Left: the probability $P$ that the particle is not in its "
            "instantaneous band level (vertical axis, logarithmic) along a history "
            "of constant rate $A = 0.3$, $1$, $3$ from $a_4 = 0$ to $2$ "
            "(horizontal axis), exact (solid) and the first-order dressing "
            "$\\sum_m Q_{0m}^2$ (dashed), starting in the dressed state. At $A = "
            "0.3$ they agree; at $A = 1$ the exact $P$ stays near 0.009 while the "
            "estimate falls; at $A = 3$ first order fails. Right: $A = 1$ with the "
            "dressed start and with the bare start (an abrupt start of the motion), "
            "which leaves about three times more.")
deviation = float(np.max(np.abs(runs[0.3] / dressing(0.3) - 1.0)))
report("A = 0.3: largest relative difference exact / first order", f"{deviation:.3f}")
report("A = 1: exact P at a4 = 0 and 2", f"{runs[1.0][0]:.5f}, {runs[1.0][-1]:.5f}")
report("A = 1: first-order dressing at a4 = 0 and 2",
       f"{dressing(1.0)[0]:.5f}, {dressing(1.0)[-1]:.5f}")
report("A = 1, bare start: largest P", f"{bare.max():.5f}")
check(deviation < 0.15, "at A = 0.3 the exact P agrees with the first-order dressing "
      "within 15 percent at all 101 points")
```

Figure 22a.6 and the numbers of Out [14]: at $A = 0.3$ the exact $P$ and the first-order dressing differ by at most $11.3$ percent; at $A = 1$ the exact $P$ is $0.00904$ at the start and $0.00730$ at the end, while the first-order dressing falls from $0.00912$ to $0.00289$; the bare start at $A = 1$ reaches $0.02787$. The check requires agreement within 15 percent at $A = 0.3$.

*What the student should see in Figure 22a.6, and why.* On the left the blue pair ($A = 0.3$) lies almost on top of each other and falls from about $8 \times 10^{-4}$ to $2.6 \times 10^{-4}$: at a small rate the particle carries exactly the dressing that $Q$ measures, and the dressing shrinks along the history because $Q$ falls as the momentum redshifts. At $A = 1$ the exact curve stays near $0.009$ while the dressing falls to $0.003$; the difference is, in the reading suggested by Section 22.7, probability that has really left the band level, not dressing that would disappear if the motion stopped slowly (the notebook does not separate the two by a computation of its own). At $A = 3$ the exact $P$ stays near $0.075$, the size of the sudden limit, and the first-order dressing is no guide. On the right, the abrupt (bare) start at $A = 1$ shakes the particle: $P$ rises from 0 to $0.028$ near $a_4 = 1.6$, about three times the dressing, because starting the motion suddenly is itself a sudden change.

**In [15], how far the sudden limit reaches (Figure 22a.7).**

```python
ENDS = np.linspace(0.0, 6.0, 61)  # end slices of a sudden jump from a4,0 = 0
ends_q = K11 * np.exp(-ENDS)
band_a, band_b = orbitals(levels(np.zeros(61), ends_q), ends_q)
ceiling = 1.0 - (band_a @ (SIMPSON * band_a[0]) + band_b @ (SIMPSON * band_b[0])) ** 2
```

The sudden limit caps the damage, and it depends on how much the band orbital itself changes. The cell computes the band orbital of the Fermi shell at 61 end slices from 0 to 6, three times beyond the record's span (free field, computed here), and the sudden limit $1 - (\int\varphi_0(s)^\dagger\varphi_0(0)\,dy)^2$ of a jump from 0 to each of them. `band_a @ (SIMPSON * band_a[0])` computes in one matrix product the Simpson integrals of $a_0(s)a_0(0)$ for all 61 end slices.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.2), layout="constrained")
for colour, index in zip(PALETTE, (0, 10, 20, 60)):
    left.plot(Y, band_a[index], color=colour, lw=2.0,
              label=f"$a$, $a_{{4,0}} = {ENDS[index]:.0f}$")
    left.plot(Y, band_b[index], color=colour, lw=1.2, ls="--")
left.plot([], [], color="0.4", ls="--", label="$b$ (dashed)")
left.set_xlabel("hidden coordinate $y$ (tip at $-3$, brane at 0)")
left.set_ylabel("band orbital (normalised)")
left.set_title("The band orbital of the Fermi shell")
left.legend(fontsize=8)
```

The left panel draws the two components of the band orbital, $a$ solid and $b$ dashed, against $y$ at the end slices 0, 1, 2 and 6 (the indices 0, 10, 20, 60 of `ENDS`).

```python
right.plot(ENDS, ceiling, color=PALETTE[0], lw=2.0)
right.plot([END], [sudden], "o", color=PALETTE[1], ms=9,
           label="end of the recorded span")
right.set_xlabel("end slice $a_{4,0}$ of a sudden jump from 0")
right.set_ylabel("$P_{sudden}$")
right.set_title("The ceiling of the damage")
right.legend(fontsize=8)
```

The right panel: the sudden limit against the end slice, with an orange dot at the end of the recorded span, the value of In [12].

```python
save_figure(fig, "sudden_ceiling",
            "Left: the band orbital of the Fermi shell of $N = 688$, components "
            "$a$ (solid) and $b$ (dashed), against the hidden coordinate $y$ "
            "(horizontal axis) at the slices $a_{4,0} = 0$, $1$, $2$, $6$: as the "
            "momentum redshifts, $b$ shrinks and the orbital approaches the brane "
            "zero mode $e^{y}$. Right: the sudden limit $P_{sudden}$ (vertical "
            "axis) of a jump from $a_{4,0} = 0$ to the end slice (horizontal "
            "axis); it grows and levels off near 0.105: even an instant jump to "
            "the far future leaves almost 90 percent of the particles in the band "
            "level.")
report("sudden limit for the end slices 2, 4, 6",
       ", ".join(f"{ceiling[i]:.4f}" for i in (20, 40, 60)))
check(np.all(np.diff(ceiling) > -1e-12) and ceiling[-1] < 0.11
      and abs(ceiling[20] - sudden) < 1e-12,
      "the sudden limit grows with the end slice and stays below 0.11 up to 6")
```

Figure 22a.7 and Out [15]: the sudden limit is $0.0749$, $0.1021$ and $0.1051$ for the end slices 2, 4 and 6. The check requires that it never decreases (`np.diff` gives the differences of neighbours), that it stays below $0.11$, and that its value at the slice 2 equals the sudden limit of In [12].

*What the student should see in Figure 22a.7, and why.* On the left the band orbital is concentrated near the brane: $a$ grows towards $y = 0$ and $b$ is small and negative. As the slice grows, $b$ shrinks towards zero and $a$ spreads a little towards the tip, approaching the zero mode $(e^{y}, 0)$, the exact brane-bound orbital of momentum 0 (Chapter 14). The orbitals of the slices 2 and 6 are already close to each other. On the right the sudden limit rises steeply at first and then levels off near $0.105$: the orbital cannot move further than to the zero mode, so even an instantaneous jump to the far future leaves almost 90 percent of the particles in the band level.

**In [16], how many levels are needed (Figure 22a.8).**

```python
sizes, errors = [], {"sudden": [], 1.0: [], 3.0: []}
results = {}
for low in range(1, 10):
    for high in (low, low + 1):
        chosen = np.where((BASIS >= -low) & (BASIS <= high))[0]
        zero = int(np.where(BASIS[chosen] == 0)[0][0])
        e, k = E_SMOOTH[:, chosen], K_SMOOTH[:, chosen][:, :, chosen]
        start = np.zeros(len(chosen), dtype=complex)
        start[zero] = 1.0
        sizes.append(len(chosen))
```

A truncated basis can only be trusted if the results stop changing as it grows. The loop builds smaller bases from the labels $-l, \ldots, l$ and $-l, \ldots, l + 1$ for $l = 1, \ldots, 9$, that is, of $3, 4, 5, \ldots, 20$ levels. `np.where(condition)[0]` gives the positions where the condition holds (`&` is "and" for arrays); `zero` is the position of label 0 within the chosen labels; `e` and `k` keep the columns, and for $K$ also the rows, of the chosen levels; `start` puts the particle into the band level.

```python
        c, _ = passage(0.0, e, k, RATE_SMOOTH, start, 400)
        errors["sudden"].append(abs(1.0 - abs(c[zero]) ** 2 - sudden))
        for rate in (1.0, 3.0):
            duration = 2.0 * END / rate
            c, _ = passage(duration, e, k, RATE_SMOOTH, start, steps_needed(duration))
            results[(len(chosen), rate)] = 1.0 - abs(c[zero]) ** 2
for rate in (1.0, 3.0):
    errors[rate] = [abs(results[(size, rate)] - results[(SIZE, rate)])
                    for size in sizes]
```

For each basis: the sudden limit, compared with the direct overlap of In [12], and the smooth passages at $A = 1$ and $A = 3$. Their errors are measured against the result of the full 20-level basis.

```python
halving = 0.0
for rate in (RATES[0], 1.0, 10.0):
    duration = 2.0 * END / rate
    steps = steps_needed(duration)
    other = 2 * steps if steps < U_STEPS else steps // 2
    p_one, p_two = (1.0 - abs(passage(duration, E_SMOOTH, K_SMOOTH, RATE_SMOOTH, START,
                                      n)[0][ZERO]) ** 2 for n in (steps, other))
    halving = max(halving, abs(p_one - p_two))
```

The second numerical question, the time steps: three passages ($A = 0.25$, $1$, $10$) are repeated with twice the number of steps (or half of it, when the finest number is already in use), and `halving` keeps the largest change of $P$. The parentheses around the expression with `for` make a **generator**, whose two values are assigned to `p_one` and `p_two`.

```python
fig, ax = plt.subplots(figsize=(7.0, 4.2))
ax.plot(sizes, errors["sudden"], "o-", color=PALETTE[0], lw=2.0, ms=6,
        label="sudden limit (against the direct overlap)")
for colour, marker, rate in ((PALETTE[1], "s", 1.0), (PALETTE[2], "^", 3.0)):
    ax.plot(sizes[:-1], errors[rate][:-1], marker + "--", color=colour, lw=1.5, ms=6,
            label=f"$A = {rate:.0f}$ (against 20 levels)")
ax.set_yscale("log")
ax.set_xticks(range(3, 21))
ax.set_xlabel("number of instantaneous levels in the basis")
ax.set_ylabel("$|P - P_{reference}|$")
ax.set_title("Convergence with the size of the basis")
ax.legend(fontsize=8)
```

The errors against the size of the basis on a logarithmic axis, with a tick at every size from 3 to 20. For $A = 1$ and $3$ the last point (the 20-level basis itself, whose error is zero by definition) is left out (`[:-1]`), because zero has no place on a logarithmic axis.

```python
save_figure(fig, "convergence",
            "The error of the probability $P$ (vertical axis, logarithmic) against "
            "the number of instantaneous levels kept in the basis (horizontal "
            "axis), for the sudden limit (blue, against the direct overlap of the "
            "two orbitals) and for the smooth passages at $A = 1$ and $A = 3$ "
            "(against the 20-level result). The errors fall steadily; with 20 "
            "levels the sudden limit is right to a few millionths.")
report("sudden limit: error with 20 levels", f"{errors["sudden"][-1]:.1e}")
report("A = 1: change from 18 to 20 levels", f"{errors[1.0][-3]:.1e}")
report("largest change of P when the steps are doubled or halved", f"{halving:.1e}")
check(errors["sudden"][-1] < 1e-5 and errors[1.0][-3] < 1e-6,
      "the 20-level basis is converged: sudden limit within 1e-5, A = 1 within 1e-6")
check(halving < 1e-9, "doubling or halving the time steps changes P by less than 1e-9")
```

Figure 22a.8 and Out [16]: with 20 levels the sudden limit is right to $4.2 \times 10^{-6}$; at $A = 1$ going from 18 to 20 levels changes $P$ by $2.4 \times 10^{-8}$ (`errors[1.0][-3]` is the entry of the 18-level basis, the third from the end of the list of sizes); and doubling or halving the time steps changes $P$ by at most $3.0 \times 10^{-11}$. The two checks require $10^{-5}$, $10^{-6}$ and $10^{-9}$.

*What the student should see in Figure 22a.8, and why.* All three error curves fall by several powers of ten as levels are added, with small ups and downs where a newly added level happens to matter little. The sudden limit converges most slowly (from $7 \times 10^{-3}$ with 3 levels to a few millionths with 20), because a sudden jump excites all levels at once, while a passage at a finite rate mostly reaches the nearby levels; the passage at $A = 1$ converges fastest. These measured errors are the uncertainties of the COMPUTED probabilities of In [12] and In [14]: they are thousands of times smaller than the effects the figures show.

**In [17], the breakdown estimate.**

```python
q_first = q_max[(688, "lam0", 0.0)]  # the largest Q of the free Fermi shell, A = 1
estimates = [
    ("naive: Q = 1 for the weakest recorded state", naive[weakest]),
    ("naive: Q = 1 for the band level, 0.02 <= q <= 6", 1.0 / g_star),
    ("first order: Q^2 reaches the sudden limit", math.sqrt(sudden) / q_first),
    ("exact: P reaches half the sudden limit", rate_half),
]
```

The four estimates of the breakdown rate of Section 22.8: the naive one for the weakest recorded state ($1/Q_{max}$, In [3]); the naive one for the band level of every shell and slice with redshifted momentum $0.02 \le q \le 6$ ($1/G^*$, In [6]); the first-order one, the rate at which $(AQ_0)^2$ reaches the sudden limit, $A = \sqrt{P_{sudden}}/Q_0$ with $Q_0 = 0.0934506$, the record's $Q_{max}$ of the free state $N = 688$ at the slice 0; and the exact $A_{1/2}$ (In [12]). `estimates` is a list of pairs (text, value).

```python
say("breakdown estimate                                    rate A")
for label, value in estimates:
    say(f"{label:50s} {value:9.3f}")
report("P at the record's rate A = 1, constant rate (dressed start)",
       f"{runs[1.0].min():.4f} ... {runs[1.0].max():.4f}")
report("P at the peak rate A = 1, smooth passage", f"{excited[6]:.4f}")
report("sudden limit over the span 0 ... 2, the most P reaches in the scan",
       f"{sudden:.4f}")
```

The table of Out [17], each text padded to 50 characters (`:50s`) and each rate printed with three digits after the point in a field of width 9: $10.701$, $10.021$, $2.929$ and $1.508$. Then the probability that a particle of the Fermi shell is outside its instantaneous level at the record's rate: between $0.0073$ and $0.0092$ along the constant-rate history with the dressed start, $0.0138$ at the end of the smooth passage with peak rate 1; and the sudden limit $0.0749$, the most that $P$ reached in the scan of In [12].

```python
NAMES = ["naive_rates", "one_curve", "across_the_gap", "sector_levels",
         "smooth_passage", "constant_rate", "sudden_ceiling", "convergence"]
missing = [name for number, name in enumerate(NAMES, start=1)
           if not output_file(f"{FIGURE_FOLDER}/22a_{number}_{name}.png").is_file()]
check(missing == [], "every figure file of this notebook exists")
all_checks_passed()
```

The last check requires that all eight figure files exist (`enumerate(NAMES, start=1)` numbers the names from 1, and the file of figure $k$ is `22a_k_name.png`), and the last line prints ALL 20 CHECKS PASSED (notebook 22a): two checks in In [2], one each in In [3] and In [4], three in In [5], two in In [7], one in In [8], two in In [9], three in In [12], one each in In [14] and In [15], two in In [16] and one in In [17].

### 22.13 What Notebook 22a found, and how a student could continue

**The results.** Every number below is printed by the notebook in the cell named; the uncertainties are the ones the notebook measures.

| result | value | status | where |
| --- | --- | --- | --- |
| largest $Q$ of the record at $A = 1$ | $0.0934532$ (N688_lamm2_a00) | COMPUTED (Revision record) | Out [2]; `adiabaticity.csv` |
| naive breakdown rate $1/Q_{max}$ of the weakest recorded state | $10.70$ | COMPUTED from the record | Out [3] |
| record's levels and $Q$ of the free Fermi shells, reproduced | to $8.8 \times 10^{-14}$ and $1.3 \times 10^{-13}$ (relative) | COMPUTED here | Out [5] |
| top of the curve $G(q) = Q/A$ of the band jump | $G^* = 0.09979$ at $q^* = 2.128$ | COMPUTED here ($\lambda = 0$) | Out [6] |
| naive breakdown rate of the band level of every shell with $0.02 \le q \le 6$ (all states of the record), $1/G^*$ | $10.02$ | COMPUTED here ($\lambda = 0$) | Out [6] |
| largest change of $Q_{max}$ by the interaction | $9.8$ percent (N136_lamp2_a20) | COMPUTED from the record | Out [7] |
| strongest jump from a negative level to a bulk level, per unit rate | $0.0489$ at $q = 0.111$ | COMPUTED here; its reading OPEN | Out [8] |
| $P$ at the end of the smooth passage with peak rate $A = 1$ | $0.0138$ | COMPUTED here | Out [12] |
| rate $A_{1/2}$ at which $P$ reaches half the sudden limit | $1.508$, between the scan rates $1.259$ and $1.585$ | COMPUTED here | Out [12] |
| sudden limit of the span $a_{4,0} = 0$ to $2$ | $0.074906$ (overlap), $0.074902$ (20-level basis) | COMPUTED here | Out [12] |
| $P$ along the constant rate $A = 1$, dressed start | $0.0073$ to $0.0092$ | COMPUTED here | Out [14], Out [17] |
| sudden limit for the end slices 4 and 6 | $0.1021$ and $0.1051$ | COMPUTED here ($\lambda = 0$, beyond the record's span) | Out [15] |
| numerical errors | total probability $1.2 \times 10^{-11}$; basis: sudden limit $4.2 \times 10^{-6}$, $A = 1$ $2.4 \times 10^{-8}$; time steps $3.0 \times 10^{-11}$ | measured | Out [12], Out [16] |

The rate $A_{1/2}$ comes from a straight-line interpolation in $\ln A$ between two rates of the scan (ten per factor 10); that $P$ crosses half the sudden limit between the scan rates $10^{0.1} = 1.259$ and $10^{0.2} = 1.585$ is certain, and the interpolated value $1.508$ lies between them; the interpolation error itself is not measured.

**What the results mean.** Four statements, each for the free field ($\lambda = 0$) in the sector computed, follow from the table.

- In this book's reading (Section 22.7; the record calls $Q^2$ the leading-order transition probability), the record's $Q$ measures the dressing, and the numbers confirm this reading: at a small rate ($A = 0.3$) a particle carries the dressing $\sum_mQ_{0m}^2$, and the exact evolution agrees with it within $11.3$ percent along the whole span (Out [14]).
- The naive criterion "$Q$ reaches 1" overestimates the breakdown rate about sevenfold ($10.7$ against $1.508$). The reason is visible in the derivation of Section 22.7: what can leave the level is a probability, $Q^2$ to first order, and what it should be compared with is not 1 but the largest probability that can leave at all, the sudden limit $0.0749$. The first-order estimate built on that comparison, $A = 2.929$, is within a factor of two of the exact $A_{1/2}$.
- The damage is capped: however fast the passage, at most about $7.5$ percent of the particles of the Fermi shell leave the band level over the record's span, and at most about $10.5$ percent even for a jump to the slice 6, because the band orbital itself changes little (Figure 22a.7).
- At the record's rate $A = 1$, about one percent of the Fermi-shell particles are outside their instantaneous level ($0.7$ to $0.9$ percent along the constant-rate history, $1.4$ percent at the end of the smooth passage). The instantaneous picture is therefore a fair first approximation at $A = 1$ for this sector, but the record's history is not deep inside the adiabatic regime: the gas stops following its levels at rates only about $1.5$ times larger.

**What the notebook does not show.** It treats the free field only, one sector only ($j = +1$, even parity, the Fermi shell of $N = 688$), and one particle at a time; it does not include the interaction, the other sectors, the many-body state or the thermal states. The probability $P$ counts the negative levels of the basis among the levels a particle can leave to; how that part is to be read in the quantised theory is part of the OPEN question of the negative branch. The history is a PRESCRIBED BACKGROUND, and the Z2 brane is ASSUMED.

**A consequence for Fermi-level crossings, from the record's own statement.** The exact evolution conserves the momentum, the block and the brane parity, so particles jump only between levels of the same sector (`Revision/kohn_sham/ks-theory.json`, key `adiabaticity.exactEvolution`). In the free field, therefore, the number of particles in every sector stays what it was at the start. When levels of different sectors cross the Fermi level, as in the record's example $N = 696$ (Section 22.5), the evolving gas cannot move its particles into the sector that the instantaneous ground state would fill: at best, in the adiabatic limit, it becomes the adiabatically continued state of the record, which lies above the instantaneous ground state by up to $8.623$ (units of $m$) at the slice 2 (`Revision/kohn_sham/results/adiabatic/crossing-demo.csv`). Whether interactions beyond the mean field (collisions, which the functional of the record does not contain) let the gas relax towards the instantaneous ground state is OPEN.

**How a student could continue.**

1. *Other shells and sectors.* By exact rule 2 the free evolution of a shell of momentum $k$ from the slice $s_1$ to the slice $s_2$ depends only on how $q = ke^{-a_4}$ moves from $ke^{-s_1}$ to $ke^{-s_2}$. Repeat In [9] to In [16] for the Fermi shell of $N = 136$ ($k = 0.5$), for the odd brane parity and for the block type $j = -1$, and draw the breakdown rate as a function of $k$.
2. *The interacting problem.* Write a time-dependent Kohn-Sham solver: evolve every occupied orbital of every sector with a method that conserves probability exactly, and at every time step recompute the densities $n(y)$ and $S(y)$ and from them $M = m + \tfrac{15}{16}\lambda S$ and $v = -\lambda n/16$ (`Revision/kohn_sham/ks-theory.json`, key `exchange.kohnShamPotentials`). Tests fixed in advance: for $\lambda = 0$ it must reproduce Notebook 22a; the particle number must be conserved; at a very small rate the gas must stay close to the record's instantaneous states; and the energy balance must follow the identity $dE/da_4 = -3\,(2\mathrm{Vol}_7)\int e^{6Hy}(p_3 - p_t)\,dy$ of the record (key `emt.energyChange`) up to the dressing.
3. *Crossings.* Follow the record's example $N = 696$ through its Fermi-level crossing with the evolution of item 2, and measure how far the evolved gas stays from the instantaneous ground state.
4. *The negative branch.* Formulate the jumps of Figure 22a.3 in the quantised theory: compare the modes of the field before and after a passage (the Bogoliubov method), and find out whether, with the Krein metric of Chapter 10, they describe the creation of pairs of quanta of positive norm. This is OPEN, and it concerns quanta inside one universe, not universes.

**Where to start.** The builder of the notebook, `Revision/textbook/notebooks/src/22a_adiabatic_breakdown.py`; the theory, `Revision/kohn_sham/ks-theory.json` (keys `adiabaticity`, `exchange`, `emt`); the Rust solver in `Revision/kohn_sham/solver` with its README; the folder `Revision/kohn_sham/results/adiabatic` (`adiabaticity.csv`, `crossing-demo.csv`, `fermi-level-crossings.csv`, `history.json`); the reference solver `Revision/kohn_sham/reference/run_reference.py` for a second method.

### 22.14 Problem 3: the back-reaction of the gas on $a_4$

**The question.** Every Kohn-Sham result of the record is a test-field result: the gas lives on the history $a_4 = AHx_4$, which is prescribed. The open problem is to solve the gas and the geometry together: a history $a_4(x_4)$ (or a more general metric) and gas states such that the gas is a solution in that geometry and its energy-momentum tensor is the source of that geometry in the field equations. An answer is such a solution, with its numbers checked as in Chapter 16, or a proof, under stated assumptions, that none exists.

**What is known.**

- PROVED (Chapter 12; `Revision/field_equations_a4/a4-equations.json`, key `generalSource`; both reports in `Revision/field_equations_a4/reports`): for the author's metric the Einstein-Lovelock equations reduce to the constraint (the $x_4$ component), the evolution equation $a_4''F(a_4') = \kappa(p_3 - p_t)$, the hidden ($x_8$) equation and conditions on the source: every component of the source must be independent of $x_8$, the source must obey $p_3 + p_t = 2p_8$, and its mixed $x_4$-$x_8$ components must vanish. The left-hand sides of the equations are free of $x_8$ (key `generalSource.x8_dependence`; independently `Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json`, check `einstein_x8_independent`), and that is why the source must be free of $x_8$ too.
- PROVED: the linear member $a_4 = AHx_4 + a_0$ needs $p_3 = p_t = p_8$ and a constant $\rho$ (check `linear_member_equal_pressures` of both reports).
- PROVED: in Einstein gravity every source obeys $\kappa(\rho + p_8) = -6\big((a_4')^2 + H^2\big)$ (check `einstein_null_energy_x8` of both reports; `Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json`, check `einstein_null_energy`). The derivation is given below.
- COMPUTED: no recorded Kohn-Sham state is an admissible source. The report is `ks-source-conditions.json` in the folder `Revision/field_equations_a4/reports`, and its checks say why. Check `ks_profiles_depend_on_x8`: for every state with a nonzero energy-momentum tensor the energy density varies along the hidden coordinate, by at least $0.0497$ of the largest component (smallest case N136_lamm2_a20). Check `ks_profiles_violate_algebraic_condition`: $\max_y|p_3 + p_t - 2p_8|/\max|T|$ lies between $2.09$ and $3.99$. Check `ks_integrals_violate_algebraic_condition`: even the source integrated over the hidden direction violates $p_3 + p_t = 2p_8$; the ratio $(\int p_3 + \int p_t)/(2\int p_8)$ is never 1 (closest $0.414$, N688_lamm2_a00). Check `ks_history_is_a_prescribed_background`: along the history the integrated energy changes, for example $\int\rho = 80.28$, $32.38$, $12.45$ for N136_lam0 at the slices 0, 1 and 2, and $p_3 \ne p_t$, while the linear member needs a constant $\rho$ and equal pressures.
- PROVED and COMPUTED, the energy exchange: along the history the energy of the gas changes as $dE/da_4 = -3\,(2\mathrm{Vol}_7)\int_{-L}^{0}e^{6Hy}(p_3 - p_t)\,dy$, where $\mathrm{Vol}_7$ is the coordinate volume of 3-space and the extra times. The identity is the key `emt.energyChange` of `Revision/kohn_sham/ks-theory.json`, verified by the check `adiabatic_hellmann_feynman` of the theory report `ks-theory-python.json`. The record computes both sides: for N688_lam0_a00 the finite difference of the energies gives $-597.9157012757526$ and the energy-momentum integral $-597.9157012806555$ (the columns `dE_da4_finite_difference` and `dE_da4_emt` of `adiabaticity.csv`). In a coupled solution this energy would have to be exchanged with the geometry.
- Chapter 12 constructs three exact solutions of the coupled equations of Einstein gravity and a homogeneous condensate of the classical field dirac16complex00, two of them with the extra times deflating as $e^{-Hx_4}$ (Notebook 12d; a computation of this book under the assumptions stated there, not a Revision record). For that classical, homogeneous source the back-reaction is solved. For the quantised gas it is OPEN.

**The null combination in Einstein gravity, line by line.** The constraint and the hidden equation of Einstein gravity (`Revision/field_equations_a4/a4-equations.json`, key `einstein`) are

$$
3(a_4')^2 + 21H^2 + \Lambda = -\kappa\rho, \qquad -3(a_4')^2 + 15H^2 + \Lambda = \kappa p_8 .
$$

$$
\kappa\rho = -3(a_4')^2 - 21H^2 - \Lambda .
$$

Rule: multiply the constraint by $-1$.

$$
\kappa(\rho + p_8) = -3(a_4')^2 - 21H^2 - \Lambda - 3(a_4')^2 + 15H^2 + \Lambda = -6(a_4')^2 - 6H^2 .
$$

Rule: add the hidden equation; $\Lambda$ cancels, $-3 - 3 = -6$ and $-21 + 15 = -6$.

The right-hand side is negative for every real history when $H > 0$. So in Einstein gravity, with a positive coupling $\kappa$, every source of the author's metric must have $\rho + p_8 < 0$ everywhere: it must violate the null energy condition along the hidden direction. This holds for every $a_4$ and every $\Lambda$; any candidate source, a time-dependent Kohn-Sham gas included, must meet it, or the gravity theory must contain more than the Einstein term.

**Why it is hard.** The metric of the record fixes the dependence on $x_8$ completely ($\sin^{1/3}z$ and $\cot^2z$), and leaves only one free function, $a_4(x_4)$. A gas bound to the brane, whose density falls off towards the tip, cannot be the source of such a metric: its energy-momentum depends on $y$. A coupled solution therefore needs a more general metric, whose factors depend on $y$ and on $x_4$; the field equations then become partial differential equations in two variables, and the Kohn-Sham reduction of Chapter 14, which used the exact warp $e^{Hy}$, must be redone for the new metric at every step. In addition, the brane enters (Problem 4), the couplings $\alpha_2$, $\alpha_3$, $\Lambda$ and $\kappa$ are unknown, and in Einstein gravity the source must violate the null energy condition along $x_8$, as just shown.

**A first step.** (a) Redo the derivation above, and its Einstein-Gauss-Bonnet version from the general null combination of the record (`Revision/field_equations_a4/a4-equations.json`, key `generalSource.nullCombinations`). (b) Check the energy-exchange identity on the record's numbers (Exercise 7 of Section 22.20). (c) Write down a more general metric that keeps the symmetries of the author's metric (3-space isotropic, the three extra times isotropic) but lets the factors depend on $y$ and $x_4$, for example $ds^2 = e^{2\mathcal{A}(y, x_4)}(dx_1^2 + dx_2^2 + dx_3^2) - e^{2\mathcal{B}(y, x_4)}(dx_5^2 + dx_6^2 + dx_7^2) - e^{2\mathcal{C}(y, x_4)}dx_4^2 + dy^2$, which contains the author's metric as $\mathcal{A} = Hy + a_4$, $\mathcal{B} = Hy - a_4$, $\mathcal{C} = 0$ (this ansatz is a suggestion of this book, a HYPOTHESIS about a useful next step, not a result). Compute its Einstein tensor with two independent programs, as the record does for the author's metric, and find which conditions it puts on a source. (d) Only then ask whether a Kohn-Sham gas can satisfy them, starting with the free gas.

**Where to start.** `Revision/field_equations_a4/README.md` and its verifiers; `Revision/field_equations_a4/python/check_ks_source_conditions.py` and its report; the lead's independent curvature code `Revision/lead_checks/einstein_gauss_bonnet_a4.py`; the profiles `Revision/kohn_sham/results/ground/profiles` and the integrals `Revision/kohn_sham/results/ground/emt-integrals.csv`; the GKD and Lovelock programs of Chapter 11 in `Revision/gkd_lovelock`.

### 22.15 Problem 4: the Z2 brane and its junction conditions

**The question.** The hidden direction ends at $z = \pi/2$, the brane. The record continues the universe beyond it by its mirror image, the Z2 construction: the field on the mirror patch $\pi/2 < z < \pi$ is the reflected field. This is ASSUMED. The open problem is to derive it, or to replace it, from field equations: which conditions must the metric and the field satisfy at the brane (the **junction conditions**), what energy and momentum must sit on the brane itself, and is the mirror the right continuation? An answer is a set of junction conditions derived from the field equations of gravity and of the field, with the brane's energy-momentum, checked like every other exact statement of the record.

**What is known.**

- PROVED: the map $z \to \pi - z$ (that is, $x_8 \to \pi/(6H) - x_8$) is an isometry of the author's metric: every component takes the same value at $z$ and at $\pi - z$ (`Revision/pairing/reports/python-pairing.json`, check `geometry.mirror_isometry`; `Revision/pairing/reports/wolfram-pairing.json`, check `T2_mirror_is_isometry`).
- PROVED: in the coordinate $x_8$ the metric is degenerate at the brane: $g_{88} = \cot^2z$ and $\sqrt{|g|} = \cos z$ vanish at $z = \pi/2$ (`Revision/pairing/reports/python-pairing.json`, check `geometry.brane_degenerate`).
- ASSUMED (`Revision/kohn_sham/ks-theory.json`, key `boundaryConditions.brane`): the Z2 mirror (orbifold) at $y = 0$, with the mirror warp $e^{-H|y|}$; continuity of the mirrored field gives the two brane parities, $b(0) = 0$ (even) and $a(0) = 0$ (odd), which both stop the current along $y$ (checks `bc_brane_parity_conditions`, `bc_mirror_map_PA` and `bc_mirror_parities_of_densities` of `Revision/kohn_sham/reports/ks-theory-python.json`). PROVED under this assumption: the doubled problem is symmetric under the mirror exactly when the mirror copy carries $(-m, +\lambda)$ (`Revision/pairing/kohn_sham/reports/python-t3.json`, check `T3.z2_mirror_copy_carries_minus_m_plus_lambda`).
- What rests on it: theorem T2 in the author's field (the mirror pairing), theorem T3, and every Kohn-Sham number of the record (the densities are those of the doubled system, each patch with the weight $1/2$; key `densities.total`).
- NOT established, as the record says itself: "no junction condition, brane tension or matching of the field across it is derived" (`Revision/pairing/reports/python-pairing.json`, key `not_established`). OPEN.

**The brane in the coordinate y, line by line.** The two derivations of this paragraph and the next are the book's own, built on statements of the record; no Revision verifier checks them as such. The record's hidden coordinate is $y = \ln(\sin z)/(6H)$, with $dy = \cot z\,dx_8$ (`Revision/kohn_sham/ks-theory.json`, key `geometry.hiddenCoordinate`).

$$
\cot^2z\,dx_8^2 = dy^2 .
$$

Rule: square both sides of $dy = \cot z\,dx_8$.

$$
\sin z = e^{6Hy}, \qquad \sin^{1/3}z = e^{2Hy} .
$$

Rule: solve $y = \ln(\sin z)/(6H)$ for $\sin z$ (multiply by $6H$, then apply the exponential), and raise both sides to the power $1/3$.

$$
ds^2 = e^{2Hy}\big[e^{2a_4}(dx_1^2 + dx_2^2 + dx_3^2) - e^{-2a_4}(dx_5^2 + dx_6^2 + dx_7^2)\big] - dx_4^2 + dy^2 .
$$

Rule: insert both lines into the author's metric (the record's key `geometry.lineElement`; check `geometry_warped_form` of `Revision/kohn_sham/reports/ks-theory-python.json`).

At the brane $y = 0$ every coefficient of this line element is finite and nonzero ($e^{0} = 1$). The zero of $g_{88}$ in the coordinate $x_8$ belongs to that coordinate: $dx_8 = \tan z\,dy$, and $\tan z$ grows without bound as $z \to \pi/2$, so near the brane one unit of $y$ corresponds to ever more units of $x_8$. In the same way $\sqrt{|g|}$ is $e^{6Hy} = \sin z$ in the coordinate $y$, and $\sin z \cdot \cot z = \cos z$ in the coordinate $x_8$ (rule: a volume element changes by the factor $|dy/dx_8| = \cot z$). What makes the brane special is therefore not a singularity of the geometry but the end of the coordinate range: $y$ cannot exceed 0, because $\sin z$ cannot exceed 1. To go on, a continuation must be chosen, and the Z2 mirror is one choice.

**The mirror has a kink, line by line.** On the patch the warp factor of the six directions $x_1, x_2, x_3, x_5, x_6, x_7$ is $W(y) = e^{Hy}$ (key `geometry.warp`). The mirror continues it to $W(y) = e^{-H|y|}$ on $-L \le y \le L$ (key `boundaryConditions.brane`).

$$
W'(y) = He^{Hy} \ \ (y < 0), \qquad W'(y) = -He^{-Hy} \ \ (y > 0) .
$$

Rule: for $y < 0$, $|y| = -y$ and $W = e^{Hy}$; for $y > 0$, $|y| = y$ and $W = e^{-Hy}$; differentiate each.

$$
W'(0^-) = H, \qquad W'(0^+) = -H .
$$

Rule: let $y$ go to 0 from below and from above; $e^{0} = 1$. The function $W$ is continuous at $y = 0$ (both sides give 1) but its slope jumps by $-2H$: $W$ has a kink.

$$
\int_{-\epsilon}^{\epsilon}W''(y)\,dy = W'(\epsilon) - W'(-\epsilon) = -He^{-H\epsilon} - He^{-H\epsilon} = -2He^{-H\epsilon} \ \to\ -2H \quad (\epsilon \to 0) .
$$

Rule: the fundamental theorem of calculus (the integral of a derivative is the difference of the values at the ends), then the two slopes above, then $e^{-H\epsilon} \to 1$.

The integral of $W''$ over an interval around the brane does not shrink to zero with the interval: the second derivative of $W$ has a part concentrated on the brane. The curvature of a metric contains the second derivatives of its components, so the curvature of the doubled metric has a part concentrated on the brane, and the field equations can then only hold if the source has a part concentrated there too: energy and momentum that live on the brane. Which energy density and which pressures, in which directions, the field equations demand is exactly what the junction conditions would say. Nobody has derived them for this metric: OPEN.

**Why it is hard.** The brane is a 7-dimensional surface whose own signature is (3,4): three space directions $x_1, x_2, x_3$ and four times $x_4, x_5, x_6, x_7$. The junction conditions of general relativity (W. Israel, Nuovo Cimento B 44, 1 (1966); quoted, not derived here) are formulated for surfaces in ordinary spacetime; the Lovelock terms of Chapter 11 change them; and the warp multiplies only six of the seven brane directions, because $x_4$ is not warped. For the field, the record's parities come from continuity of the mirrored field; other continuations are possible, and T2 and T3 depend on this one.

**A first step.** (a) Redo the two derivations above. (b) Compute the curvature of the doubled metric with $W = e^{-H|y|}$, keeping the concentrated parts, with two independent programs (the lead's curvature code in `Revision/lead_checks/einstein_gauss_bonnet_a4.py` is one starting point); write down the brane energy-momentum that Einstein's equations then require, and check whether it is a pure tension (the same negative pressure in every brane direction) or whether the unwarped time $x_4$ makes it different in different directions. (c) Integrate the field equation of the spinor across the brane in the same way and compare the resulting matching conditions with the record's parities $b(0) = 0$ and $a(0) = 0$. (d) Solve the Kohn-Sham problem of Chapter 15 with another brane condition and measure how much the levels and energies change.

**Where to start.** The Kohn-Sham theory record `Revision/kohn_sham/ks-theory.json`, with its keys `geometry` and `boundaryConditions`, and the two verifiers of this record in the folder `Revision/kohn_sham/theory`. For the mirror pairing, the pairing record `Revision/pairing/pairing-theory.json`, the T3 record `t3-theory.json` in the folder `Revision/pairing/kohn_sham`, and section 5.4 of the document `Revision/docs/PAIR_CREATION_PROOFS.md`, which proves T2 with the mirror.

### 22.16 Problem 5: the dark-sector hypotheses

**The question.** The author's request contains two hypotheses, quoted from `Revision/README.md`: "Hypothesis: dirac16complex provides a possible physical mechanism for a time-varying dark energy equation of state and/or a possible physical mechanism for a time-varying dark matter equation of state, both of which you will investigate." and "Hypothesis00: dirac16complex00 provides [the same], both of which you will investigate." (the brackets are those of the README, which abridges the repeated sentence). The open problem is to investigate them: compute the equation of state that an observer in 3-space would see as the extra times deflate and 3-space inflates, its change in time, and compare it with the observations. An answer is such a computation with its uncertainties, and an honest statement of what each field can and cannot produce.

**What is known.** Status: HYPOTHESIS, being investigated. The investigation is planned in the Revision record (`Revision/SPEC.md`, section 8; the planned folder `Revision/dark_sector` is listed as "to do (wave 2)" in the table of `Revision/README.md`), and no result of it exists in the record. This book claims no result about the dark sector. The observational numbers to which the plan refers come from a private document of the author, and the book quotes them only as `Revision/README.md` states them: the parametrisation $w(a) = w_0 + w_a(1 - a)$ (CPL), the constant-$w$ fit $w = -0.764$, and $(w_0, w_a) = (-0.861, -0.60)$; in this convention thawing means $w_a < 0$. In that document $H$ is the Hubble rate and $a$ the scale factor of the observed universe; they are not the $H$ and $a_4$ of the author's metric.

**What the CPL numbers say, line by line.**

$$
w(1) = w_0 + w_a \cdot 0 = w_0 = -0.861 .
$$

Rule: today the scale factor is $a = 1$, so $1 - a = 0$.

$$
w(0) = w_0 + w_a = -0.861 - 0.60 = -1.461 .
$$

Rule: in the far past $a \to 0$, so $1 - a \to 1$.

So the fitted $w$ falls below $-1$ in the past. What that requires:

$$
w < -1, \ \rho > 0 \quad\Longleftrightarrow\quad p < -\rho \quad\Longleftrightarrow\quad \rho + p < 0 .
$$

Rule: multiply $w = p/\rho < -1$ by the positive number $\rho$ (the direction of an inequality is kept), then add $\rho$ to both sides.

A fluid of positive energy density with $w < -1$ (called **phantom**) violates the null energy condition. Whether anything in this theory can appear to a 3-space observer as such a fluid is part of the question; nothing is claimed.

**What bears on the question (not dark-sector results).** PROVED: the 7-volume of the author's metric does not change with $a_4$ ($\sqrt{|g|} = \cos z$, Chapter 12), and for a source free of $x_8$ the conservation law reads $\rho' = -3a_4'(p_3 - p_t)$: energy is exchanged between 3-space and the extra times through the difference of their pressures. The record states the law under the key `generalSource.conservation_reduced` of `Revision/field_equations_a4/a4-equations.json`, and the lead's report `emt-divergence-and-spin-connection.json` in the folder `Revision/lead_checks/reports` verifies it independently with the check `divergence_x4_component`. In the good sector the Kohn-Sham gas has no kinetic pressure along the extra times: $p_t = e_{int}$ (key `emt.p_t` of the Kohn-Sham theory record). And the history along which the Kohn-Sham states are computed is a PRESCRIBED BACKGROUND; in the words of the record (`history.json`, key `status`), "quantities derived along this history (energies, pressures, equations of state) are not consequences of the coupled field equations". Any equation of state read from these states inherits this limitation.

**Why it is hard.** The observations are made in four dimensions, the theory lives in eight. One must define what the observer measures: which scale factor plays the role of the observed $a$, which energy density and pressure the observer sees (integrated over the hidden direction and the extra times, or not), and how the time $x_4$ relates to the time of the observations. Each choice must be justified, not fitted. The equations of state must be consequences of the coupled equations, which brings back Problem 3. And a phantom value $w < -1$ needs a source that violates the null energy condition, which an ordinary gas of positive energy does not do.

**A first step.** (a) Write down precise definitions of the observer's density, pressure and scale factor; the record's plan (`Revision/SPEC.md`, sections 8 and 11) proposes some and labels its own analysis as "to be CHECKED by the dark-sector work, not results". (b) Compute the equation of state for the simplest sources with these definitions: the homogeneous condensates of Chapters 9 and 12, whose $w = p/\rho$ is constant, and the Kohn-Sham gas along the prescribed history, with that caveat stated. (c) Fit the CPL form, compare with the values above, and report honestly what each field can and cannot produce.

**Where to start.** `Revision/README.md` and `Revision/SPEC.md` (sections 8 and 11); the energy-momentum tensors of the theory record, `Revision/theory/field-theory.json`; the Kohn-Sham integrals `Revision/kohn_sham/results/ground/emt-integrals.csv` and the thermal results in `Revision/kohn_sham/results/thermo`; the equations for $a_4$ in `Revision/field_equations_a4/a4-equations.json`.

### 22.17 Problem 6: matter and antimatter

**The question.** The universe we observe contains matter and almost no antimatter (Chapter 21 teaches the observations and the measured baryon-to-photon ratio from zero). The author asked that this theory solve the matter-antimatter mysteries. The open problem is whether an extension of the theory could produce the observed excess of matter from a start without excess, and with the measured size.

**What is known.**

- PROVED: the U(1) charge of each field, $Q = \int\cos z\,\Psi^\dagger B\Psi\,d^7x$, is exactly conserved on every solution in the author's metric (`Revision/lead_checks/reports/charge-conjugation-and-u1.json`, check `u1_noether_matrix_identity`). Hence no net charge can be generated inside one universe.
- PROVED: the charge conjugations are matrices: $\mathcal{C}_+ = C$ (same mass) and $\mathcal{C}_- = \Gamma C$ (mass reversed) (checks `charge_conjugation_matrix_plus` and `charge_conjugation_matrix_minus` of the same report); for a real commuting field the current vanishes identically and $\mathcal{C}_+$ acts as the identity, so the nontrivial real map between matter and antimatter is the matrix $\Gamma$ with the mass reversed, which is T1 (check `real_fields_charge_conjugation`); for the quantised Grassmann field the conjugation that keeps the canonical anticommutator is $\Psi \to \Gamma\Psi^{\dagger T}$, which reverses the mass (check `quantum_charge_conjugation_unitary_type`). Chapters 5 and 21 derive all of this.
- PROVED: a T1 partner carries the opposite charge, so a T1 pair $\{+m, -m\}$ has total charge zero as classical bilinears (T1d, Chapter 18); for two universes that are quantised independently of each other there is no such cancellation (Q). The idea that our universe has a partner of opposite charge, an anti-universe, belongs to a class of ideas of which one published example is L. Boyle, K. Finn and N. Turok, Phys. Rev. Lett. 121, 251301 (2018). That our universe has such a partner is a HYPOTHESIS.
- The theory as built does NOT solve the matter-antimatter problem: it has no baryons, no process that violates baryon number, no violation of CP, and no computation of a departure from thermal equilibrium.

**What would be needed.** Sakharov's three conditions (Chapter 21) in an extended theory: processes that violate baryon number; violation of C and of CP; and a departure from thermal equilibrium; and then a computation of the excess that agrees with the measured baryon-to-photon ratio. Every scenario that adds these is a HYPOTHESIS until it is computed and checked.

**Why it is hard.** The U(1) symmetry of the theory is exact, so an asymmetry needs new terms in the Lagrangian, and with every new term the pairing theorems must be derived again (they hold for the Lagrangian of the record, not for an arbitrary extension). The field dirac16complex is not the field of the baryons of the Standard Model, so even a charge asymmetry of this field would still have to be connected to baryons. A departure from equilibrium needs the time-dependent dynamics of Problem 2, and a quantum computation of rates needs the Krein quantisation of Chapter 10 beyond the good sector.

**A first step.** (a) List the simplest terms that could be added to the Lagrangian and decide, with the exact matrix methods of the record (the solution of $M(\gamma^a)^* = \pm\gamma^aM$ in `Revision/lead_checks/charge_conjugation_and_u1.py` is the model), which of them break the U(1) and which of the discrete maps ($\mathcal{C}_+$, $\mathcal{C}_-$, $\Gamma$, the reflections) they respect. (b) For each such term, derive T1 again and state exactly how it changes. (c) Only then add a departure from equilibrium, with the time-dependent tools of Problem 2, and compute the charge produced from a symmetric start. Each of these steps is labelled HYPOTHESIS until it is done and checked.

**Where to start.** `Revision/lead_checks/charge_conjugation_and_u1.py` and its report; Chapters 5 and 21 and their notebooks; the pairing record `Revision/pairing/pairing-theory.json`.

### 22.18 Smaller open items

The table lists further open items that earlier chapters met, with their status and the record that states them.

| item | status | record |
| --- | --- | --- |
| modes with momentum along the extra times grow, at rates without bound | the growth PROVED; a mechanism that removes it, or a well-posed formulation, OPEN | `Revision/theory/reports/python-scope.json`, check `extra_time_growth_rates_unbounded`; Chapter 8 |
| every quantum and Kohn-Sham result is restricted to the good sector (no extra-time momentum) | ASSUMED | `Revision/kohn_sham/ks-theory.json`, key `sectorAndAnsatz.sector`; Chapter 10 |
| a positive-norm Fock space for a universe beyond the good sector | not established; OPEN | `Revision/pairing/reports/python-pairing.json`, key `not_established` |
| correlation in the Kohn-Sham functional | none (Hartree and exchange only); ASSUMED | `Revision/kohn_sham/ks-theory.json`, key `exchange.kohnShamPotentials.correlation` |
| which levels count as particles (the positive branch and the zero modes at $k = 0$) | CONVENTION; its justification OPEN | `Revision/kohn_sham/ks-theory.json`, key `thermodynamics.fillingConvention` |
| the tip at $y = -3$ with the tip angle $\theta = 0$ | CHOSEN | `Revision/kohn_sham/ks-theory.json`, key `boundaryConditions.tip` |
| the meaning of jumps into the negative branch | OPEN | Notebook 22a, In [8]; Section 22.13 |
| relaxation of the gas through Fermi-level crossings | OPEN | `Revision/kohn_sham/results/adiabatic/crossing-demo.csv`; Section 22.13 |

### 22.19 What we proved, what we computed, what we assumed

**PROVED** (exact; each derivation is written out line by line in this chapter; the record checks are named where the Revision record verifies the statement):

| statement | where it is verified |
| --- | --- |
| a T1 pair as the complete source leaves no real history $a_4$ in Einstein gravity for $H > 0$ (corollary C1): $(a_4')^2 = -H^2$ | `wolfram-a4-report.json`, `einstein_no_vacuum_solution`; `python-a4-report.json`, `einstein_no_vacuum`; lead's report `einstein-gauss-bonnet-a4.json`, `no_vacuum_for_H_positive`; Section 22.4 |
| the Ricci scalar of the author's metric is $R = 6(a_4')^2 - 42H^2$ | derived in Section 22.4 from the record's Einstein components; no Revision verifier checks $R$ itself |
| the total probability $\langle\chi\vert \chi\rangle$ is conserved | `ks-theory-python.json` and `ks-theory-wolfram.json`, `hamiltonian_16_hermitian`; Section 22.6 |
| $K_{mn} = \langle m\vert \partial_a h\vert n\rangle/(\varepsilon_n - \varepsilon_m)$ for $m \ne n$ | `ks-theory-python.json`, `adiabatic_offdiagonal_identity`; Section 22.6, line 6 |
| $\partial_a h = -j\kappa k\sigma_3$ in the free field | `ks-theory-python.json`, `adiabatic_hellmann_feynman`; Section 22.6, line 8 |
| the amplitude equations (lines 1 to 5) and $K_{nn} = 0$ (line 7) | derivations of this book, Section 22.6; no Revision check covers them |
| the dressing amplitude $\vert \alpha_m\vert  = Q_{0m}$; $Q(A) = A\,Q(1)$ | derivations of this book, Section 22.7 ($Q(A) = A\,Q(1)$ read off the record's formula, `ks-theory.json`, key `adiabaticity.measure`); the dressing tested numerically in Notebook 22a, In [14] |
| in the free field $Q/A = G(q)$ with $q = ke^{-a_{4,0}}$ | `ks-theory-python.json`, `rescaling_identity`; Section 22.7 |
| the sudden limit $P_{sudden} = 1 - \vert \langle\varphi_0(s_2)\vert \varphi_0(s_1)\rangle\vert ^2$, the rate of the smooth passage, the first-order formula for $P^{(1)}$ | derivations of this book, Section 22.8; tested numerically in Notebook 22a, In [12] and In [14] |
| in Einstein gravity every source has $\kappa(\rho + p_8) = -6((a_4')^2 + H^2)$ | both a4 reports, `einstein_null_energy_x8`; lead's report, `einstein_null_energy`; Section 22.14 |
| the line element in the coordinate $y$ is regular at $y = 0$; the mirror warp $e^{-H\vert y\vert }$ has a kink, and $\int_{-\epsilon}^{\epsilon}W''\,dy \to -2H$ | derived in Section 22.15 from the record's statements (`ks-theory-python.json`, `geometry_warped_form`) |
| $w(1) = w_0$, $w(0) = w_0 + w_a$; $w < -1$ with $\rho > 0$ if and only if $\rho + p < 0$ | algebra, Section 22.16 |
| exact U(1) conservation, the charge-conjugation matrices, T1, T2, Q, T3 | Chapters 5 and 18 to 21; `charge-conjugation-and-u1.json`, pairing and T3 reports |

**COMPUTED** (numerical, with measured accuracy): from the Revision record, $Q_{max} \le 0.0935$ for the 75 ground states at $A = 1$, the adiabatically continued state of $N = 696$ above the instantaneous ground state by up to $8.623$, the violations of the source conditions (ratios $2.09$ to $3.99$, closest integrated ratio $0.414$), and the agreement of $dE/da_4$ from finite differences and from the energy-momentum integral (for N688_lam0_a00, $-597.9157012757526$ against $-597.9157012806555$). In Notebook 22a (free field, the Fermi-shell sector of $N = 688$): the record's levels and $Q$ reproduced to $10^{-13}$; $G^* = 0.09979$ at $q^* = 2.128$; the strongest jump across the gap $0.0489$ per unit rate; $P = 0.0138$ at the peak rate 1; $A_{1/2} = 1.508$; the sudden limit $0.0749$ (span 0 to 2) and $0.1051$ (0 to 6); the breakdown estimates $10.701$, $10.021$, $2.929$ and $1.508$; with the errors of Section 22.13.

**ASSUMED**: the Z2 brane and the parities it gives; the good sector; the tip (CHOSEN); which levels count as particles (CONVENTION); the history $a_4 = AHx_4$ (PRESCRIBED BACKGROUND); in Notebook 22a the free field ($\lambda = 0$) and one sector; the expansion in instantaneous orbitals, truncated to 20 levels with its convergence measured; the first-order approximations of Sections 22.7 and 22.8, whose range of validity the notebook measures.

**HYPOTHESIS**: the author's dark-sector hypotheses; that our universe has a partner of opposite charge; every scenario of creation or of matter-antimatter asymmetry; the generalised metric of Section 22.14 and the reduced quantum model of Section 22.4 as useful next steps.

**OPEN**: whether any universe is created, in pairs or otherwise (no creation process, rate, amplitude or big-bang dynamics follows from the equations); the time-dependent Kohn-Sham problem with interaction; the reading of jumps into the negative branch; relaxation through Fermi-level crossings; the back-reaction of the gas on $a_4$; the junction conditions of the brane; the equation of state seen by a 3-space observer; an asymmetry between matter and antimatter in an extended theory; the extra-time modes beyond the good sector.

### 22.20 Exercises

**Exercise 1.** The record's largest $Q$ of the free state N136_lam0_a00 is $0.0851488$ at $A = 1$ (Out [5]). (a) What is its naive breakdown rate? (b) What is $Q$ at $A = 5$, and the first-order dressing probability $Q^2$ there? (c) Can the first-order estimate be trusted at $A = 5$?

*Answer.* (a) By exact rule 1, $Q(A) = 0.0851488\,A$ reaches 1 at $A = 1/0.0851488 = 11.744$. (b) $Q(5) = 5 \cdot 0.0851488 = 0.425744$ and $Q^2 = 0.181258$. (c) No: first order needs $Q \ll 1$, and $0.43$ is not small. Notebook 22a shows for the free Fermi shell of $N = 688$ what happens at such rates: the exact probability levels off at the sudden limit of about $0.075$ over the record's span, while the first-order estimate overshoots (Figure 22a.5). A first-order number of $0.18$ is therefore not to be trusted.

**Exercise 2.** From the row of Out [5] for $N = 688$ at the slice 0 ($\varepsilon_0 = 1.247113$, $\varepsilon_1 = 3.500518$, $Q = 0.0934506$) compute the energy difference, the matrix element $|\langle 0|\partial_a h|1\rangle|$ and $|K_{10}|$. Compare with the record's column `Q_max_matrix_element` ($0.4745266881$) and with the right panel of Figure 22a.4.

*Answer.* $\varepsilon_1 - \varepsilon_0 = 2.253405$. From $Q = |\langle 0|\partial_a h|1\rangle|/(\varepsilon_1 - \varepsilon_0)^2$ (Section 22.7, with $A = H = 1$): $|\langle 0|\partial_a h|1\rangle| = Q(\varepsilon_1 - \varepsilon_0)^2 = 0.0934506 \cdot 5.077834 = 0.474527$, which agrees with the record to the seven digits of the inputs. By line 6 of Section 22.6, $|K_{10}| = |\langle 1|\partial_a h|0\rangle|/|\varepsilon_0 - \varepsilon_1| = Q(\varepsilon_1 - \varepsilon_0) = 0.0934506 \cdot 2.253405 = 0.210582$, the starting value of the blue curve on the right of Figure 22a.4.

**Exercise 3.** Show that the cubic polynomial $p(t)$ with $p(0) = f_0$, $p(h) = f_1$, $p'(0) = f_0'$, $p'(h) = f_1'$ has the value $p(h/2) = (f_0 + f_1)/2 + h(f_0' - f_1')/8$ in the middle (the rule of the function `orbitals` in In [4]). Test it on $f(t) = t^3$ with $h = 1$.

*Answer.* Write $p(t) = f_0 + f_0't + ct^2 + dt^3$; this already gives $p(0) = f_0$ and $p'(0) = f_0'$. Put $\Delta = f_1 - f_0 - f_0'h$ and $\delta = f_1' - f_0'$. The two conditions at $t = h$ read $ch^2 + dh^3 = \Delta$ and $2ch + 3dh^2 = \delta$. Multiply the first by $3/h$ and subtract the second: $ch = 3\Delta/h - \delta$, so $ch^2 = 3\Delta - \delta h$, and from the first condition $dh^3 = \Delta - ch^2$. Then $p(h/2) = f_0 + f_0'h/2 + ch^2/4 + dh^3/8 = f_0 + f_0'h/2 + ch^2/4 + (\Delta - ch^2)/8 = f_0 + f_0'h/2 + ch^2/8 + \Delta/8$. Insert $ch^2 = 3\Delta - \delta h$: $ch^2/8 + \Delta/8 = \Delta/2 - \delta h/8$. Hence $p(h/2) = f_0 + f_0'h/2 + (f_1 - f_0 - f_0'h)/2 - (f_1' - f_0')h/8 = (f_0 + f_1)/2 + h(f_0' - f_1')/8$. Test: $f_0 = 0$, $f_1 = 1$, $f_0' = 0$, $f_1' = 3$: $(0 + 1)/2 + (0 - 3)/8 = 0.5 - 0.375 = 0.125 = (1/2)^3$. Exact, as it must be, because $t^3$ is itself a cubic.

**Exercise 4.** Compute the redshifted momenta of the Fermi shell of $N = 136$ at the slice $1.5$ and of the Fermi shell of $N = 688$ at the slice 2. Why are their $Q$ in Out [5] ($0.0527487$ and $0.0528933$) nearly equal, and why is the second slightly larger?

*Answer.* $q = 0.5\,e^{-1.5} = 0.5 \cdot 0.223130 = 0.111565$ and $q = 0.829156\,e^{-2} = 0.829156 \cdot 0.135335 = 0.112214$ (Out [5] prints $0.1116$ and $0.1122$). By exact rule 2 the free $Q/A$ depends only on $q$, and the two values of $q$ differ by only $0.6$ percent, so the two $Q$ are nearly equal although the shells and the slices are different. In this range $G(q)$ rises with $q$ (the whole recorded range lies left of the top in Figure 22a.2), so the larger $q$ has the slightly larger $Q$. The band levels behave the same way: $0.204636$ and $0.205760$.

**Exercise 5.** The sudden limit of the span $a_{4,0} = 0$ to $2$ is $P_{sudden} = 0.074906$ (Out [12]). Compute the overlap $|\langle\varphi_0(2)|\varphi_0(0)\rangle|$ and the angle $\theta$ with $\cos\theta$ equal to it. Show that for a particle whose orbital is turned by the angle $\theta$ in the plane of two orthonormal orbitals, $P_{sudden} = \sin^2\theta$.

*Answer.* $|\langle\varphi_0(2)|\varphi_0(0)\rangle| = \sqrt{1 - 0.074906} = \sqrt{0.925094} = 0.961818$, and $\theta = \arccos 0.961818 = 0.27723$ radian, about $15.9$ degrees. If the new band orbital is $\varphi_0(2) = \cos\theta\,\varphi_0(0) + \sin\theta\,\varphi_1$ with $\varphi_1$ orthonormal to $\varphi_0(0)$, the overlap is $\cos\theta$ and $P_{sudden} = 1 - \cos^2\theta = \sin^2\theta$; here $\sin^2(0.27723) = 0.074906$. The band orbital turns by only about 16 degrees over two e-folds of the extra times.

**Exercise 6.** Show that $a_4' = iH$ with $\Lambda = -18H^2$ solves both vacuum equations of Einstein gravity of Section 22.4. Why is it not a history of the author's universe?

*Answer.* $(iH)^2 = -H^2$. The $x_4$ equation: $3(-H^2) + 21H^2 - 18H^2 = 0$. The $x_8$ equation: $-3(-H^2) + 15H^2 - 18H^2 = 3H^2 + 15H^2 - 18H^2 = 0$. Both hold. But $a_4 = iHx_4 + a_0$ is complex, so the metric components $e^{2a_4}\sin^{1/3}z$ would be complex numbers, and a metric must be real. So there is no real history: this is corollary C1 again.

**Exercise 7.** The source-condition report gives for N136_lam0_a00 the integrals $\int\rho = 80.2822$, $\int p_3 = 23.8133$, $\int p_t = 0$ (each $2\mathrm{Vol}_7\int e^{6Hy}(\ldots)\,dy$). Use the energy-exchange identity of Section 22.14 to compute $dE/da_4$, and compare with the record's columns `dE_da4_emt` ($-71.43975618$) and `dE_da4_finite_difference` ($-71.43975618$). Do the same for N688_lam0_a00 ($\int p_3 = 199.305$, $\int p_t = 0$). What does the sign mean?

*Answer.* $dE/da_4 = -3(\int p_3 - \int p_t) = -3 \cdot 23.8133 = -71.4399$, in agreement with both columns to the six digits that the source-condition report prints. For $N = 688$: $-3 \cdot 199.305 = -597.915$, against $-597.9157$ in the record. The sign: as $a_4$ grows (the extra times deflate and 3-space inflates), the energy of the gas falls, because its 3-momenta redshift; $p_t = 0$ here because the gas has no kinetic pressure along the extra times. In a coupled solution this energy would have to go into the geometry, which is why the history cannot be the linear member with a constant $\rho$ (Section 22.14).

**Exercise 8.** For the mirror warp $W(y) = e^{-H|y|}$ with $H = 1$: compute $W(0)$, the slopes $W'(0^-)$ and $W'(0^+)$, and $\int_{-0.01}^{0.01}W''\,dy$. Then show that $\sqrt{|g|} = e^{6Hy}$ in the coordinate $y$ becomes $\cos z$ in the coordinate $x_8$.

*Answer.* $W(0) = 1$; $W'(0^-) = 1$, $W'(0^+) = -1$. $\int_{-0.01}^{0.01}W''\,dy = W'(0.01) - W'(-0.01) = -e^{-0.01} - e^{-0.01} = -2e^{-0.01} = -1.980100$, close to $-2H = -2$, and closer still for a shorter interval. For the volume: $\sqrt{|g|}\,dy$ must equal $\sqrt{|g|_{x_8}}\,dx_8$, and $dy = \cot z\,dx_8$, so $\sqrt{|g|_{x_8}} = e^{6Hy}\cot z = \sin z\cot z = \cos z$, using $\sin z = e^{6Hy}$.

**Exercise 9.** For the CPL values $(w_0, w_a) = (-0.861, -0.60)$ compute $w$ at $a = 1$, $a = 1/2$ and $a \to 0$, and the scale factor at which $w = -1$. Is this thawing or freezing in the convention of Section 22.16? What does $w < -1$ require of a fluid with $\rho > 0$?

*Answer.* $w(1) = -0.861$; $w(1/2) = -0.861 - 0.60 \cdot 0.5 = -1.161$; $w(0) = -0.861 - 0.60 = -1.461$. $w = -1$ when $0.60(1 - a) = 0.139$, that is $1 - a = 0.231667$ and $a = 0.768$. Since $w_a < 0$ it is thawing in this convention ($w$ rises towards today from below). For $\rho > 0$, $w < -1$ means $\rho + p < 0$ (Section 22.16): the fluid violates the null energy condition. These are statements about the quoted fit; this book claims nothing about whether either field can produce them.

**Exercise 10.** From Out [17] check the first-order estimate $2.929$ of the breakdown rate, and compute how much larger the naive estimate is than the exact $A_{1/2}$ and than the first-order estimate.

*Answer.* The first-order estimate is the rate at which $(AQ_0)^2 = P_{sudden}$ with $Q_0 = 0.0934506$ and $P_{sudden} = 0.074906$: $A = \sqrt{0.074906}/0.0934506 = 0.273690/0.0934506 = 2.929$. The naive estimate $10.701$ is $10.701/1.508 = 7.10$ times the exact $A_{1/2}$ and $10.701/2.929 = 3.65$ times the first-order estimate. Comparing the dressing probability with the largest probability that can leave the level at all is what brings the estimate within a factor of two of the exact evolution.
