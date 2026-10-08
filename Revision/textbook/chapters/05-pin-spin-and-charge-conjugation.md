## 5. The matrices $C$, $\Gamma$ and $B$, the groups Pin(4,4) and Spin(4,4), and the charge-conjugation matrices

Chapter 4 built the author's eight real gamma matrices, one $16 \times 16$ matrix for each of the eight directions of the author's universe, and proved that they obey the Clifford relation. This chapter builds from them everything else that a field with 16 components needs before its equations can be written down: the charge matrix $C$ (which turns two spinors into a number), the chirality $\Gamma$ (which cuts the 16 components into two halves of 8), the matrix $B$ (whose bilinear is the charge density), the groups Pin(4,4) and Spin(4,4) of spinor transformations with their generators $S^{ab}$, and the two charge-conjugation matrices $\mathcal{C}_+ = C$ and $\mathcal{C}_- = \Gamma C$. It proves the author's statement that the 16 components carry an irreducible representation of Pin(4,4) that splits under Spin(4,4) into two inequivalent halves, and it answers exactly the question which group the scaled commutators $S^{ab}$ generate.

### 5.1 What this chapter does

A spinor field $\Psi$ attaches 16 numbers $\Psi_1, \dots, \Psi_{16}$ to every point of spacetime. Its field equation (Chapter 7) multiplies $\Psi$ by the gamma matrices. Four further questions must be answered before the equation can be used, and each needs one of the matrices of this chapter.

- How do we make a single number out of a spinor, a number that does not change when the eight directions are turned into each other? The answer is the **bilinear** $\Psi^\dagger C\Psi$ with the charge matrix $C$ (Sections 5.4 and 5.18).
- Which parts of a spinor stay separate under every turning of the directions? The two **chiral halves**, components 1 to 8 and 9 to 16, picked out by the chirality $\Gamma$ (Sections 5.5 and 5.13).
- What is the **charge density** of a spinor field, the quantity whose total is conserved? It is $\Psi^\dagger B\Psi$ with the matrix $B$ (Section 5.6).
- What exchanges particles and antiparticles? A **charge-conjugation matrix**. Because the author's gammas are real, plain complex conjugation does nothing to a real field and cannot exchange anything; the exchange must be made by a matrix, and there are exactly two such matrices, $\mathcal{C}_+ = C$ and $\mathcal{C}_- = \Gamma C$ (Sections 5.28 and 5.29). For the quantised field only one conjugation survives, and it reverses the mass (Section 5.34). Section 5.39 states what these exact maps do and do not say about matter and antimatter in the universe.

Between these questions stands the group theory: the groups Pin(4,4) and Spin(4,4) that act on spinors, the words irreducible and inequivalent, and what the scaled commutators $S^{ab} = \tfrac14[\gamma^a, \gamma^b]$ generate. Everything is introduced from zero: a reader who knows school algebra and the derivative of one-variable functions can follow every line.

The chapter has six worked examples, each a complete Jupyter notebook:

- Notebook 05a: the matrices $C$, $\Gamma$ and $B$ and every property that the Revision record states about them (26 checks, six figures);
- Notebook 05b: the commutants, which prove that Pin(4,4) acts irreducibly on the 16 components and that Spin(4,4) splits them into two inequivalent halves (17 checks, five figures);
- Notebook 05d: the spin transformations, rotations and boosts, the double cover and the forms kept by them (20 checks, six figures);
- Notebook 05f: what the scaled commutators generate (24 checks, six figures);
- Notebook 05c: the charge-conjugation matrices (20 checks, nine figures);
- Notebook 05e: the conjugation of the quantised field, computed on a space of $2^{16} = 65536$ quantum states (18 checks, eight figures).

They appear in this order, a, b, d, f, c, e: first the matrices, then the group theory, then charge conjugation. Every notebook is complete in itself, so you may run them in any order.

**Notation.** The author's coordinates are written $x1, \dots, x8$ (Chapter 0 writes them $x_1, \dots, x_8$): $x1$, $x2$, $x3$ are ordinary 3-space, which inflates; $x4$ is the time; $x5$, $x6$, $x7$ are the three extra times, which deflate exponentially; $x8$ is the hidden space direction. The gamma matrix of the direction $x4$ is written $\gamma^{(x4)}$, and so on. Letters $a$, $b$, $c$, $d$, $e$ stand for any of the eight directions. The flat metric of the frame is

$$
\eta = \mathrm{diag}(+1, +1, +1, -1, -1, -1, -1, +1)
$$

in the order $x1, \dots, x8$; its entry for the direction $a$ is written $\eta_{aa}$ (or $\eta^{aa}$, which is the same number). The directions with $\eta_{aa} = +1$ ($x1$, $x2$, $x3$, $x8$) are called **space-like**, those with $\eta_{aa} = -1$ ($x4$, $x5$, $x6$, $x7$) **time-like**. The symbol $1$ also stands for the $16 \times 16$ identity matrix, and $1_8$ for the $8 \times 8$ one.

### 5.2 The eight real gamma matrices

The gamma matrices are eight real $16 \times 16$ matrices $\gamma^{(x1)}, \dots, \gamma^{(x8)}$. Chapter 4 built them from the author's formulas (his matrices T16, with $\gamma^{(x8)} = \mathrm{T16}[0]$, $\gamma^{(x1)}, \dots, \gamma^{(x7)} = \mathrm{T16}[1], \dots, \mathrm{T16}[7]$) and proved the **Clifford relation**

$$
\gamma^a\gamma^b + \gamma^b\gamma^a = 2\eta^{ab}\, 1 \qquad \text{for all } a, b ,
$$

where $\eta^{ab}$ is $\eta_{aa}$ when $a = b$ and 0 when $a \neq b$. Written out, the relation says two things. For $a = b$: $\gamma^a\gamma^a = \eta_{aa} 1$, so a space-like gamma squares to $+1$ and a time-like gamma to $-1$. For $a \neq b$: $\gamma^a\gamma^b = -\gamma^b\gamma^a$, so two different gammas **anticommute** (exchanging them costs a sign). The Revision record stores the eight matrices in the file `Revision/algebra/gammas.json`, and two independent programs have checked them: `Revision/algebra/reports/python-algebra.json` (35 of 35 checks passed) and `Revision/algebra/reports/wolfram-algebra.json` (45 of 45 checks passed).

Every gamma is a **signed permutation matrix**: in each row exactly one entry is nonzero, and it is $+1$ or $-1$; the same holds in each column. Such a matrix is described completely by saying, for each row, in which column its nonzero entry stands and with which sign. The two following tables do this for all eight gammas, first the four space-like ones and then the four time-like ones. The entry $+9$ in row 1 of the column $\gamma^{(x8)}$ means: the matrix $\gamma^{(x8)}$ has the entry $+1$ in row 1 and column 9, and zeros in the other fifteen places of row 1. The tables are read off the record `Revision/algebra/gammas.json`.

| row | $\gamma^{(x1)}$ | $\gamma^{(x2)}$ | $\gamma^{(x3)}$ | $\gamma^{(x8)}$ |
| --- | --- | --- | --- | --- |
| 1 | $-16$ | $+15$ | $-14$ | $+9$ |
| 2 | $-15$ | $-16$ | $+13$ | $+10$ |
| 3 | $+14$ | $-13$ | $-16$ | $+11$ |
| 4 | $+13$ | $+14$ | $+15$ | $+12$ |
| 5 | $-12$ | $+11$ | $-10$ | $+13$ |
| 6 | $-11$ | $-12$ | $+9$ | $+14$ |
| 7 | $+10$ | $-9$ | $-12$ | $+15$ |
| 8 | $+9$ | $+10$ | $+11$ | $+16$ |
| 9 | $+8$ | $-7$ | $+6$ | $+1$ |
| 10 | $+7$ | $+8$ | $-5$ | $+2$ |
| 11 | $-6$ | $+5$ | $+8$ | $+3$ |
| 12 | $-5$ | $-6$ | $-7$ | $+4$ |
| 13 | $+4$ | $-3$ | $+2$ | $+5$ |
| 14 | $+3$ | $+4$ | $-1$ | $+6$ |
| 15 | $-2$ | $+1$ | $+4$ | $+7$ |
| 16 | $-1$ | $-2$ | $-3$ | $+8$ |

The four time-like gammas, read in the same way:

| row | $\gamma^{(x4)}$ | $\gamma^{(x5)}$ | $\gamma^{(x6)}$ | $\gamma^{(x7)}$ |
| --- | --- | --- | --- | --- |
| 1 | $-14$ | $+15$ | $+16$ | $+9$ |
| 2 | $+13$ | $+16$ | $-15$ | $+10$ |
| 3 | $+16$ | $-13$ | $+14$ | $+11$ |
| 4 | $-15$ | $-14$ | $-13$ | $+12$ |
| 5 | $+10$ | $-11$ | $-12$ | $-13$ |
| 6 | $-9$ | $-12$ | $+11$ | $-14$ |
| 7 | $-12$ | $+9$ | $-10$ | $-15$ |
| 8 | $+11$ | $+10$ | $+9$ | $-16$ |
| 9 | $+6$ | $-7$ | $-8$ | $-1$ |
| 10 | $-5$ | $-8$ | $+7$ | $-2$ |
| 11 | $-8$ | $+5$ | $-6$ | $-3$ |
| 12 | $+7$ | $+6$ | $+5$ | $-4$ |
| 13 | $-2$ | $+3$ | $+4$ | $+5$ |
| 14 | $+1$ | $+4$ | $-3$ | $+6$ |
| 15 | $+4$ | $-1$ | $+2$ | $+7$ |
| 16 | $-3$ | $-2$ | $-1$ | $+8$ |

**How to multiply two signed permutation matrices.** Let $M$ have in row $r$ the entry $s$ (a sign) in column $k$, and let $N$ have in row $k$ the entry $t$ in column $c$. The entry of $MN$ in row $r$ and column $q$ is $\sum_j M_{rj}N_{jq}$; only $j = k$ contributes, and $N_{kq}$ is nonzero only for $q = c$. So $MN$ has in row $r$ the single entry $st$ in column $c$: follow the row number through the two columns of the table and multiply the signs. For example, for $\gamma^{(x4)}\gamma^{(x4)}$: row 1 of $\gamma^{(x4)}$ points to column 14 with the sign $-$, and row 14 of $\gamma^{(x4)}$ points to column 1 with the sign $+$; so row 1 of $\gamma^{(x4)}\gamma^{(x4)}$ has the entry $(-1)(+1) = -1$ in column 1, as $\gamma^{(x4)}\gamma^{(x4)} = \eta_{x4\,x4} 1 = -1$ demands. For $\gamma^{(x8)}\gamma^{(x8)}$: row 1 points to column 9 with $+$, row 9 points back to column 1 with $+$; the product has $+1$ on the diagonal.

**Symmetric and antisymmetric.** The transpose $M^T$ of a matrix exchanges rows and columns, $(M^T)_{rc} = M_{cr}$. The table shows that $\gamma^{(x1)}$ has $-1$ in row 1, column 16, and also $-1$ in row 16, column 1: the two entries mirror each other with the same sign. In fact the four space-like gammas are **symmetric** ($M^T = M$) and the four time-like ones are **antisymmetric** ($M^T = -M$; for example $\gamma^{(x4)}$ has $-1$ in row 1, column 14 and $+1$ in row 14, column 1). In one formula:

$$
(\gamma^a)^T = \eta_{aa}\,\gamma^a .
$$

The statuses of these facts are listed in the next table. Here and in every later status table, the last column names the report file of the Revision record and the names of its checks; a report is a file in which a program has recorded every check with its name, its verdict and a detail text. The two reports `python-algebra.json` and `wolfram-algebra.json` lie in the folder `Revision/algebra/reports`.

| statement | status | where it is verified |
| --- | --- | --- |
| the Clifford relation for all 64 pairs of directions | PROVED (exact integer arithmetic) | `python-algebra.json`, checks `clifford_relation` and `clifford_relation_sympy`; `wolfram-algebra.json`, check `Clifford_relation` |
| every gamma is real and a signed permutation matrix | PROVED | `python-algebra.json`, check `reality_signed_permutations`; `wolfram-algebra.json`, checks `reality` and `signed_permutation_matrices` |
| $(\gamma^a)^T = \eta_{aa}\gamma^a$ | PROVED | `python-algebra.json` and `wolfram-algebra.json`, check `symmetry_pattern` |

Notebook 05a checks all three facts again. Everything in Sections 5.3 to 5.6 follows from the Clifford relation and the symmetry pattern alone.

### 5.3 Six rules for products of gammas

A **product of different gammas** is a product $P = \gamma^{a_1}\gamma^{a_2}\cdots\gamma^{a_k}$ of $k$ gammas of $k$ different directions $a_1, \dots, a_k$; $k$ is its **degree**. There are $2^8 = 256$ of them if we take the directions in the order $x1, \dots, x8$ and count the empty product $1$ (each direction is either in the product or not). The six rules below are used again and again in this chapter.

**Rule 1 (moving a gamma through a product).** Take a gamma $\gamma^e$ and the product $P$. Move $\gamma^e$ from the left of $P$ to its right, one factor at a time. Passing a factor $\gamma^{a_j}$ with $a_j \neq e$ costs a sign, because

$$
\gamma^e\gamma^{a_j} = -\gamma^{a_j}\gamma^e \qquad (a_j \neq e) ,
$$

which is the Clifford relation for two different directions. Passing the factor $\gamma^e$ itself costs nothing, because a matrix commutes with itself. So the sign is $-1$ to the power of the number of factors different from $e$:

$$
\gamma^e P = (-1)^{k-1}\, P\gamma^e \ \text{ if } e \text{ is one of the } k \text{ factors}, \qquad \gamma^e P = (-1)^{k}\, P\gamma^e \ \text{ if it is not.}
$$

**Rule 2 (the square of a product).** Write $P = \gamma^{a_1}P'$ with $P' = \gamma^{a_2}\cdots\gamma^{a_k}$. Then

$$
PP = \gamma^{a_1}P'\gamma^{a_1}P' .
$$

Move the second $\gamma^{a_1}$ to the left through $P'$; $P'$ has $k - 1$ factors, all different from $a_1$, so Rule 1 (read from right to left) gives

$$
PP = (-1)^{k-1}\gamma^{a_1}\gamma^{a_1}P'P' = (-1)^{k-1}\eta_{a_1a_1}\, P'P' ,
$$

where the second step is the Clifford relation $\gamma^{a_1}\gamma^{a_1} = \eta_{a_1a_1}1$. The product $P'P'$ is the square of a product of $k - 1$ different gammas, so the same step applies to it, with $k - 2$ factors to pass, and so on down to the empty product. Collecting the signs:

$$
PP = (-1)^{(k-1) + (k-2) + \dots + 1 + 0}\ \eta_{a_1a_1}\eta_{a_2a_2}\cdots\eta_{a_ka_k}\, 1 = (-1)^{k(k-1)/2}\ \eta_{a_1a_1}\cdots\eta_{a_ka_k}\, 1 ,
$$

where the last step is the sum of the numbers $0, 1, \dots, k-1$, which is $k(k-1)/2$ (write the sum forwards and backwards and add: $k$ pairs, each adding up to $k - 1$).

**Rule 3 (reversing a product).** $\gamma^{a_k}\cdots\gamma^{a_2}\gamma^{a_1} = (-1)^{k(k-1)/2}\, \gamma^{a_1}\gamma^{a_2}\cdots\gamma^{a_k}$. Proof: in the reversed product, move $\gamma^{a_1}$ from the last place to the first; it passes $k - 1$ different factors, each costing a sign. Then move $\gamma^{a_2}$ to the second place; it passes $k - 2$ factors. Continuing, the total number of sign changes is $(k-1) + (k-2) + \dots + 0 = k(k-1)/2$.

**Rule 4 (the transpose of a product).** The transpose of a product is the product of the transposes in the reverse order, $(MN)^T = N^TM^T$. With the symmetry pattern $(\gamma^a)^T = \eta_{aa}\gamma^a$ and Rule 3:

$$
P^T = (\gamma^{a_k})^T\cdots(\gamma^{a_1})^T = \eta_{a_1a_1}\cdots\eta_{a_ka_k}\ \gamma^{a_k}\cdots\gamma^{a_1} = (-1)^{k(k-1)/2}\ \eta_{a_1a_1}\cdots\eta_{a_ka_k}\ P .
$$

**Rule 5 (the trace of a product is zero).** The **trace** $\mathrm{tr}\,M$ of a square matrix is the sum of its diagonal entries; for two square matrices $\mathrm{tr}(MN) = \mathrm{tr}(NM)$, because both are $\sum_{r,c} M_{rc}N_{cr}$. Claim: every product $P$ of $k \geq 1$ different gammas has $\mathrm{tr}\,P = 0$. Proof: first find a gamma $\gamma^e$ that anticommutes with $P$. If $k$ is even, take $e$ to be one of the factors: by Rule 1 the sign is $(-1)^{k-1} = -1$. If $k$ is odd, then $k \leq 7$, so at least one of the eight directions is not a factor; take $e$ to be such a direction: the sign is $(-1)^k = -1$. Now, using $\gamma^e\gamma^e = \eta_{ee}1$ and $\eta_{ee}\eta_{ee} = 1$,

$$
\mathrm{tr}\,P = \eta_{ee}\,\mathrm{tr}(\gamma^e\gamma^e P) = \eta_{ee}\,\mathrm{tr}(\gamma^e P\gamma^e) = -\eta_{ee}\,\mathrm{tr}(\gamma^e\gamma^e P) = -\mathrm{tr}\,P .
$$

The first step inserts $\eta_{ee}\gamma^e\gamma^e = 1$; the second is $\mathrm{tr}(MN) = \mathrm{tr}(NM)$ with $M = \gamma^e$ and $N = \gamma^eP$; the third uses $P\gamma^e = -\gamma^eP$; the fourth undoes the first. A number equal to minus itself is 0.

**Rule 6 (counting eigenvalues).** An **eigenvalue** of a square matrix $M$ is a number $\lambda$ for which some column $v \neq 0$ has $Mv = \lambda v$. A $16 \times 16$ matrix has 16 eigenvalues when each is counted as often as it occurs as a root of the polynomial $\det(\lambda 1 - M)$ (its **multiplicity**), and the trace is their sum. Claim: if $MM = 1$ and $\mathrm{tr}\,M = 0$, then $M$ has the eigenvalue $+1$ eight times and $-1$ eight times. Proof: if $Mv = \lambda v$, then $v = MMv = M(\lambda v) = \lambda^2 v$, so $\lambda^2 = 1$ and $\lambda = \pm 1$. With $n_+$ eigenvalues $+1$ and $n_-$ eigenvalues $-1$: $n_+ + n_- = 16$ and $n_+ - n_- = \mathrm{tr}\,M = 0$, so $n_+ = n_- = 8$. In the same way, if $MM = -1$ and $\mathrm{tr}\,M = 0$, then $\lambda^2 = -1$, $\lambda = \pm i$, and $i(n_+ - n_-) = 0$ gives eight $+i$ and eight $-i$. In both cases the **determinant**, the product of the 16 eigenvalues, is $(+1)^8(-1)^8 = 1$ or $i^8(-i)^8 = 1$.

Applied to the gammas themselves: a space-like gamma has $\gamma\gamma = +1$ and trace 0 (Rule 5 with $k = 1$), so eight eigenvalues $+1$ and eight $-1$; a time-like gamma has eight $+i$ and eight $-i$; every gamma has determinant $+1$. Status: PROVED (by the rules above). Notebook 05a checks the squaring rule on all 255 products of degree 1 to 8 and counts the eigenvalues; Notebook 05d computes the eight determinants exactly.

### 5.4 The charge matrix C and the Dirac adjoint

**Definition.** The **charge matrix** is the product of the four space-like gammas,

$$
C = \gamma^{(x8)}\gamma^{(x1)}\gamma^{(x2)}\gamma^{(x3)} .
$$

The author calls it sigma16. It is used to make numbers out of spinors: the **Dirac adjoint** of a column $\Psi$ is the row $\bar\Psi = \Psi^\dagger C$, where $\Psi^\dagger$ is the row of the complex conjugates of the components of $\Psi$, and the **scalar** of the field is

$$
S = \bar\Psi\Psi = \Psi^\dagger C\Psi = \sum_{r,c}\Psi_r^{\ast} C_{rc}\Psi_c .
$$

Section 5.18 proves that $S$ does not change when the directions are turned by any element of Spin(4,4); this is why $C$, and not the identity matrix, stands between $\Psi^\dagger$ and $\Psi$. Here are its properties, each derived from Section 5.3.

**(C1) How C moves past a gamma: $C\gamma^a = -\eta_{aa}\gamma^aC$.** $C$ is a product of $k = 4$ different gammas. If $a$ is space-like, $\gamma^a$ is one of its factors, and Rule 1 gives $\gamma^aC = (-1)^{3}C\gamma^a = -C\gamma^a$. If $a$ is time-like, it is not a factor, and Rule 1 gives $\gamma^aC = (-1)^4C\gamma^a = C\gamma^a$. Both cases read $\gamma^aC = -\eta_{aa}C\gamma^a$. Multiplying this by $-\eta_{aa}$ and using $\eta_{aa}\eta_{aa} = 1$ gives the claim. So $C$ anticommutes with the four space-like gammas and commutes with the four time-like ones.

**(C2) C is symmetric.** Rule 4 with $k = 4$ and four space-like factors: $C^T = (-1)^{6}(+1)^4\, C = C$.

**(C3) $CC = 1$.** Rule 2 with $k = 4$: $CC = (-1)^{6}(+1)^4\,1 = 1$. So $C$ is its own inverse, $C^{-1} = C$.

**(C4) Every $C\gamma^a$ is antisymmetric.** Line by line:

$$
(C\gamma^a)^T = (\gamma^a)^T C^T = \eta_{aa}\gamma^a C = \eta_{aa}(-\eta_{aa})\,C\gamma^a = -C\gamma^a .
$$

The first step is $(MN)^T = N^TM^T$; the second uses the symmetry pattern and (C2); the third is (C1) in the form $\gamma^aC = -\eta_{aa}C\gamma^a$; the fourth is $\eta_{aa}\eta_{aa} = 1$.

**(C5) $C\gamma^aC^{-1} = -(\gamma^a)^T$.** With $C^{-1} = C$ from (C3):

$$
C\gamma^aC = (-\eta_{aa}\gamma^aC)\,C = -\eta_{aa}\gamma^a\,CC = -\eta_{aa}\gamma^a = -(\gamma^a)^T .
$$

The first step is (C1), the second regroups the product, the third is (C3), the fourth is the symmetry pattern.

**(C6) C has signature (8, 8).** By Rule 5, $\mathrm{tr}\,C = 0$; with $CC = 1$, Rule 6 gives eight eigenvalues $+1$ and eight $-1$. For a real symmetric matrix the pair (number of positive eigenvalues, number of negative eigenvalues) is called its **signature**; $C$ has signature $(8, 8)$. This means that the **quadratic form** $u^TCu = \sum_{r,c}u_rC_{rc}u_c$ of a real column $u$ takes both signs. Example (Notebook 05a, section 7): the table of Section 5.6 shows $C_{1,5} = C_{5,1} = -1$. For $u(t) = \cos t\, e_1 + \sin t\, e_5$, where $e_r$ is the column with 1 in row $r$ and 0 elsewhere, only these two entries meet two nonzero components, and

$$
u^TCu = 2\cos t\,\sin t\; C_{1,5} = -\sin 2t ,
$$

by the double-angle formula $2\sin t\cos t = \sin 2t$. At $t = \pi/4$ the form is $-1$; with the components 9 and 13, where $C_{9,13} = +1$, it is $+1$. The ordinary squared length $u^Tu = \cos^2t + \sin^2t = 1$ never changes sign; the form of $C$ does.

**(C7) The shape of C.** The table of Section 5.6 shows $C = \mathrm{diag}(-\sigma, \sigma)$, the block matrix with $-\sigma$ in the top left, $+\sigma$ in the bottom right and zeros elsewhere, where $\sigma$ is the author's $8 \times 8$ matrix with the $4 \times 4$ identity in its two off-diagonal blocks:

$$
\sigma = \begin{pmatrix} 0 & 1_4 \\ 1_4 & 0 \end{pmatrix} .
$$

**Consequences for the bilinears.** The **currents** of the field are $J^a = -i\bar\Psi\gamma^a\Psi = \Psi^\dagger(-iC\gamma^a)\Psi$. By (C4), $C\gamma^a$ is real and antisymmetric, so the matrix $-iC\gamma^a$ is **Hermitian** (equal to its conjugate transpose): $(-iC\gamma^a)^\dagger = (+i)(C\gamma^a)^T = -iC\gamma^a$. A Hermitian matrix $K$ gives a real number $\Psi^\dagger K\Psi$ for every complex column $\Psi$ of ordinary numbers (its complex conjugate is $\Psi^\dagger K^\dagger\Psi$, the same number). $C$ is real and symmetric, hence Hermitian too, so $S$ and the eight currents are real.

| statement | status | where it is verified |
| --- | --- | --- |
| $C = \gamma^{(x8)}\gamma^{(x1)}\gamma^{(x2)}\gamma^{(x3)}$, the author's sigma16, equal to $\mathrm{diag}(-\sigma, \sigma)$ | PROVED | `wolfram-algebra.json`, check `C_definition`; `python-algebra.json`, check `C_equals_notebook_sigma16` |
| (C2), (C3): $C^T = C$ and $CC = 1$ | PROVED | `python-algebra.json`, check `C_real_symmetric_involution`; `wolfram-algebra.json`, checks `C_real_symmetric` and `C_squared_identity` |
| (C4): every $C\gamma^a$ is antisymmetric | PROVED | `python-algebra.json`, check `C_gamma_antisymmetric`; `wolfram-algebra.json`, check `C_gamma_real_antisymmetric` |
| (C5): $C\gamma^aC^{-1} = -(\gamma^a)^T$ | PROVED | `python-algebra.json`, check `C_conjugation`; `wolfram-algebra.json`, check `C_gamma_C_inverse` |
| (C1) and (C6): the commutation signs, the signature $(8, 8)$, the form along two paths | PROVED above; COMPUTED in Notebook 05a (exactly, and to $10^{-14}$ for the form) | Notebook 05a, its sections 6 and 7 (the notebook's own computation) |

Notebook 05a re-checks every row of this table.

### 5.5 The chirality and the two halves

**Definition.** The **chirality** is the product of all eight gammas in the author's order,

$$
\Gamma = \gamma^{(x8)}\gamma^{(x1)}\gamma^{(x2)}\gamma^{(x3)}\gamma^{(x4)}\gamma^{(x5)}\gamma^{(x6)}\gamma^{(x7)} .
$$

(The author calls it T16[8]; the label 8 is a name, not a ninth direction.) Its properties:

**(X1) $\Gamma\Gamma = 1$.** Rule 2 with $k = 8$, four space-like and four time-like factors: $\Gamma\Gamma = (-1)^{28}(+1)^4(-1)^4\,1 = 1$.

**(X2) $\Gamma$ anticommutes with every gamma.** Every direction is one of the eight factors, so Rule 1 gives $\gamma^a\Gamma = (-1)^{7}\Gamma\gamma^a = -\Gamma\gamma^a$.

**(X3) $\Gamma$ commutes with every product of an even number of gammas and anticommutes with every product of an odd number.** Moving $\Gamma$ through a product of $j$ gammas (different or not) passes $j$ factors, each costing a sign by (X2): $\Gamma E = (-1)^j E\Gamma$. A product of an even number of gammas is called **even**, one of an odd number **odd**.

**(X4) $\Gamma = C\gamma^{(x4)}\gamma^{(x5)}\gamma^{(x6)}\gamma^{(x7)}$.** The first four factors of $\Gamma$ are $C$.

**(X5) $C\Gamma = \Gamma C$.** $C$ is even (four factors); use (X3).

**(X6) $\Gamma$ is symmetric.** Rule 4 with $k = 8$: $\Gamma^T = (-1)^{28}(+1)^4(-1)^4\,\Gamma = \Gamma$.

**(X7) $\Gamma^TC\Gamma = C$.** Line by line: $\Gamma^TC\Gamma = \Gamma C\Gamma$ by (X6); $= C\Gamma\Gamma$ by (X5); $= C$ by (X1).

**(X8) $\Gamma^TC\gamma^a\Gamma = -C\gamma^a$ for every $a$.** Line by line: $\Gamma^TC\gamma^a\Gamma = \Gamma C\gamma^a\Gamma$ by (X6); $= C\Gamma\gamma^a\Gamma$ by (X5); $= -C\gamma^a\Gamma\Gamma$ by (X2); $= -C\gamma^a$ by (X1).

**(X9) $\Gamma = \mathrm{diag}(-1_8, 1_8)$.** For the author's gammas the product is diagonal: $-1$ on the first eight diagonal places and $+1$ on the last eight (the table of Section 5.6, column $\Gamma$: row $r$ points to column $r$, with the sign $-$ for $r \leq 8$). This agrees with Rule 6: eight eigenvalues $-1$ and eight $+1$.

**The chiral projectors.** A **projector** is a matrix with $PP = P$. Put

$$
P_- = \tfrac12(1 - \Gamma), \qquad P_+ = \tfrac12(1 + \Gamma) .
$$

Then, multiplying out and using (X1),

$$
P_-P_- = \tfrac14(1 - 2\Gamma + \Gamma\Gamma) = \tfrac14(2 - 2\Gamma) = P_- ,
$$

and in the same way $P_+P_+ = P_+$, while $P_-P_+ = \tfrac14(1 - \Gamma\Gamma) = 0$ and $P_- + P_+ = 1$. By (X9), $P_- = \mathrm{diag}(1_8, 0)$ keeps the components 1 to 8 of a column and sets the others to zero, and $P_+ = \mathrm{diag}(0, 1_8)$ keeps the components 9 to 16. These are the two **chiral halves**: on the first half $\Gamma = -1$, on the second $\Gamma = +1$.

**Every gamma exchanges the halves.** Using (X2),

$$
\gamma^aP_- = \tfrac12(\gamma^a - \gamma^a\Gamma) = \tfrac12(\gamma^a + \Gamma\gamma^a) = P_+\gamma^a .
$$

So if a column $\Psi$ lives in the first half ($P_-\Psi = \Psi$), then $\gamma^a\Psi = \gamma^aP_-\Psi = P_+\gamma^a\Psi$ lives in the second half, and the same with the halves exchanged. In the table of Section 5.2 this is visible: in every gamma, rows 1 to 8 point to columns 9 to 16 and rows 9 to 16 to columns 1 to 8.

**The block rule.** Cut a $16 \times 16$ matrix into four $8 \times 8$ blocks, $M = \begin{pmatrix} W & X \\ Y & Z \end{pmatrix}$. With $\Gamma = \mathrm{diag}(-1_8, 1_8)$, multiplying from the left changes the sign of the top rows and from the right the sign of the left columns:

$$
\Gamma M = \begin{pmatrix} -W & -X \\ Y & Z \end{pmatrix}, \qquad M\Gamma = \begin{pmatrix} -W & X \\ -Y & Z \end{pmatrix} .
$$

So $M$ commutes with $\Gamma$ exactly when $X = Y = 0$ (**block diagonal**), and anticommutes with it exactly when $W = Z = 0$ (**block off-diagonal**). With (X3): every even product of gammas is block diagonal and every odd one block off-diagonal.

**Why (X7) and (X8) matter.** Map a field $\Psi$ to $\Gamma\Psi$. Because $\Gamma$ is real, $(\Gamma\Psi)^\dagger = \Psi^\dagger\Gamma^T$, and so

$$
(\Gamma\Psi)^\dagger C(\Gamma\Psi) = \Psi^\dagger\Gamma^TC\Gamma\Psi = \Psi^\dagger C\Psi ,
$$

by (X7): the scalar $S$ is unchanged. By (X8) every bilinear $\Psi^\dagger C\gamma^a\Psi$ changes its sign, and so does every $\Psi^\dagger C\gamma^aE\Psi$ with an even product $E$ (move $\Gamma$ through $E$ first, which costs nothing). The kinetic term of the Lagrangian of Chapter 7 is of this form, so the map $\Psi \to \Gamma\Psi$ keeps the mass term and reverses the kinetic term. These matrix identities are the input of the pairing theorem T1, which Chapter 18 proves: the map $\Gamma$ carries the solutions with the parameters $(m, \lambda)$ to the solutions with $(-m, -\lambda)$. T1 is an exact map between two sets of solutions; it does not say that anything is created (Chapter 20).

| statement | status | where it is verified |
| --- | --- | --- |
| (X9): $\Gamma = \mathrm{diag}(-1_8, 1_8)$, the author's T16[8] | PROVED | `python-algebra.json`, check `chirality_diag`; `wolfram-algebra.json`, checks `Gamma_definition` and `Gamma_diag` |
| (X1), (X2): $\Gamma\Gamma = 1$, and $\Gamma$ anticommutes with every gamma | PROVED | `python-algebra.json`, check `chirality_anticommutes`; `wolfram-algebra.json`, check `Gamma_anticommutes_with_gammas` |
| (X4): $\Gamma = C\gamma^{(x4)}\gamma^{(x5)}\gamma^{(x6)}\gamma^{(x7)}$ | PROVED | `python-algebra.json`, check `chirality_eq_C_times_time_gammas` |
| (X5) to (X8) | PROVED | `python-algebra.json`, check `chirality_C_relation`; `wolfram-algebra.json`, check `Gamma_commutes_with_C` |
| every gamma exchanges the two halves | PROVED | `python-algebra.json`, check `reflections_exchange_halves`; `wolfram-algebra.json`, check `Spin_Pin_reflection_swaps_halves` |

Notebook 05a re-checks every row of this table.

### 5.6 The matrix B and the charge density

**Definition.** $B = -i\,C\gamma^{(x4)} = -i\,\gamma^{(x8)}\gamma^{(x1)}\gamma^{(x2)}\gamma^{(x3)}\gamma^{(x4)}$, where $i$ is the imaginary unit ($i^2 = -1$).

**(B1) B is purely imaginary.** $C\gamma^{(x4)}$ is a product of real matrices, so it is real, and $B$ is $-i$ times it.

**(B2) B is Hermitian.** The conjugate transpose of $B$ conjugates the number $-i$ to $+i$ and transposes the real matrix:

$$
B^\dagger = (+i)\,(C\gamma^{(x4)})^T = (+i)(-C\gamma^{(x4)}) = -i\,C\gamma^{(x4)} = B ,
$$

where the second step is (C4) for $a = x4$.

**(B3) $BB = 1$.** First $BB = (-i)^2\,(C\gamma^{(x4)})(C\gamma^{(x4)}) = -(C\gamma^{(x4)})^2$. The matrix $C\gamma^{(x4)}$ is the product of the five different gammas of $x8, x1, x2, x3, x4$, four space-like and one time-like, so Rule 2 gives $(C\gamma^{(x4)})^2 = (-1)^{10}(+1)^4(-1)\,1 = -1$. Hence $BB = -(-1) = 1$.

**(B4) B has signature (8, 8).** By Rule 5 (with $k = 5$) $\mathrm{tr}\,B = 0$, and with $BB = 1$ Rule 6 gives eight eigenvalues $+1$ and eight $-1$; the characteristic polynomial is $\det(\lambda 1 - B) = (\lambda - 1)^8(\lambda + 1)^8$. As $B$ is Hermitian, the number $\Psi^\dagger B\Psi$ is real for every complex column, and it takes both signs.

**(B5) B commutes with five gammas and anticommutes with three.** Rule 1 with the five factors $x8, x1, x2, x3, x4$: a gamma among them passes four others, sign $(-1)^4 = +1$; a gamma not among them ($x5$, $x6$, $x7$) passes five, sign $(-1)^5 = -1$. The number $-i$ commutes with every matrix. So $B$ commutes with $\gamma^{(x1)}, \gamma^{(x2)}, \gamma^{(x3)}, \gamma^{(x4)}, \gamma^{(x8)}$ and anticommutes with the gammas of the three extra times.

**What B is for.** The time component of the current of Section 5.4 is

$$
J^{(x4)} = \Psi^\dagger(-iC\gamma^{(x4)})\Psi = \Psi^\dagger B\Psi ,
$$

the **charge density** of the field. The Revision record proves that the total charge

$$
Q = \int \cos z\; \Psi^\dagger B\Psi\; d^7x
$$

does not change in time for every solution of the field equation. Here the integral runs over the seven directions other than the time, $z = 6Hx8$, and $\cos z$ is the volume factor of the author's metric; the status table at the end of this section names the check, and Chapter 21 derives it. Because $B$ has eight positive and eight negative eigenvalues, the charge density can be positive or negative: the field can carry charge of both signs. In the quantum theory $B$ is the matrix of the canonical anticommutator, and its indefinite signature forces an indefinite (Krein) inner product (Section 5.34 and Chapter 10).

**The matrices $C$, $\Gamma$, $B$ and $\Gamma C$ in one table.** Each is a signed permutation matrix (for $B$, after division by $i$); the table is read like the one of Section 5.2. $C$, $\Gamma$ and $B$ are stored in the record `Revision/algebra/gammas.json`; $\Gamma C$ (the charge-conjugation matrix $\mathcal{C}_-$ of Section 5.28) is $C$ with the signs of rows 1 to 8 reversed, as Notebook 05c computes.

| row | $C$ | $\Gamma$ | $B/i$ | $\Gamma C$ |
| --- | --- | --- | --- | --- |
| 1 | $-5$ | $-1$ | $+10$ | $+5$ |
| 2 | $-6$ | $-2$ | $-9$ | $+6$ |
| 3 | $-7$ | $-3$ | $-12$ | $+7$ |
| 4 | $-8$ | $-4$ | $+11$ | $+8$ |
| 5 | $-1$ | $-5$ | $-14$ | $+1$ |
| 6 | $-2$ | $-6$ | $+13$ | $+2$ |
| 7 | $-3$ | $-7$ | $+16$ | $+3$ |
| 8 | $-4$ | $-8$ | $-15$ | $+4$ |
| 9 | $+13$ | $+9$ | $+2$ | $+13$ |
| 10 | $+14$ | $+10$ | $-1$ | $+14$ |
| 11 | $+15$ | $+11$ | $-4$ | $+15$ |
| 12 | $+16$ | $+12$ | $+3$ | $+16$ |
| 13 | $+9$ | $+13$ | $-6$ | $+9$ |
| 14 | $+10$ | $+14$ | $+5$ | $+10$ |
| 15 | $+11$ | $+15$ | $+8$ | $+11$ |
| 16 | $+12$ | $+16$ | $-7$ | $+12$ |

Reading the table: $C$ maps row 1 to column 5 with the sign $-$, so $C_{1,5} = -1$, the entry used in (C6); $B/i$ has $+10$ in row 1 and $-1$ in row 10, so $B_{1,10} = +i$ and $B_{10,1} = -i = (B_{1,10})^{\ast}$, as a Hermitian matrix requires; $\Gamma C$ has $+\sigma$ in both diagonal blocks.

| statement | status | where it is verified |
| --- | --- | --- |
| (B1): $B = -iC\gamma^{(x4)}$ is purely imaginary | PROVED | `wolfram-algebra.json`, checks `B_definition` and `B_purely_imaginary` |
| (B2) to (B4): $B$ is Hermitian, $BB = 1$, $\mathrm{tr}\,B = 0$, characteristic polynomial $(\lambda - 1)^8(\lambda + 1)^8$ | PROVED | `python-algebra.json`, check `B_hermitian_involution_signature`; `wolfram-algebra.json`, checks `B_Hermitian`, `B_squared_identity` and `B_signature_8_8` |
| (B5): the commutation signs of $B$ | PROVED | `python-algebra.json`, check `B_gamma_relations` |
| the total charge $Q$ is conserved | PROVED in the record (derived in Chapter 21) | `Revision/lead_checks/reports/charge-conjugation-and-u1.json`, check `u1_noether_matrix_identity` |

Notebook 05a re-checks the first three rows.

### 5.7 Example: Notebook 05a checks C, Γ and B

Notebook 05a reads the eight gammas from the record `Revision/algebra/gammas.json` as exact whole numbers and checks, one by one, every statement of Sections 5.2 to 5.6. It reads the two reports of the record and, for every check that repeats a recorded check, prints a second line naming the report file and the check. It tests the squaring rule of Section 5.3 on all 255 products of different gammas, evaluates the quadratic form of $C$ along two paths, computes the characteristic polynomial of $B$ exactly with sympy, counts the eigenvalues of all eleven matrices and draws six teaching figures: heat maps of $C$ and $\sigma$, the two values of the quadratic form, heat maps of $\Gamma$, its projectors and $\gamma^{(x1)}$, heat maps of the matrices that make $B$, the table of eigenvalue counts and the table of commutation signs. Its last line is ALL 26 CHECKS PASSED (notebook 05a).

<!-- NOTEBOOK 05a -->

### 5.10 Line-by-line walk-through of Notebook 05a

The notebook has 23 code cells, In [1] to In [23]. This section explains every line of every one of them. The words used are those of the notebook's section 3 (matrix, product, transpose, eigenvalue, signature, heat map and so on), which Sections 5.2 to 5.6 defined.

**In [1], the set-up cell.** It is the same in every notebook of the book; only the line that sets `NOTEBOOK_ID` differs. Its first part repeats the complete run instructions of Section 5.8 as comment lines: every line that starts with `#` is a **comment**, which Python skips. The code starts after the line THE SET-UP between two lines of `=` signs. (The function definitions in the cell also carry **docstrings**, texts in triple quotes below the `def` line that say what the function does; they are left out of the quotations here.)

```python
import json  # reads and writes JSON files (text files that hold names and numbers)
import os  # reads the environment variable TEXTBOOK_OUTPUT_ROOT (explained below)
import textwrap  # breaks long printed text into lines of at most 89 characters
from pathlib import Path  # file and folder paths that work on Windows, macOS and Linux

import matplotlib  # the plotting package
import matplotlib.pyplot as plt  # its drawing functions, called plt by convention
from IPython.display import Image, display  # shows a saved picture below a cell
```

`import` loads a **module** (a part of Python or of an installed package) so that the code can use it. `json`, `os`, `textwrap` and `pathlib` come with Python; `from pathlib import Path` takes the single name `Path` out of `pathlib`. A `Path` is the address of a file or folder, written the same way on every operating system. The plotting package matplotlib is loaded together with its drawing functions under the short name `plt`, and `Image` and `display` come from IPython, the part of Jupyter that runs Python code; together they show a saved picture below a cell.

```python
NOTEBOOK_ID = "05a"  # this notebook: chapter 05, example a
```

A **variable** is a name for a value. This line gives the name `NOTEBOOK_ID` to the **string** (a text in quotes) `"05a"`. The figure files and the last line of the notebook use it.

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

`def` defines a **function**, a named piece of code that runs when it is called. `Path.cwd()` is the folder in which the notebook runs, and `.resolve()` writes it as a complete address. `here.parents` lists the parent folder, its parent and so on; `[here, *here.parents]` is the list that starts with `here` and continues with all of them. The `for` loop takes the folders one after the other; `/` joins a folder and a name into a longer path, and `.is_file()` is true when that file exists. The first folder that holds `Revision/textbook/requirements.txt` is the repository, and `return` hands it back. If there is none, `raise` stops the notebook with a `FileNotFoundError` whose message says what to do.

```python
REPO = find_repository_root()
OUTPUT_ROOT = Path(os.environ.get("TEXTBOOK_OUTPUT_ROOT", str(REPO)))
```

The first line calls the function and names its result `REPO`; it is never printed, because it differs from computer to computer while the printed output of a notebook must not. The second line chooses the folder below which files are written. `os.environ` holds the **environment variables** (named texts that a program receives from the computer); `.get(name, default)` returns the value of `TEXTBOOK_OUTPUT_ROOT` if it is set and the repository folder otherwise. When you run the notebook the variable is not set; the book's checking tool sets it to a scratch folder, so that a check never changes the repository.

```python
def repository_file(relative):
    return REPO / relative


def output_file(relative):
    path = OUTPUT_ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    return path
```

`repository_file("Revision/...")` is the full path of a repository file, for reading a Revision record. `output_file("Revision/...")` is the full path at which to write a file; `path.parent.mkdir(parents=True, exist_ok=True)` first creates its folder (and any missing folder above it) and does nothing if it exists.

```python
def say(text):
    print(textwrap.fill(str(text), width=89, subsequent_indent="    "))
```

`say` prints a text in lines of at most 89 characters, the width of a page of the book; `textwrap.fill` breaks the text at blanks, and every line after the first starts with four blanks.

```python
matplotlib.rcdefaults()  # ignore personal matplotlib settings: same figures everywhere
plt.rcParams.update({"figure.figsize": (7.0, 4.2), "font.size": 10.0,
                     "axes.grid": True, "grid.alpha": 0.3})
```

`matplotlib.rcdefaults()` returns to the built-in settings of matplotlib, so that the figures are the same on every computer. `plt.rcParams.update({...})` then sets the size of a figure (7.0 by 4.2 inches), the size of its letters (10 points) and a faint grid behind the curves. The braces make a **dictionary**: pairs `key: value`.

```python
FIGURE_FOLDER = "Revision/textbook/figures"  # where the figures are saved
CAPTION_FILE = f"{FIGURE_FOLDER}/{NOTEBOOK_ID}.captions.json"  # their captions
FIGURE_NUMBERS = {}  # figure name -> its number k (file name <id>_<k>_<name>.png)
CAPTIONS = {}  # figure file name -> caption, written to CAPTION_FILE after every figure
output_file(CAPTION_FILE).write_text("{}\n", encoding="utf-8", newline="\n")
```

A string that starts with `f` is an **f-string**: each name in braces is replaced by its value, so `CAPTION_FILE` is `"Revision/textbook/figures/05a.captions.json"`. `FIGURE_NUMBERS` and `CAPTIONS` start as empty dictionaries. The last line writes an empty dictionary `{}` and a line end into the captions file, which `save_figure` then fills; `encoding="utf-8"` fixes how letters are stored and `newline="\n"` stores the same line end on every system.

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

`setdefault(name, value)` returns the number already stored for this figure name, or stores and returns one more than the number of figures so far; so the figures are numbered 1, 2, 3, and a cell run twice keeps its number. The file name joins the notebook id, the number and the name, for example `05a_1_c_matrix.png`. `fig.savefig` writes the picture as a PNG file with 150 dots per inch, cuts away the empty margin and stores no program name, so that two runs write the same bytes. `plt.close(fig)` removes the figure from memory, because Jupyter would otherwise draw it a second time. The caption is stored and the whole dictionary is written to the captions file (`json.dumps` turns it into JSON text with sorted keys). `display(Image(...))` shows the saved picture below the cell, and the last line prints where it was saved.

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

`PASSED` is an empty **list**, an ordered collection written with square brackets. `check` is the function behind every check of the book. `condition` is either `True` or `False`; if it is false, `raise AssertionError(...)` stops the notebook with an error that names the check (Python's own statement `assert` is not used, because Python started with the option `-O` skips it). If it is true, the name is appended to `PASSED` and the line PASS name is printed; when the optional third argument names a Revision record, a second line says which record and check the result reproduces.

```python
def report(label, value, unit=""):
    say(f"RESULT {label} = {value}" + (f" {unit}" if unit else ""))


def all_checks_passed():
    print(f"ALL {len(PASSED)} CHECKS PASSED (notebook {NOTEBOOK_ID})")


say(f"Set-up of notebook {NOTEBOOK_ID} complete: repository folder found, helpers "
    "defined.")
```

`report` prints a key number as a line that starts with RESULT, followed by the unit when one is given. `all_checks_passed` prints the last line of the notebook with the number of checks that passed (`len` is the length of a list). The last statement prints the single output line of In [1].

**In [2], the gammas from the record.**

```python
import numpy as np  # arrays of numbers, matrices and linear algebra

FIXTURE = "Revision/algebra/gammas.json"  # the Revision record of the gammas
fixture = json.loads(repository_file(FIXTURE).read_text(encoding="utf-8"))
COORDS = fixture["coordinates"]  # the coordinate names "x1", "x2", ..., "x8"
ETA = dict(zip(COORDS, fixture["eta"]))  # eta_aa: +1 space-like, -1 time-like
```

numpy is loaded under the short name `np`. `read_text` reads the record file as text and `json.loads` turns the text into Python objects: `fixture` is a dictionary whose keys are the names stored in the record. `fixture["coordinates"]` is the list `["x1", ..., "x8"]`. `zip` pairs each coordinate name with its entry of the list `fixture["eta"]`, and `dict` makes a dictionary of the pairs, so `ETA["x4"]` is $-1$.

```python
gamma = {x: np.array(m, dtype=np.int64) for x, m in zip(COORDS, fixture["gamma"])}
I16 = np.eye(16, dtype=np.int64)  # the 16 x 16 identity matrix, written 1 in the text
```

A **dictionary comprehension** `{x: ... for x, m in ...}` builds a dictionary in one line: for each pair of a name `x` and a stored matrix `m` (a list of 16 rows of 16 whole numbers) it stores `np.array(m, dtype=np.int64)`, the same matrix as a numpy array of 64-bit whole numbers. With whole numbers every product below is exact: nothing is rounded. `np.eye(16)` is the identity matrix.

```python
for x in COORDS:
    kind = "space-like" if ETA[x] == 1 else "time-like"
    rows, columns = gamma[x].shape  # the numbers of rows and of columns
    say(f"gamma^({x}): {rows} x {columns}, eta = {ETA[x]:+d} ({kind})")
```

For each direction the loop chooses the word space-like or time-like (`a if condition else b` is `a` when the condition holds and `b` otherwise), reads the shape of the matrix (16 rows and 16 columns) and prints one line; `{ETA[x]:+d}` writes the whole number with its sign. The eight printed lines show eight $16 \times 16$ matrices, four with $\eta = +1$ and four with $\eta = -1$.

**In [3], the recorded checks.**

```python
import contextlib  # lets a block of code print into a text buffer
import io  # the text buffer io.StringIO
import sys  # sys.stdout: the channel through which the notebook prints

REPORT_FILES = {"python": "Revision/algebra/reports/python-algebra.json",
                "wolfram": "Revision/algebra/reports/wolfram-algebra.json"}
VERDICTS = {}  # (report key, check name) -> (verdict in lower case, detail text)
for key, path in REPORT_FILES.items():
    report_data = json.loads(repository_file(path).read_text(encoding="utf-8"))
    for entry in report_data["checks"]:
        VERDICTS[(key, entry["name"])] = (entry["verdict"].lower(), entry["detail"])
```

Three more modules of Python are loaded. `REPORT_FILES` names the two reports of the record. The loop reads each report; `report_data["checks"]` is its list of checks, each a dictionary with the keys `name`, `verdict` and `detail`. Every check is stored in `VERDICTS` under the pair (report key, check name); `.lower()` writes the verdict in small letters, because one report writes PASS and the other pass.

```python
def recorded(key, name):
    return VERDICTS[(key, name)][0] == "pass"


def record_of(key, name):
    return f"{REPORT_FILES[key]}, check {name}"
```

`recorded("python", "clifford_relation")` is true when the Python report holds that check with the verdict pass (`[0]` takes the first element of the stored pair). `record_of` builds the text that a reproducing check prints after the word reproduces.

```python
def check_reproduces(condition, name, record):
    collected = io.StringIO()
    with contextlib.redirect_stdout(collected):  # print into the buffer
        check(condition, name, record=record)  # stops here if the check fails
    sys.stdout.write(collected.getvalue())  # the PASS and reproduces lines together
```

This is `check` for a check that reproduces a record. Inside the `with` block everything printed goes into the text buffer `collected` instead of the screen; `check` prints its PASS line and its reproduces line there (or stops the notebook if the condition is false). Then `sys.stdout.write` sends both lines at once. Jupyter delivers printed text in pieces, and one piece keeps the two lines together for the tools that read the notebook.

```python
say(f"{len(VERDICTS)} recorded checks were read from the two reports.")
check_reproduces(COORDS == ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]
                 and fixture["eta"] == [1, 1, 1, -1, -1, -1, -1, 1]
                 and recorded("wolfram", "eta_in_author_order"),
                 "the coordinates are x1..x8 and eta = diag(+1,+1,+1,-1,-1,-1,-1,+1)",
                 record=record_of("wolfram", "eta_in_author_order"))
```

The first line prints the number of recorded checks read: 80, the 35 of the Python report and the 45 of the Wolfram report. The check compares the list of coordinate names and the list of the signs of $\eta$ with the expected lists (`==` compares two lists element by element) and requires that the Wolfram report recorded the same fact; `and` is true only when all its parts are true. It prints PASS and the record it reproduces.

**In [4], the Clifford relation.**

```python
def anticommutator(m, n):
    return m @ n + n @ m


failures = []  # the pairs (x, y) for which the relation fails
for x in COORDS:
    for y in COORDS:
        # the right side: 2 eta_xx 1 when x = y, the zero matrix otherwise
        expected = 2 * ETA[x] * I16 if x == y else np.zeros_like(I16)
        if not np.array_equal(anticommutator(gamma[x], gamma[y]), expected):
            failures.append((x, y))
```

In Python the sign `@` multiplies two matrices, so `anticommutator(m, n)` is $mn + nm$. Two loops run through all $8 \times 8 = 64$ ordered pairs of directions. For each pair the right side of the Clifford relation is $2\eta_{xx}1$ when the two directions are equal and the zero matrix (`np.zeros_like(I16)`, zeros of the same shape) otherwise. `np.array_equal` is true only when all 256 entries agree; a pair for which they do not is appended to `failures`.

```python
say(f"pairs tested: {len(COORDS) ** 2}; pairs that fail: {len(failures)}")
check_reproduces(failures == [] and recorded("python", "clifford_relation"),
                 "{gamma^a, gamma^b} = 2 eta^ab 1 for all 64 pairs",
                 record=record_of("python", "clifford_relation"))
```

`**` is the power in Python, so `len(COORDS) ** 2` is 64. The printed line reports 64 pairs tested and 0 failures, and the check requires the list of failures to be empty.

**In [5], signed permutations and the symmetry pattern.**

```python
values = sorted({int(v) for x in COORDS for v in gamma[x].flat})  # every entry once
one_per_row = all((gamma[x] != 0).sum(axis=1).tolist() == [1] * 16 for x in COORDS)
one_per_column = all((gamma[x] != 0).sum(axis=0).tolist() == [1] * 16 for x in COORDS)
say(f"the entries of the gammas are {values}")
```

`gamma[x].flat` runs through the 256 entries of a matrix. The braces make a **set**, which keeps every value only once; `sorted` turns it into an ordered list, here `[-1, 0, 1]`. `gamma[x] != 0` is a table of true and false values (true where the entry is not zero); `.sum(axis=1)` counts the true values in each row and `.sum(axis=0)` in each column; `.tolist()` turns the result into a list, and `[1] * 16` is the list of sixteen ones. `all(...)` is true when the condition holds for every direction.

```python
check_reproduces(values == [-1, 0, 1] and one_per_row and one_per_column
                 and recorded("python", "reality_signed_permutations"),
                 "every gamma is real and a signed permutation matrix",
                 record=record_of("python", "reality_signed_permutations"))
symmetric = [x for x in COORDS if np.array_equal(gamma[x].T, gamma[x])]
antisymmetric = [x for x in COORDS if np.array_equal(gamma[x].T, -gamma[x])]
say("symmetric gammas: " + ", ".join(symmetric))
say("antisymmetric gammas: " + ", ".join(antisymmetric))
check_reproduces(symmetric == ["x1", "x2", "x3", "x8"]
                 and antisymmetric == ["x4", "x5", "x6", "x7"]
                 and recorded("python", "symmetry_pattern"),
                 "(gamma^a)^T = eta_aa gamma^a: space-like symmetric, time-like "
                 "antisymmetric",
                 record=record_of("python", "symmetry_pattern"))
```

The first check combines the three facts. Then two **list comprehensions** collect the directions whose matrix equals its transpose (`.T` is the transpose) and those whose matrix equals minus its transpose; `", ".join(...)` writes a list of names separated by commas. The printed lines are `x1, x2, x3, x8` and `x4, x5, x6, x7`, and the second check requires exactly these lists: the space-like gammas are symmetric and the time-like ones antisymmetric.

**In [6], three helpers.**

```python
from matplotlib.colors import LinearSegmentedColormap

# Colours of the heat maps: -1 blue, 0 light grey, +1 red (a diverging colour scale).
SIGNS = LinearSegmentedColormap.from_list("signs", ["#2a78d6", "#f0efec", "#e34948"])
```

A **colour map** assigns a colour to every number of a range. `from_list` makes one that runs smoothly through the three listed colours (each written as a hexadecimal code of its red, green and blue parts): blue for the lowest value, light grey in the middle, red for the highest.

```python
def heat_map(ax, matrix, title, halves=True, row_label=True):
    size = matrix.shape[0]
    image = ax.imshow(matrix, cmap=SIGNS, vmin=-1, vmax=1)
    ax.set_title(title)
    ticks = [0, 3, 7, 11, 15] if size == 16 else [0, 3, 7]  # counted from 0
    ax.set_xticks(ticks, [str(t + 1) for t in ticks])  # labels counted from 1
    ax.set_yticks(ticks, [str(t + 1) for t in ticks])
    ax.set_xlabel("column")
    if row_label:
        ax.set_ylabel("row")
    ax.grid(False)  # no grid lines across the coloured squares
    if halves and size == 16:
        ax.axhline(7.5, color="black", linewidth=0.8)  # between rows 8 and 9
        ax.axvline(7.5, color="black", linewidth=0.8)  # between columns 8 and 9
    return image
```

`heat_map` draws a matrix on the **axes** `ax` (one picture area of a figure). `ax.imshow` draws one coloured square per entry with the colour map `SIGNS`, so that $-1$ is blue, $0$ grey and $+1$ red (`vmin` and `vmax` fix the range). Python counts rows and columns from 0, the book from 1: the tick marks stand at the positions 0, 3, 7, 11, 15 and are labelled 1, 4, 8, 12, 16 (for an $8 \times 8$ matrix only 1, 4, 8). The optional argument `row_label=False` leaves out the word row on the second and later pictures of a row of pictures. For a $16 \times 16$ matrix two thin black lines at the position 7.5 (between the eighth and the ninth row and column) show the two halves. The function returns the drawn image, which a colour bar needs.

```python
def commutation_sign(m, n):
    if np.array_equal(m @ n, n @ m):
        return 1
    if np.array_equal(m @ n, -(n @ m)):
        return -1
    return 0


def product(directions):
    result = I16
    for d in directions:
        result = result @ gamma[d]
    return result


say("helpers heat_map, commutation_sign and product are defined")
```

`commutation_sign(m, n)` returns $+1$ when $mn = nm$, $-1$ when $mn = -nm$ and $0$ when neither holds. `product(["x8", "x1"])` multiplies the gammas of the listed directions in the order of the list, starting from the identity. The cell prints one line.

**In [7], the charge matrix.**

```python
C = product(["x8", "x1", "x2", "x3"])  # the four space-like gammas
C_record = np.array(fixture["C"], dtype=np.int64)  # the C stored in the record
check_reproduces(np.array_equal(C, C_record) and recorded("wolfram", "C_definition"),
                 "C = gamma^(x8) gamma^(x1) gamma^(x2) gamma^(x3) equals the recorded C",
                 record=record_of("wolfram", "C_definition"))
```

$C = \gamma^{(x8)}\gamma^{(x1)}\gamma^{(x2)}\gamma^{(x3)}$ is computed and compared with the matrix $C$ that the record stores.

```python
I4, Z4 = np.eye(4, dtype=np.int64), np.zeros((4, 4), dtype=np.int64)
I8, Z8 = np.eye(8, dtype=np.int64), np.zeros((8, 8), dtype=np.int64)
sigma = np.block([[Z4, I4], [I4, Z4]])  # the author's 8 x 8 matrix sigma
check_reproduces(np.array_equal(C, np.block([[-sigma, Z8], [Z8, sigma]]))
                 and recorded("python", "C_equals_notebook_sigma16"),
                 "C = diag(-sigma, sigma), called sigma16 by the author",
                 record=record_of("python", "C_equals_notebook_sigma16"))
check_reproduces(np.array_equal(C.T, C) and np.array_equal(C @ C, I16)
                 and recorded("python", "C_real_symmetric_involution"),
                 "C is real and symmetric, and C C = 1 (so C is its own inverse)",
                 record=record_of("python", "C_real_symmetric_involution"))
```

The first two lines make identity and zero matrices of sizes 4 and 8 (a line `A, B = p, q` names two values at once). `np.block` assembles a matrix from a list of rows of blocks: `[[Z4, I4], [I4, Z4]]` is the author's $\sigma$, and `[[-sigma, Z8], [Z8, sigma]]` is $\mathrm{diag}(-\sigma, \sigma)$. The two checks confirm (C7), then (C2) and (C3) of Section 5.4.

**In [8], the picture of C.**

```python
fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.4), width_ratios=[2, 1])
heat_map(axes[0], C, r"$C = \gamma^{(x8)}\gamma^{(x1)}\gamma^{(x2)}\gamma^{(x3)}$")
image = heat_map(axes[1], sigma, r"$\sigma$ (8 x 8)", halves=False,
                 row_label=False)
fig.colorbar(image, ax=axes, ticks=[-1, 0, 1], shrink=0.75, label="matrix entry")
save_figure(fig, "c_matrix",
            "Heat maps of the charge matrix $C$ (left, 16 by 16) and of the "
            ...)
```

`plt.subplots(1, 2, ...)` makes a figure with one row of two picture areas; `width_ratios=[2, 1]` makes the first twice as wide as the second. A string that starts with `r` is a **raw string**: its backslashes are kept as they are, which the mathematical titles (typeset by matplotlib between dollar signs) need. The first heat map shows $C$, the second $\sigma$ without the half lines. `fig.colorbar` adds a bar that shows which colour means which value, with ticks at $-1$, $0$, $+1$, shrunk to three quarters of the height. `save_figure` saves the figure as `05a_1_c_matrix.png` with its caption (the full caption is printed in the notebook text above; Python joins strings written next to each other into one). In the figure, look at the top-left block: blue squares in the pattern of $\sigma$; the bottom-right block: red squares in the same pattern; the picture is mirror-symmetric about its diagonal, because $C^T = C$.

**In [9], how C moves past the gammas.**

```python
signs_C = {x: commutation_sign(C, gamma[x]) for x in COORDS}  # +1 or -1 for each x
say("C gamma^(x) = s gamma^(x) C with s = "
    + ", ".join(f"{x}: {signs_C[x]:+d}" for x in COORDS))
check(all(signs_C[x] == -ETA[x] for x in COORDS),
      "C gamma^a = -eta_aa gamma^a C (anticommutes with space-like, commutes with "
      "time-like gammas)")
```

`signs_C` stores, for each direction, the sign $s$ in $C\gamma^a = s\,\gamma^aC$. The printed line lists them: $-1$ for $x1$, $x2$, $x3$, $x8$ and $+1$ for $x4$ to $x7$. The check is (C1): $s = -\eta_{aa}$ for every direction. It is this notebook's own check (no record holds it in this form), so it prints no reproduces line.

```python
check_reproduces(all(np.array_equal((C @ gamma[x]).T, -(C @ gamma[x])) for x in COORDS)
                 and recorded("python", "C_gamma_antisymmetric"),
                 "C gamma^a is antisymmetric for every a",
                 record=record_of("python", "C_gamma_antisymmetric"))
check_reproduces(all(np.array_equal(C @ gamma[x] @ C, -gamma[x].T) for x in COORDS)
                 and recorded("python", "C_conjugation"),
                 "C gamma^a C^-1 = -(gamma^a)^T for every a",
                 record=record_of("python", "C_conjugation"))
```

The two checks are (C4) and (C5). The second writes $C\gamma^aC$ for $C\gamma^aC^{-1}$, because $C^{-1} = C$.

**In [10], the squaring rule on all 255 products.**

```python
import itertools  # lists all subsets of a given size


def square_sign(directions):
    k = len(directions)
    s = (-1) ** (k * (k - 1) // 2)  # // is division of whole numbers
    for d in directions:
        s *= ETA[d]
    return s
```

`square_sign` computes the sign that Rule 2 of Section 5.3 predicts for the square of the product of the listed directions: $(-1)^{k(k-1)/2}$ times the product of the $\eta_{dd}$. `//` divides whole numbers without a remainder ($k(k-1)$ is always even), and `s *= ETA[d]` multiplies `s` by $\eta_{dd}$.

```python
agree = 0  # how many subsets obey the rule
for k in range(1, 9):
    for subset in itertools.combinations(COORDS, k):
        p = product(subset)
        if np.array_equal(p @ p, square_sign(subset) * I16):
            agree += 1
say(f"subsets tested: 255; subsets that obey the squaring rule: {agree}")
```

`range(1, 9)` runs through $k = 1, \dots, 8$. `itertools.combinations(COORDS, k)` lists every subset of $k$ directions, each in the order $x1, \dots, x8$; there are $\binom{8}{k}$ of them, $2^8 - 1 = 255$ in all. For each subset the cell multiplies the gammas, squares the product and compares it with the predicted sign times the identity; `agree += 1` adds one to the counter. The printed line reports 255 of 255.

```python
for label, dirs in [("C", ["x8", "x1", "x2", "x3"]),
                    ("Gamma", ["x8", "x1", "x2", "x3", "x4", "x5", "x6", "x7"]),
                    ("C gamma^(x4)", ["x8", "x1", "x2", "x3", "x4"])]:
    say(f"({label})^2 = {square_sign(dirs):+d} times 1 (k = {len(dirs)})")
check(agree == 255, "the squaring rule holds for all 255 products of different gammas")
```

The loop prints the predicted squares of the three products used in this chapter: $C^2 = +1$, $\Gamma^2 = +1$ and $(C\gamma^{(x4)})^2 = -1$, the facts behind (C3), (X1) and (B3). The check requires all 255 subsets to agree.

**In [11], the quadratic form of C.**

```python
t = np.linspace(0.0, np.pi, 401)  # 401 equally spaced values of t from 0 to pi
e = np.eye(16)  # e[r - 1] is the column e_r (a 1 in row r)
u = np.outer(np.cos(t), e[0]) + np.outer(np.sin(t), e[4])  # u(t), one per row
v = np.outer(np.cos(t), e[8]) + np.outer(np.sin(t), e[12])  # v(t), one per row
```

`np.linspace(0.0, np.pi, 401)` is an array of 401 numbers from 0 to $\pi$ with equal steps. `e[0]` is the first row of the identity, the column $e_1$ written as a row; Python counts from 0, so $e_5$ is `e[4]`. `np.outer(a, b)` is the table whose row $j$ is the number `a[j]` times the row `b`; so `u` has 401 rows, row $j$ being $\cos t_j\, e_1 + \sin t_j\, e_5$, and `v` holds $\cos t\, e_9 + \sin t\, e_{13}$ in the same way.

```python
form_u = np.einsum("tr,rc,tc->t", u, C, u)  # u^T C u for every t at once
form_v = np.einsum("tr,rc,tc->t", v, C, v)  # v^T C v for every t at once
say(f"C_(1,5) = {C[0, 4]:+d} and C_(9,13) = {C[8, 12]:+d}")
check(C[0, 4] == -1 and C[8, 12] == 1
      and np.max(np.abs(form_u + np.sin(2 * t))) < 1e-14
      and np.max(np.abs(form_v - np.sin(2 * t))) < 1e-14,
      "u^T C u = -sin 2t and v^T C v = +sin 2t along the two paths")
```

`np.einsum` evaluates a sum over repeated letters: `"tr,rc,tc->t"` means $\sum_{r,c} u_{tr}C_{rc}u_{tc}$ for every $t$, that is $u^TCu$ at all 401 times at once. The printed line shows $C_{1,5} = -1$ and $C_{9,13} = +1$ (entries `[0, 4]` and `[8, 12]`). The check compares the computed forms with $-\sin 2t$ and $+\sin 2t$: the largest difference (`np.max(np.abs(...))`) must be below $10^{-14}$, because the numbers are now floating-point numbers, which keep about 16 significant digits.

```python
eigenvalues_C = np.linalg.eigvalsh(C.astype(float))  # 16 real eigenvalues, sorted
n_plus = int(np.sum(np.abs(eigenvalues_C - 1.0) < 1e-9))  # how many are +1
n_minus = int(np.sum(np.abs(eigenvalues_C + 1.0) < 1e-9))  # how many are -1
say(f"trace of C = {int(np.trace(C))}; eigenvalues +1: {n_plus}, -1: {n_minus}")
check(np.trace(C) == 0 and n_plus == 8 and n_minus == 8,
      "C has eight eigenvalues +1 and eight -1: signature (8, 8)")
```

`np.linalg.eigvalsh` computes the eigenvalues of a symmetric matrix (`.astype(float)` turns the whole numbers into floating-point numbers first). `np.abs(eigenvalues_C - 1.0) < 1e-9` is true for every eigenvalue within $10^{-9}$ of $+1$, and `np.sum` counts the true values. The printed line shows trace 0, eight $+1$ and eight $-1$: (C6) of Section 5.4.

**In [12], the picture of the two forms.**

```python
fig, ax = plt.subplots(figsize=(7.0, 4.2))
ax.plot(t, form_u, color="#2a78d6", linewidth=2,
        label=r"$u^T C u$ with $u = \cos t\, e_1 + \sin t\, e_5$")
ax.plot(t, form_v, color="#eb6834", linewidth=2, linestyle="--",
        label=r"$v^T C v$ with $v = \cos t\, e_9 + \sin t\, e_{13}$")
ax.plot(t, np.einsum("tr,tr->t", u, u), color="#1baf7a", linewidth=2,
        linestyle=":", label=r"$u^T u$ (ordinary squared length)")
ax.axhline(0.0, color="black", linewidth=0.6)
```

`ax.plot(xs, ys, ...)` draws a curve through the points; `color` gives its colour, `linewidth` its thickness, `linestyle` makes it dashed or dotted, and `label` is its name in the legend. The third curve is $u^Tu$ (`"tr,tr->t"` sums $u_{tr}u_{tr}$ over $r$), which is 1 everywhere. `ax.axhline(0.0)` draws the horizontal line at height 0.

```python
ax.set_xticks([0, np.pi / 4, np.pi / 2, 3 * np.pi / 4, np.pi],
              ["0", r"$\pi/4$", r"$\pi/2$", r"$3\pi/4$", r"$\pi$"])
ax.set_xlabel("$t$ (radians)")
ax.set_ylabel("value of the quadratic form")
ax.set_title("The form of $C$ takes both signs; the ordinary length does not")
# the legend goes below the picture, where it hides no curve
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.17), ncol=1)
save_figure(fig, "c_form_signs", ...)
```

The tick marks of the horizontal axis are placed at multiples of $\pi/4$ and labelled in radians; the axes and the picture get their labels and title. `ax.legend` draws the box that names the curves; `bbox_to_anchor=(0.5, -0.17)` puts its top centre below the picture, where it hides no curve. The figure, `05a_2_c_form_signs.png`, shows the solid curve $-\sin 2t$ going down to $-1$, the dashed curve $+\sin 2t$ going up to $+1$, and the dotted line at 1: the form of $C$ takes both signs on unit columns, the ordinary length does not.

**In [13], the chirality.**

```python
Gamma = product(["x8", "x1", "x2", "x3", "x4", "x5", "x6", "x7"])  # all eight
check_reproduces(np.array_equal(Gamma, np.array(fixture["Gamma"], dtype=np.int64))
                 and np.array_equal(Gamma, np.block([[-I8, Z8], [Z8, I8]]))
                 and recorded("python", "chirality_diag"),
                 "Gamma = gamma^(x8) gamma^(x1) ... gamma^(x7) = diag(-1_8, 1_8), as "
                 "recorded",
                 record=record_of("python", "chirality_diag"))
```

$\Gamma$ is the product of all eight gammas in the author's order. The check compares it with the recorded matrix and with $\mathrm{diag}(-1_8, 1_8)$: (X9) of Section 5.5.

```python
check_reproduces(np.array_equal(Gamma @ Gamma, I16)
                 and all(commutation_sign(Gamma, gamma[x]) == -1 for x in COORDS)
                 and recorded("python", "chirality_anticommutes"),
                 "Gamma Gamma = 1 and Gamma anticommutes with every gamma^a",
                 record=record_of("python", "chirality_anticommutes"))
check_reproduces(np.array_equal(Gamma, C @ product(["x4", "x5", "x6", "x7"]))
                 and recorded("python", "chirality_eq_C_times_time_gammas"),
                 "Gamma = C gamma^(x4) gamma^(x5) gamma^(x6) gamma^(x7)",
                 record=record_of("python", "chirality_eq_C_times_time_gammas"))
```

These are (X1) with (X2), and (X4).

```python
check_reproduces(commutation_sign(C, Gamma) == 1 and np.array_equal(Gamma.T, Gamma)
                 and np.array_equal(Gamma.T @ C @ Gamma, C)
                 and all(np.array_equal(Gamma.T @ C @ gamma[x] @ Gamma, -(C @ gamma[x]))
                         for x in COORDS)
                 and recorded("python", "chirality_C_relation"),
                 "C Gamma = Gamma C, Gamma^T C Gamma = C, Gamma^T C gamma^a Gamma = -C "
                 "gamma^a",
                 record=record_of("python", "chirality_C_relation"))
```

This check combines (X5), (X6), (X7) and (X8), the matrix input of the pairing theorem T1.

**In [14], the projectors.**

```python
P_minus = (I16 - Gamma) // 2  # the projector onto components 1 to 8
P_plus = (I16 + Gamma) // 2  # the projector onto components 9 to 16
check(np.array_equal(P_minus, np.block([[I8, Z8], [Z8, Z8]]))
      and np.array_equal(P_plus, np.block([[Z8, Z8], [Z8, I8]]))
      and np.array_equal(P_minus @ P_minus, P_minus)
      and np.array_equal(P_plus @ P_plus, P_plus)
      and not np.any(P_minus @ P_plus) and np.array_equal(P_minus + P_plus, I16)
      and np.trace(P_minus) == 8 and np.trace(P_plus) == 8,
      "P_- = diag(1_8, 0) and P_+ = diag(0, 1_8) are complementary projectors of rank 8")
```

The entries of $1 \pm \Gamma$ are 0 and 2, so the division by 2 with `//` is exact and keeps whole numbers. The check confirms the shapes $\mathrm{diag}(1_8, 0)$ and $\mathrm{diag}(0, 1_8)$, the projector rules $P_-P_- = P_-$, $P_+P_+ = P_+$, $P_-P_+ = 0$ (`np.any` is true when some entry is not zero, so `not np.any(...)` means the matrix is zero) and $P_- + P_+ = 1$, and that each keeps 8 components (trace 8).

```python
check_reproduces(all(np.array_equal(gamma[x] @ P_minus, P_plus @ gamma[x])
                     for x in COORDS)
                 and all(not np.any(gamma[x][:8, :8]) and not np.any(gamma[x][8:, 8:])
                         for x in COORDS)
                 and recorded("python", "reflections_exchange_halves")
                 and recorded("wolfram", "Spin_Pin_reflection_swaps_halves"),
                 "gamma^a P_- = P_+ gamma^a: every gamma exchanges the two halves",
                 record=record_of("python", "reflections_exchange_halves"))
```

The check is $\gamma^aP_- = P_+\gamma^a$ for every direction, and that the two diagonal blocks of every gamma are zero. `gamma[x][:8, :8]` is the top-left block: the **slice** `:8` takes the rows (or columns) 0 to 7 in Python's counting, the book's 1 to 8; `8:` takes the rest.

**In [15], the picture of the chirality.**

```python
fig, axes = plt.subplots(1, 4, figsize=(13.0, 3.9))
heat_map(axes[0], Gamma, r"$\Gamma$")
heat_map(axes[1], P_minus, r"$P_- = (1 - \Gamma)/2$", row_label=False)
heat_map(axes[2], P_plus, r"$P_+ = (1 + \Gamma)/2$", row_label=False)
image = heat_map(axes[3], gamma["x1"], r"$\gamma^{(x1)}$ for comparison",
                 row_label=False)
fig.colorbar(image, ax=axes, ticks=[-1, 0, 1], shrink=0.8, label="matrix entry")
save_figure(fig, "chirality", ...)
```

Four heat maps in one row and a colour bar, saved as `05a_3_chirality.png`. In the figure, $\Gamma$ is blue on the first eight diagonal places and red on the last eight; $P_-$ and $P_+$ are red on the diagonal of one half; $\gamma^{(x1)}$ has its coloured squares only in the two off-diagonal blocks.

**In [16], the matrix B.**

```python
B = -1j * (C @ gamma["x4"])  # B = -i C gamma^(x4); 1j is the imaginary unit
B_record = (np.array(fixture["B"]["re"], dtype=np.int64)
            + 1j * np.array(fixture["B"]["im"], dtype=np.int64))
check_reproduces(np.array_equal(B, B_record) and recorded("wolfram", "B_definition"),
                 "B = -i C gamma^(x4) equals the recorded B",
                 record=record_of("wolfram", "B_definition"))
```

Python writes the imaginary unit as `1j`. The record stores the real and the imaginary part of $B$ separately (`fixture["B"]["re"]` and `fixture["B"]["im"]`), and the cell assembles them into one complex matrix before comparing. The entries of $B$ are $0$, $i$ and $-i$, which the computer stores exactly.

```python
check_reproduces(not np.any(B.real) and np.array_equal(B.conj().T, B)
                 and np.array_equal(B @ B, I16) and np.trace(B) == 0
                 and recorded("python", "B_hermitian_involution_signature")
                 and recorded("wolfram", "B_Hermitian")
                 and recorded("wolfram", "B_squared_identity"),
                 "B is purely imaginary and Hermitian, B B = 1 and tr B = 0",
                 record=record_of("python", "B_hermitian_involution_signature"))
```

`B.real` is the real part (it must be zero everywhere), and `B.conj().T` the conjugate transpose $B^\dagger$. The check combines (B1) to (B4).

**In [17], the characteristic polynomial of B.**

```python
import sympy as sp  # exact algebra with symbols

lam = sp.Symbol("lam")  # the variable lambda of the polynomial
B_exact = sp.I * sp.Matrix((-(C @ gamma["x4"])).tolist())  # B with exact sympy numbers
polynomial = sp.factor(B_exact.charpoly(lam).as_expr())  # det(lam 1 - B), factored
say(f"characteristic polynomial of B: {polynomial}")
```

sympy computes with symbols and exact numbers. `sp.Symbol("lam")` is the letter $\lambda$. Since $B = -iC\gamma^{(x4)} = i(-C\gamma^{(x4)})$, the matrix is built as sympy's imaginary unit `sp.I` times the whole-number matrix $-C\gamma^{(x4)}$ (`.tolist()` turns the numpy array into a list of rows, which `sp.Matrix` accepts). `charpoly(lam)` computes $\det(\lambda 1 - B)$ exactly, `.as_expr()` writes it as an ordinary expression, and `sp.factor` writes it as a product of factors. The printed result is `(lam - 1)**8*(lam + 1)**8`, sympy's way of writing $(\lambda - 1)^8(\lambda + 1)^8$.

```python
detail = VERDICTS[("python", "B_hermitian_involution_signature")][1]
check_reproduces(sp.expand(polynomial - (lam - 1) ** 8 * (lam + 1) ** 8) == 0
                 and f"= {polynomial}" in detail
                 and recorded("wolfram", "B_signature_8_8"),
                 "det(lam 1 - B) = (lam - 1)^8 (lam + 1)^8: signature (8, 8)",
                 record=record_of("python", "B_hermitian_involution_signature"))
```

`detail` is the detail text of the recorded check, which states the polynomial. The check requires that the difference between the computed polynomial and $(\lambda - 1)^8(\lambda + 1)^8$ multiplies out (`sp.expand`) to exactly 0, and that the text `= (lam - 1)**8*(lam + 1)**8` occurs in the recorded detail (`in` tests whether one string occurs in another): the notebook and the record wrote the same polynomial, character by character.

**In [18], how B moves past the gammas.**

```python
signs_B = {x: commutation_sign(B, gamma[x]) for x in COORDS}
commute = [x for x in COORDS if signs_B[x] == 1]
anticommute = [x for x in COORDS if signs_B[x] == -1]
say("B commutes with gamma^(x) for x = " + ", ".join(commute))
say("B anticommutes with gamma^(x) for x = " + ", ".join(anticommute))
check_reproduces(commute == ["x1", "x2", "x3", "x4", "x8"]
                 and anticommute == ["x5", "x6", "x7"]
                 and recorded("python", "B_gamma_relations"),
                 "B commutes with gamma^a for a = x1, x2, x3, x4, x8 and anticommutes "
                 "for x5, x6, x7",
                 record=record_of("python", "B_gamma_relations"))
```

The sign of $B$ with each gamma is computed and the directions are sorted into two lists. The printed lines and the check confirm (B5): $B$ anticommutes exactly with the gammas of the three extra times.

**In [19], the picture of B.**

```python
fig, axes = plt.subplots(1, 3, figsize=(11.0, 4.0))
heat_map(axes[0], gamma["x4"], r"$\gamma^{(x4)}$ (antisymmetric)")
heat_map(axes[1], C @ gamma["x4"], r"$C\gamma^{(x4)}$ (antisymmetric)",
         row_label=False)
image = heat_map(axes[2], B.imag, r"imaginary part of $B = -iC\gamma^{(x4)}$",
                 row_label=False)
fig.colorbar(image, ax=axes, ticks=[-1, 0, 1], shrink=0.8, label="matrix entry")
save_figure(fig, "b_matrix", ...)
```

Three heat maps: $\gamma^{(x4)}$, $C\gamma^{(x4)}$ and the imaginary part of $B$ (`B.imag`), which is $-C\gamma^{(x4)}$. In `05a_4_b_matrix.png` every picture changes colour when it is mirrored about its diagonal: all three are antisymmetric, and $B$, being $i$ times an antisymmetric real matrix, is Hermitian.

**In [20], the spectra.**

```python
TARGETS = [1, -1, 1j, -1j]  # the four possible eigenvalues
TARGET_NAMES = ["+1", "-1", "+i", "-i"]
matrices = {f"gamma^({x})": gamma[x] for x in COORDS}
matrices.update({"C": C, "Gamma": Gamma, "B": B})
counts = {}  # name -> [how many eigenvalues near +1, -1, +i, -i]
for name, m in matrices.items():
    eigenvalues = np.linalg.eigvals(m.astype(complex))
    counts[name] = [int(np.sum(np.abs(eigenvalues - z) < 1e-9)) for z in TARGETS]
    say(f"{name:12} " + "  ".join(f"{n}: {c}" for n, c in
                                  zip(TARGET_NAMES, counts[name])))
```

`matrices` collects the eleven matrices under their names (`update` adds three more entries). For each, `np.linalg.eigvals` computes its 16 eigenvalues as complex floating-point numbers, and the list comprehension counts how many lie within $10^{-9}$ of each of $+1$, $-1$, $+i$, $-i$ (for a complex number `np.abs` is its distance from 0). `{name:12}` pads the name to 12 characters, so that the eleven printed lines form a table.

```python
predicted = {name: ([8, 8, 0, 0] if name in ("C", "Gamma", "B")
                    or ETA[name[7:9]] == 1 else [0, 0, 8, 8]) for name in matrices}
check(counts == predicted and all(np.trace(gamma[x]) == 0 for x in COORDS),
      "eigenvalues: +1 and -1 eight times each for the space-like gammas, C, Gamma "
      "and B; +i and -i eight times each for the time-like gammas")
```

The prediction of Rule 6: eight $+1$ and eight $-1$ for $C$, $\Gamma$, $B$ and the space-like gammas, eight $+i$ and eight $-i$ for the time-like ones. For a gamma, `name[7:9]` cuts the two characters at positions 7 and 8 out of a name such as `gamma^(x1)`, which are `x1`; the `or` looks at it only when the name is not one of the three (Python evaluates `a or b` from the left and stops when `a` is true). The check compares all counts with the prediction and checks that every gamma has trace 0, the condition of Rule 6.

**In [21], the picture of the spectra.**

```python
from matplotlib.colors import LinearSegmentedColormap as Ramp

names = list(matrices)  # the 11 matrices in the order of the table
table = np.array([counts[name] for name in names])  # 11 rows, 4 columns
COUNT_COLORS = Ramp.from_list("counts", ["#f0efec", "#2a78d6"])  # 0 grey, 8 blue
fig, ax = plt.subplots(figsize=(6.0, 6.4))
ax.imshow(table, cmap=COUNT_COLORS, vmin=0, vmax=8, aspect="auto")
for k in range(1, table.shape[0]):  # white gaps between the rows
    ax.axhline(k - 0.5, color="white", linewidth=2)
for k in range(1, table.shape[1]):  # and between the columns
    ax.axvline(k - 0.5, color="white", linewidth=2)
```

The table of counts becomes an array of 11 rows and 4 columns and is drawn as coloured squares, grey for 0 and blue for 8 (`as Ramp` gives the imported name a shorter name; `aspect="auto"` lets the squares be stretched to fill the picture). White lines between the rows and columns separate the squares.

```python
for r in range(table.shape[0]):
    for c in range(table.shape[1]):
        ax.text(c, r, str(table[r, c]), ha="center", va="center",
                color="white" if table[r, c] == 8 else "black")
ax.set_xticks(range(4), ["$+1$", "$-1$", "$+i$", "$-i$"])
labels = [rf"$\gamma^{{({x})}}$" for x in COORDS] + ["$C$", r"$\Gamma$", "$B$"]
ax.set_yticks(range(len(names)), labels)
ax.set_xlabel("eigenvalue")
ax.set_title("How many times each eigenvalue occurs (16 in each row)")
ax.grid(False)
save_figure(fig, "spectra", ...)
```

`ax.text(c, r, ...)` writes each count in the middle of its square (`ha` and `va` centre it horizontally and vertically), in white on blue and in black on grey. The column labels are the four eigenvalues; the row labels are made by an `rf`-string, raw and formatted at once, in which a doubled brace `{{` stands for a single brace in the result, so that `$\gamma^{(x1)}$` and so on come out. The figure `05a_5_spectra.png` shows blue squares with 8 in the columns $+1$ and $-1$ for the space-like gammas, $C$, $\Gamma$ and $B$, and in the columns $+i$ and $-i$ for the time-like gammas.

**In [22], the table of commutation signs.**

```python
rows = {"C": signs_C, "Gamma": {x: commutation_sign(Gamma, gamma[x]) for x in COORDS},
        "B": signs_B}
sign_table = np.array([[rows[name][x] for x in COORDS] for name in rows])
expected_table = np.array([[-ETA[x] for x in COORDS], [-1] * 8,
                           [1, 1, 1, 1, -1, -1, -1, 1]])
check(np.array_equal(sign_table, expected_table),
      "the commutation signs of C, Gamma and B with the eight gammas are as predicted")
```

The signs of $C$ (In [9]), of $\Gamma$ (computed here) and of $B$ (In [18]) with the eight gammas form a table of 3 rows and 8 columns. The predicted table has the rows $-\eta_{aa}$ (C1), eight times $-1$ (X2) and the pattern of (B5). The check compares them.

```python
fig, ax = plt.subplots(figsize=(8.0, 3.2))
ax.imshow(sign_table, cmap=SIGNS, vmin=-1, vmax=1, aspect="auto")
for k in range(1, 3):  # white gaps between the rows
    ax.axhline(k - 0.5, color="white", linewidth=2)
for k in range(1, 8):  # and between the columns
    ax.axvline(k - 0.5, color="white", linewidth=2)
for r in range(3):
    for c in range(8):
        ax.text(c, r, f"{sign_table[r, c]:+d}", ha="center", va="center",
                color="white", fontweight="bold")
ax.set_xticks(range(8), [rf"$\gamma^{{({x})}}$" for x in COORDS])
ax.set_yticks(range(3), ["$C$", r"$\Gamma$", "$B$"])
ax.set_title(r"Sign $s$ in $M\gamma^a = s\,\gamma^a M$ (red $+1$ commute, "
             r"blue $-1$ anticommute)")
ax.grid(False)
save_figure(fig, "commutation_signs", ...)
```

The drawing works as in In [21], with the colour map of the heat maps: red squares $+1$ (commute), blue squares $-1$ (anticommute), each with its sign written in bold white. In `05a_6_commutation_signs.png` the row $C$ is blue for $x1$, $x2$, $x3$, $x8$ and red for $x4$ to $x7$; the row $\Gamma$ is blue everywhere; the row $B$ is blue only for the extra times $x5$, $x6$, $x7$.

**In [23], the last check.**

```python
FIGURES = ["05a_1_c_matrix.png", "05a_2_c_form_signs.png", "05a_3_chirality.png",
           "05a_4_b_matrix.png", "05a_5_spectra.png", "05a_6_commutation_signs.png"]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in FIGURES),
      "the six figure files of notebook 05a exist")
all_checks_passed()
```

The cell checks that the six figure files exist and prints the last line, ALL 26 CHECKS PASSED (notebook 05a). The 26 checks are: one in In [3], one in In [4], two in In [5], three in In [7], three in In [9], one in In [10], two in In [11], four in In [13], two in In [14], two in In [16], and one each in In [17], In [18], In [20], In [22] and In [23]. The cells In [1], In [2], In [6], In [8], In [12], In [15], In [19] and In [21] check nothing.

### 5.11 Groups and representations from zero

This section introduces the words of group theory that the rest of the chapter needs, each with a proof of the one fact used later. All groups here are groups of matrices.

**Group.** A **group** of $n \times n$ matrices is a set $G$ of invertible matrices that contains the identity, the product of any two of its members and the inverse of each member. Examples: the two matrices $\{1, -1\}$; all invertible $n \times n$ matrices; the rotations of the plane $R(\varphi) = \begin{pmatrix} \cos\varphi & -\sin\varphi \\ \sin\varphi & \cos\varphi \end{pmatrix}$, because $R(\varphi)R(\psi) = R(\varphi + \psi)$ (the addition theorems of sine and cosine) and $R(\varphi)^{-1} = R(-\varphi)$. A **subgroup** is a subset that is itself a group. The group **generated** by some matrices is the set of all finite products of these matrices and of their inverses; it is the smallest group that contains them.

**Representation.** A group of $16 \times 16$ matrices acts on columns of 16 numbers by multiplication, $\Psi \to g\Psi$. One says that the 16 components **carry a representation** of the group. A **subspace** is a set of columns that contains every sum and every multiple of its members (for example all columns whose components 9 to 16 are zero). A subspace $W$ is **invariant** when $gw$ lies in $W$ for every $g$ of the group and every $w$ of $W$. The zero subspace $\{0\}$ and the set of all columns are always invariant. The representation is **irreducible** when there is no other invariant subspace: the 16 components cannot be cut into smaller pieces that the group keeps apart.

**Span.** A **combination** of matrices $M_1, \dots, M_N$ is $c_1M_1 + \dots + c_NM_N$ with numbers $c_j$; the **span** is the set of all combinations. The matrices are **linearly independent** when no one of them is a combination of the others; then their span has **dimension** $N$. Writing each $16 \times 16$ matrix as one row of 256 numbers, $N$ matrices are independent exactly when the $N$ rows have **rank** $N$ (the rank of a list of rows is the number of independent ones among them).

**Commutant, intertwiner, equivalence.** The **commutant** of a list of matrices is the set of all matrices $X$ that commute with every matrix of the list. Two groups (or lists) of matrices $g \to \rho_1(g)$ and $g \to \rho_2(g)$, labelled by the same elements $g$, have an **intertwiner** $T$ when $T\rho_1(g) = \rho_2(g)T$ for every $g$; they are **equivalent** when an invertible intertwiner exists, because then $\rho_2(g) = T\rho_1(g)T^{-1}$ and the two are the same matrices written in another basis.

**Lemma 1.** For an intertwiner $T$, the set of columns $v$ with $Tv = 0$ (its **kernel**) is invariant under $\rho_1$, and the set of columns $Tv$ (its **image**) is invariant under $\rho_2$. Proof: if $Tv = 0$, then $T\rho_1(g)v = \rho_2(g)Tv = 0$, so $\rho_1(g)v$ lies in the kernel; and $\rho_2(g)(Tv) = T(\rho_1(g)v)$ lies in the image.

**Lemma 2 (Schur's lemma).** An intertwiner $T$ between two irreducible representations is either zero or invertible. Proof: by Lemma 1 and irreducibility, the kernel of $T$ is $\{0\}$ or everything, and so is its image. If $T \neq 0$, the kernel is not everything, so it is $\{0\}$: $T$ maps different columns to different columns. And the image is not $\{0\}$, so it is everything: every column is reached. A matrix with both properties is invertible.

**Lemma 3 (span criterion).** If the matrices of a group $G$ of $n \times n$ matrices span all $n \times n$ matrices, then (a) the representation is irreducible, and (b) its commutant consists of the multiples of the identity. Proof of (a): let $W \neq \{0\}$ be invariant and $w \neq 0$ a column of $W$. An invariant subspace is mapped into itself by every combination of group matrices (each term maps $w$ into $W$, and $W$ contains sums and multiples), hence by every matrix. For any column $v$, the matrix $M = v\,w^T/(w^Tw)$ (the column $v$ times the row $w^T$, divided by the number $w^Tw > 0$; for complex columns use $w^\dagger$) satisfies $Mw = v$. So $v$ lies in $W$, and $W$ is everything. Proof of (b): a matrix $X$ that commutes with every group matrix commutes with every combination of them, hence with every matrix, in particular with the matrix $E_{rc}$ that has a single 1 in row $r$ and column $c$. The entry $(i, j)$ of $XE_{rc}$ is $X_{ir}$ when $j = c$ and 0 otherwise; that of $E_{rc}X$ is $X_{cj}$ when $i = r$ and 0 otherwise. Taking $j = c$ and $i \neq r$: $X_{ir} = 0$, so every entry off the diagonal is zero. Taking $i = r$ and $j = c$: $X_{rr} = X_{cc}$, so all diagonal entries are equal. So $X$ is a number times $1$.

**Lemma 4 (two blocks).** Suppose the matrices of a group of $16 \times 16$ matrices span exactly the block-diagonal matrices $\mathrm{diag}(X, Y)$, with $X$ and $Y$ any two $8 \times 8$ matrices. Then (a) the first half (components 1 to 8) and the second half (9 to 16) are invariant subspaces; (b) each half is irreducible; (c) the two halves are inequivalent; (d) the commutant has dimension 2 and is spanned by $P_- = \mathrm{diag}(1_8, 0)$ and $P_+ = \mathrm{diag}(0, 1_8)$. Proof: (a) a block-diagonal matrix maps a column with zeros in one half to a column with zeros in the same half. (b) On the first half the group acts by the blocks $X$, which span all $8 \times 8$ matrices; Lemma 3 applies, and the same for $Y$. (c) Let $T$ be an $8 \times 8$ intertwiner, $TX = YT$ for every group element. The equation then holds for every combination, hence for every pair $(X, Y)$ of $8 \times 8$ matrices (the span contains $\mathrm{diag}(X, Y)$ for all $X$ and $Y$ independently). Take $X = 1_8$ and $Y = 0$: $T = 0$. The only intertwiner is zero, so the halves are inequivalent. (d) Write a $16 \times 16$ matrix in blocks, $Z = \begin{pmatrix} W & U \\ V & R \end{pmatrix}$. Then

$$
\mathrm{diag}(X, Y)\,Z = \begin{pmatrix} XW & XU \\ YV & YR \end{pmatrix}, \qquad Z\,\mathrm{diag}(X, Y) = \begin{pmatrix} WX & UY \\ VX & RY \end{pmatrix} .
$$

$Z$ commutes with all of them when $W$ commutes with every $X$ (so $W = w1_8$ by Lemma 3(b)), $R$ with every $Y$ (so $R = r1_8$), and $XU = UY$ and $YV = VX$ for all $X$, $Y$ (so $U = V = 0$, by the argument of (c)). Hence $Z = wP_- + rP_+$: a space of dimension 2.

**The negative control.** If instead the second half carried a copy of the first ($Y = X$ always), the commutant would contain every $\begin{pmatrix} p1_8 & q1_8 \\ s1_8 & t1_8 \end{pmatrix}$, which commutes with every $\mathrm{diag}(X, X)$: dimension 4. So the commutant dimension 2 distinguishes two inequivalent halves (dimension 2) from two equivalent ones (dimension 4); Notebook 05b computes both.

**Real or complex numbers.** All the equations of this chapter for an unknown matrix have whole-number coefficients. Gaussian elimination, which finds their solutions, uses only addition, subtraction, multiplication and division of the coefficients, so it takes exactly the same steps whether the unknowns are allowed to be rational, real or complex numbers. The dimension of the space of solutions is therefore the same in all three cases, and the irreducibility proved below holds over the real and over the complex numbers.

### 5.12 Pin(4,4), Spin(4,4) and the generators $S^{ab}$

**Vectors in the algebra.** A **vector** is a list of eight real numbers $v = (v_{x1}, \dots, v_{x8})$. To it belongs the matrix $\gamma(v) = \sum_a v_a\gamma^a$, and two vectors have the **metric product** $\eta(u, v) = \sum_a \eta_{aa}u_av_a$. From the Clifford relation, line by line:

$$
\gamma(u)\gamma(v) + \gamma(v)\gamma(u) = \sum_{a,b} u_av_b\,(\gamma^a\gamma^b + \gamma^b\gamma^a) = \sum_{a,b} u_av_b\, 2\eta^{ab}1 = 2\eta(u, v)\,1 .
$$

The first step multiplies out both products and collects the terms with the same pair $(a, b)$; the second is the Clifford relation; the third keeps only the terms $a = b$ (where $\eta^{aa} = \eta_{aa}$). With $u = v$: $\gamma(v)\gamma(v) = \eta(v, v)\,1$. A vector with $\eta(u, u) = +1$ or $-1$ is a **unit vector**. For a unit vector, $\gamma(u)$ is invertible with $\gamma(u)^{-1} = \eta(u, u)\,\gamma(u)$, because $\gamma(u)\,\eta(u, u)\gamma(u) = \eta(u, u)^2\,1 = 1$. (A **null** vector, such as $e_{x1} + e_{x4}$ with $\eta = 1 - 1 = 0$, has $\gamma(v)\gamma(v) = 0$ and no inverse; it is excluded.)

**O(4,4) and SO(4,4).** The real $8 \times 8$ matrices $\Lambda$ that keep the metric product, $\eta(\Lambda u, \Lambda v) = \eta(u, v)$ for all $u$, $v$, are those with $\Lambda^T\eta\Lambda = \eta$; they form the group **O(4,4)**. Taking the determinant of both sides, $(\det\Lambda)^2\det\eta = \det\eta$, and $\det\eta = (+1)^4(-1)^4 = 1$, so $\det\Lambda = \pm1$. Those with $\det\Lambda = +1$ form the subgroup **SO(4,4)**.

**Reflections.** For a unit vector $u$, the **reflection** along $u$ is the $8 \times 8$ matrix $R_u$ with

$$
R_uv = v - 2\,\frac{\eta(u, v)}{\eta(u, u)}\,u .
$$

It sends $u$ to $u - 2u = -u$ and keeps every $w$ with $\eta(u, w) = 0$. These $w$ form a 7-dimensional subspace that does not contain $u$, so in a basis made of $u$ and seven such $w$ the matrix is $\mathrm{diag}(-1, 1, \dots, 1)$, and $\det R_u = -1$. It keeps the metric product: expanding $\eta(R_uv, R_uw)$ gives $\eta(v, w)$ plus three terms with the factor $\eta(u, v)\eta(u, w)/\eta(u, u)$ and the coefficients $-2$, $-2$ and $+4$, which add up to zero. So $R_u$ lies in O(4,4) but not in SO(4,4).

**The key identity.** For a unit vector $u$ and any vector $v$:

$$
-\gamma(u)\gamma(v)\gamma(u)^{-1} = \gamma(R_uv) .
$$

Proof, line by line. By the relation above, $\gamma(u)\gamma(v) = 2\eta(u, v)1 - \gamma(v)\gamma(u)$. Multiply from the right by $\gamma(u)^{-1}$:

$$
\gamma(u)\gamma(v)\gamma(u)^{-1} = 2\eta(u, v)\,\gamma(u)^{-1} - \gamma(v) = 2\eta(u, v)\,\eta(u, u)\,\gamma(u) - \gamma(v) .
$$

Since $\eta(u, u) = \pm1$, $\eta(u, u) = 1/\eta(u, u)$, and $\gamma$ is linear ($\gamma(v) - c\,\gamma(u) = \gamma(v - cu)$), so the right side is $-\gamma\big(v - 2\eta(u, v)u/\eta(u, u)\big) = -\gamma(R_uv)$. Multiplying by $-1$ gives the identity. **Conjugation by a unit vector is a reflection, up to the sign.**

**Pin(4,4) and Spin(4,4).** **Pin(4,4)** is the set of all products

$$
g = \gamma(u_1)\gamma(u_2)\cdots\gamma(u_k)
$$

of finitely many unit vectors ($k = 0, 1, 2, \dots$; the empty product is $1$). It is a group: the product of two such products is again one, and the inverse $g^{-1} = \gamma(u_k)^{-1}\cdots\gamma(u_1)^{-1}$ is one too, because $\gamma(u)^{-1} = \gamma(\eta(u, u)u)$ and $\eta(u, u)u$ is a unit vector. **Spin(4,4)** is the subgroup of the products with an **even** number $k$ of factors. Examples: every $\gamma^a = \gamma(e_a)$ lies in Pin(4,4), where $e_a$ is the basic unit vector of the direction $a$; so does every product of different gammas, and it lies in Spin(4,4) when it is even. In particular $C$ (four factors), $\Gamma$ (eight), $1 = \gamma^{(x1)}\gamma^{(x1)}$ and $-1 = \gamma^{(x4)}\gamma^{(x4)}$ lie in Spin(4,4).

**Even and odd are well defined.** Multiply out a product of $k$ vectors: each $\gamma(u_j)$ is a combination of single gammas, so the product is a combination of products of $k$ gammas. Each such product can be brought into the order $x1, \dots, x8$ by exchanging neighbours (a sign each time) and then shortened by $\gamma^a\gamma^a = \eta_{aa}1$, which removes two factors at a time. So the product is a combination of products of different gammas whose degrees have the same parity (evenness or oddness) as $k$. Section 5.13 shows that the 256 products of different gammas are linearly independent; so a nonzero matrix cannot be both a combination of even products and a combination of odd products. An element of Pin(4,4) is invertible, hence not zero, so it is either **even** or **odd**, never both.

**The vector matrix.** For $g$ in Pin(4,4) put $\alpha(g) = g$ if $g$ is even and $\alpha(g) = -g$ if it is odd (the **twisted** action). For a single unit vector the key identity reads $\alpha(\gamma(u))\,\gamma^c\,\gamma(u)^{-1} = \gamma(R_ue_c) = \sum_d (R_u)_{dc}\gamma^d$. For a product, $\alpha(gh) = \alpha(g)\alpha(h)$, and

$$
\alpha(gh)\gamma^c(gh)^{-1} = \alpha(g)\big[\alpha(h)\gamma^ch^{-1}\big]g^{-1} = \sum_d \Lambda(h)_{dc}\,\alpha(g)\gamma^dg^{-1} = \sum_{e} \big(\Lambda(g)\Lambda(h)\big)_{ec}\gamma^e ,
$$

where $\Lambda(g)$ is the $8 \times 8$ matrix with $\alpha(g)\gamma^cg^{-1} = \sum_d \Lambda(g)_{dc}\gamma^d$. So $\Lambda(gh) = \Lambda(g)\Lambda(h)$, and for $g = \gamma(u_1)\cdots\gamma(u_k)$:

$$
\Lambda(g) = R_{u_1}R_{u_2}\cdots R_{u_k} ,
$$

a product of $k$ reflections. It lies in O(4,4), with $\det\Lambda(g) = (-1)^k$: the even elements, those of Spin(4,4), have vector matrices in SO(4,4). The matrix $\Lambda(g)$ says how $g$ moves the eight directions; it is called the **vector matrix** of $g$. Section 5.18 shows that $g$ and $-g$ have the same vector matrix and that these are the only two (the **double cover**).

**The generators.** For two directions $a$ and $b$ the **scaled commutator**

$$
S^{ab} = \tfrac14[\gamma^a, \gamma^b] = \tfrac14(\gamma^a\gamma^b - \gamma^b\gamma^a)
$$

is called a **generator**. $S^{aa} = 0$ and $S^{ba} = -S^{ab}$. For $a \neq b$ the two gammas anticommute, so $\gamma^a\gamma^b - \gamma^b\gamma^a = 2\gamma^a\gamma^b$ and $S^{ab} = \tfrac12\gamma^a\gamma^b$: its entries are $0$ and $\pm\tfrac12$. With $a$ before $b$ in the order $x1, \dots, x8$ there are $8 \cdot 7/2 = 28$ generators, one for each **coordinate plane** $(a, b)$. When $\eta_{aa}\eta_{bb} = +1$ (both directions space-like, or both time-like) the plane is called a **rotation** plane: $\binom{4}{2} + \binom{4}{2} = 6 + 6 = 12$ of them. When $\eta_{aa}\eta_{bb} = -1$ (one space-like and one time-like direction) it is a **boost** plane: $4 \cdot 4 = 16$ of them. Note that a plane of two times, such as $(x4, x5)$, is a rotation plane.

**The vector rule.** For all $a$, $b$, $c$:

$$
[S^{ab}, \gamma^c] = \eta^{bc}\gamma^a - \eta^{ac}\gamma^b .
$$

Proof for $a \neq b$ (for $a = b$ both sides are zero). Use the Clifford relation first as $\gamma^b\gamma^c = 2\eta^{bc}1 - \gamma^c\gamma^b$ and then as $\gamma^a\gamma^c = 2\eta^{ac}1 - \gamma^c\gamma^a$:

$$
\gamma^a\gamma^b\gamma^c = 2\eta^{bc}\gamma^a - \gamma^a\gamma^c\gamma^b = 2\eta^{bc}\gamma^a - 2\eta^{ac}\gamma^b + \gamma^c\gamma^a\gamma^b .
$$

Hence $[\gamma^a\gamma^b, \gamma^c] = \gamma^a\gamma^b\gamma^c - \gamma^c\gamma^a\gamma^b = 2\eta^{bc}\gamma^a - 2\eta^{ac}\gamma^b$, and dividing by 2 gives the rule. It says that a generator turns the gammas into combinations of each other, as an infinitesimal turning of the directions turns the components of a vector: in the plane $(x1, x2)$, $[S^{(x1)(x2)}, \gamma^{(x1)}] = -\gamma^{(x2)}$ and $[S^{(x1)(x2)}, \gamma^{(x2)}] = \gamma^{(x1)}$, and every other gamma commutes with $S^{(x1)(x2)}$.

| statement | status | where it is verified |
| --- | --- | --- |
| $S^{ab} = -S^{ba}$, $S^{ab} = \tfrac12\gamma^a\gamma^b$ for $a \neq b$, entries $0$, $\pm\tfrac12$ | PROVED | `python-algebra.json`, check `S_definition`; `wolfram-algebra.json`, checks `S_antisymmetric_in_ab`, `S_half_product` and `S_real_entries_in_half_integers` |
| the vector rule for all 512 triples $(a, b, c)$ | PROVED | `python-algebra.json`, check `S_vector_action`; `wolfram-algebra.json`, check `S_gamma_commutator` |
| the key identity, the vector matrix, $\det\Lambda(g) = (-1)^k$ | PROVED (above) | Notebook 05d checks the key identity for three unit vectors |

### 5.13 Irreducible under Pin(4,4), two inequivalent halves under Spin(4,4)

The author's statement about the field dirac16complex is that its 16 components transform under a 16-dimensional irreducible representation of Pin(4,4), and, for the transformations of determinant 1, under a direct sum of two inequivalent $8 \times 8$ irreducible representations of Spin(4,4). This section proves both halves of the statement.

**From a matrix equation to linear equations.** Every statement below is about an unknown matrix $X$ that obeys equations such as $\gamma^aX = X\gamma^a$. Let $X$ be an unknown $n \times m$ matrix, $L$ a known $n \times n$ matrix and $R$ a known $m \times m$ matrix. The entry $(r, c)$ of $LX - XR$ is

$$
(LX)_{rc} - (XR)_{rc} = \sum_k L_{rk}X_{kc} - \sum_k X_{rk}R_{kc} .
$$

So $LX - XR = 0$ is a list of $nm$ **linear equations** for the $nm$ entries of $X$: in the equation $(r, c)$ the unknown $X_{kc}$ has the coefficient $L_{rk}$ and the unknown $X_{rk}$ the coefficient $-R_{kc}$. Listing the unknowns row by row ($X_{11}, X_{12}, \dots$), these coefficients form the matrix

$$
A = \mathrm{kron}(L, 1_m) - \mathrm{kron}(1_n, R^T) ,
$$

with one row per equation and one column per unknown; $\mathrm{kron}(P, Q)$, the **Kronecker product**, is the big matrix whose block in block row $r$ and block column $k$ is $P_{rk}$ times the whole matrix $Q$. For a list of equations (for example one for each of the eight gammas) the coefficient matrices are stacked on top of each other. The solutions form a space of dimension (number of unknowns) minus (rank of $A$). The rank can be computed **exactly** by Gaussian elimination with fractions, without any rounding.

**A second, independent engine.** For the coefficient matrix $A$, the matrix $N = A^TA$ is symmetric, and $Ny = 0$ exactly when $Ay = 0$: if $Ny = 0$, then $0 = y^TNy = (Ay)^T(Ay)$, which is the sum of the squares of the entries of $Ay$, so $Ay = 0$; the converse is clear. So the dimension of the solution space equals the number of zero eigenvalues of $N$, which a floating-point eigenvalue program computes independently of the exact elimination.

**Theorem P (Pin(4,4) is irreducible).** The 16 components carry an irreducible representation of Pin(4,4), and only the multiples of $1$ commute with every element of Pin(4,4).

Proof, step by step.

- Step 1: the span of Pin(4,4) is the span of the 256 products of different gammas. Every product of different gammas is a product of unit vectors $\gamma(e_a)$, hence an element of Pin(4,4). Conversely, every element of Pin(4,4) is, by the multiplication argument of Section 5.12, a combination of products of different gammas.
- Step 2: the 256 products of different gammas are linearly independent. This is an exact computation: the $256 \times 256$ matrix of their entries has rank 256 (Revision record and Notebook 05b). 256 independent $16 \times 16$ matrices span the space of all $16 \times 16$ matrices, which has dimension 256.
- Step 3: by Lemma 3 of Section 5.11, the representation is irreducible and its commutant consists of the multiples of $1$.

The second engine confirms the commutant directly: the $8 \times 256 = 2048$ equations $\gamma^aX - X\gamma^a = 0$ ($a = x1, \dots, x8$) have rank 255, so their solutions form a space of dimension $256 - 255 = 1$, the multiples of $1$. (A matrix that commutes with the eight gammas commutes with all their products and combinations, hence with all of Pin(4,4); the converse holds because every gamma is in Pin(4,4).)

**Theorem S (two inequivalent halves under Spin(4,4)).** Under Spin(4,4) the 16 components split into the two chiral halves of 8 components (Section 5.5); each half carries an irreducible representation of Spin(4,4); the two are inequivalent; and the commutant of Spin(4,4) is spanned by $P_-$ and $P_+$.

Proof, step by step.

- Step 1: the span of Spin(4,4) is the span of the 128 even products of different gammas, by the argument of Theorem P restricted to even products (Section 5.12: an even element is a combination of even products; every even product of different gammas is an even element).
- Step 2: every even product is block diagonal (the block rule of Section 5.5), and the 128 even products are linearly independent (exact rank 128). The block-diagonal matrices $\mathrm{diag}(X, Y)$ form a space of dimension $64 + 64 = 128$. So the even products span exactly all block-diagonal matrices.
- Step 3: Lemma 4 of Section 5.11 gives all four claims.

**The same with the 28 generators.** The Revision record and Notebook 05b also compute the commutant of the 28 generators $S^{ab}$: dimension 2, spanned by $P_-$ and $P_+$; on each half the commutant of the 28 blocks has dimension 1; and the equations for an intertwiner between the halves have only the solution 0. A matrix commutes with every exponential $\exp(\theta S^{ab})$ (Section 5.18) exactly when it commutes with every $S^{ab}$ (take the derivative at $\theta = 0$ in one direction; in the other, a matrix that commutes with $S$ commutes with every power of $S$ and hence with the power series of the exponential). So these numbers show that the conclusions of Theorem S hold already for the part of Spin(4,4) made of products of exponentials, which Section 5.23 calls $\mathrm{Spin}_0(4,4)$.

**Why Pin(4,4) sees one block of 16.** Every gamma is an odd element of Pin(4,4), and every gamma exchanges the two halves (Section 5.5). So neither half is invariant under Pin(4,4): the two inequivalent halves of Spin(4,4) are joined by the reflections into one irreducible representation of Pin(4,4).

**Imposing the gammas one at a time.** How large is the commutant of only the first $j$ gammas? With no condition all 256 entries are free. The matrices that commute with $\gamma^{(x1)}$ are those that map each of its two eigenspaces into itself: if $\gamma v = \lambda v$ and $X\gamma = \gamma X$, then $\gamma(Xv) = X\gamma v = \lambda Xv$, so $Xv$ has the same eigenvalue; conversely a matrix that acts separately on the two eigenspaces commutes with $\gamma$. A real symmetric matrix has a basis of eigenvectors, and $\gamma^{(x1)}$ has eight eigenvalues $+1$ and eight $-1$ (Section 5.3), so there are $8^2 + 8^2 = 128$ free entries. Notebook 05b computes, exactly, that every further gamma halves the dimension again: $256, 128, 64, 32, 16, 8, 4, 2, 1$. (Only the first step is proved here; the whole sequence is COMPUTED.)

| statement | status | where it is verified |
| --- | --- | --- |
| the 256 products of different gammas are independent (rank 256) | PROVED (exact computation) | `python-algebra.json`, check `clifford_products_span_M16`; `wolfram-algebra.json`, check `Clifford_basis_spans_full_matrix_algebra` |
| Theorem P: commutant of the eight gammas has dimension 1 | PROVED | `python-algebra.json`, check `pin_commutant_dimension_1`; `wolfram-algebra.json`, check `Pin44_irreducible_commutant_dim_1` |
| the 128 even products are block diagonal and independent | PROVED (exact computation) | `python-algebra.json`, check `even_products_span_M8_plus_M8`; `wolfram-algebra.json`, check `even_subalgebra_dimension` |
| commutant of the 28 $S^{ab}$ has dimension 2, spanned by $P_-$, $P_+$ | PROVED | `python-algebra.json`, check `spin_commutant_dimension_2`; `wolfram-algebra.json`, check `Spin44_commutant_dim_2_chiral_projectors` |
| each half irreducible; the halves inequivalent (intertwiners 0) | PROVED | `python-algebra.json`, checks `spin_halves_irreducible` and `spin_halves_inequivalent`; `wolfram-algebra.json`, checks `chiral_halves_irreducible` and `chiral_halves_inequivalent_intertwiners_0` |
| the halving sequence 256, 128, ..., 1; the negative control gives 4 | COMPUTED (exact rank) | Notebook 05b (its own computation) |

### 5.14 Example: Notebook 05b computes the commutants

Notebook 05b turns every statement of Section 5.13 into a system of linear equations and computes its exact rank with sympy. It first tests the construction of the coefficient matrix on a random matrix and on a $2 \times 2$ warm-up that can be done by hand; then it computes the ranks of the 256 and of the 128 even products of different gammas, the commutant of the eight gammas, the commutants obtained by imposing the gammas one at a time, the commutant of the 28 generators, the commutants on each half, the intertwiners between the halves and the negative control with two equal halves. It confirms every dimension a second time with the zero eigenvalues of $A^TA$, and predicts all 256 eigenvalues of $A^TA$ for the eight gammas exactly. It draws five figures and ends with the line ALL 17 CHECKS PASSED (notebook 05b).

<!-- NOTEBOOK 05b -->

### 5.17 Line-by-line walk-through of Notebook 05b

The notebook has 17 code cells. In [1] is the set-up cell, word for word the one of Notebook 05a explained in Section 5.10, except the line `NOTEBOOK_ID = "05b"  # this notebook: chapter 05, example b`; its comment lines repeat the instructions of Section 5.15.

**In [2], the gammas and the recorded checks.**

```python
import contextlib  # lets a block of code print into a text buffer
import io  # the text buffer io.StringIO
import sys  # sys.stdout: the channel through which the notebook prints

import numpy as np  # arrays of numbers, matrices and linear algebra

fixture = json.loads(repository_file("Revision/algebra/gammas.json")
                     .read_text(encoding="utf-8"))
COORDS = fixture["coordinates"]  # "x1", ..., "x8"
ETA = dict(zip(COORDS, fixture["eta"]))  # +1 space-like, -1 time-like
gamma = {x: np.array(m, dtype=np.int64) for x, m in zip(COORDS, fixture["gamma"])}
I16 = np.eye(16, dtype=np.int64)  # the identity matrix 1
```

These lines load the modules and read the gammas exactly as In [2] and In [3] of Notebook 05a do (Section 5.10): `fixture` is the record, `COORDS` the coordinate names, `ETA` the signs $\eta_{aa}$, `gamma` the eight matrices of whole numbers and `I16` the identity.

```python
REPORT_FILES = {"python": "Revision/algebra/reports/python-algebra.json",
                "wolfram": "Revision/algebra/reports/wolfram-algebra.json"}
VERDICTS = {}  # (report key, check name) -> (verdict in lower case, detail text)
for key, path in REPORT_FILES.items():
    report_data = json.loads(repository_file(path).read_text(encoding="utf-8"))
    for entry in report_data["checks"]:
        VERDICTS[(key, entry["name"])] = (entry["verdict"].lower(), entry["detail"])


def recorded(key, name):
    return VERDICTS[(key, name)][0] == "pass"


def detail(key, name):
    return VERDICTS[(key, name)][1]


def record_of(key, name):
    return f"{REPORT_FILES[key]}, check {name}"


def check_reproduces(condition, name, record):
    collected = io.StringIO()
    with contextlib.redirect_stdout(collected):  # print into the buffer
        check(condition, name, record=record)  # stops here if the check fails
    sys.stdout.write(collected.getvalue())  # the PASS and reproduces lines together
```

The two reports are read and the helpers `recorded`, `record_of` and `check_reproduces` are defined as in Notebook 05a. The new helper `detail(key, name)` returns the detail text of a recorded check (`[1]`, the second element of the stored pair); several checks below compare a number with the number written in that text.

```python
clifford_ok = all(
    np.array_equal(gamma[x] @ gamma[y] + gamma[y] @ gamma[x],
                   2 * ETA[x] * I16 if x == y else 0 * I16)
    for x in COORDS for y in COORDS)
check_reproduces(clifford_ok and recorded("python", "clifford_relation"),
                 "{gamma^a, gamma^b} = 2 eta^ab 1 for all 64 pairs",
                 record=record_of("python", "clifford_relation"))
```

The Clifford relation is checked for the 64 pairs in one expression: `all(... for x in COORDS for y in COORDS)` runs through all pairs and is true when every comparison is; `0 * I16` is the zero matrix.

**In [3], the tools.**

```python
import sympy as sp  # exact algebra
from sympy.polys.matrices import DomainMatrix  # exact matrices over QQ


def commutation_system(lefts, rights):
    blocks = []
    for L, R in zip(lefts, rights):
        n, m = L.shape[0], R.shape[0]
        blocks.append(np.kron(L, np.eye(m, dtype=np.int64))
                      - np.kron(np.eye(n, dtype=np.int64), R.T))
    return np.vstack(blocks)  # the blocks stacked on top of each other
```

`commutation_system` builds the coefficient matrix of Section 5.13 for a list of equations $LX - XR = 0$, one for each pair $(L, R)$ of the two lists (`zip` pairs them). For each pair it reads the sizes $n$ and $m$, forms $\mathrm{kron}(L, 1_m) - \mathrm{kron}(1_n, R^T)$ with numpy's Kronecker product `np.kron`, and `np.vstack` stacks all blocks on top of each other.

```python
def exact_rank(A):
    return DomainMatrix.from_list(A.tolist(), sp.QQ).rank()


def solution_basis(A, n, m):
    null = DomainMatrix.from_list(A.tolist(), sp.QQ).nullspace().to_Matrix()
    return [np.array(null.row(k).tolist()[0], dtype=float).reshape(n, m)
            for k in range(null.rows)]
```

`DomainMatrix.from_list(..., sp.QQ)` makes an exact sympy matrix whose entries are rational numbers (`QQ` is sympy's name for the rational numbers). Its `.rank()` is computed by Gaussian elimination with fractions, without rounding. `.nullspace()` returns a basis of the solutions of $Ay = 0$, one solution per row; `.to_Matrix()` turns it into an ordinary sympy matrix. `solution_basis` takes each row (`null.row(k)`), turns it into a numpy array of floating-point numbers and reshapes the $nm$ numbers into an $n \times m$ matrix (the unknowns were listed row by row, so `reshape` restores the matrix).

```python
rng = np.random.default_rng(12345)  # random numbers with a fixed seed
X = rng.integers(-5, 6, size=(16, 16))  # a random 16 x 16 matrix, entries -5..5
L, R = gamma["x1"], gamma["x4"]
A = commutation_system([L], [R])
say(f"one pair (L, R) gives {A.shape[0]} equations for {A.shape[1]} unknowns")
check(np.array_equal(A @ X.reshape(256), (L @ X - X @ R).reshape(256)),
      "the coefficient matrix applied to X row by row gives L X - X R")
```

The construction is tested before it is used. `np.random.default_rng(12345)` is a random-number generator started with the fixed **seed** 12345, so that every run draws the same numbers; `rng.integers(-5, 6, size=(16, 16))` draws a $16 \times 16$ matrix of whole numbers from $-5$ to $5$ (the upper end 6 is excluded). For $L = \gamma^{(x1)}$ and $R = \gamma^{(x4)}$ the coefficient matrix has 256 rows and 256 columns (printed). The check multiplies it with the 256 entries of $X$ listed row by row (`X.reshape(256)`) and compares the result with the entries of $LX - XR$ listed in the same order.

**In [4], the warm-up.**

```python
M = np.array([[0, 1], [1, 0]], dtype=np.int64)
A_small = commutation_system([M], [M])  # 4 equations for the 4 entries p, q, r, s
rank_small = exact_rank(A_small)
basis_small = solution_basis(A_small, 2, 2)
say(f"coefficient matrix (rows = equations, columns = p, q, r, s):")
for row in A_small.tolist():
    say(f"    {row}")
say(f"rank {rank_small}; dimension of the solution space {4 - rank_small}")
for k, b in enumerate(basis_small, 1):
    say(f"basis solution {k}: rows {b.astype(int).tolist()}")
check(rank_small == 2 and len(basis_small) == 2,
      "warm-up: the 2 x 2 matrices commuting with M form a space of dimension 2")
```

For $M = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ and $X = \begin{pmatrix} p & q \\ r & s \end{pmatrix}$ the equation $MX - XM = 0$ reads $r - q = 0$, $s - p = 0$, $p - s = 0$, $q - r = 0$, the four printed rows of coefficients (columns $p, q, r, s$). Two of them repeat the other two, so the rank is 2 and the solution space has dimension $4 - 2 = 2$. `enumerate(basis_small, 1)` numbers the basis solutions from 1; `.astype(int)` turns them into whole numbers for printing. The two printed solutions are $M$ itself and the identity, as the hand computation of the notebook's text predicts.

**In [5], the 256 products of different gammas.**

```python
import itertools  # subsets of a given size
from math import comb  # comb(8, k): the number of subsets of size k

products = {}  # degree k -> list of the Clifford products of degree k
for k in range(9):
    products[k] = []
    for subset in itertools.combinations(COORDS, k):
        p = I16
        for x in subset:
            p = p @ gamma[x]
        products[k].append(p)
```

For each degree $k = 0, \dots, 8$ the cell lists every subset of $k$ directions in the order $x1, \dots, x8$ and multiplies their gammas; for $k = 0$ the only subset is empty and the product is the identity. `products[k]` is the list of the $\binom{8}{k}$ products of degree $k$; `comb(8, k)` from the module `math` computes this binomial number.

```python
rows_all = np.array([p.reshape(256) for k in range(9) for p in products[k]])
rows_even = np.array([p.reshape(256) for k in (0, 2, 4, 6, 8) for p in products[k]])
rank_all, rank_even = exact_rank(rows_all), exact_rank(rows_even)
cumulative = []  # the rank after adding the degrees 0, 1, ..., k
for k in range(9):
    cumulative.append(exact_rank(np.array(
        [p.reshape(256) for j in range(k + 1) for p in products[j]])))
```

Each product is written as one row of 256 numbers (`reshape(256)`), giving a $256 \times 256$ array for all products and a $128 \times 256$ array for the even ones; their exact ranks are computed. `cumulative[k]` is the rank of all products of degrees 0 to $k$.

```python
for k in range(9):
    say(f"degree {k}: {len(products[k]):2d} products (comb(8, {k}) = {comb(8, k):2d});"
        f" rank of all products up to degree {k}: {cumulative[k]}")
say(f"rank of all 256 products: {rank_all}; rank of the 128 even products: "
    f"{rank_even}")
check_reproduces(rank_all == 256 and f"rank {rank_all} (Fraction elimination)"
                 in detail("python", "clifford_products_span_M16")
                 and recorded("python", "clifford_products_span_M16")
                 and recorded("wolfram", "Clifford_basis_spans_full_matrix_algebra"),
                 "the 256 Clifford products are independent: they span all 16 x 16 "
                 "matrices",
                 record=record_of("python", "clifford_products_span_M16"))
```

The nine printed lines show the numbers of products 1, 8, 28, 56, 70, 56, 28, 8, 1 and the cumulative ranks 1, 9, 37, 93, 163, 219, 247, 255, 256: each degree raises the rank by exactly the number of its products, so no product is a combination of the others. (`{len(products[k]):2d}` writes a whole number in two places.) The check requires the rank 256 and that the recorded detail text contains the words `rank 256 (Fraction elimination)`: the record found the same number.

```python
even_diagonal = all(not p[:8, 8:].any() and not p[8:, :8].any()
                    for k in (0, 2, 4, 6, 8) for p in products[k])
odd_off = all(not p[:8, :8].any() and not p[8:, 8:].any()
              for k in (1, 3, 5, 7) for p in products[k])
check_reproduces(rank_even == 128 and even_diagonal and odd_off
                 and f"rank {rank_even} (Fraction)"
                 in detail("python", "even_products_span_M8_plus_M8")
                 and recorded("python", "even_products_span_M8_plus_M8")
                 and recorded("wolfram", "even_subalgebra_dimension"),
                 "the 128 even products are block diagonal and independent (64 + 64); "
                 "the odd ones are block off-diagonal",
                 record=record_of("python", "even_products_span_M8_plus_M8"))
```

`p[:8, 8:]` is the top-right block (rows 1 to 8, columns 9 to 16) and `p[8:, :8]` the bottom-left block; `.any()` is true when some entry is not zero. So `even_diagonal` says that every even product has zero off-diagonal blocks, and `odd_off` that every odd product has zero diagonal blocks, the block rule of Section 5.5. The check adds the rank 128 and the recorded number.

**In [6], the picture of the products and ranks.**

```python
from matplotlib.patches import Patch  # a coloured square for a legend

degrees = np.arange(9)
counts = [len(products[k]) for k in range(9)]
colors = ["#2a78d6" if k % 2 == 0 else "#eb6834" for k in range(9)]
fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2))
axes[0].bar(degrees, counts, color=colors, edgecolor="white", linewidth=2)
for k in range(9):
    axes[0].text(k, counts[k] + 1.5, str(counts[k]), ha="center")
axes[0].set_xlabel("degree $k$ (number of different gammas multiplied)")
axes[0].set_ylabel("number of products")
axes[0].set_title(r"$\binom{8}{k}$ products of degree $k$")
axes[0].set_ylim(0, 80)
axes[0].legend(handles=[Patch(color="#2a78d6", label="even degree"),
                        Patch(color="#eb6834", label="odd degree")],
               loc="upper right")
```

`np.arange(9)` is the array $0, 1, \dots, 8$. `k % 2` is the remainder of $k$ divided by 2, so even degrees get blue and odd degrees orange. `axes[0].bar` draws one bar per degree with the height of its count, and `text` writes the count just above each bar. A `Patch` is a coloured square for a legend that is made by hand (the bars themselves carry no labels).

```python
added = np.cumsum(counts)  # how many products have been added up to degree k
axes[1].plot(added, cumulative, "o-", color="#2a78d6", linewidth=2, markersize=8,
             label="exact rank")
axes[1].plot([0, 256], [0, 256], ":", color="black", linewidth=1,
             label="rank = number of products")
axes[1].set_xlabel("number of products added (degrees 0 to $k$)")
axes[1].set_ylabel("rank")
axes[1].set_title("The rank grows by one for every product")
axes[1].legend(loc="upper left")
save_figure(fig, "clifford_products", ...)
```

`np.cumsum` adds up the counts: 1, 9, 37, 93, 163, 219, 247, 255, 256 products after the degrees 0 to $k$. The right picture plots the cumulative ranks against these numbers (`"o-"` draws dots joined by lines) and the dotted line rank = number of products. In `05b_1_clifford_products.png` the dots lie exactly on the dotted line.

**In [7], the commutant of the eight gammas.**

```python
gammas = [gamma[x] for x in COORDS]
A_pin = commutation_system(gammas, gammas)  # 8 x 256 = 2048 equations
rank_pin = exact_rank(A_pin)
basis_pin = solution_basis(A_pin, 16, 16)
dimension_pin = 256 - rank_pin
say(f"equations {A_pin.shape[0]}, unknowns {A_pin.shape[1]}, rank {rank_pin}, "
    f"dimension of the commutant {dimension_pin}")
```

With $L = R = \gamma^a$ the equations $\gamma^aX - X\gamma^a = 0$ say that $X$ commutes with $\gamma^a$; for the eight gammas they are $2048$ equations for 256 unknowns. The printed line shows the rank 255 and the dimension $256 - 255 = 1$.

```python
only = basis_pin[0]
proportional = np.array_equal(only / only[0, 0], np.eye(16))  # a multiple of 1?
say(f"the basis solution divided by its entry (1,1) equals the identity: "
    f"{proportional}")
check_reproduces(dimension_pin == 1 and len(basis_pin) == 1 and proportional
                 and f"= {dimension_pin} (Fraction)"
                 in detail("python", "pin_commutant_dimension_1")
                 and recorded("python", "pin_commutant_dimension_1")
                 and recorded("wolfram", "Pin44_irreducible_commutant_dim_1"),
                 "only the multiples of 1 commute with all eight gammas: Pin(4,4) acts "
                 "irreducibly on the 16 components",
                 record=record_of("python", "pin_commutant_dimension_1"))
```

The only basis solution is divided by its entry in row 1, column 1 (`only[0, 0]`), and the result is compared with the identity: True. The check is Theorem P, with the recorded dimension.

**In [8], the second engine.**

```python
N_pin = A_pin.T @ A_pin  # 256 x 256, whole numbers, symmetric
eigen_pin = np.linalg.eigvalsh(N_pin.astype(float))  # sorted from small to large
zeros_pin = int(np.sum(np.abs(eigen_pin) < 1e-9))
say(f"numpy: eigenvalues of A^T A below 1e-9: {zeros_pin}")
```

$N = A^TA$ is computed in whole numbers, its 256 eigenvalues in floating-point numbers, and the eigenvalues below $10^{-9}$ in size are counted: exactly one, the dimension of the commutant again.

```python
predicted = []  # the eigenvalue 4 n(P) of every Clifford product P
exact_eigenvectors = True
for k in range(9):
    n_anti = k if k % 2 == 0 else 8 - k  # gammas anticommuting with a product
    for p in products[k]:
        predicted.append(4 * n_anti)
        exact_eigenvectors &= np.array_equal(N_pin @ p.reshape(256),
                                             4 * n_anti * p.reshape(256))
```

The notebook's text explains why every product $P$ of different gammas, written as a row of 256 numbers, is an eigenvector of $N$ with the eigenvalue $4n(P)$, where $n(P)$ is the number of gammas that anticommute with $P$. By Rule 1 of Section 5.3, a product of even degree $k$ anticommutes with its $k$ factors and commutes with the others, so $n = k$; a product of odd degree anticommutes with the $8 - k$ gammas that are not factors, so $n = 8 - k$. The loop collects the predicted eigenvalue of each product and checks the eigenvector equation exactly (`&=` keeps `exact_eigenvectors` true only while every test passes).

```python
predicted = np.sort(np.array(predicted))
values, multiplicities = np.unique(predicted, return_counts=True)
say("predicted eigenvalues of A^T A, written value x multiplicity:")
say("    " + ", ".join(f"{v} x {c}" for v, c in zip(values, multiplicities)))
check(exact_eigenvectors and zeros_pin == 1
      and np.max(np.abs(eigen_pin - predicted)) < 1e-9,
      "A^T A has exactly one zero eigenvalue; every Clifford product P is an "
      "eigenvector with eigenvalue 4 n(P)")
```

The 256 predicted eigenvalues are sorted; `np.unique(..., return_counts=True)` lists each different value once together with how often it occurs. The printed line reads 0 x 1, 4 x 8, 8 x 28, ..., 32 x 1: the value $4n$ occurs as often as there are products with that $n$. The check requires the exact eigenvector equations, one zero eigenvalue, and that numpy's sorted eigenvalues agree with the sorted predictions to within $10^{-9}$. The 256 products are independent, so they are all the eigenvectors, and the prediction is the complete list.

**In [9], imposing the gammas one at a time.**

```python
halving = [256]  # dimension of the commutant of the first j gammas, j = 0, 1, ..., 8
for j in range(1, 9):
    A_j = commutation_system(gammas[:j], gammas[:j])
    halving.append(256 - exact_rank(A_j))
for j in range(9):
    names = ", ".join(COORDS[:j]) if j else "none"
    say(f"gammas imposed: {j} ({names}); commutant dimension {halving[j]}")
check(halving == [256 // 2 ** j for j in range(9)],
      "every further gamma halves the commutant: 256, 128, 64, ..., 2, 1")
```

`gammas[:j]` is the list of the first $j$ gammas. For $j = 1, \dots, 8$ the exact dimension of their commutant is appended to `halving`, which starts with 256 (no condition). The printed lines show 256, 128, 64, 32, 16, 8, 4, 2, 1, and the check compares the list with $256/2^j$ (`2 ** j` is $2^j$; `//` divides whole numbers).

**In [10], the 28 generators.**

```python
pairs = [(a, b) for i, a in enumerate(COORDS) for b in COORDS[i + 1:]]  # 28 pairs
S = {(a, b): (gamma[a] @ gamma[b] - gamma[b] @ gamma[a]) / 4 for a, b in pairs}
entries = sorted({float(v) for s in S.values() for v in s.flat})
say(f"{len(S)} generators S^ab; their entries are {entries}")
```

`enumerate(COORDS)` gives each name with its position `i`; `COORDS[i + 1:]` is the list of the names after it, so `pairs` lists the 28 planes $(a, b)$ with $a$ before $b$. `S` stores $\tfrac14(\gamma^a\gamma^b - \gamma^b\gamma^a)$ for each plane; the division by 4 makes floating-point numbers, but halves are stored exactly. The printed line shows 28 generators with the entries $-0.5$, $0$, $0.5$.

```python
check_reproduces(len(S) == 28 and entries == [-0.5, 0.0, 0.5]
                 and all(np.array_equal(S[(a, b)], gamma[a] @ gamma[b] / 2)
                         for a, b in pairs)
                 and recorded("python", "S_definition"),
                 "S^ab = (1/4)[gamma^a, gamma^b] = (1/2) gamma^a gamma^b: 28 matrices "
                 "with entries 0, +1/2, -1/2",
                 record=record_of("python", "S_definition"))
check_reproduces(all(not s[:8, 8:].any() and not s[8:, :8].any() for s in S.values())
                 and recorded("python", "S_block_diagonal"),
                 "every S^ab is block diagonal: it maps each chiral half into itself",
                 record=record_of("python", "S_block_diagonal"))
```

The first check confirms $S^{ab} = \tfrac12\gamma^a\gamma^b$ and the entries; the second that every generator is block diagonal (it is even).

**In [11], the commutant of the generators.**

```python
generators = [(gamma[a] @ gamma[b]).astype(np.int64) for a, b in pairs]  # 2 S^ab
A_spin = commutation_system(generators, generators)  # 7168 equations
rank_spin = exact_rank(A_spin)
basis_spin = solution_basis(A_spin, 16, 16)
dimension_spin = 256 - rank_spin
```

For the exact computation the cell uses the whole-number matrices $2S^{ab} = \gamma^a\gamma^b$, which have the same commutant as the $S^{ab}$ (a matrix commutes with $S$ exactly when it commutes with $2S$). The $28 \times 256 = 7168$ equations have the exact rank 254 and a solution space of dimension 2.

```python
P_minus = np.diag([1] * 8 + [0] * 8)  # diag(1_8, 0): components 1 to 8
P_plus = np.diag([0] * 8 + [1] * 8)  # diag(0, 1_8): components 9 to 16
together = np.array([b.reshape(256) for b in basis_spin]
                    + [P_minus.reshape(256), P_plus.reshape(256)])
same_span = np.linalg.matrix_rank(together) == 2  # four matrices, two directions
eigen_spin = np.linalg.eigvalsh((A_spin.T @ A_spin).astype(float))
zeros_spin = int(np.sum(np.abs(eigen_spin) < 1e-9))
```

`np.diag(list)` makes the diagonal matrix with the listed diagonal: the two projectors. The two basis solutions and the two projectors, written as rows, form four rows; if their rank is 2, the two pairs span the same space (`np.linalg.matrix_rank` computes a floating-point rank, which is reliable for such small whole numbers). The second engine counts the zero eigenvalues of $A^TA$.

```python
say(f"equations {A_spin.shape[0]}, rank {rank_spin}, dimension {dimension_spin}; "
    f"numpy: zero eigenvalues of A^T A: {zeros_spin}")
say(f"the basis and P_-, P_+ span the same space: {same_span}")
check_reproduces(dimension_spin == 2 and zeros_spin == 2 and same_span
                 and f"= {dimension_spin} (Fraction)"
                 in detail("python", "spin_commutant_dimension_2")
                 and recorded("python", "spin_commutant_dimension_2")
                 and recorded("wolfram", "Spin44_commutant_dim_2_chiral_projectors"),
                 "the commutant of the 28 S^ab has dimension 2, spanned by P_- and P_+",
                 record=record_of("python", "spin_commutant_dimension_2"))
```

The printed lines report 7168 equations, rank 254, dimension 2, two zero eigenvalues and True. The check confirms the recorded dimension 2.

**In [12], the picture of the eigenvalues of $A^TA$.**

```python
fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2))
for ax, eig, zeros, title in [
        (axes[0], eigen_pin, zeros_pin, "eight gammas (Pin(4,4))"),
        (axes[1], eigen_spin, zeros_spin, "28 generators $S^{ab}$ (Spin(4,4))")]:
    index = np.arange(1, 257)  # the eigenvalues numbered 1 to 256
    ax.plot(index, eig, color="#2a78d6", linewidth=2, label="eigenvalue")
    ax.plot(index[:zeros], eig[:zeros], "o", color="#eb6834", markersize=9,
            label=f"zero eigenvalues: {zeros}")
    ax.set_xlabel("number of the eigenvalue (sorted)")
    ax.set_title(f"$A^T A$ for the {title}")
    ax.legend(loc="lower right")
axes[0].set_ylabel("eigenvalue of $A^T A$")
save_figure(fig, "system_eigenvalues", ...)
```

The loop draws the same kind of picture for the two systems: the sorted eigenvalues against their numbers 1 to 256 (`np.arange(1, 257)`), and orange dots on the first `zeros` of them, the zero eigenvalues. In `05b_2_system_eigenvalues.png` the left curve climbs in the steps 0, 4, 8, ..., 32 with one dot at 0; the right curve has two dots at 0.

**In [13], the picture of the halving.**

```python
fig, ax = plt.subplots(figsize=(7.0, 4.2))
ax.plot(range(9), halving, "o-", color="#2a78d6", linewidth=2, markersize=8)
for j in range(9):
    ax.annotate(str(halving[j]), (j, halving[j]), textcoords="offset points",
                xytext=(8, 4))
ax.set_yscale("log", base=2)
ax.set_yticks([1, 4, 16, 64, 256], ["1", "4", "16", "64", "256"])
ax.set_xticks(range(9), ["none"] + COORDS)
ax.set_xlabel("gammas imposed, in the order x1, x2, ..., x8 (the last one named)")
ax.set_ylabel("dimension of the commutant")
ax.set_title("Each further gamma halves the commutant")
save_figure(fig, "commutant_halving", ...)
```

The nine dimensions are drawn against the number of gammas imposed; `annotate` writes each value next to its dot, shifted by 8 and 4 points. `set_yscale("log", base=2)` makes the vertical axis logarithmic with base 2, so that each halving is a step of the same size and the dots lie on a straight line. In `05b_3_commutant_halving.png` the line descends evenly from 256 to 1.

**In [14], the picture of the Spin(4,4) commutant.**

```python
from matplotlib.colors import LinearSegmentedColormap

# What the caption below says about the two basis matrices, checked: each is
# diagonal, has no negative entry, and is constant on each half (rows 1-8, 9-16).
shapes_ok = all(np.array_equal(b, np.diag(np.diag(b))) and b.min() >= 0
                and len(set(np.diag(b)[:8].tolist())) == 1
                and len(set(np.diag(b)[8:].tolist())) == 1 for b in basis_spin)
check(shapes_ok, "the two basis matrices are diagonal, nonnegative and constant on "
      "each half")
```

Before drawing, the cell checks what the caption says. `np.diag(b)` of a matrix is its diagonal, and `np.diag` of that list is the diagonal matrix with it; equality means that `b` is diagonal. `b.min() >= 0` says no entry is negative. `set(...)` of the first eight diagonal entries has one element exactly when they are all equal; the same for the last eight.

```python
SIGNS = LinearSegmentedColormap.from_list("signs", ["#2a78d6", "#f0efec", "#e34948"])
pictures = [(basis_spin[0], "sympy basis matrix 1"),
            (basis_spin[1], "sympy basis matrix 2"),
            (P_minus, "$P_- = \\mathrm{diag}(1_8, 0)$"),
            (P_plus, "$P_+ = \\mathrm{diag}(0, 1_8)$")]
fig, axes = plt.subplots(1, 4, figsize=(13.0, 3.9))
for k, (ax, (matrix, title)) in enumerate(zip(axes, pictures)):
    image = ax.imshow(matrix, cmap=SIGNS, vmin=-1, vmax=1)
    ax.set_title(title)
    ax.set_xticks([0, 7, 15], ["1", "8", "16"])
    ax.set_yticks([0, 7, 15], ["1", "8", "16"])
    ax.axhline(7.5, color="black", linewidth=0.8)
    ax.axvline(7.5, color="black", linewidth=0.8)
    ax.set_xlabel("column")
    if k == 0:
        ax.set_ylabel("row")
    ax.grid(False)
fig.colorbar(image, ax=axes, ticks=[-1, 0, 1], shrink=0.8, label="matrix entry")
save_figure(fig, "spin_commutant", ...)
```

The colour map of Notebook 05a is made again. `pictures` pairs the four matrices with their titles; in an ordinary string a backslash must be doubled, so `"\\mathrm"` gives `\mathrm`. The loop draws each as a heat map with the half lines (`enumerate` gives the number `k` of each picture, so that only the first gets the word row). `05b_4_spin_commutant.png` shows four diagonal matrices, each grey or red, constant on each half.

**In [15], the two halves.**

```python
minus_blocks = [g[:8, :8] for g in generators]  # the blocks of 2 S^ab on half -
plus_blocks = [g[8:, 8:] for g in generators]  # the blocks of 2 S^ab on half +
dim_minus = 64 - exact_rank(commutation_system(minus_blocks, minus_blocks))
dim_plus = 64 - exact_rank(commutation_system(plus_blocks, plus_blocks))
dim_minus_plus = 64 - exact_rank(commutation_system(minus_blocks, plus_blocks))
dim_plus_minus = 64 - exact_rank(commutation_system(plus_blocks, minus_blocks))
```

`minus_blocks` are the top-left $8 \times 8$ blocks of the 28 matrices $2S^{ab}$, `plus_blocks` the bottom-right ones. Each system has $28 \times 64$ equations for the 64 entries of an $8 \times 8$ unknown $X$. With the pairs $(L, R) = (S_-, S_-)$ the solutions are the commutant on the first half; with $(S_+, S_+)$ on the second; with $(S_-, S_+)$ they are the $X$ with $S_-X = XS_+$, the intertwiners from the second half to the first; with $(S_+, S_-)$ those in the other direction.

```python
Z8 = np.zeros((8, 8), dtype=np.int64)
doubled = [np.block([[m, Z8], [Z8, m]]) for m in minus_blocks]  # the control
dim_control = 256 - exact_rank(commutation_system(doubled, doubled))
say(f"commutant on half -: {dim_minus}; on half +: {dim_plus}")
say(f"intertwiners: {dim_minus_plus} and {dim_plus_minus}")
say(f"control (two copies of half -): commutant dimension {dim_control}")
```

The negative control builds artificial $16 \times 16$ matrices $\mathrm{diag}(S_-, S_-)$ with the same block twice and computes their commutant. The printed lines show the dimensions 1 and 1, the intertwiners 0 and 0, and 4 for the control.

```python
check_reproduces(dim_minus == 1 and dim_plus == 1
                 and "dimension 1 (sympy 1)"
                 in detail("python", "spin_halves_irreducible")
                 and recorded("python", "spin_halves_irreducible")
                 and recorded("wolfram", "chiral_halves_irreducible"),
                 "each chiral half is an irreducible representation of Spin(4,4)",
                 record=record_of("python", "spin_halves_irreducible"))
check_reproduces(dim_minus_plus == 0 and dim_plus_minus == 0
                 and "dimension 0 (sympy 0)"
                 in detail("python", "spin_halves_inequivalent")
                 and recorded("python", "spin_halves_inequivalent")
                 and recorded("wolfram", "chiral_halves_inequivalent_intertwiners_0"),
                 "the two halves are inequivalent: the only intertwiner is zero",
                 record=record_of("python", "spin_halves_inequivalent"))
check(dim_control == 4,
      "negative control: two copies of the same half give commutant dimension 4")
```

The three checks state Theorem S in the form of the record (irreducible halves, no intertwiner) and the control value 4 of Lemma 4.

**In [16], why Pin(4,4) sees one block, and the dimensions.**

```python
check_reproduces(all(np.array_equal(gamma[x] @ P_minus, P_plus @ gamma[x])
                     for x in COORDS)
                 and recorded("python", "reflections_exchange_halves"),
                 "gamma^a P_- = P_+ gamma^a: every reflection exchanges the two halves",
                 record=record_of("python", "reflections_exchange_halves"))
```

The check repeats the fact of Section 5.5 that every gamma exchanges the halves.

```python
labels = ["Pin(4,4) on all 16", "Spin(4,4) on all 16", "Spin(4,4) on half -",
          "Spin(4,4) on half +", "intertwiners - to +", "intertwiners + to -",
          "control: two equal halves"]
values = [dimension_pin, dimension_spin, dim_minus, dim_plus, dim_minus_plus,
          dim_plus_minus, dim_control]
colors = ["#2a78d6"] * 6 + ["#eb6834"]  # blue: the theory, orange: the control
fig, ax = plt.subplots(figsize=(8.0, 4.4))
positions = np.arange(len(labels))[::-1]  # the first label at the top
ax.barh(positions, values, color=colors, edgecolor="white", linewidth=2)
for y, v in zip(positions, values):
    ax.text(v + 0.06, y, str(v), va="center")
ax.set_yticks(positions, labels)
ax.set_xlim(0, 4.6)
ax.set_xlabel("dimension of the space of solutions")
ax.set_title("Commutants and intertwiners")
legend_squares = [Patch(color="#2a78d6", label="the author's spinor (computed)"),
                  Patch(color="#eb6834", label="negative control (artificial)")]
ax.legend(handles=legend_squares, loc="upper right")
save_figure(fig, "dimensions", ...)
```

The seven computed dimensions are drawn as horizontal bars (`barh`), six blue and the control orange. `[::-1]` reverses the array of positions, so that the first label stands at the top; each value is written just right of its bar. `05b_5_dimensions.png` shows the bars 1, 2, 1, 1, 0, 0 and the orange bar 4.

**In [17], the last check.**

```python
FIGURES = ["05b_1_clifford_products.png", "05b_2_system_eigenvalues.png",
           "05b_3_commutant_halving.png", "05b_4_spin_commutant.png",
           "05b_5_dimensions.png"]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in FIGURES),
      "the five figure files of notebook 05b exist")
all_checks_passed()
```

The five figure files must exist, and the last line reads ALL 17 CHECKS PASSED (notebook 05b): one check each in In [2], In [3], In [4], In [7], In [8], In [9], In [11], In [14], In [16] and In [17], two each in In [5] and In [10], and three in In [15]. Ten of them reproduce recorded checks; the other seven (in In [3], In [4], In [8], In [9], In [14], the control in In [15], and In [17]) are the notebook's own computations.

### 5.18 Spin transformations: rotations, boosts and the double cover

A **spin transformation** is a $16 \times 16$ matrix $R$ that acts on the components, $\Psi \to R\Psi$, and at the same time turns the eight directions into each other. This section builds them from the generators and proves how they act.

**The commutation rules of so(4,4).** The **commutator** of two matrices is $[M, N] = MN - NM$. For commutators the **product rule** $[A, BC] = [A, B]C + B[A, C]$ holds, because both sides are $ABC - BCA$ (on the right, $ABC - BAC + BAC - BCA$). For $c \neq d$, $S^{cd} = \tfrac12\gamma^c\gamma^d$, and the product rule with the vector rule of Section 5.12 gives

$$
[S^{ab}, \gamma^c\gamma^d] = (\eta^{bc}\gamma^a - \eta^{ac}\gamma^b)\gamma^d + \gamma^c(\eta^{bd}\gamma^a - \eta^{ad}\gamma^b) .
$$

Each product of two gammas is $\gamma^x\gamma^y = \tfrac12[\gamma^x, \gamma^y] + \tfrac12\{\gamma^x, \gamma^y\} = 2S^{xy} + \eta^{xy}1$ (the Clifford relation for the second part). Inserting this, the four number terms $\eta^{bc}\eta^{ad} - \eta^{ac}\eta^{bd} + \eta^{bd}\eta^{ca} - \eta^{ad}\eta^{cb}$ cancel in pairs, and with $S^{ca} = -S^{ac}$, $S^{cb} = -S^{bc}$ and a division by 2:

$$
[S^{ab}, S^{cd}] = \eta^{bc}S^{ad} - \eta^{ac}S^{bd} - \eta^{bd}S^{ac} + \eta^{ad}S^{bc} .
$$

These are the commutation rules of the **Lie algebra so(4,4)**, the algebra of infinitesimal turnings of the 4+4 directions. The Revision record checks them for all $28 \times 28 = 784$ pairs of generators.

**The exponential of a matrix.** For a square matrix $M$ the **exponential** is the power series

$$
\exp(M) = 1 + M + \tfrac12M^2 + \tfrac16M^3 + \dots = \sum_{k \ge 0}\frac{M^k}{k!} ,
$$

the same series as for $e^x$; it converges for every square matrix (a fact of analysis, quoted here without proof). Fix a plane $(a, b)$ with $a \neq b$ and put $J = \gamma^a\gamma^b = 2S^{ab}$, so that $\theta S^{ab} = \tfrac\theta2J$. Then

$$
JJ = \gamma^a\gamma^b\gamma^a\gamma^b = -\gamma^a\gamma^a\gamma^b\gamma^b = -\eta_{aa}\eta_{bb}\,1 ,
$$

where the second step exchanges the two middle factors (they anticommute) and the third is the Clifford relation twice.

- **Rotation** ($\eta_{aa}\eta_{bb} = +1$): $JJ = -1$, so $J^{2n} = (-1)^n$ and $J^{2n+1} = (-1)^nJ$. Splitting the series into even and odd powers and using the power series of cosine and sine, $\exp(\tfrac\theta2J) = \cos\tfrac\theta2\;1 + \sin\tfrac\theta2\;J$.
- **Boost** ($\eta_{aa}\eta_{bb} = -1$): $JJ = +1$, every power has the sign $+$, and the series of $\cosh x = \tfrac12(e^x + e^{-x})$ and $\sinh x = \tfrac12(e^x - e^{-x})$ give $\exp(\tfrac\theta2J) = \cosh\tfrac\theta2\;1 + \sinh\tfrac\theta2\;J$.

In both cases the inverse is $\exp(-\theta S^{ab})$: $(c1 + sJ)(c1 - sJ) = c^2 - s^2JJ$, which is $\cos^2 + \sin^2 = 1$ for a rotation and $\cosh^2 - \sinh^2 = 1$ for a boost (from the definitions, $\cosh^2x - \sinh^2x = \tfrac14[(e^{2x} + 2 + e^{-2x}) - (e^{2x} - 2 + e^{-2x})] = 1$). The number $\theta$ is called the **angle** of a rotation and the **rapidity** of a boost.

**How a rotation moves the directions: the half angle.** Take the rotation in the plane $(x1, x2)$: $R = c1 + sJ$ with $J = \gamma^{(x1)}\gamma^{(x2)}$, $c = \cos\tfrac\theta2$, $s = \sin\tfrac\theta2$. By Rule 1, $J$ anticommutes with $\gamma^{(x1)}$ and $\gamma^{(x2)}$ (a factor of a product of two: sign $(-1)^1$) and commutes with the other six gammas. Line by line:

$$
R\gamma^{(x1)} = \gamma^{(x1)}(c1 - sJ) = \gamma^{(x1)}R^{-1}, \qquad \text{so} \qquad R\gamma^{(x1)}R^{-1} = \gamma^{(x1)}(c1 - sJ)^2 .
$$

The first step moves $\gamma^{(x1)}$ to the left through $J$ (a sign); the second multiplies from the right by $R^{-1} = c1 - sJ$. Now

$$
(c1 - sJ)^2 = c^2 - 2csJ + s^2JJ = (c^2 - s^2)1 - 2cs\,J = \cos\theta\,1 - \sin\theta\,J ,
$$

by $JJ = -1$ and the double-angle formulas $\cos^2\tfrac\theta2 - \sin^2\tfrac\theta2 = \cos\theta$ and $2\sin\tfrac\theta2\cos\tfrac\theta2 = \sin\theta$. With $\gamma^{(x1)}J = \gamma^{(x1)}\gamma^{(x1)}\gamma^{(x2)} = \gamma^{(x2)}$:

$$
R\gamma^{(x1)}R^{-1} = \cos\theta\,\gamma^{(x1)} - \sin\theta\,\gamma^{(x2)} .
$$

In the same way $R\gamma^{(x2)}R^{-1} = \gamma^{(x2)}(\cos\theta\,1 - \sin\theta\,J) = \cos\theta\,\gamma^{(x2)} + \sin\theta\,\gamma^{(x1)}$ (because $\gamma^{(x2)}\gamma^{(x1)}\gamma^{(x2)} = -\gamma^{(x1)}\gamma^{(x2)}\gamma^{(x2)} = -\gamma^{(x1)}$), and $R\gamma^cR^{-1} = \gamma^c$ for the other six directions. So conjugation by $R$ turns the directions $x1$ and $x2$ by the **full** angle $\theta$, while $R$ itself contains only the **half** angle $\theta/2$. At $\theta = 2\pi$ the directions are back where they started, but

$$
R(2\pi) = \cos\pi\;1 + \sin\pi\;J = -1 .
$$

A turn by $2\pi$ multiplies every spinor by $-1$; only a turn by $4\pi$ gives $R = +1$. This is the defining property of spinors.

**How a boost moves the directions.** For the boost in the plane $(x1, x4)$, $J = \gamma^{(x1)}\gamma^{(x4)}$ with $JJ = +1$, $c = \cosh\tfrac\theta2$ and $s = \sinh\tfrac\theta2$. The same steps give $R\gamma^{(x1)}R^{-1} = \gamma^{(x1)}(c1 - sJ)^2$ with $(c1 - sJ)^2 = (c^2 + s^2)1 - 2cs\,J = \cosh\theta\,1 - \sinh\theta\,J$; here $\cosh^2x + \sinh^2x = \cosh 2x$ and $2\sinh x\cosh x = \sinh 2x$ follow from the definitions by multiplying out, as above. Hence

$$
R\gamma^{(x1)}R^{-1} = \cosh\theta\,\gamma^{(x1)} - \sinh\theta\,\gamma^{(x4)}, \qquad R\gamma^{(x4)}R^{-1} = \cosh\theta\,\gamma^{(x4)} - \sinh\theta\,\gamma^{(x1)} .
$$

The pair of directions $(x1, x4)$ is mixed by a hyperbolic turn, which keeps $v_1^2 - v_4^2$ because $\cosh^2\theta - \sinh^2\theta = 1$, and never comes back.

**Reading off the vector matrix with traces.** For an even $R$ write $R\gamma^cR^{-1} = \sum_d\Lambda_{dc}\gamma^d$ (Section 5.12). Since $\mathrm{tr}(\gamma^d\gamma^e) = 16\,\eta^{de}$ (for $d \neq e$ by Rule 5 with $k = 2$; for $d = e$ it is the trace of $\eta_{dd}1$), multiplying by $\gamma^d$ and taking the trace leaves one term:

$$
\Lambda_{dc} = \eta_{dd}\,\mathrm{tr}\big(\gamma^dR\gamma^cR^{-1}\big)/16 .
$$

Notebook 05d computes vector matrices this way.

**The double cover.** Since $\Lambda(-g) = \Lambda(g)$ (the two signs cancel in $g\gamma^cg^{-1}$), every vector matrix belongs to at least two spinor matrices, $g$ and $-g$. There are no others. Proof: if $\Lambda(g) = \Lambda(h)$, then $k = gh^{-1}$ has $\Lambda(k) = \Lambda(g)\Lambda(h)^{-1} = 1$, that is $\alpha(k)\gamma^ck^{-1} = \gamma^c$ for every $c$. If $k$ is even, $k\gamma^c = \gamma^ck$: $k$ commutes with every gamma, so $k = \lambda1$ by Theorem P of Section 5.13; and by the spinor norm below, $k^TCk = \pm C$, so $\lambda^2 = \pm1$, and since $k$ is a real matrix, $\lambda = \pm1$. If $k$ were odd, $k\gamma^c = -\gamma^ck$ for every $c$; then $\Gamma k$ commutes with every gamma (moving $\gamma^c$ through $\Gamma k$ costs two signs), so $\Gamma k = \lambda1$ and $k = \lambda\Gamma$, an even matrix, which is impossible for an odd element (Section 5.12). So $h = \pm g$. Status: PROVED. That every matrix of O(4,4) is the vector matrix of some element of Pin(4,4) is the theorem of Cartan and Dieudonné (every such matrix is a product of reflections), which this book quotes without proof (ASSUMED). With it, Pin(4,4) is a **double cover** of O(4,4) and Spin(4,4) of SO(4,4).

**The forms that are kept.** Two bilinears matter: $\Psi^\dagger C\Psi$ (the scalar) and $\Psi^\dagger B\Psi$ (the charge density).

First, for every generator, $(S^{ab})^TC + CS^{ab} = 0$. Proof for $a \neq b$: by Rule 4, $(S^{ab})^T = \tfrac12\eta_{aa}\eta_{bb}\gamma^b\gamma^a = -\tfrac12\eta_{aa}\eta_{bb}\gamma^a\gamma^b$, and by (C1) used twice, $\gamma^a\gamma^bC = \eta_{aa}\eta_{bb}C\gamma^a\gamma^b$. So $(S^{ab})^TC = -\tfrac12(\eta_{aa}\eta_{bb})^2C\gamma^a\gamma^b = -CS^{ab}$. For $R = \exp(\theta S^{ab})$ the transpose is $\exp(\theta(S^{ab})^T)$ (transpose every power), and $(S^T)^kC = C(-S)^k$ (move $C$ to the left one factor at a time), so

$$
R^TC = C\exp(-\theta S^{ab}) = CR^{-1}, \qquad R^TCR = C .
$$

Products of exponentials keep it too: if $R_1^TCR_1 = C$ and $R_2^TCR_2 = C$, then $(R_1R_2)^TC(R_1R_2) = R_2^T(R_1^TCR_1)R_2 = C$. Since $R$ is real, $(R\Psi)^\dagger C(R\Psi) = \Psi^\dagger R^TCR\Psi = \Psi^\dagger C\Psi$: **the scalar $S$ is invariant** under every product of exponentials.

Second, $B = -iC\gamma^{(x4)}$. For a generator that does not involve $x4$ ($a, b \neq x4$), $(S^{ab})^\dagger B + BS^{ab} = 0$; for the seven generators $S^{(x4)b}$, $(S^{(x4)b})^\dagger B + BS^{(x4)b} = iC\gamma^b \neq 0$. Proof of the second statement (the first is similar): with $S = \tfrac12\gamma^{(x4)}\gamma^b$ ($S$ is real, so $S^\dagger = S^T$),

$$
BS = -\tfrac{i}2C\gamma^{(x4)}\gamma^{(x4)}\gamma^b = \tfrac{i}2C\gamma^b, \qquad S^TB = -\tfrac{i}2\eta_{bb}\gamma^{(x4)}\gamma^bC\gamma^{(x4)} = \tfrac{i}2C\gamma^{(x4)}\gamma^b\gamma^{(x4)} = \tfrac{i}2C\gamma^b ,
$$

where the first uses $\gamma^{(x4)}\gamma^{(x4)} = -1$; the second uses Rule 4 for $S^T$, then (C1) to move $C$ to the front (sign $-\eta_{bb}$ for $\gamma^b$, $+1$ for $\gamma^{(x4)}$), then $\gamma^b\gamma^{(x4)} = -\gamma^{(x4)}\gamma^b$ and $\gamma^{(x4)}\gamma^{(x4)} = -1$. The sum is $iC\gamma^b$. So the charge density $\Psi^\dagger B\Psi$ is kept only by the transformations that leave the time $x4$ alone. This is what one expects: the charge density is the time component of the current $J^a$, and a boost that mixes the time $x4$ with another direction mixes it with the other components, as the charge density of special relativity does.

**The spinor norm.** For $g = \gamma(u_1)\cdots\gamma(u_k)$ in Pin(4,4) put $N(g) = \eta(u_1, u_1)\cdots\eta(u_k, u_k) = \pm1$. Then

$$
g^TCg = (-1)^k\,N(g)\,C .
$$

Proof: from (C5), $(\gamma^a)^T = -C\gamma^aC$, so $(\gamma^a)^TC = -C\gamma^a$ and, by linearity, $\gamma(u)^TC = -C\gamma(u)$. Hence $\gamma(u)^TC\gamma(u) = -C\gamma(u)\gamma(u) = -\eta(u, u)\,C$. In $g^TCg = \gamma(u_k)^T\cdots\gamma(u_1)^T\,C\,\gamma(u_1)\cdots\gamma(u_k)$ apply this to the innermost pair, then to the next, and so on: each factor contributes $-\eta(u_j, u_j)$. Consequence: a product of exponentials has $g^TCg = +C$, but $g = \gamma^{(x1)}\gamma^{(x4)}$, an element of Spin(4,4) with $k = 2$ and $N = (+1)(-1) = -1$, has $g^TCg = -C$. **So Spin(4,4) contains elements that are not products of exponentials.** Section 5.23 finds all of them.

**Determinant 1.** Every gamma has determinant $+1$ as a $16 \times 16$ matrix (Section 5.3, Rule 6), and so has every product of gammas, every $\gamma(u)$ of a unit vector (its square is $\pm1$ and its trace 0) and every element of Pin(4,4). So the words determinant 1 in the author's statement about Spin(4,4) refer to the vector matrix $\Lambda$ in O(4,4), never to the spinor matrix itself.

| statement | status | where it is verified |
| --- | --- | --- |
| the so(4,4) rules for all 784 pairs of generators | PROVED | `python-algebra.json`, check `S_lorentz_algebra`; `wolfram-algebra.json`, check `S_Lorentz_algebra` |
| $(S^{ab})^TC + CS^{ab} = 0$ and $[\Gamma, S^{ab}] = 0$ | PROVED | `python-algebra.json`, check `S_preserves_C_and_commutes_with_Gamma`; `wolfram-algebra.json`, checks `S_preserves_C` and `S_commutes_with_Gamma` |
| $B$ kept exactly by the 21 generators without $x4$; $iC\gamma^b$ for $S^{(x4)b}$ | PROVED | `wolfram-algebra.json`, check `S_preserves_B_only_off_x4` |
| closed formulas, half angles, $R(2\pi) = -1$, the spinor norm, the double cover (kernel $\pm1$), determinants $+1$ | PROVED above; COMPUTED in Notebook 05d | Notebook 05d (its own computation, to $10^{-10}$ or better; the determinants exactly) |
| every matrix of O(4,4) is a vector matrix (Cartan and Dieudonné) | ASSUMED (quoted theorem) | not computed in this book |

### 5.19 Example: Notebook 05d computes spin transformations

Notebook 05d builds the 28 generators, repeats the recorded so(4,4) rules (784 pairs), the vector rule (512 triples) and the invariance of $C$, sorts the 28 planes into 12 rotations and 16 boosts, compares the power series of the exponential with the closed formulas, computes the vector matrices by the trace formula, shows the half angle and the sign $-1$ after a turn by $2\pi$, follows a unit vector around a circle and along hyperbolas, measures which transformations keep the forms of $C$ and $B$, and checks the reflections, the spinor norm, the double cover and the determinants. It draws six figures and ends with ALL 20 CHECKS PASSED (notebook 05d).

<!-- NOTEBOOK 05d -->

### 5.22 Line-by-line walk-through of Notebook 05d

The notebook has 17 code cells. In [1] is the set-up cell of Section 5.10 with `NOTEBOOK_ID = "05d"`; its comments repeat the instructions of Section 5.20.

**In [2], the gammas, C, Γ, B and the recorded checks.**

```python
import contextlib  # lets a block of code print into a text buffer
import io  # the text buffer io.StringIO
import sys  # sys.stdout: the channel through which the notebook prints

import numpy as np  # arrays of numbers, matrices and linear algebra

fixture = json.loads(repository_file("Revision/algebra/gammas.json")
                     .read_text(encoding="utf-8"))
COORDS = fixture["coordinates"]  # "x1", ..., "x8"
ETA = dict(zip(COORDS, fixture["eta"]))  # +1 space-like, -1 time-like
ETA_MATRIX = np.diag([float(ETA[x]) for x in COORDS])  # the 8 x 8 metric eta
gamma = {x: np.array(m, dtype=np.int64) for x, m in zip(COORDS, fixture["gamma"])}
I16 = np.eye(16, dtype=np.int64)
```

As in Notebook 05a, the record of the gammas is read. New is `ETA_MATRIX`, the $8 \times 8$ diagonal matrix $\eta$ with floating-point entries (`np.diag` of the list of the eight signs), used for the metric product of vectors below.

```python
C = gamma["x8"] @ gamma["x1"] @ gamma["x2"] @ gamma["x3"]  # the charge matrix
Gamma = I16
for x in ["x8", "x1", "x2", "x3", "x4", "x5", "x6", "x7"]:
    Gamma = Gamma @ gamma[x]  # the chirality, the product of all eight gammas
B = -1j * (C @ gamma["x4"])  # B = -i C gamma^(x4)
```

$C$, $\Gamma$ and $B$ are built as in Sections 5.4 to 5.6; the loop multiplies the eight gammas in the author's order, starting from the identity.

```python
REPORT_FILES = {"python": "Revision/algebra/reports/python-algebra.json",
                "wolfram": "Revision/algebra/reports/wolfram-algebra.json"}
VERDICTS = {}  # (report key, check name) -> (verdict in lower case, detail text)
for key, path in REPORT_FILES.items():
    report_data = json.loads(repository_file(path).read_text(encoding="utf-8"))
    for entry in report_data["checks"]:
        VERDICTS[(key, entry["name"])] = (entry["verdict"].lower(), entry["detail"])


def recorded(key, name):
    return VERDICTS[(key, name)][0] == "pass"


def record_of(key, name):
    return f"{REPORT_FILES[key]}, check {name}"


def check_reproduces(condition, name, record):
    collected = io.StringIO()
    with contextlib.redirect_stdout(collected):  # print into the buffer
        check(condition, name, record=record)  # stops here if the check fails
    sys.stdout.write(collected.getvalue())  # the PASS and reproduces lines together
```

The two reports and the helpers `recorded`, `record_of` and `check_reproduces`, exactly as in Notebook 05a (Section 5.10, In [3]).

```python
def eta(a, b):
    return ETA[a] if a == b else 0


check_reproduces(all(np.array_equal(gamma[a] @ gamma[b] + gamma[b] @ gamma[a],
                                    2 * eta(a, b) * I16) for a in COORDS for b in COORDS)
                 and recorded("python", "clifford_relation"),
                 "{gamma^a, gamma^b} = 2 eta^ab 1 for all 64 pairs",
                 record=record_of("python", "clifford_relation"))
```

`eta(a, b)` is $\eta^{ab}$: $\eta_{aa}$ for equal directions and 0 otherwise. The check is the Clifford relation for all 64 pairs.

**In [3], the generators and their rules.**

```python
S = {(a, b): (gamma[a] @ gamma[b] - gamma[b] @ gamma[a]) / 4.0
     for a in COORDS for b in COORDS}  # all 64 ordered pairs
pairs = [(a, b) for i, a in enumerate(COORDS) for b in COORDS[i + 1:]]  # 28 pairs


def commutator(m, n):
    return m @ n - n @ m
```

`S` holds $S^{ab}$ for all 64 ordered pairs (including $S^{aa} = 0$), as floating-point arrays with the entries $0$ and $\pm\tfrac12$. Every sum and product below involves only halves and quarters, which the computer stores exactly (they are sums of powers of 2), so comparisons with `np.array_equal` are exact. `pairs` lists the 28 planes, and `commutator` is $[m, n] = mn - nm$.

```python
definition_ok = all(np.array_equal(S[(a, b)], -S[(b, a)]) for a in COORDS
                    for b in COORDS) and all(
    np.array_equal(S[(a, b)], gamma[a] @ gamma[b] / 2.0) for a, b in pairs)
check_reproduces(len(pairs) == 28 and definition_ok
                 and recorded("python", "S_definition"),
                 "S^ab = -S^ba and S^ab = (1/2) gamma^a gamma^b: 28 independent "
                 "generators",
                 record=record_of("python", "S_definition"))
```

The check confirms $S^{ab} = -S^{ba}$ for all 64 pairs and $S^{ab} = \tfrac12\gamma^a\gamma^b$ for the 28 planes.

```python
algebra_failures = 0
for a, b in pairs:
    for c, d in pairs:
        right = (eta(b, c) * S[(a, d)] - eta(a, c) * S[(b, d)]
                 - eta(b, d) * S[(a, c)] + eta(a, d) * S[(b, c)])
        if not np.array_equal(commutator(S[(a, b)], S[(c, d)]), right):
            algebra_failures += 1
say(f"so(4,4) rules tested for {len(pairs) ** 2} pairs; failures {algebra_failures}")
check_reproduces(algebra_failures == 0 and recorded("python", "S_lorentz_algebra")
                 and recorded("wolfram", "S_Lorentz_algebra"),
                 "[S^ab, S^cd] = eta^bc S^ad - eta^ac S^bd - eta^bd S^ac + eta^ad S^bc",
                 record=record_of("python", "S_lorentz_algebra"))
```

For each of the $28 \times 28 = 784$ pairs of planes the right side of the so(4,4) rule is assembled and compared with the commutator; failures are counted. The printed line reports 784 pairs and 0 failures.

```python
vector_failures = sum(
    not np.array_equal(commutator(S[(a, b)], gamma[c]),
                       eta(b, c) * gamma[a] - eta(a, c) * gamma[b])
    for a in COORDS for b in COORDS for c in COORDS)
say(f"vector rule tested for 512 triples; failures {vector_failures}")
check_reproduces(vector_failures == 0 and recorded("python", "S_vector_action")
                 and recorded("wolfram", "S_gamma_commutator"),
                 "[S^ab, gamma^c] = eta^bc gamma^a - eta^ac gamma^b for all 512 triples",
                 record=record_of("python", "S_vector_action"))
```

The vector rule of Section 5.12 is tested for all $8 \times 8 \times 8 = 512$ triples; `sum` of true and false values counts the true ones (a failure counts 1). The printed line reports 0 failures.

**In [4], the invariances of the generators.**

```python
check_reproduces(all(not ((S[k].T @ C + C @ S[k]).any()) for k in S)
                 and all(not commutator(Gamma, S[k]).any() for k in S)
                 and recorded("python", "S_preserves_C_and_commutes_with_Gamma"),
                 "(S^ab)^T C + C S^ab = 0 and [Gamma, S^ab] = 0 for all a, b",
                 record=record_of("python", "S_preserves_C_and_commutes_with_Gamma"))
```

For all 64 keys `k` of `S` the cell checks $(S^{ab})^TC + CS^{ab} = 0$ (so the scalar does not change to first order) and $[\Gamma, S^{ab}] = 0$ (so the halves are kept).

**In [5], rotations and boosts.**

```python
kind = {}  # (a, b) -> +1 for a rotation, -1 for a boost
squares_ok = True
for a, b in pairs:
    J = gamma[a] @ gamma[b]
    squares_ok &= np.array_equal(J @ J, -ETA[a] * ETA[b] * I16)
    kind[(a, b)] = ETA[a] * ETA[b]
rotations = [p for p in pairs if kind[p] == 1]
boosts = [p for p in pairs if kind[p] == -1]
say(f"rotations: {len(rotations)}; boosts: {len(boosts)}")
say("rotation planes: " + " ".join(f"({a},{b})" for a, b in rotations))
check(squares_ok and len(rotations) == 12 and len(boosts) == 16,
      "(gamma^a gamma^b)^2 = -eta_aa eta_bb: 12 rotation planes and 16 boost planes")
```

For each plane $J = \gamma^a\gamma^b$ is squared and compared with $-\eta_{aa}\eta_{bb}1$; the plane is a rotation when $\eta_{aa}\eta_{bb} = +1$ and a boost otherwise. The printed lines show 12 rotations and 16 boosts and list the rotation planes: the six inside $\{x1, x2, x3, x8\}$ and the six inside $\{x4, x5, x6, x7\}$.

```python
from matplotlib.colors import LinearSegmentedColormap

SIGNS = LinearSegmentedColormap.from_list("signs", ["#2a78d6", "#f0efec", "#e34948"])
table = np.zeros((8, 8))
for (a, b), value in kind.items():
    i, j = COORDS.index(a), COORDS.index(b)
    table[i, j] = table[j, i] = value  # the same plane in both orders
fig, ax = plt.subplots(figsize=(6.4, 5.6))
ax.imshow(table, cmap=SIGNS, vmin=-1, vmax=1)
for i in range(8):
    for j in range(8):
        word = "" if i == j else ("rot" if table[i, j] == 1 else "boost")
        ax.text(j, i, word, ha="center", va="center", color="white", fontsize=8,
                fontweight="bold")
for k in range(1, 8):
    ax.axhline(k - 0.5, color="white", linewidth=2)
    ax.axvline(k - 0.5, color="white", linewidth=2)
ax.set_xticks(range(8), COORDS)
ax.set_yticks(range(8), COORDS)
ax.set_title("The 28 planes: rotations (red) and boosts (blue)")
ax.grid(False)
save_figure(fig, "plane_types", ...)
```

The kinds are written into an $8 \times 8$ table, each plane in both orders (`COORDS.index(a)` is the position of a name in the list; `x = y = value` sets both entries). The table is drawn with the colour map of the heat maps (red $+1$, blue $-1$, grey 0 on the diagonal), with the word rot or boost in each square and white gaps between the squares. `05d_1_plane_types.png` shows two red $4 \times 4$ squares of rotations, for $\{x1, x2, x3, x8\}$ and for the four times, and blue boosts wherever a space-like direction meets a time-like one.

**In [6], the exponential two ways.**

```python
def exp_series(M, terms=80):
    result = np.eye(M.shape[0])
    term = np.eye(M.shape[0])
    for k in range(1, terms):
        term = term @ M / k  # M^k / k! from M^(k-1) / (k-1)!
        result = result + term
    return result
```

`exp_series` sums the power series of the exponential up to the term $M^{79}/79!$. Each term is computed from the previous one by multiplying by $M$ and dividing by $k$, because $M^k/k! = (M^{k-1}/(k-1)!)\,M/k$.

```python
def spin_transformation(a, b, theta):
    J = (gamma[a] @ gamma[b]).astype(float)  # J = 2 S^ab
    if ETA[a] * ETA[b] == 1:  # J J = -1: a rotation
        return np.cos(theta / 2) * np.eye(16) + np.sin(theta / 2) * J
    return np.cosh(theta / 2) * np.eye(16) + np.sinh(theta / 2) * J  # a boost
```

`spin_transformation(a, b, theta)` is the closed formula of Section 5.18: $\cos\tfrac\theta2\,1 + \sin\tfrac\theta2\,J$ for a rotation and $\cosh\tfrac\theta2\,1 + \sinh\tfrac\theta2\,J$ for a boost.

```python
tests = [(("x1", "x2"), [0.3, 1.0, 2.5, 2 * np.pi, 4 * np.pi]),
         (("x4", "x5"), [0.3, 1.0, 2.5, 2 * np.pi, 4 * np.pi]),
         (("x1", "x4"), [-1.5, 0.3, 1.0, 2.5]),
         (("x5", "x8"), [-1.5, 0.3, 1.0, 2.5])]
largest_difference = 0.0
for (a, b), angles in tests:
    for theta in angles:
        difference = np.max(np.abs(exp_series(theta * S[(a, b)])
                                   - spin_transformation(a, b, theta)))
        largest_difference = max(largest_difference, difference)
    name = "rotation" if kind[(a, b)] == 1 else "boost"
    say(f"plane ({a},{b}), a {name}: series and closed formula compared at "
        f"{len(angles)} values")
check(largest_difference < 1e-10,
      "the power series of exp(theta S^ab) equals the closed formula with half "
      "angles (difference below 1e-10)")
```

Two rotations (one of them in the plane of two times) and two boosts are tested at several angles or rapidities; for each, the largest difference of any entry between the series and the closed formula is kept in `largest_difference`. Four lines are printed, and the check requires the largest difference to be below $10^{-10}$ (the series is summed in floating-point numbers, and at $4\pi$ its terms first grow large before they shrink).

**In [7], the vector matrix and the sign after $2\pi$.**

```python
def vector_matrix(R):
    R_inverse = np.linalg.inv(R)
    Lam = np.zeros((8, 8))
    for j, c in enumerate(COORDS):
        moved = R @ gamma[c] @ R_inverse  # where the direction c is moved to
        for i, d in enumerate(COORDS):
            Lam[i, j] = ETA[d] * np.trace(gamma[d] @ moved) / 16.0
    return Lam
```

`vector_matrix(R)` computes $\Lambda$ by the trace formula of Section 5.18: for each direction $c$ it forms $R\gamma^cR^{-1}$ (`np.linalg.inv` is the inverse matrix) and fills column $c$ with $\eta_{dd}\,\mathrm{tr}(\gamma^dR\gamma^cR^{-1})/16$ for each row $d$.

```python
def rebuilds(R, Lam):
    R_inverse = np.linalg.inv(R)
    return all(np.allclose(sum(Lam[i, j] * gamma[d] for i, d in enumerate(COORDS)),
                           R @ gamma[c] @ R_inverse, atol=1e-12)
               for j, c in enumerate(COORDS))
```

`rebuilds` checks that $\sum_d\Lambda_{dc}\gamma^d$ really equals $R\gamma^cR^{-1}$ for every $c$, that is, that the moved gamma is a combination of gammas with the coefficients read off. `np.allclose(x, y, atol=1e-12)` is true when every entry of `x` differs from that of `y` by at most about $10^{-12}$.

```python
rotation_ok = True
for theta in np.linspace(0.0, 2 * np.pi, 9):
    R = spin_transformation("x1", "x2", theta)
    Lam = vector_matrix(R)
    expected = np.eye(8)  # the rotation by theta in the (x1, x2) block
    expected[0, 0] = expected[1, 1] = np.cos(theta)
    expected[0, 1], expected[1, 0] = np.sin(theta), -np.sin(theta)
    rotation_ok &= (rebuilds(R, Lam) and np.allclose(Lam, expected, atol=1e-12)
                    and np.allclose(Lam.T @ ETA_MATRIX @ Lam, ETA_MATRIX)
                    and abs(np.linalg.det(Lam) - 1.0) < 1e-12)
check(rotation_ok,
      "R = exp(theta S^(x1 x2)) turns the directions x1, x2 by the full angle "
      "theta; Lambda lies in SO(4,4)")
```

For nine angles from 0 to $2\pi$ the cell computes the rotation in the plane $(x1, x2)$ and its vector matrix, and compares it with the prediction of Section 5.18: the identity except for the block of $x1$ and $x2$, which holds $\cos\theta$ on the diagonal, $\sin\theta$ in row $x1$, column $x2$, and $-\sin\theta$ in row $x2$, column $x1$. It also checks $\Lambda^T\eta\Lambda = \eta$ and $\det\Lambda = 1$ (`np.linalg.det`): $\Lambda$ lies in SO(4,4).

```python
R_2pi, R_4pi = spin_transformation("x1", "x2", 2 * np.pi), spin_transformation(
    "x1", "x2", 4 * np.pi)
# Rounding leaves differences of about 1e-16, which differ between computers, so
# the cell prints only whether they are below 1e-12.
small_2pi = np.max(np.abs(R_2pi + np.eye(16))) < 1e-12
small_4pi = np.max(np.abs(R_4pi - np.eye(16))) < 1e-12
say(f"every entry of R(2 pi) + 1 is below 1e-12: {small_2pi}; "
    f"every entry of R(4 pi) - 1 is below 1e-12: {small_4pi}")
check(np.allclose(R_2pi, -np.eye(16), atol=1e-12)
      and np.allclose(R_4pi, np.eye(16), atol=1e-12)
      and np.allclose(vector_matrix(R_2pi), np.eye(8), atol=1e-12),
      "a rotation by 2 pi gives R = -1 on spinors but Lambda = 1 on vectors; by 4 pi, R "
      "= +1")
```

$R(2\pi)$ and $R(4\pi)$ are computed; $\sin\pi$ is not exactly 0 in floating-point numbers, so the cell prints only whether the entries of $R(2\pi) + 1$ and $R(4\pi) - 1$ are below $10^{-12}$ (both True). The check is the double cover: $R(2\pi) = -1$ while its vector matrix is the identity, and $R(4\pi) = +1$.

**In [8], the picture of the half angles.**

```python
angles = np.linspace(0.0, 4 * np.pi, 241)
rapidities = np.linspace(-3.0, 3.0, 241)
vec_rot = [vector_matrix(spin_transformation("x1", "x2", th))[0, 0] for th in angles]
spin_rot = [np.trace(spin_transformation("x1", "x2", th)) / 16 for th in angles]
vec_boost = [vector_matrix(spin_transformation("x1", "x4", th))[0, 0]
             for th in rapidities]
spin_boost = [np.trace(spin_transformation("x1", "x4", th)) / 16 for th in rapidities]
check(np.allclose(vec_rot, np.cos(angles)) and np.allclose(spin_rot, np.cos(angles / 2))
      and np.allclose(vec_boost, np.cosh(rapidities))
      and np.allclose(spin_boost, np.cosh(rapidities / 2)),
      "vectors move with cos(theta), cosh(theta); spinors with the half angle")
```

For 241 angles from 0 to $4\pi$ (rotation in $(x1, x2)$) and 241 rapidities from $-3$ to $3$ (boost in $(x1, x4)$), the cell computes the vector entry $\Lambda_{x1,x1}$ and the spinor quantity $\mathrm{tr}\,R/16$; since $\mathrm{tr}\,J = 0$ (Rule 5), $\mathrm{tr}\,R/16$ is $\cos\tfrac\theta2$ or $\cosh\tfrac\theta2$. The check compares the four lists with $\cos\theta$, $\cos\tfrac\theta2$, $\cosh\theta$ and $\cosh\tfrac\theta2$.

```python
fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.4))
axes[0].plot(angles, vec_rot, color="#2a78d6", linewidth=2,
             label=r"vector: $\Lambda_{x1,x1} = \cos\theta$")
axes[0].plot(angles, spin_rot, color="#eb6834", linewidth=2, linestyle="--",
             label=r"spinor: $\mathrm{tr}\,R/16 = \cos(\theta/2)$")
axes[0].plot([2 * np.pi, 2 * np.pi], [1.0, -1.0], "o", color="black", markersize=7,
             label=r"at $2\pi$: vector back at $1$, spinor at $-1$")
axes[0].set_xticks([0, np.pi, 2 * np.pi, 3 * np.pi, 4 * np.pi],
                   ["0", r"$\pi$", r"$2\pi$", r"$3\pi$", r"$4\pi$"])
axes[0].set_xlabel(r"rotation angle $\theta$ in the plane $(x1, x2)$")
axes[0].set_ylabel("value")
axes[0].set_title("A rotation: the spinor needs $4\\pi$ to come back")
axes[0].legend(loc="upper center", bbox_to_anchor=(0.5, -0.17))
axes[1].plot(rapidities, vec_boost, color="#2a78d6", linewidth=2,
             label=r"vector: $\Lambda_{x1,x1} = \cosh\theta$")
axes[1].plot(rapidities, spin_boost, color="#eb6834", linewidth=2, linestyle="--",
             label=r"spinor: $\mathrm{tr}\,R/16 = \cosh(\theta/2)$")
axes[1].set_xlabel(r"rapidity $\theta$ in the plane $(x1, x4)$")
axes[1].set_title("A boost: never periodic;\nthe spinor grows half as fast")
axes[1].legend(loc="upper center", bbox_to_anchor=(0.5, -0.17))
save_figure(fig, "half_angles", ...)
```

Two pictures: on the left the two rotation curves and two black dots at $\theta = 2\pi$ (the vector entry at 1, the spinor quantity at $-1$); on the right the two boost curves. The tick marks of the left horizontal axis are at multiples of $\pi$; `"\n"` in a title starts a new line; both legends go below their pictures. In `05d_2_half_angles.png` the solid cosine completes two periods over $4\pi$ while the dashed one completes one: the spinor needs $4\pi$ to come back.

**In [9], the rotation matrices.**

```python
fig, axes = plt.subplots(1, 4, figsize=(13.0, 3.9))
for k, (ax, th, label) in enumerate(zip(
        axes, [0.0, np.pi, 2 * np.pi, 4 * np.pi], ["0", r"\pi", r"2\pi", r"4\pi"])):
    image = ax.imshow(spin_transformation("x1", "x2", th), cmap=SIGNS, vmin=-1,
                      vmax=1)
    ax.set_title(rf"$R(\theta)$ at $\theta = {label}$")
    ax.set_xticks([0, 7, 15], ["1", "8", "16"])
    ax.set_yticks([0, 7, 15], ["1", "8", "16"])
    ax.set_xlabel("column")
    if k == 0:
        ax.set_ylabel("row")
    ax.grid(False)
fig.colorbar(image, ax=axes, ticks=[-1, 0, 1], shrink=0.8, label="matrix entry")
check(np.allclose(spin_transformation("x1", "x2", np.pi),
                  gamma["x1"] @ gamma["x2"], atol=1e-12),
      "R(pi) = gamma^(x1) gamma^(x2) for the rotation in the plane (x1, x2)")
save_figure(fig, "rotation_matrices", ...)
```

The loop draws $R(\theta)$ at $\theta = 0$, $\pi$, $2\pi$ and $4\pi$ as heat maps (the `zip` runs through the four axes, the four angles and their labels together). The check confirms $R(\pi) = \gamma^{(x1)}\gamma^{(x2)}$ (because $\cos\tfrac\pi2 = 0$ and $\sin\tfrac\pi2 = 1$). In `05d_3_rotation_matrices.png` the first picture is the identity (red diagonal), the second the signed permutation $\gamma^{(x1)}\gamma^{(x2)}$, the third minus the identity (blue diagonal) and the fourth the identity again.

**In [10], circles and hyperbolas.**

```python
circle = np.array([vector_matrix(spin_transformation("x1", "x2", th))[:, 0]
                   for th in np.linspace(0.0, 2 * np.pi, 121)])  # images of e_x1
hyper_space = np.array([vector_matrix(spin_transformation("x1", "x4", th))[:, 0]
                        for th in np.linspace(-2.0, 2.0, 121)])  # images of e_x1
hyper_time = np.array([vector_matrix(spin_transformation("x1", "x4", th))[:, 3]
                       for th in np.linspace(-2.0, 2.0, 121)])  # images of e_x4
check(np.allclose(circle[:, 0] ** 2 + circle[:, 1] ** 2, 1.0)
      and np.allclose(hyper_space[:, 0] ** 2 - hyper_space[:, 3] ** 2, 1.0)
      and np.allclose(hyper_time[:, 0] ** 2 - hyper_time[:, 3] ** 2, -1.0),
      "rotations keep v1^2 + v2^2, boosts keep v1^2 - v4^2")
```

Column $c$ of a vector matrix (`[:, 0]` is the first column, `[:, 3]` the fourth) is the image of the basic unit vector $e_c$. The cell collects the images of $e_{x1}$ under 121 rotations in $(x1, x2)$, and the images of $e_{x1}$ and of $e_{x4}$ under 121 boosts in $(x1, x4)$. The check confirms that the rotation keeps $v_1^2 + v_2^2 = 1$ and the boost keeps $v_1^2 - v_4^2$, equal to $+1$ for the image of $e_{x1}$ and $-1$ for that of $e_{x4}$.

```python
fig, axes = plt.subplots(1, 2, figsize=(11.0, 5.0))
axes[0].plot(circle[:, 0], circle[:, 1], color="#2a78d6", linewidth=2)
axes[0].plot(circle[::15, 0], circle[::15, 1], "o", color="#2a78d6", markersize=8)
axes[0].set_aspect("equal")
axes[0].set_xlabel("$v_1$ (component along $x1$)")
axes[0].set_ylabel("$v_2$ (component along $x2$)")
axes[0].set_title("rotation in $(x1, x2)$: a circle")
axes[1].plot(hyper_space[:, 0], hyper_space[:, 3], color="#2a78d6", linewidth=2,
             label=r"image of $e_{x1}$: $v_1^2 - v_4^2 = 1$")
axes[1].plot(hyper_time[:, 0], hyper_time[:, 3], color="#eb6834", linewidth=2,
             label=r"image of $e_{x4}$: $v_1^2 - v_4^2 = -1$")
axes[1].plot([-4, 4], [-4, 4], ":", color="black", linewidth=1,
             label="null lines $v_4 = \\pm v_1$")
axes[1].plot([-4, 4], [4, -4], ":", color="black", linewidth=1)
axes[1].set_xlim(-4, 4)
axes[1].set_ylim(-4, 4)
axes[1].set_aspect("equal")
axes[1].set_xlabel("$v_1$ (component along $x1$)")
axes[1].set_ylabel("$v_4$ (component along the time $x4$)")
axes[1].set_title("boost in $(x1, x4)$: hyperbolas")
axes[1].legend(loc="upper center", bbox_to_anchor=(0.5, -0.14))
save_figure(fig, "orbits", ...)
```

The left picture draws the circle and a dot every 15 steps (`[::15]` takes every fifteenth row, that is every $\pi/4$); `set_aspect("equal")` gives both axes the same scale, so that a circle looks round. The right picture draws the two hyperbola branches and the two dotted **null lines** $v_4 = \pm v_1$, on which $v_1^2 - v_4^2 = 0$. In `05d_4_orbits.png` neither hyperbola crosses the null lines: a boost never turns a space-like vector into a time-like one.

**In [11], which generators keep the form of B.**

```python
keep_B = [p for p in pairs if not (S[p].T @ B + B @ S[p]).any()]
break_B = [p for p in pairs if p not in keep_B]
rule_x4 = all(np.array_equal(S[("x4", b)].T @ B + B @ S[("x4", b)],
                             1j * (C @ gamma[b])) for b in COORDS if b != "x4")
say(f"generators with S^T B + B S = 0: {len(keep_B)}; the others: "
    + " ".join(f"({a},{b})" for a, b in break_B))
check_reproduces(len(keep_B) == 21 and all("x4" in p for p in break_B) and rule_x4
                 and recorded("wolfram", "S_preserves_B_only_off_x4"),
                 "S^dagger B + B S = 0 exactly for the 21 generators without x4; for "
                 "S^(x4 b) it equals i C gamma^b",
                 record=record_of("wolfram", "S_preserves_B_only_off_x4"))
```

`keep_B` lists the planes whose generator obeys $S^TB + BS = 0$ ($S$ is real, so $S^T = S^\dagger$); `break_B` the others. `rule_x4` checks the formula $iC\gamma^b$ of Section 5.18 for the seven generators $S^{(x4)b}$. The printed line shows 21 planes that keep $B$ and the seven planes with $x4$. (`"x4" in p` is true when the pair `p` contains the name `x4`.)

```python
finite_C = max(np.max(np.abs(spin_transformation(a, b, 0.7).T @ C
                             @ spin_transformation(a, b, 0.7) - C)) for a, b in pairs)
finite_B = {p: np.max(np.abs(spin_transformation(*p, 0.7).T @ B
                             @ spin_transformation(*p, 0.7) - B)) for p in pairs}
check(finite_C < 1e-12 and all((finite_B[p] < 1e-12) == (p in keep_B) for p in pairs),
      "at theta = 0.7: R^T C R = C for all 28 planes; R^T B R = B exactly for the 21 "
      "planes without x4")
```

For finite transformations at $\theta = 0.7$ the cell computes the largest entry of $R^TCR - C$ over all 28 planes and of $R^TBR - B$ for each plane (`spin_transformation(*p, 0.7)` unpacks the pair `p` into the two arguments `a` and `b`). The check: the form of $C$ is kept for all planes, that of $B$ exactly for the 21 planes without $x4$.

**In [12], the picture of the forms.**

```python
thetas = np.linspace(-3.0, 3.0, 241)
planes = [("x1", "x2"), ("x5", "x6"), ("x1", "x4"), ("x4", "x5")]
colors = ["#2a78d6", "#1baf7a", "#eb6834", "#4a3aa7"]
lines = ["-", "--", "-", "-."]
change_B = {p: [np.max(np.abs(spin_transformation(*p, th).T @ B
                              @ spin_transformation(*p, th) - B)) for th in thetas]
            for p in planes}
change_C = max(np.max(np.abs(spin_transformation(*p, th).T @ C
                             @ spin_transformation(*p, th) - C))
               for p in planes for th in thetas)
shown = "below 1e-12" if change_C < 1e-12 else f"{change_C:.2e}"
say(f"largest change of the form of C over the four planes and all angles: {shown}")
```

For four planes (two rotations without $x4$, a boost and a rotation with $x4$) and 241 values of $\theta$ the cell computes how much the form of $B$ changes; for the form of $C$ only the largest change over everything is kept and printed (below $10^{-12}$; the cell prints the words instead of a number because the last digits of rounding differ between computers).

```python
fig, ax = plt.subplots(figsize=(8.0, 4.4))
for p, color, line in zip(planes, colors, lines):
    name = "rotation" if kind[p] == 1 else "boost"
    ax.plot(thetas, change_B[p], color=color, linestyle=line, linewidth=2,
            label=f"form of $B$, {name} in $({p[0]}, {p[1]})$")
ax.plot(thetas, np.zeros_like(thetas), ":", color="black", linewidth=2,
        label="form of $C$, all four planes")
ax.set_xlabel(r"angle or rapidity $\theta$")
ax.set_ylabel("largest entry of the change")
ax.set_title(r"$R^T C R - C$ is always 0; $R^T B R - B$ only away from $x4$")
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=2)
save_figure(fig, "invariant_forms", ...)
```

One curve per plane for the form of $B$, and a dotted line at zero for the form of $C$. In `05d_5_invariant_forms.png` the two rotations without $x4$ lie on the horizontal axis (no change), while the boost in $(x1, x4)$ and the rotation in $(x4, x5)$ rise away from $\theta = 0$.

**In [13], reflections.**

```python
def gamma_of(v):
    return sum(v[i] * gamma[x].astype(float) for i, x in enumerate(COORDS))


def metric_product(u, v):
    return float(u @ ETA_MATRIX @ v)


def reflection(u):
    return np.eye(8) - 2.0 * np.outer(u, u @ ETA_MATRIX) / metric_product(u, u)
```

`gamma_of(v)` is $\gamma(v) = \sum_a v_a\gamma^a$; `metric_product(u, v)` is $\eta(u, v) = u^T\eta v$; `reflection(u)` is the $8 \times 8$ matrix of $R_u$: since $R_uv = v - 2u\,(u^T\eta v)/\eta(u, u)$, its matrix is $1 - 2\,u\,(\eta u)^T/\eta(u, u)$, and `np.outer(u, u @ ETA_MATRIX)` is the column $u$ times the row $u^T\eta$.

```python
e = np.eye(8)  # e[i] is the unit vector along COORDS[i]
tilted = np.cosh(0.5) * e[0] + np.sinh(0.5) * e[3]
v = np.arange(1, 9) / 10.0
reflections_ok = True
for u in (e[0], e[3], tilted):
    gu = gamma_of(u)
    left = -gu @ gamma_of(v) @ np.linalg.inv(gu)
    Ru = reflection(u)
    reflections_ok &= (np.allclose(left, gamma_of(Ru @ v), atol=1e-12)
                       and abs(np.linalg.det(Ru) + 1.0) < 1e-12
                       and np.allclose(Ru.T @ ETA_MATRIX @ Ru, ETA_MATRIX))
    say(f"eta(u, u) = {metric_product(u, u):+.6f}: reflection checked")
check(reflections_ok,
      "-gamma(u) gamma(v) gamma(u)^-1 = gamma(R_u v); det R_u = -1; R_u keeps eta")
```

Three unit vectors are tested: $e_{x1}$ (space-like), $e_{x4}$ (time-like) and the tilted $\cosh(0.5)\,e_{x1} + \sinh(0.5)\,e_{x4}$ (with $\eta = \cosh^2 - \sinh^2 = 1$), each with the fixed vector $v = (0.1, 0.2, \dots, 0.8)$. For each, the key identity of Section 5.12, $\det R_u = -1$ and $R_u^T\eta R_u = \eta$ are checked, and $\eta(u, u)$ is printed: $+1$, $-1$, $+1$.

**In [14], the spinor norm, $\Lambda(\Gamma)$ and the double cover.**

```python
elements = [("gamma^(x1)", [e[0]]), ("gamma^(x4)", [e[3]]),
            ("gamma^(x1) gamma^(x4)", [e[0], e[3]]),
            ("gamma(tilted) gamma^(x5)", [tilted, e[4]]),
            ("Gamma", [e[7]] + [e[i] for i in range(7)])]
norm_ok = True
for name, factors in elements:
    g = np.eye(16)
    for u in factors:
        g = g @ gamma_of(u)
    k = len(factors)
    N = int(round(np.prod([metric_product(u, u) for u in factors])))
    predicted = (-1) ** k * N
    norm_ok &= np.allclose(g.T @ C @ g, predicted * C, atol=1e-12)
    say(f"{name:26} k = {k}, N(g) = {N:+d}: g^T C g = {predicted:+d} C")
check(norm_ok, "g^T C g = (-1)^k N(g) C for all five elements")
```

Five elements of Pin(4,4) are given by their unit-vector factors (for $\Gamma$: $e_{x8}$ followed by $e_{x1}, \dots, e_{x7}$). For each, the product $g$, the number of factors $k$ and the spinor norm $N(g)$ (the product of the $\eta(u, u)$, rounded to a whole number) are computed, and $g^TCg$ is compared with $(-1)^kN(g)\,C$. The printed table shows in particular $g^TCg = -C$ for $\gamma^{(x1)}\gamma^{(x4)}$ and for $\gamma(\text{tilted})\gamma^{(x5)}$: two even elements that are not products of exponentials.

```python
check(np.allclose(vector_matrix(Gamma.astype(float)), -np.eye(8), atol=1e-12),
      "Gamma moves every direction to its opposite: Lambda(Gamma) = -1 (det +1)")
cover_ok = all(
    np.allclose(spin_transformation("x1", "x2", th + 2 * np.pi),
                -spin_transformation("x1", "x2", th), atol=1e-12)
    and np.allclose(vector_matrix(spin_transformation("x1", "x2", th + 2 * np.pi)),
                    vector_matrix(spin_transformation("x1", "x2", th)), atol=1e-12)
    for th in np.linspace(0.0, 2 * np.pi, 7))
check(cover_ok, "R(theta + 2 pi) = -R(theta), and both move the vectors in the "
      "same way: two spinor matrices for every vector matrix")
```

$\Gamma$ is even, and its vector matrix is $-1_8$: by (X2), $\Gamma\gamma^c\Gamma^{-1} = -\gamma^c$. Then, for seven angles, $R(\theta + 2\pi) = -R(\theta)$ and the two have the same vector matrix.

**In [15], the determinants of the gammas.**

```python
import sympy as sp  # exact algebra

determinants = {x: sp.Matrix(gamma[x].tolist()).det() for x in COORDS}
say("det gamma^(x) = " + ", ".join(f"{x}: {determinants[x]}" for x in COORDS))
check(all(d == 1 for d in determinants.values()),
      "every gamma matrix has determinant +1 as a 16 x 16 matrix")
```

sympy computes the eight determinants exactly. The printed line shows 1 for every direction, as Rule 6 predicts.

**In [16], four vector matrices as pictures.**

```python
pictures = [(vector_matrix(spin_transformation("x1", "x2", np.pi / 3)),
             r"rotation, $\theta = \pi/3$, $(x1, x2)$"),
            (vector_matrix(spin_transformation("x1", "x4", 1.0)),
             r"boost, $\theta = 1$, $(x1, x4)$"),
            (reflection(e[0]), r"reflection $R_u$, $u = e_{x1}$"),
            (vector_matrix(Gamma.astype(float)), r"$\Lambda(\Gamma) = -1_8$")]
fig, axes = plt.subplots(1, 4, figsize=(14.0, 4.0))
for k, (ax, (matrix, title)) in enumerate(zip(axes, pictures)):
    image = ax.imshow(matrix, cmap=SIGNS, vmin=-1.6, vmax=1.6)
    for i in range(8):
        for j in range(8):
            if abs(matrix[i, j]) > 1e-12:  # write the nonzero entries
                ax.text(j, i, f"{matrix[i, j]:.2f}", ha="center", va="center",
                        fontsize=6)
    ax.set_xticks(range(8), COORDS, fontsize=7)
    ax.set_yticks(range(8), COORDS, fontsize=7)
    ax.set_title(title, fontsize=9)
    ax.grid(False)
fig.colorbar(image, ax=axes, shrink=0.8, label="matrix entry")
save_figure(fig, "vector_matrices", ...)
```

Four $8 \times 8$ matrices are drawn with the colour scale from $-1.6$ to $1.6$ (a boost has entries $\cosh 1 \approx 1.54$), and each nonzero entry is written in its square with two decimals (`:.2f`). In `05d_6_vector_matrices.png` the rotation has $0.50$ and $\pm0.87$ ($\cos$ and $\sin$ of $\pi/3$) in the $(x1, x2)$ block, the boost $1.54$ and $-1.18$ ($\cosh 1$ and $-\sinh 1$) in the $(x1, x4)$ block, the reflection one $-1$ at $x1$, and $\Lambda(\Gamma)$ is $-1$ on the whole diagonal.

**In [17], the last check.**

```python
FIGURES = ["05d_1_plane_types.png", "05d_2_half_angles.png",
           "05d_3_rotation_matrices.png", "05d_4_orbits.png",
           "05d_5_invariant_forms.png", "05d_6_vector_matrices.png"]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in FIGURES),
      "the six figure files of notebook 05d exist")
all_checks_passed()
```

The six figure files must exist, and the last line reads ALL 20 CHECKS PASSED (notebook 05d): one in In [2], three in In [3], one in In [4], In [5] and In [6] each, two in In [7], one each in In [8], In [9] and In [10], two in In [11], one in In [13], three in In [14], one in In [15] and one in In [17]. Six of them (In [2], the three of In [3], In [4] and the first of In [11]) reproduce recorded checks; the other fourteen are the notebook's own computations.

### 5.23 What do the scaled commutators generate?

The 28 scaled commutators $S^{ab} = \tfrac14[\gamma^a, \gamma^b]$ are called the generators. It is tempting to say that they generate Pin(4,4). This section answers exactly what they generate, and the answer is: **not all of Pin(4,4), and not even all of Spin(4,4)**. The products of their exponentials form the piece of Pin(4,4) that is joined to $1$, written $\mathrm{Spin}_0(4,4)$; Pin(4,4) consists of four such pieces; and the exponentials together with the two gammas $\gamma^{(x8)}$ and $\gamma^{(x4)}$ generate all of Pin(4,4). The proof has ten steps, (A) to (J); Notebook 05f checks each of them on the matrices.

**(A) The matrices by which the generators move the directions.** The vector rule of Section 5.12 can be written $[S^{ab}, \gamma^c] = \sum_d M^{ab}_{dc}\gamma^d$ with the $8 \times 8$ matrix

$$
M^{ab}_{dc} = \eta^{bc}\delta_{da} - \eta^{ac}\delta_{db} ,
$$

where $\delta_{da}$ is 1 for $d = a$ and 0 otherwise (insert it: the sum over $d$ picks $\eta^{bc}\gamma^a - \eta^{ac}\gamma^b$). For $a \neq b$ exactly two entries are nonzero: in row $a$, column $b$ the entry $\eta^{bb} = \eta_{bb}$ (take $c = b$, $d = a$), and in row $b$, column $a$ the entry $-\eta_{aa}$ (take $c = a$, $d = b$).

**(B) A basis of so(4,4).** The Lie algebra **so(4,4)** is the set of real $8 \times 8$ matrices $X$ with $X^T\eta + \eta X = 0$ (the infinitesimal form of $\Lambda^T\eta\Lambda = \eta$). Since $(\eta X)^T = X^T\eta$, the condition says that $\eta X$ is antisymmetric. An antisymmetric $8 \times 8$ matrix is fixed by its $8 \cdot 7/2 = 28$ entries above the diagonal, so so(4,4) has dimension 28. For $M^{ab}$ the matrix $\eta M^{ab}$ has the entry $\eta_{aa}\eta_{bb}$ in row $a$, column $b$ and $-\eta_{bb}\eta_{aa}$ in row $b$, column $a$: it is antisymmetric, so every $M^{ab}$ lies in so(4,4). The 28 matrices $M^{ab}$ with $a$ before $b$ have their nonzero entries in 28 different pairs of places, so they are independent: they are a **basis** of so(4,4).

**(C) Commutators go to commutators.** Multiplying out shows the **Jacobi identity** $[[X, Y], Z] = [X, [Y, Z]] - [Y, [X, Z]]$ for any three matrices (both sides are $XYZ - YXZ - ZXY + ZYX$). Let $[S_1, \gamma^c] = \sum_d (M_1)_{dc}\gamma^d$ and $[S_2, \gamma^c] = \sum_d (M_2)_{dc}\gamma^d$. Then

$$
[S_1, [S_2, \gamma^c]] = \sum_d (M_2)_{dc}[S_1, \gamma^d] = \sum_{d,e} (M_1)_{ed}(M_2)_{dc}\gamma^e = \sum_e (M_1M_2)_{ec}\gamma^e ,
$$

and the Jacobi identity gives $[[S_1, S_2], \gamma^c] = \sum_e ([M_1, M_2])_{ec}\gamma^e$: **the matrix of a commutator is the commutator of the matrices.** Together with (B) and the so(4,4) rules of Section 5.18, the 28 independent $S^{ab}$ and the 28 matrices $M^{ab}$ have the same commutation table: the $S^{ab}$ span an exact copy of so(4,4). (The $S^{ab}$ are independent because they are one half times 28 different products of two gammas, which are independent by Section 5.13.)

**(D) Every exponential is a product of two unit vectors.** For a rotation ($\eta_{aa}\eta_{bb} = +1$), $\exp(\theta S^{ab}) = \cos\tfrac\theta2\,1 + \sin\tfrac\theta2\,\gamma^a\gamma^b$ (Section 5.18). Because $\gamma^a\gamma^a = \eta_{aa}1$ and $\eta_{aa}^2 = 1$,

$$
\gamma^a\big(\eta_{aa}\cos\tfrac\theta2\,\gamma^a + \sin\tfrac\theta2\,\gamma^b\big) = \cos\tfrac\theta2\,1 + \sin\tfrac\theta2\,\gamma^a\gamma^b .
$$

So $\exp(\theta S^{ab}) = \gamma^a\gamma(u)$ with $u = \eta_{aa}\cos\tfrac\theta2\,e_a + \sin\tfrac\theta2\,e_b$, and $\eta(u, u) = \eta_{aa}\cos^2\tfrac\theta2 + \eta_{bb}\sin^2\tfrac\theta2 = \eta_{aa}$ (since $\eta_{bb} = \eta_{aa}$ for a rotation). For a boost the same steps with $\cosh$ and $\sinh$ give $u = \eta_{aa}\cosh\tfrac\theta2\,e_a + \sinh\tfrac\theta2\,e_b$ and $\eta(u, u) = \eta_{aa}(\cosh^2\tfrac\theta2 - \sinh^2\tfrac\theta2) = \eta_{aa}$, since $\eta_{bb} = -\eta_{aa}$. Both $\gamma^a$ and $\gamma(u)$ are unit vectors: **every exponential lies in Spin(4,4)**, and so does every product of exponentials.

**(E) How an exponential moves the directions.** Put $R(\theta) = \exp(\theta S)$ for one generator $S = S^{ab}$, and $F_c(\theta) = R\gamma^cR^{-1}$. Differentiating the power series term by term gives $dR/d\theta = SR = RS$, and $d(R^{-1})/d\theta = -SR^{-1}$ (since $R^{-1} = \exp(-\theta S)$). By the product rule of differentiation,

$$
\frac{dF_c}{d\theta} = SR\gamma^cR^{-1} - R\gamma^cSR^{-1} = R\,[S, \gamma^c]\,R^{-1} = \sum_d M_{dc}F_d .
$$

Writing $F_c = \sum_e\Lambda_{ec}(\theta)\gamma^e$, this says $d\Lambda/d\theta = \Lambda M$ with $\Lambda(0) = 1$, whose solution is the matrix exponential $\Lambda(\theta) = \exp(\theta M)$ (it solves the equation, because $d\exp(\theta M)/d\theta = \exp(\theta M)M$, and a linear equation of this kind has only one solution with a given starting value, a fact of the theory of differential equations quoted here). From the two entries of $M = M^{ab}$: $Me_a = -\eta_{aa}e_b$ and $Me_b = \eta_{bb}e_a$, so $MMe_a = -\eta_{aa}\eta_{bb}e_a$. Summing the power series as in Section 5.18:

$$
\Lambda e_a = \cos\theta\,e_a - \eta_{aa}\sin\theta\,e_b \ \ \text{(rotation)}, \qquad \Lambda e_a = \cosh\theta\,e_a - \eta_{aa}\sinh\theta\,e_b \ \ \text{(boost)} .
$$

**(F) The forbidden band.** Order the directions as $x1, x2, x3, x8$ (space-like) and then $x4, x5, x6, x7$ (time-like), and cut a vector matrix into four $4 \times 4$ blocks,

$$
\Lambda = \begin{pmatrix} A & B' \\ C' & D \end{pmatrix} .
$$

$A$ is the **space block** and $D$ the **time block** (the primes distinguish the other two blocks from the matrices $B$ and $C$). In this order $\eta = \mathrm{diag}(1_4, -1_4)$, and multiplying out the blocks of $\Lambda^T\eta\Lambda = \eta$ gives, in the top-left and bottom-right places,

$$
A^TA - C'^TC' = 1_4, \qquad D^TD - B'^TB' = 1_4 .
$$

For every column $w$ of four numbers the first equation gives $|Aw|^2 = w^TA^TAw = |w|^2 + |C'w|^2 \geq |w|^2$, where $|w|^2 = w^Tw$ is the squared length. So every eigenvalue of the symmetric matrix $A^TA$ is at least 1 (take $w$ an eigenvector of length 1), and $(\det A)^2 = \det(A^TA)$, the product of these eigenvalues, is at least 1. **So $\det A$ is never between $-1$ and $1$**; the same holds for $\det D$. This holds for every matrix of O(4,4).

**(G) Products of exponentials stay above the band.** Let $h = \exp(\theta_1S_1)\cdots\exp(\theta_nS_n)$ be a product of exponentials, and $h(t) = \exp(t\theta_1S_1)\cdots\exp(t\theta_nS_n)$ for $0 \le t \le 1$: a path from $h(0) = 1$ to $h(1) = h$. The entries of $\Lambda(h(t))$ are sums of products of $\cos$, $\sin$, $\cosh$ and $\sinh$ of multiples of $t$, so $\det A(t)$ is a continuous function of $t$. It starts at $\det 1_4 = 1$ and never enters the band $(-1, 1)$; by the intermediate value theorem (a continuous function that takes a value below $-1$ and one above $1$ also takes every value between) it can never become negative. So $\det A \geq 1$ along the whole path, and in the same way $\det D \geq 1$. **Every product of exponentials has the sign pattern $(+, +)$**, where the **sign pattern** of $g$ is the pair (sign of $\det A$, sign of $\det D$).

**(H) Four pieces.** $\Lambda(\gamma^{(x8)}) = R_{e_{x8}}$ reverses only the direction $x8$: its space block has determinant $-1$ and its time block $+1$, pattern $(-, +)$. $\Lambda(\gamma^{(x4)})$ reverses only $x4$: pattern $(+, -)$. $\Lambda(\gamma^{(x8)}\gamma^{(x4)})$ reverses both: $(-, -)$. For a product of exponentials $h$ and $w$ one of these, $\Lambda(hw) = \Lambda(h)\Lambda(w)$ (Section 5.12), and $\Lambda(w)$ is a diagonal matrix of signs: multiplying by it from the right only changes the signs of some columns of $\Lambda(h)$, so the space block of $hw$ is $A$ times a diagonal matrix of signs and $hw$ has the pattern of $w$. Four different patterns: the four sets

$$
\mathrm{Spin}_0, \quad \mathrm{Spin}_0\,\gamma^{(x8)}, \quad \mathrm{Spin}_0\,\gamma^{(x4)}, \quad \mathrm{Spin}_0\,\gamma^{(x8)}\gamma^{(x4)}
$$

have no element in common, where $\mathrm{Spin}_0 = \mathrm{Spin}_0(4,4)$ is the group of all products of exponentials and $\mathrm{Spin}_0\,w$ the set of the products $hw$. In particular **$\gamma^{(x8)}\gamma^{(x4)}$ lies in Spin(4,4) but is not a product of exponentials**, in agreement with its spinor norm (Section 5.18).

**(I) Every unit vector is a turned $\gamma^{(x8)}$ or $\gamma^{(x4)}$.** Let $v$ be a space-like unit vector, with space part $\sigma$ (its components along $x1, x2, x3, x8$) and time part $\tau$ (along $x4, \dots, x7$), so that $|\sigma|^2 - |\tau|^2 = 1$. Three stages carry $e_{x8}$ to $v$:

- a boost in the plane $(x8, x4)$ carries $e_{x8}$ to $|\sigma|\,e_{x8} + |\tau|\,e_{x4}$ (by (E), choose $\sinh\theta = -|\tau|$; then $\cosh\theta = \sqrt{1 + |\tau|^2} = |\sigma|$);
- three rotations in the planes $(x4, x5)$, $(x4, x6)$, $(x4, x7)$ turn $e_{x4}$ into $\tau/|\tau|$ and do not touch $x8$, giving $|\sigma|\,e_{x8} + \tau$;
- three rotations in the planes $(x8, x1)$, $(x8, x2)$, $(x8, x3)$ turn $e_{x8}$ into $\sigma/|\sigma|$ and do not touch the time part, giving $\sigma + \tau = v$.

Each rotation stage turns the axis vector step by step: the first rotation puts the right component on the first other direction and keeps the rest of the length on the axis, the second does the same for the next direction, and the last leaves exactly the axis component of the target. The angles follow from (E). With $h$ the product of these at most seven exponentials, $\Lambda(h)e_{x8} = v$, and since $h$ is even,

$$
h\gamma^{(x8)}h^{-1} = \sum_d\Lambda(h)_{d,x8}\,\gamma^d = \gamma(\Lambda(h)e_{x8}) = \gamma(v) .
$$

A time-like unit vector is treated in the same way, starting from $e_{x4}$ with a boost in the plane $(x4, x8)$.

**(J) Moving the gammas to the right.** Moving $\gamma^e$ through $\gamma^a\gamma^b$ costs $(-1)^2 = +1$ when $e$ is neither $a$ nor $b$, and $-1$ when $e$ is one of them (Rule 1). So $\gamma^eS^{ab}(\gamma^e)^{-1} = s\,S^{ab}$ with that sign $s$, and, term by term in the power series,

$$
\gamma^e\exp(\theta S^{ab}) = \exp(s\theta S^{ab})\,\gamma^e .
$$

Now take any element $g = \gamma(v_1)\cdots\gamma(v_k)$ of Pin(4,4). Write each factor as in (I), $\gamma(v_j) = h_j\gamma^{e_j}h_j^{-1}$ with $e_j = x8$ or $x4$. Move every gamma to the right end with the rule just proved: what remains on the left is a product of exponentials, and on the right a product of gammas $\gamma^{(x8)}$ and $\gamma^{(x4)}$. With $\gamma^{(x8)}\gamma^{(x8)} = 1$, $\gamma^{(x4)}\gamma^{(x4)} = -1$ and $\gamma^{(x4)}\gamma^{(x8)} = -\gamma^{(x8)}\gamma^{(x4)}$, that product is $\pm$ one of $1$, $\gamma^{(x8)}$, $\gamma^{(x4)}$, $\gamma^{(x8)}\gamma^{(x4)}$, and a sign $-1$ is itself the product of exponentials $\exp(2\pi S^{(x1)(x2)}) = -1$ (Section 5.18).

**The answer.** By (D) the exponentials lie in Pin(4,4), and $\gamma^{(x8)}$ and $\gamma^{(x4)}$ do by definition; by (I) and (J) every element of Pin(4,4) is a product of exponentials times one of the four words; by (G) and (H) the four pieces are different. So

$$
\mathrm{Pin}(4,4) = \mathrm{Spin}_0 \cup \mathrm{Spin}_0\,\gamma^{(x8)} \cup \mathrm{Spin}_0\,\gamma^{(x4)} \cup \mathrm{Spin}_0\,\gamma^{(x8)}\gamma^{(x4)} ,
$$

four pieces with no element in common, and Spin(4,4), the even elements, is the union of the first and the last piece. **The exponentials of the scaled commutators generate exactly $\mathrm{Spin}_0(4,4)$; together with $\gamma^{(x8)}$ and $\gamma^{(x4)}$ they generate all of Pin(4,4).** It is not correct to say that the scaled commutators alone generate Pin(4,4). Nothing in the representation statements of Section 5.13 changes: irreducibility under Pin(4,4) and the two inequivalent halves already hold for the smaller groups (Section 5.13).

**What the group elements span.** For a rotation, $\exp(\pi S^{ab}) = \gamma^a\gamma^b$ ($\cos\tfrac\pi2 = 0$, $\sin\tfrac\pi2 = 1$); for a boost, $(\exp(\theta S^{ab}) - \exp(-\theta S^{ab}))/(2\sinh\tfrac\theta2) = \gamma^a\gamma^b$. So the span of $\mathrm{Spin}_0(4,4)$ contains every product of two different gammas, and, because the span of a group contains the products of its members, every even product of different gammas: all 128 of them. Every element is even, so the span is exactly these 128 dimensions, the block-diagonal matrices. Adding one gamma adds the odd products: the span of Pin(4,4) is all 256 dimensions.

| statement | status | where it is verified |
| --- | --- | --- |
| the 28 $S^{ab}$ are independent (rank 28) and span a copy of so(4,4) | PROVED; rank COMPUTED exactly | `python-algebra.json`, checks `S_definition`, `S_vector_action` and `S_lorentz_algebra`; Notebook 05f (rank 28, dimension of so(4,4) 28, the 784 commutators of the $M^{ab}$) |
| (D) and (E): $\exp(\theta S^{ab}) = \gamma^a\gamma(u)$; $\Lambda = \exp(\theta M^{ab})$ | PROVED above; COMPUTED (to $10^{-10}$ and $10^{-12}$) | Notebook 05f, its own computation |
| (F) to (H): the forbidden band, the sign pattern $(+, +)$ of $\mathrm{Spin}_0(4,4)$, the four pieces | PROVED above; COMPUTED on 200 and 240 random elements and along ten paths | Notebook 05f, its own computation |
| (I) and (J): every element of Pin(4,4) is in one of the four pieces | PROVED above; COMPUTED on 40 unit vectors and 12 elements | Notebook 05f, its own computation |
| the spans: 128 for $\mathrm{Spin}_0(4,4)$, 256 for Pin(4,4) | PROVED above; COMPUTED (singular values) | `python-algebra.json`, checks `even_products_span_M8_plus_M8` and `clifford_products_span_M16`; Notebook 05f |

### 5.24 Example: Notebook 05f computes what the scaled commutators generate

Notebook 05f checks steps (A) to (J) one by one: the rank 28 of the generators, the 28 matrices $M^{ab}$ and their commutators, the dimension 28 of so(4,4), the factorisation of every exponential into two unit vectors, the formula $\Lambda = \exp(\theta M)$, the block equations and the band on 200 random products of exponentials, the four sign patterns on 240 random elements, ten paths from $1$ that never cross the band, the construction of (I) on 40 random unit vectors, the rule of (J), the decomposition of 12 random elements of Pin(4,4) into exponentials times one of four words, and the spans 128 and 256. All random numbers come from a generator with a fixed seed, so every run makes the same choices. It draws six figures and ends with ALL 24 CHECKS PASSED (notebook 05f).

<!-- NOTEBOOK 05f -->

### 5.27 Line-by-line walk-through of Notebook 05f

The notebook has 19 code cells. In [1] is the set-up cell of Section 5.10 with `NOTEBOOK_ID = "05f"`; its comments repeat the instructions of Section 5.25.

**In [2], the gammas and the recorded checks.**

```python
import contextlib  # lets a block of code print into a text buffer
import io  # the text buffer io.StringIO
import sys  # sys.stdout: the channel through which the notebook prints

import numpy as np  # arrays of numbers, matrices and linear algebra

fixture = json.loads(repository_file("Revision/algebra/gammas.json")
                     .read_text(encoding="utf-8"))
COORDS = fixture["coordinates"]  # "x1", ..., "x8"
ETA = dict(zip(COORDS, fixture["eta"]))  # +1 space-like, -1 time-like
ETA_MATRIX = np.diag([float(ETA[x]) for x in COORDS])  # the 8 x 8 metric eta
gamma = {x: np.array(m, dtype=np.int64) for x, m in zip(COORDS, fixture["gamma"])}
I16 = np.eye(16, dtype=np.int64)  # the 16 x 16 identity matrix 1
SPACE = ["x1", "x2", "x3", "x8"]  # the four space-like directions
TIME = ["x4", "x5", "x6", "x7"]  # the four time-like directions
```

The gammas are read as in Notebook 05d; `ETA_MATRIX` is the $8 \times 8$ metric. New are the lists `SPACE` and `TIME` of the space-like and time-like directions, in the order used for the blocks of step (F).

```python
REPORT_FILES = {"python": "Revision/algebra/reports/python-algebra.json",
                "wolfram": "Revision/algebra/reports/wolfram-algebra.json"}
VERDICTS = {}  # (report key, check name) -> (verdict in lower case, detail text)
for key, path in REPORT_FILES.items():
    report_data = json.loads(repository_file(path).read_text(encoding="utf-8"))
    for entry in report_data["checks"]:
        VERDICTS[(key, entry["name"])] = (entry["verdict"].lower(), entry["detail"])


def recorded(key, name):
    return VERDICTS[(key, name)][0] == "pass"


def record_of(key, name):
    return f"{REPORT_FILES[key]}, check {name}"


def check_reproduces(condition, name, record):
    collected = io.StringIO()
    with contextlib.redirect_stdout(collected):  # print into the buffer
        check(condition, name, record=record)  # stops here if the check fails
    sys.stdout.write(collected.getvalue())  # the PASS and reproduces lines together


def eta(a, b):
    return ETA[a] if a == b else 0


check_reproduces(all(np.array_equal(gamma[a] @ gamma[b] + gamma[b] @ gamma[a],
                                    2 * eta(a, b) * I16) for a in COORDS for b in COORDS)
                 and recorded("python", "clifford_relation"),
                 "{gamma^a, gamma^b} = 2 eta^ab 1 for all 64 pairs",
                 record=record_of("python", "clifford_relation"))
```

The reports, the helpers and the Clifford check are those of Notebook 05d, In [2] (Section 5.22).

**In [3], the 28 generators are independent.**

```python
import sympy as sp  # exact algebra
from sympy.polys.matrices import DomainMatrix  # exact matrices over QQ

S = {(a, b): (gamma[a] @ gamma[b] - gamma[b] @ gamma[a]) / 4.0
     for a in COORDS for b in COORDS}  # all 64 ordered pairs; S^aa = 0
pairs = [(a, b) for i, a in enumerate(COORDS) for b in COORDS[i + 1:]]  # 28 planes


def exact_rank(rows):
    whole = [[int(round(x)) for x in row] for row in rows]  # entries 0, +1, -1
    return DomainMatrix.from_list(whole, sp.QQ).rank()
```

`S` and `pairs` are those of Notebook 05d. `exact_rank` takes a list of rows whose entries are whole numbers stored as floating-point numbers, turns each entry into a Python whole number (`int(round(x))`), and computes the rank exactly over the rational numbers, as in Notebook 05b.

```python
rank_S = exact_rank([(gamma[a] @ gamma[b]).reshape(256) for a, b in pairs])
entries = sorted({float(v) for p in pairs for v in S[p].flat})
say(f"{len(pairs)} generators; their entries are {entries}; exact rank {rank_S}")
check_reproduces(rank_S == 28 and entries == [-0.5, 0.0, 0.5]
                 and all(np.array_equal(S[(a, b)], gamma[a] @ gamma[b] / 2.0)
                         for a, b in pairs)
                 and recorded("python", "S_definition"),
                 "the 28 S^ab = (1/2) gamma^a gamma^b are linearly independent "
                 "(exact rank 28)",
                 record=record_of("python", "S_definition"))
```

The 28 whole-number matrices $2S^{ab} = \gamma^a\gamma^b$, each written as a row of 256 numbers, have the exact rank 28 (printed together with the entries $-0.5$, $0$, $0.5$ of the $S^{ab}$): no generator is a combination of the others.

**In [4], the matrices $M^{ab}$: a copy of so(4,4).**

```python
def generator_matrix(a, b):
    result = np.zeros((8, 8))
    for j, c in enumerate(COORDS):
        for i, d in enumerate(COORDS):
            result[i, j] = eta(b, c) * (d == a) - eta(a, c) * (d == b)
    return result


M = {(a, b): generator_matrix(a, b) for a in COORDS for b in COORDS}  # all 64
```

`generator_matrix(a, b)` fills the $8 \times 8$ matrix of step (A), $M^{ab}_{dc} = \eta^{bc}\delta_{da} - \eta^{ac}\delta_{db}$, entry by entry: `(d == a)` is true or false, which Python counts as 1 or 0, so it plays the role of $\delta_{da}$. `M` holds the matrices for all 64 ordered pairs.

```python
vector_ok = all(
    np.array_equal(S[p] @ gamma[c] - gamma[c] @ S[p],
                   sum(M[p][i, j] * gamma[d] for i, d in enumerate(COORDS)))
    for p in pairs for j, c in enumerate(COORDS))
check_reproduces(vector_ok and recorded("python", "S_vector_action")
                 and recorded("wolfram", "S_gamma_commutator"),
                 "[S^ab, gamma^c] = sum_d M^ab_dc gamma^d with M_dc = eta^bc delta_da "
                 "- eta^ac delta_db",
                 record=record_of("python", "S_vector_action"))
```

For the 28 planes and the 8 directions $c$ the commutator $[S^{ab}, \gamma^c]$ is compared with $\sum_dM^{ab}_{dc}\gamma^d$: the vector rule in the form of step (A).

```python
in_so44 = all(not (M[p].T @ ETA_MATRIX + ETA_MATRIX @ M[p]).any() for p in pairs)
rank_M = exact_rank([M[p].reshape(64) for p in pairs])
equations = []  # the 64 equations (X^T eta + eta X)_rc = 0 for the entries of X
for r in range(8):
    for c in range(8):
        row = np.zeros(64)
        row[r * 8 + c] += ETA_MATRIX[r, r]  # (eta X)_rc = eta_rr X_rc
        row[c * 8 + r] += ETA_MATRIX[c, c]  # (X^T eta)_rc = X_cr eta_cc
        equations.append(row)
dimension_so44 = 64 - exact_rank(equations)
say(f"rank of the 28 matrices M^ab: {rank_M}; dimension of so(4,4): "
    f"{dimension_so44}")
check(in_so44 and rank_M == 28 and dimension_so44 == 28,
      "every M^ab lies in so(4,4), the 28 M^ab are independent and so(4,4) has "
      "dimension 28: the M^ab are a basis of so(4,4)")
```

Step (B) in three parts. `in_so44`: every $M^{ab}$ obeys $(M^{ab})^T\eta + \eta M^{ab} = 0$. `rank_M`: the 28 matrices, each written as a row of 64 numbers, have rank 28. `equations`: the condition $X^T\eta + \eta X = 0$ for an unknown $8 \times 8$ matrix $X$ is written as 64 linear equations for its 64 entries, listed row by row (the entry $X_{rc}$ is unknown number $8r + c$). The entry $(r, c)$ of $\eta X$ is $\eta_{rr}X_{rc}$ and that of $X^T\eta$ is $X_{cr}\eta_{cc}$, so equation $(r, c)$ has the coefficient $\eta_{rr}$ at the place of $X_{rc}$ and $\eta_{cc}$ at the place of $X_{cr}$ (`+=` adds, so that on the diagonal, where the two places coincide, both contributions count). The dimension of so(4,4) is 64 minus the rank of these equations. The printed line shows 28 and 28.

```python
def table_failures(X):
    failures = 0
    for a, b in pairs:
        for c, d in pairs:
            right = (eta(b, c) * X[(a, d)] - eta(a, c) * X[(b, d)]
                     - eta(b, d) * X[(a, c)] + eta(a, d) * X[(b, c)])
            if not np.array_equal(X[(a, b)] @ X[(c, d)] - X[(c, d)] @ X[(a, b)],
                                  right):
                failures += 1
    return failures


failures_S, failures_M = table_failures(S), table_failures(M)
say(f"pairs that break the table: S^ab {failures_S}, M^ab {failures_M} (of 784)")
check_reproduces(failures_S == 0 and failures_M == 0
                 and recorded("python", "S_lorentz_algebra")
                 and recorded("wolfram", "S_Lorentz_algebra"),
                 "the S^ab and the M^ab have the same commutators: the S^ab span an "
                 "exact copy of so(4,4)",
                 record=record_of("python", "S_lorentz_algebra"))
```

`table_failures` counts the pairs of planes for which a family of 64 matrices breaks the so(4,4) commutation table. It is applied to the $S^{ab}$ (a recorded fact) and to the $M^{ab}$ (step (C)): 0 failures of 784 for both.

**In [5], the shape of the $M^{ab}$.**

```python
from matplotlib.colors import LinearSegmentedColormap

SIGNS = LinearSegmentedColormap.from_list("signs", ["#2a78d6", "#f0efec", "#e34948"])
shape_ok = all(
    np.count_nonzero(M[(a, b)]) == 2
    and np.array_equal(M[(a, b)].T, -ETA[a] * ETA[b] * M[(a, b)]) for a, b in pairs)
check(shape_ok, "each M^ab has two nonzero entries; antisymmetric for the 12 "
      "rotations, symmetric for the 16 boosts")
```

Step (A) predicts two nonzero entries ($\eta_{bb}$ and $-\eta_{aa}$ in mirrored places). They have opposite signs, so the matrix is antisymmetric, when $\eta_{aa}\eta_{bb} = +1$ (a rotation), and equal signs, so it is symmetric, for a boost: in one formula $(M^{ab})^T = -\eta_{aa}\eta_{bb}M^{ab}$. `np.count_nonzero` counts the nonzero entries.

```python
fig, axes = plt.subplots(4, 7, figsize=(14.0, 8.8))
numbers = [x[1] for x in COORDS]  # the tick labels 1, ..., 8
for ax, (a, b) in zip(axes.flat, pairs):
    ax.imshow(M[(a, b)], cmap=SIGNS, vmin=-1, vmax=1)
    kind = "rotation" if ETA[a] * ETA[b] == 1 else "boost"
    ax.set_title(f"$M^{{{a}\\,{b}}}$, {kind}", fontsize=9)
    ax.set_xticks(range(8), numbers, fontsize=6)
    ax.set_yticks(range(8), numbers, fontsize=6)
    ax.grid(False)
fig.suptitle("The 28 matrices $M^{ab}$: how $S^{ab}$ moves the directions "
             "$x1$ to $x8$ (rows and columns numbered 1 to 8)")
save_figure(fig, "generator_matrices", ...)
```

A grid of 4 rows and 7 columns of small pictures, one per plane (`axes.flat` runs through the 28 picture areas). `x[1]` is the second character of a name such as `x5`, so the tick labels are the numbers 1 to 8. In the f-string of the title, three braces `{{{a}` give one literal brace followed by the value of `a`, and `\\,` a small space. `fig.suptitle` is a title over the whole figure. In `05f_1_generator_matrices.png` every small picture has exactly two coloured squares, mirrored about the diagonal: of opposite colours for the 12 rotations, of the same colour for the 16 boosts.

**In [6], the exponential and its two factors.**

```python
def exponential(a, b, theta):
    J = (gamma[a] @ gamma[b]).astype(float)  # J = 2 S^ab, J J = -eta_aa eta_bb
    if ETA[a] * ETA[b] == 1:  # J J = -1: a rotation
        return np.cos(theta / 2) * np.eye(16) + np.sin(theta / 2) * J
    return np.cosh(theta / 2) * np.eye(16) + np.sinh(theta / 2) * J  # a boost


def series_exponential(X, terms=60):
    result = np.eye(X.shape[0])
    term = np.eye(X.shape[0])
    for k in range(1, terms):
        term = term @ X / k  # X^k / k! from X^(k-1) / (k-1)!
        result = result + term
    return result
```

`exponential` is the closed formula and `series_exponential` the power series, here summed to 60 terms; both work as `spin_transformation` and `exp_series` of Notebook 05d (Section 5.22, In [6]). `series_exponential` also serves for the $8 \times 8$ matrix exponential $\exp(\theta M)$ in In [8].

```python
def gamma_of(v):
    return sum(v[i] * gamma[x].astype(float) for i, x in enumerate(COORDS))


def metric_product(u, v):
    return float(u @ ETA_MATRIX @ v)


def second_factor(a, b, theta):
    i, j = COORDS.index(a), COORDS.index(b)
    if ETA[a] * ETA[b] == 1:  # a rotation
        return ETA[a] * np.cos(theta / 2) * E8[i] + np.sin(theta / 2) * E8[j]
    return ETA[a] * np.cosh(theta / 2) * E8[i] + np.sinh(theta / 2) * E8[j]


E8 = np.eye(8)  # E8[i] is the basic unit vector of the direction COORDS[i]
```

`gamma_of` and `metric_product` are $\gamma(v)$ and $\eta(u, v)$ as in Notebook 05d. `second_factor(a, b, theta)` is the unit vector $u$ of step (D): $\eta_{aa}\cos\tfrac\theta2\,e_a + \sin\tfrac\theta2\,e_b$ for a rotation and the same with $\cosh$ and $\sinh$ for a boost. `E8[i]` is the basic unit vector of the direction number `i`; the function uses `E8`, which is defined in the line after it, before the function is first called, so this is allowed.

```python
series_gap = max(np.max(np.abs(series_exponential(0.9 * S[p]) - exponential(*p, 0.9)))
                 for p in pairs)
check(series_gap < 1e-10, "the closed formula equals the power series of "
      "exp(theta S^ab) for all 28 planes (difference below 1e-10)")
factor_ok = True
for a, b in pairs:
    for theta in [-2.5, -0.4, 0.9, 2.2, 5.0]:
        u = second_factor(a, b, theta)
        factor_ok &= (np.allclose(gamma[a] @ gamma_of(u), exponential(a, b, theta),
                                  rtol=0.0, atol=1e-10)
                      and abs(metric_product(u, u) - ETA[a]) < 1e-10)
check(factor_ok, "exp(theta S^ab) = gamma^a gamma(u) with eta(u, u) = eta_aa: a "
      "product of two unit vectors (28 planes, 5 values each)")
```

The first check compares the closed formula with the series for all 28 planes at $\theta = 0.9$. The second checks step (D) for all 28 planes at five values of $\theta$: $\exp(\theta S^{ab}) = \gamma^a\gamma(u)$ and $\eta(u, u) = \eta_{aa}$. (`rtol=0.0, atol=1e-10` makes `np.allclose` accept only differences below $10^{-10}$, without a relative tolerance.)

**In [7], the picture of the second factor.**

```python
cases = [("x1", "x2", np.linspace(0.0, 4 * np.pi, 241)),
         ("x1", "x4", np.linspace(-3.0, 3.0, 241)),
         ("x4", "x8", np.linspace(-3.0, 3.0, 241))]
fig, axes = plt.subplots(1, 3, figsize=(13.0, 4.6))
norm_ok = True  # eta(u, u) = eta_aa along all three curves
for ax, (a, b, thetas) in zip(axes, cases):
    points = np.array([second_factor(a, b, th) for th in thetas])
    i, j = COORDS.index(a), COORDS.index(b)
    norms = [metric_product(p, p) for p in points]
    norm_ok &= max(abs(n - ETA[a]) for n in norms) < 1e-10
    ax.plot(points[:, i], points[:, j], color="#2a78d6", linewidth=2)
    marks = points[::40]  # every 40th value of theta
    ax.plot(marks[:, i], marks[:, j], "o", color="#eb6834", markersize=6)
    kind = "rotation" if ETA[a] * ETA[b] == 1 else "boost"
    ax.set_title(f"{kind} in $({a}, {b})$: $\\eta(u, u) = {norms[0]:+.0f}$")
    ax.set_xlabel(f"$u_{{{a}}}$")
    ax.set_ylabel(f"$u_{{{b}}}$")
    ax.set_aspect("equal")
    ax.set_xlim(-4.2, 4.2)
    ax.set_ylim(-4.2, 4.2)
check(norm_ok, "along the three curves eta(u, u) stays equal to eta_aa")
save_figure(fig, "two_unit_vectors", ...)
```

For three planes (a rotation over $\theta$ from 0 to $4\pi$ and two boosts over $-3$ to 3) the cell computes the second factor $u$ at 241 values and plots its two nonzero components against each other, with an orange dot every 40th value. The check confirms $\eta(u, u) = \eta_{aa}$ along all three curves, and each title prints this value ($+1$ for the planes starting with $x1$, $-1$ for the plane $(x4, x8)$). In `05f_2_two_unit_vectors.png` the rotation's $u$ runs once around the unit circle, and the boosts' $u$ run along branches of hyperbolas.

**In [8], the vector matrix of an exponential.**

```python
def vector_matrix(g, odd=False):
    g_inverse = np.linalg.inv(g)
    sign = -1.0 if odd else 1.0
    result = np.zeros((8, 8))
    for j, c in enumerate(COORDS):
        moved = sign * (g @ gamma[c] @ g_inverse)  # alpha(g) gamma^c g^-1
        for i, d in enumerate(COORDS):
            result[i, j] = ETA[d] * np.trace(gamma[d] @ moved) / 16.0
    return result
```

`vector_matrix(g, odd)` is the vector matrix of Section 5.12 with the twisted action: for an odd element (`odd=True`) the moved gamma gets the sign $-1$. Otherwise it is the trace formula of Notebook 05d.

```python
exp_ok = True
for p in pairs:
    Lam = vector_matrix(exponential(*p, 0.9))
    exp_ok &= (np.allclose(Lam, series_exponential(0.9 * M[p]), rtol=0.0, atol=1e-12)
               and np.allclose(Lam.T @ ETA_MATRIX @ Lam, ETA_MATRIX, atol=1e-12)
               and abs(np.linalg.det(Lam) - 1.0) < 1e-12)
check(exp_ok, "the vector matrix of exp(theta S^ab) is exp(theta M^ab); it keeps "
      "the metric and has determinant 1 (28 planes)")
```

Step (E) for all 28 planes at $\theta = 0.9$: the vector matrix of the spinor exponential equals the $8 \times 8$ exponential $\exp(0.9\,M^{ab})$, keeps the metric and has determinant 1.

```python
def turned_axis(a, b, theta):
    i, j = COORDS.index(a), COORDS.index(b)
    if ETA[a] * ETA[b] == 1:  # a rotation
        return np.cos(theta) * E8[i] - ETA[a] * np.sin(theta) * E8[j]
    return np.cosh(theta) * E8[i] - ETA[a] * np.sinh(theta) * E8[j]  # a boost


turn_ok = all(
    np.allclose(vector_matrix(exponential(a, b, th))[:, COORDS.index(a)],
                turned_axis(a, b, th), rtol=0.0, atol=1e-12)
    for a, b in [("x8", "x1"), ("x4", "x5"), ("x8", "x4"), ("x4", "x8")]
    for th in [-1.3, 0.4, 2.0])
check(turn_ok, "Lambda e_a = cos(theta) e_a - eta_aa sin(theta) e_b for a rotation "
      "and cosh(theta) e_a - eta_aa sinh(theta) e_b for a boost")
```

`turned_axis` is the formula of step (E) for $\Lambda e_a$. The check compares it with column $a$ of the computed vector matrix for the four planes used by the construction of step (I) ($(x8, x1)$, $(x4, x5)$, $(x8, x4)$, $(x4, x8)$; note that the order of $a$ and $b$ matters) at three values each.

**In [9], the block equations on random products.**

```python
SPACE_INDEX = [COORDS.index(x) for x in SPACE]  # the positions of x1, x2, x3, x8
TIME_INDEX = [COORDS.index(x) for x in TIME]  # the positions of x4, x5, x6, x7


def blocks(Lam):
    return (Lam[np.ix_(SPACE_INDEX, SPACE_INDEX)], Lam[np.ix_(SPACE_INDEX, TIME_INDEX)],
            Lam[np.ix_(TIME_INDEX, SPACE_INDEX)], Lam[np.ix_(TIME_INDEX, TIME_INDEX)])
```

`SPACE_INDEX` is the list of positions $[0, 1, 2, 7]$ of $x1, x2, x3, x8$ and `TIME_INDEX` the list $[3, 4, 5, 6]$. `np.ix_(rows, columns)` picks the entries in the listed rows and columns, so `blocks` returns the four $4 \times 4$ blocks $A$, $B'$, $C'$, $D$ of step (F).

```python
rng = np.random.default_rng(12345)  # random numbers with a fixed seed


def random_factors(count):
    factors = []
    for _ in range(count):
        a, b = pairs[int(rng.integers(28))]  # a random plane
        if ETA[a] * ETA[b] == 1:  # a rotation: an angle from 0 to 2 pi
            theta = rng.uniform(0.0, 2 * np.pi)
        else:  # a boost: a rapidity from -1 to 1
            theta = rng.uniform(-1.0, 1.0)
        factors.append((a, b, float(theta)))
    return factors
```

The random-number generator starts from the fixed seed 12345; every later cell draws from the same generator in the same order, so every run makes the same choices. `random_factors(count)` draws `count` factors $(a, b, \theta)$: a plane chosen at random from the 28 (`rng.integers(28)` is a whole number from 0 to 27), with a uniformly random angle in $[0, 2\pi)$ for a rotation or a rapidity in $[-1, 1)$ for a boost (`rng.uniform(low, high)`). The loop variable `_` is a name for a value that is not used.

```python
def compose(factors, t=1.0):
    g = np.eye(16)
    for a, b, theta in factors:
        g = exponential(a, b, t * theta) @ g
    return g
```

`compose(factors, t)` multiplies the exponentials $\exp(t\theta_jS_j)$ in the order of the list, each new one on the left: the result is $\exp(t\theta_nS_n)\cdots\exp(t\theta_1S_1)$, in which the first factor of the list acts first on a column. With $t$ running from 0 to 1 it is the path $h(t)$ of step (G).

```python
block_ok, smallest = True, np.inf
for _ in range(200):
    A, B_, C_, D = blocks(vector_matrix(compose(random_factors(6))))
    block_ok &= (np.allclose(A.T @ A - C_.T @ C_, np.eye(4), atol=1e-9)
                 and np.allclose(D.T @ D - B_.T @ B_, np.eye(4), atol=1e-9))
    smallest = min(smallest, np.linalg.det(A), np.linalg.det(D))
report("smallest det A or det D of 200 products of six exponentials",
       f"{smallest:.3f}")
check(block_ok and smallest > 1.0 - 1e-9,
      "200 products of exponentials: A^T A - C^T C = 1, D^T D - B^T B = 1, and "
      "det A >= 1, det D >= 1")
```

For 200 random products of six exponentials the cell checks the two block equations of step (F) (the blocks are named `B_` and `C_` so as not to overwrite other names) and keeps the smallest of all determinants of $A$ and $D$, starting from `np.inf` (infinity). The RESULT line prints it, $1.019$, and the check requires it to be at least 1: every product has the sign pattern $(+, +)$, step (G).

**In [10], the four words and the four pieces.**

```python
WORDS = {"1": (I16, False), "gamma^(x8)": (gamma["x8"], True),
         "gamma^(x4)": (gamma["x4"], True),
         "gamma^(x8) gamma^(x4)": (gamma["x8"] @ gamma["x4"], False)}


def pattern(Lam):
    A, _, _, D = blocks(Lam)
    return (int(np.sign(np.linalg.det(A))), int(np.sign(np.linalg.det(D))))
```

`WORDS` stores the four words $1$, $\gamma^{(x8)}$, $\gamma^{(x4)}$, $\gamma^{(x8)}\gamma^{(x4)}$, each with the flag that says whether it is odd. `pattern` returns the sign pattern of a vector matrix: the signs (`np.sign`) of $\det A$ and $\det D$; the two middle blocks are not needed and are given the throw-away name `_`.

```python
flip8 = np.diag([1.0, 1, 1, 1, 1, 1, 1, -1])  # reverses x8 only
flip4 = np.diag([1.0, 1, 1, -1, 1, 1, 1, 1])  # reverses x4 only
expected = {"1": np.eye(8), "gamma^(x8)": flip8, "gamma^(x4)": flip4,
            "gamma^(x8) gamma^(x4)": flip8 @ flip4}
words_ok = all(np.allclose(vector_matrix(w.astype(float), odd), expected[name])
               for name, (w, odd) in WORDS.items())
for name, (w, odd) in WORDS.items():
    say(f"{name:22} sign pattern (sign det A, sign det D) = "
        f"{pattern(vector_matrix(w.astype(float), odd))}")
check(words_ok, "the vector matrices of 1, gamma^(x8), gamma^(x4), gamma^(x8) "
      "gamma^(x4) are the identity and the reversals of x8, x4 and both")
```

The predicted vector matrices of step (H) are diagonal matrices of signs. The check compares them with the computed ones (the twisted action for the two odd words), and the four printed lines show the patterns $(1, 1)$, $(-1, 1)$, $(1, -1)$, $(-1, -1)$.

```python
points = {}  # word -> list of (det A, det D)
pieces_ok = True
for name, (w, odd) in WORDS.items():
    points[name] = []
    Lam_w = vector_matrix(w.astype(float), odd)
    for _ in range(60):
        h = compose(random_factors(6))
        Lam = vector_matrix(h @ w, odd)
        pieces_ok &= (np.allclose(Lam, vector_matrix(h) @ Lam_w, atol=1e-9)
                      and pattern(Lam) == pattern(Lam_w))
        A, _, _, D = blocks(Lam)
        points[name].append((np.linalg.det(A), np.linalg.det(D)))
check(pieces_ok, "for 4 x 60 elements h w: Lambda(h w) = Lambda(h) Lambda(w), and h w "
      "has the sign pattern of w")
```

For each word $w$ and 60 random products $h$ the cell checks $\Lambda(hw) = \Lambda(h)\Lambda(w)$ and that $hw$ has the pattern of $w$, and stores the pair $(\det A, \det D)$ for the picture.

```python
# An observation that the picture below shows and that the proof does not need:
# for every one of the 240 elements the two determinants have the same size.
equal_size = all(abs(abs(dA) - abs(dD)) < 1e-9 * max(abs(dA), 1.0)
                 for name in WORDS for dA, dD in points[name])
check(equal_size, "observed for all 240 elements: |det A| = |det D|")
```

An observation, checked but not used by the proof: for all 240 elements $|\det A| = |\det D|$, to a relative accuracy of $10^{-9}$. It is COMPUTED for these 240 elements only; the book neither proves nor uses it.

**In [11], the picture of the four pieces.**

```python
colors = {"1": "#2a78d6", "gamma^(x8)": "#eb6834", "gamma^(x4)": "#1baf7a",
          "gamma^(x8) gamma^(x4)": "#4a3aa7"}
labels = {"1": r"$h$ (products of exponentials)",
          "gamma^(x8)": r"$h\gamma^{(x8)}$",
          "gamma^(x4)": r"$h\gamma^{(x4)}$",
          "gamma^(x8) gamma^(x4)": r"$h\gamma^{(x8)}\gamma^{(x4)}$"}
fig, ax = plt.subplots(figsize=(7.4, 6.6))
ax.axvspan(-1.0, 1.0, color="#d8d6d2", alpha=0.6, linewidth=0)
ax.axhspan(-1.0, 1.0, color="#d8d6d2", alpha=0.6, linewidth=0)
for name in WORDS:
    values = np.array(points[name])
    ax.plot(values[:, 0], values[:, 1], "o", color=colors[name], markersize=5,
            label=labels[name])
ax.set_xscale("symlog", linthresh=1.0)
ax.set_yscale("symlog", linthresh=1.0)
ax.set_xlim(-60, 60)
ax.set_ylim(-60, 60)
ax.text(0.0, 0.0, "forbidden band:\n$|\\det| < 1$", ha="center", va="center",
        fontsize=8)
ax.set_xlabel("$\\det A$ (space block)")
ax.set_ylabel("$\\det D$ (time block)")
ax.set_title("The four pieces of Pin(4,4)")
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=2)
save_figure(fig, "four_pieces", ...)
```

`axvspan` and `axhspan` shade the vertical and the horizontal band between $-1$ and $1$ in grey. The 240 points are drawn in four colours, one per word. `set_xscale("symlog", linthresh=1.0)` makes an axis **symmetric logarithmic**: linear between $-1$ and $1$ and logarithmic outside, so that values from 1 to 60 and the band are visible together. In `05f_3_four_pieces.png` each colour fills one of the four corners outside the band, and the products of exponentials (blue) never leave the corner where both determinants are at least 1.

**In [12], paths from 1.**

```python
path_t = np.linspace(0.0, 1.0, 101)  # t = 0, 0.01, ..., 1
curves_h, curves_g8 = [], []  # det A(t) along h(t) and along gamma^(x8) h(t)
g8 = gamma["x8"].astype(float)
for _ in range(10):
    factors = random_factors(6)
    along_h, along_g8 = [], []
    for t in path_t:
        h = compose(factors, t)
        along_h.append(np.linalg.det(blocks(vector_matrix(h))[0]))
        along_g8.append(np.linalg.det(blocks(vector_matrix(g8 @ h, odd=True))[0]))
    curves_h.append(along_h)
    curves_g8.append(along_g8)
curves_h, curves_g8 = np.array(curves_h), np.array(curves_g8)
check(np.all(curves_h > 1.0 - 1e-9) and np.all(curves_g8 < -1.0 + 1e-9)
      and np.allclose(curves_h[:, 0], 1.0) and np.allclose(curves_g8[:, 0], -1.0),
      "along ten paths t -> h(t) det A stays >= 1, and along gamma^(x8) h(t) it "
      "stays <= -1")
```

For ten random products of six exponentials the cell follows the path $h(t)$ of step (G) at 101 values of $t$ and records $\det A(t)$ (`blocks(...)[0]` is the space block), and the same for the odd elements $\gamma^{(x8)}h(t)$. The check: the first family starts at 1 and stays at or above 1, the second starts at $-1$ and stays at or below $-1$.

```python
fig, ax = plt.subplots(figsize=(8.0, 4.6))
ax.axhspan(-1.0, 1.0, color="#d8d6d2", alpha=0.6, linewidth=0)
for k in range(10):
    ax.plot(path_t, curves_h[k], color="#2a78d6", linewidth=1.5,
            label=r"$h(t)$" if k == 0 else None)
    ax.plot(path_t, curves_g8[k], color="#eb6834", linewidth=1.5, linestyle="--",
            label=r"$\gamma^{(x8)}h(t)$" if k == 0 else None)
ax.set_yscale("symlog", linthresh=1.0)
ax.set_ylim(-60, 60)
ax.text(0.5, 0.0, "forbidden band $|\\det A| < 1$", ha="center", va="center")
ax.set_xlabel("path parameter $t$ (from 1 at $t = 0$ to $h$ at $t = 1$)")
ax.set_ylabel("$\\det A$ (space block)")
ax.set_title("Ten paths of products of exponentials, and the same times "
             "$\\gamma^{(x8)}$")
ax.legend(loc="upper left")
save_figure(fig, "paths_and_band", ...)
```

The twenty curves are drawn over the grey band (only the first curve of each family gets a legend label; `None` means no label). In `05f_4_paths_and_band.png` the blue curves start at 1 and stay above the band, the orange ones start at $-1$ and stay below it: no curve crosses the band, which is why $\gamma^{(x8)}$ cannot be reached from 1 by exponentials.

**In [13], every unit vector is a turned basic one.**

```python
def turn_factor(a, b, along_a, along_b):
    if ETA[a] * ETA[b] == 1:  # a rotation
        return (a, b, float(np.arctan2(-ETA[a] * along_b, along_a)))
    return (a, b, float(np.arcsinh(-ETA[a] * along_b)))  # a boost
```

`turn_factor` returns the factor $(a, b, \theta)$ whose vector matrix carries $e_a$ to the direction of $\text{along}_a\,e_a + \text{along}_b\,e_b$. For a rotation, step (E) gives $\Lambda e_a = \cos\theta\,e_a - \eta_{aa}\sin\theta\,e_b$; `np.arctan2(y, x)` is the angle $\theta$ of the point $(x, y)$ in the plane, so that $\cos\theta$ and $\sin\theta$ are $x$ and $y$ divided by the distance $\sqrt{x^2 + y^2}$. With $x = \text{along}_a$ and $y = -\eta_{aa}\text{along}_b$, the vector $\Lambda e_a$ points along $\text{along}_a\,e_a + \text{along}_b\,e_b$. For a boost, $\Lambda e_a = \cosh\theta\,e_a - \eta_{aa}\sinh\theta\,e_b$; with $\sinh\theta = -\eta_{aa}\text{along}_b$ (`np.arcsinh` is the inverse of sinh) and $\text{along}_a^2 - \text{along}_b^2 = 1$, $\cosh\theta = \sqrt{1 + \text{along}_b^2} = \text{along}_a$.

```python
def block_rotation(axis, others, n):
    factors = []
    for k, b in enumerate(others):
        if k < len(others) - 1:  # keep the length of the rest on the axis
            rest = np.sqrt(n[axis] ** 2 + sum(n[o] ** 2 for o in others[k + 1:]))
        else:  # the last rotation leaves exactly n_axis on the axis
            rest = n[axis]
        factors.append(turn_factor(axis, b, rest, n[b]))
    return factors
```

`block_rotation` returns three rotations in the planes (axis, first other), (axis, second other), (axis, third other) that carry $e_{\text{axis}}$ to the unit vector $n$ of its block (`n` is a dictionary from direction names to components). The first rotation puts the component $n_b$ on the first other direction and leaves on the axis the length of everything that is still to come, $\sqrt{n_{\text{axis}}^2 + n_{b_2}^2 + n_{b_3}^2}$; each later rotation acts only on what is left on the axis; the last one leaves exactly $n_{\text{axis}}$, which may be negative.

```python
def carry(v):
    part = {x: float(v[COORDS.index(x)]) for x in COORDS}
    sigma = np.sqrt(sum(part[x] ** 2 for x in SPACE))  # length of the space part
    tau = np.sqrt(sum(part[x] ** 2 for x in TIME))  # length of the time part
    space_turn = block_rotation("x8", ["x1", "x2", "x3"],
                                {x: part[x] / sigma for x in SPACE}) if sigma else []
    time_turn = block_rotation("x4", ["x5", "x6", "x7"],
                               {x: part[x] / tau for x in TIME}) if tau else []
    if metric_product(v, v) > 0:  # space-like: from e_x8
        return [turn_factor("x8", "x4", sigma, tau)] + time_turn + space_turn, "x8"
    return [turn_factor("x4", "x8", tau, sigma)] + space_turn + time_turn, "x4"
```

`carry(v)` is the construction of step (I). `part` holds the eight components by name; `sigma` and `tau` are the lengths $|\sigma|$ and $|\tau|$ of the space part and the time part. `space_turn` turns $e_{x8}$ into $\sigma/|\sigma|$ and `time_turn` turns $e_{x4}$ into $\tau/|\tau|$ (an empty list when that part is zero; `if sigma else []` uses that the number 0 counts as false). For a space-like $v$ the factors are the boost in $(x8, x4)$, then the time rotations, then the space rotations, and the starting direction is $x8$; for a time-like $v$ the boost in $(x4, x8)$, then the space rotations, then the time rotations, starting from $x4$. The function returns the list of factors (the first acts first) together with the starting direction.

```python
def random_unit_vector():
    while True:
        w = rng.normal(size=8)  # eight numbers from the normal distribution
        q = metric_product(w, w)
        if abs(q) >= 0.5:
            return w / np.sqrt(abs(q))
```

A random unit vector: eight numbers are drawn from the normal distribution (the bell curve centred at 0), and the vector is kept only when $|\eta(w, w)| \geq 0.5$ (so that it is not nearly null); `while True` repeats until that happens. Dividing by $\sqrt{|\eta(w, w)|}$ makes $\eta = +1$ or $-1$.

```python
starts = {"x8": 0, "x4": 0}  # how many space-like and time-like vectors
carry_ok, most_factors = True, 0
for _ in range(40):
    v = random_unit_vector()
    factors, e = carry(v)
    starts[e] += 1
    most_factors = max(most_factors, len(factors))
    h = compose(factors)
    carry_ok &= (np.allclose(vector_matrix(h)[:, COORDS.index(e)], v, atol=1e-12)
                 and np.allclose(h @ gamma[e] @ np.linalg.inv(h), gamma_of(v),
                                 atol=1e-12))
say(f"space-like vectors: {starts['x8']}; time-like vectors: {starts['x4']}; "
    f"at most {most_factors} exponentials per vector")
check(carry_ok and starts["x8"] > 0 and starts["x4"] > 0 and most_factors <= 7,
      "for 40 random unit vectors v: gamma(v) = h gamma^(e) h^-1 with h a product "
      "of at most 7 exponentials and e = x8 or x4")
```

For 40 random unit vectors the cell builds $h$, checks that column $e$ of its vector matrix is $v$ and that $h\gamma^eh^{-1} = \gamma(v)$ as $16 \times 16$ matrices, and counts the space-like and time-like vectors and the largest number of factors. The printed line shows 20 and 20 and at most 7.

**In [14], the construction at work.**

```python
examples = [random_unit_vector() for _ in range(6)]
space_example = next(v for v in examples if metric_product(v, v) > 0)
time_example = next(v for v in examples if metric_product(v, v) < 0)
line_colors = ["#2a78d6", "#eb6834", "#1baf7a", "#4a3aa7", "#e34948", "#eda100",
               "#52514e", "#9e9c98"]
fig, axes = plt.subplots(1, 2, figsize=(12.0, 4.6), sharey=True)
steps_ok = True
```

Six more random unit vectors are drawn; `next(...)` takes the first space-like and the first time-like one among them. Eight colours, one per direction, and two pictures that share the vertical axis (`sharey=True`).

```python
for ax, v in zip(axes, [space_example, time_example]):
    factors, e = carry(v)
    moving = [E8[COORDS.index(e)]]  # the vector after 0, 1, ..., 7 steps
    for a, b, theta in factors:
        moving.append(vector_matrix(exponential(a, b, theta)) @ moving[-1])
    moving = np.array(moving)
    steps_ok &= np.allclose([metric_product(m, m) for m in moving], ETA[e])
    steps_ok &= np.allclose(moving[-1], v, atol=1e-12)
    if e == "x8":
        for a, b, theta in factors:
            say(f"    factor exp(theta S^({a} {b})), theta = {theta:+.4f}")
```

For each example the moving vector starts at $e_{x8}$ or $e_{x4}$, and each factor's vector matrix is applied to the latest vector (`moving[-1]` is the last element of the list). The cell checks that the metric product stays $\eta_{ee}$ at every step and that the last vector is $v$, and for the space-like example it prints the seven factors with their angles to four decimals.

```python
    for i, x in enumerate(COORDS):
        ax.plot(range(len(moving)), moving[:, i], "o-", color=line_colors[i],
                linewidth=1.5, markersize=4, label=x)
        ax.plot([len(moving) - 0.6], [v[i]], "D", color=line_colors[i],
                markersize=6)
    kind = "space-like" if e == "x8" else "time-like"
    ax.set_title(f"a {kind} unit vector, built from $e_{{{e}}}$")
    ax.set_xticks(range(len(moving)))
    ax.set_xlabel("number of exponentials applied")
axes[0].set_ylabel("component of the moving vector")
axes[1].legend(loc="upper center", bbox_to_anchor=(-0.05, -0.15), ncol=8)
check(steps_ok, "in both examples the moving vector keeps eta(w, w) and ends at v")
save_figure(fig, "carrying_vectors", ...)
```

Still inside the loop, each of the eight components is drawn against the number of steps, and the target component of $v$ as a diamond (`"D"`) just right of the last step. In `05f_5_carrying_vectors.png` the first step shares the length between $x8$ and $x4$ (a boost), the next three steps fill one block and the last three the other, and every curve ends at its diamond.

**In [15], moving a gamma through an exponential.**

```python
def conjugation_sign(e, a, b):
    return -1 if e in (a, b) else 1


conjugation_ok = all(
    np.allclose(gamma[e] @ exponential(a, b, 0.8) @ np.linalg.inv(gamma[e]),
                exponential(a, b, conjugation_sign(e, a, b) * 0.8), atol=1e-12)
    for e in ("x8", "x4") for a, b in pairs)
check(conjugation_ok, "gamma^e exp(theta S^ab) (gamma^e)^-1 = exp(s theta S^ab), "
      "s = -1 if e is a or b, +1 otherwise")
```

`conjugation_sign` is the sign $s$ of step (J). The check confirms $\gamma^e\exp(\theta S^{ab})(\gamma^e)^{-1} = \exp(s\theta S^{ab})$ for $e = x8$ and $x4$, all 28 planes and $\theta = 0.8$.

**In [16], twelve random elements of Pin(4,4).**

```python
FOUR = {"1": I16, "gamma^(x8)": gamma["x8"], "gamma^(x4)": gamma["x4"],
        "gamma^(x8) gamma^(x4)": gamma["x8"] @ gamma["x4"]}


def evaluate(word):
    g = np.eye(16)
    for item in word:
        if item[0] == "exp":
            g = g @ exponential(*item[1:])
        else:
            g = g @ gamma[item[1]]
    return g
```

A **word** is a list of items in the order of the matrix product: an exponential `("exp", a, b, theta)` or a gamma `("gamma", e)`. `evaluate` multiplies the items from left to right (`item[1:]` is the item without its first entry, unpacked into the arguments of `exponential`). `FOUR` holds the four words as matrices.

```python
def word_of(v):
    factors, e = carry(v)
    h_word = [("exp", a, b, th) for a, b, th in reversed(factors)]  # E_n ... E_1
    h_inverse = [("exp", a, b, -th) for a, b, th in factors]  # E_1^-1 ... E_n^-1
    return h_word + [("gamma", e)] + h_inverse
```

`word_of(v)` writes $\gamma(v) = h\gamma^eh^{-1}$ as a word. Since the first factor acts first, $h = E_n\cdots E_1$, which is the list of factors reversed; $h^{-1} = E_1^{-1}\cdots E_n^{-1}$, each with the opposite angle.

```python
def move_gammas_right(word):
    exponentials, waiting = [], []  # waiting: the gammas moved to the right so far
    for item in word:
        if item[0] == "gamma":
            waiting.append(item[1])
        else:  # this exponential is moved to the left of all waiting gammas
            _, a, b, theta = item
            s = 1
            for e in waiting:
                s *= conjugation_sign(e, a, b)
            exponentials.append(("exp", a, b, s * theta))
    return exponentials, waiting
```

`move_gammas_right` reads the word from left to right. A gamma is put on the list `waiting`. An exponential that comes after waiting gammas is moved to their left; by step (J) each gamma it passes multiplies its angle by the sign $s$ of that gamma. The result is the list of exponentials followed by the list of gammas, which as a word equals the original word.

```python
def reduce_gammas(waiting):
    product = I16
    for e in waiting:
        product = product @ gamma[e]
    for name, w in FOUR.items():
        if np.array_equal(product, w):
            return 1, name
        if np.array_equal(product, -w):
            return -1, name
    raise ValueError("the product of the gammas is not one of the four words")
```

`reduce_gammas` multiplies the waiting gammas and finds which of the four words it equals, with which sign; if it were none of them (impossible by step (J)), the notebook would stop with an error.

```python
decomposition_ok = True
for number in range(12):
    k = 1 + number % 6  # the number of unit vectors
    vectors = [random_unit_vector() for _ in range(k)]
    g = np.eye(16)
    word = []
    for v in vectors:
        g = g @ gamma_of(v)
        word += word_of(v)
    size = np.max(np.abs(g))  # for relative differences
    exponentials, waiting = move_gammas_right(word)
    sign, name = reduce_gammas(waiting)
    if sign == -1:  # -1 = exp(2 pi S^(x1 x2))
        exponentials.append(("exp", "x1", "x2", 2 * np.pi))
    rebuilt = evaluate(exponentials) @ FOUR[name]
```

Twelve elements are made from $k = 1, \dots, 6$ random unit vectors (twice each; `number % 6` is the remainder of the number divided by 6). For each, the product $g$ and its word are built, the gammas are moved to the right and reduced, a sign $-1$ is replaced by the exponential $\exp(2\pi S^{(x1)(x2)}) = -1$, and the decomposition is multiplied out again as `rebuilt`.

```python
    same_pattern = (pattern(vector_matrix(g, odd=k % 2 == 1))
                    == pattern(vector_matrix(FOUR[name].astype(float), WORDS[name][1])))
    decomposition_ok &= (np.max(np.abs(evaluate(word) - g)) < 1e-9 * size
                         and np.max(np.abs(rebuilt - g)) < 1e-9 * size
                         and same_pattern and WORDS[name][1] == (k % 2 == 1))
    plural = "s" if k > 1 else " "  # "1 unit vector", "2 unit vectors"
    say(f"element {number + 1:2d}: {k} unit vector{plural} = {len(exponentials):2d} "
        f"exponentials times {name}")
check(decomposition_ok, "12 random elements of Pin(4,4): each is a product of "
      "exponentials times one of 1, gamma^(x8), gamma^(x4), gamma^(x8) gamma^(x4), "
      "with the matching sign pattern")
```

The checks for each element: the word equals $g$, the decomposition equals $g$ (both to a relative accuracy of $10^{-9}$, measured against the largest entry `size` of $g$, because the entries of $g$ can be large), $g$ has the sign pattern of its word, and the word is odd exactly when $k$ is odd. The twelve printed lines show, for example, that one unit vector becomes 14 exponentials times $\gamma^{(x8)}$ (seven for $h$ and seven for $h^{-1}$), and that the elements made of four or six vectors can end with any of the even words.

**In [17], the spans.**

```python
formula_ok = all(
    np.allclose(exponential(a, b, np.pi), gamma[a] @ gamma[b], atol=1e-12)
    if ETA[a] * ETA[b] == 1 else
    np.allclose((exponential(a, b, 0.8) - exponential(a, b, -0.8))
                / (2 * np.sinh(0.4)), gamma[a] @ gamma[b], atol=1e-12)
    for a, b in pairs)
check(formula_ok, "exp(pi S^ab) = gamma^a gamma^b for the rotations and "
      "(exp(theta S^ab) - exp(-theta S^ab)) / (2 sinh(theta/2)) = gamma^a gamma^b "
      "for the boosts")
```

The two formulas of the last paragraph of Section 5.23 are checked for all 28 planes (for the boosts with $\theta = 0.8$, so that $2\sinh\tfrac\theta2 = 2\sinh 0.4$).

```python
spin0_elements = [compose(random_factors(6)) for _ in range(170)]
four_words = list(FOUR.values())
pin_elements = [compose(random_factors(6)) @ four_words[k % 4] for k in range(300)]


def rank_curve(elements):
    ranks = []
    for n in range(1, len(elements) + 1):
        rows = np.array([g.reshape(256) for g in elements[:n]])
        singular = np.linalg.svd(rows, compute_uv=False)
        ranks.append(int(np.sum(singular > 1e-9 * singular[0])))
    return ranks
```

170 random products of six exponentials, and 300 random elements of all four pieces (`k % 4` runs through the four words). `rank_curve` computes, for $n = 1, 2, \dots$, the rank of the first $n$ elements written as rows. It uses the **singular values** of the array of rows (`np.linalg.svd(..., compute_uv=False)`): the square roots of the eigenvalues of $A^TA$ for the array $A$, sorted from the largest. By the argument of Section 5.13 the number of nonzero ones is the rank; here a singular value counts as nonzero when it is above $10^{-9}$ times the largest.

```python
ranks_spin0, ranks_pin = rank_curve(spin0_elements), rank_curve(pin_elements)
block_diagonal = all(not g[:8, 8:].any() and not g[8:, :8].any()
                     for g in spin0_elements)
report("rank of 170 products of exponentials", ranks_spin0[-1])
report("rank of 300 elements of Pin(4,4)", ranks_pin[-1])
check_reproduces(ranks_spin0 == [min(n, 128) for n in range(1, 171)]
                 and block_diagonal
                 and recorded("python", "even_products_span_M8_plus_M8"),
                 "the products of exponentials are block diagonal and span 128 "
                 "dimensions, as the 128 even Clifford products",
                 record=record_of("python", "even_products_span_M8_plus_M8"))
check_reproduces(ranks_pin == [min(n, 256) for n in range(1, 301)]
                 and recorded("python", "clifford_products_span_M16"),
                 "the elements of Pin(4,4) span all 256 dimensions of the 16 x 16 "
                 "matrices",
                 record=record_of("python", "clifford_products_span_M16"))
```

The two RESULT lines print the final ranks, 128 and 256. The checks require that each new element raised the rank by one until it stopped at 128 (for the products of exponentials, which are also all block diagonal) and at 256 (for Pin(4,4)): the numbers that the record found for the even and for all products of different gammas.

**In [18], the picture of the spans.**

```python
fig, ax = plt.subplots(figsize=(8.0, 4.6))
ax.plot(range(1, 171), ranks_spin0, color="#2a78d6", linewidth=2.5,
        label=r"products of exponentials ($\mathrm{Spin}_0(4,4)$)")
ax.plot(range(1, 301), ranks_pin, color="#eb6834", linewidth=2, linestyle="--",
        label="elements of Pin(4,4) (all four pieces)")
ax.axhline(128, color="#2a78d6", linewidth=0.8, linestyle=":")
ax.axhline(256, color="#eb6834", linewidth=0.8, linestyle=":")
ax.set_xlabel("number $n$ of random group elements")
ax.set_ylabel("rank of the first $n$ elements")
ax.set_yticks([0, 64, 128, 192, 256])
ax.set_title("The span of the group elements")
ax.legend(loc="lower right")
save_figure(fig, "span_ranks", ...)
```

The two rank curves and dotted lines at 128 and 256. In `05f_6_span_ranks.png` both curves rise along the diagonal and then stop flat, the solid one at 128 and the dashed one at 256.

**In [19], the last check.**

```python
FIGURES = ["05f_1_generator_matrices.png", "05f_2_two_unit_vectors.png",
           "05f_3_four_pieces.png", "05f_4_paths_and_band.png",
           "05f_5_carrying_vectors.png", "05f_6_span_ranks.png"]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in FIGURES),
      "the six figure files of notebook 05f exist")
all_checks_passed()
```

The last line reads ALL 24 CHECKS PASSED (notebook 05f): one each in In [2] and In [3], three in In [4], one in In [5], two in In [6], one in In [7], two in In [8], one in In [9], three in In [10], one each in In [12] to In [16], three in In [17] and one in In [19]. Six of them reproduce recorded checks (In [2], In [3], the first and the third of In [4], and the last two of In [17]); the other eighteen are the notebook's own computations.

### 5.28 Charge conjugation is a matrix

**The question.** Every known particle has an **antiparticle** with the same mass and the opposite charge; the positron is the antiparticle of the electron. In a field theory the step from a solution to its antiparticle solution is made by a map called **charge conjugation**: it turns every solution of the field equation into another solution whose charge density has the opposite sign. In the usual four-dimensional Dirac theory this map contains a complex conjugation of the components together with a fixed matrix. In the author's theory one fact changes the picture: the eight gammas are real (Section 5.2). Take a **real** field, one whose 16 components are real numbers at every point, so that $\Psi^\ast = \Psi$. On such a field the complex conjugation $\Psi \to \Psi^\ast$ changes nothing at all: it is the identity map. A map that changes nothing cannot exchange matter and antimatter. So whatever charge conjugation is in this theory, it must be made by a **matrix**, and this section finds every matrix that can do the job. The answer (Theorem CC below) is: exactly two, up to a factor, $\mathcal{C}_+ = C$ and $\mathcal{C}_- = \Gamma C$. The Revision record that this section follows is the lead check `Revision/lead_checks/charge_conjugation_and_u1.py` with its report `Revision/lead_checks/reports/charge-conjugation-and-u1.json` (12 of 12 checks passed); Notebook 05c reproduces ten of its checks.

**The field equation.** Chapter 7 derives, from the Lagrangian of the Revision record, the field equation of both fields of the author,

$$
\gamma^\mu D_\mu\Psi = V\Psi, \qquad V = m + U'(S) .
$$

Here the index $\mu$ runs over the eight coordinates and a repeated index is summed (the **sum convention** of Chapter 1); $\gamma^\mu = e^\mu{}_a\gamma^a$ are the gammas of the curved space, made from the constant gammas $\gamma^a$ with the **vielbein** $e^\mu{}_a$, a set of real factors that Chapter 6 computes from the author's metric; $D_\mu = \partial_\mu + \Omega_\mu$ is the **covariant derivative**, the partial derivative $\partial_\mu$ along the coordinate $\mu$ plus a $16 \times 16$ matrix $\Omega_\mu$, the **spin connection**, which is a combination of the generators $S^{ab}$ with real coefficients (Chapter 6); $m$ is the mass; $U(S)$ is the self-interaction, a function of the scalar $S = \bar\Psi\Psi$, with derivative $U'(S)$; for the record's choice $U = \tfrac\lambda2S^2$ one has $V = m + \lambda S$. Only one property of this equation is needed now: **every matrix in it is real.** The gammas are real (Section 5.2), the vielbein factors are real, the number $V$ is real, and the Revision record checks that every entry of every $\Omega_\mu$ is a real expression (check `spinor_connection_real` of the lead report).

**Definition.** A **charge-conjugation matrix** is a constant $16 \times 16$ matrix $\mathcal{C}$ such that, whenever $\Psi$ solves the field equation, the column

$$
\Psi^c = \mathcal{C}\,\bar\Psi^T
$$

solves the field equation of the same form, either with the same $V$ (**same mass**) or with $-V$ (**mass reversed**). Here $\bar\Psi = \Psi^\dagger C$ is the Dirac adjoint of Section 5.4, a row, and $\bar\Psi^T$ is that row turned into a column.

**From the definition to an equation for a matrix, line by line.** First the column $\bar\Psi^T$:

$$
\bar\Psi^T = (\Psi^\dagger C)^T = C^T(\Psi^\dagger)^T = C\Psi^\ast .
$$

The first step is the definition of $\bar\Psi$; the second is the rule $(XY)^T = Y^TX^T$; the third uses that the transpose of the row $\Psi^\dagger$ is the column $\Psi^\ast$ of the conjugated components, and $C^T = C$ (property (C2) of Section 5.4). So $\Psi^c = \mathcal{C}C\Psi^\ast$. Write $M = \mathcal{C}C$; then $\Psi^c = M\Psi^\ast$, and since $CC = 1$ (C3), $\mathcal{C} = MC$.

- Step 1 (conjugate the equation). The complex conjugate of a product is the product of the complex conjugates, a real factor is its own conjugate, and the derivative of the conjugate is the conjugate of the derivative (the coordinates are real). So the conjugate of $\gamma^\mu D_\mu\Psi = V\Psi$ is $\gamma^\mu D_\mu\Psi^\ast = V\Psi^\ast$: **the column $\Psi^\ast$ solves the same equation.**
- Step 2 (multiply by a constant matrix). Multiply from the left by $M$: $M\gamma^\mu D_\mu\Psi^\ast = V\,M\Psi^\ast$; the number $V$ may stand on either side of $M$.
- Step 3 (the condition on $M$). Suppose that, with one sign $s$ ($+1$ or $-1$) for all eight directions,

$$
M\gamma^a = s\,\gamma^aM \qquad \text{for } a = x1, \dots, x8 .
$$

Then $M\gamma^\mu = \sum_a e^\mu{}_aM\gamma^a = s\,\gamma^\mu M$, because the vielbein factors are numbers. $M$ commutes with every product of two gammas: $M\gamma^a\gamma^b = s\,\gamma^aM\gamma^b = s^2\,\gamma^a\gamma^bM = \gamma^a\gamma^bM$ (the condition used twice, then $s^2 = 1$). The spin connection is a combination of the $S^{ab} = \tfrac12\gamma^a\gamma^b$, so $M\Omega_\mu = \Omega_\mu M$; and a constant matrix commutes with a derivative, $M\partial_\mu = \partial_\mu M$. Hence $MD_\mu = D_\mu M$.
- Step 4 (the new field). With Step 3, $M\gamma^\mu D_\mu\Psi^\ast = s\,\gamma^\mu MD_\mu\Psi^\ast = s\,\gamma^\mu D_\mu(M\Psi^\ast)$. So the equation of Step 2 reads $s\,\gamma^\mu D_\mu(M\Psi^\ast) = V\,(M\Psi^\ast)$. Multiplying by $s$ and using $s^2 = 1$:

$$
\gamma^\mu D_\mu(M\Psi^\ast) = s\,V\,(M\Psi^\ast) .
$$

**The new field $M\Psi^\ast$ solves the equation with $V$ when $s = +1$ and with $-V$ when $s = -1$.** Because the gammas are real, $(\gamma^a)^\ast = \gamma^a$, and the condition of Step 3 can be written $M(\gamma^a)^\ast = s\,\gamma^aM$; this is the form that the Revision record solves (it would also be the right form for complex gammas). One more remark about $V = m + \lambda S$, which depends on the field through $S$: Section 5.29 shows that for commuting components both matrices found below give a new field with the same $S$ as $\Psi$. Then $sV = s\,m + s\,\lambda S$, so the new field solves the field equation with the parameters $(m, \lambda)$ when $s = +1$ and $(-m, -\lambda)$ when $s = -1$. For a free field ($\lambda = 0$) only the mass matters. (For anticommuting components the table of Section 5.29 shows that the scalar changes its sign; this affects only the self-interaction term, and Section 5.34 treats the quantised field.)

**Theorem CC (the two charge-conjugation matrices).**

- (a) The solutions $M$ of $M(\gamma^a)^\ast = +\gamma^aM$ for all $a$ are the multiples of $1$; the solutions of $M(\gamma^a)^\ast = -\gamma^aM$ for all $a$ are the multiples of $\Gamma$.
- (b) Hence there are exactly two charge-conjugation matrices, up to a factor: $\mathcal{C}_+ = C$ (same mass), with $\Psi^c = \mathcal{C}_+\bar\Psi^T = \Psi^\ast$, and $\mathcal{C}_- = \Gamma C$ (mass reversed), with $\Psi^c = \mathcal{C}_-\bar\Psi^T = \Gamma\Psi^\ast$.
- (c) They obey $\mathcal{C}_+^{-1}\gamma^a\mathcal{C}_+ = -(\gamma^a)^T$ and $\mathcal{C}_-^{-1}\gamma^a\mathcal{C}_- = +(\gamma^a)^T$ for every $a$; both are real and symmetric, and $\mathcal{C}_+\mathcal{C}_+ = \mathcal{C}_-\mathcal{C}_- = 1$.

*Proof of (a).* The gammas are real, so the condition reads $M\gamma^a = s\,\gamma^aM$. For $s = +1$, $M$ commutes with all eight gammas, and by Theorem P of Section 5.13 it is a multiple of $1$. For $s = -1$, $M$ anticommutes with every gamma. Then $\Gamma M$ commutes with every gamma:

$$
\gamma^a(\Gamma M) = -\Gamma\gamma^aM = -\Gamma(-M\gamma^a) = (\Gamma M)\gamma^a .
$$

The first step is (X2) of Section 5.5 ($\Gamma$ anticommutes with every gamma); the second is the condition, read as $\gamma^aM = -M\gamma^a$; the third collects the two signs. By Theorem P, $\Gamma M = \lambda 1$ for some number $\lambda$; multiplying from the left by $\Gamma$ and using $\Gamma\Gamma = 1$ (X1) gives $M = \lambda\Gamma$. Conversely, $1$ commutes with every gamma and $\Gamma$ anticommutes with every gamma (X2), so both are solutions. The two solution spaces are therefore one-dimensional, spanned by $1$ and by $\Gamma$.

*Proof of (b).* $\mathcal{C} = MC$ (above). $M = 1$ gives $\mathcal{C}_+ = C$ and $\Psi^c = 1\,\Psi^\ast = \Psi^\ast$; $M = \Gamma$ gives $\mathcal{C}_- = \Gamma C$ and $\Psi^c = \Gamma\Psi^\ast$.

*Proof of (c).* For $\mathcal{C}_+ = C$, with $C^{-1} = C$ (C3), $\mathcal{C}_+^{-1}\gamma^a\mathcal{C}_+ = C\gamma^aC = -(\gamma^a)^T$ by (C5). For $\mathcal{C}_-$, the inverse of a product is the product of the inverses in the reverse order, so $\mathcal{C}_-^{-1} = C^{-1}\Gamma^{-1} = C\Gamma$ by (C3) and (X1). Then

$$
\mathcal{C}_-^{-1}\gamma^a\mathcal{C}_- = C\Gamma\gamma^a\Gamma C = C(-\gamma^a\Gamma)\Gamma C = -C\gamma^aC = +(\gamma^a)^T .
$$

The second step is (X2), the third is $\Gamma\Gamma = 1$ (X1), the fourth is (C5). Both matrices are products of real matrices, hence real. Symmetry: $C^T = C$ is (C2); $(\Gamma C)^T = C^T\Gamma^T = C\Gamma = \Gamma C$ by $(XY)^T = Y^TX^T$, (C2), (X6) and (X5). Squares: $CC = 1$ is (C3); $\Gamma C\Gamma C = \Gamma\Gamma CC = 1$ by (X5), (X1) and (C3). $\square$

**The shape of $\mathcal{C}_-$.** $\Gamma = \mathrm{diag}(-1_8, 1_8)$ and $C = \mathrm{diag}(-\sigma, \sigma)$ (Sections 5.4 and 5.5), so $\Gamma C = \mathrm{diag}(\sigma, \sigma)$: multiplying by $\Gamma$ from the left reverses the sign of the rows 1 to 8 (the block rule of Section 5.5). The table of Section 5.6 lists $\Gamma C$ next to $C$.

**The same two matrices from the transposition rules.** Many books define a charge-conjugation matrix by the condition $\mathcal{C}^{-1}\gamma^a\mathcal{C} = \zeta(\gamma^a)^T$ with a sign $\zeta$, that is $\gamma^a\mathcal{C} = \zeta\,\mathcal{C}(\gamma^a)^T$. Solving this directly gives the same two matrices: the solutions $X$ of $\gamma^aX = \zeta X(\gamma^a)^T$ (all $a$) are the multiples of $C$ for $\zeta = -1$ and of $\Gamma C$ for $\zeta = +1$. Proof: (C5) with $C^{-1} = C$ says $(\gamma^a)^T = -C\gamma^aC$, so the equation reads $\gamma^aX = -\zeta XC\gamma^aC$; multiplying from the right by $C$ (and $CC = 1$) gives $\gamma^a(XC) = -\zeta(XC)\gamma^a$. By part (a), $XC = \lambda1$ when $-\zeta = +1$ and $XC = \lambda\Gamma$ when $-\zeta = -1$; multiplying from the right by $C$ gives $X = \lambda C$ or $X = \lambda\Gamma C$.

**What $\mathcal{C}_+$ does to a real field.** For every field $\mathcal{C}_+\bar\Psi^T$ is the column $\Psi^\ast$. For a complex field this column differs from $\Psi$; for a real field it is $\Psi$ itself. So the same-mass charge conjugation leaves every real field unchanged: a real field is its own $\mathcal{C}_+$ conjugate. Section 5.29 shows what this means for the charge, and which real map is not trivial.

**A worked example: the free field along the time.** Take flat space, no self-interaction, and a field that depends only on the time $x4$. The field equation keeps only the term with $\mu = x4$, and in flat space $\gamma^{(x4)}$ is the constant gamma of $x4$:

$$
\gamma^{(x4)}\frac{d\Psi}{dx4} = m\Psi .
$$

Multiplying from the left by $-\gamma^{(x4)}$ and using $\gamma^{(x4)}\gamma^{(x4)} = -1$ gives $d\Psi/dx4 = -m\gamma^{(x4)}\Psi$. For any constant column $\Psi_0$ the column

$$
\Psi(x4) = \cos(m\,x4)\,\Psi_0 - \sin(m\,x4)\,\gamma^{(x4)}\Psi_0
$$

solves it. Check, line by line: by the chain rule, $d\cos(m\,x4)/dx4 = -m\sin(m\,x4)$ and $d\sin(m\,x4)/dx4 = m\cos(m\,x4)$, so

$$
\frac{d\Psi}{dx4} = -m\sin(m\,x4)\,\Psi_0 - m\cos(m\,x4)\,\gamma^{(x4)}\Psi_0 ;
$$

multiplying from the left by $\gamma^{(x4)}$ and using $\gamma^{(x4)}\gamma^{(x4)} = -1$ in the second term,

$$
\gamma^{(x4)}\frac{d\Psi}{dx4} = -m\sin(m\,x4)\,\gamma^{(x4)}\Psi_0 + m\cos(m\,x4)\,\Psi_0 = m\Psi .
$$

Now the two conjugates. Since $\cos$, $\sin$ and $\gamma^{(x4)}$ are real,

$$
\Psi^\ast(x4) = \cos(m\,x4)\,\Psi_0^\ast - \sin(m\,x4)\,\gamma^{(x4)}\Psi_0^\ast :
$$

the same formula with the starting column $\Psi_0^\ast$, so $\Psi^\ast$ solves the equation with the **same mass** $m$. For the other, put $\Phi_0 = \Gamma\Psi_0^\ast$ and use $\Gamma\gamma^{(x4)} = -\gamma^{(x4)}\Gamma$ (X2):

$$
\Gamma\Psi^\ast(x4) = \cos(m\,x4)\,\Phi_0 + \sin(m\,x4)\,\gamma^{(x4)}\Phi_0 = \cos(-m\,x4)\,\Phi_0 - \sin(-m\,x4)\,\gamma^{(x4)}\Phi_0 ,
$$

where the last step uses $\cos(-y) = \cos y$ and $\sin(-y) = -\sin y$. This is the solution formula with $m$ replaced by $-m$: $\Gamma\Psi^\ast$ solves the equation with the **mass reversed**. Notebook 05c checks both statements exactly with sympy, for a general mass $m$, and numerically on 801 time points (figures 3 and 4 of the notebook).

| statement | status | where it is verified |
| --- | --- | --- |
| the gammas, $C$ and the $S^{ab}$ are real; $B$ is purely imaginary and Hermitian | PROVED | `Revision/lead_checks/reports/charge-conjugation-and-u1.json`, checks `representation_real` and `B_imaginary_hermitian`; Notebook 05c, In [2] |
| every entry of the spin connection $\Omega_\mu$ is real, so $\gamma^\mu D_\mu$ is a real operator | PROVED in the record | the same report, check `spinor_connection_real` |
| Theorem CC (a): the solutions of $M(\gamma^a)^\ast = \pm\gamma^aM$ are the multiples of $1$ and of $\Gamma$ | PROVED; the exact solution of the 2048 equations COMPUTED | the same report, checks `intertwiners_same_mass` and `intertwiners_reversed_mass`; Notebook 05c, In [3] and In [4] |
| Theorem CC (b), (c): $\mathcal{C}_+ = C$, $\mathcal{C}_- = \Gamma C$ and their transposition rules | PROVED | the same report, checks `charge_conjugation_matrix_plus` and `charge_conjugation_matrix_minus`; Notebook 05c, In [5] and In [7] |
| the transposition equations have only the solutions $C$ and $\Gamma C$ | PROVED; COMPUTED exactly | Notebook 05c, In [5] (its own computation) |
| the free solution: $\Psi$ and $\Psi^\ast$ solve with $m$, $\Gamma\Psi^\ast$ with $-m$ | PROVED; COMPUTED exactly (sympy) and numerically (residuals below $10^{-12}$) | Notebook 05c, In [8] and In [9] (its own computation) |

### 5.29 The bilinears, the reality conditions and real fields

**Anticommuting numbers.** The components of the field dirac16complex00 are ordinary (complex) numbers, which **commute**: $\Psi_r\Psi_c = \Psi_c\Psi_r$. The components of dirac16complex are **anticommuting** numbers, also called **Grassmann numbers** after the mathematician who introduced them: exchanging two of them in a product costs a sign, $\Psi_r\Psi_c = -\Psi_c\Psi_r$, and in particular $\Psi_r\Psi_r = -\Psi_r\Psi_r$, so $\Psi_r\Psi_r = 0$. Chapter 7 builds them from zero. Here only the exchange rule is used, and the conjugated components $\Psi_r^\ast$ are treated as further anticommuting numbers. Write $\epsilon = +1$ for commuting and $\epsilon = -1$ for anticommuting components: exchanging two components costs the factor $\epsilon$.

**How a bilinear changes, line by line.** For a fixed matrix $K$ the **bilinear** $\Psi^\dagger K\Psi = \sum_{r,c}\Psi_r^\ast K_{rc}\Psi_c$ is a single number. Replace $\Psi$ by $\Psi' = M\Psi^\ast$ with a real matrix $M$.

1. $(\Psi')^\dagger = (M\Psi^\ast)^\dagger = (\Psi^\ast)^\dagger M^\dagger = \Psi^TM^\dagger$, by the rule $(XY)^\dagger = Y^\dagger X^\dagger$ and because conjugating twice gives the number back. So $\Psi'^\dagger K\Psi' = \Psi^TM^\dagger KM\Psi^\ast = \sum_{r,c}\Psi_r\,(M^\dagger KM)_{rc}\,\Psi_c^\ast$.
2. Exchange the two factors $\Psi_r$ and $\Psi_c^\ast$; this costs the factor $\epsilon$: $\sum_{r,c}\epsilon\,\Psi_c^\ast\,(M^\dagger KM)_{rc}\,\Psi_r$.
3. Rename the summation letters, $r \leftrightarrow c$: $\sum_{r,c}\Psi_r^\ast\,\epsilon(M^\dagger KM)_{cr}\,\Psi_c = \Psi^\dagger K'\Psi$ with $K' = \epsilon\,(M^\dagger KM)^T$.

So **the bilinear with the matrix $K$ turns into the bilinear with the matrix $K' = \epsilon(M^\dagger KM)^T$.** If $K' = +K$ the bilinear is kept, if $K' = -K$ it is reversed.

**The signs of $S$ and $J$.** The scalar has $K = C$, the currents $K = -iC\gamma^a$ (Section 5.4). The two maps have $M = 1$ ($\mathcal{C}_+$) and $M = \Gamma$ ($\mathcal{C}_-$); both are real and symmetric, so $M^\dagger = M$.

- $\mathcal{C}_+$, scalar: $K' = \epsilon C^T = \epsilon C$ by (C2). So $S \to \epsilon S$.
- $\mathcal{C}_+$, currents: $(-iC\gamma^a)^T = -i(C\gamma^a)^T = -i(-C\gamma^a) = iC\gamma^a$ by (C4), so $K' = \epsilon\,iC\gamma^a = -\epsilon K$. So $J^a \to -\epsilon J^a$.
- $\mathcal{C}_-$, scalar: $\Gamma C\Gamma = \Gamma^TC\Gamma = C$ by (X6) and (X7), so $K' = \epsilon C^T = \epsilon C$. So $S \to \epsilon S$.
- $\mathcal{C}_-$, currents: $\Gamma(-iC\gamma^a)\Gamma = -i\,\Gamma^TC\gamma^a\Gamma = -i(-C\gamma^a) = iC\gamma^a$ by (X6) and (X8), and its transpose is $i(C\gamma^a)^T = -iC\gamma^a = K$ by (C4). So $K' = \epsilon K$ and $J^a \to \epsilon J^a$.

| map | components | $S$ becomes | every $J^a$ becomes |
| --- | --- | --- | --- |
| $\mathcal{C}_+$ ($M = 1$) | commuting ($\epsilon = +1$) | $+S$ | $-J^a$ |
| $\mathcal{C}_+$ ($M = 1$) | anticommuting ($\epsilon = -1$) | $-S$ | $+J^a$ |
| $\mathcal{C}_-$ ($M = \Gamma$) | commuting ($\epsilon = +1$) | $+S$ | $+J^a$ |
| $\mathcal{C}_-$ ($M = \Gamma$) | anticommuting ($\epsilon = -1$) | $-S$ | $-J^a$ |

This is the table that the Revision record measured (check `bilinears_under_charge_conjugation`, the part of its detail text after the word measured); Notebook 05c reproduces it exactly. For the anticommuting rows the table is a statement about classical Grassmann components. For the quantised field the question is decided by an operator computation, which Section 5.34 carries out: after normal ordering the quantised field has exactly the signs of the anticommuting rows. (The detail text of the record's check also contains, in parentheses, the remark that normal ordering supplies one more sign for each bilinear; that remark is not part of the measured table, and the computation of Section 5.34 and Notebook 05e does not support it. This is listed as an open point for the owner of the record in Section 5.40.)

**What the table means for the commuting field.** For dirac16complex00, whose components are commuting complex numbers, $\mathcal{C}_+$ keeps the mass and the scalar and reverses every current, in particular the charge density $J^{(x4)} = \Psi^\dagger B\Psi$. So it turns every solution of charge $Q$ into a solution of the same mass and charge $-Q$: it is the antiparticle map of this field. $\mathcal{C}_-$ reverses the mass and keeps the charge. Notebook 05c shows this on the free solution of Section 5.28 with a fixed complex column $\Psi_0$: the solution has $S = -2$ and $J^{(x4)} = -6$ at every time; $\Psi^\ast$ has $S = -2$ and $J^{(x4)} = +6$; $\Gamma\Psi^\ast$ has $S = -2$ and $J^{(x4)} = -6$ (figure 5 of the notebook).

**The reality (Majorana) conditions.** A field equal to its own conjugate obeys $\Psi = M\Psi^\ast$; such a requirement is called a **Majorana** or **reality condition**, after the physicist who first used one. Is it a sensible requirement? Take the complex conjugate of the condition, $\Psi^\ast = M^\ast\Psi$, and put it back into the condition: $\Psi = MM^\ast\Psi$. If $MM^\ast = 1$ this is automatically true, and the condition is called **consistent**; otherwise it forces further conditions on $\Psi$ (possibly $\Psi = 0$). For $M = 1$, $MM^\ast = 1$: the condition $\Psi = \Psi^\ast$ says that the field is real. For $M = \Gamma$, $\Gamma\Gamma^\ast = \Gamma\Gamma = 1$: the condition $\Psi = \Gamma\Psi^\ast$ says, component by component, $\Psi_r = -\Psi_r^\ast$ for $r = 1, \dots, 8$ (where $\Gamma = -1$), so these components are purely imaginary, and $\Psi_r = \Psi_r^\ast$ for $r = 9, \dots, 16$, which are real. Both conditions are consistent (record check `majorana_conditions_consistent`).

**Do they survive the time evolution?** Consistency is a statement about one moment. For the free solution of Section 5.28: if $\Psi_0$ is real, every factor of the solution is real and the field stays real for ever. If instead $\Psi_0 = \Gamma\Psi_0^\ast$, then, using $\Gamma\gamma^{(x4)} = -\gamma^{(x4)}\Gamma$ (X2) and $\Gamma\Psi_0^\ast = \Psi_0$,

$$
\Gamma\Psi(x4)^\ast = \cos(m\,x4)\,\Gamma\Psi_0^\ast - \sin(m\,x4)\,\Gamma\gamma^{(x4)}\Psi_0^\ast = \cos(m\,x4)\,\Psi_0 + \sin(m\,x4)\,\gamma^{(x4)}\Psi_0 ,
$$

and subtracting this from $\Psi(x4)$:

$$
\Psi(x4) - \Gamma\Psi(x4)^\ast = -2\sin(m\,x4)\,\gamma^{(x4)}\Psi_0 .
$$

Its length is $2|\sin(m\,x4)|$ times the length of $\Psi_0$, because $\gamma^{(x4)}$ is a signed permutation matrix and keeps lengths. So the condition $\Psi = \Gamma\Psi^\ast$ holds at all times only for $m = 0$. This is what "mass reversed" means: a field equal to its own $\mathcal{C}_-$ image would have to solve the equation with $V$ and with $-V$ at the same time (figure 7 of Notebook 05c).

**Real fields.** For a real field with commuting components, three facts hold.

- (F1) **The currents vanish.** $J^a = \Psi^\dagger(-iC\gamma^a)\Psi = -i\,\Psi^TA\Psi$ with $A = C\gamma^a$, which is antisymmetric by (C4). For every real column $u$ and every antisymmetric $A$, $u^TAu = 0$: the number $u^TAu$ equals its own transpose, $u^TAu = (u^TAu)^T = u^TA^Tu = -u^TAu$ (the rule $(XYZ)^T = Z^TY^TX^T$, then $A^T = -A$), and a number equal to minus itself is 0. So a real commuting field carries no current and no charge.
- (F2) **$\mathcal{C}_+$ acts as the identity.** $\Psi^c = \Psi^\ast = \Psi$: a real field is its own same-mass conjugate.
- (F3) **The real matrix $\Gamma$ reverses the mass.** The map $\Psi \to \Gamma\Psi$ (no conjugation) takes real fields to real fields. It keeps the scalar, $(\Gamma\Psi)^TC(\Gamma\Psi) = \Psi^T\Gamma^TC\Gamma\Psi = \Psi^TC\Psi$ by (X7), and it reverses every kinetic matrix, $\Gamma^TC\gamma^a\Gamma = -C\gamma^a$ by (X8). In the field equation: $\Gamma$ commutes with $\Omega_\mu$ (an even matrix, (X3)) and with $\partial_\mu$, so $\Gamma D_\mu = D_\mu\Gamma$, and $\Gamma$ anticommutes with every $\gamma^\mu$; hence $\gamma^\mu D_\mu(\Gamma\Psi) = -\Gamma\gamma^\mu D_\mu\Psi = -V\,(\Gamma\Psi)$. With $S(\Gamma\Psi) = S(\Psi)$ and $V = m + \lambda S$, the field $\Gamma\Psi$ solves the field equation with $(m, \lambda) \to (-m, -\lambda)$. This is the pairing theorem T1 of the Revision record, which Chapter 18 proves for the Lagrangian; the same calculation holds for complex fields, where $\Gamma$ also reverses every current.

By Theorem CC, every real matrix that maps real solutions to solutions with $\pm V$ is a multiple of $1$ or of $\Gamma$. So for real fields the only nontrivial matrix map is $\Gamma$, and it reverses the mass. The Revision record states this as: for real fields the matter–antimatter map is the matrix $\Gamma$ together with $m \to -m$ (check `real_fields_charge_conjugation`). A real commuting field has no charge to reverse (F1); what the map exchanges is the sign of the mass.

| statement | status | where it is verified |
| --- | --- | --- |
| the bilinear rule $K' = \epsilon(M^\dagger KM)^T$ and the sign table of $S$ and $J$ | PROVED; COMPUTED exactly | `Revision/lead_checks/reports/charge-conjugation-and-u1.json`, check `bilinears_under_charge_conjugation` (its measured table); Notebook 05c, In [14] |
| on the free solution: $S = -2$ for all three fields, $J^{(x4)} = -6$, $+6$, $-6$ | COMPUTED (exact at $x4 = 0$; constant to $10^{-12}$) | Notebook 05c, In [12] (its own computation) |
| both reality conditions are consistent ($MM^\ast = 1$) | PROVED | the same report, check `majorana_conditions_consistent`; Notebook 05c, In [16] |
| the real condition is kept in time; $\Psi = \Gamma\Psi^\ast$ is violated by twice the size of $\sin(m\,x4)$ | PROVED; COMPUTED for $m = 1$, $0.5$, $0$ | Notebook 05c, In [17] (its own computation) |
| real fields: (F1), (F2), (F3) | PROVED | the same report, check `real_fields_charge_conjugation`; Notebook 05c, In [18] |
| the parenthetical remark of the record that normal ordering adds a sign | not supported (Section 5.34) | Notebook 05e, In [16] to In [18] |

### 5.30 Example: Notebook 05c computes the charge-conjugation matrices

Notebook 05c turns Sections 5.28 and 5.29 into exact computations on the author's gammas. It reads the gammas from `Revision/algebra/gammas.json` and the lead report `Revision/lead_checks/reports/charge-conjugation-and-u1.json`; it writes the conditions $M(\gamma^a)^\ast = \pm\gamma^aM$ as two systems of 2048 linear equations for the 256 entries of $M$ and solves them exactly, confirming the result with the zero eigenvalues of $A^TA$; it builds $\mathcal{C}_+$ and $\mathcal{C}_-$ and checks their transposition rules, and solves the transposition equations directly; it applies both maps to a complex column and to the free solution along $x4$, exactly with sympy and on 801 time points; it computes $S$ and $J^{(x4)}$ of the three fields and the full sign table for commuting and anticommuting components; it checks the reality conditions and follows them in time; it treats real fields; and it checks which conjugation keeps the anticommutator of the quantised field. Ten of its checks reproduce checks of the lead report. It draws nine figures and ends with the line ALL 20 CHECKS PASSED (notebook 05c).

<!-- NOTEBOOK 05c -->

### 5.33 Line-by-line walk-through of Notebook 05c

The notebook has 21 code cells. In [1] is the set-up cell of Section 5.10 with `NOTEBOOK_ID = "05c"`; its comments repeat the instructions of Section 5.31. As in the earlier walk-throughs, the docstrings of the functions (the texts in triple quotes below a `def` line) are left out of the quotations, and a long caption given to `save_figure` is shortened to `...`; the full caption is printed under the figure in the complete text of the notebook.

**In [2], the gammas, $C$, $\Gamma$, $B$ and the lead report.**

```python
import contextlib  # lets a block of code print into a text buffer
import io  # the text buffer io.StringIO
import sys  # sys.stdout: the channel through which the notebook prints

import numpy as np  # arrays of numbers, matrices and linear algebra
```

The modules `contextlib`, `io` and `sys` serve the helper `check_reproduces` below; numpy is loaded under its short name `np`.

```python
fixture = json.loads(repository_file("Revision/algebra/gammas.json")
                     .read_text(encoding="utf-8"))
COORDS = fixture["coordinates"]  # "x1", ..., "x8"
ETA = dict(zip(COORDS, fixture["eta"]))  # +1 space-like, -1 time-like
gamma = {x: np.array(m, dtype=np.int64) for x, m in zip(COORDS, fixture["gamma"])}
I16 = np.eye(16, dtype=np.int64)  # the identity matrix 1
```

These lines read the record of the gammas exactly as Notebook 05a does (Section 5.10, In [2]): `fixture` is the record, `COORDS` the eight coordinate names, `ETA` the signs $\eta_{aa}$, `gamma` the eight matrices as arrays of whole numbers (so that every product is exact) and `I16` the identity. A statement may run over two lines when the line break stands inside a bracket, as in the first line.

```python
def product(directions):
    result = I16
    for d in directions:
        result = result @ gamma[d]
    return result
```

`product(["x8", "x1"])` multiplies the gammas of the listed directions in the order of the list, starting from the identity; `@` is the matrix product.

```python
C = product(["x8", "x1", "x2", "x3"])  # the charge matrix (sigma16)
Gamma = product(["x8", "x1", "x2", "x3", "x4", "x5", "x6", "x7"])  # the chirality
B = -1j * (C @ gamma["x4"])  # B = -i C gamma^(x4)
pairs = [(a, b) for i, a in enumerate(COORDS) for b in COORDS[i + 1:]]
S_gen = {(a, b): (gamma[a] @ gamma[b] - gamma[b] @ gamma[a]) / 4 for a, b in pairs}
```

$C$, $\Gamma$ and $B = -iC\gamma^{(x4)}$ are built as in Sections 5.4 to 5.6 (`1j` is Python's imaginary unit $i$). `pairs` lists the 28 planes $(a, b)$ with $a$ before $b$ (`enumerate` gives each name with its position `i`, and `COORDS[i + 1:]` is the list of the names after it), and `S_gen` holds the 28 generators $S^{ab} = \tfrac14(\gamma^a\gamma^b - \gamma^b\gamma^a)$.

```python
RECORD = "Revision/lead_checks/reports/charge-conjugation-and-u1.json"
lead = json.loads(repository_file(RECORD).read_text(encoding="utf-8"))
LEAD = {c["name"]: (c["verdict"].lower(), c["detail"]) for c in lead["checks"]}
```

`RECORD` is the path of the lead report. `lead` is the whole report read as a dictionary; `lead["checks"]` is its list of checks, and the dictionary comprehension stores each check under its name as the pair (verdict in small letters, detail text).

```python
def recorded(name):
    return LEAD[name][0] == "pass"


def detail(name):
    return LEAD[name][1]


def check_reproduces(condition, name, record):
    collected = io.StringIO()
    with contextlib.redirect_stdout(collected):  # print into the buffer
        check(condition, name, record=record)  # stops here if the check fails
    sys.stdout.write(collected.getvalue())  # the PASS and reproduces lines together
```

`recorded(name)` is true when the lead report holds the check `name` with the verdict pass; `detail(name)` is its detail text (the second element `[1]` of the stored pair). `check_reproduces` is the helper of Notebook 05a (Section 5.10, In [3]): it lets `check` print the PASS line and the line that names the reproduced record into a text buffer and then sends both lines at once.

```python
passed, total = lead["summary"]["passed"], lead["summary"]["total"]
say(f"the lead report holds {len(LEAD)} checks; passed: {passed} of {total}")
is_real = all(not np.iscomplexobj(gamma[x]) for x in COORDS)
```

The first line reads the two numbers of the report's summary; the printed line says that the report holds 12 checks, all passed. `np.iscomplexobj` is true for an array of complex numbers; `is_real` is true when none of the eight gammas is complex.

```python
check_reproduces(is_real and np.array_equal(C.T, C) and np.array_equal(C @ C, I16)
                 and all(np.isrealobj(s) for s in S_gen.values())
                 and recorded("representation_real"),
                 "the gammas, C (symmetric, C C = 1) and the S^ab are real",
                 record=f"{RECORD}, check representation_real")
check_reproduces(not np.any(B.real) and np.array_equal(B.conj().T, B)
                 and np.array_equal(B @ B, I16) and recorded("B_imaginary_hermitian"),
                 "B = -i C gamma^(x4) is purely imaginary and Hermitian, B B = 1",
                 record=f"{RECORD}, check B_imaginary_hermitian")
```

The first check: the gammas are real, $C^T = C$, $CC = 1$, and every generator is real (`np.isrealobj`); this is the fact that makes plain complex conjugation do nothing on a real field. The second check: the real part of $B$ is zero everywhere (`not np.any(B.real)`), $B^\dagger = B$ (`B.conj().T` is the conjugate transpose) and $BB = 1$. Both print PASS and the lead check they reproduce.

**In [3], every conjugation matrix, solved exactly.**

```python
import sympy as sp  # exact algebra
from sympy.polys.matrices import DomainMatrix  # exact matrices over QQ


def conjugation_system(s):
    blocks = []
    for x in COORDS:
        G = np.conj(gamma[x]).astype(np.int64)  # (gamma^a)*, equal to gamma^a
        blocks.append(np.kron(I16, G.T) - s * np.kron(gamma[x], I16))
    return np.vstack(blocks)
```

`conjugation_system(s)` builds the coefficient matrix of the 2048 linear equations $M(\gamma^a)^\ast - s\,\gamma^aM = 0$, $a = x1, \dots, x8$, for the 256 entries of $M$ listed row by row. The rule of Section 5.13 for $LX - XR$ is used with the roles turned around: the entry $(r, c)$ of $MG$ is $\sum_kM_{rk}G_{kc}$, and the coefficient matrix of $M \to MG$ is $\mathrm{kron}(1, G^T)$; the entry $(r, c)$ of $GM$ is $\sum_kG_{rk}M_{kc}$, with the coefficient matrix $\mathrm{kron}(G, 1)$. `np.conj` writes out the complex conjugate although it equals the gamma (the gammas are real), so that the code says exactly what the equation says; `np.vstack` stacks the eight blocks of 256 rows.

```python
def exact_solutions(A, n=16):
    null = DomainMatrix.from_list(A.tolist(), sp.QQ).nullspace().to_Matrix()
    return [np.array(null.row(k).tolist()[0], dtype=float).reshape(n, n)
            for k in range(null.rows)]
```

`exact_solutions(A)` returns a basis of all solutions of $Ay = 0$, each turned back into a $16 \times 16$ matrix, as `solution_basis` of Notebook 05b does (Section 5.17, In [3]): sympy's `DomainMatrix` over the rational numbers `QQ` finds the solutions by exact elimination, `nullspace()` returns one solution per row, and `reshape(n, n)` restores the matrix (`n=16` is a **default value**: the argument may be left out).

```python
def proportional(X, Y):
    stacked = np.array([X.reshape(-1), Y.reshape(-1)], dtype=float)
    return bool(X.any() and Y.any() and np.linalg.matrix_rank(stacked) == 1)
```

`proportional(X, Y)` is true when both matrices are nonzero and one is a number times the other: written as two rows of 256 numbers (`reshape(-1)` lays out all entries in one row), they must have rank 1. `bool(...)` turns the result into a plain true or false.

```python
A_same, A_reversed = conjugation_system(+1), conjugation_system(-1)
M_same, M_reversed = exact_solutions(A_same), exact_solutions(A_reversed)
say(f"s = +1: {A_same.shape[0]} equations, {len(M_same)} independent solution(s)")
say(f"s = -1: {A_reversed.shape[0]} equations, {len(M_reversed)} independent "
    f"solution(s)")
```

The two systems are built and solved. The printed lines report, for each sign, 2048 equations and 1 independent solution.

```python
check_reproduces(len(M_same) == 1 and proportional(M_same[0], I16)
                 and "dimension 1" in detail("intertwiners_same_mass")
                 and recorded("intertwiners_same_mass"),
                 "M (gamma^a)* = + gamma^a M: one solution, the identity (same mass)",
                 record=f"{RECORD}, check intertwiners_same_mass")
check_reproduces(len(M_reversed) == 1 and proportional(M_reversed[0], Gamma)
                 and "dimension 1" in detail("intertwiners_reversed_mass")
                 and recorded("intertwiners_reversed_mass"),
                 "M (gamma^a)* = - gamma^a M: one solution, Gamma (mass reversed)",
                 record=f"{RECORD}, check intertwiners_reversed_mass")
```

Theorem CC (a) as two checks: for $s = +1$ exactly one solution, proportional to the identity; for $s = -1$ exactly one, proportional to $\Gamma$. Each also requires that the record's detail text contains the words `dimension 1`, the dimension the record found.

**In [4], the second engine and the picture of the solutions.**

```python
from matplotlib.colors import LinearSegmentedColormap

SIGNS = LinearSegmentedColormap.from_list("signs", ["#2a78d6", "#f0efec", "#e34948"])


def heat_map(ax, matrix, title, row_label=True):
    image = ax.imshow(matrix, cmap=SIGNS, vmin=-1, vmax=1)
    ax.set_title(title)
    ax.set_xticks([0, 3, 7, 11, 15], ["1", "4", "8", "12", "16"])
    ax.set_yticks([0, 3, 7, 11, 15], ["1", "4", "8", "12", "16"])
    ax.axhline(7.5, color="black", linewidth=0.8)
    ax.axvline(7.5, color="black", linewidth=0.8)
    ax.set_xlabel("column")
    if row_label:
        ax.set_ylabel("row")
    ax.grid(False)
    return image
```

The colour map (blue $-1$, light grey $0$, red $+1$) and the heat map of Notebook 05a (Section 5.10, In [6]), here always for a $16 \times 16$ matrix with the two black lines between the halves.

```python
eigen_same = np.linalg.eigvalsh((A_same.T @ A_same).astype(float))
eigen_reversed = np.linalg.eigvalsh((A_reversed.T @ A_reversed).astype(float))
zeros_same = int(np.sum(np.abs(eigen_same) < 1e-9))
zeros_reversed = int(np.sum(np.abs(eigen_reversed) < 1e-9))
say(f"zero eigenvalues of A^T A: s = +1: {zeros_same}; s = -1: {zeros_reversed}")
check(zeros_same == 1 and zeros_reversed == 1,
      "numerical second engine: exactly one zero eigenvalue for each sign")
```

The second engine of Section 5.13: the number of solutions of $Ay = 0$ equals the number of zero eigenvalues of the symmetric matrix $A^TA$. `np.linalg.eigvalsh` computes the 256 eigenvalues in floating-point numbers (sorted from small to large), and the eigenvalues below $10^{-9}$ in size are counted. The printed line shows one for each sign, and the check requires it.

```python
fig, axes = plt.subplots(1, 3, figsize=(13.0, 4.0), width_ratios=[1, 1, 1.3])
shown_same = M_same[0] / M_same[0][0, 0]  # scaled: entry (1,1) equal to 1
shown_reversed = M_reversed[0] / M_reversed[0][0, 0] * Gamma[0, 0]  # as in Gamma
heat_map(axes[0], shown_same, "solution for $s = +1$")
image = heat_map(axes[1], shown_reversed, "solution for $s = -1$", row_label=False)
```

A solution is fixed only up to a factor. The solution for $s = +1$ is divided by its entry in row 1, column 1, so that this entry becomes 1, like the identity's; the solution for $s = -1$ is scaled so that this entry equals the one of $\Gamma$, which is $-1$. Both are drawn as heat maps.

```python
index = np.arange(1, 257)
axes[2].plot(index, eigen_same, color="#2a78d6", linewidth=2,
             label="$s = +1$ (same mass)")
axes[2].plot(index, eigen_reversed, color="#eb6834", linewidth=2, linestyle="--",
             label="$s = -1$ (mass reversed)")
axes[2].plot([1], [eigen_same[0]], "o", color="#2a78d6", markersize=9)
axes[2].plot([1], [eigen_reversed[0]], "o", color="#eb6834", markersize=9)
axes[2].set_xlabel("number of the eigenvalue (sorted)")
axes[2].set_ylabel("eigenvalue of $A^T A$")
axes[2].set_title("one zero eigenvalue for each sign")
axes[2].legend(loc="lower right")
fig.colorbar(image, ax=axes[:2], ticks=[-1, 0, 1], shrink=0.8, label="matrix entry")
save_figure(fig, "solution_spaces", ...)
```

The third picture plots the sorted eigenvalues of the two systems against their numbers 1 to 256, and a large dot on the first (smallest) eigenvalue of each, which is the zero one. The colour bar belongs to the first two pictures (`axes[:2]`). **What figure 05c.1 shows**: on the left the identity (a red diagonal), in the middle $\Gamma$ (blue on the first eight diagonal places, red on the last eight), on the right two staircase curves of eigenvalues that each touch zero exactly once. The student should see that each equation system leaves exactly one free direction: the identity for the same mass, $\Gamma$ for the reversed mass.

**In [5], the two charge-conjugation matrices.**

```python
calC_plus = (M_same[0] / M_same[0][0, 0]) @ C  # M = 1 (scaled), so calC_+ = C
calC_minus = Gamma @ C  # M = Gamma, so calC_- = Gamma C
inverse_plus = np.linalg.inv(calC_plus)
inverse_minus = np.linalg.inv(calC_minus)
```

From $\mathcal{C} = MC$: the solution for $s = +1$, scaled to the identity, times $C$ gives $\mathcal{C}_+$; $\Gamma C$ is $\mathcal{C}_-$. `np.linalg.inv` computes the inverse matrices (for these signed permutation matrices the floating-point inverse is exact).

```python
check_reproduces(np.array_equal(calC_plus, C)
                 and all(np.array_equal(inverse_plus @ gamma[x] @ calC_plus, -gamma[x].T)
                         for x in COORDS)
                 and np.array_equal(calC_plus.T, calC_plus)
                 and recorded("charge_conjugation_matrix_plus"),
                 "calC_+ = C: calC_+^-1 gamma^a calC_+ = -(gamma^a)^T, real and "
                 "symmetric",
                 record=f"{RECORD}, check charge_conjugation_matrix_plus")
check_reproduces(all(np.array_equal(inverse_minus @ gamma[x] @ calC_minus, gamma[x].T)
                     for x in COORDS)
                 and np.isrealobj(calC_minus)
                 and np.array_equal(calC_minus.T, calC_minus)
                 and np.array_equal(calC_minus @ calC_minus, I16)
                 and recorded("charge_conjugation_matrix_minus"),
                 "calC_- = Gamma C: calC_-^-1 gamma^a calC_- = +(gamma^a)^T, real",
                 record=f"{RECORD}, check charge_conjugation_matrix_minus")
```

Theorem CC (b) and (c): $\mathcal{C}_+ = C$ with $\mathcal{C}_+^{-1}\gamma^a\mathcal{C}_+ = -(\gamma^a)^T$ for all eight directions, symmetric; $\mathcal{C}_-$ with $\mathcal{C}_-^{-1}\gamma^a\mathcal{C}_- = +(\gamma^a)^T$, real, symmetric and with square 1.

```python
def transposition_system(zeta):
    return np.vstack([np.kron(gamma[x], I16) - zeta * np.kron(I16, gamma[x])
                      for x in COORDS])


X_minus = exact_solutions(transposition_system(-1))  # should be multiples of C
X_plus = exact_solutions(transposition_system(+1))  # should be multiples of Gamma C
say(f"zeta = -1: {len(X_minus)} solution(s); zeta = +1: {len(X_plus)} solution(s)")
check(len(X_minus) == 1 and proportional(X_minus[0], C)
      and len(X_plus) == 1 and proportional(X_plus[0], Gamma @ C),
      "the only solutions of gamma^a X = -X (gamma^a)^T are multiples of C, of "
      "gamma^a X = +X (gamma^a)^T multiples of Gamma C")
```

The independent derivation of Section 5.28 ("the same two matrices from the transposition rules"). For $\gamma^aX - \zeta X(\gamma^a)^T = 0$ the coefficient matrix is $\mathrm{kron}(\gamma^a, 1) - \zeta\,\mathrm{kron}(1, ((\gamma^a)^T)^T)$, and $((\gamma^a)^T)^T = \gamma^a$, which is why the second Kronecker factor is the gamma itself. The printed line reports one solution for each sign, and the check confirms that they are proportional to $C$ and to $\Gamma C$.

**In [6], the picture of the three matrices.**

```python
fig, axes = plt.subplots(1, 3, figsize=(11.0, 4.0))
heat_map(axes[0], calC_plus, r"$\mathcal{C}_+ = C$")
heat_map(axes[1], Gamma, r"$\Gamma$", row_label=False)
image = heat_map(axes[2], calC_minus, r"$\mathcal{C}_- = \Gamma C$",
                 row_label=False)
fig.colorbar(image, ax=axes, ticks=[-1, 0, 1], shrink=0.8, label="matrix entry")
save_figure(fig, "conjugation_matrices", ...)
```

Three heat maps and a colour bar. **What figure 05c.2 shows**: $\mathcal{C}_+ = C$ with blue squares in the pattern of $\sigma$ in the top-left block and red ones in the bottom-right block; $\Gamma$, blue then red on the diagonal; and $\mathcal{C}_- = \Gamma C$, red in the pattern of $\sigma$ in both diagonal blocks. The student should see that multiplying by $\Gamma$ only reverses the signs of the rows 1 to 8, and that all three pictures are mirror-symmetric about the diagonal (all three matrices are symmetric).

**In [7], the conjugate fields of a complex column.**

```python
k = np.arange(16)  # 0, 1, ..., 15
PSI0 = (k % 4 - 1) + 1j * (k % 3 - 1)  # a fixed complex column with small entries
say("Psi_0 = " + ", ".join(f"{z.real:+.0f}{z.imag:+.0f}i" for z in PSI0[:8]) + ",")
say("        " + ", ".join(f"{z.real:+.0f}{z.imag:+.0f}i" for z in PSI0[8:]))
```

A fixed complex column $\Psi_0$: its component number $k$ (counted from 0) is $(k \bmod 4) - 1 + i\,((k \bmod 3) - 1)$, where `%` gives the remainder of a division. Operations on the array `k` act on all 16 entries at once. The two printed lines list the components in the form $a + bi$ (`:+.0f` writes a number with its sign and no decimals): $-1-1i, +0+0i, +1+1i, +2-1i, \dots$.

```python
psibar_T = C @ PSI0.conj()  # (Psi^dagger C)^T = C^T Psi* = C Psi*
check(np.array_equal(calC_plus @ psibar_T, PSI0.conj())
      and np.array_equal(calC_minus @ psibar_T, Gamma @ PSI0.conj()),
      "Psi^c = calC_+ Psibar^T = Psi* and Psi^c = calC_- Psibar^T = Gamma Psi*")
```

$\bar\Psi^T = C\Psi^\ast$ (Section 5.28) is computed for this column, and the check confirms the two formulas $\mathcal{C}_+\bar\Psi^T = \Psi^\ast$ and $\mathcal{C}_-\bar\Psi^T = \Gamma\Psi^\ast$ of Theorem CC (b), entry by entry.

**In [8], which mass each field solves with, exactly.**

```python
x4, m = sp.symbols("x4 m", real=True)  # the time and the mass, real numbers
psi0 = sp.Matrix([sp.Integer(int(z.real)) + sp.I * sp.Integer(int(z.imag))
                  for z in PSI0])
G4 = sp.Matrix(gamma["x4"].tolist())  # gamma^(x4) as an exact sympy matrix
GAMMA = sp.Matrix(Gamma.tolist())
```

`sp.symbols("x4 m", real=True)` makes two sympy symbols, the time and the mass, declared real (so that sympy knows that their conjugates are themselves). `psi0` is $\Psi_0$ with exact whole-number real and imaginary parts (`sp.I` is sympy's $i$); `G4` and `GAMMA` are $\gamma^{(x4)}$ and $\Gamma$ as exact sympy matrices.

```python
psi = sp.cos(m * x4) * psi0 - sp.sin(m * x4) * G4 * psi0  # the solution
fields = {"Psi": psi, "Psi* (calC_+)": psi.conjugate(),
          "Gamma Psi* (calC_-)": GAMMA * psi.conjugate()}
solves = {}  # (field, mass sign) -> True when the residual is exactly zero
```

`psi` is the free solution $\Psi(x4) = \cos(m\,x4)\Psi_0 - \sin(m\,x4)\gamma^{(x4)}\Psi_0$ of Section 5.28, as a column of 16 exact expressions. `fields` collects it and its two images, $\Psi^\ast$ (`conjugate()`) and $\Gamma\Psi^\ast$, under readable names.

```python
for name, phi in fields.items():
    for sign in (+1, -1):
        residual = (G4 * phi.diff(x4) - sign * m * phi).applyfunc(sp.expand)
        solves[(name, sign)] = residual == sp.zeros(16, 1)
    say(f"{name:20} solves with +m: {solves[(name, 1)]!s:5}  "
        f"with -m: {solves[(name, -1)]!s:5}")
```

For each field $\Phi$ and each sign, the **residual** $\gamma^{(x4)}d\Phi/dx4 - (\pm m)\Phi$ is computed (`diff(x4)` differentiates every component); it is zero exactly when $\Phi$ solves the equation with that mass. `applyfunc(sp.expand)` multiplies out every component, and the comparison with the zero column `sp.zeros(16, 1)` is exact. Each printed line shows, for one field, True or False for $+m$ and $-m$ (`!s` writes the value as text, `:5` pads it to five characters).

```python
expected = {("Psi", 1): True, ("Psi", -1): False,
            ("Psi* (calC_+)", 1): True, ("Psi* (calC_+)", -1): False,
            ("Gamma Psi* (calC_-)", 1): False, ("Gamma Psi* (calC_-)", -1): True}
check(solves == expected,
      "exactly: Psi and Psi* solve with +m, Gamma Psi* solves with -m")
```

The prediction of Section 5.28 is written down and compared with the six results: $\Psi$ and $\Psi^\ast$ solve with $+m$ only, $\Gamma\Psi^\ast$ with $-m$ only. The printed lines (True False, True False, False True) agree.

**In [9], the same with numbers on 801 time points.**

```python
t = np.linspace(0.0, 4.0 * np.pi, 801)  # the time x4 in units of 1/m, m = 1
g4 = gamma["x4"].astype(float)
cos_t, sin_t = np.cos(t)[:, None], np.sin(t)[:, None]  # columns for broadcasting
psi_t = cos_t * PSI0 - sin_t * np.einsum("rc,c->r", g4, PSI0)  # row t: Psi(x4_t)
dpsi_t = -sin_t * PSI0 - cos_t * np.einsum("rc,c->r", g4, PSI0)  # dPsi/dx4
```

With $m = 1$ the time is measured in units of $1/m$. `t` holds 801 times from 0 to $4\pi$. `[:, None]` turns a list of 801 numbers into a column of 801 rows, so that `cos_t * PSI0` multiplies each row of 16 components by its own number (numpy's **broadcasting**: an array with one column is repeated along the missing direction). `np.einsum("rc,c->r", g4, PSI0)` is the column $\gamma^{(x4)}\Psi_0$. So `psi_t` has one row per time, the solution at that time, and `dpsi_t` its derivative, $-\sin t\,\Psi_0 - \cos t\,\gamma^{(x4)}\Psi_0$.

```python
numeric = {"Psi": (psi_t, dpsi_t),
           "Psi* (calC_+)": (psi_t.conj(), dpsi_t.conj()),
           "Gamma Psi* (calC_-)": (psi_t.conj() @ Gamma.T, dpsi_t.conj() @ Gamma.T)}
largest = {}  # (field, sign) -> largest size of the residual over the 801 points
```

The three fields with their derivatives. For a field stored as rows, multiplying every row by $\Gamma$ is done by `@ Gamma.T`: a row $u^T$ times $\Gamma^T$ is the transpose of the column $\Gamma u$.

```python
for name, (phi, dphi) in numeric.items():
    for sign in (+1, -1):
        residual = np.einsum("rc,tc->tr", g4, dphi) - sign * 1.0 * phi
        largest[(name, sign)] = float(np.max(np.linalg.norm(residual, axis=1)))
    shown = {sign: (f"{largest[(name, sign)]:.2f}" if largest[(name, sign)] > 1e-12
                    else "below 1e-12") for sign in (1, -1)}  # rounding-proof text
    say(f"{name:20} largest residual with +m: {shown[1]:11}, with -m: {shown[-1]}")
```

For each field and sign the residual $\gamma^{(x4)}d\Phi/dx4 \mp \Phi$ is computed at all 801 times at once (`"rc,tc->tr"` multiplies $\gamma^{(x4)}$ with the column of every time $t$). `np.linalg.norm(..., axis=1)` is the length of the residual at each time, and the largest one is kept. A tiny residual is printed as the words below 1e-12 rather than as a number, because its last digits depend on the computer. The printed lines show below 1e-12 where the exact computation said True, and 11.83 where it said False.

```python
check(all((largest[key] < 1e-12) == solves[key] for key in solves),
      "the numerical residuals agree with the exact result")
```

The check: a residual below $10^{-12}$ exactly where the exact computation found a solution.

**In [10], the picture of the three fields.**

```python
fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2), sharey=True)
styles = {"Psi": ("#2a78d6", "-"), "Psi* (calC_+)": ("#eb6834", "--"),
          "Gamma Psi* (calC_-)": ("#1baf7a", ":")}
labels = {"Psi": r"$\Psi$", "Psi* (calC_+)": r"$\Psi^c_+ = \Psi^*$",
          "Gamma Psi* (calC_-)": r"$\Psi^c_- = \Gamma\Psi^*$"}
```

Two pictures that share the vertical axis (`sharey=True`), and for each field a colour, a line style (solid, dashed, dotted) and a legend label.

```python
for name, (phi, _) in numeric.items():
    color, line = styles[name]
    axes[0].plot(t, phi[:, 0].real, color=color, linestyle=line, linewidth=2,
                 label=labels[name])
    axes[1].plot(t, phi[:, 0].imag, color=color, linestyle=line, linewidth=2,
                 label=labels[name])
```

For each field, the real part (left) and the imaginary part (right) of its first component (`phi[:, 0]` is column 0 of the rows, that is component 1 at every time) is drawn against the time. The derivative is not needed here, so it gets the throw-away name `_`.

```python
for ax, part in zip(axes, ["real part", "imaginary part"]):
    ax.set_xticks([0, np.pi, 2 * np.pi, 3 * np.pi, 4 * np.pi],
                  ["0", r"$\pi$", r"$2\pi$", r"$3\pi$", r"$4\pi$"])
    ax.set_xlabel("time $x4$ (in units of $1/m$)")
    ax.set_title(f"component 1, {part}")
axes[0].set_ylabel("value of the component")
axes[1].legend(loc="upper center", bbox_to_anchor=(-0.05, -0.17), ncol=3)
save_figure(fig, "conjugate_solutions", ...)
```

Tick marks at multiples of $\pi$, axis labels and titles; one legend with three columns below both pictures. **What figure 05c.3 shows**: on the left the real part of $\Psi^\ast$ (dashed) lies on that of $\Psi$ (solid), and that of $\Gamma\Psi^\ast$ (dotted) is its mirror image; on the right the imaginary part of $\Psi^\ast$ is the mirror image of that of $\Psi$, and that of $\Gamma\Psi^\ast$ lies on it. The reason: $\Psi^\ast$ reverses the imaginary part, and $\Gamma$ (which is $-1$ on the first half) reverses component 1 once more.

**In [11], the table of the largest residuals.**

```python
from matplotlib.patches import Patch  # a coloured square for a legend

names = list(numeric)
table = np.array([[largest[(name, 1)], largest[(name, -1)]] for name in names])
fig, ax = plt.subplots(figsize=(7.0, 3.6))
solved = table < 1e-12  # True where the field solves the equation
ax.imshow(np.where(solved, 1.0, 0.0), cmap=LinearSegmentedColormap.from_list(
    "solve", ["#f0efec", "#2a78d6"]), vmin=0, vmax=1, aspect="auto")
```

The six largest residuals form a table of three rows (fields) and two columns (masses). `solved` is true where the residual is below $10^{-12}$; `np.where(solved, 1.0, 0.0)` turns it into ones and zeros, drawn blue and grey with a two-colour map made on the spot.

```python
for r in range(3):
    for c in range(2):
        text = "solves" if solved[r, c] else f"no ({table[r, c]:.2f})"
        ax.text(c, r, text, ha="center", va="center",
                color="white" if solved[r, c] else "black", fontweight="bold")
ax.axhline(0.5, color="white", linewidth=2)
ax.axhline(1.5, color="white", linewidth=2)
ax.axvline(0.5, color="white", linewidth=2)
ax.set_xticks([0, 1], ["mass $+m$", "mass $-m$"])
ax.set_yticks(range(3), [labels[name] for name in names])
ax.set_title("Largest residual of the field equation on $0 \\leq x4 \\leq 4\\pi$")
ax.legend(handles=[Patch(color="#2a78d6", label="residual below $10^{-12}$"),
                   Patch(color="#f0efec", label="residual of order 1")],
          loc="upper center", bbox_to_anchor=(0.5, -0.14), ncol=2)
ax.grid(False)
save_figure(fig, "which_mass", ...)
```

Each square gets the word solves or the word no with the residual; white lines separate the squares; the labels name the masses and the fields; a legend made of two coloured squares (`Patch`) goes below the picture. **What figure 05c.4 shows**: blue squares solves for $\Psi$ and $\Psi^\ast$ under $+m$ and for $\Gamma\Psi^\ast$ under $-m$, grey squares no (11.83) in the other three places: $\mathcal{C}_+$ keeps the mass, $\mathcal{C}_-$ reverses it.

**In [12], the scalar and the charge density of the three fields.**

```python
bilinears = {}  # field -> (S at every time point, J^(x4) at every time point)
for name, (phi, _) in numeric.items():
    S_t = np.einsum("tr,rc,tc->t", phi.conj(), C, phi).real  # Psi^dagger C Psi
    J_t = np.einsum("tr,rc,tc->t", phi.conj(), B, phi).real  # Psi^dagger B Psi
    bilinears[name] = (S_t, J_t)
    say(f"{name:20} S from {S_t.min():+.6f} to {S_t.max():+.6f}; "
        f"J^(x4) from {J_t.min():+.6f} to {J_t.max():+.6f}")
```

For commuting components the scalar $S = \Psi^\dagger C\Psi$ and the charge density $J^{(x4)} = \Psi^\dagger B\Psi$ are computed at all 801 times (`"tr,rc,tc->t"` is $\sum_{r,c}\Psi_r^\ast K_{rc}\Psi_c$ for every time). Both are real (Section 5.4), and `.real` drops the imaginary part, which is zero up to rounding. Each printed line shows the smallest and the largest value over the times: $S$ stays at $-2$ for all three fields, $J^{(x4)}$ at $-6$, $+6$ and $-6$. Both are constant. With $d\Psi/dx4 = -m\gamma^{(x4)}\Psi$ and $(\gamma^{(x4)}\Psi)^\dagger = \Psi^\dagger(\gamma^{(x4)})^T$, the product rule gives $dS/dx4 = -m\Psi^\dagger\big((\gamma^{(x4)})^TC + C\gamma^{(x4)}\big)\Psi$, which is 0 because $(\gamma^{(x4)})^T = -\gamma^{(x4)}$ and $\gamma^{(x4)}$ commutes with $C$ (C1); in the same way $dJ^{(x4)}/dx4 = -m\Psi^\dagger\big((\gamma^{(x4)})^TB + B\gamma^{(x4)}\big)\Psi = 0$, because $(\gamma^{(x4)})^TB = iC\gamma^{(x4)}\gamma^{(x4)} = -iC$ and $B\gamma^{(x4)} = -iC\gamma^{(x4)}\gamma^{(x4)} = iC$.

```python
S_psi, J_psi = bilinears["Psi"][0][0], bilinears["Psi"][1][0]
report("S of the solution Psi", f"{S_psi:+.6f}")
report("J^(x4) of the solution Psi", f"{J_psi:+.6f}")
constant = all(np.ptp(v) < 1e-12 for pair in bilinears.values() for v in pair)
```

The values of $\Psi$ at the first time point, $x4 = 0$, are printed as two RESULT lines: $S = -2.000000$ and $J^{(x4)} = -6.000000$. `np.ptp` (peak to peak) is the largest minus the smallest value; `constant` is true when it is below $10^{-12}$ for all six lists.

```python
S_exact = PSI0.conj() @ C @ PSI0
J_exact = PSI0.conj() @ B @ PSI0
check(S_exact == -2 and J_exact == -6 and S_psi == -2 and J_psi == -6,
      "at x4 = 0 exactly: S = -2 and J^(x4) = -6 for the solution Psi")
```

At $x4 = 0$ the solution is $\Psi_0$, whose real and imaginary parts are whole numbers; $C$ and $B$ have the entries $0$, $\pm1$, $\pm i$; so $\Psi_0^\dagger C\Psi_0$ and $\Psi_0^\dagger B\Psi_0$ are computed exactly (small whole numbers are stored without rounding). The check requires $-2$ and $-6$ exactly, the numbers quoted in the caption of the next figure.

```python
check(constant and abs(S_psi) > 1 and abs(J_psi) > 1
      and np.allclose(bilinears["Psi* (calC_+)"][0], S_psi)
      and np.allclose(bilinears["Psi* (calC_+)"][1], -J_psi)
      and np.allclose(bilinears["Gamma Psi* (calC_-)"][0], S_psi)
      and np.allclose(bilinears["Gamma Psi* (calC_-)"][1], J_psi),
      "commuting components: Psi* keeps S and reverses J; Gamma Psi* keeps S and J")
```

The commuting rows of the sign table of Section 5.29, on this solution: all values constant, not zero (so that a sign can be seen), $\Psi^\ast$ with the same $S$ and the opposite $J^{(x4)}$, $\Gamma\Psi^\ast$ with the same $S$ and the same $J^{(x4)}$.

**In [13], the bar picture of $S$ and $J$.**

```python
fig, ax = plt.subplots(figsize=(8.0, 4.2))
width = 0.26  # the width of one bar
for j, name in enumerate(names):
    color, _ = styles[name]
    values = [bilinears[name][0][0], bilinears[name][1][0]]
    bars = ax.bar(np.arange(2) + (j - 1) * width, values, width, color=color,
                  edgecolor="white", linewidth=2, label=labels[name])
    for bar, v in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, v + (0.3 if v > 0 else -0.7),
                f"{v:+.0f}", ha="center")
```

Two groups of three bars: at the position 0 the scalar, at 1 the charge density; the three fields are shifted by $-1$, $0$, $+1$ bar widths. Each bar gets its value written just above (positive) or below (negative) it; `bar.get_x() + bar.get_width() / 2` is the middle of the bar.

```python
ax.axhline(0.0, color="black", linewidth=0.8)
ax.set_xticks([0, 1], [r"scalar $S = \Psi^\dagger C\Psi$",
                       r"charge density $J^{(x4)} = \Psi^\dagger B\Psi$"])
ax.set_ylabel("value (constant along $x4$)")
ax.set_ylim(-8, 8)
ax.set_title("Commuting components: what the two conjugations do to S and J")
ax.legend(loc="upper left")
save_figure(fig, "bilinears", ...)
```

The zero line, the labels of the two groups, the vertical range from $-8$ to $8$, the title and the legend. **What figure 05c.5 shows**: three bars at $-2$ in the left group; in the right group $-6$ (blue, $\Psi$), $+6$ (orange, $\Psi^\ast$) and $-6$ (aqua, $\Gamma\Psi^\ast$). For commuting components $\mathcal{C}_+$ reverses the charge and keeps the mass; $\mathcal{C}_-$ keeps the charge and reverses the mass.

**In [14], the sign table.**

```python
K_S = C.astype(complex)  # the matrix of the scalar S
K_J = [-1j * (C @ gamma[x]) for x in COORDS]  # the matrices of the currents J^a


def sign_of(M, K, eps):
    new = eps * (M.conj().T @ K @ M).T
    return 1 if np.array_equal(new, K) else (-1 if np.array_equal(new, -K) else 0)
```

The matrices of the scalar and of the eight currents, and `sign_of(M, K, eps)`, which computes $K' = \epsilon(M^\dagger KM)^T$ of Section 5.29 and returns $+1$ if $K' = K$, $-1$ if $K' = -K$, and 0 otherwise. The comparisons are exact, because all entries are $0$, $\pm1$ or $\pm i$.

```python
measured = {}  # the record's keys, e.g. "plus,eps=1" -> [sign of S, [signs of J]]
for map_name, M in (("plus", I16), ("minus", Gamma)):
    for eps in (1, -1):
        measured[f"{map_name},eps={eps}"] = [
            sign_of(M, K_S, eps), [sign_of(M, K, eps) for K in K_J]]
for key, (sign_S, signs_J) in measured.items():
    say(f"{key:13} S -> {sign_S:+d} S;  J^a -> s J^a with s = "
        + " ".join(f"{s:+d}" for s in signs_J))
```

For the two maps ($M = 1$ and $M = \Gamma$) and the two kinds of components the signs are collected under the keys that the record uses, for example `plus,eps=1`. The four printed lines are the four rows of the table of Section 5.29: `plus,eps=1` $+1$ and eight times $-1$; `plus,eps=-1` $-1$ and eight times $+1$; `minus,eps=1` $+1$ and eight times $+1$; `minus,eps=-1` $-1$ and eight times $-1$.

```python
recorded_table = json.loads(detail("bilinears_under_charge_conjugation")
                            .split("measured: ", 1)[1])
check_reproduces(measured == recorded_table
                 and recorded("bilinears_under_charge_conjugation"),
                 "the signs of S and J under calC_+ and calC_-, commuting and "
                 "anticommuting, equal the recorded table",
                 record=f"{RECORD}, check bilinears_under_charge_conjugation")
```

The record's detail text ends with the word measured, a colon and the table in JSON form. `split("measured: ", 1)[1]` takes the text after these words, and `json.loads` turns it into a dictionary of the same shape as `measured`. The check requires the two to be equal: the notebook and the record measured the same 36 signs.

**In [15], the picture of the sign table.**

```python
row_keys = ["plus,eps=1", "plus,eps=-1", "minus,eps=1", "minus,eps=-1"]
row_names = [r"$\mathcal{C}_+$, commuting", r"$\mathcal{C}_+$, anticommuting",
             r"$\mathcal{C}_-$, commuting", r"$\mathcal{C}_-$, anticommuting"]
grid = np.array([[measured[key][0]] + measured[key][1] for key in row_keys])
fig, ax = plt.subplots(figsize=(10.0, 3.8))
ax.imshow(grid, cmap=SIGNS, vmin=-1, vmax=1, aspect="auto")
```

The four rows of signs, each the sign of $S$ followed by the eight signs of the currents (`[a] + list` puts one element in front of a list), form a $4 \times 9$ array, drawn with the colour map of the heat maps.

```python
for r in range(4):
    for c in range(9):
        ax.text(c, r, f"{grid[r, c]:+d}", ha="center", va="center", color="white",
                fontweight="bold")
for k in range(1, 4):
    ax.axhline(k - 0.5, color="white", linewidth=2)
for k in range(1, 9):
    ax.axvline(k - 0.5, color="white", linewidth=3 if k == 1 else 2)
ax.set_xticks(range(9), ["$S$"] + [rf"$J^{{({x})}}$" for x in COORDS])
ax.set_yticks(range(4), row_names)
ax.set_title("Sign of each bilinear after the conjugation (red $+1$ kept, blue "
             "$-1$ reversed)")
ax.grid(False)
save_figure(fig, "sign_table", ...)
```

Each square gets its sign in bold white; white lines separate the squares, with a thicker line between the column $S$ and the currents; the columns are labelled $S$, $J^{(x1)}, \dots, J^{(x8)}$ (the doubled braces of the `rf`-string give single braces) and the rows by map and kind of component. **What figure 05c.6 shows**: the row $\mathcal{C}_+$, commuting is red for $S$ and blue for all currents; the row $\mathcal{C}_-$, commuting is red everywhere; each anticommuting row is the commuting row above it with every colour reversed. The student should see that the exchange of two anticommuting components flips every sign once more.

**In [16], the reality conditions.**

```python
check_reproduces(np.array_equal(I16 @ np.conj(I16), I16)
                 and np.array_equal(Gamma @ np.conj(Gamma), I16)
                 and recorded("majorana_conditions_consistent"),
                 "M M* = 1 for M = 1 and M = Gamma: both reality conditions are "
                 "consistent",
                 record=f"{RECORD}, check majorana_conditions_consistent")
```

The consistency condition $MM^\ast = 1$ of Section 5.29 for $M = 1$ and $M = \Gamma$.

**In [17], the reality conditions in time.**

```python
start_real = PSI0.real.astype(complex)  # obeys Psi_0* = Psi_0
start_gamma = np.concatenate([1j * PSI0.imag[:8], PSI0.real[8:]])  # first half
start_gamma = start_gamma / np.linalg.norm(start_gamma)  # imaginary, size 1
start_real = start_real / np.linalg.norm(start_real)  # size 1
check(np.allclose(start_gamma, Gamma @ start_gamma.conj())
      and np.allclose(start_real, start_real.conj()),
      "the two starting columns obey Psi_0 = Gamma Psi_0* and Psi_0 = Psi_0*")
```

Two starting columns of length 1: the real part of $\Psi_0$, which obeys $\Psi_0 = \Psi_0^\ast$; and a column whose first half is $i$ times the imaginary parts of the first eight components of $\Psi_0$ and whose second half is the real parts of the last eight (`np.concatenate` joins two arrays), which obeys $\Psi_0 = \Gamma\Psi_0^\ast$. Dividing by `np.linalg.norm` (the length) makes the length 1. The check confirms the two conditions.

```python
def evolve(start, mass):
    return (np.cos(mass * t)[:, None] * start
            - np.sin(mass * t)[:, None] * np.einsum("rc,c->r", g4, start))
```

`evolve(start, mass)` is the free solution with the given starting column and mass at all 801 times, one row per time.

```python
violation = {}  # (condition, mass) -> size of the violation at every time
for mass in (1.0, 0.5, 0.0):
    f_real = evolve(start_real, mass)
    f_gamma = evolve(start_gamma, mass)
    violation[("real", mass)] = np.linalg.norm(f_real - f_real.conj(), axis=1)
    violation[("gamma", mass)] = np.linalg.norm(f_gamma - f_gamma.conj() @ Gamma.T,
                                                axis=1)
```

For the masses 1, 0.5 and 0 both solutions are computed, and at each time the length of $\Psi - \Psi^\ast$ (the violation of the real condition) and of $\Psi - \Gamma\Psi^\ast$ (the violation of the other one).

```python
check(all(np.max(violation[("real", mass)]) < 1e-12 for mass in (1.0, 0.5, 0.0))
      and np.max(violation[("gamma", 0.0)]) < 1e-12
      and np.allclose(violation[("gamma", 1.0)], 2 * np.abs(np.sin(t)))
      and np.allclose(violation[("gamma", 0.5)], 2 * np.abs(np.sin(0.5 * t))),
      "Psi = Psi* is kept in time; Psi = Gamma Psi* is violated by 2 |sin(m x4)|")
```

The prediction of Section 5.29: the real condition is never violated; the other is violated by exactly $2|\sin(m\,x4)|$ (the starting column has length 1), which is zero only for $m = 0$.

```python
fig, ax = plt.subplots(figsize=(8.0, 4.2))
ax.plot(t, violation[("gamma", 1.0)], color="#eb6834", linewidth=2,
        label=r"$|\Psi - \Gamma\Psi^*|$, $m = 1$")
ax.plot(t, violation[("gamma", 0.5)], color="#eda100", linewidth=2, linestyle="--",
        label=r"$|\Psi - \Gamma\Psi^*|$, $m = 0.5$")
ax.plot(t, violation[("gamma", 0.0)], color="#4a3aa7", linewidth=3, linestyle="-.",
        label=r"$|\Psi - \Gamma\Psi^*|$, $m = 0$")
ax.plot(t, violation[("real", 1.0)], color="#2a78d6", linewidth=2, linestyle=":",
        label=r"$|\Psi - \Psi^*|$, $m = 1$ (real start)")
```

Four curves: the violation of $\Psi = \Gamma\Psi^\ast$ for the three masses (solid, dashed, dash-dotted) and that of the real condition for $m = 1$ (dotted).

```python
ax.set_xticks([0, np.pi, 2 * np.pi, 3 * np.pi, 4 * np.pi],
              ["0", r"$\pi$", r"$2\pi$", r"$3\pi$", r"$4\pi$"])
ax.set_xlabel("time $x4$")
ax.set_ylabel("size of the violation")
ax.set_ylim(-0.1, 2.4)
ax.annotate("the dash-dotted and the dotted curve are exactly 0 at all times",
            (2.5 * np.pi, 0.0), xytext=(2.0 * np.pi, 0.35), ha="center",
            arrowprops={"arrowstyle": "->", "color": "black"},
            bbox={"facecolor": "white", "edgecolor": "#52514e"})
ax.set_title("Which reality condition survives the time evolution")
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.17), ncol=2)
save_figure(fig, "reality_in_time", ...)
```

Tick marks, labels, the vertical range, and an **annotation**: a text in a white box with an arrow pointing at the place $(2.5\pi, 0)$, where two curves lie on the axis and would otherwise be hard to see. **What figure 05c.7 shows**: the solid curve $2|\sin x4|$ with arches of height 2, the dashed curve $2|\sin(x4/2)|$ with arches twice as wide, and two curves lying exactly on zero: the real field stays real, and the condition of the mass-reversing conjugation survives only for $m = 0$.

**In [18], real fields.**

```python
r = sp.Matrix(sp.symbols("r1:17", real=True))  # a general real column
currents = [sp.expand((-sp.I * r.T * sp.Matrix((C @ gamma[x]).tolist()) * r)[0, 0])
            for x in COORDS]
say("J^a of a general real column, a = x1..x8: " + ", ".join(map(str, currents)))
```

`sp.symbols("r1:17", real=True)` makes the 16 real symbols $r_1, \dots, r_{16}$, and `r` is the column of them: all real columns at once. For each direction the current $J^a = -i\,r^TC\gamma^ar$ is multiplied out (`[0, 0]` takes the single entry of the $1 \times 1$ result). The printed line shows eight zeros: fact (F1) of Section 5.29.

```python
S_change = sp.expand((GAMMA * r).T * sp.Matrix(C.tolist()) * (GAMMA * r)
                     - r.T * sp.Matrix(C.tolist()) * r)[0, 0]
kinetic_reversed = all(np.array_equal(Gamma.T @ C @ gamma[x] @ Gamma,
                                      -(C @ gamma[x])) for x in COORDS)
```

`S_change` is $S(\Gamma r) - S(r)$ for the general real column, multiplied out; it must be 0. `kinetic_reversed` checks $\Gamma^TC\gamma^a\Gamma = -C\gamma^a$ for the eight directions, (X8).

```python
psi0_real = psi0.applyfunc(sp.re)  # the real part of every component of Psi_0
psi_real = sp.cos(m * x4) * psi0_real - sp.sin(m * x4) * G4 * psi0_real
image = GAMMA * psi_real  # the real field Gamma Psi
image_solves_minus = (G4 * image.diff(x4) + m * image).applyfunc(sp.expand) \
    == sp.zeros(16, 1)
```

The real free solution that starts at the real part of $\Psi_0$ (`sp.re` is the real part), its image $\Gamma\Psi$, and the exact test whether the image solves the equation with $-m$: the residual $\gamma^{(x4)}d\Phi/dx4 + m\Phi$ must vanish. A backslash at the end of a line continues the statement on the next line.

```python
check_reproduces(all(c == 0 for c in currents) and S_change == 0 and kinetic_reversed
                 and psi_real.conjugate() == psi_real and image_solves_minus
                 and recorded("real_fields_charge_conjugation"),
                 "real fields: J = 0, calC_+ is the identity, Gamma keeps S, reverses "
                 "the kinetic matrices and maps a solution with m to one with -m",
                 record=f"{RECORD}, check real_fields_charge_conjugation")
```

The three facts (F1) to (F3) of Section 5.29 in one check: the currents vanish, the real solution equals its conjugate (so $\mathcal{C}_+$ acts as the identity on it), $\Gamma$ keeps $S$, reverses the kinetic matrices, and maps the real solution with mass $m$ to a real solution with mass $-m$.

**In [19], the picture of a real field.**

```python
real_t = evolve(PSI0.real.astype(complex), 1.0).real  # the real solution, m = 1
gamma_t = real_t @ Gamma.T  # Gamma Psi at every time
fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2), sharey=True)
```

The real solution for $m = 1$ at the 801 times (the starting column is not normalised here), and its image under $\Gamma$; two pictures with a shared vertical axis.

```python
for ax, comp in zip(axes, [0, 8]):
    ax.plot(t, real_t[:, comp], color="#2a78d6", linewidth=3,
            label=r"real solution $\Psi$ (mass $m$)")
    ax.plot(t, real_t[:, comp], color="#eb6834", linewidth=2, linestyle="--",
            label=r"$\Psi^c_+ = \Psi^* = \Psi$ (identical)")
    ax.plot(t, gamma_t[:, comp], color="#1baf7a", linewidth=2, linestyle=":",
            label=r"$\Gamma\Psi$ (solves with mass $-m$)")
    ax.set_xticks([0, np.pi, 2 * np.pi, 3 * np.pi, 4 * np.pi],
                  ["0", r"$\pi$", r"$2\pi$", r"$3\pi$", r"$4\pi$"])
    ax.set_xlabel("time $x4$ (in units of $1/m$)")
    half = "first" if comp < 8 else "second"  # components 1-8 or 9-16
    ax.set_title(f"component {comp + 1} ({half} half)")
```

For component 1 (left; Python's index 0) and component 9 (right; index 8) three curves are drawn: the real solution (thick, solid), its $\mathcal{C}_+$ image, which is the same curve (dashed on top of it), and its $\Gamma$ image (dotted). The title names the component and its half.

```python
axes[0].set_ylabel("value of the component")
axes[1].text(2.0 * np.pi, 0.0, "all three curves coincide:\n"
             r"$\Gamma = +1$ on the second half", ha="center", va="center",
             bbox={"facecolor": "white", "edgecolor": "#52514e"})
axes[1].legend(loc="upper center", bbox_to_anchor=(-0.05, -0.17), ncol=3)
save_figure(fig, "real_field", ...)
```

A text box in the right picture explains why only one curve is visible there, and one legend goes below both pictures. **What figure 05c.8 shows**: on the left the dashed curve lies exactly on the solid one, and the dotted curve is their mirror image; on the right all three coincide. For a real field the same-mass conjugation does nothing; the only nontrivial real map is $\Gamma$, which flips the first half and belongs to the mass $-m$.

**In [20], the quantised field.**

```python
q_plus = I16 @ B.T @ I16.conj().T  # M = 1
q_minus = Gamma @ B.T @ Gamma.conj().T  # M = Gamma
say(f"B^T = -B: {np.array_equal(B.T, -B)};  1 B^T 1 = B: "
    f"{np.array_equal(q_plus, B)};  Gamma B^T Gamma^dagger = B: "
    f"{np.array_equal(q_minus, B)}")
```

The test of Section 5.34: a map $\Psi \to M\Psi^{\dagger T}$ of the quantised field keeps the canonical anticommutator exactly when $MB^TM^\dagger = B$. The cell computes $MB^TM^\dagger$ for $M = 1$ and $M = \Gamma$. The printed line shows True for $B^T = -B$, False for $M = 1$ and True for $M = \Gamma$.

```python
check_reproduces(np.array_equal(q_minus, B) and np.array_equal(q_plus, -B)
                 and recorded("quantum_charge_conjugation_unitary_type"),
                 "M B^T M^dagger = B for M = Gamma and = -B for M = 1: the conjugation "
                 "of the quantised field is Psi -> Gamma Psi^(dagger T), which reverses "
                 "the mass",
                 record=f"{RECORD}, check quantum_charge_conjugation_unitary_type")
```

The check reproduces the record: $\Gamma B^T\Gamma^\dagger = B$, while $M = 1$ gives $-B$.

```python
fig, axes = plt.subplots(1, 3, figsize=(11.0, 4.0))
heat_map(axes[0], B.imag, "imaginary part of $B$")
heat_map(axes[1], q_plus.imag, r"imaginary part of $1\,B^T 1$", row_label=False)
image = heat_map(axes[2], q_minus.imag, r"imaginary part of $\Gamma B^T\Gamma$",
                 row_label=False)
fig.colorbar(image, ax=axes, ticks=[-1, 0, 1], shrink=0.8, label="matrix entry")
save_figure(fig, "quantum_b", ...)
```

Three heat maps of imaginary parts (the real parts are zero). **What figure 05c.9 shows**: the middle picture has every colour of the left one reversed ($B^T = -B$), while the right picture equals the left one: only $\Psi \to \Gamma\Psi^{\dagger T}$ keeps the canonical rule.

**In [21], the last check.**

```python
FIGURES = ["05c_1_solution_spaces.png", "05c_2_conjugation_matrices.png",
           "05c_3_conjugate_solutions.png", "05c_4_which_mass.png",
           "05c_5_bilinears.png", "05c_6_sign_table.png",
           "05c_7_reality_in_time.png", "05c_8_real_field.png", "05c_9_quantum_b.png"]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in FIGURES),
      "the nine figure files of notebook 05c exist")
all_checks_passed()
```

The nine figure files must exist, and the last line reads ALL 20 CHECKS PASSED (notebook 05c): two checks in In [2], two in In [3], one in In [4], three in In [5], one in In [7], one in In [8], one in In [9], two in In [12], one in In [14], one in In [16], two in In [17], one in In [18], one in In [20] and one in In [21]. Ten of them reproduce checks of the lead report (the two of In [2], the two of In [3], the first two of In [5], and those of In [14], In [16], In [18] and In [20]); the other ten are the notebook's own computations. The two lead checks that the notebook does not repeat are `spinor_connection_real` and `u1_noether_matrix_identity`, which need the curved metric (Chapters 6 and 21).

### 5.34 The quantised field: operators, the indefinite form and normal ordering

The field dirac16complex is **quantised** (Chapter 10 does this in full): its 16 components become operators, and a charge conjugation of the quantised field must be a map of operators that keeps the basic rule of the quantum theory. This section explains the few words of quantum theory that are needed, from zero, and then derives which conjugation survives and what it does to the scalar and to the currents. Notebook 05e computes every statement on an explicit computer model with $2^{16} = 65536$ quantum states.

**Operators, anticommutators, modes.** In quantum theory a **state** is a column of numbers, and an **operator** is a rule that turns a state into another state; here every operator is a (big) matrix acting on columns. Operators are multiplied by doing one after the other, and the order matters. The **anticommutator** of two operators is $\{X, Y\} = XY + YX$. A **fermion mode** is a place that holds zero or one particle. With $n$ modes a basic state is a **pattern** of $n$ occupations, each 0 or 1, so there are $2^n$ patterns; all combinations of them form the **Fock space**. The **annihilation operator** $f_p$ empties mode $p$ (and gives zero if it is empty), and the **creation operator** $f_p^\ast$ fills it (zero if it is full), each with the sign $(-1)^{n_{<p}}$, where $n_{<p}$ is the number of occupied modes below $p$. Example with two modes 0 and 1: write the patterns as $|00\rangle$ (both empty), $|10\rangle$ (mode 0 full), $|01\rangle$ (mode 1 full) and $|11\rangle$ (both full). Then $f_0|11\rangle = |01\rangle$ (no mode below 0), while $f_1|11\rangle = -|10\rangle$ (mode 0 below is full). Because of this sign, operators of different modes **anticommute**; together these rules give the **canonical anticommutation relations**

$$
\{f_p, f_q^\ast\} = \delta_{pq}, \qquad \{f_p, f_q\} = 0, \qquad \{f_p^\ast, f_q^\ast\} = 0 ,
$$

where $\delta_{pq}$ is 1 for $p = q$ and 0 otherwise; in particular $f_pf_p = 0$: no mode holds two fermions. Check of one case: $f_0f_1|11\rangle = f_0(-|10\rangle) = -|00\rangle$ and $f_1f_0|11\rangle = f_1|01\rangle = |00\rangle$ (mode 0 is now empty, so no sign); the two add up to zero, $\{f_0, f_1\}|11\rangle = 0$. On the Fock space the ordinary inner product $\langle a|b\rangle = \sum_na_n^\ast b_n$ is **positive**: $\langle a|a\rangle$ is a sum of squared sizes. The **Hilbert adjoint** $X^\ast$ of an operator is the conjugate transpose of its matrix; $f_p^\ast$ is the Hilbert adjoint of $f_p$. For every operator $X$ and every state $\phi$,

$$
\langle\phi|\{X, X^\ast\}|\phi\rangle = \langle\phi|XX^\ast|\phi\rangle + \langle\phi|X^\ast X|\phi\rangle = |X^\ast\phi|^2 + |X\phi|^2 \geq 0 ,
$$

because $\langle\phi|XY\phi\rangle = \langle X^\ast\phi|Y\phi\rangle$ (the defining property of the adjoint) and $|v|^2 = \langle v|v\rangle$ is a squared length. **The anticommutator of an operator with its Hilbert adjoint is never negative.**

**The canonical rule of the record.** The Revision record quantises dirac16complex with the canonical anticommutator on a slice of constant time $x4$,

$$
\{\Psi_A(x), \Psi^\dagger_C(y)\} = B_{AC}\,\frac{\delta^7(x - y)}{\cos z} ,
$$

where $\delta^7$ is the delta function of the seven other coordinates and $\cos z$ the volume factor (formula `quantisation` of `Revision/theory/field-theory.json`; Chapter 10 derives it). For the operators of one single momentum, the record's exact Fock-space example, the delta function and the factor are absent and the rule reads $\{\Psi_A, \Psi^\dagger_C\} = B_{AC}$ for $A, C = 1, \dots, 16$.

**Why $\Psi^\dagger$ cannot be the Hilbert adjoint.** Suppose $\Psi^\dagger_A$ were the Hilbert adjoint $\Psi_A^\ast$. Every diagonal entry of $B$ is zero (the table of Section 5.6: row $r$ of $B/i$ never points to column $r$). So the rule would give $\{\Psi_A, \Psi_A^\ast\} = B_{AA} = 0$, and by the inequality above $|\Psi_A^\ast\phi|^2 + |\Psi_A\phi|^2 = 0$ for every state $\phi$; a sum of two squared lengths is zero only when both are, so $\Psi_A\phi = 0$ for every $\phi$: $\Psi_A$ would be the zero operator. But row $A$ of $B$ contains a nonzero entry $B_{AC}$, and the anticommutator of the zero operator with anything is zero, not $B_{AC}$: a contradiction. The record makes the same argument with the column $u$ that has $u_7 = -i/\sqrt2$, $u_{16} = 1/\sqrt2$ and zeros elsewhere, which obeys $Bu = -u$: the operator $X = \sum_Au_A^\ast\Psi_A$ has $\{X, X^\dagger\} = u^\dagger Bu = -1 < 0$, impossible for a Hilbert adjoint (check `no_positive_inner_product` of `Revision/theory/reports/wolfram-field-theory.json`). So the canonical rule needs an **indefinite** inner product, one in which some states have negative squared length; a space with such a product is called a **Krein space** (Chapter 10).

**The record's positive realisation.** The record keeps the positive Fock space and writes $\Psi^\dagger = \chi B$, where $\chi$ is the Hilbert adjoint of $\Psi$. For one momentum without extra-time part (the **good sector**; the record's example has the mass $m = 3$ and the momentum 4 along $x1$) the mode Hamiltonian is the $16 \times 16$ matrix

$$
h = -im\,\gamma^{(x4)} - 4\,\gamma^{(x4)}\gamma^{(x1)} .
$$

(The record writes the energy density of one momentum $k$ as $\Psi^\dagger(mC - iC\,k_a\gamma^a)\Psi = \chi h\Psi$, so $h = B(mC - iC\,k_a\gamma^a)$. With $BC = -iC\gamma^{(x4)}C = -i\gamma^{(x4)}$, because $C\gamma^{(x4)}C = -(\gamma^{(x4)})^T = \gamma^{(x4)}$ by (C5) and the antisymmetry of $\gamma^{(x4)}$, and with $k_{x1} = 4$ the only nonzero momentum, this is $h = -im\gamma^{(x4)} - 4i(-i\gamma^{(x4)})\gamma^{(x1)}$, the matrix above; check `mode_hamiltonian_Krein_selfadjoint` of `Revision/theory/reports/wolfram-field-theory.json`.) Both terms are Hermitian ($\gamma^{(x4)}$ is real and antisymmetric, so $-i\gamma^{(x4)}$ is Hermitian; $\gamma^{(x4)}\gamma^{(x1)}$ is real and, by Rule 4 of Section 5.3, symmetric), they anticommute (Rule 1), and each squares to 1 ($(-i\gamma^{(x4)})^2 = -\gamma^{(x4)}\gamma^{(x4)} = 1$; $(\gamma^{(x4)}\gamma^{(x1)})^2 = -\eta_{x4\,x4}\eta_{x1\,x1}1 = 1$). Hence $hh = (m^2 + 4^2)1 = 25\cdot1$, and the eigenvalues of $h$ are $\pm5$: the energy is $E = \sqrt{3^2 + 4^2} = 5$. Let $u_1, \dots, u_8$ be orthonormal eigenvectors with $hu_s = 5u_s$ and $v_1, \dots, v_8$ with $hv_s = -5v_s$; the 16 columns form a matrix $W$ with $W^\dagger W = WW^\dagger = 1$. With eight particle modes $b_s$ and eight antiparticle modes $d_s$ (sixteen modes in all) the field operators are

$$
\Psi_A = \sum_{s=1}^{8}\big((u_s)_A\,b_s + (v_s)_A\,d_s^\ast\big), \qquad \chi_A = \sum_{s=1}^{8}\big((u_s)_A^\ast\,b_s^\ast + (v_s)_A^\ast\,d_s\big), \qquad \Psi^\dagger_A = \sum_C\chi_CB_{CA} .
$$

Line by line: by the canonical relations only the pairs $(b_s, b_s^\ast)$ and $(d_s^\ast, d_s)$ have a nonzero anticommutator, equal to 1, so

$$
\{\Psi_A, \chi_C\} = \sum_s(u_s)_A(u_s)_C^\ast + \sum_s(v_s)_A(v_s)_C^\ast = (WW^\dagger)_{AC} = \delta_{AC} ,
$$

and then $\{\Psi_A, \Psi^\dagger_C\} = \sum_D\{\Psi_A, \chi_D\}B_{DC} = B_{AC}$: the canonical rule holds. The record also computes the energy $\chi h\Psi$, whose value in the **vacuum** $|0\rangle$ (no mode occupied) is $-8E = -40$ (the eight negative-energy solutions form a filled **sea**), and, after **normal ordering** (the subtraction of the vacuum value, defined below), the energy $+5$ for each of the 16 one-quantum states $b_s^\ast|0\rangle$ and $d_s^\ast|0\rangle$, and the charge $\Psi^\dagger B\Psi$ equal to $+1$ for the eight particles and $-1$ for the eight antiparticles (check `Fock_space_good_sector_example`). Notebook 05e reproduces all of this.

**Which conjugation keeps the rule.** For a real matrix $M$ define the conjugated field $\Psi'_A = \sum_CM_{AC}\Psi^\dagger_C$, the operator form of $M\Psi^\ast$, written $\Psi' = M\Psi^{\dagger T}$. Its canonical conjugate is obtained by conjugating both sides (which conjugates the numbers): $\Psi'^\dagger_A = \sum_CM_{AC}^\ast\Psi_C$. Then, line by line,

$$
\{\Psi'_A, \Psi'^\dagger_C\} = \sum_{D,E}M_{AD}M_{CE}^\ast\{\Psi^\dagger_D, \Psi_E\} = \sum_{D,E}M_{AD}B_{ED}M_{CE}^\ast = (MB^TM^\dagger)_{AC} .
$$

The first step expands both operators (numbers come out of an anticommutator); the second uses the canonical rule $\{\Psi^\dagger_D, \Psi_E\} = \{\Psi_E, \Psi^\dagger_D\} = B_{ED}$; the third reads the sum as a matrix product, since $B_{ED} = (B^T)_{DE}$ and $M^\ast_{CE} = (M^\dagger)_{EC}$. **The rule is kept exactly when $MB^TM^\dagger = B$.** Now $B$ is Hermitian and purely imaginary, so $B^T = (B^\dagger)^\ast = B^\ast = -B$. For $M = 1$: $MB^TM^\dagger = B^T = -B$: the rule is broken. For $M = \Gamma$ (real, $\Gamma^\dagger = \Gamma^T = \Gamma$):

$$
\Gamma B^T\Gamma = -\Gamma B\Gamma = -(-i)\,\Gamma C\gamma^{(x4)}\Gamma = i\,\Gamma^TC\gamma^{(x4)}\Gamma = i(-C\gamma^{(x4)}) = B ,
$$

by $B^T = -B$, the definition of $B$, (X6) and (X8). **Only $\Psi' = \Gamma\Psi^{\dagger T}$ keeps the canonical rule** (lead check `quantum_charge_conjugation_unitary_type`): the conjugation of the quantised field has the type of $\mathcal{C}_-$.

**The conjugated bilinear, line by line.** Let $X = \Psi^\dagger K\Psi = \sum_{A,C}\Psi^\dagger_AK_{AC}\Psi_C$ and $X' = \Psi'^\dagger K\Psi'$.

1. Insert the definitions: $X' = \sum_{A,C}\sum_{D,E}M^\ast_{AD}\Psi_D\,K_{AC}\,M_{CE}\Psi^\dagger_E = \sum_{D,E}\Psi_D\,K'_{DE}\,\Psi^\dagger_E$ with $K' = M^\dagger KM$ (collect the numbers: $\sum_{A,C}M^\ast_{AD}K_{AC}M_{CE} = (M^\dagger KM)_{DE}$).
2. Exchange the two operators with the canonical rule, $\Psi_D\Psi^\dagger_E = -\Psi^\dagger_E\Psi_D + B_{DE}$: $X' = -\sum_{D,E}\Psi^\dagger_EK'_{DE}\Psi_D + \sum_{D,E}K'_{DE}B_{DE}$.
3. Rename $D \leftrightarrow E$ in the first sum, and write the second as a trace ($\sum_{D,E}K'_{DE}(B^T)_{ED} = \mathrm{tr}(K'B^T)$):

$$
X' = \Psi^\dagger\big(-K'^T\big)\Psi + c, \qquad c = \mathrm{tr}(K'B^T) .
$$

So the conjugated bilinear is the bilinear with the matrix $-(M^\dagger KM)^T$ plus the number $c$ (times the identity operator). The matrix $-(M^\dagger KM)^T$ is exactly the rule $\epsilon(M^\dagger KM)^T$ of Section 5.29 with $\epsilon = -1$, the rule of classical anticommuting components. When $-(M^\dagger KM)^T = sK$ with a sign $s$, the result is $X' = sX + c$.

**The constant $c$.** For the scalar and the currents $K'$ is $\pm C$ or $\pm iC\gamma^a$, and $B^T = -B = iC\gamma^{(x4)}$. Then $K'B^T$ is a number times $C\,C\gamma^{(x4)} = \gamma^{(x4)}$ or times $C\gamma^aC\gamma^{(x4)} = -(\gamma^a)^T\gamma^{(x4)} = -\eta_{aa}\gamma^a\gamma^{(x4)}$ (by (C3), (C5) and the symmetry pattern). By Rule 5 of Section 5.3 the trace of a product of different gammas is zero, so $c = 0$, except when $\gamma^a\gamma^{(x4)}$ is not a product of different gammas, that is for $a = x4$: the charge density, whose matrix $-iC\gamma^{(x4)}$ is $B$ itself. For $M = 1$, $K' = B$ and $c = \mathrm{tr}(BB^T) = -\mathrm{tr}(BB) = -\mathrm{tr}\,1 = -16$; for $M = \Gamma$, $K' = \Gamma B\Gamma = -B$ and $c = +16$.

**Normal ordering removes $c$ and nothing else.** For an operator $X$ built from two field operators, **normal ordering** is the subtraction of its vacuum value, $:\!X\!: = X - \langle 0|X|0\rangle$ (for products of $b$, $b^\ast$, $d$, $d^\ast$ this is the same as moving every creation operator to the left of every annihilation operator, with a sign for each exchange). From $X' = sX + c$, the vacuum value is $\langle 0|X'|0\rangle = s\langle 0|X|0\rangle + c$, and

$$
:\!X'\!: = X' - \langle 0|X'|0\rangle = sX + c - s\langle 0|X|0\rangle - c = s\,:\!X\!: .
$$

The constant cancels and the sign stays. **After normal ordering the quantised bilinears change with the signs of the classical anticommuting components.** The argument uses only the canonical rule and the fact that normal ordering subtracts a number, so it does not depend on the momentum of the example or on the choice of the vacuum. For the allowed map $M = \Gamma$ the anticommuting row of Section 5.29 gives $(S, J) \to (-S, -J)$: every current is reversed, so the normal-ordered charge of every quantum changes sign (particles $+1 \to -1$, antiparticles $-1 \to +1$), and the scalar is reversed, so the mass term $mS$ becomes $(-m)S$: **the conjugation of the quantised field exchanges particles and antiparticles and reverses the mass**, as the Revision record states.

**About a remark in the record.** The detail text of the lead check `bilinears_under_charge_conjugation` adds, in parentheses, that in the quantum theory normal ordering supplies one more sign for each bilinear, which would give $(S, J) \to (S, -J)$ for $\mathcal{C}_+$. That remark is not part of the record's measured table, and the derivation above, which Notebook 05e confirms on the Fock space, does not support it: normal ordering removes the number $c$ and changes no sign. This book follows the computation; the point is listed as open for the owner of the record (Section 5.40).

| statement | status | where it is verified |
| --- | --- | --- |
| the canonical relations of fermion operators, 2 and 16 modes | COMPUTED exactly (2 modes) and on a random state (16 modes) | Notebook 05e, In [4] and In [6] (its own computation) |
| $\{\Psi_A, \chi_C\} = \delta_{AC}$, $\{\Psi_A, \Psi^\dagger_C\} = B_{AC}$ in the positive realisation | PROVED; COMPUTED on 65536 states | `Revision/theory/reports/wolfram-field-theory.json`, check `Fock_space_good_sector_example`; Notebook 05e, In [8] |
| the canonical conjugate is not a Hilbert adjoint ($\{X, X^\dagger\} = -1$) | PROVED; COMPUTED | the same report, check `no_positive_inner_product`; Notebook 05e, In [10] |
| vacuum energy $-8E = -40$, energies $+5$, charges $\pm1$ | COMPUTED (to $10^{-12}$) | the same report, check `Fock_space_good_sector_example`; Notebook 05e, In [12] |
| $MB^TM^\dagger = B$ for $M = \Gamma$, $= -B$ for $M = 1$ | PROVED; COMPUTED on the Fock space | `Revision/lead_checks/reports/charge-conjugation-and-u1.json`, check `quantum_charge_conjugation_unitary_type`; Notebook 05e, In [14] |
| $X' = sX + c$ with the anticommuting signs; $c = \mp16$ for the charge density, 0 otherwise | PROVED; COMPUTED on the Fock space | Notebook 05e, In [16] and In [17]; the signs equal the anticommuting rows of the lead check `bilinears_under_charge_conjugation` |
| $:\!X'\!: = s\,:\!X\!:$; $\Psi \to \Gamma\Psi^{\dagger T}$ reverses the charge of every quantum | PROVED; COMPUTED | Notebook 05e, In [18] and In [19] (its own computation) |

### 5.35 Example: Notebook 05e computes the conjugation of the quantised field

Notebook 05e builds fermion operators from zero, first for two modes as $4 \times 4$ matrices and then for sixteen modes on the Fock space of 65536 patterns, where a state is stored as a list of its nonzero amplitudes. It realises the quantised field of the record's good-sector example ($m = 3$, momentum 4 along $x1$, $E = 5$), checks the canonical rule, shows why the canonical conjugate cannot be a Hilbert adjoint, and reproduces the vacuum energy $-40$, the energies $+5$ and the charges $\pm1$ of the 16 quanta. Then it applies the two conjugations $M = 1$ and $M = \Gamma$ to the operators, measures the anticommutators, computes all nine conjugated bilinears as operators, finds the sign and the constant of $X' = sX + c$, and checks that normal ordering removes the constant and keeps the sign. It reads `Revision/algebra/gammas.json`, `Revision/theory/field-theory.json`, `Revision/theory/reports/wolfram-field-theory.json` and `Revision/lead_checks/reports/charge-conjugation-and-u1.json`. It draws eight figures and ends with the line ALL 18 CHECKS PASSED (notebook 05e).

<!-- NOTEBOOK 05e -->

### 5.38 Line-by-line walk-through of Notebook 05e

The notebook has 20 code cells. In [1] is the set-up cell of Section 5.10 with `NOTEBOOK_ID = "05e"`; its comments repeat the instructions of Section 5.36. Docstrings are left out of the quotations and long captions are shortened to `...`, as before.

**In [2], the gammas, $C$, $\Gamma$, $B$ and the records.**

```python
import contextlib  # lets a block of code print into a text buffer
import io  # the text buffer io.StringIO
import sys  # sys.stdout: the channel through which the notebook prints

import numpy as np  # arrays of numbers, matrices and linear algebra

fixture = json.loads(repository_file("Revision/algebra/gammas.json")
                     .read_text(encoding="utf-8"))
COORDS = fixture["coordinates"]  # "x1", ..., "x8"
gamma = {x: np.array(m, dtype=np.int64) for x, m in zip(COORDS, fixture["gamma"])}
I16 = np.eye(16, dtype=np.int64)  # the identity matrix 1
```

The modules and the gammas, as in Notebook 05c, In [2] (Section 5.33).

```python
C = gamma["x8"] @ gamma["x1"] @ gamma["x2"] @ gamma["x3"]  # the charge matrix
Gamma = I16
for x in ["x8", "x1", "x2", "x3", "x4", "x5", "x6", "x7"]:
    Gamma = Gamma @ gamma[x]  # the chirality: the product of all eight gammas
B = -1j * (C @ gamma["x4"])  # B = -i C gamma^(x4), entries 0, +i, -i
```

$C$, $\Gamma$ and $B$; the loop multiplies the eight gammas in the author's order, starting from the identity.

```python
REPORT_FILES = {"lead": "Revision/lead_checks/reports/charge-conjugation-and-u1.json",
                "wolfram": "Revision/theory/reports/wolfram-field-theory.json"}
VERDICTS = {}  # (report key, check name) -> (verdict in lower case, detail text)
for key, path in REPORT_FILES.items():
    report_data = json.loads(repository_file(path).read_text(encoding="utf-8"))
    for entry in report_data["checks"]:
        VERDICTS[(key, entry["name"])] = (entry["verdict"].lower(), entry["detail"])
```

Two reports are read: the lead report of charge conjugation and the Wolfram report of the field theory, which holds the record's checks of the quantisation. Every check is stored under the pair (report key, check name), as in Notebook 05a (Section 5.10, In [3]).

```python
def recorded(key, name):
    return VERDICTS[(key, name)][0] == "pass"


def detail(key, name):
    return VERDICTS[(key, name)][1]


def record_of(key, name):
    return f"{REPORT_FILES[key]}, check {name}"


def check_reproduces(condition, name, record):
    collected = io.StringIO()
    with contextlib.redirect_stdout(collected):  # print into the buffer
        check(condition, name, record=record)  # stops here if the check fails
    sys.stdout.write(collected.getvalue())  # the PASS and reproduces lines together
```

The four helpers of Notebook 05b (Section 5.17, In [2]): whether a report holds a check with the verdict pass, its detail text, the text printed after reproduces, and the check that prints its two lines in one piece.

```python
say(f"{len(VERDICTS)} recorded checks were read from the two reports.")
check(np.array_equal(B.conj().T, B) and np.array_equal(B @ B, I16)
      and not np.any(np.diag(B)) and np.array_equal(B.T, -B),
      "B is Hermitian, B B = 1, B^T = -B and every diagonal entry of B is 0")
```

The printed line reports 96 checks: the 12 of the lead report and the 84 of the Wolfram report. The check confirms the facts about $B$ that Section 5.34 uses: Hermitian, square 1, $B^T = -B$, and a zero diagonal (`np.diag(B)` is the list of the diagonal entries).

**In [3], the rule of the record.**

```python
theory = json.loads(repository_file("Revision/theory/field-theory.json")
                    .read_text(encoding="utf-8"))
formula = next(f for f in theory["formulas"] if f["key"] == "quantisation")["wl"]
RULE = "{Psi_A(x), Psi^dagger_C(y)}_(x4 = y4) = B_AC delta^7(x - y)/Cos[z]"
POSITIVE = "positive representation chi = Psi^dagger B, {Psi_A, chi_C} = delta_AC"
say("the record states: " + RULE)
say("and: " + POSITIVE)
check(RULE in formula and POSITIVE in formula,
      "the formula quantisation of Revision/theory/field-theory.json states both rules")
```

The record `Revision/theory/field-theory.json` holds a list of formulas, each with a key and a text (`"wl"`, written in the notation of the Wolfram Language). `next(f for f in ... if ...)` takes the first formula whose key is `quantisation`. The two sentences that this notebook realises, the canonical rule and its positive representation with $\chi = \Psi^\dagger B$ (equivalently $\Psi^\dagger = \chi B$, because $BB = 1$), are printed, and the check confirms that the record's text contains both, character by character.

**In [4], two modes as $4 \times 4$ matrices.**

```python
def two_mode_matrix(p, filling):
    matrix = np.zeros((4, 4), dtype=np.int64)
    for n in range(4):  # the pattern n: binary digit q = occupation of mode q
        full = (n >> p) & 1  # the occupation of mode p in the pattern n
        if full != filling:  # f_p needs a full mode, f_p^* an empty one
            below = bin(n & ((1 << p) - 1)).count("1")  # occupied modes below p
            matrix[n ^ (1 << p), n] = (-1) ** below  # ^ flips binary digit p
    return matrix
```

The computer stores a pattern of occupations as a whole number $n$ whose **binary digits** are the occupations: digit $q$ (counted from 0, from the right) is the occupation of mode $q$. So for two modes $n = 0, 1, 2, 3$ are $|00\rangle$, $|10\rangle$, $|01\rangle$, $|11\rangle$. The operators on binary digits: shifting $n$ to the right by $p$ places and taking `& 1` (the last binary digit) gives the occupation of mode $p$; `1` shifted to the left by $p$ places is the number with a single 1 in digit $p$, and subtracting 1 from it gives the number with ones in all digits below $p$; `n & (...)` keeps only those digits of $n$; `bin(...)` writes a number in binary digits, and `.count("1")` counts the occupied modes below $p$. The operator `^` (exclusive or) with that single-digit number flips digit $p$. For each pattern $n$ on which the operator acts (`filling=False`: $f_p$, which needs a full mode; `filling=True`: $f_p^\ast$, which needs an empty one), column $n$ of the matrix gets the entry $(-1)^{\text{below}}$ in the row of the new pattern. Columns of patterns on which the operator gives zero stay zero.

```python
f2 = {p: two_mode_matrix(p, False) for p in (0, 1)}  # f_0, f_1
f2_star = {p: two_mode_matrix(p, True) for p in (0, 1)}  # f_0^*, f_1^*
Z4 = np.zeros((4, 4), dtype=np.int64)
relations_ok = all(
    np.array_equal(f2[p] @ f2_star[q] + f2_star[q] @ f2[p],
                   np.eye(4, dtype=np.int64) if p == q else Z4)
    and np.array_equal(f2[p] @ f2[q] + f2[q] @ f2[p], Z4)
    and np.array_equal(f2_star[p], f2[p].T)
    for p in (0, 1) for q in (0, 1))
```

The four matrices $f_0$, $f_1$, $f_0^\ast$, $f_1^\ast$, and for all four pairs $(p, q)$ the canonical relations $\{f_p, f_q^\ast\} = \delta_{pq}1$ and $\{f_p, f_q\} = 0$, and that $f_p^\ast$ is the transpose of $f_p$ (the matrices are real, so the transpose is the Hilbert adjoint).

```python
# column 3 of f_1 is the image of the pattern |11>; its entry in row 1 (|10>) is -1
say(f"f_1 applied to |11>: amplitudes on |00>, |10>, |01>, |11> = "
    f"{f2[1][:, 3].tolist()}")
check(relations_ok and all(not np.any(f2[p] @ f2[p]) for p in (0, 1)),
      "two modes: {f_p, f_q^*} = delta_pq, {f_p, f_q} = 0, f_p f_p = 0, "
      "f_p^* = f_p^T")
```

The printed line is column 3 of $f_1$, the image of $|11\rangle$: $[0, -1, 0, 0]$, that is $f_1|11\rangle = -|10\rangle$, the example of Section 5.34. The check adds $f_pf_p = 0$.

**In [5], the picture of the two-mode operators.**

```python
from matplotlib.colors import LinearSegmentedColormap

SIGNS = LinearSegmentedColormap.from_list("signs", ["#2a78d6", "#f0efec", "#e34948"])
PATTERNS = ["|00>", "|10>", "|01>", "|11>"]  # the patterns n = 0, 1, 2, 3
fig, axes = plt.subplots(1, 4, figsize=(13.0, 3.5))
```

The colour map of the heat maps, the names of the four patterns and a row of four pictures.

```python
for k, (ax, matrix, title) in enumerate(zip(
        axes, [f2[0], f2_star[0], f2[1], f2_star[1]],
        ["$f_0$ (empties mode 0)", "$f_0^*$ (fills mode 0)",
         "$f_1$ (empties mode 1)", "$f_1^*$ (fills mode 1)"])):
    image = ax.imshow(matrix, cmap=SIGNS, vmin=-1, vmax=1)
    for r in range(4):
        for c in range(4):
            if matrix[r, c]:
                ax.text(c, r, f"{matrix[r, c]:+d}", ha="center", va="center",
                        color="white", fontweight="bold")
```

For each of the four operators: its matrix as a heat map, and its nonzero entries written in their squares.

```python
    ax.set_xticks(range(4), PATTERNS)
    # the row labels only on the first picture (the rows are the same in all four)
    ax.set_yticks(range(4), PATTERNS if k == 0 else [""] * 4)
    ax.set_xlabel("from the pattern")
    if k == 0:
        ax.set_ylabel("to the pattern")
    ax.set_title(title)
    ax.grid(False)
fig.colorbar(image, ax=axes, ticks=[-1, 0, 1], shrink=0.8, label="matrix entry")
save_figure(fig, "two_modes", ...)
```

The columns are labelled by the pattern acted on, the rows by the resulting pattern (only in the first picture). **What figure 05e.1 shows**: each operator moves one pattern to another, so each picture has two coloured squares; all are red ($+1$) except one blue square in $f_1$ (from $|11\rangle$ to $|10\rangle$) and one in $f_1^\ast$ (from $|10\rangle$ to $|11\rangle$): the sign that makes operators of different modes anticommute.

**In [6], sixteen modes.**

```python
def sign_below(n, p):
    return -1 if bin(n & ((1 << p) - 1)).count("1") % 2 else 1
```

`sign_below(n, p)` is $(-1)$ to the power of the number of occupied modes below $p$ in the pattern $n$: $-1$ when that number is odd (`% 2` is its remainder after division by 2).

```python
def annihilate(p, state):
    result = {}
    for n, amplitude in state.items():
        if n >> p & 1:  # mode p is full in the pattern n
            new = n ^ (1 << p)  # the same pattern with mode p emptied
            result[new] = result.get(new, 0) + sign_below(n, p) * amplitude
    return result


def create(p, state):
    result = {}
    for n, amplitude in state.items():
        if not n >> p & 1:  # mode p is empty in the pattern n
            new = n | (1 << p)  # the same pattern with mode p filled
            result[new] = result.get(new, 0) + sign_below(n, p) * amplitude
    return result
```

With 16 modes there are 65536 patterns, too many for full matrices; a state is therefore stored as a dictionary `{pattern: amplitude}` that lists only the nonzero amplitudes. `annihilate(p, state)` is $f_p$: for every pattern in which mode $p$ is full it adds the amplitude, times the sign, to the pattern with mode $p$ emptied (`result.get(new, 0)` is the amplitude collected so far, 0 if none). `create(p, state)` is $f_p^\ast$: for every pattern in which mode $p$ is empty it fills the mode (the operator `|`, the binary or, applied with the single-digit number sets digit $p$ to 1).

```python
def combine(terms):
    result = {}
    for coefficient, state in terms:
        for n, amplitude in state.items():
            result[n] = result.get(n, 0) + coefficient * amplitude
    return result


def inner(left, right):
    return sum(np.conj(a) * right.get(n, 0) for n, a in left.items())


def largest(state):
    return max((abs(a) for a in state.values()), default=0.0)
```

`combine` adds states with coefficients, $\sum c_j\,\text{state}_j$. `inner(left, right)` is the positive inner product $\sum_n\text{left}_n^\ast\,\text{right}_n$. `largest(state)` is the largest size of an amplitude, 0 for the empty dictionary (the zero state); it measures how far a state is from zero.

```python
rng = np.random.default_rng(12345)  # random numbers with a fixed seed
RANDOM_STATE = {int(n): complex(rng.normal(), rng.normal())
                for n in rng.integers(0, 2 ** 16, size=6)}  # six random patterns
```

A random test state: six random patterns (whole numbers from 0 to 65535) with random complex amplitudes whose real and imaginary parts come from the normal distribution (the bell curve centred at 0). The fixed seed 12345 makes every run use the same numbers.

```python
worst = 0.0  # the largest violation of a canonical relation
for p in range(16):
    for q in range(16):
        mixed = combine([(1, annihilate(p, create(q, RANDOM_STATE))),
                         (1, create(q, annihilate(p, RANDOM_STATE)))])
        expected = RANDOM_STATE if p == q else {}  # delta_pq times the state
        worst = max(worst, largest(combine([(1, mixed), (-1, expected)])))
        same = combine([(1, annihilate(p, annihilate(q, RANDOM_STATE))),
                        (1, annihilate(q, annihilate(p, RANDOM_STATE)))])
        worst = max(worst, largest(same))
say(f"patterns in the random state: {len(RANDOM_STATE)}; pairs tested: 2 x 256")
check(worst < 1e-12,
      "sixteen modes: {f_p, f_q^*} = delta_pq and {f_p, f_q} = 0 on a random state")
```

For all $16 \times 16$ pairs $(p, q)$: $\{f_p, f_q^\ast\}$ applied to the random state minus $\delta_{pq}$ times the state, and $\{f_p, f_q\}$ applied to it; `worst` keeps the largest amplitude left over. The printed line reports 6 patterns and $2 \times 256$ tests; the check requires everything left over to be below $10^{-12}$.

**In [7], the mode Hamiltonian and its eigenvectors.**

```python
MASS, MOMENTUM = 3, 4  # the record's example: m = 3, momentum 4 along x1
E = float(np.sqrt(MASS ** 2 + MOMENTUM ** 2))  # the energy, 5
h = -1j * MASS * gamma["x4"] - MOMENTUM * (gamma["x4"] @ gamma["x1"])
```

The record's example: $m = 3$, momentum 4 along $x1$, $E = \sqrt{3^2 + 4^2} = 5$, and $h = -im\gamma^{(x4)} - 4\gamma^{(x4)}\gamma^{(x1)}$ (Section 5.34).

```python
def orthonormal_columns(P):
    basis = []
    for column in P.T:
        v = column.astype(complex)
        for _ in range(2):  # a second pass removes rounding errors
            for e in basis:
                v = v - (e.conj() @ v) * e  # remove the part along e
        length = np.sqrt((v.conj() @ v).real)
        if length > 1e-8:  # a new direction: keep it with length 1
            basis.append(v / length)
    return np.array(basis).T
```

The **Gram-Schmidt procedure**: it goes through the columns of a matrix $P$ (the rows of `P.T`), subtracts from each column its parts along the columns already kept ($e^\dagger v$ is the size of the part of $v$ along the unit column $e$), and keeps it, divided by its length, when the length that remains is not zero. The subtraction is done twice, because the first pass leaves rounding errors. The kept columns are orthonormal (of length 1 and perpendicular to each other) and span the same space as the columns of $P$.

```python
U_plus = orthonormal_columns((np.eye(16) + h / E) / 2)  # u_1..u_8: energy +5
V_minus = orthonormal_columns((np.eye(16) - h / E) / 2)  # v_1..v_8: energy -5
W = np.hstack([U_plus, V_minus])  # 16 x 16: the columns u_1..u_8, v_1..v_8
report("E for m = 3 and momentum 4 along x1", f"{E:.12f}")
```

Because $hh = E^2\,1$, the matrices $\tfrac12(1 \pm h/E)$ are projectors onto the eigenvectors with the eigenvalues $\pm E$: $h\cdot\tfrac12(1 + h/E) = \tfrac12(h + E\,1) = E\cdot\tfrac12(1 + h/E)$, so every column of the first is an eigenvector with eigenvalue $+E$ (or zero), and in the same way for the second with $-E$. Gram-Schmidt picks eight orthonormal columns from each; `np.hstack` puts them side by side into $W$. The RESULT line prints $E = 5.000000000000$.

```python
check(np.max(np.abs(h - h.conj().T)) < 1e-15
      and np.max(np.abs(h @ h - 25 * np.eye(16))) < 1e-13
      and U_plus.shape == (16, 8) and V_minus.shape == (16, 8)
      and np.max(np.abs(h @ U_plus - E * U_plus)) < 1e-13
      and np.max(np.abs(h @ V_minus + E * V_minus)) < 1e-13
      and np.max(np.abs(W.conj().T @ W - np.eye(16))) < 1e-13
      and np.max(np.abs(W @ W.conj().T - np.eye(16))) < 1e-13,
      "h is Hermitian, h h = 25, with 8 + 8 orthonormal complete eigenvectors")
```

The check: $h$ is Hermitian, $hh = 25\cdot1$, eight columns for each energy, $hu_s = 5u_s$ and $hv_s = -5v_s$, and $W^\dagger W = WW^\dagger = 1$ (orthonormal and complete), each to a small floating-point tolerance.

**In [8], the field operators and the canonical rule.**

```python
def basic(i, state):
    p = i % 16  # the mode
    empties = (i < 16) == (p < 8)  # F_p for p < 8 and F_p^* for p >= 8 empty mode p
    return annihilate(p, state) if empties else create(p, state)
```

Every operator used here is a combination of 32 **basic operators** $O_i$: $O_p = F_p$ and $O_{16+p} = F_p^\ast$ for $p = 0, \dots, 15$, where $F_p = b_{p+1} = f_p$ for $p < 8$ (particles) and $F_p = d_{p-7}^\ast = f_p^\ast$ for $p \geq 8$ (antiparticles appear in $\Psi$ through their creation operators), and $F_p^\ast$ is the Hilbert adjoint of $F_p$. `basic(i, state)` applies $O_i$: the mode is $p = i \bmod 16$, and $O_i$ empties mode $p$ exactly when ($i < 16$ and $p < 8$) or ($i \geq 16$ and $p \geq 8$), which is what the comparison of the two truth values `(i < 16) == (p < 8)` says.

```python
ZEROS = np.zeros((16, 16))
PSI = np.hstack([W, ZEROS])  # row A: Psi_A = sum_p W_Ap F_p
CHI = np.hstack([ZEROS, W.conj()])  # row A: chi_A = sum_p conj(W_Ap) F_p^*
PSI_DAG = B.T @ CHI  # row A: Psi^dagger_A = sum_C chi_C B_CA
```

An operator $\sum_ic_iO_i$ is stored as the row of its 32 coefficients. The field $\Psi_A = \sum_pW_{Ap}F_p$ (Section 5.34 with the columns of $W$) is row $A$ of `PSI`: the 16 numbers $W_{A,p}$ followed by 16 zeros. Its Hilbert adjoint $\chi_A = \sum_pW^\ast_{Ap}F_p^\ast$ is row $A$ of `CHI`. The canonical conjugate $\Psi^\dagger_A = \sum_C\chi_CB_{CA} = \sum_C(B^T)_{AC}\chi_C$ is row $A$ of $B^T$ times `CHI`.

```python
def apply(row, state):
    return combine([(row[i], basic(i, state)) for i in range(32)
                    if abs(row[i]) > 1e-15])


def anticommutator(row1, row2, state):
    return combine([(1, apply(row1, apply(row2, state))),
                    (1, apply(row2, apply(row1, state)))])
```

`apply(row, state)` applies the operator of a row to a state (coefficients below $10^{-15}$ are skipped). `anticommutator(row1, row2, state)` applies $\{X, Y\} = XY + YX$.

```python
def measured_rule(rows1, rows2, state):
    norm = inner(state, state).real
    numbers = np.zeros((16, 16), dtype=complex)
    rest = 0.0
    for A in range(16):
        for C_ in range(16):
            result = anticommutator(rows1[A], rows2[C_], state)
            numbers[A, C_] = inner(state, result) / norm
            rest = max(rest, largest(combine([(1, result),
                                              (-numbers[A, C_], state)])))
    return numbers, rest
```

`measured_rule` measures the 256 anticommutators $\{X_A, Y_C\}$ on a state. Each must be a number times the state; the number is read off as $\langle\phi|\{X, Y\}\phi\rangle/\langle\phi|\phi\rangle$, and `rest` keeps the largest amplitude left over after that number times the state is subtracted (it must be zero). The letter `C_` avoids overwriting the matrix `C`.

```python
with_chi, rest_chi = measured_rule(PSI, CHI, RANDOM_STATE)
with_dagger, rest_dagger = measured_rule(PSI, PSI_DAG, RANDOM_STATE)
psi_psi, rest_pp = measured_rule(PSI, PSI, RANDOM_STATE)
dag_dag, rest_dd = measured_rule(PSI_DAG, PSI_DAG, RANDOM_STATE)
all_rest = max(rest_chi, rest_dagger, rest_pp, rest_dd)
say("every anticommutator is a number times the state (rest below 1e-12): "
    f"{all_rest < 1e-12}")
```

Four families of anticommutators are measured on the random state: $\{\Psi_A, \chi_C\}$, $\{\Psi_A, \Psi^\dagger_C\}$, $\{\Psi_A, \Psi_C\}$ and $\{\Psi^\dagger_A, \Psi^\dagger_C\}$. The printed line says True: each is a number times the state.

```python
check_reproduces(np.max(np.abs(with_chi - np.eye(16))) < 1e-12
                 and np.max(np.abs(with_dagger - B)) < 1e-12
                 and np.max(np.abs(psi_psi)) < 1e-12
                 and np.max(np.abs(dag_dag)) < 1e-12 and all_rest < 1e-12
                 and recorded("wolfram", "Fock_space_good_sector_example"),
                 "{Psi_A, chi_C} = delta_AC and {Psi_A, Psi^dagger_C} = B_AC on the "
                 "positive Fock space; {Psi, Psi} = 0 = {Psi^dagger, Psi^dagger}",
                 record=record_of("wolfram", "Fock_space_good_sector_example"))
```

The check: the measured numbers are the identity for $\chi$, the matrix $B$ for $\Psi^\dagger$, and zero for the other two families, exactly as Section 5.34 derived.

**In [9], the picture of the measured rules.**

```python
def heat_map(ax, matrix, title, row_label=True):
    image = ax.imshow(matrix, cmap=SIGNS, vmin=-1, vmax=1)
    ax.set_title(title)
    ax.set_xticks([0, 3, 7, 11, 15], ["1", "4", "8", "12", "16"])
    ax.set_yticks([0, 3, 7, 11, 15], ["1", "4", "8", "12", "16"])
    ax.axhline(7.5, color="black", linewidth=0.8)
    ax.axvline(7.5, color="black", linewidth=0.8)
    ax.set_xlabel("column")
    if row_label:
        ax.set_ylabel("row")
    ax.grid(False)
    return image
```

The heat map of Notebook 05c, In [4].

```python
check(np.max(np.abs(with_chi.imag)) < 1e-12 and np.max(np.abs(with_dagger.real))
      < 1e-12, "the measured numbers are real for chi and imaginary for Psi^dagger")
fig, axes = plt.subplots(1, 3, figsize=(11.0, 4.0))
heat_map(axes[0], with_chi.real, r"measured $\{\Psi_A, \chi_C\}$")
heat_map(axes[1], with_dagger.imag, r"measured $\{\Psi_A, \Psi^\dagger_C\}$ / $i$",
         row_label=False)
image = heat_map(axes[2], B.imag, r"the matrix $B$ / $i$", row_label=False)
fig.colorbar(image, ax=axes, ticks=[-1, 0, 1], shrink=0.8, label="matrix entry")
save_figure(fig, "anticommutators", ...)
```

Before drawing, the check confirms what the pictures show: the numbers for $\chi$ are real and those for $\Psi^\dagger$ purely imaginary, so the real part of the first and the imaginary part of the second say everything. **What figure 05e.2 shows**: on the left the identity (a red diagonal); in the middle and on the right the same pattern of red and blue squares, $B/i$, with an empty diagonal. The realisation obeys the canonical rule.

**In [10], why the canonical conjugate is not the Hilbert adjoint.**

```python
u = np.zeros(16, dtype=complex)
u[6], u[15] = -1j / np.sqrt(2), 1 / np.sqrt(2)  # u_7 and u_16 (Python counts from 0)
X_row = u.conj() @ PSI  # X = sum_A conj(u_A) Psi_A
X_adjoint = u @ CHI  # X^* = sum_A u_A chi_A (the Hilbert adjoint)
X_dagger = u @ PSI_DAG  # X^dagger = sum_A u_A Psi^dagger_A (canonical conjugate)
```

The record's column $u$ ($u_7 = -i/\sqrt2$, $u_{16} = 1/\sqrt2$), the operator $X = \sum_Au_A^\ast\Psi_A$ as a row (a combination of the rows of `PSI`), its Hilbert adjoint $X^\ast = \sum_Au_A\chi_A$ and its canonical conjugate $X^\dagger = \sum_Au_A\Psi^\dagger_A$.

```python
norm_random = inner(RANDOM_STATE, RANDOM_STATE).real
with_adjoint = inner(RANDOM_STATE, anticommutator(X_row, X_adjoint,
                                                  RANDOM_STATE)) / norm_random
with_canonical = inner(RANDOM_STATE, anticommutator(X_row, X_dagger,
                                                    RANDOM_STATE)) / norm_random
eigen_B = np.linalg.eigvalsh(B)  # the 16 eigenvalues of the Hermitian matrix B
say(f"{{X, X^*}} = {with_adjoint.real:+.6f};  {{X, X^dagger}} = "
    f"{with_canonical.real:+.6f};  u^dagger B u = {(u.conj() @ B @ u).real:+.6f}")
```

The two anticommutators are measured on the random state as numbers, and the 16 eigenvalues of $B$ are computed. In an f-string a doubled brace `{{` prints a single brace. The printed line shows $\{X, X^\ast\} = +1.000000$, $\{X, X^\dagger\} = -1.000000$ and $u^\dagger Bu = -1.000000$.

```python
check_reproduces(np.allclose(B @ u, -u) and abs(u.conj() @ B @ u + 1) < 1e-12
                 and abs(with_adjoint - 1) < 1e-12 and abs(with_canonical + 1) < 1e-12
                 and recorded("wolfram", "no_positive_inner_product"),
                 "{X, X^*} = +1 but {X, X^dagger} = u^dagger B u = -1: the canonical "
                 "conjugate needs an indefinite (Krein) inner product",
                 record=record_of("wolfram", "no_positive_inner_product"))
```

The check: $Bu = -u$, $u^\dagger Bu = -1$, the anticommutator with the Hilbert adjoint is $+1$ (positive, as it must be), and the canonical one is $-1$: the argument of Section 5.34 on the computer.

**In [11], the picture of the indefinite form.**

```python
fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.0))
axes[0].plot(np.arange(1, 17), eigen_B, "o", color="#2a78d6", markersize=8)
axes[0].axhline(0.0, color="black", linewidth=0.8)
axes[0].set_xticks([1, 4, 8, 12, 16])
axes[0].set_xlabel("number of the eigenvalue (sorted)")
axes[0].set_ylabel("eigenvalue of $B$")
axes[0].set_title("$B$: eight eigenvalues $-1$, eight $+1$")
```

The left picture: the 16 sorted eigenvalues of $B$ as dots.

```python
axes[1].bar([0, 1], [with_adjoint.real, with_canonical.real],
            color=["#1baf7a", "#eb6834"], edgecolor="white", linewidth=2, width=0.5)
for x_bar, value in zip([0, 1], [with_adjoint.real, with_canonical.real]):
    axes[1].text(x_bar, value + (0.08 if value > 0 else -0.16), f"{value:+.0f}",
                 ha="center")
axes[1].axhline(0.0, color="black", linewidth=0.8)
axes[1].set_xticks([0, 1], [r"$\{X, X^*\}$ (Hilbert adjoint)",
                            r"$\{X, X^\dagger\}$ (canonical)"])
axes[1].set_ylim(-1.5, 1.5)
axes[1].set_ylabel("measured number")
axes[1].set_title("$X = u^\\dagger\\Psi$ with $Bu = -u$")
save_figure(fig, "why_krein", ...)
```

The right picture: two bars with their values written beside them. **What figure 05e.3 shows**: on the left eight dots at $-1$ and eight at $+1$, the signature $(8, 8)$ of $B$; on the right a green bar up to $+1$ (the Hilbert adjoint) and an orange bar down to $-1$ (the canonical conjugate). A negative value is impossible for a Hilbert adjoint, which is why the canonical rule needs an indefinite (Krein) inner product.

**In [12], the vacuum, the 16 quanta and the expectation-value rule.**

```python
VACUUM = {0: 1.0}  # the pattern 0: no particle, no antiparticle


def bilinear(L, K, R, state):
    Q = L.T @ K @ R  # 32 x 32: the coefficient of O_i O_j
    terms = []
    for j in range(32):
        if np.max(np.abs(Q[:, j])) > 1e-15:
            lowered = basic(j, state)  # O_j applied first
            if lowered:
                terms += [(Q[i, j], basic(i, lowered)) for i in range(32)
                          if abs(Q[i, j]) > 1e-15]
    return combine(terms)
```

The vacuum is the pattern 0 with amplitude 1. A bilinear $\sum_{A,C}L_AK_{AC}R_C$ of two operators given by rows $L_A$ and $R_C$ is $\sum_{i,j}Q_{ij}O_iO_j$ with the $32 \times 32$ matrix $Q = L^TKR$ (insert $L_A = \sum_iL_{Ai}O_i$ and $R_C = \sum_jR_{Cj}O_j$). `bilinear(L, K, R, state)` applies it to a state: for each $j$ with a nonzero column of $Q$ it applies $O_j$ first, and if the result is not the zero state (an empty dictionary counts as false), it applies every $O_i$ with its coefficient.

```python
def vacuum_value(L, K, R):
    return inner(VACUUM, bilinear(L, K, R, VACUUM))


QUANTA = [create(p, VACUUM) for p in range(16)]  # b_s^*|0> (p < 8), d_s^*|0>


def normal_ordered_value(L, K, R, state):
    return inner(state, bilinear(L, K, R, state)) - vacuum_value(L, K, R)
```

`vacuum_value` is $\langle 0|X|0\rangle$. `QUANTA` lists the 16 one-quantum states: filling mode $p$ of the vacuum gives $b_{p+1}^\ast|0\rangle$ for $p < 8$ and $d_{p-7}^\ast|0\rangle$ for $p \geq 8$. `normal_ordered_value` is $\langle q|X|q\rangle - \langle 0|X|0\rangle$, the value of $:\!X\!:$ in a state $q$ of length 1.

```python
vacuum_energy = vacuum_value(CHI, h, PSI)
energies = np.array([normal_ordered_value(CHI, h, PSI, q) for q in QUANTA])
vacuum_charge = vacuum_value(PSI_DAG, B, PSI)
charges = np.array([normal_ordered_value(PSI_DAG, B, PSI, q) for q in QUANTA])
report("vacuum energy <0|chi h Psi|0> (the filled sea)", f"{vacuum_energy.real:.6f}")
report("vacuum charge <0|Psi^dagger B Psi|0>", f"{vacuum_charge.real:.6f}")
say("normal-ordered energies of the 16 quanta: "
    + " ".join(f"{e.real:+.0f}" for e in energies))
say("normal-ordered charges of the 16 quanta:  "
    + " ".join(f"{c.real:+.0f}" for c in charges))
```

The energy operator is $\chi h\Psi$ and the charge operator $\Psi^\dagger B\Psi$ (which equals $\chi BB\Psi = \chi\Psi$). The RESULT lines print the vacuum energy $-40.000000$ ($-8E$, the filled sea) and the vacuum charge $8.000000$; the two printed lists show the normal-ordered energy $+5$ for all 16 quanta, and the charge $+1$ for the eight particles and $-1$ for the eight antiparticles.

```python
rule_ok = True
for K_rule in [C, -1j * (C @ gamma["x4"]), -1j * (C @ gamma["x1"])]:
    values = [normal_ordered_value(PSI_DAG, K_rule, PSI, q) for q in QUANTA]
    predicted = ([W[:, s].conj() @ B @ K_rule @ W[:, s] for s in range(8)]
                 + [-(W[:, s].conj() @ B @ K_rule @ W[:, s]) for s in range(8, 16)])
    rule_ok &= np.max(np.abs(np.array(values) - np.array(predicted))) < 1e-12
```

The expectation-value rule of the record: $\langle q|:\!\Psi^\dagger K\Psi\!:|q\rangle = u_s^\dagger BKu_s$ for a particle and $-v_s^\dagger BKv_s$ for an antiparticle (`W[:, s]` is column $s$ of $W$), tested for three of the record's matrices: the scalar, the charge density and the current along $x1$. `&=` keeps `rule_ok` true only while every test passes.

```python
check_reproduces(abs(vacuum_energy + 40) < 1e-12 and np.max(np.abs(energies - 5)) < 1e-12
                 and abs(vacuum_charge - 8) < 1e-12
                 and np.max(np.abs(charges - np.array([1] * 8 + [-1] * 8))) < 1e-12
                 and rule_ok and "-8 E" in detail("wolfram",
                                                  "Fock_space_good_sector_example"),
                 "vacuum energy -40, every quantum +5, charges +1 and -1, and the "
                 "expectation-value rule for M = C, -i C gamma^(x4), -i C gamma^(x1)",
                 record=record_of("wolfram", "Fock_space_good_sector_example"))
```

The check collects the numbers and requires that the record's detail text contains `-8 E`, the vacuum energy it states.

**In [13], the picture of the quanta.**

```python
raw_energies = energies + vacuum_energy  # <q|chi h Psi|q>
raw_charges = charges + vacuum_charge  # <q|Psi^dagger B Psi|q>
index = np.arange(1, 17)
fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2))
```

The values in the states before normal ordering are the normal-ordered values plus the vacuum values.

```python
for ax, raw, ordered, name in [(axes[0], raw_energies, energies, "energy"),
                               (axes[1], raw_charges, charges, "charge")]:
    ax.bar(index - 0.2, raw.real, 0.4, color="#9e9c98", label="value in the state")
    ax.bar(index + 0.2, ordered.real, 0.4, color="#2a78d6",
           label="after normal ordering")
    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.axvline(8.5, color="black", linewidth=0.8, linestyle=":")
    ax.set_xticks([1, 4, 8, 9, 12, 16])
    ax.set_xlabel("quantum: 1 to 8 particles, 9 to 16 antiparticles")
    ax.set_title(f"the {name} of the 16 quanta")
axes[0].set_ylabel("value")
handles, names = axes[0].get_legend_handles_labels()  # one legend for both
fig.legend(handles, names, loc="lower center", bbox_to_anchor=(0.5, -0.1), ncol=2)
save_figure(fig, "quanta", ...)
```

For the energy (left) and the charge (right), a grey bar (value in the state) and a blue bar (after normal ordering) for each quantum, and a dotted line between particles and antiparticles; one legend for both pictures (`get_legend_handles_labels` collects the labelled bars of the first picture). **What figure 05e.4 shows**: the grey energy bars at $-35$ ($= -40 + 5$) and the blue ones at $+5$; the grey charge bars at $9$ for particles and $7$ for antiparticles, the blue ones at $+1$ and $-1$. The student should see that the vacuum values are large and that normal ordering subtracts them, leaving the physical numbers.

**In [14], the two conjugations of the operators.**

```python
MAPS = {"M = 1": I16, "M = Gamma": Gamma}  # the two conjugation matrices
conjugated = {}  # name -> (rows of Psi', rows of Psi'^dagger)
measured_conjugated = {}  # name -> the measured {Psi'_A, Psi'^dagger_C}
```

The two maps of Section 5.34 and two dictionaries for the results.

```python
for name, M in MAPS.items():
    rows_prime = M @ PSI_DAG  # Psi'_A = sum_C M_AC Psi^dagger_C
    rows_prime_dagger = M.conj() @ PSI  # Psi'^dagger_A = sum_C conj(M_AC) Psi_C
    conjugated[name] = (rows_prime, rows_prime_dagger)
    numbers, rest = measured_rule(rows_prime, rows_prime_dagger, RANDOM_STATE)
    measured_conjugated[name] = numbers
    predicted = M @ B.T @ M.conj().T
    say(f"{name:9}: measured equals M B^T M^dagger: "
        f"{np.max(np.abs(numbers - predicted)) < 1e-12 and rest < 1e-12}; "
        f"it equals +B: {np.max(np.abs(numbers - B)) < 1e-12}; "
        f"-B: {np.max(np.abs(numbers + B)) < 1e-12}")
```

For each map the rows of the conjugated field and of its canonical conjugate are formed (a matrix times the rows gives the rows of the combinations), the 256 anticommutators are measured on the random state and compared with the prediction $MB^TM^\dagger$. The two printed lines: for $M = 1$ the measurement equals the prediction and $-B$; for $M = \Gamma$ it equals the prediction and $+B$.

```python
check_reproduces(np.max(np.abs(measured_conjugated["M = 1"] + B)) < 1e-12
                 and np.max(np.abs(measured_conjugated["M = Gamma"] - B)) < 1e-12
                 and recorded("lead", "quantum_charge_conjugation_unitary_type"),
                 "on the Fock space: Psi' = Psi^(dagger T) gives -B, Psi' = Gamma "
                 "Psi^(dagger T) gives +B: only M = Gamma keeps the canonical rule",
                 record=record_of("lead", "quantum_charge_conjugation_unitary_type"))
```

The check reproduces the lead check on actual operators: only $M = \Gamma$ keeps the canonical rule.

**In [15], the picture of the conjugated rules.**

```python
fig, axes = plt.subplots(1, 3, figsize=(11.0, 4.0))
heat_map(axes[0], B.imag, r"$B$ / $i$ (the rule)")
heat_map(axes[1], measured_conjugated["M = 1"].imag,
         r"measured, $M = 1$, / $i$", row_label=False)
image = heat_map(axes[2], measured_conjugated["M = Gamma"].imag,
                 r"measured, $M = \Gamma$, / $i$", row_label=False)
fig.colorbar(image, ax=axes, ticks=[-1, 0, 1], shrink=0.8, label="matrix entry")
save_figure(fig, "conjugated_rules", ...)
```

**What figure 05e.5 shows**: the rule $B/i$ on the left; in the middle, measured for $M = 1$, every colour reversed ($-B$); on the right, measured for $M = \Gamma$, the same picture as on the left. Only $\Gamma$ gives a conjugation of the quantised field.

**In [16], the conjugated bilinears: a sign and a constant.**

```python
K_MATRICES = {"S": C.astype(complex)}  # the scalar S = Psi^dagger C Psi
for x in COORDS:
    K_MATRICES[f"J^({x})"] = -1j * (C @ gamma[x])  # the current J^a
BILINEAR_NAMES = list(K_MATRICES)  # "S", "J^(x1)", ..., "J^(x8)"
signs, constants = {}, {}  # (map, bilinear) -> s and c
identity_ok = True
```

The nine matrices: the scalar and the eight currents, under their names.

```python
for map_name, M in MAPS.items():
    rows_prime, rows_prime_dagger = conjugated[map_name]
    for bname, K in K_MATRICES.items():
        K_prime = M.conj().T @ K @ M  # K' = M^dagger K M
        c = np.trace(K_prime @ B.T)  # the predicted constant
        s = 1 if np.array_equal(-K_prime.T, K) else (
            -1 if np.array_equal(-K_prime.T, -K) else 0)  # -K'^T = s K
        X_prime = bilinear(rows_prime_dagger, K, rows_prime, RANDOM_STATE)
        X = bilinear(PSI_DAG, K, PSI, RANDOM_STATE)
        difference = combine([(1, X_prime), (-s, X), (-c, RANDOM_STATE)])
        identity_ok &= s != 0 and largest(difference) < 1e-10
        signs[(map_name, bname)], constants[(map_name, bname)] = s, c
```

For each map and each of the nine bilinears: the predicted constant $c = \mathrm{tr}(K'B^T)$ and the predicted sign $s$ with $-K'^T = sK$ (Section 5.34); then the conjugated operator $X' = \Psi'^\dagger K\Psi'$ and the original $X = \Psi^\dagger K\Psi$ are applied to the random state, and the state $X'\phi - sX\phi - c\,\phi$ must vanish. `identity_ok` stays true only if every sign is $\pm1$ and every difference is below $10^{-10}$.

```python
for map_name in MAPS:
    say(f"{map_name:9}: s = " + " ".join(f"{signs[(map_name, b)]:+d}"
                                        for b in BILINEAR_NAMES)
        + "  (S, J^(x1), ..., J^(x8))")
    say(f"{'':9}  c = " + " ".join(f"{constants[(map_name, b)].real:+.0f}"
                                   for b in BILINEAR_NAMES))
```

Two lines per map: the nine signs and the nine constants (in the second line the empty string, padded to nine characters, prints nine blanks, so that the two lines line up). The printed result: for $M = 1$ the signs $-1$ for $S$ and $+1$ for all eight currents, for $M = \Gamma$ the sign $-1$ for all nine; the constants are 0 except $-16$ ($M = 1$) and $+16$ ($M = \Gamma$) for $J^{(x4)}$.

```python
lead_detail = detail("lead", "bilinears_under_charge_conjugation")
recorded_table = json.loads(lead_detail.split("measured: ", 1)[1])
anticommuting_rows = {"M = 1": recorded_table["plus,eps=-1"],
                      "M = Gamma": recorded_table["minus,eps=-1"]}
rows_agree = all([signs[(m_name, "S")], [signs[(m_name, b)] for b in
                                         BILINEAR_NAMES[1:]]] == row
                 for m_name, row in anticommuting_rows.items())
```

The record's measured table is read as in Notebook 05c, In [14]; its two anticommuting rows (keys `plus,eps=-1` and `minus,eps=-1`) are compared with the operator signs, written in the same shape [sign of $S$, list of the eight signs of the currents].

```python
check(identity_ok, "X' = s X + c holds on the Fock space for all 9 bilinears and both "
      "maps, with c = tr(K' B^T)")
check_reproduces(rows_agree and recorded("lead", "bilinears_under_charge_conjugation"),
                 "the operator signs s equal the measured signs of the anticommuting "
                 "rows (eps = -1) of the recorded table",
                 record=record_of("lead", "bilinears_under_charge_conjugation"))
```

Two checks: the operator identity $X' = sX + c$ (the derivation of Section 5.34, confirmed on the Fock space), and that the operator signs are those of the record's anticommuting rows.

**In [17], the constants and the vacuum values.**

```python
nonzero = sorted({b for (m_name, b), c in constants.items() if abs(c) > 1e-12})
check(nonzero == ["J^(x4)"] and abs(constants[("M = 1", "J^(x4)")] + 16) < 1e-12
      and abs(constants[("M = Gamma", "J^(x4)")] - 16) < 1e-12,
      "c = 0 except for the charge density J^(x4): c = -16 (M = 1), +16 (M = Gamma)")
```

The set of bilinears with a nonzero constant (sorted, so that the printed order never changes) must be the charge density alone, with $c = -16$ and $+16$, as Section 5.34 computed.

```python
vac_original = {b: vacuum_value(PSI_DAG, K, PSI) for b, K in K_MATRICES.items()}
vac_conjugated = {}  # (map, bilinear) -> <0|X'|0>
for map_name in MAPS:
    rows_prime, rows_prime_dagger = conjugated[map_name]
    for bname, K in K_MATRICES.items():
        vac_conjugated[(map_name, bname)] = vacuum_value(rows_prime_dagger, K,
                                                         rows_prime)
```

The vacuum values $\langle 0|X|0\rangle$ of the nine original bilinears and $\langle 0|X'|0\rangle$ of the 18 conjugated ones.

```python
# values below 1e-12 are printed as 0 (rounding could otherwise print "-0.00")
shown = {b: (v.real if abs(v) > 1e-12 else 0.0) for b, v in vac_original.items()}
say("vacuum values <0|X|0>: " + ", ".join(f"{b} {shown[b]:+.2f}"
                                         for b in BILINEAR_NAMES))
check(all(abs(vac_conjugated[key] - signs[key] * vac_original[key[1]]
              - constants[key]) < 1e-12 for key in vac_conjugated),
      "<0|X'|0> = s <0|X|0> + c for all 9 bilinears and both maps")
```

The printed line lists the vacuum values: $S$ $-4.80$, $J^{(x1)}$ $-6.40$, $J^{(x4)}$ $+8.00$ and 0 for the others; the filled sea of the example has a nonzero scalar and a nonzero current along its momentum $x1$. The check: $\langle 0|X'|0\rangle = s\langle 0|X|0\rangle + c$ for all 18 cases (`key[1]` is the name of the bilinear in the pair `key`).

```python
positions = np.arange(len(BILINEAR_NAMES))
labels = ["$S$"] + [rf"$J^{{({x})}}$" for x in COORDS]
fig, axes = plt.subplots(1, 2, figsize=(12.0, 4.2), sharey=True)
for ax, map_name, title in [(axes[0], "M = 1", r"$\Psi' = \Psi^{\dagger T}$"),
                            (axes[1], "M = Gamma",
                             r"$\Psi' = \Gamma\Psi^{\dagger T}$")]:
    ax.bar(positions - 0.27, [vac_original[b].real for b in BILINEAR_NAMES], 0.27,
           color="#9e9c98", label=r"$\langle 0|X|0\rangle$")
    ax.bar(positions, [vac_conjugated[(map_name, b)].real for b in BILINEAR_NAMES],
           0.27, color="#2a78d6", label=r"$\langle 0|X'|0\rangle$")
    ax.bar(positions + 0.27, [constants[(map_name, b)].real for b in BILINEAR_NAMES],
           0.27, color="#eb6834", label="the constant $c$")
    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.set_xticks(positions, labels)
    ax.set_title(title)
    ax.legend(loc="lower left")
axes[0].set_ylabel("value")
save_figure(fig, "vacuum_values", ...)
```

For each map, three bars per bilinear: the vacuum value before (grey) and after (blue) the conjugation, and the constant $c$ (orange). **What figure 05e.6 shows**: for $M = 1$ the scalar's vacuum value changes from $-4.8$ to $+4.8$, that of $J^{(x1)}$ stays at $-6.4$, and that of $J^{(x4)}$ goes from $8$ to $8 - 16 = -8$; for $M = \Gamma$ all signs flip, and $J^{(x4)}$ goes from $8$ to $-8 + 16 = 8$. The orange bars appear only at $J^{(x4)}$. Normal ordering subtracts each operator's own vacuum value, which removes $c$.

**In [18], after normal ordering.**

```python
def apply_normal_ordered(L, K, R, state):
    return combine([(1, bilinear(L, K, R, state)),
                    (-vacuum_value(L, K, R), state)])
```

`apply_normal_ordered` applies $:\!X\!: = X - \langle 0|X|0\rangle$ to a state.

```python
normal_ok = True
for map_name in MAPS:
    rows_prime, rows_prime_dagger = conjugated[map_name]
    for bname, K in K_MATRICES.items():
        for state in [RANDOM_STATE] + QUANTA:
            left = apply_normal_ordered(rows_prime_dagger, K, rows_prime, state)
            right = apply_normal_ordered(PSI_DAG, K, PSI, state)
            normal_ok &= largest(combine([(1, left),
                                          (-signs[(map_name, bname)], right)])) < 1e-10
check(normal_ok, ":X': = s :X: for all 9 bilinears, both maps, on the random state "
      "and the 16 quanta")
```

For both maps, all nine bilinears and 17 states (the random state and the 16 quanta) the cell compares $:\!X'\!:$ applied to the state with $s$ times $:\!X\!:$ applied to it. The check: normal ordering removes the constant and keeps the sign, everywhere.

```python
def classical_sign(M, K, eps):
    new = eps * (M.conj().T @ K @ M).T
    return 1 if np.array_equal(new, K) else (-1 if np.array_equal(new, -K) else 0)


tables = {"commuting components (classical)": 1,
          "anticommuting components (classical)": -1}
grids = {}
for title, eps in tables.items():
    grids[title] = np.array([[classical_sign(M, K_MATRICES[b], eps)
                              for b in BILINEAR_NAMES] for M in MAPS.values()])
grids["quantised field after normal ordering"] = np.array(
    [[signs[(m_name, b)] for b in BILINEAR_NAMES] for m_name in MAPS])
```

`classical_sign` is `sign_of` of Notebook 05c: the classical rule $K' = \epsilon(M^\dagger KM)^T$. Three tables of two rows (the maps) and nine columns (the bilinears) are built: classical commuting, classical anticommuting, and the operator signs of the quantised field.

```python
check(np.array_equal(grids["quantised field after normal ordering"],
                     grids["anticommuting components (classical)"])
      and np.array_equal(grids["commuting components (classical)"],
                         -grids["anticommuting components (classical)"]),
      "after normal ordering the quantised field has the signs of the anticommuting "
      "components; the commuting ones are the opposite")
```

The check: the quantised table equals the classical anticommuting one, and the commuting one is its opposite.

```python
fig, axes = plt.subplots(3, 1, figsize=(9.0, 6.6))
for ax, (title, grid) in zip(axes, grids.items()):
    ax.imshow(grid, cmap=SIGNS, vmin=-1, vmax=1, aspect="auto")
    for r in range(2):
        for c_col in range(9):
            ax.text(c_col, r, f"{grid[r, c_col]:+d}", ha="center", va="center",
                    color="white", fontweight="bold")
    ax.axhline(0.5, color="white", linewidth=2)
    for k in range(1, 9):
        ax.axvline(k - 0.5, color="white", linewidth=3 if k == 1 else 2)
    ax.set_xticks(range(9), labels)
    ax.set_yticks([0, 1], [r"$\mathcal{C}_+$ type, $M = 1$",
                           r"$\mathcal{C}_-$ type, $M = \Gamma$"])
    ax.set_title(title)
    ax.grid(False)
fig.tight_layout()
save_figure(fig, "sign_tables", ...)
```

Three sign tables, one above the other, drawn as in Notebook 05c, In [15] (`c_col` is used as the column counter, because `c` already names a constant); `fig.tight_layout()` spaces the three pictures so that their labels do not overlap. **What figure 05e.7 shows**: the top table (commuting) has a red $S$ and blue currents for $M = 1$ and is all red for $M = \Gamma$; the middle (anticommuting) and the bottom (quantised field after normal ordering) are equal, each the top table with every colour reversed. Normal ordering adds no sign.

**In [19], the charges of the quanta after the conjugation.**

```python
K_charge = K_MATRICES["J^(x4)"]  # equal to B
charge_values = {"original": charges.real}
for map_name in MAPS:
    rows_prime, rows_prime_dagger = conjugated[map_name]
    charge_values[map_name] = np.array(
        [normal_ordered_value(rows_prime_dagger, K_charge, rows_prime, q).real
         for q in QUANTA])
check(np.array_equal(K_charge, B)
      and np.max(np.abs(charge_values["M = Gamma"] + charges.real)) < 1e-12
      and np.max(np.abs(charge_values["M = 1"] - charges.real)) < 1e-12,
      "M = Gamma reverses the normal-ordered charge of every quantum; M = 1 keeps it")
```

The normal-ordered charge density of the conjugated field, $:\!J'^{(x4)}\!:$, is evaluated in each of the 16 one-quantum states, for both maps. The check: its matrix is $B$; with $M = \Gamma$ (the allowed conjugation) every charge is reversed, particles $+1 \to -1$ and antiparticles $-1 \to +1$; with $M = 1$ (which breaks the canonical rule) every charge stays.

```python
fig, ax = plt.subplots(figsize=(8.0, 4.2))
ax.plot(index, charge_values["original"], "o", color="#9e9c98", markersize=12,
        label=r"$:\!J^{(x4)}\!:$ (the field)")
ax.plot(index, charge_values["M = 1"], "s", color="#eb6834", markersize=6,
        label=r"$M = 1$ (breaks the rule)")
ax.plot(index, charge_values["M = Gamma"], "D", color="#2a78d6", markersize=7,
        label=r"$M = \Gamma$ (keeps the rule)")
ax.axhline(0.0, color="black", linewidth=0.8)
ax.axvline(8.5, color="black", linewidth=0.8, linestyle=":")
ax.set_xticks([1, 4, 8, 9, 12, 16])
ax.set_ylim(-1.6, 1.6)
ax.set_xlabel("quantum: 1 to 8 particles, 9 to 16 antiparticles")
ax.set_ylabel("normal-ordered charge")
ax.set_title("The charge of each quantum, and of its conjugates")
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.17), ncol=3)
save_figure(fig, "conjugated_charges", ...)
```

Large grey circles for the field, small orange squares (`"s"`) for $M = 1$ and blue diamonds (`"D"`) for $M = \Gamma$. **What figure 05e.8 shows**: the grey circles at $+1$ for quanta 1 to 8 and at $-1$ for 9 to 16; the orange squares sit inside the circles (unchanged); the blue diamonds are at $-1$ for the particles and $+1$ for the antiparticles. The only conjugation that keeps the canonical rule exchanges the charges of particles and antiparticles, and, by In [16], it also reverses the scalar and with it the mass.

**In [20], the last check.**

```python
FIGURES = ["05e_1_two_modes.png", "05e_2_anticommutators.png", "05e_3_why_krein.png",
           "05e_4_quanta.png", "05e_5_conjugated_rules.png",
           "05e_6_vacuum_values.png", "05e_7_sign_tables.png",
           "05e_8_conjugated_charges.png"]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in FIGURES),
      "the eight figure files of notebook 05e exist")
all_checks_passed()
```

The eight figure files must exist, and the last line reads ALL 18 CHECKS PASSED (notebook 05e): one check each in In [2], In [3], In [4], In [6], In [7], In [8], In [9], In [10], In [12], In [14], In [19] and In [20], and two each in In [16], In [17] and In [18]. Five of them reproduce Revision records (In [8], In [10], In [12], In [14] and the second check of In [16]); the other thirteen are the notebook's own computations.

### 5.39 What the charge-conjugation matrices say, and do not say, about matter and antimatter

The request that this book answers asks for a theory that "solves matter anti-matter mysteries". The matrices of this chapter are the first tools for that question, so this section states exactly what they establish and what they do not. Chapter 21 treats the question in full; Chapters 18 and 20 treat the pairs of universes.

**What this chapter proves (exact maps between solutions).**

- In this theory charge conjugation is a matrix map, and there are exactly two charge-conjugation matrices, $\mathcal{C}_+ = C$ (same mass) and $\mathcal{C}_- = \Gamma C$ (mass reversed) (Theorem CC, Section 5.28).
- For the commuting complex field dirac16complex00, $\mathcal{C}_+$ maps every solution to a solution with the same mass and the opposite charge density (Section 5.29).
- For a real commuting field the currents vanish, $\mathcal{C}_+$ does nothing, and the only nontrivial real matrix map is $\Gamma$ with $(m, \lambda) \to (-m, -\lambda)$ (Section 5.29).
- For the quantised anticommuting field dirac16complex the only conjugation that keeps the canonical anticommutator is $\Psi \to \Gamma\Psi^{\dagger T}$; after normal ordering it reverses the charge of every quantum and reverses the mass (Section 5.34).
- The map $\Psi \to \Gamma\Psi$ keeps the scalar and reverses every current (Section 5.5, (X7) and (X8)); it carries a solution with the parameters $(m, \lambda)$ to one with $(-m, -\lambda)$ (Section 5.29, (F3); this is the input of the pairing theorem T1, which Chapter 18 proves). So a solution and its $\Gamma$ image carry opposite charges, and the two together have total charge zero.
- The total charge $Q = \int\cos z\,\Psi^\dagger B\Psi\,d^7x$ of one solution is conserved (Section 5.6; record check `u1_noether_matrix_identity`, derived in Chapter 21). So no process described by these field equations changes the net charge inside one universe.

All of these are exact statements about **maps between sets of solutions** of the field equations.

**What is not proved, and is not claimed.**

- Nothing in this chapter shows that any universe is **created**, in pairs or otherwise. The maps relate solutions that are both allowed by the equations; they contain no creation process, no rate, no amplitude and no big-bang dynamics (Chapter 20).
- The theory as built does **not** solve the matter–antimatter problem. The observed universe contains far more matter than antimatter (Chapter 21 explains the measurement from zero). In 1967 Sakharov showed that producing such an excess from a symmetric start needs three things: a process that changes the baryon number (roughly, the number of protons and neutrons minus the number of their antiparticles), a violation of the symmetries C and CP, and a departure from thermal equilibrium (Chapter 21 derives the three conditions). The theory as built has no baryons, no process that changes a charge (the charge $Q$ is conserved), no violation of CP built in or computed, and no computation of a departure from equilibrium. Chapter 21 lists what would have to be added.
- The idea that a universe and an anti-universe together carry zero charge belongs to a class of ideas in the published literature; one example is L. Boyle, K. Finn and N. Turok, "CPT-Symmetric Universe", Phys. Rev. Lett. 121, 251301 (2018). The pair-level statement above (a solution and its $\Gamma$ image have total charge zero) is a statement of this kind about solutions. Any scenario in which our universe is one member of such a pair, or in which the pairing explains the observed excess of matter, is a **HYPOTHESIS**: nothing in this chapter or in the Revision record derives it.

### 5.40 What we proved, what we computed, what we assumed

**PROVED** (exact; the proof is in this chapter, and where a Revision record holds the fact, the report and check named confirm it independently; the notebooks named confirm it again):

- Six rules for products of different gammas (moving a gamma through a product, the square, the reverse, the transpose, the trace 0, the count of eigenvalues); the properties of $C = \gamma^{(x8)}\gamma^{(x1)}\gamma^{(x2)}\gamma^{(x3)}$ ((C1) to (C7): symmetric, $CC = 1$, $C\gamma^a$ antisymmetric, $C\gamma^aC^{-1} = -(\gamma^a)^T$, signature $(8, 8)$, $C = \mathrm{diag}(-\sigma, \sigma)$), of the chirality $\Gamma$ ((X1) to (X9), $\Gamma = \mathrm{diag}(-1_8, 1_8)$, $\Gamma^TC\Gamma = C$, $\Gamma^TC\gamma^a\Gamma = -C\gamma^a$) and of $B = -iC\gamma^{(x4)}$ ((B1) to (B5): Hermitian, $BB = 1$, signature $(8, 8)$, commuting with five gammas and anticommuting with the three of the extra times) (Sections 5.3 to 5.6; Notebook 05a; `Revision/algebra/reports/python-algebra.json` and `Revision/algebra/reports/wolfram-algebra.json`, the checks named in the tables of those sections).
- Theorem P: the 16 components carry an irreducible representation of Pin(4,4), and only the multiples of 1 commute with it; Theorem S: under Spin(4,4) they split into two irreducible, inequivalent halves of 8, and the commutant is spanned by $P_-$ and $P_+$; the same holds for the 28 generators $S^{ab}$ (Section 5.13; Notebook 05b; checks `clifford_products_span_M16`, `pin_commutant_dimension_1`, `even_products_span_M8_plus_M8`, `spin_commutant_dimension_2`, `spin_halves_irreducible`, `spin_halves_inequivalent`, `reflections_exchange_halves`).
- The so(4,4) rules, the vector rule, the key identity of reflections, the closed formulas of the exponentials, the half angle and $R(2\pi) = -1$, the invariance of the scalar under products of exponentials, the form of $B$ kept by exactly the 21 generators without $x4$, the spinor norm $g^TCg = (-1)^kN(g)\,C$, the double cover (the vector matrix fixes $g$ up to the sign), and determinant $+1$ for every element of Pin(4,4) (Sections 5.12 and 5.18; Notebook 05d; checks `S_lorentz_algebra`, `S_vector_action`, `S_preserves_C_and_commutes_with_Gamma`, `S_preserves_B_only_off_x4`).
- What the scaled commutators generate: the products of their exponentials form exactly $\mathrm{Spin}_0(4,4)$, the piece of Pin(4,4) joined to 1; Pin(4,4) consists of four pieces, $\mathrm{Spin}_0$, $\mathrm{Spin}_0\gamma^{(x8)}$, $\mathrm{Spin}_0\gamma^{(x4)}$ and $\mathrm{Spin}_0\gamma^{(x8)}\gamma^{(x4)}$; together with $\gamma^{(x8)}$ and $\gamma^{(x4)}$ the exponentials generate all of Pin(4,4) (Section 5.23; Notebook 05f).
- Theorem CC: exactly two charge-conjugation matrices, $\mathcal{C}_+ = C$ (same mass, $\Psi^c = \Psi^\ast$) and $\mathcal{C}_- = \Gamma C$ (mass reversed, $\Psi^c = \Gamma\Psi^\ast$), with $\mathcal{C}_\pm^{-1}\gamma^a\mathcal{C}_\pm = \mp(\gamma^a)^T$; the sign table of the scalar and the currents for commuting and anticommuting components; both reality conditions consistent, the real one kept in time and the other only for $m = 0$; for real fields $J = 0$, $\mathcal{C}_+$ the identity and $\Gamma$ the nontrivial map with $(m, \lambda) \to (-m, -\lambda)$ (Sections 5.28 and 5.29; Notebook 05c; the lead report of charge conjugation, with the checks named in the tables of those two sections).
- For the quantised field: the canonical conjugate cannot be a Hilbert adjoint; only $\Psi \to \Gamma\Psi^{\dagger T}$ keeps the canonical anticommutator; every conjugated bilinear is $X' = sX + c$ with the sign of the classical anticommuting components and the constant $c = \mathrm{tr}(K'B^T)$; normal ordering removes $c$ and keeps $s$; the allowed conjugation reverses the charge of every quantum and the mass (Section 5.34; Notebook 05e; checks `quantum_charge_conjugation_unitary_type` of the lead report and `no_positive_inner_product` of `Revision/theory/reports/wolfram-field-theory.json`).

**COMPUTED** (floating-point numbers, with the measured accuracy, or exact computations of the notebooks): the quadratic form of $C$ along two paths, $\mp\sin 2t$ to $10^{-14}$ (05a); the exact ranks 256 and 128 of the products of different gammas, the commutant and intertwiner dimensions 1, 2, 1, 1, 0, 0 by exact ranks and again by the zero eigenvalues of $A^TA$, the halving sequence $256, 128, \dots, 1$ and the negative control 4 (05b); the vector matrices and the closed formulas to $10^{-10}$ or better (05d); the sign pattern $(+, +)$ on 200 random products of exponentials (smallest determinant 1.019), the four patterns on 240 random elements, ten paths that never cross the band, the construction of step (I) on 40 random unit vectors and the decomposition of 12 random elements of Pin(4,4), and the spans 128 and 256 by singular values (05f); the exact solution spaces of the 2048 equations for each sign and the residuals of the free solution, below $10^{-12}$ where it solves and 11.83 where it does not, the values $S = -2$ and $J^{(x4)} = -6$, $+6$, $-6$ of the free solution and its images (exact at $x4 = 0$), and the violation $2|\sin(m\,x4)|$ of the condition $\Psi = \Gamma\Psi^\ast$ (05c); on the Fock space of 65536 states, the canonical rule to $10^{-12}$, the vacuum energy $-40$, the energies $+5$ and the charges $\pm1$, the vacuum values $S = -4.80$, $J^{(x1)} = -6.40$, $J^{(x4)} = 8$, the constants $c = \mp16$, and the reversed charges of the 16 quanta (05e). One observation is COMPUTED only and not used: $|\det A| = |\det D|$ for the 240 elements of Notebook 05f.

**ASSUMED**: the author's gammas, built from his formulas for T16 (Chapter 4), his coordinates and his metric (the input of the whole theory); the field equation $\gamma^\mu D_\mu\Psi = V\Psi$ of the Revision record (Chapter 7) and its canonical quantisation (Chapter 10); the theorem of Cartan and Dieudonné (every matrix of O(4,4) is a product of reflections), quoted without proof; three facts of analysis quoted without proof (the power series of the exponential converges for every square matrix; a linear differential equation has only one solution with a given starting value; the intermediate value theorem); and, for Notebook 05e, the scope of the example: one momentum without extra-time part, at one point of space, with the Fock vacuum of that momentum.

**HYPOTHESIS and OPEN**: this chapter derives no creation of universes and no explanation of the matter–antimatter asymmetry; every scenario built on the maps of this chapter is a HYPOTHESIS (Section 5.39). OPEN for the owner of the Revision record: the detail text of the lead check `bilinears_under_charge_conjugation` contains, in parentheses, the remark that normal ordering supplies one more sign for each bilinear, giving $(S, J) \to (S, -J)$ for $\mathcal{C}_+$; the derivation of Section 5.34 and the Fock-space computation of Notebook 05e show that normal ordering removes only a constant, so that the quantised signs are those of the record's own measured anticommuting rows. The remark should be corrected in the record; the book follows the computation.

### 5.41 Exercises

**Exercise 1.** Use only the table of Section 5.6. (a) Read off the entries $C_{1,5}$ and $(\Gamma C)_{1,5}$, and $C_{9,13}$ and $(\Gamma C)_{9,13}$, and explain them with $\Gamma = \mathrm{diag}(-1_8, 1_8)$. (b) Show that $(\Gamma C)_{5,1} = (\Gamma C)_{1,5}$, as the symmetry of $\mathcal{C}_-$ demands. (c) Which entry of $\sigma$ do the entries $(\Gamma C)_{1,5}$ and $(\Gamma C)_{9,13}$ correspond to?

*Answer.* (a) Row 1 of $C$ reads $-5$: $C_{1,5} = -1$. Multiplying by $\Gamma$ from the left multiplies row $r$ by the diagonal entry $\Gamma_{rr}$, which is $-1$ for $r = 1$; so $(\Gamma C)_{1,5} = (-1)(-1) = +1$, and the table indeed shows $+5$ in row 1 of $\Gamma C$. Row 9 of $C$ reads $+13$: $C_{9,13} = +1$; $\Gamma_{99} = +1$, so $(\Gamma C)_{9,13} = +1$, and the table shows $+13$. (b) Row 5 of $\Gamma C$ reads $+1$: $(\Gamma C)_{5,1} = +1 = (\Gamma C)_{1,5}$. (c) $\sigma$ has $1_4$ in its two off-diagonal blocks, so $\sigma_{1,5} = 1$. In $\Gamma C = \mathrm{diag}(\sigma, \sigma)$ the top-left block is $\sigma$ itself, so $(\Gamma C)_{1,5} = \sigma_{1,5} = 1$; the bottom-right block starts at row and column 9, so $(\Gamma C)_{9,13} = \sigma_{1,5} = 1$ as well.

**Exercise 2.** Without a computer, show that $\mathcal{C}_+^{-1}\gamma^{(x4)}\mathcal{C}_+ = +\gamma^{(x4)}$ and $\mathcal{C}_-^{-1}\gamma^{(x4)}\mathcal{C}_- = -\gamma^{(x4)}$, and check that both agree with Theorem CC (c).

*Answer.* By (C1) with $\eta_{x4\,x4} = -1$, $C\gamma^{(x4)} = \gamma^{(x4)}C$. So $\mathcal{C}_+^{-1}\gamma^{(x4)}\mathcal{C}_+ = C\gamma^{(x4)}C = \gamma^{(x4)}CC = \gamma^{(x4)}$, using $CC = 1$ (C3). Theorem CC (c) says it is $-(\gamma^{(x4)})^T$, and indeed $(\gamma^{(x4)})^T = -\gamma^{(x4)}$ (the time-like gammas are antisymmetric), so $-(\gamma^{(x4)})^T = \gamma^{(x4)}$. For $\mathcal{C}_-$: $\mathcal{C}_-^{-1}\gamma^{(x4)}\mathcal{C}_- = C\Gamma\gamma^{(x4)}\Gamma C = -C\gamma^{(x4)}\Gamma\Gamma C = -C\gamma^{(x4)}C = -\gamma^{(x4)}$, by (X2), (X1) and the first part; Theorem CC (c) says $+(\gamma^{(x4)})^T = -\gamma^{(x4)}$. Both agree.

**Exercise 3.** Take $\Psi_0 = e_1$, the column with 1 in row 1 and 0 elsewhere. (a) Using the table of the time-like gammas in Section 5.2, find $\gamma^{(x4)}e_1$ and write the free solution $\Psi(x4)$ of Section 5.28. (b) Write $\Psi^\ast$ and $\Gamma\Psi^\ast$ and say which mass each belongs to. (c) Compute $S = \Psi^TC\Psi$ and $J^{(x4)}$ of $\Psi$ with the table of Section 5.6. What do the answers illustrate?

*Answer.* (a) $\gamma^{(x4)}e_1$ is column 1 of $\gamma^{(x4)}$. The table lists, for each row, the column of its nonzero entry; row 14 of $\gamma^{(x4)}$ reads $+1$, so the only nonzero entry of column 1 is $+1$ in row 14: $\gamma^{(x4)}e_1 = e_{14}$. So $\Psi(x4) = \cos(m\,x4)\,e_1 - \sin(m\,x4)\,e_{14}$. (b) $\Psi$ is real, so $\Psi^\ast = \Psi$: the same-mass conjugate is the field itself (mass $m$). $\Gamma$ is $-1$ in row 1 and $+1$ in row 14, so $\Gamma\Psi^\ast = -\cos(m\,x4)\,e_1 - \sin(m\,x4)\,e_{14}$. With $\Phi_0 = \Gamma e_1 = -e_1$ the solution formula with mass $-m$ gives $\cos(-m\,x4)\Phi_0 - \sin(-m\,x4)\gamma^{(x4)}\Phi_0 = -\cos(m\,x4)\,e_1 + \sin(m\,x4)\,(-e_{14})$, the same column: $\Gamma\Psi^\ast$ belongs to the mass $-m$. (c) $S = \cos^2(m\,x4)\,C_{1,1} - \cos(m\,x4)\sin(m\,x4)\,(C_{1,14} + C_{14,1}) + \sin^2(m\,x4)\,C_{14,14}$. Row 1 of $C$ points to column 5 and row 14 to column 10, so all four entries are 0 and $S = 0$. In the same way row 1 of $B/i$ points to column 10 and row 14 to column 5, so $B_{1,1} = B_{1,14} = B_{14,1} = B_{14,14} = 0$ and $J^{(x4)} = 0$. The example illustrates Section 5.29: a real field carries no charge, $\mathcal{C}_+$ does nothing to it, and the nontrivial real map $\Gamma$ gives a different real solution with the mass reversed.

**Exercise 4.** Take the complex column $\Psi = e_1 + e_5 + i\,e_{10}$. (a) Compute $S = \Psi^\dagger C\Psi$ and $J^{(x4)} = \Psi^\dagger B\Psi$ with the table of Section 5.6. (b) Do the same for $\Psi^\ast$ and for $\Gamma\Psi^\ast$, and compare with the commuting rows of the sign table of Section 5.29.

*Answer.* (a) $S = \sum_{r,c}\Psi_r^\ast C_{rc}\Psi_c$ needs the entries of $C$ between the rows and columns 1, 5, 10. Row 1 of $C$ points to 5 with $-$ ($C_{1,5} = -1$), row 5 to 1 with $-$ ($C_{5,1} = -1$), row 10 to 14 (not among them). So $S = \Psi_1^\ast C_{1,5}\Psi_5 + \Psi_5^\ast C_{5,1}\Psi_1 = (1)(-1)(1) + (1)(-1)(1) = -2$. For $B$: row 1 of $B/i$ points to 10 with $+$ ($B_{1,10} = +i$), row 10 to 1 with $-$ ($B_{10,1} = -i$), row 5 to 14 (not among them). So $J^{(x4)} = \Psi_1^\ast B_{1,10}\Psi_{10} + \Psi_{10}^\ast B_{10,1}\Psi_1 = (1)(i)(i) + (-i)(-i)(1) = -1 - 1 = -2$. (b) $\Psi^\ast = e_1 + e_5 - i\,e_{10}$: $S$ involves only the real components 1 and 5, so $S = -2$; $J^{(x4)} = (1)(i)(-i) + (i)(-i)(1) = 1 + 1 = +2$. $\Gamma\Psi^\ast = -e_1 - e_5 - i\,e_{10}$ ($\Gamma = -1$ in rows 1 and 5, $+1$ in row 10): $S = (-1)(-1)(-1) + (-1)(-1)(-1) = -2$; $J^{(x4)} = (-1)(i)(-i) + (i)(-i)(-1) = -1 - 1 = -2$. So $\mathcal{C}_+$ keeps $S$ and reverses $J^{(x4)}$, and $\mathcal{C}_-$ keeps both: the commuting rows of the table.

**Exercise 5.** For a fixed angle $\alpha$, consider the condition $\Psi = e^{i\alpha}\Psi^\ast$. (a) Show that it is consistent in the sense of Section 5.29. (b) Find all columns that obey it. (c) Why does this not contradict the statement that there are only two charge-conjugation matrices?

*Answer.* (a) Here $M = e^{i\alpha}1$ and $MM^\ast = e^{i\alpha}e^{-i\alpha}1 = 1$: consistent. (b) Write $\Psi = e^{i\alpha/2}u$ with $u = e^{-i\alpha/2}\Psi$. Then $e^{i\alpha}\Psi^\ast = e^{i\alpha}e^{-i\alpha/2}u^\ast = e^{i\alpha/2}u^\ast$, so the condition reads $e^{i\alpha/2}u = e^{i\alpha/2}u^\ast$, that is $u = u^\ast$: the solutions are the columns $e^{i\alpha/2}u$ with $u$ real. (c) Theorem CC finds the matrices up to a factor; $e^{i\alpha}1$ is a multiple of $1$. The condition is the reality condition of $\mathcal{C}_+$ for the field $e^{-i\alpha/2}\Psi$, which differs from $\Psi$ only by a constant phase.

**Exercise 6.** With the sign rule of Section 5.34 compute $f_1^\ast f_0^\ast|00\rangle$ and $f_0^\ast f_1^\ast|00\rangle$ for two modes, and show that $f_0^\ast$ and $f_1^\ast$ anticommute on this state.

*Answer.* $f_0^\ast|00\rangle = |10\rangle$ (no mode below mode 0, sign $+$). Then $f_1^\ast|10\rangle$ fills mode 1; mode 0 below it is full, so the sign is $(-1)^1$: $f_1^\ast|10\rangle = -|11\rangle$. Hence $f_1^\ast f_0^\ast|00\rangle = -|11\rangle$. In the other order, $f_1^\ast|00\rangle = |01\rangle$ (mode 0 below is empty, sign $+$), and $f_0^\ast|01\rangle = |11\rangle$ (no mode below mode 0). Hence $f_0^\ast f_1^\ast|00\rangle = |11\rangle$. The sum is $\{f_0^\ast, f_1^\ast\}|00\rangle = -|11\rangle + |11\rangle = 0$.

**Exercise 7.** (a) Compute the constant $c = \mathrm{tr}(K'B^T)$ of Section 5.34 for the scalar ($K = C$) and the map $M = 1$. (b) Compute it for the charge density ($K = B$) and the map $M = \Gamma$. (c) The vacuum value of the charge density in the example of Notebook 05e is $\langle 0|J^{(x4)}|0\rangle = 8$. What is $\langle 0|J'^{(x4)}|0\rangle$ for $M = \Gamma$, and what is the normal-ordered result?

*Answer.* (a) $K' = C$ and $B^T = -B = iC\gamma^{(x4)}$, so $K'B^T = iCC\gamma^{(x4)} = i\gamma^{(x4)}$ by $CC = 1$, and $c = i\,\mathrm{tr}\,\gamma^{(x4)} = 0$ (Rule 5). (b) $K' = \Gamma B\Gamma = -B$ (Section 5.34), so $K'B^T = -B(-B) = BB = 1$ and $c = \mathrm{tr}\,1 = 16$. (c) For $M = \Gamma$ every sign is $s = -1$, so $\langle 0|J'^{(x4)}|0\rangle = s\langle 0|J^{(x4)}|0\rangle + c = -8 + 16 = 8$. After normal ordering, $:\!J'^{(x4)}\!: = J'^{(x4)} - 8 = (-J^{(x4)} + 16) - 8 = -(J^{(x4)} - 8) = -:\!J^{(x4)}\!:$: the constant is gone and the sign $-1$ stays, so every charge is reversed, as figure 8 of Notebook 05e shows.

**Exercise 8.** (a) Show that $\exp(\pi S^{(x4)(x5)}) = \gamma^{(x4)}\gamma^{(x5)}$. (b) Compute the spinor norm of $g = \gamma^{(x4)}\gamma^{(x5)}$ and check $g^TCg = C$. (c) Do the same for $h = \gamma^{(x1)}\gamma^{(x4)}$ and explain, with Section 5.23, why $h$ is not a product of exponentials although it lies in Spin(4,4).

*Answer.* (a) $x4$ and $x5$ are both time-like, so $\eta_{x4\,x4}\eta_{x5\,x5} = +1$ and the plane is a rotation plane; the closed formula of Section 5.18 gives $\exp(\theta S^{(x4)(x5)}) = \cos\tfrac\theta2\,1 + \sin\tfrac\theta2\,\gamma^{(x4)}\gamma^{(x5)}$, and at $\theta = \pi$, $\cos\tfrac\pi2 = 0$ and $\sin\tfrac\pi2 = 1$. (b) $g$ is a product of $k = 2$ unit vectors $e_{x4}$ and $e_{x5}$ with $\eta(e_{x4}, e_{x4}) = \eta(e_{x5}, e_{x5}) = -1$, so $N(g) = (-1)(-1) = +1$ and $g^TCg = (-1)^2N(g)\,C = C$, as for every product of exponentials. (c) For $h$, $N(h) = \eta(e_{x1}, e_{x1})\,\eta(e_{x4}, e_{x4}) = (+1)(-1) = -1$, so $h^TCh = -C$. Every product of exponentials keeps $C$ (Section 5.18), so $h$ is not one. In the language of Section 5.23: $\Lambda(h)$ reverses $x1$ and $x4$, so its space block has determinant $-1$ and its time block $-1$; the sign pattern is $(-, -)$, the piece $\mathrm{Spin}_0\,\gamma^{(x8)}\gamma^{(x4)}$, while the products of exponentials have the pattern $(+, +)$. Since $h$ has two factors, it is even and lies in Spin(4,4).
