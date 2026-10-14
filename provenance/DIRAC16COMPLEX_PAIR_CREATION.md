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
