## 16. Does the big bang create universes in pairs?

### 16.1 The question, and the answer in brief

The request that this book answers asks, among other things, for a proof "that the 'big bang' creates universes in pairs". The author's notebook states the same idea as a hypothesis: at the time $x_4=0$ a universe of mass $+M$ and a universe of mass $-M$ are created together. This chapter examines that statement with everything the earlier chapters have built, and it says exactly how much of it the repository establishes.

The answer, in five sentences, each with its status word from Section 0.3:

1. **PROVED.** The field equations of dirac16complex (anticommuting components) and of dirac16complex00 (commuting components) have exact **pairing symmetries** (Chapter 15): the chirality map $\Psi\mapsto\gamma^8\Psi$ turns every solution with mass and coupling $(m,\lambda)$ into a solution with $(-m,-\lambda)$ (theorem T1); a reflection of a space-like frame direction turns every solution with $(m,\lambda)$ into one with $(-m,\lambda)$, and across the brane of the primordial field it produces a mirror universe of mass $-M$ (theorem T2); and the same two statements hold exactly for the Kohn–Sham ground and first excited states (theorem T3).
2. **PROVED (a consequence of T1), with a limit that is also PROVED.** A pair made of a universe $\Psi_+$ with $(m,\lambda)$ and its image $\Psi_-=\gamma^8\Psi_+$ with $(-m,-\lambda)$ carries zero total energy, momentum, stress and charge at every point of every gravitational field and at every time $x_4$. So the **totals** of such a pair are those of the empty state, and Einstein's equations with the pair as their only source are the equations without a source. This holds for the fields treated as classical fields, with the partner's coupling $-\lambda$ and the partner in exactly the configuration $\gamma^8\Psi_+$; the partner then has the opposite classical energy density, $-\rho_+$ (negative wherever $\rho_+>0$, as in Worked example 16.B). The limit: in the theory as built the two members do not interact, so the charge of each member, and in a gravitational field that does not change with time also the energy of each member, is conserved **on its own**. These separate conservation laws forbid the appearance of a cancelling pair out of the empty state unless each member has zero charge (and, in such a static field, zero energy), exactly as for the mirror pair of item 3 (Section 16.9). Only an interaction between the members, which the theory does not contain, could leave the totals as the only conserved quantities (OPEN). For the quantized field no reading examined in the repository gives two independent universes whose energies and charges cancel (Section 16.6): at the quantum level the cancellation is OPEN.
3. **PROVED.** A pair with zero total energy and momentum is invisible to gravity, so it can only accompany a gravitational field that needs no source. In eight-dimensional Einstein gravity the primordial field of the notebook needs a nonzero source (Chapter 9), so such a pair cannot be what produces it; with the Lovelock terms of orders 2 and 3 this is OPEN (Section 16.10). The mirror pair of T2, which can live on the two sides of the brane, has equal, not opposite, energies.
4. **OPEN (not derived).** No creation process, no creation rate, no probability amplitude, no wave function of the universe and no dynamical big bang is derived anywhere in the project.
5. **HYPOTHESIS.** "The big bang creates universes in pairs" therefore remains what the notebook calls it, a hypothesis. Stage 1 of the project put it in one sentence, which this chapter repeats: the pairing of the masses $\pm m$ is "a structural property of the equations, not a claim that universes of masses $\pm M$ are created in pairs" (Stage-1 document `provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md`, Section 1.3, item 6).

**The word "consistent".** In this chapter "a process is consistent with a law" means "the law does not forbid it". It is a statement of logic, and it can be proved: to prove that energy conservation does not forbid a process, one shows that the energy before equals the energy after. It is much weaker than "the process happens". Section 16.4 shows with an everyday example of physics how large the difference is.

**Plan.** Section 16.2 quotes the hypothesis and reads it word by word. Section 16.3 separates three different questions hidden in it. Sections 16.4 and 16.5 show, with two examples from ordinary physics and from Chapter 11, what "creation" means when it is actually computed. Sections 16.6 and 16.7 state what is proved, with the key steps of the proofs (the complete proofs are in Chapter 15), and Section 16.8 what is computed. Section 16.9 derives what is consistent with the conservation laws and what the separate conservation laws of the two members forbid, and Section 16.10 confronts the zero total source of a cancelling pair with the nonzero source that the primordial field needs. Sections 16.11 and 16.12 list what is not derived and what a calculation of pair creation would require. Section 16.13 is the ledger of the chapter.

**Sources.** The exact Stage-5 theory consists of two Wolfram packages with their verifiers and two independent sympy checkers. Their reports and the collected exact statements are these files, with the programs that write them:

```
artifacts/dirac16complex/pair-creation/
  wolfram-pairing-report.json            141 of 141 checks true
    (scripts/verify_dirac16complex_pairing.wls, wolfram/Dirac16ComplexPairing.wl)
  python-pairing-report.json             172 of 172 checks true
    (scripts/check_dirac16complex_pairing.py)
  wolfram-dirac16complex00-report.json    46 of 46 checks true
    (scripts/verify_dirac16complex00.wls, wolfram/Dirac16Complex00.wl)
  python-dirac16complex00-report.json     49 of 49 checks true
    (scripts/check_dirac16complex00.py)
  pairing-theory.json                    the exact pairing statements
  dirac16complex00-theory.json           the exact statements on dirac16complex00
```

Check names beginning with `PAIR_` belong to the Wolfram pairing report; the Python report repeats each family under names beginning with `S5_`. The numerical pair runs are in the subfolders `rust/` and `reference/` of the same folder. Further sources are the matter–antimatter analysis `provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md`, the Stage-1 and Stage-2 documents, the notebook survey `handoff/surveys/survey_notebook-physics.md`, and Chapters 8, 9, 11 and 13 of this book.

**State of the work when this chapter was written.** Stages 1 to 3 of the project are complete and verified by their gates. In Stage 4 the Rust Kohn–Sham solver of Chapter 13 is complete, its final cross-check against the independent reference solver has 63 checks of which 1 failed (`artifacts/dirac16complex/kohn-sham/python-check-report.json`, the check `canonical_eigenvalues`), and the Stage-4 gate has not been run; this chapter uses Stage-4 outputs in Sections 16.8 and 16.10, and they carry that status. The exact Stage-5 theory is complete in the sense that its four reports are committed and every check in them is true. The Stage-5 numerics are partial (Section 16.8), the Stage-5 documents have not been written, and no Stage-5 gate exists. The chapter quotes only committed files and says at each number where it comes from.

### 16.2 The hypothesis in the author's own words

The notebook is a working file, and its statements about pairs of universes are spread over a few text cells. The survey of the notebook quotes them (`handoff/surveys/survey_notebook-physics.md`, item 3 and the list of section titles). Cell 6 says:

"HYPOTHESIS: If, employing the Einstein eqs (or Einstein-Lovelock eqs), superluminal inflation/deflation exists, then at time x4 = 0 ... a pair of universes with MASSES ± M is created".

Cell 7, the title of a section, asks:

"Bigger Bang: Question: Are Universe (s) of masses ± M created in pairs at time x4 = 0 (before the particles of the standard model exist) ?"

Cell 17 records the task:

"M is the mass of the Ψ16 field"; "TODO: prove Universe(s) of masses ±M are created in pairs!"

Cell 23, in the middle of a derivation of the source of the metric, adds a hope: that the source tensor of the spinor field be $\Lambda g^{\mu\nu}$, "and H = some function of M, where Universe(s) of masses ± M created in pairs at time x4 = 0".

The project documents have responded to the TODO of cell 17 twice, in the same careful way, without claiming to have carried it out. Stage 1: the pairing of the masses by the chirality map "is a structural property of the equations, not a claim that universes of masses $\pm M$ are created in pairs" (Stage-1 document, Section 1.3, item 6). Stage 2 (the Stage-2 document, Section 16): the pairing "echoes the notebook's hypothesis", but it is "structural only", and "nothing about a creation process at $x_4=0$, about a pair of universes, or about a physical preference between the two signs follows from it".

**Reading the hypothesis word by word.** Each word needs a precise meaning before anything can be proved about it.

- *"A universe of mass $M$."* Cell 17 says that $M$ is the mass of the field $\Psi_{16}$. A "universe of mass $M$" is therefore a configuration of the dirac16complex field (or of dirac16complex00) whose mass parameter in the Lagrangian is $M$, living in some gravitational field. It is **not** the total gravitational mass or energy of that universe; Section 16.6 shows that a universe with a negative mass parameter can have positive energy. The dictionary between the notebook and this book is $m=-HM$ (Sections 5.12 and 9.14): the notebook writes the mass term as $+HM\,\Psi^TC\Psi$, this book as $-m\,\bar\Psi\Psi$. So the notebook's universe of mass $+M$ has the book's mass $m=-HM$. The sign of the mass is a convention at this point, and Section 16.7 shows that it is even less than that: it is tied to the orientation of the frame.
- *"At time $x_4=0$."* $x_4$ is the time in which everything evolves (Section 0.6). The gravitational field is the notebook's metric of Chapter 9, which is **prescribed**, not computed (status ASSUMED); its free function $a_4(t)$, $t=Hx_4$, is not determined by any equation of the notebook or of the project.
- *"Before the particles of the standard model exist."* The theory contains no particles of the Standard Model at all; this part of the sentence is outside what the theory can address.
- *"Big bang."* In cosmology the big bang is the hot and dense early phase from which the present expansion of the universe started; in the classical solutions of Einstein's equations that describe it, the scale factor (the number that measures the size of every region of space, Section 9.4) goes to zero at a finite time in the past, and the equations break down there (a **singularity**). The notebook's section title speaks of a "Bigger Bang", and the notebook uses the moment $x_4=0$ for it. Section 16.11 shows that the notebook's metric has no singularity at $x_4=0$.
- *"Created in pairs."* This is the claim itself. Section 16.3 separates three things it can mean.
- *The premise "if ... superluminal inflation/deflation exists".* Chapter 9 has examined it for Einstein gravity: every member of the notebook's family of metrics needs a source with negative energy density, $\rho_{\mathrm{req}}=-3H^2(7+a_4'^2)/\kappa<0$ (Section 9.10, PROVED), and for linear $a_4$ a dirac16complex condensate that does not depend on $x_0$ is an exact source of that kind (Proposition 9.4, PROVED in the mean-field reading). So the premise can be met in Einstein gravity, but only with a negative energy density. With the Lovelock terms of orders 2 and 3, which neither the notebook nor the project computes, the question is OPEN.

**Status.** The hypothesis of cells 6, 7 and 17 is a HYPOTHESIS (the honesty ledger of Section 0.9 records it so). The hope of cell 23 that the source be $\Lambda g$ cannot be realized in eight-dimensional Einstein gravity (Section 9.10, PROVED), and no relation between $H$ and $M$ is derived anywhere (OPEN).

### 16.3 Three different questions

The sentence "the big bang creates universes in pairs" packs three questions of very different difficulty into one.

**Q1. Is it allowed?** Do the conservation laws of the theory (energy, momentum, charge) and the equations of gravity permit a transition from a state without universes to a state with a pair? This is a question about **constraints**: it asks whether something forbids the transition. It can be answered by comparing conserved quantities before and after.

**Q2. Does it happen in a classical solution?** Is there a solution of the coupled equations (the field equations of the two universes together with the gravitational field equations) that contains no universes before some moment and the pair after it? This is a question about **dynamics** in the classical theory.

**Q3. How likely is it?** In the quantum theory, what is the probability amplitude for the transition, and what is the probability, or the number of pairs created per unit time? This is a question about **quantum dynamics**; its answer is a number.

The repository answers Q1 for the fields treated as classical fields (Section 16.9), and the answer has two parts. The totals of a cancelling pair (energy, momentum, charge) are those of the empty state, so the conservation of the totals does not forbid its appearance. But in the theory as built the two members do not interact, so the charge of each member (and, in a gravitational field that does not change with time, the energy of each member) is conserved on its own, and these separate laws forbid the appearance of any pair, cancelling or mirror, whose members carry a nonzero charge (or, in such a field, a nonzero energy). At the quantum level Q1 is still open (Section 16.6). The repository does not answer Q2 or Q3 (Sections 16.11 and 16.12): both are OPEN.

**Symmetry is not realization.** A pairing theorem says: for every solution with mass $+M$ there is a solution with mass $-M$. It does not say that whenever the first is present, the second is present too. An everyday comparison makes the difference plain. The laws of mechanics do not change when everything is reflected in a mirror; so for every right hand that the laws allow, a left hand is allowed as well. That does not mean that every right hand comes with a left hand, still less that hands are created in right–left pairs. To go from "the partner is allowed" to "the partner is created together with the original", one needs an answer to Q2 or Q3.

### 16.4 A lesson from ordinary physics: when can a photon make a pair?

The difference between "allowed" and "happens" is best seen in a process that is completely understood: the creation of an electron and a positron (its antiparticle) from light. It also shows that the conservation laws can forbid a process that one might naively expect.

**Energy, momentum and mass.** We use ordinary space with three directions and one time, and units in which the speed of light is 1. A particle of mass $m$ with momentum $\mathbf p=(p_1,p_2,p_3)$ has the energy $E=\sqrt{m^2+|\mathbf p|^2}$, where $|\mathbf p|^2=p_1^2+p_2^2+p_3^2$. This is the relation $E^2=k_1^2+k_2^2+k_3^2+m^2$ of Section 2.4, which the Dirac equation was built to reproduce. A photon has $m=0$, so $E=|\mathbf p|$. For a collection of particles, the total energy $E_{\mathrm{tot}}$ and the total momentum $\mathbf p_{\mathrm{tot}}$ are the sums over the particles, and we define its **invariant mass** $\mu$ by

$$
\mu^2:=E_{\mathrm{tot}}^2-|\mathbf p_{\mathrm{tot}}|^2 .
$$

For a single particle $\mu=m$. The conservation of energy and momentum says that $E_{\mathrm{tot}}$ and $\mathbf p_{\mathrm{tot}}$ are the same before and after any process; hence $\mu^2$ is the same before and after as well. (These conservation laws, and the relation between $E$, $\mathbf p$ and $m$, are the standard physics of special relativity; we use them as given.)

**Lemma 16.1.** Two bodies with invariant masses $\mu_1,\mu_2\ge0$ (each a particle or a collection of particles, with energies $E_i=\sqrt{\mu_i^2+|\mathbf p_i|^2}$) have together an invariant mass of at least $\mu_1+\mu_2$:

$$
(E_1+E_2)^2-|\mathbf p_1+\mathbf p_2|^2\ \ge\ (\mu_1+\mu_2)^2 .
$$

*Proof.* Write $a=|\mathbf p_1|$ and $b=|\mathbf p_2|$. Multiplying out,

$$
(E_1+E_2)^2-|\mathbf p_1+\mathbf p_2|^2=E_1^2-a^2+E_2^2-b^2+2\bigl(E_1E_2-\mathbf p_1\cdot\mathbf p_2\bigr)=\mu_1^2+\mu_2^2+2\bigl(E_1E_2-\mathbf p_1\cdot\mathbf p_2\bigr).
$$

The dot product satisfies $\mathbf p_1\cdot\mathbf p_2=ab\cos\theta\le ab$, where $\theta$ is the angle between the two vectors. So it is enough to show $E_1E_2\ge\mu_1\mu_2+ab$. Both sides are non-negative, so we may compare their squares:

$$
E_1^2E_2^2=(\mu_1^2+a^2)(\mu_2^2+b^2)=\mu_1^2\mu_2^2+\mu_1^2b^2+\mu_2^2a^2+a^2b^2,
$$

$$
(\mu_1\mu_2+ab)^2=\mu_1^2\mu_2^2+2\mu_1\mu_2ab+a^2b^2 .
$$

The difference is $\mu_1^2b^2+\mu_2^2a^2-2\mu_1\mu_2ab=(\mu_1b-\mu_2a)^2\ge0$. Hence $E_1E_2-\mathbf p_1\cdot\mathbf p_2\ge\mu_1\mu_2$, and the left-hand side is at least $\mu_1^2+\mu_2^2+2\mu_1\mu_2=(\mu_1+\mu_2)^2$. $\square$

**Proposition 16.2 (a single photon cannot make a pair).** A single photon in empty space cannot turn into an electron and a positron.

*Proof.* Before: one photon, $\mu^2=E^2-|\mathbf p|^2=0$. After: two particles of mass $m>0$ each, so by Lemma 16.1 $\mu^2\ge(2m)^2>0$. Since $\mu^2$ is conserved, $0\ge4m^2$, which is false. $\square$

Charge does not forbid the process (the electron has charge $-1$ and the positron $+1$, total 0, the same as the photon's), and neither does energy on its own (the photon can have as much energy as we like). It is the combination of energy and momentum conservation that forbids it.

**Proposition 16.3 (with a nucleus it is allowed).** A photon of energy $E_\gamma$ that hits a nucleus of mass $M_N$ at rest can produce an electron–positron pair (the nucleus remaining in the final state) only if

$$
E_\gamma\ \ge\ 2m\Bigl(1+\frac{m}{M_N}\Bigr),
$$

and the conservation laws allow it for every energy above this threshold.

*Proof.* Before: total energy $E_\gamma+M_N$, total momentum that of the photon, of size $E_\gamma$. So $\mu^2=(E_\gamma+M_N)^2-E_\gamma^2=M_N^2+2E_\gamma M_N$. After: the pair has, by Lemma 16.1, an invariant mass of at least $2m$, and applying the lemma once more to the pair and the nucleus, the final state has $\mu\ge2m+M_N$. Conservation requires $M_N^2+2E_\gamma M_N\ge(2m+M_N)^2=M_N^2+4mM_N+4m^2$, that is $E_\gamma\ge2m+2m^2/M_N$. Conversely, if the inequality holds, there are final momenta of the three bodies with exactly the initial total energy and momentum (Exercise 16.4 constructs them), so no conservation law is violated. $\square$

**Worked example.** In units of the electron mass, $m=1$. For a nucleus with $M_N=4$ the threshold is $2(1+\tfrac14)=2.5$. For $M_N=1000$ it is $2.002$, and for $M_N=1836$ (about the mass of a proton in units of the electron mass) it is $2.00109$. For a heavy nucleus the photon must bring the two rest energies, $2m$, and a tiny bit more: the nucleus takes up the momentum but almost no energy. With the standard value of the electron's rest energy, about 0.511 MeV, the threshold near a heavy nucleus is about 1.022 MeV.

**Two photons.** Two photons of energies $E_a$ and $E_b$ moving head-on have the momenta $E_a\mathbf n$ and $-E_b\mathbf n$ for a unit vector $\mathbf n$, so

$$
\mu^2=(E_a+E_b)^2-(E_a-E_b)^2=4E_aE_b,
$$

so the conservation laws require $4E_aE_b\ge4m^2$, that is $E_aE_b\ge m^2$; above this value they allow a pair (the construction of Exercise 16.4 works here as well). Here no third body is needed.

**What the example teaches.** Three lessons carry over to universes.

1. Conservation laws are **necessary** conditions. They can rule a process out (Proposition 16.2); they never rule a process in.
2. Whether an allowed process happens, and how often, is computed from the **dynamics**. For light near a nucleus this is quantum electrodynamics, the quantum theory of electrons and light, which gives the probability of pair creation as a **cross section**: an effective target area $\sigma$ attributed to each nucleus, such that a photon aimed at random into an area $A$ around one nucleus makes a pair with the probability $\sigma/A$. The calculation goes back to Bethe and Heitler (H. Bethe and W. Heitler, Proc. R. Soc. Lond. A 146, 83 (1934)), and pair creation by two photons was first computed by Breit and Wheeler (G. Breit and J. A. Wheeler, Phys. Rev. 46, 1087 (1934)). This book quotes these results; it does not derive them.
3. For a pair of universes of masses $\pm M$ related by T1, treated as classical fields, the **totals** of the pair (energy, momentum, charge) are zero, the same as for the empty state (Section 16.9). Here the analogy with light breaks down at two points. First, the electron and the positron are two quanta of one and the same field, the electron field, whose charge is the sum of their charges, $-1+1=0$; the two universes of a cancelling pair are two different fields, each with a charge of its own. Second, light and the electron field interact (the interaction of quantum electrodynamics is what turns light into matter), so the energy of the light alone is not conserved: the photon hands its energy to the pair, and only the total energy is conserved. The two universes do not interact, so the charge of each universe, and in a gravitational field that does not change with time the energy of each universe, is conserved on its own. These separate laws forbid the appearance of a pair out of the empty state unless each universe has zero charge (and, in such a field, zero energy). The analogue of lesson 2, a dynamics that produces the pair and a computed probability, does not exist in the project either (Sections 16.11 and 16.12).

**Status.** Lemma 16.1 and Propositions 16.2 and 16.3 are PROVED here from the conservation of energy and momentum and the relation $E^2=m^2+|\mathbf p|^2$, which are ASSUMED as standard physics. The existence and size of the pair-creation cross sections are quoted from the literature, not computed in this book.

### 16.5 What creation looks like when it is computed

The project itself contains one complete calculation of pair creation: not of universes, but of particle–antiparticle pairs of the dirac16complex field in an expanding universe. It is experiment EXP-4b of Stage 3, described in Section 11.11. Recalling its structure shows what a calculation of the creation of universes would have to provide.

**The ingredients of EXP-4b.**

1. **A quantum field with a vacuum.** The field is quantized in the good sector (no momentum along the extra times, Section 8.10); its vacuum is the filled Dirac sea.
2. **A time-dependent background.** Three-dimensional space expands with a prescribed scale factor $a(t)$: de Sitter inflation glued to a radiation era at $t=0$.
3. **The dynamics.** Every momentum mode obeys its equation $i\,\dot u=h(t)\,u$ with a Hamiltonian $h(t)$ that changes with time because the momentum is redshifted by the expansion.
4. **The answer: a number.** A mode that starts in its negative-energy level ends with a weight $|\beta_k|^2$ in the positive-energy level; that is a created particle, and the hole it leaves is a created antiparticle. Summed over the modes, the number of created quanta per comoving volume is $na^3$.

**The result** (COMPUTED; `artifacts/dirac16complex/numerics/exp4/summary.json`, key `pair`, list `masses`, entry $m=1$, value `nA3`): for $m=H_{\mathrm{inf}}$ the sudden end of inflation creates $na^3=4.412\times10^{-3}\,H_{\mathrm{inf}}^3$ quanta, and for $m=0$ none (Section 11.11 explains why: the massless equation does not notice an expansion of this type). Gravitational particle creation of this kind was discovered by Parker (L. Parker, Phys. Rev. Lett. 21, 562 (1968)).

**What the analogous calculation for universes would need.** A quantum theory in which a whole universe plays the role of a quantum; a "vacuum" that describes the absence of universes; a dynamics, either an interaction or a time-dependent background of some kind, that connects this state with states containing universes; and the resulting amplitude. None of these four ingredients exists in the notebook or in the project. Section 16.12 lists them in detail. The pairing theorems, to which we now turn, are statements of a different kind: they compare solutions, they do not produce them.

### 16.6 What is proved (1): the chirality map and the cancelling pair

**The setting.** Both fields of the book, dirac16complex (anticommuting components) and dirac16complex00 (commuting components), have the same Lagrangian density (Chapters 6 and 8)

$$
\mathcal L_{m,\lambda}=\sqrt{|g|}\,\Bigl[K-mS-\tfrac\lambda2S^2\Bigr],\qquad K=\tfrac12\bigl(\bar\Psi\gamma^\mu D_\mu\Psi-(D_\mu\bar\Psi)\gamma^\mu\Psi\bigr),\qquad S=\bar\Psi\Psi,\qquad \bar\Psi=\Psi^\dagger C,
$$

with $D_\mu\Psi=\partial_\mu\Psi+\Omega_\mu\Psi$, $D_\mu\bar\Psi=\partial_\mu\bar\Psi-\bar\Psi\Omega_\mu$, $\Omega_\mu=\tfrac12\omega_{\mu ab}S^{ab}$ and $\gamma^\mu=e_a{}^\mu\gamma^a$. The subscripts record the mass $m$ and the coupling $\lambda$ of the potential $U=\tfrac\lambda2S^2$. The field equation is $E_{m,\lambda}[\Psi]:=\gamma^\mu D_\mu\Psi-(m+\lambda S)\Psi=0$. The conserved Hermitian current is $J^\mu=-i\bar\Psi\gamma^\mu\Psi$, whose time component in Gaussian normal gauge is the charge density $J^4=\Psi^\dagger B\Psi$ with $B=-iC\gamma^4$ (Section 8.12). The energy–momentum tensor is (Chapter 7; Sections 9.12 and 13.14 use the same formula)

$$
T_{\mu\nu}=-\tfrac14\Bigl[\bar\Psi\gamma_\mu D_\nu\Psi+\bar\Psi\gamma_\nu D_\mu\Psi-(D_\mu\bar\Psi)\gamma_\nu\Psi-(D_\nu\bar\Psi)\gamma_\mu\Psi\Bigr]+g_{\mu\nu}\,\mathcal L_s,\qquad \mathcal L_s=\mathcal L/\sqrt{|g|},
$$

with $\gamma_\mu=g_{\mu\nu}\gamma^\nu$ and the energy density $\rho=T_{44}$.

**Four matrix facts** (Chapter 2, Sections 2.10 and 2.12). (i) $\gamma^8=\gamma^0\gamma^1\cdots\gamma^7=\mathrm{diag}(-I_8,I_8)$ is real and diagonal, hence Hermitian, and $(\gamma^8)^2=1$. (ii) $\gamma^8$ anticommutes with every $\gamma^a$, hence with every curved $\gamma^\mu=e_a{}^\mu\gamma^a$ and every $\gamma_\mu$ (the coefficients are ordinary functions). (iii) $\gamma^8$ commutes with $C$ and with every $S^{ab}$, hence with every $\Omega_\mu$ and with $D_\mu$. (iv) $\gamma^8B\gamma^8=-B$: indeed $\gamma^8B\gamma^8=-iC\gamma^8\gamma^4\gamma^8=-iC(-\gamma^4)(\gamma^8)^2=iC\gamma^4=-B$, using (iii) to move $\gamma^8$ past $C$ and (ii) to move it past $\gamma^4$.

**The bilinear rule.** Put $\Psi_-:=\gamma^8\Psi$. By (i), $\Psi_-^\dagger=\Psi^\dagger\gamma^8$, and by (iii), $\bar\Psi_-=\Psi^\dagger\gamma^8C=\Psi^\dagger C\gamma^8=\bar\Psi\gamma^8$. Also $D_\mu\Psi_-=\gamma^8D_\mu\Psi$ and $D_\mu\bar\Psi_-=(D_\mu\bar\Psi)\gamma^8$, because $\gamma^8$ is constant and commutes with $\Omega_\mu$. Therefore every bilinear $\bar\Psi X\Psi$ (with or without derivatives on either side) goes over into $\bar\Psi\gamma^8X\gamma^8\Psi$. If $X$ contains exactly one gamma matrix, possibly multiplied by spin generators $S^{ab}$ and ordinary functions, then (ii) and (iii) give $\gamma^8X\gamma^8=-X$; if $X=1$, then $\gamma^8X\gamma^8=1$. So

$$
K[\Psi_-]=-K[\Psi],\qquad S[\Psi_-]=S[\Psi],\qquad J^\mu[\Psi_-]=-J^\mu[\Psi],
$$

and every kinetic bilinear inside $T_{\mu\nu}$ changes sign.

**Theorem T1 (chirality map; PROVED).** For every gravitational field (every vielbein), every mass $m$, every coupling $\lambda$, every field configuration $\Psi$ (solution or not) and both statistics:

$$
\begin{aligned}
&\mathcal L_{m,\lambda}[\gamma^8\Psi]=-\mathcal L_{-m,-\lambda}[\Psi],\qquad E_{-m,-\lambda}[\gamma^8\Psi]=-\gamma^8E_{m,\lambda}[\Psi],\\
&T_{\mu\nu}[\gamma^8\Psi;-m,-\lambda]=-T_{\mu\nu}[\Psi;m,\lambda],
\end{aligned}
$$

and $J^\mu[\gamma^8\Psi]=-J^\mu[\Psi]$. In particular $\Psi$ solves the field equations with $(m,\lambda)$ if and only if $\gamma^8\Psi$ solves them with $(-m,-\lambda)$.

*Proof.* Lagrangian: by the bilinear rule, $\mathcal L_{m,\lambda}[\gamma^8\Psi]=\sqrt{|g|}\,[-K-mS-\tfrac\lambda2S^2]=-\sqrt{|g|}\,[K-(-m)S-\tfrac{(-\lambda)}2S^2]=-\mathcal L_{-m,-\lambda}[\Psi]$. Field equation: $\gamma^\mu D_\mu(\gamma^8\Psi)=\gamma^\mu\gamma^8D_\mu\Psi=-\gamma^8\gamma^\mu D_\mu\Psi$ by (ii), and $S[\gamma^8\Psi]=S[\Psi]$, so

$$
E_{-m,-\lambda}[\gamma^8\Psi]=-\gamma^8\gamma^\mu D_\mu\Psi-(-m-\lambda S)\gamma^8\Psi=-\gamma^8\bigl[\gamma^\mu D_\mu\Psi-(m+\lambda S)\Psi\bigr]=-\gamma^8E_{m,\lambda}[\Psi].
$$

Since $\gamma^8$ is invertible, one side vanishes exactly when the other does. Energy–momentum tensor: the bracket consists of kinetic bilinears, which change sign, and $\mathcal L_s[\gamma^8\Psi;-m,-\lambda]=-\mathcal L_s[\Psi;m,\lambda]$ is the Lagrangian identity with $(m,\lambda)$ replaced by $(-m,-\lambda)$ and divided by $\sqrt{|g|}$. Current: bilinear rule. Statistics: the map is linear and keeps every $\Psi^\dagger$ to the left of every $\Psi$, so no two anticommuting factors are ever exchanged; the proof holds word for word for Grassmann components (in the notebook basis the map simply multiplies $\Psi_0,\dots,\Psi_7$ by $-1$). $\square$ (Chapter 6 proves the Lagrangian identity in the same way, and Section 15.3 gives every step of the whole theorem.)

**The coupling must change sign.** The potential $\tfrac\lambda2S^2$ is even in $S$ while the kinetic term is odd under the map. At a fixed coupling the identity fails: $\mathcal L_{m,\lambda}[\gamma^8\Psi]+\mathcal L_{-m,\lambda}[\Psi]=\sqrt{|g|}\,[-K-mS-\tfrac\lambda2S^2+K+mS-\tfrac\lambda2S^2]=-\lambda\sqrt{|g|}\,S^2\ne0$ (erratum E2 of `handoff/specs/CONTRACT.md`; check `PAIR_T1generic_naiveFixedLambdaFails`). So the partner universe of T1 has mass $-m$ **and** coupling $-\lambda$; only for $\lambda=0$ are the two members the same free field with the masses $+m$ and $-m$.

**The same map, read as a reversed frame.** Replacing the vielbein $e$ by $-e$ leaves the metric $g_{\mu\nu}=e_\mu{}^a\eta_{ab}e_\nu{}^b$, $\sqrt{|g|}$ and the spin connection unchanged (in $\omega_\mu{}^a{}_b$ the vielbein and its inverse appear once each, so the two signs cancel) and reverses every $\gamma^\mu$. Hence $K\to-K$, $S\to S$, and $\mathcal L_{m,\lambda}[-e,\Psi]=-\mathcal L_{-m,-\lambda}[e,\Psi]$: the partner of T1 is also the original field described with the reversed frame (checks `PAIR_T1jets_vielbeinSignFlipIsT1` and `PAIR_T1jets_gamma8WithFrameSignIsSymmetry`). The signs of $m$ and $\lambda$, together with the overall sign of the Lagrangian, are therefore tied to a choice of frame; Section 16.7 meets a cleaner form of the same fact.

**How T1 is verified.** Stage 1 checked the Lagrangian identity with the exact matrices (check `ALG_gamma8Map` in both algebra reports of Stage 1). Stage 5 checked every identity of T1 as an exact polynomial identity in completely generic symbols, in a genuine Grassmann algebra with 288 odd generators, with exact jets of a general non-diagonal vielbein, and in the notebook's primordial field with an arbitrary function $a_4$ and fields that depend on all eight coordinates. The checks, all true in `wolfram-pairing-report.json`, are

```
PAIR_T1generic_lagrangian       PAIR_T1generic_fieldEquation
PAIR_T1generic_conjugateFieldEquation  PAIR_T1generic_emtAll36
PAIR_T1generic_current          PAIR_T1grassmann_lagrangian
PAIR_T1grassmann_diracOperator  PAIR_T1grassmann_emt   PAIR_T1grassmann_current
PAIR_T1jets_lagrangian          PAIR_T1jets_emt        PAIR_T1jets_fieldEquations
PAIR_T1primordial_lagrangian    PAIR_T1primordial_diracOperator
PAIR_T1primordial_emt64         PAIR_T1primordial_current
```

and the independent Python checker repeats the four families as `S5_T1generic`, `S5_T1grassmann`, `S5_T1jets` and `S5_T1primordial`. The theorem is about infinitely many fields, so the proof is the derivation above; the checks confirm it exactly.

**Worked example 16.A (T1 with the actual matrices).** Take the constant spinor $\Psi=e_0+e_4-i\,e_9$, where $e_k$ is the column with 1 in position $k$ (counting from 0) and 0 elsewhere. From the table of $C$ and $B/i$ in Section 2.9: $(Cu)_0=-u_4$, $(Cu)_4=-u_0$, $(Cu)_9=u_{13}$; $(Bu)_0=i\,u_9$, $(Bu)_4=-i\,u_{13}$, $(Bu)_9=-i\,u_0$. Only the components 0, 4 and 9 of $\Psi$ are nonzero, so only these rows are needed:

$$
\begin{aligned}
&(C\Psi)_0=-\Psi_4=-1,\qquad (C\Psi)_4=-\Psi_0=-1,\qquad (C\Psi)_9=\Psi_{13}=0,\\
&(B\Psi)_0=i\Psi_9=1,\qquad (B\Psi)_4=-i\Psi_{13}=0,\qquad (B\Psi)_9=-i\Psi_0=-i .
\end{aligned}
$$

Hence $S=\Psi^\dagger C\Psi=1\cdot(-1)+1\cdot(-1)+i\cdot0=-2$ and $J^4=\Psi^\dagger B\Psi=1\cdot1+1\cdot0+i\cdot(-i)=2$ (remember $\Psi_9^\ast=+i$). Now $\gamma^8=\mathrm{diag}(-I_8,I_8)$ reverses the components 0 to 7, so $\gamma^8\Psi=-e_0-e_4-i\,e_9$. Repeating: $(C\gamma^8\Psi)_0=1$, $(C\gamma^8\Psi)_4=1$, so $S[\gamma^8\Psi]=(-1)(1)+(-1)(1)=-2$; and $(B\gamma^8\Psi)_0=i(-i)=1$, $(B\gamma^8\Psi)_9=-i(-1)=i$, so $J^4[\gamma^8\Psi]=(-1)(1)+(i)(i)=-2$. The scalar density is unchanged and the charge density has changed sign, exactly as T1 says. (The same numbers come out of the exact fixture `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json`.)

**Corollary 16.4 (the cancelling pair; PROVED).** Let $\Psi_+$ be a solution of the theory $\mathcal L_{m,\lambda}$, and let a second field $\Psi_-$ of the theory $\mathcal L_{-m,-\lambda}$, in the same gravitational field, be in the configuration $\Psi_-=\gamma^8\Psi_+$ (by T1 this is a solution). Then at every point and at every time $x_4$, in particular at $x_4=0$,

$$
T^{\mathrm{pair}}_{\mu\nu}:=T_{\mu\nu}[\Psi_+;m,\lambda]+T_{\mu\nu}[\Psi_-;-m,-\lambda]=0,\qquad J^\mu_++J^\mu_-=0,\qquad \mathcal L^{\mathrm{pair}}=0,\qquad S^{\mathrm{pair}}=2S[\Psi_+].
$$

The pair carries no net energy density, momentum density, stress or charge density anywhere, and hence no total energy, momentum or charge.

*Proof.* Add the identities of T1 for $\Psi=\Psi_+$. $\square$ (Corollary 15.4 states the same result with its hypotheses listed one by one.)

The Stage-5 checks are `PAIR_T1jets_pairEMTAndCurrentVanish` and `PAIR_totals_fieldLevelChiralPair`. The matter–antimatter analysis proves the same statement independently, as its Corollary M4.1, with the checks

```
artifacts/dirac16complex/matter-antimatter/wolfram-matter-antimatter-report.json
  MA_M4_pairEMTAndCurrentG1_commuting   MA_M4_pairEMTG1_grassmann
```

**Worked example 16.B (a pair at rest in flat space).** In flat space ($g=\eta$, $\Omega_\mu=0$) with $\lambda=0$, take a constant column $u$ and $\Psi_+=u\,e^{-i\varepsilon x_4}$, a field that depends only on the time. We first compute its energy density for any such stationary solution, treating the components as commuting numbers (the classical field dirac16complex00). With $\gamma_4=\eta_{44}\gamma^4=-\gamma^4$ and $D_4=\partial_4$, the $44$ component of $T_{\mu\nu}$ is

$$
\rho=T_{44}=-\tfrac14\bigl[2\bar\Psi\gamma_4\partial_4\Psi-2(\partial_4\bar\Psi)\gamma_4\Psi\bigr]+\eta_{44}\mathcal L_s=\tfrac12\bigl[\bar\Psi\gamma^4\partial_4\Psi-(\partial_4\bar\Psi)\gamma^4\Psi\bigr]-\mathcal L_s .
$$

Now $\partial_4\Psi=-i\varepsilon\Psi$ and, since $\bar\Psi=u^\dagger C\,e^{+i\varepsilon x_4}$, $\partial_4\bar\Psi=+i\varepsilon\bar\Psi$. The bracket is $-i\varepsilon\bar\Psi\gamma^4\Psi-i\varepsilon\bar\Psi\gamma^4\Psi$, so the first term is $-i\varepsilon\,\Psi^\dagger C\gamma^4\Psi=\varepsilon\,\Psi^\dagger B\Psi$. On a solution, $\mathcal L_s=SU'(S)-U(S)$ (Chapter 7: the field equations turn $K$ into $(m+U')S$), which is 0 for $U=0$. Hence

$$
\rho=\varepsilon\,\Psi^\dagger B\Psi=\varepsilon\,u^\dagger Bu .
$$

Take $m>0$ and the rest state $u_+=\tfrac12(e_0-e_4-i\,e_9-i\,e_{13})$ of Section 8.8, which satisfies $-i\gamma^4u_+=u_+$, $Cu_+=u_+$ and $Bu_+=u_+$. The field equation $\gamma^4\partial_4\Psi_+=m\Psi_+$ reads $-i\varepsilon\gamma^4u_+=mu_+$, which holds with $\varepsilon=m$. So $\Psi_+=u_+e^{-imx_4}$ is a solution with mass $m$, and

$$
\rho_+=m\,u_+^\dagger Bu_+=m,\qquad J^4_+=u_+^\dagger Bu_+=1,\qquad S_+=u_+^\dagger Cu_+=1 .
$$

The partner is $\Psi_-=\gamma^8u_+e^{-imx_4}$ with $\gamma^8u_+=\tfrac12(-e_0+e_4-i\,e_9-i\,e_{13})=:w$. It solves the equation with mass $-m$: $-im\gamma^4w=-im\gamma^4\gamma^8u_+=im\gamma^8\gamma^4u_+=-m\gamma^8(-i\gamma^4u_+)=-m\,w$, which is $\gamma^4\partial_4\Psi_-=-m\Psi_-$; its frequency is again $\varepsilon=m$. With $\gamma^8B\gamma^8=-B$ and $\gamma^8C\gamma^8=C$,

$$
\rho_-=m\,w^\dagger Bw=m\,u_+^\dagger\gamma^8B\gamma^8u_+=-m,\qquad J^4_-=-1,\qquad S_-=u_+^\dagger\gamma^8C\gamma^8u_+=+1 .
$$

(Check by hand with the tables of Section 2.9: $(Bw)_0=iw_9=\tfrac12$, $(Bw)_4=-iw_{13}=-\tfrac12$, $(Bw)_9=-iw_0=\tfrac i2$, $(Bw)_{13}=iw_4=\tfrac i2$, and $w^\dagger Bw=-\tfrac14-\tfrac14-\tfrac14-\tfrac14=-1$.) Both energy densities agree with the formula $\rho=mS+U$ that Chapter 7 derives for fields that depend only on the time: $\rho_+=m\,S_+=m$ and $\rho_-=(-m)\,S_-=-m$. The pair has $\rho_++\rho_-=0$ and $J^4_++J^4_-=0$, while its scalar density is $2$: this is Corollary 16.4 in the smallest possible example. The cancellation works because the partner has the **opposite** classical energy density, here the negative value $-m$.

**The classical energy has no fixed sign anyway.** The other rest state of Section 8.8, $u_-=\tfrac12(e_0+e_4+i\,e_9-i\,e_{13})$, also has $-i\gamma^4u_-=u_-$, hence also frequency $m$ for mass $m$, but $u_-^\dagger Bu_-=-1$: a universe of mass $+m$ in the state $u_-e^{-imx_4}$ has the classical energy density $-m$. The classical energy of the commuting field is not bounded below and its charge density has no fixed sign; Stage 5 proves both statements exactly for dirac16complex00 (`artifacts/dirac16complex/pair-creation/dirac16complex00-theory.json`, key `fields`, and the reports `wolfram-dirac16complex00-report.json` and `python-dirac16complex00-report.json`). Exercise 16.7 even builds a single classical universe with zero energy density and zero charge density. So, for the classical field, zero total energy is not a special property of pairs.

**The quantum field: two readings of the partner.** For the quantized field dirac16complex, energies and charges are not the classical bilinears but the expectation values of Section 8.12: a quantum in the normalized positive-energy mode $u$ has $\langle\Psi^\dagger X\Psi\rangle=u^\dagger BXu$, with $X=Bh$ for the energy ($h$ the mode Hamiltonian), $X=B$ for the charge and $X=C$ for the scalar density. At rest, $h=-im\gamma^4$ for mass $m$ and $BC=-i\gamma^4$. The partner universe can be given a quantum structure in two ways. The Stage-5 exact theory computes both (`pairing-theory.json`, key `T1krein`), with the checks

```
PAIR_T1krein_imageAnticommutatorMinusB   PAIR_T1krein_imageOperatorIdentities
PAIR_T1krein_imageExpectationValues      PAIR_T1krein_independentCARPlusB
PAIR_T1krein_independentExpectationValues
```

- **The image field.** The partner is the operator $\Psi_-=\gamma^8\Psi_+$ acting on the same space of states. Its canonical anticommutator is $\gamma^8B\gamma^8=-B$ (fact (iv)): it carries the **reversed Krein metric**. This is the anticommutator that the Lagrangian $-\mathcal L_{-m,-\lambda}$, which by T1 equals $\mathcal L_{m,\lambda}[\gamma^8\,\cdot\,]$, produces (in Chapter 8 the anticommutator comes from the kinetic term, and an overall minus sign reverses it). Its expectation rule is $\langle X\rangle=w^\dagger(-B)Xw$ with $w=\gamma^8u$. Every operator of this partner is $\gamma^8$ times the corresponding operator of the $+M$ universe.
- **The independent field.** The theory $\mathcal L_{-m,-\lambda}$ is quantized on its own, with the positive structure $+B$ of Chapter 8. Its modes are the $w=\gamma^8u$ (same energies $\varepsilon$), and its rule is $\langle X\rangle=w^\dagger BXw$.

For the rest quantum of Worked example 16.B the three descriptions give (energy $E$, charge $Q$, scalar density $S$):

| universe | $E$ | $Q$ | $S$ |
| --- | --- | --- | --- |
| $+M$ universe, mode $u_+$, rule $u^\dagger BXu$ | $u_+^\dagger h(m)u_+=m$ | $u_+^\dagger u_+=1$ | $u_+^\dagger(-i\gamma^4)u_+=1$ |
| image partner, mode $w$, rule $w^\dagger(-B)Xw$ | $-w^\dagger h(-m)w=-m$ | $-w^\dagger w=-1$ | $-w^\dagger(-i\gamma^4)w=1$ |
| independent partner, mode $w$, rule $w^\dagger BXw$ | $w^\dagger h(-m)w=m$ | $w^\dagger w=1$ | $w^\dagger(-i\gamma^4)w=-1$ |

Each entry is one line of algebra: $B^2=1$; $h(-m)w=im\gamma^4w=m\,w$ because $-i\gamma^4w=-w$ (from $\gamma^4\gamma^8=-\gamma^8\gamma^4$); for the image energy $w^\dagger(-B)(Bh(-m))w=-w^\dagger h(-m)w$; and $w^\dagger(-i\gamma^4)w=-w^\dagger w=-1$. So the image partner has $(E,Q,S)\to(-E,-Q,S)$ and the independent partner $(E,Q,S)\to(E,Q,-S)$. (Section 15.8 explains the reason in general: the expectation-value rule multiplies every classical matrix by $B$, and $\gamma^8$ reverses $B$.) This is the general rule found by the exact theory (`pairing-theory.json`, `T1krein`, entries `imageField` and `independentQuantisation`) and by the matter–antimatter analysis (the matter–antimatter document, Section 7.2, with three further exact examples).

**What the two readings give (PROVED; the Fock-level part cited from Stage 5).** Two facts decide the question.

1. *The image reading cancels only formally.* With the image rule the partner's $(E,Q,S)$ are $(-E,-Q,S)$, and at the level of operators Stage 5 proves ${:}T_{\mu\nu}[\gamma^8\Psi;-m,-\lambda]{:}=-{:}T_{\mu\nu}[\Psi;m,\lambda]{:}$ for the normal-ordered energy–momentum tensor. But the image field is built from the same operators, on the same states, as $\Psi_+$. The identities $Q_++Q[\Psi_-]=0$ and $H_++H[\Psi_-;-m]=0$ therefore have the form $X+(-X)=0$ and hold in every state; they are not a compensation by a second universe. Relative to its own canonical structure (the anticommutator $-B$, that is the Lagrangian $-\mathcal L_{-m,-\lambda}$), the image field's generator of time evolution is $-H[\Psi_-;-m]=+H_+$, its generator of phases is $-Q[\Psi_-]=+Q_+$, and its source of gravity, the energy–momentum tensor of its own Lagrangian (Section 5.8 defines it by varying the field's own action), is $-T_{\mu\nu}[\Psi_-;-m,-\lambda]=+T_{\mu\nu}[\Psi_+;m,\lambda]$. It is the same quantum system as the $+M$ universe, with the same energy and charge. The values $-|\varepsilon|$ and $-1$ per quantum in the table are expectation values of the formulas of $\mathcal L_{-m,-\lambda}$, not of that field's own Hamiltonian and charge. This observation is recorded in the committed matter–antimatter report `artifacts/dirac16complex/matter-antimatter/wolfram-matter-antimatter-report.json` (measurement `M5_implication`, entry `kreinLevelCaveat`, with the matrix identities of the check `MA_M4_kreinOneParticle`), and Chapter 17 discusses it as well.
2. *The independent reading adds.* Quantized with its own positive structure, the $-M$ universe has positive energies, so the energies of the pair add; the charges cancel only under the additional assumption that the $-M$ universe is in a state of opposite charge; and for $\lambda\ne0$ its interaction energy has the opposite sign. This is the mirror pairing of Section 16.7.

**Conclusion.** The cancellation of Corollary 16.4 is a statement about **classical** fields: two independent classical fields, with the Lagrangians $\mathcal L_{m,\lambda}$ and $\mathcal L_{-m,-\lambda}$, in the correlated configuration $\Psi_-=\gamma^8\Psi_+$, the second with the opposite classical energy density $-\rho_+$ (for dirac16complex00 this is the physical content; for dirac16complex it is a statement about its classical Grassmann-valued field). Of the two quantum readings examined in the repository, neither describes two independent, consistently quantized universes whose energies and charges cancel. Whether any quantum description of a physical universe of mass $-M$ realizes the classical cancellation is **OPEN**. (The matter–antimatter report also records the Fock-level statements taken from Stage 5 as provisional until the Stage-5 gate has passed; measurement `M4_kreinLevelStatus`.)

### 16.7 What is proved (2): mirror universes and Kohn–Sham pairs

**Theorem T2 (mirror map; PROVED).** Let $u=\sum_av_a\gamma^a$ be a real unit vector of the Clifford algebra that is **space-like**, $n(u)=\eta(v,v)=+1$ (for example $u=\gamma^0$, $\gamma^1$, $\gamma^2$ or $\gamma^3$). Replace the field by $u\Psi$ and, at the same time, the vielbein by the reflected vielbein, in which the frame direction $v$ is reversed (the metric does not change). Then

$$
\mathcal L_{m,\lambda}[\text{reflected frame},\,u\Psi]=\mathcal L_{-m,\lambda}[\text{original frame},\,\Psi],
$$

the energy–momentum tensor is **unchanged**, $T\to+T$, the current is unchanged, $J\to+J$, and the scalar density changes sign, $S\to-S$. Solutions with $(m,\lambda)$ go over into solutions with $(-m,\lambda)$: the **same** coupling.

*Key step.* The scalar density picks up the Pin character of Section 2.14: by Theorem 2.8 with one factor, $u^TCu=-n(u)\,C$, and since $u$ is real, $u^\dagger=u^T$; hence $S=\Psi^\dagger C\Psi\to\Psi^\dagger u^TCu\Psi=-n(u)\,S=-S$ for a space-like $u$. The kinetic term, on the other hand, keeps its sign, because the reflection of the frame supplies a second minus sign that cancels the one from the character (Chapter 6 shows this in flat space, where the frame reflection is the reflection of the coordinate $x_b$; Section 15.5 carries it out in every gravitational field; `pairing-theory.json`, key `T2`, entry `proof`). With $K\to K$ and $S\to-S$, $K-mS-\tfrac\lambda2S^2\to K+mS-\tfrac\lambda2S^2$, which is the Lagrangian with mass $-m$ and the same $\lambda$. For a time-like $u$ the same construction gives a map of the T1 type instead (a table of all eight basis vectors and two general unit vectors is `T2frameTable` in `pairing-theory.json`). Checks: `PAIR_T2frame_twistedSpacelikeMapsToMinusMSameLambda`, `PAIR_T2frame_scalarAndCurrentSigns`, `PAIR_T2frame_characterIsMinusNorm`, `PAIR_T2frame_onShellImage` and the Python family `S5_T2frame`.

**What T2 says about the sign of the mass.** The theory with mass $-m$ in one frame is the theory with mass $+m$ in the reflected frame, with the same energy–momentum tensor and the same charge. Only the scalar density, which itself changes sign under the reflection, distinguishes them. So the sign of the mass has meaning only relative to an orientation of the frame (the exact theory records this reading in `pairing-theory.json`, key `T2z2`, entry `interpretation`). A "universe of mass $-M$" in the sense of T2 is the mirror image of a universe of mass $+M$.

**The mirror universe across the brane** (PROVED in Section 15.6; the checks are listed at the end of this paragraph). In the Z2 geometry of Section 9.16, the static primordial field on $y<0$ glued to its mirror image on $y>0$, the reflection $y\to-y$ is an **isometry**, that is, a map of spacetime to itself that leaves the metric unchanged (here because the metric depends on $y$ only through $|y|$), and it reflects the frame direction 0. Take $u=\gamma^0$ and define $\Psi'(y,x)=\gamma^0\Psi(-y,x)$, where $x$ stands for the other seven coordinates. Then $\Psi$ solves the field equation with $(m,\lambda)$ on $y<0$ exactly when $\Psi'$ solves it with $(-m,\lambda)$ on $y>0$; the energy density and all pressures of $\Psi'$ at $y$ equal those of $\Psi$ at $-y$; the charge density is the same on both sides; the scalar density is opposite. A configuration with $\Psi(-y)=\pm\gamma^0\Psi(y)$ obeys the field equation with one mass function on both sides exactly when that mass function is odd, $m(-y)=-m(y)$: the mirror universe carries the mass $-M$ (Section 13.5 and erratum E4.6 of `handoff/specs/STAGE4_SPEC.md`). The parity conditions of the Kohn–Sham problem of Chapter 13 are of this form, so **every Kohn–Sham state of Chapter 13 is already a pair of universes of masses $+M$ and $-M$ in this mirror sense** (`pairing-theory.json`, key `T3`, entry `stage4Z2Pair`). The checks of this paragraph are

```
PAIR_T2z2_diracOperator    PAIR_T2z2_emtPullback     PAIR_T2z2_currentPullback
PAIR_T2z2_massFunctionMap  PAIR_T2z2_symmetricIffOddMass
```

**Theorem T3 (Kohn–Sham level; PROVED in Section 15.7).** In the static primordial field, with the Kohn–Sham model of Chapter 13 or its counterpart for the commuting field in Chapter 14 (the proof covers both statistics), the $-M$ universe with the **same** coupling $\lambda$ and the tip condition $a(-L)=0$ instead of $b(-L)=0$ (in the bag family of Section 13.5, the angle $\theta=\pi$ instead of $\theta=0$) is the exact image of the $+M$ universe under the block map $\chi\to\sigma_2\chi$, $j\to-j$, which in the real variables of Section 13.14 is the swap $(a,b,j)\to(b,a,-j)$. Its spectra (with multiplicities), occupations, chemical potential, energy, free energy, entropy, Kohn–Sham gap, particle–hole list and Delta-SCF energy are identical to those of the $+M$ universe; its number density and all components of its energy–momentum tensor are identical; its scalar density and effective mass are reversed, $S_p\to-S_p$, $M_{\mathrm{eff}}\to-M_{\mathrm{eff}}$. The self-consistent iteration maps step by step, so the ground state defined by continuation in $\lambda$ and the first excited state map exactly. The image of the $+M$ state under T1 (coupling $-\lambda$, Krein metric $-B$) has the same orbitals and levels but reversed one-body densities and energies: $n\to-n$, $S\to S$, $E\to-E$, $T_{\mu\nu}\to-T_{\mu\nu}$. Checks: the families `PAIR_T3block_*` and `PAIR_T3ks_*` (for example `PAIR_T3ks_sigma2KSOperatorEquivariant`, `PAIR_T3ks_sigma2FunctionalInvariant`, `PAIR_T3ks_imageRuleEnergyOdd`) and the Python families `S5_T3block` and `S5_T3ks`.

**The boundary condition matters (PROVED; Section 15.9 derives the details).** If the $-M$ universe keeps the untransformed tip condition, the pairing fails. The exact theory shows it on the brane zero modes of Section 13.6: with the transformed condition the $-M$ zero mode has the same first-order band splitting $c(M)$ as the $+M$ one, while with the untransformed condition the constant becomes

$$
c_{\mathrm{ctrl}}=e^{-a_{4,0}}\,\frac{2M}{2M+H}\cdot\frac{e^{(2M+H)L}-1}{e^{2ML}-1},\qquad c(M)=e^{-a_{4,0}}\,\frac{2M}{2M-H}\cdot\frac{1-e^{-(2M-H)L}}{1-e^{-2ML}} .
$$

For $M=H=1$, $L=3$, $a_{4,0}=0$: $c(M)=2(1-e^{-3})/(1-e^{-6})=1.905148$ and $c_{\mathrm{ctrl}}=2(e^9-1)/\bigl(3(e^6-1)\bigr)=13.421975$ (`pairing-theory.json`, key `T3`, entry `untransformedBCControl`; checks `PAIR_T3ks_zeroModeUntransformedControl`, `PAIR_T3ks_controlSplittingClosedForm`).

**The pair totals at the Kohn–Sham level** (PROVED; checks `PAIR_totals_ksMirrorPair` and `PAIR_totals_ksKreinImagePair`). For a $+M$ state with $N$ particles above the sea, energy $E_+$ and energy–momentum tensor $T_+$:

- the **mirror pair** ($+M$ universe and the ordinary $-M$ universe of T3): $E_{\mathrm{pair}}=2E_+$, charge $2N$, total scalar density 0, $T_{\mathrm{pair}}=2T_+$;
- the **Krein image pair** ($+M$ universe and its T1 image with $-\lambda$ and $-B$): $E_{\mathrm{pair}}=0$, charge 0, $T_{\mathrm{pair}}=0$ at every point, total scalar density $2S_+$. The image is obtained from the ordinary $-M$ state by reversing the sign of every one-body density and energy (`pairing-theory.json`, key `pairTotals`), so this zero is of the $X+(-X)$ kind discussed in Section 16.6.

**Two kinds of pair.** The theorems therefore produce two different kinds of $\pm M$ pair, and it matters which one is meant:

| property | cancelling pair (T1) | mirror pair (T2, T3) |
| --- | --- | --- |
| partner of $\Psi_+$ | $\gamma^8\Psi_+$ | $u\Psi_+$ with the reflected frame; $\gamma^0\Psi_+(-y)$ across the brane |
| parameters of the partner | $(-m,-\lambda)$ | $(-m,\lambda)$ |
| where the partner lives | at the same points of the same spacetime | reflected; on the other side of the brane |
| energy–momentum of the partner | $-T_+$ | $+T_+$ (reflected) |
| charge of the partner | $-Q_+$ | $+Q_+$ |
| scalar density of the partner | $+S_+$ | $-S_+$ |
| totals of the pair | $T=0$, $Q=0$ | $T=2T_+$, $Q=2Q_+$ |
| quantum reading | image field (metric $-B$): cancels only as $X+(-X)$ within one system; two cancelling universes OPEN | independent field (metric $+B$): energies add |

### 16.8 What is computed

The numerical side of Stage 5 (called T4 in `handoff/specs/STAGE5_SPEC.md`) solves the Kohn–Sham equations of the $+M$ universe, of the $-M$ universe with the transformed tip condition, and of a **control**: the $-M$ universe with the untransformed tip condition. When this chapter was written it was partial. What exists is the following; Section 15.10 gives the complete tables.

**The Rust runs (COMPUTED).** The Rust solver of Chapter 13 has a subcommand `pairs`, whose outputs are committed under `artifacts/dirac16complex/pair-creation/rust/pairs/` for 18 configurations, all for dirac16complex: $m=1$, $L=3$, $N=8$ at $T=0$ with the five couplings $\hat\lambda\in\{0,\pm\hat\lambda_1,\pm\hat\lambda_2\}$; $m=1$, $L=3$, $N=112$ with the same five couplings at $T=0$ and at $T=0.1\,m$; and $m=3$, $L=3$, $N=8$ at $T=0$ with $\hat\lambda\in\{0,\pm\hat\lambda_1\}$. Each run writes a file `pairing.json`. In all 18 runs every level of the $+M$ universe is matched by a level of the $-M$ universe under the level map of T3, with no mismatch of multiplicities; the level energies agree to at most $6.6\times10^{-9}$, and the total energies to at most $1.5\times10^{-8}$ (key `pairingDeviation_plusM_vs_minusM`). Every $+M$ run at $T=0$ reproduces the corresponding Stage-4 run of Chapter 13 bit for bit (key `stage4Reproduction`), and the Stage-4 outputs were left unchanged by the new subcommand (`artifacts/dirac16complex/pair-creation/rust/stage4-identity-report.json`, 9 of 9 checks true). Some pair totals (key `pairTotals`; energies in units of $m$, $m=1$):

| run | $E_+$ | mirror pair $E$ | mirror pair charge | Krein image pair $E$ |
| --- | --- | --- | --- | --- |
| `d16c_m1_L3_N8_lam0_T0` | 0 | 0 | 16 | 0 |
| `d16c_m1_L3_N8_lamp1_T0` | $-9.868332\times10^{-4}$ | $-1.973666\times10^{-3}$ | 16 | $1.3\times10^{-12}$ |
| `d16c_m1_L3_N112_lam0_T0` | 61.090723287 | 122.181446574 | 224 | $-7.3\times10^{-11}$ |
| `d16c_m1_L3_N112_lamp2_T0p1` | 69.806552563 | 139.613105141 | 224 | $-1.5\times10^{-8}$ |

The mirror-pair energy recorded in the file is the sum $E_++E_-$ of the two universes, each computed separately; it equals $2E_+$ up to the small difference between $E_-$ and $E_+$. For the last row, $2\times69.806552563=139.613105126$, which differs from the recorded sum by $1.5\times10^{-8}$. The mirror pair doubles the energy and the charge; the Krein image pair, computed from the $-M$ run by reversing signs (Section 16.7), has zero energy up to the numerical error (at most $1.5\times10^{-8}$ in absolute value over the 18 runs) and zero charge (at most $2.2\times10^{-12}$). The last row is at the temperature $T=0.1\,m$.

**The control (COMPUTED).** Without interaction the control converges and differs from the $+M$ universe, as the exact theory predicts: for $N=8$ its Kohn–Sham gap is $0.1008511$ instead of $0.4307337$ (it is the energy of a bound state that exists only with the untransformed condition, Section 15.9), and for $N=112$ its energy is $56.265496$ instead of $61.090723$ (`d16c_m1_L3_N8_lam0_T0/pairing.json` and `d16c_m1_L3_N112_lam0_T0/pairing.json`, key `universes`, entry `minusM_control`). The controls without interaction at $T=0.1\,m$ and for $m=3$ converge as well and also differ from the $+M$ universe (the files `d16c_m1_L3_N112_lam0_T0p1/pairing.json` and `d16c_m3_L3_N8_lam0_T0/pairing.json`, key `controlOutcome`). With interaction the control was **not run**. Before the first self-consistent update the solver checks that the shift of the levels which that update can cause stays inside its energy window. With the untransformed tip condition the zero modes sit at the tip, where the proper densities are enhanced by $e^{6HL}$, and the bound on the shift exceeds the window in every interacting control (for example 40.34 against 4.59 in `d16c_m1_L3_N8_lamp1_T0/pairing.json`, key `universes`, entry `minusM_control`, field `error`, which begins "not run: the first SCF update violates the window premise of the solver"). So the numerical failure of the pairing with the untransformed condition is shown only in the runs without interaction. That the transformed boundary condition is not a detail, and that without it there is no pairing, rests on the exact control of Section 16.7 (Section 15.9) together with these runs.

**What is not computed.** No Kohn–Sham pair runs of the commuting field dirac16complex00 were made with the Rust solver; the reference solver computed a few of them for $m=3$, $N=112$, and the pairing of that field with interaction is not demonstrated numerically (Chapter 14 lists what exists). The independent reference solver has computed only part of its pair matrix: its summary `artifacts/dirac16complex/pair-creation/reference/reference-pairs-summary.json` records `complete` as false, with 131 runs still pending, and the runs it has finished ($m=3$, $N=112$) do not overlap with the 18 Rust configurations, so no pair run has yet been computed by both solvers. The checker that compares the two solvers, `scripts/check_dirac16complex_pairs.py`, exists, but no report of it is committed; the Stage-5 gate does not exist, and the Stage-5 documents have not been written. The numerical pairing is therefore COMPUTED by one solver, with its own checks; its independent cross-check is OPEN. The exact statements of Sections 16.6 and 16.7 do not depend on these numbers.

### 16.9 What is consistent: no conservation law forbids a cancelling pair

**When a conservation law forbids a transition.** A **conserved quantity** is a number, computed from the state of the system, that does not change in time. It forbids a transition from a state A to a state B exactly when its values in A and B differ. If every conserved quantity has the same value in A and in B, the conservation laws say nothing: they neither forbid the transition nor make it happen. Section 16.4 was an example: charge alone allows a photon to become an electron–positron pair; energy and momentum together forbid it.

**The empty state.** Classically, the empty state is $\Psi_+=\Psi_-=0$ everywhere; every bilinear vanishes, so $T_{\mu\nu}=0$ and $J^\mu=0$. In the quantum theory of the good sector it is the vacuum of Section 8.10, in which the normal-ordered energy, momentum and charge are zero.

**The conserved quantities of the theory.** (a) The **charge** $Q=\int\sqrt{|g|}\,J^{x_4}\,d^7x$ over a slice $x_4=\text{const}$ does not depend on $x_4$, in every gravitational field and for both statistics, because the Lagrangian is invariant under $\Psi\to e^{i\alpha}\Psi$ (Section 5.7 for the principle, Section 8.12 for the current; Theorem M1 of the matter–antimatter document, Section 4.1, gives the complete proof with its machine checks). (b) The **energy–momentum tensor** is conserved in the local sense, $\nabla_\mu T^\mu{}_\nu=0$ on every solution (Chapter 7); Einstein's equations require exactly this of their source (Section 9.9). (c) If the gravitational field does not depend on $x_4$, as the static primordial field does not, the Lagrangian density does not depend on $x_4$ explicitly, and Noether's theorem with the translation of Example 2 of Section 5.7 makes the total **energy** a conserved quantity; the same holds for the momentum along every coordinate on which nothing depends.

**Proposition 16.5 (the cancelling pair is consistent with every conservation law; PROVED for classical fields).** Let $\Psi_+$ be a classical field of the theory $\mathcal L_{m,\lambda}$ and $\Psi_-$ a second, independent classical field of the theory $\mathcal L_{-m,-\lambda}$, in the correlated configuration $\Psi_-=\gamma^8\Psi_+$ (the cancelling pair of Corollary 16.4). In any gravitational field and at any time $x_4$, in particular at $x_4=0$:

1. every density built from $T_{\mu\nu}$ or $J^\mu$ vanishes for the pair at every point, so the pair's charge, and in a static field its energy and momenta, are zero, the values of the empty state; hence **no conservation law forbids a transition from the empty state to the pair**;
2. the gravitational field equations with the pair as their only source, $G^\mu{}_\nu=\kappa\,T^{\mathrm{pair}\,\mu}{}_\nu$ (or the Einstein–Lovelock equations of Section 4.9 with the same right-hand side), are the equations **without any source**: whatever geometry is possible without the pair is also possible with it, and the pair changes nothing in it.

*Proof.* Each member obeys its own field equation, and the two members do not interact, so the conserved quantities of each member are conserved separately, and those of the pair are their sums. By Corollary 16.4 the densities of the two members cancel at every point, so the sums are zero. Item 2 follows because the right-hand side is $\kappa\cdot0=0$. $\square$

This is the precise content of the phrase "the creation of a $\pm M$ pair is consistent with the conservation laws". It is a statement about Q1 of Section 16.3, and for classical fields it is true. Two conditions are built into it: the partner has the coupling $-\lambda$, and it has negative classical energy (Worked example 16.B).

**At the quantum level it is OPEN.** For the quantized field the corresponding statement would need a quantum description of two independent universes whose energies and charges cancel. Section 16.6 showed that neither reading examined in the repository provides one: the image reading cancels only as $X+(-X)=0$ within a single quantum system, and in the independent reading the energies add. Whether the quantum theory admits a cancelling pair of independent universes at all is OPEN.

**Three remarks.**

1. *The idea is old.* That a universe with zero total energy could appear "from nothing" without violating energy conservation was proposed by Tryon (E. P. Tryon, Nature 246, 396 (1973)), and the phrase "creation of universes from nothing" is the title of a paper of Vilenkin (A. Vilenkin, Phys. Lett. B 117, 25 (1982)). What T1 adds is an exact, verified mechanism for the zero: an explicit partner whose energy–momentum tensor is minus that of the original at every point. Zero total energy has never, by itself, produced a rate: that is always a separate calculation.
2. *Consistency is not existence.* Section 16.4 showed conservation laws allowing a process whose probability must still be computed. Proposition 16.5 is of exactly that kind.
3. *The partner must be exact.* The cancellation holds only for $\Psi_-=\gamma^8\Psi_+$ at every point, with the coupling $-\lambda$. Any other configuration of mass $-M$ leaves a remainder. A creation process, if one existed, would have to produce this exact correlation between the two members.

**The mirror pair is not consistent with the conservation laws unless it is neutral (PROVED).** For the mirror pair of T2 and T3 the partner has the same charge as the original (Section 16.7), so the pair has the charge $2Q_+$. The charge is exactly conserved and the empty state has charge 0; therefore a mirror pair can appear from the empty state only if $Q_+=0$. In a static field the same argument with the energy requires $E_+=0$. Every Kohn–Sham state of Chapter 13 has the charge $N=8$, 112 or 1016 (its particle number), so no computed Kohn–Sham mirror pair could appear from the empty state: the free state with $N=8$ has $E_+=0$, but its mirror pair has the charge 16 (Section 16.8). An independently quantized partner in a state of opposite charge (made of antiparticles) would cancel the charge, but that is an additional assumption about its state, and its energy would still add (the matter–antimatter document, Section 7.3). In a gravitational field that changes with time, the energy is not conserved (the expanding universes of Chapter 11 create particle pairs of positive energy, Section 11.11), and only the charge constrains a mirror pair.

### 16.10 Zero total source against the source that the primordial field needs

A cancelling pair is invisible to gravity (Proposition 16.5, item 2). The notebook, however, wants the pair to be created in its own primordial gravitational field. The two statements have to be put side by side.

**Proposition 16.6 (a cancelling pair cannot produce the primordial field; PROVED).** Suppose that a T1 pair is the only matter and that gravity obeys the eight-dimensional Einstein equations, with or without a cosmological constant $\Lambda$. Then no member of the notebook's primordial family of metrics is a solution, whatever the function $a_4$.

*Proof.* By Corollary 16.4 the equations become $G^\mu{}_\nu+\Lambda\,\delta^\mu{}_\nu=0$ (Section 4.8 writes $G_{\mu\nu}+\Lambda g_{\mu\nu}=\kappa T_{\mu\nu}$; raising one index gives this mixed form). For $\Lambda=0$ this fails because $G^4{}_4=3H^2(7+a_4'^2)\ge21H^2>0$ (Section 9.8). For $\Lambda\ne0$ all eight diagonal components of $G^\mu{}_\nu$ would have to be equal to $-\Lambda$; already $G^0{}_0=G^4{}_4$ means $-3H^2(a_4'^2-5)=3H^2(7+a_4'^2)$, that is $15-3a_4'^2=21+3a_4'^2$, that is $a_4'^2=-1$, impossible for a real function. For the static member ($a_4'=a_4''=0$), $G^\mu{}_\nu=\mathrm{diag}(15,15,15,15,21,15,15,15)\,H^2$ (Section 9.15), and $15H^2+\Lambda=0$ and $21H^2+\Lambda=0$ cannot both hold. $\square$

So a pair with zero total energy–momentum is compatible only with a gravitational field that needs no source, while the primordial field of the notebook needs one: in Einstein gravity $\rho_{\mathrm{req}}=-3H^2(7+a_4'^2)/\kappa<0$, and for the static member $\rho_{\mathrm{req}}=-21H^2/\kappa$, $p_{\mathrm{req}}=+15H^2/\kappa$ (Sections 9.10 and 9.15). There are two ways to read the notebook's picture, and each must be stated honestly.

**Reading A: the cancelling pair lives in a geometry that something else produces.** The pair then adds nothing to the source, and the geometry is whatever the other matter makes it. For the static primordial field, the candidates for that other matter are:

- an $x_0$-independent condensate of dirac16complex, which is an exact source if and only if its three-gamma bilinears vanish, $mS=-36H^2/\kappa$ and $\lambda S^2=30H^2/\kappa$ (Proposition 9.4 and Section 9.15; PROVED in the mean-field reading); its energy density is negative, and whether such a state is realized or stable is OPEN;
- the Kohn–Sham states of Chapter 13, which do **not** qualify: every state with band or bulk levels has a positive average energy density, for example $\langle\rho\rangle=0.0230891$ for $N=112$ without interaction, which would need the negative coupling $\kappa=-909.5$ (COMPUTED; `artifacts/dirac16complex/kohn-sham/rust/emt/emt-summary.csv`; Section 13.14), and the sourcing conditions are met in no computed run;
- the Lovelock terms of orders 2 and 3: if some choice of the notebook's constants $w_1,w_2,w_3,\Lambda$ made the field a solution of the **vacuum** Einstein–Lovelock equations, which is what the notebook's cell 14 writes down, then a cancelling pair would fit it exactly. Nobody has computed these terms for this field (Section 4.9), so this is OPEN.

In reading A the pair is allowed, but it plays no role in producing the universe it lives in.

**Reading B: the two universes are the two halves of the Z2 geometry.** This is the reading that Stage 4 built as a model of the notebook's picture (Section 9.16, status ASSUMED). The partner is the mirror universe of T2 on the other side of the brane. Nothing cancels: the energy density of the $-M$ half at $y$ equals that of the $+M$ half at $-y$, the charges are equal, and each half needs the negative bulk source $\rho_{\mathrm{req}}=-21H^2/\kappa$, while the brane needs the positive surface energy density $12H/\kappa$ and the surface pressure $-10H/\kappa$ (Section 9.16, PROVED as requirements of the geometry). No computed state supplies the bulk source (Chapter 13), and the matter on the brane is not derived from anything (OPEN).

| property | reading A (cancelling pair) | reading B (mirror pair across the brane) |
| --- | --- | --- |
| pairing theorem | T1 (with $-\lambda$; classical fields) | T2 and T3 (same $\lambda$) |
| total energy–momentum of the pair | 0 at every point | twice that of one universe |
| total charge of the pair | 0 | twice that of one universe |
| appearance from the empty state | allowed by every conservation law (classical fields; quantum level OPEN) | forbidden unless each universe is neutral (and, in a static field, of zero energy) |
| what the gravitational field needs | a separate source, or a vacuum Einstein–Lovelock solution (OPEN) | $\rho_{\mathrm{req}}<0$ in each half and a brane stress, not supplied by any computed state |
| status of the picture | consistent, not derived | a chosen model (ASSUMED), its sources OPEN |

In neither reading is the notebook's field produced by a pair of universes. In reading A the pair is allowed by all the conservation laws but does not act on the geometry. In reading B the pair is the mirror structure of the geometry itself, and that structure needs sources that the theory has not supplied.

### 16.11 What is not derived

The following items are not derived anywhere in the notebook or the project. Each is OPEN unless stated otherwise.

1. **No creation process.** The field equations of the $+M$ and $-M$ members are separate equations; no term of the theory couples them, and gravity, in reading A, sees only their sum, which is zero. There is no equation whose solution describes a transition from a state without universes to a state with a pair. For classical fields such a transition is even excluded within every setting in which the book can decide it (Proposition 16.7 below).
2. **No rate, probability or amplitude.** Section 16.12 lists what their calculation would need.
3. **No wave function of the universe.** The notebook's file name speaks of a "wave function of the universe", and a section title of the notebook (cell 308, according to the survey) introduces "the wave function, Ψ16, for this Universe": the notebook uses the phrase for the classical field $\Psi_{16}$ itself. In quantum cosmology the phrase means something else: a quantum state of the geometry together with the matter fields, as in the proposal of Hartle and Hawking (J. B. Hartle and S. W. Hawking, Phys. Rev. D 28, 2960 (1983)). According to its survey, the notebook contains no field quantization (only classical fields and single-particle wave functions), and the project quantizes only the matter field in a prescribed geometry (Chapter 8). A wave function of the universe in the quantum-cosmology sense exists in neither.
4. **No dynamical big bang.** The metric is prescribed (ASSUMED), its function $a_4$ is free, and the moment $x_4=0$ is regular (Proposition 16.8 below). Nothing in the field marks a beginning.
5. **No selection of pairs.** T1 to T3 hold for every solution. They say that every universe of mass $+M$ has an allowed partner of mass $-M$; they do not say that the partner is present (Section 16.3).
6. **Nothing singles out $x_4=0$.** T1 holds at every time $x_4$. In the static field, used by Chapters 13 and 15, nothing depends on $x_4$ at all; for the notebook's choice $a_4=t$, the moment $x_4=0$ is only the moment at which $a_4=0$.
7. **No value of $M$, and no relation between $H$ and $M$.** The mass is a free parameter, and the relation "H = some function of M" hoped for in cell 23 is not derived.
8. **No solution of the matter–antimatter problem.** The pairing theorems do not create charge. The charge of each universe is exactly conserved in every gravitational field (Theorem M1), and each field has an exact symmetry that reverses the charge, charge conjugation for dirac16complex00 and a CP-type symmetry for dirac16complex (Theorem M2), so two of Sakharov's three conditions for producing an excess of matter fail; the theory contains no baryons of the Standard Model, and no departure from equilibrium is computed (PROVED and stated in Chapter 17, which follows the matter–antimatter analysis `provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md`). A cancelling pair with opposite charges is consistent with these laws; that it explains the observed excess of matter is not established.

**Proposition 16.7 (a classical field cannot appear from nothing; PROVED in the setting stated).** Consider a classical field of the good sector described by finitely many mode amplitudes, collected in a column $u(x_4)$, that obeys

$$
i\,\frac{du}{dx_4}=F(u,x_4),
$$

where $F$ is a smooth function of $u$ with $F(0,x_4)=0$ for every $x_4$. This covers one mode in flat space, $F=h_ku$ with the constant matrix of Section 8.9; the modes in the expanding universes of Chapter 11, $F=h(x_4)u$ with a matrix that changes with time; and any finite set of coupled modes with the interaction $\lambda S\Psi$, which is of third order in $u$. If $u=0$ at one time, then $u=0$ at all times.

*Proof.* The constant function $u(x_4)=0$ is a solution, because $F(0,x_4)=0$. By the existence and uniqueness theorem of Picard and Lindelöf (Section 10.2, quoted there), it is the only solution with the value 0 at the initial time. $\square$ (For a constant matrix the solution is explicit, $u(x_4)=e^{-ih_kx_4}u(0)$, Section 8.9, and $u(0)=0$ gives $u=0$ at once.)

So, within the classical theory, a pair cannot arise from the empty configuration by the field equations. It must either be present in the initial data (and then it is not created), or the equations must break down at an initial singular moment (which the notebook's field does not have, by Proposition 16.8), or the equations must be changed. Two limits of this statement: it concerns classical fields, and quantum fields behave differently (the vacuum of EXP-4b creates pairs, Section 16.5); and for the full field equation in 4+4 dimensions, whose initial-value problem is not well posed outside the good sector (Section 8.9), no uniqueness theorem is proved in this book.

**Proposition 16.8 (the notebook's field is regular at $x_4=0$; PROVED).** For every smooth function $a_4$, on the notebook's chart $0<z<\pi/2$, the metric of Section 9.2 is smooth and non-degenerate at every finite time $x_4$, in particular at $x_4=0$: its eight diagonal entries are finite and nonzero, $\det g=+\cos^2z\ne0$, and its Ricci scalar $R=6H^2(a_4'^2-7)$ is finite.

*Proof.* The entries are $\cot^2z$, $s^{1/3}e^{\pm2a_4}$ and $-1$ with $s=\sin z$ (Section 9.2); on the chart $\cot z$ and $s$ are positive and finite, and $e^{\pm2a_4}$ is positive and finite whenever $a_4$ is finite. The determinant is $\cos^2z$ (Section 9.3) and the Ricci scalar is $6H^2(a_4'^2-7)$ (Section 9.8), finite whenever $a_4'$ is. $\square$

For the notebook's example $a_4=t$ the scale factor of 3-space, $s^{1/6}e^{Hx_4}$, tends to zero only as $x_4\to-\infty$, never at a finite time. The field therefore has no big-bang singularity at $x_4=0$ or at any other finite time on its chart. (Its chart ends at $z=\pi/2$, where only the coordinate $x_0$ degenerates, and at the tip $z\to0$, which lies at infinite proper distance; Sections 9.5 and 9.16.)

### 16.12 What a calculation of pair creation would require

Questions Q2 and Q3 of Section 16.3 can be attacked in two ways. Both are OPEN; this section lists what each would need, so that a student can see where the missing work lies (Chapter 18 collects the open problems).

**The classical route (Q2).** One would need a solution of the coupled system: the field equations of both members together with Einstein's (or the Einstein–Lovelock) equations, whose source is the total energy–momentum tensor, so that the metric is **computed** rather than prescribed. By Proposition 16.7 a classical pair cannot grow out of zero fields, so the solution would have to start from a genuinely singular moment, at which the geometry degenerates and the equations lose their meaning, together with a rule for what emerges from it. Such a rule is an initial condition, not a derivation. The notebook's metric has no such moment (Proposition 16.8). The classical route can therefore describe at most how a pair that is already there evolves.

**The quantum route (Q3).** Here the analogue of Section 16.5 is needed, one level up:

1. **A space of states with different numbers of universes**, containing a state with no universe and states with one universe or with a pair. In quantum cosmology the corresponding object is a wave function of the geometry and the matter fields, which obeys the Wheeler–DeWitt equation (B. S. DeWitt, Phys. Rev. 160, 1113 (1967)); the proposals of Hartle and Hawking and of Vilenkin cited in Sections 16.9 and 16.11 are of this kind. Nothing of this exists in the project, which quantizes only the matter field in a prescribed geometry.
2. **A probability interpretation.** Probabilities need a positive inner product. The canonical state space of dirac16complex is a Krein space, and a positive Fock space exists only in the good sector (Chapter 8). For the cancelling pair no quantum description with two independent universes is known (Section 16.6), so this item is not a formality.
3. **A dynamics that connects the states:** an interaction term, or a time-dependent background, whose matrix element between the empty state and the pair state is not zero. In the theory as built nothing couples the two members, and gravity sees only their total, which vanishes.
4. **The amplitude and what follows from it:** the amplitude $\langle\text{pair}|\,U\,|\text{empty}\rangle$ of the evolution operator $U$, the probability $|\langle\text{pair}|U|\text{empty}\rangle|^2$, and a rate, which could then be compared with the number $na^3=4.412\times10^{-3}H_{\mathrm{inf}}^3$ that EXP-4b computes for particle pairs.
5. **An answer to the stability question.** If a quantum theory contained an independent universe of mass $-M$ with negative energies, so that pairs of zero total energy could be created by some interaction, energy conservation would not limit their number, since every configuration of the $+M$ member would have a partner with the opposite energy. In ordinary quantum field theory, quanta of negative energy that interact with quanta of positive energy are known to make the empty state unstable (J. M. Cline, S. Jeon and G. D. Moore, Phys. Rev. D 70, 043543 (2004)). A calculation of pair creation in the cancelling reading would have to face this question; it has not been examined here.
6. **Numbers.** The mass $M$, the length scale $1/H$, the gravitational coupling $\kappa$ and the coupling $\lambda$ would have to be fixed. The theory as built does not fix any of them.

**The photon analogy, completed.**

| ingredient | photon near a nucleus | pair of universes of masses $\pm M$ |
| --- | --- | --- |
| conservation laws satisfied? | yes, above the threshold of Proposition 16.3 | yes, for a cancelling pair of classical fields (Proposition 16.5); quantum level OPEN |
| something to take up momentum or energy | the nucleus | not needed: all totals are zero |
| dynamics connecting initial and final states | quantum electrodynamics | none in the theory |
| computed probability | the Bethe–Heitler cross section (literature) | none (OPEN) |

The first two lines are where the pairing theorems stand. The last two are the missing step.

### 16.13 The ledger of this chapter

| statement | status | where verified |
| --- | --- | --- |
| "At $x_4=0$ a pair of universes of masses $\pm M$ is created" (notebook, cells 6, 7 and 17) | HYPOTHESIS | `handoff/surveys/survey_notebook-physics.md`; Section 16.2 |
| The primordial metric and its function $a_4$ | ASSUMED (prescribed) | Chapter 9 |
| A single photon cannot create a pair; the threshold near a nucleus | PROVED (from standard kinematics) | Section 16.4 |
| An expanding universe creates particle pairs: $na^3=4.412\times10^{-3}H_{\mathrm{inf}}^3$ for $m=H_{\mathrm{inf}}$ | COMPUTED | `artifacts/dirac16complex/numerics/exp4/summary.json`; Section 11.11 |
| T1: $\mathcal L_{m,\lambda}[\gamma^8\Psi]=-\mathcal L_{-m,-\lambda}[\Psi]$, $T\to-T$, $J\to-J$, both statistics, every gravitational field | PROVED | `PAIR_T1generic_*`, `PAIR_T1grassmann_*`, `PAIR_T1jets_*`, `PAIR_T1primordial_*`; `ALG_gamma8Map`; Section 16.6 |
| Corollary 16.4: the cancelling pair has $T=0$, $J=0$ at every point and every $x_4$ | PROVED | `PAIR_T1jets_pairEMTAndCurrentVanish`, `PAIR_totals_fieldLevelChiralPair`; Section 16.6 |
| Quantum level: the image field cancels only as $X+(-X)$ within one quantum system; an independently quantized partner adds | PROVED (Fock level cited from Stage 5, provisional until its gate) | `PAIR_T1krein_*`; `MA_M4_kreinOneParticle`; Section 16.6 |
| A quantum description of two independent universes whose energies and charges cancel | OPEN | Section 16.6 |
| T2: space-like reflection gives $(m,\lambda)\to(-m,\lambda)$ with $T\to+T$, $J\to+J$; the mirror universe across the brane | PROVED | `PAIR_T2frame_*`, `PAIR_T2z2_*`; Section 16.7 |
| T3: the Kohn–Sham states of the $+M$ and $-M$ universes coincide with the transformed tip condition; the pairing fails without it | PROVED | `PAIR_T3block_*`, `PAIR_T3ks_*`; Section 16.7 |
| Kohn–Sham pair totals: mirror pair $2E_+$, charge $2N$; Krein image pair 0 | PROVED; COMPUTED in 18 Rust runs | `PAIR_totals_ksMirrorPair`, `PAIR_totals_ksKreinImagePair`; `rust/pairs/*/pairing.json`; Section 16.8 |
| Independent cross-check of the pair numerics; Kohn–Sham pair runs of dirac16complex00 | OPEN | `reference/reference-pairs-summary.json`; Section 16.8 |
| No conservation law forbids the appearance of a cancelling pair of classical fields (Proposition 16.5) | PROVED (partner with $-\lambda$ and negative classical energy) | Section 16.9 |
| A mirror pair with nonzero charge cannot appear from the empty state | PROVED | Section 16.9 |
| A cancelling pair cannot produce the primordial field in Einstein gravity (Proposition 16.6) | PROVED | Section 16.10 |
| The primordial field solves the vacuum Einstein–Lovelock equations for some couplings | OPEN | Sections 4.9 and 16.10 |
| A classical field of the good sector cannot appear from zero (Proposition 16.7) | PROVED | Section 16.11 |
| The notebook's field is regular at $x_4=0$ (Proposition 16.8) | PROVED | Section 16.11 |
| A creation process, rate, amplitude or wave function of the universe; a dynamical big bang | OPEN | Sections 16.11 and 16.12; Chapter 18 |
| "The big bang creates universes in pairs" | HYPOTHESIS: consistent with the conservation laws for classical cancelling pairs, not derived | this chapter |

### 16.14 What we proved and what we assumed

**Proved in this chapter** (with the complete argument given here, or with the key steps given here and the complete proof in Chapter 15, and in every case with the exact machine checks named): the kinematics of pair creation by light, namely that a single photon in empty space cannot make an electron–positron pair, that near a nucleus of mass $M_N$ the conservation laws allow it exactly when $E_\gamma\ge2m(1+m/M_N)$, and that two head-on photons need $E_aE_b\ge m^2$ (Lemma 16.1, Propositions 16.2 and 16.3); theorem T1, $\mathcal L_{m,\lambda}[\gamma^8\Psi]=-\mathcal L_{-m,-\lambda}[\Psi]$ with $E\to-\gamma^8E$, $T_{\mu\nu}\to-T_{\mu\nu}$ and $J^\mu\to-J^\mu$, for both statistics in every gravitational field, and its reading as a reversal of the frame; Corollary 16.4, the cancelling pair with $T^{\mathrm{pair}}_{\mu\nu}=0$ and $J^{\mathrm{pair}}=0$ at every point and every $x_4$; the rest-frame worked examples, which show the cancellation and show that the classical energy of dirac16complex00 has no fixed sign; the two quantum readings of the partner, of which the image field with the Krein metric $-B$ cancels only as an identity $X+(-X)=0$ within one quantum system and the independently quantized field adds; theorem T2, the mirror map $(m,\lambda)\to(-m,\lambda)$ with $T\to+T$ and $J\to+J$, and the mirror universe of mass $-M$ across the brane; theorem T3 and the Kohn–Sham pair totals (the mirror pair doubles energy and charge; the Krein image pair has zero energy, charge and energy–momentum, a zero of the $X+(-X)$ kind); the consistency of the cancelling pair of classical fields with every conservation law and with the source-free gravitational equations (Proposition 16.5); that a mirror pair with nonzero charge cannot appear from the empty state; that a cancelling pair cannot produce any member of the primordial family in Einstein gravity, with or without a cosmological constant (Proposition 16.6); that a classical field of the good sector described by finitely many modes cannot appear from zero (Proposition 16.7); and that the notebook's field is regular at $x_4=0$ and at every finite time (Proposition 16.8).

**Computed:** the particle pairs created by an expanding universe (EXP-4b, Section 11.11), which serve as the model of a creation calculation; the Kohn–Sham pair runs of the Rust solver for dirac16complex (18 configurations), which reproduce the $+M$ universe in the $-M$ universe to at most $1.5\times10^{-8}$ in the energy, give the mirror and Krein image pair totals, and show that the pairing fails with the untransformed tip condition; the average energy densities of the Kohn–Sham states of Chapter 13, which are positive.

**Assumed or quoted:** the conservation of energy and momentum and the relation $E^2=m^2+|\mathbf p|^2$ of special relativity; the literature on pair-creation cross sections, on gravitational particle creation, on zero-energy universes, on the wave function of the universe and on the instability caused by negative-energy quanta, all cited and none used as a result; the theorem of Picard and Lindelöf (Section 10.2); the prescribed primordial metric and its free function $a_4$ (Chapter 9); the Z2 gluing of Stage 4 as a model of the notebook's picture (Section 9.16); the Kohn–Sham model of Chapter 13 with its approximations; the mean-field reading of the bilinears in the source analysis of Chapter 9; and the defining assumptions of the cancelling pair: two independent classical fields in the correlated configuration $\Psi_-=\gamma^8\Psi_+$, the partner with the coupling $-\lambda$ (and hence with negative classical energy).

**Open:** a creation process, a rate, a probability amplitude, a wave function of the universe in the sense of quantum cosmology, a dynamical big bang; a quantum description of two independent universes of masses $\pm M$ whose energies and charges cancel; whether the primordial field solves the vacuum Einstein–Lovelock equations for some couplings; the sources of the Z2 geometry (bulk and brane); the independent cross-check of the Kohn–Sham pair numerics and the pair runs of dirac16complex00.

**Hypothesis:** that the big bang creates universes of masses $\pm M$ in pairs. The pairing theorems make the creation of a cancelling pair of classical fields consistent with every conservation law; they do not derive it. In the words of Stage 1, the pairing is "a structural property of the equations, not a claim that universes of masses $\pm M$ are created in pairs".

### 16.15 Exercises

**Exercise 16.1.** Give each statement one of the five status words of Section 0.3, with one sentence of reason. (a) For a T1 pair in the static primordial field, $T^{\mathrm{pair}}_{\mu\nu}=0$ at $x_4=0$. (b) At $x_4=0$ a pair of universes of masses $\pm M$ is created. (c) The probability per unit time that a pair of universes is created. (d) In the Rust run `d16c_m1_L3_N112_lam0_T0` the mirror pair has the energy 122.181447. (e) The two halves of the Z2 geometry are glued at $y=0$.

**Exercise 16.2.** Two electrons ($m=1$) have the momenta $\mathbf p_1=(3,0,0)$ and $\mathbf p_2=(0,4,0)$. Compute $E_1$, $E_2$ and the invariant mass squared of the pair, and check Lemma 16.1.

**Exercise 16.3.** Show that a single photon cannot turn into one neutral particle of mass $\mu>0$, and that such a particle, at rest, cannot decay into a single photon.

**Exercise 16.4.** Complete the proof of Proposition 16.3: for $E_\gamma\ge2m(1+m/M_N)$, construct momenta of the electron, the positron and the nucleus, all along the direction $\mathbf n$ of the photon, with the initial total energy $E_\gamma+M_N$ and the initial total momentum $E_\gamma\mathbf n$. (Hint: give the electron and the positron the momenta $(q+r)\mathbf n$ and $(q-r)\mathbf n$, the nucleus $(E_\gamma-2q)\mathbf n$, choose $q=mE_\gamma/(2m+M_N)$, and vary $r\ge0$.)

**Exercise 16.5.** In units $m=1$: (a) compute the threshold of Proposition 16.3 for $M_N=4$ and for $M_N=1836$. (b) Two photons collide head-on, one with $E_a=3$. How large must $E_b$ be at least? (c) If the two photons have equal energies, how large must each be?

**Exercise 16.6.** Using the tables of Section 2.9 ($C$: row 1 reads $-5$, row 5 reads $-1$, row 8 reads $+12$, row 12 reads $+8$; $B/i$: row 1 reads $-8$, row 5 reads $+12$, row 8 reads $+1$, row 12 reads $-5$), compute $S=\Psi^\dagger C\Psi$ and $J^4=\Psi^\dagger B\Psi$ for $\Psi=e_1+e_5+i\,e_8$ and for $\gamma^8\Psi$.

**Exercise 16.7.** In flat space with $\lambda=0$ and $m>0$, let $\Psi=\tfrac1{\sqrt2}(u_++u_-)\,e^{-imx_4}$ with the rest states $u_\pm$ of Section 8.8. Show that $\Psi$ solves the field equation with mass $m$, and compute its classical energy density $\rho$, its charge density $J^4$ and its scalar density $S$. What does the result say about "zero total energy" as a property of pairs?

**Exercise 16.8.** The file

```
artifacts/dirac16complex/pair-creation/rust/pairs/d16c_m1_L3_N112_lam0_T0/pairing.json
```

gives $E_+=61.090723$ for the $+M$ universe with $N=112$ particles. What are the energy and the charge of the mirror pair and of the Krein image pair? Which of the two may appear from the empty state in the static field, as far as the conservation laws are concerned?

**Exercise 16.9.** Show directly that the static primordial field cannot be produced by a T1 pair together with a cosmological constant: which value of $\Lambda$ would the component $G^0{}_0$ require, and which the component $G^4{}_4$?

**Exercise 16.10.** For the notebook's choice $a_4=t$, at the point with $\sin z=3/5$ and with $H=1$: write down the diagonal of the metric at $x_4=0$ and at $x_4=-10$, and the Ricci scalar. When does the scale factor of 3-space vanish?

**Exercise 16.11.** Let $h(t)=t\,\sigma_x$ with the Pauli matrix $\sigma_x$ of Section 2.3. (a) Show that $u(t)=\bigl(\cos\tfrac{t^2}2,\,-i\sin\tfrac{t^2}2\bigr)^T$ solves $i\,\dot u=h(t)u$ with $u(0)=(1,0)^T$. (b) Show that $u^\dagger u$ is constant. (c) Which solution has $u(0)=0$, and why is it the only one?

**Exercise 16.12.** (a) Assuming $K\to K$ and $S\to-S$ (the map of T2), show that $\mathcal L_{m,\lambda}$ goes over into $\mathcal L_{-m,\lambda}$. (b) Assuming $K\to-K$ and $S\to S$ (the map of T1), show that it goes over into $-\mathcal L_{-m,-\lambda}$. (c) Explain why no map with $K\to-K$ and $S\to S$ can turn $\mathcal L_{m,\lambda}$ into $-\mathcal L_{-m,\lambda}$ when $\lambda\ne0$.

**Exercise 16.13.** Repeat the table of Section 16.6 for a quantum in the rest mode $u_-$ of Section 8.8 (Krein sign $-1$): compute $(E,Q,S)$ in the $+M$ universe, for the image partner and for the independent partner. Compare the energy with the classical energy density $m\,u_-^\dagger Bu_-$.

### 16.16 Answers to the exercises

**Answer 16.1.** (a) PROVED: it is Corollary 16.4, which holds for the two classical fields of a cancelling pair in every gravitational field at every $x_4$. (b) HYPOTHESIS: it is the notebook's claim; nothing in the project derives it. (c) OPEN: no calculation of such a probability exists (Section 16.12). (d) COMPUTED: it is a floating-point result of the Rust solver, recorded in the file's key `pairTotals`. (e) ASSUMED: the Z2 gluing is a construction chosen by Stage 4 to model the notebook's picture, not a result of any equation (Section 9.16).

**Answer 16.2.** $E_1=\sqrt{1+9}=\sqrt{10}\approx3.1623$ and $E_2=\sqrt{1+16}=\sqrt{17}\approx4.1231$. The total momentum is $(3,4,0)$ with $|\mathbf p_1+\mathbf p_2|^2=25$. So $\mu^2=(\sqrt{10}+\sqrt{17})^2-25=10+17+2\sqrt{170}-25=2+2\sqrt{170}\approx28.08$. Lemma 16.1 requires $\mu^2\ge(1+1)^2=4$, which holds; equality would need equal velocities (Exercise 16.4), and these two electrons move in different directions.

**Answer 16.3.** A photon has $\mu^2=E^2-|\mathbf p|^2=0$; one particle of mass $\mu$ has $\mu^2>0$. Since the invariant mass squared is conserved, $0=\mu^2$ is impossible. The decay is the same statement read backwards: the particle at rest has $E=\mu$ and $\mathbf p=0$, so $E^2-|\mathbf p|^2=\mu^2>0$, while one photon has 0.

**Answer 16.4.** Write $P=E_\gamma$ and $\mu_0=2m+M_N$. The total momentum is $(q+r)+(q-r)+(P-2q)=P$ for every $q$ and $r$. The total energy is the continuous function

$$
f(r)=\sqrt{m^2+(q+r)^2}+\sqrt{m^2+(q-r)^2}+\sqrt{M_N^2+(P-2q)^2}.
$$

With $q=mP/\mu_0$ the nucleus has the momentum $P-2q=M_NP/\mu_0$, so every body has momentum proportional to its mass, and $f(0)=\frac{m}{\mu_0}\sqrt{\mu_0^2+P^2}+\frac{m}{\mu_0}\sqrt{\mu_0^2+P^2}+\frac{M_N}{\mu_0}\sqrt{\mu_0^2+P^2}=\sqrt{\mu_0^2+P^2}$. As $r$ grows, $f(r)$ grows without bound. By the intermediate value theorem $f$ takes every value between $f(0)$ and infinity, so a value $r\ge0$ with $f(r)=E_\gamma+M_N$ exists provided $\sqrt{\mu_0^2+E_\gamma^2}\le E_\gamma+M_N$. Squaring, this is $(2m+M_N)^2\le M_N^2+2E_\gamma M_N$, which is exactly the threshold condition $E_\gamma\ge2m(1+m/M_N)$. For two photons the same construction with the pair alone ($\mu_0=2m$, $P=E_a-E_b$, $q=P/2$) works exactly when $4m^2+(E_a-E_b)^2\le(E_a+E_b)^2$, that is $E_aE_b\ge m^2$.

**Answer 16.5.** (a) $2(1+\tfrac14)=2.5$ and $2(1+\tfrac1{1836})\approx2.00109$. (b) $E_b\ge m^2/E_a=\tfrac13$. (c) $E^2\ge1$, so each photon needs at least $E=1=m$: two photons of equal energy must each bring one rest energy.

**Answer 16.6.** For $\Psi$: $(C\Psi)_1=-\Psi_5=-1$, $(C\Psi)_5=-\Psi_1=-1$, $(C\Psi)_8=\Psi_{12}=0$, so $S=1\cdot(-1)+1\cdot(-1)+(-i)\cdot0=-2$. $(B\Psi)_1=-i\Psi_8=-i\cdot i=1$, $(B\Psi)_5=i\Psi_{12}=0$, $(B\Psi)_8=i\Psi_1=i$, so $J^4=1\cdot1+1\cdot0+(-i)\cdot i=1+1=2$ (with $\Psi_8^\ast=-i$). For $\gamma^8\Psi=-e_1-e_5+i\,e_8$ (the components 1 and 5 lie in the upper half and change sign): $(C\gamma^8\Psi)_1=1$, $(C\gamma^8\Psi)_5=1$, so $S=(-1)(1)+(-1)(1)=-2$; $(B\gamma^8\Psi)_1=-i\cdot i=1$, $(B\gamma^8\Psi)_8=i\cdot(-1)=-i$, so $J^4=(-1)(1)+(-i)(-i)=-1-1=-2$. The scalar density is unchanged and the charge density changes sign, as T1 requires.

**Answer 16.7.** Both $u_+$ and $u_-$ satisfy $-i\gamma^4u_\pm=u_\pm$ (Section 8.8), so $\gamma^4\partial_4\Psi=-im\gamma^4\Psi=m\Psi$: $\Psi$ solves the field equation with mass $m$ and has frequency $\varepsilon=m$. From Section 8.8, $Bu_+=u_+$, $Bu_-=-u_-$, $Cu_+=u_+$, $Cu_-=-u_-$, and $u_\pm^\dagger u_\pm=1$; one also checks $u_+^\dagger u_-=\tfrac14\bigl(1\cdot1+(-1)\cdot1+(i)(i)+(i)(-i)\bigr)=0$. Hence $B(u_++u_-)=u_+-u_-$ and $(u_++u_-)^\dagger(u_+-u_-)=1-1+u_-^\dagger u_+-u_+^\dagger u_-=0$, so $J^4=0$ and, by the formula of Worked example 16.B, $\rho=m\,\Psi^\dagger B\Psi=0$. In the same way $C(u_++u_-)=u_+-u_-$ gives $S=0$. A single classical universe of mass $m$ can have zero energy density and zero charge density. For the classical field, zero total energy is therefore not a property that singles out pairs; what T1 adds is the exact cancellation of every component of the energy–momentum tensor between a configuration and its partner.

**Answer 16.8.** Mirror pair: $E=2\times61.090723=122.181447$ and charge $2\times112=224$ (the file's `pairTotals.mirrorPair` agrees). Krein image pair: $E=0$ (the file records $-7.3\times10^{-11}$, the numerical error) and charge 0. The empty state has energy 0 and charge 0. The mirror pair differs in both, so energy conservation (in the static field) and charge conservation forbid its appearance from the empty state. The Krein image pair agrees in both, but its zero is of the form $X+(-X)$: the image is the same quantum system as the $+M$ universe (Section 16.6). So it shows no more than the classical statement of Proposition 16.5, and whether two independent quantum universes can cancel is OPEN. Allowed, in any case, does not mean that it happens.

**Answer 16.9.** With a T1 pair as the only matter, the equations are $G^\mu{}_\nu+\Lambda\delta^\mu{}_\nu=0$. For the static field $G^0{}_0=15H^2$ requires $\Lambda=-15H^2$, and $G^4{}_4=21H^2$ requires $\Lambda=-21H^2$. One constant cannot have both values.

**Answer 16.10.** At $\sin z=3/5$: $\cot^2z=16/9$ and $s^{1/3}=(3/5)^{1/3}\approx0.8434$. At $x_4=0$, $a_4=0$ and the diagonal is $(16/9,\ 0.8434,\ 0.8434,\ 0.8434,\ -1,\ -0.8434,\ -0.8434,\ -0.8434)$. At $x_4=-10$, $a_4=-10$, $e^{2a_4}=e^{-20}\approx2.061\times10^{-9}$ and $e^{-2a_4}\approx4.852\times10^{8}$, so the diagonal is $(16/9,\ 1.738\times10^{-9}\ (\times3),\ -1,\ -4.092\times10^{8}\ (\times3))$: very different, but finite and nonzero. The Ricci scalar is $6(1-7)=-36$ at every time. The scale factor of 3-space, $s^{1/6}e^{x_4}$, is positive at every finite time and tends to 0 only as $x_4\to-\infty$: there is no moment at which it vanishes.

**Answer 16.11.** (a) $\dot u=\bigl(-t\sin\tfrac{t^2}2,\ -it\cos\tfrac{t^2}2\bigr)^T$, so $i\dot u=\bigl(-it\sin\tfrac{t^2}2,\ t\cos\tfrac{t^2}2\bigr)^T$. And $h(t)u=t\,\sigma_xu$ exchanges the two components: $t\bigl(-i\sin\tfrac{t^2}2,\ \cos\tfrac{t^2}2\bigr)^T$, the same. At $t=0$, $u=(1,0)^T$. (b) $u^\dagger u=\cos^2\tfrac{t^2}2+\sin^2\tfrac{t^2}2=1$. (c) $u(t)=0$ for all $t$ solves the equation and has $u(0)=0$; by the theorem of Picard and Lindelöf (Section 10.2) the solution with a given initial value is unique, so it is the only one. Nothing can grow out of zero, even though $h$ changes with time: this is Proposition 16.7 for one mode.

**Answer 16.12.** (a) $\mathcal L_{m,\lambda}/\sqrt{|g|}=K-mS-\tfrac\lambda2S^2\to K-m(-S)-\tfrac\lambda2(-S)^2=K-(-m)S-\tfrac\lambda2S^2=\mathcal L_{-m,\lambda}/\sqrt{|g|}$. (b) $K-mS-\tfrac\lambda2S^2\to-K-mS-\tfrac\lambda2S^2=-\bigl[K-(-m)S-\tfrac{(-\lambda)}2S^2\bigr]=-\mathcal L_{-m,-\lambda}/\sqrt{|g|}$. (c) Under such a map the image is $-K-mS-\tfrac\lambda2S^2$, while $-\mathcal L_{-m,\lambda}/\sqrt{|g|}=-K-mS+\tfrac\lambda2S^2$. They differ by $-\lambda S^2$, which is not zero for $\lambda\ne0$ (and for a field with $S\ne0$). The even potential forces $\lambda\to-\lambda$ in every map that reverses the kinetic term.

**Answer 16.13.** $h(m)u_-=-im\gamma^4u_-=m\,u_-$, so in the $+M$ universe $E=u_-^\dagger h(m)u_-=m$, $Q=u_-^\dagger u_-=1$ and $S=u_-^\dagger(-i\gamma^4)u_-=u_-^\dagger u_-=1$. For $w=\gamma^8u_-$ one has $-i\gamma^4w=-w$ (because $\gamma^4$ anticommutes with $\gamma^8$), hence $h(-m)w=m\,w$. The image partner gives $E=-w^\dagger h(-m)w=-m$, $Q=-w^\dagger w=-1$ and $S=-w^\dagger(-i\gamma^4)w=1$; the independent partner gives $E=m$, $Q=1$ and $S=-1$. These are the same numbers as for $u_+$: with the expectation rule of Section 8.12 a quantum in a positive-energy mode has positive energy whatever the Krein sign of the mode. The classical energy density of the same mode is $m\,u_-^\dagger Bu_-=-m$. The classical bilinear and the quantum expectation value can therefore have opposite signs, which is why the classical cancellation of Corollary 16.4 does not carry over automatically to the quantum field (Section 16.6).
