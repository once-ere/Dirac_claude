# dirac16complex00 in the primordial gravitational field

## The semi-classical Pin(4,4) spinor field: Lagrangian, field equations, non-triviality [2], energy-momentum tensor, equations of state and the field equations for a4[x4] and b4[x4] (Revision record)

## Abstract

This document records, for the author's primordial gravitational field of `Revision/SPEC.md` section 1, the field theory of dirac16complex00: a field $\Phi$ with 16 complex commuting components that transform as a spinor of Pin(4,4) (a set of 16 scalar fields that transform as a Pin(4,4) spinor), treated as a classical ("semi-classical") field. The metric is the author's metric of 2026-10-14, whose three extra-time components carry a second function $b_4(x_4) > 0$; on the user's order of 2026-10-15 every statement is proved for general functions $a_4$ and $b_4$, and $b_4$ is never 1 (the earlier metric with $b_4 = 1$ is withdrawn). The document gives the Lagrangian and its coupling to gravity through the vielbein and the canonical spin connection, the exact Euler-Lagrange equations (covariant, explicit in the metric, and as 16 component equations), the non-triviality theorem [2] with its proof and its exact scope (in the diagonal vielbein the gravitational term of the field equation is $\gamma^\mu\Omega_\mu = 3H\gamma^{(x_0)} + \tfrac34(b_4'/b_4)\gamma^{(x_4)}$, never zero for $H > 0$; this value depends on the frame and on the field variables, while $\Omega_\mu$ itself vanishes in no frame because the metric is curved), the self-consistency of the equations and its limits (no well-posed Cauchy problem for data that depend on the extra times; boundary terms at $z = \pi/2$), the energy-momentum tensor as a classical bilinear, its kinetic and potential parts, the energy density, the pressures and the equations of state, and the Einstein-Lovelock field equations for $a_4(x_4)$ and $b_4(x_4)$ with dirac16complex00 as the source. Every formula is an output of Revision code (Wolfram and an independent sympy checker for each part); each section ends with the names of the checks that verify it, and the check index collects them. Nothing is taken from the earlier stages of the repository. The classical energy of dirac16complex00 is unbounded below already for $U = 0$ (positive-frequency modes of negative energy) and its charge is indefinite and only locally conserved (the charge of a slice is constant only if no charge flows through the brane $z = \pi/2$, where this record imposes no boundary condition). A homogeneous condensate cannot be the source of the metric with $b_4$ not constant in Einstein gravity, and with the author's Lovelock weights it is the source of no exponential history with $b_4$ not constant; the background history of SPEC section 1 requires a constant source of negative energy density that no condensate supplies. What the record does not establish is stated in the section "What is not claimed". The verdict of the dark-sector investigation of Hypothesis00 is summarised in section 10, from `Revision/docs/DARK_SECTOR_HYPOTHESES`, and section 1 points to the other Revision documents.

## 1. Scope, sources and conventions

**Sources.** Every formula and number below is read from these Revision outputs (all produced by Revision code, all checks passing):

| part | Wolfram record | independent sympy record |
| --- | --- | --- |
| gammas, Pin(4,4), Spin(4,4) (SPEC section 2) | `Revision/algebra/reports/wolfram-algebra.json`, fixture `Revision/algebra/gammas.json` | `Revision/algebra/reports/python-algebra.json` |
| geometry with $b_4$, Lagrangian, field equations, energy-momentum tensor (SPEC sections 1-4) | `Revision/theory/reports/wolfram-field-theory.json`, formulas `Revision/theory/field-theory.json` | `Revision/theory/reports/python-field-theory.json` |
| field equations for $a_4(x_4)$ and $b_4(x_4)$ (SPEC section 5) | `Revision/field_equations_a4/reports/wolfram-a4-report.json`, formulas `Revision/field_equations_a4/a4-equations.json` | `Revision/field_equations_a4/reports/python-a4-report.json` |
| pairing theorems (SPEC section 9) | `Revision/pairing/reports/wolfram-pairing.json`, theorems `Revision/pairing/pairing-theory.json` | `Revision/pairing/reports/python-pairing.json` |
| scope of the statements: frame dependence, boundary terms, growth, sign of the energy | `Revision/theory/reports/wolfram-scope.json` | `Revision/theory/reports/python-scope.json` |

The Wolfram and the sympy records are written independently (no shared code); each sympy record re-derives the statements and compares them with the Wolfram record. The theory records verify every statement for both statistics: the checks whose names end in `_C` (Wolfram) or start with `commuting_` (sympy) are the ones for the commuting field dirac16complex00 of this document; the Grassmann versions belong to dirac16complex (`Revision/docs/DIRAC16COMPLEX_FIELD_THEORY`).

**Related Revision documents.** The generalized Kronecker delta and the Lovelock tensors $P_{(1)}$, $P_{(2)}$, $P_{(3)}$ behind the field equations for $a_4$ and $b_4$ of section 11 are described in `Revision/docs/LOVELOCK_GKD`. Hypothesis00 (SPEC section 8) is investigated in `Revision/docs/DARK_SECTOR_HYPOTHESES`, whose verdict for dirac16complex00 is summarised at the end of section 10; its two dirac16complex00 records are `Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json` (the derivations and the models; 49 of 49 checks pass) and `Revision/dark_sector/dirac16complex00/reports/python-independent-numerics.json` (an independent implementation from solutions of the field equation; 32 of 32 checks pass). The pairing theorems for both fields are in `Revision/docs/PAIR_CREATION_PROOFS`. The Kohn-Sham model of `Revision/docs/KOHN_SHAM_DEFLATING_FIELD` belongs to dirac16complex and is not used here.

**Coordinates (the author's).** $x_0, x_1, \dots, x_7$, in the author's order: $x_0$ is the hidden space direction; $x_1, x_2, x_3$ are ordinary 3-space (inflating, scale factor $e^{a_4}\sin^{1/6}z$); $x_4$ is the time; $x_5, x_6, x_7$ are the three extra times, time-like, which deflate (scale factor $e^{-a_4}b_4^{1/2}\sin^{1/6}z$; on the background history below it is proportional to $e^{-a_4/3}$, an exponential deflation). (Until 2026-10-14 this record named them $x_1, \dots, x_8$, with the hidden direction $x_8$ listed last; the user ordered the author's coordinates on 2026-10-14.) Throughout $z = 6Hx_0 \in (0, \pi/2)$, $H > 0$ is the author's constant, $a_4' = da_4/dx_4$, $b_4' = db_4/dx_4$, and

$$
u = \frac{b_4'}{b_4},\qquad v = u' = \frac{b_4''}{b_4} - u^2 .
$$

In formulas the index $i$ runs over $x_1, x_2, x_3$ and $t$ over $x_5, x_6, x_7$.

**The metric** (SPEC section 1, exactly, as changed by the user on 2026-10-14; rows and columns in the order $x_0, \dots, x_7$):

```text
g = {{Cot[6 H x0]^2,0,0,0,0,0,0,0},
     {0,E^(2 a4[x4]) Sin[6 H x0]^(1/3),0,0,0,0,0,0},
     {0,0,E^(2 a4[x4]) Sin[6 H x0]^(1/3),0,0,0,0,0},
     {0,0,0,E^(2 a4[x4]) Sin[6 H x0]^(1/3),0,0,0,0},
     {0,0,0,0,-1,0,0,0},
     {0,0,0,0,0,-E^(-2 a4[x4]) b4[x4] Sin[6 H x0]^(1/3),0,0},
     {0,0,0,0,0,0,-E^(-2 a4[x4]) b4[x4] Sin[6 H x0]^(1/3),0},
     {0,0,0,0,0,0,0,-E^(-2 a4[x4]) b4[x4] Sin[6 H x0]^(1/3)}}
```

with two functions of the time, $a_4(x_4)$ and $b_4(x_4) > 0$ (record of the change: `Revision/metric_b4/METRIC_CHANGE_PROVENANCE.md`). On the user's orders of 2026-10-15 ("b4 is a function of x4; b4 is NEVER 1"; "move everything to b4(x4); b4 is never 1") every statement of this document holds for general $a_4$ and $b_4$, and $b_4$ is never 1; a constant $b_4$ is a rescaling of $x_5, x_6, x_7$ and is excluded as well. Where a history is needed, it is the background history of SPEC section 1, $a_4 = Hx_4$, $b_4 = b_4(0)e^{(4/3)Hx_4}$ (section 11). Signature (4,4): space-like $x_0, x_1, x_2, x_3$, time-like $x_4, x_5, x_6, x_7$. The volume factor is

$$
\sqrt{|g|} = b_4^{3/2}\cos z ,
$$

so $\partial_4\sqrt{|g|} = \tfrac32u\sqrt{|g|}$: the inflation $e^{3a_4}$ of 3-space is compensated by the factor $e^{-3a_4}$ of the extra times, and the volume depends on $x_4$ through $b_4$ alone. $H = 0$ is not a metric of the family (a degenerate limit: $g_{11}, g_{55} \to 0$ and $g_{00} \to \infty$); every statement assumes $H > 0$ and $0 < z < \pi/2$.

**Spinor notation.** $\bar\Phi = \Phi^\dagger C$, $S = \bar\Phi\Phi$, $U(S)$ a real potential ($U = \tfrac{\lambda}{2}S^2$ where stated), $V = m + U'(S)$. Frame gammas are written $\gamma^{(x_a)}$, coordinate gammas $\gamma^\mu = e^\mu{}_a\gamma^{(a)}$. The theory records write $\Psi$ for both statistics; here $\Phi$ denotes the commuting field.

**Labels.** "Exact" means verified by exact symbolic computation (no floating point) in the named checks; "interpretation" marks a reading that is not itself a computed statement.

| statement | Wolfram checks | sympy checks |
| --- | --- | --- |
| the metric with $b_4$, its vielbein and $\sqrt{\lvert g\rvert} = b_4^{3/2}\cos z$ | `metric_is_the_authors`, `sqrt_det_g` | `metric_from_vielbein_equals_SPEC`, `sqrt_det_g_equals_b4_cos_z` |
| $H = 0$ is a degenerate limit | `degenerate_at_H_0` | |

## 2. The field dirac16complex00 and its symmetry group

dirac16complex00 is a field $\Phi$ with 16 complex commuting components (16 scalar fields) that transform as a Pin(4,4) spinor. It is a classical field; it is not quantised (SPEC section 6: only dirac16complex, the anticommuting field, is quantised canonically). SPEC section 3 calls it the analogue of Dirac's 1928 wave function and the author calls it semi-classical; both are interpretations, and the record shows two exact differences from Dirac's wave function: its charge $Q = \int b_4^{3/2}\cos z\,\Phi^\dagger B\Phi\,d^7x$ (locally conserved, section 7) is an indefinite form, and its classical energy is unbounded below already for $U = 0$ in the good sector (section 9).

**The gammas.** The real $16\times16$ matrices are the author's T16, rebuilt in Revision code from the author's formulas (the tau matrices and their blocks), with the frame map $\gamma^{(x_k)} = T16[k]$ for $k = 0, \dots, 7$ ($\gamma^{(x_0)}$ of the hidden direction, $\gamma^{(x_4)}$ of the time). Verified exactly:

- $\{\gamma^{(a)}, \gamma^{(b)}\} = 2\eta^{ab}$ with $\eta = \mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1)$ in the order $x_0 \ldots x_7$; every $\gamma^{(a)}$ is a real signed permutation matrix; the space-like ones are symmetric, the time-like ones antisymmetric.
- $C = \gamma^{(x_0)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)}$ is real symmetric, $C^2 = 1$, and $C\gamma^{(a)}$ is real antisymmetric for every $a$; $C = \mathrm{diag}(-\sigma, \sigma)$ with the notebook's $\sigma$.
- $\Gamma = \gamma^{(x_0)}\gamma^{(x_1)}\cdots\gamma^{(x_7)} = \mathrm{diag}(-I_8, I_8)$, $\Gamma^2 = 1$, and $\Gamma$ anticommutes with every $\gamma^{(a)}$.
- $B = -iC\gamma^{(x_4)}$ is Hermitian, $B^2 = 1$, with eigenvalues $+1$ and $-1$ eight times each: signature (8,8).
- $S^{ab} = \tfrac14[\gamma^{(a)}, \gamma^{(b)}]$ satisfy the so(4,4) relations; $(S^{ab})^T C + C S^{ab} = 0$, so $S = \bar\Phi\Phi$ is Spin(4,4)-invariant; $[\Gamma, S^{ab}] = 0$.

**Pin(4,4) and Spin(4,4).** The 16-dimensional representation is irreducible under Pin(4,4) (commutant dimension 1: the 256 Clifford products span all of $M_{16}(\mathbb{R})$). Under Spin(4,4) it splits into the two chiral halves $\Gamma = -1$ and $\Gamma = +1$, each irreducible (commutant dimension 1 on each half), and the two 8-dimensional representations are inequivalent (intertwiner dimension 0; the commutant of all $S^{ab}$ on the 16 has dimension 2, spanned by the chiral projectors). Every reflection $\gamma^{(a)}$ exchanges the halves. Pin(4,4) is the double cover of O(4,4), Spin(4,4) of SO(4,4).

**Consequence used below.** Since $C^2 = 1$ and $C = \mathrm{diag}(-\sigma, \sigma)$ is not $\pm1$, $C$ has both eigenvalues $+1$ and $-1$: the bilinear $S = \Phi^\dagger C\Phi$ is an indefinite Hermitian form and takes both signs.

| statement | Wolfram checks (algebra) | sympy checks (algebra) |
| --- | --- | --- |
| Clifford relation, reality, symmetry pattern | `Clifford_relation`, `reality`, `symmetry_pattern`, `eta_in_author_order`, `coordinate_map` | `clifford_relation`, `clifford_relation_sympy`, `reality_signed_permutations`, `symmetry_pattern` |
| $C$, $\Gamma$, $B$ | `C_real_symmetric`, `C_squared_identity`, `C_gamma_real_antisymmetric`, `Gamma_diag`, `B_Hermitian`, `B_squared_identity`, `B_signature_8_8` | `C_equals_notebook_sigma16`, `C_real_symmetric_involution`, `C_gamma_antisymmetric`, `chirality_diag`, `chirality_anticommutes`, `B_hermitian_involution_signature` |
| so(4,4), invariance of $S$ | `S_Lorentz_algebra`, `S_preserves_C`, `S_commutes_with_Gamma` | `S_lorentz_algebra`, `S_preserves_C_and_commutes_with_Gamma` |
| Pin(4,4) irreducible; Spin(4,4): two inequivalent irreducible halves | `Pin44_irreducible_commutant_dim_1`, `Spin44_commutant_dim_2_chiral_projectors`, `chiral_halves_irreducible`, `chiral_halves_inequivalent_intertwiners_0`, `Spin_Pin_reflection_swaps_halves` | `clifford_products_span_M16`, `pin_commutant_dimension_1`, `even_products_span_M8_plus_M8`, `spin_commutant_dimension_2`, `spin_halves_irreducible`, `spin_halves_inequivalent`, `reflections_exchange_halves` |
| the fixture equals the independent construction | | `fixture_comparison_gammas_json`, `gammas_json_equals_python_construction` |

## 3. Coupling to the primordial field: vielbein and canonical spin connection

**Vielbein.** The diagonal vielbein $e^a{}_\mu = f_a\delta^a_\mu$ with

$$
\begin{aligned}
& f_{x_0} = \cot z, \qquad f_{x_1} = f_{x_2} = f_{x_3} = e^{a_4}\sin^{1/6}z, \qquad f_{x_4} = 1, \\
& f_{x_5} = f_{x_6} = f_{x_7} = e^{-a_4}b_4^{1/2}\sin^{1/6}z
\end{aligned}
$$

reproduces the author's metric entry by entry, $g = e^T\eta e$, with inverse $e_a{}^\mu = \delta_a^\mu/f_a$ and $\sqrt{|g|} = f_{x_0}\cdots f_{x_7} = b_4^{3/2}\cos z$.

**Levi-Civita connection.** The 25 independent nonzero Christoffel symbols ($m \le n$) are, for $i = x_1, x_2, x_3$ and $t = x_5, x_6, x_7$ (no sum),

$$
\begin{aligned}
&\Gamma^{x_i}{}_{x_i x_4} = a_4', \qquad \Gamma^{x_i}{}_{x_i x_0} = H\cot z, \qquad \Gamma^{x_4}{}_{x_i x_i} = e^{2a_4}\sin^{1/3}z\; a_4', \\
&\Gamma^{x_0}{}_{x_i x_i} = -e^{2a_4} H\sec z\,\sin^{4/3}z, \\
&\Gamma^{x_t}{}_{x_4 x_t} = -\big(a_4' - \tfrac12u\big), \qquad \Gamma^{x_t}{}_{x_t x_0} = H\cot z, \qquad \Gamma^{x_4}{}_{x_t x_t} = e^{-2a_4}b_4\sin^{1/3}z\,\big(a_4' - \tfrac12u\big), \\
&\Gamma^{x_0}{}_{x_t x_t} = e^{-2a_4}b_4 H\sec z\,\sin^{4/3}z, \qquad \Gamma^{x_0}{}_{x_0 x_0} = -12H\csc(12Hx_0) .
\end{aligned}
$$

**Canonical spin connection.** $\omega_\mu{}^a{}_b = e^a{}_\nu(\partial_\mu e_b{}^\nu + \Gamma^\nu{}_{\mu\lambda}e_b{}^\lambda)$ satisfies the vielbein postulate $\partial_\mu e^a{}_\nu - \Gamma^\lambda{}_{\mu\nu}e^a{}_\lambda + \omega_\mu{}^a{}_b e^b{}_\nu = 0$ for all 512 components, and $\omega_{\mu ab} = \eta_{ac}\omega_\mu{}^c{}_b = -\omega_{\mu ba}$. Exactly 12 components with $a < b$ are nonzero:

$$
\begin{aligned}
& \omega_{x_i,(x_i)(x_4)} = a_4' e^{a_4}\sin^{1/6}z, \qquad \omega_{x_i,(x_i)(x_0)} = H e^{a_4}\sin^{1/6}z, \\
& \omega_{x_t,(x_4)(x_t)} = -\big(a_4' - \tfrac12u\big) e^{-a_4}b_4^{1/2}\sin^{1/6}z, \qquad \omega_{x_t,(x_t)(x_0)} = -H e^{-a_4}b_4^{1/2}\sin^{1/6}z ,
\end{aligned}
$$

and $\omega_{x_0} = \omega_{x_4} = 0$. Each component is $a_4'$, $a_4' - \tfrac12u = -\frac{d}{dx_4}\ln\big(e^{-a_4}b_4^{1/2}\big)$ or $H$ times a factor that never vanishes on the patch.

**Spinor connection and covariant derivative.** $\Omega_\mu = \tfrac12\omega_{\mu ab}S^{ab}$, a real matrix:

$$
\begin{aligned}
\Omega_{x_i} &= \tfrac12 e^{a_4}\sin^{1/6}z\,\big(a_4'\,\gamma^{(x_i)}\gamma^{(x_4)} + H\,\gamma^{(x_i)}\gamma^{(x_0)}\big), \qquad i = x_1, x_2, x_3, \\
\Omega_{x_t} &= -\tfrac12 e^{-a_4}b_4^{1/2}\sin^{1/6}z\,\big(\big(a_4' - \tfrac12u\big)\gamma^{(x_4)}\gamma^{(x_t)} + H\,\gamma^{(x_t)}\gamma^{(x_0)}\big), \qquad t = x_5, x_6, x_7, \\
\Omega_{x_0} &= \Omega_{x_4} = 0,
\end{aligned}
$$

$$
D_\mu\Phi = \partial_\mu\Phi + \Omega_\mu\Phi, \qquad D_\mu\bar\Phi = \partial_\mu\bar\Phi - \bar\Phi\,\Omega_\mu, \qquad \gamma^\mu = e^\mu{}_a\gamma^{(a)} .
$$

This is the canonical connection: it makes the gammas covariantly constant,

$$
D_\mu\gamma^\nu = \partial_\mu\gamma^\nu + \Gamma^\nu{}_{\mu\lambda}\gamma^\lambda + [\Omega_\mu, \gamma^\nu] = 0
$$

for all 64 pairs $(\mu, \nu)$. It is built from the mixed $\omega_\mu{}^a{}_b$ lowered with $\eta$ (SPEC section 3), not from a contraction of the mixed components without the metric factor.

**Curvature.** $R^\mu{}_\nu$ is diagonal except for the pair $x_4$-$x_0$, which is proportional to $b_4'$:

$$
\begin{aligned}
& R^{x_0}{}_{x_0} = -6H^2, \qquad R^{x_i}{}_{x_i} = a_4'' - 6H^2 + \tfrac32a_4'u, \qquad R^{x_4}{}_{x_4} = 6(a_4')^2 - 3a_4'u + \tfrac34u^2 + \tfrac32v, \\
& R^{x_t}{}_{x_t} = -a_4'' - 6H^2 - \tfrac32a_4'u + \tfrac34u^2 + \tfrac12v, \qquad R^{x_4}{}_{x_0} = \tfrac32Hu\cot z, \qquad R^{x_0}{}_{x_4} = -\tfrac32Hu\tan z,
\end{aligned}
$$

$$
R = 6(a_4')^2 - 3a_4'u + 3u^2 + 3v - 42H^2 .
$$

These equal the independent record of the metric change, `Revision/metric_b4/results/metric-b4.json`, compared there with the author's stored outputs. Since $R^{x_0}{}_{x_0} = -6H^2 < 0$ for every $H > 0$ and all functions $a_4$, $b_4$, the metric is curved for every member of the family, constant $a_4$ and $b_4$ included; all Riemann components vanish only in the formal limit $a_4' = a_4'' = 0$, $b_4' = b_4'' = 0$, $H = 0$ (flat 4+4), which is outside the family.

| statement | Wolfram checks (theory) | sympy checks (theory) |
| --- | --- | --- |
| vielbein and its inverse | `metric_is_the_authors`, `vielbein_inverse` | `metric_from_vielbein_equals_SPEC` |
| 25 Christoffel symbols | `christoffel_count` | `christoffel_symmetric_metric_compatible` |
| vielbein postulate, antisymmetry, the 12 components | `vielbein_postulate`, `omega_antisymmetric`, `omega_components` | `vielbein_postulate`, `spin_connection_antisymmetric` |
| $\Omega_\mu$ (real); $\Omega_{x_0} = \Omega_{x_4} = 0$ | `Omega_components` | `Omega_x0_and_Omega_x4_vanish`, `spinor_connection_real` |
| covariant constancy of the gammas | `gamma_covariantly_constant` | `covariant_constancy_D_mu_gamma_nu` |
| Ricci tensor (with the pair $x_4$-$x_0$) and scalar; curved for every $H > 0$ | `ricci_mixed_components`, `ricci_scalar`, `never_flat_for_H_positive` | `curvature_nonzero_flat_only_formally` |

## 4. The Lagrangian

The Lagrangian density (SPEC section 3; the same form as for dirac16complex, only the statistics differ):

$$
\mathcal{L} = \sqrt{|g|}\,\Big[\tfrac12\big(\bar\Phi\gamma^\mu D_\mu\Phi - (D_\mu\bar\Phi)\gamma^\mu\Phi\big) - m\,S - U(S)\Big], \qquad S = \bar\Phi\Phi = \Phi^\dagger C\Phi ,
$$

with $\sqrt{|g|} = b_4^{3/2}\cos z$, an explicit mass term linear in $m$ and quadratic in the spinor, and $U(S) = \tfrac{\lambda}{2}S^2$ where stated (a general real $U$ elsewhere). Proved exactly for the commuting field:

1. $\mathcal{L}$ is real, $\mathcal{L}^* = \mathcal{L}$: $C$ real symmetric, $C\gamma^{(a)}$ real antisymmetric and $(S^{ab})^TC + CS^{ab} = 0$ make the symmetrised kinetic term and $\bar\Phi\Phi$ real without a factor $i$ (the sympy record checks it on 408 monomials, with the control that the unsymmetrised form is not real off shell).
2. $\mathcal{L}$ differs from the unsymmetrised form by a total divergence: $\mathcal{L} = \sqrt{|g|}\,[\bar\Phi\gamma^\mu D_\mu\Phi - mS - U] - \tfrac12\partial_\mu(\sqrt{|g|}\,\bar\Phi\gamma^\mu\Phi)$.
3. For this diagonal metric $\{\gamma^\mu, \Omega_\mu\} = 0$ for each $\mu$ separately, so $\bar\Phi\{\gamma^\mu, \Omega_\mu\}\Phi = 0$ and the spin connection drops out of $\mathcal{L}$ itself (next display).

$$
\mathcal{L} = b_4^{3/2}\cos z\,\Big[\tfrac12\sum_a \frac{1}{f_a}\big(\bar\Phi\gamma^{(a)}\partial_a\Phi - \partial_a\bar\Phi\,\gamma^{(a)}\Phi\big) - m S - U(S)\Big] .
$$

The canonical spin connection reaches the field equations only through the identity

$$
\partial_\mu\big(\sqrt{|g|}\,\gamma^\mu\big) = 2\sqrt{|g|}\,\gamma^\mu\Omega_\mu
$$

in the variation of the derivative terms (section 6). Consequently the Euler-Lagrange equations of $\mathcal{L}$ are exactly those of the connection-free symmetric Lagrangian (the display above), and the surviving term is its half-density (volume and vielbein divergence) term.

**Negative control (why the Dirac-type form is used).** The notebook's real Majorana-type Lagrangian $L_g = \sqrt{|g|}\,\Theta^TC\gamma^\mu D_\mu\Theta$ with 16 real anticommuting components is a total derivative,

$$
L_g = \partial_\mu\big(\tfrac12\sqrt{|g|}\,\Theta^TC\gamma^\mu\Theta\big),
$$

and has no field equations (all Euler-Lagrange expressions vanish identically). For real commuting components the same $L_g$ is not a total derivative: it gives the massless expression $2\sqrt{|g|}\,(C\gamma^\mu D_\mu\Phi)_A$, while $\Phi^TC\gamma^\mu\Phi = 0$ identically. The Dirac-type $\mathcal{L}$ with $\bar\Phi = \Phi^\dagger C$ is used for both fields: it is real, carries the mass term, and gives the same field equation for both statistics.

| statement | Wolfram checks (theory) | sympy checks (theory) |
| --- | --- | --- |
| $\mathcal{L}$ real | `L_real_C` | `commuting_lagrangian_real`, `commuting_controls_not_vacuous` |
| total-divergence relation | `L_total_divergence_to_unsymmetrised_C` | `commuting_total_divergence_relation` |
| spin connection drops out of $\mathcal{L}$, enters through the divergence identity; same equations as the connection-free symmetric Lagrangian | `L_spin_connection_drops_out_C`, `gammaOmega_divergence_form`, `connection_free_lagrangian_same_equations` (scope) | `anticommutator_gamma_Omega_vanishes`, `divergence_of_sqrtg_gamma`, `connection_free_lagrangian_same_equations` (scope) |
| negative control: Majorana-type $L_g$ | `Majorana_Lg_total_derivative_grassmann`, `Majorana_Lg_commuting_control` | `negative_control_majorana_grassmann_total_derivative`, `negative_control_majorana_commuting_contrast` |

## 5. The exact field equations

**Covariant form.** The Euler-Lagrange equations of $\mathcal{L}$ for the commuting field (variation with respect to $\Phi^*$ and to $\Phi$) are

$$
\gamma^\mu D_\mu\Phi = \big(m + U'(S)\big)\,\Phi, \qquad (D_\mu\bar\Phi)\,\gamma^\mu = -\big(m + U'(S)\big)\,\bar\Phi ,
$$

and the second is the Dirac conjugate of the first. For $U = \tfrac{\lambda}{2}S^2$: $\gamma^\mu D_\mu\Phi = (m + \lambda S)\Phi$. (The sympy derivation includes the control that the same comparison with $m \to -m$ fails.)

**Explicit form in the primordial field** ($z = 6Hx_0$):

$$
\begin{aligned}
& e^{-a_4}\sin^{-1/6}z\,\big(\gamma^{(x_1)}\partial_1 + \gamma^{(x_2)}\partial_2 + \gamma^{(x_3)}\partial_3\big)\Phi + \gamma^{(x_4)}\partial_4\Phi \\
& \qquad + e^{a_4}b_4^{-1/2}\sin^{-1/6}z\,\big(\gamma^{(x_5)}\partial_5 + \gamma^{(x_6)}\partial_6 + \gamma^{(x_7)}\partial_7\big)\Phi \\
& \qquad + \tan z\,\gamma^{(x_0)}\partial_0\Phi + 3H\,\gamma^{(x_0)}\Phi + \tfrac34u\,\gamma^{(x_4)}\Phi = \big(m + U'(S)\big)\,\Phi ,
\end{aligned}
$$

and the adjoint equation

$$
\begin{aligned}
& e^{-a_4}\sin^{-1/6}z\,\big(\partial_1\bar\Phi\,\gamma^{(x_1)} + \partial_2\bar\Phi\,\gamma^{(x_2)} + \partial_3\bar\Phi\,\gamma^{(x_3)}\big) + \partial_4\bar\Phi\,\gamma^{(x_4)} \\
& \qquad + e^{a_4}b_4^{-1/2}\sin^{-1/6}z\,\big(\partial_5\bar\Phi\,\gamma^{(x_5)} + \partial_6\bar\Phi\,\gamma^{(x_6)} + \partial_7\bar\Phi\,\gamma^{(x_7)}\big) \\
& \qquad + \tan z\,\partial_0\bar\Phi\,\gamma^{(x_0)} + 3H\,\bar\Phi\,\gamma^{(x_0)} + \tfrac34u\,\bar\Phi\,\gamma^{(x_4)} = -\big(m + U'(S)\big)\,\bar\Phi .
\end{aligned}
$$

The derivative coefficients are $1/f_a$: the inverse 3-space scale factor $e^{-a_4}\sin^{-1/6}z$, the inverse extra-time scale factor $e^{a_4}b_4^{-1/2}\sin^{-1/6}z$ (it grows as the extra times deflate) and $\tan z$ for the hidden direction; the last two terms on the left are the spin-connection term $\gamma^\mu\Omega_\mu\Phi$.

**Evolution form.** Since $(\gamma^{(x_4)})^2 = -1$, the field equation is equivalent to the first-order evolution equation

$$
\partial_4\Phi = -\gamma^{(x_4)}\Big[\big(m + U'(S)\big)\Phi - \sum_{a \ne x_4}\frac{1}{f_a}\,\gamma^{(a)}\partial_a\Phi - 3H\,\gamma^{(x_0)}\Phi\Big] - \tfrac34u\,\Phi ;
$$

the slices $x_4 = \mathrm{const}$ are non-characteristic ($g^{44} = -1 \ne 0$), and the last term is the factor $b_4^{-3/4}$ of the solutions below.

**Chiral block form.** With $\Phi = (\varphi_-, \varphi_+)$ ($\Gamma = -1$ on rows 1-8, $\Gamma = +1$ on rows 9-16) every gamma is block off-diagonal, with $8\times8$ blocks $\bar\tau_a$ (upper right) and $\tau_a$ (lower left) listed in `Revision/theory/field-theory.json` (`field_equation_blocks`), and the field equation is the pair

$$
\begin{aligned}
& \sum_a \frac{1}{f_a}\,\bar\tau_a\,\partial_a\varphi_+ + 3H\,\bar\tau_{x_0}\varphi_+ + \tfrac34u\,\bar\tau_{x_4}\varphi_+ = V\varphi_-, \\
& \sum_a \frac{1}{f_a}\,\tau_a\,\partial_a\varphi_- + 3H\,\tau_{x_0}\varphi_- + \tfrac34u\,\tau_{x_4}\varphi_- = V\varphi_+ .
\end{aligned}
$$

The mass term and the gravitational terms couple the two chiral halves.

**The 16 component equations.** With $\epsilon_s = e^{-a_4}\sin^{-1/6}z$, $\epsilon_t = e^{a_4}b_4^{-1/2}\sin^{-1/6}z$, $t = \tan z$, $\hat\partial_4 = \partial_4 + \tfrac34u$, $V = m + U'(S)$ and $\Phi_A$ the components in the row order of `Revision/algebra/gammas.json`, the equation $(\gamma^\mu D_\mu\Phi)_A = V\Phi_A$ reads (generated from `field_equation_components` of `Revision/theory/field-theory.json`, which the sympy record compares term by term; the $b_4$ term of the spin connection enters every component with the matrix $\gamma^{(x_4)}$, on the same component and with the same sign as $\partial_4$, hence $\hat\partial_4$):

$$
\begin{aligned}
(1)\;\; & -\hat\partial_4\Phi_{14} + \epsilon_s\,(-\partial_1\Phi_{16} + \partial_2\Phi_{15} - \partial_3\Phi_{14}) \\
& + \epsilon_t\,(\partial_5\Phi_{15} + \partial_6\Phi_{16} + \partial_7\Phi_{9}) + (t\,\partial_0 + 3H)\,\Phi_{9} = V\,\Phi_{1} \\
(2)\;\; & \hat\partial_4\Phi_{13} + \epsilon_s\,(-\partial_1\Phi_{15} - \partial_2\Phi_{16} + \partial_3\Phi_{13}) \\
& + \epsilon_t\,(\partial_5\Phi_{16} - \partial_6\Phi_{15} + \partial_7\Phi_{10}) + (t\,\partial_0 + 3H)\,\Phi_{10} = V\,\Phi_{2} \\
(3)\;\; & \hat\partial_4\Phi_{16} + \epsilon_s\,(\partial_1\Phi_{14} - \partial_2\Phi_{13} - \partial_3\Phi_{16}) \\
& + \epsilon_t\,(-\partial_5\Phi_{13} + \partial_6\Phi_{14} + \partial_7\Phi_{11}) + (t\,\partial_0 + 3H)\,\Phi_{11} = V\,\Phi_{3} \\
(4)\;\; & -\hat\partial_4\Phi_{15} + \epsilon_s\,(\partial_1\Phi_{13} + \partial_2\Phi_{14} + \partial_3\Phi_{15}) \\
& + \epsilon_t\,(-\partial_5\Phi_{14} - \partial_6\Phi_{13} + \partial_7\Phi_{12}) + (t\,\partial_0 + 3H)\,\Phi_{12} = V\,\Phi_{4}
\end{aligned}
$$

$$
\begin{aligned}
(5)\;\; & \hat\partial_4\Phi_{10} + \epsilon_s\,(-\partial_1\Phi_{12} + \partial_2\Phi_{11} - \partial_3\Phi_{10}) \\
& + \epsilon_t\,(-\partial_5\Phi_{11} - \partial_6\Phi_{12} - \partial_7\Phi_{13}) + (t\,\partial_0 + 3H)\,\Phi_{13} = V\,\Phi_{5} \\
(6)\;\; & -\hat\partial_4\Phi_{9} + \epsilon_s\,(-\partial_1\Phi_{11} - \partial_2\Phi_{12} + \partial_3\Phi_{9}) \\
& + \epsilon_t\,(-\partial_5\Phi_{12} + \partial_6\Phi_{11} - \partial_7\Phi_{14}) + (t\,\partial_0 + 3H)\,\Phi_{14} = V\,\Phi_{6} \\
(7)\;\; & -\hat\partial_4\Phi_{12} + \epsilon_s\,(\partial_1\Phi_{10} - \partial_2\Phi_{9} - \partial_3\Phi_{12}) \\
& + \epsilon_t\,(\partial_5\Phi_{9} - \partial_6\Phi_{10} - \partial_7\Phi_{15}) + (t\,\partial_0 + 3H)\,\Phi_{15} = V\,\Phi_{7} \\
(8)\;\; & \hat\partial_4\Phi_{11} + \epsilon_s\,(\partial_1\Phi_{9} + \partial_2\Phi_{10} + \partial_3\Phi_{11}) \\
& + \epsilon_t\,(\partial_5\Phi_{10} + \partial_6\Phi_{9} - \partial_7\Phi_{16}) + (t\,\partial_0 + 3H)\,\Phi_{16} = V\,\Phi_{8}
\end{aligned}
$$

$$
\begin{aligned}
(9)\;\; & \hat\partial_4\Phi_{6} + \epsilon_s\,(\partial_1\Phi_{8} - \partial_2\Phi_{7} + \partial_3\Phi_{6}) \\
& + \epsilon_t\,(-\partial_5\Phi_{7} - \partial_6\Phi_{8} - \partial_7\Phi_{1}) + (t\,\partial_0 + 3H)\,\Phi_{1} = V\,\Phi_{9} \\
(10)\;\; & -\hat\partial_4\Phi_{5} + \epsilon_s\,(\partial_1\Phi_{7} + \partial_2\Phi_{8} - \partial_3\Phi_{5}) \\
& + \epsilon_t\,(-\partial_5\Phi_{8} + \partial_6\Phi_{7} - \partial_7\Phi_{2}) + (t\,\partial_0 + 3H)\,\Phi_{2} = V\,\Phi_{10} \\
(11)\;\; & -\hat\partial_4\Phi_{8} + \epsilon_s\,(-\partial_1\Phi_{6} + \partial_2\Phi_{5} + \partial_3\Phi_{8}) \\
& + \epsilon_t\,(\partial_5\Phi_{5} - \partial_6\Phi_{6} - \partial_7\Phi_{3}) + (t\,\partial_0 + 3H)\,\Phi_{3} = V\,\Phi_{11} \\
(12)\;\; & \hat\partial_4\Phi_{7} + \epsilon_s\,(-\partial_1\Phi_{5} - \partial_2\Phi_{6} - \partial_3\Phi_{7}) \\
& + \epsilon_t\,(\partial_5\Phi_{6} + \partial_6\Phi_{5} - \partial_7\Phi_{4}) + (t\,\partial_0 + 3H)\,\Phi_{4} = V\,\Phi_{12}
\end{aligned}
$$

$$
\begin{aligned}
(13)\;\; & -\hat\partial_4\Phi_{2} + \epsilon_s\,(\partial_1\Phi_{4} - \partial_2\Phi_{3} + \partial_3\Phi_{2}) \\
& + \epsilon_t\,(\partial_5\Phi_{3} + \partial_6\Phi_{4} + \partial_7\Phi_{5}) + (t\,\partial_0 + 3H)\,\Phi_{5} = V\,\Phi_{13} \\
(14)\;\; & \hat\partial_4\Phi_{1} + \epsilon_s\,(\partial_1\Phi_{3} + \partial_2\Phi_{4} - \partial_3\Phi_{1}) \\
& + \epsilon_t\,(\partial_5\Phi_{4} - \partial_6\Phi_{3} + \partial_7\Phi_{6}) + (t\,\partial_0 + 3H)\,\Phi_{6} = V\,\Phi_{14} \\
(15)\;\; & \hat\partial_4\Phi_{4} + \epsilon_s\,(-\partial_1\Phi_{2} + \partial_2\Phi_{1} + \partial_3\Phi_{4}) \\
& + \epsilon_t\,(-\partial_5\Phi_{1} + \partial_6\Phi_{2} + \partial_7\Phi_{7}) + (t\,\partial_0 + 3H)\,\Phi_{7} = V\,\Phi_{15} \\
(16)\;\; & -\hat\partial_4\Phi_{3} + \epsilon_s\,(-\partial_1\Phi_{1} - \partial_2\Phi_{2} - \partial_3\Phi_{3}) \\
& + \epsilon_t\,(-\partial_5\Phi_{2} - \partial_6\Phi_{1} + \partial_7\Phi_{8}) + (t\,\partial_0 + 3H)\,\Phi_{8} = V\,\Phi_{16}
\end{aligned}
$$

In every component the gravitational term $3H\,\Phi_B$ appears next to the hidden-direction derivative $\tan z\,\partial_0\Phi_B$ of the same component $B$ ($\gamma^{(x_0)}$ is a permutation matrix with entries $+1$).

**Exact solutions used as test points.** They satisfy the field equation for all functions $a_4$ and $b_4$.

- $U = 0$: $\Phi = b_4^{-3/4}\sin^{\alpha}z\,\big(\cosh(kx_4) + \tfrac{\sinh(kx_4)}{k}M\big)\chi$ with constant $\chi$ (16 free complex constants), $M = -m\gamma^{(x_4)} + 3H(2\alpha + 1)\gamma^{(x_4)}\gamma^{(x_0)}$, $k^2 = 9H^2(2\alpha+1)^2 - m^2$ and $\alpha$ arbitrary; $M^2 = k^2$ and $M^TC + CM = 0$, and the factor $b_4^{-3/4}$ compensates the term $\tfrac34u\,\gamma^{(x_4)}$. Honest scope: at these solutions the pressures and the momentum density vanish and $\rho = mS$ with $S = b_4^{-3/2}S_\chi$, so they test the terms $\tan z\,\gamma^{(x_0)}\partial_0$, $3H\gamma^{(x_0)}$ and $\tfrac34u\,\gamma^{(x_4)}$ but are a weak test of conservation; the general proof of conservation is the Noether identity of section 7.
- $U = \tfrac{\lambda}{2}S^2$, homogeneous (nonlinear): for every solution $\chi(x_4)$ of the linear system $\chi' = M\chi$, $M = -(m + \lambda b_4^{-3/2}S_0)\gamma^{(x_4)} + 3H\gamma^{(x_4)}\gamma^{(x_0)}$ with $S_0 = \chi(0)^\dagger C\chi(0)$, the field $\Phi = b_4^{-3/4}\chi$ solves the field equation; $M^TC + CM = 0$, so $\chi^\dagger C\chi = S_0$ for all $x_4$ and $S = b_4^{-3/2}S_0$; $\nabla_\mu T^\mu{}_\nu = 0$ for all $\nu$, and $\rho = mS + \lambda S^2/2$, $p = \lambda S^2/2$. For $b_4$ not constant the effective mass $m + \lambda b_4^{-3/2}S_0$ depends on $x_4$, and there is no closed form in general.

| statement | Wolfram checks (theory) | sympy checks (theory) |
| --- | --- | --- |
| Euler-Lagrange equations derived from $\mathcal{L}$ | `EL_Psibar_C`, `EL_Psi_C` | `commuting_euler_lagrange_psibar_variation`, `commuting_euler_lagrange_psi_variation` |
| the adjoint equation is the Dirac conjugate | `adjoint_equation_is_Dirac_conjugate_C` | `commuting_adjoint_equation_is_conjugate` |
| explicit form, 16 components, chiral blocks | `Dirac_operator_explicit_C`, `block_form` | `commuting_euler_lagrange_psibar_variation` (the sympy field equation), compared term by term with `field_equation_components` and entry by entry with `field_equation_blocks` in the comparison record (section `comparison_with_wolfram` of the sympy report: 33 of 33 formula records and 65 of 65 check pairs agree) |
| evolution form | `evolution_form_C` | `hamiltonian_form_and_heisenberg_equation` |
| exact solutions | `solution_matrix_square`, `exact_solution_x4_x0_C`, `exact_solution_nonlinear_homogeneous_C` | `exact_solution_family_x4_x0`, `exact_nonlinear_homogeneous_solution` |

## 6. Non-triviality [2]: theorem and proof

The author's requirement [2]: the Lagrangian of dirac16complex00 must be non-trivial, i.e. its Euler-Lagrange equations always possess nonzero contributions from gravity through the canonical spin connection unless the spacetime is flat 4+4, and they must be self-consistent, checked and verified.

**Theorem (NON-TRIVIALITY [2]).** Hypotheses: the author's metric of section 1 with $H > 0$ and $0 < z < \pi/2$; $a_4$ and $b_4 > 0$ any differentiable functions of $x_4$ (constant ones included); the diagonal vielbein of section 3 and its canonical spin connection; $\Phi$ the commuting 16-component field with the Lagrangian of section 4 and any real potential $U$. Then statements (1) to (4) hold. Statements (1) and (2) concern the diagonal vielbein and the field variables $\Phi$; statements (3) and (4) are the frame-independent content (see "Scope of [2]" below).

**(1) The gravitational term of the field equation.** The spin-connection part of the Euler-Lagrange operator is

$$
\gamma^\mu D_\mu\Phi - \gamma^\mu\partial_\mu\Phi = \gamma^\mu\Omega_\mu\,\Phi, \qquad \gamma^\mu\Omega_\mu = 3H\,\gamma^{(x_0)} + \tfrac34u\,\gamma^{(x_4)} ,
$$

a matrix independent of $a_4$ and $x_0$, never zero for $H > 0$ (its $\gamma^{(x_0)}$ coefficient is $3H$). Since $\gamma^{(x_0)}$ and $\gamma^{(x_4)}$ anticommute, with squares $+1$ and $-1$,

$$
\big(\gamma^\mu\Omega_\mu\big)^2 = \big(9H^2 - \tfrac{9}{16}u^2\big)\,I_{16} ,
$$

so the term is nonzero for every $\Phi \ne 0$ wherever $u^2 \ne 16H^2$ (on the background history $u = \tfrac43H$ and the square is $8H^2I_{16}$); where $|u| = 4H$ the matrix is $3H(\gamma^{(x_0)} \pm \gamma^{(x_4)})$, of rank 8, and annihilates an 8-dimensional subspace.

**(2) What cancels and what survives.** Per direction (no sum)

$$
\begin{aligned}
\gamma^{x_i}\Omega_{x_i} &= \tfrac{a_4'}{2}\,\gamma^{(x_4)} + \tfrac{H}{2}\,\gamma^{(x_0)} \qquad (i = x_1, x_2, x_3), \\
\gamma^{x_t}\Omega_{x_t} &= \big(-\tfrac{a_4'}{2} + \tfrac{u}{4}\big)\,\gamma^{(x_4)} + \tfrac{H}{2}\,\gamma^{(x_0)} \qquad (t = x_5, x_6, x_7),
\end{aligned}
$$

and $\gamma^{x_0}\Omega_{x_0} = \gamma^{x_4}\Omega_{x_4} = 0$. The $a_4'$ terms of the time direction ($\gamma^{(x_4)}$) of the 3 inflating and the 3 deflating directions cancel exactly, $3a_4'/2 - 3a_4'/2 = 0$; the $b_4'$ terms of the 3 extra times add, $3 \cdot u/4 = \tfrac34u$; the hidden-direction ($\gamma^{(x_0)}$) terms of all six directions add, $6 \cdot H/2 = 3H$.

**(3) It vanishes only in flat 4+4 space.** $\Omega_\mu = 0$ for all $\mu$ if and only if $a_4' = 0$, $b_4' = 0$ and $H = 0$; $H = 0$ is a degenerate limit outside the family, so for every admissible metric the spin connection is nonzero. No choice of frame removes it: $[D_\mu, D_\nu] = \tfrac12 R_{ab\mu\nu}S^{ab}$ and $R^{x_0}{}_{x_0} = -6H^2 \ne 0$.

**(4) The vielbein in every derivative term.** Gravity also enters every derivative term,

$$
\gamma^\mu\partial_\mu = e^{-a_4}\sin^{-1/6}z\,\gamma^{(x_i)}\partial_i + \gamma^{(x_4)}\partial_4 + e^{a_4}b_4^{-1/2}\sin^{-1/6}z\,\gamma^{(x_t)}\partial_t + \tan z\,\gamma^{(x_0)}\partial_0
$$

(sums over $i$ and $t$), none of the factors being identically 1; $a_4$ enters the field equation only through these factors (its spin-connection terms cancel by (2)), and $b_4$ through $b_4^{-1/2}$ and through $\tfrac34u\,\gamma^{(x_4)}$.

**Proof.** Step (a), the inflating directions $i = x_1, x_2, x_3$: by section 3

$$
\gamma^{x_i} = e^{-a_4}\sin^{-1/6}z\,\gamma^{(x_i)}, \qquad \Omega_{x_i} = \tfrac12 e^{a_4}\sin^{1/6}z\,\big(a_4'\gamma^{(x_i)}\gamma^{(x_4)} + H\gamma^{(x_i)}\gamma^{(x_0)}\big) .
$$

The scale factors cancel and $(\gamma^{(x_i)})^2 = \eta^{ii} = +1$, so $\gamma^{x_i}\Omega_{x_i} = \tfrac12(a_4'\gamma^{(x_4)} + H\gamma^{(x_0)})$.

Step (b), the deflating extra times $t = x_5, x_6, x_7$:

$$
\gamma^{x_t} = e^{a_4}b_4^{-1/2}\sin^{-1/6}z\,\gamma^{(x_t)}, \qquad \Omega_{x_t} = -\tfrac12 e^{-a_4}b_4^{1/2}\sin^{1/6}z\,\big(\big(a_4' - \tfrac12u\big)\gamma^{(x_4)}\gamma^{(x_t)} + H\gamma^{(x_t)}\gamma^{(x_0)}\big) .
$$

The scale factors cancel; with $\gamma^{(x_t)}\gamma^{(x_4)}\gamma^{(x_t)} = -\gamma^{(x_4)}(\gamma^{(x_t)})^2 = \gamma^{(x_4)}$ and $(\gamma^{(x_t)})^2 = -1$ this gives $\gamma^{x_t}\Omega_{x_t} = -\tfrac12\big((a_4' - \tfrac12u)\gamma^{(x_4)} - H\gamma^{(x_0)}\big)$.

Step (c): $\Omega_{x_0} = \Omega_{x_4} = 0$. Summing (a), (b) and (c) gives statements (1) and (2). Equivalently, since $\{\gamma^\mu, \Omega_\mu\} = 0$ for each $\mu$,

$$
\gamma^\mu\Omega_\mu = \frac{1}{2\sqrt{|g|}}\,\partial_\mu\big(\sqrt{|g|}\,e_a{}^\mu\big)\gamma^{(a)} ;
$$

only $\mu = x_0$ and $\mu = x_4$ contribute, with $\sqrt{|g|}\,e_{x_0}{}^{x_0} = b_4^{3/2}\cos z\tan z = b_4^{3/2}\sin z$ and $e_{x_4}{}^{x_4} = 1$:

$$
\frac{1}{2b_4^{3/2}\cos z}\,\partial_0\big(b_4^{3/2}\sin z\big) = 3H, \qquad \frac{1}{2\sqrt{|g|}}\,\partial_4\sqrt{|g|} = \tfrac34u .
$$

The square of statement (1) follows from $\{\gamma^{(x_0)}, \gamma^{(x_4)}\} = 0$.

Step (d): each of the 12 nonzero $\omega_{\mu ab}$ is $a_4'$, $a_4' - \tfrac12u$ or $H$ times $\pm e^{\pm a_4}\sin^{1/6}z$ or $\pm e^{-a_4}b_4^{1/2}\sin^{1/6}z$, never zero on the patch, and the $S^{ab}$ are linearly independent; the $x_4$-parts vanish if and only if $a_4$ and $e^{-a_4}b_4^{1/2}$ are constant, that is $a_4' = b_4' = 0$; this gives statement (3), with the curvature statement from the integrability identity and the Ricci components of section 3.

Step (e): statement (4) is the explicit form of section 5. Every step is verified exactly, for the author's T16 and, in the field-equations record, also for a second, independently built Clifford representation. $\square$

**What survives and what cancels, in words.** The three inflating directions contribute $+\tfrac{a_4'}{2}\gamma^{(x_4)}$ each and the three deflating extra times $\big(-\tfrac{a_4'}{2} + \tfrac{u}{4}\big)\gamma^{(x_4)}$ each: the $a_4'$ terms cancel exactly, the $b_4'$ terms remain. In sum the $\gamma^{(x_4)}$ coefficient is half the logarithmic rate of the 7-volume, $\tfrac12\,\partial_4\ln\sqrt{|g|} = \tfrac34u$: the factors $e^{\pm 3a_4}$ compensate in the volume, $b_4^{3/2}$ does not. The warp $\sin^{1/6}z$ of the six directions along the hidden direction gives $+\tfrac{H}{2}\gamma^{(x_0)}$ for each of them and survives as $3H\gamma^{(x_0)}$.

**Scope of [2] (exact).** The value $\gamma^\mu\Omega_\mu = 3H\gamma^{(x_0)} + \tfrac34u\,\gamma^{(x_4)}$ belongs to the diagonal vielbein and to the field variables $\Phi$:

- In another admissible vielbein of the same metric, the frame boosted in the $(x_0, x_4)$ plane, $e'^{(x_4)} = \cosh b\,e^{(x_4)} + \sinh b\,e^{(x_0)}$, $e'^{(x_0)} = \sinh b\,e^{(x_4)} + \cosh b\,e^{(x_0)}$ with rapidity $b = c\,x_4 + b_0$, its canonical connection gives $\gamma'^\mu\Omega'_\mu = \tfrac{6H - c}{2}(\cosh b\,\gamma^{(x_0)} - \sinh b\,\gamma^{(x_4)}) + \tfrac34u\,(\cosh b\,\gamma^{(x_4)} - \sinh b\,\gamma^{(x_0)})$. For $c = 6H$ the $H$ part vanishes identically, for every $H > 0$, $a_4$ and $b_4$; for any rapidity function the coefficients satisfy $\cosh b\,c_4 + \sinh b\,c_0 = \tfrac34u$, so no boost in this plane removes the term unless $b_4' = 0$.
- Within the diagonal frame the rescaling $\Phi = b_4^{-3/4}\sin^{-1/2}z\,\chi$ removes the term exactly: $\gamma^\mu D_\mu\Phi = b_4^{-3/4}\sin^{-1/2}z\,\gamma^\mu\partial_\mu\chi$, so for $U = 0$ the equation for $\chi$ has no spin-connection term, and for $U = \tfrac{\lambda}{2}S^2$ the term becomes the $x_0$- and $x_4$-dependent coupling $\lambda S[\chi]/(b_4^{3/2}\sin z)$. The exact family of section 5 shows this: $\alpha = -\tfrac12$ gives $M = -m\gamma^{(x_4)}$ with no $H$ term.
- The canonical connection drops out of $\mathcal{L}$ (section 4), so the Euler-Lagrange equations are those of the connection-free symmetric Lagrangian; the deflation $a_4$ contributes nothing to $\gamma^\mu\Omega_\mu$ although the $a_4$ sector is curved ($R^{x_4}{}_{x_4} = 6(a_4')^2 - 3a_4'u + \tfrac34u^2 + \tfrac32v$), while $b_4$ enters also through $\tfrac34u\,\gamma^{(x_4)}$.
- What cannot be removed in any frame is $\Omega_\mu$ itself (its curvature is the Riemann tensor, $R^{x_0}{}_{x_0} = -6H^2$), together with the frame factors $e^{\mp a_4}\sin^{-1/6}z$, $e^{a_4}b_4^{-1/2}\sin^{-1/6}z$ and $\tan z$ of the derivative terms: this is the frame-independent content of [2]. In the diagonal frame the connection also enters the energy-momentum tensor (for a homogeneous configuration $K^{x_4}{}_{x_1}$ contains $\tfrac12 e^{a_4}\sin^{1/6}z\,H\,\bar\Phi\gamma^{(x_4)}\gamma^{(x_1)}\gamma^{(x_0)}\Phi$).
- Interpretation (labelled): in the quantum theory of dirac16complex the term $3H\gamma^{(x_0)}$ makes the hidden-direction operator antisymmetric for the measure $\cos z\,dx_0$ in the variables $\Psi$, up to a boundary term that does not vanish at $z = \pi/2$, and the term $\tfrac34u\,\gamma^{(x_4)}$ compensates the $x_4$ dependence of the measure $b_4^{3/2}$; in the variables $\chi$ with the measure $dy = \cot z\,dx_0$ no such term is needed. This role therefore depends on the variables and the measure.

| statement | Wolfram checks | sympy checks |
| --- | --- | --- |
| (1) $\gamma^\mu\Omega_\mu = 3H\gamma^{(x_0)} + \tfrac34u\,\gamma^{(x_4)}$ and its square | `nontriviality_2_dirac16complex00`, `gammaOmega_total` (theory); `gravity_term_gamma_mu_Omega_mu` ($a_4$ record) | `gamma_mu_Omega_mu_equals_3H_gamma_x0_plus_b4_term`, `gravity_term_square` (theory); `ownrep_gravity_term`, `authorT16_gravity_term` ($a_4$ record) |
| (2) the $a_4'$ terms cancel, the $b_4'$ and $x_0$ terms add | `gammaOmega_per_direction`, `gammaOmega_divergence_form` | `a4_time_terms_cancel_b4_terms_add`, `divergence_of_sqrtg_gamma` |
| (3) $\Omega_\mu = 0$ only for $a_4' = b_4' = 0$ and $H = 0$; never flat | `Omega_vanishes_iff_a4prime_b4prime_and_H_vanish`, `never_flat_for_H_positive`, `spin_curvature_equals_Riemann` | `nontriviality_Omega_zero_iff_flat`, `curvature_nonzero_flat_only_formally`, `spinor_curvature_equals_riemann` |
| (4) explicit operator | `Dirac_operator_explicit_C` | |
| the same terms in the quantum theory of dirac16complex (up to a boundary term) | `good_sector_hermiticity_curved`, `good_sector_hermiticity_up_to_the_brane_flux` (scope) | `good_sector_hermiticity_up_to_the_brane_flux` (scope) |
| scope: the boosted frame removes the $H$ part of $\gamma^\mu\Omega_\mu$, not its $b_4'$ part and not $\Omega_\mu$ | `boosted_frame_reproduces_metric`, `boosted_frame_canonical_connection`, `boosted_frame_gammaOmega_formula`, `boosted_frame_removes_only_the_H_term`, `boosted_frame_curvature_nonzero` (scope) | the same five names (scope) |
| scope: rescaling, deflation, energy-momentum tensor | `rescaling_removes_the_connection_term`, `rescaled_equation_quadratic_potential`, `gammaOmega_blind_to_the_deflation`, `spin_connection_in_the_energy_momentum_tensor` (scope) | the same four names (scope) |

## 7. Self-consistency of the field equations

All statements are exact and verified for the commuting field, for general $a_4$ and $b_4$.

**Reality and derivation.** $\mathcal{L}$ is real; the Euler-Lagrange equations derived from it are the field equation and its Dirac conjugate (sections 4 and 5).

**Integrability of the connection.** For all 28 pairs,

$$
[D_\mu, D_\nu]\Phi = \big(\partial_\mu\Omega_\nu - \partial_\nu\Omega_\mu + [\Omega_\mu, \Omega_\nu]\big)\Phi = \tfrac12 R_{ab\mu\nu}S^{ab}\Phi .
$$

**Second-order consistency (Lichnerowicz identity).** Identically for a general field,

$$
(\gamma^\mu D_\mu)^2\Phi = g^{\mu\nu}\big(D_\mu D_\nu - \Gamma^\lambda{}_{\mu\nu}D_\lambda\big)\Phi - \frac{R}{4}\,\Phi, \qquad R = 6(a_4')^2 - 3a_4'u + 3u^2 + 3v - 42H^2,
$$

and $\gamma^\mu\gamma^\nu F_{\mu\nu} = -\tfrac{R}{2}$ for the spinor curvature $F_{\mu\nu} = [D_\mu, D_\nu]$.

**Cauchy problem.** The equation is first order in $x_4$ with non-characteristic slices (evolution form, section 5). This does not make the Cauchy problem well posed, and it is not listed here as a self-consistency property: for data that depend on the extra times the growth rates of the modes have no upper bound (with frozen coefficients $k_5 = K$ gives the rate $\sqrt{K^2 - m^2 - k_0^2 - k_1^2 - k_2^2 - k_3^2}$; Hadamard ill-posedness), and in the good sector, without a boundary condition at $z = \pi/2$, the $x_0$-independent modes grow whenever $m^2 < 9H^2$ (for $U = 0$; on these modes $\Phi = b_4^{-3/4}\chi$, and the matrix $-im\gamma^{(x_4)} + 3iH\gamma^{(x_4)}\gamma^{(x_0)}$ of the evolution of $\chi$ has the square $(m^2 - 9H^2)I_{16}$).

**Conserved current.** $J^\mu = -i\bar\Phi\gamma^\mu\Phi$ is real, and off shell

$$
\partial_\mu\big(\sqrt{|g|}\,J^\mu\big) = -i\sqrt{|g|}\,\big(\bar E\Phi + \bar\Phi E\big),\qquad \sqrt{|g|} = b_4^{3/2}\cos z,
$$

with $E = \gamma^\mu D_\mu\Phi - (m + U'(S))\Phi$ and $\bar E = (D_\mu\bar\Phi)\gamma^\mu + (m + U'(S))\bar\Phi$ (the convention of the Wolfram record), so $\nabla_\mu J^\mu = 0$ on shell. The charge density is $J^{x_4} = \Phi^\dagger B\Phi$, and the charge of a slice of constant $x_4$, $Q = \int b_4^{3/2}\cos z\,\Phi^\dagger B\Phi\,d^7x$, is an indefinite form ($B$ has signature (8,8)). Only the local law is established: $Q$ is constant in $x_4$ only if no charge flows through the boundary of the slice, and at the brane $z = \pi/2$ the flow is not zero in general (`good_sector_hermiticity_up_to_the_brane_flux`, both engines; the lead's independent record `Revision/lead_checks/reports/charge-conjugation-and-u1.json` states the same for the current of dirac16complex, for general $a_4$ and $b_4$). This record imposes no boundary condition at $z = \pi/2$ (section 15).

**Bianchi-type identity of the energy-momentum tensor.** The off-shell Noether identity of diffeomorphism invariance (for general $a_4$ and $b_4$),

$$
\partial_\mu\big(\sqrt{|g|}\,T^\mu{}_\lambda\big) - \sqrt{|g|}\,T^\mu{}_a\,\partial_\lambda e^a{}_\mu = \sum_\phi \mathrm{EL}_\phi\,\partial_\lambda\phi \qquad (\lambda = x_0, \ldots, x_7),
$$

and the off-shell identity of local Lorentz invariance (the antisymmetric part of $T$ is a combination of the Euler-Lagrange expressions $\mathrm{EL}_\phi$) give: on shell $T$ is symmetric and $\nabla_\mu T^\mu{}_\nu = 0$, exactly, for general solutions.

**Gravity side.** Each Lovelock tensor is divergence-free, $\nabla_\mu E_{(k)}{}^\mu{}_\nu = 0$, and the constraint is propagated by the other components (section 11).

**Test points.** The exact solutions of section 5 satisfy the field equation, current conservation and $\nabla_\mu T^\mu{}_\nu = 0$ exactly.

| statement | Wolfram checks (theory) | sympy checks (theory) |
| --- | --- | --- |
| integrability $[D_\mu, D_\nu] = \tfrac12 R_{ab\mu\nu}S^{ab}$ | `spin_curvature_equals_Riemann` | `spinor_curvature_equals_riemann` |
| Lichnerowicz identity | `Lichnerowicz_identity_C` | `lichnerowicz_identity_on_fields`, `lichnerowicz_contraction` |
| current: reality, conservation, indefinite charge | `current_real_C`, `current_conservation_identity_C`, `charge_density_is_Krein_form_C` | `commuting_current_conservation` |
| Noether identities and conservation of $T$ | `Noether_identity_diffeomorphisms_C`, `Noether_identity_local_Lorentz_C`, `conservation_on_shell_general` | `commuting_emt_conservation_on_shell`, `commuting_emt_conservation_negative_control` |
| no well-posed Cauchy problem: unbounded growth, growing good-sector modes without a boundary condition | `extra_time_growth_rates_unbounded`, `good_sector_x0_independent_modes_without_boundary_condition` (scope) | the same two names (scope) |

## 8. The energy-momentum tensor (classical bilinears)

For dirac16complex00 the energy-momentum tensor is the classical bilinear (a c-number function of $\Phi$; no operator ordering, no normal ordering).

**Definition and closed form.** $T^\nu{}_\mu = e^b{}_\mu\,\tfrac{1}{\sqrt{|g|}}\,\delta S_{\mathrm{act}}/\delta e^b{}_\nu$ (exact first-order variation of $\sqrt{|g|}$, $\gamma^\mu$ and the spin connection; $S_{\mathrm{act}}$ the action) equals, for all 64 components and general $a_4$ and $b_4$,

$$
T^\nu{}_\mu = \delta^\nu_\mu\,L_0 - \tfrac12\big(\bar\Phi\gamma^\nu D_\mu\Phi - D_\mu\bar\Phi\,\gamma^\nu\Phi\big) - \tfrac14\,g_{\mu\rho}\nabla_\lambda\big(\bar\Phi\{\gamma^\lambda, \Sigma^{\nu\rho}\}\Phi\big), \qquad \Sigma^{\nu\rho} = \tfrac14[\gamma^\nu, \gamma^\rho],
$$

with $L_0 = \mathcal{L}/\sqrt{|g|}$; the last term (the totally antisymmetric spin density) comes from the variation of the spin connection. Its symmetric part is the Belinfante tensor

$$
T^\nu{}_\mu = \delta^\nu_\mu\,L_0 - \tfrac14\big(\bar\Phi\gamma^\nu D_\mu\Phi - D_\mu\bar\Phi\,\gamma^\nu\Phi + \bar\Phi\gamma_\mu D^\nu\Phi - D^\nu\bar\Phi\,\gamma_\mu\Phi\big),
$$

and on shell the variation tensor is symmetric and equals it (section 7; independently, with all 64 components of a first-order vielbein variation around the author's metric, the variation tensor equals the Belinfante tensor on shell for 64 of 64 components). The normalisation is $\delta S_{\mathrm{act}} = \tfrac12\int\sqrt{|g|}\,T^{\mu\nu}\delta g_{\mu\nu}$.

**Sign convention.** The energy density is $\rho = -T^{x_4}{}_{x_4}$ and the pressures are $p_\mu = T^\mu{}_\mu$ (no sum) for the space-like and the extra-time directions:

$$
\rho = -T^{x_4}{}_{x_4}, \qquad p_3 = T^{x_1}{}_{x_1}, \qquad p_t = T^{x_5}{}_{x_5}, \qquad p_0 = T^{x_0}{}_{x_0} .
$$

**Diagonal components in the primordial field.** With the kinetic term of direction $\mu$ (no sum)

$$
K_\mu = \frac{1}{2f_\mu}\big(\bar\Phi\gamma^{(\mu)}\partial_\mu\Phi - \partial_\mu\bar\Phi\,\gamma^{(\mu)}\Phi\big),
$$

that is

$$
\begin{aligned}
K_{x_i} &= \tfrac12 e^{-a_4}\sin^{-1/6}z\,\big(\bar\Phi\gamma^{(x_i)}\partial_i\Phi - \partial_i\bar\Phi\,\gamma^{(x_i)}\Phi\big), \qquad K_{x_4} = \tfrac12\big(\bar\Phi\gamma^{(x_4)}\partial_4\Phi - \partial_4\bar\Phi\,\gamma^{(x_4)}\Phi\big), \\
K_{x_t} &= \tfrac12 e^{a_4}b_4^{-1/2}\sin^{-1/6}z\,\big(\bar\Phi\gamma^{(x_t)}\partial_t\Phi - \partial_t\bar\Phi\,\gamma^{(x_t)}\Phi\big), \qquad K_{x_0} = \tfrac12\tan z\,\big(\bar\Phi\gamma^{(x_0)}\partial_0\Phi - \partial_0\bar\Phi\,\gamma^{(x_0)}\Phi\big),
\end{aligned}
$$

one has

$$
L_0 = \sum_\mu K_\mu - mS - U(S), \qquad T^\mu{}_\mu = L_0 - K_\mu \;\;(\text{no sum}) .
$$

No spin-connection term survives in the diagonal components ($\{\gamma^\mu, \Omega_\mu\} = 0$), and the variation tensor and the Belinfante tensor agree on the diagonal off shell. Hence, for every configuration (off shell),

$$
\begin{aligned}
\rho &= -\sum_{\mu \ne x_4} K_\mu + mS + U(S), \\
p_3 &= \sum_{\mu \ne x_1} K_\mu - mS - U(S) \quad (= T^{x_2}{}_{x_2} = T^{x_3}{}_{x_3} \text{ for states isotropic in 3-space}), \\
p_t &= \sum_{\mu \ne x_5} K_\mu - mS - U(S), \qquad p_0 = \sum_{\mu \ne x_0} K_\mu - mS - U(S) .
\end{aligned}
$$

**The $x_4$-$x_0$ component** (the off-diagonal component allowed by the symmetry of the metric; $\Omega_{x_0} = \Omega_{x_4} = 0$):

$$
\begin{aligned}
& T^{x_4}{}_{x_0} = -\tfrac14\big(B_{40} - \cot z\,B_{04}\big), \qquad T^{x_0}{}_{x_4} = -\tan^2 z\;T^{x_4}{}_{x_0}, \\
& B_{40} = \bar\Phi\gamma^{(x_4)}\partial_0\Phi - \partial_0\bar\Phi\,\gamma^{(x_4)}\Phi, \qquad B_{04} = \bar\Phi\gamma^{(x_0)}\partial_4\Phi - \partial_4\bar\Phi\,\gamma^{(x_0)}\Phi ;
\end{aligned}
$$

On homogeneous on-shell states both $T^{x_4}{}_{x_0}$ and $T^{x_0}{}_{x_4}$ vanish identically, so these states do not source the off-diagonal field equation $\kappa\,T^{x_4}{}_{x_0} = \cot z\,u\,Q$ of section 11, which then requires $uQ = 0$; this is not claimed for the other off-diagonal components (42 of the remaining 54 are nonzero bilinears in general), whose vanishing is a separate condition on the state (section 12).

**Trace.** Off shell (an exact identity in both engines) $T^\mu{}_\mu = 8L_0 - \sum_\mu K_\mu = 7\sum_\mu K_\mu - 8(mS + U)$. Exactly, $\sum_\mu K_\mu = (m + U')S + \tfrac12(\bar\Phi E - \bar E\Phi)$, so on shell $\sum_\mu K_\mu = (m + U'(S))S$, $L_0 = S\,U'(S) - U(S)$ and

$$
T^\mu{}_\mu = -mS + 7S\,U'(S) - 8U(S) = -mS + 3\lambda S^2 \quad (U = \tfrac{\lambda}{2}S^2) .
$$

**Conservation and energy exchange.** For a diagonal tensor

$$
T = \mathrm{diag}(p_0, p_3, p_3, p_3, -\rho, p_t, p_t, p_t)(x_0, x_4)
$$

whose entries are functions of $x_0$ and $x_4$, all eight components of the divergence are

$$
\nabla_\mu T^\mu{}_{x_4} = -\partial_4\rho - 3a_4'(p_3 - p_t) - \tfrac32u\,(\rho + p_t), \qquad \nabla_\mu T^\mu{}_{x_0} = \partial_0 p_0 + 3H\cot z\,(2p_0 - p_3 - p_t),
$$

and $\nabla_\mu T^\mu{}_\nu = 0$ identically for $\nu = x_1, x_2, x_3, x_5, x_6, x_7$. Conservation is therefore exactly $\partial_4\rho = -3a_4'(p_3 - p_t) - \tfrac32u(\rho + p_t)$ and $\partial_0 p_0 = -3H\cot z\,(2p_0 - p_3 - p_t)$; for a homogeneous tensor (entries functions of $x_4$ only) it gives

$$
\frac{d\rho}{dx_4} = -3\,a_4'\,(p_3 - p_t) - \tfrac32\,u\,(\rho + p_t), \qquad p_3 + p_t = 2p_0 :
$$

energy flows between 3-space and the extra times unless $p_3 = p_t$, and the extra-time volume factor $b_4^{3/2}$ dilutes $\rho + p_t$.

| statement | Wolfram checks (theory) | sympy checks (theory) |
| --- | --- | --- |
| variation tensor in closed form | `T_vielbein_variation_closed_form_C` | `commuting_emt_equals_general_vielbein_variation_on_shell` |
| Belinfante tensor, symmetric | `T_symmetric_part_Belinfante_C` | `commuting_emt_symmetric` |
| normalisation $\delta S_{\mathrm{act}} = \tfrac12\int\sqrt{\lvert g\rvert}\,T^{\mu\nu}\delta g_{\mu\nu}$, diagonal components | `T_diagonal_components_C` | `commuting_emt_equals_vielbein_variation_diagonal` |
| $x_4$-$x_0$ component | `T_x4_x0_component_C` | `commuting_T_x4x0_homogeneous` |
| trace, on-shell kinetic sum | `EMT_trace_C`, `kinetic_sum_on_shell_C` | `commuting_trace_on_shell` |
| energy exchange with the $b_4'$ term and the $x_0$ condition | `energy_exchange_equation` | `energy_exchange_equation` |

## 9. Kinetic energy, potential energy, energy density and pressures

**Split.** $T^\nu{}_\mu = T_{\mathrm{kin}}{}^\nu{}_\mu + T_{\mathrm{pot}}{}^\nu{}_\mu$ with the potential part and the kinetic (derivative) part

$$
\begin{aligned}
T_{\mathrm{pot}}{}^\nu{}_\mu &= -\delta^\nu_\mu\,\big(mS + U(S)\big), \\
T_{\mathrm{kin}}{}^\nu{}_\mu &= \delta^\nu_\mu\sum_\lambda K_\lambda - \tfrac14\big(\bar\Phi\gamma^\nu D_\mu\Phi - D_\mu\bar\Phi\,\gamma^\nu\Phi + \bar\Phi\gamma_\mu D^\nu\Phi - D^\nu\bar\Phi\,\gamma_\mu\Phi\big)
\end{aligned}
$$

(formula `EMT_kinetic_potential` of `Revision/theory/field-theory.json`, compared with the sympy split).

**Densities** (per unit proper 7-volume; the energy in a region of a slice $x_4 = \mathrm{const}$ is the integral with the weight $\sqrt{|g|} = b_4^{3/2}\cos z$):

| quantity | kinetic part | potential part | total |
| --- | --- | --- | --- |
| energy density $\rho = -T^{x_4}{}_{x_4}$ | $-\sum_{\mu \ne x_4} K_\mu$ | $mS + U(S)$ | $-\sum_{\mu \ne x_4} K_\mu + mS + U$ |
| 3-space pressure $p_3 = T^{x_1}{}_{x_1}$ | $\sum_{\mu \ne x_1} K_\mu$ | $-(mS + U)$ | $\sum_{\mu \ne x_1} K_\mu - mS - U$ |
| extra-time pressure $p_t = T^{x_5}{}_{x_5}$ | $\sum_{\mu \ne x_5} K_\mu$ | $-(mS + U)$ | $\sum_{\mu \ne x_5} K_\mu - mS - U$ |
| hidden-direction pressure $p_0 = T^{x_0}{}_{x_0}$ | $\sum_{\mu \ne x_0} K_\mu$ | $-(mS + U)$ | $\sum_{\mu \ne x_0} K_\mu - mS - U$ |

**Homogeneous states on shell** ($\Phi$ depending on $x_4$ only): $K_\mu = 0$ for $\mu \ne x_4$ and $K_{x_4} = (m + U'(S))S$ (the $b_4'$ terms of $\Phi$ and $\bar\Phi$ cancel in $K_{x_4}$). So the kinetic energy density vanishes, $-T_{\mathrm{kin}}{}^{x_4}{}_{x_4} = 0$, the kinetic pressure is $(m + U'(S))S$ in every direction, and

$$
\rho = m S + U(S), \qquad p_3 = p_t = p_0 = S\,U'(S) - U(S) ;
$$

for $U = \tfrac{\lambda}{2}S^2$: $\rho = mS + \tfrac{\lambda}{2}S^2$ and $p = \tfrac{\lambda}{2}S^2$ (formula `EMT_homogeneous_on_shell` of `Revision/theory/field-theory.json`; the exact nonlinear solutions of section 5 realise these values). Along a homogeneous solution $b_4^{3/2}S = S_0$ is constant, $S = b_4^{-3/2}S_0$: $S$, $\rho$ and $p$ follow the extra-time volume, consistent with the energy exchange of section 8, $d\rho/dx_4 = (m + \lambda S)\,dS/dx_4 = -\tfrac32u\,(mS + \lambda S^2) = -\tfrac32u\,(\rho + p)$.

**Sign of the energy (exact).** The classical energy of dirac16complex00 is unbounded below already for $U = 0$ in the good sector. In the flat frame with $m = 2$ and $(k_0, k_1, k_2, k_3) = (4, 1, 2, 0)$, $E = 5$, the one-particle generator commutes with $B$ and its $E = 5$ eigenspace (dimension 8) contains vectors $u_\pm$ with $Bu_- = -u_-$ and $Bu_+ = +u_+$; the positive-frequency solutions $\Phi = c\,u_\pm\,e^{i(k\cdot x - 5x_4)}$ ($|u_\pm| = 1$) have the energy density $\rho = -T^{x_4}{}_{x_4} = -5|c|^2$ and $+5|c|^2$ and the charge density $\Phi^\dagger B\Phi = -|c|^2$ and $+|c|^2$ (`commuting_field_energy_unbounded_below`, both engines). By the Krein-inertia theorem of the pairing record (every real-frequency eigenspace has inertia (4,4), `Q_one_particle_Krein_inertia_real_frequencies`) such negative-energy modes exist at every real frequency. In the author's metric the homogeneous solutions of section 5 have $\rho = mS + \tfrac{\lambda}{2}S^2$ with $S = b_4^{-3/2}S_0$ and $S_0 = \chi^\dagger C\chi$ of either sign. dirac16complex00 therefore has a negative-energy (ghost-like) sector at positive frequency, the classical form of the spin-statistics problem of a commuting field with a first-order Lagrangian; this matters for any reading of Hypothesis00, for example a phantom $w < -1$.

| statement | Wolfram checks | sympy checks |
| --- | --- | --- |
| homogeneous on-shell $\rho$, $p$; kinetic and potential parts | `exact_solution_nonlinear_homogeneous_C` (theory) | `commuting_homogeneous_on_shell_rho_p` (theory) |
| $b_4^{3/2}S$ constant along $x_4$ for a homogeneous solution | `condensate_S_b4_three_halves_constant` ($a_4$ record) | `ownrep_condensate_S_b4_three_halves_constant`, `authorT16_condensate_S_b4_three_halves_constant` ($a_4$ record) |
| energy unbounded below, indefinite charge | `commuting_field_energy_unbounded_below` (scope), `Q_one_particle_Krein_inertia_real_frequencies` (pairing) | `commuting_field_energy_unbounded_below` (scope), `Q.one_particle_Krein_inertia_proof` (pairing) |

## 10. Equations of state

From the diagonal components (SPEC section 4):

$$
w_3 = \frac{p_3}{\rho}, \qquad w_t = \frac{p_t}{\rho}, \qquad w_{x_0} = \frac{p_0}{\rho} .
$$

For homogeneous states on shell the three are equal,

$$
w_3 = w_t = w_{x_0} = \frac{S\,U'(S) - U(S)}{mS + U(S)}, \qquad w = \frac{\lambda S}{2m + \lambda S} \quad (U = \tfrac{\lambda}{2}S^2)
$$

For $\lambda = 0$ the homogeneous state has $p = 0$ and $w = 0$. For $\lambda \ne 0$ the ratio drifts as $b_4$ changes, because $S = b_4^{-3/2}S_0$; on the background history $b_4^{-3/2} \propto e^{-2a_4}$, so $\lambda S/m \propto e^{-2a_4}$.

| statement | source |
| --- | --- |
| definitions and homogeneous values of $w_3$, $w_t$, $w_{x_0}$ | formula `equation_of_state_definitions` of `Revision/theory/field-theory.json`; sympy check `commuting_homogeneous_on_shell_rho_p` |

Not computed in this document: the equation of state that a 3-space observer infers (after integrating over the hidden direction and the extra times), its time dependence as the extra times deflate, CPL parameters, and any comparison with supernova data. These belong to the dark-sector investigation of Hypothesis00 (SPEC section 8), the separate Revision record `Revision/docs/DARK_SECTOR_HYPOTHESES`.

**The verdict of the dark-sector record for dirac16complex00 (Hypothesis00; a summary, every number from its reports, on the background history with $b_4$).** The equation of state that a 3-space observer infers is not fixed by the field equations alone: the 4-dimensional density needs an ASSUMPTION about how the observer normalises over the deflating extra times, and the two normalisations of the dirac16complex00 record (N1, per unit extra-time coordinate volume, the scaling of the definitions (A) and (B) of that document, and N2, per unit proper 7-volume, its definition (C)) are related by $w_{\rm eff}(N2) = w_{\rm eff}(N1) - 1 + \beta/2$ with $\beta = d\ln b_4/da_4 = \tfrac43$, so they differ by exactly $-1/3$ on the history (`observer_N1_weff_identity_b4`, `observer_N2_weff_identity_b4`). Dark matter: under N1 and in the ratio $p_3/\rho$ a positive-energy gas of good-sector modes has the time-varying, dark-matter-like law from $1/3$ to 0, independent of $b_4$, and a $\lambda = 0$ condensate is dust-like. Dark energy: not with positive energies; positive-energy content with real frequencies has $w_{\rm eff}(N2) \geq -1/3$ (`positive_models_bounded_by_minus_one_third`): the gas M2 of good-sector modes, whose physical parameter was CHOSEN on the withdrawn $b_4 = 1$ record to give $w_0 = -0.861$, now has the tangent $(-583/3000, 81037/500000)$, freezing (`M2_tangent_exact_b4`), the extra-time mode M3 the thawing-sign tangent $(-287/1000, -196963/4500000)$ (`M3_tangent_exact_b4`), and the model M4, whose two parameters were CHOSEN on the withdrawn record to reproduce the Unite CPL tangent $(w_0, w_a) = (-0.861, -0.60)$, has on this history the tangent $(-0.287, -0.0667)$ (`M4_withdrawn_tuning_on_b4_history`); for M3 and M4 the bound holds before the turning point $a_*$ of the extra-time mode (M3: $a_* = 6.2640$, M4: $a_* = 1.8859$), past which the mode grows, its frequency is imaginary and the bound is not established. The Unite $w_0$ needs a component of negative classical energy larger than the positive energy, $G \geq 1583/1000$ (`unite_w0_requires_dominant_ghost`), and the composition M5 with a ghost-like component, which crossed $w = -1$ on the withdrawn record, does not cross it on $[1/3, 1]$ on this history (`M5_withdrawn_composition_on_b4_history`). The Unite constant $w = -0.764$ is the ratio of a condensate only at one instant and only for the tuned value $\lambda S/m = -382/441$ (`condensate_ratio_equals_unite_constant_w`), where the drifting ratio has $w_a = -84231/31250 = -2.695392$, the thawing sign (`condensate_ratio_drift_at_unite_value`); it is phantom exactly while $\lambda S/m \in (-2, -1)$ (`condensate_phantom_interval`). No condensate is the source of the background history: its $S = b_4^{-3/2}S_0$ decays, while the history needs the constant source of section 11, and in Einstein gravity a $b_4(x_4)$ needs a $T^{x_4}{}_{x_0}$ that a condensate does not have (`condensate_cannot_source_branch`). The observer's expansion reads $w = -1$ exactly on $a_4 = Hx_4$ (section 3.3 of the dark-sector document). A model with as many tuned parameters as matched numbers reproduces them by construction and is not a prediction; on this history the tuned models of the withdrawn record no longer reproduce the Unite numbers. That record establishes neither Hypothesis nor Hypothesis00; it states what each field can and cannot produce under its stated assumptions.

## 11. The field equations for a4[x4] and b4[x4]

**Einstein-Lovelock equations** (SPEC section 5):

$$
\sum_{k=1}^{3}\alpha_k\,E_{(k)}{}^\mu{}_\nu + \Lambda\,\delta^\mu_\nu = \kappa\,T^\mu{}_\nu, \qquad E_{(k)} = -\frac{P_{(k)}}{2^{k+1}}, \qquad E_{(1)} = G ,
$$

with $P_{(k)}{}^h{}_j$ the Lovelock tensors computed with the generalized Kronecker delta (GKD) from the Riemann tensor (MTW convention). $P_{(4)}$ vanishes in 8 dimensions (a GKD with 9 indices over 8 values), so $k = 1, 2, 3$ is the complete series. The components computed directly from the curvature equal the GKD record `Revision/gkd_lovelock/results/lovelock-tensors.json` monomial by monomial, for general $a_4$ and $b_4$, and the independent record of the metric change. The mixed Riemann components contain neither the warp nor $e^{a_4}$ nor $b_4^{1/2}$, so the left-hand sides depend on $H$, $a_4'$, $a_4''$, $u$ and $v$ only: a constant factor of $b_4$ is a rescaling of $x_5, x_6, x_7$.

**The Lovelock components.** The only nonzero off-diagonal components are the pair $x_4$-$x_0$, $x_0$-$x_4$, each proportional to $u$; $x_2 = x_3 = x_1$ and $x_6 = x_7 = x_5$. The diagonal components (the TeX of `Revision/field_equations_a4/a4-equations.json`, key `lovelockTensors`):

$$
\begin{aligned}
E_{(1)}{}^{x_0}{}_{x_0} &= -3 (a_4')^2+\frac{3 (a_4') u}{2}+15 H^2-\frac{3 u^2}{2} \\
&\quad -\frac{3 v}{2}, \\
E_{(1)}{}^{x_1}{}_{x_1} &= -3 (a_4')^2+3 (a_4') u+a_4''+15 H^2 \\
&\quad -\frac{3 u^2}{2}-\frac{3 v}{2}, \\
E_{(1)}{}^{x_4}{}_{x_4} &= 3 (a_4')^2-\frac{3 (a_4') u}{2}+21 H^2-\frac{3 u^2}{4}, \\
E_{(1)}{}^{x_5}{}_{x_5} &= -3 (a_4')^2-a_4''+15 H^2-\frac{3 u^2}{4} \\
&\quad -v .
\end{aligned}
$$

$$
\begin{aligned}
E_{(2)}{}^{x_0}{}_{x_0} &= 12 (a_4')^4-12 (a_4')^3 u+168 (a_4')^2 H^2+18 (a_4')^2 u^2 \\
&\quad +12 (a_4')^2 v+24 (a_4') a_4'' u-84 (a_4') H^2 u-\frac{15 (a_4') u^3}{2} \\
&\quad -12 (a_4') u v-6 a_4'' u^2-180 H^4+48 H^2 u^2 \\
&\quad +60 H^2 v-\frac{3 u^4}{4}-\frac{3 u^2 v}{2}, \\
E_{(2)}{}^{x_1}{}_{x_1} &= 12 (a_4')^4-24 (a_4')^3 u-24 (a_4')^2 a_4''+168 (a_4')^2 H^2 \\
&\quad +18 (a_4')^2 u^2+12 (a_4')^2 v+24 (a_4') a_4'' u-120 (a_4') H^2 u \\
&\quad -3 (a_4') u^3-6 (a_4') u v-40 a_4'' H^2-3 a_4'' u^2 \\
&\quad -180 H^4+42 H^2 u^2+60 H^2 v-\frac{3 u^4}{4} \\
&\quad -\frac{3 u^2 v}{2}, \\
E_{(2)}{}^{x_4}{}_{x_4} &= -36 (a_4')^4+36 (a_4')^3 u-120 (a_4')^2 H^2+60 (a_4') H^2 u \\
&\quad -\frac{9 (a_4') u^3}{2}-420 H^4+30 H^2 u^2, \\
E_{(2)}{}^{x_5}{}_{x_5} &= 12 (a_4')^4+24 (a_4')^2 a_4''+168 (a_4')^2 H^2-48 (a_4') H^2 u \\
&\quad -3 (a_4') u^3-6 (a_4') u v+40 a_4'' H^2-3 a_4'' u^2 \\
&\quad -180 H^4+24 H^2 u^2+40 H^2 v .
\end{aligned}
$$

$$
\begin{aligned}
E_{(3)}{}^{x_0}{}_{x_0} &= -72 (a_4')^6+108 (a_4')^5 u-648 (a_4')^4 H^2-216 (a_4')^4 u^2 \\
&\quad -108 (a_4')^4 v-432 (a_4')^3 a_4'' u+648 (a_4')^3 H^2 u+171 (a_4')^3 u^3 \\
&\quad +216 (a_4')^3 u v+324 (a_4')^2 a_4'' u^2-1944 (a_4')^2 H^4-324 (a_4')^2 H^2 u^2 \\
&\quad -216 (a_4')^2 H^2 v-\frac{81 (a_4')^2 u^4}{2}-81 (a_4')^2 u^2 v-432 (a_4') a_4'' H^2 u \\
&\quad -54 (a_4') a_4'' u^3+972 (a_4') H^4 u+81 (a_4') H^2 u^3+216 (a_4') H^2 u v \\
&\quad +108 a_4'' H^2 u^2+360 H^6-324 H^4 u^2-540 H^4 v \\
&\quad +\frac{27 H^2 u^4}{2}+27 H^2 u^2 v, \\
E_{(3)}{}^{x_1}{}_{x_1} &= -72 (a_4')^6+216 (a_4')^5 u+360 (a_4')^4 a_4''-648 (a_4')^4 H^2 \\
&\quad -216 (a_4')^4 u^2-108 (a_4')^4 v-432 (a_4')^3 a_4'' u+432 (a_4')^3 H^2 u \\
&\quad +90 (a_4')^3 u^3+108 (a_4')^3 u v+432 (a_4')^2 a_4'' H^2+162 (a_4')^2 a_4'' u^2 \\
&\quad -1944 (a_4')^2 H^4-216 (a_4')^2 H^2 v-\frac{27 (a_4')^2 u^4}{2}-27 (a_4')^2 u^2 v \\
&\quad -432 (a_4') a_4'' H^2 u-18 (a_4') a_4'' u^3+1080 (a_4') H^4 u-54 (a_4') H^2 u^3 \\
&\quad +108 (a_4') H^2 u v+360 a_4'' H^4+54 a_4'' H^2 u^2+360 H^6 \\
&\quad -216 H^4 u^2-540 H^4 v+\frac{27 H^2 u^4}{2}+27 H^2 u^2 v, \\
E_{(3)}{}^{x_4}{}_{x_4} &= 360 (a_4')^6-540 (a_4')^5 u+648 (a_4')^4 H^2+270 (a_4')^4 u^2 \\
&\quad -648 (a_4')^3 H^2 u-45 (a_4')^3 u^3+1080 (a_4')^2 H^4-540 (a_4') H^4 u \\
&\quad +81 (a_4') H^2 u^3+2520 H^6-270 H^4 u^2, \\
E_{(3)}{}^{x_5}{}_{x_5} &= -72 (a_4')^6-360 (a_4')^4 a_4''-648 (a_4')^4 H^2+54 (a_4')^4 u^2 \\
&\quad +72 (a_4')^4 v+288 (a_4')^3 a_4'' u+864 (a_4')^3 H^2 u-18 (a_4')^3 u^3 \\
&\quad -36 (a_4')^3 u v-432 (a_4')^2 a_4'' H^2-54 (a_4')^2 a_4'' u^2-1944 (a_4')^2 H^4 \\
&\quad -324 (a_4')^2 H^2 u^2+864 (a_4') H^4 u+54 (a_4') H^2 u^3+108 (a_4') H^2 u v \\
&\quad -360 a_4'' H^4+54 a_4'' H^2 u^2+360 H^6-162 H^4 u^2 \\
&\quad -360 H^4 v .
\end{aligned}
$$

Each $E_{(k)}$ is divergence-free, and $\sum_h P_{(k)}{}^h{}_h = (8 - 2k)L_{(k)}$. The off-diagonal pair is $\sum_k\alpha_kE_{(k)}{}^{x_4}{}_{x_0} = \cot z\,u\,Q$ and $\sum_k\alpha_kE_{(k)}{}^{x_0}{}_{x_4} = -\tan z\,u\,Q$ with

$$
\begin{aligned}
Q &= 540 (a_4')^4 \alpha_3 H-540 (a_4')^3 \alpha_3 H u-36 (a_4')^2 \alpha_2 H+648 (a_4')^2 \alpha_3 H^3 \\
&\quad +135 (a_4')^2 \alpha_3 H u^2+18 (a_4') \alpha_2 H u-324 (a_4') \alpha_3 H^3 u+\frac{3 \alpha_1 H}{2} \\
&\quad -60 \alpha_2 H^3+\frac{3}{2} \alpha_2 H u^2+540 \alpha_3 H^5-27 \alpha_3 H^3 u^2
\end{aligned}
$$

(key `offDiagonalFactor_Q`; in Einstein gravity $Q = \tfrac32H$).

**The independent equations for a general source** $T = \mathrm{diag}(p_0, p_3, p_3, p_3, -\rho, p_t, p_t, p_t)$ plus $q_{40} = T^{x_4}{}_{x_0}$ and $q_{04} = T^{x_0}{}_{x_4}$:

- constraint ($x_4$, first order: it contains $a_4'$ and $u$, but neither $a_4''$ nor $v$): $\sum_k\alpha_k E_{(k)}{}^{x_4}{}_{x_4} + \Lambda = -\kappa\rho$;
- 3-space ($x_1 = x_2 = x_3$): $\sum_k\alpha_k E_{(k)}{}^{x_1}{}_{x_1} + \Lambda = \kappa p_3$;
- extra times ($x_5 = x_6 = x_7$): $\sum_k\alpha_k E_{(k)}{}^{x_5}{}_{x_5} + \Lambda = \kappa p_t$;
- hidden direction ($x_0$): $\sum_k\alpha_k E_{(k)}{}^{x_0}{}_{x_0} + \Lambda = \kappa p_0$;
- off-diagonal: $\kappa q_{40} = \cot z\,u\,Q$, $\kappa q_{04} = -\tan z\,u\,Q$, and $0 = \kappa T^\mu{}_\nu$ for every other $\mu \ne \nu$.

**The second-order equations.** The 3-space minus extra-time combination and the hidden-direction equation are linear in $(a_4'', v)$, with a Jacobian whose determinant equals $-3$ in Einstein gravity; where it does not vanish they determine $a_4''$ and $v = (b_4'/b_4)'$ from the source.

**Consistency conditions.**

- The combination 3-space plus extra times minus twice the hidden direction is no longer an identity: the field equations give

$$
\begin{aligned}
&270 (a_4')^4 \alpha_3 u^2+180 (a_4')^4 \alpha_3 v+720 (a_4')^3 a_4'' \alpha_3 u-270 (a_4')^3 \alpha_3 u^3 \\
&\quad -360 (a_4')^3 \alpha_3 u v-540 (a_4')^2 a_4'' \alpha_3 u^2-18 (a_4')^2 \alpha_2 u^2-12 (a_4')^2 \alpha_2 v \\
&\quad +324 (a_4')^2 \alpha_3 H^2 u^2+216 (a_4')^2 \alpha_3 H^2 v+\frac{135}{2} (a_4')^2 \alpha_3 u^4+135 (a_4')^2 \alpha_3 u^2 v \\
&\quad -24 (a_4') a_4'' \alpha_2 u+432 (a_4') a_4'' \alpha_3 H^2 u+90 (a_4') a_4'' \alpha_3 u^3+9 (a_4') \alpha_2 u^3 \\
&\quad +12 (a_4') \alpha_2 u v-162 (a_4') \alpha_3 H^2 u^3-216 (a_4') \alpha_3 H^2 u v+6 a_4'' \alpha_2 u^2 \\
&\quad -108 a_4'' \alpha_3 H^2 u^2+\frac{3 \alpha_1 u^2}{4}+\frac{\alpha_1 v}{2}-30 \alpha_2 H^2 u^2 \\
&\quad -20 \alpha_2 H^2 v+\frac{3 \alpha_2 u^4}{4}+\frac{3}{2} \alpha_2 u^2 v+270 \alpha_3 H^4 u^2 \\
&\quad +180 \alpha_3 H^4 v-\frac{27}{2} \alpha_3 H^2 u^4-27 \alpha_3 H^2 u^2 v = \kappa  (-2 p_0+p_3+p_t) .
\end{aligned}
$$

  every term on the left contains $u$ or $v$; at constant $b_4$ (the withdrawn metric) the condition was $p_3 + p_t = 2p_0$, and on the background history with the author's weights the left-hand side vanishes, so there $p_3 + p_t = 2p_0$.
- $x_0$-dependence: the diagonal left-hand sides are free of $x_0$ (and of $a_4$ itself), so every diagonal component of the source must be a function of $x_4$ alone; the off-diagonal pair must have the $x_0$ dependence $\cot z\,u\,Q/\kappa$ and $-\tan z\,u\,Q/\kappa$, an $x_0$-dependent pair unless $uQ = 0$.
- Isotropy: since the left-hand sides of $x_1, x_2, x_3$ coincide (and those of $x_5, x_6, x_7$), the source must have $T^{x_1}{}_{x_1} = T^{x_2}{}_{x_2} = T^{x_3}{}_{x_3}$ and $T^{x_5}{}_{x_5} = T^{x_6}{}_{x_6} = T^{x_7}{}_{x_7}$.
- Conservation: $\nabla_\mu T^\mu{}_{x_4} = -\partial_4\rho - 3a_4'(p_3 - p_t) - \tfrac32u(\rho + p_t) + \partial_0 q_{04} - 6H\tan z\,q_{04}$ and $\nabla_\mu T^\mu{}_{x_0} = \partial_0 p_0 + 3H\cot z\,(2p_0 - p_3 - p_t) + \partial_4 q_{40} + \tfrac32u\,q_{40}$.
- Constraint propagation: $\tfrac{d}{dx_4}\sum_k\alpha_k E_{(k)}{}^{x_4}{}_{x_4} = 3a_4'\sum_k\alpha_k(E^{x_1}{}_{x_1} - E^{x_5}{}_{x_5}) + \tfrac32u\sum_k\alpha_k(E^{x_5}{}_{x_5} - E^{x_4}{}_{x_4}) + 6HuQ$ identically: with the conservation law the derivative of the constraint follows from the other components.

**Einstein gravity** ($\alpha_1 = 1$, $\alpha_2 = \alpha_3 = 0$):

$$
\begin{aligned}
& 3 (a_4')^2-\frac{3 (a_4') u}{2}+21 H^2+\Lambda-\frac{3 u^2}{4} = -\kappa  \rho, \\
& -3 (a_4')^2+3 (a_4') u+a_4''+15 H^2+\Lambda-\frac{3 u^2}{2}-\frac{3 v}{2} = \kappa  p_3, \\
& -3 (a_4')^2-a_4''+15 H^2+\Lambda-\frac{3 u^2}{4}-v = \kappa  p_t, \\
& -3 (a_4')^2+\frac{3 (a_4') u}{2}+15 H^2+\Lambda-\frac{3 u^2}{2}-\frac{3 v}{2} = \kappa  p_0, \\
& \frac{3 \cot z H u}{2} = \kappa  q_{40}, \qquad \kappa  (p_0+\rho ) = -3 (a_4')^2-\frac{3}{4} (u-2 (a_4'))^2-6 H^2-\frac{3 v}{2} .
\end{aligned}
$$

The off-diagonal factor $Q = \tfrac32H$ never vanishes: a source without $T^{x_4}{}_{x_0}$ forces $b_4' = 0$, so with $b_4$ not constant Einstein gravity needs an $x_0$-dependent off-diagonal source. Every source has $\kappa(\rho + p_0) < 0$ wherever $v \ge 0$ (for $\kappa > 0$ it violates the null energy condition along $x_4 + x_0$), and $T = 0$ has no solution for $H > 0$ and any $\Lambda$ (the off-diagonal equation forces $u = 0$, and then the $x_4$ and $x_0$ components cannot both hold).

**Exponential histories** $a_4 = A H x_4 + a_0$, $b_4 = b_4(0)e^{\beta AHx_4}$ ($a_4' = AH$, $u = \beta AH$, $a_4'' = v = 0$; 3-space scale factor $e^{AHx_4}$, extra-time scale factor $e^{-(1 - \beta/2)AHx_4}$). For any $\alpha_k$ the field equations require constant $\rho$, $p_3$, $p_t$, $p_0$, in general with unequal pressures (key `requiredSource`), and the off-diagonal pair $\kappa q_{40} = \cot z\,\beta AH\,Q(A, \beta)$. The required diagonal source contains $A$ only through $A^2$ and the off-diagonal pair is odd in $A$: whether the extra times deflate or inflate is a choice of sign and is not selected by the equations. In Einstein gravity $\kappa q_{40} = \tfrac32\beta AH^2\cot z \ne 0$ for $\beta A \ne 0$. With the author's weights ($\alpha_k = w_k/H^{2k}$, $w = (1, 1/32, 1/1152)$, $\Lambda = -10$ in the convention of this record, the notebook's $\Lambda = 10$)

$$
Q = \frac{3 \left(5 A^4 \beta^2-20 A^4 \beta+20 A^4+A^2 \beta^2+12 A^2 \beta-24 A^2+4\right)}{128 H} ,
$$

which at $A = 1$ is $3\beta(3\beta - 4)/(64H)$: a source without $T^{x_4}{}_{x_0}$ is possible exactly for $\beta = 0$ ($b_4$ constant, excluded) and $\beta = \tfrac43$, the background history

$$
a_4 = Hx_4,\quad b_4 = b_4(0)\,e^{(4/3)Hx_4}
$$

of SPEC section 1, on which the field equations require, at $H = 1$, the constant source

$$
\kappa(\rho, p_3, p_t, p_0) = \big(-\tfrac{2}{27}, -\tfrac29, -\tfrac{22}{27}, -\tfrac{14}{27}\big),\qquad q_{40} = q_{04} = 0 :
$$

a negative energy density for $\kappa > 0$; the history is not a vacuum solution, and the record uses it as a PRESCRIBED background. With these weights an exponential history is a vacuum solution exactly for $\beta = 0$ and $A = \pm1$, none with $b_4$ not constant (that every vacuum solution has $b_4$ constant is proved in `Revision/metric_b4/results/vacuum-b4.json`); in Einstein-Gauss-Bonnet gravity vacuum exponential histories with $b_4$ not constant exist only for the tuned couplings $\beta = 4$, $\alpha_2 = 1/(40H^2(1 - A^2))$ and $\beta = 2(1 + A^2)/A^2$, $\alpha_2 = -A^2/(4H^2(A^2 - 1)^2) < 0$.

| statement | Wolfram checks ($a_4$ record) | sympy checks ($a_4$ record) |
| --- | --- | --- |
| metric with $b_4$, volume, Riemann free of the warp, $e^{a_4}$ and $b_4^{1/2}$ | `metric_is_SPEC_section_1`, `sqrt_abs_det_g_is_cos_z`, `mixed_riemann_free_of_warp_and_a4` | `mixed_riemann_free_of_warp_and_a4`, `riemann_entries_laurent` |
| $P_{(k)}$ from the curvature equal the GKD record and the metric record; traces; $P_{(4)} = 0$ | `P1_direct_equals_minus_4_Einstein`, `P1_direct_equals_gkd_branch_monomials`, `P2_direct_equals_gkd_branch_monomials`, `P3_direct_equals_gkd_branch_monomials`, `P1_trace_identity`, `P2_trace_identity`, `P3_trace_identity`, `P4_vanishes_pigeonhole`, `lovelock_equals_metric_b4_set` | `P1_equals_minus_4_Einstein`, `P1_equals_gkd_branch_monomials`, `P2_equals_gkd_branch_monomials`, `P3_equals_gkd_branch_monomials`, `P1_trace_identity` |
| divergence-free $E_{(k)}$ | `E1_divergence_free`, `E2_divergence_free`, `E3_divergence_free` | `E1_divergence_free`, `E2_divergence_free`, `E3_divergence_free` |
| independent components, structure, $b_4$ only through $u$ and $v$ | `independent_components`, `P1_structure`, `lovelock_depends_on_b4_through_u_and_v` | `other_components_vanish`, `P1_structure`, `json_lovelock_components`, `json_general_source_equations` |
| off-diagonal factor $Q$ | `offdiagonal_factorises` | `offdiagonal_factorises` |
| first-order constraint, second-order system, the identity | `constraint_first_order`, `second_order_system_a4pp_vv`, `algebraic_identity_x1_plus_x5_minus_2x0` | `constraint_first_order`, `second_order_system`, `algebraic_identity` |
| conservation, constraint propagation | `conservation_components`, `constraint_propagation_bianchi` | `conservation_components`, `bianchi_x4`, `json_conservation` |
| Einstein case | `einstein_components`, `einstein_offdiagonal_forces_b4_constant`, `einstein_null_energy_x0`, `einstein_no_vacuum_solution`, `einstein_second_order_system` | `einstein_components`, `einstein_null_energy_x0`, `einstein_no_vacuum`, `json_einstein` |
| exponential histories, the author's weights, the background history, Gauss-Bonnet vacua | `exponential_history_required_source`, `einstein_exponential_history_offdiagonal_source`, `author_weights_branch`, `author_weights_history_source`, `author_weights_no_vacuum_with_b4_not_constant`, `egb_exponential_vacuum_branches` | `exponential_history_required_source`, `author_weights_branch`, `author_weights_history_source`, `author_weights_no_vacuum_with_b4_not_constant`, `egb_exponential_vacuum_branches`, `json_exponential_history` |

## 12. dirac16complex00 as the source of the a4 and b4 equations

**The tensor.** The source is the classical bilinear tensor of section 8. The field-equations record writes it as $T^\mu{}_\nu = \sigma_T\big(-K^{(\mu}{}_{\nu)} + \delta^\mu_\nu\,L_0\big)$ with $K^\mu{}_\nu = \tfrac12(\bar\Phi\gamma^\mu D_\nu\Phi - D_\nu\bar\Phi\,\gamma^\mu\Phi)$ symmetrised, and $\sigma_T = +1$; this is the Belinfante tensor of section 8 (whose symmetrised kinetic term is the same expression), so the two records use the same tensor and the same sign. With $k_\mu = K^\mu{}_\mu$ (no sum; equal to $K_\mu$ of section 8) and $L_0 = \sum_\mu k_\mu - mS - U(S)$:

$$
\rho = k_4 - L_0, \qquad p_3 = L_0 - k_1, \qquad p_t = L_0 - k_5, \qquad p_0 = L_0 - k_0, \qquad q_{40} = -K^{(x_4}{}_{x_0)} .
$$

**The equations with dirac16complex00 as the source** (classical commuting $\Phi$; $k_\mu$, $S$ and $U$ classical bilinears): the constraint $\sum_k\alpha_k E_{(k)}{}^{x_4}{}_{x_4} + \Lambda = -\kappa\,(k_4 - L_0)$; the 3-space, extra-time and hidden-direction equations with $\kappa p_3 = \kappa(L_0 - k_1)$, $\kappa p_t = \kappa(L_0 - k_5)$ and $\kappa p_0 = \kappa(L_0 - k_0)$; the identity of section 11 with $p_3 + p_t - 2p_0 = 2k_0 - k_1 - k_5$; the off-diagonal pair $-\kappa K^{(x_4}{}_{x_0)} = \cot z\,u\,Q$; and $K^{(\mu}{}_{\nu)} = 0$ for every other $\mu \ne \nu$; together with $k_1 = k_2 = k_3$, $k_5 = k_6 = k_7$ and the requirement that every diagonal component be independent of $x_0$. On shell $L_0 = S\,U'(S) - U(S)$. The second-order equations show what drives $a_4''$ and $v$: the differences between the kinetic terms along 3-space, the extra times and the hidden direction. This record contains no exact non-homogeneous dirac16complex00 configuration that satisfies all of these conditions; whether one exists is open.

**The homogeneous condensate.** For $\Phi = \Phi(x_4)$ on shell the field equation is $\partial_4\Phi = A_\Phi\Phi$ with $A_\Phi = A_0 - \tfrac34u\,I_{16}$, $A_0 = -\gamma^{(x_4)}\big(M - 3H\gamma^{(x_0)}\big)$ and $M = m + U'(S)$, free of $x_0$: $\Phi = b_4^{-3/4}\chi$ with $\partial_4\chi = A_0\chi$. Proved exactly for general $b_4$ (Wolfram, and in the sympy record both for an independently built Clifford representation and for the author's T16):

- $CA_\Phi + A_\Phi^TC = -\tfrac32u\,C$, so $\partial_4S = -\tfrac32u\,S$ and $b_4^{3/2}S$ is constant along $x_4$;
- the diagonal kinetic components are $K^{x_4}{}_{x_4} = MS$ and $0$ for every other direction, and $K^{x_4}{}_{x_0} = K^{x_0}{}_{x_4} = 0$ (the $b_4'$ terms of $\Phi$ and $\bar\Phi$ cancel); hence $\rho = mS + U(S)$, $p_3 = p_t = p_0 = S\,U'(S) - U(S)$ and $q_{40} = q_{04} = 0$, and the $x_0$-independence holds;
- the nonzero off-diagonal kinetic components are exactly multiples of the 15 three-gamma bilinears $B_{abc} = \bar\Phi\gamma^{(a)}\gamma^{(b)}\gamma^{(c)}\Phi$ with $\{a,b,c\} = \{i, x_4, x_0\}$ ($i = x_1..x_3, x_5..x_7$) and $\{i, j, x_4\}$ ($i = x_1..x_3$, $j = x_5..x_7$); there are 42 nonzero ordered pairs $(\mu, \nu)$.

The 42 components fall into ten groups; within each group the coefficient is the same for every 3-space index $x_i$ ($i = 1, 2, 3$) and extra-time index $x_t$ ($t = 5, 6, 7$), and on the patch $\sqrt[12]{\cot^2 z+1} = \sin^{-1/6}z$ (the gammas in this table are the frame gammas; the coefficients depend on $H$, $a_4'$, $b_4$ and $u$; generated from `Revision/field_equations_a4/a4-equations.json`):

| component | bilinear | coefficient |
| --- | --- | --- |
| $K^{x_0}{}_{x_i}$ | $\bar\Phi \gamma^{x_0} \gamma^{x_i} \gamma^{x_4} \Phi$ | $\frac{e^{a_4} (a_4')}{4 \cot z \sqrt[12]{\cot^2 z+1}}$ |
| $K^{x_0}{}_{x_t}$ | $\bar\Phi \gamma^{x_0} \gamma^{x_4} \gamma^{x_t} \Phi$ | $-\frac{e^{-a_4} \sqrt{b_4} (2 (a_4')-u)}{8 \cot z \sqrt[12]{\cot^2 z+1}}$ |
| $K^{x_i}{}_{x_0}$ | $\bar\Phi \gamma^{x_0} \gamma^{x_i} \gamma^{x_4} \Phi$ | $\frac{1}{4} e^{-a_4} (a_4') \cot z \sqrt[12]{\cot^2 z+1}$ |
| $K^{x_i}{}_{x_4}$ | $\bar\Phi \gamma^{x_0} \gamma^{x_i} \gamma^{x_4} \Phi$ | $\frac{7}{4} e^{-a_4} \sqrt[12]{\cot^2 z+1}\, H$ |
| $K^{x_i}{}_{x_t}$ | $\bar\Phi \gamma^{x_i} \gamma^{x_4} \gamma^{x_t} \Phi$ | $-\frac{1}{8} e^{-2 a_4} \sqrt{b_4} (4 (a_4')-u)$ |
| $K^{x_4}{}_{x_i}$ | $\bar\Phi \gamma^{x_0} \gamma^{x_i} \gamma^{x_4} \Phi$ | $-\frac{7 e^{a_4} H}{4 \sqrt[12]{\cot^2 z+1}}$ |
| $K^{x_4}{}_{x_t}$ | $\bar\Phi \gamma^{x_0} \gamma^{x_4} \gamma^{x_t} \Phi$ | $-\frac{7 e^{-a_4} \sqrt{b_4} H}{4 \sqrt[12]{\cot^2 z+1}}$ |
| $K^{x_t}{}_{x_0}$ | $\bar\Phi \gamma^{x_0} \gamma^{x_4} \gamma^{x_t} \Phi$ | $\frac{e^{a_4} \cot z \sqrt[12]{\cot^2 z+1} (2 (a_4')-u)}{8 \sqrt{b_4}}$ |
| $K^{x_t}{}_{x_i}$ | $\bar\Phi \gamma^{x_i} \gamma^{x_4} \gamma^{x_t} \Phi$ | $\frac{e^{2 a_4} (4 (a_4')-u)}{8 \sqrt{b_4}}$ |
| $K^{x_t}{}_{x_4}$ | $\bar\Phi \gamma^{x_0} \gamma^{x_4} \gamma^{x_t} \Phi$ | $-\frac{7 e^{a_4} \sqrt[12]{\cot^2 z+1}\, H}{4 \sqrt{b_4}}$ |

The off-diagonal field equations $0 = \kappa T^\mu{}_\nu$ therefore require $B_{i\,x_4 x_0} = 0$ for the six $i$ (each of them appears with a coefficient proportional to $H$) and, where $4a_4' \ne u$, $B_{i j x_4} = 0$ for the nine pairs $i, j$.

**Exact witnesses** that these conditions can be met with $S \ne 0$: $\Phi = b_4^{-3/4}e^{-i\omega x_4}\Phi_0$ with $\omega = \sqrt{M^2 - 9H^2}$ ($M^2 > 9H^2$), and $\Phi_0 = v_1 + c\,v_2$ built from the two eigenvectors of $A_0$ in the sectors $\gamma^{(x_1)}\gamma^{(x_5)} = \gamma^{(x_2)}\gamma^{(x_6)} = \gamma^{(x_3)}\gamma^{(x_7)} = -1$ and $+1$, $c = \overline{v_1^\dagger C v_2}$. At $(M, H) = (5, 1)$, $(5, 4/3)$ and $(-5, 1)$ (exact Gaussian-rational arithmetic) the frequencies are $\omega = 4, 3, 4$, the field solves the condensate equation for every $b_4$, all 15 three-gamma bilinears and every off-diagonal kinetic component vanish for every $a_4$, $a_4'$ and $b_4$, and $b_4^{3/2}S = 51200$, $28800$, $51200$ respectively. These values are computed in the author's matrices T16; $S$ scales with the arbitrary normalisation of the exact null vectors $v_1, v_2$, whereas $\omega$, $S \ne 0$ and the vanishing of the bilinears do not depend on that normalisation.

**Statement (the condensate as a source of the metric with $b_4$).** The condensate is a source of the homogeneous form: equal pressures, $p_3 = p_t = p_0$, and no $T^{x_4}{}_{x_0}$. With $b_4$ not constant such a source is impossible in Einstein gravity (the off-diagonal equation forces $b_4' = 0$); with the author's weights it is the source of no exponential history with $\beta \ne 0$ ($Q = 0$ and equal pressures have no common real solution); in Einstein-Gauss-Bonnet gravity only on the two tuned vacuum branches of section 11; histories that are not exponential are not decided. In particular no condensate is the source of the background history: on it $S = b_4^{-3/2}S_0$ decays like $e^{-2Hx_4}$, and with it $\rho = mS + \tfrac{\lambda}{2}S^2$ and $p = \tfrac{\lambda}{2}S^2$, while the history needs the constant, nonzero source of section 11 (`condensate_cannot_source_branch` of the dark-sector record). The witnesses above show that the off-diagonal conditions can be met; this record contains no check that combines a witness with the field equations for definite $\kappa$, $\Lambda$, $m$, $\lambda$ and a history.

| statement | Wolfram checks ($a_4$ record) | sympy checks ($a_4$ record) |
| --- | --- | --- |
| the Clifford facts used, in the author's T16 (with the Cl(1,1)$^{\otimes 4}$ basis as an exactly equivalent comparison) | `clifford_relations_author_T16`, `C_properties_author_T16`, `gamma_mu_anticommutes_with_Omega_mu_no_sum`, `representations_equivalent_author_T16_own_rep` | `ownrep_clifford`, `ownrep_C_properties`, `ownrep_anticommutator_no_sum`, `authorT16_clifford`, `authorT16_C_properties`, `authorT16_anticommutator_no_sum` |
| condensate equation free of $x_0$; $b_4^{3/2}S$ constant; adjoint | `condensate_equation_x0_consistent`, `condensate_S_b4_three_halves_constant`, `condensate_adjoint_equation` | `ownrep_condensate_S_b4_three_halves_constant`, `ownrep_condensate_adjoint`, `authorT16_condensate_S_b4_three_halves_constant`, `authorT16_condensate_adjoint` |
| diagonal kinetic tensor of the condensate | `condensate_kinetic_tensor_diagonal` | `ownrep_condensate_kinetic_diagonal`, `authorT16_condensate_kinetic_diagonal` |
| off-diagonal components: the 15 three-gamma bilinears, coefficients | `condensate_offdiagonal_are_three_gamma_bilinears`, `offdiagonal_coefficients_representation_independent` | `ownrep_condensate_offdiagonal_three_gamma`, `authorT16_condensate_offdiagonal_three_gamma`, `json_offdiagonal_coefficients`, `offdiagonal_coefficients_representation_independent` |
| exact witnesses | `condensate_diagonal_witness_exact` | `ownrep_condensate_witness`, `authorT16_condensate_witness` |
| the condensate as a source with $b_4$ not constant | `condensate_source_with_b4_not_constant` | `condensate_source_with_b4_not_constant` |

## 13. Pairing theorems for dirac16complex00 (summary)

The pairing of universes of masses $\{+m, -m\}$ is the subject of `Revision/docs/PAIR_CREATION_PROOFS`; for the commuting field the Revision pairing records prove exactly the following, in the primordial field with $b_4(x_4)$ (its spin connection contains $b_4'$, `primordial_connection_depends_on_b4`, `geometry.connection_depends_on_b4`).

**T1 (chirality pairing).** Hypotheses: any gravitational field, fixed and the same for both members (a test field; the metric is not varied); $\Gamma = \mathrm{diag}(-I_8, I_8)$; $U = \tfrac{\lambda}{2}S^2$, or any function $U$ with $U \to -U$. Then, identically,

$$
\mathcal{L}_{m,\lambda}[\Gamma\Phi] = -\mathcal{L}_{-m,-\lambda}[\Phi], \qquad S[\Gamma\Phi] = S[\Phi], \qquad T^{(-m,-\lambda)}[\Gamma\Phi] = -T^{(m,\lambda)}[\Phi], \qquad J[\Gamma\Phi] = -J[\Phi]
$$

(for a general $U$: $\mathcal{L}_{m,U}[\Gamma\Phi] = -\mathcal{L}_{-m,-U}[\Phi]$), and $\Phi$ solves the $(m, \lambda)$ equations if and only if $\Gamma\Phi$ solves the $(-m, -\lambda)$ ones. The pair's total energy-momentum density, current and charge vanish as classical c-number bilinears.

**T2 (mirror pairing).** With the isometry $\phi: x_0 \to \pi/(6H) - x_0$ ($z \to \pi - z$, the $Z_2$ mirror across $z = \pi/2$, an ASSUMED construction at a degenerate surface of the metric) and $\Phi'(\phi(x)) = \gamma^{(x_0)}\Phi(x)$:

$$
\mathcal{L}_{m,\lambda}[\Phi'](\phi(x)) = \mathcal{L}_{-m,\lambda}[\Phi](x), \qquad S' = -S ,
$$

and the mirror partner carries the same energy density and charge (the tensor transformed by the reflection), not the opposite.

There is no quantum reading for dirac16complex00: it is not quantised. These theorems map solutions to solutions; they derive no creation process, rate or amplitude (the lists of what is not established in the pairing records).

| statement | Wolfram checks (pairing) | sympy checks (pairing) |
| --- | --- | --- |
| T1 for the commuting field in the primordial metric with $b_4$ | `Gamma_properties`, `T1_kernel_field_equation`, `T1_linearity_argument`, `primordial_connection_depends_on_b4`, `T1_Lagrangian_primordial_commuting`, `T1_Lagrangian_negative_controls_primordial_commuting`, `T1_field_equation_covariance_primordial_commuting`, `T1_Euler_Lagrange_map_primordial_commuting`, `T1_energy_momentum_primordial_commuting`, `T1_current_primordial_commuting`, `T1_general_potential_primordial_commuting` | `geometry.connection_depends_on_b4`, `T1.metric.commuting.lagrangian`, `T1.metric.commuting.negative_controls`, `T1.metric.commuting.euler_lagrange_map`, `T1.metric.commuting.emt`, `T1.metric.commuting.pair_total_emt_zero`, `T1.metric.commuting.current`, `T1.metric.commuting.general_potential` |
| T2 for the commuting field | `T2_mirror_is_isometry`, `T2_mirror_Lagrangian_commuting`, `T2_mirror_energy_momentum_and_current_commuting`, `T2_mirror_Euler_Lagrange_commuting` | `T2.metric.commuting.euler_lagrange_map`, `T2.metric.commuting.emt`, `T2.metric.commuting.current`, `T2.metric.commuting.S_odd` |

## 14. Check index

Every check below has the verdict PASS in the named report (the publication test re-reads the reports and confirms each name and verdict). Counts at the time of writing: wolfram-algebra 45 checks, python-algebra 35, wolfram-field-theory 84, python-field-theory 72, wolfram-a4-report 59, python-a4-report 65, wolfram-pairing 102, python-pairing 67, wolfram-scope 15, python-scope 14, python-derive-eos 49, python-independent-numerics 32; all pass.

| report | checks cited in this document |
| --- | --- |
| `Revision/algebra/reports/wolfram-algebra.json` | `Clifford_relation`, `reality`, `symmetry_pattern`, `eta_in_author_order`, `coordinate_map`, `C_real_symmetric` |
| `Revision/algebra/reports/wolfram-algebra.json` | `C_squared_identity`, `C_gamma_real_antisymmetric`, `Gamma_diag`, `B_Hermitian`, `B_squared_identity`, `B_signature_8_8` |
| `Revision/algebra/reports/wolfram-algebra.json` | `S_Lorentz_algebra`, `S_preserves_C`, `S_commutes_with_Gamma`, `Pin44_irreducible_commutant_dim_1`, `Spin44_commutant_dim_2_chiral_projectors`, `chiral_halves_irreducible` |
| `Revision/algebra/reports/wolfram-algebra.json` | `chiral_halves_inequivalent_intertwiners_0`, `Spin_Pin_reflection_swaps_halves` |
| `Revision/algebra/reports/python-algebra.json` | `symmetry_pattern`, `coordinate_map`, `clifford_relation`, `clifford_relation_sympy`, `reality_signed_permutations`, `C_equals_notebook_sigma16` |
| `Revision/algebra/reports/python-algebra.json` | `C_real_symmetric_involution`, `C_gamma_antisymmetric`, `chirality_diag`, `chirality_anticommutes`, `B_hermitian_involution_signature`, `S_lorentz_algebra` |
| `Revision/algebra/reports/python-algebra.json` | `S_preserves_C_and_commutes_with_Gamma`, `clifford_products_span_M16`, `pin_commutant_dimension_1`, `even_products_span_M8_plus_M8`, `spin_commutant_dimension_2`, `spin_halves_irreducible` |
| `Revision/algebra/reports/python-algebra.json` | `spin_halves_inequivalent`, `reflections_exchange_halves`, `fixture_comparison_gammas_json` |
| `Revision/theory/reports/wolfram-field-theory.json` | `metric_is_the_authors`, `sqrt_det_g`, `degenerate_at_H_0`, `vielbein_inverse`, `christoffel_count`, `vielbein_postulate` |
| `Revision/theory/reports/wolfram-field-theory.json` | `omega_antisymmetric`, `omega_components`, `Omega_components`, `gamma_covariantly_constant`, `ricci_mixed_components`, `ricci_scalar` |
| `Revision/theory/reports/wolfram-field-theory.json` | `never_flat_for_H_positive`, `L_real_C`, `L_total_divergence_to_unsymmetrised_C`, `L_spin_connection_drops_out_C`, `gammaOmega_divergence_form`, `Majorana_Lg_total_derivative_grassmann` |
| `Revision/theory/reports/wolfram-field-theory.json` | `Majorana_Lg_commuting_control`, `EL_Psibar_C`, `EL_Psi_C`, `adjoint_equation_is_Dirac_conjugate_C`, `Dirac_operator_explicit_C`, `block_form` |
| `Revision/theory/reports/wolfram-field-theory.json` | `evolution_form_C`, `solution_matrix_square`, `exact_solution_x4_x0_C`, `exact_solution_nonlinear_homogeneous_C`, `nontriviality_2_dirac16complex00`, `gammaOmega_total` |
| `Revision/theory/reports/wolfram-field-theory.json` | `gammaOmega_per_direction`, `Omega_vanishes_iff_a4prime_b4prime_and_H_vanish`, `spin_curvature_equals_Riemann`, `good_sector_hermiticity_curved`, `Lichnerowicz_identity_C`, `current_real_C` |
| `Revision/theory/reports/wolfram-field-theory.json` | `current_conservation_identity_C`, `charge_density_is_Krein_form_C`, `Noether_identity_diffeomorphisms_C`, `Noether_identity_local_Lorentz_C`, `conservation_on_shell_general`, `T_vielbein_variation_closed_form_C` |
| `Revision/theory/reports/wolfram-field-theory.json` | `T_symmetric_part_Belinfante_C`, `T_diagonal_components_C`, `T_x4_x0_component_C`, `EMT_trace_C`, `kinetic_sum_on_shell_C`, `energy_exchange_equation` |
| `Revision/theory/reports/python-field-theory.json` | `metric_from_vielbein_equals_SPEC`, `sqrt_det_g_equals_b4_cos_z`, `gammas_json_equals_python_construction`, `christoffel_symmetric_metric_compatible`, `vielbein_postulate`, `spin_connection_antisymmetric` |
| `Revision/theory/reports/python-field-theory.json` | `Omega_x0_and_Omega_x4_vanish`, `spinor_connection_real`, `covariant_constancy_D_mu_gamma_nu`, `curvature_nonzero_flat_only_formally`, `commuting_lagrangian_real`, `commuting_controls_not_vacuous` |
| `Revision/theory/reports/python-field-theory.json` | `commuting_total_divergence_relation`, `anticommutator_gamma_Omega_vanishes`, `divergence_of_sqrtg_gamma`, `negative_control_majorana_grassmann_total_derivative`, `negative_control_majorana_commuting_contrast`, `commuting_euler_lagrange_psibar_variation` |
| `Revision/theory/reports/python-field-theory.json` | `commuting_euler_lagrange_psi_variation`, `commuting_adjoint_equation_is_conjugate`, `hamiltonian_form_and_heisenberg_equation`, `exact_solution_family_x4_x0`, `exact_nonlinear_homogeneous_solution`, `gamma_mu_Omega_mu_equals_3H_gamma_x0_plus_b4_term` |
| `Revision/theory/reports/python-field-theory.json` | `gravity_term_square`, `a4_time_terms_cancel_b4_terms_add`, `nontriviality_Omega_zero_iff_flat`, `spinor_curvature_equals_riemann`, `lichnerowicz_identity_on_fields`, `lichnerowicz_contraction` |
| `Revision/theory/reports/python-field-theory.json` | `commuting_current_conservation`, `commuting_emt_conservation_on_shell`, `commuting_emt_conservation_negative_control`, `commuting_emt_equals_general_vielbein_variation_on_shell`, `commuting_emt_symmetric`, `commuting_emt_equals_vielbein_variation_diagonal` |
| `Revision/theory/reports/python-field-theory.json` | `commuting_T_x4x0_homogeneous`, `commuting_trace_on_shell`, `energy_exchange_equation`, `commuting_homogeneous_on_shell_rho_p` |
| `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `spin_connection_antisymmetric`, `gravity_term_gamma_mu_Omega_mu`, `condensate_S_b4_three_halves_constant`, `metric_is_SPEC_section_1`, `sqrt_abs_det_g_is_cos_z`, `mixed_riemann_free_of_warp_and_a4` |
| `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `P1_direct_equals_minus_4_Einstein`, `P1_direct_equals_gkd_branch_monomials`, `P2_direct_equals_gkd_branch_monomials`, `P3_direct_equals_gkd_branch_monomials`, `P1_trace_identity`, `P2_trace_identity` |
| `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `P3_trace_identity`, `P4_vanishes_pigeonhole`, `lovelock_equals_metric_b4_set`, `E1_divergence_free`, `E2_divergence_free`, `E3_divergence_free` |
| `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `independent_components`, `P1_structure`, `lovelock_depends_on_b4_through_u_and_v`, `offdiagonal_factorises`, `constraint_first_order`, `second_order_system_a4pp_vv` |
| `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `algebraic_identity_x1_plus_x5_minus_2x0`, `conservation_components`, `constraint_propagation_bianchi`, `einstein_components`, `einstein_offdiagonal_forces_b4_constant`, `einstein_null_energy_x0` |
| `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `einstein_no_vacuum_solution`, `einstein_second_order_system`, `exponential_history_required_source`, `einstein_exponential_history_offdiagonal_source`, `author_weights_branch`, `author_weights_history_source` |
| `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `author_weights_no_vacuum_with_b4_not_constant`, `egb_exponential_vacuum_branches`, `clifford_relations_author_T16`, `C_properties_author_T16`, `gamma_mu_anticommutes_with_Omega_mu_no_sum`, `representations_equivalent_author_T16_own_rep` |
| `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `condensate_equation_x0_consistent`, `condensate_adjoint_equation`, `condensate_kinetic_tensor_diagonal`, `condensate_offdiagonal_are_three_gamma_bilinears`, `offdiagonal_coefficients_representation_independent`, `condensate_diagonal_witness_exact` |
| `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `condensate_source_with_b4_not_constant` |
| `Revision/field_equations_a4/reports/python-a4-report.json` | `ownrep_gravity_term`, `authorT16_gravity_term`, `ownrep_condensate_S_b4_three_halves_constant`, `authorT16_condensate_S_b4_three_halves_constant`, `mixed_riemann_free_of_warp_and_a4`, `riemann_entries_laurent` |
| `Revision/field_equations_a4/reports/python-a4-report.json` | `P1_trace_identity`, `P2_trace_identity`, `P3_trace_identity`, `P1_equals_minus_4_Einstein`, `P1_equals_gkd_branch_monomials`, `P2_equals_gkd_branch_monomials` |
| `Revision/field_equations_a4/reports/python-a4-report.json` | `P3_equals_gkd_branch_monomials`, `E1_divergence_free`, `E2_divergence_free`, `E3_divergence_free`, `P1_structure`, `other_components_vanish` |
| `Revision/field_equations_a4/reports/python-a4-report.json` | `json_lovelock_components`, `json_general_source_equations`, `offdiagonal_factorises`, `constraint_first_order`, `second_order_system`, `algebraic_identity` |
| `Revision/field_equations_a4/reports/python-a4-report.json` | `conservation_components`, `bianchi_x4`, `json_conservation`, `einstein_components`, `einstein_null_energy_x0`, `einstein_no_vacuum` |
| `Revision/field_equations_a4/reports/python-a4-report.json` | `json_einstein`, `exponential_history_required_source`, `author_weights_branch`, `author_weights_history_source`, `author_weights_no_vacuum_with_b4_not_constant`, `egb_exponential_vacuum_branches` |
| `Revision/field_equations_a4/reports/python-a4-report.json` | `json_exponential_history`, `ownrep_clifford`, `ownrep_C_properties`, `ownrep_anticommutator_no_sum`, `authorT16_clifford`, `authorT16_C_properties` |
| `Revision/field_equations_a4/reports/python-a4-report.json` | `authorT16_anticommutator_no_sum`, `ownrep_condensate_adjoint`, `authorT16_condensate_adjoint`, `ownrep_condensate_kinetic_diagonal`, `authorT16_condensate_kinetic_diagonal`, `offdiagonal_coefficients_representation_independent` |
| `Revision/field_equations_a4/reports/python-a4-report.json` | `ownrep_condensate_offdiagonal_three_gamma`, `authorT16_condensate_offdiagonal_three_gamma`, `json_offdiagonal_coefficients`, `ownrep_condensate_witness`, `authorT16_condensate_witness`, `condensate_source_with_b4_not_constant` |
| `Revision/pairing/reports/wolfram-pairing.json` | `Q_one_particle_Krein_inertia_real_frequencies`, `primordial_connection_depends_on_b4`, `Gamma_properties`, `T1_kernel_field_equation`, `T1_linearity_argument`, `T1_Lagrangian_primordial_commuting` |
| `Revision/pairing/reports/wolfram-pairing.json` | `T1_Lagrangian_negative_controls_primordial_commuting`, `T1_field_equation_covariance_primordial_commuting`, `T1_Euler_Lagrange_map_primordial_commuting`, `T1_energy_momentum_primordial_commuting`, `T1_current_primordial_commuting`, `T1_general_potential_primordial_commuting` |
| `Revision/pairing/reports/wolfram-pairing.json` | `T2_mirror_is_isometry`, `T2_mirror_Lagrangian_commuting`, `T2_mirror_energy_momentum_and_current_commuting`, `T2_mirror_Euler_Lagrange_commuting` |
| `Revision/pairing/reports/python-pairing.json` | `Q.one_particle_Krein_inertia_proof`, `geometry.connection_depends_on_b4`, `T1.metric.commuting.lagrangian`, `T1.metric.commuting.negative_controls`, `T1.metric.commuting.euler_lagrange_map`, `T1.metric.commuting.emt` |
| `Revision/pairing/reports/python-pairing.json` | `T1.metric.commuting.pair_total_emt_zero`, `T1.metric.commuting.current`, `T1.metric.commuting.general_potential`, `T2.metric.commuting.euler_lagrange_map`, `T2.metric.commuting.emt`, `T2.metric.commuting.current` |
| `Revision/pairing/reports/python-pairing.json` | `T2.metric.commuting.S_odd` |
| `Revision/theory/reports/wolfram-scope.json` | `connection_free_lagrangian_same_equations`, `good_sector_hermiticity_up_to_the_brane_flux`, `boosted_frame_reproduces_metric`, `boosted_frame_canonical_connection`, `boosted_frame_gammaOmega_formula`, `boosted_frame_removes_only_the_H_term` |
| `Revision/theory/reports/wolfram-scope.json` | `boosted_frame_curvature_nonzero`, `rescaling_removes_the_connection_term`, `rescaled_equation_quadratic_potential`, `gammaOmega_blind_to_the_deflation`, `spin_connection_in_the_energy_momentum_tensor`, `extra_time_growth_rates_unbounded` |
| `Revision/theory/reports/wolfram-scope.json` | `good_sector_x0_independent_modes_without_boundary_condition`, `commuting_field_energy_unbounded_below` |
| `Revision/theory/reports/python-scope.json` | `connection_free_lagrangian_same_equations`, `good_sector_hermiticity_up_to_the_brane_flux`, `boosted_frame_reproduces_metric`, `boosted_frame_canonical_connection`, `boosted_frame_gammaOmega_formula`, `boosted_frame_removes_only_the_H_term` |
| `Revision/theory/reports/python-scope.json` | `boosted_frame_curvature_nonzero`, `rescaling_removes_the_connection_term`, `rescaled_equation_quadratic_potential`, `gammaOmega_blind_to_the_deflation`, `spin_connection_in_the_energy_momentum_tensor`, `extra_time_growth_rates_unbounded` |
| `Revision/theory/reports/python-scope.json` | `good_sector_x0_independent_modes_without_boundary_condition`, `commuting_field_energy_unbounded_below` |
| `Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json` | `observer_N1_weff_identity_b4`, `observer_N2_weff_identity_b4`, `positive_models_bounded_by_minus_one_third`, `M2_tangent_exact_b4`, `M3_tangent_exact_b4`, `M4_withdrawn_tuning_on_b4_history` |
| `Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json` | `unite_w0_requires_dominant_ghost`, `M5_withdrawn_composition_on_b4_history`, `condensate_ratio_equals_unite_constant_w`, `condensate_ratio_drift_at_unite_value`, `condensate_phantom_interval`, `condensate_cannot_source_branch` |

## 15. What is not claimed

- **No quantisation.** dirac16complex00 is not quantised; its energy-momentum tensor is a classical bilinear. The operator statements (Krein space, Fock space, normal ordering) belong to dirac16complex.
- **The energy is not bounded below, the charge is indefinite.** The record decides the energy question negatively: already for $U = 0$ in the good sector there are positive-frequency solutions of negative energy, and the energy density $-5|c|^2$ of the example of section 9 is unbounded below as $|c|$ grows; the charge $\int b_4^{3/2}\cos z\,\Phi^\dagger B\Phi$ is indefinite and only locally conserved (it is constant only if no charge flows through the brane $z = \pi/2$; see the item on the brane below). The descriptions "semi-classical" and "analogue of Dirac's 1928 wave function" are interpretations: that wave function has a positive conserved density, this field does not.
- **Frame dependence of the gravitational term.** $\gamma^\mu\Omega_\mu = 3H\gamma^{(x_0)} + \tfrac34u\,\gamma^{(x_4)}$ is the value for the diagonal vielbein and the variables $\Phi$; its $H$ part vanishes in the boosted frame of section 6 (no boost in this plane removes its $b_4'$ part), and the rescaling $\Phi = b_4^{-3/4}\sin^{-1/2}z\,\chi$ removes all of it. Only $\Omega_\mu$ itself (curvature) and the frame factors are frame-independent; non-triviality [2] is claimed in this exact sense.
- **No 3-space observer equation of state, no CPL fit, no comparison with supernova data.** Section 10 gives the ratios $p/\rho$ of the 8-dimensional tensor only; Hypothesis00 (a time-varying dark-energy or dark-matter equation of state from dirac16complex00) is investigated in the separate dark-sector record `Revision/docs/DARK_SECTOR_HYPOTHESES`, not here (its verdict is summarised in section 10: it establishes neither hypothesis). For the homogeneous condensate with $\lambda \ne 0$ the ratio $w$ drifts with $b_4$.
- **No general solution, no well-posed Cauchy problem.** The exact solutions of section 5 are test points; the field equation is not solved in general, and no existence statement for the nonlinear Cauchy problem is made beyond the first-order evolution form. For data that depend on the extra times the problem is ill-posed in Hadamard's sense (section 7), and the good sector needs a boundary condition at $z = \pi/2$, which this record does not impose.
- **No history from a condensate.** Section 12 shows that a homogeneous condensate cannot be the source of the metric with $b_4$ not constant in Einstein gravity, that with the author's weights it is the source of no exponential history with $b_4$ not constant, and that no condensate is the source of the background history; non-exponential histories are not decided, the sign of $A$ is not selected by the equations, and no non-homogeneous source (which would drive $a_4''$ and $v$ through differences of the kinetic terms) is constructed.
- **The $x_0$ dependence.** The metric of section 1 is an exact solution only with an isotropic source whose diagonal components are independent of $x_0$ and whose off-diagonal components vanish except the pair $x_4$-$x_0$ of section 11, which must be $\cot z\,u\,Q/\kappa$; a dirac16complex00 configuration whose diagonal components depend on $x_0$ is not a consistent source for this metric.
- **The brane.** The patch end $z = \pi/2$ is a degenerate surface of the metric ($g_{00} = 0$, $\sqrt{|g|} = 0$) at finite proper distance; no junction condition is derived, the mirror construction used by T2 is an assumption, and the boundary term $b_4^{3/2}\sin z\,u^\dagger M_0 v$ of the hidden direction does not vanish there.
- **Pairing.** The pairing theorems of section 13 derive no creation process, rate or amplitude for universes of masses $\{+m, -m\}$; they are correspondences between solutions, in a fixed gravitational field.
- **The withdrawn metric.** The earlier metric with $b_4 = 1$ is withdrawn; no statement of this document is restricted to it, and its formulas are not results of this record (they are the values of the formulas above at $u = v = 0$, a case the record excludes).
- **Notebook conventions.** The canonical spin connection used here is the one with $\omega_{\mu ab} = \eta_{ac}\omega_\mu{}^c{}_b$; the notebook's contraction of the mixed components (which lacks a metric factor) is not used, and its Majorana-type $L_g$ serves only as the negative control of section 4.

## 16. Reproduction

From the repository root, in this order (each verifier writes its report and exits with code 0 only if every check passes; every calculation stays below the limit of 7 min 3 s for one run):

```text
wolframscript -file Revision/algebra/wolfram/verify_algebra.wls
python Revision/algebra/python/check_algebra.py
wolframscript -file Revision/theory/wolfram/verify_field_theory.wls base
wolframscript -file Revision/theory/wolfram/verify_field_theory.wls emt-G
wolframscript -file Revision/theory/wolfram/verify_field_theory.wls emt-C
wolframscript -file Revision/theory/wolfram/verify_field_theory.wls solutions
wolframscript -file Revision/theory/wolfram/verify_field_theory.wls solutions-G
wolframscript -file Revision/theory/wolfram/verify_field_theory.wls quantisation
wolframscript -file Revision/theory/wolfram/verify_field_theory.wls merge
python Revision/theory/python/check_field_theory.py --part nonlinear
python Revision/theory/python/check_field_theory.py
wolframscript -file Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls
python Revision/field_equations_a4/python/check_field_equations_a4.py
wolframscript -file Revision/pairing/wolfram/verify_pairing.wls
python Revision/pairing/python/check_pairing.py
wolframscript -file Revision/theory/wolfram/verify_scope.wls
python Revision/theory/python/check_scope.py
```

The Wolfram field-theory verifier runs in six parts and a merge (on 2026-10-15: 35 s, 156 s, 108 s, 34 s, 51 s, 11 s and 5 s; the scope verifier 29 s), and the sympy checker in two runs, the part `--part nonlinear` (209 s; the nonlinear homogeneous solutions of both statistics, written to a git-ignored part file that the full run takes over only if its inputs are unchanged) and the full run (128 s), whose comparison with the Wolfram record agrees entirely (33 of 33 formula records and 65 of 65 check pairs); `Revision/theory/wolfram/WOLFRAMSCRIPT_PROVENANCE.md`, section 6.9. The run times of the other verifiers are recorded in the READMEs of their folders and in `Revision/docs/PAIR_CREATION_PROOFS`.

The two dark-sector programs whose reports section 10 cites (their place in the full order and their run times are given in section 12 of `Revision/docs/DARK_SECTOR_HYPOTHESES`):

```text
python Revision/dark_sector/dirac16complex00/python/derive_eos.py
python Revision/dark_sector/dirac16complex00/python/independent_numerics.py
```

The document is built and checked with (the first command on one line)

```text
python scripts/build_provenance_pdf.py Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md
       --developer-layout --specifications Revision/pdf-specifications.json
python -m unittest Revision/tests/test_dirac16complex00_field_theory_publication.py -v
```

The builder makes the .tex twice and the PDF in two fresh directories, requires byte identity and a warning-free LaTeX log, and verifies the PDF against its entry in Revision's own registry `Revision/pdf-specifications.json`. The publication test checks that the .tex is the builder's output for this .md, that the PDF is registered with its page count and sha256, that the formula blocks of sections 5, 11 and 12 are the ones generated from `Revision/theory/field-theory.json` and `Revision/field_equations_a4/a4-equations.json`, that no statement of the withdrawn metric is left, and that every check cited in section 14 exists in its report with a passing verdict.
