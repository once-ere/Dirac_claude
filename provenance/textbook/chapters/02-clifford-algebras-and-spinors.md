## 2. Clifford algebras and spinors from zero

### 2.1 What this chapter does

The field of this book, dirac16complex, has 16 components $\Psi_0,\dots,\Psi_{15}$ at every point of an 8-dimensional spacetime, and its field equation (Chapter 7) contains eight real 16 by 16 matrices $\gamma^0,\dots,\gamma^7$, the **gamma matrices**. Neither the number 16 nor these matrices are arbitrary. This chapter explains, from nothing, where they come from and what they do.

The story has five steps.

1. The **square-root problem.** The length of a vector is the square root of a sum of squares. Paul Dirac discovered that a sum of squares can be written as the square of a *linear* expression, provided the coefficients are matrices that anticommute. The Pauli matrices (three directions) and the Dirac matrices (four directions) are the first examples (Section 2.3 and Section 2.4).
2. The **Clifford algebra** $\mathrm{Cl}(p,q)$ is the general rule behind these examples, for any number of directions with any signs (Section 2.5).
3. **How big the matrices must be.** In 8 directions the anticommuting matrices must be at least 16 by 16, and for signature (4,4) real 16 by 16 matrices exist. We construct them in two ways: by a tensor-product recipe (Section 2.7) and by the author's notebook, whose matrices are called T16^A (Section 2.8). This is why a spinor in 4+4 dimensions has 16 components.
4. The **special matrices** of the theory: the charge matrix $C=\sigma_{16}$, the chirality $\gamma^8$, the spin generators $S^{ab}$ and the matrix $B$ (Section 2.9 to Section 2.12).
5. **Symmetry groups.** After defining groups and representations from zero (Section 2.13) we build the groups Pin(4,4) and Spin(4,4), which act on spinors, and we prove the **representation theorem**: under Pin(4,4) the 16 complex components form one indivisible (irreducible) block, while under Spin(4,4) they split into two blocks of 8 that are irreducible and genuinely different from each other (Section 2.14 and Section 2.15).

Every statement of this chapter is proved in the text, step by step, with two kinds of exceptions, each labelled where it occurs. First, a few standard results of mathematics are quoted without proof: the power series of the exponential, sine and cosine functions (calculus of one variable) and the convergence of the exponential series for matrices (Section 2.11), and the Cartan–Dieudonné theorem on reflections (Section 2.14). Second, a few properties of the notebook's particular matrices (for example that its eight gammas satisfy the Clifford relation) are taken in this chapter from the exact machine checks of the repository; Chapter 3 then proves them by hand. Where the repository has a machine check of a statement, the check is named together with its report file; Section 2.16 collects them.

The sources of this chapter are these files of the repository:

- the Stage-1 document `provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md`, its §2 (notation), §3 (the gamma matrices) and §4 (Pin(4,4) and Spin(4,4));
- the contract `handoff/specs/CONTRACT.md`, its §1, §2 and the errata in §11;
- the exact Python module `scripts/d16c_exact.py` and the checker `scripts/check_dirac16complex_algebra.py`;
- the Wolfram package `wolfram/Dirac16ComplexAlgebra.wl`;
- the reports `python-algebra-report.json` and `wolfram-algebra-report.json` and the exact data file `algebra-fixture.json`, all in the folder `artifacts/dirac16complex/arbitrary-field/`. Every report named in this chapter lies in that folder, and a check name such as `ALG_clifford` refers to the check of that name in both algebra reports; Section 2.16 lists them.

We use the conventions of the whole book (Chapter 1): everything is counted from 0; the eight coordinates are $x_0,\dots,x_7$; $x_4$ is the time; the flat metric is $\eta=\mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1)$, so directions 0 to 3 are space-like and directions 4 to 7 are time-like. We write $\eta_{ab}$ for the entry in row $a$ and column $b$ of $\eta$ and $\eta^{ab}$ for the entry of its inverse; because $\eta$ is diagonal with entries $\pm1$, $\eta^{ab}=\eta_{ab}$ as numbers. So $\eta_{aa}=+1$ for $a\le3$, $\eta_{aa}=-1$ for $a\ge4$, and $\eta_{ab}=0$ for $a\ne b$.

### 2.2 Matrix tools used in this chapter

This section collects every matrix fact the chapter uses. Chapter 1 introduces vectors, matrices and complex numbers; here we add what is special to this chapter, with proofs.

**Entries and products.** An $n$ by $n$ matrix $M$ has entries $M_{ij}$, where $i$ is the row and $j$ the column, both counted from 0 to $n-1$. The product of two matrices is $(AB)_{ij}=\sum_{k=0}^{n-1}A_{ik}B_{kj}$, and a matrix acts on a column $u$ by $(Mu)_i=\sum_jM_{ij}u_j$. Matrix multiplication is associative, $(AB)D=A(BD)$, but in general not commutative, $AB\ne BA$. $I_n$ (or simply $I$, or $1$) is the identity matrix. The **transpose** $M^T$ has entries $(M^T)_{ij}=M_{ji}$, and $(AB)^T=B^TA^T$. The **conjugate transpose** is $M^\dagger=(M^\ast)^T$, where ${}^\ast$ is complex conjugation of every entry, and $(AB)^\dagger=B^\dagger A^\dagger$. The **inverse** $M^{-1}$, if it exists, satisfies $MM^{-1}=M^{-1}M=I$. The **elementary matrix** $E_{ij}$ has a 1 in row $i$, column $j$, and 0 everywhere else.

**Linear combinations, span, independence, dimension.** A **linear combination** of matrices $M_0,\dots,M_{r-1}$ is $c_0M_0+\dots+c_{r-1}M_{r-1}$ with numbers $c_k$ (real or complex). The set of all linear combinations is the **span**. The matrices are **linearly independent** if the only combination that gives the zero matrix is the one with all $c_k=0$. A **basis** of a set of matrices closed under linear combinations is an independent list that spans it, and the number of elements of a basis is its **dimension**. The set $\mathrm{Mat}_n(\mathbb R)$ of all real $n$ by $n$ matrices has the basis $E_{ij}$ ($i,j=0,\dots,n-1$), because $M=\sum_{ij}M_{ij}E_{ij}$ and this is zero only if every $M_{ij}=0$; so its dimension is $n^2$. The same holds for complex matrices, $\mathrm{Mat}_n(\mathbb C)$. A fact we use repeatedly: in a set of dimension $m$ there are never more than $m$ independent elements, and $m$ independent elements always form a basis. The **rank** of a list of matrices (or of the rows of a matrix) is the largest number of independent elements in it, which is the dimension of its span.

**Commutator and anticommutator.** For two matrices,

$$
[A,B]:=AB-BA,\qquad\{A,B\}:=AB+BA .
$$

$A$ and $B$ **commute** if $[A,B]=0$ and **anticommute** if $\{A,B\}=0$, that is, if $AB=-BA$. Example:

$$
A=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad B=\begin{pmatrix}1&0\\0&-1\end{pmatrix}:\qquad AB=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad BA=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
$$

so $\{A,B\}=0$ and $[A,B]=2AB$. These two matrices anticommute.

**Trace.** The trace is the sum of the diagonal entries, $\operatorname{tr}M=\sum_iM_{ii}$. It is linear, $\operatorname{tr}(cA+dB)=c\operatorname{tr}A+d\operatorname{tr}B$, and it has the **cyclic property**

$$
\operatorname{tr}(AB)=\operatorname{tr}(BA).
$$

*Proof.* $\operatorname{tr}(AB)=\sum_i\sum_kA_{ik}B_{ki}=\sum_k\sum_iB_{ki}A_{ik}=\operatorname{tr}(BA)$; only the order of two finite sums was exchanged. $\square$ A consequence: for an invertible $S$, $\operatorname{tr}(S^{-1}AS)=\operatorname{tr}(ASS^{-1})=\operatorname{tr}A$. The trace does not change when the basis is changed.

**Block matrices.** A 16 by 16 matrix can be cut into four 8 by 8 blocks, and block matrices multiply like 2 by 2 matrices whose entries are matrices, keeping the order of the factors:

$$
\begin{pmatrix}A&B\\ C&D\end{pmatrix}\begin{pmatrix}E&F\\ G&H\end{pmatrix}=\begin{pmatrix}AE+BG&AF+BH\\ CE+DG&CF+DH\end{pmatrix}.
$$

(Write out the sum $\sum_k$ in the product and split it into $k<8$ and $k\ge8$.) The transpose of a block matrix transposes the pattern and every block: $\begin{pmatrix}A&B\\ C&D\end{pmatrix}^T=\begin{pmatrix}A^T&C^T\\ B^T&D^T\end{pmatrix}$.

**Kronecker (tensor) product.** For an $n$ by $n$ matrix $A$ and an $m$ by $m$ matrix $B$, the Kronecker product $A\otimes B$ is the $nm$ by $nm$ matrix made of $n\times n$ blocks, the block in position $(i,j)$ being $A_{ij}B$. In indices,

$$
(A\otimes B)_{im+k,\;jm+l}=A_{ij}B_{kl}\qquad(i,j=0,\dots,n-1;\ k,l=0,\dots,m-1).
$$

Example with $n=m=2$:

$$
\begin{pmatrix}0&1\\1&0\end{pmatrix}\otimes\begin{pmatrix}1&0\\0&-1\end{pmatrix}=\begin{pmatrix}0&0&1&0\\0&0&0&-1\\1&0&0&0\\0&-1&0&0\end{pmatrix}.
$$

**Mixed-product rule.** $(A\otimes B)(D\otimes F)=(AD)\otimes(BF)$.

*Proof.* The entry in row $im+k$ and column $jm+l$ of the left side is a sum over all columns $rm+s$ of the first factor:

$$
\sum_{r=0}^{n-1}\sum_{s=0}^{m-1}(A\otimes B)_{im+k,\,rm+s}(D\otimes F)_{rm+s,\,jm+l}=\sum_{r,s}A_{ir}B_{ks}D_{rj}F_{sl}=\Bigl(\sum_rA_{ir}D_{rj}\Bigr)\Bigl(\sum_sB_{ks}F_{sl}\Bigr),
$$

which is $(AD)_{ij}(BF)_{kl}$, the entry of $(AD)\otimes(BF)$. $\square$ The same rule holds for products of more factors, $A\otimes B\otimes D$ with three or four slots, applied slot by slot; and $(A\otimes B)^T=A^T\otimes B^T$ (exchange $i\leftrightarrow j$ and $k\leftrightarrow l$ in the index formula).

**Special kinds of matrices.** A real matrix $M$ is **symmetric** if $M^T=M$, **antisymmetric** if $M^T=-M$, and **orthogonal** if $M^TM=I$, that is, $M^{-1}=M^T$. A **signed permutation** matrix has exactly one nonzero entry in every row and every column, and that entry is $+1$ or $-1$; acting on a column it reorders the components and flips some signs. Every signed permutation matrix is orthogonal: $(M^TM)_{ij}=\sum_kM_{ki}M_{kj}$, and for $i\ne j$ no row $k$ has nonzero entries in both columns $i$ and $j$, while for $i=j$ exactly one term is $(\pm1)^2=1$. A complex matrix is **Hermitian** if $M^\dagger=M$, **anti-Hermitian** if $M^\dagger=-M$, and **unitary** if $M^\dagger M=I$.

**Matrices whose square is $\pm1$, and projectors.** A matrix $\Pi$ with $\Pi^2=\Pi$ is a **projector**. Let $M$ be a $d$ by $d$ matrix with $M^2=I$. Then

$$
P_\pm:=\tfrac12(I\pm M)\quad\text{satisfy}\quad P_\pm^2=P_\pm,\qquad P_+P_-=P_-P_+=0,\qquad P_++P_-=I,\qquad M=P_+-P_- .
$$

*Proof.* $P_\pm^2=\tfrac14(I\pm2M+M^2)=\tfrac14(2I\pm2M)=P_\pm$ and $P_+P_-=\tfrac14(I-M^2)=0$; the last two follow by adding and subtracting. $\square$ So every column $u$ splits as $u=P_+u+P_-u$, with $M(P_\pm u)=\pm P_\pm u$ (because $MP_\pm=\tfrac12(M\pm I)=\pm P_\pm$). The images of $P_+$ and $P_-$ are the **eigenspaces** of $M$ for the **eigenvalues** $+1$ and $-1$. Choosing a basis of each image, $M$ becomes $\mathrm{diag}(+1,\dots,+1,-1,\dots,-1)$, and then $P_+=\mathrm{diag}(1,\dots,1,0,\dots,0)$, whose trace is the number of $+1$'s. Since the trace does not depend on the basis,

$$
\dim(\text{eigenspace }+1)=\operatorname{tr}P_+=\tfrac12(d+\operatorname{tr}M),\qquad\dim(\text{eigenspace }-1)=\tfrac12(d-\operatorname{tr}M).
$$

In particular a **traceless** matrix ($\operatorname{tr}M=0$) with $M^2=I$ has the eigenvalue $+1$ exactly $d/2$ times and $-1$ exactly $d/2$ times, and its determinant is $(+1)^{d/2}(-1)^{d/2}$. If instead $M^2=-I$, the same argument with complex coefficients and $P_\pm=\tfrac12(I\mp iM)$ gives eigenvalues $+i$ and $-i$; for a traceless $M$ each occurs $d/2$ times, and $\det M=i^{d/2}(-i)^{d/2}=(i\cdot(-i))^{d/2}=1$. For a real symmetric or complex Hermitian matrix with $M^2=I$, the pair (number of $+1$ eigenvalues, number of $-1$ eigenvalues) is called its **signature**.

### 2.3 The square-root problem and the Pauli matrices

**Pythagoras.** A vector $(p,q)$ in the plane has squared length $p^2+q^2$. Can the square root of $p^2+q^2$ be written as a *linear* expression $\alpha p+\beta q$? Squaring,

$$
(\alpha p+\beta q)^2=\alpha^2p^2+(\alpha\beta+\beta\alpha)\,pq+\beta^2q^2 .
$$

We need $\alpha^2=1$, $\beta^2=1$ and $\alpha\beta+\beta\alpha=0$. With ordinary numbers this is impossible: $\alpha\beta+\beta\alpha=2\alpha\beta=0$ forces $\alpha=0$ or $\beta=0$. With matrices it is possible, because matrices can anticommute. The two matrices of the example in Section 2.2,

$$
\sigma_x=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad\sigma_z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
$$

satisfy $\sigma_x^2=\sigma_z^2=I$ and $\sigma_x\sigma_z+\sigma_z\sigma_x=0$. Hence $(p\sigma_x+q\sigma_z)^2=(p^2+q^2)I$.

**Worked example.** For $p=3$, $q=4$:

$$
3\sigma_x+4\sigma_z=\begin{pmatrix}4&3\\3&-4\end{pmatrix},\qquad\begin{pmatrix}4&3\\3&-4\end{pmatrix}^2=\begin{pmatrix}16+9&12-12\\12-12&9+16\end{pmatrix}=25\,I .
$$

The matrix $3\sigma_x+4\sigma_z$ is a "square root" of $25=3^2+4^2$.

**Minus signs.** Spacetime needs minus signs: in this book $\eta(v,v)=v_0^2+v_1^2+v_2^2+v_3^2-v_4^2-\dots-v_7^2$. A real matrix can square to $-I$:

$$
N=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad N^2=\begin{pmatrix}-1&0\\0&-1\end{pmatrix}=-I,
$$

and $\sigma_xN+N\sigma_x=\begin{pmatrix}-1&0\\0&1\end{pmatrix}+\begin{pmatrix}1&0\\0&-1\end{pmatrix}=0$. So $(p\sigma_x+qN)^2=(p^2-q^2)I$: a square root of a difference of squares, with real entries. This little matrix $N$ is the seed of everything real in this book.

**The general requirement.** Suppose we want matrices $\gamma^0,\dots,\gamma^{n-1}$ such that for all numbers $p_0,\dots,p_{n-1}$

$$
\Bigl(\sum_ap_a\gamma^a\Bigr)^2=\Bigl(\sum_a\eta^{aa}p_a^2\Bigr)I
$$

for a given diagonal metric $\eta$. Expanding the square, $\sum_{a,b}p_ap_b\gamma^a\gamma^b$, and pairing the terms $(a,b)$ and $(b,a)$ (they have the same coefficient $p_ap_b$),

$$
\Bigl(\sum_ap_a\gamma^a\Bigr)^2=\tfrac12\sum_{a,b}p_ap_b\bigl(\gamma^a\gamma^b+\gamma^b\gamma^a\bigr).
$$

This equals $\sum_{a,b}\eta^{ab}p_ap_bI$ for all $p$ exactly when

$$
\gamma^a\gamma^b+\gamma^b\gamma^a=2\eta^{ab}I\qquad\text{for all }a,b .
$$

This is the **Clifford relation**. It says: each $\gamma^a$ squares to $\eta^{aa}I$ ($+I$ for a space-like direction, $-I$ for a time-like one), and two different gammas anticommute.

**The Pauli matrices.** For three space directions (metric $+1,+1,+1$) we need a third 2 by 2 matrix anticommuting with $\sigma_x$ and $\sigma_z$ and squaring to $+I$. There is no real one (Exercise 2.2), but there is a complex one. The three **Pauli matrices** are

$$
\sigma_x=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad\sigma_y=\begin{pmatrix}0&-i\\ i&0\end{pmatrix},\qquad\sigma_z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$

They are named by letters, not numbers, to keep them apart from the gammas; they are Hermitian and traceless, each squares to $I$, and any two anticommute. For instance

$$
\sigma_x\sigma_y=\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}0&-i\\ i&0\end{pmatrix}=\begin{pmatrix}i&0\\0&-i\end{pmatrix}=i\sigma_z,\qquad\sigma_y\sigma_x=\begin{pmatrix}-i&0\\0&i\end{pmatrix}=-i\sigma_z,
$$

so $\{\sigma_x,\sigma_y\}=0$, and in the same way $\sigma_y\sigma_z=i\sigma_x$ and $\sigma_z\sigma_x=i\sigma_y$. The product of all three is $\sigma_x\sigma_y\sigma_z=i\sigma_z\sigma_z=iI$. Wolfgang Pauli introduced these matrices (1927) to describe the spin of the electron; they return in Chapter 3, where they build the quaternions.

A warning about names: the notebook uses the letter $\sigma$ for two other matrices, the 8 by 8 matrix $\sigma=\begin{pmatrix}0&I_4\\ I_4&0\end{pmatrix}$ and the 16 by 16 charge matrix $\sigma_{16}$ (Section 2.9). The subscripts $x,y,z$ always mean Pauli matrices.

### 2.4 Dirac matrices in four dimensions

**Why a first-order equation.** In special relativity (units with the speed of light equal to 1) a particle of mass $m$, energy $E$ and momentum $(k_1,k_2,k_3)$ satisfies $E^2=k_1^2+k_2^2+k_3^2+m^2$. In quantum mechanics a plane wave $e^{i(k_1x_1+k_2x_2+k_3x_3-Et)}$ turns $\partial/\partial x_j$ into $ik_j$ and $\partial/\partial t$ into $-iE$, so the energy relation becomes a second-order wave equation. Dirac (1928) wanted a *first-order* equation whose square is that wave equation; he needed the square root of $E^2-k_1^2-k_2^2-k_3^2$, four directions with one sign opposite to the other three. By Section 2.3 this needs four matrices satisfying the Clifford relation.

**Four anticommuting matrices.** Two by two matrices are too small: Section 2.6 proves that four anticommuting matrices must be at least 4 by 4. Dirac's choice, in the particle-physics convention $\eta=\mathrm{diag}(+1,-1,-1,-1)$ with time first, is built from 2 by 2 blocks and the Pauli matrices:

$$
\gamma_{\mathrm D}^0=\begin{pmatrix}I_2&0\\0&-I_2\end{pmatrix},\qquad\gamma_{\mathrm D}^j=\begin{pmatrix}0&\sigma_j\\-\sigma_j&0\end{pmatrix}\quad(j=x,y,z).
$$

*Check.* By the block rule, $(\gamma_{\mathrm D}^0)^2=\mathrm{diag}(I_2,I_2)=I_4$, and

$$
(\gamma_{\mathrm D}^j)^2=\begin{pmatrix}-\sigma_j^2&0\\0&-\sigma_j^2\end{pmatrix}=-I_4,\qquad\gamma_{\mathrm D}^0\gamma_{\mathrm D}^j=\begin{pmatrix}0&\sigma_j\\ \sigma_j&0\end{pmatrix}=-\gamma_{\mathrm D}^j\gamma_{\mathrm D}^0,
$$

$$
\gamma_{\mathrm D}^j\gamma_{\mathrm D}^k+\gamma_{\mathrm D}^k\gamma_{\mathrm D}^j=\begin{pmatrix}-(\sigma_j\sigma_k+\sigma_k\sigma_j)&0\\0&-(\sigma_j\sigma_k+\sigma_k\sigma_j)\end{pmatrix}=0\quad(j\ne k).
$$

So $\{\gamma_{\mathrm D}^\mu,\gamma_{\mathrm D}^\nu\}=2\,\mathrm{diag}(+1,-1,-1,-1)^{\mu\nu}I_4$. The subscript D (for Dirac) keeps these matrices apart from the 16 by 16 gammas of this book.

**Changing the sign convention.** This book counts space-like directions with $+1$ and time-like ones with $-1$. If matrices $\gamma^a$ satisfy the Clifford relation with a metric $\eta$, then the matrices $i\gamma^a$ satisfy it with $-\eta$, because $\{i\gamma^a,i\gamma^b\}=i^2\{\gamma^a,\gamma^b\}=-2\eta^{ab}I$. So $i\gamma_{\mathrm D}^\mu$ are Dirac matrices for the metric $(-1,+1,+1,+1)$ with time first. The price is that they are no longer real. In signature (4,4) no such price has to be paid: Section 2.7 constructs real matrices.

**What the gammas do in a field equation.** Take any matrices with the Clifford relation for the metric of this book, $\eta=\mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1)$, and consider the flat-space equation $\sum_\mu\gamma^\mu\partial_\mu\Psi=m\Psi$ for a column $\Psi$ of functions ($\partial_\mu=\partial/\partial x_\mu$). Applying the operator $\sum_\nu\gamma^\nu\partial_\nu$ once more and using $\partial_\mu\partial_\nu=\partial_\nu\partial_\mu$ and the pairing argument of Section 2.3,

$$
m^2\Psi=\sum_{\mu,\nu}\gamma^\mu\gamma^\nu\partial_\mu\partial_\nu\Psi=\sum_\mu\eta^{\mu\mu}\partial_\mu^2\Psi .
$$

For a plane wave $\Psi=u\,e^{i(k_0x_0+\dots+k_7x_7)}$ with a constant column $u$, $\partial_\mu^2\Psi=-k_\mu^2\Psi$, so

$$
k_4^2=m^2+k_0^2+k_1^2+k_2^2+k_3^2-k_5^2-k_6^2-k_7^2 .
$$

This is the energy–momentum relation of the 8-dimensional theory, with $k_4$ playing the role of the energy. (It is the relation found in Stage 1, §10.6, for the flat-space modes; Chapter 8 discusses what the minus signs of the extra times do.) The gamma matrices are exactly what makes a first-order equation square to the correct second-order one.

### 2.5 Clifford algebras in general

**Generators and relations.** Fix a number of directions $n$ and a diagonal metric $\eta$ with $p$ entries $+1$ followed by $q$ entries $-1$ ($p+q=n$). The **Clifford algebra** $\mathrm{Cl}(p,q)$ is built from $n$ symbols $\gamma^0,\dots,\gamma^{n-1}$, the **generators**, which can be multiplied (associatively) and added, subject only to the Clifford relation

$$
\gamma^a\gamma^b+\gamma^b\gamma^a=2\eta^{ab}\,1\qquad(a,b=0,\dots,n-1).
$$

In this book the generators are always concrete matrices, so the reader may simply read "$\mathrm{Cl}(p,q)$" as "the set of all real linear combinations of products of the $n$ gamma matrices". For this book $n=8$, $p=q=4$, and the algebra is $\mathrm{Cl}(4,4)$.

**Monomials.** For a set $A=\{a_1<a_2<\dots<a_k\}\subseteq\{0,\dots,n-1\}$ write

$$
\gamma_A:=\gamma^{a_1}\gamma^{a_2}\cdots\gamma^{a_k},\qquad\gamma_\varnothing:=1 .
$$

The number $k=|A|$ is the **degree** (or grade) of the monomial; $\gamma_A$ is **even** if $k$ is even and **odd** if $k$ is odd. There are $2^n$ subsets of $\{0,\dots,n-1\}$ (each element is in or out), so there are $2^n$ monomials: $\binom n0=1$ of degree 0, $\binom n1=n$ of degree 1, and so on. For $n=8$ there are $2^8=256$ monomials, 128 of them even and 128 odd (Exercise 2.4).

**Three rules for monomials.** Everything in this chapter rests on three rules, each a direct consequence of the Clifford relation.

(R1) *Every product of generators is $\pm$ a monomial.* To bring a product into increasing order, exchange neighbours: two different neighbours anticommute (a factor $-1$), and two equal neighbours combine to $\gamma^a\gamma^a=\eta^{aa}=\pm1$. In particular $\gamma_A\gamma_B=\pm\gamma_{A\triangle B}$, where $A\triangle B$ (the **symmetric difference**) is the set of indices that lie in exactly one of $A$ and $B$: the indices in both meet a partner and turn into $\pm1$.

(R2) *The square of a monomial of degree $k$ is*

$$
\gamma_A\gamma_A=(-1)^{k(k-1)/2}\prod_{a\in A}\eta^{aa}\;1 .
$$

*Proof.* In $\gamma^{a_1}\cdots\gamma^{a_k}\gamma^{a_1}\cdots\gamma^{a_k}$ move the second $\gamma^{a_1}$ to the left past the $k-1$ factors $\gamma^{a_k},\dots,\gamma^{a_2}$, all different from it: a sign $(-1)^{k-1}$. It then stands next to the first $\gamma^{a_1}$, and the two give $\eta^{a_1a_1}$. What remains is the square of the monomial $\gamma^{a_2}\cdots\gamma^{a_k}$ of degree $k-1$. Repeating, the total sign is $(-1)^{(k-1)+(k-2)+\dots+1+0}=(-1)^{k(k-1)/2}$. $\square$ So every monomial squares to $+1$ or $-1$, and its inverse is $\gamma_A^{-1}=\pm\gamma_A$ with the same sign.

(R3) *Commuting a generator through a monomial.* If $b\notin A$, then $\gamma^b\gamma_A=(-1)^k\gamma_A\gamma^b$; if $b\in A$, then $\gamma^b\gamma_A=(-1)^{k-1}\gamma_A\gamma^b$.

*Proof.* Moving $\gamma^b$ from the left end to the right end passes each of the $k$ factors once. Passing a factor with a different index gives $-1$; passing the factor $\gamma^b$ itself (if $b\in A$) gives $+1$. $\square$

**Worked example: $\mathrm{Cl}(1,1)$ is all real 2 by 2 matrices.** Take $n=2$, $\eta=\mathrm{diag}(+1,-1)$, and the generators $\gamma^0=P:=\sigma_x$ and $\gamma^1=N$ of Section 2.3. The four monomials are

$$
1=\begin{pmatrix}1&0\\0&1\end{pmatrix},\quad P=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad N=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad PN=\begin{pmatrix}-1&0\\0&1\end{pmatrix}=-G,
$$

with $G:=\sigma_z=\mathrm{diag}(1,-1)$. Rule (R2) predicts $(PN)^2=(-1)^{1}\eta^{00}\eta^{11}=(-1)(+1)(-1)=+1$, and indeed $G^2=I$. Every real 2 by 2 matrix is a combination of them:

$$
\begin{pmatrix}\alpha&\beta\\ \gamma&\delta\end{pmatrix}=\tfrac{\alpha+\delta}2\,1+\tfrac{\beta+\gamma}2\,P+\tfrac{\beta-\gamma}2\,N+\tfrac{\delta-\alpha}2\,PN .
$$

(Check the four entries.) The four monomials are therefore a basis of $\mathrm{Mat}_2(\mathbb R)$, whose dimension is $4=2^2$: $\mathrm{Cl}(1,1)\cong\mathrm{Mat}_2(\mathbb R)$. The rest of the chapter proves the same statement one size up, $\mathrm{Cl}(4,4)\cong\mathrm{Mat}_{16}(\mathbb R)$, where $256=16^2$.

**The three matrices $P$, $N$, $G$.** We record the facts about them used below. They are real, $P$ and $G$ are symmetric, $N$ is antisymmetric, $P^2=G^2=I$, $N^2=-I$, and any two of them anticommute:

$$
PN=-G=-NP,\qquad PG=-N=-GP,\qquad NG=-P=-GN .
$$

(Each product is a 2 by 2 multiplication; for example $PG=\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}1&0\\0&-1\end{pmatrix}=\begin{pmatrix}0&-1\\1&0\end{pmatrix}=-N$.)

### 2.6 How big must the matrices be? The trace lemma

Suppose $\gamma^0,\dots,\gamma^{n-1}$ are $d$ by $d$ matrices (real or complex) that satisfy the Clifford relation for some signature $(p,q)$, and suppose $n=p+q$ is **even**. This section proves that the $2^n$ monomials are linearly independent. Since at most $d^2$ matrices of size $d$ can be independent, this forces $d^2\ge2^n$.

**Theorem 2.1 (trace lemma).** If $n$ is even, every monomial $\gamma_A$ with $A\ne\varnothing$ has trace zero.

*Proof.* Let $k=|A|\ge1$. We find a generator $\gamma^b$ that anticommutes with $\gamma_A$.

- If $k$ is odd, then $k\le n-1$ (because $n$ is even), so some index $b$ is not in $A$. By (R3), $\gamma^b\gamma_A=(-1)^k\gamma_A\gamma^b=-\gamma_A\gamma^b$.
- If $k$ is even, pick any $b\in A$. By (R3), $\gamma^b\gamma_A=(-1)^{k-1}\gamma_A\gamma^b=-\gamma_A\gamma^b$.

In both cases $\gamma^b$ is invertible ($(\gamma^b)^{-1}=\eta^{bb}\gamma^b$, since $(\gamma^b)^2=\eta^{bb}$) and $\gamma_A=-(\gamma^b)^{-1}\gamma_A\gamma^b$. Taking the trace and using the cyclic property,

$$
\operatorname{tr}\gamma_A=-\operatorname{tr}\bigl((\gamma^b)^{-1}\gamma_A\gamma^b\bigr)=-\operatorname{tr}\gamma_A,
$$

so $\operatorname{tr}\gamma_A=0$. $\square$

(For odd $n$ the lemma fails for the top monomial: the Pauli product $\sigma_x\sigma_y\sigma_z=iI$ has trace $2i$.)

**Theorem 2.2 (independence of the monomials).** If $n$ is even, the $2^n$ monomials are linearly independent. Consequently $d^2\ge2^n$, that is, $d\ge2^{n/2}$.

*Proof.* Suppose $\sum_Bc_B\gamma_B=0$ with numbers $c_B$. Fix a set $A$, multiply on the left by $\gamma_A^{-1}=\pm\gamma_A$ and take the trace:

$$
0=\sum_Bc_B\operatorname{tr}\bigl(\gamma_A^{-1}\gamma_B\bigr).
$$

By (R1), $\gamma_A^{-1}\gamma_B=\pm\gamma_{A\triangle B}$, and $A\triangle B=\varnothing$ exactly when $B=A$. For $B\ne A$ the trace vanishes by Theorem 2.1; for $B=A$ the product is $\gamma_A^{-1}\gamma_A=1$, with trace $d$. So $0=d\,c_A$, and $c_A=0$. Since $A$ was arbitrary, all coefficients vanish. $\square$

**Consequences for this book.**

- *Dirac:* $n=4$ gives $d\ge4$. Dirac's 4 by 4 matrices are the smallest possible.
- *4+4 dimensions:* $n=8$ gives $d\ge16$. **A spinor in eight dimensions has at least 16 components**, and dirac16complex has exactly the minimum.
- *The full matrix algebra.* If $n=8$ and $d=16$, the 256 monomials are 256 independent elements of $\mathrm{Mat}_{16}(\mathbb R)$ (or of $\mathrm{Mat}_{16}(\mathbb C)$), whose dimension is $16^2=256$. Hence they are a **basis**: every 16 by 16 matrix is a unique linear combination of monomials. For real gammas this says $\mathrm{Cl}(4,4)\cong\mathrm{Mat}_{16}(\mathbb R)$.
- *The even and the odd monomials* are independent too (they are part of the 256), so the even part of the algebra has dimension 128 and the odd part has dimension 128, and a matrix that is a combination of even monomials and also a combination of odd monomials is zero.

**Corollary 2.3 (matrices that commute with all gammas).** Let $\gamma^0,\dots,\gamma^7$ be 16 by 16 matrices with the Clifford relation of signature (4,4). If a matrix $X$ (real or complex) satisfies $X\gamma^a=\gamma^aX$ for all $a$, then $X=c\,I$ for a number $c$.

*Proof.* $X$ commutes with every product of gammas, hence with every monomial, hence (by the basis property) with every matrix, in particular with every elementary matrix $E_{ij}$. Compare the entries in position $(k,j)$ of $XE_{ij}$ and $E_{ij}X$: $(XE_{ij})_{kj}=X_{ki}$ and $(E_{ij}X)_{kj}=\delta_{ki}X_{jj}$, where $\delta_{ki}$ is 1 for $k=i$ and 0 otherwise. So $X_{ki}=0$ for $k\ne i$, and $X_{ii}=X_{jj}$ for all $i,j$: $X$ is a multiple of $I$. $\square$

In the language of Section 2.13, the **commutant** of the gammas consists of the scalar matrices. The repository computes this commutant directly (Section 2.15).

### 2.7 A 16 by 16 construction: the tensor-product picture

We now show that real 16 by 16 gammas for signature (4,4) exist, by an explicit recipe that uses only the matrices $P$, $N$ and $G$ of Section 2.5. It is the "Clifford picture" of the reference implementation dirac-main (Stage 1, §3.3). For $k=1,2,3,4$ (a 1-based slot label, one of the labelled exceptions to counting from 0) define

$$
\hat\gamma_k^+:=\underbrace{G\otimes\dots\otimes G}_{k-1}\otimes P\otimes\underbrace{I_2\otimes\dots\otimes I_2}_{4-k},\qquad\hat\gamma_k^-:=\underbrace{G\otimes\dots\otimes G}_{k-1}\otimes N\otimes\underbrace{I_2\otimes\dots\otimes I_2}_{4-k},
$$

each a Kronecker product of four 2 by 2 matrices, hence 16 by 16. Order them as frame matrices:

$$
(\hat\gamma^0,\hat\gamma^1,\hat\gamma^2,\hat\gamma^3,\hat\gamma^4,\hat\gamma^5,\hat\gamma^6,\hat\gamma^7):=(\hat\gamma_1^+,\hat\gamma_2^+,\hat\gamma_3^+,\hat\gamma_4^+,\hat\gamma_1^-,\hat\gamma_2^-,\hat\gamma_3^-,\hat\gamma_4^-).
$$

For example $\hat\gamma^0=P\otimes I_2\otimes I_2\otimes I_2$, $\hat\gamma^1=G\otimes P\otimes I_2\otimes I_2$ and $\hat\gamma^4=N\otimes I_2\otimes I_2\otimes I_2$.

**Theorem 2.4.** The $\hat\gamma^a$ are real 16 by 16 signed permutation matrices that satisfy $\{\hat\gamma^a,\hat\gamma^b\}=2\eta^{ab}I_{16}$ with $\eta=\mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1)$.

*Proof.* A Kronecker product of signed permutation matrices is a signed permutation matrix: each row of $A\otimes B$ combines one row of $A$ with one row of $B$ and so contains exactly one product of nonzero entries, and likewise for columns. By the mixed-product rule, products of these matrices are computed slot by slot.

*Squares.* In $(\hat\gamma_k^\pm)^2$ every slot is squared: $G^2=I$, $I^2=I$, $P^2=I$ and $N^2=-I$. So $(\hat\gamma_k^+)^2=+I_{16}$ and $(\hat\gamma_k^-)^2=-I_{16}$, as required for $a\le3$ and $a\ge4$.

*Same slot, $\hat\gamma_k^+$ and $\hat\gamma_k^-$.* The two products $\hat\gamma_k^+\hat\gamma_k^-$ and $\hat\gamma_k^-\hat\gamma_k^+$ agree in every slot except slot $k$, which is $PN$ in the first and $NP=-PN$ in the second. So they anticommute.

*Different slots $k<l$.* Take one matrix from slot $k$ (with $X=P$ or $N$ in slot $k$) and one from slot $l$ (with $Y=P$ or $N$ in slot $l$). Compare the two orders of multiplication slot by slot: in the slots before $k$ both matrices have $G$, and $GG=GG$; in slot $k$ the first has $X$ and the second $G$, and $XG=-GX$; in the slots strictly between $k$ and $l$ the first has $I_2$ and the second $G$, which commute; in slot $l$ the first has $I_2$ and the second $Y$, which commute; in the slots after $l$ both have $I_2$. Exactly one slot contributes a minus sign, so the two matrices anticommute. $\square$

**The chirality of this picture.** Define $\hat\gamma^8:=\hat\gamma^0\hat\gamma^1\cdots\hat\gamma^7$. Move $\hat\gamma^4=\hat\gamma_1^-$ to the right of $\hat\gamma^0=\hat\gamma_1^+$ (past three different factors, sign $(-1)^3$), then $\hat\gamma_2^-$ to the right of $\hat\gamma_2^+$ (two factors, $(-1)^2$), then $\hat\gamma_3^-$ to the right of $\hat\gamma_3^+$ (one factor, $-1$). The total sign is $(-1)^6=+1$, and

$$
\hat\gamma^8=(\hat\gamma_1^+\hat\gamma_1^-)(\hat\gamma_2^+\hat\gamma_2^-)(\hat\gamma_3^+\hat\gamma_3^-)(\hat\gamma_4^+\hat\gamma_4^-).
$$

Slot by slot, $\hat\gamma_k^+\hat\gamma_k^-$ has $G^2=I$ before slot $k$, $PN=-G$ in slot $k$ and $I_2$ after it. The product of the four pairs is therefore

$$
\hat\gamma^8=(-G)\otimes(-G)\otimes(-G)\otimes(-G)=G\otimes G\otimes G\otimes G .
$$

This is a diagonal matrix. Number the 16 basis columns by $j=8b_0+4b_1+2b_2+b_3$ with bits $b_0,\dots,b_3\in\{0,1\}$, one bit per slot (the first slot is the most significant, as in the index formula of the Kronecker product). Since $G=\mathrm{diag}(+1,-1)$, the diagonal entry of $\hat\gamma^8$ in position $j$ is $(-1)^{b_0+b_1+b_2+b_3}$: it is $-1$ exactly for the eight numbers $j\in\{1,2,4,7,8,11,13,14\}$, which have an odd number of 1-bits, and $+1$ for $j\in\{0,3,5,6,9,10,12,15\}$. These two lists reappear in Chapter 3.

**The charge matrix of this picture** is $C_{\mathrm{dm}}:=\hat\gamma^0\hat\gamma^1\hat\gamma^2\hat\gamma^3$. Slot by slot, with $G^2=I$,

$$
C_{\mathrm{dm}}=(PGGG)\otimes(PGG)\otimes(PG)\otimes P=(PG)\otimes P\otimes(PG)\otimes P=N\otimes P\otimes N\otimes P,
$$

using $PG=-N$ twice. The subscript dm stands for dirac-main. The repository checks that these tensor matrices satisfy the Clifford relation and equal dirac-main's committed generators (check `ALG_cliffordPictureIntertwiner`).

### 2.8 The notebook's gamma matrices T16^A

The author's notebook uses a different set of real 16 by 16 matrices, called (T16^A)[a] there. In this book they are written $\gamma^a$ without a hat, and they are the **primary gamma matrices** of the whole project (contract, §1). The notebook builds them in **block form** from eight real 8 by 8 matrices $\tau_a$ and eight partners $\bar\tau_a$:

$$
\gamma^a=\begin{pmatrix}0&\bar\tau_a\\ \tau_a&0\end{pmatrix}\qquad(a=0,\dots,7).
$$

Chapter 3 constructs the $\tau_a$ from 4 by 4 building blocks and explains their origin in the split octonions. For now we only need the finished matrices. Each $\gamma^a$ is a signed permutation matrix, so it can be written down completely in a small table: for each row $i$ the table gives the column $j$ of the single nonzero entry and its sign. The entry $-13$ in row 0 of the column $\gamma^4$ means $(\gamma^4)_{0,13}=-1$, that is, $(\gamma^4u)_0=-u_{13}$ for every column $u$; the entry $+0$ means $+u_0$, and $-0$ means $-u_0$.

| $i$ | $\gamma^0$ | $\gamma^1$ | $\gamma^2$ | $\gamma^3$ |
| --- | --- | --- | --- | --- |
| 0 | $+8$ | $-15$ | $+14$ | $-13$ |
| 1 | $+9$ | $-14$ | $-15$ | $+12$ |
| 2 | $+10$ | $+13$ | $-12$ | $-15$ |
| 3 | $+11$ | $+12$ | $+13$ | $+14$ |
| 4 | $+12$ | $-11$ | $+10$ | $-9$ |
| 5 | $+13$ | $-10$ | $-11$ | $+8$ |
| 6 | $+14$ | $+9$ | $-8$ | $-11$ |
| 7 | $+15$ | $+8$ | $+9$ | $+10$ |
| 8 | $+0$ | $+7$ | $-6$ | $+5$ |
| 9 | $+1$ | $+6$ | $+7$ | $-4$ |
| 10 | $+2$ | $-5$ | $+4$ | $+7$ |
| 11 | $+3$ | $-4$ | $-5$ | $-6$ |
| 12 | $+4$ | $+3$ | $-2$ | $+1$ |
| 13 | $+5$ | $+2$ | $+3$ | $-0$ |
| 14 | $+6$ | $-1$ | $+0$ | $+3$ |
| 15 | $+7$ | $-0$ | $-1$ | $-2$ |

| $i$ | $\gamma^4$ | $\gamma^5$ | $\gamma^6$ | $\gamma^7$ |
| --- | --- | --- | --- | --- |
| 0 | $-13$ | $+14$ | $+15$ | $+8$ |
| 1 | $+12$ | $+15$ | $-14$ | $+9$ |
| 2 | $+15$ | $-12$ | $+13$ | $+10$ |
| 3 | $-14$ | $-13$ | $-12$ | $+11$ |
| 4 | $+9$ | $-10$ | $-11$ | $-12$ |
| 5 | $-8$ | $-11$ | $+10$ | $-13$ |
| 6 | $-11$ | $+8$ | $-9$ | $-14$ |
| 7 | $+10$ | $+9$ | $+8$ | $-15$ |
| 8 | $+5$ | $-6$ | $-7$ | $-0$ |
| 9 | $-4$ | $-7$ | $+6$ | $-1$ |
| 10 | $-7$ | $+4$ | $-5$ | $-2$ |
| 11 | $+6$ | $+5$ | $+4$ | $-3$ |
| 12 | $-1$ | $+2$ | $+3$ | $+4$ |
| 13 | $+0$ | $+3$ | $-2$ | $+5$ |
| 14 | $+3$ | $-0$ | $+1$ | $+6$ |
| 15 | $-2$ | $-1$ | $-0$ | $+7$ |

The tables were generated from the function `notebook_gammas` of `scripts/d16c_exact.py`; the same matrices are stored exactly under the key `gamma` of the data file `algebra-fixture.json`. The Wolfram verifier also rebuilds them from the 11 verbatim definition cells of the notebook and finds them identical (within check `ALG_expression1`). Every row of every table points into the other half: rows 0 to 7 point to columns 8 to 15 and rows 8 to 15 to columns 0 to 7. That is the block form: the upper-left and lower-right blocks are zero.

**Three checks by hand.**

- $(\gamma^0)^2=+1$ in row 0: $(\gamma^0u)_0=u_8$ and row 8 of $\gamma^0$ says $(\gamma^0v)_8=v_0$, so $(\gamma^0\gamma^0u)_0=(\gamma^0u)_8=u_0$.
- $(\gamma^4)^2=-1$ in row 0: $(\gamma^4u)_0=-u_{13}$ and row 13 of $\gamma^4$ says $(\gamma^4v)_{13}=+v_0$, so $(\gamma^4\gamma^4u)_0=-(\gamma^4u)_{13}=-u_0$.
- $\gamma^0\gamma^4=-\gamma^4\gamma^0$ in row 0: $(\gamma^0\gamma^4u)_0=(\gamma^4u)_8=+u_5$ (row 8 of $\gamma^4$), while $(\gamma^4\gamma^0u)_0=-(\gamma^0u)_{13}=-u_5$ (row 13 of $\gamma^0$). The two differ by a sign.

**Facts about the notebook's gammas.**

(N1) *They satisfy the Clifford relation.* $\{\gamma^a,\gamma^b\}=2\eta^{ab}I_{16}$ for all 64 ordered pairs $(a,b)$, with squares $+1,+1,+1,+1,-1,-1,-1,-1$. In this chapter we take this from the exact machine check, which tests all 64 pairs (Stage 1, Result 3.1; check `ALG_clifford`). Chapter 3 proves it by hand, reducing it to a few 4 by 4 multiplications. The reader can also verify any single row with the tables, as above.

(N2) *They are orthogonal.* Each $\gamma^a$ is a signed permutation matrix, hence orthogonal (Section 2.2): $(\gamma^a)^T=(\gamma^a)^{-1}$.

(N3) *$\gamma^a$ is symmetric for $a\le3$ and antisymmetric for $a\ge4$.* *Proof.* By (N1), $(\gamma^a)^2=\eta^{aa}$, so $(\gamma^a)^{-1}=\eta^{aa}\gamma^a$. By (N2), $(\gamma^a)^T=(\gamma^a)^{-1}=\eta^{aa}\gamma^a$. $\square$ (Stage 1, Result 3.1; check `ALG_gammaTransposeSymmetry`.) The tensor matrices of Section 2.7 have the same pattern, since $P,G,I_2$ are symmetric and $N$ is antisymmetric.

(N4) *Their 256 monomials are a basis of $\mathrm{Mat}_{16}(\mathbb R)$.* This follows from Theorem 2.2. The computer confirms it independently: the 256 monomials, written as rows of 256 numbers, have rank 256, and the 128 even ones have rank 128 (Stage 1, Result 3.2; check `ALG_faithful`). The notebook itself tabulates the 256 ordered products of its gammas (its cell 594, according to the survey of the notebook in `handoff/surveys/`; we call it the notebook survey below).

### 2.9 The charge matrix $C=\sigma_{16}$ and expression [1]

**Definition.** The **charge matrix** is the product of the four space-like gammas,

$$
C:=\gamma^0\gamma^1\gamma^2\gamma^3 .
$$

In the notebook it is called σ16; the notebook itself identifies σ16 with the product of its first four gammas (cells 612 to 615, per the notebook survey). It is used to build the **Dirac adjoint** $\bar\Psi=\Psi^\dagger C$ of Chapter 6. We derive its properties from the Clifford relation and fact (N3) only, so they hold for the notebook's gammas and for the tensor picture alike.

**(C1) How $C$ commutes with the gammas:** $C\gamma^a=-\eta^{aa}\gamma^aC$. *Proof.* $C$ is the monomial with $A=\{0,1,2,3\}$, of degree 4. By (R3): for $a\le3$ ($a\in A$), $\gamma^aC=(-1)^3C\gamma^a=-C\gamma^a$; for $a\ge4$ ($a\notin A$), $\gamma^aC=(-1)^4C\gamma^a=C\gamma^a$. Both cases are $C\gamma^a=-\eta^{aa}\gamma^aC$. $\square$

**(C2) $C$ is symmetric.** *Proof.* $C^T=(\gamma^3)^T(\gamma^2)^T(\gamma^1)^T(\gamma^0)^T=\gamma^3\gamma^2\gamma^1\gamma^0$ by (N3). To restore the order, move $\gamma^0$ to the front (past three different factors), then $\gamma^1$ to the second place (two factors), then $\gamma^2$ to the third place (one factor): the sign is $(-1)^{3+2+1}=+1$. So $C^T=C$. $\square$

**(C3) $C^2=1$.** *Proof.* $C^2=CC^T=\gamma^0\gamma^1\gamma^2\gamma^3\gamma^3\gamma^2\gamma^1\gamma^0$. The two $\gamma^3$ in the middle give $(\gamma^3)^2=1$, then the two $\gamma^2$, and so on: $C^2=1$. $\square$

**(C4) Expression [1].** The task statement of the project contains, verbatim in WolframScript, the expression

```
\[Sigma]16.(T16^A)[#]==-Transpose[\[Sigma]16.(T16^A)[#]]&/@Range[0,7]
```

It asks whether $(C\gamma^a)^T=-C\gamma^a$ for $a=0,\dots,7$. *Proof that it holds.* $(C\gamma^a)^T=(\gamma^a)^TC^T=\eta^{aa}\gamma^aC$ by (N3) and (C2). By (C1), $\gamma^aC=-\eta^{aa}C\gamma^a$. Hence $(C\gamma^a)^T=\eta^{aa}(-\eta^{aa})C\gamma^a=-C\gamma^a$, because $(\eta^{aa})^2=1$. $\square$ The Wolfram verifier evaluates the expression literally and obtains {True, True, True, True, True, True, True, True} (Stage 1, Result 3.4; check `ALG_expression1`, measurement `ALG_expression1.listWolframForm`). Expression [1] is the reason why the notebook's Lagrangian carries no dynamics for a real Grassmann field (Chapter 5).

**(C5) The signature of $C$ is (8,8).** *Proof.* $C$ is a monomial of degree 4, so $\operatorname{tr}C=0$ by Theorem 2.1. With $C^2=1$ the projector argument of Section 2.2 gives eigenvalue $+1$ eight times and $-1$ eight times; $C$ is real symmetric, so its signature is (8,8). $\square$ (Stage 1, Result 3.3; check `ALG_chargeMatrix`, which also records the characteristic polynomial $(x-1)^8(x+1)^8$.)

**(C6) The notebook's $C$.** For the notebook's gammas the product is the block matrix

$$
C=\begin{pmatrix}-\sigma&0\\0&\sigma\end{pmatrix},\qquad\sigma=\begin{pmatrix}0&I_4\\ I_4&0\end{pmatrix},
$$

a signed permutation matrix (part of check `ALG_chargeMatrix`; Chapter 3 derives it by hand). Here it is as a table, together with the matrix $B$ of Section 2.12:

| $i$ | $C$ | $B/i$ |
| --- | --- | --- |
| 0 | $-4$ | $+9$ |
| 1 | $-5$ | $-8$ |
| 2 | $-6$ | $-11$ |
| 3 | $-7$ | $+10$ |
| 4 | $-0$ | $-13$ |
| 5 | $-1$ | $+12$ |
| 6 | $-2$ | $+15$ |
| 7 | $-3$ | $-14$ |
| 8 | $+12$ | $+1$ |
| 9 | $+13$ | $-0$ |
| 10 | $+14$ | $-3$ |
| 11 | $+15$ | $+2$ |
| 12 | $+8$ | $-5$ |
| 13 | $+9$ | $+4$ |
| 14 | $+10$ | $+7$ |
| 15 | $+11$ | $-6$ |

**Worked example: $C$ defines an indefinite form.** For a real column $u$ the number $u^TCu=\sum_{ij}u_iC_{ij}u_j$ can have either sign. With $u=e_0+e_4$ (components 0 and 4 equal to 1, all others 0) only the entries $C_{04}=C_{40}=-1$ contribute, and $u^TCu=-2$. With $u=e_8+e_{12}$ only $C_{8,12}=C_{12,8}=+1$ contribute, and $u^TCu=+2$. This is the matrix form of signature (8,8); it is why energies built with $C$ in Chapter 7 have no fixed sign.

### 2.10 The chirality $\gamma^8$ and the two halves

**Definition.** The **chirality** (or volume element) is the product of all eight gammas in increasing order,

$$
\gamma^8:=\gamma^0\gamma^1\gamma^2\gamma^3\gamma^4\gamma^5\gamma^6\gamma^7 .
$$

The label 8 is a name, not a ninth direction. In the notebook it is T16A[8] (cells 620 and 621, per the notebook survey).

**(X1) $(\gamma^8)^2=1$.** By (R2) with $k=8$: $(-1)^{8\cdot7/2}\prod_{a=0}^7\eta^{aa}=(-1)^{28}(+1)^4(-1)^4=+1$.

**(X2) $\gamma^8$ anticommutes with every $\gamma^a$.** By (R3) with $k=8$ and $a\in A$: $\gamma^a\gamma^8=(-1)^7\gamma^8\gamma^a=-\gamma^8\gamma^a$.

**(X3) $\gamma^8$ commutes with every even monomial and anticommutes with every odd one.** Passing $\gamma^8$ through a monomial of degree $k$ passes $k$ gammas, each giving $-1$ by (X2): the sign is $(-1)^k$. In particular $\gamma^8$ commutes with $C$ (degree 4) and with the spin generators $S^{ab}$ of Section 2.11 (degree 2).

**(X4) Eight $+1$'s and eight $-1$'s.** $\gamma^8$ is a monomial, so $\operatorname{tr}\gamma^8=0$ (Theorem 2.1); with (X1) and Section 2.2 it has the eigenvalue $+1$ eight times and $-1$ eight times.

**(X5) The notebook's chirality is diagonal:**

$$
\gamma^8=\begin{pmatrix}-I_8&0\\0&I_8\end{pmatrix}.
$$

(Stage 1, Result 3.6; check `ALG_chirality`; Chapter 3 derives it by hand.) In the tensor picture the chirality is $G\otimes G\otimes G\otimes G$ (Section 2.7), also diagonal but with a different pattern of signs; the two are related by the change of basis of Chapter 3.

**Chiral projectors and the two halves.** By Section 2.2 the matrices

$$
P_-:=\tfrac12\bigl(1-\gamma^8\bigr),\qquad P_+:=\tfrac12\bigl(1+\gamma^8\bigr)
$$

are projectors with $P_-+P_+=1$ and $P_-P_+=0$. For the notebook's gammas, (X5) gives $P_-=\mathrm{diag}(I_8,0)$ and $P_+=\mathrm{diag}(0,I_8)$. So the 16 components of a spinor split into two halves of 8:

- the upper components $\Psi_0,\dots,\Psi_7$ (the notebook's Ψ16upper) have chirality $-1$: $\gamma^8\Psi=-\Psi$ if only they are nonzero;
- the lower components $\Psi_8,\dots,\Psi_{15}$ (Ψ16lower) have chirality $+1$.

**(X6) Odd matrices exchange the halves, even matrices keep them.** From (X2), $\gamma^a(1-\gamma^8)=(1+\gamma^8)\gamma^a$, that is, $\gamma^aP_-=P_+\gamma^a$: a gamma maps the chirality $-1$ half into the chirality $+1$ half and vice versa. Even matrices commute with $\gamma^8$ (X3) and therefore map each half into itself.

This explains the block form of the notebook's gammas. Write any 16 by 16 matrix in blocks, $M=\begin{pmatrix}A&B\\ D&E\end{pmatrix}$. With $\gamma^8=\mathrm{diag}(-I_8,I_8)$,

$$
\gamma^8M=\begin{pmatrix}-A&-B\\ D&E\end{pmatrix},\qquad M\gamma^8=\begin{pmatrix}-A&B\\ -D&E\end{pmatrix}.
$$

$M$ anticommutes with $\gamma^8$ exactly when $A=E=0$ (block off-diagonal, like every $\gamma^a$), and commutes with it exactly when $B=D=0$ (block diagonal, like $C$ and every even monomial).

### 2.11 The spin generators $S^{ab}$ and the rotation of spinors

**Definition.** For $a,b=0,\dots,7$ the **spin generators** are

$$
S^{ab}:=\tfrac14\bigl[\gamma^a,\gamma^b\bigr]=\tfrac14\bigl(\gamma^a\gamma^b-\gamma^b\gamma^a\bigr).
$$

In the notebook they are SAB (Section title of cell 430, per the notebook survey), with 1-based list indices: SAB[[a+1,b+1]] is $S^{ab}$.

**(S1) Simple facts.** $S^{ba}=-S^{ab}$ and $S^{aa}=0$. For $a\ne b$ the two gammas anticommute, so $[\gamma^a,\gamma^b]=2\gamma^a\gamma^b$ and $S^{ab}=\tfrac12\gamma^a\gamma^b$.

**(S2) There are 28 independent ones.** The $S^{ab}$ with $a<b$ are one half times the $\binom82=28$ different monomials of degree 2, which are independent by Theorem 2.2. Of the 28, twelve have both indices of the same kind (6 pairs inside $\{0,1,2,3\}$ and 6 inside $\{4,5,6,7\}$), and sixteen mix a space-like with a time-like index.

**(S3) The spin generators rotate the gammas:**

$$
\bigl[S^{ab},\gamma^c\bigr]=\eta^{bc}\gamma^a-\eta^{ac}\gamma^b .
$$

*Proof.* For $a=b$ both sides vanish. For $a\ne b$ use the Clifford relation twice, first as $\gamma^b\gamma^c=2\eta^{bc}-\gamma^c\gamma^b$ and then as $\gamma^a\gamma^c=2\eta^{ac}-\gamma^c\gamma^a$:

$$
\gamma^a\gamma^b\gamma^c=2\eta^{bc}\gamma^a-\gamma^a\gamma^c\gamma^b=2\eta^{bc}\gamma^a-2\eta^{ac}\gamma^b+\gamma^c\gamma^a\gamma^b .
$$

Hence $[\gamma^a\gamma^b,\gamma^c]=\gamma^a\gamma^b\gamma^c-\gamma^c\gamma^a\gamma^b=2\eta^{bc}\gamma^a-2\eta^{ac}\gamma^b$, and dividing by 2 gives the claim. $\square$ (Stage 1, Result 3.5; part of check `ALG_spinTransposeProperties`.)

For a **Clifford vector** $v:=\sum_cv_c\gamma^c$ with numbers $v_c$ this reads $[S^{ab},v]=\eta^{bb}v_b\gamma^a-\eta^{aa}v_a\gamma^b$. For example $[S^{01},v]=v_1\gamma^0-v_0\gamma^1$: the components $(v_0,v_1)$ are turned a little in their plane and nothing else changes. The spin generators are the "infinitesimal rotations" of spinors.

**(S4) Finite transformations: the exponential.** For a square matrix $M$ define

$$
\exp(M):=\sum_{k=0}^\infty\frac{M^k}{k!}=1+M+\tfrac12M^2+\tfrac16M^3+\dots
$$

(the series converges for every square matrix, like the series of $e^x$; we quote this from analysis). If a matrix $J$ satisfies $J^2=-1$, then $J^{2m}=(-1)^m$ and $J^{2m+1}=(-1)^mJ$; splitting the series into even and odd powers and using the power series of cosine and sine (quoted from calculus),

$$
\exp(\varphi J)=\sum_m\frac{(-1)^m\varphi^{2m}}{(2m)!}+J\sum_m\frac{(-1)^m\varphi^{2m+1}}{(2m+1)!}=\cos\varphi+J\sin\varphi .
$$

If instead $J^2=+1$, the same steps with the series of $\cosh\varphi=\tfrac12(e^\varphi+e^{-\varphi})$ and $\sinh\varphi=\tfrac12(e^\varphi-e^{-\varphi})$ give $\exp(\varphi J)=\cosh\varphi+J\sinh\varphi$.

For $a\ne b$ put $J:=\gamma^a\gamma^b=2S^{ab}$. By (R2), $J^2=-\eta^{aa}\eta^{bb}$. So $\theta S^{ab}=\tfrac\theta2J$ and

$$
\exp(\theta S^{ab})=\begin{cases}\cos\tfrac\theta2+\gamma^a\gamma^b\sin\tfrac\theta2&\text{if }\eta^{aa}\eta^{bb}=+1\ \text{(a rotation)},\\[2pt] \cosh\tfrac\theta2+\gamma^a\gamma^b\sinh\tfrac\theta2&\text{if }\eta^{aa}\eta^{bb}=-1\ \text{(a boost)}.\end{cases}
$$

In both cases the inverse is obtained by $\theta\to-\theta$: $(c+sJ)(c-sJ)=c^2-s^2J^2$, which is $\cos^2+\sin^2=1$ for a rotation and $\cosh^2-\sinh^2=1$ for a boost.

**Worked example: a rotation by $2\pi$ gives $-1$.** Let $R(\theta)=\exp(\theta S^{01})=c+sJ$ with $J=\gamma^0\gamma^1$, $c=\cos\tfrac\theta2$, $s=\sin\tfrac\theta2$. By (R3), $J$ anticommutes with $\gamma^0$ and $\gamma^1$ and commutes with $\gamma^2,\dots,\gamma^7$. Therefore $R\gamma^0=(c+sJ)\gamma^0=\gamma^0(c-sJ)=\gamma^0R^{-1}$, and

$$
R\gamma^0R^{-1}=\gamma^0R^{-2}=\gamma^0(c-sJ)^2=\gamma^0\bigl(c^2-s^2-2csJ\bigr)=\gamma^0\bigl(\cos\theta-\sin\theta\,\gamma^0\gamma^1\bigr)=\cos\theta\,\gamma^0-\sin\theta\,\gamma^1 .
$$

In the same way $R\gamma^1R^{-1}=\gamma^1(\cos\theta-\sin\theta\,\gamma^0\gamma^1)=\cos\theta\,\gamma^1+\sin\theta\,\gamma^0$ (because $\gamma^1\gamma^0\gamma^1=-\gamma^0\gamma^1\gamma^1=-\gamma^0$), and $R\gamma^cR^{-1}=\gamma^c$ for $c\ge2$. So conjugation by $R(\theta)$ rotates the vector directions 0 and 1 by the angle $\theta$. But $R$ itself contains only half angles. At $\theta=2\pi$ the vectors are back where they started ($\cos2\pi=1$, $\sin2\pi=0$), while

$$
R(2\pi)=\cos\pi+\gamma^0\gamma^1\sin\pi=-1 .
$$

A full turn multiplies every spinor by $-1$; only a turn by $4\pi$ brings it back. This is the defining property of spinors, and it is why the spinor groups of Section 2.14 are "double covers" of the vector groups.

**Worked example: a boost.** For $R=\exp(\theta S^{04})=\cosh\tfrac\theta2+\sinh\tfrac\theta2\,\gamma^0\gamma^4$ the same steps, now with $(\gamma^0\gamma^4)^2=+1$, give

$$
R\gamma^0R^{-1}=\cosh\theta\,\gamma^0-\sinh\theta\,\gamma^4,\qquad R\gamma^4R^{-1}=\cosh\theta\,\gamma^4-\sinh\theta\,\gamma^0 .
$$

The pair of directions (0,4) is mixed by a hyperbolic rotation, which preserves $v_0^2-v_4^2$ because $\cosh^2\theta-\sinh^2\theta=1$. This is a Lorentz boost between the space direction $x_0$ and the time $x_4$.

**(S5) A transpose property.** $(CS^{ab})^T=-CS^{ab}$ for all $a,b$. *Proof.* For $a=b$ both sides vanish. For $a\ne b$, by (N3) and (C2),

$$
(CS^{ab})^T=\tfrac12(\gamma^b)^T(\gamma^a)^TC^T=\tfrac12\eta^{aa}\eta^{bb}\gamma^b\gamma^aC=-\tfrac12\eta^{aa}\eta^{bb}\gamma^a\gamma^bC .
$$

From (C1), $\gamma^aC=-\eta^{aa}C\gamma^a$ (multiply (C1) by $-\eta^{aa}$). Using it twice, $\gamma^a\gamma^bC=\eta^{aa}\eta^{bb}C\gamma^a\gamma^b$. So $(CS^{ab})^T=-\tfrac12(\eta^{aa}\eta^{bb})^2C\gamma^a\gamma^b=-CS^{ab}$. $\square$ Two related statements, that $C\{\gamma^c,S^{ab}\}$ is symmetric and $C[\gamma^c,S^{ab}]$ antisymmetric, are Exercise 2.8. The Wolfram verifier checks the first property for all 64 pairs and the other two for all 512 triples; the Python checker counts 476 verified identities of these kinds for $a<b$ (Stage 1, Result 3.5; check `ALG_spinTransposeProperties`).

**Consequence: exponentials preserve $C$.** Let $R=\exp(\theta S^{ab})=c+sJ$ as in (S4). From (S5) and $C^T=C$, $J^TC=(CJ)^T=-CJ$. Hence $R^TC=cC+sJ^TC=C(c-sJ)=CR^{-1}$, and

$$
R^TCR=C .
$$

This is the matrix fact behind the invariance of the Lagrangian under rotations and boosts (Chapter 6); Section 2.14 generalizes it to every element of the spinor groups.

### 2.12 The matrix $B=-iC\gamma^4$

**Definition.** $B:=-iC\gamma^4=-i\gamma^0\gamma^1\gamma^2\gamma^3\gamma^4$. It is $-i$ times a monomial of degree 5.

**(B1) $B$ is Hermitian.** $B^\dagger=(-i)^\ast(C\gamma^4)^T=i(\gamma^4)^TC^T=i(-\gamma^4)C=-i\gamma^4C$, using (N3) ($\gamma^4$ is antisymmetric) and (C2). By (C1) with $a=4$, $\gamma^4C=C\gamma^4$, so $B^\dagger=-iC\gamma^4=B$.

**(B2) $B^2=1$.** $B^2=(-i)^2C\gamma^4C\gamma^4=-CC\gamma^4\gamma^4=-(1)(-1)=1$, again using $\gamma^4C=C\gamma^4$.

**(B3) $B$ commutes with $C$, and $BC=-i\gamma^4$.** $BC=-iC\gamma^4C=-iC^2\gamma^4=-i\gamma^4$ and $CB=-iC^2\gamma^4=-i\gamma^4$.

**(B4) Signature (8,8).** $\operatorname{tr}B=-i\operatorname{tr}(\gamma^0\gamma^1\gamma^2\gamma^3\gamma^4)=0$ by Theorem 2.1; with (B2) and Section 2.2, $B$ has the eigenvalue $+1$ eight times and $-1$ eight times.

(Stage 1, Result 10.2; check `ALG_chargeFormB`, which records the multiplicities 8 and 8 and the identity $BC=-i\gamma^4$.)

For the notebook's gammas, $B$ is $i$ times the signed permutation in the table of Section 2.9; for example $(Bu)_0=i\,u_9$ and $(Bu)_9=-i\,u_0$, so that $B_{09}=i$ and $B_{90}=-i=(B_{09})^\ast$, as a Hermitian matrix requires.

**Where $B$ is used.** In the quantum theory of Chapter 8, $B$ is the matrix of the equal-time anticommutator of the field in the simplest (Gaussian normal) coordinates, $\{\Psi_a(x),\Psi^\dagger_b(y)\}=B_{ab}\,\delta^7(x-y)/\sqrt{|g|}$ (Stage 1, §10.3). Its signature (8,8) is the algebraic root of the indefinite ("Krein") inner product found there.

### 2.13 Groups and representations from zero

**Groups.** A **group** is a set $G$ with a product $gh$ such that: the product is associative, $(gh)k=g(hk)$; there is an identity element $e$ with $eg=ge=g$; and every $g$ has an inverse $g^{-1}$ with $gg^{-1}=g^{-1}g=e$. Examples: the nonzero real numbers under multiplication; the two numbers $\{+1,-1\}$ under multiplication; the invertible $d$ by $d$ matrices under matrix multiplication; the rotations of the plane. A **subgroup** is a subset that is itself a group with the same product. The subgroup **generated** by some elements is the set of all finite products of them and their inverses.

**Homomorphisms.** A map $\varphi$ from a group $G$ to a group $H$ is a **homomorphism** if $\varphi(gh)=\varphi(g)\varphi(h)$ for all $g,h$. Its **kernel** is the set of $g$ with $\varphi(g)=e$. Example: the determinant is a homomorphism from invertible matrices to nonzero numbers, $\det(AB)=\det A\det B$; its kernel is the set of matrices of determinant 1.

**Representations.** A **representation** of a group $G$ on $V=\mathbb R^d$ or $\mathbb C^d$ is a homomorphism $\rho$ from $G$ to the invertible $d$ by $d$ matrices: every group element $g$ becomes a matrix $\rho(g)$ that acts on columns, and $\rho(gh)=\rho(g)\rho(h)$. We then say that $G$ **acts** on $V$. A subspace $W\subseteq V$ (a subset closed under addition and multiplication by numbers) is **invariant** if $\rho(g)w\in W$ for every $g$ and every $w\in W$. The subspaces $\{0\}$ and $V$ are always invariant. The representation is **irreducible** if $V\ne\{0\}$ and there is no other invariant subspace: $V$ cannot be cut into smaller pieces that the group respects.

**Intertwiners, equivalence, commutant.** Let $\rho_1$ act on $V_1$ and $\rho_2$ on $V_2$. A matrix $T$ from $V_1$ to $V_2$ is an **intertwiner** if $T\rho_1(g)=\rho_2(g)T$ for all $g$. The two representations are **equivalent** if an *invertible* intertwiner exists; then $\rho_2(g)=T\rho_1(g)T^{-1}$, and the two representations are the same up to a change of basis. The intertwiners from a representation to itself form its **commutant**: the matrices that commute with every $\rho(g)$.

**Example: the field of numbers matters.** The rotations of the plane act on $\mathbb R^2$ by $R(\varphi)=\begin{pmatrix}\cos\varphi&-\sin\varphi\\ \sin\varphi&\cos\varphi\end{pmatrix}$. Over the real numbers this is irreducible: an invariant line would be a direction that every rotation maps to itself, and a rotation by $90°$ has no such direction. Over the complex numbers it is reducible: the column $w=(1,-i)^T$ satisfies

$$
R(\varphi)w=\begin{pmatrix}\cos\varphi+i\sin\varphi\\ \sin\varphi-i\cos\varphi\end{pmatrix}=e^{i\varphi}\begin{pmatrix}1\\-i\end{pmatrix},
$$

so the complex line through $w$ is invariant. This is why Stage 1 says precisely "irreducible *complex* representation".

**Lemma 2.5.** For an intertwiner $T$ from $\rho_1$ to $\rho_2$, the **kernel** $\{v:Tv=0\}$ is invariant under $\rho_1$ and the **image** $\{Tv\}$ is invariant under $\rho_2$. *Proof.* If $Tv=0$ then $T\rho_1(g)v=\rho_2(g)Tv=0$. And $\rho_2(g)(Tv)=T(\rho_1(g)v)$ lies in the image. $\square$

**Theorem 2.6 (Schur's lemma, first part).** An intertwiner between two irreducible representations is either zero or invertible. *Proof.* By Lemma 2.5 the kernel is $\{0\}$ or all of $V_1$, and the image is $\{0\}$ or all of $V_2$. If $T\ne0$, the kernel is not all of $V_1$, so it is $\{0\}$ ($T$ is one-to-one), and the image is not $\{0\}$, so it is $V_2$ ($T$ is onto). A one-to-one and onto linear map is invertible. $\square$

**Theorem 2.7 (span criterion).** Let $\rho$ be a representation of $G$ on $\mathbb C^d$ whose matrices $\rho(g)$ span, by complex linear combinations, all of $\mathrm{Mat}_d(\mathbb C)$. Then $\rho$ is irreducible, and its commutant consists of the multiples of $I$.

*Proof.* Let $W\ne\{0\}$ be invariant and pick $w\ne0$ in $W$. Since $W$ is invariant under every $\rho(g)$ and closed under linear combinations, it is invariant under every matrix. For any column $v$, the matrix $M=v\,w^\dagger/(w^\dagger w)$ satisfies $Mw=v$; hence $v\in W$, and $W=\mathbb C^d$. For the commutant: a matrix commuting with every $\rho(g)$ commutes with every linear combination, hence with every matrix, and the elementary-matrix argument of Corollary 2.3 shows that it is a multiple of $I$. $\square$

The second statement is the form of **Schur's lemma** that Stage 1 uses: here the commutant consists of the scalar matrices only. Section 2.15 also uses the commutant in the opposite direction: when a representation is a sum of two pieces, the size of its commutant tells whether the two pieces are equivalent.

### 2.14 Reflections, O(4,4), Pin(4,4) and Spin(4,4)

**Vectors inside the algebra.** To a vector $v=(v_0,\dots,v_7)$ of $\mathbb R^8$ we attach the matrix

$$
\gamma(v):=\sum_{a=0}^7v_a\gamma^a,
$$

and we write $\eta(u,v):=\sum_a\eta^{aa}u_av_a$ for the metric product of two vectors. The pairing argument of Section 2.3 gives

$$
\gamma(u)\gamma(v)+\gamma(v)\gamma(u)=2\eta(u,v)\,1,\qquad\gamma(v)^2=\eta(v,v)\,1 .
$$

A vector $u$ with $n(u):=\eta(u,u)=+1$ or $-1$ is a **unit vector**, and $n(u)$ is its **norm**. For a unit vector $\gamma(u)^2=n(u)$, so $\gamma(u)$ is invertible with $\gamma(u)^{-1}=n(u)\gamma(u)$. (A vector with $\eta(u,u)=0$, such as $u=e_0+e_4$, is called **null**; then $\gamma(u)^2=0$ and $\gamma(u)$ has no inverse, which is why null vectors are excluded below.)

**The groups O(4,4) and SO(4,4).** $\mathrm O(4,4)$ is the set of real 8 by 8 matrices $\Lambda$ that preserve the metric, $\eta(\Lambda u,\Lambda v)=\eta(u,v)$ for all $u,v$; in matrix form $\Lambda^T\eta\Lambda=\eta$. It is a group: products and inverses of such matrices again preserve $\eta$. Taking determinants, $(\det\Lambda)^2\det\eta=\det\eta$, and $\det\eta=(+1)^4(-1)^4=1$, so $\det\Lambda=\pm1$. The elements with $\det\Lambda=+1$ form the subgroup $\mathrm{SO}(4,4)$. These are the "Lorentz transformations" of the 4+4 dimensional flat spacetime, including those that reverse orientation.

**Reflections.** For a unit vector $u$ define the **reflection in the hyperplane orthogonal to $u$**:

$$
R_u(v):=v-2\,\frac{\eta(u,v)}{\eta(u,u)}\,u .
$$

It sends $u$ to $u-2u=-u$ and leaves every $w$ with $\eta(u,w)=0$ unchanged. The vectors $w$ with $\eta(u,w)=0$ form a 7-dimensional subspace (the solutions of one nonzero linear equation), and $u$ does not lie in it because $\eta(u,u)\ne0$. In a basis made of $u$ and seven vectors of that subspace, $R_u=\mathrm{diag}(-1,1,1,1,1,1,1,1)$; hence $R_u^2=1$ and $\det R_u=-1$. $R_u$ preserves $\eta$ (Exercise 2.11), so $R_u\in\mathrm O(4,4)$ but $R_u\notin\mathrm{SO}(4,4)$.

**The key identity.** For a unit vector $u$ and any vector $v$,

$$
-\gamma(u)\,\gamma(v)\,\gamma(u)^{-1}=\gamma\bigl(R_u(v)\bigr).
$$

*Proof.* From the anticommutator, $\gamma(u)\gamma(v)=2\eta(u,v)-\gamma(v)\gamma(u)$. Multiply on the right by $\gamma(u)^{-1}=n(u)\gamma(u)$:

$$
\gamma(u)\gamma(v)\gamma(u)^{-1}=2\eta(u,v)\,n(u)\,\gamma(u)-\gamma(v)=-\gamma\Bigl(v-2\frac{\eta(u,v)}{\eta(u,u)}u\Bigr),
$$

because $n(u)=\eta(u,u)=1/\eta(u,u)$ when $\eta(u,u)=\pm1$. $\square$ So conjugation by a unit vector is a reflection, up to a sign.

**Definition of Pin(4,4) and Spin(4,4).** $\mathrm{Pin}(4,4)$ is the set of all products

$$
g=\gamma(u_1)\gamma(u_2)\cdots\gamma(u_k)
$$

of finitely many unit vectors ($k=0,1,2,\dots$; the empty product is 1). It is a group: the product of two such products is again one, and $g^{-1}=\gamma(u_k)^{-1}\cdots\gamma(u_1)^{-1}$ with $\gamma(u)^{-1}=\gamma(n(u)u)$, again a unit vector. $\mathrm{Spin}(4,4)$ is the subgroup of products with an **even** number $k$ of factors. Every element acts on spinors by matrix multiplication, $\Psi\mapsto g\Psi$ (Stage 1, §4.2). Examples: each $\gamma^a$ is a unit vector ($n=\eta^{aa}$), so $\gamma^a\in\mathrm{Pin}(4,4)$; the numbers $1=\gamma^0\gamma^0$ and $-1=\gamma^4\gamma^4$ lie in $\mathrm{Spin}(4,4)$; every monomial is $\pm$ a product of gammas and so lies in $\mathrm{Pin}(4,4)$, in $\mathrm{Spin}(4,4)$ if it is even; and $\exp(\theta S^{ab})$ lies in $\mathrm{Spin}(4,4)$, because (Section 2.11) $\cos\tfrac\theta2+\sin\tfrac\theta2\gamma^a\gamma^b=\gamma^a\bigl(\cos\tfrac\theta2\,\eta^{aa}\gamma^a+\sin\tfrac\theta2\,\gamma^b\bigr)$ is a product of two unit vectors of norm $\eta^{aa}$ (and similarly with cosh and sinh for a boost, where $\cosh^2-\sinh^2=1$ gives the norm).

**The parity is well defined.** A product of $k$ vectors is, by (R1), a combination of monomials whose degrees all have the parity of $k$ (the degree of $\gamma_A\gamma_B=\pm\gamma_{A\triangle B}$ has the parity of $|A|+|B|$). If an element could be written both with an even and with an odd number of factors, it would be both a combination of even monomials and a combination of odd monomials, hence zero (Section 2.6), which is impossible for an invertible matrix. So every $g$ has a definite **parity** $|g|\in\{0,1\}$ (0 for even, 1 for odd), and we put $\alpha(g):=(-1)^{|g|}g$.

**Theorem 2.8 (spinor norm).** For $g=\gamma(u_1)\cdots\gamma(u_k)\in\mathrm{Pin}(4,4)$,

$$
g^TCg=(-1)^k\,N(g)\,C,\qquad N(g):=n(u_1)\,n(u_2)\cdots n(u_k)=\pm1 .
$$

*Proof.* First, $C\gamma(u)^TC^{-1}=-\gamma(u)$ for every vector: by (N3) and (C1), $C(\gamma^a)^TC^{-1}=\eta^{aa}C\gamma^aC^{-1}=\eta^{aa}(-\eta^{aa}\gamma^a)=-\gamma^a$, and the rest is linearity. Hence $Cg^TC^{-1}=(C\gamma(u_k)^TC^{-1})\cdots(C\gamma(u_1)^TC^{-1})=(-1)^k\gamma(u_k)\cdots\gamma(u_1)$, and, since $C^{-1}=C$, $g^TC=(-1)^kC\,\gamma(u_k)\cdots\gamma(u_1)$. Multiplying by $g$ on the right, the product $\gamma(u_k)\cdots\gamma(u_1)\gamma(u_1)\cdots\gamma(u_k)$ collapses from the middle, $\gamma(u_1)^2=n(u_1)$, then $\gamma(u_2)^2=n(u_2)$, and so on. $\square$

The number $N(g)$ is the **spinor norm**. The formula shows that it depends only on $g$, not on how $g$ is written as a product, and that $N(gh)=N(g)N(h)$. Examples: $N(\gamma^0)=+1$, $N(\gamma^4)=-1$, $N(\gamma^0\gamma^4)=-1$, and $N(\exp(\theta S^{ab}))=+1$ (it is a product of two unit vectors of equal norm). For a spinor, $\Psi\mapsto g\Psi$ multiplies the bilinear $\Psi^\dagger C\Psi$ by $(-1)^kN(g)$, because $(g\Psi)^\dagger C(g\Psi)=\Psi^\dagger g^TCg\Psi$ for a real $g$; for a single unit vector the factor is $-n(u)$. This is the "Pin character" of Stage 1 (§7.7; check `ALG_pinLiftCharacter`), which Chapter 6 uses.

**Theorem 2.9 (how spinor transformations move vectors).** For every $g\in\mathrm{Pin}(4,4)$ there are matrices $\Lambda_{\mathrm t}(g)$ and $\Lambda_{\mathrm u}(g)$ in $\mathrm O(4,4)$ with

$$
\alpha(g)\,\gamma(v)\,g^{-1}=\gamma\bigl(\Lambda_{\mathrm t}(g)v\bigr),\qquad g\,\gamma(v)\,g^{-1}=\gamma\bigl(\Lambda_{\mathrm u}(g)v\bigr)\qquad\text{for all }v .
$$

Both are homomorphisms, $\Lambda_{\mathrm t}(\gamma(u))=R_u$, $\Lambda_{\mathrm u}(\gamma(u))=-R_u$, $\Lambda_{\mathrm u}(g)=(-1)^{|g|}\Lambda_{\mathrm t}(g)$, and $\det\Lambda_{\mathrm t}(g)=\det\Lambda_{\mathrm u}(g)=(-1)^{|g|}$.

*Proof.* For one unit vector, $\alpha(\gamma(u))=-\gamma(u)$ and the key identity gives $\Lambda_{\mathrm t}(\gamma(u))=R_u$; without the sign, $\Lambda_{\mathrm u}(\gamma(u))=-R_u$. For a product $gh$, parities add, so $\alpha(gh)=\alpha(g)\alpha(h)$ and

$$
\alpha(gh)\gamma(v)(gh)^{-1}=\alpha(g)\bigl(\alpha(h)\gamma(v)h^{-1}\bigr)g^{-1}=\alpha(g)\,\gamma\bigl(\Lambda_{\mathrm t}(h)v\bigr)\,g^{-1}=\gamma\bigl(\Lambda_{\mathrm t}(g)\Lambda_{\mathrm t}(h)v\bigr).
$$

So $\Lambda_{\mathrm t}(g)$ exists for every product, is a product of reflections (hence in $\mathrm O(4,4)$), and $\Lambda_{\mathrm t}(gh)=\Lambda_{\mathrm t}(g)\Lambda_{\mathrm t}(h)$. The untwisted version differs by the sign $(-1)^{|g|}$ and is a homomorphism for the same reason; $-1_8$ is in $\mathrm O(4,4)$. Determinants: $\det R_u=-1$ and $\det(-R_u)=(-1)^8\det R_u=-1$, so a product of $k$ factors has determinant $(-1)^k$ under both maps. $\square$

The map $\Lambda_{\mathrm t}$ with the factor $\alpha$ is the **twisted adjoint action** and $\Lambda_{\mathrm u}$ the **untwisted** one (Stage 1, §4.2; contract §2). They agree on $\mathrm{Spin}(4,4)$. The computer confirms, for several unit vectors, that the untwisted matrix lies exactly in $\mathrm O(4,4)$ (check `ALG_pinLiftCharacter`).

**Theorem 2.10 (the kernel is $\{\pm1\}$).** $\Lambda_{\mathrm t}(g)=1_8$ exactly when $g=\pm1$, and the same holds for $\Lambda_{\mathrm u}$.

*Proof.* Both $\pm1$ lie in $\mathrm{Spin}(4,4)$ and act trivially. Conversely, let $\Lambda_{\mathrm t}(g)=1_8$, that is, $\alpha(g)\gamma^a=\gamma^ag$ for all $a$.

- If $g$ is even, $\alpha(g)=g$, so $g$ commutes with every $\gamma^a$. By Corollary 2.3, $g=c\cdot1$ with a real number $c$. Theorem 2.8 with even $k$ gives $c^2C=N(g)C$, so $c^2=N(g)=\pm1$; a real $c$ has $c^2=1$, hence $c=\pm1$.
- If $g$ is odd, $\alpha(g)=-g$, so $g$ anticommutes with every $\gamma^a$. Then $g\gamma^8$ commutes with every $\gamma^a$: $g\gamma^8\gamma^a=-g\gamma^a\gamma^8=\gamma^ag\gamma^8$, by (X2). By Corollary 2.3, $g\gamma^8=c\cdot1$, so $g=c\gamma^8$ (since $(\gamma^8)^2=1$). But $\gamma^8$ is an even monomial and $g$ is odd; a nonzero matrix cannot be both, so $c=0$ and $g=0$, impossible.

For $\Lambda_{\mathrm u}$ the even case is identical, and in the odd case $g$ would commute with every $\gamma^a$, so $g=c\cdot1$ would be even: impossible. $\square$

**Onto, and the double cover (quoted theorem).** The **Cartan–Dieudonné theorem** of linear algebra states that every element of $\mathrm O(4,4)$ is a product of at most 8 reflections $R_u$ in non-null vectors, which may be normalized to unit vectors. We quote it without proof; it is not machine-checked in the repository. With it, $\Lambda_{\mathrm t}$ maps $\mathrm{Pin}(4,4)$ **onto** $\mathrm O(4,4)$. Together with Theorem 2.10: if $\Lambda_{\mathrm t}(g)=\Lambda_{\mathrm t}(h)$, then $\Lambda_{\mathrm t}(gh^{-1})=1_8$, so $g=\pm h$. Every element of $\mathrm O(4,4)$ is the image of exactly two elements $\pm g$: **Pin(4,4) is a double cover of O(4,4)**. Since determinants are $(-1)^{|g|}$, the even elements are exactly those mapped into $\mathrm{SO}(4,4)$, and **Spin(4,4) is a double cover of SO(4,4)**: in the words of the README, Spin(4,4) consists of "the determinant-1 transformations". The untwisted map is onto $\mathrm O(4,4)$ as well: on even elements it agrees with $\Lambda_{\mathrm t}$, and on odd elements it is $-\Lambda_{\mathrm t}$; multiplication by $-1_8$, whose determinant is $+1$ in 8 dimensions, maps the determinant $-1$ part of $\mathrm O(4,4)$ onto itself. (Stage 1 records the stronger fact that $-1_8$ lies in the part of $\mathrm{SO}(4,4)$ connected to $1_8$: it is the product of rotations by $\pi$ in the planes (0,1), (2,3), (4,5) and (6,7).) The rotation by $2\pi$ of Section 2.11 shows the double cover at work: $R(2\pi)=-1$ and $R(0)=1$ have the same vector image $1_8$.

**"Determinant 1" refers to the vector image.** As 16 by 16 matrices, all elements of $\mathrm{Pin}(4,4)$ have determinant $+1$. *Proof.* For a unit vector $u$, $\gamma(u)$ is traceless (a combination of traceless monomials). If $n(u)=+1$, $\gamma(u)^2=1$ and Section 2.2 gives eight eigenvalues $+1$ and eight $-1$, so $\det\gamma(u)=(+1)^8(-1)^8=1$. If $n(u)=-1$, $\gamma(u)^2=-1$ and Section 2.2 gives $\det\gamma(u)=1$ as well. A product of determinant-1 matrices has determinant 1. $\square$ So the spinor determinant does not distinguish $\mathrm{Spin}(4,4)$ from $\mathrm{Pin}(4,4)$; "determinant 1" always means $\det\Lambda(g)=1$ (Stage 1, §4.2).

**The part connected to 1.** The products of exponentials $\exp(\theta S^{ab})$ form a subgroup of $\mathrm{Spin}(4,4)$, called $\mathrm{Spin}_0(4,4)$; Stage 1 calls it the identity component (the elements that can be reached from 1 by a continuous path, a topological description that we do not need). Every element of it has spinor norm $N=+1$, because $N$ is multiplicative and $N(\exp(\theta S^{ab}))=+1$. Since $N(\gamma^0\gamma^4)=-1$, the element $\gamma^0\gamma^4$ of $\mathrm{Spin}(4,4)$ is *not* a product of exponentials: $\mathrm{Spin}(4,4)$ contains more than its part connected to 1. By Theorem 2.8, elements of $\mathrm{Spin}(4,4)$ with $N=-1$ reverse the sign of $\Psi^\dagger C\Psi$; Chapter 6 uses this to decide which transformations are symmetries of the Lagrangian.

### 2.15 The representation theorem

We can now prove the central theorem of this chapter (Stage 1, §4.3 and §4.4; contract §2). In this section "the gammas" are the notebook's, so that $\gamma^8=\mathrm{diag}(-I_8,I_8)$ by (X5); the statements hold for any 16 by 16 gammas of signature (4,4) after the change of basis that diagonalizes $\gamma^8$.

**Theorem 2.11 (irreducibility under Pin(4,4)).** The representation $g\mapsto g$ of $\mathrm{Pin}(4,4)$ on $\mathbb C^{16}$ is irreducible, and its commutant consists of the multiples of $I_{16}$.

*Proof.* Every monomial is a product of gammas, and each $\gamma^a$ is a unit vector; so every monomial lies in $\mathrm{Pin}(4,4)$, up to a sign that can be absorbed because $-1\in\mathrm{Pin}(4,4)$. Hence the span of $\mathrm{Pin}(4,4)$ contains the 256 monomials, which span all real 16 by 16 matrices (Section 2.6), and with complex coefficients all of $\mathrm{Mat}_{16}(\mathbb C)$. Theorem 2.7 gives both claims. $\square$

**Theorem 2.12 (two inequivalent halves under Spin(4,4)).** Let $\mathbb C^8_-$ and $\mathbb C^8_+$ be the images of $P_-$ and $P_+$: the columns whose lower, respectively upper, eight components vanish. Then

1. both halves are invariant under $\mathrm{Spin}(4,4)$;
2. the span of $\mathrm{Spin}(4,4)$ is the set of all block-diagonal matrices $\mathrm{diag}(X,Y)$ with arbitrary $X,Y\in\mathrm{Mat}_8(\mathbb C)$;
3. each half is an irreducible representation of $\mathrm{Spin}(4,4)$ whose commutant consists of the multiples of $I_8$;
4. the two halves are **inequivalent**: the only intertwiner between them is zero;
5. the commutant of $\mathrm{Spin}(4,4)$ on $\mathbb C^{16}$ is two-dimensional, spanned by $P_-$ and $P_+$.

*Proof.* (1) Every element of $\mathrm{Spin}(4,4)$ is a combination of even monomials, which commute with $\gamma^8$ (X3) and are therefore block diagonal (Section 2.10); a block-diagonal matrix maps each half into itself.

(2) Every even monomial is $\pm$ an element of $\mathrm{Spin}(4,4)$, and every element of $\mathrm{Spin}(4,4)$ is a combination of even monomials, so the two spans agree. The 128 even monomials are independent (Section 2.6) and block diagonal. The real block-diagonal matrices form a set of dimension $64+64=128$, so the even monomials are a basis of it; with complex coefficients they span all complex block-diagonal matrices.

(3) By (2), the upper-left blocks $X$ of the matrices in the span run through all of $\mathrm{Mat}_8(\mathbb C)$ (take $Y=0$), and so do the lower-right blocks. Theorem 2.7, applied to each half, gives irreducibility and scalar commutants.

(4) An intertwiner is an 8 by 8 matrix $T$ with $Tg_-=g_+T$ for every $g=\mathrm{diag}(g_-,g_+)$ in $\mathrm{Spin}(4,4)$. By linearity $TX=YT$ for every $\mathrm{diag}(X,Y)$ in the span, and by (2) we may choose $X=I_8$ and $Y=0$: then $T=0$. So there is no invertible intertwiner, and the halves are inequivalent. The same argument works from $\mathbb C^8_+$ to $\mathbb C^8_-$.

(5) Write a matrix that commutes with the span in blocks, $Z=\begin{pmatrix}Z_{11}&Z_{12}\\ Z_{21}&Z_{22}\end{pmatrix}$. Commuting with $\mathrm{diag}(X,Y)$ means $Z_{11}X=XZ_{11}$, $Z_{22}Y=YZ_{22}$, $Z_{12}Y=XZ_{12}$ and $Z_{21}X=YZ_{21}$ for all $X,Y$. The first two force $Z_{11}=a\,I_8$ and $Z_{22}=b\,I_8$ (the elementary-matrix argument); the last two, with $X=I_8$, $Y=0$ and with $X=0$, $Y=I_8$, force $Z_{12}=Z_{21}=0$. So $Z=aP_-+bP_+$. $\square$

Had the two halves been equivalent through an invertible $T$, the matrix $\begin{pmatrix}0&0\\ T&0\end{pmatrix}$ would also commute with $\mathrm{Spin}(4,4)$ and the commutant would be four-dimensional (a copy of $\mathrm{Mat}_2(\mathbb C)$). The computed dimension 2 therefore also proves inequivalence; this is the form of the argument in Stage 1 (§4.4).

**Remarks.**

- The odd elements of $\mathrm{Pin}(4,4)$, such as the $\gamma^a$ themselves, exchange the two halves (X6). That is why $\mathrm{Pin}(4,4)$ sees one block of 16 while $\mathrm{Spin}(4,4)$ sees two blocks of 8.
- The theorem holds unchanged for $\mathrm{Spin}_0(4,4)$: its span also contains every $\gamma^a\gamma^b$ ($a\ne b$), since for a rotation $\exp(\pi S^{ab})=\gamma^a\gamma^b$, and for a boost $\exp(\theta S^{ab})-\exp(-\theta S^{ab})=2\sinh\tfrac\theta2\,\gamma^a\gamma^b$; products of these give every even monomial.
- The notebook's matrices are real, so the same splitting holds for real spinors, $\mathbb R^{16}=\Delta_-\oplus\Delta_+$; dirac16complex uses the complex version $\mathbb C\otimes(\Delta_-\oplus\Delta_+)$ (Stage 1, §4.5), with components that are, in addition, Grassmann-odd (Chapter 5 and Chapter 6).
- The vector space $\mathbb R^8$ and the two halves $\Delta_-$ and $\Delta_+$ are all 8-dimensional. The notebook remarks on these three 8-dimensional representations of Spin(4,4) (cell 669, per the notebook survey); the symmetry that permutes them is called **triality**. It is a standard fact that this book neither proves nor uses; Chapter 3 shows the concrete identification of all three spaces with the split octonions.

**What the computer computed.** The Python checker writes the commutant condition $\gamma^aX-X\gamma^a=0$ ($a=0,\dots,7$) for an unknown 16 by 16 matrix $X$ as $8\cdot256=2048$ linear equations in the 256 unknowns $X_{ij}$, with integer coefficients, and solves them by exact Gaussian elimination with fractions (functions `intertwiner_equations` and `nullspace` of `scripts/d16c_exact.py`); the Wolfram verifier does the same with its own code. The solution space has dimension exactly 1 (the scalar matrices), which is Theorem 2.11 in computed form (Stage 1, Result 4.1; check `ALG_pinIrreducibleComplex`). Gaussian elimination only adds, subtracts, multiplies and divides the integer coefficients, so it runs identically whether complex or only rational solutions are allowed; the dimension over the complex numbers is the same. For the 28 spin generators (whose products give all even monomials, so they have the same commutant as $\mathrm{Spin}(4,4)$), the computed commutant has dimension 2 and is spanned by $P_-$ and $P_+$; every $S^{ab}$ and every even monomial is block diagonal; the commutants of the two blocks have dimensions (1, 1); the even monomials restricted to each block have rank (64, 64); and the intertwiner spaces between the blocks have dimensions (0, 0) in both directions (Stage 1, Result 4.2; check `ALG_spinDecomposition`). Every one of these numbers is predicted by Theorem 2.12.
