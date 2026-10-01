## 17. Matter and antimatter

### 17.1 What this chapter answers

The request that this book answers ends with the words "this theory solves matter anti-matter mysteries" (Section 0.2). This chapter explains what those mysteries are, starting from zero, and then states exactly what the dirac16complex theory contributes to them. The honest answer comes first, because everything else in the chapter supports it.

**The honest answer.** The theory as built does not solve the matter–antimatter problem, and within the theory the central step of such a solution is impossible. The Lagrangian of both fields of this book, dirac16complex (anticommuting components) and dirac16complex00 (commuting components), does not change when the field is multiplied by a constant phase $e^{i\alpha}$. By Noether's theorem the associated charge $Q$ is conserved in every gravitational field, as long as no charge flows in or out through the boundary of space (Theorem M1, Section 17.9), so no process of the theory can create a net charge inside one universe. The theory also has exact symmetries that turn every solution with charge $Q$ into a solution with charge $-Q$ without reversing the time $x_4$: for dirac16complex00 the charge conjugation C, in every gravitational field; for dirac16complex a combination CP of charge conjugation with a spatial reflection, in flat space and in every gravitational field in which the reflection is an isometry (leaves the metric unchanged), for example the primordial field of Chapter 9 with a reflection of $x_1$, $x_2$ or $x_3$ (Theorem M2, Sections 17.10 and 17.11). A generic gravitational field breaks this CP, but that opens no way to an asymmetry, because the charge stays conserved. Nothing in the repository computes a departure from thermal equilibrium. The first two facts negate the first two of the three conditions that Sakharov found in 1967 to be necessary for creating a matter–antimatter asymmetry (Section 17.5); the third condition is not addressed by any computation, and since the first fails exactly, a departure from equilibrium could not help. What the theory does provide is exact but limited: as classical fields, a universe of mass $+M$ and its chirality image of mass $-M$ carry opposite charges and zero total charge (Theorem M4, Section 17.13). At the quantum level the image is the same quantum system with the Krein metric $-B$, and no cancellation between two independently quantised universes follows (Section 17.13). Under three hypotheses that nothing in the repository derives, this gives a picture in which the whole pair is symmetric while each member is asymmetric (Section 17.14). The picture predicts no number; in particular it does not predict the observed baryon-to-photon ratio $\eta\approx6\times10^{-10}$.

**The plan.** Sections 17.2 to 17.7 explain the problem from zero: antiparticles and conserved numbers, the size of the observed asymmetry, why the universe is not a patchwork of matter and antimatter regions, Sakharov's three conditions with a derivation in plain words, why the Standard Model of particle physics does not suffice, and the class of "universe and anti-universe" ideas. Sections 17.8 to 17.16 carry out the exact analysis of the theory: the theorems M1 to M4, the conditional scenario M5 and the scorecard M6, followed by the list of what would have to be added to the theory. Section 17.17 lists the machine checks and the commands that rerun them.

**Sources.** The exact analysis of this chapter is that of the matter-antimatter document, whose title is "Matter and antimatter in the dirac16complex theory: what can be proved", written under its own specification; this chapter follows it and explains each step for a beginner. Its machine checks are in two independent reports, one written by a Wolfram Language verifier (44 of 44 checks true) and one by an independent Python checker (75 of 75 checks true); the Wolfram verifier also writes a file of exact results. The committed files are not all of the same age, and the chapter says where this matters. On two points it follows the wording of the committed Wolfram report and exact-results file, which were rewritten after the committed text of the document: the scope of CP in a gravitational field (Section 17.11) and the reading of the pair of universes at the quantum level (Sections 17.13 and 17.14). The committed Python report was written by an earlier version of the Python checker; the checker in the same commit has 77 checks, two more than that report, and a rerun of it gives 77 of 77 true (Section 17.17). The quantum statements about the pair of universes use the exact pairing results of Stage 5 (141 of 141 checks true). The files are

```
provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md        the matter-antimatter document
handoff/specs/MATTER_ANTIMATTER_SPEC.md               its specification
artifacts/dirac16complex/matter-antimatter/
    wolfram-matter-antimatter-report.json             Wolfram report (44 checks)
    python-matter-antimatter-report.json              Python report (75 checks, earlier
                                                      version of the checker)
    matter-antimatter-theory.json                     exact results (Wolfram)
wolfram/Dirac16ComplexMatterAntimatter.wl             the Wolfram package
scripts/verify_dirac16complex_matter_antimatter.wls   the Wolfram verifier
scripts/check_dirac16complex_matter_antimatter.py     the Python checker
artifacts/dirac16complex/pair-creation/
    pairing-theory.json                               Stage-5 exact pairing results
    wolfram-pairing-report.json                       Stage-5 report (141 checks)
```

Check names in typewriter type that begin with `MA_` belong to the two matter-antimatter reports (two of them, marked where they appear, only to the Python checker of this commit and not yet to its committed report), and those that begin with `PAIR_` to the Stage-5 pairing report. The literature cited in Sections 17.2 to 17.7 is listed in Section 17.18.

**Labels.** As everywhere in this book (Section 0.3): PROVED means a complete derivation is given here, and where the repository has an exact machine check it is named; COMPUTED means floating-point data read from a committed file; ASSUMED marks a convention, an input or an approximation; HYPOTHESIS marks a claim that nothing in the repository derives; OPEN marks a question that the project has not answered. The conventions are those of the whole book: counting from 0, coordinates $x_0,\dots,x_7$ with $x_4$ the time, $\eta=\mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1)$, the notebook's gamma matrices $\gamma^0,\dots,\gamma^7$ (Chapter 2), $C=\gamma^0\gamma^1\gamma^2\gamma^3$, the chirality $\gamma^8=\gamma^0\gamma^1\cdots\gamma^7=\mathrm{diag}(-I_8,I_8)$, $\bar\Psi=\Psi^\dagger C$ and $B=-iC\gamma^4$.

### 17.2 Particles, antiparticles and conserved numbers

**Antiparticles.** In 1928 Dirac wrote down his equation for the electron (Chapter 2). Its solutions come with negative as well as positive energies, and Dirac concluded that a particle with the mass of the electron and the opposite electric charge must exist. Such a particle, the positron, was found in cosmic rays in 1932 (C. D. Anderson, Phys. Rev. 43, 491 (1933)). Every known particle has an **antiparticle** with the same mass and the opposite values of all its charges: the electron has the positron, the proton the antiproton, the neutron the antineutron (both neutral, but with opposite baryon number, defined below). A few neutral particles, such as the photon, are their own antiparticles.

**Annihilation and pair creation.** A particle and its antiparticle can **annihilate**: an electron and a positron that meet turn into two (or more) photons. Conversely, energy can turn into a particle–antiparticle pair: a photon of enough energy that passes near an atomic nucleus, which takes up momentum, can turn into an electron and a positron. (A single free photon cannot do this: energy and momentum cannot both be conserved.) In both processes the total electric charge is unchanged, because the two members of a pair carry opposite charges. Chapter 11 met a gravitational version of pair creation: in an expanding universe the change of the mode Hamiltonian with time lifts quanta out of the Dirac sea and leaves antiparticles behind (Section 11.11).

**Three conserved numbers.** Three kinds of charge matter here.

- The **electric charge**, measured in units of the proton charge. It is exactly conserved in every process ever observed.
- The **baryon number** $B$. Protons, neutrons and their heavier relatives are **baryons** and have $B=+1$; their antiparticles have $B=-1$; each quark carries $B=\tfrac13$ and each antiquark $-\tfrac13$. Particles made of a quark and an antiquark, such as the pions $\pi^+,\pi^-,\pi^0$, have $B=0$, and so do electrons, neutrinos and photons.
- The **lepton number** $L$. Electrons, muons, tau leptons and neutrinos have $L=+1$ and their antiparticles $L=-1$.

"Matter" in cosmology means baryons: the atoms of stars, planets and gas owe almost all their mass to protons and neutrons. The **matter–antimatter problem** is the question why the universe contains baryons but essentially no antibaryons.

**Worked example: bookkeeping.** A number is conserved in a process if its total before equals its total after. Count the three numbers in three observed processes (a bar denotes an antiparticle, $\bar\nu_e$ is the electron antineutrino, $\gamma$ a photon):

| Process | electric charge | baryon number $B$ | lepton number $L$ |
| --- | --- | --- | --- |
| $n\to p+e^-+\bar\nu_e$ | $0\to+1-1+0=0$ | $1\to1+0+0=1$ | $0\to0+1-1=0$ |
| $e^++e^-\to\gamma+\gamma$ | $+1-1=0\to0$ | $0\to0$ | $-1+1=0\to0$ |
| $p+\bar p\to\pi^++\pi^-+\pi^0$ | $+1-1=0\to+1-1+0=0$ | $1-1=0\to0$ | $0\to0$ |

All three numbers are conserved in all three processes. The first line, the decay of a free neutron, turns a neutron into a proton; $B$ is unchanged because both are baryons.

**Conservation and symmetry.** A number is **conserved** when no process can change it. Noether's theorem (Section 5.7) connects conservation with symmetry: if the action of a field theory does not change under a continuous transformation that is the same at every point, then there is a current $j^\mu$ whose divergence vanishes on every solution, and the integral of its time component over space, the **charge**, does not change with time. The phase symmetry $\psi\to e^{i\alpha}\psi$ of Example 1 of Section 5.7 is the simplest case. Theorem M1 of Section 17.9 is the same theorem for the field of this book, and it is the reason why the theory, as built, cannot produce an asymmetry of its own charge.

### 17.3 What is observed: the baryon-to-photon ratio

**The definition.** The universe is filled with the photons of the **cosmic microwave background**, the thermal radiation left over from the hot early universe, now at the temperature $T_0=2.7255$ K (D. J. Fixsen, Astrophys. J. 707, 916 (2009)). Because both the baryons and these photons are diluted in the same way by the expansion (after the first seconds of the universe their numbers per comoving volume stay constant), their ratio is a fixed number that characterizes our universe, the **baryon-to-photon ratio**

$$
\eta=\frac{n_B-n_{\bar B}}{n_\gamma},
$$

where $n_B$, $n_{\bar B}$ and $n_\gamma$ are the numbers of baryons, antibaryons and photons per unit volume. Today $n_{\bar B}$ is negligible, so $\eta$ is simply the number of baryons per photon.

**Two independent measurements.** The value of $\eta$ is measured in two independent ways. First, the nuclei of the light elements (deuterium, helium-3, helium-4, lithium-7) were made in the first minutes of the universe (**big-bang nucleosynthesis**), and how much of each was made depends on $\eta$; the observed abundances fix $\eta$ (R. H. Cyburt, B. D. Fields, K. A. Olive and T.-H. Yeh, Rev. Mod. Phys. 88, 015004 (2016)). Second, the pattern of hot and cold spots in the microwave background (its "acoustic peaks") depends on the density of baryons at the time the radiation was released. The Planck satellite measured it; the Planck 2018 cosmological parameters give

$$
\Omega_bh^2=0.0224\pm0.0001
$$

(Planck Collaboration, Astron. Astrophys. 641, A6 (2020)). The two determinations agree.

**What $\Omega_bh^2$ means.** $H_0$ is today's Hubble rate (Section 11.2), written $H_0=100\,h$ km/s/Mpc with a pure number $h$ (1 Mpc, a megaparsec, is $3.0857\times10^{22}$ m). The **critical density** $\rho_{\mathrm{crit}}=3H_0^2/(8\pi G)$, with Newton's constant $G$, is the total density of a spatially flat universe with the Hubble rate $H_0$ (it is the first Friedmann equation of Section 11.2, $H^2=\tfrac{8\pi G}3\rho$, solved for $\rho$). $\Omega_b$ is the mass density of baryons divided by $\rho_{\mathrm{crit}}$. The combination $\Omega_bh^2$ is what the microwave background measures directly: it is proportional to the baryon mass density itself, because $\rho_{\mathrm{crit}}\propto H_0^2\propto h^2$.

**From $\Omega_bh^2$ to $\eta$, step by step.** We use the standard values of the constants (E. Tiesinga, P. J. Mohr, D. B. Newell and B. N. Taylor, Rev. Mod. Phys. 93, 025010 (2021)): $G=6.6743\times10^{-11}\ \mathrm{m^3\,kg^{-1}\,s^{-2}}$, Boltzmann's constant $k_B=1.380649\times10^{-23}$ J/K, Planck's constant divided by $2\pi$, $\hbar=1.054572\times10^{-34}$ J s, the speed of light $c=2.99792458\times10^8$ m/s and the proton mass $m_p=1.672622\times10^{-27}$ kg.

1. *The unit of the Hubble rate.* $100$ km/s/Mpc $=10^5\ \mathrm{m\,s^{-1}}/(3.0857\times10^{22}\ \mathrm m)=3.2408\times10^{-18}\ \mathrm{s^{-1}}$.
2. *The critical density.* $\rho_{\mathrm{crit}}=h^2\cdot3\,(3.2408\times10^{-18})^2/(8\pi\cdot6.6743\times10^{-11})=1.8783\times10^{-26}\,h^2$ kg/m$^3$. Hence the baryon mass density is $\rho_b=\Omega_b\rho_{\mathrm{crit}}=1.8783\times10^{-26}\,(\Omega_bh^2)$ kg/m$^3$.
3. *The number of baryons.* Almost all baryons are protons and neutrons, whose masses differ by 0.14 percent, so the number density is $n_B\approx\rho_b/m_p=11.230\,(\Omega_bh^2)$ per m$^3$. (A correction we do not apply: the fraction $Y_p\approx0.245$ of the baryonic mass is bound in helium-4 nuclei (the observed helium mass fraction; Cyburt et al., cited above). Masses of particles are usually quoted as rest energies $mc^2$ in MeV (mega-electronvolts, $1\ \mathrm{MeV}=1.602177\times10^{-13}$ J). A helium-4 nucleus has $3727.38$ MeV (Tiesinga et al., cited above), that is $931.84$ MeV per nucleon, less than the proton's $938.27$ MeV. Counting the helium nucleons with their own mass multiplies $n_B$ by $(1-Y_p)+Y_p\cdot938.27/931.84=0.755+0.245\times1.00690=1.0017$. This raises the result by about 0.2 percent, and the coefficient of step 5 from $2.7342\times10^{-8}$ to about $2.739\times10^{-8}$. The change is below the 0.45 percent precision of $\Omega_bh^2=0.0224\pm0.0001$ used here, so we keep the simpler value.)
4. *The number of photons.* The microwave background has the spectrum of a black body. For a black body of temperature $T$ the number of photons per unit volume is $n_\gamma=\frac{2\zeta(3)}{\pi^2}\bigl(\frac{k_BT}{\hbar c}\bigr)^3$, where $\zeta(3)=\sum_{n\ge1}n^{-3}=1.2020569$; this standard formula of statistical physics is quoted, not derived, in this book. With $k_BT_0/(\hbar c)=1190.23$ per m and $2\zeta(3)/\pi^2=0.243588$: $n_\gamma=0.243588\times(1190.23)^3=4.1073\times10^8$ per m$^3$, that is about 411 photons per cubic centimetre.
5. *The ratio.* $\eta=11.230\,(\Omega_bh^2)/(4.1073\times10^8)=2.7342\times10^{-8}\,\Omega_bh^2$. For $\Omega_bh^2=0.0224\pm0.0001$ this gives

$$
\eta=6.12\times10^{-10},\qquad\text{between }6.10\times10^{-10}\text{ and }6.15\times10^{-10}.
$$

In words: there are about six baryons for every ten billion photons, or $1/\eta\approx1.6\times10^9$ photons per baryon.

**Why this is a problem.** Run the expansion backwards. At temperatures at which the thermal energy far exceeds the rest energy of a proton, baryons, antibaryons and photons were all abundant and turned into each other all the time. If the early universe had contained exactly as many baryons as antibaryons, then, as it cooled, almost all of them would have annihilated with each other, and far less matter than we observe would be left (L. Canetti, M. Drewes and M. Shaposhnikov, New J. Phys. 14, 095012 (2012)). The present baryons are therefore the remnant of a small excess of baryons over antibaryons in the early universe. One could simply put this excess into the initial conditions of the universe. The standard view, reviewed in the article just cited, is that it should instead be **generated by physical processes** from a state without asymmetry; explaining how is the matter–antimatter problem, also called **baryogenesis**.

### 17.4 No antimatter domains

Could the universe be symmetric on the whole, with some regions made of matter and others of antimatter? Galaxies made of antimatter would shine exactly like galaxies of matter, so their light alone would not reveal them. But wherever a region of matter touches a region of antimatter, particles and antiparticles annihilate. Cohen, De Rújula and Glashow showed that after the universe became transparent, annihilation at the boundaries of such regions cannot be avoided, and that the gamma rays it produces would exceed the observed diffuse gamma-ray background unless the region of matter in which we live is essentially the whole visible universe (A. G. Cohen, A. De Rújula and S. L. Glashow, Astrophys. J. 495, 539 (1998)). A universe made of domains of matter and antimatter, symmetric on the whole, is therefore excluded by observation.

A second observation matters below. Antimatter responds to gravity like matter, as far as tested: antihydrogen atoms released in the ALPHA-g experiment at CERN move downward in the gravity of the Earth, and repulsive "antigravity" is ruled out for them (ALPHA Collaboration, Nature 621, 716 (2023)). The member of mass $-M$ of the pair of universes of Section 17.13 is therefore **not** antimatter in our universe: its negative mass is a parameter of a second field configuration, and nothing in this book says that antimatter has negative mass or falls upward.

### 17.5 Sakharov's three conditions, derived in plain words

In 1967 Andrei Sakharov identified three ingredients that any process which creates the baryon asymmetry from a state without asymmetry must contain (A. D. Sakharov, JETP Lett. 5, 24 (1967)). Each condition follows from a short argument, which we give now. Throughout, "the system" is the whole universe, it starts in a state with baryon number $B=0$ and without any asymmetry, and we ask what is needed for $B\ne0$ to appear later.

**Condition 1: baryon-number violation.**

*Proposition 17.1.* If every process conserves $B$, then $B(t)=B(0)$ at every time.

*Proof.* Conservation means $dB/dt=0$, so $B$ is constant. $\square$

Starting from $B=0$, the universe would have $B=0$ forever. So some process must change $B$. In the dirac16complex theory the role of $B$ could only be played by the charge $Q$, and Theorem M1 shows that $Q$ is conserved: this condition fails.

**Condition 2: C and CP violation.** **Charge conjugation** C exchanges every particle with its antiparticle. **Parity** P reflects space, $\mathbf x\to-\mathbf x$. **CP** does both. A transformation is a **symmetry of the dynamics** if it turns every possible history of the system into another possible history, running in the same direction of time. The next proposition says that a symmetry that reverses $B$ forbids the creation of an average asymmetry.

*Proposition 17.2.* Let $\mathcal S$ be a symmetry of the dynamics that reverses $B$: if a history $h$ has the baryon number $B[h](t)$ at time $t$, then its image $\mathcal Sh$ has $B[\mathcal Sh](t)=-B[h](t)$. Suppose the initial state is an ensemble (a list of possible initial configurations $c$ with probabilities $p(c)$) in which every configuration and its image are equally likely, $p(\mathcal Sc)=p(c)$. Then the average baryon number $\langle B(t)\rangle$ is zero at every time.

*Proof.* Let $h_c$ be the history that starts from $c$. Because $\mathcal S$ is a symmetry, the history that starts from $\mathcal Sc$ is $\mathcal Sh_c$. The map $c\to\mathcal Sc$ is one-to-one, so a sum over all $c$ may be rewritten as a sum over all $\mathcal Sc$:

$$
\langle B(t)\rangle=\sum_cp(c)\,B[h_c](t)=\sum_cp(\mathcal Sc)\,B[\mathcal Sh_c](t)=\sum_cp(c)\bigl(-B[h_c](t)\bigr)=-\langle B(t)\rangle ,
$$

so $\langle B(t)\rangle=0$. $\square$

Apply this with $\mathcal S=\mathrm C$: an initial state without asymmetry contains particles and antiparticles in equal numbers, so it is C-symmetric, and if C were a symmetry of the dynamics no average asymmetry could ever develop. Apply it with $\mathcal S=\mathrm{CP}$: a homogeneous and isotropic initial state is also symmetric under the reflection P, and P does not change $B$, so CP reverses $B$ as well; if CP were a symmetry, again no asymmetry could develop. Hence **both C and CP must be violated**. In the dirac16complex theory one of them is exact for each field (Theorem M2): C for dirac16complex00, in every gravitational field, and CP for dirac16complex, in flat space and in every gravitational field in which the reflection is an isometry (a map of the points that leaves the metric unchanged, Section 17.10). The latter include the fields that are homogeneous and isotropic in the space-like directions, the natural setting of the CP step above. So this condition fails too. A generic gravitational field breaks the CP of dirac16complex (Section 17.11), but that cannot produce an asymmetry, because the first condition fails exactly in every gravitational field.

*Worked example (a toy model).* Consider a heavy particle $X$ with two ways to decay: into two quarks ($B=\tfrac23$) with probability $r$, or into an antiquark and an antilepton ($B=-\tfrac13$) with probability $1-r$. Its antiparticle $\bar X$ decays into two antiquarks ($B=-\tfrac23$) with probability $\bar r$, or into a quark and a lepton ($B=\tfrac13$) with probability $1-\bar r$. The decays themselves violate $B$. The average baryon number produced by one $X$ is $\tfrac23r-\tfrac13(1-r)=r-\tfrac13$, by one $\bar X$ it is $-\tfrac23\bar r+\tfrac13(1-\bar r)=\tfrac13-\bar r$, and a population of $N$ particles $X$ and $N$ antiparticles $\bar X$ produces

$$
\Delta B=N\bigl(r-\bar r\bigr).
$$

For $N=1000$, $r=0.51$ and $\bar r=0.49$ this is $\Delta B=20$. If C were a symmetry, the decay $X\to qq$ and its C-image $\bar X\to\bar q\bar q$ would have the same rate, and since $X$ and $\bar X$ have the same total decay rate (by the CPT theorem mentioned below), $r=\bar r$ and $\Delta B=0$; if CP were a symmetry, the same would hold after summing over the directions of the decay products. Only if both are violated can $r\ne\bar r$.

**Condition 3: departure from thermal equilibrium.** In thermal equilibrium at temperature $T$ each quantum state of energy $E$ is occupied with the Fermi–Dirac probability $f(E)=1/(e^{(E-\mu)/T}+1)$ (Section 12.14; Boltzmann's constant is set to 1), where the chemical potential $\mu$ belongs to a conserved number. For a particle of baryon number $+1$ in a state of energy $E$ the occupation is $f_+=1/(e^{(E-\mu_B)/T}+1)$, and for its antiparticle in the state of the same energy it is $f_-=1/(e^{(E+\mu_B)/T}+1)$: the antiparticle carries the opposite baryon number, so it sees $-\mu_B$. The two energies are equal because particles and antiparticles have the same mass, a consequence of the CPT theorem of ordinary relativistic quantum field theory (quoted, not proved in this book). If reactions that change $B$ run back and forth in equilibrium, $B$ is not a conserved number, and the equilibrium state has no chemical potential for it: the Gibbs state of Section 12.14 is built from the Hamiltonian and the conserved numbers only. Then $\mu_B=0$, $f_+=f_-$ for every energy, and the average baryon number vanishes. An asymmetry can therefore only be produced while the universe is **out of equilibrium**, for example during a phase transition or in the decay of heavy particles that happens too late for the inverse processes to keep up.

*Worked example.* Take a state with $E=2T$. At $\mu_B=0$, $f_+=f_-=1/(e^2+1)=0.119203$. A chemical potential $\mu_B=0.1\,T$ would give $f_+=1/(e^{1.9}+1)=0.130108$ and $f_-=1/(e^{2.1}+1)=0.109097$, a surplus of $0.021012$ particles per state; but in equilibrium with $B$-violating reactions $\mu_B$ must vanish, and the surplus with it.

These three conditions are the yardstick of the scorecard of Section 17.15.

### 17.6 Why the Standard Model is not enough

The Standard Model of particle physics contains all three ingredients in principle. Baryon number is violated at high temperature by the electroweak **sphaleron** processes (V. A. Kuzmin, V. A. Rubakov and M. E. Shaposhnikov, Phys. Lett. B 155, 36 (1985)). C is violated maximally by the weak interaction, and CP is violated by the complex phase of the quark mixing matrix. A departure from equilibrium could occur at the electroweak transition in the early universe. The consensus of the literature, reviewed by Canetti, Drewes and Shaposhnikov (New J. Phys. 14, 095012 (2012)), is nevertheless that the Standard Model cannot produce the observed asymmetry, for two reasons.

1. Lattice computations showed that for Higgs masses of the order of the W-boson mass and above, the electroweak transition is not a first-order phase transition and provides no strong departure from equilibrium (K. Kajantie, M. Laine, K. Rummukainen and M. E. Shaposhnikov, Phys. Rev. Lett. 77, 2887 (1996)). The Higgs boson discovered at the Large Hadron Collider (ATLAS Collaboration, Phys. Lett. B 716, 1 (2012); CMS Collaboration, Phys. Lett. B 716, 30 (2012)) is heavier than the end point found there.
2. The CP violation of the quark mixing matrix produces an asymmetry far too small (M. B. Gavela, P. Hernández, J. Orloff and O. Pène, Mod. Phys. Lett. A 9, 795 (1994); P. Huet and E. Sather, Phys. Rev. D 51, 379 (1995)).

Physics beyond the Standard Model is therefore needed. This section reports the literature; nothing in it is computed in this book.

### 17.7 Pairs of universes: global symmetry, local asymmetry

One class of ideas replaces the question "why is there more matter than antimatter?" by a global symmetry: the universe as a whole is symmetric, but it consists of two parts, each of which is asymmetric in the opposite way. The known published example is the **CPT-symmetric universe** of Boyle, Finn and Turok (L. Boyle, K. Finn and N. Turok, Phys. Rev. Lett. 121, 251301 (2018)). They propose that the universe after the big bang is the CPT image of the universe before it, so that the epochs before and after the bang form a universe–antiuniverse pair, and they argue that CPT symmetry selects a vacuum state and gives a new interpretation of the cosmological baryon asymmetry. This book neither depends on nor tests that proposal; it is cited as the known example of the class.

The pair of universes of this theory (Section 17.13) is of a different kind. Both members exist at the same time $x_4$, and they are related by the chirality map $\Psi\to\gamma^8\Psi$ together with the change of the mass $m\to-m$, not by a reflection of time through a bang. The resemblance is only structural: a symmetric whole made of two asymmetric parts. Such a picture, even when it is consistent, does not explain the size of the asymmetry in either part, and each part must separately agree with every observation of Sections 17.3 and 17.4.

### 17.8 The theory in this chapter: two fields, one current

**The two fields.** Both fields of this book are columns $\Psi=(\Psi_0,\dots,\Psi_{15})^T$ of 16 complex components at every point, which carry the irreducible Clifford module of Pin(4,4) (Chapter 2). For **dirac16complex** the components are anticommuting Grassmann numbers (Section 5.9): $\Psi_a\Psi_b=-\Psi_b\Psi_a$, $\Psi_a\Psi_b^\ast=-\Psi_b^\ast\Psi_a$, and complex conjugation reverses the order of a product, $(\theta_1\theta_2)^\ast=\theta_2^\ast\theta_1^\ast$. For **dirac16complex00** the components are ordinary commuting complex numbers (Chapter 6). We write

$$
s=-1\ \text{for anticommuting components},\qquad s=+1\ \text{for commuting components},
$$

and call $s$ the **statistics sign**. The two theories have the same Lagrangian and differ only in $s$.

**The Lagrangian** (Chapter 6), for both fields:

$$
\mathcal L=\sqrt{|g|}\,\bigl[K-mS-U(S)\bigr],\qquad S=\bar\Psi\Psi,\qquad K=\tfrac12\bigl(\bar\Psi\gamma^\mu D_\mu\Psi-(D_\mu\bar\Psi)\gamma^\mu\Psi\bigr),
$$

with the curved gammas $\gamma^\mu=e_a{}^\mu\gamma^a$, the spinor covariant derivatives $D_\mu\Psi=\partial_\mu\Psi+\Omega_\mu\Psi$ and $D_\mu\bar\Psi=\partial_\mu\bar\Psi-\bar\Psi\Omega_\mu$, and the canonical spinor connection $\Omega_\mu=\tfrac12\omega_{\mu ab}S^{ab}$ (Chapter 4). For anticommuting components $U$ must be a polynomial in $S$ of degree at most 16, because $S^{17}=0$ (Section 5.9); for commuting components $U$ may be any function. We write $\mathcal L_{m,\lambda}$ for the Lagrangian with mass $m$ and $U=\tfrac\lambda2S^2$.

**The field equations** (Chapter 7) are $E=0$ and $\bar E=0$ with

$$
E:=\gamma^\mu D_\mu\Psi-\bigl(m+U'(S)\bigr)\Psi,\qquad \bar E:=(D_\mu\bar\Psi)\gamma^\mu+\bigl(m+U'(S)\bigr)\bar\Psi .
$$

**The current and the charge.** The current of the phase symmetry is

$$
j^\mu=\bar\Psi\gamma^\mu\Psi=\Psi^\dagger C\gamma^\mu\Psi .
$$

Each matrix $C\gamma^a$ is real and antisymmetric (expression [1], Section 2.9), hence anti-Hermitian, so $j^\mu$ is anti-Hermitian; for commuting components it is a purely imaginary number (fact 4 of Section 1.5). The Hermitian current of this book is $J^\mu=-ij^\mu=-i\bar\Psi\gamma^\mu\Psi$ (Section 8.12). The matter-antimatter document states its theorems for $j^\mu$; the factor $-i$ changes nothing in them. The **charge** of the slice $\Sigma_{x_4}=\{x_4=\text{const}\}$ is

$$
Q(x_4)=\int_{\Sigma_{x_4}}\sqrt{|g|}\,J^{x_4}\,d^7x ,
$$

where $J^{x_4}$ is the component of $J^\mu$ along the coordinate $x_4$ and $d^7x=dx_0\,dx_1\,dx_2\,dx_3\,dx_5\,dx_6\,dx_7$. In Gaussian normal gauge ($g^{44}=-1$ and $\gamma^{x_4}=\gamma^4$, Section 8.6) the charge density is

$$
J^4=-i\Psi^\dagger C\gamma^4\Psi=\Psi^\dagger B\Psi,\qquad B=-iC\gamma^4 .
$$

$B$ is Hermitian with $B^2=1$ and has eight eigenvalues $+1$ and eight eigenvalues $-1$ (Section 2.12), so for a classical field $Q$ is an **indefinite** quadratic form: it can be positive, negative or zero. After quantization $B$ is the Krein metric of the canonical anticommutator $\{\Psi_a,\Psi_b^\dagger\}=B_{ab}\,\delta^7/\sqrt{|g|}$ (Section 8.6), and in the good sector the normal-ordered charge is $Q=\sum\bigl(b^\ast b-d^\ast d\bigr)$: particles carry $Q=+1$ and antiparticles $Q=-1$ (Section 8.12).

**Test geometries.** The machine checks of this chapter use three exactly given gravitational fields: G1, the generic non-diagonal polynomial vielbein of Stage 1, at three rational points (Wolfram checks); and, built independently from exact vielbein jets (values and derivatives) at one point, G_A, a non-diagonal vielbein with space–space, space–time and time–time mixing, and G_B, a diagonal vielbein that depends on $x_0$ and $x_4$ only and has reflection symmetries (Python checks). As always, a check at test points confirms a general proof; the proofs below are the general ones (Section 0.3).

### 17.9 Theorem M1: exact U(1) symmetry and charge conservation

**Theorem M1.** For both statistics, every admissible potential $U$ and every vielbein:

1. (global phase) $\mathcal L[e^{i\alpha}\Psi]=\mathcal L[\Psi]$ for every constant real $\alpha$;
2. (local phase and Noether current) for a phase $\alpha(x)$ that depends on the point, $\mathcal L[e^{i\alpha}\Psi]=\mathcal L[\Psi]+i\sqrt{|g|}\,(\partial_\mu\alpha)\,j^\mu$, so the Noether current of the phase symmetry is $N^\mu=i\sqrt{|g|}\,j^\mu$;
3. (off-shell identity) for every configuration, solution or not, $\partial_\mu\bigl(\sqrt{|g|}\,j^\mu\bigr)=\sqrt{|g|}\,\bigl(\bar E\,\Psi+\bar\Psi\,E\bigr)$;
4. (conservation) on every solution $\nabla_\mu j^\mu=0$, and $Q(x_4)$ does not depend on $x_4$ whenever the flux of $\sqrt{|g|}\,J^\mu$ through the boundary of the slices vanishes (fields of compact support, sufficient fall-off at infinity, or slice coordinates identified periodically);
5. (charge density) in Gaussian normal gauge $J^4=\Psi^\dagger B\Psi$, with $B$ Hermitian, $B^2=1$, eight eigenvalues $+1$, eight eigenvalues $-1$ and trace 0.

**Consequence.** No solution of the field equations of either field, for any $U$ and in any gravitational field with $g^{44}\ne0$, changes $Q$, as long as the boundary flux of item 4 vanishes. The charge of a universe is then fixed by its initial data at $x_4=0$.

**Proof of item 1.** For commuting components the substitution multiplies $\Psi$ by $e^{i\alpha}$, $\Psi^\dagger$ by $e^{-i\alpha}$ and hence $\bar\Psi=\Psi^\dagger C$ by $e^{-i\alpha}$ ($C$ is real). Every term of $\mathcal L$ is either a bilinear $\Psi^\dagger X\Psi$ with a matrix $X$ built from the geometry (the kinetic term and $S$), which the phase does not touch, or a function of $S$; each bilinear is multiplied by $e^{-i\alpha}e^{i\alpha}=1$. For anticommuting components complex conjugation is antilinear, $(c\theta)^\ast=c^\ast\theta^\ast$, so replacing every generator $\Psi_a$ by $e^{i\alpha}\Psi_a$ and every $\Psi_a^\ast$ by $e^{-i\alpha}\Psi_a^\ast$, and every product of generators by the product of the replaced generators in the same order, is a consistent rule for the whole Grassmann algebra (an automorphism). Every monomial of $\mathcal L$ contains as many factors of the kind $\Psi$ as of the kind $\Psi^\ast$: this is clear for $K$ and $S$, and $S^k$ consists of $\binom{16}k$ monomials with $k$ factors of each kind (Section 5.9). So every monomial is multiplied by $(e^{i\alpha}e^{-i\alpha})^k=1$, and every admissible $U$, a polynomial of degree at most 16 in $S$, is invariant. $\square$

**Proof of item 2.** With $\alpha=\alpha(x)$ the product rule gives

$$
D_\mu\bigl(e^{i\alpha}\Psi\bigr)=e^{i\alpha}\bigl(D_\mu\Psi+i(\partial_\mu\alpha)\Psi\bigr),\qquad D_\mu\bigl(e^{-i\alpha}\bar\Psi\bigr)=e^{-i\alpha}\bigl(D_\mu\bar\Psi-i(\partial_\mu\alpha)\bar\Psi\bigr),
$$

while $S$ and $U(S)$ do not change. Inserting this into $K$, the phases $e^{\pm i\alpha}$ cancel and

$$
K\ \to\ \tfrac12\Bigl(\bar\Psi\gamma^\mu\bigl(D_\mu\Psi+i\partial_\mu\alpha\,\Psi\bigr)-\bigl(D_\mu\bar\Psi-i\partial_\mu\alpha\,\bar\Psi\bigr)\gamma^\mu\Psi\Bigr)=K+i(\partial_\mu\alpha)\,\bar\Psi\gamma^\mu\Psi=K+i(\partial_\mu\alpha)\,j^\mu .
$$

So $\mathcal L$ changes by $i\sqrt{|g|}\,(\partial_\mu\alpha)j^\mu$, and the coefficient of $\partial_\mu\alpha$ is the Noether current. (It agrees with the Noether formula of Section 5.7, applied with the Grassmann derivative conventions of Section 5.10.) $\square$

For commuting components item 2 already gives conservation by the argument of Section 5.7. If $\alpha$ vanishes near the boundary, $\Psi\to e^{i\alpha}\Psi$ is an allowed variation of the field, so on a solution the change of the action vanishes to first order in $\alpha$: $\int i\sqrt{|g|}\,(\partial_\mu\alpha)j^\mu\,d^8x=0$. Integrating by parts, $\int i\,\alpha\,\partial_\mu(\sqrt{|g|}\,j^\mu)\,d^8x=0$ for every such $\alpha$, and the fundamental lemma of Section 5.2 gives $\partial_\mu(\sqrt{|g|}\,j^\mu)=0$. Item 3 gives more: an identity that holds for every configuration and needs no variational argument, so it holds verbatim for anticommuting components.

**Proof of item 3.** The product rule (the derivative $\partial_\mu$ is even and needs no Grassmann signs) gives

$$
\partial_\mu\bigl(\sqrt{|g|}\,\bar\Psi\gamma^\mu\Psi\bigr)=\sqrt{|g|}\,(\partial_\mu\bar\Psi)\gamma^\mu\Psi+\bar\Psi\,\partial_\mu\bigl(\sqrt{|g|}\,\gamma^\mu\bigr)\Psi+\sqrt{|g|}\,\bar\Psi\gamma^\mu\partial_\mu\Psi .
$$

The only geometric input is the divergence identity of Section 4.12, a consequence of the covariant constancy of the gammas:

$$
\partial_\mu\bigl(\sqrt{|g|}\,\gamma^\mu\bigr)=\sqrt{|g|}\,\bigl(\gamma^\mu\Omega_\mu-\Omega_\mu\gamma^\mu\bigr).
$$

Inserting it and collecting the terms,

$$
\begin{aligned}
\partial_\mu\bigl(\sqrt{|g|}\,j^\mu\bigr)&=\sqrt{|g|}\,\bigl[(\partial_\mu\bar\Psi-\bar\Psi\Omega_\mu)\gamma^\mu\Psi+\bar\Psi\gamma^\mu(\partial_\mu\Psi+\Omega_\mu\Psi)\bigr]\\
&=\sqrt{|g|}\,\bigl[(D_\mu\bar\Psi)\gamma^\mu\Psi+\bar\Psi\gamma^\mu D_\mu\Psi\bigr].
\end{aligned}
$$

On the other hand, by the definitions of $E$ and $\bar E$,

$$
\bar E\,\Psi+\bar\Psi\,E=(D_\mu\bar\Psi)\gamma^\mu\Psi+\bigl(m+U'(S)\bigr)S+\bar\Psi\gamma^\mu D_\mu\Psi-\bigl(m+U'(S)\bigr)S ,
$$

because $U'(S)$ is an even element (a polynomial in $S$), which commutes with every component, so that $\bar\Psi\,U'(S)\Psi=U'(S)\,S$. The two potential terms cancel, and the two expressions agree. No factor was reordered anywhere, so the argument holds for both statistics. $\square$

**Proof of item 4.** On a solution $E=\bar E=0$, so $\partial_\mu(\sqrt{|g|}\,j^\mu)=0$, and $\nabla_\mu j^\mu=|g|^{-1/2}\partial_\mu(\sqrt{|g|}\,j^\mu)=0$ by the divergence formula of Section 4.5. Multiply by $-i$: $\partial_\mu(\sqrt{|g|}\,J^\mu)=0$. Now integrate this over the slab between the slices $x_4=t_1$ and $x_4=t_2$, and over a box in the seven other coordinates. By the fundamental theorem of calculus in each variable (Section 1.10), the term with $\mu=4$ gives $Q(t_2)-Q(t_1)$, and the seven other terms give the flux of $\sqrt{|g|}\,J^i$ through the side faces of the box:

$$
Q(t_2)-Q(t_1)=-\int_{t_1}^{t_2}dx_4\oint\sqrt{|g|}\,J^i\,dS_i .
$$

This is pure calculus and holds in any signature. The flux vanishes when the fields vanish near the side faces, when they fall off fast enough as the box grows, or when opposite faces are identified (a torus), because then the contributions of opposite faces cancel. Then $Q(t_2)=Q(t_1)$. That $J^4$ is indefinite plays no role: $Q$ is conserved although it is not positive. $\square$

**Proof of item 5.** $\sqrt{|g|}\,J^{x_4}=-i\sqrt{|g|}\,\Psi^\dagger C\gamma^{x_4}\Psi$, and in Gaussian normal gauge $\gamma^{x_4}=\gamma^4$ and $-iC\gamma^4=B$. The properties of $B$ are proved in Section 2.12. $\square$

**The quantized field.** The identity of item 3 is algebraic, and in it every $\Psi^\dagger$ stands to the left of every $\Psi$; it therefore holds for the operator-valued field as well. The Heisenberg equations of the quantized theory are the field equations (Section 8.6), and normal ordering changes $Q$ by a constant. Hence the normal-ordered charge $\sum(b^\ast b-d^\ast d)$ is conserved in the quantized theory too. (This step is derived; it is not a separate machine check.)

**Worked example: a charge density that can be negative.** Take flat space, $\lambda=0$, and the two rest states of Section 8.8,

$$
u_+=\tfrac12\bigl(e_0-e_4-i\,e_9-i\,e_{13}\bigr),\qquad u_-=\tfrac12\bigl(e_0+e_4+i\,e_9-i\,e_{13}\bigr),
$$

which satisfy $-i\gamma^4u_\pm=u_\pm$, $Bu_+=u_+$ and $Bu_-=-u_-$. Their scalar product is $u_+^\dagger u_-=\tfrac14\bigl(1\cdot1+(-1)\cdot1+i\cdot i+i\cdot(-i)\bigr)=\tfrac14(1-1-1+1)=0$ (the components of $u_+^\dagger$ are the complex conjugates $\tfrac12,-\tfrac12,\tfrac i2,\tfrac i2$ at the places 0, 4, 9, 13). The commuting field $\Psi=(a\,u_++b\,u_-)\,e^{-imx_4}$ with complex numbers $a,b$ solves the free field equation, because $\gamma^4\partial_4\Psi=\gamma^4(-im)\Psi=m(-i\gamma^4)\Psi=m\Psi$. Its charge density is

$$
J^4=\Psi^\dagger B\Psi=|a|^2u_+^\dagger u_+-|b|^2u_-^\dagger u_-=|a|^2-|b|^2 ,
$$

since the cross terms contain $u_+^\dagger Bu_-=-u_+^\dagger u_-=0$. For $a=\tfrac35$, $b=\tfrac45$ it is $\tfrac9{25}-\tfrac{16}{25}=-\tfrac7{25}$, although the field has positive frequency (both modes are eigenvectors of the rest Hamiltonian $h_0=m(-i\gamma^4)$ of Section 8.9 with the positive eigenvalue $m$) and Hilbert density $|a|^2+|b|^2=1$. Its classical energy density is negative too: for a free plane wave of frequency $\omega$ it is $\rho=\omega J^4$ (Section 7.11), here $\rho=mJ^4=-\tfrac7{25}m$. The charge density is constant in $x_4$, as Theorem M1 requires. In the quantized theory, by contrast, a one-particle state built on any normalized positive-energy mode $u$ has the charge $u^\dagger B\,B\,u=u^\dagger u=1$ (the expectation-value rule of Section 8.12).

**The Kohn–Sham states have a fixed particle number (COMPUTED).** The Kohn–Sham states of Chapters 13 and 14 are computed at a fixed particle number $N$: the Mermin functional contains the constraint $\sum_nf_n=N$ with the chemical potential $\mu$ as its Lagrange multiplier (Section 12.14). For the Stage-4 states of dirac16complex (Chapter 13), in the no-sea convention of Stage 4 the net occupation, particle occupations minus sea holes, is the Kohn–Sham image of the charge $Q$. For the Stage-5 states of dirac16complex00 (Chapter 14) no more is claimed than that they are equilibrium (Mermin) states at fixed $N$: their densities are adopted by prescription, and an honest Gaussian ensemble of classical waves filling the rest shell would have zero charge density (Section 14.8). As a record of data, not a proof, the Wolfram verifier reads the committed Stage-4 runs (check `MA_M1_ksFixedNetNumberRecorded`, measurement `M1_ksFixedNetNumber` of `wolfram-matter-antimatter-report.json`): 56 reference-solver run files with 168 levels and 33 Rust run files all have the net occupation $N$ to $10^{-9}$ relative, with largest absolute deviations $3.5073\times10^{-10}$ (reference solver) and $1.012\times10^{-11}$ (Rust). This is the only check of the two matter-antimatter reports that uses floating-point numbers.

**How M1 was verified.** The Wolfram package represents anticommuting components in an exact Grassmann algebra with 1440 odd generators (the values and first and second derivatives of $\Psi$ and $\Psi^\ast$; compare Section 5.10) and commuting components as exact symbols. With an undefined function $U$ the argument of $U$ is identically invariant, so $U(S)$ is invariant for every function (commuting components, flat space and the three G1 points). For anticommuting components at the three G1 points, with $U=\tfrac\lambda2S^2+\tfrac{c_3}3S^3$, the Lagrangian density has 1848 monomials, all of U(1) charge 0, and the explicit phase automorphism leaves it unchanged; the powers $S^k$, $k=1,\dots,17$, have 16, 120, 560, 1820, 4368, 8008, 11440, 12870, 11440, 8008, 4368, 1820, 560, 120, 16, 1 and 0 monomials. The off-shell identity of item 3 holds exactly at the three G1 points (1088 monomials on its left side for anticommuting components). As a **negative control**, with the notebook's contraction of the spin connection (Section 4.14) the identity fails at all three points, as it must, since the divergence identity fails for that contraction. On shell, with exact solutions of the field equations at the three G1 points for $(m,\lambda)=(3/7,5/11)$, $(-2/5,7/13)$ and $(5/9,-3/8)$, the divergence of the current vanishes, while for generic off-shell data it does not. The independent Python checker verifies, in G_A and in G_B and for both statistics, the U(1) invariance with the exact phase $e^{i\alpha}=(3+4i)/5$, the Noether current, the Euler–Lagrange expressions and the off-shell identity as exact polynomial identities in fully generic field jets (Lagrangian densities of 1364 and 1636 monomials in G_A and 952 and 1224 in G_B for anticommuting and commuting components), and it proves the divergence identity for arbitrary first vielbein jets: both sides are linear in the 512 numbers $\partial_\lambda e_\nu{}^a$ at a point, and all 512 directions are verified exactly (measurements `M1` of `python-matter-antimatter-report.json`). The main check names are

```
wolfram-matter-antimatter-report.json
  MA_M1_u1InvarianceCommutingGenericU_flat  MA_M1_u1InvarianceGrassmann_G1
  MA_M1_noetherCurrentLocalPhase_grassmann_G1  MA_M1_noetherIdentity_grassmann_G1
  MA_M1_noetherIdentity_commuting_G1  MA_M1_negativeControlNotebookConnection
  MA_M1_onShellConservation_G1  MA_M1_chargeDensityMatrix  MA_M1_stage1ChecksCited
python-matter-antimatter-report.json
  MA_M1_noetherIdentity_<X>_<G>  (X = grassmann, commuting; G = G_A..., G_B...)
  MA_M1_divergenceIdentityAllFirstJets  MA_M1
```

### 17.10 Theorem M2, part 1: the maps and the transformation rule

Sakharov's second condition asks whether the theory has symmetries that exchange matter and antimatter. Chapter 6 met the complex conjugations and the reflections of a space-like direction in flat space. This section derives one transformation rule for all candidates of this kind and for both fields. In flat space the rule is a statement about one theory; in a gravitational field it holds in a frame form, which the end of the section explains. Section 17.11 then finds the exact symmetries among the candidates, and its Lemma D shows that no other constant matrix gives one.

**The maps.** For a subset $R\subseteq\{0,\dots,7\}$ of directions let $r_a=-1$ for $a\in R$ and $r_a=+1$ otherwise, and let $x\mapsto Rx$ be the **reflection** $x_a\mapsto r_ax_a$ of the coordinates in $R$. Write $s_R=|R\cap\{0,1,2,3\}|$ for the number of reflected space-like directions and $\sigma_R=(-1)^{s_R}$. For a set $A=\{a_1<\dots<a_k\}$ let $\Gamma_A=\gamma^{a_1}\gamma^{a_2}\cdots\gamma^{a_k}$ be its Clifford monomial (Section 2.5), with $\Gamma_\varnothing=1$, and write $R^c$ for the complement of $R$. For a constant invertible $16\times16$ matrix $M$ we consider the **linear** and the **antilinear** maps

$$
T^{\mathrm{lin}}_{M,R}:\ \Psi'(x)=M\,\Psi(Rx),\qquad T^{\mathrm{anti}}_{M,R}:\ \Psi'(x)=M\,\Psi^\ast(Rx).
$$

An antilinear map contains a complex conjugation: it turns $c\Psi$ into $c^\ast\Psi'$. For $R=\varnothing$ the antilinear maps are the candidates for **charge conjugation** C. For $R\ne\varnothing$ the maps with a Pin(4,4) matrix $M$ (Section 2.14) are reflections, called P-type if $R\subseteq\{0,1,2,3\}$ (space is reflected) and T-type if $4\in R$ (the time $x_4$ is reflected), and their combinations with C. The textbook form $\Psi'=M\bar\Psi^T$ of a charge conjugation is included: since $C^T=C$, $\bar\Psi^T=(\Psi^\dagger C)^T=C\Psi^\ast$, so $M\bar\Psi^T=(MC)\Psi^\ast$.

**Lemma A (the only charge conjugations).** Let $\theta$ be a sign, $+1$ or $-1$ (it has nothing to do with the metric $\eta$). The solutions of $\gamma^aM=\theta\,M(\gamma^a)^\ast$ for all $a$ are the multiples of $1$ for $\theta=+1$ and the multiples of $\gamma^8$ for $\theta=-1$. The solutions of $\gamma^aM=\zeta M(\gamma^a)^T$ for all $a$ are the multiples of $C$ for $\zeta=-1$ and of $\gamma^8C$ for $\zeta=+1$. Hence every constant charge conjugation compatible with the Dirac operator is, up to a factor, one of

$$
\mathrm C_0:\ \Psi\to\Psi^\ast,\qquad \mathrm C_8:\ \Psi\to\gamma^8\Psi^\ast .
$$

(Why this condition: the conjugate of $\gamma^a\partial_a\Psi$ is $(\gamma^a)^\ast\partial_a\Psi^\ast$, and $\gamma^a\partial_a(M\Psi^\ast)$ is a multiple of $M$ times it for every field only if $\gamma^aM=\pm M(\gamma^a)^\ast$.)

*Proof.* The gammas are real, so the first condition reads $\gamma^aM=\theta M\gamma^a$. For $\theta=+1$, $M$ commutes with every $\gamma^a$, and by Corollary 2.3 it is a multiple of $1$. For $\theta=-1$, $\gamma^8$ anticommutes with every $\gamma^a$ (Section 2.10), so $\gamma^8M$ commutes with every $\gamma^a$: $\gamma^a\gamma^8M=-\gamma^8\gamma^aM=\gamma^8M\gamma^a$. Hence $\gamma^8M=c\cdot1$ and $M=c\,\gamma^8$. For the transposed condition, $C$ is symmetric and $C\gamma^a$ antisymmetric, so $(\gamma^a)^TC=(C\gamma^a)^T=-C\gamma^a$, that is $(\gamma^a)^T=-C\gamma^aC^{-1}$. The condition becomes $\gamma^aM=-\zeta MC\gamma^aC^{-1}$, that is $\gamma^a(MC)=-\zeta(MC)\gamma^a$, and the first part, applied to $MC$, gives $MC\propto1$ for $\zeta=-1$ and $MC\propto\gamma^8$ for $\zeta=+1$. With $C^{-1}=C$ and $\gamma^8C=C\gamma^8$ this is the claim. $\square$

**Lemma B (sign patterns).** For every set $R$, the equation $r_a\,M^{-1}\gamma^aM=\varepsilon\,\gamma^a$ for all $a$, with one common sign $\varepsilon$, has up to a factor exactly two solutions: $M=\Gamma_R$ with $\varepsilon=(-1)^{|R|}$, and $M=\Gamma_{R^c}$ with $\varepsilon=-(-1)^{|R|}$. Both are real orthogonal matrices ($M^\dagger=M^T=M^{-1}$), and

$$
M^\dagger CM=\sigma_R\,C,\qquad \sigma_R=(-1)^{s_R}.
$$

*Proof.* By rule (R3) of Section 2.5, for a monomial $\Gamma_A$ of degree $k=|A|$: $\Gamma_A^{-1}\gamma^a\Gamma_A=(-1)^k\gamma^a$ if $a\notin A$ and $(-1)^{k-1}\gamma^a$ if $a\in A$. For $A=R$ this is $(-1)^{|R|}r_a\gamma^a$, so $r_a\Gamma_R^{-1}\gamma^a\Gamma_R=(-1)^{|R|}\gamma^a$ (use $r_a^2=1$). For $A=R^c$, whose size $8-|R|$ has the parity of $|R|$, the roles of "in" and "not in" are exchanged, and $r_a\Gamma_{R^c}^{-1}\gamma^a\Gamma_{R^c}=-(-1)^{|R|}\gamma^a$. If $M$ and $M'$ solve the same equation with the same sign, then $M^{-1}\gamma^aM=M'^{-1}\gamma^aM'$, so $M'M^{-1}$ commutes with every $\gamma^a$ and is a multiple of $1$ (Corollary 2.3). Every monomial is a product of signed permutation matrices, hence real and orthogonal. Finally, $M^\dagger CM=M^{-1}\gamma^0\gamma^1\gamma^2\gamma^3M=\prod_{a=0}^{3}\bigl(M^{-1}\gamma^aM\bigr)=\prod_{a=0}^{3}\bigl(\varepsilon r_a\gamma^a\bigr)=\varepsilon^4\,r_0r_1r_2r_3\,C=\sigma_RC$. $\square$

**Lemma C (the statistics sign).** For every matrix $Y$, $\Psi^TY\Psi^\ast=s\,\Psi^\dagger Y^T\Psi$, and the same holds with a derivative on either factor.

*Proof.* $\Psi^TY\Psi^\ast=\sum_{i,j}\Psi_iY_{ij}\Psi^\ast_j=s\sum_{i,j}\Psi_j^\ast Y_{ij}\Psi_i=s\,\Psi^\dagger Y^T\Psi$: exchanging two odd factors costs a sign, exchanging two commuting factors does not. $\square$

**Theorem M2 (the transformation rule).** Let $M$ be one of the two solutions of Lemma B for the set $R$, with its sign $\varepsilon$ (a factor of modulus 1 in front of $M$ changes nothing). Then, for $U=\tfrac\lambda2S^2$,

$$
\mathcal L_{m,\lambda}[T\Psi](x)=\kappa\,\mathcal L_{\sigma\kappa m,\,\kappa\lambda}[\Psi](Rx),\qquad j'^a(x)=c_j\,r_a\,j^a(Rx),
$$

where

$$
\begin{aligned}
&\text{linear maps:}&&\kappa=\sigma_R\varepsilon,\qquad \sigma=\sigma_R,\qquad c_j=\kappa,\\
&\text{antilinear maps:}&&\kappa=s\,\sigma_R\varepsilon,\qquad \sigma=s\,\sigma_R,\qquad c_j=-\kappa .
\end{aligned}
$$

In words: the kinetic term is multiplied by $\kappa$, the scalar $S$ by $\sigma$, and the current by $c_j$ in addition to the sign $r_a$ that every vector component gets under the reflection.

*Proof for linear maps (flat space).* Now $\partial_a\Psi'(x)=r_aM(\partial_a\Psi)(Rx)$ and $\Psi'^\dagger=\Psi^\dagger M^\dagger$. By Lemma B, $M^\dagger CM=\sigma_RC$ and $M^\dagger C\gamma^aM=(M^{-1}CM)(M^{-1}\gamma^aM)=\sigma_R\varepsilon\,r_a\,C\gamma^a$. Hence $S\to\sigma_RS$ and $j^a\to\sigma_R\varepsilon\,r_aj^a$. In $K$ every term carries one matrix $C\gamma^a$ and one derivative $\partial_a$, so it acquires $\sigma_R\varepsilon\,r_a\cdot r_a=\sigma_R\varepsilon=\kappa$. Therefore, using $\kappa^2=1$ and $(\sigma S)^2=S^2$,

$$
\kappa K-m\sigma S-\tfrac\lambda2S^2=\kappa\Bigl[K-(\sigma\kappa m)S-\tfrac{\kappa\lambda}2S^2\Bigr],
$$

which is $\kappa\,\mathcal L_{\sigma\kappa m,\kappa\lambda}$ (divided by $\sqrt{|g|}=1$). $\square$

*Proof for antilinear maps (flat space).* Now $\Psi'^\dagger=\Psi^TM^\dagger$ (the conjugate of $M\Psi^\ast$ is $M\Psi$ because $M$ is real). By Lemma C and Lemma B,

$$
S'=\Psi^T\bigl(M^\dagger CM\bigr)\Psi^\ast=\sigma_R\,\Psi^TC\Psi^\ast=s\sigma_R\,\Psi^\dagger C^T\Psi=s\sigma_R\,S .
$$

For the kinetic term put $Y=M^\dagger C\gamma^aM=\sigma_R\varepsilon\,r_aC\gamma^a$ and use $(C\gamma^a)^T=-C\gamma^a$:

$$
\begin{aligned}
\Psi'^\dagger C\gamma^a\partial_a\Psi'&=r_a\,\Psi^TY\partial_a\Psi^\ast=r_a\,s\,(\partial_a\Psi^\dagger)Y^T\Psi=-s\sigma_R\varepsilon\,(\partial_a\Psi^\dagger)C\gamma^a\Psi,\\
-(\partial_a\Psi'^\dagger)C\gamma^a\Psi'&=-r_a\,(\partial_a\Psi^T)Y\Psi^\ast=-r_a\,s\,\Psi^\dagger Y^T\partial_a\Psi=s\sigma_R\varepsilon\,\Psi^\dagger C\gamma^a\partial_a\Psi .
\end{aligned}
$$

Adding and halving, $K\to s\sigma_R\varepsilon\,K$. In the same way $j'^a=\Psi^TY\Psi^\ast=s\Psi^\dagger Y^T\Psi=-s\sigma_R\varepsilon\,r_aj^a$. The Lagrangian follows as in the linear case. $\square$

*Curved fields: the frame form.* In a gravitational field the maps are used in **frame form**: the points are not moved, $\Psi'(x)=M\Psi(x)$ (or $M\Psi^\ast(x)$), and at the same time the frame is changed by the constant signs, $e'_\mu{}^a=r_a\,e_\mu{}^a$ (no sum over $a$). This leaves the metric unchanged, $g'_{\mu\nu}=\sum_ar_a^2\,e_\mu{}^a\eta_{aa}e_\nu{}^a=g_{\mu\nu}$, because $\eta$ is diagonal and $r_a^2=1$, and hence also the Christoffel symbols. The inverse frame changes in the same way, $e'_a{}^\mu=r_a\,e_a{}^\mu$, because $\sum_\mu r_ae_a{}^\mu\,r_be_\mu{}^b=r_ar_b\,\delta_a{}^b=\delta_a{}^b$. So $\gamma'^\mu=\sum_ar_a\,e_a{}^\mu\gamma^a$, and the formula of Section 4.11 for the spin connection gives

$$
\omega'_\mu{}^a{}_b=e'_b{}^\nu\bigl(\Gamma^\rho{}_{\mu\nu}\,e'_\rho{}^a-\partial_\mu e'_\nu{}^a\bigr)=r_b\,e_b{}^\nu\bigl(\Gamma^\rho{}_{\mu\nu}\,r_ae_\rho{}^a-r_a\,\partial_\mu e_\nu{}^a\bigr)=r_ar_b\,\omega_\mu{}^a{}_b ,
$$

and after lowering the index with the diagonal $\eta$, $\omega'_{\mu ab}=r_ar_b\,\omega_{\mu ab}$. Multiplying the equation $r_aM^{-1}\gamma^aM=\varepsilon\gamma^a$ of Lemma B by $M$ from the left and by $M^{-1}$ from the right gives $r_a\gamma^a=\varepsilon M\gamma^aM^{-1}$, that is $M\gamma^aM^{-1}=\varepsilon r_a\gamma^a$ (multiply by $\varepsilon$ and use $\varepsilon^2=1$), hence $MS^{ab}M^{-1}=\tfrac14[\varepsilon r_a\gamma^a,\varepsilon r_b\gamma^b]=r_ar_bS^{ab}$, $\Omega'_\mu=\tfrac12\omega'_{\mu ab}S^{ab}=M\Omega_\mu M^{-1}$ and $D'_\mu(M\Psi)=\partial_\mu(M\Psi)+M\Omega_\mu M^{-1}M\Psi=M\,D_\mu\Psi$. For antilinear maps one also needs $(D_\mu\Psi)^\ast=D_\mu\Psi^\ast$, which holds because $\Omega_\mu$ is real. With these replacements the flat computation goes through unchanged: $\partial_a$ is replaced by $e_a{}^\mu D_\mu$, and the sign $r_a$ that the reflection of the points supplied in flat space is now supplied by the frame change. So the rule holds in every gravitational field in the frame form

$$
\mathcal L_{m,\lambda}[T\Psi;\,e\,\mathrm{diag}(r)](x)=\kappa\,\mathcal L_{\sigma\kappa m,\,\kappa\lambda}[\Psi;\,e](x),
$$

where the second argument names the frame that is used. Read this carefully: it relates the theory on the frame $e\,\mathrm{diag}(r)$ to the theory on the frame $e$. For $R=\varnothing$ the two frames are the same, and the rule is a statement about one theory in every gravitational field. For $R\ne\varnothing$ it is a statement about one theory only when the frame change can be undone; Section 17.11 examines when this happens.

*The coordinate form.* Suppose now that the reflection of the points carries the frame into the reflected frame, $e_\mu{}^a(x)=r_\mu r_a\,e_\mu{}^a(Rx)$ for all $\mu$ and $a$ (no sums). This holds in flat space, and for example for a diagonal frame whose entries do not depend on the reflected coordinates; it makes the reflection an **isometry**, a map of the points that leaves the metric unchanged, $g_{\mu\nu}(x)=r_\mu r_\nu\,g_{\mu\nu}(Rx)$. Then the inverse frame obeys the same rule, the Christoffel symbols obey $\Gamma^\rho{}_{\mu\nu}(x)=r_\rho r_\mu r_\nu\,\Gamma^\rho{}_{\mu\nu}(Rx)$ (each index of a derivative or of the metric brings its sign), and the formula of Section 4.11 gives $\omega_\mu{}^a{}_b(x)=r_\mu\,r_ar_b\,\omega_\mu{}^a{}_b(Rx)$. For the reflected field $\Psi'(x)=M\Psi(Rx)$ every derivative and every connection term with index $\mu$ brings the sign $r_\mu$, every frame factor $e_a{}^\mu$ brings $r_\mu r_a$, and the two signs $r_\mu$ cancel. What remains is exactly the frame form at the point $Rx$. So in such a field the coordinate form holds for the one theory on the frame $e$: $\mathcal L_{m,\lambda}[T\Psi](x)=\kappa\,\mathcal L_{\sigma\kappa m,\kappa\lambda}[\Psi](Rx)$. $\square$

### 17.11 Theorem M2, part 2: C, P and CP for the two fields

Theorem M2 treats the two matrices of Lemma B. The next lemma shows that no other constant matrix can give an exact symmetry, so that nothing is missed. Here, and in Corollary M2.1, a map is an **exact symmetry** if $\mathcal L_{m,\lambda}[T\Psi](x)=\mathcal L_{m,\lambda}[\Psi](Rx)$ for every field $\Psi$, in flat space or in a gravitational field in which the reflection is an isometry (Section 17.10).

**Lemma D (no other matrices).** Let $M$ be any constant invertible $16\times16$ matrix and $R$ any set, and suppose that the linear or the antilinear map with $M$ and $R$ is an exact symmetry in flat space for some $m\ne0$ and some $\lambda$. Then $r_aM^{-1}\gamma^aM=\gamma^a$ for all $a$, so that $M=c\,M_0$, where $M_0$ is the solution of Lemma B with $\varepsilon=+1$ and $c$ a number. Moreover $|c|^2\sigma_R=1$ for the linear map and $|c|^2\sigma_R=s$ for the antilinear map; hence $|c|=1$, and $\sigma_R=1$, respectively $\sigma_R=s$.

*Proof.* Both sides of the defining relation are polynomials in the values $\Psi_i$, $\Psi_i^\ast$ and the first derivatives $\partial_a\Psi_i$, $\partial_a\Psi_i^\ast$ at one point, which can be chosen independently of each other. For anticommuting components different monomials are independent elements of the Grassmann algebra (Section 5.9); for commuting components a polynomial in the real and imaginary parts of complex numbers that vanishes for all their values has only zero coefficients. So the coefficient of each monomial must be the same on both sides. The coefficient of $\Psi_i^\ast\Psi_j$ (no derivative) comes from the mass term, and the coefficient of $\Psi_i^\ast\,\partial_a\Psi_j$ from the first half of $K$, which is $\tfrac12(C\gamma^a)_{ij}$ on the right-hand side.

*Linear map.* $\Psi'^\dagger=\Psi^\dagger M^\dagger$ and $\partial_a\Psi'(x)=r_aM(\partial_a\Psi)(Rx)$. The mass terms give $m\,(M^\dagger CM)_{ij}=m\,C_{ij}$, so $M^\dagger CM=C$ because $m\ne0$. The kinetic terms give $\tfrac12r_a(M^\dagger C\gamma^aM)_{ij}=\tfrac12(C\gamma^a)_{ij}$, so $r_aM^\dagger C\gamma^aM=C\gamma^a$. Multiplying $M^\dagger CM=C$ by $M^{-1}$ from the right gives $M^\dagger C=CM^{-1}$; inserted into the second equation, $r_a\,CM^{-1}\gamma^aM=C\gamma^a$, and multiplying by $C^{-1}=C$ from the left, $r_aM^{-1}\gamma^aM=\gamma^a$.

*Antilinear map.* $\Psi'^\dagger=\Psi^TM^\dagger$. By Lemma C, $S'=\Psi^T(M^\dagger CM)\Psi^\ast=s\,\Psi^\dagger(M^\dagger CM)^T\Psi$, so the mass terms give $s(M^\dagger CM)^T=C$, that is $M^\dagger CM=sC$ ($C$ is symmetric). In $K'$ only the second half, $-(\partial_a\Psi'^\dagger)C\gamma^a\Psi'=-r_a(\partial_a\Psi^T)Y\Psi^\ast$ with $Y=M^\dagger C\gamma^aM$, contains monomials of the kind $\Psi^\ast\,\partial_a\Psi$; by Lemma C it equals $-r_as\,\Psi^\dagger Y^T\partial_a\Psi$. So $-\tfrac12r_as\,Y^T=\tfrac12C\gamma^a$, and transposing with $(C\gamma^a)^T=-C\gamma^a$, $Y=s\,r_a\,C\gamma^a$. With $M^\dagger C=sCM^{-1}$ (from $M^\dagger CM=sC$) this reads $s\,CM^{-1}\gamma^aM=s\,r_aC\gamma^a$, hence again $r_aM^{-1}\gamma^aM=\gamma^a$.

In both cases $M$ solves the equation of Lemma B with $\varepsilon=+1$, whose solutions are the multiples of $M_0$. Finally $M^\dagger CM=|c|^2M_0^\dagger CM_0=|c|^2\sigma_RC$ by Lemma B, and this must equal $C$ (linear map) or $sC$ (antilinear map). $\square$

The same comparison with the signs kept shows a little more (derived here, not a separate machine check): if a map of this kind with $m\ne0$ satisfies $\mathcal L_{m,\lambda}[T\Psi](x)=\kappa\,\mathcal L_{m',\lambda'}[\Psi](Rx)$ with a sign $\kappa$ and some $m',\lambda'$, then $M^\dagger CM=\sigma'C$ with $\sigma'=\kappa m'/m$ for the linear map ($\sigma'\ne0$, because $M^\dagger CM$ is invertible), the kinetic terms give $r_aM^{-1}\gamma^aM=(\kappa/\sigma')\gamma^a$, and squaring both sides ($(M^{-1}\gamma^aM)^2=(\gamma^a)^2$) gives $(\kappa/\sigma')^2=1$. For the antilinear map the same steps give $M^\dagger CM=s\sigma'C$ and again $r_aM^{-1}\gamma^aM=(\kappa/\sigma')\gamma^a$. So $M$ is again a solution of Lemma B, with $\varepsilon=\kappa/\sigma'$, and comparing $M^\dagger CM$ with Lemma B as above shows that the factor in front of it has modulus 1. The 1024 maps counted below therefore contain, up to such factors, every map of this kind whose Lagrangian is $\pm\mathcal L_{m',\lambda'}$.

**Corollary M2.1 (exact symmetries).** A map of Section 17.10 is an exact symmetry for all $m$ and $\lambda$ if and only if $\kappa=\sigma=1$. It is then a symmetry for every potential $U$, because $K\to K$ and $S\to S$. Explicitly:

- linear maps: an exact symmetry with the reflected set $R$ exists if and only if $s_R$ is even, for any number of reflected time-like directions; it is the monomial among $\Gamma_R$, $\Gamma_{R^c}$ that has $\varepsilon=+1$;
- antilinear maps, commuting components: if and only if $s_R$ is even;
- antilinear maps, anticommuting components: if and only if $s_R$ is odd.

*Proof.* By Lemma D an exact symmetry of flat space, whatever its constant matrix, is up to a factor of modulus 1 one of the maps of Theorem M2, so it suffices to examine these (in a gravitational field in which the reflection is an isometry they obey the same rule, Section 17.10); for them the rule gives $\mathcal L_{m,\lambda}\to\kappa\mathcal L_{\sigma\kappa m,\kappa\lambda}$, which equals $\mathcal L_{m,\lambda}$ for all $m$ and $\lambda$ exactly when $\kappa=\sigma=1$. For linear maps, $\sigma=\sigma_R=1$ means $s_R$ even, and then $\kappa=\varepsilon=1$ picks one of the two monomials, which have opposite signs $\varepsilon$ (Lemma B). For antilinear maps, $\sigma=s\sigma_R=1$ means $\sigma_R=s$ ($s_R$ even for $s=+1$, odd for $s=-1$), and then $\kappa=\varepsilon=1$ again picks one monomial. So for each allowed set $R$ there is, up to a factor of modulus 1, exactly one exact map of each type. The Lagrangian relation equates the densities at the points $x$ and $Rx$; a reflection does not change volumes, so the action is unchanged, and solutions are mapped to solutions. $\square$

No map of this kind sends $\mathcal L_{m,\lambda}$ to $-\mathcal L_{m,\lambda}$ when $\lambda\ne0$: that would need $\kappa=-1$ together with $\sigma\kappa=1$ and $\kappa\lambda=\lambda$, which contradict each other. For $\lambda=0$ the maps with $\kappa=\sigma=-1$ send $\mathcal L_{m,0}$ to $-\mathcal L_{m,0}$, and they are then symmetries of the field equations, which are the same for $\mathcal L$ and $-\mathcal L$.

**Corollary M2.2 (the charge).** For an exact symmetry $c_j=+1$ if the map is linear and $c_j=-1$ if it is antilinear. Hence, if $x_4$ is not reflected ($r_4=+1$), an exact linear symmetry preserves $J^4$ and $Q$, and an exact antilinear symmetry reverses them, $Q\to-Q$.

*Proof.* $c_j=\kappa=1$ for linear and $c_j=-\kappa=-1$ for antilinear exact maps. With $r_4=+1$ the rule gives $j'^4(x)=c_j\,j^4(Rx)$, and integrating over a slice, whose coordinates are merely reflected, gives $Q'=c_jQ$. $\square$

**Counting.** For each statistics there are $2^8=256$ sets $R$, 2 matrices and 2 types, so 1024 maps. Their Lagrangian images fall into the four classes $\mathcal L_{m,\lambda}$, $\mathcal L_{-m,\lambda}$, $-\mathcal L_{m,-\lambda}$ and $-\mathcal L_{-m,-\lambda}$ with 256 maps each. The exact symmetries number 256 for each statistics: 128 linear ($R\cap\{0,1,2,3\}$ of even size, 8 choices, times any subset of $\{4,5,6,7\}$, 16 choices) and 128 antilinear. The exact symmetries that reverse $Q$ without reflecting $x_4$ are the exact antilinear maps with $4\notin R$: 8 choices of $R\cap\{0,1,2,3\}$ with the right parity times 8 subsets of $\{5,6,7\}$, that is **64 for each statistics**.

**Worked example: three rows from the rule.** (i) $\mathrm C_0$ on commuting components: $R=\varnothing$, $M=1=\Gamma_\varnothing$, so $\varepsilon=(-1)^0=+1$, $\sigma_R=+1$ and $s=+1$; hence $\kappa=\sigma=+1$ and $c_j=-1$. The map is exact and reverses the charge. (ii) The same map on anticommuting components: now $s=-1$, so $\kappa=\sigma=-1$ and $\mathcal L_{m,\lambda}\to-\mathcal L_{(-1)(-1)m,\,-\lambda}=-\mathcal L_{m,-\lambda}$: not a symmetry. (iii) $\mathrm C_8\mathrm P_1$ on anticommuting components, the map $\Psi'(x)=\Gamma_{\{0,2,3,4,5,6,7\}}\Psi^\ast(R_1x)$ that reflects $x_1$: $R=\{1\}$ and $M=\Gamma_{R^c}$, so $\varepsilon=-(-1)^1=+1$, $s_R=1$, $\sigma_R=-1$ and $s=-1$; hence $\kappa=(-1)(-1)(+1)=+1$, $\sigma=(-1)(-1)=+1$ and $c_j=-1$. The map is exact and reverses the charge. (In $\gamma^8\gamma^1=\gamma^0\gamma^1\gamma^2\cdots\gamma^7\gamma^1$ move the last factor to the left past the six factors $\gamma^7,\dots,\gamma^2$, which gives the sign $(-1)^6=+1$, and use $(\gamma^1)^2=1$: so $\gamma^8\gamma^1=\Gamma_{\{0,2,3,4,5,6,7\}}$, and the map is $\mathrm C_8$ applied after the reflection $\Psi\to\gamma^1\Psi(R_1x)$.)

A direct way to see (i): the gammas are real and $S=\Psi^\dagger C\Psi$ is real for commuting components, so the complex conjugate of the field equation $\gamma^\mu D_\mu\Psi=(m+\lambda S)\Psi$ is the same equation for $\Psi^\ast$. Every solution $\Psi$ has the partner solution $\Psi^\ast$, and its charge density is $(\Psi^\ast)^\dagger B\Psi^\ast=\Psi^TB\Psi^\ast=\Psi^\dagger B^T\Psi=-\Psi^\dagger B\Psi$, because $B^T=-B$ ($B=-iC\gamma^4$ with $C\gamma^4$ antisymmetric).

**C, P, CP, T and CPT for the two fields.** The table applies the rule to the maps with names. $R_Ax$ is $x$ with the coordinates $x_a$, $a\in A$, reversed. "exact" means $\mathcal L\to\mathcal L$; the effect on $Q$ is given for the maps that do not reflect $x_4$ and whose effect on the charge the matter-antimatter document records. $\mathrm P_b$ is the Pin(4,4) lift $\gamma^b$ of the reflection of $x_b$ (Section 2.14).

| Map | Definition | dirac16complex00 (commuting) | dirac16complex (anticommuting) |
| --- | --- | --- | --- |
| $\mathrm C_0$ | $\Psi^\ast(x)$ | exact, $Q\to-Q$ | $-\mathcal L_{m,-\lambda}$, $Q\to Q$ |
| $\mathrm C_8$ | $\gamma^8\Psi^\ast(x)$ | $-\mathcal L_{-m,-\lambda}$, $Q\to Q$ | $\mathcal L_{-m,\lambda}$, $Q\to-Q$ |
| chirality | $\gamma^8\Psi(x)$ | $-\mathcal L_{-m,-\lambda}$, $Q\to-Q$ | $-\mathcal L_{-m,-\lambda}$, $Q\to-Q$ |
| $\mathrm P_b$, $b\le3$ | $\gamma^b\Psi(R_bx)$ | $\mathcal L_{-m,\lambda}$ | $\mathcal L_{-m,\lambda}$ |
| $\mathrm C_0\mathrm P_b$ | $\gamma^b\Psi^\ast(R_bx)$ | $\mathcal L_{-m,\lambda}$ | $-\mathcal L_{-m,-\lambda}$ |
| $\mathrm C_8\mathrm P_b$ | $\Gamma_{\{b\}^c}\Psi^\ast(R_bx)$ | $-\mathcal L_{m,-\lambda}$ | exact, $Q\to-Q$ |
| $\mathrm C_8\mathrm P_{123}$ | $\Gamma_{\{0,4,5,6,7\}}\Psi^\ast(R_{123}x)$ | $-\mathcal L_{m,-\lambda}$ | exact, $Q\to-Q$ |
| $\mathrm P_{0123}$ | $C\Psi(R_{0123}x)$ | exact, $Q\to Q$ | exact, $Q\to Q$ |
| $\mathrm C_0\mathrm P_{0123}$ | $C\Psi^\ast(R_{0123}x)$ | exact, $Q\to-Q$ | $-\mathcal L_{m,-\lambda}$ |
| T, linear | $\Gamma_{\{4\}^c}\Psi(R_4x)$ | exact | exact |
| T, antilinear | $\Gamma_{\{4\}^c}\Psi^\ast(R_4x)$ | exact | $-\mathcal L_{m,-\lambda}$ |
| total inversion | $\gamma^8\Psi(-x)$ | exact | exact |
| CPT | $\gamma^8\Psi^\ast(-x)$ | exact | $-\mathcal L_{m,-\lambda}$ |
| $\mathrm C\mathrm P_{123}\mathrm T$ | $\gamma^1\gamma^2\gamma^3\gamma^4\Psi^\ast(R_{1234}x)$ | $-\mathcal L_{m,-\lambda}$ | exact |

Reading of the table:

- **dirac16complex00 (commuting field).** C is exact and reverses the charge. P and CP with one (or three) reflected space-like directions are not exact for $m\ne0$; P is exact at $m=0$. CP with an even number of reflected space-like directions, for example $\mathrm C_0\mathrm P_{0123}$, is exact. T (linear and antilinear) and the full antilinear inversion CPT are exact.
- **dirac16complex (anticommuting field).** No constant C is exact for $m\ne0$: $\mathrm C_0$ gives $-\mathcal L_{m,-\lambda}$, and $\mathrm C_8$ gives $\mathcal L_{-m,\lambda}$, the theory with the opposite mass (so C is exact at $m=0$). CP with an odd number of reflected space-like directions is exact and reverses the charge: $\mathrm C_8\mathrm P_b$ for $b=0,1,2,3$ and $\mathrm C_8\mathrm P_{123}$. T is exact as a linear map (after quantization it is of antiunitary type, see below). The antilinear total inversion is not exact, while $\mathrm C\mathrm P_{123}\mathrm T$ is.

**Which entries hold in a gravitational field.** The table is computed in flat space. The rows with $R=\varnothing$, the maps $\mathrm C_0$, $\mathrm C_8$ and the chirality map, move neither the points nor the frame, so by Section 17.10 their entries hold for one theory in every gravitational field; in particular $\mathrm C_0$ is an exact, charge-reversing symmetry of dirac16complex00 in every gravitational field. Every other row reflects points. In a gravitational field in which the reflection is an isometry, such as the primordial field of Chapter 9 for the reflections of $x_1$, $x_2$ and $x_3$ (its metric is diagonal and depends only on $x_0$ and $x_4$, Section 9.2), the coordinate form of Section 17.10 holds and the entry is unchanged. In a generic gravitational field only the frame form holds, and it relates the theory on the frame $e$ to the theory on the frame $e\,\mathrm{diag}(r)$. For the CP maps of the anticommuting field these are really two different theories, for two reasons.

1. *No frame rotation undoes the frame change.* $\mathcal L$ is invariant under the frame rotations of $\mathrm{Spin}_0(4,4)$ (Section 2.14), whose vector matrices $\Lambda$ are products of exponentials and can therefore be joined to the unit matrix by letting all angles go to 0. Write $\Lambda$ in blocks, with $A$ the $4\times4$ block of the space-like directions and $G$ the block that maps them to the time-like ones. The space-like block of the equation $\Lambda^T\eta\Lambda=\eta$ reads $A^TA-G^TG=I_4$, so $A^TA=I_4+G^TG$, whose eigenvalues are at least 1, and $(\det A)^2=\det(A^TA)\ge1$. So $\det A$ never lies between $-1$ and $1$; it equals 1 at the unit matrix and changes continuously with the angles, so it is at least 1 for every such $\Lambda$. The matrix $\mathrm{diag}(r)$ of a CP map has $\det A=(-1)^{s_R}=-1$ ($s_R$ is odd), so it is not a frame rotation of this kind.
2. *No other exact symmetry undoes it either.* The only matrices that turn the gammas as $\mathrm{diag}(r)$ does are its two linear Pin lifts $\Gamma_R$ and $\Gamma_{R^c}$ (Lemma B), and by Corollary M2.1 neither is an exact symmetry when $s_R$ is odd.

At a fixed frame, the internal part $\Psi\to\Gamma_{R^c}\Psi^\ast$ of such a map multiplies the kinetic terms of the different frame directions by different signs, and nothing compensates them: it turns $\mathcal L$ into none of $\pm\mathcal L_{\pm m,\pm\lambda}$. **So CP of dirac16complex is exact in flat space and in every gravitational field in which the reflection is an isometry, and a generic gravitational field breaks it.** This opens no way to an asymmetry: Theorem M1 holds in every gravitational field, so the charge stays conserved and Sakharov's first condition fails exactly. The committed exact-results file states this scope (`matter-antimatter-theory.json`, key `M2`, entries `answer.grassmann` and `answer.sakharov2`), and the committed Python checker verifies it in the check `MA_M2_cpScopeInCurvedFields`: at a fixed frame of the generic field G_A the internal parts of $\mathrm C_8\mathrm P_0,\dots,\mathrm C_8\mathrm P_3$ and $\mathrm C_8\mathrm P_{123}$ give none of $\pm\mathcal L_{\pm m,\pm\lambda}$, while with the reflection the same matrices give the exact, charge-reversing maps; all $8\times16=128$ sign patterns with an odd number of reflected space-like directions have $\det A=-1$; and neither linear Pin lift of any of them is exact. (This check is not in the committed Python report, which was written by an earlier version of the checker; Section 17.17.) The same limitation applies to every table row that reflects points: it holds in flat space and wherever the reflection is an isometry.

**For both fields an exact symmetry exists that preserves $x_4$ and reverses $Q$:** $\mathrm C_0$ for the commuting field, in every gravitational field, and $\mathrm C_8\mathrm P_b$ for the anticommuting field, in flat space and in gravitational fields in which the reflection of $x_b$ is an isometry. By Proposition 17.2, such a symmetry alone forbids the creation of an average charge from a symmetric state.

**The quantized anticommuting field.** After quantization (Chapter 8), a symmetry must be carried by an operator on the space of states: a **unitary** operator preserves inner products (Section 8.2); an **antiunitary** operator preserves them up to complex conjugation and complex-conjugates every number it passes, which is how time reversal is implemented in ordinary quantum mechanics. A map of the field operators can be implemented by such an operator only if it preserves the canonical anticommutator $\{\Psi_a,\Psi_b^\dagger\}=B_{ab}\,\delta^7$ (flat space, Gaussian normal gauge). A unitary operator leaves numbers alone, so the transformed operators must reproduce the number matrix $B$; an antiunitary operator complex-conjugates numbers, so they must reproduce $B^\ast=-B$. We call a map of **unitary type** if it passes the first test (it is then a linear automorphism of the anticommutation relations) and of **antiunitary type** if it passes the second (an antilinear automorphism). Passing the test is necessary for an implementation, not sufficient; whether an actual operator exists is the OPEN question at the end of this paragraph. Lemma B gives $M\gamma^aM^{-1}=\varepsilon r_a\gamma^a$ (multiply $r_aM^{-1}\gamma^aM=\varepsilon\gamma^a$ by $\varepsilon r_aM$ from the left and by $M^{-1}$ from the right) and hence, multiplying four of these, $MCM^{-1}=\sigma_RC$, so that $MBM^{-1}=\sigma_R\varepsilon\,r_4\,B$; and $B^T=-B$. For a linear map $\Psi\to M\Psi$ and for the antilinear map $\Psi\to M\Psi^{\dagger T}$ (the operator version of $M\Psi^\ast$; its adjoint is $M\Psi$ because $M$ is real):

$$
\begin{aligned}
&\{M\Psi,(M\Psi)^\dagger\}=MBM^\dagger=\sigma_R\varepsilon\,r_4\,B,\\
&\{(M\Psi^{\dagger T})_a,\ (M\Psi)_b\}=\sum_{c,d}M_{ac}M_{bd}\{\Psi^\dagger_c,\Psi_d\}=\bigl(MB^TM^\dagger\bigr)_{ab}=-\sigma_R\varepsilon\,r_4\,B_{ab} .
\end{aligned}
$$

For an exact symmetry of the anticommuting field ($\sigma_R\varepsilon=1$ for linear maps; $\sigma_R=-1$ and $\varepsilon=1$ for antilinear maps) both right-hand sides equal $r_4B$. Hence every exact symmetry is compatible with the canonical structure: it is of unitary type if it preserves $x_4$ and of antiunitary type if it reverses $x_4$ (derived; the Wolfram verifier confirms it for all 256 exact maps, check `MA_M2_canonicalStructure`). The charge conjugation of unitary type is $\mathrm C_8$ ($\gamma^8B^T\gamma^8=-\gamma^8B\gamma^8=B$), whereas $\mathrm C_0$ is of antiunitary type although it preserves $x_4$ ($1\cdot B^T\cdot1=-B$). For the CP of unitary type, $\mathrm C_8\mathrm P_b$ with $M=\Gamma_{\{b\}^c}$, the charge density becomes

$$
J'^4=\sum_{a,d}\bigl(M\Psi\bigr)_aB_{ad}\bigl(M\Psi^{\dagger T}\bigr)_d=\sum_{c,e}\Psi_c\,\bigl(M^TBM\bigr)_{ce}\,\Psi^\dagger_e .
$$

Reordering the operators with the anticommutator, $\Psi_c\Psi^\dagger_e=-\Psi^\dagger_e\Psi_c+B_{ce}\delta^7$, and using $(M^TBM)^T=M^TB^TM=-M^TBM$, gives

$$
J'^4=-\Psi^\dagger(M^TBM)^T\Psi+(\text{a number})=\Psi^\dagger\,M^TBM\,\Psi+(\text{a number}).
$$

By Lemma B, $M^TBM=M^{-1}BM=\sigma_R\varepsilon\,r_4\,B=-B$ for this map. So $J'^4=-J^4$ up to a constant, and the normal-ordered charge is reversed, $:\!Q\!:\ \to-:\!Q\!:$ (derived). **OPEN:** whether each of these maps of unitary or antiunitary type is actually implemented by a unitary or antiunitary operator on the positive ($J=B$) Fock space of the good sector (Section 8.10) is not decided in the repository (the committed reports say the same: `MA_M2_canonicalStructure` of the Wolfram report and `MA_M2_canonicalStructureOfExactGrassmannSymmetries` of the Python report).

**A remark on the slicing in signature (4,4).** The group $\mathrm{Spin}_0(4,4)$ of products of exponentials $\exp(\theta S^{ab})$ (Section 2.14), under which $\mathcal L$ is invariant, contains the element

$$
\exp(\pi S^{45})=\cos\tfrac\pi2+\gamma^4\gamma^5\sin\tfrac\pi2=\gamma^4\gamma^5 ,
$$

because $(\gamma^4\gamma^5)^2=-(\gamma^4)^2(\gamma^5)^2=-1$ makes the pair $(4,5)$ of two time-like directions a "rotation" pair (Section 2.11). It rotates the plane of the times $x_4$ and $x_5$ by the angle $\pi$, $(x_4,x_5)\to(-x_4,-x_5)$. In flat space, as a linear map with $R=\{4,5\}$ and $M=\Gamma_R$, it has $\varepsilon=(-1)^2=+1$ and $s_R=0$, so it is exact, and $c_j=+1$ with $r_4=-1$ gives $J'^4(x)=-J^4(Rx)$: it maps every classical solution of charge $Q$ into one of charge $-Q$. The product of four such rotations, in the planes $(0,1)$, $(2,3)$, $(4,5)$ and $(6,7)$, is $\gamma^8$, the total inversion, which is exact as well. In a world with one time the direction of time cannot be reversed by a continuous rotation; with two or more times it can. In signature (4,4) the time orientation of the slicing $x_4=\text{const}$ can therefore be reversed continuously, and the sign of the **classical** charge $Q$ refers to a chosen slicing.

After quantization of the anticommuting field this changes. Both maps reverse $x_4$, so they are of antiunitary type: for $M=\gamma^4\gamma^5$ the anticommutator gives $MBM^\dagger=\sigma_R\varepsilon\,r_4\,B=-B$, and the same holds for $M=\gamma^8$ ($R=\{0,\dots,7\}$, $\varepsilon=(-1)^8=1$, $s_R=4$, $r_4=-1$). An antiunitary operator $A$ with $A\Psi A^{-1}=M\Psi(Rx)$ complex-conjugates the numbers $B_{cd}$ in $J^4=\sum_{c,d}\Psi^\dagger_cB_{cd}\Psi_d$, so

$$
AJ^4(x)A^{-1}=\Psi^\dagger M^TB^\ast M\Psi\,(Rx)=+J^4(Rx),
$$

because $B^\ast=-B$ and $M^TBM=M^{-1}BM=\sigma_R\varepsilon\,r_4\,B=-B$ (Lemma B, as in the computation of $MBM^{-1}$ above). The quantum charge is preserved, as it is under time reversal in ordinary quantum mechanics (derived; the committed Python checker records $M^TB^\ast M=+B$ for both maps in the entry `facts.quantisedGrassmannField` of its measurement for `MA_M2_spin0ContainsChargeReversingTimeRotation`, an entry that the committed report, written by an earlier version of the checker, does not contain). These maps reverse $x_4$; they are not C or CP in Sakharov's sense, and the scorecard of Section 17.15 does not use them.

**How M2 was verified.** The Wolfram verifier finds the intertwiner spaces of Lemma A one-dimensional each (bases $1$, $\gamma^8$, $C$, $\gamma^8C$); the 256 monomials realise the 256 sign patterns bijectively; the statistics sign $s$ is computed with an exact random matrix $Y$; for all 1024 maps per statistics the Lagrangian density computed from the transformed field jets (commuting symbols, respectively the Grassmann algebra) equals $\kappa\mathcal L_{\sigma\kappa m,\kappa\lambda}$ as the rule predicts, with the eight current signs, without a single mismatch; the frame form in the curved field G1 is checked for 31 frame reflections for both statistics; and all 256 exact maps of the anticommuting field preserve the canonical structure. The independent Python checker verifies the solution spaces of Lemma A, the internal maps on curved jets in G_A, named reflections, three generic non-axis unit vectors, reflections in the curved field G_B, the rotation $\exp(\pi S^{45})$ and the total inversion, and the complete character table of the 1024 maps per statistics (4 classes of 256, 256 exact symmetries, 64 exact charge-reversing symmetries without $x_4$ reversal). The two implementations agree on all 2048 classification rows and on all 22 items of the C, P, CP, T and CPT summary (check `MA_agreesWithWolfram`). The Python checker of the same commit adds the check `MA_M2_cpScopeInCurvedFields` described above, which the committed Python report does not yet contain (Section 17.17). Lemma D and the remark after it are derived in this chapter and are not separate machine checks. The main check names are

```
wolfram-matter-antimatter-report.json
  MA_M2_conjugationIntertwiners  MA_M2_signPatternClassification  MA_M2_statisticsSign
  MA_M2_lagrangianFlatCommuting_all  MA_M2_lagrangianFlatGrassmann_all
  MA_M2_frameLevelG1_commuting  MA_M2_frameLevelG1_grassmann
  MA_M2_symmetrySummaryAndChargeReversal  MA_M2_canonicalStructure
python-matter-antimatter-report.json
  MA_M2_chargeConjugationSolutionSpaces  MA_M2_spin0ContainsChargeReversingTimeRotation
  MA_M2_discreteGroupCharacterTable  MA_M2_C_and_CP_status
  MA_M2_canonicalStructureOfExactGrassmannSymmetries  MA_M2
checker of this commit only (not in the committed Python report)
  MA_M2_cpScopeInCurvedFields
```

### 17.12 Theorem M3: which charge-violating terms the symmetry allows

Sakharov's first condition needs an interaction that changes the charge. The simplest candidates are **Majorana-type** terms, built with $\Psi^T$ in place of $\Psi^\dagger$, such as $\Psi^TM\Psi$ with a constant matrix $M$ (named after Ettore Majorana, who used such terms for neutral fermions). Under $\Psi\to e^{i\alpha}\Psi$ both factors are multiplied by $e^{i\alpha}$, so the term is multiplied by $e^{2i\alpha}$: it has **U(1) charge 2** and violates the symmetry of Theorem M1. Which of them does the local Lorentz symmetry of the theory allow? Theorem M3 answers this. It is a classification of what the symmetry permits; it is not a claim that any such term is present in the theory, or natural.

**The condition for invariance.** Under a spin transformation $\Psi\to R\Psi$ (Section 2.14) the term becomes $\Psi^TR^TMR\Psi$. For $R=\exp(\theta S^{ab})=1+\theta S^{ab}+O(\theta^2)$,

$$
R^TMR=M+\theta\bigl((S^{ab})^TM+MS^{ab}\bigr)+O(\theta^2).
$$

So invariance under all of $\mathrm{Spin}_0(4,4)$ requires $(S^{ab})^TM+MS^{ab}=0$ for all 28 generators. Conversely this condition suffices: with $R(\theta)=\exp(\theta S)$, $dR/d\theta=SR=RS$, so $\frac d{d\theta}\bigl(R^TMR\bigr)=R^T\bigl(S^TM+MS\bigr)R=0$, hence $R^TMR=M$ for every $\theta$, and for every product of such exponentials.

**Theorem M3.**

1. (invariant forms) The constant matrices $M$ with $(S^{ab})^TM+MS^{ab}=0$ for all 28 generators are exactly $M=C(\alpha P_-+\beta P_+)$ with complex numbers $\alpha,\beta$, where $P_\mp=\tfrac12(1\mp\gamma^8)$. This space has dimension 2, all its elements are symmetric, and it contains no nonzero antisymmetric matrix.
2. (the full group) The elements of $\mathrm{Spin}(4,4)$ of spinor norm $-1$ (Section 2.14), such as $g=\gamma^a\gamma^b$ with $a$ space-like and $b$ time-like, act by $g^T(CP_\pm)g=-CP_\pm$. No nonzero form is strictly invariant under the full $\mathrm{Spin}(4,4)$; both basis forms carry the spinor-norm character.
3. (Pin characters) For every unit vector $u=u_a\gamma^a$ with $u^2=n(u)=\pm1$: $u^TCu=-n(u)\,C$ and $u^T(C\gamma^8)u=+n(u)\,C\gamma^8$, while $u^T(CP_\pm)u=-n(u)\,CP_\mp$. So $C$ carries the character $-n(u)$ (the character of $\bar\Psi\Psi$), $C\gamma^8$ the character $+n(u)$, and the chiral forms $CP_\pm$ are $\mathrm{Spin}_0$-invariant but not Pin-covariant, because $u$ exchanges the two chiralities.
4. (derivative terms) The invariant derivative bilinears $\Psi^TM\gamma^a\partial_a\Psi$ have $M$ in the same two-dimensional space. $M\gamma^a$ is symmetric for every $a$ exactly when $M\propto C\gamma^8$, and antisymmetric for every $a$ exactly when $M\propto C$.
5. (what survives) For **anticommuting** components every invariant mass-type term $\Psi^TM\Psi$ vanishes identically: **no Majorana mass term exists**. The derivative term $\sqrt{|g|}\,\Psi^TC\gamma^\mu D_\mu\Psi$ is a total divergence, while $\sqrt{|g|}\,\Psi^TC\gamma^8\gamma^\mu D_\mu\Psi$ survives, with the flat-space Euler–Lagrange expression $2C\gamma^8\gamma^a\partial_a\Psi$. For **commuting** components the two chiral mass terms $\Psi^TCP_\pm\Psi$ survive (equivalently $\Psi^TC\Psi$ and $\Psi^TC\gamma^8\Psi$), and so does the derivative term $\sqrt{|g|}\,\Psi^TC\gamma^\mu D_\mu\Psi$, which has the form of the notebook's Lagrangian Lg[]; $\sqrt{|g|}\,\Psi^TC\gamma^8\gamma^\mu D_\mu\Psi$ is then a total divergence.
6. (charge) Every term of items 1 to 5 has U(1) charge 2, and none of them is contained in $\mathcal L$.

*Proof of item 1.* From $(CS^{ab})^T=-CS^{ab}$ (Section 2.11) and $C^T=C$ we get $(S^{ab})^TC=-CS^{ab}$, that is $(S^{ab})^T=-CS^{ab}C^{-1}$. The condition becomes $-CS^{ab}C^{-1}M+MS^{ab}=0$; multiplying by $C^{-1}$ from the left, $S^{ab}(C^{-1}M)=(C^{-1}M)S^{ab}$: the matrix $C^{-1}M$ commutes with all 28 generators. By Theorem 2.12 and the remark after it (it holds for $\mathrm{Spin}_0(4,4)$), this commutant is spanned by $P_-$ and $P_+$. So $M=C(\alpha P_-+\beta P_+)$. The chirality $\gamma^8=\mathrm{diag}(-I_8,I_8)$ is symmetric and commutes with $C$, so $(CP_\pm)^T=P_\pm^TC^T=P_\pm C=CP_\pm$: both basis matrices are symmetric, and so is every combination. $\square$

*Proof of item 3.* From $(\gamma^a)^TC=-C\gamma^a$ and linearity, $u^TC=-Cu$, so $u^TCu=-Cu\,u=-n(u)\,C$. Since $u$ anticommutes with $\gamma^8$: $u^TC\gamma^8u=-Cu\gamma^8u=C\gamma^8u\,u=n(u)\,C\gamma^8$. Since $uP_\pm=P_\mp u$: $u^TCP_\pm u=-CuP_\pm u=-CP_\mp u\,u=-n(u)\,CP_\mp$. $\square$

*Proof of item 2.* Apply item 3 twice with $u=\gamma^a$ ($n=+1$) and $u=\gamma^b$ ($n=-1$): $(\gamma^a)^T(CP_\pm)\gamma^a=-n(\gamma^a)\,CP_\mp=-CP_\mp$, and then $g^T(CP_\pm)g=(\gamma^b)^T(-CP_\mp)\gamma^b=-\bigl(-n(\gamma^b)\bigr)CP_\pm=-CP_\pm$. A form $\alpha CP_-+\beta CP_+$ is therefore mapped to its negative by $g$, and it is invariant only if it is zero. $\square$

*Proof of item 4.* For $M=C\gamma^8$: $(C\gamma^8\gamma^a)^T=(\gamma^a)^T\gamma^8C=(\gamma^a)^TC\gamma^8=-C\gamma^a\gamma^8=C\gamma^8\gamma^a$, symmetric. For $M=C$: $(C\gamma^a)^T=-C\gamma^a$, antisymmetric. A combination $\alpha CP_-+\beta CP_+$ with $\beta=-\alpha$ is proportional to $C\gamma^8$, with $\beta=\alpha$ proportional to $C$, and otherwise has neither property. That invariance puts $M$ into this space follows as for item 1, because a global spin transformation $R$ with its vector matrix $\Lambda$ ($R^{-1}\gamma^aR=\Lambda^a{}_b\gamma^b$) turns $\Psi^TM\gamma^a\partial_a\Psi$ into $\Psi^TR^TMR\,\gamma^b\partial_b\Psi$; the verifiers find the same two-dimensional space for the derivative forms (check `MA_M3_kineticInvariantForms`). $\square$

*Proof of item 5.* For anticommuting components $\Psi_i\Psi_j=-\Psi_j\Psi_i$, so $\Psi^TM\Psi=\Psi^TM_A\Psi$ with the antisymmetric part $M_A=\tfrac12(M-M^T)$ (Lemma 5.4). The map $M\mapsto(S^{ab})^TM+MS^{ab}$ sends symmetric matrices to symmetric ones and antisymmetric ones to antisymmetric ones (transpose it). Moreover a bilinear $\Psi^TX\Psi=2\sum_{i<j}X_{ij}\Psi_i\Psi_j$ with antisymmetric $X$ vanishes only if $X=0$, because the monomials $\Psi_i\Psi_j$ ($i<j$) are independent. So the invariance of $\Psi^TM_A\Psi$ is exactly the condition of item 1 for $M_A$, and item 1 makes $M_A$ symmetric and antisymmetric at once: $M_A=0$, and every invariant mass-type term vanishes. For derivative terms: if $A$ is a constant antisymmetric matrix, Lemma 5.5 gives $\Psi^TA\,\partial_a\Psi=\tfrac12\partial_a(\Psi^TA\Psi)$, a total derivative, which is the case $A=C\gamma^a$; in curved space, with $\sqrt{|g|}$ and the canonical connection, this is the theorem of Section 5.13 that Lg[] is a pure divergence for a Grassmann field. If instead $X$ is constant and symmetric, the term $\Psi^TX\partial_a\Psi$ has the left derivatives $\partial_L/\partial\Psi_c=(X\partial_a\Psi)_c$ and $\partial_L/\partial(\partial_a\Psi_c)=-(X\Psi)_c$ (move $\partial_a\Psi_c$ to the left past the odd $\Psi_i$), so its Euler–Lagrange expression is $(X\partial_a\Psi)_c+\partial_a(X\Psi)_c=2(X\partial_a\Psi)_c\ne0$; this is the case $X=C\gamma^8\gamma^a$. For commuting components only the symmetric part of a matrix counts in $\Psi^TM\Psi$ (Section 1.8), $CP_\pm$ are symmetric and nonzero, and the roles of symmetric and antisymmetric in the derivative terms are exchanged. $\square$

*Proof of item 6.* $\Psi^T\to e^{i\alpha}\Psi^T$ and $\Psi\to e^{i\alpha}\Psi$, so every term $\Psi^TX\Psi$ is multiplied by $e^{2i\alpha}$; $\mathcal L$ contains only bilinears $\Psi^\dagger\cdots\Psi$ and functions of $S$ (Section 17.8). $\square$

**Worked example.** In the notebook's basis $C=\mathrm{diag}(-\sigma,\sigma)$ with $\sigma=\begin{pmatrix}0&I_4\\ I_4&0\end{pmatrix}$ (Section 2.9) and $P_-=\mathrm{diag}(I_8,0)$, so $CP_-=\mathrm{diag}(-\sigma,0)$: its only nonzero entries are $-1$ in the places $(0,4),(1,5),(2,6),(3,7)$ and their mirror images. For commuting components

$$
\Psi^TCP_-\Psi=-2\bigl(\Psi_0\Psi_4+\Psi_1\Psi_5+\Psi_2\Psi_6+\Psi_3\Psi_7\bigr).
$$

With $\Psi_0=1$, $\Psi_4=2$ and all other components 0 this is $-4$; after the phase $\Psi\to e^{i\alpha}\Psi$ it is $-4e^{2i\alpha}$, which for $\alpha=\pi/2$ is $+4$. A term $g\,\Psi^TCP_-\Psi$ plus its complex conjugate in the Lagrangian would therefore break the U(1) of Theorem M1 down to the two phases with $e^{2i\alpha}=1$, namely $\Psi\to\pm\Psi$. For anticommuting components the same expression is $-(\Psi_0\Psi_4+\Psi_4\Psi_0)-\dots=0$: the Majorana mass term does not exist.

**Pin characters of the Majorana-type terms.** Under $\Psi\to u\Psi$ with $u=\gamma^b$ ($n=\eta_{bb}$), $\Psi^TC\Psi$ picks up the factor $-n$ and $\Psi^TC\gamma^8\Psi$ the factor $+n$ (item 3); for the derivative terms the factor also depends on the lift of the reflection (the twisted and untwisted lifts of Section 2.14), as recorded in check `MA_M3_pinCharactersMajoranaTerms`.

**The notebook's Lagrangian.** Lg[] (Section 5.12) uses Transpose[Psi16], not ConjugateTranspose: its kinetic matrix $\sigma_{16}\,\mathrm T16^a=C\gamma^a$ and its mass matrix $\sigma_{16}=C$ belong to the family of item 1, with the Pin character $-n(u)$. It is therefore of Majorana type. For a complex commuting field it has U(1) charge 2; for a real commuting field it is non-trivial; for a Grassmann field it is a total derivative with a vanishing mass term (Chapter 5). dirac16complex00 uses the charge-0 Lagrangian $\mathcal L$ of Section 17.8 instead (Chapter 6).

**Quartic examples (not a classification).** For anticommuting components invariant charge-violating terms of higher order do exist. The matrices $C\gamma^a\gamma^b$ with $a\ne b$ are antisymmetric (transpose and use $(\gamma^a)^TC=-C\gamma^a$ twice), so the bilinears $T^{ab}=\Psi^TC\gamma^a\gamma^b\Psi$ do not vanish for Grassmann components, and they transform as an antisymmetric tensor. Their full contractions are $\mathrm{Spin}_0$-invariant:

$$
\begin{aligned}
&Q_4=\sum_{a<b}\eta_{aa}\eta_{bb}\,\bigl(\Psi^TC\gamma^a\gamma^b\Psi\bigr)^2 &&\text{(40 monomials, charge 4)},\\
&Q_2=\sum_{a<b}\eta_{aa}\eta_{bb}\,\bigl(\Psi^TC\gamma^a\gamma^b\Psi\bigr)\bigl(\Psi^\dagger C\gamma^a\gamma^b\Psi\bigr) &&\text{(160 monomials, charge 2)}.
\end{aligned}
$$

These are examples only: higher-order charge-violating terms are not classified (OPEN), and nothing here says that such a term is present, natural, or sufficient for generating an asymmetry.

**How M3 was verified.** Wolfram: the null space of the 28 conditions has dimension 2 with basis $CP_-$, $CP_+$, a symmetric subspace of dimension 2 and an antisymmetric subspace of dimension 0; the character table over the four characters has the dimensions 0, 1, 1, 0 (trivial, $-n$, $+n$, determinant); all four mass-type forms vanish for Grassmann components (a control with an antisymmetric matrix has 8 nonzero monomials), while for commuting components $CP_-$, $CP_+$, $C$ and $C\gamma^8$ give forms of rank 8, 8, 16 and 16; the kinetic Euler–Lagrange expressions, the charge 2, the Pin characters, the identification of Lg[] and $Q_4$. Python, independently: the null space as the exact integer basis $\tfrac12(C\gamma^8-C)$, $\tfrac12(C\gamma^8+C)$; the survival table with monomial counts ($\Psi^TC\Psi$ and $\Psi^TC\gamma^8\Psi$ have 0 monomials for Grassmann and 8 each for commuting components, while the charge-0 bilinears $\Psi^\dagger C\Psi$ and $\Psi^\dagger C\gamma^8\Psi$ have 16); the derivative terms in the curved field G_A; $Q_4$ with 40 and $Q_2$ with 160 monomials, and the agreement of $Q_4$ with 8 times the chiral form of the Wolfram package. The main check names are

```
wolfram-matter-antimatter-report.json
  MA_M3_spinInvariantForms  MA_M3_pinCharacterForms  MA_M3_kineticInvariantForms
  MA_M3_grassmannSurvival  MA_M3_commutingSurvival  MA_M3_u1Charge
  MA_M3_notebookLgIsMajoranaType  MA_M3_extraGrassmannQuarticCharge4
python-matter-antimatter-report.json
  MA_M3_invariantFormsSpan_C_Cgamma8  MA_M3_allInvariantFormsSymmetric
  MA_M3_massTypeSurvivalAndCharge  MA_M3_derivativeTypeSurvivalCurved
  MA_M3_quarticChargeViolatingExamplesGrassmann  MA_M3
```

### 17.13 Theorem M4: the chirality pair of universes

**Theorem M4 (field level; the pairing theorem T1 of Stage 5).** For every vielbein, every $m$ and $\lambda$, both statistics and every configuration $\Psi$ (solution or not), with $\Psi_-:=\gamma^8\Psi$:

$$
\begin{aligned}
&\bar\Psi_-=\bar\Psi\gamma^8,\qquad S[\Psi_-]=S[\Psi],\qquad K[\Psi_-]=-K[\Psi],\qquad j^\mu[\Psi_-]=-j^\mu[\Psi],\\
&\mathcal L_{m,\lambda}[\gamma^8\Psi]=-\mathcal L_{-m,-\lambda}[\Psi],\qquad E_{-m,-\lambda}[\gamma^8\Psi]=-\gamma^8E_{m,\lambda}[\Psi],\\
&T_{\mu\nu}[\gamma^8\Psi;-m,-\lambda]=-T_{\mu\nu}[\Psi;m,\lambda].
\end{aligned}
$$

Hence $\Psi$ solves the field equations with $(m,\lambda)$ if and only if $\gamma^8\Psi$ solves them with $(-m,-\lambda)$.

*Proof.* $\gamma^8$ is Hermitian, $(\gamma^8)^2=1$, it anticommutes with every $\gamma^a$, and it commutes with $C$ and with every $S^{ab}$ (both are even, Section 2.10), hence with every $\Omega_\mu$ and with $D_\mu$. Therefore $\bar\Psi_-=\Psi^\dagger\gamma^8C=\Psi^\dagger C\gamma^8=\bar\Psi\gamma^8$, and a bilinear $\bar\Psi X\Psi$ goes to $\bar\Psi\gamma^8X\gamma^8\Psi$. This is $-\bar\Psi X\Psi$ when $X$ contains one gamma matrix (the current, the kinetic term, the kinetic part of $T_{\mu\nu}$) and $+\bar\Psi X\Psi$ for $X=1$ (the scalar $S$). Consequently

$$
\mathcal L_{m,\lambda}[\gamma^8\Psi]=\sqrt{|g|}\bigl[-K-mS-\tfrac\lambda2S^2\bigr]=-\sqrt{|g|}\Bigl[K-(-m)S-\tfrac{(-\lambda)}2S^2\Bigr]=-\mathcal L_{-m,-\lambda}[\Psi].
$$

For the field equation, $\gamma^\mu D_\mu(\gamma^8\Psi)=-\gamma^8\gamma^\mu D_\mu\Psi$ and $(-m-\lambda S)\gamma^8\Psi=-\gamma^8(m+\lambda S)\Psi$, so $E_{-m,-\lambda}[\gamma^8\Psi]=-\gamma^8\gamma^\mu D_\mu\Psi+\gamma^8(m+\lambda S)\Psi=-\gamma^8E_{m,\lambda}[\Psi]$. The energy–momentum tensor (Chapter 7) is $T_{\mu\nu}=-\tfrac14[\text{kinetic bilinears}]+g_{\mu\nu}\mathcal L_s$: the kinetic bilinears change sign, and $\mathcal L_s[\gamma^8\Psi;-m,-\lambda]=-\mathcal L_s[\Psi;m,\lambda]$ is the Lagrangian identity with $(m,\lambda)$ replaced by $(-m,-\lambda)$. The map is linear and keeps every $\Psi^\dagger$ to the left of every $\Psi$, so the proof holds for both statistics. $\square$

**Why $\lambda$ must change sign.** The potential $U=\tfrac\lambda2S^2$ is even in $S$, and $S$ does not change, so at a fixed $\lambda$ the identity fails: $\mathcal L_{m,\lambda}[\gamma^8\Psi]+\mathcal L_{-m,\lambda}[\Psi]=\sqrt{|g|}\bigl[-K-mS-\tfrac\lambda2S^2+K+mS-\tfrac\lambda2S^2\bigr]=-\lambda\sqrt{|g|}\,S^2\ne0$ (the erratum E2 of the project contract).

**Corollary M4.1 (the pair).** Let $\Psi_+$ carry $(m,\lambda)$ and $\Psi_-=\gamma^8\Psi_+$ carry $(-m,-\lambda)$ in the same gravitational field. Then at every point and every $x_4$, in particular at $x_4=0$,

$$
j^\mu_++j^\mu_-=0,\qquad Q_++Q_-=0,\qquad T^{\mathrm{pair}}_{\mu\nu}=T_{\mu\nu}[\Psi_+;m,\lambda]+T_{\mu\nu}[\Psi_-;-m,-\lambda]=0 .
$$

The pair carries no net charge and no net energy, momentum or stress, so the Einstein (or Einstein–Lovelock) equations with the pair as their source are the source-free equations. The energies cancel because the classical energy density of the member of mass $-M$ is minus that of the member of mass $+M$. This is a statement about conservation laws and constraints; it is not a computed creation rate or amplitude (Chapter 16).

**Worked example.** The rest state $u_+$ of Section 17.9 has $Bu_+=u_+$. Its image $v=\gamma^8u_+$ flips the signs of the upper eight components: $v=\tfrac12(-e_0+e_4-i\,e_9-i\,e_{13})$. With the rows of $B$ (Section 2.9: $(Bw)_0=iw_9$, $(Bw)_4=-iw_{13}$, $(Bw)_9=-iw_0$, $(Bw)_{13}=iw_4$) one finds $(Bv)_0=i(-\tfrac i2)=\tfrac12=-v_0$, and likewise for the other three places, so $Bv=-v$ and $v^\dagger Bv=-1$: the charge densities of $\Psi_+=u_+e^{-imx_4}$ and of its partner add to $1+(-1)=0$. The partner solves the field equation with the mass $-m$: $h_0(-m)=im\gamma^4=\gamma^8(-im\gamma^4)\gamma^8$, so $h_0(-m)v=\gamma^8h_0(m)u_+=m\,v$.

**One-particle (Krein) level.** In the good sector in flat space, with no momenta along $x_5,x_6,x_7$, the mode Hamiltonian $h_k(m)=-im\gamma^4-\gamma^4\sum_{j\ne4}k_j\gamma^j$ is Hermitian, commutes with $B$ and satisfies $h_k(m)^2=(m^2+k^2)\,1$ (Sections 8.9 and 8.10). Since $\gamma^8\gamma^4\gamma^8=-\gamma^4$ and $\gamma^8\gamma^4\gamma^j\gamma^8=\gamma^4\gamma^j$ (two anticommutations), and $B$ is $-i$ times a product of five gammas,

$$
\gamma^8h_k(m)\gamma^8=h_k(-m),\qquad \gamma^8B\gamma^8=-B .
$$

So $\gamma^8$ maps the positive-energy (negative-energy) eigenspace of $h_k(m)$ onto the positive-energy (negative-energy) eigenspace of $h_k(-m)$ with the same energy: if $h_k(m)u=Eu$, then $h_k(-m)\gamma^8u=\gamma^8h_k(m)u=E\gamma^8u$. It preserves the Hilbert norm $u^\dagger u$ ($\gamma^8$ is orthogonal) and reverses the Krein norm $u^\dagger Bu$. At rest the $B$-form on each positive-energy space has signature (4,4) (Section 8.8), and the Gram matrix of the image is minus the original one.

Which energy and charge an image mode carries depends on the canonical structure given to the image field. With the expectation-value rule of Section 8.12, $\langle\Psi^\dagger X\Psi\rangle=u^\dagger BXu$ for a Hilbert-normalised positive-energy mode $u$, the energy is $X=Bh$, the charge $X=B$ and the scalar density $X=C$. For the image field $\Psi_-=\gamma^8\Psi$ the canonical anticommutator is $\gamma^8B\gamma^8=-B$, and the rule reads $u_-^\dagger(-B)Xu_-$ with $u_-=\gamma^8u$. For an independently quantised theory of mass $-m$ with its own positive structure the rule is $u_-^\dagger BXu_-$. The table gives $(E,Q,S)$ per quantum for three exact positive-energy modes $u$ with mass $m$ and momentum $k=(k_0,k_1,k_2,k_3)$ (measurement `M4.kreinModeFacts` of `python-matter-antimatter-report.json`):

| $m$, $k$ | universe of mass $+m$ | image field, metric $-B$ | independent, metric $+B$ |
| --- | --- | --- | --- |
| $1$, $(1,1,2,3)$ | $(4,1,1/4)$ | $(-4,-1,1/4)$ | $(4,1,-1/4)$ |
| $3$, $(1,1,1,2)$ | $(4,1,3/4)$ | $(-4,-1,3/4)$ | $(4,1,-3/4)$ |
| $3/5$, $(4/5,0,0,0)$ | $(1,1,3/5)$ | $(-1,-1,3/5)$ | $(1,1,-3/5)$ |

In the first column $E=\sqrt{m^2+k^2}$ (for example $\sqrt{1+1+1+4+9}=4$), $Q=u^\dagger BBu=u^\dagger u=1$ and $S=m/E$. The last value is the flat-space case $M_{\mathrm{eff}}=m$ of the result $s=M_{\mathrm{eff}}/E$ of Section 11.4, and it takes two lines: $BC=-i\gamma^4$ (Section 2.12), so $S=u^\dagger BCu=u^\dagger Zu$ with $Z=-i\gamma^4$; and $h_k(m)=mZ+X$ with $X=-\gamma^4\sum_jk_j\gamma^j$, where $Z^2=1$ and $ZX+XZ=0$ (each $\gamma^4\gamma^j$ with $j\ne4$ anticommutes with $\gamma^4$), so $Zh+hZ=2m$. Sandwiching this between $u^\dagger$ and $u$ with $hu=Eu$, $u^\dagger h=Eu^\dagger$ and $u^\dagger u=1$ gives $2E\,u^\dagger Zu=2m$, that is $S=m/E$. The general pattern follows from the two matrix identities. For the image field: $u_-^\dagger(-B)(Bh(-m))u_-=-u^\dagger\gamma^8h(-m)\gamma^8u=-u^\dagger h(m)u=-E$, $u_-^\dagger(-B)Bu_-=-u^\dagger u=-1$ and $u_-^\dagger(-B)Cu_-=-u^\dagger(\gamma^8B\gamma^8)(\gamma^8C\gamma^8)u=u^\dagger BCu=S$: so $(E,Q,S)\to(-E,-Q,S)$. For the independent field: $u_-^\dagger h(-m)u_-=E$, $u_-^\dagger u_-=1$ and $u_-^\dagger BCu_-=-S$: so $(E,Q,S)\to(E,Q,-S)$.

**Fock level (from Stage 5; PROVISIONAL).** The Stage-5 Wolfram pairing report has all 141 of its checks true, and its exact Fock-level result (the checks `PAIR_T1krein_*`, in a Fock model of four rest modes with $m=1$, the sea formed by the two negative-energy modes, and normal ordering as the subtraction of the sea value; key `T1krein` of `pairing-theory.json`) is as follows.

- The image field $\Psi_-=\gamma^8\Psi$, on the same Fock space and in the same state, has the anticommutator $-B$ on its modes; the operator identities $H[\Psi_-;-m]=-H[\Psi;m]$, $Q[\Psi_-]=-Q[\Psi]$ and $S[\Psi_-]=S[\Psi]$ hold, normal ordering commutes with the map, and $:\!T_{\mu\nu}[\gamma^8\Psi;-m,-\lambda]\!:\ =-:\!T_{\mu\nu}[\Psi;m,\lambda]\!:$ as operators. Stage 5 describes the image as a universe with the Krein metric $-B$, energy $-|\epsilon|$ and charge $-1$ per quantum; these numbers are the expectation values of the formulas of $\mathcal L_{-m,-\lambda}$, not the image field's own energy and charge (the caveat below).
- An independently quantised theory of mass $-m$ with the positive ($J=B$) structure has the modes $w_n=\gamma^8u_n$ (same energy $\epsilon$, Krein sign $-\beta_n$). A quantum in $w_n$ has energy $+|\epsilon|$, charge $+1$ and the opposite scalar density; with the same mode occupations such a universe has, in this free Fock model, the same energy–momentum and the same charge as the universe of mass $+m$, so the pair totals add instead of cancelling (Stage 5 calls this the T2-type pairing; its Kohn–Sham form is the mirror map of Section 13.14, treated in Chapter 15). For $\lambda\ne0$ the energies do not simply add: with the parameters $(-m,-\lambda)$ the interaction energy of the $-M$ universe is $-\tfrac\lambda2S'^2$ with $S'=-S_+$, that is $-\tfrac\lambda2S_+^2$, the opposite of that of the $+M$ universe (entry `kreinLevelCaveat` of the Wolfram matter-antimatter report). Only the kinetic and mass energies add.

The Stage-5 files carry no finality flag: the Wolfram matter-antimatter report records the status of these statements as provisional until the Stage-5 gate has passed (measurement `M4_kreinLevelStatus` of `wolfram-matter-antimatter-report.json`).

**How particles and antiparticles map** (derived from these operator identities, as in the matter-antimatter document). In the universe of mass $+m$ a particle has $(E,Q)=(+|\epsilon|,+1)$ and an antiparticle, a hole in the sea, has $(+|\epsilon|,-1)$. The image field describes the same particles and antiparticles, with the same energies and charges when these are measured with its own generators $-H[\Psi_-;-m]$ and $-Q[\Psi_-]$; only the formulas of $\mathcal L_{-m,-\lambda}$, evaluated on the same states, give $(-|\epsilon|,-1)$ and $(-|\epsilon|,+1)$. In the independently quantised $-M$ universe, particles and antiparticles have the same energies and charges as in the $+M$ universe and the opposite scalar density. For the modes of positive and negative Krein norm: a mode $u_n$ with Krein sign $\beta_n=u_n^\dagger Bu_n$ goes to $w_n=\gamma^8u_n$ with $w_n^\dagger Bw_n=-\beta_n$. Measured with the image field's own metric $-B$ the sign is $\beta_n$ again; measured with $+B$ (independent quantization) every positive-norm mode becomes a negative-norm mode and conversely.

So the cancellation of Corollary M4.1 does not carry over to the quantum level as a cancellation between two universes. If the $-M$ member is the image field with the Krein metric $-B$, the operator totals vanish, but only as identities of the form $X+(-X)=0$ within one quantum system (the caveat that follows). If the $-M$ universe is an independently quantised field with positive energies, the charges would cancel only by an additional assumption about the state of the $-M$ universe, and the energies would not cancel (the kinetic and mass energies add, and for $\lambda\ne0$ the interaction energies have opposite signs).

**A caveat on what the operator cancellation means.** The committed Wolfram matter-antimatter report records a further point (measurement `M5_implication`, entry `kreinLevelCaveat`, and the matrix checks of `M4_kreinOneParticle`). In the image-field reading, $\Psi_-=\gamma^8\Psi_+$ is built from the same operators, on the same Fock space and in the same state, as $\Psi_+$. The identities $Q_++Q[\Psi_-]=0$ and $H_++H[\Psi_-;-m]=0$ are therefore of the form $X+(-X)=0$ and hold in every state; they are not a compensation by a second, independent universe. Relative to its own canonical structure (anticommutator $-B$, Lagrangian $-\mathcal L_{-m,-\lambda}$), the image field's generator of time evolution is $-H[\Psi_-;-m]=+H_+$ and its generator of phases is $-Q[\Psi_-]=+Q_+$: it is the same quantum system as $\Psi_+$, with the same energy and charge, and the values $-|\epsilon|$ and $-1$ per quantum are expectation values of the $\mathcal L_{-m,-\lambda}$ formulas rather than of that field's own Hamiltonian and charge. In the independent reading the kinetic and mass energies add, the charges cancel only by an additional assumption on the state of the $-M$ universe, and for $\lambda\ne0$ its interaction energy has the opposite sign. The committed report sums this up in one sentence: at the quantum level no reading of H1 gives a cancellation between two independent, consistently quantised universes. **Of the two readings examined in the repository, neither describes two independent, consistently quantised universes whose charges and energies cancel.** Whether any quantum description of a physical universe of mass $-M$ gives the classical cancellation of Corollary M4.1 is **OPEN**.

**How M4 was verified.** Wolfram: the matrix facts (the current matrices are odd under $\gamma^8$, the mass matrix is even, $\bar\Psi\to\bar\Psi\gamma^8$, $B\to-B$); the current flip in G1 for Grassmann components at three points; for commuting components at the three G1 points the field jets of $T^{\mathrm{pair}}_{\mu\nu}$ and of the pair current vanish while the individual ones do not, and the image of an exact solution solves the $(-m,-\lambda)$ equations; for Grassmann components all 64 components of $T^{\mathrm{pair}}_{\mu\nu}$ vanish at the point p1, while each member has 64 nonzero components; and the one-particle facts above. Python, independently: the $\gamma^8$ matrix facts, including $(\gamma^8)^TC\gamma^a\gamma^8=-C\gamma^a$ and the commutation with $\Omega_\mu$ in G_A; in G_A for both statistics the current flip, $S$ invariant, $K\to-K$, the Lagrangian identity, the Euler–Lagrange pairing and the pairing of all 36 independent components of $T_{\mu\nu}$, as exact polynomial identities; the three Krein mode samples of the table; and the citation of the Stage-5 report with all twelve `PAIR_T1krein` checks true. The Python checker of the same commit adds the check `MA_M4_imageFieldFockModel`, which the committed Python report does not yet contain (Section 17.17): in an exact Fock model of four modes of the good sector it builds the image field as a genuine operator on the same Fock space and verifies the caveat above, namely that the image field's own generators of $x_4$-evolution and of phases are $-H[\Psi_-;-m]=+H_+$ and $-Q[\Psi_-]=+Q_+$, that $Q_++Q[\Psi_-]=0$ in every Fock state, and that an independently quantised $-m$ field with the same occupations has $H'=H_+$, $Q'=Q_+$ and $S'=-S_+$. The main check names are

```
wolfram-matter-antimatter-report.json
  MA_M4_currentFlipMatrix  MA_M4_currentFlipG1_grassmann
  MA_M4_pairEMTAndCurrentG1_commuting  MA_M4_pairEMTG1_grassmann  MA_M4_kreinOneParticle
python-matter-antimatter-report.json
  MA_M4_gamma8MatrixFacts  MA_M4_gamma8ChargeFlipCurved  MA_M4_gamma8EulerLagrangePairing
  MA_M4_gamma8EMTPairing  MA_M4_kreinModeFacts  MA_M4
checker of this commit only (not in the committed Python report)
  MA_M4_imageFieldFockModel
wolfram-pairing-report.json (Stage 5, cited)
  PAIR_T1krein_imageAnticommutatorMinusB  PAIR_T1krein_imageOperatorIdentities
  PAIR_T1krein_imageExpectationValues  PAIR_T1krein_independentCARPlusB
  PAIR_T1krein_independentExpectationValues  (and seven more PAIR_T1krein_ checks)
```

### 17.14 M5: the conditional scenario, stated as a hypothesis

The pair of Section 17.13 suggests a picture of the kind described in Section 17.7: our universe has an excess of charge, and a partner universe has the opposite excess. This section states that picture as precisely as possible, separates what is proved from what is assumed, and says what the picture does not do.

**The hypotheses.** The following three statements are **hypotheses**. None of them is derived anywhere in the repository.

- **H1 (HYPOTHESIS, not derived).** Our universe is one member of a chirality pair created together: two independent classical fields in the same gravitational field, $\Psi_+$ governed by the Lagrangian $\mathcal L_{m,\lambda}$ and $\Psi_-$ governed by the Lagrangian $+\mathcal L_{-m,-\lambda}$, in the correlated configuration $\Psi_-=\gamma^8\Psi_+$ (the correlation is part of the assumption). The sign in front of the second Lagrangian matters. The field equations of $+\mathcal L_{-m,-\lambda}$ and of $-\mathcal L_{-m,-\lambda}$ are the same, but the Noether current and the energy–momentum tensor are computed from the Lagrangian itself: with $+\mathcal L_{-m,-\lambda}$ the Noether current of $\Psi_-$ is $i\sqrt{|g|}\,j^\mu[\Psi_-]$ (Theorem M1 holds for every $m$ and $\lambda$), and its energy–momentum tensor is $T_{\mu\nu}[\Psi_-;-m,-\lambda]=-T_{\mu\nu}[\Psi_+;m,\lambda]$ (Theorem M4), so the second member has the classical energy $-E_+$. This is the form of H1 recorded in the committed Wolfram report (measurement `M5_implication`, entry `hypotheses`). At the quantum level H1 has no reading in which two independent, consistently quantised universes cancel each other's charge and energy (the caveat of Section 17.13). No creation process, rate or amplitude is computed anywhere in the repository.
- **H2 (HYPOTHESIS, not derived).** The creation assigns $Q_+=-Q_-\ne0$. Given H1, the relation $Q_-=-Q_+$ follows from M4; the content of H2 is $Q_+\ne0$, and nothing in the repository computes the value or the sign of $Q_+$.
- **H3 (HYPOTHESIS, not derivable within the theory).** The dirac16complex U(1) charge is identified with the baryon number $B$ (or with $B-L$). The theory contains no Standard-Model baryons, quarks or leptons, so this identification cannot be derived from it.

**Proposition M5 (classical level).** If H1, H2 and H3 hold, then $Q_+(x_4)+Q_-(x_4)=0$ at every $x_4$, each of $Q_+$ and $Q_-$ is separately conserved (when the boundary flux vanishes), and the baryon excess $B_+=Q_+\ne0$ seen in one member is compensated exactly by $B_-=-Q_+$ in the other. The pair also carries $T^{\mathrm{pair}}_{\mu\nu}=0$ for the classical bilinears: the member of mass $-M$ has the classical energy $-E_+$.

*Proof.* By M4, $\sqrt{|g|}\,j^{x_4}[\gamma^8\Psi_+]=-\sqrt{|g|}\,j^{x_4}[\Psi_+]$ at every point. By H1 the charge of $\Psi_-$ is the Noether charge of $+\mathcal L_{-m,-\lambda}$, which is built from the same current $j^\mu[\Psi_-]$, so $Q_-=-Q_+$ at every $x_4$, and $Q_++Q_-=0$. By M1 each charge is conserved, $dQ_\pm/dx_4=0$. By H3, $B_\pm=Q_\pm$, and by H2, $B_+\ne0$. The statement about $T^{\mathrm{pair}}_{\mu\nu}$ is Corollary M4.1, with $T_{\mu\nu}[\Psi_-;-m,-\lambda]$ the energy–momentum tensor of $+\mathcal L_{-m,-\lambda}$. $\square$

The Wolfram verifier checks the implication symbolically: $Q_++Q_-$ simplifies to 0, and $dQ_-/dx_4$ simplifies to 0 given $dQ_+/dx_4=0$ (check `MA_M5_implication`, with the ingredients computed in the checks of M1 and M4). The committed report records its status in these words: the classical-level implication is proved; the scenario itself is a hypothesis, not a result. The implication is elementary; its substance lies entirely in the hypotheses.

**At the quantum level (PROVISIONAL, and no cancellation between two universes).** Proposition M5 is not proved for the quantized fields. The operator identity $:\!T_{\mu\nu}[\gamma^8\Psi;-m,-\lambda]\!:\ =-:\!T_{\mu\nu}[\Psi;m,\lambda]\!:$ of Section 17.13 is cited from the Stage-5 pairing results, which are provisional until the Stage-5 gate has passed (measurement `M4_kreinLevelStatus`). And even taken as given, by the caveat of Section 17.13 it is an identity of the form $X+(-X)=0$ within one quantum system, not a compensation by a second universe; for an independently quantised $-M$ universe the energies do not cancel and the charges cancel only by an additional assumption.

**What M5 does not do.**

1. It does not produce an asymmetry. By M1, $Q_+$ is constant, so a nonzero $Q_+$ today is the same as a nonzero $Q_+$ at $x_4=0$: the asymmetry of our universe is an initial condition, which H2 puts in by hand.
2. It does not predict $\eta$. The observed $\eta\approx6\times10^{-10}$ is **not predicted**: nothing here computes the magnitude or the sign of $Q_+$, nor the photon content of the universe to which $\eta$ refers.
3. It does not satisfy Sakharov's conditions; it replaces them by a global symmetry of the pair together with an initial condition in each member.
4. It depends on the reading of H1. At the classical level the cancellation holds for two correlated classical fields, the second governed by $+\mathcal L_{-m,-\lambda}$, and the member of mass $-M$ then has the classical energy $-E_+$. At the quantum level, when the $-M$ member is the image field $\gamma^8\Psi_+$ with the Krein metric $-B$, the totals vanish only as an operator identity of the form $X+(-X)=0$ within one quantum system (the caveat of Section 17.13), not as a cancellation between two universes; if the $-M$ universe is instead quantised independently with its own positive structure, its quanta carry charge $+1$ and energy $+|\epsilon|$, its energies add to ours, and its charge cancels ours only under an additional assumption about its state. Which reading, if any, describes a physical universe of mass $-M$ is OPEN.
5. It does not relate the dirac16complex charge to the baryons of the Standard Model (H3), and it does not show that pairs are created (H1). Whether the big bang creates universes in pairs is the subject of Chapter 16; no creation process, rate or amplitude is derived anywhere in the repository.
6. It is not a statement about the observed world. The model lives in signature (4,4), with four time-like directions, while observed spacetime has one time (row L43 of the ledger of Chapter 0); applying the scenario to "our universe" is a further assumption, and nothing in it is fitted to or compared with data. Its quantum statements are formal: the canonical state space is a Krein space (Section 8.7), a positive Fock space exists only in the good sector (Section 8.10), the extra-time sector is ill-posed (Section 8.13), and dirac16complex00 is treated as a classical field.

### 17.15 M6: the Sakharov scorecard, and the answer

The three conditions of Section 17.5, applied to the theory as built:

| Sakharov condition | Status in the theory as built | What would have to be added |
| --- | --- | --- |
| 1. Violation of the conserved number (baryon number; here the charge $Q$) | Fails, by M1: $Q$ is exactly conserved in every gravitational field (when the boundary flux vanishes), for both statistics and every potential | A U(1)-violating interaction from the list of M3 (Section 17.16, item 1) |
| 2. C and CP violation | Fails, by M2: C is exact for the commuting field in every gravitational field, and CP is exact for the anticommuting field in flat space and in gravitational fields in which the reflection is an isometry; each reverses $Q$ and preserves $x_4$. A generic gravitational field breaks this CP, which does not help, because condition 1 fails | Terms that break all 64 exact charge-reversing symmetries without $x_4$ reversal (Section 17.16, item 2) |
| 3. Departure from thermal equilibrium | Not addressed by any computation; the Kohn–Sham states of Chapters 13 and 14 are equilibrium states at fixed $N$ | A non-equilibrium history and a computation of rates (Section 17.16, item 3) |

Since condition 1 fails exactly, no departure from equilibrium could create a net charge inside one universe of this theory. The computed checks behind the rows are

```
row 1  wolfram-matter-antimatter-report.json
         MA_M1_noetherIdentity_grassmann_G1  MA_M1_noetherIdentity_commuting_G1
       python-matter-antimatter-report.json
         MA_M1_noetherIdentity_<X>_<G>  (both statistics, both geometries)
row 2  wolfram-matter-antimatter-report.json
         MA_M2_symmetrySummaryAndChargeReversal
       python-matter-antimatter-report.json
         MA_M2_discreteGroupCharacterTable  MA_M2_C_and_CP_status
       checker of this commit only (not in the committed Python report)
         MA_M2_cpScopeInCurvedFields
row 3  none; nothing was computed
```

The same three rows, in the checker's own words, are stored in the committed Python report as the measurement `M6_sakharovScorecard`, and that report records the honest answer as the measurement `honestAnswer`. The committed report was written by an earlier version of the checker (Section 17.17). The checker of the same commit words the rows more precisely: row 1 adds the vanishing boundary flux, and row 2 adds the scope of CP given in the table above and lists `MA_M2_cpScopeInCurvedFields`. Its honest answer adds that at the quantum level no reading gives a cancellation between two independent universes, because the image field is the same quantum system (Section 17.13).

**The answer.** The dirac16complex theory as built does **not** solve the matter–antimatter problem. Its charge is exactly conserved (M1), it has exact charge-reversing symmetries (M2: C for dirac16complex00 in every gravitational field, CP for dirac16complex in flat space and wherever the reflection is an isometry), nothing computes a departure from equilibrium, it contains no baryons of the Standard Model, and it predicts no value of $\eta$. What it contributes is exact but structural: a pair of universes of masses $+M$ and $-M$ with opposite charges and zero total charge (M4), which, under the three hypotheses of M5, would realise the idea of a symmetric whole made of two asymmetric parts. The statement "this theory solves the matter–antimatter mysteries" is therefore not established; it cannot be proved within the theory as built, because its central part, the creation of a net charge inside one universe, is excluded by Theorem M1.

### 17.16 What would have to be added to the theory

The following list is a consequence of M1 to M3. It describes necessary ingredients; none of them is present in the theory, none is claimed to be natural, and none has been shown to be sufficient.

1. **A charge-violating interaction.** By M3, for the anticommuting field no Majorana-type mass term exists. The lowest-order candidates are the derivative term $\sqrt{|g|}\,\Psi^TC\gamma^8\gamma^\mu D_\mu\Psi$ plus its Hermitian conjugate (charge 2), and quartic terms such as $Q_4$ (charge 4) and $Q_2$ (charge 2) plus their conjugates. For the commuting field the mass terms $\Psi^TCP_\pm\Psi$ and the derivative term $\sqrt{|g|}\,\Psi^TC\gamma^\mu D_\mu\Psi$ (the form of the notebook's Lg[]), each plus its complex conjugate, have charge 2. Each such term breaks the U(1) of M1 down to a discrete set of phases (derived): $e^{i\alpha}$ with $e^{2i\alpha}=1$ for charge-2 terms, and with $e^{4i\alpha}=1$ for charge-4 terms.
2. **Breaking of every charge-reversing symmetry.** The added terms must break every exact symmetry of Section 17.11 that reverses $Q$ without reversing $x_4$: $\mathrm C_0$ and the 63 others for the commuting field ($\mathrm C_0$ holds in every gravitational field), and the CP family for the anticommuting field (64 maps, among them $\mathrm C_8\mathrm P_b$ for $b=0,1,2,3$ and $\mathrm C_8\mathrm P_{123}$), which hold in flat space and wherever the reflection is an isometry. A generic gravitational field already breaks the CP family (Section 17.11), but that is of use only together with item 1: as long as the charge is conserved, no symmetry breaking can create a net charge. A remark that is derived but not machine-checked: the U(1) rotation $\Psi\to e^{i\alpha}\Psi$ is a symmetry of $\mathcal L$ and multiplies the coefficient $g$ of a charge-2 term by $e^{2i\alpha}$, so the phase of a single such coefficient can be removed by redefining the field; only relative phases between several charge-violating terms can be physical. Whether a given combination breaks the CP family is not computed (OPEN).
3. **A departure from equilibrium.** A dynamical history in which the charge-violating processes are out of equilibrium, for example during the evolution of the primordial field of Chapter 9, and a computation of their rates. Nothing of this kind has been computed.
4. **A link to baryons.** The dirac16complex charge would have to be connected to the baryon number of the Standard Model (H3), which requires couplings to Standard-Model fields that the theory does not contain.
5. **A computation of $\eta$.** Only with items 1 to 4 could a value of $\eta$ be computed and compared with the observed $\eta\approx6\times10^{-10}$ of Section 17.3.

### 17.17 How the analysis was verified, and how to rerun it

**The reports.** Two independent exact implementations were written for the analysis, and one Stage-5 report is used as an input:

```
artifacts/dirac16complex/matter-antimatter/wolfram-matter-antimatter-report.json
  44 of 44 checks true; producer scripts/verify_dirac16complex_matter_antimatter.wls
  with wolfram/Dirac16ComplexMatterAntimatter.wl; also writes
  artifacts/dirac16complex/matter-antimatter/matter-antimatter-theory.json
artifacts/dirac16complex/matter-antimatter/python-matter-antimatter-report.json
  75 of 75 checks true; producer scripts/check_dirac16complex_matter_antimatter.py
  with scripts/grassmann_algebra.py, in an earlier version; the report records
  for the checker the sha256
  20914546ed5894ef223be8a1ae7ffecb62b308fdbf13d88f35a939a3c27bd526
  while the committed checker file has the sha256
  ef1a00dc02e72186cd6c78d83ad3d930c372ccd9440983a307e8e04cae622231
  and 77 checks (all true when rerun)
artifacts/dirac16complex/pair-creation/wolfram-pairing-report.json   (Stage-5 input)
  141 of 141 checks true; producer scripts/verify_dirac16complex_pairing.wls
```

Both matter-antimatter implementations compute exactly: integers, fractions, Gaussian rationals (complex numbers with rational parts), exact symbolic algebra and exact Grassmann algebras. No floating-point number decides any check, with the one labelled exception `MA_M1_ksFixedNetNumberRecorded` (Section 17.9). Each starts from the gamma matrices built from their definitions and compares them with the exact fixture `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json`. The Python checker uses nothing produced by Wolfram as truth: it compares its own results with the Wolfram theory file only in its agreement check `MA_agreesWithWolfram` (2048 classification rows, 22 summary items, the 64 charge-reversing symmetries, the invariant forms, the survival table, $Q_4$, the Krein facts and the $\gamma^8$ facts, with no disagreement). Two things about the committed Python report are older than the files next to it. First, it records, as `inputSha256`, the sha256 of the Wolfram theory file it compared with, `a3a85c9a...`; the committed theory file has the sha256 `1505a396...` (the Wolfram verifier was rerun afterwards), so the agreement check of that report refers to the earlier version. Second, it was written by an earlier version of the Python checker (the two sha256 values are in the list above). The checker file in the same commit has 77 checks, two more than the report: `MA_M2_cpScopeInCurvedFields`, which verifies the scope of CP in a gravitational field (Section 17.11), and `MA_M4_imageFieldFockModel`, which verifies in an exact Fock model that the image field is the same quantum system as $\Psi_+$ (Sections 17.13 and 17.14). It also words some measurements more precisely: the rows of `M6_sakharovScorecard`, the hypothesis H1 of `M5_conditionalScenario` (the second member with the Lagrangian $+\mathcal L_{-m,-\lambda}$) and `honestAnswer`. A rerun of this checker against the committed theory file gives 77 of 77 checks true, and the 75 checks of the committed report are among them, all true (Section 19.10 records such a rerun from a fresh clone). Regenerating the committed report is unfinished work of the matter–antimatter analysis. The Stage-5 input files carry no finality flag; they are cited by their sha256 values in both matter-antimatter reports, and the Fock-level statements taken from them are provisional (Section 17.13).

**Counting the checks yourself.** With the method of Section 0.8, start Python in the repository root:

```
>>> import json
>>> folder = "artifacts/dirac16complex/matter-antimatter/"
>>> for name in ["wolfram-matter-antimatter-report.json",
...              "python-matter-antimatter-report.json"]:
...     checks = json.load(open(folder + name, encoding="utf-8"))["checks"]
...     print(name, sum(checks.values()), len(checks))
...
```

(The last line, an empty continuation line, ends the loop.) It prints the two file names followed by `44 44` and `75 75`: all checks of the committed reports are true.

**Rerunning the verifiers without touching the committed files.** Run from the repository root; the output goes to the folder `build/ma/`, which Git ignores. The Wolfram step takes about 11 to 13 minutes and the Python checker about a minute (681 and 53 seconds in the rerun of Section 19.10; the matter-antimatter document gives about 13 minutes and half a minute). In Git Bash:

```
export PYTHONUTF8=1
wolframscript -file scripts/verify_dirac16complex_matter_antimatter.wls \
    build/ma/wolfram-report.json build/ma/theory.json
python scripts/check_dirac16complex_matter_antimatter.py \
    --theory build/ma/theory.json --output build/ma/python-report.json
```

In PowerShell (the line continuation is a backtick):

```
$env:PYTHONUTF8 = "1"
wolframscript -file scripts/verify_dirac16complex_matter_antimatter.wls `
    build/ma/wolfram-report.json build/ma/theory.json
python scripts/check_dirac16complex_matter_antimatter.py `
    --theory build/ma/theory.json --output build/ma/python-report.json
```

Each checker prints one line `check_<name>=true` (or `false`) per check and ends with `check_count` and `failed_check_count`. Expect `check_count=44` and `failed_check_count=0` from the Wolfram verifier, and `check_count=77` and `failed_check_count=0` from the Python checker: 77, not the 75 of the committed report, for the reason given above. The Wolfram report path is a plain positional argument, and an optional second positional argument sets the path of the theory file (the matter-antimatter document explains why no double hyphen is used). The typeset matter-antimatter document is `provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.pdf`; Chapter 19 collects the commands of all stages.

### 17.18 Literature cited in this chapter

- C. D. Anderson, "The positive electron", Phys. Rev. 43, 491 (1933).
- A. D. Sakharov, "Violation of CP invariance, C asymmetry, and baryon asymmetry of the universe", JETP Lett. 5, 24 (1967).
- Planck Collaboration (N. Aghanim et al.), "Planck 2018 results. VI. Cosmological parameters", Astron. Astrophys. 641, A6 (2020), arXiv:1807.06209; erratum Astron. Astrophys. 652, C4 (2021).
- D. J. Fixsen, "The temperature of the cosmic microwave background", Astrophys. J. 707, 916 (2009).
- E. Tiesinga, P. J. Mohr, D. B. Newell and B. N. Taylor, "CODATA recommended values of the fundamental physical constants: 2018", Rev. Mod. Phys. 93, 025010 (2021).
- R. H. Cyburt, B. D. Fields, K. A. Olive and T.-H. Yeh, "Big bang nucleosynthesis: Present status", Rev. Mod. Phys. 88, 015004 (2016).
- L. Canetti, M. Drewes and M. Shaposhnikov, "Matter and antimatter in the universe", New J. Phys. 14, 095012 (2012), arXiv:1204.4186.
- A. G. Cohen, A. De Rújula and S. L. Glashow, "A matter-antimatter universe?", Astrophys. J. 495, 539 (1998).
- ALPHA Collaboration (E. K. Anderson et al.), "Observation of the effect of gravity on the motion of antimatter", Nature 621, 716 (2023).
- V. A. Kuzmin, V. A. Rubakov and M. E. Shaposhnikov, "On anomalous electroweak baryon-number non-conservation in the early universe", Phys. Lett. B 155, 36 (1985).
- K. Kajantie, M. Laine, K. Rummukainen and M. E. Shaposhnikov, "Is there a hot electroweak phase transition at $m_H\gtrsim m_W$?", Phys. Rev. Lett. 77, 2887 (1996), arXiv:hep-ph/9605288.
- ATLAS Collaboration, "Observation of a new particle in the search for the Standard Model Higgs boson with the ATLAS detector at the LHC", Phys. Lett. B 716, 1 (2012).
- CMS Collaboration, "Observation of a new boson at a mass of 125 GeV with the CMS experiment at the LHC", Phys. Lett. B 716, 30 (2012).
- M. B. Gavela, P. Hernández, J. Orloff and O. Pène, "Standard Model CP-violation and baryon asymmetry", Mod. Phys. Lett. A 9, 795 (1994).
- P. Huet and E. Sather, "Electroweak baryogenesis and standard model CP violation", Phys. Rev. D 51, 379 (1995), arXiv:hep-ph/9404302.
- L. Boyle, K. Finn and N. Turok, "CPT-Symmetric Universe", Phys. Rev. Lett. 121, 251301 (2018).

### 17.19 What we proved and what we assumed

**Proved in this chapter** (complete derivations, with the exact machine checks named where the repository has them): the three Sakharov conditions in the form of Propositions 17.1 and 17.2 and of the equilibrium argument of Section 17.5, each under its stated premises; the conversion $\eta=2.7342\times10^{-8}\,\Omega_bh^2$, given the quoted constants and the quoted black-body photon density, and the size (about 0.2 percent) of the helium correction it leaves out; **Theorem M1**: the exact U(1) invariance of $\mathcal L$ for both statistics and every admissible potential, the Noether current, the off-shell identity $\partial_\mu(\sqrt{|g|}\,j^\mu)=\sqrt{|g|}(\bar E\Psi+\bar\Psi E)$ in every gravitational field, the conservation of $Q$ when the boundary flux vanishes, the indefinite charge density $\Psi^\dagger B\Psi$, and (derived) the conservation of the normal-ordered charge after quantization; **Theorem M2**: the lemmas A, B and C; the transformation rule for all linear and antilinear maps built from a constant matrix and a reflection of frame directions, in flat space, in every gravitational field in the frame form (which relates the theories on the frames $e$ and $e\,\mathrm{diag}(r)$), and in the coordinate form wherever the reflection is an isometry; Lemma D (derived here), which shows that no other constant matrix gives an exact symmetry; the classification of the exact symmetries; the counts (1024 maps, four classes of 256, 256 exact symmetries, 64 exact charge-reversing symmetries without $x_4$ reversal for each statistics); the table of C, P, CP, T and CPT, with its scope: C exact for dirac16complex00 in every gravitational field; no constant C but an exact CP for dirac16complex with $m\ne0$, in flat space and wherever the reflection is an isometry, broken by a generic gravitational field (no frame rotation of $\mathrm{Spin}_0(4,4)$ and no other exact symmetry undoes its frame change); the compatibility of the exact symmetries with the canonical anticommutator (of unitary type if they preserve $x_4$, of antiunitary type if they reverse it), and (derived) the reversal of the normal-ordered charge by the CP of unitary type; the continuous reversal of $x_4$ and of the classical charge by $\exp(\pi S^{45})=\gamma^4\gamma^5$ in signature (4,4), and (derived) the preservation of the quantum charge by these maps, which are of antiunitary type; **Theorem M3**: the invariant bilinear forms are $C(\alpha P_-+\beta P_+)$, all symmetric, so the anticommuting field has no Majorana mass term, with the Pin characters, the derivative terms and the charge 2 of every such term; **Theorem M4**: the chirality map turns every solution with $(m,\lambda)$ into one with $(-m,-\lambda)$, reverses the current and the energy–momentum tensor, so the pair has zero total charge and zero total energy–momentum in every gravitational field, and at the one-particle level $\gamma^8$ preserves energies and Hilbert norms and reverses Krein norms; the classical-level implication of **M5** (Proposition M5), for two classical fields governed by $\mathcal L_{m,\lambda}$ and $+\mathcal L_{-m,-\lambda}$.

**Computed (floating-point data):** only the record that the committed Kohn–Sham runs have the net occupation $N$ to $10^{-9}$ relative.

**Cited and provisional:** the Fock-level statements of Section 17.13, taken from the Stage-5 pairing report (`PAIR_T1krein`, all 141 checks of that report true), provisional until the Stage-5 gate has passed, including the operator identity $:\!T^{\mathrm{pair}}_{\mu\nu}\!:\ =0$ in the image-field reading, which is not a part of Proposition M5; and the caveat on their meaning recorded in the Wolfram matter-antimatter report (the image field is the same quantum system; in the independent reading, in the free Fock model, the kinetic and mass energies add, and for $\lambda\ne0$ the interaction energies have opposite signs). The two checks `MA_M2_cpScopeInCurvedFields` and `MA_M4_imageFieldFockModel` belong to the checker of this commit and are not in the committed Python report (Section 17.17).

**Quoted from the literature, not derived:** every observational statement (the value of $\Omega_bh^2$, the temperature of the microwave background, the agreement with nucleosynthesis, the exclusion of antimatter domains, the ALPHA-g result), the analysis of the Standard Model, the black-body photon density, the values of the constants, the CPT theorem of ordinary quantum field theory, and the description of the proposal of Boyle, Finn and Turok.

**Assumed:** the Lagrangian of Section 17.8 for both statistics (Chapter 6), with anticommuting components for the fermion field dirac16complex; the signature (4,4) as the setting of the model, which is not the signature of observed spacetime (row L43 of Chapter 0), so that applying the scenario of M5 to our universe is a further assumption; the canonical quantization with respect to $x_4$ and the restriction of every quantum statement to the good sector (Chapter 8), where alone a positive Fock space exists, so that the quantum statements are formal (Krein space, ill-posed extra-time sector) and dirac16complex00 is treated as a classical field; Gaussian normal gauge wherever $B$ appears; the vanishing of the boundary flux for charge conservation; a fixed gravitational field as the background of the discrete symmetries of M2; and the class of maps examined in M2 (constant matrices, complex conjugation, reflections of frame directions).

**Hypotheses (not derived):** H1, H2 and H3 of Section 17.14.

**OPEN:** a creation process, rate or amplitude for a pair of universes (Chapter 16); which quantum reading, if any, gives a physical universe of mass $-M$ whose charge and energy cancel those of ours (of the two readings examined, neither does); whether the exact symmetries of unitary and antiunitary type are implemented by actual operators on the positive Fock space of the good sector; whether any combination of charge-violating terms breaks the CP family; higher-order charge-violating terms; and everything that a computation of $\eta$ would need (Section 17.16).

**The conclusion, stated plainly:** the theory as built does not solve the matter–antimatter problem. It contains no baryon-number-violating interaction (its charge is exactly conserved in every gravitational field when no charge flows through the boundary), it has an exact charge-reversing symmetry for each of its two fields (C for dirac16complex00 in every gravitational field; CP for dirac16complex in flat space and wherever the reflection is an isometry, and where a gravitational field breaks this CP the charge is still conserved), it contains no departure-from-equilibrium computation and no Standard-Model baryons, and it predicts no baryon-to-photon ratio.

### 17.20 Exercises

**Exercise 17.1.** For each process decide whether the electric charge, $B$, $L$ and $B-L$ are conserved: (a) $p\to e^++\pi^0$ (a decay that has never been observed; some extensions of the Standard Model predict it); (b) $\mu^-\to e^-+\bar\nu_e+\nu_\mu$ (the muon $\mu^-$ and the muon neutrino $\nu_\mu$ have $L=+1$); (c) $\bar p+p\to\pi^++\pi^-$.

**Exercise 17.2.** With $\eta=2.7342\times10^{-8}\,\Omega_bh^2$ (Section 17.3), compute $\eta$ and the number of photons per baryon for $\Omega_bh^2=0.0220$ and $0.0230$. Why does the coefficient not depend on $h$?

**Exercise 17.3.** A quantum state has the energy $E=T$. Compute the particle and antiparticle occupations $f_\pm=1/(e^{(E\mp\mu_B)/T}+1)$ for $\mu_B=0$ and for $\mu_B=0.1\,T$, and the surplus per state. Why must $\mu_B$ vanish when reactions that change $B$ are in equilibrium?

**Exercise 17.4.** In the toy model of Section 17.5 take $N=5000$, $r=0.52$ and $\bar r=0.48$. (a) Compute $\Delta B$. (b) Which Sakharov conditions does the toy meet by construction, and which one is hidden in the assumption that the decays run in one direction only? (c) What is $\Delta B$ if C is an exact symmetry?

**Exercise 17.5.** For commuting components and a constant $\alpha$, find the factor that multiplies each of the following under $\Psi\to e^{i\alpha}\Psi$: (a) $S=\bar\Psi\Psi$, (b) $j^\mu$, (c) $\Psi^TC\Psi$, (d) $S^2$, (e) $S\,\Psi^TC\gamma^8\Psi$. Which of them may appear in a Lagrangian with the U(1) symmetry of Theorem M1?

**Exercise 17.6.** For the commuting field $\Psi=(a\,u_++b\,u_-)\,e^{-imx_4}$ of Section 17.9 compute $J^4$, $\Psi^\dagger\Psi$ and the classical energy density $\rho$ for $(a,b)=(1,0)$, $(0,1)$, $(1/\sqrt2,1/\sqrt2)$ and $(1/\sqrt2,i/\sqrt2)$. Which charge does one quantum in the mode $u_-$ carry in the quantized theory?

**Exercise 17.7.** Take two components and the matrix $Y$ whose only nonzero entry is $Y_{01}=1$. Compute $\Psi^TY\Psi^\ast$ and $\Psi^\dagger Y^T\Psi$ for commuting and for anticommuting components, and read off the statistics sign $s$ of Lemma C.

**Exercise 17.8.** Use the rule of Theorem M2 to find $\kappa$, $\sigma$ and $c_j$ for $\mathrm C_0\mathrm P_{0123}$ ($M=C$, $R=\{0,1,2,3\}$, antilinear) and for $\mathrm P_b$ ($M=\gamma^b$, $R=\{b\}$ with $b\le3$, linear), for both statistics, and compare with the table of Section 17.11.

**Exercise 17.9.** (a) How many subsets of $\{0,1,2,3\}$ have an even number of elements, and how many an odd number? (b) Derive the number 64 of exact charge-reversing symmetries without $x_4$ reversal. (c) Why is there exactly one exact map for each allowed set $R$?

**Exercise 17.10.** (a) Show that $(CP_+)^T=CP_+$. (b) For commuting components compute $\Psi^TCP_+\Psi$ for $\Psi_8=1$, $\Psi_{12}=3$ and all other components 0, and its value after $\Psi\to e^{i\pi/2}\Psi$. (c) Show that $\Psi^TCP_+\Psi=0$ for anticommuting components.

**Exercise 17.11.** For the unit vector $u=\gamma^4$ compute $u^TCu$ and $u^T(C\gamma^8)u$ directly, and compare with item 3 of Theorem M3.

**Exercise 17.12.** Compute $\gamma^8u_-$ for the rest state $u_-$ of Section 17.9 and its Krein norm $(\gamma^8u_-)^\dagger B(\gamma^8u_-)$. What is the total charge density of the pair made of $u_-e^{-imx_4}$ and its image?

**Exercise 17.13.** Show that $\mathcal L_{m,\lambda}[\gamma^8\Psi]+\mathcal L_{-m,-\lambda}[\Psi]=0$ and $\mathcal L_{m,\lambda}[\gamma^8\Psi]+\mathcal L_{-m,\lambda}[\Psi]=-\lambda\sqrt{|g|}\,S^2$.

**Exercise 17.14.** (a) Show that $(\gamma^4\gamma^5)^2=-1$ and $\exp(\pi S^{45})=\gamma^4\gamma^5$. (b) Show that conjugation by $R=\gamma^4\gamma^5$ maps $\gamma^4\to-\gamma^4$ and $\gamma^5\to-\gamma^5$ and leaves $\gamma^0$ unchanged. (c) Why is this exact symmetry not a candidate for C or CP in Sakharov's argument?

**Exercise 17.15.** Show that $\gamma^8B^T\gamma^8=B$ and $B^T=-B$. Which of the charge conjugations $\mathrm C_0$ and $\mathrm C_8$ is of unitary type in the quantized anticommuting theory (Section 17.11), and what is still open about it?

**Exercise 17.16.** (a) Suppose H1 and H3 hold, and $Q_+=0$ at $x_4=0$. What is the baryon excess $B_+$ of our universe today? (b) Explain why the scenario M5 cannot predict $\eta$, even if H1 to H3 hold.

**Exercise 17.17.** The term $g\sqrt{|g|}\,\Psi^TC\gamma^8\gamma^\mu D_\mu\Psi$ plus its Hermitian conjugate is added to the Lagrangian of the anticommuting field, with a complex number $g\ne0$. (a) Which constant phases $e^{i\alpha}$ remain symmetries? (b) Show that the phase of $g$ can be changed at will by redefining the field. (c) Which of Sakharov's conditions would this term address, and what would still be missing?

**Exercise 17.18.** (a) Write down $\mathrm{diag}(r)$ for the CP map $\mathrm C_8\mathrm P_1$ ($R=\{1\}$) and for the map $\mathrm C_0\mathrm P_{0123}$ ($R=\{0,1,2,3\}$), and the determinant of the $4\times4$ block of the space-like directions in each case. (b) Which of the two frame changes is a frame rotation of $\mathrm{Spin}_0(4,4)$? (Hint: the rotation $\exp(\pi S^{01})$ turns the plane of $x_0$ and $x_1$ by the angle $\pi$.) (c) Is $\mathrm C_8\mathrm P_1$ a symmetry of dirac16complex in the primordial field of Chapter 9? In the generic test field G_A?

### 17.21 Answers to the exercises

**Answer 17.1.** (a) Charge: $+1\to+1+0$, conserved. $B$: $1\to0$, violated. $L$: $0\to-1$ (the positron is an antilepton), violated. $B-L$: $1\to0-(-1)=1$, conserved. (b) Charge: $-1\to-1+0+0$, conserved; $B$: $0\to0$; $L$: $1\to1-1+1=1$, conserved; hence also $B-L$. (c) Charge: $-1+1=0\to+1-1=0$; $B$: $-1+1=0\to0$; $L$: $0\to0$: all conserved.

**Answer 17.2.** $\eta=2.7342\times10^{-8}\times0.0220=6.015\times10^{-10}$ and $2.7342\times10^{-8}\times0.0230=6.289\times10^{-10}$; the numbers of photons per baryon are $1/\eta=1.662\times10^9$ and $1.590\times10^9$. The critical density is proportional to $H_0^2$, hence to $h^2$, so the baryon mass density $\Omega_b\rho_{\mathrm{crit}}$ depends on $\Omega_b$ and $h$ only through the product $\Omega_bh^2$; this is also why the microwave background measures this product.

**Answer 17.3.** For $\mu_B=0$: $f_+=f_-=1/(e+1)=0.268941$, no surplus. For $\mu_B=0.1\,T$: $f_+=1/(e^{0.9}+1)=0.289050$ and $f_-=1/(e^{1.1}+1)=0.249740$, a surplus of $0.039311$ particles per state. A chemical potential belongs to a conserved number: the Gibbs state is built from the Hamiltonian and the conserved numbers. If reactions that change $B$ are in equilibrium, $B$ is not conserved, the equilibrium state has no chemical potential for it, $\mu_B=0$, and particles and antiparticles are equally populated.

**Answer 17.4.** (a) $\Delta B=N(r-\bar r)=5000\times0.04=200$. (b) The decays violate $B$ (condition 1), and $r\ne\bar r$ requires C and CP violation (condition 2). The departure from equilibrium (condition 3) is hidden in the assumption that the inverse processes, such as $q+q\to X$, do not run; in equilibrium they would, and by the argument of Section 17.5 the average asymmetry would be erased. (c) An exact C gives $r=\bar r$ and $\Delta B=0$.

**Answer 17.5.** (a) $e^{-i\alpha}e^{i\alpha}=1$; (b) 1; (c) $e^{2i\alpha}$; (d) 1; (e) $1\cdot e^{2i\alpha}=e^{2i\alpha}$. Only (a), (b), (d) and functions of invariant quantities may appear; (c) and (e) carry U(1) charge 2.

**Answer 17.6.** $J^4=|a|^2-|b|^2$ and $\Psi^\dagger\Psi=|a|^2+|b|^2$ (Section 17.9). For $(1,0)$: $J^4=1$; for $(0,1)$: $J^4=-1$; for $(1/\sqrt2,1/\sqrt2)$ and $(1/\sqrt2,i/\sqrt2)$: $J^4=\tfrac12-\tfrac12=0$. In all four cases $\Psi^\dagger\Psi=1$. All four fields have the frequency $\omega=m$, so $\rho=mJ^4$ (Section 7.11): $\rho=m$, $-m$, $0$ and $0$. The second field has positive frequency and negative classical energy. In the quantized theory one quantum in the positive-energy mode $u_-$ has the charge $u_-^\dagger B\,B\,u_-=u_-^\dagger u_-=1$, like every particle.

**Answer 17.7.** $\Psi^TY\Psi^\ast=\Psi_0\Psi_1^\ast$. The only nonzero entry of $Y^T$ is $(Y^T)_{10}=1$, so $\Psi^\dagger Y^T\Psi=\Psi_1^\ast\Psi_0$. For commuting components the two are equal: $s=+1$. For anticommuting components $\Psi_0\Psi_1^\ast=-\Psi_1^\ast\Psi_0$: $s=-1$.

**Answer 17.8.** $\mathrm C_0\mathrm P_{0123}$: $M=C=\Gamma_R$ with $|R|=4$, so $\varepsilon=(-1)^4=+1$; $s_R=4$, $\sigma_R=+1$. Then $\kappa=s$, $\sigma=s$ and $c_j=-s$. Commuting ($s=1$): exact, $c_j=-1$, so $Q\to-Q$. Anticommuting ($s=-1$): $\kappa=\sigma=-1$, $\mathcal L_{m,\lambda}\to-\mathcal L_{m,-\lambda}$. $\mathrm P_b$: $M=\gamma^b=\Gamma_R$ with $|R|=1$, so $\varepsilon=-1$; $s_R=1$, $\sigma_R=-1$. Then $\kappa=\sigma_R\varepsilon=+1$, $\sigma=-1$, $c_j=+1$: $\mathcal L_{m,\lambda}\to\mathcal L_{-m,\lambda}$ for both statistics. All four entries agree with the table.

**Answer 17.9.** (a) Even: $\binom40+\binom42+\binom44=1+6+1=8$; odd: $\binom41+\binom43=4+4=8$. (b) The charge-reversing exact symmetries that keep $x_4$ are the exact antilinear maps with $4\notin R$. The part $R\cap\{0,1,2,3\}$ must have even size (commuting) or odd size (anticommuting): 8 choices; the part $R\cap\{5,6,7\}$ is arbitrary: $2^3=8$ choices. In total $8\times8=64$. (c) By Lemma D, an exact map with the set $R$ has, up to a factor of modulus 1, a matrix that solves the equation of Lemma B with $\varepsilon=+1$; no other constant matrix is possible. The two solutions $\Gamma_R$ and $\Gamma_{R^c}$ of Lemma B have opposite signs $\varepsilon$, so exactly one of them has $\varepsilon=+1$.

**Answer 17.10.** (a) $(CP_+)^T=P_+^TC^T=P_+C=CP_+$, because $P_+=\mathrm{diag}(0,I_8)$ is symmetric and commutes with $C$ ($\gamma^8$ does). (b) $CP_+=\mathrm{diag}(0,\sigma)$ has the entries $+1$ at $(8,12),(9,13),(10,14),(11,15)$ and at the mirror places, so $\Psi^TCP_+\Psi=2(\Psi_8\Psi_{12}+\Psi_9\Psi_{13}+\Psi_{10}\Psi_{14}+\Psi_{11}\Psi_{15})=2\cdot1\cdot3=6$. After the phase it is $e^{i\pi}\cdot6=-6$. (c) Each pair of mirror entries gives, for example, $\Psi_8\Psi_{12}+\Psi_{12}\Psi_8=0$ for anticommuting components.

**Answer 17.11.** $\gamma^4$ is antisymmetric, $(\gamma^4)^T=-\gamma^4$, and commutes with $C$ (it anticommutes with all four factors of $C$). So $u^TCu=-\gamma^4C\gamma^4=-C(\gamma^4)^2=C$. With $n(u)=-1$ item 3 predicts $-n(u)C=C$. Next, $u^TC\gamma^8u=-\gamma^4C\gamma^8\gamma^4=-C\gamma^4\gamma^8\gamma^4=C\gamma^8\gamma^4\gamma^4=-C\gamma^8$, and item 3 predicts $n(u)C\gamma^8=-C\gamma^8$.

**Answer 17.12.** $u_-=\tfrac12(e_0+e_4+i\,e_9-i\,e_{13})$, and $\gamma^8$ reverses the upper eight components: $v=\gamma^8u_-=\tfrac12(-e_0-e_4+i\,e_9-i\,e_{13})$. With the rows of $B$: $(Bv)_0=iv_9=-\tfrac12=v_0$, $(Bv)_4=-iv_{13}=-\tfrac12=v_4$, $(Bv)_9=-iv_0=\tfrac i2=v_9$, $(Bv)_{13}=iv_4=-\tfrac i2=v_{13}$. So $Bv=v$ and the Krein norm is $+1$, as $\gamma^8B\gamma^8=-B$ requires ($u_-^\dagger Bu_-=-1$). The total charge density of the pair is $-1+1=0$.

**Answer 17.13.** With $S[\gamma^8\Psi]=S$ and $K[\gamma^8\Psi]=-K$: $\mathcal L_{m,\lambda}[\gamma^8\Psi]=\sqrt{|g|}(-K-mS-\tfrac\lambda2S^2)$. Adding $\mathcal L_{-m,-\lambda}[\Psi]=\sqrt{|g|}(K+mS+\tfrac\lambda2S^2)$ gives 0. Adding $\mathcal L_{-m,\lambda}[\Psi]=\sqrt{|g|}(K+mS-\tfrac\lambda2S^2)$ gives $-\lambda\sqrt{|g|}\,S^2$.

**Answer 17.14.** (a) $\gamma^4\gamma^5\gamma^4\gamma^5=-\gamma^4\gamma^4\gamma^5\gamma^5=-(-1)(-1)=-1$. With $S^{45}=\tfrac12\gamma^4\gamma^5$ and $J=\gamma^4\gamma^5$, $J^2=-1$, Section 2.11 gives $\exp(\pi S^{45})=\exp(\tfrac\pi2J)=\cos\tfrac\pi2+J\sin\tfrac\pi2=J$. (b) $R^{-1}=-\gamma^4\gamma^5$. Then $R\gamma^4R^{-1}=-\gamma^4\gamma^5\gamma^4\gamma^4\gamma^5=\gamma^4\gamma^5\gamma^5=-\gamma^4$ and $R\gamma^5R^{-1}=-\gamma^4\gamma^5\gamma^5\gamma^4\gamma^5=\gamma^4\gamma^4\gamma^5=-\gamma^5$. $\gamma^0$ anticommutes with both $\gamma^4$ and $\gamma^5$, so it commutes with $R$ and is unchanged. (c) It reverses $x_4$: it maps a history running forward in $x_4$ to one running backward. Proposition 17.2 needs a symmetry that maps histories to histories in the same direction of time, which C and CP do and this rotation does not.

**Answer 17.15.** $C$ is symmetric, $\gamma^4$ antisymmetric, and they commute, so $(C\gamma^4)^T=(\gamma^4)^TC=-\gamma^4C=-C\gamma^4$ and $B^T=-i(C\gamma^4)^T=iC\gamma^4=-B$. Then $\gamma^8B^T\gamma^8=-\gamma^8B\gamma^8=-(-B)=B$. By Section 17.11 a map $\Psi\to M\Psi^{\dagger T}$ gives the anticommutator $MB^TM^\dagger$: for $\mathrm C_8$ ($M=\gamma^8$) this is $B$, so $\mathrm C_8$ is of unitary type; for $\mathrm C_0$ ($M=1$) it is $-B$, so $\mathrm C_0$ is of antiunitary type although it does not reverse $x_4$. Being of unitary type is necessary for an implementation by a unitary operator, not sufficient: whether a unitary operator on the positive Fock space of the good sector implements $\mathrm C_8$ is OPEN.

**Answer 17.16.** (a) By M1 the charge is conserved, so $Q_+=0$ at all times, and by H3 $B_+=0$: no baryon excess. The excess of our universe must be assumed as an initial condition, which is the content of H2. (b) By M1, $Q_+$ never changes, so its value is an initial condition put in by H2; nothing in the repository computes it. Moreover $\eta$ counts the photons of our universe, and the theory contains no photons of the Standard Model, so even the denominator of $\eta$ is outside the theory.

**Answer 17.17.** (a) The added term is multiplied by $e^{2i\alpha}$ and its conjugate by $e^{-2i\alpha}$, so only phases with $e^{2i\alpha}=1$ remain: $\alpha\in\{0,\pi\}$, that is $\Psi\to\pm\Psi$. (b) Redefine $\Psi=e^{i\beta}\Psi'$. The original Lagrangian is unchanged (Theorem M1), and the new term becomes $ge^{2i\beta}\sqrt{|g|}\,\Psi'^TC\gamma^8\gamma^\mu D_\mu\Psi'$; choosing $2\beta=-\arg g$ makes the coefficient real and positive. Only relative phases between several charge-violating terms could have a physical meaning. (c) It addresses condition 1: the charge would no longer be conserved. For condition 2 every exact charge-reversing symmetry of the CP family would have to be broken as well, and whether this term does so is not computed. Condition 3 needs a non-equilibrium history and a computation of rates, and a link to the baryons of the Standard Model and a computation of $\eta$ would still be missing (Section 17.16).

**Answer 17.18.** (a) The two frame changes are

$$
\mathrm C_8\mathrm P_1:\ \mathrm{diag}(1,-1,1,1,1,1,1,1),\qquad \mathrm C_0\mathrm P_{0123}:\ \mathrm{diag}(-1,-1,-1,-1,1,1,1,1).
$$

The space-like block of the first is $\mathrm{diag}(1,-1,1,1)$, with determinant $-1$; that of the second is $-I_4$, with determinant $(-1)^4=+1$. (b) The second. The rotation by $\pi$ in the plane of $x_0,x_1$ reverses $x_0$ and $x_1$ and leaves the other six coordinates alone, the one in the plane of $x_2,x_3$ reverses $x_2$ and $x_3$, and their product is the frame change of $\mathrm C_0\mathrm P_{0123}$. The first cannot be a frame rotation of $\mathrm{Spin}_0(4,4)$, because every such rotation has a space-like block with determinant at least 1 (Section 17.11, "Which entries hold in a gravitational field"). (c) The primordial field has a diagonal metric that depends only on $x_0$ and $x_4$ (Section 9.2), so the reflection of $x_1$ is an isometry, and $\mathrm C_8\mathrm P_1$ in its coordinate form is an exact, charge-reversing symmetry there. G_A is a generic non-diagonal field without this isometry: only the frame form holds, which relates the theories on the frames $e$ and $e\,\mathrm{diag}(r)$, and at a fixed frame the internal part of $\mathrm C_8\mathrm P_1$ is not a symmetry (check `MA_M2_cpScopeInCurvedFields`). The charge is conserved in both fields (Theorem M1).
