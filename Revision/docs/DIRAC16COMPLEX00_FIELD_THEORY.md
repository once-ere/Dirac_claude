# dirac16complex00 in the primordial gravitational field

## The semi-classical Pin(4,4) spinor field: Lagrangian, field equations, non-triviality [2], energy-momentum tensor, equations of state and the field equations for a4[x4] and b4[x4] (Revision record)

## Abstract

This document records, for the primordial gravitational field of `Revision/SPEC.md` section 1, the field theory of dirac16complex00: a field $\Phi$ with 16 complex commuting components that transform as a spinor of Pin(4,4) (a set of 16 scalar fields that transform as a Pin(4,4) spinor), treated as a classical ("semi-classical") field. The metric is the corrected metric of 2026-10-16 (version 2): $g = \mathrm{diag}\big(e^{-2a_4}b_4\cot^2 z,\ e^{2a_4}\,(\times3),\ -1,\ -e^{-2a_4}b_4(\sin^2 z)^{1/6}\,(\times3)\big)$ with $z = 6Hx_0$ real, two functions $a_4(x_4)$ and $b_4(x_4) > 0$ of the time, the hidden coordinate $x_0$ space-like and $g_{44} = -1$; every statement is proved for general $a_4$ and $b_4$ and for every real $z$ (the metric of 2026-10-14 and its version 1 of 2026-10-16 are withdrawn). The document gives the Lagrangian and its coupling to gravity through the vielbein and the canonical spin connection, the exact Euler-Lagrange equations (covariant, explicit in the metric, and as 16 component equations), the non-triviality theorem [2] with its proof and its exact scope (in the diagonal vielbein the gravitational term of the field equation is $\gamma^\mu\Omega_\mu = \tfrac32He^{a_4}b_4^{-1/2}\gamma^{(x_0)} + (b_4'/b_4 - \tfrac12a_4')\gamma^{(x_4)}$, never zero for $H > 0$; this value depends on the frame and on the field variables, while $\Omega_\mu$ itself vanishes in no frame wherever the metric is curved, which it is on the background history), the self-consistency of the equations and its limits (no well-posed Cauchy problem for data that depend on the extra times; boundary terms at the degenerate points $z = \pi/2 + n\pi$), the energy-momentum tensor as a classical bilinear, its kinetic and potential parts, the energy density, the pressures and the equations of state, and the Einstein-Lovelock field equations for $a_4(x_4)$ and $b_4(x_4)$ with dirac16complex00 as the source. Every formula is an output of Revision code (Wolfram and an independent sympy checker for each part); each section ends with the names of the checks that verify it, and the check index collects them. Nothing is taken from the earlier stages of the repository. The classical energy of dirac16complex00 is unbounded below already for $U = 0$ (positive-frequency modes of negative energy) and its charge is indefinite and only locally conserved. The field equations admit no off-diagonal source and require equal hidden and extra-time pressures; a homogeneous condensate has equal pressures in all directions, and the background history of SPEC section 1 requires an anisotropic source that grows with $x_4$, so no condensate is its source. What the record does not establish is stated in the section "What is not claimed". The verdict of the dark-sector investigation of Hypothesis00 is summarised in section 10, and section 1 points to the other Revision documents.

## 1. Scope, sources and conventions

**Sources.** Every formula and number below is read from these Revision outputs (all produced by Revision code, all checks passing):

| part | Wolfram record | independent sympy record |
| --- | --- | --- |
| gammas, Pin(4,4), Spin(4,4) (SPEC section 2) | `Revision/algebra/reports/wolfram-algebra.json`, fixture `Revision/algebra/gammas.json` | `Revision/algebra/reports/python-algebra.json` |
| geometry, Lagrangian, field equations, energy-momentum tensor (SPEC sections 1-4) | `Revision/theory/reports/wolfram-field-theory.json`, formulas `Revision/theory/field-theory.json` | `Revision/theory/reports/python-field-theory.json` |
| field equations for $a_4(x_4)$ and $b_4(x_4)$ (SPEC section 5) | `Revision/field_equations_a4/reports/wolfram-a4-report.json`, formulas `Revision/field_equations_a4/a4-equations.json` | `Revision/field_equations_a4/reports/python-a4-report.json` |
| pairing theorems (SPEC section 9) | `Revision/pairing/reports/wolfram-pairing.json`, theorems `Revision/pairing/pairing-theory.json` | `Revision/pairing/reports/python-pairing.json` |
| scope of the statements: frame dependence, boundary terms, growth, sign of the energy | `Revision/theory/reports/wolfram-scope.json` | `Revision/theory/reports/python-scope.json` |

The Wolfram and the sympy records are written independently (no shared code); each sympy record re-derives the statements and compares them with the Wolfram record. The theory records verify every statement for both statistics: the checks whose names end in `_C` (Wolfram) or start with `commuting_` (sympy) are the ones for the commuting field dirac16complex00 of this document; the Grassmann versions belong to dirac16complex (`Revision/docs/DIRAC16COMPLEX_FIELD_THEORY`).

**Related Revision documents.** The generalized Kronecker delta and the Lovelock tensors $P_{(1)}$, $P_{(2)}$, $P_{(3)}$ behind the field equations for $a_4$ and $b_4$ of section 11 are described in `Revision/docs/LOVELOCK_GKD`. Hypothesis00 (SPEC section 8) is investigated in the dark-sector record (`Revision/docs/DARK_SECTOR_HYPOTHESES`), whose verdict for dirac16complex00 is summarised at the end of section 10; its two dirac16complex00 records are `Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json` (the derivations and the models; 48 of 48 checks pass) and `Revision/dark_sector/dirac16complex00/reports/python-independent-numerics.json` (an independent implementation from solutions of the field equation; 32 of 32 checks pass). The pairing theorems for both fields are in `Revision/docs/PAIR_CREATION_PROOFS`. The Kohn-Sham model of `Revision/docs/KOHN_SHAM_DEFLATING_FIELD` belongs to dirac16complex and is not used here.

**Coordinates (the author's).** $x_0, x_1, \dots, x_7$, in the author's order: $x_0$ is the hidden direction, space-like (scale factor $e^{-a_4}b_4^{1/2}\lvert\cot z\rvert$); $x_1, x_2, x_3$ are ordinary 3-space (inflating, scale factor $e^{a_4}$); $x_4$ is the time; $x_5, x_6, x_7$ are the three extra times, time-like (scale factor $e^{-a_4}b_4^{1/2}(\sin^2 z)^{1/12}$; on the background history below it is proportional to $e^{-a_4/3}$, an exponential deflation). The hidden direction and the extra times form one block, $e^{-2a_4}b_4$ times a static metric of the $z$ dependence. Throughout $z = 6Hx_0$ takes every real value, $H > 0$ is the author's constant, $a_4' = da_4/dx_4$, $b_4' = db_4/dx_4$, and

$$
u = \frac{b_4'}{b_4},\qquad v = u',\qquad k = \frac{e^{2a_4}}{b_4},\qquad h_4 = \tfrac12u - a_4' = \frac{d}{dx_4}\ln\big(e^{-a_4}b_4^{1/2}\big) .
$$

$h_4$ is the expansion rate of the block $(x_0, x_5, x_6, x_7)$. In formulas the index $i$ runs over $x_1, x_2, x_3$ and $t$ over $x_5, x_6, x_7$.

**The metric** (SPEC section 1, version 2 of 2026-10-16, exactly; rows and columns in the order $x_0, \dots, x_7$):

```text
g = {{E^(-2 a4[x4]) b4[x4] Cot[6 H x0]^2,0,0,0,0,0,0,0},
     {0,E^(2 a4[x4]),0,0,0,0,0,0},
     {0,0,E^(2 a4[x4]),0,0,0,0,0},
     {0,0,0,E^(2 a4[x4]),0,0,0,0},
     {0,0,0,0,-1,0,0,0},
     {0,0,0,0,0,-E^(-2 a4[x4]) b4[x4] (Sin[6 H x0]^2)^(1/6),0,0},
     {0,0,0,0,0,0,-E^(-2 a4[x4]) b4[x4] (Sin[6 H x0]^2)^(1/6),0},
     {0,0,0,0,0,0,0,-E^(-2 a4[x4]) b4[x4] (Sin[6 H x0]^2)^(1/6)}}
```

with two functions of the time, $a_4(x_4)$ and $b_4(x_4) > 0$ (record of the correction: `Revision/metric_warped/`). $(\sin^2 z)^{1/6}$ is the positive real root, so the metric is defined for every real $z$; it is degenerate at the points $z = n\pi/2$ (at $z = \pi/2 + n\pi$: $g_{00} = 0$ and $\sqrt{|g|} = 0$, the fold of the Kohn-Sham record, where the two halves of a cell meet; at $z = n\pi$: $g_{00} \to \infty$ and $g_{tt} \to 0$). Every statement of this document holds for general $a_4$ and $b_4$ and for every real $z$ between these points; $b_4$ is never 1, and a constant $b_4 = c$, which becomes $b_4 = 1$ after the rescaling $x_k \to \sqrt{c}\,x_k$ of $x_0, x_5, x_6, x_7$ together with $H \to H/\sqrt{c}$, is excluded as a history as well. Where a history is needed, it is the background history of SPEC section 1, $a_4 = Hx_4$, $b_4 = b_4(0)e^{(4/3)Hx_4}$ (section 11). Signature (4,4): space-like $x_0, x_1, x_2, x_3$, time-like $x_4, x_5, x_6, x_7$. The volume factor is

$$
\sqrt{|g|} = e^{-a_4}b_4^2\,|\cot z|\,(\sin^2 z)^{1/4} ,
$$

so $\partial_4\sqrt{|g|} = (2u - a_4')\sqrt{|g|}$: the factor $e^{3a_4}$ of 3-space is overcompensated by the factor $e^{-4a_4}b_4^2$ of the block of the hidden direction and the extra times. $H = 0$ is not a metric of the family (a degenerate limit: $g_{55} \to 0$ and $g_{00} \to \infty$ at fixed $x_0 \neq 0$); every statement assumes $H > 0$.

**Spinor notation.** $\bar\Phi = \Phi^\dagger C$, $S = \bar\Phi\Phi$, $U(S)$ a real potential ($U = \tfrac{\lambda}{2}S^2$ where stated), $V = m + U'(S)$. Frame gammas are written $\gamma^{(x_a)}$, coordinate gammas $\gamma^\mu = e^\mu{}_a\gamma^{(a)}$. The theory records write $\Psi$ for both statistics; here $\Phi$ denotes the commuting field.

**Labels.** "Exact" means verified by exact symbolic computation (no floating point) in the named checks; "interpretation" marks a reading that is not itself a computed statement; "ASSUMED" marks an assumption.

| statement | Wolfram checks | sympy checks |
| --- | --- | --- |
| the corrected metric, its vielbein and $\sqrt{\lvert g\rvert}$ | `metric_is_the_corrected_metric`, `sqrt_det_g` | `metric_from_vielbein_equals_SPEC`, `sqrt_det_g` |
| $H = 0$ is a degenerate limit | `degenerate_at_H_0` | |

## 2. The field dirac16complex00 and its symmetry group

dirac16complex00 is a field $\Phi$ with 16 complex commuting components (16 scalar fields) that transform as a Pin(4,4) spinor. It is a classical field; it is not quantised (SPEC section 6: only dirac16complex, the anticommuting field, is quantised canonically). SPEC section 3 calls it the analogue of Dirac's 1928 wave function and the author calls it semi-classical; both are interpretations, and the record shows two exact differences from Dirac's wave function: its charge $Q = \int\sqrt{|g|}\,\Phi^\dagger B\Phi\,d^7x$ (locally conserved, section 7) is an indefinite form, and its classical energy is unbounded below already for $U = 0$ in the good sector (section 9).

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
& f_{x_0} = e^{-a_4}b_4^{1/2}\cot z, \qquad f_{x_1} = f_{x_2} = f_{x_3} = e^{a_4}, \qquad f_{x_4} = 1, \\
& f_{x_5} = f_{x_6} = f_{x_7} = e^{-a_4}b_4^{1/2}(\sin^2 z)^{1/12}
\end{aligned}
$$

($f_{x_0}$ signed) reproduces the corrected metric entry by entry, $g = e^T\eta e$, with inverse $e_a{}^\mu = \delta_a^\mu/f_a$ and $\sqrt{|g|} = \sigma_z f_{x_0}\cdots f_{x_7}$, $\sigma_z = \mathrm{sign}(\cot z)$, constant between the degenerate points.

**Levi-Civita connection.** The 21 independent nonzero Christoffel symbols ($m \le n$) are, for $i = x_1, x_2, x_3$ and $t = x_5, x_6, x_7$ (no sum),

$$
\begin{aligned}
&\Gamma^{x_0}{}_{x_0 x_0} = -12H\csc(12Hx_0), \qquad \Gamma^{x_0}{}_{x_0 x_4} = h_4, \qquad \Gamma^{x_0}{}_{x_t x_t} = H(\sin^2 z)^{1/6}\tan z, \\
&\Gamma^{x_i}{}_{x_i x_4} = a_4', \qquad \Gamma^{x_4}{}_{x_i x_i} = e^{2a_4}a_4', \qquad \Gamma^{x_4}{}_{x_0 x_0} = e^{-2a_4}b_4\cot^2 z\;h_4, \\
&\Gamma^{x_4}{}_{x_t x_t} = -e^{-2a_4}b_4(\sin^2 z)^{1/6}\,h_4, \qquad \Gamma^{x_t}{}_{x_t x_0} = H\cot z, \qquad \Gamma^{x_t}{}_{x_t x_4} = h_4 .
\end{aligned}
$$

The hidden direction and the extra times share the rate $h_4$; 3-space is independent of $x_0$.

**Canonical spin connection.** $\omega_\mu{}^a{}_b = e^a{}_\nu(\partial_\mu e_b{}^\nu + \Gamma^\nu{}_{\mu\lambda}e_b{}^\lambda)$ satisfies the vielbein postulate $\partial_\mu e^a{}_\nu - \Gamma^\lambda{}_{\mu\nu}e^a{}_\lambda + \omega_\mu{}^a{}_b e^b{}_\nu = 0$ for all 512 components, and $\omega_{\mu ab} = \eta_{ac}\omega_\mu{}^c{}_b = -\omega_{\mu ba}$. Exactly 10 components with $a < b$ are nonzero ($s_b = e^{-a_4}b_4^{1/2}$):

$$
\begin{aligned}
& \omega_{x_0,(x_0)(x_4)} = h_4\,s_b\cot z, \qquad \omega_{x_i,(x_i)(x_4)} = a_4'e^{a_4}, \\
& \omega_{x_t,(x_4)(x_t)} = h_4\,s_b(\sin^2 z)^{1/12}, \qquad \omega_{x_t,(x_0)(x_t)} = H(\sin^2 z)^{1/12} ,
\end{aligned}
$$

and $\omega_{x_4} = 0$. Each component is $h_4$, $a_4'$ or $H$ times a factor that does not vanish between the degenerate points.

**Spinor connection and covariant derivative.** $\Omega_\mu = \tfrac12\omega_{\mu ab}S^{ab}$, a real matrix:

$$
\begin{aligned}
\Omega_{x_0} &= \tfrac12 h_4\,s_b\cot z\;\gamma^{(x_0)}\gamma^{(x_4)}, \qquad \Omega_{x_i} = \tfrac12 a_4'e^{a_4}\,\gamma^{(x_i)}\gamma^{(x_4)}, \qquad i = x_1, x_2, x_3, \\
\Omega_{x_t} &= \tfrac12(\sin^2 z)^{1/12}\,\big(h_4\,s_b\,\gamma^{(x_4)}\gamma^{(x_t)} + H\,\gamma^{(x_0)}\gamma^{(x_t)}\big), \qquad t = x_5, x_6, x_7, \qquad \Omega_{x_4} = 0,
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

**Curvature.** $R^\mu{}_\nu$ is diagonal and independent of $x_0$ (unlike the metric of 2026-10-14, there is no off-diagonal Ricci component):

$$
\begin{aligned}
& R^{x_0}{}_{x_0} = R^{x_t}{}_{x_t} = -3H^2k + (a_4')^2 - a_4'' - \tfrac52a_4'u + \tfrac12\frac{b_4''}{b_4} + \tfrac12u^2, \qquad R^{x_i}{}_{x_i} = -(a_4')^2 + a_4'' + 2a_4'u, \\
& R^{x_4}{}_{x_4} = 7(a_4')^2 - a_4'' - 4a_4'u + 2\frac{b_4''}{b_4} - u^2,
\end{aligned}
$$

$$
R = -12H^2k + 8(a_4')^2 - 2a_4'' - 8a_4'u + 4\frac{b_4''}{b_4} + u^2 .
$$

These equal the independent sympy record of the corrected metric, `Revision/metric_warped/results/warped-metric.json`. The metric is not curved for every member of the family: for $a_4 = 0$, $b_4 = H^2x_4^2$ all 4096 Riemann components vanish (8-dimensional flat space in Milne form: the block of curvature $-H^2$ scaled by $Hx_4$). On the background history $a_4 = Hx_4$, $b_4 = e^{(4/3)Hx_4}$ the metric is curved ($R \neq 0$).

| statement | Wolfram checks (theory) | sympy checks (theory) |
| --- | --- | --- |
| vielbein and its inverse | `metric_is_the_corrected_metric`, `vielbein_inverse` | `metric_from_vielbein_equals_SPEC` |
| 21 Christoffel symbols | `christoffel_count` | `christoffel_symmetric_metric_compatible` |
| vielbein postulate, antisymmetry, the 10 components | `vielbein_postulate`, `omega_antisymmetric`, `omega_components` | `vielbein_postulate`, `spin_connection_antisymmetric` |
| $\Omega_\mu$ (real); $\Omega_{x_4} = 0$, $\Omega_{x_0} \neq 0$ | `Omega_components` | `Omega_x4_vanishes_Omega_x0_does_not`, `spinor_connection_real` |
| covariant constancy of the gammas | `gamma_covariantly_constant`, `S_rotates_gamma_with_omega` | `covariant_constancy_D_mu_gamma_nu` |
| Ricci tensor (diagonal) and scalar; the flat member; curved on the background history | `ricci_mixed_components`, `ricci_scalar`, `flat_member_and_curvature` | `curvature_and_flat_member` |

## 4. The Lagrangian

The Lagrangian density (SPEC section 3; the same form as for dirac16complex, only the statistics differ):

$$
\mathcal{L} = \sqrt{|g|}\,\Big[\tfrac12\big(\bar\Phi\gamma^\mu D_\mu\Phi - (D_\mu\bar\Phi)\gamma^\mu\Phi\big) - m\,S - U(S)\Big], \qquad S = \bar\Phi\Phi = \Phi^\dagger C\Phi ,
$$

with $\sqrt{|g|} = e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}$, an explicit mass term linear in $m$ and quadratic in the spinor, and $U(S) = \tfrac{\lambda}{2}S^2$ where stated (a general real $U$ elsewhere). Proved exactly for the commuting field:

1. $\mathcal{L}$ is real, $\mathcal{L}^* = \mathcal{L}$: $C$ real symmetric, $C\gamma^{(a)}$ real antisymmetric and $(S^{ab})^TC + CS^{ab} = 0$ make the symmetrised kinetic term and $\bar\Phi\Phi$ real without a factor $i$ (the sympy record checks it on 408 monomials, with the control that the unsymmetrised form is not real off shell).
2. $\mathcal{L}$ differs from the unsymmetrised form by a total divergence: $\mathcal{L} = \sqrt{|g|}\,[\bar\Phi\gamma^\mu D_\mu\Phi - mS - U] - \tfrac12\partial_\mu(\sqrt{|g|}\,\bar\Phi\gamma^\mu\Phi)$.
3. For this diagonal metric $\{\gamma^\mu, \Omega_\mu\} = 0$ for each $\mu$ separately ($\Omega_\mu$ contains only $S^{(\mu)b}$), so $\bar\Phi\{\gamma^\mu, \Omega_\mu\}\Phi = 0$ and the spin connection drops out of $\mathcal{L}$ itself (next display).

$$
\mathcal{L} = \sqrt{|g|}\,\Big[\tfrac12\sum_a \frac{1}{f_a}\big(\bar\Phi\gamma^{(a)}\partial_a\Phi - \partial_a\bar\Phi\,\gamma^{(a)}\Phi\big) - m S - U(S)\Big] .
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
& e^{a_4}b_4^{-1/2}\tan z\,\gamma^{(x_0)}\partial_0\Phi + e^{-a_4}\big(\gamma^{(x_1)}\partial_1 + \gamma^{(x_2)}\partial_2 + \gamma^{(x_3)}\partial_3\big)\Phi + \gamma^{(x_4)}\partial_4\Phi \\
& \qquad + e^{a_4}b_4^{-1/2}(\sin^2 z)^{-1/12}\big(\gamma^{(x_5)}\partial_5 + \gamma^{(x_6)}\partial_6 + \gamma^{(x_7)}\partial_7\big)\Phi \\
& \qquad + \tfrac32He^{a_4}b_4^{-1/2}\,\gamma^{(x_0)}\Phi + \big(u - \tfrac12a_4'\big)\,\gamma^{(x_4)}\Phi = \big(m + U'(S)\big)\,\Phi ,
\end{aligned}
$$

and the adjoint equation

$$
\begin{aligned}
& e^{a_4}b_4^{-1/2}\tan z\,\partial_0\bar\Phi\,\gamma^{(x_0)} + e^{-a_4}\big(\partial_1\bar\Phi\,\gamma^{(x_1)} + \partial_2\bar\Phi\,\gamma^{(x_2)} + \partial_3\bar\Phi\,\gamma^{(x_3)}\big) + \partial_4\bar\Phi\,\gamma^{(x_4)} \\
& \qquad + e^{a_4}b_4^{-1/2}(\sin^2 z)^{-1/12}\big(\partial_5\bar\Phi\,\gamma^{(x_5)} + \partial_6\bar\Phi\,\gamma^{(x_6)} + \partial_7\bar\Phi\,\gamma^{(x_7)}\big) \\
& \qquad + \tfrac32He^{a_4}b_4^{-1/2}\,\bar\Phi\,\gamma^{(x_0)} + \big(u - \tfrac12a_4'\big)\,\bar\Phi\,\gamma^{(x_4)} = -\big(m + U'(S)\big)\,\bar\Phi .
\end{aligned}
$$

The derivative coefficients are $1/f_a$: the inverse 3-space scale factor $e^{-a_4}$, the inverse extra-time scale factor $e^{a_4}b_4^{-1/2}(\sin^2 z)^{-1/12}$ and the inverse hidden scale factor $e^{a_4}b_4^{-1/2}\tan z$ (both grow as the block deflates); the last two terms on the left are the spin-connection term $\gamma^\mu\Omega_\mu\Phi$.

**Evolution form.** Since $(\gamma^{(x_4)})^2 = -1$, the field equation is equivalent to the first-order evolution equation

$$
\partial_4\Phi = -\gamma^{(x_4)}\Big[\big(m + U'(S)\big)\Phi - \sum_{a \ne x_4}\frac{1}{f_a}\,\gamma^{(a)}\partial_a\Phi - \tfrac32He^{a_4}b_4^{-1/2}\,\gamma^{(x_0)}\Phi\Big] - \big(u - \tfrac12a_4'\big)\,\Phi ;
$$

the slices $x_4 = \mathrm{const}$ are non-characteristic ($g^{44} = -1 \ne 0$), and the last term is the factor $e^{a_4/2}b_4^{-1}$ of the solutions below.

**Chiral block form.** With $\Phi = (\varphi_-, \varphi_+)$ ($\Gamma = -1$ on rows 1-8, $\Gamma = +1$ on rows 9-16) every gamma is block off-diagonal, with $8\times8$ blocks $\bar\tau_a$ (upper right) and $\tau_a$ (lower left) listed in `Revision/theory/field-theory.json` (`field_equation_blocks`), and with $c_g = \tfrac32He^{a_4}b_4^{-1/2}$ and $v_g = u - \tfrac12a_4'$ the field equation is the pair

$$
\begin{aligned}
& \sum_a \frac{1}{f_a}\,\bar\tau_a\,\partial_a\varphi_+ + c_g\,\bar\tau_{x_0}\varphi_+ + v_g\,\bar\tau_{x_4}\varphi_+ = V\varphi_-, \\
& \sum_a \frac{1}{f_a}\,\tau_a\,\partial_a\varphi_- + c_g\,\tau_{x_0}\varphi_- + v_g\,\tau_{x_4}\varphi_- = V\varphi_+ .
\end{aligned}
$$

The mass term and the gravitational terms couple the two chiral halves.

**The 16 component equations.** With $\epsilon_s = e^{-a_4}$, $\epsilon_t = e^{a_4}b_4^{-1/2}(\sin^2 z)^{-1/12}$, $\epsilon_0 = e^{a_4}b_4^{-1/2}$, $t = \tan z$, $\hat\partial_4 = \partial_4 + u - \tfrac12a_4'$, $V = m + U'(S)$ and $\Phi_A$ the components in the row order of `Revision/algebra/gammas.json`, the equation $(\gamma^\mu D_\mu\Phi)_A = V\Phi_A$ reads (generated from `field_equation_components` of `Revision/theory/field-theory.json`, which the sympy record compares term by term; the term $v_g\gamma^{(x_4)}$ of the spin connection enters every component on the same component and with the same sign as $\partial_4$, hence $\hat\partial_4$, and the term $c_g\gamma^{(x_0)}$ next to the hidden-direction derivative, hence $\epsilon_0(t\,\partial_0 + \tfrac32H)$):

$$
\begin{aligned}
(1)\;\; & -\hat\partial_4\Phi_{14} + \epsilon_s\,(-\partial_1\Phi_{16} + \partial_2\Phi_{15} - \partial_3\Phi_{14}) \\
& + \epsilon_t\,(\partial_5\Phi_{15} + \partial_6\Phi_{16} + \partial_7\Phi_{9}) + \epsilon_0\,(t\,\partial_0 + \tfrac32H)\,\Phi_{9} = V\,\Phi_{1} \\
(2)\;\; & \hat\partial_4\Phi_{13} + \epsilon_s\,(-\partial_1\Phi_{15} - \partial_2\Phi_{16} + \partial_3\Phi_{13}) \\
& + \epsilon_t\,(\partial_5\Phi_{16} - \partial_6\Phi_{15} + \partial_7\Phi_{10}) + \epsilon_0\,(t\,\partial_0 + \tfrac32H)\,\Phi_{10} = V\,\Phi_{2} \\
(3)\;\; & \hat\partial_4\Phi_{16} + \epsilon_s\,(\partial_1\Phi_{14} - \partial_2\Phi_{13} - \partial_3\Phi_{16}) \\
& + \epsilon_t\,(-\partial_5\Phi_{13} + \partial_6\Phi_{14} + \partial_7\Phi_{11}) + \epsilon_0\,(t\,\partial_0 + \tfrac32H)\,\Phi_{11} = V\,\Phi_{3} \\
(4)\;\; & -\hat\partial_4\Phi_{15} + \epsilon_s\,(\partial_1\Phi_{13} + \partial_2\Phi_{14} + \partial_3\Phi_{15}) \\
& + \epsilon_t\,(-\partial_5\Phi_{14} - \partial_6\Phi_{13} + \partial_7\Phi_{12}) + \epsilon_0\,(t\,\partial_0 + \tfrac32H)\,\Phi_{12} = V\,\Phi_{4}
\end{aligned}
$$

$$
\begin{aligned}
(5)\;\; & \hat\partial_4\Phi_{10} + \epsilon_s\,(-\partial_1\Phi_{12} + \partial_2\Phi_{11} - \partial_3\Phi_{10}) \\
& + \epsilon_t\,(-\partial_5\Phi_{11} - \partial_6\Phi_{12} - \partial_7\Phi_{13}) + \epsilon_0\,(t\,\partial_0 + \tfrac32H)\,\Phi_{13} = V\,\Phi_{5} \\
(6)\;\; & -\hat\partial_4\Phi_{9} + \epsilon_s\,(-\partial_1\Phi_{11} - \partial_2\Phi_{12} + \partial_3\Phi_{9}) \\
& + \epsilon_t\,(-\partial_5\Phi_{12} + \partial_6\Phi_{11} - \partial_7\Phi_{14}) + \epsilon_0\,(t\,\partial_0 + \tfrac32H)\,\Phi_{14} = V\,\Phi_{6} \\
(7)\;\; & -\hat\partial_4\Phi_{12} + \epsilon_s\,(\partial_1\Phi_{10} - \partial_2\Phi_{9} - \partial_3\Phi_{12}) \\
& + \epsilon_t\,(\partial_5\Phi_{9} - \partial_6\Phi_{10} - \partial_7\Phi_{15}) + \epsilon_0\,(t\,\partial_0 + \tfrac32H)\,\Phi_{15} = V\,\Phi_{7} \\
(8)\;\; & \hat\partial_4\Phi_{11} + \epsilon_s\,(\partial_1\Phi_{9} + \partial_2\Phi_{10} + \partial_3\Phi_{11}) \\
& + \epsilon_t\,(\partial_5\Phi_{10} + \partial_6\Phi_{9} - \partial_7\Phi_{16}) + \epsilon_0\,(t\,\partial_0 + \tfrac32H)\,\Phi_{16} = V\,\Phi_{8}
\end{aligned}
$$

$$
\begin{aligned}
(9)\;\; & \hat\partial_4\Phi_{6} + \epsilon_s\,(\partial_1\Phi_{8} - \partial_2\Phi_{7} + \partial_3\Phi_{6}) \\
& + \epsilon_t\,(-\partial_5\Phi_{7} - \partial_6\Phi_{8} - \partial_7\Phi_{1}) + \epsilon_0\,(t\,\partial_0 + \tfrac32H)\,\Phi_{1} = V\,\Phi_{9} \\
(10)\;\; & -\hat\partial_4\Phi_{5} + \epsilon_s\,(\partial_1\Phi_{7} + \partial_2\Phi_{8} - \partial_3\Phi_{5}) \\
& + \epsilon_t\,(-\partial_5\Phi_{8} + \partial_6\Phi_{7} - \partial_7\Phi_{2}) + \epsilon_0\,(t\,\partial_0 + \tfrac32H)\,\Phi_{2} = V\,\Phi_{10} \\
(11)\;\; & -\hat\partial_4\Phi_{8} + \epsilon_s\,(-\partial_1\Phi_{6} + \partial_2\Phi_{5} + \partial_3\Phi_{8}) \\
& + \epsilon_t\,(\partial_5\Phi_{5} - \partial_6\Phi_{6} - \partial_7\Phi_{3}) + \epsilon_0\,(t\,\partial_0 + \tfrac32H)\,\Phi_{3} = V\,\Phi_{11} \\
(12)\;\; & \hat\partial_4\Phi_{7} + \epsilon_s\,(-\partial_1\Phi_{5} - \partial_2\Phi_{6} - \partial_3\Phi_{7}) \\
& + \epsilon_t\,(\partial_5\Phi_{6} + \partial_6\Phi_{5} - \partial_7\Phi_{4}) + \epsilon_0\,(t\,\partial_0 + \tfrac32H)\,\Phi_{4} = V\,\Phi_{12}
\end{aligned}
$$

$$
\begin{aligned}
(13)\;\; & -\hat\partial_4\Phi_{2} + \epsilon_s\,(\partial_1\Phi_{4} - \partial_2\Phi_{3} + \partial_3\Phi_{2}) \\
& + \epsilon_t\,(\partial_5\Phi_{3} + \partial_6\Phi_{4} + \partial_7\Phi_{5}) + \epsilon_0\,(t\,\partial_0 + \tfrac32H)\,\Phi_{5} = V\,\Phi_{13} \\
(14)\;\; & \hat\partial_4\Phi_{1} + \epsilon_s\,(\partial_1\Phi_{3} + \partial_2\Phi_{4} - \partial_3\Phi_{1}) \\
& + \epsilon_t\,(\partial_5\Phi_{4} - \partial_6\Phi_{3} + \partial_7\Phi_{6}) + \epsilon_0\,(t\,\partial_0 + \tfrac32H)\,\Phi_{6} = V\,\Phi_{14} \\
(15)\;\; & \hat\partial_4\Phi_{4} + \epsilon_s\,(-\partial_1\Phi_{2} + \partial_2\Phi_{1} + \partial_3\Phi_{4}) \\
& + \epsilon_t\,(-\partial_5\Phi_{1} + \partial_6\Phi_{2} + \partial_7\Phi_{7}) + \epsilon_0\,(t\,\partial_0 + \tfrac32H)\,\Phi_{7} = V\,\Phi_{15} \\
(16)\;\; & -\hat\partial_4\Phi_{3} + \epsilon_s\,(-\partial_1\Phi_{1} - \partial_2\Phi_{2} - \partial_3\Phi_{3}) \\
& + \epsilon_t\,(-\partial_5\Phi_{2} - \partial_6\Phi_{1} + \partial_7\Phi_{8}) + \epsilon_0\,(t\,\partial_0 + \tfrac32H)\,\Phi_{8} = V\,\Phi_{16}
\end{aligned}
$$

In every component the gravitational term $\tfrac32He^{a_4}b_4^{-1/2}\,\Phi_B$ appears next to the hidden-direction derivative $e^{a_4}b_4^{-1/2}\tan z\,\partial_0\Phi_B$ of the same component $B$ ($\gamma^{(x_0)}$ is a permutation matrix with entries $+1$).

**Exact solutions used as test points.** They satisfy the field equation for all functions $a_4$ and $b_4$ and every real $z$; $K = \gamma^{(x_4)}\gamma^{(x_0)}$ ($K^2 = 1$) and $F = e^{a_4/2}b_4^{-1}$, whose logarithmic derivative is $-(u - \tfrac12a_4')$:

- $U = 0$, $m = 0$: $\Phi = F(\sin^2 z)^{\alpha/2}\big(\cosh I + \sinh I\,K\big)\chi$ with constant $\chi$ (16 free complex constants), $\alpha$ arbitrary and $I' = \tfrac32H(4\alpha + 1)e^{a_4}b_4^{-1/2}$.
- $U = 0$, $\alpha = -\tfrac14$ (then $I' = 0$), $m$ arbitrary: $\Phi = F(\sin^2 z)^{-1/8}\big(\cos(mx_4) - \sin(mx_4)\gamma^{(x_4)}\big)\chi$.
- Honest scope of these two families: their $x_0$ dependence is a real scalar factor, so $K_\mu = 0$ for $\mu \ne x_4$, and with the on-shell kinetic sum of section 8 the pressures vanish and $\rho = mS$ (zero for $m = 0$); they test the terms $e^{a_4}b_4^{-1/2}(\tan z\,\partial_0 + \tfrac32H)\gamma^{(x_0)}$ and $(u - \tfrac12a_4')\gamma^{(x_4)}$ but are a weak test of conservation; the general proof of conservation is the Noether identity of section 7.
- $U = \tfrac{\lambda}{2}S^2$, homogeneous (nonlinear): for every solution $\chi(x_4)$ of the system $\chi' = M\chi$, $M = -(m + \lambda e^{a_4}b_4^{-2}S_0)\gamma^{(x_4)} + \tfrac32He^{a_4}b_4^{-1/2}K$ with $S_0 = \chi^\dagger C\chi$, the field $\Phi = F\chi$ solves the field equation; $M^TC + CM = 0$, so $\chi^\dagger C\chi = S_0$ for all $x_4$, the system is linear once $S_0$ is fixed by $\chi(0)$, and $S = e^{a_4}b_4^{-2}S_0$; $\nabla_\mu T^\mu{}_\nu = 0$ for all $\nu$, and $\rho = mS + \lambda S^2/2$, $p = \lambda S^2/2$. The effective mass and the coefficient of $K$ depend on $x_4$, and there is no closed form in general.

| statement | Wolfram checks (theory) | sympy checks (theory) |
| --- | --- | --- |
| Euler-Lagrange equations derived from $\mathcal{L}$ | `EL_Psibar_C`, `EL_Psi_C` | `commuting_euler_lagrange_psibar_variation`, `commuting_euler_lagrange_psi_variation` |
| the adjoint equation is the Dirac conjugate | `adjoint_equation_is_Dirac_conjugate_C` | `commuting_adjoint_equation_is_conjugate` |
| explicit form, 16 components, chiral blocks | `Dirac_operator_explicit_C`, `block_form` | `commuting_euler_lagrange_psibar_variation` (the sympy field equation), compared term by term with `field_equation_components` and entry by entry with `field_equation_blocks` in the comparison record (section `comparison_with_wolfram` of the sympy report: 33 of 33 formula records and 65 of 65 check pairs agree) |
| evolution form | `evolution_form_C` | `hamiltonian_form_and_heisenberg_equation` |
| exact solutions | `solution_matrix_square`, `exact_solution_x4_x0_m0_C`, `exact_solution_x4_x0_quarter_C`, `exact_solution_nonlinear_homogeneous_C` | `exact_solution_family_x4_x0`, `exact_nonlinear_homogeneous_solution` |

## 6. Non-triviality [2]: theorem and proof

The author's requirement [2]: the Lagrangian of dirac16complex00 must be non-trivial, i.e. its Euler-Lagrange equations always possess nonzero contributions from gravity through the canonical spin connection unless the spacetime is flat 4+4, and they must be self-consistent, checked and verified.

**Theorem (NON-TRIVIALITY [2]).** Hypotheses: the corrected metric of section 1 with $H > 0$ and $z$ between degenerate points; $a_4$ and $b_4 > 0$ any differentiable functions of $x_4$ (a constant $a_4$ included; the identities hold for a constant $b_4$ as well, which section 1 excludes as a history); the diagonal vielbein of section 3 and its canonical spin connection; $\Phi$ the commuting 16-component field with the Lagrangian of section 4 and any real potential $U$. Then statements (1) to (4) hold. Statements (1) and (2) concern the diagonal vielbein and the field variables $\Phi$; statements (3) and (4) are the frame-independent content (see "Scope of [2]" below).

**(1) The gravitational term of the field equation.** The spin-connection part of the Euler-Lagrange operator is

$$
\gamma^\mu D_\mu\Phi - \gamma^\mu\partial_\mu\Phi = \gamma^\mu\Omega_\mu\,\Phi, \qquad \gamma^\mu\Omega_\mu = \tfrac32He^{a_4}b_4^{-1/2}\,\gamma^{(x_0)} + \big(u - \tfrac12a_4'\big)\,\gamma^{(x_4)} = c_g\,\gamma^{(x_0)} + v_g\,\gamma^{(x_4)} ,
$$

a matrix independent of $x_0$ for every real $z$, never zero for $H > 0$ (its $\gamma^{(x_0)}$ coefficient $c_g$ is positive). Since $\gamma^{(x_0)}$ and $\gamma^{(x_4)}$ anticommute, with squares $+1$ and $-1$,

$$
\big(\gamma^\mu\Omega_\mu\big)^2 = \big(\tfrac94H^2k - (u - \tfrac12a_4')^2\big)\,I_{16} ,
$$

so the term is nonzero for every $\Phi \ne 0$ wherever $c_g^2 \ne v_g^2$; on the background history $c_g = \tfrac32He^{Hx_4/3}$, $v_g = \tfrac56H$ and the square is $H^2\big(\tfrac94e^{2Hx_4/3} - \tfrac{25}{36}\big)I_{16} > 0$; where $c_g = \pm v_g$ the matrix is $c_g(\gamma^{(x_0)} \pm \gamma^{(x_4)})$, of rank 8, and annihilates an 8-dimensional subspace.

**(2) What each direction contributes.** Per direction (no sum)

$$
\begin{aligned}
\gamma^{x_0}\Omega_{x_0} &= \tfrac{h_4}{2}\,\gamma^{(x_4)}, \qquad \gamma^{x_i}\Omega_{x_i} = \tfrac{a_4'}{2}\,\gamma^{(x_4)} \qquad (i = x_1, x_2, x_3), \\
\gamma^{x_t}\Omega_{x_t} &= \tfrac{h_4}{2}\,\gamma^{(x_4)} + \tfrac{H}{2}e^{a_4}b_4^{-1/2}\,\gamma^{(x_0)} \qquad (t = x_5, x_6, x_7),
\end{aligned}
$$

and $\gamma^{x_4}\Omega_{x_4} = 0$. The $\gamma^{(x_4)}$ terms add to $\tfrac32a_4' + 4\cdot\tfrac{h_4}{2} = u - \tfrac12a_4'$: half the logarithmic rate of the 7-volume, $\tfrac12\partial_4\ln\sqrt{|g|}$; the hidden-direction ($\gamma^{(x_0)}$) terms of the three extra times add to $3 \cdot \tfrac{H}{2}e^{a_4}b_4^{-1/2} = c_g$. Unlike the metric of 2026-10-14, where the $a_4'$ terms cancelled, the term now sees the deflation of the block through $e^{a_4}b_4^{-1/2}$ and $h_4$.

**(3) It vanishes in no frame where the metric is curved.** $\Omega_\mu = 0$ for all $\mu$ if and only if $a_4' = 0$, $b_4' = 0$ and $H = 0$; $H = 0$ is a degenerate limit outside the family, so for every admissible metric the spin connection is nonzero in the diagonal frame. Whether a frame can remove it is decided by the curvature: $[D_\mu, D_\nu] = \tfrac12 R_{ab\mu\nu}S^{ab}$, so $\Omega_\mu$ vanishes in no frame wherever the Riemann tensor is nonzero, in particular on the background history; on the flat member $a_4 = 0$, $b_4 = H^2(x_4 - c)^2$ (and only where the metric is flat) it is a pure frame effect.

**(4) The vielbein in every derivative term.** Gravity also enters every derivative term,

$$
\gamma^\mu\partial_\mu = e^{a_4}b_4^{-1/2}\tan z\,\gamma^{(x_0)}\partial_0 + e^{-a_4}\gamma^{(x_i)}\partial_i + \gamma^{(x_4)}\partial_4 + e^{a_4}b_4^{-1/2}(\sin^2 z)^{-1/12}\gamma^{(x_t)}\partial_t
$$

(sums over $i$ and $t$), none of the factors being identically 1.

**Proof.** Step (a), the 3-space directions $i = x_1, x_2, x_3$: by section 3

$$
\gamma^{x_i} = e^{-a_4}\gamma^{(x_i)}, \qquad \Omega_{x_i} = \tfrac12 a_4'e^{a_4}\,\gamma^{(x_i)}\gamma^{(x_4)} .
$$

The scale factors cancel and $(\gamma^{(x_i)})^2 = \eta^{ii} = +1$, so $\gamma^{x_i}\Omega_{x_i} = \tfrac12a_4'\gamma^{(x_4)}$.

Step (b), the extra times $t = x_5, x_6, x_7$:

$$
\gamma^{x_t} = e^{a_4}b_4^{-1/2}(\sin^2 z)^{-1/12}\,\gamma^{(x_t)}, \qquad \Omega_{x_t} = \tfrac12(\sin^2 z)^{1/12}\,\big(h_4\,s_b\,\gamma^{(x_4)}\gamma^{(x_t)} + H\gamma^{(x_0)}\gamma^{(x_t)}\big) .
$$

With $\gamma^{(x_t)}\gamma^{(x_4)}\gamma^{(x_t)} = -\gamma^{(x_4)}(\gamma^{(x_t)})^2 = \gamma^{(x_4)}$ and likewise $\gamma^{(x_t)}\gamma^{(x_0)}\gamma^{(x_t)} = \gamma^{(x_0)}$ this gives $\gamma^{x_t}\Omega_{x_t} = \tfrac12e^{a_4}b_4^{-1/2}\big(h_4\,s_b\,\gamma^{(x_4)} + H\gamma^{(x_0)}\big)$, and $e^{a_4}b_4^{-1/2}s_b = 1$.

Step (c), the hidden direction: $\gamma^{x_0} = e^{a_4}b_4^{-1/2}\tan z\,\gamma^{(x_0)}$ and $\Omega_{x_0} = \tfrac12h_4\,s_b\cot z\,\gamma^{(x_0)}\gamma^{(x_4)}$, so $\gamma^{x_0}\Omega_{x_0} = \tfrac12h_4\gamma^{(x_4)}$; and $\Omega_{x_4} = 0$. Summing (a), (b) and (c) gives statements (1) and (2). Equivalently, since $\{\gamma^\mu, \Omega_\mu\} = 0$ for each $\mu$,

$$
\gamma^\mu\Omega_\mu = \frac{1}{2\sqrt{|g|}}\,\partial_\mu\big(\sqrt{|g|}\,e_a{}^\mu\big)\gamma^{(a)} ;
$$

only $\mu = x_0$ and $\mu = x_4$ contribute, with $\sqrt{|g|}\,e_{x_0}{}^{x_0} = \sigma_z b_4^{3/2}(\sin^2 z)^{1/4}$ and $e_{x_4}{}^{x_4} = 1$:

$$
\frac{1}{2\sqrt{|g|}}\,\partial_0\big(\sigma_z b_4^{3/2}(\sin^2 z)^{1/4}\big) = \tfrac32He^{a_4}b_4^{-1/2}, \qquad \frac{1}{2\sqrt{|g|}}\,\partial_4\sqrt{|g|} = u - \tfrac12a_4' .
$$

The square of statement (1) follows from $\{\gamma^{(x_0)}, \gamma^{(x_4)}\} = 0$.

Step (d): each of the 10 nonzero $\omega_{\mu ab}$ is $h_4$, $a_4'$ or $H$ times one of the factors $e^{a_4}$, $s_b\cot z$, $s_b(\sin^2 z)^{1/12}$, $(\sin^2 z)^{1/12}$, none of which vanishes between the degenerate points, and the $S^{ab}$ are linearly independent; the $x_4$-parts vanish if and only if $a_4$ and $e^{-a_4}b_4^{1/2}$ are constant, that is $a_4' = b_4' = 0$; with the $H$-part this gives the first sentence of statement (3); the rest follows from the integrability identity (section 7) and the flat member of section 3.

Step (e): statement (4) is the explicit form of section 5. Every step is verified exactly, for the author's T16 and, in the field-equations record, also for a second, independently built Clifford representation. $\square$

**Scope of [2] (exact).** The value $\gamma^\mu\Omega_\mu = c_g\gamma^{(x_0)} + v_g\gamma^{(x_4)}$ belongs to the diagonal vielbein and to the field variables $\Phi$:

- In another admissible vielbein of the same metric, the frame boosted in the $(x_4, x_0)$ plane, $e'^{(x_4)} = \cosh b\,e^{(x_4)} + \sinh b\,e^{(x_0)}$, $e'^{(x_0)} = \sinh b\,e^{(x_4)} + \cosh b\,e^{(x_0)}$ with rapidity $b = \beta x_4 + b_0$, its canonical connection gives $\gamma'^\mu\Omega'_\mu = (c_g - \tfrac{\beta}{2})(\cosh b\,\gamma^{(x_0)} - \sinh b\,\gamma^{(x_4)}) + v_g\,(\cosh b\,\gamma^{(x_4)} - \sinh b\,\gamma^{(x_0)})$. A rapidity with $b' = 2c_g$ removes the $c_g$ part identically, for every $H > 0$, $a_4$ and $b_4$; for any rapidity function the coefficients satisfy $\cosh b\,c_4 + \sinh b\,c_0 = v_g$, so no boost in this plane removes the term unless $b_4'/b_4 = a_4'/2$.
- Within the diagonal frame the rescaling $\Phi = e^{a_4/2}b_4^{-1}(\sin^2 z)^{-1/8}\chi$ removes the term exactly: $\gamma^\mu D_\mu\Phi = e^{a_4/2}b_4^{-1}(\sin^2 z)^{-1/8}\gamma^\mu\partial_\mu\chi$, so for $U = 0$ the equation for $\chi$ has no spin-connection term, and for $U = \tfrac{\lambda}{2}S^2$ the term becomes the $x_0$- and $x_4$-dependent coupling $\lambda e^{a_4}S[\chi]/(b_4^2|\sin z|^{1/2})$. The exact family of section 5 shows this: $\alpha = -\tfrac14$ gives $I' = 0$, no $H$ term.
- The canonical connection drops out of $\mathcal{L}$ (section 4), so the Euler-Lagrange equations are those of the connection-free symmetric Lagrangian. Unlike the metric of 2026-10-14, the term sees the hidden block: its $\gamma^{(x_0)}$ coefficient is $\tfrac32H$ times the inverse scale factor $e^{a_4}b_4^{-1/2}$ of the block, which grows as the block deflates.
- What cannot be removed in any frame where the metric is curved is $\Omega_\mu$ itself (its curvature is the Riemann tensor; on the boosted frame the spinor curvature component $F'_{x_5x_0}$ is nonzero for general $a_4$, $b_4$), together with the frame factors $e^{-a_4}$, $e^{a_4}b_4^{-1/2}(\sin^2 z)^{-1/12}$ and $e^{a_4}b_4^{-1/2}\tan z$ of the derivative terms: this is the frame-independent content of [2]. In the diagonal frame the connection also enters the energy-momentum tensor: for a homogeneous configuration the connection part of $K^{x_4}{}_{x_1}$ vanishes (3-space does not depend on $x_0$), but that of $K^{x_4}{}_{x_5}$ is $\tfrac12H(\sin^2 z)^{1/12}\,\bar\Phi\gamma^{(x_4)}\gamma^{(x_0)}\gamma^{(x_5)}\Phi$, not identically zero.
- Interpretation (labelled): in the quantum theory of dirac16complex the term $\tfrac32He^{a_4}b_4^{-1/2}\gamma^{(x_0)}$ makes the hidden-direction operator $e^{a_4}b_4^{-1/2}(\tan z\,\partial_0 + \tfrac32H)\gamma^{(x_0)}$ antisymmetric for the measure $\sqrt{|g|}/f_{x_0}\,dx_0 = b_4^{3/2}(\sin^2 z)^{1/4}dx_0$ in the variables $\Psi$, up to a boundary term that vanishes where $\sin z = 0$ but not where $\cos z = 0$, and the term $v_g\gamma^{(x_4)}$ compensates the $x_4$ dependence of the measure; in the variables $\chi$ no such term is needed. This role therefore depends on the variables and the measure.

| statement | Wolfram checks | sympy checks |
| --- | --- | --- |
| (1) $\gamma^\mu\Omega_\mu = c_g\gamma^{(x_0)} + v_g\gamma^{(x_4)}$ and its square | `nontriviality_2_dirac16complex00`, `gammaOmega_total` (theory); `gravity_term_gamma_mu_Omega_mu` ($a_4$ record) | `gamma_mu_Omega_mu_equals_hidden_block_terms`, `gravity_term_square` (theory); `ownrep_gravity_term`, `authorT16_gravity_term` ($a_4$ record) |
| (2) the contribution of each direction | `gammaOmega_per_direction`, `gammaOmega_divergence_form` | `per_direction_terms`, `divergence_of_sqrtg_gamma` |
| (3) $\Omega_\mu = 0$ only for $a_4' = b_4' = 0$ and $H = 0$; removable only where flat | `Omega_vanishes_iff_a4prime_b4prime_and_H_vanish`, `flat_member_and_curvature`, `spin_curvature_equals_Riemann` | `nontriviality_Omega_zero_iff_flat`, `curvature_and_flat_member`, `spinor_curvature_equals_riemann` |
| (4) explicit operator | `Dirac_operator_explicit_C` | |
| the same terms in the quantum theory of dirac16complex (up to a boundary term) | `good_sector_hermiticity_curved`, `good_sector_hermiticity_up_to_the_brane_flux` (scope) | `good_sector_hermiticity_up_to_the_brane_flux` (scope) |
| scope: the boosted frame removes the $c_g$ part of $\gamma^\mu\Omega_\mu$, not its $v_g$ part and not $\Omega_\mu$ | `boosted_frame_reproduces_metric`, `boosted_frame_canonical_connection`, `boosted_frame_gammaOmega_formula`, `boosted_frame_removes_only_the_H_term`, `boosted_frame_curvature_nonzero` (scope) | the same five names (scope) |
| scope: rescaling, the hidden block, energy-momentum tensor | `rescaling_removes_the_connection_term`, `rescaled_equation_quadratic_potential`, `gammaOmega_sees_the_hidden_block`, `spin_connection_in_the_energy_momentum_tensor` (scope) | the same four names (scope) |

## 7. Self-consistency of the field equations

All statements are exact and verified for the commuting field, for general $a_4$ and $b_4$ and every real $z$.

**Reality and derivation.** $\mathcal{L}$ is real; the Euler-Lagrange equations derived from it are the field equation and its Dirac conjugate (sections 4 and 5).

**Integrability of the connection.** For all 28 pairs,

$$
[D_\mu, D_\nu]\Phi = \big(\partial_\mu\Omega_\nu - \partial_\nu\Omega_\mu + [\Omega_\mu, \Omega_\nu]\big)\Phi = \tfrac12 R_{ab\mu\nu}S^{ab}\Phi .
$$

**Second-order consistency (Lichnerowicz identity).** Identically for a general field,

$$
(\gamma^\mu D_\mu)^2\Phi = g^{\mu\nu}\big(D_\mu D_\nu - \Gamma^\lambda{}_{\mu\nu}D_\lambda\big)\Phi - \frac{R}{4}\,\Phi, \qquad R = -12H^2k + 8(a_4')^2 - 2a_4'' - 8a_4'u + 4\frac{b_4''}{b_4} + u^2,
$$

and $\gamma^\mu\gamma^\nu F_{\mu\nu} = -\tfrac{R}{2}$ for the spinor curvature $F_{\mu\nu} = [D_\mu, D_\nu]$.

**Cauchy problem.** The equation is first order in $x_4$ with non-characteristic slices (evolution form, section 5). This does not make the Cauchy problem well posed, and it is not listed here as a self-consistency property: for data that depend on the extra times the growth rates of the modes have no upper bound (with frozen coefficients $k_5 = K$ gives the rate $\sqrt{K^2 - m^2 - k_0^2 - k_1^2 - k_2^2 - k_3^2}$; Hadamard ill-posedness), and in the good sector, without a boundary condition at the degenerate points, the $x_0$-independent modes grow wherever $m^2 < c_g^2$ (for $U = 0$; on these modes $\Phi = e^{a_4/2}b_4^{-1}\chi$, and the matrix $A = -im\gamma^{(x_4)} + ic_g\gamma^{(x_4)}\gamma^{(x_0)}$ of the evolution of $\chi$ has the square $(m^2 - c_g^2)I_{16}$); on the background history $c_g = \tfrac32He^{Hx_4/3}$ grows, so every mass falls below it at late $x_4$.

**Conserved current.** $J^\mu = -i\bar\Phi\gamma^\mu\Phi$ is real, and off shell

$$
\partial_\mu\big(\sqrt{|g|}\,J^\mu\big) = -i\sqrt{|g|}\,\big(\bar E\Phi + \bar\Phi E\big),\qquad \sqrt{|g|} = e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4},
$$

with $E = \gamma^\mu D_\mu\Phi - (m + U'(S))\Phi$ and $\bar E = (D_\mu\bar\Phi)\gamma^\mu + (m + U'(S))\bar\Phi$ (the convention of the Wolfram record), so $\nabla_\mu J^\mu = 0$ on shell. The charge density is $J^{x_4} = \Phi^\dagger B\Phi$, and the charge of a slice of constant $x_4$, $Q = \int\sqrt{|g|}\,\Phi^\dagger B\Phi\,d^7x$, is an indefinite form ($B$ has signature (8,8)). Only the local law is established: $Q$ is constant in $x_4$ only if no charge flows through the boundary of the slice, and at the degenerate points $z = \pi/2 + n\pi$ the flux term $\sigma_z b_4^{3/2}(\sin^2 z)^{1/4}\,u^\dagger M_0 v$ of the hidden direction does not vanish in general (`good_sector_hermiticity_up_to_the_brane_flux`, both engines). This record imposes no boundary condition there (section 15); a constant total charge is an ASSUMED no-flux condition.

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

and on shell the variation tensor is symmetric and equals it (section 7; independently, with all 64 components of a first-order vielbein variation around the metric, the variation tensor equals the Belinfante tensor on shell for 64 of 64 components). The normalisation is $\delta S_{\mathrm{act}} = \tfrac12\int\sqrt{|g|}\,T^{\mu\nu}\delta g_{\mu\nu}$.

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
K_{x_i} &= \tfrac12 e^{-a_4}\big(\bar\Phi\gamma^{(x_i)}\partial_i\Phi - \partial_i\bar\Phi\,\gamma^{(x_i)}\Phi\big), \qquad K_{x_4} = \tfrac12\big(\bar\Phi\gamma^{(x_4)}\partial_4\Phi - \partial_4\bar\Phi\,\gamma^{(x_4)}\Phi\big), \\
K_{x_t} &= \tfrac12 e^{a_4}b_4^{-1/2}(\sin^2 z)^{-1/12}\big(\bar\Phi\gamma^{(x_t)}\partial_t\Phi - \partial_t\bar\Phi\,\gamma^{(x_t)}\Phi\big), \\
K_{x_0} &= \tfrac12 e^{a_4}b_4^{-1/2}\tan z\,\big(\bar\Phi\gamma^{(x_0)}\partial_0\Phi - \partial_0\bar\Phi\,\gamma^{(x_0)}\Phi\big),
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

**The $x_4$-$x_0$ component** ($\Omega_{x_4} = 0$; $\Omega_{x_0}$ drops out):

$$
\begin{aligned}
& T^{x_4}{}_{x_0} = -\tfrac14\big(B_{40} - e^{-a_4}b_4^{1/2}\cot z\,B_{04}\big), \qquad T^{x_0}{}_{x_4} = -e^{2a_4}b_4^{-1}\tan^2 z\;T^{x_4}{}_{x_0}, \\
& B_{40} = \bar\Phi\gamma^{(x_4)}\partial_0\Phi - \partial_0\bar\Phi\,\gamma^{(x_4)}\Phi, \qquad B_{04} = \bar\Phi\gamma^{(x_0)}\partial_4\Phi - \partial_4\bar\Phi\,\gamma^{(x_0)}\Phi .
\end{aligned}
$$

On homogeneous on-shell states both $T^{x_4}{}_{x_0}$ and $T^{x_0}{}_{x_4}$ vanish identically. The field equations of section 11 require every off-diagonal component of the source to vanish; for the homogeneous condensate 36 off-diagonal kinetic components are nonzero bilinears in general, and their vanishing is a separate condition on the state (section 12).

**Trace.** Off shell (an exact identity in both engines) $T^\mu{}_\mu = 8L_0 - \sum_\mu K_\mu = 7\sum_\mu K_\mu - 8(mS + U)$. Exactly, $\sum_\mu K_\mu = (m + U')S + \tfrac12(\bar\Phi E - \bar E\Phi)$, so on shell $\sum_\mu K_\mu = (m + U'(S))S$, $L_0 = S\,U'(S) - U(S)$ and

$$
T^\mu{}_\mu = -mS + 7S\,U'(S) - 8U(S) = -mS + 3\lambda S^2 \quad (U = \tfrac{\lambda}{2}S^2) .
$$

**Conservation and energy exchange.** For a diagonal tensor

$$
T = \mathrm{diag}(p_0, p_3, p_3, p_3, -\rho, p_t, p_t, p_t)(x_0, x_4)
$$

whose entries are functions of $x_0$ and $x_4$, all eight components of the divergence are (every real $z$; $\sigma_z$ cancels)

$$
\nabla_\mu T^\mu{}_{x_4} = -\partial_4\rho - 3a_4'(\rho + p_3) - 3h_4(\rho + p_t) - h_4(\rho + p_0), \qquad \nabla_\mu T^\mu{}_{x_0} = \partial_0 p_0 + 3H\cot z\,(p_0 - p_t),
$$

and $\nabla_\mu T^\mu{}_\nu = 0$ identically for $\nu = x_1, x_2, x_3, x_5, x_6, x_7$. Conservation is therefore exactly $\partial_4\rho = -3a_4'(\rho + p_3) - 3h_4(\rho + p_t) - h_4(\rho + p_0)$ and $\partial_0 p_0 = -3H\cot z\,(p_0 - p_t)$; for a homogeneous tensor (entries functions of $x_4$ only) it gives

$$
\frac{d\rho}{dx_4} = -3\,a_4'\,(\rho + p_3) - 4\,h_4\,(\rho + p_t), \qquad p_0 = p_t :
$$

the 3-space volume $e^{3a_4}$ dilutes $\rho + p_3$, and the block of the hidden direction and the extra times, whose volume changes with the rate $4h_4$, dilutes $\rho + p_t$.

| statement | Wolfram checks (theory) | sympy checks (theory) |
| --- | --- | --- |
| variation tensor in closed form | `T_vielbein_variation_closed_form_C` | `commuting_emt_equals_general_vielbein_variation_on_shell` |
| Belinfante tensor, symmetric | `T_symmetric_part_Belinfante_C` | `commuting_emt_symmetric` |
| normalisation $\delta S_{\mathrm{act}} = \tfrac12\int\sqrt{\lvert g\rvert}\,T^{\mu\nu}\delta g_{\mu\nu}$, diagonal components | `T_diagonal_components_C` | `commuting_emt_equals_vielbein_variation_diagonal` |
| $x_4$-$x_0$ component | `T_x4_x0_component_C` | `commuting_T_x4x0_homogeneous` |
| trace, on-shell kinetic sum | `EMT_trace_C`, `kinetic_sum_on_shell_C` | `commuting_trace_on_shell` |
| energy exchange with the rate $h_4$ and the $x_0$ condition | `energy_exchange_equation` | `energy_exchange_equation` |

## 9. Kinetic energy, potential energy, energy density and pressures

**Split.** $T^\nu{}_\mu = T_{\mathrm{kin}}{}^\nu{}_\mu + T_{\mathrm{pot}}{}^\nu{}_\mu$ with the potential part and the kinetic (derivative) part

$$
\begin{aligned}
T_{\mathrm{pot}}{}^\nu{}_\mu &= -\delta^\nu_\mu\,\big(mS + U(S)\big), \\
T_{\mathrm{kin}}{}^\nu{}_\mu &= \delta^\nu_\mu\sum_\lambda K_\lambda - \tfrac14\big(\bar\Phi\gamma^\nu D_\mu\Phi - D_\mu\bar\Phi\,\gamma^\nu\Phi + \bar\Phi\gamma_\mu D^\nu\Phi - D^\nu\bar\Phi\,\gamma_\mu\Phi\big)
\end{aligned}
$$

(formula `EMT_kinetic_potential` of `Revision/theory/field-theory.json`, compared with the sympy split).

**Densities** (per unit proper 7-volume; the energy in a region of a slice $x_4 = \mathrm{const}$ is the integral with the weight $\sqrt{|g|} = e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}$):

| quantity | kinetic part | potential part | total |
| --- | --- | --- | --- |
| energy density $\rho = -T^{x_4}{}_{x_4}$ | $-\sum_{\mu \ne x_4} K_\mu$ | $mS + U(S)$ | $-\sum_{\mu \ne x_4} K_\mu + mS + U$ |
| 3-space pressure $p_3 = T^{x_1}{}_{x_1}$ | $\sum_{\mu \ne x_1} K_\mu$ | $-(mS + U)$ | $\sum_{\mu \ne x_1} K_\mu - mS - U$ |
| extra-time pressure $p_t = T^{x_5}{}_{x_5}$ | $\sum_{\mu \ne x_5} K_\mu$ | $-(mS + U)$ | $\sum_{\mu \ne x_5} K_\mu - mS - U$ |
| hidden-direction pressure $p_0 = T^{x_0}{}_{x_0}$ | $\sum_{\mu \ne x_0} K_\mu$ | $-(mS + U)$ | $\sum_{\mu \ne x_0} K_\mu - mS - U$ |

**Homogeneous states on shell** ($\Phi$ depending on $x_4$ only): $K_\mu = 0$ for $\mu \ne x_4$ and $K_{x_4} = (m + U'(S))S$ (the scalar factor $e^{a_4/2}b_4^{-1}$ of $\Phi$ and $\bar\Phi$ cancels in $K_{x_4}$). So the kinetic energy density vanishes, $-T_{\mathrm{kin}}{}^{x_4}{}_{x_4} = 0$, the kinetic pressure is $(m + U'(S))S$ in every direction, and

$$
\rho = m S + U(S), \qquad p_3 = p_t = p_0 = S\,U'(S) - U(S) ;
$$

for $U = \tfrac{\lambda}{2}S^2$: $\rho = mS + \tfrac{\lambda}{2}S^2$ and $p = \tfrac{\lambda}{2}S^2$ (formula `EMT_homogeneous_on_shell` of `Revision/theory/field-theory.json`; the exact nonlinear solutions of section 5 realise these values). Along a homogeneous solution $e^{-a_4}b_4^{2}S = S_0$ is constant, $S = e^{a_4}b_4^{-2}S_0$: $S$, $\rho$ and $p$ follow the inverse 7-volume, consistent with the energy exchange of section 8, $d\rho/dx_4 = (m + \lambda S)\,dS/dx_4 = -(2u - a_4')(mS + \lambda S^2) = -(3a_4' + 4h_4)(\rho + p)$.

**Sign of the energy (exact).** The classical energy of dirac16complex00 is unbounded below already for $U = 0$ in the good sector. In the flat frame with $m = 2$ and $(k_0, k_1, k_2, k_3) = (4, 1, 2, 0)$, $E = 5$, the one-particle generator commutes with $B$ and its $E = 5$ eigenspace (dimension 8) contains vectors $u_\pm$ with $Bu_- = -u_-$ and $Bu_+ = +u_+$; the positive-frequency solutions $\Phi = c\,u_\pm\,e^{i(k\cdot x - 5x_4)}$ ($|u_\pm| = 1$) have the energy density $\rho = -T^{x_4}{}_{x_4} = -5|c|^2$ and $+5|c|^2$ and the charge density $\Phi^\dagger B\Phi = -|c|^2$ and $+|c|^2$ (`commuting_field_energy_unbounded_below`, both engines). By the Krein-inertia theorem of the pairing record (every real-frequency eigenspace has inertia (4,4), `Q_one_particle_Krein_inertia_real_frequencies`) such negative-energy modes exist at every real frequency. In the primordial field the homogeneous solutions of section 5 have $\rho = mS + \tfrac{\lambda}{2}S^2$ with $S = e^{a_4}b_4^{-2}S_0$ and $S_0 = \chi^\dagger C\chi$ of either sign. dirac16complex00 therefore has a negative-energy (ghost-like) sector at positive frequency, the classical form of the spin-statistics problem of a commuting field with a first-order Lagrangian; this matters for any reading of Hypothesis00, for example a phantom $w < -1$.

| statement | Wolfram checks | sympy checks |
| --- | --- | --- |
| homogeneous on-shell $\rho$, $p$; kinetic and potential parts | `exact_solution_nonlinear_homogeneous_C` (theory) | `commuting_homogeneous_on_shell_rho_p` (theory) |
| $e^{-a_4}b_4^2S$ constant along $x_4$ for a homogeneous solution | `condensate_S_law` ($a_4$ record) | `ownrep_condensate_S_law`, `authorT16_condensate_S_law` ($a_4$ record) |
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

For $\lambda = 0$ the homogeneous state has $p = 0$ and $w = 0$. For $\lambda \ne 0$ the ratio drifts, because $S = e^{a_4}b_4^{-2}S_0$; on the background history $e^{a_4}b_4^{-2} \propto e^{-(5/3)a_4}$, so $\lambda S/m \propto e^{-(5/3)a_4}$.

| statement | source |
| --- | --- |
| definitions and homogeneous values of $w_3$, $w_t$, $w_{x_0}$ | formula `equation_of_state_definitions` of `Revision/theory/field-theory.json`; sympy check `commuting_homogeneous_on_shell_rho_p` |

Not computed in this document: the equation of state that a 3-space observer infers (after integrating over the hidden direction and the extra times), its time dependence as the block deflates, CPL parameters, and any comparison with supernova data. These belong to the dark-sector investigation of Hypothesis00 (SPEC section 8), the separate Revision record `Revision/docs/DARK_SECTOR_HYPOTHESES`.

**The verdict of the dark-sector record for dirac16complex00 (Hypothesis00; a summary, every number from its reports, on the background history of the corrected metric).** The equation of state that a 3-space observer infers is not fixed by the field equations alone: the 4-dimensional density needs an ASSUMPTION about how the observer normalises over the hidden direction and the extra times, and the two normalisations of the dirac16complex00 record (N1, per unit coordinate volume of the extra times and the hidden direction, and N2, per unit proper 7-volume) are related by $w_{\rm eff}(N2) = w_{\rm eff}(N1) - (4 - 2\beta)/3$ with $\beta = d\ln b_4/da_4 = \tfrac43$, so they differ by exactly $-4/9$ on the history (`observer_N1_weff_identity`, `observer_N2_weff_identity`). Dark energy: not with positive energies; positive-energy content with real frequencies has $w_{\rm eff}(N2) \geq -4/9$ (`positive_models_bounded_by_minus_four_ninths`): the gas M2 of good-sector modes, whose physical parameter was CHOSEN on the withdrawn $b_4 = 1$ record to give $w_0 = -0.861$, has the tangent $(-2749/9000, 81037/500000)$, freezing (`M2_tangent_exact`), the extra-time mode M3 the thawing-sign tangent $(-3583/9000, -196963/4500000)$ (`M3_tangent_exact`), and the model M4, whose two parameters were CHOSEN on the withdrawn record to reproduce the Unite CPL tangent $(w_0, w_a) = (-0.861, -0.60)$, has on this history the tangent $(-0.398111111111, -0.0666666666667)$ (`M4_former_tuning_on_the_history`); for M3 and M4 the bound holds before the turning point $a_*$ of the extra-time mode (M3: $a_* = 6.2640$, M4: $a_* = 1.8859$), past which the mode grows, its frequency is imaginary and the bound is not established. The Unite $w_0$ needs a component of negative classical energy larger than the positive energy, $G \geq 3749/3000$ (`unite_w0_requires_dominant_ghost`), and the composition M5 with a ghost-like component has on this history the CPL fit $(-0.443790594178, -0.32308292878)$ over $a \in [1/2, 1]$ and does not cross $w = -1$ on $[1/3, 1]$ (`M5_former_composition_on_the_history`). The Unite constant $w = -0.764$ is the ratio of a condensate only at one instant and only for the tuned value $\lambda S/m = -382/441$ (`condensate_ratio_equals_unite_constant_w`), where the drifting ratio has $w_a = -28077/12500 = -2.24616$, the thawing sign (`condensate_ratio_drift_at_unite_value`); it is phantom exactly while $\lambda S/m \in (-2, -1)$ (`condensate_phantom_interval`), and the observer reads $w_{\rm eff}(N1) = \tfrac59w$ and $w_{\rm eff}(N2) = \tfrac59w - \tfrac49$ (`condensate_observer`). No condensate is the source of the background history: the history needs the anisotropic source of section 11, $\kappa(p_3 - p_0) = -\tfrac{9}{16}k^2 + \tfrac{1069}{432}k + \tfrac{2015}{972}$, while every condensate has equal pressures, and its $S \propto e^{-(5/3)a_4}$ decays while the required source grows (`history_required_source`, `condensate_cannot_source_history`). A model with as many tuned parameters as matched numbers reproduces them by construction and is not a prediction; on this history the tuned models of the withdrawn record no longer reproduce the Unite numbers. That record establishes neither Hypothesis nor Hypothesis00; it states what each field can and cannot produce under its stated assumptions.

## 11. The field equations for a4[x4] and b4[x4]

**Einstein-Lovelock equations** (SPEC section 5):

$$
\sum_{k=1}^{3}\alpha_k\,E_{(k)}{}^\mu{}_\nu + \Lambda\,\delta^\mu_\nu = \kappa\,T^\mu{}_\nu, \qquad E_{(k)} = -\frac{P_{(k)}}{2^{k+1}}, \qquad E_{(1)} = G ,
$$

with $P_{(k)}{}^h{}_j$ the Lovelock tensors computed with the generalized Kronecker delta (GKD) from the Riemann tensor (MTW convention). $P_{(4)}$ vanishes in 8 dimensions (a GKD with 9 indices over 8 values), so $k = 1, 2, 3$ is the complete series. The components computed directly from the curvature equal the GKD record `Revision/gkd_lovelock/results/lovelock-tensors.json` monomial by monomial, for general $a_4$ and $b_4$. Every mixed Riemann component $R^{ab}{}_{cd}$ is free of $x_0$ and sectional ($\{c, d\} = \{a, b\}$: 28 planes), so every component of $E_{(k)}$ is a polynomial in $H$, $a_4'$, $a_4''$, $u$, $v$ and $k = e^{2a_4}/b_4$ ($k$ enters through the curvature $-H^2k$ of the block of the hidden direction and the extra times; $a_4$ and $b_4$ themselves enter only through $k$).

**The Lovelock components.** Every $E_{(k)}$ is diagonal (all 56 off-diagonal components vanish identically), with $x_1 = x_2 = x_3$ and $x_0 = x_5 = x_6 = x_7$: $E_{(k)}{}^{x_5}{}_{x_5} = E_{(k)}{}^{x_0}{}_{x_0}$ for $k = 1, 2, 3$. The independent components (the TeX of `Revision/field_equations_a4/a4-equations.json`, key `lovelockTensors`):

$$
\begin{aligned}
E_{(1)}{}^{x_0}{}_{x_0} &= -3 (a_4')^2+\frac{3 (a_4') u}{2}+3 H^2 k-\frac{3 u^2}{2}-\frac{3 v}{2}, \\
E_{(1)}{}^{x_1}{}_{x_1} &= -5 (a_4')^2+6 (a_4') u+2 a_4''+6 H^2 k-\frac{5 u^2}{2}-2 v, \\
E_{(1)}{}^{x_4}{}_{x_4} &= 3 (a_4')^2+6 H^2 k-\frac{3 u^2}{2}.
\end{aligned}
$$

$$
\begin{aligned}
E_{(2)}{}^{x_0}{}_{x_0} &= 12 (a_4')^4-12 (a_4')^3 u+48 (a_4')^2 H^2 k+18 (a_4')^2 u^2 \\
&\quad +12 (a_4')^2 v+24 (a_4') a_4'' u+6 (a_4') H^2 k u-\frac{15 (a_4') u^3}{2} \\
&\quad -12 (a_4') u v+24 a_4'' H^2 k-6 a_4'' u^2+3 H^2 k u^2 \\
&\quad +6 H^2 k v-\frac{3 u^4}{4}-\frac{3 u^2 v}{2}, \\
E_{(2)}{}^{x_1}{}_{x_1} &= 28 (a_4')^4-48 (a_4')^3 u-48 (a_4')^2 a_4''+48 (a_4')^2 H^2 k \\
&\quad +20 (a_4')^2 u^2+16 (a_4')^2 v+32 (a_4') a_4'' u-24 (a_4') H^2 k u \\
&\quad +6 (a_4') u^3-12 H^4 k^2+18 H^2 k u^2+24 H^2 k v \\
&\quad -\frac{15 u^4}{4}-6 u^2 v, \\
E_{(2)}{}^{x_4}{}_{x_4} &= -36 (a_4')^4-48 (a_4')^2 H^2 k+36 (a_4')^2 u^2+48 (a_4') H^2 k u \\
&\quad -12 (a_4') u^3-12 H^4 k^2+6 H^2 k u^2-\frac{3 u^4}{4}.
\end{aligned}
$$

$$
\begin{aligned}
E_{(3)}{}^{x_0}{}_{x_0} &= -72 (a_4')^6+108 (a_4')^5 u-216 (a_4')^4 H^2 k-216 (a_4')^4 u^2 \\
&\quad -108 (a_4')^4 v-432 (a_4')^3 a_4'' u+108 (a_4')^3 H^2 k u+171 (a_4')^3 u^3 \\
&\quad +216 (a_4')^3 u v-432 (a_4')^2 a_4'' H^2 k+324 (a_4')^2 a_4'' u^2+54 (a_4')^2 H^2 k u^2 \\
&\quad +108 (a_4')^2 H^2 k v-\frac{81 (a_4')^2 u^4}{2}-81 (a_4')^2 u^2 v+216 (a_4') a_4'' H^2 k u \\
&\quad -54 (a_4') a_4'' u^3, \\
E_{(3)}{}^{x_1}{}_{x_1} &= -216 (a_4')^6+432 (a_4')^5 u+720 (a_4')^4 a_4''-144 (a_4')^4 H^2 k \\
&\quad -180 (a_4')^4 u^2-144 (a_4')^4 v-576 (a_4')^3 a_4'' u+144 (a_4')^3 H^2 k u \\
&\quad -108 (a_4')^3 u^3-216 (a_4')^2 H^4 k^2-180 (a_4')^2 H^2 k u^2-144 (a_4')^2 H^2 k v \\
&\quad +\frac{189 (a_4')^2 u^4}{2}+108 (a_4')^2 u^2 v-288 (a_4') a_4'' H^2 k u+72 (a_4') a_4'' u^3 \\
&\quad +72 (a_4') H^2 k u^3+144 (a_4') H^2 k u v-18 (a_4') u^5-36 (a_4') u^3 v \\
&\quad -144 a_4'' H^4 k^2+72 a_4'' H^2 k u^2-9 a_4'' u^4, \\
E_{(3)}{}^{x_4}{}_{x_4} &= 360 (a_4')^6+432 (a_4')^4 H^2 k-540 (a_4')^4 u^2-864 (a_4')^3 H^2 k u \\
&\quad +360 (a_4')^3 u^3-216 (a_4')^2 H^4 k^2+324 (a_4')^2 H^2 k u^2-\frac{135 (a_4')^2 u^4}{2}.
\end{aligned}
$$

Each $E_{(k)}$ is divergence-free, and $\sum_h P_{(k)}{}^h{}_h = (8 - 2k)L_{(k)}$.

**The independent equations for a general source** $T = \mathrm{diag}(p_0, p_3, p_3, p_3, -\rho, p_t, p_t, p_t)$:

- constraint ($x_4$, first order: it contains $a_4'$, $u$ and $k$, but neither $a_4''$ nor $v$): $\sum_k\alpha_k E_{(k)}{}^{x_4}{}_{x_4} + \Lambda = -\kappa\rho$;
- 3-space ($x_1 = x_2 = x_3$): $\sum_k\alpha_k E_{(k)}{}^{x_1}{}_{x_1} + \Lambda = \kappa p_3$;
- hidden direction and extra times ($x_0 = x_5 = x_6 = x_7$): $\sum_k\alpha_k E_{(k)}{}^{x_0}{}_{x_0} + \Lambda = \kappa p_0 = \kappa p_t$;
- off-diagonal: $0 = \kappa T^\mu{}_\nu$ for every $\mu \ne \nu$ (the left-hand sides vanish identically); in particular $T^{x_4}{}_{x_0} = T^{x_0}{}_{x_4} = 0$.

The field equations therefore have three independent components ($x_4$, $x_1$, $x_0$); they require $p_0 = p_t$ and a source without off-diagonal components (unlike the metric of 2026-10-14, whose Lovelock tensors had an off-diagonal pair $E^{x_4}{}_{x_0} \propto \cot z\,u$).

**The second-order equations.** The $x_1$ and $x_0$ components are linear in $(a_4'', v)$, with a Jacobian whose determinant is $-3/b_4$ in Einstein gravity (in the variables $(a_4'', b_4'')$); where it does not vanish they determine $a_4''$ and $v = (b_4'/b_4)'$ from the source, and the $x_4$ component is the constraint.

**Consistency conditions.**

- $x_0$-dependence: the left-hand sides are free of $x_0$, so every diagonal component of the source must be a function of $x_4$ alone.
- Isotropy: since the left-hand sides of $x_1, x_2, x_3$ coincide (and those of $x_0, x_5, x_6, x_7$), the source must have $T^{x_1}{}_{x_1} = T^{x_2}{}_{x_2} = T^{x_3}{}_{x_3}$ and $T^{x_0}{}_{x_0} = T^{x_5}{}_{x_5} = T^{x_6}{}_{x_6} = T^{x_7}{}_{x_7}$.
- Conservation (with $q_{40} = T^{x_4}{}_{x_0}$ and $q_{04} = T^{x_0}{}_{x_4}$ kept for the identity): $\nabla_\mu T^\mu{}_{x_4} = -\partial_4\rho - 3a_4'(\rho + p_3) - 3h_4(\rho + p_t) - h_4(\rho + p_0) + \partial_0 q_{04} - 3H(\cot z + 2\tan z)\,q_{04}$ and $\nabla_\mu T^\mu{}_{x_0} = \partial_0 p_0 + 3H\cot z\,(p_0 - p_t) + \partial_4 q_{40} + \tfrac32u\,q_{40} - h_4\cot^2 z\,q_{04}/k$.
- Constraint propagation: $\tfrac{d}{dx_4}\sum_k\alpha_k E_{(k)}{}^{x_4}{}_{x_4} = 3a_4'\sum_k\alpha_k(E^{x_1}{}_{x_1} - E^{x_4}{}_{x_4}) + 4h_4\sum_k\alpha_k(E^{x_0}{}_{x_0} - E^{x_4}{}_{x_4})$ identically ($k' = k(2a_4' - u)$): with the conservation law the derivative of the constraint follows from the other components.

**Einstein gravity** ($\alpha_1 = 1$, $\alpha_2 = \alpha_3 = 0$):

$$
\begin{aligned}
& 3 (a_4')^2+6 H^2 k+\Lambda-\frac{3 u^2}{2} = -\kappa  \rho, \\
& -5 (a_4')^2+6 (a_4') u+2 a_4''+6 H^2 k+\Lambda-\frac{5 u^2}{2}-2 v = \kappa  p_3, \\
& -3 (a_4')^2+\frac{3 (a_4') u}{2}+3 H^2 k+\Lambda-\frac{3 u^2}{2}-\frac{3 v}{2} = \kappa  p_0 \quad (x_0 = x_5 = x_6 = x_7), \\
& \kappa  (p_0+\rho ) = -\frac{3}{2} \left(4 (a_4')^2-(a_4') u+2 H^2 k+v\right), \\
& \kappa  (p_3+\rho ) = -8 (a_4')^2+6 (a_4') u+2 a_4''-u^2-2 v.
\end{aligned}
$$

The flat member $a_4 = 0$, $b_4 = H^2(x_4 - c)^2$ solves the vacuum equations with $\Lambda = 0$. No exponential history (below) is a vacuum solution, for any $\Lambda$: the vacuum equations have no real solution with $k > 0$.

**Exponential histories** $a_4 = A H x_4 + a_0$, $b_4 = b_4(0)e^{\beta AHx_4}$ ($a_4' = AH$, $u = \beta AH$, $a_4'' = v = 0$; 3-space scale factor $e^{AHx_4}$, scale factor of the block $e^{-(1 - \beta/2)AHx_4}$; $k = (e^{2a_0}/b_4(0))\,e^{(2 - \beta)AHx_4}$, constant exactly for $\beta = 2$ or $A = 0$). For any $\alpha_k$ the field equations require a diagonal source with $p_0 = p_t$ whose entries $\rho$, $p_3$, $p_0$ are polynomials of degree at most 2 in $k$ (key `requiredSource`): the source is constant only for $\beta = 2$ or $A = 0$. Written as functions of $k$ the required entries contain $A$ only through $A^2$ (read from the formulas of `requiredSource`): whether 3-space inflates or deflates is a choice of sign and is not selected by the equations. In Einstein gravity

$$
\begin{aligned}
\rho &= \frac{\frac{3}{2} A^2 \beta^2 H^2-3 A^2 H^2-6 H^2 k-\Lambda}{\kappa }, \\
p_3 &= \frac{-\frac{5}{2} A^2 \beta^2 H^2+6 A^2 \beta H^2-5 A^2 H^2+6 H^2 k+\Lambda}{\kappa }, \\
p_0 = p_t &= \frac{-\frac{3}{2} A^2 \beta^2 H^2+\frac{3}{2} A^2 \beta H^2-3 A^2 H^2+3 H^2 k+\Lambda}{\kappa }.
\end{aligned}
$$

With the author's weights ($\alpha_k = w_k/H^{2k}$, $w = (1, 1/32, 1/1152)$, $\Lambda = -10$ in the convention of this record, the notebook's $\Lambda = 10$) the background history

$$
a_4 = Hx_4,\quad b_4 = b_4(0)\,e^{(4/3)Hx_4}
$$

of SPEC section 1 ($A = 1$, $\beta = \tfrac43$, $b_4(0) = 1$, so $k = e^{(2/3)Hx_4}$) requires, at $H = 1$, the source (key `historySource_kappaT_minus_Lam`)

$$
\begin{aligned}
-\kappa\rho - \Lambda &= -\frac{9 k^2}{16}+\frac{161 k}{24}+\frac{121}{432}, \\
\kappa p_3 - \Lambda &= -\frac{9 k^2}{16}+\frac{1601 k}{216}-\frac{5359}{3888}, \\
\kappa p_0 - \Lambda = \kappa p_t - \Lambda &= \frac{79 k}{16}-\frac{497}{144},
\end{aligned}
$$

and in Einstein gravity

$$
\begin{aligned}
-\kappa\rho - \Lambda &= 6 H^2 k+\frac{H^2}{3}, \\
\kappa p_3 - \Lambda &= 6 H^2 k-\frac{13 H^2}{9}, \\
\kappa p_0 - \Lambda = \kappa p_t - \Lambda &= 3 H^2 k-\frac{11 H^2}{3}:
\end{aligned}
$$

a diagonal, $x_0$-independent source with $p_0 = p_t$ that grows with $x_4$ (powers of $k$) and is anisotropic, $\kappa(p_3 - p_0) = -\tfrac{9}{16}k^2 + \tfrac{1069}{432}k + \tfrac{2015}{972}$ for the author's weights. The history is not a vacuum solution, and the record uses it as a PRESCRIBED background. With the author's weights no exponential history is a vacuum solution; in Einstein-Gauss-Bonnet gravity ($\alpha_3 = 0$) there is no vacuum exponential history where $k$ varies, and for constant $k = k_0 > 0$ ($\beta = 2$, any $A$) the vacuum histories are exactly those with $k_0 \ne A^2$ and the tuned coupling $\alpha_2 = -1/(4H^2(A^2 - k_0))$.

| statement | Wolfram checks ($a_4$ record) | sympy checks ($a_4$ record) |
| --- | --- | --- |
| the corrected metric, volume, Riemann free of $x_0$ and sectional; the flat member | `metric_is_SPEC_section_1`, `sqrt_abs_det_g`, `mixed_riemann_free_of_x0`, `mixed_riemann_only_sectional`, `riemann_pair_antisymmetry`, `flat_member` | `mixed_riemann_free_of_x0`, `mixed_riemann_only_sectional`, `riemann_pair_antisymmetry`, `riemann_entries_polynomial`, `flat_member` |
| $P_{(k)}$ from the curvature equal the GKD record; traces; $P_{(4)} = 0$ | `P1_direct_equals_minus_4_Einstein`, `P1_direct_equals_gkd_branch_monomials`, `P2_direct_equals_gkd_branch_monomials`, `P3_direct_equals_gkd_branch_monomials`, `P1_trace_identity`, `P2_trace_identity`, `P3_trace_identity`, `P4_vanishes_pigeonhole` | `P1_equals_minus_4_Einstein`, `P1_equals_gkd_branch_monomials`, `P2_equals_gkd_branch_monomials`, `P3_equals_gkd_branch_monomials`, `P1_trace_identity`, `P2_trace_identity`, `P3_trace_identity` |
| divergence-free $E_{(k)}$ | `E1_divergence_free`, `E2_divergence_free`, `E3_divergence_free` | `E1_divergence_free`, `E2_divergence_free`, `E3_divergence_free` |
| independent components, structure, the variables $u$, $v$, $k$ | `independent_components`, `P1_structure`, `P2_structure`, `P3_structure`, `lovelock_variables` | `independent_components`, `P1_structure`, `P2_structure`, `P3_structure`, `json_lovelock_components`, `json_general_source_equations` |
| first-order constraint, second-order system | `constraint_first_order`, `second_order_system_a4pp_vv` | `constraint_first_order`, `second_order_system` |
| conservation, constraint propagation | `conservation_components`, `constraint_propagation_bianchi` | `conservation_components`, `bianchi_x4`, `json_conservation` |
| Einstein case | `einstein_equals_metric_warped_record`, `einstein_components`, `einstein_null_combinations`, `einstein_flat_vacuum`, `einstein_no_exponential_vacuum`, `einstein_second_order_system` | `einstein_equals_metric_warped_record`, `einstein_components`, `einstein_null_combinations`, `einstein_flat_vacuum`, `einstein_no_exponential_vacuum`, `json_einstein` |
| exponential histories, the author's weights, the background history, Gauss-Bonnet vacua | `exponential_history_required_source`, `author_weights_history_source`, `author_weights_no_exponential_vacuum`, `egb_exponential_vacuum_branches` | `exponential_history_required_source`, `author_weights_history_source`, `author_weights_no_exponential_vacuum`, `egb_exponential_vacuum_branches`, `egb_no_vacuum_where_k_varies`, `json_exponential_history`, `json_required_source_and_null_combinations` |

## 12. dirac16complex00 as the source of the a4 and b4 equations

**The tensor.** The source is the classical bilinear tensor of section 8. The field-equations record writes it as $T^\mu{}_\nu = \sigma_T\big(-K^{(\mu}{}_{\nu)} + \delta^\mu_\nu\,L_0\big)$ with $K^\mu{}_\nu = \tfrac12(\bar\Phi\gamma^\mu D_\nu\Phi - D_\nu\bar\Phi\,\gamma^\mu\Phi)$ symmetrised, and $\sigma_T = +1$; this is the Belinfante tensor of section 8 (whose symmetrised kinetic term is the same expression), so the two records use the same tensor and the same sign. With $k_\mu = K^\mu{}_\mu$ (no sum; equal to $K_\mu$ of section 8) and $L_0 = \sum_\mu k_\mu - mS - U(S)$:

$$
\rho = k_4 - L_0, \qquad p_3 = L_0 - k_1, \qquad p_t = L_0 - k_5, \qquad p_0 = L_0 - k_0, \qquad T^\mu{}_\nu = -K^{(\mu}{}_{\nu)} \;\; (\mu \ne \nu) .
$$

**The equations with dirac16complex00 as the source** (classical commuting $\Phi$; $k_\mu$, $S$ and $U$ classical bilinears): the constraint $\sum_k\alpha_k E_{(k)}{}^{x_4}{}_{x_4} + \Lambda = -\kappa\,(k_4 - L_0)$; the 3-space and hidden-direction equations with $\kappa p_3 = \kappa(L_0 - k_1)$ and $\kappa p_0 = \kappa(L_0 - k_0)$; the condition $p_0 = p_t$, that is $k_0 = k_5$; and $K^{(\mu}{}_{\nu)} = 0$ for every $\mu \ne \nu$; together with $k_1 = k_2 = k_3$, $k_5 = k_6 = k_7$ and the requirement that every diagonal component be independent of $x_0$. On shell $L_0 = S\,U'(S) - U(S)$. The second-order equations show what drives $a_4''$ and $v$: the differences between the kinetic terms along 3-space and along the block. This record contains no exact non-homogeneous dirac16complex00 configuration that satisfies all of these conditions; whether one exists is open.

**The homogeneous condensate.** For $\Phi = \Phi(x_4)$ on shell the field equation is $\partial_4\Phi = A_\Phi\Phi$ with $A_\Phi = B_\Phi - (u - \tfrac12a_4')I_{16}$, $B_\Phi = -M\gamma^{(x_4)} + \tfrac32He^{a_4}b_4^{-1/2}\gamma^{(x_4)}\gamma^{(x_0)}$ and $M = m + U'(S)$, free of $x_0$: $\Phi = e^{a_4/2}b_4^{-1}\chi$ with $\partial_4\chi = B_\Phi\chi$ and $B_\Phi^2 = (\tfrac94H^2k - M^2)I_{16}$. Proved exactly for general $a_4$ and $b_4$ (Wolfram, and in the sympy record both for an independently built Clifford representation and for the author's T16):

- $CA_\Phi + A_\Phi^TC = -2(u - \tfrac12a_4')\,C$, so $\partial_4S = (a_4' - 2u)\,S$ and $S = e^{a_4}b_4^{-2}S_0$ (exact for every initial $\Phi$);
- the diagonal kinetic components are $K^{x_4}{}_{x_4} = MS$ and $0$ for every other direction, and $K^{x_4}{}_{x_0} = K^{x_0}{}_{x_4} = 0$; hence $\rho = mS + U(S)$, $p_3 = p_t = p_0 = S\,U'(S) - U(S)$, and the $x_0$-independence holds;
- the nonzero off-diagonal kinetic components are exactly combinations of the 24 three-gamma bilinears $B_{abc} = \bar\Phi\gamma^{(a)}\gamma^{(b)}\gamma^{(c)}\Phi$ with $\{a,b,c\} = \{x_0, i, x_4\}$ (3), $\{x_0, i, t\}$ (9), $\{i, x_4, t\}$ (9) and $\{x_0, x_4, t\}$ (3) ($i = x_1..x_3$, $t = x_5..x_7$); there are 36 nonzero ordered pairs $(\mu, \nu)$ (the pairs $x_0$-$i$, $i$-$x_4$, $i$-$t$, $x_4$-$t$).

The 36 components fall into eight groups; within each group the coefficient is the same for every 3-space index $x_i$ ($i = 1, 2, 3$) and extra-time index $x_t$ ($t = 5, 6, 7$), and the groups $K^{x_i}{}_{x_t}$ and $K^{x_t}{}_{x_i}$ carry two bilinears each (the gammas in this table are the frame gammas; the coefficients depend on $H$, $a_4'$, $u$, $e^{a_4}$, $b_4$ and $x_0$; generated from `Revision/field_equations_a4/a4-equations.json`):

| component: bilinear | coefficient |
| --- | --- |
| $K^{x_0}{}_{x_i}$: $\bar\Phi \gamma^{x_0} \gamma^{x_i} \gamma^{x_4} \Phi$ | $\frac{e^{2 a_4} \sin z (4 (a_4')-u)}{8 \sqrt{b_4} \cos z}$ |
| $K^{x_i}{}_{x_0}$: $\bar\Phi \gamma^{x_0} \gamma^{x_i} \gamma^{x_4} \Phi$ | $-\frac{e^{-2 a_4} \sqrt{b_4} \left(\sin^2 z-1\right) (4 (a_4')-u)}{8 \cos z \sin z}$ |
| $K^{x_i}{}_{x_4}$: $\bar\Phi \gamma^{x_0} \gamma^{x_i} \gamma^{x_4} \Phi$ | $\frac{3 H}{4 \sqrt{b_4}}$ |
| $K^{x_i}{}_{x_t}$: $\bar\Phi \gamma^{x_0} \gamma^{x_i} \gamma^{x_t} \Phi$ | $-\frac{1}{4} e^{-a_4} H (\sin^2 z)^{1/12}$ |
| $K^{x_i}{}_{x_t}$: $\bar\Phi \gamma^{x_i} \gamma^{x_4} \gamma^{x_t} \Phi$ | $-\frac{1}{8} e^{-2 a_4} \sqrt{b_4} (\sin^2 z)^{1/12} (4 (a_4')-u)$ |
| $K^{x_4}{}_{x_i}$: $\bar\Phi \gamma^{x_0} \gamma^{x_i} \gamma^{x_4} \Phi$ | $-\frac{3 e^{2 a_4} H}{4 \sqrt{b_4}}$ |
| $K^{x_4}{}_{x_t}$: $\bar\Phi \gamma^{x_0} \gamma^{x_4} \gamma^{x_t} \Phi$ | $-H (\sin^2 z)^{1/12}$ |
| $K^{x_t}{}_{x_i}$: $\bar\Phi \gamma^{x_0} \gamma^{x_i} \gamma^{x_t} \Phi$ | $\frac{e^{3 a_4} H}{4 b_4 (\sin^2 z)^{1/12}}$ |
| $K^{x_t}{}_{x_i}$: $\bar\Phi \gamma^{x_i} \gamma^{x_4} \gamma^{x_t} \Phi$ | $\frac{e^{2 a_4} (4 (a_4')-u)}{8 \sqrt{b_4} (\sin^2 z)^{1/12}}$ |
| $K^{x_t}{}_{x_4}$: $\bar\Phi \gamma^{x_0} \gamma^{x_4} \gamma^{x_t} \Phi$ | $-\frac{e^{2 a_4} H}{b_4 (\sin^2 z)^{1/12}}$ |

The off-diagonal field equations $0 = \kappa T^\mu{}_\nu$ therefore require all 24 bilinears $B_{abc}$ to vanish: those with $x_0$ appear with coefficients proportional to $H$, and $B_{i\,x_4 t}$ with the coefficient $4a_4' - u$ (on the background history $4a_4' - u = \tfrac83H \ne 0$).

**Exact witnesses** that these conditions can be met with $S \ne 0$, on the histories with constant $k = e^{2a_4}/b_4 = k_0$ ($b_4 = e^{2a_4}/k_0$, any $a_4$) and constant $M$: $\Phi = e^{a_4/2}b_4^{-1}e^{-i\omega x_4}\Phi_0$ with $\omega = \sqrt{M^2 - \tfrac94H^2k_0}$ ($M^2 > \tfrac94H^2k_0$), and $\Phi_0 = v_1 + c\,v_2$ built from the two eigenvectors of $B_\Phi$ for $-i\omega$ in the sectors $\gamma^{(x_1)}\gamma^{(x_5)} = \gamma^{(x_2)}\gamma^{(x_6)} = \gamma^{(x_3)}\gamma^{(x_7)} = -1$ and $+1$, $c = \overline{v_1^\dagger C v_2}$. At $(M, H, k_0) = (5, 1, 4)$, $(5, 4/3, 4)$ and $(-5, 1, 4)$ (exact Gaussian-rational arithmetic) the frequencies are $\omega = 4, 3, 4$, the field solves the condensate equation, all 24 three-gamma bilinears vanish, and $e^{-a_4}b_4^2S = 51200$, $28800$, $51200$ respectively. These values are computed in the author's matrices T16; $S$ scales with the arbitrary normalisation of the exact null vectors $v_1, v_2$, whereas $\omega$, $S \ne 0$ and the vanishing of the bilinears do not depend on that normalisation. For histories with $k$ not constant no witness is constructed (not decided).

**Statement (the condensate as a source).** The condensate is a source with equal pressures, $p_3 = p_t = p_0$, and (with the 24 bilinears zero) no off-diagonal component; such a source needs $\sum_k\alpha_k(E^{x_1}{}_{x_1} - E^{x_0}{}_{x_0}) = 0$. On the exponential histories: no solution in Einstein gravity, neither for varying $k$ nor for constant $k > 0$; with the author's weights none where $k$ varies, and for constant $k$ exactly $k_0 = (16 + 2A^2)/(2 + A^2)$ on $\beta = 2$ and $k_0 = 8$ on the static history $A = 0$, where the $x_4$ and $x_0$ equations further need $U(S) = c - mS$ on the range of $S$ for $A \ne 0$ and fix $S_0$ for $A = 0$ (not decided further); histories that are not exponential are not decided. In particular no condensate is the source of the background history: on it the required source is anisotropic and grows with $k$ (section 11), while every condensate has equal pressures and $S = e^{a_4}b_4^{-2}S_0 \propto e^{-(5/3)Hx_4}$ decays (`condensate_cannot_source_history` of the dark-sector record). The witnesses above show that the off-diagonal conditions can be met; this record contains no check that combines a witness with the field equations for definite $\kappa$, $\Lambda$, $m$, $\lambda$ and a history.

| statement | Wolfram checks ($a_4$ record) | sympy checks ($a_4$ record) |
| --- | --- | --- |
| the Clifford facts used, in the author's T16 (with the Cl(1,1)$^{\otimes 4}$ basis as an exactly equivalent comparison) | `clifford_relations_author_T16`, `C_properties_author_T16`, `gamma_mu_anticommutes_with_Omega_mu_no_sum`, `representations_equivalent_author_T16_own_rep` | `ownrep_clifford`, `ownrep_C_properties`, `ownrep_anticommutator_no_sum`, `authorT16_clifford`, `authorT16_C_properties`, `authorT16_anticommutator_no_sum`, `representations_equivalent_authorT16_ownrep` |
| condensate equation free of $x_0$; $S = e^{a_4}b_4^{-2}S_0$; adjoint | `condensate_equation_x0_consistent`, `condensate_S_law`, `condensate_adjoint_equation` | `ownrep_condensate_equation`, `authorT16_condensate_equation`, `ownrep_condensate_S_law`, `authorT16_condensate_S_law`, `ownrep_condensate_adjoint`, `authorT16_condensate_adjoint` |
| diagonal kinetic tensor of the condensate | `condensate_kinetic_tensor_diagonal` | `ownrep_condensate_kinetic_diagonal`, `authorT16_condensate_kinetic_diagonal` |
| off-diagonal components: the 24 three-gamma bilinears, coefficients | `condensate_offdiagonal_are_three_gamma_bilinears`, `offdiagonal_coefficients_representation_independent` | `ownrep_condensate_offdiagonal_three_gamma`, `authorT16_condensate_offdiagonal_three_gamma`, `json_offdiagonal_coefficients`, `offdiagonal_coefficients_representation_independent` |
| exact witnesses | `condensate_witness_constant_k_exact` | `ownrep_condensate_witness`, `authorT16_condensate_witness` |
| the condensate as a source with equal pressures | `condensate_source_equal_pressures` | `condensate_source_equal_pressures` |

## 13. Pairing theorems for dirac16complex00 (summary)

The pairing of universes of masses $\{+m, -m\}$ is the subject of `Revision/docs/PAIR_CREATION_PROOFS`; for the commuting field the Revision pairing records prove exactly the following, in the corrected metric (its spin connection contains $b_4'$, `primordial_connection_depends_on_b4`, `geometry.connection_depends_on_b4`).

**T1 (chirality pairing).** Hypotheses: any gravitational field, fixed and the same for both members (a test field; the metric is not varied); $\Gamma = \mathrm{diag}(-I_8, I_8)$; $U = \tfrac{\lambda}{2}S^2$, or any function $U$ with $U \to -U$. Then, identically,

$$
\mathcal{L}_{m,\lambda}[\Gamma\Phi] = -\mathcal{L}_{-m,-\lambda}[\Phi], \qquad S[\Gamma\Phi] = S[\Phi], \qquad T^{(-m,-\lambda)}[\Gamma\Phi] = -T^{(m,\lambda)}[\Phi], \qquad J[\Gamma\Phi] = -J[\Phi]
$$

(for a general $U$: $\mathcal{L}_{m,U}[\Gamma\Phi] = -\mathcal{L}_{-m,-U}[\Phi]$), and $\Phi$ solves the $(m, \lambda)$ equations if and only if $\Gamma\Phi$ solves the $(-m, -\lambda)$ ones. The pair's total energy-momentum density, current and charge vanish as classical c-number bilinears.

**T2 (mirror pairing).** The reflection $\phi: x_0 \to \pi/(6H) - x_0$ ($z \to \pi - z$, across the fold $z = \pi/2$) maps the patch $0 < z < \pi/2$ onto the other half $\pi/2 < z < \pi$ of the cell and is an isometry of the corrected metric. With $\Phi'(\phi(x)) = \gamma^{(x_0)}\Phi(x)$:

$$
\mathcal{L}_{m,\lambda}[\Phi'](\phi(x)) = \mathcal{L}_{-m,\lambda}[\Phi](x), \qquad S' = -S ,
$$

and the mirror partner carries the same energy density and charge (the tensor transformed by the reflection), not the opposite. T2 is a correspondence between solutions on the two halves of a cell; the corrected metric has no $Z_2$ orbifold, the metric is degenerate at the fold, no junction condition or matching of the field across the fold is derived, and a field continuous across the fold is not thereby its own mirror image.

There is no quantum reading for dirac16complex00: it is not quantised. These theorems map solutions to solutions; they derive no creation process, rate or amplitude (the lists of what is not established in the pairing records).

| statement | Wolfram checks (pairing) | sympy checks (pairing) |
| --- | --- | --- |
| T1 for the commuting field in the corrected metric | `Gamma_properties`, `T1_kernel_field_equation`, `T1_linearity_argument`, `primordial_connection_depends_on_b4`, `T1_Lagrangian_primordial_commuting`, `T1_Lagrangian_negative_controls_primordial_commuting`, `T1_field_equation_covariance_primordial_commuting`, `T1_Euler_Lagrange_map_primordial_commuting`, `T1_energy_momentum_primordial_commuting`, `T1_current_primordial_commuting`, `T1_general_potential_primordial_commuting` | `geometry.connection_depends_on_b4`, `T1.metric.commuting.lagrangian`, `T1.metric.commuting.negative_controls`, `T1.metric.commuting.euler_lagrange_map`, `T1.metric.commuting.emt`, `T1.metric.commuting.pair_total_emt_zero`, `T1.metric.commuting.current`, `T1.metric.commuting.general_potential` |
| T2 for the commuting field; the fold | `T2_mirror_is_isometry`, `T2_mirror_Lagrangian_commuting`, `T2_mirror_energy_momentum_and_current_commuting`, `T2_mirror_Euler_Lagrange_commuting` | `geometry.mirror_isometry`, `geometry.fold_degenerate`, `T2.metric.commuting.euler_lagrange_map`, `T2.metric.commuting.emt`, `T2.metric.commuting.current`, `T2.metric.commuting.S_odd` |

## 14. Check index

Every check below has the verdict PASS in the named report (the publication test re-reads the reports and confirms each name and verdict). Counts at the time of writing: wolfram-algebra 45 checks, python-algebra 35, wolfram-field-theory 86, python-field-theory 72, wolfram-a4-report 57, python-a4-report 69, wolfram-pairing 102, python-pairing 67, wolfram-scope 16, python-scope 15, python-derive-eos 48, python-independent-numerics 32; all pass.

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
| `Revision/theory/reports/wolfram-field-theory.json` | `metric_is_the_corrected_metric`, `sqrt_det_g`, `degenerate_at_H_0`, `vielbein_inverse`, `christoffel_count`, `vielbein_postulate` |
| `Revision/theory/reports/wolfram-field-theory.json` | `omega_antisymmetric`, `omega_components`, `Omega_components`, `gamma_covariantly_constant`, `S_rotates_gamma_with_omega`, `ricci_mixed_components` |
| `Revision/theory/reports/wolfram-field-theory.json` | `ricci_scalar`, `flat_member_and_curvature`, `L_real_C`, `L_total_divergence_to_unsymmetrised_C`, `L_spin_connection_drops_out_C`, `gammaOmega_divergence_form` |
| `Revision/theory/reports/wolfram-field-theory.json` | `Majorana_Lg_total_derivative_grassmann`, `Majorana_Lg_commuting_control`, `EL_Psibar_C`, `EL_Psi_C`, `adjoint_equation_is_Dirac_conjugate_C`, `Dirac_operator_explicit_C` |
| `Revision/theory/reports/wolfram-field-theory.json` | `block_form`, `evolution_form_C`, `solution_matrix_square`, `exact_solution_x4_x0_m0_C`, `exact_solution_x4_x0_quarter_C`, `exact_solution_nonlinear_homogeneous_C` |
| `Revision/theory/reports/wolfram-field-theory.json` | `nontriviality_2_dirac16complex00`, `gammaOmega_total`, `gammaOmega_per_direction`, `Omega_vanishes_iff_a4prime_b4prime_and_H_vanish`, `spin_curvature_equals_Riemann`, `good_sector_hermiticity_curved` |
| `Revision/theory/reports/wolfram-field-theory.json` | `Lichnerowicz_identity_C`, `current_real_C`, `current_conservation_identity_C`, `charge_density_is_Krein_form_C`, `Noether_identity_diffeomorphisms_C`, `Noether_identity_local_Lorentz_C` |
| `Revision/theory/reports/wolfram-field-theory.json` | `conservation_on_shell_general`, `T_vielbein_variation_closed_form_C`, `T_symmetric_part_Belinfante_C`, `T_diagonal_components_C`, `T_x4_x0_component_C`, `EMT_trace_C` |
| `Revision/theory/reports/wolfram-field-theory.json` | `kinetic_sum_on_shell_C`, `energy_exchange_equation` |
| `Revision/theory/reports/python-field-theory.json` | `sqrt_det_g`, `metric_from_vielbein_equals_SPEC`, `gammas_json_equals_python_construction`, `christoffel_symmetric_metric_compatible`, `vielbein_postulate`, `spin_connection_antisymmetric` |
| `Revision/theory/reports/python-field-theory.json` | `Omega_x4_vanishes_Omega_x0_does_not`, `spinor_connection_real`, `covariant_constancy_D_mu_gamma_nu`, `curvature_and_flat_member`, `commuting_lagrangian_real`, `commuting_controls_not_vacuous` |
| `Revision/theory/reports/python-field-theory.json` | `commuting_total_divergence_relation`, `anticommutator_gamma_Omega_vanishes`, `divergence_of_sqrtg_gamma`, `negative_control_majorana_grassmann_total_derivative`, `negative_control_majorana_commuting_contrast`, `commuting_euler_lagrange_psibar_variation` |
| `Revision/theory/reports/python-field-theory.json` | `commuting_euler_lagrange_psi_variation`, `commuting_adjoint_equation_is_conjugate`, `hamiltonian_form_and_heisenberg_equation`, `exact_solution_family_x4_x0`, `exact_nonlinear_homogeneous_solution`, `gamma_mu_Omega_mu_equals_hidden_block_terms` |
| `Revision/theory/reports/python-field-theory.json` | `gravity_term_square`, `per_direction_terms`, `nontriviality_Omega_zero_iff_flat`, `spinor_curvature_equals_riemann`, `lichnerowicz_identity_on_fields`, `lichnerowicz_contraction` |
| `Revision/theory/reports/python-field-theory.json` | `commuting_current_conservation`, `commuting_emt_conservation_on_shell`, `commuting_emt_conservation_negative_control`, `commuting_emt_equals_general_vielbein_variation_on_shell`, `commuting_emt_symmetric`, `commuting_emt_equals_vielbein_variation_diagonal` |
| `Revision/theory/reports/python-field-theory.json` | `commuting_T_x4x0_homogeneous`, `commuting_trace_on_shell`, `energy_exchange_equation`, `commuting_homogeneous_on_shell_rho_p` |
| `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `spin_connection_antisymmetric`, `Omega_x4_vanishes_Omega_x0_does_not`, `gravity_term_gamma_mu_Omega_mu`, `condensate_S_law`, `metric_is_SPEC_section_1`, `sqrt_abs_det_g` |
| `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `mixed_riemann_free_of_x0`, `mixed_riemann_only_sectional`, `riemann_pair_antisymmetry`, `flat_member`, `P1_direct_equals_minus_4_Einstein`, `P1_direct_equals_gkd_branch_monomials` |
| `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `P2_direct_equals_gkd_branch_monomials`, `P3_direct_equals_gkd_branch_monomials`, `P1_trace_identity`, `P2_trace_identity`, `P3_trace_identity`, `P4_vanishes_pigeonhole` |
| `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `E1_divergence_free`, `E2_divergence_free`, `E3_divergence_free`, `independent_components`, `P1_structure`, `P2_structure` |
| `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `P3_structure`, `lovelock_variables`, `constraint_first_order`, `second_order_system_a4pp_vv`, `conservation_components`, `constraint_propagation_bianchi` |
| `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `einstein_equals_metric_warped_record`, `einstein_components`, `einstein_null_combinations`, `einstein_flat_vacuum`, `einstein_no_exponential_vacuum`, `einstein_second_order_system` |
| `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `exponential_history_required_source`, `author_weights_history_source`, `author_weights_no_exponential_vacuum`, `egb_exponential_vacuum_branches`, `clifford_relations_author_T16`, `C_properties_author_T16` |
| `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `gamma_mu_anticommutes_with_Omega_mu_no_sum`, `representations_equivalent_author_T16_own_rep`, `condensate_equation_x0_consistent`, `condensate_adjoint_equation`, `condensate_kinetic_tensor_diagonal`, `condensate_offdiagonal_are_three_gamma_bilinears` |
| `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `offdiagonal_coefficients_representation_independent`, `condensate_witness_constant_k_exact`, `condensate_source_equal_pressures` |
| `Revision/field_equations_a4/reports/python-a4-report.json` | `ownrep_gravity_term`, `authorT16_gravity_term`, `ownrep_condensate_S_law`, `authorT16_condensate_S_law`, `mixed_riemann_free_of_x0`, `mixed_riemann_only_sectional` |
| `Revision/field_equations_a4/reports/python-a4-report.json` | `riemann_pair_antisymmetry`, `flat_member`, `riemann_entries_polynomial`, `P1_trace_identity`, `P2_trace_identity`, `P3_trace_identity` |
| `Revision/field_equations_a4/reports/python-a4-report.json` | `P1_equals_minus_4_Einstein`, `P1_equals_gkd_branch_monomials`, `P2_equals_gkd_branch_monomials`, `P3_equals_gkd_branch_monomials`, `E1_divergence_free`, `E2_divergence_free` |
| `Revision/field_equations_a4/reports/python-a4-report.json` | `E3_divergence_free`, `independent_components`, `P1_structure`, `P2_structure`, `P3_structure`, `json_lovelock_components` |
| `Revision/field_equations_a4/reports/python-a4-report.json` | `json_general_source_equations`, `constraint_first_order`, `second_order_system`, `conservation_components`, `bianchi_x4`, `json_conservation` |
| `Revision/field_equations_a4/reports/python-a4-report.json` | `einstein_equals_metric_warped_record`, `einstein_components`, `einstein_null_combinations`, `einstein_flat_vacuum`, `einstein_no_exponential_vacuum`, `json_einstein` |
| `Revision/field_equations_a4/reports/python-a4-report.json` | `exponential_history_required_source`, `author_weights_history_source`, `author_weights_no_exponential_vacuum`, `egb_exponential_vacuum_branches`, `egb_no_vacuum_where_k_varies`, `json_exponential_history` |
| `Revision/field_equations_a4/reports/python-a4-report.json` | `json_required_source_and_null_combinations`, `ownrep_clifford`, `ownrep_C_properties`, `ownrep_anticommutator_no_sum`, `authorT16_clifford`, `authorT16_C_properties` |
| `Revision/field_equations_a4/reports/python-a4-report.json` | `authorT16_anticommutator_no_sum`, `representations_equivalent_authorT16_ownrep`, `ownrep_condensate_equation`, `authorT16_condensate_equation`, `ownrep_condensate_adjoint`, `authorT16_condensate_adjoint` |
| `Revision/field_equations_a4/reports/python-a4-report.json` | `ownrep_condensate_kinetic_diagonal`, `authorT16_condensate_kinetic_diagonal`, `offdiagonal_coefficients_representation_independent`, `ownrep_condensate_offdiagonal_three_gamma`, `authorT16_condensate_offdiagonal_three_gamma`, `json_offdiagonal_coefficients` |
| `Revision/field_equations_a4/reports/python-a4-report.json` | `ownrep_condensate_witness`, `authorT16_condensate_witness`, `condensate_source_equal_pressures` |
| `Revision/pairing/reports/wolfram-pairing.json` | `Q_one_particle_Krein_inertia_real_frequencies`, `primordial_connection_depends_on_b4`, `Gamma_properties`, `T1_kernel_field_equation`, `T1_linearity_argument`, `T1_Lagrangian_primordial_commuting` |
| `Revision/pairing/reports/wolfram-pairing.json` | `T1_Lagrangian_negative_controls_primordial_commuting`, `T1_field_equation_covariance_primordial_commuting`, `T1_Euler_Lagrange_map_primordial_commuting`, `T1_energy_momentum_primordial_commuting`, `T1_current_primordial_commuting`, `T1_general_potential_primordial_commuting` |
| `Revision/pairing/reports/wolfram-pairing.json` | `T2_mirror_is_isometry`, `T2_mirror_Lagrangian_commuting`, `T2_mirror_energy_momentum_and_current_commuting`, `T2_mirror_Euler_Lagrange_commuting` |
| `Revision/pairing/reports/python-pairing.json` | `Q.one_particle_Krein_inertia_proof`, `geometry.connection_depends_on_b4`, `T1.metric.commuting.lagrangian`, `T1.metric.commuting.negative_controls`, `T1.metric.commuting.euler_lagrange_map`, `T1.metric.commuting.emt` |
| `Revision/pairing/reports/python-pairing.json` | `T1.metric.commuting.pair_total_emt_zero`, `T1.metric.commuting.current`, `T1.metric.commuting.general_potential`, `geometry.mirror_isometry`, `geometry.fold_degenerate`, `T2.metric.commuting.euler_lagrange_map` |
| `Revision/pairing/reports/python-pairing.json` | `T2.metric.commuting.emt`, `T2.metric.commuting.current`, `T2.metric.commuting.S_odd` |
| `Revision/theory/reports/wolfram-scope.json` | `connection_free_lagrangian_same_equations`, `good_sector_hermiticity_up_to_the_brane_flux`, `boosted_frame_reproduces_metric`, `boosted_frame_canonical_connection`, `boosted_frame_gammaOmega_formula`, `boosted_frame_removes_only_the_H_term` |
| `Revision/theory/reports/wolfram-scope.json` | `boosted_frame_curvature_nonzero`, `rescaling_removes_the_connection_term`, `rescaled_equation_quadratic_potential`, `gammaOmega_sees_the_hidden_block`, `spin_connection_in_the_energy_momentum_tensor`, `extra_time_growth_rates_unbounded` |
| `Revision/theory/reports/wolfram-scope.json` | `good_sector_x0_independent_modes_without_boundary_condition`, `commuting_field_energy_unbounded_below` |
| `Revision/theory/reports/python-scope.json` | `connection_free_lagrangian_same_equations`, `good_sector_hermiticity_up_to_the_brane_flux`, `boosted_frame_reproduces_metric`, `boosted_frame_canonical_connection`, `boosted_frame_gammaOmega_formula`, `boosted_frame_removes_only_the_H_term` |
| `Revision/theory/reports/python-scope.json` | `boosted_frame_curvature_nonzero`, `rescaling_removes_the_connection_term`, `rescaled_equation_quadratic_potential`, `gammaOmega_sees_the_hidden_block`, `spin_connection_in_the_energy_momentum_tensor`, `extra_time_growth_rates_unbounded` |
| `Revision/theory/reports/python-scope.json` | `good_sector_x0_independent_modes_without_boundary_condition`, `commuting_field_energy_unbounded_below` |
| `Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json` | `observer_N1_weff_identity`, `observer_N2_weff_identity`, `positive_models_bounded_by_minus_four_ninths`, `M2_tangent_exact`, `M3_tangent_exact`, `M4_former_tuning_on_the_history` |
| `Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json` | `unite_w0_requires_dominant_ghost`, `M5_former_composition_on_the_history`, `condensate_ratio_equals_unite_constant_w`, `condensate_ratio_drift_at_unite_value`, `condensate_phantom_interval`, `condensate_observer` |
| `Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json` | `history_required_source`, `condensate_cannot_source_history` |

## 15. What is not claimed

- **No quantisation.** dirac16complex00 is not quantised; its energy-momentum tensor is a classical bilinear. The operator statements (Krein space, Fock space, normal ordering) belong to dirac16complex.
- **The energy is not bounded below, the charge is indefinite.** The record decides the energy question negatively: already for $U = 0$ in the good sector there are positive-frequency solutions of negative energy, and the energy density $-5|c|^2$ of the example of section 9 is unbounded below as $|c|$ grows; the charge $\int\sqrt{|g|}\,\Phi^\dagger B\Phi$ is indefinite and only locally conserved (it is constant only if no charge flows through the degenerate points; see the item on the fold below). The descriptions "semi-classical" and "analogue of Dirac's 1928 wave function" are interpretations: that wave function has a positive conserved density, this field does not.
- **Frame dependence of the gravitational term.** $\gamma^\mu\Omega_\mu = \tfrac32He^{a_4}b_4^{-1/2}\gamma^{(x_0)} + (u - \tfrac12a_4')\gamma^{(x_4)}$ is the value for the diagonal vielbein and the variables $\Phi$; its $c_g$ part vanishes in the boosted frame of section 6 (no boost in this plane removes its $v_g$ part), and the rescaling $\Phi = e^{a_4/2}b_4^{-1}(\sin^2 z)^{-1/8}\chi$ removes all of it. Only $\Omega_\mu$ itself where the metric is curved and the frame factors are frame-independent; non-triviality [2] is claimed in this exact sense. On the flat member $a_4 = 0$, $b_4 = H^2(x_4 - c)^2$ the spin connection is a pure frame effect.
- **No 3-space observer equation of state, no CPL fit, no comparison with supernova data.** Section 10 gives the ratios $p/\rho$ of the 8-dimensional tensor only; Hypothesis00 (a time-varying dark-energy or dark-matter equation of state from dirac16complex00) is investigated in the separate dark-sector record `Revision/docs/DARK_SECTOR_HYPOTHESES`, not here (its verdict is summarised in section 10: it establishes neither hypothesis). For the homogeneous condensate with $\lambda \ne 0$ the ratio $w$ drifts with $a_4$ and $b_4$.
- **No general solution, no well-posed Cauchy problem.** The exact solutions of section 5 are test points; the field equation is not solved in general, and no existence statement for the nonlinear Cauchy problem is made beyond the first-order evolution form. For data that depend on the extra times the problem is ill-posed in Hadamard's sense (section 7), and the good sector needs a boundary condition at the degenerate points, which this record does not impose.
- **No history from a condensate.** Section 12 shows that a homogeneous condensate is the source of no exponential history in Einstein gravity, that with the author's weights it is a source at most on the constant-$k$ histories named there (not decided further), and that no condensate is the source of the background history; non-exponential histories are not decided, and no non-homogeneous source (which would drive $a_4''$ and $v$ through differences of the kinetic terms) is constructed.
- **The $x_0$ dependence.** The corrected metric is an exact solution only with a source whose diagonal components are independent of $x_0$, with $p_0 = p_t$ and without off-diagonal components; a dirac16complex00 configuration whose diagonal components depend on $x_0$ is not a consistent source for this metric.
- **The fold.** The points $z = \pi/2 + n\pi$ are degenerate surfaces of the metric ($g_{00} = 0$, $\sqrt{|g|} = 0$); no junction condition is derived, the mirror correspondence used by T2 is an isometry statement and not an orbifold, and the boundary term $\sigma_z b_4^{3/2}(\sin^2 z)^{1/4}u^\dagger M_0 v$ of the hidden direction does not vanish there.
- **Pairing.** The pairing theorems of section 13 derive no creation process, rate or amplitude for universes of masses $\{+m, -m\}$; they are correspondences between solutions, in a fixed gravitational field.
- **The withdrawn metrics.** The metric of 2026-10-14 (with the factors $\sin^{1/3}z$, $g_{00} = \cot^2 z$ and the patch $0 < z < \pi/2$) and the version 1 of 2026-10-16 are withdrawn; no statement of this document is restricted to them, and their formulas are not results of this record.
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

The Wolfram field-theory verifier runs in six parts and a merge (on 2026-10-16: base 14 s, emt-C 57 s, emt-G 179 s, solutions 36 s, solutions-G 17 s, quantisation 5 s; the scope verifier 2 s), and the sympy checker in two runs, the part `--part nonlinear` (32 s; the nonlinear homogeneous solutions of both statistics, written to a git-ignored part file that the full run takes over only if its inputs are unchanged) and the full run (148 s to 161 s), whose comparison with the Wolfram record agrees entirely (33 of 33 formula records and 65 of 65 check pairs); `Revision/theory/wolfram/WOLFRAMSCRIPT_PROVENANCE.md`, section 6.10. The run times of the other verifiers are recorded in the READMEs of their folders and in `Revision/docs/PAIR_CREATION_PROOFS`.

The two dark-sector programs whose reports section 10 cites (their place in the full order and their run times are given in `Revision/docs/DARK_SECTOR_HYPOTHESES`):

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

The builder makes the .tex twice and the PDF in two fresh directories, requires byte identity and a warning-free LaTeX log, and verifies the PDF against its entry in Revision's own registry `Revision/pdf-specifications.json`. The publication test checks that the .tex is the builder's output for this .md, that the PDF is registered with its page count and sha256, that the formula blocks of sections 5, 11 and 12 are the ones generated from `Revision/theory/field-theory.json` and `Revision/field_equations_a4/a4-equations.json`, that no statement of the withdrawn metrics is left, and that every check cited in section 14 exists in its report with a passing verdict.
