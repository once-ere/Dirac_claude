# The generalized Kronecker delta and the Lovelock tensors of the author's primordial metric

## GKD, the pure-Rust generalized Kronecker delta, and the exact Lovelock tensors of order k = 1, 2, 3 of Lovelock's equation (4.38) for the 4+4 metric with deflating extra times, with their independent verifications and an exact statement of what they establish

## Abstract

This document records the computation of `Revision/gkd_lovelock`: the generalized Kronecker delta of the author's notebook, re-implemented in pure Rust as the function GKD, and the three nonzero Lovelock tensors $P_{(1)}$, $P_{(2)}$, $P_{(3)}$ of Lovelock's equation (4.38) for the author's primordial metric of signature (4,4), in which the three extra times $x_5, x_6, x_7$ deflate as $e^{-a_4(x_4)}$ while 3-space inflates as $e^{a_4(x_4)}$. Every component of $P_{(k)}$ is an exact polynomial in $H$, $a_4'$ and $a_4''$; the tensors are diagonal, free of the warp factor $\sin^{1/3}z$, of $e^{a_4}$ and of $x_8$, with equal components in the three 3-space directions and in the three extra-time directions, and $P_{(4)} = 0$ identically in eight dimensions. The Rust program checks 19 identities (19 of 19 pass); GKD equals the author's determinant on all 16,777,216 pairs of index lists of length 4 and on 200,000 pseudo-random pairs of each length 5 to 9. Two independent verifications agree with every component: a Wolfram Language check that evaluates the author's definition verbatim (29 of 29 checks pass) and a sympy checker that shares no code with the Rust program (49 of 49 checks pass). The field equations for $a_4$ use these tensors with the normalisation $E_{(k)} = -P_{(k)}/2^{k+1}$, $E_{(1)} = G$. Not established here: any solution of the field equations, anything at or beyond the brane $z = \pi/2$, and a comparison with the answers in the output cells of the author's notebook, which were never read.

## 1. The task and the result

The author's test (2026-10-01, `Revision/README.md` and `Revision/SPEC.md` sections 5 and 10): refactor the author's Wolfram Language definition of the generalized Kronecker delta into a pure-Rust function GKD, use it to compute, with provenance, the three nonzero Lovelock tensors of Lovelock's equation (4.38) for the author's 8 x 8 metric, write every component, and do the work without reading the author's answers. The result, in one paragraph each:

1. GKD (section 3). For index lists of equal length, GKD returns the determinant of the author's 0/1 matrix without computing a determinant: it is the sign of the permutation that maps the lower list onto the upper list, or 0. The equality with the author's definition is a theorem (section 3.2), confirmed exhaustively and on random samples by three programs.
2. The Lovelock tensors (sections 4 to 6). $P_{(k)}{}^h{}_j$, $A_{(k)}{}^{lh}$ and $L_{(k)}$ for $k = 1, 2, 3$ are computed exactly from the metric alone, with every term of the sums weighted by an explicit call of GKD. Their nonzero components are listed in section 6.3.
3. The verifications (sections 7 and 10). The Rust program, the Wolfram check and the sympy checker agree exactly on every one of the 64 components of each tensor; every check of the three reports has the verdict PASS.
4. The use (section 9). The field equations for $a_4$ of `Revision/field_equations_a4` recompute the three tensors in both of their verifiers and compare them with the file of this record.

Every formula and number below is taken from the Revision files named with it; nothing is taken from the earlier stages of the repository. Interpretations are labelled as such.

## 2. Setting and conventions

### 2.1 The author's metric and coordinates

The coordinates are named as the author names them; arrays index them $0, \dots, 7$. $x_1, x_2, x_3$ are ordinary 3-space, which inflates with the scale factor $e^{a_4}\sin^{1/6}z$; $x_4$ is the time; $x_5, x_6, x_7$ are the three extra times, time-like, which DEFLATE exponentially with the scale factor $e^{-a_4}\sin^{1/6}z$ as $a_4(x_4)$ increases (they are never treated as static); $x_8$ is the hidden space direction with $z = 6Hx_8 \in (0,\pi/2)$; $H > 0$ is the author's constant and $a_4' = da_4/dx_4$. The metric of `Revision/SPEC.md` section 1, as the Rust program stores it (`metricDiagonal` of `curvature.json`), is

$$
\begin{aligned}
g = \mathrm{diag}\big(& e^{2a_4}\sin^{1/3}z,\ e^{2a_4}\sin^{1/3}z,\ e^{2a_4}\sin^{1/3}z,\ -1, \\
& -e^{-2a_4}\sin^{1/3}z,\ -e^{-2a_4}\sin^{1/3}z,\ -e^{-2a_4}\sin^{1/3}z,\ \cot^2 z\big),
\end{aligned}
$$

of signature (4,4): space-like $x_1, x_2, x_3, x_8$, time-like $x_4, x_5, x_6, x_7$. Its determinant is $\det g = \cos^2 z$, so $\sqrt{|g|} = \cos z$ on $0 < z < \pi/2$; the Rust program writes it as $\sin z\cot z$ (`sqrtAbsDetG`). The 7-volume factor $e^{3a_4}e^{-3a_4} = 1$ shows that the inflation of 3-space is compensated by the deflation of the extra times.

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

`lovelock_gkd gkd-selftest --exhaustive-max 4` compares GKD with `gkd.rs::kdelta_det` on every pair of index lists of length 1 to 4 over the eight labels and on 200,000 pseudo-random pairs (xorshift64*, half of them permutations of each other) of each length 5 to 9. The report `Revision/gkd_lovelock/results/gkd-selftest.json` has the verdict `SUCCESS`:

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

For the author's metric $n = 8$ and $m = 4$, so the sum runs over $k = 1, 2, 3$; $\sqrt{g}$ means $\sqrt{|\det g|} = \cos z$ (section 2.1).

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
- $P_{(k)}$ is stored with its first index up and its second down (`P1_mixed_up_h_down_j`, `P2_mixed_up_h_down_j`, `P3_mixed_up_h_down_j`); $A_{(k)}$ with both indices up (`A1_contravariant_l_h`, `A2_contravariant_l_h`, `A3_contravariant_l_h`). For the diagonal metric $A_{(k)}{}^{lh} = \cos z\;g^{ll}\,P_{(k)}{}^h{}_l$.
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
| `poly.rs` | `poly.rs::Poly`, `poly.rs::d` | exact Laurent polynomials with rational coefficients in $H$, $a_4'$ to $a_4''''$, $E = e^{a_4}$, $S = \sin^{1/3}z$, $C = \cot z$, with the exact derivatives in $x_4$ and $x_8$ |
| `geometry.rs` | `geometry.rs::metric_diagonal`, `geometry.rs::Geometry` | the metric, its inverse, $\sqrt{\lvert g\rvert} = S^3C$, the Christoffel symbols, $R^a{}_{bcd}$, $R^{ab}{}_{cd}$, Ricci and $R$ |
| `geometry.rs` | `geometry.rs::nonzero_mixed`, `geometry.rs::einstein_mixed` | the list of nonzero $R^{ab}{}_{cd}$; the Einstein tensor from the Ricci tensor |
| `lovelock.rs` | `lovelock.rs::lovelock_mixed`, `lovelock.rs::lovelock_scalar`, `lovelock.rs::dfs` | $P_{(k)}{}^h{}_j$ and $L_{(k)}$ by a depth-first search over the nonzero curvature entries |
| `lovelock.rs` | `lovelock.rs::lovelock_contravariant`, `lovelock.rs::divergence` | $A_{(k)}{}^{lh}$; the covariant divergence $\nabla_hP^h{}_j$ |
| `lovelock.rs` | `lovelock.rs::brute_force_numeric`, `lovelock.rs::usual_normalisation` | the unpruned literal sum at a numerical point; the factor $-1/2^{k+1}$ |
| `output.rs` | `output.rs::tensor_json`, `output.rs::monomials_json`, `output.rs::tensor_markdown` | deterministic JSON and Markdown writers |
| `main.rs` | `main.rs::gkd_selftest`, `main.rs::run_lovelock`, `main.rs::print_config` | the command line `gkd-selftest`, `lovelock`, `print-config` |

The symbols $S$ and $C$ satisfy $S^6(1 + C^2) = 1$, so the representation of `poly.rs` is not canonical in general; $S$ cancels identically in every mixed tensor the program prints, every zero test is done on mixed tensors, and the independent checkers use a canonical form (section 7.2).

### 5.2 The enumeration

For each pair $(h, j)$, `lovelock.rs::dfs` chooses $k$ ordered nonzero entries $R^{ab}{}_{cd}$ one after another and appends $a, b$ to the lower list and $c, d$ to the upper list. A branch is cut when an index would repeat within a list (GKD is 0 by cases (a) and (b)); at a leaf the two index SETS must be equal (otherwise GKD is 0 by case (c)), and only then is GKD called; a nonzero value multiplies the product of the chosen entries. A vanishing curvature factor gives a vanishing term, so only the nonzero entries are enumerated. The counters of `lovelock-report.json`:

| $k$ | leaves | GKD calls | nonzero GKD values | GKD calls for $L_{(k)}$ | nonzero components of $P_{(k)}$ |
| --- | --- | --- | --- | --- | --- |
| 1 | 5616 | 696 | 696 | 108 | 8 |
| 2 | 176640 | 32640 | 32640 | 7200 | 8 |
| 3 | 1128960 | 495360 | 495360 | 213120 | 8 |
| 4 | 0 | 0 | 0 | 1105920 | 0 |

The pruning is checked, not assumed: `lovelock.rs::brute_force_numeric` evaluates the completely unpruned literal sum, every index list sent to GKD, at the point $H = 0.23$, $a_4 = 0.17$, $a_4' = 0.61$, $a_4'' = -0.37$, $x_8 = 0.41$: 262144 index lists for $k = 1$ (maximal relative deviation from the exact $P_{(1)}$ 1.40e-15) and 1073741824 index lists for $k = 2$ (maximal relative deviation from the exact $P_{(2)}$ 4.41e-14) (`k1_brute_force_numeric`, `k2_brute_force_numeric`). The two independent checkers repeat the unpruned sums exactly (section 7).

## 6. Results

### 6.1 Christoffel symbols and curvature

`curvature.json` lists 25 nonzero Christoffel symbols $\Gamma^a{}_{bc}$ with $b \le c$. With $i = 1, 2, 3$ (3-space) and $t = 5, 6, 7$ (extra times):

$$
\begin{aligned}
&\Gamma^{x_i}{}_{x_ix_4} = a_4',\quad \Gamma^{x_t}{}_{x_4x_t} = -a_4',\quad \Gamma^{x_i}{}_{x_ix_8} = \Gamma^{x_t}{}_{x_tx_8} = H\cot z,\\
&\Gamma^{x_4}{}_{x_ix_i} = a_4'e^{2a_4}\sin^{1/3}z,\quad \Gamma^{x_4}{}_{x_tx_t} = a_4'e^{-2a_4}\sin^{1/3}z,\\
&\Gamma^{x_8}{}_{x_ix_i} = -He^{2a_4}\sin^{1/3}z\,\tan z,\quad \Gamma^{x_8}{}_{x_tx_t} = He^{-2a_4}\sin^{1/3}z\,\tan z,\\
&\Gamma^{x_8}{}_{x_8x_8} = -6H\tan z - 6H\cot z .
\end{aligned}
$$

The mixed Riemann tensor $R^{ab}{}_{cd}$ has 156 nonzero entries. Up to the antisymmetry in each index pair they are, with $i \ne i'$ in 3-space and $t \ne t'$ among the extra times:

| entry | value |
| --- | --- |
| $R^{x_ix_{i'}}{}_{x_ix_{i'}}$ and $R^{x_tx_{t'}}{}_{x_tx_{t'}}$ | $(a_4')^2 - H^2$ |
| $R^{x_ix_t}{}_{x_ix_t}$ | $-(a_4')^2 - H^2$ |
| $R^{x_ix_4}{}_{x_ix_4}$ | $a_4'' + (a_4')^2$ |
| $R^{x_4x_t}{}_{x_4x_t}$ | $-a_4'' + (a_4')^2$ |
| $R^{x_ix_8}{}_{x_ix_8}$ and $R^{x_tx_8}{}_{x_tx_8}$ | $-H^2$ |
| $R^{x_ix_4}{}_{x_ix_8}$ and $R^{x_4x_t}{}_{x_tx_8}$ | $Ha_4'\cot z$ |
| $R^{x_ix_8}{}_{x_ix_4}$ and $R^{x_tx_8}{}_{x_4x_t}$ | $-Ha_4'\tan z$ |

$R^{x_4x_8}{}_{x_4x_8} = 0$. Every $R^{ab}{}_{cd}$ is free of $\sin^{1/3}z$ and of $e^{a_4}$ (`mixed_riemann_free_of_sin_third`, `mixed_riemann_free_of_warp_and_exponential`). The deflation enters through $a_4'$ and $a_4''$ with the opposite sign of the inflating directions: the sectional curvature of the plane $(x_i, x_4)$ is $a_4'' + (a_4')^2$ and that of $(x_4, x_t)$ is $-a_4'' + (a_4')^2$.

The mixed Ricci tensor is diagonal, $R^{x_i}{}_{x_i} = a_4'' - 6H^2$, $R^{x_4}{}_{x_4} = 6(a_4')^2$, $R^{x_t}{}_{x_t} = -a_4'' - 6H^2$, $R^{x_8}{}_{x_8} = -6H^2$; the Ricci scalar is $R = 6(a_4')^2 - 42H^2$ (`ricciScalar`), and the Einstein tensor is

$$
\begin{aligned}
&G^{x_i}{}_{x_i} = a_4'' - 3(a_4')^2 + 15H^2,\quad G^{x_4}{}_{x_4} = 3(a_4')^2 + 21H^2,\\
&G^{x_t}{}_{x_t} = -a_4'' - 3(a_4')^2 + 15H^2,\quad G^{x_8}{}_{x_8} = -3(a_4')^2 + 15H^2 .
\end{aligned}
$$

### 6.2 The Lovelock scalars

From `lovelock-tensors.json` (keys `L1`, `L2`, `L3`):

$$
\begin{aligned}
L_{(1)} &= 12\,(a_4')^{2} - 84\,H^{2} ,\\
L_{(2)} &= -96\,(a_4')^{4} - 2112\,H^{2}\,(a_4')^{2} + 3360\,H^{4} ,\\
L_{(3)} &= 1152\,(a_4')^{6} + 31104\,H^{2}\,(a_4')^{4} + 100224\,H^{4}\,(a_4')^{2} - 40320\,H^{6} .
\end{aligned}
$$

### 6.3 The Lovelock tensors

Every $P_{(k)}{}^h{}_j$ is diagonal: all 56 off-diagonal components of each tensor vanish, including $x_4$-$x_8$. The diagonal satisfies $x_1 = x_2 = x_3$ and $x_5 = x_6 = x_7$, so four components per order are independent. The formulas below are the LaTeX texts of `lovelock-tensors.json`, unchanged.

$k = 1$:

$$
\begin{aligned}
P_{(1)}{}^{x_1}{}_{x_1} &= -4\,a_4'' + 12\,(a_4')^{2} - 60\,H^{2} \\
P_{(1)}{}^{x_4}{}_{x_4} &= -12\,(a_4')^{2} - 84\,H^{2} \\
P_{(1)}{}^{x_5}{}_{x_5} &= 4\,a_4'' + 12\,(a_4')^{2} - 60\,H^{2} \\
P_{(1)}{}^{x_8}{}_{x_8} &= 12\,(a_4')^{2} - 60\,H^{2}
\end{aligned}
$$

$k = 2$:

$$
\begin{aligned}
P_{(2)}{}^{x_1}{}_{x_1} &= 192\,(a_4')^{2}\,a_4'' - 96\,(a_4')^{4} + 320\,H^{2}\,a_4'' \\
&\quad - 1344\,H^{2}\,(a_4')^{2} + 1440\,H^{4} \\
P_{(2)}{}^{x_4}{}_{x_4} &= 288\,(a_4')^{4} + 960\,H^{2}\,(a_4')^{2} + 3360\,H^{4} \\
P_{(2)}{}^{x_5}{}_{x_5} &= -192\,(a_4')^{2}\,a_4'' - 96\,(a_4')^{4} - 320\,H^{2}\,a_4'' \\
&\quad - 1344\,H^{2}\,(a_4')^{2} + 1440\,H^{4} \\
P_{(2)}{}^{x_8}{}_{x_8} &= -96\,(a_4')^{4} - 1344\,H^{2}\,(a_4')^{2} + 1440\,H^{4}
\end{aligned}
$$

$k = 3$:

$$
\begin{aligned}
P_{(3)}{}^{x_1}{}_{x_1} &= -5760\,(a_4')^{4}\,a_4'' + 1152\,(a_4')^{6} - 6912\,H^{2}\,(a_4')^{2}\,a_4'' + 10368\,H^{2}\,(a_4')^{4} \\
&\quad - 5760\,H^{4}\,a_4'' + 31104\,H^{4}\,(a_4')^{2} - 5760\,H^{6} \\
P_{(3)}{}^{x_4}{}_{x_4} &= -5760\,(a_4')^{6} - 10368\,H^{2}\,(a_4')^{4} - 17280\,H^{4}\,(a_4')^{2} - 40320\,H^{6} \\
P_{(3)}{}^{x_5}{}_{x_5} &= 5760\,(a_4')^{4}\,a_4'' + 1152\,(a_4')^{6} + 6912\,H^{2}\,(a_4')^{2}\,a_4'' + 10368\,H^{2}\,(a_4')^{4} \\
&\quad + 5760\,H^{4}\,a_4'' + 31104\,H^{4}\,(a_4')^{2} - 5760\,H^{6} \\
P_{(3)}{}^{x_8}{}_{x_8} &= 1152\,(a_4')^{6} + 10368\,H^{2}\,(a_4')^{4} + 31104\,H^{4}\,(a_4')^{2} - 5760\,H^{6}
\end{aligned}
$$

Remarks, each an exact property of the listed components:

- $P_{(1)} = -4G$ component by component (compare section 6.1).
- Of the metric function only the derivatives $a_4'$ and $a_4''$ occur, not $a_4$ itself; $a_4''$ occurs only in the 3-space and extra-time components, with opposite signs (the inflating and the deflating directions), and never in the $x_4$ and $x_8$ components.
- $P_{(k)}^{x_1}{}_{x_1} + P_{(k)}^{x_5}{}_{x_5} = 2P_{(k)}^{x_8}{}_{x_8}$ for $k = 1, 2, 3$ (read off the lists above).
- The contravariant densities are $A_{(k)}{}^{ll} = \cos z\;g^{ll}\,P_{(k)}{}^l{}_l$, with $g^{x_ix_i} = e^{-2a_4}\sin^{-1/3}z$, $g^{x_4x_4} = -1$, $g^{x_tx_t} = -e^{2a_4}\sin^{-1/3}z$ and $g^{x_8x_8} = \tan^2z$; for example the file gives $A_{(1)}{}^{x_4x_4} = 12\,(a_4')^{2}\,\sin(6Hx_8)\,\cot(6Hx_8) + 84\,H^{2}\,\sin(6Hx_8)\,\cot(6Hx_8)$. All 64 components of each $A_{(k)}$, each with its exact monomial list, are in `lovelock-tensors.json`; all 384 components of $P_{(k)}$ and $A_{(k)}$ are also written out in `lovelock-components.md`.

### 6.4 The checks of the Rust program

`lovelock_gkd lovelock --brute-force-k2` writes `curvature.json`, `lovelock-tensors.json`, `lovelock-components.md` and `lovelock-report.json`. The report gives `"checkCount": 19`, `"failedCheckCount": 0` and `"verdict": "SUCCESS"`; every one of its 19 checks has `"passed": true`:

| check | check | check |
| --- | --- | --- |
| `riemann_antisymmetry` | `riemann_first_bianchi` | `mixed_riemann_free_of_sin_third` |
| `k1_equals_minus_4_einstein` | `k1_trace_identity` | `k1_divergence_free` |
| `k1_symmetric` | `k1_free_of_sin_third` | `k2_trace_identity` |
| `k2_divergence_free` | `k2_symmetric` | `k2_free_of_sin_third` |
| `k3_trace_identity` | `k3_divergence_free` | `k3_symmetric` |
| `k3_free_of_sin_third` | `k4_tensor_vanishes` | `k1_brute_force_numeric` |
| `k2_brute_force_numeric` | | |

They are mathematical identities, not comparisons with the author's numbers: the antisymmetries and the first Bianchi identity of $R^{ab}{}_{cd}$ for all 4096 index lists, $P_{(1)} = -4G$ by an independent route, the trace identities, $\nabla_hP_{(k)}{}^h{}_j = 0$ for every $j$, the symmetry of $g_{hh}P_{(k)}{}^h{}_j$ (so $A_{(k)}{}^{lh} = A_{(k)}{}^{hl}$), the absence of the warp factor, $P_{(4)} = 0$ and the unpruned numerical sums. Two runs give byte-identical files (`Revision/gkd_lovelock/results/PROVENANCE_OF_THE_COMPUTATION.md`).

## 7. Independent verifications

### 7.1 The Wolfram check (29 checks)

`Revision/gkd_lovelock/verification/verify_lovelock_gkd.wls` with the package `LovelockGKDCheck.wl` writes `wolfram-gkd-report.json`: `"checkCount": 29`, `"expectedCheckCount": 29`, `"failedCheckCount": 0`, `"verdict": "SUCCESS"`, producer Wolfram Language 15.0.1. What it does:

- The author's definition, re-typed verbatim, is the kernel's definition of `kδ` (compared with the text recorded in `PROVENANCE_OF_THE_COMPUTATION.md`), with `delta[a_Integer, b_Integer] := KroneckerDelta[a, b]`; unequal lengths stay unevaluated.
- GKD is NOT re-implemented in Wolfram Language: a small exporter compiled with cargo against the unchanged crate writes the values of the Rust function GKD for 346304 pairs (all 64, 4096 and 262144 pairs of lengths 1, 2, 3 and 20000 pseudo-random pairs of each length 4 to 7; values file of 3161984 bytes), and the verbatim `kδ` is evaluated on every pair: 0 mismatches. The negative control against $-$GKD reports a mismatch at exactly every pair where GKD is nonzero (8, 112, 2016, 10022, 10005, 10002, 10000 pairs for lengths 1 to 7).
- The curvature is recomputed from the metric with `D`, `Inverse` and `Simplify` (156 nonzero $R^{ab}{}_{cd}$, the same as `curvature.json`), and $\det g = \cos^2 z$.
- The Lovelock tensors are recomputed with the verbatim `kδ`: for $k = 1$ and $k = 2$ every $k$-tuple of the 156 nonzero entries for each of the 64 components (9984 and 1557504 calls), for $k = 3$ every list left after skipping lists with a repeated label in a row (1128960 calls). `FullSimplify` of the difference with the Rust tensors is 0 for all 64 components of each $P_{(k)}$ and $A_{(k)}$. The numbers of nonzero `kδ` terms, 696, 32640 and 495360, equal the Rust counters. A tampered $P_{(2)}$ component and a tampered $A_{(3)}$ component are flagged, and only those.

| check | check |
| --- | --- |
| `definition_is_the_authors_verbatim` | `definition_unequal_lengths_stay_unevaluated` |
| `gkd_values_file_layout` | `gkd_equals_kdelta_exhaustive_length_1` |
| `gkd_equals_kdelta_exhaustive_length_2` | `gkd_equals_kdelta_exhaustive_length_3` |
| `gkd_equals_kdelta_random_length_4` | `gkd_equals_kdelta_random_length_5` |
| `gkd_equals_kdelta_random_length_6` | `gkd_equals_kdelta_random_length_7` |
| `negative_control_gkd_comparison_detects_a_sign_flip` | `riemann_mixed_equals_rust_curvature` |
| `sqrt_det_g_is_cos` | `lovelock_kdelta_values_are_integers` |
| `k1_P_equals_rust_all_64_components` | `k1_A_equals_rust_all_64_components` |
| `k2_P_equals_rust_all_64_components` | `k2_A_equals_rust_all_64_components` |
| `k3_P_equals_rust_all_64_components` | `k3_A_equals_rust_all_64_components` |
| `negative_control_tensor_comparison_detects_a_change` | `k1_equals_minus_4_einstein` |
| `k1_trace_equals_6_L1` | `k2_trace_equals_4_L2` |
| `k3_trace_equals_2_L3` | `k1_nonzero_kdelta_terms_equal_rust_counter` |
| `k2_nonzero_kdelta_terms_equal_rust_counter` | `k3_nonzero_kdelta_terms_equal_rust_counter` |
| `rust_json_text_equals_its_monomials` | |

Scope. The Wolfram check is independent of the Rust code in its definition of $\delta$ (the author's verbatim text), its curvature and its Lovelock sums; it uses the Rust program for the GKD values it compares and for the tensors it compares with. Its default run skips, for $k = 3$, lists with a repeated label in a row (their determinant is 0 because two rows or columns are equal); an optional mode recomputes the eight diagonal $k = 3$ components with no skip at all, and its single recorded run passed 30 of 30 checks (`Revision/gkd_lovelock/verification/WOLFRAMSCRIPT_PROVENANCE.md`, part 4.5); that report is not committed. Only Wolfram 15.0.1 was used.

### 7.2 The sympy checker (49 checks)

The sympy checker is the file `check_lovelock_gkd.py` in the folder `Revision/gkd_lovelock/verification/`. Its report `python-lovelock-report.json` gives `"checkCount": 49`, `"failedCheckCount": 0` and `"verdict": "SUCCESS"`. It shares no code with the Rust crate: the geometry is sympy's own differentiation, $\delta$ is the author's definition evaluated with sympy's determinant (memoised by the 0/1 matrix), and the sums are organised breadth-first (all $k$-fold products with pairwise different lower and pairwise different upper indices, then completed by every admissible $h$ and $j$, one literal call of the determinant per term). Its counters:

| $k$ | products | determinant calls | nonzero values | distinct multisets |
| --- | --- | --- | --- | --- |
| 1 | 156 | 5772 | 804 | 156 |
| 2 | 11040 | 187680 | 39840 | 5520 |
| 3 | 282240 | 1411200 | 708480 | 47040 |

with 4096401 determinant calls in all and 29030 distinct 0/1 matrices determined by sympy. The skipped terms are checked as well: the completely unpruned literal sums for $k = 1$ (10140 calls) and $k = 2$ (1581840 calls) agree exactly with the pruned sums; 20000 random terms of the unpruned $k = 3$ sum, 19900 of them with a repeated index, give 0 whenever skipped; 300 random 9-index lists give 0. The comparison with the Rust output is exact three times over: by an exact canonical form (`canon`, which uses $s^6(1 + c^2) = 1$ to reach a unique form, so a zero difference is a proof of equality), by plain sympy simplification, and numerically with 60 digits at 5 random rational points.

| check | check | check |
| --- | --- | --- |
| `gkd_literal_equals_cofactor_expansion` | `gkd_examples` | `gkd_nine_indices_in_eight_dimensions_vanish` |
| `normalisation_P1_derived_minus_4` | `normalisation_P2_derived_minus_8` | `normalisation_L3_cubic_derived` |
| `metric_inverse` | `sqrt_abs_det_g` | `christoffel_symmetric` |
| `riemann_first_bianchi` | `mixed_riemann_free_of_warp_and_exponential` | `riemann_antisymmetry_and_pair_symmetry` |
| `k1_unpruned_literal_sum_agrees` | `k2_unpruned_literal_sum_agrees` | `k3_pruned_terms_vanish_literally` |
| `k4_terms_vanish_literally` | `k1_equals_minus_4_einstein` | `L1_equals_2R` |
| `k2_equals_minus_8_gauss_bonnet` | `L2_equals_4_gauss_bonnet` | `gauss_bonnet_index_placement` |
| `L3_equals_8_cubic_lovelock_density` | `k1_trace_identity` | `k2_trace_identity` |
| `k3_trace_identity` | `k1_divergence_free` | `k1_symmetric` |
| `k1_free_of_warp` | `k2_divergence_free` | `k2_symmetric` |
| `k2_free_of_warp` | `k3_divergence_free` | `k3_symmetric` |
| `k3_free_of_warp` | `rust_k1_mixed_components_agree` | `rust_k1_contravariant_components_agree` |
| `rust_L1_agrees` | `rust_k2_mixed_components_agree` | `rust_k2_contravariant_components_agree` |
| `rust_L2_agrees` | `rust_k3_mixed_components_agree` | `rust_k3_contravariant_components_agree` |
| `rust_L3_agrees` | `negative_controls_detected` | `rust_metric_and_sqrt_g_agree` |
| `rust_christoffels_agree` | `rust_riemann_agrees` | `rust_ricci_einstein_scalar_agree` |
| `rust_text_matches_monomials` | | |

Scope. The sympy checker reads only the metric (typed in from the task text) and, for the comparison, `curvature.json` and `lovelock-tensors.json`; it never reads the author's notebook. Its literal $\delta$ is compared with an independent cofactor expansion on all 266304 pairs of lengths 1 to 3 and 7500 random pairs of lengths 4 to 8. The negative controls (a coefficient increased by 1, a wrong power of $\sin^{1/3}z$, a wrong power of $e^{a_4}$, an added $10^{-30}H^4$) are each detected by each of its three comparison methods.

## 8. The comparison with the author's notebook

What was read is recorded in `PROVENANCE_OF_THE_COMPUTATION.md`, written before any comparison, and in the provenance file `WOLFRAMSCRIPT_PROVENANCE.md` of the folder `Revision/gkd_lovelock/notebook_reading/`: only the 58 INPUT cells of `Generalized _Kronecker_Delta_4+4.nb` (sha256 `23bb4e0c70943e766d9b081a3a399ef29664889aad088041329ce2e065b80afb`), converted to text without evaluation; the committed digest `notebook-input-cells.txt` gives, for each, its label, its length and its first 160 characters. The definition of `kδ` was taken from the cell `In[87]` and Lovelock's equation from the picture in the cell `In[101]` (1372 x 435 pixels). No output cell, no file `Generalized_Kronecker_Delta.txt` and no other Mathematica file of the author was opened; the metric was taken from the author's message.

What the notebook computes, as far as its input cells show (a reading of the digest, labelled as such): it sets up the xAct packages, an 8-dimensional manifold and a metric of signature (4,4) (`In[29]`); it builds the generalized delta in a second way, as contracted products of two Levi-Civita tensors divided by $(8 - p)!$ (`delta11`, `delta22`, `delta33`, `delta55`); it defines `kδ` (`In[87]`) and evaluates it for 3, 5 and 7 index pairs (`kδ33`, `kδ55`, `kδ77`); it compares the two constructions (`In[102]`, `In[105]`, `In[108]`); and it contains the picture of (4.38). Its answers are in the output cells, which were not read.

The comparison that was made:

- The definition: `definition_is_the_authors_verbatim` shows that the definition evaluated by the Wolfram check is the author's text, character for character.
- The function: GKD equals the author's `kδ` on every pair of lists of length 1 to 3, on 20000 random pairs of each length 4 to 7 (Wolfram), and equals the literal determinant on every pair of length 1 to 4 and 200000 random pairs of each length 5 to 9 (Rust self-test), as the theorem of section 3.2 requires.
- The equation: the tensors are those of (4.38) as shown in the notebook's picture, with the conventions of section 4.2.

The comparison that was NOT made: `PROVENANCE_OF_THE_COMPUTATION.md` announces a comparison with the author's own answers in a later commit; no file under `Revision/` records it. Whether the Lovelock tensors of this record agree with any tensors computed in the author's notebooks is therefore not established (section 12).

## 9. How the field equations for $a_4$ use the Lovelock tensors

`Revision/field_equations_a4` writes the Einstein-Lovelock equations of `Revision/SPEC.md` section 5 for the author's metric,

$$
\sum_{k=1}^{3}\alpha_k\,E_{(k)}{}^\mu{}_\nu + \Lambda\,\delta^\mu_\nu = \kappa\,T^\mu{}_\nu,\qquad E_{(k)} = -\frac{P_{(k)}}{2^{k+1}},\qquad E_{(1)} = G ,
$$

with $\alpha_1 = 1$ for Einstein gravity ($\alpha_2 = \alpha_3 = 0$). Both of its verifiers recompute the three tensors with their own GKD (Wolfram: as the determinant of the delta matrix; sympy: as the permutation sign) and compare all 64 components of each with the exact monomial lists of `Revision/gkd_lovelock/results/lovelock-tensors.json`:

| step | Wolfram records (`wolfram-a4-report.json`) | sympy records (`python-a4-report.json`) |
| --- | --- | --- |
| $P_{(k)}$ equal to this record | `P1_direct_equals_gkd_branch_monomials`, `P2_direct_equals_gkd_branch_monomials`, `P3_direct_equals_gkd_branch_monomials` | `P1_equals_gkd_branch_monomials`, `P2_equals_gkd_branch_monomials`, `P3_equals_gkd_branch_monomials` |
| $L_{(k)}$ equal to this record | `L1_direct_equals_gkd_branch`, `L2_direct_equals_gkd_branch`, `L3_direct_equals_gkd_branch` | `L1_equals_gkd_branch`, `L2_equals_gkd_branch`, `L3_equals_gkd_branch` |
| $P_{(1)} = -4G$, traces | `P1_direct_equals_minus_4_Einstein`, `P1_trace_identity`, `P2_trace_identity`, `P3_trace_identity` | `P1_equals_minus_4_Einstein`, `P1_trace_identity`, `P2_trace_identity`, `P3_trace_identity` |
| structure, $P_{(4)} = 0$ | `P1_structure`, `P2_structure`, `P3_structure`, `independent_components`, `P4_vanishes_pigeonhole` | `P1_structure`, `P2_structure`, `P3_structure`, `other_components_vanish` |
| divergence of $E_{(k)}$; the $E_{(k)}$ of `a4-equations.json` | `E1_divergence_free`, `E2_divergence_free`, `E3_divergence_free` | `E1_divergence_free`, `E2_divergence_free`, `E3_divergence_free`, `json_lovelock_components` |

What follows from the tensors of this record (taken from those reports, not derived here): the independent components are $x_1 = x_2 = x_3$, $x_4$, $x_5 = x_6 = x_7$, $x_8$ and the pair $x_4$-$x_8$, whose left-hand side is 0; the evolution equation, the 3-space minus extra-time combination, factorises as $a_4''\,F(a_4') = \kappa(p_3 - p_t)$ with

$$
F(a_4') = 2\alpha_1 - 48\alpha_2(a_4')^2 - 80\alpha_2H^2 + 720\alpha_3(a_4')^4 + 864\alpha_3(a_4')^2H^2 + 720\alpha_3H^4
$$

(Wolfram record `evolution_factorises_a4pp_times_F`, sympy record `evolution_factorises`). The identity $P_{(k)}^{x_1}{}_{x_1} + P_{(k)}^{x_5}{}_{x_5} = 2P_{(k)}^{x_8}{}_{x_8}$ of section 6.3 becomes the source condition $p_3 + p_t = 2p_8$ (`algebraic_identity_x1_plus_x5_minus_2x8`, `algebraic_identity`). The solutions of these equations and their sources are the subject of the field-theory documents `Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.md` and `Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md`, not of this one.

## 10. Verification records

Every check has a name, a verdict and a detail. Counts at the time of writing, as the JSON files give them (the publication test re-reads them):

| report | checks | PASS | FAIL |
| --- | --- | --- | --- |
| `Revision/gkd_lovelock/results/lovelock-report.json` | 19 | 19 | 0 |
| `Revision/gkd_lovelock/results/wolfram-gkd-report.json` | 29 | 29 | 0 |
| `Revision/gkd_lovelock/results/python-lovelock-report.json` | 49 | 49 | 0 |
| `Revision/field_equations_a4/reports/wolfram-a4-report.json` | 52 | 52 | 0 |
| `Revision/field_equations_a4/reports/python-a4-report.json` | 63 | 63 | 0 |

The Rust report stores each check with `"passed": true` instead of a verdict; its 19 checks are counted as PASS. The GKD self-test `Revision/gkd_lovelock/results/gkd-selftest.json` has no list of checks; its nine comparisons (section 3.3) all have 0 mismatches and its verdict is `SUCCESS`. The test file `Revision/tests/test_gkd_lovelock.py` pins the sha256 of the seven result files of the computation and its verifications (`curvature.json`, `lovelock-tensors.json`, `lovelock-components.md`, `lovelock-report.json`, `gkd-selftest.json`, `python-lovelock-report.json`, `wolfram-gkd-report.json`), requires every check to pass, and, in its slow tests, re-runs the Rust program, the sympy checker and the Wolfram check and requires byte-identical outputs.

Re-verification for this document (2026-10-08, on the shared machine of the provenance files; written to a scratch directory, the committed files untouched): `lovelock_gkd lovelock --brute-force-k2` gave 19 of 19 checks in 18.9 s and four files byte-identical to the committed ones; the sympy checker gave 49 of 49 checks in 40.3 s and a report byte-identical to the committed one. These two run times are measurements made while writing this document; they are not recorded in a report.

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
python -m unittest Revision/tests/test_gkd_lovelock.py -v
python scripts/build_provenance_pdf.py Revision/docs/LOVELOCK_GKD.md \
    --developer-layout --specifications Revision/pdf-specifications.json
python -m unittest Revision/tests/test_lovelock_gkd_publication.py -v
```

On Windows the binary is `lovelock_gkd.exe`. Each of the commands that write into `Revision/gkd_lovelock/results` overwrites a committed file with a byte-identical one; to leave the committed files untouched, give another output directory or report path and compare. The Wolfram check builds its exporter in `<$TemporaryDirectory>/revision_gkd_export` (or in `$LOVELOCK_GKD_EXPORT_DIR`); run only one copy at a time with the default directory. The notebook-reading commands need the author's notebook in the repository root and write the uncommitted text `build/lovelock_nb_inputs.txt`.

### 11.2 Expected output

- `gkd-selftest`: nine lines starting with `PASS - GKD vs literal`, then `gkd-selftest: SUCCESS (...)`; the file `gkd-selftest.json` with the table of section 3.3.
- `lovelock`: the 19 check lines starting with `PASS - `, three lines starting with `info - ` (the scalar $L_{(4)}$ and the times of the two unpruned sums), the counter lines of section 5.2, then `check_count=19`, `failed_check_count=0` and `lovelock: SUCCESS (...)`; exit code 0.
- The sympy checker: 49 lines `[PASS] <name>` in six groups, then `total ... s; 49 checks, 0 failed; verdict SUCCESS`; exit code 0.
- The Wolfram check: ten `time_<step>=<seconds>` lines, the 29 lines `check_<name>=true`, then `check_count=29`, `failed_check_count=0`, `time_total=<seconds>` and `report=<path>`; exit code 0 (1 if a check fails, 2 on a load, build or input/output error).
- The notebook reading: `input cells written: 58`, `58 input cells`, `{1372, 435}` and `28229 bytes (117 bytes of text/time chunks removed)`, with both committed outputs reproduced byte for byte.

### 11.3 Run times

From the provenance files (shared 24-core machine, Windows 11):

- The Wolfram check, from part 4.4 of the provenance file `WOLFRAMSCRIPT_PROVENANCE.md` in `Revision/gkd_lovelock/verification/`: `time_total` 68.4 s in the run of 2026-10-08 that regenerated the committed report, 68-135 s over seven runs; the $k = 2$ sum took 26-43 s and the $k = 3$ sum 35-77 s over eight runs; peak memory of the kernel about 486 MB working set. The optional no-skip mode for $k = 3$ took 1637.7 s (part 4.5).
- The notebook reading, from the provenance file `WOLFRAMSCRIPT_PROVENANCE.md` in `Revision/gkd_lovelock/notebook_reading/`: the whole set takes about 10 to 25 seconds, and up to about 40 seconds on a fully loaded machine.
- The GKD self-test with `--exhaustive-max 4`: several minutes (`Revision/tests/test_gkd_lovelock.py`, which runs it only when `LOVELOCK_GKD_SELFTEST=1`).
- The Rust `lovelock` run and the sympy checker: no run time is recorded in a provenance file; see the measurement of section 10 (18.9 s and 40.3 s).

### 11.4 The PDF

The PDF build runs the Markdown-to-LaTeX builder twice (with different hash seeds), runs pdflatex three times into each of two fresh directories, requires warning-free logs and byte-identical PDFs, and checks the PDF against its entry `lovelock-gkd` in `Revision/pdf-specifications.json` (the Revision registry; the registry of the earlier stages is not touched).

## 12. What is established and what is not

### 12.1 Established

1. GKD equals the author's definition `kδ` for all index lists of equal length (theorem of section 3.2, with its proof); confirmed exhaustively up to length 4 (Rust) and length 3 (Wolfram, sympy) and on pseudo-random samples up to length 9.
2. For the author's metric on $0 < z < \pi/2$, with the conventions of sections 2.2 and 4.2: the 25 nonzero Christoffel symbols, the 156 nonzero $R^{ab}{}_{cd}$, the Ricci and Einstein tensors and the Lovelock tensors $P_{(k)}$, $A_{(k)}$ and scalars $L_{(k)}$, $k = 1, 2, 3$, exactly as listed in section 6 and in `lovelock-tensors.json`; three programs that share no code for the sums agree on every component.
3. $P_{(1)} = -4G$, $P_{(2)} = -8\mathcal{H}$ (Gauss-Bonnet), $L_{(1)} = 2R$, $L_{(2)} = 4\,GB$, $L_{(3)} = 8(2T_1 + \dots + T_8)$; the trace identities; $\nabla_hP_{(k)}{}^h{}_j = 0$; the symmetry of $A_{(k)}$; $P_{(4)} = 0$ in eight dimensions.
4. The structure: diagonal, free of $\sin^{1/3}z$, $e^{a_4}$ and $x_8$, with $x_1 = x_2 = x_3$ and $x_5 = x_6 = x_7$, and with $a_4''$ entering the 3-space and extra-time components with opposite signs.

### 12.2 Not established

1. No solution: this record gives the left-hand sides of the field equations only. Which $a_4$ and which sources solve them is not part of it (section 9).
2. The domain: only the patch $0 < z < \pi/2$, where $\sqrt{|g|} = \cos z$. Nothing is computed at the brane $z = \pi/2$, where $g_{88} = \cot^2z = 0$ and $\det g = 0$, or on a mirror patch.
3. No comparison with the author's answers: the output cells of the author's notebook were never read, and the announced comparison is not recorded in `Revision/` (section 8). Agreement with the author's own Lovelock tensors is therefore not established.
4. For $k = 3$ the tensor $P_{(3)}$ is verified by three independent recomputations, the trace, the divergence and the symmetry, and the scalar $L_{(3)}$ against the classical cubic density; it is not compared with an independent closed formula for the third-order Lovelock tensor. $E_{(k)} = -P_{(k)}/2^{k+1}$ is a normalisation convention, which equals the Einstein tensor for $k = 1$ and the Gauss-Bonnet tensor for $k = 2$.
5. The unpruned sums are exact for $k = 1, 2$ (sympy) and numerical at one point (Rust); for $k = 3$ the skipped terms are confirmed by a random sample (sympy) and by the theorem of section 3.2; the Wolfram no-skip run of the diagonal $k = 3$ components is recorded in its provenance file only, and its report is not committed.
6. Only Wolfram Language 15.0.1 and the toolchains named in the provenance files were used.
7. No physical interpretation is attached to the components here; in particular nothing is said about the sign of an energy or about the stability of a solution.
