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
- `Revision/algebra/reports/wolfram-algebra.json`: the exact checks of the algebra computed with WolframScript (45 checks, all passed, as Notebook 04a reads and prints them);
- `Revision/algebra/reports/python-algebra.json`: the same algebra checked independently with Python (35 checks, all passed, as Notebook 04a prints them);
- `Revision/algebra/reports/python-gammas.json`: the gammas as rebuilt by the Python program;
- `Revision/theory/reports/python-field-theory.json` and `Revision/theory/reports/python-scope.json`, the theory reports from which Notebook 04b reproduces four checks about plane waves (each named where it is used).

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

The notebook has 28 code cells, In [1] to In [28]. This section quotes every line of every one of them, in order, and explains what each line or small group of lines does. Two kinds of lines are text for the reader and are not executed: a **comment** is everything after a `#` sign on a line, and a **docstring** is a text in triple quotes `"""..."""` directly below a `def` line, which says in words what the function does (Python stores it with the function and skips it when the function runs). They are quoted with the code they describe; the explanations below add what they do not already say.

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
    """Return the repository folder (Dirac_claude).

    Jupyter runs a notebook in the folder that holds it.  Starting there, go up one
    folder at a time until a folder contains Revision/textbook/requirements.txt (the
    list of the book's packages); that folder is the repository."""
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
# The repository folder.  It is never printed: it differs from computer to computer,
# and the printed output of a notebook must not.
REPO = find_repository_root()
# Every file is WRITTEN below OUTPUT_ROOT.  OUTPUT_ROOT is the repository folder unless
# the environment variable TEXTBOOK_OUTPUT_ROOT names another folder; the book's
# checking tool sets it, so that a check run writes into a scratch folder instead.
OUTPUT_ROOT = Path(os.environ.get("TEXTBOOK_OUTPUT_ROOT", str(REPO)))
```

The line `REPO = find_repository_root()` calls the function and names the result `REPO`. As its comment says, it is never printed, because it differs from computer to computer while the printed output must not. The line that defines `OUTPUT_ROOT` chooses the folder below which files are written: `os.environ` holds the **environment variables** of the running program (named texts it receives from the computer), and `.get(name, default)` returns the value of `TEXTBOOK_OUTPUT_ROOT` if it is set and otherwise the default, the repository folder as a string. When you run the notebook the variable is not set, so the files go into the repository; the book's checking tool sets it to a scratch folder.

```python
def repository_file(relative):
    """The path of the repository file relative, for READING (a Revision record)."""
    return REPO / relative


def output_file(relative):
    """The path at which to WRITE the repository file relative (its folder is made)."""
    path = OUTPUT_ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    return path
```

`repository_file("Revision/...")` gives the full path of a repository file, for reading a Revision record. `output_file("Revision/...")` gives the full path at which to write a file; `path.parent.mkdir(parents=True, exist_ok=True)` first creates the folder that will hold it (and any missing folder above it) and does nothing if it exists.

```python
def say(text):
    """Print text in lines of at most 89 characters (the width of a page of the book)."""
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
# Start with an empty captions file ({} is an empty JSON dictionary); save_figure fills
# it.  newline="\n" writes the same line ends on Windows, macOS and Linux.
output_file(CAPTION_FILE).write_text("{}\n", encoding="utf-8", newline="\n")
```

A string that starts with `f` is an **f-string**: every name in braces is replaced by its value, so `CAPTION_FILE` is `"Revision/textbook/figures/04a.captions.json"`. `FIGURE_NUMBERS` and `CAPTIONS` start as empty dictionaries. The last line writes the text `{}` (an empty JSON dictionary) and a line end into the captions file; `encoding="utf-8"` fixes how letters are stored and `newline="\n"` writes the same line end on every operating system.

```python
def save_figure(fig, name, caption):
    """Save the figure fig as Revision/textbook/figures/<id>_<k>_<name>.png, record its
    caption in CAPTION_FILE, show the saved picture below the cell and close the figure.
    k counts the figures of the notebook 1, 2, 3, ...; a cell run again keeps its k."""
    number = FIGURE_NUMBERS.setdefault(name, len(FIGURE_NUMBERS) + 1)
    file_name = f"{NOTEBOOK_ID}_{number}_{name}.png"
    relative = f"{FIGURE_FOLDER}/{file_name}"
    # dpi=150: 150 dots per inch.  bbox_inches="tight": cut away the empty margin.
    # metadata={"Software": None}: no program name is stored in the PNG file, so that
    # every run writes exactly the same bytes.
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

`save_figure` saves and shows a figure, as its docstring says; `<id>` and `<k>` in the docstring stand for the notebook's name and the figure's number. `setdefault(name, value)` returns the number already stored for this figure name or stores and returns one more than the number of figures so far; so the figures are numbered 1, 2, 3, and a cell run twice keeps its number. `fig.savefig` writes the PNG file with 150 dots per inch, cuts away the empty margin (`bbox_inches="tight"`) and stores no program name (`metadata={"Software": None}`), so that two runs write the same bytes. `plt.close(fig)` removes the figure from memory, because Jupyter would otherwise draw it a second time. The caption is stored, the whole dictionary of captions is written to the captions file (`json.dumps` turns it into JSON text, one entry per line, keys sorted), `display(Image(...))` shows the saved picture, and the last line prints where it was saved.

```python
PASSED = []  # the names of the checks that passed, in order


def check(condition, name, record=None):
    """A check.  If condition is False, stop with an AssertionError that names the
    check (an if statement is used instead of assert, because python -O would skip an
    assert).  Otherwise print "PASS <name>" and, when the check reproduces a Revision
    record, a second line naming the record file and its check."""
    if not condition:
        raise AssertionError(f"check failed: {name}")
    PASSED.append(name)
    say(f"PASS {name}")
    if record is not None:
        say(f"     reproduces {record}")
```

`PASSED` is an empty **list** (an ordered collection in square brackets). `check` is behind every check of the book. `condition` is either `True` or `False`; if it is false, `raise AssertionError(...)` stops the notebook with an error naming the check. (Python also has a statement `assert condition`, but the docstring explains why it is not used: Python started with the option `-O` skips every `assert`, while an `if` statement always runs.) Otherwise the name is appended to `PASSED` and `PASS name` is printed. `record=None` makes the third argument optional; when given, a second line names the Revision record that the check reproduces.

```python
def report(label, value, unit=""):
    """Print a key number as a line "RESULT <label> = <value> <unit>"."""
    say(f"RESULT {label} = {value}" + (f" {unit}" if unit else ""))


def all_checks_passed():
    """Print the last line of the notebook: how many checks passed."""
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
    """Mathematica's Signature: 0 if a number occurs twice; otherwise +1 for an even
    and -1 for an odd number of inversions (pairs of positions i < j with
    numbers[i] > numbers[j])."""
    if len(set(numbers)) != len(numbers):  # a set keeps each number only once
        return 0
    inversions = sum(1 for i, j in itertools.combinations(range(len(numbers)), 2)
                     if numbers[i] > numbers[j])
    return -1 if inversions % 2 else 1  # % 2 is the remainder after division by 2
```

The permutation sign of Section 4.2. `set(numbers)` keeps each number once, so if it is shorter than the list a number is repeated and the sign is 0. `itertools.combinations(range(len(numbers)), 2)` lists every pair of positions $i < j$; the expression `sum(1 for ... if numbers[i] > numbers[j])` adds 1 for every pair in which the larger number stands first, that is it counts the inversions. `inversions % 2` is 1 for an odd and 0 for an even count, and Python reads 1 as true and 0 as false, so the function returns $-1$ for an odd and $+1$ for an even number of inversions.

```python
def delta(i, j):
    """The Kronecker delta: 1 if i == j, otherwise 0."""
    return 1 if i == j else 0


def anticommutator(a, b):
    """{a, b} = a b + b a; the operator @ multiplies matrices."""
    return a @ b + b @ a


def identity(n):
    """The n x n identity matrix with whole-number entries."""
    return np.eye(n, dtype=np.int64)


def zeros(n):
    """The n x n zero matrix with whole-number entries."""
    return np.zeros((n, n), dtype=np.int64)
```

Four short functions, each with one line of code below its docstring: the Kronecker delta ($1$ if $i = j$, else 0; `==` tests equality); the anticommutator $\{a, b\} = ab + ba$, with `@` the matrix product; the $n \times n$ identity matrix with whole-number entries (`np.eye`); and the $n \times n$ zero matrix.

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
    """check(condition, name) for a statement that the Revision record verified too.
    records: pairs (report file, check name); each must be recorded as passed."""
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
    """Draw a matrix with entries -1, 0, +1 as a heat map in the panel ax."""
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
    """The key of the three colours, below the panels of the figure."""
    handles = [Patch(facecolor=SIGN_COLOURS(k), edgecolor="#898781", label=label)
               for k, label in enumerate(["entry -1", "entry 0", "entry +1"])]
    fig.legend(handles=handles, loc="outside lower center", ncol=3, fontsize=9,
               frameon=False)
```

`sign_legend` adds the key of the three colours below the panels. `enumerate` numbers the three labels 0, 1, 2; `SIGN_COLOURS(k)` is colour number `k`; each `Patch` is a small coloured square with its label, and `fig.legend` places the three in one row (`ncol=3`) below the figure, without a frame.

**In [5], the six blocks.**

```python
def Qa(h, p, q):
    """The author's Qa[h, p, q] (In[294]); h, p, q count from 1, as in Mathematica."""
    return signature([h, p, q, 4])


def Qb(h, p, q):
    """The author's Qb[h, p, q] (In[294])."""
    return delta(p, 4) * delta(q, h) - delta(p, h) * delta(q, 4)
```

The author's two patterns of Section 4.5, letter for letter: $Q_a[h]_{pq} = \mathrm{Signature}[\{h, p, q, 4\}]$ and $Q_b[h]_{pq} = \delta_{p4}\delta_{qh} - \delta_{ph}\delta_{q4}$, with $h, p, q$ counted from 1; `*` multiplies numbers.

```python
# s4[h] = Qa - Qb (In[300]) and t4[h] = Qa + Qb (In[301]). Row p, column q of the
# formula (1 to 4) is row p - 1, column q - 1 of the numpy array (0 to 3).
s4 = {h: np.array([[Qa(h, p, q) - Qb(h, p, q) for q in range(1, 5)]
                   for p in range(1, 5)]) for h in (1, 2, 3)}
t4 = {h: np.array([[Qa(h, p, q) + Qb(h, p, q) for q in range(1, 5)]
                   for p in range(1, 5)]) for h in (1, 2, 3)}
```

`range(1, 5)` is 1, 2, 3, 4. The inner **list comprehension** `[... for q in range(1, 5)]` makes one row (the four columns $q$), the outer one the four rows $p$, and `np.array` turns the list of rows into a matrix. Row $p$ of the formula becomes row $p - 1$ of the array, because numpy counts from 0. The dictionaries `s4` and `t4` hold the three blocks under the keys 1, 2, 3.

```python
def side_by_side(matrices, labels):
    """Print square matrices next to each other, one printed line per row."""
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
    """(1/2) sum_rs epsilon_pqrs m_rs for every p, q (a 4 x 4 matrix)."""
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
    """x y for quaternions stored as (q1, q2, q3, q4) = q4 + q1 i + q2 j + q3 k."""
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
    """The 4 x 4 matrix of q -> q u: column p holds the components of e_p u."""
    return np.array([quaternion_product(e, u) for e in BASIS]).T


def left_multiplication(u):
    """The 4 x 4 matrix of q -> u q: column p holds the components of u e_p."""
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
    """The code of every row of a signed permutation matrix m: "+5" in row i means
    (m u)_i = +u_5. Stops with an error if a row has not exactly one nonzero."""
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
    """(m u)_row = sign * u_column for a signed permutation m: return (sign, column)."""
    column = int(np.flatnonzero(m[row])[0])
    return int(m[row, column]), column


def signed(sign, letter, index):
    """The text "+u_5" or "-u_5" for sign = +1 or -1, letter = "u", index = 5."""
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
    """An exact number of gammas.json: a JSON integer, or a text "p/q"."""
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
    """How many entries of the stored matrix differ from our integer matrix."""
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

### 4.9 Square roots in 4+4 dimensions and the plane waves of the field

Section 4.3 showed that the Clifford relation is the same statement as the square-root rule. For the author's gammas, whose Clifford relation Section 4.5 proved, the rule reads

$$
\Bigl(\sum_{a=1}^{8} p_a \gamma^{(x_a)}\Bigr)^2 = (p_1^2 + p_2^2 + p_3^2 - p_4^2 - p_5^2 - p_6^2 - p_7^2 + p_8^2)\, I_{16}
$$

for all numbers $p_1, \dots, p_8$: the author's eight matrices take the square root of the quadratic form of his space-time, with a plus sign for 3-space and the hidden direction and a minus sign for the time and the three extra times. (Status: PROVED; Notebook 04b confirms it with sympy for all values of the $p_a$, and with floating-point numbers for 300 random vectors.) This section uses the rule to find what the field equation says about waves, and what a momentum along an extra time does.

**Complex numbers and the conjugate transpose.** A **complex number** is $x + iy$ with real $x, y$ and $i^2 = -1$; its **complex conjugate** is $x - iy$. The **conjugate transpose** $M^\dagger$ of a matrix transposes it and conjugates every entry. A matrix is **Hermitian** if $M^\dagger = M$; a real symmetric matrix is Hermitian. An **eigenvalue** of $M$ is a number $\lambda$ for which a nonzero column $u$ (an **eigenvector**) has $Mu = \lambda u$. A Hermitian matrix has only real eigenvalues. Proof: from $Mu = \lambda u$ follows $u^\dagger M u = \lambda\, u^\dagger u$ (multiply from the left by the row $u^\dagger$); the number $u^\dagger M u$ equals its own complex conjugate, because its conjugate is $u^\dagger M^\dagger u = u^\dagger M u$, so it is real; and $u^\dagger u = \sum_i \lvert u_i \rvert^2$ is real and positive; so $\lambda$ is a real number divided by a positive one. We also quote one fact of linear algebra without proof: for a Hermitian matrix the trace equals the sum of the eigenvalues, each counted as often as it occurs (its **multiplicity**). Finally, the **smallest singular value** of a square matrix $M$ is the smallest length of $Mu$ over all columns $u$ of length 1; it is 0 exactly when some nonzero $u$ has $Mu = 0$. numpy computes it, and Notebook 04b uses it to locate the energies at which waves exist.

**The model: flat 4+4 space.** The full field equation of the theory, $\gamma^\mu D_\mu\Psi = (m + U'(S))\Psi$, is derived in Chapter 7; it contains the frame factors of Section 4.4, the gravitational correction in $D_\mu$, and a self-interaction $U'(S)$. This section studies the simplest equation with the same algebra,

$$
\sum_{a=1}^{8} \gamma^{(x_a)}\, \partial_a \Psi = m\Psi ,
$$

in **flat 4+4 space**, where the metric is the constant $\eta$: no gravity, no inflation, no deflation and no self-interaction ($\partial_a$ is the derivative with respect to $x_a$). This is a model for the algebra only (status ASSUMED for this section): in the author's space-time the extra times deflate at every moment. What carries over is the algebra of the frame: in a region so small that the metric functions change little across it, waves with **frame momenta** $k_a$ obey the same matrix algebra; the Revision record uses this local plane-wave reading with the coefficients of the equation held fixed.

**Plane waves, line by line.** A **plane wave** is $\Psi = u\, e^{i(k_1x_1 + k_2x_2 + k_3x_3 + k_5x_5 + k_6x_6 + k_7x_7 + k_8x_8 - Ex_4)}$ with a constant column $u$; $E$ is its **energy** (its frequency in the time $x_4$) and the $k_a$ are its **momenta**.

1. $\partial_a\Psi = ik_a\Psi$ for $a \neq 4$ and $\partial_4\Psi = -iE\Psi$ — the derivative of $e^{cx}$ is $c\,e^{cx}$.
2. $-iE\gamma^{(x_4)}u + i\sum_{a \neq 4} k_a\gamma^{(x_a)}u = mu$ — line 1 inserted into the equation, and both sides divided by the exponential, which is never zero.
3. $iEu + i\sum_{a \neq 4} k_a\gamma^{(x_4)}\gamma^{(x_a)}u = m\gamma^{(x_4)}u$ — both sides multiplied from the left by $\gamma^{(x_4)}$, and $(\gamma^{(x_4)})^2 = -I_{16}$ ($x_4$ is time-like).
4. $Eu + \sum_{a \neq 4} k_a\gamma^{(x_4)}\gamma^{(x_a)}u = -im\gamma^{(x_4)}u$ — both sides multiplied by $-i$, with $-i \cdot i = 1$.
5. $Eu = hu$ with $h = -im\gamma^{(x_4)} - \sum_{a \neq 4} k_a\gamma^{(x_4)}\gamma^{(x_a)}$ — the sum moved to the right-hand side.

So a plane wave exists exactly when $E$ is an eigenvalue of the $16 \times 16$ matrix $h$. Write $h = m\beta + \sum_{a \neq 4} k_a\alpha_a$ with $\beta = -i\gamma^{(x_4)}$ and $\alpha_a = -\gamma^{(x_4)}\gamma^{(x_a)}$, and abbreviate $g_4 = \gamma^{(x_4)}$, $g_a = \gamma^{(x_a)}$. From the Clifford relation ($g_4^2 = -I$, $g_a^2 = \eta^{aa} I$, different gammas anticommute):

- $\beta^2 = (-i)^2 g_4^2 = (-1)(-1) I = I$ — numbers move to the front;
- $\alpha_a^2 = g_4 g_a g_4 g_a = -g_4 g_4 g_a g_a = -(-1)\eta^{aa} I = \eta^{aa} I$ — one exchange of the neighbours $g_a g_4$ gives the factor $-1$;
- $\beta\alpha_a = i g_4 g_4 g_a = -i g_a$ and $\alpha_a\beta = i g_4 g_a g_4 = -i g_4 g_4 g_a = i g_a$ — so $\beta\alpha_a + \alpha_a\beta = 0$;
- for $a \neq b$: $\alpha_a\alpha_b = g_4 g_a g_4 g_b = -g_4 g_4 g_a g_b = g_a g_b$ and $\alpha_b\alpha_a = g_b g_a = -g_a g_b$ — so they anticommute.

So $\beta$ and the seven $\alpha_a$ obey a Clifford relation with the signs $+1$ for $\beta$ and $\eta^{aa}$ for $\alpha_a$, and the general rule of Section 4.3, applied with the numbers $m$ and $k_a$, gives

$$
h^2 = (m^2 + k_1^2 + k_2^2 + k_3^2 + k_8^2 - k_5^2 - k_6^2 - k_7^2)\, I_{16} .
$$

If $hu = Eu$ with $u \neq 0$, then $h^2u = E^2u$, so

$$
E^2 = m^2 + k_1^2 + k_2^2 + k_3^2 + k_8^2 - k_5^2 - k_6^2 - k_7^2 ,
$$

the **mass shell** of the flat 4+4 equation. Status: PROVED (here, and exactly with sympy in Notebook 04b); it reproduces `Revision/theory/reports/python-field-theory.json`, check `mode_hamiltonian_B_selfadjoint_dispersion` (that check also verifies a statement about a matrix $B$, which Chapter 10 needs and this chapter does not).

**Without momentum along the extra times.** When $k_5 = k_6 = k_7 = 0$ (the Revision record calls this the **good sector**), $h$ is Hermitian, so its eigenvalues are real. Proof: the gammas are real with $(g_a)^T = \eta_{aa} g_a$ (Section 4.5). Then $\beta^\dagger = i g_4^T = -i g_4 = \beta$ (conjugating $-i$ gives $i$, and $g_4$ is antisymmetric). $\alpha_a$ is real with $\alpha_a^T = -g_a^T g_4^T = -(\eta_{aa}g_a)(-g_4) = \eta_{aa} g_a g_4 = -\eta_{aa} g_4 g_a = \eta_{aa}\alpha_a$: symmetric, hence Hermitian, for the space-like $x_1, x_2, x_3, x_8$ (and antisymmetric for the extra times, which is why they are left out here). With real momenta, $h$ is then a sum of Hermitian matrices. The **exact example of the Revision record**: $m = 2$ and $(k_1, k_2, k_3, k_8) = (1, 2, 0, 4)$ give $E^2 = 4 + 1 + 4 + 0 + 16 = 25$, so every eigenvalue is $+5$ or $-5$. How often each occurs follows from the trace: $\mathrm{tr}\, g_4 = 0$ (a block off-diagonal matrix has zeros on its diagonal) and $\mathrm{tr}(g_4 g_a) = -\mathrm{tr}(g_a g_4) = -\mathrm{tr}(g_4 g_a)$ (anticommuting, then the cyclic property), so $\mathrm{tr}(g_4g_a) = 0$ and $\mathrm{tr}\, h = 0$. With $n_+$ eigenvalues $+5$ and $n_-$ eigenvalues $-5$: $n_+ + n_- = 16$ and $5n_+ - 5n_- = \mathrm{tr}\, h = 0$, so $n_+ = n_- = 8$: the energies $+5$ and $-5$, eight times each. Status: PROVED (this derivation) and COMPUTED (Notebook 04b finds the 16 eigenvalues numerically with deviations below $10^{-12}$); it reproduces `Revision/theory/reports/python-field-theory.json`, check `good_sector_spectrum_and_B_sectors` (its exact example).

**A momentum along an extra time.** The extra times enter $E^2$ with a minus sign. Adding a momentum $k_5$ along $x_5$ to the example gives $E^2 = 25 - k_5^2$. For $k_5 < 5$ the energies $\pm\sqrt{25 - k_5^2}$ are real. For $k_5 > 5$ they are imaginary, $E = \pm i\kappa$ with $\kappa = \sqrt{k_5^2 - 25}$, and the factor $e^{-iEx_4}$ of the wave becomes, for $E = i\kappa$, $e^{-i \cdot i\kappa\, x_4} = e^{\kappa x_4}$ (because $-i \cdot i = 1$): the wave **grows exponentially** in the time instead of oscillating, and the one with $E = -i\kappa$ shrinks. In general the growth rate is $\kappa = \sqrt{k_5^2 - m^2 - k_1^2 - k_2^2 - k_3^2 - k_8^2}$ whenever this is real; it has no upper bound as $k_5$ grows. Status: PROVED (the formula) and COMPUTED (Notebook 04b checks all 16 eigenvalues for 160 values of $k_5$ to $10^{-10}$); it reproduces `Revision/theory/reports/python-scope.json`, check `extra_time_growth_rates_unbounded`. A problem of the kind "given the field at one time, find it at later times" is called **well posed** (in the sense of the mathematician Jacques Hadamard) when a solution exists, is unique, and changes only a little when the given data change a little. The Revision record draws from the missing upper bound the conclusion that the first-order equation is not well posed in this sense for data that depend on the extra times (`Revision/theory/reports/python-scope.json`, check `extra_time_growth_rates_unbounded`): a wave with a tiny amplitude but a large momentum $k_5$ grows like $e^{\kappa x_4}$ with an arbitrarily large $\kappa$, so arbitrarily small changes of the data cause large changes after any fixed time. Chapter 8 explains this. The record's smallest exact example is $m = 1$ with only $k_5 = 2$: $h^2 = (1 - 4) I_{16} = -3 I_{16}$, so every eigenvalue has $E^2 = -3$, $E = +i\sqrt3$ or $-i\sqrt3$, eight times each (the trace argument again), and the wave with $E = i\sqrt3$ grows like $e^{\sqrt3\, x_4}$. Status: PROVED (exactly, with sympy, in Notebook 04b); it reproduces `Revision/theory/reports/python-field-theory.json`, check `extra_time_modes_grow`.

**Why the deflation matters here.** In the author's space-time a wave with a fixed **coordinate** momentum $k_{x_5}$ along $x_5$, a factor $e^{ik_{x_5}x_5}$, has a **frame** momentum that grows: the derivative along the frame direction is the coordinate derivative divided by the frame factor $e^{-a_4}\sin^{1/6} z$ of $x_5$ (Section 4.4), so the frame momentum is $e^{a_4}\sin^{-1/6}(z)\, k_{x_5}$. As the extra times deflate ($a_4$ grows), this frame momentum grows like $e^{a_4}$. In the local plane-wave reading that the same Revision check `extra_time_modes_grow` states, every wave along an extra time therefore reaches, sooner or later, the region where its energy is imaginary. Notebook 04b computes only the flat algebra behind this statement; the waves in the curved, deflating space-time are the subject of Chapter 8.

The next three sections hold Notebook 04b.

<!-- NOTEBOOK 04b -->

### 4.12 Line-by-line walk-through of Notebook 04b

The notebook has 17 code cells, In [1] to In [17].

**In [1], the set-up cell.** It is the set-up cell of Notebook 04a, explained line by line in Section 4.8, with one difference: the line `NOTEBOOK_ID = "04b"` names this notebook, so its figures are numbered 04b.1, 04b.2, ..., and its comment lines hold the run instructions of Section 4.10. It prints one line, Set-up of notebook 04b complete: repository folder found, helpers defined.

**In [2], numbers are not enough.**

```python
import numpy as np  # floating-point arrays and linear algebra
import sympy as sp  # exact algebra with symbols
```

numpy computes with floating-point numbers in this notebook (numbers with about 16 significant digits, so the last digits may be rounded); sympy computes exactly with **symbols**, letters that stand for any number, so an identity that sympy confirms holds for every value.

```python
alpha, beta = sp.symbols("alpha beta")  # two unknown numbers
equations = [alpha**2 - 1, beta**2 - 1, 2 * alpha * beta]  # each must equal 0
solutions = sp.solve(equations, [alpha, beta], dict=True)  # ** is a power
say(f"number solutions of alpha^2 = 1, beta^2 = 1, 2 alpha beta = 0: {solutions}")
check(solutions == [], "no two numbers solve the square-root problem")
```

`sp.symbols("alpha beta")` makes two symbols. The list `equations` holds three expressions that must all be zero: $\alpha^2 - 1$, $\beta^2 - 1$ and $2\alpha\beta$ (in Python `**` is a power). `sp.solve` returns the list of all solutions, real or complex, each as a dictionary; it is the empty list `[]`, which the cell prints and the check requires. This confirms the first paragraph of Section 4.3.

**In [3], two real $2 \times 2$ matrices.**

```python
sigma_x = sp.Matrix([[0, 1], [1, 0]])
sigma_z = sp.Matrix([[1, 0], [0, -1]])
N = sp.Matrix([[0, 1], [-1, 0]])
I2 = sp.eye(2)  # the 2 x 2 identity matrix
p, q = sp.symbols("p q", real=True)  # two symbols that stand for any real numbers
```

The three matrices $\sigma_x$, $\sigma_z$ and $N$ of Section 4.3 as sympy matrices (each given by the list of its rows), the identity $I_2$, and two real symbols $p$ and $q$.

```python
euclidean = ((p * sigma_x + q * sigma_z) ** 2).expand()  # multiplied out
indefinite = ((p * sigma_x + q * N) ** 2).expand()
say(f"(p sigma_x + q sigma_z)^2 = {euclidean.tolist()}")
say(f"(p sigma_x + q N)^2 = {indefinite.tolist()}")
```

`** 2` squares the sympy matrix (a matrix product), and `.expand()` multiplies out every entry. The two printed matrices are $(p^2 + q^2)I_2$ and $(p^2 - q^2)I_2$; `.tolist()` writes a matrix as a list of rows.

```python
example = 3 * sigma_x + 4 * sigma_z
say(f"3 sigma_x + 4 sigma_z = {example.tolist()}, its square = "
    f"{(example * example).tolist()}")
check(euclidean == (p**2 + q**2) * I2 and (example * example) == 25 * I2,
      "(p sigma_x + q sigma_z)^2 = (p^2 + q^2) I2 for all p, q")
check(indefinite == (p**2 - q**2) * I2,
      "(p sigma_x + q N)^2 = (p^2 - q^2) I2 for all p, q")
```

The worked example of Section 4.3, $3\sigma_x + 4\sigma_z$ and its square $25 I_2$, is printed; the two checks confirm both identities for all $p$ and $q$ (sympy compares the matrices of expressions exactly).

**In [4], the eigenvalues of the two roots, and figure 1.**

```python
p_values = np.linspace(-3.0, 3.0, 201)  # 201 equally spaced values of p
sx = np.array(sigma_x, dtype=float)  # the same matrices as numpy arrays
sz = np.array(sigma_z, dtype=float)
n_matrix = np.array(N, dtype=float)
```

`np.linspace(-3.0, 3.0, 201)` makes 201 numbers from $-3$ to 3 in equal steps of 0.03. The sympy matrices are copied into numpy arrays of floating-point numbers.

```python
euclid_eigen = np.array([np.sort(np.linalg.eigvals(pv * sx + sz).real)
                         for pv in p_values])  # q = 1
indef_eigen = np.array([np.linalg.eigvals(pv * sx + n_matrix) for pv in p_values])
root_euclid = np.sqrt(p_values**2 + 1.0)
root_indef = np.sqrt((p_values**2 - 1.0).astype(complex))  # complex square root
```

For every value `pv` of $p$ (and $q = 1$), `np.linalg.eigvals` computes the two eigenvalues of $p\sigma_x + \sigma_z$ (`.real` keeps their real parts, `np.sort` puts them in increasing order) and of $p\sigma_x + N$ (complex numbers in general). A square root of $c\,I_2$ has the eigenvalues $\pm\sqrt{c}$ (if $Mu = \lambda u$, then $M^2u = \lambda^2 u = cu$), so they are compared with $\sqrt{p^2 + 1}$ and $\sqrt{p^2 - 1}$; `.astype(complex)` turns the numbers $p^2 - 1$ into complex numbers, so that the square root of a negative one is imaginary instead of an error.

```python
errors = [np.max(np.abs(euclid_eigen[:, 1] - root_euclid)),
          np.max(np.abs(np.sort(np.abs(indef_eigen), axis=1)[:, 1]
                        - np.abs(root_indef)))]
check(max(errors) < 1e-12, "numpy eigenvalues equal +-sqrt(p^2 + 1), +-sqrt(p^2 - 1)")
```

`euclid_eigen[:, 1]` is the column of the larger eigenvalue; its largest distance from $\sqrt{p^2 + 1}$ is the first error. For the second root, `np.abs` takes the size of each complex eigenvalue, and the larger size is compared with the size of $\sqrt{p^2 - 1}$. The check allows a rounding error of $10^{-12}$.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(8.4, 3.8), layout="constrained")
left.plot(p_values, root_euclid, color="#2a78d6", linewidth=2,
          label="$+\\sqrt{p^2+1}$")
left.plot(p_values, -root_euclid, color="#eb6834", linewidth=2,
          label="$-\\sqrt{p^2+1}$")
left.set_title("eigenvalues of $p\\,\\sigma_x + \\sigma_z$")
left.set_xlabel("$p$")
left.set_ylabel("eigenvalue")
left.legend(fontsize=8)
```

A figure with two panels side by side, named `left` and `right`. The left panel draws the two eigenvalues $\pm\sqrt{p^2+1}$ against $p$ (blue and orange lines, two points wide), with a title, axis labels and a legend; `label=` is the name in the legend, and text between dollar signs is typeset as mathematics.

```python
right.plot(p_values, np.abs(root_indef.real), color="#2a78d6", linewidth=2,
           label="real part of $+\\sqrt{p^2-1}$")
right.plot(p_values, np.abs(root_indef.imag), color="#1baf7a", linewidth=2,
           linestyle="--", label="imaginary part of $+\\sqrt{p^2-1}$")
right.set_title("eigenvalues of $p\\,\\sigma_x + N$")
right.set_xlabel("$p$")
right.set_ylabel("part of the eigenvalue")
right.legend(fontsize=8)
save_figure(fig, "square_roots_2x2", ...)
```

The right panel draws the real part (solid) and the imaginary part (dashed) of $\sqrt{p^2 - 1}$, and the figure is saved (its caption is printed in Section 4.11). **What figure 1 shows and why:** on the left two real curves that never meet, because $p^2 + 1 > 0$; on the right the solid curve is zero for $\lvert p \rvert < 1$ and the dashed curve is zero for $\lvert p \rvert > 1$: where the minus term of $p^2 - q^2$ wins, the square root becomes imaginary. This is the two-dimensional picture of what a momentum along an extra time does in In [15].

**In [5], the Pauli matrices.**

```python
sigma_y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
pauli = [sigma_x, sigma_y, sigma_z]
```

$\sigma_y$ with the imaginary unit, which sympy writes `sp.I`, and the list of the three Pauli matrices.

```python
def table_of(matrices, size):
    """The numbers c_ab with {M_a, M_b} = c_ab I; None where it is not a multiple."""
    rows = []
    for ma in matrices:
        row = []
        for mb in matrices:
            m = (ma * mb + mb * ma).expand()
            row.append(m[0, 0] if m == m[0, 0] * sp.eye(size) else None)
        rows.append(row)
    return rows
```

`table_of` computes, for every pair of matrices of the list, the anticommutator; if it is a multiple of the identity, it stores the multiple (its upper-left entry), otherwise the special value `None`. The result is the table of the numbers $c_{ab}$ in $\{M_a, M_b\} = c_{ab} I$, as a list of rows.

```python
pauli_table = table_of(pauli, 2)
say(f"Pauli table c_ab: {pauli_table}")
check(pauli_table == [[2, 0, 0], [0, 2, 0], [0, 0, 2]],
      "{sigma_a, sigma_b} = 2 delta_ab I2 for the three Pauli matrices")
check(sigma_x * sigma_y == sp.I * sigma_z and sigma_x * sigma_y * sigma_z == sp.I * I2,
      "sigma_x sigma_y = i sigma_z and sigma_x sigma_y sigma_z = i I2")
```

The Pauli table is twice the identity table, $2\delta_{ab}$: the Clifford relation for three space directions. The second check confirms $\sigma_x\sigma_y = i\sigma_z$ and $\sigma_x\sigma_y\sigma_z = iI_2$, computed by hand in Section 4.3.

**In [6], Dirac's matrices.**

```python
Z2 = sp.zeros(2, 2)
dirac = [sp.Matrix(sp.BlockMatrix([[I2, Z2], [Z2, -I2]]))]  # gamma_D^0
for s in pauli:  # gamma_D^x, gamma_D^y, gamma_D^z
    dirac.append(sp.Matrix(sp.BlockMatrix([[Z2, s], [-s, Z2]])))
dirac_table = table_of(dirac, 4)
say(f"Dirac table c_ab: {dirac_table}")
check(dirac_table == [[2, 0, 0, 0], [0, -2, 0, 0], [0, 0, -2, 0], [0, 0, 0, -2]],
      "{gamma_D^a, gamma_D^b} = 2 diag(+1, -1, -1, -1)_ab I4")
```

`sp.BlockMatrix` glues $2 \times 2$ blocks, and `sp.Matrix(...)` turns the result into an ordinary $4 \times 4$ matrix. The list `dirac` holds $\gamma_D^0 = \mathrm{diag}(I_2, -I_2)$ and, for each Pauli matrix $s$, $\gamma_D^j = \begin{pmatrix} 0 & s \\ -s & 0 \end{pmatrix}$ (`.append` adds an element to a list). Their table is $2\,\mathrm{diag}(+1, -1, -1, -1)$, which the check requires.

**In [7], figure 2.**

```python
from matplotlib.colors import BoundaryNorm, ListedColormap

TABLE_COLOURS = ListedColormap(["#2a78d6", "#f0efec", "#e34948"])  # -2, 0, +2
TABLE_NORM = BoundaryNorm([-3, -1, 1, 3], 3)
```

Three colours and the boundaries $-3, -1, 1, 3$: $-2$ blue, 0 grey, $+2$ red.

```python
def draw_table(ax, table, labels, title):
    """Draw a table of the numbers c_ab as a heat map with the numbers written in."""
    values = np.array(table, dtype=float)
    ax.imshow(values, cmap=TABLE_COLOURS, norm=TABLE_NORM)
    for (a, b), value in np.ndenumerate(values):
        ax.text(b, a, f"{int(value):+d}" if value else "0", ha="center",
                va="center", color="white" if value else "#52514e", fontsize=11)
    ax.set_xticks(range(len(labels)), labels)
    ax.set_yticks(range(len(labels)), labels)
    ax.set_title(title, fontsize=10)
    ax.grid(False)
```

`draw_table` paints a table of the numbers $c_{ab}$ as a heat map, writes each number into its square (with its sign, or 0), names the rows and columns with `labels`, and sets the title.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(8.0, 4.0), layout="constrained")
draw_table(left, pauli_table, ["$\\sigma_x$", "$\\sigma_y$", "$\\sigma_z$"],
           "Pauli: $\\{\\sigma_a, \\sigma_b\\} = c_{ab} I_2$")
draw_table(right, dirac_table, ["$\\gamma_D^0$", "$\\gamma_D^x$", "$\\gamma_D^y$",
                                "$\\gamma_D^z$"],
           "Dirac: $\\{\\gamma_D^a, \\gamma_D^b\\} = c_{ab} I_4$")
save_figure(fig, "pauli_dirac_tables", ...)
```

The Pauli table on the left, Dirac's on the right. **What figure 2 shows and why:** grey off the diagonal (different matrices anticommute) and twice the signs of the directions on the diagonal: three red squares for Pauli's three space directions; one red square for Dirac's time and three blue ones for his space directions, in his convention $(+1, -1, -1, -1)$.

**In [8], Dirac's mass shell.**

```python
E, k1, k2, k3 = sp.symbols("E k1 k2 k3", real=True)
P = E * dirac[0] - k1 * dirac[1] - k2 * dirac[2] - k3 * dirac[3]
check((P * P).expand() == (E**2 - k1**2 - k2**2 - k3**2) * sp.eye(4),
      "(E gamma_D^0 - k . gamma_D)^2 = (E^2 - k^2) I4 for all E and k")
```

The matrix $P = E\gamma_D^0 - k_1\gamma_D^x - k_2\gamma_D^y - k_3\gamma_D^z$ of Section 4.3 with real symbols, and the exact check $P^2 = (E^2 - k_1^2 - k_2^2 - k_3^2) I_4$ for all values.

```python
dirac_numeric = [np.array(g, dtype=complex) for g in dirac]  # numpy copies


def smallest_singular_value(matrix):
    """The smallest length of matrix @ u over all columns u of length 1."""
    return np.linalg.svd(matrix, compute_uv=False).min()
```

numpy copies of Dirac's matrices with complex entries. `np.linalg.svd(matrix, compute_uv=False)` computes the singular values of a matrix (the possible lengths of $Mu$ along special directions, for columns $u$ of length 1), and `.min()` takes the smallest.

```python
mass, momentum = 3.0, (4.0, 0.0, 0.0)
energies = np.linspace(-8.0, 8.0, 801)  # steps of 0.02


def dirac_operator(energy):
    """P - m I4 for the energy energy and the fixed momentum and mass."""
    P_num = energy * dirac_numeric[0]
    for j in range(3):
        P_num = P_num - momentum[j] * dirac_numeric[j + 1]
    return P_num - mass * np.eye(4)
```

The example $m = 3$, $k = (4, 0, 0)$, for which the mass shell is $E^2 = 9 + 16 = 25$. `energies` holds 801 energies from $-8$ to 8 in steps of 0.02. `dirac_operator(energy)` builds the numeric matrix $P - mI_4$ for one energy.

```python
dirac_svals = np.array([smallest_singular_value(dirac_operator(e))
                        for e in energies])
# The energies where it vanishes, rounded to 6 decimals, as plain Python numbers:
zeros_at = [float(x) for x in np.round(energies[dirac_svals < 1e-9], 6)]
report("energies where a Dirac plane wave exists", zeros_at)
kernel = np.sum(np.linalg.svd(dirac_operator(5.0), compute_uv=False) < 1e-9)
report("independent solutions u at E = 5", int(kernel))
check(zeros_at == [-5.0, 5.0] and kernel == 2,
      "Dirac plane waves exist exactly at E = +-sqrt(m^2 + k^2) = +-5")
```

The smallest singular value is computed at all 801 energies. `energies[dirac_svals < 1e-9]` keeps the energies at which it is below $10^{-9}$ (zero up to rounding): a **boolean mask**, an array of True/False that selects entries. `np.round(..., 6)` rounds them to six decimals. At $E = 5$ the number of singular values below $10^{-9}$ is the number of independent solutions $u$. The output: plane waves exist exactly at $E = -5$ and $E = 5$, with two independent solutions at $E = 5$; the check requires both.

**In [9], figure 3.**

```python
fig, ax = plt.subplots(figsize=(7.0, 3.8), layout="constrained")
ax.plot(energies, dirac_svals, color="#2a78d6", linewidth=2)
for e in (-5.0, 5.0):
    ax.axvline(e, color="#898781", linewidth=1, linestyle=":")
ax.set_xlabel("energy $E$")
ax.set_ylabel("smallest singular value of $P - m I_4$")
ax.set_title("Dirac plane waves for $m = 3$, $k = (4, 0, 0)$")
save_figure(fig, "dirac_mass_shell", ...)
```

The smallest singular value against the energy, with dotted vertical lines (`axvline`) at $E = \pm 5$. **What figure 3 shows and why:** the curve touches zero only at the two dotted lines, the two solutions of $E^2 = m^2 + k^2 = 25$: the first-order matrix equation contains the energy relation of special relativity.

**In [10], the square root in 4+4 dimensions.**

```python
record = json.loads(repository_file("Revision/algebra/gammas.json")
                    .read_text(encoding="utf-8"))
eta = record["eta"]  # [1, 1, 1, -1, -1, -1, -1, 1] in the order x1..x8
for matrix in record["gamma"]:  # the entries must be whole numbers
    if not all(isinstance(x, int) for row in matrix for x in row):
        raise ValueError("a gamma matrix of gammas.json has an entry that is not "
                         "a whole number")
gamma = [np.array(matrix, dtype=np.int64) for matrix in record["gamma"]]
sympy_gamma = [sp.Matrix(matrix) for matrix in record["gamma"]]
say("coordinates " + ", ".join(record["coordinates"]) + f"; eta = {eta}")
```

The author's gammas are read from the Revision record file `gammas.json` (the same matrices that Notebook 04a built from his formulas). The loop makes sure that every entry is a whole number (`isinstance(x, int)`). Then the eight matrices are kept twice: as numpy arrays of whole numbers (`gamma`) and as sympy matrices (`sympy_gamma`). The printed line lists the coordinates and the signs.

```python
p_symbols = sp.symbols("p1:9", real=True)  # p1, p2, ..., p8
p_slash = sp.zeros(16, 16)
for a in range(8):
    p_slash += p_symbols[a] * sympy_gamma[a]
quadratic_form = sum(eta[a] * p_symbols[a] ** 2 for a in range(8))
say(f"quadratic form: {quadratic_form}")
check((p_slash * p_slash).expand() == quadratic_form * sp.eye(16),
      "(sum_a p_a gamma^(xa))^2 = eta(p, p) I16 for all p (exact)")
```

`sp.symbols("p1:9")` makes the eight symbols $p_1, \dots, p_8$. The loop builds $\sum_a p_a\gamma^{(x_a)}$, read "p slash" (`+=` adds to a variable). `quadratic_form` is $\eta(p, p) = \sum_a \eta^{aa}p_a^2$, printed as `p1**2 + p2**2 + p3**2 - p4**2 - p5**2 - p6**2 - p7**2 + p8**2`. The check confirms exactly the square-root rule at the start of Section 4.9.

**In [11], the same with 300 random vectors, and figure 4.**

```python
generator = np.random.default_rng(12345)  # the seed makes the numbers repeatable
vectors = generator.normal(size=(300, 8))  # 300 vectors p with 8 components
forms, diagonal, worst = [], [], []
```

A **random-number generator** started from the fixed number 12345 (its **seed**) produces the same numbers in every run. `normal(size=(300, 8))` draws $300 \times 8$ numbers from the normal (bell-shaped) distribution: 300 vectors $p$. Three empty lists are prepared.

```python
for vector in vectors:
    slash = sum(vector[a] * gamma[a] for a in range(8))  # p slash, a 16 x 16 array
    square = slash @ slash
    form = sum(eta[a] * vector[a] ** 2 for a in range(8))  # eta(p, p)
    forms.append(form)
    diagonal.append(square[0, 0])
    worst.append(np.max(np.abs(square - form * np.eye(16))))
```

For each vector: the floating-point matrix $\sum_a p_a\gamma^{(x_a)}$, its square, and $\eta(p, p)$; the lists collect $\eta(p, p)$, the upper-left entry of the square, and the largest deviation of any entry of the square from $\eta(p, p) I_{16}$.

```python
# The exact size of the rounding errors depends on the computer (its numerical
# library); the right panel of the figure shows them. The check only requires them
# to stay below 1e-12, so the printed lines are the same on every computer.
check(max(worst) < 1e-12, "(p slash)^2 = eta(p, p) I16 for 300 random vectors p")
say("every rounding error of the 300 tests is below 1e-12")
```

The check allows rounding errors up to $10^{-12}$; as the comment says, the exact sizes of rounding errors differ between computers, so the notebook prints only that they are below the bound.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(8.4, 3.8), layout="constrained")
left.plot(forms, diagonal, "o", markersize=4, color="#2a78d6", alpha=0.7)
line = np.array([min(forms), max(forms)])
left.plot(line, line, color="#0b0b0b", linewidth=1, label="slope 1")
left.set_xlabel("$\\eta(p, p)$")
left.set_ylabel("diagonal entry of $(\\sum_a p_a\\gamma^{(x_a)})^2$")
left.set_title("$(\\sum_a p_a\\gamma^{(x_a)})^2 = \\eta(p,p)\\, I_{16}$")
left.legend(fontsize=8)
```

The left panel draws one dot (`"o"`, size 4, 70 per cent opaque) per vector, at $\eta(p, p)$ horizontally and the diagonal entry vertically, and the black line of slope 1 from the smallest to the largest $\eta(p, p)$.

```python
right.semilogy(range(1, 301), np.maximum(worst, 1e-18), "o", markersize=3,
               color="#eb6834")
right.set_xlabel("number of the random vector")
right.set_ylabel("largest deviation from $\\eta(p,p)\\, I_{16}$")
right.set_title("rounding errors")
save_figure(fig, "square_root_8d", ...)
```

The right panel draws, on a **logarithmic** vertical axis (`semilogy`: equal distances for equal factors of ten), the largest deviation for each vector; `np.maximum(worst, 1e-18)` replaces a deviation of exactly 0 by $10^{-18}$, because 0 has no logarithm. **What figure 4 shows and why:** on the left all 300 dots lie on the line of slope 1, for positive and for negative $\eta(p, p)$ (the minus signs of the time and the extra times make many values negative); on the right every deviation is of the size of floating-point rounding, that is, an error in about the sixteenth significant digit of entries whose size is between about 1 and 15, many powers of ten under the tolerance $10^{-12}$. (This panel may look slightly different on another computer; the exact identity is the sympy check of In [10].)

**In [12], the formula for $h^2$.**

```python
THEORY = "Revision/theory/reports/python-field-theory.json"
theory = json.loads(repository_file(THEORY).read_text(encoding="utf-8"))
theory_checks = {entry["name"]: entry for entry in theory["checks"]}


def recorded_pass(name):
    """True when the theory report holds the check name with the verdict pass."""
    return theory_checks.get(name, {}).get("verdict", "").upper() == "PASS"
```

The theory report of the Revision record is read, and its checks are kept in a dictionary by name. `recorded_pass(name)` is true when the report holds the named check with the verdict pass; the chained `.get(..., {})` and `.get("verdict", "")` return an empty dictionary or an empty text instead of an error when something is missing.

```python
m, k = sp.symbols("m", real=True), sp.symbols("k1:9", real=True)  # k[0] is k1
g4 = sympy_gamma[3]  # gamma^(x4)
h = -sp.I * m * g4
for a in range(8):
    if a != 3:  # every direction except the time x4
        h -= k[a] * g4 * sympy_gamma[a]
dispersion = m**2 + k[0]**2 + k[1]**2 + k[2]**2 + k[7]**2 \
    - k[4]**2 - k[5]**2 - k[6]**2
```

A real symbol $m$ and the eight momentum symbols $k_1, \dots, k_8$ (`k[0]` is $k_1$; $k_4$ is not used, because the time carries the energy). `h` is built exactly as in line 5 of Section 4.9: $-im\gamma^{(x_4)}$ minus $k_a\gamma^{(x_4)}\gamma^{(x_a)}$ for every $a$ other than the time (`-=` subtracts from a variable). `dispersion` is $m^2 + k_1^2 + k_2^2 + k_3^2 + k_8^2 - k_5^2 - k_6^2 - k_7^2$.

```python
check((h * h).expand() == dispersion * sp.eye(16)
      and recorded_pass("mode_hamiltonian_B_selfadjoint_dispersion"),
      "h^2 = (m^2 + k1^2 + k2^2 + k3^2 + k8^2 - k5^2 - k6^2 - k7^2) I16")
print(f"     reproduces {THEORY}")
print("         check mode_hamiltonian_B_selfadjoint_dispersion (formula for h^2)")
```

The check confirms $h^2$ exactly, for all values of the symbols, and that the Revision report holds the check `mode_hamiltonian_B_selfadjoint_dispersion` as passed; the two printed lines name the record.

**In [13], the good-sector example.**

```python
gamma_complex = [g.astype(complex) for g in gamma]


def h_matrix(mass_value, momenta):
    """The numeric h for the mass and the eight momenta (momenta[3] is not used)."""
    result = -1j * mass_value * gamma_complex[3]
    for a in range(8):
        if a != 3:
            result = result - momenta[a] * gamma_complex[3] @ gamma_complex[a]
    return result
```

Complex copies of the gammas (Python writes the imaginary unit `1j`), and the function `h_matrix` that builds the numeric $h$ for a mass and a list of eight momenta (`momenta[3]` is not used).

```python
example = h_matrix(2.0, [1.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0])
hermitian = np.array_equal(example, example.conj().T)  # h^dagger = h, exactly
eigenvalues = np.linalg.eigvalsh(example)  # real eigenvalues, increasing order
rounded = [float(x) for x in np.round(eigenvalues, 9)]  # 9 decimals
multiplicities = {value: rounded.count(value) for value in sorted(set(rounded))}
report("eigenvalue: multiplicity of h for m = 2, k = (1, 2, 0, k8 = 4)",
       multiplicities)
```

The record's example $m = 2$, $(k_1, k_2, k_3, k_8) = (1, 2, 0, 4)$. `example.conj().T` is the conjugate transpose, and `np.array_equal` compares exactly: $h$ is Hermitian. `np.linalg.eigvalsh` computes the eigenvalues of a Hermitian matrix (real numbers, in increasing order). They are rounded to nine decimals and counted: the RESULT line reads `{-5.0: 8, 5.0: 8}`.

```python
eight_each = np.allclose(eigenvalues[:8], -5.0, atol=1e-12) and \
    np.allclose(eigenvalues[8:], 5.0, atol=1e-12)
check(hermitian and eight_each
      and recorded_pass("good_sector_spectrum_and_B_sectors"),
      "good sector: h is Hermitian with energies +5 and -5, eight each")
print(f"     reproduces {THEORY}")
print("         check good_sector_spectrum_and_B_sectors (its exact example)")
```

`np.allclose(x, value, atol=1e-12)` is true when every entry of `x` lies within $10^{-12}$ of `value`: the first eight eigenvalues are $-5$ and the last eight $+5$. The check reproduces the record's exact example.

```python
energies_4p4 = np.linspace(-8.0, 8.0, 801)
svals_4p4 = np.array([smallest_singular_value(e * np.eye(16) - example)
                      for e in energies_4p4])
distance = np.minimum(np.abs(energies_4p4 - 5.0), np.abs(energies_4p4 + 5.0))
check(np.max(np.abs(svals_4p4 - distance)) < 1e-9,
      "smallest singular value of E - h = distance from E to +-5")
```

The smallest singular value of $EI_{16} - h$ at 801 energies from $-8$ to 8. For a Hermitian $h$ it equals the distance from $E$ to the nearest eigenvalue, here $\min(\lvert E - 5 \rvert, \lvert E + 5 \rvert)$ (`np.minimum` takes the smaller of two numbers, entry by entry); the check confirms this to $10^{-9}$.

**In [14], figure 5.**

```python
fig, ax = plt.subplots(figsize=(7.0, 3.8), layout="constrained")
ax.plot(energies_4p4, svals_4p4, color="#2a78d6", linewidth=2)
for e in (-5.0, 5.0):
    ax.axvline(e, color="#898781", linewidth=1, linestyle=":")
ax.set_xlabel("energy $E$")
ax.set_ylabel("smallest singular value of $E I_{16} - h$")
ax.set_title("plane waves in flat 4+4 space, $m = 2$, $k = (1, 2, 0;\\ k_8 = 4)$")
save_figure(fig, "mass_shell_4p4", ...)
```

The same kind of figure as figure 3, now for the author's gammas. **What figure 5 shows and why:** a zigzag of straight lines, the distance from $E$ to the nearer of $\pm 5$, touching zero only at the dotted lines $E = \pm 5$, where $E^2 = m^2 + k_1^2 + k_2^2 + k_3^2 + k_8^2 = 25$; each of the two energies belongs to eight independent solutions. It has the shape of the Dirac curve: the same algebra in more directions.

**In [15], a momentum along an extra time, and figure 6.**

```python
SCOPE = "Revision/theory/reports/python-scope.json"
scope = json.loads(repository_file(SCOPE).read_text(encoding="utf-8"))
scope_checks = {entry["name"]: entry for entry in scope["checks"]}
scope_ok = scope_checks.get("extra_time_growth_rates_unbounded", {}).get(
    "verdict", "").upper() == "PASS"  # the record must hold this check as passed
```

The scope report of the Revision record is read, and `scope_ok` is true when it holds the check `extra_time_growth_rates_unbounded` as passed.

```python
k5_values = np.linspace(0.025, 7.975, 160)  # steps of 0.05, avoiding k5 = 5
real_parts, imaginary_parts, deviations, counts_ok = [], [], [], True
for k5 in k5_values:
    values = np.linalg.eigvals(h_matrix(2.0, [1.0, 2.0, 0.0, 0.0, k5, 0.0, 0.0, 4.0]))
    root = np.sqrt(complex(25.0 - k5**2))  # +sqrt(25 - k5^2), complex if needed
    to_plus, to_minus = np.abs(values - root), np.abs(values + root)
    deviations.append(np.max(np.minimum(to_plus, to_minus)))
    counts_ok &= bool(np.sum(to_plus < to_minus) == 8)  # eight near +root
    real_parts.append(np.sort(values.real))
    imaginary_parts.append(np.sort(values.imag))
```

160 values of $k_5$ from 0.025 to 7.975 in steps of 0.05 (the value $k_5 = 5$, where both energies are 0, is skipped). For each, the 16 eigenvalues of $h$ with the momentum $k_5$ added (in position 4 of the list, the direction $x_5$; $h$ is no longer Hermitian, so the general `eigvals` is used); `root` is $\sqrt{25 - k_5^2}$, imaginary when $k_5 > 5$. For each eigenvalue its distance to $+$root and to $-$root is computed; the largest of the smaller distances is stored, and `counts_ok` stays true only if exactly eight eigenvalues lie nearer to $+$root. The sorted real and imaginary parts are kept for the figure.

```python
# As above, the size of the deviations depends on the computer; the check requires
# every one of the 160 x 16 eigenvalues to lie within 1e-10 of its exact value.
check(max(deviations) < 1e-10 and counts_ok and scope_ok,
      "with momentum k5: eight energies +sqrt(25 - k5^2), eight -sqrt(25 - k5^2)")
print(f"     reproduces {SCOPE}")
print("         check extra_time_growth_rates_unbounded (growth rate formula)")
```

The check requires all $160 \times 16$ eigenvalues within $10^{-10}$ of $\pm\sqrt{25 - k_5^2}$, eight of each, and the Revision check as passed.

```python
real_parts, imaginary_parts = np.array(real_parts), np.array(imaginary_parts)
fig, (left, right) = plt.subplots(1, 2, figsize=(8.4, 3.8), layout="constrained")
for column in range(16):  # the 16 eigenvalues; they lie on two curves
    left.plot(k5_values, real_parts[:, column], ".", markersize=3, color="#2a78d6")
    right.plot(k5_values, imaginary_parts[:, column], ".", markersize=3,
               color="#1baf7a")
```

The lists become arrays with one row per $k_5$ and one column per eigenvalue; each column is drawn as small dots, real parts on the left, imaginary parts on the right.

```python
for ax, part in ((left, "real"), (right, "imaginary")):
    ax.axvline(5.0, color="#898781", linewidth=1, linestyle=":")
    ax.set_xlabel("momentum $k_5$ along the extra time $x_5$")
    ax.set_ylabel(f"{part} part of the energy $E$")
left.set_title("real parts: $\\pm\\sqrt{25 - k_5^2}$ for $k_5 < 5$")
right.set_title("imaginary parts: $\\pm\\sqrt{k_5^2 - 25}$ for $k_5 > 5$")
save_figure(fig, "extra_time_momentum", ...)
```

Both panels get a dotted line at $k_5 = 5$ and axis labels, then titles, and the figure is saved. **What figure 6 shows and why:** on the left the real parts follow the upper and the lower half of a circle of radius 5, $\pm\sqrt{25 - k_5^2}$, reach zero at $k_5 = 5$ and stay zero beyond; on the right the imaginary parts are zero up to $k_5 = 5$ and then open up as $\pm\sqrt{k_5^2 - 25}$, growing without bound. Because the extra times enter the quadratic form with a minus sign, a large enough momentum along an extra time turns oscillating waves into growing and shrinking ones.

**In [16], the exact example with growing modes.**

```python
example_values = {m: 1, k[0]: 0, k[1]: 0, k[2]: 0, k[4]: 2, k[5]: 0, k[6]: 0,
                  k[7]: 0}  # mass 1, momentum 2 along x5, nothing else
h_example = h.subs(example_values)  # the exact 16 x 16 matrix h for these numbers
exact_eigenvalues = h_example.eigenvals()  # {eigenvalue: multiplicity}
```

`h.subs(...)` substitutes the numbers of the record's example ($m = 1$, $k_5 = 2$, all other momenta 0) into the exact matrix $h$ of In [12]. `eigenvals()` returns the exact eigenvalues as a dictionary eigenvalue: multiplicity.

```python
names = sorted(str(value) for value in exact_eigenvalues)  # as sympy writes them
# printed in sorted order, so that every run prints the same line
listed = ", ".join(f"{value} ({count} times)" for value, count in
                   sorted(exact_eigenvalues.items(), key=lambda item: str(item[0])))
say(f"h^2 = -3 I16: {h_example * h_example == -3 * sp.eye(16)}; exact eigenvalues: "
    f"{listed}")
```

`names` lists the eigenvalues as sympy writes them, sorted. `listed` writes each eigenvalue with its multiplicity; `sorted(..., key=lambda item: str(item[0]))` sorts the pairs by the text of the eigenvalue (a `lambda` is a one-line function without a name), so that every run prints the same order. The printed line: $h^2 = -3I_{16}$ is True, and the eigenvalues are `-sqrt(3)*I` and `sqrt(3)*I`, eight times each.

```python
detail = theory_checks.get("extra_time_modes_grow", {}).get("detail", "")
check(h_example * h_example == -3 * sp.eye(16)
      and exact_eigenvalues == {sp.sqrt(3) * sp.I: 8, -sp.sqrt(3) * sp.I: 8}
      and recorded_pass("extra_time_modes_grow")
      and "m = 1, k5 = 2" in detail and str(names) in detail,
      "m = 1, k5 = 2: E = +i sqrt(3) and -i sqrt(3), eight each (growing modes)")
print(f"     reproduces {THEORY}")
print("         check extra_time_modes_grow (its exact example)")
```

`detail` is the text of the Revision check `extra_time_modes_grow`. The check requires $h^2 = -3I_{16}$, the eigenvalues $\pm i\sqrt3$ with multiplicity 8 each, the Revision check as passed, and the record's text to contain the example and the same list of eigenvalues word for word.

**In [17], the last check.**

```python
names = ["04b_1_square_roots_2x2.png", "04b_2_pauli_dirac_tables.png",
         "04b_3_dirac_mass_shell.png", "04b_4_square_root_8d.png",
         "04b_5_mass_shell_4p4.png", "04b_6_extra_time_momentum.png"]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in names),
      "all six figure files exist")
all_checks_passed()
```

The six figure files must exist; the last line reads ALL 17 CHECKS PASSED (notebook 04b): one check in each of In [2], In [4], In [6], In [10], In [11], In [12], In [15], In [16] and In [17], and two in each of In [3], In [5], In [8] and In [13].

### 4.13 The 256 products: Cl(4,4) is all real 16 by 16 matrices

The Clifford algebra Cl(4,4) is the set of all real combinations of products of the eight gammas (Section 4.3). This section proves that it is the set of **all** real $16 \times 16$ matrices, and that sixteen is the smallest size eight such matrices can have. Everything follows from the Clifford relation alone.

**Sets and how to count them.** A **set** is a collection of different objects, written in braces, for example $A = \{x_2, x_5\}$; the **empty set** $\{\}$ has no element. A **subset** of a set $S$ is a set whose elements all belong to $S$. A set of eight directions has $2^8 = 256$ subsets, because each of the eight directions is either in a subset or not (two choices, eight times). The **binomial coefficient** $\binom{n}{k}$ ("n choose k") is the number of subsets with $k$ elements of a set with $n$ elements. With the **factorial** $n! = 1 \cdot 2 \cdots n$ and $0! = 1$ it is $\binom{n}{k} = \frac{n!}{k!\,(n-k)!}$: $k$ different elements can be picked one after the other in $n(n-1)\cdots(n-k+1) = n!/(n-k)!$ ways, and every subset of $k$ elements arises in this way $k!$ times, once for each order of its elements. For $n = 8$ the numbers for $k = 0, 1, \dots, 8$ are $1, 8, 28, 56, 70, 56, 28, 8, 1$ (for example $\binom{8}{2} = 8 \cdot 7/2 = 28$). Exactly half of the 256 subsets have an even number of elements. Proof: the rule "add $x_1$ if it is missing, remove it if it is present" turns every subset into another one, changes the number of elements by one (so it turns even into odd and odd into even), and applied twice gives the subset back; so it pairs every even subset with exactly one odd subset, and there are 128 of each.

**The products.** For a set $A$ of directions write $\gamma_A$ for the product of their gammas in increasing order, for example $\gamma_{\{x_2, x_5\}} = \gamma^{(x_2)}\gamma^{(x_5)}$, and $\gamma_{\{\}} = I_{16}$. The number $k$ of factors is the **degree** of $\gamma_A$; the product is **even** if $k$ is even and **odd** if $k$ is odd. There are 256 products, $\binom{8}{k}$ of degree $k$, 128 even and 128 odd. The **symmetric difference** $A \triangle B$ is the set of the directions that lie in exactly one of $A$ and $B$. Three rules follow from the Clifford relation.

**Rule R1: products multiply into products.** $\gamma_A\gamma_B = s(A, B)\,\gamma_{A \triangle B}$ with the sign $s(A, B) = (-1)^{N(A,B)}\prod_{c \in A \cap B}\eta^{cc}$, where $N(A, B)$ is the number of pairs $(a, b)$ with $a$ in $A$, $b$ in $B$ and $a$ later than $b$ in the order $x_1, \dots, x_8$, and $A \cap B$ is the set of the directions in both. Proof, step by step: in $\gamma_A\gamma_B$, take the factors of $\gamma_B$ one after the other, the earliest direction first, and move each to the left until it stands in increasing order. A factor $\gamma^b$ passes exactly the factors $\gamma^a$ of $A$ with $a$ later than $b$ (the factors of $B$ moved before it are earlier than $b$ and stay on its left); each of them is a different gamma, so each exchange gives a factor $-1$ (anticommutation). If $b$ also lies in $A$, $\gamma^b$ then stands next to its partner $\gamma^b$, and the two give $(\gamma^b)^2 = \eta^{bb} I_{16}$ and disappear. What remains is the product, in increasing order, of the directions in exactly one of $A$ and $B$, and the collected signs are $(-1)^{N(A,B)}$ and one $\eta^{cc}$ for each common direction.

**Rule R2: squares.** With $B = A$ the common directions are all of $A$, and $N(A, A)$ is the number of pairs in $A$ with the later one first, $k(k-1)/2$ for a product of degree $k$ (every pair of different elements of $A$ counts once). So

$$
\gamma_A\gamma_A = (-1)^{k(k-1)/2}\prod_{a \in A}\eta^{aa}\; I_{16} :
$$

every product squares to $+I_{16}$ or to $-I_{16}$, and its inverse is $\gamma_A^{-1} = \pm\gamma_A$ with the same sign. For example a product of two gammas has $(\gamma^a\gamma^b)^2 = (-1)^1\eta^{aa}\eta^{bb} I_{16} = -\eta^{aa}\eta^{bb} I_{16}$.

**Rule R3: passing one gamma.** Moving $\gamma^b$ from the left of $\gamma_A$ to its right passes each of the $k$ factors once: $\gamma^b\gamma_A = (-1)^k\gamma_A\gamma^b$ if $b$ is not in $A$ (all $k$ factors are different from $\gamma^b$), and $\gamma^b\gamma_A = (-1)^{k-1}\gamma_A\gamma^b$ if $b$ is in $A$ (passing $\gamma^b$ itself gives no sign).

**The trace lemma.** Every product other than $I_{16}$ has trace 0. Proof, line by line, for a product $\gamma_A$ of degree $k \geq 1$:

1. If $k$ is odd, then $k \leq 7$, so some direction $b$ is not in $A$, and R3 gives $\gamma^b\gamma_A = (-1)^k\gamma_A\gamma^b = -\gamma_A\gamma^b$.
2. If $k$ is even, take $b$ in $A$; R3 gives $\gamma^b\gamma_A = (-1)^{k-1}\gamma_A\gamma^b = -\gamma_A\gamma^b$.
3. In both cases multiply from the left by $(\gamma^b)^{-1} = \eta^{bb}\gamma^b$: $\gamma_A = -(\gamma^b)^{-1}\gamma_A\gamma^b$.
4. Take the trace and use the cyclic property with the two factors $(\gamma^b)^{-1}$ and $\gamma_A\gamma^b$: $\mathrm{tr}\,\gamma_A = -\mathrm{tr}(\gamma_A\gamma^b(\gamma^b)^{-1}) = -\mathrm{tr}\,\gamma_A$.
5. A number equal to its own negative is 0.

Line 1 needs an even number of directions: with an odd number, the product of all of them has odd degree and no direction outside it.

**The products are perpendicular and independent.** Each $\gamma_A$ is a product of orthogonal matrices, hence orthogonal ($(MN)^T(MN) = N^T M^T M N = N^T N = I$), so $\gamma_A^T = \gamma_A^{-1} = \pm\gamma_A$ (R2). Then, line by line:

1. $\gamma_A^T\gamma_B = \pm\gamma_A\gamma_B = \pm\gamma_{A \triangle B}$ — the last remark and R1.
2. $\mathrm{tr}(\gamma_A^T\gamma_B) = 0$ for $A \neq B$ — then $A \triangle B$ is not empty, and the trace lemma applies.
3. $\mathrm{tr}(\gamma_A^T\gamma_A) = \mathrm{tr}\, I_{16} = 16$ — $\gamma_A$ is orthogonal.

The 256 numbers $\mathrm{tr}(\gamma_A^T\gamma_B)$ therefore form the table $16\,\delta_{AB}$; this table is called the **Gram matrix**. Now suppose a combination vanishes, $\sum_B c_B\gamma_B = 0$. Multiplying from the left by $\gamma_A^T$ and taking the trace gives $\sum_B c_B\,\mathrm{tr}(\gamma_A^T\gamma_B) = 16\,c_A = 0$, so every coefficient is 0: the 256 products are **linearly independent** (no combination of them with coefficients not all zero gives the zero matrix).

**They are a basis of all real $16 \times 16$ matrices.** The real $16 \times 16$ matrices form a space of **dimension** 256: every matrix is in exactly one way a combination $\sum_{i,j} M_{ij}E_{ij}$ of the 256 matrices $E_{ij}$ that have a single 1 in row $i$ and column $j$. We quote a fact of linear algebra: in a space of dimension $m$, any $m$ independent elements form a **basis**, that is, every element of the space is exactly one combination of them. So every real $16 \times 16$ matrix $M$ is a combination $M = \sum_A c_A\gamma_A$, and multiplying by $\gamma_A^T$ and taking the trace gives the coefficients:

$$
c_A = \tfrac{1}{16}\,\mathrm{tr}(\gamma_A^T M) .
$$

**Cl(4,4) is the set of all real $16 \times 16$ matrices** (status PROVED; reproduced exactly by Notebook 04c, which finds the **rank** 256 of the 256 products, the rank of a list of matrices being the largest number of independent matrices among them; `Revision/algebra/reports/wolfram-algebra.json`, check `Clifford_basis_spans_full_matrix_algebra`, and `Revision/algebra/reports/python-algebra.json`, check `clifford_products_span_M16`).

**Which products are symmetric.** A product is symmetric exactly when it squares to $+I_{16}$, because $\gamma_A^T = \gamma_A^{-1}$ and $\gamma_A^{-1} = \pm\gamma_A$ with the sign of the square; it is antisymmetric when it squares to $-I_{16}$. The symmetric $16 \times 16$ matrices form a space of dimension $16 \cdot 17/2 = 136$ (the free entries on and above the diagonal) and the antisymmetric ones a space of dimension $16 \cdot 15/2 = 120$ (the free entries above the diagonal). The symmetric products are independent, so there are at most 136 of them; the antisymmetric ones at most 120; together there are $256 = 136 + 120$. So there are exactly 136 symmetric and 120 antisymmetric products (status PROVED; Notebook 04c counts them by degree).

**Even products are block diagonal, odd products block off-diagonal.** Every gamma is block off-diagonal (Section 4.5). By the block rule (Section 4.2), a product of an even number of block off-diagonal matrices is block diagonal and a product of an odd number is block off-diagonal. The block diagonal real matrices form a space of dimension $64 + 64 = 128$, and the 128 even products are independent block diagonal matrices, so by the quoted fact they are a basis of all block diagonal matrices; in the same way the 128 odd products are a basis of all block off-diagonal matrices. Status PROVED; `Revision/algebra/reports/wolfram-algebra.json`, check `even_subalgebra_dimension`, and `Revision/algebra/reports/python-algebra.json`, check `even_products_span_M8_plus_M8`.

**How big must the matrices be?** The argument above works for any even number $n$ of $d \times d$ matrices with a Clifford relation, real or complex, if $\gamma_A^{-1}$ is used in place of $\gamma_A^T$: the $2^n$ products are independent, and independent matrices cannot be more numerous than the dimension $d^2$ of the space of all $d \times d$ matrices. So $d^2 \geq 2^n$. For Dirac's $n = 4$: $d \geq 4$, and his $4 \times 4$ matrices are the smallest possible. For the author's $n = 8$: $d^2 \geq 256$, so $d \geq 16$. **A field on which eight gamma matrices act has at least sixteen components; the author's fields have exactly sixteen** (status PROVED). For an odd number of matrices the trace lemma fails, and fewer components suffice: the author's seven $8 \times 8$ matrices $\tau_1, \dots, \tau_7$ satisfy a Clifford relation (Section 4.5), yet $8^2 = 64 < 2^7 = 128$. The reason is that their product is $\tau_1\cdots\tau_7 = I_8$ (Section 4.5, Step 2, line 9): multiplying the product $\tau_A$ of a set $A$ by the product $\tau_{A'}$ of the remaining directions gives $\pm\tau_1\cdots\tau_7 = \pm I_8$ (R1), so $\tau_{A'} = \pm\tau_A^{-1} = \pm\tau_A$ (R2), and the 128 products come in pairs that are equal up to sign. Notebook 04c finds that exactly $64 = 8^2$ of them are independent.

**The 28 products of two gammas and the matrices $S^{ab}$.** The products of degree 2, $\gamma^a\gamma^b$ with $a$ before $b$, are $\binom{8}{2} = 28$ matrices. The Revision record names the matrices

$$
S^{ab} = \tfrac14\bigl(\gamma^a\gamma^b - \gamma^b\gamma^a\bigr) = \tfrac14[\gamma^a, \gamma^b] .
$$

Line by line, for $a \neq b$: $\gamma^b\gamma^a = -\gamma^a\gamma^b$ (different gammas anticommute); so $\gamma^a\gamma^b - \gamma^b\gamma^a = 2\gamma^a\gamma^b$; so $S^{ab} = \tfrac14 \cdot 2\gamma^a\gamma^b = \tfrac12\gamma^a\gamma^b$. For $a = b$ the two terms cancel: $S^{aa} = 0$. Exchanging $a$ and $b$ changes the sign: $S^{ba} = -S^{ab}$. So the 64 matrices $S^{ab}$ are the 28 products of degree 2, halved, their 28 negatives, and 8 zero matrices; their entries are $0$ and $\pm\tfrac12$. By R2, $(\gamma^a\gamma^b)^2 = -\eta^{aa}\eta^{bb} I_{16}$. Two directions of the same kind (both space-like or both time-like) have $\eta^{aa}\eta^{bb} = +1$, so their product squares to $-I_{16}$, like the imaginary unit; there are $\binom{4}{2} + \binom{4}{2} = 12$ such pairs, the planes of **rotations**. A space-like and a time-like direction have $\eta^{aa}\eta^{bb} = -1$, so their product squares to $+I_{16}$; there are $4 \cdot 4 = 16$ such pairs, the planes of **boosts** (the transformations that, in special relativity, change the velocity of an observer). All 28 are even products, hence block diagonal. The $S^{ab}$ are the **generators** of the rotations and boosts of the 16-component field: a generator is a matrix from which a whole family of transformations is built, the transformation by a small angle $\epsilon$ being $I_{16} + \epsilon S^{ab}$ up to terms with $\epsilon^2$ (Chapter 5 makes this precise). The Revision record checks that they obey the rules of the rotations and boosts of the 4+4 space-time (`Revision/algebra/reports/wolfram-algebra.json`, checks `S_gamma_commutator` and `S_Lorentz_algebra`), and Chapter 5 shows how they generate the groups Spin(4,4) and, with the gammas themselves, Pin(4,4). Status of this paragraph: PROVED; `Revision/algebra/reports/python-algebra.json`, check `S_definition`; `Revision/algebra/reports/wolfram-algebra.json`, checks `S_half_product` and `S_real_entries_in_half_integers`; Notebook 04c compares all 64 matrices $S^{ab}$ entry by entry with the matrices stored in `Revision/algebra/gammas.json` and finds them equal.

The next three sections hold Notebook 04c.

<!-- NOTEBOOK 04c -->

### 4.16 Line-by-line walk-through of Notebook 04c

The notebook has 19 code cells, In [1] to In [19].

**In [1], the set-up cell.** It is the set-up cell of Notebook 04a, explained line by line in Section 4.8, except for the line `NOTEBOOK_ID = "04c"` and the run instructions of Section 4.14 in its comment lines. It prints one line.

**In [2], the 256 products.**

```python
import itertools  # all subsets of a given size
from math import comb  # comb(n, k) is the binomial coefficient n choose k

import numpy as np
import sympy as sp
from matplotlib.colors import BoundaryNorm, ListedColormap
from sympy.polys.matrices import DomainMatrix  # exact matrices for the rank
```

`comb(n, k)` computes $\binom{n}{k}$. `DomainMatrix` is sympy's fast matrix type for exact linear algebra with whole numbers and fractions, used for the ranks in In [10], In [13] and In [15]. The other imports are as in Notebook 04a.

```python
record = json.loads(repository_file("Revision/algebra/gammas.json")
                    .read_text(encoding="utf-8"))
eta = record["eta"]  # [1, 1, 1, -1, -1, -1, -1, 1] in the order x1..x8
gamma = [np.array(matrix, dtype=np.int64) for matrix in record["gamma"]]
I16 = np.eye(16, dtype=np.int64)
```

The author's eight gammas and their signs are read from the Revision record file `gammas.json` (Notebook 04a showed that they are exactly the matrices built from his formulas), as whole-number arrays.

```python
SETS = [s for k in range(9) for s in itertools.combinations(range(8), k)]
INDEX = {s: i for i, s in enumerate(SETS)}  # set -> its number in the list
```

`itertools.combinations(range(8), k)` lists the sets of $k$ directions as tuples of increasing numbers (0 stands for $x_1$, ..., 7 for $x_8$); the list comprehension collects them for $k = 0, 1, \dots, 8$, so `SETS` holds the 256 sets ordered by degree, starting with the empty tuple `()`. `INDEX` gives the number of each set in this list.

```python
products = np.zeros((256, 16, 16), dtype=np.int64)
for i, s in enumerate(SETS):
    matrix = I16
    for a in s:  # multiply the gammas of the set in increasing order
        matrix = matrix @ gamma[a]
    products[i] = matrix
DEGREE = np.array([len(s) for s in SETS])  # the number of factors of each product
```

`products` is one array of shape (256, 16, 16): product number $i$ is `products[i]`, a $16 \times 16$ matrix. For each set the gammas are multiplied in increasing order, starting from $I_{16}$ (so the empty set gives $I_{16}$). `DEGREE` holds the degree of every product.

```python
def label(s):
    """A short name of a set: its coordinate numbers, e.g. (1, 4) -> "25"."""
    return "".join(str(a + 1) for a in s) if s else "I"
```

`label` writes a short name of a set: the coordinate numbers glued together, for example the set $\{x_2, x_5\}$, stored as `(1, 4)`, becomes `"25"`; the empty set (which Python reads as false) becomes `"I"`.

```python
counts = [int(np.sum(DEGREE == k)) for k in range(9)]
report("number of products of degree 0, 1, ..., 8", counts)
report("even and odd products", (sum(counts[0::2]), sum(counts[1::2])))
check(counts == [comb(8, k) for k in range(9)] and sum(counts) == 256
      and sum(counts[0::2]) == 128,
      "the products by degree are 1, 8, 28, 56, 70, 56, 28, 8, 1 (128 even)")
```

`np.sum(DEGREE == k)` counts the products of degree $k$ (True counts as 1). `counts[0::2]` takes every second entry starting with the first (the even degrees), `counts[1::2]` the others. The RESULT lines show $1, 8, 28, 56, 70, 56, 28, 8, 1$ and $(128, 128)$, and the check compares them with the binomial coefficients.

**In [3], figure 1.**

```python
fig, ax = plt.subplots(figsize=(7.0, 3.8), layout="constrained")
ax.set_axisbelow(True)  # grid lines behind the bars
colours = ["#2a78d6" if k % 2 == 0 else "#eb6834" for k in range(9)]
bars = ax.bar(range(9), counts, color=colours, width=0.7)
ax.bar_label(bars, labels=[str(n) for n in counts], padding=2, fontsize=9)
ax.set_xticks(range(9))
ax.set_xlabel("degree $k$ (number of gamma factors)")
ax.set_ylabel("number of products")
ax.set_ylim(0, 80)
ax.legend(handles=[bars[0], bars[1]], labels=["even degree (128 in all)",
                                             "odd degree (128 in all)"], fontsize=9)
save_figure(fig, "products_by_degree", ...)
```

A bar chart: `ax.bar` draws one bar per degree, blue for even and orange for odd degrees; `ax.bar_label` writes each count above its bar; the vertical axis runs from 0 to 80; the legend uses the first two bars (degree 0, blue, and degree 1, orange) as samples of the two colours. **What figure 1 shows and why:** the counts rise from 1 to 70 at degree 4 and fall back to 1, symmetric about the middle because choosing $k$ directions is the same as leaving out $8 - k$; the blue bars add up to 128, the orange ones to 128.

**In [4], rule R1 for all pairs.**

```python
def sign_formula(A, B):
    """s(A, B) of rule R1: (-1)^N(A, B) times the signs eta of the common directions."""
    later_pairs = sum(1 for a in A for b in B if a > b)  # N(A, B)
    sign = (-1) ** later_pairs
    for c in set(A) & set(B):  # & : the directions in both sets
        sign *= eta[c]
    return sign
```

`sign_formula` computes the sign $s(A, B)$ of rule R1: `later_pairs` counts the pairs with $a$ in $A$, $b$ in $B$ and $a$ later than $b$; the sign starts as $(-1)$ to that power and is multiplied (`*=`) by $\eta^{cc}$ for every common direction (`set(A) & set(B)` is the set of the directions in both).

```python
rule_r1 = True
SIGN = np.zeros((256, 256), dtype=np.int64)  # SIGN[i, j] = s(A_i, A_j)
for i, A in enumerate(SETS):
    row = products[i] @ products  # gamma_A times each of the 256 products
    for j, B in enumerate(SETS):
        target = products[INDEX[tuple(sorted(set(A) ^ set(B)))]]  # ^ : symmetric diff.
        SIGN[i, j] = sign_formula(A, B)
        rule_r1 &= bool((row[j] == SIGN[i, j] * target).all())
```

For every product $\gamma_A$, `products[i] @ products` multiplies it with all 256 products at once (numpy applies `@` to each of the 256 matrices in turn). For every $B$, `set(A) ^ set(B)` is the symmetric difference; `sorted` puts it in increasing order and `tuple` makes it a key of `INDEX`, which finds the product $\gamma_{A \triangle B}$. `rule_r1` stays true only if every one of the 65536 products equals $s(A, B)\,\gamma_{A \triangle B}$.

```python
report("pairs with sign +1 and with sign -1",
       (int(np.sum(SIGN == 1)), int(np.sum(SIGN == -1))))
check(rule_r1, "gamma_A gamma_B = s(A,B) gamma_(A sym. diff. B) for all 65536 pairs")
```

The RESULT line counts the pairs with sign $+1$ and $-1$: $(33280, 32256)$. The check confirms rule R1 for all pairs.

```python
signed_permutations = all(
    (np.count_nonzero(m, axis=0) == 1).all() and (np.count_nonzero(m, axis=1) == 1).all()
    and set(np.unique(m)) <= {-1, 0, 1} for m in products[1:])  # <= : subset
check(signed_permutations and all((m.T @ m == I16).all() for m in products),
      "every product is a signed permutation matrix, hence orthogonal")
```

For the products after $I_{16}$ (`products[1:]` skips the first; $I_{16}$ obviously qualifies), every column and every row must have exactly one nonzero entry, and the different values (`np.unique`) must form a subset of $\{-1, 0, 1\}$ (`<=` tests "is a subset of" for sets). The check also confirms $\gamma_A^T\gamma_A = I_{16}$ for all 256.

**In [5], figure 2.**

```python
four = [s for s in SETS if all(a < 4 for a in s)]  # the 16 sets inside x1..x4
table = np.array([[SIGN[INDEX[A], INDEX[B]] for B in four] for A in four])
fig, ax = plt.subplots(figsize=(7.4, 7.0), layout="constrained")
ax.imshow(table, cmap=ListedColormap(["#2a78d6", "#e34948"]),
          norm=BoundaryNorm([-2, 0, 2], 2))
```

`four` keeps the 16 sets made only of $x_1, x_2, x_3, x_4$ (direction numbers below 4). `table` is the $16 \times 16$ table of their signs $s(A, B)$, painted with two colours: blue for $-1$, red for $+1$.

```python
for r, A in enumerate(four):
    for c_, B in enumerate(four):
        name = label(tuple(sorted(set(A) ^ set(B))))
        ax.text(c_, r, ("+" if table[r, c_] > 0 else "-") + name, ha="center",
                va="center", color="white", fontsize=7)
names = [label(s) for s in four]
ax.set_xticks(range(16), names, fontsize=8)
ax.set_yticks(range(16), names, fontsize=8)
ax.set_xlabel("second factor $\\gamma_B$ (coordinate numbers of $B$)")
ax.set_ylabel("first factor $\\gamma_A$")
ax.grid(False)
save_figure(fig, "multiplication_table", ...)
```

Every square gets the sign and the name of $A \triangle B$, so that it reads, for example, $-14$ for $\gamma_A\gamma_B = -\gamma^{(x_1)}\gamma^{(x_4)}$; rows and columns are labelled with the names of the 16 sets. **What figure 2 shows and why:** every product of two of these 16 matrices is again one of them, up to sign (rule R1): they form the Clifford algebra of four directions, the algebra of Dirac's matrices. The diagonal holds the squares, $+$I or $-$I as rule R2 predicts (for example the square of $\gamma^{(x_4)}$ is $-$I, because $x_4$ is time-like).

**In [6], rule R2, and the symmetric products.**

```python
rule_r2 = True
square_sign = np.zeros(256, dtype=np.int64)
for i, s in enumerate(SETS):
    k = len(s)
    predicted = (-1) ** (k * (k - 1) // 2)  # // : division without remainder
    for a in s:
        predicted *= eta[a]
    square_sign[i] = predicted
    rule_r2 &= bool((products[i] @ products[i] == predicted * I16).all())
```

For every product the sign of rule R2, $(-1)^{k(k-1)/2}\prod_{a \in A}\eta^{aa}$, is computed and stored in `square_sign`, and `rule_r2` stays true only if every square equals that sign times $I_{16}$.

```python
symmetric = np.array([(m.T == m).all() for m in products])
antisymmetric = np.array([(m.T == -m).all() for m in products])
plus, minus = int(np.sum(square_sign == 1)), int(np.sum(square_sign == -1))
report("products with square +I16 and with square -I16", (plus, minus))
check(rule_r2, "gamma_A^2 = (-1)^(k(k-1)/2) prod(eta) I16 for all 256 products")
check(plus == 136 == 16 * 17 // 2 and minus == 120 == 16 * 15 // 2
      and (symmetric == (square_sign == 1)).all()
      and (antisymmetric == (square_sign == -1)).all(),
      "136 products are symmetric (square +I16), 120 antisymmetric (square -I16)")
```

Two True/False arrays record which products are symmetric and which antisymmetric; `plus` and `minus` count the squares $+I_{16}$ and $-I_{16}$: $(136, 120)$. The first check confirms R2; the second confirms the counts (Python allows the chain `plus == 136 == 16 * 17 // 2`, meaning both equalities) and that a product is symmetric exactly when its square is $+I_{16}$.

**In [7], figure 3.**

```python
plus_by_degree = [int(np.sum((DEGREE == k) & (square_sign == 1))) for k in range(9)]
minus_by_degree = [int(np.sum((DEGREE == k) & (square_sign == -1))) for k in range(9)]
fig, ax = plt.subplots(figsize=(7.0, 3.8), layout="constrained")
ax.set_axisbelow(True)  # grid lines behind the bars
low = ax.bar(range(9), plus_by_degree, color="#e34948", width=0.7,
             label="square $+I_{16}$ (symmetric)")
high = ax.bar(range(9), minus_by_degree, bottom=plus_by_degree, color="#2a78d6",
              width=0.7, label="square $-I_{16}$ (antisymmetric)")
```

For each degree the products with square $+I_{16}$ and with square $-I_{16}$ are counted (`&` combines two True/False arrays entry by entry). The red bars show the first counts; the blue bars are stacked on top of them (`bottom=`).

```python
# numbers inside the bars that are tall enough, above the two bars of height 1
ax.bar_label(low, labels=[str(n) if n > 2 else "" for n in plus_by_degree],
             label_type="center", color="white", fontsize=8)
ax.bar_label(high, labels=[str(n) if n else "" for n in minus_by_degree],
             label_type="center", color="white", fontsize=8)
for k in (0, 8):
    ax.text(k, plus_by_degree[k] + 1.5, str(plus_by_degree[k]), ha="center",
            fontsize=8, color="#0b0b0b")
ax.set_xticks(range(9))
ax.set_xlabel("degree $k$")
ax.set_ylabel("number of products")
ax.legend(fontsize=9)
save_figure(fig, "squares_by_degree", ...)
```

The counts are written into the middle of the bars that are tall enough; for degrees 0 and 8, whose bars have height 1, the number is written above the bar instead. **What figure 3 shows and why:** the red counts per degree are $1, 4, 16, 28, 38, 28, 16, 4, 1$ and the blue ones $0, 4, 12, 28, 32, 28, 12, 4, 0$; for example among the 28 products of degree 2, the 16 boost planes square to $+I_{16}$ and the 12 rotation planes to $-I_{16}$ (Section 4.13). The totals are 136 and 120, the dimensions of the symmetric and of the antisymmetric matrices.

**In [8], the trace lemma and the Gram matrix.**

```python
traces = np.array([np.trace(m) for m in products])
check(traces[0] == 16 and (traces[1:] == 0).all(),
      "trace lemma: tr gamma_A = 0 for all 255 products other than I16")
```

The trace of every product: 16 for $I_{16}$ and 0 for the 255 others, as the trace lemma says.

```python
flat = products.reshape(256, 256)  # each product as one row of 256 entries
gram = flat @ flat.T  # gram[A, B] = tr(gamma_A^T gamma_B), exact whole numbers
# tr(gamma_A gamma_B) = sum_ij (gamma_A)_ij (gamma_B^T)_ij: the same with the
# transposed products in the second factor.
flat_transposed = products.transpose(0, 2, 1).reshape(256, 256)
without_transpose = flat @ flat_transposed.T
```

`reshape(256, 256)` writes each $16 \times 16$ product as one row of 256 numbers (row by row). Because $\mathrm{tr}(X^TY) = \sum_{i,j}X_{ij}Y_{ij}$ (the definitions of trace, product and transpose), the trace product of two products is the product of their two rows, and `flat @ flat.T` computes all $256 \times 256$ of them at once: the Gram matrix. `products.transpose(0, 2, 1)` transposes every product (it exchanges the last two indices), and the same trick gives the table of $\mathrm{tr}(\gamma_A\gamma_B)$.

```python
check((gram == 16 * np.eye(256, dtype=np.int64)).all(),
      "tr(gamma_A^T gamma_B) = 16 for A = B and 0 otherwise (all 65536 pairs)")
check((without_transpose == 16 * np.diag(square_sign)).all(),
      "tr(gamma_A gamma_B) = 16 times the sign of the square for A = B, else 0")
```

The Gram matrix is $16 I_{256}$, as Section 4.13 proved; and $\mathrm{tr}(\gamma_A\gamma_B)$ is 16 times the sign of the square of $\gamma_A$ for $A = B$ and 0 otherwise.

**In [9], figure 4.**

```python
starts = [int(np.argmax(DEGREE == k)) for k in range(9)]  # first product of degree k
three = ListedColormap(["#2a78d6", "#f0efec", "#e34948"])  # -1, 0, +1
three_norm = BoundaryNorm([-1.5, -0.5, 0.5, 1.5], 3)
fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 4.8), layout="constrained")
```

`np.argmax` of a True/False array gives the position of the first True: `starts[k]` is the number of the first product of degree $k$ (0, 1, 9, 37, ...). The three colours and boundaries of the sign heat maps, and a figure with two panels.

```python
left.imshow(gram // 16, cmap=three, norm=three_norm, interpolation="nearest")
left.set_xticks(range(0, 256, 64))
left.set_yticks(range(0, 256, 64))
left.set_xlabel("number of the product $\\gamma_B$")
left.set_ylabel("number of the product $\\gamma_A$")
left.set_title("$\\mathrm{tr}(\\gamma_A^T\\gamma_B)/16$, all 256 products")
left.grid(False)
```

The left panel paints the Gram matrix divided by 16 (`interpolation="nearest"` draws every entry as a sharp square).

```python
corner = starts[3]  # 37: the products of degree 0, 1 and 2
right.imshow(without_transpose[:corner, :corner] // 16, cmap=three, norm=three_norm)
names = [label(s) for s in SETS[:corner]]
right.set_xticks(range(corner), names, fontsize=5, rotation=90)
right.set_yticks(range(corner), names, fontsize=5)
right.set_title("$\\mathrm{tr}(\\gamma_A\\gamma_B)/16$, degrees 0, 1, 2")
right.grid(False)
save_figure(fig, "trace_products", ...)
```

The right panel magnifies the corner of the table $\mathrm{tr}(\gamma_A\gamma_B)/16$ for the first 37 products ($1 + 8 + 28$, degrees 0, 1 and 2), labelled with their names (the column labels turned by 90 degrees). **What figure 4 shows and why:** on the left a single red diagonal line on grey: every product is perpendicular to every other, which is why they are independent. On the right the diagonal is red for I and for $\gamma^{(x_1)}, \gamma^{(x_2)}, \gamma^{(x_3)}, \gamma^{(x_8)}$ (squares $+I_{16}$), blue for $\gamma^{(x_4)}, \dots, \gamma^{(x_7)}$ (squares $-I_{16}$), and for the products of two gammas red for the 16 boost planes and blue for the 12 rotation planes, $-\eta^{aa}\eta^{bb}$ by rule R2.

**In [10], the exact rank.**

```python
WOLFRAM = "Revision/algebra/reports/wolfram-algebra.json"
PYTHON = "Revision/algebra/reports/python-algebra.json"
RECORDED = {}
for report_file in (WOLFRAM, PYTHON):
    text = repository_file(report_file).read_text(encoding="utf-8")
    RECORDED[report_file] = {e["name"]: e for e in json.loads(text)["checks"]}
```

The two algebra reports of the Revision record are read, as in Notebook 04a.

```python
def recorded(report_file, name):
    """The detail text of a Revision check; it must be recorded as passed."""
    entry = RECORDED[report_file][name]
    if entry["verdict"].upper() != "PASS":
        raise AssertionError(f"{report_file}: {name} is not recorded as passed")
    return entry["detail"]
```

`recorded` returns the detail text of a Revision check after making sure that it is recorded as passed.

```python
def exact_rank(rows):
    """The exact rank of a list of rows of whole numbers (fractions, over QQ)."""
    matrix = DomainMatrix([[sp.ZZ(int(x)) for x in row] for row in rows],
                          (len(rows), len(rows[0])), sp.ZZ)
    return matrix.convert_to(sp.QQ).rank()
```

The **rank** of a list of rows is the largest number of independent rows among them. `exact_rank` builds a `DomainMatrix` of whole numbers (`sp.ZZ`, with its numbers of rows and columns), converts it to the rational numbers `sp.QQ` (exact fractions) and computes its rank by exact elimination, without any rounding.

```python
rank_all = exact_rank(flat.tolist())
report("exact rank of the 256 products", rank_all)
check(rank_all == 256
      and f"span dimension {rank_all} = 16^2" in recorded(
          WOLFRAM, "Clifford_basis_spans_full_matrix_algebra")
      and f"{rank_all} (sympy DomainMatrix over QQ)" in recorded(
          PYTHON, "clifford_products_span_M16"),
      "the 256 products are independent: Cl(4,4) is all real 16 x 16 matrices")
print(f"     reproduces {WOLFRAM}")
print("         check Clifford_basis_spans_full_matrix_algebra")
print(f"     reproduces {PYTHON}")
print("         check clifford_products_span_M16")
```

The 256 products, as 256 rows of 256 numbers, have the exact rank 256. The check also requires that both Revision checks state this rank in their own words (the texts are built with the computed rank, so they must contain 256). The printed lines name the two records.

**In [11], every matrix is a combination of the products.**

```python
e00 = np.zeros((16, 16), dtype=np.int64)
e00[0, 0] = 1
generator = np.random.default_rng(12345)
random_matrix = generator.integers(-3, 4, size=(16, 16))  # whole numbers -3..3
coefficients = {}
```

Two example matrices: $E_{00}$, with a single 1 in row 0 and column 0, and a $16 \times 16$ matrix of random whole numbers from $-3$ to 3 (the upper limit 4 of `integers` is not included), from a generator with the fixed seed 12345.

```python
for name, matrix in (("E00", e00), ("random", random_matrix)):
    sixteen_c = flat @ matrix.reshape(256)  # 16 c_A = tr(gamma_A^T M) for all A
    rebuilt = np.einsum("a,aij->ij", sixteen_c, products)  # sum_A (16 c_A) gamma_A
    coefficients[name] = sixteen_c / 16.0
    check((rebuilt == 16 * matrix).all(),
          f"the matrix {name} equals sum_A c_A gamma_A with c_A = tr(gamma_A^T M)/16")
```

For each example, `flat @ matrix.reshape(256)` computes the 256 numbers $\mathrm{tr}(\gamma_A^T M) = 16c_A$ (whole numbers, so the arithmetic stays exact). `np.einsum("a,aij->ij", ...)` forms $\sum_A (16c_A)\gamma_A$ (the letter `a`, missing after the arrow, is summed). The check requires that this is exactly $16M$; the coefficients $c_A$ are stored for the figure. Two PASS lines.

```python
nonzero = [label(SETS[i]) for i in np.flatnonzero(coefficients["E00"])]
diagonal = [label(s) for i, s in enumerate(SETS)
            if (products[i] == np.diag(np.diag(products[i]))).all()]
say("the nonzero coefficients of E00 belong to: " + ", ".join(nonzero))
check(nonzero == diagonal and len(nonzero) == 16
      and set(np.abs(coefficients["E00"][np.flatnonzero(coefficients["E00"])]))
      == {1 / 16},
      "E00 has 16 coefficients +-1/16, on the 16 diagonal products")
```

`nonzero` names the products with a nonzero coefficient in $E_{00}$; `diagonal` names the products that are diagonal matrices (a matrix equals the diagonal matrix of its own diagonal exactly when it is diagonal). The printed list is I, 16, 25, 34, 78, 1256, 1346, 1678, 2345, 2578, 3478, 123456, 125678, 134678, 234578, 12345678: exactly the 16 sets made of whole pairs $(x_1, x_6)$, $(x_2, x_5)$, $(x_3, x_4)$, $(x_7, x_8)$, each pair either in or out, a pattern that Section 4.17 explains. The check requires that the two lists agree, that there are 16, and that every nonzero coefficient is $\pm 1/16$. (The reason: $c_A = \mathrm{tr}(\gamma_A^T E_{00})/16 = (\gamma_A)_{00}/16$, which is nonzero only when row 0 of the signed permutation $\gamma_A$ points to column 0.)

**In [12], figure 5.**

```python
fig, (top, bottom) = plt.subplots(2, 1, figsize=(8.0, 5.6), layout="constrained",
                                  sharex=True)
for ax, name, colour in ((top, "E00", "#2a78d6"), (bottom, "random", "#eb6834")):
    ax.bar(range(256), coefficients[name], color=colour, width=0.8)
    ax.axhline(0.0, color="#898781", linewidth=0.8)
    ax.set_ylabel("coefficient $c_A$")
    for start in starts[1:]:
        ax.axvline(start - 0.5, color="#c3c2b7", linewidth=0.6, linestyle=":")
top.set_title("$E_{00}$ (a single 1 in row 0, column 0)")
bottom.set_title("a matrix of random whole numbers from $-3$ to $3$")
bottom.set_xlabel("number of the product $\\gamma_A$ (dotted lines: degree changes)")
save_figure(fig, "coefficients", ...)
```

Two panels one above the other, sharing the horizontal axis (`sharex=True`): one bar per product with its coefficient, a grey zero line, and dotted lines where the degree changes. **What figure 5 shows and why:** for $E_{00}$ only 16 bars, all of height $\pm 1/16$, at the diagonal products; for the random matrix nearly every one of the 256 bars is nonzero. Every matrix, however special or random, is a combination of the 256 products.

**In [13], even and odd products.**

```python
even, odd = flat[DEGREE % 2 == 0], flat[DEGREE % 2 == 1]  # rows of 256 numbers
even_blocks = all((m[:8, 8:] == 0).all() and (m[8:, :8] == 0).all()
                  for m in products[DEGREE % 2 == 0])
odd_blocks = all((m[:8, :8] == 0).all() and (m[8:, 8:] == 0).all()
                 for m in products[DEGREE % 2 == 1])
rank_even, rank_odd = exact_rank(even.tolist()), exact_rank(odd.tolist())
report("exact ranks of the even and of the odd products", (rank_even, rank_odd))
```

The masks `DEGREE % 2 == 0` and `== 1` select the even and the odd products. `even_blocks` requires every even product to be block diagonal (zero upper-right and lower-left blocks), `odd_blocks` every odd one to be block off-diagonal. Both exact ranks are 128.

```python
check(even_blocks and odd_blocks and rank_even == 128 and rank_odd == 128
      and f"dimension {rank_even} = 2 x 8^2" in recorded(
          WOLFRAM, "even_subalgebra_dimension")
      and f"rank {rank_even} (Fraction), {rank_even} (sympy)" in recorded(
          PYTHON, "even_products_span_M8_plus_M8"),
      "even products block diagonal, odd block off-diagonal, ranks 128 and 128")
print(f"     reproduces {WOLFRAM}")
print("         check even_subalgebra_dimension")
print(f"     reproduces {PYTHON}")
print("         check even_products_span_M8_plus_M8")
```

The check combines the block forms, the two ranks and the statements of the two Revision checks.

```python
support_even = np.sum(products[DEGREE % 2 == 0] != 0, axis=0)  # count per entry
support_odd = np.sum(products[DEGREE % 2 == 1] != 0, axis=0)
report("even products nonzero at each position (values found)",
       sorted(set(int(x) for x in support_even.flatten())))
```

For each position $(i, j)$, `support_even` counts how many even products have a nonzero entry there (`axis=0` adds over the 128 products), and `support_odd` the same for the odd ones. The RESULT line shows that the even counts take only the values 0 and 16.

```python
upper = np.arange(16) < 8  # True for the rows (and columns) 0 to 7
# in_diagonal_blocks[i, j] is True when row i and column j lie in the same half;
# ~ turns True into False and back.
in_diagonal_blocks = np.equal.outer(upper, upper)
check((support_even[in_diagonal_blocks] == 16).all()
      and (support_even[~in_diagonal_blocks] == 0).all()
      and (support_odd[~in_diagonal_blocks] == 16).all()
      and (support_odd[in_diagonal_blocks] == 0).all(),
      "each position of its blocks is covered by exactly 16 even (or odd) products")
```

`upper` marks the upper half of the rows; `np.equal.outer(upper, upper)` is the $16 \times 16$ table that is True where row and column lie in the same half (the two diagonal blocks). The check requires 16 even products at every position of the diagonal blocks and none elsewhere, and the opposite for the odd products.

**In [14], figure 6.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(8.4, 4.2), layout="constrained")
cover = ListedColormap(["#f0efec", "#1c5cab"])  # 0 products, 16 products
for ax, values, title in ((left, support_even, "128 even products"),
                          (right, support_odd, "128 odd products")):
    ax.imshow(values, cmap=cover, norm=BoundaryNorm([-1, 8, 17], 2))
    ax.set_xticks(range(0, 16, 4))
    ax.set_yticks(range(0, 16, 4))
    ax.set_title(title)
    ax.set_xlabel("column")
    ax.set_ylabel("row")
    ax.axhline(7.5, color="#0b0b0b", linewidth=1)
    ax.axvline(7.5, color="#0b0b0b", linewidth=1)
    ax.grid(False)
save_figure(fig, "even_odd_blocks", ...)
```

Two heat maps of the counts, light grey for 0 and dark blue for 16, with black lines between the blocks. **What figure 6 shows and why:** the even products fill exactly the two diagonal $8 \times 8$ blocks, and the odd ones exactly the two others, because every gamma is block off-diagonal (Section 4.13).

**In [15], how big must the matrices be?**

```python
def all_products(generators):
    """The 2^n ordered products of a list of square sympy matrices."""
    size = generators[0].shape[0]
    result = []
    for k in range(len(generators) + 1):
        for s in itertools.combinations(range(len(generators)), k):
            matrix = sp.eye(size)
            for a in s:
                matrix = matrix * generators[a]
            result.append(matrix)
    return result
```

`all_products` forms the $2^n$ ordered products of a list of $n$ sympy matrices, exactly as In [2] did for the gammas.

```python
sigma_x, sigma_y = sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]])
sigma_z, N_matrix = sp.Matrix([[1, 0], [0, -1]]), sp.Matrix([[0, 1], [-1, 0]])
Z2, I2 = sp.zeros(2, 2), sp.eye(2)
dirac = [sp.Matrix(sp.BlockMatrix([[I2, Z2], [Z2, -I2]]))] + [
    sp.Matrix(sp.BlockMatrix([[Z2, s], [-s, Z2]])) for s in (sigma_x, sigma_y, sigma_z)]
taus = [sp.Matrix(gamma[a][8:, :8].tolist()) for a in range(7)]  # tau[1..7]
```

The Pauli matrices, $N$, and Dirac's four matrices (Section 4.3), rebuilt in three lines. `taus` takes the lower-left $8 \times 8$ blocks of $\gamma^{(x_1)}, \dots, \gamma^{(x_7)}$; by the author's construction these are $\tau_1, \dots, \tau_7$ (Section 4.5).

```python
examples = {"n = 2, real 2 x 2": [sigma_x, N_matrix], "n = 4, Dirac 4 x 4": dirac,
            "n = 7, tau 8 x 8": taus, "n = 8, gammas 16 x 16":
                [sp.Matrix(g.tolist()) for g in gamma]}
rows = []
for name, generators in examples.items():
    prods = all_products(generators)
    d = generators[0].shape[0]
    flat_rows = sp.Matrix([list(m) for m in prods])  # one row per product
    # exact rank; from_Matrix chooses exact numbers (Gaussian integers for Dirac)
    rank = DomainMatrix.from_Matrix(flat_rows).rank()
    rows.append((name, len(prods), rank, d * d))
    print(f"{name:24} products {len(prods):4d}   rank {rank:4d}   d^2 {d * d:4d}")
```

Four examples, each a list of matrices with a Clifford relation: $\sigma_x$ and $N$ (signs $+1, -1$), Dirac's matrices, the seven $\tau$, and the eight gammas. For each, all $2^n$ products are formed; `list(m)` lists the entries of a sympy matrix row by row, so `flat_rows` has one row per product; `DomainMatrix.from_Matrix` chooses an exact number system (for Dirac's matrices the **Gaussian integers**, whole numbers plus whole multiples of $i$), and `.rank()` computes the exact rank. One line per example is printed: products 4, 16, 128, 256; ranks 4, 16, 64, 256; $d^2$ 4, 16, 64, 256.

```python
tau_product = sp.eye(8)
for t in taus:
    tau_product = tau_product * t
check([r[2] for r in rows] == [4, 16, 64, 256] and [r[1] for r in rows]
      == [4, 16, 128, 256], "ranks 4, 16, 64, 256: products fill d^2 for even n")
check(tau_product == sp.eye(8) and taus[6] == sp.diag(-1, -1, -1, -1, 1, 1, 1, 1)
      and "tau[7] = diag(-I4, I4) and tau[1]...tau[7] = ID8"
      in recorded(PYTHON, "tau7_and_product"),
      "tau[1] tau[2] ... tau[7] = I8 and tau[7] = diag(-I4, I4)")
print(f"     reproduces {PYTHON}")
print("         check tau7_and_product")
```

The product of the seven $\tau$ is computed. The first check requires the ranks and the numbers of products of the table; the second that $\tau_1\cdots\tau_7 = I_8$ and $\tau_7 = \mathrm{diag}(-I_4, I_4)$, the reason why only 64 of the 128 products of the seven $\tau$ are independent (Section 4.13).

**In [16], figure 7.**

```python
fig, ax = plt.subplots(figsize=(7.6, 4.0), layout="constrained")
ax.set_axisbelow(True)  # grid lines behind the bars
positions = np.arange(len(rows))
for offset, column, colour, name in ((-0.25, 1, "#2a78d6", "number of products $2^n$"),
                                     (0.0, 2, "#eb6834", "exact rank"),
                                     (0.25, 3, "#1baf7a", "$d^2$ (all matrices)")):
    values = [r[column] for r in rows]
    bars = ax.bar(positions + offset, values, width=0.24, color=colour, label=name)
    ax.bar_label(bars, labels=[str(v) for v in values], fontsize=8, padding=1)
ax.set_yscale("log", base=2)
ax.set_ylim(1, 1024)
ax.set_xticks(positions, [r[0] for r in rows], fontsize=9)
ax.set_ylabel("count (logarithmic scale)")
ax.legend(fontsize=8, loc="upper left")
save_figure(fig, "how_big", ...)
```

For each of the four examples three bars side by side (shifted by $-0.25$, 0 and $+0.25$): the number of products, the exact rank and $d^2$, each labelled with its value; the vertical axis is logarithmic with base 2, from 1 to 1024. **What figure 7 shows and why:** for $n = 2$, 4 and 8 the three bars of each group have the same height, $2^n = d^2$: the products fill all $d \times d$ matrices, so no smaller $d$ is possible. For $n = 7$ the first bar (128) is taller than the other two (64): seven matrices fit into $8 \times 8$, but eight need $16 \times 16$.

**In [17], the 28 products of two gammas and the matrices $S^{ab}$.**

```python
from fractions import Fraction  # exact fractions such as 1/2


def exact(entry):
    """A number of gammas.json: a JSON integer or a text "p/q", as a Fraction."""
    if isinstance(entry, int):
        return Fraction(entry)
    numerator, denominator = entry.split("/")
    return Fraction(int(numerator), int(denominator))
```

`exact` reads a number of `gammas.json` (a whole number, or a text "p/q") as an exact fraction, as in Notebook 04a.

```python
PAIRS_AB = [(a, b) for a in range(8) for b in range(a + 1, 8)]  # the 28 pairs
two = {(a, b): products[INDEX[(a, b)]] for a, b in PAIRS_AB}  # gamma^a gamma^b
half_ok, record_ok, values = True, True, set()
```

`PAIRS_AB` lists the 28 pairs $a < b$, and `two` looks up their products $\gamma^a\gamma^b$ among the 256 products. Three variables start: two truth values and an empty set of the entries found.

```python
for a, b in itertools.product(range(8), repeat=2):  # all 64 ordered pairs
    ab, ba = gamma[a] @ gamma[b], gamma[b] @ gamma[a]
    commutator = ab - ba  # 4 S^ab, a whole-number matrix
    if a != b:
        half_ok &= bool((commutator == 2 * ab).all())  # 4 S^ab = 2 gamma^a gamma^b
    else:
        half_ok &= not commutator.any()  # S^aa = 0
```

For all 64 ordered pairs the commutator $\gamma^a\gamma^b - \gamma^b\gamma^a = 4S^{ab}$ is computed with whole numbers. For $a \neq b$ it must equal $2\gamma^a\gamma^b$ (so $S^{ab} = \tfrac12\gamma^a\gamma^b$); for $a = b$ it must vanish (`.any()` is true when some entry is nonzero, `not` reverses it).

```python
    stored = record["S"][a][b]  # the record's S^ab: 16 rows of exact numbers
    for i, j in itertools.product(range(16), repeat=2):
        ours = Fraction(int(commutator[i, j]), 4)  # S^ab entry, exact
        values.add(ours)
        record_ok &= exact(stored[i][j]) == ours
```

Still inside the loop: the record file stores $S^{ab}$ under the key `"S"`; every one of its 256 entries is compared with the exact fraction (commutator entry)/4, and the entry is added to the set `values`.

```python
report("the different entries of the 64 matrices S^ab",
       [str(v) for v in sorted(values)])
check(half_ok and record_ok and sorted(values) == [Fraction(-1, 2), 0,
                                                   Fraction(1, 2)]
      and "(1/2) gamma^a gamma^b for a != b" in recorded(PYTHON, "S_definition")
      and "S^ab = (1/2) gamma^a gamma^b" in recorded(WOLFRAM, "S_half_product")
      and "{-1/2, 0, 1/2}" in recorded(WOLFRAM, "S_real_entries_in_half_integers"),
      "S^ab = (1/4)(g^a g^b - g^b g^a) = (1/2) g^a g^b = the record's S, entry by entry")
print(f"     reproduces {PYTHON}")
print("         check S_definition")
print(f"     reproduces {WOLFRAM}")
print("         checks S_half_product, S_real_entries_in_half_integers")
```

The RESULT line lists the entries found, $-1/2$, 0 and $1/2$. The check combines: $S^{ab} = \tfrac12\gamma^a\gamma^b$ and $S^{aa} = 0$; all $64 \times 256 = 16384$ entries equal to the record's; the entries are exactly $-\tfrac12, 0, \tfrac12$; and the statements of the three Revision checks.

```python
square_of = {pair: int((m @ m)[0, 0]) for pair, m in two.items()}  # +1 or -1
rotations = [pair for pair in PAIRS_AB if square_of[pair] == -1]
boosts = [pair for pair in PAIRS_AB if square_of[pair] == 1]
report("pairs whose product squares to -I16 (rotations), to +I16 (boosts)",
       (len(rotations), len(boosts)))
check(all((m @ m == square_of[(a, b)] * I16).all()
          and square_of[(a, b)] == -eta[a] * eta[b]
          and not m[:8, 8:].any() and not m[8:, :8].any()
          for (a, b), m in two.items())
      and len(rotations) == 12 and len(boosts) == 16,
      "(g^a g^b)^2 = -eta^aa eta^bb I16; 12 rotation, 16 boost planes; block diagonal")
```

For each of the 28 products the sign of its square is read off its upper-left entry; the pairs are sorted into rotation planes (square $-I_{16}$) and boost planes (square $+I_{16}$): $(12, 16)$. The check requires, for every pair, that the square is exactly that sign times $I_{16}$, that the sign is $-\eta^{aa}\eta^{bb}$, and that the product is block diagonal; and the counts 12 and 16.

**In [18], figure 8.**

```python
from matplotlib.patches import Patch  # coloured squares for the key

FRAME = {-1: "#0b0b0b", 1: "#1baf7a"}  # square -I16: black, square +I16: green
fig, axes = plt.subplots(7, 7, figsize=(8.6, 8.9), layout="constrained")
```

The frame colours: black for a rotation plane, green for a boost plane. The figure has a grid of $7 \times 7$ panels.

```python
for r, c_ in itertools.product(range(7), repeat=2):
    ax = axes[r, c_]
    a, b = r, c_ + 1  # row: first factor x_(a+1); column: second factor x_(b+1)
    if b <= a:
        ax.axis("off")  # no panel on or below the diagonal
        continue
    ax.imshow(two[(a, b)], cmap=three, norm=three_norm)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():  # the frame of the panel
        spine.set_edgecolor(FRAME[square_of[(a, b)]])
        spine.set_linewidth(2.0)
    ax.set_title(f"$x_{a + 1}\\,x_{b + 1}$", fontsize=8)
```

Panel $(r, c)$ shows the product of the directions $a = r$ and $b = c + 1$ (rows $x_1$ to $x_7$, columns $x_2$ to $x_8$). The panels on and below the diagonal ($b \le a$) are switched off, and `continue` jumps to the next panel. Each remaining panel shows $\gamma^a\gamma^b$ as a heat map without tick marks; its four border lines (`spines`) get the colour of its plane, two points wide, and its title names the two directions.

```python
key = [Patch(facecolor="white", edgecolor=FRAME[-1], linewidth=2,
             label="square $-I_{16}$: rotation plane (12)"),
       Patch(facecolor="white", edgecolor=FRAME[1], linewidth=2,
             label="square $+I_{16}$: boost plane (16)"),
       Patch(facecolor="#2a78d6", label="entry $-1$"),
       Patch(facecolor="#e34948", label="entry $+1$")]
fig.legend(handles=key, loc="outside lower center", ncol=2, fontsize=9,
           frameon=False)
save_figure(fig, "two_gamma_products", ...)
```

The key below the figure explains the two frame colours and the two entry colours. **What figure 8 shows and why:** a triangle of 28 small heat maps, the products of two of the author's real gammas, each block diagonal with 16 nonzero entries (two of every four quadrants are empty), because each is an even product. The black frames sit where both directions are of the same kind (among $x_1, x_2, x_3, x_8$, or among $x_4, \dots, x_7$), the green ones where one is space-like and one time-like. Four panels are diagonal matrices: $x_1x_6$, $x_2x_5$, $x_3x_4$ and $x_7x_8$ (Section 4.17 explains why exactly these). Half of each product is the matrix $S^{ab}$ of the Revision record.

**In [19], the last check.**

```python
names = ["04c_1_products_by_degree.png", "04c_2_multiplication_table.png",
         "04c_3_squares_by_degree.png", "04c_4_trace_products.png",
         "04c_5_coefficients.png", "04c_6_even_odd_blocks.png", "04c_7_how_big.png",
         "04c_8_two_gamma_products.png"]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in names),
      "all eight figure files exist")
all_checks_passed()
```

The eight figure files must exist; the last line reads ALL 19 CHECKS PASSED (notebook 04c): one check in each of In [2], In [10] and In [19]; two in each of In [4], In [6], In [13], In [15] and In [17]; and three in each of In [8] and In [11].

### 4.17 A second set of gammas and the one change of basis

The author's gammas are one solution of the Clifford relation. Are they special? This section builds a second set of eight real $16 \times 16$ gammas from three $2 \times 2$ matrices, with a recipe that needs nothing from the author's notebook, and proves that the two sets differ only by a renumbering of the sixteen components and some signs. It also proves that this renumbering is the only change of basis between them, and that only the multiples of $I_{16}$ commute with all eight gammas.

**Three $2 \times 2$ matrices.**

$$
P = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad N = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}, \qquad G = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

($P$ and $G$ are the $\sigma_x$ and $\sigma_z$ of Section 4.3). They are real; $P$ and $G$ are symmetric and $N$ is antisymmetric; $P^2 = G^2 = I_2$ and $N^2 = -I_2$; and any two of them anticommute: $PN = -G = -NP$, $PG = -N = -GP$, $NG = -P = -GN$. Each of these is one $2 \times 2$ multiplication; for example $PG = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = -N$ and $GP = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} = N$.

**The Kronecker product.** For a $2 \times 2$ matrix $A$ and an $m \times m$ matrix $B$, the **Kronecker product** (or tensor product) $A \otimes B$ is the $2m \times 2m$ matrix of four blocks whose block in position $(i, j)$ is $A_{ij}B$; in indices, $(A \otimes B)_{im + k,\ jm + l} = A_{ij}B_{kl}$. For example

$$
P \otimes G = \begin{pmatrix} 0 \cdot G & 1 \cdot G \\ 1 \cdot G & 0 \cdot G \end{pmatrix} = \begin{pmatrix} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & -1 \\ 1 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0 \end{pmatrix} .
$$

The **mixed-product rule** $(A \otimes B)(C \otimes D) = (AC) \otimes (BD)$ holds. Proof, line by line, for the entry in row $im + k$ and column $jm + l$:

1. $\bigl((A \otimes B)(C \otimes D)\bigr)_{im+k,\, jm+l} = \sum_{r,s} (A \otimes B)_{im+k,\, rm+s}\,(C \otimes D)_{rm+s,\, jm+l}$ — the product rule, summing over all columns $rm + s$ of the first factor.
2. $= \sum_{r,s} A_{ir}B_{ks}C_{rj}D_{sl}$ — the index formula, twice.
3. $= \bigl(\sum_r A_{ir}C_{rj}\bigr)\bigl(\sum_s B_{ks}D_{sl}\bigr)$ — the double sum of products splits into a product of two sums.
4. $= (AC)_{ij}(BD)_{kl} = \bigl((AC) \otimes (BD)\bigr)_{im+k,\, jm+l}$ — the product rule and the index formula.

In the same way $(A \otimes B)^T = A^T \otimes B^T$ (exchange $i$ with $j$ and $k$ with $l$ in the index formula). A product of four $2 \times 2$ matrices, $M_1 \otimes M_2 \otimes M_3 \otimes M_4$, is a $16 \times 16$ matrix; $M_1$ stands in **slot** 1, ..., $M_4$ in slot 4, and products are computed slot by slot. The 16 components are numbered $j = 8b_1 + 4b_2 + 2b_3 + b_4$ by four binary digits (**bits**) $b_1, \dots, b_4$, each 0 or 1, one per slot; for example $j = 5$ has the bits 0101.

**The recipe.** For a slot $k$ and $M = P$ or $N$, put $G$ into the slots before $k$, $M$ into slot $k$ and $I_2$ into the slots after $k$. Every space-like direction gets a $P$, every time-like direction an $N$, and each slot is shared by one space-like and one time-like direction. With the pairs $(x_1, x_6)$ in slot 1, $(x_2, x_5)$ in slot 2, $(x_3, x_4)$ in slot 3 and $(x_8, x_7)$ in slot 4 (why exactly these pairs is explained below):

| direction | slot 1 | slot 2 | slot 3 | slot 4 |
| --- | --- | --- | --- | --- |
| $\hat\gamma^{(x_1)}$ | $P$ | $I_2$ | $I_2$ | $I_2$ |
| $\hat\gamma^{(x_6)}$ | $N$ | $I_2$ | $I_2$ | $I_2$ |
| $\hat\gamma^{(x_2)}$ | $G$ | $P$ | $I_2$ | $I_2$ |
| $\hat\gamma^{(x_5)}$ | $G$ | $N$ | $I_2$ | $I_2$ |
| $\hat\gamma^{(x_3)}$ | $G$ | $G$ | $P$ | $I_2$ |
| $\hat\gamma^{(x_4)}$ | $G$ | $G$ | $N$ | $I_2$ |
| $\hat\gamma^{(x_8)}$ | $G$ | $G$ | $G$ | $P$ |
| $\hat\gamma^{(x_7)}$ | $G$ | $G$ | $G$ | $N$ |

for example $\hat\gamma^{(x_5)} = G \otimes N \otimes I_2 \otimes I_2$ (read "gamma hat").

**The recipe satisfies the Clifford relation.** By the mixed-product rule every product is computed slot by slot.

1. Squares: every slot is squared; $G^2 = I_2^2 = P^2 = I_2$ and $N^2 = -I_2$, so a matrix with $P$ squares to $+I_{16}$ (space-like) and one with $N$ to $-I_{16}$ (time-like).
2. The two matrices of the same slot $k$: their two products agree in every slot except slot $k$, which holds $PN$ in one order and $NP = -PN$ in the other; so they anticommute.
3. Two matrices of different slots $k < l$: compare the two orders slot by slot. Before $k$ both have $G$ ($GG = GG$); in slot $k$ the first has $P$ or $N$ and the second $G$, which anticommute (one factor $-1$); between $k$ and $l$ the first has $I_2$ and the second $G$, which commute; in slot $l$ the first has $I_2$, which commutes with everything; after $l$ both have $I_2$. Exactly one factor $-1$: they anticommute.

Each $\hat\gamma$ is a signed permutation matrix (a Kronecker product of signed permutation matrices is one: each row combines one row of each factor and so holds one nonzero product), and it has the author's symmetry pattern $(\hat\gamma^{(x_a)})^T = \eta_{aa}\hat\gamma^{(x_a)}$, because $P$, $G$ and $I_2$ are symmetric, $N$ is antisymmetric and the transpose works slot by slot. By Section 4.13 its 256 products are a basis of all real $16 \times 16$ matrices.

**The product of all eight, in both sets.** The product of the two matrices of slot $k$ is, slot by slot, $GG = I_2$ before $k$, $PN = -G$ in slot $k$ and $I_2$ after $k$: minus the matrix with $G$ in slot $k$ and $I_2$ elsewhere. The product of all eight hat gammas in the author's order, $\hat\Gamma = \hat\gamma^{(x_8)}\hat\gamma^{(x_1)}\hat\gamma^{(x_2)}\cdots\hat\gamma^{(x_7)}$, can be reordered into the pairs $(x_1, x_6), (x_2, x_5), (x_3, x_4), (x_8, x_7)$; each exchange of two neighbouring (anticommuting) factors gives a factor $-1$ and changes the number of inversions by one, so the reordering multiplies the product by the permutation sign of the reordering, which is $+1$ (Notebook 04d counts the 12 inversions). The four pair products then give $(-1)^4\, G \otimes G \otimes G \otimes G = G \otimes G \otimes G \otimes G$. Since $G = \mathrm{diag}(+1, -1)$, its diagonal entry in row $j$ is $(-1)^{b_1 + b_2 + b_3 + b_4}$: $-1$ in the eight rows $1, 2, 4, 7, 8, 11, 13, 14$, whose bits contain an odd number of ones. The author's product is $\mathrm{diag}(-I_8, I_8)$ (Section 4.5). Both have eight entries of each sign, in different rows.

**The change of basis, line by line.** Let $\gamma_A$ and $\hat\gamma_A$ be the products of the two sets for the 256 sets $A$ (Section 4.13). For any $16 \times 16$ matrix $M$ define

$$
S = \sum_A \gamma_A\, M\, \hat\gamma_A^T .
$$

1. Fix a direction $b$. By R1, $\gamma^{(b)}\gamma_A = \epsilon\,\gamma_{A'}$ with $A' = A \triangle \{b\}$ ($b$ added to $A$, or removed if it was in $A$) and a sign $\epsilon = \pm 1$ that depends only on $b$, $A$ and $\eta$. The hat gammas obey the same Clifford relation, so $\hat\gamma^{(b)}\hat\gamma_A = \epsilon\,\hat\gamma_{A'}$ with the SAME sign.
2. Both sets are signed permutation matrices, hence orthogonal: $(\hat\gamma^{(b)})^{-1} = (\hat\gamma^{(b)})^T$. From line 1, $\hat\gamma_A = \epsilon\,(\hat\gamma^{(b)})^T\hat\gamma_{A'}$, and transposing (Section 4.2), $\hat\gamma_A^T = \epsilon\,\hat\gamma_{A'}^T\hat\gamma^{(b)}$.
3. Therefore $\gamma^{(b)}S = \sum_A \epsilon\,\gamma_{A'}\, M\, \epsilon\,\hat\gamma_{A'}^T\hat\gamma^{(b)} = \bigl(\sum_A \gamma_{A'} M \hat\gamma_{A'}^T\bigr)\hat\gamma^{(b)}$ — lines 1 and 2 inserted, and $\epsilon^2 = 1$.
4. As $A$ runs through all 256 sets, $A' = A \triangle \{b\}$ runs through all 256 sets too, each exactly once (doing it twice gives $A$ back). So the sum is $S$ again: $\gamma^{(b)}S = S\hat\gamma^{(b)}$ for every $b$.

A matrix $X$ with $\gamma^{(b)}X = X\hat\gamma^{(b)}$ for every $b$ is called an **intertwiner**; $S$ is one, for every $M$.

**$S$ is orthogonal up to a factor.** Transposing $\gamma^{(b)}S = S\hat\gamma^{(b)}$ gives $S^T(\gamma^{(b)})^T = (\hat\gamma^{(b)})^T S^T$; both sets have the same symmetry pattern, so after dividing by $\eta_{bb} = \pm 1$: $S^T\gamma^{(b)} = \hat\gamma^{(b)}S^T$. Then $(S^TS)\hat\gamma^{(b)} = S^T\gamma^{(b)}S = \hat\gamma^{(b)}(S^TS)$: the matrix $S^TS$ commutes with all eight hat gammas.

**Only multiples of the identity commute with all gammas.** Suppose $X$ commutes with every $\hat\gamma^{(b)}$. Then it commutes with every product $\hat\gamma_A$ and with every combination of them, that is (Section 4.13) with every real $16 \times 16$ matrix, in particular with $E_{ij}$, the matrix with a single 1 in row $i$ and column $j$. The entry in row $k$, column $j$ of $XE_{ij}$ is $X_{ki}$; that of $E_{ij}X$ is $X_{jj}$ if $k = i$ and 0 otherwise. So $X_{ki} = 0$ for $k \neq i$, and $X_{ii} = X_{jj}$: $X = c\,I_{16}$. The same holds for the author's gammas. Applied to $S^TS$: $S^TS = c\,I_{16}$, with $c > 0$ when $S \neq 0$ (the diagonal entries of $S^TS$ are sums of squares of the columns of $S$). Then $Q = S/\sqrt{c}$ satisfies $Q^TQ = I_{16}$ and

$$
\gamma^{(x_a)} = Q\,\hat\gamma^{(x_a)}\,Q^T \qquad \text{for all eight directions}.
$$

**Unique up to a factor.** If $X$ is any intertwiner, then $Q\hat\gamma^{(b)}Q^TX = X\hat\gamma^{(b)}$; multiplying from the left by $Q^T$ gives $\hat\gamma^{(b)}(Q^TX) = (Q^TX)\hat\gamma^{(b)}$, so $Q^TX$ commutes with every hat gamma, $Q^TX = cI_{16}$, and $X = cQ$.

**What Notebook 04d finds.** With $M = E_{08}$ (the first choice that gives a nonzero $S$), $S = 16\,Q$ with a **signed permutation matrix** $Q$ ($c = 256$). Its codes, rows 0 to 15, are $+8, +4, +2, -14, -7, +11, -13, -1, -9, -5, -3, +15, -6, +10, -12, -0$; the code $+8$ in row 0 means that $(Q\chi)_0 = +\chi_8$: component 0 of the author's basis is component 8 of the tensor basis. **The author's T16 are the tensor-product gammas with the sixteen components renumbered and some of their signs flipped.** The first eight rows pick the eight tensor components with an odd number of ones in their bits, where $\hat\Gamma = -1$, which is why the author's product of all eight gammas is $\mathrm{diag}(-I_8, I_8)$. Status: PROVED (exact integer arithmetic; Notebook 04d checks $\gamma_A = Q\hat\gamma_AQ^T$ for all 256 products).

**What it means for the field equation.** In flat 4+4 space write $\Psi = Q\chi$. Then $\gamma^{(x_a)}\partial_a\Psi = Q\hat\gamma^{(x_a)}Q^TQ\,\partial_a\chi = Q\,\hat\gamma^{(x_a)}\partial_a\chi$, so $\sum_a\gamma^{(x_a)}\partial_a\Psi = m\Psi$ becomes $Q\bigl(\sum_a\hat\gamma^{(x_a)}\partial_a\chi - m\chi\bigr) = 0$, and, since $Q$ is invertible, $\sum_a\hat\gamma^{(x_a)}\partial_a\chi = m\chi$: the same equation in the other basis. The same argument applies to every equation of the book that is written with products of the gammas and numbers, because all 256 products transform with $Q$ (Notebook 04d checks them all). The choice between the two sets is a choice of how to number the sixteen components, not a choice of physics.

**Why these pairs of directions.** A signed permutation $Q$ turns a diagonal matrix $D$ into a diagonal matrix $QDQ^T$ (it only renumbers the diagonal entries and multiplies each by $(\pm 1)^2 = 1$). So if $\gamma_A = Q\hat\gamma_AQ^T$ with a signed permutation $Q$, then $\gamma_A$ is diagonal exactly when $\hat\gamma_A$ is: both sets must have their diagonal products for the same sets $A$. The author's 16 diagonal products belong to the sets made of whole pairs $(x_1, x_6)$, $(x_2, x_5)$, $(x_3, x_4)$, $(x_7, x_8)$ (Notebook 04c, In [11]); the diagonal products of the hat set belong to the sets made of whole slot pairs (the pair product of a slot is $-G$ in that slot, a diagonal matrix). So the slot pairs must be the author's pairs. With other pairs, for example $(x_1, x_4), (x_2, x_5), (x_3, x_6), (x_8, x_7)$, the Clifford relation still holds and a change of basis still exists (the argument above did not use the pairs), but it cannot be a signed permutation: Notebook 04d finds $Q_2$ with two entries $\pm 1/\sqrt2$ in every row, which mixes the components two by two.

**How strongly the equations reject every other matrix.** The equations $\gamma^{(x_a)}X - X\hat\gamma^{(x_a)} = 0$ for $a = 1, \dots, 8$ are $8 \times 256 = 2048$ linear equations for the 256 entries of $X$. Write $A$ for this system as a $2048 \times 256$ matrix, so that the sum of the squares of all 2048 left-hand sides is $v^T K v$ with $K = A^TA$, where $v$ lists the entries of $X$. $K$ has the exact eigenvectors $X_B = Q\hat\gamma_B$ for the 256 sets $B$. Line by line:

1. Write $L_a(X) = \gamma^{(a)}X - X\hat\gamma^{(a)}$ for the left-hand side of equation block $a$; $A$ is the stack of the eight blocks $L_a$, and $K = \sum_a L_a^TL_a$ (the product of a stack with its transpose adds up the products of the blocks).
2. The transpose of the block $L_a$ is the map $Y \to (\gamma^{(a)})^TY - Y(\hat\gamma^{(a)})^T$ (the rows of the system become its columns). Both sets have $(\gamma^{(a)})^T = \eta_{aa}\gamma^{(a)}$ and $(\hat\gamma^{(a)})^T = \eta_{aa}\hat\gamma^{(a)}$, so $L_a^T = \eta_{aa}L_a$ and $K = \sum_a\eta_{aa}L_aL_a$.
3. $L_a(X_B) = Q\hat\gamma^{(a)}Q^TQ\hat\gamma_B - Q\hat\gamma_B\hat\gamma^{(a)} = Q(\hat\gamma^{(a)}\hat\gamma_B - \hat\gamma_B\hat\gamma^{(a)})$ — insert $\gamma^{(a)} = Q\hat\gamma^{(a)}Q^T$ and $Q^TQ = I_{16}$. By R3 this is 0 when $\hat\gamma^{(a)}$ commutes with $\hat\gamma_B$, and $2Q\hat\gamma^{(a)}\hat\gamma_B$ when it anticommutes.
4. In the anticommuting case apply $L_a$ once more: $L_a(2Q\hat\gamma^{(a)}\hat\gamma_B) = 2Q(\hat\gamma^{(a)}\hat\gamma^{(a)}\hat\gamma_B - \hat\gamma^{(a)}\hat\gamma_B\hat\gamma^{(a)}) = 2Q(\eta_{aa}\hat\gamma_B + \eta_{aa}\hat\gamma_B) = 4\eta_{aa}X_B$ — the square is $\eta_{aa}$, and $\hat\gamma_B\hat\gamma^{(a)} = -\hat\gamma^{(a)}\hat\gamma_B$. Multiplied by the $\eta_{aa}$ of line 2 it gives $4X_B$, because $\eta_{aa}^2 = 1$.
5. Adding over $a$: $KX_B = 4n_BX_B$, where $n_B$ is the number of directions whose gamma anticommutes with $\hat\gamma_B$; by R3 these are the $k$ directions in $B$ for an even degree $k$, and the $8 - k$ directions outside $B$ for an odd $k$.

So the eigenvalues of $K$ are $0, 4, 8, \dots, 32$, with the multiplicities $\binom{8}{0}, \binom{8}{1}, \dots, \binom{8}{8}$, and the eigenvalue 0, which means "solves all 2048 equations", belongs only to $B = \{\}$, that is to $X = Q$. Because the 256 eigenvectors $X_B$ are perpendicular to each other (Section 4.13), every matrix $X$ is a combination of them, and the part of $X$ perpendicular to $Q$ raises the sum of the squared equations by at least 4 times its squared size (the sum of the squares of its entries).

**Status.** PROVED (exact integer arithmetic and exact ranks in Notebook 04d): the hat gammas satisfy the Clifford relation with the author's $\eta$ and symmetry pattern; their 256 products have rank 256; $\gamma_A = Q\hat\gamma_AQ^T$ for all 256 products with the signed permutation $Q$; the intertwiners form a space of dimension 1 (the system has the exact rank 255); and only the multiples of $I_{16}$ commute with all eight of the author's gammas, which reproduces `Revision/algebra/reports/python-algebra.json`, check `pin_commutant_dimension_1`, and `Revision/algebra/reports/wolfram-algebra.json`, check `Pin44_irreducible_commutant_dim_1`. Chapter 5 explains what this last statement means for the group Pin(4,4): the sixteen components cannot be split into smaller pieces that the reflections and rotations of the 4+4 space-time keep apart.

The next three sections hold Notebook 04d.

<!-- NOTEBOOK 04d -->

### 4.20 Line-by-line walk-through of Notebook 04d

The notebook has 18 code cells, In [1] to In [18].

**In [1], the set-up cell.** It is the set-up cell of Notebook 04a, explained line by line in Section 4.8, except for the line `NOTEBOOK_ID = "04d"` and the run instructions of Section 4.18 in its comment lines. It prints one line.

**In [2], the three $2 \times 2$ matrices.**

```python
import itertools  # all subsets of a given size, all pairs of indices
from math import comb  # comb(n, k): the binomial coefficient "n choose k"

import numpy as np  # integer matrices; their sums and products are exact
import sympy as sp  # exact ranks, computed with fractions
from matplotlib.colors import BoundaryNorm, ListedColormap
from matplotlib.patches import Patch
from sympy.polys.matrices import DomainMatrix  # exact matrices for the rank
```

The imports, as in Notebooks 04a and 04c.

```python
P = np.array([[0, 1], [1, 0]], dtype=np.int64)
N = np.array([[0, 1], [-1, 0]], dtype=np.int64)
G = np.array([[1, 0], [0, -1]], dtype=np.int64)
I2 = np.eye(2, dtype=np.int64)
for name, m in (("P", P), ("N", N), ("G", G)):
    say(f"{name} = {m.tolist()},  {name} {name} = {(m @ m).tolist()}")
```

$P$, $N$, $G$ and $I_2$ as whole-number arrays; the loop prints each matrix and its square: $PP = GG = I_2$ and $NN = -I_2$.

```python
squares = (P @ P == I2).all() and (G @ G == I2).all() and (N @ N == -I2).all()
triples = [(P, N, -G), (P, G, -N), (N, G, -P)]  # (A, B, the product A B)
# A B = C and B A = -C for each triple: the two matrices anticommute
products_ok = all((a @ b == c).all() and (b @ a == -c).all() for a, b, c in triples)
symmetry_ok = (P.T == P).all() and (G.T == G).all() and (N.T == -N).all()
check(squares and products_ok and symmetry_ok,
      "P^2 = G^2 = I2, N^2 = -I2, PN = -G, PG = -N, NG = -P, any two anticommute")
```

`triples` lists three triples $(A, B, C)$ with $AB = C$; the check requires $AB = C$ and $BA = -C$ for each (so the pairs anticommute), the squares, and the symmetry of $P$ and $G$ and antisymmetry of $N$: every rule of Section 4.17.

**In [3], the Kronecker product.**

```python
example = np.kron(P, G)  # the 4 x 4 matrix P (x) G
print("P (x) G =")
for row in example:
    print("    " + " ".join(f"{x:2d}" for x in row))
```

`np.kron(P, G)` computes $P \otimes G$ (written `P (x) G` in printed text), and the loop prints its four rows: the matrix of Section 4.17.

```python
# index formula with m = 2: (A (x) B)[2i + k, 2j + l] = A[i, j] B[k, l]
formula_ok = all(example[2 * i + k, 2 * j + l] == P[i, j] * G[k, l]
                 for i, j, k, l in itertools.product(range(2), repeat=4))
```

The index formula is checked for all 16 combinations of $i, j, k, l$ in $\{0, 1\}$.

```python
def kron4(m1, m2, m3, m4):
    """m1 (x) m2 (x) m3 (x) m4: a 16 x 16 matrix made of four 2 x 2 matrices."""
    return np.kron(np.kron(np.kron(m1, m2), m3), m4)
```

`kron4` forms $m_1 \otimes m_2 \otimes m_3 \otimes m_4$, a $16 \times 16$ matrix, by three Kronecker products in a row.

```python
generator = np.random.default_rng(12345)  # fixed seed: the same numbers every run
a1, b1, a2, b2 = (generator.integers(-3, 4, size=(2, 2)) for _ in range(4))
two_slots = (np.kron(a1, b1) @ np.kron(a2, b2) == np.kron(a1 @ a2, b1 @ b2)).all()
first = [generator.integers(-3, 4, size=(2, 2)) for _ in range(4)]  # four slots
second = [generator.integers(-3, 4, size=(2, 2)) for _ in range(4)]
four_slots = (kron4(*first) @ kron4(*second)
              == kron4(*[f @ s for f, s in zip(first, second)])).all()
check(formula_ok and two_slots and four_slots,
      "Kronecker product: index formula and mixed-product rule (2 and 4 slots)")
```

Random $2 \times 2$ matrices of whole numbers from $-3$ to 3 (fixed seed) test the mixed-product rule: with two slots, $(a_1 \otimes b_1)(a_2 \otimes b_2) = (a_1a_2) \otimes (b_1b_2)$; with four slots, slot by slot (`*first` hands the four matrices of the list to `kron4` as four arguments; `zip` pairs the slots of the two lists; the name `_` marks a loop variable that is not used).

**In [4], the eight tensor-product gammas.**

```python
record = json.loads(repository_file("Revision/algebra/gammas.json")
                    .read_text(encoding="utf-8"))
COORDINATES = record["coordinates"]  # ["x1", ..., "x8"]
eta = record["eta"]  # [1, 1, 1, -1, -1, -1, -1, 1]
gamma = [np.array(m, dtype=np.int64) for m in record["gamma"]]  # the author's
I16 = np.eye(16, dtype=np.int64)
SLOT = [1, 2, 3, 3, 2, 1, 4, 4]  # slots of x1..x8: (x1,x6) (x2,x5) (x3,x4) (x8,x7)
```

The coordinate names, the signs and the author's gammas are read from `gammas.json`. `SLOT` gives the slot of each direction $x_1, \dots, x_8$: $x_1$ and $x_6$ in slot 1, $x_2$ and $x_5$ in slot 2, $x_3$ and $x_4$ in slot 3, $x_7$ and $x_8$ in slot 4.

```python
def factor_names(slot, middle):
    """The names of the four factors: G before the slot, middle in it, I after."""
    return ["G"] * (slot - 1) + [middle] + ["I"] * (4 - slot)


MATRIX_OF = {"G": G, "P": P, "N": N, "I": I2}  # name -> 2 x 2 matrix
FACTORS = [factor_names(SLOT[a], "P" if eta[a] > 0 else "N") for a in range(8)]
hat = [kron4(*[MATRIX_OF[name] for name in FACTORS[a]]) for a in range(8)]
```

`factor_names` writes the recipe as a list of four letters: `"G"` repeated for the slots before the own slot, the letter `middle` in it, and `"I"` after it. `FACTORS` gives every direction its four letters, with `P` for a space-like and `N` for a time-like direction; `hat` turns the letters into matrices with `MATRIX_OF` and forms their Kronecker product: the eight hat gammas, in the order $x_1, \dots, x_8$.

```python
for a in range(8):
    kind = "space-like" if eta[a] > 0 else "time-like "
    print(f"hat gamma^({COORDINATES[a]})  {kind}  = " + " (x) ".join(FACTORS[a]))
check(COORDINATES == [f"x{k}" for k in range(1, 9)]
      and eta == [1, 1, 1, -1, -1, -1, -1, 1],
      "the record lists x1..x8 with eta = diag(+1, +1, +1, -1, -1, -1, -1, +1)")
```

One printed line per direction with its four factors (the table of Section 4.17). The check confirms the coordinates and signs read from the record.

**In [5], figure 1.**

```python
PAIR_ORDER = [0, 5, 1, 4, 2, 3, 7, 6]  # x1, x6, x2, x5, x3, x4, x8, x7
ROLE = ["3-space", "3-space", "3-space", "the time", "extra time", "extra time",
        "extra time", "hidden"]
CODE = {"I": 0, "G": 1, "P": 2, "N": 3}  # a number per letter, for the colours
grid = np.array([[CODE[name] for name in FACTORS[a]] for a in PAIR_ORDER])
slot_colours = ListedColormap(["#ffffff", "#c3c2b7", "#e34948", "#2a78d6"])
```

The rows of the figure are ordered by the pairs that share a slot. Every letter gets a number (`CODE`), and `grid` is the $8 \times 4$ table of these numbers; the four colours are white for $I_2$, grey for $G$, red for $P$ and blue for $N$.

```python
fig, ax = plt.subplots(figsize=(7.0, 4.8), layout="constrained")
# aspect="auto": the squares become rectangles that fill the panel
ax.imshow(grid, cmap=slot_colours, norm=BoundaryNorm([-0.5, 0.5, 1.5, 2.5, 3.5], 4),
          aspect="auto")
for row, a in enumerate(PAIR_ORDER):
    for column, name in enumerate(FACTORS[a]):
        text = "$I_2$" if name == "I" else name
        colour = "white" if name in ("P", "N") else "#0b0b0b"
        ax.text(column, row, text, ha="center", va="center", fontsize=12,
                color=colour)
```

The table is painted, and every cell gets its letter ($I_2$ typeset as mathematics), white on the dark colours and black on the light ones.

```python
ax.set_xticks(range(4), [f"slot {k}" for k in range(1, 5)])
ax.set_yticks(range(8), [f"$x_{a + 1}$ ({ROLE[a]})" for a in PAIR_ORDER])
for boundary in (1.5, 3.5, 5.5):  # lines between the four pairs
    ax.axhline(boundary, color="#0b0b0b", linewidth=1.2)
ax.grid(False)
ax.set_title("$\\hat\\gamma$ = slot 1 $\\otimes$ slot 2 $\\otimes$ slot 3 "
             "$\\otimes$ slot 4")
save_figure(fig, "slot_pattern", ...)
```

Columns and rows are labelled, black lines separate the four pairs, and the title states the recipe. **What figure 1 shows and why:** a staircase: each pair has its own slot with a red $P$ and a blue $N$, grey $G$ before it and white $I_2$ after it; this staircase is what makes all eight anticommute (Section 4.17).

**In [6], figure 2.**

```python
SIGN_COLOURS = ListedColormap(["#2a78d6", "#f0efec", "#e34948"])  # -1, 0, +1
SIGN_NORM = BoundaryNorm([-1.5, -0.5, 0.5, 1.5], SIGN_COLOURS.N)


def draw_signs(ax, matrix, title):
    """Draw a matrix with entries -1, 0, +1 as a heat map in the panel ax."""
    ax.imshow(matrix, cmap=SIGN_COLOURS, norm=SIGN_NORM)
    ax.set_title(title, fontsize=10)
    ax.set_xticks(range(0, 16, 4))
    ax.set_yticks(range(0, 16, 4))
    ax.grid(False)  # no grid lines on top of the coloured squares


def sign_legend(fig):
    """The key of the three colours, below the panels of the figure."""
    handles = [Patch(facecolor=SIGN_COLOURS(k), edgecolor="#898781", label=label)
               for k, label in enumerate(["entry -1", "entry 0", "entry +1"])]
    fig.legend(handles=handles, loc="outside lower center", ncol=3, fontsize=9,
               frameon=False)
```

The three-colour heat map and its key, as in Notebook 04a (without the numbers in the squares).

```python
fig, axes = plt.subplots(2, 4, figsize=(8.8, 5.0), layout="constrained")
for a in range(8):  # a // 4 is the row of the panel, a % 4 its column
    draw_signs(axes[a // 4, a % 4], hat[a], f"$\\hat\\gamma^{{(x_{a + 1})}}$")
sign_legend(fig)
save_figure(fig, "tensor_gammas", ...)
```

The eight hat gammas in two rows of four panels. **What figure 2 shows and why:** each is a signed permutation matrix, but the pattern differs from the author's: a $P$ or $N$ in slot $k$ exchanges components whose numbers differ in bit $k$, so the coloured squares lie on diagonals at the distance 8 (slot 1), 4 (slot 2), 2 (slot 3) or 1 (slot 4) from the main diagonal, and the factors $G$ in front flip signs ($\hat\gamma^{(x_1)}$ and $\hat\gamma^{(x_6)}$, with nothing before slot 1, show two clean diagonals at distance 8).

**In [7], the Clifford relation and the 256 products.**

```python
clifford_ok = all(
    (hat[a] @ hat[b] + hat[b] @ hat[a] == 2 * eta[a] * (a == b) * I16).all()
    for a in range(8) for b in range(8))  # (a == b) is 1 or 0
permutation_ok = all((np.count_nonzero(m, axis=0) == 1).all()
                     and (np.count_nonzero(m, axis=1) == 1).all()
                     and (np.abs(m).sum() == 16) for m in hat)
symmetry_ok = all((hat[a].T == eta[a] * hat[a]).all() for a in range(8))
check(clifford_ok and permutation_ok and symmetry_ok,
      "hat gammas: Clifford relation (64 pairs), signed permutations, symmetry")
```

The Clifford relation for all 64 ordered pairs (in arithmetic, `(a == b)` counts as 1 or 0, so `2 * eta[a] * (a == b)` is $2\eta^{ab}$); signed permutations (one nonzero per column and per row, and the absolute values add up to 16, so every nonzero is $\pm 1$); and the symmetry pattern $(\hat\gamma^{(x_a)})^T = \eta_{aa}\hat\gamma^{(x_a)}$.

```python
SETS = [s for k in range(9) for s in itertools.combinations(range(8), k)]


def product(matrices, indices):
    """The product of matrices[i] for i in indices, from left to right."""
    result = I16
    for i in indices:
        result = result @ matrices[i]
    return result


author_products = np.array([product(gamma, s) for s in SETS])  # gamma_A, 256 of them
hat_products = np.array([product(hat, s) for s in SETS])  # hat gamma_A
```

The 256 sets as in Notebook 04c; `product` multiplies the listed matrices from left to right; the 256 products of both sets are stored, each as an array of shape (256, 16, 16).

```python
def exact_rank(rows):
    """The exact rank of a list of rows of whole numbers (fractions, over QQ)."""
    matrix = DomainMatrix([[sp.ZZ(int(x)) for x in row] for row in rows],
                          (len(rows), len(rows[0])), sp.ZZ)
    return matrix.convert_to(sp.QQ).rank()


hat_rank = exact_rank(hat_products.reshape(256, 256).tolist())
report("exact rank of the 256 products of the hat gammas", hat_rank)
check(hat_rank == 256, "the 256 hat products are a basis of all real 16 x 16 matrices")
```

The exact rank of Notebook 04c, applied to the 256 hat products written as rows: 256, so they too are a basis of all real $16 \times 16$ matrices.

**In [8], the products of all eight gammas.**

```python
WOLFRAM = "Revision/algebra/reports/wolfram-algebra.json"
PYTHON = "Revision/algebra/reports/python-algebra.json"
RECORDED = {}  # report file -> {check name: the check (name, verdict, detail)}
for report_file in (WOLFRAM, PYTHON):
    text = repository_file(report_file).read_text(encoding="utf-8")
    RECORDED[report_file] = {e["name"]: e for e in json.loads(text)["checks"]}


def check_record(condition, name, *records):
    """check(condition, name) for a statement that the Revision record verified;
    records are pairs (report file, check name), each recorded as passed."""
    for report_file, check_name in records:
        entry = RECORDED[report_file].get(check_name)
        if entry is None or entry["verdict"].upper() != "PASS":
            raise AssertionError(f"{report_file} has no passed check {check_name}")
    check(condition, name)
    for report_file, check_name in records:
        print(f"     reproduces {report_file}")
        print(f"         check {check_name}")
```

The two algebra reports and the function `check_record`, as in Notebook 04a (without the set of reproduced checks).

```python
def permutation_sign(numbers):
    """+1 for an even, -1 for an odd number of inversions (pairs i < j with
    numbers[i] > numbers[j])."""
    inversions = sum(1 for i, j in itertools.combinations(range(len(numbers)), 2)
                     if numbers[i] > numbers[j])
    return -1 if inversions % 2 else 1
```

The permutation sign of Section 4.2, for lists without repetitions.

```python
PAIRS = [(0, 5), (1, 4), (2, 3), (7, 6)]  # (x1,x6) (x2,x5) (x3,x4) (x8,x7)
pair_ok = True
for slot, (s, t) in enumerate(PAIRS, start=1):
    only_g = kron4(*[G if k == slot else I2 for k in range(1, 5)])
    pair_ok &= bool((hat[s] @ hat[t] == -only_g).all())
```

For each slot (`enumerate(..., start=1)` numbers the pairs from 1), the product of its two hat gammas must be minus the matrix with $G$ in that slot and $I_2$ elsewhere.

```python
AUTHOR_ORDER = [7, 0, 1, 2, 3, 4, 5, 6]  # x8, x1, x2, ..., x7
paired_order = [a for pair in PAIRS for a in pair]  # x1, x6, x2, x5, x3, x4, x8, x7
# where each factor of the paired order stands in the author's order
positions = [AUTHOR_ORDER.index(a) for a in paired_order]
reorder_sign = permutation_sign(positions)
say(f"positions of x1, x6, x2, x5, x3, x4, x8, x7 in the author's order: {positions}")
say(f"permutation sign of the reordering: {reorder_sign:+d}")
```

`AUTHOR_ORDER` is the order of the factors in the author's product $\gamma^{(x_8)}\gamma^{(x_1)}\cdots\gamma^{(x_7)}$; `paired_order` lists the directions pair by pair; `.index(a)` finds where each stands in the author's order. The printed list of positions is $[1, 6, 2, 5, 3, 4, 0, 7]$; it has 12 inversions ($1$ before $0$; $6$ before $2, 5, 3, 4, 0$; $2$ before $0$; $5$ before $3, 4, 0$; $3$ before $0$; $4$ before $0$), an even number, so the sign is $+1$.

```python
chirality_hat = product(hat, AUTHOR_ORDER)
gggg = kron4(G, G, G, G)
bits = [format(j, "04b") for j in range(16)]  # "0000", "0001", ..., "1111"
parity = [(-1) ** b.count("1") for b in bits]  # -1 for an odd number of 1s
check(pair_ok and (chirality_hat == reorder_sign * gggg).all()
      and (np.diag(chirality_hat) == parity).all()
      and (chirality_hat == np.diag(parity)).all(),
      "hat Gamma = (sign +1) G (x) G (x) G (x) G = diag((-1)^(b1+b2+b3+b4))")
```

$\hat\Gamma$ is the product of the hat gammas in the author's order. `format(j, "04b")` writes $j$ with four binary digits, and `parity` is $(-1)$ to the number of ones. The check requires the pair products, $\hat\Gamma = (+1)\,G \otimes G \otimes G \otimes G$, and that $\hat\Gamma$ is the diagonal matrix of the parities.

```python
chirality_author = product(gamma, AUTHOR_ORDER)
say("rows with -1 on the diagonal, author: "
    f"{[j for j in range(16) if chirality_author[j, j] < 0]}")
say("rows with -1 on the diagonal, hat:    "
    f"{[j for j in range(16) if chirality_hat[j, j] < 0]}")
check_record((chirality_author == np.diag([-1] * 8 + [1] * 8)).all(),
             "author: Gamma = gamma^(x8) gamma^(x1) ... gamma^(x7) = diag(-I8, I8)",
             (WOLFRAM, "Gamma_diag"), (PYTHON, "chirality_diag"))
```

The same product of the author's gammas. The two printed lines list the rows with $-1$: 0 to 7 for the author, $1, 2, 4, 7, 8, 11, 13, 14$ for the hat set. The check confirms the author's $\mathrm{diag}(-I_8, I_8)$ and names the two Revision checks.

**In [9], figure 3.**

```python
fig, (top, bottom) = plt.subplots(2, 1, figsize=(8.0, 5.4), layout="constrained")
for ax, values, title in (
        (top, np.diag(chirality_author), "author: $\\Gamma = $ "
         "$\\gamma^{(x_8)}\\gamma^{(x_1)}\\cdots\\gamma^{(x_7)}$"),
        (bottom, np.diag(chirality_hat), "tensor picture: $\\hat\\Gamma = "
         "G \\otimes G \\otimes G \\otimes G$")):
    colours = ["#2a78d6" if v < 0 else "#e34948" for v in values]
    ax.bar(range(16), values, color=colours, width=0.7)
    ax.axhline(0.0, color="#898781", linewidth=0.8)
    ax.set_ylim(-1.4, 1.4)
    ax.set_yticks([-1, 0, 1])
    ax.set_ylabel("diagonal entry")
    ax.set_title(title, fontsize=10)
top.set_xticks(range(16))
bottom.set_xticks(range(16), [f"{j}\n{bits[j]}" for j in range(16)], fontsize=8)
bottom.set_xlabel("row number $j$ and its bits $b_1 b_2 b_3 b_4$")
save_figure(fig, "chirality_diagonals", ...)
```

Two bar charts, one above the other: the 16 diagonal entries of the author's product and of the hat product, blue for $-1$ and red for $+1$; the lower one labels every row with its number and, on a second line (`"\n"` starts a new line), its bits. **What figure 3 shows and why:** the author's diagonal is eight blue bars followed by eight red ones; the hat diagonal alternates in a pattern that follows the parity of the bits. Both have eight entries of each sign, so a renumbering of the components can turn one into the other; In [10] finds it.

**In [10], the change of basis.**

```python
def change_of_basis(products_1, products_2, i, j):
    """S = sum_A products_1[A] E_ij products_2[A]^T as one matrix product:
    products_1[:, :, i] is the table of the columns i (256 rows of 16 numbers)."""
    return products_1[:, :, i].T @ products_2[:, :, j]
```

The term $\gamma_AE_{ij}\hat\gamma_A^T$ has the entry $(\gamma_A)_{ki}(\hat\gamma_A)_{lj}$ in row $k$, column $l$ (only column $i$ of $\gamma_A$ and column $j$ of $\hat\gamma_A$ survive). `products_1[:, :, i]` is the $256 \times 16$ table whose row $A$ is column $i$ of $\gamma_A$; transposed and multiplied with the same table of the hat products for column $j$, it gives $\sum_A(\gamma_A)_{ki}(\hat\gamma_A)_{lj}$ for all $k, l$: the whole sum $S$ for $M = E_{ij}$ in one matrix product.

```python
def first_nonzero(products_1, products_2):
    """The first (i, j) in reading order with a nonzero S, and that S."""
    for i, j in itertools.product(range(16), repeat=2):
        S = change_of_basis(products_1, products_2, i, j)
        if S.any():
            return i, j, S
    raise ValueError("every S is zero")
```

`first_nonzero` tries $(i, j) = (0, 0), (0, 1), \dots$ in this order and returns the first pair with a nonzero $S$, and that $S$.

```python
i0, j0, S = first_nonzero(author_products, hat_products)
E = np.zeros((16, 16), dtype=np.int64)
E[i0, j0] = 1  # the matrix E_ij with a single 1
plain_sum = sum(author_products[t] @ E @ hat_products[t].T for t in range(256))
report("first (i, j) with a nonzero S", (i0, j0))
report("the different entries of S", sorted(set(int(x) for x in S.flatten())))
```

The first nonzero $S$ belongs to $(i, j) = (0, 8)$. As a control, `plain_sum` computes $\sum_A\gamma_AE_{08}\hat\gamma_A^T$ term by term. The entries of $S$ are $-16$, 0 and 16.

```python
c = int((S.T @ S)[0, 0])  # the factor c in S^T S = c I16
root = int(round(c ** 0.5))  # its square root, a whole number here
report("c in S^T S = c I16, and its square root", (c, root))
check((plain_sum == S).all()
      and all((gamma[a] @ S == S @ hat[a]).all() for a in range(8))
      and (S.T @ S == c * I16).all() and root * root == c,
      "S intertwines: gamma^a S = S hat gamma^a for all 8 a, and S^T S = c I16")
```

$c$ is read off the upper-left entry of $S^TS$: 256, with the square root 16 (`c ** 0.5` is the square root, `round` and `int` make it a whole number, and `root * root == c` confirms that it is exact). The check requires that the shortcut equals the plain sum, that $S$ intertwines all eight pairs of gammas, and that $S^TS = c\,I_{16}$.

```python
Q = S // root  # exact: every entry of S is a multiple of root
codes = []
for row in Q:
    column = int(np.flatnonzero(row)[0])  # the column of the nonzero entry
    codes.append(("+" if row[column] > 0 else "-") + str(column))
say("rows 0 to 15 of Q: " + " ".join(codes))
check((Q * root == S).all() and (np.count_nonzero(Q, axis=0) == 1).all()
      and (np.count_nonzero(Q, axis=1) == 1).all() and (Q.T @ Q == I16).all(),
      "Q = S / sqrt(c) is a signed permutation matrix (orthogonal)")
```

$Q = S/16$, computed exactly by whole-number division; its codes are printed, $+8\ +4\ +2\ -14\ -7\ +11\ -13\ -1\ -9\ -5\ -3\ +15\ -6\ +10\ -12\ -0$. The check confirms that the division was exact and that $Q$ is an orthogonal signed permutation matrix.

**In [11], all products, and the formula for $S$.**

```python
all_products_ok = all((author_products[t] == Q @ hat_products[t] @ Q.T).all()
                      for t in range(256))
check(all_products_ok and (chirality_author == Q @ chirality_hat @ Q.T).all(),
      "gamma_A = Q hat gamma_A Q^T for all 256 products, and Gamma = Q hat Gamma Q^T")
```

Not only the eight gammas but all 256 products, and the product of all eight, transform with $Q$.

```python
formula_ok = all((change_of_basis(author_products, hat_products, i, j)
                  == 16 * Q[i, j] * Q).all()
                 for i, j in itertools.product(range(16), repeat=2))
nonzero_positions = int(np.count_nonzero(Q))
report("positions (i, j) with a nonzero S(E_ij)", nonzero_positions)
check(formula_ok and nonzero_positions == 16,
      "S(E_ij) = 16 Q_ij Q for all 256 positions (i, j)")
```

For every one of the 256 choices $M = E_{ij}$, $S = 16\,Q_{ij}\,Q$. (Reason: $\sum_A\hat\gamma_AY\hat\gamma_A^T$ commutes with every hat gamma by the argument of Section 4.17, so it is a multiple of $I_{16}$; its trace is $\sum_A\mathrm{tr}(Y\hat\gamma_A^T\hat\gamma_A) = 256\,\mathrm{tr}\,Y$, so it is $16\,\mathrm{tr}(Y)\,I_{16}$; with $\gamma_A = Q\hat\gamma_AQ^T$ and $Y = Q^TE_{ij}$ this gives $S(E_{ij}) = 16\,\mathrm{tr}(Q^TE_{ij})\,Q = 16\,Q_{ij}\,Q$.) So $S$ is nonzero exactly at the 16 positions where $Q$ has its nonzero entries, and the first of them in reading order is $(0, 8)$, as found.

**In [12], figure 4.**

```python
fig, ax = plt.subplots(figsize=(6.0, 6.0), layout="constrained")
draw_signs(ax, Q, "$Q$: $\\gamma^{(x_a)} = Q\\,\\hat\\gamma^{(x_a)} Q^T$")
ax.set_xticks(range(16), [f"{j} ({bits[j]})" for j in range(16)], fontsize=6,
              rotation=90)
ax.set_yticks(range(16), [str(i) for i in range(16)], fontsize=8)
ax.set_xlabel("component $j$ of the tensor basis (its bits)")
ax.set_ylabel("component $i$ of the author's basis")
for i in range(16):
    j = int(np.flatnonzero(Q[i])[0])
    ax.text(j, i, f"{Q[i, j]:+d}", ha="center", va="center", color="white",
            fontsize=7)
sign_legend(fig)
save_figure(fig, "change_of_basis", ...)
```

$Q$ as a heat map; the columns are labelled with their number and bits (turned by 90 degrees), and the single nonzero entry of every row is written into its square. **What figure 4 shows and why:** sixteen coloured squares, one in each row and each column: $Q$ renumbers the components and flips some signs. The first eight rows use exactly the columns whose bits contain an odd number of ones, where $\hat\Gamma = -1$; this moves the eight entries $-1$ of $\hat\Gamma$ to the top, as in the author's $\mathrm{diag}(-I_8, I_8)$.

**In [13], only one change of basis.**

```python
def intertwiner_system(left, right):
    """The 2048 x 256 matrix of the equations left[a] X - X right[a] = 0, a = 1..8,
    for the 256 entries of X read row by row."""
    return np.vstack([np.kron(left[a], I16) - np.kron(I16, right[a].T)
                      for a in range(8)])
```

The equations $L X - X R = 0$ for the 256 entries of $X$, read row by row (entry $(k, l)$ is unknown number $16k + l$). With this numbering, $LX$ is $(L \otimes I_{16})$ times the list of unknowns: by the index formula, $(L \otimes I_{16})_{16i+j,\,16k+l} = L_{ik}\delta_{jl}$, and summing over $k, l$ against $X_{kl}$ gives $\sum_kL_{ik}X_{kj} = (LX)_{ij}$. In the same way $XR$ is $(I_{16} \otimes R^T)$ times the list: $(I_{16} \otimes R^T)_{16i+j,\,16k+l} = \delta_{ik}R_{lj}$, which gives $\sum_lX_{il}R_{lj} = (XR)_{ij}$. `np.vstack` stacks the eight blocks of 256 equations into the $2048 \times 256$ system.

```python
system = intertwiner_system(gamma, hat)  # the author's gammas and the hat gammas
commutant = intertwiner_system(gamma, gamma)  # the author's gammas on both sides
rank_system, rank_commutant = exact_rank(system.tolist()), exact_rank(
    commutant.tolist())
report("exact ranks of the two systems (2048 equations, 256 unknowns)",
       (rank_system, rank_commutant))
```

Two systems: the intertwiners from the hat gammas to the author's, and the matrices that commute with all eight of the author's gammas. Both have the exact rank 255, so each solution space has the dimension $256 - 255 = 1$ (the number of unknowns minus the number of independent equations).

```python
q_solves = not (system @ Q.reshape(256)).any()  # Q, read row by row, solves it
check(rank_system == 255 and q_solves,
      "the intertwiners form a space of dimension 1: the multiples of Q")
```

$Q$, written as a list of 256 numbers, solves the first system; with the dimension 1, the solutions are exactly the multiples of $Q$.

```python
python_detail = RECORDED[PYTHON]["pin_commutant_dimension_1"]["detail"]
wolfram_detail = RECORDED[WOLFRAM]["Pin44_irreducible_commutant_dim_1"]["detail"]
check_record(256 - rank_commutant == 1 and not (commutant @ I16.reshape(256)).any()
             and "= 1 (Fraction), 1 (sympy)" in python_detail
             and "has dimension 1" in wolfram_detail,
             "only the multiples of I16 commute with all eight author's gammas",
             (PYTHON, "pin_commutant_dimension_1"),
             (WOLFRAM, "Pin44_irreducible_commutant_dim_1"))
```

The second system has a one-dimensional solution space, and $I_{16}$ solves it: only the multiples of $I_{16}$ commute with all eight of the author's gammas. The check also requires the two Revision checks to state the dimension 1 in their own words, and names them.

**In [14], the penalty matrix.**

```python
K = system.T @ system  # 256 x 256, whole numbers
penalty = []  # 4 n_B for every set B
eigen_ok = True
for t, s in enumerate(SETS):
    k = len(s)
    n_B = k if k % 2 == 0 else 8 - k  # the number of anticommuting directions
    v = (Q @ hat_products[t]).reshape(256)  # X_B = Q hat gamma_B, row by row
    eigen_ok &= bool((K @ v == 4 * n_B * v).all())
    penalty.append(4 * n_B)
```

$K = A^TA$ is computed with whole numbers. For each set $B$ of degree $k$, $n_B$ is $k$ for even $k$ and $8 - k$ for odd $k$; the column $v$ lists the entries of $X_B = Q\hat\gamma_B$; and `eigen_ok` stays true only if $Kv = 4n_Bv$ exactly, line 5 of the derivation in Section 4.17.

```python
values = list(range(0, 33, 4))  # 0, 4, ..., 32
multiplicities = [penalty.count(v) for v in values]
numeric = np.linalg.eigvalsh(K.astype(float))  # floating-point eigenvalues
rounded = np.round(numeric).astype(int)  # nearest whole numbers
numeric_ok = np.max(np.abs(numeric - rounded)) < 1e-9 and all(
    int(np.sum(rounded == v)) == m for v, m in zip(values, multiplicities))
report("multiplicities of 0, 4, ..., 32 in K", multiplicities)
check(eigen_ok and multiplicities == [comb(8, j) for j in range(9)] and numeric_ok,
      "K = A^T A has the exact eigenvalues 4 n_B; only Q has the eigenvalue 0")
```

The multiplicities of $0, 4, \dots, 32$ are counted: $1, 8, 28, 56, 70, 56, 28, 8, 1$. As an independent control, numpy computes all 256 eigenvalues of $K$ in floating point; they must lie within $10^{-9}$ of whole numbers and come with the same multiplicities. The check requires the exact eigenvectors, the binomial multiplicities and the numerical agreement.

**In [15], figure 5.**

```python
fig, ax = plt.subplots(figsize=(7.2, 3.9), layout="constrained")
ax.set_axisbelow(True)  # grid lines behind the bars
colours = ["#eb6834" if v == 0 else "#2a78d6" for v in values]
bars = ax.bar(values, multiplicities, width=2.8, color=colours)
ax.bar_label(bars, labels=[str(m) for m in multiplicities], padding=2, fontsize=9)
ax.set_xticks(values)
ax.set_ylim(0, 80)
ax.set_xlabel("eigenvalue of $K = A^T A$ (the penalty of a candidate $X$)")
ax.set_ylabel("multiplicity")
ax.set_title("$\\gamma^{(x_a)}X - X\\hat\\gamma^{(x_a)} = 0$: one solution, $X = Q$")
save_figure(fig, "penalty_spectrum", ...)
```

A bar chart of the multiplicities against the eigenvalues, the bar of the eigenvalue 0 in orange. **What figure 5 shows and why:** one orange bar of height 1 at 0 (only $Q$ solves all 2048 equations) and blue bars of the binomial heights 8, 28, 56, 70, 56, 28, 8, 1 at 4 to 32: the part of any matrix that is perpendicular to $Q$ makes the sum of the squared equations at least 4 times its squared size.

**In [16], another way to fill the slots.**

```python
SLOT_2 = [1, 2, 3, 1, 2, 3, 4, 4]  # pairs (x1,x4) (x2,x5) (x3,x6) (x8,x7)
FACTORS_2 = [factor_names(SLOT_2[a], "P" if eta[a] > 0 else "N") for a in range(8)]
hat_2 = [kron4(*[MATRIX_OF[name] for name in FACTORS_2[a]]) for a in range(8)]
clifford_2 = all(
    (hat_2[a] @ hat_2[b] + hat_2[b] @ hat_2[a] == 2 * eta[a] * (a == b) * I16).all()
    for a in range(8) for b in range(8))
check(clifford_2 and all((hat_2[a].T == eta[a] * hat_2[a]).all() for a in range(8)),
      "second assignment: the Clifford relation and the symmetry pattern hold too")
hat_2_products = np.array([product(hat_2, s) for s in SETS])
```

The second assignment of directions to slots, with the pairs $(x_1, x_4)$, $(x_2, x_5)$, $(x_3, x_6)$, $(x_8, x_7)$; the same recipe builds `hat_2`; the check confirms the Clifford relation and the symmetry pattern; and the 256 products of the new set are formed.

```python
def diagonal_sets(products):
    """The sets A (as coordinate names) whose product is a diagonal matrix."""
    return [tuple(COORDINATES[a] for a in s) for s, m in zip(SETS, products)
            if (m == np.diag(np.diag(m))).all()]
```

`diagonal_sets` lists, as tuples of coordinate names, the sets whose product is a diagonal matrix.

```python
diagonal_author = diagonal_sets(author_products)
say("diagonal products, author:            " + ", ".join(
    "".join(n[1] for n in s) or "I" for s in diagonal_author[:5]) + ", ...")
say("diagonal products, second assignment: " + ", ".join(
    "".join(n[1] for n in s) or "I" for s in diagonal_sets(hat_2_products)[:5])
    + ", ...")
check(len(diagonal_author) == 16 and diagonal_sets(hat_products) == diagonal_author
      and diagonal_sets(hat_2_products) != diagonal_author,
      "the first assignment has the author's 16 diagonal products, the second not")
```

The first five diagonal products of each set are printed by their coordinate numbers (`n[1]` is the digit of a name such as `"x6"`; `or "I"` names the empty set): I, 16, 25, 34, 78 for the author, but I, 14, 25, 36, 78 for the second assignment. The check requires 16 diagonal products for the author, the same sets for the first hat set, and different sets for the second: by the argument of Section 4.17, no signed permutation can relate the second set to the author's.

```python
i2, j2, S_2 = first_nonzero(author_products, hat_2_products)
c_2 = int((S_2.T @ S_2)[0, 0])
report("second assignment: entries of S_2 and c_2",
       (sorted(set(int(x) for x in S_2.flatten())), c_2))
check(all((gamma[a] @ S_2 == S_2 @ hat_2[a]).all() for a in range(8))
      and (S_2.T @ S_2 == c_2 * I16).all() and c_2 == 128
      and (np.count_nonzero(S_2, axis=1) == 2).all(),
      "second assignment: S_2 intertwines, S_2^T S_2 = 128 I16, two entries per row")
Q_2 = S_2 / np.sqrt(c_2)  # floating point: the entries are +-1/sqrt(2)
```

The same formula gives a change of basis $S_2$ for the second set: entries $-8$, 0, 8, $S_2^TS_2 = 128\,I_{16}$, two nonzero entries in every row. So $Q_2 = S_2/\sqrt{128}$ has the entries $\pm 8/\sqrt{128} = \pm 1/\sqrt2$, computed in floating point: an orthogonal matrix that mixes the components in pairs, not a signed permutation.

**In [17], figure 6.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(8.8, 4.6), layout="constrained")
for ax, matrix, title in (
        (left, Q, "pairs (x1,x6) (x2,x5) (x3,x4) (x8,x7): $Q$"),
        (right, Q_2, "pairs (x1,x4) (x2,x5) (x3,x6) (x8,x7): $Q_2$")):
    image = ax.imshow(matrix, cmap="RdBu_r", vmin=-1.0, vmax=1.0)
    ax.set_title(title, fontsize=9)
    ax.set_xticks(range(0, 16, 4))
    ax.set_yticks(range(0, 16, 4))
    ax.set_xlabel("tensor component $j$")
    ax.set_ylabel("author's component $i$")
    ax.grid(False)
fig.colorbar(image, ax=[left, right], shrink=0.8, label="entry")
save_figure(fig, "two_assignments", ...)
```

$Q$ and $Q_2$ side by side with one continuous colour scale (`"RdBu_r"`: blue for $-1$, white for 0, red for $+1$; `vmin` and `vmax` fix its ends), and a colour bar explaining it. **What figure 6 shows and why:** on the left sixteen full-coloured squares, one per row and column; on the right thirty-two paler squares, two per row and column, of the size $1/\sqrt2 \approx 0.71$. Both matrices are orthogonal and both turn one set of gammas exactly into the other; only the assignment that matches the author's pairs gives a pure renumbering.

**In [18], the last check.**

```python
names = ["04d_1_slot_pattern.png", "04d_2_tensor_gammas.png",
         "04d_3_chirality_diagonals.png", "04d_4_change_of_basis.png",
         "04d_5_penalty_spectrum.png", "04d_6_two_assignments.png"]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in names),
      "all six figure files exist")
all_checks_passed()
```

The six figure files must exist; the last line reads ALL 18 CHECKS PASSED (notebook 04d): one check in each of In [2], In [3], In [4], In [14] and In [18]; two in each of In [7], In [8], In [10], In [11] and In [13]; and three in In [16].

### 4.21 What we proved, what we computed, what we assumed

**PROVED** (exact; the proof is in this chapter, the computer confirms it with exact arithmetic in the notebook named, and the Revision record checks named confirm it independently):

- The square of a linear expression $\sum_a p_a\gamma^a$ is the quadratic form $\sum_a\eta^{aa}p_a^2$ exactly when the coefficients satisfy the Clifford relation; no ordinary numbers do (Section 4.3; Notebook 04b).
- The author's formulas give six $4 \times 4$ blocks equal to the six matrices his notebook displays; they are the right (s4) and minus the left (t4) multiplications by the quaternion units, which gives all their rules; the $8 \times 8$ matrices satisfy $\tau_1\tau_2\tau_3 = \tau_4\tau_5\tau_6\tau_7 = \sigma$, $\tau_7 = \mathrm{diag}(-I_4, I_4)$, $\bar\tau_A = -\tau_A$ and the key rule; the sixteen-by-sixteen matrices T16 satisfy the Clifford relation, T16[8] $= \mathrm{diag}(-I_8, I_8)$; renamed with the coordinate map ($\gamma^{(x_8)} = $ T16[0], $\gamma^{(x_k)} = $ T16[$k$]) they satisfy $\gamma^a\gamma^b + \gamma^b\gamma^a = 2\eta^{ab}I_{16}$ with $\eta = \mathrm{diag}(+1, +1, +1, -1, -1, -1, -1, +1)$, they are real signed permutation matrices, symmetric for $x_1, x_2, x_3, x_8$ and antisymmetric for the time $x_4$ and the deflating extra times $x_5, x_6, x_7$ (Section 4.5; Notebook 04a, which reproduces 30 checks of `Revision/algebra/reports/wolfram-algebra.json` and `Revision/algebra/reports/python-algebra.json`, among them `Clifford_relation`, `clifford_relation`, `reality`, `symmetry_pattern` and `coordinate_map`, and finds all $2 \times 2048$ entries equal to those of `Revision/algebra/gammas.json` and `Revision/algebra/reports/python-gammas.json`).
- The author's gammas take the square root of the 4+4 quadratic form; plane waves of the flat equation $\sum_a\gamma^{(x_a)}\partial_a\Psi = m\Psi$ obey $E^2 = m^2 + k_1^2 + k_2^2 + k_3^2 + k_8^2 - k_5^2 - k_6^2 - k_7^2$; without extra-time momentum $h$ is Hermitian, and the record's example has the energies $\pm 5$, eight times each; with a momentum along an extra time the energies become imaginary once $k_5^2 > m^2 + k_1^2 + k_2^2 + k_3^2 + k_8^2$, with the growth rate $\sqrt{k_5^2 - m^2 - k_1^2 - k_2^2 - k_3^2 - k_8^2}$; the record's example $m = 1$, $k_5 = 2$ has $E = \pm i\sqrt3$, eight times each (Section 4.9; Notebook 04b; `Revision/theory/reports/python-field-theory.json`, checks `mode_hamiltonian_B_selfadjoint_dispersion`, `good_sector_spectrum_and_B_sectors` and `extra_time_modes_grow`; `Revision/theory/reports/python-scope.json`, check `extra_time_growth_rates_unbounded`).
- The 256 products of the gammas multiply by rule R1, square to $\pm I_{16}$ by rule R2, have trace 0 except $I_{16}$, are perpendicular in the trace sense and independent: Cl(4,4) is the set of all real $16 \times 16$ matrices; 136 products are symmetric and 120 antisymmetric; the 128 even ones span the block diagonal matrices and the 128 odd ones the block off-diagonal matrices; eight gamma matrices need at least sixteen components; $S^{ab} = \tfrac14[\gamma^a, \gamma^b] = \tfrac12\gamma^a\gamma^b$, with 12 rotation planes and 16 boost planes (Section 4.13; Notebook 04c; checks `Clifford_basis_spans_full_matrix_algebra`, `clifford_products_span_M16`, `even_subalgebra_dimension`, `even_products_span_M8_plus_M8`, `tau7_and_product`, `S_definition`, `S_half_product`, `S_real_entries_in_half_integers`).
- A second set of real gammas, built from $P$, $N$ and $G$ with Kronecker products, satisfies the same Clifford relation; the author's gammas are this set with the sixteen components renumbered and some signs flipped, $\gamma^{(x_a)} = Q\hat\gamma^{(x_a)}Q^T$ with a signed permutation $Q$; this change of basis is unique up to a factor; and only the multiples of $I_{16}$ commute with all eight of the author's gammas (Section 4.17; Notebook 04d; `Revision/algebra/reports/python-algebra.json`, check `pin_commutant_dimension_1`, and `Revision/algebra/reports/wolfram-algebra.json`, check `Pin44_irreducible_commutant_dim_1`).

**COMPUTED** (floating-point numbers, with the measured accuracy): the eigenvalues of the $2 \times 2$ roots agree with $\pm\sqrt{p^2 \pm 1}$ to $10^{-12}$; $(\sum_a p_a\gamma^{(x_a)})^2 = \eta(p, p)I_{16}$ for 300 random vectors, every deviation below $10^{-12}$ (the bound that the notebook asserts; the sizes themselves, plotted in figure 4 of Notebook 04b, depend on the computer's numerical library); the sixteen energies of the good-sector example lie within $10^{-12}$ of $\pm 5$, and the smallest singular value of $EI_{16} - h$ equals the distance to $\pm 5$ within $10^{-9}$; the $160 \times 16$ energies with a momentum $k_5$ lie within $10^{-10}$ of $\pm\sqrt{25 - k_5^2}$; the floating-point eigenvalues of the penalty matrix $K$ lie within $10^{-9}$ of $0, 4, \dots, 32$ (Notebooks 04b and 04d). Each of these confirms an exact statement proved above.

**ASSUMED**: the author's metric, the roles of his coordinates and his formulas for T16 (the input of the theory; Section 4.4 and Section 4.5); in Section 4.9, flat 4+4 space without self-interaction, a model of the algebra only, since the author's extra times deflate at every moment; and two facts of linear algebra quoted without proof (in a space of dimension $m$ any $m$ independent elements form a basis; the trace of a Hermitian matrix is the sum of its eigenvalues).

**HYPOTHESIS and OPEN**: this chapter states none. What the growing waves along the extra times mean for the curved, deflating space-time is the subject of Chapter 8. Nothing in this chapter concerns the creation of universes or matter and antimatter; the matrices it builds are used in Part V, where the honest scope of those questions is stated.

### 4.22 Exercises

**Exercise 1.** Show that the three real matrices $\sigma_x$, $\sigma_z$ and $N$ of Section 4.3 satisfy $(p\sigma_x + q\sigma_z + rN)^2 = (p^2 + q^2 - r^2)I_2$ for all $p, q, r$. Compute $\sigma_x\sigma_zN$. Then prove that no real $2 \times 2$ matrix $M$ with $M^2 = +I_2$ anticommutes with both $\sigma_x$ and $\sigma_z$, and explain why three anticommuting matrices fit into $2 \times 2$ although $2^3 = 8 > 2^2$.

*Answer.* The squares are $\sigma_x^2 = \sigma_z^2 = I_2$ and $N^2 = -I_2$. The pairs anticommute: $\sigma_z\sigma_x = -\sigma_x\sigma_z$ (Section 4.2) and $N\sigma_x = -\sigma_xN$ (Section 4.3), and $\sigma_zN = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, $N\sigma_z = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix} = -\sigma_zN$. So the general rule of Section 4.3 with the signs $(+1, +1, -1)$ gives $(p^2 + q^2 - r^2)I_2$. Next, $\sigma_x\sigma_z = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = -N$, so $\sigma_x\sigma_zN = -N^2 = I_2$. For the second part, every real $2 \times 2$ matrix is $\begin{pmatrix} \alpha & \beta \\ \gamma & \delta \end{pmatrix} = \tfrac{\alpha + \delta}{2}I_2 + \tfrac{\beta + \gamma}{2}\sigma_x + \tfrac{\alpha - \delta}{2}\sigma_z + \tfrac{\beta - \gamma}{2}N$ (check the four entries), so write $M = aI_2 + b\sigma_x + c\sigma_z + dN$. Then $\sigma_xM + M\sigma_x = 2a\sigma_x + 2bI_2 + c(\sigma_x\sigma_z + \sigma_z\sigma_x) + d(\sigma_xN + N\sigma_x) = 2a\sigma_x + 2bI_2$, which vanishes only for $a = b = 0$; in the same way $\sigma_zM + M\sigma_z = 2a\sigma_z + 2cI_2$ forces $c = 0$. So $M = dN$ and $M^2 = -d^2I_2$, never $+I_2$. Three matrices fit because $n = 3$ is odd: the trace lemma fails for the product of all three, which is $I_2$ with trace 2, so the eight products come in pairs that are equal up to sign (for example $\sigma_x\sigma_z = -N$) and only four of them are independent, $4 = 2^2$, like the seven $\tau$ of Section 4.13.

**Exercise 2.** The code table of Notebook 04a (output of In [18]) begins, for row 0, with $-15$ in the column x1 and $+14$ in the column x2; row 14 reads $-1$ (x1), row 15 reads $-0$ (x1) and $-1$ (x2). Use only these entries to show that row 0 of $(\gamma^{(x_1)})^2$ is $+u_0$ and that row 0 of $\gamma^{(x_1)}\gamma^{(x_2)}$ is minus row 0 of $\gamma^{(x_2)}\gamma^{(x_1)}$.

*Answer.* Row 0 of $\gamma^{(x_1)}$: $(\gamma^{(x_1)}v)_0 = -v_{15}$. With $v = \gamma^{(x_1)}u$ and row 15 of $\gamma^{(x_1)}$, $v_{15} = -u_0$, so $(\gamma^{(x_1)}\gamma^{(x_1)}u)_0 = -(-u_0) = +u_0$, as it must be for the space-like $x_1$. For the products: $(\gamma^{(x_1)}\gamma^{(x_2)}u)_0 = -(\gamma^{(x_2)}u)_{15} = -(-u_1) = +u_1$ (row 15 of $\gamma^{(x_2)}$ is $-1$), while $(\gamma^{(x_2)}\gamma^{(x_1)}u)_0 = +(\gamma^{(x_1)}u)_{14} = +(-u_1) = -u_1$ (row 14 of $\gamma^{(x_1)}$ is $-1$). The two differ by a sign: in row 0, the two gammas anticommute.

**Exercise 3.** How many of the 56 products of degree 3 square to $+I_{16}$, and how many to $-I_{16}$? Compare with figure 3 of Notebook 04c.

*Answer.* By rule R2 with $k = 3$, $\gamma_A^2 = (-1)^{3}\prod_{a \in A}\eta^{aa}\,I_{16} = -\prod_{a \in A}\eta^{aa}\,I_{16}$. This is $+I_{16}$ exactly when the product of the three signs is $-1$, that is when $A$ contains an odd number of time-like directions. One time-like and two space-like directions: $\binom41\binom42 = 4 \cdot 6 = 24$ sets; three time-like: $\binom43 = 4$ sets. So $24 + 4 = 28$ products square to $+I_{16}$ and $56 - 28 = 28$ to $-I_{16}$, the two equal bars at degree 3 in the figure.

**Exercise 4.** Compute the $4 \times 4$ matrix $P \otimes N$ with the index formula, and its square in two ways: with the mixed-product rule, and by following row 0 in the code notation.

*Answer.* $P \otimes N = \begin{pmatrix} 0 \cdot N & 1 \cdot N \\ 1 \cdot N & 0 \cdot N \end{pmatrix} = \begin{pmatrix} 0 & 0 & 0 & 1 \\ 0 & 0 & -1 & 0 \\ 0 & 1 & 0 & 0 \\ -1 & 0 & 0 & 0 \end{pmatrix}$. By the mixed-product rule, $(P \otimes N)^2 = P^2 \otimes N^2 = I_2 \otimes (-I_2) = -I_4$. In code notation, row 0 is $+3$ and row 3 is $-0$, so $((P \otimes N)^2u)_0 = +((P \otimes N)u)_3 = -u_0$, row 0 of $-I_4$.

**Exercise 5.** Take $m = 1$, no momentum in $x_1, x_2, x_3, x_8$, and a wave $e^{ik_{x_5}x_5}$ along the extra time $x_5$ with the coordinate momentum $k_{x_5} = 1$, at a point where $\sin z = 1/64$. Using the frame factor of Section 4.4, find the frame momentum and $E^2$ (a) when $a_4 = 0$ and (b) when $a_4 = \ln 2$. What happens to the growth rate as the extra times deflate?

*Answer.* The frame factor of $x_5$ is $e^{-a_4}\sin^{1/6} z = e^{-a_4}(1/64)^{1/6} = e^{-a_4}/2$, since $2^6 = 64$. The frame momentum is the coordinate momentum divided by it: $k_5 = 2e^{a_4}$. (a) $a_4 = 0$: $k_5 = 2$, and $E^2 = m^2 - k_5^2 = 1 - 4 = -3$, so $E = \pm i\sqrt3$: the exact example of the Revision record, with the growth rate $\sqrt3 \approx 1.73$. (b) $a_4 = \ln 2$: $e^{a_4} = 2$, $k_5 = 4$, $E^2 = 1 - 16 = -15$, growth rate $\sqrt{15} \approx 3.87$. As $a_4$ grows the extra times deflate, the frame momentum grows like $e^{a_4}$, and the growth rate grows with it. (This is the local plane-wave reading of Section 4.9, with the coefficients held fixed near the point.)

**Exercise 6.** For which of the pairs $(x_1, x_2)$, $(x_1, x_4)$, $(x_5, x_6)$, $(x_4, x_8)$ does $(2S^{ab})^2$ equal $-I_{16}$, and for which $+I_{16}$? Which are rotation planes and which boost planes? Show also that $S^{ba} = -S^{ab}$.

*Answer.* $2S^{ab} = \gamma^a\gamma^b$ for $a \neq b$ (Section 4.13), and $(\gamma^a\gamma^b)^2 = -\eta^{aa}\eta^{bb}I_{16}$. $(x_1, x_2)$: both space-like, $\eta^{aa}\eta^{bb} = +1$, square $-I_{16}$, a rotation plane. $(x_1, x_4)$: space-like and time-like, $-1$, square $+I_{16}$, a boost plane. $(x_5, x_6)$: both time-like, $(-1)(-1) = +1$, square $-I_{16}$, a rotation plane. $(x_4, x_8)$: time-like and space-like, square $+I_{16}$, a boost plane. Finally $S^{ba} = \tfrac14(\gamma^b\gamma^a - \gamma^a\gamma^b) = -\tfrac14(\gamma^a\gamma^b - \gamma^b\gamma^a) = -S^{ab}$.

**Exercise 7.** Without a computer, find the energies of the plane waves of the flat equation for $m = 3$, $(k_1, k_2, k_3, k_8) = (0, 0, 4, 0)$ and no momentum along the extra times, and how often each occurs.

*Answer.* $h^2 = (m^2 + k_3^2)I_{16} = (9 + 16)I_{16} = 25I_{16}$ (Section 4.9), so every eigenvalue is $+5$ or $-5$. Without extra-time momentum $h$ is Hermitian, and its trace is 0 (every term of $h$ is a multiple of $\gamma^{(x_4)}$ or of $\gamma^{(x_4)}\gamma^{(x_a)}$ with $a \neq x_4$, which have trace 0). With $n_+$ eigenvalues $+5$ and $n_-$ eigenvalues $-5$: $n_+ + n_- = 16$ and $5n_+ - 5n_- = 0$, so $E = +5$ and $E = -5$ occur eight times each.
