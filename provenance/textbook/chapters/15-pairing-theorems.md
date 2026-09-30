## 15. The pairing theorems

### 15.1 What this chapter proves, and what it does not

**The question.** The author's notebook opens with a hypothesis. Its cell 6 says that at the time $x_4=0$ "a pair of universes with MASSES ± M is created" (quoted from the survey `handoff/surveys/survey_notebook-physics.md`; Chapter 0 quotes the cells 6, 7 and 17 in full, and Chapter 16 discusses them). Before one can ask whether such a pair is created, one must know whether the equations of this book allow it at all. If a universe of mass $+M$ is a solution, is there a partner of mass $-M$? And what energy, momentum and charge do the two carry together? This chapter answers these two questions exactly, with three theorems called T1, T2 and T3 as in the Stage-5 specification `handoff/specs/STAGE5_SPEC.md` (its §5), and it reports the numerical test of the third one.

In this chapter a **universe of mass $+M$** means a configuration or solution of the field equations (from Section 15.7 on, a Kohn–Sham state of Chapter 13) whose mass parameter is $m=+M$, and its **partner of mass $-M$** is one with $m=-M$. The notebook writes its mass term with a number $M$, and the Lagrangian of this book has $m=-HM$ (Section 5.12). Every statement below relates $m$ to $-m$, so it does not matter which member of a pair is called the universe of mass $+M$.

**The three theorems in words.**

- **T1, the chirality map** (Sections 15.3 and 15.4). Multiply the field by the chirality $\gamma^8$ of Chapter 2. A configuration of the theory with mass $m$ and coupling $\lambda$ becomes a configuration of the theory with $-m$ and $-\lambda$, in every gravitational field. Its energy density, momentum, stresses and charge all change sign; its scalar density $S=\bar\Psi\Psi$ does not. The pair made of a field and its image therefore carries **zero** total energy–momentum and zero total charge, at every point and at every time.
- **T2, the mirror map** (Sections 15.5 and 15.6). Combine the field with the reflection of one space-like direction. A configuration with $(m,\lambda)$ becomes one with $(-m,\lambda)$, the **same** coupling. Energy, momentum and charge are unchanged (they are only reflected); the scalar density changes sign. In the mirror-extended primordial field of Chapter 9, the reflection of the hidden direction across the brane turns a universe of mass $+M$ on one side into a universe of mass $-M$ on the other side.
- **T3, the Kohn–Sham level** (Section 15.7). In the Kohn–Sham approximation of Chapter 13 (and of Chapter 14 for dirac16complex00) the chirality map becomes a swap of the two components of every $2\times2$ block. With suitably transformed boundary conditions, the Kohn–Sham ground state and first excited state of the universe of mass $-M$ with the **same** $\lambda$ are the exact images of those of the universe of mass $+M$: the same energies, the same energy–momentum tensor, the opposite scalar density.

T1 and T3 both come from $\gamma^8$, yet T1 reverses the energy and needs $-\lambda$, while T3 keeps the energy and the same $\lambda$. Section 15.8 explains why: T1 is a statement about the classical bilinears of the field, T3 about the expectation values of the positive-norm quantum theory of Chapter 8, and the two differ by the matrix $B$, which $\gamma^8$ reverses. Section 15.9 shows what goes wrong when the boundary conditions are not transformed, and Section 15.10 reports the numerical tests.

**What is not proved.** This is the honesty rule of Chapter 0. The theorems show which partners exist and what they carry, and they show that a pair of the T1 type is consistent with every conservation law and with the gravitational field equations. They do **not** compute any process that creates a pair: no rate, no probability, no amplitude, and no dynamical big bang is derived. The Stage-1 document says it in one sentence that this book repeats: the pairing of the masses $\pm m$ is "a structural property of the equations, not a claim that universes of masses $\pm M$ are created in pairs" (`provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md`, §1.3, item 6). Section 15.11 lists precisely what is and what is not established. Chapter 16 takes up the question of pair creation, and Chapter 17 the question of matter and antimatter.

**Sources and their status.** The exact theory of the pairing theorems is the Wolfram package `wolfram/Dirac16ComplexPairing.wl` with its verifier, and an independent sympy checker re-derives everything with its own code and compares the results. The programs and their reports:

```
wolfram/Dirac16ComplexPairing.wl, scripts/verify_dirac16complex_pairing.wls
scripts/check_dirac16complex_pairing.py          (independent, sympy)
artifacts/dirac16complex/pair-creation/
  wolfram-pairing-report.json           141 of 141 checks true
  python-pairing-report.json            172 of 172 checks true
  pairing-theory.json                   every map and formula, exact
  wolfram-dirac16complex00-report.json   46 of 46 checks true
  python-dirac16complex00-report.json    49 of 49 checks true
```

The Python pairing report includes the comparison with the Wolfram results (check `S5_pairingAgreesWithWolfram`). The last two reports belong to the Stage-5 field theory of dirac16complex00. Check names beginning with `PAIR_` or `C00_` are checks of the two Wolfram reports; the Python reports contain the same families under names beginning with `S5_`. The matter–antimatter document `provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md` (its Section 7) uses the same results. Three things were **not finished** when this chapter was written: the numerical demonstration had been stopped part of the way through (Section 15.10 says exactly which runs exist), the Stage-5 cross-checker and the Stage-5 gate had not been run, and the Stage-5 documents `provenance/DIRAC16COMPLEX_PAIR_CREATION.md` and `provenance/DIRAC16COMPLEX00_FIELD_THEORY.md` were not yet written. The exact results are therefore quoted as committed, and the chapter is built directly on the specification, the exact reports and the committed outputs.

**Conventions.** As everywhere in the book: counting from 0, coordinates $x_0,\dots,x_7$ with $x_4$ the time, $\eta=\mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1)$, the notebook's gamma matrices $\gamma^0,\dots,\gamma^7$ (Section 2.8), $C=\gamma^0\gamma^1\gamma^2\gamma^3$, $\gamma^8=\gamma^0\gamma^1\cdots\gamma^7$, $B=-iC\gamma^4$, $\bar\Psi=\Psi^\dagger C$ and $D_\mu\Psi=\partial_\mu\Psi+\Omega_\mu\Psi$ with the canonical spin connection of Chapter 4. The two fields of Chapter 6, dirac16complex (anticommuting Grassmann components, quantized in Chapter 8) and dirac16complex00 (commuting components, a classical field), have the same Lagrangian,

$$
\mathcal L_{m,\lambda}=\sqrt{|g|}\,\Bigl[K-mS-\tfrac\lambda2S^2\Bigr],\qquad K=\tfrac12\bigl(\bar\Psi\gamma^\mu D_\mu\Psi-(D_\mu\bar\Psi)\gamma^\mu\Psi\bigr),\qquad S=\bar\Psi\Psi ,
$$

and the same field equations $E_{m,\lambda}[\Psi]=0$ and $\bar E_{m,\lambda}[\Psi]=0$ (Chapter 7), with

$$
E_{m,\lambda}[\Psi]:=\gamma^\mu D_\mu\Psi-(m+\lambda S)\Psi,\qquad \bar E_{m,\lambda}[\Psi]:=(D_\mu\bar\Psi)\gamma^\mu+(m+\lambda S)\bar\Psi .
$$

The energy–momentum tensor of Chapter 7 is

$$
T_{\mu\nu}=-\tfrac14\Bigl[\bar\Psi\gamma_\mu D_\nu\Psi+\bar\Psi\gamma_\nu D_\mu\Psi-(D_\mu\bar\Psi)\gamma_\nu\Psi-(D_\nu\bar\Psi)\gamma_\mu\Psi\Bigr]+g_{\mu\nu}\,\mathcal L_s,\qquad \mathcal L_s=\mathcal L/\sqrt{|g|},
$$

and we use it as an expression that can be evaluated on any configuration, a solution or not. The conserved current is $J^\mu=-i\bar\Psi\gamma^\mu\Psi$ (Section 8.12); in Gaussian normal gauge its time component is $J^4=\Psi^\dagger B\Psi$, and the charge of a slice is $Q=\int\sqrt{|g|}\,J^{x_4}\,d^7x$. We write $\mathcal L_{m,\lambda}[e,\Psi]$ or $T_{\mu\nu}[e,\Psi;m,\lambda]$ when the vielbein $e$ must be named.

### 15.2 Tools: constant matrices, bilinears and parity

Every proof of this chapter manipulates expressions $\Psi^\dagger X\Phi=\sum_{a,b}\Psi_a^\ast X_{ab}\Phi_b$, where $X$ is a $16\times16$ matrix of ordinary numbers (or ordinary functions of $x$) and $\Psi$, $\Phi$ are columns of field components or their derivatives. Chapter 6 calls them bilinears. This section collects the facts that we need about them.

**Six facts about $\gamma^8$, $C$ and $B$** (proved in Sections 2.9, 2.10, 2.12 and 8.6; checks `PAIR_algebra_gamma8Properties`, `PAIR_algebra_CProperties`, `PAIR_algebra_BProperties`):

- (F1) $\gamma^8=\mathrm{diag}(-I_8,I_8)$ is real and diagonal, hence Hermitian, and $(\gamma^8)^2=1$.
- (F2) $\gamma^8\gamma^a=-\gamma^a\gamma^8$ for every $a$. The curved gammas $\gamma^\mu=e_a{}^\mu\gamma^a$ and $\gamma_\mu=g_{\mu\nu}\gamma^\nu$ of any vielbein are combinations of the $\gamma^a$ with ordinary functions as coefficients, so $\gamma^8$ anticommutes with them too.
- (F3) $\gamma^8$ commutes with $C$ (a product of four gammas) and with every $S^{ab}=\tfrac14[\gamma^a,\gamma^b]$ (two gammas), hence with every spinor connection $\Omega_\mu=\tfrac12\omega_{\mu ab}S^{ab}$, in every gravitational field.
- (F4) $C$ is real and symmetric with $C^2=1$, and every $C\gamma^a$ is real and antisymmetric.
- (F5) $B=-iC\gamma^4$ is Hermitian, $B^2=1$, and $BC=-i\gamma^4$.
- (F6) $\gamma^8B\gamma^8=-B$.

*Proof of (F6).* $\gamma^8B\gamma^8=-i\,\gamma^8C\gamma^4\gamma^8=-i\,C\gamma^8\gamma^4\gamma^8=-i\,C(-\gamma^4)(\gamma^8)^2=+iC\gamma^4=-B$, by (F3), (F2) and (F1). $\square$

In words: $\gamma^8$ reverses the matrix $B$. Chapter 8 showed that $B$ is the matrix of the canonical anticommutator, the Krein metric of the quantum theory (Section 8.7). Fact (F6) will decide the difference between T1 and T3.

**Lemma 15.1 (constant matrices inside bilinears).** Let $R$ and $X$ be constant $16\times16$ matrices of ordinary numbers, and let $\Psi$, $\Phi$ be columns of commuting components or of Grassmann components. Then

$$
(R\Psi)^\dagger X(R\Phi)=\Psi^\dagger\bigl(R^\dagger XR\bigr)\Phi ,
$$

and the same holds when $\Phi$ is replaced by a derivative $\partial_\mu\Phi$ or $D_\mu\Phi$.

*Proof.* The components of $R\Phi$ are $(R\Phi)_b=\sum_cR_{bc}\Phi_c$, and those of $(R\Psi)^\ast$ are $(R\Psi)_a^\ast=\sum_dR_{ad}^\ast\Psi_d^\ast$. For Grassmann components this uses the rule $(c\theta)^\ast=c^\ast\theta^\ast$ for a number $c$ and one generator $\theta$ (Section 5.9). Hence

$$
\sum_{a,b}(R\Psi)_a^\ast X_{ab}(R\Phi)_b=\sum_{d,c}\Psi_d^\ast\Bigl(\sum_{a,b}R_{ad}^\ast X_{ab}R_{bc}\Bigr)\Phi_c=\sum_{d,c}\Psi_d^\ast\bigl(R^\dagger XR\bigr)_{dc}\Phi_c .
$$

Only ordinary numbers were moved; every $\Psi^\ast$ still stands to the left of every $\Phi$, and no two field components were exchanged. So the computation is the same for both statistics. A constant $R$ commutes with $\partial_\mu$. $\square$

**Lemma 15.2 (parity under $\gamma^8$).** If $P$ is a product of $k$ frame gamma matrices (repetitions allowed), then $\gamma^8P\gamma^8=(-1)^kP$. We call $P$ **even** if $k$ is even and **odd** if $k$ is odd. The parity of a product of matrices is the product of their parities.

*Proof.* Move $\gamma^8$ from the left of $P$ to its right, one factor at a time. Each passage gives a factor $-1$ by (F2), so $\gamma^8P=(-1)^kP\gamma^8$; multiply on the right by $\gamma^8$ and use $(\gamma^8)^2=1$. If $\gamma^8X\gamma^8=\epsilon_XX$ and $\gamma^8Y\gamma^8=\epsilon_YY$, then $\gamma^8XY\gamma^8=\gamma^8X\gamma^8\gamma^8Y\gamma^8=\epsilon_X\epsilon_YXY$. $\square$

The matrices that occur in this book fall into the following classes (check `PAIR_algebra_bilinearParities` tests all 456 matrices $C\gamma^a$, $C\gamma^aS^{bc}$, $CS^{bc}\gamma^a$ and the matrix $C$):

| matrix $X$ | number of gamma factors | $\gamma^8X\gamma^8$ | where it occurs |
| --- | --- | --- | --- |
| $C$ | 4 | $+C$ | $S=\bar\Psi\Psi$, the mass term, $U(S)$ |
| $C\gamma^a$, $C\gamma^aS^{bc}$, $CS^{bc}\gamma^a$ | 5, 7, 7 | $-X$ | kinetic term, $T_{\mu\nu}$, current $J^\mu$ |
| $B=-iC\gamma^4$ | 5 | $-B$ | charge density $J^4=\Psi^\dagger B\Psi$ |
| $BC=-i\gamma^4$ | 9 | $-BC$ | scalar density in the expectation-value rule |
| $BC\gamma^a$ | 10 | $+BC\gamma^a$ | energy and current in the expectation-value rule |

The last two rows show the rule that will matter in Section 15.8: **multiplying by $B$ reverses the parity**, because $B$ is odd.

### 15.3 Theorem T1: the chirality map

**Theorem 15.3 (T1, the chirality map).** Let $e$ be any vielbein (so any metric and its canonical spin connection), $m$ and $\lambda$ any real numbers, and $\Psi$ any configuration of commuting or of Grassmann components, not necessarily a solution. Put $\Psi_-:=\gamma^8\Psi$. Then:

1. $\bar\Psi_-=\bar\Psi\gamma^8$, $D_\mu\Psi_-=\gamma^8D_\mu\Psi$ and $D_\mu\bar\Psi_-=(D_\mu\bar\Psi)\gamma^8$;
2. $S[\Psi_-]=S[\Psi]$ and $K[\Psi_-]=-K[\Psi]$;
3. $\mathcal L_{m,\lambda}[\Psi_-]=-\mathcal L_{-m,-\lambda}[\Psi]$;
4. $E_{-m,-\lambda}[\Psi_-]=-\gamma^8E_{m,\lambda}[\Psi]$ and $\bar E_{-m,-\lambda}[\Psi_-]=-\bar E_{m,\lambda}[\Psi]\gamma^8$; hence $\Psi$ solves the field equations with $(m,\lambda)$ if and only if $\gamma^8\Psi$ solves them with $(-m,-\lambda)$;
5. $T_{\mu\nu}[\Psi_-;-m,-\lambda]=-T_{\mu\nu}[\Psi;m,\lambda]$ for all $\mu,\nu$;
6. $J^\mu[\Psi_-]=-J^\mu[\Psi]$, and the charge of every slice changes sign, $Q[\Psi_-]=-Q[\Psi]$.

*Proof.* Step 1 (adjoint and derivatives). By Lemma 15.1 with $R=\gamma^8$, which is Hermitian (F1), $\bar\Psi_-=(\gamma^8\Psi)^\dagger C=\Psi^\dagger\gamma^8C=\Psi^\dagger C\gamma^8=\bar\Psi\gamma^8$ by (F3). Since $\gamma^8$ is constant and commutes with $\Omega_\mu$ (F3), $D_\mu(\gamma^8\Psi)=\gamma^8\partial_\mu\Psi+\Omega_\mu\gamma^8\Psi=\gamma^8(\partial_\mu\Psi+\Omega_\mu\Psi)=\gamma^8D_\mu\Psi$, and in the same way $D_\mu\bar\Psi_-=\partial_\mu(\bar\Psi\gamma^8)-\bar\Psi\gamma^8\Omega_\mu=(D_\mu\bar\Psi)\gamma^8$.

Step 2 (scalar and kinetic term). $S[\Psi_-]=\bar\Psi\gamma^8\gamma^8\Psi=S[\Psi]$ by (F1). For the first half of $K$, $\bar\Psi_-\gamma^\mu D_\mu\Psi_-=\bar\Psi\gamma^8\gamma^\mu\gamma^8D_\mu\Psi=-\bar\Psi\gamma^\mu D_\mu\Psi$ by (F2) and (F1), and the second half changes sign in the same way. So $K[\Psi_-]=-K[\Psi]$. In the language of Lemma 15.2: the scalar has an even matrix, the kinetic term odd ones.

Step 3 (Lagrangian). With $U=\tfrac\lambda2S^2$, which is even in $S$,

$$
\mathcal L_{m,\lambda}[\Psi_-]=\sqrt{|g|}\Bigl[-K-mS-\tfrac\lambda2S^2\Bigr]=-\sqrt{|g|}\Bigl[K-(-m)S-\tfrac{(-\lambda)}2S^2\Bigr]=-\mathcal L_{-m,-\lambda}[\Psi].
$$

Step 4 (field equations). Using Step 1, (F2) and $S[\Psi_-]=S$,

$$
E_{-m,-\lambda}[\Psi_-]=\gamma^\mu\gamma^8D_\mu\Psi-(-m-\lambda S)\gamma^8\Psi=-\gamma^8\gamma^\mu D_\mu\Psi+\gamma^8(m+\lambda S)\Psi=-\gamma^8E_{m,\lambda}[\Psi],
$$

and $\bar E_{-m,-\lambda}[\Psi_-]=(D_\mu\bar\Psi)\gamma^8\gamma^\mu-(m+\lambda S)\bar\Psi\gamma^8=-\bigl[(D_\mu\bar\Psi)\gamma^\mu+(m+\lambda S)\bar\Psi\bigr]\gamma^8$. Since $\gamma^8$ is invertible, one side vanishes exactly when the other does.

Step 5 (energy–momentum tensor). Each of the four bilinears in the bracket of $T_{\mu\nu}$ contains exactly one curved gamma between an adjoint and a field, so each changes sign as in Step 2. The last term is $g_{\mu\nu}\mathcal L_s$, and by Step 3 (divided by $\sqrt{|g|}$) $\mathcal L_s[\Psi_-;-m,-\lambda]=-\mathcal L_s[\Psi;m,\lambda]$. So every term of $T_{\mu\nu}[\Psi_-;-m,-\lambda]$ is minus the corresponding term of $T_{\mu\nu}[\Psi;m,\lambda]$.

Step 6 (current and charge). $J^\mu[\Psi_-]=-i\bar\Psi\gamma^8\gamma^\mu\gamma^8\Psi=-J^\mu[\Psi]$. The charge is the integral of $\sqrt{|g|}\,J^{x_4}$ over the same slice with the same $\sqrt{|g|}$, so it changes sign.

Step 7 (both statistics). Every step multiplied matrices of ordinary numbers or used Lemma 15.1; nowhere were two field components exchanged. The proof therefore holds word for word for Grassmann components. (In the notebook's basis the map sends $\Psi_a\to-\Psi_a$ for $a\le7$ and $\Psi_a\to\Psi_a$ for $a\ge8$; for Grassmann generators this is a map of the algebra onto itself that respects all products, check `PAIR_algebra_chiralBlockStructure`.) $\square$

**Why $\lambda$ must change sign.** The potential $\tfrac\lambda2S^2$ is even, so it does not change sign when $K$ does. At a fixed coupling the map fails: $\mathcal L_{m,\lambda}[\gamma^8\Psi]+\mathcal L_{-m,\lambda}[\Psi]=\sqrt{|g|}\,[-K-mS-\tfrac\lambda2S^2+K+mS-\tfrac\lambda2S^2]=-\lambda\sqrt{|g|}\,S^2$, which is not zero when $\lambda\ne0$ and $S\ne0$. This is erratum E2 of `handoff/specs/CONTRACT.md` (§11); the verifiers confirm the failure (checks `PAIR_T1generic_naiveFixedLambdaFails`, `PAIR_T1grassmann_naiveFixedLambdaFails`, `PAIR_T1jets_naiveFixedLambdaFails`). For $\lambda=0$ the two members of the pair are the same free field with the masses $+m$ and $-m$.

**T1 relates two theories; it is not a symmetry of one.** Since $E_{m,\lambda}$ and $E_{-m,-\lambda}$ differ only in the sign of the mass term, $E_{m,\lambda}[\gamma^8\Psi]=E_{-m,-\lambda}[\gamma^8\Psi]-2(m+\lambda S)\gamma^8\Psi$. If $\Psi$ is a solution with $(m,\lambda)$, the first term vanishes by item 4, and $\gamma^8\Psi$ solves the original equations only where $(m+\lambda S)\Psi=0$. The image of a solution is a solution of the *partner* theory (check `PAIR_T1jets_onShellImage`, which also confirms that the image is not a solution with $(m,\lambda)$ or $(-m,\lambda)$ at the test points).

**A second view: reversing the frame.** Replace the vielbein $e_\mu{}^a$ by $-e_\mu{}^a$ and keep $\Psi$. The metric $g=e\,\eta\,e^T$ and $\sqrt{|g|}$ do not change; the curved gammas $\gamma^\mu=e_a{}^\mu\gamma^a$ change sign; the Christoffel symbols do not change, and neither does the spin connection $\omega_\mu{}^a{}_b=e_b{}^\nu(\Gamma^\rho{}_{\mu\nu}e_\rho{}^a-\partial_\mu e_\nu{}^a)$ of Section 4.11, because each of its terms contains two factors of the vielbein. Hence $K\to-K$, $S\to S$ and $\mathcal L_{m,\lambda}[-e,\Psi]=-\mathcal L_{-m,-\lambda}[e,\Psi]$: the same statement as item 3. Combining the two changes, $\mathcal L_{m,\lambda}[-e,\gamma^8\Psi]=\mathcal L_{m,\lambda}[e,\Psi]$. This is no accident: $\gamma^8=(\gamma^0\gamma^1)(\gamma^2\gamma^3)(\gamma^4\gamma^5)(\gamma^6\gamma^7)$ is the product of four rotations by $\pi$, $\exp(\pi S^{ab})=\gamma^a\gamma^b$ in the planes $(0,1)$, $(2,3)$, $(4,5)$ and $(6,7)$ (Exercise 2.14; the planes $(4,5)$ and $(6,7)$ are rotation planes because $\eta^{44}\eta^{55}=\eta^{66}\eta^{77}=+1$), and it turns every frame vector into its negative. So $(e,\Psi)\to(-e,\gamma^8\Psi)$ is a local frame rotation of spinor norm $+1$, under which the Lagrangian is invariant (Chapter 6; the checks are listed at the end of this section). The content of T1 can therefore be put in one sentence: **the theory with $(-m,-\lambda)$ is the theory with $(m,\lambda)$ whose action is multiplied by $-1$**, written in the relabelled field $\gamma^8\Psi$. Multiplying an action by $-1$ does not change its field equations, but it reverses everything that is computed from the action by a variation with respect to the metric (the energy–momentum tensor, Section 5.8) and the canonical structure of the quantum theory (Section 15.4).

**Worked example: a quantum at rest and its image.** Take flat space, $\lambda=0$ and the rest state of Section 8.8,

$$
u_+=\tfrac12\bigl(e_0-e_4-i\,e_9-i\,e_{13}\bigr),\qquad -i\gamma^4u_+=u_+,\qquad Cu_+=u_+,\qquad Bu_+=u_+ ,
$$

where $e_n$ is the column with 1 in place $n$. The field $\Psi_+=e^{-imx_4}u_+$ depends on $x_4$ only, so $\gamma^\mu D_\mu\Psi_+=\gamma^4\partial_4\Psi_+=-im\gamma^4\Psi_+=m\Psi_+$: it solves the free equation with mass $m$. Its image is $\Psi_-=\gamma^8\Psi_+=e^{-imx_4}\tilde u$ with $\tilde u:=\gamma^8u_+=\tfrac12(-e_0+e_4-i\,e_9-i\,e_{13})$, because $\gamma^8$ multiplies the components 0 to 7 by $-1$. With the rows of $\gamma^4$ and $B$ quoted in Section 11.4 and the rows of $C$ used in Section 8.8 ($(\gamma^4v)_0=-v_{13}$, $(\gamma^4v)_4=v_9$, $(\gamma^4v)_9=-v_4$, $(\gamma^4v)_{13}=v_0$; $(Cv)_0=-v_4$, $(Cv)_4=-v_0$, $(Cv)_9=v_{13}$, $(Cv)_{13}=v_9$; $(Bv)_0=iv_9$, $(Bv)_4=-iv_{13}$, $(Bv)_9=-iv_0$, $(Bv)_{13}=iv_4$) one finds $-i\gamma^4\tilde u=-\tilde u$, $C\tilde u=\tilde u$ and $B\tilde u=-\tilde u$ (Exercise 15.4). Hence $\gamma^4\partial_4\Psi_-=m(-i\gamma^4)\Psi_-=-m\Psi_-$: the image solves the free equation with mass $-m$, as item 4 says. The classical densities are:

| quantity | $\Psi_+$ (mass $m$) | $\Psi_-=\gamma^8\Psi_+$ (mass $-m$) | sum |
| --- | --- | --- | --- |
| charge density $J^4=\Psi^\dagger B\Psi$ | $+1$ | $-1$ | 0 |
| scalar density $S=\Psi^\dagger C\Psi$ | $+1$ | $+1$ | 2 |
| energy density $\rho=m\,\Psi^\dagger B\Psi$ | $+m$ | $-m$ | 0 |

The energy density is the component $T_{44}$; for a field that oscillates like $e^{-i\varepsilon x_4}$ in flat space with $\lambda=0$ it equals $\varepsilon\,\Psi^\dagger B\Psi$ (the derivation of Section 13.14, with $\mathcal L_s=0$ on shell when $\lambda=0$), and here $\varepsilon=m$ for both members.

**How T1 was verified.** The identities of items 1 to 6 were checked in four independent ways, each in both pairing reports: as polynomial identities in completely generic independent symbols for the vielbein, the connection and the field, which is a check for every gravitational field (the Python checker also derives the Euler–Lagrange expressions from the Lagrangian); in a Grassmann algebra with 288 odd generators; with exact jets of the general non-diagonal test vielbein G1 of Stage 1 at three points, including the on-shell images, the conservation of both energy–momentum tensors and the reversal of the frame (13 checks); and for generic fields of all eight coordinates in the primordial field of Chapter 9 with an arbitrary function $a_4$, all 64 components of $T_{\mu\nu}$. The Lagrangian part is also check `ALG_gamma8Map` of Stage 1.

```
PAIR_T1generic_lagrangian            PAIR_T1generic_fieldEquation
PAIR_T1generic_conjugateFieldEquation PAIR_T1generic_emtAll36
PAIR_T1generic_current               S5_T1generic_eulerLagrangeFromLagrangian
PAIR_T1grassmann_lagrangian          PAIR_T1grassmann_diracOperator
PAIR_T1grassmann_emt                 PAIR_T1grassmann_current
PAIR_T1jets_* (13 checks)            PAIR_T1primordial_* (6 checks)
PAIR_algebra_gamma8InIdentityComponent
PAIR_T1jets_vielbeinSignFlipGeometry PAIR_T1jets_vielbeinSignFlipIsT1
PAIR_T1jets_gamma8WithFrameSignIsSymmetry
```

### 15.4 The chiral pair: zero total energy–momentum and charge

**Corollary 15.4 (the chiral pair).** Assume:

- (a) both members live in the same gravitational field, that is, they are two fields on one spacetime with one vielbein $e$ and one metric $g$;
- (b) the first member is a configuration $\Psi_+$ of the theory with $(m,\lambda)$, and the second is $\Psi_-=\gamma^8\Psi_+$, a configuration of the theory with $(-m,-\lambda)$ (for $\lambda=0$ both members belong to the same free field, with masses $+m$ and $-m$);
- (c) the energy–momentum tensor, current and action of the pair are the sums of those of the members, each computed with its own parameters.

Then, at every point and every time $x_4$, in particular at $x_4=0$,

$$
\begin{aligned}
&T^{\mathrm{pair}}_{\mu\nu}=T_{\mu\nu}[\Psi_+;m,\lambda]+T_{\mu\nu}[\Psi_-;-m,-\lambda]=0,\qquad J^\mu_++J^\mu_-=0,\qquad Q_++Q_-=0,\\
&\mathcal L^{\mathrm{pair}}=\mathcal L_{m,\lambda}[\Psi_+]+\mathcal L_{-m,-\lambda}[\Psi_-]=0,\qquad S^{\mathrm{pair}}=2S_+ .
\end{aligned}
$$

If $\Psi_+$ solves its field equations, $\Psi_-$ solves its own. With the pair as the only source, the Einstein equations $G_{\mu\nu}=\kappa T^{\mathrm{pair}}_{\mu\nu}$, and equally the Einstein–Lovelock equations of Section 9.9, are the **source-free** equations.

*Proof.* Items 5, 6, 3 and 2 of Theorem 15.3, applied to $\Psi=\Psi_+$, give the four sums and $S[\Psi_-]=S[\Psi_+]$; item 4 gives the statement on solutions. $\square$

(Checks `PAIR_totals_fieldLevelChiralPair`, in the primordial field with an arbitrary $a_4$, all 64 components; `PAIR_T1jets_pairEMTAndCurrentVanish`, on shell in the general field G1; in the matter–antimatter reports, `MA_M4_pairEMTAndCurrentG1_commuting` and `MA_M4_pairEMTG1_grassmann`.)

**What the corollary means.** Take the "empty" state $\Psi=0$: it has $T_{\mu\nu}=0$, no charge and no action. A T1 pair has the same totals. No conservation law of the theory (energy, momentum, charge) and no constraint of the gravitational field equations therefore forbids the appearance of such a pair in place of the empty state. This is the precise sense in which the pairing is **consistent** with the notebook's hypothesis. Three remarks keep it in proportion.

1. *No mechanism is contained in it.* The field equations of each member contain the field in every term, so $\Psi=0$ is a solution. For the mode equations of Chapters 8 and 11, which are ordinary differential equations in $x_4$ in the good sector, the uniqueness theorem of Picard and Lindelöf (Section 10.2) says that data which vanish at one time stay zero at all times (the zero function is a solution; the set of times at which a solution vanishes is closed, by continuity, and open, by the uniqueness near each of its points, so it is the whole interval of existence): the classical equations do not create a pair out of the empty state. A creation process would need something beyond them, such as a quantum transition amplitude, a boundary condition at a singular moment or an interaction between the members; none is derived in this project.
2. *The corollary holds for every configuration, solution or not.* It is automatic, because the partner theory has the action of the original one multiplied by $-1$ (Section 15.3). It therefore selects no particular universe and says nothing about which universe is realized.
3. *A T1 pair cannot be the source of the primordial field.* Its total energy–momentum is zero, while the primordial field of Chapter 9 needs a nonzero, negative energy density in eight-dimensional Einstein gravity ($\rho_{\mathrm{req}}=-21H^2/\kappa$ for the static member, Section 9.15). If the pair is the only matter, the geometry must solve the source-free equations, which the primordial field does not (Section 9.10). The pairing theorems do not change the sourcing analysis of Chapters 9 and 13.

**The quantum field.** For the Grassmann field dirac16complex the corollary is a statement about operators, and one more hypothesis enters. Chapter 8 found the canonical anticommutator $\{\Psi_a(x),\Psi_b^\dagger(y)\}=B_{ab}\,\delta^7(x-y)/\sqrt{|g|}$ in Gaussian normal gauge. For the image field $\Psi_-=\gamma^8\Psi$, built from the same operators, Lemma 15.1 and (F6) give

$$
\{\Psi_-,\Psi_-^\dagger\}=\gamma^8\{\Psi,\Psi^\dagger\}\gamma^8=\gamma^8B\gamma^8\,\frac{\delta^7}{\sqrt{|g|}}=-B\,\frac{\delta^7}{\sqrt{|g|}} :
$$

the image field carries the **reversed Krein metric** $-B$. This is exactly the canonical structure of the Lagrangian $-\mathcal L_{-m,-\lambda}$: the rule of Section 8.6 gives the anticommutator $iK^{-1}\delta^7$, where $K$ is the matrix in front of $\partial_4\Psi$ in the Lagrangian, and multiplying the Lagrangian by $-1$ multiplies $K$ by $-1$ and the anticommutator by $-1$ (Exercise 15.3). Two different "universes of mass $-M$" can therefore be meant:

- **the image field** $\Psi_-=\gamma^8\Psi_+$ on the same state space, with the metric $-B$. The exact Fock-space model of the Stage-5 verifier (four rest modes, the filled Dirac sea, normal ordering as subtraction of the sea value) confirms the operator identities $:\!H[\Psi_-;-m]\!:\;=-:\!H[\Psi;m]\!:$, $Q[\Psi_-]=-Q[\Psi]$ and $S[\Psi_-]=S[\Psi]$, and $:\!T_{\mu\nu}[\gamma^8\Psi;-m,-\lambda]\!:\;=-:\!T_{\mu\nu}[\Psi;m,\lambda]\!:$. Every quantum of the image carries the energy $-|\varepsilon|$ and the opposite charge. **For this pair the cancellation of Corollary 15.4 holds as an operator statement.**
- **an independently quantized theory** with $(-m,\lambda)$ or $(-m,-\lambda)$, with its own canonical anticommutator $+B$ and the positive Fock space of Section 8.10. Its modes are $\gamma^8u$ for the modes $u$ of the $+m$ theory, with the same frequencies, and each quantum has a positive energy, the charge $+1$ for a particle and the **opposite** scalar density. **For this pair the energy–momentum does not cancel; it doubles.** This is the pairing of T2 and T3 below.

The checks of the two readings, in the Fock model of the Wolfram pairing report:

```
image field:        PAIR_T1krein_imageAnticommutatorMinusB
                    PAIR_T1krein_imageOperatorIdentities
                    PAIR_T1krein_imageExpectationValues
independent theory: PAIR_T1krein_minusMModes  PAIR_T1krein_independentCARPlusB
                    PAIR_T1krein_independentExpectationValues
```

The matter–antimatter document tabulates the energy $E$, charge $Q$ and scalar density $S$ of one quantum in three exact modes (its Section 7.2; check `MA_M4_kreinOneParticle` of `artifacts/dirac16complex/matter-antimatter/wolfram-matter-antimatter-report.json`):

| $m$, momentum $(k_0,k_1,k_2,k_3)$ | $+m$ universe | image field, metric $-B$ | independent $-m$ theory, metric $+B$ |
| --- | --- | --- | --- |
| 1, $(1,1,2,3)$ | $(4,\,1,\,\tfrac14)$ | $(-4,\,-1,\,\tfrac14)$ | $(4,\,1,\,-\tfrac14)$ |
| 3, $(1,1,1,2)$ | $(4,\,1,\,\tfrac34)$ | $(-4,\,-1,\,\tfrac34)$ | $(4,\,1,\,-\tfrac34)$ |
| $\tfrac35$, $(\tfrac45,0,0,0)$ | $(1,\,1,\,\tfrac35)$ | $(-1,\,-1,\,\tfrac35)$ | $(1,\,1,\,-\tfrac35)$ |

The energies are $E=\sqrt{m^2+k_0^2+k_1^2+k_2^2+k_3^2}$ and the scalar densities $m/E$. (Proof: write $h_k=mA+P$ with $A=-i\gamma^4=BC$ and $P$ the momentum part; $A^2=1$ and $\{A,P\}=0$ (Section 8.9), so $Ah_k+h_kA=2m$, and for a normalized eigenvector $h_ku=Eu$ of $h_k$, which is Hermitian for the space-like momenta used here (Section 8.10), this gives $2E\,u^\dagger Au=2m$.) For the first row $\sqrt{1+1+1+4+9}=4$. The Stage-5 exact results at this Fock level are all true in the committed reports; the matter–antimatter analysis labels its own use of them provisional until the Stage-5 gate has been run from a fresh clone (measurement `M4_kreinLevelStatus` of the Wolfram matter–antimatter report).

For the **commuting** field dirac16complex00, which is a classical field, Corollary 15.4 is a statement about ordinary numbers and needs no hypothesis beyond (a) to (c). Its classical charge density is itself indefinite and its classical energy is not bounded below (Chapter 7; checks `C00_charge_indefinite` and `C00_energy_unboundedBelow`), and the image of a configuration simply has the opposite energy and charge.

### 15.5 Theorem T2: reflections of character minus one

T1 reverses the energy. A different map relates $m$ and $-m$ without reversing the energy: a reflection. Chapter 6 derived it in flat space for the reflection of one coordinate; here we prove it in every gravitational field, where the reflection must act on the frame together with the field.

**Tools from Chapter 2.** A real vector $v=(v_0,\dots,v_7)$ with $n(v):=\eta(v,v)=\pm1$ gives the **unit vector** $u=\gamma(v)=\sum_av_a\gamma^a$ of Pin(4,4), with $u^2=n(u)$, $u^{-1}=n(u)\,u$, $\det u=1$ as a $16\times16$ matrix, and $u^\dagger=u^T$ because $u$ is real (Section 2.14). $u$ is **space-like** if $n(u)=+1$ and **time-like** if $n(u)=-1$. Two facts of Section 2.14 are used:

- the key identity $-u\,\gamma(w)\,u^{-1}=\gamma(R_uw)$ for every vector $w$, where $R_u$ is the reflection of vectors in the hyperplane orthogonal to $v$;
- Theorem 2.8 with one factor, $u^TCu=-n(u)\,C$, hence $u^TC=-n(u)\,C\,u^{-1}$. The number $-n(u)$ is the Pin character of $u$; for a space-like $u$ it is $-1$.

**The reflected frame.** Let $e$ be a vielbein. We define a second vielbein $e_u$ in two steps. First, rotate the frame by the constant matrix $\Lambda$ that the spin matrix $u$ covers, $u^{-1}\gamma^au=\Lambda^a{}_b\gamma^b$; such a $\Lambda$ exists and lies in $\mathrm O(4,4)$ by Theorem 2.9. The local spin covariance theorem of Section 4.12 was stated for spin transformations, but its proof uses only two properties of the spin matrix, the covering relation and the determinant 1, and $u$ has both. So it applies to $u$ and gives, for the rotated frame, the spinor connection $u\Omega_\mu u^{-1}$ (the term $(\partial_\mu u)u^{-1}$ vanishes, $u$ being constant) and $D'_\mu(u\Psi)=u\,D_\mu\Psi$. The curved gammas of the rotated frame are $u\gamma^\mu u^{-1}$: the inverse vielbein of $e'_\mu{}^a=\Lambda^a{}_be_\mu{}^b$ is $e'_a{}^\mu=e_c{}^\mu(\Lambda^{-1})^c{}_a$, and the inverted covering relation $u\gamma^cu^{-1}=(\Lambda^{-1})^c{}_a\gamma^a$ gives $e'_a{}^\mu\gamma^a=e_c{}^\mu\,u\gamma^cu^{-1}$. Second, reverse all eight frame vectors; by Section 15.3 this changes the curved gammas by a sign and leaves the spinor connection unchanged. The result is a vielbein $e_u$ with

$$
\gamma_u^\mu=-u\,\gamma^\mu u^{-1},\qquad \Omega^{(u)}_\mu=u\,\Omega_\mu u^{-1},\qquad D^{(u)}_\mu(u\Psi)=u\,D_\mu\Psi .
$$

It describes the same metric, because $\{\gamma_u^\mu,\gamma_u^\nu\}=u\{\gamma^\mu,\gamma^\nu\}u^{-1}=2g^{\mu\nu}$. By the key identity, $\gamma_u^\mu=e_a{}^\mu\,\gamma(R_ue_a)$: every frame direction $a$ now carries the reflected vector $R_ue_a$ instead of $e_a$. So $e_u$ is the frame **reflected by $R_u$**; Stage 5 calls this the twisted frame action and writes $e\to e\,R_u$.

**Theorem 15.5 (T2, the mirror map).** Let $u$ be a unit vector, $e$ any vielbein, $e_u$ the reflected frame, and $\Psi$ any configuration of commuting or Grassmann components. Put $\Psi_u:=u\Psi$. Then

$$
S[e_u,\Psi_u]=-n(u)\,S[e,\Psi],\qquad K[e_u,\Psi_u]=n(u)\,K[e,\Psi],\qquad J^\mu[e_u,\Psi_u]=n(u)\,J^\mu[e,\Psi].
$$

For a **space-like** $u$ ($n(u)=+1$, Pin character $-1$):

$$
\begin{aligned}
&\mathcal L_{m,\lambda}[e_u,\Psi_u]=\mathcal L_{-m,\lambda}[e,\Psi],\qquad T_{\mu\nu}[e_u,\Psi_u;m,\lambda]=T_{\mu\nu}[e,\Psi;-m,\lambda],\\
&E_{-m,\lambda}[e_u,\Psi_u]=-u\,E_{m,\lambda}[e,\Psi],
\end{aligned}
$$

so $\Psi$ solves the field equations with $(m,\lambda)$ in the frame $e$ exactly when $u\Psi$ solves them with $(-m,\lambda)$, **the same coupling**, in the reflected frame; the energy–momentum tensor and the current are the same, and the scalar density is opposite. For a **time-like** $u$ ($n(u)=-1$) one gets instead $\mathcal L_{m,\lambda}[e_u,\Psi_u]=-\mathcal L_{-m,-\lambda}[e,\Psi]$, a map of the T1 type.

*Proof.* Write $n=n(u)$. Step 1 (adjoint). By Lemma 15.1 and $u^\dagger=u^T$, $\bar\Psi_u=\Psi^\dagger u^TC=-n\,\Psi^\dagger C\,u^{-1}=-n\,\bar\Psi u^{-1}$. For the derivative, $D^{(u)}_\mu\bar\Psi_u=\partial_\mu\bar\Psi_u-\bar\Psi_u\,u\Omega_\mu u^{-1}=-n\bigl[(\partial_\mu\bar\Psi)u^{-1}-\bar\Psi\Omega_\mu u^{-1}\bigr]=-n\,(D_\mu\bar\Psi)\,u^{-1}$.

Step 2 (the bilinears). $S[e_u,\Psi_u]=(-n\bar\Psi u^{-1})(u\Psi)=-nS$. For the kinetic term,

$$
\bar\Psi_u\gamma_u^\mu D^{(u)}_\mu\Psi_u=\bigl(-n\bar\Psi u^{-1}\bigr)\bigl(-u\gamma^\mu u^{-1}\bigr)\bigl(uD_\mu\Psi\bigr)=n\,\bar\Psi\gamma^\mu D_\mu\Psi ,
$$

and in the same way $(D^{(u)}_\mu\bar\Psi_u)\gamma_u^\mu\Psi_u=n\,(D_\mu\bar\Psi)\gamma^\mu\Psi$, so $K\to nK$. The current has one gamma and no derivative: $J^\mu\to nJ^\mu$.

Step 3 (Lagrangian). For $n=+1$: $\mathcal L_{m,\lambda}[e_u,\Psi_u]=\sqrt{|g|}\,[K-m(-S)-\tfrac\lambda2S^2]=\mathcal L_{-m,\lambda}[e,\Psi]$. For $n=-1$: $\sqrt{|g|}\,[-K-mS-\tfrac\lambda2S^2]=-\mathcal L_{-m,-\lambda}[e,\Psi]$.

Step 4 (energy–momentum tensor). With $\gamma^u_\mu=g_{\mu\nu}\gamma_u^\nu=-u\gamma_\mu u^{-1}$, each bilinear of the bracket of $T_{\mu\nu}$ picks up the factor $n$ exactly as in Step 2, and $g_{\mu\nu}\mathcal L_s$ follows Step 3. For $n=+1$ every term of $T_{\mu\nu}[e_u,\Psi_u;m,\lambda]$ equals the corresponding term of $T_{\mu\nu}[e,\Psi;-m,\lambda]$.

Step 5 (field equation, $n=+1$). $E_{-m,\lambda}[e_u,\Psi_u]=(-u\gamma^\mu u^{-1})(uD_\mu\Psi)-(-m+\lambda(-S))u\Psi=-u\bigl[\gamma^\mu D_\mu\Psi-(m+\lambda S)\Psi\bigr]=-u\,E_{m,\lambda}[e,\Psi]$, and $u$ is invertible. As in Section 15.3 no two field components were exchanged, so the proof holds for both statistics. $\square$

**Remarks.**

- *The other lift.* Without the reversal of the frame (the frame rotated only by $\Lambda$, curved gammas $u\gamma^\mu u^{-1}$), the kinetic term gets $-n$ instead of $n$, and a space-like $u$ gives $-\mathcal L_{m,-\lambda}$: this is erratum E3 of the contract and the "other lift" of Chapter 6 (check `PAIR_T2frame_untwistedSpacelikeContractE3`). Composing that lift with $\gamma^8$ gives back T2 (check `PAIR_T2frame_gamma8TimesUntwistedSpacelike`).
- *The canonical structure is preserved.* For $u=\gamma^0,\gamma^1,\gamma^2,\gamma^3$ (and $\gamma^4$) one has $uBu^\dagger=+B$, for $u=\gamma^5,\gamma^6,\gamma^7$ one has $uBu^\dagger=-B$ (check `PAIR_algebra_kreinUnderBasicReflections`; for example $\gamma^0B\gamma^0=-i\gamma^0C\gamma^4\gamma^0=-iC\gamma^4=B$, because $\gamma^0$ anticommutes with both $C$ and $\gamma^4$). The mirror map by a space-like basis direction therefore keeps the anticommutator $+B$: the mirror image of a state of the positive-norm quantum theory is again a state of that theory, with the same energies and charges.
- *The mirror pair doubles.* For a space-like $u$ the pair $\{(m,\lambda,e,\Psi),\ (-m,\lambda,e_u,u\Psi)\}$ has $T^{\mathrm{pair}}=2T$, $J^{\mathrm{pair}}=2J$, $\mathcal L^{\mathrm{pair}}=2\mathcal L$ and $S^{\mathrm{pair}}=0$ (check `PAIR_totals_fieldLevelMirrorPair`). A T2 pair is a universe and its mirror image; it does not cancel.
- *For the Grassmann field without a reflection.* Chapter 6 found that the antilinear map $\Psi\to\gamma^8\Psi^\ast$ sends $\mathcal L_{m,\lambda}$ to $\mathcal L_{-m,\lambda}$ for Grassmann components; combined with a space-like reflection it becomes an exact symmetry that reverses the charge (the CP of Chapter 17).

**How T2 was verified.** For the eight basis vectors $\gamma^0,\dots,\gamma^7$ and for general rational space-like and time-like unit vectors, with exact jets of the general test vielbein G1: the character $-n(u)$ (`PAIR_T2frame_characterIsMinusNorm`), the geometry of the reflected frames (`PAIR_T2frame_frameReflectionsGeometry`), $\mathcal L\to\mathcal L_{-m,\lambda}$ for space-like $u$ (`PAIR_T2frame_twistedSpacelikeMapsToMinusMSameLambda`), the T1 type for time-like $u$ (`PAIR_T2frame_twistedTimelike`), and the on-shell images (`PAIR_T2frame_onShellImage`); the full table is `T2frameTable` in `pairing-theory.json`.

### 15.6 The mirror universe across the Z2 brane

In the primordial field the mirror map becomes very concrete. Chapter 9 (Section 9.16) and Chapter 13 (Section 13.2) extend the static member of the notebook's field beyond the end $y=0$ of the notebook's chart by a mirror copy, glued along the **Z2 brane** $y=0$:

$$
ds^2=dy^2-dx_4^2+W(y)^2\Bigl[e^{2a_{4,0}}\bigl(dx_1^2+dx_2^2+dx_3^2\bigr)-e^{-2a_{4,0}}\bigl(dx_5^2+dx_6^2+dx_7^2\bigr)\Bigr],\qquad W(y)=e^{-H|y|}.
$$

Here $y$ is the proper hidden coordinate, the side $y<0$ is the notebook's patch and $y>0$ its mirror copy. We write $s_\mu=-1$ for $\mu=y$ and $s_\mu=+1$ for the other seven coordinates. The warp $W$ is even in $y$, and its derivative $W'$ is odd.

**The Dirac operator.** The vielbein is diagonal, $h=(1,\,We^{a_{4,0}}\,(\times3),\,1,\,We^{-a_{4,0}}\,(\times3))$ in the order $(y,x_1,\dots,x_7)$, so $\gamma^{x_y}=\gamma^0$, $\gamma^{x_l}=W^{-1}e^{-a_{4,0}}\gamma^l$ for $l=1,2,3$, $\gamma^{x_4}=\gamma^4$ and $\gamma^{x_j}=W^{-1}e^{a_{4,0}}\gamma^j$ for $j=5,6,7$. Every curved gamma is an even function of $y$ times the frame gamma with the same number. The diagonal-vielbein formula of Section 4.11 gives exactly six nonzero connection matrices, one for each warped direction $p\in\{1,2,3,5,6,7\}$:

$$
\Omega_p=c_p(y)\,S^{0p},\qquad c_l=-W'e^{a_{4,0}}\ (l=1,2,3),\qquad c_j=+W'e^{-a_{4,0}}\ (j=5,6,7),\qquad \Omega_y=\Omega_4=0 ,
$$

and every $c_p$ is an odd function of $y$. (For $y<0$ this is the connection of Section 9.13 written in the coordinate $y$; it gives $\gamma^\mu\Omega_\mu=3(W'/W)\gamma^0$, which is $+3H\gamma^0$ for $y<0$ and $-3H\gamma^0$ for $y>0$.)

**Lemma 15.6.** For $\Psi'(y,x):=\gamma^0\,\Psi(-y,x)$ (all other coordinates $x$ unchanged) and $y\ne0$:

$$
D_\mu\Psi'(y)=s_\mu\,\gamma^0\,(D_\mu\Psi)(-y)\quad\text{for every }\mu,\qquad \gamma^0\gamma^{x_\mu}(y)\gamma^0=-s_\mu\,\gamma^{x_\mu}(-y).
$$

*Proof.* For $\mu=y$, the chain rule gives $\partial_y[\Psi(-y)]=-(\partial_y\Psi)(-y)$, and $\Omega_y=0$. For $\mu=4$ and the other coordinates, $\partial_\mu$ does not touch $y$. For a warped direction $p$ the connection term needs $S^{0p}\gamma^0=\tfrac12\gamma^0\gamma^p\gamma^0=-\tfrac12\gamma^p=-\gamma^0S^{0p}$, so that

$$
\begin{aligned}
\Omega_p(y)\,\gamma^0\Psi(-y)&=c_p(y)\,S^{0p}\gamma^0\Psi(-y)=-c_p(y)\,\gamma^0S^{0p}\Psi(-y)\\
&=\gamma^0\,c_p(-y)S^{0p}\Psi(-y)=\gamma^0\,\Omega_p(-y)\Psi(-y),
\end{aligned}
$$

using that $c_p$ is odd. Together, $D_p\Psi'(y)=\gamma^0(D_p\Psi)(-y)$. For the gammas, $\gamma^0\gamma^0\gamma^0=\gamma^0$ and $\gamma^0\gamma^a\gamma^0=-\gamma^a$ for $a\ne0$, that is $\gamma^0\gamma^a\gamma^0=-s_a\gamma^a$; the curved gammas are even functions of $y$ times frame gammas. $\square$

**Theorem 15.7 (T2 across the brane).** For $\Psi'(y)=\gamma^0\Psi(-y)$ and both statistics:

$$
\begin{aligned}
&\gamma^\mu D_\mu\Psi'(y)=-\gamma^0\,(\gamma^\mu D_\mu\Psi)(-y),\qquad S[\Psi'](y)=-S[\Psi](-y),\qquad K[\Psi'](y)=K[\Psi](-y),\\
&E_{-m,\lambda}[\Psi'](y)=-\gamma^0\,E_{m,\lambda}[\Psi](-y),\qquad \mathcal L_{-m,\lambda}[\Psi'](y)=\mathcal L_{m,\lambda}[\Psi](-y),\\
&T_{\mu\nu}[\Psi';-m,\lambda](y)=s_\mu s_\nu\,T_{\mu\nu}[\Psi;m,\lambda](-y),\qquad J^\mu[\Psi'](y)=s_\mu\,J^\mu[\Psi](-y).
\end{aligned}
$$

So $\Psi$ solves the field equations with $(m,\lambda)$ on the side $y<0$ exactly when $\Psi'$ solves them with $(-m,\lambda)$, the same $\lambda$, on the side $y>0$. The mirror universe has the same energy density $\rho=T_{44}$, the same pressures and the same charge density $J^4$ at mirror points; the scalar density and the flux along $y$ change sign.

*Proof.* By Lemma 15.6, inserting $1=\gamma^0\gamma^0$ in front of each curved gamma,

$$
\begin{aligned}
\gamma^\mu D_\mu\Psi'(y)&=\sum_\mu\gamma^{x_\mu}(y)\,s_\mu\gamma^0(D_\mu\Psi)(-y)=\sum_\mu s_\mu\,\gamma^0\bigl(\gamma^0\gamma^{x_\mu}(y)\gamma^0\bigr)(D_\mu\Psi)(-y)\\
&=-\gamma^0\sum_\mu s_\mu^2\,\gamma^{x_\mu}(-y)(D_\mu\Psi)(-y)=-\gamma^0\,(\gamma^\mu D_\mu\Psi)(-y),
\end{aligned}
$$

because $s_\mu^2=1$. The adjoint is $\bar\Psi'(y)=\Psi(-y)^\dagger\gamma^0C=-\bar\Psi(-y)\gamma^0$, because $\gamma^0$ is real symmetric and anticommutes with $C$ (Section 2.9, (C1)). Hence $S[\Psi'](y)=-\bar\Psi\gamma^0\gamma^0\Psi=-S(-y)$, and for any bilinear with one curved gamma and one derivative,

$$
\bar\Psi'\gamma_\mu D_\nu\Psi'(y)=\bigl(-\bar\Psi\gamma^0\bigr)\gamma_\mu\bigl(s_\nu\gamma^0D_\nu\Psi\bigr)(-y)=-s_\nu\,\bar\Psi\bigl(\gamma^0\gamma_\mu\gamma^0\bigr)D_\nu\Psi(-y)=s_\mu s_\nu\,\bigl(\bar\Psi\gamma_\mu D_\nu\Psi\bigr)(-y).
$$

The same computation holds for the terms with $D_\mu\bar\Psi'$ (conjugate Lemma 15.6). The kinetic term consists of the terms with $\mu=\nu$ contracted with $\gamma^{x_\mu}$, where $s_\mu^2=1$, so $K[\Psi'](y)=K[\Psi](-y)$; the current has one gamma and no derivative, so $J^\mu[\Psi'](y)=s_\mu J^\mu[\Psi](-y)$. The field equation: $E_{-m,\lambda}[\Psi'](y)=-\gamma^0(\gamma^\mu D_\mu\Psi)(-y)-\bigl(-m-\lambda S(-y)\bigr)\gamma^0\Psi(-y)=-\gamma^0E_{m,\lambda}[\Psi](-y)$. The Lagrangian: $\sqrt{|g|}=W^6$ is even (the factors $e^{\pm a_{4,0}}$ cancel), and $K-(-m)(-S)-\tfrac\lambda2S^2=K-mS-\tfrac\lambda2S^2$. The energy–momentum tensor: the bracket terms were just computed, $g_{\mu\nu}$ is diagonal and even, and $\mathcal L_s$ maps as the Lagrangian. $\square$

(Checks `PAIR_T2z2_geometry`, `PAIR_T2z2_diracOperator`, `PAIR_T2z2_scalarOdd`, `PAIR_T2z2_lagrangianEven`, `PAIR_T2z2_emtPullback` for all 64 components, `PAIR_T2z2_currentPullback`; the Python checker adds `S5_T2z2_kineticEven` and `S5_T2z2_fieldEquationMapsToMinusMSameLambda`, and `PAIR_T2z2_sameMassFails` confirms that the image does **not** solve the equations with the same mass.)

**Corollary 15.8 (the mirror universe carries the mass $-M$).** Let the mass be a function $m(y)$. By the proof above, the image $\Psi'$ solves the equations with the mass function $y\mapsto-m(-y)$. A configuration that is **Z2-symmetric**, $\Psi(y)=\pm\gamma^0\Psi(-y)$, solves the field equations on both sides with one mass function $m(y)$ exactly when $\bigl(m(y)+m(-y)\bigr)\Psi(y)=0$, that is, where $\Psi\ne0$, when the mass function is **odd**: $m(-y)=-m(y)$. With $m=+M$ on the notebook's side, the mirror side carries $-M$. With the Hartree term the effective mass $m(y)+\lambda S(y)$ of a Z2-symmetric configuration is odd automatically, because $S$ is odd by Theorem 15.7. (Checks `PAIR_T2z2_massFunctionMap`, `PAIR_T2z2_symmetricIffOddMass`; this is erratum E4.6 of `handoff/specs/STAGE4_SPEC.md`, which Section 13.5 used.)

*Proof.* The proof of Theorem 15.7 never used that $m$ is constant; with a mass function it says that $\Psi'(y)=\gamma^0\Psi(-y)$ solves the equations with the mass function $-m(-y)$ whenever $\Psi$ solves them with $m(y)$. Now let $\Psi$ solve the equations with $m(y)$ on both sides and be Z2-symmetric, so that $\Psi'=\pm\Psi$. Then $\Psi$ solves the equations with $m(y)$ and with $-m(-y)$; subtracting the two equations leaves $\bigl(m(y)+m(-y)\bigr)\Psi(y)=0$. Conversely, if $m$ is odd, take a solution on $y<0$ and define it on $y>0$ by $\Psi(y):=\pm\gamma^0\Psi(-y)$; by the same statement it solves the equations with $-m(-y)=m(y)$ there. $\square$

**Every Stage-4 Kohn–Sham state is already a mirror pair.** The Kohn–Sham problem of Chapter 13 imposes the parity conditions $\Psi(-y)=\pm\gamma^0\Psi(y)$ at the brane, that is, it is solved on $y\le0$ and continued to $y>0$ by the Z2 identification. By Corollary 15.8, every such state describes a universe of mass $+M$ on the side $y<0$ and a universe of mass $-M$ on the side $y>0$, with the same $\lambda$, the same energy density and pressures, the same charge density and the opposite scalar density, joined by the brane, which carries the Israel stress of Section 9.16 (`pairing-theory.json`, key `T3.stage4Z2Pair`). This is a geometric realization of the notebook's "pair of universes of masses $\pm M$". It is a **model**: the Z2 gluing is a choice (Section 9.16), and nothing here says that the pair was created.

**Worked example: the brane zero mode.** At zero momentum, with a constant mass $M>0$ and no interaction, the block equation of Section 13.5 has on the side $y<0$ the zero mode $\chi=(e^{My},0)$ of parity $+$ (Section 13.6). In the block basis $\gamma^0$ acts as $\sigma_z$, so the Z2 continuation of parity $+$ is $\chi(y)=\sigma_z\chi(-y)=(e^{-My},0)$ for $y>0$. There the first block equation $\chi_1'=M_{\mathrm{eff}}\chi_1$ reads $-Me^{-My}=M_{\mathrm{eff}}e^{-My}$, so $M_{\mathrm{eff}}=-M$: the mirror side has the mass $-M$, and the mode $e^{-M|y|}$ is localized at the brane from both sides (Exercise 15.7).

**A remark on the even-mass symmetry.** For an even mass function, Stage 4 used the reflection $P_B:\Psi'(y)=i\gamma^0\gamma^8\Psi(-y)$ (Section 13.5). At the level of the classical field it is, up to the factor $i$, the chirality map of T1 followed by the reflection of Theorem 15.7, so it maps $(m,\lambda)$ first to $(-m,-\lambda)$ and then to $(m,-\lambda)$, with $\mathcal L\to-\mathcal L$ (check `PAIR_T2z2_PBfieldLevelFlipsLambda`). In the Kohn–Sham model it is a symmetry with the same $\lambda$, because the matrix $BC$ of the scalar density in the expectation-value rule is $P_B$-even while $C$ is $P_B$-odd (checks `PAIR_T2z2_ruleParities`, `S5_T2z2_PBRuleMatrixEvenCOdd`; Exercise 15.16). This is a first instance of the effect explained in Section 15.8.

### 15.7 Theorem T3: the Kohn–Sham level

We now turn to the Kohn–Sham approximation of Chapter 13: a finite number $N$ of quanta in the static primordial field, described by orbitals in eight $2\times2$ blocks. The question is whether the Kohn–Sham ground state and first excited state of a universe of mass $+M$ have exact partners in a universe of mass $-M$.

**The Kohn–Sham problem, recalled.** (Chapter 13; for the statistics sign, Chapter 14.) The 16 components are split by the commuting labels $(j,s_2,s_3)$ of Section 13.4 into eight blocks of two components $\chi=(\chi_1,\chi_2)$. At a 3-momentum $\mathbf k=(k,0,0)$ an orbital of block type $j$ solves

$$
h_j(M_{\mathrm{eff}},v)\,\chi=\varepsilon\,\chi,\qquad h_j(M,v):=j\Bigl[-i\sigma_x\frac{d}{dy}+M(y)\,\sigma_y+\xi(y)\,k\,\sigma_z\Bigr]+v(y)
$$

on $-L\le y\le0$, with the momentum weight $\xi(y)=e^{-Hy-a_{4,0}}$ and the Pauli matrices $\sigma_x,\sigma_y,\sigma_z$, in the notation of Chapter 13 (the check names and `pairing-theory.json` write the Pauli matrices as sigma1, sigma2, sigma3, and the theory files call the weight `kappa`). The boundary conditions (Section 13.5) are a **parity** at the brane, $p=+$: $\chi_2(0)=0$ or $p=-$: $\chi_1(0)=0$, both sectors belonging to every state, and a **bag condition** at the tip, $(1-Q(\theta))\chi(-L)=0$ with $Q(\theta)=\cos\theta\,\sigma_z+\sin\theta\,\sigma_y$; Stage 4 uses $\theta=0$, that is $\chi_2(-L)=0$. The expectation-value rule of Section 8.12 gives, per orbital, the proper densities of Section 13.7,

$$
n=\frac{e^{-6Hy}}{\ell^3}\chi^\dagger\chi,\qquad s=\frac{e^{-6Hy}}{\ell^3}\,j\,\chi^\dagger\sigma_y\chi,\qquad t=\frac{e^{-6Hy}}{\ell^3}\,j\,\chi^\dagger\sigma_z\chi,\qquad c=\frac{e^{-6Hy}}{\ell^3}\,j\,\chi^\dagger\sigma_x\chi ,
$$

the number (charge) density, the scalar density, the density of the 3-momentum current and the current along $y$. Summed over the orbitals with the weights $w=f$ (particle levels) or $w=-(1-f)$ (sea levels), $f$ the Fermi–Dirac occupation at the temperature $T$ with the chemical potential $\mu$ fixed by $N$, they give $n_p(y)$ and $S_p(y)$. The Kohn–Sham potentials are

$$
M_{\mathrm{eff}}=m+\Bigl(1+\frac{\mathrm{sg}}{16}\Bigr)\lambda\,S_p,\qquad v=\mathrm{sg}\,\frac{\lambda}{16}\,n_p,
$$

where the **statistics sign** is $\mathrm{sg}=-1$ for dirac16complex (Section 13.8: $M_{\mathrm{eff}}=m+\tfrac{15}{16}\lambda S_p$, $v=-\tfrac{\lambda}{16}n_p$) and $\mathrm{sg}=+1$ for dirac16complex00, whose exchange term has the opposite sign (Chapter 14: $M_{\mathrm{eff}}=m+\tfrac{17}{16}\lambda S_p$, $v=+\tfrac{\lambda}{16}n_p$; checks `PAIR_stat_uniformGasExchange`, `PAIR_stat_ldaPotentials`). Chapter 6 writes this sign as $s$; here the letter $s$ is taken by the scalar density. The energy is $E=\sum w\,\varepsilon-E_H-E_x$ with $E_H+E_x=\lambda\int\bigl[\tfrac12S_p^2+\tfrac{\mathrm{sg}}{32}(n_p^2+S_p^2)\bigr]dV$ (Section 13.9), and the free energy is $F=E-TS_{\mathrm{ent}}$.

**Lemma 15.9 (the chirality in the reduced equation and in the blocks).**

1. In the 16-component reduced equation of Section 13.3, $\chi'=N(M)\chi$ with $N(M)=M\gamma^0-i\xi k\,\gamma^0\gamma^1+i(\varepsilon-v)\gamma^0\gamma^4$, one has $\gamma^8N(M)\gamma^8=N(-M)$.
2. $\gamma^8$ maps the block $(j,s_2,s_3)$ onto the block $(-j,s_2,s_3)$, and in the block bases it acts by $\tau\,\sigma_y$ with a number $\tau$ of modulus 1.

*Proof.* (1) $\gamma^0$ is odd, $\gamma^0\gamma^1$ and $\gamma^0\gamma^4$ are even (Lemma 15.2), so only the mass term changes sign. (2) $J=\gamma^0\gamma^1\gamma^4$ is odd and $K_1=\gamma^2\gamma^3$, $K_2=\gamma^5\gamma^6$ are even. If a column $\phi$ has $J\phi=j\phi$, $K_1\phi=is_2\phi$ and $K_2\phi=is_3\phi$, then $J\gamma^8\phi=-\gamma^8J\phi=-j\,\gamma^8\phi$ while $K_{1,2}\gamma^8\phi=\gamma^8K_{1,2}\phi$: the image lies in the block $(-j,s_2,s_3)$. Write $\gamma^8[v_+\ v_-]=[w_+\ w_-]\,G$ with the bases $(v_+,v_-)$ of the first and $(w_+,w_-)$ of the second block and a $2\times2$ matrix $G$. In both blocks $A_0=\gamma^0$ acts as $\sigma_z$ and $A_1=\gamma^0\gamma^1$ as $-i\sigma_y$, while $A_4=\gamma^0\gamma^4$ acts as $j\sigma_x$ in the first and as $-j\sigma_x$ in the second block (Section 13.4). From $\gamma^8A_0=-A_0\gamma^8$ we get $G\sigma_z=-\sigma_zG$; from $\gamma^8A_4=A_4\gamma^8$ we get $G(j\sigma_x)=(-j\sigma_x)G$, that is $G\sigma_x=-\sigma_xG$. Write $G=g_0+g_1\sigma_x+g_2\sigma_y+g_3\sigma_z$ (every $2\times2$ matrix has this form). Anticommuting with $\sigma_z$ forces $g_0=g_3=0$, anticommuting with $\sigma_x$ forces $g_0=g_1=0$; so $G=\tau\sigma_y$ with $\tau:=g_2$. The bases are orthonormal and $\gamma^8$ is unitary (Hermitian with square 1), so $G$ is unitary and $|\tau|=1$. $\square$

The exact computation finds $\tau=\pm1$ for all eight blocks in the block basis of the Stage-4 theory file `kohn-sham-theory.json` (check `PAIR_T3block_gamma8IsSigma2BetweenPartnerBlocks`).

**Worked example.** Section 13.4 lists the basis of the block $(1,1,1)$; the same construction gives the basis of the block $(-1,1,1)$ (`kohn-sham-theory.json`, block index 4). Multiplied by $\sqrt8$, the four vectors are

$$
\begin{aligned}
\sqrt8\,v_+&=(0,0,0,0,\,1,i,-1,i,\,0,0,0,0,\,1,i,-1,i),\\
\sqrt8\,v_-&=(i,-1,-i,-1,\,0,0,0,0,\,-i,1,i,1,\,0,0,0,0),\\
\sqrt8\,w_+&=(1,i,-1,i,\,0,0,0,0,\,1,i,-1,i,\,0,0,0,0),\\
\sqrt8\,w_-&=(0,0,0,0,\,i,-1,-i,-1,\,0,0,0,0,\,-i,1,i,1).
\end{aligned}
$$

Since $\gamma^8$ changes the sign of the components 0 to 7,

$$
\begin{aligned}
\sqrt8\,\gamma^8v_+&=(0,0,0,0,\,-1,-i,1,-i,\,0,0,0,0,\,1,i,-1,i)=\sqrt8\,i\,w_-,\\
\sqrt8\,\gamma^8v_-&=(-i,1,i,1,\,0,0,0,0,\,-i,1,i,1,\,0,0,0,0)=-\sqrt8\,i\,w_+,
\end{aligned}
$$

which is $\gamma^8[v_+\ v_-]=[w_+\ w_-]\,\sigma_y$, that is $\tau=1$ (Exercise 15.10).

**Lemma 15.10 (the block map).** For every block type $j$, mass function $M(y)$ and potential $v(y)$,

$$
\sigma_y\,h_j(M,v)\,\sigma_y=h_{-j}(-M,v),
$$

as differential operators. Hence if $\chi$ is an orbital of $h_j(M,v)$ with the level $\varepsilon$, then $\sigma_y\chi$ is an orbital of $h_{-j}(-M,v)$ with the **same** level $\varepsilon$ and the same 3-momentum.

*Proof.* The Pauli matrices anticommute pairwise and square to 1, so $\sigma_y\sigma_x\sigma_y=-\sigma_x$, $\sigma_y\sigma_y\sigma_y=\sigma_y$, $\sigma_y\sigma_z\sigma_y=-\sigma_z$, and the constant $\sigma_y$ commutes with $d/dy$. Therefore $\sigma_yh_j(M,v)\sigma_y=j\bigl[+i\sigma_x\tfrac{d}{dy}+M\sigma_y-\xi k\sigma_z\bigr]+v=(-j)\bigl[-i\sigma_x\tfrac{d}{dy}+(-M)\sigma_y+\xi k\sigma_z\bigr]+v$. If $h_j\chi=\varepsilon\chi$, then $h_{-j}(-M,v)(\sigma_y\chi)=\sigma_yh_j(M,v)\sigma_y\sigma_y\chi=\sigma_yh_j\chi=\varepsilon\,\sigma_y\chi$. $\square$

(Checks `PAIR_T3block_sigma2MapsBlockODE`, `PAIR_T3block_hamiltonianSigma2`.) In the real form $\chi=(a,\,ib)$ of Section 13.5, $\sigma_y(a,\,ib)=(b,\,ia)$: the map is the swap $(a,b,j)\to(b,a,-j)$ that Section 13.14 found directly from the real system (check `PAIR_T3block_sigma2IsRustSwap`).

**Lemma 15.11 (the boundary conditions).** Under $\chi\to\sigma_y\chi$: the parity at the brane changes, $p\to-p$; the bag angle at the tip changes as $\theta\to\pi-\theta$; in particular the Stage-4 condition $\theta=0$ ($\chi_2(-L)=0$) becomes $\theta=\pi$ ($\chi_1(-L)=0$).

*Proof.* $\sigma_y\chi=(-i\chi_2,\,i\chi_1)$, so $\chi_2(0)=0$ becomes $(\sigma_y\chi)_1(0)=0$ and conversely. For the bag, $\sigma_yQ(\theta)\sigma_y=\cos\theta\,\sigma_y\sigma_z\sigma_y+\sin\theta\,\sigma_y=-\cos\theta\,\sigma_z+\sin\theta\,\sigma_y=Q(\pi-\theta)$, since $\cos(\pi-\theta)=-\cos\theta$ and $\sin(\pi-\theta)=\sin\theta$. So $(1-Q(\theta))\chi=0$ is equivalent to $(1-Q(\pi-\theta))\sigma_y\chi=\sigma_y(1-Q(\theta))\chi=0$. For $\theta=0$: $Q(\pi)=-\sigma_z$ and $(1+\sigma_z)\sigma_y\chi(-L)=0$ says $(\sigma_y\chi)_1(-L)=0$. $\square$

(Checks `PAIR_T3block_parityMap`, `PAIR_T3block_bagAngleMap`.) Since every Stage-4 Kohn–Sham state contains both parity sectors, the exchange $p\to-p$ only relabels the sectors. The one boundary condition that really changes is the tip bag.

**Lemma 15.12 (the densities).** Under $\chi\to\sigma_y\chi$ together with $j\to-j$, with the expectation-value rule,

$$
(n,\,s,\,t,\,c)\ \longrightarrow\ (n,\,-s,\,t,\,c).
$$

*Proof.* $n\propto(\sigma_y\chi)^\dagger(\sigma_y\chi)=\chi^\dagger\chi$. $s\propto(-j)\,\chi^\dagger\sigma_y\sigma_y\sigma_y\chi=-j\,\chi^\dagger\sigma_y\chi$. $t\propto(-j)\,\chi^\dagger\sigma_y\sigma_z\sigma_y\chi=(-j)(-\chi^\dagger\sigma_z\chi)=j\,\chi^\dagger\sigma_z\chi$. $c\propto(-j)(-\chi^\dagger\sigma_x\chi)=j\,\chi^\dagger\sigma_x\chi$. The phase $\tau$ of Lemma 15.9 drops out, since $|\tau|^2=1$. $\square$

(Check `PAIR_T3block_densityAndCurrentMaps`; measurement `T3block_densitySigns_sigma2` $=\{1,-1,1,1\}$.)

**Theorem 15.13 (T3, the Kohn–Sham level).** Let the **universe of mass $+M$** be the Kohn–Sham problem of Chapter 13 with the bare mass $m$, the coupling $\lambda$, the statistics sign $\mathrm{sg}$, both parity sectors, the tip bag angle $\theta$, $N$ quanta at the temperature $T$ (Fermi–Dirac occupations, normal ordering against the free Dirac sea, the particle and sea labels fixed by continuity from $\lambda=0$ with the zero modes counted as particles, Section 13.7). Let the **universe of mass $-M$** be the same problem with the bare mass $-m$, the **same** $\lambda$ and $\mathrm{sg}$, both parity sectors and the tip bag angle $\pi-\theta$. Then the map $\chi\to\sigma_y\chi$ in the partner block $(j,s_2,s_3)\to(-j,s_2,s_3)$, at the same momentum, sends the one problem exactly onto the other:

1. the self-consistent potentials correspond as $M_{\mathrm{eff}}\to-M_{\mathrm{eff}}$ and $v\to v$, and every self-consistent solution of the $+M$ problem is mapped onto a self-consistent solution of the $-M$ problem, and conversely;
2. the Kohn–Sham levels with their multiplicities, the occupations, the particle and sea labels, the weights, $\mu$, $E$, $F$ and $S_{\mathrm{ent}}$ are identical;
3. the profiles $n_p(y)$, $v(y)$, $t$, $c$ and the energy–momentum profiles $\rho(y)$, $p_y(y)$, $p_3(y)$, $p_t(y)$ are identical, while $S_p(y)\to-S_p(y)$ and $M_{\mathrm{eff}}(y)\to-M_{\mathrm{eff}}(y)$;
4. the ground state (defined by continuation in $\lambda$ from $\lambda=0$, erratum E4.8) and the first excited state (the Kohn–Sham gap, the particle–hole list, the Delta-SCF state) of the $+M$ universe are mapped exactly onto those of the $-M$ universe.

With $-\lambda$ in place of $\lambda$ the map fails for $\lambda\ne0$.

*Proof.* Step 1 (potentials). Suppose the $+M$ problem has the densities $(n_p,S_p)$. By Lemma 15.12 the mapped orbitals have the densities $(n_p,-S_p)$. With the bare mass $-m$ and the same $\lambda$ the potentials built from them are

$$
-m+\Bigl(1+\frac{\mathrm{sg}}{16}\Bigr)\lambda\,(-S_p)=-M_{\mathrm{eff}},\qquad \mathrm{sg}\,\frac{\lambda}{16}\,n_p=v ,
$$

exactly the potentials $(-M_{\mathrm{eff}},v)$ in which Lemma 15.10 places the mapped orbitals. With $-\lambda$ instead, the mass would be $-m+(1+\tfrac{\mathrm{sg}}{16})\lambda S_p\ne-M_{\mathrm{eff}}$ and the potential $-v\ne v$ whenever $\lambda S_p\ne0$ or $\lambda n_p\ne0$.

Step 2 (spectrum and boundary conditions). By Lemmas 15.10 and 15.11, $\chi$ is an eigenfunction of $h_j(M_{\mathrm{eff}},v)$ with the parity $p$ and the bag $\theta$ exactly when $\sigma_y\chi$ is an eigenfunction of $h_{-j}(-M_{\mathrm{eff}},v)$ with the parity $-p$ and the bag $\pi-\theta$, with the same $\varepsilon$. Since $\sigma_y^2=1$ the correspondence is one to one, so the two spectra coincide with multiplicities, level by level.

Step 3 (occupations and labels). The occupations depend only on $\varepsilon$, $\mu$ and $T$. At $\lambda=0$ the free problems are mapped onto each other by Step 2 (with $M_{\mathrm{eff}}=\pm m$, $v=0$), so the free partner of a mapped level is the mapped free partner, with the same $\varepsilon_{\mathrm{free}}$; hence the particle and sea labels, and the weights $f$ or $-(1-f)$, are the same. The zero modes $(e^{my},0)$ of the $+M$ problem go to the zero modes $\sigma_y(e^{my},0)=(0,\,ie^{my})$ of the $-M$ problem, again particle levels. The particle number $N=\sum w$ is the same function of $\mu$, so $\mu$ is the same.

Step 4 (self-consistency). Steps 1 to 3 say that the iteration map of the self-consistent loop (densities $\to$ potentials $\to$ orbitals and occupations $\to$ densities) of the $-M$ problem is the image of that of the $+M$ problem. Every iterate, and every fixed point, is mapped. The continuation path $\lambda/4,\lambda/2,3\lambda/4,\lambda$ that defines the ground state is the same path in both problems, because $\lambda$ is not changed, and so is every fallback with occupation smearing.

Step 5 (energies). $\sum w\varepsilon$ is the same. $E_H+E_x$ contains $S_p$ only through $S_p^2$ and $n_p$ through $n_p^2$, so it is the same. Hence $E$ is the same, and with the same occupations $S_{\mathrm{ent}}$ and $F$ are the same.

Step 6 (first excited state). The levels, the occupations and the thresholds for holes and particles are the same, so the Kohn–Sham gap and the particle–hole list are the same. The Delta-SCF state fixes the occupations by the identity of the levels (shell, parity, block type, Prüfer index); the mapped identities define the mapped constraint, and by Step 4 its self-consistent solution is the image, with the same energy $E_1$.

Step 7 (energy–momentum tensor). By Section 13.14 (with $L_s=\tfrac\lambda2S_p^2+\tfrac{\mathrm{sg}\lambda}{32}(n_p^2+S_p^2)$ for either statistics), $\rho=\sum w\,\varepsilon\,n-L_s$, $p_y=\sum w\,[\varepsilon n-m\,s-\xi k\,t]-L_s$, $p_3=\tfrac13\sum w\,\xi k\,t+L_s$ and $p_t=L_s$. Under the map $\varepsilon$, $w$, $n$, $t$ and $L_s$ are unchanged, and $m\,s\to(-m)(-s)=m\,s$. So all four profiles are unchanged. $\square$

The statement is the key `T3.theoremStandardRule` of `pairing-theory.json`. Its checks, in both pairing reports (the negative control of the operator check confirms that $-\lambda$ does not map):

```
PAIR_T3block_potentialsStandardRule   PAIR_T3ks_stationarityBothStatistics
PAIR_T3ks_sigma2FunctionalInvariant   PAIR_T3ks_sigma2Densities
PAIR_T3ks_sigma2KSOperatorEquivariant PAIR_T3ks_zeroModeSplittingMapsExactly
PAIR_T3ks_massiveLevelsMap            PAIR_T3emt_standardRulePlusT
PAIR_T3emt_stage4CrossCheck
```

**The hypotheses, once more.** T3 is a theorem about the Kohn–Sham model, not about the exact many-body theory: it assumes the model of Chapter 13 (mean field with the local exchange of the uniform gas, no correlation term, a fixed metric, the good sector, the torus of momenta, the expectation-value rule and normal ordering against the free sea), and it needs the **transformed** tip condition. For dirac16complex00 the model is the one of Chapter 14: a DFT-motivated mean field in which the expectation-value rule and the Pauli filling are imposed by prescription. With the rule, the covariance of the occupied modes is indefinite (on a filled rest shell it has the eigenvalues $+1$ four times, $-1$ four times and $0$ eight times, check `PAIR_stat_expectationRuleCovarianceIndefinite`), so for the commuting field the model is a formal (Krein-signed) Gaussian functional rather than the statistics of a classical random field (`pairing-theory.json`, key `statistics.positivity`). The proof of T3 keeps $\mathrm{sg}$ as a symbol and holds for both values.

**Two remarks on notation and on a second route.** In the Rust solver the block label is $s=-j$ and the orbital is written $\chi=(a,\,ib)$; the map is then $(\text{shell},p,s,n)\to(\text{shell},-p,-s,-n)$ for (shell, parity, block type, Prüfer index), with the same $\varepsilon$ and the orbital $(a,b)\to\pm(b,a)$ (`levelMap` in every `pairing.json`); the Stage-4 tip condition $b(-L)=0$ becomes $a(-L)=0$. The Python reference solver writes the block orbital as $(f,g)$, with parity $+$ meaning $g(0)=0$; in its notation the tip condition $g(-L)=0$ (called `g0`) of the $+M$ universe becomes $f(-L)=0$ (called `f0`), and the map is the swap $f\leftrightarrow g$ together with the block type (`pairing-theory.json`, key `T3.numericsPrescription.componentSwap`). The reflection $\gamma^1$ of the 3-space direction $x_1$ gives a second exact route: it acts as $\sigma_x$ in every block, keeps $j$, reverses $k$ and changes $\theta\to\theta+\pi$, with the same conclusions over closed shells $\{\mathbf k,-\mathbf k\}$ (checks `PAIR_T3block_gamma1IsSigma1InEveryBlock`, `PAIR_T3ks_sigma1FunctionalInvariant`).

**The pair totals at the Kohn–Sham level.** For the ordinary universe of mass $-M$ (the standard rule, the same $\lambda$) the pair of Theorem 15.13 is a **mirror pair**: $E^{\mathrm{pair}}=2E_+$, $F^{\mathrm{pair}}=2F_+$, charge $2N$, $S^{\mathrm{pair}}_p(y)=0$ and every energy–momentum profile doubled (check `PAIR_totals_ksMirrorPair`). It is the Kohn–Sham form of T2.

### 15.8 Why T1 and T3 give different partners

T1 (Section 15.3) says: the image of a universe of mass $+M$ has the coupling $-\lambda$ and the opposite energy. T3 (Section 15.7) says: the partner has the same $\lambda$ and the same energy. Both are built on $\gamma^8$. There is no contradiction, because the two theorems are about different quantities.

**Classical bilinears versus the expectation-value rule.** T1 is about the classical bilinears $\Psi^\dagger X\Psi$ of the field. The Kohn–Sham model uses instead the expectation values of the positive-norm quantum theory of Chapter 8. For one quantum in a normalized mode $u$ above the Dirac sea the rule of Section 8.12 is

$$
\bigl\langle\Psi^\dagger X\Psi\bigr\rangle=u^\dagger B\,X\,u .
$$

So every classical matrix $X$ is replaced by $BX$. By Lemma 15.2, $B$ is odd, and **multiplying by $B$ reverses the parity** under $\gamma^8$. The energy and the current, whose classical matrices are odd, become even; the scalar density, whose classical matrix $C$ is even, becomes odd. Under $u\to\gamma^8u$:

| quantity | classical matrix $X$ | classical bilinear under $\gamma^8$ | rule matrix $BX$ | expectation value under $\gamma^8$ |
| --- | --- | --- | --- | --- |
| charge density | $B$ | changes sign | $B^2=1$ | unchanged |
| scalar density | $C$ | unchanged | $BC=-i\gamma^4$ | changes sign |
| energy, momentum, stresses (the bracket of $T_{\mu\nu}$) | $C\gamma^a$ and $C\gamma^aS^{bc}$ | change sign | $BC\gamma^a$, $BC\gamma^aS^{bc}$ | unchanged |

The first two columns are T1: energy and charge change sign, the scalar density does not, and self-consistency of the mass $m+\lambda S$ then requires $\lambda\to-\lambda$. The last two columns are T3: energy and charge stay, the scalar density changes sign, and self-consistency of $m+\lambda S\to-(m+\lambda S)$ requires the same $\lambda$.

**The same statement for one block.** In the block $(j,s_2,s_3)$ the matrix $B$ acts as the number $js_2$ (Section 13.4), the **Krein sign** of the block. So for a mode that lives in one block, every classical bilinear is $js_2$ times the corresponding expectation value, and in particular the classical energy–momentum tensor of such a mode is $js_2$ times its Kohn–Sham one-body energy–momentum tensor (checks `C00_static_classicalModeIsKreinWeightedKS` and `C00_static_classicalEnergyKreinSigned` of `wolfram-dirac16complex00-report.json`; key `static.classicalVersusKohnSham` of `artifacts/dirac16complex/pair-creation/dirac16complex00-theory.json`). The block map $j\to-j$ reverses the Krein sign. The expectation values are unchanged (T3), so the classical bilinears change sign (T1).

**Worked example (continued).** The rest state $u_+$ of Section 15.3 and its image $\tilde u=\gamma^8u_+$. As a mode of the $-m$ theory, $\tilde u$ is a positive-energy mode: $h(-m)\tilde u=-m(-i\gamma^4)\tilde u=m\,\tilde u$ with $h(m)=-im\gamma^4$ (Section 8.9). Per quantum, with $BC=-i\gamma^4$:

| quantity per quantum | $u_+$, mass $m$ | $\tilde u$, classical bilinear | $\tilde u$, rule with $+B$ (T3) | $\tilde u$, rule with $-B$ (image field) |
| --- | --- | --- | --- | --- |
| charge $\langle J^4\rangle$ | $u_+^\dagger B^2u_+=1$ | $\tilde u^\dagger B\tilde u=-1$ | $\tilde u^\dagger B^2\tilde u=1$ | $-1$ |
| scalar $\langle S\rangle$ | $u_+^\dagger(-i\gamma^4)u_+=1$ | $\tilde u^\dagger C\tilde u=1$ | $\tilde u^\dagger(-i\gamma^4)\tilde u=-1$ | $+1$ |
| energy | $u_+^\dagger h(m)u_+=m$ | $m\,\tilde u^\dagger B\tilde u=-m$ | $\tilde u^\dagger h(-m)\tilde u=m$ | $-m$ |

For $u_+$ the classical and the rule values coincide, because $u_+$ has the Krein sign $u_+^\dagger Bu_+=+1$. (Exercise 15.4 recomputes the table by hand.)

**The Krein image at the Kohn–Sham level.** Section 15.4 showed that the image field $\gamma^8\Psi$ of the quantum theory carries the reversed metric $-B$. Its expectation-value rule is therefore $\langle\Psi_-^\dagger X\Psi_-\rangle=u^\dagger(-B)Xu$ with $u$ the mapped mode, and every one-body density gets one more sign: $(n,s,t,c)\to(-n,\,s,\,-t,\,-c)$ (check `PAIR_T3block_potentialsImageRule`). The potentials then match with $(m,\lambda)\to(-m,-\lambda)$: $-m+(1+\tfrac{\mathrm{sg}}{16})(-\lambda)S_p=-M_{\mathrm{eff}}$ and $\mathrm{sg}\tfrac{(-\lambda)}{16}(-n_p)=v$, while $E_H+E_x$ changes sign. The image has the same orbitals $\sigma_y\chi$, the same levels and the same occupations, and all its one-body densities and energies, including $T_{\mu\nu}$, are those of the ordinary $-M$ run with the opposite sign: $E\to-E$ and $T_{\mu\nu}\to-T_{\mu\nu}$ (checks `PAIR_T3ks_imageRuleEnergyOdd`, `PAIR_T3emt_imageRuleMinusT`). This is T1 at the Kohn–Sham level. One formal feature deserves mention: the derivatives of the image's energy with respect to the occupations (Janak's theorem, Section 12.15) are $-\varepsilon$, and since $f(\varepsilon;\mu,T)=f(-\varepsilon;-\mu,-T)$ for the Fermi function, the image is a stationary state of its free energy at the formal temperature $-T$ and chemical potential $-\mu$, with $F_-(-T)=-F_+(T)$ (check `PAIR_T3ks_occupationsAndTemperature`). For the Krein image pair: $E^{\mathrm{pair}}=0$, charge 0, $T^{\mathrm{pair}}_{\mu\nu}=0$ at every point, $S^{\mathrm{pair}}=2S_+$ (check `PAIR_totals_ksKreinImagePair`).

**Summary of the four pairings.**

| pairing | map | partner | $T_{\mu\nu}$ | $Q$ | $S$ |
| --- | --- | --- | --- | --- | --- |
| T1, classical fields (Section 15.3) | $\Psi\to\gamma^8\Psi$ | $(-m,-\lambda)$ | $-T_{\mu\nu}$ | $-Q$ | $+S$ |
| T1, Krein image (Section 15.8) | $\chi\to\sigma_y\chi$, metric $-B$ | $(-m,-\lambda)$ | $-T_{\mu\nu}$ | $-Q$ | $+S$ |
| T2, mirror (Sections 15.5, 15.6) | $\Psi\to u\Psi$, reflected frame | $(-m,\lambda)$ | $+T_{\mu\nu}$, reflected | $+Q$ | $-S$ |
| T3, Kohn–Sham (Section 15.7) | $\chi\to\sigma_y\chi$, metric $+B$ | $(-m,\lambda)$, bag $\pi-\theta$ | $+T_{\mu\nu}$ | $+Q$ | $-S$ |

Only the pairs of the first two rows cancel. They need the coupling $-\lambda$ (or $\lambda=0$) and, for the quantum field, the reversed Krein metric of the second member.

### 15.9 When the boundary conditions are not transformed: the control

T3 needs the tip bag $\pi-\theta$ in the universe of mass $-M$. What happens if the $-M$ universe keeps the Stage-4 bag $\theta=0$ ($\chi_2(-L)=0$)? Write $P(m,\theta)$ for the Kohn–Sham problem with the bare mass $m$ and the tip bag angle $\theta$. By Theorem 15.13, $P(-m,\theta)$ is the image of $P(+m,\pi-\theta)$; so it is the image of $P(+m,\theta)$ only if the two bags give the same problem, which they do not for $\theta=0$, and the pairing fails. The exact theory makes this concrete at zero momentum, with a constant mass $M>0$ and no interaction (`pairing-theory.json`, key `T3.untransformedBCControl`). We derive the three differences.

**1. The zero mode moves to the tip.** With the mass $-M$ at $k=0$ and $\varepsilon=0$ the block equation reads $\chi_1'=-M\chi_1$, $\chi_2'=M\chi_2$. The parity-$+$ conditions $\chi_2(0)=\chi_2(-L)=0$ force $\chi_2\equiv0$, and then $\chi=(e^{-My},0)$: a zero mode that grows toward the tip $y=-L$, where the $+M$ zero mode $(e^{My},0)$ is smallest. The ratio of its density at the brane to that at the tip is $e^{-2ML}$, against $e^{+2ML}$ for $+M$ (check `PAIR_T3ks_zeroModeUntransformedControl`). With the transformed bag the $-M$ zero mode is $(0,e^{My})$, localized at the brane like the $+M$ one (check `PAIR_T3ks_zeroModeImage`).

**2. The brane band splits differently.** By the Hellmann–Feynman rule of Section 13.6, a zero mode $\chi$ moves at small $k$ as $\varepsilon\approx j\,c\,k$ with $c=\int\xi\,\chi^\dagger\sigma_z\chi\,dy\big/\int\chi^\dagger\chi\,dy$. For the tip zero mode $\chi^\dagger\sigma_z\chi=e^{-2My}$, and

$$
c_{\mathrm{ctrl}}=\frac{\int_{-L}^0e^{-Hy-a_{4,0}}e^{-2My}\,dy}{\int_{-L}^0e^{-2My}\,dy}=e^{-a_{4,0}}\,\frac{2M}{2M+H}\cdot\frac{e^{(2M+H)L}-1}{e^{2ML}-1},
$$

against $c(M)=e^{-a_{4,0}}\frac{2M}{2M-H}\cdot\frac{1-e^{-(2M-H)L}}{1-e^{-2ML}}$ for the paired problems (Section 13.6). For $M=H=1$, $a_{4,0}=0$ and $L=3$: $c=1.905148$ and $c_{\mathrm{ctrl}}=13.421975$. At $M=H$ the difference is $c_{\mathrm{ctrl}}-c=\tfrac23(Y-1)^2/(Y+1)>0$ with $Y=e^{HL}$ (Exercise 15.14; checks `PAIR_T3ks_controlSplittingClosedForm`, `PAIR_T3ks_controlDiffersFromPairedProblem`). The Rust solver measures the slopes $1.9051480$ (both paired universes) and $13.4219708$ (control) on its free spectra, against the closed forms $1.9051483$ and $13.4219752$ (`artifacts/dirac16complex/pair-creation/rust/pairs/free-section.json`, key `splitting`, relative differences $1.3\times10^{-7}$ and $3.3\times10^{-7}$).

**3. A bound state appears below the mass gap.** In the parity-$-$ sector ($\chi_1(0)=0$) with $\theta=0$ ($\chi_2(-L)=0$), eliminate $\chi_1$ as in Section 13.6: from $\chi_2'=-M_{\mathrm{eff}}\chi_2+ij\varepsilon\chi_1$ we get $\chi_1=(\chi_2'+M_{\mathrm{eff}}\chi_2)/(ij\varepsilon)$ and $\chi_2''=(M^2-\varepsilon^2)\chi_2$. The condition $\chi_1(0)=0$ becomes $\chi_2'(0)+M_{\mathrm{eff}}\chi_2(0)=0$. For $\varepsilon^2<M^2$ put $q=\sqrt{M^2-\varepsilon^2}$; the solution with $\chi_2(-L)=0$ is $\chi_2=\sinh(q(y+L))$, and the brane condition reads

$$
q\cosh(qL)+M_{\mathrm{eff}}\sinh(qL)=0 .
$$

For $M_{\mathrm{eff}}=+M$ both terms are positive and there is no solution: the $+M$ universe has no level with $|\varepsilon|<M$ in this sector (Section 13.6). For the control, $M_{\mathrm{eff}}=-M$, the condition is $\tanh(qL)=q/M$. The function $\tanh(qL)-q/M$ vanishes at $q=0$, has the slope $L-1/M$ there and is negative at $q=M$; since $\tanh$ is concave for positive arguments, there is exactly one root $q\in(0,M)$ when $ML>1$, and none when $ML\le1$. The level is

$$
\varepsilon_{\mathrm b}=\pm\sqrt{M^2-q^2}=\pm\frac{M}{\cosh(qL)}\approx\pm2M\,e^{-ML}\quad(ML\gg1),
$$

using $1-\tanh^2=1/\cosh^2$. For $M=1$, $L=3$: $q=0.9949015$ and $\varepsilon_{\mathrm b}=0.1008511214$ (Exercise 15.13); for $M=3$, $L=3$: $\varepsilon_{\mathrm b}=7.404590\times10^{-4}$. For $\varepsilon^2>M^2$ the same computation with $\sin$ gives the level conditions $p\cos(pL)\pm M\sin(pL)=0$ ($+$ for the paired universes, $-$ for the control), which have no common solution. (Checks `PAIR_T3ks_mixedSectorSolutions`, `PAIR_T3ks_controlMixedSectorLevelsDisjoint`, `PAIR_T3ks_controlSubGapBoundState`.)

**Consequence.** With the untransformed bag the spectra differ already at $k=0$, so the occupations, energies, densities and the energy–momentum tensor of the $-M$ universe differ from those of the $+M$ universe. The numerical control of Section 15.10 shows exactly this, and item 3 predicts its Kohn–Sham gap for $N=8$ to twelve digits.

### 15.10 The numerical demonstration

**What was planned.** The Stage-5 specification (§5, T4) asks for the Kohn–Sham ground and first excited states of the $+M$ universe, of the transformed $-M$ universe and of the untransformed control, for both fields, $m\in\{1,3\}$ ($H=1$), $L=3$, $N\in\{8,112\}$, $\hat\lambda\in\{0,\pm\hat\lambda_1,\pm\hat\lambda_2\}$ with the couplings of Section 13.10, at $T=0$ and at $T=0.1\,|m|$, computed by the Rust solver (its `pairs` subcommand, module `src/pairs.rs` of `studies/dirac16complex_kohn_sham`, described in the solver's `README.md`, section "Stage 5") and by the independent Python reference solver (`scripts/ks_reference_pairs.py` with `scripts/ks_reference_solver.py`), and compared by `scripts/check_dirac16complex_pairs.py`.

**What exists** (committed outputs, state of 2026-09-30):

- **Rust, dirac16complex only**, in `artifacts/dirac16complex/pair-creation/rust/pairs/`, one folder per configuration with a `pairing.json` (the comparison of the three universes) and the run files of each universe: $m=1$, $N=8$ for all five couplings at $T=0$; $m=1$, $N=112$ for all five couplings at $T=0$ and at $T=0.1$; $m=3$, $N=8$ for $\hat\lambda\in\{0,\pm\hat\lambda_1\}$ at $T=0$. The committed outputs stop before the remaining configurations ($m=3$, $N=112$; $m=3$, $N=8$ at $\pm\hat\lambda_2$; every dirac16complex00 configuration), and no summary file of the run is committed. The untransformed control was solved only at $\lambda=0$: for $\lambda\ne0$ its first self-consistent update violates the energy-window premise of the solver, because the tip-localized zero modes sit where the proper-density factor is $e^{6HL}\approx6.6\times10^7$ (`controlOutcome` in each `pairing.json`).
- **Reference solver**, in `artifacts/dirac16complex/pair-creation/reference/` with the summary `reference-pairs-summary.json`, which records itself as incomplete (`complete: false`, 131 runs pending): converged runs exist for $m=3$, $N=112$; for dirac16complex at $\lambda=0$ ($T=0$ and $T=0.1\,|m|$, all three universes) and at $\pm\hat\lambda_1$ ($T=0$, the $+M$ and $-M$ universes); for dirac16complex00 at $\lambda=0$ (both temperatures, all three universes) and the $+M$ universe alone at $+\hat\lambda_1$. The run at $+\hat\lambda_2$ did not converge (a collapse of the self-consistent loop was suspected), the interacting controls failed on the energy window, and the interacting runs at $T>0$ were not attempted.
- **Not done**: the cross-check report of `scripts/check_dirac16complex_pairs.py` (no report is committed), the Stage-5 gate, and any figure of the pairs. No numerical test of T3 exists for dirac16complex00 at $\lambda\ne0$, where its exchange sign matters; at $\lambda=0$ the two fields are the same problem.

Two identity checks were completed: the $+M$ universe of every $T=0$ Rust configuration reproduces the committed Stage-4 run bit for bit (`stage4Reproduction` in each `pairing.json`), and the Stage-4 outputs of the Rust solver are unchanged by the Stage-5 additions (all nine checks of `artifacts/dirac16complex/pair-creation/rust/stage4-identity-report.json` true).

**Rust results at $T=0$** (dirac16complex, $L=3$, $H=1$; energies in units of $H$, which is $m$ for $m=1$; the run label gives $m$, $N$ and $\hat\lambda/\hat\lambda_1$, where $\pm10$ means $\pm\hat\lambda_2$; numbers from the `pairing.json` of each configuration). The columns give the ground-state energy of the $+M$ universe, its difference from that of the transformed $-M$ universe, and the total scalar charges $S_{\mathrm{tot}}=\ell^3\int S_c\,dy$ of both:

| $m$, $N$, $\hat\lambda/\hat\lambda_1$ | $E_0(+M)$ | $\lvert E_0(+M)-E_0(-M)\rvert$ | $S_{\mathrm{tot}}(+M)$ | $S_{\mathrm{tot}}(-M)$ |
| --- | --- | --- | --- | --- |
| 1, 8, 0 | 0 | 0 | 0 | 0 |
| 1, 8, +1 | $-0.000986833163$ | $1.3\times10^{-12}$ | $+0.00790445514$ | $-0.00790445514$ |
| 1, 8, $-1$ | $+0.000986833163$ | $1.3\times10^{-12}$ | $-0.00790445514$ | $+0.00790445514$ |
| 1, 8, +10 | $-0.00783039195$ | $1.7\times10^{-10}$ | $+0.0506051452$ | $-0.0506051448$ |
| 1, 8, $-10$ | $+0.00783039195$ | $1.7\times10^{-10}$ | $-0.0506051452$ | $+0.0506051448$ |
| 1, 112, 0 | 61.0907233 | $7.3\times10^{-11}$ | $-20.853342$ | $+20.853342$ |
| 1, 112, +1 | 61.1132120 | $4.9\times10^{-10}$ | $-20.9453233$ | $+20.9453233$ |
| 1, 112, $-1$ | 61.0686105 | $1.2\times10^{-9}$ | $-20.7616373$ | $+20.7616373$ |
| 1, 112, +10 | 61.3283111 | $7.0\times10^{-9}$ | $-21.7686201$ | $+21.7686201$ |
| 1, 112, $-10$ | 60.8913051 | $8.1\times10^{-9}$ | $-20.0394132$ | $+20.0394132$ |
| 3, 8, 0 | 0 | 0 | 0 | 0 |
| 3, 8, +1 | $-1.19999991$ | $3.7\times10^{-12}$ | below $10^{-12}$ | below $10^{-12}$ |
| 3, 8, $-1$ | $+1.19999991$ | $3.7\times10^{-12}$ | below $10^{-12}$ | below $10^{-12}$ |

The $+M$ energies are the Stage-4 values of Section 13.11. For $m=3$, $N=8$ the eight occupied orbitals are zero modes with $\chi_2\equiv0$, whose scalar density vanishes (Section 13.11), so only the exchange potential acts. The first excited state:

| $m$, $N$, $\hat\lambda/\hat\lambda_1$ | $\Delta_{KS}(+M)$ | difference | $\Delta_{\mathrm{SCF}}(+M)$ | difference | largest $\lvert\Delta\varepsilon\rvert$ over all levels |
| --- | --- | --- | --- | --- | --- |
| 1, 8, 0 | 0.430733679 | $3.0\times10^{-12}$ | 0.430733679 | $3.0\times10^{-12}$ | $3.3\times10^{-10}$ |
| 1, 8, +1 | 0.430943911 | $4.3\times10^{-12}$ | 0.430938122 | $8.2\times10^{-12}$ | $2.9\times10^{-10}$ |
| 1, 8, $-1$ | 0.430515902 | $7.4\times10^{-12}$ | 0.430523397 | $2.6\times10^{-11}$ | $3.0\times10^{-10}$ |
| 1, 8, +10 | 0.431898697 | $5.9\times10^{-13}$ | 0.431945853 | $1.9\times10^{-10}$ | $4.9\times10^{-9}$ |
| 1, 8, $-10$ | 0.429137447 | $1.6\times10^{-11}$ | 0.429160673 | $1.0\times10^{-10}$ | $6.6\times10^{-9}$ |
| 1, 112, 0 | 0.0955462022 | $3.7\times10^{-12}$ | 0.0955462022 | $3.7\times10^{-12}$ | $3.3\times10^{-10}$ |
| 1, 112, +1 | 0.0954841338 | $9.5\times10^{-12}$ | 0.0954841923 | $9.4\times10^{-10}$ | $3.2\times10^{-10}$ |
| 1, 112, $-1$ | 0.0956051341 | $2.5\times10^{-11}$ | 0.0956050822 | $1.3\times10^{-9}$ | $3.1\times10^{-10}$ |
| 1, 112, +10 | 0.0948132008 | $6.2\times10^{-11}$ | 0.0948140420 | $2.0\times10^{-9}$ | $1.6\times10^{-9}$ |
| 1, 112, $-10$ | 0.0960101550 | $1.5\times10^{-11}$ | 0.0960098274 | $8.9\times10^{-10}$ | $3.8\times10^{-9}$ |
| 3, 8, 0 | 0.895832758 | $1.7\times10^{-11}$ | 0.895832758 | $1.7\times10^{-11}$ | $6.0\times10^{-10}$ |
| 3, 8, +1 | 0.895832758 | $5.6\times10^{-12}$ | 0.897264439 | $8.2\times10^{-10}$ | $6.4\times10^{-10}$ |
| 3, 8, $-1$ | 0.895832758 | $2.4\times10^{-12}$ | 0.894861136 | $4.6\times10^{-10}$ | $6.2\times10^{-10}$ |

In every configuration of this section, at $T=0$ and at $T=0.1\,m$, each level of the $+M$ universe (between 662 and 977 levels per configuration in the solver's energy window) has its partner under the map $(\text{shell},p,s,n)\to(\text{shell},-p,-s,-n)$ with no mismatch of multiplicity, the orbitals agree after the swap $(a,b)\to(b,a)$ to at most $1.5\times10^{-8}$, the profiles $n_c$, $n_p$, $v$, $\rho$, $p_y$, $p_3$, $p_t$ agree and $S_c$, $S_p$ are opposite to at most $2.0\times10^{-12}$ in the solver's normalized norms, and $M_{\mathrm{eff}}$ is opposite to at most $1.2\times10^{-7}$ relative (keys `pairingDeviation_plusM_vs_minusM` of the `pairing.json` files).

**Rust results at $T=0.1\,m$** ($m=1$, $N=112$): the Mermin states of Section 13.13 and their partners.

| $\hat\lambda/\hat\lambda_1$ | $E$ | $F$ | $S_{\mathrm{ent}}$ | $\mu$ | largest difference of these four |
| --- | --- | --- | --- | --- | --- |
| 0 | 69.5093780 | 53.9716429 | 155.377351 | 0.697334281 | $1.7\times10^{-9}$ |
| +1 | 69.5379866 | 53.9885813 | 155.494053 | 0.697612981 | $1.6\times10^{-9}$ |
| $-1$ | 69.4815823 | 53.9546932 | 155.268891 | 0.697058519 | $6.9\times10^{-10}$ |
| +10 | 69.8065526 | 54.1412640 | 156.652886 | 0.700242844 | $1.5\times10^{-8}$ |
| $-10$ | 69.2714394 | 53.8109715 | 154.604679 | 0.694812714 | $1.5\times10^{-8}$ |

The row $\lambda=0$ is the Stage-4 thermodynamics of Section 13.13 ($E=69.50938$, $F=53.97164$).

**How good is the agreement?** The pairing holds, level by level, to between $10^{-12}$ and $10^{-8}$. That is the precision of the solver itself: its tolerances are $10^{-12}$ (relative) and $10^{-14}$ (absolute) in the integration and $10^{-10}$ in the self-consistent loop (`parameters` of each `run.json`), and the Stage-4 refined-tolerance run changes energies by up to $5.96\times10^{-8}$ relative (Section 13.10). The two universes are computed as independent problems, with different boundary conditions and different signs of the mass, so this agreement is a genuine numerical test of Theorem 15.13, not a copy.

**The pair totals.** Each `pairing.json` also forms the two pair totals of Section 15.8 from the two runs: the mirror pair ($+M$ plus $-M$) and the Krein image pair ($+M$ minus $-M$ for every one-body density and energy). For $m=1$, $N=112$, $+\hat\lambda_2$, $T=0$:

| quantity | mirror pair, $(+M)+(-M)$ | Krein image pair, $(+M)-(-M)$ |
| --- | --- | --- |
| energy $E$ | 122.6566221 | $-7.0\times10^{-9}$ |
| charge (number of quanta) | 224 | 0 |
| total scalar charge $S_{\mathrm{tot}}$ | $-5.3\times10^{-9}$ | $-43.5372402$ |
| $\langle\rho\rangle$ | 0.0463577818 | $-2.7\times10^{-12}$ |
| $\langle p_y\rangle$ | 0.0220049755 | $-2.6\times10^{-13}$ |
| $\langle p_3\rangle$ | 0.0137914530 | $-1.8\times10^{-13}$ |

The mirror pair has twice the energy, charge and pressures of one universe and zero scalar charge; the Krein image pair has zero energy, charge and pressures and twice the scalar charge, $2\times(-21.7686201)$. Both are what Sections 15.7 and 15.8 predict.

**The untransformed control** (the $-M$ universe with the Stage-4 bag $\theta=0$), at $\lambda=0$:

| configuration | quantity | $+M$ universe | $-M$, transformed | $-M$, untransformed |
| --- | --- | --- | --- | --- |
| $m=1$, $N=8$, $T=0$ | $\Delta_{KS}$ | 0.4307336786 | 0.4307336786 | 0.1008511214 |
| $m=3$, $N=8$, $T=0$ | $\Delta_{KS}$ | 0.8958327583 | 0.8958327583 | 0.0007404590 |
| $m=1$, $N=112$, $T=0$ | $E_0$ | 61.0907233 | 61.0907233 | 56.2654962 |
| $m=1$, $N=112$, $T=0.1$ | $F$ | 53.9716429 | 53.9716429 | 49.2723994 |

The control does not pair. For $N=8$ its eight occupied orbitals are the tip zero modes at $\varepsilon=0$, and its lowest excitation goes to the sub-gap bound state of Section 15.9: the Rust gaps $0.10085112137571$ ($m=1$) and $0.00074045901682$ ($m=3$) agree with $\varepsilon_{\mathrm b}=M/\cosh(qL)=0.10085112137514$ and $0.00074045901623$ to $6\times10^{-13}$. For $N=112$ the control's ground state is a different state altogether, $4.8\,m$ lower in energy, in which a level of 32 states at the Fermi level is filled to three quarters, so that its Kohn–Sham gap is 0 (`rust/pairs/d16c_m1_L3_N112_lam0_T0/minusM_control/levels.csv`, column `f`).

**The reference solver** ($m=3$, $N=112$, $L=3$, $H=1$; grids $N_0=120$, 240, 480 with the extrapolation of the reference solver; `reference-pairs-summary.json`):

| $\hat\lambda/\hat\lambda_1$, $T$ | $E(+M)$ | $E(-M)$ | $S_{\mathrm{tot}}(+M)$ | $S_{\mathrm{tot}}(-M)$ |
| --- | --- | --- | --- | --- |
| 0, 0 | 131.448298 | 131.448295 | $-7.206331$ | $+7.206334$ |
| 0, 0.3 | 161.026343 | 161.026341 | $-7.971180$ | $+7.971183$ |
| +1, 0 | 127.409033 | 127.409029 | $-8.466395$ | $+8.466399$ |
| $-1$, 0 | 135.701559 | 135.701558 | $-6.388991$ | $+6.388992$ |

These are dirac16complex runs; $T=0.3$ is $T=0.1\,|m|$, where the free energies are $104.727753$ and $104.727750$. The Kohn–Sham gaps of the two universes are

| $\hat\lambda/\hat\lambda_1$, $T$ | $\Delta_{KS}(+M)$ | $\Delta_{KS}(-M)$ |
| --- | --- | --- |
| 0, 0 | 0.2342637881 | 0.2342637838 |
| 0, 0.3 | 0.2794285932 | 0.2794285878 |
| +1, 0 | 0.2350337045 | 0.2350336992 |
| $-1$, 0 | 0.2336532576 | 0.2336532545 |

The dirac16complex00 runs at $\lambda=0$ give the same numbers to all digits, as they must, since the statistics enters only through the exchange term, which is proportional to $\lambda$. The reference controls at $\lambda=0$ give $E_0=119.118131$ at $T=0$ and $F=93.121665$ at $T=0.3$, far from the paired values. The pairing defect of the reference solver, about $3\times10^{-6}$ in $E$, is much larger than that of the Rust solver. This too was predicted (`pairing-theory.json`, `T3.numericsPrescription.discretisationNote`): the reference solver puts the two components of $\chi$ on two staggered grids, and the swap $\chi\to\sigma_y\chi$ exchanges the roles of the two grids, so the two universes are discretized differently and pair only up to the discretization error. Both values agree with the Stage-4 Rust energy $131.4482953$ of the same $+M$ problem (`artifacts/dirac16complex/kohn-sham/rust/scf/m3_L3_N112_lam0_T0/run.json`) to within $3\times10^{-6}$.

**Reproduction.** The exact verifier and the independent checker run from the repository root; written into `build/`, they leave the committed reports untouched. In Git Bash:

```
export PYTHONUTF8=1
wolframscript -file scripts/verify_dirac16complex_pairing.wls \
    build/pairing/wolfram-pairing-report.json
python scripts/check_dirac16complex_pairing.py \
    --output build/pairing/python-pairing-report.json
```

In PowerShell set `$env:PYTHONUTF8 = "1"` and replace each line-ending backslash by a backtick. Each program prints one line per check and ends with the lines `check_count` and `failed_check_count`. For the Kohn–Sham pair runs, the solver's `README.md` (section "Stage 5") gives the Rust command, and the reference script takes an output folder; in Git Bash, writing into `build/` (the Rust subcommand writes into the subfolder `pairs/` of the folder given):

```
cargo build --release --manifest-path studies/dirac16complex_kohn_sham/Cargo.toml
./studies/dirac16complex_kohn_sham/target/release/dirac16complex_kohn_sham \
    pairs --output build/pairs-rust
python scripts/ks_reference_pairs.py --output build/pairs-reference
```

Section 19.10 records which of these runs are committed.

### 15.11 What the pairing theorems establish, and what they do not

**Established (proved, with exact machine checks):**

- For both fields and in every gravitational field, the chirality map sends the theory $(m,\lambda)$ to the theory $(-m,-\lambda)$, whose action is minus the original one, and every configuration to a configuration; energy–momentum and charge change sign (T1).
- A T1 pair has zero total energy–momentum, charge and action at every point and every time, so the gravitational field equations with the pair as source are the source-free equations; its appearance from the empty state violates no conservation law and no constraint (Corollary 15.4). For the quantum field this requires the second member to be the image field with the reversed Krein metric $-B$.
- A reflection of a space-like direction, acting on the field and the frame, sends $(m,\lambda)$ to $(-m,\lambda)$ with the same energy–momentum and charge (T2); across the Z2 brane of the static primordial field this is the mirror universe of mass $-M$, and every Stage-4 Kohn–Sham state is such a mirror pair.
- In the Kohn–Sham model of Chapters 13 and 14, for both statistics, the universe of mass $-M$ with the same $\lambda$ and the transformed tip condition has exactly the same ground state, first excited state, thermodynamics and energy–momentum tensor as the universe of mass $+M$, and the opposite scalar density (T3); with the untransformed tip condition the pairing fails.

**Computed:** the Rust and reference results of Section 15.10, which confirm T3 to the precision of each solver for dirac16complex in the configurations listed there, and confirm the failure of the untransformed control.

**Not established:**

- No process that creates a pair is derived: no rate, probability or amplitude, no wave function of the universe, no dynamical big bang. The theorems show consistency with conservation laws and constraints, not occurrence.
- The cancelling (T1) pair needs the coupling $-\lambda$ (or $\lambda=0$) for the second member and, for the quantum field, the reversed Krein metric. Nothing in the theory selects this pair over the mirror pair of T2 and T3, whose energy doubles.
- The Kohn–Sham statements concern a mean-field model (no correlation, fixed metric, the good sector); for dirac16complex00 the model is a formal functional with Pauli filling imposed by prescription.
- The numerical demonstration is incomplete (Section 15.10): no Rust run of dirac16complex00, no run with $m=3$, $N=112$ in Rust, no cross-check report and no Stage-5 gate.
- The primordial field still requires a negative energy density in Einstein gravity; the pairing does not supply it.

Whether the big bang creates universes in pairs is therefore **not** answered by these theorems; it remains the notebook's hypothesis, and Chapter 16 discusses it. What the opposite charges of a T1 pair mean for the matter–antimatter asymmetry is the subject of Chapter 17.

### 15.12 What we proved and what we assumed

**What we proved.** With complete derivations in this chapter: how a constant matrix passes through a bilinear, for commuting and for Grassmann components (Lemma 15.1); the parity of products of gammas under $\gamma^8$ and the fact that $\gamma^8$ reverses $B$ (Lemma 15.2, fact (F6)); Theorem T1 in every gravitational field, for both statistics, with the Lagrangian, field equations, energy–momentum tensor and current (Theorem 15.3), the failure at fixed $\lambda$, the equivalence with a reversal of the frame, and the fact that the partner theory has the negated action; the vanishing totals of the chiral pair and the source-free gravitational equations (Corollary 15.4); the anticommutator $-B$ of the image field; Theorem T2 for every unit vector in every gravitational field, with the reflected frame built from the covariance theorem of Section 4.12 (Theorem 15.5); its explicit form across the Z2 brane, the pull-back of the energy–momentum tensor and the current, and the odd mass function of a Z2-symmetric configuration (Lemma 15.6, Theorem 15.7, Corollary 15.8); the block form $\tau\,\sigma_y$ of $\gamma^8$ (Lemma 15.9), the map $\sigma_yh_j(M,v)\sigma_y=h_{-j}(-M,v)$ (Lemma 15.10), the transformation of the parity and bag conditions (Lemma 15.11) and of the densities (Lemma 15.12); Theorem T3 for both statistics (Theorem 15.13) and its Krein-image form with $-\lambda$; the explanation of the difference between T1 and T3 by the parity of $B$; and, for the untransformed control, the tip zero mode, the splitting constant $c_{\mathrm{ctrl}}$ and the sub-gap bound state with $\tanh(qL)=q/M$.

**What we took from elsewhere.** The algebra of the gammas, $C$, $B$, the Pin group and its reflections (Chapter 2); the vielbein, the spin connection and the covariance theorem (Chapter 4); the Lagrangian, field equations and energy–momentum tensor (Chapters 6 and 7); the canonical anticommutator, the positive Fock space and the expectation-value rule (Chapter 8); the static primordial field and the Z2 gluing (Chapter 9); the block reduction, boundary conditions, densities, Kohn–Sham functional and energy–momentum formulas (Chapter 13) and the statistics sign of the exchange (Chapter 14); the Fock-level model of the image field and the numbers of the one-particle table, from the Stage-5 and matter–antimatter reports; the uniqueness theorem of Picard and Lindelöf (Chapter 10). The exact checks at test points confirm the general derivations; they do not replace them.

**What we assumed.** The Z2 gluing of the primordial field is a choice of model (Section 9.16). The Kohn–Sham model is an approximation with the assumptions listed after Theorem 15.13, and for dirac16complex00 it is defined by prescription. That the two members of a T1 pair live on one spacetime and that their totals add is hypothesis (a) to (c) of Corollary 15.4. Which of the pairings, if any, describes the notebook's "pair of universes" is not decided by the equations; it is an interpretation, and no statement of this chapter makes it.

### 15.13 Exercises

**Exercise 15.1.** Decide whether $\gamma^8X\gamma^8=+X$ or $-X$ for $X=C$, $C\gamma^3$, $C\gamma^0\gamma^1$, $B$, $BC$, $BC\gamma^1$ and $\gamma^0\gamma^4$.

**Exercise 15.2.** Show that $E_{m,\lambda}[\gamma^8\Psi]=-\gamma^8E_{m,\lambda}[\Psi]-2(m+\lambda S)\gamma^8\Psi$. Conclude that the image of a solution with $(m,\lambda)$ is not a solution with $(m,\lambda)$ wherever $\Psi\ne0$ and $m+\lambda S\ne0$.

**Exercise 15.3.** In flat space and Gaussian normal gauge, the Lagrangian $\mathcal L_{m,\lambda}$ has, after a total derivative, the form $\Psi^\dagger K\partial_4\Psi-\mathcal H$ with $K=C\gamma^4$ (Section 8.5). Use the rule $\{\Psi,\Psi^\dagger\}=iK^{-1}\delta^7$ of Section 8.6 to find the anticommutator of the Lagrangian $-\mathcal L_{-m,-\lambda}$, and compare it with $\{\gamma^8\Psi,(\gamma^8\Psi)^\dagger\}$ computed from $\{\Psi,\Psi^\dagger\}=B\,\delta^7$.

**Exercise 15.4.** Let $\tilde u=\gamma^8u_+=\tfrac12(-e_0+e_4-ie_9-ie_{13})$. With the rows of $\gamma^4$, $C$ and $B$ quoted in Section 15.3, show $-i\gamma^4\tilde u=-\tilde u$, $C\tilde u=\tilde u$ and $B\tilde u=-\tilde u$, and recompute the table of Section 15.8.

**Exercise 15.5.** For a time-like unit vector $u$ ($n(u)=-1$) go through the proof of Theorem 15.5 and show $\mathcal L_{m,\lambda}[e_u,u\Psi]=-\mathcal L_{-m,-\lambda}[e,\Psi]$. Then compute $uBu^\dagger$ for $u=\gamma^4$ and for $u=\gamma^5$.

**Exercise 15.6.** Show that $S^{0p}\gamma^0=-\gamma^0S^{0p}$ for $p\ne0$, and that the coefficient $c_l=-W'e^{a_{4,0}}$ of $\Omega_l$ is odd in $y$ for $W=e^{-H|y|}$. Deduce $D_l\Psi'(y)=\gamma^0(D_l\Psi)(-y)$ for $\Psi'(y)=\gamma^0\Psi(-y)$.

**Exercise 15.7.** Check that $\chi(y)=(e^{-M|y|},0)$ solves the block equation of Section 13.5 at $k=0$, $\varepsilon=0$, $v=0$ on both sides of the brane with the mass function $M(y)=-M\,\mathrm{sgn}(y)$, that it satisfies $\chi(y)=\sigma_z\chi(-y)$, and that its number density is even in $y$.

**Exercise 15.8.** Using only $\sigma_a\sigma_b=-\sigma_b\sigma_a$ ($a\ne b$) and $\sigma_a^2=1$, show $\sigma_y\sigma_x\sigma_y=-\sigma_x$ and $\sigma_y\sigma_z\sigma_y=-\sigma_z$, and verify $\sigma_yh_j(M,v)\sigma_y=h_{-j}(-M,v)$ term by term.

**Exercise 15.9.** Show $\sigma_yQ(\theta)\sigma_y=Q(\pi-\theta)$. Write the bag conditions for $\theta=0$, $\theta=\pi$ and $\theta=\pi/2$ in components, and say which of them the map sends into which.

**Exercise 15.10.** With the vectors $v_\pm$ and $w_\pm$ of Section 15.7, verify $\gamma^8v_+=i\,w_-$ and $\gamma^8v_-=-i\,w_+$ (up to the common factor $1/\sqrt8$), and write the $2\times2$ matrix $G$ of Lemma 15.9.

**Exercise 15.11.** (a) Transform $(n,s,t,c)$ with the image rule, in which the metric is $-B$. (b) For dirac16complex00 ($M_{\mathrm{eff}}=m+\tfrac{17}{16}\lambda S_p$, $v=\tfrac{\lambda}{16}n_p$) check that the ordinary map needs $(m,\lambda)\to(-m,\lambda)$ and the image map $(m,\lambda)\to(-m,-\lambda)$.

**Exercise 15.12.** At $\lambda=0$ and $k=0$ the level $\varepsilon=\sqrt{M^2+(\pi/L)^2}$ of parity $+$ has the scalar charge $\int\chi^\dagger j\sigma_y\chi\,dy=d\varepsilon/dM$ (Section 13.9). Show that the image level in the $-M$ problem has the opposite scalar charge, in agreement with Lemma 15.12, and evaluate both for $M=1$, $L=3$.

**Exercise 15.13.** For the control with $M=1$, $L=3$: bracket the root of $f(q)=\tanh(3q)-q$ in $(0.9,1)$, halve the bracket six times, and compute $\varepsilon_{\mathrm b}=1/\cosh(3q)$. Compare with the Rust gap $0.1008511214$ of the control of Section 15.10. Estimate $\varepsilon_{\mathrm b}$ for $M=3$, $L=3$ with the formula $2Me^{-ML}$.

**Exercise 15.14.** Show that at $M=H$ and $a_{4,0}=0$, $c(M)=2Y/(Y+1)$ and $c_{\mathrm{ctrl}}=\tfrac23(Y^2+Y+1)/(Y+1)$ with $Y=e^{HL}$, hence $c_{\mathrm{ctrl}}-c=\tfrac23(Y-1)^2/(Y+1)$. Evaluate for $L=3$.

**Exercise 15.15.** From the tables of Section 15.10 compute, for $m=1$, $N=112$, $+\hat\lambda_2$, $T=0$, the energies and total scalar charges of the mirror pair and of the Krein image pair, and compare with the pair table. Which pair cancels, and which quantity doubles in each?

**Exercise 15.16.** Show that $P_B=i\gamma^0\gamma^8$ is Hermitian with $P_B^2=1$, that $P_BCP_B=-C$, $P_BBP_B=-B$ and therefore $P_B(BC)P_B=BC$. Explain why $P_B$ reverses $\lambda$ for the classical field but keeps it in the Kohn–Sham model.

### 15.14 Answers to the exercises

**Answer 15.1.** Count the gamma factors (Lemma 15.2): $C$ has 4, even, $+C$; $C\gamma^3$ has 5, odd, $-X$; $C\gamma^0\gamma^1$ has 6, even, $+X$; $B$ has 5, odd, $-B$; $BC$ has 9, odd, $-BC$ (equivalently $BC=-i\gamma^4$ has 1); $BC\gamma^1$ has 10, even, $+X$; $\gamma^0\gamma^4$ has 2, even, $+X$.

**Answer 15.2.** $E_{m,\lambda}[\Phi]-E_{-m,-\lambda}[\Phi]=-(m+\lambda S)\Phi-(m+\lambda S)\Phi=-2(m+\lambda S)\Phi$ for any $\Phi$, because the two expressions differ only in the sign of $m+\lambda S$ and $S[\gamma^8\Psi]=S[\Psi]$. With $\Phi=\gamma^8\Psi$ and item 4 of Theorem 15.3, $E_{m,\lambda}[\gamma^8\Psi]=-\gamma^8E_{m,\lambda}[\Psi]-2(m+\lambda S)\gamma^8\Psi$. If $\Psi$ solves $E_{m,\lambda}=0$, what remains is $-2(m+\lambda S)\gamma^8\Psi$, which vanishes only where $(m+\lambda S)\Psi=0$, since $\gamma^8$ is invertible.

**Answer 15.3.** For $\mathcal L_{m,\lambda}$, $K=C\gamma^4$. Since $\gamma^4$ commutes with $C$, $(C\gamma^4)(-\gamma^4C)=-C(\gamma^4)^2C=C^2=1$, so $K^{-1}=-\gamma^4C=-C\gamma^4$ (Section 8.5 with $g^{44}=-1$) and $iK^{-1}=-iC\gamma^4=B$. For $-\mathcal L_{-m,-\lambda}$ the kinetic term does not depend on $m$ or $\lambda$, and the overall sign gives $K=-C\gamma^4$, hence $iK^{-1}=-B$. On the other hand $\{\gamma^8\Psi,(\gamma^8\Psi)^\dagger\}=\gamma^8\{\Psi,\Psi^\dagger\}\gamma^8=\gamma^8B\gamma^8\,\delta^7=-B\,\delta^7$. The two agree: the image field is canonically a field of $-\mathcal L_{-m,-\lambda}$.

**Answer 15.4.** The components of $\tilde u$ are $u_0=-\tfrac12$, $u_4=\tfrac12$, $u_9=-\tfrac i2$, $u_{13}=-\tfrac i2$. $(\gamma^4u)_0=-u_{13}=\tfrac i2$, so $(-i\gamma^4u)_0=\tfrac12=-u_0$; $(\gamma^4u)_4=u_9=-\tfrac i2$, so $(-i\gamma^4u)_4=-\tfrac12=-u_4$; $(\gamma^4u)_9=-u_4=-\tfrac12$, so $(-i\gamma^4u)_9=\tfrac i2=-u_9$; $(\gamma^4u)_{13}=u_0=-\tfrac12$, so $(-i\gamma^4u)_{13}=\tfrac i2=-u_{13}$. Hence $-i\gamma^4\tilde u=-\tilde u$. $(Cu)_0=-u_4=-\tfrac12=u_0$, $(Cu)_4=-u_0=\tfrac12=u_4$, $(Cu)_9=u_{13}=u_9$, $(Cu)_{13}=u_9=u_{13}$: $C\tilde u=\tilde u$. $(Bu)_0=iu_9=\tfrac12=-u_0$, $(Bu)_4=-iu_{13}=-\tfrac12=-u_4$, $(Bu)_9=-iu_0=\tfrac i2=-u_9$, $(Bu)_{13}=iu_4=\tfrac i2=-u_{13}$: $B\tilde u=-\tilde u$. Since $\tilde u^\dagger \tilde u=4\cdot\tfrac14=1$: classically $\tilde u^\dagger B\tilde u=-1$, $\tilde u^\dagger C\tilde u=1$, energy $m\cdot(-1)=-m$. With the rule and $+B$: charge $u^\dagger B^2u=1$, scalar $u^\dagger(-i\gamma^4)u=-1$, energy $u^\dagger h(-m)u=u^\dagger(im\gamma^4)u=-m\,u^\dagger(-i\gamma^4)u=m$. With $-B$ every rule value changes sign: $-1$, $+1$, $-m$. For $u_+$ the values of Section 8.8 ($-i\gamma^4u_+=u_+$, $Cu_+=u_+$, $Bu_+=u_+$) give 1, 1 and $m$ in both columns.

**Answer 15.5.** With $n=-1$: $\bar\Psi_u=+\bar\Psi u^{-1}$, so $S\to S$; the kinetic bilinear becomes $(\bar\Psi u^{-1})(-u\gamma^\mu u^{-1})(uD_\mu\Psi)=-\bar\Psi\gamma^\mu D_\mu\Psi$, so $K\to-K$. Then $\mathcal L\to\sqrt{|g|}[-K-mS-\tfrac\lambda2S^2]=-\mathcal L_{-m,-\lambda}$. For $u=\gamma^4$: $u^\dagger=(\gamma^4)^T=-\gamma^4$, and $\gamma^4B(-\gamma^4)=i\gamma^4C\gamma^4\gamma^4=-i\gamma^4C=-iC\gamma^4=B$ (since $\gamma^4$ commutes with $C$). For $u=\gamma^5$: $u^\dagger=-\gamma^5$, and $\gamma^5B(-\gamma^5)=i\gamma^5C\gamma^4\gamma^5=iC\gamma^5\gamma^4\gamma^5=-iC\gamma^4(\gamma^5)^2=iC\gamma^4=-B$ (here $\gamma^5$ commutes with $C$ and anticommutes with $\gamma^4$).

**Answer 15.6.** For $p\ne0$, $S^{0p}=\tfrac12\gamma^0\gamma^p$, so $S^{0p}\gamma^0=\tfrac12\gamma^0\gamma^p\gamma^0=-\tfrac12\gamma^0\gamma^0\gamma^p=-\tfrac12\gamma^p$ and $\gamma^0S^{0p}=\tfrac12\gamma^0\gamma^0\gamma^p=\tfrac12\gamma^p$: they are opposite. $W=e^{-H|y|}$ is even, so $W'(-y)=-W'(y)$ and $c_l(-y)=-c_l(y)$. Then $D_l[\gamma^0\Psi(-y)]=\gamma^0(\partial_l\Psi)(-y)+c_l(y)S^{0l}\gamma^0\Psi(-y)=\gamma^0(\partial_l\Psi)(-y)-c_l(y)\gamma^0S^{0l}\Psi(-y)=\gamma^0\bigl[\partial_l\Psi+c_l(-y)S^{0l}\Psi\bigr](-y)=\gamma^0(D_l\Psi)(-y)$.

**Answer 15.7.** At $k=0$, $\varepsilon=v=0$ the block equation is $\chi_1'=M(y)\chi_1$, $\chi_2'=-M(y)\chi_2$. With $\chi_2=0$ and $\chi_1=e^{-M|y|}$: for $y<0$, $\chi_1=e^{My}$ and $\chi_1'=M\chi_1$ with $M(y)=+M$; for $y>0$, $\chi_1=e^{-My}$ and $\chi_1'=-M\chi_1$ with $M(y)=-M$. So $M(y)=-M\,\mathrm{sgn}(y)$, an odd function. $\sigma_z\chi(-y)=(e^{-M|y|},0)=\chi(y)$. The density $\chi^\dagger\chi=e^{-2M|y|}$ is even, and the scalar density $j\chi^\dagger\sigma_y\chi=0$ because $\chi_2=0$.

**Answer 15.8.** $\sigma_y\sigma_x\sigma_y=-\sigma_x\sigma_y\sigma_y=-\sigma_x$ and $\sigma_y\sigma_z\sigma_y=-\sigma_z\sigma_y\sigma_y=-\sigma_z$. Term by term, with the constant $\sigma_y$ commuting with $d/dy$:

$$
\begin{aligned}
&\sigma_y\bigl(-ij\sigma_x\tfrac{d}{dy}\bigr)\sigma_y=+ij\sigma_x\tfrac{d}{dy}=-i(-j)\sigma_x\tfrac{d}{dy},\qquad \sigma_y\bigl(jM\sigma_y\bigr)\sigma_y=jM\sigma_y=(-j)(-M)\sigma_y,\\
&\sigma_y\bigl(j\xi k\sigma_z\bigr)\sigma_y=-j\xi k\sigma_z=(-j)\xi k\sigma_z,\qquad \sigma_yv\sigma_y=v .
\end{aligned}
$$

Together these are the four terms of $h_{-j}(-M,v)$.

**Answer 15.9.** $\sigma_yQ(\theta)\sigma_y=\cos\theta\,(-\sigma_z)+\sin\theta\,\sigma_y=\cos(\pi-\theta)\sigma_z+\sin(\pi-\theta)\sigma_y$. $\theta=0$: $Q=\sigma_z$, $(1-\sigma_z)\chi=(0,2\chi_2)$, the condition $\chi_2(-L)=0$. $\theta=\pi$: $Q=-\sigma_z$, the condition $\chi_1(-L)=0$. $\theta=\pi/2$: $Q=\sigma_y$, $(1-\sigma_y)\chi=(\chi_1+i\chi_2,\ \chi_2-i\chi_1)=0$, that is $\chi_1=-i\chi_2$. The map sends $\theta=0$ to $\pi$, $\pi$ to $0$, and $\pi/2$ to itself.

**Answer 15.10.** $\gamma^8$ multiplies the components 0 to 7 by $-1$. Multiply every vector by $\sqrt8$. The nonzero components of $\sqrt8\,w_-$ are $(i,-1,-i,-1)$ in places 4 to 7 and $(-i,1,i,1)$ in places 12 to 15; times $i$ they become $(-1,-i,1,-i)$ and $(1,i,-1,i)$. The nonzero components of $\sqrt8\,v_+$ are $(1,i,-1,i)$ in places 4 to 7 and the same in places 12 to 15; $\gamma^8$ turns the first group into $(-1,-i,1,-i)$ and keeps the second. So $\gamma^8v_+=i\,w_-$. In the same way $\sqrt8\,v_-$ has $(i,-1,-i,-1)$ in places 0 to 3 and $(-i,1,i,1)$ in places 8 to 11; $\gamma^8$ gives $(-i,1,i,1)$ and $(-i,1,i,1)$; and $-i$ times $\sqrt8\,w_+$, which has $(1,i,-1,i)$ in both groups, is $(-i,1,i,1)$ in both groups. So $\gamma^8v_-=-i\,w_+$. Hence $\gamma^8[v_+\ v_-]=[w_+\ w_-]\,G$ with

$$
G=\begin{pmatrix}0&-i\\ i&0\end{pmatrix}=\sigma_y :
$$

the first column of $G$ holds the coefficients $(0,i)$ of the image of $v_+$, the second those of $v_-$, $(-i,0)$.

**Answer 15.11.** (a) With $-B$ each expectation value gets one more sign: $(n,s,t,c)\to(-n,\,s,\,-t,\,-c)$. (b) Ordinary map, $(n_p,S_p)\to(n_p,-S_p)$: $m'+\tfrac{17}{16}\lambda'(-S_p)$ must equal $-m-\tfrac{17}{16}\lambda S_p$ for all $S_p$, so $m'=-m$ and $\lambda'=\lambda$; then $v'=\tfrac{\lambda}{16}n_p=v$, as Lemma 15.10 requires. Image map, $(n_p,S_p)\to(-n_p,S_p)$: $m'+\tfrac{17}{16}\lambda'S_p=-m-\tfrac{17}{16}\lambda S_p$ gives $m'=-m$ and $\lambda'=-\lambda$, and then $v'=\tfrac{-\lambda}{16}(-n_p)=v$. The same holds with $\tfrac{15}{16}$ and $-\tfrac{1}{16}$ for dirac16complex.

**Answer 15.12.** For the $+M$ problem $\varepsilon=\sqrt{M^2+q^2}$ with $q=\pi/L$, so $d\varepsilon/dM=M/\varepsilon$. The $-M$ problem has the mass $M'=-M$ and the same level $\varepsilon=\sqrt{M'^2+q^2}$ (Lemma 15.10 and check `PAIR_T3ks_massiveLevelsMap`), so its scalar charge is $d\varepsilon/dM'=M'/\varepsilon=-M/\varepsilon$: opposite, as Lemma 15.12 says. For $M=1$, $L=3$: $q=1.047198$, $\varepsilon=1.447972$ and the scalar charges are $\pm0.690621$.

**Answer 15.13.** $f(0.9)=+0.0910$ and $f(1)=-0.0049$, so a root lies in $(0.9,1)$. Halving: $f(0.95)=+0.0433$, bracket $(0.95,1)$; $f(0.975)=+0.0193$, $(0.975,1)$; $f(0.9875)=+0.0072$, $(0.9875,1)$; $f(0.99375)=+0.0011$, $(0.99375,1)$; $f(0.996875)=-0.0019$, $(0.99375,0.996875)$; $f(0.9953125)=-0.0004$, $(0.99375,0.9953125)$. Continuing gives $q=0.9949015$. Then $\cosh(3q)=\cosh(2.984705)=9.915606$ and $\varepsilon_{\mathrm b}=0.1008511$, the Rust gap $0.1008511214$ of the control to all digits shown. For $M=3$, $L=3$: $2Me^{-ML}=6e^{-9}=7.4046\times10^{-4}$, close to the exact $7.40459\times10^{-4}$ and to the Rust gap $0.0007404590$.

**Answer 15.14.** At $M=H=1$: $c=\frac{2}{1}\cdot\frac{1-e^{-L}}{1-e^{-2L}}=\frac{2}{1+e^{-L}}=\frac{2Y}{Y+1}$, and $c_{\mathrm{ctrl}}=\frac23\cdot\frac{e^{3L}-1}{e^{2L}-1}=\frac23\cdot\frac{(Y-1)(Y^2+Y+1)}{(Y-1)(Y+1)}=\frac23\cdot\frac{Y^2+Y+1}{Y+1}$. The difference is $\frac{\frac23(Y^2+Y+1)-2Y}{Y+1}=\frac23\cdot\frac{Y^2-2Y+1}{Y+1}=\frac23\cdot\frac{(Y-1)^2}{Y+1}$, positive for $Y>1$. For $L=3$, $Y=20.085537$ and the difference is $11.516827=13.421975-1.905148$.

**Answer 15.15.** Mirror pair: $E=61.3283111+61.3283111=122.6566221$, charge $112+112=224$, $S_{\mathrm{tot}}=-21.7686201+21.7686201=0$ (the file gives $-5.3\times10^{-9}$). Krein image pair: the image has the $-M$ values with the opposite sign, so $E=61.3283111-61.3283111=0$ ($-7.0\times10^{-9}$ in the file), charge $112-112=0$, $S_{\mathrm{tot}}=-21.7686201-21.7686201=-43.5372402$. The Krein image pair cancels in energy, charge and pressures and doubles the scalar charge; the mirror pair doubles energy, charge and pressures and cancels the scalar charge.

**Answer 15.16.** $P_B^\dagger=-i\gamma^8\gamma^0=i\gamma^0\gamma^8=P_B$ (both factors are real symmetric and they anticommute), and $P_B^2=-\gamma^0\gamma^8\gamma^0\gamma^8=\gamma^0\gamma^0\gamma^8\gamma^8=1$. $P_BCP_B=-\gamma^0\gamma^8C\gamma^0\gamma^8=-\gamma^0C\gamma^8\gamma^0\gamma^8=\gamma^0C\gamma^0\gamma^8\gamma^8=\gamma^0C\gamma^0=-C$, because $C$ commutes with $\gamma^8$ and anticommutes with $\gamma^0$. $P_BBP_B$: $\gamma^0$ commutes with $B$ ($\gamma^0B\gamma^0=B$, Section 15.5) and $\gamma^8$ anticommutes with it (F6), so $P_BBP_B=-\gamma^0\gamma^8B\gamma^0\gamma^8=\gamma^0\gamma^8B\gamma^8\gamma^0=-\gamma^0B\gamma^0=-B$. Hence $P_B(BC)P_B=(P_BBP_B)(P_BCP_B)=(-B)(-C)=BC$. For the classical field, $P_B$ reverses the kinetic term (through its factor $\gamma^8$, as in T1) and the scalar density $\bar\Psi\Psi$, whose matrix $C$ is $P_B$-odd; so $\mathcal L_{m,\lambda}\to\sqrt{|g|}\,[-K+mS-\tfrac\lambda2S^2]=-\mathcal L_{m,-\lambda}$: the same mass, the opposite coupling. In the Kohn–Sham model the scalar density has the matrix $BC$, which $P_B$ keeps, and $P_B$ keeps the number-density matrix $B^2=1$ as well (check `PAIR_T2z2_ruleParities`); so the densities, the potentials and hence an even mass function with the same $\lambda$ are mapped onto themselves.
