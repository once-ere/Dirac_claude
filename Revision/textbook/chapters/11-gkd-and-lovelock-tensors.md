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

`all_different` is $r_p = 8!/((8 - p)!\,8^p)$ of Section 11.4, and 0 for more than 8 labels. `expected_nonzero` returns the expectation $N(r_p + q_p)$ and the standard deviation $\sqrt{Nr_p(1 - r_p) + Nq_p(1 - q_p)}$ for `half` $= N$ rearranged and $N$ independent samples (`math.sqrt` is the square root).

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
