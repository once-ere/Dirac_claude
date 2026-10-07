## 4. Clifford algebra Cl(4,4) and the author's T16

The field equations of this book contain eight real $16 \times 16$ matrices, the **gamma matrices** $\gamma^{(x_1)}, \gamma^{(x_2)}, \dots, \gamma^{(x_8)}$, one for each direction of the author's eight-dimensional space-time. This chapter explains from zero why such matrices are needed, why they must have at least 16 rows and 16 columns, how the author built his matrices (he calls them T16) in his Mathematica notebook, which rules they obey, and what all their products together make up: the **Clifford algebra** Cl(4,4). The chapter has four worked examples, each a complete notebook. Notebook 04a rebuilds T16 from the author's formulas with exact whole-number arithmetic and checks every rule. Notebook 04b follows the square-root idea from the matrices of Pauli and Dirac to the author's eight gammas and to the plane waves of the field. Notebook 04c forms all 256 products of the gammas and proves that they make up all real $16 \times 16$ matrices. Notebook 04d builds a second set of gammas from three $2 \times 2$ matrices and finds the one and only change of basis between the two sets. Everything in this chapter is the algebra of constant matrices; it makes no statement about the creation of universes or about matter and antimatter.

### 4.1 Why matrices, and why sixteen components

The length of an arrow in the plane with the components $p$ and $q$ is $\sqrt{p^2 + q^2}$ (Pythagoras). A square root is an awkward object in an equation: it is not linear, and it cannot be differentiated term by term. In 1928 Paul Dirac looked for an equation for the electron that contains only first derivatives and whose square is the relation $E^2 = m^2 + k_1^2 + k_2^2 + k_3^2$ between the energy $E$, the mass $m$ and the momentum $(k_1, k_2, k_3)$ of a particle in special relativity. He found that a sum of squares can be written as the square of a **linear** expression, provided that its coefficients are matrices that **anticommute**: $\alpha\beta = -\beta\alpha$. Such matrices are called gamma matrices, and the rule they obey is the **Clifford relation**. Dirac needed four of them, for the time and the three directions of space, and the smallest ones are $4 \times 4$; that is why Dirac's electron field has four components.

The author's space-time has eight directions: the three directions $x_1, x_2, x_3$ of ordinary space, the time $x_4$, three **extra times** $x_5, x_6, x_7$, which deflate exponentially in the author's metric, and a hidden space direction $x_8$. Eight directions need eight gamma matrices, and Section 4.13 proves that eight such matrices must have at least $16 \times 16$ entries. This is why the fields dirac16complex and dirac16complex00 of this book have exactly sixteen components. The author's gamma matrices are **real**: every entry is $-1$, $0$ or $+1$. Later chapters use this fact (Chapter 5 and Chapter 7); this chapter only proves it.

The chapter proceeds as follows.

- Section 4.2 collects the facts about matrices that the chapter uses, each with its proof.
- Section 4.3 solves the square-root problem and derives the Clifford relation.
- Section 4.4 describes the eight directions of the author's space-time and the signs $\eta$ that tell space-like from time-like directions.
- Section 4.5 follows the author's construction of T16 step by step and proves its Clifford relation by hand; Notebook 04a (Sections 4.6 to 4.8) repeats the construction with the computer.
- Section 4.9 studies the square root of the 4+4 quadratic form and the plane waves of the field in flat 4+4 space, including what a momentum along an extra time does; Notebook 04b (Sections 4.10 to 4.12).
- Section 4.13 forms the 256 products of the gammas and proves that they are a basis of all real $16 \times 16$ matrices; Notebook 04c (Sections 4.14 to 4.16).
- Section 4.17 builds the gammas a second time, from $2 \times 2$ matrices, and proves that the two sets differ only by a renumbering of the sixteen components; Notebook 04d (Sections 4.18 to 4.20).
- Section 4.21 lists what was proved, computed and assumed, and Section 4.22 gives exercises with complete worked answers.

Every number of this chapter comes either from the Revision record or from the chapter's own notebooks, which reproduce the Revision record where they overlap. The Revision record files used here are:

- `Revision/algebra/gammas.json`: the eight gamma matrices of the author, written exactly;
- `Revision/algebra/reports/wolfram-algebra.json`: 45 checks, all passed, computed with WolframScript;
- `Revision/algebra/reports/python-algebra.json`: 35 checks, all passed, computed independently with Python;
- `Revision/algebra/reports/python-gammas.json`: the gammas as rebuilt by the Python program;
- `Revision/theory/reports/python-field-theory.json` (70 checks, all passed) and `Revision/theory/reports/python-scope.json` (14 checks, all passed), for the plane waves of Notebook 04b.

Each statement carries a label: PROVED (exact, with the proof in the text and the record file and check that confirm it), COMPUTED (a floating-point computation with its measured accuracy), ASSUMED (taken as given), HYPOTHESIS or OPEN.

### 4.2 The matrix tools of this chapter

This section defines every word about matrices that the chapter uses and proves every rule.

**Matrices and their entries.** An $n \times n$ **matrix** $M$ is a square table of numbers with $n$ rows and $n$ columns. $M_{ij}$ is the **entry** in row $i$ and column $j$. The notebooks count rows and columns from 0 (Python's convention), so a $16 \times 16$ matrix has the rows $0, 1, \dots, 15$. The author's formulas for his $4 \times 4$ building blocks count from 1, as Mathematica does; where this chapter uses them it says so. A **column** $u$ is a list of $n$ numbers $u_0, \dots, u_{n-1}$ written one below the other; the matrix acts on it by $(Mu)_i = \sum_j M_{ij} u_j$.

**The product.** The product of two $n \times n$ matrices is

$$
(AB)_{ij} = \sum_{k} A_{ik} B_{kj} ,
$$

row $i$ of $A$ times column $j$ of $B$, entry by entry, added up. In Python it is written `A @ B`. Products are **associative**, $(AB)D = A(BD)$ (both sides are $\sum_{k,l} A_{ik}B_{kl}D_{lj}$), so brackets may be left out. They are not **commutative**: in general $AB \neq BA$. For example, with

$$
A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad B = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}: \qquad AB = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \qquad BA = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} = -AB .
$$

The **identity matrix** $I_n$ has 1 on the diagonal and 0 elsewhere, so $I_n M = M I_n = M$. A number $c$ times a matrix multiplies every entry by $c$; $c I_n$ is called a **multiple of the identity**. The **Kronecker delta** $\delta_{ij}$ is 1 if $i = j$ and 0 otherwise, so $(I_n)_{ij} = \delta_{ij}$.

**Commutator and anticommutator.** For two matrices $A$ and $B$,

$$
[A, B] = AB - BA, \qquad \{A, B\} = AB + BA .
$$

$A$ and $B$ **commute** if $[A, B] = 0$, that is $AB = BA$, and **anticommute** if $\{A, B\} = 0$, that is $AB = -BA$. The two matrices of the example above anticommute.

**The transpose.** The transpose $M^T$ exchanges rows and columns: $(M^T)_{ij} = M_{ji}$. The transpose of a product is the product of the transposes in the opposite order, $(AB)^T = B^T A^T$. Proof, line by line:

1. $((AB)^T)_{ij} = (AB)_{ji}$ — definition of the transpose.
2. $(AB)_{ji} = \sum_k A_{jk} B_{ki}$ — definition of the product.
3. $\sum_k A_{jk} B_{ki} = \sum_k (B^T)_{ik} (A^T)_{kj}$ — each factor rewritten with the definition of the transpose, and the two numbers in each term exchanged (numbers commute).
4. $\sum_k (B^T)_{ik} (A^T)_{kj} = (B^T A^T)_{ij}$ — definition of the product.

$M$ is **symmetric** if $M^T = M$ and **antisymmetric** if $M^T = -M$. An antisymmetric matrix has zeros on its diagonal, because $M_{ii} = -M_{ii}$.

**Inverse and orthogonal matrices.** The **inverse** $M^{-1}$ of $M$, when it exists, satisfies $M M^{-1} = M^{-1} M = I_n$. A real matrix is **orthogonal** if $M^T M = I_n$; then $M^{-1} = M^T$.

**Signed permutation matrices.** A **signed permutation matrix** has exactly one nonzero entry in every row and in every column, and that entry is $+1$ or $-1$. Acting on a column it puts the components into a new order and changes some of their signs. We describe such a matrix by the **code** of each row: the code $+5$ in row 2 means that the only nonzero entry of row 2 is $+1$ in column 5, so $(Mu)_2 = +u_5$; the code $-0$ means $-u_0$. Every signed permutation matrix is orthogonal. Proof: $(M^T M)_{ij} = \sum_k (M^T)_{ik} M_{kj} = \sum_k M_{ki} M_{kj}$ (definitions of product and transpose). For $i \neq j$ no row $k$ has nonzero entries in both columns $i$ and $j$ (a row has only one nonzero entry), so every term is 0. For $i = j$ exactly one row $k$ has a nonzero entry in column $i$, and it contributes $(\pm 1)^2 = 1$. So $M^T M = I_n$.

**Block matrices.** A $16 \times 16$ matrix can be cut into four $8 \times 8$ **blocks** (upper left, upper right, lower left, lower right), and an $8 \times 8$ matrix into four $4 \times 4$ blocks. Block matrices multiply like $2 \times 2$ matrices whose entries are matrices, keeping the order of the factors:

$$
\begin{pmatrix} A & B \\ C & D \end{pmatrix} \begin{pmatrix} E & F \\ K & L \end{pmatrix} = \begin{pmatrix} AE + BK & AF + BL \\ CE + DK & CF + DL \end{pmatrix} .
$$

Proof: the entry in row $i$ and column $j$ of the product is a sum over all columns $k$ of the first factor; split it into the sum over the columns of the left half and the sum over the columns of the right half. For a row $i$ of the upper half and a column $j$ of the left half, the first part is the entry of $AE$ and the second the entry of $BK$; the other three positions work in the same way. In the same way the transpose of a block matrix transposes the pattern and every block:

$$
\begin{pmatrix} A & B \\ C & D \end{pmatrix}^T = \begin{pmatrix} A^T & C^T \\ B^T & D^T \end{pmatrix} .
$$

A matrix whose two off-diagonal blocks are zero is **block diagonal**; one whose two diagonal blocks are zero is **block off-diagonal**. By the block rule, the product of two block off-diagonal matrices is block diagonal, and the product of a block diagonal and a block off-diagonal matrix is block off-diagonal.

**The trace.** The trace $\mathrm{tr}\, M$ is the sum of the diagonal entries. It has the **cyclic property** $\mathrm{tr}(AB) = \mathrm{tr}(BA)$. Proof: $\mathrm{tr}(AB) = \sum_i \sum_k A_{ik} B_{ki}$ (definitions), and exchanging the order of the two finite sums and of the two numbers in each term gives $\sum_k \sum_i B_{ki} A_{ik} = \mathrm{tr}(BA)$.

**The permutation sign.** For a list of different numbers, an **inversion** is a pair of positions in which the larger number stands first. The **permutation sign** of the list (Mathematica calls it *Signature*) is $+1$ if the number of inversions is even and $-1$ if it is odd; for a list in which a number occurs twice it is 0. Examples: $(1, 2, 3, 4)$ has no inversion, sign $+1$; $(2, 1, 3, 4)$ has one, the pair $(2, 1)$, sign $-1$; $(2, 3, 1, 4)$ has two, the pairs $(2, 1)$ and $(3, 1)$, sign $+1$; $(1, 1, 3, 4)$ has sign 0. **Exchanging two entries of a list flips its sign.** Proof: exchanging two *neighbouring* entries changes only whether this one pair is an inversion (every other pair keeps its order), so the number of inversions changes by exactly one. Exchanging the entries at the positions $i < j$ can be done with neighbour exchanges: move the entry at position $i$ to the right, past $j - i$ neighbours, to position $j$; then the entry that was at position $j$ stands at position $j - 1$; move it to the left, past $j - i - 1$ neighbours, to position $i$. That is $2(j - i) - 1$ neighbour exchanges, an odd number, so the sign flips.

### 4.3 The square-root problem and the Clifford relation

**Numbers are not enough.** Can $\sqrt{p^2 + q^2}$ be written as $\alpha p + \beta q$ with fixed coefficients $\alpha$ and $\beta$, for all numbers $p$ and $q$? Square the candidate, keeping $\alpha\beta$ and $\beta\alpha$ apart, because for matrices the order matters:

1. $(\alpha p + \beta q)^2 = (\alpha p + \beta q)(\alpha p + \beta q)$ — definition of the square.
2. $= \alpha p\, \alpha p + \alpha p\, \beta q + \beta q\, \alpha p + \beta q\, \beta q$ — multiplied out (distributive law).
3. $= \alpha^2 p^2 + (\alpha\beta + \beta\alpha)\, pq + \beta^2 q^2$ — the numbers $p$ and $q$ commute with everything and are moved to the right.

This must equal $p^2 + q^2$ for all $p$ and $q$. With $p = 1$, $q = 0$ it gives $\alpha^2 = 1$; with $p = 0$, $q = 1$ it gives $\beta^2 = 1$; with $p = q = 1$ it gives $\alpha^2 + \beta^2 + \alpha\beta + \beta\alpha = 2$, hence $\alpha\beta + \beta\alpha = 0$. Conversely, these three conditions make line 3 equal to $p^2 + q^2$. For ordinary numbers $\alpha\beta + \beta\alpha = 2\alpha\beta$, and $2\alpha\beta = 0$ forces $\alpha = 0$ or $\beta = 0$, which contradicts $\alpha^2 = \beta^2 = 1$. So no two numbers solve the problem (status PROVED; Notebook 04b confirms with sympy that the three equations have no solution).

**Matrices are enough.** The two matrices of Section 4.2,

$$
\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix},
$$

satisfy $\sigma_x^2 = \sigma_z^2 = I_2$ (multiply out) and anticommute ($\sigma_z\sigma_x = -\sigma_x\sigma_z$, computed in Section 4.2). By line 3, with the number 1 replaced by $I_2$: $(p\sigma_x + q\sigma_z)^2 = (p^2 + q^2) I_2$. Example: $p = 3$, $q = 4$ gives

$$
3\sigma_x + 4\sigma_z = \begin{pmatrix} 4 & 3 \\ 3 & -4 \end{pmatrix}, \qquad \begin{pmatrix} 4 & 3 \\ 3 & -4 \end{pmatrix}^2 = \begin{pmatrix} 16 + 9 & 12 - 12 \\ 12 - 12 & 9 + 16 \end{pmatrix} = 25\, I_2 ,
$$

a matrix square root of $25 = 3^2 + 4^2$. Space-time needs **minus signs** too, and a real matrix can square to $-I_2$:

$$
N = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}, \qquad N^2 = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} = -I_2, \qquad \sigma_x N = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix} = -N\sigma_x .
$$

So $(p\sigma_x + qN)^2 = p^2 I_2 + q^2 N^2 = (p^2 - q^2) I_2$: a real square root of a *difference* of squares.

**The general rule.** We want matrices $\gamma^1, \dots, \gamma^n$ such that, for given signs $\eta^{aa} = \pm 1$ and for all numbers $p_1, \dots, p_n$,

$$
\Bigl(\sum_a p_a \gamma^a\Bigr)^2 = \Bigl(\sum_a \eta^{aa} p_a^2\Bigr) I .
$$

The signs are collected in the diagonal matrix $\eta = \mathrm{diag}(\eta^{11}, \dots, \eta^{nn})$; its off-diagonal entries are $\eta^{ab} = 0$ for $a \neq b$. The left side, line by line:

1. $\bigl(\sum_a p_a \gamma^a\bigr)^2 = \bigl(\sum_a p_a \gamma^a\bigr)\bigl(\sum_b p_b \gamma^b\bigr)$ — definition of the square; the summation letter of the second factor is called $b$, which changes nothing.
2. $= \sum_{a,b} p_a p_b\, \gamma^a \gamma^b$ — multiplied out; the numbers $p_a p_b$ are moved to the front.
3. $= \sum_{a,b} p_a p_b\, \gamma^b \gamma^a$ — the same sum with the two summation letters renamed ($a$ called $b$ and $b$ called $a$), and $p_b p_a = p_a p_b$.
4. $= \tfrac12 \sum_{a,b} p_a p_b\, (\gamma^a\gamma^b + \gamma^b\gamma^a)$ — half the sum of lines 2 and 3, which are equal.

If the **Clifford relation**

$$
\gamma^a \gamma^b + \gamma^b \gamma^a = 2 \eta^{ab} I \qquad \text{for all } a, b
$$

holds, line 4 becomes $\tfrac12 \sum_{a,b} p_a p_b\, 2\eta^{ab} I = \sum_a \eta^{aa} p_a^2\, I$ (only $a = b$ survives), the wanted square. Conversely, if the square rule holds for all $p$: choose $p_a = 1$ and all other $p$ zero, then the left side is $(\gamma^a)^2$ and the right side $\eta^{aa} I$; choose $p_a = p_b = 1$ for two different $a, b$ and all other $p$ zero, then the left side is $(\gamma^a + \gamma^b)^2 = (\gamma^a)^2 + (\gamma^b)^2 + \gamma^a\gamma^b + \gamma^b\gamma^a$ and the right side $(\eta^{aa} + \eta^{bb}) I$, so $\gamma^a\gamma^b + \gamma^b\gamma^a = 0$. So **the square-root rule and the Clifford relation say the same thing** (status PROVED). In words: each gamma matrix squares to $+I$ for a direction with sign $+1$ (a **space-like** direction) and to $-I$ for a direction with sign $-1$ (a **time-like** direction), and two different gamma matrices anticommute.

**Pauli's three matrices.** For three space directions (signs $+1, +1, +1$) a third $2 \times 2$ matrix is needed that squares to $+I_2$ and anticommutes with $\sigma_x$ and $\sigma_z$. No real one exists (Exercise 1 of Section 4.22 shows what the real $N$ gives instead), but a complex one does. With the imaginary unit $i$, $i^2 = -1$, the three **Pauli matrices** (Wolfgang Pauli, 1927) are

$$
\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} .
$$

For example $\sigma_x\sigma_y = \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix} = i\sigma_z$ and $\sigma_y\sigma_x = -i\sigma_z$, so they anticommute; and $\sigma_x\sigma_y\sigma_z = i\sigma_z\sigma_z = iI_2$.

**Dirac's four matrices.** Four anticommuting matrices do not fit into $2 \times 2$ matrices (Section 4.13 proves that four need at least $4 \times 4$). Dirac's choice, in the convention of particle physicists with the time first and the signs $(+1, -1, -1, -1)$, is made of $2 \times 2$ blocks (the letter D keeps these matrices apart from the author's):

$$
\gamma_D^0 = \begin{pmatrix} I_2 & 0 \\ 0 & -I_2 \end{pmatrix}, \qquad \gamma_D^j = \begin{pmatrix} 0 & \sigma_j \\ -\sigma_j & 0 \end{pmatrix} \quad (j = x, y, z) .
$$

By the block rule of Section 4.2: $(\gamma_D^0)^2 = \mathrm{diag}(I_2, I_2) = I_4$; $(\gamma_D^j)^2 = \mathrm{diag}(-\sigma_j^2, -\sigma_j^2) = -I_4$; $\gamma_D^0\gamma_D^j = \begin{pmatrix} 0 & \sigma_j \\ \sigma_j & 0 \end{pmatrix}$ and $\gamma_D^j\gamma_D^0 = \begin{pmatrix} 0 & -\sigma_j \\ -\sigma_j & 0 \end{pmatrix}$, which anticommute; and for $j \neq k$, $\gamma_D^j\gamma_D^k + \gamma_D^k\gamma_D^j = \mathrm{diag}(-\{\sigma_j, \sigma_k\}, -\{\sigma_j, \sigma_k\}) = 0$.

**Dirac's equation contains the energy relation.** For a plane wave $\psi = u\, e^{-i(Et - k_1x_1 - k_2x_2 - k_3x_3)}$ with a constant column $u$, Dirac's equation $i(\gamma_D^0\partial_t + \gamma_D^x\partial_1 + \gamma_D^y\partial_2 + \gamma_D^z\partial_3)\psi = m\psi$ becomes $(P - m I_4) u = 0$ with $P = E\gamma_D^0 - k_1\gamma_D^x - k_2\gamma_D^y - k_3\gamma_D^z$ (the derivative of $e^{cx}$ is $c\, e^{cx}$; multiply by $i$; divide by the exponential, which is never zero). By the general rule with the signs $(+1, -1, -1, -1)$, $P^2 = (E^2 - k_1^2 - k_2^2 - k_3^2) I_4$. A nonzero $u$ with $Pu = mu$ gives $P^2 u = P(mu) = m^2 u$, hence $(E^2 - k_1^2 - k_2^2 - k_3^2 - m^2) u = 0$, and because $u \neq 0$, $E^2 = m^2 + k_1^2 + k_2^2 + k_3^2$: the energy relation of special relativity, the **mass shell**. Notebook 04b checks all of this exactly and shows it in pictures.

**The Clifford algebra.** Given $n$ matrices with a Clifford relation, the set of all their real linear combinations of products is called the **Clifford algebra** of the signs $\eta$; with $p$ signs $+1$ and $q$ signs $-1$ it is written Cl$(p, q)$. The author's space-time has four space-like and four time-like directions, so its Clifford algebra is Cl(4,4). Section 4.13 shows that it is the set of all real $16 \times 16$ matrices.

### 4.4 The eight directions of the author's space-time and their signs

The author's metric is the diagonal $8 \times 8$ matrix $g$ that gives the squared length of a small step: a step $dx_\mu$ along the coordinate $x_\mu$ has the squared length $g_{\mu\mu}\, dx_\mu^2$. Its diagonal entries, in the order of the author's coordinates $x_1, \dots, x_8$, are $e^{2a_4}\sin^{1/3} z$ three times, $-1$, $-e^{-2a_4}\sin^{1/3} z$ three times, and $\cot^2 z$, where $a_4$ is a function of the time $x_4$, $z = 6 H x_8$ lies between 0 and $\pi/2$, and $H > 0$ is the author's constant (Chapter 3 studies this metric in full). A direction with $g_{\mu\mu} > 0$ is **space-like**, one with $g_{\mu\mu} < 0$ is **time-like**. The **frame factor** of a direction is $\sqrt{\lvert g_{\mu\mu} \rvert}$: a coordinate step $dx_\mu$ is a step of the length $\sqrt{\lvert g_{\mu\mu} \rvert}\, \lvert dx_\mu \rvert$.

| coordinate | role | metric entry | frame factor | sign $\eta$ |
| --- | --- | --- | --- | --- |
| $x_1, x_2, x_3$ | ordinary 3-space, inflating | $e^{2a_4}\sin^{1/3} z$ | $e^{a_4}\sin^{1/6} z$ | $+1$ |
| $x_4$ | the time | $-1$ | $1$ | $-1$ |
| $x_5, x_6, x_7$ | the extra times, deflating exponentially | $-e^{-2a_4}\sin^{1/3} z$ | $e^{-a_4}\sin^{1/6} z$ | $-1$ |
| $x_8$ | the hidden space direction | $\cot^2 z$ | $\cot z$ | $+1$ |

When $a_4$ grows with the time $x_4$, the frame factor $e^{a_4}$ of 3-space grows (3-space **inflates**) and the frame factor $e^{-a_4}$ of the extra times shrinks exponentially (the extra times **deflate**). Chapter 12 derives the equations that govern $a_4$.

At every point one can choose eight perpendicular directions of unit length, one along each coordinate: a **frame**. Measured in the frame, the metric becomes the diagonal matrix of signs

$$
\eta = \mathrm{diag}(+1, +1, +1, -1, -1, -1, -1, +1) \qquad (\text{order } x_1, \dots, x_8):
$$

four space-like directions ($x_1, x_2, x_3, x_8$) and four time-like ones ($x_4, x_5, x_6, x_7$), the **signature** (4,4). Because $\eta$ is diagonal with entries $\pm 1$, the entries of $\eta$ and of its inverse are the same numbers, $\eta^{ab} = \eta_{ab}$. The gamma matrices belong to the frame directions: $\gamma^{(x_a)}$ is the gamma matrix of the frame direction along $x_a$, and they satisfy the Clifford relation with this $\eta$. They are **constant**: the same matrices at every point and at every time. The inflation of 3-space and the deflation of the extra times reach the field equation only through the frame factors: the field equation contains $\gamma^\mu = \gamma^{(x_\mu)} / \sqrt{\lvert g_{\mu\mu} \rvert}$, for example $\gamma^{(x_5)}$ multiplied by $e^{a_4}\sin^{-1/6} z$, a factor that grows as the extra time $x_5$ deflates. The gamma matrices themselves never change.

The author's Mathematica notebook numbers the frame directions in its own order, $A = 0, \dots, 7$: $A = 0$ is the hidden direction, $A = 1, 2, 3$ are 3-space, $A = 4$ is the time and $A = 5, 6, 7$ are the extra times, and its matrix of signs is eta4488 $= \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$ (his input cell In[45]). Translated to the author's coordinates (the coordinate map of the Revision record):

| coordinate | $x_1$ | $x_2$ | $x_3$ | $x_4$ | $x_5$ | $x_6$ | $x_7$ | $x_8$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| index $A$ of T16 in the author's notebook | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 0 |
| sign $\eta$ | $+1$ | $+1$ | $+1$ | $-1$ | $-1$ | $-1$ | $-1$ | $+1$ |

So $\gamma^{(x_k)} = $ T16[$k$] for $k = 1, \dots, 7$ and $\gamma^{(x_8)} = $ T16[0], and the sign of each coordinate is the entry of eta4488 at its index $A$. Status: ASSUMED (the metric and the coordinate roles are the author's input; the map is the one the Revision record uses and checks: `Revision/algebra/reports/wolfram-algebra.json`, checks `coordinate_map` and `eta_in_author_order`).

### 4.5 The author's construction of T16, step by step

The author builds his matrices in his Mathematica notebook, whose file name is

```text
Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb
```

in four steps. The Revision record re-typed his formulas from the input cells In[45], In[46], In[294], In[300], In[301], In[338], In[351], In[370], In[371] and In[372] (the notebook itself is only read, never changed) and rebuilt the matrices twice, with WolframScript and with Python. This section follows the four steps and proves, by hand, every rule that the computer checks in Notebook 04a.

**Step 1: six $4 \times 4$ blocks.** For $h = 1, 2, 3$ and $p, q = 1, 2, 3, 4$ (counted from 1, as in the author's formulas) the author defines two patterns (In[294]):

$$
Q_a[h]_{pq} = \mathrm{Signature}[\{h, p, q, 4\}], \qquad Q_b[h]_{pq} = \delta_{p4}\delta_{qh} - \delta_{ph}\delta_{q4} ,
$$

and from them the blocks s4[$h$] $= Q_a[h] - Q_b[h]$ (In[300]) and t4[$h$] $= Q_a[h] + Q_b[h]$ (In[301]). $Q_a[h]_{pq}$ is the permutation sign of the list $(h, p, q, 4)$; it is nonzero only when $h, p, q, 4$ are four different numbers. $Q_b[h]$ has exactly two nonzero entries: $+1$ in row 4, column $h$, and $-1$ in row $h$, column 4. A worked example for $h = 1$:

- row 1, column 4 of s4[1]: $Q_a = \mathrm{Signature}[\{1, 1, 4, 4\}] = 0$ (repeated numbers) and $Q_b = \delta_{14}\delta_{41} - \delta_{11}\delta_{44} = -1$, so the entry is $0 - (-1) = +1$;
- row 2, column 3: $Q_a = \mathrm{Signature}[\{1, 2, 3, 4\}] = +1$ and $Q_b = 0$, so the entry is $+1$;
- row 3, column 2: $Q_a = \mathrm{Signature}[\{1, 3, 2, 4\}] = -1$ (one inversion) and $Q_b = 0$, so the entry is $-1$;
- row 4, column 1: $Q_a = 0$ and $Q_b = \delta_{44}\delta_{11} = +1$, so the entry is $0 - 1 = -1$;
- every other entry is 0, because $Q_a$ and $Q_b$ vanish there.

All six blocks, computed in this way (Notebook 04a prints them and compares them with the six matrices that the author's notebook displays in its output Out[304]):

$$
\mathrm{s4}[1] = \begin{pmatrix} 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & -1 & 0 & 0 \\ -1 & 0 & 0 & 0 \end{pmatrix}, \quad \mathrm{s4}[2] = \begin{pmatrix} 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0 \end{pmatrix}, \quad \mathrm{s4}[3] = \begin{pmatrix} 0 & 1 & 0 & 0 \\ -1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & -1 & 0 \end{pmatrix},
$$

$$
\mathrm{t4}[1] = \begin{pmatrix} 0 & 0 & 0 & -1 \\ 0 & 0 & 1 & 0 \\ 0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \end{pmatrix}, \quad \mathrm{t4}[2] = \begin{pmatrix} 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & -1 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix}, \quad \mathrm{t4}[3] = \begin{pmatrix} 0 & 1 & 0 & 0 \\ -1 & 0 & 0 & 0 \\ 0 & 0 & 0 & -1 \\ 0 & 0 & 1 & 0 \end{pmatrix} .
$$

*The blocks are antisymmetric.* Exchanging $p$ and $q$ exchanges two entries of the list $(h, p, q, 4)$, which flips its permutation sign (Section 4.2): $Q_a[h]_{qp} = -Q_a[h]_{pq}$. Exchanging $p$ and $q$ in $Q_b$ turns $\delta_{p4}\delta_{qh} - \delta_{ph}\delta_{q4}$ into $\delta_{q4}\delta_{ph} - \delta_{qh}\delta_{p4}$, which is minus the original: $Q_b[h]_{qp} = -Q_b[h]_{pq}$. A sum or difference of antisymmetric matrices is antisymmetric, so s4[$h$] and t4[$h$] are antisymmetric.

*The blocks are quaternion multiplications.* A **quaternion** is $q = q_4 + q_1\mathbf{i} + q_2\mathbf{j} + q_3\mathbf{k}$ with four real numbers; we store it as the list $(q_1, q_2, q_3, q_4)$, the real part last, to match the blocks. Quaternions are multiplied with Hamilton's rules $\mathbf{i}^2 = \mathbf{j}^2 = \mathbf{k}^2 = -1$, $\mathbf{ij} = \mathbf{k} = -\mathbf{ji}$, $\mathbf{jk} = \mathbf{i} = -\mathbf{kj}$, $\mathbf{ki} = \mathbf{j} = -\mathbf{ik}$, and their multiplication is associative. For a fixed quaternion $u$ the **right multiplication** $R_u$ maps $q$ to $q\,u$ and the **left multiplication** $L_u$ maps $q$ to $u\,q$; both are linear, so each is a $4 \times 4$ matrix, whose column $p$ holds the components of $e_p u$ (or $u e_p$), where $e_1 = \mathbf{i}$, $e_2 = \mathbf{j}$, $e_3 = \mathbf{k}$, $e_4 = 1$. Example: the columns of $R_{\mathbf{i}}$ are the components of $\mathbf{i}\mathbf{i} = -1$, $\mathbf{j}\mathbf{i} = -\mathbf{k}$, $\mathbf{k}\mathbf{i} = \mathbf{j}$ and $1\,\mathbf{i} = \mathbf{i}$, that is $(0, 0, 0, -1)$, $(0, 0, -1, 0)$, $(0, 1, 0, 0)$ and $(1, 0, 0, 0)$; these are exactly the four columns of s4[1] above. In the same way (Notebook 04a checks all six):

$$
\mathrm{s4}[h] = R_{u_h}, \qquad \mathrm{t4}[h] = -L_{u_h}, \qquad u_1 = \mathbf{i},\ u_2 = \mathbf{j},\ u_3 = \mathbf{k} .
$$

This explains every rule of the blocks. Line by line:

1. $R_u R_w = R_{wu}$ — because $R_u(R_w(q)) = (q\,w)\,u = q\,(w\,u)$ (associativity).
2. $L_u L_w = L_{uw}$ — because $L_u(L_w(q)) = u\,(w\,q) = (u\,w)\,q$.
3. $L_u R_w = R_w L_u$ — because $u\,(q\,w) = (u\,q)\,w$ (associativity).
4. $R_{-1} = L_{-1} = -I_4$ — multiplying by the number $-1$ changes every sign.
5. s4[$h$]$^2 = R_{u_h u_h} = R_{-1} = -I_4$ and t4[$h$]$^2 = (-1)^2 L_{u_h u_h} = -I_4$ — by lines 1, 2 and 4 and $\mathbf{i}^2 = \mathbf{j}^2 = \mathbf{k}^2 = -1$.
6. For $h \neq k$: s4[$h$] s4[$k$] $= R_{u_k u_h} = -R_{u_h u_k} = -$s4[$k$] s4[$h$] — by line 1, because two different units anticommute ($u_k u_h = -u_h u_k$) and $R$ is linear; t4 works in the same way with line 2.
7. s4[$h$] t4[$k$] $= -R_{u_h} L_{u_k} = -L_{u_k} R_{u_h} = $ t4[$k$] s4[$h$] — by line 3: every s-block commutes with every t-block.

So the s-blocks anticommute among themselves and square to $-I_4$, the t-blocks do the same, and every s-block commutes with every t-block: $\{\mathrm{s4}[h], \mathrm{s4}[k]\} = \{\mathrm{t4}[h], \mathrm{t4}[k]\} = -2\delta_{hk} I_4$ and $[\mathrm{s4}[h], \mathrm{t4}[k]] = 0$. Two further products are needed below. By lines 1 and 2, s4[1] s4[2] s4[3] $= R_{\mathbf{i}} R_{\mathbf{j}} R_{\mathbf{k}} = R_{\mathbf{kji}}$, and $\mathbf{kji} = (\mathbf{kj})\mathbf{i} = -\mathbf{i}\mathbf{i} = 1$, so s4[1] s4[2] s4[3] $= I_4$; and t4[3] t4[2] t4[1] $= (-1)^3 L_{\mathbf{k}} L_{\mathbf{j}} L_{\mathbf{i}} = -L_{\mathbf{kji}} = -I_4$.

The author calls s4 *self-dual* and t4 *anti-self-dual*. The **dual** of an antisymmetric $4 \times 4$ matrix $M$ is $(\star M)_{pq} = \tfrac12\sum_{r,s}\epsilon_{pqrs} M_{rs}$, where the **Levi-Civita symbol** $\epsilon_{pqrs}$ is the permutation sign of $(p, q, r, s)$. For an antisymmetric $M$ the two surviving terms of each sum are equal; for example $(\star M)_{12} = \tfrac12(\epsilon_{1234}M_{34} + \epsilon_{1243}M_{43}) = \tfrac12(M_{34} + (-1)(-M_{34})) = M_{34}$. In the same way $(\star M)_{13} = -M_{24}$ and $(\star M)_{14} = M_{23}$, so $M$ is self-dual ($\star M = M$) when $M_{12} = M_{34}$, $M_{13} = -M_{24}$ and $M_{14} = M_{23}$, and anti-self-dual ($\star M = -M$) when $M_{12} = -M_{34}$, $M_{13} = M_{24}$ and $M_{14} = -M_{23}$. Read off from the matrices above: s4[1] has $M_{12} = 0 = M_{34}$, $M_{13} = 0 = -M_{24}$, $M_{14} = 1 = M_{23}$ (self-dual), and t4[1] has $M_{14} = -1$, $M_{23} = 1$ (anti-self-dual).

**Step 2: the $8 \times 8$ matrices.** With $4 \times 4$ blocks (In[46], In[338], In[351]):

$$
\sigma = \begin{pmatrix} 0 & I_4 \\ I_4 & 0 \end{pmatrix}, \quad \tau_0 = I_8, \quad \tau_h = \begin{pmatrix} 0 & \mathrm{s4}[h] \\ \mathrm{s4}[h] & 0 \end{pmatrix}, \quad \tau_{7-h} = \begin{pmatrix} 0 & \mathrm{t4}[h] \\ -\mathrm{t4}[h] & 0 \end{pmatrix} \quad (h = 1, 2, 3),
$$

so $\tau_6$ comes from t4[1], $\tau_5$ from t4[2] and $\tau_4$ from t4[3]; then $\tau_7 = \tau_1\tau_2\tau_3\tau_4\tau_5\tau_6$, $\bar\tau_0 = I_8$ and $\bar\tau_A = \sigma\,\tau_A^T\,\sigma$ for $A = 1, \dots, 7$ (the author writes tau[A] and taubar[A]). The rules of these matrices follow from the block rule and Step 1, line by line:

1. $\sigma \begin{pmatrix} A & B \\ C & D \end{pmatrix} \sigma = \begin{pmatrix} D & C \\ B & A \end{pmatrix}$ — the block rule, applied twice: $\sigma$ on the left exchanges the two block rows, on the right the two block columns.
2. $\tau_h^2 = \mathrm{diag}(\mathrm{s4}[h]^2, \mathrm{s4}[h]^2) = -I_8$ and $\tau_{7-h}^2 = \mathrm{diag}(-\mathrm{t4}[h]^2, -\mathrm{t4}[h]^2) = +I_8$ — block rule and Step 1, line 5.
3. $\tau_h\tau_k + \tau_k\tau_h = \mathrm{diag}(\{\mathrm{s4}[h], \mathrm{s4}[k]\}, \{\mathrm{s4}[h], \mathrm{s4}[k]\}) = 0$ for $h \neq k$, and in the same way $\tau_{7-h}\tau_{7-k} + \tau_{7-k}\tau_{7-h} = \mathrm{diag}(-\{\mathrm{t4}[h], \mathrm{t4}[k]\}, -\{\mathrm{t4}[h], \mathrm{t4}[k]\}) = 0$ — block rule and Step 1.
4. $\tau_h\tau_{7-k} + \tau_{7-k}\tau_h = \mathrm{diag}(-\mathrm{s4}[h]\mathrm{t4}[k] + \mathrm{t4}[k]\mathrm{s4}[h],\ \mathrm{s4}[h]\mathrm{t4}[k] - \mathrm{t4}[k]\mathrm{s4}[h]) = 0$ — block rule; the s-blocks commute with the t-blocks.
5. $\tau_1\tau_2\tau_3 = \begin{pmatrix} 0 & \mathrm{s4}[1]\mathrm{s4}[2]\mathrm{s4}[3] \\ \mathrm{s4}[1]\mathrm{s4}[2]\mathrm{s4}[3] & 0 \end{pmatrix} = \sigma$ — block rule twice, and s4[1] s4[2] s4[3] $= I_4$.
6. $\tau_4\tau_5\tau_6 = \begin{pmatrix} 0 & -\mathrm{t4}[3]\mathrm{t4}[2]\mathrm{t4}[1] \\ \mathrm{t4}[3]\mathrm{t4}[2]\mathrm{t4}[1] & 0 \end{pmatrix} = \begin{pmatrix} 0 & I_4 \\ -I_4 & 0 \end{pmatrix}$ — block rule twice, and t4[3] t4[2] t4[1] $= -I_4$.
7. $\tau_7 = (\tau_1\tau_2\tau_3)(\tau_4\tau_5\tau_6) = \begin{pmatrix} 0 & I_4 \\ I_4 & 0 \end{pmatrix}\begin{pmatrix} 0 & I_4 \\ -I_4 & 0 \end{pmatrix} = \begin{pmatrix} -I_4 & 0 \\ 0 & I_4 \end{pmatrix}$ — lines 5 and 6 and the block rule.
8. $\tau_7^2 = I_8$, and $\tau_7$ anticommutes with $\tau_1, \dots, \tau_6$ — $\tau_7$ is diagonal with the blocks $-I_4$ and $I_4$; multiplying a block off-diagonal matrix by it from the left flips the sign of the upper-right block, from the right the sign of the lower-left block, so the two products differ by a sign.
9. $\tau_4\tau_5\tau_6\tau_7 = \begin{pmatrix} 0 & I_4 \\ -I_4 & 0 \end{pmatrix}\begin{pmatrix} -I_4 & 0 \\ 0 & I_4 \end{pmatrix} = \sigma$ and $\tau_1\tau_2\cdots\tau_7 = \tau_7\tau_7 = I_8$ — line 6, the block rule, and the definition $\tau_1\cdots\tau_6 = \tau_7$.
10. $\bar\tau_A = -\tau_A$ for $A = 1, \dots, 7$ — for $A = h$: $\tau_h^T = \begin{pmatrix} 0 & \mathrm{s4}[h]^T \\ \mathrm{s4}[h]^T & 0 \end{pmatrix} = -\tau_h$ (block transpose, s4 antisymmetric), and by line 1 $\sigma\tau_h\sigma = \tau_h$, so $\bar\tau_h = -\tau_h$; for $A = 7 - h$: $\tau_{7-h}^T = \begin{pmatrix} 0 & -\mathrm{t4}[h]^T \\ \mathrm{t4}[h]^T & 0 \end{pmatrix} = \tau_{7-h}$, and by line 1 $\sigma\tau_{7-h}\sigma = \begin{pmatrix} 0 & -\mathrm{t4}[h] \\ \mathrm{t4}[h] & 0 \end{pmatrix} = -\tau_{7-h}$; for $A = 7$: $\tau_7$ is symmetric and by line 1 $\sigma\tau_7\sigma = \mathrm{diag}(I_4, -I_4) = -\tau_7$.

Lines 2, 3, 4 and 8 together say that the seven matrices $\tau_1, \dots, \tau_7$ satisfy a Clifford relation of their own: $\tau_A\tau_B + \tau_B\tau_A = -2\,\mathrm{eta4488}_{AB}\, I_8$ for $A, B = 1, \dots, 7$ ($\tau_1, \tau_2, \tau_3$ square to $-I_8$, $\tau_4, \dots, \tau_7$ to $+I_8$). With line 10 this gives the **key rule** for all 64 pairs $A, B = 0, \dots, 7$:

$$
\tau_A\bar\tau_B + \tau_B\bar\tau_A = \bar\tau_A\tau_B + \bar\tau_B\tau_A = 2\,\mathrm{eta4488}_{AB}\, I_8 .
$$

Proof: for $A, B \geq 1$ both sides equal $-(\tau_A\tau_B + \tau_B\tau_A)$ by line 10, which is $2\,\mathrm{eta4488}_{AB} I_8$; for $A = 0$ and $B \geq 1$ the left side is $\bar\tau_B + \tau_B = 0 = 2\,\mathrm{eta4488}_{0B} I_8$; for $A = B = 0$ it is $2 I_8$.

**Step 3: the $16 \times 16$ matrices.** The author puts $\bar\tau_A$ into the upper-right and $\tau_A$ into the lower-left $8 \times 8$ corner (In[371]) and multiplies the first eight (In[372]):

$$
\mathrm{T16}[A] = \begin{pmatrix} 0 & \bar\tau_A \\ \tau_A & 0 \end{pmatrix} \quad (A = 0, \dots, 7), \qquad \mathrm{T16}[8] = \mathrm{T16}[0]\,\mathrm{T16}[1] \cdots \mathrm{T16}[7] .
$$

By the block rule, T16[$A$] T16[$B$] $= \mathrm{diag}(\bar\tau_A\tau_B, \tau_A\bar\tau_B)$. Adding the same with $A$ and $B$ exchanged and using the key rule:

$$
\mathrm{T16}[A]\,\mathrm{T16}[B] + \mathrm{T16}[B]\,\mathrm{T16}[A] = \mathrm{diag}(\bar\tau_A\tau_B + \bar\tau_B\tau_A,\ \tau_A\bar\tau_B + \tau_B\bar\tau_A) = 2\,\mathrm{eta4488}_{AB}\, I_{16} .
$$

This is the Clifford relation in the author's frame order. The product T16[8] is block diagonal (eight block off-diagonal factors). Its upper-left block is $\bar\tau_0\tau_1\,\bar\tau_2\tau_3\,\bar\tau_4\tau_5\,\bar\tau_6\tau_7 = \tau_1(-\tau_2)\tau_3(-\tau_4)\tau_5(-\tau_6)\tau_7 = -\tau_1\cdots\tau_7 = -I_8$ (pairs of factors multiplied with the block rule, line 10, line 9), and its lower-right block is $\tau_0\bar\tau_1\,\tau_2\bar\tau_3\,\tau_4\bar\tau_5\,\tau_6\bar\tau_7 = (+1)\tau_1\cdots\tau_7 = I_8$ (four minus signs). So T16[8] $= \mathrm{diag}(-I_8, I_8)$, and T16[0] T16[1] $\cdots$ T16[8] $=$ T16[8]$^2 = I_{16}$. Chapter 5 calls this product the **chirality**; here it is only a product.

**Step 4: the author's coordinates.** With the map of Section 4.4, $\gamma^{(x_k)} = $ T16[$k$] for $k = 1, \dots, 7$ and $\gamma^{(x_8)} = $ T16[0], and the signs become $\eta = \mathrm{diag}(+1, +1, +1, -1, -1, -1, -1, +1)$. Renaming does not change a matrix, so

$$
\gamma^{a}\gamma^{b} + \gamma^{b}\gamma^{a} = 2\eta^{ab} I_{16} \qquad (a, b = x_1, \dots, x_8).
$$

Three more properties follow. (i) **Reality**: every entry is $-1$, 0 or $+1$, because the building blocks have only such entries and the construction only places blocks and changes signs (the products $\tau_7$ and $\bar\tau_A$ are products of signed permutation matrices, which are again signed permutation matrices). (ii) Every $\gamma^a$ is a **signed permutation matrix**, hence orthogonal: $(\gamma^a)^T = (\gamma^a)^{-1}$. (iii) The **symmetry pattern** $(\gamma^a)^T = \eta_{aa}\gamma^a$: symmetric for the space-like $x_1, x_2, x_3, x_8$, antisymmetric for the time-like $x_4, \dots, x_7$. Proof of (iii), line by line: $(\gamma^a)^2 = \eta_{aa} I_{16}$ (Clifford relation with $b = a$); multiplying by $\eta_{aa}$ and using $\eta_{aa}^2 = 1$ gives $\gamma^a(\eta_{aa}\gamma^a) = I_{16}$, so $(\gamma^a)^{-1} = \eta_{aa}\gamma^a$; with (ii), $(\gamma^a)^T = (\gamma^a)^{-1} = \eta_{aa}\gamma^a$.

**Status.** PROVED (by hand above, and exactly by the computer in two independent Revision programs): the six blocks are those the author displays (`Revision/algebra/reports/python-algebra.json`, check `notebook_blocks_s4_t4`; `Revision/algebra/reports/wolfram-algebra.json`, check `s4_t4_entries_from_Signature_and_deltas`); their rules (checks `s4_t4_quaternion_algebras`, `s4_self_dual_t4_anti_self_dual`, `blocks_antisymmetric_square_minus_one_commute`); the rules of $\sigma$ and $\tau$ (checks `sigma8_involution`, `tau7_and_sigma_identities`, `tau7_and_product`, `taubar_relations`, `notebook_tau_clifford`); the key rule (checks `tau_taubar_Clifford_relation`, `notebook_tau_taubar_clifford`); the block form and T16[8] (checks `T16_block_form`, `Gamma_diag`, `chirality_diag`, `notebook_product_identity`); the Clifford relation for all 64 pairs (checks `Clifford_relation`, `clifford_relation`, `clifford_relation_sympy`); reality, signed permutations and the symmetry pattern (checks `reality`, `signed_permutation_matrices`, `reality_signed_permutations`, `symmetry_pattern`). Notebook 04a reproduces 30 of these Revision checks (16 of the WolframScript report and 14 of the Python report) and compares all $8 \times 256 = 2048$ entries with both Revision files: none differs.

The next three sections hold Notebook 04a: how to run it, its complete text, and the line-by-line walk-through.

<!-- NOTEBOOK 04a -->

### 4.8 Line-by-line walk-through of Notebook 04a

The notebook has 28 code cells, In [1] to In [28]. This section explains every line of every one of them, in order. Docstrings (the texts in triple quotes right below a `def` line, which say what a function does) are left out of the quotations; they are printed in full in Section 4.7.

**In [1], the set-up cell.** Its first part is the complete run instructions of Section 4.6 again, as **comment lines**: every line that starts with `#` is a comment, which Python skips; they are there so that the notebook file carries its own instructions. The code starts after the second line of `=` signs. This set-up cell is the same in every notebook of the book, except for the line that names the notebook.

```python
import json  # reads and writes JSON files (text files that hold names and numbers)
import os  # reads the environment variable TEXTBOOK_OUTPUT_ROOT (explained below)
import textwrap  # breaks long printed text into lines of at most 89 characters
from pathlib import Path  # file and folder paths that work on Windows, macOS and Linux

import matplotlib  # the plotting package
import matplotlib.pyplot as plt  # its drawing functions, called plt by convention
from IPython.display import Image, display  # shows a saved picture below a cell
```

`import` loads a **module** (a part of Python or of an installed package) so that the code can use it. `json`, `os`, `textwrap` and `pathlib` come with Python; `from pathlib import Path` takes only the name `Path` out of `pathlib`. A `Path` is the address of a file or folder, written the same way on every operating system. The plotting package matplotlib is loaded, its drawing functions under the short name `plt`, and from IPython (the part of Jupyter that runs Python code) the two functions `Image` and `display`, which show a picture file below a cell.

```python
NOTEBOOK_ID = "04a"  # this notebook: chapter 04, example a
```

A **variable** is a name for a value; this line gives the name `NOTEBOOK_ID` to the **string** (a text in quotes) `"04a"`. The figure files and the last printed line use it.

```python
def find_repository_root():
    here = Path.cwd().resolve()  # the folder in which this notebook runs
    for folder in [here, *here.parents]:  # this folder, its parent, its grandparent ...
        if (folder / "Revision" / "textbook" / "requirements.txt").is_file():
            return folder
    raise FileNotFoundError(
        "The repository folder was not found: open this notebook inside the folder "
        "Revision/textbook/notebooks of the repository Dirac_claude")
```

`def` defines a **function**, a named piece of code that runs when it is called. `Path.cwd()` is the folder in which the notebook runs, and `.resolve()` writes it as a complete address. `here.parents` lists its parent folder, the parent of that, and so on; `[here, *here.parents]` is the list that starts with `here` and continues with all of them (the star unpacks the parents into the list). The `for` loop takes the folders one after the other; the operator `/` joins a folder and a name into a longer path, and `.is_file()` is true when that file exists. The first folder that contains `Revision/textbook/requirements.txt` is the repository, and `return` hands it back. If none qualifies, `raise` stops the notebook with a `FileNotFoundError` whose message says what to do.

```python
REPO = find_repository_root()
OUTPUT_ROOT = Path(os.environ.get("TEXTBOOK_OUTPUT_ROOT", str(REPO)))
```

The first line calls the function and names the result `REPO`. It is never printed, because it differs from computer to computer while the printed output must not. The second line chooses the folder below which files are written: `os.environ` holds the **environment variables** of the running program (named texts it receives from the computer), and `.get(name, default)` returns the value of `TEXTBOOK_OUTPUT_ROOT` if it is set and otherwise the default, the repository folder as a string. When you run the notebook the variable is not set, so the files go into the repository; the book's checking tool sets it to a scratch folder.

```python
def repository_file(relative):
    return REPO / relative


def output_file(relative):
    path = OUTPUT_ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    return path
```

`repository_file("Revision/...")` gives the full path of a repository file, for reading a Revision record. `output_file("Revision/...")` gives the full path at which to write a file; `path.parent.mkdir(parents=True, exist_ok=True)` first creates the folder that will hold it (and any missing folder above it) and does nothing if it exists.

```python
def say(text):
    print(textwrap.fill(str(text), width=89, subsequent_indent="    "))
```

`say` prints a text in lines of at most 89 characters (the width of a page of the book); `textwrap.fill` breaks the text at blanks, and every continuation line starts with four blanks. `str(text)` turns any value into a string first.

```python
matplotlib.rcdefaults()  # ignore personal matplotlib settings: same figures everywhere
plt.rcParams.update({"figure.figsize": (7.0, 4.2), "font.size": 10.0,
                     "axes.grid": True, "grid.alpha": 0.3})
```

`matplotlib.rcdefaults()` returns to the built-in settings of matplotlib, so that personal settings on your computer cannot change the figures. `plt.rcParams.update({...})` then sets four settings for every figure: 7.0 by 4.2 inches, letters of 10 points, and a faint grid (30 per cent opaque) behind the curves. The braces `{...}` make a **dictionary**, a collection of pairs `key: value`.

```python
FIGURE_FOLDER = "Revision/textbook/figures"  # where the figures are saved
CAPTION_FILE = f"{FIGURE_FOLDER}/{NOTEBOOK_ID}.captions.json"  # their captions
FIGURE_NUMBERS = {}  # figure name -> its number k (file name <id>_<k>_<name>.png)
CAPTIONS = {}  # figure file name -> caption, written to CAPTION_FILE after every figure
output_file(CAPTION_FILE).write_text("{}\n", encoding="utf-8", newline="\n")
```

A string that starts with `f` is an **f-string**: every name in braces is replaced by its value, so `CAPTION_FILE` is `"Revision/textbook/figures/04a.captions.json"`. `FIGURE_NUMBERS` and `CAPTIONS` start as empty dictionaries. The last line writes the text `{}` (an empty JSON dictionary) and a line end into the captions file; `encoding="utf-8"` fixes how letters are stored and `newline="\n"` writes the same line end on every operating system.

```python
def save_figure(fig, name, caption):
    number = FIGURE_NUMBERS.setdefault(name, len(FIGURE_NUMBERS) + 1)
    file_name = f"{NOTEBOOK_ID}_{number}_{name}.png"
    relative = f"{FIGURE_FOLDER}/{file_name}"
    fig.savefig(output_file(relative), dpi=150, bbox_inches="tight",
                metadata={"Software": None})
    plt.close(fig)  # forget the figure, so that Jupyter does not draw it a second time
    CAPTIONS[file_name] = caption
    output_file(CAPTION_FILE).write_text(
        json.dumps(CAPTIONS, indent=1, sort_keys=True) + "\n", encoding="utf-8",
        newline="\n")
    display(Image(filename=str(output_file(relative))),
            metadata={"textbook_figure": file_name})  # the saved picture itself
    say(f"Figure {NOTEBOOK_ID}.{number} saved as {relative}")
```

`save_figure` (shown without its docstring and three comment lines) saves and shows a figure. `setdefault(name, value)` returns the number already stored for this figure name or stores and returns one more than the number of figures so far; so the figures are numbered 1, 2, 3, and a cell run twice keeps its number. `fig.savefig` writes the PNG file with 150 dots per inch, cuts away the empty margin (`bbox_inches="tight"`) and stores no program name (`metadata={"Software": None}`), so that two runs write the same bytes. `plt.close(fig)` removes the figure from memory, because Jupyter would otherwise draw it a second time. The caption is stored, the whole dictionary of captions is written to the captions file (`json.dumps` turns it into JSON text, one entry per line, keys sorted), `display(Image(...))` shows the saved picture, and the last line prints where it was saved.

```python
PASSED = []  # the names of the checks that passed, in order


def check(condition, name, record=None):
    if not condition:
        raise AssertionError(f"check failed: {name}")
    PASSED.append(name)
    say(f"PASS {name}")
    if record is not None:
        say(f"     reproduces {record}")
```

`PASSED` is an empty **list** (an ordered collection in square brackets). `check` is behind every check of the book. `condition` is either `True` or `False`; if it is false, `raise AssertionError(...)` stops the notebook with an error naming the check. Otherwise the name is appended to `PASSED` and `PASS name` is printed. `record=None` makes the third argument optional; when given, a second line names the Revision record that the check reproduces.

```python
def report(label, value, unit=""):
    say(f"RESULT {label} = {value}" + (f" {unit}" if unit else ""))


def all_checks_passed():
    print(f"ALL {len(PASSED)} CHECKS PASSED (notebook {NOTEBOOK_ID})")


say(f"Set-up of notebook {NOTEBOOK_ID} complete: repository folder found, helpers "
    "defined.")
```

`report` prints a key number as a line that starts with RESULT; the expression `(f" {unit}" if unit else "")` adds a blank and the unit only when a unit is given. `all_checks_passed` prints the last line of the notebook with `len(PASSED)`, the number of checks that passed. The last statement prints the only output of In [1].

**In [2], the small tools.**

```python
import itertools  # loops over all pairs (or triples, ...) of indices
from fractions import Fraction  # exact fractions such as 1/2

import numpy as np  # integer matrices; their products are exact (no rounding)
import sympy as sp  # a second, independent engine for exact matrix algebra
from matplotlib.colors import BoundaryNorm, ListedColormap
from matplotlib.patches import Patch, Rectangle
```

`itertools` makes all pairs, triples or lists of indices; `Fraction` (used in In [26]) holds exact fractions. numpy, under the short name `np`, stores matrices as arrays; all matrices of this notebook hold whole numbers (numpy's type `int64`), whose sums and products are exact, so every check is exact. sympy, as `sp`, is a second program for exact algebra, used in In [21] as an independent judge. `BoundaryNorm` and `ListedColormap` make the three-colour heat maps; `Patch` draws the coloured squares of a legend and `Rectangle` a frame.

```python
def signature(numbers):
    if len(set(numbers)) != len(numbers):  # a set keeps each number only once
        return 0
    inversions = sum(1 for i, j in itertools.combinations(range(len(numbers)), 2)
                     if numbers[i] > numbers[j])
    return -1 if inversions % 2 else 1  # % 2 is the remainder after division by 2
```

The permutation sign of Section 4.2. `set(numbers)` keeps each number once, so if it is shorter than the list a number is repeated and the sign is 0. `itertools.combinations(range(len(numbers)), 2)` lists every pair of positions $i < j$; the expression `sum(1 for ... if numbers[i] > numbers[j])` adds 1 for every pair in which the larger number stands first, that is it counts the inversions. `inversions % 2` is 1 for an odd and 0 for an even count, and Python reads 1 as true and 0 as false, so the function returns $-1$ for an odd and $+1$ for an even number of inversions.

```python
def delta(i, j):
    return 1 if i == j else 0


def anticommutator(a, b):
    return a @ b + b @ a


def identity(n):
    return np.eye(n, dtype=np.int64)


def zeros(n):
    return np.zeros((n, n), dtype=np.int64)
```

Four one-line functions: the Kronecker delta ($1$ if $i = j$, else 0; `==` tests equality); the anticommutator $\{a, b\} = ab + ba$, with `@` the matrix product; the $n \times n$ identity matrix with whole-number entries (`np.eye`); and the $n \times n$ zero matrix.

```python
for numbers in ([1, 2, 3, 4], [2, 1, 3, 4], [2, 3, 1, 4], [1, 1, 3, 4]):
    say(f"the sign of {numbers} is {signature(numbers)}")
check(signature([1, 2, 3, 4]) == 1 and signature([2, 1, 3, 4]) == -1
      and signature([2, 3, 1, 4]) == 1 and signature([1, 1, 3, 4]) == 0,
      "the permutation sign agrees with the four examples worked out by hand")
```

The loop prints the sign of the four example lists of Section 4.2, and the check requires the values $+1$, $-1$, $+1$ and 0 found there by hand. `and` is true only when both sides are true. Output: four lines and the first PASS line.

**In [3], the Revision reports.**

```python
WOLFRAM = "Revision/algebra/reports/wolfram-algebra.json"  # WolframScript report
PYTHON = "Revision/algebra/reports/python-algebra.json"  # Python report
RECORDED = {}  # report file -> {check name: the check (name, verdict, detail)}
for report_file in (WOLFRAM, PYTHON):
    text = repository_file(report_file).read_text(encoding="utf-8")
    RECORDED[report_file] = {entry["name"]: entry
                             for entry in json.loads(text)["checks"]}
    say(f"{report_file}: {len(RECORDED[report_file])} checks recorded")
REPRODUCED = set()  # the (report, check) pairs that this notebook reproduces
```

The two report files of the Revision record are named. For each, `read_text` reads the file and `json.loads` turns the JSON text into Python lists and dictionaries; the report holds a list `"checks"` of entries, each with a `"name"`, a `"verdict"` and a `"detail"`. The **dictionary comprehension** `{entry["name"]: entry for entry in ...}` makes a dictionary from check names to entries. The cell prints how many checks each report holds: 45 and 35. `REPRODUCED` starts as an empty **set** (a collection without repetitions).

```python
def check_record(condition, name, *records):
    for report_file, check_name in records:
        entry = RECORDED[report_file].get(check_name)
        if entry is None or entry["verdict"].upper() != "PASS":
            raise AssertionError(f"{report_file} has no passed check {check_name}")
    check(condition, name)
    for report_file, check_name in records:
        print(f"     reproduces {report_file}")
        print(f"         check {check_name}")
        REPRODUCED.add((report_file, check_name))
```

`check_record` is `check` for a statement that the Revision record also verified. `*records` collects any number of further arguments, each a pair (report file, check name). The first loop looks each check up (`.get` returns `None` for a missing name) and stops with an error if it is missing or not recorded as passed; `.upper()` makes the comparison work for both spellings, PASS in the WolframScript report and pass in the Python report. Then `check` tests the notebook's own condition and prints the PASS line, and the second loop prints, for each Revision check, the file and the check name and adds the pair to `REPRODUCED`.

**In [4], the drawing tools.**

```python
# Three colours: entry -1 blue, entry 0 light grey, entry +1 red.
SIGN_COLOURS = ListedColormap(["#2a78d6", "#f0efec", "#e34948"])
# The boundaries -1.5, -0.5, 0.5, 1.5 put -1, 0 and +1 into the three colours.
SIGN_NORM = BoundaryNorm([-1.5, -0.5, 0.5, 1.5], SIGN_COLOURS.N)
```

A colour such as `"#2a78d6"` is written as three two-digit hexadecimal numbers (base 16) for the amounts of red, green and blue. `ListedColormap` makes a list of three colours; `BoundaryNorm` with the boundaries $-1.5, -0.5, 0.5, 1.5$ assigns every value between two neighbouring boundaries to one colour, so $-1$ is blue, 0 light grey and $+1$ red. `SIGN_COLOURS.N` is the number of colours, 3.

```python
def draw_signs(ax, matrix, title, numbers=False, first=0):
    size = matrix.shape[0]
    ax.imshow(matrix, cmap=SIGN_COLOURS, norm=SIGN_NORM)
    ax.set_title(title, fontsize=10)
    step = 1 if size <= 8 else 4  # label every row (small) or every 4th (large)
    ticks = list(range(0, size, step))
    ax.set_xticks(ticks, [str(t + first) for t in ticks], fontsize=7)
    ax.set_yticks(ticks, [str(t + first) for t in ticks], fontsize=7)
    ax.grid(False)  # no grid lines on top of the coloured squares
    if numbers:
        for (row, column), value in np.ndenumerate(matrix):
            if value:
                ax.text(column, row, f"{value:+d}", ha="center", va="center",
                        color="white", fontsize=8)
```

`draw_signs` draws one matrix into one **panel** `ax` (a pair of axes) of a figure. `matrix.shape[0]` is its number of rows. `ax.imshow` paints every entry as a small coloured square, row 0 at the top. The axis labels mark every row of a small matrix and every fourth row of a large one; `range(0, size, step)` counts from 0 in steps of `step`, and `t + first` shifts the labels to start at 1 for the author's $4 \times 4$ blocks. With `numbers=True`, `np.ndenumerate` runs through all entries with their positions, and every nonzero entry is written into its square in white, with its sign (`{value:+d}` writes $+1$ or $-1$); `ha` and `va` centre the text.

```python
def sign_legend(fig):
    handles = [Patch(facecolor=SIGN_COLOURS(k), edgecolor="#898781", label=label)
               for k, label in enumerate(["entry -1", "entry 0", "entry +1"])]
    fig.legend(handles=handles, loc="outside lower center", ncol=3, fontsize=9,
               frameon=False)
```

`sign_legend` adds the key of the three colours below the panels. `enumerate` numbers the three labels 0, 1, 2; `SIGN_COLOURS(k)` is colour number `k`; each `Patch` is a small coloured square with its label, and `fig.legend` places the three in one row (`ncol=3`) below the figure, without a frame.

**In [5], the six blocks.**

```python
def Qa(h, p, q):
    return signature([h, p, q, 4])


def Qb(h, p, q):
    return delta(p, 4) * delta(q, h) - delta(p, h) * delta(q, 4)
```

The author's two patterns of Section 4.5, letter for letter: $Q_a[h]_{pq} = \mathrm{Signature}[\{h, p, q, 4\}]$ and $Q_b[h]_{pq} = \delta_{p4}\delta_{qh} - \delta_{ph}\delta_{q4}$, with $h, p, q$ counted from 1; `*` multiplies numbers.

```python
s4 = {h: np.array([[Qa(h, p, q) - Qb(h, p, q) for q in range(1, 5)]
                   for p in range(1, 5)]) for h in (1, 2, 3)}
t4 = {h: np.array([[Qa(h, p, q) + Qb(h, p, q) for q in range(1, 5)]
                   for p in range(1, 5)]) for h in (1, 2, 3)}
```

`range(1, 5)` is 1, 2, 3, 4. The inner **list comprehension** `[... for q in range(1, 5)]` makes one row (the four columns $q$), the outer one the four rows $p$, and `np.array` turns the list of rows into a matrix. Row $p$ of the formula becomes row $p - 1$ of the array, because numpy counts from 0. The dictionaries `s4` and `t4` hold the three blocks under the keys 1, 2, 3.

```python
def side_by_side(matrices, labels):
    # ^11: centred in 11 characters; rstrip() removes the blanks at the end
    print("   ".join(f"{label:^11}" for label in labels).rstrip())
    for row in range(matrices[0].shape[0]):
        print("   ".join(" ".join(f"{x:2d}" for x in m[row]) for m in matrices))


side_by_side([s4[1], s4[2], s4[3]], ["s4[1]", "s4[2]", "s4[3]"])
print()
side_by_side([t4[1], t4[2], t4[3]], ["t4[1]", "t4[2]", "t4[3]"])
```

`side_by_side` prints several matrices next to each other. `"   ".join(...)` glues texts together with three blanks between them; `{label:^11}` centres a title in 11 characters. For each row number, the inner `" ".join(f"{x:2d}" ...)` writes the entries of that row of one matrix, each two characters wide, and the outer join puts the rows of the three matrices next to each other. The output shows the six blocks, exactly the matrices of Section 4.5; `print()` prints the empty line between the two groups.

**In [6], comparison with the author's display.**

```python
DISPLAYED_S4 = {  # Out[304] of the author's notebook: s4by4[1], s4by4[2], s4by4[3]
    1: [[0, 0, 0, 1], [0, 0, 1, 0], [0, -1, 0, 0], [-1, 0, 0, 0]],
    2: [[0, 0, -1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, -1, 0, 0]],
    3: [[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0]],
}
DISPLAYED_T4 = {  # Out[304]: t4by4[1], t4by4[2], t4by4[3]
    1: [[0, 0, 0, -1], [0, 0, 1, 0], [0, -1, 0, 0], [1, 0, 0, 0]],
    2: [[0, 0, -1, 0], [0, 0, 0, -1], [1, 0, 0, 0], [0, 1, 0, 0]],
    3: [[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]],
}
```

The six matrices that the author's notebook displays in its output Out[304], typed in row by row (the Revision Python checker types in the same six).

```python
# .all() is True when the comparison holds for every entry.
same = all((s4[h] == np.array(DISPLAYED_S4[h])).all()
           and (t4[h] == np.array(DISPLAYED_T4[h])).all() for h in (1, 2, 3))
check_record(same, "the formulas give the six blocks that the author displays",
             (PYTHON, "notebook_blocks_s4_t4"),
             (WOLFRAM, "s4_t4_entries_from_Signature_and_deltas"))
```

Comparing two numpy arrays with `==` gives an array of `True`/`False`, one per entry; `.all()` is true when every entry agrees. `all(... for h in (1, 2, 3))` requires it for the three values of $h$. The check prints PASS and names the two Revision checks it reproduces.

**In [7], figure 1.**

```python
fig, axes = plt.subplots(2, 3, figsize=(7.4, 5.6), layout="constrained")
for h in (1, 2, 3):
    draw_signs(axes[0, h - 1], s4[h], f"s4[{h}]", numbers=True, first=1)
    draw_signs(axes[1, h - 1], t4[h], f"t4[{h}]", numbers=True, first=1)
sign_legend(fig)
save_figure(fig, "blocks_s4_t4", ...)
```

(The caption string is shortened to `...` here; it is printed in full in Section 4.7, and Python joins the strings written next to each other into one.) `plt.subplots(2, 3, ...)` makes a figure with two rows of three panels, 7.4 by 5.6 inches; `layout="constrained"` spaces the panels so that nothing overlaps. `axes[0, h - 1]` is the panel in row 0 and column $h - 1$. The upper row shows s4[1], s4[2], s4[3], the lower row the t-blocks, each entry written into its square, rows and columns numbered 1 to 4. **What figure 1 shows and why:** every block has exactly one coloured square in each row and each column (a signed permutation), and the square in row $p$, column $q$ has the opposite colour of the square in row $q$, column $p$, because every block is antisymmetric (Section 4.5).

**In [8], the rules of the blocks.**

```python
I4 = identity(4)
blocks = [s4[1], s4[2], s4[3], t4[1], t4[2], t4[3]]
antisymmetric = all((m.T == -m).all() for m in blocks)
square_minus_one = all((m @ m == -I4).all() for m in blocks)
```

`m.T` is the transpose of `m`. `antisymmetric` is true when $m^T = -m$ for all six blocks, and `square_minus_one` when $m\,m = -I_4$ for all six.

```python
anticommute = all((anticommutator(s4[h], s4[k]) == -2 * delta(h, k) * I4).all()
                  and (anticommutator(t4[h], t4[k]) == -2 * delta(h, k) * I4).all()
                  for h in (1, 2, 3) for k in (1, 2, 3))
s_t_commute = all((s4[h] @ t4[k] == t4[k] @ s4[h]).all()
                  for h in (1, 2, 3) for k in (1, 2, 3))
```

The two `for` parts run through all nine pairs $(h, k)$. `anticommute` tests $\{\mathrm{s4}[h], \mathrm{s4}[k]\} = \{\mathrm{t4}[h], \mathrm{t4}[k]\} = -2\delta_{hk} I_4$, and `s_t_commute` tests that every s-block commutes with every t-block.

```python
check_record(antisymmetric and square_minus_one and s_t_commute,
             "the blocks are antisymmetric, square to -I4, and s4 commutes with t4",
             (PYTHON, "blocks_antisymmetric_square_minus_one_commute"))
check_record(anticommute and s_t_commute and antisymmetric,
             "{s4[h], s4[k]} = {t4[h], t4[k]} = -2 delta_hk I4, [s4[h], t4[k]] = 0",
             (WOLFRAM, "s4_t4_quaternion_algebras"))
```

Two checks, each worded as the Revision check it reproduces: the Python check combines antisymmetry, squares and commuting, the WolframScript check the anticommutators, the commuting and the antisymmetry.

**In [9], self-dual and anti-self-dual.**

```python
epsilon = np.zeros((4, 4, 4, 4), dtype=np.int64)
for p, q, r, s in itertools.product(range(4), repeat=4):  # all 4^4 = 256 lists
    epsilon[p, q, r, s] = signature([p, q, r, s])
```

`epsilon` is a table with four indices, each 0 to 3 (counting from 0 does not change a permutation sign). `itertools.product(range(4), repeat=4)` lists all $4^4 = 256$ lists $(p, q, r, s)$, and each entry is set to the permutation sign: the Levi-Civita symbol of Section 4.5.

```python
def dual(m):
    twice = np.einsum("pqrs,rs->pq", epsilon, m)  # the sum over r and s
    if (twice % 2).any():  # for an antisymmetric m every entry of twice is even
        raise ValueError("the dual is not a whole-number matrix")
    return twice // 2  # exact division by 2
```

`np.einsum("pqrs,rs->pq", epsilon, m)` computes, for every $p$ and $q$, the sum $\sum_{r,s}\epsilon_{pqrs} m_{rs}$: the letters before the arrow name the indices of the two inputs, the letters after it the indices of the result, and every letter that does not appear after the arrow is summed over. That is twice the dual. For an antisymmetric matrix every entry of it is even (the two equal terms of Section 4.5); the `if` line stops with an error otherwise, and `//` divides exactly by 2.

```python
for h in (1, 2, 3):
    say(f"h = {h}: dual(s4) == s4: {(dual(s4[h]) == s4[h]).all()},  "
        f"dual(t4) == -t4: {(dual(t4[h]) == -t4[h]).all()}")
check_record(all((dual(s4[h]) == s4[h]).all() and (dual(t4[h]) == -t4[h]).all()
                 for h in (1, 2, 3)),
             "every s4[h] is self-dual and every t4[h] anti-self-dual",
             (WOLFRAM, "s4_self_dual_t4_anti_self_dual"))
```

For each $h$ one line reports $\star\mathrm{s4}[h] = \mathrm{s4}[h]$ and $\star\mathrm{t4}[h] = -\mathrm{t4}[h]$ (three lines, all True), and the check requires both for all three.

**In [10], the quaternions.**

```python
def quaternion_product(x, y):
    x1, x2, x3, x4 = x
    y1, y2, y3, y4 = y
    return (x4 * y1 + x1 * y4 + x2 * y3 - x3 * y2,  # the i component
            x4 * y2 + x2 * y4 + x3 * y1 - x1 * y3,  # the j component
            x4 * y3 + x3 * y4 + x1 * y2 - x2 * y1,  # the k component
            x4 * y4 - x1 * y1 - x2 * y2 - x3 * y3)  # the real component
```

The product of two quaternions stored as $(q_1, q_2, q_3, q_4)$. The first two lines **unpack** the four components of each. The four returned lines come from multiplying $(x_4 + x_1\mathbf{i} + x_2\mathbf{j} + x_3\mathbf{k})(y_4 + y_1\mathbf{i} + y_2\mathbf{j} + y_3\mathbf{k})$ term by term with Hamilton's rules; for example the $\mathbf{i}$ component collects $x_4 y_1$ (from $x_4\cdot y_1\mathbf{i}$), $x_1 y_4$, $x_2 y_3$ (from $\mathbf{jk} = \mathbf{i}$) and $-x_3 y_2$ (from $\mathbf{kj} = -\mathbf{i}$), and the real component $x_4y_4 - x_1y_1 - x_2y_2 - x_3y_3$ (from $\mathbf{i}^2 = \mathbf{j}^2 = \mathbf{k}^2 = -1$).

```python
UNITS = {1: (1, 0, 0, 0), 2: (0, 1, 0, 0), 3: (0, 0, 1, 0)}  # i, j, k
BASIS = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]  # e_1, ..., e_4


def right_multiplication(u):
    return np.array([quaternion_product(e, u) for e in BASIS]).T


def left_multiplication(u):
    return np.array([quaternion_product(u, e) for e in BASIS]).T
```

`UNITS` holds $\mathbf{i}, \mathbf{j}, \mathbf{k}$ under the keys 1, 2, 3, and `BASIS` the four quaternions $e_1, \dots, e_4$. `right_multiplication(u)` lists the products $e_p u$ as the rows of an array and transposes it with `.T`, so that they become the columns: the matrix $R_u$ of Section 4.5. `left_multiplication(u)` does the same with $u e_p$: the matrix $L_u$.

```python
say(f"i j = {quaternion_product(UNITS[1], UNITS[2])} (that is k), "
    f"j i = {quaternion_product(UNITS[2], UNITS[1])} (that is -k)")
check(quaternion_product(UNITS[1], UNITS[2]) == (0, 0, 1, 0)
      and quaternion_product(UNITS[1], UNITS[1]) == (0, 0, 0, -1),
      "the quaternion product follows Hamilton's rules i j = k and i i = -1")
check(all((s4[h] == right_multiplication(UNITS[h])).all()
          and (t4[h] == -left_multiplication(UNITS[h])).all() for h in (1, 2, 3)),
      "s4[h] is right and t4[h] minus left multiplication by i, j, k")
```

The printed line shows $\mathbf{ij} = (0, 0, 1, 0) = \mathbf{k}$ and $\mathbf{ji} = (0, 0, -1, 0) = -\mathbf{k}$. The first check confirms two of Hamilton's rules; the second confirms s4[$h$] $= R_{u_h}$ and t4[$h$] $= -L_{u_h}$ for $h = 1, 2, 3$, the fact from which Section 4.5 derived every rule of the blocks.

**In [11], $\sigma$, $\tau$ and $\bar\tau$.**

```python
I8, Z4, Z8 = identity(8), zeros(4), zeros(8)
eta4488 = np.diag([1, 1, 1, 1, -1, -1, -1, -1])  # In[45]: frame order A = 0..7
sigma = np.block([[Z4, I4], [I4, Z4]])  # In[46]
```

Three matrices are named in one line ($I_8$ and the zero matrices of sizes 4 and 8). `np.diag(list)` makes the diagonal matrix with the listed diagonal: the author's eta4488. `np.block` glues blocks into a big matrix, row of blocks by row of blocks: $\sigma = \begin{pmatrix} 0 & I_4 \\ I_4 & 0 \end{pmatrix}$.

```python
tau = {0: I8}  # In[338]
for h in (1, 2, 3):
    tau[h] = np.block([[Z4, s4[h]], [s4[h], Z4]])  # tau[1], tau[2], tau[3]
    tau[7 - h] = np.block([[Z4, t4[h]], [-t4[h], Z4]])  # tau[6], tau[5], tau[4]
tau[7] = tau[1] @ tau[2] @ tau[3] @ tau[4] @ tau[5] @ tau[6]  # In[338]
taubar = {0: I8}  # In[351]
for A in range(1, 8):
    taubar[A] = sigma @ tau[A].T @ sigma
```

The dictionary `tau` starts with $\tau_0 = I_8$; the loop adds $\tau_h$ from s4[$h$] and $\tau_{7-h}$ from t4[$h$] for $h = 1, 2, 3$; $\tau_7$ is the product of the first six; and `taubar` holds $\bar\tau_0 = I_8$ and $\bar\tau_A = \sigma\tau_A^T\sigma$ for $A = 1, \dots, 7$ (`range(1, 8)` is 1 to 7). These are the formulas of Step 2 in Section 4.5.

```python
def codes(m):
    result = []
    for row in m:
        columns = np.flatnonzero(row)  # the columns of the nonzero entries
        if len(columns) != 1 or abs(row[columns[0]]) != 1:
            raise ValueError("not a signed permutation matrix")
        column = int(columns[0])
        result.append(("+" if row[column] > 0 else "-") + str(column))
    return result
```

`codes` writes a signed permutation matrix in the code notation of Section 4.2. For every row, `np.flatnonzero(row)` lists the columns of its nonzero entries; if there is not exactly one, or it is not $\pm 1$, the function stops with an error (so `codes` also checks that the matrix is a signed permutation matrix). Otherwise it appends the sign and the column number, for example `"+5"`.

```python
labels = [f"tau[{A}]" for A in range(1, 8)]  # the column titles
print("row " + "".join(f"{label:>8}" for label in labels))
tau_codes = {A: codes(tau[A]) for A in range(1, 8)}
for i in range(8):
    print(f"{i:3d} " + "".join(f"{tau_codes[A][i]:>8}" for A in range(1, 8)))
```

The table of codes: one title line (`{label:>8}` writes each title right-aligned in 8 characters) and one line per row $i = 0, \dots, 7$ with the code of row $i$ of each of $\tau_1, \dots, \tau_7$. In the output one reads, for example, that $\tau_7$ has the codes $-0, -1, -2, -3, +4, +5, +6, +7$: it is $\mathrm{diag}(-I_4, I_4)$, as Step 2 proved.

**In [12], figure 2.**

```python
fig, axes = plt.subplots(2, 4, figsize=(8.6, 5.0), layout="constrained")
for A in range(8):
    draw_signs(axes[A // 4, A % 4], tau[A], f"tau[{A}]")  # // and %: row, column
sign_legend(fig)
save_figure(fig, "tau_matrices", ...)
```

Two rows of four panels; matrix $A$ goes into row $A // 4$ (the whole part of $A/4$) and column $A \% 4$ (the remainder). **What figure 2 shows and why:** $\tau_0$ is the identity (red diagonal); $\tau_1$ to $\tau_6$ have their entries only in the upper-right and lower-left $4 \times 4$ corners, because they are made of the blocks s4 and t4 placed there; $\tau_7$ is diagonal with four blue and four red entries, $\mathrm{diag}(-I_4, I_4)$.

**In [13], the rules of $\sigma$ and $\tau$.**

```python
sigma_ok = (sigma.T == sigma).all() and np.trace(sigma) == 0 \
    and (sigma @ sigma == I8).all()
check_record(sigma_ok, "sigma is symmetric, traceless and squares to I8",
             (WOLFRAM, "sigma8_involution"))
```

A backslash at the end of a line continues the statement on the next line. $\sigma$ must be symmetric, have trace 0 (`np.trace`) and square to $I_8$.

```python
product_1_to_7 = I8
for A in range(1, 8):
    product_1_to_7 = product_1_to_7 @ tau[A]
check_record((tau[7] == np.diag([-1, -1, -1, -1, 1, 1, 1, 1])).all()
             and (product_1_to_7 == I8).all(),
             "tau[7] = diag(-I4, I4) and tau[1] tau[2] ... tau[7] = I8",
             (PYTHON, "tau7_and_product"))
```

The loop multiplies $\tau_1\tau_2\cdots\tau_7$ step by step, starting from $I_8$. The check requires $\tau_7 = \mathrm{diag}(-I_4, I_4)$ and $\tau_1\cdots\tau_7 = I_8$ (Step 2, lines 7 and 9).

```python
sigma_products = (sigma == tau[1] @ tau[2] @ tau[3]).all() and \
    (sigma == tau[4] @ tau[5] @ tau[6] @ tau[7]).all()
sigma_transpose = all((sigma @ taubar[A] == (sigma @ tau[A]).T).all()
                      for A in range(8))
check_record(sigma_products and sigma_transpose,
             "sigma = tau1 tau2 tau3 = tau4 ... tau7 and sigma taubar = (sigma tau)^T",
             (WOLFRAM, "tau7_and_sigma_identities"),
             (PYTHON, "notebook_sigma_eq_tau1tau2tau3"))
```

Two identities that the author's notebook states: $\sigma = \tau_1\tau_2\tau_3 = \tau_4\tau_5\tau_6\tau_7$ (Step 2, lines 5 and 9), and $\sigma\bar\tau_A = (\sigma\tau_A)^T$ for all eight $A$ (true because $(\sigma\tau_A)^T = \tau_A^T\sigma^T = \tau_A^T\sigma$, and $\sigma\bar\tau_A = \sigma\sigma\tau_A^T\sigma = \tau_A^T\sigma$ since $\sigma^2 = I_8$).

```python
check_record(sigma_transpose and all((taubar[A] == -tau[A]).all()
                                     for A in range(1, 8)),
             "taubar[A] = -tau[A] for A = 1, ..., 7",
             (PYTHON, "taubar_relations"))
check_record(all((anticommutator(tau[A], tau[B]) == -2 * eta4488[A, B] * I8).all()
                 for A in range(1, 8) for B in range(1, 8)),
             "tau[A] tau[B] + tau[B] tau[A] = -2 eta4488_AB I8 for A, B = 1..7",
             (PYTHON, "notebook_tau_clifford"))
```

$\bar\tau_A = -\tau_A$ for $A = 1, \dots, 7$ (Step 2, line 10), and the Clifford relation of the seven $\tau$ with the signs $-\mathrm{eta4488}$, for all 49 pairs; `eta4488[A, B]` is the entry in row $A$, column $B$. Five PASS lines in all.

**In [14], the key rule.**

```python
table = np.zeros((8, 8), dtype=np.int64)
multiples_of_identity = True
other_order = True
for A, B in itertools.product(range(8), repeat=2):  # all 64 pairs
    m = tau[A] @ taubar[B] + tau[B] @ taubar[A]
    table[A, B] = m[0, 0]  # the number that multiplies I8 (if it is a multiple)
    multiples_of_identity &= bool((m == table[A, B] * I8).all())
    other = taubar[A] @ tau[B] + taubar[B] @ tau[A]
    other_order &= bool((other == table[A, B] * I8).all())
```

For each of the 64 pairs the matrix $\tau_A\bar\tau_B + \tau_B\bar\tau_A$ is computed and its upper-left entry stored in `table`; if the matrix is a multiple of $I_8$, that entry is the multiple. `x &= y` means `x = x and y`: `multiples_of_identity` stays true only if every one of the 64 matrices equals its entry times $I_8$. The same is tested for the other order $\bar\tau_A\tau_B + \bar\tau_B\tau_A$. `bool(...)` turns numpy's truth value into Python's.

```python
print("A\\B" + "".join(f"{B:4d}" for B in range(8)))
for A in range(8):
    print(f"{A:3d}" + "".join(f"{table[A, B]:4d}" for B in range(8)))
check_record(multiples_of_identity and other_order and (table == 2 * eta4488).all(),
             "tau[A] taubar[B] + tau[B] taubar[A] = 2 eta4488_AB I8, both orders",
             (WOLFRAM, "tau_taubar_Clifford_relation"),
             (PYTHON, "notebook_tau_taubar_clifford"))
```

The table is printed (`"A\\B"` prints `A\B`, the backslash written twice in the code because a single one has a special meaning in strings), row $A$, column $B$: 2 on the diagonal for $A = 0, 1, 2, 3$, $-2$ for $A = 4, \dots, 7$, and 0 elsewhere. The check requires that it is twice eta4488: the key rule of Section 4.5.

**In [15], the $16 \times 16$ matrices.**

```python
T16 = {A: np.block([[Z8, taubar[A]], [tau[A], Z8]]) for A in range(8)}  # In[371]
T16[8] = T16[0]
for A in range(1, 8):
    T16[8] = T16[8] @ T16[A]  # In[372]: T16[8] = T16[0] T16[1] ... T16[7]
I16 = identity(16)
```

T16[$A$] $= \begin{pmatrix} 0 & \bar\tau_A \\ \tau_A & 0 \end{pmatrix}$ for $A = 0, \dots, 7$, then T16[8] as the product T16[0] T16[1] $\cdots$ T16[7], built up step by step, and $I_{16}$.

```python
# [:8, 8:] means rows 0 to 7 and columns 8 to 15 (the upper-right corner), etc.
block_form = all((T16[A][:8, :8] == 0).all() and (T16[A][8:, 8:] == 0).all()
                 and (T16[A][:8, 8:] == taubar[A]).all()
                 and (T16[A][8:, :8] == tau[A]).all() for A in range(8))
check_record(block_form, "T16[A] = ((0, taubar[A]), (tau[A], 0)) for A = 0, ..., 7",
             (WOLFRAM, "T16_block_form"))
```

A **slice** `[:8, 8:]` picks rows 0 to 7 and columns 8 to 15 (`:8` means up to, not including, 8; `8:` from 8 to the end). The check confirms the four corners of every T16[$A$].

```python
say(f"diagonal of T16[8]: {list(int(x) for x in np.diag(T16[8]))}")
check_record((T16[8] == np.diag([-1] * 8 + [1] * 8)).all(),
             "T16[8] = T16[0] ... T16[7] = diag(-I8, I8)",
             (WOLFRAM, "Gamma_diag"), (PYTHON, "chirality_diag"))
```

`np.diag(matrix)` extracts the diagonal of a matrix (while `np.diag(list)` builds one); the line prints the 16 diagonal entries: eight $-1$, then eight $+1$. `[-1] * 8 + [1] * 8` is the list of eight $-1$ followed by eight 1. The check confirms T16[8] $= \mathrm{diag}(-I_8, I_8)$, proved by hand in Step 3.

```python
product_0_to_8 = I16
for A in range(9):
    product_0_to_8 = product_0_to_8 @ T16[A]
check_record((product_0_to_8 == I16).all(), "T16[0] T16[1] ... T16[8] = I16",
             (WOLFRAM, "notebook_product_identity"))
```

The product of all nine matrices T16[0] to T16[8] is $I_{16}$, an identity that the author's notebook states; it is T16[8]$^2 = I_{16}$.

**In [16], figure 3.**

```python
fig, ax = plt.subplots(figsize=(5.6, 5.6), layout="constrained")
draw_signs(ax, T16[4], "T16[4], the gamma matrix of the time $x_4$")
for left, top in ((-0.5, -0.5), (7.5, -0.5), (-0.5, 7.5), (7.5, 7.5)):
    ax.add_patch(Rectangle((left, top), 8, 8, fill=False, edgecolor="#0b0b0b",
                           linewidth=1.5))  # the frame of one 8 x 8 corner
```

One panel with T16[4]. In `imshow` the centre of the square of entry $(i, j)$ lies at the point $(j, i)$, so the square of entry $(0, 0)$ starts at $-0.5$; each `Rectangle((left, top), 8, 8, fill=False, ...)` draws an unfilled black frame of $8 \times 8$ squares around one corner.

```python
labels = {(3.5, 3.5): "0", (11.5, 3.5): "taubar[4]", (3.5, 11.5): "tau[4]",
          (11.5, 11.5): "0"}
for (x, y), label in labels.items():
    ax.text(x, y, label, ha="center", va="center", fontsize=12, color="#0b0b0b",
            bbox={"facecolor": "white", "alpha": 0.85, "edgecolor": "none"})
sign_legend(fig)
save_figure(fig, "block_form_of_t16", ...)
```

The centres of the four corners get their names, each on a white, slightly transparent background (`bbox`). **What figure 3 shows and why:** the upper-left and lower-right corners are empty, because T16[4] is block off-diagonal; the upper-right corner is $\bar\tau_4$ and the lower-left $\tau_4$, with one coloured square in each row.

**In [17], the author's coordinates.**

```python
COORDINATES = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]
FRAME_INDEX = [1, 2, 3, 4, 5, 6, 7, 0]  # A of T16[A] for x1, ..., x8
ROLE = ["3-space", "3-space", "3-space", "the time", "extra time (deflating)",
        "extra time (deflating)", "extra time (deflating)", "hidden direction"]
gamma = [T16[A] for A in FRAME_INDEX]  # gamma[0] = gamma^(x1), ...
eta = np.array([eta4488[A, A] for A in FRAME_INDEX])  # signs in the order x1..x8
```

The coordinate map of Section 4.4: `FRAME_INDEX` lists, for $x_1, \dots, x_8$, the index $A$ of the author's T16[$A$]. `gamma` is the list of the eight gamma matrices in the order of the coordinates (Python counts it from 0: `gamma[0]` is $\gamma^{(x_1)}$, `gamma[7]` is $\gamma^{(x_8)}$), and `eta` the list of their signs, read off from the diagonal of eta4488 at the same indices.

```python
for a in range(8):
    kind = "space-like" if eta[a] > 0 else "time-like"
    print(f"gamma^({COORDINATES[a]}) = T16[{FRAME_INDEX[a]}]   eta = {eta[a]:+d}   "
          f"{kind:10}   {ROLE[a]}")
```

One printed line per coordinate: its matrix, its sign, its kind and its role.

```python
renamed = all(gamma[k - 1] is T16[k] for k in range(1, 8)) and gamma[7] is T16[0]
check_record(list(eta) == [1, 1, 1, -1, -1, -1, -1, 1] and renamed,
             "gamma^(xk) = T16[k], gamma^(x8) = T16[0], eta = diag(+,+,+,-,-,-,-,+)",
             (WOLFRAM, "coordinate_map"), (WOLFRAM, "eta_in_author_order"),
             (PYTHON, "coordinate_map"))
```

`is` tests that two names refer to the very same object (not only equal entries): `gamma[k - 1]` is T16[$k$] itself for $k = 1, \dots, 7$, and `gamma[7]` is T16[0]. The check requires these and $\eta = \mathrm{diag}(+1, +1, +1, -1, -1, -1, -1, +1)$, reproducing three Revision checks.

**In [18], the eight gammas in code notation.**

```python
gamma_codes = [codes(g) for g in gamma]
print("row" + "".join(f"{name:>6}" for name in COORDINATES))
for i in range(16):
    print(f"{i:3d}" + "".join(f"{gamma_codes[a][i]:>6}" for a in range(8)))
```

`codes` (which also confirms that each is a signed permutation matrix) is applied to all eight gammas, and the table prints, for each row $i = 0, \dots, 15$, the code of row $i$ of each gamma. This table is the complete content of the eight matrices: for example the column x4 starts with $-13$, so $(\gamma^{(x_4)}u)_0 = -u_{13}$, and the column x8 reads $+8, +9, \dots, +15, +0, \dots, +7$: $\gamma^{(x_8)}$ exchanges the upper and the lower eight components. Every code of rows 0 to 7 is a column 8 to 15 and vice versa: the block form.

**In [19], figure 4.**

```python
fig, axes = plt.subplots(2, 4, figsize=(8.8, 5.0), layout="constrained")
for a in range(8):
    draw_signs(axes[a // 4, a % 4], gamma[a], f"$\\gamma^{{(x_{a + 1})}}$")
sign_legend(fig)
save_figure(fig, "gammas_x1_to_x8", ...)
```

The eight gammas in two rows of four panels. In the f-string title, the doubled braces `{{` and `}}` print single braces and the doubled backslash prints one, so the title becomes the mathematical text $\gamma^{(x_1)}$, ..., $\gamma^{(x_8)}$. **What figure 4 shows and why:** each matrix has exactly one coloured square in every row and every column, all in the upper-right and lower-left $8 \times 8$ corners (signed permutations in block form); $\gamma^{(x_8)}$ consists of two red diagonal lines, because it is T16[0] $= \begin{pmatrix} 0 & I_8 \\ I_8 & 0 \end{pmatrix}$. These are the author's eight real $16 \times 16$ gamma matrices themselves.

**In [20], the Clifford relation for all 64 pairs.**

```python
c = np.zeros((8, 8), dtype=np.int64)  # {gamma^a, gamma^b} = c[a, b] I16
all_multiples = True
for a, b in itertools.product(range(8), repeat=2):
    m = anticommutator(gamma[a], gamma[b])
    c[a, b] = m[0, 0]
    all_multiples &= bool((m == c[a, b] * I16).all())
```

As in In [14], now for the gammas: for all 64 ordered pairs $(a, b)$ the anticommutator is computed, its upper-left entry stored as $c_{ab}$, and `all_multiples` stays true only if each anticommutator is exactly $c_{ab} I_{16}$.

```python
print("a\\b" + "".join(f"{name:>5}" for name in COORDINATES))
for a in range(8):
    print(f"{COORDINATES[a]:>3}" + "".join(f"{c[a, b]:5d}" for b in range(8)))
squares = ", ".join(f"{COORDINATES[a]}:{c[a, a] // 2}" for a in range(8))
say(f"squares (gamma^a)^2 / I16: {squares}")
```

The table of the $c_{ab}$ is printed; the string `squares` lists, for each coordinate, $c_{aa}/2$, the number in $(\gamma^a)^2 = (c_{aa}/2) I_{16}$, in the form `x1:1, x2:1, ...`.

```python
recorded = RECORDED[WOLFRAM]["Clifford_relation"]["detail"]
check_record(all_multiples and (c == 2 * np.diag(eta)).all() and squares in recorded,
             "{gamma^a, gamma^b} = 2 eta^ab I16 for all 64 pairs a, b",
             (WOLFRAM, "Clifford_relation"), (PYTHON, "clifford_relation"))
```

`recorded` is the detail text of the WolframScript check `Clifford_relation`. The check requires every anticommutator to be a multiple of $I_{16}$, the table to be $2\eta$, and the text `squares` to appear word for word in the Revision detail (`in` tests whether one string is part of another). The output shows the table: 2 on the diagonal for $x_1, x_2, x_3, x_8$, $-2$ for $x_4, \dots, x_7$, 0 elsewhere.

**In [21], the same with sympy.**

```python
sympy_gamma = [sp.Matrix(g.tolist()) for g in gamma]  # the same entries, in sympy
sympy_ok = all(
    sympy_gamma[a] * sympy_gamma[b] + sympy_gamma[b] * sympy_gamma[a]
    == 2 * int(eta[a] * delta(a, b)) * sp.eye(16)
    for a in range(8) for b in range(a, 8))
check_record(sympy_ok, "sympy confirms the 36 relations {gamma^a, gamma^b} = 2 eta^ab",
             (PYTHON, "clifford_relation_sympy"))
```

`g.tolist()` turns a numpy array into a list of rows, and `sp.Matrix` makes a sympy matrix of it; in sympy `*` is the matrix product and `sp.eye(16)` the identity. `range(a, 8)` makes $b$ run from $a$ to 7, so the 36 pairs with $a \le b$ are tested (the others follow, because $\{\gamma^a, \gamma^b\} = \{\gamma^b, \gamma^a\}$). $2\eta^{ab}$ is written as $2\,\eta_{aa}\delta_{ab}$, since $\eta$ is diagonal.

**In [22], one relation followed by hand.**

```python
def follow(m, row):
    column = int(np.flatnonzero(m[row])[0])
    return int(m[row, column]), column


def signed(sign, letter, index):
    return ("+" if sign > 0 else "-") + letter + "_" + str(index)
```

`follow(m, row)` reads one row of a signed permutation matrix the way a student reads the code table: it returns the sign and the column of the single nonzero entry, so that $(mu)_{\text{row}} = \text{sign}\cdot u_{\text{column}}$. `signed` writes such a term as a text, for example `-u_13`.

```python
g4, g8 = gamma[3], gamma[7]  # gamma^(x4) and gamma^(x8)
s1, c1 = follow(g4, 0)  # row 0 of gamma^(x4)
s2, c2 = follow(g4, c1)  # row c1 of gamma^(x4)
say(f"row 0 of gamma^(x4):  (gamma^(x4) v)_0 = {signed(s1, "v", c1)}")
say(f"row {c1} of gamma^(x4): (gamma^(x4) u)_{c1} = {signed(s2, "u", c2)}")
say(f"with v = gamma^(x4) u: (gamma^(x4) gamma^(x4) u)_0 = {signed(s1 * s2, "u", c2)}")
```

Row 0 of $\gamma^{(x_4)}$ gives $(\gamma^{(x_4)}v)_0 = -v_{13}$; row 13 gives $(\gamma^{(x_4)}u)_{13} = +u_0$. With $v = \gamma^{(x_4)}u$: $(\gamma^{(x_4)}\gamma^{(x_4)}u)_0 = -v_{13} = -u_0$, row 0 of $(\gamma^{(x_4)})^2 = -I_{16}$. (The f-strings contain double quotes inside their braces, such as `signed(s1, "v", c1)`; Python allows this from version 3.12 on, one reason why the book needs Python 3.12 or newer.)

```python
t1, d1 = follow(g8, 0)  # row 0 of gamma^(x8) gamma^(x4): first gamma^(x8) ...
t2, d2 = follow(g4, d1)  # ... then row d1 of gamma^(x4)
r1, e1 = follow(g4, 0)  # row 0 of gamma^(x4) gamma^(x8): first gamma^(x4) ...
r2, e2 = follow(g8, e1)  # ... then row e1 of gamma^(x8)
say(f"(gamma^(x8) gamma^(x4) u)_0 = {signed(t1 * t2, "u", d2)};  "
    f"(gamma^(x4) gamma^(x8) u)_0 = {signed(r1 * r2, "u", e2)}")
check(s1 * s2 == -1 and c2 == 0, "by hand: row 0 of (gamma^(x4))^2 is -u_0")
check(d2 == e2 and t1 * t2 == -(r1 * r2),
      "by hand: row 0 of gamma^(x8) gamma^(x4) is minus that of gamma^(x4) gamma^(x8)")
```

The same for the two orders of $\gamma^{(x_8)}$ and $\gamma^{(x_4)}$: row 0 of $\gamma^{(x_8)}$ points to component 8, and row 8 of $\gamma^{(x_4)}$ to $+u_5$, so $(\gamma^{(x_8)}\gamma^{(x_4)}u)_0 = +u_5$; row 0 of $\gamma^{(x_4)}$ points to $-$component 13, and row 13 of $\gamma^{(x_8)}$ to $+u_5$, so $(\gamma^{(x_4)}\gamma^{(x_8)}u)_0 = -u_5$. The two checks require the hand results: $-u_0$, and the same component with opposite signs.

**In [23], figure 5.**

```python
fig, ax = plt.subplots(figsize=(5.4, 4.9), layout="constrained")
colours = ListedColormap(["#2a78d6", "#f0efec", "#e34948"])  # -2, 0, +2
ax.imshow(c, cmap=colours, norm=BoundaryNorm([-3, -1, 1, 3], 3))
for (a, b), value in np.ndenumerate(c):
    ax.text(b, a, f"{value:+d}" if value else "0", ha="center", va="center",
            color="white" if value else "#52514e", fontsize=10)
```

The $8 \times 8$ table $c$ as a heat map with the boundaries $-3, -1, 1, 3$, so $-2$ is blue, 0 grey and $+2$ red; each number is written into its square (white on colour, dark grey on grey).

```python
labels = [f"$x_{k}$" for k in range(1, 9)]
ax.set_xticks(range(8), labels)
ax.set_yticks(range(8), labels)
ax.set_xlabel("direction $b$")
ax.set_ylabel("direction $a$")
ax.set_title("$\\gamma^a\\gamma^b + \\gamma^b\\gamma^a = c_{ab}\\, I_{16}$")
ax.grid(False)
save_figure(fig, "anticommutator_table", ...)
```

The rows and columns are labelled $x_1, \dots, x_8$, the axes named, the title set, and the figure saved. **What figure 5 shows and why:** a diagonal of three red, four blue and one red square: $c_{ab} = 2\eta^{ab}$, red for the space-like $x_1, x_2, x_3, x_8$, blue for the time-like $x_4$ to $x_7$, and grey off the diagonal because different gammas anticommute. It is the Clifford relation in one picture.

**In [24], reality, signed permutations and the symmetry pattern.**

```python
entries = sorted(set(int(x) for g in gamma for x in g.flatten()))
say(f"the different entries of the eight gamma matrices: {entries}")
rows_ok = all((np.count_nonzero(g, axis=1) == 1).all() for g in gamma)  # each row
columns_ok = all((np.count_nonzero(g, axis=0) == 1).all() for g in gamma)  # column
orthogonal = all((g.T @ g == I16).all() for g in gamma)
```

`g.flatten()` lists all 256 entries of a matrix; collecting them from all eight gammas in a set and sorting gives the different values: $[-1, 0, 1]$. `np.count_nonzero(g, axis=1)` counts the nonzero entries of each row (`axis=0`: of each column); each count must be 1. `orthogonal` tests $g^T g = I_{16}$.

```python
check_record(entries == [-1, 0, 1], "every gamma^a is real with entries -1, 0, +1",
             (WOLFRAM, "reality"))
check_record(rows_ok and columns_ok and orthogonal,
             "every gamma^a is a signed permutation matrix, hence orthogonal",
             (WOLFRAM, "signed_permutation_matrices"),
             (PYTHON, "reality_signed_permutations"))
```

Two checks: reality (the entries are whole numbers $-1, 0, +1$, in particular real), and signed permutation matrices that are orthogonal.

```python
symmetric = [COORDINATES[a] for a in range(8) if (gamma[a].T == gamma[a]).all()]
antisymmetric = [COORDINATES[a] for a in range(8) if (gamma[a].T == -gamma[a]).all()]
say("symmetric: " + ", ".join(symmetric) + ";  antisymmetric: "
    + ", ".join(antisymmetric))
check_record(symmetric == ["x1", "x2", "x3", "x8"]
             and antisymmetric == ["x4", "x5", "x6", "x7"]
             and all((gamma[a].T == eta[a] * gamma[a]).all() for a in range(8)),
             "(gamma^a)^T = eta_aa gamma^a: symmetric for x1, x2, x3, x8 only",
             (WOLFRAM, "symmetry_pattern"), (PYTHON, "symmetry_pattern"))
```

The lists of the symmetric and of the antisymmetric gammas are made and printed: $x_1, x_2, x_3, x_8$ and $x_4, x_5, x_6, x_7$. The check requires exactly these lists and $(\gamma^a)^T = \eta_{aa}\gamma^a$ for all eight: the symmetry pattern proved in Step 4 of Section 4.5.

**In [25], figure 6.**

```python
fig, axes = plt.subplots(2, 2, figsize=(6.4, 6.6), layout="constrained")
draw_signs(axes[0, 0], gamma[0], "$\\gamma^{(x_1)}$ (space-like)")
draw_signs(axes[0, 1], gamma[0].T, "its transpose: the same")
draw_signs(axes[1, 0], gamma[3], "$\\gamma^{(x_4)}$ (time-like)")
draw_signs(axes[1, 1], gamma[3].T, "its transpose: all signs flipped")
sign_legend(fig)
save_figure(fig, "symmetry_pattern", ...)
```

Four panels: $\gamma^{(x_1)}$ and its transpose, $\gamma^{(x_4)}$ and its transpose. **What figure 6 shows and why:** the upper two pictures are identical (a symmetric matrix equals its transpose); in the lower two every red square has become blue and every blue square red at the same place, because the transpose of an antisymmetric matrix is minus the matrix.

**In [26], comparison with the Revision record files.**

```python
def exact(entry):
    if isinstance(entry, int):
        return Fraction(entry)
    if isinstance(entry, str) and "/" in entry:
        numerator, denominator = entry.split("/")
        return Fraction(int(numerator), int(denominator))
    raise ValueError(f"an entry of gammas.json that is not exact: {entry}")
```

The file `gammas.json` writes every number exactly: a whole number as a JSON integer, a fraction as a text such as `"1/2"`. `exact` reads both into an exact `Fraction`: `isinstance(entry, int)` tests whether the entry is a whole number; for a text containing `/`, `split("/")` cuts it into numerator and denominator. Anything else stops the notebook with an error, so no rounded number can slip in.

```python
def differing(stored, ours):
    return sum(1 for (i, j), x in np.ndenumerate(ours)
               if exact(stored[i][j]) != int(x))
```

`differing` counts the entries in which a stored matrix (a list of rows from the file) differs from the notebook's matrix: it runs through all positions $(i, j)$ and adds 1 whenever the two numbers are not equal (`!=`).

```python
fixture = json.loads(repository_file("Revision/algebra/gammas.json")
                     .read_text(encoding="utf-8"))
python_gammas = json.loads(repository_file(
    "Revision/algebra/reports/python-gammas.json").read_text(encoding="utf-8"))
fixture_differ = [differing(fixture["gamma"][a], gamma[a]) for a in range(8)]
python_differ = [differing(python_gammas["gamma"][a], gamma[a]) for a in range(8)]
```

The two Revision files are read: `gammas.json`, written by the WolframScript program, and `python-gammas.json`, written by the independent Python program. For each of the eight gammas the number of differing entries is counted, for both files.

```python
report("entries compared per file", 8 * 16 * 16)
report("differing entries, gammas.json, per x1..x8", fixture_differ)
report("differing entries, python-gammas.json, per x1..x8", python_differ)
```

Three RESULT lines: 2048 entries are compared per file, and the number of differing entries is 0 for every one of the eight gammas, in both files.

```python
check_record(fixture["coordinates"] == COORDINATES and fixture["eta"] == list(eta)
             and fixture["notebookFrameIndex"] == FRAME_INDEX
             and sum(fixture_differ) == 0,
             "Revision/algebra/gammas.json holds exactly these eight gammas",
             (WOLFRAM, "fixture_round_trip"),
             (PYTHON, "fixture_comparison_gammas_json"))
python_map = python_gammas["map_coordinate_to_T16_index"]  # {"x1": 1, ...}
check(python_map == dict(zip(COORDINATES, FRAME_INDEX)) and sum(python_differ) == 0,
      "Revision/algebra/reports/python-gammas.json holds exactly these eight gammas")
```

The first check also compares the coordinate names, the signs and the coordinate map stored in `gammas.json` with the notebook's. The second compares the map stored in the Python file, a dictionary from coordinate names to indices, with the dictionary made from the notebook's two lists (`zip` pairs the two lists entry by entry, `dict` turns the pairs into a dictionary), and requires no differing entry.

**In [27], the totals.**

```python
for report_file in (WOLFRAM, PYTHON):
    verdicts = [entry["verdict"].upper() for entry in RECORDED[report_file].values()]
    passed = verdicts.count("PASS")  # how many checks of the report passed
    mine = [name for f, name in REPRODUCED if f == report_file]
    report(f"{report_file} passed", f"{passed} of {len(verdicts)}")
    report("    of these checks, reproduced in this notebook", len(mine))
check(len(REPRODUCED) == 30, "this notebook reproduces 30 checks of the two reports")
```

For each report, the verdicts of all checks are collected (`.values()` gives the entries of a dictionary), and `count("PASS")` counts the passed ones; `mine` lists the checks of this report that the notebook reproduced. The output: the WolframScript report passed 45 of 45, of which this notebook reproduced 16; the Python report passed 35 of 35, of which it reproduced 14. The check requires 30 reproduced Revision checks in all.

**In [28], the last check.**

```python
names = ["04a_1_blocks_s4_t4.png", "04a_2_tau_matrices.png",
         "04a_3_block_form_of_t16.png", "04a_4_gammas_x1_to_x8.png",
         "04a_5_anticommutator_table.png", "04a_6_symmetry_pattern.png"]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in names),
      "all six figure files exist")
all_checks_passed()
```

The check confirms that the six figure files were written, and `all_checks_passed()` prints the last line, ALL 28 CHECKS PASSED (notebook 04a): one check in each of In [2], In [6], In [9], In [14], In [17], In [20], In [21], In [27] and In [28]; two in each of In [8], In [10], In [22] and In [26]; three in each of In [15] and In [24]; and five in In [13].
