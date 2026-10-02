# dirac16complex00 in the primordial gravitational field

## The semi-classical Pin(4,4) spinor field: Lagrangian, field equations, non-triviality [2], energy-momentum tensor, equations of state and the field equations for a4[x4] (Revision record)

## Abstract

This document records, for the author's primordial gravitational field of `Revision/SPEC.md` section 1, the field theory of dirac16complex00: a field $\Phi$ with 16 complex commuting components that transform as a spinor of Pin(4,4) (a set of 16 scalar fields that transform as a Pin(4,4) spinor), treated as a classical ("semi-classical") field. It gives the Lagrangian and its coupling to gravity through the vielbein and the canonical spin connection, the exact Euler-Lagrange equations (covariant, explicit in the metric, and as 16 component equations), the non-triviality theorem [2] with its proof and its exact scope (in the diagonal vielbein the gravitational term of the field equation is $\gamma^\mu\Omega_\mu = 3H\gamma^{(x_8)}$, nonzero for every $H > 0$; this value depends on the frame and on the field variables, while $\Omega_\mu$ itself vanishes in no frame because the metric is curved), the self-consistency of the equations and its limits (no well-posed Cauchy problem for data that depend on the extra times; boundary terms at $z = \pi/2$), the energy-momentum tensor as a classical bilinear, its kinetic and potential parts, the energy density, the pressures and the equations of state, and the Einstein-Lovelock field equations for $a_4(x_4)$ with dirac16complex00 as the source. Every formula is an output of Revision code (Wolfram and an independent sympy checker for each part); each section ends with the names of the checks that verify it, and the check index collects them. Nothing is taken from the earlier stages of the repository. The classical energy of dirac16complex00 is unbounded below already for $U = 0$ (positive-frequency modes of negative energy) and its conserved charge is indefinite. What the record does not establish is stated in the section "What is not claimed".

## 1. Scope, sources and conventions

**Sources.** Every formula and number below is read from these Revision outputs (all produced by Revision code, all checks passing):

| part | Wolfram record | independent sympy record |
| --- | --- | --- |
| gammas, Pin(4,4), Spin(4,4) (SPEC section 2) | `Revision/algebra/reports/wolfram-algebra.json`, fixture `Revision/algebra/gammas.json` | `Revision/algebra/reports/python-algebra.json` |
| geometry, Lagrangian, field equations, energy-momentum tensor (SPEC sections 1-4) | `Revision/theory/reports/wolfram-field-theory.json`, formulas `Revision/theory/field-theory.json` | `Revision/theory/reports/python-field-theory.json` |
| field equations for $a_4(x_4)$ (SPEC section 5) | `Revision/field_equations_a4/reports/wolfram-a4-report.json`, formulas `Revision/field_equations_a4/a4-equations.json` | `Revision/field_equations_a4/reports/python-a4-report.json` |
| pairing theorems (SPEC section 9) | `Revision/pairing/reports/wolfram-pairing.json`, theorems `Revision/pairing/pairing-theory.json` | `Revision/pairing/reports/python-pairing.json` |
| scope of the statements: frame dependence, boundary terms, growth, sign of the energy | `Revision/theory/reports/wolfram-scope.json` | `Revision/theory/reports/python-scope.json` |

The Wolfram and the sympy records are written independently (no shared code); each sympy record re-derives the statements and compares them with the Wolfram record. The theory records verify every statement for both statistics: the checks whose names end in `_C` (Wolfram) or start with `commuting_` (sympy) are the ones for the commuting field dirac16complex00 of this document; the Grassmann versions belong to dirac16complex (`Revision/docs/DIRAC16COMPLEX_FIELD_THEORY`).

**Coordinates (the author's names).** $x_1, x_2, x_3$ are ordinary 3-space (inflating, scale factor $e^{a_4}\sin^{1/6}z$); $x_4$ is the time; $x_5, x_6, x_7$ are the three extra times, time-like, which deflate exponentially (scale factor $e^{-a_4}\sin^{1/6}z$ with $a_4$ increasing); $x_8$ is the hidden space direction. Throughout $z = 6Hx_8 \in (0, \pi/2)$, $H > 0$ is the author's constant and $a_4' = da_4/dx_4$. In formulas the index $i$ runs over $x_1, x_2, x_3$ and $t$ over $x_5, x_6, x_7$.

**The metric** (SPEC section 1, exactly):

```text
g = {{E^(2 a4[x4]) Sin[6 H x8]^(1/3),0,0,0,0,0,0,0},
     {0,E^(2 a4[x4]) Sin[6 H x8]^(1/3),0,0,0,0,0,0},
     {0,0,E^(2 a4[x4]) Sin[6 H x8]^(1/3),0,0,0,0,0},
     {0,0,0,-1,0,0,0,0},
     {0,0,0,0,-E^(-2 a4[x4]) Sin[6 H x8]^(1/3),0,0,0},
     {0,0,0,0,0,-E^(-2 a4[x4]) Sin[6 H x8]^(1/3),0,0},
     {0,0,0,0,0,0,-E^(-2 a4[x4]) Sin[6 H x8]^(1/3),0},
     {0,0,0,0,0,0,0,Cot[6 H x8]^2}}
```

Signature (4,4): space-like $x_1, x_2, x_3, x_8$, time-like $x_4, x_5, x_6, x_7$. The volume factor is

$$
\sqrt{|g|} = \cos z ,
$$

independent of $x_4$: the inflation $e^{3a_4}$ of 3-space is compensated by the deflation $e^{-3a_4}$ of the extra times. $H = 0$ is not a metric of the family (a degenerate limit: $g_{11}, g_{55} \to 0$ and $g_{88} \to \infty$); every statement assumes $H > 0$ and $0 < z < \pi/2$.

**Spinor notation.** $\bar\Phi = \Phi^\dagger C$, $S = \bar\Phi\Phi$, $U(S)$ a real potential ($U = \tfrac{\lambda}{2}S^2$ where stated), $V = m + U'(S)$. Frame gammas are written $\gamma^{(x_a)}$, coordinate gammas $\gamma^\mu = e^\mu{}_a\gamma^{(a)}$. The theory records write $\Psi$ for both statistics; here $\Phi$ denotes the commuting field.

**Labels.** "Exact" means verified by exact symbolic computation (no floating point) in the named checks; "interpretation" marks a reading that is not itself a computed statement.

| statement | Wolfram checks | sympy checks |
| --- | --- | --- |
| the metric, its vielbein and $\sqrt{\lvert g\rvert} = \cos z$ | `metric_is_the_authors`, `sqrt_det_g_is_cos_z` | `metric_from_vielbein_equals_SPEC`, `sqrt_det_g_equals_cos_z` |
| $H = 0$ is a degenerate limit | `degenerate_at_H_0` | |

## 2. The field dirac16complex00 and its symmetry group

dirac16complex00 is a field $\Phi$ with 16 complex commuting components (16 scalar fields) that transform as a Pin(4,4) spinor. It is a classical field; it is not quantised (SPEC section 6: only dirac16complex, the anticommuting field, is quantised canonically). SPEC section 3 calls it the analogue of Dirac's 1928 wave function and the author calls it semi-classical; both are interpretations, and the record shows two exact differences from Dirac's wave function: its conserved charge $Q = \int\cos z\,\Phi^\dagger B\Phi\,d^7x$ is an indefinite form, and its classical energy is unbounded below already for $U = 0$ in the good sector (section 9).

**The gammas.** The real $16\times16$ matrices are the author's T16, rebuilt in Revision code from the author's formulas (the tau matrices and their blocks), with the frame map $\gamma^{(x_8)} = T16[0]$, $\gamma^{(x_1..x_3)} = T16[1..3]$, $\gamma^{(x_4)} = T16[4]$ and $\gamma^{(x_5..x_7)} = T16[5..7]$. Verified exactly:

- $\{\gamma^{(a)}, \gamma^{(b)}\} = 2\eta^{ab}$ with $\eta = \mathrm{diag}(+1,+1,+1,-1,-1,-1,-1,+1)$ in the order $x_1 \ldots x_8$; every $\gamma^{(a)}$ is a real signed permutation matrix; the space-like ones are symmetric, the time-like ones antisymmetric.
- $C = \gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)}$ is real symmetric, $C^2 = 1$, and $C\gamma^{(a)}$ is real antisymmetric for every $a$; $C = \mathrm{diag}(-\sigma, \sigma)$ with the notebook's $\sigma$.
- $\Gamma = \gamma^{(x_8)}\gamma^{(x_1)}\cdots\gamma^{(x_7)} = \mathrm{diag}(-I_8, I_8)$, $\Gamma^2 = 1$, and $\Gamma$ anticommutes with every $\gamma^{(a)}$.
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
& f_{x_1} = f_{x_2} = f_{x_3} = e^{a_4}\sin^{1/6}z, \qquad f_{x_4} = 1, \\
& f_{x_5} = f_{x_6} = f_{x_7} = e^{-a_4}\sin^{1/6}z, \qquad f_{x_8} = \cot z
\end{aligned}
$$

reproduces the author's metric entry by entry, $g = e^T\eta e$, with inverse $e_a{}^\mu = \delta_a^\mu/f_a$ and $\sqrt{|g|} = f_1\cdots f_8 = \cos z$.

**Levi-Civita connection.** The 25 independent nonzero Christoffel symbols ($m \le n$) are, for $i = x_1, x_2, x_3$ and $t = x_5, x_6, x_7$ (no sum),

$$
\begin{aligned}
&\Gamma^{x_i}{}_{x_i x_4} = a_4', \qquad \Gamma^{x_i}{}_{x_i x_8} = H\cot z, \qquad \Gamma^{x_4}{}_{x_i x_i} = e^{2a_4}\sin^{1/3}z\; a_4', \\
&\Gamma^{x_8}{}_{x_i x_i} = -e^{2a_4} H\sec z\,\sin^{4/3}z, \\
&\Gamma^{x_t}{}_{x_4 x_t} = -a_4', \qquad \Gamma^{x_t}{}_{x_t x_8} = H\cot z, \qquad \Gamma^{x_4}{}_{x_t x_t} = e^{-2a_4}\sin^{1/3}z\; a_4', \\
&\Gamma^{x_8}{}_{x_t x_t} = e^{-2a_4} H\sec z\,\sin^{4/3}z, \qquad \Gamma^{x_8}{}_{x_8 x_8} = -12H\csc(12Hx_8) .
\end{aligned}
$$

**Canonical spin connection.** $\omega_\mu{}^a{}_b = e^a{}_\nu(\partial_\mu e_b{}^\nu + \Gamma^\nu{}_{\mu\lambda}e_b{}^\lambda)$ satisfies the vielbein postulate $\partial_\mu e^a{}_\nu - \Gamma^\lambda{}_{\mu\nu}e^a{}_\lambda + \omega_\mu{}^a{}_b e^b{}_\nu = 0$ for all 512 components, and $\omega_{\mu ab} = \eta_{ac}\omega_\mu{}^c{}_b = -\omega_{\mu ba}$. Exactly 12 components with $a < b$ are nonzero:

$$
\begin{aligned}
& \omega_{x_i,(x_i)(x_4)} = a_4' e^{a_4}\sin^{1/6}z, \qquad \omega_{x_i,(x_i)(x_8)} = H e^{a_4}\sin^{1/6}z, \\
& \omega_{x_t,(x_4)(x_t)} = -a_4' e^{-a_4}\sin^{1/6}z, \qquad \omega_{x_t,(x_t)(x_8)} = -H e^{-a_4}\sin^{1/6}z ,
\end{aligned}
$$

and $\omega_{x_4} = \omega_{x_8} = 0$. Each component is $a_4'$ or $H$ times a factor that never vanishes on the patch.

**Spinor connection and covariant derivative.** $\Omega_\mu = \tfrac12\omega_{\mu ab}S^{ab}$:

$$
\begin{aligned}
\Omega_{x_i} &= \tfrac12 e^{a_4}\sin^{1/6}z\,\big(a_4'\,\gamma^{(x_i)}\gamma^{(x_4)} + H\,\gamma^{(x_i)}\gamma^{(x_8)}\big), \qquad i = x_1, x_2, x_3, \\
\Omega_{x_t} &= -\tfrac12 e^{-a_4}\sin^{1/6}z\,\big(a_4'\,\gamma^{(x_4)}\gamma^{(x_t)} + H\,\gamma^{(x_t)}\gamma^{(x_8)}\big), \qquad t = x_5, x_6, x_7, \\
\Omega_{x_4} &= \Omega_{x_8} = 0,
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

**Curvature.** $R^\mu{}_\nu$ is diagonal with

$$
R^{x_i}{}_{x_i} = a_4'' - 6H^2,\quad R^{x_4}{}_{x_4} = 6(a_4')^2,\quad R^{x_t}{}_{x_t} = -a_4'' - 6H^2,\quad R^{x_8}{}_{x_8} = -6H^2 ,
$$

$$
R = 6\big((a_4')^2 - 7H^2\big) .
$$

Since $R^{x_8}{}_{x_8} = -6H^2 < 0$ for every $H > 0$ and every function $a_4$, the metric is curved for every member of the family, $a_4$ constant included; all Riemann components vanish only in the formal limit $a_4' = a_4'' = 0$, $H = 0$ (flat 4+4), which is outside the family.

| statement | Wolfram checks (theory) | sympy checks (theory) |
| --- | --- | --- |
| vielbein and its inverse | `metric_is_the_authors`, `vielbein_inverse` | `metric_from_vielbein_equals_SPEC` |
| 25 Christoffel symbols | `christoffel_count` | `christoffel_symmetric_metric_compatible` |
| vielbein postulate, antisymmetry, the 12 components | `vielbein_postulate`, `omega_antisymmetric`, `omega_components` | `vielbein_postulate`, `spin_connection_antisymmetric` |
| $\Omega_\mu$; $\Omega_{x_4} = \Omega_{x_8} = 0$ | `Omega_components` | `Omega_x4_and_Omega_x8_vanish` |
| covariant constancy of the gammas | `gamma_covariantly_constant` | `covariant_constancy_D_mu_gamma_nu` |
| Ricci tensor and scalar; curved for every $H > 0$ | `ricci_mixed_components`, `ricci_scalar`, `never_flat_for_H_positive` | `curvature_nonzero_flat_only_formally` |

## 4. The Lagrangian

The Lagrangian density (SPEC section 3; the same form as for dirac16complex, only the statistics differ):

$$
\mathcal{L} = \sqrt{|g|}\,\Big[\tfrac12\big(\bar\Phi\gamma^\mu D_\mu\Phi - (D_\mu\bar\Phi)\gamma^\mu\Phi\big) - m\,S - U(S)\Big], \qquad S = \bar\Phi\Phi = \Phi^\dagger C\Phi ,
$$

with an explicit mass term linear in $m$ and quadratic in the spinor, and $U(S) = \tfrac{\lambda}{2}S^2$ where stated (a general real $U$ elsewhere). Proved exactly for the commuting field:

1. $\mathcal{L}$ is real, $\mathcal{L}^* = \mathcal{L}$: $C$ real symmetric, $C\gamma^{(a)}$ real antisymmetric and $(S^{ab})^TC + CS^{ab} = 0$ make the symmetrised kinetic term and $\bar\Phi\Phi$ real without a factor $i$ (the sympy record checks it on 408 monomials, with the control that the unsymmetrised form is not real off shell).
2. $\mathcal{L}$ differs from the unsymmetrised form by a total divergence: $\mathcal{L} = \sqrt{|g|}\,[\bar\Phi\gamma^\mu D_\mu\Phi - mS - U] - \tfrac12\partial_\mu(\sqrt{|g|}\,\bar\Phi\gamma^\mu\Phi)$.
3. For this diagonal metric $\{\gamma^\mu, \Omega_\mu\} = 0$ for each $\mu$ separately, so $\bar\Phi\{\gamma^\mu, \Omega_\mu\}\Phi = 0$ and the spin connection drops out of $\mathcal{L}$ itself (next display).

$$
\mathcal{L} = \cos z\,\Big[\tfrac12\sum_a \frac{1}{f_a}\big(\bar\Phi\gamma^{(a)}\partial_a\Phi - \partial_a\bar\Phi\,\gamma^{(a)}\Phi\big) - m S - U(S)\Big] .
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

**Explicit form in the primordial field** ($z = 6Hx_8$):

$$
\begin{aligned}
& e^{-a_4}\sin^{-1/6}z\,\big(\gamma^{(x_1)}\partial_1 + \gamma^{(x_2)}\partial_2 + \gamma^{(x_3)}\partial_3\big)\Phi + \gamma^{(x_4)}\partial_4\Phi \\
& \qquad + e^{a_4}\sin^{-1/6}z\,\big(\gamma^{(x_5)}\partial_5 + \gamma^{(x_6)}\partial_6 + \gamma^{(x_7)}\partial_7\big)\Phi \\
& \qquad + \tan z\,\gamma^{(x_8)}\partial_8\Phi + 3H\,\gamma^{(x_8)}\Phi = \big(m + U'(S)\big)\,\Phi ,
\end{aligned}
$$

and the adjoint equation

$$
\begin{aligned}
& e^{-a_4}\sin^{-1/6}z\,\big(\partial_1\bar\Phi\,\gamma^{(x_1)} + \partial_2\bar\Phi\,\gamma^{(x_2)} + \partial_3\bar\Phi\,\gamma^{(x_3)}\big) + \partial_4\bar\Phi\,\gamma^{(x_4)} \\
& \qquad + e^{a_4}\sin^{-1/6}z\,\big(\partial_5\bar\Phi\,\gamma^{(x_5)} + \partial_6\bar\Phi\,\gamma^{(x_6)} + \partial_7\bar\Phi\,\gamma^{(x_7)}\big) \\
& \qquad + \tan z\,\partial_8\bar\Phi\,\gamma^{(x_8)} + 3H\,\bar\Phi\,\gamma^{(x_8)} = -\big(m + U'(S)\big)\,\bar\Phi .
\end{aligned}
$$

The derivative coefficients are $1/f_a$: the inverse 3-space scale factor $e^{-a_4}\sin^{-1/6}z$, the inverse extra-time scale factor $e^{a_4}\sin^{-1/6}z$ (it grows as the extra times deflate) and $\tan z$ for the hidden direction; the last term on the left is the spin-connection term.

**Evolution form.** Since $(\gamma^{(x_4)})^2 = -1$, the field equation is equivalent to the first-order evolution equation

$$
\partial_4\Phi = -\gamma^{(x_4)}\Big[\big(m + U'(S)\big)\Phi - \sum_{a \ne x_4}\frac{1}{f_a}\,\gamma^{(a)}\partial_a\Phi - 3H\,\gamma^{(x_8)}\Phi\Big] ;
$$

the slices $x_4 = \mathrm{const}$ are non-characteristic ($g^{44} = -1 \ne 0$).

**Chiral block form.** With $\Phi = (\varphi_-, \varphi_+)$ ($\Gamma = -1$ on rows 1-8, $\Gamma = +1$ on rows 9-16) every gamma is block off-diagonal, with $8\times8$ blocks $\bar\tau_a$ (upper right) and $\tau_a$ (lower left) listed in `Revision/theory/field-theory.json` (`field_equation_blocks`), and the field equation is the pair

$$
\sum_a \frac{1}{f_a}\,\bar\tau_a\,\partial_a\varphi_+ + 3H\,\bar\tau_{x_8}\varphi_+ = V\varphi_-, \qquad \sum_a \frac{1}{f_a}\,\tau_a\,\partial_a\varphi_- + 3H\,\tau_{x_8}\varphi_- = V\varphi_+ .
$$

The mass term and the gravitational term $3H$ both couple the two chiral halves.

**The 16 component equations.** With $u = e^{-a_4}\sin^{-1/6}z$, $v = e^{a_4}\sin^{-1/6}z$, $t = \tan z$, $V = m + U'(S)$ and $\Phi_A$ the components in the row order of `Revision/algebra/gammas.json`, the equation $(\gamma^\mu D_\mu\Phi)_A = V\Phi_A$ reads (generated from `field_equation_components` of `Revision/theory/field-theory.json`, which the sympy record compares term by term):

$$
\begin{aligned}
(1)\;\; & -\partial_4\Phi_{14} + u\,(-\partial_1\Phi_{16} + \partial_2\Phi_{15} - \partial_3\Phi_{14}) \\
& + v\,(\partial_5\Phi_{15} + \partial_6\Phi_{16} + \partial_7\Phi_{9}) + (t\,\partial_8 + 3H)\,\Phi_{9} = V\,\Phi_{1} \\
(2)\;\; & \partial_4\Phi_{13} + u\,(-\partial_1\Phi_{15} - \partial_2\Phi_{16} + \partial_3\Phi_{13}) \\
& + v\,(\partial_5\Phi_{16} - \partial_6\Phi_{15} + \partial_7\Phi_{10}) + (t\,\partial_8 + 3H)\,\Phi_{10} = V\,\Phi_{2} \\
(3)\;\; & \partial_4\Phi_{16} + u\,(\partial_1\Phi_{14} - \partial_2\Phi_{13} - \partial_3\Phi_{16}) \\
& + v\,(-\partial_5\Phi_{13} + \partial_6\Phi_{14} + \partial_7\Phi_{11}) + (t\,\partial_8 + 3H)\,\Phi_{11} = V\,\Phi_{3} \\
(4)\;\; & -\partial_4\Phi_{15} + u\,(\partial_1\Phi_{13} + \partial_2\Phi_{14} + \partial_3\Phi_{15}) \\
& + v\,(-\partial_5\Phi_{14} - \partial_6\Phi_{13} + \partial_7\Phi_{12}) + (t\,\partial_8 + 3H)\,\Phi_{12} = V\,\Phi_{4}
\end{aligned}
$$

$$
\begin{aligned}
(5)\;\; & \partial_4\Phi_{10} + u\,(-\partial_1\Phi_{12} + \partial_2\Phi_{11} - \partial_3\Phi_{10}) \\
& + v\,(-\partial_5\Phi_{11} - \partial_6\Phi_{12} - \partial_7\Phi_{13}) + (t\,\partial_8 + 3H)\,\Phi_{13} = V\,\Phi_{5} \\
(6)\;\; & -\partial_4\Phi_{9} + u\,(-\partial_1\Phi_{11} - \partial_2\Phi_{12} + \partial_3\Phi_{9}) \\
& + v\,(-\partial_5\Phi_{12} + \partial_6\Phi_{11} - \partial_7\Phi_{14}) + (t\,\partial_8 + 3H)\,\Phi_{14} = V\,\Phi_{6} \\
(7)\;\; & -\partial_4\Phi_{12} + u\,(\partial_1\Phi_{10} - \partial_2\Phi_{9} - \partial_3\Phi_{12}) \\
& + v\,(\partial_5\Phi_{9} - \partial_6\Phi_{10} - \partial_7\Phi_{15}) + (t\,\partial_8 + 3H)\,\Phi_{15} = V\,\Phi_{7} \\
(8)\;\; & \partial_4\Phi_{11} + u\,(\partial_1\Phi_{9} + \partial_2\Phi_{10} + \partial_3\Phi_{11}) \\
& + v\,(\partial_5\Phi_{10} + \partial_6\Phi_{9} - \partial_7\Phi_{16}) + (t\,\partial_8 + 3H)\,\Phi_{16} = V\,\Phi_{8}
\end{aligned}
$$

$$
\begin{aligned}
(9)\;\; & \partial_4\Phi_{6} + u\,(\partial_1\Phi_{8} - \partial_2\Phi_{7} + \partial_3\Phi_{6}) \\
& + v\,(-\partial_5\Phi_{7} - \partial_6\Phi_{8} - \partial_7\Phi_{1}) + (t\,\partial_8 + 3H)\,\Phi_{1} = V\,\Phi_{9} \\
(10)\;\; & -\partial_4\Phi_{5} + u\,(\partial_1\Phi_{7} + \partial_2\Phi_{8} - \partial_3\Phi_{5}) \\
& + v\,(-\partial_5\Phi_{8} + \partial_6\Phi_{7} - \partial_7\Phi_{2}) + (t\,\partial_8 + 3H)\,\Phi_{2} = V\,\Phi_{10} \\
(11)\;\; & -\partial_4\Phi_{8} + u\,(-\partial_1\Phi_{6} + \partial_2\Phi_{5} + \partial_3\Phi_{8}) \\
& + v\,(\partial_5\Phi_{5} - \partial_6\Phi_{6} - \partial_7\Phi_{3}) + (t\,\partial_8 + 3H)\,\Phi_{3} = V\,\Phi_{11} \\
(12)\;\; & \partial_4\Phi_{7} + u\,(-\partial_1\Phi_{5} - \partial_2\Phi_{6} - \partial_3\Phi_{7}) \\
& + v\,(\partial_5\Phi_{6} + \partial_6\Phi_{5} - \partial_7\Phi_{4}) + (t\,\partial_8 + 3H)\,\Phi_{4} = V\,\Phi_{12}
\end{aligned}
$$

$$
\begin{aligned}
(13)\;\; & -\partial_4\Phi_{2} + u\,(\partial_1\Phi_{4} - \partial_2\Phi_{3} + \partial_3\Phi_{2}) \\
& + v\,(\partial_5\Phi_{3} + \partial_6\Phi_{4} + \partial_7\Phi_{5}) + (t\,\partial_8 + 3H)\,\Phi_{5} = V\,\Phi_{13} \\
(14)\;\; & \partial_4\Phi_{1} + u\,(\partial_1\Phi_{3} + \partial_2\Phi_{4} - \partial_3\Phi_{1}) \\
& + v\,(\partial_5\Phi_{4} - \partial_6\Phi_{3} + \partial_7\Phi_{6}) + (t\,\partial_8 + 3H)\,\Phi_{6} = V\,\Phi_{14} \\
(15)\;\; & \partial_4\Phi_{4} + u\,(-\partial_1\Phi_{2} + \partial_2\Phi_{1} + \partial_3\Phi_{4}) \\
& + v\,(-\partial_5\Phi_{1} + \partial_6\Phi_{2} + \partial_7\Phi_{7}) + (t\,\partial_8 + 3H)\,\Phi_{7} = V\,\Phi_{15} \\
(16)\;\; & -\partial_4\Phi_{3} + u\,(-\partial_1\Phi_{1} - \partial_2\Phi_{2} - \partial_3\Phi_{3}) \\
& + v\,(-\partial_5\Phi_{2} - \partial_6\Phi_{1} + \partial_7\Phi_{8}) + (t\,\partial_8 + 3H)\,\Phi_{8} = V\,\Phi_{16}
\end{aligned}
$$

In every component the gravitational term $3H\,\Phi_B$ appears next to the hidden-direction derivative $\tan z\,\partial_8\Phi_B$ of the same component $B$ ($\gamma^{(x_8)}$ is a permutation matrix with entries $+1$).

**Exact solutions used as test points.** They satisfy the field equation for every $a_4$.

- $U = 0$: $\Phi = \sin^{\alpha}z\,\big(\cosh(kx_4) + \tfrac{\sinh(kx_4)}{k}M\big)\chi$ with constant $\chi$ (16 free complex constants), $M = -m\gamma^{(x_4)} + 3H(2\alpha + 1)\gamma^{(x_4)}\gamma^{(x_8)}$, $k^2 = 9H^2(2\alpha+1)^2 - m^2$ and $\alpha$ arbitrary; $M^2 = k^2$ and $M^TC + CM = 0$. Honest scope: at these solutions the pressures and the momentum density vanish and $\rho = mS$ is constant in $x_4$, so they test the terms $\tan z\,\gamma^{(x_8)}\partial_8$ and $3H\gamma^{(x_8)}$ but are a weak test of conservation; the general proof of conservation is the Noether identity of section 7.
- $U = \tfrac{\lambda}{2}S^2$, homogeneous (nonlinear): $\Phi = \big(\cosh(kx_4) + \tfrac{\sinh(kx_4)}{k}M\big)\chi$, $M = -(m + \lambda S_0)\gamma^{(x_4)} + 3H\gamma^{(x_4)}\gamma^{(x_8)}$, $S_0 = \chi^\dagger C\chi$, $k^2 = 9H^2 - (m + \lambda S_0)^2$: $S = S_0$ is constant, the field equation holds, $\nabla_\mu T^\mu{}_\nu = 0$ for all $\nu$, and $\rho = mS_0 + \lambda S_0^2/2$, $p = \lambda S_0^2/2$.

| statement | Wolfram checks (theory) | sympy checks (theory) |
| --- | --- | --- |
| Euler-Lagrange equations derived from $\mathcal{L}$ | `EL_Psibar_C`, `EL_Psi_C` | `commuting_euler_lagrange_psibar_variation`, `commuting_euler_lagrange_psi_variation` |
| the adjoint equation is the Dirac conjugate | `adjoint_equation_is_Dirac_conjugate_C` | `commuting_adjoint_equation_is_conjugate` |
| explicit form, 16 components, chiral blocks | `Dirac_operator_explicit_C`, `block_form` | `commuting_euler_lagrange_psibar_variation` (the sympy field equation), compared term by term with `field_equation_components` and entry by entry with `field_equation_blocks` in the regenerated comparison record (section `comparison_with_wolfram` of the sympy report: 32 of 32 formula records agree) |
| evolution form | `evolution_form_C` | |
| exact solutions | `solution_matrix_square`, `exact_solution_x4_x8_C`, `exact_solution_nonlinear_homogeneous_C` | `exact_solution_family_x4_x8`, `exact_nonlinear_homogeneous_solution` |

## 6. Non-triviality [2]: theorem and proof

The author's requirement [2]: the Lagrangian of dirac16complex00 must be non-trivial, i.e. its Euler-Lagrange equations always possess nonzero contributions from gravity through the canonical spin connection unless the spacetime is flat 4+4, and they must be self-consistent, checked and verified.

**Theorem (NON-TRIVIALITY [2]).** Hypotheses: the author's metric of section 1 with $H > 0$ and $0 < z < \pi/2$; $a_4$ any differentiable function of $x_4$ (constant included); the diagonal vielbein of section 3 and its canonical spin connection; $\Phi$ the commuting 16-component field with the Lagrangian of section 4 and any real potential $U$. Then statements (1) to (4) hold. Statements (1) and (2) concern the diagonal vielbein and the field variables $\Phi$; statements (3) and (4) are the frame-independent content (see "Scope of [2]" below).

**(1) The gravitational term of the field equation.** The spin-connection part of the Euler-Lagrange operator is

$$
\gamma^\mu D_\mu\Phi - \gamma^\mu\partial_\mu\Phi = \gamma^\mu\Omega_\mu\,\Phi, \qquad \gamma^\mu\Omega_\mu = 3H\,\gamma^{(x_8)} ,
$$

a constant matrix, independent of $a_4$, $x_4$ and $x_8$. The term $3H\gamma^{(x_8)}\Phi$ is nonzero for every $H > 0$ and every $\Phi \ne 0$, because $\gamma^{(x_8)}$ is invertible, $(\gamma^{(x_8)})^2 = 1$.

**(2) What cancels and what survives.** Per direction (no sum)

$$
\begin{aligned}
\gamma^{x_i}\Omega_{x_i} &= \tfrac{a_4'}{2}\,\gamma^{(x_4)} + \tfrac{H}{2}\,\gamma^{(x_8)} \qquad (i = x_1, x_2, x_3), \\
\gamma^{x_t}\Omega_{x_t} &= -\tfrac{a_4'}{2}\,\gamma^{(x_4)} + \tfrac{H}{2}\,\gamma^{(x_8)} \qquad (t = x_5, x_6, x_7),
\end{aligned}
$$

and $\gamma^{x_4}\Omega_{x_4} = \gamma^{x_8}\Omega_{x_8} = 0$. The time-direction ($\gamma^{(x_4)}$) terms of the 3 inflating and the 3 deflating directions cancel exactly, $3a_4'/2 - 3a_4'/2 = 0$; the hidden-direction ($\gamma^{(x_8)}$) terms of all six directions add, $6 \cdot H/2 = 3H$.

**(3) It vanishes only in flat 4+4 space.** $\Omega_\mu = 0$ for all $\mu$ if and only if $a_4' = 0$ and $H = 0$; $H = 0$ is a degenerate limit outside the family, so for every admissible metric the spin connection is nonzero. No choice of frame removes it: $[D_\mu, D_\nu] = \tfrac12 R_{ab\mu\nu}S^{ab}$ and $R^{x_8}{}_{x_8} = -6H^2 \ne 0$.

**(4) The vielbein in every derivative term.** Gravity also enters every derivative term,

$$
\gamma^\mu\partial_\mu = e^{-a_4}\sin^{-1/6}z\,\gamma^{(x_i)}\partial_i + \gamma^{(x_4)}\partial_4 + e^{a_4}\sin^{-1/6}z\,\gamma^{(x_t)}\partial_t + \tan z\,\gamma^{(x_8)}\partial_8
$$

(sums over $i$ and $t$), none of the factors being identically 1; $a_4$ enters the field equation only through these factors (its spin-connection terms cancel by (2)).

**Proof.** Step (a), the inflating directions $i = x_1, x_2, x_3$: by section 3

$$
\gamma^{x_i} = e^{-a_4}\sin^{-1/6}z\,\gamma^{(x_i)}, \qquad \Omega_{x_i} = \tfrac12 e^{a_4}\sin^{1/6}z\,\big(a_4'\gamma^{(x_i)}\gamma^{(x_4)} + H\gamma^{(x_i)}\gamma^{(x_8)}\big) .
$$

The scale factors cancel and $(\gamma^{(x_i)})^2 = \eta^{ii} = +1$, so $\gamma^{x_i}\Omega_{x_i} = \tfrac12(a_4'\gamma^{(x_4)} + H\gamma^{(x_8)})$.

Step (b), the deflating extra times $t = x_5, x_6, x_7$:

$$
\gamma^{x_t} = e^{a_4}\sin^{-1/6}z\,\gamma^{(x_t)}, \qquad \Omega_{x_t} = -\tfrac12 e^{-a_4}\sin^{1/6}z\,\big(a_4'\gamma^{(x_4)}\gamma^{(x_t)} + H\gamma^{(x_t)}\gamma^{(x_8)}\big) .
$$

With $\gamma^{(x_t)}\gamma^{(x_4)}\gamma^{(x_t)} = -\gamma^{(x_4)}(\gamma^{(x_t)})^2 = \gamma^{(x_4)}$ and $(\gamma^{(x_t)})^2 = -1$ this gives $\gamma^{x_t}\Omega_{x_t} = -\tfrac12(a_4'\gamma^{(x_4)} - H\gamma^{(x_8)})$.

Step (c): $\Omega_{x_4} = \Omega_{x_8} = 0$. Summing (a), (b) and (c) gives statements (1) and (2). Equivalently, since $\{\gamma^\mu, \Omega_\mu\} = 0$ for each $\mu$,

$$
\gamma^\mu\Omega_\mu = \frac{1}{2\sqrt{|g|}}\,\partial_\mu\big(\sqrt{|g|}\,e_a{}^\mu\big)\gamma^{(a)} ;
$$

only $\mu = x_8$ contributes: $\sqrt{|g|}\,e_{x_8}{}^{x_8} = \cos z\tan z = \sin z$ and $\tfrac{1}{2\cos z}\partial_8\sin z = 3H$, while $\partial_4(\sqrt{|g|}\,e_{x_4}{}^{x_4}) = \partial_4\cos z = 0$.

Step (d): each of the 12 nonzero $\omega_{\mu ab}$ is $a_4'$ or $H$ times $\pm e^{\pm a_4}\sin^{1/6}z \ne 0$, and the $S^{ab}$ are linearly independent; this gives statement (3), with the curvature statement from the integrability identity and the Ricci components of section 3.

Step (e): statement (4) is the explicit form of section 5. Every step is verified exactly, for the author's T16 and, in the $a_4$ record, also for a second, independently built Clifford representation. $\square$

**What survives and what cancels, in words.** The three inflating directions contribute $+\tfrac{a_4'}{2}\gamma^{(x_4)}$ each and the three deflating extra times $-\tfrac{a_4'}{2}\gamma^{(x_4)}$ each: the expansion-rate terms cancel exactly because 3-space inflates at the rate at which the extra times deflate (the same balance that makes $\sqrt{|g|} = \cos z$ independent of $x_4$). The warp $\sin^{1/6}z$ of the six directions along the hidden direction gives $+\tfrac{H}{2}\gamma^{(x_8)}$ for each of them and survives as $3H\gamma^{(x_8)}$.

**Scope of [2] (exact).** The value $\gamma^\mu\Omega_\mu = 3H\gamma^{(x_8)}$ belongs to the diagonal vielbein and to the field variables $\Phi$:

- In another admissible vielbein of the same metric, the frame boosted in the $(x_4, x_8)$ plane, $e'^{(x_4)} = \cosh b\,e^{(x_4)} + \sinh b\,e^{(x_8)}$, $e'^{(x_8)} = \sinh b\,e^{(x_4)} + \cosh b\,e^{(x_8)}$ with rapidity $b = \beta x_4 + b_0$, its canonical connection gives $\gamma'^\mu\Omega'_\mu = \tfrac{6H - \beta}{2}(\cosh b\,\gamma^{(x_8)} - \sinh b\,\gamma^{(x_4)})$, which vanishes identically for $\beta = 6H$, for every $H > 0$ and every $a_4$.
- Within the diagonal frame the rescaling $\Phi = \sin^{-1/2}z\,\chi$ removes the term exactly: $\gamma^\mu D_\mu\Phi = \sin^{-1/2}z\,\gamma^\mu\partial_\mu\chi$, so for $U = 0$ the equation for $\chi$ has no spin-connection term, and for $U = \tfrac{\lambda}{2}S^2$ the term becomes the $x_8$-dependent coupling $\lambda S[\chi]/\sin z$. The exact family of section 5 shows this: $\alpha = -\tfrac12$ gives $M = -m\gamma^{(x_4)}$ with no $H$ term.
- The canonical connection drops out of $\mathcal{L}$ (section 4), so the Euler-Lagrange equations are those of the connection-free symmetric Lagrangian; the deflation $a_4$ contributes nothing to $\gamma^\mu\Omega_\mu$ although $R^{x_4}{}_{x_4} = 6(a_4')^2 \neq 0$.
- What cannot be removed in any frame is $\Omega_\mu$ itself (its curvature is the Riemann tensor, $R^{x_8}{}_{x_8} = -6H^2$), together with the frame factors $e^{\mp a_4}\sin^{-1/6}z$ and $\tan z$ of the derivative terms: this is the frame-independent content of [2]. In the diagonal frame the connection also enters the energy-momentum tensor (for a homogeneous configuration $K^{x_4}{}_{x_1}$ contains $\tfrac12 e^{a_4}\sin^{1/6}z\,H\,\bar\Phi\gamma^{(x_4)}\gamma^{(x_1)}\gamma^{(x_8)}\Phi$).
- Interpretation (labelled): in the quantum theory of dirac16complex the term makes the hidden-direction operator antisymmetric for the measure $\cos z\,dx_8$ in the variables $\Psi$, up to a boundary term that does not vanish at $z = \pi/2$; in the variables $\chi$ with the measure $dy = \cot z\,dx_8$ no $H$ term is needed. This role therefore depends on the variables and the measure.

| statement | Wolfram checks | sympy checks |
| --- | --- | --- |
| (1) $\gamma^\mu\Omega_\mu = 3H\gamma^{(x_8)}$, nonzero for every $\Phi \ne 0$ | `nontriviality_2_dirac16complex00`, `gammaOmega_equals_3H_gamma_x8` (theory); `gravity_term_gamma_mu_Omega_mu` ($a_4$ record) | `gamma_mu_Omega_mu_equals_3H_gamma_x8` (theory); `ownrep_gravity_term`, `authorT16_gravity_term` ($a_4$ record) |
| (2) the $x_4$ terms cancel, the $x_8$ terms add | `gammaOmega_x4_terms_cancel`, `gammaOmega_divergence_form` | `time_terms_cancel_hidden_term_survives`, `divergence_of_sqrtg_gamma` |
| (3) $\Omega_\mu = 0$ only for $a_4' = 0$ and $H = 0$; never flat | `Omega_vanishes_iff_a4prime_and_H_vanish`, `never_flat_for_H_positive`, `spin_curvature_equals_Riemann` | `nontriviality_Omega_zero_iff_flat`, `curvature_nonzero_flat_only_formally`, `spinor_curvature_equals_riemann` |
| (4) explicit operator | `Dirac_operator_explicit_C` | |
| the same term in the quantum theory of dirac16complex (up to a boundary term) | `good_sector_hermiticity_curved`, `good_sector_hermiticity_up_to_the_brane_flux` (scope) | `good_sector_hermiticity_up_to_the_brane_flux` (scope) |
| scope: the boosted frame removes $\gamma^\mu\Omega_\mu$, not $\Omega_\mu$ | `boosted_frame_reproduces_metric`, `boosted_frame_canonical_connection`, `boosted_frame_gammaOmega_formula`, `boosted_frame_gammaOmega_vanishes`, `boosted_frame_curvature_nonzero` (scope) | the same five names (scope) |
| scope: rescaling, deflation, energy-momentum tensor | `rescaling_removes_the_connection_term`, `rescaled_equation_quadratic_potential`, `gammaOmega_blind_to_the_deflation`, `spin_connection_in_the_energy_momentum_tensor` (scope) | the same four names (scope) |

## 7. Self-consistency of the field equations

All statements are exact and verified for the commuting field.

**Reality and derivation.** $\mathcal{L}$ is real; the Euler-Lagrange equations derived from it are the field equation and its Dirac conjugate (sections 4 and 5).

**Integrability of the connection.** For all 28 pairs,

$$
[D_\mu, D_\nu]\Phi = \big(\partial_\mu\Omega_\nu - \partial_\nu\Omega_\mu + [\Omega_\mu, \Omega_\nu]\big)\Phi = \tfrac12 R_{ab\mu\nu}S^{ab}\Phi .
$$

**Second-order consistency (Lichnerowicz identity).** Identically for a general field,

$$
(\gamma^\mu D_\mu)^2\Phi = g^{\mu\nu}\big(D_\mu D_\nu - \Gamma^\lambda{}_{\mu\nu}D_\lambda\big)\Phi - \frac{R}{4}\,\Phi, \qquad R = 6\big((a_4')^2 - 7H^2\big),
$$

and $\gamma^\mu\gamma^\nu F_{\mu\nu} = -\tfrac{R}{2}$ for the spinor curvature $F_{\mu\nu} = [D_\mu, D_\nu]$.

**Cauchy problem.** The equation is first order in $x_4$ with non-characteristic slices (evolution form, section 5). This does not make the Cauchy problem well posed, and it is not listed here as a self-consistency property: for data that depend on the extra times the growth rates of the modes have no upper bound (with frozen coefficients $k_5 = K$ gives the rate $\sqrt{K^2 - m^2 - k_1^2 - k_2^2 - k_3^2 - k_8^2}$; Hadamard ill-posedness), and in the good sector, without a boundary condition at $z = \pi/2$, the $x_8$-independent modes grow whenever $m^2 < 9H^2$ (for $U = 0$; the matrix $-im\gamma^{(x_4)} + 3iH\gamma^{(x_4)}\gamma^{(x_8)}$ has square $(m^2 - 9H^2)I_{16}$).

**Conserved current.** $J^\mu = -i\bar\Phi\gamma^\mu\Phi$ is real, and off shell

$$
\partial_\mu\big(\sqrt{|g|}\,J^\mu\big) = -i\sqrt{|g|}\,\big(\bar E\Phi + \bar\Phi E\big),
$$

with $E = \gamma^\mu D_\mu\Phi - (m + U'(S))\Phi$ and $\bar E = (D_\mu\bar\Phi)\gamma^\mu + (m + U'(S))\bar\Phi$ (the convention of the Wolfram record), so $\nabla_\mu J^\mu = 0$ on shell. The charge density is $J^{x_4} = \Phi^\dagger B\Phi$, and the conserved charge $Q = \int\cos z\,\Phi^\dagger B\Phi\,d^7x$ is an indefinite form ($B$ has signature (8,8)).

**Bianchi-type identity of the energy-momentum tensor.** The off-shell Noether identity of diffeomorphism invariance,

$$
\partial_\mu\big(\sqrt{|g|}\,T^\mu{}_\lambda\big) - \sqrt{|g|}\,T^\mu{}_a\,\partial_\lambda e^a{}_\mu = \sum_\phi \mathrm{EL}_\phi\,\partial_\lambda\phi \qquad (\lambda = x_1, \ldots, x_8),
$$

and the off-shell identity of local Lorentz invariance (the antisymmetric part of $T$ is a combination of the Euler-Lagrange expressions $\mathrm{EL}_\phi$) give: on shell $T$ is symmetric and $\nabla_\mu T^\mu{}_\nu = 0$, exactly, for general solutions.

**Gravity side.** Each Lovelock tensor is divergence-free, $\nabla_\mu E_{(k)}{}^\mu{}_\nu = 0$, and the constraint is propagated by the evolution equation (section 11).

**Test points.** The exact solutions of section 5 satisfy the field equation, current conservation and $\nabla_\mu T^\mu{}_\nu = 0$ exactly.

| statement | Wolfram checks (theory) | sympy checks (theory) |
| --- | --- | --- |
| integrability $[D_\mu, D_\nu] = \tfrac12 R_{ab\mu\nu}S^{ab}$ | `spin_curvature_equals_Riemann` | `spinor_curvature_equals_riemann` |
| Lichnerowicz identity | `Lichnerowicz_identity_C` | `lichnerowicz_identity_on_fields`, `lichnerowicz_contraction` |
| current: reality, conservation, indefinite charge | `current_real_C`, `current_conservation_identity_C`, `charge_density_is_Krein_form_C` | `commuting_current_conservation` |
| Noether identities and conservation of $T$ | `Noether_identity_diffeomorphisms_C`, `Noether_identity_local_Lorentz_C`, `conservation_on_shell_general` | `commuting_emt_conservation_on_shell`, `commuting_emt_conservation_negative_control` |
| no well-posed Cauchy problem: unbounded growth, growing good-sector modes without a boundary condition | `extra_time_growth_rates_unbounded`, `good_sector_x8_independent_modes_without_boundary_condition` (scope) | the same two names (scope) |

## 8. The energy-momentum tensor (classical bilinears)

For dirac16complex00 the energy-momentum tensor is the classical bilinear (a c-number function of $\Phi$; no operator ordering, no normal ordering).

**Definition and closed form.** $T^\nu{}_\mu = e^b{}_\mu\,\tfrac{1}{\sqrt{|g|}}\,\delta S_{\mathrm{act}}/\delta e^b{}_\nu$ (exact first-order variation of $\sqrt{|g|}$, $\gamma^\mu$ and the spin connection; $S_{\mathrm{act}}$ the action) equals, for all 64 components,

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
\rho = -T^{x_4}{}_{x_4}, \qquad p_3 = T^{x_1}{}_{x_1}, \qquad p_t = T^{x_5}{}_{x_5}, \qquad p_8 = T^{x_8}{}_{x_8} .
$$

**Diagonal components in the primordial field.** With the kinetic term of direction $\mu$ (no sum)

$$
K_\mu = \frac{1}{2f_\mu}\big(\bar\Phi\gamma^{(\mu)}\partial_\mu\Phi - \partial_\mu\bar\Phi\,\gamma^{(\mu)}\Phi\big),
$$

that is

$$
\begin{aligned}
K_{x_i} &= \tfrac12 e^{-a_4}\sin^{-1/6}z\,\big(\bar\Phi\gamma^{(x_i)}\partial_i\Phi - \partial_i\bar\Phi\,\gamma^{(x_i)}\Phi\big), \qquad K_{x_4} = \tfrac12\big(\bar\Phi\gamma^{(x_4)}\partial_4\Phi - \partial_4\bar\Phi\,\gamma^{(x_4)}\Phi\big), \\
K_{x_t} &= \tfrac12 e^{a_4}\sin^{-1/6}z\,\big(\bar\Phi\gamma^{(x_t)}\partial_t\Phi - \partial_t\bar\Phi\,\gamma^{(x_t)}\Phi\big), \qquad K_{x_8} = \tfrac12\tan z\,\big(\bar\Phi\gamma^{(x_8)}\partial_8\Phi - \partial_8\bar\Phi\,\gamma^{(x_8)}\Phi\big),
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
p_t &= \sum_{\mu \ne x_5} K_\mu - mS - U(S), \qquad p_8 = \sum_{\mu \ne x_8} K_\mu - mS - U(S) .
\end{aligned}
$$

**The $x_4$-$x_8$ component** (the off-diagonal component allowed by the symmetry of the metric; $\Omega_{x_4} = \Omega_{x_8} = 0$):

$$
\begin{aligned}
& T^{x_4}{}_{x_8} = -\tfrac14\big(B_{48} - \cot z\,B_{84}\big), \qquad T^{x_8}{}_{x_4} = -\tan^2 z\;T^{x_4}{}_{x_8}, \\
& B_{48} = \bar\Phi\gamma^{(x_4)}\partial_8\Phi - \partial_8\bar\Phi\,\gamma^{(x_4)}\Phi, \qquad B_{84} = \bar\Phi\gamma^{(x_8)}\partial_4\Phi - \partial_4\bar\Phi\,\gamma^{(x_8)}\Phi ;
\end{aligned}
$$

it vanishes on homogeneous on-shell states.

**Trace.** Off shell $T^\mu{}_\mu = 8L_0 - \sum_\mu K_\mu = 7\sum_\mu K_\mu - 8(mS + U)$. Exactly, $\sum_\mu K_\mu = (m + U')S + \tfrac12(\bar\Phi E - \bar E\Phi)$, so on shell $\sum_\mu K_\mu = (m + U'(S))S$, $L_0 = S\,U'(S) - U(S)$ and

$$
T^\mu{}_\mu = -mS + 7S\,U'(S) - 8U(S) = -mS + 3\lambda S^2 \quad (U = \tfrac{\lambda}{2}S^2) .
$$

**Conservation and energy exchange.** For a diagonal homogeneous tensor

$$
T = \mathrm{diag}(p_3, p_3, p_3, -\rho, p_t, p_t, p_t, p_8)(x_4)
$$

one has $\nabla_\mu T^\mu{}_{x_4} = -\rho' - 3a_4'(p_3 - p_t)$ and $\nabla_\mu T^\mu{}_{x_8} = 3H\cot z\,(2p_8 - p_3 - p_t)$, so conservation gives

$$
\frac{d\rho}{dx_4} = -3\,a_4'\,(p_3 - p_t), \qquad p_3 + p_t = 2p_8 :
$$

energy flows between 3-space and the extra times unless $p_3 = p_t$, since $\sqrt{|g|}$ does not depend on $x_4$.

| statement | Wolfram checks (theory) | sympy checks (theory) |
| --- | --- | --- |
| variation tensor in closed form | `T_vielbein_variation_closed_form_C` | `commuting_emt_equals_general_vielbein_variation_on_shell` |
| Belinfante tensor, symmetric | `T_symmetric_part_Belinfante_C` | `commuting_emt_symmetric` |
| normalisation $\delta S_{\mathrm{act}} = \tfrac12\int\sqrt{\lvert g\rvert}\,T^{\mu\nu}\delta g_{\mu\nu}$, diagonal components | `T_diagonal_components_C` | `commuting_emt_equals_vielbein_variation_diagonal` |
| $x_4$-$x_8$ component | `T_x4_x8_component_C` | `commuting_T_x4x8_homogeneous` |
| trace, on-shell kinetic sum | `EMT_trace_C`, `kinetic_sum_on_shell_C` | `commuting_trace_on_shell` |
| energy exchange and the $x_8$ condition | `energy_exchange_equation` | `energy_exchange_equation` |

## 9. Kinetic energy, potential energy, energy density and pressures

**Split.** $T^\nu{}_\mu = T_{\mathrm{kin}}{}^\nu{}_\mu + T_{\mathrm{pot}}{}^\nu{}_\mu$ with the potential part and the kinetic (derivative) part

$$
\begin{aligned}
T_{\mathrm{pot}}{}^\nu{}_\mu &= -\delta^\nu_\mu\,\big(mS + U(S)\big), \\
T_{\mathrm{kin}}{}^\nu{}_\mu &= \delta^\nu_\mu\sum_\lambda K_\lambda - \tfrac14\big(\bar\Phi\gamma^\nu D_\mu\Phi - D_\mu\bar\Phi\,\gamma^\nu\Phi + \bar\Phi\gamma_\mu D^\nu\Phi - D^\nu\bar\Phi\,\gamma_\mu\Phi\big)
\end{aligned}
$$

(formula `EMT_kinetic_potential` of `Revision/theory/field-theory.json`, compared with the sympy split).

**Densities** (per unit proper 7-volume; the energy in a region of a slice $x_4 = \mathrm{const}$ is the integral with the weight $\sqrt{|g|} = \cos z$):

| quantity | kinetic part | potential part | total |
| --- | --- | --- | --- |
| energy density $\rho = -T^{x_4}{}_{x_4}$ | $-\sum_{\mu \ne x_4} K_\mu$ | $mS + U(S)$ | $-\sum_{\mu \ne x_4} K_\mu + mS + U$ |
| 3-space pressure $p_3 = T^{x_1}{}_{x_1}$ | $\sum_{\mu \ne x_1} K_\mu$ | $-(mS + U)$ | $\sum_{\mu \ne x_1} K_\mu - mS - U$ |
| extra-time pressure $p_t = T^{x_5}{}_{x_5}$ | $\sum_{\mu \ne x_5} K_\mu$ | $-(mS + U)$ | $\sum_{\mu \ne x_5} K_\mu - mS - U$ |
| hidden-direction pressure $p_8 = T^{x_8}{}_{x_8}$ | $\sum_{\mu \ne x_8} K_\mu$ | $-(mS + U)$ | $\sum_{\mu \ne x_8} K_\mu - mS - U$ |

**Homogeneous states on shell** ($\Phi$ depending on $x_4$ only): $K_\mu = 0$ for $\mu \ne x_4$ and $K_{x_4} = (m + U'(S))S$. So the kinetic energy density vanishes, $-T_{\mathrm{kin}}{}^{x_4}{}_{x_4} = 0$, the kinetic pressure is $(m + U'(S))S$ in every direction, and

$$
\rho = m S + U(S), \qquad p_3 = p_t = p_8 = S\,U'(S) - U(S) ;
$$

for $U = \tfrac{\lambda}{2}S^2$: $\rho = mS + \tfrac{\lambda}{2}S^2$ and $p = \tfrac{\lambda}{2}S^2$ (formula `EMT_homogeneous_on_shell` of `Revision/theory/field-theory.json`; the exact nonlinear solution of section 5 realises these values). $S$ is constant along $x_4$ for a homogeneous solution, so $\rho$ and $p$ are constant, consistent with $d\rho/dx_4 = -3a_4'(p_3 - p_t) = 0$.

**Sign of the energy (exact).** The classical energy of dirac16complex00 is unbounded below already for $U = 0$ in the good sector. In the flat frame with $m = 2$ and $(k_1, k_2, k_3, k_8) = (1, 2, 0, 4)$, $E = 5$, the one-particle generator commutes with $B$ and its $E = 5$ eigenspace (dimension 8) contains vectors $u$ with $Bu = -u$ and with $Bu = +u$; the positive-frequency solutions $\Phi = c\,u\,e^{i(k\cdot x - 5x_4)}$ ($|u| = 1$) have the energy density $\rho = -T^{x_4}{}_{x_4} = -5|c|^2$ and $+5|c|^2$ and the charge density $\Phi^\dagger B\Phi = -|c|^2$ and $+|c|^2$ (`commuting_field_energy_unbounded_below`, both engines). By the Krein-inertia theorem of the pairing record (every real-frequency eigenspace has inertia (4,4), `Q_one_particle_Krein_inertia_real_frequencies`) such negative-energy modes exist at every real frequency. In the author's metric the homogeneous solutions of section 5 have $\rho = mS_0$ with $S_0 = \chi^\dagger C\chi$ of either sign. dirac16complex00 therefore has a negative-energy (ghost-like) sector at positive frequency, the classical form of the spin-statistics problem of a commuting field with a first-order Lagrangian; this matters for any reading of Hypothesis00, for example a phantom $w < -1$.

| statement | Wolfram checks | sympy checks |
| --- | --- | --- |
| homogeneous on-shell $\rho$, $p$; kinetic and potential parts | `exact_solution_nonlinear_homogeneous_C` (theory) | `commuting_homogeneous_on_shell_rho_p` (theory) |
| $S$ constant along $x_4$ for a homogeneous solution | `condensate_S_constant` ($a_4$ record) | `ownrep_condensate_S_constant`, `authorT16_condensate_S_constant` ($a_4$ record) |
| energy unbounded below, indefinite charge | `commuting_field_energy_unbounded_below` (scope), `Q_one_particle_Krein_inertia_real_frequencies` (pairing) | `commuting_field_energy_unbounded_below` (scope), `Q.one_particle_Krein_inertia_proof` (pairing) |

## 10. Equations of state

From the diagonal components (SPEC section 4):

$$
w_3 = \frac{p_3}{\rho}, \qquad w_t = \frac{p_t}{\rho}, \qquad w_8 = \frac{p_8}{\rho} .
$$

For homogeneous states on shell the three are equal,

$$
w_3 = w_t = w_8 = \frac{S\,U'(S) - U(S)}{mS + U(S)}, \qquad w = \frac{\lambda S}{2m + \lambda S} \quad (U = \tfrac{\lambda}{2}S^2)
$$

For $\lambda = 0$ the homogeneous state has $p = 0$ and $w = 0$. Because $S$, $\rho$ and $p$ are constant for a homogeneous solution, these ratios are constant in $x_4$.

| statement | source |
| --- | --- |
| definitions and homogeneous values of $w_3$, $w_t$, $w_8$ | formula `equation_of_state_definitions` of `Revision/theory/field-theory.json`; sympy check `commuting_homogeneous_on_shell_rho_p` |

Not computed in this document: the equation of state that a 3-space observer infers (after integrating over the hidden direction and the extra times), its time dependence as the extra times deflate, CPL parameters, and any comparison with supernova data. These belong to the dark-sector investigation of Hypothesis00 (SPEC section 8), a separate Revision record that is planned and not yet written.

## 11. The field equations for a4[x4]

**Einstein-Lovelock equations** (SPEC section 5):

$$
\sum_{k=1}^{3}\alpha_k\,E_{(k)}{}^\mu{}_\nu + \Lambda\,\delta^\mu_\nu = \kappa\,T^\mu{}_\nu, \qquad E_{(k)} = -\frac{P_{(k)}}{2^{k+1}}, \qquad E_{(1)} = G ,
$$

with $P_{(k)}{}^h{}_j$ the Lovelock tensors computed with the generalized Kronecker delta (GKD) from the Riemann tensor (MTW convention). $P_{(4)}$ vanishes in 8 dimensions (a GKD with 9 indices over 8 values), so $k = 1, 2, 3$ is the complete series. The components computed directly from the curvature equal the GKD record `Revision/gkd_lovelock/results/lovelock-tensors.json` monomial by monomial. The mixed Riemann components contain neither the warp nor $e^{a_4}$, so the left-hand sides depend on $H$, $a_4'$ and $a_4''$ only.

**The Lovelock components.** All off-diagonal components vanish (including $x_4$-$x_8$); $x_2 = x_3 = x_1$ and $x_6 = x_7 = x_5$:

$$
\begin{aligned}
E_{(1)}{}^{x_1}{}_{x_1} &= -3 (a_4')^2+a_4''+15 H^2, \qquad E_{(1)}{}^{x_4}{}_{x_4} = 3 (a_4')^2+21 H^2, \\
E_{(1)}{}^{x_5}{}_{x_5} &= -3 (a_4')^2-a_4''+15 H^2, \qquad E_{(1)}{}^{x_8}{}_{x_8} = 15 H^2-3 (a_4')^2, \\
E_{(2)}{}^{x_1}{}_{x_1} &= 12 (a_4')^4-24 (a_4')^2 a_4''+168 (a_4')^2 H^2-40 a_4'' H^2-180 H^4, \\
E_{(2)}{}^{x_4}{}_{x_4} &= -36 (a_4')^4-120 (a_4')^2 H^2-420 H^4, \\
E_{(2)}{}^{x_5}{}_{x_5} &= 12 (a_4')^4+24 (a_4')^2 a_4''+168 (a_4')^2 H^2+40 a_4'' H^2-180 H^4, \\
E_{(2)}{}^{x_8}{}_{x_8} &= 12 (a_4')^4+168 (a_4')^2 H^2-180 H^4,
\end{aligned}
$$

$$
\begin{aligned}
E_{(3)}{}^{x_1}{}_{x_1} &= -72 (a_4')^6+360 (a_4')^4 a_4''-648 (a_4')^4 H^2+432 (a_4')^2 a_4'' H^2 \\
&\quad -1944 (a_4')^2 H^4+360 a_4'' H^4+360 H^6, \\
E_{(3)}{}^{x_4}{}_{x_4} &= 360 (a_4')^6+648 (a_4')^4 H^2+1080 (a_4')^2 H^4+2520 H^6, \\
E_{(3)}{}^{x_5}{}_{x_5} &= -72 (a_4')^6-360 (a_4')^4 a_4''-648 (a_4')^4 H^2-432 (a_4')^2 a_4'' H^2 \\
&\quad -1944 (a_4')^2 H^4-360 a_4'' H^4+360 H^6, \\
E_{(3)}{}^{x_8}{}_{x_8} &= -72 (a_4')^6-648 (a_4')^4 H^2-1944 (a_4')^2 H^4+360 H^6 .
\end{aligned}
$$

Each $E_{(k)}$ is divergence-free, and $\sum_h P_{(k)}{}^h{}_h = (8 - 2k)L_{(k)}$.

**The independent equations for a general source** $T = \mathrm{diag}(p_3, p_3, p_3, -\rho, p_t, p_t, p_t, p_8)$ plus $q_{48} = T^{x_4}{}_{x_8}$ and $q_{84} = T^{x_8}{}_{x_4}$:

- constraint ($x_4$, first order in $a_4$): $\sum_k\alpha_k E_{(k)}{}^{x_4}{}_{x_4} + \Lambda = -\kappa\rho$;
- 3-space ($x_1 = x_2 = x_3$): $\sum_k\alpha_k E_{(k)}{}^{x_1}{}_{x_1} + \Lambda = \kappa p_3$;
- extra times ($x_5 = x_6 = x_7$): $\sum_k\alpha_k E_{(k)}{}^{x_5}{}_{x_5} + \Lambda = \kappa p_t$;
- hidden direction ($x_8$, first order in $a_4$): $\sum_k\alpha_k E_{(k)}{}^{x_8}{}_{x_8} + \Lambda = \kappa p_8$;
- off-diagonal: $0 = \kappa q_{48} = \kappa q_{84}$, and $0 = \kappa T^\mu{}_\nu$ for every other $\mu \ne \nu$.

**The evolution equation** (3-space minus extra time) contains $a_4''$ and is sourced by $p_3 - p_t$:

$$
a_4''\,F(a_4') = \kappa\,(p_3 - p_t), \qquad F = 720 (a_4')^4 \alpha_3-48 (a_4')^2 \alpha_2+864 (a_4')^2 \alpha_3 H^2+2 \alpha_1-80 \alpha_2 H^2+720 \alpha_3 H^4 ;
$$

$F$ vanishes identically only for $\alpha_1 = \alpha_2 = \alpha_3 = 0$.

**Consistency conditions.**

- Algebraic: $\sum_k\alpha_k(E^{x_1}{}_{x_1} + E^{x_5}{}_{x_5} - 2E^{x_8}{}_{x_8}) = 0$ identically, so the equations force $p_3+p_t = 2 p_8$.
- $x_8$-dependence: the left-hand sides are free of $x_8$ (and of $a_4$ itself), so every component of the source must be a function of $x_4$ alone and $q_{48} = q_{84} = 0$; an $x_8$-dependent source is not compatible with the metric of section 1.
- Isotropy: since the left-hand sides of $x_1, x_2, x_3$ coincide (and those of $x_5, x_6, x_7$), the source must have $T^{x_1}{}_{x_1} = T^{x_2}{}_{x_2} = T^{x_3}{}_{x_3}$ and $T^{x_5}{}_{x_5} = T^{x_6}{}_{x_6} = T^{x_7}{}_{x_7}$.
- Conservation: $\nabla_\mu T^\mu{}_{x_4} = -\partial_4\rho - 3a_4'(p_3 - p_t) + \partial_8 q_{84} - 6H\tan z\,q_{84}$ and $\nabla_\mu T^\mu{}_{x_8} = \partial_8 p_8 + 3H\cot z\,(2p_8 - p_3 - p_t) + \partial_4 q_{48}$; with an $x_8$-independent source and $q_{48} = q_{84} = 0$ they reduce to $\rho' = -3a_4'(p_3 - p_t)$ and $p_3 + p_t = 2p_8$, both implied by the field equations (Bianchi identity).
- Constraint propagation: $\tfrac{d}{dx_4}\sum_k\alpha_k E_{(k)}{}^{x_4}{}_{x_4} = 3a_4'\sum_k\alpha_k(E^{x_1}{}_{x_1} - E^{x_5}{}_{x_5})$ identically, so the derivative of the constraint is $3a_4'$ times the evolution equation once $\rho' = -3a_4'(p_3 - p_t)$ holds; for $a_4' \ne 0$ the evolution equation follows from the constraint and conservation.

**Einstein gravity** ($\alpha_1 = 1$, $\alpha_2 = \alpha_3 = 0$):

$$
\begin{aligned}
& 3 (a_4')^2+21 H^2+\Lambda = -\kappa  \rho, \qquad -3 (a_4')^2+a_4''+15 H^2+\Lambda = \kappa  p_3, \\
& -3 (a_4')^2-a_4''+15 H^2+\Lambda = \kappa  p_t, \qquad -3 (a_4')^2+15 H^2+\Lambda = \kappa  p_8, \\
& 2 a_4'' = \kappa  (p_3-p_t), \qquad \kappa  (p_8+\rho ) = -6 (a_4')^2-6 H^2 .
\end{aligned}
$$

Every $C^2$ function $a_4$ is allowed with the source it requires; that source always has $\kappa(\rho + p_8) = -6((a_4')^2 + H^2) < 0$ (for $\kappa > 0$ it violates the null energy condition along $x_4 + x_8$), and $T = 0$ has no solution for $H > 0$ and any $\Lambda$.

**The linear member $a_4 = A H x_4 + a_0$** ($a_4' = AH$, $a_4'' = 0$; 3-space scale factor $e^{AHx_4}$, extra-time scale factor $e^{-AHx_4}$: exponential deflation of the extra times for $A > 0$). For any $\alpha_k$ the field equations require $p_3 = p_t = p_8 = p$ and $\rho$, all constant, with

$$
\begin{aligned}
\rho &= -\frac{360 A^6 \alpha_3 H^6}{\kappa }+\frac{36 A^4 \alpha_2 H^4}{\kappa }-\frac{648 A^4 \alpha_3 H^6}{\kappa }-\frac{3 A^2 \alpha_1 H^2}{\kappa }+\frac{120 A^2 \alpha_2 H^4}{\kappa } \\
&\quad -\frac{1080 A^2 \alpha_3 H^6}{\kappa }-\frac{21 \alpha_1 H^2}{\kappa }+\frac{420 \alpha_2 H^4}{\kappa }-\frac{2520 \alpha_3 H^6}{\kappa }-\frac{\Lambda}{\kappa }, \\
p &= -\frac{72 A^6 \alpha_3 H^6}{\kappa }+\frac{12 A^4 \alpha_2 H^4}{\kappa }-\frac{648 A^4 \alpha_3 H^6}{\kappa }-\frac{3 A^2 \alpha_1 H^2}{\kappa }+\frac{168 A^2 \alpha_2 H^4}{\kappa } \\
&\quad -\frac{1944 A^2 \alpha_3 H^6}{\kappa }+\frac{15 \alpha_1 H^2}{\kappa }-\frac{180 \alpha_2 H^4}{\kappa }+\frac{360 \alpha_3 H^6}{\kappa }+\frac{\Lambda}{\kappa } ;
\end{aligned}
$$

a vacuum ($\rho = p = 0$) needs

$$
\mathcal{V} = 72 A^4 \alpha_3 H^4-8 A^2 \alpha_2 H^2+144 A^2 \alpha_3 H^4+\alpha_1-40 \alpha_2 H^2+360 \alpha_3 H^4 = 0,
$$

which in Einstein gravity ($\mathcal{V} = 1$) is impossible. The equations contain $A$ only through $A^2$: the deflating branch $A > 0$ ($a_4$ increasing) and the branch $A < 0$ satisfy the same equations.

| statement | Wolfram checks ($a_4$ record) | sympy checks ($a_4$ record) |
| --- | --- | --- |
| metric, volume, Riemann free of warp and $e^{a_4}$ | `metric_is_SPEC_section_1`, `sqrt_abs_det_g_is_cos_z`, `mixed_riemann_free_of_warp_and_a4` | `mixed_riemann_free_of_warp_and_a4`, `riemann_entries_laurent` |
| $P_{(k)}$ from the curvature equal the GKD record; traces; $P_{(4)} = 0$ | `P1_direct_equals_minus_4_Einstein`, `P1_direct_equals_gkd_branch_monomials`, `P2_direct_equals_gkd_branch_monomials`, `P3_direct_equals_gkd_branch_monomials`, `P1_trace_identity`, `P2_trace_identity`, `P3_trace_identity`, `P4_vanishes_pigeonhole` | `P1_equals_minus_4_Einstein`, `P1_equals_gkd_branch_monomials`, `P2_equals_gkd_branch_monomials`, `P3_equals_gkd_branch_monomials` |
| divergence-free $E_{(k)}$ | `E1_divergence_free`, `E2_divergence_free`, `E3_divergence_free` | `E1_divergence_free`, `E2_divergence_free`, `E3_divergence_free` |
| independent components, structure | `independent_components` | `other_components_vanish`, `json_lovelock_components`, `json_general_source_equations` |
| evolution equation and $F$ | `evolution_factorises_a4pp_times_F`, `evolution_F_not_identically_zero` | `evolution_factorises`, `evolution_F_not_identically_zero` |
| algebraic condition, first-order constraint and $x_8$ equation | `algebraic_identity_x1_plus_x5_minus_2x8`, `x8_component_contains_no_a4pp` | `algebraic_identity`, `constraint_and_x8_first_order` |
| conservation, constraint propagation | `conservation_components`, `constraint_propagation_bianchi` | `conservation_components`, `bianchi_x4` |
| Einstein case | `einstein_components`, `einstein_null_energy_x8`, `einstein_no_vacuum_solution` | `einstein_components`, `einstein_null_energy_x8`, `einstein_no_vacuum`, `json_einstein` |
| linear member | `linear_member_equal_pressures`, `linear_member_vacuum_factor` | `linear_member_equal_pressures`, `linear_member_vacuum_factor`, `json_linear_member` |

## 12. dirac16complex00 as the source of the a4 equations

**The tensor.** The source is the classical bilinear tensor of section 8. The $a_4$ record writes it as $T^\mu{}_\nu = \sigma_T\big(-K^{(\mu}{}_{\nu)} + \delta^\mu_\nu\,L_0\big)$ with $K^\mu{}_\nu = \tfrac12(\bar\Phi\gamma^\mu D_\nu\Phi - D_\nu\bar\Phi\,\gamma^\mu\Phi)$ symmetrised, and $\sigma_T = +1$; this is the Belinfante tensor of section 8 (whose symmetrised kinetic term is the same expression), so the two records use the same tensor and the same sign. With $k_\mu = K^\mu{}_\mu$ (no sum; equal to $K_\mu$ of section 8) and $L_0 = \sum_\mu k_\mu - mS - U(S)$:

$$
\rho = k_4 - L_0, \qquad p_3 = L_0 - k_1, \qquad p_t = L_0 - k_5, \qquad p_8 = L_0 - k_8, \qquad q_{48} = -K^{(x_4}{}_{x_8)} .
$$

**The equations with dirac16complex00 as the source** (classical commuting $\Phi$; $k_\mu$, $S$ and $U$ classical bilinears):

$$
\begin{aligned}
&\textstyle\sum_k\alpha_k E_{(k)}{}^{x_4}{}_{x_4} + \Lambda = -\kappa\,(k_4 - L_0), \qquad \sum_k\alpha_k E_{(k)}{}^{x_8}{}_{x_8} + \Lambda = \kappa\,(L_0 - k_8), \\
&a_4''\,F(a_4') = \kappa\,(k_5 - k_1), \qquad 2k_8 = k_1 + k_5, \qquad K^{(\mu}{}_{\nu)} = 0 \;\; (\mu \ne \nu),
\end{aligned}
$$

together with $k_1 = k_2 = k_3$, $k_5 = k_6 = k_7$ and the requirement that every component be independent of $x_8$. On shell $L_0 = S\,U'(S) - U(S)$. The evolution equation shows what drives $a_4''$: a difference between the kinetic terms along 3-space and along the extra times. This record contains no exact non-homogeneous dirac16complex00 configuration that satisfies all of these conditions with $k_1 \ne k_5$; whether one exists is open.

**The homogeneous condensate.** For $\Phi = \Phi(x_4)$ on shell the field equation is $\partial_4\Phi = A_\Phi\Phi$ with $A_\Phi = -\gamma^{(x_4)}\big(M - 3H\gamma^{(x_8)}\big)$ and $M = m + U'(S)$, free of $x_8$. Proved exactly (Wolfram, and in the sympy record both for an independently built Clifford representation and for the author's T16):

- $CA_\Phi + A_\Phi^TC = 0$, so $S = \bar\Phi\Phi$ is constant along $x_4$;
- the diagonal kinetic components are $K^{x_4}{}_{x_4} = MS$ and $0$ for every other direction, and $K^{x_4}{}_{x_8} = K^{x_8}{}_{x_4} = 0$; hence $\rho = mS + U(S)$, $p_3 = p_t = p_8 = S\,U'(S) - U(S)$ and $q_{48} = q_{84} = 0$, and the algebraic condition and the $x_8$-independence hold;
- the nonzero off-diagonal kinetic components are exactly multiples of the 15 three-gamma bilinears $B_{abc} = \bar\Phi\gamma^{(a)}\gamma^{(b)}\gamma^{(c)}\Phi$ with $\{a,b,c\} = \{i, x_4, x_8\}$ ($i = x_1..x_3, x_5..x_7$) and $\{i, j, x_4\}$ ($i = x_1..x_3$, $j = x_5..x_7$); there are 42 nonzero ordered pairs $(\mu, \nu)$.

The 42 components fall into ten groups; within each group the coefficient is the same for every 3-space index $x_i$ ($i = 1, 2, 3$) and extra-time index $x_t$ ($t = 5, 6, 7$), and on the patch $\sqrt[12]{\cot^2 z+1} = \sin^{-1/6}z$ (the gammas in this table are the frame gammas; generated from `Revision/field_equations_a4/a4-equations.json`):

| component | bilinear | coefficient |
| --- | --- | --- |
| $K^{x_i}{}_{x_4}$ | $\bar\Phi \gamma^{x_i} \gamma^{x_4} \gamma^{x_8} \Phi$ | $\frac{7}{4} e^{-a_4} \sqrt[12]{\cot^2 z+1}\, H$ |
| $K^{x_i}{}_{x_t}$ | $\bar\Phi \gamma^{x_i} \gamma^{x_4} \gamma^{x_t} \Phi$ | $-\frac{1}{2} e^{-2 a_4} (a_4')$ |
| $K^{x_i}{}_{x_8}$ | $\bar\Phi \gamma^{x_i} \gamma^{x_4} \gamma^{x_8} \Phi$ | $\frac{1}{4} e^{-a_4} (a_4') \cot z \sqrt[12]{\cot^2 z+1}$ |
| $K^{x_4}{}_{x_i}$ | $\bar\Phi \gamma^{x_i} \gamma^{x_4} \gamma^{x_8} \Phi$ | $-\frac{7 e^{a_4} H}{4 \sqrt[12]{\cot^2 z+1}}$ |
| $K^{x_4}{}_{x_t}$ | $\bar\Phi \gamma^{x_4} \gamma^{x_t} \gamma^{x_8} \Phi$ | $-\frac{7 e^{-a_4} H}{4 \sqrt[12]{\cot^2 z+1}}$ |
| $K^{x_t}{}_{x_i}$ | $\bar\Phi \gamma^{x_i} \gamma^{x_4} \gamma^{x_t} \Phi$ | $\frac{1}{2} e^{2 a_4} (a_4')$ |
| $K^{x_t}{}_{x_4}$ | $\bar\Phi \gamma^{x_4} \gamma^{x_t} \gamma^{x_8} \Phi$ | $-\frac{7}{4} e^{a_4} \sqrt[12]{\cot^2 z+1}\, H$ |
| $K^{x_t}{}_{x_8}$ | $\bar\Phi \gamma^{x_4} \gamma^{x_t} \gamma^{x_8} \Phi$ | $\frac{1}{4} e^{a_4} (a_4') \cot z \sqrt[12]{\cot^2 z+1}$ |
| $K^{x_8}{}_{x_i}$ | $\bar\Phi \gamma^{x_i} \gamma^{x_4} \gamma^{x_8} \Phi$ | $\frac{e^{a_4} (a_4')}{4 \cot z \sqrt[12]{\cot^2 z+1}}$ |
| $K^{x_8}{}_{x_t}$ | $\bar\Phi \gamma^{x_4} \gamma^{x_t} \gamma^{x_8} \Phi$ | $-\frac{e^{-a_4} (a_4')}{4 \cot z \sqrt[12]{\cot^2 z+1}}$ |

The off-diagonal field equations $0 = \kappa T^\mu{}_\nu$ therefore require $B_{i\,x_4 x_8} = 0$ for the six $i$ (coefficients proportional to $H$ and to $a_4'$) and, when $a_4' \ne 0$, $B_{i j x_4} = 0$ for the nine pairs $i, j$.

**Exact witnesses** that these conditions can be met with $S \ne 0$: $\Phi = e^{-i\omega x_4}\Phi_0$ with $\omega = \sqrt{M^2 - 9H^2}$ ($M^2 > 9H^2$), and $\Phi_0 = v_1 + c\,v_2$ built from the two eigenvectors of $A_\Phi$ in the sectors $\gamma^{(x_1)}\gamma^{(x_5)} = \gamma^{(x_2)}\gamma^{(x_6)} = \gamma^{(x_3)}\gamma^{(x_7)} = -1$ and $+1$, $c = \overline{v_1^\dagger C v_2}$. At $(M, H) = (5, 1)$, $(5, 4/3)$ and $(-5, 1)$ (exact Gaussian-rational arithmetic) the frequencies are $\omega = 4, 3, 4$, all 15 three-gamma bilinears and every off-diagonal kinetic component vanish for every $a_4$ and $a_4'$, and $S = 204800$, $115200$, $204800$ respectively.

**Theorem (the condensate allows only the linear member).** Hypotheses: $\Phi$ a homogeneous on-shell condensate as above (classical, commuting) satisfying the off-diagonal conditions; $a_4 \in C^2$; $(\alpha_1, \alpha_2, \alpha_3) \ne (0, 0, 0)$. Then $p_3 = p_t$, so $a_4''F(a_4') = 0$; $F$ is a nonzero polynomial in $a_4'$ with finitely many roots and $a_4'$ is continuous, so $a_4'' = 0$ on every interval:

$$
a_4 = A H x_4 + a_0 ,
$$

with real $A$: only the linear member is allowed (`theoremLinear` of `Revision/field_equations_a4/a4-equations.json`, resting on the checks listed below). The equations contain $A$ only through $A^2$ (invariant under $A \to -A$): the extra times deflate for $A > 0$, which is a choice of sign and is not selected by the equations; $A < 0$ is allowed on the same footing, and $A = 0$ is the static case.

**The source it requires.** With $a_4' = AH$ the remaining equations are the constraint and the $x_8$ equation, at $a_4' = AH$:

$$
\kappa\,\big(mS + U\big) = -\Big(\Lambda + \sum_k\alpha_k E_{(k)}{}^{x_4}{}_{x_4}\Big), \qquad \kappa\,\big(S\,U' - U\big) = \Lambda + \sum_k\alpha_k E_{(k)}{}^{x_8}{}_{x_8} ,
$$

that is, $\rho = mS + U$ and $p = SU' - U$ must equal the linear-member values of section 11. In Einstein gravity

$$
\kappa\,(mS + U) = -(3A^2 + 21)H^2 - \Lambda, \qquad \kappa\,(S\,U' - U) = (15 - 3A^2)H^2 + \Lambda ,
$$

and for $U = \tfrac{\lambda}{2}S^2$ and $m \ne 0$ these are equivalent to

$$
\kappa\, m S = -(36H^2 + 2\Lambda), \qquad 6(A^2 + 1)H^2 = -\kappa\, S\,(m + \lambda S),
$$

so $A^2 = -\kappa S(m + \lambda S)/(6H^2) - 1$, and a real $A$ needs $\kappa S(m + \lambda S) \le -6H^2$. For the condensate $m + \lambda S = M$ is the effective mass of the field equation and $S(m + \lambda S) = \rho + p$; the requirement is the null-energy statement of section 11 for this source. $S$ takes both signs (section 2), so the sign condition is not excluded by the algebra; the three exact witnesses above have $S > 0$ with $M = 5, 5, -5$. This record contains no check that combines a witness with the Einstein conditions (definite $\kappa$, $\Lambda$, $m$, $\lambda$ and $A$): that the deflating member is realised by a specific dirac16complex00 condensate is not established here.

| statement | Wolfram checks ($a_4$ record) | sympy checks ($a_4$ record) |
| --- | --- | --- |
| the Clifford facts used, in a second representation | `C_properties_own_rep`, `gamma_mu_anticommutes_with_Omega_mu_no_sum` | `ownrep_clifford`, `ownrep_C_properties`, `ownrep_anticommutator_no_sum`, `authorT16_clifford`, `authorT16_C_properties`, `authorT16_anticommutator_no_sum` |
| condensate equation free of $x_8$; $S$ constant; adjoint | `condensate_equation_x8_consistent`, `condensate_S_constant`, `condensate_adjoint_equation` | `ownrep_condensate_S_constant`, `ownrep_condensate_adjoint`, `authorT16_condensate_S_constant`, `authorT16_condensate_adjoint` |
| diagonal kinetic tensor of the condensate | `condensate_kinetic_tensor_diagonal` | `ownrep_condensate_kinetic_diagonal`, `authorT16_condensate_kinetic_diagonal` |
| off-diagonal components: the 15 three-gamma bilinears, coefficients | `condensate_offdiagonal_are_three_gamma_bilinears` | `ownrep_condensate_offdiagonal_three_gamma`, `authorT16_condensate_offdiagonal_three_gamma`, `json_offdiagonal_coefficients`, `offdiagonal_coefficients_representation_independent` |
| exact witnesses | `condensate_diagonal_witness_exact` | `ownrep_condensate_witness`, `authorT16_condensate_witness` |
| the linear member is the only one ($F \ne 0$) | `evolution_F_not_identically_zero`, `linear_member_equal_pressures` | `evolution_F_not_identically_zero`, `linear_member_equal_pressures` |
| Einstein conditions with $U = \tfrac{\lambda}{2}S^2$ | `condensate_einstein_quadratic_U` | `condensate_einstein_quadratic_U` |

## 13. Pairing theorems for dirac16complex00 (summary)

The pairing of universes of masses $\{+m, -m\}$ is the subject of `Revision/docs/PAIR_CREATION_PROOFS`; for the commuting field the Revision pairing records prove exactly the following.

**T1 (chirality pairing).** Hypotheses: any gravitational field, fixed and the same for both members (a test field; the metric is not varied); $\Gamma = \mathrm{diag}(-I_8, I_8)$; $U = \tfrac{\lambda}{2}S^2$, or any function $U$ with $U \to -U$. Then, identically,

$$
\mathcal{L}_{m,\lambda}[\Gamma\Phi] = -\mathcal{L}_{-m,-\lambda}[\Phi], \qquad S[\Gamma\Phi] = S[\Phi], \qquad T^{(-m,-\lambda)}[\Gamma\Phi] = -T^{(m,\lambda)}[\Phi], \qquad J[\Gamma\Phi] = -J[\Phi]
$$

(for a general $U$: $\mathcal{L}_{m,U}[\Gamma\Phi] = -\mathcal{L}_{-m,-U}[\Phi]$), and $\Phi$ solves the $(m, \lambda)$ equations if and only if $\Gamma\Phi$ solves the $(-m, -\lambda)$ ones. The pair's total energy-momentum density, current and charge vanish as classical c-number bilinears.

**T2 (mirror pairing).** With the isometry $\phi: x_8 \to \pi/(6H) - x_8$ ($z \to \pi - z$, the $Z_2$ mirror across $z = \pi/2$, an ASSUMED construction at a degenerate surface of the metric) and $\Phi'(\phi(x)) = \gamma^{(x_8)}\Phi(x)$:

$$
\mathcal{L}_{m,\lambda}[\Phi'](\phi(x)) = \mathcal{L}_{-m,\lambda}[\Phi](x), \qquad S' = -S ,
$$

and the mirror partner carries the same energy density and charge (the tensor transformed by the reflection), not the opposite.

There is no quantum reading for dirac16complex00: it is not quantised. These theorems map solutions to solutions; they derive no creation process, rate or amplitude (the lists of what is not established in the pairing records).

| statement | Wolfram checks (pairing) | sympy checks (pairing) |
| --- | --- | --- |
| T1 for the commuting field in the primordial metric | `Gamma_properties`, `T1_kernel_field_equation`, `T1_linearity_argument`, `T1_Lagrangian_primordial_commuting`, `T1_Lagrangian_negative_controls_primordial_commuting`, `T1_field_equation_covariance_primordial_commuting`, `T1_Euler_Lagrange_map_primordial_commuting`, `T1_energy_momentum_primordial_commuting`, `T1_current_primordial_commuting`, `T1_general_potential_primordial_commuting` | `T1.metric.commuting.lagrangian`, `T1.metric.commuting.negative_controls`, `T1.metric.commuting.euler_lagrange_map`, `T1.metric.commuting.emt`, `T1.metric.commuting.pair_total_emt_zero`, `T1.metric.commuting.current`, `T1.metric.commuting.general_potential` |
| T2 for the commuting field | `T2_mirror_is_isometry`, `T2_mirror_Lagrangian_commuting`, `T2_mirror_energy_momentum_and_current_commuting`, `T2_mirror_Euler_Lagrange_commuting` | `T2.metric.commuting.euler_lagrange_map`, `T2.metric.commuting.emt`, `T2.metric.commuting.current`, `T2.metric.commuting.S_odd` |

## 14. Check index

Every check below has the verdict PASS in the named report (the publication test re-reads the reports and confirms each name and verdict). Counts at the time of writing: wolfram-algebra 45 checks, python-algebra 35, wolfram-field-theory 84, python-field-theory 70, wolfram-a4-report 47, python-a4-report 61, wolfram-pairing 101, python-pairing 66, wolfram-scope 15, python-scope 14; all pass.

| report | checks cited in this document |
| --- | --- |
| `Revision/algebra/reports/wolfram-algebra.json` | `Clifford_relation`, `reality`, `symmetry_pattern`, `eta_in_author_order`, `coordinate_map`, `C_real_symmetric` |
| `Revision/algebra/reports/wolfram-algebra.json` | `C_squared_identity`, `C_gamma_real_antisymmetric`, `Gamma_diag`, `B_Hermitian`, `B_squared_identity`, `B_signature_8_8` |
| `Revision/algebra/reports/wolfram-algebra.json` | `S_Lorentz_algebra`, `S_preserves_C`, `S_commutes_with_Gamma`, `Pin44_irreducible_commutant_dim_1`, `Spin44_commutant_dim_2_chiral_projectors`, `chiral_halves_irreducible` |
| `Revision/algebra/reports/wolfram-algebra.json` | `chiral_halves_inequivalent_intertwiners_0`, `Spin_Pin_reflection_swaps_halves` |
| `Revision/algebra/reports/python-algebra.json` | `clifford_relation`, `clifford_relation_sympy`, `reality_signed_permutations`, `symmetry_pattern`, `C_equals_notebook_sigma16`, `C_real_symmetric_involution` |
| `Revision/algebra/reports/python-algebra.json` | `C_gamma_antisymmetric`, `chirality_diag`, `chirality_anticommutes`, `B_hermitian_involution_signature`, `S_lorentz_algebra`, `S_preserves_C_and_commutes_with_Gamma` |
| `Revision/algebra/reports/python-algebra.json` | `clifford_products_span_M16`, `pin_commutant_dimension_1`, `even_products_span_M8_plus_M8`, `spin_commutant_dimension_2`, `spin_halves_irreducible`, `spin_halves_inequivalent` |
| `Revision/algebra/reports/python-algebra.json` | `reflections_exchange_halves`, `fixture_comparison_gammas_json` |
| `Revision/theory/reports/wolfram-field-theory.json` | `metric_is_the_authors`, `vielbein_inverse`, `sqrt_det_g_is_cos_z`, `degenerate_at_H_0`, `christoffel_count`, `ricci_scalar` |
| `Revision/theory/reports/wolfram-field-theory.json` | `ricci_mixed_components`, `never_flat_for_H_positive`, `vielbein_postulate`, `omega_antisymmetric`, `omega_components`, `Omega_components` |
| `Revision/theory/reports/wolfram-field-theory.json` | `gamma_covariantly_constant`, `spin_curvature_equals_Riemann`, `gammaOmega_equals_3H_gamma_x8`, `gammaOmega_x4_terms_cancel`, `gammaOmega_divergence_form`, `L_real_C` |
| `Revision/theory/reports/wolfram-field-theory.json` | `L_total_divergence_to_unsymmetrised_C`, `L_spin_connection_drops_out_C`, `EL_Psibar_C`, `EL_Psi_C`, `adjoint_equation_is_Dirac_conjugate_C`, `Dirac_operator_explicit_C` |
| `Revision/theory/reports/wolfram-field-theory.json` | `block_form`, `evolution_form_C`, `nontriviality_2_dirac16complex00`, `Omega_vanishes_iff_a4prime_and_H_vanish`, `current_real_C`, `current_conservation_identity_C` |
| `Revision/theory/reports/wolfram-field-theory.json` | `charge_density_is_Krein_form_C`, `Lichnerowicz_identity_C`, `Majorana_Lg_total_derivative_grassmann`, `Majorana_Lg_commuting_control`, `T_vielbein_variation_closed_form_C`, `T_symmetric_part_Belinfante_C` |
| `Revision/theory/reports/wolfram-field-theory.json` | `Noether_identity_diffeomorphisms_C`, `Noether_identity_local_Lorentz_C`, `conservation_on_shell_general`, `T_diagonal_components_C`, `EMT_trace_C`, `kinetic_sum_on_shell_C` |
| `Revision/theory/reports/wolfram-field-theory.json` | `T_x4_x8_component_C`, `energy_exchange_equation`, `solution_matrix_square`, `exact_solution_x4_x8_C`, `exact_solution_nonlinear_homogeneous_C`, `good_sector_hermiticity_curved` |
| `Revision/theory/reports/python-field-theory.json` | `gammas_json_equals_python_construction`, `metric_from_vielbein_equals_SPEC`, `sqrt_det_g_equals_cos_z`, `christoffel_symmetric_metric_compatible`, `spin_connection_antisymmetric`, `vielbein_postulate` |
| `Revision/theory/reports/python-field-theory.json` | `Omega_x4_and_Omega_x8_vanish`, `covariant_constancy_D_mu_gamma_nu`, `gamma_mu_Omega_mu_equals_3H_gamma_x8`, `time_terms_cancel_hidden_term_survives`, `anticommutator_gamma_Omega_vanishes`, `divergence_of_sqrtg_gamma` |
| `Revision/theory/reports/python-field-theory.json` | `nontriviality_Omega_zero_iff_flat`, `curvature_nonzero_flat_only_formally`, `spinor_curvature_equals_riemann`, `lichnerowicz_contraction`, `lichnerowicz_identity_on_fields`, `commuting_lagrangian_real` |
| `Revision/theory/reports/python-field-theory.json` | `commuting_controls_not_vacuous`, `commuting_total_divergence_relation`, `commuting_euler_lagrange_psibar_variation`, `commuting_euler_lagrange_psi_variation`, `commuting_adjoint_equation_is_conjugate`, `commuting_current_conservation` |
| `Revision/theory/reports/python-field-theory.json` | `commuting_emt_symmetric`, `commuting_emt_conservation_on_shell`, `commuting_emt_conservation_negative_control`, `commuting_trace_on_shell`, `commuting_homogeneous_on_shell_rho_p`, `commuting_T_x4x8_homogeneous` |
| `Revision/theory/reports/python-field-theory.json` | `commuting_emt_equals_general_vielbein_variation_on_shell`, `commuting_emt_equals_vielbein_variation_diagonal`, `negative_control_majorana_grassmann_total_derivative`, `negative_control_majorana_commuting_contrast`, `energy_exchange_equation`, `exact_solution_family_x4_x8` |
| `Revision/theory/reports/python-field-theory.json` | `exact_nonlinear_homogeneous_solution` |
| `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `metric_is_SPEC_section_1`, `sqrt_abs_det_g_is_cos_z`, `mixed_riemann_free_of_warp_and_a4`, `P1_direct_equals_minus_4_Einstein`, `P1_direct_equals_gkd_branch_monomials`, `P2_direct_equals_gkd_branch_monomials` |
| `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `P3_direct_equals_gkd_branch_monomials`, `P1_trace_identity`, `P2_trace_identity`, `P3_trace_identity`, `P4_vanishes_pigeonhole`, `E1_divergence_free` |
| `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `E2_divergence_free`, `E3_divergence_free`, `independent_components`, `evolution_factorises_a4pp_times_F`, `evolution_F_not_identically_zero`, `algebraic_identity_x1_plus_x5_minus_2x8` |
| `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `x8_component_contains_no_a4pp`, `constraint_propagation_bianchi`, `conservation_components`, `einstein_components`, `einstein_null_energy_x8`, `einstein_no_vacuum_solution` |
| `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `linear_member_equal_pressures`, `linear_member_vacuum_factor`, `C_properties_own_rep`, `gamma_mu_anticommutes_with_Omega_mu_no_sum`, `gravity_term_gamma_mu_Omega_mu`, `condensate_equation_x8_consistent` |
| `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `condensate_S_constant`, `condensate_adjoint_equation`, `condensate_kinetic_tensor_diagonal`, `condensate_offdiagonal_are_three_gamma_bilinears`, `condensate_einstein_quadratic_U`, `condensate_diagonal_witness_exact` |
| `Revision/field_equations_a4/reports/python-a4-report.json` | `mixed_riemann_free_of_warp_and_a4`, `riemann_entries_laurent`, `P1_equals_minus_4_Einstein`, `P1_equals_gkd_branch_monomials`, `P2_equals_gkd_branch_monomials`, `P3_equals_gkd_branch_monomials` |
| `Revision/field_equations_a4/reports/python-a4-report.json` | `E1_divergence_free`, `E2_divergence_free`, `E3_divergence_free`, `evolution_factorises`, `evolution_F_not_identically_zero`, `algebraic_identity` |
| `Revision/field_equations_a4/reports/python-a4-report.json` | `constraint_and_x8_first_order`, `bianchi_x4`, `other_components_vanish`, `conservation_components`, `einstein_components`, `einstein_null_energy_x8` |
| `Revision/field_equations_a4/reports/python-a4-report.json` | `einstein_no_vacuum`, `linear_member_equal_pressures`, `linear_member_vacuum_factor`, `condensate_einstein_quadratic_U`, `json_lovelock_components`, `json_general_source_equations` |
| `Revision/field_equations_a4/reports/python-a4-report.json` | `json_einstein`, `json_linear_member`, `ownrep_clifford`, `ownrep_C_properties`, `ownrep_anticommutator_no_sum`, `ownrep_gravity_term` |
| `Revision/field_equations_a4/reports/python-a4-report.json` | `ownrep_condensate_S_constant`, `ownrep_condensate_adjoint`, `ownrep_condensate_kinetic_diagonal`, `ownrep_condensate_offdiagonal_three_gamma`, `ownrep_condensate_witness`, `authorT16_clifford` |
| `Revision/field_equations_a4/reports/python-a4-report.json` | `authorT16_C_properties`, `authorT16_anticommutator_no_sum`, `authorT16_gravity_term`, `authorT16_condensate_S_constant`, `authorT16_condensate_adjoint`, `authorT16_condensate_kinetic_diagonal` |
| `Revision/field_equations_a4/reports/python-a4-report.json` | `authorT16_condensate_offdiagonal_three_gamma`, `authorT16_condensate_witness`, `json_offdiagonal_coefficients`, `offdiagonal_coefficients_representation_independent` |
| `Revision/pairing/reports/wolfram-pairing.json` | `Gamma_properties`, `T1_kernel_field_equation`, `T1_linearity_argument`, `T1_Lagrangian_primordial_commuting`, `T1_Lagrangian_negative_controls_primordial_commuting`, `T1_field_equation_covariance_primordial_commuting` |
| `Revision/pairing/reports/wolfram-pairing.json` | `T1_Euler_Lagrange_map_primordial_commuting`, `T1_energy_momentum_primordial_commuting`, `T1_current_primordial_commuting`, `T1_general_potential_primordial_commuting`, `T2_mirror_is_isometry`, `T2_mirror_Lagrangian_commuting` |
| `Revision/pairing/reports/wolfram-pairing.json` | `T2_mirror_energy_momentum_and_current_commuting`, `T2_mirror_Euler_Lagrange_commuting` |
| `Revision/pairing/reports/python-pairing.json` | `T1.metric.commuting.lagrangian`, `T1.metric.commuting.negative_controls`, `T1.metric.commuting.euler_lagrange_map`, `T1.metric.commuting.emt`, `T1.metric.commuting.pair_total_emt_zero`, `T1.metric.commuting.current` |
| `Revision/pairing/reports/python-pairing.json` | `T1.metric.commuting.general_potential`, `T2.metric.commuting.euler_lagrange_map`, `T2.metric.commuting.emt`, `T2.metric.commuting.current`, `T2.metric.commuting.S_odd`, `Q.one_particle_Krein_inertia_proof` |
| `Revision/pairing/reports/wolfram-pairing.json` | `Q_one_particle_Krein_inertia_real_frequencies` |
| `Revision/theory/reports/wolfram-scope.json` | `boosted_frame_reproduces_metric`, `boosted_frame_canonical_connection`, `boosted_frame_gammaOmega_formula`, `boosted_frame_gammaOmega_vanishes`, `boosted_frame_curvature_nonzero`, `rescaling_removes_the_connection_term` |
| `Revision/theory/reports/wolfram-scope.json` | `rescaled_equation_quadratic_potential`, `gammaOmega_blind_to_the_deflation`, `connection_free_lagrangian_same_equations`, `spin_connection_in_the_energy_momentum_tensor`, `good_sector_hermiticity_up_to_the_brane_flux` |
| `Revision/theory/reports/wolfram-scope.json` | `good_sector_x8_independent_modes_without_boundary_condition`, `extra_time_growth_rates_unbounded`, `commuting_field_energy_unbounded_below` |
| `Revision/theory/reports/python-scope.json` | `boosted_frame_reproduces_metric`, `boosted_frame_canonical_connection`, `boosted_frame_gammaOmega_formula`, `boosted_frame_gammaOmega_vanishes`, `boosted_frame_curvature_nonzero`, `rescaling_removes_the_connection_term` |
| `Revision/theory/reports/python-scope.json` | `rescaled_equation_quadratic_potential`, `gammaOmega_blind_to_the_deflation`, `connection_free_lagrangian_same_equations`, `spin_connection_in_the_energy_momentum_tensor`, `good_sector_hermiticity_up_to_the_brane_flux` |
| `Revision/theory/reports/python-scope.json` | `good_sector_x8_independent_modes_without_boundary_condition`, `extra_time_growth_rates_unbounded`, `commuting_field_energy_unbounded_below` |

## 15. What is not claimed

- **No quantisation.** dirac16complex00 is not quantised; its energy-momentum tensor is a classical bilinear. The operator statements (Krein space, Fock space, normal ordering) belong to dirac16complex.
- **The energy is not bounded below, the charge is indefinite.** The record decides the energy question negatively: already for $U = 0$ in the good sector there are positive-frequency solutions of negative energy, and the energy density $-5|c|^2$ of the example of section 9 is unbounded below as $|c|$ grows; the conserved charge $\int\cos z\,\Phi^\dagger B\Phi$ is indefinite. The descriptions "semi-classical" and "analogue of Dirac's 1928 wave function" are interpretations: that wave function has a positive conserved density, this field does not.
- **Frame dependence of the gravitational term.** $\gamma^\mu\Omega_\mu = 3H\gamma^{(x_8)}$ is the value for the diagonal vielbein and the variables $\Phi$; it vanishes in the boosted frame of section 6 and is removed by the rescaling $\Phi = \sin^{-1/2}z\,\chi$. Only $\Omega_\mu$ itself (curvature) and the frame factors are frame-independent; non-triviality [2] is claimed in this exact sense.
- **No 3-space observer equation of state, no CPL fit, no comparison with supernova data.** Section 10 gives the ratios $p/\rho$ of the 8-dimensional tensor only; Hypothesis00 (a time-varying dark-energy or dark-matter equation of state from dirac16complex00) is investigated in the separate dark-sector record, not here. For the homogeneous condensate the ratio $w$ is constant in $x_4$.
- **No general solution, no well-posed Cauchy problem.** The exact solutions of section 5 are test points; the field equation is not solved in general, and no existence statement for the nonlinear Cauchy problem is made beyond the first-order evolution form. For data that depend on the extra times the problem is ill-posed in Hadamard's sense (section 7), and the good sector needs a boundary condition at $z = \pi/2$, which this record does not impose.
- **No realisation of the deflating member by a specific condensate.** The theorem of section 12 shows that a homogeneous condensate allows only $a_4 = AHx_4 + a_0$ and gives the conditions the source must satisfy; the sign of $A$ (deflation for $A > 0$) is not selected by the equations; it is not shown that a specific dirac16complex00 condensate meets those conditions with definite $\kappa$, $\Lambda$, $m$, $\lambda$ and $A > 0$, and no non-homogeneous source with $k_1 \ne k_5$ (which would drive $a_4''$) is constructed.
- **The $x_8$ dependence.** The metric of section 1 is an exact solution only with an $x_8$-independent, isotropic source with vanishing off-diagonal components; a dirac16complex00 configuration that depends on $x_8$ is not a consistent source for this metric.
- **The brane.** The patch end $z = \pi/2$ is a degenerate surface of the metric ($g_{88} = 0$, $\sqrt{|g|} = 0$) at finite proper distance; no junction condition is derived, the mirror construction used by T2 is an assumption, and the boundary term $\sin z\,u^\dagger M_8 v$ of the hidden direction does not vanish there.
- **Pairing.** The pairing theorems of section 13 derive no creation process, rate or amplitude for universes of masses $\{+m, -m\}$; they are correspondences between solutions, in a fixed gravitational field.
- **Notebook conventions.** The canonical spin connection used here is the one with $\omega_{\mu ab} = \eta_{ac}\omega_\mu{}^c{}_b$; the notebook's contraction of the mixed components (which lacks a metric factor) is not used, and its Majorana-type $L_g$ serves only as the negative control of section 4.

## 16. Reproduction

From the repository root, in this order (each verifier writes its report and exits with code 0 only if every check passes; two runs give byte-identical outputs):

```text
wolframscript -file Revision/algebra/wolfram/verify_algebra.wls
python Revision/algebra/python/check_algebra.py
wolframscript -file Revision/theory/wolfram/verify_field_theory.wls
python Revision/theory/python/check_field_theory.py
wolframscript -file Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls
python Revision/field_equations_a4/python/check_field_equations_a4.py
wolframscript -file Revision/pairing/wolfram/verify_pairing.wls
python Revision/pairing/python/check_pairing.py
wolframscript -file Revision/theory/wolfram/verify_scope.wls
python Revision/theory/python/check_scope.py
```

**Re-run for this document (2026-10-01).** The eight verifiers of the first edition were run in this order on a scratch copy of the Revision inputs. Run times on the development machine: algebra 4 s (Wolfram) and 2 s (sympy); theory 1029 s (Wolfram) and 115 s (sympy); $a_4$ equations 15 s and 4 s; pairing 82 s and 147 s. After the review of 2026-10-01 the sympy theory checker, the pairing verifiers, the $a_4$ verifiers and the new scope verifiers were run again on the working tree: every check passes, and the outputs of two runs are byte-identical. The comparison section `comparison_with_wolfram` of `Revision/theory/reports/python-field-theory.json` was regenerated against the current Wolfram record (84 checks): 32 of 32 formula records and 63 of 63 check pairs agree; its parser now reads the prose form of `energy_exchange` in the current `Revision/theory/field-theory.json`, and the five prose records that it did not compare before are compared by re-deriving their formulas. The sympy theory checker now exits with an error when the comparison disagrees (103 s for the regenerated report; the scope verifiers 17 s and 1 s). The reports cited here are the files of the working tree.

The document is built and checked with (the first command on one line)

```text
python scripts/build_provenance_pdf.py Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md
       --developer-layout --specifications Revision/pdf-specifications.json
python -m unittest Revision/tests/test_dirac16complex00_field_theory_publication.py -v
```

The builder makes the .tex twice and the PDF in two fresh directories, requires byte identity and a warning-free LaTeX log, and verifies the PDF against its entry in Revision's own registry `Revision/pdf-specifications.json`. The publication test checks that the .tex is the builder's output for this .md, that the PDF is registered with its page count and sha256, that the formula blocks of sections 5, 11 and 12 are the ones generated from `Revision/theory/field-theory.json` and `Revision/field_equations_a4/a4-equations.json`, and that every check cited in section 14 exists in its report with a passing verdict.
