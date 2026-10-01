## 1. Mathematical toolkit from zero

The physics of this book is written in a small number of mathematical languages: vectors and matrices, complex numbers, indices with a summation rule, derivatives of functions of several variables, and metrics, which measure lengths in spaces whose directions need not all behave alike. This chapter builds these languages from school algebra and the calculus of one variable. Every later chapter uses them. The examples are deliberately small (two or three dimensions, matrices of size $2\times2$), because every rule that holds for them holds in the same form for the eight dimensions and $16\times16$ matrices of the rest of the book.

Where a standard fact of mathematics is used without proof, the text says so, and Section 1.13 lists all such facts.

### 1.1 Numbers, lists, sums and powers

**Numbers.** We use the natural numbers $0$, $1$, $2$, $3$, and so on (we include 0), the integers, which also contain the negative whole numbers $-1$, $-2$, $-3$, and so on, the fractions (rational numbers) such as $-7/3$, and the real numbers, which include numbers like $\sqrt2$ and $\pi$ that are not fractions. The set of real numbers is written $\mathbb R$. The symbol $\in$ means "is an element of": $x\in\mathbb R$ says that $x$ is a real number. An **open interval** $(a,b)$ is the set of real numbers $x$ with $a<x<b$; for example $z\in(0,\pi/2)$ means $0<z<\pi/2$. Complex numbers are introduced in Section 1.5.

**Functions.** A function $f$ assigns to each allowed input exactly one output. A function of several variables takes several inputs, such as $f(x_0,x_4)=x_0^2\sin x_4$, which assigns to the pair $(x_0,x_4)$ the number $x_0^2\sin x_4$.

**Lists, counted from 0.** A list (also called a tuple) is an ordered collection of entries. This book counts entries from 0: the list $(x_0,x_1,\dots,x_7)$ has the eight entries $x_0$ to $x_7$, entry number $k$ is $x_k$, and the last entry has the number 7, one less than the number of entries. In the list $(5,7,2)$ entry 0 is 5, entry 1 is 7 and entry 2 is 2. Counting from 0 is a convention (Chapter 0); it is the convention of every document of the project, and it makes many formulas shorter.

**Sums and products.** The symbol $\sum$ (capital Greek sigma) abbreviates a sum and $\prod$ (capital pi) a product:

$$
\sum_{k=0}^{n-1}a_k=a_0+a_1+\dots+a_{n-1},\qquad \prod_{k=0}^{n-1}a_k=a_0\,a_1\cdots a_{n-1}.
$$

The letter $k$ is a **dummy index**: it can be renamed without changing the value, $\sum_{k=0}^{3}k^2=\sum_{j=0}^{3}j^2=0+1+4+9=14$. Two rules follow from the ordinary laws of arithmetic and are used constantly: a constant factor can be taken out of a sum, $\sum_kc\,a_k=c\sum_ka_k$, and a sum of sums can be added term by term, $\sum_k(a_k+b_k)=\sum_ka_k+\sum_kb_k$. A double sum $\sum_j\sum_k a_{jk}$ adds all entries $a_{jk}$ of a rectangular array, and it can be done in either order, because addition is commutative and associative.

**Powers and roots.** For positive real numbers $a,b$ and real exponents $p,q$:

$$
a^pa^q=a^{p+q},\qquad (a^p)^q=a^{pq},\qquad (ab)^p=a^pb^p,\qquad a^{-p}=\frac1{a^p},\qquad \sqrt a=a^{1/2}.
$$

These rules are school algebra and are used here without proof. They are exactly the rules that decide whether a simplification is correct. For example, for $0<s$ and real $a$,

$$
\frac1{\sqrt{s^{1/3}/e^{2a}}}=\Bigl(\frac{s^{1/3}}{e^{2a}}\Bigr)^{-1/2}=\frac{(s^{1/3})^{-1/2}}{(e^{2a})^{-1/2}}=\frac{s^{-1/6}}{e^{-a}}=\frac{e^{a}}{s^{1/6}} .
$$

Exercise 1.3 uses this computation to check a substitution rule of the author's notebook.

**Elementary functions.** We use the exponential function $e^x$, its inverse, the natural logarithm $\ln x$ (for $x>0$), and the trigonometric functions $\sin$, $\cos$, $\tan=\sin/\cos$ and $\cot=\cos/\sin$, with $\cos^2x+\sin^2x=1$ and the addition theorems

$$
\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta,\qquad \sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta ,
$$

which are also school mathematics and are used without proof. The hyperbolic functions are defined by

$$
\cosh x=\frac{e^x+e^{-x}}2,\qquad \sinh x=\frac{e^x-e^{-x}}2 .
$$

They satisfy $\cosh^2x-\sinh^2x=1$. Proof: $\cosh^2x-\sinh^2x=\tfrac14\bigl[(e^{2x}+2+e^{-2x})-(e^{2x}-2+e^{-2x})\bigr]=\tfrac14\cdot4=1$.

### 1.2 Vectors

**Definition.** A **vector** with $n$ components is a column of $n$ numbers,

$$
v=\begin{pmatrix}v_0\\ v_1\\ \vdots\\ v_{n-1}\end{pmatrix}.
$$

The numbers $v_0,\dots,v_{n-1}$ are its **components**, counted from 0. Vectors with the same number of components are added component by component, and a vector is multiplied by a number $c$ (a **scalar**) by multiplying every component:

$$
(v+w)_k=v_k+w_k,\qquad (cv)_k=c\,v_k,\qquad k=0,\dots,n-1 .
$$

The **zero vector** $0$ has all components 0. The set of all vectors with $n$ real components is written $\mathbb R^n$; with complex components (Section 1.5) it is written $\mathbb C^n$. The fields of this book have sixteen components at every point, written $\Psi=(\Psi_0,\dots,\Psi_{15})^T$ (the $T$ is explained in Section 1.3). For the commuting field dirac16complex00 the components are complex numbers, so at each point $\Psi$ is a vector in $\mathbb C^{16}$. For dirac16complex they are complex anticommuting (Grassmann) quantities, introduced in Chapter 5. Matrices act on them by the same rule $(A\Psi)_i=\sum_jA_{ij}\Psi_j$ (Section 1.3), but a product of two components changes sign when the two factors are exchanged (Section 1.8 and Chapter 5).

**Example.** In $\mathbb R^3$, with $v=(1,2,0)^T$ and $w=(0,1,1)^T$: $v+w=(1,3,1)^T$ and $3v=(3,6,0)^T$.

**Linear combinations and bases.** A **linear combination** of vectors $u_0,\dots,u_{m-1}$ is a vector $c_0u_0+\dots+c_{m-1}u_{m-1}$ with numbers $c_k$. The vectors are **linearly independent** when the only linear combination that gives the zero vector is the one with all $c_k=0$; otherwise they are **linearly dependent**, and then one of them is a linear combination of the others (if $\sum_kc_ku_k=0$ with some $c_j\ne0$, then $u_j=-\sum_{k\ne j}(c_k/c_j)\,u_k$). The **standard basis** of $\mathbb R^n$ consists of the $n$ vectors $e_0,\dots,e_{n-1}$, where $e_k$ has the component 1 in place $k$ and 0 elsewhere. Every vector is a linear combination of them, $v=\sum_{k=0}^{n-1}v_ke_k$, because component $j$ of the right-hand side is $\sum_kv_k(e_k)_j=v_j$ (only the term $k=j$ contributes). The standard basis vectors are linearly independent: $\sum_kc_ke_k$ is the vector with components $c_k$, and it is zero only if every $c_k$ is zero.

A **basis** is a list of linearly independent vectors of which every vector is a linear combination; the expansion coefficients are then unique (if $v=\sum_kc_ku_k=\sum_kc'_ku_k$, then $\sum_k(c_k-c'_k)u_k=0$, so $c_k=c'_k$ for every $k$ by independence). All bases of $\mathbb R^n$ (or $\mathbb C^n$) have exactly $n$ vectors; this number is the **dimension**. (This last fact is standard linear algebra and is used without proof.) The dimension counts basis vectors, not vectors: $\mathbb R^2$ contains infinitely many vectors but has dimension 2.

**Example.** In $\mathbb R^2$ the vectors $(1,1)^T$ and $(1,-1)^T$ are linearly independent: $c_0(1,1)^T+c_1(1,-1)^T=(c_0+c_1,\,c_0-c_1)^T$ is zero only if $c_0+c_1=0$ and $c_0-c_1=0$, that is $c_0=c_1=0$. The vectors $(1,2)^T$ and $(2,4)^T$ are linearly dependent, since $2(1,2)^T-(2,4)^T=0$.

### 1.3 Matrices

**Definition.** A **matrix** with $m$ rows and $n$ columns (an $m\times n$ matrix) is a rectangular array of numbers $A_{ij}$, where $i=0,\dots,m-1$ numbers the row and $j=0,\dots,n-1$ the column. A vector with $n$ components is an $n\times1$ matrix. Matrices of the same shape are added entry by entry and multiplied by numbers entry by entry.

**Matrix times vector.** An $m\times n$ matrix $A$ turns a vector $v$ with $n$ components into a vector $Av$ with $m$ components:

$$
(Av)_i=\sum_{j=0}^{n-1}A_{ij}v_j .
$$

Component $i$ of $Av$ is row $i$ of $A$ multiplied entry by entry with $v$ and added. For example

$$
\begin{pmatrix}1&2\\ 3&4\end{pmatrix}\begin{pmatrix}5\\ 6\end{pmatrix}=\begin{pmatrix}1\cdot5+2\cdot6\\ 3\cdot5+4\cdot6\end{pmatrix}=\begin{pmatrix}17\\ 39\end{pmatrix}.
$$

The map $v\mapsto Av$ is **linear**: $A(v+w)=Av+Aw$ and $A(cv)=c\,Av$, as follows directly from the formula.

**Matrix product.** The product of an $m\times n$ matrix $A$ and an $n\times p$ matrix $B$ is the $m\times p$ matrix

$$
(AB)_{ik}=\sum_{j=0}^{n-1}A_{ij}B_{jk} .
$$

It is defined so that $(AB)v=A(Bv)$ for every vector $v$: component $i$ of $A(Bv)$ is $\sum_jA_{ij}\sum_kB_{jk}v_k=\sum_k\bigl(\sum_jA_{ij}B_{jk}\bigr)v_k$. Example:

$$
\begin{pmatrix}1&2\\ 0&1\end{pmatrix}\begin{pmatrix}0&1\\ 1&0\end{pmatrix}=\begin{pmatrix}1\cdot0+2\cdot1&1\cdot1+2\cdot0\\ 0\cdot0+1\cdot1&0\cdot1+1\cdot0\end{pmatrix}=\begin{pmatrix}2&1\\ 1&0\end{pmatrix}.
$$

In the other order the same two matrices give $\begin{pmatrix}0&1\\ 1&0\end{pmatrix}\begin{pmatrix}1&2\\ 0&1\end{pmatrix}=\begin{pmatrix}0&1\\ 1&2\end{pmatrix}$, a different matrix. **Matrix multiplication is not commutative**: in general $AB\ne BA$. This single fact is the reason why the order of factors matters in every formula of this book. Matrix multiplication is, however, **associative**, $(AB)C=A(BC)$: both sides have the entries $\sum_j\sum_kA_{ij}B_{jk}C_{kl}$, and it is **distributive**, $A(B+C)=AB+AC$ and $(A+B)C=AC+BC$.

**Special matrices.** A **square** matrix has as many rows as columns. The **identity matrix** $I_n$ (or simply $I$, or $1$) is the $n\times n$ matrix with 1 on the diagonal ($i=j$) and 0 elsewhere; $Iv=v$ and $IA=AI=A$. Its entries are written with the **Kronecker delta**, $\delta_{ij}=1$ if $i=j$ and $0$ otherwise. A **diagonal matrix** has zero entries off the diagonal; $\mathrm{diag}(d_0,\dots,d_{n-1})$ denotes the diagonal matrix with diagonal $d_0,\dots,d_{n-1}$. Two diagonal matrices are multiplied by multiplying their diagonals: $\mathrm{diag}(d_k)\,\mathrm{diag}(d'_k)=\mathrm{diag}(d_kd'_k)$, so diagonal matrices commute with each other.

**Transpose.** The **transpose** $A^T$ of an $m\times n$ matrix is the $n\times m$ matrix with $(A^T)_{ij}=A_{ji}$: rows become columns. The transpose of a column vector is a row vector, which is why we write $v=(v_0,\dots,v_{n-1})^T$ to save space. The transpose of a product is the product of the transposes in the reverse order,

$$
(AB)^T=B^TA^T .
$$

Proof: $((AB)^T)_{ki}=(AB)_{ik}=\sum_jA_{ij}B_{jk}=\sum_j(B^T)_{kj}(A^T)_{ji}=(B^TA^T)_{ki}$. For three factors, $(ABC)^T=C^TB^TA^T$ by applying the rule twice.

**Symmetric and antisymmetric matrices.** A square matrix is **symmetric** if $A^T=A$ ($A_{ij}=A_{ji}$) and **antisymmetric** if $A^T=-A$ ($A_{ij}=-A_{ji}$). The diagonal of an antisymmetric matrix is zero, because $A_{ii}=-A_{ii}$ forces $A_{ii}=0$. Every square matrix $M$ is, in exactly one way, the sum of a symmetric and an antisymmetric matrix:

$$
M=M_S+M_A,\qquad M_S=\tfrac12(M+M^T),\qquad M_A=\tfrac12(M-M^T).
$$

Proof: $M_S^T=\tfrac12(M^T+M)=M_S$, $M_A^T=\tfrac12(M^T-M)=-M_A$, and $M_S+M_A=M$. If also $M=S+A$ with $S$ symmetric and $A$ antisymmetric, then $M^T=S-A$, so $S=\tfrac12(M+M^T)=M_S$ and $A=M_A$: the split is unique. This split decides, in Chapter 5, which parts of the notebook's Lagrangian survive for anticommuting fields.

**Trace.** The **trace** of a square matrix is the sum of its diagonal entries, $\mathrm{tr}A=\sum_iA_{ii}$. Although $AB\ne BA$ in general, the two products have the same trace:

$$
\mathrm{tr}(AB)=\sum_i\sum_jA_{ij}B_{ji}=\sum_j\sum_iB_{ji}A_{ij}=\mathrm{tr}(BA).
$$

In the example above both products have trace 2.

**Inverse.** A square matrix $A$ is **invertible** if there is a matrix $A^{-1}$ with $AA^{-1}=A^{-1}A=I$. For a $2\times2$ matrix,

$$
A=\begin{pmatrix}a&b\\ c&d\end{pmatrix},\qquad A^{-1}=\frac1{ad-bc}\begin{pmatrix}d&-b\\ -c&a\end{pmatrix}\qquad(ad-bc\ne0),
$$

which is checked by multiplying out: $\begin{pmatrix}a&b\\ c&d\end{pmatrix}\begin{pmatrix}d&-b\\ -c&a\end{pmatrix}=\begin{pmatrix}ad-bc&0\\ 0&ad-bc\end{pmatrix}$. The inverse of a product is the product of the inverses in reverse order, $(AB)^{-1}=B^{-1}A^{-1}$, because $(AB)(B^{-1}A^{-1})=A(BB^{-1})A^{-1}=AA^{-1}=I$ (and similarly in the other order). A diagonal matrix $\mathrm{diag}(d_k)$ with all $d_k\ne0$ has the inverse $\mathrm{diag}(1/d_k)$.

**Block matrices.** A large matrix can be cut into smaller matrices, called blocks, and multiplied block by block as if the blocks were numbers, provided the order of the factors inside each block product is kept. For matrices cut into $2\times2$ blocks of matching sizes,

$$
\begin{pmatrix}A&B\\ C&D\end{pmatrix}\begin{pmatrix}E&F\\ G&H\end{pmatrix}=\begin{pmatrix}AE+BG&AF+BH\\ CE+DG&CF+DH\end{pmatrix}.
$$

Proof: an entry of the product in, say, the upper-left block is a sum over the column index of the first factor; splitting that sum into the columns belonging to the first block column and those belonging to the second gives exactly the entry of $AE$ plus the entry of $BG$. A case that occurs throughout the book is the off-diagonal block matrix

$$
M=\begin{pmatrix}0&X\\ Y&0\end{pmatrix},\qquad M^2=\begin{pmatrix}0\cdot0+XY&0\cdot X+X\cdot0\\ Y\cdot0+0\cdot Y&YX+0\cdot0\end{pmatrix}=\begin{pmatrix}XY&0\\ 0&YX\end{pmatrix}.
$$

The notebook builds its $16\times16$ gamma matrices in exactly this form, with $8\times8$ blocks (Chapters 2 and 3). For square matrices $D_0,\dots,D_{k-1}$, $\mathrm{diag}(D_0,\dots,D_{k-1})$ denotes the block matrix with these blocks on the diagonal and zero blocks elsewhere; for example $M^2=\mathrm{diag}(XY,YX)$ above, and $\mathrm{diag}(-I_8,I_8)$ is the $16\times16$ diagonal matrix with eight entries $-1$ followed by eight entries $+1$.

**Tensor (Kronecker) product.** For an $m\times m$ matrix $A$ and an $n\times n$ matrix $B$, the **tensor product** $A\otimes B$ is the $mn\times mn$ matrix made of an $m\times m$ arrangement of $n\times n$ blocks, block $(i,j)$ being $A_{ij}B$. For $2\times2$ matrices:

$$
A\otimes B=\begin{pmatrix}A_{00}B&A_{01}B\\ A_{10}B&A_{11}B\end{pmatrix},\qquad \text{for example}\qquad \begin{pmatrix}1&0\\ 0&-1\end{pmatrix}\otimes\begin{pmatrix}0&1\\ 1&0\end{pmatrix}=\begin{pmatrix}0&1&0&0\\ 1&0&0&0\\ 0&0&0&-1\\ 0&0&-1&0\end{pmatrix}.
$$

It obeys the **mixed-product rule** $(A\otimes B)(C\otimes D)=(AC)\otimes(BD)$. Proof: by the block rule, block $(i,k)$ of the product is $\sum_j(A_{ij}B)(C_{jk}D)=\bigl(\sum_jA_{ij}C_{jk}\bigr)BD=(AC)_{ik}\,BD$, which is block $(i,k)$ of $(AC)\otimes(BD)$. Four-fold tensor products of $2\times2$ matrices give $16\times16$ matrices; this is the second standard way of writing the gamma matrices of this book (the tensor-product picture of Section 2.7; Section 3.11 relates it to the notebook's matrices).

### 1.4 Determinants

**The $2\times2$ case.** The **determinant** of a $2\times2$ matrix is

$$
\det\begin{pmatrix}a&b\\ c&d\end{pmatrix}=ad-bc .
$$

It is the factor by which the matrix changes areas (up to sign): the square with corners $0$, $e_0$, $e_1$, $e_0+e_1$ is mapped to the parallelogram spanned by the two columns of the matrix, whose area is $|ad-bc|$ (a fact of plane geometry, used here without proof and not needed later in the book).

The determinant of a product is the product of the determinants. For $2\times2$ matrices this is a direct computation: with $A=\begin{pmatrix}a&b\\ c&d\end{pmatrix}$ and $B=\begin{pmatrix}e&f\\ g&h\end{pmatrix}$,

$$
\begin{aligned}
\det(AB)&=(ae+bg)(cf+dh)-(af+bh)(ce+dg)\\
&=aecf+aedh+bgcf+bgdh-afce-afdg-bhce-bhdg\\
&=ad(eh-fg)-bc(eh-fg)=\det A\,\det B ,
\end{aligned}
$$

where in the second line the terms $aecf$ and $afce$ cancel, and so do $bgdh$ and $bhdg$. Consequently a $2\times2$ matrix is invertible exactly when its determinant is not zero: if $ad-bc\ne0$, the formula of Section 1.3 gives the inverse, and if $A$ is invertible, then $\det A\,\det A^{-1}=\det I=1$, so $\det A\ne0$.

**Permutations and their signs.** A **permutation** of $(0,1,\dots,n-1)$ is a reordering $(\sigma(0),\sigma(1),\dots,\sigma(n-1))$ of these numbers. An **inversion** of $\sigma$ is a pair of places $i<j$ with $\sigma(i)>\sigma(j)$. The **sign** of $\sigma$ is $\mathrm{sgn}\,\sigma=(-1)^{\text{number of inversions}}$: $+1$ for an even and $-1$ for an odd number of inversions. For $n=3$ the six permutations are

| permutation | inversions | sign |
| --- | --- | --- |
| (0,1,2) | none | $+1$ |
| (1,2,0) | (1,0), (2,0) | $+1$ |
| (2,0,1) | (2,0), (2,1) | $+1$ |
| (1,0,2) | (1,0) | $-1$ |
| (0,2,1) | (2,1) | $-1$ |
| (2,1,0) | (2,1), (2,0), (1,0) | $-1$ |

(an inversion is listed by the two entries that stand in the wrong order). Exchanging two entries of a permutation always changes its sign; this is a standard fact that we use without proof.

**The general determinant.** For an $n\times n$ matrix,

$$
\det A=\sum_{\sigma}\mathrm{sgn}(\sigma)\,A_{0\sigma(0)}A_{1\sigma(1)}\cdots A_{n-1\,\sigma(n-1)},
$$

the sum running over all $n!$ permutations. Each term takes exactly one entry from every row and from every column. For $n=2$ the permutations $(0,1)$ and $(1,0)$ give $A_{00}A_{11}-A_{01}A_{10}$, the formula above. For $n=3$ the six permutations of the table give

$$
\det A=A_{00}A_{11}A_{22}+A_{01}A_{12}A_{20}+A_{02}A_{10}A_{21}-A_{01}A_{10}A_{22}-A_{00}A_{12}A_{21}-A_{02}A_{11}A_{20}.
$$

For a **diagonal** matrix every term except the one of the identity permutation contains an off-diagonal entry, which is zero, so

$$
\det\mathrm{diag}(d_0,\dots,d_{n-1})=d_0d_1\cdots d_{n-1}.
$$

This formula is used in Section 1.11 to compute the determinant of the metric of the primordial field.

Four further facts hold for every $n$ and are used without proof: $\det(AB)=\det A\det B$ (proved above for $n=2$); $\det A^T=\det A$; a square matrix $M$ is invertible exactly when $\det M\ne0$ (proved above for $n=2$); and a square matrix $M$ is invertible exactly when $Mv=0$ has only the solution $v=0$. (One direction of the last fact is immediate: if $M$ is invertible and $Mv=0$, then $v=M^{-1}Mv=M^{-1}0=0$. The other direction, that $M$ is invertible whenever $Mv=0$ forces $v=0$, is the part used without proof.) Together the last two facts say:

$$
Mv=0\ \text{has a solution}\ v\ne0\quad\text{exactly when}\quad \det M=0 .
$$

**Example.** For the matrix with rows $(1,2,0)$, $(0,1,1)$, $(1,3,1)$ the $3\times3$ formula gives $1\cdot1\cdot1+2\cdot1\cdot1+0-2\cdot0\cdot1-1\cdot1\cdot3-0=1+2-3=0$. The determinant vanishes because the third row is the sum of the first two, so the rows are linearly dependent.

### 1.5 Complex numbers

**Definition.** The equation $x^2=-1$ has no real solution. We introduce a new number $i$ with $i^2=-1$ and consider all numbers $z=a+ib$ with real $a$ and $b$; they are the **complex numbers**, and their set is $\mathbb C$. The real number $a=\mathrm{Re}\,z$ is the real part and $b=\mathrm{Im}\,z$ the imaginary part. Complex numbers are added and multiplied with the ordinary rules of algebra, replacing $i^2$ by $-1$ wherever it appears:

$$
(a+ib)+(c+id)=(a+c)+i(b+d),\qquad (a+ib)(c+id)=(ac-bd)+i(ad+bc).
$$

For example $(1+2i)(3-i)=3-i+6i-2i^2=5+5i$.

**Conjugate and modulus.** The **complex conjugate** of $z=a+ib$ is $z^\ast=a-ib$. The product $zz^\ast=a^2+b^2$ is real and not negative; its square root $|z|=\sqrt{a^2+b^2}$ is the **modulus** of $z$. Every $z\ne0$ has the inverse

$$
\frac1z=\frac{z^\ast}{zz^\ast}=\frac{z^\ast}{|z|^2},\qquad\text{for example}\qquad \frac1{1+i}=\frac{1-i}{2}.
$$

Conjugation respects sums and products, $(z+w)^\ast=z^\ast+w^\ast$ and $(zw)^\ast=z^\ast w^\ast$. Proof of the second rule: with $z=a+ib$ and $w=c+id$, $(zw)^\ast=(ac-bd)-i(ad+bc)$, and $z^\ast w^\ast=(a-ib)(c-id)=ac-iad-ibc+i^2bd=(ac-bd)-i(ad+bc)$. It follows that $|zw|^2=zw\,z^\ast w^\ast=|z|^2|w|^2$. A number is real exactly when $z^\ast=z$, and purely imaginary (of the form $ib$) exactly when $z^\ast=-z$.

**The complex exponential.** For real $\theta$ we define

$$
e^{i\theta}=\cos\theta+i\sin\theta .
$$

This definition has the property that justifies the notation, the law of exponents:

$$
e^{i\alpha}e^{i\beta}=(\cos\alpha\cos\beta-\sin\alpha\sin\beta)+i(\sin\alpha\cos\beta+\cos\alpha\sin\beta)=\cos(\alpha+\beta)+i\sin(\alpha+\beta)=e^{i(\alpha+\beta)},
$$

by the addition theorems of Section 1.1. Moreover $|e^{i\theta}|^2=\cos^2\theta+\sin^2\theta=1$ and $(e^{i\theta})^\ast=\cos\theta-i\sin\theta=e^{-i\theta}$.

**Derivatives of complex-valued functions.** A complex-valued function $f(\theta)=a(\theta)+i\,b(\theta)$ of a real variable, with real functions $a$ and $b$, is differentiated part by part: $f'=a'+i\,b'$. The sum rule $(f+g)'=f'+g'$ follows at once. The product rule $(fg)'=f'g+fg'$ also holds. Proof: with $g=c+id$ ($c$, $d$ real), the multiplication rule above gives $fg=(ac-bd)+i(ad+bc)$. Applying the real product rule to each of the four products and regrouping,

$$
\begin{aligned}
(fg)'&=(a'c+ac'-b'd-bd')+i(a'd+ad'+b'c+bc')\\
&=\bigl[(a'c-b'd)+i(a'd+b'c)\bigr]+\bigl[(ac'-bd')+i(ad'+bc')\bigr]=f'g+fg' ,
\end{aligned}
$$

because the first bracket is $(a'+ib')(c+id)$ and the second is $(a+ib)(c'+id')$. The same part-by-part rule is used for matrices with complex entries in Section 1.9. With it, the derivative of $e^{i\theta}=\cos\theta+i\sin\theta$ with respect to $\theta$ is

$$
\frac{d}{d\theta}e^{i\theta}=-\sin\theta+i\cos\theta=i(\cos\theta+i\sin\theta)=i\,e^{i\theta},
$$

the same rule as for the real exponential with the constant $i$ in place of a real constant. For a general complex number $z=x+iy$ we define $e^z=e^xe^{iy}$; then $e^ze^w=e^{z+w}$ for all complex $z,w$, by the two laws of exponents. Every complex number can be written in **polar form** $z=r\,e^{i\theta}$ with $r=|z|$ and a real angle $\theta$: for $z=a+ib\ne0$ the point $(a/r,b/r)$ of the plane has distance 1 from the origin, so it is $(\cos\theta,\sin\theta)$ for some angle $\theta$ (a fact of school trigonometry, used without proof), and then $z=r(\cos\theta+i\sin\theta)$. Multiplying by $e^{i\alpha}$ rotates $z$ by the angle $\alpha$ without changing its modulus, since $re^{i\theta}e^{i\alpha}=re^{i(\theta+\alpha)}$. A factor $e^{i\alpha}$ is called a **phase**.

A wave that oscillates in time, such as $e^{-i\varepsilon x_4}$ with a real $\varepsilon$, has modulus 1 at every time. If $\varepsilon$ is imaginary, $\varepsilon=i\gamma$ with real $\gamma>0$, the same expression is $e^{\gamma x_4}$, which grows without bound; this is how "imaginary frequencies" signal an instability in Chapter 8.

**Complex vectors and matrices.** Vectors and matrices may have complex entries; all rules of Sections 1.2 to 1.4 hold unchanged. The conjugate $A^\ast$ of a matrix conjugates every entry, and the **Hermitian conjugate** (or adjoint) is

$$
A^\dagger=(A^\ast)^T,\qquad (A^\dagger)_{ij}=(A_{ji})^\ast .
$$

For a column vector $v$, $v^\dagger$ is the row of conjugated components. Like the transpose, the Hermitian conjugate reverses products, $(AB)^\dagger=B^\dagger A^\dagger$: indeed $(AB)^\ast=A^\ast B^\ast$ entry by entry (by the product rule of conjugation), and the transpose reverses the order. The number

$$
v^\dagger w=\sum_kv_k^\ast w_k
$$

is the **scalar product** of two complex vectors, and $v^\dagger v=\sum_k|v_k|^2$ is real, not negative, and zero only for $v=0$. It is the squared length of $v$. Two vectors are **orthogonal** if their scalar product is zero, $v^\dagger w=0$; the order does not matter, because $(v^\dagger w)^\ast=\sum_kv_kw_k^\ast=w^\dagger v$, so $v^\dagger w=0$ exactly when $w^\dagger v=0$. A vector has **length 1** if $v^\dagger v=1$. For real vectors $v^\dagger w=\sum_kv_kw_k$, which is the dot product of Section 1.11.

A square matrix is **Hermitian** if $A^\dagger=A$, **anti-Hermitian** if $A^\dagger=-A$, and **unitary** if $U^\dagger U=I$. A unitary matrix preserves scalar products: $(Uv)^\dagger(Uw)=v^\dagger U^\dagger Uw=v^\dagger w$. Four facts are used repeatedly:

1. A real symmetric matrix is Hermitian, and a real antisymmetric matrix is anti-Hermitian. Proof: for a real matrix $A^\ast=A$, so $A^\dagger=A^T$.
2. If $A$ is anti-Hermitian, then $iA$ is Hermitian: $(iA)^\dagger=i^\ast A^\dagger=(-i)(-A)=iA$.
3. For a Hermitian $H$ and every vector $v$ the number $v^\dagger Hv$ is real. Proof: a $1\times1$ matrix equals its transpose, so $(v^\dagger Hv)^\ast=(v^\dagger Hv)^\dagger=v^\dagger H^\dagger(v^\dagger)^\dagger=v^\dagger Hv$.
4. For an anti-Hermitian $A$ the number $v^\dagger Av$ is purely imaginary, by the same computation with $A^\dagger=-A$.

**Example.** $A=\begin{pmatrix}1&i\\ -i&2\end{pmatrix}$ is Hermitian: $A^T=\begin{pmatrix}1&-i\\ i&2\end{pmatrix}$, and conjugating every entry gives back $A$. The real antisymmetric matrix $\begin{pmatrix}0&-1\\ 1&0\end{pmatrix}$ is anti-Hermitian, and $i$ times it, $\begin{pmatrix}0&-i\\ i&0\end{pmatrix}$, is Hermitian. In Chapter 6 fact 1 is the reason why the kinetic term of the dirac16complex Lagrangian needs no factor $i$: the matrices $C\gamma^a$ are real and antisymmetric, hence anti-Hermitian.

### 1.6 Eigenvalues and eigenvectors

**Definition.** A number $\lambda$ is an **eigenvalue** of a square matrix $A$, with **eigenvector** $v\ne0$, if

$$
Av=\lambda v .
$$

The matrix acts on its eigenvectors like multiplication by a number. Since $Av=\lambda v$ is the same as $(\lambda I-A)v=0$, and such a $v\ne0$ exists exactly when $\det(\lambda I-A)=0$ (Section 1.4), the eigenvalues are the roots of the **characteristic polynomial**

$$
p(x)=\det(xI-A).
$$

For a $2\times2$ matrix $A=\begin{pmatrix}a&b\\ c&d\end{pmatrix}$,

$$
p(x)=(x-a)(x-d)-bc=x^2-(a+d)x+(ad-bc)=x^2-(\mathrm{tr}A)\,x+\det A .
$$

If $\lambda_0$ and $\lambda_1$ are the two roots, then $p(x)=(x-\lambda_0)(x-\lambda_1)=x^2-(\lambda_0+\lambda_1)x+\lambda_0\lambda_1$, and comparing coefficients gives $\mathrm{tr}A=\lambda_0+\lambda_1$ and $\det A=\lambda_0\lambda_1$: the trace is the sum and the determinant the product of the eigenvalues. (The same holds for every $n$, counting each eigenvalue as often as it occurs as a root; we use this without proof.)

**Examples.** For $X=\begin{pmatrix}0&1\\ 1&0\end{pmatrix}$, $p(x)=x^2-1=(x-1)(x+1)$: the eigenvalues are $+1$, with eigenvector $(1,1)^T$, and $-1$, with eigenvector $(1,-1)^T$; indeed $X(1,1)^T=(1,1)^T$ and $X(1,-1)^T=(-1,1)^T=-(1,-1)^T$. For $Y=\begin{pmatrix}0&-1\\ 1&0\end{pmatrix}$, $p(x)=x^2+1$, whose roots are $+i$ and $-i$: a real matrix can have complex eigenvalues, which is one reason why complex numbers are needed even when all matrices are real.

**Multiplicity.** A root may occur several times. The notation $p(x)=(x-1)^8(x+1)^8$ means that $+1$ and $-1$ each occur eight times; this is the characteristic polynomial of the $16\times16$ matrix $C$ of Chapter 2 (Stage-1 document, Result 3.3). For the Hermitian matrices of this book the multiplicity of an eigenvalue equals the number of linearly independent eigenvectors that belong to it (a standard theorem, used without proof).

**Squares equal to $\pm I$.** If $A^2=I$, every eigenvalue is $+1$ or $-1$: from $Av=\lambda v$ follows $v=A^2v=\lambda Av=\lambda^2v$, so $\lambda^2=1$. If $A^2=-I$, the same argument gives $\lambda^2=-1$, so $\lambda=\pm i$. The gamma matrices of Chapter 2 square to $+I$ or $-I$, so their eigenvalues are known at once.

**Projectors.** A matrix with $P^2=P$ is a **projector**. If $A^2=I$, the two matrices

$$
P_+=\tfrac12(I+A),\qquad P_-=\tfrac12(I-A)
$$

are projectors with $P_++P_-=I$ and $P_+P_-=P_-P_+=0$, and $AP_\pm=\pm P_\pm$. Proof: $P_+^2=\tfrac14(I+2A+A^2)=\tfrac14(2I+2A)=P_+$, similarly $P_-^2=P_-$; $P_+P_-=\tfrac14(I-A^2)=0$; and $AP_\pm=\tfrac12(A\pm A^2)=\tfrac12(A\pm I)=\pm P_\pm$. So $P_+$ keeps the part of a vector with eigenvalue $+1$ and removes the part with eigenvalue $-1$, and $P_-$ does the opposite. Every vector splits as $v=P_+v+P_-v$. The chirality projectors $P_\mp=\tfrac12(1\mp\gamma^8)$ of Chapter 2 are of this kind.

**Hermitian matrices have real eigenvalues.** If $H^\dagger=H$ and $Hv=\lambda v$ with $v\ne0$, then $v^\dagger Hv=\lambda\,v^\dagger v$. The left side is real (fact 3 of Section 1.5) and $v^\dagger v>0$, so $\lambda$ is real. Moreover, eigenvectors of a Hermitian matrix that belong to different eigenvalues are orthogonal: if $Hv=\lambda v$ and $Hw=\mu w$ with $\lambda\ne\mu$, then $w^\dagger Hv=\lambda\,w^\dagger v$, and also $w^\dagger Hv=(Hw)^\dagger v=\mu\,w^\dagger v$ (using $H^\dagger=H$ and $\mu^\ast=\mu$), so $(\lambda-\mu)\,w^\dagger v=0$ and $w^\dagger v=0$. A stronger standard theorem, the **spectral theorem**, says that every Hermitian $n\times n$ matrix has $n$ eigenvectors that are orthogonal to each other and of length 1; it is used without proof.

### 1.7 Commutators and anticommutators

Because matrices need not commute, two combinations of a product and its reverse are given names. The **commutator** and the **anticommutator** of two square matrices are

$$
[A,B]=AB-BA,\qquad \{A,B\}=AB+BA .
$$

$A$ and $B$ **commute** if $[A,B]=0$ and **anticommute** if $\{A,B\}=0$, that is $AB=-BA$. Directly from the definitions: $[B,A]=-[A,B]$, $\{B,A\}=\{A,B\}$, $\{A,A\}=2A^2$, $[A,A]=0$, and every product splits into the two parts,

$$
AB=\tfrac12[A,B]+\tfrac12\{A,B\}.
$$

The commutator obeys a product rule (the **Leibniz rule**), which is proved by writing out both sides:

$$
[A,BC]=[A,B]\,C+B\,[A,C],\qquad\text{since}\qquad ABC-BCA=(AB-BA)C+B(AC-CA).
$$

**A worked example that anticipates Chapter 2.** Take the three real $2\times2$ matrices

$$
X=\begin{pmatrix}0&1\\ 1&0\end{pmatrix},\qquad Z=\begin{pmatrix}1&0\\ 0&-1\end{pmatrix},\qquad Y=\begin{pmatrix}0&-1\\ 1&0\end{pmatrix}.
$$

Multiplying out,

$$
XZ=\begin{pmatrix}0&-1\\ 1&0\end{pmatrix}=Y,\qquad ZX=\begin{pmatrix}0&1\\ -1&0\end{pmatrix}=-Y,\qquad X^2=Z^2=I,\qquad Y^2=-I .
$$

Hence $\{X,Z\}=0$ and $[X,Z]=2Y$. Further, $XY=X(XZ)=X^2Z=Z$ and $YX=XZX=X(ZX)=-X(XZ)=-Z$, so $\{X,Y\}=0$; and $ZY=Z(XZ)=(ZX)Z=-XZ^2=-X$ and $YZ=XZ^2=X$, so $\{Z,Y\}=0$.

A word on notation before the relations are collected (Section 1.8 explains it in full). We now number the three matrices with a raised index. On the letters $\Gamma$ and $\gamma$ a raised index is a label that numbers the matrices of a list, not a power: $\Gamma^2$ below is the third matrix of the list, not $\Gamma\cdot\Gamma$, and its square is written $(\Gamma^2)^2=Y^2=-I$. Likewise the two raised indices of $\hat\eta^{ab}$ and $\eta^{ab}$ are labels: $\hat\eta^{ab}$ is the entry in row $a$ and column $b$ of $\hat\eta$ (Section 1.11 explains why such entries are written with raised indices; for the diagonal matrices with entries $\pm1$ used here it makes no difference). A raised number on a matrix that carries no label keeps its usual meaning, a power, as in $X^2=I$ above. With the names $\Gamma^0=X$, $\Gamma^1=Z$, $\Gamma^2=Y$ and the diagonal matrix $\hat\eta=\mathrm{diag}(+1,+1,-1)$, all nine relations fit into one formula:

$$
\{\Gamma^a,\Gamma^b\}=2\hat\eta^{ab}I\qquad(a,b=0,1,2).
$$

Matrices obeying such a relation generate a **Clifford algebra**; Chapter 2 builds the eight $16\times16$ matrices $\gamma^0,\dots,\gamma^7$ with $\{\gamma^a,\gamma^b\}=2\eta^{ab}I_{16}$ for the $\eta$ of this book. Notice also that $X$ and $Z$, which square to $+I$, are symmetric, while $Y$, which squares to $-I$, is antisymmetric. Part of this is forced: a real symmetric matrix is Hermitian, so its eigenvalues are real (Section 1.6), while a matrix with square $-I$ has only the eigenvalues $\pm i$; since every square matrix has at least one complex eigenvalue (the fundamental theorem of algebra, used without proof), a real symmetric matrix can never square to $-I$. The square alone does not force the rest of the pattern: $\begin{pmatrix}1&-2\\ 1&-1\end{pmatrix}$ has square $-I$ and is not antisymmetric, and $\begin{pmatrix}1&1\\ 0&-1\end{pmatrix}$ has square $+I$ and is not symmetric (multiply out to check). The full pattern holds for the real matrices with $M^TM=I$, called **orthogonal** matrices. $X$, $Z$ and $Y$ are orthogonal: $X^TX=X^2=I$, $Z^TZ=Z^2=I$ and $Y^TY=(-Y)Y=-Y^2=I$. For an orthogonal $M$, $M^T=M^{-1}$; and $M^2=\pm I$ says that $M(\pm M)=I$, that is $M^{-1}=\pm M$. Together, $M^T=\pm M$: an orthogonal matrix with square $+I$ is symmetric, and one with square $-I$ is antisymmetric. The notebook's gamma matrices are of this kind: each is a signed permutation matrix (every row and every column contains exactly one nonzero entry, $+1$ or $-1$), hence orthogonal (Section 2.2 proves this), which is why they are symmetric for the space-like directions 0 to 3 and antisymmetric for the time-like directions 4 to 7 (Chapter 2, Section 2.8, facts (N2) and (N3)).

### 1.8 Indices and the summation convention

**Free and dummy indices.** In the formula $(Av)_i=\sum_jA_{ij}v_j$ the index $i$ is **free**: the formula holds for each value of $i$, and it appears once in every term. The index $j$ is a **dummy**: it is summed over, and it can be renamed, $\sum_jA_{ij}v_j=\sum_kA_{ik}v_k$, as long as the new name is not already in use in the term. In a correct equation every term has the same free indices. An index formula is a compact way of writing many equations at once; for example $\{\Gamma^a,\Gamma^b\}=2\hat\eta^{ab}I$ of Section 1.7 stands for nine matrix equations, one for each pair $(a,b)$.

**Upper and lower indices.** In Sections 1.2 to 1.7 the components of plain columns of numbers were written with lower indices, $v_k$. For the vectors of the eight-dimensional space two kinds of objects occur, and they are distinguished by the position of their index. The components of a displacement or a velocity carry an upper index, $v^\mu$; the coefficients of a metric, $g_{\mu\nu}$ (Section 1.11), and the derivatives $\partial_\mu$ (Section 1.9) carry lower indices. An upper index is not an exponent: $v^2$ means component 2 of $v$, and the square of that component is written $(v^2)^2$.

**The summation convention.** In a single term, an index that appears twice, once as an upper and once as a lower index, is summed over its whole range, without writing $\sum$:

$$
v^\mu w_\mu=\sum_{\mu=0}^{7}v^\mu w_\mu,\qquad g_{\mu\nu}v^\mu w^\nu=\sum_{\mu=0}^7\sum_{\nu=0}^7g_{\mu\nu}v^\mu w^\nu,\qquad \partial_\mu V^\mu=\sum_{\mu=0}^7\frac{\partial V^\mu}{\partial x^\mu}.
$$

This is the **Einstein summation convention**. In this book the indices $\mu,\nu,\rho,\sigma,\lambda$ of the coordinates (coordinate indices, also called curved indices; Chapter 4) and the indices $a,b,c$ that are raised and lowered with the flat metric $\eta$ of Section 1.11 (frame indices, Section 4.10) run over $0,\dots,7$. An index that appears twice in the same position (both lower or both upper) is not summed automatically; where such a sum is meant, as for matrix entries $A_{ij}$, the symbol $\sum$ is written.

**Coordinates and their names.** In the index formulas of this chapter and of Chapter 4 the coordinates are written $x^\mu$ with an upper index. Other chapters (Chapter 9, which follows the notebook closely, and the line elements of later chapters, such as $dx_1^2$ in Chapters 7, 11 and 13), the notebook and the project documents write the same coordinates as $x_0,x_1,\dots,x_7$, also inside formulas such as $\partial_\mu=\partial/\partial x_\mu$; this chapter does the same in words and in examples such as $e^{-i\varepsilon x_4}$. There the lower index is only part of the name, and $\partial/\partial x_\mu$ is the same derivative as $\partial/\partial x^\mu$. The two notations denote the same numbers: $x^4$ in a formula is the coordinate named $x_4$, the time. The index of a coordinate is never lowered with a metric in this book.

**The Kronecker delta.** With one upper and one lower index, $\delta^\mu{}_\nu$ is 1 for $\mu=\nu$ and 0 otherwise. Contracting with it renames an index:

$$
\delta^\mu{}_\nu v^\nu=v^\mu,\qquad \delta^\mu{}_\nu\delta^\nu{}_\rho=\delta^\mu{}_\rho,\qquad \delta^\mu{}_\mu=8 .
$$

Proof of the first: in $\sum_\nu\delta^\mu{}_\nu v^\nu$ only the term with $\nu=\mu$ is not zero, and it equals $v^\mu$. The last formula counts the eight values of $\mu$.

**Symmetric times antisymmetric gives zero.** If $S_{\mu\nu}=S_{\nu\mu}$ and $A^{\mu\nu}=-A^{\nu\mu}$, then

$$
S_{\mu\nu}A^{\mu\nu}=0 .
$$

Proof: renaming the two dummy indices ($\mu$ becomes $\nu$ and $\nu$ becomes $\mu$) does not change the value, so $S_{\mu\nu}A^{\mu\nu}=S_{\nu\mu}A^{\nu\mu}$; using the two symmetries, the right side equals $S_{\mu\nu}(-A^{\mu\nu})$. A number equal to its own negative is 0. Example with $2\times2$ arrays: for $S=\begin{pmatrix}1&2\\ 2&3\end{pmatrix}$ and $A=\begin{pmatrix}0&1\\ -1&0\end{pmatrix}$ the full double sum is $1\cdot0+2\cdot1+2\cdot(-1)+3\cdot0=0$.

**Consequence for quadratic expressions.** For a vector $v$ with ordinary (commuting) components and a square matrix $M$, the quadratic expression $v^TMv=\sum_j\sum_kv_jM_{jk}v_k$ contains the products $v_jv_k$, which are symmetric in $j$ and $k$. By the rule just proved, the antisymmetric part of $M$ drops out:

$$
v^TMv=v^TM_Sv,\qquad\text{in particular}\qquad v^TAv=0\ \text{for antisymmetric }A .
$$

Chapter 5 meets the opposite case: for anticommuting quantities $\theta_j\theta_k=-\theta_k\theta_j$ the products are antisymmetric, and then the symmetric part drops out, $\theta^TM\theta=\theta^TM_A\theta$. This one difference decides whether the notebook's Lagrangian is trivial (Stage-1 document, §6).

**Sums over ordered pairs.** If $A_{ab}$ and $B^{ab}$ are both antisymmetric, the product $A_{ab}B^{ab}$ (no sum) is symmetric under exchanging $a$ and $b$, and it vanishes for $a=b$. Hence the sum over all ordered pairs is twice the sum over the pairs with $a<b$:

$$
\tfrac12A_{ab}B^{ab}=\sum_{a<b}A_{ab}B^{ab}.
$$

This is why the spinor connection $\Omega_\mu$ of Chapter 4 can be written either as $\tfrac12\omega_{\mu ab}S^{ab}$ with the summation convention or as $\sum_{a<b}\omega_{\mu ab}S^{ab}$ without the factor $\tfrac12$ (there $\omega_{\mu ab}$, the spin connection, and $S^{ab}$ are both antisymmetric in $a$ and $b$).

**The Levi-Civita symbol.** For $n$ indices, each taking the values $0,\dots,n-1$, the symbol $\varepsilon_{j_0j_1\dots j_{n-1}}$ is the sign of the permutation $(j_0,\dots,j_{n-1})$ when the indices are all different, and 0 when two of them are equal. For three indices: $\varepsilon_{012}=\varepsilon_{120}=\varepsilon_{201}=+1$, $\varepsilon_{102}=\varepsilon_{021}=\varepsilon_{210}=-1$, and for example $\varepsilon_{011}=0$. With it the determinant formula of Section 1.4 reads $\det A=\sum_{j_0,j_1,j_2}\varepsilon_{j_0j_1j_2}A_{0j_0}A_{1j_1}A_{2j_2}$ for $n=3$ (and similarly for every $n$). The notebook uses a four-index symbol with the 1-based indices $1,\dots,4$ of Mathematica to build its gamma matrices (Chapter 3); this is one of the labelled exceptions to counting from 0.

### 1.9 Functions of several variables and partial derivatives

**Partial derivatives.** For a function $f(x^0,\dots,x^7)$ of eight variables, the **partial derivative** with respect to $x^\mu$ is the ordinary derivative with respect to $x^\mu$ while all the other variables are held fixed. It is written

$$
\partial_\mu f=\frac{\partial f}{\partial x^\mu}.
$$

Example: for $f(x^0,x^4)=(x^0)^2\sin x^4$,

$$
\partial_0f=2x^0\sin x^4,\qquad \partial_4f=(x^0)^2\cos x^4,\qquad \partial_4\partial_0f=2x^0\cos x^4=\partial_0\partial_4f .
$$

The last equality is an instance of a general theorem (Schwarz's theorem): for a function whose second partial derivatives are continuous, the order of two partial derivatives does not matter, $\partial_\mu\partial_\nu f=\partial_\nu\partial_\mu f$. We use it without proof. All functions in this book are **smooth**, that is, they have as many continuous derivatives as are needed, unless the text says otherwise.

**Product rule.** Because a partial derivative is a derivative in one variable, the rules of one-variable calculus hold for it; in particular $\partial_\mu(fg)=(\partial_\mu f)g+f\,\partial_\mu g$. For matrices whose entries are functions, derivatives are taken entry by entry, and the product rule keeps the order of the factors:

$$
\partial_\mu(AB)=(\partial_\mu A)B+A\,\partial_\mu B .
$$

Proof: entry $(i,k)$ of the left side is $\partial_\mu\sum_jA_{ij}B_{jk}=\sum_j\bigl((\partial_\mu A_{ij})B_{jk}+A_{ij}\partial_\mu B_{jk}\bigr)$, which is entry $(i,k)$ of the right side. Applying it to $AA^{-1}=I$, whose derivative is zero, gives $(\partial_\mu A)A^{-1}+A\,\partial_\mu(A^{-1})=0$, and multiplying from the left by $A^{-1}$:

$$
\partial_\mu(A^{-1})=-A^{-1}(\partial_\mu A)A^{-1}.
$$

For a $1\times1$ matrix this is the familiar $(1/a)'=-a'/a^2$.

**Chain rule.** Let $f(u,v)$ depend on two variables that in turn depend on $t$. Then

$$
\frac{d}{dt}f(u(t),v(t))=\frac{\partial f}{\partial u}\,\frac{du}{dt}+\frac{\partial f}{\partial v}\,\frac{dv}{dt}.
$$

Derivation. Write $\Delta u=u(t+\Delta t)-u(t)$, $\Delta v=v(t+\Delta t)-v(t)$ and split the change of $f$ into two steps, first in $u$ and then in $v$:

$$
f(u+\Delta u,v+\Delta v)-f(u,v)=\bigl[f(u+\Delta u,v+\Delta v)-f(u,v+\Delta v)\bigr]+\bigl[f(u,v+\Delta v)-f(u,v)\bigr].
$$

By the mean value theorem of one-variable calculus (for a differentiable function, $g(b)-g(a)=g'(c)(b-a)$ for some $c$ between $a$ and $b$; used without proof), the first bracket equals $\partial_uf(u+\theta_1\Delta u,v+\Delta v)\,\Delta u$ and the second $\partial_vf(u,v+\theta_2\Delta v)\,\Delta v$, with numbers $\theta_1,\theta_2$ between 0 and 1. Divide by $\Delta t$ and let $\Delta t\to0$: then $\Delta u/\Delta t\to du/dt$, $\Delta v/\Delta t\to dv/dt$, and, because the partial derivatives are continuous and $\Delta u,\Delta v\to0$, the two partial derivatives tend to their values at $(u,v)$. This gives the formula. With more variables the same argument gives one term per variable: $\frac{d}{dt}f(x(t))=\partial_\mu f\,\frac{dx^\mu}{dt}$ (summation convention).

**Change of variables.** If new coordinates are functions of old ones, the chain rule converts derivatives. The project uses, for the primordial field, $z=6Hx^0$ and $t=Hx^4$ with a constant $H>0$. A function of $z$ then depends on $x^0$ through $z$, and

$$
\partial_0=\frac{dz}{dx^0}\,\frac{\partial}{\partial z}=6H\,\partial_z,\qquad \partial_4=\frac{dt}{dx^4}\,\frac{\partial}{\partial t}=H\,\partial_t .
$$

For example $\partial_0\cot z=6H\,\partial_z\cot z=-6H/\sin^2z$.

**Linear approximation.** For a small displacement $h$, a smooth function changes by

$$
f(x+h)=f(x)+\partial_\mu f(x)\,h^\mu+(\text{terms of second and higher order in }h).
$$

The linear term is the chain rule applied to the function $t\mapsto f(x+th)$ at $t=0$, whose derivative there is $\partial_\mu f(x)\,h^\mu$; that the remainder is of second order in $h$ for a smooth $f$ is Taylor's theorem, used without proof. "First order" in this book means: keep the term linear in the small quantity and drop the rest.

**The derivative of a determinant.** For an invertible matrix $g$ whose entries depend on $x$,

$$
\partial_\mu\det g=\det g\;\mathrm{tr}\bigl(g^{-1}\partial_\mu g\bigr).
$$

This is **Jacobi's formula**. We prove it in the two cases that the book needs most and use it without proof otherwise. For a diagonal matrix $g=\mathrm{diag}(g_0,\dots,g_{n-1})$, $\det g=g_0\cdots g_{n-1}$ and the product rule give $\partial_\mu\det g=\sum_k g_0\cdots(\partial_\mu g_k)\cdots g_{n-1}=\det g\sum_k\partial_\mu g_k/g_k$, and $\sum_k\partial_\mu g_k/g_k$ is the trace of $g^{-1}\partial_\mu g=\mathrm{diag}(\partial_\mu g_k/g_k)$. For a $2\times2$ matrix with entries $a,b,c,d$, $\partial(ad-bc)=d\,\partial a+a\,\partial d-c\,\partial b-b\,\partial c$, while

$$
\det g\;\mathrm{tr}(g^{-1}\partial g)=\mathrm{tr}\left[\begin{pmatrix}d&-b\\ -c&a\end{pmatrix}\begin{pmatrix}\partial a&\partial b\\ \partial c&\partial d\end{pmatrix}\right]=d\,\partial a-b\,\partial c-c\,\partial b+a\,\partial d ,
$$

the same expression.

**The derivative of the volume factor.** The determinant $\det g$ is a sum of products of entries of $g$ (Section 1.4), so it is continuous when the entries are. Near a point where $\det g\ne0$ it therefore has a fixed sign, because a continuous function that is not zero at a point keeps its sign near that point (a standard fact, used without proof). Write $\det g=\epsilon\,|\det g|$ with this fixed sign $\epsilon=\pm1$; then also $|\det g|=\epsilon\det g$, since $\epsilon^2=1$, and $\partial_\mu|\det g|=\epsilon\,\partial_\mu\det g$, since $\epsilon$ is constant near the point. By the chain rule for $\sqrt u$, whose derivative is $1/(2\sqrt u)$, and by Jacobi's formula,

$$
\begin{aligned}
\partial_\mu\sqrt{|\det g|}&=\frac{\partial_\mu|\det g|}{2\sqrt{|\det g|}}=\frac{\epsilon\,\partial_\mu\det g}{2\sqrt{|\det g|}}\\
&=\frac{\epsilon\det g\;\mathrm{tr}\bigl(g^{-1}\partial_\mu g\bigr)}{2\sqrt{|\det g|}}=\frac{|\det g|\;\mathrm{tr}\bigl(g^{-1}\partial_\mu g\bigr)}{2\sqrt{|\det g|}},
\end{aligned}
$$

and $|\det g|/\sqrt{|\det g|}=\sqrt{|\det g|}$ gives

$$
\partial_\mu\sqrt{|\det g|}=\tfrac12\sqrt{|\det g|}\;\mathrm{tr}\bigl(g^{-1}\partial_\mu g\bigr).
$$

This formula is used in Chapter 4 to relate the volume factor to the Christoffel symbols.

### 1.10 Integrals in several variables, integration by parts and the delta function

**One variable.** The definite integral $\int_a^bf(x)\,dx$ and the fundamental theorem of calculus, $\int_a^bF'(x)\,dx=F(b)-F(a)$, are school mathematics and are used without proof.

**Integration by parts.** Integrating the product rule $(fg)'=f'g+fg'$ from $a$ to $b$ gives $f(b)g(b)-f(a)g(a)=\int_a^bf'g\,dx+\int_a^bfg'\,dx$, that is

$$
\int_a^bf\,g'\,dx=\bigl[fg\bigr]_a^b-\int_a^bf'\,g\,dx,\qquad \bigl[fg\bigr]_a^b=f(b)g(b)-f(a)g(a).
$$

Example: with $f=x$ and $g'=e^x$ (so $g=e^x$), $\int_0^1xe^x\,dx=\bigl[xe^x\bigr]_0^1-\int_0^1e^x\,dx=e-(e-1)=1$. When the product $fg$ vanishes at both ends, the boundary term drops out, and the derivative moves from one factor to the other at the price of a minus sign. This is the key step in the derivation of the Euler–Lagrange equations (Chapter 5).

**Several variables.** An integral over a box $a_\mu\le x^\mu\le b_\mu$ is computed as an iterated integral, one variable after the other. For a continuous function on a box the order of the variables does not matter (Fubini's theorem, used without proof). The volume element of the eight coordinates is written $d^8x=dx^0dx^1\cdots dx^7$.

**Integrals of derivatives vanish when the boundary values vanish.** Let $V^\mu(x)$, $\mu=0,\dots,n-1$, be smooth functions on a box. Then

$$
\int_{\mathrm{box}}\partial_\mu V^\mu\,d^nx=\sum_{\mu}\int\Bigl[V^\mu\Bigr]_{x^\mu=a_\mu}^{x^\mu=b_\mu}\,\prod_{\nu\ne\mu}dx^\nu ,
$$

and in particular the integral is zero if every $V^\mu$ vanishes on the boundary of the box. Proof: the left side is a sum of $n$ integrals, one for each $\mu$. In the integral of $\partial_\mu V^\mu$ (no sum), do the integral over $x^\mu$ first, with the other variables fixed; by the fundamental theorem it equals the difference of the values of $V^\mu$ at $x^\mu=b_\mu$ and $x^\mu=a_\mu$. This is the simplest form of the divergence theorem (Gauss's theorem). It is the reason why adding a total derivative $\partial_\mu V^\mu$ to a Lagrangian does not change the field equations (Chapter 5). Example on the unit square: for $V^0=\sin(\pi x^0)\,x^1$ and $V^1=0$, $\int_0^1\!\int_0^1\partial_0V^0\,dx^0dx^1=\int_0^1x^1\,[\sin\pi-\sin0]\,dx^1=0$.

**The delta function.** In Chapter 8 the equal-time anticommutators contain the symbol $\delta(x-y)$, Dirac's delta function. It is not an ordinary function but a rule for integrals: for every continuous $f$,

$$
\int f(x)\,\delta(x-y)\,dx=f(y).
$$

One can picture it as the limit of ever narrower and taller rectangles of area 1. Let $r_\epsilon(u)=1/\epsilon$ for $|u|<\epsilon/2$ and $0$ otherwise. Then $\int f(x)\,r_\epsilon(x-y)\,dx=\frac1\epsilon\int_{y-\epsilon/2}^{y+\epsilon/2}f(x)\,dx$ is the average of $f$ over an interval of length $\epsilon$ around $y$. A continuous function takes its average value somewhere in the interval (the mean value theorem for integrals, used without proof), so the average tends to $f(y)$ as $\epsilon\to0$. In several variables the delta function is the product of one-dimensional ones; for example $\delta^7(x-y)$ in Chapter 8 is the product of seven deltas, one for each coordinate other than the time $x^4$.

### 1.11 Metrics and signatures

**The dot product.** In ordinary 3-space the dot product of two vectors is $u\cdot v=u_0v_0+u_1v_1+u_2v_2=u^TIv$, and the length of $v$ is $\sqrt{v\cdot v}$. A **metric** generalizes it: a symmetric, invertible $n\times n$ matrix $g$ defines the scalar product

$$
g(u,v)=u^Tg\,v=g_{\mu\nu}u^\mu v^\nu ,
$$

which is symmetric in $u$ and $v$ because $g$ is symmetric. The number $g(v,v)$ is the squared length of $v$. For $g=I$ it is the dot product. But a metric may have negative diagonal entries, and then $g(v,v)$ can be negative or zero for a vector $v\ne0$.

**Space-like, time-like and null.** In the convention of this book a vector is **space-like** if $g(v,v)>0$, **time-like** if $g(v,v)<0$, and **null** (or light-like) if $g(v,v)=0$ and $v\ne0$. The special relativity of the observed world has one time-like and three space-like directions; with time first and this sign convention its metric is $\mathrm{diag}(-1,+1,+1,+1)$. Many books of particle physics, and the scalar-field reference of the project, use the opposite overall sign, $\mathrm{diag}(+1,-1,-1,-1)$; the two conventions describe the same geometry, since one metric is the negative of the other (the Stage-1 document, §2.3, compares them for a scalar field). The flat metric of this book is

$$
\begin{aligned}
&\eta=\mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1),\\
&\eta(v,v)=(v^0)^2+(v^1)^2+(v^2)^2+(v^3)^2-(v^4)^2-(v^5)^2-(v^6)^2-(v^7)^2 .
\end{aligned}
$$

The basis vector $e_0$ is space-like ($\eta(e_0,e_0)=\eta_{00}=+1$), $e_4$ is time-like ($\eta_{44}=-1$), and $e_0+e_4$ is null: $\eta(e_0+e_4,e_0+e_4)=1-1=0$.

**Signature.** The **signature** of a metric is the pair $(p,q)$ of the numbers of its positive and its negative eigenvalues. (A metric is real and symmetric, so its eigenvalues are real, and it is invertible, so none is zero.) For a diagonal metric the eigenvalues are the diagonal entries, so $\eta$ has signature (4,4). If the basis is changed, so that $g$ becomes $g'=\Lambda^Tg\Lambda$ with an invertible matrix $\Lambda$ whose columns are the new basis vectors, the eigenvalues change but their signs do not: $g'$ has the same signature. This is **Sylvester's law of inertia**, used without proof. The signature is therefore a property of the geometry, not of the basis.

**Example.** $g=\begin{pmatrix}1&2\\ 2&1\end{pmatrix}$ has $p(x)=(x-1)^2-4=(x-3)(x+1)$, eigenvalues 3 and $-1$, signature (1,1). In the basis $u=(1,1)^T$, $w=(1,-1)^T$ one finds $g(u,u)=1+2+2+1=6$, $g(w,w)=1-2-2+1=-2$ and $g(u,w)=(1,1)\,(1-2,\,2-1)^T=0$, so in this basis the metric is $\mathrm{diag}(6,-2)$: again one positive and one negative entry, as Sylvester's law says.

**Inverse metric, raising and lowering.** The inverse matrix of $g_{\mu\nu}$ is written with upper indices, $g^{\mu\nu}$, and satisfies $g^{\mu\nu}g_{\nu\rho}=\delta^\mu{}_\rho$. For $\eta$, whose diagonal entries are $\pm1$, $\eta^2=I$, so the inverse has the same entries: $\eta^{ab}=\eta_{ab}$. A metric **lowers** an index and its inverse **raises** it:

$$
v_\mu=g_{\mu\nu}v^\nu,\qquad v^\mu=g^{\mu\nu}v_\nu,\qquad g(u,v)=u^\mu v_\mu .
$$

With $\eta$, lowering keeps the components 0 to 3 and changes the sign of the components 4 to 7: $v_0=v^0$, and $v_4=\eta_{44}v^4=-v^4$.

**Curved metrics and the line element.** In curved space (Chapter 4) the metric depends on the point, $g_{\mu\nu}(x)$, and it measures small displacements $dx^\mu$ at $x$. The **line element**

$$
ds^2=g_{\mu\nu}(x)\,dx^\mu dx^\nu
$$

is the squared length of the displacement from $x$ to $x+dx$. The same geometry can be described in different coordinates. Example: the flat plane in polar coordinates, $x=r\cos\theta$ and $y=r\sin\theta$. The chain rule gives $dx=\cos\theta\,dr-r\sin\theta\,d\theta$ and $dy=\sin\theta\,dr+r\cos\theta\,d\theta$, hence

$$
\begin{aligned}
ds^2=dx^2+dy^2&=(\cos^2\theta+\sin^2\theta)\,dr^2+2(-r\cos\theta\sin\theta+r\sin\theta\cos\theta)\,dr\,d\theta\\
&\quad+r^2(\sin^2\theta+\cos^2\theta)\,d\theta^2\\
&=dr^2+r^2d\theta^2 .
\end{aligned}
$$

In the coordinates $(r,\theta)$ the metric is $\mathrm{diag}(1,r^2)$. In general, if the old coordinates $x^\mu$ are functions of new ones $x'^\alpha$, then $dx^\mu=\frac{\partial x^\mu}{\partial x'^\alpha}dx'^\alpha$, and inserting this into the line element gives the **transformation law of the metric**

$$
g'_{\alpha\beta}=\frac{\partial x^\mu}{\partial x'^\alpha}\,\frac{\partial x^\nu}{\partial x'^\beta}\,g_{\mu\nu},\qquad\text{in matrix form}\qquad g'=J^TgJ,\quad J^\mu{}_\alpha=\frac{\partial x^\mu}{\partial x'^\alpha}.
$$

**The volume element.** From $g'=J^TgJ$ and the product rule for determinants, $\det g'=(\det J)^2\det g$, so $\sqrt{|\det g'|}=|\det J|\sqrt{|\det g|}$. The change-of-variables formula for multiple integrals (used without proof) says that $d^nx=|\det J|\,d^nx'$. Together these show that $\sqrt{|\det g|}\,d^nx$ has the same value in every coordinate system: it is the **volume element** of the geometry, and it multiplies every Lagrangian of this book. The book writes $\sqrt{|g|}$ for $\sqrt{|\det g|}$. For polar coordinates $\sqrt{|g|}=r$, and the area of the disc of radius $R$ is $\int_0^R\int_0^{2\pi}r\,d\theta\,dr=2\pi\cdot\tfrac12R^2=\pi R^2$, as it must be.

**Worked example: the metric of the primordial field.** In Chapter 9 the notebook's metric is, in the coordinates $x^0,\dots,x^7$, with $z=6Hx^0\in(0,\pi/2)$, $s=\sin z$ and a real function $a_4$ of the time,

$$
g=\mathrm{diag}\bigl(\cot^2z,\ s^{1/3}e^{2a_4},\ s^{1/3}e^{2a_4},\ s^{1/3}e^{2a_4},\ -1,\ -s^{1/3}e^{-2a_4},\ -s^{1/3}e^{-2a_4},\ -s^{1/3}e^{-2a_4}\bigr).
$$

For $0<z<\pi/2$ the first four entries are positive and the last four negative, so the signature is (4,4). The determinant is the product of the diagonal (Section 1.4):

$$
\begin{aligned}
\det g&=\cot^2z\cdot\bigl(s^{1/3}e^{2a_4}\bigr)^3\cdot(-1)\cdot\bigl(-s^{1/3}e^{-2a_4}\bigr)^3\\
&=\cot^2z\cdot s\,e^{6a_4}\cdot(-1)\cdot(-1)\,s\,e^{-6a_4}=\cot^2z\,\sin^2z=\cos^2z ,
\end{aligned}
$$

using $(-x)^3=-x^3$, $(s^{1/3})^3=s$ and $e^{6a_4}e^{-6a_4}=1$. The sign is $+$ because there are four negative entries, an even number. Hence $\sqrt{|g|}=\cos z$, which does not depend on the time. The exact Stage-2 verifier confirms $\det g=+\cos^2z$ (check `P_metric_detG_equals_plus_cos2z` in `artifacts/dirac16complex/primordial-field/wolfram-primordial-report.json`); the Stage-2 specification had first written $-\cos^2z$, and the sign was corrected when it was computed. Jacobi's formula of Section 1.9 gives a check of the derivative. The diagonal entries contribute to $\mathrm{tr}(g^{-1}\partial_zg)=\sum_\mu\partial_z\ln|g_{\mu\mu}|$ the terms $\partial_z\ln\cot^2z=-2/(\sin z\cos z)$, three times $\partial_z\ln s^{1/3}=\tfrac13\cot z$ from 3-space, zero from the entry $-1$, and three times $\tfrac13\cot z$ from the extra times, in total

$$
\mathrm{tr}(g^{-1}\partial_zg)=-\frac2{\sin z\cos z}+2\,\frac{\cos z}{\sin z}=\frac{-2+2\cos^2z}{\sin z\cos z}=-2\tan z,
$$

so $\partial_z\sqrt{|g|}=\tfrac12\cos z\,(-2\tan z)=-\sin z$, which is indeed the derivative of $\cos z$.

### 1.12 The (4,4) world of this book

The space of this book has eight coordinates, four space-like and four time-like:

| coordinate | role | $\eta$ entry |
| --- | --- | --- |
| $x_0$ | hidden space direction | $+1$ |
| $x_1,x_2,x_3$ | ordinary 3-space | $+1$ |
| $x_4$ | the time in which everything evolves | $-1$ |
| $x_5,x_6,x_7$ | the three extra times | $-1$ |

The roles are those of the notebook. Choosing $x_4$ as the time means: initial data are given at one value of $x_4$, and the field equations determine the field at later values of $x_4$ (Chapters 8 and 10).

The observed world has one time and three space directions, signature (3,1) in the sign convention of this book. The signature (4,4) is therefore not the signature of observed spacetime; it is the setting of the model, chosen by the notebook, and the book treats it as an assumption (ledger row L43 of Chapter 0). Two consequences are visible already. First, the Clifford algebra of an eight-dimensional space with this metric is the algebra of all real $16\times16$ matrices (Chapter 2), which is why the field has sixteen components. Second, three extra time-like directions change the relation between frequency and wave number: Chapter 8 derives that in flat space a wave of mass $m$ with momenta $k_0,\dots,k_3$ along the space-like directions and $k_5,k_6,k_7$ along the extra times has the squared frequency $E^2=m^2+k_0^2+k_1^2+k_2^2+k_3^2-k_5^2-k_6^2-k_7^2$, which becomes negative for large extra-time momenta. By Section 1.5 a negative $E^2$ means an imaginary frequency and a wave that grows exponentially in time; this instability is why the physics of the book is restricted to the sector without extra-time momenta.

### 1.13 What we proved and what we assumed

We **proved**, from the definitions: the uniqueness of the expansion coefficients in a basis; the rules for sums, products, transposes and inverses of matrices, including $(AB)^T=B^TA^T$, $\mathrm{tr}(AB)=\mathrm{tr}(BA)$ and $(AB)^{-1}=B^{-1}A^{-1}$; the unique split of a square matrix into symmetric and antisymmetric parts; the block product and the mixed-product rule of tensor products; the product rule of $2\times2$ determinants and the determinant of a diagonal matrix; the arithmetic of complex numbers, the product rule for complex-valued functions of a real variable, the law of exponents for $e^{i\theta}$ and its derivative; the four facts about Hermitian and anti-Hermitian matrices of Section 1.5; that Hermitian matrices have real eigenvalues and orthogonal eigenvectors for different eigenvalues; that $A^2=\pm I$ forces the eigenvalues $\pm1$ or $\pm i$ and gives the projectors $\tfrac12(I\pm A)$; the Clifford relations of the three $2\times2$ matrices $X$, $Z$, $Y$; that a real symmetric matrix cannot square to $-I$, and that an orthogonal matrix with square $+I$ is symmetric and one with square $-I$ antisymmetric; that a symmetric array contracted with an antisymmetric one gives zero, and its consequence for quadratic expressions; the product rule for matrix derivatives and the derivative of the inverse; the chain rule (from the mean value theorem); Jacobi's formula for diagonal and for $2\times2$ matrices, and from it the derivative of $\sqrt{|\det g|}$; integration by parts; the vanishing of integrals of derivatives with vanishing boundary values on a box; the polar-coordinate metric and the transformation law of the metric; the invariance of the volume element (from the change-of-variables formula); and $\det g=+\cos^2z$, $\sqrt{|g|}=\cos z$ and signature (4,4) for the metric of the primordial field.

We **assumed** (standard mathematics used without proof): the rules for powers, the addition theorems of trigonometry, and that every point at distance 1 from the origin of the plane is $(\cos\theta,\sin\theta)$ for some angle $\theta$; that all bases of $\mathbb R^n$ have $n$ vectors; the area formula $|ad-bc|$ for a parallelogram (not used later); for general $n$, that $\det(AB)=\det A\det B$, that $\det A^T=\det A$, that $A$ is invertible exactly when $\det A\ne0$, that a square matrix $M$ is invertible exactly when $Mv=0$ forces $v=0$ (only the direction from "forces $v=0$" to "invertible" is assumed), and that exchanging two entries of a permutation changes its sign; that the trace and the determinant are the sum and the product of all eigenvalues; the fundamental theorem of algebra; that multiplicities of eigenvalues of Hermitian matrices count independent eigenvectors, and the spectral theorem; Schwarz's theorem on mixed partial derivatives; that a continuous function which is not zero at a point keeps its sign near that point; the mean value theorems of differential and integral calculus; Taylor's theorem; Jacobi's formula for general matrices; the fundamental theorem of calculus; Fubini's theorem; the change-of-variables formula for multiple integrals; and Sylvester's law of inertia. We also used the **conventions** of the book (ASSUMED choices): counting from 0, the summation convention for one upper and one lower index, the metric $\eta=\mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1)$, and the sign convention in which space-like vectors have positive squared length.

### 1.14 Exercises

Exercise 1.1. (a) How many entries does the list $(\Psi_0,\dots,\Psi_{15})$ have, and what is the label of its tenth entry? (b) Compute $\sum_{k=0}^{4}(2k+1)$. (c) Compute $\sum_{a=0}^{7}\eta_{aa}$ and $\prod_{a=0}^{7}\eta_{aa}$.

Exercise 1.2. Are the vectors $u_0=(1,2,0)^T$, $u_1=(0,1,1)^T$ and $u_2=(1,3,1)^T$ linearly independent? If not, give a linear combination with coefficients not all zero that vanishes, and relate your answer to the determinant example of Section 1.4.

Exercise 1.3. (A substitution rule of the notebook.) Let $0<z<\pi/2$ and let $a$ be real. (a) Simplify $1/\sqrt{\sin^{1/3}z/e^{2a}}$. (b) Cell 1058 of the notebook replaces this expression by $1/(e^{a}\sin^{1/6}z)$. Compute the ratio of the correct value to the notebook's value. For which $a$ do they agree?

Exercise 1.4. For $A=\begin{pmatrix}1&2\\ 0&1\end{pmatrix}$ and $B=\begin{pmatrix}0&1\\ 1&0\end{pmatrix}$ compute $AB$, $BA$, $[A,B]$, $\{A,B\}$, $\mathrm{tr}(AB)$, $\mathrm{tr}(BA)$, $\det A$, $\det B$ and $\det(AB)$.

Exercise 1.5. Let $X$ and $Y$ be $n\times n$ matrices and $M=\begin{pmatrix}0&X\\ Y&0\end{pmatrix}$. (a) Show that $M^T=\begin{pmatrix}0&Y^T\\ X^T&0\end{pmatrix}$, so that $M$ is symmetric exactly when $Y=X^T$ and antisymmetric exactly when $Y=-X^T$. (b) For $n=1$, $X=1$, $Y=-1$ write down $M$ and $M^2$. (c) For $n=2$ and $X=Y=\begin{pmatrix}0&1\\ 1&0\end{pmatrix}$ compute $M^2$.

Exercise 1.6. (a) Compute $(2+i)(1-3i)$. (b) Write $1/(3+4i)$ in the form $a+ib$. (c) Compute $|3+4i|$. (d) Show that $(e^{i\theta})^\ast=e^{-i\theta}$ and $e^{i\pi}=-1$. (e) Show that $|e^{-i\varepsilon t}|=1$ for real $\varepsilon$ and $t$, and compute $|e^{-i\varepsilon t}|$ for $\varepsilon=i\gamma$ with real $\gamma$.

Exercise 1.7. Let $A=\begin{pmatrix}2&1-i\\ 1+i&3\end{pmatrix}$. (a) Show that $A$ is Hermitian. (b) Compute its characteristic polynomial and eigenvalues. (c) Find an eigenvector for each eigenvalue and check that the two are orthogonal.

Exercise 1.8. Show that $Y=\begin{pmatrix}0&-1\\ 1&0\end{pmatrix}$ has the eigenvalues $\pm i$, find the eigenvectors, and show that they are orthogonal ($w^\dagger v=0$), although $Y$ is not Hermitian. Explain why with fact 2 of Section 1.5.

Exercise 1.9. (a) For $Z=\mathrm{diag}(1,-1)$ compute $P_\pm=\tfrac12(I\pm Z)$ and verify $P_\pm^2=P_\pm$, $P_+P_-=0$ and $P_++P_-=I$. (b) The chirality matrix of Chapter 2 is the $16\times16$ matrix $\gamma^8=\mathrm{diag}(-I_8,I_8)$. Compute $P_-=\tfrac12(I_{16}-\gamma^8)$ and $P_+=\tfrac12(I_{16}+\gamma^8)$, and say which components of $\Psi=(\Psi_0,\dots,\Psi_{15})^T$ each of them keeps.

Exercise 1.10. (a) Write $\delta^\mu{}_\nu\delta^\nu{}_\rho$ for $\mu=\rho=4$ as an explicit sum and evaluate it. (b) Give $\varepsilon_{210}$, $\varepsilon_{120}$ and $\varepsilon_{112}$. (c) Compute the determinant of the matrix with rows $(2,1,0)$, $(0,1,3)$, $(1,0,1)$ with the formula of Section 1.4. (d) Check $\sum_a\sum_bS_{ab}A_{ab}=0$ for $S=\begin{pmatrix}1&4\\ 4&0\end{pmatrix}$ and $A=\begin{pmatrix}0&-3\\ 3&0\end{pmatrix}$.

Exercise 1.11. For $f(x^0,x^4)=e^{2x^4}\sin x^0$ compute $\partial_0f$, $\partial_4f$, $\partial_0\partial_4f$, $\partial_4\partial_0f$ and $\partial_0\partial_0f$.

Exercise 1.12. (a) With $z=6Hx^0$, compute $\partial_0(\sin^{1/3}z)$. (b) For $f(u,v)=uv^2$ with $u=\cos t$ and $v=\sin t$, compute $df/dt$ with the chain rule and, as a check, directly from $f(t)=\cos t\sin^2t$.

Exercise 1.13. Compute $\int_0^\pi x\sin x\,dx$ by integration by parts.

Exercise 1.14. Let $g=\begin{pmatrix}0&1\\ 1&0\end{pmatrix}$ be a metric on $\mathbb R^2$. (a) What is its signature? (b) Show that $e_0$ and $e_1$ are null. (c) Find a space-like and a time-like vector. (d) Lower the index of $v=(v^0,v^1)$.

Exercise 1.15. With the metric $\eta$ of this book: (a) for $v$ with components $(1,0,0,0,1,0,0,0)$ compute $\eta(v,v)$ and the lowered components $v_\mu$; (b) for $w=(0,0,0,0,1,1,0,0)$ compute $\eta(w,w)$; (c) for $u=(1,1,1,1,1,1,0,0)$ compute $\eta(u,u)$. Classify each vector as space-like, time-like or null.

Exercise 1.16. (The warped coordinate of the primordial field.) With $z=6Hx^0\in(0,\pi/2)$ define $\zeta=\ln(\sin z)/(6H)$. (a) Show that $d\zeta/dx^0=\cot z$, so that the first term of the line element, $\cot^2z\,(dx^0)^2$, equals $d\zeta^2$. (b) Show that $\sin^{1/3}z=e^{2H\zeta}$. (c) Which values does $\zeta$ take?

Exercise 1.17. Let $g(x)=\begin{pmatrix}1&x\\ x&-1\end{pmatrix}$. (a) Compute $\det g$ and its derivative with respect to $x$. (b) Compute $g^{-1}$ and $\mathrm{tr}(g^{-1}\,dg/dx)$, and check Jacobi's formula. (c) What is the signature of $g$, for every $x$?

### 1.15 Answers to the exercises

Answer 1.1. (a) Sixteen entries, labelled 0 to 15; the tenth entry has the label 9, so it is $\Psi_9$. (b) $1+3+5+7+9=25$. (c) The diagonal is $(+1,+1,+1,+1,-1,-1,-1,-1)$, so the sum is $4-4=0$ and the product is $(+1)^4(-1)^4=+1$.

Answer 1.2. They are dependent: $u_0+u_1=(1,3,1)^T=u_2$, so $u_0+u_1-u_2=0$. These are the rows of the $3\times3$ example of Section 1.4, whose determinant is 0. The two facts agree: since $\det A^T=\det A=0$, the equation $A^Tc=0$ has a solution $c\ne0$ (Section 1.4), and the components of such a $c$ are the coefficients of a vanishing combination of the rows of $A$; here $c=(1,1,-1)^T$.

Answer 1.3. (a) By the power rules of Section 1.1, $1/\sqrt{\sin^{1/3}z/e^{2a}}=(\sin^{1/3}z)^{-1/2}(e^{2a})^{1/2}=e^{a}/\sin^{1/6}z$. (b) The ratio is $\dfrac{e^a/\sin^{1/6}z}{1/(e^a\sin^{1/6}z)}=e^{2a}$. The two agree only for $a=0$. For $a\ne0$ the notebook's rule is wrong, which is row L18 of the ledger; Chapter 9 follows its consequences for the notebook's equations.

Answer 1.4. $AB=\begin{pmatrix}2&1\\ 1&0\end{pmatrix}$ and $BA=\begin{pmatrix}0&1\\ 1&2\end{pmatrix}$ (Section 1.3), so $[A,B]=\begin{pmatrix}2&0\\ 0&-2\end{pmatrix}$ and $\{A,B\}=\begin{pmatrix}2&2\\ 2&2\end{pmatrix}$. Both traces are 2. $\det A=1\cdot1-2\cdot0=1$, $\det B=0-1=-1$, and $\det(AB)=2\cdot0-1\cdot1=-1=\det A\det B$.

Answer 1.5. (a) Transposing a block matrix transposes the arrangement of the blocks and each block: block $(i,j)$ of $M^T$ is the transpose of block $(j,i)$ of $M$. This gives $M^T=\begin{pmatrix}0&Y^T\\ X^T&0\end{pmatrix}$. Comparing with $M$ and $-M$ block by block: $M^T=M$ exactly when $Y^T=X$ (equivalently $Y=X^T$), and $M^T=-M$ exactly when $Y=-X^T$. (b) $M=\begin{pmatrix}0&1\\ -1&0\end{pmatrix}$ and $M^2=\mathrm{diag}(XY,YX)=\mathrm{diag}(-1,-1)=-I$; $M$ is antisymmetric (it is $-Y$ in the notation of Section 1.7). (c) $XY=YX=X^2=I_2$, so $M^2=I_4$.

Answer 1.6. (a) $(2+i)(1-3i)=2-6i+i-3i^2=5-5i$. (b) $\dfrac1{3+4i}=\dfrac{3-4i}{(3+4i)(3-4i)}=\dfrac{3-4i}{25}=\dfrac3{25}-\dfrac4{25}i$. (c) $\sqrt{9+16}=5$. (d) $(e^{i\theta})^\ast=\cos\theta-i\sin\theta=\cos(-\theta)+i\sin(-\theta)=e^{-i\theta}$, since $\cos$ is even and $\sin$ is odd; $e^{i\pi}=\cos\pi+i\sin\pi=-1$. (e) For real $\varepsilon t$ the modulus of $e^{-i\varepsilon t}$ is 1 by Section 1.5. For $\varepsilon=i\gamma$, $e^{-i\varepsilon t}=e^{-i\cdot i\gamma t}=e^{\gamma t}$, whose modulus $e^{\gamma t}$ grows without bound for $\gamma>0$.

Answer 1.7. (a) $A^T=\begin{pmatrix}2&1+i\\ 1-i&3\end{pmatrix}$, and conjugating every entry gives $A$ back, so $A^\dagger=A$. (b) $p(x)=(x-2)(x-3)-(1-i)(1+i)=x^2-5x+6-2=x^2-5x+4=(x-1)(x-4)$, so the eigenvalues are 1 and 4, both real as Section 1.6 requires. (c) For 4: $(A-4I)v=0$ gives $-2v_0+(1-i)v_1=0$; with $v_1=2$ we get $v=(1-i,\,2)^T$ (check the second row: $(1+i)(1-i)-2=0$). For 1: $(A-I)w=0$ gives $w_0+(1-i)w_1=0$; with $w_1=1$ we get $w=(-1+i,\,1)^T$ (second row: $(1+i)(-1+i)+2=-2+2=0$). Then $w^\dagger v=(-1-i)(1-i)+1\cdot2=(-1+i-i+i^2)+2=0$.

Answer 1.8. $p(x)=x^2+1$, roots $\pm i$. For $+i$: $Yv=iv$ reads $(-v_1,v_0)=(iv_0,iv_1)$, so $v_1=-iv_0$ and $v=(1,-i)^T$. For $-i$: $w=(1,i)^T$. Then $w^\dagger v=1\cdot1+(i)^\ast(-i)=1+(-i)(-i)=1+i^2=0$. The reason: $Y$ is real and antisymmetric, hence anti-Hermitian (fact 1), so $iY$ is Hermitian (fact 2); $iY$ has the same eigenvectors with the real eigenvalues $i\cdot(\pm i)=\mp1$, and eigenvectors of a Hermitian matrix with different eigenvalues are orthogonal (Section 1.6).

Answer 1.9. (a) $P_+=\mathrm{diag}(1,0)$ and $P_-=\mathrm{diag}(0,1)$. Then $P_\pm^2=P_\pm$ (the entries 0 and 1 are their own squares), $P_+P_-=\mathrm{diag}(0,0)=0$ and $P_++P_-=I$. (b) $P_-=\tfrac12\mathrm{diag}(I_8+I_8,\,I_8-I_8)=\mathrm{diag}(I_8,0)$ keeps $\Psi_0,\dots,\Psi_7$ and removes $\Psi_8,\dots,\Psi_{15}$; $P_+=\mathrm{diag}(0,I_8)$ keeps $\Psi_8,\dots,\Psi_{15}$. So $\Psi_0,\dots,\Psi_7$ are the components with $\gamma^8=-1$ (chirality $-1$) and $\Psi_8,\dots,\Psi_{15}$ those with chirality $+1$, as in Stage 1 (Stage-1 document, Result 3.6).

Answer 1.10. (a) $\sum_{\nu=0}^7\delta^4{}_\nu\delta^\nu{}_4$; only $\nu=4$ contributes, giving $\delta^4{}_4\delta^4{}_4=1=\delta^4{}_4$. (b) $\varepsilon_{210}=-1$ (three inversions), $\varepsilon_{120}=+1$ (two inversions), $\varepsilon_{112}=0$ (a repeated index). (c) With the six terms of Section 1.4: $A_{00}A_{11}A_{22}=2\cdot1\cdot1=2$, $A_{01}A_{12}A_{20}=1\cdot3\cdot1=3$, and the other four terms each contain a zero entry, so $\det A=5$. (d) $1\cdot0+4\cdot(-3)+4\cdot3+0\cdot0=0$.

Answer 1.11. $\partial_0f=e^{2x^4}\cos x^0$, $\partial_4f=2e^{2x^4}\sin x^0$, $\partial_0\partial_4f=\partial_4\partial_0f=2e^{2x^4}\cos x^0$ (as Schwarz's theorem says), and $\partial_0\partial_0f=-e^{2x^4}\sin x^0$.

Answer 1.12. (a) $\partial_0(\sin^{1/3}z)=6H\cdot\tfrac13\sin^{-2/3}z\,\cos z=2H\cos z\,\sin^{-2/3}z$. (b) Chain rule: $\partial_uf\,u'+\partial_vf\,v'=v^2(-\sin t)+2uv\cos t=-\sin^3t+2\sin t\cos^2t$. Directly: $\frac d{dt}(\cos t\sin^2t)=-\sin t\sin^2t+\cos t\cdot2\sin t\cos t$, the same.

Answer 1.13. With $f=x$ and $g'=\sin x$, $g=-\cos x$: $\int_0^\pi x\sin x\,dx=\bigl[-x\cos x\bigr]_0^\pi+\int_0^\pi\cos x\,dx=\pi+\bigl[\sin x\bigr]_0^\pi=\pi$.

Answer 1.14. (a) $g$ is the matrix $X$ of Section 1.6, with eigenvalues $+1$ and $-1$: signature (1,1). (b) $g(e_0,e_0)=g_{00}=0$ and $g(e_1,e_1)=g_{11}=0$, and neither vector is zero. (c) $g(v,v)=2v^0v^1$, so $(1,1)^T$ is space-like ($g=2$) and $(1,-1)^T$ is time-like ($g=-2$). (d) $v_0=g_{0\nu}v^\nu=v^1$ and $v_1=g_{1\nu}v^\nu=v^0$: lowering exchanges the two components.

Answer 1.15. (a) $\eta(v,v)=1-1=0$: $v$ is null; $v_\mu=(1,0,0,0,-1,0,0,0)$. (b) $\eta(w,w)=-1-1=-2$: time-like. (c) $\eta(u,u)=1+1+1+1-1-1=2$: space-like.

Answer 1.16. (a) By the chain rule, $\dfrac{d\zeta}{dx^0}=\dfrac1{6H}\,\dfrac{\cos z}{\sin z}\,\dfrac{dz}{dx^0}=\dfrac1{6H}\cot z\cdot6H=\cot z$, so $d\zeta=\cot z\,dx^0$ and $d\zeta^2=\cot^2z\,(dx^0)^2$. (b) $e^{6H\zeta}=\sin z$, so $\sin^{1/3}z=(e^{6H\zeta})^{1/3}=e^{2H\zeta}$. (c) For $0<z<\pi/2$, $0<\sin z<1$, so $\ln\sin z<0$ and $\zeta$ takes all values in $(-\infty,0)$. This is the warped form of the metric used in Chapter 9 (Stage-2 document, §4.4).

Answer 1.17. (a) $\det g=-1-x^2$ and $d(\det g)/dx=-2x$. (b) By the $2\times2$ formula, $g^{-1}=\dfrac1{-1-x^2}\begin{pmatrix}-1&-x\\ -x&1\end{pmatrix}=\dfrac1{1+x^2}\begin{pmatrix}1&x\\ x&-1\end{pmatrix}$. With $dg/dx=\begin{pmatrix}0&1\\ 1&0\end{pmatrix}$, $g^{-1}\,dg/dx=\dfrac1{1+x^2}\begin{pmatrix}x&1\\ -1&x\end{pmatrix}$, whose trace is $2x/(1+x^2)$. Jacobi's formula: $\det g\cdot\mathrm{tr}(g^{-1}dg/dx)=(-1-x^2)\cdot2x/(1+x^2)=-2x$, which is the derivative computed in (a). (c) The determinant, the product of the two eigenvalues, is negative for every $x$, so one eigenvalue is positive and one negative: the signature is (1,1) for every $x$.
