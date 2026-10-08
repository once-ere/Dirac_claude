## 21. Matter and antimatter from zero: what this theory explains and what it does not

The world we see is made of matter, and almost no antimatter. Why that is so is one of the open questions of physics. This chapter explains the question from zero, with the observations, the three conditions that Andrei Sakharov found for any answer, and small worked models of each condition. Then it asks, condition by condition, what the theory of this book says. On the way it derives, line by line, the facts of the theory that matter for the question: that charge conjugation in this theory is made by a **matrix** (there are exactly two such matrices), that the charge of the field is **exactly conserved** in the author's metric while the three extra times deflate, how the **quantised** field can be conjugated, and what a pair of solutions of masses $+m$ and $-m$ carries. The chapter ends with a scorecard and with a precise list of what the theory as built does not do.

### 21.1 What this chapter does, and the answer first

The request that this book answers ends with the words "this theory solves matter anti-matter mysteries". The honest answer comes first, because every later section supports it.

**The answer.** The theory as built does **not** solve the matter-antimatter problem. The reasons, each of which this chapter proves or documents:

- The theory contains no baryons (no protons, neutrons or quarks), so it cannot say anything about the baryon number of the observed universe.
- The only number of the theory that could play the role of "matter minus antimatter" is the **U(1) charge** $Q$ of its field. It is **exactly conserved**: in the author's metric, for every history $a_4(x_4)$, in particular the one in which ordinary space inflates and the three extra times $x_5, x_6, x_7$ deflate exponentially, no solution can change its charge unless charge flows through the boundary (PROVED, Sections 21.16 to 21.18). So no process described by these equations can make a net charge inside one universe: Sakharov's first condition fails.
- For the commuting field dirac16complex00 the same-mass charge conjugation is an exact symmetry (PROVED, Sections 21.10 and 21.31). No violation of C or CP in reaction rates is built into the theory or computed (NOT COMPUTED). No departure from thermal equilibrium is computed (NOT COMPUTED); the Kohn-Sham history of this book is a prescribed background (Section 21.31).

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

**The metric.** The author's metric is diagonal, with the entries (in the order $x_1, \dots, x_8$)

$$
g = \mathrm{diag}\big(e^{2a_4}s,\ e^{2a_4}s,\ e^{2a_4}s,\ -1,\ -e^{-2a_4}s,\ -e^{-2a_4}s,\ -e^{-2a_4}s,\ \cot^2z\big),\qquad s = \sin^{1/3}z,\quad z = 6Hx_8 .
$$

Its **scale factors** $f_a = \sqrt{|g_{aa}|}$ are $f_1 = f_2 = f_3 = e^{a_4}\sin^{1/6}z$ (ordinary space), $f_4 = 1$ (the time), $f_5 = f_6 = f_7 = e^{-a_4}\sin^{1/6}z$ (the extra times) and $f_8 = \cot z$ (the hidden direction). When $a_4$ grows with the time, ordinary space inflates and the three extra times deflate exponentially. The volume factor is $\sqrt{|\det g|} = f_1f_2\cdots f_8 = e^{3a_4}e^{-3a_4}\sin z\cot z = \cos z$: the inflation of space and the deflation of the extra times cancel, and $a_4$ drops out (Chapter 12; record check `sqrt_abs_det_g_is_cos_z` of `Revision/field_equations_a4/reports/wolfram-a4-report.json`). This one fact will be the reason why the charge is conserved without any time-derivative terms (Section 21.17).

**The gammas.** The Revision record `Revision/algebra/gammas.json` holds the author's eight real $16 \times 16$ gamma matrices $\gamma^{(x1)}, \dots, \gamma^{(x8)}$, rebuilt in Revision code from the author's formulas. Every entry is $-1$, $0$ or $+1$, and each row and column holds one nonzero entry (a **signed permutation matrix**). They obey the **Clifford relation**

$$
\gamma^a\gamma^b + \gamma^b\gamma^a = 2\eta^{ab}\,1,\qquad \eta = \mathrm{diag}(+1, +1, +1, -1, -1, -1, -1, +1),
$$

and the **symmetry pattern** $(\gamma^a)^T = \eta_{aa}\gamma^a$: the four space-like gammas ($x_1, x_2, x_3, x_8$) are symmetric, the four time-like ones antisymmetric. Two consequences used again and again: different gammas **anticommute**, $\gamma^a\gamma^b = -\gamma^b\gamma^a$ for $a \ne b$, and $\gamma^a\gamma^a = \eta^{aa}1$. Notebook 21a checks all of this exactly (In [3]).

**The four matrices built from them** (Chapters 4 and 5):

- the **charge matrix** $C = \gamma^{(x8)}\gamma^{(x1)}\gamma^{(x2)}\gamma^{(x3)}$, the product of the four space-like gammas (the author's sigma16);
- the **chirality** $\Gamma = \gamma^{(x8)}\gamma^{(x1)}\gamma^{(x2)}\cdots\gamma^{(x7)}$, the product of all eight, which equals $\mathrm{diag}(-1, \dots, -1, +1, \dots, +1)$ (eight of each);
- the **Krein matrix** $B = -iC\gamma^{(x4)}$;
- the 28 **generators** $S^{ab} = \tfrac14(\gamma^a\gamma^b - \gamma^b\gamma^a)$ of the rotations and boosts, which for $a \ne b$ equal $\tfrac12\gamma^a\gamma^b$.

**Three rules for moving gammas**, each derived from the Clifford relation:

- (R1) $\Gamma$ anticommutes with every gamma. Moving $\gamma^b$ from the left of $\Gamma$ to its right passes the seven factors $\gamma^a$ with $a \ne b$, each of which costs a sign, and the factor $\gamma^b$ itself, which costs none: the total sign is $(-1)^7 = -1$.
- (R2) $\Gamma$ commutes with every product of an even number of gammas, in particular with $C$ and with every $S^{ab}$ (each factor costs a sign by (R1), and an even number of signs multiply to $+1$). Also $\Gamma\Gamma = 1$ and $\Gamma^T = \Gamma$, because $\Gamma$ is diagonal with entries $\pm1$.
- (R3) $C^T = C$, $CC = 1$ and $C\gamma^aC = -(\gamma^a)^T$ for every $a$. Derivation: $C^T = (\gamma^{(x3)})^T(\gamma^{(x2)})^T(\gamma^{(x1)})^T(\gamma^{(x8)})^T = \gamma^{(x3)}\gamma^{(x2)}\gamma^{(x1)}\gamma^{(x8)}$ (the transpose of a product is the product of the transposes in reverse order; space-like gammas are symmetric); reversing the order of four different anticommuting factors takes $3 + 2 + 1 = 6$ exchanges, so $C^T = (-1)^6C = C$. Then $CC = CC^T = \gamma^{(x8)}\gamma^{(x1)}\gamma^{(x2)}\gamma^{(x3)}\gamma^{(x3)}\gamma^{(x2)}\gamma^{(x1)}\gamma^{(x8)} = 1$ (each neighbouring pair $\gamma\gamma$ of a space-like gamma is $+1$, from the inside out). Next, $\gamma^aC = -C\gamma^a$ when $a$ is space-like (passing through $C$ costs three signs for the other three factors and none for $\gamma^a$ itself) and $\gamma^aC = +C\gamma^a$ when $a$ is time-like (four signs). With the symmetry pattern, $(C\gamma^a)^T = (\gamma^a)^TC^T = \eta_{aa}\gamma^aC = -C\gamma^a$ in both cases: every $C\gamma^a$ is **antisymmetric**. Writing this as $(\gamma^a)^TC = -C\gamma^a$ and multiplying from the right by $C$ (with $CC = 1$) gives $(\gamma^a)^T = -C\gamma^aC$.

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
\Psi = \sin^\alpha z\,\Big(\cosh(kx_4)\,1 + \frac{\sinh(kx_4)}{k}M_m\Big)\chi,\qquad M_m = -m\gamma^{(x4)} + b\,\gamma^{(x4)}\gamma^{(x8)},\quad b = 3H(2\alpha + 1),\quad k^2 = b^2 - m^2 ,
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

Notebook 21a turns Sections 21.7 to 21.11 into exact computations on the author's gammas. It reads the gammas from `Revision/algebra/gammas.json` and the lead report `Revision/lead_checks/reports/charge-conjugation-and-u1.json`; it checks the eight real gammas and draws them; it builds $C$, $\Gamma$, $B$ and the $S^{ab}$; it writes the conditions $M(\gamma^a)^\ast = s\gamma^aM$ as two systems of 2048 linear equations for the 256 entries of $M$ and solves them exactly over the rational numbers; it watches each equation halve the solution space; it builds $\mathcal{C}_+$ and $\mathcal{C}_-$, checks their transposition rules and solves the transposition equations; it checks the two reality conditions; it reads the field equation and the exact solution from the field-theory record word for word and applies both conjugations to the solution; it computes the signs of all 256 bilinears; and it treats real fields. Nine of its checks reproduce checks of the lead report, two reproduce the field-theory record. It runs in about 30 seconds (the last verified run took 9 to 14 seconds), needs no Rust, prints 27 PASS lines and draws seven figures.

<!-- NOTEBOOK 21a -->

### 21.15 Line-by-line walk-through of Notebook 21a

Draft.
