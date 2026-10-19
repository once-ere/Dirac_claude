## 11. GKD and the Lovelock tensors

Einstein's equations of gravity set one curvature tensor, the Einstein tensor, equal to the energy and momentum of matter. In eight dimensions there is room for more: two further tensors, built from products of two and of three curvature tensors, have the same good properties as Einstein's. Together with Einstein's they are the three **Lovelock tensors** of the formula (4.38) that the author quotes in his notebook. Every term of these tensors carries a weight $+1$, $-1$ or $0$ given by the **generalized Kronecker delta**, which the author defined as a determinant and which the Revision program computes with a fast rule called **GKD**. This chapter proves that the rule is right, counts and tests it, builds the three Lovelock tensors of the corrected metric of the Revision record twice (with the Revision Rust program and with independent Python code), proves their classical identities and their structure, and studies their components along the deflating history of the record. Chapter 12 then turns these components into the field equations for $a_4$ and $b_4$.

### 11.1 What this chapter does, and why

In Chapter 3 we computed the curvature of the author's metric, the corrected metric of the Revision record (version 2 of 2026-10-16): its Christoffel symbols, its Riemann tensor $R^{ab}{}_{cd}$, its Ricci tensor and its Einstein tensor $G^h{}_j$. Einstein's field equations, $G^\mu{}_\nu + \Lambda\delta^\mu{}_\nu = \kappa T^\mu{}_\nu$, use only the Einstein tensor. Why that tensor? Because its **divergence** vanishes for every metric (the contracted Bianchi identity, Section 3.25), as the conservation of energy and momentum demands of the right-hand side. In 1971 David Lovelock found every tensor with this property that is built from the metric and its first and second derivatives (D. Lovelock, J. Math. Phys. 12, 498 (1971); we quote his theorem and do not prove it). In four dimensions only the Einstein tensor (and the constant term $\Lambda$) exists. In eight dimensions there are exactly three: the Einstein tensor and two companions. The author's notebook quotes them in the form of equation (4.38) of the book of Lovelock and Rund, and the Revision computed them for the corrected metric (folder `Revision/gkd_lovelock`, document `Revision/docs/LOVELOCK_GKD.md`).

The chapter has three parts, each with one notebook.

- **The generalized Kronecker delta** (Sections 11.3 to 11.9). We restate the author's definition, a determinant of a matrix of zeros and ones, prove that it equals the sign of a permutation or zero, and show that this rule (GKD) is exactly what the Revision's Rust program computes. We count how often each value occurs, prove that a delta with nine labels in eight dimensions is always zero, compare the cost of the rule with the cost of the determinant, and connect the delta with the Levi-Civita tensors of the curved metric (the author's second route). Notebook 11a checks all of this in Python and reads the record of the Rust self-test. Nothing in this part depends on the metric.
- **The three Lovelock tensors** (Sections 11.10 to 11.19). We collect the curvature of the corrected metric (and show, line by line, why no curvature component mixes the time with the hidden direction), define the Lovelock tensors $P_{(1)}, P_{(2)}, P_{(3)}$ and the Lovelock scalars $L_{(1)}, L_{(2)}, L_{(3)}$, explain how the enormous sums are organised so that a computer can do them exactly, and prove by hand, line by line, that $P_{(1)} = -4G$, that $P_{(2)} = -8$ times the Gauss-Bonnet tensor, and the trace identity. Notebook 11b runs the Rust program `lovelock_gkd`, checks that it reproduces the Revision records byte for byte, and computes everything a second time in Python.
- **The components along the deflating history** (Sections 11.20 to 11.27). We write out the components of the normalised tensors $E_{(k)} = -P_{(k)}/2^{k+1}$, prove their structure (which components are equal, which contain second derivatives, how they depend on $e^{2a_4}/b_4$, which do not care about the direction of time), derive the two conservation identities that they obey, and draw them along the deflating history of the record, $a_4 = AHx_4$, $b_4 = b_4(0)\,e^{(4/3)AHx_4}$, together with the source that this history needs, and along an illustrative test history. Notebook 11c does this with exact algebra.

Everything in this chapter is geometry of the given metric: no physical assumption about matter enters, and nothing here concerns pairs of universes or matter and antimatter. Every formula is PROVED (by a derivation written out here, or by exact computation in the Revision records and the notebooks) or COMPUTED (a numerical test), and each statement names the record file and check that confirm it. The metric of 2026-10-14 (with the factor $\sin^{1/3}z$ on 3-space and $\cot^2z$ alone as $g_{00}$), withdrawn on 2026-10-16, appears only as dated history, where it explains why the metric was corrected (Section 11.10).

### 11.2 The words and symbols of this chapter

Each word is defined in plain terms here; the later sections make the definitions precise.

- **Coordinates** $x_0, \dots, x_7$: the author's names of the eight directions, in the author's order. $x_0$: the hidden direction, space-like, through the angle $z = 6Hx_0$, which takes every real value. $x_1, x_2, x_3$: ordinary 3-space (they inflate). $x_4$: the time. $x_5, x_6, x_7$: the three **extra times**, time-like directions that **deflate exponentially**. Programs number the coordinates $0, 1, \dots, 7$ in the same order, so the number $k$ stands for $x_k$.
- **The corrected metric**: the diagonal metric with the entries $g_{00} = e^{-2a_4}b_4\cot^2z$, $g_{11} = g_{22} = g_{33} = e^{2a_4}$, $g_{44} = -1$ and $g_{55} = g_{66} = g_{77} = -e^{-2a_4}b_4(\sin^2z)^{1/6}$ (every other entry is 0), with two functions $a_4(x_4)$ and $b_4(x_4) > 0$ of the time ($b_4$ is never 1), the constant $H > 0$, and $(\sin^2z)^{1/6}$ the positive sixth root of $\sin^2z$; signature (4,4) wherever $\sin z\cos z \ne 0$ (Section 3.5). The **scale factor** of a direction is $f_a = \sqrt{|g_{aa}|}$: $e^{a_4}$ for 3-space, $e^{-a_4}b_4^{1/2}(\sin^2z)^{1/12}$ for an extra time, $e^{-a_4}b_4^{1/2}|\cot z|$ for the hidden direction. The **block**: the four directions $x_0, x_5, x_6, x_7$, which share the factor $e^{-a_4}b_4^{1/2}$ and shrink together.
- **The six variables**: $H$; $a_4' = da_4/dx_4$ and $a_4''$; $u = b_4'/b_4$ and its derivative $v = du/dx_4$ (so $b_4''/b_4 = v + u^2$); and $k = e^{2a_4}/b_4$, a positive pure number. The block deflates at the rate $a_4' - u/2$ (the derivative of $-\ln(e^{-a_4}b_4^{1/2})$); the record writes $h_4 = u/2 - a_4'$. **A warning about the letter $k$**: as a label in parentheses, $E_{(k)}$, $P_{(k)}$, it is the order of a Lovelock tensor; standing alone in a formula, as in $H^2k$, it is the number $e^{2a_4}/b_4$. The notebooks write the second as the symbol `K`.
- **Label**: the name of a coordinate. **Index list**: an ordered list of labels, such as $(x_2, x_1, x_4)$; its **length** $p$ is the number of entries. A **pair** of index lists is a **lower** list $(l_1, \dots, l_p)$ and an **upper** list $(u_1, \dots, u_p)$ of the same length.
- **Kronecker delta** $\delta(a, b) = \delta^b_a$: the number 1 if the labels $a$ and $b$ are equal, 0 otherwise.
- **Permutation**, **inversion**, **sign**: a permutation is a re-ordering of $p$ objects, written as the list $(\sigma(1), \dots, \sigma(p))$; an inversion is a pair of places $i < j$ with $\sigma(i) > \sigma(j)$; the sign is $(-1)^{\text{number of inversions}}$, $+1$ for an **even** and $-1$ for an **odd** permutation (Section 1.19).
- **Determinant** (Leibniz formula): $\det M = \sum_\pi \mathrm{sign}(\pi)\,M_{1\pi(1)}\cdots M_{p\pi(p)}$, a sum of $p!$ products, one for every permutation $\pi$ (Section 1.20). **Minor** $M^{(rc)}$: the matrix left when row $r$ and column $c$ of $M$ are removed.
- **Generalized Kronecker delta**: $\delta^{u_1\dots u_p}_{l_1\dots l_p} = \det[\delta(l_i, u_j)]$, the author's `kδ[lower, upper]`. **GKD**: the Rust function of the Revision program that computes it by the rule proved in Section 11.3.
- **Pigeonhole principle**: if more than $n$ objects are put into $n$ boxes, some box holds two of them.
- **Levi-Civita symbol** $[i_1\dots i_n]$: the sign of the list $(i_1, \dots, i_n)$ if it is a re-ordering of all $n$ labels, and 0 otherwise (Section 1.44).
- **Metric** $g_{ab}$, **inverse metric** $g^{ab}$: the author's metric is diagonal, so $g^{aa} = 1/g_{aa}$ and all other entries are zero.
- **Christoffel symbol** $\Gamma^a{}_{bc}$, **Riemann tensor** $R^a{}_{bcd}$ and $R^{ab}{}_{cd} = g^{bb}R^a{}_{bcd}$, **plane curvature** $K(a, b) = R^{ab}{}_{ab}$ (no sum), **Ricci tensor** $R^h{}_j = \sum_c R^{hc}{}_{jc}$, **Ricci scalar** $R = \sum_h R^h{}_h$, **Einstein tensor** $G^h{}_j = R^h{}_j - \frac12\delta^h_jR$: Chapter 3 (Sections 3.15 and 3.17) defines them. A **mixed component** is a nonzero $R^{ab}{}_{cd}$ whose lower pair of labels is not its upper pair, such as $R^{x_4x_5}{}_{x_0x_5}$.
- **Summed label**: in this chapter a label that appears once up and once down inside one term is summed over its eight values, unless "no sum" is said; the free labels $h$ and $j$ are never summed.
- **Lovelock tensor** $P_{(k)}{}^h{}_j$ of **order** $k$ and **Lovelock scalar** $L_{(k)}$: the sums of Section 11.11. **Normalised Lovelock tensor** $E_{(k)} = -P_{(k)}/2^{k+1}$; $E_{(1)}$ is the Einstein tensor. **Gauss-Bonnet tensor**: the classical name of the order-2 Lovelock tensor. **Density** $A_{(k)}{}^{lh} = \sqrt{|\det g|}\,g^{ll}P_{(k)}{}^h{}_l$: the form in which formula (4.38) is written.
- **Euler density**: in a space of even dimension $n = 2m$, the Lovelock scalar of order $m$ (in eight dimensions $L_{(4)}$). For a closed space (finite, without an edge) with a positive-definite metric its integral is a constant times the **Euler characteristic**, a whole number fixed by the shape of the space that does not change when the metric is deformed (Section 11.11; a classical theorem, quoted: ASSUMED).
- **Component**: one number of a tensor, such as $E^{x_1}{}_{x_1}$; a **diagonal** component has $h = j$.
- **Leaf**, **pruning** (skipping): a complete combination of $k$ curvature entries in the computer's search; pruning means leaving out combinations known to give zero.
- **Divergence** $\nabla_h P^h{}_j$: the curved-space form of "change plus outflow"; zero divergence means **conservation**.
- **History**: the two metric functions $a_4(x_4)$ and $b_4(x_4)$ as functions of the time. **The history of the record**: $a_4 = AHx_4$, $b_4 = b_4(0)\,e^{(4/3)AHx_4}$ with the **slope** $A = 1$ and $b_4(0) = 1$; on it $a_4' = AH$, $u = \frac43AH$, $a_4'' = v = 0$, $k = e^{(2/3)AHx_4}/b_4(0)$, and the block deflates like $e^{-AHx_4/3}$. It is a PRESCRIBED background: it is not a solution of the vacuum field equations, it needs a source, and the record prescribes it instead of solving for it (Section 11.23). **Illustration**: a choice made only to show how a formula behaves; it is not a solution of any equation.
- **Exact** computation: with whole numbers and fractions, no rounding. **Byte for byte**: two files equal in every byte.
- **Status labels**: PROVED (exact, by a derivation or by exact computation, with the record file and check), COMPUTED (numerical, with its accuracy), ASSUMED, HYPOTHESIS, OPEN.
- **The record files of this chapter.** A record file named without its folder lies in the folder `Revision/gkd_lovelock/results`: the report `lovelock-report.json` of the Rust program (its 27 checks and the counters of its sums); `curvature.json` (the metric, the Christoffel symbols, the Riemann, Ricci and Einstein tensors); `lovelock-tensors.json` (every component of the Lovelock tensors, and the scalars); `gkd-selftest.json` (the GKD self-test); `python-lovelock-report.json` (the Revision's independent sympy verification, with 56 checks); and `wolfram-gkd-report.json` (the Revision's independent Wolfram verification, with 29 checks). The record of the field equations of $a_4$ and $b_4$ is `Revision/field_equations_a4/a4-equations.json`, and its sympy report is `Revision/field_equations_a4/reports/python-a4-report.json`.

### 11.3 The author's generalized Kronecker delta and the rule GKD

**The definition.** The author defined the generalized delta in an input cell of his Mathematica notebook. The Revision record quotes the cell verbatim in `Revision/gkd_lovelock/results/PROVENANCE_OF_THE_COMPUTATION.md` (the cell stored as In[87], the author's In[54]); in Mathematica's plain-text spelling it reads

```text
k\[Delta][lower_, upper_] /; Length[lower] == Length[upper] :=
    Det[Outer[delta, lower, upper]]
```

For a lower list $(l_1, \dots, l_p)$ and an upper list $(u_1, \dots, u_p)$ of the same length (the condition after `/;`), `Outer[delta, lower, upper]` is the $p \times p$ matrix $M$ with the entry $M_{ij} = \delta(l_i, u_j)$ in row $i$ and column $j$: one row for each lower label, one column for each upper label, and a 1 wherever the two labels are equal. `Det` takes its determinant. So

$$
\delta^{u_1\dots u_p}_{l_1\dots l_p} = \det\big[\delta(l_i, u_j)\big]_{i,j = 1,\dots,p} .
$$

For two lists of different lengths the definition does not apply, and Mathematica leaves the expression unevaluated (record `Revision/gkd_lovelock/results/wolfram-gkd-report.json`, check `definition_unequal_lengths_stay_unevaluated`). For $p = 1$ the matrix is the single number $\delta(l_1, u_1)$, so the generalized delta of one label is the ordinary Kronecker delta. For $p = 2$:

$$
\delta^{u_1u_2}_{l_1l_2} = \det\begin{pmatrix}\delta(l_1, u_1) & \delta(l_1, u_2)\\ \delta(l_2, u_1) & \delta(l_2, u_2)\end{pmatrix}
$$

(the definition with $p = 2$),

$$
= \delta(l_1, u_1)\,\delta(l_2, u_2) - \delta(l_1, u_2)\,\delta(l_2, u_1)
$$

(the $2 \times 2$ determinant is $ad - bc$, Section 1.20). For example $\delta^{x_1x_2}_{x_1x_2} = 1\cdot 1 - 0\cdot 0 = 1$ and $\delta^{x_2x_1}_{x_1x_2} = 0\cdot 0 - 1\cdot 1 = -1$.

**Theorem (the rule GKD; PROVED).** Let $M_{ij} = \delta(l_i, u_j)$. Then $\det M = 0$ if a label appears twice in the lower list, or twice in the upper list, or if some lower label does not appear in the upper list. Otherwise $\det M = \mathrm{sign}(\sigma)$, where $\sigma(i)$ is the place of $l_i$ in the upper list.

*Proof, case by case.*

(a) Two equal lower labels, $l_i = l_k$ with $i \ne k$. For every column $j$,

$$
M_{ij} = \delta(l_i, u_j) = \delta(l_k, u_j) = M_{kj}
$$

(the definition of $M$; then $l_i = l_k$; then the definition again). So rows $i$ and $k$ are equal, and a matrix with two equal rows has determinant 0 (rule 4 of Section 1.20: exchanging the two rows changes nothing, yet flips the sign, so $\det M = -\det M$ and $\det M = 0$).

(b) Two equal upper labels, $u_j = u_k$ with $j \ne k$. By the same steps columns $j$ and $k$ are equal, so the transpose $M^T$ has two equal rows and $\det M = \det M^T = 0$ (rules 2 and 4 of Section 1.20).

(c) A lower label $l_i$ that equals no upper label. Then $M_{ij} = 0$ for every $j$: row $i$ is all zeros. Every product of the Leibniz formula contains exactly one entry of row $i$, so every product is 0, and $\det M = 0$.

(d) Otherwise: the $p$ lower labels are different, the $p$ upper labels are different, and every lower label appears among the upper labels. Then $l_i$ equals exactly one upper label, the one at the place $\sigma(i)$. Different lower labels sit at different places of the upper list, so $\sigma$ sends the places $1, \dots, p$ to the places $1, \dots, p$ without repetition: $\sigma$ is a permutation. Row $i$ of $M$ has its only 1 in column $\sigma(i)$, so $M$ is the permutation matrix of $\sigma$. In the Leibniz formula the product of a permutation $\pi$ is $M_{1\pi(1)}\cdots M_{p\pi(p)}$; it is 1 when $\pi(i) = \sigma(i)$ for every $i$ and 0 otherwise (one factor is then an entry off the 1s). Only the term $\pi = \sigma$ survives:

$$
\det M = \mathrm{sign}(\sigma)\cdot 1\cdots 1 = \mathrm{sign}(\sigma) .
$$

End of proof. $\square$

The same theorem is proved in Section 1.42; it is repeated here because the whole chapter rests on it. It is also written, as the opening comment, in the Rust file `Revision/gkd_lovelock/code/src/gkd.rs`.

**The rule as a recipe.** The Rust function `GKD(lower, upper)` follows the proof step by step, without building a matrix:

- It walks through the upper list and notes the place of every label. A label seen a second time means two equal columns: it returns 0 (case b).
- It walks through the lower list and looks up the place of every label. A label not found means a row of zeros: it returns 0 (case c). A place found a second time means two equal lower labels: it returns 0 (case a). The places form the list $\sigma$.
- It counts the inversions of $\sigma$ and returns $+1$ for an even count and $-1$ for an odd count (case d).

Counting the inversions of a list of $p$ entries compares each of the $p(p - 1)/2$ pairs of places once. The Leibniz formula instead adds $p!$ products. For $p = 7$, the length that the third Lovelock tensor needs, this is 21 comparisons against 5,040 products.

**Examples (PROVED).** Take the lower list $(x_1, x_2, x_3, x_4)$.

- Upper list $(x_2, x_1, x_4, x_3)$: the places of $x_1, x_2, x_3, x_4$ in it are $\sigma = (2, 1, 4, 3)$ (counting from 1). The inversions are the pairs of entries $(2, 1)$ and $(4, 3)$: two, an even number, so the value is $+1$.
- Upper list $(x_2, x_3, x_4, x_1)$: $\sigma = (4, 1, 2, 3)$; the inversions are $(4, 1)$, $(4, 2)$, $(4, 3)$: three, odd, value $-1$.
- Lower list $(x_1, x_2, x_3, x_3)$ with upper list $(x_1, x_2, x_3, x_4)$: $x_3$ repeats in the lower list, case (a), value 0.

These are the three matrices of Figure 11a.1 (Notebook 11a, In [3]). The Revision record lists five examples with the labels 1 to 4, lower list first: `kdelta[{1,2},{1,2}] = 1`, `kdelta[{1,2},{2,1}] = -1`, `kdelta[{1,1},{1,1}] = 0`, `kdelta[{1,2,3},{2,3,1}] = 1`, `kdelta[{1,2,3},{1,2,4}] = 0` (`Revision/gkd_lovelock/results/python-lovelock-report.json`, check `gkd_examples`). Any whole numbers can serve as labels, because only the equality of two labels matters. Notebook 11a, In [2] and In [4], reproduces all five with both the determinant and the rule.

### 11.4 Counting the values; nine labels in eight dimensions; the cost of the determinant

**The number of nonzero values (PROVED).** Fix the length $p \le 8$. By the theorem, a pair has a nonzero value exactly when the lower list holds $p$ different labels and the upper list holds the same $p$ labels in some order. The lower list can be chosen in

$$
8\cdot 7\cdots(8 - p + 1) = \frac{8!}{(8 - p)!}
$$

ways (8 choices for the first label, 7 for the second, which must differ from the first, and so on; the numbers of choices multiply). For each such lower list the upper list can be any of its $p!$ orders. So the number of pairs with a nonzero value is

$$
N_{\ne 0}(p) = \frac{8!}{(8 - p)!}\; p!
$$

out of $8^p\cdot 8^p = 8^{2p}$ pairs (8 choices for each of the $2p$ entries).

**Half are $+1$, half are $-1$ (PROVED, for $p \ge 2$).** Exchange the first two labels of the upper list. In $\sigma$ this exchanges the values 1 and 2 (the places of these two labels). The two entries of $\sigma$ that hold the values 1 and 2 change their relative order, so the pair they form becomes an inversion if it was none, and stops being one if it was one. Every other pair of entries is compared as before: a pair that contains neither of the two entries is unchanged, and an entry with a value of 3 or more is larger than both 1 and 2, so its comparison with either of them gives the same answer. Hence the number of inversions changes by exactly one, and the exchange turns every even order into an odd one. Doing it twice gives back the original order, so the exchange pairs the even orders with the odd orders one to one: there are as many of each. For $p = 1$ the only order is the identity, which is even. (Section 1.19 proves the same for every exchange of two entries.)

**The table (PROVED by the formula; COMPUTED by counting).** With $8!/(8-p)!$ equal to 8, 56, 336, 1680 for $p = 1, 2, 3, 4$:

| length $p$ | all pairs $8^{2p}$ | value $+1$ | value $-1$ | value 0 |
| --- | --- | --- | --- | --- |
| 1 | 64 | 8 | 0 | 56 |
| 2 | 4096 | 56 | 56 | 3984 |
| 3 | 262144 | 1008 | 1008 | 260128 |
| 4 | 16777216 | 20160 | 20160 | 16736896 |

For example $p = 3$: $336\cdot 3! = 336\cdot 6 = 2016$ nonzero values, half of them, 1008, of each sign, and $262144 - 2016 = 260128$ zeros. The counts for $p = 1, 2, 3$ are those of the Revision's Wolfram verification, which called the author's verbatim definition on every one of these 266,304 pairs (`Revision/gkd_lovelock/results/wolfram-gkd-report.json`, field `measurements`, entry `gkdComparison`, and checks `gkd_equals_kdelta_exhaustive_length_1` to `_length_3`); Notebook 11a counts them again (In [6]) and compares them with the formula and with the record (In [7]). The row $p = 4$ comes from the formula; the Rust self-test of the record compared all 16,777,216 pairs of length 4 (`Revision/gkd_lovelock/results/gkd-selftest.json`), and Notebook 11a runs it again (In [14]). Figure 11a.4 draws the table.

**Nine labels in eight dimensions (PROVED).** A list of 9 labels taken from only 8 must repeat a label, by the pigeonhole principle. So case (a) applies, and every generalized delta with $p \ge 9$ is zero. The Lovelock tensor of order $k$ (Section 11.11) carries a delta of length $p = 2k + 1$: $p = 3, 5, 7$ for $k = 1, 2, 3$, and $p = 9$ for $k = 4$. Therefore the Lovelock tensor of order 4, and every higher one, vanishes identically in eight dimensions, and the Lovelock sum stops at $k = 3$ (record `Revision/gkd_lovelock/results/python-lovelock-report.json`, check `gkd_nine_indices_in_eight_dimensions_vanish`; record `Revision/gkd_lovelock/results/lovelock-report.json`, check `k4_tensor_vanishes`; Notebook 11a, In [10]).

**The cost of the determinant (PROVED by counting).** The Leibniz formula of a $p \times p$ determinant adds $p!$ products; the rule GKD makes $p(p - 1)/2$ comparisons of places. And the number $8^{2p}$ of all pairs grows so fast that only the lengths up to 4 can be tested exhaustively:

| length $p$ | products $p!$ | comparisons $p(p-1)/2$ | all pairs $8^{2p}$ |
| --- | --- | --- | --- |
| 1 | 1 | 0 | 64 |
| 2 | 2 | 1 | 4096 |
| 3 | 6 | 3 | $2.6 \times 10^5$ |
| 4 | 24 | 6 | $1.7 \times 10^7$ |
| 5 | 120 | 10 | $1.1 \times 10^9$ |
| 6 | 720 | 15 | $6.9 \times 10^{10}$ |
| 7 | 5040 | 21 | $4.4 \times 10^{12}$ |
| 8 | 40320 | 28 | $2.8 \times 10^{14}$ |
| 9 | 362880 | 36 | $1.8 \times 10^{16}$ |

(Notebook 11a, In [12], prints this table and draws it as Figure 11a.5.) The work of one literal determinant grows by the factor $p$ from one length to the next, because $p! = p\cdot(p - 1)!$. Notebook 11a also measures both methods on the same 200 pairs of length 7 and checks that the rule is more than ten times faster (In [12]). It does not print the measured times: they differ from computer to computer and from run to run, and the printed output of every notebook of this book must be the same on every run.

**Random tests and the birthday problem (PROVED; COMPUTED).** For the lengths 5 to 9 the Rust self-test of the record compares GKD with the literal determinant on 200,000 pseudo-random pairs of each length (Section 1.49 explains the generator `xorshift64*` and its seeds). Half of the samples are **rearranged** pairs: $p$ random labels form the upper list and the lower list is the same list in a random order. The other half are two **independent** random lists. A rearranged pair has a nonzero value exactly when its $p$ random labels are all different. Each label is one of 8 with equal chance, so this happens with the probability

$$
r_p = \frac{8}{8}\cdot\frac{7}{8}\cdots\frac{8 - p + 1}{8} = \frac{8!}{(8 - p)!\,8^p}
$$

(the first label may be anything; the second must avoid the first, 7 of 8 values; the third must avoid the first two, 6 of 8; and so on; independent chances multiply, a rule of probability ASSUMED here, Section 1.50). This is the **birthday problem** with 8 possible birthdays. An independent pair is nonzero with the small probability $q_p = N_{\ne 0}(p)/8^{2p}$. With $N$ samples of each kind the expected number of nonzero values is $N(r_p + q_p)$, and the usual random scatter of such a count, its **standard deviation**, is $\sqrt{Nr_p(1 - r_p) + Nq_p(1 - q_p)}$ (ASSUMED from probability theory). For $p = 5$ and $N = 100000$:

$$
r_5 = \frac{8\cdot 7\cdot 6\cdot 5\cdot 4}{8^5} = \frac{6720}{32768} = 0.20508, \qquad q_5 = \frac{6720\cdot 120}{8^{10}} = \frac{806400}{1073741824} = 0.00075
$$

(the formula; then $8^5 = 32768$ and $8^{10} = 1073741824$), so the expected count is $100000\cdot(0.20508 + 0.00075) = 20583$ (rounded), with a standard deviation of about 128. The record's count is 20538 (`gkd-selftest.json`), 0.35 standard deviations below the expectation. Notebook 11a, In [15], makes this comparison for every length 5 to 9 of the record, and In [11] for its own 2,000 Python samples of each length 4 to 9; all counts lie within 2 standard deviations (Figure 11a.6). For $p = 9$ the chance is $r_9 = 0$, because the factor $(8 - 9 + 1)/8 = 0$ appears: the pigeonhole principle once more, and both tests find no nonzero value. A random test is evidence, not a proof; the proof that GKD equals the determinant is the theorem of Section 11.3. The tests show that the two programs implement the theorem without a slip.

### 11.5 The author's second route: two Levi-Civita tensors of the curved metric

The author's notebook builds the generalized delta also in a second way, from two **Levi-Civita tensors**, in the cell In[32] (record `Revision/gkd_lovelock/results/notebook-input-cells.txt`). Section 1.44 proved the identity behind it for the Levi-Civita **symbol** $[i_1\dots i_8]$ (the sign of the list, or 0):

$$
\sum_{c_2,\dots,c_8}[a\,c_2\dots c_8]\,[b\,c_2\dots c_8] = 7!\;\delta^b_a .
$$

The author uses the Levi-Civita **tensor** of a curved metric $g$, whose second factor carries upper labels raised with the inverse metric. Section 1.44 used the fact that raising all labels multiplies the product by the sign of $\det g$, and promised it here. We prove it now.

**A determinant identity (PROVED).** For every $n \times n$ matrix $N$ and every list $(i_1, \dots, i_n)$,

$$
\sum_{m_1,\dots,m_n} N_{i_1m_1}\cdots N_{i_nm_n}\,[m_1\dots m_n] = \det N\;[i_1\dots i_n] .
$$

*Proof.* (i) For the list $(i_1, \dots, i_n) = (1, \dots, n)$: the symbol $[m_1\dots m_n]$ is 0 unless $(m_1, \dots, m_n)$ is a permutation $\pi$, and then it is $\mathrm{sign}(\pi)$; so the left side is $\sum_\pi\mathrm{sign}(\pi)N_{1\pi(1)}\cdots N_{n\pi(n)}$, the Leibniz formula, which is $\det N = \det N\,[1\dots n]$. (ii) Exchanging two entries of the list $(i_1, \dots, i_n)$ exchanges two rows of the products on the left, which flips the sign of the left side (rule 3 of Section 1.20, applied to the matrix with the rows $i_1, \dots, i_n$), and it flips the sign of $[i_1\dots i_n]$ on the right (Section 1.19). Every re-ordering of $(1, \dots, n)$ is reached by such exchanges, so both sides agree for every re-ordering. (iii) If the list repeats a label, the matrix with the rows $i_1, \dots, i_n$ has two equal rows, so the left side is 0 (rule 4), and so is the right side. $\square$

**Raising all labels (PROVED).** The Levi-Civita tensor of $g$ is $\varepsilon_{i_1\dots i_8} = \sqrt{|\det g|}\,[i_1\dots i_8]$; raising all its labels gives

$$
\varepsilon^{i_1\dots i_8} = \sum_{m_1,\dots,m_8} g^{i_1m_1}\cdots g^{i_8m_8}\,\sqrt{|\det g|}\,[m_1\dots m_8]
$$

(one inverse metric for each label),

$$
= \sqrt{|\det g|}\;\det(g^{-1})\,[i_1\dots i_8] = \frac{\sqrt{|\det g|}}{\det g}\,[i_1\dots i_8]
$$

(the identity just proved with $N = g^{-1}$; then $\det(g^{-1}) = 1/\det g$, rule 1 of Section 1.20 applied to $g\,g^{-1} = I$). For the author's diagonal metric no general rule is needed: only $m_r = i_r$ survives in each sum, and the product $g^{i_1i_1}\cdots g^{i_8i_8}$ over a re-ordering of all eight labels is the product of all eight diagonal entries $1/g_{aa}$, which is $1/\det g$ (the determinant of a diagonal matrix is the product of its diagonal, Section 1.20). Multiplying the two tensors,

$$
\varepsilon_{a_1\dots a_8}\,\varepsilon^{b_1\dots b_8} = \sqrt{|\det g|}\cdot\frac{\sqrt{|\det g|}}{\det g}\,[a_1\dots a_8][b_1\dots b_8] = \frac{|\det g|}{\det g}\,[a_1\dots a_8][b_1\dots b_8]
$$

(the two definitions; $\sqrt{u}\sqrt{u} = u$), and $|\det g|/\det g$ is the sign of $\det g$. For the author's metric, the corrected metric of the Revision record, $\det g = e^{-2a_4}b_4^4\cot^2z\,|\sin z| > 0$ wherever $\sin z\cos z \neq 0$, for every $a_4$ and every $b_4 > 0$ (four entries of the diagonal are negative, an even number; record `Revision/gkd_lovelock/results/python-lovelock-report.json`, check `sqrt_abs_det_g`; `Revision/gkd_lovelock/results/wolfram-gkd-report.json`, check `sqrt_det_g`; Section 1.21), so the sign is $+1$: the product of the two curved Levi-Civita tensors is exactly the product of the two symbols, and the author's second route gives, after the contraction over seven labels and the division by $7!$, the ordinary Kronecker delta $\delta^b_a$ with no extra sign. In a metric with an odd number of time-like directions, such as the four-dimensional spacetime of everyday physics, the sign would be $-1$. Notebook 01c checks the author's second route with the flat metric of signature (4,4) (Section 1.44).

### 11.6 Example: the generalized Kronecker delta in Python and in Rust

Notebook 11a puts Sections 11.3 and 11.4 to work. It writes the author's definition literally in Python, as an exact determinant computed by sympy; writes the rule GKD as a Python function; reproduces the record's five examples; draws three $4 \times 4$ matrices and all six arrangements of three labels; compares the rule with the determinant for all 266,304 pairs of lengths 1 to 3 and for 12,000 pseudo-random pairs of lengths 4 to 9; counts the values and compares the counts with the formula and with the Wolfram record; shows that every delta of nine labels vanishes; compares the cost of the two methods; builds the Revision Rust program `lovelock_gkd` with cargo and reads the record `Revision/gkd_lovelock/results/gkd-selftest.json` of its GKD self-test, checking every row; compares the self-test's counts with the birthday formula; and checks once more that every check and number it quotes from the Revision records is there. It needs Rust. The Rust self-test itself takes 7 to 13 minutes, because it computes 200,000 literal determinants of $9 \times 9$ matrices, each a sum of 362,880 products; that is longer than the limit of 7 minutes that this book sets for one computation, so the notebook prints the command that repeats it instead of running it (In [13]). The whole notebook took 28.4 seconds, including the start of the kernel, when it was built on 2026-10-18 (the provenance file `Revision/textbook/notebooks/11a_kronecker_delta_gkd.PROVENANCE.md`). It prints 24 PASS lines, draws six figures and ends with the line ALL 24 CHECKS PASSED (notebook 11a).

<!-- NOTEBOOK 11a -->

### 11.9 Line-by-line walk-through of Notebook 11a

The notebook has 17 code cells, In [1] to In [17]. This section explains every line of every one of them, in order: a line or a small group of lines is quoted, then explained. A line that starts with `#`, and the part of a line after `#`, is a **comment**, which Python skips; it is there for the reader. Inside a function the text in triple quotes below the `def` line is its **docstring**, a description that Python stores but does not run; to keep the quotations short, docstrings are left out of them where the explanation repeats them, and a long figure caption passed to `save_figure` is shortened to `...` (the full caption is printed under the figure in Section 11.8). Because Notebook 11a is the first notebook of this chapter, its set-up cell is explained here in full; the walk-throughs of Notebooks 11b and 11c refer back to this explanation.

**In [1], the set-up cell.** Its first part, down to the heading THE SET-UP between two lines of `=` signs, consists of comment lines that repeat the complete run instructions of Section 11.7, so that the notebook file carries its own instructions. The code below the heading computes no physics; it is the same in every notebook of the book except for the line that names the notebook and, in notebooks without Rust, the two lines `import shutil` and `import subprocess` and the helper `rust_program`, which such notebooks lack (all three are explained below, the helper at the end).

```python
import json  # reads and writes JSON files (text files that hold names and numbers)
import os  # reads the environment variable TEXTBOOK_OUTPUT_ROOT (explained below)
import textwrap  # breaks long printed text into lines of at most 89 characters
from pathlib import Path  # file and folder paths that work on Windows, macOS and Linux
```

`import` loads a **module**, a part of Python or of an installed package, so that the code can use its functions. `json`, `os`, `textwrap` and `pathlib` come with Python. `from pathlib import Path` takes the single name `Path` out of the module `pathlib`; a `Path` is the address of a file or folder, written the same way on every operating system.

```python
import matplotlib  # the plotting package
import matplotlib.pyplot as plt  # its drawing functions, called plt by convention
from IPython.display import Image, display  # shows a saved picture below a cell
import shutil  # finds the program cargo
import subprocess  # runs cargo and the Rust programs
```

These load the plotting package matplotlib, its drawing functions under the short name `plt`, the two functions `Image` and `display` of IPython (the part of Jupyter that runs Python), which show a picture file below a cell, and the two modules that a notebook with Rust needs: `shutil` can look for a program on the computer, and `subprocess` can start another program and collect what it prints.

```python
NOTEBOOK_ID = "11a"  # this notebook: chapter 11, example a
```

A **variable** is a name for a value. This line gives the name `NOTEBOOK_ID` to the **string** (a text in quotes) `"11a"`; the figures and the captions file are named after it.

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

`def` defines a **function**, a named piece of code that runs each time it is called. `Path.cwd()` is the folder in which Jupyter runs the notebook (the folder of the notebook file), and `.resolve()` writes it as a complete address. `here.parents` is the list of the folders above it, and `[here, *here.parents]` is the list that starts with `here` and continues with them (the star unpacks one list into another). The `for` loop visits these folders one after the other. The operator `/` joins a folder and a name into a longer path, and `.is_file()` is true when that file exists. The first folder that contains the file `Revision/textbook/requirements.txt` is the repository, and `return` hands it back. If no folder does, `raise` stops the notebook with a `FileNotFoundError` whose message says what to do.

```python
REPO = find_repository_root()
OUTPUT_ROOT = Path(os.environ.get("TEXTBOOK_OUTPUT_ROOT", str(REPO)))
```

(The comment lines above each of these two lines are left out.) The first line calls the function and names the result `REPO`. It is never printed, because it differs from computer to computer and the printed output of a notebook must not. The second line chooses where files are written: `os.environ` holds the **environment variables** of the running program (named texts it receives from the computer), and `.get(name, default)` returns the value of `TEXTBOOK_OUTPUT_ROOT` if it is set and `str(REPO)` otherwise. When you run the notebook the variable is not set, so files go into the repository; the book's checking tool sets it to a scratch folder, so that a check run changes nothing in the repository.

```python
def repository_file(relative):
    return REPO / relative


def output_file(relative):
    path = OUTPUT_ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    return path
```

Two small helpers (docstrings left out). `repository_file` gives the full path of a repository file, for READING a Revision record. `output_file` gives the full path at which to WRITE a file; `path.parent.mkdir(parents=True, exist_ok=True)` first creates the file's folder and any missing folder above it, and does nothing if they exist.

```python
def say(text):
    print(textwrap.fill(str(text), width=89, subsequent_indent="    "))
```

`say` prints a text in lines of at most 89 characters, the width of a page of the book: `str(text)` turns any value into text, and `textwrap.fill` breaks it at blanks and starts every line after the first with four blanks.

```python
matplotlib.rcdefaults()  # ignore personal matplotlib settings: same figures everywhere
plt.rcParams.update({"figure.figsize": (7.0, 4.2), "font.size": 10.0,
                     "axes.grid": True, "grid.alpha": 0.3})
```

`matplotlib.rcdefaults()` returns matplotlib to its built-in settings, so the figures are the same on every computer. `plt.rcParams.update({...})` then sets the size of a figure (7.0 by 4.2 inches), the size of its letters (10 points) and a faint grid (`grid.alpha` 0.3 means 30 per cent opaque). The braces make a **dictionary**, a collection of pairs `key: value`.

```python
FIGURE_FOLDER = "Revision/textbook/figures"  # where the figures are saved
CAPTION_FILE = f"{FIGURE_FOLDER}/{NOTEBOOK_ID}.captions.json"  # their captions
FIGURE_NUMBERS = {}  # figure name -> its number k (file name <id>_<k>_<name>.png)
CAPTIONS = {}  # figure file name -> caption, written to CAPTION_FILE after every figure
# Start with an empty captions file ({} is an empty JSON dictionary); save_figure fills
# it.  newline="\n" writes the same line ends on Windows, macOS and Linux.
output_file(CAPTION_FILE).write_text("{}\n", encoding="utf-8", newline="\n")
```

A string that starts with `f` is an **f-string**: a name in braces is replaced by its value, so `CAPTION_FILE` is `"Revision/textbook/figures/11a.captions.json"`. `FIGURE_NUMBERS` and `CAPTIONS` start as empty dictionaries. The two comment lines explain the last line, which writes an empty JSON dictionary and a line end into the captions file; `encoding="utf-8"` fixes how letters are stored as bytes and `newline="\n"` stores the same line end on every system.

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

(Docstring and three comment lines left out.) `setdefault(name, value)` returns the number already stored for this figure name, or stores and returns one more than the number of figures so far: the figures are numbered 1, 2, 3, and a cell run twice keeps its number. The file name joins the notebook id, the number and the name, for example `11a_1_outer_delta_matrices.png`. `fig.savefig` writes a PNG picture file with 150 dots per inch, cuts away the empty margin and stores no program name, so that two runs write the same bytes. `plt.close(fig)` removes the figure from memory, because Jupyter would otherwise draw it a second time. The caption is stored, the whole dictionary is written to the captions file (`json.dumps` turns it into JSON text with sorted keys), `display(Image(...))` shows the saved picture below the cell, and the last line prints where it was saved.

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

`PASSED` is an empty **list**, an ordered collection in square brackets. `check` is behind every check of the book: if `condition` is false, `raise AssertionError(...)` stops the notebook with an error that names the check (an `if` is used instead of the statement `assert`, because Python started with its optimising option skips every `assert`); otherwise the name is appended to `PASSED` and the line PASS name is printed, followed by a second line naming the Revision record when `record` is given. `record=None` makes that argument optional.

```python
def report(label, value, unit=""):
    say(f"RESULT {label} = {value}" + (f" {unit}" if unit else ""))


def all_checks_passed():
    print(f"ALL {len(PASSED)} CHECKS PASSED (notebook {NOTEBOOK_ID})")
```

`report` prints a key number as a line RESULT label = value, with the unit when one is given (`a if c else b` is `a` when `c` is true and `b` otherwise; an empty string counts as false). `all_checks_passed` prints the last line of the notebook with the number of checks that passed; `len` is the length of a list.

```python
def rust_program(manifest, binary):
    if shutil.which("cargo") is None:
        raise FileNotFoundError(
            "cargo was not found: install Rust from https://rustup.rs, open a new "
            "terminal, activate the environment and start JupyterLab again")
    crate = (REPO / manifest).parent  # the folder that holds Cargo.toml
```

The helper that builds a Rust program (docstring left out). `shutil.which("cargo")` searches the folders where the computer looks for programs and returns `None` (Python's "nothing") when cargo is not installed; the notebook then stops with a message that says how to install it. `crate` is the folder of the crate, the folder that holds the file `Cargo.toml` named by `manifest`.

```python
    completed = subprocess.run(
        ["cargo", "build", "--release", "--manifest-path", str(REPO / manifest),
         "--target-dir", str(crate / "target")],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
```

`subprocess.run([...])` starts the program cargo with the words of the list as its command line, waits until it ends and returns a record of the run, here named `completed`. The command is the build command of the run instructions: build the crate in the release (optimised) mode and put the result into the folder `target` next to `Cargo.toml`. `capture_output=True` collects what cargo prints instead of showing it; `text=True` with `encoding="utf-8"` turns the collected bytes into text, and `errors="replace"` replaces any byte that is not valid text by a placeholder instead of stopping.

```python
    if completed.returncode != 0:  # show the end of cargo's error message
        print(completed.stderr[-3000:])
        raise RuntimeError(f"cargo build failed for {manifest}")
    for file_name in (binary, binary + ".exe"):  # Linux and macOS; Windows
        path = crate / "target" / "release" / file_name
        if path.is_file():
            say(f"Rust program {binary} is built and ready.")
            return path
    raise FileNotFoundError(f"cargo built {manifest} but {binary} is missing")
```

Every program ends with a **return code**, 0 for success. If cargo failed, the last 3,000 characters of its error output (`stderr[-3000:]`, the slice from 3,000 characters before the end to the end) are printed and the notebook stops. Otherwise the loop looks for the program file without and with the ending `.exe` (Windows adds it), prints that the program is ready and returns its path. If neither file exists, the notebook stops with a message.

```python
say(f"Set-up of notebook {NOTEBOOK_ID} complete: repository folder found, helpers "
    "defined.")
```

The last line prints the cell's only output, Set-up of notebook 11a complete: repository folder found, helpers defined. (Two strings written next to each other inside the parentheses are joined into one.)

**In [2], the literal definition.**

```python
import itertools  # loops over all lists of labels, and over all permutations
import math  # factorials n! and the numbers n!/(n-p)!
import re  # regular expressions: reads numbers out of the texts of the records
import time  # a stopwatch (used inside one check; no time is ever printed)

import numpy as np  # arrays of numbers and pseudo-random numbers
import sympy as sp  # exact algebra: sympy computes determinants exactly
```

Six more modules: `itertools` produces all lists of labels and all permutations; `math` has `math.factorial(p)` $= p!$ and `math.perm(n, p)` $= n!/(n - p)!$; `re` reads numbers out of text with **regular expressions** (patterns of characters); `time` provides a stopwatch; numpy (short name `np`) handles arrays of numbers and makes pseudo-random numbers; sympy (short name `sp`) does exact algebra.

```python
NAMES = ["x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7"]  # the labels 0..7 by name
```

The list of the eight coordinate names; `NAMES[0]` is `"x1"` and `NAMES[7]` is `"x0"`, because Python counts places from 0.

```python
def outer_delta(lower, upper):
    return [[1 if a == b else 0 for b in upper] for a in lower]
```

The matrix `Outer[delta, lower, upper]` as a list of rows. The inner part `[1 if a == b else 0 for b in upper]` is a **list comprehension**: for each upper label `b` it writes 1 if `b` equals the lower label `a` and 0 otherwise; that is one row. The outer comprehension makes one such row for each lower label `a`. So the entry in row $i$ and column $j$ is $\delta(l_i, u_j)$, exactly the author's matrix.

```python
DETERMINANTS = {}  # memory: a matrix (a tuple of rows) -> its determinant


def kdelta(lower, upper):
    if len(lower) != len(upper):
        raise ValueError("kdelta needs two index lists of the same length")
    matrix = tuple(tuple(row) for row in outer_delta(lower, upper))
    if matrix not in DETERMINANTS:  # each different matrix is computed only once
        DETERMINANTS[matrix] = int(sp.Matrix(matrix).det())
    return DETERMINANTS[matrix]
```

The author's definition, literally (docstring left out). Two lists of different lengths are refused with a `ValueError`, as Mathematica leaves the author's expression unevaluated. The matrix is turned into a **tuple** of tuples (a tuple is a list that cannot be changed; only such values can be keys of a dictionary). If this matrix has not been met before, sympy computes its determinant exactly (`sp.Matrix(matrix).det()`), `int` turns the result into a Python whole number, and it is stored in the dictionary `DETERMINANTS`. Many different pairs of lists give the same 0/1 matrix, so this memory saves most of the work.

```python
EXAMPLES = [  # (lower list, upper list, value stated in the Revision record)
    ((1, 2), (1, 2), 1),
    ((1, 2), (2, 1), -1),
    ((1, 1), (1, 1), 0),
    ((1, 2, 3), (2, 3, 1), 1),
    ((1, 2, 3), (1, 2, 4), 0),
]
```

The five examples of the record check `gkd_examples` of `Revision/gkd_lovelock/results/python-lovelock-report.json`, each as a lower list, an upper list and the stated value.

```python
for lower, upper, stated in EXAMPLES:
    say(f"kdelta[{list(lower)}, {list(upper)}] = {kdelta(lower, upper)}   "
        f"(the record states {stated})")
check(all(kdelta(lower, upper) == stated for lower, upper, stated in EXAMPLES),
      "the five examples give 1, -1, 0, 1, 0",
      record="Revision/gkd_lovelock/results/python-lovelock-report.json, "
             "check gkd_examples")
```

The loop takes the three parts of each example apart (`for lower, upper, stated in ...`) and prints the computed value next to the stated one; these are the first five output lines. `all(...)` is true when every comparison in the parentheses is true; the check prints PASS the five examples give 1, -1, 0, 1, 0 and the line naming the record. Look at the fourth example: the place of the lower label 1 in the upper list $(2, 3, 1)$ is 3, that of 2 is 1, that of 3 is 2; $\sigma = (3, 1, 2)$ has the two inversions $(3, 1)$ and $(3, 2)$, so the value is $+1$, as printed.

```python
try:  # lists of different lengths must be refused, as in the author's definition
    kdelta((1,), (1, 2))
    refused = False
except ValueError:
    refused = True
check(refused, "kdelta refuses two lists of different lengths")
```

`try ... except ValueError` runs the line `kdelta((1,), (1, 2))` and catches the `ValueError` it should raise. (`(1,)` is a tuple with the single entry 1.) If the error comes, `refused` is set to `True`; if it did not come, the line after the call would set it to `False` and the check would fail. Output: PASS kdelta refuses two lists of different lengths. Two checks so far.

**In [3], three matrices drawn (Figure 11a.1).**

```python
SHOWN = [  # (lower list, upper list); the label k stands for xk
    ((1, 2, 3, 4), (2, 1, 4, 3)),  # x2 x1 x4 x3: two exchanges, even
    ((1, 2, 3, 4), (2, 3, 4, 1)),  # x2 x3 x4 x1: a cycle of four, odd
    ((1, 2, 3, 3), (1, 2, 3, 4)),  # x3 twice in the lower list
]
fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.9))
```

The three pairs of the examples of Section 11.3, written with the numbers 0 to 7 for $x_0$ to $x_7$ (the number $k$ stands for $x_k$, so `(1, 2, 3, 4)` is the list $(x_1, x_2, x_3, x_4)$ and `(2, 1, 4, 3)` the list $(x_2, x_1, x_4, x_3)$, as the comments say). `plt.subplots(1, 3, ...)` makes a figure `fig` with one row of three panels, the **axes** (drawing areas) `axes[0]`, `axes[1]`, `axes[2]`, 10.5 by 3.9 inches in all.

```python
for ax, (lower, upper) in zip(axes, SHOWN):
    matrix = np.array(outer_delta(lower, upper))
    ax.imshow(matrix, cmap="Blues", vmin=0.0, vmax=1.5)  # 0 white, 1 blue
```

`zip(axes, SHOWN)` pairs the first panel with the first pair of lists, and so on. For each, the matrix is built and turned into a numpy array; `ax.imshow` draws it as a picture of coloured squares, one per entry, with the colour map `Blues` running from white at `vmin` = 0 to dark blue at `vmax` = 1.5 (so that a 1 is a medium blue and the numbers stay readable).

```python
    for i in range(4):  # i: the row
        for j in range(4):  # j: the column
            ax.text(j, i, str(matrix[i, j]), ha="center", va="center")
```

`range(4)` is $0, 1, 2, 3$. The two loops write each entry as text at the centre of its square; `ax.text(x, y, ...)` takes the horizontal position first, which is the column `j`, then the row `i`.

```python
    ax.set_xticks(range(4), [NAMES[label] for label in upper])  # column labels
    ax.set_yticks(range(4), [NAMES[label] for label in lower])  # row labels
    ax.set_xlabel("upper list (one column per label)")
    ax.set_ylabel("lower list (one row per label)")
```

The columns are marked with the names of the upper labels and the rows with the names of the lower labels; then the two axes get their titles.

```python
    value = kdelta(lower, upper)
    ax.set_title(f"determinant = {value:+d}" if value else "determinant = 0")
    ax.grid(False)  # no grid lines across the squares
fig.tight_layout()  # no overlapping labels
```

The exact determinant becomes the panel title; the format `:+d` writes a whole number with its sign, $+1$ or $-1$, and a value 0 (which counts as false) gives the title determinant = 0. The grid of the set-up cell is switched off for these pictures, and `fig.tight_layout()` moves the panels so that no labels overlap.

```python
save_figure(fig, "outer_delta_matrices",
            "The matrix Outer of delta for three pairs of index lists of length 4; "
            ...)
check([kdelta(lower, upper) for lower, upper in SHOWN] == [1, -1, 0],
      "the three drawn matrices have the determinants +1, -1 and 0")
```

The figure is saved as `11a_1_outer_delta_matrices.png` with its caption (the output line Figure 11a.1 saved as ...), and the check confirms the three values $+1$, $-1$, 0 of Section 11.3 (third PASS line).

*What Figure 11a.1 shows.* Three $4 \times 4$ matrices of zeros and ones; rows are the lower labels, columns the upper labels, and blue squares are the ones. In the left and middle panels every row and every column has exactly one 1: these are permutation matrices, with determinant $+1$ (two exchanges) and $-1$ (three inversions). In the right panel the two rows of $x_3$ are equal and the column of $x_4$ is empty, so the determinant is 0, by case (a) and case (c) of the theorem at once.

**In [4], the rule GKD in Python.**

```python
def inversions(sigma):
    return sum(1 for i in range(len(sigma)) for j in range(i + 1, len(sigma))
               if sigma[i] > sigma[j])
```

The number of inversions of a list `sigma` (docstring left out): for every pair of places `i < j` (the inner range starts at `i + 1`) it counts 1 when the entries stand in the wrong order, and `sum` adds the ones.

```python
def gkd(lower, upper):
    if len(lower) != len(upper):
        raise ValueError("gkd needs two index lists of the same length")
    position = {}  # label -> its place in the upper list
    for place, label in enumerate(upper):
        if label in position:
            return 0  # a label twice in the upper list: equal columns (case b)
        position[label] = place
```

The rule of Section 11.3, step by step (docstring left out). `enumerate(upper)` gives each upper label together with its place 0, 1, 2, .... A label already in the dictionary `position` has been seen before: two equal columns, value 0. Otherwise its place is stored.

```python
    sigma = []  # sigma[i]: the place in the upper list of the i-th lower label
    for label in lower:
        if label not in position:
            return 0  # a lower label missing above: a row of zeros (case c)
        sigma.append(position[label])
    if len(set(sigma)) < len(sigma):
        return 0  # a label twice in the lower list: equal rows (case a)
    return 1 if inversions(sigma) % 2 == 0 else -1  # even +1, odd -1 (case d)
```

For each lower label its place in the upper list is looked up; a label that is not there gives a row of zeros, value 0. A **set** keeps only different entries, so `len(set(sigma)) < len(sigma)` is true when a place occurs twice, which happens exactly when a label occurs twice in the lower list: value 0. Otherwise `sigma` is a permutation; `% 2` is the remainder after division by 2, so an even number of inversions gives $+1$ and an odd number $-1$.

```python
for lower, upper, stated in EXAMPLES:
    say(f"gkd({list(lower)}, {list(upper)}) = {gkd(lower, upper)}")
check(all(gkd(lower, upper) == kdelta(lower, upper) for lower, upper, _ in EXAMPLES),
      "gkd and kdelta agree on the five examples")
```

The rule is applied to the five examples, which prints the five values 1, $-1$, 0, 1, 0, and the check confirms that it agrees with the literal determinant on all of them (the name `_` marks the stated value, which is not needed here). Fourth PASS line.

**In [5], the six arrangements of three labels (Figure 11a.2).**

```python
lower = (1, 2, 3)  # x1, x2, x3
fig, axes = plt.subplots(2, 3, figsize=(9.0, 6.4))
signs = []
for ax, upper in zip(axes.flat, itertools.permutations(lower)):
    matrix = np.array(outer_delta(lower, upper))
    sigma = [upper.index(label) for label in lower]  # places of x1, x2, x3 above
    sign = 1 if inversions(sigma) % 2 == 0 else -1
    signs.append((sign, kdelta(lower, upper)))
```

A figure with two rows of three panels; `axes.flat` runs through the six panels one by one. `itertools.permutations(lower)` produces the $3! = 6$ arrangements of $(1, 2, 3)$, that is of $(x_1, x_2, x_3)$. For each arrangement used as the upper list, `upper.index(label)` is the place of a label in it, so `sigma` lists the places of $x_1, x_2, x_3$; its sign comes from the inversions, and the pair (sign, exact determinant) is stored in `signs`.

```python
    ax.imshow(matrix, cmap="Greens" if sign > 0 else "Oranges", vmin=0.0, vmax=1.4)
    for i in range(3):
        for j in range(3):
            ax.text(j, i, str(matrix[i, j]), ha="center", va="center")
    ax.set_xticks(range(3), [NAMES[label] for label in upper])
    ax.set_yticks(range(3), [NAMES[label] for label in lower])
```

Each matrix is drawn in green for an even and in orange for an odd arrangement, with its entries written in, its columns marked with the arranged upper labels and its rows with $x_1, x_2, x_3$.

```python
    count = inversions(sigma)  # the number of inversions of sigma
    plural = "" if count == 1 else "s"  # 1 inversion, 2 inversions
    ax.set_title(f"sigma = {tuple(sigma)}, {count} inversion{plural}, "
                 f"sign {sign:+d}", fontsize=9)
    ax.grid(False)
fig.tight_layout()
```

The title of each panel gives $\sigma$, its number of inversions (with the right plural) and its sign.

```python
save_figure(fig, "six_permutations",
            "All six arrangements of the labels $x_1, x_2, x_3$. Each panel shows "
            ...)
check(all(sign == det for sign, det in signs) and
      sorted(sign for sign, _ in signs) == [-1, -1, -1, 1, 1, 1],
      "the six arrangements of three labels: three even, three odd, sign = determinant")
```

The figure is saved, and the check confirms two things: every sign from the inversions equals the exact determinant, and the sorted list of the six signs is three times $-1$ and three times $+1$, half even and half odd as Section 11.4 proved. Fifth PASS line.

*What Figure 11a.2 shows.* Six $3 \times 3$ permutation matrices. The identity and the two cyclic arrangements, $(x_2, x_3, x_1)$ and $(x_3, x_1, x_2)$, are green: 0 or 2 inversions, sign $+1$. The three arrangements that exchange two labels are orange: 1 or 3 inversions, sign $-1$. Each title's sign is the determinant of the panel's matrix.

**In [6], every pair of lengths 1, 2 and 3.**

```python
COUNTS = {}  # p -> {+1: count, -1: count, 0: count}
mismatches = 0  # pairs where gkd and the determinant differ
for p in (1, 2, 3):
    counts = {1: 0, -1: 0, 0: 0}
    for lower in itertools.product(range(8), repeat=p):  # all 8^p lower lists
        for upper in itertools.product(range(8), repeat=p):  # all 8^p upper lists
            value = gkd(lower, upper)
            if value != kdelta(lower, upper):
                mismatches += 1
            counts[value] += 1
    COUNTS[p] = counts
```

`itertools.product(range(8), repeat=p)` produces all $8^p$ lists of length $p$ with entries 0 to 7. For each length the two nested loops visit all $8^p\cdot 8^p$ pairs, compute the rule, compare it with the literal determinant (counting any disagreement in `mismatches`; `+= 1` adds one) and count how often each value occurs. The counts of each length are stored in `COUNTS`.

```python
    say(f"p = {p}: {8 ** (2 * p):6d} pairs; value +1: {counts[1]:4d} times, "
        f"-1: {counts[-1]:4d} times, 0: {counts[0]:6d} times")
```

Inside the loop over `p`, one line per length; `**` is a power, and `:6d` writes a whole number right-aligned in 6 places. Output: 64, 4096 and 262144 pairs, with the counts 8, 0, 56; 56, 56, 3984; and 1008, 1008, 260128, exactly the table of Section 11.4.

```python
compared = sum(8 ** (2 * p) for p in (1, 2, 3))
report("pairs compared (all pairs of lengths 1, 2 and 3)", compared)
report("pairs where GKD and the determinant differ", mismatches)
report("different 0/1 matrices whose determinant sympy computed", len(DETERMINANTS))
```

Three RESULT lines: $64 + 4096 + 262144 = 266304$ pairs compared, 0 disagreements, and 145 different 0/1 matrices for which sympy had to compute a determinant; all other pairs reused a stored one.

```python
wolfram_record = json.loads(repository_file(
    "Revision/gkd_lovelock/results/wolfram-gkd-report.json").read_text(
        encoding="utf-8"))
entries = [c for c in wolfram_record["checks"]
           if c["name"].startswith("gkd_equals_kdelta_exhaustive_length_")]
```

The Revision's Wolfram report is read: `read_text` reads the file as text and `json.loads` turns the JSON text into Python lists and dictionaries. Its checks form a list of entries; the comprehension keeps the entries whose names begin with `gkd_equals_kdelta_exhaustive_length_` (`startswith` tests how a text begins). There are three of them, for the lengths 1, 2 and 3; in each, the Revision's Wolfram verification compared the values of the Rust function GKD (written out by a small Rust program that calls it) with the author's literal determinant, evaluated by Wolfram, on every pair of lists of that length.

```python
recorded_pairs = sum(int(re.search(r"all (\d+) pairs", e["detail"]).group(1))
                     for e in entries)  # the numbers of pairs the record names
```

Each entry's `detail` text names its number of pairs, as in "all 4096 pairs of index lists of length 2". The regular expression `all (\d+) pairs` finds this phrase (`\d+` is one or more digits, and the brackets mark the part to keep), `.group(1)` is the kept text and `int` turns it into a whole number; `sum` adds the three numbers: $64 + 4096 + 262144$.

```python
check(mismatches == 0 and compared == 266304 and len(entries) == 3
      and all(e["verdict"] == "PASS" and "(0 mismatches;" in e["detail"]
              for e in entries) and recorded_pairs == 266304,
      "GKD equals the literal determinant for all 266304 pairs of lengths 1 to 3",
      record="Revision/gkd_lovelock/results/wolfram-gkd-report.json, checks "
             "gkd_equals_kdelta_exhaustive_length_1 to _3")
```

The check requires no disagreement among the notebook's own 266,304 pairs, and that the record's three checks are there, have the verdict PASS, report 0 mismatches and together speak of the same 266,304 pairs (`in` tests whether one text occurs inside another). Sixth PASS line. (The Revision's sympy report `python-lovelock-report.json` also has a check on these 266,304 pairs, `gkd_literal_equals_cofactor_expansion`, but it compares something else: the literal determinant with a second, independent way of computing a determinant, the cofactor expansion (Laplace's rule, proved in Section 11.13: the determinant is the sum of the entries of one row, each times the smaller determinant left when its row and column are removed, with alternating signs). It confirms the determinant side, not GKD, and is therefore not the record of this check; In [16] only confirms that it is there and passed.)

**In [7], the counts against the formula and the Wolfram record.**

```python
def nonzero_pairs(p, n=8):
    return math.perm(n, p) * math.factorial(p)


def formula_counts(p):
    nonzero = nonzero_pairs(p)
    plus = nonzero if p == 1 else nonzero // 2  # p = 1: only the identity
    return {1: plus, -1: nonzero - plus, 0: 8 ** (2 * p) - nonzero}
```

`nonzero_pairs` is the formula $N_{\ne 0}(p) = 8!/(8 - p)!\cdot p!$ of Section 11.4 (`n=8` gives the argument `n` the default value 8). `formula_counts` splits it: for $p = 1$ every nonzero value is $+1$, otherwise half of them (`//` is whole-number division); the zeros are the rest of the $8^{2p}$ pairs.

```python
wolfram = json.loads(repository_file(
    "Revision/gkd_lovelock/results/wolfram-gkd-report.json").read_text(
        encoding="utf-8"))
for p in (1, 2, 3):
    recorded = [m for m in wolfram["measurements"]["gkdComparison"] if m["p"] == p][0]
    plus, minus, zero = recorded["plusOne"], recorded["minusOne"], recorded["zero"]
    say(f"p = {p}: formula {formula_counts(p)}, Wolfram record +1: {plus}, "
        f"-1: {minus}, 0: {zero}")
```

The Revision's Wolfram report is read; for each length the entry of its table `gkdComparison` with that `p` is found, its three counts are taken out, and the formula and the record are printed side by side (three output lines, the third broken by `say`).

```python
check(all(COUNTS[p] == formula_counts(p) for p in (1, 2, 3)),
      "the counts of +1, -1 and 0 equal the formula for p = 1, 2, 3")
check(all(COUNTS[p] == {1: m["plusOne"], -1: m["minusOne"], 0: m["zero"]}
          for p in (1, 2, 3)
          for m in wolfram["measurements"]["gkdComparison"] if m["p"] == p),
      "the counts equal those of the Wolfram verification",
      record="Revision/gkd_lovelock/results/wolfram-gkd-report.json, measurements "
             "gkdComparison, p = 1, 2, 3")
```

Two checks: the measured counts equal the formula, and they equal the record's counts (two dictionaries are equal when they have the same keys with the same values). PASS lines seven and eight.

**In [8], the map of all pairs of length 2 (Figure 11a.3).**

```python
pairs_of_labels = list(itertools.product(range(8), repeat=2))  # 64 lists (l1, l2)
grid = np.array([[gkd(lower, upper) for upper in pairs_of_labels]
                 for lower in pairs_of_labels])  # 64 x 64 values
```

The 64 lists of length 2 in the order $(0, 0), (0, 1), \dots, (7, 7)$, so the list $(l_1, l_2)$ has the number $8l_1 + l_2$. `grid` holds the value of GKD for every pair: row = lower list, column = upper list.

```python
fig, ax = plt.subplots(figsize=(6.6, 6.0))
picture = ax.imshow(grid, cmap="bwr", vmin=-1, vmax=1)  # blue -1, red +1
ticks = range(0, 64, 8)  # one tick at the start of each block of 8
ax.set_xticks(ticks, [f"({NAMES[t // 8]},x0)" for t in ticks], rotation=90)
ax.set_yticks(ticks, [f"({NAMES[t // 8]},x0)" for t in ticks])
```

The values are drawn with the colour map `bwr` (blue, white, red) from $-1$ (blue) through 0 (white) to $+1$ (red). `range(0, 64, 8)` is $0, 8, 16, \dots, 56$, the first list of each block of eight, the list $(l_1, 0)$; `t // 8` is its first label $l_1$, and its second label is 0, that is $x_0$, so the marks read $(x_0, x_0)$, $(x_1, x_0)$, and so on up to $(x_7, x_0)$ (rotated by 90 degrees on the horizontal axis).

```python
ax.set_xlabel("upper list $(u_1, u_2)$, numbered $8 u_1 + u_2$")
ax.set_ylabel("lower list $(l_1, l_2)$, numbered $8 l_1 + l_2$")
ax.set_title("GKD for all 4096 pairs of index lists of length 2")
ax.grid(False)
fig.colorbar(picture, ax=ax, ticks=[-1, 0, 1], shrink=0.8, label="value of GKD")
```

Axis titles (matplotlib draws text between dollar signs as mathematics), the title, no grid, and a colour bar beside the picture that shows which colour means which value.

```python
save_figure(fig, "gkd_map_length_two",
            "The value of the generalized Kronecker delta for all 4096 pairs of "
            ...)
check(int((grid == 1).sum()) == 56 and int((grid == -1).sum()) == 56
      and np.array_equal(grid, grid.T),
      "length 2: 56 values +1, 56 values -1, and the picture is symmetric")
```

After saving, the check counts the entries equal to 1 and to $-1$ (`grid == 1` is an array of true and false, and `.sum()` counts the trues) and tests that the picture equals its mirror image across the diagonal (`grid.T` is the transpose). The symmetry holds because the pair (lower, upper) and the pair (upper, lower) have transposed matrices and therefore the same determinant. Ninth PASS line.

*What Figure 11a.3 shows.* A $64 \times 64$ picture, almost all white. Red squares lie on the diagonal (upper list equal to the lower list, $+1$) except at the 8 lists with two equal labels, which are white. Blue squares lie at the mirrored places, where the upper list is the lower one reversed ($-1$). There are 56 of each; the remaining 3984 values are 0.

**In [9], the value counts (Figure 11a.4).**

```python
fig, ax = plt.subplots(figsize=(7.4, 4.4))
width = 0.26  # the width of one bar
for shift, value, colour, name in ((-width, 1, "tab:red", "value +1"),
                                   (0.0, -1, "tab:blue", "value -1"),
                                   (width, 0, "0.6", "value 0")):
```

A bar chart with three bars per length: the loop runs over the three values, each with its sideways shift, its colour (`"0.6"` is a grey) and its name in the legend.

```python
    heights = [COUNTS[p][value] if p < 4 else formula_counts(4)[value]
               for p in (1, 2, 3, 4)]
    bars = ax.bar([p + shift for p in (1, 2, 3, 4)], heights, width, color=colour,
                  label=name, hatch=None)
    bars[3].set_hatch("//")  # p = 4: from the formula
```

The heights are the measured counts for $p = 1, 2, 3$ and the formula for $p = 4$. `ax.bar` draws the four bars of this value; the fourth bar (place 3, counted from 0) gets a hatching to mark that it comes from the formula.

```python
    for p, height in zip((1, 2, 3, 4), heights):
        ax.text(p + shift, max(height, 1.2) * 1.15, f"{height:,}" if height else
                "none", ha="center", va="bottom", fontsize=7, rotation=90)
```

Each bar gets its count written above it (the format `:,` puts commas between groups of three digits); a count of 0 cannot be drawn on a logarithmic axis, so it is written as "none" just above the bottom.

```python
ax.set_yscale("log")  # a logarithmic vertical axis
ax.set_ylim(1.0, 2e9)
ax.set_xticks([1, 2, 3, 4], ["p = 1", "p = 2", "p = 3", "p = 4 (formula)"])
ax.set_xlabel("length $p$ of the two index lists")
ax.set_ylabel("number of pairs (logarithmic scale)")
ax.set_title("How often GKD is +1, -1 and 0 among all $8^{2p}$ pairs")
ax.legend(loc="upper left")
```

On a **logarithmic axis** each equal step is a factor of 10, so the counts 8 and 16,736,896 fit into one picture. The axis runs from 1 to $2 \times 10^9$; the remaining lines set the marks, titles and legend.

```python
save_figure(fig, "value_counts",
            "The number of pairs of index lists of length $p$ over the eight labels "
            ...)
check(formula_counts(4) == {1: 20160, -1: 20160, 0: 16736896},
      "length 4: 20160 values +1, 20160 values -1 and 16736896 zeros (formula)")
```

The figure is saved and the formula's counts for $p = 4$ are checked: $1680\cdot 24 = 40320$ nonzero values, half of each sign. Tenth PASS line.

*What Figure 11a.4 shows.* For each length three bars: red ($+1$), blue ($-1$), grey (0), on a logarithmic axis. Red and blue have equal height for $p \ge 2$; for $p = 1$ there is no $-1$. The grey bar grows much faster than the others: the fraction of nonzero values falls from 8 in 64 at $p = 1$ to 40,320 in 16,777,216 at $p = 4$, about one in 416.

**In [10], random pairs of lengths 4 to 9.**

```python
rng = np.random.default_rng(12345)  # pseudo-random numbers with a fixed seed
SAMPLES = 2000  # pairs per length p
python_nonzero = {}  # p -> number of nonzero values among the samples
random_mismatches = 0
```

`np.random.default_rng(12345)` makes a generator of pseudo-random numbers that starts from the seed 12345, so every run on every computer draws the same numbers. 2,000 pairs are drawn for each length.

```python
for p in range(4, 10):
    nonzero = 0
    for s in range(SAMPLES):
        upper = [int(v) for v in rng.integers(0, 8, size=p)]  # p labels from 0..7
        if s % 2 == 0:  # even s: the lower list is the upper list rearranged
            lower = [upper[i] for i in rng.permutation(p)]
        else:  # odd s: an independent random lower list
            lower = [int(v) for v in rng.integers(0, 8, size=p)]
```

`range(4, 10)` is 4 to 9. `rng.integers(0, 8, size=p)` draws $p$ whole numbers from 0 to 7 (the upper bound 8 is not included). For an even sample number `s`, `rng.permutation(p)` is a random arrangement of the places $0, \dots, p - 1$, and the lower list takes the upper labels in that order: a rearranged pair. For an odd `s` the lower list is drawn independently.

```python
        value = gkd(lower, upper)
        nonzero += value != 0  # True counts as 1, False as 0
        random_mismatches += value != kdelta(lower, upper)
    python_nonzero[p] = nonzero
    say(f"p = {p}: {SAMPLES} random pairs, {nonzero:4d} nonzero values")
```

For every sample the rule is computed, the nonzero values are counted, and every disagreement with the literal determinant is counted (a true comparison adds 1, a false one 0). One line per length is printed: 394, 186, 82, 24, 3 and 0 nonzero values for $p = 4$ to 9.

```python
report("random pairs compared (lengths 4 to 9)", 6 * SAMPLES)
report("random pairs where GKD and the determinant differ", random_mismatches)
report("different 0/1 matrices whose determinant sympy computed (so far)",
       len(DETERMINANTS))
check(random_mismatches == 0,
      "GKD equals the literal determinant for 12000 random pairs of lengths 4 to 9")
check(python_nonzero[9] == 0,
      "every delta with 9 indices in 8 dimensions is 0 (pigeonhole)",
      record="Revision/gkd_lovelock/results/python-lovelock-report.json, "
             "check gkd_nine_indices_in_eight_dimensions_vanish")
```

RESULT lines: 12,000 pairs compared, 0 disagreements, and 10,097 different matrices met so far (this is why the cell takes a few seconds: sympy computes almost ten thousand new determinants of sizes 4 to 9). The two checks: no disagreement, and no nonzero value of length 9, as the pigeonhole principle demands (PASS lines eleven and twelve).

**In [11], the counts against the birthday formula.**

```python
def all_different(p, n=8):
    return math.perm(n, p) / n ** p if p <= n else 0.0


def expected_nonzero(p, half):
    r = all_different(p)
    q = nonzero_pairs(p) / 8 ** (2 * p) if p <= 8 else 0.0
    mean = half * (r + q)
    spread = math.sqrt(half * r * (1 - r) + half * q * (1 - q))
    return mean, spread
```

`all_different` is the chance $r_p = 8!/((8 - p)!\,8^p)$ of Section 11.4; for more than 8 labels it returns 0. `expected_nonzero` returns the expectation $N(r_p + q_p)$ and the standard deviation $\sqrt{Nr_p(1 - r_p) + Nq_p(1 - q_p)}$ for `half` $= N$ rearranged and $N$ independent samples (`math.sqrt` is the square root).

```python
within = True
for p in range(4, 10):
    mean, spread = expected_nonzero(p, SAMPLES // 2)
    distance = abs(python_nonzero[p] - mean) / spread if spread > 0 else 0.0
    say(f"p = {p}: counted {python_nonzero[p]:4d}, expected {mean:7.1f} "
        f"+- {spread:5.1f}  ({distance:.2f} standard deviations away)")
    within = within and (distance < 5.0 if spread > 0 else python_nonzero[p] == 0)
check(within, "the Python counts of nonzero values agree with the birthday formula")
```

For each length, with $N = 1000$, the distance of the count from its expectation is measured in standard deviations (`abs` is the size of a number; the format `:7.1f` writes a decimal number with one digit after the point). The output: 394 against $412.6 \pm 15.6$ (1.19 standard deviations), 186 against $205.8 \pm 12.8$ (1.55), 82 against $77.1 \pm 8.4$ (0.58), 24 against $19.3 \pm 4.3$ (1.09), 3 against $2.4 \pm 1.6$ (0.38), and 0 against exactly 0 for $p = 9$. The check requires every distance to be below 5 standard deviations (a chance of less than one in a million for each count), and exactly 0 where the standard deviation is 0. Thirteenth PASS line.

**In [12], the cost of the determinant (Figure 11a.5).**

```python
lengths = list(range(1, 10))
leibniz_terms = [math.factorial(p) for p in lengths]  # products in the formula
comparisons = [p * (p - 1) // 2 for p in lengths]  # comparisons of the rule
all_pairs = [8 ** (2 * p) for p in lengths]  # all pairs of lists of length p
for p, terms, compare, total in zip(lengths, leibniz_terms, comparisons, all_pairs):
    say(f"p = {p}: Leibniz products {terms:6d}, comparisons of GKD {compare:2d}, "
        f"pairs of lists {total:.3e}")
```

The three rows of the cost table of Section 11.4 for $p = 1$ to 9, printed one line per length (the format `:.3e` writes a number in the form $1.678 \times 10^7$ as `1.678e+07`).

```python
fig, ax = plt.subplots(figsize=(7.4, 4.4))
ax.semilogy(lengths, leibniz_terms, "o-", label="products in the Leibniz formula, $p!$")
ax.semilogy(lengths, [max(c, 0.5) for c in comparisons], "s-",
            label="comparisons made by GKD, $p(p-1)/2$")
ax.semilogy(lengths, all_pairs, "^:", label="all pairs of index lists, $8^{2p}$")
```

`ax.semilogy` draws a curve with a logarithmic vertical axis; `"o-"` means circles joined by a line, `"s-"` squares and a line, `"^:"` triangles and a dotted line. The comparison count 0 of $p = 1$ is drawn at 0.5, because 0 has no place on a logarithmic axis.

```python
ax.axvline(4.5, color="0.5", lw=0.8)  # where exhaustive testing ends
ax.text(4.65, 3e15, "right of this line:\nrandom samples only", fontsize=8,
        va="top")
ax.set_xlabel("length $p$ of the index lists")
ax.set_ylabel("count (logarithmic scale)")
ax.set_title("The work of the literal determinant and of the rule GKD")
ax.legend(loc="upper left", fontsize=8)
save_figure(fig, "cost_of_the_determinant",
            "Work per evaluation of the generalized Kronecker delta for index lists "
            ...)
```

A thin vertical line at $p = 4.5$ separates the lengths tested exhaustively from those tested by samples, with a note beside it (`\n` starts a new line of text); then titles, legend, and the saved figure.

```python
timing_rng = np.random.default_rng(7)
timing_pairs = []
for _ in range(200):
    upper = [int(v) for v in timing_rng.permutation(8)[:7]]  # 7 different labels
    lower = [upper[i] for i in timing_rng.permutation(7)]  # the same, rearranged
    timing_pairs.append((lower, upper))
```

200 pairs of length 7 for the timing, from a second generator with the seed 7: the first 7 entries (`[:7]`) of a random arrangement of the eight labels are 7 different labels, and the lower list is the same labels in another random order. Every one of these pairs has a nonzero value.

```python
start = time.perf_counter()
rule_values = [gkd(lower, upper) for lower, upper in timing_pairs]
rule_seconds = time.perf_counter() - start
start = time.perf_counter()
determinant_values = [int(sp.Matrix(outer_delta(lower, upper)).det())
                      for lower, upper in timing_pairs]  # no memory: all computed
determinant_seconds = time.perf_counter() - start
```

`time.perf_counter()` reads a stopwatch; the difference of two readings is the time between them in seconds. The rule is timed on the 200 pairs, then sympy's exact determinant on the same pairs, computed afresh each time (without the memory of `kdelta`).

```python
check(rule_values == determinant_values,
      "200 pairs of length 7: the rule and sympy's determinant agree")
check(determinant_seconds > 10 * rule_seconds,
      "the rule GKD is more than ten times faster than the determinant (p = 7)")
```

Two checks: the 200 values agree, and the determinants took more than ten times as long as the rule. The times themselves are never printed, so the output stays the same on every run. PASS lines fourteen and fifteen.

*What Figure 11a.5 shows.* Three curves on a logarithmic axis against the length $p$. The circles ($p!$) rise ever more steeply, to 362,880 at $p = 9$; the squares ($p(p-1)/2$) stay small, 36 at $p = 9$; the triangles ($8^{2p}$) rise as a straight line, because a power $64^p$ is a straight line on a logarithmic axis, to $1.8 \times 10^{16}$. Right of the line at $p = 4.5$ only samples can be tested.

**In [13], the Rust program is built, and the command of its self-test.**

```python
program = rust_program("Revision/gkd_lovelock/code/Cargo.toml", "lovelock_gkd")
```

The helper of the set-up cell runs cargo for the crate `Revision/gkd_lovelock/code` and returns the path of the program `lovelock_gkd` (with `.exe` on Windows), named `program` here. When the program is up to date this takes about a second; a first build took a few seconds on the computer that built the book (the crate has no dependencies, so nothing is downloaded). Output: Rust program lovelock_gkd is built and ready.

```python
COMMAND = ["lovelock_gkd", "gkd-selftest", "--exhaustive-max", "4", "--output", "FOLDER"]
say("To repeat the self-test (7 to 13 minutes), run in the folder of the program: "
    + " ".join(COMMAND))
```

`COMMAND` is the list of the words of the command that runs the self-test: the program, the command `gkd-selftest`, the option that makes the lengths 1 to 4 exhaustive, and the folder for the result file; `" ".join(COMMAND)` joins the words with spaces. The cell does not run the command. The self-test takes 7 to 13 minutes on the computer that built the book, most of it in the 200,000 literal determinants of $9 \times 9$ matrices, each a sum of $9! = 362880$ products; that is longer than the limit of 7 minutes that this book sets for one computation. Output: the line with the command

```text
lovelock_gkd gkd-selftest --exhaustive-max 4 --output FOLDER
```

To repeat the self-test yourself, run this command in a terminal, in the folder `Revision/gkd_lovelock/code/target/release` (on Windows the program file is `lovelock_gkd.exe`), with a folder of your choice in place of FOLDER: the file `gkd-selftest.json` that it writes there must equal the record byte for byte.

**In [14], the record of the Rust self-test.**

```python
SELFTEST = "Revision/gkd_lovelock/results/gkd-selftest.json"
written = repository_file(SELFTEST).read_bytes()  # the record of the Rust run
selftest_record = json.loads(written.decode("utf-8"))
say("The record of the Rust self-test (as a table):")
```

`read_bytes()` reads the record as its raw bytes (the next cell uses them again), `decode("utf-8")` turns them into text and `json.loads` into a dictionary. Then a heading line is printed.

```python
rust_rows = {}  # p -> (mode, pairs, nonzero or None, mismatches)
for row in selftest_record["results"]:
    rust_rows[row["p"]] = (row["mode"], row["pairs"], row.get("nonzero"),
                           row["mismatches"])
```

The entry `results` of the record holds one row per length $p$: the mode (`exhaustive` or `random`), the number of pairs, for the random lengths the number of nonzero values, and the number of disagreements between GKD and the literal determinant. `row.get("nonzero")` gives the number of nonzero values, and `None` for an exhaustive row, which has no such entry. The dictionary `rust_rows` keeps each row as a tuple under its length.

```python
for p, (mode, pairs, nonzero, bad) in sorted(rust_rows.items()):
    extra = "" if nonzero is None else f", {nonzero:6d} nonzero"
    say(f"  p = {p}: {mode:10s} {pairs:9d} pairs{extra}; disagreements: {bad}")
```

The rows are printed in the order of $p$ as a table. The output shows 64, 4096, 262144 and 16777216 pairs compared exhaustively for $p = 1$ to 4, and 200,000 random pairs for each $p = 5$ to 9 with 20538, 7812, 1949, 244 and 0 nonzero values; every disagreement count is 0.

```python
check(selftest_record["program"] == "lovelock_gkd gkd-selftest"
      and selftest_record["verdict"] == "SUCCESS",
      "the record of the Rust program lovelock_gkd gkd-selftest has the verdict "
      "SUCCESS", record=SELFTEST)
check(sorted(rust_rows) == list(range(1, 10))
      and all(row[3] == 0 for row in rust_rows.values())
      and rust_rows[4][:2] == ("exhaustive", 16777216),
      "Rust: GKD equals the literal determinant for every tested pair, p = 1 to 9",
      record=SELFTEST)
check(program.is_file(), "the program lovelock_gkd that repeats the self-test is built")
```

The first check requires the program name of the record and its verdict SUCCESS. The second requires a row for every length 1 to 9, no disagreement in any row (`row[3]` is the fourth entry, the mismatches) and the exhaustive test of all 16,777,216 pairs of length 4 (`[:2]` takes the first two entries of the row). The third requires that the program file that repeats the self-test exists (`is_file()`). PASS lines sixteen to eighteen.

**In [15], the self-test against the birthday formula (Figure 11a.6).**

```python
selftest = json.loads(written.decode("utf-8"))
rust_nonzero = {row["p"]: row["nonzero"] for row in selftest["results"]
                if row["mode"] == "random"}
```

The bytes just compared are decoded as text and read as JSON. A **dictionary comprehension** collects, for every random length, its number of nonzero values.

```python
agree = True
for p, nonzero in sorted(rust_nonzero.items()):
    mean, spread = expected_nonzero(p, 100000)
    distance = abs(nonzero - mean) / spread if spread > 0 else 0.0
    say(f"Rust p = {p}: counted {nonzero:6d}, expected {mean:8.1f} +- {spread:6.1f}"
        f"  ({distance:.2f} standard deviations away)")
    agree = agree and (distance < 5.0 if spread > 0 else nonzero == 0)
check(selftest["verdict"] == "SUCCESS" and agree and rust_nonzero[9] == 0,
      "the Rust counts of nonzero values agree with the birthday formula")
```

The same comparison as in In [11], now with $N = 100000$ samples of each kind: 20538 against $20582.9 \pm 128.0$ (0.35 standard deviations), 7812 against $7711.6 \pm 84.4$ (1.19), 1949 against $1927.2 \pm 43.5$ (0.50), 244 against $240.9 \pm 15.5$ (0.20), and 0 for $p = 9$. The check also requires the verdict SUCCESS of the file. Nineteenth PASS line.

```python
lengths_1_to_8 = np.arange(1, 9)  # r_p is drawn where it is not zero
fig, ax = plt.subplots(figsize=(7.4, 4.4))
ax.semilogy(lengths_1_to_8, [all_different(p) for p in lengths_1_to_8], "k-",
            label="chance that $p$ labels out of 8 are all different, $r_p$")
```

`np.arange(1, 9)` is the array $1, \dots, 8$; the black line (`"k-"`) is $r_p$ on a logarithmic axis.

```python
python_points = [p for p in python_nonzero if python_nonzero[p] > 0]
ax.semilogy(python_points, [python_nonzero[p] / (SAMPLES // 2)
                            for p in python_points], "o",
            label="Python: nonzero values / 1000 rearranged pairs")
rust_points = [p for p in rust_nonzero if rust_nonzero[p] > 0]
ax.semilogy(rust_points, [rust_nonzero[p] / 100000 for p in rust_points], "s",
            fillstyle="none", markersize=10,
            label="Rust: nonzero values / 100000 rearranged pairs")
```

The measured fractions: the nonzero values of all the samples of one length divided by the number of rearranged samples, dots for Python and large open squares for Rust. Lengths with no nonzero value are left out, because 0 has no place on a logarithmic axis.

```python
ax.plot([9], [1e-6], "v", color="black", markersize=9)  # marks the zeros of p = 9
ax.text(9.0, 2.2e-6, "p = 9: none\n(0 of 1000,\n0 of 100000)", fontsize=8,
        ha="center", va="bottom")
ax.axvline(8.5, color="0.5", lw=0.8)
ax.text(8.6, 0.3, "more than 8\nlabels: always\na repetition", fontsize=8, va="top")
```

A black triangle at the bottom edge and a note mark the zeros of $p = 9$; a vertical line at 8.5 with a note marks where every list must repeat a label.

```python
ax.set_xlim(0.5, 10.0)
ax.set_ylim(5e-7, 2.0)
ax.set_xlabel("length $p$ of the index lists")
ax.set_ylabel("fraction (logarithmic scale)")
ax.set_title("Nonzero deltas among rearranged random pairs")
ax.legend(loc="lower left", fontsize=8)
save_figure(fig, "all_labels_different",
            "The chance $r_p = 8!/((8 - p)!\\, 8^p)$ that $p$ random labels out of "
            ...)
```

The ranges of the two axes, titles, legend and the saved figure (in the caption string a doubled backslash stands for one backslash).

*What Figure 11a.6 shows.* The chance $r_p$ falls from 1 at $p = 1$ to $0.0024$ at $p = 8$; the dots and squares lie on the line, within their random scatter. The independent samples add at most $q_4 = 40320/8^8 \approx 0.0024$, too little to see. For $p = 9$ both tests found no nonzero value, as the pigeonhole principle demands.

**In [16], the quoted records once more.**

```python
def verdicts(path):
    data = json.loads(repository_file(path).read_text(encoding="utf-8"))
    checks = data["checks"]
    if isinstance(checks, dict):  # name -> {"passed": true or false, ...}
        return {name: "PASS" if entry["passed"] else "FAIL"
                for name, entry in checks.items()}
    return {entry["name"]: entry["verdict"] for entry in checks}  # a list of entries
```

A helper (docstring left out) that returns, for one report, a dictionary from the name of each check to PASS or FAIL. The Revision reports store their checks in one of two forms, and `isinstance(checks, dict)` tells which: a dictionary of entries with a field `passed`, or a list of entries with a `name` and a `verdict`.

```python
RECORDS = "Revision/gkd_lovelock/results"  # the folder of the Revision records
QUOTED = {  # report -> the checks that this notebook quotes from it
    "python-lovelock-report.json": [
        "gkd_examples", "gkd_literal_equals_cofactor_expansion",
        "gkd_nine_indices_in_eight_dimensions_vanish"],
    "wolfram-gkd-report.json": [
        "gkd_equals_kdelta_exhaustive_length_1",
        "gkd_equals_kdelta_exhaustive_length_2",
        "gkd_equals_kdelta_exhaustive_length_3"],
}
```

The checks that the notebook's text quotes, by report.

```python
for report_name, names in QUOTED.items():
    found = verdicts(f"{RECORDS}/{report_name}")
    for name in names:
        say(f"{report_name}: {name} {found.get(name, 'MISSING')}")
    check(all(found.get(name) == "PASS" for name in names),
          f"the {len(names)} checks quoted from {report_name} are there and PASS",
          record=f"{RECORDS}/{report_name}, checks " + ", ".join(names))
```

For each report every quoted check is printed with its verdict (`get(name, 'MISSING')` gives MISSING for a name that is not there), and the check requires all of them to be present with PASS. `", ".join(names)` joins the names with commas. Two PASS lines, twenty and twenty-one.

```python
provenance = repository_file(
    f"{RECORDS}/PROVENANCE_OF_THE_COMPUTATION.md").read_text(encoding="utf-8")
definition = ("[lower_, upper_] /; Length[lower] == Length[upper] := "
              "Det[Outer[delta, lower, upper]]")  # after the name of the delta
check(definition in provenance,
      "the record quotes the author's definition as section 4 of this notebook "
      "does",
      record=f"{RECORDS}/PROVENANCE_OF_THE_COMPUTATION.md")
```

The record of the author's definition is read, and the check requires the definition, from the bracket after its name on, to occur in it exactly as the notebook quotes it in its own section 4 (the name itself is written with a Greek letter in the record). Two strings written one after the other inside brackets are joined into one by Python. Twenty-second PASS line.

```python
order_three = [row for row in json.loads(repository_file(
    f"{RECORDS}/lovelock-report.json").read_text(encoding="utf-8"))["counters"]
    if row["k"] == 3][0]
report("GKD calls of the order-3 Lovelock sum (record)", order_three["gkdCalls"])
check(order_three["gkdCalls"] == 322560,
      "the order-3 Lovelock sum calls GKD 322560 times, as section 4 of this "
      "notebook says",
      record=f"{RECORDS}/lovelock-report.json, counters, k = 3, gkdCalls")
```

The Rust report's counters are read and the row of order 3 is taken; its number of GKD calls for the corrected metric, 322,560, is printed (RESULT GKD calls of the order-3 Lovelock sum (record) = 322560) and checked (the number quoted in the notebook's section 4 and explained in Section 11.12). Twenty-third PASS line.

**In [17], the end.**

```python
figure_files = [f"11a_{k}_{name}.png" for k, name in enumerate(
    ["outer_delta_matrices", "six_permutations", "gkd_map_length_two",
     "value_counts", "cost_of_the_determinant", "all_labels_different"], 1)]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_files),
      "all six figure files of the notebook exist")
all_checks_passed()
```

`enumerate(..., 1)` numbers the six figure names from 1, which gives the six file names; the check requires all six files to exist in the figures folder (PASS line twenty-four), and `all_checks_passed()` prints the last line, ALL 24 CHECKS PASSED (notebook 11a). The 24 checks are: 2 in In [2], 1 each in In [3], In [4], In [5], In [6], 2 in In [7], 1 each in In [8] and In [9], 2 in In [10], 1 in In [11], 2 in In [12], 3 in In [14], 1 in In [15], 4 in In [16] and 1 in In [17].

### 11.10 The curvature that the Lovelock sums need

The Lovelock tensors are built from the Riemann tensor. Chapter 3 computed it for the author's metric (Sections 3.23 to 3.25); here we collect what the sums need, in the convention of every Revision record (the convention of Misner, Thorne and Wheeler, Section 3.17):

$$
\Gamma^a{}_{bc} = \tfrac12\,g^{aa}\big(\partial_b g_{ac} + \partial_c g_{ab} - \partial_a g_{bc}\big),\qquad
R^a{}_{bcd} = \partial_c\Gamma^a{}_{db} - \partial_d\Gamma^a{}_{cb} + \sum_e\big(\Gamma^a{}_{ce}\Gamma^e{}_{db} - \Gamma^a{}_{de}\Gamma^e{}_{cb}\big),
$$

and $R^{ab}{}_{cd} = g^{bb}R^a{}_{bcd}$ (no sum; for a diagonal metric the general $\sum_e g^{be}R^a{}_{ecd}$ keeps only $e = b$). The form $R^{ab}{}_{cd}$, with two labels up and two down, is the one the Lovelock sums use. It changes sign when the two upper labels or the two lower labels are exchanged:

$$
R^{ab}{}_{cd} = -R^{ba}{}_{cd} = -R^{ab}{}_{dc}
$$

(the Rust report `lovelock-report.json`, check `riemann_antisymmetry`; Section 3.17 proves it). In particular $R^{aa}{}_{cd} = 0$: a component with two equal upper labels or two equal lower labels vanishes.

**Scale factors and their rates.** Write each diagonal entry of the corrected metric as $g_{aa} = \eta_a f_a^2$, with $\eta_a = +1$ for $x_0, x_1, x_2, x_3$, $\eta_a = -1$ for $x_4, x_5, x_6, x_7$, and the scale factor $f_a > 0$:

$$
f_0 = e^{-a_4}b_4^{1/2}|\cot z|,\qquad f_i = e^{a_4}\ (i = 1, 2, 3),\qquad f_4 = 1,\qquad f_t = e^{-a_4}b_4^{1/2}(\sin^2z)^{1/12}\ (t = 5, 6, 7).
$$

Every scale factor is a function of $x_4$ times a function of $x_0$. Their logarithmic derivatives, the **rates**, follow from $\ln f_t = -a_4 + \frac12\ln b_4 + \frac1{12}\ln\sin^2z$ and its companions:

$$
\partial_4\ln f_i = a_4',\qquad \partial_4\ln f_0 = \partial_4\ln f_t = -a_4' + \tfrac12u = h_4,\qquad \partial_0\ln f_i = 0,\qquad \partial_0\ln f_t = H\cot z
$$

(the derivative of $\frac12\ln b_4$ is $\frac12b_4'/b_4 = \frac12u$; the derivative of $\frac1{12}\ln\sin^2z$ with respect to $x_0$ is $\frac1{12}\cdot\frac{2\sin z\cos z}{\sin^2z}\cdot 6H = H\cot z$, by the chain rule with $dz/dx_0 = 6H$). The hidden direction and the extra times change in time at the same rate $h_4$: this is the block.

**The Christoffel symbols (PROVED).** For a diagonal metric the formula keeps only the terms in which two of the labels $a, b, c$ are equal. The record lists 21 nonzero symbols with $b \le c$ (`curvature.json`, entry `christoffelNonzero_b_le_c`; Notebook 11b, In [6], recomputes and prints all 21): with $i = 1, 2, 3$ and $t = 5, 6, 7$,

$$
\begin{aligned}
&\Gamma^{x_i}{}_{x_ix_4} = a_4',\qquad \Gamma^{x_0}{}_{x_0x_4} = \Gamma^{x_t}{}_{x_4x_t} = \tfrac12u - a_4',\qquad \Gamma^{x_t}{}_{x_0x_t} = H\cot z,\\
&\Gamma^{x_4}{}_{x_ix_i} = a_4'e^{2a_4},\qquad \Gamma^{x_4}{}_{x_tx_t} = (a_4' - \tfrac12u)\,e^{-2a_4}b_4(\sin^2z)^{1/6},\\
&\Gamma^{x_4}{}_{x_0x_0} = -(a_4' - \tfrac12u)\,e^{-2a_4}b_4\cot^2z,\qquad \Gamma^{x_0}{}_{x_tx_t} = H(\sin^2z)^{1/6}\tan z,\\
&\Gamma^{x_0}{}_{x_0x_0} = -6H(\cot z + \tan z),
\end{aligned}
$$

that is $3 + 1 + 3 + 3 + 3 + 3 + 1 + 1 + 3 = 21$ symbols. Two of them, which we need below, line by line. First,

$$
\Gamma^{x_t}{}_{x_0x_t} = \tfrac12\,g^{tt}\,\partial_0g_{tt} = \partial_0\ln f_t = H\cot z
$$

(the formula with $a = c = t$, $b = x_0$; then $\frac12g^{tt}\partial_0g_{tt} = \frac12\partial_0\ln|g_{tt}| = \partial_0\ln f_t$; then the rate above). Second, with $a = x_0$ and $b = c = t$ only the last term of the formula survives:

$$
\Gamma^{x_0}{}_{x_tx_t} = -\tfrac12\,g^{00}\,\partial_0g_{tt} = -\tfrac12\,e^{2a_4}b_4^{-1}\tan^2z\cdot\big(-e^{-2a_4}b_4\,2H\cot z\,(\sin^2z)^{1/6}\big) = H\tan z\,(\sin^2z)^{1/6}
$$

($g^{00} = 1/g_{00} = e^{2a_4}b_4^{-1}\tan^2z$; $\partial_0g_{tt} = -e^{-2a_4}b_4\,\partial_0(\sin^2z)^{1/6}$, and by the chain rule $\partial_0(\sin^2z)^{1/6} = \frac16(\sin^2z)^{-5/6}\cdot 2\sin z\cos z\cdot 6H = 2H\cot z\,(\sin^2z)^{1/6}$; then $e^{2a_4}e^{-2a_4} = 1$, $b_4^{-1}b_4 = 1$ and $\tan^2z\cot z = \tan z$).

**No mixed component (PROVED).** The Riemann tensor of a general metric has components of every kind. For our metric only the curvatures of coordinate planes survive; we show it for the components that could couple the time to the hidden direction, $R^{x_4c}{}_{x_0c}$ with $c$ one of the six directions of 3-space and of the extra times. The formula for $R^a{}_{bcd}$ with $a = x_4$, $b = c$, $c = x_0$, $d = c$ (we write the label $c$ of the direction also as the third label) reads

$$
R^4{}_{c0c} = \partial_0\Gamma^4{}_{cc} - \partial_c\Gamma^4{}_{0c} + \sum_e\Gamma^4{}_{0e}\Gamma^e{}_{cc} - \sum_e\Gamma^4{}_{ce}\Gamma^e{}_{0c}
$$

(the definition with these four labels). Nothing depends on $x_c$, and $\Gamma^4{}_{0c} = 0$ for $c \ne x_0$ (the metric has no entry $g_{0c}$), so the second term is 0. In the first sum only $e = x_0$ survives, because $\Gamma^4{}_{04} = \frac12g^{44}\partial_0g_{44} = 0$ ($g_{44} = -1$ is constant); in the last sum only $e = c$ survives:

$$
R^4{}_{c0c} = \partial_0\Gamma^4{}_{cc} + \Gamma^4{}_{00}\,\Gamma^0{}_{cc} - \Gamma^4{}_{cc}\,\Gamma^c{}_{0c} .
$$

The Christoffel formula gives, with $g_{aa} = \eta_af_a^2$ and $g^{44} = -1$,

$$
\begin{aligned}
&\Gamma^4{}_{cc} = -\tfrac12g^{44}\partial_4g_{cc} = \eta_cf_c^2\,\partial_4\ln f_c,\qquad \Gamma^4{}_{00} = f_0^2\,\partial_4\ln f_0,\\
&\Gamma^0{}_{cc} = -\tfrac12g^{00}\partial_0g_{cc} = -\frac{\eta_cf_c^2}{f_0^2}\,\partial_0\ln f_c,\qquad \Gamma^c{}_{0c} = \partial_0\ln f_c
\end{aligned}
$$

(each time $\partial g_{aa} = \eta_a\,\partial f_a^2 = 2\eta_af_a^2\,\partial\ln f_a$; and $\eta_0 = +1$). Insert them; the derivative of the first product is $\partial_0(\eta_cf_c^2\,\partial_4\ln f_c) = \eta_cf_c^2\big(2\,\partial_0\ln f_c\,\partial_4\ln f_c + \partial_0\partial_4\ln f_c\big)$:

$$
R^4{}_{c0c} = \eta_cf_c^2\Big(2\,\partial_0\ln f_c\,\partial_4\ln f_c + \partial_0\partial_4\ln f_c - \partial_4\ln f_0\,\partial_0\ln f_c - \partial_4\ln f_c\,\partial_0\ln f_c\Big)
$$

(the three terms with the common factor $\eta_cf_c^2$ taken out). Collect the products, and raise the second label with $g^{cc} = 1/(\eta_cf_c^2)$:

$$
R^{x_4c}{}_{x_0c} = \partial_0\ln f_c\,\big(\partial_4\ln f_c - \partial_4\ln f_0\big) + \partial_0\partial_4\ln f_c .
$$

The last term is 0 because $\ln f_c$ is a function of $x_4$ plus a function of $x_0$ (the product $f_c = A(x_4)B(x_0)$ has $\ln f_c = \ln A + \ln B$). So each possible mixed component is a product of two factors: how the scale factor of $c$ changes along $x_0$, and how its rate in time differs from that of the hidden direction. For the corrected metric:

- for 3-space, $\partial_0\ln f_i = 0$: $e^{2a_4}$ does not depend on $x_0$;
- for the extra times, $\partial_4\ln f_t - \partial_4\ln f_0 = h_4 - h_4 = 0$: they share the rate of the hidden direction.

Every term vanishes, for every history and every real $z$: $R^{x_4c}{}_{x_0c} = 0$. The other candidate, $R^{x_0c}{}_{x_4c}$, vanishes too: for a diagonal metric $R^{ab}{}_{cd} = g^{aa}g^{bb}R_{abcd}$ (both upper labels raised), and the pair symmetry $R_{abcd} = R_{cdab}$ (Section 3.17) gives $R^{x_0c}{}_{x_4c} = g^{00}g^{cc}R_{0c4c} = g^{00}g^{cc}R_{4c0c} = (g^{00}/g^{44})\,R^{x_4c}{}_{x_0c} = 0$. For a diagonal metric that depends on $x_0$ and $x_4$ only, these are the only components that are not plane curvatures (`Revision/docs/METRIC_SELF_CONSISTENCY.md`, section 2.1). The record confirms the result exactly: its 112 nonzero $R^{ab}{}_{cd}$ are all of the form $R^{ab}{}_{ab}$ or $R^{ab}{}_{ba}$ (`lovelock-report.json`, check `mixed_riemann_only_sectional`; `python-lovelock-report.json`, check of the same name). Notebook 11b computes the two factors for every direction (In [11], Figure 11b.4) and finds only plane curvatures among its own 112 components (In [8]; Figure 11b.3, drawn by In [10]).

*Why the metric was corrected (dated history).* In the metric of 2026-10-14, withdrawn on 2026-10-16, 3-space carried the factor $\sin^{1/3}z = (\sin^2z)^{1/6}$ and the hidden direction had $g_{00} = \cot^2z$ without any time dependence. Then both factors were nonzero: $R^{x_4x_i}{}_{x_0x_i} = H\cot z\cdot a_4'$ for 3-space and $R^{x_4x_t}{}_{x_0x_t} = H\cot z\,(\frac12u - a_4')$ for the extra times. Their sum, the Ricci component $R^{x_4}{}_{x_0}$, was $3Ha_4'\cot z + 3H\cot z(\frac12u - a_4') = \frac32H\cot z\,u$, and so the Einstein tensor had the off-diagonal component $G^{x_4}{}_{x_0} = \frac32H\cot z\,b_4'/b_4$, which a diagonal source cannot match unless $b_4' = 0$ (`Revision/docs/METRIC_SELF_CONSISTENCY.md`, sections 2.1 and 2.3). The corrected metric removes every such component at every Lovelock order (Section 11.21).

**The plane curvatures (PROVED).** For two different directions $a$ and $b$, $K(a, b) = R^{ab}{}_{ab}$ (no sum) is the curvature of their coordinate plane. With $i$ standing for a 3-space direction and "block" for one of $x_0, x_5, x_6, x_7$, the 28 planes are (`curvature.json`, entry `riemannMixedNonzero`; Notebook 11b, In [7] to In [9]):

| plane | how many | $K(a, b)$ | at $x_4 = 0$ on the history of the record |
| --- | --- | --- | --- |
| two 3-space directions $(i, i')$ | 3 | $a_4'^2$ | $H^2$ |
| a 3-space direction and the time $(i, x_4)$ | 3 | $a_4'^2 + a_4''$ | $H^2$ |
| a 3-space direction and a block direction | 12 | $-a_4'(a_4' - \frac12u)$ | $-H^2/3$ |
| the time and a block direction | 4 | $(a_4' - \frac12u)^2 - a_4'' + \frac12v$ | $H^2/9$ |
| two block directions | 6 | $(a_4' - \frac12u)^2 - H^2k$ | $-8H^2/9$ |

($3 + 3 + 12 + 4 + 6 = 28$; on the history of the record at $x_4 = 0$, $a_4' = H$, $u = \frac43H$, $a_4'' = v = 0$ and $k = 1$, so $a_4' - \frac12u = \frac13H$.) Every plane gives four nonzero components, $R^{ab}{}_{ab} = R^{ba}{}_{ba} = K(a, b)$ and $R^{ab}{}_{ba} = R^{ba}{}_{ab} = -K(a, b)$: $4\cdot 28 = 112$ (record check `riemann_antisymmetry`, "112 nonzero entries"). Figure 11b.2 draws the 28 numbers as an $8 \times 8$ table at this moment and at the same moment with $a_4'' = v = H^2$ added (Notebook 11b, In [9]). The hidden direction behaves exactly like an extra time: every plane that contains $x_0$ has the curvature of the same plane with an extra time in place of $x_0$.

We derive the last row line by line, because it shows where $k$ comes from. Take two different extra times $t$ and $t'$. In the formula for $R^t{}_{t'tt'}$ the derivative terms vanish ($\Gamma^t{}_{t't'} = 0$ and $\Gamma^t{}_{tt'} = 0$ for $t \ne t'$, and nothing depends on $x_t$), and so does the last sum (every $\Gamma^t{}_{t'e}$ is 0); in the remaining sum only $e = x_0$ and $e = x_4$ survive:

$$
R^t{}_{t'tt'} = \Gamma^t{}_{t0}\,\Gamma^0{}_{t't'} + \Gamma^t{}_{t4}\,\Gamma^4{}_{t't'}
$$

(the definition, with the vanishing terms dropped). Insert the Christoffel symbols listed above:

$$
\begin{aligned}
R^t{}_{t'tt'} &= H\cot z\cdot H\tan z\,(\sin^2z)^{1/6} + (\tfrac12u - a_4')\cdot(a_4' - \tfrac12u)\,e^{-2a_4}b_4(\sin^2z)^{1/6}\\
&= \big(H^2 - (a_4' - \tfrac12u)^2e^{-2a_4}b_4\big)(\sin^2z)^{1/6}
\end{aligned}
$$

($\cot z\tan z = 1$; the common factor $(\sin^2z)^{1/6}$ taken out). Raise the second label with $g^{t't'} = -e^{2a_4}b_4^{-1}(\sin^2z)^{-1/6}$:

$$
R^{tt'}{}_{tt'} = -H^2e^{2a_4}b_4^{-1} + (a_4' - \tfrac12u)^2 = (a_4' - \tfrac12u)^2 - H^2k
$$

(the factor $(\sin^2z)^{1/6}$ cancels, and $e^{2a_4}/b_4 = k$). The first part, $-H^2k$, is the constant curvature $-H^2$ of the block of Chapter 3, divided by the square $e^{-2a_4}b_4$ of its scale factor; the second part comes from the deflation of the block. Every $x_0$-dependence has cancelled.

**The Ricci tensor, the Ricci scalar and the Einstein tensor (PROVED).** For a diagonal $R^{ab}{}_{cd}$ made of plane curvatures, $R^h{}_h = \sum_cK(h, c)$ (the definition of the Ricci tensor; only $c \ne h$ contributes), and every off-diagonal $R^h{}_j$ is zero. From the table, line by line:

$$
\begin{aligned}
R^{x_1}{}_{x_1} &= 2a_4'^2 + (a_4'^2 + a_4'') + 4\cdot\big(-a_4'(a_4' - \tfrac12u)\big) = a_4'' - a_4'^2 + 2a_4'u,\\
R^{x_4}{}_{x_4} &= 3(a_4'^2 + a_4'') + 4\big((a_4' - \tfrac12u)^2 - a_4'' + \tfrac12v\big) = 7a_4'^2 - 4a_4'u - a_4'' + u^2 + 2v,\\
R^{x_0}{}_{x_0} &= 3\cdot\big(-a_4'(a_4' - \tfrac12u)\big) + \big((a_4' - \tfrac12u)^2 - a_4'' + \tfrac12v\big) + 3\big((a_4' - \tfrac12u)^2 - H^2k\big)\\
&= a_4'^2 - \tfrac52a_4'u - a_4'' + u^2 + \tfrac12v - 3H^2k
\end{aligned}
$$

(for $x_1$: two planes inside 3-space, one with the time, four with the block; for $x_4$: three planes with 3-space and four with the block; for $x_0$: three with 3-space, one with the time, three inside the block; then $(a_4' - \frac12u)^2 = a_4'^2 - a_4'u + \frac14u^2$ multiplied out and equal powers collected). $R^{x_5}{}_{x_5}$ equals $R^{x_0}{}_{x_0}$ (the same planes with $x_0$ and $x_5$ exchanged). The Ricci scalar is the sum of the eight diagonal entries:

$$
R = 3R^{x_1}{}_{x_1} + R^{x_4}{}_{x_4} + 4R^{x_0}{}_{x_0} = 8a_4'^2 - 8a_4'u - 2a_4'' - 12H^2k + 5u^2 + 4v
$$

(collect each monomial: $a_4''$: $3 - 1 - 4 = -2$; $a_4'^2$: $-3 + 7 + 4 = 8$; $a_4'u$: $6 - 4 - 10 = -8$; $u^2$: $1 + 4 = 5$; $v$: $2 + 2 = 4$; $H^2k$: $-12$). This is the record's `ricciScalar` (`curvature.json`; Notebook 11b, In [8]). Subtracting $\frac12R$ from each diagonal entry gives the Einstein tensor,

$$
\begin{aligned}
G^{x_1}{}_{x_1} &= 2a_4'' - 5a_4'^2 + 6a_4'u + 6H^2k - \tfrac52u^2 - 2v,\qquad G^{x_4}{}_{x_4} = 3a_4'^2 + 6H^2k - \tfrac32u^2,\\
G^{x_0}{}_{x_0} &= G^{x_5}{}_{x_5} = -3a_4'^2 + \tfrac32a_4'u + 3H^2k - \tfrac32u^2 - \tfrac32v
\end{aligned}
$$

(record `curvature.json`, entry `einsteinMixed`; for example $G^{x_4}{}_{x_4} = 7a_4'^2 - 4a_4'u - a_4'' + u^2 + 2v - (4a_4'^2 - 4a_4'u - a_4'' - 6H^2k + \frac52u^2 + 2v) = 3a_4'^2 + 6H^2k - \frac32u^2$), with every off-diagonal component zero.

**Three facts used below (PROVED).**

- Every nonzero $R^{ab}{}_{cd}$ is plus or minus one of the five plane curvatures of the table: a polynomial in the six variables $H$, $a_4'$, $a_4''$, $u$, $v$, $k$, free of $x_0$ (record `lovelock-report.json`, check `mixed_riemann_free_of_x0`; `python-lovelock-report.json`, check `mixed_riemann_free_of_x0`; Notebook 11b, In [7]).
- **Weight 2.** Count $H$, $a_4'$ and $u$ as 1, $a_4''$ and $v$ as 2, and $k$ as 0 (each count is one inverse length: $z = 6Hx_0$ is a pure number, so $H$ is an inverse length; $a_4$ and $\ln b_4$ are pure numbers, so $a_4'$ and $u = (\ln b_4)'$ are inverse lengths and $a_4''$, $v$ inverse lengths squared; $k = e^{2a_4}/b_4$ is a pure number). Then every plane curvature of the table has the weight 2: curvature has the dimension $1/\text{length}^2$.
- **Labels.** Every nonzero entry carries the same pair of labels up and down. The entries that contain $a_4''$ or $v$ are exactly the planes with the time $x_4$; the entries that contain $k$ are exactly the planes inside the block.

### 11.11 Lovelock's equation (4.38): the three Lovelock tensors

**The formula.** The author's notebook contains, as the cell stored in the file as In[101] (his In[68]), an image of equation (4.38) of the book of Lovelock and Rund; the Revision rendered it to `Revision/gkd_lovelock/results/notebook-in68-image.png` and read the formula from that picture (record `Revision/gkd_lovelock/results/PROVENANCE_OF_THE_COMPUTATION.md`). For a space of $n = 2m$ dimensions it reads, as programmed in the record (`Revision/gkd_lovelock/code/src/lovelock.rs`),

$$
A^{lh} = \sqrt{|\det g|}\sum_{k=1}^{m-1}\alpha_{(k)}\,g^{jl}\,\delta^{h\,h_1\dots h_{2k}}_{j\,j_1\dots j_{2k}}\,R^{j_1j_2}{}_{h_1h_2}\cdots R^{j_{2k-1}j_{2k}}{}_{h_{2k-1}h_{2k}} + \lambda\sqrt{|\det g|}\,g^{lh},
$$

with constants $\alpha_{(k)}$ and $\lambda$, and a sum over every label that appears once up and once down ($j$ and the $4k$ labels $h_1, \dots, h_{2k}, j_1, \dots, j_{2k}$). For the corrected metric $\sqrt{|\det g|} = e^{-a_4}b_4^2|\cot z|(\sin^2z)^{1/4}$ (Section 11.5). The building blocks are, for each **order** $k$, the **Lovelock tensor**

$$
P_{(k)}{}^h{}_j = \sum\delta^{h\,h_1\dots h_{2k}}_{j\,j_1\dots j_{2k}}\,R^{j_1j_2}{}_{h_1h_2}\,R^{j_3j_4}{}_{h_3h_4}\cdots R^{j_{2k-1}j_{2k}}{}_{h_{2k-1}h_{2k}}
$$

(the sum over the $4k$ labels $h_1, \dots, h_{2k}, j_1, \dots, j_{2k}$; $h$ and $j$ are free), the **Lovelock scalar**, the same sum without the free pair,

$$
L_{(k)} = \sum\delta^{h_1\dots h_{2k}}_{j_1\dots j_{2k}}\,R^{j_1j_2}{}_{h_1h_2}\cdots R^{j_{2k-1}j_{2k}}{}_{h_{2k-1}h_{2k}},
$$

and the **density** $A_{(k)}{}^{lh} = \sqrt{|\det g|}\,g^{ll}\,P_{(k)}{}^h{}_l$ (no sum; diagonal metric). Read the generalized delta carefully: its upper list $(h, h_1, \dots, h_{2k})$ collects the LOWER labels of the curvature factors, and its lower list $(j, j_1, \dots, j_{2k})$ their UPPER labels. In the language of GKD,

$$
P_{(k)}{}^h{}_j = \sum\mathrm{GKD}\big([j, j_1, \dots, j_{2k}],\,[h, h_1, \dots, h_{2k}]\big)\,\prod_{i=1}^{k}R^{j_{2i-1}j_{2i}}{}_{h_{2i-1}h_{2i}} ,
$$

the lower list first, as in the author's `kδ[lower, upper]`. The matrix of the exchanged lists, with the entries $\delta(u_i, l_j)$, is the transpose of $M$, and a matrix and its transpose have the same determinant (rule 2 of Section 1.20); so exchanging the two lists does not change the value. The record of the field equations writes them in the other order (`Revision/field_equations_a4/a4-equations.json`, key `conventions`, entry `lovelock`).

**Which orders exist (PROVED).** The delta of order $k$ has $2k + 1$ labels in each list. In eight dimensions ($m = 4$) the sum runs over $k = 1, 2, 3$, and the order $k = 4$, with nine labels, vanishes identically by the pigeonhole principle (Section 11.4; record check `k4_tensor_vanishes`). So there are exactly three Lovelock tensors in eight dimensions. The scalar $L_{(4)}$, with eight labels per list, does not vanish: it is the **Euler density** of eight dimensions, and only its tensor $P_{(4)}$ is zero. The name comes from a classical theorem that this book quotes and does not prove (ASSUMED): in a space of even dimension $n = 2m$ the Lovelock scalar of order $m$ is called the Euler density, because for a **closed** space (finite and without an edge, like the surface of a ball) with a positive-definite metric (every squared length positive, unlike the author's metric) its integral over the whole space, with the volume factor $\sqrt{|\det g|}$, is a constant times the **Euler characteristic**: a whole number that depends only on the shape of the space (2 for the surface of a ball, 0 for the surface of a ring) and does not change when the metric is deformed (the Chern-Gauss-Bonnet theorem). A quantity whose integral does not change when the metric changes gives no field equation; this agrees with $P_{(4)} = 0$, which the pigeonhole principle proved above for every metric. For the corrected metric the program prints $L_{(4)}$ as a polynomial of 25 terms in the six variables (Notebook 11b, In [3] counts the terms and In [22] prints the polynomial); on the history of the record it is

$$
L_{(4)} = \frac{2048}{27}\big(729k^2 - 378k + 25\big)H^8,\qquad k = e^{2Hx_4/3}
$$

(Notebook 11b, In [22]).

**The usual normalisation.** Books on gravity use the normalised tensors

$$
E_{(k)}{}^h{}_j = -\frac{1}{2^{k+1}}\,P_{(k)}{}^h{}_j ,
$$

because then $E_{(1)}$ is exactly Einstein's tensor $G$ (Section 11.14). The field equations of Chapter 12 are $\sum_{k=1}^{3}\alpha_kE_{(k)}{}^\mu{}_\nu + \Lambda\delta^\mu_\nu = \kappa T^\mu{}_\nu$, with $\alpha_1 = 1$, $\alpha_2 = \alpha_3 = 0$ for Einstein's gravity (record `Revision/field_equations_a4/a4-equations.json`, key `conventions`, entry `fieldEquations`). Any other normalisation is absorbed into the constants $\alpha_k$.

**What Lovelock proved (quoted, ASSUMED in general).** For every metric each $P_{(k)}$ has zero covariant divergence, $\sum_h\nabla_hP_{(k)}{}^h{}_j = 0$, and is symmetric once its upper label is lowered, $g_{hh}P_{(k)}{}^h{}_j = g_{jj}P_{(k)}{}^j{}_h$ (for a diagonal metric); and every tensor with these properties that is built from the metric and its first and second derivatives is a combination of the $P_{(k)}$ and of $\delta^h_j$. We do not prove this theorem. For the corrected metric both properties are PROVED by exact computation in the record: checks `k1_divergence_free` to `k3_divergence_free` and `k1_symmetric` to `k3_symmetric` of `Revision/gkd_lovelock/results/lovelock-report.json` and of `Revision/gkd_lovelock/results/python-lovelock-report.json` (the symmetry makes $A_{(k)}{}^{lh} = A_{(k)}{}^{hl}$). Section 11.22 writes out what zero divergence means for the components.

**Weight $2k$ (PROVED).** The generalized delta is a pure number, and each of the $k$ curvature factors has the weight 2 (Section 11.10). So every term of $P_{(k)}$ has the weight $2k$: the tensor of order $k$ has the dimension $1/\text{length}^{2k}$. The three orders can be added in one equation only with constants $\alpha_k$ of different dimensions; the record uses the author's weights $\alpha_k = w_k/H^{2k}$ with the pure numbers $w = (1, \frac1{32}, \frac1{1152})$ and $\Lambda = -10$ (record `a4-equations.json`, key `exponentialHistory`, entry `authorWeights`), so that every term $\alpha_kE_{(k)}$ of the field equations is a pure number (Section 11.23 uses them).

### 11.12 Organising the sum: only nonzero curvature, no repeated label

**How large the literal sum is.** For one component $(h, j)$ the sum over the $4k$ labels $h_1, \dots, h_{2k}, j_1, \dots, j_{2k}$, each with 8 values, has $8^{4k}$ terms; for all 64 components $64\cdot 8^{4k}$. That is $2.6 \times 10^5$ terms for $k = 1$, $1.1 \times 10^9$ for $k = 2$, $4.4 \times 10^{12}$ for $k = 3$ and $1.8 \times 10^{16}$ for $k = 4$ (Notebook 11b, In [5]). Each term is a product of exact polynomials, so the literal sum of order 3 is out of reach. Three exact facts make it small.

**Step 1: only nonzero curvature factors.** A term with a vanishing curvature factor vanishes. So each factor need only run through the 112 nonzero entries $R^{ab}{}_{cd}$ of Section 11.10, and a term is an ordered choice of $k$ entries: $64\cdot 112^k$ terms for all components, $7.2 \times 10^3$, $8.0 \times 10^5$, $9.0 \times 10^7$ and $1.0 \times 10^{10}$ for $k = 1$ to 4.

**Step 2: no repeated label.** If two chosen entries share an upper label, or an entry shares an upper label with the free label $j$, the delta's lower list repeats a label and the delta is 0 (case a of Section 11.3); the same for the lower labels and the free $h$ (case b). The program therefore builds the choices one entry at a time and keeps an entry only if it repeats no label already used. To test this quickly it stores a set of labels as a **bit mask**, the whole number $\sum 2^{\text{label}}$: the set $\{x_1, x_3\}$ (numbers 1 and 3) is $2^1 + 2^3 = 10$. Two sets share a label exactly when the bitwise AND of their masks is not 0 (the AND keeps a bit where both numbers have a 1, Section 1.49), and the union of two sets is their bitwise OR (a bit is 1 where at least one of the two numbers has a 1). A complete choice of $k$ entries is called a **leaf**. The counts of leaves for all 64 components are 4,032, 107,520, 645,120 and 0 for $k = 1, 2, 3, 4$ (record `Revision/gkd_lovelock/results/lovelock-report.json`, field `counters`, entry `leaves`). For $k = 4$ there is no leaf: three entries already use seven different labels in the lower list ($j$ and six more), and a fourth entry would bring two more, nine different labels out of eight.

**Step 3: equal label sets.** At a leaf the lower list holds $2k + 1$ different labels and so does the upper list. If the two sets of labels differ, some lower label is missing above and the delta is 0 (case c). Only leaves whose two masks are equal are passed to GKD, which then returns $+1$ or $-1$ (case d: both lists hold the same different labels). The numbers of GKD calls are 672, 26,880, 322,560 and 0, and every one of them gives a nonzero value (record entries `gkdCalls` and `gkdNonzero`, equal for every $k$). For the scalars $L_{(k)}$ the calls are 112, 6,720, 161,280 and, for the nonzero Euler density $L_{(4)}$, 645,120 (entry `scalarGkdCalls`). Because every entry is a plane curvature, which brings the same two labels to both lists, a leaf for a diagonal component $(h, h)$ always has equal masks; a leaf for $h \ne j$ never has, because $j$ is then in the lower list and not in the upper one (Section 11.21 (a)).

**Step 4: exact products, collected.** Every term that remains is weighted by an explicit call of GKD, multiplied out exactly and added. The program represents every quantity as an exact **Laurent polynomial** (a sum of monomials that may contain negative powers, such as $\cot^{-1}z$) in fourteen symbols: $H$, $a_4'$ to $a_4''''$, $E = e^{a_4}$, $W = (\sin^2z)^{1/12}$, $C = \cot z$, $Q = b_4^{1/2}$, $b_4'$ to $b_4''''$ and $G = \mathrm{sgn}(\cot z)$, with coefficients that are exact fractions of whole numbers (the files `poly.rs` and `rational.rs` of the crate; every operation that would overflow stops the program instead of rounding). The derivatives along $x_0$ are exact rules, $dC/dx_0 = -6H(1 + C^2)$ and $dW/dx_0 = HCW$, valid for every real $z$ with $\sin z\cos z \ne 0$. So the result is exact: no rounding happens anywhere.

**How the skipping is tested.** The steps 1 to 3 rest on the theorem of Section 11.3, and they are tested in four independent ways, none of which skips anything:

- the program itself evaluates the literal, unpruned sum over all $64\cdot 8^4 = 262144$ index lists of order 1 and all $64\cdot 8^8 = 1073741824$ index lists of order 2, with GKD weights, at one numerical point, and finds the exact tensors up to rounding errors of $7.86 \times 10^{-16}$ and $3.57 \times 10^{-13}$ (relative; checks `k1_brute_force_numeric` and `k2_brute_force_numeric` of `lovelock-report.json`; the last digits of such rounding errors differ from computer to computer);
- the Revision's sympy checker evaluates the unpruned literal sums of orders 1 and 2 with the author's determinant on every ordered product of nonzero entries (7,280 and 815,360 calls) and finds the same tensors exactly (`python-lovelock-report.json`, checks `k1_unpruned_literal_sum_agrees` and `k2_unpruned_literal_sum_agrees`);
- the Revision's Wolfram check calls the author's verbatim definition on every ordered product for $k = 1$ (7,168 calls) and $k = 2$ (802,816 calls) and on every leaf for $k = 3$ (645,120 calls), and finds the Rust tensors exactly (`wolfram-gkd-report.json`, checks `k1_P_equals_rust_all_64_components` to `k3_P_equals_rust_all_64_components`, and its field `measurements`, entry `lovelockKDeltaCalls`);
- Notebook 11b repeats the literal sums of orders 1 and 2 with its own GKD (In [16]).

Figure 11b.1 draws the four counts of each order side by side.

### 11.13 Laplace's rule and the expansion along the column of h

The classical identities of the Lovelock tensors all come from one tool: the expansion of a determinant along a row or a column. Chapter 1 used it only for $3 \times 3$ matrices; we prove it in general.

**Laplace's rule (PROVED).** For a $p \times p$ matrix $M$ and any row $r$,

$$
\det M = \sum_{c=1}^{p}(-1)^{r+c}\,M_{rc}\,\det M^{(rc)} ,
$$

where $M^{(rc)}$ is the minor (row $r$ and column $c$ removed); and the same holds along any column $c$, with the sum over $r$.

*Proof.* Every product of the Leibniz formula contains exactly one entry of row $r$. Group the products by the column $c$ of that entry:

$$
\det M = \sum_c M_{rc}\,C_{rc},\qquad C_{rc} = \sum_{\pi:\ \pi(r) = c}\mathrm{sign}(\pi)\prod_{i \ne r}M_{i\pi(i)}
$$

(the Leibniz formula, with the factor of row $r$ taken out of each product). $C_{rc}$, the **cofactor**, contains no entry of row $r$. Now let $M_\ast$ be $M$ with row $r$ replaced by the row that has 1 in column $c$ and 0 elsewhere. Its cofactors are those of $M$ (they contain no entry of row $r$), and only the column $c$ of its row $r$ is not zero, so

$$
\det M_\ast = 1\cdot C_{rc} = C_{rc}
$$

(the grouping above, applied to $M_\ast$). We compute $\det M_\ast$ a second way. Move row $r$ to the top by $r - 1$ exchanges with the row above it, and column $c$ to the left by $c - 1$ exchanges with the column before it. Each exchange flips the sign of the determinant (rule 3 of Section 1.20 for rows, and for columns rule 3 applied to the transpose, rule 2), so the new matrix $M'$ has

$$
\det M' = (-1)^{(r-1)+(c-1)}\det M_\ast = (-1)^{r+c}\det M_\ast
$$

(and $(-1)^{-2} = 1$). Its first row is $(1, 0, \dots, 0)$, and removing its first row and column leaves $M^{(rc)}$, because the other rows and columns keep their order. In the Leibniz formula of $M'$ only the permutations with $\pi(1) = 1$ have a nonzero factor in row 1. Such a $\pi$ has the smallest value 1 at the first place, so the first place forms no inversion with any later place, and its sign is the sign of its restriction to the places $2, \dots, p$, which runs through all permutations of these places. Hence $\det M' = 1\cdot\det M^{(rc)}$, and

$$
C_{rc} = \det M_\ast = (-1)^{r+c}\det M' = (-1)^{r+c}\det M^{(rc)}
$$

(the last two equations together, multiplied by $(-1)^{r+c}$, whose square is 1). Inserting this into the grouping gives the rule along row $r$. Along a column, apply the rule to the transpose (rule 2). $\square$

**The expansion of every Lovelock tensor (PROVED).** Write the delta of $P_{(k)}$ as the determinant of the $(2k + 1) \times (2k + 1)$ matrix $M$ whose rows belong to the lower labels $j, j_1, \dots, j_{2k}$ in this order and whose columns belong to the upper labels $h, h_1, \dots, h_{2k}$. Its first column holds $\delta(j, h), \delta(j_1, h), \dots, \delta(j_{2k}, h)$. Expand along this column:

$$
\delta^{h\,h_1\dots h_{2k}}_{j\,j_1\dots j_{2k}} = \delta^h_j\,\delta^{h_1\dots h_{2k}}_{j_1\dots j_{2k}} + \sum_{s=1}^{2k}(-1)^{(s+1)+1}\,\delta^h_{j_s}\,\delta^{h_1\dots h_{2k}}_{j\,j_1\dots j_{s-1}j_{s+1}\dots j_{2k}}
$$

(Laplace's rule along column 1: the entry in row 1 has the sign $(-1)^{1+1} = +1$ and the minor with the rows $j_1, \dots, j_{2k}$; the entry $\delta(j_s, h)$ stands in row $s + 1$, and its minor keeps the rows $j, j_1, \dots, j_{s-1}, j_{s+1}, \dots, j_{2k}$). In the minor, move the row of $j$ down past the $s - 1$ rows $j_1, \dots, j_{s-1}$:

$$
\delta^{h_1\dots h_{2k}}_{j\,j_1\dots j_{s-1}j_{s+1}\dots j_{2k}} = (-1)^{s-1}\,\delta^{h_1\dots h_{2k}}_{j_1\dots j_{s-1}\,j\,j_{s+1}\dots j_{2k}}
$$

($s - 1$ exchanges of neighbouring rows, each a factor $-1$ by rule 3; now $j$ stands at the place $s$, where $j_s$ stood). The two signs combine to $(-1)^{s+2}(-1)^{s-1} = (-1)^{2s+1} = -1$, so

$$
\delta^{h\,h_1\dots h_{2k}}_{j\,j_1\dots j_{2k}} = \delta^h_j\,\delta^{h_1\dots h_{2k}}_{j_1\dots j_{2k}} - \sum_{s=1}^{2k}\delta^h_{j_s}\,\delta^{h_1\dots h_{2k}}_{j_1\dots(j\text{ at place }s)\dots j_{2k}} .
$$

Multiply by the product of the curvature factors and sum over the $4k$ labels. The first term gives $\delta^h_j L_{(k)}$ (the definition of the scalar). In the term $s$, the factor $\delta^h_{j_s}$ keeps only $j_s = h$ in the sum over $j_s$, so $h$ takes the place of $j_s$ in its curvature factor:

$$
P_{(k)}{}^h{}_j = \delta^h_jL_{(k)} - \sum_{s=1}^{2k}T_s,
$$

$$
T_s = \sum\delta^{h_1\dots h_{2k}}_{j_1\dots(j\text{ at place }s)\dots j_{2k}}\;R^{j_1j_2}{}_{h_1h_2}\cdots R^{j_{2k-1}j_{2k}}{}_{h_{2k-1}h_{2k}}\quad(\text{with } h \text{ in place of } j_s) .
$$

**The $2k$ terms are equal.** (i) Let $s$ be even, the second upper place of its factor $R^{j_{s-1}h}{}_{h_{s-1}h_s}$. Exchange the rows of $j_{s-1}$ and $j$ in the delta (the places $s - 1$ and $s$), a factor $-1$ (rule 3), and write $R^{j_{s-1}h}{}_{h_{s-1}h_s} = -R^{hj_{s-1}}{}_{h_{s-1}h_s}$, another factor $-1$ (antisymmetry). The term is unchanged, and now $j$ stands at the place $s - 1$ and $h$ first in its factor: $T_s = T_{s-1}$. (ii) Let $s = 2m - 1$ be odd with $m > 1$, the first place of the $m$-th factor. Exchange the $m$-th factor with the first factor: the product of the curvature factors is unchanged (numbers commute). In the delta this exchanges the pair of rows at the places $2m - 1, 2m$ with the pair at the places 1, 2, which is two exchanges of rows, a factor $(-1)^2 = +1$, and the pair of columns $h_{2m-1}, h_{2m}$ with $h_1, h_2$, again $+1$. After renaming the summed labels the term is $T_1$. So all $2k$ terms equal $T_1$, and

$$
P_{(k)}{}^h{}_j = \delta^h_j\,L_{(k)} - 2k\,Y_{(k)}{}^h{}_j,\qquad Y_{(k)}{}^h{}_j = \sum\delta^{h_1\dots h_{2k}}_{j\,j_2\dots j_{2k}}\,R^{hj_2}{}_{h_1h_2}\,R^{j_3j_4}{}_{h_3h_4}\cdots R^{j_{2k-1}j_{2k}}{}_{h_{2k-1}h_{2k}} .
$$

Notebook 11b computes $Y_{(k)}$ with its own GKD sum and checks this expansion exactly for all 64 components and $k = 1, 2, 3$ (In [21]). The Revision's sympy checker derived the same expansion, along the row of $h$ in its convention (`Revision/gkd_lovelock/verification/check_lovelock_gkd.py`, module docstring).

### 11.14 Order 1 is Einstein's tensor; the trace identity

**The pieces of order 1 (PROVED).** For $k = 1$ the delta in $Y_{(1)}$ has two labels, and by the formula of Section 11.3

$$
Y_{(1)}{}^h{}_j = \sum_{h_1,h_2,j_2}\big(\delta^{h_1}_j\delta^{h_2}_{j_2} - \delta^{h_2}_j\delta^{h_1}_{j_2}\big)\,R^{hj_2}{}_{h_1h_2}
$$

(the $2 \times 2$ delta with the lower list $(j, j_2)$ and the upper list $(h_1, h_2)$),

$$
= \sum_{j_2}\big(R^{hj_2}{}_{jj_2} - R^{hj_2}{}_{j_2j}\big) = 2\sum_{j_2}R^{hj_2}{}_{jj_2} = 2R^h{}_j
$$

(each Kronecker delta keeps one value of a summed label; then the antisymmetry $R^{hj_2}{}_{j_2j} = -R^{hj_2}{}_{jj_2}$; then the definition of the Ricci tensor). In the same way

$$
L_{(1)} = \sum\big(\delta^{h_1}_{j_1}\delta^{h_2}_{j_2} - \delta^{h_2}_{j_1}\delta^{h_1}_{j_2}\big)R^{j_1j_2}{}_{h_1h_2} = \sum_{h_1,h_2}\big(R^{h_1h_2}{}_{h_1h_2} - R^{h_2h_1}{}_{h_1h_2}\big) = 2\sum_{h_1,h_2}R^{h_1h_2}{}_{h_1h_2} = 2R
$$

(the same steps; $\sum_{a,b}R^{ab}{}_{ab} = \sum_aR^a{}_a = R$).

**$P_{(1)} = -4G$ and $E_{(1)} = G$ (PROVED).** The expansion of Section 11.13 with $k = 1$ gives

$$
P_{(1)}{}^h{}_j = \delta^h_j\cdot 2R - 2\cdot 2R^h{}_j = -4\big(R^h{}_j - \tfrac12\delta^h_jR\big) = -4\,G^h{}_j
$$

(insert $L_{(1)} = 2R$ and $Y_{(1)} = 2R^h{}_j$; take out $-4$; the definition of $G$), and therefore $E_{(1)} = -P_{(1)}/2^2 = G$. This holds for every metric. For the author's metric the record checks it in all 64 components (`lovelock-report.json` and `python-lovelock-report.json`, check `k1_equals_minus_4_einstein`; `wolfram-gkd-report.json`, check `k1_equals_minus_4_einstein`), and so does Notebook 11b (In [18]). With the Einstein tensor of Section 11.10 the components of $P_{(1)}$ are $-4$ times those of $G$: for example, from $G^{x_1}{}_{x_1} = 2a_4'' - 5a_4'^2 + 6a_4'u + 6H^2k - \frac52u^2 - 2v$,

$$
P_{(1)}{}^{x_1}{}_{x_1} = -4G^{x_1}{}_{x_1} = 20a_4'^2 - 24a_4'u - 8a_4'' + 10u^2 + 8v - 24H^2k
$$

(each coefficient multiplied by $-4$), as the Wolfram record lists it in the variables $b_4'$ and $b_4''$ (`wolfram-gkd-report.json`, field `measurements`, entry `wolframComponents`: $-24H^2e^{2a_4}/b_4 + 20a_4'^2 - 24a_4'b_4'/b_4 + 2b_4'^2/b_4^2 - 8a_4'' + 8b_4''/b_4$, which is the same polynomial, because $b_4'/b_4 = u$ and $b_4''/b_4 = v + u^2$ give $2u^2 + 8(v + u^2) = 10u^2 + 8v$). And, with the Ricci scalar of Section 11.10, $L_{(1)} = 2R = 16a_4'^2 - 16a_4'u - 4a_4'' - 24H^2k + 10u^2 + 8v$ (record `Revision/gkd_lovelock/results/lovelock-tensors.json`, key `L1`; Notebook 11b, In [22]).

**The trace identity (PROVED).** Set $j = h$ in the expansion of Section 11.13 and sum over the eight values of $h$:

$$
\sum_hP_{(k)}{}^h{}_h = \Big(\sum_h\delta^h_h\Big)L_{(k)} - 2k\sum_hY_{(k)}{}^h{}_h = 8\,L_{(k)} - 2k\,L_{(k)} = (8 - 2k)\,L_{(k)}
$$

($\delta^h_h = 1$ for each of the eight values; in $\sum_hY_{(k)}{}^h{}_h$ the label $h$ is summed exactly like $j_1$ in the definition of the scalar, so renaming it $j_1$ gives $L_{(k)}$). The factors are 6, 4 and 2 for $k = 1, 2, 3$, the factors of Section 1.44, found there by contracting the delta directly. The record checks the identity exactly (`lovelock-report.json`, checks `k1_trace_identity` to `k3_trace_identity`; `wolfram-gkd-report.json`, checks `k1_trace_equals_6_L1`, `k2_trace_equals_4_L2`, `k3_trace_equals_2_L3`), and so does Notebook 11b (In [22]). For $k = 1$: the trace of $P_{(1)} = -4G$ is $-4(R - 4R) = 12R = 6\cdot 2R$, as it must be.

### 11.15 Order 2 is the Gauss-Bonnet tensor; order 3 is the cubic Lovelock density

**The piece $Y_{(2)}$, line by line (PROVED).** Write $X^h{}_j = Y_{(2)}{}^h{}_j = \sum\delta^{h_1h_2h_3h_4}_{j\,j_2j_3j_4}\,R^{hj_2}{}_{h_1h_2}\,R^{j_3j_4}{}_{h_3h_4}$. The delta is a $4 \times 4$ determinant with the rows $j, j_2, j_3, j_4$ and the columns $h_1, h_2, h_3, h_4$. Expand it along its first row, the row of $j$, whose entries are $\delta(j, h_c) = \delta^{h_c}_j$ with the signs $+, -, +, -$ (Laplace's rule, $(-1)^{1+c}$). This gives four terms; in each, the factor $\delta^{h_c}_j$ puts $j$ in place of $h_c$ in the curvature factors. We use the result of order 1 in the form

$$
\sum\delta^{a\,c_1c_2}_{b\,d_1d_2}R^{d_1d_2}{}_{c_1c_2} = P_{(1)}{}^a{}_b = 2R\,\delta^a_b - 4R^a{}_b
$$

(Section 11.14, with the labels renamed), and write the summed labels as $b = j_2$, $c = j_3$, $d = j_4$.

Term 1 ($c = 1$, sign $+$): the minor has the rows $j_2, j_3, j_4$ and the columns $h_2, h_3, h_4$:

$$
\sum R^{hj_2}{}_{jh_2}\,\delta^{h_2h_3h_4}_{j_2j_3j_4}R^{j_3j_4}{}_{h_3h_4} = \sum_{j_2,h_2}R^{hj_2}{}_{jh_2}\big(2R\,\delta^{h_2}_{j_2} - 4R^{h_2}{}_{j_2}\big) = 2R\,R^h{}_j - 4\sum_{b,x}R^{hb}{}_{jx}R^x{}_b
$$

(the order-1 result with $a = h_2$, $b = j_2$; then $\delta^{h_2}_{j_2}$ sets $h_2 = j_2$ and $\sum_{j_2}R^{hj_2}{}_{jj_2} = R^h{}_j$; the summed labels renamed $b = j_2$, $x = h_2$).

Term 2 ($c = 2$, sign $-$): the minor has the columns $h_1, h_3, h_4$, and $h_2$ becomes $j$:

$$
-\sum R^{hj_2}{}_{h_1j}\big(2R\,\delta^{h_1}_{j_2} - 4R^{h_1}{}_{j_2}\big) = -2R\sum_{j_2}R^{hj_2}{}_{j_2j} + 4\sum R^{hj_2}{}_{h_1j}R^{h_1}{}_{j_2} = 2R\,R^h{}_j - 4\sum_{b,x}R^{hb}{}_{jx}R^x{}_b
$$

(the same steps; then $R^{hj_2}{}_{j_2j} = -R^{hj_2}{}_{jj_2}$ and $R^{hj_2}{}_{h_1j} = -R^{hj_2}{}_{jh_1}$ by antisymmetry). Terms 1 and 2 together: $4R\,R^h{}_j - 8\sum R^{hb}{}_{jx}R^x{}_b$.

Term 3 ($c = 3$, sign $+$): $h_3$ becomes $j$, and the minor $\delta^{h_1h_2h_4}_{j_2j_3j_4}$ has the rows $j_2, j_3, j_4$ and the columns $h_1, h_2, h_4$. Expand it along its third column, the column of $h_4$, with the signs $+, -, +$:

$$
\delta^{h_1h_2h_4}_{j_2j_3j_4} = \delta^{h_4}_{j_2}\,\delta^{h_1h_2}_{j_3j_4} - \delta^{h_4}_{j_3}\,\delta^{h_1h_2}_{j_2j_4} + \delta^{h_4}_{j_4}\,\delta^{h_1h_2}_{j_2j_3}
$$

(Laplace's rule along column 3; the sign of row $r$ is $(-1)^{r+3}$). Multiply by $R^{hj_2}{}_{h_1h_2}R^{j_3j_4}{}_{jh_4}$ and sum, using $\sum_{h_1,h_2}\delta^{h_1h_2}_{uv}R^{hj_2}{}_{h_1h_2} = R^{hj_2}{}_{uv} - R^{hj_2}{}_{vu} = 2R^{hj_2}{}_{uv}$:

$$
2\sum R^{hj_2}{}_{j_3j_4}R^{j_3j_4}{}_{jj_2} - 2\sum R^{hj_2}{}_{j_2j_4}R^{j_3j_4}{}_{jj_3} + 2\sum R^{hj_2}{}_{j_2j_3}R^{j_3j_4}{}_{jj_4}
$$

(each $\delta^{h_4}$ puts the matching lower label in place of $h_4$). In the second sum $\sum_{j_2}R^{hj_2}{}_{j_2j_4} = -R^h{}_{j_4}$ and $\sum_{j_3}R^{j_3j_4}{}_{jj_3} = -R^{j_4}{}_j$; in the third $\sum_{j_2}R^{hj_2}{}_{j_2j_3} = -R^h{}_{j_3}$ and $\sum_{j_4}R^{j_3j_4}{}_{jj_4} = R^{j_3}{}_j$ (antisymmetry, then the definition of the Ricci tensor). So term 3 is

$$
2\sum R^{hb}{}_{cd}R^{cd}{}_{jb} - 2\sum_cR^h{}_cR^c{}_j - 2\sum_cR^h{}_cR^c{}_j = 2\sum R^{hb}{}_{cd}R^{cd}{}_{jb} - 4\sum_cR^h{}_cR^c{}_j .
$$

Term 4 ($c = 4$, sign $-$): $h_4$ becomes $j$, the factor is $R^{j_3j_4}{}_{h_3j} = -R^{j_3j_4}{}_{jh_3}$, and the two minus signs give $+\sum\delta^{h_1h_2h_3}_{j_2j_3j_4}R^{hj_2}{}_{h_1h_2}R^{j_3j_4}{}_{jh_3}$, which is term 3 with $h_4$ renamed $h_3$. So term 4 equals term 3. Adding the four terms:

$$
X^h{}_j = 4R\,R^h{}_j - 8\sum R^{hb}{}_{jx}R^x{}_b - 8\sum_cR^h{}_cR^c{}_j + 4\sum R^{hb}{}_{cd}R^{cd}{}_{jb} .
$$

**$L_{(2)}$ is four times the Gauss-Bonnet scalar (PROVED).** By the trace argument of Section 11.14, $L_{(2)} = \sum_hX^h{}_h$:

$$
\begin{aligned}
L_{(2)} &= 4R^2 - 8\sum R^b{}_xR^x{}_b - 8\sum R^h{}_cR^c{}_h + 4\sum R^{ab}{}_{cd}R^{cd}{}_{ab}\\
&= 4\Big(R^2 - 4\sum_{a,b}R^a{}_bR^b{}_a + \sum R^{ab}{}_{cd}R^{cd}{}_{ab}\Big) = 4\,\mathrm{GB}
\end{aligned}
$$

($\sum_hR^{hb}{}_{hx} = R^b{}_x$; the two Ricci squares are the same sum; then 4 taken out). $\mathrm{GB} = R^2 - 4R^a{}_bR^b{}_a + R^{ab}{}_{cd}R^{cd}{}_{ab}$ is the classical **Gauss-Bonnet scalar**.

**$P_{(2)}$ is $-8$ times the Gauss-Bonnet tensor (PROVED).** The expansion of Section 11.13 with $k = 2$:

$$
P_{(2)}{}^h{}_j = \delta^h_j\,4\,\mathrm{GB} - 4X^h{}_j = -16R\,R^h{}_j + 32\sum R^{hb}{}_{jx}R^x{}_b + 32\sum_cR^h{}_cR^c{}_j - 16\sum R^{hb}{}_{cd}R^{cd}{}_{jb} + 4\,\delta^h_j\,\mathrm{GB}
$$

(insert $L_{(2)}$ and $X$; multiply out). The classical Gauss-Bonnet tensor of Lanczos, which uses no generalized delta, is (in the mixed form of the record)

$$
2\mathcal{H}^h{}_j = 4\Big(R\,R^h{}_j - 2\sum_aR^h{}_aR^a{}_j - 2\sum_{a,b}R^{ha}{}_{jb}R^b{}_a + \sum_{a,b,c}R^{ha}{}_{bc}R^{bc}{}_{ja}\Big) - \delta^h_j\,\mathrm{GB} .
$$

Multiplying by $-4$ gives $-8\mathcal{H}^h{}_j = -16R\,R^h{}_j + 32\sum R^h{}_aR^a{}_j + 32\sum R^{ha}{}_{jb}R^b{}_a - 16\sum R^{ha}{}_{bc}R^{bc}{}_{ja} + 4\delta^h_j\,\mathrm{GB}$, which is $P_{(2)}{}^h{}_j$ term by term after renaming the summed labels ($b \to a$, $x \to b$ in the second term; $b \to a$, $c \to b$, $d \to c$ in the fourth). So $P_{(2)} = -8\mathcal{H}$ and $E_{(2)} = -P_{(2)}/8 = \mathcal{H}$ for every metric: the second Lovelock tensor is the Gauss-Bonnet tensor. For the author's metric the record checks it in all 64 components (`python-lovelock-report.json`, checks `k2_equals_minus_8_gauss_bonnet` and `L2_equals_4_gauss_bonnet`), and so does Notebook 11b (In [19]). The record also found the factors $-4$ and $-8$ without any algebra, from literal sums on random curvature tensors in four and five dimensions (checks `normalisation_P1_derived_minus_4` and `normalisation_P2_derived_minus_8`). For the corrected metric $L_{(2)}$ is a polynomial of 16 terms in the six variables (record key `L2`; Notebook 11b, In [22], prints it); on the history of the record it is $L_{(2)} = \frac{32}{27}(81k^2 - 702k - 58)H^4$ (Section 11.23), so there the Gauss-Bonnet scalar is $\mathrm{GB} = L_{(2)}/4 = \frac{8}{27}(81k^2 - 702k - 58)H^4$.

**Order 3 (PROVED for the author's metric by exact computation; the general formula quoted).** The third scalar is the **cubic Lovelock density**,

$$
L_{(3)} = 8\big(2T_1 + 8T_2 + 24T_3 + 3T_4 + 24T_5 + 16T_6 - 12T_7 + T_8\big),
$$

with the eight cubic invariants $T_1 = R^{ab}{}_{cd}R^{cd}{}_{ef}R^{ef}{}_{ab}$, $T_2 = R^{ab}{}_{cd}R^{ce}{}_{bf}R^{df}{}_{ae}$, $T_3 = R^{ab}{}_{cd}R^{cd}{}_{be}R^e{}_a$, $T_4 = R\,R^{ab}{}_{cd}R^{cd}{}_{ab}$, $T_5 = R^{ab}{}_{cd}R^c{}_aR^d{}_b$, $T_6 = R^a{}_bR^b{}_cR^c{}_a$, $T_7 = R\,R^a{}_bR^b{}_a$, $T_8 = R^3$ (every label summed). We do not derive these coefficients by hand: the record determined them from literal sums on nine random curvature tensors in six dimensions (a system of nine equations for eight unknowns with a unique solution; `python-lovelock-report.json`, check `normalisation_L3_cubic_derived`), and checked the identity exactly for the author's metric (check `L3_equals_8_cubic_lovelock_density`); Notebook 11b checks it again (In [20]). For the corrected metric $L_{(3)}$ is a polynomial of 20 terms (record key `L3`; Notebook 11b, In [22]); on the history of the record it is $L_{(3)} = \frac{256}{9}(243k^2 + 99k + 22)H^6$ (Section 11.23).

### 11.16 Example: the three Lovelock tensors computed twice

Notebook 11b computes the three Lovelock tensors of the corrected metric in two independent ways and checks Sections 11.10 to 11.15. It builds and runs the Revision Rust program `lovelock_gkd`, which computes everything exactly from the metric alone (the corrected metric of 2026-10-16, for general functions $a_4(x_4)$ and $b_4(x_4)$), runs its 27 checks and writes four files; the notebook compares three of the four files with the committed Revision records byte for byte, and the fourth, the report `lovelock-report.json`, apart from its two floating-point numbers (the rounding errors measured by its two brute-force checks, whose last digits may depend on the computer). Then it recomputes the Christoffel symbols and the Riemann tensor with sympy and compares all 112 nonzero components exactly with the record; draws the plane curvatures, the whole Riemann tensor, and the two factors of every possible mixed component, one of which always vanishes; recomputes the three tensors and scalars with its own Python GKD sum and its own exact arithmetic, reproduces every counter of the Rust sums and all $3 \times 64$ components; repeats the sums of orders 1 and 2 literally; checks the expansion of Section 11.13, the identities $P_{(1)} = -4G$, $P_{(2)} = -8\mathcal{H}$, the cubic density, the trace identities and $P_{(4)} = 0$; draws the components of $E_{(1)}, E_{(2)}, E_{(3)}$ at the moment $x_4 = 0$ of the history of the record; and checks that every check it quotes from the records is there. It needs Rust and takes about two minutes (110 seconds, including the start of the kernel, when it was built on 2026-10-18; provenance file `Revision/textbook/notebooks/11b_lovelock_tensors.PROVENANCE.md`). It prints 38 PASS lines, draws five figures and ends with the line ALL 38 CHECKS PASSED (notebook 11b).

<!-- NOTEBOOK 11b -->

### 11.19 Line-by-line walk-through of Notebook 11b

The notebook has 25 code cells, In [1] to In [25]. As in Section 11.9, every line or small group of lines is quoted and explained; docstrings are left out where the explanation repeats them, and long captions are shortened to `...` (they are printed in full under the figures in Section 11.18).

**In [1], the set-up cell.** It is word for word the set-up cell of Notebook 11a, explained line by line in Section 11.9 under In [1], with two differences: its comment lines are the run instructions of Notebook 11b (Section 11.17), and its line `NOTEBOOK_ID = "11b"  # this notebook: chapter 11, example b` names this notebook, so the figures are saved as `11b_<k>_<name>.png` and their captions in `11b.captions.json`. It contains the helper `rust_program`. It prints Set-up of notebook 11b complete: repository folder found, helpers defined.

**In [2], the Rust program is built.**

```python
program = rust_program("Revision/gkd_lovelock/code/Cargo.toml", "lovelock_gkd")
```

The same line as the first line of In [13] of Notebook 11a: cargo builds the crate (or confirms in about a second that it is up to date), and `program` is the path of `lovelock_gkd`. Output: Rust program lovelock_gkd is built and ready.

**In [3], the program computes everything.** The command it runs is

```text
lovelock_gkd lovelock --output FOLDER --brute-force-k2
```

with the option that adds the literal unpruned sum of order 2 at a numerical point (Section 11.12).

```python
import re  # regular expressions: patterns that read parts of a line of text

RESULTS = "Revision/gkd_lovelock/results"  # the folder of the Revision records
OUT_FOLDER = REPO / "Revision" / "gkd_lovelock" / "code" / "target" / "textbook_11b"
completed = subprocess.run(
    [str(program), "lovelock", "--output", str(OUT_FOLDER), "--brute-force-k2"],
    capture_output=True, text=True, encoding="utf-8", errors="replace")
```

The module `re` reads parts of the printed lines. `RESULTS` is the folder of the Revision records, and `OUT_FOLDER` a folder inside the crate's build folder `target`, which git ignores, so the run adds nothing to the repository. `subprocess.run` starts the program and collects what it prints (Section 11.9, In [1]). The program computes, exactly and from the corrected metric alone, the Christoffel symbols, the Riemann tensor and the Lovelock tensors of orders 1 to 4 for general functions $a_4$ and $b_4$, runs its 27 checks and writes four files; the record's run took 13.3 seconds (`Revision/docs/LOVELOCK_GKD.md`, section 10), most of it in the literal sum of order 2.

```python
rust_checks = []  # (name, verdict) of every check the program printed
for line in completed.stdout.splitlines():
    found = re.match(r"(PASS|FAIL) - (\w+): ", line)
    if found:
        rust_checks.append((found.group(2), found.group(1)))
    if line.startswith("info - L_(4)"):
        l4_text = line.split("): ", 1)[1]  # the formula after the explanation
```

Each printed line is examined. `re.match` tests whether the line BEGINS with the pattern: PASS or FAIL (`(PASS|FAIL)` means one or the other), a dash, and a name made of letters, digits and underscores (`\w+`), followed by a colon. `found.group(2)` is the name and `found.group(1)` the verdict; the pair is stored. The program also prints an information line with the scalar $L_{(4)}$; `line.split("): ", 1)` cuts that line once at the first `): ` and `[1]` keeps the part after it, the formula.

```python
say("The checks of the Rust program (name, verdict):")
for number, (name, verdict) in enumerate(rust_checks, 1):
    say(f"  {number:2d} {name:34s} {verdict}")
```

The 27 checks are printed as a numbered table (the format `:34s` pads a text to 34 places). They are: the antisymmetry and the first Bianchi identity of the Riemann tensor (1 and 2); the freedom of every $R^{ab}{}_{cd}$ from $x_0$ (3); the absence of mixed components, every nonzero $R^{ab}{}_{cd}$ being a plane curvature (4); the positivity of $\sqrt{|\det g|}$ in each quarter of the period of $z$ (5); the identity $P_{(1)} = -4G$ (6); for each order $k = 1, 2, 3$ the trace identity, zero divergence, the symmetry, the freedom from $x_0$, the vanishing off-diagonal components and the equality of the hidden and the extra-time components (7 to 24); the vanishing of $P_{(4)}$ (25); and the two brute-force sums (26 and 27). All 27 print PASS.

```python
l4_terms = len(re.split(r" [+-] ", l4_text))  # the terms, separated by + and -
report("terms of the eighth-order scalar L(4) printed by the program", l4_terms)
```

`re.split(r" [+-] ", l4_text)` cuts the formula at every plus or minus sign that stands between two blanks, that is between two terms (a minus sign at the very beginning has no blank before it and does not cut), and `len` counts the pieces. RESULT: 25 terms, the polynomial $L_{(4)}$ of Section 11.11, which In [22] prints in full.

```python
check(completed.returncode == 0 and "lovelock: SUCCESS" in completed.stdout,
      "the Rust program lovelock_gkd lovelock ended with SUCCESS")
check(len(rust_checks) == 27 and all(v == "PASS" for _, v in rust_checks),
      "all 27 checks of the Rust program passed",
      record=f"{RESULTS}/lovelock-report.json, checkCount 27, failedCheckCount 0")
```

Two checks: the program ended with the return code 0 and the verdict SUCCESS, and it printed exactly 27 checks, all PASS, as the record states. PASS lines one and two.

**In [4], the four files against the records.**

```python
DEVIATION = re.compile(r"(max relative deviation from the exact P_\(\d\) = )"
                       r"([0-9.]+e[-+]?\d+)")  # the two floating-point numbers
```

`re.compile` prepares a pattern for repeated use. It finds the text "max relative deviation from the exact P_(1) = " (or P_(2); `\d` is one digit, `\(` and `\)` literal parentheses) as the first group, and the decimal number that follows as the second group: digits and points, the letter e, an optional sign and digits, for example `7.86e-16`.

```python
for file_name in ("curvature.json", "lovelock-tensors.json",
                  "lovelock-components.md"):
    written = (OUT_FOLDER / file_name).read_bytes()
    stored = repository_file(f"{RESULTS}/{file_name}").read_bytes()
    report(f"size of {file_name}", len(written), "bytes")
    check(written == stored,
          f"the program wrote {file_name} equal to the Revision record byte for byte",
          record=f"{RESULTS}/{file_name} (the whole file)")
```

The three files that hold only exact numbers are compared with the committed records byte for byte, and their sizes are printed: 39,730, 164,399 and 56,688 bytes. PASS lines three to five.

```python
written = (OUT_FOLDER / "lovelock-report.json").read_text(encoding="utf-8")
stored = repository_file(f"{RESULTS}/lovelock-report.json").read_text(
    encoding="utf-8")
deviations = [float(number) for _, number in DEVIATION.findall(written)]
masked_written = DEVIATION.sub(r"\1X", written)  # the two numbers replaced by X
masked_stored = DEVIATION.sub(r"\1X", stored)
```

The report holds two decimal numbers, the rounding errors of the two brute-force checks, which are computed in floating-point arithmetic, so that their last digits depend on the computer and its mathematics library. `DEVIATION.findall(written)` finds both, and `float` turns the second group of each into a decimal number. `DEVIATION.sub(r"\1X", ...)` replaces every match by its first group followed by the letter X, so the two numbers disappear from both texts.

```python
report("size of lovelock-report.json", len(written.encode("utf-8")), "bytes")
check(masked_written == masked_stored and len(deviations) == 2
      and all(value < 1e-10 for value in deviations),
      "the program wrote lovelock-report.json equal to the Revision record byte for "
      "byte, apart from its two brute-force deviations, both below 1e-10",
      record=f"{RESULTS}/lovelock-report.json (the whole file; checks "
             "k1_brute_force_numeric and k2_brute_force_numeric)")
```

The size is printed (5,005 bytes). The check requires the masked texts to be equal, exactly two deviations, and both below the program's own limit $10^{-10}$. Sixth PASS line.

**In [5], the work of the sums (Figure 11b.1).**

```python
import numpy as np  # arrays of numbers

lovelock_report = json.loads((OUT_FOLDER / "lovelock-report.json").read_text(
    encoding="utf-8"))
COUNTERS = {row["k"]: row for row in lovelock_report["counters"]}
```

The report just compared is read as JSON; its field `counters` is a list of four rows, one per order, and the dictionary comprehension stores each row under its order $k$.

```python
say("order k   literal lists   ordered products    leaves   GKD calls   nonzero GKD")
for k in (1, 2, 3, 4):
    leaves, calls = COUNTERS[k]["leaves"], COUNTERS[k]["gkdCalls"]
    nonzero = COUNTERS[k]["gkdNonzero"]
    say(f"      {k}   {64 * 8 ** (4 * k):13.2e}   {64 * 112 ** k:16.2e}   "
        f"{leaves:7d}   {calls:9d}   {nonzero:11d}")
```

A table of Section 11.12: for each order the literal number $64\cdot 8^{4k}$ of index lists, the number $64\cdot 112^k$ of ordered products of nonzero entries, and the record's leaves, GKD calls and nonzero GKD values. The output shows $2.62 \times 10^5$, $1.07 \times 10^9$, $4.40 \times 10^{12}$, $1.80 \times 10^{16}$ index lists, $7.17 \times 10^3$, $8.03 \times 10^5$, $8.99 \times 10^7$, $1.01 \times 10^{10}$ ordered products, 4032, 107520, 645120, 0 leaves and 672, 26880, 322560, 0 calls, each call nonzero.

```python
fig, ax = plt.subplots(figsize=(7.6, 4.5))
orders = np.array([1, 2, 3, 4])
series = [("literal index lists, $64 \\cdot 8^{4k}$", [64 * 8 ** (4 * k)
                                                      for k in orders], "0.7"),
          ("ordered products of nonzero entries, $64 \\cdot 112^k$",
           [64 * 112 ** k for k in orders], "tab:purple"),
          ("leaves after skipping repeated labels",
           [COUNTERS[k]["leaves"] for k in orders], "tab:blue"),
          ("GKD calls", [COUNTERS[k]["gkdCalls"] for k in orders], "tab:orange")]
```

The four series of bars, each a name for the legend, four heights and a colour.

```python
width = 0.2
for number, (name, heights, colour) in enumerate(series):
    place = orders + (number - 1.5) * width
    ax.bar(place, [h if h > 0 else np.nan for h in heights], width, color=colour,
           label=name)
    for x, h in zip(place, heights):
        if h == 0:
            ax.text(x, 1.5, "0", ha="center", fontsize=8)
```

Each series is shifted sideways by its own amount (adding a number to the numpy array `orders` adds it to every entry). A height 0 is drawn as `np.nan` ("not a number", which matplotlib leaves out), because 0 has no place on a logarithmic axis, and a small "0" is written instead.

```python
ax.set_yscale("log")
ax.set_ylim(1.0, 1e18)
ax.set_xlim(0.5, 4.5)
ax.set_xticks(orders, [f"k = {k}" for k in orders])
ax.set_xlabel("order $k$ of the Lovelock tensor")
ax.set_ylabel("number of terms (logarithmic scale)")
ax.set_title("The work of the Lovelock sums, and how it is reduced")
ax.legend(loc="upper left", fontsize=8)
save_figure(fig, "work_of_the_sums",
            "The number of terms of the Lovelock sums for the 64 components of "
            ...)
```

A logarithmic vertical axis from 1 to $10^{18}$, the marks, titles, legend, and the saved figure.

```python
check([COUNTERS[k]["leaves"] for k in (1, 2, 3, 4)] == [4032, 107520, 645120, 0]
      and [COUNTERS[k]["gkdCalls"] for k in (1, 2, 3, 4)] == [672, 26880, 322560, 0],
      "the counters of the Rust sums are 4032, 107520, 645120, 0 leaves and 672, "
      "26880, 322560, 0 GKD calls",
      record=f"{RESULTS}/lovelock-report.json, counters")
```

The check fixes the counters quoted in the text. Seventh PASS line.

*What Figure 11b.1 shows.* For each order four bars on a logarithmic axis: grey (all literal index lists), purple (ordered products of nonzero curvature entries), blue (leaves without a repeated label) and orange (GKD calls). For $k = 3$ the grey bar reaches $4.4 \times 10^{12}$ while the orange one stays at 322,560, about one term in fourteen million. For $k = 4$ the blue and orange bars are missing (marked 0): no leaf exists, because nine labels out of eight must repeat.

**In [6], the metric and its Christoffel symbols with sympy.**

```python
import sympy as sp  # exact algebra and calculus

NAMES = ["x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7"]  # label k is xk
```

sympy is loaded, and the eight names of the coordinates are listed in the author's order; the label $k$ of a program is $x_k$.

```python
H = sp.Symbol("H", positive=True)  # the author's constant H > 0
X = sp.symbols("x0:8", real=True)  # the coordinates x0, ..., x7
a4 = sp.Function("a4")(X[4])  # the unknown function a4(x4)
b4 = sp.Function("b4")(X[4])  # the unknown function b4(x4) > 0
C = sp.Function("C")(X[0])  # C = cot z with z = 6 H x0
W = sp.Function("W")(X[0])  # W = (sin^2 z)^(1/12) > 0
RULES = {sp.Derivative(C, X[0]): -6 * H * (1 + C ** 2),  # d cot z / d x0
         sp.Derivative(W, X[0]): H * C * W}  # d (sin^2 z)^(1/12) / d x0
```

`H` is a positive symbol, `X` the eight coordinates ($x_0$ to $x_7$, all real), and `a4`, `b4` are unknown functions of the time $x_4$. The functions of $x_0$ are not written with `sp.cot` and powers of `sp.sin`: sympy would then have to decide signs and roots of $\sin^2z$ for a real $z$ and would produce absolute values and case distinctions. Instead `C` and `W` are unknown functions of $x_0$, standing for $\cot z$ and $(\sin^2z)^{1/12}$, and `RULES` holds their exact derivatives, by the chain rule with $dz/dx_0 = 6H$:

$$
\begin{aligned}
\frac{d\cot z}{dx_0} &= -\frac{6H}{\sin^2z} = -6H\,(1 + \cot^2z),\\
\frac{d(\sin^2z)^{1/12}}{dx_0} &= \tfrac1{12}(\sin^2z)^{-11/12}\cdot 2\sin z\cos z\cdot 6H = H\cot z\,(\sin^2z)^{1/12}
\end{aligned}
$$

($1/\sin^2z = 1 + \cot^2z$; and $2\cdot 6/12 = 1$, $\cos z/\sin z = \cot z$). These rules hold for every real $z$ with $\sin z\cos z \ne 0$, the rules of the Rust program (Section 11.12).

```python
block = sp.exp(-2 * a4) * b4  # the factor of g_00 and of the three extra times
METRIC = ([block * C ** 2] + [sp.exp(2 * a4)] * 3 + [sp.Integer(-1)]
          + [-block * W ** 2] * 3)  # g_00, g_11, ..., g_77
```

The corrected metric of Section 11.2: `block` is the common factor $e^{-2a_4}b_4$ of the hidden direction and the extra times, so $g_{00} = e^{-2a_4}b_4C^2$, $g_{11} = g_{22} = g_{33} = e^{2a_4}$, $g_{44} = -1$ and $g_{55} = g_{66} = g_{77} = -e^{-2a_4}b_4W^2$, with $W^2 = (\sin^2z)^{1/6}$. A list multiplied by 3 repeats its entry three times.

```python
A1, A2, U, V = sp.symbols("A1 A2 U V")  # a4', a4'', u = b4'/b4, v = u'
K, B = sp.symbols("K B", positive=True)  # k = e^(2 a4)/b4 and b4 itself
SYMBOLS = {sp.Derivative(a4, (X[4], 2)): A2, sp.Derivative(a4, X[4]): A1,
           sp.Derivative(b4, (X[4], 2)): (V + U ** 2) * B,
           sp.Derivative(b4, X[4]): U * B}
PLAIN = {C: sp.Symbol("C"), W: sp.Symbol("W")}  # C(x0), W(x0) printed as C, W
```

The six variables of Section 11.2 as plain symbols: `A1` $= a_4'$, `A2` $= a_4''$, `U` $= u$, `V` $= v$, `K` $= k$ (positive), and `B` for $b_4$ itself. `SYMBOLS` replaces the derivatives: $b_4' = u\,b_4$ and $b_4'' = (v + u^2)\,b_4$ (the derivative of $b_4' = ub_4$ is $u'b_4 + ub_4' = vb_4 + u^2b_4$). `PLAIN` prints `C(x0)` and `W(x0)` as `C` and `W`.

```python
def readable(expr):
    expr = expr.subs(SYMBOLS).subs(b4, B).subs(a4, sp.log(K * B) / 2)
    return sp.factor(sp.cancel(expr)).subs(PLAIN)
```

`readable` (docstring left out) writes an expression in the six variables: the derivatives become symbols, $b_4$ becomes `B`, and $a_4$ is replaced by $\frac12\ln(KB)$, which is the definition $k = e^{2a_4}/b_4$ solved for $a_4$; then `sp.cancel` and `sp.factor` simplify the fraction.

```python
christoffel = {}  # (a, b, c) -> Gamma^a_bc, only the nonzero ones
for a in range(8):
    for b in range(8):
        for c in range(8):
            value = 0
            if a == c:
                value += sp.diff(METRIC[a], X[b])  # d_b g_ac
            if a == b:
                value += sp.diff(METRIC[a], X[c])  # d_c g_ab
            if b == c:
                value -= sp.diff(METRIC[b], X[a])  # - d_a g_bc
            if value != 0:  # times g^aa / 2, the derivatives of C and W replaced
                christoffel[a, b, c] = sp.cancel((value / (2 * METRIC[a]))
                                                 .subs(RULES))
```

The Christoffel formula of Section 11.10 for a diagonal metric. For the three labels $a, b, c$ the three terms of $\frac12g^{aa}(\partial_bg_{ac} + \partial_cg_{ab} - \partial_ag_{bc})$ survive only when two labels agree: $g_{ac}$ is $g_{aa}$ when $c = a$ (first `if`), $g_{ab}$ is $g_{aa}$ when $b = a$ (second), and $g_{bc}$ is $g_{bb}$ when $c = b$ (third). A nonzero sum is divided by $2g_{aa}$, the derivatives of $C$ and $W$ are replaced by the rules, and `sp.cancel` writes the result as one simplified fraction.

```python
def gamma(a, b, c):
    return christoffel.get((a, b, c), 0)
```

`gamma(a, b, c)` returns $\Gamma^a{}_{bc}$, or 0 when the symbol is not in the dictionary (docstring left out).

```python
christoffel_b_le_c = sorted(key for key in christoffel if key[1] <= key[2])
report("nonzero Christoffel symbols Gamma^a_bc with b <= c", len(christoffel_b_le_c))
for a, b, c in christoffel_b_le_c:
    say(f"  Gamma^{NAMES[a]}_({NAMES[b]} {NAMES[c]}) = "
        f"{readable(christoffel[a, b, c])}")
```

The symbols with $b \le c$ (the others follow from the symmetry), sorted by their labels, are counted and printed in readable form. RESULT: 21, and the 21 lines are the list of Section 11.10, for example `Gamma^x0_(x0 x4) = -(2*A1 - U)/2`, which is $\frac12u - a_4'$, and `Gamma^x4_(x1 x1) = A1*B*K`, which is $a_4'\,b_4k = a_4'e^{2a_4}$.

```python
check(all(christoffel.get((a, c, b)) == value
          for (a, b, c), value in christoffel.items()),
      "Gamma^a_bc = Gamma^a_cb (symmetric in the lower labels)")
```

The check confirms $\Gamma^a{}_{bc} = \Gamma^a{}_{cb}$ for every symbol. Eighth PASS line.

**In [7], the Riemann tensor with sympy.**

```python
RIEMANN = {}  # (a, b, c, d) -> R^ab_cd in the symbols H, A1, A2, U, V, K
for a in range(8):
    for b in range(8):
        for c in range(8):
            for d in range(8):
                value = sp.diff(gamma(a, d, b), X[c]) - sp.diff(gamma(a, c, b), X[d])
                for e in range(8):
                    value += (gamma(a, c, e) * gamma(e, d, b)
                              - gamma(a, d, e) * gamma(e, c, b))
                if value == 0:
                    continue
                value = (value / METRIC[b]).subs(RULES).subs(SYMBOLS).subs(b4, B)
                value = sp.cancel(value.subs(a4, sp.log(K * B) / 2))  # e^(2a4) = K B
                if value != 0:
                    RIEMANN[a, b, c, d] = sp.expand(value)
```

For every list of four labels the formula of Section 11.10, $R^a{}_{bcd} = \partial_c\Gamma^a{}_{db} - \partial_d\Gamma^a{}_{cb} + \sum_e(\Gamma^a{}_{ce}\Gamma^e{}_{db} - \Gamma^a{}_{de}\Gamma^e{}_{cb})$, is evaluated; a zero is skipped at once (`continue`). Dividing by `METRIC[b]` raises the second label ($R^{ab}{}_{cd} = g^{bb}R^a{}_{bcd}$). Then the derivatives of $C$ and $W$, of $a_4$ and of $b_4$ are replaced, $b_4$ becomes `B`, and $a_4 = \frac12\ln(KB)$ turns every $e^{2a_4}$ into $KB$; `sp.cancel` simplifies, and the nonzero results are stored expanded. This takes a few seconds.

```python
report("nonzero components R^ab_cd", len(RIEMANN))
VARIABLES = (H, A1, A2, U, V, K)  # the six variables
check(all(v.free_symbols <= set(VARIABLES) and v.is_polynomial(*VARIABLES)
          for v in RIEMANN.values()),
      "every R^ab_cd is a polynomial in H, a4', a4'', u, v and k: free of x0 (of C and "
      "W) and of b4 and e^a4 except through u, v and k",
      record=f"{RESULTS}/lovelock-report.json, check mixed_riemann_free_of_x0")
```

RESULT: 112 nonzero components. The check requires every component to contain only the six variables and to be a polynomial in them: no $C$ and no $W$ (so no $x_0$), no $B$ (so $b_4$ enters only through $u$, $v$ and $k$), and no division by any variable. Ninth PASS line.

**In [8], sympy against the Rust record.**

```python
curvature = json.loads((OUT_FOLDER / "curvature.json").read_text(encoding="utf-8"))
```

The file `curvature.json` that the program wrote in In [3] (equal to the record, In [4]) is read.

```python
def from_mathematica(text):
    text = re.sub(r"Derivative\[(\d)\]\[a4\]\[x4\]", r"A\1", text)  # a4' -> A1
    text = text.replace("Derivative[1][b4][x4]", "(U*B)")  # b4' = u b4
    text = text.replace("Derivative[2][b4][x4]", "((V + U**2)*B)")  # b4''
    text = text.replace("b4[x4]", "B")  # b4
    text = re.sub(r"E\^\((-?\d+)\*a4\[x4\]\)", r"(K*B)**(\1/2)", text)  # e^(n a4)
    value = sp.sympify(text.replace("^", "**"),
                       locals={"H": H, "A1": A1, "A2": A2, "U": U, "V": V, "K": K,
                               "B": B})
    return sp.expand(value)
```

`from_mathematica` (docstring left out) reads a formula of the record, which is written in Mathematica's notation. `re.sub` turns `Derivative[1][a4][x4]` into `A1` and `Derivative[2][a4][x4]` into `A2` (`\1` repeats the digit found by `(\d)`); the derivatives of $b_4$ become $ub_4$ and $(v + u^2)b_4$; `b4[x4]` becomes `B`; and a power `E^(n*a4[x4])` becomes $(KB)^{n/2}$, which is $e^{na_4}$ by the definition of $k$. `sp.sympify` reads the text as a sympy expression with the given symbols, after `^` has been replaced by Python's power `**`.

```python
rust_riemann = {}
for item in curvature["riemannMixedNonzero"]:
    a, b = (NAMES.index(name) for name in item["up"])
    c, d = (NAMES.index(name) for name in item["down"])
    rust_riemann[a, b, c, d] = from_mathematica(item["value"])
same_values = set(rust_riemann) == set(RIEMANN) and all(
    sp.expand(RIEMANN[key] - rust_riemann[key]) == 0 for key in RIEMANN)
check(same_values, "sympy and Rust give the same 112 nonzero R^ab_cd exactly",
      record="Revision/gkd_lovelock/results/python-lovelock-report.json, "
             "check rust_riemann_agrees")
```

The record lists every nonzero $R^{ab}{}_{cd}$ with its upper pair `up`, its lower pair `down` and its value; `NAMES.index` turns a name into its label. The check requires the record and sympy to have the same 112 keys and equal values. Tenth PASS line.

```python
antisymmetric = all(sp.expand(v + RIEMANN.get((b, a, c, d), 0)) == 0 and
                    sp.expand(v + RIEMANN.get((a, b, d, c), 0)) == 0
                    for (a, b, c, d), v in RIEMANN.items())
check(antisymmetric, "R^ab_cd = -R^ba_cd = -R^ab_dc for all components",
      record=f"{RESULTS}/lovelock-report.json, check riemann_antisymmetry")
```

The antisymmetry $R^{ab}{}_{cd} = -R^{ba}{}_{cd} = -R^{ab}{}_{dc}$, tested for every component. Eleventh PASS line.

```python
sectional = all({c, d} == {a, b} for (a, b, c, d) in RIEMANN)
check(sectional and len(RIEMANN) == 4 * 28,
      "every nonzero R^ab_cd has {c, d} = {a, b}: 4 entries for each of the 28 "
      "planes, no mixed component",
      record=f"{RESULTS}/lovelock-report.json, check mixed_riemann_only_sectional")
```

Every nonzero component has the same SET of labels below as above (`{c, d} == {a, b}`): it is a plane curvature $R^{ab}{}_{ab}$ or its mirror $R^{ab}{}_{ba}$, and there are $4\cdot 28 = 112$ of them, four for each of the 28 planes. Twelfth PASS line: no mixed component (Section 11.10).

```python
check(len(christoffel_b_le_c) == len(curvature["christoffelNonzero_b_le_c"]) == 21,
      "21 nonzero Christoffel symbols with b <= c, as in the record")
```

The record also lists 21 nonzero Christoffel symbols with $b \le c$. Thirteenth PASS line.

```python
ricci_scalar = sp.expand(sum(RIEMANN.get((a, b, a, b), 0) for a in range(8)
                             for b in range(8)))
report("Ricci scalar R", ricci_scalar)
check(sp.expand(ricci_scalar - from_mathematica(curvature["ricciScalar"])) == 0,
      "the Ricci scalar is R = 8 a4'^2 - 8 a4' u - 2 a4'' - 12 H^2 k + 5 u^2 + 4 v, "
      "as in the record",
      record=f"{RESULTS}/curvature.json, ricciScalar")
```

The Ricci scalar $R = \sum_{a,b}R^{ab}{}_{ab}$, printed as RESULT `8*A1**2 - 8*A1*U - 2*A2 - 12*H**2*K + 5*U**2 + 4*V` and compared with the record's `ricciScalar`. Fourteenth PASS line.

**In [9], the plane curvatures (Figure 11b.2).**

```python
MOMENT = {H: 1, A1: 1, A2: 0, U: sp.Rational(4, 3), V: 0, K: 1}  # record, x4 = 0
SPED_UP = {**MOMENT, A2: 1, V: 1}  # the same moment with a4'' = v = H^2
```

Two moments: `MOMENT` is $x_4 = 0$ on the history of the record ($H = 1$, $a_4' = 1$, $a_4'' = 0$, $u = \frac43$, $v = 0$, $k = 1$), and `SPED_UP` is the same moment with $a_4'' = v = 1$; `{**MOMENT, ...}` copies the dictionary and changes two entries.

```python
fig, axes = plt.subplots(1, 2, figsize=(11.6, 5.0))
planes = {}
for ax, (name, point) in zip(axes, (("moment", MOMENT), ("sped up", SPED_UP))):
    table = [[sp.sympify(RIEMANN.get((a, b, a, b), 0)).subs(point) for b in range(8)]
             for a in range(8)]  # exact fractions
    planes[name] = table
    picture = ax.imshow(np.array([[float(x) for x in row] for row in table]),
                        cmap="RdBu_r", vmin=-2.2, vmax=2.2)
    for a in range(8):
        for b in range(8):
            if a != b:
                ax.text(b, a, str(table[a][b]), ha="center", va="center",
                        fontsize=7)
    ax.set_xticks(range(8), NAMES)
    ax.set_yticks(range(8), NAMES)
    ax.grid(False)
```

Two panels. For each moment the $8 \times 8$ table of the plane curvatures $K(a, b) = R^{ab}{}_{ab}$ is computed as exact fractions (`.subs(point)` inserts the numbers; a missing component is 0), drawn with the colour map `RdBu_r` (blue negative, red positive) and written into the squares off the diagonal as fractions such as `-1/3`.

```python
axes[0].set_title("history of the record at $x_4 = 0$")
axes[1].set_title("the same moment with $a_4'' = v = H^2$")
fig.colorbar(picture, ax=list(axes), shrink=0.8, label="$K(a, b)$ in units of $H^2$")
save_figure(fig, "curvature_of_planes",
            "The curvature $K(a, b) = R^{ab}_{\\ ab}$ of the plane of the coordinate "
            ...)
```

The titles, one colour bar for both panels, and the saved figure.

```python
check(planes["moment"][1][2] == 1 and planes["moment"][1][5] == sp.Rational(-1, 3)
      and planes["moment"][1][0] == sp.Rational(-1, 3)
      and planes["moment"][0][5] == sp.Rational(-8, 9)
      and planes["moment"][4][0] == sp.Rational(1, 9) == planes["moment"][4][5]
      and planes["moment"][1][4] == 1 and planes["sped up"][1][4] == 2
      and planes["sped up"][5][4] == sp.Rational(-7, 18) == planes["sped up"][0][4],
      "plane curvatures: 3-space 1, 3-space with the block -1/3, block -8/9, x4 with "
      "3-space 1 + a4'', x4 with the block 1/9 - a4'' + v/2")
```

The check reads six planes of the table: $K(x_1, x_2) = 1$, $K(x_1, x_5) = K(x_1, x_0) = -\frac13$, $K(x_0, x_5) = -\frac89$, $K(x_4, x_0) = K(x_4, x_5) = \frac19$, $K(x_1, x_4) = 1$ at the moment and 2 when sped up ($a_4'^2 + a_4''$), and $K(x_5, x_4) = K(x_0, x_4) = \frac19 - 1 + \frac12 = -\frac7{18}$ when sped up ($(a_4' - \frac12u)^2 - a_4'' + \frac12v$). These are the values of the table of Section 11.10. Fifteenth PASS line.

*What Figure 11b.2 shows.* Two $8 \times 8$ tables of fractions in units of $H^2$. On the left the block of 3-space ($x_1, x_2, x_3$) is red with the value 1, also with the time $x_4$; every plane of 3-space with $x_0$ or an extra time is light blue, $-\frac13$; the planes inside the block of $x_0, x_5, x_6, x_7$ are darker blue, $-\frac89$; and the planes of the time with the block are pale red, $\frac19$. The row and the column of $x_0$ are exactly those of $x_5$, $x_6$ and $x_7$: the hidden direction behaves like an extra time. On the right only the row and the column of $x_4$ change: 2 with 3-space and $-\frac7{18}$ with the block.

**In [10], the whole Riemann tensor (Figure 11b.3).**

```python
whole = np.zeros((64, 64))
for (a, b, c, d), value in RIEMANN.items():
    whole[8 * a + b, 8 * c + d] = float(value.subs(SPED_UP))
```

A $64 \times 64$ table of zeros; every component $R^{ab}{}_{cd}$ is entered at the row $8a + b$ and the column $8c + d$, as a decimal number at the sped-up moment.

```python
fig, ax = plt.subplots(figsize=(6.8, 6.2))
largest = np.abs(whole).max()
picture = ax.imshow(whole, cmap="RdBu_r", vmin=-largest, vmax=largest)
for edge in range(8, 64, 8):  # lines between the blocks
    ax.axhline(edge - 0.5, color="0.8", lw=0.5)
    ax.axvline(edge - 0.5, color="0.8", lw=0.5)
ticks = list(range(3, 64, 8))  # the middle of each block
ax.set_xticks(ticks, [f"c = {name}" for name in NAMES], rotation=90, fontsize=8)
ax.set_yticks(ticks, [f"a = {name}" for name in NAMES], fontsize=8)
ax.set_xlabel("lower pair $(x_c, x_d)$, column $8c + d$")
ax.set_ylabel("upper pair $(x_a, x_b)$, row $8a + b$")
ax.set_title("All components $R^{ab}{}_{cd}$ at one moment")
ax.grid(False)
fig.colorbar(picture, ax=ax, shrink=0.8, label="value (units of $H^2$)")
```

The table is drawn on a colour scale symmetric about zero, with thin grey lines between the blocks of eight rows and columns and one mark in the middle of each block.

```python
save_figure(fig, "riemann_matrix",
            "All 4096 components of the Riemann tensor $R^{ab}_{\\ \\ cd}$ of the "
            ...)
```

The saved figure.

```python
places = {(8 * a + b, 8 * c + d) for (a, b, c, d) in RIEMANN}
check(int(np.count_nonzero(whole)) == 112
      and all(column in (8 * (row // 8) + row % 8, 8 * (row % 8) + row // 8)
              for row, column in places),
      "112 of the 4096 components are not zero, all at the places of R^ab_ab and "
      "R^ab_ba")
```

`places` collects the row and the column of every nonzero component. The check requires 112 nonzero entries, each in the column $8a + b$ (the place of $R^{ab}{}_{ab}$, on the main diagonal) or $8b + a$ (the place of $R^{ab}{}_{ba}$); `row // 8` and `row % 8` recover $a$ and $b$ from the row number. Sixteenth PASS line.

*What Figure 11b.3 shows.* A $64 \times 64$ picture, almost all grey-white. The main diagonal carries the plane curvatures (red for the planes of 3-space and of 3-space with the time, blue for the block); every other coloured square is the mirror $R^{ab}{}_{ba} = -K(a, b)$ of a diagonal one and has the opposite colour. No coloured square lies anywhere else: no component connects two different planes.

**In [11], why nothing mixes the time and the hidden direction (Figure 11b.4).**

```python
def rate(c, coordinate):
    value = (sp.diff(METRIC[c], X[coordinate]) / (2 * METRIC[c])).subs(RULES)
    return sp.cancel(value.subs(SYMBOLS).subs(b4, B))
```

`rate(c, coordinate)` is $\partial\ln f_c = \partial g_{cc}/(2g_{cc})$ along the given coordinate, the rate of Section 11.10 (docstring left out), with the derivatives of $C$, $W$, $a_4$ and $b_4$ replaced.

```python
transverse = [1, 2, 3, 5, 6, 7]  # the directions of 3-space and the extra times
along_x0 = {c: rate(c, 0) for c in transverse}  # first factor
relative = {c: sp.cancel(rate(c, 4) - rate(0, 4)) for c in transverse}  # second
for c in transverse:
    say(f"c = {NAMES[c]}: d0 ln f_c = {along_x0[c].subs(PLAIN)}, "
        f"d4 ln f_c - d4 ln f_0 = {relative[c]}, product = "
        f"{sp.cancel(along_x0[c] * relative[c])}")
```

For each of the six directions of 3-space and of the extra times the two factors of the formula $R^{x_4c}{}_{x_0c} = \partial_0\ln f_c\,(\partial_4\ln f_c - \partial_4\ln f_0)$ of Section 11.10 are computed and printed with their product. The output: for $c = x_1, x_2, x_3$ the first factor is 0 and the second `2*A1 - U/2` ($a_4' - (\frac12u - a_4')$); for $c = x_5, x_6, x_7$ the first factor is `C*H` ($H\cot z$) and the second 0; every product is 0.

```python
fig, ax = plt.subplots(figsize=(7.6, 4.2))
places_c = np.arange(len(transverse))
first = [float(along_x0[c].subs(H, 1).subs(C, 1)) for c in transverse]
second = [float(relative[c].subs(MOMENT)) for c in transverse]
ax.bar(places_c - 0.18, first, 0.36, color="tab:blue",
       label="$\\partial_0 \\ln f_c$ (units of $H \\cot z$)")
ax.bar(places_c + 0.18, second, 0.36, color="tab:orange",
       label="$\\partial_4 \\ln f_c - \\partial_4 \\ln f_0$ (units of $H$)")
for place in places_c:
    ax.text(place, 1.45, "product 0", ha="center", fontsize=8)
ax.axhline(0.0, color="black", lw=0.8)
ax.set_ylim(-0.2, 2.15)
ax.set_xticks(places_c, [NAMES[c] for c in transverse])
ax.set_xlabel("the direction $c$ of the term $R^{x_4 c}{}_{x_0 c}$")
ax.set_ylabel("value")
ax.set_title("The two factors of each mixed term: one of them is always 0")
ax.legend(loc="upper center", ncol=2, fontsize=8)
save_figure(fig, "mixing_terms_vanish",
            "Why the corrected metric has no curvature component that mixes the "
            ...)
```

The two factors as bars side by side, the first at $H = 1$, $C = 1$ (so in units of $H\cot z$), the second at the moment of the record; above every pair the note "product 0".

```python
check(all(sp.cancel(along_x0[c] * relative[c]) == 0 for c in transverse)
      and not any((4, c, 0, c) in RIEMANN or (0, c, 4, c) in RIEMANN
                  for c in transverse),
      "every term R^(x4 c)_(x0 c) has a vanishing factor, and none is among the 112 "
      "components")
```

The check requires every product to vanish identically and none of the components $R^{x_4c}{}_{x_0c}$ and $R^{x_0c}{}_{x_4c}$ to be among the 112. Seventeenth PASS line.

```python
ricci_40 = sp.expand(sum(RIEMANN.get((4, c, 0, c), 0) for c in range(8)))
check(ricci_40 == 0 and curvature["einsteinMixed"]["x4,x0"]["mathematica"] == "0"
      and curvature["einsteinMixed"]["x0,x4"]["mathematica"] == "0",
      "R^x4_x0 = 0, and the record's G^x4_x0 and G^x0_x4 are 0",
      record=f"{RESULTS}/curvature.json, einsteinMixed x4,x0 and x0,x4")
```

The Ricci component $R^{x_4}{}_{x_0} = \sum_cR^{x_4c}{}_{x_0c}$ is 0, and the record's Einstein components $G^{x_4}{}_{x_0}$ and $G^{x_0}{}_{x_4}$ are written as `"0"`. Eighteenth PASS line.

*What Figure 11b.4 shows.* Six pairs of bars. For $x_1, x_2, x_3$ only the orange bar stands ($\frac43$, the difference of the rates of 3-space and of the block at the moment of the record), for $x_5, x_6, x_7$ only the blue one (1, in units of $H\cot z$). In no pair do both bars stand, so every product vanishes.

**In [12], exact polynomial arithmetic and GKD.**

```python
from fractions import Fraction  # exact fractions of whole numbers

ONE = {(0, 0, 0, 0, 0, 0): Fraction(1)}  # the polynomial 1
```

From here on the notebook computes with its own exact polynomials, independent of sympy's: a polynomial in the six variables is a dictionary from the six exponents $(e_H, e_{a_4'}, e_{a_4''}, e_u, e_v, e_k)$ of each monomial to its coefficient, a `Fraction` (an exact fraction of whole numbers). `ONE` is the polynomial 1.

```python
def poly_mul(p, q):
    out = {}
    for m1, c1 in p.items():
        for m2, c2 in q.items():
            m = tuple(e1 + e2 for e1, e2 in zip(m1, m2))  # add the exponents
            out[m] = out.get(m, 0) + c1 * c2
    return {m: c for m, c in out.items() if c != 0}
```

The product of two polynomials (docstring left out): every monomial of the first times every monomial of the second, which adds the exponents (`zip` pairs the six exponents of the two monomials, and `tuple` collects their sums) and multiplies the coefficients; equal monomials are collected, and monomials whose coefficient became 0 are dropped.

```python
def poly_add(p, q, factor=1):
    out = dict(p)
    for m, c in q.items():
        out[m] = out.get(m, 0) + factor * c
    return {m: c for m, c in out.items() if c != 0}
```

`poly_add(p, q, factor)` is $p + \text{factor}\cdot q$: a copy of `p` (`dict(p)`), to which each monomial of `q` times the factor is added; zeros are dropped.

```python
def to_poly(expr):
    poly = sp.Poly(sp.expand(expr), *VARIABLES)
    return {m: Fraction(int(v.p), int(v.q))
            for m, v in zip(poly.monoms(), poly.coeffs())}
```

`to_poly` turns a sympy polynomial into this form: `sp.Poly` lists the exponents of its monomials (`poly.monoms()`) and their coefficients (`poly.coeffs()`), and each sympy fraction `v` becomes a `Fraction` of its numerator `v.p` and denominator `v.q`.

```python
def gkd(lower, upper):
    position = {}
    for place, label in enumerate(upper):
        if label in position:
            return 0
        position[label] = place
    sigma = [position.get(label) for label in lower]
    if None in sigma or len(set(sigma)) < len(sigma):
        return 0
    inversions = sum(1 for i in range(len(sigma)) for j in range(i + 1, len(sigma))
                     if sigma[i] > sigma[j])
    return 1 if inversions % 2 == 0 else -1
```

The rule GKD of Notebook 11a (In [4]), written more compactly: `position.get(label)` gives `None` for a lower label that is missing above, and the test `None in sigma` then returns 0 (case c); a repeated place returns 0 (case a); otherwise the sign of the inversions.

```python
ENTRIES = [(key, to_poly(RIEMANN[key])) for key in sorted(RIEMANN)]  # 112 entries
LOWER_MASK = np.array([(1 << a) | (1 << b) for (a, b, c, d), _ in ENTRIES])
UPPER_MASK = np.array([(1 << c) | (1 << d) for (a, b, c, d), _ in ENTRIES])
```

The 112 nonzero entries, sorted by their labels, each with its polynomial. For each entry $R^{ab}{}_{cd}$ the bit masks of Section 11.12 are stored: its upper labels $a, b$ go into the delta's LOWER list and its lower labels $c, d$ into the delta's UPPER list. The operator written with two less-than signs shifts the number 1 to the left by the given number of places, so it is $2^a$; the vertical bar is the bitwise OR, so the mask of $\{a, b\}$ is $2^a + 2^b$. `np.array` holds the 112 masks, so that one comparison can test all of them at once.

```python
report("nonzero curvature entries in the sums", len(ENTRIES))
check(gkd([0, 1, 2], [1, 2, 0]) == 1 and gkd([0, 1], [1, 0]) == -1,
      "gkd: a cycle of three labels is even (+1), an exchange of two odd (-1)",
      record=f"{RESULTS}/lovelock-report.json, gkdSelfCheck")
```

RESULT: 112 entries. The check repeats the two values that the Rust program records for itself in the field `gkdSelfCheck` of its report: $+1$ for the cycle $(0, 1, 2) \to (1, 2, 0)$ and $-1$ for one exchange. Nineteenth PASS line.

**In [13], the Lovelock sum.** This cell only defines a function; it prints nothing.

```python
def lovelock_sum(k, free_pair):
    pairs = [(h, j) for h in range(8) for j in range(8)] if free_pair else [None]
    weights, leaves, calls = {}, 0, 0
```

`lovelock_sum(k, free_pair)` computes $P_{(k)}$ for all 64 pairs $(h, j)$ when `free_pair` is true, and $L_{(k)}$ (one sum, marked `None`) otherwise. `weights` collects, per pair, the summed GKD weight of each set of entries; `leaves` and `calls` count.

```python
    for pair in pairs:
        start_lower = 1 << pair[1] if pair else 0  # j is the first lower label
        start_upper = 1 << pair[0] if pair else 0  # h is the first upper label
        stack = [((), start_lower, start_upper)]
```

For a tensor component the delta's lower list starts with $j$ and its upper list with $h$, so the masks start with these labels; for the scalar they start empty. The **stack** is a list of partial combinations still to be extended, each a tuple of the chosen entry numbers with the two masks; it starts with the empty combination.

```python
        while stack:
            chosen, lower_mask, upper_mask = stack.pop()
            if len(chosen) == k:  # a leaf
                leaves += 1
                if lower_mask != upper_mask:
                    continue  # a lower label is missing above: GKD = 0
```

`while stack:` repeats as long as the stack is not empty; `stack.pop()` takes the last partial combination off it. A combination of $k$ entries is a leaf and is counted. If its two masks differ, some lower label is missing above, GKD would be 0 (case c), and the leaf is dropped (step 3 of Section 11.12).

```python
                lower = ([pair[1]] if pair else []) + [
                    x for i in chosen for x in ENTRIES[i][0][:2]]  # j, j1, ..., j2k
                upper = ([pair[0]] if pair else []) + [
                    x for i in chosen for x in ENTRIES[i][0][2:]]  # h, h1, ..., h2k
                sign = gkd(lower, upper)
                calls += 1
```

The two lists of the delta: $j$ followed by the upper labels of the chosen entries in order (`ENTRIES[i][0][:2]` is the pair $a, b$ of entry `i`), and $h$ followed by their lower labels (`[2:]` is $c, d$). GKD is called, and the call is counted.

```python
                if sign != 0:
                    bucket = weights.setdefault(pair, {})
                    key = tuple(sorted(chosen))  # the set of entries
                    bucket[key] = bucket.get(key, 0) + sign
                continue
```

A nonzero value is added to the weight of the SET of chosen entries (`sorted` makes the key independent of the order), because the product of the entries does not depend on their order. `continue` goes back to the top of the `while` loop.

```python
            free = np.nonzero(((LOWER_MASK & lower_mask) == 0)
                              & ((UPPER_MASK & upper_mask) == 0))[0]
            for i in free:  # every entry that repeats no label
                stack.append((chosen + (int(i),), lower_mask | int(LOWER_MASK[i]),
                              upper_mask | int(UPPER_MASK[i])))
```

A combination with fewer than $k$ entries is extended (step 2 of Section 11.12). `LOWER_MASK & lower_mask` is computed for all 112 entries at once; `== 0` marks the entries that share no label with the lower list so far, and the same for the upper list; `&` between the two true/false arrays keeps the entries that pass both tests, and `np.nonzero(...)[0]` lists their numbers. Each such entry is appended to the combination, and the masks grow by its labels (bitwise OR).

```python
    products = {}  # set of entries -> the product of their polynomials
    result = {}
    for pair, bucket in weights.items():
        total = {}
        for key, weight in bucket.items():
            if weight == 0:
                continue
            if key not in products:
                product = ONE
                for i in key:
                    product = poly_mul(product, ENTRIES[i][1])
                products[key] = product
            total = poly_add(total, products[key], weight)
        if total:
            result[pair] = total
    return result, leaves, calls
```

After the search, every set of entries with a nonzero total weight is multiplied out once (and remembered in `products`, because the same set appears for many pairs), multiplied by its weight and added to the component (step 4). Components that are not zero are returned in `result`, together with the two counters.

**In [14], the sums of orders 1 to 3.**

```python
P, L, MY_COUNTERS = {}, {}, {}
for k in (1, 2, 3):
    P[k], leaves, calls = lovelock_sum(k, free_pair=True)
    scalar, scalar_leaves, scalar_calls = lovelock_sum(k, free_pair=False)
    L[k] = scalar.get(None, {})
    MY_COUNTERS[k] = (leaves, calls, scalar_calls)
    say(f"k = {k}: leaves {leaves:7d}, GKD calls {calls:6d}, scalar GKD calls "
        f"{scalar_calls:6d}, nonzero components {len(P[k])}")
```

For each order the tensor and the scalar are computed (this takes most of the notebook's running time, mostly for $k = 3$), and the counters are stored and printed: 4032, 107520, 645120 leaves; 672, 26880, 322560 GKD calls; 112, 6720, 161280 scalar calls; and 8 nonzero components for every order.

```python
same_counters = all(
    MY_COUNTERS[k] == (COUNTERS[k]["leaves"], COUNTERS[k]["gkdCalls"],
                       COUNTERS[k]["scalarGkdCalls"])
    and COUNTERS[k]["gkdNonzero"] == COUNTERS[k]["gkdCalls"]
    and len(P[k]) == COUNTERS[k]["nonzeroComponents"] == 8
    for k in (1, 2, 3))
check(same_counters, "the Python sums reproduce the counters of the Rust sums; "
      "8 nonzero components for each order",
      record=f"{RESULTS}/lovelock-report.json, counters k = 1, 2, 3")
```

The Python search, written independently, finds exactly the counters of the Rust search; every GKD call of the record is nonzero; and both find 8 nonzero components for every order. Twentieth PASS line.

**In [15], every component against the record.**

```python
tensors = json.loads((OUT_FOLDER / "lovelock-tensors.json").read_text(
    encoding="utf-8"))
U2_PLUS_V = {(0, 0, 0, 2, 0, 0): Fraction(1), (0, 0, 0, 0, 1, 0): Fraction(1)}
```

The program's file of the Lovelock tensors is read. `U2_PLUS_V` is the polynomial $u^2 + v$, which is $b_4''/b_4$.

```python
def from_monomials(monomials):
    out = {}
    for numerator, denominator, e in monomials:
        if any(e[i] for i in (3, 4, 6, 7, 11, 12, 13)):
            raise ValueError("unexpected symbol in a Lovelock component")
        if e[5] % 2 or e[5] + e[8] + 2 * e[9] + 2 * e[10] != 0:
            raise ValueError("the powers of b4 do not cancel")
        term = {(e[0], e[1], e[2], e[9], 0, e[5] // 2): Fraction(numerator,
                                                                 denominator)}
        for _ in range(e[10]):  # b4''/b4 = v + u^2, once for each power of b4''
            term = poly_mul(term, U2_PLUS_V)
        out = poly_add(out, term)
    return out
```

The file lists every component as exact monomials, each a numerator, a denominator and the fourteen exponents of the symbols of Section 11.12 (in the order $H$, $a_4'$, $a_4''$, $a_4'''$, $a_4''''$, $E = e^{a_4}$, $W$, $C$, $Q = b_4^{1/2}$, $b_4'$, $b_4''$, $b_4'''$, $b_4''''$, $G$). `from_monomials` (docstring left out) rebuilds a component in the six variables. It stops if a monomial contains a third or fourth derivative, $W$, $C$ or $G$ (the exponents 3, 4, 6, 7, 11, 12, 13), and if the powers of $b_4$ do not cancel: with $E^{e_5} = k^{e_5/2}b_4^{e_5/2}$, $Q^{e_8} = b_4^{e_8/2}$, $b_4' = ub_4$ and $b_4'' = (v + u^2)b_4$, the total power of $b_4$ is $\frac12(e_5 + e_8 + 2e_9 + 2e_{10})$, which must be 0, and $e_5$ must be even. Each monomial then becomes $H^{e_0}a_4'^{e_1}a_4''^{e_2}u^{e_9}k^{e_5/2}$ times $(u^2 + v)^{e_{10}}$, and the monomials are added.

```python
agree = all(from_monomials(tensors[f"P{k}_mixed_up_h_down_j"]
                           [f"{NAMES[h]},{NAMES[j]}"]["monomials"])
            == P[k].get((h, j), {})
            for k in (1, 2, 3) for h in range(8) for j in range(8))
for k in (1, 2, 3):
    nonzero = " ".join(sorted(f"{NAMES[h]},{NAMES[j]}" for h, j in P[k]))
    say(f"k = {k}: nonzero components (h, j): {nonzero}")
```

All $3 \times 64$ components of the record, stored under keys such as `"x1,x1"`, are compared exactly with the Python components (a missing Python component is the empty polynomial, zero). The nonzero components are printed: for every order only the eight diagonal ones, $x_0x_0$ to $x_7x_7$.

```python
check(agree,
      "all 3 x 64 components of P(1), P(2), P(3) equal the Rust components exactly",
      record="Revision/gkd_lovelock/results/python-lovelock-report.json, checks "
             "rust_k1_mixed_components_agree, rust_k2_mixed_components_agree and "
             "rust_k3_mixed_components_agree")
scalars_agree = all(to_poly(from_mathematica(tensors[f"L{k}"])) == L[k]
                    for k in (1, 2, 3))
check(scalars_agree, "the scalars L(1), L(2), L(3) equal the Rust scalars exactly",
      record="Revision/gkd_lovelock/results/python-lovelock-report.json, checks "
             "rust_L1_agrees, rust_L2_agrees and rust_L3_agrees")
```

Two checks: all $3 \times 64$ components agree exactly, and the three scalars of the record (in Mathematica text, read with `from_mathematica`) equal the Python scalars. PASS lines twenty-one and twenty-two.

```python
check(all(set(P[k]) == {(h, h) for h in range(8)}
          and P[k][1, 1] == P[k][2, 2] == P[k][3, 3]
          and P[k][0, 0] == P[k][5, 5] == P[k][6, 6] == P[k][7, 7]
          for k in (1, 2, 3)),
      "only the 8 diagonal components are nonzero, with x1 = x2 = x3 and "
      "x0 = x5 = x6 = x7, for k = 1, 2, 3",
      record=f"{RESULTS}/lovelock-report.json, checks k1_offdiagonal_vanishes to "
             "k3_offdiagonal_vanishes, k1_hidden_equals_extra_times to "
             "k3_hidden_equals_extra_times")
```

For every order the nonzero components are exactly the eight diagonal ones (a set comprehension in braces), the three space components are equal, and the hidden component equals the three extra-time components. Twenty-third PASS line. In particular no Lovelock tensor has an $x_4$-$x_0$ component, for any history (Section 11.21 (a)).

**In [16], the literal sums of orders 1 and 2.**

```python
import itertools  # all ordered lists of k entries
def literal_sum(k):
    pairs = [None] + [(h, j) for h in range(8) for j in range(8)]
    weights, calls = {}, 0
    for chosen in itertools.product(range(len(ENTRIES)), repeat=k):
        lower = [x for i in chosen for x in ENTRIES[i][0][:2]]  # j1, ..., j2k
        upper = [x for i in chosen for x in ENTRIES[i][0][2:]]  # h1, ..., h2k
        key = tuple(sorted(chosen))  # the set of entries of this product
```

`literal_sum` (docstring left out) does NOT skip anything: `itertools.product(range(112), repeat=k)` runs through all $112^k$ ordered lists of $k$ entries, and for each the two lists of the delta are built.

```python
        for pair in pairs:
            if pair is None:  # the scalar: no free pair
                sign = gkd(lower, upper)
            else:  # the tensor: j first in the lower list, h first in the upper
                sign = gkd([pair[1]] + lower, [pair[0]] + upper)
            calls += 1
            if sign != 0:
                bucket = weights.setdefault(pair, {})
                bucket[key] = bucket.get(key, 0) + sign
```

For the scalar and for each of the 64 pairs, GKD is called on the complete lists, with no test before the call: $65\cdot 112^k$ calls. Nonzero values are added to the weights as before.

```python
    result = {}
    for pair, bucket in weights.items():
        total = {}
        for key, weight in bucket.items():
            product = ONE
            for i in key:
                product = poly_mul(product, ENTRIES[i][1])
            total = poly_add(total, product, weight)
        if total:
            result[pair] = total
    return result, calls
```

The weighted products are multiplied out and added, as in In [13], and the components are returned with the number of calls.

```python
record_checks = {c["name"]: c for c in json.loads(repository_file(
    "Revision/gkd_lovelock/results/python-lovelock-report.json").read_text(
        encoding="utf-8"))["checks"]}
```

The checks of the Revision's sympy report are read into a dictionary by name.

```python
for k in (1, 2):
    literal, calls = literal_sum(k)
    recorded = record_checks[f"k{k}_unpruned_literal_sum_agrees"]
    recorded_calls = int(re.search(r"(\d+) kdelta calls", recorded["detail"]).group(1))
    say(f"k = {k}: {calls} GKD calls (the record: {recorded_calls})")
```

For $k = 1$ and 2 the literal sum is computed, and the number of calls stated in the record's check text (the digits before "kdelta calls") is read. Output: 7280 and 815360 calls, both equal to the record.

```python
    same = (literal.pop(None, {}) == L[k]
            and all(literal.get(hj, {}) == P[k].get(hj, {})
                    for hj in set(literal) | set(P[k])))
    check(same and calls == recorded_calls == 65 * 112 ** k
          and recorded["verdict"] == "PASS",
          f"the literal sum of order {k}, without skipping, gives the same P({k}) "
          f"and L({k})",
          record="Revision/gkd_lovelock/results/python-lovelock-report.json, check "
                 f"k{k}_unpruned_literal_sum_agrees")
```

`literal.pop(None, {})` takes the scalar out of the result; it must equal $L_{(k)}$, and every component, over the union (`|`) of the components of both results, must equal $P_{(k)}$. The check also requires the number of calls to be $65\cdot 112^k$ and the record's verdict PASS. PASS lines twenty-four and twenty-five: the skipping changes nothing.

**In [17], order 4 has no term.**

```python
seven_labels = True
for h in range(8):
    for j in range(8):
        stack = [((), 1 << j, 1 << h)]
        while stack:
            chosen, lower_mask, upper_mask = stack.pop()
            if len(chosen) == 3:  # a leaf of order 3
                seven_labels = seven_labels and bin(lower_mask).count("1") == 7
                continue
```

The search of In [13] is repeated for order 3 without calling GKD. At every leaf `bin(mask)` writes the mask in binary and `.count("1")` counts its ones, the number of labels in the lower list; it must be 7 ($j$ and the six upper labels of three entries).

```python
            free = np.nonzero(((LOWER_MASK & lower_mask) == 0)
                              & ((UPPER_MASK & upper_mask) == 0))[0]
            for i in free:
                stack.append((chosen + (int(i),), lower_mask | int(LOWER_MASK[i]),
                              upper_mask | int(UPPER_MASK[i])))
check(seven_labels and COUNTERS[4]["leaves"] == 0,
      "every leaf of order 3 uses 7 labels, so P(4) has no term: P(4) = 0",
      record=f"{RESULTS}/lovelock-report.json, check k4_tensor_vanishes")
```

The extension step as before. Since every leaf of order 3 already uses seven different lower labels, a fourth entry would need nine different labels out of eight; together with the record's counter of 0 leaves for $k = 4$ the check confirms $P_{(4)} = 0$. Twenty-sixth PASS line.

**In [18], order 1 is Einstein's tensor.**

```python
RM = dict(ENTRIES)  # (a, b, c, d) -> R^ab_cd as a polynomial dict
def poly_sum(polynomials):
    total = {}
    for p in polynomials:
        total = poly_add(total, p)
    return total
```

`RM` is the dictionary of the 112 entries; `poly_sum` adds a list of polynomials (docstring left out).

```python
def constant(n):
    return {(0, 0, 0, 0, 0, 0): Fraction(n)}
```

`constant(n)` is the polynomial with the single number $n$ (docstring left out).

```python
RIC = {(h, j): poly_sum(RM.get((h, a, j, a), {}) for a in range(8))
       for h in range(8) for j in range(8)}  # R^h_j
R_SCALAR = poly_sum(RIC[h, h] for h in range(8))  # R
delta = {(h, j): (ONE if h == j else {}) for h in range(8) for j in range(8)}
EINSTEIN = {hj: poly_add(RIC[hj], poly_mul(delta[hj], R_SCALAR), Fraction(-1, 2))
            for hj in RIC}  # G = Ric - R/2
```

The Ricci tensor $R^h{}_j = \sum_aR^{ha}{}_{ja}$ for all 64 pairs, the Ricci scalar, the Kronecker delta as polynomials (1 or empty), and the Einstein tensor $G = \mathrm{Ric} - \frac12\delta R$, all with the exact arithmetic of In [12].

```python
check(all(P[1].get(hj, {}) == poly_mul(constant(-4), EINSTEIN[hj])
          for hj in EINSTEIN) and L[1] == poly_add({}, R_SCALAR, 2),
      "P(1) = -4 G for all 64 components and L(1) = 2 R",
      record="Revision/gkd_lovelock/results/python-lovelock-report.json, checks "
             "k1_equals_minus_4_einstein and L1_equals_2R")
```

The check of Section 11.14: every component of $P_{(1)}$ equals $-4$ times the Einstein component, and $L_{(1)} = 2R$. Twenty-seventh PASS line.

**In [19], order 2 is the Gauss-Bonnet tensor.**

```python
ric_square = poly_sum(poly_mul(RIC[a, b], RIC[b, a]) for a in range(8)
                      for b in range(8))  # R^a_b R^b_a
riem_square = poly_sum(poly_mul(v, RM[(c, d, a, b)]) for (a, b, c, d), v in
                       RM.items() if (c, d, a, b) in RM)  # R^ab_cd R^cd_ab
GB = poly_add(poly_add(poly_mul(R_SCALAR, R_SCALAR), ric_square, -4), riem_square)
```

The two squares $\sum R^a{}_bR^b{}_a$ and $\sum R^{ab}{}_{cd}R^{cd}{}_{ab}$ (only entries whose partner with the pairs exchanged is nonzero contribute), and the Gauss-Bonnet scalar $\mathrm{GB} = R^2 - 4R^a{}_bR^b{}_a + R^{ab}{}_{cd}R^{cd}{}_{ab}$ of Section 11.15.

```python
two_h = {}  # 2 H^h_j
for h in range(8):
    for j in range(8):
        t = poly_mul(R_SCALAR, RIC[h, j])
        t = poly_add(t, poly_sum(poly_mul(RIC[h, a], RIC[a, j]) for a in range(8)),
                     -2)
        t = poly_add(t, poly_sum(poly_mul(RM.get((h, a, j, b), {}), RIC[b, a])
                                 for a in range(8) for b in range(8)), -2)
        t = poly_add(t, poly_sum(poly_mul(v, RM.get((b, c, j, a), {}))
                                 for (hh, a, b, c), v in RM.items() if hh == h))
        two_h[h, j] = poly_add(poly_mul(constant(4), t), poly_mul(delta[h, j], GB),
                               -1)
```

For each pair $(h, j)$ the four sums of Lanczos's tensor (Section 11.15) are collected in `t`: $R\,R^h{}_j$, then $-2\sum_aR^h{}_aR^a{}_j$, then $-2\sum_{a,b}R^{ha}{}_{jb}R^b{}_a$, then $\sum R^{ha}{}_{bc}R^{bc}{}_{ja}$ over the entries with first label $h$ (the name `hh` is the entry's first label). Finally $2\mathcal{H}^h{}_j = 4t - \delta^h_j\,\mathrm{GB}$.

```python
check(all(P[2].get(hj, {}) == poly_mul(constant(-4), two_h[hj]) for hj in two_h)
      and L[2] == poly_add({}, GB, 4),
      "P(2) = -8 times the Gauss-Bonnet tensor for all 64 components and L(2) = 4 GB",
      record="Revision/gkd_lovelock/results/python-lovelock-report.json, checks "
             "k2_equals_minus_8_gauss_bonnet and L2_equals_4_gauss_bonnet")
```

$-4\cdot 2\mathcal{H} = -8\mathcal{H}$ must equal $P_{(2)}$ in all 64 components, and $L_{(2)} = 4\,\mathrm{GB}$: the result derived by hand in Section 11.15. Twenty-eighth PASS line.

**In [20], the cubic density.**

```python
T = [{} for _ in range(8)]  # T1 ... T8
for (a, b, c, d), v in RM.items():
    for (c2, d2, e, f), w in RM.items():
        if (c2, d2) == (c, d) and (e, f, a, b) in RM:  # R^ab_cd R^cd_ef R^ef_ab
            T[0] = poly_add(T[0], poly_mul(poly_mul(v, w), RM[(e, f, a, b)]))
```

Eight empty polynomials for the eight invariants (`T[0]` is $T_1$). For every entry $v = R^{ab}{}_{cd}$ and every entry $w$ whose upper pair is $(c, d)$, the product with $R^{ef}{}_{ab}$ is added to $T_1$, when that entry is nonzero.

```python
    for e in range(8):
        for f in range(8):
            if (c, e, b, f) in RM and (d, f, a, e) in RM:  # R^ab_cd R^ce_bf R^df_ae
                T[1] = poly_add(T[1], poly_mul(poly_mul(v, RM[(c, e, b, f)]),
                                               RM[(d, f, a, e)]))
        if (c, d, b, e) in RM:  # R^ab_cd R^cd_be R^e_a
            T[2] = poly_add(T[2], poly_mul(poly_mul(v, RM[(c, d, b, e)]), RIC[e, a]))
    T[4] = poly_add(T[4], poly_mul(poly_mul(v, RIC[c, a]), RIC[d, b]))  # R R^c_a R^d_b
```

Still inside the loop over $v = R^{ab}{}_{cd}$: $T_2 = R^{ab}{}_{cd}R^{ce}{}_{bf}R^{df}{}_{ae}$ over $e, f$; $T_3 = R^{ab}{}_{cd}R^{cd}{}_{be}R^e{}_a$ over $e$; and $T_5 = R^{ab}{}_{cd}R^c{}_aR^d{}_b$ (the comment's first R stands for the entry $v$).

```python
T[3] = poly_mul(R_SCALAR, riem_square)  # R R^ab_cd R^cd_ab
T[5] = poly_sum(poly_mul(poly_mul(RIC[a, b], RIC[b, c]), RIC[c, a])
                for a in range(8) for b in range(8) for c in range(8))
T[6] = poly_mul(R_SCALAR, ric_square)  # R R^a_b R^b_a
T[7] = poly_mul(poly_mul(R_SCALAR, R_SCALAR), R_SCALAR)  # R^3
```

The remaining four invariants: $T_4 = R\,R^{ab}{}_{cd}R^{cd}{}_{ab}$, $T_6 = R^a{}_bR^b{}_cR^c{}_a$, $T_7 = R\,R^a{}_bR^b{}_a$, $T_8 = R^3$.

```python
density = {}
for coefficient, t in zip([2, 8, 24, 3, 24, 16, -12, 1], T):
    density = poly_add(density, t, coefficient)
check(L[3] == poly_add({}, density, 8),
      "L(3) = 8 (2 T1 + 8 T2 + 24 T3 + 3 T4 + 24 T5 + 16 T6 - 12 T7 + T8)",
      record="Revision/gkd_lovelock/results/python-lovelock-report.json, check "
             "L3_equals_8_cubic_lovelock_density")
```

The cubic density with the record's coefficients, and the check $L_{(3)} = 8\times$ density. Twenty-ninth PASS line.

**In [21], the expansion along the column of h.**

```python
def expansion_sum(k):
    result = {}
    for h in range(8):
        first = [i for i, (key, _) in enumerate(ENTRIES) if key[0] == h]
```

`expansion_sum(k)` computes $Y_{(k)}$ of Section 11.13 (docstring left out). For each $h$, `first` lists the entries whose first upper label is $h$: these are the possible first factors $R^{hj_2}{}_{h_1h_2}$.

```python
        for j in range(8):
            bucket = {}
            stack = []
            for i in first:  # the first factor R^{h j2}_{h1 h2}
                a, b, c, d = ENTRIES[i][0]
                if b != j:  # j2 = j would repeat j in the lower list: GKD = 0
                    stack.append(((i,), (1 << j) | (1 << b), (1 << c) | (1 << d)))
```

For each $j$ the search starts with every possible first factor whose second upper label $j_2$ differs from $j$ (otherwise the delta's lower list $(j, j_2, \dots)$ would repeat a label). The lower mask holds $j$ and $j_2$; the upper mask the two lower labels $h_1, h_2$ of the factor. The label $h$ itself is not in the delta of $Y_{(k)}$.

```python
            while stack:
                chosen, lower_mask, upper_mask = stack.pop()
                if len(chosen) == k:  # a leaf
                    if lower_mask != upper_mask:
                        continue  # a lower label is missing above: GKD = 0
                    lower = [j, ENTRIES[chosen[0]][0][1]] + [
                        x for i in chosen[1:] for x in ENTRIES[i][0][:2]]
                    upper = [x for i in chosen for x in ENTRIES[i][0][2:]]
                    sign = gkd(lower, upper)
                    if sign != 0:
                        key = tuple(sorted(chosen))
                        bucket[key] = bucket.get(key, 0) + sign
                    continue
```

The same search as in In [13], with the lists of $Y_{(k)}$: the lower list is $j$, then $j_2$ (the second upper label of the first factor), then the upper labels of the other factors (`chosen[1:]` leaves out the first); the upper list is the lower labels of all factors.

```python
                free = np.nonzero(((LOWER_MASK & lower_mask) == 0)
                                  & ((UPPER_MASK & upper_mask) == 0))[0]
                for i in free:
                    stack.append((chosen + (int(i),), lower_mask | int(LOWER_MASK[i]),
                                  upper_mask | int(UPPER_MASK[i])))
            total = {}
            for key, weight in bucket.items():
                product = ONE
                for i in key:
                    product = poly_mul(product, ENTRIES[i][1])
                total = poly_add(total, product, weight)
            result[h, j] = total
    return result
```

The extension step and the multiplication of the weighted products, as before; the component $(h, j)$ of $Y_{(k)}$ is stored.

```python
Y = {k: expansion_sum(k) for k in (1, 2, 3)}
expansion_holds = all(
    P[k].get((h, j), {})
    == poly_add(poly_mul(delta[h, j], L[k]), Y[k][h, j], -2 * k)
    for k in (1, 2, 3) for h in range(8) for j in range(8))
check(expansion_holds and all(Y[1][hj] == poly_add({}, RIC[hj], 2) for hj in RIC),
      "P(k) = delta L(k) - 2k Y(k) for all 64 components, k = 1, 2, 3; Y(1) = 2 Ric")
```

$Y_{(k)}$ for the three orders, and the check of the expansion $P_{(k)} = \delta L_{(k)} - 2kY_{(k)}$ in all $3 \times 64$ components, together with $Y_{(1)} = 2\,\mathrm{Ric}$ of Section 11.14. Thirtieth PASS line.

**In [22], the trace identity and the four scalars.**

```python
def show(p):
    return str(sp.expand(sum(c * sp.prod([s ** e for s, e in zip(VARIABLES, m)])
                             for m, c in p.items())))
```

`show` turns a polynomial dictionary back into sympy text, for printing (docstring left out): each monomial is the product of the six variables raised to its exponents (`sp.prod` multiplies a list).

```python
for k in (1, 2, 3):
    trace = poly_sum(P[k].get((h, h), {}) for h in range(8))
    report(f"Lovelock scalar L({k})", show(L[k]))
    check(trace == poly_add({}, L[k], 8 - 2 * k),
          f"the trace of P({k}) is (8 - {2 * k}) L({k})",
          record=f"{RESULTS}/lovelock-report.json, check k{k}_trace_identity")
```

For each order the trace $\sum_hP_{(k)}{}^h{}_h$ is formed, the scalar is printed, and the trace identity of Section 11.14 is checked. The RESULT lines give $L_{(1)} = 16a_4'^2 - 16a_4'u - 4a_4'' - 24H^2k + 10u^2 + 8v$ and the scalars $L_{(2)}$ and $L_{(3)}$ with 16 and 20 terms; no third derivative and no $x_0$ appear. PASS lines thirty-one to thirty-three.

```python
L4 = from_mathematica(l4_text)  # the scalar printed by the program in section 5
report("eighth-order scalar L(4) (the Euler density)", L4)
report("L(4) on the history of the record (H = 1)",
       sp.factor(L4.subs({H: 1, A1: 1, A2: 0, U: sp.Rational(4, 3), V: 0})))
```

The formula of $L_{(4)}$ that the program printed in In [3] is read with `from_mathematica` and printed in full (25 terms). Then the history of the record is inserted ($H = 1$, $a_4' = 1$, $a_4'' = 0$, $u = \frac43$, $v = 0$; $k$ stays free), and `sp.factor` writes the result as a product: RESULT `2048*(729*K**2 - 378*K + 25)/27`, the formula of Section 11.11.

**In [23], the components at one moment (Figure 11b.5).**

```python
def poly_value(p, point):
    total = Fraction(0)
    for m, coefficient in p.items():
        term = coefficient
        for value, exponent in zip(point, m):
            term *= Fraction(value) ** exponent
        total += term
    return total
```

`poly_value` evaluates a polynomial dictionary exactly, with fractions, at a point given as the six values $(H, a_4', a_4'', u, v, k)$ (docstring left out): each monomial is its coefficient times each value raised to its exponent.

```python
POINT = (1, 1, 0, Fraction(4, 3), 0, 1)  # H, a4', a4'', u, v, k at x4 = 0
fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.6))
tables = {}
for ax, k in zip(axes, (1, 2, 3)):
    scale = Fraction(-1, 2 ** (k + 1))  # E_(k) = -P_(k) / 2^(k+1)
    table = [[scale * poly_value(P[k].get((h, j), {}), POINT) for j in range(8)]
             for h in range(8)]  # exact fractions
    tables[k] = table
    numbers = np.array([[float(x) for x in row] for row in table])
    largest = np.abs(numbers).max()
    ax.imshow(numbers, cmap="RdBu_r", vmin=-largest, vmax=largest)
```

`POINT` is the moment $x_4 = 0$ of the history of the record. Three panels, one per order. Each component of $E_{(k)} = -P_{(k)}/2^{k+1}$ is evaluated exactly at this point; the table of fractions is kept, turned into decimal numbers for the picture, and drawn with its own colour scale.

```python
    for h in range(8):
        for j in range(8):
            if h != j:
                colour = "0.6"  # grey zeros off the diagonal
            elif abs(numbers[h, j]) > 0.6 * largest:
                colour = "white"  # white on the darkest squares, to stay readable
            else:
                colour = "black"
            ax.text(j, h, str(table[h][j]), ha="center", va="center",
                    fontsize=6 if h == j else 5.5, color=colour)
```

Every value is written into its square as a fraction: grey for the zeros off the diagonal, white on the darkest squares and black elsewhere.

```python
    ax.set_xticks(range(8), NAMES)
    ax.set_yticks(range(8), NAMES)
    ax.set_xlabel("lower label $j$")
    ax.set_ylabel("upper label $h$")
    ax.set_title(f"$E_{{({k})}}{{}}^h{{}}_j$ in units of $H^{{{2 * k}}}$")
    ax.grid(False)
fig.tight_layout()
save_figure(fig, "lovelock_component_tables",
            "All 64 components $E_{(k)}{}^h{}_j$ of the normalised Lovelock tensors "
            ...)
```

Marks, axis titles and the panel titles (the doubled braces print single braces, so the title reads $E_{(k)}{}^h{}_j$ in units of $H^{2k}$), then the saved figure.

```python
diagonal_ok = all(
    all(tables[k][h][j] == 0 for h in range(8) for j in range(8) if h != j)
    and tables[k][1][1] == tables[k][2][2] == tables[k][3][3]
    and tables[k][0][0] == tables[k][5][5] == tables[k][6][6] == tables[k][7][7]
    for k in (1, 2, 3))
```

For each order: every entry off the diagonal is 0, the three space entries are equal, and the hidden entry equals the three extra-time entries.

```python
say("diagonals (x0 ... x7):")
for k in (1, 2, 3):
    say(f"  E({k}): " + " ".join(str(tables[k][h][h]) for h in range(8)))
check(diagonal_ok and [tables[1][h][h] for h in range(8)]
      == [Fraction(-2, 3)] + [Fraction(41, 9)] * 3 + [Fraction(19, 3)]
      + [Fraction(-2, 3)] * 3,
      "at x4 = 0 on the history of the record: only diagonal entries, space entries "
      "equal, hidden entry = extra-time entries; G = diag(-2/3, 41/9, 41/9, 41/9, "
      "19/3, -2/3, -2/3, -2/3) H^2")
```

The three diagonals are printed in the order $x_0, \dots, x_7$: $E_{(1)}$: $-\frac23$, $\frac{41}{9}$ (three times), $\frac{19}{3}$, $-\frac23$ (three times); $E_{(2)}$: $\frac{1868}{27}$, $\frac{1024}{27}$ (three times), $\frac{320}{27}$, $\frac{1868}{27}$ (three times); $E_{(3)}$: $-\frac{32}{3}$, $-\frac{8384}{27}$ (three times), $-320$, $-\frac{32}{3}$ (three times). Section 11.20 recomputes every one of these entries by hand. The check confirms the pattern and the Einstein diagonal. Thirty-fourth PASS line.

*What Figure 11b.5 shows.* Three $8 \times 8$ tables in units of $H^2$, $H^4$ and $H^6$, each filled only on its diagonal: the places of the components $x_4$-$x_0$ and $x_0$-$x_4$ are grey zeros like all other places off the diagonal. In each table the three squares of 3-space are equal, and the square of $x_0$ equals the three squares of the extra times. The time square $x_4$ stands apart: in $E_{(1)}$ it is the largest ($\frac{19}{3}$ against $\frac{41}{9}$ and $-\frac23$), in $E_{(2)}$ the smallest of the positive entries ($\frac{320}{27}$), and in $E_{(3)}$ the most negative ($-320$). Section 11.21 proves the patterns for every history.

**In [24], the quoted records once more.**

```python
def verdicts(path):
    data = json.loads(repository_file(path).read_text(encoding="utf-8"))
    checks = data["checks"]
    if isinstance(checks, dict):  # name -> {"passed": true or false, ...}
        return {name: "PASS" if entry["passed"] else "FAIL"
                for name, entry in checks.items()}
    return {entry["name"]: entry["verdict"] for entry in checks}  # a list of entries
```

The helper of Notebook 11a, In [16]: for one report, a dictionary from the name of each check to PASS or FAIL, for both forms in which the reports store their checks (docstring left out).

```python
QUOTED = {  # report -> the checks that this notebook quotes from it
    "python-lovelock-report.json": [
        "rust_riemann_agrees", "rust_k1_mixed_components_agree",
        "rust_k2_mixed_components_agree", "rust_k3_mixed_components_agree",
        "rust_L1_agrees", "rust_L2_agrees", "rust_L3_agrees",
        "k1_unpruned_literal_sum_agrees", "k2_unpruned_literal_sum_agrees",
        "k1_equals_minus_4_einstein", "L1_equals_2R",
        "k2_equals_minus_8_gauss_bonnet", "L2_equals_4_gauss_bonnet",
        "L3_equals_8_cubic_lovelock_density", "normalisation_P1_derived_minus_4",
        "normalisation_P2_derived_minus_8", "normalisation_L3_cubic_derived",
        "mixed_riemann_only_sectional", "rust_christoffels_agree"],
    "lovelock-report.json": [
        "riemann_antisymmetry", "mixed_riemann_free_of_x0",
        "mixed_riemann_only_sectional", "k1_trace_identity", "k2_trace_identity",
        "k3_trace_identity", "k1_offdiagonal_vanishes", "k2_offdiagonal_vanishes",
        "k3_offdiagonal_vanishes", "k1_hidden_equals_extra_times",
        "k2_hidden_equals_extra_times", "k3_hidden_equals_extra_times",
        "k4_tensor_vanishes", "k1_brute_force_numeric", "k2_brute_force_numeric"],
}
```

The 19 checks that the notebook's text quotes from the sympy report and the 15 that it quotes from the Rust report.

```python
for report_name, names in QUOTED.items():
    found = verdicts(f"{RESULTS}/{report_name}")
    missing = [name for name in names if found.get(name) != "PASS"]
    say(f"{report_name}: {len(names)} quoted checks; not there or not PASS: "
        f"{missing if missing else 'none'}")
    check(not missing,
          f"the {len(names)} checks quoted from {report_name} are there and PASS",
          record=f"{RESULTS}/{report_name}, checks " + ", ".join(names))
```

For each report the list `missing` collects every quoted check that is absent or not PASS; it is printed ("none") and must be empty (`not missing` is true for an empty list). PASS lines thirty-five and thirty-six.

```python
totals = {}
for report_name in ("python-lovelock-report.json", "wolfram-gkd-report.json"):
    data = json.loads(repository_file(f"{RESULTS}/{report_name}").read_text(
        encoding="utf-8"))
    totals[report_name] = (data["checkCount"], data["failedCheckCount"],
                           data["verdict"])
    say(f"{report_name}: {data['checkCount']} checks, {data['failedCheckCount']} "
        f"failed, verdict {data['verdict']}")
```

The numbers of checks of the two verification reports are read and printed: 56 checks, 0 failed, verdict SUCCESS for the sympy report, and 29, 0, SUCCESS for the Wolfram report.

```python
check(totals == {"python-lovelock-report.json": (56, 0, "SUCCESS"),
                 "wolfram-gkd-report.json": (29, 0, "SUCCESS")},
      "the sympy verification has 56 checks and the Wolfram verification 29, none "
      "failed",
      record=f"{RESULTS}/python-lovelock-report.json and wolfram-gkd-report.json, "
             "checkCount and failedCheckCount")
```

The counts quoted in the notebook's text are fixed by this check, so a later change of either report would be noticed. Thirty-seventh PASS line.

**In [25], the end.**

```python
figure_files = [f"11b_{k}_{name}.png" for k, name in enumerate(
    ["work_of_the_sums", "curvature_of_planes", "riemann_matrix",
     "mixing_terms_vanish", "lovelock_component_tables"], 1)]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_files),
      "all five figure files of the notebook exist")
all_checks_passed()
```

As in Notebook 11a, In [17]: the five figure files must exist (thirty-eighth PASS line), and the last line is ALL 38 CHECKS PASSED (notebook 11b). The 38 checks are: 2 in In [3], 4 in In [4], 1 each in In [5], In [6] and In [7], 5 in In [8], 1 each in In [9] and In [10], 2 in In [11], 1 in In [12], 1 in In [14], 3 in In [15], 2 in In [16], 1 each in In [17] to In [21], 3 in In [22], 1 in In [23], 3 in In [24] and 1 in In [25].

### 11.20 The components of the three tensors for the author's metric

**The result (PROVED by exact computation).** The Rust program of the record computes all $3 \times 64$ components of $P_{(1)}, P_{(2)}, P_{(3)}$ exactly, for general functions $a_4(x_4)$ and $b_4(x_4)$, and writes them into the record `lovelock-tensors.json`. The Revision's sympy and Wolfram verifications recompute every one of them independently and find the same (checks `rust_k1_mixed_components_agree` to `rust_k3_mixed_components_agree` of the sympy report, and `k1_P_equals_rust_all_64_components` to `k3_P_equals_rust_all_64_components` of the Wolfram report), and so does Notebook 11b (In [15]). Only the eight diagonal components are nonzero, for every order and every history (record checks `k1_offdiagonal_vanishes` to `k3_offdiagonal_vanishes`); the three space components are equal, and the hidden component equals the three extra-time components (checks `k1_hidden_equals_extra_times` to `k3_hidden_equals_extra_times`). With $E_{(k)} = -P_{(k)}/2^{k+1}$, the three independent components of each order are, in the six variables of Section 11.2:

$$
\begin{aligned}
E_{(1)}{}^{x_1}{}_{x_1} &= 2a_4'' - 5a_4'^2 + 6a_4'u + 6H^2k - \tfrac52u^2 - 2v,\qquad E_{(1)}{}^{x_4}{}_{x_4} = 3a_4'^2 + 6H^2k - \tfrac32u^2,\\
E_{(1)}{}^{x_0}{}_{x_0} &= -3a_4'^2 + \tfrac32a_4'u + 3H^2k - \tfrac32u^2 - \tfrac32v,
\end{aligned}
$$

$$
\begin{aligned}
E_{(2)}{}^{x_1}{}_{x_1} &= 28a_4'^4 - 48a_4'^3u - 48a_4'^2a_4'' + 48a_4'^2H^2k + 20a_4'^2u^2 + 16a_4'^2v + 32a_4'a_4''u \\
&\quad - 24a_4'H^2ku + 6a_4'u^3 - 12H^4k^2 + 18H^2ku^2 + 24H^2kv - \tfrac{15}{4}u^4 - 6u^2v,\\
E_{(2)}{}^{x_4}{}_{x_4} &= -36a_4'^4 - 48a_4'^2H^2k + 36a_4'^2u^2 + 48a_4'H^2ku - 12a_4'u^3 - 12H^4k^2 + 6H^2ku^2 - \tfrac34u^4,\\
E_{(2)}{}^{x_0}{}_{x_0} &= 12a_4'^4 - 12a_4'^3u + 48a_4'^2H^2k + 18a_4'^2u^2 + 12a_4'^2v + 24a_4'a_4''u + 6a_4'H^2ku \\
&\quad - \tfrac{15}{2}a_4'u^3 - 12a_4'uv + 24a_4''H^2k - 6a_4''u^2 + 3H^2ku^2 + 6H^2kv - \tfrac34u^4 - \tfrac32u^2v,
\end{aligned}
$$

$$
\begin{aligned}
E_{(3)}{}^{x_1}{}_{x_1} &= -216a_4'^6 + 432a_4'^5u + 720a_4'^4a_4'' - 144a_4'^4H^2k - 180a_4'^4u^2 - 144a_4'^4v - 576a_4'^3a_4''u \\
&\quad + 144a_4'^3H^2ku - 108a_4'^3u^3 - 216a_4'^2H^4k^2 - 180a_4'^2H^2ku^2 - 144a_4'^2H^2kv + \tfrac{189}{2}a_4'^2u^4 \\
&\quad + 108a_4'^2u^2v - 288a_4'a_4''H^2ku + 72a_4'a_4''u^3 + 72a_4'H^2ku^3 + 144a_4'H^2kuv - 18a_4'u^5 \\
&\quad - 36a_4'u^3v - 144a_4''H^4k^2 + 72a_4''H^2ku^2 - 9a_4''u^4,\\
E_{(3)}{}^{x_4}{}_{x_4} &= 360a_4'^6 + 432a_4'^4H^2k - 540a_4'^4u^2 - 864a_4'^3H^2ku + 360a_4'^3u^3 - 216a_4'^2H^4k^2 \\
&\quad + 324a_4'^2H^2ku^2 - \tfrac{135}{2}a_4'^2u^4,\\
E_{(3)}{}^{x_0}{}_{x_0} &= -72a_4'^6 + 108a_4'^5u - 216a_4'^4H^2k - 216a_4'^4u^2 - 108a_4'^4v - 432a_4'^3a_4''u + 108a_4'^3H^2ku \\
&\quad + 171a_4'^3u^3 + 216a_4'^3uv - 432a_4'^2a_4''H^2k + 324a_4'^2a_4''u^2 + 54a_4'^2H^2ku^2 + 108a_4'^2H^2kv \\
&\quad - \tfrac{81}{2}a_4'^2u^4 - 81a_4'^2u^2v + 216a_4'a_4''H^2ku - 54a_4'a_4''u^3,
\end{aligned}
$$

with $E^{x_2}{}_{x_2} = E^{x_3}{}_{x_3} = E^{x_1}{}_{x_1}$ and $E^{x_5}{}_{x_5} = E^{x_6}{}_{x_6} = E^{x_7}{}_{x_7} = E^{x_0}{}_{x_0}$ for every order. These are exactly the components that the record of the field equations lists (`Revision/field_equations_a4/a4-equations.json`, key `lovelockTensors`, compared in its sympy report `Revision/field_equations_a4/reports/python-a4-report.json`, check `json_lovelock_components`); Notebook 11c reads them from the Rust record, prints them and compares them with this list and with the independent sympy results (In [2] and In [3]). The components contain only the six variables: no $x_0$ (no $\cot z$ and no $(\sin^2z)^{1/12}$), no $a_4$ and no $b_4$ except through $u$, $v$ and $k$, and no third derivative. The order-1 components are those of the Einstein tensor of Section 11.10, as Section 11.14 proved they must be.

**Every component checked by hand, on the history of the record.** On the histories $a_4 = AHx_4$, $b_4 = b_4(0)\,e^{(4/3)AHx_4}$ we have $a_4' = AH$, $u = \frac43AH$, $a_4'' = v = 0$, and the components become short polynomials in the slope $A$ and in $k$. Order 1, line by line:

$$
\begin{aligned}
E_{(1)}{}^{x_4}{}_{x_4} &= 3A^2H^2 + 6H^2k - \tfrac32\cdot\tfrac{16}{9}A^2H^2\\
&= \big(3 - \tfrac83\big)A^2H^2 + 6H^2k = \tfrac13A^2H^2 + 6H^2k,\\
E_{(1)}{}^{x_1}{}_{x_1} &= -5A^2H^2 + 6\cdot\tfrac43A^2H^2 + 6H^2k - \tfrac52\cdot\tfrac{16}{9}A^2H^2\\
&= \big(-5 + 8 - \tfrac{40}{9}\big)A^2H^2 + 6H^2k = -\tfrac{13}{9}A^2H^2 + 6H^2k,\\
E_{(1)}{}^{x_0}{}_{x_0} &= -3A^2H^2 + \tfrac32\cdot\tfrac43A^2H^2 + 3H^2k - \tfrac32\cdot\tfrac{16}{9}A^2H^2\\
&= \big(-3 + 2 - \tfrac83\big)A^2H^2 + 3H^2k = -\tfrac{11}{3}A^2H^2 + 3H^2k
\end{aligned}
$$

(in each line: insert $a_4' = AH$, $u = \frac43AH$, $u^2 = \frac{16}{9}A^2H^2$, $a_4'' = v = 0$; take out $A^2H^2$; add the fractions). For the time component of order 2, with $H = 1$, the eight terms become $-36A^4 - 48A^2k + 36\cdot\frac{16}{9}A^4 + 48\cdot\frac43A^2k - 12\cdot\frac{64}{27}A^4 - 12k^2 + 6\cdot\frac{16}{9}A^2k - \frac34\cdot\frac{256}{81}A^4$, and collecting equal powers,

$$
E_{(2)}{}^{x_4}{}_{x_4} = \Big(-36 + 64 - \tfrac{256}{9} - \tfrac{64}{27}\Big)A^4 + \Big(-48 + 64 + \tfrac{32}{3}\Big)A^2k - 12k^2 = -\tfrac{76}{27}A^4 + \tfrac{80}{3}A^2k - 12k^2
$$

($-36 + 64 = 28 = \frac{756}{27}$, $\frac{256}{9} = \frac{768}{27}$, so $\frac{756 - 768 - 64}{27} = -\frac{76}{27}$; and $16 + \frac{32}{3} = \frac{80}{3}$). The other components reduce in the same way; Notebook 11c prints all nine (In [6]):

| order | time $E^{x_4}{}_{x_4}$ | space $E^{x_1}{}_{x_1}$ | block $E^{x_0}{}_{x_0} = E^{x_5}{}_{x_5}$ |
| --- | --- | --- | --- |
| 1 (units $H^2$) | $\frac13A^2 + 6k$ | $-\frac{13}{9}A^2 + 6k$ | $-\frac{11}{3}A^2 + 3k$ |
| 2 (units $H^4$) | $-\frac{76}{27}A^4 + \frac{80}{3}A^2k - 12k^2$ | $\frac{52}{27}A^4 + 48A^2k - 12k^2$ | $\frac{212}{27}A^4 + \frac{184}{3}A^2k$ |
| 3 (units $H^6$) | $40A^6 - 144A^4k - 216A^2k^2$ | $\frac{184}{27}A^6 - \frac{304}{3}A^4k - 216A^2k^2$ | $-\frac{104}{3}A^6 + 24A^4k$ |

At the moment $x_4 = 0$ of the history of the record, $A = 1$ and $k = 1$, so each entry is the sum of its coefficients:

$$
\begin{aligned}
E_{(1)} &: \quad \tfrac13 + 6 = \tfrac{19}{3},\qquad -\tfrac{13}{9} + 6 = \tfrac{41}{9},\qquad -\tfrac{11}{3} + 3 = -\tfrac23,\\
E_{(2)} &: \quad -\tfrac{76}{27} + \tfrac{720}{27} - \tfrac{324}{27} = \tfrac{320}{27},\qquad \tfrac{52}{27} + 36 = \tfrac{1024}{27},\qquad \tfrac{212}{27} + \tfrac{1656}{27} = \tfrac{1868}{27},\\
E_{(3)} &: \quad 40 - 144 - 216 = -320,\qquad \tfrac{184}{27} - \tfrac{2736}{27} - \tfrac{5832}{27} = -\tfrac{8384}{27},\qquad -\tfrac{104}{3} + 24 = -\tfrac{32}{3}
\end{aligned}
$$

(time, space and block in this order; every whole number written over the common denominator). In the order $x_0, \dots, x_7$ the diagonals at this moment are

$$
\begin{aligned}
E_{(1)} &= \big(-\tfrac23, \tfrac{41}{9}, \tfrac{41}{9}, \tfrac{41}{9}, \tfrac{19}{3}, -\tfrac23, -\tfrac23, -\tfrac23\big)H^2,\\
E_{(2)} &= \big(\tfrac{1868}{27}, \tfrac{1024}{27}, \tfrac{1024}{27}, \tfrac{1024}{27}, \tfrac{320}{27}, \tfrac{1868}{27}, \tfrac{1868}{27}, \tfrac{1868}{27}\big)H^4,\\
E_{(3)} &= \big(-\tfrac{32}{3}, -\tfrac{8384}{27}, -\tfrac{8384}{27}, -\tfrac{8384}{27}, -320, -\tfrac{32}{3}, -\tfrac{32}{3}, -\tfrac{32}{3}\big)H^6,
\end{aligned}
$$

exactly the numbers that Notebook 11b computes from its own GKD sums (In [23], Figure 11b.5).

**What is and is not established about the author's own results.** The author's stored outputs belong to the metric of 2026-10-14, withdrawn on 2026-10-16. Compared with the frozen record of that metric, the author's metric, his Ricci scalar and all 64 components of his Einstein tensor agree exactly (`Revision/gkd_lovelock/comparison/author-comparison-report.json`: 80 checks, 75 PASS, 0 FAIL, 5 NOT-AVAILABLE; `Revision/docs/LOVELOCK_GKD.md`, section 8.2), and so do the Lovelock tensors of orders 1 to 3 that a third notebook of the author, `Dirac_Einstein-Lovelock_4+4_Nash.nb`, stores for that metric (`Revision/metric_b4/METRIC_CHANGE_PROVENANCE.md`, the check file `verify_metric_b4.wls`; `Revision/docs/LOVELOCK_GKD.md`, section 8.4). For the corrected metric no output of the author exists. Agreement with Lovelock tensors computed by the author for the corrected metric is therefore NOT established; what is established is that three independent programs, the Rust program, the sympy checker and the Wolfram check, agree on every component.

### 11.21 Their structure: diagonal, equal directions, constraint, second derivatives, powers of k, sign and weight

The components have a clear structure, which Chapter 12 uses at every step. We prove each part by hand from the curvature of Section 11.10 and from the rule GKD; Notebook 11c confirms every part with exact algebra (In [2] for parts (a) and (b), In [4] for parts (c) to (h)).

**Four tools.** (i) **Relabelling.** If a bijection $\tau$ of the eight labels is applied to every label of both lists of a generalized delta, its matrix does not change, because $\delta(\tau l_i, \tau u_j) = \delta(l_i, u_j)$ ($\tau$ maps equal labels to equal labels and different labels to different labels); so $\delta^{\tau U}_{\tau L} = \delta^U_L$. And because $\tau$ runs through all labels exactly once, a sum over all values of the summed labels is unchanged when every summed label is replaced by its image. (ii) **Plane entries.** Every nonzero curvature entry carries the same two labels in its upper and in its lower pair (Section 11.10). (iii) **The label $x_4$ and the second derivatives.** Every entry that contains $a_4''$ or $v$ is an entry of a plane $(c, x_4)$: it carries $x_4$ in both pairs. (iv) **The block and $k$.** Every entry that contains $k$ is an entry of a plane inside the block: it carries two of the four labels $x_0, x_5, x_6, x_7$ in both pairs.

**(a) Only diagonal components (PROVED).** In a term of $P_{(k)}{}^h{}_j$ the delta's lower list is $j$ followed by the upper pairs of the factors, and its upper list is $h$ followed by their lower pairs. By tool (ii) the factors bring the same labels to both lists. For a nonzero term the two lists must hold the same set of labels (case c of Section 11.3), and they do exactly when $\{j\} = \{h\}$. So every off-diagonal component vanishes identically, for every order and every history (record checks `k1_offdiagonal_vanishes` to `k3_offdiagonal_vanishes`; Notebook 11b, In [15]; Notebook 11c, In [2]). In the withdrawn metric of 2026-10-14 the mixed entries $R^{x_4c}{}_{x_0c}$ brought $x_4$ to one list and $x_0$ to the other, and that allowed the components $P^{x_4}{}_{x_0}$ and $P^{x_0}{}_{x_4}$; their absence is the whole effect of the correction on the Lovelock tensors.

**(b) Equal directions, and the hidden direction equal to the extra times (PROVED).** The relabelling that exchanges $x_1$ and $x_2$ is a change of coordinates that leaves the metric unchanged ($g_{11} = g_{22}$), so it maps every curvature entry to the entry with the exchanged labels, of the same value. By tool (i) it maps the sum $P^{x_1}{}_{x_1}$ term by term onto $P^{x_2}{}_{x_2}$: the two are equal. The same holds for $x_3$, and for the extra times $x_5, x_6, x_7$. For the hidden direction we use the relabelling $\tau$ that exchanges $x_0$ and $x_5$. It is NOT a symmetry of the metric ($g_{00}$ and $g_{55}$ are different functions of $z$), but it maps every curvature entry to an entry of the same value: the table of Section 11.10 gives every plane with $x_0$ the curvature of the same plane with an extra time in place of $x_0$ (the block has constant curvature, Section 3.9), the plane $(x_0, x_5)$ goes to itself, and the other planes are not touched. So by tool (i) $\tau$ maps $P^{x_0}{}_{x_0}$ term by term onto $P^{x_5}{}_{x_5}$:

$$
E^{x_0}{}_{x_0} = E^{x_5}{}_{x_5}\qquad\text{for } k = 1, 2, 3
$$

(record checks `k1_hidden_equals_extra_times` to `k3_hidden_equals_extra_times`). Section 11.22 obtains the same equality a second time, from conservation.

**(c) The second derivatives enter at most linearly (PROVED).** By tool (iii) an entry with $a_4''$ or $v$ puts the label $x_4$ into both lists of the delta. Two such entries in one term would repeat $x_4$ in both lists, and GKD would be 0. So every component has the form (polynomial without second derivatives) $+ a_4''\cdot$(polynomial) $+ v\cdot$(polynomial), with no products $a_4''^2$, $a_4''v$, $v^2$, and the two polynomials free of second derivatives.

**(d) The time component contains no second derivative: the constraint (PROVED).** In $P^{x_4}{}_{x_4}$ the label $x_4$ already stands in both lists (as $h$ and $j$), so no factor may carry $x_4$: by tool (iii) no entry with $a_4''$ or $v$ occurs. The factors are curvatures of planes among $x_0, x_1, x_2, x_3, x_5, x_6, x_7$: $a_4'^2$, $-a_4'(a_4' - \frac12u)$ and $(a_4' - \frac12u)^2 - H^2k$. So $E^{x_4}{}_{x_4}$ is a polynomial in $H$, $a_4'$, $u$ and $k$ alone, as the list of Section 11.20 shows. In the field equations this component is the **constraint**: a condition on the first derivatives, not an equation for their change (record `python-a4-report.json`, check `constraint_first_order`).

**(e) The second-order system (PROVED by exact computation).** By part (c) the space and the block components are linear in $a_4''$ and $v$:

$$
E^{x_1}{}_{x_1} = \ldots + J_{11}\,a_4'' + J_{12}\,v,\qquad E^{x_0}{}_{x_0} = \ldots + J_{21}\,a_4'' + J_{22}\,v ,
$$

where the dots and the four coefficients $J$ contain no second derivative. For Einstein's tensor the list of Section 11.20 gives $J = \begin{pmatrix}2 & -2\\ 0 & -\frac32\end{pmatrix}$ ($2a_4'' - 2v$ in the space component, $-\frac32v$ in the block component; Notebook 11c, In [4]). In the field equations, where the matrix $\sum_k\alpha_kJ_{(k)}$ has a nonzero determinant, the space and the block equations determine $a_4''$ and $v$, that is how $a_4$ and $b_4$ change, while the time component is the constraint. The record lists this matrix and its determinant (`a4-equations.json`, key `generalSource`, entries `secondOrderJacobian` and `secondOrderJacobianDet`; `python-a4-report.json`, check `second_order_system`); Notebook 11c reproduces the matrix from the components (In [4]). Chapter 12 uses it.

**(f) How the components depend on $k$ (PROVED).** By tool (iv) every factor that contains $k$ uses two of the four block labels in both lists, and a block label cannot repeat. In $P^{x_0}{}_{x_0}$ the label $x_0$ already stands in both lists, so only three block labels are left: at most one block plane fits into a term, and the hidden component, like each extra-time component, is **at most linear in $k$**. In $P^{x_1}{}_{x_1}$ and $P^{x_4}{}_{x_4}$ all four block labels are free: at most two block planes, so at most $k^2$; for order 1 there is only one factor, so at most $k$. Notebook 11c finds the degrees (space, time, block) $= (1, 1, 1)$, $(2, 2, 1)$ and $(2, 2, 1)$ for $k = 1, 2, 3$ (In [4]). In the field equations this says that the source component $p_0 = p_t$ grows at most like $k$, while $\rho$ and $p_3$ may grow like $k^2$ (Section 11.23).

**(g) Reversing the time: deflation is a choice of sign (PROVED).** Use the coordinate $y_4 = -x_4$ instead of $x_4$. Since $dx_4^2 = dy_4^2$, the metric in the new coordinates has exactly the corrected form, with the functions $\tilde a_4(y_4) = a_4(-y_4)$ and $\tilde b_4(y_4) = b_4(-y_4)$. Its Lovelock components are therefore given by the same polynomials, with the new variables

$$
\tilde a_4' = -a_4',\qquad \tilde a_4'' = a_4'',\qquad \tilde u = \tilde b_4'/\tilde b_4 = -u,\qquad \tilde v = v,\qquad \tilde k = k
$$

(the chain rule: each derivative brings a factor $dx_4/dy_4 = -1$, so first derivatives change sign and second derivatives do not; $k$ contains no derivative). On the other hand a diagonal component of a tensor with one upper and one lower label does not change under this reflection: the component $x_4x_4$ is multiplied by $(-1)(-1) = 1$, and the others are not touched (the tensor rule of Section 3.14; $P_{(k)}$ is a tensor, built from the Riemann tensor and the generalized delta). So every diagonal component satisfies

$$
E(H, -a_4', a_4'', -u, v, k) = E(H, a_4', a_4'', u, v, k)
$$

at every point and for every history. Any five numbers are the values of $a_4'$, $a_4''$, $u$, $v$ and $k$ at $x_4 = 0$ of some history (for example $a_4 = c_1x_4 + \frac12c_2x_4^2 + c_0$ and $b_4 = b_0\,e^{d_1x_4 + d_2x_4^2/2}$ with $e^{2c_0}/b_0$ equal to the chosen $k$), so the identity holds for all values: **every component is unchanged when $a_4'$ and $u$ change sign together**. On the histories of the record this is $A \to -A$: the deflating block with inflating 3-space ($A > 0$) and the reverse ($A < 0$) give the same tensors at equal $k$. The gravitational side of the field equations does not prefer deflation; deflation of the extra times is a choice of sign (Chapter 12 draws the consequences). Notebook 11c checks the symmetry exactly (In [4]) and draws it (In [6], Figure 11c.1, top row).

**(h) Weight $2k$ (PROVED in Section 11.11).** Every term of $E_{(k)}$ has the weight $2k$ when $H$, $a_4'$ and $u$ count 1, $a_4''$ and $v$ count 2, and $k$ counts 0: $E_{(1)}$ is quadratic, $E_{(2)}$ quartic, $E_{(3)}$ of sixth degree in this sense. Notebook 11c checks it by replacing $H, a_4', u$ by $sH, sa_4', su$ and $a_4'', v$ by $s^2a_4'', s^2v$ and finding the factor $s^{2k}$ (In [4]).

### 11.22 The two conservation identities

Every Lovelock tensor has zero covariant divergence (Lovelock's theorem; for the corrected metric PROVED by exact computation: `Revision/gkd_lovelock/results/lovelock-report.json`, checks `k1_divergence_free` to `k3_divergence_free`). For this metric the one statement becomes two short identities between the components. We derive them for every order, line by line.

**The divergence of a diagonal tensor.** For a tensor $P^h{}_j$ with one upper and one lower label, the covariant divergence is

$$
\nabla_hP^h{}_j = \sum_h\partial_hP^h{}_j + \sum_{h,m}\Gamma^h{}_{hm}P^m{}_j - \sum_{h,m}\Gamma^m{}_{hj}P^h{}_m
$$

(one $+\Gamma$ for the upper label, one $-\Gamma$ for the lower label, then the upper label contracted with the derivative; Section 3.15). If $P$ is diagonal, the first sum keeps $h = j$, the second keeps $m = j$, and the third keeps $m = h$:

$$
\nabla_hP^h{}_j = \partial_jP^j{}_j + \sum_h\Gamma^h{}_{hj}\big(P^j{}_j - P^h{}_h\big)\qquad(\text{no sum over } j)
$$

(the second and third sums combined, since both now run over $h$).

**The time direction, $j = x_4$.** The symbols $\Gamma^h{}_{hx_4}$ are the rates of Section 11.10: $a_4'$ for the three space directions, $h_4 = \frac12u - a_4'$ for the hidden direction and the three extra times, and 0 for $x_4$. So

$$
\nabla_hP^h{}_{x_4} = \partial_4P^{x_4}{}_{x_4} + 3a_4'\big(P^{x_4}{}_{x_4} - P^{x_1}{}_{x_1}\big) + 4h_4\big(P^{x_4}{}_{x_4} - P^{x_0}{}_{x_0}\big)
$$

(the three space components are equal, and so are the four block components, Section 11.21 (b)). Setting the divergence to zero, multiplying by $-1/2^{k+1}$ and moving the last two terms to the other side:

$$
\frac{d}{dx_4}E^{x_4}{}_{x_4} = 3a_4'\big(E^{x_1}{}_{x_1} - E^{x_4}{}_{x_4}\big) + 4h_4\big(E^{x_0}{}_{x_0} - E^{x_4}{}_{x_4}\big),\qquad h_4 = \tfrac12u - a_4'. \qquad\text{(I)}
$$

**The hidden direction, $j = x_0$.** Nothing depends on $x_0$ (record checks `k1_free_of_x0` to `k3_free_of_x0`), so $\partial_0P^{x_0}{}_{x_0} = 0$. The symbols $\Gamma^h{}_{hx_0}$ are $\partial_0\ln f_h$: $H\cot z$ for the three extra times, 0 for 3-space (no warp) and for $x_4$; the term $h = x_0$ has the factor $P^{x_0}{}_{x_0} - P^{x_0}{}_{x_0} = 0$. So

$$
\nabla_hP^h{}_{x_0} = 3H\cot z\,\big(P^{x_0}{}_{x_0} - P^{x_5}{}_{x_5}\big),
$$

and wherever $\cot z \ne 0$ (away from the fold $\cos z = 0$) zero divergence gives

$$
E^{x_0}{}_{x_0} = E^{x_5}{}_{x_5}. \qquad\text{(II)}
$$

This is part (b) of Section 11.21 once more, now as a consequence of conservation.

**The transverse directions.** For $j$ one of $x_1, x_2, x_3, x_5, x_6, x_7$: nothing depends on $x_j$, and every $\Gamma^h{}_{hj}$ is zero, so the divergence vanishes without any condition.

**Identity (I) checked by hand for Einstein's tensor.** The time component depends on $x_4$ only through $a_4'$, $u$ and $k$ (Section 11.21 (d)), and $k' = k(2a_4' - u)$ (the derivative of $\ln k = 2a_4 - \ln b_4$ is $2a_4' - u$). So by the chain rule

$$
\frac{d}{dx_4}E^{x_4}{}_{x_4} = \frac{\partial E^{x_4}{}_{x_4}}{\partial a_4'}\,a_4'' + \frac{\partial E^{x_4}{}_{x_4}}{\partial u}\,v + \frac{\partial E^{x_4}{}_{x_4}}{\partial k}\,k(2a_4' - u) .
$$

For $E_{(1)}{}^{x_4}{}_{x_4} = 3a_4'^2 + 6H^2k - \frac32u^2$ the left side of (I) is therefore

$$
6a_4'a_4'' - 3uv + 6H^2k(2a_4' - u) = 6a_4'a_4'' - 3uv + 12a_4'H^2k - 6H^2ku
$$

(the three partial derivatives are $6a_4'$, $-3u$ and $6H^2$). On the right side, from Section 11.20,

$$
E^{x_1}{}_{x_1} - E^{x_4}{}_{x_4} = 2a_4'' - 2v - 8a_4'^2 + 6a_4'u - u^2,\qquad E^{x_0}{}_{x_0} - E^{x_4}{}_{x_4} = -\tfrac32v - 6a_4'^2 + \tfrac32a_4'u - 3H^2k
$$

(subtract term by term). Multiply the first by $3a_4'$ and the second by $4h_4 = 2u - 4a_4'$:

$$
\begin{aligned}
3a_4'(\ldots) &= 6a_4'a_4'' - 6a_4'v - 24a_4'^3 + 18a_4'^2u - 3a_4'u^2,\\
(2u - 4a_4')(\ldots) &= -3uv + 6a_4'v - 12a_4'^2u + 3a_4'u^2 - 6H^2ku + 24a_4'^3 - 6a_4'^2u + 12a_4'H^2k .
\end{aligned}
$$

Their sum: $6a_4'a_4''$ stays; $-6a_4'v + 6a_4'v = 0$; $-24a_4'^3 + 24a_4'^3 = 0$; $18a_4'^2u - 12a_4'^2u - 6a_4'^2u = 0$; $-3a_4'u^2 + 3a_4'u^2 = 0$; and $-3uv$, $-6H^2ku$, $12a_4'H^2k$ stay. So the right side is $6a_4'a_4'' - 3uv + 12a_4'H^2k - 6H^2ku$, the left side. Notebook 11c prints both sides (In [5]) and checks (I) exactly for $k = 1, 2, 3$, and (II) as well. The record states (I) as its **constraint propagation**: the derivative of the constraint is fixed by the other two components, so a history that satisfies the space and block equations keeps satisfying the constraint (`a4-equations.json`, key `generalSource`, entry `constraint_propagation`; `python-a4-report.json`, check `bianchi_x4`).

**What they mean in the field equations (a preview of Chapter 12).** In $\sum_k\alpha_kE_{(k)} + \Lambda\delta = \kappa T$, with $T = \mathrm{diag}(p_0, p_3, p_3, p_3, -\rho, p_t, p_t, p_t)$ (in the order $x_0, \dots, x_7$), the components are $\sum_k\alpha_kE^{x_4}{}_{x_4} = -\kappa\rho - \Lambda$, $\sum_k\alpha_kE^{x_1}{}_{x_1} = \kappa p_3 - \Lambda$ and $\sum_k\alpha_kE^{x_0}{}_{x_0} = \kappa p_0 - \Lambda$. Identity (II) then requires $p_0 = p_t$: the pressure along the hidden direction equals that along the extra times (record `a4-equations.json`, key `generalSource`, entry `hiddenEqualsExtraTimes`). Identity (I) becomes the energy balance

$$
\rho' = -3a_4'\,(\rho + p_3) - 4h_4\,(\rho + p_0)
$$

($-\kappa\rho'$ on the left; on the right $3a_4'(\kappa p_3 + \kappa\rho) + 4h_4(\kappa p_0 + \kappa\rho)$, since $\Lambda$ cancels in each difference; then divide by $-\kappa$): each expanding or shrinking direction changes the energy density at its own rate, 3-space with $\rho + p_3$ and the four directions of the block with $\rho + p_0$ (record entry `energyExchange`). On the history of the record $h_4 = \frac23H - H = -\frac13H$, so the term of the block is $-4h_4(\rho + p_0) = \frac43H(\rho + p_0)$: where $\rho + p_0 > 0$ the shrinking block raises the energy density. Notebook 11c checks that the record states these consequences (In [12]).

### 11.23 Along the deflating history; an illustrative test history

**The histories of the record (PROVED).** Along $a_4 = AHx_4$, $b_4 = b_4(0)\,e^{(4/3)AHx_4}$ every component is $H^{2k}$ times a polynomial in the slope $A$ and in $k = e^{(2/3)AHx_4}/b_4(0)$: the table of Section 11.20 (Notebook 11c, In [6]). Two facts can be read off. First, every entry is even in $A$ at fixed $k$: the histories $A$ and $-A$ give the same tensors at equal $k$ (Section 11.21 (g)). Second, the block entries are at most linear in $k$, the others at most quadratic (Section 11.21 (f)). On the history of the record ($A = 1$, $b_4(0) = 1$) $k = e^{2Hx_4/3}$ grows, and so does every component: the curvature $-H^2k$ of the shrinking block grows as the block shrinks. Figure 11c.1 draws the components against $A$ at the moment $k = 1$ (top row) and along the history of the record against $Hx_4$ (bottom row).

**The source that this history needs (PROVED by exact computation).** With the components on the history, the field equations of Section 11.22 give the source that the history needs. For Einstein gravity ($\alpha_1 = 1$, $\alpha_2 = \alpha_3 = 0$) it is the order-1 row of the table at $A = 1$:

$$
-\kappa\rho - \Lambda = \tfrac13H^2 + 6H^2k,\qquad \kappa p_3 - \Lambda = -\tfrac{13}{9}H^2 + 6H^2k,\qquad \kappa p_0 - \Lambda = \kappa p_t - \Lambda = -\tfrac{11}{3}H^2 + 3H^2k
$$

(record `a4-equations.json`, key `exponentialHistory`, entry `authorWeights`, sub-entry `einsteinHistorySource_kappaT_minus_Lam`; the same as `Revision/metric_warped/results/warped-metric.json`, key `history_source`, entry `einstein_A1_beta43`). With the author's weights $\alpha_k = w_k/H^{2k}$, $w = (1, \frac1{32}, \frac1{1152})$ (Section 11.11), every term $\alpha_kE_{(k)}$ is a pure number: the three rows of the table are added with the factors $1$, $\frac1{32}$ and $\frac1{1152}$, and

$$
\begin{aligned}
-\kappa\rho - \Lambda &= \tfrac{121}{432} + \tfrac{161}{24}k - \tfrac9{16}k^2,\qquad \kappa p_3 - \Lambda = -\tfrac{5359}{3888} + \tfrac{1601}{216}k - \tfrac9{16}k^2,\\
\kappa p_0 - \Lambda &= \kappa p_t - \Lambda = -\tfrac{497}{144} + \tfrac{79}{16}k
\end{aligned}
$$

(record `python-a4-report.json`, check `author_weights_history_source`; Notebook 11c, In [8], reproduces both sources exactly). For example the block entry: $-\frac{11}{3} + \frac1{32}\cdot\frac{212}{27} - \frac1{1152}\cdot\frac{104}{3} = \frac{-1584 + 106 - 13}{432} = -\frac{1491}{432} = -\frac{497}{144}$ for the part without $k$, and $3 + \frac1{32}\cdot\frac{184}{3} + \frac1{1152}\cdot 24 = 3 + \frac{23}{12} + \frac1{48} = \frac{237}{48} = \frac{79}{16}$ for the coefficient of $k$. The source is diagonal, has $p_0 = p_t$ and grows with $k$. The history is therefore not a solution of the vacuum equations, and the record uses it as a PRESCRIBED background: it does not solve for the history, it prescribes it (`a4-equations.json`, key `exponentialHistory`, entry `authorWeights`, sub-entries `statement` and `vacuum`: no exponential history is a vacuum solution for the author's weights; Chapter 12). As dated history: with these weights the author's notebook `Dirac_Einstein-Lovelock_4+4_Nash.nb` found $a_4 = Hx_4$, $b_4 = 1$ as a vacuum solution of the metric of 2026-10-14, withdrawn on 2026-10-16 (`Revision/metric_b4/METRIC_CHANGE_PROVENANCE.md`, section 2).

**The Lovelock scalars along the history of the record.** From the record (keys `L1` to `L3` of `lovelock-tensors.json`), in units of $H^{2k}$ (Notebook 11c, In [7]):

$$
L_{(1)} = \tfrac{112}{9} - 24k = -\tfrac89(27k - 14),\qquad L_{(2)} = \tfrac{32}{27}\big(81k^2 - 702k - 58\big),\qquad L_{(3)} = \tfrac{256}{9}\big(243k^2 + 99k + 22\big) .
$$

At $x_4 = 0$ ($k = 1$) they are $-\frac{104}{9}$, $-\frac{21728}{27}$ and $\frac{93184}{9}$. $L_{(1)}$ vanishes exactly at $k = \frac{14}{27}$, that is at $Hx_4 = \frac32\ln\frac{14}{27} \approx -0.985$ (divide by $-\frac89$; then $k = e^{2Hx_4/3}$ gives $Hx_4 = \frac32\ln k$). For $L_{(2)}$ the quadratic $81k^2 - 702k - 58 = 0$ has the roots

$$
k = \frac{702 \pm\sqrt{702^2 + 4\cdot 81\cdot 58}}{2\cdot 81} = \frac{702 \pm\sqrt{511596}}{162} = \frac{39 \pm\sqrt{1579}}{9}
$$

(the formula for the roots of a quadratic; $511596 = 4\cdot 81\cdot 1579$, so $\sqrt{511596} = 18\sqrt{1579}$, and numerator and denominator divided by 18); only the plus sign gives $k > 0$, $k = (39 + \sqrt{1579})/9 \approx 8.7485$, at $Hx_4 \approx 3.253$ (COMPUTED with 15 digits by Notebook 11c, In [7]). $L_{(3)}$ has only positive coefficients, so it is positive for every $k > 0$ and never vanishes on the history. Figure 11c.2 draws the three scalars with their zeros.

**An illustrative test history (ILLUSTRATION, not a solution of any equation).** On the histories of the record $a_4'' = v = 0$, so they cannot show where the second derivatives enter. Notebook 11c therefore also uses a test history in which the block deflates at all times and the deflation speeds up, with the record's ratio $b_4 = e^{(4/3)a_4}$:

$$
a_4(x_4) = Hx_4 + \tfrac12\ln\cosh(Hx_4),\qquad b_4 = e^{(4/3)a_4} .
$$

Its derivatives, line by line:

$$
a_4' = H + \tfrac12\cdot\frac{\sinh(Hx_4)}{\cosh(Hx_4)}\cdot H = H\big(1 + \tfrac12\tanh(Hx_4)\big)
$$

(the derivative of $\ln w$ is $w'/w$, the derivative of $\cosh t$ is $\sinh t$, and the chain rule gives the factor $H$; $\sinh/\cosh = \tanh$),

$$
a_4'' = \tfrac12H\cdot\frac{H}{\cosh^2(Hx_4)} = \frac{H^2}{2}\,\mathrm{sech}^2(Hx_4)
$$

(the derivative of $\tanh t$ is $1/\cosh^2t = \mathrm{sech}^2t$, and the chain rule again), and from $\ln b_4 = \frac43a_4$: $u = \frac43a_4'$, $v = \frac43a_4''$, and $k = e^{2a_4}/b_4 = e^{(2/3)a_4}$. Since $-1 < \tanh < 1$, $a_4'$ lies between $H/2$ and $3H/2$, and the scale factor $e^{-a_4}b_4^{1/2} = e^{-a_4/3}$ of the block always shrinks, slowly in the far past and three times faster in the far future. The second derivatives are bumps of height $H^2/2$ and $\frac23H^2$ at $x_4 = 0$ ($\mathrm{sech}\,0 = 1$). Figure 11c.3 draws the history (Notebook 11c, In [9]). Along it the components behave as Section 11.21 says (Figure 11c.4, In [10]): the second derivatives contribute a bump to the space and block components and exactly nothing to the time component. At $x_4 = 0$, for example, $a_4' = H$, $u = \frac43H$ and $k = 1$ as on the history of the record, while $a_4'' = \frac12H^2$ and $v = \frac23H^2$; the space component of $E_{(1)}$ moves by $2a_4'' - 2v = 1 - \frac43 = -\frac13$ (units $H^2$) and the block component by $-\frac32v = -1$, the values of the bottom row of Figure 11c.4 at $x_4 = 0$. Finally Notebook 11c checks identity (I) along this history with a finite-difference derivative, $f'(t) \approx (f(t + \epsilon) - f(t - \epsilon))/(2\epsilon)$ with $\epsilon = 0.01$, whose error is of the size $\epsilon^2/6$ times the third derivative of the time component; the largest relative deviations are $1.7 \times 10^{-5}$, $6.8 \times 10^{-5}$ and $6.5 \times 10^{-5}$ for $k = 1, 2, 3$ (COMPUTED, In [11], Figure 11c.5), the size of this error, while the exact identity holds without any error (In [5]).

**What the deflation does and does not decide (honesty).** The Lovelock tensors are the gravitational side of the field equations. They are the same for $(a_4', u)$ and $(-a_4', -u)$: whether the block deflates is not decided by them but by the source and the initial data (Chapter 12). This symmetry is a property of the metric's geometry; it is NOT the pairing of universes of masses $+m$ and $-m$ of Chapters 18 to 20, and nothing in this chapter says anything about the creation of universes or about matter and antimatter.

### 11.24 Example: the components and identities along the deflating history

Notebook 11c reads the exact components of the three Lovelock tensors from the Revision record `lovelock-tensors.json`, for the corrected metric with general functions $a_4$ and $b_4$, forms the normalised tensors $E_{(k)}$, checks that every off-diagonal component vanishes (the components $x_4$-$x_0$ and $x_0$-$x_4$ included) and that the diagonal components are those recorded for the field equations of $a_4$ and $b_4$ (`Revision/field_equations_a4/a4-equations.json`) and by the Revision's independent sympy verification; proves with sympy the structure of Section 11.21 (the time component free of second derivatives, the linearity in $a_4''$ and $v$ with the recorded coefficient matrix, the degrees in $k$, the reversal of the time, the weight $2k$) and the two identities of Section 11.22; draws the components on the histories of the record as functions of the slope $A$ and along the history of the record against the time, and the three Lovelock scalars with their zeros; reproduces the source that the history needs, for Einstein gravity and for the author's weights; and uses the illustrative test history to show where $a_4''$ and $v$ enter and to check identity (I) numerically. It quotes the reports of the field equations only by the names of their checks, never by their numbers of checks, so that it stays valid when these reports gain checks. It needs no Rust, takes about 20 seconds (17.2 seconds, including the start of the kernel, when it was built on 2026-10-18; provenance file `Revision/textbook/notebooks/11c_lovelock_components.PROVENANCE.md`), prints 22 PASS lines, draws five figures and ends with the line ALL 22 CHECKS PASSED (notebook 11c).

<!-- NOTEBOOK 11c -->

### 11.27 Line-by-line walk-through of Notebook 11c

The notebook has 13 code cells, In [1] to In [13]. As in Sections 11.9 and 11.19, every line or small group of lines is quoted and explained; docstrings are left out where the explanation repeats them, and long captions are shortened to `...` (they are printed in full under the figures in Section 11.26).

**In [1], the set-up cell.** It is the set-up cell of Notebook 11a, explained line by line in Section 11.9 under In [1], with three differences: its comment lines are the run instructions of Notebook 11c (Section 11.25); its line `NOTEBOOK_ID = "11c"  # this notebook: chapter 11, example c` names this notebook; and, because this notebook runs no Rust program, the two lines `import shutil` and `import subprocess` and the helper `rust_program` are absent. It prints Set-up of notebook 11c complete: repository folder found, helpers defined.

**In [2], the components from the Revision record.**

```python
import re  # regular expressions: rewrites the record's names

import numpy as np  # arrays of numbers
import sympy as sp  # exact algebra

H, A1, A2, U, V = sp.symbols("H A1 A2 U V")  # H, a4', a4'', u = b4'/b4, v = u'
K = sp.Symbol("K", positive=True)  # k = e^(2 a4)/b4 > 0
NAMES = ["x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7"]
tensors = json.loads(repository_file(
    "Revision/gkd_lovelock/results/lovelock-tensors.json").read_text(encoding="utf-8"))
```

`re` (regular expressions, used in In [7] to rewrite the record's formulas), numpy and sympy are loaded; five sympy symbols stand for $H$, $a_4'$, $a_4''$, $u$ and $v$, and the positive symbol `K` for $k = e^{2a_4}/b_4$; `NAMES` lists the coordinate names in the author's order; and the Rust record of the Lovelock tensors is read as JSON (Section 11.9 explains `repository_file`, `read_text` and `json.loads`).

```python
def from_monomials(monomials):
    total = sp.Integer(0)
    for numerator, denominator, e in monomials:
        if any(e[i] for i in (3, 4, 6, 7, 11, 12, 13)):
            raise ValueError("the component contains a third or fourth "
                             "derivative, W, cot z or sgn(cot z)")
        if e[5] % 2 or e[5] + e[8] + 2 * e[9] + 2 * e[10] != 0:
            raise ValueError("the powers of b4 do not cancel")
        total += (sp.Rational(numerator, denominator) * H ** e[0] * A1 ** e[1]
                  * A2 ** e[2] * K ** (e[5] // 2) * U ** e[9] * (V + U ** 2) ** e[10])
    return sp.expand(total)
```

A component of the record is a list of monomials, each a numerator, a denominator and the fourteen exponents of the symbols of Section 11.12 (in the order $H$, $a_4'$, $a_4''$, $a_4'''$, $a_4''''$, $E = e^{a_4}$, $W$, $C$, $Q = b_4^{1/2}$, $b_4'$, $b_4''$, $b_4'''$, $b_4''''$, $G$). The function (docstring left out) rebuilds the component as a sympy expression in the six variables, exactly as `from_monomials` of Notebook 11b (Section 11.19, In [15]) does with its own polynomials: it stops if a monomial contains a third or fourth derivative, $W$, $\cot z$ or the sign of $\cot z$, and if the powers of $b_4$ do not cancel; otherwise each monomial is the exact fraction (`sp.Rational`) times $H^{e_0}a_4'^{e_1}a_4''^{e_2}k^{e_5/2}u^{e_9}(v + u^2)^{e_{10}}$. Since the notebook does not stop, every component is a polynomial in the six variables, free of $x_0$ (Section 11.20).

```python
P = {k: {(h, j): from_monomials(tensors[f"P{k}_mixed_up_h_down_j"][f"{a},{b}"]
                                ["monomials"])
         for h, a in enumerate(NAMES) for j, b in enumerate(NAMES)}
     for k in (1, 2, 3)}
E = {k: {hj: sp.expand(-value / 2 ** (k + 1)) for hj, value in P[k].items()}
     for k in (1, 2, 3)}
```

`P[k][h, j]` is the component $P_{(k)}{}^h{}_j$, built for all 64 pairs (`enumerate(NAMES)` gives each number with its name, used for the record's keys such as `"x1,x1"`), and `E[k][h, j]` the normalised component $E_{(k)} = -P_{(k)}/2^{k+1}$, multiplied out.

```python
check(all(E[k][h, j] == 0 for k in (1, 2, 3) for h in range(8) for j in range(8)
          if h != j),
      "every off-diagonal component of E(1), E(2), E(3) is zero, x4-x0 included, "
      "for general a4 and b4",
      record="Revision/gkd_lovelock/results/lovelock-report.json, checks "
             "k1_offdiagonal_vanishes to k3_offdiagonal_vanishes")
check(all(E[k][1, 1] == E[k][2, 2] == E[k][3, 3]
          and E[k][0, 0] == E[k][5, 5] == E[k][6, 6] == E[k][7, 7]
          for k in (1, 2, 3)),
      "x1 = x2 = x3 and x0 = x5 = x6 = x7 for every order",
      record="Revision/gkd_lovelock/results/lovelock-report.json, checks "
             "k1_hidden_equals_extra_times to k3_hidden_equals_extra_times")
```

Two checks: every off-diagonal component of the three tensors is zero, the components $x_4$-$x_0$ and $x_0$-$x_4$ included, for general $a_4$ and $b_4$ (Section 11.21 (a)); and the three space components are equal, and so are the hidden component and the three extra-time components (Section 11.21 (b)). PASS lines one and two.

```python
for k in (1, 2, 3):
    for h in (1, 4, 0):  # x1, x4, x0
        say(f"E({k})^{NAMES[h]}_{NAMES[h]} = {E[k][h, h]}")
```

The three independent components of each order are printed: nine lines that are exactly the list of Section 11.20 (sympy writes `A1**2` for $a_4'^2$ and `H**2*K` for $H^2k$).

**In [3], against the other records.**

```python
a4_record = json.loads(repository_file(
    "Revision/field_equations_a4/a4-equations.json").read_text(encoding="utf-8"))
RECORD_NAMES = {"ad1": A1, "ad2": A2, "uu": U, "vv": V, "kk": K, "H": H}
def from_text(text, names=RECORD_NAMES):
    return sp.sympify(text.replace("^", "**"), locals=names)
```

The record of the field equations is read. Its formulas use the names `ad1`, `ad2`, `uu`, `vv`, `kk` for $a_4'$, $a_4''$, $u$, $v$, $k$ (its key `conventions`, entry `symbols`); `from_text` (docstring left out) reads such a formula as a sympy expression with these names, after `^` has been replaced by `**`.

```python
same = all(sp.expand(from_text(a4_record["lovelockTensors"][f"E{k}"][key]["input"])
                     - E[k][h, h]) == 0
           for k in (1, 2, 3)
           for key, h in (("x0x0", 0), ("x1x1", 1), ("x4x4", 4), ("x5x5", 5)))
check(same, "E(1), E(2), E(3) equal the components recorded for the a4 and b4 "
      "equations",
      record="Revision/field_equations_a4/reports/python-a4-report.json, check "
             "json_lovelock_components")
```

The record lists the normalised components under the key `lovelockTensors`, for each order the four components $x_0x_0$, $x_1x_1$, $x_4x_4$ and $x_5x_5$ (entry `input`). All twelve must equal the components of In [2]. Third PASS line: the field equations of Chapter 12 use exactly these tensors.

```python
checker = json.loads(repository_file(
    "Revision/gkd_lovelock/results/python-lovelock-report.json").read_text(
        encoding="utf-8"))
independent = checker["independentResults"]
B0, B1, B2, EA = sp.symbols("B0 B1 B2 EA", positive=True)
CHECKER_NAMES = {"A1": A1, "A2": A2, "H": H, "B0": B0, "B1": B1, "B2": B2, "E": EA}
IN_SIX = {B1: U * B0, B2: (V + U ** 2) * B0, EA: sp.sqrt(K * B0)}
```

The Revision's independent sympy checker stores its own results under `independentResults`, written with the names `B0`, `B1`, `B2` for $b_4$, $b_4'$, $b_4''$ and `E` for $e^{a_4}$. `IN_SIX` translates them into the six variables: $b_4' = ub_4$, $b_4'' = (v + u^2)b_4$ and $e^{a_4} = \sqrt{kb_4}$.

```python
same = all(
    sp.expand(from_text(text, CHECKER_NAMES).subs(IN_SIX)
              - P[k][NAMES.index(key.split(",")[0]), NAMES.index(key.split(",")[1])])
    == 0
    for k in (1, 2, 3) for key, text in independent[f"P{k}_mixed_nonzero"].items())
check(same and all(len(independent[f"P{k}_mixed_nonzero"]) == 8 for k in (1, 2, 3)),
      "P(1), P(2), P(3) equal the independent sympy results (8 nonzero components "
      "each)",
      record="Revision/gkd_lovelock/results/python-lovelock-report.json, "
             "independentResults")
```

Each of the checker's components, keyed like `"x1,x1"` (`key.split(",")` gives the two names), translated and compared with the component of the Rust record; the checker must list exactly the eight nonzero components for each order. Fourth PASS line: two programs that share no code give the same tensors.

**In [4], the structure.**

```python
s = sp.Symbol("s")  # the scaling number of item 5
alphas = sp.symbols("alpha1 alpha2 alpha3")  # the constants of the field equations
recorded_J = sp.Matrix(from_text(
    a4_record["generalSource"]["secondOrderJacobian"]["input"].replace("{", "[")
    .replace("}", "]"), {**RECORD_NAMES, "alpha1": alphas[0], "alpha2": alphas[1],
                         "alpha3": alphas[2]}))
J = sp.zeros(2, 2)  # sum_k alpha_k J_(k)
structure = {name: True for name in ("constraint", "linear", "k", "even", "weight")}
```

`s` is the scaling number of the weight test below, and `alphas` the three constants $\alpha_1, \alpha_2, \alpha_3$ of the field equations. `recorded_J` is the record's coefficient matrix of the second derivatives (key `generalSource`, entry `secondOrderJacobian`), written in Mathematica's braces, which are replaced by brackets so that sympy reads a list of lists; `sp.Matrix` makes it a matrix. `J` will be the same matrix computed here, and `structure` collects five yes-or-no results, all starting as `True`.

```python
for k in (1, 2, 3):
    e = E[k]
    structure["constraint"] &= not e[4, 4].has(A2) and not e[4, 4].has(V)
    structure["linear"] &= all(sp.Poly(e[h, h], A2, V).total_degree() <= 1
                               for h in (1, 0))
```

For each order: the time component `e[4, 4]` must contain neither $a_4''$ nor $v$ (`.has`), Section 11.21 (d); and the space and block components must have total degree at most 1 in the pair $(a_4'', v)$, Section 11.21 (c). (`&=` keeps `True` only if the new test is also true.)

```python
    J += alphas[k - 1] * sp.Matrix([[sp.diff(e[1, 1], A2), sp.diff(e[1, 1], V)],
                                    [sp.diff(e[0, 0], A2), sp.diff(e[0, 0], V)]])
```

The coefficients of $a_4''$ and $v$ in the space component (first row) and the block component (second row) are the derivatives with respect to `A2` and `V`; each order adds its matrix times $\alpha_k$.

```python
    degrees = [sp.degree(e[h, h], K) for h in (1, 4, 0)]  # x1, x4, x0
    structure["k"] &= degrees[2] <= 1 and max(degrees) <= 2
```

The degrees in $k$ of the three components (space, time, block): the block component must be at most linear in $k$ and every component at most quadratic, Section 11.21 (f).

```python
    structure["even"] &= all(sp.expand(e[h, h].subs({A1: -A1, U: -U}, simultaneous=True)
                                       - e[h, h]) == 0 for h in range(8))
```

Every diagonal component must be unchanged when $a_4'$ and $u$ change sign together (`simultaneous=True` makes both replacements at once), Section 11.21 (g).

```python
    scaled = {H: s * H, A1: s * A1, U: s * U, A2: s ** 2 * A2, V: s ** 2 * V}
    structure["weight"] &= all(
        sp.expand(e[h, h].subs(scaled, simultaneous=True) - s ** (2 * k) * e[h, h])
        == 0 for h in range(8))
    report(f"degrees of E({k}) in k (x1, x4, x0)", degrees)
```

The weight test of Section 11.21 (h): replacing $H, a_4', u$ by $sH, sa_4', su$ and $a_4'', v$ by $s^2a_4'', s^2v$ must multiply every component of $E_{(k)}$ by $s^{2k}$. The degrees are printed: $[1, 1, 1]$, $[2, 2, 1]$ and $[2, 2, 1]$ for $k = 1, 2, 3$.

```python
report("coefficient matrix of Einstein's tensor (k = 1)",
       J.subs({alphas[0]: 1, alphas[1]: 0, alphas[2]: 0}).tolist())
```

The matrix of Einstein's tensor alone ($\alpha_1 = 1$, $\alpha_2 = \alpha_3 = 0$) is printed: `[[2, -2], [0, -3/2]]`, the matrix of Section 11.21 (e).

```python
check(structure["constraint"], "the x4 component contains no a4'' and no v",
      record="Revision/field_equations_a4/reports/python-a4-report.json, check "
             "constraint_first_order")
check(structure["linear"] and sp.expand(J - recorded_J) == sp.zeros(2, 2),
      "the x1 and x0 components are linear in (a4'', v), with the coefficient matrix "
      "of the record",
      record="Revision/field_equations_a4/reports/python-a4-report.json, check "
             "second_order_system (a4-equations.json, secondOrderJacobian)")
check(structure["k"], "the hidden component is at most linear in k, the space and "
      "time components at most quadratic")
check(structure["even"], "every component is unchanged under (a4', u) -> (-a4', -u), "
      "the reversal of the time")
check(structure["weight"], "every component of E(k) has the weight 2k (dimension "
      "1/length^(2k))")
```

Five checks: the constraint (the time component has no second derivative), the linearity together with the record's matrix (`J - recorded_J` must be the zero matrix, for any $\alpha_k$), the powers of $k$, the reversal of the time, and the weight. PASS lines five to nine.

**In [5], the two conservation identities.**

```python
rate = U / 2 - A1  # h4 = u/2 - a4', the rate of the block
```

`rate` is the rate $h_4 = \frac12u - a_4'$ of the block (Section 11.10).

```python
def d_dx4(expr):
    return sp.expand(sp.diff(expr, A1) * A2 + sp.diff(expr, U) * V
                     + sp.diff(expr, K) * K * (2 * A1 - U))
```

`d_dx4` (docstring left out) differentiates a function of $a_4'$, $u$ and $k$ along the time by the chain rule of Section 11.22: the derivative of $a_4'$ is $a_4''$, that of $u$ is $v$, and that of $k$ is $k(2a_4' - u)$. It is applied only to the time component, which depends on nothing else.

```python
def balance(k):
    e = E[k]
    return sp.expand(3 * A1 * (e[1, 1] - e[4, 4]) + 4 * rate * (e[0, 0] - e[4, 4]))
```

`balance(k)` (docstring left out) is the right side of identity (I): $3a_4'(E^{x_1}{}_{x_1} - E^{x_4}{}_{x_4}) + 4h_4(E^{x_0}{}_{x_0} - E^{x_4}{}_{x_4})$.

```python
say(f"order 1: d/dx4 E^x4_x4 = {d_dx4(E[1][4, 4])}")
say(f"         right side of (I) = {balance(1)}")
```

For Einstein's tensor both sides are printed: `6*A1*A2 + 12*A1*H**2*K - 6*H**2*K*U - 3*U*V` twice, the result of the hand computation of Section 11.22.

```python
check(all(sp.expand(d_dx4(E[k][4, 4]) - balance(k)) == 0 for k in (1, 2, 3)),
      "d/dx4 E^x4_x4 = 3 a4' (E^x1_x1 - E^x4_x4) + 4 h4 (E^x0_x0 - E^x4_x4) with "
      "h4 = u/2 - a4', for k = 1, 2, 3 (identity I)",
      record="Revision/field_equations_a4/reports/python-a4-report.json, check "
             "bianchi_x4; Revision/gkd_lovelock/results/lovelock-report.json, checks "
             "k1_divergence_free, k2_divergence_free and k3_divergence_free")
check(all(sp.expand(E[k][0, 0] - E[k][5, 5]) == 0 for k in (1, 2, 3)),
      "E^x0_x0 = E^x5_x5 for k = 1, 2, 3 (identity II)",
      record="Revision/field_equations_a4/a4-equations.json, generalSource "
             "hiddenEqualsExtraTimes")
```

Two checks: identity (I) holds exactly for $k = 1, 2, 3$, and identity (II), $E^{x_0}{}_{x_0} = E^{x_5}{}_{x_5}$, holds for every order. PASS lines ten and eleven.

**In [6], the histories of the record (Figure 11c.1).**

```python
A, t = sp.symbols("A t")  # the slope A and the time t = H x4
FAMILY = {H: 1, A1: A, A2: 0, U: sp.Rational(4, 3) * A, V: 0}
ON_FAMILY = {k: {h: sp.expand(E[k][h, h].subs(FAMILY)) for h in (4, 1, 0)}
             for k in (1, 2, 3)}
for k in (1, 2, 3):
    say(f"E({k}): x4: {ON_FAMILY[k][4]};  x1: {ON_FAMILY[k][1]};  "
        f"x0: {ON_FAMILY[k][0]}")
```

`A` is the slope and `t` the time $Hx_4$. `FAMILY` inserts the histories $a_4 = AHx_4$, $b_4 = b_4(0)\,e^{(4/3)AHx_4}$ with $H = 1$: $a_4' = A$, $a_4'' = 0$, $u = \frac43A$, $v = 0$, while $k$ stays free. The nine components on these histories are printed; they are the table of Section 11.20, for example `E(1): x4: A**2/3 + 6*K;  x1: -13*A**2/9 + 6*K;  x0: -11*A**2/3 + 3*K`.

```python
slopes = np.linspace(-2.0, 2.0, 401)
times = np.linspace(-3.0, 3.0, 601)
STYLES = ((4, "-", "$E^{x_4}{}_{x_4}$ (time)"), (1, "--", "$E^{x_1}{}_{x_1}$ (space)"),
          (0, ":", "$E^{x_0}{}_{x_0} = E^{x_5}{}_{x_5}$ (block)"))
fig, axes = plt.subplots(2, 3, figsize=(12.6, 7.6))
symmetric = True
```

401 slopes from $-2$ to 2 and 601 times from $-3$ to 3; `STYLES` gives each component a line style and a legend text; six panels in two rows.

```python
for column, k in enumerate((1, 2, 3)):
    for h, style, label in STYLES:
        at_moment = sp.lambdify(A, ON_FAMILY[k][h].subs(K, 1), "numpy")
        values = np.broadcast_to(at_moment(slopes), slopes.shape).astype(float)
        symmetric &= np.allclose(values, values[::-1])
        axes[0, column].plot(slopes, values, style, label=label)
        along = sp.lambdify(t, ON_FAMILY[k][h].subs({A: 1, K: sp.exp(2 * t / 3)}),
                            "numpy")
        axes[1, column].plot(times, np.broadcast_to(along(times), times.shape),
                             style, label=label)
```

For each order and component: the top panel draws the component against the slope at $k = 1$ (`sp.lambdify` turns the formula into a numpy function, and `np.broadcast_to` makes an array even of a constant), and the test `np.allclose(values, values[::-1])` compares the curve with its mirror image (`[::-1]` reverses the array); the bottom panel draws it along the history of the record, $A = 1$ and $k = e^{2t/3}$.

```python
    axes[0, column].set_xlabel("slope $A = a_4^{\\prime}/H$ (at $k = 1$)")
    axes[1, column].set_xlabel("time $H x_4$ on the history of the record")
    axes[0, column].set_title(f"order k = {k}")
    for row in (0, 1):
        axes[row, column].axhline(0.0, color="0.5", lw=0.8)
        axes[row, column].set_ylabel(f"$E_{{({k})}}$ in units of $H^{{{2 * k}}}$")
        axes[row, column].legend(fontsize=7, loc="best")
fig.tight_layout()
save_figure(fig, "components_linear_history",
            "The normalised Lovelock tensors $E_{(1)}$ (Einstein), $E_{(2)}$ and "
            ...)
```

Axis titles, a grey zero line, legends, and the saved figure.

```python
check(symmetric, "on the histories every curve is symmetric under A -> -A")
```

Twelfth PASS line: every curve is symmetric under $A \to -A$.

*What Figure 11c.1 shows.* Top row: the components against the slope $A$ at $k = 1$, each curve a mirror image of itself about $A = 0$. For $E_{(1)}$ the time component stays positive (6 at $A = 0$, rising like $\frac13A^2$), the space component falls from 6, and the block component from 3, below 0 for $|A| > 0.9$. For $E_{(2)}$ time and space start at $-12$ and the block at 0; for $E_{(3)}$ all three start at 0. Bottom row: along the history of the record every component of $E_{(1)}$ grows with $k = e^{2Hx_4/3}$; in $E_{(2)}$ the block component grows, while the time component and, later, the space component turn negative and fall steeply; in $E_{(3)}$ time and space fall steeply from the start, and the block component stays small.

**In [7], the Lovelock scalars (Figure 11c.2).**

```python
def from_mathematica(text):
    text = re.sub(r"Derivative\[(\d)\]\[a4\]\[x4\]", r"A\1", text)  # a4' -> A1
    text = text.replace("Derivative[1][b4][x4]", "(U*B0)")  # b4' = u b4
    text = text.replace("Derivative[2][b4][x4]", "((V + U**2)*B0)")  # b4''
    text = text.replace("b4[x4]", "B0")  # b4
    text = re.sub(r"E\^\((-?\d+)\*a4\[x4\]\)", r"(K*B0)**(\1/2)", text)  # e^(n a4)
    return sp.expand(from_text(text, {"H": H, "A1": A1, "A2": A2, "U": U, "V": V,
                                      "K": K, "B0": B0}))
```

`from_mathematica` (docstring left out) reads a formula of `lovelock-tensors.json`, as the function of the same name in Notebook 11b (Section 11.19, In [8]), here with `B0` for $b_4$.

```python
L = {k: from_mathematica(tensors[f"L{k}"]) for k in (1, 2, 3)}
L_HISTORY = {k: sp.expand(L[k].subs(FAMILY).subs(A, 1)) for k in (1, 2, 3)}
scalar_times = np.linspace(-3.0, 4.0, 701)  # H x4 from -3 to 4
fig, axes = plt.subplots(1, 3, figsize=(12.0, 3.8))
zeros = {}
```

The three scalars of the record, the scalars on the history of the record ($A = 1$), polynomials in $k$, and 701 times from $-3$ to 4.

```python
for ax, k in zip(axes, (1, 2, 3)):
    roots = sp.Poly(L_HISTORY[k], K).nroots(n=15)  # every root, numerically
    zeros[k] = [float(r) for r in roots if r.is_real and r > 0]
    moments = [1.5 * np.log(r) for r in zeros[k]]  # H x4 = (3/2) ln k0
    say(f"L({k}) on the history = {sp.factor(L_HISTORY[k])}")
    report(f"positive zeros of L({k}) on the history: k, H x4",
           ", ".join(f"{r:.6f}, {m:.4f}" for r, m in zip(zeros[k], moments))
           or "none")
```

`sp.Poly(..., K).nroots(n=15)` finds every root of the polynomial in $k$ numerically with 15 digits; the real positive ones are kept, and each becomes a moment $Hx_4 = \frac32\ln k$ (from $k = e^{2Hx_4/3}$). The output: `L(1) on the history = -8*(27*K - 14)/9` with the zero at $k = 0.518519$, $Hx_4 = -0.9852$; `L(2) on the history = 32*(81*K**2 - 702*K - 58)/27` with the zero at $k = 8.748515$, $Hx_4 = 3.2533$; and `L(3) on the history = 256*(243*K**2 + 99*K + 22)/9` with no zero (the empty string and `or "none"` print none).

```python
    along = sp.lambdify(t, L_HISTORY[k].subs(K, sp.exp(2 * t / 3)), "numpy")
    ax.plot(scalar_times, along(scalar_times), color="tab:green")
    for m in moments:
        ax.plot([m], [0.0], "o", color="black", markersize=4)
    ax.axhline(0.0, color="0.5", lw=0.8)
    ax.axvline(0.0, color="0.5", lw=0.8)
    ax.set_xlabel("time $H x_4$ on the history of the record")
    ax.set_ylabel(f"$L_{{({k})}}$ in units of $H^{{{2 * k}}}$")
    ax.set_title(f"Lovelock scalar of order {k}")
fig.tight_layout()
save_figure(fig, "lovelock_scalars",
            "The Lovelock scalars $L_{(1)} = 2R$, $L_{(2)}$ and $L_{(3)}$ of the "
            ...)
```

Each scalar along the time, black dots at its zeros, grey lines through 0, and the saved figure.

```python
check(len(zeros[1]) == 1 and abs(zeros[1][0] - 14 / 27) < 1e-12
      and len(zeros[2]) == 1 and zeros[3] == []
      and [L_HISTORY[k].subs(K, 1) for k in (1, 2, 3)]
      == [sp.Rational(-104, 9), sp.Rational(-21728, 27), sp.Rational(93184, 9)],
      "on the history L(1) vanishes at k = 14/27, L(2) at one positive k, L(3) "
      "never; at x4 = 0 the scalars are -104/9, -21728/27, 93184/9")
```

The check requires one zero of $L_{(1)}$, at $k = \frac{14}{27}$ (within $10^{-12}$), one positive zero of $L_{(2)}$, none of $L_{(3)}$, and the exact values at $x_4 = 0$. Thirteenth PASS line.

*What Figure 11c.2 shows.* Three curves against $Hx_4$ from $-3$ to 4. $L_{(1)}$ falls from small positive values through its zero at $Hx_4 \approx -0.99$ to about $-330$; $L_{(2)}$ is negative, has a minimum of about $-1900$ near $Hx_4 \approx 2.2$, and crosses zero at $Hx_4 \approx 3.25$; $L_{(3)}$ is positive everywhere and grows to about $1.5 \times 10^6$.

**In [8], the source that the history needs.**

```python
weights = {"Einstein": (1, 0, 0),
           "author": (1, sp.Rational(1, 32), sp.Rational(1, 1152))}
record_sources = a4_record["exponentialHistory"]["authorWeights"]
keys = {"Einstein": "einsteinHistorySource_kappaT_minus_Lam",
        "author": "historySource_kappaT_minus_Lam"}
agree = {}
```

Two sets of weights: Einstein gravity ($\alpha_1 = 1$, $\alpha_2 = \alpha_3 = 0$) and the author's pure numbers $w = (1, \frac1{32}, \frac1{1152})$; the two recorded sources and their names in the record.

```python
for name, w in weights.items():
    source = {h: sp.expand(sum(w[k - 1] * ON_FAMILY[k][h] for k in (1, 2, 3))
                           .subs(A, 1)) for h in (4, 1, 0)}
    say(f"{name}: -kappa rho - Lambda = {source[4]};  kappa p3 - Lambda = "
        f"{source[1]};  kappa p0 - Lambda = kappa pt - Lambda = {source[0]}")
```

For each set, the three components of $\sum_kw_kE_{(k)}$ on the history of the record ($A = 1$) are formed and printed as $-\kappa\rho - \Lambda$, $\kappa p_3 - \Lambda$ and $\kappa p_0 - \Lambda = \kappa p_t - \Lambda$ (the field equations of Section 11.22). The output: `6*K + 1/3`, `6*K - 13/9`, `3*K - 11/3` for Einstein and `-9*K**2/16 + 161*K/24 + 121/432`, `-9*K**2/16 + 1601*K/216 - 5359/3888`, `79*K/16 - 497/144` for the author's weights, the sources of Section 11.23.

```python
    recorded = record_sources[keys[name]]
    agree[name] = all(
        sp.expand(from_text(recorded[entry]["input"]).subs(H, 1) - source[h]) == 0
        for entry, h in (("minus_rho", 4), ("p3", 1), ("p0", 0), ("pt", 0)))
check(agree["Einstein"], "Einstein gravity: the source of the history equals the "
      "record",
      record="Revision/field_equations_a4/a4-equations.json, exponentialHistory, "
             "authorWeights, einsteinHistorySource_kappaT_minus_Lam")
check(agree["author"], "the author's weights: the source of the history equals the "
      "record",
      record="Revision/field_equations_a4/reports/python-a4-report.json, check "
             "author_weights_history_source")
```

Each of the four recorded entries (`minus_rho`, `p3`, `p0`, `pt`) is read, $H = 1$ is inserted, and it must equal the computed source; the block entry serves both $p_0$ and $p_t$. Two checks, PASS lines fourteen and fifteen.

**In [9], the test history (Figure 11c.3).**

```python
history = t + sp.log(sp.cosh(t)) / 2  # a4 with H = 1 (t = H x4)
b4_history = sp.exp(sp.Rational(4, 3) * history)  # b4 = e^((4/3) a4)
first = sp.diff(history, t)  # a4'
second = sp.diff(history, t, 2)  # a4''
u_history = sp.diff(b4_history, t) / b4_history  # u = b4'/b4
k_history = sp.exp(2 * history) / b4_history  # k = e^(2 a4)/b4
```

The illustrative test history of Section 11.23 with $H = 1$: $a_4 = t + \frac12\ln\cosh t$ and $b_4 = e^{(4/3)a_4}$; sympy differentiates them and forms $u = b_4'/b_4$ and $k = e^{2a_4}/b_4$.

```python
check(sp.simplify(first - (1 + sp.tanh(t) / 2)) == 0
      and sp.simplify(second - sp.sech(t) ** 2 / 2) == 0
      and sp.simplify(u_history - sp.Rational(4, 3) * first) == 0
      and sp.simplify(k_history - sp.exp(sp.Rational(2, 3) * history)) == 0,
      "the test history has a4' = 1 + tanh/2 > 0, a4'' = sech^2/2, u = (4/3) a4' and "
      "k = e^((2/3) a4) (H = 1)")
```

The check confirms the derivatives of Section 11.23: $a_4' = 1 + \frac12\tanh t$, $a_4'' = \frac12\mathrm{sech}^2t$, $u = \frac43a_4'$ and $k = e^{(2/3)a_4}$. Sixteenth PASS line.

```python
test_times = np.linspace(-4.0, 4.0, 801)  # H x4 from -4 to 4
VALUES = {name: sp.lambdify(t, expr, "numpy")(test_times)
          for name, expr in (("a4", history), ("a1", first), ("a2", second))}
VALUES["u"] = 4 * VALUES["a1"] / 3  # u = (4/3) a4'
VALUES["v"] = 4 * VALUES["a2"] / 3  # v = (4/3) a4''
VALUES["k"] = np.exp(2 * VALUES["a4"] / 3)  # k = e^((2/3) a4)
```

801 times from $-4$ to 4 (step 0.01); the values of $a_4$, $a_4'$ and $a_4''$ at these times, computed with numpy, and from them $u$, $v = \frac43a_4''$ and $k$.

```python
fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.0))
axes[0].semilogy(test_times, np.exp(VALUES["a4"]),
                 label="space, $e^{a_4}$ (inflates)")
axes[0].semilogy(test_times, np.exp(-VALUES["a4"] / 3), "--",
                 label="block, $e^{-a_4} b_4^{1/2} = e^{-a_4/3}$ (deflates)")
axes[0].set_xlabel("time $H x_4$")
axes[0].set_ylabel("scale factor (logarithmic scale)")
axes[0].set_title("scale factors of the test history")
axes[0].legend(fontsize=8)
for name, style, label in (("a1", "-", "$a_4^{\\prime}/H$"), ("u", "-.", "$u/H$"),
                           ("a2", "--", "$a_4^{\\prime\\prime}/H^2$"),
                           ("v", ":", "$v/H^2$")):
    axes[1].plot(test_times, VALUES[name], style, label=label)
axes[1].set_xlabel("time $H x_4$")
axes[1].set_ylabel("value")
axes[1].set_title("its first and second derivatives")
axes[1].legend(fontsize=8)
fig.tight_layout()
save_figure(fig, "test_history",
...)
```

Left panel: the two scale factors $e^{a_4}$ and $e^{-a_4/3}$ on a logarithmic axis (`semilogy`); right panel: the four derivatives; then the saved figure.

*What Figure 11c.3 shows.* Left: on the logarithmic axis the scale factor of space rises from about 0.1 to about 300 and the scale factor of the block falls from about 2 to about 0.15; both lines bend at $x_4 = 0$, where the change speeds up. Right: $a_4'/H$ rises from $\frac12$ to $\frac32$ and $u/H$ from $\frac23$ to 2; $a_4''/H^2$ and $v/H^2$ are bumps of height $\frac12$ and $\frac23$ at $x_4 = 0$.

**In [10], the components along the test history (Figure 11c.4).**

```python
def along_history(expr, second_derivatives=True):
    function = sp.lambdify((A1, A2, U, V, K), expr.subs(H, 1), "numpy")
    a2 = VALUES["a2"] if second_derivatives else 0 * VALUES["a2"]
    v = VALUES["v"] if second_derivatives else 0 * VALUES["v"]
    values = function(VALUES["a1"], a2, VALUES["u"], v, VALUES["k"])
    return np.broadcast_to(values, test_times.shape).astype(float)
```

`along_history` (docstring left out) evaluates a component at every time of the test history; with `second_derivatives=False` it puts $a_4'' = v = 0$ and keeps $a_4'$, $u$ and $k$.

```python
fig, axes = plt.subplots(2, 3, figsize=(12.6, 7.6))
curves, parts = {}, {}
constraint_ok = True
for column, k in enumerate((1, 2, 3)):
    curves[k] = {h: along_history(E[k][h, h]) for h in (1, 4, 0)}
    parts[k] = {h: curves[k][h] - along_history(E[k][h, h], False)
                for h in (1, 4, 0)}  # what a4'' and v contribute
    constraint_ok &= not np.any(parts[k][4])  # the time component: exactly 0
```

For each order the three components are computed along the history, and `parts` keeps the difference between the full component and the component without second derivatives: the part that $a_4''$ and $v$ contribute. For the time component this part must be exactly 0 at every time (`np.any` is true if any entry is not 0).

```python
    for h, style, label in STYLES:
        axes[0, column].plot(test_times, curves[k][h], style, label=label)
        axes[1, column].plot(test_times, parts[k][h], style, label=label)
    axes[0, column].set_title(f"order k = {k}")
    axes[0, column].set_ylabel(f"$E_{{({k})}}$ in units of $H^{{{2 * k}}}$")
    axes[1, column].set_ylabel("part with $a_4''$ and $v$")
    for row in (0, 1):
        axes[row, column].set_xlabel("time $H x_4$")
        axes[row, column].legend(fontsize=7)
fig.tight_layout()
save_figure(fig, "components_test_history",
...)
```

The components (top row) and their parts with $a_4''$ and $v$ (bottom row), with titles, axis titles and legends, and the saved figure.

```python
check(constraint_ok, "along the test history the second derivatives contribute "
      "exactly 0 to the time component, for k = 1, 2, 3")
```

Seventeenth PASS line: the time component does not see the second derivatives.

*What Figure 11c.4 shows.* Top row: the components grow with $k$, those of $E_{(2)}$ and $E_{(3)}$ fast and mostly negative at late times, as on the history of the record. Bottom row: the time component's part is the flat line 0. For $E_{(1)}$ the parts of the space and block components are dips of depth $\frac13$ and 1 at $x_4 = 0$ (Section 11.23); for $E_{(2)}$ they are bumps of about 19 and 26; for $E_{(3)}$ they are dips, the space part reaching about $-290$ and dying away slowly, because its coefficients grow with $k$ while $a_4''$ and $v$ shrink.

**In [11], identity (I) numerically (Figure 11c.5).**

```python
step = test_times[1] - test_times[0]  # epsilon = 0.01
block_rate = VALUES["u"] / 2 - VALUES["a1"]  # h4 = u/2 - a4'
fig, axes = plt.subplots(1, 3, figsize=(12.0, 3.8))
worst = {}
```

The step $\epsilon = 0.01$ between neighbouring times, the rate $h_4 = \frac12u - a_4'$ at every time, three panels, and a dictionary for the largest deviations.

```python
for ax, k in zip(axes, (1, 2, 3)):
    left = np.gradient(curves[k][4], step)  # d/dx4 of the time component
    right = (3 * VALUES["a1"] * (curves[k][1] - curves[k][4])
             + 4 * block_rate * (curves[k][0] - curves[k][4]))
    inner = slice(1, -1)  # the two end points use a one-sided difference
    worst[k] = float(np.max(np.abs(left[inner] - right[inner]))
                     / np.max(np.abs(right)))
    report(f"order {k}: largest relative deviation of the finite difference",
           f"{worst[k]:.1e}")
```

`np.gradient` computes the derivative of the time component by finite differences: inside the time range the central difference $(f(t + \epsilon) - f(t - \epsilon))/(2\epsilon)$, at the two end points a one-sided difference, which is less accurate and is therefore left out (`slice(1, -1)` keeps all but the first and the last value). The right side of identity (I) is computed from the curves of In [10]. The largest difference, divided by the largest value of the right side, is printed: $1.7 \times 10^{-5}$, $6.8 \times 10^{-5}$ and $6.5 \times 10^{-5}$ for $k = 1, 2, 3$.

```python
    ax.plot(test_times, right, color="tab:blue", lw=3, alpha=0.5,
            label="right side of (I)")
    ax.plot(test_times, left, "k:",
            label="$d E^{x_4}{}_{x_4} / d x_4$ (finite difference)")
    ax.set_xlabel("time $H x_4$")
    ax.set_ylabel(f"units of $H^{{{2 * k + 1}}}$")
    ax.set_title(f"identity (I), order k = {k}")
    ax.legend(fontsize=7)
fig.tight_layout()
largest = max(worst.values())  # the largest relative deviation of the three orders
power = int(np.floor(np.log10(largest)))  # its power of ten
deviation_text = f"${largest / 10 ** power:.1f} \\times 10^{{{power}}}$"
save_figure(fig, "conservation_identity",
            "Identity (I), the conservation identity along the time, checked "
            "numerically along the illustrative test history for $k = 1, 2, 3$: the "
            "finite-difference derivative of the time component $E^{x_4}_{\\ x_4}$ "
            "(dotted black) lies on the right side $3 a_4^{\\prime} (E^{x_1}_{\\ x_1} "
            "- E^{x_4}_{\\ x_4}) + 4 h_4 (E^{x_0}_{\\ x_0} - E^{x_4}_{\\ x_4})$ with "
            "$h_4 = u/2 - a_4^{\\prime}$ (thick blue), in units of $H^{2k+1}$, against "
            "the time $H x_4$; the largest relative deviation is about "
            f"{deviation_text}, the size of the finite-difference error.")
```

The right side as a thick pale blue line and the finite difference as a black dotted line in each panel. The caption's number is built from the largest of the three deviations: `np.log10` and `np.floor` give its power of ten, and the text reads $6.8 \times 10^{-5}$.

```python
check(all(value < 1e-4 for value in worst.values()),
      "the finite-difference derivative agrees with identity (I) to 1e-4")
```

Eighteenth PASS line: the numerical derivative agrees with identity (I) to $10^{-4}$.

*What Figure 11c.5 shows.* In each panel the dotted line lies on the thick blue line over the whole time range; the two cannot be told apart, from the small values at early times to the large values at $Hx_4 = 4$ (about 260, $-42000$ and $-1.9 \times 10^6$ in units of $H^3$, $H^5$, $H^7$).

**In [12], the quoted records once more.**

```python
def verdicts(path):
    data = json.loads(repository_file(path).read_text(encoding="utf-8"))
    checks = data["checks"]
    if isinstance(checks, dict):  # name -> {"passed": true or false, ...}
        return {name: "PASS" if entry["passed"] else "FAIL"
                for name, entry in checks.items()}
    return {entry["name"]: entry["verdict"] for entry in checks}  # a list of entries
```

The helper of Notebook 11a, In [16]: for one report, a dictionary from the name of each check to PASS or FAIL (docstring left out).

```python
QUOTED = {  # report -> the checks that this notebook quotes from it
    "Revision/field_equations_a4/reports/python-a4-report.json": [
        "json_lovelock_components", "constraint_first_order", "second_order_system",
        "bianchi_x4", "independent_components", "author_weights_history_source"],
    "Revision/gkd_lovelock/results/lovelock-report.json": [
        "k1_divergence_free", "k2_divergence_free", "k3_divergence_free",
        "k1_offdiagonal_vanishes", "k2_offdiagonal_vanishes",
        "k3_offdiagonal_vanishes", "k1_hidden_equals_extra_times",
        "k2_hidden_equals_extra_times", "k3_hidden_equals_extra_times"],
}
for path, names in QUOTED.items():
    found = verdicts(path)
    missing = [name for name in names if found.get(name) != "PASS"]
    say(f"{path.split('/')[-1]}: {len(names)} quoted checks; not there or not "
        f"PASS: {missing if missing else 'none'}")
    check(not missing,
          f"the {len(names)} checks quoted from {path.split('/')[-1]} are there and "
          "PASS", record=f"{path}, checks " + ", ".join(names))
```

The 6 checks quoted from the sympy report of the field equations and the 9 quoted from the Rust report; for each report the missing or failed ones are printed ("none") and the check requires there to be none. PASS lines nineteen and twenty. The notebook quotes these reports by the names of their checks, not by their numbers of checks, so that it stays valid when a report gains checks.

```python
general = a4_record["generalSource"]  # a4-equations.json, read in section 5
stated = ("p0 = p_t" in general["hiddenEqualsExtraTimes"]
          and "for every mu != nu" in general["offDiagonal"]
          and "3 ad1 (E^x1_x1 - E^x4_x4) + 4 hh (E^x0_x0 - E^x4_x4)"
          in general["constraint_propagation"]
          and general["energyExchange"]["input"]
          == "-d4rho - 3*ad1*(p3 + rho) - 4*(p0 + rho)*(-ad1 + uu/2) == 0")
check(stated, "a4-equations.json states no off-diagonal source, p0 = p_t, the "
              "constraint propagation and the energy balance, as quoted",
      record="Revision/field_equations_a4/a4-equations.json, generalSource: "
             "offDiagonal, hiddenEqualsExtraTimes, constraint_propagation, "
             "energyExchange")
```

Four statements of the record of the field equations (key `generalSource`), each tested for the text this chapter quotes: the source has no off-diagonal component, $p_0 = p_t$, the constraint propagation (identity (I) in the record's names, with `hh` for $h_4$), and the energy balance of Section 11.22, compared character for character. Twenty-first PASS line.

**In [13], the end.**

```python
figure_files = [f"11c_{k}_{name}.png" for k, name in enumerate(
    ["components_linear_history", "lovelock_scalars", "test_history",
     "components_test_history", "conservation_identity"], 1)]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_files),
      "all five figure files of the notebook exist")
all_checks_passed()
```

The five figure files must exist (twenty-second PASS line), and the last line is ALL 22 CHECKS PASSED (notebook 11c). The 22 checks are: 2 in In [2], 2 in In [3], 5 in In [4], 2 in In [5], 1 each in In [6] and In [7], 2 in In [8], 1 each in In [9], In [10] and In [11], 3 in In [12] and 1 in In [13].

### 11.28 What we proved, what we computed, what we assumed

**PROVED in this chapter by derivations written out line by line** (each confirmed by a check of a notebook and, where named, of a Revision record):

- **The generalized Kronecker delta** (Sections 11.3 and 11.4): the author's determinant $\det[\delta(l_i, u_j)]$ is 0 when a label repeats in either list or a lower label is missing above, and otherwise the sign of the permutation that carries the lower list into the upper list; so the rule GKD of the Revision program is exactly the author's definition (Notebook 11a, In [2] to In [6]; records `Revision/gkd_lovelock/results/wolfram-gkd-report.json`, checks `gkd_equals_kdelta_exhaustive_length_1` to `_length_3`, which compare the Rust function GKD with the literal determinant, and `gkd-selftest.json`; the literal determinant itself is checked in `python-lovelock-report.json`, checks `gkd_examples` and `gkd_literal_equals_cofactor_expansion`, the second of which compares it with an independent cofactor expansion). The number of nonzero values $8!/(8 - p)!\cdot p!$, half of them $+1$ and half $-1$ for $p \ge 2$, with the counts 8; 56 and 56; 1008 and 1008; 20160 and 20160 for $p = 1$ to 4 (In [6], In [7], In [9]; record `wolfram-gkd-report.json`, entry `gkdComparison`). Every delta with nine or more labels vanishes in eight dimensions (pigeonhole), so $P_{(4)} = 0$ and Lovelock's sum stops at order 3 (In [10]; record `lovelock-report.json`, check `k4_tensor_vanishes`). The rule needs $p(p - 1)/2$ comparisons instead of the $p!$ products of the determinant. The birthday probability $r_p = 8!/((8 - p)!\,8^p)$ of a nonzero rearranged random pair (with the assumed rules of probability). None of this depends on the metric.
- **The author's second route** (Section 11.5): a determinant identity for the Levi-Civita symbol; raising all labels of the Levi-Civita tensor of a metric gives the factor $\sqrt{|\det g|}/\det g$, so the product of two Levi-Civita tensors is the sign of $\det g$ times the product of two symbols; for the corrected metric $\det g = e^{-2a_4}b_4^4\cot^2z\,|\sin z| > 0$ wherever $\sin z\cos z \ne 0$ (Section 1.21; record `python-lovelock-report.json`, check `sqrt_abs_det_g`), the sign is $+1$, and the author's second route gives the generalized delta without an extra sign.
- **The curvature that the sums use** (Section 11.10): the scale factors $f_0 = e^{-a_4}b_4^{1/2}|\cot z|$, $f_i = e^{a_4}$, $f_4 = 1$, $f_t = e^{-a_4}b_4^{1/2}(\sin^2z)^{1/12}$ and their rates; two of the 21 nonzero Christoffel symbols; the formula $R^{x_4c}{}_{x_0c} = \partial_0\ln f_c\,(\partial_4\ln f_c - \partial_4\ln f_0)$ for a diagonal metric with $g_{44} = -1$ and separated scale factors, whose first factor vanishes for 3-space (no warp) and whose second factor vanishes for the extra times (they change at the rate $h_4 = \frac12u - a_4'$ of the hidden direction), so that the corrected metric has no mixed curvature component and $R^{x_4}{}_{x_0} = 0$ for every history and every real $z$ (record `lovelock-report.json`, check `mixed_riemann_only_sectional`; Notebook 11b, In [8] and In [11]); the curvature $(a_4' - \frac12u)^2 - H^2k$ of the planes inside the block; the Ricci tensor, the Ricci scalar $R = 8a_4'^2 - 8a_4'u - 2a_4'' - 12H^2k + 5u^2 + 4v$ and the Einstein tensor from the plane curvatures (record `curvature.json`, entries `ricciScalar` and `einsteinMixed`); every nonzero $R^{ab}{}_{cd}$ is a polynomial of weight 2 in $H$, $a_4'$, $a_4''$, $u$, $v$, $k$, free of $x_0$. As dated history: in the metric of 2026-10-14, withdrawn on 2026-10-16, both factors were nonzero and $G^{x_4}{}_{x_0} = \frac32H\cot z\,b_4'/b_4$.
- **Laplace's rule** for determinants of every size, and **the expansion of every Lovelock tensor** along the column of its free upper label, $P_{(k)} = \delta\,L_{(k)} - 2k\,Y_{(k)}$ (Section 11.13; Notebook 11b, In [21]).
- **For every metric** (Sections 11.14 and 11.15): $L_{(1)} = 2R$, $P_{(1)} = -4G$, so $E_{(1)} = G$; the trace identity $\sum_hP_{(k)}{}^h{}_h = (8 - 2k)L_{(k)}$; $L_{(2)} = 4\,\mathrm{GB}$ and $P_{(2)} = -8\mathcal{H}$ with Lanczos's Gauss-Bonnet tensor $\mathcal{H}$, so $E_{(2)} = \mathcal{H}$ (Notebook 11b, In [18], In [19], In [22]; records `lovelock-report.json`, checks `k1_equals_minus_4_einstein`, `k1_trace_identity` to `k3_trace_identity`, and `python-lovelock-report.json`, checks `L1_equals_2R`, `k2_equals_minus_8_gauss_bonnet`, `L2_equals_4_gauss_bonnet`).
- **The structure of the components for the corrected metric** (Section 11.21), for every history $a_4(x_4)$, $b_4(x_4)$ and every order: only the diagonal is nonzero, in particular there is no $x_4$-$x_0$ component, because every curvature entry brings the same two labels to both lists of the delta (records `lovelock-report.json`, checks `k1_offdiagonal_vanishes` to `k3_offdiagonal_vanishes`); the three space components are equal, and the hidden component equals the three extra-time components, by the relabelling that exchanges $x_0$ and $x_5$ (checks `k1_hidden_equals_extra_times` to `k3_hidden_equals_extra_times`); the second derivatives $a_4''$ and $v$ enter at most linearly; the time component contains neither of them (the constraint; record `Revision/field_equations_a4/reports/python-a4-report.json`, check `constraint_first_order`), and the space and block components are linear in them, with the matrix $J = \begin{pmatrix}2 & -2\\ 0 & -\frac32\end{pmatrix}$ for Einstein's tensor (check `second_order_system`); the block component is at most linear in $k$, the other two at most quadratic; every component is unchanged when $a_4'$ and $u$ change sign together (by reversing the time), so the tensors do not distinguish a deflating from an inflating block; order $k$ has the weight $2k$. Notebook 11c, In [2] and In [4], confirms each statement with exact algebra.
- **The two conservation identities** (Section 11.22), from zero divergence: $\frac{d}{dx_4}E^{x_4}{}_{x_4} = 3a_4'(E^{x_1}{}_{x_1} - E^{x_4}{}_{x_4}) + 4h_4(E^{x_0}{}_{x_0} - E^{x_4}{}_{x_4})$ with $h_4 = \frac12u - a_4'$ (I), checked by hand for Einstein's tensor, and $E^{x_0}{}_{x_0} = E^{x_5}{}_{x_5}$ wherever $\cot z \ne 0$ (II); in the field equations they become the energy balance $\rho' = -3a_4'(\rho + p_3) - 4h_4(\rho + p_0)$ and the condition $p_0 = p_t$ (records `python-a4-report.json`, check `bianchi_x4`; `a4-equations.json`, key `generalSource`, entries `constraint_propagation`, `hiddenEqualsExtraTimes` and `energyExchange`; Notebook 11c, In [5] and In [12]).
- **Along the histories of the record** (Sections 11.20 and 11.23): every component is $H^{2k}$ times a polynomial in the slope $A$ and in $k$, even in $A$; the order-1 components and the order-2 time component reduced by hand; the diagonals at $x_4 = 0$, for example $G = \mathrm{diag}(-\frac23, \frac{41}{9}, \frac{41}{9}, \frac{41}{9}, \frac{19}{3}, -\frac23, -\frac23, -\frac23)H^2$; on the history of the record $L_{(1)}$ vanishes exactly at $k = \frac{14}{27}$, $L_{(2)}$ exactly at $k = (39 + \sqrt{1579})/9$, and $L_{(3)}$, with positive coefficients only, never; the source that the history needs, for Einstein gravity and with the author's weights (the block entry reduced by hand); the derivatives of the illustrative test history.

**PROVED by exact computation** (no rounding; by the Revision's programs, recomputed by the notebooks):

- GKD equals the author's determinant for every one of the 266,304 pairs of lengths 1 to 3 (Notebook 11a, In [6]; the Wolfram report, checks `gkd_equals_kdelta_exhaustive_length_1` to `_length_3`, and the Rust self-test record `gkd-selftest.json`, whose exhaustive part also covers these lengths; on the same pairs the sympy report's check `gkd_literal_equals_cofactor_expansion` confirms the determinant side: the literal determinant equals an independent cofactor expansion) and for every one of the 16,777,216 pairs of length 4 (the Rust self-test of the record `gkd-selftest.json`, read and checked by Notebook 11a, In [14]; the run itself takes 7 to 13 minutes).
- The 21 nonzero Christoffel symbols, the 112 nonzero components $R^{ab}{}_{cd}$, all of them plane curvatures, and the Ricci scalar of the corrected metric (Notebook 11b, In [6] to In [8]; records `curvature.json` and `python-lovelock-report.json`, checks `rust_christoffels_agree`, `rust_riemann_agrees` and `mixed_riemann_only_sectional`).
- All $3 \times 64$ components of $P_{(1)}, P_{(2)}, P_{(3)}$ and the scalars $L_{(1)}, L_{(2)}, L_{(3)}$, computed by the Rust program and again by the notebook's own GKD sum (Notebook 11b, In [3], In [4], In [14], In [15]; record `lovelock-tensors.json`, written again byte for byte; `python-lovelock-report.json`, checks `rust_k1_mixed_components_agree` to `rust_k3_mixed_components_agree` and `rust_L1_agrees` to `rust_L3_agrees`); the counters of the sums, 672, 26,880 and 322,560 GKD calls (In [14]; record `lovelock-report.json`, field `counters`); the literal sums of orders 1 and 2 without any skipping, with 7,280 and 815,360 GKD calls (In [16]; checks `k1_unpruned_literal_sum_agrees` and `k2_unpruned_literal_sum_agrees`); the cubic identity $L_{(3)} = 8(2T_1 + 8T_2 + \dots + T_8)$ for the corrected metric (In [20]; check `L3_equals_8_cubic_lovelock_density`); zero divergence and symmetry of all three tensors (record `lovelock-report.json`, checks `k1_divergence_free` to `k3_symmetric`); the 27 checks of the Rust program, the 56 of the sympy verification and the 29 of the Wolfram verification, none failed (In [3] and In [24]).
- The Euler density $L_{(4)}$, a polynomial of 25 terms, equal to $\frac{2048}{27}(729k^2 - 378k + 25)H^8$ on the history of the record (Notebook 11b, In [3] and In [22]).
- The components $E_{(1)}, E_{(2)}, E_{(3)}$ of Section 11.20 equal those recorded for the field equations of $a_4$ and $b_4$ and those of the independent sympy verification (Notebook 11c, In [3]; `python-a4-report.json`, check `json_lovelock_components`); the sources that the history of the record needs, for Einstein gravity and for the author's weights, equal the record (In [8]; `a4-equations.json`, key `exponentialHistory`, entry `authorWeights`; `python-a4-report.json`, check `author_weights_history_source`).

**COMPUTED** (numerical, with the measured accuracy):

- The Rust program's literal unpruned sums at a numerical point agree with the exact tensors to the relative rounding errors $7.86 \times 10^{-16}$ ($k = 1$) and $3.57 \times 10^{-13}$ ($k = 2$) (record `lovelock-report.json`, checks `k1_brute_force_numeric` and `k2_brute_force_numeric`; Notebook 11b, In [4], requires both below $10^{-10}$).
- GKD equals the determinant on 12,000 pseudo-random pairs of lengths 4 to 9 (Notebook 11a, In [10]) and on 200,000 pairs of each length 5 to 9 (record `gkd-selftest.json`); the numbers of nonzero values lie within 1.6 standard deviations of the birthday expectation (In [11] and In [15]).
- The rule GKD is more than ten times faster than sympy's determinant for 200 pairs of length 7 (In [12]; the times themselves are not printed).
- The positive zeros of the Lovelock scalars on the history of the record, with 15 digits: $k = 0.518519$ ($Hx_4 = -0.9852$) for $L_{(1)}$ and $k = 8.748515$ ($Hx_4 = 3.2533$) for $L_{(2)}$ (Notebook 11c, In [7]).
- Identity (I) along the illustrative test history by finite differences, to the relative deviations $1.7 \times 10^{-5}$, $6.8 \times 10^{-5}$, $6.5 \times 10^{-5}$ for $k = 1, 2, 3$, the size of the finite-difference error (Notebook 11c, In [11]).

**ASSUMED** (used, not proved here):

- The corrected metric of the Revision record (version 2 of 2026-10-16), as given in `Revision/SPEC.md` section 1, and the curvature convention of Misner, Thorne and Wheeler (Chapter 3).
- The history of the record, $a_4 = AHx_4$, $b_4 = b_4(0)\,e^{(4/3)AHx_4}$ with $A = 1$ and $b_4(0) = 1$, is a PRESCRIBED background: it is not a solution of the vacuum field equations, it needs the source of Section 11.23, and no field of the Revision record is shown to be that source.
- Lovelock's theorem in general: for every metric the tensors $P_{(k)}$ are divergence-free and symmetric, and they are the only such tensors built from the metric and its first and second derivatives (D. Lovelock, J. Math. Phys. 12, 498 (1971)). For the corrected metric divergence and symmetry are not assumed but PROVED by exact computation.
- The Chern-Gauss-Bonnet theorem (a classical result), quoted in Section 11.11 only to explain the name Euler density of $L_{(4)}$; nothing in this chapter depends on it, and $P_{(4)} = 0$ is proved there by the pigeonhole principle.
- The general formula of the cubic Lovelock density (a classical result): the record derived its coefficients from literal sums on random curvature tensors, and checked the identity exactly for the corrected metric; we do not derive it by hand.
- The tensor rule for a change of coordinates (Section 3.14), used for the reversal of the time and the relabelling; the rules of determinants of Section 1.20 (rule 1 for matrices larger than $2 \times 2$ is a standard theorem); that two polynomials that agree for all values of their variables have the same coefficients; the rules of probability used for the random tests (independent chances multiply; the expectation and the standard deviation of a count).

**HYPOTHESIS.** None: this chapter is geometry of the given metric.

**OPEN.** Whether nature has the couplings $\alpha_2$ and $\alpha_3$ of the Gauss-Bonnet and the cubic tensor, and which sign of $a_4'$ is realised, are not decided by the tensors computed here; Chapter 12 studies the field equations. Nothing is computed at the points $\sin z\cos z = 0$, where the metric degenerates (the fold $\cos z = 0$, where $g_{00}$ and $\det g$ vanish, and the points $\sin z = 0$). For the corrected metric no output of the author exists, so agreement with Lovelock tensors computed by the author for this metric is not established (the agreement of Section 11.20 concerns the withdrawn metric of 2026-10-14). The symmetry $A \to -A$ of this chapter is NOT the pairing of universes of masses $+m$ and $-m$ (Chapters 18 to 20); nothing in this chapter concerns the creation of universes or matter and antimatter.

### 11.29 Exercises

**Exercise 1.** Use the rule of Section 11.3 to compute (a) the delta with the lower list $(x_1, x_2, x_3, x_4)$ and the upper list $(x_3, x_1, x_4, x_2)$; (b) the delta with the lower list $(x_5, x_1, x_2)$ and the upper list $(x_1, x_2, x_5)$, and check (b) with the Leibniz formula; (c) the delta with the lower list $(x_1, x_2, x_0)$ and the upper list $(x_1, x_2, x_3)$.

*Answer.* (a) The places of $x_1, x_2, x_3, x_4$ in the upper list are 2, 4, 1, 3, so $\sigma = (2, 4, 1, 3)$. Its inversions are the pairs of entries $(2, 1)$, $(4, 1)$ and $(4, 3)$: three, an odd number, so the value is $-1$. (b) The places of $x_5, x_1, x_2$ in the upper list $(x_1, x_2, x_5)$ are 3, 1, 2: $\sigma = (3, 1, 2)$ with the two inversions $(3, 1)$ and $(3, 2)$, so the value is $+1$. The matrix has the rows $(0, 0, 1)$ ($x_5$ is the third upper label), $(1, 0, 0)$ and $(0, 1, 0)$; in the Leibniz formula only the permutation $\pi = (3, 1, 2)$ picks three ones, and its sign is $+1$, so $\det = +1$. (c) The lower label $x_0$ is not among the upper labels: row 3 is all zeros, case (c), and the value is 0.

**Exercise 2.** (a) How many of the $8^{10}$ pairs of index lists of length 5 have the value $+1$, how many $-1$, how many 0? (b) For the Rust self-test of length 6 (100,000 rearranged and 100,000 independent pairs), compute the expected number of nonzero values and its standard deviation, and compare with the record's count 7812.

*Answer.* (a) By the formula of Section 11.4,

$$
N_{\ne 0}(5) = 8\cdot 7\cdot 6\cdot 5\cdot 4\cdot 5! = 6720\cdot 120 = 806400 ,
$$

half of each sign: 403,200 values $+1$ and 403,200 values $-1$. The zeros are the rest:

$$
8^{10} - 806400 = 1073741824 - 806400 = 1072935424 .
$$

(b) The two chances are

$$
r_6 = \frac{8!}{2!\cdot 8^6} = \frac{20160}{262144} = 0.0769043,\qquad q_6 = \frac{N_{\ne 0}(6)}{8^{12}} = \frac{20160\cdot 720}{68719476736} = 0.000211 .
$$

The expectation is $100000\cdot(0.0769043 + 0.000211) = 7711.6$, and the standard deviation is

$$
\begin{aligned}
&\sqrt{100000\cdot 0.0769043\cdot 0.9230957 + 100000\cdot 0.000211\cdot 0.999789}\\
&\quad = \sqrt{7099.0 + 21.1} = \sqrt{7120.1} = 84.4 .
\end{aligned}
$$

The record's 7812 lies $(7812 - 7711.6)/84.4 = 1.19$ standard deviations above the expectation, as Notebook 11a prints (In [15]).

**Exercise 3.** Compute the determinant of the matrix with the rows $(2, 1, 0)$, $(0, 1, 3)$, $(1, 0, 1)$ by Laplace's rule along its second column, and compare with the six-term formula, which gives 5.

*Answer.* The second column holds $M_{12} = 1$, $M_{22} = 1$, $M_{32} = 0$, with the signs $(-1)^{1+2} = -1$, $(-1)^{2+2} = +1$, $(-1)^{3+2} = -1$. The minor $M^{(12)}$ (row 1 and column 2 removed) has the rows $(0, 3)$ and $(1, 1)$, determinant $0\cdot 1 - 3\cdot 1 = -3$; the minor $M^{(22)}$ has the rows $(2, 0)$ and $(1, 1)$, determinant $2$. So $\det M = -1\cdot(-3) + 1\cdot 2 - 0 = 3 + 2 = 5$, the same value.

**Exercise 4.** In a space of $n$ dimensions, which orders $k$ of the Lovelock tensors $P_{(k)}$ can be nonzero, for $n = 4, 5, 6, 8, 10$? Which scalars $L_{(k)}$ can be nonzero in eight dimensions?

*Answer.* The delta of $P_{(k)}$ has $2k + 1$ labels in each list, so $P_{(k)}$ vanishes when $2k + 1 > n$ (pigeonhole, Section 11.4). Hence: $n = 4$: $k = 1$ only (Einstein); $n = 5$ and $n = 6$: $k = 1, 2$; $n = 8$: $k = 1, 2, 3$; $n = 10$: $k = 1, 2, 3, 4$. For even $n = 2m$ the highest order is $m - 1$, as in the formula of Section 11.11. The scalar $L_{(k)}$ has $2k$ labels per list, so in eight dimensions $L_{(1)}$ to $L_{(4)}$ can be nonzero: $L_{(4)}$ is the Euler density, whose tensor $P_{(4)}$ vanishes; for the corrected metric it is a polynomial of 25 terms, and on the history of the record it is $\frac{2048}{27}(729k^2 - 378k + 25)H^8$ (Notebook 11b, In [3] and In [22]).

**Exercise 5.** At the moment $x_4 = 0$ of the history of the record ($a_4' = H$, $u = \frac43H$, $a_4'' = v = 0$, $k = 1$): (a) compute the Ricci tensor, the Ricci scalar and the Einstein tensor from the plane curvatures of Section 11.10; (b) write $P_{(1)}$ and check the trace identity of order 1 with $L_{(1)}$.

*Answer.* (a) With $a_4' - \frac12u = H - \frac23H = \frac13H$ the table of Section 11.10 gives, in units of $H^2$: 1 for two 3-space directions, 1 for 3-space and the time, $-\frac13$ for 3-space and a block direction, $\frac19$ for the time and a block direction, and $\frac19 - 1 = -\frac89$ for two block directions. The Ricci component of a direction is the sum of the curvatures of its seven planes:

$$
\begin{aligned}
R^{x_1}{}_{x_1} &= 2\cdot 1 + 1 + 4\cdot\big(-\tfrac13\big) = 3 - \tfrac43 = \tfrac53,\\
R^{x_4}{}_{x_4} &= 3\cdot 1 + 4\cdot\tfrac19 = \tfrac{27 + 4}{9} = \tfrac{31}{9},\\
R^{x_0}{}_{x_0} &= 3\cdot\big(-\tfrac13\big) + \tfrac19 + 3\cdot\big(-\tfrac89\big) = \tfrac{-9 + 1 - 24}{9} = -\tfrac{32}{9}
\end{aligned}
$$

(for $x_1$: two planes inside 3-space, one with the time, four with the block; for $x_4$: three with 3-space, four with the block; for $x_0$: three with 3-space, one with the time, three inside the block). The Ricci scalar is the sum of the eight diagonal entries:

$$
R = 3\cdot\tfrac53 + \tfrac{31}{9} + 4\cdot\big(-\tfrac{32}{9}\big) = \tfrac{45 + 31 - 128}{9} = -\tfrac{52}{9},
$$

in agreement with the formula $R = 8a_4'^2 - 8a_4'u - 2a_4'' - 12H^2k + 5u^2 + 4v = 8 - \frac{32}{3} - 12 + \frac{80}{9} = \frac{72 - 96 - 108 + 80}{9} = -\frac{52}{9}$. Subtracting $\frac12R = -\frac{26}{9}$ from each diagonal entry gives $G^{x_1}{}_{x_1} = \frac{15 + 26}{9} = \frac{41}{9}$, $G^{x_4}{}_{x_4} = \frac{31 + 26}{9} = \frac{57}{9} = \frac{19}{3}$ and $G^{x_0}{}_{x_0} = \frac{-32 + 26}{9} = -\frac23$, so

$$
G = \mathrm{diag}\big(-\tfrac23, \tfrac{41}{9}, \tfrac{41}{9}, \tfrac{41}{9}, \tfrac{19}{3}, -\tfrac23, -\tfrac23, -\tfrac23\big)H^2 ,
$$

the diagonal that Notebook 11b prints (In [23]). (b) Multiplying every entry by $-4$,

$$
P_{(1)} = -4G = \mathrm{diag}\big(\tfrac83, -\tfrac{164}{9}, -\tfrac{164}{9}, -\tfrac{164}{9}, -\tfrac{76}{3}, \tfrac83, \tfrac83, \tfrac83\big)H^2 .
$$

Its trace is $4\cdot\frac83 - 3\cdot\frac{164}{9} - \frac{76}{3} = \frac{32 - 164 - 76}{3}H^2 = -\frac{208}{3}H^2$. With $L_{(1)} = 2R = -\frac{104}{9}H^2$ the identity gives $(8 - 2)L_{(1)} = 6\cdot\big(-\frac{104}{9}\big)H^2 = -\frac{208}{3}H^2$: the same.

**Exercise 6.** Check identity (I) of Section 11.22 for $E_{(2)}$ along the history of the record ($A = 1$), from the table of Section 11.20.

*Answer.* On the history $a_4' = H$, $u = \frac43H$, $a_4'' = v = 0$, so $h_4 = \frac12u - a_4' = -\frac13H$ and $k' = k(2a_4' - u) = \frac23Hk$. The table gives, in units of $H^4$, $E^{x_4}{}_{x_4} = -\frac{76}{27} + \frac{80}{3}k - 12k^2$, $E^{x_1}{}_{x_1} = \frac{52}{27} + 48k - 12k^2$ and $E^{x_0}{}_{x_0} = \frac{212}{27} + \frac{184}{3}k$. The left side of (I), by the chain rule (only $k$ changes):

$$
\frac{d}{dx_4}E^{x_4}{}_{x_4} = \big(\tfrac{80}{3} - 24k\big)\cdot\tfrac23Hk = \big(\tfrac{160}{9}k - 16k^2\big)H
$$

(the derivative of $-12k^2$ with respect to $k$ is $-24k$; units $H^5$ from here on). The two differences, term by term:

$$
E^{x_1}{}_{x_1} - E^{x_4}{}_{x_4} = \tfrac{128}{27} + \tfrac{64}{3}k,\qquad E^{x_0}{}_{x_0} - E^{x_4}{}_{x_4} = \tfrac{288}{27} + \tfrac{104}{3}k + 12k^2 = \tfrac{32}{3} + \tfrac{104}{3}k + 12k^2
$$

($52 + 76 = 128$, $48 - \frac{80}{3} = \frac{64}{3}$, and the $k^2$ terms cancel in the first; $212 + 76 = 288$ and $\frac{184 - 80}{3} = \frac{104}{3}$ in the second). Multiply by $3a_4' = 3H$ and by $4h_4 = -\frac43H$:

$$
3H\big(\tfrac{128}{27} + \tfrac{64}{3}k\big) = \big(\tfrac{128}{9} + 64k\big)H,\qquad -\tfrac43H\big(\tfrac{32}{3} + \tfrac{104}{3}k + 12k^2\big) = \big(-\tfrac{128}{9} - \tfrac{416}{9}k - 16k^2\big)H .
$$

Their sum is $\big(64 - \frac{416}{9}\big)kH - 16k^2H = \big(\frac{160}{9}k - 16k^2\big)H$ ($64 = \frac{576}{9}$), the left side: identity (I) holds.

**Exercise 7.** For Einstein gravity the history of the record needs the source $-\kappa\rho - \Lambda = (\frac13 + 6k)H^2$, $\kappa p_3 - \Lambda = (-\frac{13}{9} + 6k)H^2$, $\kappa p_0 - \Lambda = \kappa p_t - \Lambda = (-\frac{11}{3} + 3k)H^2$ (Section 11.23). Check the energy balance $\rho' = -3a_4'(\rho + p_3) - 4h_4(\rho + p_0)$ of Section 11.22 on this history.

*Answer.* Adding the first equation to the second and to the third ($\Lambda$ cancels):

$$
\kappa(\rho + p_3) = \big(-\tfrac13 - 6k - \tfrac{13}{9} + 6k\big)H^2 = -\tfrac{16}{9}H^2,\qquad \kappa(\rho + p_0) = \big(-\tfrac13 - 6k - \tfrac{11}{3} + 3k\big)H^2 = (-4 - 3k)H^2 .
$$

The left side: $\kappa\rho = -\Lambda - (\frac13 + 6k)H^2$, so $\kappa\rho' = -6H^2k' = -6H^2\cdot\frac23Hk = -4kH^3$ ($\Lambda$ is a constant). The right side, with $a_4' = H$ and $h_4 = -\frac13H$:

$$
-3H\cdot\big(-\tfrac{16}{9}H^2\big) - 4\cdot\big(-\tfrac13H\big)(-4 - 3k)H^2 = \tfrac{16}{3}H^3 - \tfrac{16}{3}H^3 - 4kH^3 = -4kH^3 .
$$

Both sides agree, as the Bianchi identity requires; and $p_0 = p_t$, as identity (II) requires.

**Exercise 8.** For a diagonal metric with $g_{44} = -1$ and scale factors $f_c = A_c(x_4)B_c(x_0)$, Section 11.10 derived $R^{x_4c}{}_{x_0c} = \partial_0\ln f_c\,(\partial_4\ln f_c - \partial_4\ln f_0)$. Evaluate it for a 3-space direction and for an extra time, and the Ricci component $R^{x_4}{}_{x_0}$, (a) for the corrected metric; (b) for the metric of 2026-10-14, withdrawn on 2026-10-16 ($g_{00} = \cot^2z$, $g_{ii} = e^{2a_4}(\sin^2z)^{1/6}$, $g_{tt} = -e^{-2a_4}b_4(\sin^2z)^{1/6}$); (c) for the alternative K that the record offers to the author ($g_{00} = e^{2a_4}\cot^2z$, $g_{ii} = e^{2a_4}(\sin^2z)^{1/6}$, $g_{tt} = -e^{-2a_4}b_4$; `Revision/docs/METRIC_SELF_CONSISTENCY.md`, section 3.6).

*Answer.* The rates are read off the logarithms of the scale factors, with $\partial_0\ln(\sin^2z)^{1/12} = H\cot z$ and $\partial_0\ln|\cot z|$ not needed (only $\partial_4\ln f_0$ enters). (a) $\partial_4\ln f_0 = -a_4' + \frac12u$. 3-space, $f_i = e^{a_4}$: $\partial_0\ln f_i = 0$, product 0. Extra time, $f_t = e^{-a_4}b_4^{1/2}(\sin^2z)^{1/12}$: $\partial_4\ln f_t - \partial_4\ln f_0 = 0$, product 0. So $R^{x_4}{}_{x_0} = 0$. (b) $f_0 = |\cot z|$, so $\partial_4\ln f_0 = 0$. 3-space, $f_i = e^{a_4}(\sin^2z)^{1/12}$: $H\cot z\cdot a_4'$. Extra time: $H\cot z\cdot(-a_4' + \frac12u)$. The Ricci component adds three of each: $R^{x_4}{}_{x_0} = 3Ha_4'\cot z + 3H\cot z(\frac12u - a_4') = \frac32H\cot z\,u$, and since $\delta^{x_4}_{x_0} = 0$ the Einstein component is the same, $G^{x_4}{}_{x_0} = \frac32H\cot z\,b_4'/b_4$: a diagonal source would need $b_4' = 0$. (c) $f_0 = e^{a_4}|\cot z|$, so $\partial_4\ln f_0 = a_4'$. 3-space, $f_i = e^{a_4}(\sin^2z)^{1/12}$: $\partial_4\ln f_i - \partial_4\ln f_0 = a_4' - a_4' = 0$, product 0. Extra time, $f_t = e^{-a_4}b_4^{1/2}$: $\partial_0\ln f_t = 0$, product 0. So $R^{x_4}{}_{x_0} = 0$ here too: in K the hidden direction moves with 3-space, in the corrected metric with the extra times; both remove the mixed curvature, and the choice between them is the author's.

**Exercise 9.** On the history of the record $L_{(2)} = \frac{32}{27}(81k^2 - 702k - 58)H^4$ with $k = e^{2Hx_4/3}$ (Section 11.23). Show that $L_{(2)}$ vanishes at exactly one moment, and find $k$ and $Hx_4$ there to four decimals.

*Answer.* The product of the two roots of $81k^2 - 702k - 58$ is $-\frac{58}{81} < 0$ (the constant term divided by the leading coefficient), so one root is positive and one negative; only the positive one is a value of $k = e^{2Hx_4/3} > 0$, so $L_{(2)}$ vanishes at exactly one moment. By the formula for the roots of a quadratic, $k = (39 + \sqrt{1579})/9$ (Section 11.23). With $39.7366^2 = 1578.997$ and $39.7367^2 = 1579.005$, $\sqrt{1579} = 39.7366$ to four decimals, so $k = 78.7366/9 = 8.7485$. Then $Hx_4 = \frac32\ln k = \frac32(\ln 8 + \ln 1.09356) = \frac32(2.07944 + 0.08944) = \frac32\cdot 2.16888 = 3.2533$, as Notebook 11c prints (In [7]). Before this moment the Gauss-Bonnet scalar $\mathrm{GB} = L_{(2)}/4$ is negative, after it positive.

**Exercise 10.** (a) In two dimensions with the metric $g = \mathrm{diag}(1, -1)$ (one space-like, one time-like direction), compute $\varepsilon_{12}\varepsilon^{12}$ with the rule of Section 11.5. (b) The same with $g = \mathrm{diag}(-1, -1)$. (c) What decides the sign, and what is it for the author's metric?

*Answer.* (a) $|\det g| = 1$, so $\varepsilon_{12} = [12] = 1$, and $\varepsilon^{12} = g^{11}g^{22}\varepsilon_{12} = 1\cdot(-1)\cdot 1 = -1$; the product is $-1$, the sign of $\det g = -1$. (b) $\varepsilon^{12} = (-1)(-1)\cdot 1 = +1$, the product is $+1$, the sign of $\det g = +1$. (c) The sign of $\det g$, which for a diagonal metric is $(-1)$ to the number of negative entries: the number of time-like directions. The corrected metric has four, $x_4$ and the three extra times, so $\det g = e^{-2a_4}b_4^4\cot^2z\,|\sin z| > 0$ wherever $\sin z\cos z \ne 0$ (Section 1.21), and the sign is $+1$.

**Exercise 11.** For the illustrative test history of Section 11.23, compute $a_4'$, $a_4''$, $u$, $v$ and $k$ at $x_4 = 0$, the three independent components of $E_{(1)}$ there, and check identity (I) at this moment.

*Answer.* $a_4'(0) = H(1 + \frac12\tanh 0) = H$ and $a_4''(0) = \frac{H^2}{2}\mathrm{sech}^2\,0 = \frac{H^2}{2}$; then $u = \frac43a_4' = \frac43H$, $v = \frac43a_4'' = \frac23H^2$ and $k = e^{(2/3)a_4(0)} = e^0 = 1$ ($a_4(0) = 0 + \frac12\ln\cosh 0 = 0$). The components of Section 11.20 give, in units of $H^2$:

$$
\begin{aligned}
E^{x_1}{}_{x_1} &= 2\cdot\tfrac12 - 5 + 6\cdot\tfrac43 + 6 - \tfrac52\cdot\tfrac{16}{9} - 2\cdot\tfrac23 = 10 - \tfrac{40}{9} - \tfrac{12}{9} = \tfrac{38}{9},\\
E^{x_4}{}_{x_4} &= 3 + 6 - \tfrac32\cdot\tfrac{16}{9} = 9 - \tfrac83 = \tfrac{19}{3},\\
E^{x_0}{}_{x_0} &= -3 + \tfrac32\cdot\tfrac43 + 3 - \tfrac32\cdot\tfrac{16}{9} - \tfrac32\cdot\tfrac23 = -3 + 2 + 3 - \tfrac83 - 1 = -\tfrac53 .
\end{aligned}
$$

Compared with the history of the record at $x_4 = 0$ ($\frac{41}{9}$, $\frac{19}{3}$, $-\frac23$), the space component moves by $2a_4'' - 2v = -\frac13$, the block component by $-\frac32v = -1$, and the time component not at all, as Figure 11c.4 shows. Identity (I): the left side is $6a_4'a_4'' - 3uv + 12a_4'H^2k - 6H^2ku = 3 - \frac83 + 12 - 8 = \frac{13}{3}$ (units $H^3$; Section 11.22); the right side, with $h_4 = \frac23 - 1 = -\frac13$, is $3\big(\frac{38}{9} - \frac{57}{9}\big) - \frac43\big(-\frac53 - \frac{19}{3}\big) = -\frac{19}{3} + \frac{32}{3} = \frac{13}{3}$: the same.
