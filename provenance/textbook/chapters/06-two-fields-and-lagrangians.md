## 6. The two fields and their Lagrangians

### 6.1 What this chapter does

Chapter 5 ended with a negative result: the Lagrangian $\mathrm{Lg}[\,]$ of the author's notebook describes nothing when its sixteen components are real anticommuting (Grassmann) numbers, as the components of a fermion field must be. This chapter writes down the Lagrangians that the project uses instead, and it does so for two fields that share the same sixteen components and the same formula but differ in one respect, the kind of numbers their components are.

- **dirac16complex** has complex Grassmann-odd components. It is the classical form of a field that is meant to be quantized with anticommutators, a "second-quantized" field (Section 6.2 explains the words); Chapter 8 carries out that quantization.
- **dirac16complex00** has ordinary commuting complex components. It is a classical field, the sixteen-component analogue in 4+4 dimensions of the four-component wave function that Dirac wrote down in 1928.

For both fields the chapter derives, step by step: why the Lagrangian contains the matrix $C$ (Section 6.3); the Lagrangian itself (Section 6.4); why it is real (Section 6.5); the explicit mass term, which is linear in the mass and quadratic in the components, and why it is neither zero nor trivial (Section 6.6); the interaction $U(S)$ (Section 6.7); the coupling to gravity through the vielbein and the spin connection (Section 6.8); the continuous symmetries (Section 6.9); why the notebook's $\mathrm{Lg}[\,]$ is empty for real Grassmann fields but a genuine Lagrangian for real commuting ones, and how it sits inside the Lagrangian of dirac16complex00 (Section 6.10); and how the Lagrangians behave under the chirality map $\Psi\to\gamma^8\Psi$, under reflections and under complex conjugation (Sections 6.11 and 6.12). The field equations, the energy–momentum tensor and the equations of state that follow from these Lagrangians are the subject of Chapter 7.

**Sources.** The Stage-1 document `provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md` (its §4, §6 and §7) with its reports in `artifacts/dirac16complex/arbitrary-field/` (153 of 153 checks true, counted in `stage1-summary.json`); the Stage-5 specification `handoff/specs/STAGE5_SPEC.md` (its §1 and §5); the exact Stage-5 reports on dirac16complex00 in `artifacts/dirac16complex/pair-creation/`, namely `wolfram-dirac16complex00-report.json` (46 of 46 checks true; written by `scripts/verify_dirac16complex00.wls` with the package `wolfram/Dirac16Complex00.wl`) and `python-dirac16complex00-report.json` (49 of 49 checks true; written by the independent sympy checker `scripts/check_dirac16complex00.py`), whose exact formulas are collected in `dirac16complex00-theory.json` in the same folder; the Stage-5 pairing reports `wolfram-pairing-report.json` (141 of 141) and `python-pairing-report.json` (172 of 172) with `pairing-theory.json` in the same folder; and the matter–antimatter document `provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md` (its §5) with its reports in `artifacts/dirac16complex/matter-antimatter/` (44 of 44 and 75 of 75 checks true). Check names that begin with `C00_` belong to the Wolfram dirac16complex00 report, and names that begin with `PAIR_` to the Wolfram pairing report `wolfram-pairing-report.json`. The two independent Python checkers give all their checks the prefix `S5_`: the Python twin of a `C00_` check is the `S5_` check with the same ending in `python-dirac16complex00-report.json`, and the Python twin of a `PAIR_` check is the `S5_` check with the same ending in `python-pairing-report.json`. An `S5_` name that this chapter cites on its own is a check of `python-dirac16complex00-report.json`. Names that begin with `MA_` belong to the matter–antimatter reports; the other names are Stage-1 checks. The prose documents of Stage 5 (planned as `provenance/DIRAC16COMPLEX00_FIELD_THEORY.md` and `provenance/DIRAC16COMPLEX_PAIR_CREATION.md`) had not been written when this chapter was written, so the chapter cites the committed reports directly. Every general statement of this chapter is derived here. Three kinds of statement are only quoted from the reports, and each is marked as such where it occurs: numbers measured at test points (numbers of terms and of nonzero entries); the curved-space form of the reflections of Section 6.12, which Chapter 15 proves; and the completeness of the classification of the discrete maps in Section 6.12, which Chapter 17 treats.

**Conventions** (Chapter 0 and Chapter 1): counting from 0; coordinates $x_0,\dots,x_7$ with $x_4$ the time; $\eta=\mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1)$; Greek indices $\mu,\nu,\dots$ for coordinates, Latin $a,b,c,\dots$ for frame directions, both from 0 to 7; a repeated index, one up and one down, is summed. The gamma matrices $\gamma^0,\dots,\gamma^7$ are the notebook's (Section 2.8), $C=\gamma^0\gamma^1\gamma^2\gamma^3$, $\gamma^8=\gamma^0\gamma^1\cdots\gamma^7$ and $B=-iC\gamma^4$.

### 6.2 Two fields with the same sixteen components

**The spinor space.** Chapter 2 showed that sixteen complex numbers form the smallest space on which the eight gamma matrices of signature (4,4) can act, and that the group Pin(4,4) acts on it by $\Psi\to g\Psi$. Under Pin(4,4) the space $\mathbb C^{16}$ is irreducible; under its even part Spin(4,4) it splits into the two inequivalent halves $\Psi_0,\dots,\Psi_7$ (chirality $-1$) and $\Psi_8,\dots,\Psi_{15}$ (chirality $+1$) (Theorems 2.11 and 2.12). A **spinor field** attaches to every point $x$ a column $\Psi(x)=(\Psi_0(x),\dots,\Psi_{15}(x))^T$ whose components are measured in the local frame of the vielbein (Chapter 4); when the frame is turned by a local frame rotation, the column changes by the covering spin transformation, $\Psi\to R(x)\Psi$ (Section 4.12).

**Dirac's wave function of 1928.** Dirac's equation for the electron is an equation for a column of four complex functions $\psi(x)$ of the four coordinates of ordinary spacetime. Dirac read $\psi$ as a **wave function** in the sense of quantum mechanics: the number $\psi^\dagger\psi\ge0$ is the probability density of finding the electron at $x$, and it obeys a conservation law. The four components are ordinary complex numbers. This is called **first quantization**: a single particle is described by a wave function. Later physics found that this reading fails (the equation has solutions of negative energy, and particles can be created and destroyed), and the electron is described instead by a **quantum field**, whose components are operators that create and annihilate electrons and positrons and that anticommute. Turning the classical field into such operators is called **second quantization** (Chapter 8 does it for dirac16complex).

**dirac16complex.** Its components are complex Grassmann-odd numbers (Section 5.9):

$$
\Psi_a\Psi_b=-\Psi_b\Psi_a,\qquad \Psi_a\Psi_b^\ast=-\Psi_b^\ast\Psi_a,\qquad (\theta_1\theta_2)^\ast=\theta_2^\ast\theta_1^\ast .
$$

A classical Grassmann field is the classical counterpart of a field of anticommuting operators: its Lagrangian is the starting point of the quantization of Chapter 8, where the components become operators with the anticommutator $\{\Psi_a,\Psi_b^\dagger\}=B_{ab}\,\delta^7/\sqrt{|g|}$ at equal times (in the frames of Section 8.6, where $\gamma^{x_4}=\gamma^4$). This is what "second quantized" means for dirac16complex. It was introduced in Stage 1.

**dirac16complex00.** Its sixteen components are ordinary commuting complex numbers ("c-numbers") that transform together as one Pin(4,4) spinor: $\Psi\to g\Psi$ under Pin(4,4) and $\Psi\to R(x)\Psi$ under local frame rotations, exactly as for dirac16complex. It is the classical analogue, in 4+4 dimensions, of Dirac's four-component wave function. It was introduced in Stage 5 (`handoff/specs/STAGE5_SPEC.md`, §0, items 2 and 3). The two fields carry the same representation, because the representation is a property of the matrices, not of the numbers they act on: the matrices that commute with all eight gammas are the multiples of the identity (Theorem 2.11); those that commute with all 28 spin generators $S^{ab}$ form the two-dimensional space spanned by the projectors $P_-$ and $P_+$ (Theorem 2.12 (5)); and the invariant bilinear forms form the two-dimensional space spanned by $CP_-$ and $CP_+$ (checks `C00_algebra_pinModuleAndSpinInvariance` and `S5_algebra_pinModuleAndSpinInvariance`).

The last statement has a short proof. A matrix $G$ defines an **invariant bilinear form** $\Psi^TG\Phi$ if the form does not change, to first order, under the infinitesimal spin rotations $\Psi\to(1+\epsilon S^{ab})\Psi$, $\Phi\to(1+\epsilon S^{ab})\Phi$, that is if $(S^{ab})^TG+GS^{ab}=0$ for all $a,b$ (the definition of Section 8.8 and of the checks). Property (S5) of Section 2.11 says $(CS^{ab})^T=-CS^{ab}$; since $C$ is symmetric this is $(S^{ab})^TC=-CS^{ab}$, and multiplying on the right by $C$ (with $C^2=1$) gives $(S^{ab})^T=-CS^{ab}C$. So the condition reads $-CS^{ab}CG+GS^{ab}=0$. Multiply it by $C$ from the left: $-S^{ab}(CG)+(CG)S^{ab}=0$. The matrix $Z:=CG$ therefore commutes with every $S^{ab}$, hence with every $\gamma^a\gamma^b=2S^{ab}$ ($a\ne b$), hence with every even monomial (a product of such pairs), hence with every combination of even monomials, which is the whole span of Spin(4,4) (Theorem 2.12 (2)). By Theorem 2.12 (5), $Z=r_-P_-+r_+P_+$ with two numbers $r_\mp$, that is $G=CZ=r_-CP_-+r_+CP_+$. Conversely every such $G$ satisfies the condition, because $P_\mp$ commute with every $S^{ab}$ (even elements commute with $\gamma^8$). The two matrices $CP_-$ and $CP_+$ are independent: if $x\,CP_-+y\,CP_+=0$, multiply by $C$ from the left and then by $P_-$ from the right ($P_-^2=P_-$, $P_+P_-=0$) to get $x\,P_-=0$, so $x=0$, and in the same way $y=0$. $\square$ The scalar density uses $G=C=CP_-+CP_+$.

**What differs, and what does not.** The Lagrangian, the field equations, the energy–momentum tensor and the current are given by the same formulas for both fields. The statistics of the components enters in five places, listed in `dirac16complex00-theory.json` (key `fields.difference`) and treated in this book as follows:

1. which potentials $U(S)$ are possible (Section 6.7);
2. the real restriction and the notebook's $\mathrm{Lg}[\,]$ (Section 6.10);
3. the meaning of the energy–momentum tensor: for dirac16complex an operator of the quantized theory, **normal-ordered** (a prescription of Section 8.10 that removes the constant energy of the filled "Dirac sea" of negative-energy states), for dirac16complex00 an ordinary number field (Chapter 7);
4. positivity: the charge and the classical energy of dirac16complex00 have no fixed sign (Chapter 7), while for the quantized dirac16complex Chapter 8 derives a Hamiltonian that is not negative in the **good sector**, the fields that do not depend on the three extra times $x_5,x_6,x_7$ (Section 8.10);
5. the sign of the exchange term in a density-functional treatment (Chapter 14).

**What dirac16complex00 is not.** It is not a quantum field. In ordinary 3+1 dimensional physics the spin–statistics theorem states that fields of half-integer spin must be quantized with anticommutators; a quantum theory of commuting spinors would contradict it. This book proves no spin–statistics theorem for signature (4,4) (Section 5.16), and the project does not quantize dirac16complex00: it treats it only as a classical field (`handoff/specs/STAGE5_SPEC.md`, §4; `pairing-theory.json`, key `statistics`). Where Chapter 14 uses dirac16complex00 in a density-functional model, that model is labelled there as a prescription.

**A small example of the difference.** Take two components $\Psi_0,\Psi_1$. For commuting components $\Psi_0\Psi_1-\Psi_1\Psi_0=0$ and $\Psi_0\Psi_0=\Psi_0^2$ can be any complex number. For Grassmann components $\Psi_0\Psi_1-\Psi_1\Psi_0=2\Psi_0\Psi_1$ and $\Psi_0\Psi_0=0$. Every construction below keeps all conjugate factors $\Psi^\ast$ (or $\Psi^\dagger$) to the left of all factors $\Psi$, so that a formula written for one kind of component can be read, without reordering, for the other; where a reordering is unavoidable (Sections 6.10 and 6.12) the sign it produces is written out.

### 6.3 The building blocks, and why the adjoint contains $C$

We collect the objects of Chapters 2 and 4 that the Lagrangian is built from.

- (B1) The gamma matrices satisfy $\gamma^a\gamma^b+\gamma^b\gamma^a=2\eta^{ab}$; $\gamma^a$ is symmetric for $a\le3$ and antisymmetric for $a\ge4$ (Section 2.8).
- (B2) $C=\gamma^0\gamma^1\gamma^2\gamma^3$ is real and symmetric, $C^2=1$, and it has eight eigenvalues $+1$ and eight $-1$. Every $C\gamma^a$ is real and antisymmetric (expression [1] of Section 2.9), and so is every $CS^{ab}$, where $S^{ab}=\tfrac14[\gamma^a,\gamma^b]$ (Section 2.11). Equivalently $(\gamma^a)^TC=-C\gamma^a$ and $(S^{ab})^TC=-CS^{ab}$.
- (B3) The **Dirac adjoint** of a column $\Psi$ is the row $\bar\Psi:=\Psi^\dagger C$, with the components $\bar\Psi_b=\sum_a\Psi_a^\ast C_{ab}$.
- (B4) The vielbein $e_\mu{}^a(x)$, its inverse $e_a{}^\mu$, the metric $g_{\mu\nu}=e_\mu{}^a\eta_{ab}e_\nu{}^b$, the volume factor $\sqrt{|g|}=|\det e|$, and the curved gammas $\gamma^\mu=e_a{}^\mu\gamma^a$ with $\gamma^\mu\gamma^\nu+\gamma^\nu\gamma^\mu=2g^{\mu\nu}$ (Section 4.10). Since $e_a{}^\mu$ is real, every $\gamma^\mu$ is a real matrix and every $C\gamma^\mu$ is real and antisymmetric.
- (B5) The canonical spin connection $\omega_{\mu ab}=-\omega_{\mu ba}$ of Section 4.11, the spinor connection $\Omega_\mu=\tfrac12\omega_{\mu ab}S^{ab}$ (a real matrix), and the covariant derivatives $D_\mu\Psi=\partial_\mu\Psi+\Omega_\mu\Psi$ and $D_\mu\bar\Psi=\partial_\mu\bar\Psi-\bar\Psi\,\Omega_\mu$, which satisfy $D_\mu\bar\Psi=(D_\mu\Psi)^\dagger C$ (Section 4.12).
- (B6) The divergence identity $\partial_\mu\bigl(\sqrt{|g|}\,\gamma^\mu\bigr)=\sqrt{|g|}\,[\gamma^\mu,\Omega_\mu]$ (Sections 4.12 and 5.12).

**Why not $\Psi^\dagger\Psi$?** A Lagrangian must not depend on the choice of frame, so it must be built from combinations of the field that do not change under frame rotations. The simplest candidate, $\Psi^\dagger\Psi=\sum_a|\Psi_a|^2$, does not qualify. Under a spin transformation $R$ (a real matrix, Section 2.11) the column becomes $R\Psi$ and the row $\Psi^\dagger$ becomes $\Psi^\dagger R^T$, so $\Psi^\dagger\Psi\to\Psi^\dagger R^TR\,\Psi$. For a rotation $R^TR=1$, but not for a boost.

*Worked example.* Take the boost $R=\cosh\tfrac\theta2+\sinh\tfrac\theta2\,J$ with $J=\gamma^0\gamma^4$ (Section 2.11). By (B1), $J^T=(\gamma^4)^T(\gamma^0)^T=-\gamma^4\gamma^0=\gamma^0\gamma^4=J$, so $R^T=R$, and $J^2=-(\gamma^0)^2(\gamma^4)^2=+1$. Hence $R^TR=R^2=\cosh^2\tfrac\theta2+\sinh^2\tfrac\theta2+2\cosh\tfrac\theta2\sinh\tfrac\theta2\,J=\cosh\theta+\sinh\theta\,J$. For $\Psi=e_0+e_4$ ($e_n$ is the column with 1 in place $n$) the tables of Section 2.8 give $\gamma^4e_0=e_{13}$ and $\gamma^0e_{13}=e_5$, so $Je_0=e_5$, and $\gamma^4e_4=-e_9$, $\gamma^0e_9=e_1$, so $Je_4=-e_1$. Then $\Psi^TJ\Psi=(e_0+e_4)^T(e_5-e_1)=0$ and $(R\Psi)^\dagger(R\Psi)=2\cosh\theta$, which is not the original value 2 unless $\theta=0$. The Dirac adjoint cures this.

**$\bar\Psi\Psi$ is invariant.** Section 2.11 proved $R^TCR=C$ for every exponential $R=\exp(\theta S^{ab})$ (and Section 2.14 for all products of them). Therefore

$$
\bar\Psi\Psi=\Psi^\dagger C\Psi\ \to\ \Psi^\dagger R^TCR\,\Psi=\Psi^\dagger C\Psi .
$$

In the example, $\Psi=e_0+e_4$ has $\bar\Psi\Psi=\Psi^TC\Psi=C_{04}+C_{40}=-2$ (row 0 of $C$ reads $-4$ and row 4 reads $-0$, Section 2.9), and so has $R\Psi$ for every $\theta$.

**$\bar\Psi\gamma^a\Phi$ is a vector.** From $R^TCR=C$ we get $R^TC=CR^{-1}$. If $R$ covers the frame rotation $\Lambda$, that is $R^{-1}\gamma^aR=\Lambda^a{}_b\gamma^b$ (Section 4.12), then

$$
(R\Psi)^\dagger C\gamma^a(R\Phi)=\Psi^\dagger R^TC\gamma^aR\,\Phi=\Psi^\dagger CR^{-1}\gamma^aR\,\Phi=\Lambda^a{}_b\,\bar\Psi\gamma^b\Phi ,
$$

so the eight numbers $\bar\Psi\gamma^a\Phi$ change like the frame components of a vector. Contracting the frame index with $e_a{}^\mu$ and then with a covariant derivative $D_\mu$ gives combinations such as $\bar\Psi\gamma^\mu D_\mu\Psi$ that do not change at all (Section 6.9 completes the argument). These are the building blocks of the Lagrangian.

### 6.4 The Lagrangian of both fields

**Definition.** For both fields, in an arbitrary gravitational field,

$$
\mathcal L=\sqrt{|g|}\,\Bigl[\tfrac12\bigl(\bar\Psi\gamma^\mu D_\mu\Psi-(D_\mu\bar\Psi)\gamma^\mu\Psi\bigr)-m\,\bar\Psi\Psi-U(\bar\Psi\Psi)\Bigr].
$$

This is the Lagrangian of Stage 1 for dirac16complex (Stage-1 document, §7.1) and equation (L1) of `handoff/specs/STAGE5_SPEC.md`, §1, for both fields. The action of a region $R$ of spacetime is $\int_R\mathcal L\,d^8x$. We use the names

$$
\begin{aligned}
&K:=\tfrac12\bigl(\bar\Psi\gamma^\mu D_\mu\Psi-(D_\mu\bar\Psi)\gamma^\mu\Psi\bigr)\quad\text{(kinetic term)},\qquad S:=\bar\Psi\Psi\quad\text{(scalar density)},\\
&\mathcal L_s:=\mathcal L/\sqrt{|g|}=K-mS-U(S),\qquad M_{\mathrm{eff}}:=m+U'(S)\quad\text{(effective mass)},
\end{aligned}
$$

and we write $\mathcal L_{m,U}$, or $\mathcal L_{m,\lambda}$ for the default potential $U(S)=\tfrac\lambda2S^2$, when the parameters matter.

**Reading the formula term by term.**

- $\sqrt{|g|}$ turns the coordinate volume $d^8x$ into proper volume (Section 4.4), so the action does not depend on the coordinates.
- The **kinetic term** $K$ contains one derivative of the field, like the first-order Lagrangians of Sections 5.6 and 5.10. It is **symmetrized**: the derivative acts once on $\Psi$ and once on $\bar\Psi$, with opposite signs. Section 6.5 shows that this makes the Lagrangian real without any factor $i$, and Chapter 7 shows that its time part plays the role of the $\tfrac i2(\psi^\ast\dot\psi-\dot\psi^\ast\psi)$ of the oscillator of Section 5.6.
- The **mass term** $-mS=-m\bar\Psi\Psi$ is linear in the mass $m$ and quadratic in the components (Section 6.6).
- The **interaction** $-U(S)$ is a function of the scalar density (Section 6.7).
- Gravity enters through $\sqrt{|g|}$, through the curved gammas $\gamma^\mu=e_a{}^\mu\gamma^a$ and through the spin connection in $D_\mu$ (Section 6.8).

**Relation to the notebook.** Stage 1 compared the formula with the notebook's $\mathrm{Lg}[\,]$ of Section 5.12 term by term (Stage-1 document, §7.3):

| notebook $\mathrm{Lg}[\,]$ | this Lagrangian |
| --- | --- |
| Transpose[Ψ16], a real column | ConjugateTranspose: $\Psi^\dagger$ of a complex column |
| Transpose[Ψ16].σ16 | $\bar\Psi=\Psi^\dagger C$ with the same $C=\sigma_{16}$ |
| unsymmetrized $\Psi^TC\gamma^\mu D_\mu\Psi$ | symmetrized kinetic term $K$ |
| mixed connection $\omega_\mu{}^a{}_b$ | lowered connection $\omega_{\mu ab}=\eta_{ac}\omega_\mu{}^c{}_b$ |
| Sqrt[detgg] | $\sqrt{\lvert g\rvert}$ |
| $+(HM)\,\Psi^TC\Psi$ | $-m\bar\Psi\Psi$ with $m=-HM$ (same sign) |
| no self-interaction | $-U(\bar\Psi\Psi)$ |

**Worked example.** In flat space ($e_\mu{}^a=\delta_\mu{}^a$, $\Omega_\mu=0$) take the constant commuting field $\Psi=e_0+e_4$. All derivatives vanish, so $K=0$; $S=-2$ (Section 6.3); and for $U=\tfrac\lambda2S^2$ the Lagrangian is $\mathcal L=-m(-2)-\tfrac\lambda2\cdot4=2m-2\lambda$.

### 6.5 Reality: the Lagrangian is real for both kinds of components

A Lagrangian must be real, for commuting components an ordinary real number, and for Grassmann components an element that is unchanged by the conjugation of the Grassmann algebra (the book calls such an element Hermitian, Section 5.9). Otherwise the action is a complex number, the equations obtained by varying $\Psi$ and by varying $\Psi^\ast$ are in general not the conjugates of each other, and there are more independent equations than field components.

**Lemma 6.1 (conjugating a bilinear).** For two columns $\Psi$ and $\Phi$ (for example $\Phi=D_\mu\Psi$), both commuting or both Grassmann, and a matrix $M$ of ordinary numbers,

$$
\bigl(\Psi^\dagger M\Phi\bigr)^\ast=\Phi^\dagger M^\dagger\Psi .
$$

*Proof.* Commuting components: $\bigl(\sum_{a,b}\Psi_a^\ast M_{ab}\Phi_b\bigr)^\ast=\sum_{a,b}\Psi_aM_{ab}^\ast\Phi_b^\ast=\sum_{a,b}\Phi_b^\ast(M^\dagger)_{ba}\Psi_a$, because ordinary numbers may be written in any order. Grassmann components: the conjugation reverses the order of a product, $(\Psi_a^\ast\Phi_b)^\ast=\Phi_b^\ast\Psi_a$ (Section 5.9), so $\bigl(\Psi_a^\ast M_{ab}\Phi_b\bigr)^\ast=M_{ab}^\ast\,\Phi_b^\ast\Psi_a$, and the sum is the same expression. $\square$

The two computations end in the same formula for opposite reasons: for commuting numbers nothing is reordered, and for Grassmann numbers the reversal of the order is built into the conjugation. This is why the reality proof below holds for both fields at once (`dirac16complex00-theory.json`, key `lagrangian.reality`).

**Theorem 6.2 (reality).** For both kinds of components the Lagrangian $\mathcal L$ is real (Hermitian): $\mathcal L^\ast=\mathcal L$.

*Proof.* Put $X:=\bar\Psi\gamma^\mu D_\mu\Psi=\Psi^\dagger\,(C\gamma^\mu)\,(D_\mu\Psi)$, summed over $\mu$. By (B4), $C\gamma^\mu$ is real and antisymmetric, so $(C\gamma^\mu)^\dagger=(C\gamma^\mu)^T=-C\gamma^\mu$. Lemma 6.1 and (B5) give

$$
X^\ast=(D_\mu\Psi)^\dagger(C\gamma^\mu)^\dagger\Psi=-(D_\mu\Psi)^\dagger C\gamma^\mu\Psi=-(D_\mu\bar\Psi)\gamma^\mu\Psi .
$$

Hence $K=\tfrac12\bigl(X-(D_\mu\bar\Psi)\gamma^\mu\Psi\bigr)=\tfrac12(X+X^\ast)$ is real. Next, $S^\ast=(\Psi^\dagger C\Psi)^\ast=\Psi^\dagger C^\dagger\Psi=S$ because $C$ is real and symmetric. For commuting components $U(S)$ is a real function of the real number $S$. For Grassmann components $U$ is a polynomial with real coefficients (Section 6.7); since $S$ is even, $(S^k)^\ast=(S^\ast)^k=S^k$, so $U(S)^\ast=U(S)$. Finally $m$ and $\sqrt{|g|}$ are real. $\square$

**Why the kinetic term is symmetrized.** The unsymmetrized $X$ alone is not real. Its imaginary part is a total derivative: Section 7.5 proves the identity $\sqrt{|g|}\,\bigl(X+(D_\mu\bar\Psi)\gamma^\mu\Psi\bigr)=\partial_\mu\bigl(\sqrt{|g|}\,\bar\Psi\gamma^\mu\Psi\bigr)$, which says $\sqrt{|g|}(X-X^\ast)=\partial_\mu(\sqrt{|g|}\,\bar\Psi\gamma^\mu\Psi)$, so

$$
\sqrt{|g|}\,X=\sqrt{|g|}\,K+\tfrac12\,\partial_\mu\bigl(\sqrt{|g|}\,\bar\Psi\gamma^\mu\Psi\bigr).
$$

By Section 5.4 the two versions give the same field equations, but only the symmetrized one gives a real action. The repository checks both statements: the symmetrized Lagrangian is real and the unsymmetrized kinetic term is not (checks `LAG_hermiticity_G1`, `LAG_hermiticity_G2`, `GR_lagrangianHermitian`, `GR_unsymmetrizedKineticNotHermitian` of Stage 1; `C00_lagrangian_realCommuting`, which writes $\Psi=X_r+iY_r$ with real commuting symbols and finds $\mathrm{Im}\,\mathcal L=0$ exactly at a point of the general test geometry G1 and at three points of the primordial field; `S5_lagrangian_realCommuting`, which also records `unsymmetrizedKineticNotReal`).

**The same statement for the coefficients.** Collect the terms of $\mathcal L$ by the number of derivatives: $\mathcal L=\Psi^\dagger K_0\Psi+\Psi^\dagger K^\mu\partial_\mu\Psi+\partial_\mu\Psi^\dagger L^\mu\Psi-\sqrt{|g|}\,(mS+U)$ with

$$
K^\mu=\tfrac12\sqrt{|g|}\,C\gamma^\mu,\qquad L^\mu=-\tfrac12\sqrt{|g|}\,C\gamma^\mu=(K^\mu)^\dagger,\qquad K_0=\tfrac12\sqrt{|g|}\,C\{\gamma^\mu,\Omega_\mu\} .
$$

($K_0$ collects $\tfrac12\bar\Psi\gamma^\mu\Omega_\mu\Psi$ from the first half of $K$ and $+\tfrac12\bar\Psi\Omega_\mu\gamma^\mu\Psi$ from the second.) $K_0$ is real and symmetric because $C\{\gamma^c,S^{ab}\}$ is symmetric (Section 5.12). The conditions $K_0^\dagger=K_0$ and $L^\mu=(K^\mu)^\dagger$ are exactly what makes $\mathcal L$ real (Stage-1 document, Result 7.1; checks `C00_lagrangian_coefficientHermiticity` and `S5_lagrangian_coefficientHermiticity`, which read the coefficients off the symbolic Lagrangian).

**Worked example.** Flat space, commuting field depending on $x_1$ only: $\Psi=f(x_1)\,e_0+g(x_1)\,e_{11}$. Only $\gamma^1\partial_1$ contributes to $X$, and we need two entries of $C\gamma^1$. From the tables (Sections 2.8 and 2.9): $(C\gamma^1u)_0=-(\gamma^1u)_4=-(-u_{11})=u_{11}$ and $(C\gamma^1u)_{11}=+(\gamma^1u)_{15}=-u_0$. So $(C\gamma^1)_{0,11}=+1$ and $(C\gamma^1)_{11,0}=-1$, antisymmetric as it must be. Then $X=f^\ast g'-g^\ast f'$ (a prime is $d/dx_1$). Take $f=1$ and $g=e^{ikx_1}$ with a real $k$. Then

$$
X=ik\,e^{ikx_1},\qquad K=\tfrac12(X+X^\ast)=\tfrac12\bigl(ik\,e^{ikx_1}-ik\,e^{-ikx_1}\bigr)=-k\sin(kx_1),
$$

a real number, while $X$ itself is complex. And $X-X^\ast=2ik\cos(kx_1)$, which is the derivative of $\bar\Psi\gamma^1\Psi=f^\ast g-g^\ast f=2i\sin(kx_1)$, as the total-derivative identity says.

### 6.6 The mass term

**The term.** The mass term of both Lagrangians is

$$
\mathcal L_m=-m\sqrt{|g|}\;\bar\Psi\Psi=-m\sqrt{|g|}\sum_{a,b=0}^{15}\Psi_a^\ast\,C_{ab}\,\Psi_b .
$$

It is **linear in the mass** $m$ and **quadratic in the components**: every term contains exactly one factor $\Psi_a^\ast$ and one factor $\Psi_b$ (a bilinear). The Stage-5 specification requires such a term for both fields and requires it to be non-zero and non-trivial (`handoff/specs/STAGE5_SPEC.md`, §1). Both properties are proved now.

**Non-zero for commuting components.** $C$ is a signed permutation matrix (Section 2.9): $(Cu)_i=-u_{i+4}$ for $i=0,\dots,3$, $(Cu)_i=-u_{i-4}$ for $i=4,\dots,7$, $(Cu)_i=+u_{i+4}$ for $i=8,\dots,11$ and $(Cu)_i=+u_{i-4}$ for $i=12,\dots,15$. Hence

$$
S=\bar\Psi\Psi=-\sum_{i=0}^{3}\bigl(\Psi_i^\ast\Psi_{i+4}+\Psi_{i+4}^\ast\Psi_i\bigr)+\sum_{i=8}^{11}\bigl(\Psi_i^\ast\Psi_{i+4}+\Psi_{i+4}^\ast\Psi_i\bigr).
$$

Three exact values: $S=-2$ for $\Psi=e_0+e_4$, $S=+2$ for $\Psi=e_8+e_{12}$, and $S=0$ for $\Psi=e_0+i\,e_4$ (there $\Psi_0^\ast\Psi_4+\Psi_4^\ast\Psi_0=i-i=0$). The scalar density takes both signs because $C$ has eight eigenvalues $+1$ and eight $-1$ (checks `C00_massTerm_commutingExplicitSpinors` and `S5_massTerm_commutingExplicitSpinors`, which record the three values and the characteristic polynomial $(x-1)^8(x+1)^8$ of $C$).

**Non-zero for Grassmann components.** For Grassmann components the formula above is an element of the Grassmann algebra generated by the 32 odd elements $\Psi_a,\Psi_a^\ast$ at a point. Its 16 terms $\Psi_a^\ast C_{ab}\Psi_b$ are 16 different monomials, one for each nonzero entry of $C$, each with coefficient $\pm1$, and none cancels, because $\Psi_a^\ast$ and $\Psi_b$ are different generators. So $S\ne0$. (Contrast the real Grassmann field of Section 5.13, for which $\Psi^TC\Psi=0$.) $S^2$ has 120 monomials and $S^3$ has 560 (checks `C00_massTerm_grassmannNonzero` and `S5_massTerm_grassmannNonzero`, which also records all the counts of Section 5.9 up to $S^{17}=0$).

**Non-trivial: the mass changes the field equation.** A term of the Lagrangian is trivial if it does not change the field equations, for example a total derivative (Section 5.4). The mass term is not trivial, because the mass appears in the relation between frequency and wave number. We show it in flat space with $U=0$, where Chapter 7 derives the field equation $\gamma^a\partial_a\Psi=m\Psi$. Try a plane wave

$$
\Psi(x)=u\,\exp\Bigl(i\sum_{a=0}^7k_ax_a\Bigr)
$$

with a constant column $u$ and real wave numbers $k_a$. Each $\partial_a$ produces $ik_a$, so the equation becomes $\bigl(i\gamma(k)-m\bigr)u=0$ with $\gamma(k):=\sum_ak_a\gamma^a$, the notation of Section 2.14. By the Clifford relation $\gamma(k)^2=\sum_a\eta^{aa}k_a^2$ (Section 2.14; the cross terms cancel in pairs), so

$$
\bigl(i\gamma(k)-m\bigr)\bigl(i\gamma(k)+m\bigr)=-\gamma(k)^2-m^2=\Bigl(k_4^2+k_5^2+k_6^2+k_7^2-k_0^2-k_1^2-k_2^2-k_3^2-m^2\Bigr)\cdot1 .
$$

If the bracket is not zero, $i\gamma(k)-m$ has an inverse and the only solution is $u=0$. If the bracket is zero, nonzero solutions exist. Writing $\omega:=|k_4|$ for the frequency in the time $x_4$, the condition is

$$
\omega^2=m^2+k_0^2+k_1^2+k_2^2+k_3^2-k_5^2-k_6^2-k_7^2 ,
$$

the same relation as for the scalar field of Section 5.5: the mass enters as $m^2$. On the mass shell, for $m\ne0$, the solutions form a space of dimension exactly 8. *Proof.* Write $N_\pm=i\gamma(k)\pm m$ and $\ker N$ for the set of columns $u$ with $Nu=0$ (a subspace). Both $N_\pm$ are built from the single matrix $\gamma(k)$, so they commute, and on shell the product computed above is zero: $N_-N_+=N_+N_-=0$. Also $N_+-N_-=2m\cdot1$. Step 1: every column $u$ is a sum of a column of $\ker N_-$ and a column of $\ker N_+$. Indeed $u=\tfrac1{2m}(N_+-N_-)u=p+q$ with $p=\tfrac1{2m}N_+u$ and $q=-\tfrac1{2m}N_-u$, and $N_-p=\tfrac1{2m}N_-N_+u=0$, $N_+q=-\tfrac1{2m}N_+N_-u=0$. Step 2: the two subspaces meet only in 0: if $N_-u=N_+u=0$ then $2mu=(N_+-N_-)u=0$, so $u=0$. Step 3: take a basis $p_1,\dots,p_r$ of $\ker N_-$ and a basis $q_1,\dots,q_s$ of $\ker N_+$. By Step 1 the $r+s$ columns together span all of $\mathbb C^{16}$. They are also independent: if $\sum a_ip_i+\sum b_jq_j=0$, the column $\sum a_ip_i=-\sum b_jq_j$ lies in both subspaces, so it is 0 by Step 2, and then all $a_i$ and all $b_j$ vanish because each set is a basis. So the $r+s$ columns form a basis of $\mathbb C^{16}$, and since every basis of $\mathbb C^{16}$ has 16 elements (all bases of a space have the same number of elements, Section 2.2), $r+s=16$. Step 4: $\gamma^8N_-\gamma^8=-i\gamma(k)-m=-N_+$ (because $\gamma^8$ anticommutes with every $\gamma^a$ and $(\gamma^8)^2=1$). So if $N_-u=0$, then $N_+(\gamma^8u)=-\gamma^8N_-\gamma^8\gamma^8u=-\gamma^8N_-u=0$: the matrix $\gamma^8$ maps $\ker N_-$ into $\ker N_+$, and in the same way $\ker N_+$ into $\ker N_-$. The columns $\gamma^8p_1,\dots,\gamma^8p_r$ are independent (if $\sum c_i\gamma^8p_i=0$, multiplying by $\gamma^8$ gives $\sum c_ip_i=0$, so all $c_i=0$), and they lie in the $s$-dimensional $\ker N_+$, so $r\le s$ by fact (i) of Section 2.2; in the same way $s\le r$. Hence $r=s=8$. $\square$ The repository checks the product identity and the two cases $m=1$, $k=(k_0,\dots,k_7)=(1,1,2,3,4,0,0,0)$, on shell because $16-(1+1+4+9)=1=m^2$, with an 8-dimensional solution space, and $k_4=3$ instead of 4, off shell, with no solution (checks `C00_massTerm_dispersionFlat` and `S5_massTerm_dispersionFlat`). The plane-wave analysis concerns the linear field equation, which is the same for both fields (Chapter 7). In a curved field the mass enters the second-order form of the field equation in the same way, as $m^2$ (Section 7.4).

### 6.7 The interaction $U(S)$

**Grassmann components: only polynomials.** At one point, $S=\bar\Psi\Psi$ is an even element of the Grassmann algebra of the 32 odd generators $\Psi_a,\Psi_a^\ast$. Every monomial of $S^k$ contains $2k$ distinct generators, so $S^{17}=0$ (Section 5.9: $S^k$ has $\binom{16}{k}$ monomials for $k\le16$). A function of $S$ can therefore only mean its Taylor polynomial, which stops at degree 16:

$$
U(S)=u_2S^2+u_3S^3+\dots+u_{16}S^{16}\qquad(\text{real }u_k).
$$

The project requires $U(0)=U'(0)=0$ (Stage-1 document, §7.6): a constant term would be a cosmological constant, and a linear term would be a second mass term. The default is the four-fermion contact interaction

$$
U(S)=\tfrac\lambda2S^2,\qquad U'(S)=\lambda S,\qquad M_{\mathrm{eff}}=m+\lambda S .
$$

Chapter 11 calls $\lambda<0$ attractive and $\lambda>0$ repulsive.

**Commuting components: any smooth function.** For dirac16complex00, $S$ is an ordinary real number at each point, so $U$ may be any smooth real function of one variable; power series such as $e^{S}-1-S$ are allowed. The default is the same $U=\tfrac\lambda2S^2$, so that the two theories differ **only** in the statistics (`handoff/specs/STAGE5_SPEC.md`, §1). The Stage-5 verifiers check the field equations and the energy–momentum tensor with an abstract smooth $U$, whose values $U(S_0)$, $U'(S_0)$, $U''(S_0)$ at the point are independent symbols (checks `C00_EL_commutingGeneralSmoothU`, `C00_EMT_generalSmoothU` and their `S5_` twins).

**Worked example.** Two complex Grassmann components with $S=\theta_0^\ast\theta_0-\theta_1^\ast\theta_1$ (Exercise 5.10). The two pieces $P_0=\theta_0^\ast\theta_0$ and $P_1=-\theta_1^\ast\theta_1$ are even, commute, and square to zero. So $S^2=2P_0P_1=-2\,\theta_0^\ast\theta_0\theta_1^\ast\theta_1$ and $S^3=0$. The "exponential" $e^S=1+S+\tfrac12S^2$ is an exact finite sum, and $U=\tfrac\lambda2S^2=-\lambda\,\theta_0^\ast\theta_0\theta_1^\ast\theta_1$. For commuting numbers the same symbols would give an infinite series for $e^S$.

### 6.8 The coupling to gravity: vielbein and spin connection

Gravity enters the Lagrangian in three places: the volume factor $\sqrt{|g|}$, the curved gammas $\gamma^\mu=e_a{}^\mu\gamma^a$, and the spinor connection $\Omega_\mu$ inside $D_\mu$. The first two carry the vielbein itself, the third its derivatives. This section shows precisely how much of the spin connection the Lagrangian actually sees, and why the coupling is nevertheless not trivial in a curved field.

**Lemma 6.3.** For $a\ne b$ and any $c$,

$$
\{\gamma^c,S^{ab}\}=\begin{cases}\gamma^c\gamma^a\gamma^b&\text{if }c\ne a\text{ and }c\ne b,\\ 0&\text{if }c=a\text{ or }c=b.\end{cases}
$$

*Proof.* For $a\ne b$, $S^{ab}=\tfrac12\gamma^a\gamma^b$. If $c$ differs from $a$ and $b$, moving $\gamma^c$ past $\gamma^a\gamma^b$ costs two signs, so $\gamma^cS^{ab}=S^{ab}\gamma^c=\tfrac12\gamma^c\gamma^a\gamma^b$ and the anticommutator is $\gamma^c\gamma^a\gamma^b$. If $c=a$: $\gamma^aS^{ab}=\tfrac12(\gamma^a)^2\gamma^b=\tfrac12\eta^{aa}\gamma^b$ and $S^{ab}\gamma^a=\tfrac12\gamma^a\gamma^b\gamma^a=-\tfrac12(\gamma^a)^2\gamma^b=-\tfrac12\eta^{aa}\gamma^b$; they cancel. The case $c=b$ is the same with the roles exchanged. $\square$

**Theorem 6.4 (what the Lagrangian sees of the connection).** Write $\omega_{cab}:=e_c{}^\mu\,\omega_{\mu ab}$ for the frame components of the spin connection. The part of the kinetic term that contains $\Omega_\mu$ is

$$
\tfrac12\bigl(\bar\Psi\gamma^\mu\Omega_\mu\Psi+\bar\Psi\Omega_\mu\gamma^\mu\Psi\bigr)=\tfrac12\,\bar\Psi\{\gamma^\mu,\Omega_\mu\}\Psi=\tfrac14\sum_{c,a,b\ \text{distinct}}\omega_{cab}\,\bar\Psi\gamma^c\gamma^a\gamma^b\Psi ,
$$

and only the **totally antisymmetric part** of $\omega_{cab}$ contributes. In a field with a diagonal vielbein this part is zero, so there the Lagrangian contains no spin connection at all.

*Proof.* The first equality: $K=\tfrac12(\bar\Psi\gamma^\mu(\partial_\mu+\Omega_\mu)\Psi-(\partial_\mu\bar\Psi-\bar\Psi\Omega_\mu)\gamma^\mu\Psi)$, and the terms with $\Omega_\mu$ are $\tfrac12\bar\Psi\gamma^\mu\Omega_\mu\Psi+\tfrac12\bar\Psi\Omega_\mu\gamma^\mu\Psi$. The second: $\gamma^\mu=e_c{}^\mu\gamma^c$ and $\Omega_\mu=\tfrac12\omega_{\mu ab}S^{ab}$ give $\{\gamma^\mu,\Omega_\mu\}=\tfrac12\omega_{cab}\{\gamma^c,S^{ab}\}$, and Lemma 6.3 keeps only the terms with $c,a,b$ distinct. For three distinct indices $\gamma^c\gamma^a\gamma^b$ changes sign when any two of them are exchanged (the gammas anticommute), so in the sum $\omega_{cab}$ may be replaced by its totally antisymmetric part $\tfrac16(\omega_{cab}+\omega_{abc}+\omega_{bca}-\omega_{acb}-\omega_{bac}-\omega_{cba})$. For a diagonal vielbein $e_\mu{}^a=h_\mu\delta_\mu{}^a$, Section 4.11 showed that $\omega_{\mu ab}\ne0$ only when $\mu=a$ or $\mu=b$. The inverse vielbein is diagonal too, $e_c{}^\mu=\delta_c{}^\mu/h_c$, so $\omega_{cab}$ equals $1/h_c$ times the component $\omega_{\mu ab}$ with the coordinate index $\mu$ equal to the number $c$, and that component vanishes unless $c=a$ or $c=b$. So $\omega_{cab}=0$ whenever $c,a,b$ are distinct. $\square$

(Checks: `C00_algebra_anticommutatorTotallyAntisymmetric` and `S5_algebra_anticommutatorTotallyAntisymmetric` for the lemma; in `C00_connection_nonTrivialCoupling` the measurement `onlyTotallyAntisymmetricOmega` is true at every test point, `anticommutatorTermNonzero` is true at the three points of the non-diagonal geometry G1 and false at the three points of the diagonal primordial field G2. Stage 1 recorded the diagonal statement as `GEO_anticommutatorGammaOmegaVanishesDiagonal_G2`.)

**The connection enters the field equation.** Theorem 6.4 does not mean that gravity decouples in a diagonal field. When the field equation is derived (Section 7.2), the derivative of $\sqrt{|g|}\,\gamma^\mu$ appears through an integration by parts, and the divergence identity (B6) turns it into the commutator $[\gamma^\mu,\Omega_\mu]$. The field equation is $\gamma^\mu D_\mu\Psi=M_{\mathrm{eff}}\Psi$, which contains the matrix

$$
\gamma^\mu\Omega_\mu .
$$

For a diagonal vielbein $\{\gamma^\mu,\Omega_\mu\}=0$ (Section 4.12), so $[\gamma^\mu,\Omega_\mu]=2\gamma^\mu\Omega_\mu$, and (B6) gives

$$
\gamma^\mu\Omega_\mu=\frac{1}{2\sqrt{|g|}}\,\partial_\mu\bigl(\sqrt{|g|}\,\gamma^\mu\bigr).
$$

This shows how the coupling through $\sqrt{|g|}$ and $\gamma^\mu$ becomes a connection term. In the notebook's primordial field this matrix is $3H\gamma^0$ (Section 4.12), and at the points of the general test geometry G1 it has 128 nonzero entries. The spin-connection term of the field equation is nonzero in all 16 components at every G1 and G2 point (checks `C00_connection_nonTrivialCoupling`, `C00_connection_OmegaTermInFieldEquation`, `S5_connection_nonTrivialCoupling`, `S5_connection_OmegaTermInFieldEquation`). It cannot be removed by any choice of frame unless the Riemann tensor vanishes (Section 4.13), and the curvature appears explicitly in the second-order form of the field equation through the term $-\tfrac14R\Psi$ of the Lichnerowicz formula (Section 4.13), with the constant $-\tfrac14$ measured again for the commuting field at seven test points (G1 p1 to p3, G2 p1 to p3 and a point of a further generic non-diagonal integer frame, G4; measurement `lichnerowiczC` in `C00_connection_nonTrivialCoupling`). The operator $\gamma^\mu D_\mu$ does not know the statistics of the components, so all of this holds for both fields.

### 6.9 Continuous symmetries of the Lagrangian

**Local frame rotations.** Let the frame be turned, $e'_\mu{}^a=\Lambda^a{}_b(x)e_\mu{}^b$, and let the field change by a covering spin transformation $R(x)$ of spinor norm $+1$, in particular any element of $\mathrm{Spin}_0(4,4)$ (Sections 2.14 and 4.12). Then $\mathcal L$ does not change. *Proof.* Chapter 4 showed $\gamma'^\mu=R\gamma^\mu R^{-1}$ and $D'_\mu(R\Psi)=R\,D_\mu\Psi$ (Section 4.12). From $R^TCR=C$ we get $(R\Psi)^\dagger C=\Psi^\dagger R^TC=\bar\Psi R^{-1}$ (the matrix $R$ is real). Hence $\bar\Psi'\gamma'^\mu D'_\mu\Psi'=\bar\Psi R^{-1}R\gamma^\mu R^{-1}R\,D_\mu\Psi=\bar\Psi\gamma^\mu D_\mu\Psi$, the same for the second half of $K$, and $S'=S$. The metric, and so $\sqrt{|g|}$, is unchanged. $\square$ (Stage-1 document, §7.5; checks `LAG_localSpinInvariance_G1` and `LAG_localSpinInvariance_G2`.) The proof used $R^TCR=C$. By Theorem 2.8 a product $g$ of $k$ unit vectors has $g^TCg=(-1)^kN(g)\,C$, so the factor that decides whether $S$ is kept is $(-1)^kN(g)$, not the spinor norm $N(g)$ alone. Elements with $(-1)^kN(g)=-1$ reverse the sign of $S$: for example a single space-like unit vector $\gamma^b$ ($b\le3$, $k=1$, $N=+1$) and the even element $\gamma^0\gamma^4$ ($k=2$, $N=-1$), whereas a single time-like $\gamma^b$ ($b\ge4$, $k=1$, $N=-1$) keeps $S$. The single unit vectors $\gamma^b$, used as reflections, are treated in Section 6.12.

**Changes of coordinates.** Every index in $\mathcal L_s$ is contracted, so $\mathcal L_s$ is a scalar, and $\sqrt{|g|}\,d^8x$ is invariant (Section 4.4): the action does not depend on the coordinates.

**The global phase.** For a constant real $\alpha$, the change $\Psi\to e^{i\alpha}\Psi$ sends $\Psi^\dagger\to e^{-i\alpha}\Psi^\dagger$. Every term of $\mathcal L$ contains as many factors from $\Psi^\dagger$ as from $\Psi$, so each is multiplied by $e^{-i\alpha}e^{i\alpha}=1$. For Grassmann components the substitution $\Psi_a\to e^{i\alpha}\Psi_a$, $\Psi_a^\ast\to e^{-i\alpha}\Psi_a^\ast$ preserves the order of every product and all the algebra rules, and the same counting applies to every polynomial $U(S)$. So the phase is a symmetry of both fields for every potential (the matter–antimatter document, §4, Theorem M1; checks `MA_M1_u1InvarianceCommutingGenericU_G1` and `MA_M1_u1InvarianceGrassmann_G1`). Chapter 7 derives the conserved current $J^\mu=-i\bar\Psi\gamma^\mu\Psi$ that belongs to it.

### 6.10 The real restriction and the notebook's $\mathrm{Lg}[\,]$

The notebook's Lagrangian of Section 5.12 uses a **real** column $\Psi$ and the transpose instead of the Dirac adjoint. In the notation of this book, with the canonical connection,

$$
\mathrm{Lg}=\sqrt{|g|}\,\Bigl[\Psi^TC\gamma^\mu D_\mu\Psi+(HM)\,\Psi^TC\Psi\Bigr].
$$

**Real Grassmann components: nothing.** Theorem 5.6 proved that for a real Grassmann column $\mathrm{Lg}$ is the total divergence $\partial_\mu\bigl(\tfrac12\sqrt{|g|}\,\Psi^TC\gamma^\mu\Psi\bigr)$ in every gravitational field; its mass term vanishes identically because $C$ is symmetric (Lemma 5.4), and all its Euler–Lagrange expressions vanish. Stage 5 re-ran this in flat space and at the point G1 p1 of the general test geometry: the Wolfram check with Stage 1's Grassmann algebra (as its report states), the Python check with the exact Grassmann module `scripts/grassmann_algebra.py` of the Python checkers, a separate program (checks `C00_realRestriction_grassmannFlatTrivial`, `C00_realRestriction_grassmannCurvedTrivial` and their `S5_` twins; $\mathrm{Lg}$ has 544 monomials at G1 p1, a number measured there, and is nevertheless a pure divergence).

**Real commuting components: a genuine Lagrangian.** For ordinary numbers Lemma 5.4 is reversed: in $q^TMq$ only the symmetric part of $M$ survives. So now the mass term survives, and the kinetic term is not a total derivative.

**Theorem 6.5.** Let $X(x)$ be a real column of 16 commuting functions. The Euler–Lagrange expression of $\mathrm{Lg}[X]$ with the canonical connection is

$$
E_{\mathrm{Lg}}=2\sqrt{|g|}\;C\,\bigl(\gamma^\mu D_\mu X+HM\,X\bigr),
$$

so the field equation of $\mathrm{Lg}$ is the Dirac equation $\gamma^\mu D_\mu X=mX$ with $m=-HM$.

*Proof.* Write $\mathrm{Lg}=\sqrt{|g|}\bigl[X^TC\gamma^\mu\partial_\mu X+X^TC\gamma^\mu\Omega_\mu X+HM\,X^TCX\bigr]$ and vary the component $X_c$ (Section 5.3). The derivative of $\mathrm{Lg}$ with respect to $X_c$ gets one contribution from each factor $X$ in a product:

$$
\frac{\partial\mathrm{Lg}}{\partial X_c}=\sqrt{|g|}\,\Bigl[(C\gamma^\mu\partial_\mu X)_c+(C\gamma^\mu\Omega_\mu X)_c+\bigl((C\gamma^\mu\Omega_\mu)^TX\bigr)_c+2HM\,(CX)_c\Bigr],
$$

where the factor 2 comes from the two factors $X$ of $X^TCX$ and the symmetry of $C$. The derivative with respect to $\partial_\mu X_c$ is $\sqrt{|g|}\,\bigl((C\gamma^\mu)^TX\bigr)_c=-\sqrt{|g|}\,(C\gamma^\mu X)_c$, by expression [1]. So the Euler–Lagrange expression is

$$
E_{\mathrm{Lg}}=\sqrt{|g|}\Bigl[C\gamma^\mu\partial_\mu X+C\gamma^\mu\Omega_\mu X+(C\gamma^\mu\Omega_\mu)^TX+2HM\,CX\Bigr]+\partial_\mu\bigl(\sqrt{|g|}\,C\gamma^\mu X\bigr).
$$

Two facts finish the computation. First, $(C\gamma^cS^{ab})^T=CS^{ab}\gamma^c$ (Section 5.12), so $(C\gamma^\mu\Omega_\mu)^T=C\Omega_\mu\gamma^\mu$. Second, by (B6), $\partial_\mu(\sqrt{|g|}\,C\gamma^\mu X)=\sqrt{|g|}\,C\bigl([\gamma^\mu,\Omega_\mu]X+\gamma^\mu\partial_\mu X\bigr)$. Inserting both,

$$
\begin{aligned}
E_{\mathrm{Lg}}&=\sqrt{|g|}\,C\Bigl[2\gamma^\mu\partial_\mu X+\gamma^\mu\Omega_\mu X+\Omega_\mu\gamma^\mu X+\gamma^\mu\Omega_\mu X-\Omega_\mu\gamma^\mu X+2HM\,X\Bigr]\\
&=2\sqrt{|g|}\,C\bigl(\gamma^\mu D_\mu X+HM\,X\bigr). \qquad\square
\end{aligned}
$$

Neither part is trivial. The mass part $2\sqrt{|g|}\,HM\,CX$ is nonzero for every $X\ne0$ because $C$ is invertible, and the coefficient of $\partial_4X$ is $2\sqrt{|g|}\,C\gamma^{x_4}$, which is invertible whenever $g^{44}\ne0$ (Section 8.5 proves $(C\gamma^{x_4})(\gamma^{x_4}C)=g^{44}$), so the equation determines the time derivative. The matrices $\gamma^\mu$ and $\Omega_\mu$ are real, so real solutions exist. (Checks `C00_realRestriction_commutingNonTrivial` and `S5_realRestriction_commutingNonTrivial`: at three G1 points and in the primordial field the Euler–Lagrange expression is exactly $2\sqrt{|g|}\,C(\gamma^\mu D_\mu X+HM\,X)$, and neither the mass part nor the kinetic part is a total divergence.)

**With the notebook's own contraction.** If $\Omega_\mu$ in $\mathrm{Lg}$ is replaced by the notebook's $\Omega^{\mathrm{nb}}_\mu$ (Section 4.14), the step $(C\gamma^\mu\Omega^{\mathrm{nb}}_\mu)^T=C\Omega^{\mathrm{nb}}_\mu\gamma^\mu$ still holds ($\Omega^{\mathrm{nb}}_\mu$ is also a combination of the $S^{ab}$), but the divergence identity still contains the correct $\Omega_\mu$. Repeating the computation leaves the extra term

$$
E_{\mathrm{Lg}}^{\mathrm{nb}}=2\sqrt{|g|}\,C\bigl(\gamma^\mu D_\mu X+HM\,X\bigr)+\sqrt{|g|}\,C\,\{\gamma^\mu,\Omega^{\mathrm{nb}}_\mu-\Omega_\mu\}\,X .
$$

For a diagonal vielbein both anticommutators vanish (Section 5.14), so in the notebook's primordial field the wrong contraction drops out of the equations for commuting fields; in the non-diagonal G1 the extra term is nonzero (checks `C00_realRestriction_commutingNotebookContraction` and `S5_realRestriction_commutingNotebookContraction`).

**How $\mathrm{Lg}$ sits inside the Lagrangian of dirac16complex00.** For commuting components write $\Psi=X+iY$ with real columns $X,Y$, and put $K_R[Z]:=Z^TC\gamma^\mu D_\mu Z$ and $S_Z:=Z^TCZ$ for a real column $Z$.

**Theorem 6.6.** For commuting components, $S=S_X+S_Y$, $K=K_R[X]+K_R[Y]$, and therefore

$$
\mathcal L[X+iY]=\sqrt{|g|}\,\Bigl[K_R[X]+K_R[Y]-m\bigl(S_X+S_Y\bigr)-U\bigl(S_X+S_Y\bigr)\Bigr].
$$

For $U=0$ this is $\mathrm{Lg}[X]+\mathrm{Lg}[Y]$ with $HM=-m$.

*Proof.* $S=(X^T-iY^T)C(X+iY)=X^TCX+Y^TCY+i(X^TCY-Y^TCX)$, and $X^TCY=Y^TCX$ for commuting numbers and symmetric $C$. For the kinetic term, $\bar\Psi\gamma^\mu D_\mu\Psi=(X^T-iY^T)C\gamma^\mu(D_\mu X+iD_\mu Y)$ has the real part $X^TC\gamma^\mu D_\mu X+Y^TC\gamma^\mu D_\mu Y$ and the imaginary part $X^TC\gamma^\mu D_\mu Y-Y^TC\gamma^\mu D_\mu X$. In the same way $(D_\mu\bar\Psi)\gamma^\mu\Psi$ has the real part $(D_\mu X)^TC\gamma^\mu X+(D_\mu Y)^TC\gamma^\mu Y$ and the imaginary part $(D_\mu X)^TC\gamma^\mu Y-(D_\mu Y)^TC\gamma^\mu X$. A number equals its own transpose, and $(C\gamma^\mu)^T=-C\gamma^\mu$, so $(D_\mu Z)^TC\gamma^\mu W=-W^TC\gamma^\mu D_\mu Z$ for any real $Z,W$. Therefore the real part of $(D_\mu\bar\Psi)\gamma^\mu\Psi$ is $-K_R[X]-K_R[Y]$, and its imaginary part is $-Y^TC\gamma^\mu D_\mu X+X^TC\gamma^\mu D_\mu Y$, equal to the imaginary part of the first product. In $K=\tfrac12(\text{first}-\text{second})$ the imaginary parts cancel and the real parts add: $K=K_R[X]+K_R[Y]$. $\square$

So the Lagrangian of dirac16complex00 is the **complexification** of the notebook's real Lagrangian: two copies of $\mathrm{Lg}$, one for the real part and one for the imaginary part of the field, coupled only through $U$. Setting $Y=0$ is consistent: the Euler–Lagrange expression for $Y$ is $2\sqrt{|g|}\,C\bigl(\gamma^\mu D_\mu Y-(m+U'(S))Y\bigr)$ (Theorem 6.5 with $U$ added), which vanishes at $Y=0$. With $Y=0$ the field equation of $X$ is $\gamma^\mu D_\mu X=\bigl(m+U'(S_X)\bigr)X$. For $U=0$ this is the notebook's equation $\gamma^\mu D_\mu X=mX$ with $m=-HM$ (Theorem 6.5); with a potential the mass $m$ is replaced by $m+U'(S_X)$, a term that the notebook's $\mathrm{Lg}[\,]$ does not contain. In this precise sense, **for $U=0$ the real restriction of dirac16complex00 is the notebook's $\mathrm{Lg}[\,]$ with the canonical connection**, with $U\ne0$ it is $\mathrm{Lg}[\,]$ plus the self-interaction $-\sqrt{|g|}\,U(S_X)$, and $\mathrm{Lg}[\,]$ is a genuine Lagrangian for commuting fields (checks `C00_realRestriction_relationToL1`, whose recorded $X$ equation is $2\sqrt{|g|}\,C\bigl(\gamma^\mu D_\mu X-(m+\lambda S_X)X\bigr)$ for the default potential, `C00_realRestriction_commutingFlatDecomposition` and their `S5_` twins).

**For Grassmann components the opposite happens.** Write $\Psi=\rho+i\iota$ with real Grassmann columns $\rho,\iota$. Then $\rho^TC\rho=\iota^TC\iota=0$ (Lemma 5.4), and $\iota^TC\rho=\sum_{a,b}\iota_aC_{ab}\rho_b=-\sum_{a,b}\rho_bC_{ab}\iota_a=-\rho^TC\iota$, so

$$
S=\rho^TC\rho+\iota^TC\iota+i\bigl(\rho^TC\iota-\iota^TC\rho\bigr)=2i\,\rho^TC\iota :
$$

the mass term of the complex Grassmann field is a pure cross term between its real and imaginary parts, and each real part alone carries neither a mass term nor (Theorem 5.6) any dynamics (checks `C00_realRestriction_grassmannComplexDecomposition` and `S5_realRestriction_grassmannComplexDecomposition`). This is why dirac16complex must be complex.

### 6.11 The chirality map $\gamma^8$ of the Lagrangians

The chirality $\gamma^8=\gamma^0\gamma^1\cdots\gamma^7=\mathrm{diag}(-I_8,I_8)$ of Section 2.10 multiplies the upper eight components by $-1$ and leaves the lower eight unchanged. Mapping $\Psi$ to $\gamma^8\Psi$ turns the Lagrangian with mass $m$ into minus the Lagrangian with mass $-m$. This is the Lagrangian form of the pairing of the masses $\pm m$ that Chapter 15 develops into the pairing theorems.

**Five facts about $\gamma^8$** (all proved in Section 2.10 or immediate from them): (G1) $\gamma^8$ is real and diagonal, hence Hermitian; (G2) $(\gamma^8)^2=1$; (G3) $\gamma^8\gamma^a=-\gamma^a\gamma^8$ for every $a$; (G4) $\gamma^8$ commutes with $C$ and with every $S^{ab}$, both even products of gammas; (G5) consequently $\gamma^8$ commutes with every $\Omega_\mu$, in every gravitational field, and anticommutes with every $\gamma^\mu=e_a{}^\mu\gamma^a$. (Checks `PAIR_algebra_gamma8Properties` and `C00_algebra_leadFacts`.)

**Theorem 6.7 (the $\gamma^8$ map).** For every vielbein, every mass $m$, every potential $U$ and every field configuration $\Psi$ (not necessarily a solution), for both kinds of components,

$$
\mathcal L_{m,U}[\gamma^8\Psi]=-\mathcal L_{-m,-U}[\Psi],\qquad\text{in particular}\qquad \mathcal L_{m,\lambda}[\gamma^8\Psi]=-\mathcal L_{-m,-\lambda}[\Psi].
$$

*Proof.* Put $\Psi_-:=\gamma^8\Psi$.

1. The adjoint: $\bar\Psi_-=(\gamma^8\Psi)^\dagger C=\Psi^\dagger\gamma^8C=\Psi^\dagger C\gamma^8=\bar\Psi\gamma^8$, by (G1) and (G4).
2. The derivatives: by (G5), $D_\mu(\gamma^8\Psi)=\gamma^8\partial_\mu\Psi+\Omega_\mu\gamma^8\Psi=\gamma^8D_\mu\Psi$, and in the same way $D_\mu\bar\Psi_-=(D_\mu\bar\Psi)\gamma^8$.
3. The scalar density: $S[\Psi_-]=\bar\Psi\gamma^8\gamma^8\Psi=S[\Psi]$ by (G2).
4. The kinetic term: $\bar\Psi_-\gamma^\mu D_\mu\Psi_-=\bar\Psi\gamma^8\gamma^\mu\gamma^8D_\mu\Psi=-\bar\Psi\gamma^\mu D_\mu\Psi$ by (G5) and (G2), and likewise $(D_\mu\bar\Psi_-)\gamma^\mu\Psi_-=-(D_\mu\bar\Psi)\gamma^\mu\Psi$. So $K[\Psi_-]=-K[\Psi]$.
5. Therefore $\mathcal L_{m,U}[\Psi_-]=\sqrt{|g|}\bigl[-K-mS-U(S)\bigr]=-\sqrt{|g|}\bigl[K-(-m)S-(-U)(S)\bigr]=-\mathcal L_{-m,-U}[\Psi]$.

For Grassmann components nothing was reordered: in the notebook's basis the map is the substitution $\Psi_a\to-\Psi_a$, $\Psi_a^\ast\to-\Psi_a^\ast$ for $a\le7$ (and nothing for $a\ge8$), which respects every rule of the Grassmann algebra. $\square$

In words: the mass term and the interaction do not change, the kinetic term changes sign, and so the image is the theory with the opposite sign of the whole Lagrangian and the opposite mass. Because the potential does not change sign under the map, it must be given the opposite sign on the right-hand side: for the default potential the map relates $(m,\lambda)$ to $(-m,-\lambda)$, **not** to $(-m,\lambda)$. Indeed

$$
\mathcal L_{m,\lambda}[\gamma^8\Psi]+\mathcal L_{-m,\lambda}[\Psi]=\sqrt{|g|}\bigl[-K-mS-\tfrac\lambda2S^2+K+mS-\tfrac\lambda2S^2\bigr]=-\lambda\sqrt{|g|}\,S^2\ne0
$$

for $\lambda\ne0$. The simpler statement "$\mathcal L_m\to-\mathcal L_{-m}$" of the original project contract holds only for $U=0$; this is erratum E2 of `handoff/specs/CONTRACT.md` (§11). (Checks: `ALG_gamma8Map` of Stage 1; `PAIR_T1generic_lagrangian` as an identity in completely generic symbols, `PAIR_T1grassmann_lagrangian` in a Grassmann algebra of 288 odd generators, `PAIR_T1jets_lagrangian` with exact jets of the general vielbein G1, `PAIR_T1primordial_lagrangian` for arbitrary fields in the primordial field; `PAIR_T1generic_naiveFixedLambdaFails` for the fixed-$\lambda$ failure.)

**The same map, seen as reversing the frame.** Change the vielbein to $-e_\mu{}^a$ and keep $\Psi$. The metric $g=e\eta e^T$ and $\sqrt{|g|}=|\det e|$ do not change ($\det(-e)=(-1)^8\det e$); the inverse vielbein and the curved gammas change sign; the Christoffel symbols do not change, and neither does the spin connection, because in $\omega_\mu{}^a{}_b=e_b{}^\nu(\Gamma^\rho{}_{\mu\nu}e_\rho{}^a-\partial_\mu e_\nu{}^a)$ (Section 4.11) both factors change sign. So the kinetic term changes sign and $S$ does not: $\mathcal L_{m,\lambda}[-e,\Psi]=-\mathcal L_{-m,-\lambda}[e,\Psi]$, the same as Theorem 6.7. Together the two changes cancel: $\mathcal L_{m,\lambda}[-e,\gamma^8\Psi]=\mathcal L_{m,\lambda}[e,\Psi]$. This is no accident. The frame change $-1_8$ is a rotation by $\pi$ in each of the four planes $(0,1)$, $(2,3)$, $(4,5)$, $(6,7)$, and its spin cover is $\exp(\pi S^{01})\exp(\pi S^{23})\exp(\pi S^{45})\exp(\pi S^{67})=\gamma^0\gamma^1\,\gamma^2\gamma^3\,\gamma^4\gamma^5\,\gamma^6\gamma^7=\gamma^8$ (use $\exp(\pi S^{ab})=\gamma^a\gamma^b$ for a rotation, Exercise 2.14, and note that $(4,5)$ and $(6,7)$ are rotations because $\eta^{44}\eta^{55}=\eta^{66}\eta^{77}=+1$). So $(e,\Psi)\to(-e,\gamma^8\Psi)$ is a local frame rotation of Section 6.9, under which $\mathcal L$ is invariant, and the $\gamma^8$ map of Theorem 6.7 is the same as reversing all eight frame directions at a fixed field (checks `PAIR_algebra_gamma8InIdentityComponent`, `PAIR_T1jets_vielbeinSignFlipGeometry`, `PAIR_T1jets_vielbeinSignFlipIsT1`, `PAIR_T1jets_gamma8WithFrameSignIsSymmetry`).

**Worked example.** Flat space, the constant commuting field $\Psi=e_0+e_4+i\,e_{12}$. Its scalar density is $S=-2$ (the pair $e_0,e_4$ gives $-2$ as in Section 6.3, and $e_{12}$ pairs only with $e_8$, which is absent). The current $J^a=-i\bar\Psi\gamma^a\Psi$ of Chapter 7 has two nonzero components. For example $(C\gamma^0)_{0,12}=-1$ and $(C\gamma^0)_{12,0}=+1$ (Section 5.12), so $\bar\Psi\gamma^0\Psi=\Psi_0^\ast(-1)\Psi_{12}+\Psi_{12}^\ast(+1)\Psi_0=-i-i=-2i$ and $J^0=-2$; in the same way $J^7=+2$. The image $\gamma^8\Psi=-e_0-e_4+i\,e_{12}$ has $S=-2$ again and $J^0=+2$, $J^7=-2$: the scalar is unchanged and the vector bilinears change sign. The field is constant, so $K=0$, and for $U=\tfrac\lambda2S^2$ both $\mathcal L_{m,\lambda}[\gamma^8\Psi]$ and $-\mathcal L_{-m,-\lambda}[\Psi]=-\bigl(2(-m)-2(-\lambda)\bigr)$ equal $2m-2\lambda$.

**What the map does and does not say.** Chapter 7 derives the consequences for the field equations (solutions with $(m,\lambda)$ go to solutions with $(-m,-\lambda)$), for the energy–momentum tensor ($T_{\mu\nu}\to-T_{\mu\nu}$) and for the current ($J^\mu\to-J^\mu$). Chapter 15 turns these into the pairing theorems. The Stage-1 document states their nature in one sentence, which this book repeats: the pairing of $\pm m$ is "a structural property of the equations, not a claim that universes of masses $\pm M$ are created in pairs" (Stage-1 document, §1.3, item 6). Chapter 16 explains exactly what is and what is not established.

### 6.12 Two more discrete maps: reflections and complex conjugation

Two other kinds of discrete map relate the Lagrangians with different signs of the mass, and one of them shows the first place where the statistics decides whether a map is a symmetry. We derive the reflections in flat space (their curved-space form, in which the frame is reflected together with the field, is recorded in the reports named below and proved in Chapter 15) and the complex conjugations in every gravitational field.

**Reflections.** For a frame direction $b$ let $R_b$ reverse the coordinate $x_b$, and write $r_a=-1$ for $a=b$ and $r_a=+1$ otherwise. Define

$$
\Psi'(x)=\gamma^b\,\Psi(R_bx).
$$

This is the action of the unit vector $\gamma^b$ of Pin(4,4) (Section 2.14), in the lift that Stage 5 calls twisted.

**Theorem 6.8.** In flat space, for both kinds of components, with $n_b=\eta^{bb}$: $K\to n_b\,K$ and $S\to-n_b\,S$ (evaluated at the reflected point). Consequently

$$
\mathcal L_{m,\lambda}[\Psi']=\mathcal L_{-m,\lambda}[\Psi]\quad(b\le3,\ \text{space-like}),\qquad \mathcal L_{m,\lambda}[\Psi']=-\mathcal L_{-m,-\lambda}[\Psi]\quad(b\ge4,\ \text{time-like}).
$$

*Proof.* $\Psi'^\dagger=\Psi^\dagger(\gamma^b)^T$ and, by the chain rule, $\partial_a\Psi'(x)=r_a\gamma^b(\partial_a\Psi)(R_bx)$. From (B2), $(\gamma^b)^TC=-C\gamma^b$. Hence $(\gamma^b)^TC\gamma^b=-C(\gamma^b)^2=-n_bC$, which gives $S\to-n_bS$. For the kinetic matrices, $(\gamma^b)^TC\gamma^a\gamma^b=-C\gamma^b\gamma^a\gamma^b$. For $a\ne b$, $\gamma^b\gamma^a\gamma^b=-\gamma^a(\gamma^b)^2=-n_b\gamma^a$, so the product is $n_bC\gamma^a$, and $r_a=+1$. For $a=b$, $\gamma^b\gamma^b\gamma^b=n_b\gamma^b$, so the product is $-n_bC\gamma^b$, and $r_b=-1$. In both cases $r_a(\gamma^b)^TC\gamma^a\gamma^b=n_b\,C\gamma^a$, and both halves of $K$ are multiplied by $n_b$. For $n_b=+1$: $\mathcal L\to K+mS-\tfrac\lambda2S^2=\mathcal L_{-m,\lambda}$. For $n_b=-1$: $\mathcal L\to-K-mS-\tfrac\lambda2S^2=-\mathcal L_{-m,-\lambda}$. $\square$

A reflection of a space-like direction therefore relates $m$ to $-m$ **with the same** $\lambda$ and the same sign of the Lagrangian. In a curved field the same statement holds when the frame is reflected together with the field (Stage 5 calls this the mirror map T2; Chapter 15 proves it). The other lift, $\Psi'=\Gamma\Psi(R_bx)$ with $\Gamma$ the product of the seven gammas other than $\gamma^b$ (which is $\pm\gamma^8\gamma^b$), has $K\to-n_bK$, $S\to-n_bS$: it gives $-\mathcal L_{m,-\lambda}$ for a space-like $b$ and an exact symmetry for a time-like $b$ (erratum E3 of the contract). The factor $-n_b$ of $S$ is the Pin character of Section 2.14. (Checks `ALG_pinLiftCharacter`, `MA_M2_namedReflectionsFlatJets`, `PAIR_T2frame_twistedSpacelikeMapsToMinusMSameLambda`, `PAIR_T2frame_twistedTimelike`, `PAIR_T2frame_untwistedSpacelikeContractE3`.)

**Complex conjugation.** Now let $\Psi'=\Psi^\ast$ (the map called $C_0$) or $\Psi'=\gamma^8\Psi^\ast$ (called $C_8$). Here a reordering cannot be avoided, and it produces the **statistics sign** $s$, with $s=+1$ for commuting and $s=-1$ for Grassmann components.

**Lemma 6.9 (statistics sign).** For columns $\Psi,\Phi$ of the same kind and any numerical matrix $Y$, $\Psi^TY\Phi^\ast=s\,\Phi^\dagger Y^T\Psi$.

*Proof.* $\sum_{a,b}\Psi_aY_{ab}\Phi_b^\ast=s\sum_{a,b}\Phi_b^\ast Y_{ab}\Psi_a$, because exchanging two odd factors costs a sign and exchanging two commuting ones does not. $\square$

**Theorem 6.10.** In every gravitational field: $C_0$ sends $K\to s\,K$ and $S\to s\,S$; $C_8$ sends $K\to-s\,K$ and $S\to s\,S$. Hence

| map | commuting components ($s=+1$) | Grassmann components ($s=-1$) |
| --- | --- | --- |
| $C_0$: $\Psi\to\Psi^\ast$ | $\mathcal L_{m,\lambda}$ (exact symmetry) | $-\mathcal L_{m,-\lambda}$ |
| $C_8$: $\Psi\to\gamma^8\Psi^\ast$ | $-\mathcal L_{-m,-\lambda}$ | $\mathcal L_{-m,\lambda}$ |

*Proof for $C_0$.* The conjugate of $\Psi'=\Psi^\ast$ is $\Psi$, so $\Psi'^\dagger=\Psi^T$. The gammas and $\Omega_\mu$ are real, so $D_\mu\Psi^\ast=(D_\mu\Psi)^\ast$. By Lemma 6.9 with $Y=C$ (symmetric), $S'=\Psi^TC\Psi^\ast=s\,\Psi^\dagger C\Psi=sS$. With $Y=C\gamma^\mu$ (antisymmetric), $\Psi^TC\gamma^\mu D_\mu\Psi^\ast=s\,(D_\mu\Psi)^\dagger(C\gamma^\mu)^T\Psi=-s\,(D_\mu\bar\Psi)\gamma^\mu\Psi$ and $-(D_\mu\Psi)^TC\gamma^\mu\Psi^\ast=-s\,\Psi^\dagger(C\gamma^\mu)^TD_\mu\Psi=s\,\bar\Psi\gamma^\mu D_\mu\Psi$. So $K'=\tfrac12\bigl(s\bar\Psi\gamma^\mu D_\mu\Psi-s(D_\mu\bar\Psi)\gamma^\mu\Psi\bigr)=sK$. For $s=+1$ nothing changes; for $s=-1$, $\mathcal L\to\sqrt{|g|}[-K+mS-\tfrac\lambda2S^2]=-\mathcal L_{m,-\lambda}$. *For $C_8$*, compose with Theorem 6.7 ($K\to-K$, $S\to S$). $\square$

The charge density $J^4=\Psi^\dagger B\Psi$ of Chapter 7 transforms under $C_0$ into $\Psi^TB\Psi^\ast=s\Psi^\dagger B^T\Psi=-s\,J^4$ (since $B^T=-B$). So for the commuting field $C_0$ is an exact symmetry that **reverses the charge**: it is the charge conjugation of dirac16complex00. For the Grassmann field no constant charge conjugation is a symmetry when $m\ne0$: $C_0$ reverses the sign of the Lagrangian and of $\lambda$, and $C_8$ reverses the mass; and Lemma A of Theorem M2 (quoted here, not proved) shows that every constant charge conjugation compatible with the Dirac operator is, up to a constant factor, $C_0$ or $C_8$. But $C_8$ combined with the reflection of one space-like direction (Theorem 6.8, which also sends $m\to-m$ with the same $\lambda$) is an exact symmetry of dirac16complex, of the kind called CP, and it reverses the charge. These classifications are Theorem M2 of the matter–antimatter document (its §5.3 to §5.5, verified for all 1024 maps of this kind for each statistics; checks `MA_M2_lagrangianFlatCommuting_all`, `MA_M2_lagrangianFlatGrassmann_all`, `MA_M2_internalMapsCurvedJets`, `MA_M2_C_and_CP_status`). Chapter 17 explains what they mean for matter and antimatter.

### 6.13 How the repository checks all of this

Every statement of Sections 6.2 to 6.12 that the repository verifies is listed with its checks. "Both" means the Wolfram check (`C00_...`) and its independent Python twin (`S5_...` with the same ending, in `python-dirac16complex00-report.json`). Each `PAIR_` check of `wolfram-pairing-report.json` has a Python twin as well: the `S5_` check with the same ending in `python-pairing-report.json` (for example `S5_T1generic_lagrangian`).

| statement (section) | checks |
| --- | --- |
| same Pin(4,4) module for both fields; invariant forms $CP_\mp$; $\bar\Psi\Psi$ invariant (6.2, 6.3) | `C00_algebra_pinModuleAndSpinInvariance` (both) |
| $\gamma^8$, $C$, $B$ facts (6.3, 6.11) | `C00_algebra_leadFacts` (both), `PAIR_algebra_gamma8Properties` |
| reality for both statistics; unsymmetrized term not real (6.5) | `C00_lagrangian_realCommuting`, `C00_lagrangian_coefficientHermiticity`, `C00_lagrangian_grassmannFlatHermitianAndEL` (both); `LAG_hermiticity_G1`, `_G2`; `GR_lagrangianHermitian` |
| mass term non-zero; dispersion $\omega^2=m^2+\dots$ (6.6) | `C00_massTerm_commutingExplicitSpinors`, `C00_massTerm_grassmannNonzero`, `C00_massTerm_dispersionFlat` (both) |
| any smooth $U$ for the commuting field (6.7) | `C00_EL_commutingGeneralSmoothU`, `C00_EMT_generalSmoothU` (both) |
| only $\omega_{[cab]}$ in the Lagrangian; connection in the field equation (6.8) | `C00_algebra_anticommutatorTotallyAntisymmetric`, `C00_connection_nonTrivialCoupling`, `C00_connection_OmegaTermInFieldEquation` (both) |
| local spin invariance (6.9) | `LAG_localSpinInvariance_G1`, `LAG_localSpinInvariance_G2` |
| real restriction: trivial (Grassmann), non-trivial (commuting) (6.10) | `C00_realRestriction_grassmannFlatTrivial`, `C00_realRestriction_grassmannCurvedTrivial`, `C00_realRestriction_commutingNonTrivial`, `C00_realRestriction_commutingNotebookContraction` (both) |
| $\mathcal L[X+iY]=\mathrm{Lg}[X]+\mathrm{Lg}[Y]$; Grassmann cross term (6.10) | `C00_realRestriction_relationToL1`, `C00_realRestriction_commutingFlatDecomposition`, `C00_realRestriction_grassmannComplexDecomposition` (both) |
| $\mathcal L_{m,\lambda}[\gamma^8\Psi]=-\mathcal L_{-m,-\lambda}[\Psi]$ (6.11) | `ALG_gamma8Map`; `PAIR_T1generic_lagrangian`, `PAIR_T1grassmann_lagrangian`, `PAIR_T1jets_lagrangian`, `PAIR_T1primordial_lagrangian` |
| reflections and conjugations (6.12) | `ALG_pinLiftCharacter`; `PAIR_T2frame_*`; `MA_M2_*` |

The reports live in three folders, for Stage 1, for Stage 5 and for the matter–antimatter analysis:

```
artifacts/dirac16complex/arbitrary-field/
artifacts/dirac16complex/pair-creation/
artifacts/dirac16complex/matter-antimatter/
```

Every check named here is true in the committed reports. To count the checks of the two dirac16complex00 reports, use the method of Section 0.8 with the paths

```
artifacts/dirac16complex/pair-creation/wolfram-dirac16complex00-report.json
artifacts/dirac16complex/pair-creation/python-dirac16complex00-report.json
```

which gives `(46, 46)` and `(49, 49)`. The Python checker also reads the Wolfram report and compares the exact values that both compute (check `S5_agreesWithWolfram`).

### 6.14 What we proved and what we assumed

**What we proved.** With complete derivations in this chapter: the invariant bilinear forms of the spin generators are exactly the combinations of $CP_-$ and $CP_+$ (Section 6.2, from Theorem 2.12); $\bar\Psi\Psi$ is invariant under spin rotations while $\Psi^\dagger\Psi$ is not (worked example with a boost), and $\bar\Psi\gamma^a\Phi$ is a vector; the conjugate of a bilinear is $\Phi^\dagger M^\dagger\Psi$ for commuting and for Grassmann components (Lemma 6.1), and the Lagrangian is real for both (Theorem 6.2), the symmetrization differing from the plain kinetic term by an imaginary total derivative; the mass term is linear in $m$, quadratic in the components and non-zero for both kinds of components, and it is non-trivial because it enters the dispersion relation as $m^2$, with an 8-dimensional space of plane-wave solutions on the mass shell for $m\ne0$; for Grassmann components the interaction can only be a polynomial of degree at most 16, while for commuting components it can be any smooth function; only the totally antisymmetric part of the spin connection appears in the Lagrangian, and none of it for a diagonal vielbein (Lemma 6.3, Theorem 6.4), while the field equation contains $\gamma^\mu\Omega_\mu=\tfrac1{2\sqrt{|g|}}\partial_\mu(\sqrt{|g|}\gamma^\mu)$ in diagonal frames; the Lagrangian is invariant under local frame rotations of spinor norm $+1$, changes of coordinates and the global phase, while Pin elements with $(-1)^kN(g)=-1$ reverse the sign of $S$; for real commuting fields the notebook's $\mathrm{Lg}[\,]$ gives the Dirac equation with $m=-HM$ (Theorem 6.5), and the Lagrangian of dirac16complex00 is two copies of it coupled through $U$ (Theorem 6.6), so that its real restriction is $\mathrm{Lg}[\,]$ for $U=0$ and $\mathrm{Lg}[\,]$ plus the self-interaction otherwise, whereas for Grassmann fields the mass term is a pure cross term between real and imaginary parts; the chirality map gives $\mathcal L_{m,U}[\gamma^8\Psi]=-\mathcal L_{-m,-U}[\Psi]$ for both statistics and fails at fixed $\lambda\ne0$ (Theorem 6.7), and it is equivalent to reversing all eight frame vectors; reflections of a space-like direction give $\mathcal L_{-m,\lambda}$ (Theorem 6.8); complex conjugation is an exact, charge-reversing symmetry of the commuting field but not of the Grassmann field, for which $C_8$ combined with a space-like reflection is (Theorem 6.10).

**What we assumed or took from elsewhere.** The algebraic properties of the gamma matrices, $C$, $\gamma^8$ and the spin generators, including Theorems 2.8, 2.11 and 2.12 and the facts of linear algebra quoted in Section 2.2 (Chapter 2), and the geometry of the vielbein, the canonical spin connection, the covariant derivatives and the divergence identity (Chapter 4). The form of the Lagrangian is a choice of the project: the symmetrized kinetic term, the Dirac adjoint with $C$, the default potential $\tfrac\lambda2S^2$ and the conditions $U(0)=U'(0)=0$ are conventions, not derivations (Stage-1 document, §1.2). That fermion components must be anticommuting is the physical premise of dirac16complex; that dirac16complex00 is only a classical field is a decision of the project, and no spin–statistics theorem is proved for signature (4,4). The reflections were derived here in flat space only; their curved-space form, with the frame reflected together with the field, is taken from the Stage-5 and matter–antimatter reports and proved in Chapter 15; the completeness of the classification of the constant discrete maps (Theorem M2, which examines all 1024 maps of the kind of Section 6.12 for each statistics) is quoted from the matter–antimatter reports and treated in Chapter 17. Numbers measured at test points, such as the 544 monomials of $\mathrm{Lg}$ at G1 p1 or the 128 nonzero entries of $\gamma^\mu\Omega_\mu$ at the G1 points, are quoted from the reports, not derived. The machine checks at test points confirm the general derivations; they do not replace them.

### 6.15 Exercises

**Exercise 6.1.** Using the table of $C$ in Section 2.9, compute $S=\bar\Psi\Psi$ for the commuting columns $\Psi=e_0+2e_4+e_8$, $\Psi=e_0+(1+i)e_4$ and $\Psi=e_0+(1-i)e_4$.

**Exercise 6.2.** Show that $\Psi^\dagger B\Psi$ is real for every commuting $\Psi$, where $B=-iC\gamma^4$, using Lemma 6.1.

**Exercise 6.3.** For the boost $R=\cosh\tfrac\theta2+\sinh\tfrac\theta2\,\gamma^0\gamma^4$ verify $R^TCR=C$ directly from $\gamma^0C=-C\gamma^0$ and $\gamma^4C=C\gamma^4$.

**Exercise 6.4.** In flat space with $m=2$, find the frequency $\omega$ of the plane waves with (a) $k_1=1$, $k_5=1$; (b) $k_0=3$, $k_6=5$; (c) $k_1=4$, $k_7=5$. In which case does no real frequency exist?

**Exercise 6.5.** For the field $\Psi=f(x_1)e_0+g(x_1)e_{11}$ of Section 6.5 take $f=\cos(kx_1)$ and $g=i\sin(kx_1)$ with real $k$. Compute $X=\bar\Psi\gamma^1\partial_1\Psi$, the kinetic term $K$ and $\bar\Psi\gamma^1\Psi$.

**Exercise 6.6.** For Grassmann components show that $U(S)=e^{\mu S}-1-\mu S$ is a polynomial, and write it out for the two-component example of Section 6.7.

**Exercise 6.7.** Show from Lemma 6.3 that $\{\gamma^c,S^{ab}\}$ is totally antisymmetric in $(c,a,b)$ when the three indices are distinct, and compute $\{\gamma^0,S^{12}\}$ and $\{\gamma^1,S^{12}\}$.

**Exercise 6.8.** Take the polar-plane vielbein of Section 4.10 ($e_\mu{}^a=\mathrm{diag}(1,r)$, $\sqrt{|g|}=r$, $\gamma^r=\sigma_1$, $\gamma^\varphi=\sigma_2/r$). Compute $\frac1{2\sqrt{|g|}}\partial_\mu(\sqrt{|g|}\gamma^\mu)$ and compare with the value $\gamma^\mu\Omega_\mu=\frac1{2r}\sigma_1$ found in Section 4.12.

**Exercise 6.9.** Show that the Euler–Lagrange expressions of the flat-space Lagrangian $\mathcal L=\tfrac12\bigl(q^TA\dot q-\dot q^TAq\bigr)$ of two real commuting functions $q(t)$ with $A=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ are those of $q^TA\dot q$, and compute them. (This is the one-dimensional shadow of Theorem 6.5: for real commuting fields the symmetrization is automatic.)

**Exercise 6.10.** Show $\mathcal L_{m,\lambda}[\gamma^8\Psi]+\mathcal L_{-m,\lambda}[\Psi]=-\lambda\sqrt{|g|}\,S^2$ for $U=\tfrac\lambda2S^2$, and find for which potentials $U$ the map sends $\mathcal L_{m,U}$ to $-\mathcal L_{-m,U}$.

**Exercise 6.11.** Check $\exp(\pi S^{45})=\gamma^4\gamma^5$ and conclude that the product of the four rotations by $\pi$ of Section 6.11 is $\gamma^8$.

**Exercise 6.12.** Use Theorem 6.8 to find the image of $\mathcal L_{m,\lambda}$ under the reflection $\Psi'(x)=\gamma^b\Psi(R_bx)$ for $b=1$ and for $b=5$, and then under the composition of the reflections for $b=1$ and $b=2$.

**Exercise 6.13.** For Grassmann components show that $C_8$ followed by the reflection with $b=0$ is an exact symmetry, using Theorems 6.8 and 6.10.

**Exercise 6.14.** Let $\Psi=\rho+i\iota$ with real Grassmann columns $\rho,\iota$, and let $A$ be a constant real antisymmetric matrix (for example $C\gamma^a$). Show that $\Psi^\dagger A\,\partial_a\Psi-(\partial_a\Psi^\dagger)A\Psi=2i\bigl(\rho^TA\,\partial_a\iota-\iota^TA\,\partial_a\rho\bigr)$, and write the right-hand side as a total derivative plus a multiple of $\rho^TA\,\partial_a\iota$.

### 6.16 Answers to the exercises

**Answer 6.1.** With $(Cu)_0=-u_4$, $(Cu)_4=-u_0$, $(Cu)_8=u_{12}$, $(Cu)_{12}=u_8$: for $\Psi=e_0+2e_4+e_8$, $S=1\cdot(-2)+2\cdot(-1)+1\cdot0=-4$ (the component 8 pairs with 12, which is zero). For $\Psi=e_0+(1+i)e_4$, $S=\Psi_0^\ast(-\Psi_4)+\Psi_4^\ast(-\Psi_0)=-(1+i)-(1-i)=-2$. For $\Psi=e_0+(1-i)e_4$, $S=-(1-i)-(1+i)=-2$: the same, as the symmetry $C_0$ of Section 6.12 requires for a commuting field.

**Answer 6.2.** By Section 2.12, $B$ is Hermitian. Lemma 6.1 gives $(\Psi^\dagger B\Psi)^\ast=\Psi^\dagger B^\dagger\Psi=\Psi^\dagger B\Psi$, so the number is real.

**Answer 6.3.** $R^T=R$ (Section 6.3). Write $c=\cosh\tfrac\theta2$, $s=\sinh\tfrac\theta2$ and $J=\gamma^0\gamma^4$. Then $JC=\gamma^0\gamma^4C=\gamma^0C\gamma^4=-C\gamma^0\gamma^4=-CJ$, so $RC=C(c-sJ)$ and $R^TCR=RCR=C(c-sJ)(c+sJ)=C(c^2-s^2J^2)=C(c^2-s^2)=C$, because $J^2=1$ and $\cosh^2-\sinh^2=1$.

**Answer 6.4.** $\omega^2=m^2+k_0^2+\dots+k_3^2-k_5^2-k_6^2-k_7^2$. (a) $4+1-1=4$, $\omega=2$. (b) $4+9-25=-12$: no real frequency; the mode grows like $e^{\sqrt{12}\,x_4}$ (Chapter 8). (c) $4+16-25=-5$: no real frequency either. Only (a) oscillates.

**Answer 6.5.** $X=f^\ast g'-g^\ast f'=\cos(kx_1)\cdot ik\cos(kx_1)-(-i\sin(kx_1))\cdot(-k\sin(kx_1))=ik\cos^2(kx_1)-ik\sin^2(kx_1)=ik\cos(2kx_1)$. It is purely imaginary, so $K=\tfrac12(X+X^\ast)=0$. And $\bar\Psi\gamma^1\Psi=f^\ast g-g^\ast f=i\cos\sin-(-i)\sin\cos=2i\sin(kx_1)\cos(kx_1)=i\sin(2kx_1)$, whose derivative $2ik\cos(2kx_1)$ equals $X-X^\ast$, as the identity of Section 6.5 requires.

**Answer 6.6.** $e^{\mu S}-1-\mu S=\sum_{k\ge2}\mu^kS^k/k!$, and $S^k=0$ for $k\ge17$, so the sum stops at $k=16$: a polynomial with real coefficients and $U(0)=U'(0)=0$. For two components $S^3=0$, so $U=\tfrac{\mu^2}2S^2=-\mu^2\,\theta_0^\ast\theta_0\theta_1^\ast\theta_1$.

**Answer 6.7.** For distinct $c,a,b$, $\{\gamma^c,S^{ab}\}=\gamma^c\gamma^a\gamma^b$, and exchanging two of the three anticommuting factors changes the sign, so the expression is totally antisymmetric. $\{\gamma^0,S^{12}\}=\gamma^0\gamma^1\gamma^2$. $\{\gamma^1,S^{12}\}=0$ because $1\in\{1,2\}$.

**Answer 6.8.** $\sqrt{|g|}\gamma^r=r\sigma_1$ and $\sqrt{|g|}\gamma^\varphi=\sigma_2$. Only $\partial_r(r\sigma_1)=\sigma_1$ is nonzero ($\sigma_2$ does not depend on $\varphi$). So $\frac1{2r}\sigma_1$, the value of Section 4.12.

**Answer 6.9.** For commuting numbers $\dot q^TAq=q^TA^T\dot q=-q^TA\dot q$, so $\mathcal L=q^TA\dot q=q_0\dot q_1-q_1\dot q_0$. Then $\partial\mathcal L/\partial q_0=\dot q_1$, $\partial\mathcal L/\partial\dot q_0=-q_1$, so $E_0=\dot q_1+\dot q_1=2\dot q_1$; and $E_1=-\dot q_0-\dot q_0=-2\dot q_0$. These are twice the expressions of Example A of Section 5.6 (whose Lagrangian is half of this one).

**Answer 6.10.** By Theorem 6.7, $\mathcal L_{m,\lambda}[\gamma^8\Psi]=\sqrt{|g|}(-K-mS-\tfrac\lambda2S^2)$ and $\mathcal L_{-m,\lambda}[\Psi]=\sqrt{|g|}(K+mS-\tfrac\lambda2S^2)$; the sum is $-\lambda\sqrt{|g|}S^2$. In general $\mathcal L_{m,U}[\gamma^8\Psi]=-\mathcal L_{-m,-U}[\Psi]$, which equals $-\mathcal L_{-m,U}[\Psi]$ for every field exactly when $-U=U$, that is $U=0$.

**Answer 6.11.** $S^{45}=\tfrac12\gamma^4\gamma^5$ and $(\gamma^4\gamma^5)^2=-(\gamma^4)^2(\gamma^5)^2=-(-1)(-1)=-1$, so Section 2.11 gives $\exp(\pi S^{45})=\cos\tfrac\pi2+\gamma^4\gamma^5\sin\tfrac\pi2=\gamma^4\gamma^5$. In the same way $\exp(\pi S^{01})=\gamma^0\gamma^1$, $\exp(\pi S^{23})=\gamma^2\gamma^3$ and $\exp(\pi S^{67})=\gamma^6\gamma^7$ (each square is $-1$). The product in the order $(0,1),(2,3),(4,5),(6,7)$ is $\gamma^0\gamma^1\gamma^2\gamma^3\gamma^4\gamma^5\gamma^6\gamma^7=\gamma^8$.

**Answer 6.12.** $b=1$ is space-like: $\mathcal L_{-m,\lambda}$. $b=5$ is time-like: $-\mathcal L_{-m,-\lambda}$. Two space-like reflections: the first gives $K\to K$, $S\to-S$, and the second again $K\to K$, $S\to-S$, so altogether $K\to K$, $S\to S$: the composition is an exact symmetry, $\mathcal L_{m,\lambda}$ (it is the rotation by $\pi$ in the plane $(1,2)$, up to a sign of the spinor).

**Answer 6.13.** For $s=-1$, $C_8$ gives $K\to K$, $S\to-S$ (Theorem 6.10). The reflection with $b=0$ ($n_0=+1$) gives $K\to K$, $S\to-S$ (Theorem 6.8). Together $K\to K$, $S\to S$, and $U(S)$ is unchanged: $\mathcal L_{m,\lambda}\to\mathcal L_{m,\lambda}$, an exact symmetry for every $m$ and $\lambda$.

**Answer 6.14.** The conjugate of $\rho+i\iota$ is $\rho-i\iota$ (real generators are unchanged, and $i\to-i$), so $\Psi^\dagger=\rho^T-i\iota^T$. Expand both products:

$$
\begin{aligned}
\Psi^\dagger A\,\partial_a\Psi&=\rho^TA\,\partial_a\rho+\iota^TA\,\partial_a\iota+i\bigl(\rho^TA\,\partial_a\iota-\iota^TA\,\partial_a\rho\bigr),\\
(\partial_a\Psi^\dagger)A\Psi&=(\partial_a\rho)^TA\rho+(\partial_a\iota)^TA\iota+i\bigl((\partial_a\rho)^TA\iota-(\partial_a\iota)^TA\rho\bigr).
\end{aligned}
$$

For odd columns $\phi,\chi$ and antisymmetric $A$, exchanging the two odd factors gives $\phi^TA\chi=\sum_{i,j}\phi_iA_{ij}\chi_j=-\sum_{i,j}\chi_jA_{ij}\phi_i=-\chi^TA^T\phi=\chi^TA\phi$. With it, $(\partial_a\rho)^TA\rho=\rho^TA\,\partial_a\rho$, $(\partial_a\iota)^TA\iota=\iota^TA\,\partial_a\iota$, $(\partial_a\rho)^TA\iota=\iota^TA\,\partial_a\rho$ and $(\partial_a\iota)^TA\rho=\rho^TA\,\partial_a\iota$. So in the difference the terms without $i$ cancel exactly, and the difference is $i(\rho^TA\,\partial_a\iota-\iota^TA\,\partial_a\rho)-i(\iota^TA\,\partial_a\rho-\rho^TA\,\partial_a\iota)=2i\bigl(\rho^TA\,\partial_a\iota-\iota^TA\,\partial_a\rho\bigr)$. The product rule and the same exchange give $\iota^TA\,\partial_a\rho=\partial_a(\iota^TA\rho)-(\partial_a\iota)^TA\rho=\partial_a(\iota^TA\rho)-\rho^TA\,\partial_a\iota$, so the difference is $4i\,\rho^TA\,\partial_a\iota-2i\,\partial_a(\iota^TA\rho)$: a total derivative plus a genuine cross term. As for the mass term, the dynamics of the complex Grassmann field lives entirely in the cross terms between its real and imaginary parts.
