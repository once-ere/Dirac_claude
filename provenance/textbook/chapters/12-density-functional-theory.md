## 12. Many-body quantum mechanics and density functional theory from zero

### 12.1 What this chapter is for

Chapter 13 computes the lowest-energy state (the **ground state**) and the first excited state of a finite number $N$ of dirac16complex quanta that sit in the primordial gravitational field of the notebook and interact with each other. The tool is **density functional theory** (DFT) in the form invented by Kohn and Sham. This chapter builds that tool from zero, for ordinary non-relativistic particles first, because every idea is easier to see there. Nothing in this chapter is specific to dirac16complex; Chapter 13 transfers each step to the 16-component field.

Why is a special tool needed at all? A single quantum particle in three-dimensional space is described by a complex function $\psi(\mathbf r)$ of three variables. If we store it on a grid with 10 points per coordinate we need $10^3$ complex numbers. Two particles need a function of 6 variables, $10^6$ numbers; ten particles need $10^{30}$ numbers, more than any computer can hold. This growth, by a factor $10^3$ for every added particle, is called the **exponential wall** of the many-body problem. DFT climbs over the wall by working with the **density** $n(\mathbf r)$, the expected number of particles per unit volume at the point $\mathbf r$: a function of three variables, whatever $N$ is. The price is that one ingredient, the **exchange–correlation energy**, is not known exactly and must be approximated. We will see exactly where the approximation enters and what it is.

**Plan.** Sections 12.2 to 12.8 are quantum mechanics of many identical fermions: wave functions, the Pauli principle, Slater determinants, creation and annihilation operators, and the Hartree–Fock approximation, with a small example that can be solved exactly (Section 12.8). Sections 12.9 to 12.13 are density functional theory proper: the Hohenberg–Kohn theorems, functional derivatives, the Kohn–Sham equations, the local density approximation and the numerical self-consistency loop. Section 12.14 extends everything to a finite temperature (Mermin's functional), and Section 12.15 treats excited states: the Kohn–Sham gap, particle–hole excitations and the Delta-SCF method. Section 12.16 lists what was proved and what was assumed; exercises with full answers close the chapter.

**Units and counting.** In Sections 12.2 to 12.15 we use **atomic units**: Planck's constant divided by $2\pi$, the electron mass and the electron charge are set to 1 ($\hbar=m_e=e=1$), so the kinetic energy operator of one particle is $-\tfrac12\nabla^2$ and the Coulomb repulsion of two electrons at distance $r$ is $1/r$. As everywhere in this book we count from 0: the $N$ particles are numbered $0,1,\dots,N-1$, and so are the orbitals.

### 12.2 One quantum particle: states, operators and the variational principle

**States.** The state of one particle is a complex-valued function $\psi(\mathbf r)$, the **wave function**. Its squared modulus $|\psi(\mathbf r)|^2=\psi^*(\mathbf r)\psi(\mathbf r)$ is the probability per unit volume of finding the particle at $\mathbf r$, so a physical state is **normalized**: $\int|\psi|^2\,d^3r=1$. Two states are compared with the **inner product**

$$
\langle\varphi|\psi\rangle=\int\varphi^*(\mathbf r)\,\psi(\mathbf r)\,d^3r ,
$$

which is linear in $\psi$, antilinear in $\varphi$ (a factor $c$ in $\varphi$ comes out as $c^*$), and satisfies $\langle\psi|\varphi\rangle=\langle\varphi|\psi\rangle^*$ and $\langle\psi|\psi\rangle\ge0$. Two states with $\langle\varphi|\psi\rangle=0$ are **orthogonal**. It often helps to replace space by a finite set of points: then a state is a column of $M$ complex numbers $\psi=(\psi_0,\dots,\psi_{M-1})^T$ and $\langle\varphi|\psi\rangle=\sum_x\varphi_x^*\psi_x=\varphi^\dagger\psi$ (the dagger means complex conjugate and transpose, Chapter 1). Everything below holds in both pictures.

**Operators.** An observable quantity is represented by a linear **operator** $A$, a rule that turns a state into a state and satisfies $A(c_0\psi+c_1\varphi)=c_0A\psi+c_1A\varphi$. On a finite grid an operator is an $M\times M$ matrix. The operator is **Hermitian** (self-adjoint) if $\langle\varphi|A\psi\rangle=\langle A\varphi|\psi\rangle$ for all states; for a matrix this means $A^\dagger=A$. The **expectation value** of $A$ in the normalized state $\psi$ is $\langle A\rangle=\langle\psi|A\psi\rangle$, the average of many measurements. The energy operator of one particle in an external potential $v(\mathbf r)$ is the **Hamiltonian**

$$
h=-\tfrac12\nabla^2+v(\mathbf r),\qquad \nabla^2=\partial_x^2+\partial_y^2+\partial_z^2 .
$$

A state with $h\psi=\varepsilon\psi$ is a **stationary state** (an eigenstate) with energy $\varepsilon$.

**Two facts about Hermitian operators.** (i) The eigenvalues are real: if $A\psi=a\psi$ with $\psi\ne0$, then $a\langle\psi|\psi\rangle=\langle\psi|A\psi\rangle=\langle A\psi|\psi\rangle=a^*\langle\psi|\psi\rangle$, so $a=a^*$. (ii) Eigenvectors with different eigenvalues are orthogonal: if $A\psi=a\psi$ and $A\varphi=b\varphi$ with $a\ne b$, then $b\langle\psi|\varphi\rangle=\langle\psi|A\varphi\rangle=\langle A\psi|\varphi\rangle=a\langle\psi|\varphi\rangle$, so $\langle\psi|\varphi\rangle=0$. For a Hermitian matrix one can always choose an orthonormal basis of eigenvectors (the spectral theorem of linear algebra, Chapter 1).

**Outer products and functions of an operator.** We also write $|\psi\rangle$ for the state $\psi$ (a **ket**). For two states $\varphi,\chi$ the symbol $|\varphi\rangle\langle\chi|$ is the operator $\psi\mapsto\varphi\,\langle\chi|\psi\rangle$; on a grid it is the matrix $\varphi\chi^\dagger$ (a column times a row), and its trace is $\mathrm{Tr}\,|\varphi\rangle\langle\chi|=\chi^\dagger\varphi=\langle\chi|\varphi\rangle$ (we write $\mathrm{Tr}$ for the trace $\mathrm{tr}$ of Chapter 1). A Hermitian $A$ with orthonormal eigenvectors $|i\rangle$ and eigenvalues $a_i$ is $A=\sum_ia_i|i\rangle\langle i|$: both sides give $a_j|j\rangle$ on every eigenvector $|j\rangle$, and the eigenvectors form a basis. A function of $A$ is defined in the same way, $f(A)=\sum_if(a_i)|i\rangle\langle i|$. For $f=\exp$ this agrees with the power series of Chapters 8 and 10, because $A^k=\sum_ia_i^k|i\rangle\langle i|$. For a Hermitian $B$ with eigenvalues $b_i>0$ the logarithm is $\ln B=\sum_i\ln b_i\,|i\rangle\langle i|$; if some $b_i=0$, only the product $B\ln B=\sum_ib_i\ln b_i\,|i\rangle\langle i|$ is used, with the convention $0\ln0=0$ (the limit of $b\ln b$ as $b\to0$), so that $\mathrm{Tr}(B\ln B)=\sum_ib_i\ln b_i$. The same definitions apply to operators on many-particle states (Section 12.14).

**Worked example.** Two grid points (“two sites”) with the hopping matrix

$$
h=\begin{pmatrix}0&-t\\-t&0\end{pmatrix},\qquad t>0 .
$$

The characteristic polynomial is $\det(h-\varepsilon)=\varepsilon^2-t^2$, so $\varepsilon=\pm t$. For $\varepsilon=-t$ the equation $(h+t)\psi=0$ gives $\psi_0=\psi_1$, normalized $\psi_b=(1,1)^T/\sqrt2$ (the **bonding** orbital); for $\varepsilon=+t$ it gives $\psi_a=(1,-1)^T/\sqrt2$ (antibonding). Check: $\psi_b^\dagger\psi_a=(1-1)/2=0$.

**The variational principle.** Let $\psi_0,\psi_1,\dots$ be an orthonormal basis of eigenvectors of a Hermitian $H$ with eigenvalues $E_0\le E_1\le\dots$. Every normalized state is $\psi=\sum_nc_n\psi_n$ with $\sum_n|c_n|^2=1$, and

$$
\langle\psi|H\psi\rangle=\sum_n|c_n|^2E_n\ \ge\ E_0\sum_n|c_n|^2=E_0 ,
$$

with equality exactly when only the $c_n$ with $E_n=E_0$ are nonzero. So **the ground-state energy is the minimum of the energy expectation value over all normalized states**, and the minimizers are the ground states. Every method of this chapter is an application of this one inequality.

**Internal states.** Real particles carry an internal label besides their position. For an electron it is the spin $\sigma\in\{\uparrow,\downarrow\}$, two values. We collect position and label into one symbol $x=(\mathbf r,\sigma)$ and write $\int dx=\sum_\sigma\int d^3r$. A particle with $g$ internal states has a wave function $\psi(\mathbf r,\sigma)$ with $\sigma=0,\dots,g-1$. For the quanta of dirac16complex in the sector studied in Chapter 13 the analogous number is $g=8$: eight states of positive energy for each momentum (Chapter 8).

### 12.3 Many identical fermions and the Pauli principle

**The many-particle wave function.** $N$ particles are described by one complex function of all their coordinates, $\Psi(x_0,x_1,\dots,x_{N-1})$. The number $|\Psi(x_0,\dots,x_{N-1})|^2$ is the probability density of finding particle 0 at $x_0$, particle 1 at $x_1$, and so on, and $\int|\Psi|^2\,dx_0\cdots dx_{N-1}=1$.

**Identical particles.** All electrons are identical: no experiment can tell “electron 0” from “electron 1”. Hence $|\Psi|^2$ must be unchanged when two arguments are swapped. Nature realizes this in two ways. For **bosons** $\Psi$ itself is unchanged; for **fermions** it changes sign:

$$
\Psi(\dots,x_i,\dots,x_j,\dots)=-\Psi(\dots,x_j,\dots,x_i,\dots)\qquad(\text{fermions}).
$$

Electrons, protons and neutrons are fermions, and so are the quanta of dirac16complex: its components are anticommuting Grassmann fields (Chapters 5 and 8), and anticommuting fields describe fermions. Which particles are fermions is an input from experiment and from the spin–statistics connection of relativistic quantum field theory; in this book it is an **assumption about the field**, built into dirac16complex by choosing Grassmann components.

**The Pauli principle.** Put $x_i=x_j=x$ in the antisymmetry rule: $\Psi(\dots,x,\dots,x,\dots)=-\Psi(\dots,x,\dots,x,\dots)$, so $\Psi=0$ there. Two identical fermions are never found with the same position and the same internal label.

**The many-body Hamiltonian.** For $N$ particles in an external potential $v$ with a pair interaction $w$,

$$
\hat H=\sum_{i=0}^{N-1}\Bigl[-\tfrac12\nabla_i^2+v(\mathbf r_i)\Bigr]+\sum_{0\le i<j\le N-1}w(\mathbf r_i,\mathbf r_j),
$$

where $\nabla_i$ acts on the coordinates of particle $i$. For electrons $w=1/|\mathbf r_i-\mathbf r_j|$. We write $\hat H=\hat T+\hat V+\hat W$ for the three parts (kinetic, external, interaction). Only $\hat V$ distinguishes one system from another: atoms, molecules and solids with $N$ electrons all share the same $\hat T+\hat W$. This observation is the seed of DFT.

**The density.** The density is the expected number of particles per unit volume at $\mathbf r$:

$$
n(\mathbf r)=N\sum_\sigma\int|\Psi(\mathbf r\sigma,x_1,\dots,x_{N-1})|^2\,dx_1\cdots dx_{N-1}.
$$

The factor $N$ appears because any of the $N$ identical particles may be the one at $\mathbf r$, and antisymmetry makes all $N$ choices give the same integral. Integrating over $\mathbf r$ gives $\int n\,d^3r=N$. The expectation value of the external energy needs only the density: $\langle\Psi|\hat V\Psi\rangle=\int v(\mathbf r)\,n(\mathbf r)\,d^3r$, because each term $v(\mathbf r_i)$ contributes the same integral, $N$ times.

### 12.4 Slater determinants

**Two particles.** Take two orthonormal one-particle states (**orbitals**) $\varphi_a$ and $\varphi_b$. The product $\varphi_a(x_0)\varphi_b(x_1)$ is not antisymmetric, but the combination

$$
\Phi(x_0,x_1)=\frac1{\sqrt2}\bigl[\varphi_a(x_0)\varphi_b(x_1)-\varphi_b(x_0)\varphi_a(x_1)\bigr]
=\frac1{\sqrt2}\det\begin{pmatrix}\varphi_a(x_0)&\varphi_b(x_0)\\ \varphi_a(x_1)&\varphi_b(x_1)\end{pmatrix}
$$

is. Its norm is $\tfrac12[1+1-2\,\mathrm{Re}(\langle\varphi_a|\varphi_b\rangle\langle\varphi_b|\varphi_a\rangle)]=1$ for orthonormal orbitals, and it vanishes identically if $\varphi_a=\varphi_b$: two fermions cannot occupy the same orbital. This is the form of the Pauli principle that chemists and solid-state physicists use.

**$N$ particles.** For $N$ orthonormal orbitals $\varphi_0,\dots,\varphi_{N-1}$ the **Slater determinant** is

$$
\Phi(x_0,\dots,x_{N-1})=\frac1{\sqrt{N!}}\det\bigl[\varphi_a(x_i)\bigr]_{i,a=0}^{N-1}
=\frac1{\sqrt{N!}}\sum_{P}\mathrm{sgn}(P)\prod_{i=0}^{N-1}\varphi_{P(i)}(x_i),
$$

where the sum runs over the $N!$ permutations $P$ of $\{0,\dots,N-1\}$ and $\mathrm{sgn}(P)=\pm1$ is the sign of the permutation. Three properties follow from the rules for determinants. (i) Swapping two arguments $x_i,x_j$ swaps two rows, which changes the sign: $\Phi$ is antisymmetric. (ii) Two equal orbitals make two columns equal, and the determinant vanishes. (iii) $\Phi$ is normalized. For (iii) write $|\Phi|^2$ as a double sum over permutations $P,P'$ and integrate: the integral of $\prod_i\varphi^*_{P'(i)}(x_i)\varphi_{P(i)}(x_i)$ is $\prod_i\langle\varphi_{P'(i)}|\varphi_{P(i)}\rangle$, which is 1 if $P'=P$ and 0 otherwise (at least one factor is an inner product of two different orthonormal orbitals). So $\int|\Phi|^2=\frac1{N!}\sum_P1=1$.

**The density of a Slater determinant** is the sum of the orbital densities,

$$
n(x)=\sum_{a=0}^{N-1}|\varphi_a(x)|^2 .
$$

(Insert the permutation sum into the definition of $n$ and integrate over $x_1,\dots,x_{N-1}$: by orthonormality only $P'=P$ survives, and the remaining factor for the variable $x_0$ is $|\varphi_{P(0)}(x_0)|^2$; each orbital $a$ appears as $P(0)$ in $(N-1)!$ permutations, and $N\cdot(N-1)!/N!=1$.)

**Worked example.** Let “space” consist of three points $x\in\{0,1,2\}$ (no spin) and take the orthonormal orbitals $\varphi_0=(1,0,0)^T$ and $\varphi_1=(0,1,1)^T/\sqrt2$. The two-particle Slater determinant has the values

| $(x_0,x_1)$ | $(0,1)$ | $(0,2)$ | $(1,2)$ | $(1,0)$ | $(2,0)$ |
| --- | --- | --- | --- | --- | --- |
| $\Phi(x_0,x_1)$ | $1/2$ | $1/2$ | $0$ | $-1/2$ | $-1/2$ |

and $\Phi(x,x)=0$ on the diagonal. For example $\Phi(0,1)=\tfrac1{\sqrt2}[\varphi_0(0)\varphi_1(1)-\varphi_1(0)\varphi_0(1)]=\tfrac1{\sqrt2}\cdot\tfrac1{\sqrt2}=\tfrac12$, and $\Phi(1,2)=\tfrac1{\sqrt2}[0\cdot\tfrac1{\sqrt2}-\tfrac1{\sqrt2}\cdot0]=0$. The sum of $|\Phi|^2$ over all nine ordered pairs is $4\cdot\tfrac14=1$, and the density $n(x)=N\sum_{x_1}|\Phi(x,x_1)|^2$ is $n=(2\cdot\tfrac12,\ 2\cdot\tfrac14,\ 2\cdot\tfrac14)=(1,\tfrac12,\tfrac12)$, which equals $|\varphi_0|^2+|\varphi_1|^2$ as it must, with total 2.

A general antisymmetric $N$-particle state is not one Slater determinant but a linear combination of many (all determinants built from a complete orbital basis form a basis of the antisymmetric states). A single determinant is the simplest possible many-fermion state, the state of $N$ **independent** fermions. The whole of Kohn–Sham theory rests on the fact that a single determinant can nevertheless carry the exact density.

### 12.5 Creation and annihilation operators

Slater determinants are cumbersome to write. A shorter bookkeeping, called **second quantization**, labels a determinant only by which orbitals are occupied. It is the same formalism that Chapter 8 uses for the quantized dirac16complex field, here in its simplest form.

**Occupation numbers.** Fix an orthonormal basis of orbitals $\varphi_0,\varphi_1,\dots,\varphi_{M-1}$ (finite, to keep things simple). A Slater determinant built from some of them is fixed, up to sign, by the list of **occupation numbers** $n_p\in\{0,1\}$ ($p=0,\dots,M-1$): $n_p=1$ if $\varphi_p$ is used. We write it $|n_0n_1\cdots n_{M-1}\rangle$ and fix the sign by listing the occupied orbitals in increasing order of $p$ as the columns of the determinant. The state with no particle at all is the **vacuum** $|0\rangle=|00\cdots0\rangle$.

**The operators.** The **creation operator** $a_p^\dagger$ adds a particle in orbital $p$ and the **annihilation operator** $a_p$ removes one:

$$
\begin{aligned}
a_p^\dagger|\cdots n_p\cdots\rangle&=(-1)^{\nu_p}\,(1-n_p)\,|\cdots n_p{+}1\cdots\rangle,\\
a_p|\cdots n_p\cdots\rangle&=(-1)^{\nu_p}\,n_p\,|\cdots n_p{-}1\cdots\rangle,\qquad \nu_p=\sum_{q<p}n_q .
\end{aligned}
$$

The factor $(1-n_p)$ makes $a_p^\dagger$ give zero on an occupied orbital (Pauli), the factor $n_p$ makes $a_p$ give zero on an empty one, and the sign $(-1)^{\nu_p}$ is the sign of the determinant when the new column $p$ is moved past the $\nu_p$ occupied columns in front of it. From these definitions follow the **anticommutation relations**

$$
\{a_p,a_q^\dagger\}=a_pa_q^\dagger+a_q^\dagger a_p=\delta_{pq},\qquad \{a_p,a_q\}=\{a_p^\dagger,a_q^\dagger\}=0 .
$$

Proof for $p=q$: on a state with $n_p=0$, $a_pa_p^\dagger$ gives the state back (the two signs are equal and multiply to $+1$) and $a_p^\dagger a_p$ gives 0; with $n_p=1$ it is the other way round; in both cases the sum is 1. For $p<q$: $a_p$ or $a_p^\dagger$ changes $n_p$, which changes the sign factor $(-1)^{\nu_q}$ of the other operator, so the two orders differ exactly by a sign and the anticommutator vanishes. The same argument gives $\{a_p,a_q\}=0$; in particular $a_p^\dagger a_p^\dagger=0$, the Pauli principle again. The relations $\{a_p,a_q\}=\{a_p^\dagger,a_q^\dagger\}=0$ (in particular $(a_p^\dagger)^2=0$) are the rule of Grassmann numbers (Chapter 5); the remaining relation $\{a_p,a_q^\dagger\}=\delta_{pq}$ has no Grassmann analogue: it is what canonical quantization of an anticommuting field produces (Chapter 8). This is why an anticommuting field describes fermions.

The **number operator** $\hat n_p=a_p^\dagger a_p$ gives $n_p$ on $|\cdots n_p\cdots\rangle$, and $\hat N=\sum_p\hat n_p$ counts all particles. A determinant with the occupied set $O=\{p_0<p_1<\dots<p_{N-1}\}$ is $|\Phi\rangle=a_{p_0}^\dagger a_{p_1}^\dagger\cdots a_{p_{N-1}}^\dagger|0\rangle$.

**Operators of the many-body theory.** A one-body operator $\sum_iA(i)$, one copy of the one-particle operator $A$ for each particle, becomes

$$
\hat A=\sum_{p,q}A_{pq}\,a_p^\dagger a_q,\qquad A_{pq}=\langle\varphi_p|A\varphi_q\rangle .
$$

Reason: applied to a determinant, $\sum_iA(i)$ replaces one occupied orbital $\varphi_q$ at a time by $A\varphi_q=\sum_p\varphi_pA_{pq}$ and adds the results; “remove $q$, put $p$, with weight $A_{pq}$” is exactly what $A_{pq}a_p^\dagger a_q$ does, including the sign. The pair interaction $\sum_{i<j}w(i,j)$ is represented by

$$
\begin{aligned}
&\hat W=\tfrac12\sum_{p,q,r,s}w_{pqrs}\,a_p^\dagger a_q^\dagger a_sa_r,\\
&w_{pqrs}=\int\!\!\int\varphi_p^*(x)\,\varphi_q^*(x')\,w(x,x')\,\varphi_r(x)\,\varphi_s(x')\,dx\,dx' :
\end{aligned}
$$

the operator removes an occupied pair $(r,s)$ and puts $(p,q)$ in its place; the factor $\tfrac12$ compensates for counting each unordered pair twice, and the order $a_sa_r$ (with $s$ and $r$ reversed) makes the direct term come with a plus sign: $a_sa_r$ removes $r$ first and then $s$, and $a_p^\dagger a_q^\dagger$ puts back $q$ first and then $p$, the mirror order, so for $p=r$, $q=s$ the two sign factors cancel. This is a sketch; what we actually use is that $\hat W$ gives the correct energy in every determinant, which Section 12.6 derives directly from the permutation sum and checks against the expectation values below.

**Expectation values in a determinant.** Let $|\Phi\rangle$ be the determinant with occupied set $O$ in the orbital basis. Then

$$
\begin{aligned}
&\langle\Phi|a_p^\dagger a_q|\Phi\rangle=\delta_{pq}\,[p\in O],\\
&\langle\Phi|a_p^\dagger a_q^\dagger a_sa_r|\Phi\rangle=[p\in O]\,[q\in O]\,\bigl(\delta_{pr}\delta_{qs}-\delta_{ps}\delta_{qr}\bigr),
\end{aligned}
$$

where $[p\in O]$ is 1 if $p$ is occupied and 0 otherwise. The first formula holds because $a_q$ removes $q$ and $a_p^\dagger$ must put back the same orbital to return to $|\Phi\rangle$ (states with different occupations are orthogonal), and then $a_p^\dagger a_p=\hat n_p$. For the second, the pair removed and the pair added must coincide, $\{p,q\}=\{r,s\}$ with $p\ne q$. If $p=r$ and $q=s$, then $a_p^\dagger a_q^\dagger a_qa_p=a_p^\dagger\hat n_qa_p=\hat n_q\hat n_p$ (for $q\ne p$ the operator $\hat n_q$ commutes with $a_p$ and $a_p^\dagger$), which gives $[p\in O][q\in O]$. If $p=s$ and $q=r$, one anticommutation, $a_pa_q=-a_qa_p$, gives $-\hat n_p\hat n_q$. Both formulas are summarized by the **one-body density matrix** $\rho=\sum_{a\in O}|\varphi_a\rangle\langle\varphi_a|$, whose matrix elements are $\rho_{qp}=\langle\Phi|a_p^\dagger a_q|\Phi\rangle$:

$$
\langle a_p^\dagger a_q\rangle=\rho_{qp},\qquad
\langle a_p^\dagger a_q^\dagger a_sa_r\rangle=\rho_{rp}\,\rho_{sq}-\rho_{sp}\,\rho_{rq}.
$$

Both sides of these identities change in the same way under a unitary change of the orbital basis, so they hold in every orthonormal basis, not only in the one in which $\Phi$ is a single determinant. This is **Wick's theorem** for a Slater determinant: every expectation value is a sum of products of the density matrix. The same statement holds for a thermal ensemble of non-interacting fermions, with $\rho=\sum_af_a|\varphi_a\rangle\langle\varphi_a|$ and occupation probabilities $0\le f_a\le1$: in such an ensemble the occupations of different orbitals are independent (Section 12.14 derives this), so $\langle\hat n_p\hat n_q\rangle=f_pf_q$ for $p\ne q$, and the same two-line proof applies. In real space $\rho(x,x')=\sum_af_a\varphi_a(x)\varphi_a^*(x')$, and its diagonal $\rho(x,x)$ is the density $n(x)$.

### 12.6 The energy of a Slater determinant: direct and exchange terms

**The energy from the permutation sum.** We compute the energy of a determinant directly from its definition, as we computed its density in Section 12.4. For the pair interaction,

$$
\begin{aligned}
&\Bigl\langle\Phi\Bigm|\sum_{i<j}w(x_i,x_j)\Bigm|\Phi\Bigr\rangle\\
&\quad=\frac1{N!}\sum_{P,P'}\mathrm{sgn}(P)\,\mathrm{sgn}(P')\sum_{i<j}\int\prod_k\varphi^*_{P'(k)}(x_k)\;w(x_i,x_j)\prod_k\varphi_{P(k)}(x_k)\;dx_0\cdots dx_{N-1}.
\end{aligned}
$$

In the term $(i,j)$ the integral over each $x_k$ with $k\ne i,j$ is $\langle\varphi_{P'(k)}|\varphi_{P(k)}\rangle$, which vanishes unless $P'(k)=P(k)$. Then $P'$ and $P$ agree on every number except $i$ and $j$, so either $P'=P$, or $P'=P\circ(ij)$, the permutation with $P'(i)=P(j)$ and $P'(j)=P(i)$, whose sign is $\mathrm{sgn}(P')=-\mathrm{sgn}(P)$. With $a=P(i)$ and $b=P(j)$ the first case gives $w_{abab}$ and the second gives $-w_{baab}$; renaming $x\leftrightarrow x'$ in the integral and using $w(x,x')=w(x',x)$ shows $w_{baab}=w_{abba}$. Each ordered pair $(a,b)$ of different occupied orbitals arises from the $N(N-1)/2$ pairs $i<j$, each with the $(N-2)!$ permutations that have $P(i)=a$ and $P(j)=b$, and $\frac1{N!}\cdot\frac{N(N-1)}2\cdot(N-2)!=\tfrac12$. Terms with $a=b$ would contribute $w_{aaaa}-w_{aaaa}=0$, so they may be included. The one-body part is simpler: in the term $i$ the integrals over all $x_k$ with $k\ne i$ force $P'=P$, and each orbital $a$ appears as $P(i)$ in $(N-1)!$ permutations for each of the $N$ values of $i$, with $N\cdot(N-1)!/N!=1$. Together,

$$
\langle\Phi|\hat H|\Phi\rangle=\sum_{a\in O}\langle\varphi_a|h\varphi_a\rangle
+\tfrac12\sum_{a,b\in O}\bigl(w_{abab}-w_{abba}\bigr),\qquad h=-\tfrac12\nabla^2+v .
$$

**The same result from second quantization.** Wick's theorem of Section 12.5 gives it in two lines: $\langle\Phi|\hat A|\Phi\rangle=\sum_{p,q}A_{pq}\,\delta_{pq}[p\in O]=\sum_{a\in O}A_{aa}$, and $\langle\Phi|\hat W|\Phi\rangle=\tfrac12\sum_{p,q,r,s}w_{pqrs}[p\in O][q\in O](\delta_{pr}\delta_{qs}-\delta_{ps}\delta_{qr})=\tfrac12\sum_{a,b\in O}(w_{abab}-w_{abba})$. This is the check announced in Section 12.5: in every determinant the operators $\hat A$ and $\hat W$ give the energies of $\sum_iA(i)$ and $\sum_{i<j}w(i,j)$.

The first sum is the kinetic plus external energy of independent particles. The second sum has two parts. Writing out the integrals and using $\sum_a\varphi_a(x)\varphi_a^*(x')=\rho(x,x')$,

$$
\begin{aligned}
E_H&=\tfrac12\sum_{a,b}w_{abab}=\tfrac12\int\!\!\int n(x)\,w(x,x')\,n(x')\,dx\,dx',\\
E_x&=-\tfrac12\sum_{a,b}w_{abba}=-\tfrac12\int\!\!\int|\rho(x,x')|^2\,w(x,x')\,dx\,dx' .
\end{aligned}
$$

$E_H$ is the **Hartree energy**: the classical electrostatic energy of the charge cloud $n$ with itself. $E_x$ is the **exchange energy** (Fock term). It has no classical analogue; it comes from the antisymmetry of $\Phi$ and lowers the energy for a repulsive $w$. Three remarks.

1. **No self-interaction.** In $E_H$ the terms $a=b$ describe each particle repelling its own charge cloud, which is unphysical. In $E_x$ the terms $a=b$ are exactly the same numbers with a minus sign, so they cancel.
2. **Exchange acts only between equal internal labels.** If every orbital has a definite spin, then $\rho(\mathbf r\sigma,\mathbf r'\sigma')=0$ for $\sigma\ne\sigma'$, and $E_x$ couples only particles with the same spin (for a spin-independent $w$).
3. **Double counting.** Adding the orbital energies of Section 12.7 counts every pair twice, which is why $E_H$ and $E_x$ will be subtracted once from $\sum_a\varepsilon_a$.

**Contact interaction.** Let the particles have $g$ internal states and interact only when they are at the same point, independently of the label: $w(x,x')=g_c\,\delta(\mathbf r-\mathbf r')$ with a strength $g_c$. Then, with $n_\sigma(\mathbf r)=\rho(\mathbf r\sigma,\mathbf r\sigma)$ and orbitals of definite label,

$$
E_H=\frac{g_c}2\int n(\mathbf r)^2\,d^3r,\qquad E_x=-\frac{g_c}2\int\sum_{\sigma}n_\sigma(\mathbf r)^2\,d^3r .
$$

Two facts follow. First, the exchange energy of a contact interaction is **exactly local**: it is an integral over one point of a function of the densities at that point, although the general exchange integral involves two points. Second, if all $g$ labels are equally occupied, $n_\sigma=n/g$, then $\sum_\sigma n_\sigma^2=n^2/g$ and

$$
E_x=-\frac1g\,E_H\qquad(\text{contact interaction, equal occupation of the }g\text{ labels}).
$$

For electrons ($g=2$) this says $E_H+E_x=g_c\int n_\uparrow n_\downarrow\,d^3r$: two electrons of the same spin never meet at one point (Pauli), so only opposite spins feel a contact force, and exchange removes precisely the unphysical same-spin part of $E_H$. Chapter 13 finds the ratio $1/8$ for a filled shell of dirac16complex quanta, the case $g=8$ with a matrix-valued vertex.

### 12.7 The Hartree and Hartree–Fock equations

The **Hartree–Fock approximation** takes the best single determinant: it minimizes $\langle\Phi|\hat H|\Phi\rangle$ over all choices of $N$ orthonormal orbitals. By the variational principle (Section 12.2) the result $E_{HF}$ is an upper bound on the true ground-state energy $E_0$.

**Minimizing under a side condition: Lagrange multipliers.** The orbitals are not free: they must stay orthonormal. The standard tool for such problems, used again in Sections 12.10, 12.11 and 12.14, is the method of **Lagrange multipliers**. Take a real function $f(y_0,\dots,y_{m-1})$ of $m$ real variables and one side condition (a **constraint**) $c(y)=c_0$, and let $y^\ast$ be a minimum of $f$ among the points that satisfy it. To first order (Section 1.9) a small step $dy$ changes $f$ by $df=\sum_i(\partial f/\partial y_i)\,dy_i$ and $c$ by $dc=\sum_i(\partial c/\partial y_i)\,dy_i$. An allowed small step keeps $c=c_0$, so it satisfies $\sum_i(\partial c/\partial y_i)\,dy_i=0$ (this describes the allowed steps correctly where the gradient of $c$, the list of the $\partial c/\partial y_i$, is not zero; with several constraints, where their gradients are linearly independent; that such first-order steps can be completed to steps that keep the constraint exactly is the implicit function theorem of analysis, used without proof). At the minimum $df=0$ for every allowed step, since otherwise the step or the opposite step would lower $f$. Now define

$$
\lambda=\frac{\sum_i(\partial f/\partial y_i)(\partial c/\partial y_i)}{\sum_i(\partial c/\partial y_i)^2},\qquad r_i=\frac{\partial f}{\partial y_i}-\lambda\,\frac{\partial c}{\partial y_i} .
$$

Then $\sum_ir_i\,\partial c/\partial y_i=0$, so $dy_i=\epsilon r_i$ is an allowed step, and $0=df=\epsilon\sum_i(\partial f/\partial y_i)\,r_i=\epsilon\sum_i(r_i+\lambda\,\partial c/\partial y_i)\,r_i=\epsilon\sum_ir_i^2$ forces every $r_i=0$. Hence

$$
\frac{\partial f}{\partial y_i}=\lambda\,\frac{\partial c}{\partial y_i}\quad(\text{all }i),\qquad c(y)=c_0 .
$$

These are exactly the conditions that the **Lagrangian** $\mathcal L(y,\lambda)=f(y)-\lambda\,\bigl(c(y)-c_0\bigr)$ be stationary with respect to every $y_i$ and to $\lambda$: the constrained problem has become an unconstrained one with one more unknown, the **multiplier** $\lambda$. With several constraints $c_k(y)=c_{k,0}$ one takes one multiplier for each, $\mathcal L=f-\sum_k\lambda_k(c_k-c_{k,0})$, and the same argument, with $r$ the part of the gradient of $f$ that is orthogonal to all the gradients of the $c_k$, gives $\partial f/\partial y_i=\sum_k\lambda_k\,\partial c_k/\partial y_i$. A complex variable counts as two real ones (next paragraph), and a function of the values on a grid becomes a functional in the limit of a fine grid (Section 12.10).

*Example.* Minimize $f=y_0+y_1$ on the circle $y_0^2+y_1^2=1$. The conditions are $1=2\lambda y_0$ and $1=2\lambda y_1$, so $y_0=y_1=1/(2\lambda)$, and the constraint gives $2/(4\lambda^2)=1$, $\lambda=\pm1/\sqrt2$. The two stationary points $y_0=y_1=\pm1/\sqrt2$ are the maximum $f=\sqrt2$ and the minimum $f=-\sqrt2$ (with $\lambda=-1/\sqrt2$): the method finds all stationary points, and comparing their values picks the minimum.

*What the multiplier means.* Let $f^\ast(c_0)$ be the minimum for the constraint value $c_0$, attained at $y^\ast(c_0)$ with the multiplier $\lambda(c_0)$, and suppose that $y^\ast$ depends differentiably on $c_0$. By the chain rule and the conditions above,

$$
\frac{df^\ast}{dc_0}=\sum_i\frac{\partial f}{\partial y_i}\,\frac{dy^\ast_i}{dc_0}=\lambda\sum_i\frac{\partial c}{\partial y_i}\,\frac{dy^\ast_i}{dc_0}=\lambda\,\frac{d}{dc_0}\,c\bigl(y^\ast(c_0)\bigr)=\lambda ,
$$

because $c(y^\ast(c_0))=c_0$ for every $c_0$. The multiplier is the rate at which the constrained minimum changes with the constraint value. In the example the minimum on the circle $y_0^2+y_1^2=c_0$ is $f^\ast=-\sqrt{2c_0}$, whose derivative at $c_0=1$ is $-1/\sqrt2=\lambda$.

**How to vary a complex function.** A complex function $\varphi=u+iv$ has two real parts. Instead of varying $u$ and $v$ we may vary $\varphi$ and $\varphi^*$ as if they were independent, because $u=(\varphi+\varphi^*)/2$ and $v=(\varphi-\varphi^*)/(2i)$ are recovered from them; setting the derivative with respect to $\varphi^*$ to zero is equivalent to setting both real derivatives to zero (for a real-valued function of $\varphi$, the derivative with respect to $\varphi$ is the complex conjugate of the one with respect to $\varphi^*$). The precise definition of the derivative of a functional with respect to a function is given in Section 12.10; here we only need the rule “differentiate the integrand”.

**The Lagrangian.** The orbitals must stay orthonormal, so we add Lagrange multipliers $\Lambda_{ba}$ for the constraints $\langle\varphi_a|\varphi_b\rangle=\delta_{ab}$:

$$
\mathcal L=\sum_a\langle\varphi_a|h\varphi_a\rangle+\tfrac12\sum_{a,b}\bigl(w_{abab}-w_{abba}\bigr)-\sum_{a,b}\Lambda_{ba}\bigl(\langle\varphi_a|\varphi_b\rangle-\delta_{ab}\bigr).
$$

Differentiate with respect to $\varphi_a^*(x)$. The orbital $a$ appears in the first and in the second slot of $w_{abab}$ and $w_{abba}$; because $w(x,x')=w(x',x)$ the two contributions are equal, which cancels the $\tfrac12$. The result is

$$
\hat F\varphi_a=\sum_b\Lambda_{ba}\varphi_b,\qquad
(\hat F\varphi)(x)=h\varphi(x)+v_H(x)\,\varphi(x)-\int\rho(x,x')\,w(x,x')\,\varphi(x')\,dx',
$$

with the **Hartree potential** $v_H(x)=\int w(x,x')\,n(x')\,dx'$. $\hat F$ is the **Fock operator**. It depends on the occupied orbitals only through $\rho$, and $\rho$ does not change if the occupied orbitals are mixed among themselves by a unitary matrix $Q$ ($\varphi'_a=\sum_bQ_{ba}\varphi_b$), while the determinant only picks up the phase $\det Q$. The matrix $\Lambda_{ba}=\langle\varphi_b|\hat F\varphi_a\rangle$ is Hermitian, so we can choose $Q$ to diagonalize it. This gives the **canonical Hartree–Fock equations**

$$
\hat F\varphi_a=\varepsilon_a\varphi_a,\qquad a=0,\dots,N-1 .
$$

They look like one-particle Schrödinger equations, but $\hat F$ contains the unknown orbitals: the equations are **nonlinear** and are solved by iteration, starting from a guess and repeating until the orbitals no longer change (**self-consistency**, Section 12.13). For the ground state one usually occupies the $N$ eigenstates of $\hat F$ with the lowest $\varepsilon_a$ (the **aufbau** rule, from the German for “building up”). The older **Hartree approximation** keeps only $v_H$ and drops the exchange integral; it therefore keeps the self-interaction of remark 1 of Section 12.6.

**Total energy and double counting.** Summing the orbital energies, $\sum_a\varepsilon_a=\sum_a\langle\varphi_a|\hat F\varphi_a\rangle=\sum_a\langle\varphi_a|h\varphi_a\rangle+2E_H+2E_x$, so

$$
E_{HF}=\sum_{a\in O}\varepsilon_a-E_H-E_x .
$$

**Koopmans' theorem.** Remove the particle in orbital $a$ and keep the other orbitals frozen. The energy lost is $\langle\varphi_a|h\varphi_a\rangle$ plus all pair terms that contain $a$, $\sum_b(w_{abab}-w_{abba})$ (the ordered pairs $(a,b)$ and $(b,a)$ each carry the factor $\tfrac12$, and $w_{baba}=w_{abab}$, $w_{baab}=w_{abba}$). That is exactly $\langle\varphi_a|\hat F\varphi_a\rangle=\varepsilon_a$. So $-\varepsilon_a$ is the energy needed to remove a particle from orbital $a$ when the others do not relax. This gives the Hartree–Fock orbital energies a physical meaning; the Kohn–Sham analogue (Janak's theorem) appears in Section 12.15.

### 12.8 A worked example: two sites, two electrons

The smallest system in which interaction matters is a two-site model: two sites L and R, one orbital on each, hopping $t$ between them (the matrix of Section 12.2), and a repulsion $U>0$ when two electrons sit on the same site. We put in two electrons with opposite spins.

**Exact solution.** With opposite spins the two-electron states split into spin-antisymmetric states $(\uparrow\downarrow-\downarrow\uparrow)/\sqrt2$ with a symmetric spatial part, and spin-symmetric states $(\uparrow\downarrow+\downarrow\uparrow)/\sqrt2$ with an antisymmetric spatial part (in both cases the product is antisymmetric, as Section 12.3 requires). The Hamiltonian does not act on the spins and treats the two electrons alike, so it maps symmetric spatial states to symmetric ones and antisymmetric to antisymmetric ones, and the two kinds can be treated separately. The only antisymmetric spatial state of two sites is $(\mathrm{LR}-\mathrm{RL})/\sqrt2$, where LR means electron 0 on L and electron 1 on R. The hopping maps LR and RL to the same state, $(h_0+h_1)\,\mathrm{LR}=-t(\mathrm{RR}+\mathrm{LL})=(h_0+h_1)\,\mathrm{RL}$, so it gives 0 on $(\mathrm{LR}-\mathrm{RL})/\sqrt2$, and the repulsion gives 0 too (the electrons are on different sites): its energy is 0. The ground state is found among the symmetric spatial states, which are spanned by LL (both on L), RR, and $S=(\mathrm{LR}+\mathrm{RL})/\sqrt2$. The hopping of either electron turns LL into LR or RL, so $(h_0+h_1)\,\mathrm{LL}=-t(\mathrm{RL}+\mathrm{LR})=-\sqrt2\,t\,S$, and likewise for RR, while $(h_0+h_1)\,S=-\sqrt2\,t(\mathrm{LL}+\mathrm{RR})$. The repulsion gives $U$ on LL and RR and 0 on $S$. In the basis (LL, RR, $S$)

$$
\hat H=\begin{pmatrix}U&0&-\sqrt2\,t\\0&U&-\sqrt2\,t\\-\sqrt2\,t&-\sqrt2\,t&0\end{pmatrix}.
$$

The combination $(\mathrm{LL}-\mathrm{RR})/\sqrt2$ decouples with energy $U$; the combination $D=(\mathrm{LL}+\mathrm{RR})/\sqrt2$ couples to $S$ with the matrix element $-2t$, which leaves the $2\times2$ problem with the matrix $\begin{pmatrix}U&-2t\\-2t&0\end{pmatrix}$ and the eigenvalues $\tfrac12\bigl(U\pm\sqrt{U^2+16t^2}\bigr)$. The ground-state energy is

$$
E_0=\tfrac12\Bigl(U-\sqrt{U^2+16t^2}\Bigr),
$$

which is below 0 (because $\sqrt{U^2+16t^2}>U$), so it is the ground state.

**Hartree–Fock.** A determinant for two electrons of opposite spins is built from one spin-up orbital and one spin-down orbital. The simplest one, called **restricted Hartree–Fock**, puts both electrons into the bonding orbital $\varphi_b=(\mathrm L+\mathrm R)/\sqrt2$ of Section 12.2, with opposite spins. Its spatial part is $\varphi_b(0)\varphi_b(1)=(\mathrm{LL}+\mathrm{LR}+\mathrm{RL}+\mathrm{RR})/2=(D+S)/\sqrt2$. With the $2\times2$ matrix above, the energy is $\tfrac12U+\tfrac12\cdot0+2\cdot\tfrac1{\sqrt2}\cdot\tfrac1{\sqrt2}\cdot(-2t)$, that is

$$
E_{\text{RHF}}=-2t+\tfrac12U .
$$

**Is it the best determinant?** Take any spin-up orbital with moduli $(\cos\alpha,\sin\alpha)$ on (L, R) and any spin-down orbital with moduli $(\cos\beta,\sin\beta)$, $0\le\alpha,\beta\le\pi/2$. Exchange acts only between equal spins (Section 12.6), so for this contact repulsion the Hartree and exchange energies add up to $U(n_{\mathrm L\uparrow}n_{\mathrm L\downarrow}+n_{\mathrm R\uparrow}n_{\mathrm R\downarrow})$, the rule $E_H+E_x=g_c\int n_\uparrow n_\downarrow$ of Section 12.6 with the integral replaced by the sum over the two sites; here $n_{\mathrm L\uparrow}=\cos^2\alpha$ is the spin-up density on L, and so on. The energy is this term plus the hopping energies of the two orbitals. The hopping energy of an orbital with the values $(\varphi_\mathrm L,\varphi_\mathrm R)$ on the two sites is $\varphi^\dagger h\varphi=-2t\,\mathrm{Re}(\varphi_\mathrm L^*\varphi_\mathrm R)\ge-2t\,|\varphi_\mathrm L|\,|\varphi_\mathrm R|$, with equality when $\varphi_\mathrm L^*\varphi_\mathrm R$ is real and nonnegative; the repulsion does not depend on the phases, so we choose the phases that make the hopping term most negative, $-2t\cos\alpha\sin\alpha=-t\sin2\alpha$ for spin up. With $s_\alpha=\sin2\alpha$, $c_\alpha=\cos2\alpha$ (the same for $\beta$), and $\cos^2\alpha=\tfrac12(1+c_\alpha)$, $\sin^2\alpha=\tfrac12(1-c_\alpha)$,

$$
E=-t\,(s_\alpha+s_\beta)+\tfrac U2\bigl(1+c_\alpha c_\beta\bigr).
$$

Since $c_\alpha c_\beta\ge-\tfrac12(c_\alpha^2+c_\beta^2)$ (this is $(c_\alpha+c_\beta)^2\ge0$) and $1-c^2=s^2$,

$$
E\ \ge\ \sum_{x=\alpha,\beta}\Bigl(-t\,s_x+\tfrac U4\,s_x^2\Bigr).
$$

Each term, a parabola in $s_x\in[0,1]$, is smallest at $s_x=\min(1,2t/U)$, and equality holds throughout for $\beta=\pi/2-\alpha$ (then $c_\beta=-c_\alpha$ and $s_\beta=s_\alpha$). Hence $E_{HF}=-2t+\tfrac12U$ for $U\le2t$, attained by the restricted state ($\alpha=\beta=\pi/4$). For $U>2t$, $E_{HF}=-2t^2/U$, attained at $\sin2\alpha=2t/U$ by the **unrestricted** determinant with spin-up orbital $(\cos\alpha,\sin\alpha)$ and spin-down orbital $(\sin\alpha,\cos\alpha)$. That determinant breaks the left–right symmetry of each spin but keeps $n=(1,1)$. For $t=1$, $U=2$ the two coincide: $U=2t$ is exactly the threshold.

**Numbers.** For $t=1$ and $U=2$: $E_0=\tfrac12(2-\sqrt{20})=-1.236068$ and $E_{HF}=-1$. The difference $E_c=E_0-E_{HF}=-0.236068$ is the **correlation energy**: the energy that no single determinant can capture. Its physical meaning is visible in the probability of double occupancy (both electrons on one site). In the restricted state it is $|\langle D|\Phi\rangle|^2=\tfrac12$, independent of $U$; for $U\le2t$, so also here at $U=2t$, this is the Hartree–Fock state. In the exact ground state it is $0.276393$ (the squared $D$-component of the lowest eigenvector). The exact electrons **avoid each other** and keep the left–right symmetry of each spin; a single determinant cannot do both. Its double occupancy is $n_{\mathrm L\uparrow}n_{\mathrm L\downarrow}+n_{\mathrm R\uparrow}n_{\mathrm R\downarrow}=\tfrac12(1+c_\alpha c_\beta)$, which equals $\tfrac12$ whenever each spin is shared equally ($c_\alpha=c_\beta=0$); for $U>2t$ the unrestricted determinant lowers it, but only by breaking that symmetry (Exercise 12.4). Yet the density is the same in the exact and in the Hartree–Fock state, one electron on each site, $n_\mathrm L=n_\mathrm R=1$, by the left–right symmetry. A theory that works with the density alone must therefore contain, somewhere, the information that turns $n=(1,1)$ into $-1.236068$ rather than $-1$. In density functional theory that information is the exchange–correlation functional.

### 12.9 The density decides everything: the Hohenberg–Kohn theorems

We now leave wave functions behind. Fix the particle number $N$ and the interaction $\hat W$, and regard the external potential $v$ as the only thing that distinguishes one system from another (Section 12.3).

**Theorem 12.1 (Hohenberg–Kohn, 1964).** Let $v$ and $v'$ be two external potentials whose Hamiltonians $\hat H=\hat T+\hat W+\hat V$ and $\hat H'=\hat T+\hat W+\hat V'$ have non-degenerate ground states $\Psi$ and $\Psi'$. If $v-v'$ is not a constant, then the ground-state densities $n$ and $n'$ are different. In other words, the ground-state density determines the potential up to a constant, hence the Hamiltonian, hence every property of the system.

**Proof.** First, $\Psi\ne\Psi'$ (as states, that is, not merely up to a phase). If they were equal, subtracting the two Schrödinger equations would give $(\hat V-\hat V')\Psi=(E_0-E_0')\Psi$, that is $\sum_i[v(\mathbf r_i)-v'(\mathbf r_i)]=E_0-E_0'$ wherever $\Psi\ne0$, which forces $v-v'$ to be constant. (This step assumes that $\Psi$ does not vanish on a region of positive volume, which holds for the potentials of physics.) Now suppose, to reach a contradiction, that $n=n'$. Because $\Psi$ is the unique ground state of $\hat H$ and $\Psi'\ne\Psi$, the variational principle holds with strict inequality:

$$
E_0<\langle\Psi'|\hat H\Psi'\rangle=\langle\Psi'|\hat H'\Psi'\rangle+\langle\Psi'|(\hat V-\hat V')\Psi'\rangle=E_0'+\int\bigl(v-v'\bigr)\,n'\,d^3r .
$$

Exchanging the roles of the two systems gives $E_0'<E_0+\int(v'-v)\,n\,d^3r$. Add the two inequalities and use $n=n'$: the integrals cancel and we get $E_0+E_0'<E_0+E_0'$, which is false. Hence $n\ne n'$. $\square$

**The universal functional (Levy–Lieb constrained search).** For every density $n$ that comes from some antisymmetric $N$-particle wave function (an **$N$-representable** density: nonnegative, integrating to $N$, and not too irregular) define

$$
F[n]=\min_{\Psi\to n}\ \langle\Psi|\hat T+\hat W|\Psi\rangle ,
$$

the smallest kinetic-plus-interaction energy among all wave functions that have the density $n$ (“$\Psi\to n$”). $F$ is **universal**: it does not depend on $v$, only on $N$ and on the interaction. (We assume that the minimum is attained; the careful mathematical theory replaces “min” by “infimum”, which changes nothing below.)

**Theorem 12.2 (variational principle for the density).** For every external potential $v$ with ground-state energy $E_0$,

$$
E_0=\min_n\Bigl(F[n]+\int v\,n\,d^3r\Bigr),
$$

and the minimum is attained at the ground-state density.

**Proof.** The variational principle over wave functions reads $E_0=\min_\Psi\langle\Psi|\hat T+\hat W+\hat V|\Psi\rangle$. Organize the minimization in two steps: first over all $\Psi$ with a given density $n$, then over $n$. In the first step $\langle\Psi|\hat V|\Psi\rangle=\int v\,n$ is the same for all these $\Psi$ (Section 12.3), so the inner minimum is $F[n]+\int v\,n$. The outer minimum over $n$ then equals the minimum over all $\Psi$, which is $E_0$. $\square$

These two theorems say that the energy is a functional of the density alone, $E_v[n]=F[n]+\int vn$, and that minimizing it over densities gives the exact ground-state energy and density. They do not say what $F[n]$ is. For the two-site model of Section 12.8 the theorem guarantees that the number $-1.236068$ is a property of the density $(1,1)$ together with $v$; the task of DFT is to find good approximations for $F$.

### 12.10 Functionals and functional derivatives from zero

A **functional** is a rule that assigns a number to a whole function: $F[n]$ takes the function $n(\mathbf r)$ and returns one number. Examples: $N[n]=\int n\,d^3r$, $A[n]=\int n^2\,d^3r$, and the Hartree energy $E_H[n]=\tfrac12\int\!\int n(\mathbf r)\,w(\mathbf r,\mathbf r')\,n(\mathbf r')\,d^3r\,d^3r'$.

**Definition.** Change $n$ by a small amount $\epsilon\,\eta(\mathbf r)$, where $\eta$ is any function and $\epsilon$ a small number. If

$$
F[n+\epsilon\eta]=F[n]+\epsilon\int\frac{\delta F}{\delta n(\mathbf r)}\,\eta(\mathbf r)\,d^3r+O(\epsilon^2)
$$

for every $\eta$, the function $\delta F/\delta n(\mathbf r)$ is the **functional derivative** of $F$ at $n$. It is the continuum version of the gradient: on a grid with points $\mathbf r_k$ and volume $\Delta V$ per point, $F$ is an ordinary function of the numbers $n_k$ and $\delta F/\delta n(\mathbf r_k)=(\partial F/\partial n_k)/\Delta V$.

**Examples.** (i) $A[n]=\int n^2$: $A[n+\epsilon\eta]=\int(n^2+2\epsilon n\eta+\epsilon^2\eta^2)$, so $\delta A/\delta n=2n$. (ii) For $G[n]=\int f(n(\mathbf r))\,d^3r$ with any differentiable function $f$, Taylor's formula $f(n+\epsilon\eta)=f(n)+\epsilon f'(n)\eta+O(\epsilon^2)$ gives $\delta G/\delta n=f'(n)$; for instance $\delta\int n^{4/3}/\delta n=\tfrac43n^{1/3}$ and $\delta\int n^{5/3}/\delta n=\tfrac53n^{2/3}$. (iii) For $E_H$ the first-order change is $\tfrac12\int\!\int(\eta w n'+n w\eta')$, and because $w$ is symmetric both terms are equal: $\delta E_H/\delta n(\mathbf r)=\int w(\mathbf r,\mathbf r')\,n(\mathbf r')\,d^3r'=v_H(\mathbf r)$, the Hartree potential of Section 12.7. (iv) $\delta\int v\,n/\delta n=v$.

**Worked example on a grid.** Take three points with $\Delta V=1$ and $A=\sum_kn_k^2$. At $n=(1,\tfrac12,\tfrac12)$ (the density of Section 12.4) the gradient is $(2,1,1)$, which is $2n$ as example (i) says. Moving the density by $\epsilon\eta$ with $\eta=(1,-1,0)$ (a particle-conserving change) changes $A$ by $\epsilon(2-1)+O(\epsilon^2)=\epsilon+O(\epsilon^2)$; directly, $A(1+\epsilon,\tfrac12-\epsilon,\tfrac12)-A(1,\tfrac12,\tfrac12)=\epsilon+2\epsilon^2$.

**Minimizing with a constraint.** To minimize $E[n]$ over densities with $\int n=N$, introduce a Lagrange multiplier $\mu$ (Section 12.7), that is, make $\mathcal L=E[n]-\mu\bigl(\int n-N\bigr)$ stationary, and require $\delta E/\delta n(\mathbf r)=\mu$ at every point. (On a grid the constraint is $c=\sum_kn_k\,\Delta V=N$, with $\partial c/\partial n_k=\Delta V$, so the condition $\partial E/\partial n_k=\mu\,\Delta V$ of Section 12.7 is $\delta E/\delta n(\mathbf r_k)=\mu$ by the definition above.) The multiplier $\mu$ is the **chemical potential**: the change of the minimal energy per added particle, $\mu=dE_0/dN$. This is the meaning of a multiplier derived in Section 12.7, $df^\ast/dc_0=\lambda$, with $f=E$, $c=\int n$ and $c_0=N$, and it holds where the minimum depends differentiably on $N$.

### 12.11 The Kohn–Sham equations

The unknown functional $F[n]$ contains the kinetic energy, and the kinetic energy is the hardest part to approximate by an explicit formula in $n$ (Section 12.12 shows the crude attempt). Kohn and Sham (1965) avoided the problem with a trick: compute the kinetic energy **exactly**, but for a fictitious system of non-interacting particles that has the same density.

**The non-interacting reference system.** For non-interacting particles ($\hat W=0$) the constrained search of Section 12.9 defines

$$
T_s[n]=\min_{\Phi\to n}\langle\Phi|\hat T|\Phi\rangle ,
$$

the smallest kinetic energy of a non-interacting state with density $n$; its minimizer is (for the densities we consider) a single Slater determinant of orbitals $\varphi_a$ with $n=\sum_a|\varphi_a|^2$. The Kohn–Sham scheme **assumes** that the density of interest is **non-interacting $v$-representable**: it is the ground-state density of some non-interacting system in some potential $v_s$. This is an assumption, not a theorem; it holds in all practical applications we are aware of, and Chapter 13 simply adopts it.

**Splitting the functional.** Write the exact universal functional as

$$
F[n]=T_s[n]+E_H[n]+E_{xc}[n],
$$

which **defines** the **exchange–correlation energy** $E_{xc}=F-T_s-E_H$. It collects everything that the easy pieces miss: the exchange energy of Section 12.6, the correlation energy of Section 12.8, and the difference between the true kinetic energy and $T_s$. Nothing has been approximated yet.

**The equations.** Minimize $E[n]=T_s[n]+\int v\,n+E_H[n]+E_{xc}[n]$ by varying the orbitals of the determinant, with Lagrange multipliers $\varepsilon_a$ for their normalization. Since $n=\sum_a|\varphi_a|^2$, the chain rule gives $\delta n(\mathbf r')/\delta\varphi_a^*(\mathbf r)=\varphi_a(\mathbf r)\,\delta(\mathbf r-\mathbf r')$, so every density functional $G[n]$ contributes $(\delta G/\delta n)\,\varphi_a$. The kinetic term contributes $-\tfrac12\nabla^2\varphi_a$. Setting the derivative to zero gives the **Kohn–Sham equations**

$$
\Bigl[-\tfrac12\nabla^2+v_s(\mathbf r)\Bigr]\varphi_a=\varepsilon_a\varphi_a,\qquad
v_s=v+v_H+v_{xc},\qquad v_{xc}(\mathbf r)=\frac{\delta E_{xc}}{\delta n(\mathbf r)},
$$

$$
n(\mathbf r)=\sum_{a\in O}|\varphi_a(\mathbf r)|^2 ,
$$

with the $N$ lowest orbitals occupied. (As in Section 12.7 the multipliers can be made diagonal because the equations depend on the occupied orbitals only through $n$.) The **Kohn–Sham potential** $v_s$ is local: a multiplication by a function, simpler than the Fock operator. If $E_{xc}$ were known exactly, these one-particle equations would give the exact ground-state density and energy of the interacting system.

**Total energy.** Multiplying the equations by $\varphi_a^*$, integrating and summing, $\sum_a\varepsilon_a=T_s+\int v_s\,n$. Hence

$$
E_0=\sum_{a\in O}\varepsilon_a-E_H[n]+E_{xc}[n]-\int v_{xc}\,n\,d^3r ,
$$

the Kohn–Sham analogue of the double-counting formula of Section 12.7.

**Self-consistency.** $v_s$ depends on $n$, and $n$ on the orbitals, which depend on $v_s$. The equations are solved by the loop

1. guess a density $n$;
2. build $v_s=v+v_H[n]+v_{xc}[n]$;
3. solve the one-particle equations and occupy the $N$ lowest orbitals;
4. form the new density $n_{\text{out}}=\sum_a|\varphi_a|^2$;
5. if $n_{\text{out}}$ equals $n$ within a tolerance, stop; otherwise mix $n$ and $n_{\text{out}}$ (Section 12.13) and go to step 2.

**What the orbitals mean.** The Kohn–Sham orbitals and energies belong to the fictitious non-interacting system. Only the density and the total energy are guaranteed to be physical. The orbital energies are nevertheless useful: Section 12.15 shows that each is the derivative of the total energy with respect to the occupation of its own orbital, so the highest occupied one, $\varepsilon_{\text{HOMO}}$ (HOMO: highest occupied molecular orbital, a name taken over from chemistry), is the rate at which the energy changes when a small fraction of a particle is removed from the system.

### 12.12 The uniform gas and the local density approximation

To use the Kohn–Sham equations we need an approximation for $E_{xc}[n]$. The oldest and simplest one borrows it from the only many-body system whose properties are known accurately: the **uniform gas**, infinitely many particles spread with constant density over all space.

**Spherical coordinates.** The integrals of this section are done in spherical coordinates: $x=r\sin\theta\cos\phi$, $y=r\sin\theta\sin\phi$, $z=r\cos\theta$ with $r\ge0$, $0\le\theta\le\pi$ and $0\le\phi<2\pi$. The flat metric in these coordinates follows from the polar-coordinate result of Chapter 1 used twice. With $\varrho=r\sin\theta$, the pair $(x,y)=(\varrho\cos\phi,\varrho\sin\phi)$ gives $dx^2+dy^2=d\varrho^2+\varrho^2d\phi^2$, and the pair $(z,\varrho)=(r\cos\theta,r\sin\theta)$ gives $dz^2+d\varrho^2=dr^2+r^2d\theta^2$. Hence

$$
dx^2+dy^2+dz^2=dr^2+r^2d\theta^2+r^2\sin^2\theta\,d\phi^2 ,
$$

the metric is $\mathrm{diag}(1,r^2,r^2\sin^2\theta)$, $\sqrt{|g|}=r^2\sin\theta$ (Chapter 1: $\sqrt{|g|}$ is the volume factor) and $d^3r=r^2\sin\theta\,dr\,d\theta\,d\phi$. With $u=\cos\theta$ ($du=-\sin\theta\,d\theta$, and $\theta$ from 0 to $\pi$ means $u$ from 1 to $-1$):

$$
\int d^3r\,f=\int_0^\infty r^2\,dr\int_{-1}^{1}du\int_0^{2\pi}d\phi\ f .
$$

For $f$ depending only on $r$ this is $4\pi\int_0^\infty r^2f\,dr$. For $f$ depending only on $r$ and $u$ it is $2\pi\int_0^\infty r^2\,dr\int_{-1}^1du\,f$. The same formulas hold for integrals over a momentum $\mathbf k$, with $k=|\mathbf k|$ in place of $r$, and the axis $\theta=0$ may be chosen in any direction.

**Plane waves in a box.** Put the particles in a cube of side $\ell$ and volume $V=\ell^3$ and require the wave functions to repeat themselves from one face to the opposite one (**periodic boundary conditions**, a torus). The orbitals are plane waves $\varphi_{\mathbf k}(\mathbf r)=e^{i\mathbf k\cdot\mathbf r}/\sqrt V$, eigenfunctions of $-\tfrac12\nabla^2$ with energy $\tfrac12k^2$, and periodicity allows only $\mathbf k=(2\pi/\ell)(n_1,n_2,n_3)$ with integers $n_1,n_2,n_3$. Each allowed $\mathbf k$ occupies a cube of volume $(2\pi/\ell)^3=(2\pi)^3/V$ in $\mathbf k$-space, so for a large box a sum over allowed momenta becomes an integral:

$$
\sum_{\mathbf k}\ \longrightarrow\ V\int\frac{d^3k}{(2\pi)^3}.
$$

The same torus, with the spacing $\Delta k=2\pi/\ell$, is used for the three space directions $x_1,x_2,x_3$ in Chapter 13.

**The Fermi sphere.** The non-interacting ground state fills the lowest energies: all $\mathbf k$ with $|\mathbf k|<k_F$ (the **Fermi momentum**), each with all $g$ internal states. Counting states,

$$
N=g\,V\,\frac{\tfrac43\pi k_F^3}{(2\pi)^3}\quad\Longrightarrow\quad n=\frac{g\,k_F^3}{6\pi^2}.
$$

The kinetic energy per volume is $t=g\int_{k<k_F}\frac{d^3k}{(2\pi)^3}\frac{k^2}2=\frac{g}{2\pi^2}\cdot\frac{k_F^5}{10}$ (spherical coordinates, as above: $d^3k\to4\pi k^2dk$ for an integrand that depends only on $k$). For electrons ($g=2$): $n=k_F^3/(3\pi^2)$, $t=k_F^5/(10\pi^2)$, and eliminating $k_F=(3\pi^2n)^{1/3}$,

$$
t(n)=C_F\,n^{5/3},\qquad C_F=\tfrac3{10}\bigl(3\pi^2\bigr)^{2/3}=2.871234 .
$$

The **Thomas–Fermi** model (1927) approximated the kinetic energy of any system by $\int t(n(\mathbf r))\,d^3r$. It is too crude (it predicts, for example, that molecules do not bind); the Kohn–Sham scheme keeps the kinetic energy exact through $T_s$ and approximates only $E_{xc}$.

**Exchange energy of the uniform electron gas.** We compute $E_x$ of Section 12.6 for the filled Fermi sphere with $w=1/|\mathbf r-\mathbf r'|$, $g=2$, in five steps.

*Step 1: the density matrix.* For each spin, $\rho_\sigma(\mathbf r,\mathbf r')=\sum_{k<k_F}\varphi_{\mathbf k}(\mathbf r)\varphi^*_{\mathbf k}(\mathbf r')=\int_{k<k_F}\frac{d^3k}{(2\pi)^3}e^{i\mathbf k\cdot(\mathbf r-\mathbf r')}$, a function of $\mathbf R=\mathbf r-\mathbf r'$ only.

*Step 2: one integral from translation invariance.* Since the integrand depends only on $\mathbf R$, $\int\!\int d^3r\,d^3r'\to V\int d^3R$, and the two spins give equal contributions:

$$
\frac{E_x}V=-\tfrac12\cdot2\int d^3R\,\frac{|\rho_\sigma(\mathbf R)|^2}{R}
=-\int_{k<k_F}\!\!\frac{d^3k}{(2\pi)^3}\int_{k'<k_F}\!\!\frac{d^3k'}{(2\pi)^3}\int d^3R\,\frac{e^{i(\mathbf k-\mathbf k')\cdot\mathbf R}}{R}.
$$

*Step 3: the Coulomb integral.* For $\mathbf q\ne0$ compute $\int d^3R\,e^{i\mathbf q\cdot\mathbf R}e^{-\kappa R}/R$ with a small number $\kappa>0$ that makes it converge (a **regulator**; the letter $\mu$ is kept for the chemical potential), using spherical coordinates around $\mathbf q$ ($u$ is the cosine of the angle between $\mathbf R$ and $\mathbf q$):

$$
\begin{aligned}
\int d^3R\,\frac{e^{i\mathbf q\cdot\mathbf R}e^{-\kappa R}}R
&=2\pi\int_0^\infty R\,e^{-\kappa R}\,dR\int_{-1}^1e^{iqRu}\,du
=\frac{2\pi}{iq}\int_0^\infty\bigl(e^{(iq-\kappa)R}-e^{(-iq-\kappa)R}\bigr)\,dR\\
&=\frac{2\pi}{iq}\Bigl(\frac1{\kappa-iq}-\frac1{\kappa+iq}\Bigr)=\frac{4\pi}{q^2+\kappa^2}.
\end{aligned}
$$

Letting $\kappa\to0$ gives $4\pi/q^2$. Hence

$$
\frac{E_x}V=-\frac1{(2\pi)^6}\int_{k<k_F}d^3k\ I(k),\qquad I(k)=\int_{k'<k_F}d^3k'\,\frac{4\pi}{|\mathbf k-\mathbf k'|^2}.
$$

*Step 4: the inner integral.* Spherical coordinates around $\mathbf k$ give $\int_{-1}^1\frac{du}{k^2+k'^2-2kk'u}=\frac1{kk'}\ln\Bigl|\frac{k+k'}{k-k'}\Bigr|$, so $I(k)=\frac{8\pi^2}k\int_0^{k_F}k'\ln\bigl|\frac{k+k'}{k-k'}\bigr|\,dk'$. The last integral equals $kk_F+\tfrac12(k_F^2-k^2)\ln\bigl|\frac{k+k_F}{k-k_F}\bigr|$ (both sides vanish at $k_F=0$, and their derivatives with respect to $k_F$ agree, as one checks with $\frac{d}{dk_F}\ln\bigl|\frac{k+k_F}{k-k_F}\bigr|=\frac{2k}{k^2-k_F^2}$). With $x=k/k_F$,

$$
I(k)=16\pi^2k_F\,L(x),\qquad L(x)=\frac12+\frac{1-x^2}{4x}\ln\Bigl|\frac{1+x}{1-x}\Bigr| .
$$

*Step 5: the outer integral.* $\int_{k<k_F}d^3k\,I(k)=16\pi^2k_F\cdot4\pi k_F^3\int_0^1x^2L(x)\,dx$. Expand $\ln\frac{1+x}{1-x}=2\sum_{m\ge0}\frac{x^{2m+1}}{2m+1}$ for $0\le x<1$; then $\int_0^1x(1-x^2)\ln\frac{1+x}{1-x}\,dx=2\sum_m\frac1{2m+1}\bigl(\frac1{2m+3}-\frac1{2m+5}\bigr)$. The partial fractions $\frac1{(2m+1)(2m+3)}=\frac12\bigl(\frac1{2m+1}-\frac1{2m+3}\bigr)$ and $\frac1{(2m+1)(2m+5)}=\frac14\bigl(\frac1{2m+1}-\frac1{2m+5}\bigr)$ make both sums telescope, to $\tfrac12$ and $\tfrac14(1+\tfrac13)=\tfrac13$, so the integral is $2(\tfrac12-\tfrac13)=\tfrac13$ and $\int_0^1x^2L\,dx=\tfrac16+\tfrac14\cdot\tfrac13=\tfrac14$. Therefore $E_x/V=-64\pi^3k_F^4/(4\cdot64\pi^6)=-k_F^4/(4\pi^3)$, and with $k_F=(3\pi^2n)^{1/3}$:

$$
e_x(n)=\frac{E_x}V=-\frac34\Bigl(\frac3\pi\Bigr)^{1/3}n^{4/3}=-0.738559\,n^{4/3},\qquad \frac{E_x}N=-\frac{3k_F}{4\pi}.
$$

This is **Dirac's exchange energy** (1930).

**The local density approximation (LDA).** A real density varies in space. The LDA treats each small volume $d^3r$ as if it were a piece of uniform gas with the local density $n(\mathbf r)$:

$$
E_{xc}^{\text{LDA}}[n]=\int e_{xc}\bigl(n(\mathbf r)\bigr)\,d^3r,\qquad v_{xc}^{\text{LDA}}(\mathbf r)=\frac{de_{xc}}{dn}\Big|_{n(\mathbf r)}
$$

(example (ii) of Section 12.10). Its exchange part is Dirac's formula, $v_x=-(3/\pi)^{1/3}n^{1/3}$. The correlation part of the uniform electron gas is not known in closed form; it is taken from numerical (quantum Monte Carlo) simulations of the uniform gas, which we quote as a fact of the literature and do not use in this book. The LDA is exact for a uniform density and is an approximation for every other one; its accuracy must be judged case by case.

**The contact interaction is special.** For the contact interaction of Section 12.6 the exchange energy of every determinant (or non-interacting ensemble) is exactly local:

$$
E_x=-\frac{g_c}2\int\sum_{\sigma,\sigma'}\bigl|\rho(\mathbf r\sigma,\mathbf r\sigma')\bigr|^2\,d^3r ,
$$

which for orbitals of definite label is $-\tfrac{g_c}2\int\sum_\sigma n_\sigma^2\,d^3r$ (put $w=g_c\,\delta(\mathbf r-\mathbf r')$ into the exchange integral of Section 12.6). The uniform-gas formula $e_x=-\tfrac{g_c}2\sum_\sigma n_\sigma^2$ (the plane waves of the uniform gas have definite labels), evaluated with all the local label densities $n_\sigma$, is then not an approximation for the exchange part; evaluated with the total density alone, as $-\tfrac{g_c}{2g}n^2$, it is one, unless all $n_\sigma$ are equal. An “exchange-only LDA” of this kind is the Hartree–Fock energy (over determinants of orbitals of definite label) written as a density functional. Chapter 13 is close to this situation but not in it. There the exact Fock term is local but depends on the $2\times2$ density matrices of eight blocks, while the solver uses the uniform-gas closed form in only two local densities, a number density and a scalar density, of a relativistic gas of particles and antiparticles. That closed form equals the exact term only for equally occupied blocks without momentum current, so the choice is the approximation of the exchange part there (Section 13.8). There is also no correlation term (Section 13.8).

### 12.13 Solving the Kohn–Sham equations: iteration and mixing

The loop of Section 12.11 defines a map from an input density to an output density, $n_{\text{out}}=G[n_{\text{in}}]$, and the self-consistent density is a **fixed point**, $G[n]=n$. The naive iteration $n_{\text{in}}\leftarrow n_{\text{out}}$ often fails; this section shows why with a model small enough to follow by hand.

**Model.** Two sites L and R with site energies $-\Delta/2$ and $+\Delta/2$, hopping $t$ and on-site repulsion $U$, and two electrons with opposite spins in the lowest orbital. In the mean field each electron feels $U$ times the density of the **other** spin on the same site, $Un_\mathrm L/2$ on L and $Un_\mathrm R/2$ on R (the contact rule of Section 12.6: exchange removes the same-spin half). The one-electron Hamiltonian and the output density are

$$
h[n]=\begin{pmatrix}-\tfrac\Delta2+\tfrac U2n_\mathrm L&-t\\-t&\tfrac\Delta2+\tfrac U2n_\mathrm R\end{pmatrix},\qquad n_\mathrm R=2-n_\mathrm L,\qquad n_\mathrm L^{\text{out}}=2\,|c_\mathrm L|^2,
$$

where $(c_\mathrm L,c_\mathrm R)$ is the normalized lowest eigenvector of $h[n]$. For a real symmetric matrix $\begin{pmatrix}a&-t\\-t&b\end{pmatrix}$ the lowest eigenvector has $|c_\mathrm L|^2=\tfrac12\bigl(1+(b-a)/\sqrt{(b-a)^2+4t^2}\bigr)$. Here $b-a=\Delta+U(1-n_\mathrm L)$. With $x=n_\mathrm L-1$ (the excess on L) the whole loop becomes one function of one number, the map $G$ of the beginning of this section in reduced form:

$$
x_{\text{out}}=G(x)=\frac{\Delta-Ux}{\sqrt{(\Delta-Ux)^2+4t^2}} .
$$

**Numbers.** Take $\Delta=2$, $t=1$, $U=4$ and the start $n_\mathrm L=2$ (both electrons on the low site). Plain iteration ($n_\mathrm L\leftarrow n_\mathrm L^{\text{out}}$) gives

| step | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| $n_\mathrm L$ in | 2.000000 | 0.292893 | 1.923880 | 0.353344 | 1.916644 | 0.359836 |
| $n_\mathrm L$ out | 0.292893 | 1.923880 | 0.353344 | 1.916644 | 0.359836 | 1.915809 |

and continues to jump between about $0.3607$ and $1.9157$ forever: when the electrons sit on L, the repulsion pushes them to R, and vice versa. This is called **charge sloshing**. **Linear mixing** feeds back only a fraction $\beta$ of the change, $n_{\text{in}}\leftarrow(1-\beta)\,n_{\text{in}}+\beta\,n_{\text{out}}$. With $\beta=\tfrac12$:

| step | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| $n_\mathrm L$ in | 2.000000 | 1.146447 | 1.361898 | 1.314066 | 1.331307 | 1.325494 |
| $n_\mathrm L$ out | 0.292893 | 1.577350 | 1.266234 | 1.348548 | 1.319682 | 1.329519 |

The iteration converges to the self-consistent value $n_\mathrm L=1.326993$; the input and output agree to $10^{-6}$ after 13 steps.

**Why.** Near the fixed point $x_\ast=0.326993$ write $x=x_\ast+e$. To first order $G(x)=x_\ast+G'(x_\ast)\,e$, so the mixed iteration multiplies the error by $1-\beta\,(1-G'(x_\ast))$ at each step. Differentiating, $G'(x)=-4Ut^2/\bigl((\Delta-Ux)^2+4t^2\bigr)^{3/2}$, which gives $G'(x_\ast)=-1.687961$. The iteration converges exactly when $|1-\beta(1-G')|<1$, that is

$$
0<\beta<\frac2{1-G'(x_\ast)}=0.744058 .
$$

Plain iteration ($\beta=1$) multiplies the error by $-1.688$: it grows and alternates in sign, which is the sloshing. For $\beta=\tfrac12$ the factor is $-0.344$, and the error shrinks by about a factor 3 per step, as the table shows. The choice $\beta=1/(1-G')=0.372$ would give the factor 0.

**Anderson (Pulay) mixing.** For densities with many components the best $\beta$ differs from direction to direction. **Anderson mixing** keeps the last few input densities $n^{(i)}$ and their residuals $R^{(i)}=G[n^{(i)}]-n^{(i)}$, finds the numbers $c_i$ with $\sum_ic_i=1$ that make $\bigl\|\sum_ic_iR^{(i)}\bigr\|$ smallest, and takes as the next input $\sum_ic_i\bigl(n^{(i)}+\beta R^{(i)}\bigr)$. It estimates the derivative of $G$ from the history, a cheap substitute for Newton's method. The Rust solver of Chapter 13 uses it, with the stopping rule that the largest change of the densities, divided by their largest value, is below $10^{-10}$.

**Level crossings and smearing.** With integer (aufbau) occupations the output density jumps whenever the order of two levels near the highest occupied one changes during the iteration. If the levels cross back and forth, the loop never settles, whatever $\beta$ is. The standard remedy replaces the integer occupations by smooth Fermi–Dirac occupations of a small width (**smearing**). The converged object is then an **ensemble**: a weighted mixture of determinants with fractional occupations near the Fermi level, not a single determinant. One run of Chapter 13 needs this remedy, and its results are reported as those of the ensemble.

### 12.14 Finite temperature: Mermin's functional

So far the system was in its ground state. At a temperature $T>0$ it is in a statistical mixture of states. We set Boltzmann's constant to 1, so a temperature is an energy.

**Ensembles.** A mixture in which the state $\Psi_k$ occurs with probability $w_k\ge0$ ($\sum_kw_k=1$) is described by the **density operator** $\hat\rho=\sum_kw_k|\Psi_k\rangle\langle\Psi_k|$ (outer products, Section 12.2), a Hermitian operator with nonnegative eigenvalues and trace 1: $\langle\varphi|\hat\rho\varphi\rangle=\sum_kw_k|\langle\Psi_k|\varphi\rangle|^2\ge0$ for every state $\varphi$, and $\mathrm{Tr}\,\hat\rho=\sum_kw_k\langle\Psi_k|\Psi_k\rangle=1$ for normalized $\Psi_k$. Its eigenvalues $p_i$ therefore lie between 0 and 1 and add up to 1. The expectation value of an observable is $\mathrm{Tr}(\hat\rho\hat A)=\sum_kw_k\langle\Psi_k|\hat A\Psi_k\rangle$, and the **entropy** is $S=-\mathrm{Tr}(\hat\rho\ln\hat\rho)=-\sum_ip_i\ln p_i\ge0$, where the $p_i$ are the eigenvalues of $\hat\rho$ (the logarithm of an operator is taken in its eigenbasis, Section 12.2, and every term is $\ge0$ because $\ln p_i\le0$). If the $\Psi_k$ are orthonormal, the $p_i$ are the $w_k$ and $S=-\sum_kw_k\ln w_k$. When the particle number may vary (it is fixed on average by a chemical potential $\mu$), the equilibrium state at temperature $T$ minimizes the **grand potential**

$$
\Omega[\hat\rho]=\mathrm{Tr}\bigl[\hat\rho\,(\hat H-\mu\hat N)\bigr]+T\,\mathrm{Tr}\bigl[\hat\rho\ln\hat\rho\bigr].
$$

**Theorem 12.3 (Gibbs principle).** In a finite-dimensional state space, $\Omega$ has exactly one minimizer, the Gibbs state $\hat\rho_0=e^{-(\hat H-\mu\hat N)/T}/Z$, $Z=\mathrm{Tr}\,e^{-(\hat H-\mu\hat N)/T}$, and $\Omega[\hat\rho_0]=-T\ln Z$.

**Proof.** Since $\ln\hat\rho_0=-(\hat H-\mu\hat N)/T-\ln Z$, we have $\hat H-\mu\hat N=-T\ln\hat\rho_0-T\ln Z$, and therefore $\Omega[\hat\rho]=-T\ln Z+T\,\mathrm{Tr}\bigl[\hat\rho(\ln\hat\rho-\ln\hat\rho_0)\bigr]$. It remains to show **Klein's inequality** $D=\mathrm{Tr}[\hat\rho(\ln\hat\rho-\ln\hat\sigma)]\ge0$ for density operators $\hat\rho$ and $\hat\sigma$ with $\hat\sigma$ having positive eigenvalues. Write $\hat\rho=\sum_ip_i|i\rangle\langle i|$ and $\hat\sigma=\sum_jq_j|j\rangle\langle j|$ with orthonormal eigenbases. Then, using $\sum_j|\langle i|j\rangle|^2=1$ for every $i$ and $\sum_i|\langle i|j\rangle|^2=1$ for every $j$ (completeness of the two bases),

$$
\begin{aligned}
D&=\sum_ip_i\ln p_i-\sum_{i,j}p_i\,|\langle i|j\rangle|^2\ln q_j
=\sum_{i,j}|\langle i|j\rangle|^2\,p_i\bigl(\ln p_i-\ln q_j\bigr)\\
&\ge\sum_{i,j}|\langle i|j\rangle|^2\bigl(p_i-q_j\bigr)=1-1=0 .
\end{aligned}
$$

The inequality used, $a\ln a-a\ln b\ge a-b$ for $a\ge0$ and $b>0$, is $\ln y\le y-1$ with $y=b/a$, multiplied by $-a$ (for $a=0$ it reads $0\ge-b$). Moreover $\ln y\le y-1$ holds with equality only at $y=1$: the function $y-1-\ln y$ has the derivative $1-1/y$, negative for $y<1$ and positive for $y>1$, so its smallest value is the value 0 at $y=1$.

*Equality.* Subtracting the sum $\sum_{i,j}|\langle i|j\rangle|^2(p_i-q_j)=0$ writes $D=\sum_{i,j}|\langle i|j\rangle|^2\,d(p_i,q_j)$ with the nonnegative numbers $d(a,b)=a\ln a-a\ln b-a+b$. So $D=0$ forces $d(p_i,q_j)=0$ whenever $\langle i|j\rangle\ne0$. For $a>0$, $d(a,b)=a\,(y-1-\ln y)$ with $y=b/a$ vanishes only for $b=a$; for $a=0$, $d(0,b)=b>0$ never vanishes. Hence $p_i=q_j$ whenever $\langle i|j\rangle\ne0$, and then for every $j$

$$
\hat\rho\,|j\rangle=\sum_ip_i\,|i\rangle\langle i|j\rangle=q_j\sum_i|i\rangle\langle i|j\rangle=q_j\,|j\rangle=\hat\sigma\,|j\rangle ,
$$

so $\hat\rho=\hat\sigma$. With $\hat\sigma=\hat\rho_0$, whose eigenvalues are the positive numbers $e^{-\epsilon_k/T}/Z$, $\epsilon_k$ running over the eigenvalues of $\hat H-\mu\hat N$ (a function of an operator, Section 12.2), this gives $\Omega[\hat\rho]=-T\ln Z+T\,D>\Omega[\hat\rho_0]$ for every $\hat\rho\ne\hat\rho_0$: the Gibbs state is the only minimizer. $\square$

**Mermin's theorem (1965).** Replace the variational principle of Section 12.9 by the Gibbs principle: the proofs of Theorems 12.1 and 12.2 then go through word for word (the first step becomes: if $\hat\rho_0=\hat\rho_0'$ then $\ln\hat\rho_0=\ln\hat\rho_0'$, so $\hat V-\hat V'$ is a multiple of the identity; on the vacuum it is 0, so the multiple is 0, and on one particle $v=v'$; at fixed $\mu$ even a constant difference of the potentials changes the Gibbs state), with the strict inequality $\Omega[\hat\rho_0']>\Omega[\hat\rho_0]$ for two different Gibbs states taking the place of $\langle\Psi'|\hat H\Psi'\rangle>E_0$. At fixed $T$ and $\mu$ the equilibrium density determines the external potential, and there is a universal functional

$$
F_T[n]=\min_{\hat\rho\to n}\mathrm{Tr}\bigl[\hat\rho\,(\hat T+\hat W+T\ln\hat\rho)\bigr],\qquad
\Omega=\min_n\Bigl(F_T[n]+\int(v-\mu)\,n\,d^3r\Bigr).
$$

(Here $\hat T$ is the kinetic-energy operator and $T$ the temperature.)

**The Kohn–Sham form at finite temperature.** The non-interacting reference system is now an ensemble: orbitals $\varphi_a$ with **occupation probabilities** $f_a\in[0,1]$, density $n=\sum_af_a|\varphi_a|^2$. Its entropy follows from the independence of the occupations, which we now derive. For non-interacting fermions with orbital energies $\varepsilon_a$, $\hat H-\mu\hat N=\sum_a(\varepsilon_a-\mu)\,\hat n_a$ in the basis of these orbitals, and the $\hat n_a$ commute with one another. Every determinant $|n_0n_1\cdots\rangle$ is therefore an eigenstate of $\hat H-\mu\hat N$ with the eigenvalue $\sum_a(\varepsilon_a-\mu)n_a$, and in the Gibbs state it has the weight

$$
\frac{e^{-\sum_a(\varepsilon_a-\mu)n_a/T}}Z=\prod_a\frac{e^{-(\varepsilon_a-\mu)n_a/T}}{1+e^{-(\varepsilon_a-\mu)/T}},\qquad Z=\prod_a\bigl(1+e^{-(\varepsilon_a-\mu)/T}\bigr),
$$

because the sum of $e^{-\sum_a(\varepsilon_a-\mu)n_a/T}$ over all choices $n_a\in\{0,1\}$ factorizes into one factor per orbital. The probability of the configuration $\{n_a\}$ is thus a product $\prod_ap_a(n_a)$ with $p_a(1)=e^{-(\varepsilon_a-\mu)/T}/(1+e^{-(\varepsilon_a-\mu)/T})=f_a$ and $p_a(0)=1-f_a$: each orbital is an independent two-state system, and $f_a=1/(e^{(\varepsilon_a-\mu)/T}+1)$ is the Fermi–Dirac function met again below. For a product of independent probabilities the entropies add, since the logarithm of a product is the sum of the logarithms and the probabilities of each factor add up to 1. The reference ensemble with arbitrary occupations $f_a$ is taken of the same product form, so its entropy is

$$
S_s=-\sum_a\bigl[f_a\ln f_a+(1-f_a)\ln(1-f_a)\bigr].
$$

**Mermin's Kohn–Sham functional** is the free energy

$$
F=\sum_af_a\langle\varphi_a|-\tfrac12\nabla^2|\varphi_a\rangle-T\,S_s+\int v\,n+E_H[n]+F_{xc}[n],
$$

with a temperature-dependent exchange–correlation free energy $F_{xc}$. Making $F$ stationary with respect to the orbitals gives the Kohn–Sham equations of Section 12.11 unchanged. Making it stationary with respect to the occupations under the constraint $\sum_af_a=N$ (multiplier $\mu$): the energy terms contribute $\partial/\partial f_a=\langle\varphi_a|-\tfrac12\nabla^2|\varphi_a\rangle+\int(v+v_H+v_{xc})|\varphi_a|^2=\varepsilon_a$, and $\partial/\partial f\,[f\ln f+(1-f)\ln(1-f)]=\ln\frac f{1-f}$. So

$$
\varepsilon_a+T\ln\frac{f_a}{1-f_a}-\mu=0\quad\Longleftrightarrow\quad f_a=\frac1{e^{(\varepsilon_a-\mu)/T}+1},
$$

the **Fermi–Dirac distribution**. The sum $\sum_af_a$ increases strictly with $\mu$ (each $f_a$ does), so exactly one $\mu$ gives $\sum_af_a=N$; a computer finds it by **bisection** (halving an interval that brackets it). As $T\to0$, $f_a\to1$ for $\varepsilon_a<\mu$ and $f_a\to0$ for $\varepsilon_a>\mu$: the aufbau rule.

**Thermodynamics.** With $E=F+TS_s$ (the energy), the free energy $F(T)$ is the minimum of the functional at temperature $T$. Because $F$ is stationary with respect to orbitals and occupations and the constraints do not depend on $T$, only the explicit $T$ in $-TS_s$ contributes to $dF/dT$ (the **envelope theorem**: if $F(T)=G(T,x_\ast(T))$ with $\partial_xG=0$ at $x_\ast$, then $dF/dT=\partial_TG+\partial_xG\cdot dx_\ast/dT=\partial_TG$). For a functional in which $T$ appears only there, as in Chapter 13,

$$
\frac{dF}{dT}=-S_s,\qquad C_V=\frac{dE}{dT}=\frac{dF}{dT}+S_s+T\frac{dS_s}{dT}=T\frac{dS_s}{dT},
$$

where $C_V$ is the **heat capacity** at fixed particle number.

**Worked example.** Two levels $\varepsilon_0=0$ and $\varepsilon_1=1$, one particle, $T=\tfrac12$, no interaction. By symmetry $\mu=\tfrac12$ (then $f_0+f_1=\frac1{e^{-1}+1}+\frac1{e^{1}+1}=1$). The numbers are $f_0=0.731059$, $f_1=0.268941$, $E=f_1\varepsilon_1=0.268941$, $S_s=1.164406$ (each level contributes $0.582203$), $F=E-TS_s=-0.313262$. A numerical derivative of $F(T)$ at $T=\tfrac12$ gives $-1.164406=-S_s$, and $C_V=0.393224$.

### 12.15 Excited states: the Kohn–Sham gap, particle–hole pairs and Delta-SCF

The ground-state theory says nothing directly about excited states. Three quantities are used in practice, and Chapter 13 reports all three.

**Particle–hole excitations and the Kohn–Sham gap.** In a non-interacting system, moving one particle from an occupied orbital $i$ (it leaves a **hole**) to an empty orbital $a$ (a **particle**) costs exactly $\varepsilon_a-\varepsilon_i$, because the levels do not depend on the occupations. The list of these differences is the **particle–hole spectrum**, and its smallest member,

$$
\Delta_{KS}=\varepsilon_{\text{LUMO}}-\varepsilon_{\text{HOMO}},
$$

is the **Kohn–Sham gap** (LUMO: the lowest unoccupied orbital). In the interacting system the Kohn–Sham levels move when the occupations change, so $\Delta_{KS}$ is only the first estimate of the lowest excitation energy.

**Janak's theorem.** Let the energy $E(\{f\})$ of Section 12.14 be evaluated with orbitals that are self-consistent for the given occupations. Then

$$
\frac{\partial E}{\partial f_a}=\varepsilon_a .
$$

**Proof.** $E$ depends on $f_a$ explicitly and through the orbitals. The explicit derivative is $\varepsilon_a$ (Section 12.14). The implicit part is $\sum_bf_b\bigl(\langle d\varphi_b|h_s\varphi_b\rangle+\langle h_s\varphi_b|d\varphi_b\rangle\bigr)=\sum_bf_b\varepsilon_b\,d\langle\varphi_b|\varphi_b\rangle=0$, because the Kohn–Sham equations $h_s\varphi_b=\varepsilon_b\varphi_b$ hold and the orbitals stay normalized. $\square$

**Delta-SCF.** The **Delta-SCF** method computes an excited state as a second self-consistent solution in which the occupations are held fixed by hand: one particle is taken out of the HOMO and put into the LUMO, and the Kohn–Sham loop is run again with these occupations. The excitation energy is the difference of the two total energies, $\Delta_{\text{SCF}}=E_1-E_0$. Janak's theorem connects it with the gap. Move the particle gradually, with $f_{\text{HOMO}}=1-\tau$ and $f_{\text{LUMO}}=\tau$; then $dE/d\tau=\varepsilon_{\text{LUMO}}(\tau)-\varepsilon_{\text{HOMO}}(\tau)$, and integrating from $\tau=0$ to $\tau=1$,

$$
\Delta_{\text{SCF}}=\int_0^1\bigl[\varepsilon_{\text{LUMO}}(\tau)-\varepsilon_{\text{HOMO}}(\tau)\bigr]\,d\tau .
$$

At $\tau=0$ the integrand is $\Delta_{KS}$; the difference $\Delta_{\text{SCF}}-\Delta_{KS}$ measures how much the levels move when the particle is transferred (the **orbital relaxation**). The midpoint value $\varepsilon_{\text{LUMO}}(\tfrac12)-\varepsilon_{\text{HOMO}}(\tfrac12)$ (Slater's **transition state**) is a good estimate of the integral when the integrand is nearly linear in $\tau$. That the Delta-SCF state approximates a true excited state is an assumption of the method; it is well founded for the lowest state of a given symmetry and an approximation in general.

**Toy example.** Take the model energy $E(f_H,f_L)=\varepsilon_H^0f_H+\varepsilon_L^0f_L+\tfrac U2\bigl(f_H^2+f_L^2\bigr)$ with $\varepsilon_H^0=0$, $\varepsilon_L^0=1$ and $U=0.2$ (the last term plays the role of a self-interaction of each orbital). Janak's theorem gives the levels $\varepsilon_H=Uf_H$ and $\varepsilon_L=1+Uf_L$. In the ground state $(f_H,f_L)=(1,0)$: $E_0=0.1$, $\varepsilon_H=0.2$, $\varepsilon_L=1$, so $\Delta_{KS}=0.8$. In the Delta-SCF state $(0,1)$: $E_1=1.1$, so $\Delta_{\text{SCF}}=1.0$. The integral formula reproduces it: $\int_0^1\bigl[1+U\tau-U(1-\tau)\bigr]d\tau=1$. Here the relaxation raises the excitation energy by $U=0.2$ above the Kohn–Sham gap, and the transition state is exact because the integrand is linear.

**Two further notions.** At a finite temperature the occupations are fractional, and the particle–hole spectrum is read with a threshold: a level counts as occupied (HOMO side) if $f\ge\tfrac12$ and as empty if $f<\tfrac12$ (Chapter 13 uses this rule). The **fundamental gap** $E(N+1)+E(N-1)-2E(N)$, which involves adding and removing a particle, is a different quantity again; even with the exact functional it differs from $\Delta_{KS}$ in general. We quote this as a known property of exact DFT and do not need it: Chapter 13 works at fixed $N$ and reports $\Delta_{KS}$, the particle–hole list and $\Delta_{\text{SCF}}$.

### 12.16 What we proved and what we assumed

We proved, from the definitions: that Hermitian operators have real eigenvalues and orthogonal eigenvectors, and the variational principle; that Slater determinants are antisymmetric, normalized and obey the Pauli principle, with density $\sum_a|\varphi_a|^2$; the anticommutation relations of creation and annihilation operators; Wick's theorem for a determinant and for a non-interacting thermal ensemble; the energy of a determinant from the permutation sum, with its direct and exchange terms, and its agreement with the second-quantized operators; the cancellation of the self-interaction, and the exact locality of exchange for a contact interaction with the ratio $E_x=-E_H/g$ for equally occupied labels; the method of Lagrange multipliers and the meaning of a multiplier as the derivative of the constrained minimum; the Hartree–Fock equations, the double-counting formula and Koopmans' theorem; the exact energy of the two-site model and its Hartree–Fock energy (restricted for $U\le2t$, unrestricted for $U>2t$); the Hohenberg–Kohn theorem, the constrained-search variational principle for the density, the Kohn–Sham equations and their total-energy formula; the volume element of spherical coordinates, and the kinetic and exchange energies of the uniform gas (Thomas–Fermi constant and Dirac exchange); the convergence condition of linear mixing in the two-site model; the Gibbs principle via Klein's inequality, including the uniqueness of the minimizer, and Mermin's theorem (by the same argument); the independence of the orbital occupations in the non-interacting Gibbs state, the Fermi–Dirac occupations of the Mermin–Kohn–Sham functional and the relations $dF/dT=-S_s$, $C_V=T\,dS_s/dT$; Janak's theorem and the integral formula for Delta-SCF.

We assumed: that the particles are fermions (for dirac16complex this is the choice of Grassmann components, Chapters 5 and 8); a non-degenerate ground state and a wave function that does not vanish on a region of positive volume (Theorem 12.1); that the constrained minima exist and that the densities of interest are non-interacting $v$-representable (the Kohn–Sham scheme); a finite-dimensional state space in the proof of the Gibbs principle; the implicit function theorem (in the method of Lagrange multipliers) and, for $\mu=dE_0/dN$, a minimum that depends differentiably on $N$; and that a Delta-SCF state approximates a true excited state. We quoted without derivation, and do not use later: the correlation energy of the uniform electron gas from quantum Monte Carlo, and the statement that the exact Kohn–Sham gap differs from the fundamental gap. The **approximation** that makes DFT practical is the choice of $E_{xc}$; in the local density approximation it is the uniform-gas value at the local density. For a contact interaction with scalar labels (a vertex that does not depend on the label, as in Section 12.6) the exchange part of that choice is exact for determinants and non-interacting ensembles when it is evaluated with all label densities, and what remains approximate is the omission of correlation. Chapter 13 applies to dirac16complex, with Mermin's finite-temperature functional, an exchange-only local scheme built on the uniform-gas closed form in two densities, which approximates the exact local Fock term, with no correlation term (Section 13.8); the Rust implementation is `studies/dirac16complex_kohn_sham` (self-consistency and mixing in `src/scf.rs`, the exchange functional in `src/exchange.rs`).

### 12.17 Exercises

**Exercise 12.1.** In the three-point example of Section 12.4, compute $\Phi(2,1)$ and $\Phi(1,1)$, and show directly from the definition that the two-particle determinant vanishes identically if $\varphi_a=\varphi_b$.

**Exercise 12.2.** Using only the anticommutation relations, show that $\hat n_p^2=\hat n_p$ (so $\hat n_p$ has the eigenvalues 0 and 1) and that $a_p^\dagger a_p^\dagger=0$.

**Exercise 12.3.** For the same example, write the one-body density matrix $\rho(x,x')$ as a $3\times3$ matrix, and check $\rho^2=\rho$ and $\mathrm{Tr}\,\rho=2$.

**Exercise 12.4.** Solve the two-site model of Section 12.8 for $t=1$, $U=4$: exact energy, Hartree–Fock energy, correlation energy, and the exact probability of double occupancy.

**Exercise 12.5.** (a) Compute $\delta/\delta n$ of $\int n^{5/3}\,d^3r$ and of the LDA exchange energy $\int e_x(n)\,d^3r$. (b) Minimize the Thomas–Fermi energy $C_F\int n^{5/3}+\int vn+E_H[n]$ at fixed $\int n=N$ and write the resulting equation for $n$.

**Exercise 12.6.** For a uniform gas with $g$ internal states in three dimensions, show that the kinetic energy per particle is $\tfrac3{10}k_F^2$, independent of $g$.

**Exercise 12.7.** Repeat the mixing analysis of Section 12.13 for $\Delta=2$, $t=1$, $U=2$. Does plain iteration ($\beta=1$) converge?

**Exercise 12.8.** For the two-level example of Section 12.14 find the limits of $f_0$, $E$ and $S_s$ as $T\to0$ and as $T\to\infty$.

**Exercise 12.9.** For non-interacting levels with a fixed spectrum and fixed $N$, show that $C_V=\frac1{T^2}\Bigl[\sum_aw_a(\varepsilon_a-\mu)^2-\bigl(\sum_aw_a(\varepsilon_a-\mu)\bigr)^2/\sum_aw_a\Bigr]$ with $w_a=f_a(1-f_a)$, and conclude $C_V\ge0$.

**Exercise 12.10.** For the model energy $E=\sum_a\varepsilon_a^0f_a+\tfrac U2\sum_af_a^2$ of Section 12.15 with arbitrary $\varepsilon_H^0<\varepsilon_L^0$, show that $\Delta_{\text{SCF}}-\Delta_{KS}=U$.

**Exercise 12.11.** Electrons with a contact interaction of strength $g_c=1$ have the spin densities $n_\uparrow=0.3$, $n_\downarrow=0.1$ at a point. Compute the Hartree and exchange energy densities and check that their sum is $n_\uparrow n_\downarrow$.

### 12.18 Answers to the exercises

**Answer 12.1.** $\Phi(2,1)=\tfrac1{\sqrt2}[\varphi_0(2)\varphi_1(1)-\varphi_1(2)\varphi_0(1)]=\tfrac1{\sqrt2}[0\cdot\tfrac1{\sqrt2}-\tfrac1{\sqrt2}\cdot0]=0$, and $\Phi(1,1)=\tfrac1{\sqrt2}[\varphi_0(1)\varphi_1(1)-\varphi_1(1)\varphi_0(1)]=0$. If $\varphi_a=\varphi_b=\varphi$, then $\Phi(x_0,x_1)=\tfrac1{\sqrt2}[\varphi(x_0)\varphi(x_1)-\varphi(x_0)\varphi(x_1)]=0$ for all arguments.

**Answer 12.2.** $\hat n_p^2=a_p^\dagger a_pa_p^\dagger a_p=a_p^\dagger(1-a_p^\dagger a_p)a_p=\hat n_p-a_p^\dagger a_p^\dagger a_pa_p$. From $\{a_p^\dagger,a_p^\dagger\}=0$ we get $2a_p^\dagger a_p^\dagger=0$, so the last term vanishes and $\hat n_p^2=\hat n_p$. An eigenvalue $\nu$ of $\hat n_p$ satisfies $\nu^2=\nu$, so $\nu\in\{0,1\}$.

**Answer 12.3.** $\rho=\varphi_0\varphi_0^\dagger+\varphi_1\varphi_1^\dagger=\begin{pmatrix}1&0&0\\0&\tfrac12&\tfrac12\\0&\tfrac12&\tfrac12\end{pmatrix}$. Squaring, the lower $2\times2$ block gives $\begin{pmatrix}\tfrac12&\tfrac12\\ \tfrac12&\tfrac12\end{pmatrix}^2=\begin{pmatrix}\tfrac12&\tfrac12\\ \tfrac12&\tfrac12\end{pmatrix}$ and the corner gives $1$, so $\rho^2=\rho$; the trace is $1+\tfrac12+\tfrac12=2$, the particle number. The diagonal $(1,\tfrac12,\tfrac12)$ is the density found in Section 12.4.

**Answer 12.4.** $E_0=\tfrac12(4-\sqrt{32})=2-2\sqrt2=-0.828427$. The restricted determinant gives $-2+2=0$. Since $U=4>2t$, the best determinant is the unrestricted one of Section 12.8 with $\sin2\alpha=2t/U=\tfrac12$: $E_{HF}=-2t^2/U=-0.5$ (check: $-t\cdot2\cdot\tfrac12+\tfrac U2\bigl(1-\cos^22\alpha\bigr)=-1+2\cdot\tfrac14=-0.5$), so $E_c=E_0-E_{HF}=-0.328427$. The lowest eigenvector of $\begin{pmatrix}4&-2\\-2&0\end{pmatrix}$ has components $(D,S)\propto(1,1+\sqrt2)$ (from $(4-E_0)D=2S$), so the exact double occupancy is $D^2=1/\bigl(1+(1+\sqrt2)^2\bigr)=1/(4+2\sqrt2)=(2-\sqrt2)/4=0.146447$, much smaller than the restricted value $\tfrac12$: the stronger the repulsion, the more the electrons avoid each other. The unrestricted value is $n_{\mathrm L\uparrow}n_{\mathrm L\downarrow}+n_{\mathrm R\uparrow}n_{\mathrm R\downarrow}=\tfrac12\sin^22\alpha=0.125$, below the exact value: by breaking the left–right symmetry of each spin, the determinant over-separates the electrons.

**Answer 12.5.** (a) $\tfrac53n^{2/3}$, and $de_x/dn=-\tfrac43\cdot\tfrac34(3/\pi)^{1/3}n^{1/3}=-(3/\pi)^{1/3}n^{1/3}$. (b) With a multiplier $\mu$: $\tfrac53C_Fn^{2/3}+v+v_H=\mu$ wherever $n>0$, that is $n=\bigl[\tfrac3{5C_F}(\mu-v-v_H)\bigr]^{3/2}$, an equation for $n$ because $v_H$ depends on $n$ (the Thomas–Fermi equation).

**Answer 12.6.** $t/n=\dfrac{g\,k_F^5/(20\pi^2)}{g\,k_F^3/(6\pi^2)}=\dfrac{6}{20}k_F^2=\dfrac3{10}k_F^2$; the factor $g$ cancels. (It is $\tfrac35$ of the largest kinetic energy $\tfrac12k_F^2$, the average of $k^2/2$ over a full sphere.)

**Answer 12.7.** The fixed point of $G(x)=(2-2x)/\sqrt{(2-2x)^2+4}$ is $x_\ast=0.468990$ ($n_\mathrm L=1.468990$), where $G'(x_\ast)=-4Ut^2/\bigl((\Delta-Ux_\ast)^2+4t^2\bigr)^{3/2}=-0.688942$. Linear mixing converges for $0<\beta<2/(1-G')=1.184174$. Plain iteration, $\beta=1$, multiplies the error by $-0.689$ per step and converges (slowly, alternating). A weaker repulsion makes the feedback weaker.

**Answer 12.8.** As $T\to0$: $f_0\to1$, $E\to0$, $S_s\to0$ (a pure state). As $T\to\infty$: $f_0,f_1\to\tfrac12$, $E\to\tfrac12$, and each level contributes $-2\cdot\tfrac12\ln\tfrac12=\ln2$, so $S_s\to2\ln2=\ln4$: the four configurations (both empty, one or the other occupied, both occupied) become equally likely, and their average particle number is still 1.

**Answer 12.9.** With a fixed spectrum $E=\sum_af_a\varepsilon_a$ and $\sum_af_a=N$, so $\sum_a\partial_Tf_a=0$ and $C_V=\sum_a\varepsilon_a\,\partial_Tf_a=\sum_a(\varepsilon_a-\mu)\,\partial_Tf_a$. Differentiating the Fermi function, $\partial_Tf_a=w_a\bigl[(\varepsilon_a-\mu)/T^2+\mu'/T\bigr]$ with $\mu'=d\mu/dT$ and $w_a=f_a(1-f_a)$. The condition $\sum_a\partial_Tf_a=0$ gives $\mu'=-\sum_aw_a(\varepsilon_a-\mu)/\bigl(T\sum_aw_a\bigr)$. Inserting, $C_V$ equals the stated expression. The bracket is $\sum_aw_a$ times the variance of $\varepsilon_a-\mu$ with the weights $w_a/\sum_bw_b$, which is never negative.

**Answer 12.10.** Janak gives $\varepsilon_a=\varepsilon_a^0+Uf_a$. Ground state $(1,0)$: $\Delta_{KS}=\varepsilon_L^0-(\varepsilon_H^0+U)$. Energies: $E_0=\varepsilon_H^0+\tfrac U2$ and $E_1=\varepsilon_L^0+\tfrac U2$, so $\Delta_{\text{SCF}}=\varepsilon_L^0-\varepsilon_H^0$ and $\Delta_{\text{SCF}}-\Delta_{KS}=U$.

**Answer 12.11.** $n=0.4$: $e_H=\tfrac12n^2=0.08$; $e_x=-\tfrac12(n_\uparrow^2+n_\downarrow^2)=-\tfrac12(0.09+0.01)=-0.05$; the sum $0.03$ equals $n_\uparrow n_\downarrow=0.3\cdot0.1$.
