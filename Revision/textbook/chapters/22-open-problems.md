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
| 5. The dark-sector hypotheses | 22.16 to 22.24 | HYPOTHESIS, INVESTIGATED by the record and established in neither form; the observer's density ASSUMED; the remaining questions OPEN; Notebook 22b reproduces the record's numbers | Chapters 9, 12 and 15 |
| 6. Matter and antimatter | 22.25 | not solved by the theory as built; every scenario is a HYPOTHESIS | Chapter 21 |
| 7. Smaller open items | 22.26 | OPEN, CHOSEN or CONVENTION, as listed there | several chapters |

The problems are linked. The time-dependent problem (Problem 2) needs the history of $a_4$, which the back-reaction (Problem 3) would determine; both T2 and T3 of Chapters 18 and 19 rest on the Z2 brane (Problem 4); the dark-sector results of the record (Problem 5) are read on the prescribed history and rest on an ASSUMED observer density, and an equation of state that is a consequence of the coupled equations needs Problem 3 again; and a creation process (Problem 1) would need a dynamical geometry, which none of the equations of the record provides. A student is well advised to start with a problem whose first step is a finite calculation: Problem 2, whose first step this chapter carries out, or the first steps of Problems 3 and 4.

**The notebooks of this chapter.** Notebook 22a is the worked example of Problem 2. It reads the adiabaticity measure $Q$ of the 75 recorded ground states, shows that $Q$ grows exactly in proportion to the deflation rate, reproduces the record's $Q$ with the solver's shooting method written again in Python, collapses every slice and every momentum shell onto one curve with the exact rescaling identity, measures the jumps into the negative-energy branch, and solves the exact time evolution of one sector of the free field for deflation rates from $0.25$ to $251$. It draws eight figures, needs no Rust, and ends with the line ALL 20 CHECKS PASSED (notebook 22a). Notebook 22b is the worked example of Problem 5: it reads the committed outputs of the Revision dark-sector record, reproduces its key numbers (the observer identities on the computed history, the radiation-like Kohn-Sham gas, the dark-matter-like bulk band, the condensate, the mixtures and the models of dirac16complex00 against the observed values), each asserted against its record file and check, draws five figures, needs no Rust, and ends with the line ALL 27 CHECKS PASSED (notebook 22b).

**The status of every statement.** Every statement carries one of the five labels of Chapter 0: PROVED (exact, with the record file and check where the Revision record verifies it), COMPUTED (a number of a numerical computation, with its measured uncertainty and the file or notebook cell that holds it), ASSUMED (a starting point that is not derived), HYPOTHESIS (an idea that is stated and examined but not established) and OPEN (a question nobody has answered). Three special cases of ASSUMED, used as in Chapters 14 to 17, appear here as well: PRESCRIBED BACKGROUND (the history $a_4 = AHx_4$, given and not solved for), CHOSEN (a numerical or boundary choice, such as the tip of the hidden direction) and CONVENTION (a rule fixed by agreement, such as which levels count as particles). A few derivations of this chapter are the book's own and are not checked by a Revision verifier; each of them is written out line by line and says so.

**What this chapter does not do.** It does not solve any of the problems it lists. In particular, and in the words of the honesty rule: that the big bang creates universes in pairs is NOT proved, and no creation process, rate, amplitude or big-bang dynamics follows from the equations of the record (Section 22.4); the theory as built does NOT solve the matter-antimatter problem (Section 22.25); and the record's investigation of the dark-sector hypotheses establishes neither of them (Sections 22.16 to 22.24).

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

The orbitals are needed on the whole fine grid. The step ends are copied into the even columns. The midpoints are filled by **cubic Hermite interpolation**: the cubic polynomial with the values $f_0$, $f_1$ and the slopes $f_0'$, $f_1'$ at the two ends of a step of length $h$ has, in the middle, the value $(f_0 + f_1)/2 + h(f_0' - f_1')/8$ (Exercise 3 of Section 22.28 derives it); `a_e[:, :-1]` are the left ends of all steps and `a_e[:, 1:]` the right ends. This is what the Rust solver does. Finally each orbital is **normalised**: its norm $\sqrt{\int(a^2 + b^2)\,dy}$ is computed with Simpson's rule (`axis=1` sums along each row), and both components are divided by it, so that $\int(a^2 + b^2)\,dy = 1$.

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

**A first step.** (a) Redo the derivation above, and its Einstein-Gauss-Bonnet version from the general null combination of the record (`Revision/field_equations_a4/a4-equations.json`, key `generalSource.nullCombinations`). (b) Check the energy-exchange identity on the record's numbers (Exercise 7 of Section 22.28). (c) Write down a more general metric that keeps the symmetries of the author's metric (3-space isotropic, the three extra times isotropic) but lets the factors depend on $y$ and $x_4$, for example $ds^2 = e^{2\mathcal{A}(y, x_4)}(dx_1^2 + dx_2^2 + dx_3^2) - e^{2\mathcal{B}(y, x_4)}(dx_5^2 + dx_6^2 + dx_7^2) - e^{2\mathcal{C}(y, x_4)}dx_4^2 + dy^2$, which contains the author's metric as $\mathcal{A} = Hy + a_4$, $\mathcal{B} = Hy - a_4$, $\mathcal{C} = 0$ (this ansatz is a suggestion of this book, a HYPOTHESIS about a useful next step, not a result). Compute its Einstein tensor with two independent programs, as the record does for the author's metric, and find which conditions it puts on a source. (d) Only then ask whether a Kohn-Sham gas can satisfy them, starting with the free gas.

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

**The question.** The author's request contains two hypotheses, quoted from `Revision/README.md`: "Hypothesis: dirac16complex provides a possible physical mechanism for a time-varying dark energy equation of state and/or a possible physical mechanism for a time-varying dark matter equation of state, both of which you will investigate." and "Hypothesis00: dirac16complex00 provides [the same], both of which you will investigate." (the brackets are those of the README, which abridges the repeated sentence). The problem is to investigate them: compute the equation of state that an observer in 3-space would see as the extra times deflate and 3-space inflates, its change in time, and compare it with the observations. An answer is such a computation with its uncertainties, and an honest statement of what each field can and cannot produce.

**What is known now.** Status: both hypotheses have been INVESTIGATED by the Revision record, and neither is established. The investigation lives in two folders, `Revision/dark_sector/dirac16complex` (four scripts whose reports hold 30, 5, 13 and 9 checks, all PASS) and `Revision/dark_sector/dirac16complex00` (two independent implementations with 49 and 28 checks, all PASS), and it is written up in the registered document `Revision/docs/DARK_SECTOR_HYPOTHESES.md`. Sections 22.17 to 22.19 teach what the record finds, Notebook 22b (Section 22.20) reproduces its key numbers from the committed outputs, and Section 22.24 lists what remains open. The short answer, every item with the assumption it rests on:

1. The energy density $\rho_4$ that a 3-space observer assigns to 3-space is not fixed by the field equations; it is an ASSUMPTION, and the record states three definitions, called A, B and C (Section 22.17). Every verdict moves by exactly $-1$ between A and B on one side and C on the other.
2. dirac16complex, dark matter: a time-varying equation of state that falls from $1/3$ toward 0 (dark-matter-like) is present in the theory for quanta of the massive bulk band, but NOT in the computed Kohn-Sham ground states, whose gas is radiation-like under A and B (Section 22.18).
3. dirac16complex, dark energy: only under C, with $w_{\rm eff}$ between $-0.707107$ and $-0.671895$ and a slope of thawing sign far smaller than the observed one; nothing computed comes near the observed pair $(w_0, w_a) = (-0.861, -0.60)$, and no computed state crosses $w = -1$.
4. dirac16complex00, dark matter: a gas of positive-energy modes without extra-time momentum has the dark-matter-like law from $1/3$ to 0 under B (Section 22.19).
5. dirac16complex00, dark energy: only under C; the observed numbers are reproduced only by models whose parameters were CHOSEN to reproduce them, and a crossing of $w = -1$ only with a ghost-like component of negative energy.
6. On the prescribed history $a_4 = AHx_4$ the observer's expansion itself reads $w = -1$ exactly, with no time variation (Section 22.17).

In the words of the record: it "establishes neither Hypothesis nor Hypothesis00". Both remain HYPOTHESES.

**The observed numbers.** They come from a private document of the author, and the book quotes them only as `Revision/README.md` states them: the parametrisation $w(a) = w_0 + w_a(1 - a)$ (CPL, after Chevallier, Polarski and Linder), the constant-$w$ fit $w = -0.764$, and $(w_0, w_a) = (-0.861, -0.60)$; in this convention thawing means $w_a < 0$. The record calls them the **Unite values**. In that document $H$ is the Hubble rate and $a$ the scale factor of the observed universe; they are not the $H$ and $a_4$ of the author's metric.

**What the CPL numbers say, line by line.**

$$
w(1) = w_0 + w_a \cdot 0 = w_0 = -0.861 .
$$

Rule: today the scale factor is $a = 1$, so $1 - a = 0$.

$$
w(0) = w_0 + w_a = -0.861 - 0.60 = -1.461 .
$$

Rule: in the far past $a \to 0$, so $1 - a \to 1$.

$$
w_0 + w_a(1 - a) = -1 \quad\Longleftrightarrow\quad 1 - a = \frac{-1 - w_0}{w_a} = \frac{-0.139}{-0.60} = 0.231667 \quad\Longleftrightarrow\quad a = 0.768333 = \frac{461}{600} .
$$

Rule: subtract $w_0$ from both sides and divide by $w_a$; then subtract from 1 ($0.231667 = 139/600$). The record checks this crossing exactly (`Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json`, check `unite_crossing_point`).

So the fitted $w$ falls below $-1$ for $a < 461/600$. What that requires:

$$
w < -1, \ \rho > 0 \quad\Longleftrightarrow\quad p < -\rho \quad\Longleftrightarrow\quad \rho + p < 0 .
$$

Rule: multiply $w = p/\rho < -1$ by the positive number $\rho$ (the direction of an inequality is kept), then add $\rho$ to both sides.

A fluid of positive energy density with $w < -1$ (called **phantom**) violates the null energy condition. Section 22.19 shows what in this theory can produce such a reading, and at what price.

### 22.17 The observer's density and the equation of state, line by line

**Why an assumption is needed.** The observations are made in four dimensions, three of space and one of time; the theory lives in eight. An observer who sees only $x_1, x_2, x_3$ and the time $x_4$ must turn the energy of a state, which is spread over all seven other directions, into an energy per unit volume of 3-space. Over the hidden direction $x_8$ the record averages with the weight $\sqrt{|g|} = \cos z$, which does not depend on $x_4$ (check `observer_hidden_average_commutes` of `python-derive-eos.json`). Over the three extra times there is no unique choice, because they are time-like: an observer does not move through them as through a space direction. The record therefore states three definitions and decides between none of them.

**The proper 7-volume does not change, line by line.** The proper length of a step $dx$ along a direction is $\sqrt{|g_{xx}|}\,dx$; the proper volume of a small box is the product of the proper lengths of its sides.

$$
\big(e^{a_4}\sin^{1/6}z\big)^3 = e^{3a_4}\sin^{1/2}z .
$$

Rule: the three directions $x_1, x_2, x_3$ each have the factor $e^{a_4}\sin^{1/6}z$; a product of three equal factors is the third power, and $3 \cdot \frac16 = \frac12$. This is the proper 3-volume per unit coordinate volume: it inflates like $e^{3a_4}$.

$$
\big(e^{-a_4}\sin^{1/6}z\big)^3 = e^{-3a_4}\sin^{1/2}z .
$$

Rule: the same for the three extra times, whose factor is $e^{-a_4}\sin^{1/6}z$. The proper extra-time volume deflates like $e^{-3a_4}$.

$$
e^{3a_4}\sin^{1/2}z \cdot e^{-3a_4}\sin^{1/2}z \cdot \cot z = \sin z\cot z = \cos z .
$$

Rule: multiply by the factor $\sqrt{g_{88}} = \cot z$ of the hidden direction; $e^{3a_4}e^{-3a_4} = e^0 = 1$, $\sin^{1/2}z\sin^{1/2}z = \sin z$, and $\sin z \cdot \cos z/\sin z = \cos z$. The proper 7-volume element of a slice $x_4 = $ const is $\cos z$: the inflation of 3-space is compensated exactly by the deflation of the extra times (`Revision/dark_sector/dirac16complex/reports/derivation-checks.json`, checks `proper_3_and_extra_time_volume_scalings` and `proper_7_volume_element_independent_of_a4`).

**The energy balance, line by line.** Let $E$ be the energy of a state, the proper 7-volume integral of the energy density $\rho$, and $P_3$, $P_t$, $P_8$ the integrals of the pressures of 3-space, of the extra times and of the hidden direction. The record re-derives the conservation law $\nabla_\mu T^\mu{}_\nu = 0$ from the author's metric for a diagonal energy-momentum tensor that depends on $x_4$ and $x_8$; its $x_4$ component reads (checks `conservation_x4_identity` and `conservation_x4_author_metric`)

$$
\frac{\partial\rho}{\partial x_4} = -3a_4'\,(p_3 - p_t) .
$$

$$
\frac{dE}{dx_4} = \int\cos z\,\frac{\partial\rho}{\partial x_4} = -3a_4'\int\cos z\,(p_3 - p_t) = -3a_4'\,(P_3 - P_t) .
$$

Rule: integrate over a slice with the weight $\cos z$; because the weight does not depend on $x_4$, the derivative can be taken outside the integral; $a_4'$ does not depend on the position and comes out of the integral.

$$
\frac{dE}{da_4} = \frac{dE/dx_4}{da_4/dx_4} = -3\,(P_3 - P_t) = -3X, \qquad X = P_3 - P_t .
$$

Rule: the chain rule, $dE/dx_4 = (dE/da_4)(da_4/dx_4)$, divided by $a_4' = da_4/dx_4$ (check `integrated_identity_dE_da4`). So the energy of a state changes as 3-space inflates exactly by the difference of the two pressures: positive pressure in 3-space takes energy away, as for a gas in an expanding box, and negative pressure along the extra times does the same.

**The three definitions.** They differ in how the extra times are counted:

- **(A)** the extra times are compact, with a fixed coordinate period (closed time-like directions): $\rho_4 = E/(\text{proper 3-volume}) \propto E\,e^{-3a_4}$;
- **(B)** the extra times are not compact, and $\rho_4$ is taken per unit extra-time COORDINATE volume: again $\rho_4 \propto E\,e^{-3a_4}$;
- **(C)** $\rho_4$ is taken per unit PROPER 7-volume (equivalently per unit proper extra-time volume): $\rho_4 \propto E$.

All three are written as $\rho_4 \propto E\,e^{-3(1-s)a_4}$, with $s = 0$ for A and B and $s = 1$ for C. Status: ASSUMPTION. Which of them, if any, describes a physical observer is OPEN (Section 22.24). The record for dirac16complex00 calls the same two scalings N1 (the scaling of A and B) and N2 (that of C).

**The equation of state read from a dilution.** For a 4-dimensional observer a fluid with a constant equation of state $w$ thins out as $\rho \propto a^{-3(1+w)}$ (radiation, $w = 1/3$, as $a^{-4}$; dust, $w = 0$, as $a^{-3}$; a cosmological constant, $w = -1$, not at all). Turned around, this defines the equation of state that the observer infers from any dilution:

$$
\ln\rho = -3(1 + w)\ln a + \text{const} \quad\Longrightarrow\quad \frac{d\ln\rho}{d\ln a} = -3(1 + w) \quad\Longrightarrow\quad w = -1 - \frac13\,\frac{d\ln\rho}{d\ln a} .
$$

Rule: take the logarithm of $\rho = c\,a^{-3(1+w)}$ (the logarithm of a product is the sum of the logarithms, and $\ln a^n = n\ln a$), differentiate with respect to $\ln a$, then divide by $-3$ and subtract 1. Applied to $\rho_4$ it defines $w_{\rm eff} = -1 - \frac13\,d\ln\rho_4/d\ln a$.

**The observer identities, line by line.** The observer's scale factor is $a = e^{a_4 - a_{4,\rm today}}$ (normalised to $a = 1$ at a chosen today, a free parameter).

$$
\ln a = a_4 - a_{4,\rm today} \quad\Longrightarrow\quad d\ln a = da_4 .
$$

Rule: the logarithm undoes the exponential; $a_{4,\rm today}$ is a constant.

$$
\ln\rho_4 = \text{const} + \ln E - 3(1 - s)a_4 .
$$

Rule: the logarithm of $c\,E\,e^{-3(1-s)a_4}$.

$$
\frac{d\ln\rho_4}{d\ln a} = \frac{1}{E}\frac{dE}{da_4} - 3(1 - s) = -\frac{3X}{E} - 3 + 3s .
$$

Rule: differentiate with respect to $a_4$ (which is $\ln a$ up to a constant); $d\ln E/da_4 = (dE/da_4)/E$, and the energy balance $dE/da_4 = -3X$.

$$
w_{\rm eff} = -1 - \frac13\Big(-\frac{3X}{E} - 3 + 3s\Big) = -1 + \frac{X}{E} + 1 - s = \frac{X}{E} - s .
$$

Rule: insert into the definition of $w_{\rm eff}$ and multiply out.

$$
w_{\rm eff}(A) = w_{\rm eff}(B) = \frac{X}{E}, \qquad w_{\rm eff}(C) = \frac{X}{E} - 1 .
$$

Rule: $s = 0$ for A and B, $s = 1$ for C. These are exact (checks `w_eff_A_equals_X_over_E`, `w_eff_B_equals_w_eff_A`, `w_eff_C_equals_X_over_E_minus_1` and `w_eff_general_normaliser` of `derivation-checks.json`; for dirac16complex00, `observer_N1_weff_identity` and `observer_N2_weff_identity` of `python-derive-eos.json`). Notebook 22b tests them on the computed Kohn-Sham history (In [3]).

**How every verdict depends on the assumption.** The same state reads differently under each definition (the rows are records of `Revision/docs/DARK_SECTOR_HYPOTHESES.md`, section 3.2, derived in Sections 22.18 and 22.19):

| state | $w_{\rm eff}$ under A, B | $w_{\rm eff}$ under C | ratio $p_3/\rho$ |
| --- | --- | --- | --- |
| homogeneous condensate | 0, dust-like | $-1$, cosmological-constant-like | $\lambda S/(2m + \lambda S)$, constant |
| massless quanta | $1/3$, radiation | $-2/3$ | $1/3$ |
| massive quanta, flat limit | $1/3 \to 0$ | $-2/3 \to -1$ | as under A, B |
| Kohn-Sham gas, $N = 688$, $\lambda = 0$ | 0.2929 to 0.3183 | $-0.7071$ to $-0.6817$ | 0.2929 to 0.3183 |

The ratio $p_3/\rho$, the 8-dimensional equation of state, does not depend on the normalisation at all. INTERPRETATION (labelled, as in the record): supernova distances measure the dilution-inferred $w_{\rm eff}$ of a 4-dimensional observer, which agrees with the ratio only when no energy is exchanged with the extra times.

**The expansion seen by the observer.** An observer who reads the scale factor $a = e^{a_4}$ and the time $t = x_4$ and uses the 4-dimensional Friedmann equations infers $w_{\rm exp} = -1 - \frac23\,a_4''/(a_4')^2$ (check `expansion_inferred_w`). On the history $a_4 = AHx_4$ of the Kohn-Sham record, $a_4' = AH$ is constant and $a_4'' = 0$, so $w_{\rm exp} = -1$ exactly: the expansion itself has no time-varying equation of state. This is also the only history that a condensate allows as a source (Section 22.14: the linear member needs $p_3 = p_t$).

**When is a reading phantom?**

$$
w_{\rm eff}(C) < -1 \quad\Longleftrightarrow\quad \frac{X}{E} - 1 < -1 \quad\Longleftrightarrow\quad \frac{X}{E} < 0 .
$$

Rule: add 1 to both sides. With $E > 0$ this needs $X < 0$, that is $P_t > P_3$: a pressure along the extra times larger than the pressure of 3-space; otherwise it needs $E < 0$, a state of negative energy. Under A and B the same condition gives $w_{\rm eff} < 0$ (check `phantom_condition`). For a single plane-wave mode of real frequency the record proves $X \ge 0$ (check `flat_mode_X_nonnegative`): its 3-space pressure is $\ge 0$ and its extra-time pressure $\le 0$, so both make $X$ larger, not smaller.

### 22.18 dirac16complex: the Kohn-Sham gas, the bulk band, the condensate and the mixtures

**The Kohn-Sham history.** The record runs the Revision Rust Kohn-Sham solver of Chapter 15 at the 41 slices $a_{4,0} = 0, 0.05, \dots, 2$ for $N = 8$, 136 and 688 quanta and the five couplings $\lambda = 0, \pm\lambda_1, \pm\lambda_2$: 615 runs, with $H = m = 1$, $L = 3$, the tip angle $\theta = 0$ and temperature $T = 0$ (`Revision/dark_sector/dirac16complex/reports/ks-history-run.json`, 5 checks). It reproduces the 75 committed states of Chapter 15 with relative deviation 0 (check `committed_slices_reproduced`), and the occupied levels are the same at all 41 slices of every series (check `occupied_labels_fixed_along_history`), so the instantaneous ground states are the adiabatically continued states. The history is a PRESCRIBED BACKGROUND: the gas is a test field without back-reaction (Section 22.14). The record's script `compute_eos.py` evaluates $w_{\rm eff}$ for the three definitions, the tangents, the fits, the condensate and the mixtures (13 checks), and an independent second computation, `independent_free_gas.py` (Chebyshev collocation, no solver output used except for the final comparison), reproduces the solver's energies over 82 states to $1.897 \times 10^{-12}$ and $w_{\rm eff} = X/E$ to $1.492 \times 10^{-12}$ (9 checks).

**The gas is radiation-like.** The occupied levels lie on the brane band, which is massless at zero 3-momentum (the brane zero mode, slope $c\,e^{-a_4}$ with $c = 1.9051482536$ at small $k$; check `brane_band_slope`). So the gas redshifts like radiation: $d\ln E/da_4$ goes from $-0.8787$ at $a_4 = 0$ to $-0.9549$ at $a_4 = 2$ for $N = 688$, $\lambda = 0$, toward the radiation value $-1$. Over all series with $N = 136$ and 688, $X/E$ lies between 0.292893 and 0.328105 and rises monotonically toward $1/3$ (checks `gas_radiation_like_band` and `gas_X_over_E_rises_toward_one_third` of `eos-checks.json`; Notebook 22b, In [3] and Figure 22b.1). For $N = 688$, $\lambda = 0$: $w_{\rm eff}(A) = w_{\rm eff}(B)$ goes from 0.2929 to 0.3183 and $w_{\rm eff}(C)$ from $-0.7071$ to $-0.6817$. The pressure of the hidden direction gives $P_8/E$ from 0.3535 to 0.6482: a pressure, but not one that the 3-space observer sees as pressure.

**The CPL tangents of the gas.** With $a = e^{a_4 - a_{4,\rm today}}$, $da = a\,da_4$, so at $a = 1$ the slope $dw/da$ equals $dw/da_4$ and the tangent is $w_0 = w_{\rm eff}$ at $a_{4,\rm today}$, $w_a = -dw_{\rm eff}/da_4$ there. For $N = 688$, $\lambda = 0$ (`Revision/dark_sector/dirac16complex/outputs/eos-summary.json`; Notebook 22b, Out [4]):

| $a_{4,\rm today}$ | 0.5 | 1 | 1.5 | 2 |
| --- | --- | --- | --- | --- |
| $w_0$ under C | $-0.7037$ | $-0.6982$ | $-0.6907$ | $-0.6817$ |
| $w_a$ (every definition) | $-0.00905$ | $-0.01292$ | $-0.01701$ | $-0.01775$ |

($w_0$ under A and B is the value under C plus 1; $w_a$ is the same in every definition, because the definitions differ by the constant $s$.) Over all series with $N = 136$ and 688 the tangent $w_a$ lies between $-0.020523$ and $-0.008894$, the least-squares fits give $w_a$ between $-0.030371$ and $-0.018132$, and $w_{\rm eff}(C)$ lies between $-0.707107$ and $-0.671895$ (check `gas_cpl_thawing_sign_small`). The sign is that of thawing; the size is smaller than the observed 0.60 by a factor of about 20 or more. For $N = 8$ with $\lambda \ne 0$ only the brane zero modes are occupied: $E$ is constant and $P_3 = P_t$, so $w_{\rm eff}(A) = 0$ and $w_{\rm eff}(C) = -1$, constant, with $E < 0$ for $\lambda > 0$ (check `n8_interacting_zero_modes_constant`); for $N = 8$ with $\lambda = 0$, $E = 0$ and there is no equation of state.

**The dark-matter-like law, line by line.** In the flat limit (no warp) a quantum of mass $M$ and fixed coordinate momentum $k$ has the physical momentum $k/a$ and the energy $\omega = \sqrt{M^2 + k^2/a^2}$, with $a = e^{a_4}$. With the number of quanta fixed, $E \propto \omega$, and the energy balance gives $X/E = -\frac13\,d\ln E/da_4$.

$$
\ln\omega = \tfrac12\ln\big(M^2 + k^2e^{-2a_4}\big) .
$$

Rule: $\ln\sqrt{x} = \frac12\ln x$, and $1/a^2 = e^{-2a_4}$.

$$
\frac{d\ln\omega}{da_4} = \frac12\cdot\frac{-2k^2e^{-2a_4}}{M^2 + k^2e^{-2a_4}} = -\frac{k^2}{M^2a^2 + k^2} .
$$

Rule: the chain rule, $d\ln f/da_4 = f'/f$, with $d(e^{-2a_4})/da_4 = -2e^{-2a_4}$; then multiply numerator and denominator by $a^2 = e^{2a_4}$.

$$
w_{\rm eff}(A) = \frac{X}{E} = \frac{k^2}{3\,(M^2a^2 + k^2)} .
$$

Rule: multiply by $-\frac13$. For $a \to 0$ the momentum term dominates and $w_{\rm eff} \to 1/3$ (radiation); for $a \to \infty$ the mass dominates and $w_{\rm eff} \to 0$ (dust): a time-varying, dark-matter-like equation of state (check `massive_mode_w_eff_law`; for $M = 0$ it is $1/3$ at every time, check `massless_mode_w_eff`). In the author's metric the record finds this law for the massive **bulk band** (odd brane parity; its edge at zero momentum is $\varepsilon(0) = 1.292292828069$): the lowest odd-parity level of the shell $n_2 = 1$ has $w_{\rm eff}(A)$ falling monotonically from 0.239626 at $a_4 = -3$ to $2.268 \times 10^{-3}$ at $a_4 = 4$, while the brane-band level of the same shell stays between 0.291594 and 0.333275, tending to $1/3$ (`Revision/dark_sector/dirac16complex/reports/independent-checks.json`, checks `bulk_band_dark_matter_law` and `brane_band_radiation_law`; Notebook 22b, In [5] and Figure 22b.2). At late times the bulk level falls like $1/a$ rather than like $1/a^2$: the ratio $w(4)/w(3.75) = 0.765177$ is close to $e^{-0.25} = 0.778801$, which the record reads as a term of $\varepsilon(k)$ linear in small $k$. The computed ground states ($N \le 688$, $T = 0$) are filled below the bulk edge and do not populate the bulk band. COMPUTED; that such quanta are present in the universe is not established.

**The condensate, line by line.** A homogeneous condensate is an exact solution of both fields, with $S = \bar\Psi\Psi$ constant (Chapter 9), and

$$
\rho = mS + \tfrac{\lambda}{2}S^2, \qquad p_3 = p_t = p_8 = \tfrac{\lambda}{2}S^2
$$

(checks `condensate_rho_p` and `condensate_satisfies_both_identities` of `derivation-checks.json`).

$$
X = P_3 - P_t = 0 \quad\Longrightarrow\quad w_{\rm eff}(A) = w_{\rm eff}(B) = 0, \qquad w_{\rm eff}(C) = -1 .
$$

Rule: equal pressures give $X = 0$; insert into the observer identities. The condensate is dust-like under A and B and cosmological-constant-like under C, constant in time in both (check `condensate_w_eff`).

$$
\frac{p}{\rho} = \frac{\frac{\lambda}{2}S^2}{mS + \frac{\lambda}{2}S^2} = \frac{\lambda S/m}{2 + \lambda S/m} = \frac{u}{2 + u}, \qquad u = \frac{\lambda S}{m} .
$$

Rule: divide numerator and denominator by $mS/2$. The ratio is constant (check `condensate_ratio_w`).

$$
\frac{u}{2 + u} = -0.764 \ \Longrightarrow\ u = -0.764\,(2 + u) \ \Longrightarrow\ 1.764\,u = -1.528 ,
$$

$$
u = -\frac{1.528}{1.764} = -\frac{382}{441} = -0.866213151927 .
$$

Rule: multiply by $2 + u$, bring $-0.764u$ to the left, divide by 1.764; $1528/1764$ reduces by 4 to $382/441$. Then $\rho/(mS) = 1 + u/2 = 250/441 = 0.566893424036$, so $\rho > 0$ exactly when $mS > 0$ (check `condensate_ratio_equal_unite_constant_w`; Notebook 22b, In [6]). This value of $u$ is CHOSEN to give $-0.764$: one parameter tuned to one number, and it is the 8-dimensional ratio, not the observer's $w_{\rm eff}$, which is 0 or $-1$.

$$
\frac{u}{2 + u} < -1 \quad\Longleftrightarrow\quad -2 < u < -1 .
$$

Rule: if $2 + u > 0$, multiply by it: $u < -2 - u$, so $u < -1$, and with $u > -2$ the window $-2 < u < -1$; if $2 + u < 0$, multiplying reverses the inequality: $u > -2 - u$, so $u > -1$, which contradicts $u < -2$. The ratio is phantom exactly in this window (`python-derive-eos.json`, check `condensate_phantom_interval`; Figure 22b.3), and the CHOSEN $u = -0.866$ lies outside it.

**Mixtures with a condensate, line by line.** Take a radiation-like gas, $X_g = E_g/3$, so that $dE_g/da_4 = -E_g$ and $E_g \propto e^{-a_4} \propto 1/a$, and add a condensate with $X_c = 0$ and $E_c$ constant. Let $r = E_g/E_c = r_0/a$, with $r_0$ its value today.

$$
w_{\rm eff}(A) = \frac{X_g + X_c}{E_g + E_c} = \frac{E_g/3}{E_g + E_c} = \frac13\,\frac{r}{1 + r} .
$$

Rule: the observer identity for the whole mixture; divide numerator and denominator by $E_c$.

$$
\frac{dw}{da} = \frac13\,\frac{1}{(1 + r)^2}\,\frac{dr}{da} = -\frac13\,\frac{r_0}{a^2(1 + r)^2} \quad\Longrightarrow\quad w_0 = \frac{r_0}{3(1 + r_0)}, \qquad w_a = \frac{r_0}{3(1 + r_0)^2} > 0 .
$$

Rule: the quotient rule gives $d(r/(1+r))/dr = 1/(1+r)^2$, and $dr/da = -r_0/a^2$; at $a = 1$, $r = r_0$, and $w_a = -dw/da$. The mixture is **freezing**: as the gas redshifts, $w$ moves toward the condensate's value (check `mixture_radiation_condensate_cpl`). The same holds under C, with $w_0$ lowered by 1.

$$
\frac{r_0}{3(1 + r_0)} - 1 = -0.861 \ \Longrightarrow\ r_0 = 0.417\,(1 + r_0) \ \Longrightarrow\ r_0 = \frac{417}{583} = 0.715266 ,
$$

$$
w_a = \frac{r_0}{3(1 + r_0)^2} = \frac{0.139}{1 + r_0} = 0.081037 .
$$

Rule: add 1 and multiply by 3 ($3 \cdot 0.139 = 0.417$); collect $r_0$; for $w_a$ use $r_0/(3(1 + r_0)) = 0.139$, and $0.139 \cdot 583/1000 = 0.081037$. So $r_0$ is CHOSEN for $w_0 = -0.861$, and the slope then has the wrong sign: $+0.081037$, not $-0.60$ (check `mixture_C_matching_w0_unite`). With the computed gas $N = 688$, $\lambda = 0$ and today at $a_{4,\rm today} = 2$, under C (`eos-checks.json`; Notebook 22b, In [7] and Figure 22b.4):

- the gas share 0.436703 is CHOSEN so that $w_{\rm eff}(C) = -0.861$ today; then $w_a = 0.067014 > 0$, freezing (check `mixture_C_w0_unite_has_positive_wa`);
- the gas share 0.6807148417136 is CHOSEN so that the constant-$w$ proxy over $1/3 \le a \le 1$ equals $-0.764$; the CPL fit of that mixture is $(w_0, w_a) = (-0.7841, 0.0603)$, opposite in the sign of $w_a$ to the observed fit (check `mixture_C_constant_w_unite_reachable_only_with_freezing_cpl`);
- in the ratio definition, with a condensate of any constant ratio between $-3$ and 1, any gas share and $a_{4,\rm today} \in \{0.5, 1, 1.5, 2\}$, no mixture comes closer to the observed pair than 0.600001 (check `ratio_mixture_scan_cannot_reach_unite_wa`).

**Phantom and the crossing of $-1$.** No computed state of dirac16complex crosses $w = -1$: every computed state has $X \ge 0$ and $E > 0$, except the $N = 8$, $\lambda > 0$ states, which have $E < 0$ and $X = 0$ exactly. Modes of dirac16complex with extra-time momentum lie outside the good sector and are OPEN.

### 22.19 dirac16complex00: modes of both energy signs, the populations and the models M1 to M5

**Modes and their energies.** dirac16complex00 is a classical field of 16 commuting complex components. A plane wave $\Phi = u\,e^{i(kx_1 + qx_5 - \omega x_4)}$ with 3-momentum $k$ and extra-time momentum $q$ (physical momenta in a frozen local frame) obeys $\omega u = hu$ with $h^2 = (m^2 + k^2 - q^2)\,I_{16}$, so

$$
\omega^2 = m^2 + k^2 - q^2
$$

(check `mode_dispersion_h_squared`): the extra times are time-like, and $q$ enters with the opposite sign to $k$. The conserved charge is the Krein form $Q = \Phi^\dagger B\Phi$ of Chapter 10 (check `mode_generator_B_selfadjoint`). For the three test cases $(m, k, q) = (3, 4, 0)$, $(5, 0, 3)$ and $(4, 4, 4)$, with $\omega = \pm5, \pm4, \pm4$, every real-frequency eigenspace has dimension 8 and a Krein form of signature (4,4), and on it $\rho = \omega Q$ exactly (checks `mode_krein_inertia_*` and `mode_emt_*`; the second implementation finds $\rho = +1.25$ and $-1.25$ at $\omega = 1.25$ for $Q = +1$ and $-1$, check `B_krein_signed_energy`). So at every real frequency there are modes of BOTH energy signs: the classical energy of this field is unbounded below. A component of negative classical energy is called **ghost-like**; it is not an established physical state.

**Growing modes.** For $q^2 > m^2 + k^2$ the frequency is imaginary and the mode grows (Chapter 8). In the deflating field the physical extra-time momentum is $qa$, which grows with $a$, so every mode with $q \ne 0$ reaches a **turning point** $a_{\rm turn}$, where $\omega = 0$, and grows after it: the deflation drives the growth. The field-equation implementation B measures, past the turning point $a_{\rm turn} = 1.8433886$, the growth rate 0.54337468 against the adiabatic estimate 0.55114035 (check `B_growth_rate`).

**The adiabatic gas, line by line.** In the deflating local model (the warp frozen at one hidden position: an APPROXIMATION) a mode has $\omega^2 = m^2 + k^2/a^2 - q^2a^2$, its Krein charge is an adiabatic invariant, and its energy density is $\rho_i = \omega_iQ_i \propto \omega_i$. Under B the observer identity gives $w_{\rm eff}(B) = -\frac13\,d\ln\rho_i/d\ln a = -\frac13\,d\ln\omega_i/d\ln a$.

$$
\ln\omega = \tfrac12\ln\big(m^2 + k^2a^{-2} - q^2a^2\big), \qquad \frac{d\ln\omega}{d\ln a} = \frac{-k^2a^{-2} - q^2a^2}{\omega^2} .
$$

Rule: as in Section 22.18, with $d(a^{-2})/d\ln a = -2a^{-2}$ and $d(a^2)/d\ln a = 2a^2$; the factor $\frac12$ cancels the factors 2.

$$
\varepsilon_i = w_{\rm eff}(B)_i = \frac{k^2/a^2 + q^2a^2}{3\,\omega_i^2} \ \ge\ 0 .
$$

Rule: multiply by $-\frac13$; both terms of the numerator are $\ge 0$, and $\omega^2 > 0$ for a real frequency. The extra-time momentum RAISES $\varepsilon$: its pressure is negative, which increases $X$ (checks `wkb_mode_gas_conservation`, `wkb_epsilon_sign_free`). For a mixture of components (check `mixture_weighted_average`):

$$
w_{\rm eff}(B) = \frac{\sum_i\varepsilon_i\rho_i}{\sum_i\rho_i}, \qquad w_{\rm eff}(C) = \frac{\sum_i\varepsilon_i\rho_i}{\sum_i\rho_i} - 1 .
$$

**No crossing without a ghost.** If every $\rho_i \ge 0$, the first fraction is an average of numbers $\varepsilon_i \ge 0$ with weights $\rho_i \ge 0$, so it is $\ge 0$: $w_{\rm eff}(B) \ge 0$ and $w_{\rm eff}(C) \ge -1$ at every $a$. A crossing of $-1$ needs the numerator to change sign, that is a component with $\rho_i < 0$: negative classical energy, a ghost-like component. PROVED within the adiabatic model (`Revision/dark_sector/dirac16complex00/eos-theory.json`, key `wkb.theorem`). The only phantom value without negative energy is the constant ratio of a condensate with $-2 < u < -1$ (Section 22.18), which is not the observer's $w_{\rm eff}$.

**The models.** Each model is normalised to total energy density 1 at $a = 1$ and read under C unless stated. The parameters marked CHOSEN were fixed so that the model reproduces an observed number; that number is then an input, NOT an output (`eos-theory.json`, key `models`):

| model | content | CHOSEN parameters |
| --- | --- | --- |
| M1 | condensate, an exact solution | $u = \lambda S/m$; the ratio is $-0.764$ at $u = -382/441$ (CHOSEN) |
| M2 | positive-energy gas with $q = 0$ | $k^2/(k^2 + m^2) = 417/1000$ at $a = 1$, CHOSEN for $w_0 = -0.861$ |
| M3 | one positive-energy extra-time mode, $k = 0$ | $s = q^2/m^2 = 417/1417$, CHOSEN for $w_0 = -0.861$ |
| M4 | condensate plus a positive extra-time mode | $s = 264037/403037$ and the mode share $\Omega_q = 57963/264037$, both CHOSEN so that the tangent is $(-0.861, -0.60)$ |
| M5 | as M4 plus a GHOST-LIKE part: massless modes of negative energy $-G/a$ | $G = 3/10$ (a stated choice); $s$ and $\Omega_q$ CHOSEN so that the fit over $1/2 \le a \le 1$ is $(-0.861, -0.60)$ |

M2 line by line, with $r = k^2/m^2$ and $q = 0$: $\varepsilon = (r/a^2)/(3(1 + r/a^2)) = r/(3(r + a^2))$; at $a = 1$ this is $\frac13\,r/(1 + r) = \frac13\,k^2/(k^2 + m^2)$, and setting it to $0.139$ (so that $w_{\rm eff}(C) = -0.861$) gives $k^2/(k^2 + m^2) = 0.417$. Its derivative is $dw/da = -\frac23\,ra/(r + a^2)^2$, so $w_a = \frac23\,r/(1 + r)^2 = \frac23 \cdot 0.417 \cdot 0.583 = 0.162074$ (using $r/(1 + r) = 0.417$ and $1/(1 + r) = 0.583$): freezing (check `M2_tangent_exact`). Under B the same model has $w_{\rm eff} = \frac13\,k^2/(k^2 + m^2a^2)$, from $1/3$ to 0: the dark-matter-like law of dirac16complex00. M3 with $k = 0$: $w_{\rm eff}(C) = -1 + \frac13\,sa^2/(1 - sa^2) \ge -1$; at $a = 1$, $s/(1 - s) = 0.417$ gives $s = 417/1417$, and $w_a = -\frac23\,s/(1 - s)^2 = -0.393926$: thawing; the turning point is at $a_{\rm turn} = 1/\sqrt{s} = 1.8434$ (check `M3_tangent_exact`).

The resulting CPL numbers under C (tangent; least-squares fit over $1/2 \le a \le 1$; the constant-$w$ proxy, the mean of $w(a)$ over that range; records `M2_tangent_exact` to `M5_without_ghost_no_crossing` of `python-derive-eos.json`; Notebook 22b, In [8] and Figure 22b.5):

| model | tangent $w_0$ | tangent $w_a$ | fit $w_0$ | fit $w_a$ | proxy | crosses $-1$? |
| --- | --- | --- | --- | --- | --- | --- |
| M1 | $-1$ | 0 | $-1$ | 0 | $-1$ | no |
| M2 | $-0.861$ | $+0.162074$ | $-0.8655$ | 0.2173 | $-0.8112$ | no |
| M3 | $-0.861$ | $-0.393926$ | $-0.8734$ | $-0.2196$ | $-0.9283$ | no |
| M4 | $-0.861$ | $-0.600$ | $-0.8832$ | $-0.2203$ | $-0.9383$ | no |
| M5 | $-0.8396$ | $-1.0399$ | $-0.861$ | $-0.600$ | $-1.011$ | at $a = 0.7791$ |

- M4: $s = 0.6551$, $\Omega_q = 0.2195$. Its $w$ never crosses $-1$: the smallest $w_{\rm eff}(C)$ over $a = 1/300, \dots, 1$ is $-0.999999214228$ (check `M4_never_phantom`). The phantom past $w_0 + w_a = -1.461$ belongs to the straight CPL line, not to the model. Its extra-time mode reaches its turning point at $a_{\rm turn} = 1.2355$ and then grows without bound. Under B or in the ratio, M4 is not dark energy ($w \ge 0$).
- M5: $s = 0.5678$, $\Omega_q = 0.5947$, condensate share $0.7053$; its $w$ crosses $-1$ at $a = 0.7791$ (the observed line at 0.7683), and without its ghost-like part it does not cross at all (checks `M5_crosses_minus_1`, `M5_without_ghost_no_crossing`). INTERPRETATION, as in the record: because $s$ and $\Omega_q$ were chosen so that the fit equals the observed line, a crossing close to the line's crossing is expected and is not an independent agreement.
- Implementation B rebuilds M2 to M5 from solutions of the full 16-component field equation with the author's gammas and agrees with A to within 0.00083082726 in every tangent, fit and proxy; it finds the M5 crossing at $a = 0.77905405$ (check `B_vs_A_M5_crossing` of `python-independent-numerics.json`).

**The constant-$w$ proxy is not the supernova fit.** Applied to the observed CPL line itself, the mean of $w(a)$ is $-1.011$ over $1/2 \le a \le 1$ and $-1.061$ over $1/3 \le a \le 1$ (check `unite_line_fit_proxy`), not $-0.764$: the supernova constant-$w$ fit weights the data, which no part of the record computes.

**The comparison with the observed values.** Every match is labelled with the number of parameters CHOSEN for it:

| observed value | dirac16complex | dirac16complex00 | by construction? |
| --- | --- | --- | --- |
| constant $w = -0.764$ | condensate ratio at $u = -382/441$; mixture under C with gas share 0.6807 (proxy; slope $+0.0603$) | condensate ratio at $u = -382/441$, $\lambda < 0$ | yes: one parameter for one number |
| $w_0 = -0.861$ | mixture under C with gas share 0.436703: $w_a = 0.067014$, freezing | M2 ($w_a = +0.162074$), M3 ($w_a = -0.393926$) | yes: one parameter for one number |
| $(w_0, w_a) = (-0.861, -0.60)$ | not reached: gas $\lvert w_a\rvert \le 0.030371$; ratio mixtures never closer than 0.600001 | M4 tangent exactly; M5 fit exactly | yes: two parameters for two numbers |
| crossing of $-1$ at $a = 0.7683$ | no crossing in any computed state | only M5, with a ghost-like part: $a = 0.7791$ | the fit by construction; the ghost share a stated choice |

A model with as many tuned parameters as matched numbers reproduces them by construction and is NOT a prediction. Nothing in the record selects the populations of M2 to M5, the mixture shares or the condensate's $u$. What is NOT tuned are the signs and the ranges: for positive-energy content $w_{\rm eff}(C) \ge -1$; every computed state of dirac16complex has $X \ge 0$; the computed gas has the thawing sign with $\lvert w_a\rvert \le 0.030371$; gas-condensate mixtures are freezing; M4, tuned to the observed tangent, never crosses $-1$.

### 22.20 Example: the dark-sector numbers, reproduced from the record (Notebook 22b)

Notebook 22b reads the committed outputs of the dark-sector record: the table `Revision/dark_sector/dirac16complex/outputs/eos-history.csv` (energy, pressures and $dw_{\rm eff}/da_4$ of the 14 Kohn-Sham series with nonzero energy, 41 slices each), the summary `eos-summary.json` and the independent free-gas output `independent-free-gas.json` in the same folder, and the model record `Revision/dark_sector/dirac16complex00/eos-theory.json` with the field-equation results `results/independent-numerics.json` of the same folder; and it checks that every check of the five dark-sector reports is PASS. It then tests the energy balance and the observer identities of Section 22.17 on the computed history, reproduces the band and the tangents of the gas, the bulk and brane bands, the condensate ratio and its phantom window, the mixture laws, and the models M2 to M5 with their crossings, each number asserted against its record file and check, and draws five figures. It needs only numpy and matplotlib, takes a few seconds (the recorded build and check runs of 2026-10-08 took 3.3 and 2.9 seconds) and ends with the line ALL 27 CHECKS PASSED (notebook 22b).

<!-- NOTEBOOK 22b -->

### 22.23 Line-by-line walk-through of Notebook 22b

The notebook has 9 code cells, In [1] to In [9]. This section explains every line of In [2] to In [9], in order; the printed output of each cell is in Section 22.22 under the label Out [k], and the five figures are shown there with their captions. For each figure this section adds what the student should see and why.

**In [1], the set-up cell.** It is the set-up cell of every notebook of this book, with the name `"22b"`; Section 22.12 explains each of its lines for Notebook 22a, and only the name differs. Its comment lines repeat the run instructions of Section 22.21. Its code finds the repository folder (`REPO`), decides where files are written (`OUTPUT_ROOT`), and defines the helpers the later cells use: `repository_file(relative)` gives the path of a repository file for reading; `output_file(relative)` the path at which to write one; `say(text)` prints in lines of at most 89 characters; `save_figure(fig, name, caption)` saves a figure as `Revision/textbook/figures/22b_<k>_<name>.png`, records its caption, shows it and prints where it was saved, numbering the figures in the dictionary `FIGURE_NUMBERS`; `check(condition, name, record)` stops the notebook if the condition is false and otherwise prints PASS with the name, and a second line naming the Revision record when `record` is given; `report(label, value)` prints a line RESULT label = value; `all_checks_passed()` prints the last line. The folder name `FIGURE_FOLDER` is `"Revision/textbook/figures"`, and `NOTEBOOK_ID` is `"22b"`. It prints one line.

**In [2], the records.**

```python
import csv  # reads the CSV tables of the Revision record
from fractions import Fraction  # exact fractions such as -382/441

import numpy as np  # arrays of numbers and their arithmetic
```

Three modules: `csv` reads tables stored as CSV files (comma-separated values: one line per row, the entries separated by commas); `Fraction` computes with exact fractions such as $-382/441$, without any rounding; `numpy`, called `np`, holds **arrays** (tables of numbers) and computes with whole arrays at once.

```python
D16 = "Revision/dark_sector/dirac16complex"  # the record of dirac16complex
D00 = "Revision/dark_sector/dirac16complex00"  # the record of dirac16complex00
PALETTE = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300",
           "#4a3aa7", "#e34948"]  # the colours of the figures, in a fixed order
```

Two names for the two folders of the dark-sector record, used in every path below, and eight colours written as hexadecimal codes (blue, orange, green, yellow, pink, dark green, violet, red), which the figures use in this order.

```python
def read_json(relative):
    """Read a JSON record of the repository into a Python dictionary."""
    return json.loads(repository_file(relative).read_text(encoding="utf-8"))
```

`read_json` reads a JSON file of the repository: `repository_file` gives its full path, `.read_text` reads it as text, and `json.loads` turns the text into a Python **dictionary** (pairs of a key and a value).

```python
REPORTS = {"derive": f"{D16}/reports/derivation-checks.json",
           "eos": f"{D16}/reports/eos-checks.json",
           "independent": f"{D16}/reports/independent-checks.json",
           "derive00": f"{D00}/reports/python-derive-eos.json",
           "numerics00": f"{D00}/reports/python-independent-numerics.json"}
EXPECTED = {"derive": 30, "eos": 13, "independent": 9, "derive00": 49,
            "numerics00": 28}  # the number of checks each report holds
```

The five check reports of the dark-sector record, each under a short key, and the number of checks each one holds according to the record's own document (`Revision/docs/DARK_SECTOR_HYPOTHESES.md`, section 11.1). A string that starts with `f` is an **f-string**: each name in braces is replaced by its value, so `f"{D16}/reports/eos-checks.json"` is the full repository path.

```python
for key, relative in REPORTS.items():
    entries = read_json(relative)["checks"]
    passed = [entry for entry in entries if entry["verdict"] == "PASS"]
    say(f"{relative}: {len(passed)} of {len(entries)} checks PASS")
    check(len(passed) == len(entries) == EXPECTED[key],
          f"all {EXPECTED[key]} checks of the report {key} are PASS",
          record=f"{relative}, all checks")
```

The loop takes the reports one after the other. `entries` is the list of checks of one report, each a dictionary with the keys `name`, `verdict` and `detail`; the **list comprehension** in square brackets keeps those whose verdict is PASS. The cell prints the count, and the check requires that every check passed and that the count is the expected one (the chained comparison `a == b == c` is true when all three are equal). These are the lines of Out [2] that name the five reports.

```python
with open(repository_file(f"{D16}/outputs/eos-history.csv"), newline="",
          encoding="utf-8") as handle:
    rows = list(csv.DictReader(handle))
COLUMNS = ["N", "a4", "E", "P3", "Pt", "dw_eff_da4"]
SERIES = {}  # series name -> {column name: numpy array over the slices}
for name in sorted({row["series"] for row in rows}):
    mine = [row for row in rows if row["series"] == name]
    SERIES[name] = {column: np.array([float(row[column]) for row in mine])
                    for column in COLUMNS}
```

`with open(...) as handle:` opens the table of the Kohn-Sham history and closes it when the indented line has run; `csv.DictReader` reads it row by row, each row a dictionary from the column names of the first line to the texts of that row, and `list` collects all rows. `COLUMNS` names the six columns the notebook uses: the number of quanta $N$, the slice $a_4$, the energy $E$, the integrated pressures $P_3$ and $P_t$, and the record's derivative $dw_{\rm eff}/da_4$. The braces with `for` inside, `{row["series"] for row in rows}`, make a **set** of the series names (each name once), which `sorted` puts in alphabetical order so that every run treats them in the same order. For each series, `mine` keeps its rows, and the inner dictionary comprehension makes, for each column, a numpy array of the numbers of that column (`float` turns a text into a number).

```python
GAS = [name for name in SERIES if SERIES[name]["N"][0] in (136, 688)]
summary = read_json(f"{D16}/outputs/eos-summary.json")
free_gas = read_json(f"{D16}/outputs/independent-free-gas.json")
theory00 = read_json(f"{D00}/eos-theory.json")
numerics00 = read_json(f"{D00}/results/independent-numerics.json")
```

`GAS` lists the ten series of the gas proper, those with $N = 136$ or 688 (the four series with $N = 8$ hold only brane zero modes). The other four lines read the summary of the equation of state of dirac16complex, the independent free-gas computation, the model record of dirac16complex00 (implementation A) and the results of its field-equation implementation B.

```python
say(f"{len(rows)} rows read: {len(SERIES)} series, {len(GAS)} of them with "
    "N = 136 or 688")
check(all(len(SERIES[name]["a4"]) == 41 for name in SERIES)
      and all(np.all(np.diff(SERIES[name]["a4"]) > 0) for name in SERIES),
      "every series has 41 slices in increasing order of a4")
```

The cell prints the counts (574 rows, 14 series, 10 gas series) and checks that every series has 41 slices and that $a_4$ increases along each (`np.diff` gives the differences of neighbouring entries; `np.all(... > 0)` is true when all are positive). The finite differences of the next cells rely on this order.

**In [3], the observer's equation of state on the gas.**

```python
def x_over_e(name):
    """X/E = (P3 - Pt)/E of one series at its 41 slices."""
    return (SERIES[name]["P3"] - SERIES[name]["Pt"]) / SERIES[name]["E"]
```

`x_over_e` returns the array of $X/E = (P_3 - P_t)/E$ of one series; numpy subtracts and divides the arrays entry by entry.

```python
gas = SERIES["N688_lam0"]  # the gas of N = 688 quanta with lambda = 0
a4, E = gas["a4"], gas["E"]
X = gas["P3"] - gas["Pt"]
h = a4[1] - a4[0]  # the step 0.05 between two slices
```

The series N688_lam0 is the main example. `a4` and `E` are its slices and energies, `X` its $X = P_3 - P_t$, and `h` the distance between two neighbouring slices, $0.05$.

```python
def derivative(f):
    """df/da4 at the slices 2 to 38: fourth-order central differences."""
    return (f[:-4] - 8 * f[1:-3] + 8 * f[3:-1] - f[4:]) / (12 * h)
```

`derivative` computes $df/da_4$ from the values of $f$ at the slices by the **fourth-order central difference** $f'(x) \approx [f(x - 2h) - 8f(x - h) + 8f(x + h) - f(x + 2h)]/(12h)$, whose error shrinks like $h^4$ (Chapter 2 treats the order of a numerical method). The four **slices** of the array do the shifting: `f[:-4]` holds the entries 0 to 36, that is $f(x - 2h)$ for the slices 2 to 38; `f[1:-3]` the entries 1 to 37, $f(x - h)$; `f[3:-1]` the entries 3 to 39, $f(x + h)$; and `f[4:]` the entries 4 to 40, $f(x + 2h)$. So the result holds the derivative at the interior slices 2 to 38; the two slices at each end have no two neighbours on both sides.

```python
worst = 0.0  # the largest relative violation of dE/da4 = -3X
for name in GAS:
    E_n = SERIES[name]["E"]
    X_n = SERIES[name]["P3"] - SERIES[name]["Pt"]
    violation = np.max(np.abs(derivative(E_n) + 3 * X_n[2:-2])) / np.max(np.abs(E_n))
    worst = max(worst, violation)
report("largest |dE/da4 + 3X|/max|E| over the 10 gas series", f"{worst:.3e}")
check(f"{worst:.3e}" == "1.235e-07", "the energy balance dE/da4 = -3X on the data",
      record=f"{D16}/reports/eos-checks.json, "
             "check conservation_dE_da4_equals_minus_3X")
```

The energy balance of Section 22.17, $dE/da_4 = -3X$, tested on the data. For each gas series the loop differentiates the solver's energies $E$ and compares with $-3X$ from the solver's pressure integrals, at the interior slices (`X_n[2:-2]` drops the two end entries on each side, to match). The violation is measured relative to the largest energy of the series, and `worst` keeps the largest violation over the ten series. Printed with three digits it is $1.235 \times 10^{-7}$, the number of the record's check (Out [3]): the two sides agree to about seven digits, the accuracy of the solver and of the finite differences. The format `:.3e` writes a number in scientific notation with three digits after the point.

```python
rho4_AB = E * np.exp(-3 * a4)  # definitions A and B: rho4 ~ E e^(-3 a4)
rho4_C = E  # definition C: rho4 ~ E
w_AB = -1 - derivative(np.log(rho4_AB)) / 3  # -1 - (1/3) d ln rho4/d ln a
w_C = -1 - derivative(np.log(rho4_C)) / 3
```

The observer's density under the definitions A and B ($E\,e^{-3a_4}$, up to a constant factor, which does not change a logarithmic derivative) and under C ($E$). The next two lines compute $w_{\rm eff} = -1 - \frac13\,d\ln\rho_4/d\ln a$ directly from its definition, with $d\ln a = da_4$: `np.log` takes the natural logarithm of every entry, and `derivative` differentiates it.

```python
error_AB = np.max(np.abs(w_AB - (X / E)[2:-2]))
error_C = np.max(np.abs(w_C - (X / E - 1)[2:-2]))
report("largest |w_eff(A, B) - X/E| from the dilution", f"{error_AB:.1e}")
report("largest |w_eff(C) - (X/E - 1)| from the dilution", f"{error_C:.1e}")
check(max(error_AB, error_C) < 1e-7,
      "w_eff(A) = w_eff(B) = X/E and w_eff(C) = X/E - 1 on the data",
      record=f"{D16}/reports/derivation-checks.json, checks "
             "w_eff_A_equals_X_over_E and w_eff_C_equals_X_over_E_minus_1")
```

The dilution-inferred values are compared with the identities $X/E$ and $X/E - 1$ of Section 22.17. Both differences are at most $1.7 \times 10^{-8}$ (Out [3]): on the computed history the identities hold to the accuracy of the differences. The record proves them exactly with sympy; this is the numerical test.

```python
ratios = np.concatenate([x_over_e(name) for name in GAS])
report("X/E of N688_lam0 at a4 = 0 and a4 = 2", f"{X[0] / E[0]:.4f}, "
       f"{X[-1] / E[-1]:.4f}")
report("X/E over all gas series, smallest and largest",
       f"{ratios.min():.6f}, {ratios.max():.6f}")
report("w_eff(C) over all gas series, smallest and largest",
       f"{ratios.min() - 1:.6f}, {ratios.max() - 1:.6f}")
```

`np.concatenate` joins the ten arrays of $X/E$ into one array of 410 numbers. The cell prints $X/E$ of N688_lam0 at the first and the last slice (0.2929 and 0.3183; `X[-1]` is the last entry), the smallest and largest $X/E$ of all gas series (0.292893 and 0.328105), and the same moved down by 1, the range under C ($-0.707107$ to $-0.671895$).

```python
check(f"{ratios.min():.6f}" == "0.292893" and f"{ratios.max():.6f}" == "0.328105",
      "the gas is radiation-like: X/E in [0.292893, 0.328105]",
      record=f"{D16}/reports/eos-checks.json, check gas_radiation_like_band")
check(all(np.all(np.diff(x_over_e(name)) > 0) for name in GAS),
      "X/E rises with a4 in every gas series (toward 1/3, not toward 0)",
      record=f"{D16}/reports/eos-checks.json, "
             "check gas_X_over_E_rises_toward_one_third")
```

The two checks compare the band with the six digits of the record's check, and require that $X/E$ increases from each slice to the next in every gas series: the gas approaches radiation, it does not fall toward dust.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.8))
for colour, name in zip(PALETTE, ["N136_lam0", "N688_lam0", "N688_lamp2"]):
    left.plot(SERIES[name]["a4"], x_over_e(name), color=colour, label=name)
    right.plot(SERIES[name]["a4"], x_over_e(name) - 1, color=colour, label=name)
```

`plt.subplots(1, 2, ...)` makes a figure with two panels side by side, 9.0 by 3.8 inches, and names them `left` and `right`. `zip` pairs the first three colours with three series; each series is drawn in the left panel as $X/E$ (definitions A and B) and in the right panel as $X/E - 1$ (definition C), with its name as the label of the legend.

```python
left.axhline(1 / 3, color="black", linestyle="--", linewidth=0.8,
             label="radiation, 1/3")
right.axhline(-2 / 3, color="black", linestyle="--", linewidth=0.8,
              label="1/3 - 1")
left.set_title("definitions A and B: $w_{eff} = X/E$")
right.set_title("definition C: $w_{eff} = X/E - 1$")
```

`axhline` draws a horizontal line across a panel: the radiation value $1/3$ on the left (dashed: the line style written as two minus signs) and the same value moved down by 1, $-2/3$, on the right. The titles name the definitions; text between dollar signs is set as mathematics.

```python
for ax in (left, right):
    ax.set_xlabel("$a_4$ along the prescribed history")
    ax.legend(fontsize=8)
left.set_ylabel("$w_{eff}$")
save_figure(fig, "gas_three_definitions",
            "The equation of state $w_{eff}$ that a 3-space observer infers from "
...)
```

Both panels get the label of the horizontal axis and a legend; the left one the label of the vertical axis. `save_figure` saves the figure as Figure 22b.1 with its caption (shortened here; the full caption is printed under the figure in Section 22.22). **What to see:** the two panels have the same shape, moved by exactly 1. On the left, every curve rises toward the dashed radiation line, the larger gas ($N = 688$) a little lower than the smaller one, and the interaction ($\lambda_2$, green) changes almost nothing. On the right, the same curves lie between $-0.71$ and $-0.67$: far above $-1$, and rising, which is the thawing sign. The physics of the gas is the same in both panels; only the ASSUMED definition of the observer's density differs.

**In [4], the CPL tangents of the gas.**

```python
TODAY = [0.5, 1.0, 1.5, 2.0]  # the four choices of a4,today of the record
index = [int(round(t / h)) for t in TODAY]  # their positions in the slice list
recorded = {entry["series"]: entry for entry in summary["series"]}
say("a4,today   w0 under C   wa (every definition)")
differences = []
```

The four values of $a_{4,\rm today}$ that the record uses, and their positions in the list of slices: $0.5/0.05 = 10$, then 20, 30 and 40 (`round` removes the tiny error of the division, and `int` makes a whole number). `recorded` maps each series name to its entry of the summary. The cell prints a header line and starts an empty list `differences`.

```python
for t, i, entry in zip(TODAY, index, recorded["N688_lam0"]["cplTangent"]):
    w0 = X[i] / E[i] - 1  # w_eff(C) today
    wa = -gas["dw_eff_da4"][i]  # w_a = -dw/da at a = 1, and da = da4 there
    say(f"{t:8.1f}   {w0:10.4f}   {wa:12.5f}")
    differences += [abs(w0 - entry["w_eff_C"]["w0"]), abs(wa - entry["w_eff_C"]["wa"])]
check(max(differences) < 1e-12, "the CPL tangents of N688_lam0",
      record=f"{D16}/outputs/eos-summary.json, key cplTangent of N688_lam0")
```

For each choice of today, the tangent of Section 22.18: $w_0$ is $w_{\rm eff}(C) = X/E - 1$ at that slice, and $w_a = -dw_{\rm eff}/da_4$ there, read from the record's column `dw_eff_da4` (the derivative of $X/E$; under C the constant $-1$ does not change it). The format `8.1f` writes a number in 8 places with one digit after the point. The two numbers are compared with the summary's tangent of the same series; `+=` appends both differences to the list. The table of Out [4] is the table of Section 22.18.

```python
tangents = [-SERIES[name]["dw_eff_da4"][i] for name in GAS for i in index]
report("tangent wa of every gas series, smallest and largest",
       f"{min(tangents):.6f}, {max(tangents):.6f}")
check(f"{min(tangents):.6f}" == "-0.020523" and f"{max(tangents):.6f}" == "-0.008894"
      and f"{ratios.min() - 1:.6f}" == "-0.707107"
      and f"{ratios.max() - 1:.6f}" == "-0.671895",
      "every gas tangent wa is negative (thawing sign) and far below 0.60",
      record=f"{D16}/reports/eos-checks.json, check gas_cpl_thawing_sign_small")
```

The tangent $w_a$ of every gas series at every choice of today (40 numbers; the comprehension with two `for` runs over both). The smallest is $-0.020523$ and the largest $-0.008894$: all negative, the thawing sign, and at most about one thirtieth of the observed $0.60$. The check compares them, and the range of $w_{\rm eff}(C)$ from In [3], with the six digits of the record's check.

**In [5], the bulk band and the brane band.**

```python
bulk = free_gas["bulkBand_n2_1"]  # the lowest massive (odd-parity) level, shell 1
brane = free_gas["braneBand_n2_1"]  # the brane-band level of the same shell
a4_band = np.array([point["a4"] for point in bulk])
w_bulk = np.array([point["w_eff_A_B"] for point in bulk])
w_brane = np.array([point["w_eff_A_B"] for point in brane])
```

The independent free-gas output holds two lists of points, one for the lowest level of the massive bulk band of the shell $n_2 = 1$ and one for the brane-band level of the same shell, each point a dictionary with the slice `a4` and the value `w_eff_A_B` of $w_{\rm eff}$ under A and B. The three arrays collect the slices ($-3$ to 4 in steps of $0.25$) and the two curves.

```python
report("w_eff(A) of the bulk level at a4 = -3 and a4 = 4",
       f"{w_bulk[0]:.6f}, {w_bulk[-1]:.3e}")
report("ratio w(4)/w(3.75) of the bulk level", f"{w_bulk[-1] / w_bulk[-2]:.6f}")
report("w_eff(A) of the brane level, smallest and largest",
       f"{w_brane.min():.6f}, {w_brane.max():.6f}")
```

The first and last value of the bulk level (0.239626 and $2.268 \times 10^{-3}$), the ratio of its last two values (0.765177, which Section 22.18 compares with $e^{-0.25}$), and the range of the brane level (0.291594 to 0.333275).

```python
check(a4_band[0] == -3 and a4_band[-1] == 4 and np.all(np.diff(w_bulk) < 0)
      and f"{w_bulk[0]:.6f}" == "0.239626" and f"{w_bulk[-1]:.3e}" == "2.268e-03",
      "the bulk level falls from 0.239626 to 2.268e-03 (dark-matter-like)",
      record=f"{D16}/reports/independent-checks.json, check bulk_band_dark_matter_law")
check(f"{w_brane.min():.6f}" == "0.291594" and f"{w_brane.max():.6f}" == "0.333275",
      "the brane level stays between 0.291594 and 0.333275 (radiation-like)",
      record=f"{D16}/reports/independent-checks.json, check brane_band_radiation_law")
```

The first check requires the range of slices, that the bulk level falls at every step (all differences negative), and its two end values as the record's check states them; the second the range of the brane level.

```python
fig, ax = plt.subplots(figsize=(7.0, 4.2))
ax.plot(a4_band, w_bulk, "o-", color=PALETTE[1], markersize=3,
        label="bulk band (massive), one level")
ax.plot(a4_band, w_brane, "s-", color=PALETTE[0], markersize=3,
        label="brane band (massless at k = 0), one level")
ax.plot(a4, X / E, color=PALETTE[2], linewidth=2.5, label="the gas N688_lam0")
```

One panel. The bulk level is drawn in orange with small circles (`"o-"`: points joined by lines), the brane level in blue with small squares, and the gas N688_lam0 of In [3] as a thick green line over its range $0 \le a_4 \le 2$.

```python
ax.axhline(1 / 3, color="black", linestyle="--", linewidth=0.8)
ax.axhline(0.0, color="black", linestyle=":", linewidth=0.8)
ax.set_xlabel("$a_4$")
ax.set_ylabel("$w_{eff}$ under definitions A and B")
ax.legend(fontsize=8)
save_figure(fig, "bulk_and_brane_bands",
            "Which quanta of dirac16complex behave like dark matter. Horizontal "
...)
```

The radiation value $1/3$ (dashed) and the dust value 0 (dotted), the axis labels, the legend, and Figure 22b.2. **What to see:** only the orange curve goes from near radiation toward dust, the dark-matter-like behaviour of the flat-limit law of Section 22.18. The blue curve dips slightly and then climbs to $1/3$, and the green gas, which consists of brane-band quanta, follows the blue behaviour. The time-varying dark-matter-like equation of state exists in the theory, but in a band that the computed states leave empty.

**In [6], the condensate.**

```python
u = Fraction(-382, 441)  # lambda S/m, CHOSEN so that the ratio is -0.764
ratio = u / (2 + u)  # p/rho = (lambda S^2/2)/(m S + lambda S^2/2) = u/(2 + u)
density = 1 + u / 2  # rho/(m S)
report("the ratio u/(2 + u) at u = -382/441", f"{ratio} = {float(ratio)}")
report("rho/(m S) = 1 + u/2", f"{density} = {float(density):.12f}")
```

`Fraction(-382, 441)` is the exact fraction $-382/441$; arithmetic with it stays exact. The ratio $u/(2 + u)$ of Section 22.18 comes out as the fraction $-191/250 = -0.764$, and $\rho/(mS) = 1 + u/2 = 250/441 = 0.566893424036$ (Out [6]; `float` turns a fraction into a decimal number).

```python
check(ratio == Fraction(-764, 1000)
      and abs(float(u) - summary["condensate"]["u_for_ratio_minus_0p764"]) < 1e-12,
      "the condensate ratio is -0.764 at u = -382/441 (one CHOSEN parameter)",
      record=f"{D16}/reports/derivation-checks.json, "
             "check condensate_ratio_equal_unite_constant_w")
```

The ratio must equal $-764/1000$ exactly (`Fraction` reduces it to $-191/250$ and compares exactly), and $u$ must agree with the value the summary records.

```python
grid = np.linspace(-3.0, 1.0, 4001)
grid = grid[np.abs(grid + 2) > 1e-9]  # leave out the pole u = -2
below = grid / (2 + grid) < -1  # where the ratio is phantom
check(np.array_equal(below, (grid > -2) & (grid < -1)),
      "the ratio is below -1 exactly for -2 < u < -1",
      record=f"{D00}/reports/python-derive-eos.json, "
             "check condensate_phantom_interval")
```

A test of the phantom window derived in Section 22.18 on 4001 values of $u$ from $-3$ to 1 (step 0.001). The second line removes the value $u = -2$, where the ratio has a zero denominator: the condition in square brackets is an array of true and false, and indexing with it keeps the entries where it is true. `below` marks where the ratio is below $-1$; `(grid > -2) & (grid < -1)` marks the window (the operator between the two conditions means "and", applied entry by entry); `np.array_equal` requires that the two markings agree at every point.

```python
fig, ax = plt.subplots(figsize=(7.0, 4.2))
for part in (grid[grid < -2], grid[grid > -2]):
    ax.plot(part, part / (2 + part), color=PALETTE[0])
ax.axvspan(-2, -1, color=PALETTE[7], alpha=0.12, label="phantom ratio, -2 < u < -1")
```

The ratio is drawn in two pieces, left and right of the pole, so that no line jumps across it. `axvspan` shades the vertical band $-2 < u < -1$ in pale red (`alpha=0.12` makes it nearly transparent).

```python
ax.axhline(0.0, color="black", linestyle="--", linewidth=0.8,
           label="$w_{eff}$, definitions A and B")
ax.axhline(-1.0, color="black", linestyle=":", linewidth=0.8,
           label="$w_{eff}$, definition C")
ax.plot([float(u)], [float(ratio)], "o", color=PALETTE[1],
        label="CHOSEN: u = -382/441 gives -0.764")
ax.set_ylim(-4.0, 4.0)
```

The two values that the observer infers for any condensate, 0 (A, B; dashed) and $-1$ (C; dotted), and the CHOSEN point in orange; `set_ylim` shows the vertical range $-4$ to 4, so that the steep branches near the pole are cut off.

```python
ax.set_xlabel("$u = \\lambda S/m$")
ax.set_ylabel("ratio $p/\\rho$")
ax.legend(fontsize=8, loc="lower right")
save_figure(fig, "condensate_ratio",
            "The constant ratio $p/\\rho = u/(2 + u)$ of a homogeneous condensate "
...)
```

The axis labels (the doubled backslash `\\` puts one backslash into the text, which the mathematics needs before `lambda` and `rho`), the legend in the lower right corner, and Figure 22b.3. **What to see:** the ratio can take any value, and the value $-0.764$ is one point on the curve, reached by choosing $u$; it says nothing about the observer, whose two readings are the horizontal lines, the same for every $u$. Left of the pole the ratio is above 1, right of it the curve climbs from far below through the phantom band to $-1$ at $u = -1$, to 0 at $u = 0$ and on toward 1.

**In [7], the mixtures.**

```python
r0 = Fraction(417, 583)  # gas/condensate energy today, CHOSEN for w0(C) = -0.861
w0_exact = r0 / (3 * (r0 + 1)) - 1  # w_eff(C) today
wa_exact = r0 / (3 * (r0 + 1) ** 2)  # w_a of the exact law: positive (freezing)
report("exact law: w0 under C and wa", f"{w0_exact}, {float(wa_exact):.6f}")
check(w0_exact == Fraction(-861, 1000) and f"{float(wa_exact):.6f}" == "0.081037",
      "radiation plus condensate with w0(C) = -0.861 has wa = 0.081037 > 0",
      record=f"{D16}/reports/derivation-checks.json, "
             "check mixture_C_matching_w0_unite")
```

The exact law of Section 22.18 for a radiation-like gas plus a condensate, with exact fractions: at the CHOSEN $r_0 = 417/583$, $w_0$ under C is exactly $-861/1000$ and $w_a = 0.081037$, positive (`**` is the power).

```python
def mixture_w_C(share):
    """w_eff(C) of the gas N688_lam0 plus a condensate along the history; the gas
    has the energy share "share" today (a4 = 2)."""
    condensate = E[-1] * (1 - share) / share  # constant condensate energy
    return X / (E + condensate) - 1
```

`mixture_w_C` mixes the computed gas with a condensate and returns $w_{\rm eff}(C)$ at all 41 slices. Today is the last slice, $a_4 = 2$. If the gas has the share `share` of the energy today, the condensate energy is $E_c = E(2)(1 - \text{share})/\text{share}$ (from $E(2)/(E(2) + E_c) = \text{share}$), constant in time. The condensate adds energy but no $X$, so the mixture has $w_{\rm eff}(C) = X/(E + E_c) - 1$.

```python
share = 0.139 / (X[-1] / E[-1])  # CHOSEN: gives w_eff(C) = -0.861 today
w_mix = mixture_w_C(share)
```

Today $w_{\rm eff}(C) = \text{share} \cdot X/E - 1$, so $w_{\rm eff}(C) = -0.861$ needs $\text{share} = 0.139/(X/E)$ at $a_4 = 2$: $0.139/0.3183 = 0.436703$. This share is CHOSEN; `w_mix` is the mixture's history.

```python
# w_a = -dw/da4 at a4 = 2, one-sided fourth-order differences (as the record)
wa_mix = -(3 * w_mix[-5] - 16 * w_mix[-4] + 36 * w_mix[-3] - 48 * w_mix[-2]
           + 25 * w_mix[-1]) / (12 * h)
recorded_mix = summary["mixture_C_w0_minus_0p861"]
```

At the last slice there are no neighbours on the right, so the derivative uses the **one-sided fourth-order difference** $f'(x) \approx [3f(x - 4h) - 16f(x - 3h) + 36f(x - 2h) - 48f(x - h) + 25f(x)]/(12h)$, the same stencil as the record; `w_mix[-5]` is the fifth entry from the end. The minus sign makes it $w_a$. `recorded_mix` is the record's entry for this mixture.

```python
report("gas share today for w_eff(C) = -0.861 (CHOSEN)", f"{share:.6f}")
report("w0 and wa of that mixture under C", f"{w_mix[-1]:.3f}, {wa_mix:.6f}")
check(abs(share - recorded_mix["gas_fraction_today"]) < 1e-12
      and abs(wa_mix - recorded_mix["wa"]) < 1e-10 and wa_mix > 0,
      "the computed gas mixture with w0(C) = -0.861 is freezing, wa = 0.067014",
      record=f"{D16}/reports/eos-checks.json, check mixture_C_w0_unite_has_positive_wa")
```

The share 0.436703 and $(w_0, w_a) = (-0.861, 0.067014)$ are printed and compared with the record: $w_a$ is positive, freezing, the opposite sign to the observed $-0.60$.

```python
a_obs = np.exp(a4 - 2.0)  # the observer scale factor, a = 1 today (a4 = 2)
fig, ax = plt.subplots(figsize=(7.0, 4.2))
for colour, part in zip(PALETTE, [0.25, share, 0.75, 1.0]):
    ax.plot(a_obs, mixture_w_C(part), color=colour,
            label=f"gas share today {part:.3f}")
ax.plot(a_obs, -0.861 - 0.60 * (1 - a_obs), "k--", label="Unite CPL line")
ax.axhline(-1.0, color="black", linestyle=":", linewidth=0.8)
```

The observer's scale factor $a = e^{a_4 - 2}$ runs from $e^{-2} = 0.135$ to 1 over the history. Four mixtures are drawn against it, with the gas shares 0.25, the CHOSEN 0.437, 0.75 and 1 (pure gas), together with the observed CPL line (the style `"k"` followed by two minus signs: black and dashed) and the value $-1$ (dotted).

```python
ax.set_xlabel("observer scale factor $a = e^{a_4 - 2}$")
ax.set_ylabel("$w_{eff}$ under definition C")
ax.legend(fontsize=8)
save_figure(fig, "mixtures_against_unite",
            "Mixtures of the computed Kohn-Sham gas N688_lam0 with a condensate, "
...)
```

Labels, legend and Figure 22b.4. **What to see:** every curve that contains condensate slopes DOWN toward $-1$ as $a$ grows, because the gas redshifts and the condensate's $-1$ takes over; the observed line slopes UP. The orange curve meets the observed line at $a = 1$ (that is how its share was chosen) and leaves it at once in the opposite direction. No choice of the share turns one slope into the other.

**In [8], the models of dirac16complex00.**

```python
def model(a, components):
    """The total energy density and the sum of eps_i rho_i of a WKB model at a
    (a number or an array).  Each component is (kind, weight at a = 1, s)."""
    a = np.asarray(a, dtype=float)
    rho_total, eps_rho = np.zeros_like(a), np.zeros_like(a)
    for kind, weight, s in components:
```

`model` evaluates the adiabatic gas of Section 22.19 at the scale factor `a`, which may be one number or an array (`np.asarray` makes an array of it either way). A model is a list of components, each a **tuple** `(kind, weight, s)`: what it is, its energy density at $a = 1$, and its parameter. `rho_total` will hold $\sum_i\rho_i$ and `eps_rho` the sum $\sum_i\varepsilon_i\rho_i$; `np.zeros_like(a)` makes arrays of zeros of the shape of `a`.

```python
        if kind == "condensate":  # rho constant, eps = 0
            rho, eps = weight + 0 * a, 0 * a
        elif kind == "kmode":  # q = 0 and s = k^2/(k^2 + m^2) at a = 1
            r = s / (1 - s)  # k^2/m^2
            rho = weight * np.sqrt((r / a**2 + 1) / (r + 1))  # omega(a)/omega(1)
            eps = (r / a**2) / (3 * (r / a**2 + 1))
```

A condensate (with $\lambda = 0$) has constant energy density and $\varepsilon = 0$; adding `0 * a` gives the numbers the shape of `a`. A gas of modes with $q = 0$ (`"kmode"`) is described by $s = k^2/(k^2 + m^2)$ at $a = 1$; $r = s/(1 - s)$ is then $k^2/m^2$. Its energy density is $\rho_i \propto \omega = m\sqrt{1 + r/a^2}$, scaled to the weight at $a = 1$, and $\varepsilon = (k^2/a^2)/(3\omega^2) = (r/a^2)/(3(r/a^2 + 1))$, the formula of Section 22.19 with $q = 0$ and $m = 1$.

```python
        elif kind == "qmode":  # k = 0 and s = q^2/m^2 at a = 1
            rho = weight * np.sqrt((1 - s * a**2) / (1 - s))
            eps = s * a**2 / (3 * (1 - s * a**2))
        else:  # "ghost": massless modes of NEGATIVE classical energy
            rho, eps = -weight / a, 1 / 3 + 0 * a
```

An extra-time mode with $k = 0$ (`"qmode"`), $s = q^2/m^2$ at $a = 1$: $\omega = m\sqrt{1 - sa^2}$, so $\rho_i$ is the weight times $\sqrt{(1 - sa^2)/(1 - s)}$, and $\varepsilon = sa^2/(3(1 - sa^2))$. The ghost-like component: massless modes ($\varepsilon = 1/3$) of NEGATIVE energy density $-G/a$, with $G$ the weight.

```python
        rho_total = rho_total + rho
        eps_rho = eps_rho + eps * rho
    return rho_total, eps_rho
```

Each component adds its $\rho_i$ and its $\varepsilon_i\rho_i$ to the two sums, which the function returns.

```python
def w_model(a, components):
    """w_eff under definition C: sum eps_i rho_i / sum rho_i - 1."""
    rho_total, eps_rho = model(a, components)
    return eps_rho / rho_total - 1
```

`w_model` is the mixture formula of Section 22.19 under C.

```python
def tangent(components, d=1e-3):
    """CPL tangent w0 = w(1), wa = -dw/da at a = 1 (fourth-order differences)."""
    f = [float(w_model(1 + k * d, components)) for k in (-2, -1, 1, 2)]
    slope = (f[0] - 8 * f[1] + 8 * f[2] - f[3]) / (12 * d)  # dw/da at a = 1
    return float(w_model(1.0, components)), -slope
```

`tangent` returns $w_0 = w(1)$ and $w_a = -dw/da$ at $a = 1$; the slope is the fourth-order central difference of In [3], with the step $d = 10^{-3}$ in $a$.

```python
M5_RECORD = theory00["models"]["M5_with_ghost_component"]
G = float(Fraction(M5_RECORD["parameters"]["G"]))  # ghost share 3/10, a choice
s5 = float(M5_RECORD["parameters"]["s"])  # CHOSEN with q5 to fit the Unite line
q5 = float(M5_RECORD["parameters"]["Omega_q"])
c5 = float(M5_RECORD["parameters"]["Omega_c"])
```

The parameters of M5 are read from the record: the ghost share $G = 3/10$ (stored as the text `"3/10"`, which `Fraction` reads), and $s$, the mode share $\Omega_q$ and the condensate share $\Omega_c$, which the record found by solving the two fit conditions (stored with 12 digits).

```python
MODELS = {"M2": [("kmode", 1.0, 417 / 1000)],  # s CHOSEN: w0 = -0.861
          "M3": [("qmode", 1.0, 417 / 1417)],  # s CHOSEN: w0 = -0.861
          "M4": [("condensate", 1 - 57963 / 264037, 0.0),  # both CHOSEN:
                 ("qmode", 57963 / 264037, 264037 / 403037)],  # tangent = Unite
          "M5": [("condensate", c5, 0.0), ("qmode", q5, s5), ("ghost", G, 0.0)]}
```

The four models of the table of Section 22.19, each as a list of components with its CHOSEN parameters. The weights of M4 and M5 add up to 1 at $a = 1$: $(1 - \Omega_q) + \Omega_q = 1$, and $\Omega_c + \Omega_q - G = 0.705325 + 0.594675 - 0.3 = 1$.

```python
EXPECTED_WA = {"M2": 81037 / 500000, "M3": -196963 / 500000, "M4": -0.6}
RECORD_CHECK = {"M2": "M2_tangent_exact", "M3": "M3_tangent_exact",
                "M4": "M4_tangent_equals_unite"}
for name in ("M2", "M3", "M4"):
    w0, wa = tangent(MODELS[name])
    report(f"{name} tangent (w0, wa) under C", f"({w0:.6f}, {wa:.6f})")
    check(abs(w0 + 0.861) < 1e-12 and abs(wa - EXPECTED_WA[name]) < 1e-8,
          f"the tangent of {name}",
          record=f"{D00}/reports/python-derive-eos.json, check {RECORD_CHECK[name]}")
```

The exact tangent slopes of the record ($81037/500000 = 0.162074$, $-196963/500000 = -0.393926$ and $-0.6$) and the names of the record's checks. For each model the cell computes the tangent and checks $w_0 = -0.861$ to $10^{-12}$ and $w_a$ to $10^{-8}$, the accuracy of the finite difference. Out [8] prints $(-0.861, 0.162074)$, $(-0.861, -0.393926)$ and $(-0.861, -0.600000)$.

```python
a_fit = np.linspace(0.5, 1.0, 101)  # 101 points of a in [1/2, 1], as the record
wa_fit, w0_fit = np.polyfit(1 - a_fit, w_model(a_fit, MODELS["M5"]), 1)
report("M5 least-squares fit over a in [1/2, 1]", f"({w0_fit:.6f}, {wa_fit:.6f})")
check(abs(w0_fit + 0.861) < 1e-9 and abs(wa_fit + 0.6) < 1e-9,
      "the M5 fit equals the Unite pair (by construction)",
      record=f"{D00}/reports/python-derive-eos.json, check M5_fit_equals_unite")
```

The least-squares fit of M5, as in the record: 101 equally spaced values of $a$ from $1/2$ to 1, and `np.polyfit(x, y, 1)` finds the straight line $y = c_1x + c_0$ closest to the points (the sum of the squared vertical distances is smallest) and returns $[c_1, c_0]$. With $x = 1 - a$ the line is $w_0 + w_a(1 - a)$, so $c_1 = w_a$ and $c_0 = w_0$. The fit is the observed pair to $10^{-9}$: by construction, since $s$ and $\Omega_q$ were chosen for exactly this.

```python
def crossings(components):
    """The values of a in [1/3, 1] where w = -1 (400 intervals, then bisection)."""
    points = np.linspace(1 / 3, 1, 401)
    values = w_model(points, components) + 1
    found = []
```

`crossings` finds where $w = -1$ between $a = 1/3$ and 1: it divides the range into 400 intervals (401 points) and evaluates $w + 1$, which changes sign at a crossing.

```python
    for low, high, v_low, v_high in zip(points, points[1:], values, values[1:]):
        if v_low * v_high < 0:
            for _ in range(60):  # halve the interval 60 times
                middle = (low + high) / 2
                v_middle = float(w_model(middle, components) + 1)
                if v_low * v_middle <= 0:
                    high = middle
                else:
                    low, v_low = middle, v_middle
            found.append((low + high) / 2)
    return found
```

`zip(points, points[1:], ...)` runs over neighbouring pairs of points with their values. Where the product of the two values is negative, the sign changes inside the interval, and **bisection** narrows it: the middle is evaluated, and the half in which the sign still changes is kept (if the left value and the middle value have opposite signs or the middle is zero, the crossing is in the left half, so `high` moves to the middle; otherwise in the right half). After 60 halvings the interval is $2^{-60}$ times its original width $1/600$, far below the precision of the numbers, and its middle is recorded. The underscore `_` is the name of a loop variable that is not used.

```python
cross_M5 = crossings(MODELS["M5"])
no_ghost = [("condensate", 1 - q5, 0.0), ("qmode", q5, s5)]  # M5 without ghost
lowest_M4 = float(np.min(w_model(np.arange(1, 301) / 300, MODELS["M4"])))
crossing_A = float(M5_RECORD["N2"]["crossings_of_minus_1_in_[1/3,1]"][0])
crossing_B = numerics00["models"]["M5_with_ghost_component"]["crossing_N2"]
M4_RECORD = theory00["models"]["M4_condensate_plus_extra_time_mode"]
```

The crossings of M5; the same model with its ghost-like part removed (the condensate share becomes $1 - \Omega_q$, so that the total is 1 again); the smallest $w$ of M4 at $a = 1/300, 2/300, \dots, 1$ (`np.arange(1, 301)` gives the whole numbers 1 to 300); the record's crossing from implementation A (stored as a text in a list) and from the field-equation implementation B; and the record's entry for M4.

```python
report("M5 crosses w = -1 at a", f"{cross_M5[0]:.11f}")
report("the same crossing from the field equation (implementation B)",
       f"{crossing_B}")
report("lowest w_eff(C) of M4 for a = 1/300 to 1", f"{lowest_M4:.12f}")
```

Out [8] prints the crossing $a = 0.77909966367$, implementation B's $0.77905405$, and the lowest $w$ of M4, $-0.999999214228$: above $-1$.

```python
check(len(cross_M5) == 1 and abs(cross_M5[0] - crossing_A) < 1e-10,
      "M5 crosses -1 once, at a = 0.7791",
      record=f"{D00}/reports/python-derive-eos.json, check M5_crosses_minus_1")
check(crossings(no_ghost) == [] and crossings(MODELS["M4"]) == []
      and abs(lowest_M4 - float(M4_RECORD["min_w_N2_on_(0,1]"])) < 1e-11,
      "no crossing without the ghost: M5 without it, and M4 (w >= -1)",
      record=f"{D00}/reports/python-derive-eos.json, checks "
             "M5_without_ghost_no_crossing and M4_never_phantom")
check(abs(crossing_B - cross_M5[0]) < 1e-4,
      "implementation B finds the M5 crossing within 1e-4",
      record=f"{D00}/reports/python-independent-numerics.json, "
             "check B_vs_A_M5_crossing")
```

Three checks: M5 crosses $-1$ exactly once, where the record says; neither M5 without its ghost-like part nor M4 crosses at all (an empty list `[]`), and the lowest value of M4 is the record's; and the field-equation implementation B agrees on the crossing within $10^{-4}$ (the difference is $4.6 \times 10^{-5}$, the accuracy of B's numerical solution).

```python
a_plot = np.linspace(1 / 3, 1.0, 300)
fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.8))
LABELS = {"M2": "M2, gas (1 CHOSEN)", "M3": "M3, extra-time mode (1 CHOSEN)",
          "M4": "M4 (2 CHOSEN)", "M5": "M5 (2 CHOSEN, ghost-like part)"}
for colour, name in zip(PALETTE, MODELS):
    left.plot(a_plot, w_model(a_plot, MODELS[name]), color=colour,
              label=LABELS[name])
```

300 values of $a$ from $1/3$ to 1 and a figure with two panels. The labels state for each model how many parameters were CHOSEN. The loop draws $w_{\rm eff}(C)$ of the four models in the left panel (looping over a dictionary gives its keys, here in the order M2, M3, M4, M5).

```python
left.plot(a_plot, -0.861 - 0.60 * (1 - a_plot), "k--", label="Unite CPL line")
left.axhline(-1.0, color="black", linestyle=":", linewidth=0.8)
left.set_xlabel("observer scale factor $a$")
left.set_ylabel("$w_{eff}$ under definition C")
left.legend(fontsize=7)
```

The observed CPL line (dashed), the value $-1$ (dotted), the labels and the legend of the left panel.

```python
PARTS = [("condensate", MODELS["M5"][0]), ("extra-time mode", MODELS["M5"][1]),
         ("ghost-like part", MODELS["M5"][2])]
for colour, (label, component) in zip(PALETTE[4:], PARTS):
    right.plot(a_plot, model(a_plot, [component])[0], color=colour, label=label)
right.plot(a_plot, model(a_plot, MODELS["M5"])[0], "k-", label="total")
right.axhline(0.0, color="black", linewidth=0.6)
```

The right panel shows the **populations** of M5: the energy density of each of its three parts, computed by calling `model` with a list that holds only that part (`[0]` takes the first of the two returned sums, the energy density), in the colours from the fifth on (`PALETTE[4:]`), and their total in black, with the zero line.

```python
right.set_xlabel("observer scale factor $a$")
right.set_ylabel("energy density, M5")
right.legend(fontsize=7)
fig.subplots_adjust(wspace=0.3)  # room between the two panels
save_figure(fig, "models_against_unite",
            "The models of dirac16complex00 under definition C against the "
...)
```

Labels and legend of the right panel; `subplots_adjust(wspace=0.3)` widens the gap between the panels so that the labels do not overlap; Figure 22b.5. **What to see:** on the left, all four curves pass through $w = -0.861$ at $a = 1$ (by the choice of their parameters). M2 slopes the wrong way (freezing). M3 and M4 slope the right way but flatten above the dotted line $-1$: with positive energies they can never go below it. M4 even has the right slope at $a = 1$, by construction. Only M5 follows the dashed line through $-1$, and it does so only because its ghost-like part, the violet curve on the right, carries a negative energy that grows like $1/a$ toward the past. Nothing in the field equations selects any of these populations.

**In [9], the comparison with the observed values.**

```python
unite = theory00["models"]["unite"]
w0_u, wa_u = Fraction(unite["w0"]), Fraction(unite["wa"])
crossing_u = 1 + (1 + w0_u) / wa_u  # w0 + wa (1 - a) = -1 solved for a
```

The record stores the observed values as exact fractions in text form (`"-861/1000"`, `"-3/5"`), which `Fraction` reads. The crossing of the CPL line with $-1$ is solved as in Section 22.16: $a = 1 + (1 + w_0)/w_a$.

```python
TABLE = [("w = -0.764", "condensate ratio, u = -382/441", "1 for 1"),
         ("w0 = -0.861", "M2; M3; gas plus condensate", "1 for 1"),
         ("(w0, wa) = (-0.861, -0.60)", "M4 tangent; M5 fit", "2 for 2"),
         ("crossing of -1, a = 0.7683", "only M5", "ghost-like part")]
say("Unite value | reproduced by | CHOSEN parameters")
for row in TABLE:
    say(" | ".join(row))
report("the Unite CPL line crosses w = -1 at a", f"{crossing_u}")
```

A short form of the comparison table of Section 22.19: each observed value, what reproduces it, and how many parameters were CHOSEN for it. `" | ".join(row)` writes the three texts of a row with a vertical bar between them. The crossing is printed as the fraction $461/600$.

```python
check(w0_u == Fraction(-861, 1000) and wa_u == Fraction(-3, 5)
      and crossing_u == Fraction(unite["crossing_of_minus_1"]["a"])
      and crossing_u == Fraction(461, 600),
      "the Unite values and their crossing a = 461/600",
      record=f"{D00}/reports/python-derive-eos.json, check unite_crossing_point")
files = [f"{FIGURE_FOLDER}/{NOTEBOOK_ID}_{number}_{name}.png"
         for name, number in FIGURE_NUMBERS.items()]
check(len(files) == 5 and all(output_file(path).is_file() for path in files),
      "every figure file of this notebook exists")
all_checks_passed()
```

The observed values are the ones `Revision/README.md` quotes, and their crossing is exactly the record's $461/600$. `files` rebuilds the names of the saved figures from the dictionary `FIGURE_NUMBERS` of the set-up cell, and the last check requires five of them, all present. The last line prints ALL 27 CHECKS PASSED (notebook 22b).

### 22.24 What Notebook 22b found, and what remains open for the dark sector

**The results.** Every number below is printed by the notebook in the cell named, and every one reproduces the Revision record named in the same cell.

| result | value | status | where |
| --- | --- | --- | --- |
| energy balance $dE/da_4 = -3X$ on the history | relative violation $1.235 \times 10^{-7}$ | PROVED exactly in the record; COMPUTED here | Out [3] |
| $w_{\rm eff}(A, B) = X/E$, $w_{\rm eff}(C) = X/E - 1$ from the dilution | to $1.7 \times 10^{-8}$ | PROVED in the record; COMPUTED here | Out [3] |
| $X/E$ of the gas, all series | 0.292893 to 0.328105, rising | COMPUTED (record) | Out [3] |
| $w_{\rm eff}(C)$ of the gas | $-0.707107$ to $-0.671895$ | COMPUTED; rests on the ASSUMED definition C | Out [3] |
| tangent $w_a$ of the gas | $-0.020523$ to $-0.008894$ | COMPUTED (record) | Out [4] |
| bulk-band level, $w_{\rm eff}(A)$ | 0.239626 to $2.268 \times 10^{-3}$ | COMPUTED (record) | Out [5] |
| condensate ratio at $u = -382/441$ | $-0.764$ exactly | PROVED; $u$ CHOSEN | Out [6] |
| gas plus condensate, $w_0(C) = -0.861$ | share 0.436703, $w_a = 0.067014$ | COMPUTED; share CHOSEN | Out [7] |
| M2, M3, M4 tangents | $w_a = 0.162074$, $-0.393926$, $-0.600$ | PROVED (record); parameters CHOSEN | Out [8] |
| M5 fit over $1/2 \le a \le 1$ | $(-0.861, -0.600)$ | by construction | Out [8] |
| M5 crossing of $-1$ | $a = 0.77909966367$ (B: 0.77905405) | COMPUTED; needs the ghost-like part | Out [8] |

**What the results mean.** The equations of state that the record finds follow from two things: which quanta are present, and which definition of $\rho_4$ the observer uses. Neither is fixed by the field equations of the record. Under A and B the theory contains radiation-like content (the computed gas) and dark-matter-like content (the bulk band of dirac16complex, the good-sector gas of dirac16complex00), but the computed states of dirac16complex are only of the first kind. Under C the same content reads like dark energy: the gas between $-0.71$ and $-0.67$, a condensate at $-1$. The observed values are reached only by tuning as many parameters as numbers, and the crossing of $-1$ only with a component of negative energy. Neither hypothesis is established, and neither is refuted: what the record rules out, under its stated assumptions, is that the computed states of dirac16complex give the observed pair, and that any positive-energy content of dirac16complex00 crosses $-1$ (within the adiabatic model).

**Why it is hard.** The observer's $\rho_4$ needs a physical argument, not a choice: how a 4-dimensional observer measures energy when three time-like directions shrink. The populations need a dynamical origin: which quanta the early universe made, which is the time-dependent problem (Problem 2) and, beyond it, the creation question (Problem 1). The equation of state must come from the coupled equations, which brings back the back-reaction (Problem 3): no computed Kohn-Sham state is an admissible source of the author's metric. And the ghost-like and growing modes of dirac16complex00 make its classical energy unbounded below and its initial-value problem ill-posed (Chapter 8).

**What remains OPEN** (the record's own list, `Revision/docs/DARK_SECTOR_HYPOTHESES.md`, section 10):

1. a self-consistent history $a_4(x_4)$ with an admissible source (no recorded Kohn-Sham state is one; the condensate is an exact source only on the linear member);
2. populated bulk-band or thermal states along the history; only $T = 0$ ground states and $0 \le a_4 \le 2$ are computed;
3. modes of dirac16complex with extra-time momentum (outside the good sector), and the non-adiabatic Kohn-Sham problem;
4. for dirac16complex00: sources that depend on $x_8$, the frozen warp of the adiabatic model, the growing modes, a quantum treatment;
5. which normalisation of $\rho_4$, if any, describes a physical 3-space observer, and the value of $a_{4,\rm today}$;
6. what would select the populations of M2 to M5, the mixture shares or the condensate's $u$;
7. a supernova likelihood (distances, covariances): no fit to data is part of the record.

**A first step.** (a) Redo the derivations of Sections 22.17 to 22.19 by hand, then change one assumption at a time in Notebook 22b: take today at $a_{4,\rm today} = 1$ instead of 2 in In [7], or remove the ghost-like part of M5 in In [8] and watch its crossing of $-1$ disappear (Exercise 14 shows why). (b) Write down a physical model of the observer: for example a 4-dimensional brane-world observer whose energy is the integral over the extra times with a weight derived from the metric, and find which $s$ of Section 22.17 it gives. (c) Populate the bulk band thermally along the history (fixed entropy) with the Kohn-Sham solver of Chapter 15 and compute $X/E$; this is the record's open item 2.

**Where to start.** These files of the repository:

- the folder `Revision/dark_sector/dirac16complex` with its README, its four scripts in the subfolders `derive`, `compute` and `independent`, and its outputs and reports;
- the folder `Revision/dark_sector/dirac16complex00` with its README, its two implementations in the subfolder `python`, the model record `eos-theory.json`, and its results and reports;
- the document `Revision/docs/DARK_SECTOR_HYPOTHESES.md`, which states every result with its record;
- the builder of Notebook 22b, `Revision/textbook/notebooks/src/22b_dark_sector.py`.

### 22.25 Problem 6: matter and antimatter

**The question.** The universe we observe contains matter and almost no antimatter (Chapter 21 teaches the observations and the measured baryon-to-photon ratio from zero). The author asked that this theory solve the matter-antimatter mysteries. The open problem is whether an extension of the theory could produce the observed excess of matter from a start without excess, and with the measured size.

**What is known.**

- PROVED: the LOCAL conservation law $\partial_\mu(\cos z\,J^\mu) = 0$ of the U(1) current holds on every solution in the author's metric, for every history $a_4(x_4)$ (`Revision/lead_checks/reports/charge-conjugation-and-u1.json`, check `u1_noether_matrix_identity`). It says that charge is neither made nor destroyed at any point: the charge $Q = \int\cos z\,\Psi^\dagger B\Psi\,d^7x$ of a slice changes only by the flux of $\cos z\,J^\mu$ through the boundary of the slice. NOT proved: that the total charge of one universe is constant. That needs no flux through the brane $z = \pi/2$, a boundary condition that the record does not impose: wherever it is used it is ASSUMED, and whether it holds is OPEN, part of the junction conditions of Problem 4 (Sections 10.2, 18.21 and 21.18 show exact solutions whose charge changes by exactly this flux). Hence no net charge can be generated at any point inside one universe, and the total charge of one universe is constant if no charge flows through the brane.
- PROVED: the charge conjugations are matrices: $\mathcal{C}_+ = C$ (same mass) and $\mathcal{C}_- = \Gamma C$ (mass reversed) (checks `charge_conjugation_matrix_plus` and `charge_conjugation_matrix_minus` of the same report); for a real commuting field the current vanishes identically and $\mathcal{C}_+$ acts as the identity, so the nontrivial real map between matter and antimatter is the matrix $\Gamma$ with the mass reversed, which is T1 (check `real_fields_charge_conjugation`); for the quantised Grassmann field the conjugation that keeps the canonical anticommutator is $\Psi \to \Gamma\Psi^{\dagger T}$, which reverses the mass (check `quantum_charge_conjugation_unitary_type`). Chapters 5 and 21 derive all of this.
- PROVED: a T1 partner carries the opposite charge, so a T1 pair $\{+m, -m\}$ has total charge zero as classical bilinears (T1d, Chapter 18); for two universes that are quantised independently of each other there is no such cancellation (Q). The idea that our universe has a partner of opposite charge, an anti-universe, belongs to a class of ideas of which one published example is L. Boyle, K. Finn and N. Turok, Phys. Rev. Lett. 121, 251301 (2018). That our universe has such a partner is a HYPOTHESIS.
- The theory as built does NOT solve the matter-antimatter problem: it has no baryons, no process that violates baryon number, no violation of CP, and no computation of a departure from thermal equilibrium.

**What would be needed.** Sakharov's three conditions (Chapter 21) in an extended theory: processes that violate baryon number; violation of C and of CP; and a departure from thermal equilibrium; and then a computation of the excess that agrees with the measured baryon-to-photon ratio. Every scenario that adds these is a HYPOTHESIS until it is computed and checked.

**Why it is hard.** The U(1) symmetry of the theory is exact, so an asymmetry needs new terms in the Lagrangian, and with every new term the pairing theorems must be derived again (they hold for the Lagrangian of the record, not for an arbitrary extension). The field dirac16complex is not the field of the baryons of the Standard Model, so even a charge asymmetry of this field would still have to be connected to baryons. A departure from equilibrium needs the time-dependent dynamics of Problem 2, and a quantum computation of rates needs the Krein quantisation of Chapter 10 beyond the good sector.

**A first step.** (a) List the simplest terms that could be added to the Lagrangian and decide, with the exact matrix methods of the record (the solution of $M(\gamma^a)^* = \pm\gamma^aM$ in `Revision/lead_checks/charge_conjugation_and_u1.py` is the model), which of them break the U(1) and which of the discrete maps ($\mathcal{C}_+$, $\mathcal{C}_-$, $\Gamma$, the reflections) they respect. (b) For each such term, derive T1 again and state exactly how it changes. (c) Only then add a departure from equilibrium, with the time-dependent tools of Problem 2, and compute the charge produced from a symmetric start. Each of these steps is labelled HYPOTHESIS until it is done and checked.

**Where to start.** `Revision/lead_checks/charge_conjugation_and_u1.py` and its report; Chapters 5 and 21 and their notebooks; the pairing record `Revision/pairing/pairing-theory.json`.

### 22.26 Smaller open items

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
| a constant total U(1) charge: no flux of the current through the brane $z = \pi/2$ | ASSUMED where used; OPEN | `Revision/lead_checks/reports/charge-conjugation-and-u1.json` (the local law only); Sections 10.2, 18.21, 21.18 and 22.25 |

### 22.27 What we proved, what we computed, what we assumed

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
| $w(1) = w_0$, $w(0) = w_0 + w_a$; the CPL line crosses $-1$ at $a = 461/600$; $w < -1$ with $\rho > 0$ if and only if $\rho + p < 0$ | algebra, Section 22.16; `python-derive-eos.json`, `unite_crossing_point` |
| the proper 7-volume element is $\cos z$, independent of $a_4$; $dE/da_4 = -3X$ | `derivation-checks.json`, `proper_7_volume_element_independent_of_a4`, `integrated_identity_dE_da4`; Section 22.17 |
| $w_{\rm eff}(A) = w_{\rm eff}(B) = X/E$ and $w_{\rm eff}(C) = X/E - 1$ (in general $X/E - s$), for each stated definition of $\rho_4$ | `derivation-checks.json`, `w_eff_A_equals_X_over_E`, `w_eff_B_equals_w_eff_A`, `w_eff_C_equals_X_over_E_minus_1`, `w_eff_general_normaliser`; Section 22.17 |
| on the linear member $w_{\rm exp} = -1$; $w_{\rm eff}(C) < -1$ if and only if $X/E < 0$ | `derivation-checks.json`, `expansion_inferred_w`, `phantom_condition`; Section 22.17 |
| the flat-limit law $w_{\rm eff} = k^2/(3(M^2a^2 + k^2))$ of a massive quantum | `derivation-checks.json`, `massive_mode_w_eff_law`; Section 22.18 |
| the condensate: $X = 0$, $w_{\rm eff} = 0$ (A, B) and $-1$ (C); ratio $u/(2 + u)$, equal to $-0.764$ at $u = -382/441$, phantom exactly for $-2 < u < -1$ | `derivation-checks.json`, `condensate_w_eff`, `condensate_ratio_equal_unite_constant_w`; `python-derive-eos.json`, `condensate_phantom_interval`; Section 22.18 |
| radiation plus condensate: $w_a = r_0/(3(1 + r_0)^2) > 0$ (freezing) | `derivation-checks.json`, `mixture_radiation_condensate_cpl`, `mixture_C_matching_w0_unite`; Section 22.18 |
| dirac16complex00: modes of both energy signs at every real frequency; in the adiabatic model $\varepsilon_i \ge 0$, and with positive energies $w_{\rm eff}(C) \ge -1$; the tangents of M2, M3, M4 | `python-derive-eos.json`, `mode_krein_inertia_*`, `wkb_epsilon_sign_free`, `M2_tangent_exact`, `M3_tangent_exact`, `M4_tangent_equals_unite`; Section 22.19 |
| the LOCAL U(1) law $\partial_\mu(\cos z\,J^\mu) = 0$ (a constant total charge needs no flux through the brane: ASSUMED where used, OPEN), the charge-conjugation matrices, T1, T2, Q, T3 | Chapters 5, 10 and 18 to 21; `charge-conjugation-and-u1.json`, pairing and T3 reports; Section 22.25 |

**COMPUTED** (numerical, with measured accuracy): from the Revision record, $Q_{max} \le 0.0935$ for the 75 ground states at $A = 1$, the adiabatically continued state of $N = 696$ above the instantaneous ground state by up to $8.623$, the violations of the source conditions (ratios $2.09$ to $3.99$, closest integrated ratio $0.414$), and the agreement of $dE/da_4$ from finite differences and from the energy-momentum integral (for N688_lam0_a00, $-597.9157012757526$ against $-597.9157012806555$). In Notebook 22a (free field, the Fermi-shell sector of $N = 688$): the record's levels and $Q$ reproduced to $10^{-13}$; $G^* = 0.09979$ at $q^* = 2.128$; the strongest jump across the gap $0.0489$ per unit rate; $P = 0.0138$ at the peak rate 1; $A_{1/2} = 1.508$; the sudden limit $0.0749$ (span 0 to 2) and $0.1051$ (0 to 6); the breakdown estimates $10.701$, $10.021$, $2.929$ and $1.508$; with the errors of Section 22.13. From the dark-sector record (reproduced in Notebook 22b): the Kohn-Sham gas along the prescribed history, $X/E$ from 0.292893 to 0.328105 rising toward $1/3$, $w_{\rm eff}(C)$ from $-0.707107$ to $-0.671895$, tangent $w_a$ from $-0.020523$ to $-0.008894$, the energy balance on the data to $1.235 \times 10^{-7}$; the bulk-band level from 0.239626 to $2.268 \times 10^{-3}$; the computed mixture with $w_a = 0.067014$; the M5 fit, its crossing at $a = 0.7791$ and the field-equation implementation B (crossing $0.77905405$, agreement with A within 0.00083082726).

**ASSUMED**: the Z2 brane and the parities it gives; the good sector; the tip (CHOSEN); which levels count as particles (CONVENTION); the history $a_4 = AHx_4$ (PRESCRIBED BACKGROUND); in Notebook 22a the free field ($\lambda = 0$) and one sector; the observer's density $\rho_4$ (definitions A, B, C) and the value of $a_{4,\rm today}$; the adiabatic (WKB) model of dirac16complex00, an APPROXIMATION measured by implementation B; every parameter labelled CHOSEN in Sections 22.18 and 22.19 (several of them chosen to reproduce the observed values, so that those matches are NOT predictions); the no-flux condition at the brane wherever a constant total U(1) charge is used; the expansion in instantaneous orbitals, truncated to 20 levels with its convergence measured; the first-order approximations of Sections 22.7 and 22.8, whose range of validity the notebook measures.

**HYPOTHESIS**: the author's dark-sector hypotheses (investigated by the record, established in neither form; the ghost-like component of M5 is not an established physical state); that our universe has a partner of opposite charge; every scenario of creation or of matter-antimatter asymmetry; the generalised metric of Section 22.14 and the reduced quantum model of Section 22.4 as useful next steps.

**OPEN**: whether any universe is created, in pairs or otherwise (no creation process, rate, amplitude or big-bang dynamics follows from the equations); the time-dependent Kohn-Sham problem with interaction; the reading of jumps into the negative branch; relaxation through Fermi-level crossings; the back-reaction of the gas on $a_4$; the junction conditions of the brane; which definition of $\rho_4$ describes a physical 3-space observer; populated bulk-band or thermal states; what selects the populations of the dark-sector models; a fit to supernova data; whether the total U(1) charge of one universe is constant (no flux through the brane); an asymmetry between matter and antimatter in an extended theory; the extra-time modes beyond the good sector.

### 22.28 Exercises

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

**Exercise 11.** (a) The gas N688_lam0 has $X/E = 0.3183$ at $a_4 = 2$ (Out [3]). Give its $w_{\rm eff}$ under the definitions A, B and C, and under the general normalisation of Section 22.17 with $s = 1/2$. (b) Show from $dE/da_4 = -3X$ that a state with $X = E/3$ at every time has $E \propto e^{-a_4}$, and that under A its density thins out like $a^{-4}$. (c) What does a condensate give under C, and why?

*Answer.* (a) Under A and B, $w_{\rm eff} = X/E = 0.3183$; under C, $0.3183 - 1 = -0.6817$; with $s = 1/2$, $0.3183 - 0.5 = -0.1817$. The same state gives three different readings: only the ASSUMED normalisation changed. (b) With $X = E/3$ the balance reads $dE/da_4 = -E$; the function whose derivative is minus itself is $E = E_0e^{-a_4}$ (check: $d(E_0e^{-a_4})/da_4 = -E_0e^{-a_4}$). Under A, $\rho_4 \propto E\,e^{-3a_4} = E_0e^{-4a_4}$, and since $a = e^{a_4 - a_{4,\rm today}}$, $e^{-4a_4} \propto a^{-4}$: radiation, $w = 1/3$. (c) A condensate has $X = 0$, so $dE/da_4 = 0$ and $E$ is constant; under C, $\rho_4 \propto E$ is constant, and $w_{\rm eff} = -1 - \frac13 \cdot 0 = -1$: it reads like a cosmological constant (under A and B, $\rho_4 \propto e^{-3a_4} \propto a^{-3}$, like dust).

**Exercise 12.** For a massive quantum in the flat limit with $M = 1$ and $k = 1$, compute $w_{\rm eff}(A) = k^2/(3(M^2a^2 + k^2))$ at $a = 0.1$, 1 and 10, the same values under C, and the CPL tangent at $a = 1$ under C. Is it thawing or freezing?

*Answer.* $w_{\rm eff}(A) = 1/(3(a^2 + 1))$: at $a = 0.1$, $1/(3 \cdot 1.01) = 0.330033$; at $a = 1$, $1/6 = 0.166667$; at $a = 10$, $1/(3 \cdot 101) = 0.003300$. It falls from radiation toward dust: the dark-matter-like law. Under C: $-0.669967$, $-0.833333$, $-0.996700$. The derivative is $dw/da = -2a/(3(a^2 + 1)^2)$, at $a = 1$ equal to $-2/12 = -1/6$, so $w_0 = -0.833333$ under C and $w_a = -dw/da = +0.166667$ in every definition: freezing (it moves toward $-1$ as $a$ grows). This is why the bulk band, even if it were populated, would not give the observed thawing slope under C.

**Exercise 13.** The record mixes the computed gas ($X/E = 0.3182941676741$ at $a_4 = 2$) with a condensate so that $w_{\rm eff}(C) = -0.861$ today. (a) Compute the gas share of the energy today. (b) For an exactly radiation-like gas ($X/E = 1/3$) the same condition gives $r_0 = 417/583$; what is the gas share then? (c) Why does the computed gas need the larger share?

*Answer.* (a) The condensate adds energy but no $X$, so $w_{\rm eff}(C) = \text{share} \cdot X/E - 1$; setting this to $-0.861$ gives $\text{share} = 0.139/0.3182941676741 = 0.436703$ (Out [7]). (b) With $X/E = 1/3$: $\text{share} = 3 \cdot 0.139 = 0.417$, and indeed $r_0/(1 + r_0) = (417/583)/(1000/583) = 417/1000$. (c) The computed gas has $X/E = 0.3183$, a little below $1/3$, so it contributes less $X$ per unit energy, and a larger share of it is needed to reach the same $0.139$. In both cases the share is CHOSEN, and the slope comes out positive ($0.067014$ and $0.081037$): freezing, not the observed $-0.60$.

**Exercise 14.** Two components of an adiabatic gas of dirac16complex00 have the energy densities $\rho_1 = 0.7$, $\rho_2 = 0.3$ and the values $\varepsilon_1 = 0$ (a condensate), $\varepsilon_2 = 0.5$ (an extra-time mode). (a) Compute $w_{\rm eff}(C) = \sum_i\varepsilon_i\rho_i/\sum_i\rho_i - 1$. (b) Replace them by $\rho_1 = 1.3$, $\varepsilon_1 = 0$ and a ghost-like component $\rho_2 = -0.3$, $\varepsilon_2 = 1/3$ (the total is again 1); compute $w_{\rm eff}(C)$. (c) Explain with these numbers why a crossing of $-1$ needs a component of negative energy.

*Answer.* (a) $(0 \cdot 0.7 + 0.5 \cdot 0.3)/(0.7 + 0.3) - 1 = 0.15 - 1 = -0.85$. (b) $(0 \cdot 1.3 + \frac13 \cdot (-0.3))/(1.3 - 0.3) - 1 = -0.1 - 1 = -1.1$: below $-1$, phantom. (c) With positive weights $\rho_i$ the fraction is an average of the numbers $\varepsilon_i \ge 0$, so it lies between their smallest and largest value and cannot be negative: $w_{\rm eff}(C) \ge -1$. A negative weight breaks this rule: the "average" $-0.1$ lies outside the range of the $\varepsilon_i$ (0 to $1/3$). This is the theorem of Section 22.19, and it is why M5 crosses $-1$ only because of its ghost-like part, and why the record's M5 without that part does not cross at all (Out [8]). The size of the ghost share is a choice: the record notes that $G = 0.28$ would need $s = 0.726$ and $G = 0.24$ would need $s = 0.921$ (an exploration of the record, not a check), so nothing fixes it.
