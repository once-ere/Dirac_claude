## 20. Do universes come in pairs? What the equations prove and what they do not

The author asked for a proof "that Universes of masses {+mass, -mass} are created in pairs", for the fermion field dirac16complex and for the commuting field dirac16complex00, and the request for this book speaks of proving that "the big bang creates universes in pairs". This chapter answers the question of its title exactly. It collects what the equations of this book PROVE about pairs of universes (the pairing theorems T1, T2, Q and T3 and the corollary C1), proves the central steps again line by line, follows them through one exact solution, and then states, just as exactly, what the equations do NOT prove: that any universe is created, in pairs or otherwise. No creation process, no rate, no probability and no amplitude follows from these equations. The author's statement that the big bang creates universes in pairs therefore remains what it was, a HYPOTHESIS, and this chapter says precisely what a proof of it would still need.

### 20.1 What this chapter does, and why

**Why the question needs care.** A sentence like "the equations prove that universes come in pairs" can mean several very different things. It can mean that for every solution of the equations there is a partner solution (a statement about the set of all solutions); it can mean that whenever one universe exists its partner exists too (a statement about what is realised); or it can mean that some process makes two universes at once out of something else (a statement about dynamics, with a rate or a probability). The first kind of statement can be proved from the field equations of this book, and it is proved. The second and the third cannot be proved from them, because these equations describe fields on a given gravitational background and contain no process that produces a universe. A student who confuses the three would believe that the theory has shown something it has not. This chapter therefore separates them carefully and gives every statement its status.

**The answer in brief.** Each item carries its status word (defined in Section 20.2).

1. PROVED (theorem T1, the chirality pairing): multiplying a field $\Psi$ by the chirality matrix $\Gamma$ turns every configuration of the theory with mass $m$ and coupling $\lambda$ into a configuration of the theory with $(-m, -\lambda)$, solutions into solutions, in every gravitational field, and reverses its energy-momentum tensor, its current and its charge. A T1 pair therefore has zero total energy, momentum, stress and charge at every point.
2. PROVED (theorem T2, the mirror pairing): the gamma matrix of the hidden direction together with the mirror $z \to \pi - z$ across the surface $z = \pi/2$ (an ASSUMED construction) turns a solution with $(-m, \lambda)$ into a solution with $(m, \lambda)$ with EQUAL, not opposite, energy and charge.
3. PROVED (the quantum reading Q, dirac16complex only): the T1 image is the same quantum system relabelled; two independently quantised universes of masses $+m$ and $-m$ have identical one-particle spectra (the $\lambda = 0$ spectra, in flat 4+4 space or in a general field at a point with frozen coefficients) and energies that add, not cancel.
4. PROVED (theorem T3, the Kohn-Sham level, dirac16complex): every self-consistent instantaneous Kohn-Sham state with $(m, \lambda)$ has a partner with $(-m, +\lambda)$ and equal energies (ASSUMED Z2 brane, transformed tip condition).
5. PROVED (corollary C1): a T1 pair taken as the only source of the author's metric is a zero source, and in Einstein gravity the author's metric then has no solution at all for $H > 0$.
6. COMPUTED in this chapter (Notebook 20b): one exact universe, a solution of the field equation and of all 64 Einstein equations together, that needs no partner; its T1 partner solves its own field equation but cannot be the source of the author's metric.
7. PROVED (the charge of a pair): a T1 partner carries the opposite charge, so a T1 pair has zero total charge; a T2 mirror copy carries the SAME charge. This does NOT solve the matter-antimatter problem: the theory as built has no baryons, no violation of baryon number, no violation of CP and no computed departure from equilibrium (Section 20.23).
8. NOT ESTABLISHED: that any universe is created; any creation process, rate, probability or amplitude; that a partner must exist.
9. HYPOTHESIS: "the big bang creates universes of masses $+M$ and $-M$ in pairs" (the author's statement).

T1, T2, Q, T3 and C1 are exact **maps between solution sets** and one consequence of them: they say which solutions exist if one solution exists. None of them is a statement that a universe comes into being.

**The plan.** Section 20.2 defines the words. Section 20.3 reads the request and the hypothesis word by word, and Section 20.4 separates the three questions hidden in it. Sections 20.5 and 20.6 state the pairing theorems and prove them line by line: this chapter gives the complete proofs of T1 and T2 (with the reflected-connection lemma) and the Krein-metric step of Q; the remaining steps of Q, which need the one-particle Hamiltonian of Chapter 10, are proved in Chapter 18, and T3, whose proof needs the Kohn-Sham blocks of Chapter 14, is proved in Chapter 19 (Section 20.6 outlines it). Section 20.7 proves the corollary C1, and Notebook 20a makes every step of it visible (Sections 20.8 to 20.11). Section 20.12 derives one exact universe of the theory, and Notebook 20b builds it and its partners (Sections 20.13 to 20.16). Section 20.17 shows, with the creation of an electron and a positron from light, what a proof of creation contains, and Notebook 20c computes it (Sections 20.18 to 20.21). Section 20.22 says what the conservation laws of this theory allow and forbid, Section 20.23 what pairs have to do with matter and antimatter, Section 20.24 lists what is not established, Section 20.25 what a calculation of creation would require, and Section 20.26 gives the answer to the question of the title. The chapter ends with the ledger "What we proved, what we computed, what we assumed" (Section 20.27) and with exercises and their complete answers (Section 20.28).

**The three worked examples.** Each is a complete Jupyter notebook; you may run them in any order. None of them needs Rust.

| notebook | what it computes | checks | figures |
| --- | --- | --- | --- |
| 20a | corollary C1 step by step: the spin connection on both patches, a configuration with its T1 partner and its T2 mirror copy, the vacuum equations of Einstein and Einstein-Lovelock gravity | 37 | 7 |
| 20b | one exact universe of the coupled equations with the deflating history, its T1 partner, the T1 pair and its T2 mirror copy | 25 | 4 |
| 20c | allowed is not the same as happens: the thresholds of electron-positron pair creation, and what the pairing record does not establish | 12 | 4 |

**The records this chapter uses.** Every formula and number comes from these Revision records or from the chapter's own notebooks, which reproduce the records where they overlap (each such check prints the record file and the check name).

| record | what it holds |
| --- | --- |
| `Revision/docs/PAIR_CREATION_PROOFS.md` | the Revision document of the pairing theorems, the corollary C1 and the list of what is not established |
| `Revision/pairing/pairing-theory.json` | T1, T2 and Q with hypotheses, statements, proofs, and the list `not_established` |
| `Revision/pairing/reports/wolfram-pairing.json` | the WolframScript verification of T1, T2 and Q (101 checks, all PASS) |
| `Revision/pairing/reports/python-pairing.json` | the independent sympy verification (66 checks, all PASS) |
| `Revision/pairing/kohn_sham/t3-theory.json` | theorem T3, its hypotheses and its own list of what it does not establish |
| `Revision/pairing/kohn_sham/reports/` | `wolfram-t3.json` (10 checks) and `python-t3.json` (13 checks), all PASS |
| `Revision/field_equations_a4/a4-equations.json` | the Lovelock tensors of the author's metric, the null combination and the vacuum factor |
| `Revision/field_equations_a4/reports/` | `python-a4-report.json` and `wolfram-a4-report.json`: the field equations for $a_4$; `ks-source-conditions.json`: the Kohn-Sham states as a source |
| `Revision/lead_checks/reports/` | the lead's independent checks `einstein-gauss-bonnet-a4.json`, `emt-divergence-and-spin-connection.json` and `charge-conjugation-and-u1.json` |
| `Revision/algebra/gammas.json` | the author's eight real $16 \times 16$ gamma matrices |

The counts in the table are those printed by Notebook 20a (In [2]) for the two pairing reports and those of the reports' own summaries for T3; a report is named below by its file name only, for example "`python-pairing.json`, check `gammas.Gamma`". Every check cited in this chapter has the verdict PASS.

**Notation.** The author's coordinates are $x_1, \dots, x_8$: $x_1, x_2, x_3$ are ordinary 3-space, which inflates (scale factor $e^{a_4}\sin^{1/6}z$); $x_4$ is the time; $x_5, x_6, x_7$ are the three EXTRA TIMES, time-like, which DEFLATE EXPONENTIALLY (scale factor $e^{-a_4}\sin^{1/6}z$, with $a_4$ increasing); $x_8$ is the hidden space direction, with $z = 6Hx_8$ between 0 and $\pi/2$ and $H > 0$ the author's constant. The metric is

$$
\begin{aligned}
ds^2 = {} & e^{2a_4}\sin^{1/3}z\,(dx_1^2 + dx_2^2 + dx_3^2) - dx_4^2 \\
& - e^{-2a_4}\sin^{1/3}z\,(dx_5^2 + dx_6^2 + dx_7^2) + \cot^2 z\,dx_8^2 ,
\end{aligned}
$$

with $a_4 = a_4(x_4)$ and $a_4' = da_4/dx_4$; its signature is (4,4) and $\sqrt{|g|} = \cos z$. The frame metric is $\eta = \mathrm{diag}(+1, +1, +1, -1, -1, -1, -1, +1)$ in the order $x_1, \dots, x_8$. The gamma matrix of the direction $x_a$ is $\gamma^{(x_a)}$, a real $16 \times 16$ matrix, with $\gamma^{(a)}\gamma^{(b)} + \gamma^{(b)}\gamma^{(a)} = 2\eta^{ab}I_{16}$. The **deflating history** is the linear member $a_4 = AHx_4$ with $A = 1$: 3-space grows like $e^{Hx_4}$ and the extra times shrink like $e^{-Hx_4}$.

### 20.2 The words of this chapter

- **Configuration**: a field $\Psi$ given by its 16 components at every point, whether or not it obeys the field equation. A statement that holds for every configuration holds **off shell**; one that holds only for solutions holds **on shell**.
- **Solution**: a configuration that obeys the field equation $\gamma^\mu D_\mu\Psi = (m + \lambda S)\Psi$, where $S = \bar\Psi\Psi$ and $\bar\Psi = \Psi^\dagger C$.
- **Universe of mass $m$** (the meaning used by the Revision record): a solution of one of the two fields with mass parameter $m$ and coupling $\lambda$ in the author's primordial gravitational field. It is NOT the total gravitational mass or energy of that universe.
- **Parameter set** $(m, \lambda)$: the mass and the coupling of the potential $U(S) = \frac{\lambda}{2}S^2$. The theory with $(m, \lambda)$ and the theory with $(-m, -\lambda)$ are two DIFFERENT theories: their Lagrangians are different functions of the field.
- **Map between solution sets**: a rule that takes EVERY solution of one theory to a solution of another theory (here: multiply the field by a fixed matrix, possibly together with a change of the coordinate $x_8$).
- **Partner**: the image of a solution under such a map. **T1 partner**: $\Gamma\Psi$ with $(-m, -\lambda)$ at the same point. **T2 mirror copy**: $\gamma^{(x_8)}\Psi$ placed at the mirror point $\pi - z$, with $(-m, \lambda)$.
- **Pair**: a solution together with one partner. A **T1 pair** has opposite energy-momentum tensors; a **T2 pair** has equal ones.
- **Chirality**: the product of all eight gammas in the record's order, $\Gamma = \gamma^{(x_8)}\gamma^{(x_1)}\cdots\gamma^{(x_7)}$, which equals the diagonal matrix $\mathrm{diag}(-I_8, I_8)$ (eight entries $-1$, then eight entries $+1$).
- **Charge matrix** $C = \gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)}$, which defines the adjoint $\bar\Psi = \Psi^\dagger C$; **Krein matrix** $B = -iC\gamma^{(x_4)}$.
- **Energy-momentum tensor** $T_{\mu\nu}$: the source of gravity, 64 numbers at every point. **Energy density** $\rho = -T^{x_4}{}_{x_4}$; **pressure** along a direction $\mu$: $p_\mu = T^\mu{}_\mu$ (no sum); $p_3$ for 3-space, $p_t$ for the extra times, $p_8$ for the hidden direction.
- **Current** $J^\mu = -i\bar\Psi\gamma^\mu\Psi$; **charge density** $J^{x_4} = \Psi^\dagger B\Psi$; **charge** $Q = \int\cos z\,\Psi^\dagger B\Psi\,d^7x$, the integral over the seven directions other than $x_4$.
- **Patch, mirror patch, brane**: $0 < z < \pi/2$ is the **patch**; the map $z \to \pi - z$ takes it to the **mirror patch** $\pi/2 < z < \pi$; the surface $z = \pi/2$ between them is the **brane**. Gluing the two patches at the brane is the **Z2 construction**; it is ASSUMED.
- **Einstein-Lovelock equations**: $\sum_{k=1}^{3}\alpha_kE_{(k)}{}^\mu{}_\nu + \Lambda\delta^\mu_\nu = \kappa T^\mu{}_\nu$, with the three Lovelock tensors $E_{(k)}$ (Chapter 12), couplings $\alpha_k$, the **cosmological constant** $\Lambda$ and the gravitational coupling $\kappa$. **Einstein gravity** is $\alpha_1 = 1$, $\alpha_2 = \alpha_3 = 0$; then $E_{(1)} = G$ is the Einstein tensor. **Einstein-Gauss-Bonnet gravity** is $\alpha_1 = 1$, $\alpha_3 = 0$.
- **Vacuum equations**: the field equations of gravity with zero source, $\sum_k\alpha_kE_{(k)}{}^\mu{}_\nu + \Lambda\delta^\mu_\nu = 0$. A **vacuum** is a solution of them.
- **Null combination** $\rho + p_8$: the energy density plus the pressure along $x_8$.
- **Corollary**: a statement that follows from a theorem in a few lines.
- **Process**: a solution of a dynamical equation that connects an initial state with a different final state. **Creation** of a universe: a process whose initial state has fewer universes than its final state.
- **Rate, probability, amplitude**: numbers that say how often a process happens; they come from a dynamical theory. An **amplitude** is the complex number whose squared modulus is a probability.
- **Cross section**: for a process in which a particle hits a target (for example a photon a nucleus), the effective area of the target that the particle must hit for the process to happen; the number of processes per unit time is the cross section times the number of incoming particles that cross a unit area per unit time. It is measured in units of area.
- **Bogoliubov coefficient**: in a quantum field on a gravitational field that changes in time, a number that says how much of a wave that oscillates with positive frequency at early times has turned into a wave of negative frequency at late times; its squared modulus is the mean number of particles created in that wave. It is the standard measure of particle creation by a changing background.
- **Vacuum decay**: the quantum transition of a state that has the lowest energy only among its neighbouring states (a **false vacuum**) into a state of still lower energy; its rate per unit volume is computed from the quantum theory.
- **Tunnelling**: a quantum transition through a region that the classical equations forbid (a **barrier**), with a small but nonzero probability; proposals in which a universe appears by tunnelling are of this kind (Section 20.25).
- **Wave function of the universe, path integral**: a wave function of the universe is a quantum state of the geometry together with the matter fields (Section 20.25); a path integral computes an amplitude by adding up one complex number for every history that connects the initial and the final state.
- **Allowed**: not forbidden by any conservation law. Allowed does NOT mean that the process happens, nor how often.
- **Conserved quantity**: a number whose value does not change in time for every solution.
- **Status words.** PROVED: an exact statement with a proof, verified by a named check of a Revision record or by an exact computation of this book's notebooks. COMPUTED: a floating-point result with its measured accuracy. ASSUMED: an assumption on which a result rests. HYPOTHESIS: a scientific conjecture that is not established. OPEN: a question that nobody has answered here.

### 20.3 The request and the hypothesis, read word by word

**The request.** The author's request, quoted from `Revision/README.md`: "PROVE that Universes of masses {+mass, -mass} are created in pairs for each case of the dirac16complex and the dirac16complex00 fields." The request for this book repeats it as "proving that the 'big bang' creates universes in pairs".

**The hypothesis.** We write it as one sentence and give it its status:

**Hypothesis P (the author's).** The big bang creates universes of masses $+M$ and $-M$ in pairs. Status: HYPOTHESIS.

The Revision record gives its answer to the request in its list of answers to the author of 2026-10-01 (`Revision/README.md`): the pairing theorems T1, T2, Q and T3 are proved, each under its stated hypotheses, and "that universes occur in pairs, or are created, is not proved: no creation process, rate or amplitude follows from these equations". This chapter explains why, word by word.

**"A universe of mass $M$."** In the record, $M$ (or $m$) is the mass parameter of the field in its Lagrangian. A universe of mass $m$ is a solution of the field equation with this parameter, in the author's gravitational field (Section 20.2). The sign of $m$ alone does not say which of two physically different kinds of universe one has: theorem T2 (Section 20.6) shows that the image of a solution with $(-m, \lambda)$ under the reflection of one space-like frame direction is a solution with $(m, \lambda)$ with the same energy-momentum tensor. So "$+M$" and "$-M$" are labels whose sign is tied to the orientation of a frame.

**"Created."** A creation is a process (Section 20.2): an equation whose solution starts with fewer universes and ends with more, or, in a quantum theory, a nonzero amplitude for the transition from a state with fewer universes to a state with more. The field equations of this book are equations for a field on a given gravitational background; they contain no term that turns "no universe" into "a universe". We return to this in Sections 20.22 and 20.25.

**"In pairs."** That the second universe is present together with the first one, and necessarily so. The pairing theorems say that the partner is a solution of the partner theory; they do not say that it is present (Section 20.4).

**"The big bang."** In cosmology the big bang is the hot, dense early phase from which the observed expansion started; in the classical solutions of Einstein's equations that describe it, the scale factor of space goes to zero at a finite time in the past, and the equations break down there (a **singularity**). What we can prove is narrower: the author's metric has no such moment wherever its history $a_4$ is regular. We prove it line by line, for any history $a_4$ that is finite with finite $a_4'$ and $a_4''$ at the time considered, on the patch $0 < z < \pi/2$; the prescribed deflating history is such a history at every finite time. Whether the equations of this book, solved together, produce a big-bang moment is a different question, and it is not decided (see the end of this paragraph).

$$
g_{x_1x_1} = g_{x_2x_2} = g_{x_3x_3} = e^{2a_4}\sin^{1/3}z,\qquad 0 < g_{x_1x_1} < \infty .
$$

The exponential of a finite number is finite and positive, and $0 < \sin z < 1$ on the patch, so $\sin^{1/3}z$ is positive and finite.

$$
g_{x_4x_4} = -1,\qquad g_{x_5x_5} = g_{x_6x_6} = g_{x_7x_7} = -e^{-2a_4}\sin^{1/3}z,\qquad -\infty < g_{x_5x_5} < 0 .
$$

The same rule with $-2a_4$ in the exponent.

$$
g_{x_8x_8} = \cot^2 z,\qquad 0 < g_{x_8x_8} < \infty ,
$$

because $\cot z = \cos z/\sin z$ is finite and positive for $0 < z < \pi/2$.

$$
\sqrt{|g|} = \cos z > 0 .
$$

This is the record's volume factor (`python-pairing.json`, check `geometry.brane_degenerate`, which also records that it and $g_{x_8x_8}$ vanish at the brane $z = \pi/2$, the edge of the patch). So at every finite time the metric is finite and non-degenerate at every point of the patch. Its curvature is finite as well: every component $R^{ab}{}_{cd}$ is a Laurent polynomial in $\cot z$ (a sum of powers $\cot^kz$ with whole, possibly negative, $k$) whose coefficients are polynomials in $H$, $a_4'$ and $a_4''$ (`python-a4-report.json`, checks `riemann_entries_laurent` and `mixed_riemann_free_of_warp_and_a4`), and such an expression is finite where $\cot z$ is finite and not zero. For the prescribed deflating history $a_4 = Hx_4$ the three numbers $a_4 = Hx_4$, $a_4' = H$ and $a_4'' = 0$ are finite at every finite time $x_4$, so the metric and its curvature are finite at every finite time on the patch; and its 3-space scale factor $e^{Hx_4}\sin^{1/6}z$ tends to zero only as $x_4 \to -\infty$, never at a finite time. Status: PROVED for the prescribed deflating history $a_4 = AHx_4$, and for any history whose $a_4$, $a_4'$ and $a_4''$ stay finite (derived here from the metric and the two record checks). The degenerate places of the metric are the edges of the patch, not a moment of time: the brane $z = \pi/2$ ($g_{x_8x_8} = 0$ and $\sqrt{|g|} = 0$) and the tip $z \to 0$.

What this proof does NOT show: that the equations of this book exclude a big-bang moment. It assumed that $a_4$, $a_4'$ and $a_4''$ are finite, and it says nothing about a history in which one of them becomes infinite at a finite time. The history used in this book is prescribed, not computed: the Kohn-Sham history $a_4 = AHx_4$ is a PRESCRIBED BACKGROUND, because the Kohn-Sham states violate the source conditions of the $a_4$ equations (`ks-source-conditions.json`, checks `ks_profiles_depend_on_x8` and `ks_history_is_a_prescribed_background`). And when the $a_4$ equations are solved with a given source, they can break down at a finite time: Chapter 12 integrates the evolution equation of Einstein-Gauss-Bonnet gravity with a given constant source and finds that the rate $a_4'$ reaches a critical value at a finite time $x_4^\star$, where $a_4''$ becomes infinite and no solution with a smooth $a_4'$ continues. The curvature contains $a_4''$ (for example the Einstein tensor component $G^{x_1}{}_{x_1} = -3a_4'^2 + a_4'' + 15H^2$, `a4-equations.json`, key `lovelockTensors`, entry `E1`, `x1x1`), so it becomes infinite there too: a singularity at a finite time. In Einstein gravity the record allows every history $a_4$ that has a continuous second derivative, each with the source that it requires (`a4-equations.json`, key `einstein`, entry `allowedA4`), so a history in which $a_4 \to -\infty$ at a finite time, that is in which the 3-space scale factor goes to zero, is not excluded either. So: the PRESCRIBED history contains no big-bang moment; whether the coupled equations of the fields and of $a_4$, solved together, contain one is not decided (OPEN).

### 20.4 Three questions: is it allowed, does it happen, how often?

The sentence "universes are created in pairs" packs three questions of very different kinds into one.

**Q1, allowed?** Do the conservation laws of the theory permit a transition from a state without universes (or with one) to a state with a pair? This question asks whether something FORBIDS the transition. It is answered by comparing the conserved quantities before and after.

**Q2, does it happen?** Is there a solution of the dynamical equations (the field equations of both members together with the gravitational field equations) that starts without the pair and ends with it? This is a question about dynamics.

**Q3, how often?** In a quantum theory: what is the amplitude of the transition, its probability, or the number of pairs made per unit time? Its answer is a number.

**Symmetry is not realisation.** A pairing theorem says: for every solution with mass $+m$ there is a solution with mass $-m$. It does not say that whenever the first is present, the second is present too. An everyday comparison makes the difference plain. The laws of mechanics do not change when everything is reflected in a mirror, so for every right hand that the laws allow, a left hand is allowed as well. That does not mean that every right hand comes with a left hand, still less that hands are created in right-left pairs. To go from "the partner is allowed" to "the partner is created together with the original" one needs an answer to Q2 or Q3.

**What the Revision record answers.** The pairing theorems T1, T2, Q and T3 answer none of the three questions directly: they are statements about the SETS of solutions of two theories. Q1 is answered in part in Section 20.22: the conservation laws of the theory forbid a T1 pair with nonzero member charges or momenta from appearing out of zero fields. Q2 and Q3 are not answered by any equation of the record: no creation process, rate or amplitude is derived (`pairing-theory.json`, list `not_established`, items "No creation process" and "No rate and no amplitude"). Notebook 20c shows on the creation of electron-positron pairs from light what an answer to Q1, Q2 and Q3 looks like when physics does have it.

### 20.5 What is proved (1): theorem T1, line by line

**Hypotheses** (`pairing-theory.json`, theorem T1). (H1) The gravitational field is any vielbein with any spin connection, in particular the canonical one of the author's metric; it is a fixed (test) background, NOT varied, and both members of the pair live in the SAME field. (H2) $\Psi$ has Grassmann components (dirac16complex) or commuting components (dirac16complex00); the map acts at the same point, with no change of coordinates. (H3) The potential is $U(S) = \frac{\lambda}{2}S^2$. (H4) The Lagrangian density, the field equation, the energy-momentum tensor and the current are

$$
\mathcal{L}_{m,\lambda}[\Psi] = \sqrt{|g|}\,\big[K - mS - \tfrac{\lambda}{2}S^2\big],\qquad K = \tfrac12\big(\bar\Psi\gamma^\mu D_\mu\Psi - (D_\mu\bar\Psi)\gamma^\mu\Psi\big),
$$

$$
E_{m,\lambda}[\Psi] = \gamma^\mu D_\mu\Psi - (m + \lambda S)\Psi ,
$$

$$
T_{\mu\nu} = \tfrac14\big(\bar\Psi\gamma_\mu D_\nu\Psi + \bar\Psi\gamma_\nu D_\mu\Psi - (D_\mu\bar\Psi)\gamma_\nu\Psi - (D_\nu\bar\Psi)\gamma_\mu\Psi\big) - g_{\mu\nu}\,\frac{\mathcal{L}}{\sqrt{|g|}},\qquad J^\mu = -i\bar\Psi\gamma^\mu\Psi ,
$$

with $D_\mu\Psi = \partial_\mu\Psi + \Omega_\mu\Psi$, $D_\mu\bar\Psi = \partial_\mu\bar\Psi - \bar\Psi\Omega_\mu$, $\Omega_\mu = \frac12\omega_{\mu ab}S^{ab}$, $S^{ab} = \frac14[\gamma^{(a)}, \gamma^{(b)}]$ and $\gamma^\mu = \gamma^{(\mu)}/f_\mu$ for the diagonal vielbein with the lengths $f_\mu$. (This $T_{\mu\nu}$ is the one of the pairing records; it is minus the tensor of the field-theory record. The pairing records write the current as $J^\mu = \bar\Psi\gamma^\mu\Psi$; this book uses the real current $J^\mu = -i\bar\Psi\gamma^\mu\Psi$ of the field-theory record and of `charge-conjugation-and-u1.json`, whose $x_4$ component is $\Psi^\dagger B\Psi$ with the Hermitian matrix $B$. Every statement below is linear in $T$ and in $J$, so neither the sign convention of $T$ nor the factor $-i$ of $J$ matters.)

**Statement** (theorem T1).

- (T1a) $\mathcal{L}_{m,\lambda}[\Gamma\Psi] = -\mathcal{L}_{-m,-\lambda}[\Psi]$ off shell; separately $S[\Gamma\Psi] = S[\Psi]$ and $K[\Gamma\Psi] = -K[\Psi]$.
- (T1b) $E_{-m,-\lambda}[\Gamma\Psi] = -\Gamma E_{m,\lambda}[\Psi]$: $\Psi$ solves the $(m, \lambda)$ equation exactly when $\Gamma\Psi$ solves the $(-m, -\lambda)$ equation.
- (T1c) $T^{(-m,-\lambda)}_{\mu\nu}[\Gamma\Psi] = -T^{(m,\lambda)}_{\mu\nu}[\Psi]$ and $J^\mu[\Gamma\Psi] = -J^\mu[\Psi]$ at every point, off and on shell.
- (T1d) The pair has $T + T' = 0$, $J + J' = 0$ and $Q + Q' = 0$, as classical bilinears.

**Proof, step 1: the chirality anticommutes with every gamma.** Take one direction $b$ and move $\gamma^{(b)}$ from the left of $\Gamma$ to its right:

$$
\gamma^{(b)}\Gamma = \gamma^{(b)}\gamma^{(x_8)}\gamma^{(x_1)}\cdots\gamma^{(x_7)} = (-1)^7\,\gamma^{(x_8)}\gamma^{(x_1)}\cdots\gamma^{(x_7)}\gamma^{(b)} = -\Gamma\gamma^{(b)} .
$$

On its way $\gamma^{(b)}$ passes the eight factors of $\Gamma$: seven of them belong to other directions and each exchange gives a factor $-1$ (the Clifford relation $\gamma^{(a)}\gamma^{(b)} = -\gamma^{(b)}\gamma^{(a)}$ for $a \neq b$); one of them is $\gamma^{(b)}$ itself, which commutes with itself.

**Step 2: the chirality commutes with $C$, with every $S^{ab}$ and with every $\Omega_\mu$.**

$$
\Gamma C = \Gamma\gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)} = (-1)^4\,\gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)}\Gamma = C\Gamma .
$$

Step 1 was applied four times, once for each factor of $C$. In the same way $\Gamma S^{ab} = S^{ab}\Gamma$ (two factors, $(-1)^2 = 1$), and therefore $\Gamma\Omega_\mu = \Omega_\mu\Gamma$, because $\Omega_\mu$ is a sum of numbers times the $S^{ab}$.

**Step 3: the covariant derivative commutes with $\Gamma$.**

$$
D_\mu(\Gamma\Psi) = \partial_\mu(\Gamma\Psi) + \Omega_\mu\Gamma\Psi = \Gamma\partial_\mu\Psi + \Gamma\Omega_\mu\Psi = \Gamma D_\mu\Psi .
$$

$\Gamma$ is a constant matrix, so it comes out of the derivative; step 2 moved it past $\Omega_\mu$.

**Step 4: the adjoint of the partner.** $\Gamma = \mathrm{diag}(-I_8, I_8)$ is real and symmetric, so $\Gamma^\dagger = \Gamma$ and $\Gamma^2 = I_{16}$ (`python-pairing.json`, check `gammas.Gamma`).

$$
\overline{\Gamma\Psi} = (\Gamma\Psi)^\dagger C = \Psi^\dagger\Gamma^\dagger C = \Psi^\dagger\Gamma C = \Psi^\dagger C\Gamma = \bar\Psi\Gamma .
$$

The rules used, in order: the definition of the adjoint; $(M\Psi)^\dagger = \Psi^\dagger M^\dagger$; $\Gamma^\dagger = \Gamma$; step 2. In the same way $D_\mu(\bar\Psi\Gamma) = \partial_\mu\bar\Psi\,\Gamma - \bar\Psi\Gamma\Omega_\mu = (D_\mu\bar\Psi)\Gamma$.

**Step 5: the scalar is unchanged, the kinetic term changes sign.**

$$
S[\Gamma\Psi] = \bar\Psi\Gamma\,\Gamma\Psi = \bar\Psi\Psi = S[\Psi] .
$$

Step 4 and $\Gamma^2 = I_{16}$. For the kinetic term, every $\gamma^\mu = \gamma^{(\mu)}/f_\mu$ is a number times one gamma, so by step 1 $\Gamma\gamma^\mu\Gamma = -\gamma^\mu\Gamma\Gamma = -\gamma^\mu$, and with steps 3 and 4

$$
\overline{\Gamma\Psi}\,\gamma^\mu D_\mu(\Gamma\Psi) = \bar\Psi\,\Gamma\gamma^\mu\Gamma\,D_\mu\Psi = -\bar\Psi\gamma^\mu D_\mu\Psi ,\qquad \big(D_\mu\overline{\Gamma\Psi}\big)\gamma^\mu\Gamma\Psi = -(D_\mu\bar\Psi)\gamma^\mu\Psi .
$$

Both terms of $K$ change sign, so $K[\Gamma\Psi] = -K[\Psi]$.

**Step 6: the Lagrangian (T1a).**

$$
\mathcal{L}_{m,\lambda}[\Gamma\Psi] = \sqrt{|g|}\,\big[-K - mS - \tfrac{\lambda}{2}S^2\big] = -\sqrt{|g|}\,\big[K - (-m)S - \tfrac{(-\lambda)}{2}S^2\big] = -\mathcal{L}_{-m,-\lambda}[\Psi] .
$$

The first equality inserts step 5; the second takes out the factor $-1$ and writes $+m = -(-m)$ and $+\lambda = -(-\lambda)$; the third is the definition of $\mathcal{L}$ with the parameters $(-m, -\lambda)$.

**Step 7: the field equation (T1b).**

$$
E_{-m,-\lambda}[\Gamma\Psi] = \gamma^\mu D_\mu(\Gamma\Psi) - (-m - \lambda S)\Gamma\Psi = -\Gamma\gamma^\mu D_\mu\Psi + (m + \lambda S)\Gamma\Psi = -\Gamma E_{m,\lambda}[\Psi] .
$$

The first equality is the definition of $E$ with the parameters $(-m, -\lambda)$ and $S[\Gamma\Psi] = S$; the second uses step 3 and then step 1 to move $\Gamma$ to the left; the third takes out $-\Gamma$. Since $\Gamma$ is invertible, the left side vanishes exactly when $E_{m,\lambda}[\Psi]$ does.

**Step 8: the energy-momentum tensor and the current (T1c).** Each of the four kinetic terms of $T_{\mu\nu}$ has one gamma between $\bar\Psi$ and $\Psi$ and changes sign exactly as in step 5. The last term changes sign by step 6 with the parameters exchanged, $\mathcal{L}_{-m,-\lambda}[\Gamma\Psi] = -\mathcal{L}_{m,\lambda}[\Psi]$. Hence $T^{(-m,-\lambda)}_{\mu\nu}[\Gamma\Psi] = -T^{(m,\lambda)}_{\mu\nu}[\Psi]$. For the current,

$$
J^\mu[\Gamma\Psi] = -i\bar\Psi\Gamma\gamma^\mu\Gamma\Psi = +i\bar\Psi\gamma^\mu\Psi = -J^\mu[\Psi] ,
$$

by step 4 and step 1; integrating its $x_4$ component gives $Q[\Gamma\Psi] = -Q[\Psi]$.

**Step 9: the pair and the statistics (T1d).** Adding (T1c) to the quantities of $\Psi$ gives $T + T' = 0$, $J + J' = 0$ and $Q + Q' = 0$. $\Gamma$ multiplies each component by $+1$ or $-1$ and never reorders two Grassmann numbers, so steps 1 to 8 hold word for word for anticommuting components. Nothing in the proof used the form of the vielbein or of the connection, so it holds in every gravitational field. QED.

**Records.** The Wolfram pairing report has 51 checks of T1, in the author's field, in a general diagonal field and in a general field at one point, for both statistics. The sympy pairing report has 23 more, written independently. Examples, one per line:

| statement | report | check |
| --- | --- | --- |
| steps 1 and 2 | `wolfram-pairing.json` | `Gamma_properties` |
| (T1a), commuting field | `wolfram-pairing.json` | `T1_Lagrangian_primordial_commuting` |
| (T1c), the tensor | `wolfram-pairing.json` | `T1_energy_momentum_primordial_commuting` |
| (T1c), the current | `wolfram-pairing.json` | `T1_current_primordial_commuting` |
| step 5, the scalar | `python-pairing.json` | `T1.metric.commuting.S_invariant` |
| (T1b) | `python-pairing.json` | `T1.metric.commuting.euler_lagrange_map` |
| (T1d), commuting field | `python-pairing.json` | `T1.metric.commuting.pair_total_emt_zero` |
| (T1d), Grassmann field | `python-pairing.json` | `T1.metric.grassmann.pair_total_emt_zero` |

Notebook 20a reproduces T1 at a point of the deflating history (In [7]) and along the hidden direction (In [9]). The complete proof, with the four matrix lemmas behind steps 1 to 4 checked exactly, is in Chapter 18.

**What T1 is and what it is not.** It is not a symmetry of ONE theory: it changes the parameters and the sign of the action, and for $\lambda \neq 0$ it pairs $(m, \lambda)$ with $(-m, -\lambda)$, not $+m$ with $-m$ at the same coupling (for $\lambda = 0$ it pairs $+m$ with $-m$ exactly). Both the mass and the coupling must change sign: the negative controls $\mathcal{L}_{m,\lambda}[\Gamma\Psi] + \mathcal{L}_{-m,\lambda}[\Psi] \neq 0$ and $\mathcal{L}_{m,\lambda}[\Gamma\Psi] + \mathcal{L}_{m,\lambda}[\Psi] \neq 0$ are recorded (`python-pairing.json`, check `T1.metric.commuting.negative_controls`). The partner has $\rho' = -\rho$ and $p_\mu' = -p_\mu$, so every equation-of-state ratio $w = p/\rho$ is the same for both members.

### 20.6 What is proved (2): theorem T2, the quantum reading Q and theorem T3

**Theorem T2 (the mirror pairing).** Hypotheses (`pairing-theory.json`, theorem T2): $n$ is a space-like frame direction ($x_1$, $x_2$, $x_3$ or $x_8$); in a general field the frame is reflected, $e' = R_ne$, where $R_n$ is the $8 \times 8$ diagonal matrix with $-1$ in place $n$ (this is the same metric, because $R_n\eta R_n = \eta$), and $\Psi' = \gamma^{(n)}\Psi$ at the same point; in the author's field the reflection of $x_8$ is the mirror $x_8 \to \pi/(6H) - x_8$, that is $z \to \pi - z$, across the brane, with the ASSUMED Z2 construction; both statistics; $U(S) = \frac{\lambda}{2}S^2$. Statement: $\mathcal{L}_{m,\lambda}[\gamma^{(n)}\Psi; R_ne] = +\mathcal{L}_{-m,\lambda}[\Psi; e]$; $S' = -S$; $\Psi$ solves the $(-m, \lambda)$ equation exactly when its image solves the $(m, \lambda)$ equation; in the author's field the image carries, at the mirror point, the pulled-back tensor $T' = R_8TR_8$ and the current $J' = R_8J$: the energy density and the charge are EQUAL, not opposite.

The proof, derived here line by line. First, the charge matrix obeys $C\gamma^{(n)}C^{-1} = -(\gamma^{(n)})^T$ (Chapter 5), that is $(\gamma^{(n)})^TC = -C\gamma^{(n)}$, so

$$
\overline{\gamma^{(n)}\Psi} = \Psi^\dagger(\gamma^{(n)})^TC = -\Psi^\dagger C\gamma^{(n)} = -\bar\Psi\gamma^{(n)} .
$$

The first equality uses that $\gamma^{(n)}$ is real, so $(\gamma^{(n)})^\dagger = (\gamma^{(n)})^T$; the second is the relation just quoted. Then

$$
S[\gamma^{(n)}\Psi] = -\bar\Psi\gamma^{(n)}\gamma^{(n)}\Psi = -\eta_{nn}S[\Psi] = -S[\Psi] ,
$$

because $(\gamma^{(n)})^2 = \eta_{nn}I_{16}$ and $\eta_{nn} = +1$ for a space-like $n$. Second, in the reflected frame the curved gammas are $\gamma'^\mu = \gamma^{(\mu)}/f_\mu$ for $\mu \neq n$ and $-\gamma^{(n)}/f_n$ for $\mu = n$. Moving $\gamma^{(n)}$ through them,

$$
\gamma^{(n)}\gamma'^\mu\gamma^{(n)} = -\eta_{nn}\gamma^\mu \quad\text{for every }\mu ,
$$

because for $\mu \neq n$ one exchange gives $-1$ and $(\gamma^{(n)})^2 = \eta_{nn}$, and for $\mu = n$ the sign of the reflected frame gives the $-1$. Third, the covariant derivative of the image in the reflected frame is the image of the covariant derivative, $D'_\mu(\gamma^{(n)}\Psi) = \gamma^{(n)}D_\mu\Psi$ (the reflected-connection lemma). Its proof, line by line ($(\gamma^{(n)})^{-1} = \eta_{nn}\gamma^{(n)}$, because $(\gamma^{(n)})^2 = \eta_{nn}I_{16}$):

1. For $a \neq n$, $\gamma^{(n)}\gamma^{(a)}(\gamma^{(n)})^{-1} = -\gamma^{(a)}$ (one exchange); for $a = n$ it is $+\gamma^{(n)}$. Both cases together: $\gamma^{(n)}\gamma^{(a)}(\gamma^{(n)})^{-1} = -(R_n)^a{}_a\gamma^{(a)}$, since $(R_n)^a{}_a$ is $-1$ for $a = n$ and $+1$ otherwise.
2. $S^{ab} = \frac14(\gamma^{(a)}\gamma^{(b)} - \gamma^{(b)}\gamma^{(a)})$ contains two gammas, and inserting $(\gamma^{(n)})^{-1}\gamma^{(n)} = I_{16}$ between them gives $\gamma^{(n)}S^{ab}(\gamma^{(n)})^{-1} = (-1)^2(R_n)^a{}_a(R_n)^b{}_bS^{ab}$ (no sum), that is, $S^{ab}$ for $a, b \neq n$ and $-S^{ab}$ when exactly one of $a, b$ is $n$.
3. The reflected frame $e' = R_ne$ is the old frame with one leg reversed, by a constant matrix; its spin connection is therefore $\omega'_{\mu ab} = (R_n)^a{}_a(R_n)^b{}_b\,\omega_{\mu ab}$ (no sum): the components with exactly one index $n$ change sign, the others do not.
4. So in $\Omega'_\mu = \frac12\omega'_{\mu ab}S^{ab}$ each term carries the same sign as in line 2: $\Omega'_\mu = \gamma^{(n)}\Omega_\mu(\gamma^{(n)})^{-1}$.
5. Hence $D'_\mu(\gamma^{(n)}\Psi) = \partial_\mu(\gamma^{(n)}\Psi) + \gamma^{(n)}\Omega_\mu(\gamma^{(n)})^{-1}\gamma^{(n)}\Psi = \gamma^{(n)}(\partial_\mu\Psi + \Omega_\mu\Psi) = \gamma^{(n)}D_\mu\Psi$, because $\gamma^{(n)}$ is a constant matrix. In the same way $D'_\mu(\overline{\gamma^{(n)}\Psi}) = -(D_\mu\bar\Psi)\gamma^{(n)}$.

Hence

$$
\overline{\gamma^{(n)}\Psi}\,\gamma'^\mu D'_\mu(\gamma^{(n)}\Psi) = -\bar\Psi\,\gamma^{(n)}\gamma'^\mu\gamma^{(n)}\,D_\mu\Psi = \eta_{nn}\,\bar\Psi\gamma^\mu D_\mu\Psi ,
$$

so $K' = K$ for a space-like $n$, while $S' = -S$. Inserting both into the Lagrangian,

$$
\mathcal{L}_{m,\lambda}[\Psi'; e'] = \sqrt{|g|}\,\big[K - m(-S) - \tfrac{\lambda}{2}(-S)^2\big] = \sqrt{|g|}\,\big[K - (-m)S - \tfrac{\lambda}{2}S^2\big] = \mathcal{L}_{-m,\lambda}[\Psi; e] ,
$$

where the middle step uses $(-S)^2 = S^2$: the mass changes sign, the coupling does not, and the Lagrangian keeps its sign. The field equation follows in the same way. Multiplying $\gamma^{(n)}\gamma'^\mu\gamma^{(n)} = -\eta_{nn}\gamma^\mu$ on the left by $(\gamma^{(n)})^{-1} = \eta_{nn}\gamma^{(n)}$ gives $\gamma'^\mu\gamma^{(n)} = -\gamma^{(n)}\gamma^\mu$ (because $\eta_{nn}^2 = 1$), so, with $S' = -S$ and the lemma,

$$
E'_{m,\lambda}[\gamma^{(n)}\Psi] = \gamma'^\mu\gamma^{(n)}D_\mu\Psi - (m - \lambda S)\gamma^{(n)}\Psi = -\gamma^{(n)}\big[\gamma^\mu D_\mu\Psi - (-m + \lambda S)\Psi\big] = -\gamma^{(n)}E_{-m,\lambda}[\Psi] ,
$$

and since $\gamma^{(n)}$ is invertible, the image solves the $(m, \lambda)$ equation exactly when $\Psi$ solves the $(-m, \lambda)$ equation. For the current, with the adjoint $\overline{\gamma^{(n)}\Psi} = -\bar\Psi\gamma^{(n)}$ found first and $\gamma^{(n)}\gamma'^\mu\gamma^{(n)} = -\gamma^\mu$ for a space-like $n$,

$$
J'^\mu = -i\,\overline{\gamma^{(n)}\Psi}\,\gamma'^\mu\gamma^{(n)}\Psi = +i\,\bar\Psi\,\gamma^{(n)}\gamma'^\mu\gamma^{(n)}\,\Psi = -i\bar\Psi\gamma^\mu\Psi = J^\mu ;
$$

each kinetic term of $T_{\mu\nu}$ is unchanged in the same way (with the lemma for the derivatives), and so is $\mathcal{L}/\sqrt{|g|}$ by the Lagrangian line, so $T'_{\mu\nu} = T_{\mu\nu}$ in the reflected frame. In the author's field the mirror $z \to \pi - z$ leaves every metric component unchanged ($\sin(\pi - z) = \sin z$ and $\cot^2(\pi - z) = \cot^2 z$), and its pulled-back positive vielbein is $R_8e$; this turns the frame statement into the mirror statement. Status: PROVED; the Z2 construction across the brane is ASSUMED, the metric is degenerate at the brane, and no junction condition there is derived. Records: the Wolfram pairing report has 28 checks of T2 and the sympy pairing report 16; among them:

| statement | report | check |
| --- | --- | --- |
| the mirror is an isometry | `wolfram-pairing.json` | `T2_mirror_is_isometry` |
| the same, independently | `python-pairing.json` | `geometry.mirror_isometry` |
| the connection of the mirror patch | `wolfram-pairing.json` | `connection_mirror_patch` |
| equal tensor and current at the mirror point | `wolfram-pairing.json` | `T2_mirror_energy_momentum_and_current_commuting` |
| the pulled-back tensor | `python-pairing.json` | `T2.metric.commuting.emt` |
| the current | `python-pairing.json` | `T2.metric.commuting.current` |
| $S' = -S$ | `python-pairing.json` | `T2.metric.commuting.S_odd` |
| the field equations | `python-pairing.json` | `T2.metric.commuting.euler_lagrange_map` |

Notebooks 20a (In [9] and In [11]) and 20b (In [9]) reproduce them.

**The quantum reading Q (dirac16complex only).** The quantised field obeys the canonical anticommutator $\{\Psi_A(x), \Psi_B^\dagger(y)\} = B_{AB}\,\delta^7(x - y)/\sqrt{|g|}$ on a slice $x_4 = \text{const}$ (Chapter 10). For the T1 image,

$$
\{(\Gamma\Psi)_A, (\Gamma\Psi)_B^\dagger\} = (\Gamma B\Gamma^\dagger)_{AB}\,\frac{\delta^7}{\sqrt{|g|}} = -B_{AB}\,\frac{\delta^7}{\sqrt{|g|}} ,
$$

because the anticommutator is linear in each argument and

$$
\Gamma B\Gamma = -i\,\Gamma C\gamma^{(x_4)}\Gamma = -i\,C\,\Gamma\gamma^{(x_4)}\Gamma = -i\,C(-\gamma^{(x_4)}) = -B ,
$$

by step 2 and then step 1 of Section 20.5. The statements (`pairing-theory.json`, theorem Q): (Q1) the T1 image carries the Krein metric $-B$, which is also what its own Lagrangian demands; (Q2) its generators coincide with those of $\Psi$: $\Psi$ and $\Gamma\Psi$ are ONE quantum system relabelled, and the T1 identity $T' = -T$ is an identity between operators of that one system; (Q3) an independently quantised $(-m, -\lambda)$ universe has the anticommutator $+B$, cannot be identified with $\Gamma\Psi$, and on the product of the two state spaces the generators ADD, so no cancellation follows; (Q4) the one-particle ($\lambda = 0$) spectra of $+m$ and $-m$ are IDENTICAL (similar matrices, $\Gamma h_m\Gamma = h_{-m}$), in flat 4+4 space or in a general field at a point with frozen coefficients (the coefficients of the equation taken constant, equal to their values at that point); (Q5) the T2 image keeps $+B$ ($\gamma^{(x_8)}B\gamma^{(x_8)\dagger} = +B$): the mirror universe is an ordinary, independently quantisable copy with equal energies. Records: `wolfram-pairing.json`, `Q_Krein_metric_of_images`, `Q_no_identification_of_independent_universes`, `Q_one_particle_maps` (12 Q checks); `python-pairing.json`, `Q.no_cancellation_independent_universes`, `Q.T2_image_keeps_B` (10 Q checks). Status: PROVED. The quantum reading therefore removes the one place where a zero total could have looked like "a pair that costs nothing": for two independent quantum universes the energies do not cancel.

**Theorem T3 (the Kohn-Sham level, dirac16complex).** At the level of the Kohn-Sham model of Chapters 14 and 15 (instantaneous mean-field states at a fixed slice $a_{4,0}$ of the deflating history, good sector, Hartree plus the exact uniform-gas exchange), the block map of $\Gamma$, with the two brane parities exchanged and the tip angle $\theta \to \pi - \theta$, maps every self-consistent Kohn-Sham state with $(m, \lambda, \theta)$ onto one with $(-m, +\lambda, \pi - \theta)$, with equal levels, occupations, Kohn-Sham energy, grand potential and energy-momentum profiles, and $S \to -S$ (`t3-theory.json`; `wolfram-t3.json` 10 of 10 and `python-t3.json` 13 of 13 checks PASS). The Z2 brane is ASSUMED; the tip condition is a choice and must be transformed; in its parameters the map is of the T2 type (equal energies), although its matrix is the chirality of T1. Status: PROVED under these hypotheses. The proof in outline (`t3-theory.json`, key `proof`; the check names below are those of `wolfram-t3.json`, and `python-t3.json` has the same checks with a dot after `T3`; Chapter 19 gives the proof line by line and runs the Rust solver for both members): the $2 \times 2$ block form of $\Gamma$ maps each block Hamiltonian with the effective mass $M_{\mathrm{eff}}$ onto the block Hamiltonian of the other block with $-M_{\mathrm{eff}}$ at the same level (check `T3_block_hamiltonian_map`); it turns the tip condition with angle $\theta$ into the one with $\pi - \theta$ and exchanges the brane parities (checks `T3_tip_condition_map`, `T3_brane_parities_exchanged`); the densities that enter the energies are even under the map and $S$ is odd, so $M_{\mathrm{eff}} \to -M_{\mathrm{eff}}$ exactly when $(m, \lambda) \to (-m, +\lambda)$ (checks `T3_orbital_densities`, `T3_mean_field_map`); a one-to-one map between the orbitals with equal levels then gives equal occupations, energies and energy-momentum profiles (check `T3_energies_and_emt_profiles_equal`). T3's own list of what it does not establish begins with "No creation process, rate or amplitude" and adds: instantaneous states only (the time-dependent problem is OPEN), the brane ASSUMED, mean-field level only, and no back-reaction.

### 20.7 Corollary C1, line by line

**Hypotheses** (`Revision/docs/PAIR_CREATION_PROOFS.md`, section 7). (i) The gravitational field is the author's metric with the Einstein-Lovelock equations $\sum_{k=1}^3\alpha_kE_{(k)}{}^\mu{}_\nu + \Lambda\delta^\mu_\nu = \kappa T^\mu{}_\nu$. (ii) The complete source is the sum of the classical energy-momentum tensors of the two members of a T1 pair at the same points of the same patch. (iii) Nothing else sources the metric.

**Statement.** The source vanishes, so $a_4$ must solve the vacuum equations. (a) In Einstein gravity they have no real solution for $H > 0$ and any $\Lambda$. (b) In Einstein-Lovelock gravity the linear member $a_4 = AHx_4 + a_0$ is a vacuum exactly when the vacuum factor $V$ vanishes, where

$$
V = \alpha_1 - 40\alpha_2H^2 - 8A^2\alpha_2H^2 + 360\alpha_3H^4 + 144A^2\alpha_3H^4 + 72A^4\alpha_3H^4 .
$$

**Proof of (a), line by line.**

1. By hypothesis (ii) the source is $T^\mu{}_\nu[\Psi; m, \lambda] + T^\mu{}_\nu[\Gamma\Psi; -m, -\lambda]$.
2. By (T1c) the second term is minus the first, so the source is zero at every point.
3. With $\alpha_1 = 1$ and $\alpha_2 = \alpha_3 = 0$ the field equations become $G^\mu{}_\nu + \Lambda\delta^\mu_\nu = 0$.
4. The record gives $G^{x_4}{}_{x_4} = 3a_4'^2 + 21H^2$ and $G^{x_8}{}_{x_8} = -3a_4'^2 + 15H^2$ (`python-a4-report.json`, check `einstein_components`), so two of the equations read $3a_4'^2 + 21H^2 + \Lambda = 0$ and $-3a_4'^2 + 15H^2 + \Lambda = 0$.
5. Subtracting the second from the first removes $\Lambda$: $6a_4'^2 + 6H^2 = 0$.
6. For a real function $a_4$ the left side is at least $6H^2$, which is positive for $H > 0$; line 5 is false, so no real $a_4$ solves the equations. QED.

Adding the two equations of line 4 instead gives $36H^2 + 2\Lambda = 0$, so a solution would need $\Lambda = -18H^2$ and $a_4'^2 = -H^2$, that is $a_4' = \pm iH$: not a real rate. The other two independent equations, $15H^2 - 3a_4'^2 \pm a_4'' + \Lambda = 0$ for 3-space ($+$) and the extra times ($-$), then give $a_4'' = 0$. Records: `wolfram-a4-report.json`, check `einstein_no_vacuum_solution`; `python-a4-report.json`, check `einstein_no_vacuum`; `einstein-gauss-bonnet-a4.json`, check `no_vacuum_for_H_positive`. Notebook 20a, In [12], derives all of this with sympy from the record's components.

**What the geometry requires of any source.** With a source, the $x_4$ and $x_8$ equations read $\sum_k\alpha_kE_{(k)}{}^{x_4}{}_{x_4} + \Lambda = -\kappa\rho$ and $\sum_k\alpha_kE_{(k)}{}^{x_8}{}_{x_8} + \Lambda = \kappa p_8$, because $T^{x_4}{}_{x_4} = -\rho$ and $T^{x_8}{}_{x_8} = p_8$. Subtracting the first from the second:

$$
\sum_k\alpha_k\big(E_{(k)}{}^{x_8}{}_{x_8} - E_{(k)}{}^{x_4}{}_{x_4}\big) = \kappa p_8 + \kappa\rho .
$$

$\Lambda$ cancels in the difference. So every source must have the null combination

$$
\kappa(\rho + p_8) = -\sum_k\alpha_k\big(E_{(k)}{}^{x_4}{}_{x_4} - E_{(k)}{}^{x_8}{}_{x_8}\big) .
$$

In Einstein gravity, with the components of line 4,

$$
\kappa(\rho + p_8) = -\big(3a_4'^2 + 21H^2 + 3a_4'^2 - 15H^2\big) = -6(a_4'^2 + H^2) \le -6H^2 < 0 .
$$

The first equality inserts the components; the second collects the terms; the inequality holds because $a_4'^2 \ge 0$ (`python-a4-report.json` and `wolfram-a4-report.json`, check `einstein_null_energy_x8`). A T1 pair supplies $\rho + p_8 = 0$, which is never $\le -6H^2$: this is C1(a) once more, now as a statement about the source.

**Proof of (b), line by line.** For the linear member $a_4' = AH$ the record writes the right-hand side as $-6(A^2 + 1)H^2V$ with the vacuum factor $V$ above (`wolfram-a4-report.json` and `python-a4-report.json`, check `linear_member_vacuum_factor`). A vacuum has $\rho = p_8 = 0$, and $6(A^2 + 1)H^2 > 0$, so it needs $V = 0$. In Einstein-Gauss-Bonnet gravity ($\alpha_1 = 1$, $\alpha_3 = 0$):

$$
V = 1 - 40\alpha_2H^2 - 8A^2\alpha_2H^2 = 1 - 8\alpha_2H^2(A^2 + 5) .
$$

The terms with $\alpha_3$ vanish, and $40 = 8 \cdot 5$ lets us take out $8\alpha_2H^2$. Setting $V = 0$ and adding $8\alpha_2H^2(A^2 + 5)$ to both sides:

$$
8\alpha_2H^2(A^2 + 5) = 1 .
$$

Dividing by $8\alpha_2H^2$ (not zero) and subtracting 5:

$$
A^2 = \frac{1}{8\alpha_2H^2} - 5 = \frac{1 - 40\alpha_2H^2}{8\alpha_2H^2} .
$$

The last step writes 5 as $40\alpha_2H^2/(8\alpha_2H^2)$. The right side is not negative exactly when $0 < \alpha_2H^2 \le 1/40$; at $1/40$ the vacuum has $A = 0$, so $a_4$ is constant and neither 3-space nor the extra times change; the author's deflating history needs $A > 0$. For the author's history $A = 1$: $8\alpha_2H^2 \cdot 6 = 1$, so

$$
\alpha_2H^2 = \tfrac{1}{48} .
$$

The cosmological constant follows from the $x_4$ equation with $\rho = 0$: $\Lambda = -\sum_k\alpha_kE_{(k)}{}^{x_4}{}_{x_4}$. We need the two components at $a_4' = AH$ with $A = 1$. The Einstein part is $E_{(1)}{}^{x_4}{}_{x_4} = G^{x_4}{}_{x_4} = 3a_4'^2 + 21H^2 = 3H^2 + 21H^2 = 24H^2$ (line 4 above with $a_4' = H$). For the Gauss-Bonnet part we use the $x_4$ equation once more: it says $\kappa\rho = -\sum_k\alpha_kE_{(k)}{}^{x_4}{}_{x_4} - \Lambda$, so the part of $\kappa\rho$ that multiplies $\alpha_2$ is $-E_{(2)}{}^{x_4}{}_{x_4}$, and the record gives that part as $(36A^4 + 120A^2 + 420)H^4$ (`einstein-gauss-bonnet-a4.json`, check `gauss_bonnet_rho_alpha2`, which compares the record with the classical Gauss-Bonnet formula). Hence $E_{(2)}{}^{x_4}{}_{x_4} = -(36 + 120 + 420)H^4 = -576H^4$ at $A = 1$. Therefore

$$
\Lambda = -\Big(24H^2 + \frac{1}{48H^2}\big(-576H^4\big)\Big) = -24H^2 + 12H^2 = -12H^2 .
$$

The first equality inserts $\alpha_2 = 1/(48H^2)$; the second uses $576/48 = 12$. Notebook 20a (In [16]) checks exactly that with these values all four independent vacuum equations hold for $a_4 = Hx_4$ (`python-a4-report.json` and `wolfram-a4-report.json`, check `einstein_gauss_bonnet_vacuum_linear`). With the third coupling, $V = 0$ is linear in $x = \alpha_2H^2$ and $y = \alpha_3H^4$ for a fixed slope $A$; collecting the terms with $y$ on one side,

$$
y\,(72A^4 + 144A^2 + 360) = (8A^2 + 40)\,x - 1,\qquad y = \frac{(8A^2 + 40)x - 1}{72A^4 + 144A^2 + 360} ,
$$

a straight line in the plane of the two couplings; Einstein gravity ($x = y = 0$, $V = 1$) lies on none of these lines.

**What C1 says, and what it does not say.** PROVED: a T1 pair as the only source of the author's metric is a zero source; in Einstein gravity the metric then has no solution for $H > 0$, whatever $a_4$ and $\Lambda$. PROVED: in Einstein-Gauss-Bonnet gravity with $\alpha_2H^2 = 1/48$ and $\Lambda = -12H^2$ the author's deflating history IS a vacuum, so C1(a) depends on Einstein gravity. C1 does not apply to T2 pairs: the mirror copy carries the pulled-back, EQUAL tensor, so the sources add. C1 does not apply to two independently quantised universes (statement Q3). And C1 is not a creation statement: it compares two sources in ONE given geometry and derives no process, rate or amplitude. In Einstein gravity it says the opposite of "a pair makes the universe": a T1 pair alone cannot be the source of the author's metric at all.

### 20.8 Example: corollary C1 made visible

Notebook 20a turns every line of Sections 20.5 and 20.7 into a computation. It reads the author's gamma matrices, builds $C$, $\Gamma$ and the generators $S^{ab}$, and computes with sympy the canonical spin connection of the author's metric on the patch and on the mirror patch; it reproduces the record's twelve components and $\sum_\mu\gamma^\mu\Omega_\mu = 3H\gamma^{(x_8)}$, and finds $-3H\gamma^{(x_8)}$ on the mirror patch (a computation of this book, not a record). It then takes an arbitrary configuration of dirac16complex00 at one point of the deflating history, evaluates its 64-component energy-momentum tensor, its current and its field equation, and does the same for its T1 partner and its T2 mirror copy: the T1 pair cancels component by component, the T2 pair does not. Finally it derives the vacuum equations of Einstein and Einstein-Lovelock gravity from the record's Lovelock tensors and draws why Einstein gravity has no vacuum and which couplings do. It prints 37 PASS lines, 25 of which reproduce a named check of a Revision report, and draws seven figures. It needs numpy, sympy and matplotlib, no Rust, and runs in about 30 seconds (its recorded check run on the build computer took 16.1 seconds; the notebook's provenance file, which lies next to it, records every run).

<!-- NOTEBOOK 20a -->

### 20.11 Line-by-line walk-through of Notebook 20a

The notebook has 19 code cells, In [1] to In [19]. This section explains every line or small group of lines of every one of them, in order: a group of lines is quoted, then explained. Where a later cell repeats a pattern already explained, we say so and explain only what is new. The markdown cells between the code cells are printed in the complete text above and need no explanation.

**In [1], the set-up cell.** Every line that starts with `#` is a **comment**, which Python skips. The comment lines at the top of the cell are the complete run instructions of Section 20.9, so that the notebook file carries its own instructions. The code starts after the line that announces THE SET-UP; it is the same in every notebook of this book except for the notebook's name, and it computes no physics.

```python
import json  # reads and writes JSON files (text files that hold names and numbers)
import os  # reads the environment variable TEXTBOOK_OUTPUT_ROOT (explained below)
import textwrap  # breaks long printed text into lines of at most 89 characters
from pathlib import Path  # file and folder paths that work on Windows, macOS and Linux
```

`import` loads a **module** (a part of Python or of an installed package) so that the code can use it. `json`, `os`, `textwrap` and `pathlib` come with Python itself. `from pathlib import Path` takes only the name `Path` out of `pathlib`; a `Path` is the address of a file or folder, written the same way on every operating system.

```python
import matplotlib  # the plotting package
import matplotlib.pyplot as plt  # its drawing functions, called plt by convention
from IPython.display import Image, display  # shows a saved picture below a cell
```

These load the plotting package matplotlib, its drawing functions under the short name `plt`, and the two functions `Image` and `display` of IPython (the part of Jupyter that runs the Python code), which show a picture file below a cell.

```python
NOTEBOOK_ID = "20a"  # this notebook: chapter 20, example a
```

A **variable** is a name for a value. This line gives the name `NOTEBOOK_ID` to the **string** (a piece of text in quotes) `"20a"`; the figure files and the last printed line are named after it.

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

`def` defines a **function**, a named piece of code that runs each time it is called. The text in triple quotes under the `def` line is its **docstring**: it says what the function does and is not executed. `Path.cwd()` is the folder in which Jupyter runs the notebook, and `.resolve()` writes it as a complete address. `here.parents` is the list of the folders above it; `[here, *here.parents]` is a list that starts with `here` and continues with them (the star unpacks one list into another). The `for` loop visits these folders one after the other. The operator `/` joins a folder and a name into a longer path, and `.is_file()` is true when that file exists. The first folder that contains `Revision/textbook/requirements.txt` is the repository, and `return` hands it back. If no folder does, `raise` stops the notebook with a `FileNotFoundError` whose message says what to do.

```python
# The repository folder.  It is never printed: it differs from computer to computer,
# and the printed output of a notebook must not.
REPO = find_repository_root()
# Every file is WRITTEN below OUTPUT_ROOT.  OUTPUT_ROOT is the repository folder unless
# the environment variable TEXTBOOK_OUTPUT_ROOT names another folder; the book's
# checking tool sets it, so that a check run writes into a scratch folder instead.
OUTPUT_ROOT = Path(os.environ.get("TEXTBOOK_OUTPUT_ROOT", str(REPO)))
```

The first code line calls the function and names its result `REPO`. The second chooses where files are written: `os.environ` holds the **environment variables** of the running program (named texts that it receives from the computer), and `.get(name, default)` returns the value of `TEXTBOOK_OUTPUT_ROOT` if it is set and `str(REPO)`, the repository folder as text, otherwise. When you run the notebook the variable is not set, so the figures go into the repository; the book's checking tool sets it to a scratch folder.

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

Two small functions. `repository_file` gives the full path of a file of the repository, for reading a Revision record. `output_file` gives the full path at which to write a file; `path.parent.mkdir(parents=True, exist_ok=True)` first creates the folder of that file and every missing folder above it, and does nothing if the folder exists.

```python
def say(text):
    """Print text in lines of at most 89 characters (the width of a page of the book)."""
    print(textwrap.fill(str(text), width=89, subsequent_indent="    "))
```

`say` prints a text in lines of at most 89 characters, the width of a line of the book; `textwrap.fill` breaks the text at blanks and starts every line after the first with four blanks. This is why some long PASS lines of the notebook continue on an indented second line.

```python
matplotlib.rcdefaults()  # ignore personal matplotlib settings: same figures everywhere
plt.rcParams.update({"figure.figsize": (7.0, 4.2), "font.size": 10.0,
                     "axes.grid": True, "grid.alpha": 0.3})
```

`matplotlib.rcdefaults()` returns to matplotlib's built-in settings, so that the figures are the same on every computer. `plt.rcParams.update({...})` then sets the default size of a figure (7.0 by 4.2 inches), the size of its letters (10 points) and a faint grid (`grid.alpha` 0.3: 30 per cent opaque). The braces make a **dictionary**, a collection of pairs `key: value`.

```python
FIGURE_FOLDER = "Revision/textbook/figures"  # where the figures are saved
CAPTION_FILE = f"{FIGURE_FOLDER}/{NOTEBOOK_ID}.captions.json"  # their captions
FIGURE_NUMBERS = {}  # figure name -> its number k (file name <id>_<k>_<name>.png)
CAPTIONS = {}  # figure file name -> caption, written to CAPTION_FILE after every figure
# Start with an empty captions file ({} is an empty JSON dictionary); save_figure fills
# it.  newline="\n" writes the same line ends on Windows, macOS and Linux.
output_file(CAPTION_FILE).write_text("{}\n", encoding="utf-8", newline="\n")
```

A string that starts with `f` is an **f-string**: a name in braces is replaced by its value, so `CAPTION_FILE` is the text `Revision/textbook/figures/20a.captions.json`. `FIGURE_NUMBERS` and `CAPTIONS` start as empty dictionaries. The last line writes an empty JSON dictionary and a line end into the captions file; `encoding="utf-8"` fixes how the letters are stored and `newline="\n"` stores the same line end on every system.

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

`setdefault(name, value)` returns the number already stored for this figure name, or stores and returns one more than the number of figures so far: the figures are numbered 1, 2, 3, and a cell that is run twice keeps its number. The file name joins the notebook id, the number and the name, for example `20a_1_t1_pair_tensor.png`. `fig.savefig` writes a PNG file with 150 dots per inch, cuts away the empty margin, and stores no program name, so that two runs write the same bytes. `plt.close(fig)` removes the figure from memory; otherwise Jupyter would draw it a second time. The caption is stored, the whole dictionary is written to the captions file (`json.dumps` turns it into JSON text with sorted keys), `display(Image(...))` shows the saved picture below the cell, and the last line prints where it was saved.

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

`PASSED` is an empty **list** (an ordered collection in square brackets). `check` is the function behind every check of the book: if `condition` is false, `raise AssertionError(...)` stops the notebook with an error that names the check; otherwise the name is appended to `PASSED` and the line PASS followed by the name is printed, and, when `record` is given, a second line that names the Revision record. `record=None` makes that argument optional.

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

`report` prints a key number as a line that starts with RESULT; `(f" {unit}" if unit else "")` adds the unit only when one is given. `all_checks_passed` prints the last line of the notebook, with `len(PASSED)`, the number of checks that passed. The last statement prints the one output line of In [1], Set-up of notebook 20a complete.

**In [2], the records and the helper `reproduces`.**

```python
import contextlib  # redirect_stdout: send printed lines into a buffer
import io  # StringIO: a text buffer in memory
```

Two more modules of Python: `contextlib` provides `redirect_stdout`, which sends whatever `print` writes into another place, and `io` provides `StringIO`, a text buffer held in memory.

```python
GAMMAS = "Revision/algebra/gammas.json"  # the author's gamma matrices
PROOFS = "Revision/docs/PAIR_CREATION_PROOFS.md"  # the pairing document
PAIR_PY = "Revision/pairing/reports/python-pairing.json"  # sympy pairing record
PAIR_WL = "Revision/pairing/reports/wolfram-pairing.json"  # Wolfram pairing record
A4_RECORD = "Revision/field_equations_a4/a4-equations.json"  # the a4 equations
A4_PY = "Revision/field_equations_a4/reports/python-a4-report.json"
A4_WL = "Revision/field_equations_a4/reports/wolfram-a4-report.json"
LEAD_EGB = "Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json"
LEAD_EMT = "Revision/lead_checks/reports/emt-divergence-and-spin-connection.json"
```

Nine short names for the nine files of the repository that the notebook reads: the author's gammas, the Revision document of the pairing proofs, the two pairing reports, the record of the field equations for $a_4$ with its two reports, and the lead's two independent reports. Names written in capital letters are, by custom, values that the program does not change.

```python
def read_json(relative):
    """Read a JSON file of the repository (a Revision record)."""
    return json.loads(repository_file(relative).read_text(encoding="utf-8"))


def record_verdict(report_file, name):
    """The verdict ("PASS") of the check called name in a report; None if absent."""
    for entry in read_json(report_file)["checks"]:
        if entry["name"] == name:
            return entry["verdict"]
    return None
```

`read_json` reads a file of the repository as text and turns it into Python dictionaries and lists with `json.loads`. Every report holds, under the key `"checks"`, a list whose entries are dictionaries with a `"name"` and a `"verdict"`. `record_verdict` walks through that list and returns the verdict of the check with the given name, or `None` (Python's word for "nothing") if the report has no such check.

```python
def reproduces(condition, name, report_file, record_name):
    """A check that also requires the record check record_name to be PASS."""
    found = record_verdict(report_file, record_name) == "PASS"
    lines = io.StringIO()  # a text buffer
    with contextlib.redirect_stdout(lines):  # print() now writes into the buffer
        check(condition and found, name,
              record=f"{report_file}, check {record_name}")
    print(lines.getvalue(), end="")  # both lines with one print call
```

`reproduces` is the check used whenever a result of the notebook reproduces a Revision record. `found` is true only if the named check of the named report has the verdict PASS. The `with` block sends the output of `check` into the buffer `lines`; `check` passes only if the notebook's own `condition` holds AND `found` is true, and it prints the PASS line and the line "reproduces" followed by the report and the check. The last line prints both lines at once (`end=""` adds no extra line end). If either condition fails, `check` raises its error inside the `with` block and the notebook stops.

```python
proofs = repository_file(PROOFS).read_text(encoding="utf-8")
C1_WORDS = ("a T1 pair taken as the complete classical source of the author's "
            "metric is a zero source, and the Einstein equations then have no "
            "solution for")
say(f"{PROOFS} says: \"{C1_WORDS} H > 0.\"")
check(C1_WORDS in proofs, "the record states the corollary C1")
```

The first line reads the whole Revision document as one text. `C1_WORDS` is the record's sentence of the corollary C1 (two strings written next to each other inside parentheses are joined into one). `say` prints it with the name of the document; `\"` puts a double quote inside a string written with double quotes. The check `C1_WORDS in proofs` is true when the sentence occurs in the document, word for word: the first printed lines of the cell.

```python
wolfram_counts = read_json(PAIR_WL)["summary"]  # passed, failed, total
sympy_counts = read_json(PAIR_PY)["counts"]  # pass, fail, pending
passed, total = wolfram_counts["passed"], wolfram_counts["total"]
say(f"pairing reports: Wolfram {passed} of {total} PASS, sympy "
    f"{sympy_counts["pass"]} PASS and {sympy_counts["fail"]} FAIL")
check(wolfram_counts["passed"] == wolfram_counts["total"] == 101
      and sympy_counts["pass"] == 66 and sympy_counts["fail"] == 0,
      "both pairing reports pass every check (101 and 66)")
```

The two pairing reports store their counts under different keys: `"summary"` with `"passed"` and `"total"` (Wolfram) and `"counts"` with `"pass"` and `"fail"` (sympy). `passed, total = a, b` gives two names at once. Inside the braces of an f-string Python 3.12 and newer allow the same kind of quotes as around the string, as in `sympy_counts["pass"]`. The check compares the counts with the numbers of the record (101 Wolfram checks, 66 sympy checks, no failure); `a == b == 101` is true only if both comparisons hold. If a later revision of the record changed these counts, this check would fail and show the change. Output: pairing reports: Wolfram 101 of 101 PASS, sympy 66 PASS and 0 FAIL.

**In [3], the gammas, $C$ and the chirality.**

```python
import itertools  # loops over all combinations of indices

import numpy as np  # floating-point arrays
import sympy as sp  # exact algebra
```

`itertools.product` (used below) runs over all combinations of indices. **numpy**, short `np`, computes with arrays of floating-point numbers (numbers with about 16 significant digits). **sympy**, short `sp`, computes exactly with whole numbers, fractions and symbols.

```python
NAMES = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]  # positions 0..7
ETA = [1, 1, 1, -1, -1, -1, -1, 1]  # the frame metric eta, in the order x1..x8
I16 = sp.eye(16)  # the 16 by 16 unit matrix
fixture = read_json(GAMMAS)
gamma = [sp.Matrix([[sp.Rational(x) for x in row] for row in matrix])
         for matrix in fixture["gamma"]]  # gamma[a] = gamma^(x_(a+1)), exact
```

Python counts list positions from 0, so position 0 stands for $x_1$ and position 7 for $x_8$; `NAMES` holds the labels for the figures and `ETA` the diagonal of $\eta$ in the same order. `sp.eye(16)` is the exact unit matrix $I_{16}$. The file `gammas.json` stores, under the key `"gamma"`, the eight matrices as lists of rows of whole numbers. The double **list comprehension** `[[... for x in row] for row in matrix]` builds, row by row, a list of lists in which every entry is turned into an exact sympy number by `sp.Rational`; `sp.Matrix` makes a sympy matrix of it; the outer comprehension does this for each of the eight matrices. So `gamma[0]` is $\gamma^{(x_1)}$ and `gamma[7]` is $\gamma^{(x_8)}$.

```python
clifford = all(gamma[a] * gamma[b] + gamma[b] * gamma[a]
               == (2 * ETA[a] if a == b else 0) * I16
               for a in range(8) for b in range(8))
C = gamma[7] * gamma[0] * gamma[1] * gamma[2]  # C = g^(x8) g^(x1) g^(x2) g^(x3)
reproduces(clifford and C == C.T and C * C == I16
           and all((C * g).T == -(C * g) for g in gamma),
           "Clifford relation; C real symmetric, C^2 = 1, C gamma antisymmetric",
           PAIR_PY, "gammas.C")
```

`*` between sympy matrices is the matrix product. `all(...)` is true when the comparison holds for all 64 pairs $(a, b)$: the anticommutator $\gamma^{(a)}\gamma^{(b)} + \gamma^{(b)}\gamma^{(a)}$ must equal $2\eta_{aa}I_{16}$ when $a = b$ and the zero matrix otherwise (`x if condition else y` chooses one of two values). The next line builds $C$ from the record's definition. The check requires the Clifford relation, $C^T = C$ (`.T` is the transpose; the entries are real, so $C$ is real symmetric), $C^2 = I_{16}$, and that every $C\gamma^{(a)}$ is antisymmetric; it reproduces `python-pairing.json`, check `gammas.C`.

```python
chirality = gamma[7]  # the product g^(x8) g^(x1) ... g^(x7), built factor by factor
for a in range(7):
    chirality = chirality * gamma[a]
reproduces(chirality == sp.diag(*([-1] * 8 + [1] * 8)),
           "Gamma = diag(-I8, I8)", PAIR_PY, "gammas.Gamma")
reproduces(all(chirality * g == -g * chirality for g in gamma)
           and chirality * C == C * chirality,
           "Gamma anticommutes with every gamma and commutes with C",
           PAIR_WL, "Gamma_properties")
```

The loop multiplies $\gamma^{(x_8)}$ from the right by $\gamma^{(x_1)}, \dots, \gamma^{(x_7)}$, in the record's order. `[-1] * 8 + [1] * 8` is the list of eight entries $-1$ followed by eight entries $+1$, and `sp.diag(*list)` is the diagonal matrix with these entries: the check is $\Gamma = \mathrm{diag}(-I_8, I_8)$. The second check is steps 1 and 2 of Section 20.5: $\Gamma\gamma^{(a)} = -\gamma^{(a)}\Gamma$ for all eight gammas and $\Gamma C = C\Gamma$.

```python
S_exact = [[(gamma[a] * gamma[b] - gamma[b] * gamma[a]) / 4 for b in range(8)]
           for a in range(8)]  # the generators S^ab
to_numpy = lambda matrix: np.array(matrix.tolist(), dtype=float)  # noqa: E731
gamma_num = [to_numpy(g) for g in gamma]  # floating-point copies
C_num, Gamma_num = to_numpy(C), to_numpy(chirality)
S_num = [[to_numpy(S_exact[a][b]) for b in range(8)] for a in range(8)]
B_num = -1j * C_num @ gamma_num[3]  # B = -i C gamma^(x4): J^x4 = Psi^dagger B Psi
```

`S_exact[a][b]` is the generator $S^{ab} = \frac14[\gamma^{(a)}, \gamma^{(b)}]$, exactly, for all 64 pairs. `lambda matrix: ...` is a one-line function: it turns a sympy matrix into a numpy array of floating-point numbers (`tolist()` gives the list of rows); the comment `noqa: E731` tells a style checker that the one-line form is intended. The next lines make floating-point copies of the gammas, of $C$, of $\Gamma$ and of the $S^{ab}$. In numpy, `@` is the matrix product and `1j` is the imaginary unit $i$; `B_num` is $B = -iC\gamma^{(x_4)}$ (position 3 is $x_4$). The cell prints the three PASS lines with their records.

**In [4], the spin connection on both patches.**

```python
H = sp.symbols("H", positive=True)  # the author's constant H > 0
z = sp.symbols("z", real=True)  # the hidden coordinate z = 6 H x8
x4 = sp.symbols("x4", real=True)  # the time
a4 = sp.Function("a4")(x4)  # the metric function a4(x4), arbitrary
a4_value, slope = sp.symbols("a4_value slope", real=True)  # a4 and a4' at a point
```

`sp.symbols` makes sympy symbols, letters that sympy computes with; `positive=True` and `real=True` tell sympy what kind of number they stand for, which lets it simplify correctly (for example $\sqrt{H^2} = H$). `sp.Function("a4")(x4)` is an unknown function $a_4(x_4)$: sympy can differentiate it without knowing it. The last two symbols will replace $a_4$ and $a_4'$ at a point.

```python
def lengths(s8):
    """The lengths E_a of the diagonal vielbein; s8 = +1 on the patch, -1 on the
    mirror patch (where cot z < 0, so -cot z is the positive length)."""
    s = sp.sin(z) ** sp.Rational(1, 6)  # the warp sin(z)^(1/6) of a length
    return ([sp.exp(a4) * s] * 3 + [sp.Integer(1)] + [sp.exp(-a4) * s] * 3
            + [s8 * sp.cot(z)])
```

The lengths $E_a$ (written $f_a$ in Sections 20.5 and 20.6) of the diagonal vielbein, in the order $x_1, \dots, x_8$: three times $e^{a_4}\sin^{1/6}z$ for the inflating 3-space, 1 for the time, three times $e^{-a_4}\sin^{1/6}z$ for the DEFLATING extra times, and $s_8\cot z$ for the hidden direction. `**` is the power and `sp.Rational(1, 6)` the exact fraction $1/6$. `[x] * 3` is a list of three copies of `x`, and `+` joins lists. On the mirror patch $\cot z$ is negative, so the positive length there is $-\cot z$: the argument `s8` is $+1$ on the patch and $-1$ on the mirror patch.

```python
def d(expr, mu):
    """The partial derivative along the coordinate at position mu."""
    if mu == 3:
        return sp.diff(expr, x4)
    if mu == 7:
        return 6 * H * sp.diff(expr, z)  # d/dx8 = 6 H d/dz
    return sp.Integer(0)  # nothing depends on x1, x2, x3, x5, x6, x7
```

The partial derivative $\partial_\mu$ of an expression: along $x_4$ (position 3) it is `sp.diff(expr, x4)`; along $x_8$ (position 7) the chain rule gives $\partial/\partial x_8 = (dz/dx_8)\,\partial/\partial z = 6H\,\partial/\partial z$; along the other six directions it is zero, because the metric does not depend on them.

```python
def spin_connection(s8):
    """The lengths E_a and omega[mu][a][b] = omega_mu ab at a point (a4 and a4'
    replaced by the symbols a4_value and slope)."""
    E = lengths(s8)
    g = [ETA[a] * E[a] ** 2 for a in range(8)]  # the metric g_aa
    christoffel = {}
    for a, b, c in itertools.product(range(8), repeat=3):
        value = 0  # the formula of the markdown cell, term by term
        if a == c:
            value += d(g[a], b)
        if a == b:
            value += d(g[a], c)
        if b == c:
            value -= d(g[b], a)
        christoffel[a, b, c] = value / (2 * g[a])
```

The diagonal metric is $g_{aa} = \eta_{aa}E_a^2$. `itertools.product(range(8), repeat=3)` runs over all $8^3 = 512$ triples $(a, b, c)$. For each, the loop builds the Christoffel symbol of a diagonal metric term by term, $\Gamma^a{}_{bc} = (\delta_{ac}\partial_bg_{aa} + \delta_{ab}\partial_cg_{aa} - \delta_{bc}\partial_ag_{bb})/(2g_{aa})$: each `if` adds one term exactly when its Kronecker delta is 1, and `+=` and `-=` add to or subtract from `value`. The dictionary `christoffel` stores the result under the key `(a, b, c)`.

```python
    omega = [[[sp.Integer(0)] * 8 for _ in range(8)] for _ in range(8)]
    for mu, a, b in itertools.product(range(8), repeat=3):
        if a != b:
            value = ETA[a] * E[a] * christoffel[a, mu, b] / E[b]
            value = value.subs(sp.Derivative(a4, x4), slope).subs(a4, a4_value)
            omega[mu][a][b] = sp.simplify(value)
    return [length.subs(a4, a4_value) for length in E], omega
```

`omega` starts as an $8 \times 8 \times 8$ nest of zeros (`_` is a loop name whose value is not used). For $a \neq b$ the component is $\omega_{\mu ab} = \eta_{aa}(E_a/E_b)\Gamma^a{}_{\mu b}$, the formula derived in the markdown cell above the code; for $a = b$ it is zero. `.subs(old, new)` substitutes: first $a_4'$ (sympy's `Derivative(a4, x4)`) by the symbol `slope`, then $a_4$ by `a4_value`, so that the components become expressions in numbers that can be chosen at a point. `sp.simplify` writes each one in its simplest form. The function returns the lengths (with the same substitution) and the components.

```python
E_patch, omega_patch = spin_connection(1)
E_mirror, omega_mirror = spin_connection(-1)
for label, omega in (("patch", omega_patch), ("mirror patch", omega_mirror)):
    count = sum(1 for mu in range(8) for a in range(8) for b in range(a + 1, 8)
                if omega[mu][a][b] != 0)
    say(f"{label}: {count} nonzero components omega_mu ab with a < b")
```

The connection is computed on both patches. For each, `sum(1 for ... if ...)` counts the nonzero components with $a < b$ (the others follow from the antisymmetry $\omega_{\mu ba} = -\omega_{\mu ab}$). Output: 12 on the patch and 12 on the mirror patch.

**In [5], the twelve components, $\gamma^\mu\Omega_\mu$ and the mirror isometry.**

```python
s = sp.sin(z) ** sp.Rational(1, 6)
u, v = sp.exp(a4_value) * s, sp.exp(-a4_value) * s
expected = {}  # (mu, a, b) -> the record's component, on the patch
for i in (0, 1, 2):  # the inflating 3-space directions
    expected[i, i, 3], expected[i, i, 7] = slope * u, H * u
for t in (4, 5, 6):  # the deflating extra times
    expected[t, 3, t], expected[t, t, 7] = -slope * v, -H * v
```

`u` and `v` are the two lengths $e^{a_4}\sin^{1/6}z$ and $e^{-a_4}\sin^{1/6}z$ at a point. The dictionary `expected` holds the record's twelve components: for each inflating direction $i$, $\omega_{x_i,x_ix_4} = a_4'u$ and $\omega_{x_i,x_ix_8} = Hu$; for each deflating extra time $t$, $\omega_{x_t,x_4x_t} = -a_4'v$ and $\omega_{x_t,x_tx_8} = -Hv$.

```python
def components(omega):
    """The nonzero omega_mu ab with a < b, as a dictionary."""
    return {(mu, a, b): omega[mu][a][b] for mu in range(8) for a in range(8)
            for b in range(a + 1, 8) if omega[mu][a][b] != 0}


def same_components(found, wanted):
    return set(found) == set(wanted) and all(
        sp.simplify(found[key] - wanted[key]) == 0 for key in wanted)
```

`components` collects the nonzero components with $a < b$ into a dictionary (a **dictionary comprehension**). `same_components` is true when two such dictionaries have the same keys (`set(...)` is the collection of keys without order) and every difference simplifies to zero.

```python
reproduces(same_components(components(omega_patch), expected),
           "the twelve spin-connection components of the record (patch)",
           PAIR_PY, "geometry.spin_connection_components")
flipped = {key: (-value if 7 in key[1:] else value)
           for key, value in expected.items()}  # x8 components change sign
reproduces(same_components(components(omega_mirror), flipped),
           "mirror patch: the x8 components change sign, the others do not",
           PAIR_WL, "connection_mirror_patch")
```

The first check compares the patch with the record. On the mirror patch the length $E_8 = -\cot z$ has the opposite sign, so every component with a frame index $x_8$ changes sign: `flipped` is `expected` with the sign reversed wherever the position 7 occurs among the two frame indices `key[1:]`. The second check compares the mirror patch with it.

```python
Omega = {}  # s8 -> the eight matrices Omega_mu
for s8, omega in ((1, omega_patch), (-1, omega_mirror)):
    Omega[s8] = [sum((omega[mu][a][b] * S_exact[a][b] / 2 for a in range(8)
                      for b in range(8) if omega[mu][a][b] != 0), sp.zeros(16))
                 for mu in range(8)]
term = {}  # s8 -> sum over mu of gamma^mu Omega_mu
for s8, E in ((1, E_patch), (-1, E_mirror)):
    term[s8] = sum((gamma[mu] / E[mu] * Omega[s8][mu] for mu in range(8)),
                   sp.zeros(16)).applyfunc(sp.simplify)
```

For each patch, `Omega[s8][mu]` is the matrix $\Omega_\mu = \frac12\sum_{a,b}\omega_{\mu ab}S^{ab}$; `sum(..., sp.zeros(16))` adds matrices starting from the $16 \times 16$ zero matrix. `term[s8]` is $\sum_\mu\gamma^\mu\Omega_\mu$ with $\gamma^\mu = \gamma^{(\mu)}/E_\mu$; `.applyfunc(sp.simplify)` simplifies each of its 256 entries.

```python
reproduces(term[1] == 3 * H * gamma[7], "patch: gamma^mu Omega_mu = 3 H gamma^(x8)",
           LEAD_EMT, "gamma_Omega_equals_3H_gamma8")
check(term[-1] == -3 * H * gamma[7], "mirror patch: gamma^mu Omega_mu = -3 H gamma^(x8)")
g_patch = [ETA[a] * E_patch[a] ** 2 for a in range(8)]
reproduces(all(sp.simplify(entry.subs(z, sp.pi - z) - entry) == 0
               for entry in g_patch),
           "z -> pi - z leaves all eight metric components unchanged",
           PAIR_PY, "geometry.mirror_isometry")
```

On the patch the sum is $3H\gamma^{(x_8)}$, the record's spin-connection term, with no $a_4$ or $a_4'$ left: the terms of the three inflating and the three deflating directions along $\gamma^{(x_4)}$ cancel. On the mirror patch it is $-3H\gamma^{(x_8)}$; this check has no record (a computation of this notebook). The last check substitutes $z \to \pi - z$ into the eight metric components and finds each unchanged: the mirror is an isometry.

**In [6], the geometry at a point and the bilinears.**

```python
point_symbols = (z, a4_value, slope, H)
NUMERIC = {}  # s8 -> (the function of the lengths, the connection pieces)
for s8, E, omega in ((1, E_patch, omega_patch), (-1, E_mirror, omega_mirror)):
    lengths_f = sp.lambdify(point_symbols, E, "numpy")
    pieces = [(mu, a, b, sp.lambdify(point_symbols, omega[mu][a][b], "numpy"))
              for mu in range(8) for a in range(8) for b in range(8)
              if omega[mu][a][b] != 0]
    NUMERIC[s8] = (lengths_f, pieces)
```

`sp.lambdify(symbols, expression, "numpy")` turns a sympy expression into an ordinary Python function of the listed symbols that computes with numpy. For each patch, `lengths_f` computes the eight lengths and `pieces` is a list of the nonzero components $(\mu, a, b)$, each with its own function; they are stored under the key $+1$ or $-1$.

```python
def geometry_at(s8, z_value, a4_number, slope_number, H_number=1.0):
    """Lengths, metric, Omega_mu and the curved gammas at one point."""
    lengths_f, pieces = NUMERIC[s8]
    values = (z_value, a4_number, slope_number, H_number)
    E = np.array([float(x) for x in lengths_f(*values)])
    Om = [np.zeros((16, 16)) for _ in range(8)]
    for mu, a, b, f in pieces:  # Omega_mu = (1/2) sum omega_mu ab S^ab
        Om[mu] += float(f(*values)) * S_num[a][b] / 2
    return {"g": np.array(ETA) * E ** 2, "Omega": Om,
            "up": [gamma_num[mu] / E[mu] for mu in range(8)],
            "down": [ETA[mu] * E[mu] * gamma_num[mu] for mu in range(8)]}
```

`geometry_at` evaluates the geometry at one point: the patch (`s8`), $z$, $a_4$, $a_4'$ and $H$ (1 unless given). `f(*values)` calls a function with the four numbers as its arguments. It returns a dictionary with the metric $g_{\mu\mu}$, the eight matrices $\Omega_\mu$ (built from the pieces), the curved gammas with an upper index $\gamma^\mu = \gamma^{(\mu)}/E_\mu$ and with a lower index $\gamma_\mu = g_{\mu\mu}\gamma^\mu = \eta_{\mu\mu}E_\mu\gamma^{(\mu)}$.

```python
def bilinears(at, psi, dpsi, m, lam):
    """S, K, L/sqrt|g|, T_mu nu, J^mu, the field-equation residual, and the
    largest imaginary part of a quantity that must be real."""
    bar = psi.conj() @ C_num  # Psibar = Psi^dagger C (a row)
    dbar = [row.conj() @ C_num for row in dpsi]  # d_mu Psibar
    D = [dpsi[mu] + at["Omega"][mu] @ psi for mu in range(8)]  # D_mu Psi
    Dbar = [dbar[mu] - bar @ at["Omega"][mu] for mu in range(8)]  # D_mu Psibar
    S = bar @ psi
    K = 0.5 * sum(bar @ at["up"][mu] @ D[mu] - Dbar[mu] @ at["up"][mu] @ psi
                  for mu in range(8))
    L = K - m * S - lam / 2 * S ** 2  # L / sqrt|g|
```

`bilinears` evaluates, from the first jet of a configuration (the 16 values `psi` and the eight derivative columns `dpsi[mu]`), every quantity of Section 20.5. `psi.conj()` is the complex conjugate of each entry; for a one-dimensional numpy array the product `psi.conj() @ C_num` is the row $\Psi^\dagger C = \bar\Psi$. Then $\partial_\mu\bar\Psi$, $D_\mu\Psi = \partial_\mu\Psi + \Omega_\mu\Psi$ and $D_\mu\bar\Psi = \partial_\mu\bar\Psi - \bar\Psi\Omega_\mu$, the scalar $S$, the kinetic term $K$ and $\mathcal{L}/\sqrt{|g|} = K - mS - \frac{\lambda}{2}S^2$.

```python
    T = np.zeros((8, 8), dtype=complex)
    for mu, nu in itertools.product(range(8), repeat=2):
        T[mu, nu] = 0.25 * (bar @ at["down"][mu] @ D[nu]
                            + bar @ at["down"][nu] @ D[mu]
                            - Dbar[mu] @ at["down"][nu] @ psi
                            - Dbar[nu] @ at["down"][mu] @ psi)
        if mu == nu:
            T[mu, nu] -= at["g"][mu] * L
    J = np.array([-1j * bar @ at["up"][mu] @ psi for mu in range(8)])
    residual = sum(at["up"][mu] @ D[mu] for mu in range(8)) - (m + lam * S) * psi
```

The 64 components of $T_{\mu\nu}$, term by term as in the formula of Section 20.5 (the metric is diagonal, so the term $-g_{\mu\nu}\mathcal{L}/\sqrt{|g|}$ appears only for $\mu = \nu$); the eight components of the current $J^\mu = -i\bar\Psi\gamma^\mu\Psi$; and the field-equation residual $E_{m,\lambda} = \gamma^\mu D_\mu\Psi - (m + \lambda S)\Psi$, a column of 16 numbers that is zero exactly when the configuration solves the field equation.

```python
    imaginary = max(abs(S.imag), abs(K.imag), np.abs(T.imag).max(),
                    np.abs(J.imag).max())
    return {"S": S.real, "K": K.real, "L": L.real, "T": T.real, "J": J.real,
            "E": residual, "imag": imaginary}
```

$S$, $K$, $T_{\mu\nu}$ and $J^\mu$ must be real numbers (Chapter 7 proves it); in floating point they come out with tiny imaginary parts of rounding size. `imaginary` is the largest of them, so that the next cell can check it; the function returns the real parts and the residual. The cell prints nothing.

**In [7], a configuration and its T1 partner at one point.**

```python
rng = np.random.default_rng(20261007)  # a fixed seed: the same numbers every run
R8_SIGNS = [1, 1, 1, 1, 1, 1, 1, -1]  # the mirror reverses the direction x8
psi = rng.normal(size=16) + 1j * rng.normal(size=16)  # the 16 complex values
dpsi = [rng.normal(size=16) + 1j * rng.normal(size=16) for _ in range(8)]
Z0, A4_0, M0, LAM0 = 0.6, 0.5, 2.0, 0.5  # the point and the parameters (H = 1)
```

`np.random.default_rng(20261007)` is a random-number generator started from a fixed **seed**, so that every run draws the same numbers and the notebook is reproducible. `rng.normal(size=16)` draws 16 numbers from the bell-shaped normal distribution; real part plus $i$ times another 16 such numbers gives 16 random complex values $\Psi$, and the comprehension draws eight more such columns, the derivatives $\partial_\mu\Psi$. `R8_SIGNS` is the diagonal of $R_8$, used later. The point is $z = 0.6$, $a_4 = 0.5$, and the parameters are $m = 2$, $\lambda = 1/2$, in units $H = 1$.

```python
at = geometry_at(1, Z0, A4_0, 1.0)  # a4' = 1: the deflating history A = 1
one = bilinears(at, psi, dpsi, M0, LAM0)  # Psi with (m, lambda)
partner = bilinears(at, Gamma_num @ psi, [Gamma_num @ row for row in dpsi],
                    -M0, -LAM0)  # Gamma Psi with (-m, -lambda)
scale = np.abs(one["T"]).max()  # the size of the tensor
report("S of the configuration", f"{one["S"]:.6f}")
report("largest |T_mu nu| of the configuration", f"{scale:.4f}")
```

The geometry at the point on the patch with $a_4' = 1$, the rate of the deflating history. `one` holds the quantities of the configuration with $(m, \lambda)$; `partner` those of $\Gamma\Psi$ (value and derivatives multiplied by $\Gamma$, because $\partial_\mu(\Gamma\Psi) = \Gamma\partial_\mu\Psi$) with $(-m, -\lambda)$. `scale` is the largest modulus of a component of $T$; every tolerance below is measured relative to it. `:.6f` prints a number with six digits after the point. Output: RESULT S of the configuration = 1.354934 and RESULT largest modulus of $T_{\mu\nu}$ = 26.7625. The configuration is random: it is NOT a solution, and T1 must hold anyway, because it is an off-shell identity.

```python
check(max(one["imag"], partner["imag"]) < 1e-12 * scale,
      "S, K, T and J are real numbers (to rounding)")
reproduces(abs(partner["S"] - one["S"]) < 1e-12 and abs(partner["K"] + one["K"])
           < 1e-12, "S' = S and K' = -K", PAIR_PY, "T1.metric.commuting.S_invariant")
reproduces(np.abs(one["T"] + partner["T"]).max() < 1e-12 * scale,
           "T1 pair: all 64 components of T + T' vanish",
           PAIR_PY, "T1.metric.commuting.pair_total_emt_zero")
reproduces(np.abs(one["J"] + partner["J"]).max() < 1e-12 * scale,
           "T1 pair: all 8 components of J + J' vanish",
           PAIR_WL, "T1_current_primordial_commuting")
reproduces(np.abs(partner["E"] + Gamma_num @ one["E"]).max() < 1e-12 * scale,
           "E_(-m,-lambda)[Gamma Psi] = -Gamma E_(m,lambda)[Psi]",
           PAIR_PY, "T1.metric.commuting.euler_lagrange_map")
```

Five checks of theorem T1 at this point, each to $10^{-12}$ times the size of the tensor, which allows only rounding errors: the imaginary parts are rounding; $S' = S$ and $K' = -K$ (step 5 of Section 20.5); all 64 components of $T + T'$ vanish (T1c); all eight components of $J + J'$ vanish; and the residuals obey $E_{-m,-\lambda}[\Gamma\Psi] = -\Gamma E_{m,\lambda}[\Psi]$ (step 7), so one vanishes exactly when the other does.

```python
wrong_1 = bilinears(at, Gamma_num @ psi, [Gamma_num @ row for row in dpsi],
                    -M0, LAM0)  # only the mass reversed
wrong_2 = bilinears(at, Gamma_num @ psi, [Gamma_num @ row for row in dpsi],
                    M0, LAM0)  # nothing reversed
reproduces(min(np.abs(one["T"] + wrong_1["T"]).max(),
               np.abs(one["T"] + wrong_2["T"]).max()) > 1e-3 * scale,
           "negative controls: with (-m, +lambda) or (m, lambda) no cancellation",
           PAIR_PY, "T1.metric.commuting.negative_controls")
```

Two **negative controls**, computations that must FAIL to cancel: the partner $\Gamma\Psi$ with only the mass reversed, and with nothing reversed. In both cases the sum $T + T'$ is far from zero (more than $10^{-3}$ times the size of the tensor). This shows that the cancellation of the previous check is not an accident of the test: the mass AND the coupling must change sign.

**In [8], figure 1: the T1 pair cancels.**

```python
fig, axes = plt.subplots(1, 3, figsize=(12.0, 4.3))
panels = ((one["T"], "$T_{\\mu\\nu}[\\Psi;\\,m,\\lambda]$"),
          (partner["T"], "$T_{\\mu\\nu}[\\Gamma\\Psi;\\,-m,-\\lambda]$"),
          (one["T"] + partner["T"], "sum: the source of the pair"))
```

`plt.subplots(1, 3, ...)` makes a figure with one row of three panels (**axes**), 12 by 4.3 inches. `panels` pairs each table with its title; the titles are written in LaTeX, and inside a Python string a backslash is written twice, so `\\mu` reaches matplotlib as `\mu`.

```python
for ax, (values, title) in zip(axes, panels):
    image = ax.imshow(values, cmap="RdBu_r", vmin=-scale, vmax=scale)
    ax.set_xticks(range(8))
    ax.set_xticklabels(NAMES, fontsize=7)
    ax.set_yticks(range(8))
    ax.set_yticklabels(NAMES, fontsize=7)
    ax.grid(False)  # no grid lines across the coloured squares
    ax.set_title(title, fontsize=10)
fig.colorbar(image, ax=list(axes), shrink=0.8, label="value (units $H = 1$)")
```

`zip` walks through the panels and the tables together. `ax.imshow` draws an $8 \times 8$ table as coloured squares (a **heat map**): the colour map `RdBu_r` runs from blue (negative) through white (zero) to red (positive), and `vmin=-scale, vmax=scale` uses the same scale in all three panels, so that equal colours mean equal numbers. The tick lines put the labels $x_1$ to $x_8$ on both axes; `ax.grid(False)` switches off the grid lines. `fig.colorbar` draws the colour scale beside the panels.

```python
save_figure(fig, "t1_pair_tensor",
            "The energy-momentum tensor $T_{\\mu\\nu}$ (rows $\\mu$, columns $\\nu$, "
            ...
            "says, although the configuration is not even a solution.")
```

(The caption string, nine lines, is shown here by its first and last line with `...` between them; it is printed in full in the complete text of the notebook and under the figure. The same is done for every caption below.) `save_figure` saves the figure as `20a_1_t1_pair_tensor.png` and shows it. **What figure 1 shows.** Three heat maps of the 64 components $T_{\mu\nu}$ (rows $\mu$, columns $\nu$, from $x_1$ to $x_8$; colour scale in units $H = 1$): left the random configuration, middle its T1 partner, right their sum. The student should see that the middle map is the left one with every colour reversed (red becomes blue of the same depth), and that the right map is white everywhere: the source of the T1 pair is zero, component by component, even though the configuration does not solve the field equation. This is theorem T1 (T1c and T1d) at one point of the deflating history.

**In [9], along the hidden direction: the T1 partner and the T2 mirror copy.**

```python
psi_1 = rng.normal(size=16) + 1j * rng.normal(size=16)  # the spinor Psi_1
z_patch = np.linspace(0.05, np.pi / 2 - 0.02, 160)  # points of the patch
rho, charge = {"one": [], "T1": [], "T2": []}, {"one": [], "T1": [], "T2": []}
```

A second random spinor $\Psi_1$ (the generator continues where it stopped, so the numbers are new but fixed). `np.linspace(a, b, n)` gives $n$ equally spaced numbers from $a$ to $b$: 160 points of the patch from $z = 0.05$ to just below the brane. `rho` and `charge` are dictionaries of empty lists, one list for each of the three objects.

```python
for z_value in z_patch:
    field = psi + 0.3 * (np.pi / 2 - z_value) ** 2 * psi_1  # Psi(z)
    slopes_here = [row.copy() for row in dpsi]  # the derivatives along x1 .. x7
    slopes_here[7] = -3.6 * (np.pi / 2 - z_value) * psi_1  # 6 H dPsi/dz, H = 1
    mirror_slopes = [R8_SIGNS[mu] * (gamma_num[7] @ slopes_here[mu])
                     for mu in range(8)]  # the mirror reverses d/dx8
```

At each point the field is $\Psi(z) = \Psi_0 + \frac{3}{10}(\pi/2 - z)^2\Psi_1$. Its derivatives along $x_1, \dots, x_7$ are those of In [7] (`row.copy()` makes independent copies); its derivative along $x_8$ is $6H\,d\Psi/dz = 6 \cdot \frac{3}{10} \cdot 2(\pi/2 - z)(-1)\Psi_1 = -3.6(\pi/2 - z)\Psi_1$ (chain rule, $H = 1$), which vanishes at the brane and keeps the term $\tan z\,\gamma^{(x_8)}\partial_8\Psi$ finite there. The mirror copy has the derivatives $\gamma^{(x_8)}\partial_\mu\Psi$, with the sign of the $x_8$ derivative reversed, because the mirror $x_8 \to \pi/(6H) - x_8$ reverses that direction.

```python
    here = geometry_at(1, z_value, A4_0, 1.0)
    there = geometry_at(-1, np.pi - z_value, A4_0, 1.0)  # the mirror point
    results = {
        "one": bilinears(here, field, slopes_here, M0, LAM0),
        "T1": bilinears(here, Gamma_num @ field,
                        [Gamma_num @ row for row in slopes_here], -M0, -LAM0),
        "T2": bilinears(there, gamma_num[7] @ field, mirror_slopes, -M0, LAM0),
    }
    for key, result in results.items():
        rho[key].append(-result["T"][3, 3])  # rho = -T_x4x4
        charge[key].append(result["J"][3])  # J^x4
```

The geometry at the point $z$ of the patch and at the mirror point $\pi - z$ of the mirror patch. The three objects: the field with $(m, \lambda)$, its T1 partner with $(-m, -\lambda)$ at the same point, and its T2 mirror copy $\gamma^{(x_8)}\Psi$ with $(-m, \lambda)$ at the mirror point. For each, the energy density $\rho = -T_{x_4x_4}$ (position 3, 3; the notebook computes the tensor $T_{\mu\nu}$ of the pairing records; because $g^{x_4x_4} = -1$, $T^{x_4}{}_{x_4} = g^{x_4x_4}T_{x_4x_4} = -T_{x_4x_4}$, so $-T_{x_4x_4} = +T^{x_4}{}_{x_4}$ in the pairing convention, which is $-T^{x_4}{}_{x_4}$ in the field-theory convention of Section 20.2, that is $\rho$) and the charge density $J^{x_4}$ are appended to their lists.

```python
rho = {key: np.array(values) for key, values in rho.items()}
charge = {key: np.array(values) for key, values in charge.items()}
size = max(np.abs(rho["one"]).max(), np.abs(charge["one"]).max())
check(np.abs(rho["T1"] + rho["one"]).max() < 1e-12 * size
      and np.abs(charge["T1"] + charge["one"]).max() < 1e-12 * size,
      "along z: the T1 partner has -rho and -J^x4 at every point")
check(np.abs(rho["T2"] - rho["one"]).max() < 1e-10 * size
      and np.abs(charge["T2"] - charge["one"]).max() < 1e-10 * size,
      "along z: the T2 copy has the same rho and J^x4 at the mirror point")
```

The dictionary comprehension `{key: np.array(values) for ...}` turns each list into a numpy array, so that whole arrays can be added and compared. `size` is the largest modulus of the field's energy density or charge density along the line; the tolerances are measured relative to it. Two checks at all 160 points: the T1 partner has exactly $-\rho$ and $-J^{x_4}$; the T2 copy has, at the mirror point, the SAME $\rho$ and the SAME $J^{x_4}$. The second tolerance is $10^{-10}$ rather than $10^{-12}$ because the copy is evaluated with a different (mirror-patch) geometry, whose numbers $\sin^{1/6}(\pi - z)$ and $-\cot(\pi - z)$ agree with those of the patch only up to rounding, and near the brane the factor $\tan z = 1/E_8$ is large and amplifies these rounding differences. The cell prints the two PASS lines.

**In [10], figure 2: the profiles across the brane.**

```python
fig, axes = plt.subplots(1, 2, figsize=(12.0, 4.4))
for ax, data, label in ((axes[0], rho, "energy density $\\rho$"),
                        (axes[1], charge, "charge density $J^{x_4}$")):
    ax.plot(z_patch, data["one"], color="tab:blue", label="$\\Psi$, $(m, \\lambda)$")
    ax.plot(z_patch, data["T1"], "--", color="tab:red",
            label="T1 partner $\\Gamma\\Psi$, $(-m, -\\lambda)$")
    ax.plot(z_patch, data["one"] + data["T1"], color="black", linewidth=2.0,
            label="T1 pair: sum")
    ax.plot(np.pi - z_patch, data["T2"], color="tab:green",
            label="T2 copy $\\gamma^{(x_8)}\\Psi$, $(-m, \\lambda)$")
```

Two panels, the energy density on the left and the charge density on the right; the loop draws the same four curves in each. `ax.plot(x, y, ...)` draws a curve through the points; the style string of two minus signs makes it dashed, `color` sets its colour and `label` its name in the legend. The first three curves live on the patch (the field, its T1 partner and their sum); the fourth, the T2 copy, is drawn at its own points $\pi - z$ on the mirror patch.

```python
    ax.axvline(np.pi / 2, color="grey", linestyle=":", linewidth=1.5)
    ax.text(np.pi / 2, ax.get_ylim()[1], " brane", va="top", fontsize=8)
    ax.set_xlabel("hidden coordinate $z = 6Hx_8$")
    ax.set_ylabel(label + " (units $H = 1$)")
handles, names = axes[0].get_legend_handles_labels()
fig.legend(handles, names, loc="lower center", ncol=4, fontsize=8.5,
           bbox_to_anchor=(0.5, -0.06))  # one legend below both panels
axes[0].set_title("T1: reversed at the same point; T2: equal at the mirror point",
                  fontsize=9)
axes[1].set_title("the same for the charge density", fontsize=9)
save_figure(fig, "pair_profiles",
            "Left: the energy density $\\rho = -T_{x_4x_4}$, right: the charge "
            ...
            "the brane, with the same sign: T1 pairs cancel, T2 pairs add.")
```

`ax.axvline` draws the dotted vertical line of the brane $z = \pi/2$, and `ax.text` writes the word brane at its top (`ax.get_ylim()[1]` is the upper end of the vertical axis; `va="top"` hangs the text below that height). The axis labels name the quantities and the units. `get_legend_handles_labels` collects the curves and their names from the left panel, and `fig.legend` draws one legend for both panels, in four columns (`ncol=4`), below them (`bbox_to_anchor=(0.5, -0.06)` places its lower centre slightly below the figure). The two titles follow. The call of `save_figure` saves the figure as `20a_2_pair_profiles.png`; its caption string (twelve lines, shown here by its first and last line with `...` between them) is printed in full in the complete text of the notebook and under the figure. **What figure 2 shows.** Horizontal axis: the hidden coordinate $z$ from 0 to $\pi$, with the brane dotted at $\pi/2$; vertical axis: the energy density (left) and the charge density (right), units $H = 1$. Left of the brane, the blue curve of the field and the red dashed curve of its T1 partner are mirror images of each other in the horizontal axis, and their black sum lies on zero everywhere. Right of the brane, the green curve of the T2 copy is the blue curve reflected in the vertical line of the brane, with the SAME sign. The student should see the essential difference of the two theorems: T1 partners cancel, T2 partners add.

**In [11], the T2 mirror copy does not cancel; figure 3.**

```python
R8 = np.array(R8_SIGNS, dtype=float)  # the reflection R8 of the x8 direction
mirror_dpsi = [R8[mu] * (gamma_num[7] @ dpsi[mu]) for mu in range(8)]
copy = bilinears(geometry_at(-1, np.pi - Z0, A4_0, 1.0), gamma_num[7] @ psi,
                 mirror_dpsi, -M0, LAM0)  # the T2 copy at the mirror point
pulled_back = np.outer(R8, R8) * one["T"]  # R8 T R8
```

`R8` is the diagonal of $R_8 = \mathrm{diag}(1, 1, 1, 1, 1, 1, 1, -1)$. The copy of the configuration of In [7] (with its full jet, including the $x_8$ derivative, which the mirror reverses) is evaluated at the mirror point $\pi - 0.6$. `np.outer(R8, R8)` is the $8 \times 8$ table of products $R_{8,\mu}R_{8,\nu}$; multiplying it entry by entry with $T$ gives $(R_8TR_8)_{\mu\nu}$: the entries with exactly one index $x_8$ change sign, all others stay.

```python
reproduces(np.abs(copy["T"] - pulled_back).max() < 1e-10 * scale,
           "T2 copy: T' = R8 T R8 at the mirror point (64 components)",
           PAIR_PY, "T2.metric.commuting.emt")
reproduces(np.abs(copy["J"] - R8 * one["J"]).max() < 1e-10 * scale,
           "T2 copy: J' = R8 J (the charge density is unchanged)",
           PAIR_PY, "T2.metric.commuting.current")
reproduces(abs(copy["S"] + one["S"]) < 1e-10 * scale, "T2 copy: S' = -S",
           PAIR_PY, "T2.metric.commuting.S_odd")
reproduces(np.abs(copy["E"] + gamma_num[7] @ one["E"]).max() < 1e-10 * scale,
           "T2 copy: E_(-m,lambda)[Psi'] = -gamma^(x8) E_(m,lambda)[Psi]",
           PAIR_PY, "T2.metric.commuting.euler_lagrange_map")
reproduces(np.abs(copy["T"] + one["T"]).max() > 0.1 * scale,
           "T2 pair: the tensors do NOT cancel",
           PAIR_WL, "T2_mirror_energy_momentum_and_current_commuting")
```

Five checks of theorem T2 at the point: the copy's tensor is the pulled-back one, $T' = R_8TR_8$; its current is $J' = R_8J$ (so the charge density $J^{x_4}$ is unchanged); its scalar is $S' = -S$; its residual is $-\gamma^{(x_8)}$ times that of the configuration (so it solves the $(-m, \lambda)$ equation on the mirror patch exactly when the configuration solves the $(m, \lambda)$ equation on the patch); and the sum $T + T'$ is NOT small (more than a tenth of the size of the tensor): a T2 pair has no zero source.

```python
fig, axes = plt.subplots(1, 3, figsize=(12.0, 4.3))
panels = ((one["T"], "$T_{\\mu\\nu}[\\Psi]$ at $z$"),
          (copy["T"], "$T_{\\mu\\nu}$ of the T2 copy at $\\pi - z$"),
          (copy["T"] - pulled_back, "copy minus $R_8TR_8$"))
for ax, (values, title) in zip(axes, panels):
    image = ax.imshow(values, cmap="RdBu_r", vmin=-scale, vmax=scale)
    ax.set_xticks(range(8))
    ax.set_xticklabels(NAMES, fontsize=7)
    ax.set_yticks(range(8))
    ax.set_yticklabels(NAMES, fontsize=7)
    ax.grid(False)
    ax.set_title(title, fontsize=10)
fig.colorbar(image, ax=list(axes), shrink=0.8, label="value (units $H = 1$)")
save_figure(fig, "t2_mirror_tensor",
            "Left: the energy-momentum tensor $T_{\\mu\\nu}$ of the configuration "
            ...
            "the T2 pair has twice the source of one member.")
```

Three new panels: the tensor of the configuration, the tensor of its T2 copy, and the copy minus the pulled-back tensor. The drawing loop is the one of In [8], line for line: a heat map with the same colour scale in each panel, the labels $x_1$ to $x_8$ on both axes, no grid, a title; then the common colour bar, and `save_figure` saves `20a_3_t2_mirror_tensor.png`. **What figure 3 shows.** Three heat maps of $T_{\mu\nu}$ (rows and columns $x_1$ to $x_8$, units $H = 1$, red positive, blue negative): left the configuration at $z = 0.6$, middle its T2 copy at $\pi - 0.6$, right their difference after the pull-back. The student should see that the left and middle maps are equal except in the last row and the last column, whose off-diagonal entries (one index $x_8$) have the opposite colour, and that the right map is white. Unlike the T1 partner, the mirror copy carries the SAME energy: a T2 pair has twice the source of one member.

**In [12], the T1 pair as the only source: Einstein's vacuum equations.**

```python
record = read_json(A4_RECORD)
ad1, ad2 = sp.symbols("ad1 ad2")  # a4' and a4'' (complex allowed)
Lam = sp.symbols("Lambda")  # the cosmological constant
alpha2, alpha3, A = sp.symbols("alpha2 alpha3 A", real=True)
KEYS = ["x1x1", "x4x4", "x5x5", "x8x8"]  # the independent diagonal components
```

The record of the field equations for $a_4$ is read. Its formulas use the names `ad1` and `ad2` for $a_4'$ and $a_4''$; the notebook makes symbols with the same names and, on purpose, does NOT declare them real, so that sympy may find complex solutions if there are any. `Lam` is $\Lambda$; `alpha2`, `alpha3` and `A` are the two higher Lovelock couplings and the slope of the linear member. `KEYS` names the four independent diagonal components (the others repeat these).

```python
def lovelock(order, key):
    """The component key of E_(order) from the record, as a sympy expression."""
    text = record["lovelockTensors"][f"E{order}"][key]["input"].replace("^", "**")
    return sp.sympify(text, locals={"ad1": ad1, "ad2": ad2, "H": H})
```

The record stores each component of $E_{(1)}$, $E_{(2)}$ and $E_{(3)}$ as a text in Wolfram's input form, in which a power is written `^`. `.replace("^", "**")` turns it into Python's form, and `sp.sympify` reads the text as a sympy expression; `locals` makes the names in the text mean the notebook's symbols.

```python
G = {key: lovelock(1, key) for key in KEYS}  # the Einstein tensor
for key in KEYS:
    say(f"G^{key[:2]}_{key[2:]} = {G[key]}")
vacuum = [G[key] + Lam for key in KEYS]  # zero source
solutions = sp.solve(vacuum, [ad1, ad2, Lam], dict=True)
say(f"all solutions of the vacuum equations: {solutions}")
```

`G` holds the four components of the Einstein tensor $E_{(1)} = G$; the loop prints them (`key[:2]` and `key[2:]` are the first two and the last two letters of the key). Output: $G^{x_1}{}_{x_1} = 15H^2 - 3a_4'^2 + a_4''$, $G^{x_4}{}_{x_4} = 21H^2 + 3a_4'^2$, $G^{x_5}{}_{x_5} = 15H^2 - 3a_4'^2 - a_4''$, $G^{x_8}{}_{x_8} = 15H^2 - 3a_4'^2$. `vacuum` is the list of the four vacuum equations $G^\mu{}_\mu + \Lambda = 0$, and `sp.solve` finds ALL solutions for the three unknowns $a_4'$, $a_4''$, $\Lambda$, each as a dictionary. Output: two solutions, $\Lambda = -18H^2$, $a_4'' = 0$ and $a_4' = -iH$ or $+iH$.

```python
found = {(s[ad1], s[ad2], s[Lam]) for s in solutions}
reproduces(found == {(sp.I * H, 0, -18 * H ** 2), (-sp.I * H, 0, -18 * H ** 2)},
           "the only solutions have a4' = +i H or -i H: none is real",
           LEAD_EGB, "no_vacuum_for_H_positive")
difference = sp.expand(vacuum[1] - vacuum[3])  # x4 equation minus x8 equation
total = sp.expand(vacuum[1] + vacuum[3])  # x4 equation plus x8 equation
report("x4 equation minus x8 equation", difference)
report("x4 equation plus x8 equation", total)
```

`found` is the set of the solutions as triples; the check requires exactly the two triples $(\pm iH, 0, -18H^2)$ (`sp.I` is sympy's $i$): no real rate. Then the two combinations of the proof of C1(a): the $x_4$ equation minus the $x_8$ equation and their sum, multiplied out by `sp.expand`. Output: $6H^2 + 6a_4'^2$ and $36H^2 + 2\Lambda$, lines 5 and the remark after line 6 of Section 20.7.

```python
reproduces(difference == 6 * ad1 ** 2 + 6 * H ** 2
           and total == 36 * H ** 2 + 2 * Lam,
           "6 a4'^2 + 6 H^2 = 0 and 36 H^2 + 2 Lambda = 0 (record's lines)",
           A4_WL, "einstein_no_vacuum_solution")
a_real = sp.symbols("a_real", real=True)  # a real value of a4'
reproduces(sp.solve(difference.subs(ad1, a_real), a_real) == [],
           "for real a4' the difference 6 a4'^2 + 6 H^2 never vanishes",
           A4_PY, "einstein_no_vacuum")
```

The first check compares the two combinations with the record's lines. The second substitutes for $a_4'$ a symbol declared real and asks sympy for the real solutions of $6a_4'^2 + 6H^2 = 0$: the answer is the empty list `[]`, line 6 of the proof.

**In [13], figure 4: the two vacuum conditions never meet.**

```python
slopes = np.linspace(-3.0, 3.0, 601)  # a4'/H
lower = -(3 * slopes ** 2 + 21)  # Lambda/H^2 where the x4 equation holds
upper = 3 * slopes ** 2 - 15  # Lambda/H^2 where the x8 equation holds
check(np.min(upper - lower) >= 6.0 - 1e-12, "the two curves stay 6 H^2 apart or more")
```

601 values of $a_4'/H$ from $-3$ to $3$. Solving the $x_4$ equation for $\Lambda$ gives $\Lambda = -(3a_4'^2 + 21H^2)$, a parabola that opens downwards; solving the $x_8$ equation gives $\Lambda = 3a_4'^2 - 15H^2$, a parabola that opens upwards (in units of $H^2$). Their vertical distance is $6a_4'^2 + 6H^2 \ge 6H^2$; the check confirms it at all 601 points.

```python
fig, ax = plt.subplots(figsize=(7.0, 4.6))
ax.plot(slopes, lower, color="tab:red", label="$x_4$: $\\Lambda = -(3a_4'^2 + 21H^2)$")
ax.plot(slopes, upper, color="tab:blue", label="$x_8$: $\\Lambda = 3a_4'^2 - 15H^2$")
ax.fill_between(slopes, lower, upper, color="grey", alpha=0.2,
                label="gap $6a_4'^2 + 6H^2$")
ax.annotate("", xy=(1.0, -12.0), xytext=(1.0, -24.0),
            arrowprops={"arrowstyle": "<->", "color": "black"})
ax.text(1.12, -19.3, "$12H^2$ at $a_4' = H$\n(the author's history)", fontsize=8,
        va="top")  # va="top": the text hangs below the given height
ax.axhline(-18.0, color="black", linestyle=":", linewidth=1.0)
ax.text(-2.95, -17.3, "$\\Lambda = -18H^2$: both hold only for $a_4' = \\pm iH$",
        fontsize=8)
ax.set_xlabel("$a_4'/H$")
ax.set_ylabel("$\\Lambda/H^2$")
ax.set_title("Einstein gravity with zero source: the two conditions never meet")
ax.legend(fontsize=8, loc="lower right")
save_figure(fig, "einstein_vacuum_parabolas",
            "The vacuum equations of Einstein gravity for the author's metric, the "
            ...
            "(dotted line), are not real.")
```

The two parabolas are drawn in red and blue; `fill_between` shades the band between them in grey (`alpha=0.2`: 20 per cent opaque). `ax.annotate` with an empty text draws a double arrow at $a_4' = H$ from $\Lambda = -24H^2$ to $-12H^2$, the gap $12H^2$ of the deflating history, and `ax.text` labels it (`\n` starts a new line). `ax.axhline` draws the dotted horizontal line $\Lambda = -18H^2$, the value at which the two equations would hold together if $a_4'$ could be $\pm iH$. **What figure 4 shows.** Horizontal axis: the rate $a_4'/H$; vertical axis: the cosmological constant $\Lambda/H^2$. A vacuum would be a point on both parabolas, and there is none: the grey band between them is never thinner than $6H^2$ and is $12H^2$ thick at the author's history. The student should see at a glance why no choice of the rate and of $\Lambda$ removes the need for a source in Einstein gravity, and therefore why a T1 pair, whose source is zero, cannot be the only source of the author's metric.

**In [14], what the geometry requires and what a pair supplies.**

```python
couplings = {"alpha1": 1, "alpha2": alpha2, "alpha3": alpha3, "H": H, "ad1": ad1,
             "ad2": ad2, "AA": A}  # alpha1 = 1 throughout
null_text = record["generalSource"]["nullCombinations"]["kappa(rho+p8)"]["input"]
null_required = sp.sympify(null_text.replace("^", "**"), locals=couplings)
V_text = record["linearMember"]["vacuumFactor"]["input"]
V = sp.sympify(V_text.replace("^", "**"), locals=couplings)
```

`couplings` tells `sympify` what the names in the record's texts mean; $\alpha_1 = 1$ throughout (the record writes the slope as `AA`). The record's null combination $\kappa(\rho + p_8)$ for a general source and its vacuum factor $V$ of the linear member are read as sympy expressions.

```python
lovelock_sum = {key: lovelock(1, key) + alpha2 * lovelock(2, key)
                + alpha3 * lovelock(3, key) for key in KEYS}
own_null = -(lovelock_sum["x4x4"] - lovelock_sum["x8x8"])
check(sp.expand(own_null - null_required) == 0,
      "the null combination of the record equals -(E^x4_x4 - E^x8_x8)")
```

`lovelock_sum` is $\sum_k\alpha_kE_{(k)}$ for the four components. `own_null` is the notebook's own null combination, $-\sum_k\alpha_k(E_{(k)}{}^{x_4}{}_{x_4} - E_{(k)}{}^{x_8}{}_{x_8})$, derived in Section 20.7; the check finds it equal to the record's.

```python
linear = {ad1: A * H, ad2: 0}  # the linear member a4 = A H x4 + a0
reproduces(sp.expand(own_null.subs(linear) + 6 * (A ** 2 + 1) * H ** 2 * V) == 0,
           "linear member: kappa (rho + p8) = -6 (A^2 + 1) H^2 V",
           A4_WL, "linear_member_vacuum_factor")
reproduces(sp.expand(V.subs({alpha2: 0, alpha3: 0})) == 1
           and sp.expand(null_required.subs({alpha2: 0, alpha3: 0})
                         + 6 * ad1 ** 2 + 6 * H ** 2) == 0,
           "Einstein: V = 1 and kappa (rho + p8) = -6 (a4'^2 + H^2)",
           A4_PY, "einstein_null_energy_x8")
reproduces(sp.expand(null_required.subs({alpha2: 0, alpha3: 0})
                     + 6 * ad1 ** 2 + 6 * H ** 2) == 0,
           "the same null combination from the lead's independent Einstein tensor",
           LEAD_EGB, "einstein_null_energy")
```

For the linear member ($a_4' = AH$, $a_4'' = 0$) the null combination equals $-6(A^2 + 1)H^2V$. In Einstein gravity ($\alpha_2 = \alpha_3 = 0$) $V = 1$ and the null combination is $-6(a_4'^2 + H^2)$, which the record's sympy report and the lead's independent report both state.

**In [15], figure 5: the required null combination against the slope.**

```python
A_axis = np.linspace(0.0, 2.0, 401)
V_numeric = sp.lambdify((A, alpha2, alpha3), V.subs(H, 1), "numpy")
fig, ax = plt.subplots(figsize=(7.0, 4.4))
for x2, style, label in ((0.0, "-", "Einstein ($\\alpha_2 = 0$)"),
                         (1 / 48, "--", "Gauss-Bonnet, $\\alpha_2H^2 = 1/48$"),
                         (1 / 40, "-.", "Gauss-Bonnet, $\\alpha_2H^2 = 1/40$")):
    required = -6 * (A_axis ** 2 + 1) * V_numeric(A_axis, x2, 0.0)
    ax.plot(A_axis, required, style, label=label)
```

401 slopes $A$ from 0 to 2. `V_numeric` is $V$ as a numpy function of $A$, $\alpha_2$ and $\alpha_3$ in units $H = 1$. The loop draws the required $\kappa(\rho + p_8)/H^2 = -6(A^2 + 1)V$ for three theories: Einstein gravity (solid), Gauss-Bonnet with $\alpha_2H^2 = 1/48$ (dashed) and with $1/40$ (dash-dotted).

```python
ax.axhline(0.0, color="black", linewidth=2.0, label="what a T1 pair supplies: 0")
ax.plot([1.0, 0.0], [0.0, 0.0], "o", color="tab:red", markersize=7,
        label="a T1 pair fits: $V = 0$")
ax.set_xlabel("slope $A$ of the linear member $a_4 = AHx_4$")
ax.set_ylabel("required $\\kappa(\\rho + p_8)/H^2$")
ax.set_title("The source the geometry requires, and the zero of a T1 pair")
ax.legend(fontsize=8, loc="lower left")
save_figure(fig, "null_combination",
            "The null combination $\\kappa(\\rho + p_8)$ (energy density plus the "
            ...
            "$\\alpha_2H^2 = 1/48$, and $A = 0$ for $1/40$).")
```

The thick black line at zero is what a T1 pair supplies; the two red dots mark where a requirement curve reaches it. **What figure 5 shows.** Horizontal axis: the slope $A$; vertical axis: the null combination the field equations require of any source, in units $H^2$. The Einstein curve, $-6(A^2 + 1)$, stays at or below $-6$ for every slope, so it never meets the black line: in Einstein gravity a T1 pair is never the only source. Each Gauss-Bonnet curve reaches zero at exactly one slope: the dashed one crosses it at $A = 1$ (the author's history) for $\alpha_2H^2 = 1/48$, and the dash-dotted one touches it at $A = 0$ for $1/40$ and is positive at every other slope (there $V = -A^2/5$, so the requirement is $6A^2(A^2 + 1)/5$). The student should see that C1(a) is a property of Einstein gravity, not of every theory of gravity.

**In [16], Einstein-Gauss-Bonnet gravity: when a zero source is allowed.**

```python
V_gb = sp.expand(V.subs(alpha3, 0))
A_squared = sp.solve(V_gb, A ** 2)[0]
reproduces(sp.simplify(A_squared - (1 - 40 * alpha2 * H ** 2)
                       / (8 * alpha2 * H ** 2)) == 0,
           "Gauss-Bonnet vacuum: A^2 = (1 - 40 alpha2 H^2)/(8 alpha2 H^2)",
           A4_WL, "einstein_gauss_bonnet_vacuum_linear")
```

$V$ with $\alpha_3 = 0$; `sp.solve(V_gb, A ** 2)` solves $V = 0$ for $A^2$ (sympy treats $A^2$ as the unknown) and `[0]` takes the one solution. The check compares it with the formula derived line by line in Section 20.7.

```python
x2_author = sp.solve(A_squared.subs(H, 1) - 1, alpha2)[0]  # A = 1, H = 1
report("alpha2 H^2 for a vacuum with A = 1", x2_author)
gauss_bonnet = {key: (lovelock(1, key) + alpha2 * lovelock(2, key))
                .subs({ad1: H, ad2: 0, alpha2: x2_author / H ** 2})
                for key in KEYS}
Lam_author = sp.simplify(-gauss_bonnet["x4x4"])  # Lambda from the x4 equation
report("Lambda of that vacuum", Lam_author)
```

Setting $A^2 = 1$ (with $H = 1$) and solving for $\alpha_2$ gives $1/48$ (Output: RESULT $\alpha_2H^2$ for a vacuum with $A = 1$ = 1/48). The four components of $E_{(1)} + \alpha_2E_{(2)}$ are evaluated at $a_4' = H$, $a_4'' = 0$, $\alpha_2 = 1/(48H^2)$; the vacuum $x_4$ equation $E^{x_4}{}_{x_4} + \Lambda = 0$ gives $\Lambda = -E^{x_4}{}_{x_4}$. Output: RESULT Lambda of that vacuum = $-12H^2$, the value derived by hand in Section 20.7.

```python
reproduces(x2_author == sp.Rational(1, 48) and Lam_author == -12 * H ** 2
           and all(sp.simplify(gauss_bonnet[key] + Lam_author) == 0 for key in KEYS),
           "a4 = H x4 solves the Gauss-Bonnet vacuum equations exactly",
           A4_PY, "einstein_gauss_bonnet_vacuum_linear")
zero_off = all(record["lovelockTensors"][f"E{k}"][key]["input"] == "0"
               for k in (1, 2, 3) for key in ("x4x8", "x8x4"))
check(zero_off, "the mixed components x4x8 and x8x4 of E_(1..3) are 0 in the record")
```

The check requires $\alpha_2H^2 = 1/48$, $\Lambda = -12H^2$, and that ALL FOUR independent vacuum equations vanish exactly for the deflating history. The second check confirms that the record has no mixed component $x_4x_8$ in any of the three Lovelock tensors, so no further equation remains: in this theory the author's deflating history is a vacuum, and a T1 pair CAN be its only source.

```python
Lam_curve = sp.simplify(-(lovelock(1, "x4x4") + alpha2 * lovelock(2, "x4x4"))
                        .subs({ad1: A * H, ad2: 0}).subs(A ** 2, A_squared))
say(f"Lambda along the vacuum curve: {sp.factor(Lam_curve)}")
```

Along the whole family of Gauss-Bonnet vacua the cosmological constant is $\Lambda = -E^{x_4}{}_{x_4}$ at $a_4' = AH$ with $A^2$ replaced by the vacuum formula; `sp.factor` writes it as a fraction. Output: $3(3840H^4\alpha_2^2 - 192H^2\alpha_2 + 1)/(16\alpha_2)$, that is $720\alpha_2H^4 - 36H^2 + 3/(16\alpha_2)$; at $\alpha_2 = 1/(48H^2)$ this is $15H^2 - 36H^2 + 9H^2 = -12H^2$.

**In [17], figure 6: the Gauss-Bonnet vacua.**

```python
x_axis = np.linspace(0.004, 1 / 40, 400)  # alpha2 H^2
A_curve = np.sqrt((1 - 40 * x_axis) / (8 * x_axis))
Lam_numeric = sp.lambdify(alpha2, Lam_curve.subs(H, 1), "numpy")
fig, axes = plt.subplots(1, 2, figsize=(12.0, 4.3))
axes[0].plot(x_axis, A_curve, color="tab:purple")
axes[0].plot([1 / 48], [1.0], "o", color="tab:red", markersize=8,
             label="$A = 1$ at $\\alpha_2H^2 = 1/48$")
axes[0].set_ylabel("slope $A$ of the vacuum $a_4 = AHx_4$")
axes[1].plot(x_axis, Lam_numeric(x_axis), color="tab:purple")
axes[1].plot([1 / 48], [-12.0], "o", color="tab:red", markersize=8,
             label="$\\Lambda = -12H^2$ at $\\alpha_2H^2 = 1/48$")
axes[1].set_ylabel("$\\Lambda/H^2$ of that vacuum")
```

The 400 values of the coupling $\alpha_2H^2$ run from 0.004 to the limit $1/40$. For each of them the array `A_curve` holds the slope of the vacuum, $\sqrt{(1 - 40\alpha_2H^2)/(8\alpha_2H^2)}$, computed with the square root `np.sqrt`; it is drawn in the left panel. The right panel shows the cosmological constant of each vacuum, the expression `Lam_curve` of In [16] turned into a numpy function. The red dots mark the author's history.

```python
for ax in axes:
    ax.set_xlabel("Gauss-Bonnet coupling $\\alpha_2H^2$")
    ax.axvline(1 / 40, color="grey", linestyle=":")
    ax.legend(fontsize=8)
axes[0].set_title("no vacuum for $\\alpha_2 \\to 0$ (Einstein), $A = 0$ at $1/40$",
                  fontsize=9)
axes[1].set_title("the cosmological constant each vacuum needs", fontsize=9)
save_figure(fig, "gauss_bonnet_vacuum",
            "The vacua of Einstein-Gauss-Bonnet gravity ($\\alpha_1 = 1$, "
            ...
            "$\\alpha_2H^2 = 1/48$ and $\\Lambda = -12H^2$ (checked exactly).")
```

Both panels get the horizontal label, the dotted limit $\alpha_2H^2 = 1/40$ and a legend. **What figure 6 shows.** Horizontal axis: the Gauss-Bonnet coupling $\alpha_2H^2$. Left: the slope $A$ of the vacuum; it grows without bound as $\alpha_2 \to 0$, the Einstein limit, which has no vacuum, and falls to $A = 0$ at $1/40$. Right: the cosmological constant $\Lambda/H^2$ that the same vacuum needs. The student should see that each coupling between 0 and $1/40$ has exactly one vacuum among the linear members, and that the author's deflating history $A = 1$ is the one at $\alpha_2H^2 = 1/48$, with $\Lambda = -12H^2$.

**In [18], third order: one straight line of vacua per slope; figure 7.**

```python
y_line = sp.solve(V.subs({alpha2: sp.Symbol("x"), alpha3: sp.Symbol("y"), H: 1}),
                  sp.Symbol("y"))[0]
wanted = ((8 * A ** 2 + 40) * sp.Symbol("x") - 1) / (72 * A ** 4 + 144 * A ** 2 + 360)
check(sp.simplify(y_line - wanted) == 0, "for fixed A the vacua form a straight line")
check(V.subs({alpha2: 0, alpha3: 0}) == 1, "Einstein gravity (origin) has V = 1")
```

$V = 0$ is solved for $y = \alpha_3H^4$ with $x = \alpha_2H^2$ (`sp.Symbol("x")` makes one symbol). The check compares the solution with the straight line derived in Section 20.7; the second check confirms that the origin $x = y = 0$, Einstein gravity, has $V = 1$ and is no vacuum.

```python
x_plot = np.linspace(-0.01, 0.05, 200)
fig, ax = plt.subplots(figsize=(7.0, 4.6))
for slope_A in (0.0, 0.5, 1.0, 2.0, 3.0):
    line = ((8 * slope_A ** 2 + 40) * x_plot - 1) / (
        72 * slope_A ** 4 + 144 * slope_A ** 2 + 360)
    ax.plot(x_plot, 1000 * line, label=f"$A = {slope_A:g}$")
ax.plot([0.0], [0.0], "s", color="black", markersize=8,
        label="Einstein gravity: no vacuum")
ax.plot([1 / 48], [0.0], "o", color="tab:red", markersize=8,
        label="section 13: $A = 1$, $\\alpha_3 = 0$")
ax.axhline(0.0, color="grey", linewidth=0.8)
ax.axvline(0.0, color="grey", linewidth=0.8)
ax.set_xlabel("$\\alpha_2H^2$")
ax.set_ylabel("$1000\\,\\alpha_3H^4$")
ax.set_title("Couplings for which $a_4 = AHx_4$ is a vacuum (third order)")
ax.legend(fontsize=8, loc="upper left")
save_figure(fig, "third_order_vacua",
            "The Einstein-Lovelock couplings for which the linear member "
            ...
            "author's history $A = 1$ at $\\alpha_2H^2 = 1/48$.")
```

For five slopes the line is drawn, its height multiplied by 1000 so that the small values of $\alpha_3H^4$ are readable (`{slope_A:g}` prints a number without needless zeros). The black square is the origin, Einstein gravity; the red dot is the Gauss-Bonnet vacuum of In [16] (the legend's "section 13" is the notebook's own section). **What figure 7 shows.** Horizontal axis: $\alpha_2H^2$; vertical axis: $1000\,\alpha_3H^4$. For each slope $A$ the couplings for which $a_4 = AHx_4$ is a vacuum form a straight line; the five coloured lines all pass below the origin. The student should see that Einstein gravity, the black square, lies on no line, while every line contains infinitely many theories with a vacuum, among them the red dot of the author's history.

**In [19], the last check.**

```python
figure_names = ["t1_pair_tensor", "pair_profiles", "t2_mirror_tensor",
                "einstein_vacuum_parabolas", "null_combination",
                "gauss_bonnet_vacuum", "third_order_vacua"]
paths = [output_file(f"{FIGURE_FOLDER}/20a_{k}_{name}.png")
         for k, name in enumerate(figure_names, 1)]
check(all(path.is_file() for path in paths),
      "every figure file of this notebook exists")
all_checks_passed()
```

`enumerate(list, 1)` pairs each name with its number, starting at 1, so that `paths` lists the seven figure files `20a_1_t1_pair_tensor.png` to `20a_7_third_order_vacua.png`. The check confirms that all exist, and `all_checks_passed()` prints the last line. Output: PASS every figure file of this notebook exists, and ALL 37 CHECKS PASSED (notebook 20a).

### 20.12 One universe without a partner: an exact solution and its two partners

**Why an example.** The pairing theorems speak about ALL solutions at once, and so they are easy to misread. One exact solution makes every statement a number that can be checked. We build one **universe** of the commuting field dirac16complex00: a solution of its field equation that is, by itself, the COMPLETE source of the author's metric with the exponentially deflating history $a_4 = Hx_4$ in Einstein gravity. Then we build its T1 partner, the T1 pair and its T2 mirror copy, and ask of each whether it solves its own field equation and whether it can be the source of the author's metric. The answer teaches the lesson of the whole chapter in one example: the universe needs no partner, and the partners exist as solutions of OTHER equations, which nothing in the theory forces anyone to realise.

**Status.** The universe below and the statements about its partners are COMPUTED by Notebook 20b and derived by hand in this section (exact arithmetic for the field equations and for the two Einstein conditions; floating point, to $10^{-10}$, for the 64 components of the Einstein equations at nine points). They are a result of this book, not a Revision record. They rest on PROVED record statements, which are named at each step, and on these ASSUMED inputs: Einstein gravity ($\alpha_1 = 1$, $\alpha_2 = \alpha_3 = 0$); the classical commuting field dirac16complex00 (not the quantised dirac16complex); the sign convention $\sigma_T = +1$ of the record of the field equations for $a_4$ (it fixes the overall sign of the energy-momentum tensor; Chapter 12); the chosen numbers $A = 1$, $\Lambda = -36H^2$ and $M = -5H$; and, for the mirror copy, the Z2 construction across the brane. Units: $H = \kappa = 1$.

**Step 1: the field equation of a condensate.** A **condensate** is a field that depends on the time $x_4$ only, $\Phi = \Phi(x_4)$. Its derivatives along the seven other directions vanish, $\gamma^{x_4} = \gamma^{(x_4)}$ because $g_{x_4x_4} = -1$, and the spin connection enters the field equation only through $\sum_\mu\gamma^\mu\Omega_\mu = 3H\gamma^{(x_8)}$ (`python-a4-report.json`, check `authorT16_gravity_term`; `emt-divergence-and-spin-connection.json`, check `gamma_Omega_equals_3H_gamma8`). So the field equation $\gamma^\mu D_\mu\Phi = (m + \lambda S)\Phi$ becomes

$$
\gamma^{(x_4)}\Phi' + 3H\gamma^{(x_8)}\Phi = M\Phi,\qquad M = m + \lambda S ,
$$

where $\Phi' = d\Phi/dx_4$ and $M$ is the **effective mass**. Subtracting $3H\gamma^{(x_8)}\Phi$ from both sides,

$$
\gamma^{(x_4)}\Phi' = \big(M - 3H\gamma^{(x_8)}\big)\Phi .
$$

Multiplying from the left by $-\gamma^{(x_4)}$, and using $(-\gamma^{(x_4)})\gamma^{(x_4)} = -\eta^{x_4x_4}I_{16} = I_{16}$ (the Clifford relation with $\eta^{x_4x_4} = -1$),

$$
\Phi' = \mathcal{A}\Phi,\qquad \mathcal{A} = -\gamma^{(x_4)}\big(M - 3H\gamma^{(x_8)}\big)
$$

(`wolfram-a4-report.json`, check `condensate_equation_x8_consistent`). Chapter 12 derives line by line two facts about $\mathcal{A}$, which we use here: $\mathcal{A}^2 = -(M^2 - 9H^2)I_{16}$, so for $M^2 > 9H^2$ every eigenvalue of $\mathcal{A}$ is $+iw$ or $-iw$ with the **frequency** $w = \sqrt{M^2 - 9H^2}$; and $C\mathcal{A} + \mathcal{A}^TC = 0$, so the density $S = \bar\Phi\Phi$ does not change in time (`python-a4-report.json`, check `authorT16_condensate_S_constant`). An eigenvector $\Phi_0$ with $\mathcal{A}\Phi_0 = -iw\Phi_0$ gives the solution $\Phi(x_4) = e^{-iwx_4}\Phi_0$, because its derivative is $-iw\Phi = \mathcal{A}\Phi$.

**Step 2: its source.** The record proves for a condensate that the diagonal of the kinetic tensor is $K^{x_4}{}_{x_4} = MS$ and zero in the seven other directions (`python-a4-report.json`, check `authorT16_condensate_kinetic_diagonal`), and that the off-diagonal components of its energy-momentum tensor are multiples of 15 **three-gamma bilinears** $\bar\Phi\gamma^{(a)}\gamma^{(b)}\gamma^{(c)}\Phi$ (`wolfram-a4-report.json`, check `condensate_offdiagonal_are_three_gamma_bilinears`). When these 15 numbers vanish, the tensor is diagonal with

$$
\rho = mS + \tfrac{\lambda}{2}S^2,\qquad p_3 = p_t = p_8 = p = \tfrac{\lambda}{2}S^2
$$

(Chapter 12 derives both lines from $L = MS - mS - \frac{\lambda}{2}S^2 = \frac{\lambda}{2}S^2$). Two combinations will be needed. Adding,

$$
\rho + p = mS + \lambda S^2 = (m + \lambda S)S = MS ,
$$

because $\frac{\lambda}{2}S^2 + \frac{\lambda}{2}S^2 = \lambda S^2$, and then $S$ is taken out. Subtracting,

$$
\rho - p = mS ,
$$

because the two terms $\frac{\lambda}{2}S^2$ cancel.

**Step 3: the two Einstein conditions.** For the linear member $a_4 = AHx_4$ we have $a_4' = AH$ and $a_4'' = 0$. The record's Einstein tensor (`python-a4-report.json`, check `einstein_components`) then gives $G^{x_4}{}_{x_4} = (3A^2 + 21)H^2$ and $G^{x_1}{}_{x_1} = G^{x_5}{}_{x_5} = G^{x_8}{}_{x_8} = (15 - 3A^2)H^2$. With $T^{x_4}{}_{x_4} = -\rho$ and $T^{x_8}{}_{x_8} = p$, the time equation and the hidden equation are

$$
(3A^2 + 21)H^2 + \Lambda = -\kappa\rho,\qquad (15 - 3A^2)H^2 + \Lambda = \kappa p ;
$$

the equations for $x_1, x_2, x_3$ and for $x_5, x_6, x_7$ are the hidden equation again, because their components of $G$ and of $T$ are the same, and every off-diagonal equation reads $0 = 0$ once the 15 three-gamma bilinears vanish. Subtracting the second equation from the first removes $\Lambda$:

$$
(3A^2 + 21 - 15 + 3A^2)H^2 = -\kappa\rho - \kappa p\quad\Longrightarrow\quad 6(A^2 + 1)H^2 = -\kappa MS ,
$$

where the last step collects $3A^2 + 3A^2 = 6A^2$ and $21 - 15 = 6$ and uses $\rho + p = MS$. Adding the two equations removes $A$:

$$
(3A^2 + 21 + 15 - 3A^2)H^2 + 2\Lambda = -\kappa\rho + \kappa p\quad\Longrightarrow\quad 36H^2 + 2\Lambda = -\kappa mS ,
$$

using $-\kappa(\rho - p) = -\kappa mS$. These are the record's two conditions (`python-a4-report.json` and `wolfram-a4-report.json`, check `condensate_einstein_quadratic_U`):

$$
\kappa MS = -6(A^2 + 1)H^2,\qquad \kappa mS = -(36H^2 + 2\Lambda) .
$$

**Step 4: the numbers of the universe.** We choose $A = 1$ (the author's deflating history: 3-space grows like $e^{x_4}$, the three extra times shrink like $e^{-x_4}$), $\Lambda = -36$ and $M = -5$. The choice $|M| = 5 > 3$ makes the condensate oscillate, with the frequency $w = \sqrt{25 - 9} = 4$. The choice of $\Lambda$ gives the universe a positive energy density: the time equation says $\kappa\rho = -(24 + \Lambda)$ at $A = 1$, which is positive exactly when $\Lambda < -24$. Line by line:

1. The first condition with $\kappa = 1$: $MS = -6 \cdot 2 = -12$, so $S = -12/M = -12/(-5) = 12/5$.
2. The second condition: $mS = -(36 + 2 \cdot (-36)) = -(36 - 72) = 36$, so $m = 36/S = 36 \cdot 5/12 = 15$.
3. The definition $M = m + \lambda S$ solved for $\lambda$: $\lambda = (M - m)/S = (-5 - 15) \cdot 5/12 = -100/12 = -25/3$.
4. The energy density: $\rho = mS + \frac{\lambda}{2}S^2 = 36 + \big(-\frac{25}{6}\big)\cdot\frac{144}{25} = 36 - 24 = 12$.
5. The pressure: $p = \frac{\lambda}{2}S^2 = -24$; the equation of state is $w_{\mathrm{EoS}} = p/\rho = -2$.

Two checks of the arithmetic: $\rho + p = -12 = MS = (-5)(12/5)$, and $\rho - p = 36 = mS = 15 \cdot 12/5$. So the universe has mass $m = +15$ and coupling $\lambda = -25/3$.

**Step 5: the condensate itself.** It remains to find a spinor $\Phi_0$ with $\mathcal{A}\Phi_0 = -4i\Phi_0$, all 15 three-gamma bilinears zero, and $S = 12/5$. The record's recipe (`wolfram-a4-report.json`, check `condensate_diagonal_witness_exact`): take the eigenvector $v_1$ of $\mathcal{A}$ with the eigenvalue $-iw$ on which the three products $\gamma^{(x_1)}\gamma^{(x_5)}$, $\gamma^{(x_2)}\gamma^{(x_6)}$ and $\gamma^{(x_3)}\gamma^{(x_7)}$ all have the value $-1$, the eigenvector $v_2$ with the same eigenvalue on which they all have the value $+1$, the number $c = \overline{v_1^\dagger Cv_2}$ (the bar over a number is its complex conjugate), and the family $\Phi_0(t) = v_1 + t\,c\,v_2$ with a real parameter $t$. Chapter 12 shows that every member of the family has all 15 bilinears zero and the density $S(t) = 2t\,|v_1^\dagger Cv_2|^2$, which is linear in $t$. Notebook 20b solves $S(t) = 12/5$ exactly and finds $t = 15/512$; by the formula for $S(t)$ this means $|v_1^\dagger Cv_2|^2 = (12/5)/(2t) = (12/5)(256/15) = 1024/25$, the value Chapter 12 finds at $M = -5$. The universe is

$$
\Phi(x_4) = e^{-4ix_4}\,\Phi_0(15/512),
$$

and its **charge density** is $J^{x_4} = \Phi^\dagger B\Phi = -3$, the same at every time because $|e^{-4ix_4}|^2 = 1$ (COMPUTED exactly, Notebook 20b, In [5]). The universe solves its field equation exactly at every time, and its energy-momentum tensor solves all 64 Einstein equations of the author's metric with $a_4 = Hx_4$ and $\Lambda = -36H^2$, at every point checked (Notebook 20b, In [5] and In [6]). It is a complete universe of this theory, and nothing in it refers to a partner. This is the record's sentence made concrete: "a single universe with mass $+m$ is an equally valid solution without its partner" (`Revision/docs/PAIR_CREATION_PROOFS.md`, section 11.3).

**Step 6: the T1 partner $\Gamma\Phi$.** By theorem T1 the field $\Gamma\Phi$ solves the field equation with $(-m, -\lambda) = (-15, 25/3)$. We check the pieces by hand. Its density is $S' = S = 12/5$ (step 5 of Section 20.5), so its effective mass is

$$
M' = -m + (-\lambda)S' = -(m + \lambda S) = -M = 5 .
$$

Its matrix is $\mathcal{A}' = -\gamma^{(x_4)}(M' - 3H\gamma^{(x_8)}) = -\gamma^{(x_4)}(-M - 3H\gamma^{(x_8)})$. We show that it equals $\Gamma\mathcal{A}\Gamma$, line by line:

$$
\Gamma\mathcal{A}\Gamma = -\Gamma\gamma^{(x_4)}\big(M - 3H\gamma^{(x_8)}\big)\Gamma = -\Gamma\gamma^{(x_4)}\Gamma\;\Gamma\big(M - 3H\gamma^{(x_8)}\big)\Gamma ,
$$

by inserting $\Gamma\Gamma = I_{16}$ in the middle;

$$
= -\big(-\gamma^{(x_4)}\big)\big(M + 3H\gamma^{(x_8)}\big) = \gamma^{(x_4)}\big(M + 3H\gamma^{(x_8)}\big) ,
$$

because $\Gamma\gamma^{(a)}\Gamma = -\gamma^{(a)}\Gamma\Gamma = -\gamma^{(a)}$ for every gamma (step 1 of Section 20.5) and $\Gamma M\Gamma = M$ for the number $M$;

$$
= -\gamma^{(x_4)}\big(-M - 3H\gamma^{(x_8)}\big) = \mathcal{A}' ,
$$

by taking out the factor $-1$. Two matrices related by $\mathcal{A}' = \Gamma\mathcal{A}\Gamma^{-1}$ are called **similar**; they have the same eigenvalues, because $\mathcal{A}v = \mu v$ gives $\mathcal{A}'(\Gamma v) = \Gamma\mathcal{A}v = \mu\,\Gamma v$. So the partner oscillates with the SAME frequency $w = 4$: the opposite sign of its energy is not an opposite frequency. (The record proves the same kind of statement for the one-particle Hamiltonians, $\Gamma h_m\Gamma = h_{-m}$: `wolfram-pairing.json`, check `Q_one_particle_maps`.) By (T1c) its tensor is $T' = -T$: $\rho' = -12$, $p' = +24$, and its charge density is $+3$.

**Step 7: the partner alone is not a source of the author's metric.** In Section 20.7 we derived what Einstein gravity requires of every source of the author's metric, for every $a_4$:

$$
\kappa(\rho + p_8) = -6(a_4'^2 + H^2) \le -6H^2 .
$$

The universe supplies $\kappa(\rho + p_8) = 12 - 24 = -12$, which meets the requirement exactly when $a_4'^2 + 1 = 2$, that is $a_4' = \pm H$: the deflating history $+H$ (and its mirror choice $-H$; the equations do not select the sign, Chapter 12). The partner supplies $\kappa(\rho' + p_8') = -12 + 24 = +12$, which is larger than $-6H^2$, the largest value the requirement can take. So no real rate $a_4'$ and no $\Lambda$ make the partner alone a source of the author's metric. The partner's tensor does not depend on $a_4$ (the condensate does not feel the deflation, step 1), so this holds for every member of the author's family $a_4(x_4)$, not only for the linear one. The partner is a solution of ITS field equation in the author's geometry, as T1 says, but it cannot produce that geometry. (Status: PROVED here by hand from the record's null combination, `python-a4-report.json`, check `einstein_null_energy_x8`; checked by Notebook 20b, In [7].)

**Step 8: the T1 pair.** With the universe and its partner as the only source, the source is $T + T' = 0$ (T1d), and the Einstein residual is $G^\mu{}_\nu + \Lambda\delta^\mu_\nu$. At $a_4' = H$ and $\Lambda = -36H^2$ it is

$$
\begin{aligned}
G^\mu{}_\nu + \Lambda\delta^\mu_\nu &= \mathrm{diag}(12, 12, 12, 24, 12, 12, 12, 12)H^2 - 36H^2\,\delta^\mu_\nu \\
&= \mathrm{diag}(-24, -24, -24, -12, -24, -24, -24, -24)H^2 \neq 0 ,
\end{aligned}
$$

where the first matrix is $G$ (step 3 with $A = 1$: $15 - 3 = 12$ and $3 + 21 = 24$). This is corollary C1 on the example: the pair does not solve the equations that the universe alone solves.

**Step 9: the T2 mirror copy.** By theorem T2 (Section 20.6, with $m$ replaced by $-m$) the field $\Phi''(\pi - z) = \gamma^{(x_8)}\Phi(z)$ on the mirror patch solves the field equation with $(-m, \lambda) = (-15, -25/3)$ there. For the condensate, which does not depend on $z$, the copy is simply $\gamma^{(x_8)}\Phi(x_4)$. Its density is $S'' = -S$ (Section 20.6), so its effective mass is

$$
M'' = -m + \lambda S'' = -m - \lambda S = -M = 5 .
$$

On the mirror patch the spin-connection term is $-3H\gamma^{(x_8)}$ (computed by Notebook 20a, In [5]; there the positive length of the hidden direction is $-\cot z$). We check the copy's field equation by hand. Multiply the universe's equation $\gamma^{(x_4)}\Phi' + 3H\gamma^{(x_8)}\Phi = M\Phi$ from the left by $-\gamma^{(x_8)}$:

$$
-\gamma^{(x_8)}\gamma^{(x_4)}\Phi' - 3H\gamma^{(x_8)}\gamma^{(x_8)}\Phi = -M\gamma^{(x_8)}\Phi .
$$

In the first term use $-\gamma^{(x_8)}\gamma^{(x_4)} = \gamma^{(x_4)}\gamma^{(x_8)}$ (the Clifford relation for the two different directions $x_4$ and $x_8$) and $\gamma^{(x_8)}\Phi' = (\gamma^{(x_8)}\Phi)'$ (a constant matrix comes out of the derivative); in the second term group the factors as $(-3H\gamma^{(x_8)})(\gamma^{(x_8)}\Phi)$; on the right write $-M = M''$:

$$
\gamma^{(x_4)}\big(\gamma^{(x_8)}\Phi\big)' + \big(-3H\gamma^{(x_8)}\big)\big(\gamma^{(x_8)}\Phi\big) = M''\big(\gamma^{(x_8)}\Phi\big) ,
$$

which is exactly the condensate equation on the mirror patch for the field $\gamma^{(x_8)}\Phi$ with the effective mass $M'' = -M$. (Status: PROVED here by hand; checked exactly by Notebook 20b, In [9].) Its tensor is the pulled-back one, $R_8TR_8$, which for the diagonal tensor of a condensate is $T$ itself: the SAME energy density $12$ and pressure $-24$. Its charge density is $(\gamma^{(x_8)}\Phi)^\dagger B(\gamma^{(x_8)}\Phi) = \Phi^\dagger\gamma^{(x_8)}B\gamma^{(x_8)}\Phi = \Phi^\dagger B\Phi = -3$, the SAME as the universe's, because $\gamma^{(x_8)}$ is real and symmetric and $\gamma^{(x_8)}B\gamma^{(x_8)\dagger} = +B$ (`python-pairing.json`, check `Q.T2_image_keeps_B`). The mirror is an isometry, so the Einstein tensor is the same on both patches, and the copy alone solves all 64 Einstein equations on the mirror patch. The universe on the patch and its copy on the mirror patch together fill the Z2-doubled geometry with twice the energy and twice the charge, not zero. Whether the two halves can be joined at the brane (a junction condition, a brane tension) is not derived anywhere in the record: OPEN; the Z2 construction is ASSUMED.

**The bookkeeping.** In units $H = \kappa = 1$:

| object | $m$ | $\lambda$ | $\rho$ | $p$ | $J^{x_4}$ | $S$ | alone a source? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| universe | $15$ | $-25/3$ | $12$ | $-24$ | $-3$ | $12/5$ | yes |
| T1 partner | $-15$ | $25/3$ | $-12$ | $24$ | $3$ | $12/5$ | no |
| T1 pair | both | both | $0$ | $0$ | $0$ | $24/5$ | no (C1) |
| T2 copy | $-15$ | $-25/3$ | $12$ | $-24$ | $-3$ | $-12/5$ | yes (mirror) |
| T2 pair | both | both | $24$ | $-48$ | $-6$ | $0$ | each half |

The objects are the universe $\Phi$, its T1 partner $\Gamma\Phi$ and its T2 copy $\gamma^{(x_8)}\Phi$. The last column says whether the object alone is a source of the author's metric in Einstein gravity: the universe with $a_4 = \pm Hx_4$ and $\Lambda = -36H^2$ on the patch; its T1 partner for no $a_4$ and no $\Lambda$; the T2 copy on the mirror patch. The universe and its T1 partner live on the patch, the T2 copy on the mirror patch. The row of the T1 pair adds the two members at the same point; the row of the T2 pair adds the two members each at its own point (so its $\rho$ is a total of two halves, not a density at one point).

**What the example shows, and what it does not.** It shows: (1) a universe of this theory can be a complete solution of the coupled equations with no partner at all; (2) its T1 partner exists as a solution of a DIFFERENT field equation (mass $-15$, coupling $25/3$), with the same frequency and the opposite energy and charge, and it cannot be the source of the author's metric in Einstein gravity; (3) the T1 pair has zero energy and charge and therefore cannot be that source either (C1); (4) the T2 copy is an ordinary solution with the same energy and charge on the mirror patch. It does NOT show that the partner or the copy is created, or must exist; it derives no process, rate or amplitude; it says nothing about the quantised field dirac16complex; and it does not address the stability of the condensate (OPEN).

### 20.13 Example: one universe and its two partners, computed

Notebook 20b builds the universe of Section 20.12 with exact arithmetic and the author's eight gamma matrices, checks its field equation exactly at every time, evaluates its complete energy-momentum tensor at nine points of the author's metric (three values of the hidden coordinate times three times $x_4$) and checks all 64 Einstein equations there; then it does the same for the T1 partner, the T1 pair and the T2 mirror copy. It prints 25 PASS lines, 14 of which reproduce a named check of a Revision report, and draws four figures. It needs numpy, sympy and matplotlib, no Rust, and runs in about 30 seconds (its recorded check run on the build computer took 18.7 seconds).

<!-- NOTEBOOK 20b -->

### 20.16 Line-by-line walk-through of Notebook 20b

The notebook has 14 code cells, In [1] to In [14]. As in Section 20.11, each group of lines is quoted and then explained; lines that repeat a pattern of Notebook 20a are quoted as well, with a short reminder.

**In [1], the set-up cell.** It is word for word the set-up cell of Notebook 20a, explained line by line in Section 20.11, with two differences: its comment lines at the top hold the run instructions of Notebook 20b (Section 20.14), and one line names the notebook:

```python
NOTEBOOK_ID = "20b"  # this notebook: chapter 20, example b
```

So the figures are saved as `20b_1_...` to `20b_4_...`, the captions in `20b.captions.json`, and the last line will read ALL 25 CHECKS PASSED (notebook 20b). Output: Set-up of notebook 20b complete.

**In [2], the records and the helper `reproduces`.**

```python
import contextlib  # redirect_stdout: send printed lines into a buffer
import io  # StringIO: a text buffer in memory

GAMMAS = "Revision/algebra/gammas.json"  # the author's gamma matrices
A4_RECORD = "Revision/field_equations_a4/a4-equations.json"  # the a4 equations
A4_PY = "Revision/field_equations_a4/reports/python-a4-report.json"
A4_WL = "Revision/field_equations_a4/reports/wolfram-a4-report.json"
PAIR_PY = "Revision/pairing/reports/python-pairing.json"
PAIR_WL = "Revision/pairing/reports/wolfram-pairing.json"
PROOFS = "Revision/docs/PAIR_CREATION_PROOFS.md"
```

The two modules `contextlib` and `io` and the names of the seven files of the repository that the notebook reads: the author's gammas, the record of the field equations for $a_4$ with its two reports, the two pairing reports and the Revision document of the pairing proofs.

```python
def read_json(relative):
    """Read a JSON file of the repository (a Revision record)."""
    return json.loads(repository_file(relative).read_text(encoding="utf-8"))


def record_verdict(report_file, name):
    """The verdict ("PASS") of the check called name in a report; None if absent."""
    for entry in read_json(report_file)["checks"]:
        if entry["name"] == name:
            return entry["verdict"]
    return None


def reproduces(condition, name, report_file, record_name):
    """A check that also requires the record check record_name to be PASS."""
    found = record_verdict(report_file, record_name) == "PASS"
    lines = io.StringIO()  # a text buffer
    with contextlib.redirect_stdout(lines):  # print() now writes into the buffer
        check(condition and found, name,
              record=f"{report_file}, check {record_name}")
    print(lines.getvalue(), end="")  # both lines with one print call
```

The three helpers of Notebook 20a, In [2], line for line: `read_json` reads a JSON record; `record_verdict` returns the verdict of a named check of a report (or `None`); `reproduces` passes only when the notebook's own condition holds AND the named record check has the verdict PASS, and then prints the PASS line together with the line that names the record (Section 20.11 explains every line).

```python
NO_NECESSITY = ("a single universe with mass $+m$ is an equally valid solution "
                "without its partner")
proofs = repository_file(PROOFS).read_text(encoding="utf-8")
say(f"{PROOFS} says: \"... a single universe with mass +m is an equally valid "
    "solution without its partner.\"")
check(NO_NECESSITY in proofs, "the record states that no partner is required")
```

`NO_NECESSITY` is a sentence of the record's answer to the request (two strings in parentheses are joined into one). The document is read as one text; `say` prints the sentence; the check confirms that it occurs in the document word for word. Output: the quoted sentence and PASS the record states that no partner is required.

**In [3], the gammas, $C$, $\Gamma$, $B$ and the spin connection on both patches.**

```python
import itertools  # loops over all combinations of indices

import numpy as np  # floating-point arrays
import sympy as sp  # exact algebra

NAMES = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]  # positions 0..7
ETA = [1, 1, 1, -1, -1, -1, -1, 1]  # the frame metric eta, x1..x8
I16, Z16 = sp.eye(16), sp.zeros(16, 16)
gamma = [sp.Matrix([[sp.Rational(x) for x in row] for row in matrix])
         for matrix in read_json(GAMMAS)["gamma"]]  # gamma[a] = gamma^(x_(a+1))
C = gamma[7] * gamma[0] * gamma[1] * gamma[2]  # C = g^(x8) g^(x1) g^(x2) g^(x3)
chirality = gamma[7]  # Gamma = g^(x8) g^(x1) ... g^(x7), factor by factor
for a in range(7):
    chirality = chirality * gamma[a]
B = -sp.I * C * gamma[3]  # the Krein matrix B = -i C gamma^(x4)
S_exact = [[(gamma[a] * gamma[b] - gamma[b] * gamma[a]) / 4 for b in range(8)]
           for a in range(8)]
```

The same objects as in Notebook 20a, In [3], built the same way: the labels, the diagonal of $\eta$, the exact unit matrix $I_{16}$ and the exact $16 \times 16$ zero matrix `Z16` (`sp.zeros(16, 16)`; two names are assigned at once), the eight exact gammas read from `gammas.json` (here the reading and the conversion are written in one comprehension), $C$, the chirality $\Gamma$ (called `chirality`) multiplied factor by factor in the record's order, the Krein matrix $B = -iC\gamma^{(x_4)}$ (`sp.I` is the exact imaginary unit; position 3 is $x_4$), and the 64 generators $S^{ab}$.

```python
H = sp.symbols("H", positive=True)
z = sp.symbols("z", real=True)
x4 = sp.symbols("x4", real=True)
a4 = sp.Function("a4")(x4)
a4_value, slope = sp.symbols("a4_value slope", real=True)


def d(expr, mu):
    """The partial derivative along the coordinate at position mu."""
    if mu == 3:
        return sp.diff(expr, x4)
    if mu == 7:
        return 6 * H * sp.diff(expr, z)  # d/dx8 = 6 H d/dz
    return sp.Integer(0)
```

The symbols $H > 0$, $z$, $x_4$, the unknown function $a_4(x_4)$, the two symbols that replace $a_4$ and $a_4'$ at a point, and the partial derivative `d(expr, mu)` with $\partial/\partial x_8 = 6H\,\partial/\partial z$ (Notebook 20a, In [4]).

```python
def spin_connection(s8):
    """The lengths E_a and omega[mu][a][b] = omega_mu ab (s8 = +1 patch, -1 mirror)."""
    s = sp.sin(z) ** sp.Rational(1, 6)
    E = [sp.exp(a4) * s] * 3 + [sp.Integer(1)] + [sp.exp(-a4) * s] * 3
    E = E + [s8 * sp.cot(z)]
    g = [ETA[a] * E[a] ** 2 for a in range(8)]
    christoffel = {}
    for a, b, c in itertools.product(range(8), repeat=3):
        value = 0
        if a == c:
            value += d(g[a], b)
        if a == b:
            value += d(g[a], c)
        if b == c:
            value -= d(g[b], a)
        christoffel[a, b, c] = value / (2 * g[a])
    omega = [[[sp.Integer(0)] * 8 for _ in range(8)] for _ in range(8)]
    for mu, a, b in itertools.product(range(8), repeat=3):
        if a != b:
            value = ETA[a] * E[a] * christoffel[a, mu, b] / E[b]
            value = value.subs(sp.Derivative(a4, x4), slope).subs(a4, a4_value)
            omega[mu][a][b] = sp.simplify(value)
    return [length.subs(a4, a4_value) for length in E], omega
```

The canonical spin connection on the patch (`s8 = 1`) or on the mirror patch (`s8 = -1`), exactly as in Notebook 20a, In [4]: the lengths $E_a$ (three inflating $e^{a_4}\sin^{1/6}z$, the time 1, three DEFLATING $e^{-a_4}\sin^{1/6}z$, and $s_8\cot z$), the diagonal metric $g_{aa} = \eta_{aa}E_a^2$, the Christoffel symbols term by term, and $\omega_{\mu ab} = \eta_{aa}(E_a/E_b)\Gamma^a{}_{\mu b}$ for $a \neq b$ with $a_4$ and $a_4'$ replaced by the point symbols. The only difference from 20a is that the list of lengths is built inside the function in two lines (the first seven lengths, then `E + [s8 * sp.cot(z)]` appends the eighth).

```python
CONNECTION = {s8: spin_connection(s8) for s8 in (1, -1)}
gravity_term = {}  # s8 -> sum over mu of gamma^mu Omega_mu
for s8, (E, omega) in CONNECTION.items():
    Omega = [sum((omega[mu][a][b] * S_exact[a][b] / 2 for a in range(8)
                  for b in range(8) if omega[mu][a][b] != 0), Z16)
             for mu in range(8)]
    gravity_term[s8] = sum((gamma[mu] / E[mu] * Omega[mu] for mu in range(8)),
                           Z16).applyfunc(sp.simplify)
reproduces(gravity_term[1] == 3 * H * gamma[7],
           "patch: gamma^mu Omega_mu = 3 H gamma^(x8)", A4_PY, "authorT16_gravity_term")
check(gravity_term[-1] == -3 * H * gamma[7],
      "mirror patch: gamma^mu Omega_mu = -3 H gamma^(x8)")
```

`{s8: spin_connection(s8) for s8 in (1, -1)}` computes the connection on both patches and stores the pair (lengths, components) under the key $+1$ or $-1$; `.items()` walks through the keys and values of a dictionary. For each patch, `Omega` holds the eight matrices $\Omega_\mu = \frac12\sum_{a,b}\omega_{\mu ab}S^{ab}$, and `gravity_term[s8]` is $\sum_\mu\gamma^\mu\Omega_\mu$ with $\gamma^\mu = \gamma^{(\mu)}/E_\mu$, simplified entry by entry. The checks: $3H\gamma^{(x_8)}$ on the patch (the record's term, `python-a4-report.json`, check `authorT16_gravity_term`) and $-3H\gamma^{(x_8)}$ on the mirror patch (a computation of this book). Output: two PASS lines.

**In [4], choosing the universe: the two Einstein conditions.**

```python
record = read_json(A4_RECORD)
ad1, ad2 = sp.symbols("ad1 ad2", real=True)  # a4' and a4''
A, Lam, kappa = sp.symbols("A Lambda kappa", real=True)
m, lam, S_sym = sp.symbols("m lambda S", real=True)
```

The record of the field equations for $a_4$ is read. The symbols: $a_4'$ and $a_4''$ under the record's names `ad1` and `ad2` (here declared real), the slope $A$, $\Lambda$ (`Lam`), $\kappa$, the mass $m$, the coupling $\lambda$ (`lam`; the word `lambda` is reserved in Python) and the density $S$ (`S_sym`, a symbol, to keep it apart from numbers).

```python
def einstein(key):
    """The component key of the Einstein tensor E_(1) from the record."""
    text = record["lovelockTensors"]["E1"][key]["input"].replace("^", "**")
    return sp.sympify(text, locals={"ad1": ad1, "ad2": ad2, "H": H})
```

`einstein(key)` reads one component of the Einstein tensor $E_{(1)} = G$ from the record's text in Wolfram's input form and turns it into a sympy expression (`^` becomes `**`; `locals` binds the names `ad1`, `ad2` and `H` to the notebook's symbols), as `lovelock` did in Notebook 20a, In [12].

```python
G = {key: einstein(key) for key in ("x1x1", "x4x4", "x5x5", "x8x8")}
LINEAR = {ad1: A * H, ad2: 0}  # the linear member a4 = A H x4
rho_c, p_c = m * S_sym + lam * S_sym ** 2 / 2, lam * S_sym ** 2 / 2  # condensate
time_eq = G["x4x4"].subs(LINEAR) + Lam + kappa * rho_c  # = 0
hidden_eq = G["x8x8"].subs(LINEAR) + Lam - kappa * p_c  # = 0
first = sp.expand(time_eq - hidden_eq)  # kappa (m + lambda S) S + 6 (A^2 + 1) H^2
second = sp.expand(time_eq + hidden_eq)  # kappa m S + 36 H^2 + 2 Lambda
```

`G` holds the four independent diagonal components. `LINEAR` is the substitution of the linear member, $a_4' = AH$ and $a_4'' = 0$. `rho_c` and `p_c` are the condensate's $\rho = mS + \frac{\lambda}{2}S^2$ and $p = \frac{\lambda}{2}S^2$ (step 2 of Section 20.12). `time_eq` is the time equation written as "left side minus right side", $G^{x_4}{}_{x_4} + \Lambda + \kappa\rho = 0$, and `hidden_eq` the hidden equation, $G^{x_8}{}_{x_8} + \Lambda - \kappa p = 0$. `first` is their difference and `second` their sum, multiplied out by `sp.expand`: exactly the two combinations of step 3.

```python
reproduces(sp.expand(first - (kappa * (m + lam * S_sym) * S_sym
                              + 6 * (A ** 2 + 1) * H ** 2)) == 0
           and sp.expand(second - (kappa * m * S_sym + 36 * H ** 2 + 2 * Lam)) == 0,
           "Einstein: kappa M S = -6 (A^2 + 1) H^2, kappa m S = -(36 H^2 + 2 Lambda)",
           A4_PY, "condensate_einstein_quadratic_U")
```

The check compares the two combinations with $\kappa(m + \lambda S)S + 6(A^2 + 1)H^2$ and $\kappa mS + 36H^2 + 2\Lambda$; each difference must expand to zero. It reproduces the record's two conditions (`python-a4-report.json`, check `condensate_einstein_quadratic_U`).

```python
CHOICE = {H: 1, kappa: 1, A: 1, Lam: -36}  # the geometry of this notebook
M_VALUE = -5  # the effective mass M = m + lambda S
S_value = sp.solve(first.subs(CHOICE).subs(lam, (M_VALUE - m) / S_sym), S_sym)[0]
m_value = sp.solve(second.subs(CHOICE).subs(S_sym, S_value), m)[0]
lam_value = (M_VALUE - m_value) / S_value
rho_value = rho_c.subs({m: m_value, lam: lam_value, S_sym: S_value})
p_value = p_c.subs({lam: lam_value, S_sym: S_value})
```

`CHOICE` fixes the geometry of the notebook: $H = \kappa = 1$, $A = 1$, $\Lambda = -36$; `M_VALUE` is the effective mass $M = -5$. Then the four lines of step 4, done by sympy: in `first`, $\lambda$ is replaced by $(M - m)/S$ (this is $M = m + \lambda S$ solved for $\lambda$), and `sp.solve(..., S_sym)` solves for $S$ (`[0]` takes the one solution); in `second`, $S$ is replaced by its value and the equation is solved for $m$; then $\lambda$, $\rho$ and $p$ follow by substitution.

```python
for label, value in (("S", S_value), ("m", m_value), ("lambda", lam_value),
                     ("rho", rho_value), ("p", p_value)):
    report(label, value)
check((S_value, m_value, lam_value, rho_value, p_value)
      == (sp.Rational(12, 5), 15, sp.Rational(-25, 3), 12, -24),
      "the universe: S = 12/5, m = 15, lambda = -25/3, rho = 12, p = -24")
```

The loop prints the five numbers as RESULT lines, and the check compares them with the exact values of step 4. Output: RESULT S = 12/5, m = 15, lambda = -25/3, rho = 12, p = -24, and the PASS line.

**In [5], building the universe.**

```python
w = sp.sqrt(M_VALUE ** 2 - 9)  # the frequency, H = 1
A_matrix = -gamma[3] * (M_VALUE * I16 - 3 * gamma[7])  # Phi' = A Phi
spaces = []
for sign in (-1, 1):  # the value of g^(x1)g^(x5) = g^(x2)g^(x6) = g^(x3)g^(x7)
    stack = sp.Matrix.vstack(A_matrix + sp.I * w * I16,
                             gamma[0] * gamma[4] - sign * I16,
                             gamma[1] * gamma[5] - sign * I16,
                             gamma[2] * gamma[6] - sign * I16)
    spaces.append(stack.nullspace())  # every solution of stack * v = 0
v1, v2 = spaces[0][0], spaces[1][0]
```

`w` is the frequency $\sqrt{M^2 - 9} = 4$ (exactly; `sp.sqrt` of 16). `A_matrix` is $\mathcal{A} = -\gamma^{(x_4)}(M - 3\gamma^{(x_8)})$ with $H = 1$. For each of the two values $\mp1$ (`sign`), `sp.Matrix.vstack` stacks four $16 \times 16$ matrices on top of each other into one $64 \times 16$ matrix: $\mathcal{A} + iwI_{16}$ and the three matrices $\gamma^{(x_1)}\gamma^{(x_5)} - \text{sign}\,I_{16}$, $\gamma^{(x_2)}\gamma^{(x_6)} - \text{sign}\,I_{16}$, $\gamma^{(x_3)}\gamma^{(x_7)} - \text{sign}\,I_{16}$. A column $v$ with `stack * v = 0` satisfies all four conditions at once: $\mathcal{A}v = -iwv$ and each of the three products has the value `sign` on $v$. `stack.nullspace()` returns a list of columns that span all such $v$ (the **null space**). `v1` is the first column for the value $-1$, `v2` the first for $+1$.

```python
c = sp.conjugate(sp.expand((v1.H * C * v2)[0]))  # c = conj(v1^dagger C v2)
t = sp.symbols("t", real=True)
family = (v1 + t * c * v2).applyfunc(sp.expand)  # Phi_0(t)
```

`v1.H` is the **conjugate transpose** $v_1^\dagger$ (a row), so `(v1.H * C * v2)[0]` is the number $v_1^\dagger Cv_2$, and `sp.conjugate` gives $c = \overline{v_1^\dagger Cv_2}$. `t` is a real symbol and `family` the column $\Phi_0(t) = v_1 + t\,c\,v_2$, multiplied out entry by entry.

```python
def bilinear(phi, matrix):
    """phibar matrix phi = phi^dagger C matrix phi (exact)."""
    return sp.expand((phi.H * C * matrix * phi)[0])


t_value = sp.solve(bilinear(family, I16) - S_value, t)[0]
phi0 = family.subs(t, t_value).applyfunc(sp.expand)  # the universe at x4 = 0
report("t", t_value)
```

`bilinear(phi, matrix)` is $\bar\phi\,M\phi = \phi^\dagger CM\phi$, exact. The equation $S(t) = 12/5$ is solved for $t$, the universe at $x_4 = 0$, `phi0`, is the family at that $t$, and the value is printed. Output: RESULT t = 15/512.

```python
NEEDED = sorted({tuple(sorted((i, 3, 7))) for i in (0, 1, 2, 4, 5, 6)}
                | {tuple(sorted((i, j, 3))) for i in (0, 1, 2) for j in (4, 5, 6)})
zero_15 = all(bilinear(family, gamma[a] * gamma[b] * gamma[e]) == 0
              for a, b, e in NEEDED)  # for every real t, so also for t_value
reproduces([len(space) for space in spaces] == [1, 1] and zero_15
           and bilinear(phi0, I16) == S_value,
           "the universe: 15 three-gamma bilinears 0 and S = 12/5",
           A4_WL, "condensate_diagonal_witness_exact")
```

`NEEDED` lists the 15 index triples of the three-gamma bilinears that must vanish: the six triples $\{i, x_4, x_8\}$ with $i$ one of $x_1, x_2, x_3, x_5, x_6, x_7$ (positions 0, 1, 2, 4, 5, 6 together with 3 and 7), and the nine triples $\{i, j, x_4\}$ with $i$ in 3-space and $j$ an extra time. Each triple is sorted, the braces `{...}` make a **set** (a collection without repetitions), `|` joins two sets, and `sorted` puts the triples in a fixed order. `zero_15` is true when all 15 bilinears of the family vanish for the SYMBOL $t$, so for every real $t$, in particular for $15/512$. The check requires the two null spaces to be one-dimensional, the 15 zeros, and $S = 12/5$ for `phi0`; it reproduces the record's witness (`wolfram-a4-report.json`, check `condensate_diagonal_witness_exact`).

```python
reproduces((C * A_matrix + A_matrix.T * C).applyfunc(sp.expand) == Z16,
           "C A + A^T C = 0: S stays 12/5 at every time", A4_PY,
           "authorT16_condensate_S_constant")
Phi = phi0 * sp.exp(-sp.I * w * x4)  # the universe Phi(x4)
```

The check $C\mathcal{A} + \mathcal{A}^TC = 0$ (`.T` is the transpose) shows that $S$ stays $12/5$ at every time (step 1). `Phi` is the universe $\Phi(x_4) = \Phi_0e^{-iwx_4}$, a column of 16 exact functions of $x_4$.

```python
def field_residual(field, term, mass, coupling, density):
    """gamma^(x4) field' + term field - (mass + coupling density) field."""
    return (gamma[3] * sp.diff(field, x4) + term * field
            - (mass + coupling * density) * field).applyfunc(sp.simplify)
```

`field_residual` returns $\gamma^{(x_4)}\Phi' + (\text{term})\Phi - (\text{mass} + \text{coupling}\cdot\text{density})\Phi$ for a field that depends on $x_4$ only: the left side minus the right side of the condensate equation, with the spin-connection term `term` given as an argument (so that the same function serves on the mirror patch). `sp.diff(field, x4)` differentiates each entry, and `.applyfunc(sp.simplify)` simplifies each entry of the result.

```python
universe_ok = field_residual(Phi, gravity_term[1].subs(H, 1), m_value, lam_value,
                             S_value) == sp.zeros(16, 1)
reproduces(universe_ok, "the universe solves its field equation (16 components)",
           A4_WL, "condensate_equation_x8_consistent")
charge_value = sp.simplify((phi0.H * B * phi0)[0])  # J^x4, constant in time
report("charge density J^x4 of the universe", charge_value)
```

The universe's residual with the patch term $3\gamma^{(x_8)}$ (`gravity_term[1].subs(H, 1)`), $m = 15$, $\lambda = -25/3$ and $S = 12/5$ must be the zero column, at every time $x_4$ (the time is a symbol). The last lines compute the charge density $\Phi_0^\dagger B\Phi_0$ exactly; the factor $e^{-iwx_4}$ drops out of it. Output: RESULT t = 15/512, three PASS lines with their records, and RESULT charge density J^x4 of the universe = -3.

**In [6], the universe alone solves the Einstein equations.**

```python
point_symbols = (z, a4_value, slope, H)
S_num = [[np.array(S_exact[a][b].tolist(), dtype=float) for b in range(8)]
         for a in range(8)]
gamma_num = [np.array(g.tolist(), dtype=float) for g in gamma]
C_num = np.array(C.tolist(), dtype=float)
Gamma_num = np.array(chirality.tolist(), dtype=float)
B_num = np.array(B.tolist(), dtype=complex)
NUMERIC = {}
for s8, (E, omega) in CONNECTION.items():
    pieces = [(mu, a, b, sp.lambdify(point_symbols, omega[mu][a][b], "numpy"))
              for mu in range(8) for a in range(8) for b in range(8)
              if omega[mu][a][b] != 0]
    NUMERIC[s8] = (sp.lambdify(point_symbols, E, "numpy"), pieces)
```

The floating-point copies of the generators, the gammas, $C$, $\Gamma$ and $B$ (`dtype=complex` because $B$ is imaginary), and, for both patches, the numpy functions of the lengths and of the nonzero connection components (`sp.lambdify`, as in Notebook 20a, In [6]).

```python
def geometry_at(s8, z_value, a4_number, slope_number):
    """Metric, Omega_mu and curved gammas at one point (H = 1)."""
    lengths_f, pieces = NUMERIC[s8]
    values = (z_value, a4_number, slope_number, 1.0)
    E = np.array([float(x) for x in lengths_f(*values)])
    Om = [np.zeros((16, 16)) for _ in range(8)]
    for mu, a, b, f in pieces:
        Om[mu] += float(f(*values)) * S_num[a][b] / 2
    return {"g": np.array(ETA) * E ** 2, "Omega": Om,
            "up": [gamma_num[mu] / E[mu] for mu in range(8)],
            "down": [ETA[mu] * E[mu] * gamma_num[mu] for mu in range(8)]}
```

`geometry_at` is the function of Notebook 20a, In [6], with $H = 1$ fixed: it returns the metric, the eight $\Omega_\mu$ and the curved gammas with upper and lower index at one point.

```python
def mixed_tensor(at, psi, dpsi, mass, coupling):
    """T^mu_nu (convention sigma_T = +1) and K^mu_mu of a first jet."""
    bar = psi.conj() @ C_num
    dbar = [row.conj() @ C_num for row in dpsi]
    D = [dpsi[mu] + at["Omega"][mu] @ psi for mu in range(8)]
    Dbar = [dbar[mu] - bar @ at["Omega"][mu] for mu in range(8)]
    S = (bar @ psi).real
    kinetic = [0.5 * (bar @ at["up"][mu] @ D[mu] - Dbar[mu] @ at["up"][mu] @ psi)
               for mu in range(8)]  # K^mu_mu, no sum
    L = sum(kinetic).real - mass * S - coupling * S ** 2 / 2
```

`mixed_tensor` evaluates the energy-momentum tensor of a first jet, as `bilinears` did in Notebook 20a: $\bar\Phi = \Phi^\dagger C$, $\partial_\mu\bar\Phi$, the covariant derivatives, the real density $S$, and the eight diagonal kinetic terms $K^\mu{}_\mu = \frac12(\bar\Phi\gamma^\mu D_\mu\Phi - (D_\mu\bar\Phi)\gamma^\mu\Phi)$, one for each $\mu$ with no sum, kept in the list `kinetic`. Their sum is the kinetic term $K$, and `L` is $\mathcal{L}/\sqrt{|g|} = K - mS - \frac{\lambda}{2}S^2$ (`.real` drops an imaginary part of rounding size).

```python
    T = np.zeros((8, 8))
    for mu, nu in itertools.product(range(8), repeat=2):
        low = 0.25 * (bar @ at["down"][mu] @ D[nu] + bar @ at["down"][nu] @ D[mu]
                      - Dbar[mu] @ at["down"][nu] @ psi
                      - Dbar[nu] @ at["down"][mu] @ psi).real
        if mu == nu:
            low -= at["g"][mu] * L  # the pairing records' T_mu nu
        T[mu, nu] = -low / at["g"][mu]  # T^mu_nu = -g^(mu mu) T_mu nu
    return T, np.array([k.real for k in kinetic])
```

For each of the 64 pairs $(\mu, \nu)$, `low` is the tensor $T_{\mu\nu}$ of the pairing records (four kinetic terms, and $-g_{\mu\mu}\mathcal{L}/\sqrt{|g|}$ on the diagonal). The notebook needs the mixed tensor $T^\mu{}_\nu$ in the convention of the record of the field equations, which is minus the pairing records' tensor (Section 20.5): raising the first index with the diagonal metric, $T^\mu{}_\nu = g^{\mu\mu}T_{\mu\nu}$ with $g^{\mu\mu} = 1/g_{\mu\mu}$, and changing the sign gives `T[mu, nu] = -low / at["g"][mu]`. The function returns $T^\mu{}_\nu$ and the eight diagonal kinetic terms.

```python
G_numeric = np.diag([float(G[k].subs({ad1: 1, ad2: 0, H: 1})) for k in
                     ("x1x1", "x1x1", "x1x1", "x4x4", "x5x5", "x5x5", "x5x5",
                      "x8x8")])  # G^mu_nu at a4' = H, H = 1
LAMBDA = -36.0
phi0_num = np.array([complex(entry) for entry in phi0])
W = float(w)
POINTS = [(zv, xv) for zv in (0.3, 0.8, 1.3) for xv in (0.0, 0.7, 2.0)]
```

`G_numeric` is the diagonal matrix of $G^\mu{}_\nu$ at $a_4' = H = 1$, $a_4'' = 0$, in the order $x_1, \dots, x_8$ (components 1 to 3 equal $G^{x_1}{}_{x_1}$, 5 to 7 equal $G^{x_5}{}_{x_5}$): $\mathrm{diag}(12, 12, 12, 24, 12, 12, 12, 12)$. `LAMBDA` is $\Lambda = -36$, `phi0_num` the universe at $x_4 = 0$ as 16 complex floating-point numbers, `W` the frequency 4.0, and `POINTS` the nine points: $z = 0.3, 0.8, 1.3$ combined with $x_4 = 0, 0.7, 2$.

```python
def universe_jet(x_value, matrix=None):
    """Value and derivatives of matrix Phi at the time x_value."""
    value = phi0_num * np.exp(-1j * W * x_value)
    if matrix is not None:
        value = matrix @ value
    jet = [np.zeros(16, dtype=complex) for _ in range(8)]
    jet[3] = -1j * W * value  # d Phi / d x4 = -i w Phi
    return value, jet
```

`universe_jet(x, matrix)` returns the first jet of the universe (or of `matrix` times the universe) at the time $x$: the value $\Phi_0e^{-iwx}$ and eight derivative columns, all zero except the one along $x_4$, $-iw\Phi$. `matrix=None` makes the argument optional; `is not None` tests whether it was given.

```python
worst_residual, worst_kinetic = 0.0, 0.0
for z_value, x_value in POINTS:
    at = geometry_at(1, z_value, x_value, 1.0)  # a4 = x4, a4' = 1
    T, kinetic = mixed_tensor(at, *universe_jet(x_value), float(m_value),
                              float(lam_value))
    residual = G_numeric + LAMBDA * np.eye(8) - T  # kappa = 1
    worst_residual = max(worst_residual, np.abs(residual).max())
    wanted = np.zeros(8)
    wanted[3] = M_VALUE * float(S_value)  # K^x4_x4 = M S, all others 0
    worst_kinetic = max(worst_kinetic, np.abs(kinetic - wanted).max())
```

At each of the nine points: the geometry on the patch with $a_4 = x_4$ (the history $a_4 = Hx_4$ with $H = 1$) and $a_4' = 1$; the tensor and the kinetic terms of the universe (`*universe_jet(x_value)` unpacks the pair (value, jet) into two arguments); the Einstein residual $G + \Lambda - \kappa T$ with $\kappa = 1$; and the largest deviation of the kinetic terms from the record's values $K^{x_4}{}_{x_4} = MS = -12$ and zero otherwise. `worst_residual` and `worst_kinetic` keep the largest values over all points.

```python
T_universe = T  # the tensor at the last point (it is the same at every point)
report("rho of the universe", f"{-T_universe[3, 3]:.10f}")
report("p of the universe", f"{T_universe[0, 0]:.10f}")
reproduces(worst_kinetic < 1e-10, "K^x4_x4 = M S and K^mu_mu = 0 otherwise (9 points)",
           A4_PY, "authorT16_condensate_kinetic_diagonal")
check(worst_residual < 1e-10,
      "the universe ALONE solves all 64 Einstein equations (9 points)")
```

The tensor at the last point is kept as `T_universe` (it is the same at every point: the condensate has constant $\rho$ and $p$). The RESULT lines print $\rho = -T^{x_4}{}_{x_4}$ and $p = T^{x_1}{}_{x_1}$ with ten decimals (`:.10f`). Output: RESULT rho of the universe = 12.0000000000, RESULT p of the universe = -24.0000000000, PASS for the kinetic terms (reproducing `python-a4-report.json`, check `authorT16_condensate_kinetic_diagonal`), and PASS the universe ALONE solves all 64 Einstein equations (9 points): every one of the $9 \times 64$ residuals is below $10^{-10}$.

**In [7], the T1 partner $\Gamma\Phi$.**

```python
partner = chirality * Phi  # Gamma Phi
partner_ok = field_residual(partner, gravity_term[1].subs(H, 1), -m_value,
                            -lam_value, S_value) == sp.zeros(16, 1)
reproduces(partner_ok and bilinear(chirality * phi0, I16) == S_value,
           "Gamma Phi solves the (-m, -lambda) field equation; S' = S",
           PAIR_PY, "T1.metric.commuting.euler_lagrange_map")
```

`partner` is $\Gamma\Phi$, exact. Its residual with the patch term, the parameters $(-m, -\lambda)$ and the density $S$ must vanish at every time, and its density must equal $S$: step 6 of Section 20.12, reproducing `python-pairing.json`, check `T1.metric.commuting.euler_lagrange_map`.

```python
A_partner = -gamma[3] * (-M_VALUE * I16 - 3 * gamma[7])  # M' = -M
same_spectrum = (chirality * A_matrix * chirality == A_partner
                 and (A_partner * A_partner + w ** 2 * I16) == Z16)
reproduces(same_spectrum, "A' = Gamma A Gamma: the partner has the same frequency",
           PAIR_WL, "Q_one_particle_maps")
```

`A_partner` is $\mathcal{A}' = -\gamma^{(x_4)}(-M - 3\gamma^{(x_8)})$. The check requires $\Gamma\mathcal{A}\Gamma = \mathcal{A}'$, the similarity derived by hand in step 6, and $\mathcal{A}'^2 + w^2I_{16} = 0$, so that every eigenvalue of the partner's matrix is $\pm iw$: the same frequency.

```python
partner_charge = sp.simplify(((chirality * phi0).H * B * (chirality * phi0))[0])
reproduces(partner_charge == -charge_value, "the partner's charge density is -J^x4",
           PAIR_PY, "T1.metric.commuting.current")
```

The partner's charge density $(\Gamma\Phi_0)^\dagger B(\Gamma\Phi_0)$, exact, must be $-(-3) = +3$ (`python-pairing.json`, check `T1.metric.commuting.current`).

```python
worst_sum, worst_partner = 0.0, 0.0
for z_value, x_value in POINTS:
    at = geometry_at(1, z_value, x_value, 1.0)
    T_one, _ = mixed_tensor(at, *universe_jet(x_value), float(m_value),
                            float(lam_value))
    T_two, _ = mixed_tensor(at, *universe_jet(x_value, Gamma_num),
                            -float(m_value), -float(lam_value))
    worst_sum = max(worst_sum, np.abs(T_one + T_two).max())
    residual = G_numeric + LAMBDA * np.eye(8) - T_two
    worst_partner = max(worst_partner, np.abs(residual - 2 * T_one).max())
T_partner = T_two
reproduces(worst_sum < 1e-10, "T' = -T at all 9 points (64 components each)",
           PAIR_PY, "T1.metric.commuting.emt")
check(worst_partner < 1e-10 and np.abs(2 * T_one).max() > 1.0,
      "partner alone: the Einstein residual is 2 kappa T, not zero")
```

At the nine points: the tensor of the universe (`T_one`) and of the partner (`T_two`, the jet of $\Gamma\Phi$ with $(-m, -\lambda)$; `_` receives the kinetic terms, which are not needed). `worst_sum` is the largest component of $T + T'$, and `worst_partner` the largest deviation of the partner's Einstein residual from $2T$: with the partner as the only source the residual is $G + \Lambda - T' = (G + \Lambda - T) + 2T = 2T$, because the universe makes $G + \Lambda - T$ vanish and $T' = -T$. The checks: $T' = -T$ to $10^{-10}$ at all points (`python-pairing.json`, check `T1.metric.commuting.emt`), and the partner's residual is $2T$, whose largest entry is larger than 1, so NOT zero.

```python
null_universe = -T_universe[3, 3] + T_universe[7, 7]  # kappa (rho + p8)
null_partner = -T_partner[3, 3] + T_partner[7, 7]
report("kappa (rho + p8) of the universe", f"{null_universe:.10f}")
report("kappa (rho + p8) of the partner", f"{null_partner:.10f}")
```

The null combination $\kappa(\rho + p_8) = -T^{x_4}{}_{x_4} + T^{x_8}{}_{x_8}$ of the universe and of the partner, printed with ten decimals. Output: $-12.0000000000$ and $12.0000000000$.

```python
rate = sp.symbols("rate", real=True)  # a real value of a4'/H
required = sp.expand(-(einstein("x4x4") - einstein("x8x8")).subs(
    {ad1: rate, ad2: 0, H: 1}))  # the requirement -6 (a4'^2 + 1)
universe_null = rho_value + p_value  # exact: 12 - 24 = -12
partner_null = -(rho_value + p_value)  # exact: T' = -T gives +12
check(abs(null_universe - float(universe_null)) < 1e-10
      and abs(null_partner - float(partner_null)) < 1e-10,
      "kappa (rho + p8): universe -12, partner +12 (numbers = exact values)")
reproduces(required == -6 * rate ** 2 - 6
           and sorted(sp.solve(required - universe_null, rate)) == [-1, 1]
           and sp.solve(required - partner_null, rate) == [],
           "the universe fits a4' = +-H; the partner fits no real rate",
           A4_PY, "einstein_null_energy_x8")
```

`rate` is a real symbol for $a_4'/H$, and `required` is the requirement $-(G^{x_4}{}_{x_4} - G^{x_8}{}_{x_8}) = -6(a_4'^2 + 1)$ with $H = 1$, computed from the record's components. `universe_null` and `partner_null` are the exact values $-12$ and $+12$. The first check compares the floating-point values with the exact ones. The second requires the requirement to be $-6\,\text{rate}^2 - 6$, the universe's value to be met exactly at the two real rates $-1$ and $+1$, and the partner's value at no real rate (`sp.solve` returns the empty list `[]`): step 7 of Section 20.12, reproducing `python-a4-report.json`, check `einstein_null_energy_x8`. Output of the cell: six PASS lines (five of them with their records) and the two RESULT lines.

**In [8], the T1 pair as the only source.**

```python
worst_pair = 0.0
for z_value, x_value in POINTS:
    at = geometry_at(1, z_value, x_value, 1.0)
    T_one, _ = mixed_tensor(at, *universe_jet(x_value), float(m_value),
                            float(lam_value))
    T_two, _ = mixed_tensor(at, *universe_jet(x_value, Gamma_num),
                            -float(m_value), -float(lam_value))
    residual = G_numeric + LAMBDA * np.eye(8) - (T_one + T_two)
    expected = np.diag([-24.0, -24, -24, -12, -24, -24, -24, -24])
    worst_pair = max(worst_pair, np.abs(residual - expected).max())
check(worst_pair < 1e-10,
      "T1 pair alone: residual = G + Lambda = diag(-24, ..., -12, ...), not zero")
```

At the nine points the residual with the T1 pair as the only source, $G + \Lambda - (T + T')$, must equal the matrix $\mathrm{diag}(-24, -24, -24, -12, -24, -24, -24, -24)$ of step 8 (`np.diag` makes a diagonal matrix from a list). Output: PASS T1 pair alone: residual = G + Lambda = diag(-24, ..., -12, ...), not zero. This is corollary C1 on the example.

**In [9], the T2 mirror copy across the brane.**

```python
copy = gamma[7] * Phi  # gamma^(x8) Phi on the mirror patch
copy_ok = field_residual(copy, gravity_term[-1].subs(H, 1), -m_value, lam_value,
                         -S_value) == sp.zeros(16, 1)
reproduces(copy_ok and bilinear(gamma[7] * phi0, I16) == -S_value,
           "the mirror copy solves the (-m, lambda) equation there; S' = -S",
           PAIR_PY, "T2.metric.commuting.euler_lagrange_map")
copy_charge = sp.simplify(((gamma[7] * phi0).H * B * (gamma[7] * phi0))[0])
reproduces(copy_charge == charge_value, "the copy's charge density is +J^x4",
           PAIR_PY, "Q.T2_image_keeps_B")
```

`copy` is $\gamma^{(x_8)}\Phi$ (position 7 is $x_8$). Its residual is computed with the MIRROR-patch term $-3\gamma^{(x_8)}$ (`gravity_term[-1]`), the parameters $(-m, \lambda)$ and the density $-S$; it must vanish at every time, and its density must be $-S$: step 9 of Section 20.12, reproducing `python-pairing.json`, check `T2.metric.commuting.euler_lagrange_map`. The copy's charge density, exact, must equal the universe's $-3$ (`python-pairing.json`, check `Q.T2_image_keeps_B`).

```python
worst_copy, worst_pull = 0.0, 0.0
R8 = np.diag([1.0, 1, 1, 1, 1, 1, 1, -1])
for z_value, x_value in POINTS:
    there = geometry_at(-1, np.pi - z_value, x_value, 1.0)  # the mirror point
    T_copy, _ = mixed_tensor(there, *universe_jet(x_value, gamma_num[7]),
                             -float(m_value), float(lam_value))
    T_one, _ = mixed_tensor(geometry_at(1, z_value, x_value, 1.0),
                            *universe_jet(x_value), float(m_value), float(lam_value))
    worst_pull = max(worst_pull, np.abs(T_copy - R8 @ T_one @ R8).max())
    residual = G_numeric + LAMBDA * np.eye(8) - T_copy
    worst_copy = max(worst_copy, np.abs(residual).max())
T_mirror = T_copy
```

`R8` is the diagonal matrix $R_8 = \mathrm{diag}(1, 1, 1, 1, 1, 1, 1, -1)$. At each of the nine points, `there` is the geometry at the mirror point $\pi - z$ of the mirror patch (`s8 = -1`), and `T_copy` the tensor of the copy there, with $(-m, \lambda)$. `T_one` is the universe's tensor at the original point. `worst_pull` is the largest deviation of the copy's tensor from the pulled-back tensor $R_8TR_8$ (`@` is the matrix product), and `worst_copy` the largest Einstein residual of the copy alone on the mirror patch. The last value of `T_copy` is kept as `T_mirror`.

```python
reproduces(worst_pull < 1e-10, "the copy's tensor is R8 T R8 = T at 9 mirror points",
           PAIR_PY, "T2.metric.commuting.emt")
check(worst_copy < 1e-10,
      "the mirror copy ALONE solves the 64 Einstein equations on the mirror patch")
```

The checks: the copy's tensor is $R_8TR_8$, which equals $T$ because $T$ is diagonal (`python-pairing.json`, check `T2.metric.commuting.emt`), and the copy ALONE solves all 64 Einstein equations on the mirror patch. Output: four PASS lines, three with their records.

**In [10], figure 1: the Einstein residuals of the four sources.**

```python
tables = [
    ("universe $\\Phi$ alone", G_numeric + LAMBDA * np.eye(8) - T_universe),
    ("T1 partner $\\Gamma\\Phi$ alone", G_numeric + LAMBDA * np.eye(8) - T_partner),
    ("T1 pair (C1)", G_numeric + LAMBDA * np.eye(8) - T_universe - T_partner),
    ("T2 copy alone (mirror patch)", G_numeric + LAMBDA * np.eye(8) - T_mirror),
]
```

`tables` is a list of four pairs (title, residual): the universe alone, the T1 partner alone, the T1 pair, and the T2 copy alone (on the mirror patch). Each residual is $G + \Lambda - T$ for the source named.

```python
fig, axes = plt.subplots(1, 4, figsize=(14.0, 4.0))
for ax, (title, values) in zip(axes, tables):
    image = ax.imshow(values, cmap="RdBu_r", vmin=-48, vmax=48)
    for mu in range(8):
        if abs(values[mu, mu]) > 1e-6:
            ink = "white" if abs(values[mu, mu]) > 30 else "black"  # readable
            ax.text(mu, mu, f"{values[mu, mu]:.0f}", ha="center", va="center",
                    fontsize=6.5, color=ink)
    ax.set_xticks(range(8))
    ax.set_xticklabels(NAMES, fontsize=6.5)
    ax.set_yticks(range(8))
    ax.set_yticklabels(NAMES, fontsize=6.5)
    ax.grid(False)
    ax.set_title(title, fontsize=9)
fig.colorbar(image, ax=list(axes), shrink=0.75, label="residual (units $H^2$)")
```

One row of four panels, 14 by 4 inches. Each residual is drawn as a heat map with the colour scale from $-48$ to $48$ (`vmin`, `vmax`), the same in all panels. The inner loop writes the value of every nonzero diagonal entry into its square (`f"{...:.0f}"` prints it without decimals; `ha` and `va` centre the text), in white on dark squares (modulus above 30) and in black otherwise, so that it can be read. The labels, the switched-off grid, the titles and one common colour bar follow, as in Notebook 20a, In [8].

```python
save_figure(fig, "einstein_residuals",
            "The residual $G^\\mu{}_\\nu + \\Lambda\\delta^\\mu_\\nu - \\kappa "
...
            "equations there.")
```

`save_figure` saves `20b_1_einstein_residuals.png` and shows it (the eleven-line caption is shown here by its first and last lines). **What figure 1 shows.** Four $8 \times 8$ tables of the residual $G^\mu{}_\nu + \Lambda\delta^\mu_\nu - \kappa T^\mu{}_\nu$ (rows $\mu$, columns $\nu$, $x_1$ to $x_8$; colour scale in units $H^2$, white means zero), for the author's metric with $a_4 = Hx_4$ and $\Lambda = -36H^2$. The universe alone gives a white table: it solves all 64 equations. The T1 partner alone gives $2\kappa T$, with $-48$ on the diagonal except $-24$ at $x_4$. The T1 pair gives $G + \Lambda$, with $-24$ on the diagonal except $-12$ at $x_4$. The T2 copy alone on the mirror patch gives a white table again. The student should see that only the universe and its mirror copy solve the equations; the T1 partner and the T1 pair do not.

**In [11], figure 2: what Einstein gravity requires and what each source supplies.**

```python
rates = np.linspace(-2.5, 2.5, 501)
fig, ax = plt.subplots(figsize=(7.0, 4.6))
ax.plot(rates, -6 * (rates ** 2 + 1), color="black", linewidth=2.0,
        label="required: $-6(a_4'^2 + H^2)$")
```

501 rates $a_4'/H$ from $-2.5$ to $2.5$, and the requirement $-6(a_4'^2 + H^2)$ drawn as a thick black curve.

```python
supplied = (("universe $\\Phi$", null_universe, "tab:blue", "-"),
            ("T1 partner $\\Gamma\\Phi$", null_partner, "tab:red", "-"),
            ("T1 pair", null_universe + null_partner, "tab:purple", "--"),
            ("T2 copy", -T_mirror[3, 3] + T_mirror[7, 7], "tab:green", ":"))
for label, value, colour, style in supplied:
    ax.axhline(value, color=colour, linestyle=style, linewidth=1.6,
               label=f"{label} supplies {value:+.0f}")
ax.plot([-1.0, 1.0], [-12.0, -12.0], "o", color="tab:blue", markersize=8,
        label="solutions: $a_4' = \\pm H$")
```

`supplied` lists four (label, value, colour, line style) entries: the universe's $-12$, the partner's $+12$, the pair's $0$ and the copy's $-T^{x_4}{}_{x_4} + T^{x_8}{}_{x_8} = -12$. Each is drawn as a horizontal line (`ax.axhline`); the label prints the value with its sign (`:+.0f`). Two blue dots mark the two places where the universe's line meets the curve, $a_4' = \pm H$.

```python
ax.set_xlabel("rate $a_4'/H$ of the metric function")
ax.set_ylabel("$\\kappa(\\rho + p_8)/H^2$")
ax.set_ylim(-45, 18)
ax.set_title("What Einstein gravity requires, and what each source supplies")
ax.legend(fontsize=7.5, loc="lower center", ncol=2)
```

The axis labels, the vertical range from $-45$ to $18$ (`set_ylim`), the title and a legend in two columns below the curve.

```python
save_figure(fig, "null_requirement",
            "The null combination $\\kappa(\\rho + p_8)$ (energy density plus the "
...
            "nowhere.")
```

**What figure 2 shows.** Horizontal axis: the rate $a_4'/H$; vertical axis: the null combination $\kappa(\rho + p_8)$ in units $H^2$. The black parabola is what Einstein gravity requires of every source; its highest point is $-6$, at $a_4' = 0$. The blue line of the universe ($-12$) meets it at $a_4' = \pm H$; the green dotted line of the T2 copy lies on top of the blue one. The red line of the T1 partner ($+12$) and the purple dashed line of the T1 pair ($0$) lie above the parabola's highest point and meet it nowhere. The student should see in one picture why the partner and the pair cannot be the source of the author's metric for any rate, while the universe and its mirror copy can.

**In [12], figure 3: the bookkeeping.**

```python
rho_u, p_u = -T_universe[3, 3], T_universe[0, 0]
rho_m, p_m = -T_mirror[3, 3], T_mirror[0, 0]
J_u = float(charge_value)
rows = {
    "universe": (rho_u, p_u, J_u, float(S_value)),
    "T1 partner": (-T_partner[3, 3], T_partner[0, 0], float(partner_charge),
                   float(S_value)),
    "T1 pair": (rho_u - T_partner[3, 3], p_u + T_partner[0, 0],
                J_u + float(partner_charge), 2 * float(S_value)),
    "T2 copy": (rho_m, p_m, float(copy_charge), -float(S_value)),
    "T2 pair": (rho_u + rho_m, p_u + p_m, J_u + float(copy_charge), 0.0),
}
```

The numbers of the table of Section 20.12: $\rho$ and $p$ of the universe and of the copy, the universe's charge density as a floating-point number, and the dictionary `rows`, which holds for each of the five objects the four numbers $(\rho, p, J^{x_4}, S)$. The T1 pair adds the universe and the partner at the same point; the T2 pair adds the universe and the copy, each at its own point; the T2 pair's $S$ is $S + (-S) = 0$.

```python
for name, (r, p, j, s) in rows.items():
    say(f"{name:11s}: rho = {r:+7.2f}, p = {p:+7.2f}, J^x4 = {j:+6.2f}, "
        f"S = {s:+5.2f}")
check(abs(rows["T1 pair"][0]) < 1e-10 and abs(rows["T1 pair"][2]) < 1e-12
      and abs(rows["T2 pair"][0] - 24) < 1e-9 and abs(rows["T2 pair"][2] + 6) < 1e-12,
      "T1 pair: rho = 0 and J = 0; T2 pair: rho = 24 and J = -6")
```

The loop prints one line per object; in the f-string, `{name:11s}` pads the name to 11 characters and `{r:+7.2f}` prints a number with its sign, two decimals, in a field of 7 characters, so that the columns line up. Output: the five lines of the table (universe $+12$, $-24$, $-3$, $+2.40$; T1 partner $-12$, $+24$, $+3$, $+2.40$; T1 pair $0$, $0$, $0$, $+4.80$; T2 copy $+12$, $-24$, $-3$, $-2.40$; T2 pair $+24$, $-48$, $-6$, $0$). The check: the T1 pair has $\rho = 0$ and $J^{x_4} = 0$, the T2 pair $\rho = 24$ and $J^{x_4} = -6$.

```python
quantities = ["$\\rho$", "$p$", "$J^{x_4}$", "$S$"]
fig, ax = plt.subplots(figsize=(9.0, 5.0))
width = 0.16
colours = ["tab:blue", "tab:red", "tab:purple", "tab:green", "tab:olive"]
for k, (name, values) in enumerate(rows.items()):
    positions = np.arange(4) + (k - 2) * width
    ax.bar(positions, values, width=width, color=colours[k], label=name)
    for x_value, value in zip(positions, values):
        if abs(value) < 1e-9:  # a bar of height zero: write 0 so it is seen
            ax.text(x_value, 1.0, "0", ha="center", fontsize=8,
                    color=colours[k], fontweight="bold")
```

A grouped bar chart: four groups (the quantities $\rho$, $p$, $J^{x_4}$, $S$), five bars in each (the objects). `np.arange(4)` is $0, 1, 2, 3$, the centres of the groups; the bar of object $k$ is shifted by $(k - 2)$ times the width 0.16, so the five bars stand side by side. `enumerate` numbers the objects $k = 0, \dots, 4$. A bar of height zero cannot be seen, so the inner loop writes a bold 0 in its place.

```python
ax.axhline(0.0, color="black", linewidth=0.8)
ax.set_xticks(range(4))
ax.set_xticklabels(quantities)
ax.set_ylabel("value (units $H = \\kappa = 1$)")
ax.set_title("The bookkeeping of one universe and its partners")
ax.legend(fontsize=8, ncol=5, loc="upper center", bbox_to_anchor=(0.5, -0.08))
ax.set_ylim(-52, 30)
save_figure(fig, "bookkeeping",
...
            "charge of the universe.")
```

A thin line at zero, the names of the quantities under the groups, the label, the title, a legend in five columns below the chart, and the vertical range. **What figure 3 shows.** Groups of bars for $\rho$, $p$, $J^{x_4}$ and $S$ (units $H = \kappa = 1$). The red bars of the T1 partner are the blue bars of the universe reversed in $\rho$, $p$ and $J^{x_4}$ and equal in $S$, so the T1 pair (purple) is zero in the first three groups. The green bars of the T2 copy equal the blue ones in $\rho$, $p$ and $J^{x_4}$ and are reversed in $S$, so the T2 pair (olive) has twice the energy, twice the pressure and twice the charge. The student should see the difference between the two theorems as two different patterns of bars: T1 cancels, T2 adds.

**In [13], figure 4: the partner in time.**

```python
times = np.linspace(0.0, 3.0, 601)
phi_t = np.outer(np.exp(-1j * W * times), phi0_num)  # rows: times, columns: A
partner_t = phi_t @ Gamma_num.T  # Gamma Phi at every time
```

601 times from 0 to 3. `np.outer(a, b)` is the table of all products $a_ib_j$: here row $i$ is the universe $\Phi_0e^{-iwx_4}$ at the $i$-th time. `partner_t` is $\Gamma\Phi$ at every time: multiplying each row by $\Gamma^T$ from the right is the same as multiplying each column vector by $\Gamma$ from the left.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(12.0, 4.4))
for index, colour in ((0, "tab:blue"), (8, "tab:orange")):
    left.plot(times, phi_t[:, index].real, color=colour, linewidth=4.0,
              alpha=0.35, label=f"universe, component {index + 1}")
    left.plot(times, partner_t[:, index].real, "--", color=colour,
              label=f"partner, component {index + 1}")  # drawn on top
left.set_xlabel("time $x_4$ (units $1/H$)")
left.set_ylabel("real part")
left.set_title("same oscillation, the first half of the components reversed",
               fontsize=9)
left.legend(fontsize=7.5, loc="lower left", ncol=2)
left.set_ylim(-2.2, 1.7)
```

The left panel: the real parts of components 1 and 9 (positions 0 and 8) of the universe as thick pale lines (`linewidth=4.0`, `alpha=0.35`), and of the partner as dashed lines drawn on top. Component 1 lies in the half where $\Gamma = -1$, component 9 in the half where $\Gamma = +1$. Labels, title, legend and the vertical range follow.

```python
eig_u = np.linalg.eigvals(np.array(A_matrix.tolist(), dtype=float))
eig_p = np.linalg.eigvals(np.array(A_partner.tolist(), dtype=float))
right.plot(eig_u.real, eig_u.imag, "o", markersize=11, markerfacecolor="none",
           color="tab:blue", label="universe: eigenvalues of $\\mathcal{A}$")
right.plot(eig_p.real, eig_p.imag, "x", markersize=9, color="tab:red",
           label="partner: eigenvalues of $\\mathcal{A}'$")
right.set_xlim(-1.5, 1.5)
right.set_ylim(-5.5, 5.5)
right.set_xlabel("real part")
right.set_ylabel("imaginary part (units $H$)")
right.set_title("equal spectra: $\\pm 4i$, eight times each", fontsize=9)
right.legend(fontsize=8, loc="center right")
```

The right panel: `np.linalg.eigvals` computes the 16 eigenvalues of $\mathcal{A}$ and of $\mathcal{A}'$ in floating point; they are drawn in the complex plane (real part horizontal, imaginary part vertical), the universe's as open circles (`markerfacecolor="none"`), the partner's as crosses.

```python
check(np.allclose(np.sort(eig_u.imag), np.sort(eig_p.imag), atol=1e-12)
      and np.abs(eig_u.real).max() < 1e-12,
      "both spectra are +-4i, eight times each (numerically)")
```

The check: sorted by their imaginary parts, the two lists of eigenvalues agree to $10^{-12}$ (`np.allclose`), and their real parts are zero to $10^{-12}$.

```python
save_figure(fig, "partner_in_time",
            "Left: the real parts of components 1 and 9 of the universe "
...
            "the opposite energy density.")
```

**What figure 4 shows.** Left: the real parts of components 1 and 9 of the universe (thick pale) and of its T1 partner (dashed) against the time $x_4$ in units $1/H$. Component 1 of the partner is the universe's component 1 with the opposite sign; component 9 is the same; both oscillate with the period $2\pi/4 \approx 1.57$. Right: the eigenvalues of $\mathcal{A}$ (circles) and of $\mathcal{A}' = \Gamma\mathcal{A}\Gamma$ (crosses) in the complex plane: all lie at $+4i$ and $-4i$, eight times each, and the crosses sit inside the circles. The student should see that the partner has the same frequency as the universe, although its energy density is the opposite: a negative energy density here is not a negative frequency.

**In [14], the last check.**

```python
figure_names = ["einstein_residuals", "null_requirement", "bookkeeping",
                "partner_in_time"]
paths = [output_file(f"{FIGURE_FOLDER}/20b_{k}_{name}.png")
         for k, name in enumerate(figure_names, 1)]
check(all(path.is_file() for path in paths),
      "every figure file of this notebook exists")
all_checks_passed()
```

As in Notebook 20a, In [19]: the four figure files `20b_1_einstein_residuals.png` to `20b_4_partner_in_time.png` must exist, and `all_checks_passed()` prints the last line. Output: PASS every figure file of this notebook exists, and ALL 25 CHECKS PASSED (notebook 20b).

### 20.17 Allowed is not the same as happens: an electron and a positron made from light

**Why a lesson from ordinary physics.** To judge whether the equations of this book prove that universes are created, we must know what a proof of creation contains when physics does have one. The creation of an electron and a positron (its **antiparticle**: the same mass, the opposite electric charge) from light is understood completely. It shows the three questions of Section 20.4 answered one after the other, and it shows that the answer to the first (allowed?) is computed from conservation laws alone, while the answers to the second and the third (does it happen? how often?) need a dynamical theory.

**Words and the standard physics we use.** We use ordinary space with three directions and one time, units in which the speed of light is 1, and energies, momenta and masses measured in units of the electron mass $m$. A body of mass $\mu$ with the **momentum** $\vec p = (p_1, p_2, p_3)$, a vector of length $|\vec p| = \sqrt{p_1^2 + p_2^2 + p_3^2}$, has the energy $E = \sqrt{\mu^2 + |\vec p|^2}$ (the energy-momentum relation of special relativity). A **photon**, a particle of light, has $\mu = 0$, so $E = |\vec p|$. For a collection of bodies the total energy $E_{\mathrm{tot}}$ and the total momentum $\vec p_{\mathrm{tot}}$ are sums over the bodies, and the **invariant mass** $\mu$ of the collection is defined by

$$
\mu^2 = E_{\mathrm{tot}}^2 - |\vec p_{\mathrm{tot}}|^2 .
$$

For a single body it is its mass. ASSUMED (standard physics, not derived in this book): the energy-momentum relation, and the conservation of the total energy, the total momentum and the total electric charge of an isolated system in every process. Since $\mu^2$ is built from conserved totals, it is conserved too. A **threshold** is the smallest energy at which a process is allowed.

**The rule of every threshold.** A process from a state A to a state B is forbidden if some conserved quantity has different values in A and in B. So $\mu_A = \mu_B$ is NECESSARY. The lemma below says that a final state of bodies with masses $\mu_1, \mu_2, \dots$ has $\mu_B \ge \mu_1 + \mu_2 + \cdots$, so the initial state must bring at least the sum of the final masses as invariant mass. This is a necessary condition only.

**Lemma (two bodies have at least the sum of their masses).** Two bodies with masses $\mu_1, \mu_2 \ge 0$ and momenta $\vec p_1, \vec p_2$ have together $(E_1 + E_2)^2 - |\vec p_1 + \vec p_2|^2 \ge (\mu_1 + \mu_2)^2$.

*Proof, line by line.* Write $a = |\vec p_1|$ and $b = |\vec p_2|$.

1. Multiplying out, $(E_1 + E_2)^2 - |\vec p_1 + \vec p_2|^2 = (E_1^2 - a^2) + (E_2^2 - b^2) + 2(E_1E_2 - \vec p_1\cdot\vec p_2)$, because $|\vec p_1 + \vec p_2|^2 = a^2 + b^2 + 2\vec p_1\cdot\vec p_2$ (the **dot product** $\vec p_1\cdot\vec p_2 = p_{1,1}p_{2,1} + p_{1,2}p_{2,2} + p_{1,3}p_{2,3}$).
2. The energy-momentum relation $E_i^2 - |\vec p_i|^2 = \mu_i^2$ turns this into $\mu_1^2 + \mu_2^2 + 2(E_1E_2 - \vec p_1\cdot\vec p_2)$.
3. The dot product is at most the product of the lengths, $\vec p_1\cdot\vec p_2 = ab\cos\theta \le ab$ ($\theta$ is the angle between the vectors). So it is enough to show $E_1E_2 \ge \mu_1\mu_2 + ab$.
4. Both sides of that inequality are not negative, so we may compare their squares: $E_1^2E_2^2 - (\mu_1\mu_2 + ab)^2 = (\mu_1^2 + a^2)(\mu_2^2 + b^2) - (\mu_1\mu_2 + ab)^2$.
5. Multiplying out, $(\mu_1^2 + a^2)(\mu_2^2 + b^2) = \mu_1^2\mu_2^2 + \mu_1^2b^2 + \mu_2^2a^2 + a^2b^2$ and $(\mu_1\mu_2 + ab)^2 = \mu_1^2\mu_2^2 + 2\mu_1\mu_2ab + a^2b^2$; the terms $\mu_1^2\mu_2^2$ and $a^2b^2$ cancel in the difference, and what remains is $\mu_1^2b^2 - 2\mu_1\mu_2ab + \mu_2^2a^2 = (\mu_1b - \mu_2a)^2 \ge 0$, a square.
6. Hence $E_1E_2 - \vec p_1\cdot\vec p_2 \ge \mu_1\mu_2$, and line 2 is at least $\mu_1^2 + \mu_2^2 + 2\mu_1\mu_2 = (\mu_1 + \mu_2)^2$. QED.

Equality needs equality in lines 3 and 5: parallel momenta and $\mu_1b = \mu_2a$, that is $b/\mu_2 = a/\mu_1$: the two bodies move with the same velocity. Applied twice, the lemma gives the same for three bodies, $\mu \ge \mu_1 + \mu_2 + \mu_3$ (first combine two of them into one collection of invariant mass at least $\mu_1 + \mu_2$, then add the third).

**Proposition 1 (one photon can never make a pair).** A single photon in empty space cannot turn into an electron and a positron. *Proof.* Before: one photon, $\mu_A^2 = E^2 - |\vec p|^2 = 0$. After: two bodies of mass $m$, so $\mu_B \ge 2m > 0$ by the lemma. Conservation needs $\mu_A = \mu_B$, so $0 \ge 2m$, which is false. QED. Charge does not forbid the process ($-1 + 1 = 0$, the photon's charge), and energy alone does not either (the photon may have any energy): the COMBINATION of energy and momentum forbids it.

**Proposition 2 (a photon on a nucleus).** A photon of energy $E_\gamma$ that hits a **nucleus** (the heavy centre of an atom) of mass $M$ at rest can make an electron-positron pair, the nucleus remaining in the final state, only if $E_\gamma \ge 2m(1 + m/M)$. *Proof, line by line.*

1. Before: the total energy is $E_\gamma + M$ and the total momentum is the photon's, of length $E_\gamma$, so $\mu_A^2 = (E_\gamma + M)^2 - E_\gamma^2 = M^2 + 2E_\gamma M$ (multiply out; $E_\gamma^2$ cancels).
2. After: by the lemma applied twice, $\mu_B \ge m + m + M = 2m + M$.
3. Conservation, $\mu_A = \mu_B$, therefore needs $M^2 + 2E_\gamma M \ge (2m + M)^2 = M^2 + 4mM + 4m^2$.
4. Subtract $M^2$ from both sides and divide by $2M > 0$: $E_\gamma \ge 2m + 2m^2/M = 2m(1 + m/M)$. QED.

Conversely, at and above this energy the conservation laws allow the process: at exactly the threshold the three final bodies move together with the common velocity $v = |\vec p_{\mathrm{tot}}|/E_{\mathrm{tot}}$ (the equality case of the lemma), and each carries the share $\mu_i/\mu$ of the total momentum. For $M = 4m$: $E_\gamma = 2m(1 + 1/4) = 5m/2$; the totals are $|\vec p_{\mathrm{tot}}| = 5m/2$ and $E_{\mathrm{tot}} = 5m/2 + 4m = 13m/2$; $\mu = 6m$; the electron and the positron carry the momentum $(1/6)(5m/2) = 5m/12$ each and the energy $\sqrt{m^2 + 25m^2/144} = 13m/12$ each; the nucleus carries $(4/6)(5m/2) = 5m/3$ and $\sqrt{16m^2 + 25m^2/9} = 13m/3$. The momenta add up to $5m/12 + 5m/12 + 5m/3 = 30m/12 = 5m/2$ and the energies to $13m/12 + 13m/12 + 52m/12 = 78m/12 = 13m/2$: exactly the initial totals (COMPUTED exactly, Notebook 20c, In [5]). For a heavy nucleus the threshold approaches the two **rest energies** $2m$: for $M = 1000m$ it is $1001m/500 = 2.002m$, and for $M = 1836m$ (about the mass of a proton) $1837m/918 \approx 2.001089m$. The nucleus takes up the momentum but almost no energy.

**Proposition 3 (two photons).** Two photons of energies $E_a$ and $E_b$ that meet at the angle $\theta$ between their directions can make a pair only if $E_aE_b \ge 2m^2/(1 - \cos\theta)$. *Proof.* $\mu^2 = (E_a + E_b)^2 - |\vec p_a + \vec p_b|^2 = E_a^2 + 2E_aE_b + E_b^2 - (E_a^2 + E_b^2 + 2E_aE_b\cos\theta) = 2E_aE_b(1 - \cos\theta)$, using $|\vec p_a| = E_a$, $|\vec p_b| = E_b$ and $\vec p_a\cdot\vec p_b = E_aE_b\cos\theta$; the lemma requires $\mu \ge 2m$, that is $\mu^2 \ge 4m^2$, and dividing by $2(1 - \cos\theta) > 0$ gives the claim. QED. Head on ($\theta = 180$ degrees, $\cos\theta = -1$) this is $E_aE_b \ge m^2$; photons moving in the same direction ($\theta = 0$, $\mu = 0$) can never make a pair.

**Status.** The lemma and Propositions 1 to 3 are PROVED here from the ASSUMED standard physics above, and Notebook 20c checks them with sympy and on random samples. They answer Q1 completely: below the threshold the process is forbidden, at and above it allowed. They say NOTHING about Q2 and Q3. That pairs are really made above the threshold, and how often, was computed from **quantum electrodynamics**, the quantum theory of electrons and light, by Bethe and Heitler (H. Bethe and W. Heitler, Proc. R. Soc. Lond. A 146, 83 (1934)) for a photon on a nucleus, and by Breit and Wheeler (G. Breit and J. A. Wheeler, Phys. Rev. 46, 1087 (1934)) for two photons. This book quotes these works; it does not compute their results.

**Three lessons for universes.**

1. Conservation laws are NECESSARY conditions. They can rule a process out (Proposition 1); they never rule a process in.
2. Whether an allowed process happens, and how often, is computed from the DYNAMICS, here an interaction between light and the electron field. Without it the photon could not hand its energy to the pair.
3. The electron and the positron are two quanta of ONE field, the electron field, whose total charge is $-1 + 1 = 0$, and that field interacts with light. The two universes of a T1 pair are configurations of two DIFFERENT theories, with parameters $(m, \lambda)$ and $(-m, -\lambda)$, and no term of any Lagrangian of the Revision record couples them. Section 20.22 draws the consequence for their charges.

The comparison, item by item (the right column is the subject of Sections 20.22 to 20.25):

| question | electron and positron from light | universes of masses $+m$ and $-m$ |
| --- | --- | --- |
| Q1: conserved quantities | energy, momentum, charge | the U(1) charge of each universe (PROVED); the momenta of each universe along $x_1, x_2, x_3, x_5, x_6, x_7$ and its rotation quantities (derived, Section 20.22 (d')); the energy of a universe is not conserved in the deflating metric |
| Q1: an interaction that lets energy or charge pass | light couples to electrons | none in the theory |
| Q2: the dynamics of creation | quantum electrodynamics | none derived |
| Q3: rate, probability, amplitude | computed in 1934 (quoted) | none |

### 20.18 Example: the threshold of pair creation, computed

Notebook 20c proves the lemma's key line with sympy and tests the lemma on 20000 random pairs of bodies, shows on 5000 random electron-positron states that one photon can never make a pair, derives the threshold $2m(1 + m/M)$ on a nucleus with an exact final state at the threshold, and the allowed region for two photons. At the end it reads, from the Revision record of the pairing theorems, which of the three questions those theorems answer for universes, and the U(1) record of one universe. It prints 12 PASS lines, one of which reproduces a named check of a Revision report, and draws four figures. It needs numpy, sympy and matplotlib, no Rust, and runs in about 15 seconds (its recorded check run on the build computer, which was busy with other work at the time, took 28.1 seconds).

<!-- NOTEBOOK 20c -->

### 20.21 Line-by-line walk-through of Notebook 20c

The notebook has 10 code cells, In [1] to In [10].

**In [1], the set-up cell.** It is word for word the set-up cell of Notebook 20a, explained line by line in Section 20.11, except that its comment lines hold the run instructions of Notebook 20c (Section 20.19) and one line names the notebook:

```python
NOTEBOOK_ID = "20c"  # this notebook: chapter 20, example c
```

Output: Set-up of notebook 20c complete.

**In [2], the lemma.**

```python
import numpy as np  # arrays and random numbers
import sympy as sp  # exact algebra

mu1, mu2, a, b = sp.symbols("mu1 mu2 a b", nonnegative=True)
E1_sq, E2_sq = mu1 ** 2 + a ** 2, mu2 ** 2 + b ** 2  # E_i^2 = mu_i^2 + |p_i|^2
line5 = sp.expand(E1_sq * E2_sq - (mu1 * mu2 + a * b) ** 2)
check(sp.expand(line5 - (mu1 * b - mu2 * a) ** 2) == 0,
      "line 5: E1^2 E2^2 - (mu1 mu2 + a b)^2 = (mu1 b - mu2 a)^2")
```

numpy and sympy are loaded. The four symbols $\mu_1, \mu_2, a, b$ are declared not negative (`nonnegative=True`), as in the lemma. `E1_sq` and `E2_sq` are $E_1^2 = \mu_1^2 + a^2$ and $E_2^2 = \mu_2^2 + b^2$. `line5` is $E_1^2E_2^2 - (\mu_1\mu_2 + ab)^2$, multiplied out; the check confirms that it equals $(\mu_1b - \mu_2a)^2$, line 5 of the proof, exactly.

```python
def invariant_mass(energies, momenta):
    """mu = sqrt(E_tot^2 - |p_tot|^2) of a collection of bodies."""
    E_total = np.sum(energies, axis=0)
    p_total = np.sum(momenta, axis=0)
    return np.sqrt(np.maximum(E_total ** 2 - np.sum(p_total ** 2, axis=-1), 0.0))
```

`invariant_mass` computes $\mu = \sqrt{E_{\mathrm{tot}}^2 - |\vec p_{\mathrm{tot}}|^2}$ for many collections at once. The energies form an array with one row per body; `np.sum(..., axis=0)` adds the rows, so `E_total` holds the total energy of each collection. The momenta form an array with one row per body and three numbers per momentum; `axis=0` again adds over the bodies. `np.sum(p_total ** 2, axis=-1)` adds the squares of the three components (the last axis) and gives $|\vec p_{\mathrm{tot}}|^2$. `np.maximum(..., 0.0)` replaces a tiny negative rounding error by 0 before the square root.

```python
rng = np.random.default_rng(20261007)  # fixed seed: the same numbers every run
count = 20000
masses = rng.uniform(0.0, 3.0, size=(2, count))  # mu1, mu2
momenta = rng.normal(size=(2, count, 3)) * rng.uniform(0.0, 4.0, size=(2, count, 1))
energies = np.sqrt(masses ** 2 + np.sum(momenta ** 2, axis=-1))
mu_total = invariant_mass(energies, momenta)
margin = mu_total - masses.sum(axis=0)  # must never be negative
report("smallest margin mu_total - (mu1 + mu2) in 20000 pairs",
       f"{margin.min():.2e}")
check(margin.min() > -1e-12, "the lemma holds for all 20000 random pairs")
```

A random-number generator with a fixed seed. `masses` is a $2 \times 20000$ array of masses drawn uniformly between 0 and 3. `momenta` is a $2 \times 20000 \times 3$ array: normal random vectors, each multiplied by a random length factor between 0 and 4 (the last axis of size 1 multiplies all three components of a vector by the same number). `energies` is $\sqrt{\mu^2 + |\vec p|^2}$ for each body. `margin` is the invariant mass of each pair minus the sum of its two masses; the lemma says it is never negative. Output: RESULT smallest margin mu_total - (mu1 + mu2) in 20000 pairs = 2.34e-04, and PASS the lemma holds for all 20000 random pairs (the check allows $-10^{-12}$ for rounding).

**In [3], figure 1: the lemma on 20000 pairs.**

```python
fig, ax = plt.subplots(figsize=(6.4, 5.0))
ax.plot(masses.sum(axis=0), mu_total, ".", markersize=1.5, alpha=0.4,
        color="tab:blue", label="20000 random pairs")
ax.plot([0, 6], [0, 6], color="black", linewidth=1.5,
        label="$\\mu = \\mu_1 + \\mu_2$")
ax.set_xlabel("sum of the masses $\\mu_1 + \\mu_2$ (units $m$)")
ax.set_ylabel("invariant mass of the pair $\\mu$ (units $m$)")
ax.set_xlim(0, 6)
ax.set_ylim(0, 16)
ax.set_title("Two bodies have at least the sum of their masses")
ax.legend(fontsize=8, loc="upper left", markerscale=6)
```

A scatter plot: each pair is a dot (marker `"."`, size 1.5, 40 per cent opaque) at the sum of its masses (horizontal) and its invariant mass (vertical); the black line is the diagonal $\mu = \mu_1 + \mu_2$. The axis ranges, the title and a legend (`markerscale=6` enlarges the dot in the legend) follow.

```python
save_figure(fig, "invariant_mass_inequality",
            "The invariant mass "
...
            "of every threshold.")
```

**What figure 1 shows.** Horizontal axis: the sum of the two masses $\mu_1 + \mu_2$; vertical axis: the invariant mass $\mu$ of the pair; both in units of the electron mass $m$. Every one of the 20000 dots lies on or above the black diagonal, and the dots crowd towards it from above. The student should see the lemma as a picture: a collection of bodies never has less invariant mass than the sum of its masses, which is why every creation process has a threshold.

**In [4], one photon can never make a pair.**

```python
pair_momenta = rng.normal(size=(2, 5000, 3)) * 3.0  # electron and positron
pair_energies = np.sqrt(1.0 + np.sum(pair_momenta ** 2, axis=-1))  # m = 1
pair_mu = invariant_mass(pair_energies, pair_momenta)
report("smallest invariant mass of 5000 electron-positron states",
       f"{pair_mu.min():.4f}")
check(pair_mu.min() >= 2.0 - 1e-12, "every electron-positron state has mu >= 2 m > 0")
```

5000 random electron-positron states: the two momenta are normal random vectors times 3, and the energies are $\sqrt{1 + |\vec p|^2}$ because $m = 1$. The smallest invariant mass is printed with four decimals and must be at least $2m$; a single photon has invariant mass 0, so no state of the list can be reached from one photon. Output: RESULT smallest invariant mass of 5000 electron-positron states = 2.0003, and the PASS line.

**In [5], a photon on a nucleus: the threshold.**

```python
E_gamma, M_nuc, m_e = sp.symbols("E_gamma M m", positive=True)
mu_initial_sq = (E_gamma + M_nuc) ** 2 - E_gamma ** 2  # line 1
threshold = sp.solve(sp.Eq(mu_initial_sq, (2 * m_e + M_nuc) ** 2), E_gamma)[0]
say(f"threshold photon energy: {sp.factor(threshold)}")
check(sp.simplify(threshold - 2 * m_e * (1 + m_e / M_nuc)) == 0,
      "E_threshold = 2 m (1 + m/M)")
```

The positive symbols $E_\gamma$, $M$ and $m$. `mu_initial_sq` is line 1 of the proof of Proposition 2, $\mu_A^2 = (E_\gamma + M)^2 - E_\gamma^2$. `sp.Eq(a, b)` is the equation $a = b$; solving $\mu_A^2 = (2m + M)^2$ for $E_\gamma$ gives the threshold, and `sp.factor` prints it as a product. Output: threshold photon energy: 2*m*(M + m)/M. The check compares it with $2m(1 + m/M)$.

```python
M4 = 4  # the nucleus of mass 4 m, with m = 1
E_th = threshold.subs({m_e: 1, M_nuc: M4})  # 5/2
p_total, E_total = E_th, E_th + M4  # the initial totals
mu_final = sp.Integer(2 + M4)  # 6 m
shares = [1, 1, M4]  # electron, positron, nucleus masses
p_parts = [sp.Rational(mass) * p_total / mu_final for mass in shares]
E_parts = [sp.sqrt(mass ** 2 + p ** 2) for mass, p in zip(shares, p_parts)]
say(f"final state at threshold: momenta {p_parts}, energies {E_parts}")
check(sum(p_parts) == p_total and sp.simplify(sum(E_parts) - E_total) == 0
      and E_th == sp.Rational(5, 2),
      "M = 4 m: the threshold state conserves energy and momentum exactly")
```

The exact final state at the threshold for $M = 4m$ (with $m = 1$): the threshold $E_\gamma = 5/2$; the initial totals $|\vec p_{\mathrm{tot}}| = 5/2$ and $E_{\mathrm{tot}} = 13/2$; the final invariant mass $\mu = 6$; the masses of the electron, the positron and the nucleus; each momentum the share $\mu_i/\mu$ of the total; each energy $\sqrt{\mu_i^2 + p_i^2}$ (`zip` pairs each mass with its momentum). Output: momenta [5/12, 5/12, 5/3], energies [13/12, 13/12, 13/3]. The check requires the momenta to add up to $5/2$ and the energies to $13/2$ exactly, and the threshold to be $5/2$.

```python
for M_value in (4, 1000, 1836):
    value = threshold.subs({m_e: 1, M_nuc: M_value})
    report(f"threshold for M = {M_value} m", f"{sp.nsimplify(value)} = "
           f"{float(value):.6f} m")
check(threshold.subs({m_e: 1, M_nuc: 1836}) == 2 + sp.Rational(2, 1836),
      "M = 1836 m: the threshold is 2 m + 2 m/1836, just above 2 m")
```

The threshold for $M = 4m$, $1000m$ and $1836m$, printed as an exact fraction (`sp.nsimplify`) and with six decimals. Output: 5/2 = 2.500000 m, 1001/500 = 2.002000 m, 1837/918 = 2.001089 m. The last check confirms exactly that for $M = 1836m$ the threshold is $2m + 2m/1836$, just above the two rest energies.

**In [6], figure 2: the threshold against the mass of the nucleus.**

```python
M_axis = np.logspace(-0.5, 4, 400)  # M/m from about 0.3 to 10000
fig, ax = plt.subplots(figsize=(7.0, 4.4))
ax.semilogx(M_axis, 2 * (1 + 1 / M_axis), color="tab:blue",
            label="threshold $2m(1 + m/M)$")
ax.axhline(2.0, color="black", linestyle=":", label="the two rest energies $2m$")
for M_value, marker in ((4, "o"), (1000, "s"), (1836, "^")):
    ax.plot([M_value], [2 * (1 + 1 / M_value)], marker, color="tab:red",
            markersize=7, label=f"$M = {M_value}m$: {2 * (1 + 1 / M_value):.5f}$m$")
ax.fill_between(M_axis, 2 * (1 + 1 / M_axis), 9.0, color="tab:green", alpha=0.12,
                label="allowed (not forbidden)")
ax.set_ylim(1.5, 9.0)
ax.set_xlabel("mass of the nucleus $M/m$")
ax.set_ylabel("photon energy $E_\\gamma/m$")
ax.set_title("Pair creation on a nucleus: the threshold")
ax.legend(fontsize=8, loc="upper right")
```

400 masses $M/m$ spaced evenly on a logarithmic scale from $10^{-0.5} \approx 0.3$ to $10^4$ (`np.logspace`). `ax.semilogx` draws the threshold $2(1 + 1/M)$ with a logarithmic horizontal axis. The dotted line is the two rest energies $2m$; the three red markers are the thresholds for $M = 4m$, $1000m$ and $1836m$, labelled with five decimals; `fill_between` shades the allowed region above the curve in light green. The vertical range, the labels, the title and the legend follow.

```python
save_figure(fig, "nucleus_threshold",
            "The smallest photon energy $E_\\gamma$ (vertical, units of the "
...
            "often the process happens above the threshold.")
```

**What figure 2 shows.** Horizontal axis: the mass of the nucleus $M/m$ (logarithmic); vertical axis: the photon energy $E_\gamma/m$. The blue curve is the threshold $2m(1 + m/M)$; above it (green) the process is allowed by the conservation laws, below it forbidden. A light nucleus needs much more than the two rest energies; for a heavy nucleus the curve approaches the dotted line $2m$. The student should also see what the picture does NOT say: nothing about how often the process happens in the green region.

**In [7], figure 3: what the initial state brings and what the final state needs.**

```python
E_axis = np.linspace(0.0, 6.0, 601)
brought = np.sqrt(M4 ** 2 + 2 * E_axis * M4)  # mu_A for M = 4 m
crossing = E_axis[np.argmin(np.abs(brought - (2 + M4)))]
report("crossing of the two curves (M = 4 m)", f"{crossing:.2f} m")
check(abs(crossing - 2.5) < 0.01, "the curves cross at E_gamma = 2.5 m")
```

601 photon energies from 0 to 6. `brought` is the invariant mass of the initial state, $\sqrt{M^2 + 2E_\gamma M}$ with $M = 4$. `np.argmin(np.abs(brought - 6))` is the position of the photon energy at which `brought` is closest to the needed $2m + M = 6$; `crossing` is that energy. Output: RESULT crossing of the two curves (M = 4 m) = 2.50 m, and the PASS line (to 0.01, the spacing of the grid).

```python
fig, ax = plt.subplots(figsize=(7.0, 4.4))
ax.plot(E_axis, brought, color="tab:blue", label="brought: $\\sqrt{M^2 + 2E_\\gamma M}$")
ax.axhline(2 + M4, color="tab:red", label="needed at least: $2m + M = 6m$")
ax.axvline(2.5, color="black", linestyle=":", label="threshold $E_\\gamma = 5m/2$")
ax.fill_between(E_axis, 2 + M4, brought, where=brought >= 2 + M4,
                color="tab:green", alpha=0.15, label="allowed")
ax.set_xlabel("photon energy $E_\\gamma/m$")
ax.set_ylabel("invariant mass (units $m$)")
ax.set_title("Photon on a nucleus of mass $M = 4m$")
ax.legend(fontsize=8, loc="lower right")
```

The rising blue curve of what the initial state brings, the red horizontal line of what the final state needs at least, the dotted vertical line of the threshold, and the green shading where the first is at or above the second (`where=` restricts the shading). Labels, title and legend follow.

```python
save_figure(fig, "allowed_photon_energies",
            "For a photon hitting a nucleus of mass $M = 4m$ at rest: the invariant "
...
            "$E_\\gamma = 5m/2$ (dotted) on.")
```

**What figure 3 shows.** Horizontal axis: the photon energy $E_\gamma/m$; vertical axis: invariant mass in units $m$; nucleus $M = 4m$. The blue curve (brought) rises with the photon energy and crosses the red line (needed, $6m$) at $E_\gamma = 5m/2$, the dotted threshold. The student should see the threshold as the meeting point of two curves: to the left the process is forbidden, to the right allowed.

**In [8], figure 4: two photons.**

```python
Ea, Eb, theta = sp.symbols("E_a E_b theta", positive=True)
pa = sp.Matrix([Ea, 0, 0])  # photon a along the first axis
pb = sp.Matrix([Eb * sp.cos(theta), Eb * sp.sin(theta), 0])  # photon b at angle
mu_sq = sp.simplify((Ea + Eb) ** 2 - (pa + pb).dot(pa + pb))
check(sp.simplify(mu_sq - 2 * Ea * Eb * (1 - sp.cos(theta))) == 0,
      "two photons: mu^2 = 2 E_a E_b (1 - cos theta)")
check(sp.simplify(mu_sq.subs(theta, sp.pi) - 4 * Ea * Eb) == 0
      and mu_sq.subs(theta, 0) == 0,
      "head on mu^2 = 4 E_a E_b; same direction mu^2 = 0 (never allowed)")
```

The positive symbols $E_a$, $E_b$, $\theta$. Photon a moves along the first axis, $\vec p_a = (E_a, 0, 0)$; photon b at the angle $\theta$, $\vec p_b = (E_b\cos\theta, E_b\sin\theta, 0)$ (its length is $E_b$). `mu_sq` is $\mu^2 = (E_a + E_b)^2 - |\vec p_a + \vec p_b|^2$ (`.dot` is the dot product). The first check confirms $\mu^2 = 2E_aE_b(1 - \cos\theta)$, the proof of Proposition 3; the second the two special cases: head on ($\theta = \pi$, 180 degrees) $\mu^2 = 4E_aE_b$, and in the same direction ($\theta = 0$) $\mu^2 = 0$.

```python
grid = np.linspace(0.05, 6.0, 300)
EA, EB = np.meshgrid(grid, grid)
fig, ax = plt.subplots(figsize=(6.4, 5.4))
for degrees, colour in ((180, "tab:blue"), (90, "tab:orange"), (45, "tab:red")):
    bound = 2.0 / (1 - np.cos(np.radians(degrees)))  # E_a E_b >= bound (m = 1)
    ax.contourf(EA, EB, (EA * EB >= bound).astype(float), levels=[0.5, 1.5],
                colors=[colour], alpha=0.12)
    ax.contour(EA, EB, EA * EB, levels=[bound], colors=[colour])
    ax.plot([], [], color=colour,
            label=f"$\\theta = {degrees}$ deg: $E_aE_b \\geq {bound:.2f}m^2$")
ax.set_xlabel("energy of photon a, $E_a/m$")
ax.set_ylabel("energy of photon b, $E_b/m$")
ax.set_title("Two photons: allowed above each curve")
ax.legend(fontsize=8, loc="upper right")
```

A grid of 300 by 300 energy pairs from 0.05 to 6 (`np.meshgrid` makes the two tables `EA` and `EB` of all combinations). For three angles, 180, 90 and 45 degrees (`np.radians` turns degrees into radians), `bound` is $2/(1 - \cos\theta)$, the threshold of $E_aE_b$ with $m = 1$. `contourf` shades, in the colour of the angle, the region where $E_aE_b \ge$ `bound` (the comparison gives `True` or `False`, `.astype(float)` turns it into 1 or 0, and the level band from 0.5 to 1.5 selects the ones); `contour` draws its boundary curve $E_aE_b = $ `bound`. `ax.plot([], [], ...)` draws nothing but adds an entry with the colour and the bound (two decimals) to the legend. Labels, title and legend follow.

```python
save_figure(fig, "two_photon_regions",
            "Two photons of energies $E_a$ and $E_b$ (horizontal and vertical, "
...
            "direction can never make a pair.")
```

**What figure 4 shows.** Horizontal axis: the energy of photon a; vertical axis: the energy of photon b; both in units $m$. Above each curve the pair is allowed: for head-on photons above $E_aE_b = m^2$ (blue), for 90 degrees above $2m^2$ (orange), for 45 degrees above about $6.83m^2$ (red). The student should see that the smaller the angle between the photons, the more energy is needed, and that photons moving in the same direction can never make a pair.

**In [9], what the record says about universes.**

```python
theory = json.loads(repository_file("Revision/pairing/pairing-theory.json")
                    .read_text(encoding="utf-8"))
missing = theory["not_established"]  # the record's list
say(f"the record lists {len(missing)} things the pairing theorems do not establish;")
for item in missing[:3]:
    say("- " + item.split(":")[0] + ": " + item.split(":")[1].split(";")[0].strip())
```

The record `pairing-theory.json` is read, and its list `not_established` is taken (`missing`). The first line prints how many items the list has; the loop prints the first three items shortened: `item.split(":")[0]` is the text before the first colon (the item's title), and `item.split(":")[1].split(";")[0].strip()` the text after it up to the first semicolon, without blanks at the ends. Output: the record lists 9 things the pairing theorems do not establish, followed by the three items No creation process, No rate and no amplitude, and No dynamical necessity, each with its first clause.

```python
starts = [item.split(":")[0] for item in missing]
check({"No creation process", "No rate and no amplitude",
       "No dynamical necessity"} <= set(starts),
      "the record states: no creation process, no rate or amplitude, no necessity")
```

`starts` is the list of the titles of all nine items. `set(starts)` makes a set of them, and `a <= b` for two sets is true when every element of `a` is in `b`. The check requires the three titles to be in the record's list.

```python
u1 = json.loads(repository_file(
    "Revision/lead_checks/reports/charge-conjugation-and-u1.json")
    .read_text(encoding="utf-8"))
verdicts = {entry["name"]: entry["verdict"] for entry in u1["checks"]}
check(verdicts.get("u1_noether_matrix_identity") == "PASS",
      "the record proves the U(1) charge conservation of one universe",
      record="Revision/lead_checks/reports/charge-conjugation-and-u1.json, check "
             "u1_noether_matrix_identity")
```

The lead's report on charge conjugation and the U(1) charge is read, `verdicts` maps each check name to its verdict (`.get(name)` returns `None` if the name is absent), and the check requires `u1_noether_matrix_identity` to have the verdict PASS: the record's proof that the charge of one universe is conserved on shell. Output: two PASS lines, the second with the line naming the record.

**In [10], the last check.**

```python
figure_names = ["invariant_mass_inequality", "nucleus_threshold",
                "allowed_photon_energies", "two_photon_regions"]
paths = [output_file(f"{FIGURE_FOLDER}/20c_{k}_{name}.png")
         for k, name in enumerate(figure_names, 1)]
check(all(path.is_file() for path in paths),
      "every figure file of this notebook exists")
all_checks_passed()
```

As in Notebook 20a, In [19]: the four figure files must exist, and `all_checks_passed()` prints the last line. Output: PASS every figure file of this notebook exists, and ALL 12 CHECKS PASSED (notebook 20c).

### 20.22 What the conservation laws of this theory allow and forbid

Section 20.17 answered question Q1 (allowed?) for light from conservation laws alone. This section does the same for universes, with the conservation laws that the Revision record proves.

**When a conservation law forbids.** A **conserved quantity** is a number computed from the state of a system that does not change in time for every solution. It forbids a transition from a state A to a state B exactly when its values in A and in B differ. A system may have several conserved quantities, and each forbids on its own: the conservation laws allow a transition only when EVERY conserved quantity has the same value in A and in B. The **empty state** of the classical theory is the configuration in which every field is zero everywhere; all its bilinears, and hence all its conserved quantities, are zero.

**(a) The charge of one universe is conserved.** The Lagrangian of Section 20.5 does not change when the field is multiplied by a constant phase, $\Psi \to e^{i\alpha}\Psi$ with a real number $\alpha$: then $\Psi^\dagger \to e^{-i\alpha}\Psi^\dagger$, so $\bar\Psi \to e^{-i\alpha}\bar\Psi$; every term of $\mathcal{L}$ contains as many factors $\bar\Psi$ as factors $\Psi$ (one of each in $K$ and in $mS$, two of each in $\frac{\lambda}{2}S^2$; the constant phase comes out of every derivative), so the phases cancel in pairs. Such a symmetry is called a **U(1) symmetry**, and by Noether's theorem it has a conserved current, here $J^\mu = -i\bar\Psi\gamma^\mu\Psi$ (Chapter 21 derives it). The record proves the conservation law directly, for both statistics and in the author's metric: the divergence $\partial_\mu(\sqrt{|g|}\,J^\mu)$ equals, for every configuration, $\sqrt{|g|}$ times a sum of two bilinears, each of which contains the left side $E$ of the field equation or the left side $\bar E$ of its adjoint; so on shell ($E = 0$, $\bar E = 0$)

$$
\partial_\mu\big(\cos z\,J^\mu\big) = 0 .
$$

The records of this law:

| field | report | check |
| --- | --- | --- |
| dirac16complex (Grassmann) | `wolfram-field-theory.json` | `current_conservation_identity_G` |
| dirac16complex00 (commuting) | `wolfram-field-theory.json` | `current_conservation_identity_C` |
| dirac16complex (Grassmann) | `python-field-theory.json` | `grassmann_current_conservation` |
| dirac16complex00 (commuting) | `python-field-theory.json` | `commuting_current_conservation` |
| both, reduced to a $16 \times 16$ matrix identity | `charge-conjugation-and-u1.json` | `u1_noether_matrix_identity` |

From it the charge $Q = \int\cos z\,J^{x_4}\,d^7x$ is constant in time, line by line:

1. Write the sum over $\mu$ as the $x_4$ term plus the seven others: $\partial_4(\cos z\,J^{x_4}) = -\sum_{i \neq 4}\partial_i(\cos z\,J^{x_i})$.
2. Integrate both sides over the seven coordinates other than $x_4$, on a slice $x_4 = \text{const}$; on the left the derivative with respect to $x_4$ may be taken out of the integral over the other coordinates: $\frac{dQ}{dx_4} = -\sum_{i \neq 4}\int\partial_i(\cos z\,J^{x_i})\,d^7x$.
3. Each term on the right is, by the fundamental theorem of calculus in the variable $x_i$, the difference of the values of $\cos z\,J^{x_i}$ at the two ends of the range of $x_i$, integrated over the six remaining coordinates.
4. ASSUMED: these **boundary terms** vanish. This is so, for example, when each of the coordinates $x_1, x_2, x_3, x_5, x_6, x_7$ is periodic, so that its two ends are the same place, and when no current flows through the two ends of the hidden direction. Then $dQ/dx_4 = 0$.

Status: the local law is PROVED (records above); the conservation of the integrated charge holds under the ASSUMED boundary conditions of line 4. So no net charge can be generated inside one universe.

**(b) Two universes do not interact.** A T1 pair consists of two fields: $\Psi_+$ of the theory $(m, \lambda)$ and $\Psi_-$ of the theory $(-m, -\lambda)$. Their joint Lagrangian is the sum $\mathcal{L}_{m,\lambda}[\Psi_+] + \mathcal{L}_{-m,-\lambda}[\Psi_-]$: no term of any Lagrangian of the Revision record contains both fields. The field equation of $\Psi_+$ is obtained by varying $\Psi_+$ alone; the second term does not contain $\Psi_+$ and contributes nothing, so $\Psi_+$ obeys the equation of a single universe whatever $\Psi_-$ does, and the same holds for $\Psi_-$. Applying (a) to each field separately: the charge $Q_+$ of $\Psi_+$ and the charge $Q_-$ of $\Psi_-$ are EACH conserved, not only their sum.

**(c) What the separate conservation forbids.** Line by line:

1. Suppose that at some time $x_4 = t_0$ both fields are zero everywhere (the empty state).
2. Then $J^{x_4}_+ = 0$ everywhere at $t_0$, so $Q_+(t_0) = 0$.
3. By (b), $Q_+$ is conserved, so $Q_+(x_4) = 0$ at every time.
4. The members of a T1 pair have opposite charges, $Q_- = -Q_+$ (T1c).
5. Hence a T1 pair whose members carry the charges $Q$ and $-Q$ with $Q \neq 0$ cannot evolve out of zero fields in the theory as built.

The zero TOTAL charge of a T1 pair does not make its appearance allowed, because the separate charges are conserved too. Example: the universe of Section 20.12 has the constant charge density $J^{x_4} = -3$ and $\cos z > 0$ on the patch, so its charge over any region of the patch is negative, not zero; neither it nor its T1 pair can evolve out of zero fields. Status: derived here in five lines from the PROVED conservation law (a), with the ASSUMED boundary conditions of (a); it is a consequence of the record's identity, not a record of its own (Notebook 20c, section 9, states it in the same words).

**(d) The energy of a universe is not conserved in the deflating metric.** The metric depends on the time $x_4$ through $a_4$, so the energy of one universe is not a conserved quantity. The local law $\nabla_\mu T^\mu{}_\nu = 0$ holds on shell (Chapter 9; `python-field-theory.json`, check `commuting_emt_conservation_on_shell`), and for a homogeneous diagonal source its $x_4$ component reads $-d\rho/dx_4 - 3a_4'(p_3 - p_t) = 0$ (`emt-divergence-and-spin-connection.json`, check `divergence_x4_component`). Adding $d\rho/dx_4$ to both sides,

$$
\frac{d\rho}{dx_4} = -3a_4'\,(p_3 - p_t) :
$$

the energy density changes whenever the pressure of 3-space and that of the extra times differ, and energy is exchanged between the inflating 3-space and the deflating extra times. (For the universe of Section 20.12 $p_3 = p_t$, and its $\rho$ is constant.) So the energy is not conserved.

**(d') The momenta of a universe are conserved.** The metric does not depend on the six coordinates $x_1, x_2, x_3, x_5, x_6, x_7$: shifting one of them by a constant, $x_i \to x_i + c$, leaves every metric component unchanged. Such a change of coordinates that leaves the metric unchanged is a **symmetry of the metric** (an **isometry**). For each of these six directions the $x_i$ component of the local law gives a conserved **momentum**, line by line:

1. The divergence of a tensor $T^\mu{}_\nu$ is $\nabla_\mu T^\mu{}_\nu = \partial_\mu T^\mu{}_\nu + \Gamma^\mu{}_{\mu\lambda}T^\lambda{}_\nu - \Gamma^\lambda{}_{\mu\nu}T^\mu{}_\lambda$, with the Christoffel symbols $\Gamma^\lambda{}_{\mu\nu} = \frac12g^{\lambda\sigma}(\partial_\mu g_{\sigma\nu} + \partial_\nu g_{\sigma\mu} - \partial_\sigma g_{\mu\nu})$ of Chapter 3 (they are not the chirality matrix): the covariant derivative of Chapter 3 adds one Christoffel term for the upper index and subtracts one for the lower index.
2. For the diagonal metric of this book the contracted symbol is $\Gamma^\mu{}_{\mu\lambda} = \frac12\sum_\mu\partial_\lambda g_{\mu\mu}/g_{\mu\mu}$ (in the definition with $\lambda$ and $\mu$ contracted, the first and third terms cancel), which is $\partial_\lambda\ln\sqrt{|g|}$, because $|g|$ is the absolute value of the product of the eight $g_{\mu\mu}$ and the logarithm of a product is the sum of the logarithms. So the first two terms of line 1 together are $\frac{1}{\sqrt{|g|}}\partial_\mu(\sqrt{|g|}\,T^\mu{}_\nu)$ (the product rule, read backwards).
3. In the last term, lowering the index gives $\Gamma^\lambda{}_{\mu\nu}T^\mu{}_\lambda = T^{\mu\sigma}\,\tfrac12(\partial_\mu g_{\sigma\nu} + \partial_\nu g_{\sigma\mu} - \partial_\sigma g_{\mu\nu})$. The tensor is symmetric, $T^{\mu\sigma} = T^{\sigma\mu}$ (`python-field-theory.json`, checks `commuting_emt_symmetric` and `grassmann_emt_symmetric`), so exchanging the names $\mu$ and $\sigma$ in the first term shows that it cancels the third; what remains is $\tfrac12T^{\mu\sigma}\partial_\nu g_{\sigma\mu}$.
4. For $\nu = x_i$ with $i$ one of $1, 2, 3, 5, 6, 7$ every $\partial_{x_i}g_{\sigma\mu}$ is zero. On shell the divergence vanishes, $\nabla_\mu T^\mu{}_\nu = 0$, so we are left with $\partial_\mu(\cos z\,T^\mu{}_{x_i}) = 0$, because $\sqrt{|g|} = \cos z$. The records of the on-shell law are the two checks `commuting_emt_conservation_on_shell` and `grassmann_emt_conservation_on_shell` of the report `python-field-theory.json`.
5. This has the form of the charge law of (a) with $J^\mu$ replaced by $T^\mu{}_{x_i}$, so the four lines of (a) give that $P_i = \int\cos z\,T^{x_4}{}_{x_i}\,d^7x$ is constant in time, with the same ASSUMED boundary conditions.

The same holds for the rotations of 3-space (in the planes of $x_1, x_2, x_3$, where the three metric components are equal) and for the rotations of the three extra times among themselves: they too leave the metric unchanged and give conserved quantities. Because the two universes do not couple (b), each of these is conserved SEPARATELY for each universe, exactly like the charges; and the T1 partner has $T' = -T$, so its momenta are $-P_i$. Like the charges, the separately conserved momenta therefore forbid a T1 pair whose members have nonzero momenta from appearing out of zero fields (the five lines of (c) with $Q$ replaced by $P_i$). Status: derived here from the PROVED local law and the PROVED symmetry of $T$, with the boundary terms ASSUMED to vanish. Energy is the one conserved number that the deflating metric removes: in this theory the charges and the momenta (and the rotation quantities) remain.

**(e) The totals of the two kinds of pair.** A T1 pair has $T + T' = 0$ and $Q_+ + Q_- = 0$: its totals are those of the empty state, so the conservation of the TOTALS does not forbid its appearance; (c) shows that the separate charges do, unless $Q_+ = 0$. A T2 pair has the total charge $2Q_+$ (the copy carries the SAME charge): already its total forbids its appearance from zero fields unless $Q_+ = 0$.

**(f) A classical condensate cannot grow out of zero.** The zero field solves every field equation of this book, because every term of the field equation contains $\Psi$. For a condensate the field equation is the ordinary differential equation $\Phi' = -\gamma^{(x_4)}(m + \lambda S - 3H\gamma^{(x_8)})\Phi$ (Section 20.12, step 1), whose right side is a polynomial in the real and imaginary parts of the 16 components that vanishes at $\Phi = 0$. The uniqueness theorem for ordinary differential equations with such a smooth right side (the theorem of Picard and Lindelöf, quoted without proof in Chapter 2) says that near every time only one solution has a given value at that time. The zero function is a solution with the value zero. So a condensate that is zero at one time $t_0$ is zero on a small interval around $t_0$. Suppose it were not zero at some later time $t_2$. Let $t^*$ be the least upper bound of the times $s$ (the smallest number that none of them exceeds) such that the condensate is zero at every time from $t_0$ to $s$. Because the solution is continuous, it is zero at $t^*$ itself, so $t^* \neq t_2$ and hence $t^* < t_2$; by the theorem, applied at $t^*$, it is zero on a small interval beyond $t^*$, which contradicts the choice of $t^*$. The same argument runs backwards in time. So the condensate is zero at every time. For the full field equation in 4+4 dimensions, whose initial-value problem is not well posed in the extra-time directions (Chapter 8), no such uniqueness theorem is proved in this book: OPEN.

**Summary of Q1 for universes.** The totals of a T1 pair are those of the empty state; the separate conservation of each member's charge and momenta, which holds because nothing couples the two universes, forbids the appearance of a T1 pair with charged members, or with members of nonzero momentum, out of zero fields; a T2 pair is forbidden already by its total charge unless it is neutral. Only an interaction between the two universes, which the theory does not contain, could leave the totals as the only conserved charges (OPEN). And even where the conservation laws allow something, that is not a creation (Section 20.17, lesson 1).

### 20.23 Pairs of universes, matter and antimatter

The request for this book also speaks of matter-antimatter mysteries. Chapter 21 teaches that subject from zero; this section states exactly what the pairing theorems contribute to it, and what they do not.

**Words.** **Matter** is what stars, planets and we are made of: protons, neutrons and electrons. Their **antiparticles** (antiprotons, antineutrons, positrons) have the same masses and opposite charges and make up **antimatter**. The **baryon number** counts protons and neutrons minus antiprotons and antineutrons. Observations show that the universe we see contains matter and almost no antimatter; Chapter 21 gives the observations and the numbers. To produce such an excess from a state without one, three conditions must hold, as Sakharov stated in 1967 (A. D. Sakharov, JETP Lett. 5, 24 (1967)): (1) some process violates the baryon number; (2) it violates the symmetries C (charge conjugation) and CP (charge conjugation combined with a reflection of space); (3) it happens out of thermal equilibrium.

**What is PROVED in this theory.**

1. The U(1) charge of one universe is conserved exactly (Section 20.22 (a)): no net charge of this kind can be generated inside one universe.
2. The pair-level statement: by (T1c) a T1 partner carries the OPPOSITE charge, $J^\mu[\Gamma\Psi] = -J^\mu[\Psi]$, so a T1 pair of universes of masses $+m$ and $-m$ has zero total charge; a T2 mirror copy carries the SAME charge (Section 20.6). Example: the universe of Section 20.12 has $J^{x_4} = -3$, its T1 partner $+3$, its mirror copy $-3$.
3. Charge conjugation is a MATRIX (rule of this book, from the lead's record `charge-conjugation-and-u1.json`, 12 checks, all PASS; Chapters 5 and 21 derive it step by step). The author's gammas are real, so for a REAL field plain complex conjugation is the identity and is NOT charge conjugation. Solving exactly for every matrix that maps solutions to solutions gives two charge-conjugation matrices: $\mathcal{C}_+ = C$, with $\mathcal{C}_+^{-1}\gamma^{(a)}\mathcal{C}_+ = -(\gamma^{(a)})^T$, which keeps the mass; and $\mathcal{C}_- = \Gamma C$, with $\mathcal{C}_-^{-1}\gamma^{(a)}\mathcal{C}_- = +(\gamma^{(a)})^T$, which reverses the mass (checks `charge_conjugation_matrix_plus` and `charge_conjugation_matrix_minus`). For real commuting fields the current vanishes identically and $\mathcal{C}_+$ acts as the identity; the nontrivial real matrix map is $\Gamma$ with $(m, \lambda) \to (-m, -\lambda)$, which reverses the current and the kinetic term: theorem T1 (check `real_fields_charge_conjugation`). For the quantised Grassmann field the conjugation that preserves the canonical anticommutator is $\Psi \to \Gamma\Psi^{\dagger T}$, and it reverses the mass (check `quantum_charge_conjugation_unitary_type`).

**The universe/anti-universe class of ideas.** That our universe might have a partner universe in which the roles of matter and antimatter are exchanged, so that the pair as a whole is neutral, is an old class of ideas. A published example of the class, built differently from anything in this book, is the CPT-symmetric universe of L. Boyle, K. Finn and N. Turok, Phys. Rev. Lett. 121, 251301 (2018); nothing in this chapter is taken from that work, and nothing in this chapter is attributed to it. Item 2 above shows that the T1 pairs of this theory have the bookkeeping of such a pair: opposite charges, zero total. Every scenario that would use this to explain the observed excess of matter in our universe is a HYPOTHESIS, and Section 20.22 (c) shows a first obstacle inside the theory as built: since each universe's charge is conserved on its own, a T1 pair with charged members cannot evolve out of zero fields; its charges can only be assumed as initial data.

**What the theory as built does NOT do.** It does NOT solve the matter-antimatter problem. Precisely:

- it contains no baryons (no protons, neutrons or other particles of the Standard Model of particle physics) and no baryon number;
- its only charge is the U(1) charge, which is exactly conserved, so it has no process that violates a baryon-like number (Sakharov's condition 1 fails);
- it contains no source of C or CP violation that would act in such a process, and none is computed (condition 2 is not addressed);
- no departure from thermal equilibrium of any baryon-number-violating process is computed (condition 3 is not addressed; the deflating history is time-dependent, but no rate is computed in it);
- no asymmetry, no number for it, and no comparison with observation is derived.

**What would be needed** (OPEN; every item a task, not a result): a charge that can play the role of the baryon number; an interaction that violates it; C and CP violation in that interaction; a departure from equilibrium along a computed history; a calculation of the resulting asymmetry and its comparison with observation; and, for the pair scenario, either an interaction between the universes that leaves only the total charge conserved or a theory of the initial data. Chapter 21 develops the conditions and the scorecard in detail.

### 20.24 What is not established

The following are NOT established by any equation of this book or of the Revision record. The items 1 to 9 are the record's own list (`pairing-theory.json`, key `not_established`; `PAIR_CREATION_PROOFS.md`, section 11.2), the others are added by this chapter.

1. **No creation process.** The theorems map solutions to solutions and quantities to quantities; nothing produces a universe, a pair of universes or a change of the number of universes; no initial state, vacuum decay or tunnelling process is derived.
2. **No rate and no amplitude.** No transition amplitude, probability, cross section, rate or Bogoliubov coefficient for creating universes of masses $\{+m, -m\}$ is computed or implied; no wave function of the universe and no path integral is part of the theorems.
3. **No dynamical necessity.** Nothing forces the partner to exist or to be realised; a single universe with mass $+m$ is an equally valid solution without its partner (Section 20.12 builds one).
4. **T1 is not a symmetry of one theory.** It changes the parameters and the sign of the action; for $\lambda \neq 0$ it pairs $(m, \lambda)$ with $(-m, -\lambda)$, not $+m$ with $-m$ at the same coupling. The pure pairing $(m, \lambda) \to (-m, \lambda)$ is T2, at EQUAL energy-momentum.
5. **The zero total holds for classical bilinears only.** The vanishing total energy-momentum and charge of a T1 pair holds for classical bilinears and as an operator identity within ONE quantum system; two independently quantised universes have generators that add without cancelling (statement Q3).
6. **Test fields.** The gravitational field is fixed and the same for both members; corollary C1 is the only statement about back-reaction, it concerns the sum of two classical sources in one geometry, and its part (a) depends on Einstein gravity (Einstein-Gauss-Bonnet gravity admits the deflating history as a vacuum, Section 20.7).
7. **The Z2 brane.** The mirror across $z = \pi/2$ uses the ASSUMED Z2 construction; the metric is degenerate there; no junction condition, brane tension or matching of the field across the brane is derived.
8. **Quantum positivity.** A positive-norm Fock space for either universe is not established by the pairing theorems.
9. **The Kohn-Sham level.** T3 holds for instantaneous mean-field Kohn-Sham states with the ASSUMED brane and the transformed tip condition; the time-dependent problem is OPEN, correlation is not included, and the Kohn-Sham history $a_4 = AHx_4$ is a PRESCRIBED BACKGROUND (the Kohn-Sham states violate the source conditions of the $a_4$ equations: `ks-source-conditions.json`, check `ks_profiles_violate_algebraic_condition`).
10. **No big bang in the equations.** For the PRESCRIBED deflating history $a_4 = AHx_4$ (and for any history whose $a_4$, $a_4'$ and $a_4''$ stay finite) the author's metric and its curvature are finite at every finite time on the patch (Section 20.3), and T1 holds at every time, so no moment is singled out. The history is prescribed, not computed; whether the coupled equations of the fields and of $a_4$ contain a big-bang moment is not decided (OPEN), and with a given source the $a_4$ equations of Einstein-Gauss-Bonnet gravity can break down at a finite time (Chapter 12; Section 20.3).
11. **No value of the mass.** $m$, $\lambda$, $H$ and $\kappa$ are free parameters; no relation between $H$ and $m$ is derived.
12. **No solution of the matter-antimatter problem** (Section 20.23).
13. **No uniqueness for the full 4+4 field equation.** Whether a classical field that vanishes at one time vanishes at all times is proved here only for condensates (Section 20.22 (f)).

### 20.25 What a calculation of creation would require

Questions Q2 and Q3 can be attacked in two ways. Both are OPEN; this section lists what each would need, so that a student can see where the missing work lies (Chapter 22 collects the open problems).

**The classical route (Q2).** One would need a solution of the coupled system, the field equations of both members together with the Einstein-Lovelock equations whose source is the total energy-momentum tensor, so that the metric is COMPUTED rather than prescribed, which starts without the pair and ends with it. Section 20.22 shows the obstacles: the separate conservation of the two charges forbids a charged pair from zero fields, and a condensate cannot grow out of zero at all. So a classical solution can at most describe how a pair that is already present evolves: the pair would have to be in the initial data (and then it is not created), or the solution would have to start at a singular moment with a rule for what emerges from it (and such a rule is an initial condition, not a derivation), or the equations would have to be changed.

**The quantum route (Q3).** By analogy with Section 20.17, one level up:

1. **A space of states with different numbers of universes**, containing a state with no universe and states with one universe or with a pair. In quantum cosmology the corresponding object is a wave function of the geometry together with the matter fields, which obeys the Wheeler-DeWitt equation (B. S. DeWitt, Phys. Rev. 160, 1113 (1967)); proposals of this kind include those of Hartle and Hawking (J. B. Hartle and S. W. Hawking, Phys. Rev. D 28, 2960 (1983)) and of Vilenkin (A. Vilenkin, Phys. Lett. B 117, 25 (1982)). Nothing of this kind exists in this book, which quantises only the matter field in a prescribed geometry (Chapter 10).
2. **A probability interpretation.** Probabilities need a positive inner product. The canonical state space of dirac16complex is a Krein space with an indefinite inner product, and a positive Fock space is known only in the good sector without extra-time momentum (Chapter 10).
3. **A dynamics that connects the states:** an interaction, or a time-dependent background, whose matrix element between the empty state and the pair state is not zero. Nothing in the theory couples two universes. For a pair whose members carry the charges $\pm Q$ with $Q \neq 0$, the interaction would also have to break the separate conservation of the two charges while keeping their sum (Section 20.22).
4. **The amplitude and what follows from it:** the amplitude $\langle\text{pair}|\,U\,|\text{empty}\rangle$ of the evolution operator $U$, the probability $|\langle\text{pair}|U|\text{empty}\rangle|^2$, and a rate.
5. **The stability question.** A theory with quanta of negative energy that interact with quanta of positive energy can make the empty state unstable, because pairs of zero total energy can then be produced without limit (J. M. Cline, S. Jeon and G. D. Moore, Phys. Rev. D 70, 043543 (2004)). A calculation of the creation of T1 pairs, whose members have opposite energies, would have to face this question.
6. **Numbers.** The mass $m$, the constant $H$, the gravitational coupling $\kappa$ and the coupling $\lambda$ would have to be fixed; the theory as built fixes none of them.

That a universe of zero total energy might appear without violating energy conservation was proposed long ago (E. P. Tryon, Nature 246, 396 (1973)); a zero total has never, by itself, produced a rate: that is always a separate calculation.

**The photon analogy, completed.**

| ingredient | photon on a nucleus | a T1 pair of universes |
| --- | --- | --- |
| the totals allow it? | yes, above the threshold (Proposition 2) | yes: all totals of the pair are zero |
| an interaction that lets energy or charge pass | light couples to the electron field | none: each universe's charge is conserved on its own, which forbids a charged pair from zero fields |
| dynamics connecting the initial and the final state | quantum electrodynamics | none in the theory |
| a computed probability | the Bethe-Heitler cross section (quoted) | none (OPEN) |

The first line is where the pairing theorems stand. The last three lines are the missing steps, and the second shows that a coupling between universes would be needed before any rate could be computed.

### 20.26 The answer to the question of the title

**Do universes come in pairs?** For each of the two fields, dirac16complex and dirac16complex00, the equations of this book PROVE: to every solution with mass $m$ the explicit map $\Gamma$ assigns a solution with mass $-m$ and coupling $-\lambda$, with the opposite energy-momentum tensor and charge, in every gravitational field (T1); the map $\gamma^{(x_8)}$ with the ASSUMED Z2 mirror assigns a solution with mass $-m$ and the same coupling, with the SAME energy-momentum and charge, in the author's primordial field (T2); for dirac16complex at the Kohn-Sham level the block map of $\Gamma$ with the transformed boundary conditions assigns to every self-consistent instantaneous state with $(m, \lambda)$ one with $(-m, +\lambda)$ at equal energies (T3); at the quantum level the T1 partner is the same quantum system relabelled, and two independently quantised universes have identical one-particle spectra (the $\lambda = 0$ spectra, in flat 4+4 space or in a general field at a point with frozen coefficients) and energies that add (Q); and a T1 pair as the only source of the author's metric is a zero source, which in Einstein gravity admits no solution for $H > 0$ (C1). These are exact maps between solution sets, with their stated hypotheses.

The equations do NOT prove that universes come in pairs: a single universe with mass $+m$ is an equally valid solution without its partner, and Section 20.12 builds one, exactly. They do NOT prove that any universe is created, in pairs or otherwise: they contain no creation process, no rate, no probability and no amplitude, and in the theory as built the separate conservation of each universe's charge forbids a charged T1 pair from appearing out of zero fields. They do NOT solve the matter-antimatter problem.

**Hypothesis P** ("the big bang creates universes of masses $+M$ and $-M$ in pairs") therefore remains what it was: a HYPOTHESIS. Sections 20.22 to 20.25 say precisely what a proof of it would still need.

### 20.27 What we proved, what we computed, what we assumed

| statement | status | where verified |
| --- | --- | --- |
| T1: $\mathcal{L}_{m,\lambda}[\Gamma\Psi] = -\mathcal{L}_{-m,-\lambda}[\Psi]$; solutions to solutions; $T \to -T$, $J \to -J$; the pair has zero total source and charge (classical bilinears; every gravitational field; both fields) | PROVED | `wolfram-pairing.json` (51 T1 checks), `python-pairing.json` (23 T1 checks); Section 20.5; Notebook 20a, In [7] and In [9]; Notebook 20b, In [7] |
| T2: $\gamma^{(n)}$ with a frame reflection of character $-1$: $(m, \lambda) \to (-m, \lambda)$, $\mathcal{L} \to +\mathcal{L}$; in the author's field the mirror copy has the pulled-back, EQUAL tensor and charge | PROVED; the Z2 construction ASSUMED | `wolfram-pairing.json` (28 T2 checks), `python-pairing.json` (16 T2 checks); Section 20.6; Notebook 20a, In [9] and In [11]; Notebook 20b, In [9] |
| Q: the T1 image carries $-B$ and is the same quantum system; independent universes do not cancel; equal one-particle spectra ($\lambda = 0$; flat 4+4 space, or a general field at a point with frozen coefficients); the T2 image keeps $+B$ | PROVED | `wolfram-pairing.json` (12 Q checks), `python-pairing.json` (10 Q checks); Section 20.6 |
| T3: Kohn-Sham states with $(m, \lambda, \theta)$ and $(-m, +\lambda, \pi - \theta)$ have equal levels, energies and energy-momentum profiles | PROVED; brane ASSUMED, tip transformed, instantaneous mean-field states | `wolfram-t3.json` (10 checks), `python-t3.json` (13 checks); Section 20.6; Chapter 19 |
| C1(a): a T1 pair as the only source; Einstein gravity has no real solution for $H > 0$; the only solutions are $a_4' = \pm iH$, $\Lambda = -18H^2$ | PROVED | `wolfram-a4-report.json`, check `einstein_no_vacuum_solution`; `python-a4-report.json`, check `einstein_no_vacuum`; `einstein-gauss-bonnet-a4.json`, check `no_vacuum_for_H_positive`; Section 20.7; Notebook 20a, In [12] |
| every source of the author's metric needs $\kappa(\rho + p_8) = -6(a_4'^2 + H^2)$ in Einstein gravity | PROVED | both a4 reports, check `einstein_null_energy_x8`; Notebook 20a, In [14] |
| C1(b): the linear member is a vacuum exactly when $V = 0$; with $\alpha_2H^2 = 1/48$ and $\Lambda = -12H^2$ the deflating history is a Gauss-Bonnet vacuum | PROVED | both a4 reports, checks `linear_member_vacuum_factor` and `einstein_gauss_bonnet_vacuum_linear`; exact check in Notebook 20a, In [16] |
| $\sum_\mu\gamma^\mu\Omega_\mu = -3H\gamma^{(x_8)}$ on the mirror patch | COMPUTED exactly (a result of this book, not a record) | Notebook 20a, In [5]; Notebook 20b, In [3] |
| the author's metric and its curvature are finite and non-degenerate at every finite time on the patch for the prescribed history $a_4 = AHx_4$ (and any history with finite $a_4$, $a_4'$, $a_4''$): no big-bang moment in the prescribed history | PROVED for the prescribed history; for computed histories OPEN (with a given source the $a_4$ equations can break down at a finite time, Chapter 12) | Section 20.3, from `python-pairing.json`, check `geometry.brane_degenerate`, and `python-a4-report.json`, check `riemann_entries_laurent` |
| the universe $m = 15$, $\lambda = -25/3$, $A = 1$, $\Lambda = -36H^2$: $S = 12/5$, $\rho = 12$, $p = -24$, $J^{x_4} = -3$, frequency $4H$, a complete solution without a partner | COMPUTED (exact for the field equation; Einstein equations to $10^{-10}$ at nine points); a result of this book | Section 20.12; Notebook 20b, In [4] to In [6] |
| its T1 partner solves its own equation with the same frequency but is the source of no member of the author's family in Einstein gravity | PROVED here by hand (record's null combination); checked numerically | Section 20.12, steps 6 and 7; Notebook 20b, In [7] |
| its T2 mirror copy solves the coupled equations on the mirror patch with equal $\rho$ and $J^{x_4}$ | PROVED here by hand; checked | Section 20.12, step 9; Notebook 20b, In [9] |
| the charge of one universe is conserved; a T1 pair with charged members cannot evolve out of zero fields | the local law PROVED; the consequence derived here; boundary terms ASSUMED to vanish | `charge-conjugation-and-u1.json`, check `u1_noether_matrix_identity`; both field-theory reports; Section 20.22 |
| $d\rho/dx_4 = -3a_4'(p_3 - p_t)$: the energy of one universe is not conserved | PROVED | `emt-divergence-and-spin-connection.json`, check `divergence_x4_component`; Section 20.22 (d) |
| the momenta $P_i = \int\cos z\,T^{x_4}{}_{x_i}\,d^7x$ ($i = 1, 2, 3, 5, 6, 7$) of each universe are conserved separately; a T1 pair whose members have nonzero momenta cannot evolve out of zero fields | derived here from the PROVED local law and the PROVED symmetry of $T$; boundary terms ASSUMED to vanish | `python-field-theory.json`, checks `commuting_emt_conservation_on_shell`, `grassmann_emt_conservation_on_shell`, `commuting_emt_symmetric` and `grassmann_emt_symmetric`; Section 20.22 (d') |
| a condensate that vanishes at one time vanishes always | PROVED here with the quoted uniqueness theorem for ODEs | Section 20.22 (f) |
| the threshold lemma; one photon makes no pair; $E_\gamma \ge 2m(1 + m/M)$; $E_aE_b \ge 2m^2/(1 - \cos\theta)$ | PROVED here from ASSUMED special relativity | Section 20.17; Notebook 20c, In [2] to In [8] |
| the rates of pair creation by light | quoted from the literature (Bethe-Heitler, Breit-Wheeler), not computed | Section 20.17 |
| a T1 pair has zero total charge; a T2 copy has the same charge | PROVED | (T1c) in Section 20.5 and the statement of T2 in Section 20.6 ($J' = R_8J$) |
| the two charge-conjugation matrices $\mathcal{C}_+ = C$ and $\mathcal{C}_- = \Gamma C$; for real fields the nontrivial real map is $\Gamma$ (T1) | PROVED | `charge-conjugation-and-u1.json` (12 checks); Chapters 5 and 21 |
| a partner universe explains the matter excess of our universe | HYPOTHESIS | Section 20.23 |
| the theory solves the matter-antimatter problem | NOT ESTABLISHED: no baryons, no baryon-number violation, no CP violation, no departure from equilibrium computed | Section 20.23 |
| a creation process, rate, probability or amplitude for universes | NOT ESTABLISHED (OPEN) | `pairing-theory.json`, key `not_established`; Sections 20.24 and 20.25 |
| Hypothesis P: "the big bang creates universes of masses $+M$ and $-M$ in pairs" | HYPOTHESIS | Sections 20.3 and 20.26 |
| Einstein gravity in the example; the sign convention $\sigma_T = +1$; the classical field dirac16complex00 in the examples; the units $H = \kappa = 1$; the Z2 brane and the mirror patch | ASSUMED | Sections 20.12 and 20.6 |
| the junction at the brane; the stability of the condensate; uniqueness for the full 4+4 field equation; a coupling between universes; whether the coupled equations of the fields and of $a_4$ contain a big-bang moment | OPEN | Sections 20.3, 20.12, 20.22 and 20.25 |

### 20.28 Exercises

**Exercise 20.1 (the chirality commutes with the generators).** Show, using only step 1 of Section 20.5 ($\Gamma\gamma^{(b)} = -\gamma^{(b)}\Gamma$ for every $b$), that $\Gamma S^{ab} = S^{ab}\Gamma$ for $a \neq b$, where $S^{ab} = \frac14(\gamma^{(a)}\gamma^{(b)} - \gamma^{(b)}\gamma^{(a)})$.

*Answer.* Take the first product: $\Gamma\gamma^{(a)}\gamma^{(b)} = -\gamma^{(a)}\Gamma\gamma^{(b)}$ (step 1 for the direction $a$) $= +\gamma^{(a)}\gamma^{(b)}\Gamma$ (step 1 for the direction $b$). In the same way $\Gamma\gamma^{(b)}\gamma^{(a)} = \gamma^{(b)}\gamma^{(a)}\Gamma$. Subtracting the second line from the first and multiplying by $\frac14$: $\Gamma S^{ab} = \frac14(\gamma^{(a)}\gamma^{(b)} - \gamma^{(b)}\gamma^{(a)})\Gamma = S^{ab}\Gamma$. The two signs $(-1)(-1) = +1$ are the reason: $S^{ab}$ contains two gammas.

**Exercise 20.2 (a time-like reflection gives a T1-type map).** In Section 20.6 the reflection of a space-like direction $n$ gave $S' = -\eta_{nn}S$ and $K' = \eta_{nn}K$. Take the time direction $n = x_4$ ($\eta_{nn} = -1$) and compute $\mathcal{L}_{m,\lambda}[\gamma^{(x_4)}\Psi; R_4e]$ in terms of $\mathcal{L}$ of $\Psi$.

*Answer.* With $\eta_{nn} = -1$: $S' = -(-1)S = S$ and $K' = (-1)K = -K$. Insert into the Lagrangian: $\mathcal{L}_{m,\lambda}[\Psi'; e'] = \sqrt{|g|}\,[K' - mS' - \frac{\lambda}{2}S'^2] = \sqrt{|g|}\,[-K - mS - \frac{\lambda}{2}S^2]$. Take out $-1$ and write $m = -(-m)$, $\lambda = -(-\lambda)$: $= -\sqrt{|g|}\,[K - (-m)S - \frac{(-\lambda)}{2}S^2] = -\mathcal{L}_{-m,-\lambda}[\Psi; e]$. This is a T1-type map, $(m, \lambda) \to (-m, -\lambda)$ with $\mathcal{L} \to -\mathcal{L}$, as the table of the eight reflections in `PAIR_CREATION_PROOFS.md` (section 5.5) records for $x_4, x_5, x_6, x_7$.

**Exercise 20.3 (another universe and its partner).** Repeat steps 4 and 7 of Section 20.12 with $A = 1$, $\Lambda = -30H^2$ and $M = -5H$ (units $H = \kappa = 1$). Find $S$, $m$, $\lambda$, $\rho$, $p$ and the equation of state $p/\rho$, and decide whether the T1 partner can be the source of the author's metric.

*Answer.* First condition: $MS = -12$, so $S = 12/5$ (as before; it does not involve $\Lambda$). Second: $mS = -(36 + 2(-30)) = -(36 - 60) = 24$, so $m = 24 \cdot 5/12 = 10$. Then $\lambda = (M - m)/S = (-5 - 10) \cdot 5/12 = -75/12 = -25/4$. $\rho = mS + \frac{\lambda}{2}S^2 = 24 + (-\frac{25}{8})\cdot\frac{144}{25} = 24 - 18 = 6$, and $p = \frac{\lambda}{2}S^2 = -18$, so $p/\rho = -3$. (These are the numbers of the third example of Chapter 12.) Check: $\rho + p = -12 = MS$ and $\rho - p = 24 = mS$. The partner has $\rho' = -6$, $p' = 18$, so $\kappa(\rho' + p_8') = -6 + 18 = +12 > -6$: it meets the requirement $-6(a_4'^2 + 1)$ at no real rate, and it cannot be the source of any member of the author's family in Einstein gravity. (The partner's null combination is minus the universe's, $-(\rho + p) = -MS = +12$, whatever $\Lambda$ is: the result does not depend on the choice of $\Lambda$.)

**Exercise 20.4 (a Gauss-Bonnet vacuum with a faster deflation).** In Einstein-Gauss-Bonnet gravity ($\alpha_1 = 1$, $\alpha_3 = 0$), find the coupling $\alpha_2H^2$ for which the linear member with $A = 2$ (3-space grows like $e^{2Hx_4}$, the extra times shrink like $e^{-2Hx_4}$) is a vacuum, and the cosmological constant it needs.

*Answer.* From Section 20.7, $V = 1 - 8\alpha_2H^2(A^2 + 5) = 1 - 8\alpha_2H^2 \cdot 9 = 1 - 72\alpha_2H^2$, which vanishes for $\alpha_2H^2 = 1/72$; this lies in the allowed range $0 < \alpha_2H^2 \le 1/40$. The cosmological constant is $\Lambda = -(E_{(1)}{}^{x_4}{}_{x_4} + \alpha_2E_{(2)}{}^{x_4}{}_{x_4})$. At $a_4' = 2H$: $E_{(1)}{}^{x_4}{}_{x_4} = 3a_4'^2 + 21H^2 = 12H^2 + 21H^2 = 33H^2$, and $E_{(2)}{}^{x_4}{}_{x_4} = -(36A^4 + 120A^2 + 420)H^4 = -(576 + 480 + 420)H^4 = -1476H^4$ (Section 20.7). So $\Lambda = -(33H^2 - 1476H^2/72) = -(33 - 20.5)H^2 = -12.5H^2 = -\frac{25}{2}H^2$. Check with the curve printed by Notebook 20a, In [16], $\Lambda = 720\alpha_2H^4 - 36H^2 + 3/(16\alpha_2)$: with $\alpha_2 = 1/(72H^2)$ this is $10H^2 - 36H^2 + 13.5H^2 = -12.5H^2$.

**Exercise 20.5 (a threshold with an exact final state).** A photon hits a nucleus of mass $M = 2m$ at rest and makes an electron-positron pair. Find the threshold energy and the momenta and energies of the three final bodies at the threshold, and check that the totals are conserved.

*Answer.* $E_\gamma = 2m(1 + m/M) = 2m(1 + 1/2) = 3m$. The initial totals: $|\vec p_{\mathrm{tot}}| = 3m$, $E_{\mathrm{tot}} = 3m + 2m = 5m$, so $\mu^2 = 25m^2 - 9m^2 = 16m^2$ and $\mu = 4m = m + m + 2m$, the sum of the final masses, as at a threshold. Each body carries the share $\mu_i/\mu$ of the momentum: the electron and the positron $(1/4)(3m) = 3m/4$ each, with the energy $\sqrt{m^2 + 9m^2/16} = 5m/4$ each; the nucleus $(2/4)(3m) = 3m/2$, with the energy $\sqrt{4m^2 + 9m^2/4} = 5m/2$. Totals: momenta $3m/4 + 3m/4 + 3m/2 = 3m$, energies $5m/4 + 5m/4 + 5m/2 = 5m$, the initial ones. All three move with the velocity $(3m/4)/(5m/4) = (3m/2)/(5m/2) = 3/5$, the equality case of the lemma.

**Exercise 20.6 (two photons at a right angle).** One photon has the energy $E_a = 4m$. What is the smallest energy of a second photon that meets it at 90 degrees and can make an electron-positron pair with it? And if the second photon moves head on?

*Answer.* At $\theta = 90$ degrees, $\cos\theta = 0$, and Proposition 3 needs $E_aE_b \ge 2m^2$, so $E_b \ge 2m^2/(4m) = m/2$. Head on, $\cos\theta = -1$, and the condition is $E_aE_b \ge 2m^2/2 = m^2$, so $E_b \ge m/4$.

**Exercise 20.7 (the charge density of the partner).** Using $J^\mu = -i\bar\Psi\gamma^\mu\Psi$, $\bar\Psi = \Psi^\dagger C$ and $\gamma^{x_4} = \gamma^{(x_4)}$, show that $J^{x_4} = \Psi^\dagger B\Psi$ with $B = -iC\gamma^{(x_4)}$, and that $J^{x_4}[\Gamma\Psi] = -J^{x_4}[\Psi]$. Then explain in two sentences why the zero total charge of a T1 pair does not allow it to appear out of zero fields.

*Answer.* $J^{x_4} = -i\Psi^\dagger C\gamma^{(x_4)}\Psi = \Psi^\dagger(-iC\gamma^{(x_4)})\Psi = \Psi^\dagger B\Psi$, by inserting the definitions and moving the number $-i$ next to the matrices. For the partner, $(\Gamma\Psi)^\dagger B(\Gamma\Psi) = \Psi^\dagger\Gamma B\Gamma\Psi$ because $\Gamma^\dagger = \Gamma$, and $\Gamma B\Gamma = -i\,\Gamma C\gamma^{(x_4)}\Gamma = -i\,C\,\Gamma\gamma^{(x_4)}\Gamma = -i\,C(-\gamma^{(x_4)}) = -B$ (step 2, $\Gamma C = C\Gamma$, then step 1 of Section 20.5); so $J^{x_4}[\Gamma\Psi] = -\Psi^\dagger B\Psi = -J^{x_4}[\Psi]$. The two universes of the pair are two different fields with no coupling, so the charge of each is conserved on its own (Section 20.22 (b)); starting from zero fields each charge stays zero, so a pair whose members carry the charges $Q$ and $-Q$ with $Q \neq 0$ can never be reached, although the total is zero.
