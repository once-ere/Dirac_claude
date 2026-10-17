# The generalized Kronecker delta and the Lovelock tensors of the author's primordial metric

## GKD, the pure-Rust generalized Kronecker delta, and the exact Lovelock tensors of order k = 1, 2, 3 of Lovelock's equation (4.38) for the corrected 4+4 primordial metric with deflating extra times, with their independent verifications and an exact statement of what they establish

## Abstract

This document records the computation of `Revision/gkd_lovelock`: the generalized Kronecker delta of the author's notebook, re-implemented in pure Rust as the function GKD, and the three nonzero Lovelock tensors $P_{(1)}$, $P_{(2)}$, $P_{(3)}$ of Lovelock's equation (4.38) for the corrected primordial metric of 2026-10-16 (version 2) of signature (4,4), in which 3-space inflates as $e^{a_4(x_4)}$ while the hidden direction $x_0$ and the three extra times $x_5, x_6, x_7$ share the deflating scale factor $e^{-a_4(x_4)}b_4(x_4)^{1/2}$, for every real $z = 6Hx_0$. Every component of $P_{(k)}$ is exact: a polynomial in $H$, $a_4'$, $a_4''$, $u = b_4'/b_4$, $v = u'$ and $k = e^{2a_4}/b_4$. Every $P_{(k)}$ is diagonal, free of $x_0$, with equal components in the three 3-space directions and equal components in the hidden direction and the three extra times; $P_{(4)} = 0$ identically in eight dimensions. The Rust program checks 27 identities (27 of 27 pass); GKD equals the author's determinant on all 16,777,216 pairs of index lists of length 4 and on 200,000 pseudo-random pairs of each length 5 to 9. Two independent verifications agree with every component: a Wolfram Language check that evaluates the author's definition verbatim (29 of 29 checks pass) and a sympy checker that shares no code with the Rust program (56 of 56 checks pass). The field equations for $a_4$ and $b_4$ use these tensors with the normalisation $E_{(k)} = -P_{(k)}/2^{k+1}$, $E_{(1)} = G$; with the author's Lovelock weights they give, on the history $a_4 = Hx_4$, $b_4 = b_4(0)e^{(4/3)Hx_4}$, exactly the source that this history needs, a polynomial in $k$. The author's stored outputs belong to the withdrawn metric of 2026-10-14; they are compared with the frozen record of that metric (`Revision/gkd_lovelock/comparison/`; 80 checks: 75 PASS, 0 FAIL, 5 NOT-AVAILABLE): the author's metric, Ricci scalar and all 64 components of the author's Einstein tensor equal that record exactly under a function mapping stated before the comparison; no author output exists for the corrected metric, and in the two notebooks of the author in the repository a keyword scan finds no stored output of the Lovelock tensors of order $k = 2$ and $k = 3$. Not established here: any solution of the field equations, anything at the points $\sin z\cos z = 0$ where the metric degenerates, and agreement with any Lovelock tensor of order $k = 2$ or $k = 3$ computed by the author.

## 1. The task and the result

The author's test (2026-10-01, `Revision/README.md` and `Revision/SPEC.md` sections 5 and 10): refactor the author's Wolfram Language definition of the generalized Kronecker delta into a pure-Rust function GKD, use it to compute, with provenance, the three nonzero Lovelock tensors of Lovelock's equation (4.38) for the author's 8 x 8 metric, write every component, and do the work without reading the author's answers. On 2026-10-16 the metric became the corrected primordial metric (version 2, `Revision/SPEC.md` section 1), and the record was recomputed for it. The result, in one paragraph each:

1. GKD (section 3). For index lists of equal length, GKD returns the determinant of the author's 0/1 matrix without computing a determinant: it is the sign of the permutation that maps the lower list onto the upper list, or 0. The equality with the author's definition is a theorem (section 3.2), confirmed exhaustively and on random samples by three programs.
2. The Lovelock tensors (sections 4 to 6). $P_{(k)}{}^h{}_j$, $A_{(k)}{}^{lh}$ and $L_{(k)}$ for $k = 1, 2, 3$ are computed exactly from the metric alone, with every term of the sums weighted by an explicit call of GKD. Their nonzero components are listed in section 6.3.
3. The verifications (sections 7 and 10). The Rust program, the Wolfram check and the sympy checker agree exactly on every one of the 64 components of each tensor; every check of the three reports has the verdict PASS.
4. The use (section 9). The field equations for $a_4$ and $b_4$ of `Revision/field_equations_a4` recompute the three tensors in both of their verifiers and compare them with the file of this record.
5. The comparison with the author (sections 8.2 and 8.4). Made after the computation: under the mapping stated before the comparison, the stored metric, Ricci scalar and Einstein tensor of the author's earlier notebook equal those of the frozen record of the metric of 2026-10-14 at $b_4 = 1$ exactly, component by component; for $k = 2$ and $k = 3$ that notebook holds no output to compare with, and for the corrected metric no author output exists.

Every formula and number below is taken from the Revision files named with it; nothing is taken from the earlier stages of the repository. Interpretations are labelled as such.

## 2. Setting and conventions

### 2.1 The author's metric and coordinates

The coordinates are the author's, $x_0, x_1, \dots, x_7$, in the author's order; arrays index them $0, \dots, 7$ (index $k$ is $x_k$). $x_0$ is the hidden space direction with $z = 6Hx_0$, which takes every real value; $x_1, x_2, x_3$ are ordinary 3-space, which inflates with the scale factor $e^{a_4}$; $x_4$ is the time; $x_5, x_6, x_7$ are the three extra times, time-like, which DEFLATE exponentially with the scale factor $e^{-a_4}b_4^{1/2}(\sin^2z)^{1/12}$ as $a_4(x_4)$ increases (they are never treated as static), and the hidden direction shares the factor $e^{-a_4}b_4^{1/2}$; $H > 0$ is the author's constant and $a_4' = da_4/dx_4$. The metric of `Revision/SPEC.md` section 1 (the corrected primordial metric of 2026-10-16, version 2), as the Rust program stores it (`metricDiagonal` of `curvature.json`), is

$$
\begin{aligned}
g = \mathrm{diag}\big(& e^{-2a_4}b_4\cot^2 z,\ e^{2a_4},\ e^{2a_4},\ e^{2a_4},\ -1, \\
& -e^{-2a_4}b_4(\sin^2z)^{1/6},\ -e^{-2a_4}b_4(\sin^2z)^{1/6},\ -e^{-2a_4}b_4(\sin^2z)^{1/6}\big),
\end{aligned}
$$

with the metric function $b_4(x_4) > 0$ ($b_4$ is a function of the time and never 1) and $(\sin^2z)^{1/6}$ on the positive branch (the author's $\sin^{1/3}z$), of signature (4,4): space-like $x_0, x_1, x_2, x_3$, time-like $x_4, x_5, x_6, x_7$. Its determinant is $\det g = e^{-2a_4}b_4^4\cot^2z\,(\sin^2z)^{1/2}$, so $\sqrt{|g|} = e^{-a_4}b_4^2|\cot z|(\sin^2z)^{1/4}$, positive for every real $z$ with $\sin z\cos z \neq 0$; the Rust program writes it with the sign symbol $\mathrm{sgn}(\cot z)$ as $e^{-a_4}(\sin^2z)^{1/4}\cot z\,\mathrm{sgn}(\cot z)\,b_4^2$ (`sqrtAbsDetG`). The proper 7-volume grows like $e^{3a_4}(e^{-a_4}b_4^{1/2})^4 = e^{-a_4}b_4^2$. Below, $u = b_4'/b_4$ and $v = u'$ (so $b_4''/b_4 = v + u^2$), $k = e^{2a_4}/b_4$, and the log-derivative of the block scale factor $e^{-a_4}b_4^{1/2}$ is $-(a_4' - u/2)$. The Revision's Kohn-Sham record uses the history $a_4 = Hx_4$, $b_4 = b_4(0)e^{(4/3)Hx_4}$, on which $a_4' = H$, $u = \frac43H$, $a_4' - u/2 = H/3$ and $k = b_4(0)^{-1}e^{(2/3)Hx_4}$ (section 9). The metrics of 2026-10-14 (with $\sin^{1/3}z$ on 3-space and $\cot^2z$ alone in $g_{00}$) and of 2026-10-16 version 1 are withdrawn (section 8.4).

### 2.2 Curvature conventions

Stated in `Revision/gkd_lovelock/code/src/geometry.rs` and used by all three programs:

- Christoffel symbols $\Gamma^a{}_{bc} = \frac12 g^{ad}(\partial_b g_{dc} + \partial_c g_{db} - \partial_d g_{bc})$.
- Riemann tensor (Misner-Thorne-Wheeler) $R^a{}_{bcd} = \partial_c\Gamma^a{}_{bd} - \partial_d\Gamma^a{}_{bc} + \Gamma^a{}_{ce}\Gamma^e{}_{bd} - \Gamma^a{}_{de}\Gamma^e{}_{bc}$; a round 2-sphere of radius $r$ has $R^{12}{}_{12} = +1/r^2$.
- $R^{ab}{}_{cd} = g^{be}R^a{}_{ecd}$; Ricci $R_{bd} = R^a{}_{bad}$, so $R^h{}_j = R^{ha}{}_{ja}$; $R = R^{ab}{}_{ab}$; Einstein $G^h{}_j = R^h{}_j - \frac12\delta^h_jR$.

## 3. The generalized Kronecker delta

### 3.1 The author's definition

The cell stored as `In[87]` in the author's notebook `Generalized _Kronecker_Delta_4+4.nb` (the author's `In[54]`) defines

```text
kδ[lower_, upper_] /; Length[lower] == Length[upper] := Det[Outer[delta, lower, upper]]
```

For lists $l = (l_1, \dots, l_p)$ and $u = (u_1, \dots, u_p)$ the matrix `Outer[delta, lower, upper]` has the entries $M_{ij} = \delta(l_i, u_j)$ (1 if $l_i = u_j$, otherwise 0), and

$$
\delta^{u_1\cdots u_p}_{l_1\cdots l_p} = \det\big[\delta(l_i, u_j)\big]_{i,j=1}^{p} .
$$

For lists of different length the definition does not apply and the expression stays unevaluated. Because $\det M = \det M^T$, exchanging the two lists does not change the value.

### 3.2 GKD and the proof that it equals the definition

**Theorem (GKD).** For lists of equal length $p$, $\det M = 0$ if two lower indices are equal, if two upper indices are equal, or if some lower index is not among the upper indices; otherwise $\det M = \mathrm{sign}(\sigma)$, where $\sigma$ is the permutation with $l_i = u_{\sigma(i)}$.

Proof (the comment of `Revision/gkd_lovelock/code/src/gkd.rs`). (a) Two equal lower indices give two equal rows of $M$, so $\det M = 0$. (b) Two equal upper indices give two equal columns, so $\det M = 0$. (c) A lower index $l_i$ that is not among the upper indices gives a zero row $i$, so $\det M = 0$. (d) Otherwise both lists consist of $p$ distinct indices and every $l_i$ equals exactly one $u_{\sigma(i)}$; $M$ has a single 1 in each row $i$, in column $\sigma(i)$, so it is the permutation matrix of $\sigma$, and in the Leibniz formula only the term of $\sigma$ survives: $\det M = \mathrm{sign}(\sigma)$. QED.

`gkd.rs::GKD` implements cases (a) to (d) with a position table and counts the inversions of $\sigma$: $O(p^2)$ integer operations ($p \le 64$) instead of a $p \times p$ determinant. With more than eight indices over eight values two indices of a list are always equal (pigeonhole), so GKD is 0. `gkd.rs::kdelta_det` is a literal transcription of the definition (the Leibniz determinant of the 0/1 matrix, permutations by Heap's algorithm) used only to test GKD.

### 3.3 The self-test of GKD

`lovelock_gkd gkd-selftest --exhaustive-max 4` compares GKD with `gkd.rs::kdelta_det` on every pair of index lists of length 1 to 4 over the eight labels and on 200,000 pseudo-random pairs (xorshift64*, half of them permutations of each other) of each length 5 to 9. The self-test does not depend on the metric, so it was not re-run for the corrected metric. The report `Revision/gkd_lovelock/results/gkd-selftest.json` has the verdict `SUCCESS`:

| length $p$ | mode | pairs | nonzero values | mismatches |
| --- | --- | --- | --- | --- |
| 1 | exhaustive | 64 | | 0 |
| 2 | exhaustive | 4096 | | 0 |
| 3 | exhaustive | 262144 | | 0 |
| 4 | exhaustive | 16777216 | | 0 |
| 5 | random | 200000 | 20538 | 0 |
| 6 | random | 200000 | 7812 | 0 |
| 7 | random | 200000 | 1949 | 0 |
| 8 | random | 200000 | 244 | 0 |
| 9 | random | 200000 | 0 | 0 |

At length 9 (nine indices over eight values) no pair has a nonzero value, as the pigeonhole argument requires. The Lovelock program records two values of GKD itself (`gkdSelfCheck` of `lovelock-report.json`): $+1$ for a 3-cycle (`length3Pair`) and $-1$ for a transposition (`transposition`).

## 4. The Lovelock tensors

### 4.1 Lovelock's equation (4.38)

The cell stored as `In[101]` in the author's notebook (the author's `In[68]`) is a picture of Lovelock's equation (4.38) (Lovelock and Rund), rendered to `Revision/gkd_lovelock/results/notebook-in68-image.png` and read from that picture. In $n$ dimensions, with arbitrary constants $\alpha_{(k)}$ and $\lambda$ and $m = n/2$ for even $n$,

$$
A^{lh} = \sqrt{g}\sum_{k=1}^{m-1}\alpha_{(k)}\,g^{jl}\,\delta^{hh_1\cdots h_{2k}}_{jj_1\cdots j_{2k}}\,R^{j_1j_2}{}_{h_1h_2}\cdots R^{j_{2k-1}j_{2k}}{}_{h_{2k-1}h_{2k}} + \lambda\sqrt{g}\,g^{lh} .
$$

For the author's metric $n = 8$ and $m = 4$, so the sum runs over $k = 1, 2, 3$; $\sqrt{g}$ means $\sqrt{|\det g|} = e^{-a_4}b_4^2|\cot z|(\sin^2z)^{1/4}$ (section 2.1).

### 4.2 Definitions and index conventions of this record

For $k = 1, 2, 3$ (`lovelock-tensors.json`, key `definition`):

$$
\begin{aligned}
P_{(k)}{}^h{}_j &= \delta^{hh_1\cdots h_{2k}}_{jj_1\cdots j_{2k}}\,R^{j_1j_2}{}_{h_1h_2}\cdots R^{j_{2k-1}j_{2k}}{}_{h_{2k-1}h_{2k}} \\
&= \sum \mathrm{GKD}\big([j,j_1,\dots,j_{2k}],[h,h_1,\dots,h_{2k}]\big)\prod_{i=1}^{k}R^{j_{2i-1}j_{2i}}{}_{h_{2i-1}h_{2i}} ,\\
L_{(k)} &= \delta^{h_1\cdots h_{2k}}_{j_1\cdots j_{2k}}\,R^{j_1j_2}{}_{h_1h_2}\cdots R^{j_{2k-1}j_{2k}}{}_{h_{2k-1}h_{2k}} ,\\
A_{(k)}{}^{lh} &= \sqrt{|g|}\,g^{jl}\,P_{(k)}{}^h{}_j ,
\end{aligned}
$$

summed over all repeated indices. Conventions, stated once:

- The lower list of GKD is $[j, j_1, \dots, j_{2k}]$ (the lower indices of $\delta$, which carry the UPPER index pairs of the curvature factors) and the upper list is $[h, h_1, \dots, h_{2k}]$; in the code (`lovelock.rs::dfs`) the upper pair $a, b$ of a factor $R^{ab}{}_{cd}$ joins the lower row of $\delta$ and the lower pair $c, d$ joins the upper row. The field-equations branch writes the lists in the other order; by section 3.1 the value is the same.
- $P_{(k)}$ is stored with its first index up and its second down (`P1_mixed_up_h_down_j`, `P2_mixed_up_h_down_j`, `P3_mixed_up_h_down_j`); $A_{(k)}$ with both indices up (`A1_contravariant_l_h`, `A2_contravariant_l_h`, `A3_contravariant_l_h`). For the diagonal metric $A_{(k)}{}^{lh} = \sqrt{|g|}\;g^{ll}\,P_{(k)}{}^h{}_l$.
- In this notation equation (4.38) reads $A^{lh} = \sum_{k=1}^{3}\alpha_{(k)}A_{(k)}{}^{lh} + \lambda\sqrt{|g|}\,g^{lh}$.

### 4.3 Normalisations

$P_{(k)}$ carries the normalisation of the $\delta$ sum. The usual normalised Lovelock tensors are (`lovelock-tensors.json`, key `normalisationNote`; `lovelock.rs::usual_normalisation`)

$$
E_{(k)}{}^h{}_j = -\frac{P_{(k)}{}^h{}_j}{2^{k+1}},\qquad E_{(1)} = G ,
$$

with the following exact relations, derived in the docstring of `Revision/gkd_lovelock/verification/check_lovelock_gkd.py` by the Laplace expansion of the determinant, $P_{(k)}{}^h{}_j = \delta^h_jL_{(k)} - 2k\,\delta^{h_1\cdots h_{2k}}_{jj_2\cdots j_{2k}}R^{hj_2}{}_{h_1h_2}\cdots$, and verified for this metric:

- $k = 1$: $P_{(1)} = 2R\,\delta - 4\,\mathrm{Ric} = -4G$ and $L_{(1)} = 2R$ (`k1_equals_minus_4_einstein`, `L1_equals_2R`).
- $k = 2$: $P_{(2)} = -8\mathcal{H}$, with the Gauss-Bonnet (Lanczos) tensor $\mathcal{H}^h{}_j = 2(RR^h{}_j - 2R^h{}_aR^a{}_j - 2R^{ha}{}_{jb}R^b{}_a + R^{habc}R_{jabc}) - \frac12\delta^h_j(R^2 - 4R_{ab}R^{ab} + R_{abcd}R^{abcd})$, and $L_{(2)} = 4(R^2 - 4R^a{}_bR^b{}_a + R^{ab}{}_{cd}R^{cd}{}_{ab})$ (`k2_equals_minus_8_gauss_bonnet`, `L2_equals_4_gauss_bonnet`, `gauss_bonnet_index_placement`).
- $k = 3$: $L_{(3)} = 8(2T_1 + 8T_2 + 24T_3 + 3T_4 + 24T_5 + 16T_6 - 12T_7 + T_8)$ with the cubic invariants $T_1 = R^{ab}{}_{cd}R^{cd}{}_{ef}R^{ef}{}_{ab}$, $T_2 = R^{ab}{}_{cd}R^{ce}{}_{bf}R^{df}{}_{ae}$, $T_3 = R^{ab}{}_{cd}R^{cd}{}_{be}R^e{}_a$, $T_4 = R\,R^{ab}{}_{cd}R^{cd}{}_{ab}$, $T_5 = R^{ab}{}_{cd}R^c{}_aR^d{}_b$, $T_6 = R^a{}_bR^b{}_cR^c{}_a$, $T_7 = R\,R^a{}_bR^b{}_a$ and $T_8 = R^3$ (`L3_equals_8_cubic_lovelock_density`).
- The constants are also derived, not only assumed: from literal $\delta$ sums on random algebraic curvature tensors, $P_{(1)}/G$ takes the single value $-4$ in $d = 4$, $P_{(2)}/\mathcal{H}$ the single value $-8$ in $d = 5$, and in $d = 6$ the 9 x 8 system of nine random tensors has rank 8 with the unique solution c = [16, 64, 192, 24, 192, 128, -96, 8] = 8 x [2, 8, 24, 3, 24, 16, -12, 1] (`normalisation_P1_derived_minus_4`, `normalisation_P2_derived_minus_8`, `normalisation_L3_cubic_derived`).
- Trace identity: $\sum_hP_{(k)}{}^h{}_h = (n - 2k)L_{(k)} = (8 - 2k)L_{(k)}$.

### 4.4 Why the series stops at k = 3

$P_{(4)}$ would need $\delta$ with $2\cdot4 + 1 = 9$ upper and 9 lower indices over eight values: two indices of each list are equal, so every term vanishes and $P_{(4)} = 0$ identically (`k4_tensor_vanishes`, `k4_terms_vanish_literally`, `gkd_nine_indices_in_eight_dimensions_vanish`; `lovelock-tensors.json` key `k4`: “identically zero (GKD of 9 indices in 8 dimensions)”). Equation (4.38) stops at $k = m - 1 = 3$, so $k = 1, 2, 3$ is the complete series in eight dimensions.

## 5. How the code computes them

### 5.1 The crate

`Revision/gkd_lovelock/code` is the Rust crate `lovelock_gkd` (edition 2021, no dependencies, its own empty workspace). Its modules:

| file | function or type | what it does |
| --- | --- | --- |
| `gkd.rs` | `gkd.rs::GKD` | the generalized Kronecker delta by cases (a) to (d) of section 3.2 |
| `gkd.rs` | `gkd.rs::kdelta_det`, `gkd.rs::compare_exhaustive`, `gkd.rs::compare_random` | the literal Leibniz determinant and the two self-test loops |
| `rational.rs` | `rational.rs::Rational` | exact rationals on `i128`; every operation that would overflow stops with a message |
| `poly.rs` | `poly.rs::Poly`, `poly.rs::d` | exact Laurent polynomials with rational coefficients in the fourteen symbols $H$, $a_4'$ to $a_4''''$, $E = e^{a_4}$, $W = (\sin^2z)^{1/12}$, $C = \cot z$, $Q = b_4^{1/2}$, $b_4'$ to $b_4''''$ and $G = \mathrm{sgn}(\cot z)$, with the exact derivatives in $x_0$ and $x_4$ |
| `geometry.rs` | `geometry.rs::metric_diagonal`, `geometry.rs::Geometry` | the metric, its inverse, $\sqrt{\lvert g\rvert} = G\,C\,E^{-1}Q^4W^3$, the Christoffel symbols, $R^a{}_{bcd}$, $R^{ab}{}_{cd}$, Ricci and $R$ |
| `geometry.rs` | `geometry.rs::nonzero_mixed`, `geometry.rs::einstein_mixed` | the list of nonzero $R^{ab}{}_{cd}$; the Einstein tensor from the Ricci tensor |
| `lovelock.rs` | `lovelock.rs::lovelock_mixed`, `lovelock.rs::lovelock_scalar`, `lovelock.rs::dfs` | $P_{(k)}{}^h{}_j$ and $L_{(k)}$ by a depth-first search over the nonzero curvature entries |
| `lovelock.rs` | `lovelock.rs::lovelock_contravariant`, `lovelock.rs::divergence` | $A_{(k)}{}^{lh}$; the covariant divergence $\nabla_hP^h{}_j$ |
| `lovelock.rs` | `lovelock.rs::brute_force_numeric`, `lovelock.rs::usual_normalisation` | the unpruned literal sum at a numerical point; the factor $-1/2^{k+1}$ |
| `output.rs` | `output.rs::tensor_json`, `output.rs::monomials_json`, `output.rs::tensor_markdown` | deterministic JSON and Markdown writers |
| `main.rs` | `main.rs::gkd_selftest`, `main.rs::run_lovelock`, `main.rs::print_config` | the command line `gkd-selftest`, `lovelock`, `print-config` |

Every component of the metric is a monomial in these symbols: $g_{00} = E^{-2}Q^2C^2$, $g_{x_ix_i} = E^2$, $g_{44} = -1$, $g_{x_tx_t} = -E^{-2}Q^2W^2$. The symbols $W$ and $C$ satisfy $W^{12}(1 + C^2) = 1$, so the representation of `poly.rs` is not canonical in general; $W$, $C$ and $G$ cancel identically in every mixed tensor the program prints, every zero test is done on mixed tensors, and the independent checkers use a canonical form (section 7). In the result files every term is `[numerator, denominator, [fourteen exponents]]`.

### 5.2 The enumeration

For each pair $(h, j)$, `lovelock.rs::dfs` chooses $k$ ordered nonzero entries $R^{ab}{}_{cd}$ one after another and appends $a, b$ to the lower list and $c, d$ to the upper list. A branch is cut when an index would repeat within a list (GKD is 0 by cases (a) and (b)); at a leaf the two index SETS must be equal (otherwise GKD is 0 by case (c)), and only then is GKD called; a nonzero value multiplies the product of the chosen entries. A vanishing curvature factor gives a vanishing term, so only the nonzero entries are enumerated. The counters of `lovelock-report.json`:

| $k$ | leaves | GKD calls | nonzero GKD values | GKD calls for $L_{(k)}$ | nonzero components of $P_{(k)}$ |
| --- | --- | --- | --- | --- | --- |
| 1 | 4032 | 672 | 672 | 112 | 8 |
| 2 | 107520 | 26880 | 26880 | 6720 | 8 |
| 3 | 645120 | 322560 | 322560 | 161280 | 8 |
| 4 | 0 | 0 | 0 | 645120 | 0 |

The pruning is checked, not assumed: `lovelock.rs::brute_force_numeric` evaluates the completely unpruned literal sum, every index list sent to GKD, at the point $H = 0.23$, $a_4 = 0.17$, $a_4' = 0.61$, $a_4'' = -0.37$, $b_4 = 1.37$, $b_4' = 0.31$, $b_4'' = -0.23$, $x_0 = 0.41$: 262144 index lists for $k = 1$ (maximal relative deviation from the exact $P_{(1)}$ 7.86e-16) and 1073741824 index lists for $k = 2$ (maximal relative deviation from the exact $P_{(2)}$ 3.57e-13) (`k1_brute_force_numeric`, `k2_brute_force_numeric`). The two independent checkers repeat the unpruned sums exactly (section 7).

## 6. Results

### 6.1 Christoffel symbols and curvature

The formulas of this section are read from `curvature.json` and written in $a_4'$, $a_4''$, $u = b_4'/b_4$, $v = u'$ and $k = e^{2a_4}/b_4$, for every real $z$ with $\sin z\cos z \neq 0$.

`curvature.json` lists 21 nonzero Christoffel symbols $\Gamma^a{}_{bc}$ with $b \le c$. With $i = 1, 2, 3$ (3-space) and $t = 5, 6, 7$ (extra times):

$$
\begin{aligned}
&\Gamma^{x_i}{}_{x_ix_4} = a_4',\quad \Gamma^{x_t}{}_{x_4x_t} = \Gamma^{x_0}{}_{x_0x_4} = -(a_4' - u/2),\quad \Gamma^{x_t}{}_{x_0x_t} = H\cot z,\\
&\Gamma^{x_4}{}_{x_ix_i} = a_4'e^{2a_4},\quad \Gamma^{x_4}{}_{x_tx_t} = (a_4' - u/2)\,e^{-2a_4}b_4(\sin^2z)^{1/6},\quad \Gamma^{x_4}{}_{x_0x_0} = -(a_4' - u/2)\,e^{-2a_4}b_4\cot^2z,\\
&\Gamma^{x_0}{}_{x_tx_t} = H(\sin^2z)^{1/6}\tan z,\quad \Gamma^{x_0}{}_{x_0x_0} = -6H\tan z - 6H\cot z .
\end{aligned}
$$

The mixed Riemann tensor $R^{ab}{}_{cd}$ has 112 nonzero entries, all sectional, $\{c, d\} = \{a, b\}$: four entries for each of the 28 coordinate planes, with no mixed component such as $R^{x_5x_0}{}_{x_5x_4}$ (`mixed_riemann_only_sectional`). Up to the antisymmetry in each index pair they are, with $i \ne i'$ in 3-space and $t \ne t'$ among the extra times:

| entry | value |
| --- | --- |
| $R^{x_ix_{i'}}{}_{x_ix_{i'}}$ | $(a_4')^2$ |
| $R^{x_ix_4}{}_{x_ix_4}$ | $a_4'' + (a_4')^2$ |
| $R^{x_ix_0}{}_{x_ix_0}$ and $R^{x_ix_t}{}_{x_ix_t}$ | $-a_4'(a_4' - u/2)$ |
| $R^{x_4x_0}{}_{x_4x_0}$ and $R^{x_4x_t}{}_{x_4x_t}$ | $-a_4'' + v/2 + (a_4' - u/2)^2$ |
| $R^{x_0x_t}{}_{x_0x_t}$ and $R^{x_tx_{t'}}{}_{x_tx_{t'}}$ | $(a_4' - u/2)^2 - H^2k$ |

Every $R^{ab}{}_{cd}$ is free of $x_0$: of $(\sin^2z)^{1/12}$, $\cot z$ and $\mathrm{sgn}(\cot z)$ (`mixed_riemann_free_of_x0`). The hidden direction and the extra times form one block of the scale factor $e^{-a_4}b_4^{1/2}$: the planes inside the block have the curvature $(a_4' - u/2)^2 - H^2k$ (a space of constant curvature $-H^2$ times the block factor, plus the expansion term), and each plane of the block with $x_4$ or with 3-space has the curvature of the corresponding extra-time plane.

The mixed Ricci tensor is diagonal: $R^{x_i}{}_{x_i} = a_4'' - (a_4')^2 + 2a_4'u$, $R^{x_4}{}_{x_4} = 7(a_4')^2 - 4a_4'u - a_4'' + u^2 + 2v$, $R^{x_0}{}_{x_0} = R^{x_t}{}_{x_t} = (a_4')^2 - \frac52a_4'u - a_4'' - 3H^2k + u^2 + \frac12v$; the Ricci scalar is $R = 8(a_4')^2 - 8a_4'u - 2a_4'' - 12H^2k + 5u^2 + 4v$ (`ricciScalar`), and the Einstein tensor is

$$
\begin{aligned}
&G^{x_i}{}_{x_i} = 2a_4'' - 5(a_4')^2 + 6a_4'u + 6H^2k - \tfrac52u^2 - 2v,\quad G^{x_4}{}_{x_4} = 3(a_4')^2 + 6H^2k - \tfrac32u^2,\\
&G^{x_0}{}_{x_0} = G^{x_t}{}_{x_t} = -3(a_4')^2 + \tfrac32a_4'u + 3H^2k - \tfrac32u^2 - \tfrac32v .
\end{aligned}
$$

### 6.2 The Lovelock scalars

From `lovelock-tensors.json` (keys `L1`, `L2`, `L3`), with $b_4''/b_4 = v + u^2$ and $e^{2a_4}/b_4 = k$:

$$
\begin{aligned}
L_{(1)} &= 16\,(a_4')^{2} - 16\,a_4'\,u - 4\,a_4'' \\
&\quad + 10\,u^{2} + 8\,v - 24\,k\,H^{2} , \\
L_{(2)} &= -192\,(a_4')^{4} + 384\,(a_4')^{3}\,u + 288\,(a_4')^{2}\,a_4'' \\
&\quad - 336\,(a_4')^{2}\,u^{2} - 192\,(a_4')^{2}\,v - 576\,(a_4')^{2}\,k\,H^{2} \\
&\quad - 384\,a_4'\,a_4''\,u + 48\,a_4'\,u^{3} + 96\,a_4'\,u\,v \\
&\quad + 48\,a_4''\,u^{2} - 192\,a_4''\,k\,H^{2} + 30\,u^{4} \\
&\quad + 48\,u^{2}\,v - 144\,u^{2}\,k\,H^{2} - 192\,v\,k\,H^{2} \\
&\quad + 96\,k^{2}\,H^{4} , \\
L_{(3)} &= 4608\,(a_4')^{6} - 13824\,(a_4')^{5}\,u - 17280\,(a_4')^{4}\,a_4'' \\
&\quad + 15552\,(a_4')^{4}\,u^{2} + 6912\,(a_4')^{4}\,v + 6912\,(a_4')^{4}\,k\,H^{2} \\
&\quad + 27648\,(a_4')^{3}\,a_4''\,u - 5760\,(a_4')^{3}\,u^{3} - 6912\,(a_4')^{3}\,u\,v \\
&\quad - 10368\,(a_4')^{2}\,a_4''\,u^{2} + 13824\,(a_4')^{2}\,a_4''\,k\,H^{2} - 432\,(a_4')^{2}\,u^{4} \\
&\quad + 6912\,(a_4')^{2}\,k^{2}\,H^{4} + 432\,a_4'\,u^{5} + 864\,a_4'\,u^{3}\,v \\
&\quad - 1728\,a_4'\,u^{3}\,k\,H^{2} - 3456\,a_4'\,u\,v\,k\,H^{2} + 216\,a_4''\,u^{4} \\
&\quad - 1728\,a_4''\,u^{2}\,k\,H^{2} + 3456\,a_4''\,k^{2}\,H^{4} .
\end{aligned}
$$

### 6.3 The Lovelock tensors

Every $P_{(k)}{}^h{}_j$ is diagonal: the 8 diagonal components are nonzero and the other 56 off-diagonal components vanish (`k1_offdiagonal_vanishes`, `k2_offdiagonal_vanishes`, `k3_offdiagonal_vanishes`). The diagonal satisfies $x_1 = x_2 = x_3$ and $x_0 = x_5 = x_6 = x_7$ (`k1_hidden_equals_extra_times`, `k2_hidden_equals_extra_times`, `k3_hidden_equals_extra_times`), so three components per order are independent; the hidden direction and the extra times are listed both. The formulas below are the LaTeX texts of `lovelock-tensors.json`, unchanged (only broken into lines at top-level signs; $e^{2a_4}b_4^{-1} = k$).

$k = 1$:

$$
\begin{aligned}
P_{(1)}{}^{x_0}{}_{x_0} &= 6\,b_4^{-1}\,b_4'' - 6\,a_4'\,b_4^{-1}\,b_4' + 12\,(a_4')^{2} \\
&\quad - 12\,H^{2}\,e^{2 a_4}\,b_4^{-1}
\end{aligned}
$$

$$
\begin{aligned}
P_{(1)}{}^{x_1}{}_{x_1} &= 2\,b_4^{-2}\,(b_4')^{2} + 8\,b_4^{-1}\,b_4'' - 8\,a_4'' \\
&\quad - 24\,a_4'\,b_4^{-1}\,b_4' + 20\,(a_4')^{2} - 24\,H^{2}\,e^{2 a_4}\,b_4^{-1}
\end{aligned}
$$

$$
\begin{aligned}
P_{(1)}{}^{x_4}{}_{x_4} &= 6\,b_4^{-2}\,(b_4')^{2} - 12\,(a_4')^{2} - 24\,H^{2}\,e^{2 a_4}\,b_4^{-1}
\end{aligned}
$$

$$
\begin{aligned}
P_{(1)}{}^{x_5}{}_{x_5} &= 6\,b_4^{-1}\,b_4'' - 6\,a_4'\,b_4^{-1}\,b_4' + 12\,(a_4')^{2} \\
&\quad - 12\,H^{2}\,e^{2 a_4}\,b_4^{-1}
\end{aligned}
$$

$k = 2$:

$$
\begin{aligned}
P_{(2)}{}^{x_0}{}_{x_0} &= -6\,b_4^{-4}\,(b_4')^{4} + 12\,b_4^{-3}\,(b_4')^{2}\,b_4'' \\
&\quad + 48\,a_4''\,b_4^{-2}\,(b_4')^{2} - 36\,a_4'\,b_4^{-3}\,(b_4')^{3} \\
&\quad + 96\,a_4'\,b_4^{-2}\,b_4'\,b_4'' - 192\,a_4'\,a_4''\,b_4^{-1}\,b_4' \\
&\quad - 48\,(a_4')^{2}\,b_4^{-2}\,(b_4')^{2} - 96\,(a_4')^{2}\,b_4^{-1}\,b_4'' \\
&\quad + 96\,(a_4')^{3}\,b_4^{-1}\,b_4' - 96\,(a_4')^{4} \\
&\quad + 24\,H^{2}\,e^{2 a_4}\,b_4^{-3}\,(b_4')^{2} \\
&\quad - 48\,H^{2}\,e^{2 a_4}\,b_4^{-2}\,b_4'' \\
&\quad - 192\,H^{2}\,a_4''\,e^{2 a_4}\,b_4^{-1} \\
&\quad - 48\,H^{2}\,a_4'\,e^{2 a_4}\,b_4^{-2}\,b_4' \\
&\quad - 384\,H^{2}\,(a_4')^{2}\,e^{2 a_4}\,b_4^{-1}
\end{aligned}
$$

$$
\begin{aligned}
P_{(2)}{}^{x_1}{}_{x_1} &= -18\,b_4^{-4}\,(b_4')^{4} + 48\,b_4^{-3}\,(b_4')^{2}\,b_4'' \\
&\quad - 48\,a_4'\,b_4^{-3}\,(b_4')^{3} - 256\,a_4'\,a_4''\,b_4^{-1}\,b_4' \\
&\quad - 32\,(a_4')^{2}\,b_4^{-2}\,(b_4')^{2} - 128\,(a_4')^{2}\,b_4^{-1}\,b_4'' \\
&\quad + 384\,(a_4')^{2}\,a_4'' + 384\,(a_4')^{3}\,b_4^{-1}\,b_4' - 224\,(a_4')^{4} \\
&\quad + 48\,H^{2}\,e^{2 a_4}\,b_4^{-3}\,(b_4')^{2} \\
&\quad - 192\,H^{2}\,e^{2 a_4}\,b_4^{-2}\,b_4'' \\
&\quad + 192\,H^{2}\,a_4'\,e^{2 a_4}\,b_4^{-2}\,b_4' \\
&\quad - 384\,H^{2}\,(a_4')^{2}\,e^{2 a_4}\,b_4^{-1} + 96\,H^{4}\,e^{4 a_4}\,b_4^{-2}
\end{aligned}
$$

$$
\begin{aligned}
P_{(2)}{}^{x_4}{}_{x_4} &= 6\,b_4^{-4}\,(b_4')^{4} + 96\,a_4'\,b_4^{-3}\,(b_4')^{3} \\
&\quad - 288\,(a_4')^{2}\,b_4^{-2}\,(b_4')^{2} + 288\,(a_4')^{4} \\
&\quad - 48\,H^{2}\,e^{2 a_4}\,b_4^{-3}\,(b_4')^{2} \\
&\quad - 384\,H^{2}\,a_4'\,e^{2 a_4}\,b_4^{-2}\,b_4' \\
&\quad + 384\,H^{2}\,(a_4')^{2}\,e^{2 a_4}\,b_4^{-1} + 96\,H^{4}\,e^{4 a_4}\,b_4^{-2}
\end{aligned}
$$

$$
\begin{aligned}
P_{(2)}{}^{x_5}{}_{x_5} &= -6\,b_4^{-4}\,(b_4')^{4} + 12\,b_4^{-3}\,(b_4')^{2}\,b_4'' \\
&\quad + 48\,a_4''\,b_4^{-2}\,(b_4')^{2} - 36\,a_4'\,b_4^{-3}\,(b_4')^{3} \\
&\quad + 96\,a_4'\,b_4^{-2}\,b_4'\,b_4'' - 192\,a_4'\,a_4''\,b_4^{-1}\,b_4' \\
&\quad - 48\,(a_4')^{2}\,b_4^{-2}\,(b_4')^{2} - 96\,(a_4')^{2}\,b_4^{-1}\,b_4'' \\
&\quad + 96\,(a_4')^{3}\,b_4^{-1}\,b_4' - 96\,(a_4')^{4} \\
&\quad + 24\,H^{2}\,e^{2 a_4}\,b_4^{-3}\,(b_4')^{2} \\
&\quad - 48\,H^{2}\,e^{2 a_4}\,b_4^{-2}\,b_4'' \\
&\quad - 192\,H^{2}\,a_4''\,e^{2 a_4}\,b_4^{-1} \\
&\quad - 48\,H^{2}\,a_4'\,e^{2 a_4}\,b_4^{-2}\,b_4' \\
&\quad - 384\,H^{2}\,(a_4')^{2}\,e^{2 a_4}\,b_4^{-1}
\end{aligned}
$$

$k = 3$:

$$
\begin{aligned}
P_{(3)}{}^{x_0}{}_{x_0} &= 864\,a_4'\,a_4''\,b_4^{-3}\,(b_4')^{3} - 648\,(a_4')^{2}\,b_4^{-4}\,(b_4')^{4} \\
&\quad + 1296\,(a_4')^{2}\,b_4^{-3}\,(b_4')^{2}\,b_4'' \\
&\quad - 5184\,(a_4')^{2}\,a_4''\,b_4^{-2}\,(b_4')^{2} \\
&\quad + 720\,(a_4')^{3}\,b_4^{-3}\,(b_4')^{3} \\
&\quad - 3456\,(a_4')^{3}\,b_4^{-2}\,b_4'\,b_4'' \\
&\quad + 6912\,(a_4')^{3}\,a_4''\,b_4^{-1}\,b_4' \\
&\quad + 1728\,(a_4')^{4}\,b_4^{-2}\,(b_4')^{2} + 1728\,(a_4')^{4}\,b_4^{-1}\,b_4'' \\
&\quad - 1728\,(a_4')^{5}\,b_4^{-1}\,b_4' + 1152\,(a_4')^{6} \\
&\quad - 3456\,H^{2}\,a_4'\,a_4''\,e^{2 a_4}\,b_4^{-2}\,b_4' \\
&\quad + 864\,H^{2}\,(a_4')^{2}\,e^{2 a_4}\,b_4^{-3}\,(b_4')^{2} \\
&\quad - 1728\,H^{2}\,(a_4')^{2}\,e^{2 a_4}\,b_4^{-2}\,b_4'' \\
&\quad + 6912\,H^{2}\,(a_4')^{2}\,a_4''\,e^{2 a_4}\,b_4^{-1} \\
&\quad - 1728\,H^{2}\,(a_4')^{3}\,e^{2 a_4}\,b_4^{-2}\,b_4' \\
&\quad + 3456\,H^{2}\,(a_4')^{4}\,e^{2 a_4}\,b_4^{-1}
\end{aligned}
$$

$$
\begin{aligned}
P_{(3)}{}^{x_1}{}_{x_1} &= 144\,a_4''\,b_4^{-4}\,(b_4')^{4} - 288\,a_4'\,b_4^{-5}\,(b_4')^{5} \\
&\quad + 576\,a_4'\,b_4^{-4}\,(b_4')^{3}\,b_4'' \\
&\quad - 1152\,a_4'\,a_4''\,b_4^{-3}\,(b_4')^{3} \\
&\quad + 216\,(a_4')^{2}\,b_4^{-4}\,(b_4')^{4} \\
&\quad - 1728\,(a_4')^{2}\,b_4^{-3}\,(b_4')^{2}\,b_4'' \\
&\quad + 1728\,(a_4')^{3}\,b_4^{-3}\,(b_4')^{3} \\
&\quad + 9216\,(a_4')^{3}\,a_4''\,b_4^{-1}\,b_4' \\
&\quad + 576\,(a_4')^{4}\,b_4^{-2}\,(b_4')^{2} + 2304\,(a_4')^{4}\,b_4^{-1}\,b_4'' \\
&\quad - 11520\,(a_4')^{4}\,a_4'' - 6912\,(a_4')^{5}\,b_4^{-1}\,b_4' \\
&\quad + 3456\,(a_4')^{6} - 1152\,H^{2}\,a_4''\,e^{2 a_4}\,b_4^{-3}\,(b_4')^{2} \\
&\quad + 1152\,H^{2}\,a_4'\,e^{2 a_4}\,b_4^{-4}\,(b_4')^{3} \\
&\quad - 2304\,H^{2}\,a_4'\,e^{2 a_4}\,b_4^{-3}\,b_4'\,b_4'' \\
&\quad + 4608\,H^{2}\,a_4'\,a_4''\,e^{2 a_4}\,b_4^{-2}\,b_4' \\
&\quad + 576\,H^{2}\,(a_4')^{2}\,e^{2 a_4}\,b_4^{-3}\,(b_4')^{2} \\
&\quad + 2304\,H^{2}\,(a_4')^{2}\,e^{2 a_4}\,b_4^{-2}\,b_4'' \\
&\quad - 2304\,H^{2}\,(a_4')^{3}\,e^{2 a_4}\,b_4^{-2}\,b_4' \\
&\quad + 2304\,H^{2}\,(a_4')^{4}\,e^{2 a_4}\,b_4^{-1} \\
&\quad + 2304\,H^{4}\,a_4''\,e^{4 a_4}\,b_4^{-2} \\
&\quad + 3456\,H^{4}\,(a_4')^{2}\,e^{4 a_4}\,b_4^{-2}
\end{aligned}
$$

$$
\begin{aligned}
P_{(3)}{}^{x_4}{}_{x_4} &= 1080\,(a_4')^{2}\,b_4^{-4}\,(b_4')^{4} \\
&\quad - 5760\,(a_4')^{3}\,b_4^{-3}\,(b_4')^{3} \\
&\quad + 8640\,(a_4')^{4}\,b_4^{-2}\,(b_4')^{2} - 5760\,(a_4')^{6} \\
&\quad - 5184\,H^{2}\,(a_4')^{2}\,e^{2 a_4}\,b_4^{-3}\,(b_4')^{2} \\
&\quad + 13824\,H^{2}\,(a_4')^{3}\,e^{2 a_4}\,b_4^{-2}\,b_4' \\
&\quad - 6912\,H^{2}\,(a_4')^{4}\,e^{2 a_4}\,b_4^{-1} \\
&\quad + 3456\,H^{4}\,(a_4')^{2}\,e^{4 a_4}\,b_4^{-2}
\end{aligned}
$$

$$
\begin{aligned}
P_{(3)}{}^{x_5}{}_{x_5} &= 864\,a_4'\,a_4''\,b_4^{-3}\,(b_4')^{3} - 648\,(a_4')^{2}\,b_4^{-4}\,(b_4')^{4} \\
&\quad + 1296\,(a_4')^{2}\,b_4^{-3}\,(b_4')^{2}\,b_4'' \\
&\quad - 5184\,(a_4')^{2}\,a_4''\,b_4^{-2}\,(b_4')^{2} \\
&\quad + 720\,(a_4')^{3}\,b_4^{-3}\,(b_4')^{3} \\
&\quad - 3456\,(a_4')^{3}\,b_4^{-2}\,b_4'\,b_4'' \\
&\quad + 6912\,(a_4')^{3}\,a_4''\,b_4^{-1}\,b_4' \\
&\quad + 1728\,(a_4')^{4}\,b_4^{-2}\,(b_4')^{2} + 1728\,(a_4')^{4}\,b_4^{-1}\,b_4'' \\
&\quad - 1728\,(a_4')^{5}\,b_4^{-1}\,b_4' + 1152\,(a_4')^{6} \\
&\quad - 3456\,H^{2}\,a_4'\,a_4''\,e^{2 a_4}\,b_4^{-2}\,b_4' \\
&\quad + 864\,H^{2}\,(a_4')^{2}\,e^{2 a_4}\,b_4^{-3}\,(b_4')^{2} \\
&\quad - 1728\,H^{2}\,(a_4')^{2}\,e^{2 a_4}\,b_4^{-2}\,b_4'' \\
&\quad + 6912\,H^{2}\,(a_4')^{2}\,a_4''\,e^{2 a_4}\,b_4^{-1} \\
&\quad - 1728\,H^{2}\,(a_4')^{3}\,e^{2 a_4}\,b_4^{-2}\,b_4' \\
&\quad + 3456\,H^{2}\,(a_4')^{4}\,e^{2 a_4}\,b_4^{-1}
\end{aligned}
$$

Remarks, each an exact property of the listed components:

- $P_{(1)} = -4G$ component by component (compare section 6.1).
- Of the metric functions only derivatives and $k$ occur: $a_4'$ and $a_4''$, not $a_4$ itself except through $k = e^{2a_4}/b_4$, and $b_4$ only through $u = b_4'/b_4$, $v = u'$ and $k$ (record `lovelock_variables` of `Revision/field_equations_a4`). The $x_4$ components contain no $a_4''$.
- $P_{(k)}^{x_1}{}_{x_1} - P_{(k)}^{x_0}{}_{x_0}$ is nonzero for $k = 1, 2, 3$, also at constant $b_4$: 3-space and the block differ (section 9).
- The contravariant densities are $A_{(k)}{}^{ll} = \sqrt{|g|}\;g^{ll}\,P_{(k)}{}^l{}_l$ for every $l$. All 64 components of each $A_{(k)}$, each with its exact monomial list, are in `lovelock-tensors.json`; all 384 components of $P_{(k)}$ and $A_{(k)}$ are also written out in `lovelock-components.md`.

Here $\sqrt{|g|} = e^{-a_4}b_4^2|\cot z|(\sin^2z)^{1/4}$ and the inverse metric is

$$
g^{x_0x_0} = e^{2a_4}b_4^{-1}\tan^2z,\quad g^{x_ix_i} = e^{-2a_4},\quad g^{x_4x_4} = -1,\quad g^{x_tx_t} = -e^{2a_4}b_4^{-1}(\sin^2z)^{-1/6} .
$$

For example, the file gives

$$
\begin{aligned}
A_{(1)}{}^{x_4x_4} &= -6\,e^{-1 a_4}\,(\sin^2(6Hx_0))^{1/4}\,\cot(6Hx_0)\,\operatorname{sgn}(\cot(6Hx_0))\,(b_4')^{2} \\
&\quad + 12\,(a_4')^{2}\,e^{-1 a_4}\,(\sin^2(6Hx_0))^{1/4}\,\cot(6Hx_0)\,\operatorname{sgn}(\cot(6Hx_0))\,b_4^{2} \\
&\quad + 24\,H^{2}\,e^{1 a_4}\,(\sin^2(6Hx_0))^{1/4}\,\cot(6Hx_0)\,\operatorname{sgn}(\cot(6Hx_0))\,b_4
\end{aligned}
$$

### 6.4 The checks of the Rust program

`lovelock_gkd lovelock --brute-force-k2` writes `curvature.json`, `lovelock-tensors.json`, `lovelock-components.md` and `lovelock-report.json`. The report gives `"checkCount": 27`, `"failedCheckCount": 0` and `"verdict": "SUCCESS"`; every one of its 27 checks has `"passed": true`:

| check | check | check |
| --- | --- | --- |
| `riemann_antisymmetry` | `riemann_first_bianchi` | `mixed_riemann_free_of_x0` |
| `mixed_riemann_only_sectional` | `sqrt_det_g_positive_every_quarter` | `k1_equals_minus_4_einstein` |
| `k1_trace_identity` | `k1_divergence_free` | `k1_symmetric` |
| `k1_free_of_x0` | `k1_offdiagonal_vanishes` | `k1_hidden_equals_extra_times` |
| `k2_trace_identity` | `k2_divergence_free` | `k2_symmetric` |
| `k2_free_of_x0` | `k2_offdiagonal_vanishes` | `k2_hidden_equals_extra_times` |
| `k3_trace_identity` | `k3_divergence_free` | `k3_symmetric` |
| `k3_free_of_x0` | `k3_offdiagonal_vanishes` | `k3_hidden_equals_extra_times` |
| `k4_tensor_vanishes` | `k1_brute_force_numeric` | `k2_brute_force_numeric` |

They are mathematical identities, not comparisons with the author's numbers: the antisymmetries and the first Bianchi identity of $R^{ab}{}_{cd}$ for all 4096 index lists, the independence of $x_0$ and the sectional form of $R^{ab}{}_{cd}$, the positivity of $\sqrt{|g|}$ in all four quarters of the period of $z$, $P_{(1)} = -4G$ by an independent route, the trace identities, $\nabla_hP_{(k)}{}^h{}_j = 0$ for every $j$, the symmetry of $g_{hh}P_{(k)}{}^h{}_j$ (so $A_{(k)}{}^{lh} = A_{(k)}{}^{hl}$), the independence of $x_0$, the vanishing off-diagonal components and the equality of the hidden and the extra-time components, $P_{(4)} = 0$ and the unpruned numerical sums. Two runs give byte-identical files (`Revision/gkd_lovelock/results/PROVENANCE_OF_THE_COMPUTATION.md`).

## 7. Independent verifications

### 7.1 The Wolfram check (29 checks)

`Revision/gkd_lovelock/verification/verify_lovelock_gkd.wls` with the package `LovelockGKDCheck.wl` writes `wolfram-gkd-report.json`: `"checkCount": 29`, `"expectedCheckCount": 29`, `"failedCheckCount": 0`, `"verdict": "SUCCESS"`, producer Wolfram Language 15.0.1. What it does:

- The author's definition, re-typed verbatim, is the kernel's definition of `kδ` (compared with the text recorded in `PROVENANCE_OF_THE_COMPUTATION.md`), with `delta[a_Integer, b_Integer] := KroneckerDelta[a, b]`; unequal lengths stay unevaluated.
- GKD is NOT re-implemented in Wolfram Language: a small exporter compiled with cargo against the unchanged crate writes the values of the Rust function GKD for 346304 pairs (all 64, 4096 and 262144 pairs of lengths 1, 2, 3 and 20000 pseudo-random pairs of each length 4 to 7; values file of 3161984 bytes), and the verbatim `kδ` is evaluated on every pair: 0 mismatches. The negative control against $-$GKD reports a mismatch at exactly every pair where GKD is nonzero (8, 112, 2016, 10022, 10005, 10002, 10000 pairs for lengths 1 to 7).
- The curvature is recomputed from the metric with `D` and `Inverse`, brought to an exact normal form for every real $z$ (112 nonzero $R^{ab}{}_{cd}$, all free of $x_0$, the same as `curvature.json`), and $\sqrt{|\det g|}$ is the product of the roots of the $|g_{aa}|$, checked exactly and at one point in each quarter of the period of $z$.
- The Lovelock tensors are recomputed with the verbatim `kδ`: for $k = 1$ and $k = 2$ every $k$-tuple of the 112 nonzero entries for each of the 64 components (7168 and 802816 calls), for $k = 3$ every list left after skipping lists with a repeated label in a row (645120 calls). The exact zero test of the difference with the Rust tensors is 0 for all 64 components of each $P_{(k)}$ and $A_{(k)}$. The numbers of nonzero `kδ` terms, 672, 26880 and 322560, equal the Rust counters. A tampered $P_{(2)}$ component and a tampered $A_{(3)}$ component are flagged, and only those.

| check | check |
| --- | --- |
| `definition_is_the_authors_verbatim` | `definition_unequal_lengths_stay_unevaluated` |
| `gkd_values_file_layout` | `gkd_equals_kdelta_exhaustive_length_1` |
| `gkd_equals_kdelta_exhaustive_length_2` | `gkd_equals_kdelta_exhaustive_length_3` |
| `gkd_equals_kdelta_random_length_4` | `gkd_equals_kdelta_random_length_5` |
| `gkd_equals_kdelta_random_length_6` | `gkd_equals_kdelta_random_length_7` |
| `negative_control_gkd_comparison_detects_a_sign_flip` | `riemann_mixed_equals_rust_curvature` |
| `sqrt_det_g` | `lovelock_kdelta_values_are_integers` |
| `k1_P_equals_rust_all_64_components` | `k1_A_equals_rust_all_64_components` |
| `k2_P_equals_rust_all_64_components` | `k2_A_equals_rust_all_64_components` |
| `k3_P_equals_rust_all_64_components` | `k3_A_equals_rust_all_64_components` |
| `negative_control_tensor_comparison_detects_a_change` | `k1_equals_minus_4_einstein` |
| `k1_trace_equals_6_L1` | `k2_trace_equals_4_L2` |
| `k3_trace_equals_2_L3` | `k1_nonzero_kdelta_terms_equal_rust_counter` |
| `k2_nonzero_kdelta_terms_equal_rust_counter` | `k3_nonzero_kdelta_terms_equal_rust_counter` |
| `rust_json_text_equals_its_monomials` | |

Scope. The Wolfram check is independent of the Rust code in its definition of $\delta$ (the author's verbatim text), its curvature and its Lovelock sums; it uses the Rust program for the GKD values it compares and for the tensors it compares with. Its default run skips, for $k = 3$, lists with a repeated label in a row (their determinant is 0 because two rows or columns are equal). Only Wolfram 15.0.1 was used.

### 7.2 The sympy checker (56 checks)

The sympy checker is the file `check_lovelock_gkd.py` in the folder `Revision/gkd_lovelock/verification/`. Its report `python-lovelock-report.json` gives `"checkCount": 56`, `"failedCheckCount": 0` and `"verdict": "SUCCESS"`. It shares no code with the Rust crate: the geometry is sympy's own differentiation, $\delta$ is the author's definition evaluated with sympy's determinant (memoised by the 0/1 matrix), and the sums are organised breadth-first (all $k$-fold products with pairwise different lower and pairwise different upper indices, then completed by every admissible $h$ and $j$, one literal call of the determinant per term). Its counters:

| $k$ | products | determinant calls | nonzero values | distinct multisets |
| --- | --- | --- | --- | --- |
| 1 | 112 | 4144 | 784 | 112 |
| 2 | 6720 | 114240 | 33600 | 3360 |
| 3 | 161280 | 806400 | 483840 | 26880 |

with 2647169 determinant calls in all and 15016 distinct 0/1 matrices determined by sympy. The skipped terms are checked as well: the completely unpruned literal sums for $k = 1$ (7280 calls) and $k = 2$ (815360 calls) agree exactly with the pruned sums; 20000 random terms of the unpruned $k = 3$ sum, 19876 of them with a repeated index, give 0 whenever skipped; 300 random 9-index lists give 0. The comparison with the Rust output is exact three times over: by an exact canonical form (`canon`, a symbol form with $w = |\sin z|^{1/6}$, the signs of $\sin z$ and $\cot z$ and the ring of $H$, $a_4'$, $a_4''$, $b_4'/b_4$, $b_4''/b_4$ and $e^{2a_4}/b_4$, so a zero difference is a proof of equality), by plain sympy simplification, and numerically with 60 digits at 5 random rational points (one in each quarter of the period of $z$ and one at $z < 0$).

| check | check | check |
| --- | --- | --- |
| `gkd_literal_equals_cofactor_expansion` | `gkd_examples` | `gkd_nine_indices_in_eight_dimensions_vanish` |
| `normalisation_P1_derived_minus_4` | `normalisation_P2_derived_minus_8` | `normalisation_L3_cubic_derived` |
| `metric_inverse` | `sqrt_abs_det_g` | `christoffel_symmetric` |
| `riemann_first_bianchi` | `mixed_riemann_free_of_x0` | `mixed_riemann_only_sectional` |
| `riemann_antisymmetry_and_pair_symmetry` | `k1_unpruned_literal_sum_agrees` | `k2_unpruned_literal_sum_agrees` |
| `k3_pruned_terms_vanish_literally` | `k4_terms_vanish_literally` | `k1_equals_minus_4_einstein` |
| `L1_equals_2R` | `k2_equals_minus_8_gauss_bonnet` | `L2_equals_4_gauss_bonnet` |
| `gauss_bonnet_index_placement` | `L3_equals_8_cubic_lovelock_density` | `k1_trace_identity` |
| `k2_trace_identity` | `k3_trace_identity` | `k1_divergence_free` |
| `k1_symmetric` | `k1_free_of_x0` | `k1_offdiagonal_vanishes` |
| `k1_hidden_equals_extra_times` | `k2_divergence_free` | `k2_symmetric` |
| `k2_free_of_x0` | `k2_offdiagonal_vanishes` | `k2_hidden_equals_extra_times` |
| `k3_divergence_free` | `k3_symmetric` | `k3_free_of_x0` |
| `k3_offdiagonal_vanishes` | `k3_hidden_equals_extra_times` | `rust_k1_mixed_components_agree` |
| `rust_k1_contravariant_components_agree` | `rust_L1_agrees` | `rust_k2_mixed_components_agree` |
| `rust_k2_contravariant_components_agree` | `rust_L2_agrees` | `rust_k3_mixed_components_agree` |
| `rust_k3_contravariant_components_agree` | `rust_L3_agrees` | `negative_controls_detected` |
| `rust_metric_and_sqrt_g_agree` | `rust_christoffels_agree` | `rust_riemann_agrees` |
| `rust_ricci_einstein_scalar_agree` | `rust_text_matches_monomials` | |

Scope. The sympy checker reads only the metric (typed in from the task text) and, for the comparison, `curvature.json` and `lovelock-tensors.json`; it never reads the author's notebook. Its literal $\delta$ is compared with an independent cofactor expansion on all 266304 pairs of lengths 1 to 3 and 7500 random pairs of lengths 4 to 8. The negative controls (a coefficient increased by 1, a wrong power of $W$, a wrong power of $e^{a_4}$, an added $10^{-30}H^4$) are each detected by each of its three comparison methods.

## 8. The comparison with the author's notebooks

### 8.1 What was read for the computation

What was read is recorded in `PROVENANCE_OF_THE_COMPUTATION.md`, written before any comparison, and in the provenance file `WOLFRAMSCRIPT_PROVENANCE.md` of the folder `Revision/gkd_lovelock/notebook_reading/`: only the 58 INPUT cells of `Generalized _Kronecker_Delta_4+4.nb` (sha256 `23bb4e0c70943e766d9b081a3a399ef29664889aad088041329ce2e065b80afb`), converted to text without evaluation; the committed digest `notebook-input-cells.txt` gives, for each, its label, its length and its first 160 characters. The definition of `kδ` was taken from the cell `In[87]` and Lovelock's equation from the picture in the cell `In[101]` (1372 x 435 pixels). For the computation no output cell, no file `Generalized_Kronecker_Delta.txt` and no other Mathematica file of the author was opened; the metric was taken from the author's message and, since 2026-10-16, from `Revision/SPEC.md` section 1.

What the notebook computes, as far as its input cells show (a reading of the digest, labelled as such): it sets up the xAct packages, an 8-dimensional manifold and a metric of signature (4,4) (`In[29]`); it builds the generalized delta in a second way, as contracted products of two Levi-Civita tensors divided by $(8 - p)!$ (`delta11`, `delta22`, `delta33`, `delta55`); it defines `kδ` (`In[87]`) and evaluates it for 3, 5 and 7 index pairs (`kδ33`, `kδ55`, `kδ77`); it compares the two constructions (`In[102]`, `In[105]`, `In[108]`); and it contains the picture of (4.38). Its answers are in its output cells, which were not read for the computation; section 8.2 compares no output of this notebook either.

The checks against the author's definitions, made with the computation:

- The definition: `definition_is_the_authors_verbatim` shows that the definition evaluated by the Wolfram check is the author's text, character for character.
- The function: GKD equals the author's `kδ` on every pair of lists of length 1 to 3, on 20000 random pairs of each length 4 to 7 (Wolfram), and equals the literal determinant on every pair of length 1 to 4 and 200000 random pairs of each length 5 to 9 (Rust self-test), as the theorem of section 3.2 requires.
- The equation: the tensors are those of (4.38) as shown in the notebook's picture, with the conventions of section 4.2.

### 8.2 The comparison with the author's stored outputs (2026-10-08)

`PROVENANCE_OF_THE_COMPUTATION.md` announces that the comparison with the author's own answers is done afterwards, in a separate, later commit; that comparison is recorded in `Revision/gkd_lovelock/comparison/`: its `README.md`, the read-only extractor `extract_author_curvature_outputs.wls` with its output `author-curvature-outputs.json`, and the program `compare_with_author.py` with its report `author-comparison-report.json`. Its files were first committed on 2026-10-08, after the results of this record (commit 3e81eeb, 2026-10-01). By its README it changes no file of `Revision/gkd_lovelock/results/`, `Revision/gkd_lovelock/code/`, `Revision/gkd_lovelock/verification/` or `Revision/gkd_lovelock/notebook_reading/`.

This notebook of the author computes the metric of 2026-10-14 without $b_4$ (its `MatrixMetric44` has $b_4 = 1$, with $\cot^2z$ in $g_{00}$ and $\sin^{1/3}z$ on 3-space). Since 2026-10-16 the comparison therefore uses the frozen record of that metric, `Revision/gkd_lovelock/reference_2026_10_14/` (the Rust files of commit c93fe22, pinned by sha256: `reference-files-are-the-record-of-2026-10-14`), evaluated at $b_4 = 1$, the only place where this document restricts $b_4$. The corrected metric of section 2.1 is compared with `Revision/SPEC.md` section 1 (`revision-metric-spec-vs-curvature-json`), and a further check shows that it is not the metric of the notebook (`corrected-metric-differs-from-the-author-notebook-metric`): $g_{00}$ and $g_{x_1x_1}, g_{x_2x_2}, g_{x_3x_3}$ differ, $g_{x_4x_4}$ agrees, and $g_{x_5x_5}, g_{x_6x_6}, g_{x_7x_7}$ agree only where $\sin z > 0$ and are listed as differing because no sign of $\sin z$ is assumed. For the corrected metric no stored output of the author exists, so it is not compared with one.

What was read. The author's notebook `Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb` in the repository root (sha256 `5ee5cb2a95146136ee65636a4aef174f303b6c41da130d2c57e4684f9c8ff69f`), read only: `Get` of the file gives the inert notebook expression, and the stored output boxes are converted with `ToExpression[boxes, StandardForm, HoldComplete]`, so nothing is evaluated and no input cell is run. Of its 2127 cells (996 Input, 805 Output) the comparison uses these:

| cell | what it is |
| --- | --- |
| `In[79]`, `In[82]` | the definition of the author's metric `MatrixMetric44`, in which `a4` is a function of the argument $Hx_4$ |
| `In[214]` | the definition of `rt[g]`: inverse metric, Christoffel symbols, Riemann tensor, Ricci tensor, Ricci scalar and Einstein tensor |
| `Out[235]` | `gtry = MatrixMetric44`, the stored 8 x 8 metric |
| `In[238]` | `rt[gtry]`, which assigns `RS` and `EinsteinG`; its output is suppressed |
| `Out[245]` | `MatrixMetric44` printed again (a control: identical to `Out[235]`) |
| `Out[535]` | the stored Ricci scalar `RS` |
| `Out[536]` | the stored Einstein tensor `EinsteinG`, both indices down (8 x 8) |

That `Out[535]` and `Out[536]` are the values returned by `rt[gtry]` at `In[238]` is an inference from the file, labelled as such: among all input cells only `In[238]` assigns the global symbols `RS` and `EinsteinG`. The notebook was not re-run; its outputs are taken as stored.

The mapping (a definition stated before the comparison, not a fit). The author's array position 1 is the hidden direction `x0`, with $g_{00} = \cot^2(6Hx_0)$, and positions 2 to 8 are `x1` to `x7`. This record uses the same coordinates in the same order, so the coordinate map is the identity and no component is permuted. (Until 2026-10-14 the record named the hidden direction $x_8$ and listed it last; the author's `x0` was then mapped to $x_8$, with the same checks and verdicts.) The author's `a4` is a function of the argument $Hx_4$, this record's of $x_4$: $a_4(x_4) := a_4^{\mathrm{author}}(Hx_4)$, so by the chain rule $(a_4^{\mathrm{author}})^{(n)}(Hx_4) = H^{-n}a_4^{(n)}(x_4)$ for $n = 0, 1, 2$; the program checks that no other argument of `a4` occurs in the author's outputs. $H$ is the same constant on both sides. The mapping is checked on the metric first; only then are the curvature outputs compared.

The conventions and normalisations (each stated and applied, none fitted). The author's `rt[g]` uses the Christoffel symbols, the Riemann tensor and the Ricci tensor of section 2.2, and $G = \mathrm{Ric} - \frac12 g\,R$ with both indices down. The Ricci scalar is compared with no factor. The author's Einstein tensor is raised with the author's own (mapped) inverse metric, $G^\mu{}_\nu = g^{\mu s}G_{s\nu}$, with no other factor. For $k = 1$, section 4.3 gives $P_{(1)} = -4G$ and $L_{(1)} = 2R$, so `P1_mixed_up_h_down_j` of the frozen record is compared with $-4$ times the author's $G^\mu{}_\nu$ and its `L1` with 2 times the author's Ricci scalar.

The result. A check is PASS only when the difference, reduced exactly with sympy, is 0; NOT-AVAILABLE means that the author's files hold nothing to compare with (it is not a failure):

| check | what is compared | verdict |
| --- | --- | --- |
| `author-json-matches-notebook` | the notebook read by the extractor is the notebook of the working tree (sha256) | PASS |
| `author-metric-outputs-agree` | `Out[235]` and `Out[245]` are identical | PASS |
| `reference-files-are-the-record-of-2026-10-14` | the frozen files of the metric of 2026-10-14 have their pinned sha256 | PASS |
| `revision-metric-spec-vs-curvature-json` | the corrected metric of `Revision/SPEC.md` section 1 equals `metricDiagonal` of `results/curvature.json`, 64 components | PASS |
| `metric-mapping-author-Out235-vs-revision` | the author's metric `Out[235]`, mapped, equals that of the frozen record, 64 components | PASS |
| `corrected-metric-differs-from-the-author-notebook-metric` | the corrected metric is not the notebook's metric (components listed) | PASS |
| `ricci-scalar-author-Out535-vs-curvature-json` | the author's Ricci scalar `Out[535]` equals `ricciScalar` of the frozen record | PASS |
| `einstein-mixed-<h>,<j>` | each of the 64 components of `Out[536]`, mapped and raised, equals `einsteinMixed` of the frozen record (64 checks) | PASS |
| `lovelock-P1-vs-minus4-author-EinsteinG` | `P1_mixed_up_h_down_j` of the frozen record equals $-4$ times the author's $G^\mu{}_\nu$, 64 components | PASS |
| `lovelock-L1-vs-2-author-RS` | `L1` of the frozen record equals 2 times the author's Ricci scalar | PASS |
| `control-mapping-without-chain-rule-is-detected` | the mapping without the factor $H^{-n}$ leaves a nonzero difference | PASS |
| `control-einstein-without-index-raising-is-detected` | the author's $G_{x_1x_1}$ compared without raising the index leaves a nonzero difference | PASS |
| `lovelock-k2-P2-and-L2` | $P_{(2)}$ and $L_{(2)}$ | NOT-AVAILABLE |
| `lovelock-k3-P3-and-L3` | $P_{(3)}$ and $L_{(3)}$ | NOT-AVAILABLE |
| `christoffel-components` | the Christoffel symbols | NOT-AVAILABLE |
| `riemann-components` | the Riemann tensor | NOT-AVAILABLE |
| `ricci-tensor-components` | the Ricci tensor | NOT-AVAILABLE |

In all, the report `author-comparison-report.json` has 80 checks: 75 PASS, 0 FAIL, 5 NOT-AVAILABLE. Two examples of what was compared, as the report gives them: the author's stored Ricci scalar is `6*H^2*(-7 + Derivative[1][a4][H*x4]^2)`, which the mapping turns into $6(a_4')^2 - 42H^2$, the Ricci scalar of the metric of 2026-10-14 at constant $b_4$; the author's stored $G_{x_4x_4}$ becomes $-3H^2\big(7 + (a_4')^2/H^2\big)$, and raised with $g^{x_4x_4} = -1$ it is $3(a_4')^2 + 21H^2$, the $G^{x_4}{}_{x_4}$ of that metric at constant $b_4$. The controls show that the comparison is not vacuous: without the chain-rule factor the difference of the Ricci scalars is $6(H^2 - 1)(a_4')^2$, and without the index raising the difference of the $x_1x_1$ components is nonzero; both are detected.

Why five objects are NOT-AVAILABLE. The Christoffel symbols, the Riemann tensor and the Ricci tensor are computed by `rt[gtry]`, but `In[238]` ends with a semicolon, so no value of them is stored there, and no other stored output of their values was taken. For the Lovelock tensors the box strings of every cell of the main notebook and of `Generalized _Kronecker_Delta_4+4.nb` were scanned for the word Lovelock (in any case) and for box strings equal to one of the tokens `P2`, `P3`, `P4`, `LovelockP`, `kd` and `kδ`. In the main notebook 20 cells contain the word; the 4 Output cells among them hold only strings (file names), and none of its cells contains one of the tokens. In the Kronecker-delta notebook 3 cells contain the word, none of them an Output cell, and the cells with the token `kδ` are Input and Text cells. No stored output of $P_{(2)}$, $P_{(3)}$, $L_{(2)}$ or $L_{(3)}$ was found.

Runs. The comparison was first run on 2026-10-08 (78 checks: 73 PASS, 0 FAIL, 5 NOT-AVAILABLE), re-run on 2026-10-14 for the author's coordinates (the identity mapping) and on 2026-10-16 for the corrected metric, with the frozen record of 2026-10-14 and the three new or reworded checks above: every one of the earlier checks has the same verdict and the same values, two of them with a reworded description (`Revision/gkd_lovelock/comparison/README.md`, section 1.2). Two runs on 2026-10-16 (about 1 s each) gave byte-identical reports. The report records the sha256 of `Revision/SPEC.md`, which was extended in phase W5 and again in phase W7 (the note of section 9 on the fold), so it was regenerated on 2026-10-17 after each of these two changes, each time with that one value changed; the report has the sha256 `8524627cd96ce25fb010c57a6038e2368edc4bf75d11a4448298d28ec5d627ce`. The extractor reproduced `author-curvature-outputs.json` byte for byte (its sha256 is `f041955db36f67d5ec113ad65542f448af1de6eba159c85ecff73f83761039f0`).

### 8.3 What the comparison does not establish

- Nothing about $k = 2$ and $k = 3$: the tensors $P_{(2)}$ (Gauss-Bonnet) and $P_{(3)}$ and the scalars $L_{(2)}$ and $L_{(3)}$ of the record are compared with no output of the author, because the files read contain none. Agreement with the author's own Lovelock tensors of order $k = 2$ and $k = 3$ is therefore not established.
- Nothing about the corrected metric: the author's stored outputs belong to the metric of 2026-10-14, and they are compared with the frozen record of that metric; for the corrected metric no author output exists.
- The $k = 1$ comparison carries no information beyond the Einstein-tensor comparison together with this record's own identity $P_{(1)} = -4G$ (`k1_equals_minus_4_einstein`).
- The Christoffel symbols, the Riemann tensor and the Ricci tensor are not compared: no stored output of them was taken.
- The agreement is one between two computations of the same objects for that one metric on the patch $0 < z < \pi/2$; it is not an independent check of conventions beyond those stated above.
- The author's outputs are taken as stored; the notebook was not re-run, and that the stored values come from `In[238]` is the inference stated above.
- The keyword scan finds the Lovelock tensors by name; a value stored under an unrelated name would not be found by it. Only the two notebooks of the author in the repository were read; the main notebook's text says that the Einstein-Lovelock tensors are calculated in other notebooks of the author, and none of those was read (the repository holds none of them).
- Nothing about field equations, sources, solutions or physical interpretation.

### 8.4 The metrics of 2026-10-14 and 2026-10-16

On 2026-10-14 the user changed the primordial metric: the three extra-time components gained the factor $b_4(x_4)$, $g_{x_5x_5} = g_{x_6x_6} = g_{x_7x_7} = -e^{-2a_4}b_4\sin^{1/3}z$, with $g_{00} = \cot^2z$ and $g_{x_ix_i} = e^{2a_4}\sin^{1/3}z$, on $0 < z < \pi/2$; on 2026-10-15 the user ordered that everything be moved to $b_4(x_4)$, $b_4$ never 1. For that metric each $P_{(k)}$ had 10 nonzero components, the 8 diagonal ones and $x_0$-$x_4$, $x_4$-$x_0$, proportional to $b_4'$, and a source without a $T^{x_4}{}_{x_0}$ component needed $b_4' = 0$ in Einstein gravity. On 2026-10-16 the user found that a diagonal metric needs all off-diagonal source terms to vanish, and ordered the simplest modification that is self-consistent; the corrected metric (version 2, section 2.1, `Revision/metric_warped/`, `Revision/docs/METRIC_SELF_CONSISTENCY.md`) has no mixed curvature at all, and every file of `Revision/gkd_lovelock/results/` was recomputed for it: the Rust program passes 27 of 27 checks (with the brute force of $k = 2$), the Wolfram check 29 of 29, the sympy checker 56 of 56; the monomial vectors of `lovelock-tensors.json` have 14 exponents. The results of the metric of 2026-10-14 are kept, frozen, in `Revision/gkd_lovelock/reference_2026_10_14/` for the comparison of section 8.2.

The author's notebook `Dirac_Einstein-Lovelock_4+4_Nash.nb` stores the Lovelock tensors allLovelock2 and allLovelock3 for the metric of 2026-10-14; they were compared exactly with the record of that metric in `Revision/metric_b4` (`Revision/metric_b4/METRIC_CHANGE_PROVENANCE.md`). That comparison concerns the withdrawn metric; it does not extend to the corrected one, and it does not extend what section 8.3 says is not established.

## 9. How the field equations for $a_4$ and $b_4$ use the Lovelock tensors

`Revision/field_equations_a4` writes the Einstein-Lovelock equations of `Revision/SPEC.md` section 5 for the corrected metric,

$$
\sum_{k=1}^{3}\alpha_k\,E_{(k)}{}^\mu{}_\nu + \Lambda\,\delta^\mu_\nu = \kappa\,T^\mu{}_\nu,\qquad E_{(k)} = -\frac{P_{(k)}}{2^{k+1}},\qquad E_{(1)} = G ,
$$

with $\alpha_1 = 1$ for Einstein gravity ($\alpha_2 = \alpha_3 = 0$). Both of its verifiers recompute the three tensors with their own GKD (Wolfram: as the determinant of the delta matrix; sympy: as the permutation sign) and compare all 64 components of each with the exact monomial lists of `Revision/gkd_lovelock/results/lovelock-tensors.json`, for general $b_4$:

| step | Wolfram records (`wolfram-a4-report.json`) | sympy records (`python-a4-report.json`) |
| --- | --- | --- |
| $P_{(k)}$ equal to this record | `P1_direct_equals_gkd_branch_monomials`, `P2_direct_equals_gkd_branch_monomials`, `P3_direct_equals_gkd_branch_monomials` | `P1_equals_gkd_branch_monomials`, `P2_equals_gkd_branch_monomials`, `P3_equals_gkd_branch_monomials` |
| $L_{(k)}$ equal to this record | `L1_direct_equals_gkd_branch`, `L2_direct_equals_gkd_branch`, `L3_direct_equals_gkd_branch` | `L1_equals_gkd_branch`, `L2_equals_gkd_branch`, `L3_equals_gkd_branch` |
| $P_{(1)} = -4G$, traces | `P1_direct_equals_minus_4_Einstein`, `P1_trace_identity`, `P2_trace_identity`, `P3_trace_identity` | `P1_equals_minus_4_Einstein`, `P1_trace_identity`, `P2_trace_identity`, `P3_trace_identity` |
| structure, $P_{(4)} = 0$, the variables | `P1_structure`, `P2_structure`, `P3_structure`, `independent_components`, `P4_vanishes_pigeonhole`, `lovelock_variables` | `P1_structure`, `P2_structure`, `P3_structure`, `independent_components` |
| divergence of $E_{(k)}$; the $E_{(k)}$ of `a4-equations.json` | `E1_divergence_free`, `E2_divergence_free`, `E3_divergence_free` | `E1_divergence_free`, `E2_divergence_free`, `E3_divergence_free`, `json_lovelock_components` |

What follows from the tensors of this record (taken from those reports, not derived here): the independent left-hand sides are $x_0 = x_5 = x_6 = x_7$, $x_1 = x_2 = x_3$ and $x_4$; there is no off-diagonal component, so a diagonal source suffices, and it needs $p_0 = p_t$ (the hidden pressure equal to the extra-time pressure) and no dependence on $x_0$. The $x_4$ component is a first-order constraint and the $x_1$ and $x_0$ components are linear in $(a_4'', v)$ (`constraint_first_order`, `second_order_system_a4pp_vv`); the constraint is propagated by the Bianchi identity (`constraint_propagation_bianchi`). With the author's weights $\alpha_k = w_k/H^{2k}$, $w = (1, \frac{1}{32}, \frac{1}{1152})$ and $\Lambda = -10$ ($H = 1$), the history $a_4 = Hx_4$, $b_4 = b_4(0)e^{(4/3)Hx_4}$ needs a source that is anisotropic and grows with $k = e^{(2/3)Hx_4}$ ($b_4(0) = 1$): $\kappa T - \Lambda\delta$ has $-\kappa\rho - \Lambda = \frac{121}{432} + \frac{161}{24}k - \frac{9}{16}k^2$, $\kappa p_3 - \Lambda = -\frac{5359}{3888} + \frac{1601}{216}k - \frac{9}{16}k^2$ and $\kappa p_t - \Lambda = \kappa p_0 - \Lambda = -\frac{497}{144} + \frac{79}{16}k$ (`author_weights_history_source`); the Revision notebook `lovelock_gkd.ipynb` (section 8.4 of its text) reproduces this source from the tensors of this record. The solutions of these equations and their sources are the subject of the field-theory documents `Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.md` and `Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md` and of the Kohn-Sham record, not of this one.

## 10. Verification records

Every check has a name, a verdict and a detail. Counts at the time of writing, as the JSON files give them (the publication test re-reads them):

| report | checks | PASS | FAIL |
| --- | --- | --- | --- |
| `Revision/gkd_lovelock/results/lovelock-report.json` | 27 | 27 | 0 |
| `Revision/gkd_lovelock/results/wolfram-gkd-report.json` | 29 | 29 | 0 |
| `Revision/gkd_lovelock/results/python-lovelock-report.json` | 56 | 56 | 0 |
| `Revision/field_equations_a4/reports/wolfram-a4-report.json` | 57 | 57 | 0 |
| `Revision/field_equations_a4/reports/python-a4-report.json` | 69 | 69 | 0 |

The report of the comparison with the author (section 8.2) has a third verdict, NOT-AVAILABLE, for objects of which the author's files hold no stored output; it is not a failure:

| report | checks | PASS | FAIL | NOT-AVAILABLE |
| --- | --- | --- | --- | --- |
| `Revision/gkd_lovelock/comparison/author-comparison-report.json` | 80 | 75 | 0 | 5 |

The Rust report stores each check with `"passed": true` instead of a verdict; its 27 checks are counted as PASS. The GKD self-test `Revision/gkd_lovelock/results/gkd-selftest.json` has no list of checks; its nine comparisons (section 3.3) all have 0 mismatches and its verdict is `SUCCESS`. The test file `Revision/tests/test_gkd_lovelock.py` pins the sha256 of the seven result files of the computation and its verifications (`curvature.json`, `lovelock-tensors.json`, `lovelock-components.md`, `lovelock-report.json`, `gkd-selftest.json`, `python-lovelock-report.json`, `wolfram-gkd-report.json`), requires every check to pass, and, in its slow tests, re-runs the Rust program, the sympy checker and the Wolfram check and requires byte-identical outputs.

Re-verification of the corrected metric (2026-10-16, development machine; `PROVENANCE_OF_THE_COMPUTATION.md` and part 6.5 of the provenance file `WOLFRAMSCRIPT_PROVENANCE.md` of `Revision/gkd_lovelock/verification/`): `lovelock_gkd lovelock --brute-force-k2` gave 27 of 27 checks in 13.3 s, two runs byte-identical; the sympy checker gave 56 of 56 checks in 13 s, twice, byte-identical reports; the Wolfram check gave 29 of 29 checks, `time_total` 47.5 s and 46.1 s, the two reports byte-identical.

## 11. Reproduction

### 11.1 Commands

From the repository root (Rust 1.87 or newer, Python 3 with sympy and numpy, Wolfram Language with WolframScript). A backslash at the end of a line is the line continuation of a POSIX shell; in PowerShell write such a command on one line:

```text
cargo build --release --manifest-path Revision/gkd_lovelock/code/Cargo.toml
Revision/gkd_lovelock/code/target/release/lovelock_gkd gkd-selftest \
    --exhaustive-max 4 --output Revision/gkd_lovelock/results
Revision/gkd_lovelock/code/target/release/lovelock_gkd lovelock \
    --output Revision/gkd_lovelock/results --brute-force-k2
python Revision/gkd_lovelock/verification/check_lovelock_gkd.py
wolframscript -file Revision/gkd_lovelock/verification/verify_lovelock_gkd.wls \
    Revision/gkd_lovelock/results/wolfram-gkd-report.json
wolframscript -file \
    Revision/gkd_lovelock/notebook_reading/lovelock_extract_nb_inputs.wls
python Revision/gkd_lovelock/notebook_reading/lovelock_digest_nb_inputs.py
wolframscript -file \
    Revision/gkd_lovelock/notebook_reading/lovelock_export_nb_image.wls
wolframscript -file \
    Revision/gkd_lovelock/comparison/extract_author_curvature_outputs.wls
python Revision/gkd_lovelock/comparison/compare_with_author.py
python -m unittest Revision/tests/test_gkd_lovelock.py -v
python scripts/build_provenance_pdf.py Revision/docs/LOVELOCK_GKD.md \
    --developer-layout --specifications Revision/pdf-specifications.json
python -m unittest Revision/tests/test_lovelock_gkd_publication.py -v
```

On Windows the binary is `lovelock_gkd.exe`. Each of the commands that write into `Revision/gkd_lovelock/results` overwrites a committed file with a byte-identical one; to leave the committed files untouched, give another output directory or report path and compare. The Wolfram check builds its exporter in `<$TemporaryDirectory>/revision_gkd_export` (or in `$LOVELOCK_GKD_EXPORT_DIR`); run only one copy at a time with the default directory. The notebook-reading commands need the author's notebook in the repository root and write the uncommitted text `build/lovelock_nb_inputs.txt`. The extractor needs both notebooks of the author in the repository root and the comparison the main one, `Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb`, whose sha256 it checks; the extractor writes `author-curvature-outputs.json` (or the file named by the environment variable `AUTHOR_CURVATURE_OUTPUTS`), and the comparison writes `author-comparison-report.json` (or the file given with `--output`). The gate `Revision/verify_revision.sh` and its PowerShell twin run them as the steps `gkd-author-extract` and `gkd-author-compare`.

### 11.2 Expected output

- `gkd-selftest`: nine lines starting with `PASS - GKD vs literal`, then `gkd-selftest: SUCCESS (...)`; the file `gkd-selftest.json` with the table of section 3.3.
- `lovelock`: the 27 check lines starting with `PASS - `, three lines starting with `info - ` (the scalar $L_{(4)}$ and the times of the two unpruned sums), the counter lines of section 5.2, then `check_count=27`, `failed_check_count=0` and `lovelock: SUCCESS (...)`; exit code 0.
- The sympy checker: 56 lines `[PASS] <name>` in six groups, then `total ... s; 56 checks, 0 failed; verdict SUCCESS`; exit code 0.
- The Wolfram check: ten `time_<step>=<seconds>` lines, the 29 lines `check_<name>=true`, then `check_count=29`, `failed_check_count=0`, `time_total=<seconds>` and `report=<path>`; exit code 0 (1 if a check fails, 2 on a load, build or input/output error).
- The notebook reading: `input cells written: 58`, `58 input cells`, `{1372, 435}` and `28229 bytes (117 bytes of text/time chunks removed)`, with both committed outputs reproduced byte for byte.
- The comparison with the author: the extractor prints `cells: 2127`, `inputs parsed: 8/8` and `outputs parsed: 4/4`, then the output dimensions and the keyword-scan counts; the comparison prints `checks: 80; PASS 75, FAIL 0, NOT-AVAILABLE 5`; both exit with code 0 and reproduce their committed outputs byte for byte.

### 11.3 Run times

From the provenance files (development machine, Windows 11):

- The Wolfram check, from part 6.5 of the provenance file `WOLFRAMSCRIPT_PROVENANCE.md` in `Revision/gkd_lovelock/verification/`: `time_total` 47.5 s and 46.1 s in the two runs of 2026-10-16 for the corrected metric (68.4 s in the run of 2026-10-08 for an earlier metric, on a loaded machine).
- The notebook reading, from the provenance file `WOLFRAMSCRIPT_PROVENANCE.md` in `Revision/gkd_lovelock/notebook_reading/`: the whole set takes about 10 to 25 seconds, and up to about 40 seconds on a fully loaded machine.
- The GKD self-test with `--exhaustive-max 4`: several minutes (`Revision/tests/test_gkd_lovelock.py`, which runs it only when `LOVELOCK_GKD_SELFTEST=1`).
- The Rust `lovelock` run: 13.3 s, and the sympy checker 13 s (section 10).
- The comparison with the author, from section 7 of the README of `Revision/gkd_lovelock/comparison/`: the extractor 4.4 to 6.0 s (seven runs), the comparison 0.7 to 0.9 s.

### 11.4 The PDF

The PDF build runs the Markdown-to-LaTeX builder twice (with different hash seeds), runs pdflatex three times into each of two fresh directories, requires warning-free logs and byte-identical PDFs, and checks the PDF against its entry `lovelock-gkd` in `Revision/pdf-specifications.json` (the Revision registry; the registry of the earlier stages is not touched).

## 12. What is established and what is not

### 12.1 Established

1. GKD equals the author's definition `kδ` for all index lists of equal length (theorem of section 3.2, with its proof); confirmed exhaustively up to length 4 (Rust) and length 3 (Wolfram, sympy) and on pseudo-random samples up to length 9.
2. For the corrected metric, for every real $z$ with $\sin z\cos z \neq 0$, with the conventions of sections 2.2 and 4.2: the 21 nonzero Christoffel symbols, the 112 nonzero $R^{ab}{}_{cd}$, the Ricci and Einstein tensors and the Lovelock tensors $P_{(k)}$, $A_{(k)}$ and scalars $L_{(k)}$, $k = 1, 2, 3$, exactly as listed in section 6 and in `lovelock-tensors.json`; three programs that share no code for the sums agree on every component.
3. $P_{(1)} = -4G$, $P_{(2)} = -8\mathcal{H}$ (Gauss-Bonnet), $L_{(1)} = 2R$, $L_{(2)} = 4\,GB$, $L_{(3)} = 8(2T_1 + \dots + T_8)$; the trace identities; $\nabla_hP_{(k)}{}^h{}_j = 0$; the symmetry of $A_{(k)}$; $P_{(4)} = 0$ in eight dimensions.
4. The structure: $R^{ab}{}_{cd}$ is sectional and free of $x_0$; every $P_{(k)}$ is diagonal and free of $x_0$, with $x_1 = x_2 = x_3$ and $x_0 = x_5 = x_6 = x_7$; it depends only on $H$, $a_4'$, $a_4''$, $u = b_4'/b_4$, $v = u'$ and $k = e^{2a_4}/b_4$, and the $x_4$ components contain no $a_4''$.
5. Agreement with the author's stored outputs of the earlier notebook (section 8.2; the frozen record of the withdrawn metric of 2026-10-14, at $b_4 = 1$): under the mapping stated before the comparison, the author's metric `Out[235]`, Ricci scalar `Out[535]` and all 64 components of the Einstein tensor `Out[536]` (raised with the author's own metric) equal those of that record exactly, and hence its $P_{(1)}$ and $L_{(1)}$ equal $-4$ times the author's Einstein tensor and 2 times the author's Ricci scalar; of the 80 checks 75 pass, none fails and 5 are NOT-AVAILABLE.

### 12.2 Not established

1. No solution: this record gives the left-hand sides of the field equations only. Which $a_4$, which $b_4$ and which sources solve them is not part of it (section 9).
2. The domain: every real $z$ with $\sin z\cos z \neq 0$. Nothing is computed at the folds $\cos z = 0$, where $g_{00} = 0$ and $\det g = 0$, or at the points $\sin z = 0$, where the metric is singular.
3. No comparison for $k = 2$ and $k = 3$: the author's files that were read hold no stored output of $P_{(2)}$, $P_{(3)}$, $L_{(2)}$ or $L_{(3)}$, nor of the Christoffel symbols, the Riemann tensor or the Ricci tensor (section 8.2). Agreement with the author's own Lovelock tensors of order $k = 2$ and $k = 3$ is therefore not established. For the corrected metric no output of the author exists. The notebooks in which, by the main notebook's text, the author calculates the Einstein-Lovelock tensors were not read; the limits of the comparison that was made are listed in section 8.3.
4. For $k = 3$ the tensor $P_{(3)}$ is verified by three independent recomputations, the trace, the divergence and the symmetry, and the scalar $L_{(3)}$ against the classical cubic density; it is not compared with an independent closed formula for the third-order Lovelock tensor. $E_{(k)} = -P_{(k)}/2^{k+1}$ is a normalisation convention, which equals the Einstein tensor for $k = 1$ and the Gauss-Bonnet tensor for $k = 2$.
5. The unpruned sums are exact for $k = 1, 2$ (sympy) and numerical at one point (Rust); for $k = 3$ the skipped terms are confirmed by a random sample (sympy) and by the theorem of section 3.2.
6. Only Wolfram Language 15.0.1 and the toolchains named in the provenance files were used.
7. No physical interpretation is attached to the components here; in particular nothing is said about the sign of an energy or about the stability of a solution.
