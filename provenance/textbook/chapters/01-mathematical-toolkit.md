## 1. Mathematical toolkit from zero

The physics of this book is written in a small number of mathematical languages: vectors and matrices, complex numbers, indices with a summation rule, derivatives of functions of several variables, and metrics, which measure lengths in spaces whose directions need not all behave alike. This chapter builds these languages from school algebra and the calculus of one variable. Every later chapter uses them. The examples are deliberately small (two or three dimensions, matrices of size $2\times2$), because every rule that holds for them holds in the same form for the eight dimensions and $16\times16$ matrices of the rest of the book.

Where a standard fact of mathematics is used without proof, the text says so, and Section 1.13 lists all such facts.

### 1.1 Numbers, lists, sums and powers

**Numbers.** We use the natural numbers $0,1,2,3,\dots$ (we include 0), the integers $\dots,-2,-1,0,1,2,\dots$, the fractions (rational numbers) such as $-7/3$, and the real numbers, which include numbers like $\sqrt2$ and $\pi$ that are not fractions. The set of real numbers is written $\mathbb R$. The symbol $\in$ means "is an element of": $x\in\mathbb R$ says that $x$ is a real number. An **open interval** $(a,b)$ is the set of real numbers $x$ with $a<x<b$; for example $z\in(0,\pi/2)$ means $0<z<\pi/2$. Complex numbers are introduced in Section 1.5.

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

The **zero vector** $0$ has all components 0. The set of all vectors with $n$ real components is written $\mathbb R^n$; with complex components (Section 1.5) it is written $\mathbb C^n$. The field of this book has sixteen complex components at every point, so at each point it is a vector in $\mathbb C^{16}$, written $\Psi=(\Psi_0,\dots,\Psi_{15})^T$ (the $T$ is explained in Section 1.3).

**Example.** In $\mathbb R^3$, with $v=(1,2,0)^T$ and $w=(0,1,1)^T$: $v+w=(1,3,1)^T$ and $3v=(3,6,0)^T$.

**Linear combinations and bases.** A **linear combination** of vectors $u_0,\dots,u_{m-1}$ is a vector $c_0u_0+\dots+c_{m-1}u_{m-1}$ with numbers $c_k$. The vectors are **linearly independent** when the only linear combination that gives the zero vector is the one with all $c_k=0$; otherwise they are **linearly dependent**, and then one of them is a linear combination of the others. The **standard basis** of $\mathbb R^n$ consists of the $n$ vectors $e_0,\dots,e_{n-1}$, where $e_k$ has the component 1 in place $k$ and 0 elsewhere. Every vector is a linear combination of them, $v=\sum_{k=0}^{n-1}v_ke_k$, because component $j$ of the right-hand side is $\sum_kv_k(e_k)_j=v_j$ (only the term $k=j$ contributes). The standard basis vectors are linearly independent: $\sum_kc_ke_k$ is the vector with components $c_k$, and it is zero only if every $c_k$ is zero.

A **basis** is a list of linearly independent vectors of which every vector is a linear combination; the expansion coefficients are then unique. All bases of $\mathbb R^n$ (or $\mathbb C^n$) have exactly $n$ vectors; this number is the **dimension**. (This last fact is standard linear algebra and is used without proof.) The dimension counts basis vectors, not vectors: $\mathbb R^2$ contains infinitely many vectors but has dimension 2.

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
\Gamma=\begin{pmatrix}0&X\\ Y&0\end{pmatrix},\qquad \Gamma^2=\begin{pmatrix}0\cdot0+XY&0\cdot X+X\cdot0\\ Y\cdot0+0\cdot Y&YX+0\cdot0\end{pmatrix}=\begin{pmatrix}XY&0\\ 0&YX\end{pmatrix}.
$$

The notebook builds its $16\times16$ gamma matrices in exactly this form, with $8\times8$ blocks (Chapters 2 and 3).

**Tensor (Kronecker) product.** For an $m\times m$ matrix $A$ and an $n\times n$ matrix $B$, the **tensor product** $A\otimes B$ is the $mn\times mn$ matrix made of $m\times m$ blocks, block $(i,j)$ being $A_{ij}B$. For $2\times2$ matrices:

$$
A\otimes B=\begin{pmatrix}A_{00}B&A_{01}B\\ A_{10}B&A_{11}B\end{pmatrix},\qquad \text{for example}\qquad \begin{pmatrix}1&0\\ 0&-1\end{pmatrix}\otimes\begin{pmatrix}0&1\\ 1&0\end{pmatrix}=\begin{pmatrix}0&1&0&0\\ 1&0&0&0\\ 0&0&0&-1\\ 0&0&-1&0\end{pmatrix}.
$$

It obeys the **mixed-product rule** $(A\otimes B)(C\otimes D)=(AC)\otimes(BD)$. Proof: by the block rule, block $(i,k)$ of the product is $\sum_j(A_{ij}B)(C_{jk}D)=\bigl(\sum_jA_{ij}C_{jk}\bigr)BD=(AC)_{ik}\,BD$, which is block $(i,k)$ of $(AC)\otimes(BD)$. Four-fold tensor products of $2\times2$ matrices give $16\times16$ matrices; this is the second standard way of writing the gamma matrices of Pin(4,4) (Chapter 3).
