## 11. GKD and the Lovelock tensors

Einstein's equations of gravity set one curvature tensor, the Einstein tensor, equal to the energy and momentum of matter. In eight dimensions there is room for more: two further tensors, built from products of two and of three curvature tensors, have the same good properties as Einstein's. Together with Einstein's they are the three **Lovelock tensors** of the formula (4.38) that the author quotes in his notebook. Every term of these tensors carries a weight $+1$, $-1$ or $0$ given by the **generalized Kronecker delta**, which the author defined as a determinant and which the Revision program computes with a fast rule called **GKD**. This chapter proves that the rule is right, counts and tests it, builds the three Lovelock tensors of the author's metric twice (with the Revision Rust program and with independent Python code), proves their classical identities, and studies their components along the history in which the three extra times deflate exponentially. Chapter 12 then turns these components into the field equations for $a_4$.

### 11.1 What this chapter does, and why

In Chapter 3 we computed the curvature of the author's metric: its Christoffel symbols, its Riemann tensor $R^{ab}{}_{cd}$, its Ricci tensor and its Einstein tensor $G^h{}_j$. Einstein's field equations, $G^\mu{}_\nu + \Lambda\delta^\mu{}_\nu = \kappa T^\mu{}_\nu$, use only the Einstein tensor. Why that tensor? Because its **divergence** vanishes for every metric (the contracted Bianchi identity, Section 3.25), as the conservation of energy and momentum demands of the right-hand side. In 1971 David Lovelock found every tensor with this property that is built from the metric and its first and second derivatives (D. Lovelock, J. Math. Phys. 12, 498 (1971); we quote his theorem and do not prove it). In four dimensions only the Einstein tensor (and the constant term $\Lambda$) exists. In eight dimensions there are exactly three: the Einstein tensor and two companions. The author's notebook quotes them in the form of equation (4.38) of the book of Lovelock and Rund, and the Revision computed them for the author's metric (folder `Revision/gkd_lovelock`).

The chapter has three parts, each with one notebook.

- **The generalized Kronecker delta** (Sections 11.3 to 11.9). We restate the author's definition, a determinant of a matrix of zeros and ones, prove that it equals the sign of a permutation or zero, and show that this rule (GKD) is exactly what the Revision's Rust program computes. We count how often each value occurs, prove that a delta with nine labels in eight dimensions is always zero, compare the cost of the rule with the cost of the determinant, and connect the delta with the Levi-Civita tensors of the curved metric (the author's second route). Notebook 11a checks all of this in Python and runs the Rust self-test.
- **The three Lovelock tensors** (Sections 11.10 to 11.19). We recall the curvature of the author's metric, define the Lovelock tensors $P_{(1)}, P_{(2)}, P_{(3)}$ and the Lovelock scalars $L_{(1)}, L_{(2)}, L_{(3)}$, explain how the enormous sums are organised so that a computer can do them exactly, and prove by hand, line by line, that $P_{(1)} = -4G$, that $P_{(2)} = -8$ times the Gauss-Bonnet tensor, and the trace identity. Notebook 11b runs the Rust program `lovelock_gkd`, checks that it reproduces the Revision records byte for byte, and computes everything a second time in Python.
- **The components along the deflating history** (Sections 11.20 to 11.27). We write out the components of the normalised tensors $E_{(k)} = -P_{(k)}/2^{k+1}$, prove their structure (which components are equal, which contain $a_4''$, which do not care about the sign of $a_4'$), derive the two conservation identities that they obey, and draw them along the exponentially deflating history $a_4 = AHx_4$ and along an illustrative test history. Notebook 11c does this with exact algebra.

Everything in this chapter is geometry of the given metric: no physical assumption about matter enters, and nothing here concerns pairs of universes or matter and antimatter. Every formula is PROVED (by a derivation written out here, or by exact computation in the Revision records and the notebooks) or COMPUTED (a numerical test), and each statement names the record file and check that confirm it.

### 11.2 The words and symbols of this chapter

Each word is defined in plain terms here; the later sections make the definitions precise.

- **Coordinates** $x_1, \dots, x_8$: the author's names of the eight directions. $x_1, x_2, x_3$: ordinary 3-space (they inflate). $x_4$: the time. $x_5, x_6, x_7$: the three **extra times**, time-like directions that **deflate exponentially** when $a_4$ grows. $x_8$: the hidden space direction, through the angle $z = 6Hx_8$ with $0 < z < \pi/2$. Programs number the coordinates $0, 1, \dots, 7$, so the number 3 stands for $x_4$ and the number 7 for $x_8$.
- **Label**: the name of a coordinate. **Index list**: an ordered list of labels, such as $(x_2, x_1, x_4)$; its **length** $p$ is the number of entries. A **pair** of index lists is a **lower** list $(l_1, \dots, l_p)$ and an **upper** list $(u_1, \dots, u_p)$ of the same length.
- **Kronecker delta** $\delta(a, b) = \delta^b_a$: the number 1 if the labels $a$ and $b$ are equal, 0 otherwise.
- **Permutation**, **inversion**, **sign**: a permutation is a re-ordering of $p$ objects, written as the list $(\sigma(1), \dots, \sigma(p))$; an inversion is a pair of places $i < j$ with $\sigma(i) > \sigma(j)$; the sign is $(-1)^{\text{number of inversions}}$, $+1$ for an **even** and $-1$ for an **odd** permutation (Section 1.19).
- **Determinant** (Leibniz formula): $\det M = \sum_\pi \mathrm{sign}(\pi)\,M_{1\pi(1)}\cdots M_{p\pi(p)}$, a sum of $p!$ products, one for every permutation $\pi$ (Section 1.20). **Minor** $M^{(rc)}$: the matrix left when row $r$ and column $c$ of $M$ are removed.
- **Generalized Kronecker delta**: $\delta^{u_1\dots u_p}_{l_1\dots l_p} = \det[\delta(l_i, u_j)]$, the author's `kδ[lower, upper]`. **GKD**: the Rust function of the Revision program that computes it by the rule proved in Section 11.3.
- **Pigeonhole principle**: if more than $n$ objects are put into $n$ boxes, some box holds two of them.
- **Levi-Civita symbol** $[i_1\dots i_n]$: the sign of the list $(i_1, \dots, i_n)$ if it is a re-ordering of all $n$ labels, and 0 otherwise (Section 1.44).
- **Metric** $g_{ab}$, **inverse metric** $g^{ab}$: the author's metric is diagonal, so $g^{aa} = 1/g_{aa}$ and all other entries are zero.
- **Christoffel symbol** $\Gamma^a{}_{bc}$, **Riemann tensor** $R^a{}_{bcd}$ and $R^{ab}{}_{cd} = g^{bb}R^a{}_{bcd}$, **plane curvature** $K(a, b) = R^{ab}{}_{ab}$ (no sum), **Ricci tensor** $R^h{}_j = \sum_c R^{hc}{}_{jc}$, **Ricci scalar** $R = \sum_h R^h{}_h$, **Einstein tensor** $G^h{}_j = R^h{}_j - \frac12\delta^h_jR$: Chapter 3 (Sections 3.15 and 3.17) defines them.
- **Summed label**: in this chapter a label that appears once up and once down inside one term is summed over its eight values, unless "no sum" is said; the free labels $h$ and $j$ are never summed.
- **Lovelock tensor** $P_{(k)}{}^h{}_j$ of **order** $k$ and **Lovelock scalar** $L_{(k)}$: the sums of Section 11.11. **Normalised Lovelock tensor** $E_{(k)} = -P_{(k)}/2^{k+1}$; $E_{(1)}$ is the Einstein tensor. **Gauss-Bonnet tensor**: the classical name of the order-2 Lovelock tensor. **Density** $A_{(k)}{}^{lh} = \sqrt{|\det g|}\,g^{ll}P_{(k)}{}^h{}_l$: the form in which formula (4.38) is written.
- **Component**: one number of a tensor, such as $E^{x_1}{}_{x_1}$; a **diagonal** component has $h = j$.
- **Leaf**, **pruning** (skipping): a complete combination of $k$ curvature entries in the computer's search; pruning means leaving out combinations known to give zero.
- **Divergence** $\nabla_h P^h{}_j$: the curved-space form of "change plus outflow"; zero divergence means **conservation**.
- **History** $a_4(x_4)$: the metric function. **Linear history**: $a_4 = AHx_4$ with a constant **slope** $A$, so $a_4' = AH$ and $a_4'' = 0$; for $A > 0$ the extra times shrink like $e^{-AHx_4}$. **Illustration**: a choice made only to show how a formula behaves; it is not a solution of any equation.
- **Exact** computation: with whole numbers and fractions, no rounding. **Byte for byte**: two files equal in every byte.
- **Status labels**: PROVED (exact, by a derivation or by exact computation, with the record file and check), COMPUTED (numerical, with its accuracy), ASSUMED, HYPOTHESIS, OPEN.

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

| $p$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| products $p!$ | 1 | 2 | 6 | 24 | 120 | 720 | 5040 | 40320 | 362880 |
| comparisons $p(p-1)/2$ | 0 | 1 | 3 | 6 | 10 | 15 | 21 | 28 | 36 |
| pairs $8^{2p}$ | 64 | 4096 | 2.6e5 | 1.7e7 | 1.1e9 | 6.9e10 | 4.4e12 | 2.8e14 | 1.8e16 |

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

(the two definitions; $\sqrt{u}\sqrt{u} = u$), and $|\det g|/\det g$ is the sign of $\det g$. For the author's metric $\det g = \cos^2 z > 0$ for every $a_4$ (record `Revision/gkd_lovelock/results/python-lovelock-report.json`, check `sqrt_abs_det_g`; `Revision/gkd_lovelock/results/wolfram-gkd-report.json`, check `sqrt_det_g_is_cos`; Section 1.21), so the sign is $+1$: the product of the two curved Levi-Civita tensors is exactly the product of the two symbols, and the author's second route gives, after the contraction over seven labels and the division by $7!$, the ordinary Kronecker delta $\delta^b_a$ with no extra sign. In a metric with an odd number of time-like directions, such as the four-dimensional spacetime of everyday physics, the sign would be $-1$. Notebook 01c checks the author's second route with the flat metric of signature (4,4) (Section 1.44).

### 11.6 Example: the generalized Kronecker delta in Python and in Rust

Notebook 11a puts Sections 11.3 and 11.4 to work. It writes the author's definition literally in Python, as an exact determinant computed by sympy; writes the rule GKD as a Python function; reproduces the record's five examples; draws three $4 \times 4$ matrices and all six arrangements of three labels; compares the rule with the determinant for all 266,304 pairs of lengths 1 to 3 and for 12,000 pseudo-random pairs of lengths 4 to 9; counts the values and compares the counts with the formula and with the Wolfram record; shows that every delta of nine labels vanishes; compares the cost of the two methods; builds the Revision Rust program `lovelock_gkd` with cargo and runs its GKD self-test, which must reproduce the record `Revision/gkd_lovelock/results/gkd-selftest.json` byte for byte; compares the self-test's counts with the birthday formula; and checks once more that every check and number it quotes from the Revision records is there. It needs Rust. The Rust self-test alone takes 7 to 13 minutes, because it computes 200,000 literal determinants of $9 \times 9$ matrices, each a sum of 362,880 products; the whole notebook took 789.3 seconds when it was built and 699.3 seconds in its verification run (the provenance file `Revision/textbook/notebooks/11a_kronecker_delta_gkd.PROVENANCE.md`). It prints 24 PASS lines, draws six figures and ends with the line ALL 24 CHECKS PASSED (notebook 11a).

<!-- NOTEBOOK 11a -->

### 11.9 Line-by-line walk-through of Notebook 11a

The notebook has 17 code cells, In [1] to In [17]. This section explains every line of every one of them, in order: a line or a small group of lines is quoted, then explained. A line that starts with `#`, and the part of a line after `#`, is a **comment**, which Python skips; it is there for the reader. Inside a function the text in triple quotes below the `def` line is its **docstring**, a description that Python stores but does not run; to keep the quotations short, docstrings are left out of them where the explanation repeats them, and a long figure caption passed to `save_figure` is shortened to `...` (the full caption is printed under the figure in Section 11.8). Because Notebook 11a is the first notebook of this chapter, its set-up cell is explained here in full; the walk-throughs of Notebooks 11b and 11c refer back to this explanation.

**In [1], the set-up cell.** Its first part, down to the heading THE SET-UP between two lines of `=` signs, consists of comment lines that repeat the complete run instructions of Section 11.7, so that the notebook file carries its own instructions. The code below the heading computes no physics; it is the same in every notebook of the book except for the line that names the notebook (and, in notebooks without Rust, the three Rust lines explained at the end).

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
output_file(CAPTION_FILE).write_text("{}\n", encoding="utf-8", newline="\n")
```

A string that starts with `f` is an **f-string**: a name in braces is replaced by its value, so `CAPTION_FILE` is `"Revision/textbook/figures/11a.captions.json"`. `FIGURE_NUMBERS` and `CAPTIONS` start as empty dictionaries. The last line writes an empty JSON dictionary and a line end into the captions file; `encoding="utf-8"` fixes how letters are stored as bytes and `newline="\n"` stores the same line end on every system.

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
import re  # regular expressions: reads numbers out of a program's printed text
import time  # a stopwatch (used inside one check; no time is ever printed)

import numpy as np  # arrays of numbers and pseudo-random numbers
import sympy as sp  # exact algebra: sympy computes determinants exactly
```

Six more modules: `itertools` produces all lists of labels and all permutations; `math` has `math.factorial(p)` $= p!$ and `math.perm(n, p)` $= n!/(n - p)!$; `re` reads numbers out of text with **regular expressions** (patterns of characters); `time` provides a stopwatch; numpy (short name `np`) handles arrays of numbers and makes pseudo-random numbers; sympy (short name `sp`) does exact algebra.

```python
NAMES = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]  # the labels 0..7 by name
```

The list of the eight coordinate names; `NAMES[0]` is `"x1"` and `NAMES[7]` is `"x8"`, because Python counts places from 0.

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
SHOWN = [  # (lower list, upper list) with labels 0..7 standing for x1..x8
    ((0, 1, 2, 3), (1, 0, 3, 2)),  # x2 x1 x4 x3: two exchanges, even
    ((0, 1, 2, 3), (1, 2, 3, 0)),  # x2 x3 x4 x1: a cycle of four, odd
    ((0, 1, 2, 2), (0, 1, 2, 3)),  # x3 twice in the lower list
]
fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.9))
```

The three pairs of the examples of Section 11.3, written with the numbers 0 to 7 for $x_1$ to $x_8$. `plt.subplots(1, 3, ...)` makes a figure `fig` with one row of three panels, the **axes** (drawing areas) `axes[0]`, `axes[1]`, `axes[2]`, 10.5 by 3.9 inches in all.

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
lower = (0, 1, 2)  # x1, x2, x3
fig, axes = plt.subplots(2, 3, figsize=(9.0, 6.4))
signs = []
for ax, upper in zip(axes.flat, itertools.permutations(lower)):
    matrix = np.array(outer_delta(lower, upper))
    sigma = [upper.index(label) for label in lower]  # places of x1, x2, x3 above
    sign = 1 if inversions(sigma) % 2 == 0 else -1
    signs.append((sign, kdelta(lower, upper)))
```

A figure with two rows of three panels; `axes.flat` runs through the six panels one by one. `itertools.permutations(lower)` produces the $3! = 6$ arrangements of $(0, 1, 2)$. For each arrangement used as the upper list, `upper.index(label)` is the place of a label in it, so `sigma` lists the places of $x_1, x_2, x_3$; its sign comes from the inversions, and the pair (sign, exact determinant) is stored in `signs`.

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
python_record = json.loads(repository_file(
    "Revision/gkd_lovelock/results/python-lovelock-report.json").read_text(
        encoding="utf-8"))
entry = [c for c in python_record["checks"]
         if c["name"] == "gkd_literal_equals_cofactor_expansion"][0]
```

The Revision's sympy report is read: `read_text` reads the file as text and `json.loads` turns the JSON text into Python lists and dictionaries. Its checks form a list of entries; the comprehension keeps the entry whose name is `gkd_literal_equals_cofactor_expansion`, and `[0]` takes the first (and only) one.

```python
check(mismatches == 0 and compared == 266304 and entry["verdict"] == "PASS"
      and "266304 pairs" in entry["detail"],
      "GKD equals the literal determinant for all 266304 pairs of lengths 1 to 3",
      record="Revision/gkd_lovelock/results/python-lovelock-report.json, "
             "check gkd_literal_equals_cofactor_expansion")
```

The check requires no disagreement among the 266,304 pairs, and that the record's own check has the verdict PASS and speaks of the same 266304 pairs (`in` tests whether one text occurs inside another). Sixth PASS line.

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
ax.set_xticks(ticks, [f"({NAMES[t // 8]},x1)" for t in ticks], rotation=90)
ax.set_yticks(ticks, [f"({NAMES[t // 8]},x1)" for t in ticks])
```

The values are drawn with the colour map `bwr` (blue, white, red) from $-1$ (blue) through 0 (white) to $+1$ (red). `range(0, 64, 8)` is $0, 8, 16, \dots, 56$, the first list of each block of eight; `t // 8` is the first label of that block, so the marks read $(x_1, x_1)$, $(x_2, x_1)$, and so on (rotated by 90 degrees on the horizontal axis).

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

**In [13], the Rust program is built.**

```python
program = rust_program("Revision/gkd_lovelock/code/Cargo.toml", "lovelock_gkd")
```

The helper of the set-up cell runs cargo for the crate `Revision/gkd_lovelock/code` and returns the path of the program `lovelock_gkd` (with `.exe` on Windows), named `program` here. When the program is up to date this takes about a second; a first build took a few seconds on the computer that built the book (the crate has no dependencies, so nothing is downloaded). Output: Rust program lovelock_gkd is built and ready.

**In [14], the Rust self-test.** This is the cell that takes 7 to 13 minutes. The command it runs is

```text
lovelock_gkd gkd-selftest --exhaustive-max 4 --output FOLDER
```

with the option that makes the lengths 1 to 4 exhaustive and the folder for the result file.

```python
OUT_FOLDER = REPO / "Revision" / "gkd_lovelock" / "code" / "target" / "textbook_11a"
completed = subprocess.run(
    [str(program), "gkd-selftest", "--exhaustive-max", "4", "--output",
     str(OUT_FOLDER)],
    capture_output=True, text=True, encoding="utf-8", errors="replace")
say("The Rust self-test printed (as a table; its run time is left out):")
```

The result goes into a folder inside the crate's build folder `target`, which git ignores, so the run adds no file to the repository. `subprocess.run` starts the program (its path as text, then the command words) and collects its printed lines in `completed.stdout`. Then a heading line is printed.

```python
rust_rows = {}  # p -> (mode, pairs, nonzero or None, mismatches)
for line in completed.stdout.splitlines():
    found = re.search(r"all (\d+) pairs of index lists of length (\d+) .*: (\d+) "
                      r"mismatches", line)
    if found:  # an exhaustive length
        pairs, p, bad = (int(v) for v in found.groups())
        rust_rows[p] = ("exhaustive", pairs, None, bad)
```

`splitlines()` cuts the printed text into lines. `re.search(pattern, line)` looks for the pattern in a line; in the pattern, `(\d+)` captures a run of digits and `.*` stands for any characters. A line such as "PASS - GKD vs literal ..., all 64 pairs of index lists of length 1 over 8 values: 0 mismatches" matches, and `found.groups()` gives the three captured numbers: the number of pairs, the length and the number of mismatches. (The `r` before a string makes a **raw string**, in which a backslash stays a backslash.)

```python
    found = re.search(r"(\d+) pseudo-random pairs of length (\d+) \((\d+) nonzero\)"
                      r": (\d+) mismatches", line)
    if found:  # a random length
        pairs, p, nonzero, bad = (int(v) for v in found.groups())
        rust_rows[p] = ("random", pairs, nonzero, bad)
```

The same for the lines of the random lengths, which also state how many sampled values were nonzero; `\(` and `\)` are literal parentheses.

```python
for p, (mode, pairs, nonzero, bad) in sorted(rust_rows.items()):
    extra = "" if nonzero is None else f", {nonzero:6d} nonzero"
    say(f"  p = {p}: {mode:10s} {pairs:9d} pairs{extra}; disagreements: {bad}")
```

The collected rows are printed in the order of $p$ as a table, without the program's last line, which states its run time (a time differs from run to run). The output shows 64, 4096, 262144 and 16777216 pairs compared exhaustively for $p = 1$ to 4, and 200,000 random pairs for each $p = 5$ to 9 with 20538, 7812, 1949, 244 and 0 nonzero values; every disagreement count is 0.

```python
check(completed.returncode == 0 and "gkd-selftest: SUCCESS" in completed.stdout,
      "the Rust program lovelock_gkd gkd-selftest ended with SUCCESS")
check(sorted(rust_rows) == list(range(1, 10))
      and all(row[3] == 0 for row in rust_rows.values())
      and rust_rows[4][:2] == ("exhaustive", 16777216),
      "Rust: GKD equals the literal determinant for every tested pair, p = 1 to 9")
```

The first check requires the return code 0 and the program's verdict SUCCESS. The second requires a row for every length 1 to 9, no disagreement in any row (`row[3]` is the fourth entry, the mismatches) and the exhaustive test of all 16,777,216 pairs of length 4 (`[:2]` takes the first two entries of the row).

```python
written = (OUT_FOLDER / "gkd-selftest.json").read_bytes()
stored = repository_file("Revision/gkd_lovelock/results/gkd-selftest.json").read_bytes()
check(written == stored,
      "the program wrote gkd-selftest.json equal to the Revision record byte for byte",
      record="Revision/gkd_lovelock/results/gkd-selftest.json (the whole file)")
```

`read_bytes()` reads a file as its raw bytes. The file just written and the committed record must be equal in every byte: the program, built on this computer, has reproduced the Revision record exactly. PASS lines sixteen to eighteen.

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
      "the record quotes the author's definition as section 4 does",
      record=f"{RECORDS}/PROVENANCE_OF_THE_COMPUTATION.md")
```

The record of the author's definition is read, and the check requires the definition, from the bracket after its name on, to occur in it exactly as the notebook quotes it (the name itself is written with a Greek letter in the record). Twenty-second PASS line.

```python
order_three = [row for row in json.loads(repository_file(
    f"{RECORDS}/lovelock-report.json").read_text(encoding="utf-8"))["counters"]
    if row["k"] == 3][0]
report("GKD calls of the order-3 Lovelock sum (record)", order_three["gkdCalls"])
check(order_three["gkdCalls"] == 495360,
      "the order-3 Lovelock sum calls GKD 495360 times, as section 4 says",
      record=f"{RECORDS}/lovelock-report.json, counters, k = 3, gkdCalls")
```

The Rust report's counters are read and the row of order 3 is taken; its number of GKD calls, 495,360, is printed and checked (the number quoted in the notebook's section 4 and explained in Section 11.12). Twenty-third PASS line.

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

The Lovelock tensors are built from the Riemann tensor. Chapter 3 computed it for the author's metric by hand; here we collect what the sums need, in the convention of every Revision record (the convention of Misner, Thorne and Wheeler, Section 3.17):

$$
\Gamma^a{}_{bc} = \tfrac12\,g^{aa}\big(\partial_b g_{ac} + \partial_c g_{ab} - \partial_a g_{bc}\big),\qquad
R^a{}_{bcd} = \partial_c\Gamma^a{}_{db} - \partial_d\Gamma^a{}_{cb} + \sum_e\big(\Gamma^a{}_{ce}\Gamma^e{}_{db} - \Gamma^a{}_{de}\Gamma^e{}_{cb}\big),
$$

and $R^{ab}{}_{cd} = g^{bb}R^a{}_{bcd}$ (no sum; for a diagonal metric the general $\sum_e g^{be}R^a{}_{ecd}$ keeps only $e = b$). The form $R^{ab}{}_{cd}$, with two labels up and two down, is the one the Lovelock sums use. It changes sign when the two upper labels or the two lower labels are exchanged:

$$
R^{ab}{}_{cd} = -R^{ba}{}_{cd} = -R^{ab}{}_{dc}
$$

(record `Revision/gkd_lovelock/results/lovelock-report.json`, check `riemann_antisymmetry`; Section 3.17 proves it). In particular $R^{aa}{}_{cd} = 0$: a component with two equal upper labels or two equal lower labels vanishes.

**The plane curvatures.** For two different directions $a$ and $b$, $K(a, b) = R^{ab}{}_{ab}$ (no sum) is the curvature of their coordinate plane. Section 3.24 computed all 28 planes by hand. With $i$ standing for a 3-space direction ($x_1, x_2, x_3$), $j$ for an extra time ($x_5, x_6, x_7$) and $k$ for either:

| plane | how many | $K(a, b)$ | at $a_4' = 2H$, $a_4'' = 0$ |
| --- | --- | --- | --- |
| two 3-space directions $(i, i')$ | 3 | $a_4'^2 - H^2$ | $3H^2$ |
| two extra times $(j, j')$ | 3 | $a_4'^2 - H^2$ | $3H^2$ |
| a 3-space direction and an extra time $(i, j)$ | 9 | $-(a_4'^2 + H^2)$ | $-5H^2$ |
| a 3-space direction and the time $(i, x_4)$ | 3 | $a_4'^2 + a_4''$ | $4H^2$ |
| an extra time and the time $(j, x_4)$ | 3 | $a_4'^2 - a_4''$ | $4H^2$ |
| a transverse direction and the hidden one $(k, x_8)$ | 6 | $-H^2$ | $-H^2$ |
| the time and the hidden direction $(x_4, x_8)$ | 1 | 0 | 0 |

Figure 11b.2 draws these 28 numbers as an $8 \times 8$ table at $a_4' = 2H$, once with $a_4'' = 0$ and once with $a_4'' = H^2$ (Notebook 11b, In [9]). Each plane with $K \ne 0$ gives four nonzero components, $R^{ab}{}_{ab} = R^{ba}{}_{ba} = K(a, b)$ and $R^{ab}{}_{ba} = R^{ba}{}_{ab} = -K(a, b)$: 27 planes, 108 components.

**The components that mix the time and the hidden direction (PROVED).** The other nonzero components connect the plane of $x_4$ and $x_k$ with the plane of $x_8$ and $x_k$. We derive the first kind once more, line by line, writing the scale-factor exponent of the transverse direction $k$ as $\sigma_k$: the metric entry is $g_{kk} = \epsilon_k\,e^{2\sigma_ka_4}\sin^{1/3}z$ with $\sigma_k = +1$, $\epsilon_k = +1$ for 3-space (inflating, space-like) and $\sigma_k = -1$, $\epsilon_k = -1$ for an extra time (deflating, time-like). The formula for $R^a{}_{bcd}$ with $a = x_4$, $b = k$, $c = x_8$, $d = k$ reads

$$
R^4{}_{k8k} = \partial_8\Gamma^4{}_{kk} - \partial_k\Gamma^4{}_{8k} + \sum_e\Gamma^4{}_{8e}\Gamma^e{}_{kk} - \sum_e\Gamma^4{}_{ke}\Gamma^e{}_{8k}
$$

(the definition with these four labels). Nothing depends on $x_k$, so $\partial_k(\dots) = 0$; every symbol $\Gamma^4{}_{8e}$ is zero (the only nonzero symbols with the upper label $x_4$ are $\Gamma^4{}_{kk}$, Section 3.23); and in the last sum only $e = k$ survives:

$$
R^4{}_{k8k} = \partial_8\Gamma^4{}_{kk} - \Gamma^4{}_{kk}\,\Gamma^k{}_{8k} .
$$

The two symbols are, by the Christoffel formula with $g^{44} = -1$,

$$
\Gamma^4{}_{kk} = -\tfrac12\,g^{44}\,\partial_4 g_{kk} = \tfrac12\,\epsilon_k\,2\sigma_ka_4'\,e^{2\sigma_ka_4}\sin^{1/3}z = \epsilon_k\sigma_k\,a_4'\,e^{2\sigma_ka_4}\sin^{1/3}z,\qquad \Gamma^k{}_{8k} = \tfrac12\,g^{kk}\,\partial_8 g_{kk} = H\cot z
$$

(the chain rule: $\partial_4 e^{2\sigma_ka_4} = 2\sigma_ka_4'e^{2\sigma_ka_4}$; and $\partial_8\ln\sin^{1/3}z = \tfrac13\cot z\cdot 6H = 2H\cot z$, half of which is $H\cot z$). Since $\partial_8\sin^{1/3}z = 2H\cot z\,\sin^{1/3}z$,

$$
R^4{}_{k8k} = \epsilon_k\sigma_k\,a_4'\,e^{2\sigma_ka_4}\sin^{1/3}z\,\big(2H\cot z - H\cot z\big) = \epsilon_k\sigma_k\,Ha_4'\cot z\;e^{2\sigma_ka_4}\sin^{1/3}z
$$

(the derivative of the product; then the common factor taken out). Raising the second label multiplies by $g^{kk} = 1/(\epsilon_k e^{2\sigma_ka_4}\sin^{1/3}z)$:

$$
R^{4k}{}_{8k} = \sigma_k\,Ha_4'\cot z
$$

($\epsilon_k/\epsilon_k = 1$ and the exponentials cancel). So the sign is set by $\sigma_k$ alone, that is by whether the direction inflates or deflates, not by whether it is space-like or time-like: $R^{4i}{}_{8i} = +Ha_4'\cot z$ for the three 3-space directions and $R^{4j}{}_{8j} = -Ha_4'\cot z$ for the three extra times, as Section 3.24 found. The same steps with $a = x_8$, $c = x_4$ give $R^{8i}{}_{4i} = -Ha_4'\tan z$ and $R^{8j}{}_{4j} = +Ha_4'\tan z$ (Section 3.24). With the antisymmetries each of the six transverse $k$ gives eight such components: 48. Together $108 + 48 = 156$ nonzero components of the 4096 (record check `riemann_antisymmetry`, "156 nonzero entries"; Notebook 11b, In [7], recomputes them; Figure 11b.3 draws all 4096 at one point).

**What this means for the Ricci tensor.** The off-diagonal Ricci component $R^{x_4}{}_{x_8} = \sum_c R^{x_4c}{}_{x_8c}$ is the sum of the seven terms $c = x_1, \dots, x_7$ (the term $c = x_8$ vanishes by antisymmetry):

$$
R^{x_4}{}_{x_8} = 3\cdot(+Ha_4'\cot z) + 0 + 3\cdot(-Ha_4'\cot z) = 0
$$

(three inflating directions, the time itself, three deflating directions). The cancellation is exact for every $a_4$, because there are as many inflating as deflating directions (Notebook 11b, In [11], Figure 11b.4). Section 11.20 shows that the same cancellation leaves all three Lovelock tensors without an $x_4$-$x_8$ component.

**Three facts used below (PROVED).**

- Every nonzero $R^{ab}{}_{cd}$ is one of $a_4'^2 - H^2$, $-(a_4'^2 + H^2)$, $a_4'^2 \pm a_4''$, $-H^2$, $\pm Ha_4'\cot z$, $\pm Ha_4'\tan z$: a polynomial in $H$, $a_4'$, $a_4''$, $\cot z$ and $\tan z = 1/\cot z$, free of $e^{a_4}$ and of $\sin^{1/3}z$ (record check `mixed_riemann_free_of_sin_third`; `Revision/gkd_lovelock/results/python-lovelock-report.json`, check `mixed_riemann_free_of_warp_and_exponential`; Notebook 11b, In [7]).
- **Weight 2.** Count $H$ and $a_4'$ as 1 and $a_4''$ as 2 (each is one inverse length per count: $z = 6Hx_8$ is a pure number, so $H$ is an inverse length; $a_4$ is a pure number, so $a_4' = da_4/dx_4$ is an inverse length and $a_4''$ an inverse length squared), and $\cot z$ as 0. Then every one of the components just listed has the weight 2: curvature has the dimension $1/\text{length}^2$.
- **The Ricci tensor, the Ricci scalar and the Einstein tensor** (Section 3.25): $R^i{}_i = a_4'' - 6H^2$, $R^4{}_4 = 6a_4'^2$, $R^j{}_j = -a_4'' - 6H^2$, $R^8{}_8 = -6H^2$, every off-diagonal entry zero; $R = 6a_4'^2 - 42H^2$; and

$$
G^i{}_i = -3a_4'^2 + a_4'' + 15H^2,\quad G^4{}_4 = 3a_4'^2 + 21H^2,\quad G^j{}_j = -3a_4'^2 - a_4'' + 15H^2,\quad G^8{}_8 = 15H^2 - 3a_4'^2
$$

(record `Revision/gkd_lovelock/results/curvature.json`, keys `ricciMixed`, `ricciScalar`, `einsteinMixed`; Notebook 11b, In [8], reproduces the Ricci scalar).

### 11.11 Lovelock's equation (4.38): the three Lovelock tensors

**The formula.** The author's notebook contains, as the cell stored in the file as In[101] (his In[68]), an image of equation (4.38) of the book of Lovelock and Rund; the Revision rendered it to `Revision/gkd_lovelock/results/notebook-in68-image.png` and read the formula from that picture (record `Revision/gkd_lovelock/results/PROVENANCE_OF_THE_COMPUTATION.md`). For a space of $n = 2m$ dimensions it reads, as programmed in the record (`Revision/gkd_lovelock/code/src/lovelock.rs`),

$$
A^{lh} = \sqrt{|\det g|}\sum_{k=1}^{m-1}\alpha_{(k)}\,g^{jl}\,\delta^{h\,h_1\dots h_{2k}}_{j\,j_1\dots j_{2k}}\,R^{j_1j_2}{}_{h_1h_2}\cdots R^{j_{2k-1}j_{2k}}{}_{h_{2k-1}h_{2k}} + \lambda\sqrt{|\det g|}\,g^{lh},
$$

with constants $\alpha_{(k)}$ and $\lambda$, and a sum over every label that appears once up and once down ($j$ and the $4k$ labels $h_1, \dots, h_{2k}, j_1, \dots, j_{2k}$). The building blocks are, for each **order** $k$, the **Lovelock tensor**

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

**Which orders exist (PROVED).** The delta of order $k$ has $2k + 1$ labels in each list. In eight dimensions ($m = 4$) the sum runs over $k = 1, 2, 3$, and the order $k = 4$, with nine labels, vanishes identically by the pigeonhole principle (Section 11.4; record check `k4_tensor_vanishes`). So there are exactly three Lovelock tensors in eight dimensions. The scalar $L_{(4)}$, with eight labels per list, does not vanish: it is the **Euler density** of eight dimensions, and only its tensor $P_{(4)}$ is zero. For the author's metric the program prints it (Notebook 11b, In [3]):

$$
L_{(4)} = -663552\,H^2a_4'^6 - 442368\,H^4a_4'^4 - 663552\,H^6a_4'^2 .
$$

**The usual normalisation.** Books on gravity use the normalised tensors

$$
E_{(k)}{}^h{}_j = -\frac{1}{2^{k+1}}\,P_{(k)}{}^h{}_j ,
$$

because then $E_{(1)}$ is exactly Einstein's tensor $G$ (Section 11.14). The field equations of Chapter 12 are $\sum_{k=1}^{3}\alpha_kE_{(k)}{}^\mu{}_\nu + \Lambda\delta^\mu_\nu = \kappa T^\mu{}_\nu$, with $\alpha_1 = 1$, $\alpha_2 = \alpha_3 = 0$ for Einstein's gravity (record `Revision/field_equations_a4/a4-equations.json`, key `conventions`, entry `fieldEquations`). Any other normalisation is absorbed into the constants $\alpha_k$.

**What Lovelock proved (quoted, ASSUMED in general).** For every metric each $P_{(k)}$ has zero covariant divergence, $\sum_h\nabla_hP_{(k)}{}^h{}_j = 0$, and is symmetric once its upper label is lowered, $g_{hh}P_{(k)}{}^h{}_j = g_{jj}P_{(k)}{}^j{}_h$ (for a diagonal metric); and every tensor with these properties that is built from the metric and its first and second derivatives is a combination of the $P_{(k)}$ and of $\delta^h_j$. We do not prove this theorem. For the author's metric both properties are PROVED by exact computation in the record: checks `k1_divergence_free` to `k3_divergence_free` and `k1_symmetric` to `k3_symmetric` of `Revision/gkd_lovelock/results/lovelock-report.json` and of `Revision/gkd_lovelock/results/python-lovelock-report.json` (the symmetry makes $A_{(k)}{}^{lh} = A_{(k)}{}^{hl}$). Section 11.22 writes out what zero divergence means for the components.

**Weight $2k$ (PROVED).** The generalized delta is a pure number, and each of the $k$ curvature factors has the weight 2 (Section 11.10). So every term of $P_{(k)}$ has the weight $2k$: the tensor of order $k$ has the dimension $1/\text{length}^{2k}$. The three orders can be added in one equation only with constants $\alpha_k$ of different dimensions, for example $\alpha_k = w_k/H^{2k-2}$ with pure numbers $w_k$; this is the role of $H$ as "a fundamental inverse length" in the author's notebook (Chapter 12 uses the combinations $\alpha_2H^2$ and $\alpha_3H^4$).

### 11.12 Organising the sum: only nonzero curvature, no repeated label

**How large the literal sum is.** For one component $(h, j)$ the sum over the $4k$ labels $h_1, \dots, h_{2k}, j_1, \dots, j_{2k}$, each with 8 values, has $8^{4k}$ terms; for all 64 components $64\cdot 8^{4k}$. That is $2.6 \times 10^5$ terms for $k = 1$, $1.1 \times 10^9$ for $k = 2$, $4.4 \times 10^{12}$ for $k = 3$ and $1.8 \times 10^{16}$ for $k = 4$ (Notebook 11b, In [5]). Each term is a product of exact polynomials, so the literal sum of order 3 is out of reach. Three exact facts make it small.

**Step 1: only nonzero curvature factors.** A term with a vanishing curvature factor vanishes. So each factor need only run through the 156 nonzero entries $R^{ab}{}_{cd}$ of Section 11.10, and a term is an ordered choice of $k$ entries: $64\cdot 156^k$ terms for all components, $1.0 \times 10^4$, $1.6 \times 10^6$, $2.4 \times 10^8$ and $3.8 \times 10^{10}$ for $k = 1$ to 4.

**Step 2: no repeated label.** If two chosen entries share an upper label, or an entry shares an upper label with the free label $j$, the delta's lower list repeats a label and the delta is 0 (case a of Section 11.3); the same for the lower labels and the free $h$ (case b). The program therefore builds the choices one entry at a time and keeps an entry only if it repeats no label already used. To test this quickly it stores a set of labels as a **bit mask**, the whole number $\sum 2^{\text{label}}$: the set $\{x_1, x_3\}$ (numbers 0 and 2) is $2^0 + 2^2 = 5$. Two sets share a label exactly when the bitwise AND of their masks is not 0 (the AND keeps a bit where both numbers have a 1, Section 1.49), and the union of two sets is their bitwise OR (a bit is 1 where at least one of the two numbers has a 1). A complete choice of $k$ entries is called a **leaf**. The counts of leaves for all 64 components are 5,616, 176,640, 1,128,960 and 0 for $k = 1, 2, 3, 4$ (record `Revision/gkd_lovelock/results/lovelock-report.json`, field `counters`, entry `leaves`). For $k = 4$ there is no leaf: three entries already use seven different labels in the lower list ($j$ and six more), and a fourth entry would bring two more, nine different labels out of eight.

**Step 3: equal label sets.** At a leaf the lower list holds $2k + 1$ different labels and so does the upper list. If the two sets of labels differ, some lower label is missing above and the delta is 0 (case c). Only leaves whose two masks are equal are passed to GKD, which then returns $+1$ or $-1$ (case d: both lists hold the same different labels). The numbers of GKD calls are 696, 32,640, 495,360 and 0, and every one of them gives a nonzero value (record entries `gkdCalls` and `gkdNonzero`, equal for every $k$). For the scalars $L_{(k)}$ the calls are 108, 7,200, 213,120 and, for the nonzero Euler density $L_{(4)}$, 1,105,920 (entry `scalarGkdCalls`).

**Step 4: exact products, collected.** Every term that remains is weighted by an explicit call of GKD, multiplied out exactly and added. The program represents every quantity as an exact **Laurent polynomial** (a sum of monomials that may contain negative powers, such as $\cot^{-1}z$) in $H$, $a_4'$, $a_4''$ (and the higher derivatives), $e^{a_4}$, $\sin^{1/3}z$ and $\cot z$, with coefficients that are exact fractions of whole numbers (the files `poly.rs` and `rational.rs` of the crate; every operation that would overflow stops the program instead of rounding). So the result is exact: no rounding happens anywhere.

**How the skipping is tested.** The steps 1 to 3 rest on the theorem of Section 11.3, and they are tested in four independent ways, none of which skips anything:

- the program itself evaluates the literal, unpruned sum over all $64\cdot 8^4 = 262144$ index lists of order 1 and all $64\cdot 8^8 = 1073741824$ index lists of order 2, with GKD weights, at one numerical point, and finds the exact tensors up to rounding errors of $1.40 \times 10^{-15}$ and $4.41 \times 10^{-14}$ (relative; checks `k1_brute_force_numeric` and `k2_brute_force_numeric` of `lovelock-report.json`);
- the Revision's sympy checker evaluates the unpruned literal sums of orders 1 and 2 with the author's determinant on every ordered product of nonzero entries (10,140 and 1,581,840 calls) and finds the same tensors exactly (`python-lovelock-report.json`, checks `k1_unpruned_literal_sum_agrees` and `k2_unpruned_literal_sum_agrees`);
- the Revision's Wolfram check calls the author's verbatim definition on every ordered product for $k = 1$ (9,984 calls) and $k = 2$ (1,557,504 calls) and on every leaf for $k = 3$ (1,128,960 calls), and finds the Rust tensors exactly (`wolfram-gkd-report.json`, checks `k1_P_equals_rust_all_64_components` to `k3_P_equals_rust_all_64_components`);
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
P_{(k)}{}^h{}_j = \delta^h_jL_{(k)} - \sum_{s=1}^{2k}T_s,\qquad T_s = \sum\delta^{h_1\dots h_{2k}}_{j_1\dots(j\text{ at place }s)\dots j_{2k}}\;R^{j_1j_2}{}_{h_1h_2}\cdots(\text{with } h \text{ in place of } j_s)\cdots R^{j_{2k-1}j_{2k}}{}_{h_{2k-1}h_{2k}} .
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

(insert $L_{(1)} = 2R$ and $Y_{(1)} = 2R^h{}_j$; take out $-4$; the definition of $G$), and therefore $E_{(1)} = -P_{(1)}/2^2 = G$. This holds for every metric. For the author's metric the record checks it in all 64 components (`lovelock-report.json` and `python-lovelock-report.json`, check `k1_equals_minus_4_einstein`; `wolfram-gkd-report.json`, check `k1_equals_minus_4_einstein`), and so does Notebook 11b (In [18]). With the Einstein tensor of Section 11.10 the components of $P_{(1)}$ are $-4$ times those of $G$: for example $P_{(1)}{}^{x_1}{}_{x_1} = 12a_4'^2 - 4a_4'' - 60H^2$, as the Wolfram record lists (`wolfram-gkd-report.json`, field `measurements`, entry `wolframComponents`). And $L_{(1)} = 2R = 12a_4'^2 - 84H^2$ (record `Revision/gkd_lovelock/results/lovelock-tensors.json`, key `L1`; Notebook 11b, In [22]).

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
L_{(2)} = 4R^2 - 8\sum R^b{}_xR^x{}_b - 8\sum R^h{}_cR^c{}_h + 4\sum R^{ab}{}_{cd}R^{cd}{}_{ab} = 4\Big(R^2 - 4\sum_{a,b}R^a{}_bR^b{}_a + \sum R^{ab}{}_{cd}R^{cd}{}_{ab}\Big) = 4\,\mathrm{GB}
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

Multiplying by $-4$ gives $-8\mathcal{H}^h{}_j = -16R\,R^h{}_j + 32\sum R^h{}_aR^a{}_j + 32\sum R^{ha}{}_{jb}R^b{}_a - 16\sum R^{ha}{}_{bc}R^{bc}{}_{ja} + 4\delta^h_j\,\mathrm{GB}$, which is $P_{(2)}{}^h{}_j$ term by term after renaming the summed labels ($b \to a$, $x \to b$ in the second term; $b \to a$, $c \to b$, $d \to c$ in the fourth). So $P_{(2)} = -8\mathcal{H}$ and $E_{(2)} = -P_{(2)}/8 = \mathcal{H}$ for every metric: the second Lovelock tensor is the Gauss-Bonnet tensor. For the author's metric the record checks it in all 64 components (`python-lovelock-report.json`, checks `k2_equals_minus_8_gauss_bonnet` and `L2_equals_4_gauss_bonnet`), and so does Notebook 11b (In [19]). The record also found the factors $-4$ and $-8$ without any algebra, from literal sums on random curvature tensors in four and five dimensions (checks `normalisation_P1_derived_minus_4` and `normalisation_P2_derived_minus_8`). With $L_{(2)} = -96a_4'^4 - 2112a_4'^2H^2 + 3360H^4$ (record key `L2`), the Gauss-Bonnet scalar of the author's metric is $\mathrm{GB} = L_{(2)}/4 = -24a_4'^4 - 528a_4'^2H^2 + 840H^4$.

**Order 3 (PROVED for the author's metric by exact computation; the general formula quoted).** The third scalar is the **cubic Lovelock density**,

$$
L_{(3)} = 8\big(2T_1 + 8T_2 + 24T_3 + 3T_4 + 24T_5 + 16T_6 - 12T_7 + T_8\big),
$$

with the eight cubic invariants $T_1 = R^{ab}{}_{cd}R^{cd}{}_{ef}R^{ef}{}_{ab}$, $T_2 = R^{ab}{}_{cd}R^{ce}{}_{bf}R^{df}{}_{ae}$, $T_3 = R^{ab}{}_{cd}R^{cd}{}_{be}R^e{}_a$, $T_4 = R\,R^{ab}{}_{cd}R^{cd}{}_{ab}$, $T_5 = R^{ab}{}_{cd}R^c{}_aR^d{}_b$, $T_6 = R^a{}_bR^b{}_cR^c{}_a$, $T_7 = R\,R^a{}_bR^b{}_a$, $T_8 = R^3$ (every label summed). We do not derive these coefficients by hand: the record determined them from literal sums on nine random curvature tensors in six dimensions (a system of nine equations for eight unknowns with a unique solution; `python-lovelock-report.json`, check `normalisation_L3_cubic_derived`), and checked the identity exactly for the author's metric (check `L3_equals_8_cubic_lovelock_density`); Notebook 11b checks it again (In [20]). For the author's metric $L_{(3)} = 1152a_4'^6 + 31104a_4'^4H^2 + 100224a_4'^2H^4 - 40320H^6$ (record key `L3`).

### 11.16 Example: the three Lovelock tensors computed twice

Notebook 11b computes the three Lovelock tensors of the author's metric in two independent ways and checks Sections 11.10 to 11.15. It builds and runs the Revision Rust program `lovelock_gkd`, which computes everything exactly from the metric alone, runs its 19 checks and writes four files; the notebook compares the four files with the committed Revision records byte for byte. Then it recomputes the Riemann tensor with sympy and compares all 156 nonzero components with the record; draws the plane curvatures, the whole Riemann tensor and the cancelling mixed terms; recomputes the three tensors and scalars with its own Python GKD sum and its own exact arithmetic, reproduces every counter of the Rust sums and all $3 \times 64$ components; repeats the sums of orders 1 and 2 literally; checks the expansion of Section 11.13, the identities $P_{(1)} = -4G$, $P_{(2)} = -8\mathcal{H}$, the cubic density, the trace identities and $P_{(4)} = 0$; draws the components of $E_{(1)}, E_{(2)}, E_{(3)}$ at one moment of a deflating history; and checks that every check it quotes from the records is there. It needs Rust and takes one and a half to two minutes (99.6 seconds when it was built, 95.6 seconds in its verification run; provenance file `Revision/textbook/notebooks/11b_lovelock_tensors.PROVENANCE.md`). It prints 36 PASS lines, draws five figures and ends with the line ALL 36 CHECKS PASSED (notebook 11b).

<!-- NOTEBOOK 11b -->

### 11.19 Line-by-line walk-through of Notebook 11b

The notebook has 25 code cells, In [1] to In [25]. As in Section 11.9, every line or small group of lines is quoted and explained; docstrings are left out where the explanation repeats them, and long captions are shortened to `...` (they are printed in full under the figures in Section 11.18).

**In [1], the set-up cell.** It is word for word the set-up cell of Notebook 11a, explained line by line in Section 11.9 under In [1], with two differences: its comment lines are the run instructions of Notebook 11b (Section 11.17), and its line `NOTEBOOK_ID = "11b"  # this notebook: chapter 11, example b` names this notebook, so the figures are saved as `11b_<k>_<name>.png` and their captions in `11b.captions.json`. It contains the helper `rust_program`. It prints Set-up of notebook 11b complete: repository folder found, helpers defined.

**In [2], the Rust program is built.**

```python
program = rust_program("Revision/gkd_lovelock/code/Cargo.toml", "lovelock_gkd")
```

The same line as In [13] of Notebook 11a: cargo builds the crate (or confirms in about a second that it is up to date), and `program` is the path of `lovelock_gkd`. Output: Rust program lovelock_gkd is built and ready.

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

The module `re` reads parts of the printed lines. `RESULTS` is the folder of the Revision records, and `OUT_FOLDER` a folder inside the crate's build folder `target`, which git ignores, so the run adds nothing to the repository. `subprocess.run` starts the program and collects what it prints (Section 11.9, In [1] and In [14]). The program computes, exactly and from the metric alone, the Christoffel symbols, the Riemann tensor and the Lovelock tensors of orders 1 to 4, runs its 19 checks and writes four files; this takes about 15 seconds.

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

The 19 checks are printed as a numbered table (the format `:34s` pads a text to 34 places): `riemann_antisymmetry`, `riemann_first_bianchi`, `mixed_riemann_free_of_sin_third`, `k1_equals_minus_4_einstein`, then for each order $k = 1, 2, 3$ the trace identity, zero divergence, symmetry and freedom from $\sin^{1/3}z$ (the order-1 trace identity comes right after the Einstein check), then `k4_tensor_vanishes` and the two brute-force checks; all PASS.

```python
readable = (l4_text.replace("Derivative[1][a4][x4]", "a4'").replace("*", " ")
            .replace("(", "").replace(")", ""))
report("eighth-order scalar printed by the program, L(4)", readable)
```

The program writes $a_4'$ in Mathematica's notation `Derivative[1][a4][x4]`; the chain of `replace` calls turns it into `a4'`, multiplication stars into blanks, and removes parentheses. The RESULT line prints $L_{(4)} = -663552H^2a_4'^6 - 442368H^4a_4'^4 - 663552H^6a_4'^2$, the nonzero Euler density of Section 11.11.

```python
check(completed.returncode == 0 and "lovelock: SUCCESS" in completed.stdout,
      "the Rust program lovelock_gkd lovelock ended with SUCCESS")
check(len(rust_checks) == 19 and all(v == "PASS" for _, v in rust_checks),
      "all 19 checks of the Rust program passed",
      record=f"{RESULTS}/lovelock-report.json, checkCount 19, failedCheckCount 0")
```

Two checks: the program ended with the return code 0 and the verdict SUCCESS, and it printed exactly 19 checks, all PASS, as the record states. PASS lines one and two.

**In [4], the four files against the records.**

```python
DEVIATION = re.compile(r"(max relative deviation from the exact P_\(\d\) = )"
                       r"([0-9.]+e[-+]?\d+)")  # the two floating-point numbers
```

`re.compile` prepares a pattern for repeated use. It finds the text "max relative deviation from the exact P_(1) = " (or P_(2); `\d` is one digit, `\(` and `\)` literal parentheses) as the first group, and the decimal number that follows as the second group: digits and points, the letter e, an optional sign and digits, for example `1.40e-15`.

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

The three files that hold only exact numbers are compared with the committed records byte for byte, and their sizes are printed: 28,162, 55,056 and 19,604 bytes. PASS lines three to five.

```python
written = (OUT_FOLDER / "lovelock-report.json").read_text(encoding="utf-8")
stored = repository_file(f"{RESULTS}/lovelock-report.json").read_text(
    encoding="utf-8")
deviations = [float(number) for _, number in DEVIATION.findall(written)]
masked_written = DEVIATION.sub(r"\1X", written)  # the two numbers replaced by X
masked_stored = DEVIATION.sub(r"\1X", stored)
```

The report holds two decimal numbers, the rounding errors of the two brute-force checks, whose last digits may depend on the mathematics library of the operating system. `DEVIATION.findall(written)` finds both, and `float` turns the second group of each into a decimal number. `DEVIATION.sub(r"\1X", ...)` replaces every match by its first group followed by the letter X, so the two numbers disappear from both texts.

```python
report("size of lovelock-report.json", len(written.encode("utf-8")), "bytes")
check(masked_written == masked_stored and len(deviations) == 2
      and all(value < 1e-10 for value in deviations),
      "the program wrote lovelock-report.json equal to the Revision record byte for "
      "byte, apart from its two brute-force deviations, both below 1e-10",
      record=f"{RESULTS}/lovelock-report.json (the whole file; checks "
             "k1_brute_force_numeric and k2_brute_force_numeric)")
```

The size is printed (3,154 bytes). The check requires the masked texts to be equal, exactly two deviations, and both below the program's own limit $10^{-10}$. (On the computer that built the book the file was equal byte for byte even without the masking.) Sixth PASS line.

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
    say(f"      {k}   {64 * 8 ** (4 * k):13.2e}   {64 * 156 ** k:16.2e}   "
        f"{leaves:7d}   {calls:9d}   {nonzero:11d}")
```

A table of Section 11.12: for each order the literal number $64\cdot 8^{4k}$ of index lists, the number $64\cdot 156^k$ of ordered products of nonzero entries, and the record's leaves, GKD calls and nonzero GKD values. The output shows 5616, 176640, 1128960, 0 leaves and 696, 32640, 495360, 0 calls, each call nonzero.

```python
fig, ax = plt.subplots(figsize=(7.6, 4.5))
orders = np.array([1, 2, 3, 4])
series = [("literal index lists, $64 \\cdot 8^{4k}$", [64 * 8 ** (4 * k)
                                                      for k in orders], "0.7"),
          ("ordered products of nonzero entries, $64 \\cdot 156^k$",
           [64 * 156 ** k for k in orders], "tab:purple"),
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
check([COUNTERS[k]["leaves"] for k in (1, 2, 3, 4)] == [5616, 176640, 1128960, 0]
      and [COUNTERS[k]["gkdCalls"] for k in (1, 2, 3, 4)] == [696, 32640, 495360, 0],
      "the counters of the Rust sums are 5616, 176640, 1128960, 0 leaves and 696, "
      "32640, 495360, 0 GKD calls")
```

The check fixes the counters quoted in the text. Seventh PASS line.

*What Figure 11b.1 shows.* For each order four bars on a logarithmic axis: grey (all literal index lists), purple (ordered products of nonzero curvature entries), blue (leaves without a repeated label) and orange (GKD calls). For $k = 3$ the grey bar reaches $4.4 \times 10^{12}$ while the orange one stays at 495,360, about one term in nine million. For $k = 4$ the blue and orange bars are missing (marked 0): no leaf exists, because nine labels out of eight must repeat.

**In [6], the metric and its Christoffel symbols with sympy.**

```python
import sympy as sp  # exact algebra and calculus

H = sp.Symbol("H", positive=True)  # the author's constant H > 0
X = sp.symbols("x1:9", real=True)  # the coordinates x1, ..., x8
a4 = sp.Function("a4")(X[3])  # the unknown function a4(x4)
z = 6 * H * X[7]  # z = 6 H x8
warp = sp.sin(z) ** sp.Rational(1, 3)  # sin(z)^(1/3)
```

`sp.Symbol` makes a symbol that sympy computes with exactly; `positive=True` tells sympy that $H > 0$. `sp.symbols("x1:9")` makes the eight symbols `x1` to `x8` (the range 1 to 8), stored in the tuple `X`, so `X[3]` is $x_4$ and `X[7]` is $x_8$. `sp.Function("a4")(X[3])` is an unknown function of $x_4$, which sympy can differentiate. `sp.Rational(1, 3)` is the exact fraction $1/3$, so `warp` is $\sin^{1/3}z$.

```python
METRIC = ([sp.exp(2 * a4) * warp] * 3 + [sp.Integer(-1)]
          + [-sp.exp(-2 * a4) * warp] * 3 + [sp.cot(z) ** 2])  # g_11 ... g_88
```

The diagonal of the author's metric as a list of eight entries: a list multiplied by 3 repeats it three times, and `+` joins lists. So `METRIC[0]` to `METRIC[2]` are $e^{2a_4}\sin^{1/3}z$, `METRIC[3]` is $-1$, `METRIC[4]` to `METRIC[6]` are $-e^{-2a_4}\sin^{1/3}z$, and `METRIC[7]` is $\cot^2z$.

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
            if value != 0:
                christoffel[a, b, c] = value / (2 * METRIC[a])  # times g^aa / 2
```

The Christoffel formula of Section 11.10 for a diagonal metric: $\partial_bg_{ac}$ is nonzero only for $c = a$, $\partial_cg_{ab}$ only for $b = a$, and $\partial_ag_{bc}$ only for $c = b$. The three `if` lines add exactly these terms (`sp.diff(f, x)` is the exact derivative of `f` with respect to `x`). A nonzero result is divided by $2g_{aa}$, which is the factor $\frac12 g^{aa}$, and stored under the key `(a, b, c)`.

```python
def gamma(a, b, c):
    return christoffel.get((a, b, c), 0)


christoffel_b_le_c = [key for key in christoffel if key[1] <= key[2]]
report("nonzero Christoffel symbols Gamma^a_bc with b <= c", len(christoffel_b_le_c))
check(all(christoffel.get((a, c, b)) == value
          for (a, b, c), value in christoffel.items()),
      "Gamma^a_bc = Gamma^a_cb (symmetric in the lower labels)")
```

`gamma(a, b, c)` returns a symbol, or 0 when it is not stored. The list `christoffel_b_le_c` keeps the symbols with $b \le c$; there are 25 (RESULT line), the 25 of the record (Section 3.23). The check confirms the symmetry $\Gamma^a{}_{bc} = \Gamma^a{}_{cb}$. Eighth PASS line.

**In [7], the Riemann tensor with sympy.**

```python
A1, A2, C = sp.symbols("A1 A2 C")  # a4', a4'' and cot(z)
SYMBOLS = {sp.Derivative(a4, (X[3], 2)): A2, sp.Derivative(a4, X[3]): A1}
RIEMANN = {}  # (a, b, c, d) -> R^ab_cd in the symbols H, A1, A2, C
```

Three plain symbols stand for $a_4'$, $a_4''$ and $\cot z$. The dictionary `SYMBOLS` says which derivative becomes which symbol (the second derivative is listed first, so that it is replaced before the first derivative inside it). `RIEMANN` will hold the nonzero components.

```python
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
```

The formula of Section 11.10 for $R^a{}_{bcd}$, for all $8^4 = 4096$ combinations of labels: two derivative terms and the sum over $e$ of the two products. `continue` skips to the next combination when the result is exactly zero.

```python
                value = sp.simplify((value / METRIC[b]).subs(SYMBOLS))  # R^ab_cd
                value = sp.expand(value.subs({sp.tan(z): 1 / C, sp.cot(z): C,
                                              sp.cos(z): C * sp.sin(z)}))
                if value != 0:
                    RIEMANN[a, b, c, d] = value
report("nonzero components R^ab_cd", len(RIEMANN))
```

Dividing by $g_{bb}$ raises the second label: $R^{ab}{}_{cd} = R^a{}_{bcd}/g_{bb}$. `.subs(SYMBOLS)` puts `A1` and `A2` in place of the derivatives, and `sp.simplify` simplifies (this takes most of the cell's ten seconds). Then $\tan z$, $\cot z$ and $\cos z$ are written with the symbol `C` ($\tan z = 1/C$, $\cos z = C\sin z$), and `sp.expand` multiplies out. The nonzero results are stored: 156 of them (RESULT line), as Section 11.10 counted.

```python
check(all(v.free_symbols <= {H, A1, A2, C} for v in RIEMANN.values()),
      "every R^ab_cd is a polynomial in H, a4', a4'' and cot z and its inverse, free "
      "of sin(z)^(1/3) and e^a4",
      record=f"{RESULTS}/lovelock-report.json, check mixed_riemann_free_of_sin_third")
```

`v.free_symbols` is the set of symbols in a component; `<=` between two sets means "is contained in". If any component still contained $x_8$ (through $\sin z$) or $x_4$ (through $e^{a_4}$), the check would fail. Ninth PASS line.

**In [8], sympy against the Rust record.**

```python
curvature = json.loads((OUT_FOLDER / "curvature.json").read_text(encoding="utf-8"))
NAMES = curvature["coordinates"]  # ["x1", ..., "x8"]


def from_mathematica(text):
    text = re.sub(r"Derivative\[(\d)\]\[a4\]\[x4\]", r"A\1", text)  # a4' -> A1
    text = text.replace("Cot[6*H*x8]", "C").replace("^", "**")
    return sp.sympify(text, locals={"H": H, "A1": A1, "A2": A2, "C": C})
```

The program's file `curvature.json` is read; its list of coordinate names becomes `NAMES`. `from_mathematica` turns a component written in Mathematica's notation, for example `H*Derivative[1][a4][x4]*Cot[6*H*x8]^(-1)`, into a sympy expression: `re.sub` replaces `Derivative[1][a4][x4]` by `A1` and `Derivative[2][a4][x4]` by `A2` (the group `(\d)` captures the digit and `\1` puts it back), $\cot z$ becomes `C`, Mathematica's power sign `^` becomes Python's `**`, and `sp.sympify` reads the text with the four names bound to our symbols.

```python
rust_riemann = {}
for item in curvature["riemannMixedNonzero"]:
    a, b = (NAMES.index(name) for name in item["up"])
    c, d = (NAMES.index(name) for name in item["down"])
    rust_riemann[a, b, c, d] = from_mathematica(item["value"])
same_values = set(rust_riemann) == set(RIEMANN) and all(
    sp.expand(RIEMANN[key] - rust_riemann[key]) == 0 for key in RIEMANN)
check(same_values, "sympy and Rust give the same 156 nonzero R^ab_cd exactly",
      record="Revision/gkd_lovelock/results/python-lovelock-report.json, "
             "check rust_riemann_agrees")
```

Each of the record's nonzero components carries its upper pair, its lower pair and its value; `NAMES.index(name)` turns a name into its number. The check requires the same set of label combinations (a set of the keys of a dictionary) and an exactly vanishing difference for every component. Tenth PASS line.

```python
antisymmetric = all(sp.expand(v + RIEMANN.get((b, a, c, d), 0)) == 0 and
                    sp.expand(v + RIEMANN.get((a, b, d, c), 0)) == 0
                    for (a, b, c, d), v in RIEMANN.items())
check(antisymmetric, "R^ab_cd = -R^ba_cd = -R^ab_dc for all components",
      record=f"{RESULTS}/lovelock-report.json, check riemann_antisymmetry")
check(len(christoffel_b_le_c) == len(curvature["christoffelNonzero_b_le_c"]) == 25,
      "25 nonzero Christoffel symbols with b <= c, as in the record")
```

The antisymmetry of Section 11.10: each component plus the component with the upper pair exchanged, and plus the one with the lower pair exchanged, must vanish. The second check compares the number of Christoffel symbols with the record's list (`a == b == 25` tests both equalities). PASS lines eleven and twelve.

```python
ricci_scalar = sp.expand(sum(RIEMANN.get((a, b, a, b), 0) for a in range(8)
                             for b in range(8)))
report("Ricci scalar R", ricci_scalar)
check(sp.expand(ricci_scalar - from_mathematica(curvature["ricciScalar"])) == 0,
      "the Ricci scalar is R = 6 a4'^2 - 42 H^2, as in the record",
      record=f"{RESULTS}/curvature.json, ricciScalar")
```

$R = \sum_{a,b}R^{ab}{}_{ab}$, twice the sum of the 28 plane curvatures. The RESULT line prints `6*A1**2 - 42*H**2`, and the check compares it with the record. Thirteenth PASS line.

**In [9], the plane curvatures (Figure 11b.2).**

```python
def value_at(expr, h=1.0, a1=2.0, a2=0.0, cot=1.0):
    return float(sp.sympify(expr).subs({H: h, A1: a1, A2: a2, C: cot}))
```

`value_at` puts numbers in place of the four symbols (by default $H = 1$, $a_4' = 2$, $a_4'' = 0$, $\cot z = 1$) and returns a decimal number; `sp.sympify` also accepts the plain 0 of a missing component.

```python
fig, axes = plt.subplots(1, 2, figsize=(11.0, 5.0))
planes = {}
for ax, a2 in zip(axes, (0.0, 1.0)):
    table = np.array([[value_at(RIEMANN.get((a, b, a, b), 0), a2=a2)
                       for b in range(8)] for a in range(8)])
    planes[a2] = table
    picture = ax.imshow(table, cmap="RdBu_r", vmin=-6, vmax=6)
```

Two panels, for $a_4'' = 0$ and $a_4'' = H^2$. Each `table` is the $8 \times 8$ array of the plane curvatures $K(a, b) = R^{ab}{}_{ab}$ (zero on the diagonal); it is kept in `planes` for the check and drawn with the colour map `RdBu_r` (red positive, blue negative) from $-6$ to 6.

```python
    for a in range(8):
        for b in range(8):
            if a != b:
                ax.text(b, a, f"{table[a, b]:g}", ha="center", va="center",
                        fontsize=8)
    ax.set_xticks(range(8), NAMES)
    ax.set_yticks(range(8), NAMES)
    ax.set_title(f"$a_4' = 2H$, $a_4'' = {a2:g}\\,H^2$")
    ax.grid(False)
fig.colorbar(picture, ax=list(axes), shrink=0.8, label="$K(a, b)$ in units of $H^2$")
```

The values off the diagonal are written into the squares (the format `:g` writes a number without needless zeros), the rows and columns get the coordinate names, each panel its title, and one colour bar serves both panels.

```python
save_figure(fig, "curvature_of_planes",
            "The curvature $K(a, b) = R^{ab}_{\\ ab}$ of the plane of the coordinate "
            ...)
check(planes[0.0][0, 1] == 3.0 and planes[0.0][0, 4] == -5.0
      and planes[0.0][0, 7] == -1.0 and planes[1.0][0, 3] == 5.0
      and planes[1.0][4, 3] == 3.0 and planes[0.0][3, 7] == 0.0,
      "plane curvatures at a4' = 2H: 3, -5, -1; with x4: 4 + a4'' and 4 - a4''; "
      "x4 with x8: 0")
```

After saving, the check reads six entries: $K(x_1, x_2) = 4 - 1 = 3$, $K(x_1, x_5) = -(4 + 1) = -5$, $K(x_1, x_8) = -1$, $K(x_1, x_4) = 4 + 1 = 5$ and $K(x_5, x_4) = 4 - 1 = 3$ at $a_4'' = H^2$, and $K(x_4, x_8) = 0$ (in units of $H^2$), the table of Section 11.10. Fourteenth PASS line.

*What Figure 11b.2 shows.* Two $8 \times 8$ tables of the plane curvatures in units of $H^2$. Red blocks of 3 inside 3-space and inside the extra times, blue blocks of $-5$ between them, light blue $-1$ for every plane with $x_8$, and 0 for the plane of $x_4$ and $x_8$. The row and column of $x_4$ hold 4 on the left; on the right, with $a_4'' = H^2$, they hold 5 towards 3-space and 3 towards the extra times: the acceleration of $a_4$ enters 3-space and the extra times with opposite signs.

**In [10], the whole Riemann tensor (Figure 11b.3).**

```python
point = {"h": 1.0, "a1": 2.0, "a2": 1.0, "cot": 1.0 / np.sqrt(3.0)}
whole = np.zeros((64, 64))
for (a, b, c, d), value in RIEMANN.items():
    whole[8 * a + b, 8 * c + d] = value_at(value, **point)
```

The point $H = 1$, $a_4' = 2$, $a_4'' = 1$, $z = \pi/3$, where $\cot z = 1/\sqrt 3$. `np.zeros((64, 64))` is a $64 \times 64$ array of zeros; every nonzero component is put into row $8a + b$ (the upper pair) and column $8c + d$ (the lower pair). `**point` passes the four entries of the dictionary as the named arguments of `value_at`.

```python
fig, ax = plt.subplots(figsize=(6.8, 6.2))
largest = np.abs(whole).max()
picture = ax.imshow(whole, cmap="RdBu_r", vmin=-largest, vmax=largest)
for edge in range(8, 64, 8):  # lines between the blocks
    ax.axhline(edge - 0.5, color="0.8", lw=0.5)
    ax.axvline(edge - 0.5, color="0.8", lw=0.5)
```

The colour scale runs from minus to plus the largest size, so that 0 is white. Thin grey lines separate the blocks of eight rows and columns that share their first label.

```python
ticks = list(range(3, 64, 8))  # the middle of each block
ax.set_xticks(ticks, [f"c = {name}" for name in NAMES], rotation=90, fontsize=8)
ax.set_yticks(ticks, [f"a = {name}" for name in NAMES], fontsize=8)
ax.set_xlabel("lower pair $(x_c, x_d)$, column $8c + d$")
ax.set_ylabel("upper pair $(x_a, x_b)$, row $8a + b$")
ax.set_title("All components $R^{ab}{}_{cd}$ at one point")
ax.grid(False)
fig.colorbar(picture, ax=ax, shrink=0.8, label="value (units of $H^2$)")
save_figure(fig, "riemann_matrix",
            "All 4096 components of the Riemann tensor $R^{ab}_{\\ \\ cd}$ of the "
            ...)
check(int(np.count_nonzero(whole)) == 156,
      "156 of the 4096 components are not zero at this point")
```

Marks at the middle of each block, axis titles, title, colour bar and the saved figure; the check counts the nonzero entries of the array: 156 (`np.count_nonzero`). Fifteenth PASS line.

*What Figure 11b.3 shows.* A $64 \times 64$ table, mostly white. Along the main diagonal ($a = c$, $b = d$) lie the plane curvatures; along the second diagonal pattern ($a = d$, $b = c$) their sign-reversed copies. The scattered squares away from these lines are the 48 components that mix $x_4$ and $x_8$, such as $R^{x_1x_4}{}_{x_1x_8} = Ha_4'\cot z$.

**In [11], the mixed terms cancel (Figure 11b.4).**

```python
mixing = [sp.expand(RIEMANN.get((3, c, 7, c), 0)) for c in range(7)]  # c = x1..x7
for c, term in enumerate(mixing):
    say(f"R^(x4 {NAMES[c]})_(x8 {NAMES[c]}) = {term}")
total = sp.expand(sum(mixing))
say(f"sum over c = {total}")
```

The seven terms $R^{x_4c}{}_{x_8c}$ of the Ricci component $R^{x_4}{}_{x_8}$, for $c = x_1$ to $x_7$ (numbers 3 and 7 are $x_4$ and $x_8$). The output: `A1*C*H` three times, 0 for $c = x_4$, `-A1*C*H` three times, and the sum 0, as derived in Section 11.10.

```python
fig, ax = plt.subplots(figsize=(7.0, 4.0))
heights = [value_at(term, h=1.0, a1=1.0, cot=1.0) for term in mixing]
colours = ["tab:red"] * 3 + ["0.6"] + ["tab:blue"] * 3
ax.bar(NAMES[:7], heights, color=colours)
ax.text(3, 0.05, "0", ha="center", va="bottom")  # the term of c = x4 is zero
ax.axhline(0.0, color="black", lw=0.8)
```

The seven terms at $H = 1$, $a_4' = 1$, $\cot z = 1$ as bars, red for 3-space, grey for $x_4$, blue for the extra times; `NAMES[:7]` are the first seven names. A small "0" marks the bar of height zero, and a black line marks the value 0.

```python
ax.set_xlabel("the direction $c$ of the term $R^{x_4 c}{}_{x_8 c}$")
ax.set_ylabel("value (units of $H^2$)")
ax.set_title(f"Seven terms of $R^{{x_4}}{{}}_{{x_8}}$; their sum is {total}")
save_figure(fig, "mixing_terms_cancel",
            "The seven terms $R^{x_4 c}_{\\ \\ x_8 c}$, $c = x_1$ to $x_7$, whose sum "
            ...)
check(total == 0 and sp.expand(mixing[0] - H * A1 * C) == 0,
      "the seven terms of R^x4_x8 are +H a4' cot z (three times), -H a4' cot z (three "
      "times) and 0, and cancel exactly")
```

In an f-string a doubled brace `{{` prints one brace, so the title reads $R^{x_4}{}_{x_8}$ followed by the sum. The check requires the sum to be exactly 0 and the first term to be $Ha_4'\cot z$. Sixteenth PASS line.

*What Figure 11b.4 shows.* Three red bars of height $+1$ ($x_1, x_2, x_3$), a grey bar of height 0 ($x_4$) and three blue bars of height $-1$ ($x_5, x_6, x_7$), in units of $H^2$: the three inflating and the three deflating directions cancel exactly.

**In [12], exact polynomial arithmetic and GKD.**

```python
from fractions import Fraction  # exact fractions of whole numbers

ONE = {(0, 0, 0, 0): Fraction(1)}  # the polynomial 1
```

From here on the notebook computes with its own exact polynomials, independent of sympy's: a polynomial in $H, A_1, A_2, C$ is a dictionary from the exponents $(e_H, e_{A_1}, e_{A_2}, e_C)$ of each monomial to its coefficient, a `Fraction` (an exact fraction of whole numbers); $e_C$ may be negative. `ONE` is the polynomial 1.

```python
def poly_mul(p, q):
    out = {}
    for m1, c1 in p.items():
        for m2, c2 in q.items():
            m = (m1[0] + m2[0], m1[1] + m2[1], m1[2] + m2[2], m1[3] + m2[3])
            out[m] = out.get(m, 0) + c1 * c2
    return {m: c for m, c in out.items() if c != 0}
```

The product of two polynomials (docstring left out): every monomial of the first times every monomial of the second, which adds the exponents and multiplies the coefficients; equal monomials are collected, and monomials whose coefficient became 0 are dropped.

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
    poly = sp.Poly(sp.expand(expr * C ** 8), H, A1, A2, C)
    return {(m[0], m[1], m[2], m[3] - 8): Fraction(int(v.p), int(v.q))
            for m, v in zip(poly.monoms(), poly.coeffs())}
```

`to_poly` turns a sympy expression into this form. `sp.Poly` needs non-negative powers, so the expression is first multiplied by $C^8$ (no component has a power of $C$ below $-8$); `poly.monoms()` lists the exponents and `poly.coeffs()` the coefficients of the monomials; 8 is subtracted from the exponent of $C$ again, and each sympy fraction `v` becomes a `Fraction` of its numerator `v.p` and denominator `v.q`.

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
ENTRIES = [(key, to_poly(RIEMANN[key])) for key in sorted(RIEMANN)]  # 156 entries
LOWER_MASK = np.array([(1 << a) | (1 << b) for (a, b, c, d), _ in ENTRIES])
UPPER_MASK = np.array([(1 << c) | (1 << d) for (a, b, c, d), _ in ENTRIES])
```

The 156 nonzero entries, sorted by their labels, each with its polynomial. For each entry $R^{ab}{}_{cd}$ the bit masks of Section 11.12 are stored: its upper labels $a, b$ go into the delta's LOWER list and its lower labels $c, d$ into the delta's UPPER list. The operator written with two less-than signs shifts the number 1 to the left by the given number of places, so it is $2^a$; the vertical bar is the bitwise OR, so the mask of $\{a, b\}$ is $2^a + 2^b$. `np.array` holds the 156 masks, so that one comparison can test all of them at once.

```python
report("nonzero curvature entries in the sums", len(ENTRIES))
check(gkd([0, 1, 2], [1, 2, 0]) == 1 and gkd([0, 1], [1, 0]) == -1,
      "gkd: a cycle of three labels is even (+1), an exchange of two odd (-1)",
      record=f"{RESULTS}/lovelock-report.json, gkdSelfCheck")
```

RESULT: 156 entries. The check repeats the two values that the Rust program records for itself in the field `gkdSelfCheck` of its report: $+1$ for the cycle $(0, 1, 2) \to (1, 2, 0)$ and $-1$ for one exchange. Seventeenth PASS line.

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

A combination with fewer than $k$ entries is extended (step 2 of Section 11.12). `LOWER_MASK & lower_mask` is computed for all 156 entries at once; `== 0` marks the entries that share no label with the lower list so far, and the same for the upper list; `&` between the two true/false arrays keeps the entries that pass both tests, and `np.nonzero(...)[0]` lists their numbers. Each such entry is appended to the combination, and the masks grow by its labels (bitwise OR).

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

For each order the tensor and the scalar are computed (about ten seconds, mostly for $k = 3$), and the counters are stored and printed: 5616, 176640, 1128960 leaves; 696, 32640, 495360 GKD calls; 108, 7200, 213120 scalar calls; and 8 nonzero components for every order.

```python
same_counters = all(
    MY_COUNTERS[k] == (COUNTERS[k]["leaves"], COUNTERS[k]["gkdCalls"],
                       COUNTERS[k]["scalarGkdCalls"])
    and COUNTERS[k]["gkdNonzero"] == COUNTERS[k]["gkdCalls"]
    and len(P[k]) == COUNTERS[k]["nonzeroComponents"] for k in (1, 2, 3))
check(same_counters, "the Python sums reproduce the counters of the Rust sums",
      record=f"{RESULTS}/lovelock-report.json, counters k = 1, 2, 3")
```

The Python search, written independently, finds exactly the counters of the Rust search, every GKD call of the record is nonzero, and the numbers of nonzero components agree. Eighteenth PASS line.

**In [15], every component against the record.**

```python
tensors = json.loads((OUT_FOLDER / "lovelock-tensors.json").read_text(
    encoding="utf-8"))


def from_monomials(monomials):
    out = {}
    for numerator, denominator, e in monomials:
        if e[3] or e[4] or e[5] or e[6]:  # 3rd, 4th derivative, e^a4 or sin^(1/3)
            raise ValueError("unexpected symbol in a Lovelock component")
        out[(e[0], e[1], e[2], e[7])] = Fraction(numerator, denominator)
    return out
```

The program's file lists every component as exact monomials, each a numerator, a denominator and eight exponents (of $H$, $a_4'$, $a_4''$, $a_4'''$, $a_4''''$, $e^{a_4}$, $\sin^{1/3}z$, $\cot z$). `from_monomials` rebuilds a component as a polynomial dictionary; if any of the exponents 3 to 6 were not 0 it would stop, so the components contain only $H$, $a_4'$, $a_4''$ and $\cot z$.

```python
agree = {}
for k in (1, 2, 3):
    block = tensors[f"P{k}_mixed_up_h_down_j"]
    agree[k] = all(from_monomials(block[f"{NAMES[h]},{NAMES[j]}"]["monomials"])
                   == P[k].get((h, j), {}) for h in range(8) for j in range(8))
    nonzero = " ".join(sorted(f"{NAMES[h]},{NAMES[j]}" for h, j in P[k]))
    say(f"k = {k}: nonzero components (h, j): {nonzero}")
```

For each order the record's 64 components, stored under keys such as `"x1,x1"`, are compared exactly with the Python components (a missing Python component is the empty polynomial, zero). The nonzero components are printed: for every order only the eight diagonal ones, $x_1x_1$ to $x_8x_8$.

```python
check(all(agree.values()),
      "all 3 x 64 components of P(1), P(2), P(3) equal the Rust components exactly",
      record="Revision/gkd_lovelock/results/python-lovelock-report.json, checks "
             "rust_k1_mixed_components_agree, rust_k2_mixed_components_agree and "
             "rust_k3_mixed_components_agree")
scalars_agree = all(to_poly(from_mathematica(tensors[f"L{k}"])) == L[k]
                    for k in (1, 2, 3))
check(scalars_agree, "the scalars L(1), L(2), L(3) equal the Rust scalars exactly",
      record="Revision/gkd_lovelock/results/python-lovelock-report.json, checks "
             "rust_L1_agrees, rust_L2_agrees and rust_L3_agrees")
check(all(set(P[k]) == {(h, h) for h in range(8)} for k in (1, 2, 3)),
      "only the 8 diagonal components are nonzero, for k = 1, 2, 3")
```

Three checks: all $3 \times 64$ components agree exactly; the three scalars of the record (in Mathematica text, read with `from_mathematica`) equal the Python scalars; and the nonzero components are exactly the eight diagonal ones (a set comprehension in braces). PASS lines nineteen to twenty-one. In particular no Lovelock tensor has an $x_4$-$x_8$ component.

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

`literal_sum` does NOT skip anything: `itertools.product(range(156), repeat=k)` runs through all $156^k$ ordered lists of $k$ entries, and for each the two lists of the delta are built.

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

For the scalar and for each of the 64 pairs, GKD is called on the complete lists, with no test before the call: $65\cdot 156^k$ calls. Nonzero values are added to the weights as before.

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

For $k = 1$ and 2 the literal sum is computed (about 15 seconds in all), and the number of calls stated in the record's check text (the digits before "kdelta calls") is read. Output: 10140 and 1581840 calls, both equal to the record.

```python
    same = (literal.pop(None, {}) == L[k]
            and all(literal.get(hj, {}) == P[k].get(hj, {})
                    for hj in set(literal) | set(P[k])))
    check(same and calls == recorded_calls == 65 * 156 ** k
          and recorded["verdict"] == "PASS",
          f"the literal sum of order {k}, without skipping, gives the same P({k}) "
          f"and L({k})",
          record="Revision/gkd_lovelock/results/python-lovelock-report.json, check "
                 f"k{k}_unpruned_literal_sum_agrees")
```

`literal.pop(None, {})` takes the scalar out of the result; it must equal $L_{(k)}$, and every component, over the union (`|`) of the components of both results, must equal $P_{(k)}$. The check also requires the number of calls to be $65\cdot 156^k$ and the record's verdict PASS. PASS lines twenty-two and twenty-three: the skipping changes nothing.

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

The extension step as before. Since every leaf of order 3 already uses seven different lower labels, a fourth entry would need nine different labels out of eight; together with the record's counter of 0 leaves for $k = 4$ the check confirms $P_{(4)} = 0$. Twenty-fourth PASS line.

**In [18], order 1 is Einstein's tensor.**

```python
RM = dict(ENTRIES)  # (a, b, c, d) -> R^ab_cd as a polynomial dict


def poly_sum(polynomials):
    total = {}
    for p in polynomials:
        total = poly_add(total, p)
    return total
```

`RM` is the dictionary of the 156 entries; `poly_sum` adds a list of polynomials (docstring left out).

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
check(all(P[1].get(hj, {}) == poly_mul({(0, 0, 0, 0): Fraction(-4)}, EINSTEIN[hj])
          for hj in EINSTEIN) and L[1] == poly_add({}, R_SCALAR, 2),
      "P(1) = -4 G for all 64 components and L(1) = 2 R",
      record="Revision/gkd_lovelock/results/python-lovelock-report.json, checks "
             "k1_equals_minus_4_einstein and L1_equals_2R")
```

The check of Section 11.14: every component of $P_{(1)}$ equals $-4$ times the Einstein component (the constant polynomial $-4$ times $G$), and $L_{(1)} = 2R$. Twenty-fifth PASS line.

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
        two_h[h, j] = poly_add(poly_mul({(0, 0, 0, 0): Fraction(4)}, t),
                               poly_mul(delta[h, j], GB), -1)
```

For each pair $(h, j)$ the four sums of Lanczos's tensor (Section 11.15) are collected in `t`: $R\,R^h{}_j$, then $-2\sum_aR^h{}_aR^a{}_j$, then $-2\sum_{a,b}R^{ha}{}_{jb}R^b{}_a$, then $\sum R^{ha}{}_{bc}R^{bc}{}_{ja}$ over the entries with first label $h$ (the name `hh` is the entry's first label). Finally $2\mathcal{H}^h{}_j = 4t - \delta^h_j\,\mathrm{GB}$.

```python
check(all(P[2].get(hj, {}) == poly_mul({(0, 0, 0, 0): Fraction(-4)}, two_h[hj])
          for hj in two_h) and L[2] == poly_add({}, GB, 4),
      "P(2) = -8 times the Gauss-Bonnet tensor for all 64 components and L(2) = 4 GB",
      record="Revision/gkd_lovelock/results/python-lovelock-report.json, checks "
             "k2_equals_minus_8_gauss_bonnet and L2_equals_4_gauss_bonnet")
```

$-4\cdot 2\mathcal{H} = -8\mathcal{H}$ must equal $P_{(2)}$ in all 64 components, and $L_{(2)} = 4\,\mathrm{GB}$: the result derived by hand in Section 11.15. Twenty-sixth PASS line.

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

The cubic density with the record's coefficients, and the check $L_{(3)} = 8\times$ density. Twenty-seventh PASS line.

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

$Y_{(k)}$ for the three orders, and the check of the expansion $P_{(k)} = \delta L_{(k)} - 2kY_{(k)}$ in all $3 \times 64$ components, together with $Y_{(1)} = 2\,\mathrm{Ric}$ of Section 11.14. Twenty-eighth PASS line.

**In [22], the trace identity.**

```python
def show(p):
    return str(sp.expand(sum(v * H ** m[0] * A1 ** m[1] * A2 ** m[2] * C ** m[3]
                             for m, v in p.items())))
```

`show` turns a polynomial dictionary back into sympy text, for printing (docstring left out).

```python
for k in (1, 2, 3):
    trace = poly_sum(P[k].get((h, h), {}) for h in range(8))
    report(f"Lovelock scalar L({k})", show(L[k]))
    check(trace == poly_add({}, L[k], 8 - 2 * k),
          f"the trace of P({k}) is (8 - {2 * k}) L({k})",
          record=f"{RESULTS}/lovelock-report.json, check k{k}_trace_identity")
```

For each order the trace $\sum_hP_{(k)}{}^h{}_h$ is formed, the scalar is printed, and the trace identity of Section 11.14 is checked. The RESULT lines give $L_{(1)} = 12a_4'^2 - 84H^2$, $L_{(2)} = -96a_4'^4 - 2112a_4'^2H^2 + 3360H^4$ and $L_{(3)} = 1152a_4'^6 + 31104a_4'^4H^2 + 100224a_4'^2H^4 - 40320H^6$; no $a_4''$ and no $\cot z$ appear. PASS lines twenty-nine to thirty-one.

**In [23], the components at one moment (Figure 11b.5).**

```python
def poly_value(p, h, a1, a2, cot=1):
    total = Fraction(0)
    for (e_h, e_1, e_2, e_c), coefficient in p.items():
        total += (coefficient * Fraction(h) ** e_h * Fraction(a1) ** e_1
                  * Fraction(a2) ** e_2 * Fraction(cot) ** e_c)
    return total
```

`poly_value` evaluates a polynomial dictionary exactly, with fractions, at given values of $H$, $a_4'$, $a_4''$ and $\cot z$ (docstring left out).

```python
fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.6))
tables = {}
for ax, k in zip(axes, (1, 2, 3)):
    scale = Fraction(-1, 2 ** (k + 1))  # E_(k) = -P_(k) / 2^(k+1)
    # every component at a4' = 2H, a4'' = H^2 with H = 1, exactly, then as a decimal
    table = np.array([[float(scale * poly_value(P[k].get((h, j), {}), 1, 2, 1))
                       for j in range(8)] for h in range(8)])
    tables[k] = table
    largest = np.abs(table).max()
    ax.imshow(table, cmap="RdBu_r", vmin=-largest, vmax=largest)
```

Three panels, one per order. Each component of $E_{(k)} = -P_{(k)}/2^{k+1}$ is evaluated exactly at $H = 1$, $a_4' = 2$, $a_4'' = 1$ (the moment $a_4' = 2H$, $a_4'' = H^2$; the components contain no $\cot z$), turned into a decimal number, and the $8 \times 8$ table is drawn with its own colour scale.

```python
    for h in range(8):
        for j in range(8):
            if h != j:
                colour = "0.6"  # grey zeros off the diagonal
            elif abs(table[h, j]) > 0.6 * largest:
                colour = "white"  # white on the darkest squares, to stay readable
            else:
                colour = "black"
            ax.text(j, h, f"{table[h, j]:g}", ha="center", va="center",
                    fontsize=6.5 if h == j else 6, color=colour)
```

Every value is written into its square: grey for the zeros off the diagonal, white on the darkest squares and black elsewhere.

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
    np.count_nonzero(tables[k] - np.diag(np.diag(tables[k]))) == 0
    and tables[k][0, 0] == tables[k][1, 1] == tables[k][2, 2]
    and tables[k][4, 4] == tables[k][5, 5] == tables[k][6, 6]
    and tables[k][7, 7] == (tables[k][0, 0] + tables[k][4, 4]) / 2
    for k in (1, 2, 3))
```

`np.diag(table)` takes the diagonal of a table, and `np.diag` of that diagonal builds a table with only this diagonal; their difference is the part off the diagonal, which must have no nonzero entry. Further, the three space entries must be equal, the three extra-time entries equal, and the hidden entry their mean.

```python
say("diagonals (x1 ... x8): " + "; ".join(
    f"E({k}): " + " ".join(f"{v:g}" for v in np.diag(tables[k])) for k in (1, 2, 3)))
check(diagonal_ok and list(np.diag(tables[1])) == [4, 4, 4, 33, 2, 2, 2, 3],
      "at a4' = 2H, a4'' = H^2: only diagonal entries, space and extra-time entries "
      "equal, hidden entry their mean; G = diag(4, 4, 4, 33, 2, 2, 2, 3) H^2")
```

The three diagonals are printed: $E_{(1)}$: 4, 4, 4, 33, 2, 2, 2, 3; $E_{(2)}$: 548, 548, 548, $-1476$, 820, 820, 820, 684; $E_{(3)}$: $-14544$ (three times), 40248, $-30240$ (three times), $-22392$. With the Einstein tensor of Section 11.10 and $a_4' = 2H$, $a_4'' = H^2$: $G^{x_1}{}_{x_1} = -12 + 1 + 15 = 4$, $G^{x_4}{}_{x_4} = 12 + 21 = 33$, $G^{x_5}{}_{x_5} = -12 - 1 + 15 = 2$, $G^{x_8}{}_{x_8} = 15 - 12 = 3$, in units of $H^2$, which the check confirms. Thirty-second PASS line.

*What Figure 11b.5 shows.* Three $8 \times 8$ tables in units of $H^2$, $H^4$ and $H^6$, each filled only on its diagonal. In each table the first three diagonal squares are equal (3-space), the squares 5 to 7 are equal (extra times), and the last square (hidden direction) lies exactly halfway between them: $(4 + 2)/2 = 3$, $(548 + 820)/2 = 684$, $(-14544 - 30240)/2 = -22392$. The time square $x_4$ stands apart, with the opposite sign in all three tables. Section 11.21 proves these patterns for every history.

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

The helper of Notebook 11a, In [16]: for one report, a dictionary from the name of each check to PASS or FAIL, for both forms in which the reports store their checks.

```python
QUOTED = {  # report -> the checks that this notebook quotes from it
    "python-lovelock-report.json": [
        "rust_riemann_agrees", "rust_k1_mixed_components_agree",
        ...
        "normalisation_P2_derived_minus_8", "normalisation_L3_cubic_derived"],
    "lovelock-report.json": [
        "riemann_antisymmetry", "mixed_riemann_free_of_sin_third",
        ...
        "k4_tensor_vanishes", "k1_brute_force_numeric", "k2_brute_force_numeric"],
}
```

(Shortened here; the full lists are in Section 11.18.) The 17 checks quoted from the sympy report and the 8 quoted from the Rust report.

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

For each report the list `missing` collects every quoted check that is absent or not PASS; it is printed ("none") and must be empty (`not missing` is true for an empty list). PASS lines thirty-three and thirty-four.

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

The numbers of checks of the two verification reports are read and printed: 49 checks, 0 failed, verdict SUCCESS for the sympy report, and 29, 0, SUCCESS for the Wolfram report.

```python
check(totals == {"python-lovelock-report.json": (49, 0, "SUCCESS"),
                 "wolfram-gkd-report.json": (29, 0, "SUCCESS")},
      "the sympy verification has 49 checks and the Wolfram verification 29, none "
      "failed",
      record=f"{RESULTS}/python-lovelock-report.json and wolfram-gkd-report.json, "
             "checkCount and failedCheckCount")
```

The counts quoted in the notebook's text are fixed by this check, so a later change of either report would be noticed. Thirty-fifth PASS line.

**In [25], the end.**

```python
figure_files = [f"11b_{k}_{name}.png" for k, name in enumerate(
    ["work_of_the_sums", "curvature_of_planes", "riemann_matrix",
     "mixing_terms_cancel", "lovelock_component_tables"], 1)]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_files),
      "all five figure files of the notebook exist")
all_checks_passed()
```

As in Notebook 11a, In [17]: the five figure files must exist (thirty-sixth PASS line), and the last line is ALL 36 CHECKS PASSED (notebook 11b). The 36 checks are: 2 in In [3], 4 in In [4], 1 each in In [5], In [6] and In [7], 4 in In [8], 1 each in In [9] to In [12], 1 in In [14], 3 in In [15], 2 in In [16], 1 each in In [17] to In [21], 3 in In [22], 1 in In [23], 3 in In [24] and 1 in In [25].

### 11.20 The components of the three tensors for the author's metric

**The result (PROVED by exact computation).** The Rust program of the record computes all $3 \times 64$ components of $P_{(1)}, P_{(2)}, P_{(3)}$ exactly (`Revision/gkd_lovelock/results/lovelock-tensors.json`, keys `P1_mixed_up_h_down_j` to `P3_mixed_up_h_down_j`); the Revision's sympy and Wolfram verifications recompute every one of them independently and find the same (`python-lovelock-report.json`, checks `rust_k1_mixed_components_agree` to `rust_k3_mixed_components_agree`; `wolfram-gkd-report.json`, checks `k1_P_equals_rust_all_64_components` to `k3_P_equals_rust_all_64_components`), and so does Notebook 11b (In [15]). Only the eight diagonal components are nonzero, for every order. With $E_{(k)} = -P_{(k)}/2^{k+1}$ and the abbreviations $a_4'$, $a_4''$ for the derivatives with respect to the time $x_4$, the independent components are

$$
\begin{aligned}
E_{(1)}{}^{x_1}{}_{x_1} &= -3a_4'^2 + a_4'' + 15H^2, \qquad E_{(1)}{}^{x_4}{}_{x_4} = 3a_4'^2 + 21H^2,\\
E_{(1)}{}^{x_5}{}_{x_5} &= -3a_4'^2 - a_4'' + 15H^2, \qquad E_{(1)}{}^{x_8}{}_{x_8} = -3a_4'^2 + 15H^2,
\end{aligned}
$$

$$
\begin{aligned}
E_{(2)}{}^{x_1}{}_{x_1} &= 12a_4'^4 - 24a_4'^2a_4'' + 168a_4'^2H^2 - 40a_4''H^2 - 180H^4,\\
E_{(2)}{}^{x_4}{}_{x_4} &= -36a_4'^4 - 120a_4'^2H^2 - 420H^4,\\
E_{(2)}{}^{x_5}{}_{x_5} &= 12a_4'^4 + 24a_4'^2a_4'' + 168a_4'^2H^2 + 40a_4''H^2 - 180H^4,\\
E_{(2)}{}^{x_8}{}_{x_8} &= 12a_4'^4 + 168a_4'^2H^2 - 180H^4,
\end{aligned}
$$

$$
\begin{aligned}
E_{(3)}{}^{x_1}{}_{x_1} &= -72a_4'^6 + 360a_4'^4a_4'' - 648a_4'^4H^2 + 432a_4'^2a_4''H^2 - 1944a_4'^2H^4 + 360a_4''H^4 + 360H^6,\\
E_{(3)}{}^{x_4}{}_{x_4} &= 360a_4'^6 + 648a_4'^4H^2 + 1080a_4'^2H^4 + 2520H^6,\\
E_{(3)}{}^{x_5}{}_{x_5} &= -72a_4'^6 - 360a_4'^4a_4'' - 648a_4'^4H^2 - 432a_4'^2a_4''H^2 - 1944a_4'^2H^4 - 360a_4''H^4 + 360H^6,\\
E_{(3)}{}^{x_8}{}_{x_8} &= -72a_4'^6 - 648a_4'^4H^2 - 1944a_4'^2H^4 + 360H^6,
\end{aligned}
$$

with $E^{x_2}{}_{x_2} = E^{x_3}{}_{x_3} = E^{x_1}{}_{x_1}$ and $E^{x_6}{}_{x_6} = E^{x_7}{}_{x_7} = E^{x_5}{}_{x_5}$ for every order. These are exactly the components that the record of the field equations of $a_4$ lists (`Revision/field_equations_a4/a4-equations.json`, key `lovelockTensors`, compared in its sympy report `Revision/field_equations_a4/reports/python-a4-report.json`, check `json_lovelock_components`); Notebook 11c reads them from the Rust record and compares them with this list (In [2] and In [3]). The components contain only $H$, $a_4'$ and $a_4''$: no $x_8$ (no $\cot z$ and no $\sin^{1/3}z$), no $e^{a_4}$ and no higher derivative. The order-1 components are those of the Einstein tensor of Section 11.10, as Section 11.14 proved they must be.

**One component checked by hand.** Take the moment $a_4' = 2H$, $a_4'' = H^2$ of a history in which the extra times deflate and the deflation speeds up. In $E_{(2)}{}^{x_1}{}_{x_1}$:

$$
12\cdot 16H^4 - 24\cdot 4H^2\cdot H^2 + 168\cdot 4H^2\cdot H^2 - 40H^2\cdot H^2 - 180H^4 = (192 - 96 + 672 - 40 - 180)H^4 = 548H^4
$$

(insert $a_4'^2 = 4H^2$, $a_4'^4 = 16H^4$, $a_4'' = H^2$; then add the whole numbers). In the same way the diagonals at this moment are $E_{(1)} = (4, 4, 4, 33, 2, 2, 2, 3)H^2$, $E_{(2)} = (548, 548, 548, -1476, 820, 820, 820, 684)H^4$ and $E_{(3)} = (-14544, -14544, -14544, 40248, -30240, -30240, -30240, -22392)H^6$, in the order $x_1, \dots, x_8$ (Notebook 11b, In [23], Figure 11b.5).

### 11.21 Their structure: equal directions, constraint, evolution factor, mean, sign and weight

The components have a clear structure, which Chapter 12 uses at every step. We prove each part by hand from the curvature table of Section 11.10 and from the rule GKD; Notebook 11c confirms every part with exact algebra (In [4]).

**Three tools.** (i) **Relabelling.** If a bijection $\tau$ of the eight labels is applied to every label of both lists of a generalized delta, its matrix does not change, because $\delta(\tau l_i, \tau u_j) = \delta(l_i, u_j)$ ($\tau$ maps equal labels to equal labels and different labels to different labels); so $\delta^{\tau U}_{\tau L} = \delta^U_L$. And because $\tau$ runs through all labels exactly once, a sum over all values of the summed labels is unchanged when every summed label is replaced by its image. (ii) **The label 4 and the acceleration.** Every curvature entry that contains $a_4''$ is a plane entry of a plane $(k, x_4)$, so it carries the label $x_4$ in its upper pair and in its lower pair (Section 11.10). (iii) **The labels 4 and 8 in the mixed entries.** Every mixed entry, such as $R^{x_4k}{}_{x_8k}$ or $R^{x_8k}{}_{x_4k}$, has the label $x_4$ in one of its pairs and $x_8$ in the other; a plane entry has the same two labels in both pairs.

**(a) Only diagonal components (PROVED).** In a term of $P_{(k)}{}^h{}_j$ the delta's lower list is $j$ followed by the upper pairs of the factors, and its upper list is $h$ followed by their lower pairs. A plane entry adds the same two labels to both lists. A mixed entry of the first kind ($x_4$ up, $x_8$ down) adds $x_4$ to the lower list and $x_8$ to the upper list; one of the second kind does the opposite. For a nonzero term the two lists must hold the same labels (case c). If $h \ne j$, the labels $j$ and $h$ must therefore be exactly $x_4$ and $x_8$ in some order, balanced by one more mixed entry of one kind than of the other. So every off-diagonal component other than $P^{x_4}{}_{x_8}$ and $P^{x_8}{}_{x_4}$ vanishes identically. Now take $P^{x_4}{}_{x_8}$: the label $x_8$ stands in the lower list (as $j$) and must appear once in the upper list, and $x_4$ stands in the upper list (as $h$) and must appear once in the lower list; so each term contains exactly one mixed entry, $R^{x_4k}{}_{x_8k}$ or one of its antisymmetric variants, and every other factor avoids both $x_4$ and $x_8$: it is a plane curvature among the six transverse directions, $a_4'^2 - H^2$ or $-(a_4'^2 + H^2)$. Apply the relabelling $\tau$ that exchanges $x_1 \leftrightarrow x_5$, $x_2 \leftrightarrow x_6$, $x_3 \leftrightarrow x_7$ and keeps $x_4$ and $x_8$. It leaves every factor among the transverse directions unchanged (the planes $(i, i')$ and $(j, j')$ have the same curvature, and the planes $(i, j)$ go to planes $(j, i)$), it leaves the delta unchanged (tool i), and it changes the sign of the mixed entry, because $R^{x_4i}{}_{x_8i} = +Ha_4'\cot z$ and $R^{x_4j}{}_{x_8j} = -Ha_4'\cot z$ (Section 11.10). Summing over all relabelled terms is the same sum, so $P^{x_4}{}_{x_8} = -P^{x_4}{}_{x_8}$, hence $P^{x_4}{}_{x_8} = 0$; the same for $P^{x_8}{}_{x_4}$ with the second kind of mixed entry, $R^{x_8i}{}_{x_4i} = -Ha_4'\tan z$ against $R^{x_8j}{}_{x_4j} = +Ha_4'\tan z$. This is the cancellation of three inflating against three deflating directions of Section 11.10, now for every order. The record finds the same eight nonzero components for every order (`wolfram-gkd-report.json`, field `measurements`, entries `k1NonzeroComponents` to `k3NonzeroComponents`).

**(b) The three space directions are alike, and so are the three extra times (PROVED).** The relabelling that exchanges $x_1$ and $x_2$ is a change of coordinates that leaves the author's metric unchanged ($g_{11} = g_{22}$), so it maps every curvature entry to the entry with the exchanged labels, of the same value. By tool (i) it maps the sum $P^{x_1}{}_{x_1}$ term by term onto $P^{x_2}{}_{x_2}$: the two are equal. The same holds for $x_3$, and for the extra times $x_5, x_6, x_7$.

**(c) $a_4''$ appears at most once in each term (PROVED).** By tool (ii) an entry with $a_4''$ puts the label $x_4$ into both lists of the delta. Two such entries in one term would repeat $x_4$ in both lists, and GKD would be 0. So every component has the form $(\text{polynomial in } H, a_4') + a_4''\cdot(\text{polynomial in } H, a_4')$.

**(d) The time component contains no $a_4''$ (PROVED).** In $P^{x_4}{}_{x_4}$ the label $x_4$ already stands in both lists (as $h$ and $j$), so no factor may carry $x_4$: no entry with $a_4''$ (tool ii) and no mixed entry (tool iii). The factors are plane curvatures among the directions $x_1, x_2, x_3, x_5, x_6, x_7, x_8$, that is $a_4'^2 - H^2$, $-(a_4'^2 + H^2)$ and $-H^2$. So $E^{x_4}{}_{x_4}$ is a polynomial in $a_4'^2$ and $H^2$ alone, as the list of Section 11.20 shows. In the field equations this component is the **constraint**, a condition on $a_4'$, not an equation for its change.

**(e) Space against extra times: the evolution factor (PROVED).** Apply the relabelling $\tau$ of part (a) to $P^{x_1}{}_{x_1}$: it becomes $P^{x_5}{}_{x_5}$, term by term, with every factor replaced by its image. The image of a plane entry is the same entry with $a_4''$ replaced by $-a_4''$ (the table of Section 11.10: $(i, x_4)$ with $a_4'^2 + a_4''$ goes to $(j, x_4)$ with $a_4'^2 - a_4''$, and every other kind of plane goes to a plane with the same curvature). The image of a mixed entry has the opposite sign; but mixed entries occur in pairs in every nonzero term of a diagonal component other than $P^{x_4}{}_{x_4}$ and $P^{x_8}{}_{x_8}$ (the label $x_8$ must appear in both lists or in neither, so a mixed entry of one kind needs one of the other kind), and two sign changes cancel. Hence

$$
E^{x_5}{}_{x_5}(H, a_4', a_4'') = E^{x_1}{}_{x_1}(H, a_4', -a_4'') .
$$

With part (c) write $E^{x_1}{}_{x_1} = \mathcal{A}_k + a_4''\mathcal{B}_k$, where $\mathcal{A}_k$ and $\mathcal{B}_k$ are polynomials in $H$ and $a_4'$. Then $E^{x_5}{}_{x_5} = \mathcal{A}_k - a_4''\mathcal{B}_k$ (the identity just proved), and the difference is

$$
E^{x_1}{}_{x_1} - E^{x_5}{}_{x_5} = 2\mathcal{B}_k\,a_4'' = a_4''\,F_k(a_4'),\qquad F_k = 2\mathcal{B}_k .
$$

This difference is the only combination in which $a_4''$ survives; in the field equations it is the **evolution equation**, which decides how $a_4$ changes (Chapter 12). From the components of Section 11.20,

$$
F_1 = 2,\qquad F_2 = -16\big(3a_4'^2 + 5H^2\big),\qquad F_3 = 144\big(5a_4'^4 + 6a_4'^2H^2 + 5H^4\big)
$$

(for example $E_{(2)}{}^{x_1}{}_{x_1} - E_{(2)}{}^{x_5}{}_{x_5} = -48a_4'^2a_4'' - 80a_4''H^2 = -16a_4''(3a_4'^2 + 5H^2)$: the terms without $a_4''$ cancel). The record lists $F = \alpha_1F_1 + \alpha_2F_2 + \alpha_3F_3$ (`a4-equations.json`, key `generalSource`, entry `evolution_F`; `python-a4-report.json`, check `evolution_factorises`); Notebook 11c, In [4], computes the $F_k$ and compares them with the record.

**(f) The hidden component (PROVED).** The same relabelling maps $P^{x_8}{}_{x_8}$ to itself ($\tau$ keeps $x_8$), with $a_4''$ replaced by $-a_4''$; in its terms no factor carries $x_8$, so there are no mixed entries. So $E^{x_8}{}_{x_8}$ is unchanged when $a_4''$ changes sign, and by part (c) it is linear in $a_4''$: it contains no $a_4''$. Section 11.22 proves more: $E^{x_8}{}_{x_8} = \mathcal{A}_k$, the mean of the space and the extra-time components.

**(g) Even in $a_4'$: deflation is a choice of sign (PROVED).** Reverse the time: use the coordinate $y_4 = -x_4$ instead of $x_4$. Since $dx_4^2 = dy_4^2$, the metric in the new coordinates has exactly the author's form, with the function $b(y_4) = a_4(-y_4)$ in place of $a_4$. Its Lovelock components are therefore given by the same polynomials, with $b'(y_4) = -a_4'(x_4)$ and $b''(y_4) = a_4''(x_4)$ (the chain rule: each derivative brings a factor $dx_4/dy_4 = -1$). On the other hand a diagonal component of a tensor with one upper and one lower label does not change under this reflection: the component $x_4x_4$ is multiplied by $(-1)(-1) = 1$, and the others are not touched (the tensor rule of Section 3.14; $P_{(k)}$ is a tensor, built from the Riemann tensor and the generalized delta, whose entries are the same in every system of coordinates). So every diagonal component satisfies $E(H, -a_4', a_4'') = E(H, a_4', a_4'')$ at every point and for every history. Any two numbers $u, v$ are the values $a_4'(0) = u$, $a_4''(0) = v$ of the history $a_4 = ux_4 + vx_4^2/2$, so the identity holds for all values: **every component is an even function of $a_4'$**. The list of Section 11.20 shows it: $a_4'$ appears only in even powers. The meaning: replacing $a_4$ by $-a_4$ along a linear history, $A \to -A$, turns deflating extra times and inflating 3-space into inflating extra times and deflating 3-space, and the Lovelock tensors do not notice. The gravitational side of the field equations does not prefer deflation; deflation of the extra times is a choice of sign (Chapter 12 draws the consequences). Notebook 11c checks the evenness exactly (In [4]) and draws it (In [6], Figure 11c.1).

**(h) Weight $2k$ (PROVED in Section 11.11).** Every term of $E_{(k)}$ has the weight $2k$ when $H$ and $a_4'$ count 1 and $a_4''$ counts 2: $E_{(1)}$ is quadratic, $E_{(2)}$ quartic, $E_{(3)}$ of sixth degree in this sense. Notebook 11c checks it by replacing $H, a_4', a_4''$ by $uH, ua_4', u^2a_4''$ and finding the factor $u^{2k}$ (In [4]).

**One more factorisation used in Chapter 12.** The difference of the time and the hidden component is

$$
E^{x_4}{}_{x_4} - E^{x_8}{}_{x_8} = 6\big(a_4'^2 + H^2\big)V_k,\qquad V_1 = 1,\quad V_2 = -8\big(a_4'^2 + 5H^2\big),\quad V_3 = 72\big(a_4'^4 + 2a_4'^2H^2 + 5H^4\big).
$$

For $k = 2$, line by line:

$$
E_{(2)}{}^{x_4}{}_{x_4} - E_{(2)}{}^{x_8}{}_{x_8} = -36a_4'^4 - 120a_4'^2H^2 - 420H^4 - 12a_4'^4 - 168a_4'^2H^2 + 180H^4 = -48a_4'^4 - 288a_4'^2H^2 - 240H^4
$$

(the two components of Section 11.20; collect equal powers),

$$
= -48\big(a_4'^4 + 6a_4'^2H^2 + 5H^4\big) = -48\big(a_4'^2 + H^2\big)\big(a_4'^2 + 5H^2\big) = 6\big(a_4'^2 + H^2\big)\cdot(-8)\big(a_4'^2 + 5H^2\big)
$$

(take out $-48$; the quadratic $u^2 + 6u + 5 = (u + 1)(u + 5)$ in $u = a_4'^2/H^2$; $-48 = 6\cdot(-8)$). Notebook 11c checks all three (In [5]); the record uses the factor for the linear history (`python-a4-report.json`, check `linear_member_vacuum_factor`).

### 11.22 The two conservation identities

Every Lovelock tensor has zero covariant divergence (Lovelock's theorem; for the author's metric PROVED by exact computation: `Revision/gkd_lovelock/results/lovelock-report.json`, checks `k1_divergence_free` to `k3_divergence_free`). For the author's metric this one statement becomes two short identities between the components. Section 3.25 derived them for the Einstein tensor; here we derive them for every order, line by line.

**The divergence of a diagonal tensor.** For a tensor $P^h{}_j$ with one upper and one lower label, the covariant divergence is

$$
\nabla_hP^h{}_j = \sum_h\partial_hP^h{}_j + \sum_{h,m}\Gamma^h{}_{hm}P^m{}_j - \sum_{h,m}\Gamma^m{}_{hj}P^h{}_m
$$

(one $+\Gamma$ for the upper label, one $-\Gamma$ for the lower label, then the upper label contracted with the derivative; Section 3.15). If $P$ is diagonal, the first sum keeps $h = j$, the second keeps $m = j$, and the third keeps $m = h$:

$$
\nabla_hP^h{}_j = \partial_jP^j{}_j + \sum_h\Gamma^h{}_{hj}\big(P^j{}_j - P^h{}_h\big)\qquad(\text{no sum over } j)
$$

(the second and third sums combined, since both now run over $h$).

**The time direction, $j = x_4$.** The symbols $\Gamma^h{}_{hx_4}$ are $a_4'$ for the three space directions, $-a_4'$ for the three extra times, and 0 for $x_4$ and $x_8$ (Section 3.23). So

$$
\nabla_hP^h{}_{x_4} = \partial_4P^{x_4}{}_{x_4} + 3a_4'\big(P^{x_4}{}_{x_4} - P^{x_1}{}_{x_1}\big) - 3a_4'\big(P^{x_4}{}_{x_4} - P^{x_5}{}_{x_5}\big) = \partial_4P^{x_4}{}_{x_4} - 3a_4'\big(P^{x_1}{}_{x_1} - P^{x_5}{}_{x_5}\big)
$$

(the three space components are equal, and so are the three extra-time components, Section 11.21 (b); the terms $3a_4'P^{x_4}{}_{x_4}$ cancel). Setting the divergence to zero and multiplying by $-1/2^{k+1}$:

$$
\frac{d}{dx_4}E^{x_4}{}_{x_4} = 3a_4'\big(E^{x_1}{}_{x_1} - E^{x_5}{}_{x_5}\big). \qquad\text{(I)}
$$

**The hidden direction, $j = x_8$.** Nothing depends on $x_8$, so $\partial_8P^{x_8}{}_{x_8} = 0$. The symbols $\Gamma^h{}_{hx_8}$ are $H\cot z$ for the six transverse directions and 0 for $x_4$; the term $h = x_8$ has the factor $P^{x_8}{}_{x_8} - P^{x_8}{}_{x_8} = 0$. So

$$
\nabla_hP^h{}_{x_8} = 3H\cot z\big(P^{x_8}{}_{x_8} - P^{x_1}{}_{x_1}\big) + 3H\cot z\big(P^{x_8}{}_{x_8} - P^{x_5}{}_{x_5}\big) = 3H\cot z\big(2P^{x_8}{}_{x_8} - P^{x_1}{}_{x_1} - P^{x_5}{}_{x_5}\big) .
$$

Since $H\cot z > 0$ on the patch $0 < z < \pi/2$, zero divergence gives

$$
E^{x_8}{}_{x_8} = \tfrac12\big(E^{x_1}{}_{x_1} + E^{x_5}{}_{x_5}\big). \qquad\text{(II)}
$$

**The transverse directions.** For $j$ one of $x_1, x_2, x_3, x_5, x_6, x_7$: nothing depends on $x_j$, and every $\Gamma^h{}_{hj}$ is zero (Section 3.23), so the divergence vanishes without any condition.

**What the identities say about the components (PROVED).** With Section 11.21 (e), identity (II) gives $E^{x_8}{}_{x_8} = \frac12\big((\mathcal{A}_k + a_4''\mathcal{B}_k) + (\mathcal{A}_k - a_4''\mathcal{B}_k)\big) = \mathcal{A}_k$: the hidden component is the space component without its $a_4''$ part. For $k = 1$: $\frac12\big((-3a_4'^2 + a_4'' + 15H^2) + (-3a_4'^2 - a_4'' + 15H^2)\big) = -3a_4'^2 + 15H^2$. Identity (I) gives, since $E^{x_4}{}_{x_4}$ depends on $x_4$ only through $a_4'$ (Section 11.21 (d)) and by the chain rule $\frac{d}{dx_4}E^{x_4}{}_{x_4} = \frac{\partial E^{x_4}{}_{x_4}}{\partial a_4'}\,a_4''$,

$$
\frac{\partial E^{x_4}{}_{x_4}}{\partial a_4'}\,a_4'' = 3a_4'\,a_4''\,F_k\qquad\Longrightarrow\qquad\frac{\partial E^{x_4}{}_{x_4}}{\partial a_4'} = 3a_4'\,F_k(a_4')
$$

(identity (I) with Section 11.21 (e); both sides are polynomials that agree for every $a_4''$, so the factors of $a_4''$ agree). For $k = 2$: $\partial(-36a_4'^4 - 120a_4'^2H^2 - 420H^4)/\partial a_4' = -144a_4'^3 - 240a_4'H^2 = 3a_4'\cdot(-48a_4'^2 - 80H^2) = 3a_4'F_2$. The derivative of the constraint is $3a_4'$ times the evolution factor: this is the **constraint propagation** of the record (`a4-equations.json`, key `generalSource`, entry `constraint_propagation`; `python-a4-report.json`, check `bianchi_x4`). Notebook 11c checks (I) exactly for $k = 1, 2, 3$ (In [5]), and (II) both exactly (In [4]) and numerically along a test history (In [9] and In [10]).

**What they mean in the field equations (a preview of Chapter 12).** In $\sum_k\alpha_kE_{(k)} + \Lambda\delta = \kappa T$, with $T = \mathrm{diag}(p_3, p_3, p_3, -\rho, p_t, p_t, p_t, p_8)$, identity (I) becomes the conservation of energy $\rho' = -3a_4'(p_3 - p_t)$ (energy flows between 3-space and the extra times when their pressures differ), and identity (II) becomes the condition $p_3 + p_t = 2p_8$ on the pressures (record `a4-equations.json`, key `generalSource`, entries `conservation_reduced` and `algebraic_condition`; Notebook 11c, In [11], checks that the record states both).

### 11.23 Along the deflating history; an illustrative test history

**The linear history (PROVED).** Along $a_4 = AHx_4$ we have $a_4' = AH$ and $a_4'' = 0$; the extra times shrink like $e^{-AHx_4}$ (exponential deflation for $A > 0$; the author's history is $A = 1$). With $a_4'' = 0$ the space, extra-time and hidden components coincide (Section 11.21 (e) and identity (II)), and each order has only two different components. In units of $H^{2k}$:

| order | time component $E^{x_4}{}_{x_4}$ | the seven others |
| --- | --- | --- |
| $k = 1$ | $3A^2 + 21$ | $15 - 3A^2$ |
| $k = 2$ | $-36A^4 - 120A^2 - 420$ | $12A^4 + 168A^2 - 180$ |
| $k = 3$ | $360A^6 + 648A^4 + 1080A^2 + 2520$ | $-72A^6 - 648A^4 - 1944A^2 + 360$ |

(the components of Section 11.20 with $a_4' = AH$, $a_4'' = 0$). Every entry is even in $A$: the history $A$ and its mirror $-A$ give the same tensors (Section 11.21 (g)). Figure 11c.1 draws the six curves for $-3 \le A \le 3$ (Notebook 11c, In [6]).

**The Lovelock scalars along the linear history.** From the record (keys `L1` to `L3` of `lovelock-tensors.json`), in units of $H^{2k}$:

$$
L_{(1)} = 12A^2 - 84,\qquad L_{(2)} = -96A^4 - 2112A^2 + 3360,\qquad L_{(3)} = 1152A^6 + 31104A^4 + 100224A^2 - 40320 .
$$

At the mirror point $A = 0$ they are $-84$, $3360$ and $-40320$. Each has exactly one positive zero. For $k = 1$: $12A^2 = 84$, so $A^2 = 7$ and $A = \sqrt 7 \approx 2.646$ (divide by 12; take the positive root). For $k = 2$, write $u = A^2$:

$$
-96u^2 - 2112u + 3360 = 0 \quad\Longleftrightarrow\quad u^2 + 22u - 35 = 0
$$

(divide by $-96$: $2112/96 = 22$ and $3360/96 = 35$),

$$
u = -11 + \sqrt{121 + 35} = -11 + \sqrt{156} = 2\sqrt{39} - 11 \approx 1.49000
$$

(the formula for the roots of a quadratic, $u = -11 \pm\sqrt{11^2 + 35}$, with the positive root, because $u = A^2 \ge 0$; $\sqrt{156} = 2\sqrt{39}$), so $A = \sqrt{2\sqrt{39} - 11} \approx 1.2207$. For $k = 3$, $u^3 + 27u^2 + 87u - 35 = 0$ (divide by 1152) has one positive root, which Notebook 11c computes numerically, $A \approx 0.6010$ (In [7], COMPUTED with 15 digits). Figure 11c.2 draws the three scalars with their zeros.

**An illustrative test history (ILLUSTRATION, not a solution of any equation).** On the linear history $a_4'' = 0$, so it cannot show where $a_4''$ enters. Notebook 11c therefore also uses a test history in which the extra times deflate at all times and the deflation speeds up:

$$
a_4(x_4) = Hx_4 + \tfrac12\ln\cosh(Hx_4) .
$$

Its derivatives, line by line:

$$
a_4' = H + \tfrac12\cdot\frac{\sinh(Hx_4)}{\cosh(Hx_4)}\cdot H = H\big(1 + \tfrac12\tanh(Hx_4)\big)
$$

(the derivative of $\ln u$ is $u'/u$, the derivative of $\cosh t$ is $\sinh t$, and the chain rule gives the factor $H$; $\sinh/\cosh = \tanh$), and

$$
a_4'' = \tfrac12H\cdot\frac{H}{\cosh^2(Hx_4)} = \frac{H^2}{2}\,\mathrm{sech}^2(Hx_4)
$$

(the derivative of $\tanh t$ is $1/\cosh^2t = \mathrm{sech}^2t$, and the chain rule again). Since $-1 < \tanh < 1$, $a_4'$ lies between $H/2$ and $3H/2$: it is always positive, so the extra times always deflate, slowly in the far past ($a_4' \to H/2$, the linear history with $A = 1/2$) and three times faster in the far future ($a_4' \to 3H/2$, $A = 3/2$). The acceleration $a_4''$ is a bump of height $H^2/2$ at $x_4 = 0$ ($\mathrm{sech}\,0 = 1$). Figure 11c.3 draws the history (Notebook 11c, In [8]). Along it, the components behave as Section 11.21 says (Figure 11c.4, In [9]): the time component depends on $a_4'$ only and moves from one constant to another, for $k = 1$ from $3/4 + 21 = 21.75H^2$ to $27/4 + 21 = 27.75H^2$; the space and extra-time components separate while $a_4'' \ne 0$, by $a_4''F_k$; and the hidden component runs exactly halfway between them. Finally Notebook 11c checks identity (I) along this history with a finite-difference derivative, $f'(t) \approx (f(t + \epsilon) - f(t - \epsilon))/(2\epsilon)$ with $\epsilon = 0.01$, whose error is of the size $\epsilon^2/6$ times the third derivative of the time component; the largest relative deviations are $3.8 \times 10^{-5}$, $4.0 \times 10^{-5}$ and $4.5 \times 10^{-5}$ for $k = 1, 2, 3$ (COMPUTED, In [10], Figure 11c.5), the size of this error, while the exact identity holds without any error (In [5]).

**What the deflation does and does not decide (honesty).** The Lovelock tensors are the gravitational side of the field equations. They are the same for $A$ and $-A$: whether the extra times deflate is not decided by them but by the source and the initial data (Chapter 12). This symmetry $A \to -A$ is a property of the metric's geometry; it is NOT the pairing of universes of masses $+m$ and $-m$ of Chapters 18 to 20, and nothing in this chapter says anything about the creation of universes or about matter and antimatter.

### 11.24 Example: the components and identities along the deflating history

Notebook 11c reads the exact components of the three Lovelock tensors from the Revision record `lovelock-tensors.json`, forms the normalised tensors $E_{(k)}$ and checks that they are the components recorded for the field equations of $a_4$ (`a4-equations.json`) and by the Revision's sympy verification; proves with sympy the structure of Section 11.21 (space and extra-time components alike, the constraint free of $a_4''$, the evolution factors $F_k$, the hidden component as the mean, evenness in $a_4'$, weight $2k$) and the identities of Section 11.22; draws the components and the scalars along the linear history as functions of $A$, with the zeros of the scalars; and uses the illustrative test history to show where $a_4''$ enters and to check identity (I) numerically. It quotes the reports of the field equations of $a_4$ only by the names of their checks, never by their numbers of checks, so that it stays valid when these reports gain checks. It needs no Rust, takes about 15 seconds (27.3 seconds when it was built, 24.0 seconds in its verification run; provenance file `Revision/textbook/notebooks/11c_lovelock_components.PROVENANCE.md`), prints 19 PASS lines, draws five figures and ends with the line ALL 19 CHECKS PASSED (notebook 11c).

<!-- NOTEBOOK 11c -->

### 11.27 Line-by-line walk-through of Notebook 11c

The notebook has 12 code cells, In [1] to In [12]. As in Sections 11.9 and 11.19, every line or small group of lines is quoted and explained; docstrings are left out where the explanation repeats them, and long captions are shortened to `...` (they are printed in full under the figures in Section 11.26).

**In [1], the set-up cell.** It is the set-up cell of Notebook 11a, explained line by line in Section 11.9 under In [1], with three differences: its comment lines are the run instructions of Notebook 11c (Section 11.25); its line `NOTEBOOK_ID = "11c"  # this notebook: chapter 11, example c` names this notebook; and, because this notebook runs no Rust program, the two lines `import shutil` and `import subprocess` and the helper `rust_program` are absent. It prints Set-up of notebook 11c complete: repository folder found, helpers defined.

**In [2], the components from the Revision record.**

```python
import numpy as np  # arrays of numbers
import sympy as sp  # exact algebra

H, A1, A2 = sp.symbols("H A1 A2")  # H, a4' and a4''
NAMES = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]
tensors = json.loads(repository_file(
    "Revision/gkd_lovelock/results/lovelock-tensors.json").read_text(encoding="utf-8"))
```

numpy and sympy are loaded; three sympy symbols stand for $H$, $a_4'$ and $a_4''$; `NAMES` lists the coordinate names; and the Rust record of the Lovelock tensors is read as JSON (Section 11.9 explains `repository_file`, `read_text` and `json.loads`).

```python
def from_monomials(monomials):
    total = sp.Integer(0)
    for numerator, denominator, e in monomials:
        if any(e[3:]):  # 3rd or 4th derivative, e^a4, sin^(1/3) z or cot z
            raise ValueError("the component contains more than H, a4' and a4''")
        monomial = H ** e[0] * A1 ** e[1] * A2 ** e[2]  # H^eH a4'^e1 a4''^e2
        total += sp.Rational(numerator, denominator) * monomial
    return total
```

A component of the record is a list of monomials, each a numerator, a denominator and eight exponents (of $H$, $a_4'$, $a_4''$, $a_4'''$, $a_4''''$, $e^{a_4}$, $\sin^{1/3}z$, $\cot z$). The function (docstring left out) rebuilds the component as a sympy expression. `any(e[3:])` is true if any of the last five exponents is not 0; the notebook would then stop. Since it does not stop, every component is free of $x_8$, of $e^{a_4}$ and of higher derivatives (Section 11.20). Each monomial is the exact fraction (`sp.Rational`) times $H^{e_0}a_4'^{e_1}a_4''^{e_2}$.

```python
P = {k: {(h, j): from_monomials(tensors[f"P{k}_mixed_up_h_down_j"][f"{a},{b}"]
                                ["monomials"])
         for h, a in enumerate(NAMES) for j, b in enumerate(NAMES)} for k in (1, 2, 3)}
E = {k: {hj: sp.expand(-value / 2 ** (k + 1)) for hj, value in P[k].items()}
     for k in (1, 2, 3)}
```

`P[k][h, j]` is the component $P_{(k)}{}^h{}_j$, built for all 64 pairs (`enumerate(NAMES)` gives each number with its name, used for the record's keys such as `"x1,x1"`); `E[k]` holds the normalised components $E_{(k)} = -P_{(k)}/2^{k+1}$, multiplied out.

```python
for k in (1, 2, 3):
    for h in (0, 3, 4, 7):  # x1, x4, x5, x8
        say(f"E({k})^{NAMES[h]}_{NAMES[h]} = {E[k][h, h]}")
check(all(E[k][h, j] == 0 for k in (1, 2, 3) for h in range(8) for j in range(8)
          if h != j),
      "every off-diagonal component of E(1), E(2), E(3) is zero, x4-x8 included")
```

The four independent components of each order are printed: twelve lines that are exactly the list of Section 11.20 (sympy writes `A1**2` for $a_4'^2$). The check confirms that every off-diagonal component is zero (Section 11.21 (a)). First PASS line.

**In [3], against the other records.**

```python
a4_record = json.loads(repository_file(
    "Revision/field_equations_a4/a4-equations.json").read_text(encoding="utf-8"))
WOLFRAM_NAMES = {"ad1": A1, "ad2": A2, "H": H}


def from_text(text):
    return sp.sympify(text.replace("^", "**"), locals=WOLFRAM_NAMES)
```

The record of the field equations of $a_4$ is read. It writes formulas in Wolfram's input notation, with `ad1` for $a_4'$, `ad2` for $a_4''$ and `^` for powers; `from_text` (docstring left out) replaces `^` by `**` and reads the text with these names bound to the notebook's symbols.

```python
same = True
for k in (1, 2, 3):
    listed = a4_record["lovelockTensors"][f"E{k}"]
    for key, (h, j) in (("x1x1", (0, 0)), ("x4x4", (3, 3)), ("x5x5", (4, 4)),
                        ("x8x8", (7, 7)), ("x4x8", (3, 7)), ("x8x4", (7, 3))):
        same = same and sp.expand(from_text(listed[key]["input"]) - E[k][h, j]) == 0
check(same, "E(1), E(2), E(3) equal the components recorded for the a4 equations",
      record="Revision/field_equations_a4/reports/python-a4-report.json, check "
             "json_lovelock_components")
```

For each order the record's entry `lovelockTensors` lists six components, the four independent diagonal ones and the two $x_4$-$x_8$ ones (which are 0). Each must equal the notebook's component exactly. Second PASS line.

```python
checker = json.loads(repository_file(
    "Revision/gkd_lovelock/results/python-lovelock-report.json").read_text(
        encoding="utf-8"))
independent = checker["independentResults"]
same = all(
    sp.expand(sp.sympify(text, locals={"A1": A1, "A2": A2, "H": H})
              - P[k][NAMES.index(key.split(",")[0]), NAMES.index(key.split(",")[1])])
    == 0
    for k in (1, 2, 3) for key, text in independent[f"P{k}_mixed_nonzero"].items())
check(same and all(len(independent[f"P{k}_mixed_nonzero"]) == 8 for k in (1, 2, 3)),
      "P(1), P(2), P(3) equal the independent sympy results (8 nonzero components each)",
      record="Revision/gkd_lovelock/results/python-lovelock-report.json, "
             "independentResults")
```

The Revision's sympy verification stores its own, independently computed nonzero components in the entry `independentResults`, under keys such as `"x1,x1"`; `key.split(",")` cuts a key into the two names. Every one must equal the notebook's $P_{(k)}$, and there must be exactly 8 for each order. Third PASS line.

**In [4], the structure.**

```python
u = sp.Symbol("u")  # an auxiliary number used to test the weights
F = {}  # k -> F_k(a4')
alphas = sp.symbols("alpha1 alpha2 alpha3")  # the constants of the a4 equations
recorded_F = sp.sympify(
    a4_record["generalSource"]["evolution_F"]["input"].replace("^", "**"),
    locals={"ad1": A1, "H": H, "alpha1": alphas[0], "alpha2": alphas[1],
            "alpha3": alphas[2]})
```

The symbol `u` will scale the components; `F` will hold the evolution factors; the three Lovelock constants $\alpha_1, \alpha_2, \alpha_3$ are symbols; and the record's evolution factor $F = \alpha_1F_1 + \alpha_2F_2 + \alpha_3F_3$ (key `generalSource`, entry `evolution_F`) is read.

```python
structure = {name: True for name in ("alike", "constraint", "evolution", "mean",
                                     "even", "weight")}
```

A dictionary of six true/false flags, one for each property of Section 11.21; each starts true and is combined below with the result for every order.

```python
for k in (1, 2, 3):
    e = E[k]
    structure["alike"] &= (e[0, 0] == e[1, 1] == e[2, 2]
                           and e[4, 4] == e[5, 5] == e[6, 6])
    structure["constraint"] &= not e[3, 3].has(A2) and not e[7, 7].has(A2)
```

`&=` combines a flag with a new result by AND: it stays true only if both are true. "alike": the three space components are equal and the three extra-time components are equal (Section 11.21 (b)). "constraint": the time and the hidden component do not contain $a_4''$ (`expr.has(A2)` is true when the symbol occurs; parts (d) and (f)).

```python
    F[k] = sp.factor(sp.cancel((e[0, 0] - e[4, 4]) / A2))
    structure["evolution"] &= (not F[k].has(A2)
                               and sp.expand(F[k] - recorded_F.coeff(alphas[k - 1]))
                               == 0)
```

The space minus the extra-time component, divided by $a_4''$: `sp.cancel` divides exactly and `sp.factor` writes the result as a product. It must be free of $a_4''$ (part (e)) and equal to the coefficient of $\alpha_k$ in the record's $F$ (`.coeff(alphas[k - 1])`; Python counts the list `alphas` from 0).

```python
    structure["mean"] &= sp.expand(e[7, 7] - (e[0, 0] + e[4, 4]) / 2) == 0
    structure["even"] &= all(sp.expand(e[h, h].subs(A1, -A1) - e[h, h]) == 0
                             for h in range(8))
```

"mean": identity (II) of Section 11.22. "even": replacing $a_4'$ by $-a_4'$ (`.subs(A1, -A1)`) changes no diagonal component (part (g)).

```python
    weighted = {h: sp.expand(e[h, h].subs({H: u * H, A1: u * A1, A2: u ** 2 * A2}))
                for h in range(8)}
    structure["weight"] &= all(sp.expand(weighted[h] - u ** (2 * k) * e[h, h]) == 0
                               for h in range(8))
    report(f"F_{k}(a4') = (E({k})^x1_x1 - E({k})^x5_x5) / a4''", F[k])
```

"weight": replacing $H$, $a_4'$, $a_4''$ by $uH$, $ua_4'$, $u^2a_4''$ must multiply each component by $u^{2k}$, which is true exactly when every term has the weight $2k$ (part (h)). The RESULT lines print $F_1 = 2$, $F_2 = -16(3a_4'^2 + 5H^2)$ and $F_3 = 144(5a_4'^4 + 6a_4'^2H^2 + 5H^4)$.

```python
check(structure["alike"], "space components equal, extra-time components equal")
check(structure["constraint"], "the x4 and x8 components contain no a4''")
check(structure["evolution"],
      "E^x1_x1 - E^x5_x5 = a4'' F_k(a4') with F_1 = 2, F_2 = -16 (3 a4'^2 + 5 H^2), "
      "F_3 = 144 (5 a4'^4 + 6 a4'^2 H^2 + 5 H^4)",
      record="Revision/field_equations_a4/reports/python-a4-report.json, check "
             "evolution_factorises (a4-equations.json, evolution_F)")
check(structure["mean"], "E^x8_x8 is the mean of E^x1_x1 and E^x5_x5 (identity II)")
check(structure["even"] and structure["weight"],
      "every component is even in a4' and of weight 2k (dimension 1/length^(2k))")
```

Five checks, one per flag (evenness and weight together). PASS lines four to eight.

**In [5], identity (I) and the factor $V_k$.**

```python
V = {1: sp.Integer(1), 2: -8 * (A1 ** 2 + 5 * H ** 2),
     3: 72 * (A1 ** 4 + 2 * A1 ** 2 * H ** 2 + 5 * H ** 4)}
identity_I = all(
    sp.expand(sp.diff(E[k][3, 3], A1) * A2 - 3 * A1 * (E[k][0, 0] - E[k][4, 4])) == 0
    for k in (1, 2, 3))
```

`V` holds the three factors $V_k$ of Section 11.21. Identity (I): the time component depends on $x_4$ only through $a_4'$, so its derivative is $\partial E^{x_4}{}_{x_4}/\partial a_4'$ times $a_4''$ (the chain rule; `sp.diff(..., A1)` differentiates with respect to the symbol $a_4'$), and this must equal $3a_4'(E^{x_1}{}_{x_1} - E^{x_5}{}_{x_5})$ for every order.

```python
check(identity_I, "d/dx4 E^x4_x4 = 3 a4' (E^x1_x1 - E^x5_x5) for k = 1, 2, 3 "
                  "(identity I)",
      record="Revision/field_equations_a4/reports/python-a4-report.json, check "
             "bianchi_x4; Revision/gkd_lovelock/results/lovelock-report.json, checks "
             "k1_divergence_free, k2_divergence_free and k3_divergence_free")
factor_ok = all(sp.expand(E[k][3, 3] - E[k][7, 7] - 6 * (A1 ** 2 + H ** 2) * V[k]) == 0
                for k in (1, 2, 3))
check(factor_ok, "E^x4_x4 - E^x8_x8 = 6 (a4'^2 + H^2) V_k for k = 1, 2, 3",
      record="Revision/field_equations_a4/reports/python-a4-report.json, check "
             "linear_member_vacuum_factor")
```

The two checks: identity (I) holds exactly, and the factorisation $E^{x_4}{}_{x_4} - E^{x_8}{}_{x_8} = 6(a_4'^2 + H^2)V_k$ holds for $k = 1, 2, 3$. PASS lines nine and ten.

**In [6], the linear history (Figure 11c.1).**

```python
A = np.linspace(-3.0, 3.0, 601)  # values of A
LINEAR = {H: 1, A2: 0}  # H = 1 (units of H) and a4'' = 0; then a4' = A


def on_linear_history(expr):
    function = sp.lambdify(A1, expr.subs(LINEAR), "numpy")
    return np.broadcast_to(function(A), A.shape).astype(float)
```

`np.linspace(-3.0, 3.0, 601)` is the array of 601 equally spaced values from $-3$ to 3. On the linear history, with $H = 1$, $a_4' = A$ and $a_4'' = 0$. `on_linear_history` (docstring left out) substitutes these values, and `sp.lambdify` turns the remaining expression in `A1` into a numpy function that is evaluated on the whole array at once. `np.broadcast_to(..., A.shape)` makes a constant result (an expression without $A$) into an array of the same length, and `.astype(float)` into decimal numbers.

```python
fig, axes = plt.subplots(1, 3, figsize=(12.0, 4.0))
symmetric = True
for ax, k in zip(axes, (1, 2, 3)):
    time_part = on_linear_history(E[k][3, 3])
    other_part = on_linear_history(E[k][0, 0])
    symmetric &= np.allclose(time_part, time_part[::-1]) and np.allclose(
        other_part, other_part[::-1])
```

One panel per order. `time_part` is $E^{x_4}{}_{x_4}$ and `other_part` the common value of the seven other components along the history. `[::-1]` reverses an array, which maps the value at $A$ to the value at $-A$ (the grid is symmetric about 0), and `np.allclose` tests that two arrays agree up to rounding: both curves must be mirror-symmetric.

```python
    ax.plot(A, time_part, label="$E^{x_4}{}_{x_4}$ (time)")
    ax.plot(A, other_part, "--", label="$E^{x_1}{}_{x_1} = E^{x_5}{}_{x_5} = "
                                       "E^{x_8}{}_{x_8}$")
    ax.axvline(0.0, color="0.5", lw=0.8)
    ax.axhline(0.0, color="0.5", lw=0.8)
    ax.set_xlabel("$A = a_4^{\\prime}/H$")
    ax.set_ylabel(f"$E_{{({k})}}$ in units of $H^{{{2 * k}}}$")
    ax.set_title(f"order k = {k}")
    ax.legend(fontsize=7, loc="best")
```

The two curves (solid and dashed), grey lines at $A = 0$ and at the value 0, axis titles, title and legend (`loc="best"` lets matplotlib choose a free corner).

```python
fig.tight_layout()
save_figure(fig, "components_linear_history",
            "The normalised Lovelock tensors $E_{(1)}$ (Einstein), $E_{(2)}$ and "
            ...)
check(symmetric, "on the linear history every curve is symmetric under A -> -A")
```

The figure is saved and the symmetry checked. Eleventh PASS line.

*What Figure 11c.1 shows.* Three panels, one per order, against $A$ from $-3$ to 3 in units of $H^{2k}$. For $k = 1$ the time component $3A^2 + 21$ is a parabola opening upward from 21, and the other component $15 - 3A^2$ one opening downward from 15, crossing 0 at $A = \pm\sqrt 5$. For $k = 2$ the curves open the other way, and the dashed one crosses 0 at $A = \pm 1$ ($12 + 168 - 180 = 0$). For $k = 3$ both grow like $A^6$. Every curve is a mirror image of itself about $A = 0$: deflating ($A > 0$) and inflating ($A < 0$) extra times give the same tensors.

**In [7], the Lovelock scalars (Figure 11c.2).**

```python
L = {k: sp.sympify(tensors[f"L{k}"].replace("Derivative[1][a4][x4]", "A1")
                   .replace("^", "**"), locals={"A1": A1, "H": H}) for k in (1, 2, 3)}
fig, axes = plt.subplots(1, 3, figsize=(12.0, 3.8))
zeros = {}
```

The three scalars of the record (keys `L1` to `L3`, in Mathematica text) are read as sympy expressions, with $a_4'$ written `A1`. Three panels and an empty dictionary for the zeros.

```python
for ax, k in zip(axes, (1, 2, 3)):
    values = on_linear_history(L[k])
    roots = sp.Poly(L[k].subs(H, 1), A1).nroots(n=15)  # every root, numerically
    zeros[k] = [float(r) for r in roots if r.is_real and r > 0]
    listed = ", ".join(f"{r:.4f}" for r in zeros[k])  # the zeros, 4 decimals
    say(f"L({k}) = {L[k]}")
    report(f"positive zero of L({k}) on the linear history (and minus it), A", listed)
```

For each order the scalar is evaluated along the history. `sp.Poly(..., A1).nroots(n=15)` computes all roots of the polynomial in $A$ (with $H = 1$) numerically to 15 digits, including complex ones; the comprehension keeps the real positive roots. The output lines print each scalar and its positive zero: $A = 2.6458$, $1.2207$ and $0.6010$ (Section 11.23 derives the first two exactly: $\sqrt 7$ and $\sqrt{2\sqrt{39} - 11}$).

```python
    ax.plot(A, values, color="tab:green")
    for r in zeros[k]:
        ax.plot([r, -r], [0.0, 0.0], "o", color="black", markersize=4)
    ax.axhline(0.0, color="0.5", lw=0.8)
    ax.axvline(0.0, color="0.5", lw=0.8)
    ax.set_xlabel("$A = a_4^{\\prime}/H$")
    ax.set_ylabel(f"$L_{{({k})}}$ in units of $H^{{{2 * k}}}$")
    ax.set_title(f"Lovelock scalar of order {k}")
```

The green curve, black dots at the zero and at its mirror image, grey lines, axis titles and title.

```python
    if k == 3:  # a magnified view of the middle, where the zeros of L(3) lie
        zoom = ax.inset_axes([0.30, 0.42, 0.42, 0.42])  # [left, bottom, width, height]
        near = np.abs(A) <= 1.0  # the values of A between -1 and 1
        zoom.plot(A[near], values[near], color="tab:green")
        zoom.axhline(0.0, color="0.5", lw=0.8)
        for r in zeros[k]:
            zoom.plot([r, -r], [0.0, 0.0], "o", color="black", markersize=3)
        zoom.tick_params(labelsize=6)
        zoom.set_title("magnified: $-1 \\leq A \\leq 1$", fontsize=7)
```

For the third order the scale of the whole panel (millions) hides the dip near $A = 0$, so a small panel inside the big one (`ax.inset_axes`, placed by its left edge, bottom edge, width and height as fractions of the big panel) shows the part $-1 \le A \le 1$. `near` is a true/false array, and `A[near]` keeps the values where it is true.

```python
fig.tight_layout()
save_figure(fig, "lovelock_scalars",
            "The Lovelock scalars $L_{(1)} = 2R = 12 a_4^{\\prime 2} - 84 H^2$, "
            ...)
check(all(len(zeros[k]) == 1 for k in (1, 2, 3))
      and abs(zeros[1][0] - float(sp.sqrt(7))) < 1e-12
      and L[1].subs({A1: 0, H: 1}) == -84 and L[2].subs({A1: 0, H: 1}) == 3360
      and L[3].subs({A1: 0, H: 1}) == -40320,
      "each scalar has one positive zero, L(1) at A = sqrt(7); at A = 0 the scalars "
      "are -84, 3360, -40320")
```

The caption written into the figure includes the computed zeros (the f-strings of the caption insert them, rounded to three decimals). The check: exactly one positive zero for each order, the first at $\sqrt 7$ to 12 digits, and the values $-84$, 3360, $-40320$ at $A = 0$. Twelfth PASS line.

*What Figure 11c.2 shows.* $L_{(1)} = 12A^2 - 84$ is a parabola with its lowest point $-84$ at $A = 0$ and zeros at $\pm\sqrt 7$. $L_{(2)}$ opens downward from its highest point 3360 and crosses 0 at $\pm 1.221$. $L_{(3)}$ has a shallow dip to $-40320$ at $A = 0$, visible only in the magnified inset, crosses 0 at $\pm 0.601$ and then grows to about $4 \times 10^6$ at $A = \pm 3$.

**In [8], the test history (Figure 11c.3).**

```python
t = sp.Symbol("t")  # t = H x4 (the time in units of 1/H); H = 1 below
history = t + sp.log(sp.cosh(t)) / 2
first = sp.diff(history, t)  # a4' (with H = 1)
second = sp.diff(history, t, 2)  # a4''
check(sp.simplify(first - (1 + sp.tanh(t) / 2)) == 0
      and sp.simplify(second - sp.sech(t) ** 2 / 2) == 0,
      "the test history has a4' = 1 + tanh/2 > 0 and a4'' = sech^2/2 (H = 1)")
```

The illustrative history of Section 11.23 with $H = 1$, in the variable $t = Hx_4$. sympy differentiates it once and twice (`sp.diff(history, t, 2)`), and the check confirms the derivatives derived by hand: $1 + \frac12\tanh t$ and $\frac12\mathrm{sech}^2t$. Thirteenth PASS line.

```python
times = np.linspace(-6.0, 6.0, 1201)  # H x4 from -6 to 6
a4_values = sp.lambdify(t, history, "numpy")(times)
a1_values = sp.lambdify(t, first, "numpy")(times)
a2_values = sp.lambdify(t, second, "numpy")(times)
```

1201 times from $-6$ to 6, 0.01 apart, and the values of $a_4$, $a_4'$ and $a_4''$ at all of them.

```python
fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.0))
axes[0].semilogy(times, np.exp(a4_values), label="space, $e^{a_4}$ (inflates)")
axes[0].semilogy(times, np.exp(-a4_values), "--",
                 label="extra times, $e^{-a_4}$ (deflate)")
axes[0].set_xlabel("time $H x_4$")
axes[0].set_ylabel("scale factor (logarithmic scale)")
axes[0].set_title("scale factors of the test history")
axes[0].legend(fontsize=8)
```

The left panel: the scale factors $e^{a_4}$ of 3-space and $e^{-a_4}$ of the extra times (without the common factor $\sin^{1/6}z$) on a logarithmic axis, where exponential growth or decay is a straight line.

```python
axes[1].plot(times, a1_values, label="$a_4^{\\prime}/H$")
axes[1].plot(times, a2_values, "--", label="$a_4^{\\prime\\prime}/H^2$")
axes[1].set_xlabel("time $H x_4$")
axes[1].set_ylabel("value")
axes[1].set_title("its first and second derivatives")
axes[1].legend(fontsize=8)
fig.tight_layout()
save_figure(fig, "test_history",
            "The illustrative test history $a_4 = H x_4 + \\frac{1}{2} \\ln\\cosh H "
            ...)
```

The right panel: $a_4'/H$ and $a_4''/H^2$; then the figure is saved.

*What Figure 11c.3 shows.* Left: the solid line ($e^{a_4}$) rises and the dashed line ($e^{-a_4}$) falls at all times; both are straight on the logarithmic axis far from $x_4 = 0$, with the slope $\pm 1/2$ in the past and $\pm 3/2$ in the future, and they bend around $x_4 = 0$. Right: $a_4'/H$ rises like a step from 1/2 to 3/2, and $a_4''/H^2$ is a bump of height 1/2 at $x_4 = 0$. The history is an illustration, not a solution of any field equation.

**In [9], the components along the test history (Figure 11c.4).**

```python
def along_history(expr):
    function = sp.lambdify((A1, A2), expr.subs(H, 1), "numpy")
    return np.broadcast_to(function(a1_values, a2_values), times.shape).astype(float)
```

`along_history` (docstring left out) evaluates an expression in $a_4'$ and $a_4''$ (with $H = 1$) at all 1201 times at once.

```python
fig, axes = plt.subplots(1, 3, figsize=(12.0, 4.0))
middle = True
curves = {}
for ax, k in zip(axes, (1, 2, 3)):
    curves[k] = {h: along_history(E[k][h, h]) for h in (0, 3, 4, 7)}
    middle &= np.allclose(curves[k][7], (curves[k][0] + curves[k][4]) / 2,
                          rtol=1e-12, atol=1e-9)
```

For each order the four independent components are evaluated along the history and kept in `curves` (keys 0, 3, 4, 7 for $x_1, x_4, x_5, x_8$). The hidden component must equal the mean of the space and extra-time components at every time, up to rounding (`rtol` and `atol` are the allowed relative and absolute differences).

```python
    for h, style in ((3, "-"), (0, "-"), (4, "--"), (7, ":")):
        ax.plot(times, curves[k][h], style,
                label=f"$E^{{x_{h + 1}}}{{}}_{{x_{h + 1}}}$")
    ax.set_xlabel("time $H x_4$")
    ax.set_ylabel(f"$E_{{({k})}}$ in units of $H^{{{2 * k}}}$")
    ax.set_title(f"order k = {k}")
    ax.legend(fontsize=7)
```

The four curves: time and space solid, extra times dashed, hidden dotted; the legend labels are built from the number `h + 1` of each coordinate.

```python
fig.tight_layout()
save_figure(fig, "components_test_history",
            "The four independent components of $E_{(1)}$, $E_{(2)}$ and $E_{(3)}$ "
            ...)
check(middle, "along the test history E^x8_x8 is the mean of E^x1_x1 and E^x5_x5 "
              "at all 1201 times")
```

The figure is saved, and the check confirms identity (II) at all 1201 times. Fourteenth PASS line.

*What Figure 11c.4 shows.* In each panel the time component (blue) steps from one constant to another, for $k = 1$ from $21.75$ to $27.75$, because it depends on $a_4'$ alone. The space (orange) and extra-time (dashed green) components step the other way and separate only near $x_4 = 0$, where $a_4'' \ne 0$: for $k = 1$ and $k = 3$ the space component lies above ($F_1, F_3 > 0$), for $k = 2$ below ($F_2 < 0$). The dotted hidden component runs exactly between them.

**In [10], identity (I) numerically (Figure 11c.5).**

```python
step = times[1] - times[0]  # epsilon = 0.01
fig, axes = plt.subplots(1, 3, figsize=(12.0, 3.8))
worst = {}
for ax, k in zip(axes, (1, 2, 3)):
    left = np.gradient(curves[k][3], step)  # d/dx4 of the time component
    right = 3 * a1_values * (curves[k][0] - curves[k][4])
```

`step` is the spacing of the times, 0.01. `np.gradient(values, step)` estimates the derivative at every time by the central difference $(f(t + \epsilon) - f(t - \epsilon))/(2\epsilon)$ (at the two end points by a one-sided difference). `left` is the estimated derivative of the time component, `right` the right side of identity (I).

```python
    inner = slice(1, -1)  # the two end points use a one-sided difference
    worst[k] = float(np.max(np.abs(left[inner] - right[inner]))
                     / np.max(np.abs(right)))
    report(f"order {k}: largest relative deviation of the finite difference",
           f"{worst[k]:.1e}")
```

`slice(1, -1)` leaves out the first and the last time, where the less accurate one-sided difference is used. The largest difference between the two sides, divided by the largest size of the right side, is the relative deviation; the RESULT lines print $3.8 \times 10^{-5}$, $4.0 \times 10^{-5}$ and $4.5 \times 10^{-5}$ (the format `:.1e`).

```python
    ax.plot(times, right, color="tab:blue", lw=3, alpha=0.5,
            label="$3 a_4^{\\prime} (E^{x_1}{}_{x_1} - E^{x_5}{}_{x_5})$")
    ax.plot(times, left, "k:", label="$d E^{x_4}{}_{x_4} / d x_4$ (finite difference)")
    ax.set_xlabel("time $H x_4$")
    ax.set_ylabel(f"units of $H^{{{2 * k + 1}}}$")
    ax.set_title(f"identity (I), order k = {k}")
    ax.legend(fontsize=7)
fig.tight_layout()
```

Both sides are drawn: the right side as a thick, half-transparent blue line (`lw=3`, `alpha=0.5`) and the finite difference as a dotted black line on top of it. One derivative with respect to $x_4$ adds one power of $H$, so the unit is $H^{2k+1}$.

```python
largest = max(worst.values())  # the largest relative deviation of the three orders
power = int(np.floor(np.log10(largest)))  # its power of ten
deviation_text = f"${largest / 10 ** power:.1f} \\times 10^{{{power}}}$"
save_figure(fig, "conservation_identity",
            "Identity (I), the conservation identity along the time, checked "
            ...)
check(all(value < 1e-4 for value in worst.values()),
      "the finite-difference derivative agrees with identity (I) to 1e-4")
```

The largest deviation of the three orders is written into the caption in the form $4.5 \times 10^{-5}$: `np.log10` is the logarithm to the base 10, and `np.floor` rounds it down, which gives the power of ten. The check requires every relative deviation to be below $10^{-4}$. Fifteenth PASS line.

*What Figure 11c.5 shows.* In each panel the dotted black line lies on the thick blue line: a bump at $x_4 = 0$, zero far away, where $a_4'' = 0$ and the time component is constant. The sign of the bump follows $F_k$ (positive for $k = 1, 3$, negative for $k = 2$), times the positive $3a_4'a_4''$.

**In [11], the quoted records once more.**

```python
def verdicts(path):
    data = json.loads(repository_file(path).read_text(encoding="utf-8"))
    checks = data["checks"]
    if isinstance(checks, dict):  # name -> {"passed": true or false, ...}
        return {name: "PASS" if entry["passed"] else "FAIL"
                for name, entry in checks.items()}
    return {entry["name"]: entry["verdict"] for entry in checks}  # a list of entries
```

The helper of Notebook 11a, In [16] (Section 11.9): for one report, a dictionary from the name of each check to PASS or FAIL.

```python
QUOTED = {  # report -> the checks that this notebook quotes from it
    "Revision/field_equations_a4/reports/python-a4-report.json": [
        "json_lovelock_components", "evolution_factorises", "bianchi_x4",
        "linear_member_vacuum_factor"],
    "Revision/gkd_lovelock/results/lovelock-report.json": [
        "k1_divergence_free", "k2_divergence_free", "k3_divergence_free"],
}
```

The checks quoted in the notebook, by report (here with the full paths, because the two reports lie in different folders).

```python
for path, names in QUOTED.items():
    found = verdicts(path)
    for name in names:
        say(f"{path.split('/')[-1]}: {name} {found.get(name, 'MISSING')}")
    check(all(found.get(name) == "PASS" for name in names),
          f"the {len(names)} checks quoted from {path.split('/')[-1]} are there and "
          "PASS", record=f"{path}, checks " + ", ".join(names))
```

Each quoted check is printed with its verdict (`path.split('/')[-1]` is the file name, the last part of the path) and must be present with PASS. The notebook asks only for these names, not for the number of checks of the report, so it stays valid when the report gains checks. PASS lines sixteen and seventeen.

```python
general = a4_record["generalSource"]  # a4-equations.json, read in section 5
stated = (general["algebraic_condition"]["input"] == "p3 + pt == 2*p8"
          and "rho' = -3 a4' (p3 - p_t)" in general["conservation_reduced"]
          and "p3 + p_t = 2 p8" in general["conservation_reduced"]
          and "d/dx4 (constraint) = 3 a4' (evolution)"
          in general["constraint_propagation"])
check(stated, "a4-equations.json states rho' = -3 a4' (p3 - p_t), p3 + p_t = 2 p8 and "
              "the constraint propagation, as quoted",
      record="Revision/field_equations_a4/a4-equations.json, generalSource: "
             "conservation_reduced, algebraic_condition, constraint_propagation")
```

The record of the field equations must state the three consequences quoted in Section 11.22: the algebraic condition $p_3 + p_t = 2p_8$ (in Wolfram's notation), the reduced conservation law $\rho' = -3a_4'(p_3 - p_t)$, and the constraint propagation. Eighteenth PASS line.

**In [12], the end.**

```python
figure_files = [f"11c_{k}_{name}.png" for k, name in enumerate(
    ["components_linear_history", "lovelock_scalars", "test_history",
     "components_test_history", "conservation_identity"], 1)]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_files),
      "all five figure files of the notebook exist")
all_checks_passed()
```

The five figure files must exist (nineteenth PASS line), and the last line is ALL 19 CHECKS PASSED (notebook 11c). The 19 checks are: 1 in In [2], 2 in In [3], 5 in In [4], 2 in In [5], 1 each in In [6] to In [10], 3 in In [11] and 1 in In [12].

### 11.28 What we proved, what we computed, what we assumed

**PROVED in this chapter by derivations written out line by line** (each confirmed by a check of a notebook and, where named, of a Revision record):

- **The generalized Kronecker delta** (Sections 11.3 and 11.4): the author's determinant $\det[\delta(l_i, u_j)]$ is 0 when a label repeats in either list or a lower label is missing above, and otherwise the sign of the permutation that carries the lower list into the upper list; so the rule GKD of the Revision program is exactly the author's definition (Notebook 11a, In [2] to In [6]; record `Revision/gkd_lovelock/results/python-lovelock-report.json`, checks `gkd_examples` and `gkd_literal_equals_cofactor_expansion`). The number of nonzero values $8!/(8 - p)!\cdot p!$, half of them $+1$ and half $-1$ for $p \ge 2$, with the counts 8; 56 and 56; 1008 and 1008; 20160 and 20160 for $p = 1$ to 4 (In [6], In [7], In [9]; record `wolfram-gkd-report.json`, entry `gkdComparison`). Every delta with nine or more labels vanishes in eight dimensions (pigeonhole), so $P_{(4)} = 0$ and Lovelock's sum stops at order 3 (In [10]; record `lovelock-report.json`, check `k4_tensor_vanishes`). The rule needs $p(p - 1)/2$ comparisons instead of the $p!$ products of the determinant. The birthday probability $r_p = 8!/((8 - p)!\,8^p)$ of a nonzero rearranged random pair (with the assumed rules of probability).
- **The author's second route** (Section 11.5): for every matrix $N$, $\sum N_{i_1m_1}\cdots N_{i_nm_n}[m_1\dots m_n] = \det N\,[i_1\dots i_n]$; raising all labels of the Levi-Civita tensor of a metric gives the factor $\sqrt{|\det g|}/\det g$, so the product of two Levi-Civita tensors is the sign of $\det g$ times the product of two symbols; for the author's metric $\det g = \cos^2z > 0$ (record `python-lovelock-report.json`, check `sqrt_abs_det_g`), the sign is $+1$, and the author's second route gives the generalized delta without an extra sign.
- **The curvature that the sums use** (Section 11.10): the mixed components $R^{x_4k}{}_{x_8k} = \sigma_kHa_4'\cot z$ carry the sign $\sigma_k = \pm 1$ of inflation or deflation, not of the space-like or time-like character, and $R^{x_4}{}_{x_8} = 0$ because three inflating and three deflating directions cancel; every nonzero $R^{ab}{}_{cd}$ has the weight 2.
- **Laplace's rule** for determinants of every size, and **the expansion of every Lovelock tensor** along the column of its free upper label, $P_{(k)} = \delta\,L_{(k)} - 2k\,Y_{(k)}$ (Section 11.13; Notebook 11b, In [21]).
- **For every metric** (Sections 11.14 and 11.15): $L_{(1)} = 2R$, $P_{(1)} = -4G$, so $E_{(1)} = G$; the trace identity $\sum_hP_{(k)}{}^h{}_h = (8 - 2k)L_{(k)}$; $L_{(2)} = 4\,\mathrm{GB}$ and $P_{(2)} = -8\mathcal{H}$ with Lanczos's Gauss-Bonnet tensor $\mathcal{H}$, so $E_{(2)} = \mathcal{H}$ (Notebook 11b, In [18], In [19], In [22]; records `lovelock-report.json`, checks `k1_equals_minus_4_einstein`, `k1_trace_identity` to `k3_trace_identity`, and `python-lovelock-report.json`, checks `L1_equals_2R`, `k2_equals_minus_8_gauss_bonnet`, `L2_equals_4_gauss_bonnet`).
- **The structure of the components for the author's metric** (Section 11.21), for every history $a_4(x_4)$ and every order: only the diagonal is nonzero (in particular no $x_4$-$x_8$ component, by the relabelling that exchanges 3-space and the extra times); the three space components are equal, and so are the three extra-time components; $a_4''$ enters at most linearly; the time component is a polynomial in $a_4'^2$ and $H^2$ alone (the constraint); the extra-time component is the space component with $a_4''$ replaced by $-a_4''$, so their difference is $a_4''F_k(a_4')$ with $F_1 = 2$, $F_2 = -16(3a_4'^2 + 5H^2)$, $F_3 = 144(5a_4'^4 + 6a_4'^2H^2 + 5H^4)$ (the evolution factor; record `Revision/field_equations_a4/reports/python-a4-report.json`, check `evolution_factorises`); the hidden component contains no $a_4''$; every component is even in $a_4'$ (by reversing the time), so the tensors do not distinguish deflating from inflating extra times; order $k$ has the weight $2k$; and $E^{x_4}{}_{x_4} - E^{x_8}{}_{x_8} = 6(a_4'^2 + H^2)V_k$ (record check `linear_member_vacuum_factor`). Notebook 11c, In [2] to In [5], confirms each statement with exact algebra.
- **The two conservation identities** (Section 11.22), from zero divergence: $\frac{d}{dx_4}E^{x_4}{}_{x_4} = 3a_4'(E^{x_1}{}_{x_1} - E^{x_5}{}_{x_5})$ (I) and $E^{x_8}{}_{x_8} = \frac12(E^{x_1}{}_{x_1} + E^{x_5}{}_{x_5})$ (II), and the constraint propagation $\partial E^{x_4}{}_{x_4}/\partial a_4' = 3a_4'F_k$ (record `python-a4-report.json`, check `bianchi_x4`; Notebook 11c, In [4] and In [5]).
- **Along the linear history** (Section 11.23): only two different components per order, even in the slope $A$; the scalars $L_{(1)}$ and $L_{(2)}$ vanish exactly at $A = \sqrt 7$ and $A = \sqrt{2\sqrt{39} - 11}$; the derivatives of the illustrative test history.

**PROVED by exact computation** (no rounding; by the Revision's programs, recomputed by the notebooks):

- GKD equals the author's determinant for every one of the 266,304 pairs of lengths 1 to 3 (Notebook 11a, In [6]; records `python-lovelock-report.json`, check `gkd_literal_equals_cofactor_expansion`, and `wolfram-gkd-report.json`, checks `gkd_equals_kdelta_exhaustive_length_1` to `_length_3`) and for every one of the 16,777,216 pairs of length 4 (the Rust self-test, rerun in Notebook 11a, In [14], which reproduces `Revision/gkd_lovelock/results/gkd-selftest.json` byte for byte).
- The 25 nonzero Christoffel symbols, the 156 nonzero components $R^{ab}{}_{cd}$ and the Ricci scalar $R = 6a_4'^2 - 42H^2$ (Notebook 11b, In [6] to In [8]; records `curvature.json` and `python-lovelock-report.json`, check `rust_riemann_agrees`).
- All $3 \times 64$ components of $P_{(1)}, P_{(2)}, P_{(3)}$ and the scalars $L_{(1)}, L_{(2)}, L_{(3)}$, computed by the Rust program and again by the notebook's own GKD sum (Notebook 11b, In [3], In [4], In [14], In [15]; record `lovelock-tensors.json`, written again byte for byte; `python-lovelock-report.json`, checks `rust_k1_mixed_components_agree` to `rust_k3_mixed_components_agree` and `rust_L1_agrees` to `rust_L3_agrees`); the counters of the sums, 696, 32,640 and 495,360 GKD calls (In [14]; record `lovelock-report.json`, field `counters`); the literal sums of orders 1 and 2 without any skipping, with 10,140 and 1,581,840 GKD calls (In [16]; checks `k1_unpruned_literal_sum_agrees` and `k2_unpruned_literal_sum_agrees`); the cubic identity $L_{(3)} = 8(2T_1 + 8T_2 + \dots + T_8)$ for the author's metric (In [20]; check `L3_equals_8_cubic_lovelock_density`); zero divergence and symmetry of all three tensors (record `lovelock-report.json`, checks `k1_divergence_free` to `k3_symmetric`); the 19 checks of the Rust program, the 49 of the sympy verification and the 29 of the Wolfram verification, none failed (In [3] and In [24]).
- The components $E_{(1)}, E_{(2)}, E_{(3)}$ of Section 11.20 equal those recorded for the field equations of $a_4$ (Notebook 11c, In [3]; `Revision/field_equations_a4/reports/python-a4-report.json`, check `json_lovelock_components`).

**COMPUTED** (numerical, with the measured accuracy):

- The Rust program's literal unpruned sums at a numerical point agree with the exact tensors to the relative rounding errors $1.40 \times 10^{-15}$ ($k = 1$) and $4.41 \times 10^{-14}$ ($k = 2$) (record `lovelock-report.json`, checks `k1_brute_force_numeric` and `k2_brute_force_numeric`; Notebook 11b, In [4], requires both below $10^{-10}$).
- GKD equals the determinant on 12,000 pseudo-random pairs of lengths 4 to 9 (Notebook 11a, In [10]) and on 200,000 pairs of each length 5 to 9 (record `gkd-selftest.json`); the numbers of nonzero values lie within 1.6 standard deviations of the birthday expectation (In [11] and In [15]).
- The rule GKD is more than ten times faster than sympy's determinant for 200 pairs of length 7 (In [12]; the times themselves are not printed).
- The positive zero $A \approx 0.6010$ of $L_{(3)}$ on the linear history (Notebook 11c, In [7], 15 digits).
- Identity (I) along the illustrative test history by finite differences, to the relative deviations $3.8 \times 10^{-5}$, $4.0 \times 10^{-5}$, $4.5 \times 10^{-5}$ for $k = 1, 2, 3$, the size of the finite-difference error (Notebook 11c, In [10]).

**ASSUMED** (used, not proved here):

- The author's metric, as given in the Revision record, and the curvature convention of Misner, Thorne and Wheeler (Chapter 3).
- Lovelock's theorem in general: for every metric the tensors $P_{(k)}$ are divergence-free and symmetric, and they are the only such tensors built from the metric and its first and second derivatives (D. Lovelock, J. Math. Phys. 12, 498 (1971)). For the author's metric divergence and symmetry are not assumed but PROVED by exact computation.
- The general formula of the cubic Lovelock density (a classical result): the record derived its coefficients from literal sums on random curvature tensors, and checked the identity exactly for the author's metric; we do not derive it by hand.
- The tensor rule for a change of coordinates (Section 3.14), used for the time reversal and the relabelling; the rules of determinants of Section 1.20 (rule 1 for matrices larger than $2 \times 2$ is a standard theorem); that two polynomials that agree for all values of their variables have the same coefficients; the rules of probability used for the random tests (independent chances multiply; the expectation and the standard deviation of a count).

**HYPOTHESIS.** None: this chapter is geometry of the given metric.

**OPEN.** Whether nature has the couplings $\alpha_2$ and $\alpha_3$ of the Gauss-Bonnet and the cubic tensor, and which sign of $a_4'$ is realised, are not decided by the tensors computed here; Chapter 12 studies the field equations with the couplings as free parameters and shows that the sign of the deflation is set by the source and the initial data, not by gravity. The symmetry $A \to -A$ of this chapter is NOT the pairing of universes of masses $+m$ and $-m$ (Chapters 18 to 20); nothing in this chapter concerns the creation of universes or matter and antimatter.

### 11.29 Exercises

**Exercise 1.** Use the rule of Section 11.3 to compute (a) the delta with the lower list $(x_1, x_2, x_3, x_4)$ and the upper list $(x_3, x_1, x_4, x_2)$; (b) the delta with the lower list $(x_5, x_1, x_2)$ and the upper list $(x_1, x_2, x_5)$, and check (b) with the Leibniz formula; (c) the delta with the lower list $(x_1, x_2, x_8)$ and the upper list $(x_1, x_2, x_3)$.

*Answer.* (a) The places of $x_1, x_2, x_3, x_4$ in the upper list are 2, 4, 1, 3, so $\sigma = (2, 4, 1, 3)$. Its inversions are the pairs of entries $(2, 1)$, $(4, 1)$ and $(4, 3)$: three, an odd number, so the value is $-1$. (b) The places of $x_5, x_1, x_2$ in the upper list $(x_1, x_2, x_5)$ are 3, 1, 2: $\sigma = (3, 1, 2)$ with the two inversions $(3, 1)$ and $(3, 2)$, so the value is $+1$. The matrix has the rows $(0, 0, 1)$ ($x_5$ is the third upper label), $(1, 0, 0)$ and $(0, 1, 0)$; in the Leibniz formula only the permutation $\pi = (3, 1, 2)$ picks three ones, and its sign is $+1$, so $\det = +1$. (c) The lower label $x_8$ is not among the upper labels: row 3 is all zeros, case (c), and the value is 0.

**Exercise 2.** (a) How many of the $8^{10}$ pairs of index lists of length 5 have the value $+1$, how many $-1$, how many 0? (b) For the Rust self-test of length 6 (100,000 rearranged and 100,000 independent pairs), compute the expected number of nonzero values and its standard deviation, and compare with the record's count 7812.

*Answer.* (a) $N_{\ne 0}(5) = 8\cdot 7\cdot 6\cdot 5\cdot 4\cdot 5! = 6720\cdot 120 = 806400$ (Section 11.4), half of each sign: 403,200 values $+1$ and 403,200 values $-1$; the zeros are $8^{10} - 806400 = 1073741824 - 806400 = 1072935424$. (b) $r_6 = 8!/(2!\cdot 8^6) = 20160/262144 = 0.0769043$ and $q_6 = N_{\ne 0}(6)/8^{12} = 20160\cdot 720/68719476736 = 14515200/68719476736 = 0.000211$. The expectation is $100000\cdot(0.0769043 + 0.000211) = 7711.6$; the standard deviation is $\sqrt{100000\cdot 0.0769043\cdot 0.9230957 + 100000\cdot 0.000211\cdot 0.999789} = \sqrt{7099.0 + 21.1} = \sqrt{7120.1} = 84.4$. The record's 7812 lies $(7812 - 7711.6)/84.4 = 1.19$ standard deviations above the expectation, as Notebook 11a prints (In [15]).

**Exercise 3.** Compute the determinant of the matrix with the rows $(2, 1, 0)$, $(0, 1, 3)$, $(1, 0, 1)$ by Laplace's rule along its second column, and compare with the six-term formula, which gives 5.

*Answer.* The second column holds $M_{12} = 1$, $M_{22} = 1$, $M_{32} = 0$, with the signs $(-1)^{1+2} = -1$, $(-1)^{2+2} = +1$, $(-1)^{3+2} = -1$. The minor $M^{(12)}$ (row 1 and column 2 removed) has the rows $(0, 3)$ and $(1, 1)$, determinant $0\cdot 1 - 3\cdot 1 = -3$; the minor $M^{(22)}$ has the rows $(2, 0)$ and $(1, 1)$, determinant $2$. So $\det M = -1\cdot(-3) + 1\cdot 2 - 0 = 3 + 2 = 5$, the same value.

**Exercise 4.** In a space of $n$ dimensions, which orders $k$ of the Lovelock tensors $P_{(k)}$ can be nonzero, for $n = 4, 5, 6, 8, 10$? Which scalars $L_{(k)}$ can be nonzero in eight dimensions?

*Answer.* The delta of $P_{(k)}$ has $2k + 1$ labels in each list, so $P_{(k)}$ vanishes when $2k + 1 > n$ (pigeonhole, Section 11.4). Hence: $n = 4$: $k = 1$ only (Einstein); $n = 5$ and $n = 6$: $k = 1, 2$; $n = 8$: $k = 1, 2, 3$; $n = 10$: $k = 1, 2, 3, 4$. For even $n = 2m$ the highest order is $m - 1$, as in the formula of Section 11.11. The scalar $L_{(k)}$ has $2k$ labels per list, so in eight dimensions $L_{(1)}$ to $L_{(4)}$ can be nonzero: $L_{(4)}$ is the Euler density, whose tensor $P_{(4)}$ vanishes; for the author's metric it is $-663552H^2a_4'^6 - 442368H^4a_4'^4 - 663552H^6a_4'^2$ (Notebook 11b, In [3]).

**Exercise 5.** On the author's history $a_4 = Hx_4$ ($A = 1$): (a) write the Einstein tensor and $P_{(1)}$; (b) check the trace identity of order 1 with $L_{(1)}$.

*Answer.* (a) With $a_4' = H$ and $a_4'' = 0$ the components of Section 11.20 give $G^{x_1}{}_{x_1} = -3 + 15 = 12$, $G^{x_4}{}_{x_4} = 3 + 21 = 24$, $G^{x_5}{}_{x_5} = 12$, $G^{x_8}{}_{x_8} = 15 - 3 = 12$ (in units of $H^2$), so $G = \mathrm{diag}(12, 12, 12, 24, 12, 12, 12, 12)H^2$, and $P_{(1)} = -4G = \mathrm{diag}(-48, -48, -48, -96, -48, -48, -48, -48)H^2$. (b) The trace is $\sum_hP_{(1)}{}^h{}_h = -4(7\cdot 12 + 24)H^2 = -432H^2$. With $L_{(1)} = 12a_4'^2 - 84H^2 = -72H^2$, the identity gives $(8 - 2)L_{(1)} = 6\cdot(-72)H^2 = -432H^2$: the same.

**Exercise 6.** On the same history $A = 1$: compute the four independent components of $E_{(2)}$, then $P_{(2)}$, $L_{(2)}$, and check the trace identity of order 2. What is special about the Gauss-Bonnet tensor on this history?

*Answer.* With $a_4' = H$, $a_4'' = 0$ (units of $H^4$): $E_{(2)}{}^{x_1}{}_{x_1} = 12 + 168 - 180 = 0$; $E_{(2)}{}^{x_4}{}_{x_4} = -36 - 120 - 420 = -576$; $E_{(2)}{}^{x_5}{}_{x_5} = 12 + 168 - 180 = 0$; $E_{(2)}{}^{x_8}{}_{x_8} = 12 + 168 - 180 = 0$. So $P_{(2)} = -8E_{(2)} = \mathrm{diag}(0, 0, 0, 4608, 0, 0, 0, 0)H^4$ and its trace is $4608H^4$. $L_{(2)} = -96 - 2112 + 3360 = 1152$ (units of $H^4$), and $(8 - 4)L_{(2)} = 4608$: the identity holds. On the author's history the Gauss-Bonnet tensor $E_{(2)}$ has only its time component; all seven other components vanish, because $12A^4 + 168A^2 - 180 = 12(A^2 - 1)(A^2 + 15)$ is zero at $A = 1$ (multiply out: $12(A^4 + 14A^2 - 15)$).

**Exercise 7.** Check identity (I) of Section 11.22 for $k = 3$ by hand, from the components of Section 11.20.

*Answer.* The time component $E_{(3)}{}^{x_4}{}_{x_4} = 360a_4'^6 + 648a_4'^4H^2 + 1080a_4'^2H^4 + 2520H^6$ depends on $x_4$ only through $a_4'$, so its derivative is $\frac{d}{dx_4}E^{x_4}{}_{x_4} = (2160a_4'^5 + 2592a_4'^3H^2 + 2160a_4'H^4)\,a_4''$ (the chain rule; $6\cdot 360 = 2160$, $4\cdot 648 = 2592$, $2\cdot 1080 = 2160$). The difference of the space and the extra-time component is $E^{x_1}{}_{x_1} - E^{x_5}{}_{x_5} = 720a_4'^4a_4'' + 864a_4'^2a_4''H^2 + 720a_4''H^4$ (every term without $a_4''$ cancels, every term with $a_4''$ doubles). Then $3a_4'(E^{x_1}{}_{x_1} - E^{x_5}{}_{x_5}) = (2160a_4'^5 + 2592a_4'^3H^2 + 2160a_4'H^4)a_4''$, which is the same. So (I) holds, and $F_3 = 720a_4'^4 + 864a_4'^2H^2 + 720H^4 = 144(5a_4'^4 + 6a_4'^2H^2 + 5H^4)$.

**Exercise 8.** Check identity (II) for $k = 3$, and explain without any computation why $E^{x_8}{}_{x_8}$ contains no $\cot z$ for every order.

*Answer.* $\frac12(E^{x_1}{}_{x_1} + E^{x_5}{}_{x_5})$: the terms with $a_4''$ have opposite signs in the two components and cancel; the others are equal, so the mean is $-72a_4'^6 - 648a_4'^4H^2 - 1944a_4'^2H^4 + 360H^6$, which is $E_{(3)}{}^{x_8}{}_{x_8}$. Without computation: in $P^{x_8}{}_{x_8}$ the label $x_8$ already stands in both lists of the delta, so no curvature factor may carry $x_8$ (case a or b); every entry with $\cot z$ or $\tan z$ is a mixed entry and carries $x_8$ (Section 11.21, tool iii); so none occurs, and the factors are plane curvatures among $x_1, \dots, x_7$, which contain no $z$.

**Exercise 9.** Show that $L_{(3)}$ has exactly one positive zero on the linear history, and locate it between two decimals.

*Answer.* With $u = A^2$ and $H = 1$, $L_{(3)} = 1152u^3 + 31104u^2 + 100224u - 40320 = 1152\,f(u)$ with $f(u) = u^3 + 27u^2 + 87u - 35$ (divide by 1152: $31104/1152 = 27$, $100224/1152 = 87$, $40320/1152 = 35$). For $u > 0$ the derivative $f'(u) = 3u^2 + 54u + 87$ is positive, so $f$ increases; $f(0) = -35 < 0$ and $f(1) = 1 + 27 + 87 - 35 = 80 > 0$, so $f$ has exactly one zero for $u > 0$, between 0 and 1. Further, $f(0.3612) = 0.04712 + 3.52255 + 31.42440 - 35 = -0.0059$ and $f(0.3613) = 0.04716 + 3.52450 + 31.43310 - 35 = +0.0048$, so the zero lies between $u = 0.3612$ and $0.3613$, and $A = \sqrt u$ between 0.60100 and 0.60108, in agreement with $A = 0.6010$ of Notebook 11c (In [7]).

**Exercise 10.** (a) In two dimensions with the metric $g = \mathrm{diag}(1, -1)$ (one space-like, one time-like direction), compute $\varepsilon_{12}\varepsilon^{12}$ with the rule of Section 11.5. (b) The same with $g = \mathrm{diag}(-1, -1)$. (c) What decides the sign, and what is it for the author's metric?

*Answer.* (a) $|\det g| = 1$, so $\varepsilon_{12} = [12] = 1$, and $\varepsilon^{12} = g^{11}g^{22}\varepsilon_{12} = 1\cdot(-1)\cdot 1 = -1$; the product is $-1$, the sign of $\det g = -1$. (b) $\varepsilon^{12} = (-1)(-1)\cdot 1 = +1$, the product is $+1$, the sign of $\det g = +1$. (c) The sign of $\det g$, which for a diagonal metric is $(-1)$ to the number of negative entries: the number of time-like directions. The author's metric has four, $\det g = \cos^2z > 0$, and the sign is $+1$.

**Exercise 11.** For the illustrative test history of Section 11.23, compute $a_4'$ and $a_4''$ at $x_4 = 0$, and the four components of $E_{(1)}$ there. Check identity (II).

*Answer.* $a_4'(0) = H(1 + \frac12\tanh 0) = H$ and $a_4''(0) = \frac{H^2}{2}\mathrm{sech}^2\,0 = \frac{H^2}{2}$. Then (units of $H^2$): $E^{x_1}{}_{x_1} = -3 + \frac12 + 15 = 12.5$, $E^{x_4}{}_{x_4} = 3 + 21 = 24$, $E^{x_5}{}_{x_5} = -3 - \frac12 + 15 = 11.5$, $E^{x_8}{}_{x_8} = -3 + 15 = 12$. Identity (II): $\frac12(12.5 + 11.5) = 12 = E^{x_8}{}_{x_8}$. The space and extra-time components differ by $a_4''F_1 = \frac12\cdot 2 = 1$, as in Figure 11c.4 at $x_4 = 0$.
