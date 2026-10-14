# Pairs of universes of masses +M and -M: exact pairing theorems and Kohn–Sham ground and first excited states of dirac16complex and dirac16complex00 in the primordial field

## Stage 5, document B (old Stage-2/4 frame): the theorems T1, T2 and T3 with proofs, the Kohn–Sham model of both fields, the numerical demonstration T4, and an exact statement of what is proved and what is not

## 1. Summary

### 1.1 The hypothesis in the author's own words

The author's notebook

```
Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb
```

(repository root, read only, never modified; "cell $N$" is the $N$-th counted cell in file order, with the counting rule of the Stage-1 document provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md, Section 2.2) states the goal of this stage as a hypothesis. The three cells are quoted verbatim from the notebook file; line breaks and runs of spaces of the notebook are collapsed.

Cell 6 (section NOTES):

> "HYPOTHESIS: If, employing the Einstein eqs (or Einstein-Lovelock eqs), superluminal inflation/deflation exists, then at time x4 = 0 (before the particles of the standard model exist) a pair of universes with MASSES ± M is created (i.e., universes are created in pairs) Dark matter/dark energy may be related to wave function overlap of these two universes"

Cell 7 (a section title):

> "Bigger Bang: Question: Are Universe (s) of masses ± M created in pairs at time x4 = 0 (before the particles of the standard model exist) ?"

Cell 17:

> "In the spinor Lagrangian Lg[], below, M is the mass of the Ψ16 field [A.K.A., wave function characterizing the Universe(s) of masses ±M ]; TODO: prove Universe(s) of masses ±M are created in pairs!"

The Stage-5 request (handoff/specs/STAGE5_SPEC.md, Section 0, item 6) asks, for each of the two fields dirac16complex and dirac16complex00 in the primordial gravitational field, to "PROVE that Universes of masses {+mass, -mass} are created in pairs". The honesty rule of the same section binds this document: what the equations imply is proved as theorems with their hypotheses stated, each step is verified exactly by two independent implementations, and what is not derived is stated separately and labelled as interpretation.

**What "a universe of mass $M$" means here.** Following cell 17, $M$ is the mass parameter of the spinor field. A universe of mass $\pm M$ is a configuration of dirac16complex (Grassmann-odd components, second quantised) or of dirac16complex00 (commuting classical components) whose Lagrangian (L1) of Section 2.3 carries the mass parameter $m=\pm M$, in a given gravitational field. It is not the total gravitational energy of that configuration: Theorem T2 below shows that the universe of mass $-M$ can have the same, positive or negative, energy density as the one of mass $+M$.

### 1.2 What is proved

All statements in this table are exact theorems with the hypotheses stated in Sections 3 and 4 (and, for T3, in Section 6). Every one is verified in both exact reports:

```
artifacts/dirac16complex/pair-creation/wolfram-pairing-report.json   (141 of 141 checks true)
artifacts/dirac16complex/pair-creation/python-pairing-report.json    (172 of 172 checks true)
artifacts/dirac16complex/pair-creation/pairing-theory.json           (statements, proofs, block maps)
```

The Wolfram report is produced by scripts/verify_dirac16complex_pairing.wls from wolfram/Dirac16ComplexPairing.wl; the Python report by scripts/check_dirac16complex_pairing.py, an independent sympy implementation with its own derivations, which also re-reads the Wolfram report and checks the agreement of the statements and measurements (S5_wolfram_reportAllTrue, S5_wolfram_sourcesCurrent, S5_wolfram_statementsAgree, S5_wolfram_honestyStatements, S5_pairingAgreesWithWolfram).

| Result | Hypotheses | Wolfram checks | Python checks |
|---|---|---|---|
| Algebra: $\gamma^8$, $C$, $B$ facts (Section 2.4) | the exact fixture | PAIR_algebra_* (10) | S5_algebra_* (11) |
| T1: $\mathcal L_{m,\lambda}[\gamma^8\Psi]=-\mathcal L_{-m,-\lambda}[\Psi]$, field equations, $T_{\mu\nu}\to-T_{\mu\nu}$, $j\to-j$ (Section 3.1) | any vielbein, any $m,\lambda$, off shell, both statistics | PAIR_T1generic_*, PAIR_T1grassmann_*, PAIR_T1jets_*, PAIR_T1primordial_* | S5_T1generic_*, S5_T1grassmann_*, S5_T1jets_*, S5_T1primordial_* |
| Corollary T1.1: a chiral pair of classical fields has $T^{\mathrm{pair}}_{\mu\nu}=0$, $j^{\mathrm{pair}}=0$, $\mathcal L^{\mathrm{pair}}=0$ (Section 3.3) | the $-M$ member carries $-\lambda$ (or $\lambda=0$); classical fields in the correlated configuration $\Psi_-=\gamma^8\Psi_+$ | PAIR_T1jets_pairEMTAndCurrentVanish, PAIR_totals_fieldLevelChiralPair | S5_T1jets_pairEMTAndCurrentVanish, S5_totals_fieldLevelChiralPair |
| Quantum reading of T1.1 (erratum E5.1; Section 3.4): no cancellation between two independent, consistently quantised universes | dirac16complex, Krein Fock model of the rest sector | PAIR_T1krein_* (12) | S5_T1krein_* (13) |
| T2: Pin(4,4) reflection of character $-1$ with the frame reflection, $(m,\lambda)\to(-m,\lambda)$, $\mathcal L\to+\mathcal L$, $T\to+T$ (Section 4.1) | space-like unit vector $u$, twisted frame action | PAIR_T2frame_* | S5_T2frame_* |
| T2 in the Z2-extended static primordial field: the mirror universe of mass $-M$ across the brane (Section 4.3) | the Z2 extension of Stage 4 (a construction) | PAIR_T2z2_* | S5_T2z2_* |
| Field-level pair totals of T1 and T2 (Sections 3.3 and 4.4) | as above | PAIR_totals_fieldLevelChiralPair, PAIR_totals_fieldLevelMirrorPair | S5_totals_fieldLevelChiralPair, S5_totals_fieldLevelMirrorPair |
| T3: the Kohn–Sham level (Section 6) | the Stage-4 mean-field model | PAIR_T3block_*, PAIR_T3ks_*, PAIR_T3emt_* | S5_T3block_*, S5_T3ks_*, S5_T3emt_* |

In words: (i) to every configuration of either field with $(m,\lambda)$ the chirality map $\gamma^8$ assigns a configuration with $(-m,-\lambda)$, solutions to solutions, with opposite Lagrangian, energy-momentum tensor and current, in every gravitational field (T1); (ii) a pair formed by a classical field and its chiral image, with the coupling $-\lambda$ for the $-M$ member, carries zero total energy, momentum, stress, charge and action at every point and every $x_4$, in particular at $x_4=0$ (Corollary T1.1); (iii) for the quantum field dirac16complex this cancellation is an operator identity of the form $X+(-X)=0$ within one quantum system, and no reading gives a cancellation between two independent, consistently quantised universes (Section 3.4); (iv) a Pin(4,4) reflection of character $-1$ together with the corresponding reflection of the frame assigns to every configuration with $(m,\lambda)$ one with $(-m,\lambda)$, the SAME coupling, with equal Lagrangian and energy-momentum tensor (T2); in the Z2-extended static primordial field this is the mirror universe of mass $-M$ on the other side of the brane, whose energy-momentum doubles that of the $+M$ universe instead of cancelling it.

### 1.3 What is not proved

The following are NOT proved by anything in this document, and the text never claims them:

1. No creation process, and no dynamical creation rate, amplitude or probability of pair creation is derived; there is no wave function of the universe and no path integral in these theorems (pairing-theory.json, notProved).
2. The theorems do not show that pairs ARE created at $x_4=0$. T1 shows that a $\{+M,-M\}$ pair of the chiral type carries zero total energy-momentum, charge and action in every gravitational field at every $x_4$, so that its appearance from the field-free state is consistent with these conservation laws and with the gravitational constraints (Section 3.5). Consistency is not production.
3. No dynamical necessity: no equation and no conservation law forces the partner to exist; a single universe of mass $+M$ is an equally valid solution without its partner. T1 and T2 are correspondences between the solutions of two parameter sets, not mechanisms. T1 is not a symmetry of one theory: it changes the parameters and the sign of the action, and for $\lambda\ne0$ it pairs $(m,\lambda)$ with $(-m,-\lambda)$.
4. The cancelling (chiral) pair needs $\lambda\to-\lambda$ (or $\lambda=0$) and is a statement about classical fields. For the quantum field no reading gives a cancellation between two independent, consistently quantised universes (erratum E5.1 of STAGE5_SPEC.md, Section 9; Section 3.4 below). dirac16complex00 is a classical field; no quantum statement is made for it.
5. Both members live in the same, prescribed gravitational field (test-field statement). The back-reaction of the pair on the geometry is not part of the theorems. One consequence is derived in Section 3.5: a chiral pair taken as the complete source is a zero source, and the static primordial field with $H>0$ is then not a solution of the eight-dimensional Einstein equations, because it requires the source $\rho_{\mathrm{req}}=-21H^2/\kappa\ne0$ (STAGE4_SPEC.md, erratum E4.3). The pairing theorems do not change the Stage-4 sourcing analysis.
6. The Z2 mirror side of the primordial field is the extension (E2) chosen in STAGE4_SPEC.md, Section 1 (a construction, not derived from the notebook); no junction condition for the field across the brane is derived here.
7. The Kohn–Sham statements (Section 6) are about the mean-field (Hartree–Fock–LDA, no correlation) model of Stage 4; for dirac16complex00 that model is a formal Krein-signed Gaussian functional with Pauli filling imposed by prescription, not a quantum theory of commuting spinors.

<!-- NUMERICS: filled by the lead after the pairs runs -->

### 1.4 Relation to the earlier and later records

**Stage 1.** The Stage-1 document provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md already contains the chirality map (its Section 7.7: $\mathcal L_{m,\lambda}[\gamma^8\Psi]=-\mathcal L_{-m,-\lambda}[\Psi]$, checks ALG_gamma8Map) and states in its Section 1.3, item 6, that "the pairing of the masses $\pm m$ by the chirality map (Section 7.7) is a structural property of the equations, not a claim that universes of masses $\pm M$ are created in pairs." This document agrees with that statement and keeps it. What Stage 5 adds is: the map of the energy-momentum tensor, which Section 7.7 of the Stage-1 document records as "derived", is here machine-checked in all components (36 independent symmetric components with generic symbols, 64 components with exact jets and in the primordial field), together with the field equations, the conjugate equations, the current and the Grassmann-odd case; the pair corollary with its hypotheses; its quantum reading; and the second, mirror-type pairing T2 with the same $\lambda$. The Pin characters of Section 7.7 of the Stage-1 document (a reflection of character $-1$ with the untwisted lift gives $\mathcal L_{m,\lambda}\to-\mathcal L_{m,-\lambda}$, CONTRACT erratum E3) are not contradicted by T2: T2 uses the twisted frame action, which is the untwisted one composed with the frame sign flip $e\to-e$, and by the vielbein form of T1 (Section 3.2) that flip is exactly the chirality map; the composition gives $+\mathcal L_{-m,\lambda}$ (Section 4.2).

**The matter-antimatter record.** provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md, Section 7 (Theorem M4 and Corollary M4.1), states T1 and its pair corollary for classical fields, and its Section 7.3 gives the Krein reading at the Fock level: the image field $\gamma^8\Psi$ is the same quantum system with the Krein metric $-B$, its own $x_4$-generator, charge and metric energy-momentum tensor are $+H_+$, $+Q_+$ and $+T_+$, and an independently quantised $-m$ field has the same free Hamiltonian and charge as the $+m$ universe in the state with the same mode occupations. Section 3.4 of this document states the same, from the Stage-5 checks PAIR_T1krein_* and S5_T1krein_* that the matter-antimatter record cites.

**The Revision record.** The later record Revision/ (binding Revision/SPEC.md) answers the same request in Revision/docs/PAIR_CREATION_PROOFS.md, Section 11.3: maps that pair every solution of mass $m$ with a solution of mass $-m$ are proved (T1 with $\lambda\to-\lambda$ and opposite energy-momentum and charge; T2 with the same $\lambda$ and equal energy-momentum; a Kohn–Sham-level T3), "that universes occur in pairs is not proved", and "Not proved: that such universes are CREATED, in pairs or otherwise". This document does not contradict that answer; its Sections 1.2 and 1.3 say the same for the Stage-5 frame. The scope differs and is stated here explicitly. Stage 5 works in the old Stage-2/4 frame: coordinates $x_0,\dots,x_7$ counted from 0 with $x_4$ the time, the notebook chart of the Stage-2 primordial field with an arbitrary $a_4(t)$ (for T1), and the Stage-4 static warped form with constant $a_4$, the proper hidden coordinate $y=\ln(\sin z)/(6H)\le0$ and the Z2 extension $W=e^{-H|y|}$ with the brane at $y=0$, i.e. $z=\pi/2$ (for T2 and T3). The Revision record works in the author's coordinates $x_1,\dots,x_8$ with the exponentially deflating extra times $x_5,x_6,x_7$, uses an assumed Z2 construction at the brane $z=\pi/2$, where its metric is degenerate, and adds a corollary C1 (a T1 pair as the complete classical source of the author's metric is a zero source, and in Einstein gravity the author's metric then has no solution for $H>0$), whose Stage-4 analogue is derived in Section 3.5. T1 is frame-independent (it holds for every vielbein), so its content is the same in both records; T2 and T3 are proved in each record for that record's own geometry and Z2 construction, and neither record's T2 or T3 is a statement about the other's geometry.

### 1.5 Structure of this document

Section 2 fixes the conventions and lists the algebraic facts used in the proofs. Section 3 proves T1, its pair corollary and its quantum reading, and states what "creation at $x_4=0$" can mean as a statement about constraints and conservation laws. Section 4 proves T2 and its form in the Z2-extended primordial field. Sections 5 to 10 treat the Kohn–Sham model of both fields, the Kohn–Sham-level theorem T3, the numerical demonstration T4, the verification records, the reproduction commands, and the final account of what is proved, what is interpretation and what is open.

## 2. Conventions and the facts used in the proofs

### 2.1 Inherited conventions

The conventions are those of Stages 1 to 4 (handoff/specs/CONTRACT.md with its errata, Section 11; STAGE2_SPEC.md; STAGE4_SPEC.md with its errata, Sections 8 and 9) and of STAGE5_SPEC.md:

- everything is counted from 0; coordinates $x=\{x_0,\dots,x_7\}$, $x_0$ the hidden space direction, $x_1,x_2,x_3$ ordinary 3-space, $x_4$ the evolution time, $x_5,x_6,x_7$ the three extra times;
- tangent metric $\eta=\mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1)$; frame directions 0 to 3 are space-like, 4 to 7 time-like;
- $\gamma^a=\begin{pmatrix}0&\bar\tau_a\\ \tau_a&0\end{pmatrix}$, $a=0,\dots,7$, the notebook's T16^A[a], with the exact fixture artifacts/dirac16complex/arbitrary-field/algebra-fixture.json; $\{\gamma^a,\gamma^b\}=2\eta^{ab}$ (PAIR_algebra_fixtureMatches, PAIR_algebra_clifford; S5_algebra_fixtureMatches, S5_algebra_clifford);
- $C=\gamma^0\gamma^1\gamma^2\gamma^3$ (the notebook's σ16), Dirac adjoint $\bar\Psi=\Psi^\dagger C$, Krein fundamental symmetry $B=-iC\gamma^4$;
- chirality $\gamma^8=\gamma^0\gamma^1\cdots\gamma^7=\mathrm{diag}(-I_8,+I_8)$ (fixture key "chirality"); the label 8 is a name, not a ninth direction;
- vielbein $e_a{}^\mu$, metric $g=e\,\eta\,e^T$, curved gammas $\gamma^\mu=e_a{}^\mu\gamma^a$; canonical spin connection $\Omega_\mu=\tfrac18\,\omega_{\mu ab}[\gamma^a,\gamma^b]$ with $\omega_{\mu ab}=\eta_{ac}\,\omega_\mu{}^c{}_b$, fixed by the vielbein postulate; $S^{ab}=\tfrac14[\gamma^a,\gamma^b]$ (28 generators); $D_\mu\Psi=\partial_\mu\Psi+\Omega_\mu\Psi$, $D_\mu\bar\Psi=\partial_\mu\bar\Psi-\bar\Psi\Omega_\mu$;
- units with $\hbar=1$.

### 2.2 The two fields

Both fields are maps $\Psi:M^8\to\mathbb C^{16}$ with the same transformation law (a Pin(4,4) spinor). **dirac16complex** has complex Grassmann-odd components: it is the second-quantised field of Stage 1, with the equal-$x_4$ anticommutator $\{\Psi,\Psi^\dagger\}=B\,\delta^7/\sqrt{|g|}$ in the Gaussian-normal gauge and the Krein structure with fundamental symmetry $J=B$ of signature (8,8) (Stage-1 document, Sections 10.3 and 10.5; pairing-theory.json, T1krein.canonical). **dirac16complex00** has complex commuting components: it is a classical field, the analogue of Dirac's original 4-component wave function, and not a quantum field (a quantum field of commuting spinors would violate the spin-statistics connection). In every bilinear below the order $\Psi^\dagger\cdots\Psi$ is kept, so that each formula has the same meaning for both statistics.

### 2.3 Lagrangian, field equations, current and energy-momentum tensor

For both fields (STAGE5_SPEC.md, (L1); pairing-theory.json, conventions.lagrangian), with the kinetic scalar

$$
K=\tfrac12\bigl(\bar\Psi\gamma^\mu D_\mu\Psi-(D_\mu\bar\Psi)\gamma^\mu\Psi\bigr),\qquad S=\bar\Psi\Psi,
$$

the Lagrangian density is

$$
\mathcal L_{m,\lambda}[e,\Psi]=\sqrt{|g|}\,\Bigl[K-mS-\tfrac\lambda2S^2\Bigr]=\sqrt{|g|}\,\mathcal L_s .
$$

Its mass term $-m\sqrt{|g|}\,\bar\Psi\Psi$ is linear in $m$ and quadratic in the components; the self-interaction is $U(S)=\tfrac\lambda2S^2$. The Euler–Lagrange equations are

$$
E_{m,\lambda}[\Psi]:=\gamma^\mu D_\mu\Psi-(m+\lambda S)\Psi=0,\qquad \bar E_{m,\lambda}[\Psi]:=(D_\mu\bar\Psi)\gamma^\mu+(m+\lambda S)\bar\Psi=0 .
$$

The U(1) current is $j^\mu=\bar\Psi\gamma^\mu\Psi$; the charge is $Q=\int\sqrt{|g|}\,j^4\,d^7x$. The energy-momentum tensor (vielbein variation, symmetric, CONTRACT Section 7, the Stage-1 form) is

$$
T_{\mu\nu}=\mathcal K_{\mu\nu}+g_{\mu\nu}\mathcal L_s,\qquad
\mathcal K_{\mu\nu}=-\tfrac14\bigl[\bar\Psi\gamma_\mu D_\nu\Psi+\bar\Psi\gamma_\nu D_\mu\Psi-(D_\mu\bar\Psi)\gamma_\nu\Psi-(D_\nu\bar\Psi)\gamma_\mu\Psi\bigr],
$$

with the energy density $\rho=T_{44}$. For dirac16complex, $T_{\mu\nu}$, $j^\mu$ and $S$ are operators (normal ordered with respect to the free Krein vacuum as in the Stage-1 document, Section 10.7); for dirac16complex00 they are c-number fields. The expectation rule of Stage 4 (NUMERICS_CONTRACT) for a Hilbert-normalised one-particle mode $u$ is $\langle\Psi^\dagger X\Psi\rangle=u^\dagger BXu$ (pairing-theory.json, conventions.expectationRule).

### 2.4 The algebraic facts

The proofs of Sections 3 and 4 use only the following exact matrix facts. Each is checked with the actual 16 by 16 matrices of the fixture by both implementations.

**F1 ($\gamma^8$).** $\gamma^8$ is Hermitian, $(\gamma^8)^2=1$, $\gamma^8\gamma^a=-\gamma^a\gamma^8$ for every $a$, $[\gamma^8,C]=0$, and $[\gamma^8,S^{bc}]=0$ for all 28 generators, hence $[\gamma^8,\Omega_\mu]=0$ for every spin connection, in any gravitational field. $\gamma^8=(\gamma^0\gamma^1)(\gamma^2\gamma^3)(\gamma^4\gamma^5)(\gamma^6\gamma^7)$ is a product of four commuting bivectors $X_i$ with $X_i^2=-1$, so $\gamma^8=\exp\bigl(\tfrac\pi2(X_1+X_2+X_3+X_4)\bigr)$ lies in the identity component $\mathrm{Spin}_0(4,4)$, and its vector action is $-1\in\mathrm{SO}_0(4,4)$.

```
checks
  PAIR_algebra_gamma8Properties, PAIR_algebra_gamma8InIdentityComponent: wolfram-pairing
  S5_algebra_gamma8Properties, S5_algebra_gamma8InIdentityComponent: python-pairing
  PAIR_T1generic_connectionCommutesWithGamma8 / S5_T1generic_connectionCommutesWithGamma8
```

**F2 ($C$).** $C$ is real symmetric with $C^2=1$; $C\gamma^a$ is real antisymmetric (anti-Hermitian) for $a=0,\dots,7$; and $\gamma^{a\dagger}C=-C\gamma^a$ for every $a$.

```
checks
  PAIR_algebra_CProperties, PAIR_algebra_gammaDaggerC: wolfram-pairing
  S5_algebra_CProperties, S5_algebra_gammaDaggerC: python-pairing
```

**F3 ($B$).** $B=-iC\gamma^4$ is Hermitian, $B^2=1$, $\mathrm{Tr}\,B=0$ (spectrum $(+1)^8(-1)^8$), $[B,C]=0$, $BC=-i\gamma^4$, and

$$
\gamma^8B\gamma^8=-B .
$$

Under the basic reflections, $uBu^\dagger=+B$ for $u=\gamma^0,\dots,\gamma^4$ and $uBu^\dagger=-B$ for $u=\gamma^5,\gamma^6,\gamma^7$ (measured; a general unit vector mixes the two).

```
checks
  PAIR_algebra_BProperties, PAIR_algebra_kreinUnderBasicReflections: wolfram-pairing
  S5_algebra_BProperties, S5_algebra_kreinUnderBasicReflections: python-pairing
```

**F4 (bilinear parities).** For all 456 matrices $X\in\{C\gamma^a,\ C\gamma^aS^{bc},\ CS^{bc}\gamma^a\}$ ($8+224+224$; these are all the matrices of the kinetic, connection, current and energy-momentum bilinears) one has $\gamma^8X\gamma^8=-X$, and $\gamma^8C\gamma^8=+C$ (the matrix of the mass term and of $S$).

```
checks
  PAIR_algebra_bilinearParities (measurement algebra_oddBilinearMatrixCount = 456): wolfram-pairing
  S5_algebra_bilinearParities (count 456): python-pairing
```

**F5 (chiral block structure).** In the notebook basis $C$ and every $S^{ab}$ are block diagonal in $(\Psi_0,\dots,\Psi_7\,|\,\Psi_8,\dots,\Psi_{15})$ and every $\gamma^a$ is block off-diagonal; $\gamma^8\Psi=(-\Psi_{\mathrm{upper}},+\Psi_{\mathrm{lower}})$. Every monomial of a kinetic, connection, current or energy-momentum bilinear pairs an upper with a lower component (sign $-1$ under $\gamma^8$); every monomial of $S$ pairs equal chiralities (sign $+1$). For Grassmann-odd components $\gamma^8$ is therefore the algebra automorphism $\theta_a\to\chi(a)\,\theta_a$ of the Grassmann algebra ($\chi(a)=-1$ for $a<8$, $+1$ for $a\ge8$), compatible with all products and with the order of odd factors.

```
checks
  PAIR_algebra_chiralBlockStructure: wolfram-pairing
  S5_algebra_chiralBlockStructure: python-pairing
```

**F6 (Pin characters).** For a real unit vector $u=v_a\gamma^a$ with $u^2=n(u)=\eta(v,v)=\pm1$, F2 gives $u^\dagger C=-Cu=\chi(u)\,Cu^{-1}$ with the character $\chi(u)=-n(u)$: $\chi=-1$ for space-like $u$ ($n=+1$: $\gamma^0,\dots,\gamma^3$ and every space-like combination), $\chi=+1$ for time-like $u$ ($\gamma^4,\dots,\gamma^7$). This is the character of the Stage-1 document, Section 7.7, and of CONTRACT erratum E3.

```
checks
  PAIR_T2frame_unitVectors, PAIR_T2frame_characterIsMinusNorm: wolfram-pairing
  S5_algebra_characterIsMinusNorm, S5_T2frame_unitVectors, S5_T2frame_characterIsMinusNorm: python-pairing
```

## 3. Theorem T1: the chirality map

### 3.1 Statement and proof

**Theorem T1 (chirality map; field level, arbitrary gravitational field, both statistics).** Let $e$ be any vielbein (hence any metric $g=e\,\eta\,e^T$ with its Levi-Civita spin connection), let $m$ and $\lambda$ be any mass and coupling of $U=\tfrac\lambda2S^2$, and let $\Psi$ be any configuration (off shell) of dirac16complex (Grassmann-odd components) or of dirac16complex00 (commuting components). Put $\Psi_-:=\gamma^8\Psi$. Then

$$
\begin{aligned}
&\text{(a)}\quad \bar\Psi_-=\bar\Psi\gamma^8,\qquad S[\Psi_-]=S[\Psi],\qquad K[\Psi_-]=-K[\Psi],\\
&\text{(b)}\quad j^\mu[\Psi_-]=-j^\mu[\Psi]\quad\text{for every }\mu,\\
&\text{(c)}\quad \mathcal L_{m,\lambda}[\gamma^8\Psi]=-\mathcal L_{-m,-\lambda}[\Psi],\\
&\text{(d)}\quad E_{-m,-\lambda}[\gamma^8\Psi]=-\gamma^8E_{m,\lambda}[\Psi],\qquad \bar E_{-m,-\lambda}[\gamma^8\Psi]=-\bar E_{m,\lambda}[\Psi]\,\gamma^8,\\
&\text{(e)}\quad T_{\mu\nu}[\gamma^8\Psi;-m,-\lambda]=-T_{\mu\nu}[\Psi;m,\lambda]\quad\text{for all components.}
\end{aligned}
$$

Hence $\Psi$ solves the Euler–Lagrange equations with $(m,\lambda)$ if and only if $\gamma^8\Psi$ solves them with $(-m,-\lambda)$.

*Proof.* Step 1 (adjoint). By F1, $\gamma^8$ is Hermitian and commutes with $C$, so $\bar\Psi_-=\Psi^\dagger\gamma^{8\dagger}C=\Psi^\dagger C\gamma^8=\bar\Psi\gamma^8$.

Step 2 (covariant derivatives). $\gamma^8$ is a constant matrix and commutes with every $\Omega_\mu$ (F1), so $D_\mu(\gamma^8\Psi)=\gamma^8D_\mu\Psi$ and $D_\mu\bar\Psi_-=(D_\mu\bar\Psi)\gamma^8$. The geometric coefficients $e_a{}^\mu$, $\omega_{\mu ab}$, $\sqrt{|g|}$ and $g_{\mu\nu}$ are not touched by the map.

Step 3 (bilinears). A bilinear $\bar\Psi X\Psi$ goes to $\bar\Psi\gamma^8X\gamma^8\Psi$. By F4 this is $-\bar\Psi X\Psi$ when $X$ contains one gamma matrix (with or without a generator $S^{bc}$ of the connection), and $+\bar\Psi\Psi$ for $X=1$. So $S\to S$, $K\to-K$ (a), $j^\mu\to-j^\mu$ (b), and $\mathcal K_{\mu\nu}\to-\mathcal K_{\mu\nu}$. The self-interaction $\tfrac\lambda2S^2$ is even.

Step 4 (Lagrangian). With (a),

$$
\mathcal L_{m,\lambda}[\gamma^8\Psi]=\sqrt{|g|}\Bigl[-K-mS-\tfrac\lambda2S^2\Bigr]=-\sqrt{|g|}\Bigl[K-(-m)S-\tfrac{(-\lambda)}2S^2\Bigr]=-\mathcal L_{-m,-\lambda}[\Psi],
$$

which is (c).

Step 5 (field equations). By Step 2 and $\gamma^\mu\gamma^8=-\gamma^8\gamma^\mu$ (F1), $\gamma^\mu D_\mu(\gamma^8\Psi)=-\gamma^8\gamma^\mu D_\mu\Psi$, and $S[\gamma^8\Psi]=S[\Psi]$, so

$$
E_{-m,-\lambda}[\gamma^8\Psi]=-\gamma^8\gamma^\mu D_\mu\Psi+(m+\lambda S)\gamma^8\Psi=-\gamma^8\bigl[\gamma^\mu D_\mu\Psi-(m+\lambda S)\Psi\bigr]=-\gamma^8E_{m,\lambda}[\Psi].
$$

In the same way $\bar E_{-m,-\lambda}[\gamma^8\Psi]=(D_\mu\bar\Psi)\gamma^8\gamma^\mu-(m+\lambda S)\bar\Psi\gamma^8=-\bar E_{m,\lambda}[\Psi]\gamma^8$. This is (d); since $\gamma^8$ is invertible, the solution sets correspond one to one. The Python implementation also derives the Euler–Lagrange expressions from the Lagrangian itself (total derivatives acting on the geometric coefficients too; left derivatives for Grassmann-odd components) and verifies $\gamma^8\,EL^{(m,\lambda)}[\gamma^8\Psi]=-EL^{(-m,-\lambda)}[\Psi]$.

Step 6 (energy-momentum tensor). $T_{\mu\nu}=\mathcal K_{\mu\nu}+g_{\mu\nu}\mathcal L_s$. By Step 3, $\mathcal K_{\mu\nu}[\gamma^8\Psi]=-\mathcal K_{\mu\nu}[\Psi]$; by (c) applied to the parameters $(-m,-\lambda)$, $\mathcal L_s[\gamma^8\Psi;-m,-\lambda]=-\mathcal L_s[\Psi;m,\lambda]$. Adding gives (e).

Step 7 (both statistics). The map is linear, acts pointwise and keeps every $\Psi^\dagger$ to the left of every $\Psi$; in the notebook basis it is the Grassmann-algebra automorphism $\theta_a\to\chi(a)\theta_a$ of F5, which is compatible with all products and with the order of odd factors. Steps 1 to 6 use only matrix identities between $\Psi^\dagger$ and $\Psi$, so they hold verbatim for Grassmann-odd and for commuting components. $\square$

**Remark (the coupling must change sign).** At fixed $\lambda$ the map does not pair $+m$ with $-m$: $\mathcal L_{m,\lambda}[\gamma^8\Psi]+\mathcal L_{-m,\lambda}[\Psi]=-\lambda\sqrt{|g|}\,S^2\ne0$ (CONTRACT erratum E2; the simpler form $\mathcal L_m\to-\mathcal L_{-m}$ holds only for $U=0$). An analytic remark of pairing-theory.json (T1.corollaryPair.noGoFixedLambda), not machine-checked beyond the checks PAIR_T1generic_naiveFixedLambdaFails and S5_T1generic_naiveFixedLambdaFails: for $\lambda\ne0$ no map $\Psi\to M\Psi$ with a constant matrix $M$ and any frame change gives $(m,\lambda)\to(-m,\lambda)$ with $\mathcal L\to-\mathcal L$ for commuting fields, because the quartic parts would require $S_M^2=-S^2$ with the real bilinear $S_M=\Psi^\dagger M^\dagger CM\Psi$; the even interaction forces $\lambda\to-\lambda$ in every map with $T\to-T$.

```
checks (Wolfram: wolfram-pairing-report.json; Python: python-pairing-report.json)
  generic symbols, commuting components, every vielbein (polynomial identities):
    PAIR_T1generic_nontrivial, _scalarInvariantKineticOdd, _lagrangian, _naiveFixedLambdaFails,
    _fieldEquation, _conjugateFieldEquation, _emtAll36, _current, _connectionCommutesWithGamma8
    S5_T1generic_nontrivial, _scalarInvariantKineticOdd, _lagrangian, _naiveFixedLambdaFails,
    _fieldEquation, _conjugateFieldEquation, _eulerLagrangeFromLagrangian, _current, _emtAll36,
    _connectionCommutesWithGamma8
  Grassmann-odd components (dirac16complex):
    PAIR_T1grassmann_nontrivial, _scalarEvenKineticOdd, _lagrangian, _naiveFixedLambdaFails,
    _diracOperator, _emt, _current
    S5_T1grassmann_nontrivial, _scalarEvenKineticOdd, _lagrangian, _naiveFixedLambdaFails,
    _diracOperator, _conjugateDiracOperator, _emt, _current, _eulerLagrangeFromLagrangian
  exact jets of the generic non-diagonal vielbein G1 at the three points p1, p2, p3:
    PAIR_T1jets_lagrangian, _scalarEvenKineticOdd, _naiveFixedLambdaFails, _emt, _current,
    _fieldEquations, _connectionCommutes, _onShellImage, _conservationBoth
    S5_T1jets_lagrangian, _scalarEvenKineticOdd, _naiveFixedLambdaFails, _emt, _current,
    _fieldEquations, _connectionCommutes, _onShellImage, _conservationBoth
  the Stage-2 primordial field (notebook chart, arbitrary a4(t), generic fields of all eight coordinates):
    PAIR_T1primordial_nontrivialCoupling, _scalarAndKinetic, _lagrangian, _diracOperator, _emt64, _current
    S5_T1primordial_nontrivialCoupling, _scalarAndKinetic, _lagrangian, _diracOperator, _emt64, _current
```

The recorded measurements show that the identities are not empty. With generic symbols the kinetic term has 23552 monomials and its connection part 21504 (both reports: T1generic_kineticMonomials and T1generic_connectionMonomials in the Wolfram measurements, S5_T1generic in the Python measurements, where the identity runs over 4143 independent symbols); the coupling to the spin connection enters $\mathcal L$ through $\tfrac12\bar\Psi\{\gamma^\mu,\Omega_\mu\}\Psi$. In the Grassmann algebra the scalar Lagrangian has 1288 monomials and $S^2$ has 120 (both reports; the squares of odd generators vanish, against 136 monomials of $S^2$ for commuting components); the Wolfram check uses 288 odd generators (pairing-theory.json, T1.fieldsCovered), the Python check 1440. In the primordial field $\gamma^\mu\Omega_\mu=3H\gamma^0$ with 192 nonzero entries of the $\Omega_\mu$ (the individual $\Omega_\mu$ depend on $a_4(t)$, the contraction does not), and the energy-momentum identity covers 64 nonzero components (S5_T1primordial). In the jets, every on-shell configuration with $(m,\lambda)$ has an on-shell image for $(-m,-\lambda)$, which is not a solution for $(m,\lambda)$ or for $(-m,\lambda)$, and $\nabla^\mu T_{\mu\nu}=0$ holds for both members on shell and fails off shell (S5_T1jets: onShellImage, conservationBoth).

### 3.2 The vielbein form of T1

$\gamma^8$ lies in $\mathrm{Spin}_0(4,4)$ and acts on vectors as $-1$ (F1), so $(\gamma^8,\ e\to-e)$ is an exact symmetry of the theory: $\mathcal L$ and $T_{\mu\nu}$ are invariant and $E[-e,\gamma^8\Psi]=+\gamma^8E[e,\Psi]$. Equivalently, T1 is the same as reversing the sign of the vielbein at fixed $\Psi$: the metric, $\sqrt{|g|}$ and $\Omega_\mu$ are unchanged, $\gamma^\mu\to-\gamma^\mu$, and

$$
\mathcal L_{m,\lambda}[-e,\Psi]=-\mathcal L_{-m,-\lambda}[e,\Psi],\qquad T_{\mu\nu}[-e,\Psi;m,\lambda]=-T_{\mu\nu}[e,\Psi;-m,-\lambda].
$$

So the sign of $m$, taken together with the sign of $\lambda$ and of the action, is tied to the orientation of the frame.

```
checks
  PAIR_T1jets_vielbeinSignFlipGeometry, PAIR_T1jets_vielbeinSignFlipIsT1,
  PAIR_T1jets_gamma8WithFrameSignIsSymmetry: wolfram-pairing
  S5_T1jets_vielbeinSignFlipGeometry, S5_T1jets_vielbeinSignFlipIsT1,
  S5_T1jets_gamma8WithFrameSignIsSymmetry: python-pairing
```

### 3.3 Corollary T1.1: the chiral pair of classical fields

**Corollary T1.1 (pair).** *Hypotheses.* (i) The $-M$ member carries the coupling $-\lambda$; for $\lambda=0$ both members are the same free field with the masses $+m$ and $-m$. (ii) The members are classical fields: commuting c-number fields (dirac16complex00; then no further hypothesis is needed, the identity is between c-number fields), or two independent classical fields, $\Psi_+$ with $\mathcal L_{m,\lambda}$ and $\Psi_-$ with $\mathcal L_{-m,-\lambda}$, in the correlated configuration $\Psi_-=\gamma^8\Psi_+$. The correlation is an assumption about the configuration, not a consequence of the dynamics. (iii) Both members live in the SAME gravitational field, taken as given. (For the quantum field dirac16complex see Section 3.4: there the identity is an operator identity within one quantum system.)

*Statement.* Then, at every point, in any gravitational field and at every $x_4$, in particular at $x_4=0$,

$$
\begin{aligned}
&T^{\mathrm{pair}}_{\mu\nu}=T_{\mu\nu}[\Psi_+;m,\lambda]+T_{\mu\nu}[\Psi_-;-m,-\lambda]=0,\\
&j^{\mathrm{pair}\,\mu}=j^\mu[\Psi_+]+j^\mu[\Psi_-]=0,\qquad Q^{\mathrm{pair}}=\int\sqrt{|g|}\,j^{\mathrm{pair}\,4}\,d^7x=0,\\
&\mathcal L^{\mathrm{pair}}=\mathcal L_{m,\lambda}[\Psi_+]+\mathcal L_{-m,-\lambda}[\Psi_-]=0,\qquad S^{\mathrm{pair}}=2S[\Psi_+].
\end{aligned}
$$

The total energy density, momentum density, stresses, charge and action of the pair vanish identically, and $\Psi_-$ solves its field equations exactly when $\Psi_+$ solves its own (T1 (d)). The Einstein (or Einstein–Lovelock) equations with the pair as the source are the source-free equations.

*Proof.* (e) of T1 with $\Psi=\Psi_+$ gives $T_{\mu\nu}[\Psi_-;-m,-\lambda]=-T_{\mu\nu}[\Psi_+;m,\lambda]$; (b) gives $j^\mu[\Psi_-]=-j^\mu[\Psi_+]$; (c) applied to the parameters $(-m,-\lambda)$ gives $\mathcal L_{-m,-\lambda}[\gamma^8\Psi_+]=-\mathcal L_{m,\lambda}[\Psi_+]$; (a) gives $S[\Psi_-]=S[\Psi_+]$. The integrand of $Q^{\mathrm{pair}}$ vanishes pointwise. $\square$

```
checks
  PAIR_T1jets_pairEMTAndCurrentVanish, PAIR_totals_fieldLevelChiralPair, PAIR_T1generic_emtAll36: wolfram-pairing
  S5_T1jets_pairEMTAndCurrentVanish (on shell at p1, p2, p3: T + T' = 0, j + j' = 0, L + L' = 0, S' = S),
  S5_totals_fieldLevelChiralPair, S5_T1generic_emtAll36: python-pairing
```

### 3.4 The quantum reading of the corollary (erratum E5.1)

Corollary T1.1 is a statement about classical fields. For the quantum field dirac16complex the identities of T1 hold as operator identities, but they do not describe two universes whose energies cancel. The facts, all verified in an exact Fock model (pairing-theory.json, T1krein):

**The Fock model.** Four modes of the rest sector with $m=1$: joint eigenvectors $u_n$ of $h(m)=-im\gamma^4$ (Hermitian, $h^2=m^2$, $[h,B]=0$, $\gamma^8h(m)\gamma^8=h(-m)$) and of $B$, with $(\epsilon,\beta)=(+1,+1),(+1,-1),(-1,+1),(-1,-1)$. The Krein CAR $\{b_n,b_n^K\}=\beta_n$ is realised on a positive Fock space by $b_n=a_n$, $b_n^K=\beta_na_n^*$; the sea consists of the two negative-energy modes, and normal ordering is the subtraction of the sea expectation value. The field satisfies $\{\Psi_a,\Psi^K_b\}=(BP)_{ab}$ ($P$ the projector on the four modes). One particle in mode $u$ gives $\langle:\Psi^KM\Psi:\rangle=u^\dagger BMu$, one hole $-u^\dagger BMu$ (verified for $M=C,B,Bh,C\gamma^4,BC$), and every excitation has the energy $|\epsilon|=m>0$ (the $J=B$ positivity).

**(a) The image field.** $\Psi_-=\gamma^8\Psi$ on the same Fock space and in the same state has the anticommutator $\{\Psi_-,\Psi_-^K\}=\gamma^8BP\gamma^8=-BP_-$ (F3; $P_-=\gamma^8P\gamma^8$): it carries the Krein metric $-B$, i.e. it is canonically a field of the Lagrangian $-\mathcal L_{-m,-\lambda}=\mathcal L_{m,\lambda}[\gamma^8\,\cdot\,]$. The operator identities

$$
H[\Psi_-;-m]=-H[\Psi;m],\qquad Q[\Psi_-]=-Q[\Psi],\qquad S[\Psi_-]=S[\Psi]
$$

hold ($H=\Psi^KBh\Psi$, $Q=\Psi^KB\Psi=J^4$), and since $\gamma^8$ acts linearly and pointwise, normal ordering commutes with the map: $:T_{\mu\nu}[\gamma^8\Psi;-m,-\lambda]:\;=-:T_{\mu\nu}[\Psi;m,\lambda]:$. Evaluated on the image field, the $\mathcal L_{-m,-\lambda}$ formulas give the energy $-|\epsilon|$ and the charge $-1$ per particle ($+1$ per hole). These are not the image field's own energy and charge. With the anticommutator $-B$,

$$
[\Psi_-,H[\Psi_-;-m]]=-h(-m)\,\Psi_-,\qquad [\Psi_-,Q[\Psi_-]]=-\Psi_-,
$$

while the image evolves by $i\partial_4\Psi_-=[\Psi_-,H[\Psi;m]]=h(-m)\Psi_-$. So $H[\Psi_-;-m]$ generates the reversed $x_4$-evolution and $Q[\Psi_-]$ the inverse phase; the image field's own $x_4$-generator, U(1) generator and metric energy-momentum tensor are

$$
-H[\Psi_-;-m]=+H_+,\qquad -Q[\Psi_-]=+Q_+,\qquad -:T_{\mu\nu}[\Psi_-;-m,-\lambda]:\;=+:T_{\mu\nu}[\Psi_+;m,\lambda]: ,
$$

with energy $+|\epsilon|$ and charge $+1$ per particle, as in the $+m$ universe (the last identity is derived from the operator identity for $:T_{\mu\nu}:$ and the canonical Lagrangian $-\mathcal L_{-m,-\lambda}$ of the image). The image field is the same quantum system as $\Psi_+$ written in other variables: the same operators, the same Fock space and the same state. The identities $H_++H[\Psi_-;-m]=0$, $Q_++Q[\Psi_-]=0$ and $:T_{\mu\nu}[\Psi_+;m,\lambda]:+:T_{\mu\nu}[\Psi_-;-m,-\lambda]:\;=0$ have the form $X+(-X)=0$ and hold in every state, also when $Q_+\ne0$. Counted as a second source the image would give $2T_+$; since it is the same system, it adds nothing.

**(b) An independently quantised $-m$ universe.** If the theory $\mathcal L_{-m,-\lambda}$ is quantised on its own, with its own canonical structure $\{\Psi',\Psi'^K\}=+BP_w$ and the positive ($J=B$) Fock space, its modes are $w_n=\gamma^8u_n$ (same $\epsilon$, Krein sign $-\beta_n$), and a quantum in $w_n$ has the energy $+|\epsilon|$, the charge of the corresponding $+m$ excitation and the scalar density $-u^\dagger BCu$: $(E,Q,S)\to(E,Q,-S)$ per quantum. In the state with the same mode occupations its free Hamiltonian and its charge equal those of the $+m$ universe; its kinetic and mass energies add to those of the $+m$ universe, and the charges cancel only by a further assumption about its state.

The values per quantum in the Fock model ($m=1$; Python measurements S5_T1krein, imageExpectationValues and independentExpectationValues; the Wolfram measurement T1krein_scalarDensity_particle1_particle2_hole3_hole4 records the scalar densities $\{1,1,1,1\}$ of the $+m$ universe):

| Excitation | $+m$ universe $(E,Q,S)$ | $\mathcal L_{-m,-\lambda}$ formulas on the image, metric $-B$ | independently quantised $-m$, metric $+B$ |
|---|---|---|---|
| particle (two modes) | $(1,1,1)$ | $(-1,-1,1)$ | $(1,1,-1)$ |
| hole (two modes) | $(1,-1,1)$ | $(-1,1,1)$ | $(1,-1,-1)$ |

The middle column is minus the image field's own generators, not the energy and charge of a second universe.

**Consequence.** At the quantum level no reading gives a cancellation between two independent, consistently quantised universes. The cancellation $T^{\mathrm{pair}}=0$ of Corollary T1.1 is a statement about classical fields. The Krein-image pair totals of the Kohn–Sham level (Section 6) are exact identities read in the same way, $X+(-X)=0$ between the $+M$ values and the $(-m,-\lambda)$ formulas evaluated on the same state.

```
checks
  PAIR_T1krein_restHamiltonians, _modes, _fieldCAR, _statesNormalised, _expectationRule,
  _positiveExcitations, _imageAnticommutatorMinusB, _imageOperatorIdentities (including the four
  commutators above, erratum E5.1), _imageExpectationValues, _minusMModes, _independentCARPlusB,
  _independentExpectationValues: wolfram-pairing (12 checks)
  S5_T1krein_restHamiltonians, _modes, _fieldCAR, _bilinearFromFields, _statesNormalised,
  _expectationRule, _positiveExcitations, _imageAnticommutatorMinusB, _imageOperatorIdentities,
  _imageExpectationValues, _minusMModes, _independentCARPlusB, _independentExpectationValues:
  python-pairing (13 checks)
```

### 3.5 What "creation at $x_4=0$" can mean here

The corollary is a theorem about kinematics, conservation laws and constraints of classical fields. Its exact content for the hypothesis of cells 6, 7 and 17:

- The field-free state ($\Psi_+=\Psi_-=0$) has $T_{\mu\nu}=0$, $j^\mu=0$, $Q=0$ and zero action. A chiral pair (hypotheses (i) to (iii) of Corollary T1.1) has the same totals at every point and every $x_4$. The conservation of the total energy-momentum and of the total charge, and the gravitational constraints at $x_4=0$ (the components $G^4{}_\nu=\kappa\,T^{\mathrm{pair}\,4}{}_\nu$ of the Einstein equations, and their Lovelock analogues), are therefore satisfied by the pair exactly as by the field-free state: these laws do not forbid the appearance of such a pair from the field-free state (derived from Corollary T1.1).
- Each member solves its own field equations (T1 (d)), so each member's current is conserved separately. In the theory as built the two members do not interact, and the vanishing of the pair totals does not by itself allow members with nonzero individual charge to appear from a state in which each member had zero charge (derived).
- A chiral pair taken as the complete source of the gravitational field is a zero source. The static primordial field of Stage 4 requires the eight-dimensional Einstein source $\rho_{\mathrm{req}}=-21H^2/\kappa$, $p_{\mathrm{req}}=+15H^2/\kappa$ (STAGE4_SPEC.md, erratum E4.3), which is nonzero for $H>0$; so with a chiral pair as its only source it is not a solution of the eight-dimensional Einstein equations (derived; the Stage-4 analogue of corollary C1 of Revision/docs/PAIR_CREATION_PROOFS.md for the author's metric). The Einstein–Lovelock case is not studied here.
- Nothing in this section is a creation process, a rate, an amplitude or a probability, and nothing shows that such a pair is produced. "Created in pairs" remains the notebook's hypothesis; what is proved is that the chiral pair of classical fields is consistent with the conservation laws and constraints listed above.
