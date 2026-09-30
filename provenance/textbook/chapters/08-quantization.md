## 8. Canonical quantization in 4+4 dimensions

### 8.1 What this chapter does

Chapters 6 and 7 treat dirac16complex as a classical field: a column $\Psi=(\Psi_0,\dots,\Psi_{15})^T$ of complex Grassmann-valued functions of the eight coordinates, with the Lagrangian

$$
\mathcal L=\sqrt{|g|}\,\Bigl[\tfrac12\bigl(\bar\Psi\gamma^\mu D_\mu\Psi-(D_\mu\bar\Psi)\gamma^\mu\Psi\bigr)-m\,\bar\Psi\Psi-U(\bar\Psi\Psi)\Bigr],\qquad \bar\Psi=\Psi^\dagger C,
$$

and the field equation $\gamma^\mu D_\mu\Psi=(m+U'(\bar\Psi\Psi))\Psi$. **Quantization** turns the components into operators acting on a space of states, with rules that make the classical equations come back as equations between operators. This chapter carries out the standard procedure, **canonical quantization with respect to the time** $x_4$, and finds three things that do not happen in ordinary four-dimensional physics:

1. the canonical anticommutator $\{\Psi,\Psi^\dagger\}$ is not a positive matrix but the matrix $B=-iC\gamma^4$, which has eight eigenvalues $+1$ and eight eigenvalues $-1$; so the natural space of states is a **Krein space**, a space with an inner product that is not positive, and this is forced by the signature (4,4) itself;
2. in the **good sector**, where nothing depends on the three extra times $x_5,x_6,x_7$, everything becomes ordinary again: there is a positive **Fock space** of particles and antiparticles and a Hamiltonian that is not negative;
3. a wave with momentum along an extra time has a non-Hermitian mode Hamiltonian, and it **grows** exponentially (or linearly in a borderline case) instead of oscillating.

The chapter follows §10 of the Stage-1 document `provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md` and its verification records (§11), §17 of the Stage-2 document `provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.md`, the erratum E1 of `handoff/specs/CONTRACT.md` (§11 there), and the experiment EXP-5 of `provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.md`. The quantization is **canonical and formal**: no interacting quantum theory, no regularization and no renormalization is constructed (Stage-1 document, §1.3, item 4). We use $\hbar=1$, count from 0, and take $x_4$ as the time.

### 8.2 States, operators and inner products

**States.** In quantum mechanics the state of a system is a vector $f$ in a complex vector space (Chapter 1). In the examples of this chapter the space is finite-dimensional, so a state is a column of complex numbers. An **inner product** assigns to two states the complex number $\langle f,h\rangle=f^\dagger h=\sum_if_i^\ast h_i$. It is **positive**: $\langle f,f\rangle=\sum_i|f_i|^2>0$ for every $f\ne0$. A complex vector space with a positive inner product is a **Hilbert space**. Its role is to give probabilities: for normalized states ($\langle f,f\rangle=1$) the number $|\langle f,h\rangle|^2$ is the probability of finding $h$ in the state $f$, and this needs positivity.

**Operators.** A (linear) **operator** is a rule that maps states to states; in finite dimensions it is a matrix. The **adjoint** $O^\dagger$ of an operator $O$ is defined by $\langle f,Oh\rangle=\langle O^\dagger f,h\rangle$ for all $f,h$; for the inner product above it is the conjugate transpose. An operator is **Hermitian** (self-adjoint) if $O^\dagger=O$. Then its eigenvalues are real and its **expectation values** $\langle f,Of\rangle$ are real; measurable quantities (energy, charge) are represented by Hermitian operators. An operator is **unitary** if $U^\dagger U=1$; unitary operators preserve inner products, and symmetries and time evolution are represented by them.

**Commutators.** For two operators, $[X,Y]=XY-YX$ is the **commutator** and $\{X,Y\}=XY+YX$ the **anticommutator**. We shall use the identity

$$
[XY,Z]=X\{Y,Z\}-\{X,Z\}Y,
$$

which one checks by multiplying out: $X(YZ+ZY)-(XZ+ZX)Y=XYZ-ZXY$.

**Time evolution.** The **Hamiltonian** $H$ is the Hermitian operator of the energy. States evolve by the **Schrödinger equation** $i\,df/dt=Hf$, whose solution is $f(t)=e^{-iHt}f(0)$ (the exponential of a matrix is its power series). Equivalently, one keeps the states fixed and lets the operators evolve, $O(t)=e^{iHt}Oe^{-iHt}$; differentiating gives the **Heisenberg equation**

$$
\frac{dO}{dt}=i\,[H,O].
$$

**Canonical quantization in one line.** For a particle with coordinate $q$ and momentum $p$ (Section 5.2) the classical **Poisson bracket** of two functions $F(q,p)$ and $G(q,p)$ is $\{F,G\}_{\mathrm P}=\frac{\partial F}{\partial q}\frac{\partial G}{\partial p}-\frac{\partial F}{\partial p}\frac{\partial G}{\partial q}$, so $\{q,p\}_{\mathrm P}=1$, and Hamilton's equations read $\dot F=\{F,H\}_{\mathrm P}$. The quantization rule is $[q,p]=i$: the Poisson bracket, times $i$, becomes the commutator, and $\dot F=\{F,H\}_{\mathrm P}$ becomes the Heisenberg equation. For fermions the commutator is replaced by the anticommutator. The next two sections show why this gives the Pauli principle.

### 8.3 One fermion mode: anticommutators and the Pauli principle

Let $b$ be an operator with

$$
\{b,b^\dagger\}=1,\qquad b^2=0,\qquad (b^\dagger)^2=0 .
$$

The **number operator** $N=b^\dagger b$ satisfies $N^2=b^\dagger bb^\dagger b=b^\dagger(1-b^\dagger b)b=b^\dagger b-(b^\dagger)^2b^2=N$. So every eigenvalue $n$ of $N$ satisfies $n^2=n$: $n=0$ or $n=1$. **A fermion mode is either empty or occupied once**; this is the Pauli principle, and it follows from the anticommutator alone.

**Worked example.** On the two states $|0\rangle=(1,0)^T$ (empty) and $|1\rangle=(0,1)^T$ (occupied) take

$$
b=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad b^\dagger=\begin{pmatrix}0&0\\1&0\end{pmatrix},\qquad bb^\dagger=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad b^\dagger b=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
$$

Then $bb^\dagger+b^\dagger b=1$, $b^2=0$, $b|1\rangle=|0\rangle$, $b|0\rangle=0$, $b^\dagger|0\rangle=|1\rangle$ and $b^\dagger|1\rangle=0$: $b$ **annihilates** a fermion and $b^\dagger$ **creates** one, and a second one cannot be created. With the Hamiltonian $H=\omega\,b^\dagger b$ the two states have the energies 0 and $\omega$.

**Where it comes from.** The complex Grassmann oscillator of Section 5.10, $L=\tfrac i2(\theta^\ast\dot\theta-\dot\theta^\ast\theta)-\omega\theta^\ast\theta$, is quantized exactly like this: its quantum version has $\{\theta,\theta^\dagger\}=1$ and $H=\omega\theta^\dagger\theta$ (Section 8.6 derives the rule in general). The classical Grassmann variable is the “shadow” of the anticommuting operator.

### 8.4 Many fermion modes: Fock space

With $n$ modes $b_0,\dots,b_{n-1}$ the rules are

$$
\{b_i,b_j^\dagger\}=\delta_{ij},\qquad \{b_i,b_j\}=0,\qquad \{b_i^\dagger,b_j^\dagger\}=0,
$$

where $\delta_{ij}$ is 1 for $i=j$ and 0 otherwise. A **vacuum** $|0\rangle$ is a normalized state with $b_i|0\rangle=0$ for all $i$. The states $b_{i_1}^\dagger b_{i_2}^\dagger\cdots b_{i_k}^\dagger|0\rangle$ with $i_1<i_2<\dots<i_k$ are the states with the modes $i_1,\dots,i_k$ occupied once each; there are $2^n$ of them, they are orthonormal, and together they span the **Fock space**. It is a Hilbert space: its inner product is positive.

**Worked example ($n=2$).** The four states are $|00\rangle=|0\rangle$, $|10\rangle=b_0^\dagger|0\rangle$, $|01\rangle=b_1^\dagger|0\rangle$ and $|11\rangle=b_0^\dagger b_1^\dagger|0\rangle$. Using only the rules:

$$
b_0|11\rangle=b_0b_0^\dagger b_1^\dagger|0\rangle=(1-b_0^\dagger b_0)b_1^\dagger|0\rangle=b_1^\dagger|0\rangle+b_0^\dagger b_1^\dagger b_0|0\rangle=|01\rangle,
$$

$$
b_1|11\rangle=b_1b_0^\dagger b_1^\dagger|0\rangle=-b_0^\dagger b_1b_1^\dagger|0\rangle=-b_0^\dagger(1-b_1^\dagger b_1)|0\rangle=-|10\rangle .
$$

The minus sign in $b_1|11\rangle=-|10\rangle$ is the price of anticommutation. Check: $b_0b_1|11\rangle=-b_0|10\rangle=-|00\rangle$ and $b_1b_0|11\rangle=b_1|01\rangle=|00\rangle$, so $\{b_0,b_1\}|11\rangle=0$ as required.

**Changing the basis of modes.** If $\Psi_a=\sum_sU_{as}b_s$ with a unitary matrix $U$ ($UU^\dagger=1$), then $\{\Psi_a,\Psi_b^\dagger\}=\sum_{s,s'}U_{as}U^\ast_{bs'}\{b_s,b_{s'}^\dagger\}=\sum_sU_{as}U^\ast_{bs}=(UU^\dagger)_{ab}=\delta_{ab}$. Any orthonormal choice of modes gives the same standard anticommutator. This is used in Section 8.10.

### 8.5 The Hamiltonian form of the dirac16complex Lagrangian

**Slices.** We quantize with respect to $x_4$. The **slices** $x_4=\text{const}$ are seven-dimensional, with the coordinates $x_0,x_1,x_2,x_3,x_5,x_6,x_7$. The procedure needs $g^{44}\ne0$: the slices must not be “characteristic” (Stage-1 document, §10.1). We write $\gamma^{x_4}$ for the curved gamma $\gamma^\mu$ with $\mu=4$, to distinguish it from the constant frame matrix $\gamma^4$.

**Removing the time derivative of $\Psi^\dagger$.** In $\mathcal L$ the time derivatives appear in the combination $\tfrac12\sqrt{|g|}\,\bigl(\bar\Psi\gamma^{x_4}\partial_4\Psi-\partial_4\bar\Psi\,\gamma^{x_4}\Psi\bigr)$. Add the total derivative $\tfrac12\partial_4\bigl(\sqrt{|g|}\,\bar\Psi\gamma^{x_4}\Psi\bigr)$, which by the product rule equals $\tfrac12\sqrt{|g|}\,\partial_4\bar\Psi\,\gamma^{x_4}\Psi+\tfrac12\sqrt{|g|}\,\bar\Psi\gamma^{x_4}\partial_4\Psi+\tfrac12\bar\Psi\,\partial_4(\sqrt{|g|}\gamma^{x_4})\Psi$. The terms with $\partial_4\bar\Psi$ cancel, and

$$
\mathcal L'=\mathcal L+\tfrac12\partial_4\bigl(\sqrt{|g|}\,\bar\Psi\gamma^{x_4}\Psi\bigr)=\Psi^\dagger K\,\partial_4\Psi-\mathcal H,\qquad K:=\sqrt{|g|}\,C\gamma^{x_4},
$$

where $\mathcal H$ collects (with a minus sign) all terms without a time derivative of $\Psi$ or $\Psi^\dagger$. By Section 5.4, $\mathcal L'$ has the same field equations as $\mathcal L$. It has the form of the first-order Lagrangians of Section 5.6: linear in the time derivative, with a matrix $K$ in front.

**Momenta and constraints.** The momentum conjugate to $\Psi_a$ (right derivative, Section 5.10) is

$$
\Pi_a=\frac{\partial_R\mathcal L'}{\partial(\partial_4\Psi_a)}=\sqrt{|g|}\,\bigl(\Psi^\dagger C\gamma^{x_4}\bigr)_a ,
$$

and $\mathcal L'$ does not contain $\partial_4\Psi^\dagger$ at all. As in Example A of Section 5.6, the momenta are fixed functions of the fields. In Dirac's theory of constrained systems the relations $\Pi_a-\sqrt{|g|}(\Psi^\dagger C\gamma^{x_4})_a\approx0$ and $\Pi_{\Psi^\dagger,a}\approx0$ are called **primary constraints**. Their brackets with each other form, up to sign and transposition, the matrix $K$ (Stage-1 document, §10.2). The canonical momentum formula was verified in a genuine Grassmann algebra at all G1 and G2 test points (checks `QNT_canonicalMomentum_G1` and `QNT_canonicalMomentum_G2`, `wolfram-geometry-report.json`).

**$K$ is invertible exactly when $g^{44}\ne0$.** The curved gamma satisfies $(\gamma^{x_4})^2=\tfrac12\{\gamma^{x_4},\gamma^{x_4}\}=g^{44}$ (the curved Clifford relation of Chapter 4), and $C^2=1$. Hence

$$
(C\gamma^{x_4})(\gamma^{x_4}C)=C\,g^{44}\,C=g^{44}\,I_{16},\qquad (\gamma^{x_4}C)(C\gamma^{x_4})=g^{44}\,I_{16},\qquad (C\gamma^{x_4})^{-1}=\frac{\gamma^{x_4}C}{g^{44}} .
$$

The constraints are therefore of the kind Dirac calls **second class**: they can be solved, and the resulting bracket (the **Dirac bracket**) is built from $K^{-1}$. The identity above was verified symbolically for an arbitrary $e_a{}^4$ and at the G1 points (check `QNT_curvedAnticommutatorMatrix`, `wolfram-algebra-report.json`). The graded constraint computation itself is a derivation, not a separate machine check (Stage-1 document, §10.2).

**$K$ is anti-Hermitian.** $K=\sqrt{|g|}\,e_a{}^4\,C\gamma^a$ is a real combination of the real antisymmetric matrices $C\gamma^a$ (expression [1], Section 5.12), so $K^T=-K$ and, being real, $K^\dagger=-K$. This is what makes the anticommutator matrix $iK^{-1}$ of Section 8.6 Hermitian. (When $K$ depends on $x_4$, the total derivative added above also puts the derivative-free term $-\tfrac12\bar\Psi\,\partial_4(\sqrt{|g|}\gamma^{x_4})\Psi$ into $\mathcal H$; the Stage-1 document, §9.5 and §10.4, discusses it. It vanishes in flat space and in the primordial field.)

**The Hamiltonian in flat space.** In flat space ($g=\eta$, $\sqrt{|g|}=1$, $\Omega_\mu=0$, $\gamma^{x_4}=\gamma^4$) with $U=0$,

$$
\mathcal H=-\tfrac12\sum_{j\ne4}\bigl(\bar\Psi\gamma^j\partial_j\Psi-\partial_j\bar\Psi\,\gamma^j\Psi\bigr)+m\,\bar\Psi\Psi .
$$

Integrated over a slice, the term $-\partial_j\bar\Psi\,\gamma^j\Psi$ can be moved by parts, $-\int\partial_j\bar\Psi\,\gamma^j\Psi\,d^7x=+\int\bar\Psi\gamma^j\partial_j\Psi\,d^7x$ (the fields vanish far away), so the Hamiltonian is

$$
H=\int\Psi^\dagger\Bigl(mC-\sum_{j\ne4}C\gamma^j\partial_j\Bigr)\Psi\,d^7x .
$$

In a curved field $\mathcal H$ contains in addition the spin-connection terms; Chapter 7 and the Stage-1 document (§10.4) give its general form. The canonical structure, that is $K$, does not depend on the potential $U$, which contains no derivatives.

### 8.6 The equal-time anticommutator

**Result.** For two points $x$ and $y$ on the same slice,

$$
\begin{aligned}
&\bigl\{\Psi_a(x),\Psi^\dagger_b(y)\bigr\}=i\,\bigl[K^{-1}\bigr]_{ab}\,\delta^7(x-y)=i\,\frac{[\gamma^{x_4}C]_{ab}}{g^{44}}\,\frac{\delta^7(x-y)}{\sqrt{|g|}},\\
&\{\Psi_a(x),\Psi_b(y)\}=\{\Psi^\dagger_a(x),\Psi^\dagger_b(y)\}=0 .
\end{aligned}
$$

Here $\delta^7(x-y)$ is the seven-dimensional **Dirac delta**: the idealization of a very narrow bump of total integral 1, defined by $\int f(y)\,\delta^7(x-y)\,d^7y=f(x)$. On a lattice of points with cell volume $v$ it would be $\delta_{xy}/v$. The matrix $iK^{-1}$ is Hermitian, because $K^\dagger=-K$ gives $(iK^{-1})^\dagger=-i(K^\dagger)^{-1}=iK^{-1}$.

**Derivation.** We derive the rule from the requirement that the quantum Heisenberg equation reproduce the classical field equation. To keep every step visible, replace the slice by finitely many points, so that $\Psi$ is a column of $N$ odd operators, and take a Hamiltonian that is bilinear, $H=\Psi^\dagger h\Psi=\sum_{a,b}\Psi_a^\dagger h_{ab}\Psi_b$, with a numerical matrix $h$. The classical Lagrangian is $L'=\Psi^\dagger K\dot\Psi-\Psi^\dagger h\Psi$, and its Euler–Lagrange equation for $\Psi^\dagger$ (left derivative) is $K\dot\Psi=h\Psi$, that is

$$
\dot\Psi=K^{-1}h\Psi\qquad\text{(classical)}.
$$

Now suppose $\{\Psi_a,\Psi_b^\dagger\}=A_{ab}$ and $\{\Psi_a,\Psi_b\}=0$ for some matrix $A$. By the identity of Section 8.2,

$$
\begin{aligned}
&[\Psi_a^\dagger\Psi_b,\Psi_c]=\Psi_a^\dagger\{\Psi_b,\Psi_c\}-\{\Psi_a^\dagger,\Psi_c\}\Psi_b=-A_{ca}\Psi_b,\\
&[H,\Psi_c]=-\sum_{a,b}A_{ca}h_{ab}\Psi_b=-(Ah\Psi)_c .
\end{aligned}
$$

The Heisenberg equation gives $\dot\Psi=i[H,\Psi]=-iAh\Psi$. Agreement with the classical equation for every $h$ (for instance for every value of the mass) requires $-iA=K^{-1}$, that is

$$
\{\Psi_a,\Psi_b^\dagger\}=A_{ab}=i\,[K^{-1}]_{ab} .
$$

For the field the sums over points become integrals over the slice, $h$ becomes the differential operator of $H$, and $\delta_{ab}$ between points becomes $\delta^7(x-y)$; the computation is otherwise the same. Dirac's bracket method gives the same result (Stage-1 document, §10.2 and §10.3). The same computation with commutators instead of anticommutators would also reproduce the equation of motion; the choice of anticommutators is part of the definition of dirac16complex as a fermion field (Grassmann components, Section 5.9), and it is what gives the Pauli principle of Section 8.3.

**Check with the Grassmann oscillator.** For $L=\tfrac i2(\theta^\ast\dot\theta-\dot\theta^\ast\theta)-\omega\theta^\ast\theta$, adding $\tfrac i2\frac{d}{dt}(\theta^\ast\theta)$ gives $L'=i\theta^\ast\dot\theta-\omega\theta^\ast\theta$, so $K=i$ and $\{\theta,\theta^\dagger\}=i\cdot\tfrac1i=1$: the rule of Section 8.3.

**Gaussian normal gauge and the matrix $B$.** In the frames used throughout the book the time is “Gaussian normal”: $g^{44}=-1$ and $\gamma^{x_4}=\gamma^4$ (for example in the primordial field of Chapter 9, where the vielbein component along $x_4$ is 1). Then $iK^{-1}=i(C\gamma^4)^{-1}/\sqrt{|g|}=-i\gamma^4C/\sqrt{|g|}$, and since $\gamma^4$ anticommutes with all four factors of $C=\gamma^0\gamma^1\gamma^2\gamma^3$, it commutes with $C$. Therefore

$$
\bigl\{\Psi_a(x),\Psi^\dagger_b(y)\bigr\}=B_{ab}\,\frac{\delta^7(x-y)}{\sqrt{|g|}},\qquad B:=-iC\gamma^4 .
$$

In the primordial field $\sqrt{|g|}=\cos z$, and this is the anticommutator $B\,\delta^7/\cos z$ of the Stage-2 document (§17.1).

**Properties of $B$.** Each follows from $C^2=1$, $(\gamma^4)^2=-1$, $C\gamma^4=\gamma^4C$, $C^T=C$ and $(\gamma^4)^T=-\gamma^4$:

- $B^\dagger=i(\gamma^4)^TC^T=-i\gamma^4C=-iC\gamma^4=B$: **Hermitian**;
- $B^2=(-i)^2C\gamma^4C\gamma^4=-C^2(\gamma^4)^2=1$;
- $\mathrm{tr}\,B=0$: $C\gamma^4=\gamma^0\gamma^1\gamma^2\gamma^3\gamma^4$ is a product of an odd number of gammas, and such a product $X$ anticommutes with the chirality $\gamma^8$ of Chapter 2, so $\mathrm{tr}X=\mathrm{tr}(\gamma^8\gamma^8X)=\mathrm{tr}(\gamma^8X\gamma^8)=-\mathrm{tr}X$ (cyclicity of the trace and $(\gamma^8)^2=1$);
- so the eigenvalues of $B$ are $+1$ and $-1$ (from $B^2=1$), with multiplicity 8 each (from $\mathrm{tr}B=0$);
- $[C,B]=0$ and $BC=-iC\gamma^4C=-i\gamma^4$.

These are Result 10.2 of the Stage-1 document (check `ALG_chargeFormB`, both algebra reports; the characteristic polynomial $(x-1)^8(x+1)^8$ is recorded in `wolfram-algebra-report.json`). $B$ is $i$ times a signed permutation; the Student Guide (§6.4) tabulates it, for example $(Bu)_0=i\,u_9$.

**Heisenberg equation in flat space.** With $H$ of Section 8.5 and $\{\Psi_a,\Psi^\dagger_b\}=B_{ab}\delta^7$ the computation above gives $\partial_4\Psi=-iB\bigl(mC-\sum_jC\gamma^j\partial_j\bigr)\Psi$. With $BC=-i\gamma^4$ this is

$$
\partial_4\Psi=-m\gamma^4\Psi+\sum_{j\ne4}\gamma^4\gamma^j\partial_j\Psi ,
$$

which is the field equation $\gamma^\mu\partial_\mu\Psi=m\Psi$ multiplied from the left by $\gamma^4$ (use $(\gamma^4)^2=-1$). The quantum theory reproduces the classical equation, as it was built to do.

### 8.7 Why the anticommutator forces an indefinite inner product

**Theorem 8.1.** There is no Hilbert space (positive inner product) on which the operators $\Psi_a$ act with $\Psi_a^\dagger$ equal to their Hilbert adjoints and with $\{\Psi_a(x),\Psi_b^\dagger(y)\}=B_{ab}\delta^7(x-y)/\sqrt{|g|}$.

*Proof.* Suppose there were. Take a numerical column $v$ with $Bv=-v$ (it exists: $B$ has the eigenvalue $-1$) and an ordinary bump function $f$ on the slice, and form the smeared operator $\chi=\sum_av_a^\ast\int f(x)\Psi_a(x)\,d^7x$. Its adjoint is $\chi^\dagger=\sum_bv_b\int f(y)\Psi_b^\dagger(y)\,d^7y$, and

$$
\{\chi,\chi^\dagger\}=\sum_{a,b}v_a^\ast B_{ab}v_b\int\frac{f(x)^2}{\sqrt{|g|}}\,d^7x=-\,v^\dagger v\int\frac{f^2}{\sqrt{|g|}}\,d^7x<0 .
$$

But for any operator $\chi$ on a Hilbert space and any state $\varphi$, $\langle\varphi,\{\chi,\chi^\dagger\}\varphi\rangle=\langle\chi^\dagger\varphi,\chi^\dagger\varphi\rangle+\langle\chi\varphi,\chi\varphi\rangle\ge0$. A negative multiple of the identity cannot satisfy this. $\square$

**The way out: a Krein space.** A **Krein space** is a complex vector space with a Hermitian form $[f,h]$ that is non-degenerate but **indefinite** (some vectors have $[f,f]<0$), together with a **fundamental symmetry** $J$, an operator with $J=J^\dagger=J^{-1}$, such that $[f,Jh]$ is a positive inner product. The canonical anticommutator defines exactly such a structure on the one-particle wave functions: the form is $[f,h]=f^\dagger Bh$, of signature (8,8), and $J=B$ is a fundamental symmetry, because $B$ is Hermitian with $B^2=1$ and $[f,Bh]=f^\dagger B^2h=f^\dagger h$ is the standard positive product (Stage-1 document, §10.5).

**Hilbert adjoint and Krein adjoint.** In a representation on a positive Hilbert space, define

$$
\chi:=\Psi^\dagger B,\qquad\text{i.e.}\qquad \chi_b=\sum_a\Psi_a^\dagger B_{ab}.
$$

Then, in flat space and Gaussian normal gauge, $\{\Psi_a,\chi_b\}=\sum_c\{\Psi_a,\Psi_c^\dagger\}B_{cb}\,=(B^2)_{ab}\,\delta^7=\delta_{ab}\delta^7$, the standard positive anticommutator: $\chi$ is the **Hilbert adjoint** of $\Psi$. The canonical $\Psi^\dagger=\chi B$ is not the Hilbert adjoint; it is the adjoint with respect to the indefinite form, the **Krein adjoint**. Every bilinear $\Psi^\dagger M\Psi$ of the classical theory becomes $\chi BM\Psi$ in the positive representation; Section 8.12 draws the consequences.

**Worked example (a two-mode Krein toy).** Take two modes with $B=\mathrm{diag}(+1,-1)$: $\{\psi_0,\psi_0^\dagger\}=1$ and $\{\psi_1,\psi_1^\dagger\}=-1$. In a positive representation, $\chi_0=\psi_0^\dagger$ and $\chi_1=-\psi_1^\dagger$ are the Hilbert adjoints, with $\{\psi_1,\chi_1\}=1$. The operator $\psi_1^\dagger\psi_1=-\chi_1\psi_1$ has the eigenvalues 0 and $-1$ (Section 8.3 with $b=\psi_1$): the second mode carries negative “norm”. The $16\times16$ matrix $B$ contains eight such negative directions.

### 8.8 The indefiniteness is intrinsic to signature (4,4)

One might hope that a cleverer choice of “charge density” would be positive. In ordinary Dirac theory with one time direction it is: the density $\bar\psi\gamma^0\psi=\psi^\dagger\psi$ is positive. The Stage-1 document proves that in signature (4,4) no such choice exists (its Theorem 10.1). We give the argument in steps.

**Step 1 (invariant forms).** A matrix $H$ defines a **Spin(4,4)-invariant bilinear form** $\Psi^TH\Phi$ if it does not change under the infinitesimal spin rotations $\Psi\to(1+\epsilon S^{ab})\Psi$, that is if $(S^{ab})^TH+HS^{ab}=0$ for all $a,b$. The charge matrix $C$ is one: $(S^{ab})^TC=-CS^{ab}C\,C=-CS^{ab}$ by Section 5.12. The chiral projectors $P_\mp=\tfrac12(1\mp\gamma^8)$ of Chapter 2 commute with every $S^{ab}$ and with $C$, so $CP_-$ and $CP_+$ are invariant as well. The repository computed the space of all invariant bilinear forms exactly: it is 2-dimensional and spanned by $CP_-$ and $CP_+$ (Result 10.3; check `ALG_invariantForms`, both algebra reports). So every invariant Hermitian form is $H=\alpha CP_-+\beta CP_+$ with real $\alpha,\beta$. Such an $H$ is **even**: it commutes with $\gamma^8$, because $C$ and $P_\mp$ do.

**Step 2 (the density is odd).** The time component of a current built with $H$ has the matrix $H\gamma^4$, or more generally the Hermitian part $X=\tfrac12\bigl(cH\gamma^4+(cH\gamma^4)^\dagger\bigr)$ of $cH\gamma^4$ for some constant $c$. The frame matrix $\gamma^4$ anticommutes with $\gamma^8$, and $H$ commutes with it, so $\gamma^8(cH\gamma^4)\gamma^8=-cH\gamma^4$; taking adjoints (with $\gamma^8$ Hermitian) gives the same for $(cH\gamma^4)^\dagger$. Hence

$$
\gamma^8X\gamma^8=-X .
$$

**Step 3 (equal numbers of signs).** If $Xv=\lambda v$ then $X(\gamma^8v)=-\gamma^8Xv=-\lambda\,\gamma^8v$. So $\gamma^8$ maps the eigenvectors of $\lambda$ onto eigenvectors of $-\lambda$, one to one, and the Hermitian matrix $X$ has as many positive as negative eigenvalues. Unless $X=0$, the density $\Psi^\dagger X\Psi$ is indefinite. The repository shows more: $X^2=|k|^2I_{16}$ with $k=\tfrac12(\bar c\beta-c\alpha)$, so $X$ has signature (8,8) whenever it is not zero (`ALG_invariantForms`).

The reason is the one stated in the Stage-1 document: every invariant form is even in chirality while the time-like $\gamma^4$ is odd. In four dimensions with one time the invariant form is itself odd ($\gamma^0$), and the product with $\gamma^0$ is the positive identity. The indefinite (Krein) structure of dirac16complex is therefore not an accident of the choice $B$; it is intrinsic to signature (4,4).

**Positive energy does not help.** One might restrict to states of positive energy. At rest in flat space the mode Hamiltonian of Section 8.9 is $h_0=m(-i\gamma^4)$, so for $m>0$ the positive-energy space $V_+$ is the eigenspace of $-i\gamma^4$ with eigenvalue $+1$. The matrix $-i\gamma^4$ is Hermitian, squares to 1 and is traceless, so $V_+$ has dimension 8. On $V_+$ the matrix $B=C(-i\gamma^4)$ acts as $C$, which maps $V_+$ to itself (it commutes with $\gamma^4$) and squares to 1. Its trace on $V_+$ is $\mathrm{tr}(CP)$ with the projector $P=\tfrac12(1-i\gamma^4)$ onto $V_+$: $\mathrm{tr}(CP)=\tfrac12\mathrm{tr}C-\tfrac i2\mathrm{tr}(C\gamma^4)=0$, because $C$ is a product of four anticommuting gammas ($\mathrm{tr}\,\gamma^0\gamma^1\gamma^2\gamma^3=\mathrm{tr}\,\gamma^1\gamma^2\gamma^3\gamma^0=-\mathrm{tr}\,\gamma^0\gamma^1\gamma^2\gamma^3$) and $C\gamma^4$ is odd. So the Krein form $u^\dagger Bu$ has signature (4,4) even on the positive-energy states at rest. The repository finds (4,4) on both energy eigenspaces at rest and also for moving states in the good sector, for example at $m=1$, $k=(1,1,2,3)$, $E=4$ (Result 10.4; check `QNT_kreinSignature`, both algebra reports).

**Worked example with explicit vectors.** Write $e_n$ for the column with 1 in position $n$ and 0 elsewhere, and use the tables of the Student Guide (§6.3, §6.4): $(\gamma^4u)_0=-u_{13}$, $(\gamma^4u)_4=u_9$, $(\gamma^4u)_9=-u_4$, $(\gamma^4u)_{13}=u_0$, and $(Cu)_0=-u_4$, $(Cu)_4=-u_0$, $(Cu)_9=u_{13}$, $(Cu)_{13}=u_9$. Consider

$$
u_+=\tfrac12\bigl(e_0-e_4-i\,e_9-i\,e_{13}\bigr),\qquad u_-=\tfrac12\bigl(e_0+e_4+i\,e_9-i\,e_{13}\bigr).
$$

For $u_+$: $(\gamma^4u_+)_0=-(-\tfrac i2)=\tfrac i2$, so $(-i\gamma^4u_+)_0=\tfrac12$; in the same way components 4, 9 and 13 reproduce $-\tfrac12$, $-\tfrac i2$, $-\tfrac i2$, so $-i\gamma^4u_+=u_+$. And $(Cu_+)_0=-(-\tfrac12)=\tfrac12$, $(Cu_+)_4=-\tfrac12$, $(Cu_+)_9=-\tfrac i2$, $(Cu_+)_{13}=-\tfrac i2$, so $Cu_+=u_+$ and $Bu_+=u_+$. For $u_-$ the same bookkeeping gives $-i\gamma^4u_-=u_-$ but $Cu_-=-u_-$, so $Bu_-=-u_-$. Both are normalized positive-energy states at rest ($u^\dagger u=1$), and $u_+^\dagger Bu_+=+1$ while $u_-^\dagger Bu_-=-1$. ($u_+$ is the standard rest state of the Stage-3 programs, called $u_0$ in the Student Guide, §6.10.)

### 8.9 Flat-space modes and the mode Hamiltonian

**Schrödinger form.** In flat space with $U=0$ the field equation is $\gamma^4\partial_4\Psi+\sum_{j\ne4}\gamma^j\partial_j\Psi=m\Psi$. Multiply from the left by $\gamma^4$ and use $(\gamma^4)^2=-1$: $-\partial_4\Psi+\sum_j\gamma^4\gamma^j\partial_j\Psi=m\gamma^4\Psi$. For a plane wave $\Psi=e^{i\sum_jk_jx_j}u(x_4)$ with real wave numbers $k_j$ ($j\in\{0,1,2,3,5,6,7\}$) each $\partial_j$ becomes $ik_j$, and multiplying by $i$ gives

$$
i\,\partial_4u=h_k\,u,\qquad h_k=-im\gamma^4-\gamma^4\sum_{j\ne4}k_j\gamma^j .
$$

$h_k$ is the **mode Hamiltonian**, a $16\times16$ complex matrix.

**Its square.** Three facts follow from the Clifford relations: $(-im\gamma^4)^2=-m^2(\gamma^4)^2=m^2$; $(\gamma^4\gamma^j)^2=\gamma^4\gamma^j\gamma^4\gamma^j=-(\gamma^4)^2(\gamma^j)^2=\eta^{jj}$ for $j\ne4$; and all cross terms cancel, because $\{\gamma^4,\gamma^4\gamma^j\}=(\gamma^4)^2\gamma^j+\gamma^4\gamma^j\gamma^4=-\gamma^j+\gamma^j=0$ and, for $i\ne j$, $\{\gamma^4\gamma^i,\gamma^4\gamma^j\}=-(\gamma^4)^2(\gamma^i\gamma^j+\gamma^j\gamma^i)=0$. Hence

$$
h_k^2=E^2\,I_{16},\qquad E^2=m^2+k_0^2+k_1^2+k_2^2+k_3^2-k_5^2-k_6^2-k_7^2 .
$$

**Hermitian or not.** $(-i\gamma^4)^\dagger=i(\gamma^4)^T=-i\gamma^4$, so the mass term is Hermitian. $(\gamma^4\gamma^j)^\dagger=(\gamma^j)^T(\gamma^4)^T=-(\gamma^j)^T\gamma^4$. For $j\le3$, $\gamma^j$ is symmetric and this is $-\gamma^j\gamma^4=\gamma^4\gamma^j$: **Hermitian**. For $j\ge5$, $\gamma^j$ is antisymmetric and this is $\gamma^j\gamma^4=-\gamma^4\gamma^j$: **anti-Hermitian**. So the anti-Hermitian part of $h_k$ is $-\gamma^4(k_5\gamma^5+k_6\gamma^6+k_7\gamma^7)$, whose square is $-(k_5^2+k_6^2+k_7^2)I_{16}$ by the same cross-term cancellation; it vanishes only when $k_5=k_6=k_7=0$. **$h_k$ is Hermitian if and only if there is no momentum along the extra times.** The same split shows how $h_k$ behaves with respect to $B\propto\gamma^0\gamma^1\gamma^2\gamma^3\gamma^4$: the Hermitian part commutes with $B$ and the anti-Hermitian part anticommutes with it (a gamma with index $\le4$ commutes with this product of five gammas, one with index $\ge5$ anticommutes), which gives $[h_k,B]=2i\sum_{j=5}^7k_jC\gamma^j$ (Stage-1 document, §10.6).

**The Krein norm is always conserved.** Write $h_k=h_H+h_A$ with the Hermitian part $h_H$ (commuting with $B$) and the anti-Hermitian part $h_A$ (anticommuting with $B$). Then $h_k^\dagger B=(h_H-h_A)B=B(h_H+h_A)=Bh_k$. For a solution of $i\dot u=h_ku$ (so $\dot u^\dagger=iu^\dagger h_k^\dagger$),

$$
\frac{d}{dx_4}\bigl(u^\dagger Bu\bigr)=i\,u^\dagger\bigl(h_k^\dagger B-Bh_k\bigr)u=0,\qquad \frac{d}{dx_4}\bigl(u^\dagger u\bigr)=i\,u^\dagger\bigl(h_k^\dagger-h_k\bigr)u=-2i\,u^\dagger h_Au .
$$

The Krein norm $u^\dagger Bu$ never changes; the Hilbert norm $u^\dagger u$ changes whenever there is extra-time momentum.

**Samples from the repository.** These identities hold for symbolic $m$ and $k$ (Wolfram) and by a structural proof for all real $m,k$ plus ten exact samples (Python) (Result 10.5; check `QNT_flatModeHamiltonian`, both algebra reports). Some of the samples of `artifacts/dirac16complex/arbitrary-field/python-algebra-report.json`:

| $m$ | nonzero wave numbers | Hermitian | $E^2$ |
| --- | --- | --- | --- |
| 1 | none | yes | 1 |
| 3/2 | $k_0=1/2$, $k_1=-1/3$, $k_2=2$ | yes | 119/18 |
| 1 | $k_0=1/2$, $k_6=-2/3$ | no | 29/36 |
| 1 | $k_5=1$ | no | 0 |
| 1 | $k_7=2$ | no | $-3$ |
| 1/2 | $k_0,\dots,k_3=\tfrac17,\tfrac27,\tfrac37,\tfrac47$; $k_5,k_6,k_7=\tfrac57,\tfrac67,1$ | no | $-271/196$ |
| 0 | $k_1=3$, $k_5=3$ | no | 0 |

For instance $\tfrac14+\tfrac{1+4+9+16}{49}-\tfrac{25+36+49}{49}=\tfrac14-\tfrac{80}{49}=\tfrac{49-320}{196}=-\tfrac{271}{196}$.

**The three cases.** Because $h_k^2=E^2$, the power series of the exponential collapses:

$$
e^{-ih_kx_4}=\cos(Ex_4)-i\,\frac{\sin(Ex_4)}{E}\,h_k .
$$

(The even powers give $\cos$, the odd powers give $h_k$ times $\sin/E$.) Three cases occur (Stage-1 document, §10.10).

- $E^2>0$: the frequencies $\pm E$ are real and the modes oscillate, even when $h_k$ is not Hermitian (the sample $E^2=29/36$). $h_k$ is then diagonalizable, with the projectors $P_\pm=\tfrac12(1\pm h_k/E)$: one checks $P_\pm^2=P_\pm$, $P_++P_-=1$ and $h_kP_\pm=\pm EP_\pm$ from $h_k^2=E^2$.
- $E^2=0$ and $h_k\ne0$: $h_k$ is **nilpotent**, $h_k^2=0$, and $e^{-ih_kx_4}=1-ih_kx_4$: the mode **grows linearly** (the samples $m=1$, $k_5=1$ and $m=0$, $k_1=k_5=3$).
- $E^2<0$, that is exactly when $k_5^2+k_6^2+k_7^2>m^2+k_0^2+k_1^2+k_2^2+k_3^2$: with $E=i\kappa$, $\kappa=\sqrt{-E^2}$, one has $\cos(i\kappa x_4)=\cosh(\kappa x_4)$ and $\sin(i\kappa x_4)/(i\kappa)=\sinh(\kappa x_4)/\kappa$, so $e^{-ih_kx_4}=\cosh(\kappa x_4)-i\,h_k\sinh(\kappa x_4)/\kappa$: the mode **grows exponentially**, like $e^{\kappa x_4}$. Two of the ten samples are of this kind.

This is the quantum version of the classical observation of Section 5.5: an equation with several time directions does not have a well-posed initial-value problem on the slices $x_4=\text{const}$, because those slices themselves contain three time-like directions (the **ultrahyperbolic** problem).

### 8.10 The good sector and its Fock space

**Definition.** The **good sector** is the sector of fields that do not depend on $x_5,x_6,x_7$, that is $k_5=k_6=k_7=0$. It is a dimensional reduction to a theory in 4+1 dimensions on the coordinates $(x_0,x_1,x_2,x_3,x_4)$. It is **not** a subspace of the one-particle space of the full theory: on the seven-dimensional slice the set $k_5=k_6=k_7=0$ has zero volume, so no normalizable state of the full theory lies in it, and a field independent of $x_5,x_6,x_7$ cannot satisfy the $\delta^7$ anticommutator. One keeps instead the zero modes in $x_5,x_6,x_7$ on a normalization volume $V_3$, for which $\{\Psi_a,\chi_b\}=\delta_{ab}\,\delta^4/V_3$ (Stage-1 document, §10.6).

**The Dirac Hamiltonian in 4+1 dimensions.** Put $\beta:=-i\gamma^4$ and $\alpha^a:=-\gamma^4\gamma^a$ for $a=0,1,2,3$. All five are Hermitian (Section 8.9), $\beta^2=1$, $(\alpha^a)^2=-(\gamma^4)^2(\gamma^a)^2=1$, $\{\alpha^a,\alpha^b\}=2\delta^{ab}$ and $\{\alpha^a,\beta\}=0$. In the good sector

$$
h_k=m\beta+\sum_{a=0}^{3}k_a\alpha^a,\qquad h_k^2=E_k^2,\qquad E_k=\sqrt{m^2+k_0^2+k_1^2+k_2^2+k_3^2},
$$

the standard Dirac Hamiltonian in 4+1 dimensions, acting on 16 components. It is Hermitian and traceless ($\mathrm{tr}\gamma^4=0$ and $\mathrm{tr}(\gamma^4\gamma^a)=0$ for $a\ne4$), so its eigenvalues are $+E_k$ and $-E_k$ with multiplicity 8 each: for every momentum $k=(k_0,k_1,k_2,k_3)$ there are 8 particle states and 8 antiparticle states.

**One momentum, step by step.** Fix $k$ and choose orthonormal eigenvectors $u_s$ ($h_ku_s=+E_ku_s$) and $v_s$ ($h_kv_s=-E_kv_s$), $s=0,\dots,7$. Together they form an orthonormal basis of $\mathbb C^{16}$, so the **completeness relation** $\sum_s(u_s)_a(u_s)_b^\ast+\sum_s(v_s)_a(v_s)_b^\ast=\delta_{ab}$ holds. Expand the field mode as

$$
\Psi=\sum_{s=0}^{7}b_s\,u_s\,e^{-iE_kx_4}+\sum_{s=0}^{7}d_s^\ast\,v_s\,e^{+iE_kx_4},\qquad \{b_s,b_{s'}^\ast\}=\{d_s,d_{s'}^\ast\}=\delta_{ss'},
$$

all other anticommutators zero, where ${}^\ast$ is the Hilbert adjoint. By the completeness relation (and Section 8.4), $\{\Psi_a,\Psi_b^\ast\}=\delta_{ab}$: this is $\{\Psi_a,\chi_b\}=\delta_{ab}$ with $\chi=\Psi^\ast$, the positive anticommutator of Section 8.7. The **Hamiltonian** of the mode is $\Psi^\dagger(mC-iC\sum_ak_a\gamma^a)\Psi=\chi B(mC-iC\sum_ak_a\gamma^a)\Psi=\chi h_k\Psi$, because $BC=-i\gamma^4$ gives $B(mC)=m\beta$ and $B(-ik_aC\gamma^a)=-k_a\gamma^4\gamma^a=k_a\alpha^a$. Inserting the expansion and using orthonormality,

$$
H_k=\sum_sE_k\,b_s^\ast b_s-\sum_sE_k\,d_sd_s^\ast=\sum_sE_k\bigl(b_s^\ast b_s+d_s^\ast d_s\bigr)-8E_k .
$$

**Vacuum, Dirac sea, normal ordering.** The **vacuum** $|0\rangle$ is annihilated by all $b_s$ and all $d_s$. In the language of the classical modes, all negative-energy states are filled (the **Dirac sea**): $d_s^\ast$, which multiplies the negative-energy wave function $v_s$, creates an **antiparticle**, a hole in the sea, with positive energy $E_k$. The constant $-8E_k$ is the energy of the filled sea for this momentum; **normal ordering** removes it by definition. The result, for all momenta (Stage-1 document, §10.7), is

$$
H=\int\frac{d^4k}{(2\pi)^4}\,E_k\sum_{s=0}^{7}\bigl(b_s(k)^\ast b_s(k)+d_s(k)^\ast d_s(k)\bigr)\ \ge0 .
$$

This is a positive-definite Fock space with a Hamiltonian that is not negative. It is the quantization of the reduced (4+1)-dimensional theory, not a subspace of a Fock space of the full eight-dimensional theory. The construction of this section is derived from the checked Results 10.2, 10.4 and 10.5; it is not itself a machine check (Stage-1 document, §10.7 and §13, item 5).

### 8.11 Symmetries: unitary and Krein-unitary

**Two notions.** A spin transformation $R=\exp(\theta S)$ that maps the slices $x_4=\text{const}$ to themselves preserves the canonical anticommutator if $R^\dagger BR=B$; it is then called **Krein-unitary**. It is implemented by a unitary operator on the positive Fock space if in addition $R$ is unitary, $R^\dagger R=1$, and commutes with $J=B$ (Stage-1 document, §10.8). For the generator $S$ the conditions read: $S$ anti-Hermitian ($S^\dagger=-S$) for unitarity, and $S^\dagger B+BS=0$ for Krein-unitarity.

**Counting by hand.** The 28 generators $S^{ab}=\tfrac12\gamma^a\gamma^b$ ($a<b$) are real, so $(S^{ab})^\dagger=(S^{ab})^T=\tfrac14[(\gamma^b)^T,(\gamma^a)^T]$.

- *Hermiticity.* If $a,b\le3$ both gammas are symmetric and $(S^{ab})^T=\tfrac14[\gamma^b,\gamma^a]=-S^{ab}$; if $a,b\ge4$ both are antisymmetric and the two signs cancel, again $-S^{ab}$. If one index is $\le3$ and the other $\ge4$ one sign remains and $(S^{ab})^T=+S^{ab}$. So $6+6=12$ generators are anti-Hermitian and 16 (the “boosts” mixing a space-like and a time-like direction) are Hermitian.
- *Commuting with $B$.* $B=-i\gamma^0\gamma^1\gamma^2\gamma^3\gamma^4$. A gamma with index $\le4$ anticommutes with four of these five factors and commutes with itself, so it commutes with $B$; a gamma with index $5$, $6$ or $7$ anticommutes with all five, so it anticommutes with $B$. Hence $S^{ab}$ commutes with $B$ exactly when both indices lie in $\{0,\dots,4\}$ or both in $\{5,6,7\}$: $\binom52+\binom32=10+3=13$ generators; the other 15 anticommute with $B$.
- *Unitarily implemented and slice-preserving.* Anti-Hermitian and commuting with $B$: both indices in $\{0,1,2,3\}$ (6) or both in $\{5,6,7\}$ (3), in total **9**, generating $\mathrm{Spin}(4)\times\mathrm{Spin}(3)$.
- *Krein-unitary.* For an anti-Hermitian $S$ the condition $S^\dagger B+BS=0$ means $[B,S]=0$; for a Hermitian $S$ it means $\{B,S\}=0$. The first kind gives the 9 above; the second kind gives the 12 Hermitian generators with one index in $\{0,1,2,3\}$ and the other in $\{5,6,7\}$. In total **21**, exactly the generators with $a,b\ne4$, generating the Krein-unitary slice group Spin(4,3). The condition fails for the 7 generators with an index 4: the 4 Hermitian $S^{a4}$ ($a\le3$), which commute with $B$, and the 3 anti-Hermitian $S^{4b}$ ($b\ge5$), which anticommute with it.

These counts, 13, 9, 21 and 12, are Result 10.6 of the Stage-1 document (check `QNT_unitaryAndKreinSubgroups`, both algebra reports). They correct the first statement of the project contract, “Spin(4)×Spin(3) (compact, commuting with B)”, which suggested that exactly 9 generators commute with $B$; the reports record that literal claim as false (erratum E1 in `handoff/specs/CONTRACT.md`, §11).

**Boosts in the good sector.** The four boosts $S^{a4}$, $a\le3$, commute with $B$ but are Hermitian, so as $16\times16$ matrices $\exp(\theta S^{a4})$ is neither unitary nor Krein-unitary. This is a statement about matrices, not about physics: a boost tilts the slices $x_4=\text{const}$, and in the good sector it is implemented unitarily on the Fock space exactly as in ordinary Dirac theory, whose boost generators are also Hermitian. The Stage-1 document (§10.8) derives this; the matrix statements behind it were checked numerically at sample momenta while that document was revised, not as recorded checks. The symmetries that act unitarily in the good sector include the translations in $x_0,\dots,x_4$, the Spin(4,1) generated by the 10 $S^{ab}$ with $a,b\le4$, the Spin(3) of the extra times, and the U(1) phase.

### 8.12 The U(1) charge and the expectation-value rule

**The current.** The phase symmetry $\Psi\to e^{i\alpha}\Psi$ (Section 5.7) gives the conserved current $J^\mu=-i\bar\Psi\gamma^\mu\Psi$ (Chapter 7). Its matrices $-iC\gamma^a$ are Hermitian: $(-iC\gamma^a)^\dagger=i(\gamma^a)^TC=i(-C\gamma^aC)C=-iC\gamma^a$ (Section 5.12). In Gaussian normal gauge $J^4=-i\Psi^\dagger C\gamma^4\Psi=\Psi^\dagger B\Psi$: the charge density is the Krein form (checks `QNT_currentHermiticity`, both algebra reports, and `GR_currentHermitian`, `grassmann-demo-report.json`). The conserved charge is $Q=\int\sqrt{|g|}\,J^4\,d^7x$. As a quadratic form in classical spinors it is indefinite, of signature (8,8). In the positive representation, $\Psi^\dagger B\Psi=\chi BB\Psi=\chi\Psi$, and in the good sector the mode expansion of Section 8.10 gives, after normal ordering (summed over all modes),

$$
Q=\sum\bigl(b^\ast b-d^\ast d\bigr).
$$

Particles have charge $+1$ and antiparticles charge $-1$ (derived, Stage-1 document §10.9).

**The expectation-value rule.** Every classical bilinear becomes, in the positive representation, $\Psi^\dagger M\Psi=\chi BM\Psi$ (Section 8.7). For a one-particle state $|u\rangle=b_u^\ast|0\rangle$, whose wave function $u$ is a normalized ($u^\dagger u=1$) positive-energy solution in the good sector, the normal-ordered expectation value is

$$
\bigl\langle\Psi^\dagger M\Psi\bigr\rangle=u^\dagger BM\,u .
$$

*Derivation.* Choose the positive-energy basis of Section 8.10 with $u_0=u$. In $\chi_a(BM)_{ab}\Psi_b$ the particle part is $\sum_{s,s'}b_s^\ast b_{s'}\,(u_s^\dagger BMu_{s'})$, and $\langle u|b_s^\ast b_{s'}|u\rangle=1$ for $s=s'=0$ and 0 otherwise. The terms with $d\,d^\ast$ become $-d^\ast d$ after normal ordering and vanish in a state without antiparticles; the mixed terms $b^\ast d^\ast$ and $d\,b$ change the number of particles and have zero expectation value. $\square$

**Examples** (Stage-1 document, §10.11):

- the charge, $M=B$: $u^\dagger B^2u=u^\dagger u=1$;
- the energy, $M=Bh$ (because $H=\chi h\Psi=\Psi^\dagger Bh\Psi$): $u^\dagger B^2hu=u^\dagger hu=E$;
- the scalar density $S=\bar\Psi\Psi$, $M=C$: $u^\dagger BCu=u^\dagger(-i\gamma^4)u$, which equals $+1$ for a positive-energy state at rest with $m>0$. So the energy density at rest is $\langle\rho\rangle=m\langle S\rangle=m=E$, as it should be.

The two rest states $u_\pm$ of Section 8.8 both have $u^\dagger(-i\gamma^4)u=1$, but the naive density $\Psi^\dagger\Psi$ would give $u^\dagger Bu=+1$ for $u_+$ and $-1$ for $u_-$. The naive density is not the physical one. This rule is the one used by the dark-sector experiments of Chapter 11 (Student Guide, §6.10).

**Which bilinears are observables.** In the positive representation $\chi BM\Psi$ is self-adjoint exactly when $BM$ is Hermitian; for a Hermitian $M$ this holds exactly when $[M,B]=0$. The current components $J^0,\dots,J^4$ pass this test. For $J^5,J^6,J^7$ the Hermitian matrix $-iC\gamma^j$ ($j\ge5$) anticommutes with $B$ (Section 8.11: $\gamma^j$ anticommutes with $B$, and $C$ commutes with it), so $BM$ is anti-Hermitian and these components have purely imaginary expectation values: they are not observables in this Fock space (Stage-1 document, §10.9 and §10.11).

### 8.13 The extra-time modes grow

Section 8.9 showed that a wave with enough momentum along an extra time grows instead of oscillating. The fifth experiment of Stage 3, **EXP-5**, follows this growth numerically in a background in which the extra times shrink (`provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.md`, §10). The extra-time scale factor is $e^{-x_4}$, and the mode has comoving momentum $q$ along $x_5$ ($m=1$), so its physical momentum $Q=q\,e^{x_4}$ grows and

$$
h=-im\gamma^4-Q\,\gamma^4\gamma^5,\qquad E^2=m^2-q^2e^{2x_4},\qquad E^2<0\ \text{ for }\ x_4>t_\ast=\ln(m/q).
$$

For $q=0.05$ and $q=0.1$ the turning times are $t_\ast=2.99573$ and $2.30259$, and each run starts on a positive-energy eigenvector of $h$ with Krein norm $u^\dagger Bu=\pm E_0/m$, $E_0=0.998749$ and $0.994987$ (`artifacts/dirac16complex/numerics/exp5/summary.json`). The committed results are:

- the Hilbert norm $u^\dagger u$ grows to $1.258\times10^{16}$ ($q=0.05$) and $1.313\times10^{16}$ ($q=0.1$) by $x_4=t_\ast+3$, and its logarithmic growth rate rises from about 2.4 to 25.3: super-exponential growth, because $Q$ keeps growing;
- the growth agrees with the **WKB estimate** (named after Wentzel, Kramers and Brillouin: while $Q$ changes slowly, treat it as constant, so that the norm grows at the rate $2\kappa$ with $\kappa=\sqrt{Q^2-m^2}$, and add up these rates), $\ln(u^\dagger u)\approx2W(x_4)$ with $W=\int_{t_\ast}^{x_4}\kappa\,dx_4'=\sqrt{Q^2-m^2}-m\arccos(m/Q)$, to $1.03\times10^{-3}$ relative at leading order and $2.47\times10^{-4}$ at first order ($q=0.05$);
- the Krein norm stays at its initial value: its drift, divided by $\max(u^\dagger u,1)$, is at most $1.08\times10^{-9}$, as the conservation law of Section 8.9 requires.

![EXP-5: (a) $\ln(u^\dagger u)$ for both momenta and both signs of $C$ together with the WKB curve $2W$; (b) $E^2$, which turns negative at $t_\ast=\ln(m/q)$ (dotted).](artifacts/dirac16complex/numerics/figures/exp5_growth.png)

The Rust program passes 7 of 7 self-checks for EXP-5 and its independent checker 21 of 21 (numerics document, §10.6). The growth conserves the indefinite Krein norm, so the positive-norm and the negative-norm parts grow together.

**In the primordial field.** The Stage-2 document (§14.3) finds the same onset in the author's primordial field, where 3-space inflates as $e^{a_4}$ and the extra times deflate as $e^{-a_4}$: with frozen coefficients a mode with momentum $k_5$ along $x_5$ has $E^2=M_{\mathrm{eff}}^2+K^2+(k_1e^{-H\zeta-a_4})^2-(k_5e^{-H\zeta+a_4})^2$, which turns negative once $a_4>H\zeta+\ln\bigl(\sqrt{M_{\mathrm{eff}}^2+K^2}/|k_5|\bigr)$. An unboundedly growing $a_4$, such as the notebook's $a_4=t$, reaches this onset.

**Consequence.** The positive Fock space exists only in the good sector. Every quantum statement and every numerical result of Chapters 11, 13 and 14 is restricted to that sector. The restriction is **imposed, not derived**: whether some dynamical mechanism suppresses the extra-time sector is an open problem (Chapter 18).

### 8.14 How the repository checks all of this

The algebraic ingredients of the quantization are machine-checked; the constructions built on them are derivations (Stage-1 document, §13, item 5):

| statement | check (report) |
| --- | --- |
| $\Pi=\sqrt{\lvert g\rvert}\,\Psi^\dagger C\gamma^{x_4}$ in a Grassmann algebra | `QNT_canonicalMomentum_G1`, `_G2` (wolfram-geometry) |
| $(C\gamma^{x_4})(\gamma^{x_4}C)=g^{44}$; reduction to $B$ in the primordial field | `QNT_curvedAnticommutatorMatrix` (wolfram-algebra) |
| $B$ Hermitian, $B^2=1$, spectrum $(8,8)$, $[C,B]=0$, $BC=-i\gamma^4$ | `ALG_chargeFormB` (both algebra reports) |
| invariant forms $CP_\pm$; every invariant density indefinite | `ALG_invariantForms` (both algebra reports) |
| Krein signature (4,4) on the energy eigenspaces | `QNT_kreinSignature` (both algebra reports) |
| $h_k^2=E^2$, Hermiticity, $[h_k,B]$ | `QNT_flatModeHamiltonian` (both algebra reports) |
| the counts 13, 9, 21, 12 | `QNT_unitaryAndKreinSubgroups` (both algebra reports) |
| Hermitian current, $J^4$ matrix equals $B$ | `QNT_currentHermiticity` (both), `GR_currentHermitian` (grassmann-demo) |
| extra-time growth, Krein-norm conservation | EXP-5: 7 self-checks, 21 checker checks |

Not machine-checked, but derived in the Stage-1 document and in this chapter: the Dirac-bracket computation, the Hamiltonian density, the Heisenberg equations, the mode expansion, the Fock space and the expectation-value rule. The algebra reports are `artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json` (21 of 21 checks true) and `python-algebra-report.json` (21 of 21), the geometry report `wolfram-geometry-report.json` (43 of 43); the Stage-1 gate that regenerates and compares all of them is described in Chapter 19.

### 8.15 What we proved and what we assumed

**What we proved.** With complete arguments in this chapter: the anticommutator of a fermion mode implies the Pauli principle, and many modes give a Fock space (Sections 8.3 and 8.4); the dirac16complex Lagrangian can be written, up to a total derivative, in the first-order form $\Psi^\dagger K\partial_4\Psi-\mathcal H$ with the anti-Hermitian $K=\sqrt{|g|}\,C\gamma^{x_4}$, which is invertible exactly when $g^{44}\ne0$; requiring that the Heisenberg equation reproduce the classical field equation gives $\{\Psi,\Psi^\dagger\}=iK^{-1}\delta^7$, which in Gaussian normal gauge is $B\,\delta^7/\sqrt{|g|}$ with $B=-iC\gamma^4$ Hermitian, $B^2=1$ and eight eigenvalues of each sign; no positive Hilbert space can carry this anticommutator with $\Psi^\dagger$ as the Hilbert adjoint (Theorem 8.1), so the one-particle space is a Krein space with fundamental symmetry $J=B$; every Spin(4,4)-invariant charge density is indefinite, given the computed list of invariant forms; the Krein form has signature (4,4) on the positive-energy rest states; the mode Hamiltonian satisfies $h_k^2=E^2$, it is Hermitian exactly when there is no extra-time momentum, and it always conserves the Krein norm; with extra-time momentum the modes oscillate, grow linearly or grow exponentially according to the sign of $E^2$; in the good sector there is a positive Fock space with a non-negative normal-ordered Hamiltonian, particles of charge $+1$ and antiparticles of charge $-1$; the expectation-value rule $\langle\Psi^\dagger M\Psi\rangle=u^\dagger BMu$; and the counts 13, 9, 21 and 12 of the symmetry generators.

**What we assumed or took from elsewhere.** Anticommutators rather than commutators are part of the definition of dirac16complex as a fermion field; no spin–statistics theorem for signature (4,4) is proved. The quantization is canonical with respect to $x_4$ and requires $g^{44}\ne0$; the matrix $B$ appears in Gaussian normal gauge. Dirac's bracket method is described, not carried out step by step (our derivation uses the Heisenberg equation on a finite set of points instead). That the invariant bilinear forms are spanned by $CP_-$ and $CP_+$ is an exact computation of the repository (`ALG_invariantForms`), not a hand proof. Normal ordering (subtracting the energy of the filled sea) is a prescription. The good sector is a restriction **imposed by hand**; no mechanism that removes the extra-time modes is derived. The unitary implementation of the boosts in the good sector is derived in the Stage-1 document, not a recorded check. The quantization is formal: no interacting theory, regularization or renormalization is constructed, and the Krein space is not given a physical interpretation beyond the good sector. The EXP-5 numbers are floating-point results with the tolerances stated in the numerics document.

### 8.16 Exercises

**Exercise 8.1.** With the $2\times2$ matrices $b$ and $b^\dagger$ of Section 8.3, verify $\{b,b^\dagger\}=1$ and $(b^\dagger)^2=0$, and find the eigenvalues of $N=b^\dagger b$.

**Exercise 8.2.** In the two-mode Fock space of Section 8.4 compute $b_0^\dagger|01\rangle$, $b_1b_0^\dagger|01\rangle$ and $b_0^\dagger b_1|01\rangle$, and check $\{b_1,b_0^\dagger\}|01\rangle=0$.

**Exercise 8.3.** For the first-order Lagrangian $L'=2i\,\theta^\ast\dot\theta-\omega\,\theta^\ast\theta$ (complex Grassmann $\theta$), find the classical equation of motion and the anticommutator $\{\theta,\theta^\dagger\}$ given by the rule $iK^{-1}$ of Section 8.6, and check that the Heisenberg equation with $H=\omega\theta^\dagger\theta$ reproduces the classical equation.

**Exercise 8.4.** Show $B^\dagger=B$ and $B^2=1$ for $B=-iC\gamma^4$, using only $C^T=C$, $C^2=1$, $(\gamma^4)^T=-\gamma^4$, $(\gamma^4)^2=-1$ and $C\gamma^4=\gamma^4C$.

**Exercise 8.5.** Compute $E^2$ for (a) $m=2$, $k_1=1$, $k_6=2$; (b) $m=1$, $k_0=1$, $k_5=1$, $k_7=1$; (c) $m=1$, $k_5=3$. For each case say whether the mode oscillates, grows linearly or grows exponentially, and give the growth rate $\kappa$ where there is one.

**Exercise 8.6.** For $m=1$ and $k_5=1$ (all other $k_j=0$) show directly that $h=-i\gamma^4-\gamma^4\gamma^5$ satisfies $h^2=0$, and write the solution $u(x_4)$ of $i\partial_4u=hu$.

**Exercise 8.7.** Verify with the tables quoted in Section 8.8 that $u_-=\tfrac12(e_0+e_4+ie_9-ie_{13})$ satisfies $-i\gamma^4u_-=u_-$ and $Cu_-=-u_-$. Compute $u_-^\dagger u_-$, $u_-^\dagger Bu_-$ and the scalar density $u_-^\dagger(-i\gamma^4)u_-$.

**Exercise 8.8.** Among the seven generators $S^{01},\dots,S^{07}$, which commute with $B$, which are anti-Hermitian, and which satisfy the Krein condition?

**Exercise 8.9.** A toy with one positive-energy level (energy $E$, operator $b$) and one negative-energy level (energy $-E$, operator $d^\ast$) has $H=E\,b^\ast b-E\,dd^\ast$. Find the energy of the vacuum before normal ordering and the normal-ordered Hamiltonian.

**Exercise 8.10.** For EXP-5 with $m=1$ and $q=0.1$ compute $t_\ast=\ln(m/q)$ and $E_0=\sqrt{m^2-q^2}$, and compare with the values quoted in Section 8.13.

**Exercise 8.11.** A two-dimensional toy: $B=\mathrm{diag}(1,-1)$ and $h=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$. Show $h^\dagger B=Bh$ and $h^2=-1$, solve $i\dot u=hu$ with $u(0)=(1,0)^T$, and compute $u^\dagger u$ and $u^\dagger Bu$ as functions of time.

### 8.17 Answers to the exercises

**Answer 8.1.** $bb^\dagger=\mathrm{diag}(1,0)$ and $b^\dagger b=\mathrm{diag}(0,1)$ add to the identity; $(b^\dagger)^2=\begin{pmatrix}0&0\\1&0\end{pmatrix}\begin{pmatrix}0&0\\1&0\end{pmatrix}=0$. $N=\mathrm{diag}(0,1)$ has the eigenvalues 0 and 1.

**Answer 8.2.** $b_0^\dagger|01\rangle=b_0^\dagger b_1^\dagger|0\rangle=|11\rangle$; $b_1b_0^\dagger|01\rangle=b_1|11\rangle=-|10\rangle$ (Section 8.4); $b_0^\dagger b_1|01\rangle=b_0^\dagger|00\rangle=|10\rangle$. The sum is 0.

**Answer 8.3.** The left derivative with respect to $\theta^\ast$ gives $2i\dot\theta-\omega\theta=0$, that is $i\dot\theta=\tfrac\omega2\theta$. Here $K=2i$, so $\{\theta,\theta^\dagger\}=i/(2i)=\tfrac12$. With $A=\tfrac12$ the computation of Section 8.6 gives $[H,\theta]=-A\omega\theta=-\tfrac\omega2\theta$ and $\dot\theta=i[H,\theta]=-\tfrac{i\omega}2\theta$, the same equation.

**Answer 8.4.** $B^\dagger=\bigl(-iC\gamma^4\bigr)^\dagger=i(\gamma^4)^TC^T=-i\gamma^4C=-iC\gamma^4=B$. $B^2=-C\gamma^4C\gamma^4=-C^2(\gamma^4)^2=-(1)(-1)=1$.

**Answer 8.5.** (a) $E^2=4+1-4=1$: oscillation with frequency 1, although $h$ is not Hermitian. (b) $E^2=1+1-1-1=0$ with $h\ne0$: linear growth. (c) $E^2=1-9=-8$: exponential growth with $\kappa=\sqrt8=2\sqrt2\approx2.83$.

**Answer 8.6.** $(-i\gamma^4)^2=-(\gamma^4)^2=1$, $(\gamma^4\gamma^5)^2=-(\gamma^4)^2(\gamma^5)^2=-(-1)(-1)=-1$, and the cross terms cancel because $\{\gamma^4,\gamma^4\gamma^5\}=0$. So $h^2=1-1=0$, and $u(x_4)=e^{-ihx_4}u(0)=(1-ihx_4)u(0)$, which grows linearly unless $hu(0)=0$.

**Answer 8.7.** Components: $u_0=\tfrac12$, $u_4=\tfrac12$, $u_9=\tfrac i2$, $u_{13}=-\tfrac i2$. $(\gamma^4u_-)_0=-u_{13}=\tfrac i2$, so $(-i\gamma^4u_-)_0=\tfrac12$; $(\gamma^4u_-)_4=u_9=\tfrac i2$, giving $\tfrac12$; $(\gamma^4u_-)_9=-u_4=-\tfrac12$, giving $\tfrac i2$; $(\gamma^4u_-)_{13}=u_0=\tfrac12$, giving $-\tfrac i2$. So $-i\gamma^4u_-=u_-$. $(Cu_-)_0=-u_4=-\tfrac12$, $(Cu_-)_4=-u_0=-\tfrac12$, $(Cu_-)_9=u_{13}=-\tfrac i2$, $(Cu_-)_{13}=u_9=\tfrac i2$: $Cu_-=-u_-$. Hence $u_-^\dagger u_-=4\cdot\tfrac14=1$, $u_-^\dagger Bu_-=u_-^\dagger C(-i\gamma^4)u_-=u_-^\dagger Cu_-=-1$, and $u_-^\dagger(-i\gamma^4)u_-=u_-^\dagger u_-=1$.

**Answer 8.8.** Commuting with $B$: $S^{01},S^{02},S^{03},S^{04}$ (both indices $\le4$); $S^{05},S^{06},S^{07}$ anticommute. Anti-Hermitian: $S^{01},S^{02},S^{03}$ (both indices $\le3$); the other four are Hermitian. Krein condition: $S^{01},S^{02},S^{03}$ (anti-Hermitian and commuting) and $S^{05},S^{06},S^{07}$ (Hermitian and anticommuting); $S^{04}$ fails it.

**Answer 8.9.** $dd^\ast=1-d^\ast d$, so $H=E\,b^\ast b+E\,d^\ast d-E$. The vacuum ($b|0\rangle=d|0\rangle=0$) has energy $-E$, the energy of the filled level. The normal-ordered Hamiltonian is $E(b^\ast b+d^\ast d)\ge0$.

**Answer 8.10.** $t_\ast=\ln10\approx2.302585$ and $E_0=\sqrt{0.99}\approx0.994987$, the values of Section 8.13 (from `artifacts/dirac16complex/numerics/exp5/summary.json`).

**Answer 8.11.** $h^\dagger=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, $h^\dagger B=\begin{pmatrix}0&1\\1&0\end{pmatrix}=Bh$, and $h^2=-1$, so $E^2=-1$ and $\kappa=1$. Then $u(t)=(\cosh t-ih\sinh t)u(0)=(\cosh t,\ i\sinh t)^T$. The Hilbert norm $u^\dagger u=\cosh^2t+\sinh^2t=\cosh2t$ grows exponentially, while the Krein norm $u^\dagger Bu=\cosh^2t-\sinh^2t=1$ stays constant: the pattern of EXP-5 in two dimensions.
