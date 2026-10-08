## 5. The matrices $C$, $\Gamma$ and $B$, the groups Pin(4,4) and Spin(4,4), and the charge-conjugation matrices

Chapter 4 built the author's eight real gamma matrices, one $16 \times 16$ matrix for each of the eight directions of the author's universe, and proved that they obey the Clifford relation. This chapter builds from them everything else that a field with 16 components needs before its equations can be written down: the charge matrix $C$ (which turns two spinors into a number), the chirality $\Gamma$ (which cuts the 16 components into two halves of 8), the matrix $B$ (whose bilinear is the charge density), the groups Pin(4,4) and Spin(4,4) of spinor transformations with their generators $S^{ab}$, and the two charge-conjugation matrices $\mathcal{C}_+ = C$ and $\mathcal{C}_- = \Gamma C$. It proves the author's statement that the 16 components carry an irreducible representation of Pin(4,4) that splits under Spin(4,4) into two inequivalent halves, and it answers exactly the question which group the scaled commutators $S^{ab}$ generate.

### 5.1 What this chapter does

A spinor field $\Psi$ attaches 16 numbers $\Psi_1, \dots, \Psi_{16}$ to every point of spacetime. Its field equation (Chapter 7) multiplies $\Psi$ by the gamma matrices. Four further questions must be answered before the equation can be used, and each needs one of the matrices of this chapter.

- How do we make a single number out of a spinor, a number that does not change when the eight directions are turned into each other? The answer is the **bilinear** $\Psi^\dagger C\Psi$ with the charge matrix $C$ (Sections 5.4 and 5.18).
- Which parts of a spinor stay separate under every turning of the directions? The two **chiral halves**, components 1 to 8 and 9 to 16, picked out by the chirality $\Gamma$ (Sections 5.5 and 5.13).
- What is the **charge density** of a spinor field, the quantity whose total is conserved? It is $\Psi^\dagger B\Psi$ with the matrix $B$ (Section 5.6).
- What turns matter into antimatter? A **charge-conjugation matrix**. Because the author's gammas are real, plain complex conjugation does nothing to a real field and cannot exchange matter and antimatter; the exchange must be made by a matrix, and there are exactly two such matrices, $\mathcal{C}_+ = C$ and $\mathcal{C}_- = \Gamma C$ (Sections 5.1 and 5.1).

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

does not change in time for every solution of the field equation. Here the integral runs over the seven directions other than the time, $z = 6Hx8$, and $\cos z$ is the volume factor of the author's metric; the status table at the end of this section names the check, and Chapter 21 derives it. Because $B$ has eight positive and eight negative eigenvalues, the charge density can be positive or negative: the field can carry charge of both signs. In the quantum theory $B$ is the matrix of the canonical anticommutator, and its indefinite signature forces an indefinite (Krein) inner product (Section 5.1 and Chapter 10).

**The matrices $C$, $\Gamma$, $B$ and $\Gamma C$ in one table.** Each is a signed permutation matrix (for $B$, after division by $i$); the table is read like the one of Section 5.2. $C$, $\Gamma$ and $B$ are stored in the record `Revision/algebra/gammas.json`; $\Gamma C$ (the charge-conjugation matrix $\mathcal{C}_-$ of Section 5.1) is $C$ with the signs of rows 1 to 8 reversed, as Notebook 05c computes.

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

**The same with the 28 generators.** The Revision record and Notebook 05b also compute the commutant of the 28 generators $S^{ab}$: dimension 2, spanned by $P_-$ and $P_+$; on each half the commutant of the 28 blocks has dimension 1; and the equations for an intertwiner between the halves have only the solution 0. A matrix commutes with every exponential $\exp(\theta S^{ab})$ (Section 5.18) exactly when it commutes with every $S^{ab}$ (take the derivative at $\theta = 0$ in one direction; in the other, a matrix that commutes with $S$ commutes with every power of $S$ and hence with the power series of the exponential). So these numbers show that the conclusions of Theorem S hold already for the part of Spin(4,4) made of products of exponentials, which Section 5.1 calls $\mathrm{Spin}_0(4,4)$.

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

Proof: from (C5), $(\gamma^a)^T = -C\gamma^aC$, so $(\gamma^a)^TC = -C\gamma^a$ and, by linearity, $\gamma(u)^TC = -C\gamma(u)$. Hence $\gamma(u)^TC\gamma(u) = -C\gamma(u)\gamma(u) = -\eta(u, u)\,C$. In $g^TCg = \gamma(u_k)^T\cdots\gamma(u_1)^T\,C\,\gamma(u_1)\cdots\gamma(u_k)$ apply this to the innermost pair, then to the next, and so on: each factor contributes $-\eta(u_j, u_j)$. Consequence: a product of exponentials has $g^TCg = +C$, but $g = \gamma^{(x1)}\gamma^{(x4)}$, an element of Spin(4,4) with $k = 2$ and $N = (+1)(-1) = -1$, has $g^TCg = -C$. **So Spin(4,4) contains elements that are not products of exponentials.** Section 5.1 finds all of them.

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
fig, axes = plt.subplots(1, 2, figsize=(11.0, 5.1))
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
