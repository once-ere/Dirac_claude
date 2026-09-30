## 3. Split octonions and the notebook's construction of the gamma matrices

### 3.1 What this chapter does

Chapter 2 used the notebook's sixteen by sixteen gamma matrices $\gamma^a=(\mathrm{T16}^A)[a]$ as finished objects and took three of their properties from the exact machine checks: the Clifford relation, the form $C=\mathrm{diag}(-\sigma,\sigma)$ of the charge matrix, and the form $\gamma^8=\mathrm{diag}(-I_8,I_8)$ of the chirality. This chapter opens the box. The notebook does not write its gammas down entry by entry; it builds them from eight 8 by 8 matrices $\tau_0,\dots,\tau_7$, which in turn are built from six 4 by 4 matrices. The notebook's own section titles connect this construction with the **split octonions**, an 8-dimensional number system whose natural metric is exactly the metric $\eta$ of signature (4,4) used in this book (the notebook's sections "For Spin(4,4); τ tau;T16;OCTAD:Nash", "split octonions; evalues, evecs of σ" and "split octonion multiplication constants", cells 308, 837 and 891 according to the notebook survey in `handoff/surveys/`).

The chapter has four goals.

1. Build the 4 by 4 blocks and the $\tau_a$ explicitly, recognize the blocks as multiplications of **quaternions**, and prove by hand the three properties that Chapter 2 borrowed from the computer (Section 3.3 to Section 3.6).
2. Introduce the split octonions from zero, in the vector-matrix form of Max Zorn, and prove their basic identities (Section 3.7 and Section 3.8).
3. Show that the octonions give a third set of gamma matrices, and that the notebook's $\tau_a$ are exactly octonion multiplications written in a **light-cone basis** (Section 3.9 and Section 3.12).
4. Prove that any two sets of 16 by 16 gamma matrices of signature (4,4) are related by an **intertwiner** that exists and is unique up to a factor, and present the two intertwiners of the project, K_clifford and K_octonion, with the directions fixed by the errata E4 and E5 of the contract (Section 3.10 to Section 3.13).

The sources of this chapter are these files of the repository:

- the Stage-1 document `provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md`, its §3 (Results 3.1 to 3.8);
- the contract `handoff/specs/CONTRACT.md`, its §1 and the errata E4 and E5 in §11;
- the exact Python module `scripts/d16c_exact.py` (the constructions of the blocks, the $\tau_a$, the gammas of all three pictures, the Zorn product and the intertwiners) and the Wolfram package `wolfram/Dirac16ComplexAlgebra.wl`;
- the reports `python-algebra-report.json` and `wolfram-algebra-report.json` in `artifacts/dirac16complex/arbitrary-field/`. As in Chapter 2, a check name refers to the check of that name in both algebra reports.

**Labelled exceptions to counting from 0.** The notebook's 4 by 4 building blocks use Mathematica's 1-based indices $p,q\in\{1,2,3,4\}$ and $h\in\{1,2,3\}$ (Stage 1, §2.1). We keep them in Section 3.3 and Section 3.4, because the formulas are the notebook's. The three components of the ordinary three-dimensional vectors of Section 3.2 and Section 3.8 are also labelled 1, 2, 3, as usual. Everything built from these (the $\tau_a$, the octonion basis and the gammas) is counted from 0.

### 3.2 Tools: permutation signs, and vectors in three dimensions

**Permutations and their sign.** A permutation of a list of distinct numbers is a reordering of it. An **inversion** is a pair of positions in which the larger number stands first. The **sign** of the permutation is $+1$ if the number of inversions is even and $-1$ if it is odd. Examples (1-based): $(1,2,3,4)$ has no inversion, sign $+1$; $(2,1,3,4)$ has one (the pair 2,1), sign $-1$; $(2,3,1,4)$ has two (2,1 and 3,1), sign $+1$; $(1,4,3,2)$ has three (4,3; 4,2; 3,2), sign $-1$. Exchanging two entries always changes the sign (Exercise 3.1). Mathematica's function Signature returns this sign for a list of distinct entries and 0 for a list with a repeated entry. The notebook uses

$$
\epsilon_{hpq4}:=\mathrm{Signature}[\{h,p,q,4\}],
$$

which is $\pm1$ when $h,p,q,4$ are all different and 0 otherwise. The **Kronecker delta** is $\delta_{pq}=1$ for $p=q$ and $0$ otherwise.

**Vectors in three dimensions.** For $u=(u_1,u_2,u_3)$ and $r=(r_1,r_2,r_3)$ (three components, labelled 1 to 3 in the usual way) the **dot product** and the **cross product** are

$$
u\cdot r=u_1r_1+u_2r_2+u_3r_3,\qquad u\times r=\bigl(u_2r_3-u_3r_2,\ u_3r_1-u_1r_3,\ u_1r_2-u_2r_1\bigr).
$$

The dot product is a number and symmetric, $u\cdot r=r\cdot u$; the cross product is a vector and antisymmetric, $u\times r=-r\times u$. We need four identities, for all vectors $a,b,c,d$:

$$
\begin{aligned}
&\text{(V1)}\quad a\times a=0,\qquad a\cdot(a\times b)=0,\\
&\text{(V2)}\quad a\cdot(b\times c)=(a\times b)\cdot c,\\
&\text{(V3)}\quad a\times(b\times c)=b\,(a\cdot c)-c\,(a\cdot b),\\
&\text{(V4)}\quad (a\times b)\cdot(c\times d)=(a\cdot c)(b\cdot d)-(a\cdot d)(b\cdot c).
\end{aligned}
$$

*Proofs.* (V1): $a\times a=-a\times a$ by antisymmetry, so it is zero; and $a\cdot(a\times b)=a_1(a_2b_3-a_3b_2)+a_2(a_3b_1-a_1b_3)+a_3(a_1b_2-a_2b_1)$, in which the six terms cancel in pairs. (V2): both sides expand to the same six terms,

$$
a_1b_2c_3-a_1b_3c_2+a_2b_3c_1-a_2b_1c_3+a_3b_1c_2-a_3b_2c_1 .
$$

(V3): the first component of the left side is $a_2(b\times c)_3-a_3(b\times c)_2=a_2(b_1c_2-b_2c_1)-a_3(b_3c_1-b_1c_3)$, and the first component of the right side is $b_1(a_1c_1+a_2c_2+a_3c_3)-c_1(a_1b_1+a_2b_2+a_3b_3)$; in the right side the terms $a_1b_1c_1$ cancel and what remains is $a_2b_1c_2+a_3b_1c_3-a_2b_2c_1-a_3b_3c_1$, the same four terms. The other two components follow by renaming $1\to2\to3\to1$, which does not change either side's form. (V4): by (V2) with $a\times b$ in the first slot, $(a\times b)\cdot(c\times d)=a\cdot\bigl(b\times(c\times d)\bigr)$, and by (V3) $b\times(c\times d)=c\,(b\cdot d)-d\,(b\cdot c)$. $\square$

### 3.3 Quaternions

**Definition.** A **quaternion** is an expression $q=q_4+q_1\mathbf i+q_2\mathbf j+q_3\mathbf k$ with four real numbers $q_1,\dots,q_4$ (the 1-based labels match the notebook's blocks, with $q_4$ the "real part"). Quaternions are added componentwise and multiplied with the rules of William Rowan Hamilton (1843),

$$
\mathbf i^2=\mathbf j^2=\mathbf k^2=-1,\qquad\mathbf{ij}=\mathbf k=-\mathbf{ji},\qquad\mathbf{jk}=\mathbf i=-\mathbf{kj},\qquad\mathbf{ki}=\mathbf j=-\mathbf{ik},
$$

extended by the distributive law, with real numbers commuting with everything. The quaternion units $\mathbf i,\mathbf j,\mathbf k$ are written in bold to keep them apart from the complex number $i$. For $h\ne k$ in $\{1,2,3\}$ the rules say $u_hu_k=\sum_l\epsilon_{hkl}u_l$, where $u_1=\mathbf i$, $u_2=\mathbf j$, $u_3=\mathbf k$ and $\epsilon_{hkl}$ is the sign of $(h,k,l)$ (and 0 for a repeated index).

**Quaternions are associative.** The map

$$
1\mapsto I_2,\qquad\mathbf i\mapsto-i\sigma_x,\qquad\mathbf j\mapsto-i\sigma_y,\qquad\mathbf k\mapsto-i\sigma_z
$$

to complex 2 by 2 matrices respects the rules: $(-i\sigma_x)^2=-\sigma_x^2=-I_2$, and $(-i\sigma_x)(-i\sigma_y)=-\sigma_x\sigma_y=-i\sigma_z$, the image of $\mathbf k$; the other rules follow in the same way from the Pauli products of Section 2.3. The four matrices $I_2,-i\sigma_x,-i\sigma_y,-i\sigma_z$ are independent over the real numbers (their real combination $\begin{pmatrix}q_4-iq_3&-q_2-iq_1\\ q_2-iq_1&q_4+iq_3\end{pmatrix}$ vanishes only if all $q_p=0$), so a quaternion is determined by its matrix, and the product of quaternions is the product of their matrices. Matrix multiplication is associative, hence so is quaternion multiplication: $(xy)z=x(yz)$. Quaternions are, however, not commutative ($\mathbf{ij}\ne\mathbf{ji}$).

**Left and right multiplication.** Identify the quaternion $q$ with the column $(q_1,q_2,q_3,q_4)^T$. For a fixed quaternion $x$, the maps $q\mapsto xq$ and $q\mapsto qx$ are linear, so they are 4 by 4 matrices, $L_x$ and $R_x$. Associativity gives three rules:

$$
L_xL_y=L_{xy},\qquad R_xR_y=R_{yx},\qquad L_xR_y=R_yL_x,
$$

because $x(yq)=(xy)q$, $(qy)x=q(yx)$ and $x(qy)=(xq)y$.

**Worked example.** Multiply a general $q$ on the right by $\mathbf i$:

$$
q\,\mathbf i=q_1\mathbf i^2+q_2\mathbf{ji}+q_3\mathbf{ki}+q_4\mathbf i=-q_1-q_2\mathbf k+q_3\mathbf j+q_4\mathbf i .
$$

The components in the order $(\mathbf i,\mathbf j,\mathbf k,1)$ are $(q_4,\ q_3,\ -q_2,\ -q_1)$. In the same way one finds all six products with a unit:

| product | component $\mathbf i$ | component $\mathbf j$ | component $\mathbf k$ | component 1 |
| --- | --- | --- | --- | --- |
| $q\,\mathbf i$ | $q_4$ | $q_3$ | $-q_2$ | $-q_1$ |
| $q\,\mathbf j$ | $-q_3$ | $q_4$ | $q_1$ | $-q_2$ |
| $q\,\mathbf k$ | $q_2$ | $-q_1$ | $q_4$ | $-q_3$ |
| $\mathbf i\,q$ | $q_4$ | $-q_3$ | $q_2$ | $-q_1$ |
| $\mathbf j\,q$ | $q_3$ | $q_4$ | $-q_1$ | $-q_2$ |
| $\mathbf k\,q$ | $-q_2$ | $q_1$ | $q_4$ | $-q_3$ |

### 3.4 The notebook's 4 by 4 building blocks

**Definition** (notebook; Stage 1, §3.1; contract §1). For $h\in\{1,2,3\}$ and $p,q\in\{1,2,3,4\}$ (1-based),

$$
Q_a[h]_{pq}=\epsilon_{hpq4},\qquad Q_b[h]_{pq}=\delta_{p4}\delta_{qh}-\delta_{ph}\delta_{q4},\qquad s_4[h]=Q_a[h]-Q_b[h],\qquad t_4[h]=Q_a[h]+Q_b[h].
$$

$Q_a[h]$ has nonzero entries only in the rows and columns different from $h$ and 4, where it is the sign of $(h,p,q,4)$; $Q_b[h]$ has the entry $+1$ in position $(4,h)$ and $-1$ in position $(h,4)$. For $h=1$, for instance, $Q_a[1]_{23}=\epsilon_{1234}=+1$ and $Q_a[1]_{32}=\epsilon_{1324}=-1$. The six resulting matrices are

$$
s_4[1]=\begin{pmatrix}0&0&0&1\\0&0&1&0\\0&-1&0&0\\-1&0&0&0\end{pmatrix},\quad s_4[2]=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\quad s_4[3]=\begin{pmatrix}0&1&0&0\\-1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix},
$$

$$
t_4[1]=\begin{pmatrix}0&0&0&-1\\0&0&1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix},\quad t_4[2]=\begin{pmatrix}0&0&-1&0\\0&0&0&-1\\1&0&0&0\\0&1&0&0\end{pmatrix},\quad t_4[3]=\begin{pmatrix}0&1&0&0\\-1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix}.
$$

(They are produced by the functions `notebook_s4` and `notebook_t4` of `scripts/d16c_exact.py`.) The contract calls the $s_4[h]$ "self-dual" and the $t_4[h]$ "anti-self-dual"; Exercise 3.5 explains the words. We write $s_h:=s_4[h]$ and $t_h:=t_4[h]$.

**Theorem 3.1 (the blocks are quaternion multiplications).** With the identification of Section 3.3,

$$
s_1=R_{\mathbf i},\quad s_2=R_{\mathbf j},\quad s_3=R_{\mathbf k},\qquad t_1=-L_{\mathbf i},\quad t_2=-L_{\mathbf j},\quad t_3=-L_{\mathbf k}.
$$

*Proof.* The $p$-th row of $R_{\mathbf i}$ lists how component $p$ of $q\,\mathbf i$ is made from $q_1,\dots,q_4$. By the table of Section 3.3, $(q\,\mathbf i)=(q_4,q_3,-q_2,-q_1)$, so the rows of $R_{\mathbf i}$ are $(0,0,0,1)$, $(0,0,1,0)$, $(0,-1,0,0)$, $(-1,0,0,0)$: this is $s_1$. Likewise $\mathbf i\,q=(q_4,-q_3,q_2,-q_1)$ gives $L_{\mathbf i}$ with rows $(0,0,0,1)$, $(0,0,-1,0)$, $(0,1,0,0)$, $(-1,0,0,0)$, whose negative is $t_1$. The four remaining cases are read off the table in the same way. $\square$

**Corollary 3.2 (the algebra of the blocks).** For $h,k\in\{1,2,3\}$:

1. $s_h^2=t_h^2=-I_4$;
2. $s_hs_k=-\sum_l\epsilon_{hkl}s_l$ and $t_ht_k=-\sum_l\epsilon_{hkl}t_l$ for $h\ne k$; in particular $s_1s_2=-s_3$ and $t_1t_2=-t_3$;
3. $s_ht_k=t_ks_h$ for all $h,k$;
4. $s_1s_2s_3=I_4$ and $t_3t_2t_1=-I_4$;
5. all six matrices are antisymmetric signed permutation matrices, hence orthogonal.

*Proof.* (1) $s_h^2=R_{u_h}R_{u_h}=R_{u_h^2}=R_{-1}=-I_4$, and $t_h^2=L_{u_h}L_{u_h}=L_{u_h^2}=-I_4$. (2) $s_hs_k=R_{u_h}R_{u_k}=R_{u_ku_h}$ and $u_ku_h=-u_hu_k=-\sum_l\epsilon_{hkl}u_l$; and $t_ht_k=(-L_{u_h})(-L_{u_k})=L_{u_hu_k}=\sum_l\epsilon_{hkl}L_{u_l}=-\sum_l\epsilon_{hkl}t_l$. (3) $s_ht_k=-R_{u_h}L_{u_k}=-L_{u_k}R_{u_h}=t_ks_h$, by associativity. (4) $s_1s_2s_3=(-s_3)s_3=-s_3^2=I_4$, and $t_3t_2=-\epsilon_{321}t_1=t_1$, so $t_3t_2t_1=t_1^2=-I_4$. (5) Read off the matrices above. $\square$

As a check of (2) by direct multiplication:

$$
s_1s_2=\begin{pmatrix}0&0&0&1\\0&0&1&0\\0&-1&0&0\\-1&0&0&0\end{pmatrix}\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix}=-s_3 .
$$

(Row 1 of $s_1$ picks row 4 of $s_2$, which is $(0,-1,0,0)$; row 2 picks row 3, $(1,0,0,0)$; row 3 picks minus row 2, $(0,0,0,-1)$; row 4 picks minus row 1, $(0,0,1,0)$.)

### 3.5 The eight $\tau$ matrices

From here on everything is counted from 0 again. The notebook assembles 8 by 8 matrices from the 4 by 4 blocks (Stage 1, §3.1):

$$
\tau_0=I_8,\qquad\tau_h=\begin{pmatrix}0&s_h\\ s_h&0\end{pmatrix},\qquad\tau_{7-h}=\begin{pmatrix}0&t_h\\-t_h&0\end{pmatrix}\quad(h=1,2,3),\qquad\tau_7=\tau_1\tau_2\tau_3\tau_4\tau_5\tau_6 ,
$$

together with

$$
\sigma=\begin{pmatrix}0&I_4\\ I_4&0\end{pmatrix},\qquad\bar\tau_0=I_8,\qquad\bar\tau_a=\sigma\,\tau_a^T\,\sigma\quad(a=1,\dots,7).
$$

So $\tau_1,\tau_2,\tau_3$ are made from $s_1,s_2,s_3$, while $\tau_6$, $\tau_5$, $\tau_4$ are made from $t_1$, $t_2$, $t_3$ (in this order, because of the index $7-h$). In the notebook $\bar\tau_a$ is OverBar[τ][a]. As signed permutation matrices (read as in Section 2.8: the entry $-6$ in row 0 of $\tau_2$ means $(\tau_2u)_0=-u_6$):

| $i$ | $\tau_1$ | $\tau_2$ | $\tau_3$ | $\tau_4$ | $\tau_5$ | $\tau_6$ | $\tau_7$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | $+7$ | $-6$ | $+5$ | $+5$ | $-6$ | $-7$ | $-0$ |
| 1 | $+6$ | $+7$ | $-4$ | $-4$ | $-7$ | $+6$ | $-1$ |
| 2 | $-5$ | $+4$ | $+7$ | $-7$ | $+4$ | $-5$ | $-2$ |
| 3 | $-4$ | $-5$ | $-6$ | $+6$ | $+5$ | $+4$ | $-3$ |
| 4 | $+3$ | $-2$ | $+1$ | $-1$ | $+2$ | $+3$ | $+4$ |
| 5 | $+2$ | $+3$ | $-0$ | $+0$ | $+3$ | $-2$ | $+5$ |
| 6 | $-1$ | $+0$ | $+3$ | $+3$ | $-0$ | $+1$ | $+6$ |
| 7 | $-0$ | $-1$ | $-2$ | $-2$ | $-1$ | $-0$ | $+7$ |

(Generated by `notebook_tau` of `scripts/d16c_exact.py`; stored under the key `tau` of `algebra-fixture.json`.) For example, rows 0 to 3 of $\tau_1$ are the upper-right block $s_1$ shifted by four columns: row 0 of $s_1$ is $(0,0,0,1)$ in 1-based columns, that is, column 3 in 0-based counting, and in $\tau_1$ it becomes column $3+4=7$.

**Theorem 3.3 (properties of the $\tau$'s).**

1. $\tau_1,\tau_2,\tau_3$ are antisymmetric, and $\tau_4,\dots,\tau_7$ are symmetric.
2. $\bar\tau_a=-\tau_a$ for $a=1,\dots,7$ (and $\bar\tau_0=\tau_0=I_8$).
3. For $a,b\in\{1,\dots,7\}$: $\tau_a\tau_b+\tau_b\tau_a=-2\eta_{ab}I_8$. In words: $\tau_1^2=\tau_2^2=\tau_3^2=-I_8$, $\tau_4^2=\dots=\tau_7^2=+I_8$, and any two different ones anticommute.
4. $\tau_1\tau_2\tau_3=\sigma$ and $\tau_7=\mathrm{diag}(-I_4,I_4)$.
5. $\tau_1\tau_2\tau_3\tau_4\tau_5\tau_6\tau_7=I_8$.

*Proof.* We use the block rules of Section 2.2 and Corollary 3.2; $s$ stands for any $s_h$ and $t$ for any $t_k$.

(1) With $s^T=-s$: $\begin{pmatrix}0&s\\ s&0\end{pmatrix}^T=\begin{pmatrix}0&s^T\\ s^T&0\end{pmatrix}=-\begin{pmatrix}0&s\\ s&0\end{pmatrix}$. With $t^T=-t$: $\begin{pmatrix}0&t\\-t&0\end{pmatrix}^T=\begin{pmatrix}0&-t^T\\ t^T&0\end{pmatrix}=\begin{pmatrix}0&t\\-t&0\end{pmatrix}$. And $\tau_7$ is diagonal by (4).

(2) Conjugation by $\sigma$ exchanges the two halves: $\sigma\begin{pmatrix}A&B\\ D&E\end{pmatrix}\sigma=\begin{pmatrix}E&D\\ B&A\end{pmatrix}$. For $a=1,2,3$, $\tau_a^T=-\tau_a$ and $\sigma\tau_a\sigma=\tau_a$ (both off-diagonal blocks are $s$), so $\bar\tau_a=\sigma\tau_a^T\sigma=-\tau_a$. For $a=4,5,6$, $\tau_a^T=\tau_a$ and $\sigma\begin{pmatrix}0&t\\-t&0\end{pmatrix}\sigma=\begin{pmatrix}0&-t\\ t&0\end{pmatrix}=-\tau_a$, so again $\bar\tau_a=-\tau_a$. For $a=7$, $\tau_7=\mathrm{diag}(-I_4,I_4)$ by (4), and $\sigma\tau_7\sigma=\mathrm{diag}(I_4,-I_4)=-\tau_7$.

(3) *Squares.* $\tau_h^2=\mathrm{diag}(s_h^2,s_h^2)=-I_8$; for $a=7-h$, $\tau_a^2=\begin{pmatrix}0&t_h\\-t_h&0\end{pmatrix}^2=\mathrm{diag}(-t_h^2,-t_h^2)=+I_8$; and $\tau_7^2=I_8$ by (4). These are $-\eta_{aa}I_8$.
*Two $s$-type matrices*, $h\ne k$: $\tau_h\tau_k=\mathrm{diag}(s_hs_k,s_hs_k)$, and $s_hs_k=-s_ks_h$ by Corollary 3.2 (2), so they anticommute.
*Two $t$-type matrices*, built from $t$ and $t'$: $\tau\tau'=\begin{pmatrix}0&t\\-t&0\end{pmatrix}\begin{pmatrix}0&t'\\-t'&0\end{pmatrix}=\mathrm{diag}(-tt',-tt')$, and $tt'=-t't$, so they anticommute.
*An $s$-type and a $t$-type matrix:*

$$
\begin{pmatrix}0&s\\ s&0\end{pmatrix}\begin{pmatrix}0&t\\-t&0\end{pmatrix}=\begin{pmatrix}-st&0\\0&st\end{pmatrix},\qquad\begin{pmatrix}0&t\\-t&0\end{pmatrix}\begin{pmatrix}0&s\\ s&0\end{pmatrix}=\begin{pmatrix}ts&0\\0&-ts\end{pmatrix}.
$$

The sum is $\mathrm{diag}(ts-st,\ st-ts)=0$ because $s$ and $t$ commute (Corollary 3.2 (3)).
*With $\tau_7=\mathrm{diag}(-I_4,I_4)$:* $\begin{pmatrix}0&B\\ D&0\end{pmatrix}\tau_7=\begin{pmatrix}0&B\\-D&0\end{pmatrix}$ and $\tau_7\begin{pmatrix}0&B\\ D&0\end{pmatrix}=\begin{pmatrix}0&-B\\ D&0\end{pmatrix}$, whose sum is 0; every $\tau_a$ with $1\le a\le6$ has this off-diagonal form.

(4) $\tau_1\tau_2=\mathrm{diag}(s_1s_2,s_1s_2)$ and then $\tau_1\tau_2\tau_3=\begin{pmatrix}0&s_1s_2s_3\\ s_1s_2s_3&0\end{pmatrix}=\sigma$, since $s_1s_2s_3=I_4$. Next, $\tau_4\tau_5=\mathrm{diag}(-t_3t_2,-t_3t_2)=\mathrm{diag}(-t_1,-t_1)$, because $t_3t_2=t_1$ (proof of Corollary 3.2 (4)), and

$$
\tau_4\tau_5\tau_6=\begin{pmatrix}-t_1&0\\0&-t_1\end{pmatrix}\begin{pmatrix}0&t_1\\-t_1&0\end{pmatrix}=\begin{pmatrix}0&-t_1^2\\ t_1^2&0\end{pmatrix}=\begin{pmatrix}0&I_4\\-I_4&0\end{pmatrix}.
$$

Therefore $\tau_7=(\tau_1\tau_2\tau_3)(\tau_4\tau_5\tau_6)=\begin{pmatrix}0&I_4\\ I_4&0\end{pmatrix}\begin{pmatrix}0&I_4\\-I_4&0\end{pmatrix}=\begin{pmatrix}-I_4&0\\0&I_4\end{pmatrix}$.

(5) $\tau_1\cdots\tau_6\tau_7=\tau_7\tau_7=I_8$ by (3). $\square$

Statement (3) says that $\tau_1,\dots,\tau_7$ are seven anticommuting 8 by 8 matrices, three squaring to $-1$ and four to $+1$: the notebook has built a Clifford algebra with seven generators inside the 8 by 8 matrices, and the step to 16 by 16 adds the eighth direction.

### 3.6 The notebook's gammas assembled: the proofs promised in Chapter 2

The notebook's gammas are $\gamma^a=\begin{pmatrix}0&\bar\tau_a\\ \tau_a&0\end{pmatrix}$ (Section 2.8). By the block rule,

$$
\gamma^a\gamma^b=\begin{pmatrix}0&\bar\tau_a\\ \tau_a&0\end{pmatrix}\begin{pmatrix}0&\bar\tau_b\\ \tau_b&0\end{pmatrix}=\begin{pmatrix}\bar\tau_a\tau_b&0\\0&\tau_a\bar\tau_b\end{pmatrix}.
$$

**Theorem 3.4 (Stage 1, Result 3.1, by hand).** $\gamma^a\gamma^b+\gamma^b\gamma^a=2\eta^{ab}I_{16}$ for all $a,b=0,\dots,7$.

*Proof.* We need $\bar\tau_a\tau_b+\bar\tau_b\tau_a=2\eta_{ab}I_8$ and $\tau_a\bar\tau_b+\tau_b\bar\tau_a=2\eta_{ab}I_8$.

- $a=b=0$: $\bar\tau_0=\tau_0=I_8$, and both expressions are $2I_8=2\eta_{00}I_8$.
- $a=0$, $b\ge1$: with $\bar\tau_b=-\tau_b$, $\bar\tau_0\tau_b+\bar\tau_b\tau_0=\tau_b-\tau_b=0$, and $\tau_0\bar\tau_b+\tau_b\bar\tau_0=-\tau_b+\tau_b=0$; and $\eta_{0b}=0$.
- $a,b\ge1$: both expressions equal $-(\tau_a\tau_b+\tau_b\tau_a)$, which is $2\eta_{ab}I_8$ by Theorem 3.3 (3). $\square$

The symmetry pattern also follows directly: for $a\ge1$, $(\gamma^a)^T=\begin{pmatrix}0&\tau_a^T\\ \bar\tau_a^T&0\end{pmatrix}$, and with $\bar\tau_a=-\tau_a$ and Theorem 3.3 (1) this is $+\gamma^a$ for $a=1,2,3$ and $-\gamma^a$ for $a=4,\dots,7$; $\gamma^0=\begin{pmatrix}0&I_8\\ I_8&0\end{pmatrix}$ is symmetric.

**Theorem 3.5 (the charge matrix and the chirality, by hand).** $C=\gamma^0\gamma^1\gamma^2\gamma^3=\mathrm{diag}(-\sigma,\sigma)$ and $\gamma^8=\gamma^0\cdots\gamma^7=\mathrm{diag}(-I_8,I_8)$.

*Proof.* From the product formula with $\bar\tau_0=\tau_0=I_8$ and $\bar\tau_a=-\tau_a$ ($a\ge1$):

$$
\begin{aligned}
&\gamma^0\gamma^1=\mathrm{diag}(\tau_1,-\tau_1),&&\gamma^2\gamma^3=\mathrm{diag}(-\tau_2\tau_3,-\tau_2\tau_3),\\
&\gamma^4\gamma^5=\mathrm{diag}(-\tau_4\tau_5,-\tau_4\tau_5),&&\gamma^6\gamma^7=\mathrm{diag}(-\tau_6\tau_7,-\tau_6\tau_7).
\end{aligned}
$$

Multiplying the first two, $C=\mathrm{diag}(-\tau_1\tau_2\tau_3,\ \tau_1\tau_2\tau_3)=\mathrm{diag}(-\sigma,\sigma)$ by Theorem 3.3 (4). Multiplying the last two, $\gamma^4\gamma^5\gamma^6\gamma^7=\mathrm{diag}(\tau_4\tau_5\tau_6\tau_7,\ \tau_4\tau_5\tau_6\tau_7)$. Hence

$$
\gamma^8=C\,\gamma^4\gamma^5\gamma^6\gamma^7=\mathrm{diag}\bigl(-\tau_1\tau_2\cdots\tau_7,\ \tau_1\tau_2\cdots\tau_7\bigr)=\mathrm{diag}(-I_8,I_8)
$$

by Theorem 3.3 (5). $\square$

With Theorem 3.4 and Theorem 3.5 every statement of Chapter 2 about the notebook's gammas now rests on hand computations with six 4 by 4 matrices; the machine checks (`ALG_clifford`, `ALG_chargeMatrix`, `ALG_chirality`) confirm them. The tables of Section 2.8 can also be read off from the blocks: rows 0 to 7 of $\gamma^a$ are the rows of $\bar\tau_a$ with the column numbers shifted by 8, and rows 8 to 15 are the rows of $\tau_a$. For example, row 0 of $\tau_1$ is $+7$, so row 0 of $\bar\tau_1=-\tau_1$ is $-7$ and row 0 of $\gamma^1$ is $-(7+8)=-15$, as in the table.
