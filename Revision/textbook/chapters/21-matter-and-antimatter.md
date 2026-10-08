## 21. Matter and antimatter from zero: what this theory explains and what it does not

The world we see is made of matter, and almost no antimatter. Why that is so is one of the open questions of physics. This chapter explains the question from zero, with the observations, the three conditions that Andrei Sakharov found for any answer, and small worked models of each condition. Then it asks, condition by condition, what the theory of this book says. On the way it derives, line by line, the facts of the theory that matter for the question: that charge conjugation in this theory is made by a **matrix** (there are exactly two such matrices), that the charge of the field is **exactly conserved** in the author's metric while the three extra times deflate, how the **quantised** field can be conjugated, and what a pair of solutions of masses $+m$ and $-m$ carries. The chapter ends with a scorecard and with a precise list of what the theory as built does not do.

### 21.1 What this chapter does, and the answer first

The request that this book answers ends with the words "this theory solves matter anti-matter mysteries". The honest answer comes first, because every later section supports it.

**The answer.** The theory as built does **not** solve the matter-antimatter problem. The reasons, each of which this chapter proves or documents:

- The theory contains no baryons (no protons, neutrons or quarks), so it cannot say anything about the baryon number of the observed universe.
- The only number of the theory that could play the role of "matter minus antimatter" is the **U(1) charge** $Q$ of its field. It is **exactly conserved**: in the author's metric, for every history $a_4(x_4)$, in particular the one in which ordinary space inflates and the three extra times $x_5, x_6, x_7$ deflate exponentially, no solution can change its charge unless charge flows through the boundary (PROVED, Sections 21.16 to 21.18). So no process described by these equations can make a net charge inside one universe: Sakharov's first condition fails.
- For the commuting field dirac16complex00 the same-mass charge conjugation is an exact symmetry that reverses the charge (PROVED, Sections 21.10 and 21.31), so Sakharov's second condition fails for it as well (PROVED, Section 21.31). For the quantised field dirac16complex no violation of C or CP in reaction rates is built into the theory or computed (NOT COMPUTED). No departure from thermal equilibrium is computed (NOT COMPUTED); the Kohn-Sham history of this book is a prescribed background (Section 21.31).

**What the theory does provide, exactly.**

- Charge conjugation is a matrix. The author's gamma matrices are real, so for a real field plain complex conjugation changes nothing at all. Solving exactly for every matrix that maps solutions to solutions gives exactly two, up to a factor: $\mathcal{C}_+ = C$, which keeps the mass, and $\mathcal{C}_- = \Gamma C$, which reverses it (PROVED, Sections 21.8 to 21.10; Notebook 21a).
- For a real field the current vanishes, $\mathcal{C}_+$ acts as the identity, and the only nontrivial real matrix map is $\Gamma$, which reverses the mass (PROVED, Section 21.10).
- For the quantised anticommuting field dirac16complex the only conjugation that keeps the canonical anticommutator is $\Psi \to \Gamma\Psi^{\dagger T}$, and it reverses the mass (PROVED, Sections 21.25 and 21.26; Notebook 21c).
- **Pair level.** The chirality partner $\Gamma\Psi$ of a solution with the parameters $(m, \lambda)$ is a solution with $(-m, -\lambda)$ and carries exactly the opposite current, so the pair has total charge zero as classical bilinears (PROVED, theorem T1 of the Revision record; Section 21.19; Notebook 21b). This is a **map between two sets of solutions**. It does not create anything: a single universe of mass $+m$ is an equally valid solution without its partner, and no creation process, rate or amplitude follows from these equations (Chapter 20). The idea that a universe and an anti-universe together carry zero charge belongs to a class of ideas in the literature; any scenario in which our universe is one member of such a pair is a HYPOTHESIS (Section 21.37).

**The plan.** Sections 21.3 to 21.6 explain the problem from zero: particles and antiparticles, the conserved numbers, the observed excess of matter, and Sakharov's three conditions, each derived in plain words with a small model. Section 21.7 sets out the theory of this book. Sections 21.8 to 21.15 derive the charge-conjugation matrices and place Notebook 21a, which solves for them exactly from the Revision gammas. Sections 21.16 to 21.23 derive the exact conservation of the charge and the pair-level bookkeeping, with Notebook 21b. Sections 21.24 to 21.30 treat the reflections, the chirality and the quantised field, with Notebook 21c. Sections 21.31 to 21.36 apply Sakharov's conditions to the theory and place Notebook 21d, which computes the toy models and draws the scorecard. Section 21.37 says what would be needed; Section 21.38 lists every statement with its status; Sections 21.39 and 21.40 hold the exercises and their answers.

**Labels.** As everywhere in this book: PROVED means exact, with the Revision verifier file and check name, or with a complete derivation given here and an exact check in a notebook; COMPUTED means numerical, with the cell that computes it and its accuracy; ASSUMED marks an input, a convention or a quoted fact of physics; HYPOTHESIS marks a claim that nothing in the Revision record derives; OPEN marks a question that has not been answered; NOT COMPUTED marks something that no computation of the record addresses.

### 21.2 The words and symbols of this chapter

Each word is defined in plain terms here; the later sections make the definitions precise with formulas.

- **Matter, antimatter.** In cosmology "matter" means the protons and neutrons of atoms, which carry almost all of their mass. **Antimatter** is made of antiparticles.
- **Antiparticle.** For every known particle there is a particle with the same mass and the opposite values of all its charges: the positron $e^+$ for the electron $e^-$, the antiproton $\bar p$ for the proton $p$. A bar over a letter marks an antiparticle.
- **Quark.** A constituent of protons and neutrons. The up quark $u$ has electric charge $+2/3$ and the down quark $d$ has $-1/3$, in units of the proton charge.
- **Baryon, baryon number** $\mathcal{B}$. A baryon is made of three quarks, for example the proton $p = uud$ and the neutron $n = udd$. Every quark has $\mathcal{B} = 1/3$ and every antiquark $-1/3$. (Notebook 21d writes the baryon number with the plain letter $B$; in this chapter's prose the calligraphic $\mathcal{B}$ is used, because the plain $B$ is the Krein matrix below.)
- **Meson.** A quark and an antiquark, such as the pions $\pi^+ = u\bar d$, $\pi^- = d\bar u$ and $\pi^0$; $\mathcal{B} = 0$.
- **Lepton number** $L$: $+1$ for the electron and its neutrino $\nu_e$, $-1$ for the positron and the antineutrino $\bar\nu_e$, $0$ for quarks and photons. It is not the Lagrangian $\mathcal{L}$.
- **Electric charge** $Q_{\mathrm{el}}$, in units of the proton charge. (Notebook 21d prints it as Q in its bookkeeping; in this chapter $Q$ alone is the U(1) charge of the field, defined in Section 21.7.)
- **Conserved number.** A number whose total before any process equals its total after it.
- **Baryon-to-photon ratio** $\eta_B$: the number of baryons minus antibaryons per photon of the microwave background (Section 21.4). The letter $\eta$ with two indices, $\eta_{ab}$ or $\eta^{ab}$, is the frame metric; $\eta(K)$ without a subscript is the efficiency of the rate model of Section 21.6.
- **C, P, T, CP.** Charge conjugation C exchanges particles and antiparticles; parity P reflects space; time reversal T reverses the time; CP is C followed by P. A theory **violates** C (or CP) when a process and its image do not happen at the same rate.
- **Thermal equilibrium, temperature** $T$, **chemical potential** $\mu$, **Fermi-Dirac occupation** $f$: Section 21.5. (The letter $T$ also names the energy-momentum tensor in Chapter 9; in this chapter it is a temperature or the name of time reversal.)
- **Rate** $K$: a number of events per unit time.
- **Coordinates** $x_1, \dots, x_8$, in the author's order: $x_1, x_2, x_3$ ordinary 3-space (inflating); $x_4$ the time; $x_5, x_6, x_7$ the three **extra times**, time-like, which **deflate exponentially**; $x_8$ the **hidden** space direction, with the angle $z = 6Hx_8$ between $0$ and $\pi/2$ (the **patch**). The end $z = \pi/2$ is called the **brane**.
- **Gamma matrices** $\gamma^{(x1)}, \dots, \gamma^{(x8)}$: the author's eight real $16 \times 16$ matrices; **charge matrix** $C$, **chirality** $\Gamma$, **Krein matrix** $B$, **generators** $S^{ab}$: Section 21.7.
- **Spinor field** $\Psi$: at every point a column of 16 numbers, the **components** $\Psi_1, \dots, \Psi_{16}$. **Commuting** components are ordinary complex numbers (the field dirac16complex00); **anticommuting** (Grassmann) components obey $\Psi_r\Psi_c = -\Psi_c\Psi_r$ (the field dirac16complex). In Sections 21.10 and 21.15 the number $\epsilon = +1$ or $-1$ marks the two cases; in Sections 21.5, 21.6 and 21.36 the same letter $\epsilon$ is the baryon number made per decay, as in Notebook 21d.
- **Complex conjugate** $z^\ast$, **transpose** $M^T$, **conjugate transpose** $M^\dagger = (M^\ast)^T$; **symmetric** $M^T = M$; **antisymmetric** $M^T = -M$; **Hermitian** $M^\dagger = M$. A matrix or column is **real** when all its entries are real.
- **Dirac adjoint** $\bar\Psi = \Psi^\dagger C$; **scalar** $S = \bar\Psi\Psi$; **current** $J^\mu = -i\bar\Psi\gamma^\mu\Psi$; **charge density** $J^{(x4)} = \Psi^\dagger B\Psi$; **charge** $Q = \int\cos z\,\Psi^\dagger B\Psi\,d^7x$ (Section 21.7).
- **Charge-conjugation matrix** $\mathcal{C}$: a constant matrix such that $\Psi^c = \mathcal{C}\bar\Psi^T$ solves the field equation of the same form whenever $\Psi$ does (Section 21.8). The two that exist are $\mathcal{C}_+$ and $\mathcal{C}_-$.
- **Majorana (reality) condition**: the requirement $\Psi^c = \Psi$.
- **Bilinear**: a number $\Psi^\dagger K\Psi = \sum_{r,c}\Psi_r^\ast K_{rc}\Psi_c$ with a fixed matrix $K$.
- **Noether's theorem**: a continuous symmetry of the Lagrangian gives a current whose divergence vanishes on every solution (Section 21.16).
- **Chirality partner**: $\Gamma\Psi$. **Theorem T1** of the Revision record: it solves the field equations with $(m, \lambda) \to (-m, -\lambda)$ and carries the opposite current (Section 21.19).
- **Canonical anticommutator, Krein form, Krein inertia, positive representation**: Section 21.25.
- **Majorana-type term**: a term $\Psi^TM\Psi$ built from $\Psi$ twice, without $\Psi^\dagger$ (Section 21.32).
- **Status labels**: PROVED, COMPUTED, ASSUMED, HYPOTHESIS, OPEN, NOT COMPUTED (Section 21.1).

### 21.3 Particles, antiparticles and conserved numbers

**Antiparticles.** In 1928 Dirac wrote down the equation of the electron. Its solutions come with negative as well as positive energies, and Dirac concluded that a particle with the mass of the electron and the opposite electric charge must exist. That particle, the positron, was found in cosmic rays in 1932 (C. D. Anderson, Phys. Rev. 43, 491 (1933)). Since then every known particle has been found to have an antiparticle with the same mass and opposite charges. A few neutral particles, such as the photon, are their own antiparticles.

**Annihilation and particle pair creation.** An electron and a positron that meet can annihilate into photons. Conversely, a photon of enough energy that passes near a nucleus (which takes up momentum) can turn into an electron and a positron. This is the **pair creation of particles**, an observed process of ordinary physics, in which the total electric charge stays the same because the two members carry opposite charges. It must not be confused with the question whether universes are created in pairs, which Chapter 20 treats and which no equation of this book answers.

**The conserved numbers.** Three numbers are counted in every process: the electric charge $Q_{\mathrm{el}}$, the baryon number $\mathcal{B}$ and the lepton number $L$ (Section 21.2). The values for a particle made of quarks follow from its quark content by addition, with an antiquark counted with the opposite sign. Line by line for the particles of the next example:

- proton $p = uud$: $\mathcal{B} = \tfrac13 + \tfrac13 + \tfrac13 = 1$ and $Q_{\mathrm{el}} = \tfrac23 + \tfrac23 - \tfrac13 = 1$ (add the numbers of the three quarks);
- neutron $n = udd$: $\mathcal{B} = 1$ and $Q_{\mathrm{el}} = \tfrac23 - \tfrac13 - \tfrac13 = 0$ (the same rule);
- antiproton $\bar p = \bar u\bar u\bar d$: $\mathcal{B} = -1$ and $Q_{\mathrm{el}} = -1$ (every sign reversed);
- pion $\pi^+ = u\bar d$: $\mathcal{B} = \tfrac13 - \tfrac13 = 0$ and $Q_{\mathrm{el}} = \tfrac23 - (-\tfrac13) = 1$ (the antiquark $\bar d$ counts with the opposite sign of $d$);
- pion $\pi^- = d\bar u$: $\mathcal{B} = 0$ and $Q_{\mathrm{el}} = -\tfrac13 - \tfrac23 = -1$;
- neutral pion $\pi^0$: $\mathcal{B} = 0$ and $Q_{\mathrm{el}} = 0$ (Notebook 21d writes it as $u\bar u$; the physical $\pi^0$ is a mixture of $u\bar u$ and $d\bar d$, which have the same numbers).

The electron has $(\mathcal{B}, L, Q_{\mathrm{el}}) = (0, 1, -1)$, the positron $(0, -1, 1)$, the antineutrino $(0, -1, 0)$ and the photon $(0, 0, 0)$.

**Worked example: bookkeeping.** A number is conserved in a process if its total before equals its total after. For four processes (the totals are sums over the particles on each side):

| process | $\mathcal{B}$ before, after | $L$ before, after | $Q_{\mathrm{el}}$ before, after | observed? |
| --- | --- | --- | --- | --- |
| neutron decay $n \to p\,e^-\bar\nu_e$ | 1, $1 + 0 + 0 = 1$ | 0, $0 + 1 - 1 = 0$ | 0, $1 - 1 + 0 = 0$ | yes |
| annihilation $p\,\bar p \to \pi^+\pi^-\pi^0$ | $1 - 1 = 0$, 0 | 0, 0 | $1 - 1 = 0$, $1 - 1 + 0 = 0$ | yes |
| pair creation $\gamma\,p \to p\,e^-e^+$ | 1, 1 | 0, $1 - 1 = 0$ | 1, $1 - 1 + 1 = 1$ | yes |
| proton decay $p \to e^+\pi^0$ | 1, 0 | 0, $-1$ | 1, $1 + 0 = 1$ | never seen |

The three observed processes conserve all three numbers. Proton decay would change $\mathcal{B}$ by $0 - 1 = -1$ and $L$ by $-1 - 0 = -1$; it would keep $Q_{\mathrm{el}}$ and the difference $\mathcal{B} - L$ (before $1 - 0 = 1$, after $0 - (-1) = 1$). It has been searched for and never observed. Notebook 21d computes this table with exact fractions (In [3]) and draws it (figure 21d.1).

**The matter-antimatter problem** is the question why the universe contains baryons but essentially no antibaryons.

### 21.4 What is observed: the baryon-to-photon ratio, and no antimatter domains

This section quotes observations. Nothing in it is computed by this book, and no notebook of this chapter uses a measured number; every number here is ASSUMED (quoted) from the literature named with it.

**The definition.** The universe is filled with the photons of the **cosmic microwave background**, the thermal radiation left over from the hot early universe, today at the temperature 2.7255 K (D. J. Fixsen, Astrophys. J. 707, 916 (2009)). After the first seconds of the universe the number of baryons and the number of these photons in a volume that expands with the universe both stay constant, so their ratio is a fixed number of our universe, the **baryon-to-photon ratio**

$$
\eta_B = \frac{n_b - n_{\bar b}}{n_\gamma} ,
$$

where $n_b$, $n_{\bar b}$ and $n_\gamma$ are the numbers of baryons, antibaryons and photons per unit volume. Today $n_{\bar b}$ is negligible.

**Its value.** It is measured in two independent ways. The pattern of hot and cold spots in the microwave background depends on the density of baryons; the Planck satellite's 2018 analysis gives the baryon density parameter $\Omega_bh^2 = 0.0224 \pm 0.0001$ (Planck Collaboration, "Planck 2018 results. VI. Cosmological parameters", Astron. Astrophys. 641, A6 (2020)). The abundances of the light nuclei made in the first minutes (big-bang nucleosynthesis) depend on $\eta_B$ as well, and the two determinations agree (R. H. Cyburt, B. D. Fields, K. A. Olive and T.-H. Yeh, Rev. Mod. Phys. 88, 015004 (2016)). Converted with the photon density of a black body at 2.7255 K and the mass of the proton (a standard conversion, quoted and not derived here), the Planck value corresponds to

$$
\eta_B \approx 6.1 \times 10^{-10} :
$$

about six baryons for every ten billion photons, or $1/\eta_B \approx 1.6 \times 10^9$ photons per baryon (the reciprocal of the quoted value, rounded).

**Why this is a problem.** Run the expansion backwards. When the thermal energy was far above the rest energy of a proton, baryons, antibaryons and photons were all abundant and turned into each other all the time. Had the early universe held exactly as many baryons as antibaryons, almost all of them would have annihilated as it cooled, leaving far less matter than we see (L. Canetti, M. Drewes and M. Shaposhnikov, New J. Phys. 14, 095012 (2012)). The baryons of today are the remnant of a tiny excess of baryons over antibaryons, about one part in $10^9$. One could put this excess into the initial state by hand; the standard view, reviewed in the article just cited, is that physical processes should **generate** it from a symmetric start. Explaining how is the matter-antimatter problem, also called **baryogenesis**.

**No antimatter domains.** Could the universe be symmetric as a whole, with some regions of matter and others of antimatter? Wherever such regions touch, particles and antiparticles annihilate and make gamma rays. Cohen, De Rujula and Glashow showed that the gamma rays from the boundaries would exceed the observed diffuse gamma-ray background unless our region of matter is essentially the whole visible universe (A. G. Cohen, A. De Rujula and S. L. Glashow, Astrophys. J. 495, 539 (1998)). A patchwork universe is therefore excluded.

| statement | status | source |
| --- | --- | --- |
| $\Omega_bh^2 = 0.0224 \pm 0.0001$ | ASSUMED (quoted observation) | Planck Collaboration, Astron. Astrophys. 641, A6 (2020) |
| $\eta_B \approx 6.1 \times 10^{-10}$, agreement with nucleosynthesis | ASSUMED (quoted) | the same; Cyburt et al., Rev. Mod. Phys. 88, 015004 (2016) |
| no domains of antimatter in the visible universe | ASSUMED (quoted) | Cohen, De Rujula and Glashow, Astrophys. J. 495, 539 (1998) |
| a value of $\eta_B$ from the theory of this book | NOT COMPUTED | nothing in the Revision record computes it |

### 21.5 Sakharov's three conditions, derived in plain words

In 1967 Andrei Sakharov named three ingredients that any process which makes the baryon excess from a symmetric start must contain (A. D. Sakharov, JETP Lett. 5, 24 (1967)). Each follows from a short argument. Throughout, the system is the whole universe; it starts with $\mathcal{B} = 0$ and without any asymmetry, and we ask what is needed for $\mathcal{B} \ne 0$ later. The arguments are general; the small models that illustrate them are ASSUMED toy models, not part of the theory of this book, and Notebook 21d computes each of them.

**Condition 1: the baryon number must change.**

*Proposition 1.* If every process conserves $\mathcal{B}$, then $\mathcal{B}(t) = \mathcal{B}(0)$ at every time $t$.

*Proof.* Conservation means $d\mathcal{B}/dt = 0$ at every time. A function of one variable whose derivative is zero everywhere on an interval is constant there (the mean value theorem of calculus: $\mathcal{B}(t) - \mathcal{B}(0) = t\,\mathcal{B}'(\tau)$ for some $\tau$ between $0$ and $t$, and $\mathcal{B}'(\tau) = 0$). $\square$

Starting from $\mathcal{B} = 0$, the universe would keep $\mathcal{B} = 0$ for ever. So some process must change $\mathcal{B}$.

**Condition 2: C and CP must be violated.** A transformation is a **symmetry of the dynamics** if it turns every possible history of the system into another possible history that runs in the same direction of time.

*Proposition 2.* Let $\mathcal{S}$ be a symmetry of the dynamics that reverses $\mathcal{B}$: if the history $h$ has the baryon number $\mathcal{B}[h](t)$ at the time $t$, its image $\mathcal{S}h$ has $-\mathcal{B}[h](t)$. Let the initial state be an ensemble, a list of possible starting configurations $c$ with probabilities $p(c)$, in which every configuration and its image are equally likely, $p(\mathcal{S}c) = p(c)$. Then the average baryon number is zero at every time.

*Proof,* line by line. Let $h_c$ be the history that starts from $c$.

$$
\langle\mathcal{B}(t)\rangle = \sum_c p(c)\,\mathcal{B}[h_c](t)
$$

(the definition of the average over the ensemble)

$$
= \sum_c p(\mathcal{S}c)\,\mathcal{B}[h_{\mathcal{S}c}](t)
$$

(the map $c \to \mathcal{S}c$ is one to one, so summing over all $c$ is the same as summing over all $\mathcal{S}c$)

$$
= \sum_c p(c)\,\mathcal{B}[\mathcal{S}h_c](t)
$$

(the probabilities are equal by assumption, and the history that starts from $\mathcal{S}c$ is $\mathcal{S}h_c$ because $\mathcal{S}$ is a symmetry of the dynamics)

$$
= \sum_c p(c)\,\big(-\mathcal{B}[h_c](t)\big) = -\langle\mathcal{B}(t)\rangle
$$

($\mathcal{S}$ reverses $\mathcal{B}$). A number equal to minus itself is zero. $\square$

Apply this with $\mathcal{S} = $ C: a start without asymmetry holds particles and antiparticles in equal numbers, so it is C-symmetric, and if C were a symmetry of the dynamics no average asymmetry could develop. Apply it with $\mathcal{S} = $ CP: a start that is the same in every direction is also symmetric under the reflection P, which does not change $\mathcal{B}$; so CP reverses $\mathcal{B}$ as well, and if CP were a symmetry no asymmetry could develop. Hence **both C and CP must be violated**.

**A decay model for conditions 1 and 2.** A heavy toy particle $X$ decays in two ways: with probability $r$ into a channel of baryon number $\mathcal{B}_1$, with probability $1 - r$ into a channel of baryon number $\mathcal{B}_2$. Its antiparticle $\bar X$ decays into the antichannels, of baryon numbers $-\mathcal{B}_1$ and $-\mathcal{B}_2$, with probabilities $\bar r$ and $1 - \bar r$. (In ordinary quantum field theory the total decay rates of $X$ and $\bar X$ are equal; the probabilities $r$ and $\bar r$ can differ only if C and CP are violated. This is quoted, ASSUMED.) Start with $N$ particles and $N$ antiparticles. Line by line:

$$
\text{one } X \text{ makes on average } r\mathcal{B}_1 + (1 - r)\mathcal{B}_2
$$

(each channel's baryon number times its probability, summed: the average of a quantity that takes two values);

$$
\text{one } \bar X \text{ makes on average } -\bar r\mathcal{B}_1 - (1 - \bar r)\mathcal{B}_2
$$

(the same rule with the antichannels);

$$
N\big[r\mathcal{B}_1 + (1 - r)\mathcal{B}_2 - \bar r\mathcal{B}_1 - (1 - \bar r)\mathcal{B}_2\big]
$$

(the total of $N$ particles and $N$ antiparticles is $N$ times the sum of the two averages);

$$
= N\big[(r - \bar r)\mathcal{B}_1 + (-r + \bar r)\mathcal{B}_2\big] = N\,(r - \bar r)(\mathcal{B}_1 - \mathcal{B}_2)
$$

(collect the terms with $\mathcal{B}_1$ and with $\mathcal{B}_2$: in the second, $\mathcal{B}_2 - r\mathcal{B}_2 - \mathcal{B}_2 + \bar r\mathcal{B}_2 = -(r - \bar r)\mathcal{B}_2$; then factor out $r - \bar r$). The net baryon number is a **product**. It vanishes if $\mathcal{B}_1 = \mathcal{B}_2$ (then $X$ carries a conserved baryon number: condition 1 fails) or if $r = \bar r$ (particle and antiparticle behave alike: condition 2 fails). Example: $X \to qq$ with $\mathcal{B}_1 = \tfrac23$ and $X \to \bar q\bar\ell$ (an antiquark and an antilepton) with $\mathcal{B}_2 = -\tfrac13$, and $r = 0.6$, $\bar r = 0.5$: per pair ($N = 1$) the net baryon number is $(0.6 - 0.5)(\tfrac23 + \tfrac13) = 0.1 \times 1 = \tfrac{1}{10}$ (Notebook 21d, In [5], exact; figure 21d.2 shows it for all $r$ and $\bar r$).

**Condition 3: a departure from thermal equilibrium.** In **thermal equilibrium** at temperature $T$, a system's reactions run forwards and backwards equally often, and each quantum state of energy $E$ holds a fermion with the **Fermi-Dirac** probability $f(E) = 1/(e^{(E - \mu)/T} + 1)$ (Boltzmann's constant set to 1). Here $\mu$, the **chemical potential**, belongs to a conserved number; it is quoted from statistical physics (ASSUMED) that the equilibrium state depends only on the energy and on the conserved numbers. A particle of baryon number $+1$ sees $+\mu$ and its antiparticle, which has the same mass and hence the same energy, sees $-\mu$:

$$
f_+ = \frac{1}{e^{(E - \mu)/T} + 1},\qquad f_- = \frac{1}{e^{(E + \mu)/T} + 1} .
$$

The surplus of particles per state, line by line:

$$
f_+ - f_- = \frac{\big(e^{(E + \mu)/T} + 1\big) - \big(e^{(E - \mu)/T} + 1\big)}{\big(e^{(E - \mu)/T} + 1\big)\big(e^{(E + \mu)/T} + 1\big)}
$$

(the two fractions brought to their common denominator, the product of the two denominators);

$$
= \frac{e^{(E + \mu)/T} - e^{(E - \mu)/T}}{e^{2E/T} + e^{(E - \mu)/T} + e^{(E + \mu)/T} + 1}
$$

(the two 1s of the numerator cancel; the denominator is multiplied out, with $e^{(E - \mu)/T}e^{(E + \mu)/T} = e^{2E/T}$ because exponents add);

$$
= \frac{e^{\mu/T} - e^{-\mu/T}}{e^{E/T} + e^{-\mu/T} + e^{\mu/T} + e^{-E/T}}
$$

(numerator and denominator divided by $e^{E/T}$, using $e^{u}/e^{v} = e^{u - v}$);

$$
= \frac{2\sinh(\mu/T)}{2\cosh(E/T) + 2\cosh(\mu/T)} = \frac{\sinh(\mu/T)}{\cosh(E/T) + \cosh(\mu/T)}
$$

(the definitions $\sinh u = (e^u - e^{-u})/2$ and $\cosh u = (e^u + e^{-u})/2$, then the factor 2 cancelled). If reactions that change $\mathcal{B}$ run back and forth in equilibrium, $\mathcal{B}$ is not a conserved number and has no chemical potential: $\mu = 0$, so $\sinh 0 = 0$ and $f_+ = f_-$ at **every** energy. No asymmetry. An asymmetry can only be made while the universe is **out of equilibrium**, for example in decays that happen too late for the inverse processes to keep up.

*Worked example.* For a state with $E = 2T$ and $\mu = 0$, both occupations are $1/(e^2 + 1) = 0.119203$. A chemical potential $\mu = 0.1T$ would give $f_+ = 1/(e^{1.9} + 1) = 0.130108$ and $f_- = 1/(e^{2.1} + 1) = 0.109097$, a surplus of $0.021012$ particles per state (Notebook 21d, In [7], where sympy also checks the formula exactly; figure 21d.3 draws the surplus against $E/T$).

### 21.6 Condition 3 in a rate model: decays out of equilibrium

How far from equilibrium must the decays be? A small ASSUMED model answers this in closed form. A toy universe cools; the time $t$ is measured in units of its cooling time. Let $n(t)$ be the number of heavy pairs $X$, $\bar X$ (in units of their starting number) and $n_{eq}(t) = e^{-t}$ the number that equilibrium would hold (heavy particles become rare as the temperature falls). Decays and inverse decays pull $n$ towards $n_{eq}$ at the rate $K$; every net decay of a pair makes $\epsilon$ baryons (the number of Section 21.5); inverse decays, which need $X$ particles in equilibrium, erase the asymmetry $a$ at the rate $Kn_{eq}$:

$$
\frac{dn}{dt} = -K(n - n_{eq}),\qquad \frac{da}{dt} = \epsilon K(n - n_{eq}) - Kn_{eq}\,a,\qquad n(0) = 1,\quad a(0) = 0 .
$$

**Solving it exactly**, line by line (for $K \ne 1$).

*Line 1.* Write $n = n_{eq} + \Delta$. Then $dn/dt = dn_{eq}/dt + d\Delta/dt = -e^{-t} + d\Delta/dt$ (the derivative of a sum, and $de^{-t}/dt = -e^{-t}$). The first equation says $dn/dt = -K\Delta$, so $d\Delta/dt = -K\Delta + e^{-t}$, with $\Delta(0) = n(0) - n_{eq}(0) = 1 - 1 = 0$.

*Line 2.* The function $\Delta(t) = (e^{-t} - e^{-Kt})/(K - 1)$ solves it. Check: its derivative is $(-e^{-t} + Ke^{-Kt})/(K - 1)$ (chain rule for each exponential), and $-K\Delta + e^{-t} = \big(-Ke^{-t} + Ke^{-Kt} + (K - 1)e^{-t}\big)/(K - 1) = (-e^{-t} + Ke^{-Kt})/(K - 1)$ (common denominator, then $-K + K - 1 = -1$): the two agree, and $\Delta(0) = (1 - 1)/(K - 1) = 0$.

*Line 3.* Let $W(t) = K(1 - e^{-t})$, so that $dW/dt = Ke^{-t} = Kn_{eq}$ and $W(0) = 0$. By the product rule, $d(a\,e^{W})/dt = (da/dt + Kn_{eq}\,a)\,e^{W}$, and the second equation turns this into $\epsilon K\Delta\,e^{W}$. Integrating from $0$ to $t$ (fundamental theorem of calculus, with $a(0) = 0$) gives $a(t)e^{W(t)} = \epsilon\int_0^tK\Delta(s)e^{W(s)}ds$, that is

$$
a(t) = \epsilon\int_0^t K\Delta(s)\,e^{W(s) - W(t)}\,ds .
$$

*Line 4.* As $t \to \infty$, $W(t) \to K$, and $W(s) - K = -Ke^{-s}$. The final asymmetry is $a(\infty) = \epsilon\,\eta(K)$ with the **efficiency**

$$
\eta(K) = \int_0^\infty K\Delta(s)\,e^{-Ke^{-s}}\,ds .
$$

*Line 5.* Substitute $y = e^{-s}$: then $ds = -dy/y$, the limits $s = 0$ and $s = \infty$ become $y = 1$ and $y = 0$, and $\Delta = (y - y^K)/(K - 1)$. Turning the limits round removes the minus sign:

$$
\eta(K) = \frac{K}{K - 1}\int_0^1 \frac{y - y^K}{y}\,e^{-Ky}\,dy = \frac{K}{K - 1}\int_0^1\big(1 - y^{K - 1}\big)e^{-Ky}\,dy .
$$

*Line 6.* The first part is $\int_0^1e^{-Ky}dy = (1 - e^{-K})/K$. In the second substitute $u = Ky$ ($dy = du/K$, limits $0$ and $K$): $\int_0^1y^{K - 1}e^{-Ky}dy = \int_0^K(u/K)^{K - 1}e^{-u}du/K = K^{-K}\gamma(K, K)$, where $\gamma(s, x) = \int_0^xu^{s - 1}e^{-u}du$ is the **lower incomplete gamma function**. Hence

$$
\eta(K) = \frac{K}{K - 1}\Big(\frac{1 - e^{-K}}{K} - K^{-K}\gamma(K, K)\Big) .
$$

**What it says.** For slow decays (small $K$) the decays happen late, when $n_{eq}$ is already tiny, so the erasing term $Kn_{eq}a$ is ineffective and almost the whole $\epsilon$ survives. For fast decays (large $K$) $n$ stays close to $n_{eq}$ and the inverse decays erase almost everything: $K^{-K}\gamma(K, K)$ and $e^{-K}$ are exponentially small, so $\eta(K) = 1/(K - 1)$ up to exponentially small terms. Two controls: with $\epsilon = 0$ (no C and CP violation) the second equation keeps $a = 0$ for ever; without the erasing term $da/dt = \epsilon K(n - n_{eq}) = -\epsilon\,dn/dt$, so $a(\infty) = \epsilon\big(n(0) - n(\infty)\big) = \epsilon$. Notebook 21d checks lines 1 to 3 with sympy, evaluates $\eta(K)$ with mpmath, integrates the two equations with the Runge-Kutta method of Chapter 2 and finds $\eta = 0.9955325865$, $0.4110164748$ and $0.0344827586$ for $K = 0.1$, $3$ and $30$, with the integration agreeing to $10^{-7}$ (In [9] and In [10]; figures 21d.4 and 21d.5). For $K = 30$ the value is $1/29$, the fast-decay limit.

| statement | status | where |
| --- | --- | --- |
| Propositions 1 and 2 (conditions 1 and 2) | PROVED (above) | Section 21.5 |
| decay model: net baryon number $N(r - \bar r)(\mathcal{B}_1 - \mathcal{B}_2)$; example $1/10$ | PROVED for the ASSUMED model; COMPUTED exactly | Notebook 21d, In [5] |
| equilibrium surplus $\sinh(\mu/T)/(\cosh(E/T) + \cosh(\mu/T))$; zero for $\mu = 0$ | PROVED (above; sympy) | Notebook 21d, In [7] |
| rate model: the closed form of $\eta(K)$ and its two limits | PROVED for the ASSUMED model; COMPUTED (RK4 to $10^{-7}$) | Notebook 21d, In [9] to In [12] |

### 21.7 The theory of this book: two fields, one phase symmetry

This section collects what the rest of the chapter needs. Every formula is from the Revision record; the chapters named derive them in full.

**The metric.** The author's metric is diagonal. With the abbreviations $s = \sin^{1/3}z$ and $z = 6Hx_8$, its entries in the order $x_1, \dots, x_8$ are

$$
g = \mathrm{diag}\big(e^{2a_4}s,\ e^{2a_4}s,\ e^{2a_4}s,\ -1,\ -e^{-2a_4}s,\ -e^{-2a_4}s,\ -e^{-2a_4}s,\ \cot^2z\big) .
$$

Its **scale factors** $f_a = \sqrt{|g_{aa}|}$ are $f_1 = f_2 = f_3 = e^{a_4}\sin^{1/6}z$ (ordinary space), $f_4 = 1$ (the time), $f_5 = f_6 = f_7 = e^{-a_4}\sin^{1/6}z$ (the extra times) and $f_8 = \cot z$ (the hidden direction). When $a_4$ grows with the time, ordinary space inflates and the three extra times deflate exponentially. The volume factor is $\sqrt{|\det g|} = f_1f_2\cdots f_8 = e^{3a_4}e^{-3a_4}\sin z\cot z = \cos z$: the inflation of space and the deflation of the extra times cancel, and $a_4$ drops out (Chapter 12; record check `sqrt_abs_det_g_is_cos_z` of `Revision/field_equations_a4/reports/wolfram-a4-report.json`). This one fact will be the reason why the charge is conserved without any time-derivative terms (Section 21.17).

**The gammas.** The Revision record `Revision/algebra/gammas.json` holds the author's eight real $16 \times 16$ gamma matrices $\gamma^{(x1)}, \dots, \gamma^{(x8)}$, rebuilt in Revision code from the author's formulas. Every entry is $-1$, $0$ or $+1$, and each row and column holds one nonzero entry (a **signed permutation matrix**). They obey the **Clifford relation**

$$
\gamma^a\gamma^b + \gamma^b\gamma^a = 2\eta^{ab}\,1,\qquad \eta = \mathrm{diag}(+1, +1, +1, -1, -1, -1, -1, +1),
$$

and the **symmetry pattern** $(\gamma^a)^T = \eta_{aa}\gamma^a$: the four space-like gammas ($x_1, x_2, x_3, x_8$) are symmetric, the four time-like ones antisymmetric. Two consequences used again and again: different gammas **anticommute**, $\gamma^a\gamma^b = -\gamma^b\gamma^a$ for $a \ne b$, and $\gamma^a\gamma^a = \eta^{aa}1$. Notebook 21a checks all of this exactly (In [3]).

**The four matrices built from them** (Chapters 4 and 5):

- the **charge matrix** $C = \gamma^{(x8)}\gamma^{(x1)}\gamma^{(x2)}\gamma^{(x3)}$, the product of the four space-like gammas (the author's sigma16);
- the **chirality** $\Gamma = \gamma^{(x8)}\gamma^{(x1)}\gamma^{(x2)}\cdots\gamma^{(x7)}$, the product of all eight; it is diagonal, with the entries $-1$ in the first eight places and $+1$ in the last eight, written $\Gamma = \mathrm{diag}(-1_8, 1_8)$;
- the **Krein matrix** $B = -iC\gamma^{(x4)}$;
- the 28 **generators** $S^{ab} = \tfrac14(\gamma^a\gamma^b - \gamma^b\gamma^a)$ of the rotations and boosts, which for $a \ne b$ equal $\tfrac12\gamma^a\gamma^b$.

**Three rules for moving gammas**, each derived from the Clifford relation.

**(R1)** $\Gamma$ anticommutes with every gamma. Moving $\gamma^b$ from the left of $\Gamma$ to its right passes the seven factors $\gamma^a$ with $a \ne b$, each of which costs a sign, and the factor $\gamma^b$ itself, which costs none: the total sign is $(-1)^7 = -1$.

**(R2)** $\Gamma$ commutes with every product of an even number of gammas, in particular with $C$ and with every $S^{ab}$ (each factor costs a sign by (R1), and an even number of signs multiply to $+1$). Also $\Gamma\Gamma = 1$ and $\Gamma^T = \Gamma$, because $\Gamma$ is diagonal with entries $\pm1$.

**(R3)** $C^T = C$, $CC = 1$ and $C\gamma^aC = -(\gamma^a)^T$ for every $a$. Derivation, line by line. First

$$
C^T = (\gamma^{(x3)})^T(\gamma^{(x2)})^T(\gamma^{(x1)})^T(\gamma^{(x8)})^T = \gamma^{(x3)}\gamma^{(x2)}\gamma^{(x1)}\gamma^{(x8)}
$$

(the transpose of a product is the product of the transposes in reverse order; space-like gammas are symmetric). Reversing the order of four different anticommuting factors takes $3 + 2 + 1 = 6$ exchanges, so $C^T = (-1)^6C = C$. Then

$$
CC = CC^T = \gamma^{(x8)}\gamma^{(x1)}\gamma^{(x2)}\gamma^{(x3)}\gamma^{(x3)}\gamma^{(x2)}\gamma^{(x1)}\gamma^{(x8)} = 1
$$

(each neighbouring pair $\gamma\gamma$ of a space-like gamma is $+1$; remove them from the inside out). Next, $\gamma^aC = -C\gamma^a$ when $a$ is space-like (passing through $C$ costs three signs for the other three factors and none for $\gamma^a$ itself) and $\gamma^aC = +C\gamma^a$ when $a$ is time-like (four signs). With the symmetry pattern, $(C\gamma^a)^T = (\gamma^a)^TC^T = \eta_{aa}\gamma^aC = -C\gamma^a$ in both cases: every $C\gamma^a$ is **antisymmetric**. Writing this as $(\gamma^a)^TC = -C\gamma^a$ and multiplying from the right by $C$ (with $CC = 1$) gives $(\gamma^a)^T = -C\gamma^aC$.

The record checks these facts exactly (`Revision/algebra/reports/python-algebra.json` and `Revision/lead_checks/reports/charge-conjugation-and-u1.json`, check `representation_real`; Notebook 21a, In [5]).

**The two fields.** dirac16complex is a field $\Psi$ with 16 complex **anticommuting** (Grassmann) components, quantised canonically (Chapter 10). dirac16complex00 is a field with 16 complex **commuting** components, a classical field. Both transform as Pin(4,4) spinors and are coupled to gravity through the vielbein (the scale factors) and the canonical spin connection $\Omega_\mu$ (Chapter 6). The Revision record (`Revision/theory/field-theory.json`, formula `Lagrangian`) gives the same Lagrangian density for both:

$$
\mathcal{L} = \cos z\,\Big[\tfrac12\sum_\mu\big(\bar\Psi\gamma^\mu D_\mu\Psi - (D_\mu\bar\Psi)\gamma^\mu\Psi\big) - mS - U(S)\Big],\qquad \bar\Psi = \Psi^\dagger C,\quad S = \bar\Psi\Psi ,
$$

with the curved gammas $\gamma^\mu = \gamma^{(\mu)}/f_\mu$ (no sum), $D_\mu\Psi = \partial_\mu\Psi + \Omega_\mu\Psi$, $D_\mu\bar\Psi = \partial_\mu\bar\Psi - \bar\Psi\Omega_\mu$, the mass $m$ and the self-interaction $U(S) = \tfrac\lambda2S^2$ with the coupling $\lambda$. Its Euler-Lagrange equation (Chapter 7) is the **field equation**

$$
\gamma^\mu D_\mu\Psi = V\Psi,\qquad V = m + U'(S) ,
$$

which in the author's metric reads (record formula `field_equation`)

$$
e^{-a_4}\sin^{-1/6}z\sum_{i=1}^{3}\gamma^{(xi)}\partial_i\Psi + \gamma^{(x4)}\partial_4\Psi + e^{a_4}\sin^{-1/6}z\sum_{t=5}^{7}\gamma^{(xt)}\partial_t\Psi + \tan z\,\gamma^{(x8)}\partial_8\Psi + 3H\gamma^{(x8)}\Psi = V\Psi .
$$

The term $3H\gamma^{(x8)}\Psi$ is $\gamma^\mu\Omega_\mu\Psi$, the spin connection contracted with the gammas (record formula `gammaOmega_total`; Chapter 8). **Every matrix in this equation is real**: the gammas, the scale factors, $\tan z$, $3H$, and every entry of every $\Omega_\mu$ (lead check `spinor_connection_real`); $V$ is real because $S = \Psi^\dagger C\Psi$ is real (Chapter 7).

**The phase symmetry and its current.** Multiplying every component by one phase, $\Psi \to e^{i\alpha}\Psi$, multiplies $\Psi^\dagger$ by $e^{-i\alpha}$, so every bilinear $\Psi^\dagger X\Psi$, hence $\mathcal{L}$, is unchanged. The group of these phases is called **U(1)**. Its current and charge (record formula `current`) are

$$
J^\mu = -i\bar\Psi\gamma^\mu\Psi,\qquad J^{(x4)} = \Psi^\dagger B\Psi,\qquad Q = \int\cos z\,\Psi^\dagger B\Psi\,dx_1\,dx_2\,dx_3\,dx_5\,dx_6\,dx_7\,dx_8 .
$$

(The time component: $J^{x4} = -i\Psi^\dagger C\gamma^{(x4)}\Psi = \Psi^\dagger B\Psi$, because $f_4 = 1$.) Section 21.17 proves that $Q$ does not change in time.

### 21.8 Charge conjugation is a matrix: the condition on the matrix

**The question.** An antiparticle has the same mass and the opposite charge. In a field theory the step from a solution to its "antiparticle solution" is made by a map called **charge conjugation**: it turns every solution of the field equation into a solution whose charge density has the opposite sign. In Dirac's theory of the electron, whose gamma matrices are complex, this map combines the complex conjugate $\Psi^\ast$ with a fixed matrix. In the author's theory the gammas are real. Take a **real** field, one whose components are real numbers, so that $\Psi^\ast = \Psi$. On such a field, complex conjugation does nothing: it is the identity map, and a map that changes nothing cannot exchange matter and antimatter. Whatever charge conjugation is in this theory, it must be made by a **matrix**. This section and the next find every such matrix.

**Definition.** A **charge-conjugation matrix** is a constant $16 \times 16$ matrix $\mathcal{C}$ such that, whenever $\Psi$ solves the field equation, the column

$$
\Psi^c = \mathcal{C}\,\bar\Psi^T
$$

solves the field equation of the same form, either with the same $V$ (**same mass**) or with $-V$ (**mass reversed**).

**From the definition to an equation for a matrix**, line by line.

$$
\bar\Psi^T = (\Psi^\dagger C)^T = C^T(\Psi^\dagger)^T = C\Psi^\ast
$$

(the definition of $\bar\Psi$; the rule $(XY)^T = Y^TX^T$; the transpose of the row $\Psi^\dagger$ is the column $\Psi^\ast$, and $C^T = C$ by (R3)). So $\Psi^c = \mathcal{C}C\Psi^\ast$. Write $M = \mathcal{C}C$; then $\Psi^c = M\Psi^\ast$, and because $CC = 1$, $\mathcal{C} = MC$.

*Step 1 (conjugate the equation).* The complex conjugate of a product is the product of the conjugates, a real factor is its own conjugate, and the derivative of the conjugate is the conjugate of the derivative (the coordinates are real). All matrices of $\gamma^\mu D_\mu$ and the number $V$ are real (Section 21.7). So $\gamma^\mu D_\mu\Psi^\ast = V\Psi^\ast$: **the column $\Psi^\ast$ solves the same equation.**

*Step 2 (multiply by $M$ from the left).* $M\gamma^\mu D_\mu\Psi^\ast = V\,M\Psi^\ast$ (a number $V$ may stand on either side of a matrix).

*Step 3 (the condition).* Suppose that, with one sign $s = +1$ or $s = -1$ for all eight directions,

$$
M\gamma^a = s\,\gamma^aM\qquad (a = x1, \dots, x8) .
$$

Then $M\gamma^\mu = s\,\gamma^\mu M$ (the scale factor $1/f_\mu$ is a number). $M$ commutes with every product of two gammas: $M\gamma^a\gamma^b = s\,\gamma^aM\gamma^b = s^2\gamma^a\gamma^bM = \gamma^a\gamma^bM$ (the condition used twice, then $s^2 = 1$). The spin connection is a combination of such products, so $M\Omega_\mu = \Omega_\mu M$; a constant matrix commutes with a derivative; hence $MD_\mu = D_\mu M$.

*Step 4 (the new field).* With step 3, $M\gamma^\mu D_\mu\Psi^\ast = s\,\gamma^\mu MD_\mu\Psi^\ast = s\,\gamma^\mu D_\mu(M\Psi^\ast)$, and step 2 becomes $s\,\gamma^\mu D_\mu(M\Psi^\ast) = V\,(M\Psi^\ast)$. Multiplying by $s$ and using $s^2 = 1$:

$$
\gamma^\mu D_\mu(M\Psi^\ast) = s\,V\,(M\Psi^\ast) .
$$

**The new field $M\Psi^\ast$ solves the equation with $V$ when $s = +1$ and with $-V$ when $s = -1$.** Since the gammas are real, $(\gamma^a)^\ast = \gamma^a$, and the condition can be written $M(\gamma^a)^\ast = s\,\gamma^aM$, the form in which the Revision record solves it. (For $V = m + \lambda S$, which depends on the field, Section 21.10 shows that for commuting components both matrices found below keep $S$; then $sV = sm + s\lambda S$, so the new field solves the equation with $(m, \lambda)$ when $s = +1$ and with $(-m, -\lambda)$ when $s = -1$. For a free field, $\lambda = 0$, only the mass matters.)

### 21.9 The two charge-conjugation matrices

**Theorem CC.**

- (a) The matrices $M$ with $M(\gamma^a)^\ast = +\gamma^aM$ for all eight $a$ are exactly the multiples of $1$; the matrices with $M(\gamma^a)^\ast = -\gamma^aM$ for all $a$ are exactly the multiples of $\Gamma$.
- (b) Hence there are exactly two charge-conjugation matrices, up to a factor: $\mathcal{C}_+ = C$ (same mass), with $\Psi^c = \mathcal{C}_+\bar\Psi^T = \Psi^\ast$, and $\mathcal{C}_- = \Gamma C$ (mass reversed), with $\Psi^c = \mathcal{C}_-\bar\Psi^T = \Gamma\Psi^\ast$.
- (c) $\mathcal{C}_+^{-1}\gamma^a\mathcal{C}_+ = -(\gamma^a)^T$ and $\mathcal{C}_-^{-1}\gamma^a\mathcal{C}_- = +(\gamma^a)^T$ for every $a$; both are real and symmetric. Conversely, the only matrices $X$ with $\gamma^aX = \zeta X(\gamma^a)^T$ for all $a$ are the multiples of $C$ ($\zeta = -1$) and of $\Gamma C$ ($\zeta = +1$).

*Proof of (a).* The gammas are real, so the conditions read $M\gamma^a = \pm\gamma^aM$. For the sign $+$, $M$ commutes with all eight gammas. The 16 components carry an **irreducible** representation of the group Pin(4,4), which the gammas generate (Chapter 5); by Schur's lemma, a matrix that commutes with every matrix of an irreducible representation is a multiple of $1$ (record check `pin_commutant_dimension_1` of `Revision/algebra/reports/python-algebra.json`, which solves these equations exactly and finds a space of dimension 1). For the sign $-$, $M$ anticommutes with every gamma; then $\Gamma M$ commutes with every gamma:

$$
\gamma^a(\Gamma M) = -\Gamma\gamma^aM = -\Gamma(-M\gamma^a) = (\Gamma M)\gamma^a
$$

(first (R1), then the condition read as $\gamma^aM = -M\gamma^a$, then the two signs multiplied). So $\Gamma M = c\,1$ for a number $c$, and multiplying from the left by $\Gamma$ (with $\Gamma\Gamma = 1$) gives $M = c\,\Gamma$. Conversely $1$ commutes and $\Gamma$ anticommutes with every gamma (R1), so both are solutions. $\square$

**Why each equation halves the freedom.** A $16 \times 16$ matrix has 256 entries. Take only the first condition, $M\gamma^{(x1)} = \gamma^{(x1)}M$. The matrix $\gamma^{(x1)}$ is real and symmetric with $\gamma^{(x1)}\gamma^{(x1)} = 1$, so its eigenvalues are $+1$ and $-1$ (if $\gamma u = cu$ then $u = \gamma\gamma u = c^2u$, so $c^2 = 1$); its trace is zero (its nonzero entries lie outside the diagonal blocks, figure 21a.1), so each eigenvalue occurs 8 times. If $M$ commutes with $\gamma^{(x1)}$ and $\gamma^{(x1)}u = cu$, then $\gamma^{(x1)}(Mu) = M\gamma^{(x1)}u = c\,Mu$: $M$ maps each eigenspace into itself. In a basis of eigenvectors, $M$ is then made of two free $8 \times 8$ blocks: $64 + 64 = 128$ free entries, half of 256. (For $M\gamma^{(x1)} = -\gamma^{(x1)}M$, $M$ maps each eigenspace into the other one, again $64 + 64 = 128$.) Notebook 21a computes the whole sequence exactly: imposing the conditions for the first $k$ gammas leaves $256/2^k$ free numbers, $256, 128, 64, \dots, 2, 1$ (In [7], figure 21a.2). With all eight only one direction is left: the multiples of $1$ or of $\Gamma$, as part (a) says.

*Proof of (b).* $\mathcal{C} = MC$ (Section 21.8). $M = 1$ gives $\mathcal{C}_+ = C$ and $\Psi^c = \Psi^\ast$; $M = \Gamma$ gives $\mathcal{C}_- = \Gamma C$ and $\Psi^c = \Gamma\Psi^\ast$. $\square$

*Proof of (c).* For $\mathcal{C}_+ = C$: $C^{-1} = C$, so $C^{-1}\gamma^aC = C\gamma^aC = -(\gamma^a)^T$ by (R3). For $\mathcal{C}_-$: the inverse of a product is the product of the inverses in reverse order, $\mathcal{C}_-^{-1} = C^{-1}\Gamma^{-1} = C\Gamma$, and

$$
\mathcal{C}_-^{-1}\gamma^a\mathcal{C}_- = C\Gamma\gamma^a\Gamma C = C(-\gamma^a\Gamma)\Gamma C = -C\gamma^aC = +(\gamma^a)^T
$$

(first (R1), then $\Gamma\Gamma = 1$, then (R3)). Both are products of real matrices, hence real. $C^T = C$ is (R3); $(\Gamma C)^T = C^T\Gamma^T = C\Gamma = \Gamma C$ by the transpose rule, (R3), (R2). For the converse: by (R3) the equation $\gamma^aX = \zeta X(\gamma^a)^T$ reads $\gamma^aX = -\zeta XC\gamma^aC$; multiplying from the right by $C$ gives $\gamma^a(XC) = -\zeta(XC)\gamma^a$, so by part (a) $XC$ is a multiple of $1$ when $\zeta = -1$ and of $\Gamma$ when $\zeta = +1$; multiplying from the right by $C$ gives $X = c\,C$ or $X = c\,\Gamma C$. $\square$

**The shape of the two matrices.** $\Gamma = \mathrm{diag}(-1_8, 1_8)$, so $\Gamma C$ is $C$ with the signs of its first eight rows reversed; both have their entries only in the two diagonal $8 \times 8$ blocks (figure 21a.3).

| statement | status | where it is verified |
| --- | --- | --- |
| the gammas, $C$ and the $S^{ab}$ are real; $B$ is purely imaginary, Hermitian, $B^2 = 1$ | PROVED | `Revision/lead_checks/reports/charge-conjugation-and-u1.json`, checks `representation_real`, `B_imaginary_hermitian`; Notebook 21a, In [5] |
| Theorem CC (a): only multiples of $1$ and of $\Gamma$ | PROVED; the 2048 equations of each sign solved exactly | the same report, checks `intertwiners_same_mass`, `intertwiners_reversed_mass`; Notebook 21a, In [6] |
| each gamma equation halves the solution space, $256/2^k$ | COMPUTED exactly (rank over the integers) | Notebook 21a, In [7] (its own computation) |
| Theorem CC (b), (c): $\mathcal{C}_+ = C$, $\mathcal{C}_- = \Gamma C$, their transposition rules | PROVED | the same report, checks `charge_conjugation_matrix_plus`, `charge_conjugation_matrix_minus`; Notebook 21a, In [8] |

### 21.10 The reality conditions, the bilinears and real fields

**The reality (Majorana) conditions.** A field equal to its own conjugate obeys $\Psi = M\Psi^\ast$. Is that a sensible requirement? Conjugating it gives $\Psi^\ast = M^\ast\Psi$, and inserting this back gives $\Psi = MM^\ast\Psi$. If $MM^\ast = 1$, this is automatically true and the condition is **consistent**; otherwise it forces further restrictions. For $M = 1$: $MM^\ast = 1$, and the condition $\Psi = \Psi^\ast$ says the field is real. For $M = \Gamma$: $\Gamma\Gamma^\ast = \Gamma\Gamma = 1$, and the condition $\Psi = \Gamma\Psi^\ast$ says, component by component, $\Psi_r = -\Psi_r^\ast$ for $r = 1, \dots, 8$ (purely imaginary components, where $\Gamma = -1$) and $\Psi_r = \Psi_r^\ast$ for $r = 9, \dots, 16$ (real components). Both conditions are consistent (lead check `majorana_conditions_consistent`; Notebook 21a, In [10], figure 21a.4).

**How a bilinear changes**, line by line. For a fixed matrix $K$ the bilinear $\Psi^\dagger K\Psi = \sum_{r,c}\Psi_r^\ast K_{rc}\Psi_c$ is one number. Replace $\Psi$ by $\Psi' = M\Psi^\ast$ with a real matrix $M$. Exchanging two components costs the factor $\epsilon = +1$ for commuting and $\epsilon = -1$ for anticommuting components (the conjugated components $\Psi_r^\ast$ count as further anticommuting numbers).

*Line 1.* $(\Psi')^\dagger = (M\Psi^\ast)^\dagger = (\Psi^\ast)^\dagger M^\dagger = \Psi^TM^\dagger$ (the rule $(XY)^\dagger = Y^\dagger X^\dagger$; conjugating twice gives the number back). So $\Psi'^\dagger K\Psi' = \Psi^TM^\dagger KM\Psi^\ast = \sum_{r,c}\Psi_r\,(M^\dagger KM)_{rc}\,\Psi_c^\ast$.

*Line 2.* Exchange the factors $\Psi_r$ and $\Psi_c^\ast$, which costs $\epsilon$: $\sum_{r,c}\epsilon\,\Psi_c^\ast(M^\dagger KM)_{rc}\Psi_r$.

*Line 3.* Rename the summation letters, $r \leftrightarrow c$: $\sum_{r,c}\Psi_r^\ast\,\epsilon(M^\dagger KM)_{cr}\,\Psi_c = \Psi^\dagger K'\Psi$ with

$$
K' = \epsilon\,(M^\dagger KM)^T .
$$

If $K' = +K$ the bilinear is kept; if $K' = -K$ it is reversed.

**The scalar and the currents.** $S$ has $K = C$, the current $J^a$ has $K = -iC\gamma^a$. Both maps are real and symmetric, $M^\dagger = M$.

- $\mathcal{C}_+$ ($M = 1$), scalar: $K' = \epsilon C^T = \epsilon C$ (R3). So $S \to \epsilon S$.
- $\mathcal{C}_+$, currents: $K' = \epsilon(-iC\gamma^a)^T = \epsilon(-i)(C\gamma^a)^T = \epsilon(-i)(-C\gamma^a) = -\epsilon K$ (the number $-i$ is not changed by a transpose; $C\gamma^a$ is antisymmetric, (R3)). So $J^a \to -\epsilon J^a$.
- $\mathcal{C}_-$ ($M = \Gamma$), scalar: $\Gamma C\Gamma = C\Gamma\Gamma = C$ (R2), so $K' = \epsilon C$ and $S \to \epsilon S$.
- $\mathcal{C}_-$, currents: $\Gamma(-iC\gamma^a)\Gamma = -iC\Gamma\gamma^a\Gamma = -iC(-\gamma^a) = iC\gamma^a$ (R2, R1, $\Gamma\Gamma = 1$), and its transpose is $i(C\gamma^a)^T = -iC\gamma^a = K$. So $K' = \epsilon K$ and $J^a \to \epsilon J^a$.

| map | components | $S$ becomes | every $J^a$ becomes |
| --- | --- | --- | --- |
| $\mathcal{C}_+$ ($M = 1$) | commuting ($\epsilon = +1$) | $+S$ | $-J^a$ |
| $\mathcal{C}_+$ ($M = 1$) | anticommuting ($\epsilon = -1$) | $-S$ | $+J^a$ |
| $\mathcal{C}_-$ ($M = \Gamma$) | commuting ($\epsilon = +1$) | $+S$ | $+J^a$ |
| $\mathcal{C}_-$ ($M = \Gamma$) | anticommuting ($\epsilon = -1$) | $-S$ | $-J^a$ |

This is the table that the Revision record measured (lead check `bilinears_under_charge_conjugation`; Notebook 21a, In [14], compares with the record's own table). For the commuting field dirac16complex00, $\mathcal{C}_+$ keeps the mass and the scalar and reverses every current, in particular the charge density: it is the antiparticle map of this field. $\mathcal{C}_-$ reverses the mass and keeps the charge. The anticommuting rows are statements about classical Grassmann components; the quantised field is decided by the operator computation of Section 21.26. (The record's detail text adds in parentheses that normal ordering supplies one more sign for each bilinear in the quantum theory. Section 21.26 finds, with explicit operators, that the same-mass candidate counts the charge $Q - 16$, the charge shifted and not reversed; so that remark is not supported for the charge, in agreement with the operator computation of Chapter 5. This is listed as OPEN for the owner of the record in Section 21.38.)

*A check with numbers* (Notebook 21a, In [17]): for one fixed complex column $\Psi$ the notebook finds $S = +6.0205$ and $J^{(x4)} = +6.4970$; for $\Psi^\ast$, $S = +6.0205$ and $J^{(x4)} = -6.4970$; for $\Gamma\Psi^\ast$, $S = +6.0205$ and $J^{(x4)} = +6.4970$.

**All 256 bilinears.** Every $16 \times 16$ matrix is a combination of the 256 products $\Gamma_A = \gamma^{a_1}\gamma^{a_2}\cdots\gamma^{a_k}$ ($a_1 < \dots < a_k$ in the order $x_1, \dots, x_8$, $k = 0, \dots, 8$, with $\Gamma_\emptyset = 1$), so the bilinears $\bar\Psi\Gamma_A\Psi = \Psi^\dagger C\Gamma_A\Psi$ are a complete list. The number $k$ of gammas is the **degree**. For $\mathcal{C}_+$ with commuting components, $K' = (C\Gamma_A)^T$, and line by line:

$$
(C\Gamma_A)^T = \Gamma_A^TC^T = (\gamma^{a_k})^T\cdots(\gamma^{a_1})^T\,C
$$

(the transpose of a product reverses the order; $C^T = C$);

$$
= (-C\gamma^{a_k}C)\cdots(-C\gamma^{a_1}C)\,C = (-1)^kC\gamma^{a_k}\cdots\gamma^{a_1}C\,C
$$

(R3 for each factor; the inner pairs $CC = 1$ cancel);

$$
= (-1)^k(-1)^{k(k-1)/2}\,C\gamma^{a_1}\cdots\gamma^{a_k} = (-1)^{k(k+1)/2}\,C\Gamma_A
$$

($CC = 1$ at the end; reversing the order of $k$ different anticommuting factors takes $k(k-1)/2$ exchanges, each costing a sign; and $k + k(k-1)/2 = k(k+1)/2$). So under $\mathcal{C}_+$ a commuting bilinear of degree $k$ gets the sign $(-1)^{k(k+1)/2}$: $+, -, -, +, +, -, -, +, +$ for $k = 0, \dots, 8$. For $\mathcal{C}_-$ the extra factor is $\Gamma C\Gamma_A\Gamma = C\,\Gamma\Gamma_A\Gamma = (-1)^kC\Gamma_A$ (R2, then R1 once for each of the $k$ factors), so the sign is $(-1)^k(-1)^{k(k+1)/2} = (-1)^{k(k-1)/2}$ (the exponents differ by $2k$, an even number). Anticommuting components multiply every sign by $\epsilon = -1$. Notebook 21a computes the sign of all 256 bilinears in the four cases and finds exactly these rules (In [15], figure 21a.6).

**Real fields.** For a field with real commuting components three facts hold.

- (F1) **The currents vanish.** $J^a = -i\Psi^TA\Psi$ with the antisymmetric $A = C\gamma^a$ (R3). For every column $u$ of real numbers and every antisymmetric $A$, the number $u^TAu$ equals its own transpose, $u^TAu = (u^TAu)^T = u^TA^Tu = -u^TAu$ (a number is its own transpose; the transpose of a product reverses the order; $A^T = -A$), and a number equal to minus itself is zero. A real field carries no current and no U(1) charge.
- (F2) **$\mathcal{C}_+$ acts as the identity.** $\Psi^c = \Psi^\ast = \Psi$: a real field is its own same-mass conjugate.
- (F3) **The real matrix $\Gamma$ reverses the mass.** The map $\Psi \to \Gamma\Psi$ (no conjugation) takes real fields to real fields. It keeps the scalar, $(\Gamma\Psi)^TC(\Gamma\Psi) = \Psi^T\Gamma^TC\Gamma\Psi = \Psi^TC\Psi$ (R2), and it reverses every kinetic matrix, $\Gamma^TC\gamma^a\Gamma = C\Gamma\gamma^a\Gamma = -C\gamma^a$ (R2, R1). In the field equation, $\Gamma$ commutes with $\Omega_\mu$ (an even matrix, R2) and with every derivative, and anticommutes with every $\gamma^\mu$, so $\gamma^\mu D_\mu(\Gamma\Psi) = -\Gamma\gamma^\mu D_\mu\Psi = -V\,\Gamma\Psi$: with $S$ unchanged, $\Gamma\Psi$ solves the equation with $(m, \lambda) \to (-m, -\lambda)$. This is theorem T1 of the Revision record (Section 21.19).

By Theorem CC, every real matrix that maps real solutions to solutions with $\pm V$ is a multiple of $1$ or of $\Gamma$. So for real fields the only nontrivial matrix map is $\Gamma$, and it reverses the mass (lead check `real_fields_charge_conjugation`; Notebook 21a, In [18] and In [19], figure 21a.7). A real field has no charge to reverse (F1); what $\Gamma$ exchanges is the sign of the mass. Plain complex conjugation, which is the identity on a real field, is never a matter-antimatter map for it.

### 21.11 The conjugations acting on an exact solution in the author's metric

Theorem CC is general. Here it is watched at work on an **exact solution of the field equation in the author's curved metric**, valid for every history $a_4(x_4)$, in particular the one in which the three extra times deflate exponentially.

**The solution.** The Revision record (`Revision/theory/field-theory.json`, formula `exact_solutions`, item (i)) states: for $U = 0$,

$$
\Psi = \sin^\alpha z\,\Big(\cosh(kx_4)\,1 + \frac{\sinh(kx_4)}{k}M_m\Big)\chi ,
$$

$$
M_m = -m\gamma^{(x4)} + b\,\gamma^{(x4)}\gamma^{(x8)},\qquad b = 3H(2\alpha + 1),\qquad k^2 = b^2 - m^2 ,
$$

with a constant column $\chi$ and any number $\alpha$. It depends only on $x_4$ and $z$. **Why it solves the equation**, line by line:

*Step 1.* $M_m^2 = m^2\gamma^{(x4)}\gamma^{(x4)} - mb\big(\gamma^{(x4)}\gamma^{(x4)}\gamma^{(x8)} + \gamma^{(x4)}\gamma^{(x8)}\gamma^{(x4)}\big) + b^2\gamma^{(x4)}\gamma^{(x8)}\gamma^{(x4)}\gamma^{(x8)}$ (the square multiplied out, keeping the order of the matrices).

*Step 2.* $\gamma^{(x4)}\gamma^{(x4)} = -1$ ($x_4$ is time-like) and $\gamma^{(x8)}\gamma^{(x8)} = +1$; $\gamma^{(x4)}\gamma^{(x8)}\gamma^{(x4)} = -\gamma^{(x4)}\gamma^{(x4)}\gamma^{(x8)} = \gamma^{(x8)}$ (anticommute the last two, then $\gamma^{(x4)}\gamma^{(x4)} = -1$). So the bracket is $-\gamma^{(x8)} + \gamma^{(x8)} = 0$, and the last term is $b^2\gamma^{(x4)}(\gamma^{(x8)}\gamma^{(x4)})\gamma^{(x8)} = -b^2\gamma^{(x4)}\gamma^{(x4)}\gamma^{(x8)}\gamma^{(x8)} = b^2$. Hence $M_m^2 = -m^2 + b^2 = k^2$ (times $1$).

*Step 3.* Let $U(x_4) = \cosh(kx_4) + \sinh(kx_4)M_m/k$. Its derivative is $k\sinh(kx_4) + \cosh(kx_4)M_m$ (chain rule), and $M_mU = \cosh(kx_4)M_m + \sinh(kx_4)M_m^2/k = \cosh(kx_4)M_m + k\sinh(kx_4)$ (step 2): so $dU/dx_4 = M_mU$, and $\partial_4\Psi = M_m\Psi$ ($\sin^\alpha z$ and $\chi$ do not depend on $x_4$).

*Step 4.* The derivatives along $x_1, x_2, x_3, x_5, x_6, x_7$ vanish, so the factors $e^{\mp a_4}$ of the field equation multiply zero: **the solution holds for every history $a_4$**. With $\partial_8 = 6H\,\partial_z$ (chain rule, $z = 6Hx_8$) the equation becomes

$$
E_m[\Psi] \equiv \gamma^{(x4)}\partial_4\Psi + 6H\tan z\,\gamma^{(x8)}\partial_z\Psi + 3H\gamma^{(x8)}\Psi - m\Psi = 0 .
$$

*Step 5.* $\gamma^{(x4)}\partial_4\Psi = \gamma^{(x4)}M_m\Psi = \big(-m\gamma^{(x4)}\gamma^{(x4)} + b\gamma^{(x4)}\gamma^{(x4)}\gamma^{(x8)}\big)\Psi = (m - b\gamma^{(x8)})\Psi$ (step 3, then $\gamma^{(x4)}\gamma^{(x4)} = -1$).

*Step 6.* $\partial_z\sin^\alpha z = \alpha\sin^{\alpha - 1}z\cos z$, so $\partial_z\Psi = \alpha\cot z\,\Psi$ and $6H\tan z\,\gamma^{(x8)}\partial_z\Psi = 6H\alpha\,\gamma^{(x8)}\Psi$ ($\tan z\cot z = 1$).

*Step 7.* Adding: $E_m[\Psi] = \big(m - b\gamma^{(x8)} + 6H\alpha\gamma^{(x8)} + 3H\gamma^{(x8)} - m\big)\Psi = \big(3H(2\alpha + 1) - b\big)\gamma^{(x8)}\Psi = 0$, because $b = 3H(2\alpha + 1)$.

The record checks this exactly (check `exact_solution_family_x4_x8` of `Revision/theory/reports/python-field-theory.json`), and Notebook 21a checks it again with sympy (In [11]).

**The numbers chosen.** $H = 1/6$ (so $z = x_8$), $\alpha = 1$ and $m = 2$. Then $b = 3 \cdot \tfrac16 \cdot 3 = \tfrac32$ and $k^2 = \tfrac94 - 4 = -\tfrac74 < 0$. So $k = iw$ with $w = \sqrt7/2$ is imaginary; with $\cosh(iw x_4) = \cos(wx_4)$ and $\sinh(iwx_4)/(iw) = \sin(wx_4)/w$ the solution oscillates in time, and $U = \cos(wx_4) + \sin(wx_4)M_m/w$ is a **real** matrix.

**The two conjugates.** Since $U$ and $\sin z$ are real, $\Psi^\ast = \sin z\,U\chi^\ast$: the same formula with the column $\chi^\ast$, so $\Psi^\ast$ solves the equation with the **same** mass $+2$. For the other, $\Gamma M_m\Gamma = -m\Gamma\gamma^{(x4)}\Gamma + b\Gamma\gamma^{(x4)}\gamma^{(x8)}\Gamma = m\gamma^{(x4)} + b\gamma^{(x4)}\gamma^{(x8)} = M_{-m}$ (R1 for the single gamma, R2 for the pair), and $k^2$ is the same for $\pm m$; so $\Gamma U_m\Gamma = U_{-m}$ and $\Gamma\Psi^\ast = \sin z\,U_{-m}(\Gamma\chi^\ast)$: the solution formula with the mass $-2$. **$\Gamma\Psi^\ast$ solves the equation with the reversed mass $-2$.** The negative controls fail: $E_{-2}[\Psi^\ast] = E_{+2}[\Psi^\ast] + 4\Psi^\ast = 4\Psi^\ast$ (the last term of $E_m$ changes by $-(-2)\Psi^\ast + 2\Psi^\ast$), so its size is four times the size of $\Psi^\ast$, about 10; the notebook measures at least 9.67 along the time (In [13]). By the table of Section 21.10, $\Psi^\ast$ carries the charge density $-J^{(x4)}$ and $\Gamma\Psi^\ast$ carries $+J^{(x4)}$ (figure 21a.5).

| statement | status | where it is verified |
| --- | --- | --- |
| the record states the field equation and the exact solution (i) as used here | checked word for word | `Revision/theory/field-theory.json`, formulas `field_equation`, `exact_solutions`; Notebook 21a, In [11] |
| the solution solves the field equation for every $a_4$ | PROVED (above; sympy) | `Revision/theory/reports/python-field-theory.json`, check `exact_solution_family_x4_x8`; Notebook 21a, In [11] |
| $\Psi^\ast$ solves with $+2$, $\Gamma\Psi^\ast$ with $-2$; the exchanged masses fail | PROVED (sympy, exact); COMPUTED along $x_4$ (size below $10^{-12}$ and exactly four times the field) | Notebook 21a, In [12] and In [13] |
| $\Psi^\ast$ has $-J^{(x4)}$, $\Gamma\Psi^\ast$ has $+J^{(x4)}$ at every time | COMPUTED (161 times, to rounding) | Notebook 21a, In [13] |

### 21.12 Example: Notebook 21a solves for every charge-conjugation matrix

Notebook 21a turns Sections 21.7 to 21.11 into exact computations on the author's gammas. It reads the gammas from `Revision/algebra/gammas.json` and the lead report `Revision/lead_checks/reports/charge-conjugation-and-u1.json`; it checks the eight real gammas and draws them; it builds $C$, $\Gamma$, $B$ and the $S^{ab}$; it writes the conditions $M(\gamma^a)^\ast = s\gamma^aM$ as two systems of 2048 linear equations for the 256 entries of $M$ and solves them exactly over the rational numbers; it watches each equation halve the solution space; it builds $\mathcal{C}_+$ and $\mathcal{C}_-$, checks their transposition rules and solves the transposition equations; it checks the two reality conditions; it reads the field equation and the exact solution from the field-theory record word for word and applies both conjugations to the solution; it computes the signs of all 256 bilinears; and it treats real fields. Nine of its checks reproduce checks of the lead report, two reproduce the field-theory record. It runs in about 30 seconds; the times measured on the build computer, which depend on how busy that computer is, are recorded in the notebook's provenance file `Revision/textbook/notebooks/21a_conjugation_matrices.PROVENANCE.md`. It needs no Rust, prints 27 PASS lines and draws seven figures.

<!-- NOTEBOOK 21a -->

### 21.15 Line-by-line walk-through of Notebook 21a

The notebook has 20 code cells, In [1] to In [20]. This section explains every line of every one of them, in order: a line or a small group of lines is quoted, then explained. The printed lines of each cell are shown in Section 21.14 after the label Out; the figures are shown there with their captions.

**In [1], the set-up cell.** Every line that starts with `#` is a **comment**, which Python skips. The comment lines at the top of the cell are the complete run instructions of Section 21.13, so that the notebook file carries its own instructions. The code starts after the line that announces THE SET-UP; it is the same in every notebook of this book and computes no physics.

```python
import json  # reads and writes JSON files (text files that hold names and numbers)
import os  # reads the environment variable TEXTBOOK_OUTPUT_ROOT (explained below)
import textwrap  # breaks long printed text into lines of at most 89 characters
from pathlib import Path  # file and folder paths that work on Windows, macOS and Linux
```

`import` loads a **module**, a part of Python or of an installed package, so that the code can use it; the text after `#` on the same line is a comment. `json`, `os`, `textwrap` and `pathlib` come with Python. `from pathlib import Path` takes the single name `Path` out of `pathlib`; a `Path` is the address of a file or folder, written the same way on every operating system.

```python
import matplotlib  # the plotting package
import matplotlib.pyplot as plt  # its drawing functions, called plt by convention
from IPython.display import Image, display  # shows a saved picture below a cell
```

These load the plotting package matplotlib, its drawing functions under the short name `plt`, and the two functions `Image` and `display` of IPython (the part of Jupyter that runs Python), which show a picture file below a cell.

```python
NOTEBOOK_ID = "21a"  # this notebook: chapter 21, example a
```

A **variable** is a name for a value; this line gives the name `NOTEBOOK_ID` to the **string** (a text in quotes) `"21a"`. The figure files are named after it.

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

`def` defines a **function**, a named piece of code that runs when it is called. The text in triple quotes under the `def` line is its **docstring**, a description that Python stores but does not execute. `Path.cwd()` is the folder in which Jupyter runs the notebook, and `.resolve()` writes it as a complete address. `here.parents` is the list of the folders above it, and `[here, *here.parents]` is the list that starts with `here` and continues with them (the star unpacks one list into another). The `for` loop visits these folders one after the other; the indented lines below it run once for each. The operator `/` joins a folder and a name into a longer path, and `.is_file()` is true when that file exists. The first folder that holds `Revision/textbook/requirements.txt` is the repository, and `return` hands it back. If none does, `raise` stops the notebook with a `FileNotFoundError` whose message (two strings written next to each other, which Python joins) says what to do.

```python
# The repository folder.  It is never printed: it differs from computer to computer,
# and the printed output of a notebook must not.
REPO = find_repository_root()
# Every file is WRITTEN below OUTPUT_ROOT.  OUTPUT_ROOT is the repository folder unless
# the environment variable TEXTBOOK_OUTPUT_ROOT names another folder; the book's
# checking tool sets it, so that a check run writes into a scratch folder instead.
OUTPUT_ROOT = Path(os.environ.get("TEXTBOOK_OUTPUT_ROOT", str(REPO)))
```

The function is called and its result named `REPO`. The last line chooses where files are written: `os.environ` holds the **environment variables** of the program (named texts it receives from the computer), and `.get(name, default)` returns the value of `TEXTBOOK_OUTPUT_ROOT` if it is set and `str(REPO)` (the path written as a string) otherwise. When you run the notebook it is not set, so files go into the repository; the book's checking tool sets it to a scratch folder.

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

Two small functions. `repository_file` gives the full path of a repository file, for reading a Revision record. `output_file` gives the full path at which to write a file; `path.parent.mkdir(parents=True, exist_ok=True)` first creates its folder and any missing folder above it, and does nothing if the folder exists.

```python
def say(text):
    """Print text in lines of at most 89 characters (the width of a page of the book)."""
    print(textwrap.fill(str(text), width=89, subsequent_indent="    "))
```

`say` prints a text in lines of at most 89 characters; `textwrap.fill` breaks the text at blanks and starts every line after the first with four blanks. That is why some printed lines of Section 21.14 continue on an indented second line.

```python
matplotlib.rcdefaults()  # ignore personal matplotlib settings: same figures everywhere
plt.rcParams.update({"figure.figsize": (7.0, 4.2), "font.size": 10.0,
                     "axes.grid": True, "grid.alpha": 0.3})
```

`matplotlib.rcdefaults()` returns to the built-in settings, so that the figures are the same on every computer. `plt.rcParams.update({...})` sets the size of a figure (7.0 by 4.2 inches), the size of its letters (10 points) and a faint grid (`grid.alpha` 0.3 means 30 per cent opaque). The braces make a **dictionary**: pairs `key: value`, separated by commas. A line that ends inside an open bracket continues on the next line.

```python
FIGURE_FOLDER = "Revision/textbook/figures"  # where the figures are saved
CAPTION_FILE = f"{FIGURE_FOLDER}/{NOTEBOOK_ID}.captions.json"  # their captions
FIGURE_NUMBERS = {}  # figure name -> its number k (file name <id>_<k>_<name>.png)
CAPTIONS = {}  # figure file name -> caption, written to CAPTION_FILE after every figure
# Start with an empty captions file ({} is an empty JSON dictionary); save_figure fills
# it.  newline="\n" writes the same line ends on Windows, macOS and Linux.
output_file(CAPTION_FILE).write_text("{}\n", encoding="utf-8", newline="\n")
```

A string that starts with `f` is an **f-string**: a name in braces is replaced by its value, so `CAPTION_FILE` is `"Revision/textbook/figures/21a.captions.json"`. `FIGURE_NUMBERS` and `CAPTIONS` start as empty dictionaries. The last line writes an empty JSON dictionary and a line end into the captions file; `encoding="utf-8"` fixes how letters are stored, and `"\n"` is the line-end character.

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

`setdefault(name, value)` returns the number already stored for this figure name, or stores and returns one more than the number of figures so far (`len` counts the entries of a dictionary): the figures are numbered 1, 2, 3, and a cell run twice keeps its number. The file name joins the notebook id, the number and the name, for example `21a_1_eight_gammas.png`. `fig.savefig` writes the PNG file with 150 dots per inch, cuts away the empty margin and stores no program name, so that two runs write the same bytes. `plt.close(fig)` removes the figure from memory. The caption is stored, the whole dictionary is written to the captions file (`json.dumps` turns it into JSON text with sorted keys), `display(Image(...))` shows the saved picture below the cell (the output `<IPython.core.display.Image object>` in Section 21.14 is the text label of that picture), and the last line prints where the figure was saved.

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

`PASSED` is an empty **list** (square brackets). `check` is the notebook's test: `if not condition` is true when the condition is false, and then `raise AssertionError(...)` stops the notebook with an error that names the check. Otherwise the name is appended to the list and the line PASS with the name is printed. `record=None` gives the third argument a default value; when a cell passes a record, a second line says which Revision record and check the result reproduces.

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

`report` prints a key number as a line that starts with RESULT; `(f" {unit}" if unit else "")` adds the unit only when one is given (an empty string counts as false). `all_checks_passed` prints the last line of the notebook with the number of passed checks. The last statement prints the one line of Out [1].

**In [2]: reading the gammas and the lead record.**

```python
import itertools  # all subsets of a list (for the 256 products of gammas)

import numpy as np  # arrays of numbers, matrices and linear algebra
```

`itertools` comes with Python; its function `combinations` (In [15]) lists all subsets of a given size. `numpy`, imported under the short name `np`, stores numbers in **arrays** (tables of numbers) and does matrix algebra.

```python
fixture = json.loads(repository_file("Revision/algebra/gammas.json")
                     .read_text(encoding="utf-8"))
COORDS = fixture["coordinates"]  # the list "x1", ..., "x8"
ETA = dict(zip(COORDS, fixture["eta"]))  # +1 space-like, -1 time-like
```

`read_text` reads the whole Revision record `Revision/algebra/gammas.json` as text, and `json.loads` turns the text into Python objects: here a dictionary, called `fixture`. `fixture["coordinates"]` is the entry stored under the key `"coordinates"`, the list of the eight names `"x1"` to `"x8"`. `zip` pairs each name with the matching entry of `fixture["eta"]`, and `dict` turns the pairs into a dictionary, so that `ETA["x4"]` is $-1$ and `ETA["x8"]` is $+1$.

```python
# gamma["x4"] is gamma^(x4), a 16 x 16 array of whole numbers (int64)
gamma = {x: np.array(m, dtype=np.int64) for x, m in zip(COORDS, fixture["gamma"])}
I16 = np.eye(16, dtype=np.int64)  # the identity matrix 1
```

The braces with `for` inside build a dictionary in one line (a **dictionary comprehension**): for each name `x` and stored matrix `m` (a list of 16 lists of 16 numbers), the entry `gamma[x]` is the numpy array of `m` with whole-number entries (`int64`, 64-bit integers). Whole numbers make every product below exact. `np.eye(16)` is the $16 \times 16$ identity matrix.

```python
def product(directions):
    """The matrix product gamma^(d1) gamma^(d2) ... in the order of the list."""
    result = I16
    for d in directions:
        result = result @ gamma[d]  # @ is the matrix product
    return result
```

`product(["x8", "x1"])` starts with the identity and multiplies from the right by each listed gamma in turn; `@` is numpy's matrix product.

```python
RECORD = "Revision/lead_checks/reports/charge-conjugation-and-u1.json"
lead = json.loads(repository_file(RECORD).read_text(encoding="utf-8"))
LEAD = {c["name"]: c for c in lead["checks"]}  # check name -> its entry
```

The lead report of the Revision record is read in the same way. Its entry `"checks"` is a list of checks, each a dictionary with a name, a verdict and a detail text; `LEAD` makes them findable by name.

```python
def lead_passed(name):
    """True when the Revision record has the check name with the verdict PASS."""
    return LEAD.get(name, {}).get("verdict") == "PASS"
```

`LEAD.get(name, {})` returns the check's entry, or an empty dictionary if the record has no such check; `.get("verdict")` then returns its verdict or nothing; `==` compares with `"PASS"`. The function is therefore true only when the record holds the named check with the verdict PASS.

```python
say(f"coordinates: {' '.join(COORDS)}")
say("eta: " + " ".join(f"{ETA[x]:+d}" for x in COORDS))
say(f"lead record: {lead['summary']['passed']} of {lead['summary']['total']} "
    "checks passed")
```

A string followed by `.join(list)` joins the strings of the list with that string between them; here the string is one blank. In `f"{ETA[x]:+d}"` the format `+d` prints a whole number with its sign. The third line reads the record's summary. Out [2] shows the eight coordinates in the author's order, the signs $+1, +1, +1, -1, -1, -1, -1, +1$, and "lead record: 12 of 12 checks passed".

**In [3]: the eight real gammas and the Clifford relation.**

```python
shapes_ok = len(gamma) == 8 and all(g.shape == (16, 16) for g in gamma.values())
entries_ok = all(set(np.unique(g)) <= {-1, 0, 1} for g in gamma.values())
```

`len(gamma)` counts the entries of the dictionary; `g.shape` is the pair (rows, columns) of an array; `all(...)` is true when the test inside is true for every item. `np.unique(g)` lists the different entries of `g`, `set(...)` makes a set of them, and `<=` asks whether that set lies inside the set $\{-1, 0, 1\}$: every entry is $-1$, $0$ or $+1$, so every gamma is real.

```python
# a signed permutation matrix: exactly one nonzero entry in every row and column
permutation_ok = all((np.abs(g).sum(axis=0) == 1).all()
                     and (np.abs(g).sum(axis=1) == 1).all() for g in gamma.values())
check(shapes_ok and entries_ok and permutation_ok,
      "eight real 16 x 16 gamma matrices, entries -1, 0, +1, signed permutations")
```

`np.abs(g)` replaces every entry by its size; `.sum(axis=0)` adds each column and `.sum(axis=1)` each row; `== 1` compares every sum with 1 and `.all()` asks that all comparisons hold. Since the entries are $0$ or $\pm1$, a sum of sizes equal to 1 means exactly one nonzero entry. The check combines the three tests with `and`.

```python
clifford_ok = all(
    np.array_equal(gamma[a] @ gamma[b] + gamma[b] @ gamma[a],
                   2 * (ETA[a] if a == b else 0) * I16)
    for a in COORDS for b in COORDS)  # all 64 ordered pairs (a, b)
check(clifford_ok, "Clifford relation gamma^a gamma^b + gamma^b gamma^a = "
      "2 eta^ab 1 for all 64 pairs, signature (4,4)")
```

For each of the $8 \times 8 = 64$ ordered pairs, `np.array_equal` compares the anticommutator with $2\eta^{ab}1$ exactly; `(ETA[a] if a == b else 0)` is $\eta_{aa}$ on the diagonal and 0 otherwise. Whole-number arithmetic makes this an exact proof of the Clifford relation for the stored matrices.

```python
check(all(np.array_equal(gamma[x].T, ETA[x] * gamma[x]) for x in COORDS),
      "symmetry pattern (gamma^a)^T = eta_aa gamma^a")
```

`.T` is the transpose. The check proves the symmetry pattern of Section 21.7. Out [3] shows the three PASS lines.

**In [4]: the heat maps of the eight gammas.**

```python
from matplotlib.colors import LinearSegmentedColormap

# blue for -1, almost white for 0, red for +1
SIGNS = LinearSegmentedColormap.from_list("signs", ["#2a78d6", "#f0efec", "#e34948"])
```

A **colour map** turns numbers into colours. `from_list` makes one that runs through three colours given as hexadecimal codes (red, green and blue amounts): blue at the lowest value, almost white in the middle, red at the highest.

```python
def heat_map(ax, matrix, title, row_label=True):
    """Draw a 16 x 16 matrix with entries from -1 to +1 (blue -1, pale 0, red +1).
    Rows and columns are numbered from 1; black lines separate the two halves."""
    image = ax.imshow(matrix, cmap=SIGNS, vmin=-1, vmax=1)
    ax.set_title(title)
    ax.set_xticks([0, 7, 15], ["1", "8", "16"])
    ax.set_yticks([0, 7, 15], ["1", "8", "16"])
    ax.axhline(7.5, color="black", linewidth=0.8)
    ax.axvline(7.5, color="black", linewidth=0.8)
    ax.set_xlabel("column")
    if row_label:
        ax.set_ylabel("row")
    ax.grid(False)
    return image
```

`ax` is one panel of a figure. `ax.imshow` draws the matrix as a grid of coloured squares, with $-1$ (`vmin`) blue and $+1$ (`vmax`) red. Python counts rows and columns from 0, so the tick positions 0, 7 and 15 get the labels 1, 8 and 16. `axhline` and `axvline` draw a horizontal and a vertical line at 7.5, between rows (columns) 8 and 9, which splits the matrix into its four $8 \times 8$ blocks. The axis labels are set (the row label only when asked), the grid is switched off, and the drawn image is returned for the colour bar.

```python
fig, axes = plt.subplots(2, 4, figsize=(12.0, 6.6))
for k, (ax, x) in enumerate(zip(axes.flat, COORDS)):
    kind = "space-like" if ETA[x] == 1 else "time-like"
    image = heat_map(ax, gamma[x], f"$\\gamma^{{({x})}}$, {kind}",
                     row_label=(k % 4 == 0))
fig.colorbar(image, ax=axes, ticks=[-1, 0, 1], shrink=0.7, label="matrix entry")
```

`plt.subplots(2, 4, ...)` makes a figure with two rows of four panels, 12 by 6.6 inches. `axes.flat` runs through the panels row by row, `zip` pairs them with the coordinates, and `enumerate` adds the counter `k` = 0, 1, 2, .... The title is LaTeX: in an f-string a doubled brace prints one brace and a doubled backslash prints one backslash, so for `x = "x4"` the title is $\gamma^{(x4)}$ followed by "time-like". `k % 4` is the remainder of $k$ divided by 4, which is 0 for the first panel of each row: only those get a row label. `fig.colorbar` adds one colour bar for all panels.

```python
save_figure(fig, "eight_gammas",
            "The eight real $16 \\times 16$ gamma matrices of the Revision record, "
            "in the author's coordinate order $x1, x2, x3$ (ordinary space), $x4$ "
            "(the time), $x5, x6, x7$ (the deflating extra times), $x8$ (the hidden "
            "direction); horizontal axis the column, vertical axis the row, colour "
            "the entry (red $+1$, blue $-1$, pale $0$). Every matrix has exactly one "
            "nonzero entry in each row and column, and only in the two off-diagonal "
            "$8 \\times 8$ blocks: each gamma exchanges the two halves of the "
            "spinor.")
```

Figure 21a.1, saved with the caption written in the following string lines, which Python joins into one string. **What the figure shows.** Eight panels, one per gamma. Each panel has exactly one coloured square in every row and column, and all of them lie in the upper-right and lower-left blocks: every gamma maps the first eight components into the last eight and back. These two halves are the chiral halves, where $\Gamma = -1$ and $\Gamma = +1$; that every gamma exchanges them is the reason why $\Gamma$ anticommutes with every gamma.

**In [5]: $C$, $\Gamma$, $B$ and the generators.**

```python
C = product(["x8", "x1", "x2", "x3"])  # the charge matrix (the author's sigma16)
Gamma = product(["x8", "x1", "x2", "x3", "x4", "x5", "x6", "x7"])  # the chirality
B = -1j * (C @ gamma["x4"])  # B = -i C gamma^(x4), a complex matrix
```

The three matrices of Section 21.7. Python writes the imaginary unit $i$ as `1j`, so `-1j * (...)` multiplies every entry by $-i$; `B` is therefore an array of complex numbers.

```python
pairs = [(a, b) for i, a in enumerate(COORDS) for b in COORDS[i + 1:]]  # 28 pairs
S_gen = {(a, b): (gamma[a] @ gamma[b] - gamma[b] @ gamma[a]) / 4 for a, b in pairs}
```

`COORDS[i + 1:]` is the part of the list after position `i`, so each pair $(a, b)$ with $a$ before $b$ appears once: $8 \cdot 7/2 = 28$ pairs. `S_gen` stores the generator $S^{ab} = \tfrac14(\gamma^a\gamma^b - \gamma^b\gamma^a)$ for each pair; division by 4 makes the entries decimal numbers (they are $0$ and $\pm\tfrac12$).

```python
same_as_record = (np.array_equal(C, np.array(fixture["C"]))
                  and np.array_equal(Gamma, np.array(fixture["Gamma"])))
gamma_diag = np.diag(np.concatenate([-np.ones(8), np.ones(8)])).astype(np.int64)
check(same_as_record and np.array_equal(Gamma, gamma_diag),
      "C and Gamma equal the record; Gamma = diag(-1 (8 times), +1 (8 times))")
```

The record also stores $C$ and $\Gamma$; the first line compares them with the products just computed. `np.concatenate` joins eight $-1$ and eight $+1$ into one list, `np.diag` makes the diagonal matrix with that list on its diagonal, and `.astype(np.int64)` turns its entries into whole numbers. The check proves $\Gamma = \mathrm{diag}(-1_8, 1_8)$.

```python
check(np.array_equal(C.T, C) and np.array_equal(C @ C, I16)
      and all(np.isrealobj(s) for s in S_gen.values()) and lead_passed(
          "representation_real"),
      "gamma^a, C (symmetric, C^2 = 1) and all 28 S^ab are real",
      record=f"{RECORD}, check representation_real")
```

This proves (R3)'s $C^T = C$ and $CC = 1$, checks that every generator is stored as real numbers (`np.isrealobj` is true for an array without complex entries), and asks that the lead record holds the check `representation_real` with the verdict PASS; the second printed line names that record check.

```python
check(np.array_equal(B.real, np.zeros((16, 16))) and np.allclose(B, B.conj().T)
      and np.allclose(B @ B, np.eye(16)) and lead_passed("B_imaginary_hermitian"),
      "B = -i C gamma^(x4) is purely imaginary, Hermitian, B^2 = 1",
      record=f"{RECORD}, check B_imaginary_hermitian")
```

`B.real` is the array of the real parts, which must all be zero; `B.conj().T` is the conjugate transpose $B^\dagger$, and `np.allclose` compares two arrays entry by entry and accepts a difference up to $10^{-8}$ plus $10^{-5}$ times the size of the corresponding entry of the second array (numpy's default tolerances), far above rounding errors and far below the differences that matter here; `B @ B` must be the identity. Out [5] shows the three PASS lines, two of them with the record checks they reproduce.

**In [6]: every conjugation matrix, solved exactly.**

```python
import sympy as sp  # exact algebra
from sympy.polys.matrices import DomainMatrix  # exact matrices over the rationals
```

`sympy` computes with exact numbers and symbols. A `DomainMatrix` is sympy's fast matrix of exact numbers from a chosen **domain**: the rational numbers `QQ` (fractions) or the integers `ZZ`.

```python
def conjugation_system(s, directions=COORDS):
    """Coefficient matrix of M conj(gamma^a) - s gamma^a M = 0 for the 256
    unknowns M_rc (read row by row), one block of 256 equations per direction."""
    blocks = []
    for x in directions:
        G_conj = np.conj(gamma[x]).astype(np.int64)  # (gamma^a)*, equal to gamma^a
        blocks.append(np.kron(I16, G_conj.T) - s * np.kron(gamma[x], I16))
    return np.vstack(blocks)
```

The unknown matrix $M$ is read row by row as one column $y$ of 256 numbers, $y_{16r + c} = M_{rc}$ (rows and columns counted from 0). The entry $(r, c)$ of $MG$ is $\sum_kM_{rk}G_{kc}$; as a linear function of $y$ it is row $16r + c$ of the **Kronecker product** $1 \otimes G^T$ (`np.kron(I16, G_conj.T)`, the $256 \times 256$ block matrix whose block $(r, r')$ is $\delta_{rr'}G^T$). The entry $(r, c)$ of $GM$ is $\sum_kG_{rk}M_{kc}$, row $16r + c$ of $G \otimes 1$ (`np.kron(gamma[x], I16)`). So each direction contributes 256 equations $(1 \otimes G^{\ast T} - s\,G \otimes 1)\,y = 0$. `np.conj` takes the complex conjugate, which changes nothing for the real gammas but keeps the code faithful to the condition $M(\gamma^a)^\ast = s\gamma^aM$. `np.vstack` stacks the blocks into one tall coefficient matrix with $8 \cdot 256 = 2048$ rows.

```python
def exact_solutions(A):
    """A basis of all solutions y of A y = 0, each returned as a 16 x 16 matrix."""
    null = DomainMatrix.from_list(A.tolist(), sp.QQ).nullspace().to_Matrix()
    return [np.array(null.row(k).tolist()[0], dtype=object).reshape(16, 16)
            for k in range(null.rows)]
```

`A.tolist()` turns the numpy array into nested Python lists; `DomainMatrix.from_list(..., sp.QQ)` makes an exact matrix of rational numbers; `.nullspace()` computes, by exact Gaussian elimination, a basis of all solutions of $Ay = 0$ (one solution per row), and `.to_Matrix()` turns it into an ordinary sympy matrix. The list comprehension takes each basis row (`null.row(k)`), turns it into a numpy array of exact sympy numbers (`dtype=object`) and folds the 256 numbers back into a $16 \times 16$ matrix with `.reshape(16, 16)`. No rounding is involved anywhere: a solution can be neither hidden nor invented.

```python
def proportional(X, Y):
    """True when X and Y are nonzero and X is a number times Y."""
    X = np.array(X, dtype=float).reshape(-1)
    Y = np.array(Y, dtype=float).reshape(-1)
    return bool(X.any() and Y.any() and np.linalg.matrix_rank(np.array([X, Y])) == 1)
```

Both matrices are written as rows of 256 decimal numbers (`reshape(-1)` makes one long row). Two nonzero rows are multiples of each other exactly when the $2 \times 256$ matrix made of them has **rank** 1 (only one independent row); `X.any()` is true when some entry is nonzero.

```python
A_same, A_reversed = conjugation_system(+1), conjugation_system(-1)
M_same, M_reversed = exact_solutions(A_same), exact_solutions(A_reversed)
say(f"s = +1: {A_same.shape[0]} equations, {len(M_same)} independent solution(s)")
say(f"s = -1: {A_reversed.shape[0]} equations, {len(M_reversed)} independent "
    "solution(s)")
```

The two systems are built and solved; a comma on both sides assigns two values at once. `A_same.shape[0]` is the number of rows (equations). Out [6] prints 2048 equations and 1 independent solution for each sign.

```python
check(len(M_same) == 1 and proportional(M_same[0], I16)
      and lead_passed("intertwiners_same_mass"),
      "s = +1 (same mass): the solutions are the multiples of the identity",
      record=f"{RECORD}, check intertwiners_same_mass")
check(len(M_reversed) == 1 and proportional(M_reversed[0], Gamma)
      and lead_passed("intertwiners_reversed_mass"),
      "s = -1 (mass reversed): the solutions are the multiples of Gamma",
      record=f"{RECORD}, check intertwiners_reversed_mass")
```

The solution space of each sign has dimension 1, and its basis matrix is a multiple of $1$ (for $s = +1$) or of $\Gamma$ (for $s = -1$): Theorem CC (a), reproducing the two record checks.

**In [7]: each equation halves the solution space.**

```python
dimensions = {}
for s in (+1, -1):
    dims = [256]  # k = 0: no equation, every matrix is a solution
    for k in range(1, 9):
        A = conjugation_system(s, COORDS[:k])  # the first k directions only
        rank = DomainMatrix.from_list(A.tolist(), sp.ZZ).rank()  # exact rank
        dims.append(256 - rank)
    dimensions[s] = dims
    say(f"s = {s:+d}: dimensions for k = 0..8: {dims}")
```

For each sign and each $k = 1, \dots, 8$ (`range(1, 9)` stops before 9), the system of the first $k$ directions (`COORDS[:k]`, the first $k$ names) is built. Its **rank**, the number of independent equations, is computed exactly over the integers; the number of free unknowns, the dimension of the solution space, is $256$ minus the rank. `dims.append` adds it to the list. Out [7] prints $[256, 128, 64, 32, 16, 8, 4, 2, 1]$ for both signs.

```python
check(dimensions[+1] == dimensions[-1] == [256 // 2 ** k for k in range(9)],
      "each gamma equation halves the solution space: 256, 128, ..., 2, 1")
```

`256 // 2 ** k` is the whole-number quotient $256/2^k$ (`**` is a power, `//` division without remainder). Python reads `a == b == c` as "a equals b and b equals c".

```python
fig, ax = plt.subplots(figsize=(7.5, 4.4))
k_values = np.arange(9)
ax.semilogy(k_values, dimensions[+1], "o-", markersize=9,
            label="$s = +1$: $M$ commutes with the first $k$ gammas")
ax.semilogy(k_values, dimensions[-1], "s--", markersize=5,
            label="$s = -1$: $M$ anticommutes with the first $k$ gammas")
```

`np.arange(9)` is the array 0, 1, ..., 8. `semilogy` draws a curve with a logarithmic vertical axis, on which halving is a constant step. The style string `"o-"` means circles joined by a line, and the style string made of the letter s and two hyphens means small squares joined by a dashed line; the squares are drawn smaller so that the circles of the first curve remain visible around them. `label` is the text of the legend.

```python
ax.set_xticks(k_values, ["0"] + [f"{k}\n(+{x})" for k, x in zip(range(1, 9), COORDS)])
ax.set_yticks([1, 2, 4, 8, 16, 32, 64, 128, 256],
              ["1", "2", "4", "8", "16", "32", "64", "128", "256"])
ax.set_xlabel("number $k$ of gamma equations imposed (and the direction added)")
ax.set_ylabel("dimension of the solution space")
ax.set_title("Every equation halves the space of conjugation matrices")
ax.legend()
```

The tick labels of the horizontal axis show $k$ and, below it (`\n` is a line break), the direction added. The vertical ticks are the powers of 2. Axis labels, a title and the legend follow.

```python
save_figure(fig, "halving_solutions",
            "The dimension of the space of $16 \\times 16$ matrices $M$ that obey "
            "$M(\\gamma^a)^\\ast = s\\,\\gamma^a M$ for the first $k$ directions only "
            "(computed exactly as $256$ minus the rank of the equations), for "
            "$s = +1$ (circles) and $s = -1$ (squares); horizontal axis $k$ with "
            "the direction added, vertical axis the dimension on a logarithmic "
            "scale. Both sequences are $256/2^k$: every new gamma halves the "
            "freedom, and with all eight only one direction is left, the multiples "
            "of $1$ ($s = +1$) or of $\\Gamma$ ($s = -1$).")
```

Figure 21a.2. **What the figure shows.** Two identical straight staircases on the logarithmic axis, from 256 down to 1: every gamma equation removes exactly half of the remaining freedom, as Section 21.9 explains for the first step, until only the multiples of $1$ or of $\Gamma$ are left.

**In [8]: the two charge-conjugation matrices and their transposition rules.**

```python
calC_plus = C  # M = 1
calC_minus = Gamma @ C  # M = Gamma
inv_plus = np.linalg.inv(calC_plus)  # the inverse matrix
inv_minus = np.linalg.inv(calC_minus)
```

$\mathcal{C} = MC$ with $M = 1$ and $M = \Gamma$ (Theorem CC (b)). `np.linalg.inv` computes the inverse matrix in decimal numbers.

```python
check(all(np.allclose(inv_plus @ gamma[x] @ calC_plus, -gamma[x].T) for x in COORDS)
      and np.array_equal(calC_plus.T, calC_plus)
      and lead_passed("charge_conjugation_matrix_plus"),
      "calC_+ = C: calC_+^-1 gamma^a calC_+ = -(gamma^a)^T, real, symmetric",
      record=f"{RECORD}, check charge_conjugation_matrix_plus")
check(all(np.allclose(inv_minus @ gamma[x] @ calC_minus, gamma[x].T) for x in COORDS)
      and np.array_equal(calC_minus.T, calC_minus)
      and lead_passed("charge_conjugation_matrix_minus"),
      "calC_- = Gamma C: calC_-^-1 gamma^a calC_- = +(gamma^a)^T, real, symmetric",
      record=f"{RECORD}, check charge_conjugation_matrix_minus")
```

The transposition rules of Theorem CC (c) for all eight gammas, and the symmetry of both matrices (they are whole-number arrays, hence real).

```python
def transposition_system(zeta):
    """Coefficient matrix of gamma^a X - zeta X (gamma^a)^T = 0 for all a."""
    return np.vstack([np.kron(gamma[x], I16) - zeta * np.kron(I16, gamma[x])
                      for x in COORDS])
```

The converse part of (c). With $X$ read row by row as before, $\gamma X$ is `np.kron(gamma[x], I16)` applied to it, and the entry $(r, c)$ of $X\gamma^T$ is $\sum_kX_{rk}\gamma_{ck}$, which is `np.kron(I16, gamma[x])` applied to it (the transpose of $\gamma^T$ is $\gamma$).

```python
X_minus = exact_solutions(transposition_system(-1))  # expected: multiples of C
X_plus = exact_solutions(transposition_system(+1))  # expected: multiples of Gamma C
check(len(X_minus) == 1 and proportional(X_minus[0], calC_plus)
      and len(X_plus) == 1 and proportional(X_plus[0], calC_minus),
      "gamma^a X = zeta X (gamma^a)^T: zeta = -1 only C, zeta = +1 only Gamma C")
```

Both systems are solved exactly: each has a one-dimensional solution space, spanned by $C$ for $\zeta = -1$ and by $\Gamma C$ for $\zeta = +1$. So the usual textbook definition by transposition rules gives the same two matrices. Out [8] shows the three PASS lines.

**In [9]: the heat maps of the two matrices.**

```python
fig, axes = plt.subplots(1, 3, figsize=(11.5, 4.2))
heat_map(axes[0], calC_plus, r"$\mathcal{C}_+ = C$ (same mass)")
heat_map(axes[1], Gamma, r"chirality $\Gamma$", row_label=False)
image = heat_map(axes[2], calC_minus, r"$\mathcal{C}_- = \Gamma C$ (mass reversed)",
                 row_label=False)
fig.colorbar(image, ax=axes, ticks=[-1, 0, 1], shrink=0.8, label="matrix entry")
```

One row of three panels. A string that starts with `r` is a **raw string**, in which a backslash is an ordinary character, convenient for LaTeX titles. The three matrices are drawn with the helper of In [4].

```python
save_figure(fig, "conjugation_matrices",
            "Heat maps of the two charge-conjugation matrices and of the chirality "
            "that relates them: $\\mathcal{C}_+ = C$ (left, the conjugation that "
            "keeps the mass), $\\Gamma$ (middle) and $\\mathcal{C}_- = \\Gamma C$ "
            "(right, the conjugation that reverses the mass); horizontal axis the "
            "column, vertical axis the row, colour the entry (red $+1$, blue $-1$, "
            "pale $0$). $C$ and $\\Gamma C$ have their entries only in the two "
            "diagonal blocks, and they differ only by the sign of the upper half, "
            "where $\\Gamma = -1$.")
```

Figure 21a.3. **What the figure shows.** $C$ and $\Gamma C$ have one entry per row and column, all inside the two diagonal blocks (they are products of an even number of gammas, which keep the halves apart). The middle panel is the diagonal $\Gamma$: blue in the upper half, red in the lower. The right panel is the left one with the colours of the upper eight rows exchanged.

**In [10]: the two reality conditions.**

```python
check(np.array_equal(I16 @ np.conj(I16), I16)
      and np.array_equal(Gamma @ np.conj(Gamma), I16)
      and lead_passed("majorana_conditions_consistent"),
      "M M* = 1 for M = 1 and M = Gamma: both reality conditions are consistent",
      record=f"{RECORD}, check majorana_conditions_consistent")
```

The consistency condition $MM^\ast = 1$ of Section 21.10 for both matrices, reproducing the record check.

```python
rows = np.arange(1, 17)  # the component numbers 1, ..., 16
v = (np.cos(rows) + 0.5) + 1j * np.sin(2.0 * rows)  # a fixed complex column
psi_real = (v + np.conj(v)) / 2  # satisfies Psi = Psi*
psi_gamma = (v + Gamma @ np.conj(v)) / 2  # satisfies Psi = Gamma Psi*
```

`v` is a fixed complex column whose $r$-th entry is $\cos r + 0.5 + i\sin 2r$: an arbitrary but reproducible choice. $(v + v^\ast)/2$ is the real part of $v$, so it is real. For the second: $\Gamma\big((v + \Gamma v^\ast)/2\big)^\ast = (\Gamma v^\ast + \Gamma\Gamma v)/2 = (v + \Gamma v^\ast)/2$ ($\Gamma$ is real and $\Gamma\Gamma = 1$), so `psi_gamma` obeys $\Psi = \Gamma\Psi^\ast$.

```python
check(np.allclose(psi_real, np.conj(psi_real))
      and np.allclose(psi_gamma, Gamma @ np.conj(psi_gamma)),
      "the two example fields satisfy Psi = Psi* and Psi = Gamma Psi*")
```

The check confirms both conditions with numbers.

```python
fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.0), sharey=True)
for ax, psi, title in ((axes[0], psi_real, r"$\Psi = \Psi^*$ (condition of "
                        r"$\mathcal{C}_+$)"),
                       (axes[1], psi_gamma, r"$\Psi = \Gamma\Psi^*$ (condition of "
                        r"$\mathcal{C}_-$)")):
    ax.bar(rows - 0.2, psi.real, width=0.4, label="real part")
    ax.bar(rows + 0.2, psi.imag, width=0.4, label="imaginary part")
    ax.axvline(8.5, color="black", linewidth=0.8)
    ax.set_xticks([1, 4, 8, 12, 16])
    ax.set_xlabel("component number")
    ax.set_title(title)
    ax.legend(loc="lower left")
axes[0].set_ylabel("value of the component")
```

Two panels with a common vertical axis (`sharey=True`). The loop runs over two triples (panel, field, title). `ax.bar` draws bars: the real parts shifted 0.2 to the left of each component number, the imaginary parts 0.2 to the right, each 0.4 wide. A vertical line at 8.5 separates the two halves. Ticks, labels, title and legend (in the lower left corner) follow.

```python
save_figure(fig, "reality_conditions",
            "One field satisfying each reality (Majorana) condition, made from the "
            "same complex column: left $\\Psi = \\Psi^\\ast$ (every imaginary part is "
            "zero), right $\\Psi = \\Gamma\\Psi^\\ast$ (components 1 to 8, where "
            "$\\Gamma = -1$, are purely imaginary; components 9 to 16, where "
            "$\\Gamma = +1$, are real); horizontal axis the component number, "
            "vertical axis the real part (left bar of each pair) and the imaginary "
            "part (right bar). Both conditions can be imposed, because "
            "$MM^\\ast = 1$ for $M = 1$ and for $M = \\Gamma$.")
```

Figure 21a.4. **What the figure shows.** On the left every second bar of a pair is missing (zero imaginary parts). On the right components 1 to 8 have only imaginary parts and components 9 to 16 only real parts, exactly as the condition $\Psi = \Gamma\Psi^\ast$ demands component by component.

**In [11]: the exact solution of the record in the author's metric.**

```python
THEORY = {f["key"]: f["wl"] for f in json.loads(repository_file(
    "Revision/theory/field-theory.json").read_text(encoding="utf-8"))["formulas"]}
PY_THEORY = {c["name"]: c["verdict"].upper() for c in json.loads(repository_file(
    "Revision/theory/reports/python-field-theory.json").read_text(
    encoding="utf-8"))["checks"]}
```

The field-theory record holds a list of formulas, each with a key and its text in Wolfram notation (`"wl"`); `THEORY` maps each key to its text. The independent sympy report of the same record holds checks whose verdicts are written in small letters; `.upper()` turns them into capitals, so that `PY_THEORY[name]` is `"PASS"` for a passed check.

```python
# the left side of the record's field equation, word for word (right side m + U')
FIELD_EQUATION_LEFT = (
    "E^-a4[x4] Sin[z]^(-1/6) (g[x1] d1 + g[x2] d2 + g[x3] d3) Psi + g[x4] d4 Psi"
    " + E^a4[x4] Sin[z]^(-1/6) (g[x5] d5 + g[x6] d6 + g[x7] d7) Psi"
    " + Tan[z] g[x8] d8 Psi + 3 H g[x8] Psi")
# item (i) of the record's formula exact_solutions, word for word
SOLUTION_I = (
    "(i) U = 0: Psi = Sin[z]^al (Cosh[k x4] + Sinh[k x4]/k M) chi, M = -m g[x4]"
    " + 3 H (2 al + 1) g[x4].g[x8], k^2 = 9 H^2 (2 al + 1)^2 - m^2 (any a4)")
```

Two strings, each written as several pieces in parentheses that Python joins: the left side of the field equation and item (i) of the exact solutions, exactly as this book writes them in Section 21.11, but in the record's notation (`g[x4]` is $\gamma^{(x4)}$, `d4` is $\partial_4$, `al` is $\alpha$, `E^a4[x4]` is $e^{a_4}$, the dot is the matrix product).

```python
left, right = THEORY["field_equation"].split(" = ")  # the two sides
say("record, exact solution " + SOLUTION_I)
check(left == FIELD_EQUATION_LEFT and right.startswith("(m + U")
      and THEORY["exact_solutions"].startswith(SOLUTION_I + "; "),
      "the record states the field equation and the exact solution (i) used here",
      record="Revision/theory/field-theory.json, formulas field_equation and "
      "exact_solutions")
```

`split(" = ")` cuts the record's equation at the equals sign into its two sides. The check compares the left side word for word, asks that the right side starts with the factor $m + U'$, and asks that the record's text of the exact solutions starts with item (i) followed by a semicolon. If the record is ever changed, this check fails and the notebook stops.

```python
x4, z = sp.symbols("x4 z", real=True)  # the time x4 and the angle z = 6 H x8
H, alpha, m = sp.Rational(1, 6), 1, 2  # the parameters chosen above
b = 3 * H * (2 * alpha + 1)  # b = 3/2
w = sp.sqrt(m ** 2 - b ** 2)  # k = i w with w = sqrt(7)/2
```

`sp.symbols` makes two symbols that sympy treats as unknown real numbers. `sp.Rational(1, 6)` is the exact fraction $1/6$. Then $b = 3 \cdot \tfrac16 \cdot 3 = \tfrac32$ and $w = \sqrt{4 - 9/4} = \sqrt7/2$, both exact.

```python
G = {x: sp.Matrix(gamma[x].tolist()) for x in COORDS}  # exact sympy matrices
Gamma_s = sp.Matrix(Gamma.tolist())
```

Exact sympy copies of the gammas and of $\Gamma$.

```python
def M_of(mass):
    """M_m = -m gamma^(x4) + b gamma^(x4) gamma^(x8)."""
    return -mass * G["x4"] + b * G["x4"] * G["x8"]
```

The matrix $M_m$ of the solution; for sympy matrices `*` is the matrix product.

```python
def E(mass, field):
    """E_m[Psi] = gamma^(x4) d4 Psi + 6H tan z gamma^(x8) dz Psi + 3H gamma^(x8) Psi
    - m Psi (the field equation of the record for fields of x4 and z only)."""
    tan_z = sp.sin(z) / sp.cos(z)  # tan z written as sin z / cos z
    return (G["x4"] * field.diff(x4) + 6 * H * tan_z * G["x8"] * field.diff(z)
            + 3 * H * G["x8"] * field - mass * field)
```

The left side of the field equation for a field of $x_4$ and $z$ only (step 4 of Section 21.11); `field.diff(x4)` is the exact partial derivative of every component.

```python
# a fixed complex column chi with exact entries (j + i (17 - j)) / 16, j = 1..16
chi = sp.Matrix([sp.Rational(j, 16) + sp.I * sp.Rational(17 - j, 16)
                 for j in range(1, 17)])
U = sp.cos(w * x4) * sp.eye(16) + sp.sin(w * x4) / w * M_of(m)  # real 16 x 16
Psi = sp.sin(z) ** alpha * U * chi
```

`chi` is a column of 16 exact complex numbers, $(j + i(17 - j))/16$; `sp.I` is $i$. `U` is $\cos(wx_4)\,1 + \sin(wx_4)M_m/w$, the form the solution takes for imaginary $k$; it is real. `Psi` is the solution $\sin z\,U\chi$.

```python
check(E(m, Psi).expand() == sp.zeros(16, 1)
      and sp.simplify(M_of(m) ** 2 + w ** 2 * sp.eye(16)) == sp.zeros(16, 16)
      and PY_THEORY["exact_solution_family_x4_x8"] == "PASS",
      "the record's exact solution solves the field equation (mass m = 2)",
      record="Revision/theory/reports/python-field-theory.json, check "
      "exact_solution_family_x4_x8")
```

`.expand()` multiplies out every product, and the result must be the zero column: the field equation holds exactly. The second test is $M_m^2 = -w^2 = k^2$ (step 2 of Section 21.11). Out [11] prints the record's text of the solution and the two PASS lines.

**In [12]: the two conjugates, exactly.**

```python
Psi_conj = Psi.conjugate()  # Psi*: every entry complex-conjugated (x4, z are real)
Psi_gamma_conj = Gamma_s * Psi_conj  # Gamma Psi*
```

`.conjugate()` takes the complex conjugate of every component; since `x4` and `z` were declared real, sympy conjugates only the numbers $i$ in $\chi$.

```python
def vanishes(vector):
    """True when every component expands to exactly zero (sympy multiplies out
    every product; cos z / cos z cancels automatically)."""
    return vector.expand() == sp.zeros(16, 1)


check(vanishes(E(m, Psi_conj)) and vanishes(E(-m, Psi_gamma_conj)),
      "Psi* solves the equation with mass +2, Gamma Psi* with mass -2 (exact)")
check(not vanishes(E(-m, Psi_conj)) and not vanishes(E(m, Psi_gamma_conj)),
      "negative controls: Psi* fails with -2, Gamma Psi* fails with +2")
```

The first check proves what Section 21.11 derived: $\Psi^\ast$ solves the equation with the same mass $+2$, $\Gamma\Psi^\ast$ the one with the reversed mass $-2$. The second is a **negative control**, a test that must fail if the computation is meaningful: with the masses exchanged the equations do not hold.

**In [13]: the conjugates along the time, numerically.**

```python
times = np.linspace(0.0, 8.0, 161)  # 161 times x4 from 0 to 8
z_fixed = np.pi / 4
```

`np.linspace(0, 8, 161)` gives 161 equally spaced times from 0 to 8 (steps of 0.05). The angle is fixed at $z = \pi/4$.

```python
def numeric(expression):
    """Evaluate a sympy 16 x 1 expression of x4 at z = pi/4 for all times."""
    f = sp.lambdify((x4, z), expression, "numpy")
    return np.array([np.array(f(t, z_fixed), dtype=complex).reshape(16)
                     for t in times])


def size(expression):
    """|E| at every time: the length of the 16-component column."""
    return np.linalg.norm(numeric(expression), axis=1)
```

`sp.lambdify` turns an exact expression into a fast numerical function of $x_4$ and $z$. `numeric` evaluates it at every time and stacks the 161 columns into an array of shape $161 \times 16$. `size` computes for each time the length of the column, the square root of the sum of the squared moduli of its 16 entries (`np.linalg.norm` along `axis=1`, that is along each row of the array).

```python
curves = {
    r"$|E_{+2}[\Psi^*]|$ (same mass)": size(E(m, Psi_conj)),
    r"$|E_{-2}[\Gamma\Psi^*]|$ (mass reversed)": size(E(-m, Psi_gamma_conj)),
    r"$|E_{-2}[\Psi^*]|$ (control)": size(E(-m, Psi_conj)),
    r"$|E_{+2}[\Gamma\Psi^*]|$ (control)": size(E(m, Psi_gamma_conj)),
}
floor = 1e-17  # added before taking the logarithm, so that 0 can be drawn
values = list(curves.values())
```

The four sizes, stored under their legend texts: the two solutions and the two controls. On a logarithmic axis zero cannot be drawn, so `floor` ($10^{-17}$) will be added. `values` is the list of the four arrays, in the order written.

```python
say(f"largest |E| of the two solutions below 1e-12: "
    f"{max(values[0].max(), values[1].max()) < 1e-12}")
say(f"smallest |E| of the two controls: {min(values[2].min(), values[3].min()):.2f}")
field_size = size(Psi_conj)  # |Psi*| = |Gamma Psi*| at every time (Gamma permutes)
```

The first line prints True: both solutions give sizes below $10^{-12}$ at every time (rounding only). The second prints the smallest size of the controls, 9.67 (`:.2f` prints two decimals). `field_size` is the length of $\Psi^\ast$ at every time; $\Gamma$ only changes signs of components, so $\Gamma\Psi^\ast$ has the same length.

```python
check(max(values[0].max(), values[1].max()) < 1e-12
      and np.allclose(values[2], 4 * field_size)
      and np.allclose(values[3], 4 * field_size),
      "numerically: the solutions give |E| below 1e-12, the controls |E| = 4 |field|")
```

The controls are exactly four times the length of the field, as Section 21.11 predicted ($E_{-2}[\Psi^\ast] = 4\Psi^\ast$).

```python
B_c = B.astype(complex)  # the charge density is J^(x4) = Psi^dagger B Psi
density = {}
for field, label in ((Psi, r"$\Psi$"), (Psi_conj, r"$\Psi^*$"),
                     (Psi_gamma_conj, r"$\Gamma\Psi^*$")):
    values_f = numeric(field)  # shape (161, 16): the field at every time
    density[label] = np.einsum("tr,rc,tc->t", np.conj(values_f), B_c, values_f).real
d_psi, d_conj, d_gconj = density.values()
```

For each of the three fields the values at all times are computed, and `np.einsum("tr,rc,tc->t", ...)` forms, for each time $t$, the sum $\sum_{r,c}\Psi_r^\ast B_{rc}\Psi_c$: the letters name the indices of the three arrays, and the index after the arrow is the one kept. `.real` keeps the real part (the imaginary part is zero up to rounding, since $B$ is Hermitian). The last line unpacks the three density arrays.

```python
check(np.allclose(d_conj, -d_psi) and np.allclose(d_gconj, d_psi)
      and np.ptp(d_psi) > 0.1,
      "charge density: Psi* has -J^(x4), Gamma Psi* has +J^(x4) at every time")
```

$\Psi^\ast$ carries the opposite charge density at every time and $\Gamma\Psi^\ast$ the same, as the table of Section 21.10 says for commuting components. `np.ptp` (peak to peak) is the largest minus the smallest value; requiring it above 0.1 makes sure the density is not trivially zero or constant.

```python
fig, axes = plt.subplots(1, 2, figsize=(12.0, 4.4))
for (label, values_d), style in zip(density.items(), ["-", "--", ":"]):
    axes[0].plot(times, values_d, style, linewidth=2, label=f"{label}")
axes[0].set_xlabel("time $x_4$")
axes[0].set_ylabel("charge density $\\Psi^\\dagger B\\Psi$ at $z = \\pi/4$")
axes[0].set_title("A solution and its two conjugates")
axes[0].legend(fontsize=8)
```

The left panel draws the three densities against the time, with a solid, a dashed and a dotted line (`density.items()` gives the pairs label and values).

```python
for (label, values_e), style in zip(curves.items(), ["-", "--", "-.", ":"]):
    axes[1].semilogy(times, values_e + floor, style, label=label)
axes[1].set_xlabel("time $x_4$")
axes[1].set_ylabel("$|E|$ at $z = \\pi/4$ (log scale)")
axes[1].set_title("Which mass does each conjugate solve?")
axes[1].legend(fontsize=8)
```

The right panel draws the four sizes on a logarithmic axis, each raised by the floor.

```python
save_figure(fig, "curved_solution_images",
            "Charge conjugation acting on an exact solution of the field equation "
            "in the author's metric ($H = 1/6$, $\\alpha = 1$, mass $m = 2$, valid "
            "for every history $a_4$). Left: the charge density "
            "$\\Psi^\\dagger B\\Psi$ of $\\Psi$ (solid), $\\Psi^\\ast$ (dashed) and "
            "$\\Gamma\\Psi^\\ast$ (dotted, on top of the solid curve) versus the "
            "time $x_4$ at $z = \\pi/4$ (pure numbers); $\\Psi^\\ast$ carries the "
            "opposite charge density. Right: the size $|E|$ of the left-hand "
            "side of the field equation versus $x_4$, logarithmic scale. $\\Psi^\\ast$ "
            "solves the equation with the same mass $+2$ and $\\Gamma\\Psi^\\ast$ the "
            "one with the reversed mass $-2$ ($|E|$ at rounding level, about "
            "$10^{-16}$), while the exchanged masses fail ($|E|$ equals four "
            "times the size of the field, about 10).")
```

Figure 21a.5. **What the figure shows.** Left: the dashed curve is the mirror image of the solid one in the horizontal axis (opposite charge density), and the dotted curve lies on the solid one. The densities are quadratic in $\cos(wx_4)$ and $\sin(wx_4)$ with $w = \sqrt7/2$, so they oscillate with the angular frequency $2w = \sqrt7$, a period of about 2.37. Right: the two solutions stay at the rounding level near $10^{-16}$ at the bottom, the two controls near 10 at the top: about seventeen orders of magnitude separate "solves" from "does not solve".

**In [14]: the sign table of $S$ and $J$.**

```python
def effective(Mmat, K, eps):
    """The matrix K' of the bilinear after Psi -> M Psi*, with the reorder sign eps."""
    return eps * (Mmat.conj().T @ K @ Mmat).T


def sign_of(Kp, K):
    """+1 if K' = K, -1 if K' = -K, 0 otherwise."""
    return 1 if np.allclose(Kp, K) else (-1 if np.allclose(Kp, -K) else 0)
```

`effective` is the rule $K' = \epsilon(M^\dagger KM)^T$ of Section 21.10. `sign_of` compares $K'$ with $K$ and $-K$ and returns the sign, or 0 when neither matches (which never happens here).

```python
K_S = C.astype(complex)  # the scalar S = Psi^dagger C Psi
K_J = [-1j * (C @ gamma[x]) for x in COORDS]  # the currents J^a
measured = {}
```

The matrices of the scalar and of the eight currents; `measured` will collect the signs.

```python
for label, Mmat in (("plus", I16), ("minus", Gamma)):
    for eps in (1, -1):
        sS = sign_of(effective(Mmat, K_S, eps), K_S)
        sJ = [sign_of(effective(Mmat, K, eps), K) for K in K_J]
        measured[f"{label},eps={eps}"] = [sS, sJ]
        kind = "commuting" if eps == 1 else "anticommuting"
        say(f"calC_{'+' if label == 'plus' else '-'}, {kind:13}: S -> {sS:+d} S, "
            f"J -> {sJ[0]:+d} J (all eight components alike: {len(set(sJ)) == 1})")
```

Two nested loops over the two matrices and the two kinds of components. For each case the sign of $S$ and the list of the eight signs of the currents are stored under a key such as `"plus,eps=1"`, the spelling the record uses. The printed line uses a small conditional inside the f-string to write $+$ or $-$, pads the kind to 13 characters (`{kind:13}`) so that the columns line up, and reports whether the eight current signs are all equal (`set(sJ)` has one element then). Out [14] prints the four rows of the table of Section 21.10.

```python
detail = LEAD["bilinears_under_charge_conjugation"]["detail"]
recorded = json.loads(detail.split("measured: ", 1)[1])  # the record's own table
check(measured == recorded and lead_passed("bilinears_under_charge_conjugation"),
      "signs of S and J under calC_+ and calC_-, both statistics, equal the record",
      record=f"{RECORD}, check bilinears_under_charge_conjugation")
```

The record's check stores its own measured table in its detail text after the words "measured: ". `split("measured: ", 1)[1]` takes the text after them, `json.loads` reads it as a dictionary, and the check demands that the notebook's table is identical to the record's.

**In [15]: the signs of all 256 bilinears.**

```python
CASES = [("plus", I16, 1), ("plus", I16, -1), ("minus", Gamma, 1), ("minus", Gamma, -1)]
degree_signs = np.zeros((4, 9), dtype=int)  # rows: the four cases, columns: k
```

The four cases (matrix, kind of components) and an array of zeros with four rows and nine columns for the signs of the degrees $k = 0, \dots, 8$.

```python
for row, (label, Mmat, eps) in enumerate(CASES):
    for k in range(9):
        signs = {sign_of(effective(Mmat, C @ product(A), eps), C @ product(A))
                 for A in itertools.combinations(COORDS, k)}
        # one common sign for all products of degree k, else 0
        degree_signs[row, k] = signs.pop() if len(signs) == 1 else 0
```

`itertools.combinations(COORDS, k)` lists every choice of $k$ different directions in the order $x_1, \dots, x_8$; together over $k = 0, \dots, 8$ these are the 256 products $\Gamma_A$ (`product(A)`; the empty choice gives the identity). For each one the sign of the bilinear with the matrix $C\Gamma_A$ is computed, and the braces collect the signs into a **set**, which keeps each different value once. If all products of degree $k$ share one sign, the set has one element and `pop()` takes it out; otherwise 0 is stored.

```python
k_all = np.arange(9)
formula = np.array([(-1) ** (k_all * (k_all + 1) // 2),
                    -(-1) ** (k_all * (k_all + 1) // 2),
                    (-1) ** (k_all * (k_all - 1) // 2),
                    -(-1) ** (k_all * (k_all - 1) // 2)])
```

The four rows of the degree rules of Section 21.10: $(-1)^{k(k+1)/2}$ for $\mathcal{C}_+$, $(-1)^{k(k-1)/2}$ for $\mathcal{C}_-$, each with an extra minus sign for anticommuting components. numpy computes the power for all nine values of $k$ at once.

```python
for row, (label, _, eps) in enumerate(CASES):
    say(f"calC_{'+' if label == 'plus' else '-'}, eps = {eps:+d}: signs for k = 0..8: "
        + " ".join(f"{s:+d}" for s in degree_signs[row]))
check(np.array_equal(degree_signs, formula),
      "all 256 bilinears: the sign depends only on the degree k, as the formulas say")
```

The underscore `_` is a name for a value that is not used. Each row of measured signs is printed (Out [15]); the check demands that every sign was common to its degree (no 0) and equals the formula.

**In [16]: the sign table as a picture.**

```python
fig, ax = plt.subplots(figsize=(9.0, 3.8))
ax.imshow(degree_signs, cmap=SIGNS, vmin=-1, vmax=1, aspect="auto")
for row in range(4):
    for k in range(9):
        ax.text(k, row, f"{degree_signs[row, k]:+d}", ha="center", va="center")
```

The $4 \times 9$ array is drawn as coloured squares (`aspect="auto"` lets the squares stretch to fill the panel), and `ax.text` writes each sign in the middle of its square (`ha` and `va` are the horizontal and vertical alignment).

```python
ax.set_xticks(range(9), ["0\n($S$)", "1\n($J$)"] + [str(k) for k in range(2, 9)])
ax.set_yticks(range(4), [r"$\mathcal{C}_+$, commuting",
                         r"$\mathcal{C}_+$, anticommuting",
                         r"$\mathcal{C}_-$, commuting",
                         r"$\mathcal{C}_-$, anticommuting"])
ax.set_xlabel("degree $k$ (number of gamma factors in the bilinear)")
ax.set_title("Sign of every bilinear under the two charge conjugations")
ax.grid(False)
```

The column labels mark the scalar ($k = 0$) and the current ($k = 1$); `str(k)` writes a number as text. The row labels name the four cases.

```python
save_figure(fig, "bilinear_signs",
            "The sign that each of the 256 bilinears $\\bar\\Psi\\gamma^{a_1}"
            "\\cdots\\gamma^{a_k}\\Psi$ acquires under $\\Psi \\to M\\Psi^\\ast$ "
            "($M = 1$ for $\\mathcal{C}_+$, $M = \\Gamma$ for $\\mathcal{C}_-$), "
            "for commuting and anticommuting components; horizontal axis the degree "
            "$k$, rows the four cases, colour and number the sign (red $+1$, blue "
            "$-1$). All products of the same degree share one sign. For commuting "
            "components $\\mathcal{C}_+$ keeps the scalar $S$ ($k = 0$) and "
            "reverses the current $J$ ($k = 1$); anticommuting components reverse "
            "every sign.")
```

Figure 21a.6. **What the figure shows.** Each row repeats a pattern of two equal signs followed by two opposite ones: $+, -, -, +, +, -, -, +, +$ for $\mathcal{C}_+$ with commuting components, shifted by one place for $\mathcal{C}_-$, and the colours exchanged for anticommuting components. The pattern has period 4 in $k$ because $k(k+1)/2$ changes its parity in pairs.

**In [17]: a numerical confirmation with numbers.**

```python
rng = np.random.default_rng(2101)  # a fixed seed: the same numbers in every run
psi = rng.normal(size=16) + 1j * rng.normal(size=16)  # a complex field value
```

`np.random.default_rng(2101)` makes a random-number generator started from the fixed **seed** 2101, so every run draws the same numbers. `rng.normal(size=16)` draws 16 numbers from the bell-shaped normal distribution; two such draws make a complex column.

```python
def S_of(p):
    """S = Psi^dagger C Psi."""
    return np.conj(p) @ C @ p


def J_of(p):
    """The eight currents J^a = Psi^dagger (-i C gamma^a) Psi."""
    return np.array([np.conj(p) @ K @ p for K in K_J])
```

For a numpy column `p`, `np.conj(p) @ C @ p` is the number $\sum_{r,c}p_r^\ast C_{rc}p_c$.

```python
for label, p in (("Psi", psi), ("Psi*", np.conj(psi)),
                 ("Gamma Psi*", Gamma @ np.conj(psi))):
    say(f"{label:10}: S = {S_of(p).real:+.4f}, J^(x4) = {J_of(p)[3].real:+.4f}")
```

For the three columns the scalar and the time current (`J_of(p)[3]`, position 3 is $x_4$) are printed with a sign and four decimals: Out [17] shows $S = +6.0205$ for all three and $J^{(x4)} = +6.4970$, $-6.4970$, $+6.4970$.

```python
check(np.isclose(S_of(np.conj(psi)), S_of(psi))
      and np.allclose(J_of(np.conj(psi)), -J_of(psi))
      and np.isclose(S_of(Gamma @ np.conj(psi)), S_of(psi))
      and np.allclose(J_of(Gamma @ np.conj(psi)), J_of(psi)),
      "numbers: Psi* keeps S and reverses J; Gamma Psi* keeps S and J")
```

The commuting rows of the table, confirmed with numbers for all eight currents (`np.isclose` compares two numbers up to rounding).

**In [18]: real fields, exactly.**

```python
r = sp.Matrix(sp.symbols("r1:17", real=True))  # a real field with symbolic entries
C_s = sp.Matrix(C.tolist())
antisymmetric = all(np.array_equal((C @ gamma[x]).T, -(C @ gamma[x])) for x in COORDS)
```

`sp.symbols("r1:17", real=True)` makes the 16 real symbols $r_1, \dots, r_{16}$ (the range stops before 17); `sp.Matrix` puts them into a column, a real field with completely general components. `C_s` is the exact copy of $C$. The third line checks that all eight $C\gamma^a$ are antisymmetric.

```python
currents_zero = all(sp.expand((-sp.I * r.T * C_s * G[x] * r)[0, 0]) == 0
                    for x in COORDS)
S_kept = sp.expand((Gamma_s * r).T * C_s * (Gamma_s * r) - r.T * C_s * r) == \
    sp.zeros(1, 1)
kinetic_reversed = all(np.array_equal(Gamma.T @ C @ gamma[x] @ Gamma, -(C @ gamma[x]))
                       for x in COORDS)
```

`(-sp.I * r.T * C_s * G[x] * r)[0, 0]` is the single entry of the $1 \times 1$ matrix $-ir^TC\gamma^ar$; expanded, it is exactly zero for every $a$: (F1). The second statement is broken over two lines by a backslash at the end of the first (a **line continuation**); it tests that $(\Gamma r)^TC(\Gamma r) - r^TCr$ is exactly zero, so $\Gamma$ keeps $S$. The third tests $\Gamma^TC\gamma^a\Gamma = -C\gamma^a$ for all eight directions: (F3).

```python
check(antisymmetric and currents_zero and S_kept and kinetic_reversed
      and lead_passed("real_fields_charge_conjugation"),
      "real fields: J^a = 0, calC_+ is the identity, Gamma keeps S and reverses "
      "every kinetic matrix C gamma^a",
      record=f"{RECORD}, check real_fields_charge_conjugation")
```

The four facts together reproduce the record check. (That $\mathcal{C}_+$ is the identity on a real field needs no computation: $\Psi^\ast = \Psi$.)

**In [19]: real fields, in a picture.**

```python
psi_r = rng.normal(size=16)  # a real column
phi_r = rng.normal(size=16)  # a second real column
kinetic_before = np.array([psi_r @ C @ gamma[x] @ phi_r for x in COORDS])
kinetic_after = np.array([(Gamma @ psi_r) @ C @ gamma[x] @ (Gamma @ phi_r)
                          for x in COORDS])
S_before, S_after = psi_r @ C @ psi_r, (Gamma @ psi_r) @ C @ (Gamma @ psi_r)
```

Two real columns from the same generator (the next numbers it draws). Think of `phi_r` as the derivative of the field in the kinetic term. The eight **kinetic numbers** $\Psi^TC\gamma^a\Phi$ are computed before and after the map $\Gamma$, and so is the scalar: $S = \Psi^TC\Psi$ before and $(\Gamma\Psi)^TC(\Gamma\Psi)$ after. For a real column `psi_r @ C @ psi_r` is exactly $\Psi^TC\Psi$.

```python
say(f"S before = {S_before:+.4f}, S after = {S_after:+.4f}")
check(np.allclose(kinetic_after, -kinetic_before) and np.isclose(S_after, S_before),
      "numbers: Gamma reverses the eight kinetic numbers and keeps S")
```

Out [19] prints $S = -6.5629$ before and after, and the check confirms that all eight kinetic numbers change sign.

```python
fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.3), width_ratios=[1, 1.4])
heat_map(axes[0], C @ gamma["x4"], r"$C\gamma^{(x4)}$ is antisymmetric")
positions = np.arange(8)
axes[1].bar(positions - 0.2, kinetic_before, width=0.4,
            label=r"$\Psi^T C\gamma^a\Phi$")
axes[1].bar(positions + 0.2, kinetic_after, width=0.4,
            label=r"$(\Gamma\Psi)^T C\gamma^a(\Gamma\Phi)$")
axes[1].axhline(0.0, color="black", linewidth=0.8)
axes[1].set_xticks(positions, COORDS)
axes[1].set_xlabel("direction $a$")
axes[1].set_ylabel("kinetic number")
axes[1].set_title(f"$\\Gamma$ reverses the kinetic numbers; $S$ = {S_before:.3f} "
                  "stays")
axes[1].legend()
```

Two panels, the right one 1.4 times as wide (`width_ratios`). Left: the heat map of $C\gamma^{(x4)}$. Right: pairs of bars for the eight kinetic numbers before and after the map, a black line at zero, the coordinate names as tick labels, and a title that includes the value of $S$ with three decimals.

```python
save_figure(fig, "real_fields",
            "Real fields. Left: heat map of the real matrix $C\\gamma^{(x4)}$ "
            "(horizontal axis the column, vertical axis the row, red $+1$, blue "
            "$-1$); it is antisymmetric, so $\\Psi^T C\\gamma^{(x4)}\\Psi = 0$ for "
            "every real $\\Psi$ and a real field carries no current. Right: the "
            "eight kinetic numbers $\\Psi^T C\\gamma^a\\Phi$ of two fixed real "
            "columns (left bars) and of their images under the real matrix "
            "$\\Gamma$ (right bars); horizontal axis the direction $a$, vertical "
            "axis the value (pure numbers). Every kinetic number changes sign "
            "while $S = \\Psi^T C\\Psi$ stays: with the mass reversed, $\\Gamma$ "
            "maps real solutions to real solutions.")
```

Figure 21a.7. **What the figure shows.** Left: every red square has a blue partner at the mirror position across the diagonal, the picture of antisymmetry, which is why a real field carries no current. Right: each pair of bars has equal height and opposite sign: $\Gamma$ reverses the kinetic term while keeping the mass term, which is the same as keeping the kinetic term and reversing the mass, up to the overall sign of the Lagrangian.

**In [20]: the record and the figure files.**

```python
REPRODUCED_HERE = ["representation_real", "B_imaginary_hermitian",
                   "intertwiners_same_mass", "intertwiners_reversed_mass",
                   "charge_conjugation_matrix_plus", "charge_conjugation_matrix_minus",
                   "majorana_conditions_consistent",
                   "bilinears_under_charge_conjugation",
                   "real_fields_charge_conjugation"]
summary = lead["summary"]
check(summary["passed"] == summary["total"] == 12
      and all(lead_passed(name) for name in REPRODUCED_HERE),
      "the lead record passes 12 of 12; the nine checks reproduced here are in it")
```

The list of the nine record checks this notebook reproduced; the check asks that the lead report passes all 12 of its checks and holds each of the nine. (The other three concern the spin connection and the U(1) identity, reproduced in Notebook 21b, and the quantised field, reproduced in Notebook 21c.)

```python
names = sorted(FIGURE_NUMBERS, key=FIGURE_NUMBERS.get)  # in the order of saving
check(len(names) == 7 and all(
    output_file(f"{FIGURE_FOLDER}/21a_{FIGURE_NUMBERS[n]}_{n}.png").is_file()
    for n in names), "the seven figure files of notebook 21a exist")
all_checks_passed()
```

`sorted(..., key=FIGURE_NUMBERS.get)` lists the figure names in the order of their numbers. The check asks that there are seven and that each file exists where it was written. The last line prints ALL 27 CHECKS PASSED (notebook 21a), the line you must see at the end.

### 21.16 The phase symmetry and Noether's current

Sakharov's first condition asks whether some process can change the number that counts matter minus antimatter. The theory of this book has no baryons; the only number of this kind it has is the U(1) charge $Q$ of Section 21.7. This section finds the current that belongs to the phase symmetry, and Section 21.17 proves that its charge cannot change.

**The symmetry.** Under $\Psi \to e^{i\alpha}\Psi$ with a constant $\alpha$, $\Psi^\dagger \to e^{-i\alpha}\Psi^\dagger$ (the conjugate of $e^{i\alpha}$ is $e^{-i\alpha}$), so every bilinear $\Psi^\dagger X\Psi$ is multiplied by $e^{-i\alpha}e^{i\alpha} = 1$, and $\mathcal{L}$, built from bilinears, does not change.

**A phase that changes from point to point**, line by line. Let $\alpha(x)$ be a function of the coordinates and write $\alpha_\mu = \partial_\mu\alpha$. For $\Psi' = e^{i\alpha}\Psi$:

$$
D_\mu\Psi' = \partial_\mu(e^{i\alpha}\Psi) + \Omega_\mu e^{i\alpha}\Psi = e^{i\alpha}\big(D_\mu\Psi + i\alpha_\mu\Psi\big)
$$

(product rule and chain rule, $\partial_\mu e^{i\alpha} = i\alpha_\mu e^{i\alpha}$; the number $e^{i\alpha}$ passes through the matrix $\Omega_\mu$). In the same way $\bar\Psi' = (e^{i\alpha}\Psi)^\dagger C = e^{-i\alpha}\bar\Psi$ and

$$
D_\mu\bar\Psi' = \partial_\mu(e^{-i\alpha}\bar\Psi) - e^{-i\alpha}\bar\Psi\Omega_\mu = e^{-i\alpha}\big(D_\mu\bar\Psi - i\alpha_\mu\bar\Psi\big) .
$$

Inserting both into the kinetic term, the phases $e^{-i\alpha}e^{i\alpha} = 1$ cancel and

$$
\tfrac12\big(\bar\Psi'\gamma^\mu D_\mu\Psi' - (D_\mu\bar\Psi')\gamma^\mu\Psi'\big) = \tfrac12\big(\bar\Psi\gamma^\mu(D_\mu\Psi + i\alpha_\mu\Psi) - (D_\mu\bar\Psi - i\alpha_\mu\bar\Psi)\gamma^\mu\Psi\big)
$$

$$
= \tfrac12\big(\bar\Psi\gamma^\mu D_\mu\Psi - (D_\mu\bar\Psi)\gamma^\mu\Psi\big) + i\alpha_\mu\bar\Psi\gamma^\mu\Psi
$$

(the two terms with $\alpha_\mu$ are equal and add: $\tfrac12(i + i) = i$). Since $J^\mu = -i\bar\Psi\gamma^\mu\Psi$, we have $\bar\Psi\gamma^\mu\Psi = iJ^\mu$ and $i\alpha_\mu\bar\Psi\gamma^\mu\Psi = i \cdot i\,\alpha_\mu J^\mu = -\alpha_\mu J^\mu$. The scalar $S$ does not change. Hence, with the sum over $\mu$,

$$
\mathcal{L}' - \mathcal{L} = -\cos z\,\alpha_\mu J^\mu .
$$

**The current is the coefficient of $\partial_\mu\alpha$.** This is **Noether's construction**. On a solution of the field equations the action $\int\mathcal{L}\,d^8x$ does not change to first order under any small change of the field that vanishes at the boundary (the principle of stationary action of Chapter 7). For a small $\alpha$ that vanishes at the boundary, $e^{i\alpha}\Psi$ is such a change, so

$$
0 = \int(\mathcal{L}' - \mathcal{L})\,d^8x = -\int\cos z\,(\partial_\mu\alpha)J^\mu\,d^8x = \int\alpha\,\partial_\mu(\cos z\,J^\mu)\,d^8x
$$

(the last step is integration by parts in each coordinate; the boundary term vanishes because $\alpha$ does). This holds for every such $\alpha$, which is only possible if $\partial_\mu(\cos z\,J^\mu) = 0$ everywhere: **the current is conserved on every solution.** Notebook 21b checks the formula $\mathcal{L}' - \mathcal{L} = -\cos z\,\alpha_\mu J^\mu$ with numbers at one point of the author's metric, with the full spin connection, $m = 0.7$, $\lambda = 0.3$ and random field values: it finds $\mathcal{L} = -16.780795$, the same value after a constant phase, and $\mathcal{L}' - \mathcal{L} = +2.348835 = -\cos z\,\alpha_\mu J^\mu$ for a local phase (In [9]).

### 21.17 Exact charge conservation in the author's metric

Noether's argument rests on the principle of stationary action. The Revision record also proves the conservation law directly, as an exact identity, and this section derives it line by line. Write the current as $J^\mu = \Psi^\dagger K^\mu\Psi$ with $K^\mu = -iC\gamma^\mu$ and the field equation as $E = \gamma^\mu D_\mu\Psi - V\Psi = 0$, with real $V = m + U'(S)$; the components are commuting here (the matrix identity found at the end contains no field, and the record checks the conservation law for both kinds of components: checks `commuting_current_conservation` and `grassmann_current_conservation` of `Revision/theory/reports/python-field-theory.json`).

*Line 1 (product rule).*

$$
\partial_\mu(\cos z\,J^\mu) = \Psi^\dagger\big[\partial_\mu(\cos z\,K^\mu)\big]\Psi + \cos z\big[(\partial_\mu\Psi)^\dagger K^\mu\Psi + \Psi^\dagger K^\mu\partial_\mu\Psi\big] .
$$

*Line 2 (the combination of the field equation).* Consider $-i\cos z\,(\Psi^\dagger CE - E^\dagger C\Psi)$. Insert $E$; since the gammas and the $\Omega_\mu$ are real, $E^\dagger = (\partial_\mu\Psi)^\dagger(\gamma^\mu)^T + \Psi^\dagger\Omega_\mu^T(\gamma^\mu)^T - V\Psi^\dagger$. The two terms with $V$ give $-i\cos z\,(V\Psi^\dagger C\Psi - V\Psi^\dagger C\Psi) = 0$, because $V$ is real.

*Line 3 (the derivative terms).* What remains of the derivative terms is $-i\cos z\,\big[\Psi^\dagger C\gamma^\mu\partial_\mu\Psi - (\partial_\mu\Psi)^\dagger(\gamma^\mu)^TC\Psi\big]$. By (R3), $(\gamma^\mu)^TC = -C\gamma^\mu$ (the scale factor $1/f_\mu$ is a number), so this is $-i\cos z\,\big[\Psi^\dagger C\gamma^\mu\partial_\mu\Psi + (\partial_\mu\Psi)^\dagger C\gamma^\mu\Psi\big] = \cos z\big[\Psi^\dagger K^\mu\partial_\mu\Psi + (\partial_\mu\Psi)^\dagger K^\mu\Psi\big]$: exactly the second part of line 1.

*Line 4 (the spin-connection terms).* They give $-i\cos z\,\Psi^\dagger\big[C\gamma^\mu\Omega_\mu - \Omega_\mu^T(\gamma^\mu)^TC\big]\Psi$.

*Line 5 (the matrix identity).* So $\partial_\mu(\cos z\,J^\mu) = -i\cos z\,(\Psi^\dagger CE - E^\dagger C\Psi)$ holds for every field as soon as the first part of line 1 equals line 4, that is (dividing by $-i$) as soon as the $16 \times 16$ **matrix identity**

$$
\sum_\mu\partial_\mu\big(\cos z\,C\gamma^\mu\big) = \cos z\sum_\mu\big(C\gamma^\mu\Omega_\mu - \Omega_\mu^T(\gamma^\mu)^TC\big)
$$

holds (and only then: two matrices that give the same bilinear for every column are equal when, as here, $i$ times each is Hermitian).

*Line 6 (conservation).* On a solution $E = 0$, so $\partial_\mu(\cos z\,J^\mu) = 0$. Integrate over a region of the seven coordinates other than $x_4$ and over a time interval: by the fundamental theorem of calculus the charge $Q(x_4) = \int\cos z\,J^{(x4)}d^7x$ changes only by the **flux** of $\cos z\,J^\mu$ through the boundary of the region. With no flux, $Q$ is constant.

**The matrix identity in the author's metric, by hand.** The left side is a sum over the eight directions of $\partial_\mu(\cos z/f_\mu)\,C\gamma^{(\mu)}$ (the curved gamma is $\gamma^{(\mu)}/f_\mu$).

- For $\mu = x_1, x_2, x_3, x_5, x_6, x_7$ the factor $\cos z/f_\mu$ depends only on $x_4$ and $x_8$, and it is differentiated along $x_\mu$ itself: zero.
- For $\mu = x_4$: $f_4 = 1$ and $\cos z$ does not depend on $x_4$: zero. (This is where the volume factor matters.)
- For $\mu = x_8$: $\cos z/f_8 = \cos z/\cot z = \sin z$, and $\partial_8\sin z = 6H\cos z$ (chain rule, $z = 6Hx_8$).

So the left side is $6H\cos z\,C\gamma^{(x8)}$. For the right side the record gives the spin connection (formula `Omega_components` of `Revision/theory/field-theory.json`; Chapters 6 and 8 derive it):

$$
\Omega_{x_i} = \tfrac12f_i\big(a_4'\gamma^{(xi)}\gamma^{(x4)} + H\gamma^{(xi)}\gamma^{(x8)}\big)\qquad (i = 1, 2, 3),
$$

$$
\Omega_{x_t} = -\tfrac12f_t\big(a_4'\gamma^{(x4)}\gamma^{(xt)} + H\gamma^{(xt)}\gamma^{(x8)}\big)\qquad (t = 5, 6, 7),
$$

and $\Omega_{x_4} = \Omega_{x_8} = 0$, with $f_i = e^{a_4}\sin^{1/6}z$ and $f_t = e^{-a_4}\sin^{1/6}z$. Write $Y_\mu = \gamma^\mu\Omega_\mu$ (no sum). Since $\Omega_\mu^T(\gamma^\mu)^T = Y_\mu^T$ and, by (R3), $Y^TC = -CY$ for any combination $Y$ of single gammas, each direction contributes $\cos z\,(CY_\mu - Y_\mu^TC) = 2\cos z\,CY_\mu$.

- Ordinary space, $i = 1, 2, 3$: $Y_{x_i} = (\gamma^{(xi)}/f_i)\tfrac12f_i\big(a_4'\gamma^{(xi)}\gamma^{(x4)} + H\gamma^{(xi)}\gamma^{(x8)}\big) = \tfrac12\big(a_4'\gamma^{(x4)} + H\gamma^{(x8)}\big)$, because $\gamma^{(xi)}\gamma^{(xi)} = +1$. Contribution: $\cos z\,C\big(+a_4'\gamma^{(x4)} + H\gamma^{(x8)}\big)$.
- Extra times, $t = 5, 6, 7$: $Y_{x_t} = -\tfrac12\big(a_4'\gamma^{(xt)}\gamma^{(x4)}\gamma^{(xt)} + H\gamma^{(xt)}\gamma^{(xt)}\gamma^{(x8)}\big)$. Here $\gamma^{(xt)}\gamma^{(x4)}\gamma^{(xt)} = -\gamma^{(x4)}\gamma^{(xt)}\gamma^{(xt)} = \gamma^{(x4)}$ (anticommute, then $\gamma^{(xt)}\gamma^{(xt)} = -1$) and $\gamma^{(xt)}\gamma^{(xt)} = -1$, so $Y_{x_t} = \tfrac12\big(-a_4'\gamma^{(x4)} + H\gamma^{(x8)}\big)$. Contribution: $\cos z\,C\big(-a_4'\gamma^{(x4)} + H\gamma^{(x8)}\big)$.

Adding the six contributions: the coefficient of $C\gamma^{(x4)}$ is $(3 - 3)a_4'\cos z = 0$ and that of $C\gamma^{(x8)}$ is $6H\cos z$. **Both sides equal $6H\cos z\,C\gamma^{(x8)}$, for every history $a_4$.** (The same six $Y$s add to $\gamma^\mu\Omega_\mu = 3H\gamma^{(x8)}$, the record's formula `gammaOmega_total`.) The identity is PROVED (lead check `u1_noether_matrix_identity` of `Revision/lead_checks/reports/charge-conjugation-and-u1.json`, which builds the connection from the metric with sympy and verifies the identity for a general $a_4(x_4)$; Notebook 21b repeats this, In [3] to In [5]).

**Why the time-derivative terms cancel.** Each inflating direction of space contributes $+a_4'$ to the coefficient of $C\gamma^{(x4)}$, each deflating extra time $-a_4'$. Suppose instead the extra times also inflated, with the scale factor $e^{+a_4}\sin^{1/6}z$ (a **control metric**, not the author's). Then each of the six contributes $+a_4'$, the right side has $6a_4'$ times the volume factor in front of $C\gamma^{(x4)}$, and the identity still holds, because now the volume factor is $\sqrt{|g|} = e^{6a_4}\cos z$ and the left side has the term $\partial_4(e^{6a_4}\cos z)\,C\gamma^{(x4)} = 6a_4'\,e^{6a_4}\cos z\,C\gamma^{(x4)}$. The identity holds in every metric; what is special about the author's metric is that $\sqrt{|g|} = e^{3a_4}e^{-3a_4}\cos z = \cos z$ does not depend on the time: **the deflation of the three extra times exactly compensates the inflation of the three space directions**, the volume of a slice stays constant, and no time-derivative term appears at all. Notebook 21b computes both metrics and draws the eight contributions (In [6] and In [7], figure 21b.1). A **negative control**: with the spin connection set to zero the right side vanishes but the left side does not, so without the spin connection the current would not be conserved (In [5], figure 21b.2).

| statement | status | where it is verified |
| --- | --- | --- |
| the current of the phase symmetry is $J^\mu = -i\bar\Psi\gamma^\mu\Psi$, real; a constant phase leaves $\mathcal{L}$ unchanged | PROVED (Section 21.16); COMPUTED at a point | record formula `current`; Notebook 21b, In [2] and In [9] |
| the spin connection of the author's metric is real; it equals the record's formula; $\gamma^\mu\Omega_\mu = 3H\gamma^{(x8)}$ | PROVED (sympy, general $a_4$) | lead check `spinor_connection_real`; formulas `Omega_components`, `gammaOmega_total`; Notebook 21b, In [4] |
| the U(1) matrix identity; both sides $6H\cos z\,C\gamma^{(x8)}$; fails without the connection | PROVED (sympy, general $a_4$) | lead check `u1_noether_matrix_identity`; Notebook 21b, In [5] |
| the $a_4'$ terms cancel because the deflation keeps $\sqrt{\lvert g\rvert} = \cos z$; the control metric balances $6a_4'$ by its growing volume | PROVED (sympy) | Notebook 21b, In [6] (its own computation) |

### 21.18 The charge of an exact solution: the flux through the brane, a constant charge, an indefinite density

**The solution and its current.** Take again the exact solution of Section 21.11 with $H = 1/6$, $\alpha = 1$, $m = 2$: $\Psi = \sin z\,U(x_4)\chi$ with the real matrix $U = \cos(wx_4) + \sin(wx_4)M/w$, $M = -2\gamma^{(x4)} + \tfrac32\gamma^{(x4)}\gamma^{(x8)}$, $w = \sqrt7/2$, and a fixed complex column $\chi$ (Notebook 21b uses one with exact rational entries). All eight components of its current are in general nonzero, but $\Psi$ depends only on $x_4$ and $z$, so in the conservation law $\sum_\mu\partial_\mu(\cos z\,J^\mu) = 0$ only the terms with $\mu = x_4$ and $\mu = x_8$ survive. Their two densities are

$$
\cos z\,J^{(x4)} = \cos z\,\Psi^\dagger B\Psi,\qquad \cos z\,J^{x8} = \cos z\tan z\,\Psi^\dagger K_8\Psi = \sin z\,\Psi^\dagger K_8\Psi,\quad K_8 = -iC\gamma^{(x8)},
$$

because the curved gamma of $x_8$ is $\gamma^{(x8)}/f_8 = \tan z\,\gamma^{(x8)}$. With $H = 1/6$, $\partial_8 = \partial_z$, and the law reads $\partial_4(\cos z\,J^{(x4)}) + \partial_z(\cos z\,J^{x8}) = 0$; Notebook 21b checks it exactly (In [10]) and with finite differences (In [14]).

**The charge balance**, line by line. Since $U$ is real, $\Psi^\dagger B\Psi = \sin^2z\,\chi^\dagger U^TBU\chi = \sin^2z\,f(x_4)$ with $f(x_4) = \chi^\dagger U^TBU\chi$, and in the same way $\Psi^\dagger K_8\Psi = \sin^2z\,g(x_4)$ with $g = \chi^\dagger U^TK_8U\chi$.

*Line 1.* The charge of the patch (per unit of the other six coordinates) is $Q(x_4) = \int_0^{\pi/2}\cos z\sin^2z\,dz\;f(x_4) = \tfrac13f(x_4)$ (substitute $u = \sin z$, $du = \cos z\,dz$: $\int_0^1u^2du = \tfrac13$).

*Line 2.* The flux density is $\sin z \cdot \sin^2z\,g = \sin^3z\,g(x_4)$: it is $0$ at the tip $z = 0$ and $g(x_4)$ at the brane $z = \pi/2$.

*Line 3.* Integrate the conservation law over $0 < z < \pi/2$: $\frac{d}{dx_4}\int_0^{\pi/2}\cos z\,J^{(x4)}dz + \big[\sin^3z\,g\big]_0^{\pi/2} = 0$ (the integral of a derivative is the difference of the end values), so $dQ/dx_4 = -g(x_4)$.

*Line 4.* Integrating from $0$ to $x_4$:

$$
Q(x_4) - Q(0) = -\int_0^{x_4}g(t)\,dt :
$$

the charge of the patch changes exactly by what flows out through the brane. Notebook 21b checks this exactly with sympy (In [12]) and draws it (figure 21b.4); for its column $\chi$ the charge at $x_4 = 0$ is $0.178467$.

**A solution with zero flux.** Since $M^2 = -w^2$ (Section 21.11, step 2, with $k^2 = -w^2$), define $P = \tfrac12(1 - iM/w)$. Line by line:

- $P^2 = \tfrac14\big(1 - 2iM/w + i^2M^2/w^2\big) = \tfrac14\big(1 - 2iM/w + 1\big) = P$ (the square multiplied out; $i^2M^2/w^2 = (-1)(-w^2)/w^2 = 1$): $P$ is a **projector**.
- $MP = \tfrac12(M - iM^2/w) = \tfrac12(M + iw) = iw\,\tfrac12(1 - iM/w) = iwP$ (the same rule; $-iM^2/w = iw$; factor out $iw$, using $1/i = -i$).
- For $\chi_0 = P\chi$: $M\chi_0 = iw\chi_0$, hence $U\chi_0 = \big(\cos(wx_4) + i\sin(wx_4)\big)\chi_0 = e^{iwx_4}\chi_0$ (Euler's formula).

So $\Psi_0 = \sin z\,e^{iwx_4}\chi_0$ has a single frequency: a **stationary state**. Its charge density $\cos z\sin^2z\,\chi_0^\dagger B\chi_0$ does not depend on the time (the phase $e^{iwx_4}$ cancels against its conjugate), so by line 3 its flux through the brane is zero, and its charge is **constant**. For the column of Notebook 21b the constant is

$$
Q_0 = -\frac{1424}{1875} - \frac{13\sqrt7}{1500} = -0.782397
$$

(In [12], exact). It stays the same while the extra times deflate (figure 21b.6), and since the conservation law holds for every $a_4$, any other history gives the same constant.

**The charge density can be negative.** $J^{(x4)} = \Psi^\dagger B\Psi$ is a quadratic expression with the matrix $B$, which has eight eigenvalues $+1$ and eight $-1$ ($B$ is Hermitian, $B^2 = 1$ and its trace is 0; lead check `B_imaginary_hermitian` and record check `B_properties`). Writing $\Psi = \sum_jc_jv_j$ in orthonormal eigenvectors $v_j$ of $B$ gives $\Psi^\dagger B\Psi = \sum_{B = +1}\lvert c_j\rvert^2 - \sum_{B = -1}\lvert c_j\rvert^2$, which can have either sign; divided by $\Psi^\dagger\Psi = \sum\lvert c_j\rvert^2$ it lies between $-1$ and $+1$. *A worked example in flat space* ($H = 0$, $a_4$ constant). The field equation along the time is $\gamma^{(x4)}\partial_4\Psi = m\Psi$. A **rest state** $\Psi = u\,e^{-imx_4}$ with $-i\gamma^{(x4)}u = u$ solves it: $\gamma^{(x4)}\partial_4\Psi = \gamma^{(x4)}(-im)u\,e^{-imx_4} = m(-i\gamma^{(x4)}u)e^{-imx_4} = m\Psi$. It has the positive frequency $m$. Since $C$ commutes with $\gamma^{(x4)}$ ((R3): $x_4$ is time-like) and $B = C(-i\gamma^{(x4)})$, $B$ commutes with $-i\gamma^{(x4)}$ and maps the 8-dimensional space of such $u$ into itself; there it has four eigenvalues $+1$ (eigenvector $u_+$) and four $-1$ (eigenvector $u_-$), as the notebook computes. For $u = \tfrac35u_+ + \tfrac45u_-$ (length 1, since $\tfrac{9}{25} + \tfrac{16}{25} = 1$) the charge density is $\tfrac{9}{25}(+1) + \tfrac{16}{25}(-1) = -\tfrac{7}{25}$: a positive-frequency field with a **negative** charge density (Notebook 21b, In [16]; figure 21b.7 shows that for 20000 random columns the normalised density takes both signs about equally often, a fraction 0.504 negative). The sign of the charge of a single field is therefore not fixed by the sign of its frequency; Chapter 10 explains what this means after quantisation (the Krein space).

| statement | status | where it is verified |
| --- | --- | --- |
| the exact solution solves the field equation (any $a_4$); local conservation for it | PROVED (sympy) | `Revision/theory/reports/python-field-theory.json`, checks `exact_solution_family_x4_x8`, `commuting_current_conservation`; Notebook 21b, In [10] |
| charge balance $Q(x_4) - Q(0) = -\int_0^{x_4}g$ | PROVED (sympy); COMPUTED to $10^{-12}$ on 161 times | Notebook 21b, In [12] and In [13] (its own computation) |
| the stationary solution has zero flux and the constant charge $-1424/1875 - 13\sqrt7/1500 = -0.782397$ | PROVED (sympy, exact) | Notebook 21b, In [12] |
| finite differences converge to the exact law with order 2 | COMPUTED (ratios $3.966$ to $4.000$) | Notebook 21b, In [14] |
| $B$ has signature (8,8); a positive-frequency rest state with charge density $-7/25$ | PROVED (above); COMPUTED | Notebook 21b, In [16] |

### 21.19 The pair-level bookkeeping: theorem T1 and the zero total charge

**Theorem T1** of the Revision record (`Revision/docs/PAIR_CREATION_PROOFS.md`, its section 4; Chapter 18 gives the complete proof). For both fields, in every gravitational field taken as a fixed background, in particular the author's metric with the deflating extra times: for every configuration $\Psi$,

$$
\mathcal{L}_{m,\lambda}[\Gamma\Psi] = -\mathcal{L}_{-m,-\lambda}[\Psi],\qquad J^\mu[\Gamma\Psi] = -J^\mu[\Psi] ,
$$

$\Gamma\Psi$ solves the field equations with $(m, \lambda)$ if and only if $\Psi$ solves them with $(-m, -\lambda)$, and the energy-momentum tensor is reversed as well.

**The current part**, line by line. $\overline{\Gamma\Psi} = (\Gamma\Psi)^\dagger C = \Psi^\dagger\Gamma^\dagger C = \Psi^\dagger\Gamma C = \Psi^\dagger C\Gamma = \bar\Psi\Gamma$ (the rule $(XY)^\dagger = Y^\dagger X^\dagger$; $\Gamma$ is real and symmetric; $\Gamma$ commutes with $C$ by (R2)). Then $\overline{\Gamma\Psi}\gamma^\mu\Gamma\Psi = \bar\Psi\Gamma\gamma^\mu\Gamma\Psi = -\bar\Psi\gamma^\mu\Gamma\Gamma\Psi = -\bar\Psi\gamma^\mu\Psi$ (R1, then $\Gamma\Gamma = 1$). Multiplying by $-i$: $J^\mu[\Gamma\Psi] = -J^\mu[\Psi]$ at every point, for both kinds of components ($\Gamma$ only multiplies each component by $\pm1$, so no components are reordered).

**On the exact solution.** For $\lambda = 0$, $\Gamma\Psi$ solves the equation with the mass $-2$: every term of $E_m$ in Section 21.11 except the mass term contains one gamma, which anticommutes with $\Gamma$, so $E_{-m}[\Gamma\Psi] = -\Gamma E_m[\Psi] = 0$. Its charge density is the opposite of that of $\Psi$ at every point, and the pair carries none (Notebook 21b, In [11], figure 21b.3). For the stationary solution the partner has the constant charge $+0.782397$ and the pair $0$ (figure 21b.4, right). For five random columns at three times, $Q + Q' = 0$ to $10^{-12}$ while $Q$ itself is nonzero (In [17], figure 21b.8).

**What this says, exactly.** A pair made of a solution $\Psi$ with $(m, \lambda)$ and its partner $\Gamma\Psi$ with $(-m, -\lambda)$, both in the same gravitational field, has total current zero and total charge zero, as **classical bilinears** (ordinary numbers for dirac16complex00, elements of the Grassmann algebra for dirac16complex). Record checks: `T1_current_primordial_commuting` and `T1_current_primordial_grassmann` of `Revision/pairing/reports/wolfram-pairing.json`, `T1.metric.commuting.current` of `Revision/pairing/reports/python-pairing.json`. Status: PROVED.

**What it does not say** (rule R3 of this book; the record's own list is in section 11.2 of `Revision/docs/PAIR_CREATION_PROOFS.md`):

- It does not create anything. T1 is a map between the solutions of two parameter sets. No equation of this theory produces a universe, or a pair of universes, from anything; no creation process, rate, probability or amplitude follows from these equations (Chapter 20).
- No equation forces the partner to exist: a single universe with the charge $Q \ne 0$ is an equally valid solution. Since $Q$ is conserved (Section 21.17), its value is fixed by the initial data and is not explained.
- For $\lambda \ne 0$ the partner has the coupling $-\lambda$ as well; T1 is not a pairing of $+m$ with $-m$ at a fixed coupling.
- At the quantum level, the chirality image $\Gamma\Psi$ of the quantised field carries the Krein metric $-B$: it is the same quantum system, relabelled, and the identity $Q + Q' = 0$ is of the form $X + (-X) = 0$ within that one system. An independently quantised universe of mass $-m$ carries $+B$, cannot be identified with $\Gamma\Psi$, and its charge does not cancel ours (record checks `Q_Krein_metric_of_images` and `Q_no_identification_of_independent_universes` of the Wolfram pairing report; Chapter 10).
- A T1 pair taken as the complete classical source of the author's metric is a zero source, and Einstein's equations then have no solution for $H > 0$ (corollary C1 of the record; check `einstein_no_vacuum_solution` of `Revision/field_equations_a4/reports/wolfram-a4-report.json`). So a T1 pair alone cannot even be the source of the author's universe.
- The member of mass $-m$ is not antimatter of our world: its negative mass is a parameter of a second field configuration. Nothing in this book says that antimatter has negative mass.

The idea that a universe and an anti-universe together are symmetric belongs to a class of ideas in the published literature; a published example is L. Boyle, K. Finn and N. Turok, "CPT-Symmetric Universe", Phys. Rev. Lett. 121, 251301 (2018), who propose that the universe after the big bang is the CPT image of the universe before it, so that the two epochs form a universe/anti-universe pair. Their proposal is cited only as an example of the class; this book neither uses nor tests it, and the pairing of this theory is of a different kind (both members exist at the same time $x_4$, related by the chirality matrix and $m \to -m$). Any scenario in which our universe is one member of such a pair is a **HYPOTHESIS** (Section 21.37).

### 21.20 Example: Notebook 21b follows the charge in the author's metric

Notebook 21b turns Sections 21.16 to 21.19 into exact computations. It reads the gammas, the lead report, the field-theory record and both pairing reports; it builds the canonical spin connection of the author's metric with sympy for an unspecified history $a_4(x_4)$ and checks it against the record; it verifies the U(1) matrix identity, its negative control and the control metric with inflating extra times; it checks the Noether current with a local phase at one point; it follows the charge of the record's exact solution (local conservation, the balance through the brane, a stationary solution of constant charge, a finite-difference test); it shows that the charge density is indefinite; and it does the pair-level bookkeeping of theorem T1. It runs in about 40 seconds; the times measured on the build computer, which depend on how busy that computer is, are recorded in the notebook's provenance file `Revision/textbook/notebooks/21b_charge_conservation.PROVENANCE.md`. It needs no Rust, prints 21 PASS lines and draws eight figures.

<!-- NOTEBOOK 21b -->

### 21.23 Line-by-line walk-through of Notebook 21b

The notebook has 18 code cells, In [1] to In [18]. Each is explained below, line by line or in small groups of lines.

**In [1], the set-up cell.** It is the set-up cell of Notebook 21a, explained line by line in Section 21.15 under In [1], word for word except for two things: the comment lines at the top hold the run instructions of Notebook 21b (Section 21.21), and the line

```python
NOTEBOOK_ID = "21b"  # this notebook: chapter 21, example b
```

names this notebook, so that its figures are called `21b_<k>_<name>.png`. The cell prints its one line, Set-up of notebook 21b complete.

**In [2]: the gammas, $C$, $\Gamma$, $B$ and the records.**

```python
import numpy as np  # numbers, arrays, matrices
import sympy as sp  # exact algebra and calculus
```

numpy for numbers and arrays, sympy for exact algebra and calculus (Section 21.15 explains both).

```python
fixture = json.loads(repository_file("Revision/algebra/gammas.json")
                     .read_text(encoding="utf-8"))
COORDS = fixture["coordinates"]  # "x1", ..., "x8"
ETA = fixture["eta"]  # +1 space-like, -1 time-like, in the order x1..x8
gamma = [np.array(mat, dtype=np.int64) for mat in fixture["gamma"]]  # index 0..7
I16 = np.eye(16, dtype=np.int64)
```

The Revision record of the gammas is read as in Notebook 21a, but here the gammas are kept in a **list**, numbered from 0: `gamma[0]` is $\gamma^{(x1)}$, `gamma[3]` is $\gamma^{(x4)}$ and `gamma[7]` is $\gamma^{(x8)}$. `ETA` is the list of the eight signs in the same order.

```python
real_ok = all(g.shape == (16, 16) and set(np.unique(g)) <= {-1, 0, 1} for g in gamma)
clifford_ok = all(np.array_equal(gamma[a] @ gamma[b] + gamma[b] @ gamma[a],
                                 2 * (ETA[a] if a == b else 0) * I16)
                  for a in range(8) for b in range(8))
check(len(gamma) == 8 and real_ok and clifford_ok,
      "eight real 16 x 16 gamma matrices with the Clifford relation, signature (4,4)")
```

The same tests as In [3] of Notebook 21a, written with the numbers `a`, `b` from 0 to 7 (`range(8)`): eight real $16 \times 16$ matrices with entries $-1$, $0$, $+1$ that obey the Clifford relation for all 64 pairs.

```python
G = [sp.Matrix(g.tolist()) for g in gamma]  # exact sympy copies, G[0] = gamma^(x1)
C_s = G[7] * G[0] * G[1] * G[2]  # C = gamma^(x8) gamma^(x1) gamma^(x2) gamma^(x3)
C = np.array(C_s.tolist(), dtype=np.int64)
```

Exact sympy copies of the gammas; $C$ is built exactly (`C_s`) and also kept as a whole-number numpy array (`C`).

```python
Gamma = gamma[7] @ gamma[0] @ gamma[1] @ gamma[2] @ gamma[3] @ gamma[4] @ gamma[5] \
    @ gamma[6]  # the chirality (index 7 is x8)
B = -1j * (C @ gamma[3])  # B = -i C gamma^(x4); index 3 is x4
K8 = -1j * (C @ gamma[7])  # the matrix of the x8 current: -i C gamma^(x8)
S_gen = [[(G[a] * G[b] - G[b] * G[a]) / 4 for b in range(8)] for a in range(8)]
```

The chirality is the product of all eight in the order $x_8, x_1, \dots, x_7$; the backslash at the end of the first line continues the statement on the next. $B = -iC\gamma^{(x4)}$ and $K_8 = -iC\gamma^{(x8)}$ are the matrices of the charge density and of the $x_8$ current (Section 21.18). `S_gen[a][b]` is the exact generator $S^{ab}$ for all 64 ordered pairs (zero when $a = b$).

```python
LEAD_FILE = "Revision/lead_checks/reports/charge-conjugation-and-u1.json"
LEAD = {c["name"]: c["verdict"] for c in json.loads(
    repository_file(LEAD_FILE).read_text(encoding="utf-8"))["checks"]}
THEORY = {f["key"]: f for f in json.loads(repository_file(
    "Revision/theory/field-theory.json").read_text(encoding="utf-8"))["formulas"]}
PY_THEORY = {c["name"]: c["verdict"].upper() for c in json.loads(repository_file(
    "Revision/theory/reports/python-field-theory.json").read_text(
    encoding="utf-8"))["checks"]}
```

Four Revision records are read into dictionaries: the lead report (check name to verdict), the formulas of the field-theory record (key to the whole formula entry, so that `THEORY[key]["wl"]` is its text), and the verdicts of the sympy field-theory report, in capitals.

```python
WL_PAIR = {c["name"]: c["verdict"] for c in json.loads(repository_file(
    "Revision/pairing/reports/wolfram-pairing.json").read_text(
    encoding="utf-8"))["checks"]}
PY_PAIR = {c["name"]: c["verdict"] for c in json.loads(repository_file(
    "Revision/pairing/reports/python-pairing.json").read_text(
    encoding="utf-8"))["checks"]}
```

The two pairing reports of the Revision record: the WolframScript verifier and the independent sympy checker. Their verdicts are already written as PASS.

```python
clauses = THEORY["current"]["wl"].split("; ")  # the statements of the formula
say("record formula current: " + clauses[0] + "; " + clauses[2])
check(clauses[0] == "J^mu = -i Psibar gamma^mu Psi"
      and clauses[2] == "J^x4 = Psi^dagger B Psi",
      "the record defines J^mu = -i Psibar gamma^mu Psi and J^x4 = Psi^dagger B Psi",
      record="Revision/theory/field-theory.json, formula current")
```

The record's formula `current` is a list of statements separated by semicolons; `split("; ")` cuts it into them. The first defines the current and the third the charge density; the check demands that they are exactly the definitions this notebook uses. Out [2] prints the two statements and two PASS lines.

**In [3]: the canonical spin connection for every history.**

```python
x = sp.symbols("x1:9", real=True)  # the coordinates x1, ..., x8
H = sp.symbols("H", positive=True)  # the author's constant H > 0
a4 = sp.Function("a4", real=True)(x[3])  # an unspecified history a4(x4)
z = 6 * H * x[7]  # z = 6 H x8
eta = sp.diag(*ETA)
```

Eight real symbols for the coordinates (`x[0]` is $x_1$, `x[3]` is $x_4$, `x[7]` is $x_8$), a positive symbol $H$, and an **unspecified function** $a_4(x_4)$: sympy knows nothing about it except that it depends on $x_4$, so every result below holds for every history, the deflating one included. `sp.diag(*ETA)` is the diagonal matrix $\eta$ (the star passes the eight list entries as eight separate arguments).

```python
def geometry(extra_sign):
    """Scale factors, volume factor and the eight matrices Omega_mu of the metric
    whose extra-time factors are exp(extra_sign a4) sin^(1/6) z (extra_sign = -1:
    the author's deflating extra times)."""
    f = ([sp.exp(a4) * sp.sin(z) ** sp.Rational(1, 6)] * 3 + [sp.Integer(1)]
         + [sp.exp(extra_sign * a4) * sp.sin(z) ** sp.Rational(1, 6)] * 3
         + [sp.cot(z)])
    g = sp.diag(*[ETA[a] * f[a] ** 2 for a in range(8)])  # the diagonal metric
    g_inv = g.inv()
```

The function builds the geometry of a metric whose three extra-time scale factors are $e^{\pm a_4}\sin^{1/6}z$: with `extra_sign = -1` the author's metric, with `+1` the control metric of Section 21.17. A list times 3 repeats the list three times, and `+` joins lists: `f` is the list of the eight scale factors. The metric is diagonal with $g_{aa} = \eta_{aa}f_a^2$, and `g.inv()` is its inverse.

```python
    chris = [[[sp.simplify(sum(g_inv[l, m] * (sp.diff(g[m, i], x[j])
                                                + sp.diff(g[m, j], x[i])
                                                - sp.diff(g[i, j], x[m]))
                               for m in range(8)) / 2)
               for j in range(8)] for i in range(8)] for l in range(8)]
```

The Christoffel symbols $\Gamma^l{}_{ij} = \tfrac12\sum_mg^{lm}(\partial_jg_{mi} + \partial_ig_{mj} - \partial_mg_{ij})$ (Chapter 3), stored so that `chris[l][i][j]` is $\Gamma^l{}_{ij}$: three nested list comprehensions, the innermost index written last. `sp.diff(expr, x[j])` is the exact partial derivative and `sp.simplify` tidies each result.

```python
    e_inv = [1 / v for v in f]  # e_a^mu = 1 / f_a on the diagonal
    Omega = []
    for mu in range(8):
        om = sp.zeros(8, 8)  # omega_mu^a_b
        for a in range(8):
            for b_ in range(8):
                om[a, b_] = sp.simplify(f[a] * (sp.diff(e_inv[b_] if a == b_ else 0,
                                                        x[mu])
                                                + chris[a][mu][b_] * e_inv[b_]))
```

The inverse vielbein is diagonal with entries $1/f_a$. For each direction $\mu$ the $8 \times 8$ table $\omega_\mu{}^a{}_b$ of the canonical connection is computed from the **vielbein postulate** $\omega_\mu{}^a{}_b = e^a{}_\nu\big(\partial_\mu e_b{}^\nu + \Gamma^\nu{}_{\mu\lambda}e_b{}^\lambda\big)$; with the diagonal vielbein $e^a{}_\nu = f_a\delta^a_\nu$ and $e_b{}^\nu = \delta_b^\nu/f_b$ the sums collapse to $\omega_\mu{}^a{}_b = f_a\big(\partial_\mu(\delta_{ab}/f_b) + \Gamma^a{}_{\mu b}/f_b\big)$, which is the line in the loop (`e_inv[b_] if a == b_ else 0` is $\delta_{ab}/f_b$; the letter `b_` avoids a clash with other names).

```python
        om_low = eta * om  # omega_mu ab = eta_ac omega_mu^c_b
        Om = sp.zeros(16, 16)
        for a in range(8):
            for b_ in range(8):
                if om_low[a, b_] != 0:
                    Om += om_low[a, b_] * S_gen[a][b_] / 2
        Omega.append(Om.applyfunc(sp.simplify))
```

The first index is lowered with $\eta$ (a matrix product), and the spinor connection $\Omega_\mu = \tfrac12\sum_{a,b}\omega_{\mu ab}S^{ab}$ is summed (only the nonzero coefficients). `applyfunc(sp.simplify)` simplifies every entry, and the matrix is added to the list `Omega`.

```python
    volume = sp.simplify(sp.prod(f))  # sqrt|g| = product of the scale factors
    return f, volume, Omega


f_dfl, vol_dfl, Omega = geometry(-1)  # the author's metric (deflating extra times)
say(f"sqrt|g| of the author's metric = {vol_dfl}")
```

`sp.prod(f)` multiplies the eight scale factors, which for a diagonal metric is $\sqrt{|\det g|}$. The function returns the three results, and it is called for the author's metric. Out [3] prints `cos(6*H*x8)`: the volume factor is $\cos z$, with no $a_4$ in it (Section 21.7). This cell takes about 7 seconds.

**In [4]: the connection agrees with the record.**

```python
a4p = sp.Derivative(a4, x[3])  # a4' = d a4 / d x4
real_ok = all(not entry.has(sp.I) for Om in Omega for entry in Om)
nonzero = any(Om != sp.zeros(16, 16) for Om in Omega)
check(real_ok and nonzero and LEAD["spinor_connection_real"] == "PASS",
      "every entry of Omega_mu is real and not all vanish",
      record=f"{LEAD_FILE}, check spinor_connection_real")
```

`a4p` is the symbol of the derivative $a_4'$. `entry.has(sp.I)` asks whether an entry contains the imaginary unit; none does, so every $\Omega_\mu$ is real. `any` asks that at least one $\Omega_\mu$ is not the zero matrix. This reproduces the lead check that makes $\gamma^\mu D_\mu$ a real operator (Section 21.8, step 1).

```python
s16 = sp.sin(z) ** sp.Rational(1, 6)
expected = []
for mu in range(8):
    if mu in (0, 1, 2):  # x1, x2, x3: inflating ordinary space
        expected.append(sp.exp(a4) * s16 / 2 * (a4p * G[mu] * G[3] + H * G[mu] * G[7]))
    elif mu in (4, 5, 6):  # x5, x6, x7: the deflating extra times
        expected.append(-sp.exp(-a4) * s16 / 2 * (a4p * G[3] * G[mu]
                                                   + H * G[mu] * G[7]))
    else:  # x4 and x8
        expected.append(sp.zeros(16, 16))
```

The record's formula `Omega_components` (Section 21.17), written out for each direction: `if`, `elif` ("else if") and `else` choose the right case.

```python
record_text = THEORY["Omega_components"]["wl"]  # the record's statement
pieces_of_record = [  # the formula above, piece by piece, in the record's notation
    "Omega_xi = (1/2) E^a4[x4] Sin[6 H x8]^(1/6) (a4",
    "g[xi].g[x4] + H g[xi].g[x8]) (i = 1, 2, 3)",
    "Omega_xt = -(1/2) E^-a4[x4] Sin[6 H x8]^(1/6) (a4",
    "g[x4].g[xt] + H g[xt].g[x8]) (t = 5, 6, 7)",
    "Omega_x4 = Omega_x8 = 0"]
```

The record's text of the formula and five pieces of it in the record's notation. The pieces stop just before the derivative of $a_4$, which the record writes with a straight single quote; the notebook avoids writing that character.

```python
check(all((Omega[mu] - expected[mu]).applyfunc(sp.simplify) == sp.zeros(16, 16)
          for mu in range(8))
      and all(piece in record_text for piece in pieces_of_record),
      "Omega_mu equals the record formula Omega_components",
      record="Revision/theory/field-theory.json, formula Omega_components")
```

Every computed $\Omega_\mu$ minus the expected one simplifies to zero, and every piece occurs in the record's text (`in` asks whether one string occurs inside another).

```python
gamma_up = [G[mu] / f_dfl[mu] for mu in range(8)]  # gamma^mu = gamma^a / f_a
contraction = sum((gamma_up[mu] * Omega[mu] for mu in range(8)), sp.zeros(16, 16))
check((contraction - 3 * H * G[7]).applyfunc(sp.simplify) == sp.zeros(16, 16)
      and THEORY["gammaOmega_total"]["wl"] == '3*H*gamma["x8"]',
      "gamma^mu Omega_mu = 3 H gamma^(x8) for every history a4",
      record="Revision/theory/field-theory.json, formula gammaOmega_total")
```

The curved gammas $\gamma^\mu = \gamma^{(\mu)}/f_\mu$; `sum(..., sp.zeros(16, 16))` adds the eight products starting from the zero matrix. The contraction equals $3H\gamma^{(x8)}$, and the record's formula `gammaOmega_total` says the same. Out [4] shows the three PASS lines.

**In [5]: the U(1) matrix identity.**

```python
cos_z = vol_dfl  # sqrt|g| = cos z
lhs = sum((sp.diff(cos_z / f_dfl[mu], x[mu]) * C_s * G[mu] for mu in range(8)),
          sp.zeros(16, 16))
pieces = [cos_z * (C_s * gamma_up[mu] * Omega[mu]
                   - Omega[mu].T * gamma_up[mu].T * C_s) for mu in range(8)]
rhs = sum(pieces, sp.zeros(16, 16))
```

The two sides of the identity of Section 21.17: the left side $\sum_\mu\partial_\mu(\cos z\,C\gamma^\mu) = \sum_\mu\partial_\mu(\cos z/f_\mu)\,C\gamma^{(\mu)}$, and the right side as the list of its eight contributions (kept for In [6]) and their sum.

```python
check((lhs - rhs).applyfunc(sp.simplify) == sp.zeros(16, 16)
      and LEAD["u1_noether_matrix_identity"] == "PASS",
      "the U(1) Noether matrix identity holds exactly for a general history a4",
      record=f"{LEAD_FILE}, check u1_noether_matrix_identity")
check((lhs - 6 * H * sp.cos(z) * C_s * G[7]).applyfunc(sp.simplify)
      == sp.zeros(16, 16), "the left side is exactly 6 H cos z C gamma^(x8)")
check(lhs.applyfunc(sp.simplify) != sp.zeros(16, 16),
      "negative control: with Omega = 0 the right side is 0 but the left side is "
      "not")
```

The difference of the two sides simplifies to the zero matrix for the unspecified $a_4$: the identity holds for every history (reproducing the lead check). The left side equals $6H\cos z\,C\gamma^{(x8)}$, as computed by hand in Section 21.17. The negative control: without the spin connection the right side would be the zero matrix, and the left side is not zero, so the identity, and with it the conservation of the current, would fail.

**In [6]: why the $a_4'$ terms cancel.**

```python
CG4, CG8 = C_s * G[3], C_s * G[7]


def coefficients(matrix, volume):
    """The coefficients of C gamma^(x4) and C gamma^(x8) in matrix, divided by the
    volume factor (trace formula; checked to leave no remainder)."""
    c4 = sp.simplify((matrix * CG4.T).trace() / 16 / volume)
    c8 = sp.simplify((matrix * CG8.T).trace() / 16 / volume)
    remainder = (matrix - volume * (c4 * CG4 + c8 * CG8)).applyfunc(sp.simplify)
    return c4, c8, remainder == sp.zeros(16, 16)
```

The matrices $C\gamma^{(x4)}$ and $C\gamma^{(x8)}$ are signed permutation matrices, so each times its own transpose is $1$, with trace 16, while the trace of one times the transpose of the other is 0 (they are orthogonal). So if a matrix is $P = c_4C\gamma^{(x4)} + c_8C\gamma^{(x8)}$, then $c_4 = \mathrm{tr}(P(C\gamma^{(x4)})^T)/16$, and likewise $c_8$. The function divides by the volume factor and checks that nothing else is left over (`remainder` is the zero matrix).

```python
dfl = [coefficients(p, cos_z) for p in pieces]  # the author's metric
f_ctl, vol_ctl, Omega_ctl = geometry(+1)  # control: inflating extra times
gamma_up_ctl = [G[mu] / f_ctl[mu] for mu in range(8)]
pieces_ctl = [vol_ctl * (C_s * gamma_up_ctl[mu] * Omega_ctl[mu]
                         - Omega_ctl[mu].T * gamma_up_ctl[mu].T * C_s)
              for mu in range(8)]
lhs_ctl = sum((sp.diff(vol_ctl / f_ctl[mu], x[mu]) * C_s * G[mu] for mu in range(8)),
              sp.zeros(16, 16))
```

The coefficients of the eight contributions in the author's metric; then the whole computation again for the control metric (`geometry(+1)`): its curved gammas, its eight contributions and its left side. This takes about 7 seconds.

```python
ctl = [coefficients(p, vol_ctl) for p in pieces_ctl]
lhs_c4, _, _ = coefficients(lhs_ctl, vol_ctl)  # control: the volume-growth term
lhs_c4_dfl, _, _ = coefficients(lhs, cos_z)  # author's metric: zero
say(f"control metric: sqrt|g| = {vol_ctl}")
```

The coefficients of the control contributions, and the $C\gamma^{(x4)}$ coefficient of each left side (the underscores discard the other two returned values). Out [6] first prints the control volume factor `exp(6*a4(x4))*cos(6*H*x8)`, which grows with $a_4$.

```python
for mu in range(8):  # the coefficients in units of a4' (sympy divides exactly)
    say(f"{COORDS[mu]}: author's metric {str(sp.simplify(dfl[mu][0] / a4p)):>2} a4'"
        f" | control metric {str(sp.simplify(ctl[mu][0] / a4p)):>2} a4'")
```

For each direction the $C\gamma^{(x4)}$ coefficient divided by $a_4'$ is printed for both metrics (`:>2` right-aligns the text in two characters). Out [6] shows $1, 1, 1, 0, -1, -1, -1, 0$ for the author's metric and $1, 1, 1, 0, 1, 1, 1, 0$ for the control.

```python
expected_dfl = [a4p] * 3 + [0] + [-a4p] * 3 + [0]  # +a4' space, -a4' extra times
expected_ctl = [a4p] * 3 + [0] + [a4p] * 3 + [0]  # all six +a4'
check(all(c[2] for c in dfl + ctl)
      and all(sp.simplify(c[0] - e) == 0 for c, e in zip(dfl, expected_dfl))
      and all(sp.simplify(c[0] - e) == 0 for c, e in zip(ctl, expected_ctl))
      and sp.simplify(lhs_c4 - 6 * a4p) == 0 and sp.simplify(lhs_c4_dfl) == 0
      and (lhs_ctl - sum(pieces_ctl, sp.zeros(16, 16))).applyfunc(sp.simplify)
      == sp.zeros(16, 16),
      "a4' terms: +a4' (space) and -a4' (deflating extra times) cancel; the "
      "control metric balances 6 a4' by its growing volume")
```

One check for everything of the paragraph "Why the time-derivative terms cancel" of Section 21.17: no remainders; the expected coefficients in both metrics; the left side of the control has $6a_4'$ and that of the author's metric $0$; and the identity holds in the control metric too.

**In [7]: the volume balance as bars.**

```python
fig, axes = plt.subplots(1, 2, figsize=(12.0, 4.3), sharey=True)
labels = COORDS + ["left side"]
for ax, data, lhs_value, title in (
        (axes[0], dfl, lhs_c4_dfl, "author's metric: extra times deflate"),
        (axes[1], ctl, lhs_c4, "control: extra times inflate")):
    heights = [float(sp.simplify(c[0] / a4p)) for c in data + [(lhs_value,)]]
```

Two panels, one per metric. The loop runs over two groups of four values. `data + [(lhs_value,)]` appends a one-element tuple to the eight coefficient triples, so that `c[0]` is also the left-side coefficient; each is divided by $a_4'$ and turned into a decimal number with `float`.

```python
    colours = ["#e34948" if h > 0 else ("#2a78d6" if h < 0 else "#999999")
               for h in heights[:8]] + ["#555555"]
    ax.bar(range(9), heights, color=colours)
    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.set_xticks(range(9), labels, rotation=30)
    ax.set_title(title + f"; sum of the eight = {round(sum(heights[:8]))}")
    ax.set_xlabel("direction $\\mu$ of the term")
axes[0].set_ylabel("coefficient of $C\\gamma^{(x4)}$ in units of $a_4'$")
```

Red bars for positive, blue for negative, grey for zero coefficients, and a dark bar for the left side. The tick labels are turned by 30 degrees; the title states the sum of the eight contributions (`heights[:8]`, rounded to a whole number).

```python
save_figure(fig, "volume_balance",
            "Why the time-derivative terms of the U(1) identity cancel. Each bar is "
            "the coefficient of $C\\gamma^{(x4)}$, in units of $a_4'$ and divided by "
            "the volume factor, contributed by one direction $\\mu$ to the right "
            "side $\\cos z\\,\\sum_\\mu(C\\gamma^\\mu\\Omega_\\mu - \\Omega_\\mu^T"
            "(\\gamma^\\mu)^TC)$; the last bar is the coefficient of the left "
            "side. Left: the author's metric, in which ordinary space contributes "
            "$+1$ per direction and the deflating extra times $-1$ each; the sum "
            "and the left side are $0$. Right: a control metric with inflating "
            "extra times; the six contributions add to $6$, matched by the growing "
            "volume factor $e^{6a_4}\\cos z$ on the left side.")
```

Figure 21b.1. **What the figure shows.** Left: three red bars of height $+1$ (space) and three blue bars of height $-1$ (extra times), sum 0, and an empty left-side bar: the deflation cancels the inflation. Right: six red bars, sum 6, and a dark left-side bar of height 6: in a metric whose volume grows, the growth itself supplies the balancing term.

**In [8]: the matrices of the identity as heat maps.**

```python
from matplotlib.colors import TwoSlopeNorm

sample = {a4p: 0.7, a4: 0.3, H: sp.Rational(1, 6), x[7]: 0.5}  # any point
```

`TwoSlopeNorm` maps numbers to colours with the middle colour at a chosen centre value. `sample` is a dictionary of values for a sample point: $a_4' = 0.7$, $a_4 = 0.3$, $H = 1/6$, $x_8 = 0.5$.

```python
def sampled(matrix):
    """matrix / (H cos z) evaluated at the sample point, as numbers."""
    return np.array(sp.N((matrix / (H * sp.cos(z))).subs(a4p, 0.7).subs(sample))
                    .tolist(), dtype=float)
```

The matrix is divided by $H\cos z$; `.subs` replaces symbols by values. The derivative $a_4'$ is replaced first, on its own, because replacing $a_4$ by a number inside the derivative would destroy it. `sp.N` turns the exact result into decimal numbers, and the result is a numpy array.

```python
lhs_num, rhs_num = sampled(lhs), sampled(rhs)
say(f"LHS = RHS at the sample point to 1e-12: "
    f"{np.abs(lhs_num - rhs_num).max() < 1e-12}")
fig, axes = plt.subplots(1, 3, figsize=(12.0, 4.0))
norm = TwoSlopeNorm(vmin=-6, vcenter=0, vmax=6)  # blue negative, red positive
```

Both sides at the sample point; the printed line (True) confirms that they agree to $10^{-12}$. Three panels; the colour scale runs from $-6$ (blue) through $0$ to $+6$ (red).

```python
for ax, matrix, title in ((axes[0], lhs_num, "left side / $(H\\cos z)$"),
                          (axes[1], rhs_num, "right side / $(H\\cos z)$"),
                          (axes[2], 0 * rhs_num, "right side, $\\Omega = 0$")):
    image = ax.imshow(matrix, cmap="RdBu_r", norm=norm)
    ax.set_title(title)
    ax.set_xticks([0, 7, 15], ["1", "8", "16"])
    ax.set_yticks([0, 7, 15], ["1", "8", "16"])
    ax.set_xlabel("column")
    ax.grid(False)
axes[0].set_ylabel("row")
fig.colorbar(image, ax=axes, shrink=0.8, label="matrix entry")
```

The three matrices: the left side, the right side, and the right side without the spin connection (the zero matrix, `0 * rhs_num`). `"RdBu_r"` is matplotlib's red-blue colour map reversed, so that positive numbers are red.

```python
save_figure(fig, "noether_matrices",
            "The $16 \\times 16$ matrices of the U(1) identity in the author's "
            "metric, divided by $H\\cos z$: left side $\\sum_\\mu\\partial_\\mu"
            "(\\cos z\\,C\\gamma^\\mu)$ (left panel), right side $\\cos z\\sum_\\mu"
            "(C\\gamma^\\mu\\Omega_\\mu - \\Omega_\\mu^T(\\gamma^\\mu)^TC)$ (middle) "
            "and the right side of the negative control with the spin connection "
            "removed (right); horizontal axis the column, vertical axis the row, "
            "colour the entry (red positive, blue negative). The first two are the "
            "same matrix $6C\\gamma^{(x8)}$ for every history $a_4$; without the "
            "spin connection the right side would be zero and the current would "
            "not be conserved.")
```

Figure 21b.2. **What the figure shows.** The left and middle panels are identical: sixteen squares of value $\pm6$ arranged like the signed permutation matrix $C\gamma^{(x8)}$. The right panel is empty: without the connection nothing balances the left side.

**In [9]: the Noether current from a local phase change.**

```python
point = {x[7]: 0.7, H: sp.Rational(1, 6)}  # z = 0.7 (H = 1/6, so z = x8)
A4_value, A4_slope = 0.4, 0.25  # a4 and a4' at the point (any values)
```

A point of the author's metric: $x_8 = 0.7$ with $H = 1/6$, so $z = 0.7$; and arbitrary values $a_4 = 0.4$, $a_4' = 0.25$ of the history there.

```python
def at_point(expression):
    """A sympy expression evaluated at the point, as a numpy array of complex."""
    e = expression.subs(a4p, A4_slope).subs(a4, A4_value).subs(point)
    return np.array(sp.N(e).tolist(), dtype=complex) if hasattr(e, "tolist") \
        else complex(sp.N(e))
```

The values are substituted (the derivative first, as in In [8]). If the result is a matrix (it has the method `tolist`; `hasattr` asks this), it becomes a complex numpy array, otherwise a complex number; the backslash continues the line.

```python
Om_num = [at_point(Om) for Om in Omega]  # Omega_mu at the point
f_num = [at_point(v).real for v in f_dfl]  # the scale factors at the point
g_up = [gamma[mu] / f_num[mu] for mu in range(8)]  # gamma^mu at the point
cos_num = np.cos(0.7)
m_val, lam = 0.7, 0.3
```

The spin connection, the scale factors and the curved gammas at the point, the volume factor $\cos 0.7$, and the mass and coupling $m = 0.7$, $\lambda = 0.3$.

```python
rng = np.random.default_rng(2102)  # fixed seed: the same numbers in every run
psi = rng.normal(size=16) + 1j * rng.normal(size=16)  # Psi at the point
dpsi = rng.normal(size=(8, 16)) + 1j * rng.normal(size=(8, 16))  # d_mu Psi
alpha_mu = rng.normal(size=8)  # the slopes d_mu alpha of the phase
```

A random-number generator with the fixed seed 2102 provides a complex field value, eight complex first derivatives (an $8 \times 16$ array, one row per direction) and eight slopes $\alpha_\mu = \partial_\mu\alpha$ of the phase. A Lagrangian density at one point depends only on these numbers.

```python
def lagrangian(p, dp):
    """cos z [ (1/2)(Psibar gamma^mu D_mu Psi - (D_mu Psibar) gamma^mu Psi)
    - m S - (lambda/2) S^2 ] at the point, for the value p and derivatives dp."""
    bar = np.conj(p) @ C  # Psibar = Psi^dagger C
    kinetic = 0
    for mu in range(8):
        D = dp[mu] + Om_num[mu] @ p  # D_mu Psi
        Dbar = np.conj(dp[mu]) @ C - bar @ Om_num[mu]  # D_mu Psibar
        kinetic += (bar @ g_up[mu] @ D - Dbar @ g_up[mu] @ p) / 2
    S = bar @ p
    return cos_num * (kinetic - m_val * S - lam / 2 * S ** 2)
```

The Lagrangian density of the record, term by term: the Dirac adjoint $\bar\Psi = \Psi^\dagger C$ (a row); for each direction $D_\mu\Psi = \partial_\mu\Psi + \Omega_\mu\Psi$ and $D_\mu\bar\Psi = (\partial_\mu\Psi)^\dagger C - \bar\Psi\Omega_\mu$; the kinetic term summed over the eight directions (`+=` adds to the running total); the scalar $S$; and $\cos z\,[\,\text{kinetic} - mS - \tfrac\lambda2S^2\,]$.

```python
phase = np.exp(1j * 0.9)  # e^(i alpha) at the point, alpha = 0.9
L0 = lagrangian(psi, dpsi)
L_const = lagrangian(phase * psi, phase * dpsi)  # constant phase: alpha_mu = 0
L_local = lagrangian(phase * psi, phase * (dpsi + 1j * alpha_mu[:, None] * psi))
J = np.array([-1j * (np.conj(psi) @ C @ g_up[mu] @ psi) for mu in range(8)])
```

Three evaluations: the field as it is; after a constant phase $e^{0.9i}$ (value and derivatives multiplied by it); and after a local phase, whose derivatives are $e^{i\alpha}(\partial_\mu\Psi + i\alpha_\mu\Psi)$ (Section 21.16). `alpha_mu[:, None]` turns the eight slopes into a column, so that the product with the 16 components gives an $8 \times 16$ array, one row per direction. `J` holds the eight components of the current at the point.

```python
say(f"L = {L0.real:+.6f} (imaginary part below 1e-12: {abs(L0.imag) < 1e-12}); "
    f"after a constant phase {L_const.real:+.6f}")
say(f"L' - L = {(L_local - L0).real:+.6f};  -cos z alpha_mu J^mu = "
    f"{(-cos_num * alpha_mu @ J).real:+.6f}")
```

Out [9] prints $\mathcal{L} = -16.780795$ with an imaginary part below $10^{-12}$ (the Lagrangian is real), the same value after a constant phase, and $\mathcal{L}' - \mathcal{L} = +2.348835 = -\cos z\,\alpha_\mu J^\mu$ (`alpha_mu @ J` is the sum $\sum_\mu\alpha_\mu J^\mu$).

```python
check(abs(L0.imag) < 1e-12 and abs(L_const - L0) < 1e-12
      and abs((L_local - L0) - (-cos_num * alpha_mu @ J)) < 1e-12
      and np.allclose(J.imag, 0),
      "L is real and phase invariant; a local phase changes it by -cos z "
      "(d_mu alpha) J^mu with J^mu = -i Psibar gamma^mu Psi real")
```

The four statements to $10^{-12}$, including that all eight current components are real.

**In [10]: the exact solution and local conservation.**

```python
x4, zz = sp.symbols("x4 z", real=True)  # the time and the angle z = x8
Hn, al, m_sol = sp.Rational(1, 6), 1, 2
b_sol = 3 * Hn * (2 * al + 1)  # 3/2
w = sp.sqrt(m_sol ** 2 - b_sol ** 2)  # sqrt(7)/2
M_sol = -m_sol * G[3] + b_sol * G[3] * G[7]
U_sol = sp.cos(w * x4) * sp.eye(16) + sp.sin(w * x4) / w * M_sol  # a real matrix
```

New symbols for the time and the angle (the name `zz` keeps `z` of In [3] intact), the parameters $H = 1/6$, $\alpha = 1$, $m = 2$, and $b = 3/2$, $w = \sqrt7/2$, $M$ and $U$ of Section 21.11, exactly.

```python
chi_values = [(0.62, -0.31), (0.15, 0.88), (-0.47, 0.26), (0.93, -0.05),
              (-0.21, -0.64), (0.38, 0.12), (0.07, -0.93), (-0.85, 0.44),
              (0.51, 0.69), (-0.12, -0.27), (0.29, 0.58), (-0.66, 0.03),
              (0.44, -0.72), (0.81, 0.35), (-0.39, -0.18), (0.24, 0.97)]
chi = sp.Matrix([sp.Rational(round(100 * re), 100) + sp.I * sp.Rational(
    round(100 * im), 100) for re, im in chi_values])  # exact rational entries
Psi = sp.sin(zz) ** al * U_sol * chi
```

Sixteen pairs (real part, imaginary part) with two decimals; `round(100 * re)` makes the whole number of hundredths, and `sp.Rational(..., 100)` the exact fraction, so $\chi$ has exact entries such as $31/50 - 31i/100$. `Psi` is the exact solution $\sin z\,U\chi$.

```python
tan_z = sp.sin(zz) / sp.cos(zz)
E = (G[3] * Psi.diff(x4) + 6 * Hn * tan_z * G[7] * Psi.diff(zz)
     + 3 * Hn * G[7] * Psi - m_sol * Psi)  # the field equation, U = 0
SOLUTION_I = (  # item (i) of the record's formula exact_solutions, word for word
    "(i) U = 0: Psi = Sin[z]^al (Cosh[k x4] + Sinh[k x4]/k M) chi, M = -m g[x4]"
    " + 3 H (2 al + 1) g[x4].g[x8], k^2 = 9 H^2 (2 al + 1)^2 - m^2 (any a4)")
```

The left side of the field equation $E_m[\Psi]$ of Section 21.11 (step 4) with $m = 2$, and the record's text of the solution, word for word, as in Notebook 21a.

```python
check(E.expand() == sp.zeros(16, 1)
      and THEORY["exact_solutions"]["wl"].startswith(SOLUTION_I + "; ")
      and PY_THEORY["exact_solution_family_x4_x8"] == "PASS",
      "the record's exact solution solves the field equation (m = 2)",
      record="Revision/theory/reports/python-field-theory.json, check "
      "exact_solution_family_x4_x8")
```

The solution solves the equation exactly; the record states it as used here; the record's own check passed.

```python
B_s = -sp.I * C_s * G[3]
K8_s = -sp.I * C_s * G[7]
density = sp.cos(zz) * (Psi.H * B_s * Psi)[0, 0]  # cos z J^(x4)
flux = sp.sin(zz) * (Psi.H * K8_s * Psi)[0, 0]  # cos z J^(x8)
divergence = sp.expand(sp.diff(density, x4) + sp.diff(flux, zz))
```

Exact $B$ and $K_8$; `Psi.H` is sympy's conjugate transpose $\Psi^\dagger$. The two densities of Section 21.18, $\cos z\,\Psi^\dagger B\Psi$ and $\sin z\,\Psi^\dagger K_8\Psi$, and the divergence $\partial_4(\ldots) + \partial_z(\ldots)$, the only two terms of the conservation law that do not vanish for this solution.

```python
check(sp.simplify(divergence) == 0
      and PY_THEORY["commuting_current_conservation"] == "PASS",
      "d4(cos z J^(x4)) + dz(cos z J^(x8)) = 0 exactly for the exact solution",
      record="Revision/theory/reports/python-field-theory.json, check "
      "commuting_current_conservation")
```

The divergence simplifies to exactly zero, as Section 21.17 proved in general. (The text cell before this code cell says that "the current has two nonzero components"; precisely, all eight components of this solution's current are nonzero, but only these two enter the conservation law, because the others do not depend on their own coordinate. The computation is unaffected.)

**In [11]: the chirality partner and the density maps.**

```python
Gamma_s = sp.Matrix(Gamma.tolist())
partner = Gamma_s * Psi
E_partner = (G[3] * partner.diff(x4) + 6 * Hn * tan_z * G[7] * partner.diff(zz)
             + 3 * Hn * G[7] * partner + m_sol * partner)  # mass -2
density_p = sp.cos(zz) * (partner.H * B_s * partner)[0, 0]
flux_p = sp.sin(zz) * (partner.H * K8_s * partner)[0, 0]
```

The partner $\Gamma\Psi$, the left side of the field equation with the mass $-2$ (the mass term $-(-2)\Gamma\Psi = +2\Gamma\Psi$), and the partner's two densities.

```python
check(E_partner.expand() == sp.zeros(16, 1)
      and sp.expand(density_p + density) == 0 and sp.expand(flux_p + flux) == 0
      and WL_PAIR["T1_current_primordial_commuting"] == "PASS"
      and PY_PAIR["T1.metric.commuting.current"] == "PASS",
      "Gamma Psi solves the equation with mass -2 and carries the opposite "
      "current: the pair's total current is zero",
      record="Revision/pairing/reports/wolfram-pairing.json, check "
      "T1_current_primordial_commuting")
```

Theorem T1 on this solution (Section 21.19): the partner solves the equation with the reversed mass, and its densities are exactly the negatives of those of $\Psi$; both pairing reports hold the corresponding checks with the verdict PASS.

```python
density_f = sp.lambdify((x4, zz), density, "numpy")
times = np.linspace(0.0, 8.0, 161)
angles = np.linspace(0.0, np.pi / 2, 91)
T, Z = np.meshgrid(times, angles)  # every pair (time, angle)
rho = np.real(density_f(T, Z))  # the charge density of Psi
```

The density becomes a fast function; 161 times from 0 to 8 and 91 angles from 0 to $\pi/2$; `np.meshgrid` makes two arrays that together list every pair (time, angle); `rho` is the density at all of them.

```python
fig, axes = plt.subplots(1, 3, figsize=(13.0, 4.0), sharey=True)
limit = np.abs(rho).max()
for ax, values, title in ((axes[0], rho, "$\\Psi$ (mass $+2$)"),
                          (axes[1], -rho, "$\\Gamma\\Psi$ (mass $-2$)"),
                          (axes[2], rho - rho, "sum of the pair")):
    image = ax.pcolormesh(T, Z, values, cmap="RdBu_r", vmin=-limit, vmax=limit,
                          shading="auto")
    ax.set_title(title)
    ax.set_xlabel("time $x_4$")
axes[0].set_ylabel("angle $z = 6Hx_8$ (brane at $\\pi/2$)")
fig.colorbar(image, ax=axes, shrink=0.85, label="charge density $\\cos z\\,J^{(x4)}$")
```

Three colour maps over the plane of time and angle (`pcolormesh` colours each small cell by its value; the colour scale is symmetric about zero). The partner's map is drawn as `-rho`, which the check above proved equal to its density; the third map is the sum, zero.

```python
save_figure(fig, "charge_density_maps",
            "The charge density $\\cos z\\,J^{(x4)}$ of an exact solution of the "
            "field equation in the author's metric ($H = 1/6$, $\\alpha = 1$, mass "
            "$+2$; left), of its chirality partner $\\Gamma\\Psi$ (a solution with "
            "mass $-2$; middle) and of the pair (right); horizontal axis the time "
            "$x_4$, vertical axis the angle $z = 6Hx_8$ from the tip $0$ to the "
            "brane $\\pi/2$, colour the density (red positive, blue negative, pure "
            "numbers). The partner carries exactly the opposite density at every "
            "point, so the pair carries none.")
```

Figure 21b.3. **What the figure shows.** Left: for this column the density is mostly negative: dark blue bands, separated by faint red ones, repeat in time with the oscillation of the solution (period about 2.37), and every band fades out towards the tip $z = 0$ (the factor $\sin^2z$) and towards the brane $z = \pi/2$ (the factor $\cos z$). Middle: the same picture with red and blue exchanged. Right: a uniform pale panel: the pair's density is zero everywhere.

**In [12]: the charge balance and the stationary solution.**

```python
t = sp.symbols("t", real=True)
f_of = sp.expand((U_sol * chi).H * B_s * (U_sol * chi))[0, 0]  # f(x4)
g_of = sp.expand((U_sol * chi).H * K8_s * (U_sol * chi))[0, 0]  # g(x4)
Q_of = f_of / 3
```

The functions $f(x_4) = \chi^\dagger U^TBU\chi$ and $g(x_4) = \chi^\dagger U^TK_8U\chi$ of Section 21.18 (the conjugate transpose of the real $U$ times $\chi$ is $\chi^\dagger U^T$), and the charge $Q = f/3$.

```python
balance = sp.simplify(Q_of - Q_of.subs(x4, 0)
                      + sp.integrate(g_of.subs(x4, t), (t, 0, x4)))
check(balance == 0, "charge balance: Q(x4) - Q(0) = - (flux through the brane), "
      "exactly")
```

`sp.integrate(g_of.subs(x4, t), (t, 0, x4))` is the exact integral $\int_0^{x_4}g(t)\,dt$ (the variable renamed to $t$). The balance $Q(x_4) - Q(0) + \int_0^{x_4}g = 0$ holds exactly.

```python
P_stat = (sp.eye(16) - sp.I * M_sol / w) / 2  # projector onto M chi = i w chi
chi0 = P_stat * chi  # the single-frequency part of chi
g0 = sp.simplify(sp.expand((U_sol * chi0).H * K8_s * (U_sol * chi0))[0, 0])
Q0 = sp.simplify(sp.expand((U_sol * chi0).H * B_s * (U_sol * chi0))[0, 0] / 3)
```

The projector $P = \tfrac12(1 - iM/w)$, the stationary column $\chi_0 = P\chi$, its flux function $g_0$ and its charge $Q_0$.

```python
check((P_stat * P_stat - P_stat).applyfunc(sp.simplify) == sp.zeros(16, 16)
      and (M_sol * chi0 - sp.I * w * chi0).applyfunc(sp.simplify) == sp.zeros(16, 1)
      and g0 == 0 and Q0.free_symbols == set() and Q0 != 0,
      "the stationary solution sin z exp(i w x4) chi0: zero flux, constant nonzero Q")
```

$P^2 = P$; $M\chi_0 = iw\chi_0$; the flux is exactly zero; `Q0.free_symbols == set()` means that $Q_0$ contains no symbol at all, so it does not depend on the time; and it is not zero.

```python
report("charge of the general solution at x4 = 0",
       f"{float(sp.re(Q_of.subs(x4, 0))):.6f}")
report("constant charge of the stationary solution", f"{Q0} = {float(Q0):.6f}")
```

Out [12] prints RESULT lines: $Q(0) = 0.178467$ for the general column and $Q_0 = -1424/1875 - 13\sqrt7/1500 = -0.782397$ (sympy writes the square root as `sqrt(7)`).

**In [13]: the balance in a figure.**

```python
Q_f = sp.lambdify(x4, Q_of, "numpy")
g_f = sp.lambdify(x4, g_of, "numpy")
integral_f = sp.lambdify(x4, sp.integrate(g_of.subs(x4, t), (t, 0, x4)), "numpy")
Q_vals = np.real(Q_f(times))
rhs_vals = np.real(Q_f(0.0) - integral_f(times))
```

Fast functions for the charge, the flux and its integral; the charge at the 161 times and the prediction $Q(0) - \int_0^{x_4}g$.

```python
fig, axes = plt.subplots(1, 2, figsize=(12.0, 4.3))
axes[0].plot(times, Q_vals, linewidth=3, label="charge $Q(x_4)$ of the patch")
axes[0].plot(times, rhs_vals, "--", color="black",
             label="$Q(0) - \\int_0^{x_4}$ flux")
axes[0].plot(times, np.real(g_f(times)), ":", label="flux $g(x_4)$ through the brane")
axes[0].set_xlabel("time $x_4$")
axes[0].set_ylabel("charge, flux (pure numbers)")
axes[0].set_title("General solution: charge flows through the brane")
```

The left panel: the charge as a thick line, the prediction as a thin black dashed line on top of it, and the flux as a dotted line.

```python
top = 1.9 * np.abs(np.real(g_f(times))).max()  # room for the legend above
axes[0].set_ylim(-1.2 * np.abs(np.real(g_f(times))).max(), top)
axes[0].legend(fontsize=8, loc="upper right")
```

The vertical range is set from $-1.2$ to $1.9$ times the largest flux, which leaves room for the legend at the top.

```python
Q0_value = float(Q0)
axes[1].plot(times, np.full_like(times, Q0_value), linewidth=2,
             label="$Q$ of $\\Psi$ (mass $+2$)")
axes[1].plot(times, np.full_like(times, -Q0_value), "--", linewidth=2,
             label="$Q$ of $\\Gamma\\Psi$ (mass $-2$)")
axes[1].plot(times, np.zeros_like(times), ":", color="black", linewidth=2,
             label="total charge of the pair")
axes[1].set_xlabel("time $x_4$")
axes[1].set_title("Zero flux: the charge is constant")
axes[1].set_ylim(-1.3 * abs(Q0_value), 2.2 * abs(Q0_value))  # legend fits on top
axes[1].legend(fontsize=8, loc="upper right")
```

The right panel: three constant lines (`np.full_like(times, value)` is an array of the same length filled with one value): the stationary charge, the partner's opposite charge (Section 21.19) and the pair's zero total.

```python
check(np.max(np.abs(Q_vals - rhs_vals)) < 1e-12,
      "numerically: Q(x4) and Q(0) minus the integrated flux agree to 1e-12")
```

The balance holds to $10^{-12}$ at all 161 times.

```python
save_figure(fig, "charge_balance",
            "The charge balance of exact solutions in the author's metric ($H = "
            "1/6$, $\\alpha = 1$, mass $2$). Left: for a general column $\\chi$, "
            "the charge $Q(x_4)$ of the patch $0 < z < \\pi/2$ (thick line), the "
            "prediction $Q(0) - \\int_0^{x_4} g$ of the conservation law (dashed, "
            "on top of it) and the flux $g$ through the brane (dotted), versus the "
            "time $x_4$. Right: for the stationary solution $\\sin z\\,e^{iwx_4}"
            "\\chi_0$ the flux vanishes, its charge is constant, its chirality "
            "partner "
            "carries the opposite constant charge and the pair carries none. All "
            "quantities per unit of the other six coordinates (pure numbers).")
```

Figure 21b.4. **What the figure shows.** Left: the charge rises and falls; wherever the flux (dotted) is positive the charge decreases and wherever it is negative the charge increases, and the dashed prediction lies exactly on the thick line. Right: two horizontal lines at $\mp0.782397$ and the zero line between them.

**In [14]: a finite-difference test.**

```python
flux_f = sp.lambdify((x4, zz), flux, "numpy")
steps = 0.2 / 2.0 ** np.arange(7)  # 0.2, 0.1, ..., 0.003125
t0, z0 = 1.3, 0.7
```

The flux as a fast function; seven steps $h$ that halve each time; the test point $(x_4, z) = (1.3, 0.7)$.

```python
residuals = np.array([abs(np.real(
    (density_f(t0 + h, z0) - density_f(t0 - h, z0)) / (2 * h)
    + (flux_f(t0, z0 + h) - flux_f(t0, z0 - h)) / (2 * h))) for h in steps])
ratios = residuals[:-1] / residuals[1:]
```

For each step the divergence is computed with **central differences**, $\partial F \approx (F(x + h) - F(x - h))/(2h)$, whose error is proportional to $h^2$ (Chapter 2). `residuals[:-1] / residuals[1:]` divides each residual by the next one (`[:-1]` is all but the last, `[1:]` all but the first).

```python
say("residuals: " + ", ".join(f"{r:.2e}" for r in residuals))
say("ratios when h is halved: " + ", ".join(f"{q:.3f}" for q in ratios))
check(np.all(np.abs(ratios - 4.0) < 0.05),
      "finite differences: the residual falls by 4 when h is halved (order 2)")
```

Out [14] prints the residuals from $3.68 \times 10^{-3}$ down to $9.10 \times 10^{-7}$ (`.2e` is scientific notation with two decimals) and the ratios 3.966, 3.991, 3.998, 3.999, 4.000, 4.000: halving $h$ divides the residual by 4, the signature of order 2 converging to the exact value zero.

```python
fig, ax = plt.subplots(figsize=(7.0, 4.4))
ax.loglog(steps, residuals, "o-", label="|central-difference divergence|")
ax.loglog(steps, residuals[0] * (steps / steps[0]) ** 2, "--",
          label="slope 2: proportional to $h^2$")
ax.set_xlabel("step $h$")
ax.set_ylabel("residual of the conservation law")
ax.set_title("A numerical test converges to the exact law")
ax.legend()
```

A plot with both axes logarithmic (`loglog`), the residuals and a reference line proportional to $h^2$ through the first point.

```python
save_figure(fig, "local_conservation",
            "The local conservation law $\\partial_4(\\cos z\\,J^{(x4)}) + "
            "\\partial_z(\\cos z\\,J^{(x8)}) = 0$ tested with central differences "
            "of step $h$ at the point $x_4 = 1.3$, $z = 0.7$ for the exact solution "
            "of the author's metric; horizontal axis the step $h$, vertical axis "
            "the size of the computed divergence, both on logarithmic scales "
            "(pure numbers). The points follow the dashed line of slope 2: the "
            "error of the difference formula, proportional to $h^2$, is all there "
            "is; the exact divergence is zero.")
```

Figure 21b.5. **What the figure shows.** Seven points on a straight line of slope 2, lying on the dashed reference line: what a computer measures as a nonzero divergence is only the error of the difference formula.

**In [15]: the charge while the extra times deflate.**

```python
a4_vals = times / 6.0  # a4 = A H x4 with A = 1, H = 1/6
fig, axes = plt.subplots(2, 1, figsize=(8.0, 6.4), sharex=True)
axes[0].semilogy(times, np.exp(a4_vals), label="ordinary space: $e^{a_4}$")
axes[0].semilogy(times, np.exp(-a4_vals), "--",
                 label="extra times $x5, x6, x7$: $e^{-a_4}$ (deflating)")
axes[0].semilogy(times, np.exp(3 * a4_vals) * np.exp(-3 * a4_vals), ":",
                 color="black", label="slice volume $e^{3a_4}e^{-3a_4} = 1$")
```

The linear history $a_4 = AHx_4$ with $A = 1$ and $H = 1/6$, chosen only for the picture. Two panels stacked vertically with a common time axis; the upper one draws, on a logarithmic axis, the growth factor of space, the shrinking factor of the extra times and the product of the cubes, which is exactly 1.

```python
axes[0].set_ylabel("scale factor (log scale)")
axes[0].set_title("The history $a_4 = AHx_4$ ($A = 1$, $H = 1/6$)")
axes[0].legend(fontsize=8)
axes[1].plot(times, np.full_like(times, Q0_value), linewidth=2,
             label="charge $Q$ of the stationary solution")
axes[1].set_ylim(-1.5 * abs(Q0_value), 1.5 * abs(Q0_value))
axes[1].axhline(0.0, color="black", linewidth=0.8)
axes[1].set_xlabel("time $x_4$")
axes[1].set_ylabel("charge $Q$")
axes[1].legend(fontsize=8)
```

Labels and legend of the upper panel; the lower panel draws the constant charge of the stationary solution and the zero line.

```python
save_figure(fig, "charge_through_deflation",
            "Top: the scale factors of the author's metric along the time $x_4$ "
            "for the linear history $a_4 = AHx_4$ with $A = 1$, $H = 1/6$ "
            "(chosen for the picture): ordinary space $e^{a_4}$ grows, the three "
            "extra times $e^{-a_4}$ deflate exponentially, and their product, the "
            "volume factor of a slice, stays $1$ (logarithmic vertical scale). "
            "Bottom: the charge $Q$ of the stationary exact solution versus $x_4$; "
            "it does not change while space inflates and the extra times deflate. "
            "The U(1) identity was verified for every history $a_4$, so the "
            "constancy does not depend on this choice.")
```

Figure 21b.6. **What the figure shows.** Top: two straight lines on the logarithmic scale, one rising and one falling at the same rate, and a flat dotted line at 1 between them. Bottom: a flat line at $-0.782$: the charge is untouched by the deflation.

**In [16]: the charge density is indefinite.**

```python
from fractions import Fraction

eig_B = np.linalg.eigvalsh(B)
plus_space = (I16 - 1j * gamma[3]) / 2  # projector onto -i gamma^(x4) = +1
```

`Fraction` (a Python module for exact fractions) is used to print the result. `np.linalg.eigvalsh` computes the eigenvalues of a Hermitian matrix in increasing order. `plus_space` is $\tfrac12(1 + (-i\gamma^{(x4)}))$, the projector onto the eigenvectors of $-i\gamma^{(x4)}$ with eigenvalue $+1$ (the rest states of Section 21.18).

```python
# B restricted to that space: an 8-dimensional block, eigenvalues +-1
values, vectors = np.linalg.eigh(plus_space @ B @ plus_space)
u_plus = vectors[:, np.argmax(values)]  # a vector with -i g4 u = u, B u = +u
u_minus = vectors[:, np.argmin(values)]  # a vector with -i g4 u = u, B u = -u
```

`np.linalg.eigh` returns the eigenvalues and an orthonormal set of eigenvectors (the columns of `vectors`). The matrix $PBP$ has the eigenvalues of $B$ restricted to the rest-state space and zeros elsewhere; `np.argmax` and `np.argmin` give the positions of the largest ($+1$) and smallest ($-1$) eigenvalue, and `vectors[:, k]` is column `k`.

```python
u = 0.6 * u_plus + 0.8 * u_minus  # 3/5 and 4/5
rest_density = np.conj(u) @ B @ u
restricted = np.linalg.eigvalsh(plus_space @ B @ plus_space)
```

The worked example $u = \tfrac35u_+ + \tfrac45u_-$, its charge density $u^\dagger Bu$, and the eigenvalues of $PBP$ once more for the check.

```python
check(np.allclose(sorted(eig_B), [-1] * 8 + [1] * 8)
      and np.allclose(-1j * gamma[3] @ u, u)
      and np.sum(restricted > 0.5) == 4 and np.sum(restricted < -0.5) == 4
      and abs(rest_density - (-7 / 25)) < 1e-12,
      "B has signature (8,8); a positive-frequency rest state has charge density "
      "-7/25")
report("charge density of the rest state 3/5 u+ + 4/5 u-",
       Fraction(round(rest_density.real * 25), 25))
```

$B$ has eight eigenvalues $-1$ and eight $+1$; $u$ is a rest state; the restricted block has four eigenvalues $+1$ and four $-1$ (`np.sum` of a true-false array counts the trues); the density is $-7/25$. The RESULT line prints the density as the exact fraction $-7/25$ (25 times the density, rounded to a whole number, over 25).

```python
samples = rng.normal(size=(20000, 16)) + 1j * rng.normal(size=(20000, 16))
ratio = (np.einsum("nr,rc,nc->n", np.conj(samples), B, samples).real
         / np.einsum("nr,nr->n", np.conj(samples), samples).real)
say(f"fraction of random columns with negative charge density: "
    f"{np.mean(ratio < 0):.3f}")
```

20000 random complex columns (from the generator of In [9], which continues its sequence). For each, `einsum` computes $\Psi^\dagger B\Psi$ and $\Psi^\dagger\Psi$, and `ratio` is their quotient. `np.mean(ratio < 0)` is the fraction of negative ones: Out [16] prints 0.504.

```python
check(ratio.min() >= -1 - 1e-12 and ratio.max() <= 1 + 1e-12
      and 0.4 < np.mean(ratio < 0) < 0.6,
      "random columns: the ratio lies in [-1, 1] and takes both signs")
fig, ax = plt.subplots(figsize=(7.5, 4.3))
ax.hist(ratio, bins=60, range=(-1, 1), color="#7a8fb3")
ax.axvline(-7 / 25, color="#e34948", linewidth=2,
           label="rest state with positive frequency: $-7/25$")
ax.set_xlabel("$\\Psi^\\dagger B\\Psi / \\Psi^\\dagger\\Psi$")
ax.set_ylabel("number of random columns")
ax.set_title("The charge density is indefinite")
ax.legend(fontsize=8)
```

The ratio lies between $-1$ and $+1$ (Section 21.18) and is negative for between 40 and 60 per cent of the columns. `ax.hist` draws a **histogram**: the interval from $-1$ to $1$ is cut into 60 bins and each bar counts the columns whose ratio falls into it. A red vertical line marks $-7/25$.

```python
save_figure(fig, "indefinite_charge",
            "Histogram of the normalised charge density $\\Psi^\\dagger B\\Psi / "
            "\\Psi^\\dagger\\Psi$ for 20000 random complex columns $\\Psi$ (fixed "
            "seed); horizontal axis the ratio, from $-1$ to $+1$, vertical axis the "
            "number of columns in each of 60 bins. Because $B$ has eight "
            "eigenvalues $+1$ and eight $-1$, the ratio takes both signs equally "
            "often. The red line marks the worked example: a flat-space rest "
            "state of positive frequency with charge density $-7/25$.")
```

Figure 21b.7. **What the figure shows.** A bell-shaped histogram centred at zero and symmetric: the charge density of a random field is positive or negative with equal probability, and the red line shows that a field of positive frequency can lie on the negative side.

**In [17]: the pair-level bookkeeping.**

```python
U_f = sp.lambdify(x4, U_sol, "numpy")
columns = rng.normal(size=(5, 16)) + 1j * rng.normal(size=(5, 16))
check_times = [0.0, 2.5, 5.0]
totals, charges = [], []
```

The matrix $U(x_4)$ as a fast function, five random complex columns $\chi$, three test times, and two empty lists.

```python
for col in columns:
    u_t = [np.array(U_f(tt), dtype=float) @ col for tt in check_times]
    q_psi = [np.conj(v) @ B @ v / 3 for v in u_t]  # Q = f / 3 for alpha = 1
    q_par = [np.conj(Gamma @ v) @ B @ (Gamma @ v) / 3 for v in u_t]
    charges.append((q_psi[0].real, q_par[0].real))
    totals += [abs(a + b_) for a, b_ in zip(q_psi, q_par)]
```

For each column and each time, $v = U(x_4)\chi$ and the charge $Q = v^\dagger Bv/3$ of the solution $\sin z\,U\chi$ (Section 21.18, line 1), and the charge of the partner $\Gamma v$. The charges at the first time are kept for the figure; the sizes of the totals $Q + Q'$ are collected.

```python
check(max(totals) < 1e-12 and min(abs(c[0]) for c in charges) > 1e-3,
      "five random columns at three times: Q + Q(partner) = 0, Q itself nonzero")
```

All 15 totals vanish to $10^{-12}$, while every single charge is far from zero.

```python
fig, ax = plt.subplots(figsize=(8.0, 4.3))
idx = np.arange(5)
ax.bar(idx - 0.25, [c[0] for c in charges], width=0.25, label="$Q$ of $\\Psi$")
ax.bar(idx, [c[1] for c in charges], width=0.25, label="$Q$ of $\\Gamma\\Psi$")
ax.plot(idx + 0.25, [c[0] + c[1] for c in charges], "D", color="black",
        label="total of the pair (zero)")
ax.axhline(0.0, color="black", linewidth=0.8)
ax.set_xticks(idx, [f"column {k + 1}" for k in idx])
ax.set_ylabel("charge $Q$ at $x_4 = 0$")
ax.set_title("Theorem T1: the partner carries the opposite charge")
ax.legend(fontsize=8)
```

For each column two bars (the charges of $\Psi$ and of $\Gamma\Psi$) and a black diamond (`"D"`) at their total.

```python
save_figure(fig, "pair_bookkeeping",
            "Pair-level charge bookkeeping for five random columns $\\chi$ in the "
            "exact solution of the author's metric: the charge $Q$ of $\\Psi$ "
            "(left bar of each group), of its chirality partner $\\Gamma\\Psi$, a "
            "solution with the mass reversed (right bar), and their total (black "
            "diamond, zero); horizontal axis the column, vertical axis the charge at "
            "$x_4 = 0$ per unit of the other six coordinates (pure numbers). The "
            "charges of single universes can have either sign and any size; only "
            "the pair adds to zero.")
```

Figure 21b.8. **What the figure shows.** Pairs of bars of equal height and opposite sign, some positive first and some negative first, and five diamonds on the zero line: the pair-level statement of theorem T1. The figure shows a property of pairs of solutions; it does not show that such pairs are made (Section 21.19).

**In [18]: the figure files.**

```python
names = sorted(FIGURE_NUMBERS, key=FIGURE_NUMBERS.get)
check(len(names) == 8 and all(
    output_file(f"{FIGURE_FOLDER}/21b_{FIGURE_NUMBERS[n]}_{n}.png").is_file()
    for n in names), "the eight figure files of notebook 21b exist")
all_checks_passed()
```

As in the last cell of Notebook 21a: the eight figure files exist, and the last line prints ALL 21 CHECKS PASSED (notebook 21b).

### 21.24 Reflections and the chirality: P, T and $\Gamma$

Sakharov's second condition speaks of C, P and T. Sections 21.8 to 21.10 found the matrices of charge conjugation. This section collects what the Revision record proves about the reflections, which play the roles of P and T, and about the chirality $\Gamma$. All statements are from the pairing record (`Revision/docs/PAIR_CREATION_PROOFS.md`, its sections 3 and 5; Chapter 18 gives the complete proofs); the one-line derivations are repeated here.

**Reflections.** The reflection $R_n$ of a frame direction $n$ reverses that direction and keeps the others: it is the diagonal matrix with $-1$ in place $n$ and $+1$ elsewhere. Reflecting a space-like direction ($x_1, x_2, x_3$ or $x_8$) is a **parity**-type operation (P); reflecting the time $x_4$ is **time reversal** (T); reflecting an extra time $x_5, x_6, x_7$ is a time-reversal-type operation of an extra time. On the spinor, the reflection of the direction $n$ is carried by the matrix $P_n = \Gamma\gamma^{(n)}$, which is plus or minus the product of the seven other gammas, hence an element of Pin(4,4) (record check `T2_Pn_in_Pin44`), and which acts on the gammas exactly as $R_n$ (check `T2_Pn_covers_the_reflection`).

**What a reflection does to the scalar**, in one line. With the real matrix $\gamma^{(n)}$ (so $(\gamma^{(n)})^\dagger = (\gamma^{(n)})^T$) and (R3) in the form $(\gamma^a)^TC = -C\gamma^a$:

$$
S[\gamma^{(n)}\Psi] = \Psi^\dagger(\gamma^{(n)})^TC\gamma^{(n)}\Psi = -\Psi^\dagger C\gamma^{(n)}\gamma^{(n)}\Psi = -\eta_{nn}\,S[\Psi] ,
$$

because $\gamma^{(n)}\gamma^{(n)} = \eta_{nn}$. So a space-like reflection reverses the mass term and a time-like one keeps it. The record also proves (checks `T2_kernels_gamma_n_with_frame_reflection` of the Wolfram pairing report and `T2.general_field.reflection_table` of the sympy pairing report) that the kinetic term is multiplied by $+\eta_{nn}$ when the frame is reflected along. The result for the eight directions:

| direction | $\eta_{nn}$ | $S$ under $\gamma^{(n)}$ | kinetic term | parameters and Lagrangian |
| --- | --- | --- | --- | --- |
| $x_1$, $x_2$, $x_3$ (P type) | $+1$ | $-S$ | kept | $(-m, \lambda)$, $+\mathcal{L}$ (T2 type) |
| $x_4$ (T) | $-1$ | $+S$ | reversed | $(-m, -\lambda)$, $-\mathcal{L}$ (T1 type) |
| $x_5$, $x_6$, $x_7$ | $-1$ | $+S$ | reversed | $(-m, -\lambda)$, $-\mathcal{L}$ (T1 type) |
| $x_8$ (P type) | $+1$ | $-S$ | kept | $(-m, \lambda)$, $+\mathcal{L}$ (T2 type) |

Every reflection maps the theory with mass $m$ to a theory with mass $-m$. In the author's metric only the reflection of $x_8$ is realised by a map of the space onto itself, the mirror across the brane $z = \pi/2$, and that uses the ASSUMED Z2 construction (theorem T2 of the record; Chapter 18); the reflections of $x_1, x_2, x_3$ are statements about frames. For a space-like reflection the charge density is unchanged (record, statement T2c), so the T2 partner has equal, not opposite, charge.

**The chirality.** $\Gamma$ is the product of all eight gammas, the spinor image of reflecting all eight directions at once. It keeps $S$ and reverses every kinetic term and every current (Sections 21.10 and 21.19): theorem T1.

**The Krein signs.** After quantisation the matrix $B$ fixes the canonical anticommutator (Section 21.25). A constant map $\Psi \to M\Psi$ turns it into $MBM^\dagger$, and the record proves $MBM^\dagger = \sigma_MB$ with a sign $\sigma_M$ (check `Q_Krein_metric_of_images`). For the chirality, line by line: $\Gamma B\Gamma^\dagger = \Gamma B\Gamma = -iC\Gamma\gamma^{(x4)}\Gamma = -iC(-\gamma^{(x4)}) = -B$ ($\Gamma$ is real and symmetric; it commutes with $C$, (R2), and anticommutes with $\gamma^{(x4)}$, (R1)). So $\sigma_\Gamma = -1$: the chirality image of a quantised field carries the Krein metric $-B$. For the single gammas the record finds $\sigma = +1$ for $x_1, x_2, x_3, x_4, x_8$ and $-1$ for $x_5, x_6, x_7$.

| statement | status | where it is verified |
| --- | --- | --- |
| $P_n = \Gamma\gamma^{(n)}$ is in Pin(4,4) and covers the reflection $R_n$ | PROVED | `Revision/pairing/reports/wolfram-pairing.json`, checks `T2_Pn_in_Pin44`, `T2_Pn_covers_the_reflection` |
| $S[\gamma^{(n)}\Psi] = -\eta_{nn}S$; the table of the eight reflections | PROVED | the same report, `T2_character_of_Pn`, `T2_kernels_gamma_n_with_frame_reflection`; `Revision/pairing/reports/python-pairing.json`, `T2.general_field.reflection_table` |
| $\Gamma B\Gamma = -B$ and the Krein signs of the reflections | PROVED | `Revision/pairing/reports/wolfram-pairing.json`, check `Q_Krein_metric_of_images` |

### 21.25 The quantised field: which conjugation keeps the canonical anticommutator

**From numbers to operators.** After **canonical quantisation** (Chapter 10) the 16 components of the field dirac16complex are no longer numbers but **operators** $\Psi_A$, $A = 1, \dots, 16$: rules that turn one state of the quantum system into another. Two operators need not commute. The **anticommutator** of two operators is $\{X, Y\} = XY + YX$. The Revision record (`Revision/theory/field-theory.json`, formula `quantisation`) fixes, on a slice of constant time $x_4$,

$$
\{\Psi_A(x), \Psi^\dagger_C(y)\} = B_{AC}\,\delta^7(x - y)/\cos z,\qquad \{\Psi_A(x), \Psi_C(y)\} = 0 ,
$$

the **canonical anticommutator**, which the Lagrangian dictates. Because $B$ has eight negative eigenvalues, $\Psi^\dagger$ cannot be the ordinary (Hilbert) adjoint of $\Psi$: the state space carries an indefinite form, a **Krein space**. The record realises the rule in the **positive representation** $\Psi_A = b_A$, $\Psi^\dagger_C = \sum_Db^\ast_DB_{DC}$, where $b_A$ and $b^\ast_A$ are ordinary fermion operators (Section 21.26). In this section the delta function plays no role and is left out: everything is said for one point.

**The question.** Charge conjugation of the quantised field must turn $\Psi$ into a new field built from the adjoints, $\Psi' = M\Psi^{\dagger T}$, that is $\Psi'_A = \sum_BM_{AB}\Psi^\dagger_B$ with a constant matrix $M$. For $\Psi'$ to be a field of the **same** quantum theory it must obey the **same** canonical rule.

**The condition**, line by line. The adjoint of $\Psi'_C$ is $\Psi'^\dagger_C = \sum_DM^\ast_{CD}\Psi_D$ (the adjoint of a number times an operator conjugates the number; the adjoint of $\Psi^\dagger$ is $\Psi$).

*Line 1.* $\{\Psi'_A, \Psi'^\dagger_C\} = \sum_{B,D}M_{AB}M^\ast_{CD}\{\Psi^\dagger_B, \Psi_D\}$ (the anticommutator is linear in each of its two slots).

*Line 2.* $\{\Psi^\dagger_B, \Psi_D\} = \{\Psi_D, \Psi^\dagger_B\} = B_{DB} = (B^T)_{BD}$ (the anticommutator is symmetric, $XY + YX = YX + XY$; then the canonical rule).

*Line 3.* So $\{\Psi'_A, \Psi'^\dagger_C\} = \sum_{B,D}M_{AB}(B^T)_{BD}(M^\dagger)_{DC} = (MB^TM^\dagger)_{AC}$ (the definition of the matrix product, with $M^\ast_{CD} = (M^\dagger)_{DC}$).

*Line 4.* $\Psi'$ obeys the canonical rule if and only if

$$
MB^TM^\dagger = B .
$$

**Which $M$ satisfy it.** $B$ is Hermitian and purely imaginary, so $B^T = (B^\dagger)^\ast = B^\ast = -B$. For $M = \Gamma$: $\Gamma B^T\Gamma^\dagger = -\Gamma B\Gamma = -(-B) = B$ (Section 21.24): **the condition holds**. For $M = 1$: $B^T = -B \ne B$: **it fails**. More generally, for the family $M(t) = \cos t\,1 + \sin t\,\Gamma$, which is real and symmetric:

$$
M(t)\,B^T M(t)^\dagger = -M(t)BM(t) = -\big(\cos^2t\,B + \cos t\sin t\,(\Gamma B + B\Gamma) + \sin^2t\,\Gamma B\Gamma\big)
$$

(the product multiplied out). $\Gamma$ anticommutes with $B$ ($\Gamma$ commutes with $C$ and anticommutes with $\gamma^{(x4)}$), so the middle term vanishes, and $\Gamma B\Gamma = -B$. Hence

$$
M(t)\,B^TM(t)^\dagger = -(\cos^2t - \sin^2t)\,B = -\cos(2t)\,B ,
$$

which equals $B$ only when $\cos 2t = -1$, that is $t = \pi/2$ or $3\pi/2$: $M = \pm\Gamma$. The size of the failure is $\lvert1 + \cos 2t\rvert$ times the size of $B$, which is 4 (the square root of the sum of the squares of its 16 entries of modulus 1); at $t = 0$ it is 8. A multiple $c\,\Gamma$ gives $\lvert c\rvert^2B$, so it works exactly when $\lvert c\rvert = 1$, a phase. Notebook 21c computes all of this (In [4], figure 21c.2), reproducing the lead check `quantum_charge_conjugation_unitary_type`.

**Which mass?** A conjugation must also map solutions to solutions. By Theorem CC the only constant matrices that do so are the multiples of $1$ (same mass) and of $\Gamma$ (mass reversed). So for the quantised field **the only conjugation that keeps the canonical anticommutator is $\Psi \to \Gamma\Psi^{\dagger T}$ (times a phase), and it reverses the mass.** The same-mass candidate $\Psi \to \Psi^{\dagger T}$ would turn $B$ into $-B$.

### 21.26 Particles and holes; the mass reversed, the spectra equal

**Fermion modes from zero.** A **fermion mode** is a place that holds at most one particle: it is either empty (0) or occupied (1). Sixteen modes have $2^{16} = 65536$ states, one for each list of 16 zeros and ones. The **annihilation operator** $b_j$ empties mode $j$ (and gives zero if it is already empty); the **creation operator** $b_j^\ast$ fills it (and gives zero if it is already full). To make operators of different modes anticommute, each action on mode $j$ also multiplies by $(-1)$ raised to the number of occupied modes before $j$ (the **Jordan-Wigner** sign rule). With it, $\{b_j, b_k^\ast\} = \delta_{jk}$ and $\{b_j, b_k\} = 0$. The number operator $b_j^\ast b_j$ is 1 on states where mode $j$ is occupied and 0 otherwise, and $N = \sum_jb_j^\ast b_j$ counts the occupied modes. Notebook 21c builds these operators explicitly on all 65536 states (In [5]).

**The charge counts the occupied modes.** In the positive representation the charge operator is

$$
Q = \sum_{A,C}\Psi^\dagger_AB_{AC}\Psi_C = \sum_{A,C,D}b^\ast_DB_{DA}B_{AC}b_C = \sum_{D,C}b^\ast_D(B^2)_{DC}b_C = \sum_Db^\ast_Db_D = N
$$

(insert $\Psi^\dagger_A = \sum_Db^\ast_DB_{DA}$ and $\Psi_C = b_C$; the sum over $A$ is a matrix product; $B^2 = 1$).

**The charge of the conjugated field**, line by line, for $\Psi' = \Gamma\Psi^{\dagger T}$. Since $\Gamma$ is diagonal and real, $\Psi'_C = \Gamma_{CC}\Psi^\dagger_C$ and $\Psi'^\dagger_A = \Gamma_{AA}\Psi_A$.

*Line 1.* $Q' = \sum_{A,C}\Psi'^\dagger_AB_{AC}\Psi'_C = \sum_{A,C}\Gamma_{AA}B_{AC}\Gamma_{CC}\,\Psi_A\Psi^\dagger_C = \sum_{A,C}(\Gamma B\Gamma)_{AC}\Psi_A\Psi^\dagger_C$ (insert; the numbers $\Gamma_{AA}$ and $\Gamma_{CC}$ commute with the operators; for a diagonal $\Gamma$, $\Gamma_{AA}B_{AC}\Gamma_{CC} = (\Gamma B\Gamma)_{AC}$).

*Line 2.* $\Gamma B\Gamma = -B$ (Section 21.24), so $Q' = -\sum_{A,C}B_{AC}\Psi_A\Psi^\dagger_C$.

*Line 3.* The canonical rule gives $\Psi_A\Psi^\dagger_C = B_{AC} - \Psi^\dagger_C\Psi_A$, so $Q' = -\sum_{A,C}B_{AC}^2 + \sum_{A,C}\Psi^\dagger_C(B^T)_{CA}\Psi_A$ (with $B_{AC} = (B^T)_{CA}$).

*Line 4.* $\sum_{A,C}B_{AC}^2 = \mathrm{tr}(BB^T) = \mathrm{tr}(B(-B)) = -\mathrm{tr}(B^2) = -16$, and $B^T = -B$ turns the second sum into $-Q$. Hence

$$
Q' = 16 - Q .
$$

The valid conjugate counts the **empty** modes. Up to the constant 16, which does not change any difference of charges, it **reverses the charge**: $Q' - 8 = -(Q - 8)$. Particles and holes are exchanged. The same four lines with $M = 1$ (no factors $\Gamma$, so no sign in line 2) give $Q'' = \sum_{A,C}B_{AC}\Psi_A\Psi^\dagger_C = -16 + Q$: the invalid same-mass candidate would not even reverse the charge, it would shift it. Notebook 21c checks these three operator identities on a random state of the 16 modes (In [8], figure 21c.4). This operator result is the quantum counterpart of the anticommuting rows of the table of Section 21.10: the valid conjugation reverses the charge and the mass; the same-mass candidate keeps the charge (up to a shift). It does not support the parenthetical remark of the record's check `bilinears_under_charge_conjugation` that normal ordering would give the same-mass candidate the standard sign (Section 21.10).

**The mass is reversed, the spectra are equal.** In flat 4+4 space ($H = 0$, $a_4$ constant) a plane wave $u\,e^{ik\cdot x}$, with the momenta $k_a$ along the seven directions other than the time, evolves by $i\,\partial_4u = h_m(k)u$ with the **one-particle Hamiltonian** of the record

$$
h_m(k) = -im\gamma^{(x4)} - \gamma^{(x4)}\sum_{a \ne x4}k_a\gamma^{(a)} .
$$

Four facts, each derived in a few lines (write $K = \sum_{a \ne x4}k_a\gamma^{(a)}$, so $h = -\gamma^{(x4)}(im + K)$):

- *The square.* $h^2 = \gamma^{(x4)}(im + K)\gamma^{(x4)}(im + K) = \gamma^{(x4)}\gamma^{(x4)}(im - K)(im + K) = -\big(-m^2 - K^2\big) = m^2 + K^2$ ($\gamma^{(x4)}$ anticommutes with every gamma in $K$; $\gamma^{(x4)}\gamma^{(x4)} = -1$; the cross terms $imK - Kim$ cancel). By the Clifford relation $K^2 = \sum_ak_a^2\eta^{aa}$ (the products of different gammas cancel in pairs). Hence $h^2 = w^2\,1$ with $w^2 = m^2 + k_1^2 + k_2^2 + k_3^2 + k_8^2 - k_5^2 - k_6^2 - k_7^2$: the frequencies are $\pm w$ (record check `Q_one_particle_flat_dispersion`).
- *The chirality.* $\Gamma h_m\Gamma = -im\Gamma\gamma^{(x4)}\Gamma - \Gamma\gamma^{(x4)}K\Gamma = im\gamma^{(x4)} - \gamma^{(x4)}K = h_{-m}(k)$ (R1 for the single gamma, R2 for the pair): the Hamiltonians of $+m$ and $-m$ are **similar**, so their spectra are **identical**, not opposite (record check `Q_one_particle_maps`).
- *The conjugated mode.* The conjugated field contains $\Gamma u^\ast$. Conjugating the evolution gives $-i\,\partial_4u^\ast = h^\ast u^\ast$, that is $i\,\partial_4u^\ast = -h^\ast u^\ast$, and multiplying by $\Gamma$ (with $\Gamma\Gamma = 1$): $i\,\partial_4(\Gamma u^\ast) = -\Gamma h^\ast\Gamma\,(\Gamma u^\ast)$. Now $h_m^\ast = im\gamma^{(x4)} - \gamma^{(x4)}K$ (only the $i$ changes sign), so $-\Gamma h_m^\ast\Gamma = -\big(-im\gamma^{(x4)} - \gamma^{(x4)}K\big) = h_{-m}(-k)$: **the conjugated mode is a mode of the theory with the reversed mass** (and the reversed momentum, as $e^{-ik\cdot x}$ says).
- *Krein self-adjointness.* $BhB = h^\dagger$, hence $Bh = h^\dagger B$ ($B^2 = 1$). Derivation: with $(-i)^2 = -1$ and $C\gamma^{(x4)} = \gamma^{(x4)}C$, $BhB = -(C\gamma^{(x4)})h(C\gamma^{(x4)})$; the mass part gives $-(C\gamma^{(x4)})(-im\gamma^{(x4)})(C\gamma^{(x4)}) = imC\gamma^{(x4)}\gamma^{(x4)}C\gamma^{(x4)} = -im\gamma^{(x4)}$ (using $\gamma^{(x4)}\gamma^{(x4)} = -1$ and $CC = 1$) and the momentum part gives $K^T\gamma^{(x4)}$ (using $CKC = -K^T$); and $h^\dagger = im(\gamma^{(x4)})^T - K^T(\gamma^{(x4)})^T = -im\gamma^{(x4)} + K^T\gamma^{(x4)}$, the same (record check `mode_hamiltonian_B_selfadjoint_dispersion` of the sympy field-theory report).

**Krein inertia.** For a real frequency $w$ each eigenspace of $h$ has dimension 8, and the form $u^\dagger Bu$ restricted to it has four positive and four negative directions: **Krein inertia** (4,4). For an imaginary frequency the eigenspace is **Krein-neutral**: if $hu = wu$ and $hv = wv$, then $w\,u^\dagger Bv = u^\dagger Bhv = u^\dagger h^\dagger Bv = (hu)^\dagger Bv = w^\ast u^\dagger Bv$, so $(w - w^\ast)u^\dagger Bv = 0$, and the form vanishes when $w$ is not real (record check `Q_one_particle_complex_and_zero_frequencies_Krein_neutral`). Imaginary frequencies occur when the extra-time momenta dominate, $k_5^2 + k_6^2 + k_7^2 > m^2 + k_1^2 + k_2^2 + k_3^2 + k_8^2$; these modes grow exponentially in time (the ill-posedness of the extra times, Chapter 8). The record's eight samples (`Revision/pairing/pairing-theory.json`, data `one_particle_flat`), which Notebook 21c reproduces (In [10]):

| $m$ | momenta $(k_1, \dots, k_8)$ | $w$ | dimensions of the $\pm w$ eigenspaces | Krein inertia on $+w$ and $-w$ |
| --- | --- | --- | --- | --- |
| $\pm2$ | (1, 2, 0, 0, 0, 0, 0, 4) | 5 | 8 and 8 | (4,4) and (4,4) |
| $\pm3$ | (0, 0, 0, 0, 0, 0, 0, 0) | 3 | 8 and 8 | (4,4) and (4,4) |
| $\pm1$ | (1, 0, 0, 0, 0, 0, 0, 0) | $\sqrt2 = 1.414214$ | 8 and 8 | (4,4) and (4,4) |
| $\pm2$ | (0, 0, 0, 0, 1, 0, 0, 0) | $\sqrt3 = 1.732051$ | 8 and 8 | (4,4) and (4,4) |

(Each row stands for two samples of the record, $+m$ and $-m$, with identical results. The entry $k_4$ is not used. Check: for the first row $w^2 = 4 + 1 + 4 + 16 = 25$.)

| statement | status | where it is verified |
| --- | --- | --- |
| the canonical anticommutator $B_{AC}\delta/\cos z$ and the positive representation | record statement, checked word for word | `Revision/theory/field-theory.json`, formula `quantisation`; Notebook 21c, In [2] |
| $MB^TM^\dagger = B$ holds for $M = \Gamma$, gives $-B$ for $M = 1$; in the family $\cos t + \sin t\,\Gamma$ only $t = \pi/2, 3\pi/2$ | PROVED (above); COMPUTED | lead check `quantum_charge_conjugation_unitary_type`; Notebook 21c, In [4] |
| with explicit operators on 65536 states: $\{\Psi_A, \Psi^\dagger_C\} = B_{AC}$; $\Gamma\Psi^{\dagger T}$ gives $B$, $\Psi^{\dagger T}$ gives $-B$ | COMPUTED (all 256 pairs, to rounding) | `Revision/theory/reports/python-field-theory.json`, check `canonical_anticommutator_B`; Notebook 21c, In [6] |
| $Q = N$, $Q' = 16 - Q$, $Q'' = Q - 16$ | PROVED (above); COMPUTED on a random state | Notebook 21c, In [8] (its own computation) |
| $-\Gamma h_m^\ast\Gamma = h_{-m}(-k)$; $\Gamma h_m\Gamma = h_{-m}$; $h^2 = w^2$; $Bh = h^\dagger B$ | PROVED (sympy, symbolic $m$, $k$) | Wolfram pairing report, checks `Q_one_particle_maps`, `Q_one_particle_flat_dispersion`; Notebook 21c, In [9] |
| the eight samples; inertia (4,4) at real, Krein-neutral at imaginary frequencies | PROVED in the record; COMPUTED | checks `Q_one_particle_Krein_signatures`, `Q_one_particle_complex_and_zero_frequencies_Krein_neutral`; Notebook 21c, In [10] to In [12] |

What this does **not** do: no regularised quantum field theory in signature (4,4) is constructed here, the statements concern the anticommutator and the one-particle problem, and nothing in them creates particles, antiparticles or universes.

### 21.27 Example: Notebook 21c conjugates the quantised field

Notebook 21c turns Sections 21.25 and 21.26 into computations. It reads the gammas, the lead report, the field-theory record and its sympy report, and the pairing record; it checks the properties of $B$; it computes $MB^TM^\dagger$ for $M = \Gamma$, $M = 1$ and the family $\cos t\,1 + \sin t\,\Gamma$; it builds 16 fermion modes with the Jordan-Wigner rule and measures all 256 anticommutators of three fields with explicit operators on 65536 states; it checks $Q' = 16 - Q$; it proves the one-particle facts with sympy, reproduces the eight samples of the pairing record and scans the momenta into the region of growing modes. It runs in about 30 seconds; the times measured on the build computer, which depend on how busy that computer is, are recorded in the notebook's provenance file `Revision/textbook/notebooks/21c_quantum_conjugation.PROVENANCE.md`. It needs no Rust, prints 17 PASS lines and draws six figures.

<!-- NOTEBOOK 21c -->

### 21.30 Line-by-line walk-through of Notebook 21c

The notebook has 13 code cells, In [1] to In [13].

**In [1], the set-up cell.** It is the set-up cell of Notebook 21a, explained line by line in Section 21.15 under In [1], except that the comment lines at the top hold the run instructions of Notebook 21c (Section 21.28) and that the line

```python
NOTEBOOK_ID = "21c"  # this notebook: chapter 21, example c
```

names this notebook. The cell prints Set-up of notebook 21c complete.

**In [2]: the gammas, $B$ and the records.**

```python
import numpy as np  # numbers, arrays, matrices
import sympy as sp  # exact algebra

fixture = json.loads(repository_file("Revision/algebra/gammas.json")
                     .read_text(encoding="utf-8"))
COORDS = fixture["coordinates"]  # "x1", ..., "x8"
ETA = fixture["eta"]
gamma = [np.array(mat, dtype=np.int64) for mat in fixture["gamma"]]  # x1 .. x8
I16 = np.eye(16, dtype=np.int64)
```

The packages and the Revision gammas, kept in a list numbered from 0 as in Notebook 21b (`gamma[3]` is $\gamma^{(x4)}$, `gamma[7]` is $\gamma^{(x8)}$).

```python
check(len(gamma) == 8
      and all(g.shape == (16, 16) and set(np.unique(g)) <= {-1, 0, 1} for g in gamma)
      and all(np.array_equal(gamma[a] @ gamma[b] + gamma[b] @ gamma[a],
                             2 * (ETA[a] if a == b else 0) * I16)
              for a in range(8) for b in range(8)),
      "eight real 16 x 16 gamma matrices with the Clifford relation, signature (4,4)")
```

The same test as in Notebooks 21a and 21b, written as one check: eight real signed-entry matrices that obey the Clifford relation.

```python
C = gamma[7] @ gamma[0] @ gamma[1] @ gamma[2]  # C = g(x8) g(x1) g(x2) g(x3)
Gamma = C @ gamma[3] @ gamma[4] @ gamma[5] @ gamma[6]  # the chirality
B = -1j * (C @ gamma[3])  # the Krein matrix B = -i C gamma^(x4)
```

$C$, then $\Gamma$ as $C$ times the four time-like gammas (the same product $\gamma^{(x8)}\gamma^{(x1)}\cdots\gamma^{(x7)}$), and $B$.

```python
def load_checks(path):
    """name -> verdict (upper case) of a Revision report."""
    entries = json.loads(repository_file(path).read_text(encoding="utf-8"))["checks"]
    return {c["name"]: c["verdict"].upper() for c in entries}
```

A helper that reads a Revision report and returns the dictionary from check name to verdict, in capitals.

```python
LEAD_FILE = "Revision/lead_checks/reports/charge-conjugation-and-u1.json"
LEAD = load_checks(LEAD_FILE)
PY_THEORY = load_checks("Revision/theory/reports/python-field-theory.json")
WL_PAIR = load_checks("Revision/pairing/reports/wolfram-pairing.json")
THEORY = {f["key"]: f for f in json.loads(repository_file(
    "Revision/theory/field-theory.json").read_text(encoding="utf-8"))["formulas"]}
PAIRING = json.loads(repository_file("Revision/pairing/pairing-theory.json")
                     .read_text(encoding="utf-8"))
```

The lead report, the sympy field-theory report, the Wolfram pairing report, the formulas of the field-theory record, and the whole pairing record `Revision/pairing/pairing-theory.json`, whose one-particle samples are used in In [10].

```python
clauses = THEORY["quantisation"]["wl"].split("; ")  # the statements of the formula
rule = next(c for c in clauses if c.startswith("{Psi_A(x), Psi^dagger_C(y)}"))
positive = next(c for c in clauses if c.startswith("positive representation"))
say("record: " + rule)
say("record: " + positive)
```

The record's formula `quantisation` is cut at its semicolons. `next(c for c in clauses if ...)` returns the first statement that satisfies the condition: the one that starts with the anticommutator and the one that starts with the words positive representation. Out [2] prints both.

```python
check(rule.endswith("= B_AC delta^7(x - y)/Cos[z]")
      and positive == "positive representation chi = Psi^dagger B, "
      "{Psi_A, chi_C} = delta_AC",
      "the record's anticommutator B_AC delta / cos z and positive representation",
      record="Revision/theory/field-theory.json, formula quantisation")
```

The check demands that the record states the canonical rule with $B_{AC}\delta^7/\cos z$, and the positive representation with $\chi = \Psi^\dagger B$ and $\{\Psi_A, \chi_C\} = \delta_{AC}$. (Since $B^2 = 1$, $\chi = \Psi^\dagger B$ means $\Psi^\dagger = \chi B$: with $\Psi_A = b_A$ and $\chi_C = b^\ast_C$ this is the representation of Section 21.25.)

**In [3]: the properties of $B$.**

```python
eigenvalues = np.linalg.eigvalsh(B)  # eigenvalues of a Hermitian matrix, sorted
check(np.array_equal(B.real, np.zeros((16, 16))) and np.allclose(B, B.conj().T)
      and np.allclose(B @ B, np.eye(16)) and abs(np.trace(B)) < 1e-12
      and np.allclose(eigenvalues, [-1] * 8 + [1] * 8)
      and LEAD["B_imaginary_hermitian"] == "PASS"
      and PY_THEORY["B_properties"] == "PASS",
      "B is purely imaginary, Hermitian, B^2 = 1, trace 0: signature (8,8)",
      record=f"{LEAD_FILE}, check B_imaginary_hermitian")
check(np.allclose(B.T, -B), "B^T = -B")
```

The eigenvalues in increasing order; $B$ is purely imaginary, Hermitian, squares to $1$, has trace 0 (`np.trace` adds the diagonal), so eight eigenvalues $-1$ and eight $+1$; two record checks say the same. The second check is $B^T = -B$, used in Section 21.25.

```python
from matplotlib.colors import LinearSegmentedColormap

SIGNS = LinearSegmentedColormap.from_list("signs", ["#2a78d6", "#f0efec", "#e34948"])
fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.3), width_ratios=[1, 1.3])
```

The blue-white-red colour map of Notebook 21a, and a figure with two panels, the right one wider.

```python
image = axes[0].imshow(B.imag, cmap=SIGNS, vmin=-1, vmax=1)
axes[0].set_title("imaginary part of $B = -iC\\gamma^{(x4)}$")
axes[0].set_xticks([0, 7, 15], ["1", "8", "16"])
axes[0].set_yticks([0, 7, 15], ["1", "8", "16"])
axes[0].set_xlabel("column")
axes[0].set_ylabel("row")
axes[0].grid(False)
fig.colorbar(image, ax=axes[0], ticks=[-1, 0, 1], shrink=0.8)
```

The left panel draws the imaginary part of $B$ (`B.imag`) as a heat map, with a colour bar.

```python
axes[1].bar(np.arange(1, 17), eigenvalues,
            color=["#2a78d6"] * 8 + ["#e34948"] * 8)
axes[1].set_xlabel("eigenvalue number (sorted)")
axes[1].set_ylabel("eigenvalue of $B$")
axes[1].set_title("eight eigenvalues $-1$, eight $+1$")
```

The right panel draws the sixteen eigenvalues as bars, the first eight blue and the last eight red.

```python
save_figure(fig, "krein_matrix",
            "The Krein matrix $B = -iC\\gamma^{(x4)}$ of the canonical "
            "anticommutator. Left: its imaginary part as a heat map (its real part "
            "is zero; horizontal axis the column, vertical axis the row, red $+1$, "
            "blue $-1$); every row and column has one entry, and the nonzero "
            "entries join the two chiral halves. Right: its sixteen eigenvalues in "
            "increasing order, eight $-1$ and eight $+1$ (signature (8,8)); "
            "because of the eight negative eigenvalues the field adjoint cannot be "
            "an ordinary Hilbert adjoint.")
```

Figure 21c.1. **What the figure shows.** Left: sixteen coloured squares, one per row and column, all in the off-diagonal blocks ($B$ contains one gamma, $\gamma^{(x4)}$, times the block-diagonal $C$). Right: a staircase of eight bars at $-1$ and eight at $+1$.

**In [4]: which conjugation keeps the anticommutator.**

```python
def mismatch(M):
    """|| M B^T M^dagger - B ||: zero when M keeps the canonical anticommutator."""
    return np.linalg.norm(M @ B.T @ M.conj().T - B)
```

The size of the failure of the condition of Section 21.25; `np.linalg.norm` of a matrix is the square root of the sum of the squared moduli of all its entries.

```python
q_gamma = Gamma @ B.T @ Gamma.T  # M = Gamma (real, so M^dagger = M^T)
q_one = B.T  # M = 1
check(np.allclose(q_gamma, B) and np.allclose(q_one, -B)
      and LEAD["quantum_charge_conjugation_unitary_type"] == "PASS",
      "M B^T M^dagger = +B for M = Gamma and = -B for M = 1",
      record=f"{LEAD_FILE}, check quantum_charge_conjugation_unitary_type")
```

$MB^TM^\dagger$ for $M = \Gamma$ (real, so its conjugate transpose is its transpose) and for $M = 1$: $+B$ and $-B$, as the lead check records.

```python
t_values = np.linspace(0.0, 2 * np.pi, 721)  # steps of half a degree
family = [np.cos(t) * np.eye(16) + np.sin(t) * Gamma for t in t_values]
mismatches = np.array([mismatch(M) for M in family])
zeros = t_values[mismatches < 1e-12]
say("t where the mismatch vanishes (in units of pi): "
    + ", ".join(f"{t / np.pi:.3f}" for t in zeros))
```

721 values of $t$ from $0$ to $2\pi$ (steps of $2\pi/720$, half a degree), the matrices $\cos t\,1 + \sin t\,\Gamma$ and their mismatches. `t_values[mismatches < 1e-12]` keeps only the values of $t$ where the mismatch is below $10^{-12}$ (an array indexed by a true-false array keeps the entries marked true). Out [4] prints 0.500 and 1.500, that is $t = \pi/2$ and $3\pi/2$.

```python
phases_ok = all(abs(mismatch(c * Gamma)) < 1e-12 for c in (1j, np.exp(0.3j), -1))
scales_bad = all(mismatch(c * Gamma) > 1 for c in (0.5, 2.0))
check(np.allclose(zeros / np.pi, [0.5, 1.5]) and phases_ok and scales_bad,
      "in the family cos t + sin t Gamma only t = pi/2, 3pi/2 work; c Gamma works "
      "exactly for |c| = 1")
```

Multiples $c\,\Gamma$ with $\lvert c\rvert = 1$ ($c = i$, $e^{0.3i}$, $-1$) work; $c = 0.5$ and $c = 2$ fail (they give $\lvert c\rvert^2B$). The check combines the three findings.

```python
fig, ax = plt.subplots(figsize=(8.0, 4.3))
ax.plot(t_values / np.pi, mismatches)
ax.plot([0.5, 1.5], [0, 0], "o", color="#e34948", markersize=9,
        label="$M = \\pm\\Gamma$: mismatch zero")
ax.plot([0.0, 1.0, 2.0], [mismatch(np.eye(16))] * 3, "s", color="#2a78d6",
        label="$M = \\pm 1$: mismatch $\\|{-B} - B\\| = 8$")
ax.set_xlabel("$t / \\pi$ in $M(t) = \\cos t\\,1 + \\sin t\\,\\Gamma$")
ax.set_ylabel("$\\|M B^T M^\\dagger - B\\|$")
ax.set_title("Only $\\pm\\Gamma$ keeps the canonical anticommutator")
ax.legend(fontsize=8)
```

The mismatch against $t/\pi$, red dots at the two zeros, and blue squares at $t = 0, \pi, 2\pi$, where $M = \pm1$ and the mismatch is $\lVert-B - B\rVert = 2 \cdot 4 = 8$.

```python
save_figure(fig, "which_conjugation",
            "The mismatch $\\|M B^T M^\\dagger - B\\|$ (the size of the failure of "
            "the canonical anticommutator) for the conjugations $\\Psi \\to "
            "M\\Psi^{\\dagger T}$ with $M = \\cos t\\,1 + \\sin t\\,\\Gamma$; "
            "horizontal axis $t/\\pi$ from $0$ to $2$, vertical axis the mismatch "
            "(pure number). It vanishes only at $t = \\pi/2$ and $3\\pi/2$, that is "
            "for $M = \\pm\\Gamma$ (red dots); the same-mass choice $M = \\pm 1$ "
            "(blue squares) gives $-B$ instead of $B$, a mismatch of $\\|2B\\| = 8$.")
```

Figure 21c.2. **What the figure shows.** The curve $4\lvert1 + \cos 2t\rvert$ of Section 21.25: it starts at 8, falls to zero at $t = \pi/2$, rises to 8 at $t = \pi$, falls to zero at $3\pi/2$ and returns to 8. Only the two isolated points $M = \pm\Gamma$ are allowed.

**In [5]: sixteen fermion modes on a computer.**

```python
MODES, STATES = 16, 2 ** 16
index = np.arange(STATES)  # basis state numbers 0 .. 65535
occupied_count = np.zeros(STATES, dtype=np.int64)  # number of occupied modes
for j in range(MODES):
    occupied_count += (index >> j) & 1  # >> shifts the bits; & 1 reads bit j
```

A state of the 16 modes is a column of 65536 complex numbers, one **amplitude** per occupation pattern; basis state number $n$ has the pattern given by the binary digits (**bits**) of $n$: bit $j$ is the occupation of mode $j$ (counted from 0). The operator written as two greater-than signs shifts the binary digits of every number $j$ places to the right, and `& 1` (bitwise and with 1) keeps the last digit: together they read bit $j$. Adding these bits over all modes gives, for each basis state, the number of occupied modes.

```python
OPS = []  # for each mode j: the states where j is occupied, and the sign factors
for j in range(MODES):
    filled = ((index >> j) & 1).astype(bool)
    below = index & ((1 << j) - 1)  # the bits of the modes below j
    parity = np.zeros(STATES, dtype=np.int64)
    for i in range(j):
        parity += (below >> i) & 1
    OPS.append((index[filled], index[~filled], np.where(parity % 2 == 0, 1.0, -1.0)))
```

For each mode $j$: `filled` marks the states in which mode $j$ is occupied. The operator written as two less-than signs shifts digits to the left, so `1` shifted by `j` places is $2^j$, and $2^j - 1$ has ones exactly in the bits $0, \dots, j - 1$; the bitwise and with it keeps the bits of the modes below $j$. `parity` counts the occupied modes below $j$, and `np.where(parity % 2 == 0, 1.0, -1.0)` turns an even count into the sign $+1$ and an odd one into $-1$: the Jordan-Wigner sign of Section 21.26. The list `OPS` stores, for each mode, the states where it is occupied (`index[filled]`), those where it is empty (`~` negates the true-false array) and the signs.

```python
def annihilate(j, v):
    """b_j v: empty mode j (with the Jordan-Wigner sign)."""
    filled, _, sign = OPS[j]
    out = np.zeros_like(v)
    out[filled ^ (1 << j)] = sign[filled] * v[filled]
    return out
```

The annihilation operator applied to a state `v`: the amplitude of every pattern with mode $j$ occupied is moved, with its sign, to the pattern with bit $j$ cleared (`^` is the bitwise exclusive or, which flips bit $j$); every other amplitude of the result is zero. Instead of storing a $65536 \times 65536$ matrix, the notebook stores these index lists.

```python
def create(j, v):
    """b_j^* v: fill mode j (with the Jordan-Wigner sign)."""
    _, empty, sign = OPS[j]
    out = np.zeros_like(v)
    out[empty | (1 << j)] = sign[empty] * v[empty]
    return out
```

The creation operator does the reverse: amplitudes of patterns with mode $j$ empty move to the pattern with bit $j$ set (`|` is the bitwise or). The sign depends only on the modes below $j$, which the move does not change.

```python
rng = np.random.default_rng(2103)  # fixed seed: the same state in every run
v = rng.normal(size=STATES) + 1j * rng.normal(size=STATES)
v /= np.linalg.norm(v)  # a random normalised state of the 16 modes
```

A random state of the 16 modes, scaled to length 1 (`/=` divides in place).

```python
basic = all(np.allclose(annihilate(j, create(k, v)) + create(k, annihilate(j, v)),
                        (1.0 if j == k else 0.0) * v)
            for j, k in [(0, 0), (3, 3), (15, 15), (0, 1), (4, 9), (15, 2)])
check(basic, "Jordan-Wigner operators: {b_j, b_k^*} = delta_jk on a random state")
```

The rule $\{b_j, b_k^\ast\} = \delta_{jk}$, tested on the random state for six pairs: $b_jb_k^\ast v + b_k^\ast b_jv$ must be $v$ for $j = k$ and zero otherwise.

**In [6]: the anticommutators of three fields.**

```python
B_column = [int(np.flatnonzero(B[:, c])[0]) for c in range(16)]  # row of the entry
```

Every column of $B$ has exactly one nonzero entry; `np.flatnonzero` lists the positions of the nonzero entries of column `c` (`B[:, c]`), and the first one is kept. So $\Psi^\dagger_C = \sum_Db^\ast_DB_{DC}$ is a single creation operator times $B_{DC} = \pm i$.

```python
def psi(A, u):
    """Psi_A = b_A."""
    return annihilate(A, u)


def psi_dagger(Cc, u):
    """Psi^dagger_C = sum_D b_D^* B_DC (a single term)."""
    D = B_column[Cc]
    return B[D, Cc] * create(D, u)
```

The field operators of the positive representation applied to a state. (The letter `Cc` avoids a clash with the matrix `C`.)

```python
def field_pair(M):
    """For the conjugate M Psi^{dagger T} with diagonal M: the maps u -> Psi'_A u
    and u -> Psi'^dagger_C u (Psi'_A = M_AA Psi^dagger_A, Psi'^dagger_C =
    conj(M_CC) Psi_C)."""
    d = np.diag(M)
    return (lambda A, u: d[A] * psi_dagger(A, u),
            lambda Cc, u: np.conj(d[Cc]) * psi(Cc, u))
```

For a diagonal matrix $M$ (both $\Gamma$ and $1$ are diagonal), the conjugate field is $\Psi'_A = M_{AA}\Psi^\dagger_A$ and its adjoint $\Psi'^\dagger_C = M^\ast_{CC}\Psi_C$. `np.diag(M)` takes the diagonal, and `lambda` defines a small unnamed function; the function returns the pair of them.

```python
def anticommutator_matrix(first, second):
    """N_AC with {first_A, second_C} v = N_AC v, and whether it acts as a number."""
    N = np.zeros((16, 16), dtype=complex)
    number_like = True
    for A in range(16):
        for Cc in range(16):
            w = first(A, second(Cc, v)) + second(Cc, first(A, v))
            N[A, Cc] = np.vdot(v, w)  # v^dagger w
            number_like &= np.allclose(w, N[A, Cc] * v)
    return N, number_like
```

For each of the 256 pairs $(A, C)$ the anticommutator is applied to the random state, $w = XYv + YXv$; `np.vdot(v, w)` is $v^\dagger w$, the number $N_{AC}$; and `number_like` stays true only if $w = N_{AC}v$ for every pair, that is, if the anticommutator acts on the state as a plain number (`&=` combines with "and").

```python
N_psi, ok_psi = anticommutator_matrix(psi, psi_dagger)
N_same, ok_same = anticommutator_matrix(psi, psi)  # {Psi_A, Psi_C}
N_gamma, ok_gamma = anticommutator_matrix(*field_pair(Gamma))
N_one, ok_one = anticommutator_matrix(*field_pair(np.eye(16)))
```

Four measurements: $\{\Psi_A, \Psi^\dagger_C\}$, $\{\Psi_A, \Psi_C\}$, and the anticommutators of the conjugate fields with $M = \Gamma$ and $M = 1$ (the star unpacks the returned pair into the two arguments). In all, 1024 anticommutators of operators on 65536 states; this takes about 10 seconds.

```python
check(ok_psi and ok_same and np.allclose(N_psi, B) and np.allclose(N_same, 0)
      and PY_THEORY["canonical_anticommutator_B"] == "PASS",
      "operators: {Psi_A, Psi^dagger_C} = B_AC and {Psi_A, Psi_C} = 0 (256 pairs)",
      record="Revision/theory/reports/python-field-theory.json, check "
      "canonical_anticommutator_B")
check(ok_gamma and ok_one and np.allclose(N_gamma, B) and np.allclose(N_one, -B),
      "operators: Gamma Psi^{dagger T} has +B, Psi^{dagger T} has -B")
```

The positive representation obeys the canonical rule; the valid conjugate $\Gamma\Psi^{\dagger T}$ obeys it too; the same-mass candidate $\Psi^{\dagger T}$ obeys it with $-B$. This is Section 21.25 confirmed with explicit operators.

**In [7]: the measured anticommutators as heat maps.**

```python
fig, axes = plt.subplots(1, 3, figsize=(12.0, 4.2))
for ax, N, title in ((axes[0], N_psi, "$\\{\\Psi_A, \\Psi^\\dagger_C\\}$"),
                     (axes[1], N_gamma, "$\\Psi' = \\Gamma\\Psi^{\\dagger T}$"),
                     (axes[2], N_one, "$\\Psi'' = \\Psi^{\\dagger T}$")):
    image = ax.imshow(N.imag, cmap=SIGNS, vmin=-1, vmax=1)
    ax.set_title(title)
    ax.set_xticks([0, 7, 15], ["1", "8", "16"])
    ax.set_yticks([0, 7, 15], ["1", "8", "16"])
    ax.set_xlabel("$C$")
    ax.grid(False)
axes[0].set_ylabel("$A$")
fig.colorbar(image, ax=axes, ticks=[-1, 0, 1], shrink=0.8,
             label="imaginary part of the anticommutator")
```

Three heat maps of the imaginary parts of the measured $16 \times 16$ matrices (their real parts are zero), with $C$ along the horizontal and $A$ along the vertical axis.

```python
save_figure(fig, "operator_anticommutators",
            "The anticommutators $\\{X_A, Y^\\dagger_C\\}$ measured with explicit "
            "operators on the 65536 states of 16 fermion modes (imaginary parts; "
            "the real parts are zero; horizontal axis $C$, vertical axis $A$, red "
            "$+1$, blue $-1$). Left: the field $\\Psi$ of the positive "
            "representation, which gives the Krein matrix $B$. Middle: the "
            "conjugate $\\Gamma\\Psi^{\\dagger T}$, which gives $B$ again, so it is "
            "a field of the same quantum theory. Right: the same-mass candidate "
            "$\\Psi^{\\dagger T}$, which gives $-B$ (every colour reversed), so it is "
            "not.")
```

Figure 21c.3. **What the figure shows.** The left and middle panels are the same picture, the heat map of $B$ of figure 21c.1; the right panel is that picture with red and blue exchanged.

**In [8]: the valid conjugation counts the empty modes.**

```python
def charge(first_dagger, second, u):
    """sum_AC first_dagger_A B_AC second_C u (only the 16 nonzero B_AC)."""
    out = np.zeros_like(u)
    for Cc in range(16):
        A = B_column[Cc]  # the row of the nonzero entry of column C
        out += first_dagger(A, B[A, Cc] * second(Cc, u))
    return out
```

The charge operator $\sum_{A,C}X^\dagger_AB_{AC}Y_C$ applied to a state; since each column of $B$ has one nonzero entry, the double sum has only 16 terms.

```python
conj_g, conj_g_dagger = field_pair(Gamma)
conj_1, conj_1_dagger = field_pair(np.eye(16))
Q_v = charge(psi_dagger, psi, v)
Qp_v = charge(conj_g_dagger, conj_g, v)
Qpp_v = charge(conj_1_dagger, conj_1, v)
```

The two conjugate fields and their adjoints, and the three charges $Q$, $Q'$ (valid conjugate) and $Q''$ (same-mass candidate) applied to the random state.

```python
check(np.allclose(Q_v, occupied_count * v)
      and np.allclose(Qp_v, (16 - occupied_count) * v)
      and np.allclose(Qpp_v, (occupied_count - 16) * v),
      "Q = number of occupied modes, Q' = 16 - Q (Gamma), Q'' = Q - 16 (M = 1)")
```

`occupied_count * v` multiplies each amplitude by the number of occupied modes of its basis state: that is how the number operator $N$ acts. The check proves, on this state, $Q = N$, $Q' = 16 - N$ and $Q'' = N - 16$ (Section 21.26).

```python
n = np.arange(17)
fig, ax = plt.subplots(figsize=(8.0, 4.4))
ax.plot(n, n - 8, "o-", label="$Q - 8$ of the field $\\Psi$")
ax.plot(n, (16 - n) - 8, "s-", label="$Q' - 8$ of $\\Gamma\\Psi^{\\dagger T}$ "
        "(valid)")
ax.plot(n, (n - 16) + 8, "^--", color="#999999",
        label="$Q'' + 8$ of $\\Psi^{\\dagger T}$ (invalid)")
ax.axhline(0.0, color="black", linewidth=0.8)
ax.set_xlabel("number of occupied modes in the basis state")
ax.set_ylabel("charge (shifted by the constant 8)")
ax.set_title("The valid conjugation reverses the charge")
ax.legend(fontsize=8)
```

For a basis state with $n = 0, \dots, 16$ occupied modes the three charges are $n$, $16 - n$ and $n - 16$; they are drawn shifted by the constant 8 (minus 8 for the first two, plus 8 for the third), so that a reversal shows as a mirror image in the horizontal axis.

```python
save_figure(fig, "charge_of_states",
            "The charge of the basis states of 16 fermion modes, measured by three "
            "fields; horizontal axis the number of occupied modes (0 to 16), "
            "vertical axis the charge shifted by a constant (minus 8 for $\\Psi$ "
            "and $\\Gamma\\Psi^{\\dagger T}$, plus 8 for $\\Psi^{\\dagger T}$; "
            "pure numbers). "
            "The field $\\Psi$ counts the occupied modes; the valid conjugate "
            "$\\Gamma\\Psi^{\\dagger T}$ counts the empty ones, $Q' = 16 - Q$, so "
            "the shifted charge is exactly reversed (particles and holes "
            "exchanged); the invalid candidate $\\Psi^{\\dagger T}$ would give "
            "$Q - 16$, not a reversal.")
```

Figure 21c.4. **What the figure shows.** A rising line ($\Psi$) and a falling line (the valid conjugate) that cross at $n = 8$: the charge reversed about its middle. The grey dashed line of the invalid candidate lies exactly on the rising line: shifted back by the constant, it measures the same charge as $\Psi$, not the opposite.

**In [9]: the mass is reversed, the spectra are equal.**

```python
m = sp.symbols("m", real=True)
k = sp.symbols("k1:9", real=True)  # k[3] (the x4 entry) is not used
G = [sp.Matrix(g.tolist()) for g in gamma]
Gamma_s, B_s = sp.Matrix(Gamma.tolist()), -sp.I * sp.Matrix(C.tolist()) * G[3]
```

A real symbol for the mass, eight real symbols for the momenta (the fourth, along the time, is not used), exact gammas, $\Gamma$ and $B$.

```python
def h(mass, momenta):
    """h_m(k) = -i m gamma^(x4) - gamma^(x4) sum_(a != x4) k_a gamma^a."""
    total = -sp.I * mass * G[3]
    for a in range(8):
        if a != 3:
            total -= momenta[a] * G[3] * G[a]
    return total
```

The one-particle Hamiltonian of Section 21.26, built term by term (`-=` subtracts from the running total; `!=` means "not equal").

```python
zero = sp.zeros(16, 16)
h_m = h(m, k)
minus_k = [-q for q in k]
w2 = m ** 2 + k[0] ** 2 + k[1] ** 2 + k[2] ** 2 + k[7] ** 2 - k[4] ** 2 - k[5] ** 2 \
    - k[6] ** 2
```

The zero matrix, $h_m(k)$ with symbolic mass and momenta, the reversed momenta, and $w^2$ (the backslash continues the line).

```python
check((-Gamma_s * h_m.conjugate() * Gamma_s - h(-m, minus_k)).expand() == zero,
      "-Gamma conj(h_m(k)) Gamma = h_(-m)(-k): the conjugated mode has the reversed "
      "mass")
check((Gamma_s * h_m * Gamma_s - h(-m, k)).expand() == zero
      and WL_PAIR["Q_one_particle_maps"] == "PASS",
      "Gamma h_m(k) Gamma = h_(-m)(k): equal spectra for +m and -m",
      record="Revision/pairing/reports/wolfram-pairing.json, check "
      "Q_one_particle_maps")
```

The first two facts of Section 21.26, proved exactly for every real mass and momentum: the conjugated mode evolves with the reversed mass, and the Hamiltonians of $\pm m$ are similar.

```python
check((h_m * h_m - w2 * sp.eye(16)).expand() == zero
      and (B_s * h_m - h_m.H * B_s).expand() == zero
      and WL_PAIR["Q_one_particle_flat_dispersion"] == "PASS"
      and PY_THEORY["mode_hamiltonian_B_selfadjoint_dispersion"] == "PASS",
      "h_m(k)^2 = w^2 1 and B h_m = h_m^dagger B",
      record="Revision/pairing/reports/wolfram-pairing.json, check "
      "Q_one_particle_flat_dispersion")
```

The square and the Krein self-adjointness (`h_m.H` is $h^\dagger$), with the two record checks.

**In [10]: the eight samples of the pairing record.**

```python
def numeric_h(mass, momenta):
    """h_m(k) as a numpy array."""
    total = -1j * mass * gamma[3].astype(complex)
    for a in range(8):
        if a != 3:
            total = total - momenta[a] * (gamma[3] @ gamma[a])
    return total
```

The same Hamiltonian with numbers instead of symbols.

```python
def eigenspace_facts(H_mat, w):
    """Dimension and Krein inertia (positive, negative) of the eigenspace of w."""
    P = (np.eye(16) + H_mat / w) / 2  # projector onto the eigenvalue +w (w != 0)
    U_, s_, _ = np.linalg.svd(P)
    V = U_[:, s_ > 1e-9]  # orthonormal basis of the range of P
    form = np.linalg.eigvalsh(V.conj().T @ B @ V)
    return V.shape[1], (int(np.sum(form > 1e-9)), int(np.sum(form < -1e-9)))
```

Since $h^2 = w^2$, the matrix $P = \tfrac12(1 + h/w)$ is the projector onto the eigenvectors of $h$ with eigenvalue $w$ ($P^2 = \tfrac14(1 + 2h/w + h^2/w^2) = \tfrac14(2 + 2h/w) = P$). The **singular value decomposition** `np.linalg.svd` writes $P$ as a product of three matrices; the columns of the first that belong to nonzero singular values form an orthonormal basis $V$ of the eigenspace. The form $u^\dagger Bu$ restricted to the eigenspace is the matrix $V^\dagger BV$; its eigenvalues are counted by sign. The function returns the dimension (the number of columns of $V$) and the Krein inertia.

```python
rows_ok = True
for sample in PAIRING["data"]["one_particle_flat"]["samples"]:
    H_mat = numeric_h(sample["m"], sample["k"])
    w = float(sp.sympify(sample["w"].replace("Sqrt[", "sqrt(").replace("]", ")")))
    w_here = np.sqrt(np.max(np.linalg.eigvals(H_mat @ H_mat).real))
    dim_p, inertia_p = eigenspace_facts(H_mat, w_here)
    dim_m, inertia_m = eigenspace_facts(H_mat, -w_here)
```

For each sample of the record: the Hamiltonian; the record's frequency, written in Wolfram notation such as `Sqrt[2]`, which `.replace` turns into `sqrt(2)` and `sp.sympify` reads as a number; the frequency computed here as the square root of the largest eigenvalue of $h^2$; and the dimensions and inertias of both eigenspaces.

```python
    same = (abs(w_here - w) < 1e-12 and dim_p == sample["dim_plus_w"]
            and dim_m == sample["dim_minus_w"]
            and list(inertia_p) == sample["B_inertia_plus_w"]
            and list(inertia_m) == sample["B_inertia_minus_w"])
    rows_ok &= same
```

Every number is compared with the record (the inertia, a pair, is turned into a list for the comparison).

```python
    k_text = ",".join(str(q) for q in sample["k"])
    say(f"m = {sample['m']:+d}, k = ({k_text}): w = {w_here:.6f}, dims {dim_p} "
        f"{dim_m}, inertia ({inertia_p[0]},{inertia_p[1]}) "
        f"({inertia_m[0]},{inertia_m[1]}), same: {same}")
```

One printed line per sample: Out [10] shows the eight rows of the table of Section 21.26, each ending with "same: True".

```python
check(rows_ok and WL_PAIR["Q_one_particle_Krein_signatures"] == "PASS",
      "all eight one-particle samples of the pairing record reproduced",
      record="Revision/pairing/reports/wolfram-pairing.json, check "
      "Q_one_particle_Krein_signatures")
```

All eight samples agree with the record.

**In [11]: the spectra along two lines of momenta.**

```python
def spectrum(mass, k1=0.0, k5=0.0):
    """The 16 eigenvalues of h_m with momenta k1 (x1) and k5 (x5), sorted."""
    momenta = [k1, 0, 0, 0, k5, 0, 0, 0]
    values = np.linalg.eigvals(numeric_h(mass, momenta))
    return np.sort_complex(np.round(values, 9))
```

The sixteen eigenvalues of $h_m$ with a momentum $k_1$ along ordinary space and $k_5$ along an extra time, rounded to 9 decimals (so that equal values sort in the same order) and sorted (`np.sort_complex` sorts by real part, then by imaginary part).

```python
scan = np.linspace(-3.0, 3.0, 241)  # steps of 0.025; contains k5 = -1 and +1
spec_k1 = {s: np.array([spectrum(s, k1=q) for q in scan]) for s in (1, -1)}
spec_k5 = {s: np.array([spectrum(s, k5=q) for q in scan]) for s in (1, -1)}
exceptional = np.abs(np.abs(scan) - 1.0) < 1e-9  # the two points k5 = -1, +1
```

241 momenta from $-3$ to $3$; the spectra for $m = +1$ and $m = -1$ along $k_1$ and along $k_5$; and a true-false array that marks the two points $k_5 = \pm1$, where $w = 0$.

```python
check(np.allclose(spec_k1[1], spec_k1[-1], rtol=0, atol=1e-8)
      and np.allclose(spec_k5[1][~exceptional], spec_k5[-1][~exceptional],
                      rtol=0, atol=1e-8)
      and np.abs(spec_k5[1][exceptional]).max() < 1e-6
      and np.abs(spec_k5[-1][exceptional]).max() < 1e-6
      and np.allclose(np.abs(spec_k1[1].real).max(axis=1), np.sqrt(1 + scan ** 2)),
      "scans: identical spectra for m = +1 and m = -1; w = sqrt(1 + k1^2)")
```

The spectra of $m = +1$ and $m = -1$ agree to $10^{-8}$ at every point (`rtol=0, atol=1e-8` means an absolute tolerance only), except at the two points $k_5 = \pm1$. There $h^2 = 0$ although $h \ne 0$: such a matrix cannot be brought to diagonal form, and a computer finds its eigenvalues only to about the square root of the rounding unit, about $10^{-8}$; the check therefore asks only that all 32 computed eigenvalues there are below $10^{-6}$. Finally the largest real part along $k_1$ is $\sqrt{1 + k_1^2}$.

```python
fig, axes = plt.subplots(1, 2, figsize=(12.0, 4.4))
for s, style, label in ((1, "-", "$m = +1$"), (-1, "--", "$m = -1$")):
    axes[0].plot(scan, spec_k1[s].real.max(axis=1), style, color="#e34948",
                 label=f"$+w$, {label}")
    axes[0].plot(scan, spec_k1[s].real.min(axis=1), style, color="#2a78d6",
                 label=f"$-w$, {label}")
    axes[1].plot(scan, spec_k5[s].real.max(axis=1), style, color="#e34948",
                 label=f"largest real part, {label}")
    axes[1].plot(scan, spec_k5[s].imag.max(axis=1), style, color="#2ca02c",
                 label=f"largest imaginary part, {label}")
```

For both masses (solid and dashed lines): along $k_1$ the largest and smallest eigenvalue ($\pm w$); along $k_5$ the largest real part and the largest imaginary part.

```python
axes[0].set_xlabel("momentum $k_1$ along ordinary space")
axes[0].set_ylabel("frequency (eigenvalue of $h_m$)")
axes[0].set_title("Good sector: real frequencies $\\pm\\sqrt{m^2 + k_1^2}$")
axes[0].legend(fontsize=7)
axes[1].set_xlabel("momentum $k_5$ along the extra time $x5$")
axes[1].set_ylabel("largest real or imaginary part of the eigenvalues")
axes[1].set_title("Extra-time momentum: imaginary beyond $|k_5| = |m|$")
axes[1].legend(fontsize=7)
```

Labels, titles and legends of the two panels.

```python
save_figure(fig, "dispersion_pm_mass",
            "One-particle frequencies of the flat 4+4 Hamiltonian $h_m(k)$ for "
            "$m = +1$ (solid) and $m = -1$ (dashed, on top of the solid lines). "
            "Left: versus the momentum $k_1$ along ordinary space; the frequencies "
            "$\\pm\\sqrt{1 + k_1^2}$ are real and the same for both masses. Right: "
            "versus the momentum $k_5$ along an extra time; for $|k_5| < 1$ the "
            "largest real part is $\\sqrt{1 - k_5^2}$, for $|k_5| > 1$ the "
            "frequencies are imaginary, $\\pm i\\sqrt{k_5^2 - 1}$ (green), and the "
            "modes grow in time. Horizontal axes the momentum, vertical axes the "
            "frequency (pure numbers, units with $m = 1$).")
```

Figure 21c.5. **What the figure shows.** Left: two hyperbola-like curves $\pm\sqrt{1 + k_1^2}$, the dashed ones exactly on the solid ones. Right: a red half-circle $\sqrt{1 - k_5^2}$ between $k_5 = -1$ and $1$, and outside it green curves $\sqrt{k_5^2 - 1}$ rising from zero: imaginary frequencies, growing modes, the same for both masses.

**In [12]: the Krein inertia along the extra-time scan.**

```python
def leading_inertia(k5):
    """Dimension and Krein inertia of the eigenspace of the leading eigenvalue."""
    H_mat = numeric_h(1, [0, 0, 0, 0, k5, 0, 0, 0])
    w2_here = 1 - k5 ** 2
    w = np.sqrt(w2_here) if w2_here > 0 else 1j * np.sqrt(-w2_here)
    return eigenspace_facts(H_mat, w)
```

For $m = 1$ and momentum $k_5$: $w^2 = 1 - k_5^2$, and the leading eigenvalue is $w = \sqrt{w^2}$ when $w^2 > 0$ and $w = i\sqrt{-w^2}$ otherwise; the projector of In [10] works for an imaginary $w$ as well, since still $h^2 = w^2$.

```python
k5_scan = scan[np.abs(np.abs(scan) - 1.0) > 1e-6]  # leave out w = 0 at |k5| = 1
facts = [leading_inertia(q) for q in k5_scan]
positive = np.array([f[1][0] for f in facts])
negative = np.array([f[1][1] for f in facts])
dims = np.array([f[0] for f in facts])
real_region = np.abs(k5_scan) < 1
```

The scan without the two points of zero frequency (where the projector would divide by zero); the dimension and the counts of positive and negative directions for each momentum; and a mark for the region of real frequencies.

```python
check(np.all(dims == 8)
      and np.all(positive[real_region] == 4) and np.all(negative[real_region] == 4)
      and np.all(positive[~real_region] == 0) and np.all(negative[~real_region] == 0)
      and WL_PAIR["Q_one_particle_complex_and_zero_frequencies_Krein_neutral"]
      == "PASS",
      "inertia (4,4) at real frequencies, Krein-neutral at imaginary frequencies",
      record="Revision/pairing/reports/wolfram-pairing.json, check "
      "Q_one_particle_complex_and_zero_frequencies_Krein_neutral")
```

Every eigenspace has dimension 8; for real frequencies the inertia is (4,4); for imaginary frequencies there are no positive and no negative directions: the form vanishes on the eigenspace (Section 21.26).

```python
fig, ax = plt.subplots(figsize=(8.0, 4.3))
ax.plot(k5_scan, positive, "o", markersize=6, markerfacecolor="none",
        label="positive directions of the form")  # open circles
ax.plot(k5_scan, negative, "x", markersize=4,
        label="negative directions of the form")  # crosses inside the circles
ax.axvspan(-3, -1, color="#f2d0a9", alpha=0.5, label="imaginary frequency")
ax.axvspan(1, 3, color="#f2d0a9", alpha=0.5)
ax.set_xlim(-3, 3)
ax.set_ylim(-0.5, 8.5)
ax.set_xlabel("momentum $k_5$ along the extra time $x5$ ($m = 1$)")
ax.set_ylabel("Krein inertia of the 8-dimensional eigenspace")
ax.set_title("Inertia (4,4) for real frequencies, neutral for growing modes")
ax.legend(fontsize=8, loc="upper center")
```

The two counts against $k_5$: open circles for the positive and small crosses for the negative directions (they coincide, so the crosses sit inside the circles); `axvspan` shades the two regions of imaginary frequency.

```python
save_figure(fig, "krein_inertia_scan",
            "The Krein inertia of the 8-dimensional eigenspace of the leading "
            "eigenvalue of $h_m(k)$, $m = 1$, along the momentum $k_5$ of an extra "
            "time: the numbers of positive (circles) and negative (crosses) "
            "eigenvalues of the form $u^\\dagger Bu$ restricted to it; horizontal "
            "axis $k_5$, vertical axis the counts. For $|k_5| < 1$ (real "
            "frequency) the inertia is (4,4); in the shaded regions $|k_5| > 1$ the "
            "frequency is imaginary, the mode grows, and the form vanishes on the "
            "whole eigenspace (Krein-neutral).")
```

Figure 21c.6. **What the figure shows.** In the middle, between $k_5 = -1$ and $1$, a row of circles with crosses at height 4; in the two shaded regions the same marks at height 0. A growing mode carries no Krein charge of either sign.

**In [13]: the figure files.**

```python
names = sorted(FIGURE_NUMBERS, key=FIGURE_NUMBERS.get)
check(len(names) == 6 and all(
    output_file(f"{FIGURE_FOLDER}/21c_{FIGURE_NUMBERS[n]}_{n}.png").is_file()
    for n in names), "the six figure files of notebook 21c exist")
all_checks_passed()
```

The six figure files exist, and the last line prints ALL 17 CHECKS PASSED (notebook 21c).

### 21.31 Sakharov's conditions applied to this theory

Sections 21.3 to 21.6 taught the three conditions on toy models; Sections 21.7 to 21.30 derived the facts of the theory. This section puts them together, condition by condition. Each status is set by a check of the Revision record; Notebook 21d reads every one of these verdicts before it draws the scorecard (Section 21.37).

**Condition 1: a process must change the number.** The theory has no baryons; its only number of this kind is the U(1) charge $Q$. Section 21.17 proved that $\partial_\mu(\cos z\,J^\mu) = 0$ on every solution, in the author's metric with an arbitrary history $a_4(x_4)$, the deflating one included (lead check `u1_noether_matrix_identity`). So the charge of a region changes only by the flux through its boundary; a flux through the brane moves charge, it does not create it, and with no flux the charge of one universe is constant. In the language of the decay model of Section 21.5: every process of the theory has channels of the **same** charge, $\mathcal{B}_1 = \mathcal{B}_2$, so the net charge made by $N$ pairs, $N(r - \bar r)(\mathcal{B}_1 - \mathcal{B}_2)$, is zero; the rate model of Section 21.6 then starts with $\epsilon = 0$ and ends with $a = 0$, however slow the decays and however far from equilibrium (Notebook 21d, In [13]). **Condition 1 FAILS (PROVED).** For the quantised field this holds at the level of the canonical field equations; no regularised quantum field theory in signature (4,4) is constructed in the record, and no anomaly (a quantum breaking of a classical conservation law) is computed: OPEN.

**Condition 2: C and CP must be violated.** For the commuting field dirac16complex00 the same-mass charge conjugation $\Psi \to \Psi^c = \Psi^\ast$ is an exact symmetry. Proof, line by line:

- Every term of $\mathcal{L}$ is a sum of products $\Psi_r^\ast X_{rc}\Phi_c$ with a real matrix $X$ (built from $C$, the gammas, the scale factors and the $\Omega_\mu$) and with $\Phi$ the field or one of its derivatives, or a product of two such sums (the term $\tfrac\lambda2S^2$), times the real $\cos z$ (Section 21.7).
- Replacing $\Psi$ by $\Psi^\ast$ turns $\Psi_r^\ast X_{rc}\Phi_c$ into $\Psi_rX_{rc}\Phi_c^\ast = (\Psi_r^\ast X_{rc}\Phi_c)^\ast$ (commuting numbers may be reordered; $X_{rc}$ is real; the conjugate of a product is the product of the conjugates).
- So $\mathcal{L}[\Psi^\ast] = (\mathcal{L}[\Psi])^\ast$, and $\mathcal{L}$ is real (record checks `L_real_C` of `Revision/theory/reports/wolfram-field-theory.json` and `commuting_lagrangian_real` of the sympy report): $\mathcal{L}[\Psi^\ast] = \mathcal{L}[\Psi]$.

The map keeps the Lagrangian, hence maps solutions to solutions of the same theory, and it reverses every current (Section 21.10). By Proposition 2 of Section 21.5 a C-symmetric start can then develop no average charge asymmetry, even if condition 1 were met. Notebook 21d checks $\mathcal{L}[\Psi^\ast] = \mathcal{L}[\Psi] = -11.2851368126$ at one point of the author's metric with the record's spin connection (In [14]). For the quantised field dirac16complex there is no same-mass conjugation at all: the only conjugation compatible with canonical quantisation, $\Psi \to \Gamma\Psi^{\dagger T}$, reverses the mass (Section 21.25). The maps $\Gamma$ and $\Gamma\Psi^\ast$ also reverse the mass: $\mathcal{L}_{m,\lambda}[\Gamma\Psi] = \mathcal{L}_{m,\lambda}[\Gamma\Psi^\ast] = -\mathcal{L}_{-m,-\lambda}[\Psi] = 8.4767165144$ at the same point (In [14]; theorem T1, record check `T1_Lagrangian_primordial_commuting`). Whether particle and antiparticle processes of this theory happen at different rates (C and CP violation in rates) is **NOT COMPUTED**: the record computes no reaction rates at all. The status of condition 2 is therefore different for the two fields. For the commuting field dirac16complex00 condition 2 **FAILS (PROVED)**: $\mathcal{C}_+$ is an exact symmetry that reverses the charge, so Proposition 2 applies (the reality of the gammas, of $C$ and of the $\Omega_\mu$: lead checks `representation_real` and `spinor_connection_real`; the reversal of the current: lead check `bilinears_under_charge_conjugation`). For the quantised field dirac16complex it is **NOT COMPUTED**: no rates are computed, and its only conjugation reverses the mass (lead check `quantum_charge_conjugation_unitary_type`).

**Condition 3: a departure from thermal equilibrium.** The Revision record contains no computation of reaction rates or of a departure from equilibrium. Its Kohn-Sham states (Chapters 14 and 15) are instantaneous states along the history $a_4 = AHx_4$, and that history is a **prescribed background**: the Kohn-Sham states violate the source conditions of the $a_4$ equations, so the history is not a dynamical consequence of the field (record check `ks_history_is_a_prescribed_background` of `Revision/field_equations_a4/reports/ks-source-conditions.json`; Chapter 17). **NOT COMPUTED.**

**The conclusion.** Since condition 1 fails exactly, conditions 2 and 3 cannot help: whatever the rates and however far from equilibrium, no process of the theory as built makes a net charge inside one universe.

| Sakharov condition | this theory | status | record check |
| --- | --- | --- | --- |
| 1. a process changes the number | $Q$ exactly conserved for every $a_4$ | FAILS (PROVED) | `u1_noether_matrix_identity` |
| 2. C and CP violated | the commuting field: $\mathcal{C}_+$ is exact and reverses the charge, so a C-symmetric start keeps zero charge; the quantised field has only the mass-reversing conjugation; no rates computed | dirac16complex00: FAILS (PROVED: $\mathcal{C}_+$ exact, Proposition 2); dirac16complex: NOT COMPUTED (no rates; only the mass-reversing conjugation) | `representation_real`, `spinor_connection_real`, `bilinears_under_charge_conjugation`, `quantum_charge_conjugation_unitary_type` |
| 3. out of equilibrium | no rate computed; the Kohn-Sham history is a prescribed background | NOT COMPUTED | `ks_history_is_a_prescribed_background` |

### 21.32 What a charge-violating term would look like

Condition 1 could be met only by adding to the theory a term that is **not** invariant under $\Psi \to e^{i\alpha}\Psi$. The simplest candidates are **Majorana-type mass terms** $\Psi^TM\Psi$ with a constant $16 \times 16$ matrix $M$, built from $\Psi$ twice and without $\Psi^\dagger$. Under $\Psi \to e^{i\alpha}\Psi$ such a term is multiplied by $e^{i\alpha}e^{i\alpha} = e^{2i\alpha}$: it carries U(1) charge 2. This section finds every such term that respects the rotations and boosts of the theory. It is a statement about possible additions to the theory, not about the theory as built.

**The condition**, line by line. A rotation or boost acts as $\Psi \to R\Psi$ with $R = e^{\theta S^{ab}}$. The term is invariant when $(R\Psi)^TM(R\Psi) = \Psi^TR^TMR\Psi$ equals $\Psi^TM\Psi$ for every $\Psi$, that is $R^TMR = M$. For a small angle $\theta$, $R = 1 + \theta S + \dots$ (the dots are terms with $\theta^2$ and higher powers), and

$$
R^TMR = (1 + \theta S^T)M(1 + \theta S) + \dots = M + \theta\,(S^TM + MS) + \dots ,
$$

so the term of first order must vanish:

$$
(S^{ab})^TM + MS^{ab} = 0\qquad\text{for all 28 generators } S^{ab} .
$$

For the 256 entries of $M$ these are $28 \times 256 = 7168$ linear equations.

**Their solutions.** First, $CS^{ab}C = -(S^{ab})^T$ for $a \ne b$:

$$
CS^{ab}C = \tfrac12C\gamma^aCC\gamma^bC = \tfrac12\big(-(\gamma^a)^T\big)\big(-(\gamma^b)^T\big) = \tfrac12(\gamma^b\gamma^a)^T = -\tfrac12(\gamma^a\gamma^b)^T = -(S^{ab})^T
$$

(insert $CC = 1$ in the middle; (R3) twice; the transpose of a product reverses the order; $\gamma^b\gamma^a = -\gamma^a\gamma^b$ for $a \ne b$). Then the condition $S^TM + MS = 0$ with $S^T = -CSC$ reads $-CSCM + MS = 0$; multiplying from the left by $C$ gives $-SCM + CMS = 0$, that is

$$
(CM)\,S^{ab} = S^{ab}\,(CM)\qquad\text{for all } S^{ab} :
$$

$M$ solves the equations exactly when $CM$ commutes with every generator. The matrices that commute with all 28 generators form a space of dimension 2, spanned by $1$ and $\Gamma$ (equivalently by the projectors onto the two chiral halves; record check `spin_commutant_dimension_2` of `Revision/algebra/reports/python-algebra.json`: the 16 components split under Spin(4,4) into two inequivalent halves). Hence $CM = c_11 + c_2\Gamma$, and multiplying by $C$: $M = c_1C + c_2C\Gamma$. **The invariant Majorana-type matrices are exactly the combinations of $C$ and $C\Gamma$.** Notebook 21d solves the 7168 equations exactly and finds a space of dimension 2 spanned by them (In [16]); it also checks a finite rotation-boost $R$, built with $e^{\theta S} = \cos(\theta/2) + 2\sin(\theta/2)S$ when $S^2 = -\tfrac14$ (a rotation) and $e^{\theta S} = \cosh(\theta/2) + 2\sinh(\theta/2)S$ when $S^2 = +\tfrac14$ (a boost). (These follow from the power series of the exponential, as Euler's formula does, because $(2S)^2 = -1$ or $+1$. And $S^2 = \tfrac14\gamma^a\gamma^b\gamma^a\gamma^b = -\tfrac14\eta^{aa}\eta^{bb}$: a rotation when the two directions are both space-like or both time-like, a boost otherwise.)

**For anticommuting components these terms vanish**, line by line. With $\Psi_r\Psi_c = -\Psi_c\Psi_r$ and hence $\Psi_r\Psi_r = 0$:

$$
\Psi^TM\Psi = \sum_{r,c}\Psi_rM_{rc}\Psi_c = \sum_{r<c}\big(M_{rc} - M_{cr}\big)\Psi_r\Psi_c
$$

(the diagonal terms vanish; a term with $r > c$ is rewritten as $-M_{rc}\Psi_c\Psi_r$ and the summation letters renamed). Only the antisymmetric part of $M$ survives. $C$ is symmetric (R3) and so is $C\Gamma$ ($(C\Gamma)^T = \Gamma^TC^T = \Gamma C = C\Gamma$ by (R2)). So **the field dirac16complex has no Majorana-type mass term at all.** For the commuting field dirac16complex00 the terms $\Psi^TC\Psi$ and $\Psi^TC\Gamma\Psi$ are nonzero and carry charge 2 (In [16] and In [17], figure 21d.7). Adding one of them to the Lagrangian (together with its complex conjugate, to keep $\mathcal{L}$ real) would break the U(1) symmetry and let the charge change in steps of 2. That this would be consistent, or that nature contains such a term, is a HYPOTHESIS that nothing in the Revision record examines; for the anticommuting field a charge-violating term would need derivatives, more fields or new structures, which are not classified here (OPEN).

| statement | status | where it is verified |
| --- | --- | --- |
| invariance needs $S^TM + MS = 0$; solutions exactly the span of $C$ and $C\Gamma$ | PROVED (above); the 7168 equations solved exactly | `Revision/algebra/reports/python-algebra.json`, check `spin_commutant_dimension_2`; Notebook 21d, In [16] |
| a finite rotation-boost keeps $C$ and $C\Gamma$ | COMPUTED (to rounding) | Notebook 21d, In [16] |
| $C$, $C\Gamma$ symmetric: no Majorana-type mass term for anticommuting components; charge 2 for commuting ones | PROVED (above); COMPUTED | Notebook 21d, In [16] and In [17] |

### 21.33 Example: Notebook 21d computes the three conditions and the scorecard

Notebook 21d computes the worked examples of Sections 21.3, 21.5, 21.6, 21.31 and 21.32 and draws the scorecard. It counts $\mathcal{B}$, $L$ and $Q_{\mathrm{el}}$ in four processes with exact fractions; it proves the net baryon number of the decay model with sympy; it checks the equilibrium surplus and evaluates the worked example; it solves the rate model in closed form with the incomplete gamma function and integrates it with RK4; then it turns to the theory: it applies condition 1 with the record's verdict, evaluates the record's Lagrangian at a point of the author's metric for $\Psi$, $\Psi^\ast$, $\Gamma\Psi$ and $\Gamma\Psi^\ast$, solves for every invariant Majorana-type matrix, and builds the scorecard from the PASS verdicts of the record. It uses no measured number. It runs in about 20 seconds; the times measured on the build computer, which depend on how busy that computer is, are recorded in the notebook's provenance file `Revision/textbook/notebooks/21d_sakharov_scorecard.PROVENANCE.md`. It needs no Rust, prints 19 PASS lines and draws eight figures.

<!-- NOTEBOOK 21d -->

### 21.36 Line-by-line walk-through of Notebook 21d

The notebook has 20 code cells, In [1] to In [20].

**In [1], the set-up cell.** It is the set-up cell of Notebook 21a, explained line by line in Section 21.15 under In [1], except that the comment lines at the top hold the run instructions of Notebook 21d (Section 21.34) and that the line

```python
NOTEBOOK_ID = "21d"  # this notebook: chapter 21, example d
```

names this notebook. The cell prints Set-up of notebook 21d complete.

**In [2]: the verdicts of the Revision record.**

```python
from fractions import Fraction  # exact fractions such as 1/3

import mpmath  # numbers with many digits and special functions
import numpy as np  # numbers, arrays, matrices
import sympy as sp  # exact algebra
```

`Fraction` computes with exact fractions such as $1/3$; `mpmath` computes with as many digits as asked and knows special functions such as the incomplete gamma function of Section 21.6.

```python
def load_checks(path):
    """name -> verdict (upper case) of every check of a Revision report."""
    entries = json.loads(repository_file(path).read_text(encoding="utf-8"))["checks"]
    return {c["name"]: c["verdict"].upper() for c in entries}
```

The helper of Notebook 21c: a Revision report becomes a dictionary from check name to verdict in capitals.

```python
LEAD_FILE = "Revision/lead_checks/reports/charge-conjugation-and-u1.json"
PAIR_FILE = "Revision/pairing/reports/wolfram-pairing.json"
ALGEBRA_FILE = "Revision/algebra/reports/python-algebra.json"
KS_FILE = "Revision/field_equations_a4/reports/ks-source-conditions.json"
LEAD, PAIR = load_checks(LEAD_FILE), load_checks(PAIR_FILE)
ALGEBRA, KS = load_checks(ALGEBRA_FILE), load_checks(KS_FILE)
```

The four reports on which the scorecard rests: the lead checks of charge conjugation and U(1) conservation, the Wolfram pairing report, the sympy algebra report, and the record of the Kohn-Sham source conditions of the $a_4$ equations.

```python
USED = [(LEAD_FILE, LEAD, "u1_noether_matrix_identity"),
        (LEAD_FILE, LEAD, "representation_real"),
        (LEAD_FILE, LEAD, "spinor_connection_real"),
        (LEAD_FILE, LEAD, "bilinears_under_charge_conjugation"),
        (LEAD_FILE, LEAD, "quantum_charge_conjugation_unitary_type"),
        (PAIR_FILE, PAIR, "T1_current_primordial_commuting"),
        (PAIR_FILE, PAIR, "T1_current_primordial_grassmann"),
        (PAIR_FILE, PAIR, "T1_Lagrangian_primordial_commuting"),
        (ALGEBRA_FILE, ALGEBRA, "spin_commutant_dimension_2"),
        (KS_FILE, KS, "ks_history_is_a_prescribed_background")]
for path, verdicts, name in USED:
    say(f"record {path.split('/')[-1]}: {name} = {verdicts[name]}")
```

The ten record checks the notebook will use, each as a triple (file, its verdicts, check name). Two of them, `representation_real` (the gammas, $C$ and the $S^{ab}$ are real) and `spinor_connection_real` (every entry of every $\Omega_\mu$ is real), are the facts on which the exact same-mass conjugation of the commuting field rests (Section 21.31); the scorecard of In [18] uses them. The loop prints the file name (`split` cuts the path at every slash, and the index `[-1]` takes the last part), the check name and its verdict: Out [2] shows ten lines, all PASS.

**In [3]: counting conserved numbers.**

```python
QUARK = {"u": (Fraction(1, 3), Fraction(2, 3)),  # (B, Q) of the up quark
         "d": (Fraction(1, 3), Fraction(-1, 3))}  # (B, Q) of the down quark
```

The baryon number and electric charge of the up and down quarks, as exact fractions.

```python
def hadron(quarks="", antiquarks=""):
    """(B, L, Q) of a particle made of the given quarks and antiquarks."""
    B = sum(QUARK[x][0] for x in quarks) - sum(QUARK[x][0] for x in antiquarks)
    Q = sum(QUARK[x][1] for x in quarks) - sum(QUARK[x][1] for x in antiquarks)
    return (B, Fraction(0), Q)
```

A particle made of quarks: a string such as `"uud"` is read letter by letter, the numbers of its quarks are added and those of its antiquarks subtracted (the addition rule of Section 21.3); the lepton number is 0. The function returns the triple $(\mathcal{B}, L, Q_{\mathrm{el}})$.

```python
PARTICLE = {"p": hadron("uud"), "n": hadron("udd"), "pbar": hadron("", "uud"),
            "pi+": hadron("u", "d"), "pi-": hadron("d", "u"), "pi0": hadron("u", "u"),
            "e-": (0, 1, -1), "e+": (0, -1, 1), "nubar": (0, -1, 0), "gamma": (0, 0, 0)}
```

The particles of the four processes with their triples: the proton, neutron, antiproton and pions from their quark content (the neutral pion as $u\bar u$), the leptons and the photon directly.

```python
PROCESSES = [("neutron decay", ["n"], ["p", "e-", "nubar"]),
             ("annihilation", ["p", "pbar"], ["pi+", "pi-", "pi0"]),
             ("pair creation", ["gamma", "p"], ["p", "e-", "e+"]),
             ("proton decay", ["p"], ["e+", "pi0"])]
changes, totals = {}, {}  # process -> changes of (B, L, Q); totals before, after
```

The four processes, each with its name, the particles before and the particles after; two empty dictionaries for the results.

```python
for label, before, after in PROCESSES:
    total_before = [sum(PARTICLE[x][k] for x in before) for k in range(3)]
    total_after = [sum(PARTICLE[x][k] for x in after) for k in range(3)]
    totals[label] = (total_before, total_after)
    changes[label] = [a - b for a, b in zip(total_after, total_before)]
    say(f"{label:14}: {' + '.join(before):10} -> {' + '.join(after):15} "
        f"change of (B, L, Q) = ({', '.join(str(c) for c in changes[label])})")
```

For each process the three totals before and after (for each $k = 0, 1, 2$ the sum of the $k$-th number over the particles), and the changes, after minus before. The printed line pads the name to 14 and the two lists to 10 and 15 characters. Out [3] shows the changes $(0, 0, 0)$ for the three observed processes and $(-1, -1, 0)$ for proton decay.

```python
check(PARTICLE["p"] == (1, 0, 1) and PARTICLE["n"] == (1, 0, 0)
      and PARTICLE["pi+"][2] == 1 and PARTICLE["pi0"] == (0, 0, 0),
      "quark content: p has (B, L, Q) = (1, 0, 1), n (1, 0, 0), pi+ charge 1")
check(all(changes[p[0]] == [0, 0, 0] for p in PROCESSES[:3])
      and changes["proton decay"] == [-1, -1, 0],
      "three observed processes conserve B, L, Q; proton decay changes B and L by -1")
```

The quark-content values of Section 21.3, and the bookkeeping: the first three processes (`PROCESSES[:3]`) conserve all three numbers, proton decay would change $\mathcal{B}$ and $L$ by $-1$.

**In [4]: the bookkeeping as a picture.**

```python
REACTIONS = ["$n \\to p\\,e^-\\bar\\nu_e$", "$p\\,\\bar p \\to \\pi^+\\pi^-\\pi^0$",
             "$\\gamma\\,p \\to p\\,e^-e^+$", "$p \\to e^+\\pi^0$ (never seen)"]
table = np.array([[float(totals[p[0]][side][k]) for k in range(3)
                   for side in (0, 1)] for p in PROCESSES])  # rows: processes
```

The reactions written in LaTeX for the row labels. `table` has one row per process and six columns: for each of the three numbers its total before (`side` 0) and after (`side` 1), as decimal numbers.

```python
fig, ax = plt.subplots(figsize=(10.0, 4.2))
ax.imshow(table, cmap="RdBu_r", vmin=-2.5, vmax=2.5, aspect="auto")
for row in range(len(PROCESSES)):
    for col in range(6):
        value = table[row, col]
        ax.text(col, row, "0" if value == 0 else f"{value:+.0f}", ha="center",
                va="center", fontsize=11)
```

The table as coloured squares (red positive, blue negative), with each total written in its square with its sign (`+.0f`: a sign and no decimals).

```python
        if col % 2 == 1 and table[row, col] != table[row, col - 1]:  # a change
            for c in (col - 1, col):
                ax.add_patch(plt.Rectangle((c - 0.46, row - 0.44), 0.92, 0.88,
                                           fill=False, linewidth=2.5))
```

In every "after" column (the odd column numbers) the total is compared with the "before" column to its left; if they differ, a black frame (`plt.Rectangle` with lower-left corner, width and height, not filled) is drawn around both squares.

```python
ax.set_xticks(range(6), ["$B$ before", "$B$ after", "$L$ before", "$L$ after",
                         "$Q$ before", "$Q$ after"])
ax.set_yticks(range(len(PROCESSES)), [f"{p[0]}\n{r}" for p, r in
                                      zip(PROCESSES, REACTIONS)], fontsize=9)
for x in (1.5, 3.5):
    ax.axvline(x, color="black", linewidth=1)
ax.grid(False)
ax.set_title("Bookkeeping: only proton decay would change $B$ (and $L$)")
```

Column labels, row labels (the process name and, below it, the reaction), two vertical lines that separate the three numbers, and a title.

```python
save_figure(fig, "bookkeeping",
            "The totals of the baryon number $B$, the lepton number $L$ and the "
            "electric charge $Q$ before and after four processes (rows): neutron "
            "decay, proton-antiproton annihilation into three pions and pair "
            "creation near a proton (all observed), and proton decay into a "
            "positron and a pion (never observed); columns the number and the side "
            "of the process, colour and figure the total (red positive, blue "
            "negative, pure numbers). Black frames mark the numbers that change: "
            "only proton decay would change $B$ and $L$, the kind of process that "
            "Sakharov's first condition requires.")
```

Figure 21d.1. **What the figure shows.** Three rows in which each "after" square has the colour of its "before" square, and one row, proton decay, with two framed pairs: $\mathcal{B}$ from $+1$ to $0$ and $L$ from $0$ to $-1$.

**In [5]: the decay model.**

```python
r, rbar, B1, B2, N = sp.symbols("r rbar B1 B2 N", real=True)
from_X = r * B1 + (1 - r) * B2  # average baryon number made by one X
from_Xbar = -rbar * B1 - (1 - rbar) * B2  # by one antiparticle
net = sp.expand(N * (from_X + from_Xbar))  # N particles and N antiparticles
```

Five real symbols ($r$, $\bar r$, $\mathcal{B}_1$, $\mathcal{B}_2$, $N$), the two averages of Section 21.5, and the multiplied-out net baryon number.

```python
check(sp.expand(net - N * (r - rbar) * (B1 - B2)) == 0,
      "net baryon number = N (r - rbar) (B1 - B2) exactly")
```

The factorised form of Section 21.5 holds exactly.

```python
example = net.subs({N: 1, B1: sp.Rational(2, 3), B2: sp.Rational(-1, 3),
                    r: sp.Rational(3, 5), rbar: sp.Rational(1, 2)})
report("net baryon number per pair X, Xbar for r = 0.6, rbar = 0.5", example)
check(example == sp.Rational(1, 10)
      and net.subs(B2, B1) == 0 and net.subs(rbar, r) == 0,
      "example 1/10 per pair; zero when B1 = B2 or when r = rbar")
```

The worked example with exact fractions: $1/10$ per pair (printed as a RESULT line). Replacing $\mathcal{B}_2$ by $\mathcal{B}_1$, or $\bar r$ by $r$, gives exactly zero: the two conditions.

**In [6]: the decay model as a map.**

```python
grid = np.linspace(0.0, 1.0, 201)  # values of r and rbar from 0 to 1
R, RBAR = np.meshgrid(grid, grid)
net_f = sp.lambdify((r, rbar, B1, B2), net.subs(N, 1), "numpy")
fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.4), sharey=True)
```

201 values from 0 to 1 for each probability, all their pairs, and the net number per pair ($N = 1$) as a fast function.

```python
for ax, (b1, b2), title in ((axes[0], (2 / 3, -1 / 3), "$B$ violated: $B_1 = 2/3$, "
                             "$B_2 = -1/3$"),
                            (axes[1], (1 / 3, 1 / 3), "$B$ conserved: "
                             "$B_1 = B_2 = 1/3$")):
    values = net_f(R, RBAR, b1, b2) + 0 * R  # + 0 * R: an array even when constant
    image = ax.pcolormesh(R, RBAR, values, cmap="RdBu_r", vmin=-1, vmax=1,
                          shading="auto")
```

Two cases: channels of baryon number $2/3$ and $-1/3$, and two channels of the same baryon number $1/3$. In the second case the expression is the constant zero, and a function that returns a constant returns a single number; adding `0 * R` turns it into an array of the right shape. `pcolormesh` colours the plane of $(r, \bar r)$.

```python
    ax.plot([0, 1], [0, 1], "--", color="black", linewidth=1,
            label="$r = \\bar r$ (no C, CP violation)")
    ax.set_xlabel("branching probability $r$ of $X$")
    ax.set_title(title)
    ax.legend(fontsize=8, loc="upper left")
axes[0].set_ylabel("branching probability $\\bar r$ of $\\bar X$")
fig.colorbar(image, ax=axes, shrink=0.85, label="net baryon number per pair")
```

A dashed diagonal marks $r = \bar r$; labels, legend and colour bar follow.

```python
save_figure(fig, "decay_asymmetry",
            "The net baryon number $(r - \\bar r)(B_1 - B_2)$ made by the decays of "
            "one toy particle $X$ and its antiparticle, versus the branching "
            "probability $r$ of $X$ (horizontal) and $\\bar r$ of $\\bar X$ "
            "(vertical), colour the net number (red positive, blue negative). Left: "
            "channels with $B_1 = 2/3$ and $B_2 = -1/3$ (baryon number violated); "
            "the net number vanishes only on the diagonal $r = \\bar r$. Right: "
            "channels with equal baryon number; the net number is zero everywhere. "
            "An asymmetry needs both conditions 1 and 2.")
```

Figure 21d.2. **What the figure shows.** Left: red below the diagonal ($r > \bar r$), blue above it, white on it; the colour is strongest in the corners, where $r - \bar r = \pm1$. Right: uniformly white: without a change of baryon number no asymmetry, whatever the probabilities.

**In [7]: the equilibrium occupations.**

```python
E_T, mu_T = sp.symbols("E_T mu_T", real=True)  # E / T and mu / T
f_plus = 1 / (sp.exp(E_T - mu_T) + 1)
f_minus = 1 / (sp.exp(E_T + mu_T) + 1)
difference = sp.sinh(mu_T) / (sp.cosh(E_T) + sp.cosh(mu_T))
```

Symbols for $E/T$ and $\mu/T$, the two Fermi-Dirac occupations and the formula of Section 21.5 for their difference.

```python
check(sp.simplify((f_plus - f_minus - difference).rewrite(sp.exp)) == 0,
      "f+ - f- = sinh(mu/T) / (cosh(E/T) + cosh(mu/T)) exactly")
```

`.rewrite(sp.exp)` writes $\sinh$ and $\cosh$ with exponentials; the difference then simplifies to zero: the line-by-line derivation of Section 21.5 is confirmed.

```python
at_zero = [float(f.subs({E_T: 2, mu_T: 0})) for f in (f_plus, f_minus)]
at_tenth = [float(f.subs({E_T: 2, mu_T: sp.Rational(1, 10)}))
            for f in (f_plus, f_minus)]
report("f+ = f- at E = 2T, mu = 0", f"{at_zero[0]:.6f}")
report("f+, f- at E = 2T, mu = 0.1 T", f"{at_tenth[0]:.6f}, {at_tenth[1]:.6f}")
report("surplus of particles per state", f"{at_tenth[0] - at_tenth[1]:.6f}")
```

The worked example: both occupations at $E = 2T$, $\mu = 0$, and at $\mu = 0.1T$. Out [7] prints $0.119203$; $0.130108$ and $0.109097$; and the surplus $0.021012$.

```python
check(at_zero[0] == at_zero[1] and abs(at_zero[0] - 1 / (np.exp(2) + 1)) < 1e-15
      and at_tenth[0] > at_tenth[1],
      "mu = 0: equal occupations 1/(e^2 + 1); mu > 0: more particles")
```

At $\mu = 0$ the two occupations are equal to $1/(e^2 + 1)$; at $\mu > 0$ particles are more common.

**In [8]: the surplus against the energy.**

```python
energies = np.linspace(0.0, 8.0, 321)  # E / T from 0 to 8
diff_f = sp.lambdify((E_T, mu_T), difference, "numpy")
fig, ax = plt.subplots(figsize=(7.5, 4.3))
for mu_value, style in ((0.2, "-"), (0.1, "--"), (0.05, "-."), (0.0, ":")):
    ax.plot(energies, diff_f(energies, mu_value) + 0 * energies, style, linewidth=2,
            label=f"$\\mu/T = {mu_value}$")
```

321 energies from 0 to $8T$, the surplus as a fast function, and one curve for each of four chemical potentials (with `+ 0 * energies` for the same reason as in In [6]).

```python
ax.plot([2.0], [at_tenth[0] - at_tenth[1]], "o", color="black",
        label="worked example $E = 2T$, $\\mu = 0.1T$")
ax.set_xlabel("energy $E/T$")
ax.set_ylabel("$f_+ - f_-$ (particles minus antiparticles per state)")
ax.set_title("In equilibrium with $\\mu = 0$ there is no surplus")
ax.legend(fontsize=8)
```

A black dot at the worked example, axis labels, title and legend.

```python
save_figure(fig, "equilibrium_occupations",
            "The surplus $f_+ - f_- = \\sinh(\\mu/T)/(\\cosh(E/T) + \\cosh(\\mu/T))$ "
            "of particles over antiparticles per quantum state in thermal "
            "equilibrium, versus the energy $E/T$ of the state (horizontal) for the "
            "chemical potentials $\\mu/T = 0.2, 0.1, 0.05, 0$ (pure numbers). The "
            "dot is the worked example $E = 2T$, $\\mu = 0.1T$. When the reactions "
            "that change the baryon number are in equilibrium, $\\mu = 0$ and the "
            "surplus vanishes at every energy (dotted line).")
```

Figure 21d.3. **What the figure shows.** Three curves that start near $\tanh(\mu/2T)$ at $E = 0$ and fall towards zero for large energies, the higher the larger $\mu$; the curve for $\mu = 0$ is the horizontal axis itself.

**In [9]: the rate model in closed form.**

```python
t, s_, K_s, eps_s = sp.symbols("t s K epsilon", positive=True)
Delta = (sp.exp(-t) - sp.exp(-K_s * t)) / (K_s - 1)  # line 2
W = K_s * (1 - sp.exp(-t))  # line 3
```

Positive symbols for the time and the rate (two further symbols, for $s$ and $\epsilon$, are created but not used below), and the two functions $\Delta(t)$ and $W(t)$ of Section 21.6.

```python
line2_ok = (sp.simplify(sp.diff(Delta, t) - (-K_s * Delta + sp.exp(-t))) == 0
            and Delta.subs(t, 0) == 0)
line3_ok = sp.simplify(sp.diff(W, t) - K_s * sp.exp(-t)) == 0
check(line2_ok and line3_ok, "rate model: Delta(t) and W(t) solve lines 1 to 3")
mpmath.mp.dps = 30  # work with 30 significant digits
```

$\Delta$ solves $d\Delta/dt = -K\Delta + e^{-t}$ with $\Delta(0) = 0$, and $dW/dt = Ke^{-t}$: lines 1 to 3. mpmath is told to work with 30 significant digits.

```python
def efficiency(K):
    """eta(K) = K/(K - 1) ((1 - e^-K)/K - K^-K gamma(K, K)), K != 1."""
    K = mpmath.mpf(K)
    incomplete = mpmath.gammainc(K, 0, K)  # the lower incomplete gamma(K, K)
    return float(K / (K - 1) * ((1 - mpmath.exp(-K)) / K - K ** (-K) * incomplete))


for K in (0.1, 3.0, 30.0):
    say(f"K = {K:5}: eta = {efficiency(K):.10f}")
```

The closed form of line 6. `mpmath.mpf` makes a 30-digit number; `mpmath.gammainc(K, 0, K)` is $\int_0^Ku^{K - 1}e^{-u}du = \gamma(K, K)$. The result is returned as an ordinary decimal number. Out [9] prints $\eta = 0.9955325865$, $0.4110164748$ and $0.0344827586$ for $K = 0.1$, $3$ and $30$.

**In [10]: the rate model integrated with RK4.**

```python
def integrate(K, eps=1.0, erase=True, keep_every=50):
    """RK4 for (n, a) from t = 0 to 60 + 40/K; returns the final state and the
    history (every keep_every-th step)."""
    t_end = 60.0 + 40.0 / K  # long enough for n and n_eq to be negligible
    steps = int(np.ceil(t_end / min(0.1 / K, 0.02)))  # step below 0.1/K
    dt = t_end / steps
```

The integration runs to $t = 60 + 40/K$, by which time $n$ and $n_{eq}$ are negligible (for slow decays $n$ approaches $n_{eq}$ only on the time scale $1/K$). The step is at most $0.1/K$ and at most $0.02$; `np.ceil` rounds the number of steps up to a whole number, and `dt` is the exact step.

```python
    def rates(time, y):
        n_eq = np.exp(-time)
        return np.array([-K * (y[0] - n_eq),
                         eps * K * (y[0] - n_eq) - (K * n_eq * y[1] if erase else 0)])
```

The right sides of the two equations of Section 21.6 for the state $y = (n, a)$; with `erase=False` the erasing term is left out.

```python
    y, time, history = np.array([1.0, 0.0]), 0.0, [(0.0, 1.0, 0.0)]
    for step in range(steps):
        k1 = rates(time, y)
        k2 = rates(time + dt / 2, y + dt / 2 * k1)
        k3 = rates(time + dt / 2, y + dt / 2 * k2)
        k4 = rates(time + dt, y + dt * k3)
        y = y + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        time += dt
        if (step + 1) % keep_every == 0:
            history.append((time, y[0], y[1]))
    return y, np.array(history)
```

The classical fourth-order **Runge-Kutta method** (Chapter 2): from the start $n = 1$, $a = 0$, each step evaluates the slopes at the beginning, twice in the middle and at the end of the step, and advances with their weighted average; the error over a fixed time falls like $dt^4$. Every 50th state is kept for the figure.

```python
RATES = (0.1, 3.0, 30.0)
runs = {K: integrate(K) for K in RATES}
for K in RATES:
    say(f"K = {K:5}: RK4 a(infinity) = {runs[K][0][1]:.10f}, "
        f"closed form {efficiency(K):.10f}")
check(all(abs(runs[K][0][1] - efficiency(K)) < 1e-7 for K in RATES),
      "RK4 agrees with the closed form eta(K) to 1e-7 for K = 0.1, 3, 30")
```

The three integrations with $\epsilon = 1$; the final asymmetry (`runs[K][0][1]`, the second entry of the final state) is printed next to the closed form. Out [10] shows agreement to 10 decimals for $K = 0.1$ and $30$ and to $5 \times 10^{-10}$ for $K = 3$ ($0.4110164753$ against $0.4110164748$); the check demands $10^{-7}$.

```python
no_cp, _ = integrate(3.0, eps=0.0)
no_erase, _ = integrate(3.0, erase=False)
check(no_cp[1] == 0.0 and abs(no_erase[1] - 1.0) < 1e-9,
      "controls: eps = 0 gives a = 0 exactly; without erasing a(infinity) = eps")
```

The two controls of Section 21.6: with $\epsilon = 0$ the asymmetry stays exactly zero; without the erasing term the final asymmetry is $\epsilon = 1$.

**In [11]: the histories.**

```python
fig, axes = plt.subplots(2, 1, figsize=(8.0, 6.6), sharex=True)
times = np.linspace(0.0, 60.0, 601)
axes[0].semilogy(times, np.exp(-times), color="black", linewidth=1,
                 label="equilibrium $n_{eq} = e^{-t}$")
```

Two panels stacked vertically; the top one draws $n_{eq} = e^{-t}$ on a logarithmic axis from $t = 0$ to $60$.

```python
for K, style in zip(RATES, ["-", "--", ":"]):
    history = runs[K][1]
    shown = history[history[:, 0] <= 60.0]
    axes[0].semilogy(shown[:, 0], shown[:, 1], style, linewidth=2,
                     label=f"$n$, $K = {K}$")
    axes[1].plot(shown[:, 0], shown[:, 2], style, linewidth=2, label=f"$K = {K}$")
```

For each rate the stored history (columns: time, $n$, $a$), restricted to $t \le 60$ (`history[:, 0] <= 60.0` marks the rows to keep); $n$ in the top panel, $a$ in the bottom one.

```python
axes[0].set_ylim(1e-12, 2.0)
axes[0].set_ylabel("heavy pairs (log scale)")
axes[0].legend(fontsize=8, loc="lower left")
axes[1].set_xlabel("time $t$ (units of the cooling time)")
axes[1].set_ylabel("asymmetry $a/\\epsilon$")
axes[1].set_ylim(0.0, 1.05)
axes[1].legend(fontsize=8, loc="center right", bbox_to_anchor=(1.0, 0.68))
```

Axis ranges, labels and legends; `bbox_to_anchor` places the lower legend at the right edge, 68 per cent of the way up.

```python
save_figure(fig, "rate_model_histories",
            "The rate model of decays out of equilibrium for three decay rates $K$. "
            "Top: the number $n$ of heavy pairs (coloured) and the equilibrium "
            "value $n_{eq} = e^{-t}$ (thin black), logarithmic scale. Bottom: the "
            "asymmetry $a/\\epsilon$. Horizontal axis the time in units of the "
            "cooling time (pure numbers). Slow decays ($K = 0.1$) happen late, "
            "far from equilibrium, when nothing erases their product: almost the "
            "whole $\\epsilon$ survives. Fast decays ($K = 30$) keep $n$ close to "
            "$n_{eq}$, and the inverse decays erase almost everything.")
```

Figure 21d.4. **What the figure shows.** Top: for $K = 3$ and $K = 30$ the curves of $n$ lie on or just above the black line of equilibrium; for $K = 0.1$ the curve stays far above it and falls only slowly, like $e^{-Kt}$. Bottom: all three asymmetries rise steadily to their final values (they never decrease in this model): nearly 1 for $K = 0.1$, $0.41$ for $K = 3$ and only $1/29$ for $K = 30$, because the faster the decays, the more of their product the inverse decays erase while it is being made.

**In [12]: the efficiency for all rates.**

```python
K_grid = np.logspace(-2.0, 3.0, 24)  # 24 rates; K = 1 is not among them
eta = np.array([efficiency(K) for K in K_grid])
check(eta[0] > 0.99 and abs(efficiency(1000.0) * 999.0 - 1.0) < 1e-12
      and np.all(np.diff(eta) < 0),
      "efficiency: near 1 for K = 0.01, exactly 1/(K - 1) at K = 1000, decreasing")
```

`np.logspace(-2, 3, 24)` gives 24 rates from $10^{-2}$ to $10^3$, equally spaced on a logarithmic scale (the formula has $K - 1$ in a denominator, and $K = 1$ is not among them). The efficiency is above 0.99 for $K = 0.01$, equals $1/999$ at $K = 1000$ to $10^{-12}$ relative accuracy (the exponentially small terms are invisible), and decreases from each rate to the next (`np.diff` gives the differences of neighbours).

```python
fig, ax = plt.subplots(figsize=(7.5, 4.4))
ax.loglog(K_grid, eta, "-", linewidth=2, label="closed form $\\eta(K)$")
ax.loglog(K_grid[K_grid > 2], 1 / (K_grid[K_grid > 2] - 1), ":", color="black",
          label="$1/(K - 1)$: near equilibrium")
ax.loglog(RATES, [runs[K][0][1] for K in RATES], "o", color="#e34948",
          label="RK4 integration")
ax.set_xlabel("decay rate $K$ (units of the cooling rate)")
ax.set_ylabel("efficiency $a(\\infty)/\\epsilon$")
ax.set_title("Equilibrium erases the asymmetry")
ax.legend(fontsize=8, loc="lower left")
```

Both axes logarithmic: the closed form, the fast-decay limit $1/(K - 1)$ for $K > 2$, and the three RK4 results as red dots.

```python
save_figure(fig, "washout_efficiency",
            "The efficiency $\\eta(K) = a(\\infty)/\\epsilon$ of the rate model: the "
            "fraction of the asymmetry made by the decays that survives, versus "
            "the decay rate $K$, both on logarithmic scales (pure numbers). Solid: "
            "the closed form with the incomplete gamma function; dots: the RK4 "
            "integrations; dotted: the limit $1/(K - 1)$. Slow decays (out of "
            "equilibrium) keep almost all of it; the closer the decays are to "
            "equilibrium (large $K$), the less survives: condition 3.")
```

Figure 21d.5. **What the figure shows.** A flat plateau near 1 for small rates that bends down into a straight line of slope $-1$ for large rates, on which the dotted limit lies; the three red dots sit on the curve.

**In [13]: this theory, condition 1.**

```python
Q_channel = sp.Symbol("Q_channel")  # the common charge of every channel
eps_theory = net.subs({N: 1, B1: Q_channel, B2: Q_channel})  # B1 = B2
a_theory, _ = integrate(0.1, eps=float(eps_theory))  # slow decays, far from equil.
```

In this theory every channel of every process carries the same charge (Section 21.31): the decay formula with $\mathcal{B}_1 = \mathcal{B}_2$ gives the net charge per pair, and the rate model is run with that $\epsilon$ and the slowest rate, as far from equilibrium as in In [10].

```python
say(f"net charge per pair with equal channels: {eps_theory}; rate model: "
    f"a(infinity) = {a_theory[1]}")
check(LEAD["u1_noether_matrix_identity"] == "PASS" and eps_theory == 0
      and a_theory[1] == 0.0,
      "U(1) charge exactly conserved: no net charge in one universe, condition 1 "
      "fails", record=f"{LEAD_FILE}, check u1_noether_matrix_identity")
```

Out [13] prints a net charge 0 and $a(\infty) = 0.0$; the check also demands the record's verdict that the charge is exactly conserved.

**In [14]: this theory, condition 2: the Lagrangian at a point.**

```python
fixture = json.loads(repository_file("Revision/algebra/gammas.json")
                     .read_text(encoding="utf-8"))
gamma = [np.array(mat, dtype=np.int64) for mat in fixture["gamma"]]  # x1 .. x8
C = gamma[7] @ gamma[0] @ gamma[1] @ gamma[2]  # C = g(x8) g(x1) g(x2) g(x3)
Gamma = C @ gamma[3] @ gamma[4] @ gamma[5] @ gamma[6]  # the chirality
```

The Revision gammas, $C$ and $\Gamma$, as in Notebook 21c.

```python
THEORY = {f["key"]: f["wl"] for f in json.loads(repository_file(
    "Revision/theory/field-theory.json").read_text(encoding="utf-8"))["formulas"]}
lagrangian_text = ("L = Cos[z] [ (1/2) sum_mu (Psibar gamma^mu D_mu Psi - (D_mu "
                   "Psibar) gamma^mu Psi) - m S - U(S) ]")
omega_text = ["(1/2) E^a4[x4] Sin[6 H x8]^(1/6) (a4",
              "g[xi].g[x4] + H g[xi].g[x8]) (i = 1, 2, 3)",
              "-(1/2) E^-a4[x4] Sin[6 H x8]^(1/6) (a4",
              "g[x4].g[xt] + H g[xt].g[x8]) (t = 5, 6, 7)", "Omega_x4 = Omega_x8 = 0"]
record_ok = (THEORY["Lagrangian"].startswith(lagrangian_text)
             and all(piece in THEORY["Omega_components"] for piece in omega_text))
```

The record's formulas; the beginning of its Lagrangian and pieces of its spin connection, in the record's notation, which the notebook uses below; `record_ok` is true when the record states them so.

```python
H, z, a4, a4p = 1 / 6, 0.7, 0.4, 0.25  # the point of the author's metric
s16 = np.sin(z) ** (1 / 6)
f = [np.exp(a4) * s16] * 3 + [1.0] + [np.exp(-a4) * s16] * 3 + [1 / np.tan(z)]
```

A point of the author's metric, now with plain numbers: $H = 1/6$, $z = 0.7$, $a_4 = 0.4$, $a_4' = 0.25$; and the eight scale factors there ($1/\tan z = \cot z$).

```python
Omega = []  # the record's formula Omega_components at the point
for mu in range(8):
    if mu < 3:  # x1, x2, x3
        Omega.append(np.exp(a4) * s16 / 2 * (a4p * gamma[mu] @ gamma[3]
                                             + H * gamma[mu] @ gamma[7]))
    elif mu in (4, 5, 6):  # x5, x6, x7: the deflating extra times
        Omega.append(-np.exp(-a4) * s16 / 2 * (a4p * gamma[3] @ gamma[mu]
                                               + H * gamma[mu] @ gamma[7]))
    else:  # x4 and x8
        Omega.append(np.zeros((16, 16)))
gamma_up = [gamma[mu] / f[mu] for mu in range(8)]  # curved gammas at the point
```

The record's spin connection (Section 21.17) evaluated at the point, and the curved gammas.

```python
def lagrangian(p, dp, m, lam):
    """The record's Lagrangian at the point for the field value p and the eight
    first derivatives dp[mu] (commuting components)."""
    bar = np.conj(p) @ C  # Psibar = Psi^dagger C
    kinetic = 0.0
    for mu in range(8):
        D = dp[mu] + Omega[mu] @ p  # D_mu Psi
        Dbar = np.conj(dp[mu]) @ C - bar @ Omega[mu]  # D_mu Psibar
        kinetic += (bar @ gamma_up[mu] @ D - Dbar @ gamma_up[mu] @ p) / 2
    S = bar @ p
    return np.cos(z) * (kinetic - m * S - lam / 2 * S ** 2)
```

The Lagrangian density of the record at the point, as in In [9] of Notebook 21b, with the mass and the coupling as arguments.

```python
rng = np.random.default_rng(2104)  # fixed seed: the same numbers in every run
psi = rng.normal(size=16) + 1j * rng.normal(size=16)
dpsi = rng.normal(size=(8, 16)) + 1j * rng.normal(size=(8, 16))
m_value, lam_value = 0.7, 0.3
```

A fixed random field value and eight derivatives (seed 2104), $m = 0.7$, $\lambda = 0.3$.

```python
values = {
    "L[Psi]": lagrangian(psi, dpsi, m_value, lam_value),
    "L[Psi*]": lagrangian(np.conj(psi), np.conj(dpsi), m_value, lam_value),
    "L[Gamma Psi]": lagrangian(Gamma @ psi, dpsi @ Gamma.T, m_value, lam_value),
    "L[Gamma Psi*]": lagrangian(Gamma @ np.conj(psi), np.conj(dpsi) @ Gamma.T,
                                m_value, lam_value),
    "-L_(-m,-lambda)[Psi]": -lagrangian(psi, dpsi, -m_value, -lam_value)}
```

Five numbers: the Lagrangian of $\Psi$; of $\Psi^\ast$ (value and derivatives conjugated); of $\Gamma\Psi$, whose derivatives are $\Gamma\partial_\mu\Psi$ (each row of `dpsi` times $\Gamma^T$ from the right is $\Gamma$ times that row); of $\Gamma\Psi^\ast$; and minus the Lagrangian of $\Psi$ with the reversed parameters.

```python
for label, value in values.items():
    say(f"{label:21}: {value.real:+.10f} (imaginary part below 1e-12: "
        f"{abs(value.imag) < 1e-12})")
```

Out [14] prints $-11.2851368126$ for $\mathcal{L}[\Psi]$ and $\mathcal{L}[\Psi^\ast]$ and $+8.4767165144$ for the other three, all real.

```python
check(record_ok and all(abs(v.imag) < 1e-12 for v in values.values())
      and abs(values["L[Psi*]"] - values["L[Psi]"]) < 1e-12,
      "commuting field: L[Psi*] = L[Psi], the same-mass conjugation is exact")
check(abs(values["L[Gamma Psi]"] - values["-L_(-m,-lambda)[Psi]"]) < 1e-12
      and abs(values["L[Gamma Psi*]"] - values["-L_(-m,-lambda)[Psi]"]) < 1e-12
      and PAIR["T1_Lagrangian_primordial_commuting"] == "PASS",
      "L[Gamma Psi] = L[Gamma Psi*] = -L_(-m,-lambda)[Psi]: these maps reverse m",
      record=f"{PAIR_FILE}, check T1_Lagrangian_primordial_commuting")
```

The same-mass conjugation keeps the Lagrangian (Section 21.31); $\Gamma$ and $\Gamma\Psi^\ast$ map it to minus the Lagrangian with $(-m, -\lambda)$ (theorem T1).

```python
check(LEAD["bilinears_under_charge_conjugation"] == "PASS"
      and LEAD["quantum_charge_conjugation_unitary_type"] == "PASS",
      "record: calC_+ keeps S and reverses J (commuting); the quantised field has "
      "only the mass-reversing conjugation",
      record=f"{LEAD_FILE}, check quantum_charge_conjugation_unitary_type")
```

The two record verdicts on which row 2 of the scorecard rests.

**In [15]: the five Lagrangian values as bars.**

```python
fig, ax = plt.subplots(figsize=(8.5, 4.3))
labels = ["$\\mathcal{L}_{m,\\lambda}[\\Psi]$", "$\\mathcal{L}_{m,\\lambda}[\\Psi^*]$",
          "$\\mathcal{L}_{m,\\lambda}[\\Gamma\\Psi]$",
          "$\\mathcal{L}_{m,\\lambda}[\\Gamma\\Psi^*]$",
          "$-\\mathcal{L}_{-m,-\\lambda}[\\Psi]$"]
colours = ["#2a78d6", "#2a78d6", "#e34948", "#e34948", "#999999"]
ax.bar(range(5), [v.real for v in values.values()], color=colours)
ax.axhline(0.0, color="black", linewidth=0.8)
ax.set_xticks(range(5), labels, fontsize=9)
ax.set_ylabel("value of the Lagrangian density at the point")
ax.set_title("Same-mass conjugation keeps $\\mathcal{L}$; $\\Gamma$ reverses the mass")
```

Five bars with LaTeX labels: blue for $\Psi$ and $\Psi^\ast$, red for the two images, grey for the comparison value.

```python
save_figure(fig, "lagrangian_maps",
            "The Lagrangian density of the Revision record for the commuting field "
            "at one point of the author's metric ($H = 1/6$, $z = 0.7$, $a_4 = 0.4$, "
            "$a_4' = 0.25$, $m = 0.7$, $\\lambda = 0.3$, a fixed field value and "
            "fixed first derivatives): for $\\Psi$ and its same-mass conjugate "
            "$\\Psi^\\ast$ (blue, equal), for the images $\\Gamma\\Psi$ and "
            "$\\Gamma\\Psi^\\ast$ (red) and for minus the Lagrangian of the reversed "
            "mass and coupling (grey); vertical axis the value (pure numbers). The "
            "red bars equal the grey one: $\\Gamma$ maps the theory with $(m, "
            "\\lambda)$ to the theory with $(-m, -\\lambda)$.")
```

Figure 21d.6. **What the figure shows.** Two equal blue bars below zero ($-11.29$) and three equal bars above zero ($+8.48$).

**In [16]: the invariant Majorana-type matrices.**

```python
from sympy.polys.matrices import DomainMatrix  # exact matrices over the rationals

I16 = np.eye(16, dtype=np.int64)
pairs = [(a, b) for a in range(8) for b in range(a + 1, 8)]  # the 28 generators
S2 = {(a, b): gamma[a] @ gamma[b] for a, b in pairs}  # 2 S^ab = gamma^a gamma^b
```

The exact solver of Notebook 21a, the identity, the 28 pairs of directions and, for each, $2S^{ab} = \gamma^a\gamma^b$ (twice the generator: whole numbers, and the factor 2 does not change the solutions of the homogeneous equations).

```python
# unknown M read row by row: S^T M -> kron(S^T, 1), M S -> kron(1, S^T)
system = np.vstack([np.kron(S.T, I16) + np.kron(I16, S.T) for S in S2.values()])
null = DomainMatrix.from_list(system.tolist(), sp.QQ).nullspace().to_Matrix()
basis = np.array([np.array(null.row(k).tolist()[0], dtype=float)
                  for k in range(null.rows)])  # each row: one solution, 256 numbers
```

With $M$ read row by row as in Notebook 21a, $S^TM$ is `np.kron(S.T, I16)` applied to it and $MS$ is `np.kron(I16, S.T)` applied to it; the 28 blocks of 256 equations are stacked and solved exactly. Each row of `basis` is one solution, 256 decimal numbers.

```python
CG = C @ Gamma
span_ok = all(np.linalg.matrix_rank(np.vstack([basis, M.reshape(1, -1)])) == 2
              for M in (C, CG))
say(f"{system.shape[0]} equations; dimension of the solution space: {null.rows}")
```

$C\Gamma$; and `span_ok` is true when adding $C$ (or $C\Gamma$) as a third row to the two basis rows leaves the rank at 2, that is, when each lies in the space of solutions. Out [16] prints 7168 equations and dimension 2.

```python
check(null.rows == 2 and span_ok
      and all(np.array_equal(C @ S @ C, -S.T) for S in S2.values())
      and ALGEBRA["spin_commutant_dimension_2"] == "PASS",
      "invariant Majorana-type matrices: a 2-dimensional space spanned by C, C Gamma",
      record=f"{ALGEBRA_FILE}, check spin_commutant_dimension_2")
```

The space has dimension 2 and is spanned by $C$ and $C\Gamma$; the identity $CSC = -S^T$ of Section 21.32 holds for all 28 generators; the algebra record's commutant has dimension 2.

```python
ETA = [1, 1, 1, -1, -1, -1, -1, 1]


def exp_generator(a, b, theta):
    """exp(theta S^ab) for S^ab = gamma^a gamma^b / 2 (a rotation or a boost)."""
    S = S2[(a, b)] / 2
    if ETA[a] * ETA[b] == 1:  # S^2 = -1/4: a rotation
        return np.cos(theta / 2) * np.eye(16) + 2 * np.sin(theta / 2) * S
    return np.cosh(theta / 2) * np.eye(16) + 2 * np.sinh(theta / 2) * S  # a boost
```

The signs of the frame metric, and the finite transformation $e^{\theta S^{ab}}$ by the formulas of Section 21.32: a rotation when the two directions have the same sign of $\eta$, a boost otherwise.

```python
R = exp_generator(0, 1, 0.7) @ exp_generator(0, 3, 0.4) @ exp_generator(4, 7, -1.1)
check(np.allclose(R.T @ C @ R, C) and np.allclose(R.T @ CG @ R, CG)
      and not np.allclose(R.T @ R, np.eye(16)),
      "a finite rotation-boost R keeps C and C Gamma (R^T M R = M), not the identity")
```

A product of a rotation in the plane of $x_1, x_2$ (angle 0.7), a boost in the plane of $x_1, x_4$ (0.4) and a boost in the plane of $x_5, x_8$ ($-1.1$). It keeps $C$ and $C\Gamma$ ($R^TMR = M$), while $R^TR$ is not the identity: the invariance is not an accident of an orthogonal $R$.

```python
symmetric = np.array_equal(C, C.T) and np.array_equal(CG, CG.T)
psi_c = rng.normal(size=16) + 1j * rng.normal(size=16)  # a commuting field value
alpha = 0.9
phase_ok = all(np.isclose((np.exp(1j * alpha) * psi_c) @ M @ (np.exp(1j * alpha)
                                                              * psi_c),
                          np.exp(2j * alpha) * (psi_c @ M @ psi_c)) for M in (C, CG))
check(symmetric and phase_ok and abs(psi_c @ C @ psi_c) > 0.1,
      "C, C Gamma symmetric: zero for anticommuting components; for commuting "
      "ones nonzero, charge 2")
```

Both matrices are symmetric, so the terms vanish for anticommuting components (Section 21.32). For a commuting field value (the generator of In [14] continues), the term $\Psi^TM\Psi$ is multiplied by $e^{2i\alpha}$ when $\Psi$ is multiplied by $e^{i\alpha}$ ($\alpha = 0.9$): charge 2; and $\Psi^TC\Psi$ is not zero.

**In [17]: the two matrices and the phase of the term.**

```python
from matplotlib.colors import LinearSegmentedColormap

SIGNS = LinearSegmentedColormap.from_list("signs", ["#2a78d6", "#f0efec", "#e34948"])
fig, axes = plt.subplots(1, 3, figsize=(13.0, 4.2), width_ratios=[1, 1, 1.3])
```

The blue-white-red colour map and three panels, the last one wider.

```python
for ax, M, title in ((axes[0], C, "$C$ (symmetric)"),
                     (axes[1], CG, "$C\\Gamma$ (symmetric)")):
    image = ax.imshow(M, cmap=SIGNS, vmin=-1, vmax=1)
    ax.set_title(title)
    ax.set_xticks([0, 7, 15], ["1", "8", "16"])
    ax.set_yticks([0, 7, 15], ["1", "8", "16"])
    ax.set_xlabel("column")
    ax.axhline(7.5, color="black", linewidth=0.8)
    ax.axvline(7.5, color="black", linewidth=0.8)
    ax.grid(False)
axes[0].set_ylabel("row")
```

Heat maps of $C$ and $C\Gamma$ with the lines that separate the two halves.

```python
alphas = np.linspace(0.0, np.pi, 91)
majorana = np.array([(np.exp(1j * x) * psi_c) @ C @ (np.exp(1j * x) * psi_c)
                     for x in alphas])
scalar = np.array([np.conj(np.exp(1j * x) * psi_c) @ C @ (np.exp(1j * x) * psi_c)
                   for x in alphas])
base = np.angle(majorana[0])
```

91 phases $\alpha$ from 0 to $\pi$; for each, the Majorana-type term $\Psi^TC\Psi$ and the scalar $\Psi^\dagger C\Psi$ of the rotated field. `np.angle` gives the phase of a complex number; `base` is the phase of the term at $\alpha = 0$.

```python
axes[2].plot(alphas, np.unwrap(np.angle(majorana)) - base, linewidth=2,
             label="$\\Psi^T C\\Psi$: phase $2\\alpha$ (charge 2)")
axes[2].plot(alphas, np.angle(scalar) - np.angle(scalar[0]), "--", linewidth=2,
             label="$\\Psi^\\dagger C\\Psi$: unchanged (charge 0)")
axes[2].set_xlabel("phase $\\alpha$ of $\\Psi \\to e^{i\\alpha}\\Psi$")
axes[2].set_ylabel("change of the phase of the term")
axes[2].legend(fontsize=8)
axes[2].set_title("A Majorana-type term carries charge 2")
```

The change of the phase of each term against $\alpha$. `np.angle` returns values between $-\pi$ and $\pi$, so the phase of the Majorana-type term jumps by $2\pi$ when it passes $\pi$; `np.unwrap` removes these jumps.

```python
save_figure(fig, "majorana_terms",
            "Left and middle: heat maps of the only two matrices $M$ for which a "
            "Majorana-type term $\\Psi^T M\\Psi$ is invariant under the rotations and "
            "boosts of Spin(4,4), $C$ and $C\\Gamma$ (horizontal axis the column, "
            "vertical axis the row, red $+1$, blue $-1$); both are symmetric, so "
            "the term vanishes for anticommuting components. Right: the change of "
            "the phase of $\\Psi^T C\\Psi$ (solid) and of $\\Psi^\\dagger C\\Psi$ "
            "(dashed) for a commuting field under $\\Psi \\to e^{i\\alpha}\\Psi$, "
            "versus $\\alpha$ (radians): the Majorana-type term turns twice as "
            "fast, it carries U(1) charge 2 and would break the charge "
            "conservation.")
```

Figure 21d.7. **What the figure shows.** Left and middle: two block-diagonal patterns, each its own mirror image across the diagonal (symmetric). Right: a straight line of slope 2, reaching $2\pi$ at $\alpha = \pi$, and a flat dashed line at zero.

**In [18]: the scorecard from the record's verdicts.**

```python
def status(passed, text):
    """The status text when the record check passed, otherwise UNSUPPORTED."""
    return text if passed else "UNSUPPORTED"
```

A status is written only if the record check behind it passed; otherwise the row would read UNSUPPORTED (and the check below would fail).

```python
ROWS = [
    ("1. a process changes the number",
     "U(1) charge Q exactly conserved for every history a4 (no flux through the "
     "boundary)",
     status(LEAD["u1_noether_matrix_identity"] == "PASS", "FAILS (PROVED)"),
     "u1_noether_matrix_identity"),
```

Each row has four entries: the condition, what this theory has, the status, and the record check. Row 1: condition 1 fails, proved by the U(1) identity.

```python
    ("2. C and CP violated",
     "commuting field: the same-mass conjugation is an exact symmetry that "
     "reverses the charge, so a C-symmetric start keeps zero charge; quantised "
     "field: the only conjugation, Gamma, reverses the mass; no rates computed",
     status(all(LEAD[name] == "PASS" for name in (
         "representation_real", "spinor_connection_real",
         "bilinears_under_charge_conjugation",
         "quantum_charge_conjugation_unitary_type")),
         "commuting: FAILS (PROVED); quantised: NOT COMPUTED"),
     "representation_real, spinor_connection_real, "
     "bilinears_under_charge_conjugation, quantum_charge_conjugation_unitary_type"),
```

Row 2 has two statuses, one for each field (Section 21.31). For the commuting field dirac16complex00 condition 2 fails: the same-mass conjugation is exact (all matrices of $\mathcal{L}$ are real) and reverses the charge, so by Proposition 2 of Section 21.5 a start in which every configuration and its conjugate are equally likely keeps zero average charge. For the quantised field dirac16complex it is not computed. `all(...)` is `True` only when every one of the four named lead checks has the verdict PASS: `representation_real` and `spinor_connection_real` (the reality of the gammas, of $C$ and of the $\Omega_\mu$), `bilinears_under_charge_conjugation` (the conjugation reverses the current) and `quantum_charge_conjugation_unitary_type` (the quantised field has only the mass-reversing conjugation). Python joins two string pieces that stand next to each other into one text: the last entry is the list of the four checks.

```python
    ("3. out of equilibrium",
     "no rate computed; the Kohn-Sham history is a prescribed background",
     status(KS["ks_history_is_a_prescribed_background"] == "PASS", "NOT COMPUTED"),
     "ks_history_is_a_prescribed_background"),
```

Row 3: not computed; the only history of the record is a prescribed background.

```python
    ("pair level (theorem T1)",
     "the partner Gamma Psi of mass -m carries the opposite current: total charge 0",
     status(PAIR["T1_current_primordial_commuting"] == "PASS"
            and PAIR["T1_current_primordial_grassmann"] == "PASS",
            "PROVED (classical bilinears)"),
     "T1_current_primordial_commuting, T1_current_primordial_grassmann"),
```

The pair-level row: proved for classical bilinears, for both fields.

```python
    ("verdict",
     "no net charge can be made inside one universe; no baryons in the theory",
     status(LEAD["u1_noether_matrix_identity"] == "PASS", "PROBLEM NOT SOLVED"),
     "the checks above")]
for row in ROWS:
    say(f"{row[0]:34} | {row[2]}")
```

The verdict row, and a loop that prints the condition (padded to 34 characters) and the status of each row: Out [18].

```python
check([row[2] for row in ROWS] == ["FAILS (PROVED)",
                                   "commuting: FAILS (PROVED); quantised: NOT COMPUTED",
                                   "NOT COMPUTED", "PROVED (classical bilinears)",
                                   "PROBLEM NOT SOLVED"],
      "scorecard: every status is backed by a PASS verdict of the Revision record")
```

The five statuses must be exactly these, which is possible only if every record check behind them passed.

**In [19]: the scorecard as a figure.**

```python
COLOURS = {"FAILS (PROVED)": "#f4c7c3",
           "commuting: FAILS (PROVED); quantised: NOT COMPUTED": "#f2e2b8",
           "NOT COMPUTED": "#e3e3e3", "PROVED (classical bilinears)": "#cfe8c4",
           "PROBLEM NOT SOLVED": "#f4c7c3"}
fig, ax = plt.subplots(figsize=(13.0, 6.2))
ax.set_xlim(0, 13.0)
ax.set_ylim(0, len(ROWS) + 1)
ax.axis("off")
```

A pale background colour for each status (red for failure, yellow for the two statuses of condition 2, fails for the commuting field and not computed for the quantised one, grey for not computed, green for proved). The figure is used as a drawing area with coordinates from 0 to 13 across and 0 to 6 up; `ax.axis("off")` hides the axes.

```python
columns = [(0.1, 2.4, "Sakharov condition"), (2.6, 4.3, "this theory"),
           (7.1, 2.3, "status"), (9.5, 3.5, "Revision record check")]
for x0, width, heading in columns:
    ax.text(x0, len(ROWS) + 0.5, heading, fontsize=11, fontweight="bold",
            va="center")
```

The four columns, each with its left edge, its width and its heading; the headings are written in bold in the top line.

```python
for k, row in enumerate(ROWS):
    y = len(ROWS) - k - 0.5  # the first row at the top
    ax.add_patch(plt.Rectangle((0.0, y - 0.48), 13.0, 0.96, color=COLOURS[row[2]],
                               zorder=0))
    for (x0, width, _), text in zip(columns, row):
        chars = int(width * 11.5)  # about 11 characters per unit of width
        ax.text(x0, y, textwrap.fill(text, chars, break_long_words=False),
                fontsize=8.5, va="center")  # long check names stay whole
ax.set_title("Sakharov's conditions applied to the theory as built", fontsize=12)
```

For each row, from the top down: a coloured band across the whole width (`zorder=0` puts it behind the text), and the four entries, each broken into lines that fit its column (`textwrap.fill` of the set-up cell; `break_long_words=False` keeps long check names whole).

```python
save_figure(fig, "scorecard",
            "The scorecard of the theory as built against Sakharov's three "
            "conditions, with the status of each row and the Revision record "
            "check it rests on (each status is set by the notebook only when the "
            "record holds that check with the verdict PASS). Condition 1 fails "
            "exactly (the U(1) charge is conserved for every history $a_4$), so "
            "conditions 2 and 3 cannot help; condition 2 also fails for the "
            "commuting field (its same-mass conjugation is exact) and is not "
            "computed for the quantised field; the pair-level statement of theorem "
            "T1 is exact but creates nothing. The theory does not solve the "
            "matter-antimatter problem.")
```

Figure 21d.8. **What the figure shows.** A table of five coloured rows: red for condition 1 (fails) and for the verdict (problem not solved), yellow for condition 2 (fails for the commuting field, not computed for the quantised field), grey for condition 3 (not computed), green for the pair level (proved for classical bilinears), each with the record checks it rests on.

**In [20]: the figure files.**

```python
names = sorted(FIGURE_NUMBERS, key=FIGURE_NUMBERS.get)
check(len(names) == 8 and all(
    output_file(f"{FIGURE_FOLDER}/21d_{FIGURE_NUMBERS[n]}_{n}.png").is_file()
    for n in names), "the eight figure files of notebook 21d exist")
all_checks_passed()
```

The eight figure files exist, and the last line prints ALL 19 CHECKS PASSED (notebook 21d).

### 21.37 The scorecard, pairs of universes as a hypothesis, and what would be needed

**The scorecard.** Figure 21d.8 and the table of Section 21.31 put the three conditions side by side. Condition 1 fails exactly; condition 2 fails exactly for the commuting field and is not computed for the quantised field; condition 3 is not computed; and conditions 2 and 3 could not help while condition 1 fails; the pair-level statement is exact but creates nothing. **The theory as built does not solve the matter-antimatter problem.** It contains no baryons, it cannot change its charge inside one universe, and it predicts no value of the baryon-to-photon ratio $\eta_B$.

**Pairs of universes, stated as a hypothesis.** Theorem T1 suggests a picture of the kind described at the end of Section 21.19: our universe carries some charge, and a partner universe of mass $-m$ carries the opposite charge, so that the pair as a whole is symmetric. The picture rests on three statements, each of which is a **HYPOTHESIS**: nothing in the Revision record derives it.

- **H1 (HYPOTHESIS).** Our universe is one member of a T1 pair: two configurations in the same gravitational field, $\Psi$ with the parameters $(m, \lambda)$ and its partner $\Gamma\Psi$ with $(-m, -\lambda)$, in this correlated configuration.
- **H2 (HYPOTHESIS).** The configuration has a nonzero charge, $Q \ne 0$. Given H1, the partner has $-Q$ by theorem T1; the content of H2 is $Q \ne 0$, and nothing computes its value or its sign.
- **H3 (HYPOTHESIS, not derivable within the theory).** The U(1) charge of the field is the baryon number (or the difference of baryon and lepton numbers). The theory contains no quarks, baryons or leptons, so this cannot be derived from it.

*What would follow, and only for classical fields.* If H1, H2 and H3 held, the two charges would add to zero at every time (theorem T1), each would be separately constant (Section 21.17), and the baryon excess of one member would be balanced by the opposite excess of the other.

*What the picture does not do.*

- It does not produce an asymmetry. Each charge is constant, so a nonzero charge today is the same as a nonzero charge at the start: the asymmetry is an initial condition, put in by H2.
- It does not predict $\eta_B$: neither the size nor the sign of the charge is computed, nor the photons to which $\eta_B$ refers.
- It does not meet Sakharov's conditions; it replaces them by an assumed correlated configuration.
- At the quantum level there is no cancellation between two independently quantised universes: the chirality image is the same quantum system with the Krein metric $-B$, and an independent universe of mass $-m$ carries $+B$ and its own charge (Section 21.19).
- It does not show that pairs are created (Chapter 20), and it does not say that antimatter has negative mass.
- It is a statement about a model in signature (4,4), with four time-like directions, while observed spacetime has one time; applying it to "our universe" is a further assumption.

A published example of the class of universe/anti-universe ideas is the CPT-symmetric universe of Boyle, Finn and Turok, Phys. Rev. Lett. 121, 251301 (2018) (Section 21.19); it is cited as an example of the class only.

**What would have to be added** (all OPEN; none of these ingredients is present in the theory, none is claimed to be natural, and none has been shown to be sufficient):

- *Baryons.* Couplings of the field to the quarks and leptons of the Standard Model of particle physics, or another link between the U(1) charge and the baryon number (H3).
- *A charge-violating interaction* (condition 1). For the commuting field the candidates found in Section 21.32 are the Majorana-type terms $\Psi^TC\Psi$ and $\Psi^TC\Gamma\Psi$ (each with its complex conjugate), of charge 2. For the anticommuting field no Majorana-type mass term exists; a charge-violating term would need derivatives, more fields or new structures, which are not classified here. A remark derived here but not checked by the record: if one such term $g\,\Psi^TM\Psi$ (plus its conjugate) is added, the rotation $\Psi \to e^{i\alpha}\Psi$ changes its coefficient to $g\,e^{2i\alpha}$, so the phase of a single coefficient can be removed by renaming the field; only relative phases between several such terms could be a source of CP violation.
- *C and CP violation in rates* (condition 2): rates of processes of the extended theory, computed and shown to differ between particles and antiparticles.
- *A departure from equilibrium* (condition 3): a dynamical history in which the charge-violating processes run out of equilibrium, for example during the deflation of the extra times, with their rates. The record has only instantaneous Kohn-Sham states along a prescribed history; the time-dependent problem and the back-reaction on $a_4$ are OPEN (Chapters 15, 17 and 22).
- *A computed $\eta_B$*: only with all of the above could a value be computed and compared with the observed $\eta_B \approx 6.1 \times 10^{-10}$ of Section 21.4.

### 21.38 What we proved, what we computed, what we assumed

| statement | status | where it is verified |
| --- | --- | --- |
| the observed excess of matter: $\Omega_bh^2 = 0.0224 \pm 0.0001$, $\eta_B \approx 6.1 \times 10^{-10}$; no antimatter domains | ASSUMED (quoted observations) | the literature cited in Section 21.4 |
| Sakharov's three conditions (Propositions 1 and 2; the equilibrium surplus) | PROVED (Section 21.5) for the stated assumptions; the Fermi-Dirac law and equal particle and antiparticle masses quoted (ASSUMED) | Notebook 21d, In [7] |
| decay model $N(r - \bar r)(\mathcal{B}_1 - \mathcal{B}_2)$; rate model $\eta(K)$ in closed form | PROVED for the ASSUMED toy models; COMPUTED (RK4 to $10^{-7}$) | Notebook 21d, In [5], In [9] to In [12] |
| the gammas are eight real $16 \times 16$ signed permutation matrices with signature (4,4); $C$, $\Gamma$, $B$, $S^{ab}$ as stated | PROVED | `Revision/lead_checks/reports/charge-conjugation-and-u1.json`, `representation_real`, `B_imaginary_hermitian`; Notebook 21a, In [3], In [5] |
| charge conjugation is a matrix: exactly $\mathcal{C}_+ = C$ (same mass) and $\mathcal{C}_- = \Gamma C$ (mass reversed); their transposition rules; both reality conditions consistent | PROVED | the same report, `intertwiners_same_mass`, `intertwiners_reversed_mass`, `charge_conjugation_matrix_plus`, `charge_conjugation_matrix_minus`, `majorana_conditions_consistent`; Notebook 21a, In [6] to In [10] |
| each gamma equation halves the solution space | COMPUTED exactly | Notebook 21a, In [7] |
| signs of $S$, $J$ and of all 256 bilinears for both statistics | PROVED | the same report, `bilinears_under_charge_conjugation`; Notebook 21a, In [14], In [15] |
| real fields: $J = 0$, $\mathcal{C}_+$ the identity, $\Gamma$ the only nontrivial real map, with the mass reversed | PROVED | the same report, `real_fields_charge_conjugation`; Notebook 21a, In [18] |
| on the record's exact solution (any $a_4$): $\Psi^\ast$ solves with $+m$, $\Gamma\Psi^\ast$ with $-m$ | PROVED | `Revision/theory/reports/python-field-theory.json`, `exact_solution_family_x4_x8`; Notebook 21a, In [11] to In [13] |
| the Noether current $J^\mu = -i\bar\Psi\gamma^\mu\Psi$ | PROVED (Section 21.16); COMPUTED at a point | record formula `current`; Notebook 21b, In [9] |
| exact U(1) conservation in the author's metric for every $a_4$; the $a_4'$ terms cancel because $\sqrt{\lvert g\rvert} = \cos z$ | PROVED | lead check `u1_noether_matrix_identity`; Notebook 21b, In [5], In [6] |
| charge balance through the brane; a stationary solution with the constant charge $-1424/1875 - 13\sqrt7/1500 = -0.782397$ | PROVED (sympy) | Notebook 21b, In [10] to In [13] |
| the charge density is indefinite; a rest state of positive frequency with density $-7/25$ | PROVED | Notebook 21b, In [16] |
| theorem T1: the partner $\Gamma\Psi$ has $(-m, -\lambda)$ and the opposite current; a pair has total charge 0 as classical bilinears | PROVED | `Revision/pairing/reports/wolfram-pairing.json`, `T1_current_primordial_commuting`, `T1_current_primordial_grassmann`, `T1_Lagrangian_primordial_commuting`; Notebook 21b, In [11], In [17]; Notebook 21d, In [14] |
| the reflections (P, T types) and their Krein signs | PROVED in the record | the Wolfram pairing report, `T2_Pn_in_Pin44`, `T2_character_of_Pn`, `Q_Krein_metric_of_images` |
| quantised field: only $\Psi \to \Gamma\Psi^{\dagger T}$ keeps the canonical anticommutator; it reverses the mass | PROVED | lead check `quantum_charge_conjugation_unitary_type`; Notebook 21c, In [4], In [6] |
| $Q' = 16 - Q$ (charge reversed up to a constant); $Q'' = Q - 16$ for the same-mass candidate | PROVED (Section 21.26); COMPUTED with explicit operators | Notebook 21c, In [8] |
| one-particle spectra of $\pm m$ identical; inertia (4,4) at real, Krein-neutral at imaginary frequencies | PROVED | Wolfram pairing report, `Q_one_particle_maps`, `Q_one_particle_Krein_signatures`, `Q_one_particle_complex_and_zero_frequencies_Krein_neutral`; Notebook 21c, In [9] to In [12] |
| the same-mass conjugation is an exact symmetry of the commuting field | PROVED (Section 21.31); COMPUTED at a point | `Revision/theory/reports/wolfram-field-theory.json`, `L_real_C`; Notebook 21d, In [14] |
| invariant Majorana-type matrices: exactly $C$ and $C\Gamma$; none for anticommuting components | PROVED | `Revision/algebra/reports/python-algebra.json`, `spin_commutant_dimension_2`; Notebook 21d, In [16] |
| Sakharov condition 1 | FAILS (PROVED) | lead check `u1_noether_matrix_identity`; Notebook 21d, In [13] |
| Sakharov condition 2 (C and CP violation) | dirac16complex00: FAILS (PROVED: $\mathcal{C}_+$ exact, Proposition 2); dirac16complex: NOT COMPUTED (no rates; only the mass-reversing conjugation) | lead checks `representation_real`, `spinor_connection_real`, `bilinears_under_charge_conjugation`, `quantum_charge_conjugation_unitary_type`; Notebook 21d, In [14], In [18] |
| Sakharov condition 3 (departure from equilibrium) | NOT COMPUTED | `Revision/field_equations_a4/reports/ks-source-conditions.json`, `ks_history_is_a_prescribed_background` |
| our universe is one member of a pair; the U(1) charge is the baryon number | HYPOTHESIS | Section 21.37 |
| a creation process, rate or amplitude for universes, in pairs or otherwise | not derived by any equation of the record | Chapter 20; `Revision/docs/PAIR_CREATION_PROOFS.md`, its section 11.2 |
| a regularised quantum theory in signature (4,4); anomalies of the U(1) symmetry | OPEN | not constructed in the record |
| the record's parenthetical remark that normal ordering gives the same-mass candidate the standard signs | OPEN (not supported by the operator computation of Section 21.26) | lead check `bilinears_under_charge_conjugation`, its detail text; Notebook 21c, In [8] |

**In one sentence.** In this theory charge conjugation is a matrix, the charge is exactly conserved while the extra times deflate, a solution and its chirality partner carry opposite charges, and nothing in the theory as built can make more matter than antimatter.

### 21.39 Exercises

1. **Bookkeeping.** Count $Q_{\mathrm{el}}$, $\mathcal{B}$ and $L$ before and after (a) the annihilation $p + \bar p \to \pi^+ + \pi^-$ and (b) the hypothetical decay $n \to p + e^-$ without the antineutrino. Which numbers are conserved?
2. **The decay model.** For $N = 1000$ pairs, $r = 0.51$, $\bar r = 0.49$, $\mathcal{B}_1 = \tfrac23$, $\mathcal{B}_2 = -\tfrac13$, compute the net baryon number with the formula of Section 21.5. Then repeat with $\mathcal{B}_1 = \mathcal{B}_2 = \tfrac13$ and with $r = \bar r = 0.5$.
3. **The equilibrium surplus.** Show that at $E = 0$ the surplus $f_+ - f_-$ of Section 21.5 equals $\tanh(\mu/2T)$, and evaluate it for $\mu = 0.1T$. Then show that for $E$ much larger than $T$ and $\mu$ it is approximately $2\sinh(\mu/T)\,e^{-E/T}$.
4. **The rate model at $K = 2$.** Use $\gamma(2, x) = 1 - (1 + x)e^{-x}$ to compute the efficiency $\eta(2)$ exactly, and check it against the values $\eta(0.1)$ and $\eta(3)$ of Notebook 21d.
5. **Why $C$ is not one of the matrices $M$.** Show that $C$ commutes with the four time-like gammas and anticommutes with the four space-like ones. Explain why this does not contradict $\mathcal{C}_+ = C$.
6. **Real fields carry no current.** For the $2 \times 2$ antisymmetric matrix $A$ with $A_{12} = 1$, $A_{21} = -1$ and $A_{11} = A_{22} = 0$, compute $u^TAu$ for a real column $u = (u_1, u_2)$ and $u^\dagger Au$ for a complex one. What does this say about the current of a real and of a complex field?
7. **The charge of the general exact solution.** For the exact solution $\Psi = \sin^\alpha z\,U(x_4)\chi$ of Section 21.11 with any $\alpha > -\tfrac12$, show that the charge of the patch is $Q(x_4) = f(x_4)/(2\alpha + 1)$ with $f = \chi^\dagger U^TBU\chi$.
8. **A half-way conjugation.** Compute $MB^TM^\dagger$ for $M = (1 + \Gamma)/\sqrt2$, and explain with the formula of Section 21.25 why the result is the zero matrix.
9. **Anticommuting components and a $2 \times 2$ Majorana term.** For two anticommuting components $\Psi_1, \Psi_2$ and the matrix $M$ with entries $M_{11} = a$, $M_{12} = b$, $M_{21} = c$, $M_{22} = d$, compute $\Psi^TM\Psi$. When does it vanish?

### 21.40 Answers to the exercises

**1.** (a) Before: $Q_{\mathrm{el}} = 1 - 1 = 0$, $\mathcal{B} = 1 - 1 = 0$, $L = 0$. After: $Q_{\mathrm{el}} = 1 - 1 = 0$, $\mathcal{B} = 0 + 0 = 0$, $L = 0$. All three are conserved (such annihilations into two pions are observed). (b) Before: $Q_{\mathrm{el}} = 0$, $\mathcal{B} = 1$, $L = 0$. After: $Q_{\mathrm{el}} = 1 - 1 = 0$, $\mathcal{B} = 1 + 0 = 1$, $L = 0 + 1 = 1$. The charge and the baryon number are conserved, the lepton number would change by $+1$: this is why the observed decay contains the antineutrino ($L = -1$), as the table of Section 21.3 shows.

**2.** With the formula $N(r - \bar r)(\mathcal{B}_1 - \mathcal{B}_2)$: $1000 \times (0.51 - 0.49) \times (\tfrac23 + \tfrac13) = 1000 \times 0.02 \times 1 = 20$ baryons. With $\mathcal{B}_1 = \mathcal{B}_2$ the last factor is $0$, and with $r = \bar r$ the middle factor is $0$: no net baryon number in either case (conditions 1 and 2 of Section 21.5).

**3.** At $E = 0$, $\cosh 0 = 1$, so $f_+ - f_- = \sinh(\mu/T)/(1 + \cosh(\mu/T))$. With $u = \mu/2T$ and the double-angle formulas $\sinh 2u = 2\sinh u\cosh u$ and $1 + \cosh 2u = 2\cosh^2u$ (both follow from the definitions with exponentials), this is $2\sinh u\cosh u/(2\cosh^2u) = \tanh u = \tanh(\mu/2T)$. For $\mu = 0.1T$: $\tanh 0.05 = 0.049958$ (to six decimals). For large $E$, $\cosh(E/T) = (e^{E/T} + e^{-E/T})/2 \approx e^{E/T}/2$, which is much larger than $\cosh(\mu/T)$; so $f_+ - f_- \approx \sinh(\mu/T)/(e^{E/T}/2) = 2\sinh(\mu/T)\,e^{-E/T}$: the surplus dies out exponentially with the energy, as figure 21d.3 shows.

**4.** With $K = 2$: $K/(K - 1) = 2$, $(1 - e^{-2})/2$, $K^{-K} = \tfrac14$ and $\gamma(2, 2) = 1 - 3e^{-2}$. So

$$
\eta(2) = 2\Big(\frac{1 - e^{-2}}{2} - \frac{1 - 3e^{-2}}{4}\Big) = (1 - e^{-2}) - \frac{1 - 3e^{-2}}{2} = \frac12 + \frac{e^{-2}}{2} = 0.567668
$$

(multiply out; collect the constants $1 - \tfrac12$ and the terms with $e^{-2}$, $-1 + \tfrac32 = \tfrac12$; $e^{-2} = 0.135335$). It lies between $\eta(0.1) = 0.9955$ and $\eta(3) = 0.4110$, as it must, since $\eta$ decreases with $K$ (Notebook 21d, In [12]). (The formula $\gamma(2, x) = \int_0^xue^{-u}du = 1 - (1 + x)e^{-x}$ follows by integration by parts.)

**5.** $C = \gamma^{(x8)}\gamma^{(x1)}\gamma^{(x2)}\gamma^{(x3)}$. Moving a time-like $\gamma^{(t)}$ through $C$ passes four different gammas, each costing a sign: $(-1)^4 = +1$, so they commute. Moving a space-like gamma that occurs in $C$ passes the three other factors (three signs) and itself (no sign): $(-1)^3 = -1$, so they anticommute. Hence $C$ satisfies neither $C\gamma^a = +\gamma^aC$ for all $a$ nor $C\gamma^a = -\gamma^aC$ for all $a$: it is not one of the matrices $M$ of Theorem CC. There is no contradiction: the charge-conjugation matrix is $\mathcal{C} = MC$, and $\mathcal{C}_+ = C$ belongs to $M = 1$. The map is $\Psi^c = \mathcal{C}_+\bar\Psi^T = C\,C\Psi^\ast = \Psi^\ast$; the matrix $C$ appears twice, once in $\mathcal{C}_+$ and once in the Dirac adjoint, and $CC = 1$.

**6.** $u^TAu = u_1A_{12}u_2 + u_2A_{21}u_1 = u_1u_2 - u_2u_1 = 0$ for real (indeed for any commuting) numbers. For a complex column, $u^\dagger Au = u_1^\ast u_2 - u_2^\ast u_1$, and since $u_2^\ast u_1$ is the conjugate of $u_1^\ast u_2$, this is $2i\,\mathrm{Im}(u_1^\ast u_2)$, which is nonzero in general (for $u = (1, i)$ it is $2i$). The current is $J^a = -i\Psi^\dagger(C\gamma^a)\Psi$ with the antisymmetric $C\gamma^a$: it vanishes for every real field (fact F1 of Section 21.10) and is in general nonzero, and real ($-i \cdot 2i\,\mathrm{Im} = 2\,\mathrm{Im}$), for a complex field. A real field carries no U(1) charge.

**7.** Since $U$ is real, $\Psi^\dagger B\Psi = \sin^{2\alpha}z\,\chi^\dagger U^TBU\chi = \sin^{2\alpha}z\,f(x_4)$. The charge of the patch is $\int_0^{\pi/2}\cos z\,\sin^{2\alpha}z\,dz\;f(x_4)$. Substitute $u = \sin z$, $du = \cos z\,dz$, limits $0$ and $1$: $\int_0^1u^{2\alpha}du = 1/(2\alpha + 1)$ (the power rule of integration, valid for $2\alpha > -1$). So $Q = f/(2\alpha + 1)$; for $\alpha = 1$ this is the $f/3$ of Section 21.18.

**8.** $M = (1 + \Gamma)/\sqrt2$ is $\cos t\,1 + \sin t\,\Gamma$ with $t = \pi/4$. By Section 21.25, $M(t)B^TM(t)^\dagger = -\cos(2t)B$, and $\cos(\pi/2) = 0$: the result is the zero matrix. Directly: $M$ is real and symmetric, so $MB^TM^\dagger = -MBM = -\tfrac12(B + \Gamma B + B\Gamma + \Gamma B\Gamma) = -\tfrac12(B + 0 - B) = 0$, because $\Gamma B = -B\Gamma$ and $\Gamma B\Gamma = -B$. In fact $(1 + \Gamma)/2$ is the projector onto the components 9 to 16, and $B$ joins the two halves (figure 21c.1), so $\tfrac{1 + \Gamma}{2}B\tfrac{1 + \Gamma}{2} = 0$: such an $M$ would give a field whose anticommutator vanishes, which is not a field of the theory at all.

**9.** $\Psi^TM\Psi = a\Psi_1\Psi_1 + b\Psi_1\Psi_2 + c\Psi_2\Psi_1 + d\Psi_2\Psi_2$ (the sum over the four entries). For anticommuting components $\Psi_1\Psi_1 = \Psi_2\Psi_2 = 0$ and $\Psi_2\Psi_1 = -\Psi_1\Psi_2$, so $\Psi^TM\Psi = (b - c)\Psi_1\Psi_2$. It vanishes exactly when $b = c$, that is, when $M$ is symmetric. This is the $2 \times 2$ case of Section 21.32: since $C$ and $C\Gamma$ are symmetric, the anticommuting field dirac16complex has no Majorana-type mass term.
