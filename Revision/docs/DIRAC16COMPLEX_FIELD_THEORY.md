# dirac16complex in the author's primordial gravitational field

## Lagrangian, covariant field equations, non-triviality [1], energy-momentum tensor operator, equations of state and the field equations for a4[x4] (Revision record)

## Abstract

This document records, for the fermion field dirac16complex coupled to the author's primordial gravitational field, the Lagrangian, its coupling through the canonical spin connection, the exact covariant field equations (Euler-Lagrange) written out component by component, the non-triviality test [1] with its proof, the self-consistency of the field equations, the energy-momentum tensor (as a Grassmann-algebra expression and as a normal-ordered operator after canonical quantisation in 4 + 4 dimensions, with the Krein structure that this quantisation forces), the kinetic and potential energy, the energy density, the pressures and the equations of state, and the Einstein-Lovelock field equations for a4[x4] with dirac16complex as the source. Every formula is an output of Revision code (a WolframScript verifier and, for most statements, an independent sympy verifier) and is listed with the names of the checks that verify it. The main exact results are: in the diagonal vielbein the spin-connection term of the field equation is $\gamma^\mu\Omega_\mu = 3H\gamma^{(8)}$ for every $a_4$ (the time-direction terms of the three inflating and the three deflating directions cancel, the hidden-direction terms add); this value belongs to the diagonal frame and to the field variables $\Psi$ (it vanishes identically in a frame boosted in the $(x_4, x_8)$ plane, and the rescaling $\Psi = \sin^{-1/2}z\,\chi$ removes it), while the frame-independent content of non-triviality [1] is that $\Omega_\mu$ vanishes in no frame (the metric is never flat for $H > 0$) and that the vielbein factors enter every derivative term; when $\Psi^\dagger$ is realised as the Hilbert adjoint, the canonical anticommutator $\{\Psi, \Psi^\dagger\} = B\,\delta^7/\sqrt{|g|}$ with $B$ of signature (8,8) forces an indefinite (Krein) inner product (in the good sector a positive Fock realisation with $\Psi^\dagger = \chi B$ exists); homogeneous on-shell configurations have $\rho = mS + U$ and $p = SU' - U$ in every direction; the field equations for $a_4$ reduce to a constraint, an evolution equation $a_4''F(a_4') = \kappa(p_3 - p_t)$, a hidden-direction equation and the condition $p_3 + p_t = 2p_8$. Section 15 states what is not claimed, including the frame dependence of $3H\gamma^{(8)}$, the boundary terms at the patch end $z = \pi/2$ and the ill-posedness of the Cauchy problem for data that depend on the extra times.

## 1. Scope, sources and status of the record

The binding plan is `Revision/SPEC.md`; the author's task is quoted in `Revision/README.md`. This document belongs to the new record under `Revision/` and uses nothing from the earlier stages of the repository: every statement below is an output of Revision code and is cited by the name of the check that verifies it. Numbers and formulas are taken only from the following files (verdicts as recorded in them when this document was written):

| part | files | checks |
| --- | --- | --- |
| algebra (SPEC section 2) | `Revision/algebra/reports/wolfram-algebra.json`, `Revision/algebra/reports/python-algebra.json` | Wolfram: 45 of 45 checks pass; sympy: 35 of 35 checks pass |
| field theory (SPEC sections 3, 4, 6) | `Revision/theory/field-theory.json`, `Revision/theory/reports/wolfram-field-theory.json`, `Revision/theory/reports/python-field-theory.json` | Wolfram: 84 of 84 checks pass; sympy: 70 of 70 checks pass |
| field equations for a4 (SPEC section 5) | `Revision/field_equations_a4/a4-equations.json`, `Revision/field_equations_a4/reports/wolfram-a4-report.json`, `Revision/field_equations_a4/reports/python-a4-report.json` | Wolfram: 47 of 47 checks pass; sympy: 61 of 61 checks pass |
| pairing (SPEC section 9) | `Revision/pairing/pairing-theory.json`, `Revision/pairing/reports/wolfram-pairing.json`, `Revision/pairing/reports/python-pairing.json` | Wolfram: 101 of 101 checks pass; sympy: 66 of 66 checks pass |
| scope of the statements (frame dependence, boundary terms, growth, sign of the energy) | `Revision/theory/reports/wolfram-scope.json`, `Revision/theory/reports/python-scope.json` | Wolfram: 15 of 15 checks pass; sympy: 14 of 14 checks pass |
| Kohn-Sham pairing T3 (SPEC section 9) | `Revision/pairing/kohn_sham/t3-theory.json`, `Revision/pairing/kohn_sham/reports/wolfram-t3.json`, `Revision/pairing/kohn_sham/reports/python-t3.json` | Wolfram: 10 of 10 checks pass; sympy: 13 of 13 checks pass |
| the Kohn-Sham states as a source of the $a_4$ equations | `Revision/field_equations_a4/reports/ks-source-conditions.json` | Python: 5 of 5 checks pass |

Each part has two verifiers that share no code: a WolframScript verifier (exact symbolic arithmetic) and a sympy verifier (an independent re-derivation; the gamma matrices are rebuilt from the author's formulas on both sides and compared entry by entry). Where only one engine verifies a statement, only that engine's check is cited. A check is cited in typewriter type, for example `nontriviality_1_dirac16complex` (Wolfram) or `gamma_mu_Omega_mu_equals_3H_gamma_x8` (sympy); in the field-theory reports the Wolfram names end in `_G` for dirac16complex (explicit Grassmann algebra) and the sympy names begin with `grassmann_`. The proofs are exact identities in the stated generality (symbolic $H$, $a_4(x_4)$, $m$, $\lambda$, and a general field configuration on its jet space); exact numerical examples are labelled as examples.

**Status of the comparison record of the field-theory branch.** The sympy report contains a comparison with the current Wolfram side (`comparison_with_wolfram`): 32 of 32 formula records and 63 of 63 check pairs agree, against a Wolfram run of 84 checks. Every formula record of `Revision/theory/field-theory.json` is compared (the record `energy_exchange`, three Wolfram expressions, component by component against the divergence recomputed from the sympy Christoffel symbols; the prose records `nontriviality`, `majorana_negative_control`, `exact_solutions`, `equation_of_state_definitions` and `hidden_direction_hermiticity` by re-deriving their formulas in sympy), and every Wolfram check is paired with a sympy check except `exact_solution_nonlinear_homogeneous_G` (the Grassmann form of the nonlinear homogeneous solution; its commuting form is paired). The sympy verifier exits with an error unless the comparison agrees entirely, so a stale comparison cannot pass unnoticed. This document still cites each formula by the checks of each engine separately.

Conventions (SPEC sections 1 and 2): coordinates $x_1, \dots, x_8$ as the author names them; $x_1, x_2, x_3$ are ordinary 3-space, $x_4$ is the time, $x_5, x_6, x_7$ are the three extra times (time-like, deflating exponentially as $a_4$ increases), $x_8$ is the hidden space direction; $z = 6Hx_8 \in (0, \pi/2)$, $H > 0$; $a_4 = a_4(x_4)$, $a_4' = da_4/dx_4$; $\partial_a = \partial/\partial x_a$. Frame indices are aligned with the coordinates and written in parentheses: $\gamma^{(a)}$ is the frame gamma matrix of direction $x_a$. Throughout, $i \in \{1, 2, 3\}$ labels the 3-space directions and $t \in \{5, 6, 7\}$ the extra times.

## 2. The primordial gravitational field

The author's metric (SPEC section 1), with signature (4,4) (space-like $x_1, x_2, x_3, x_8$; time-like $x_4, \dots, x_7$):

$$
\begin{aligned}
ds^2 &= e^{2a_4}\sin^{1/3}z\,(dx_1^2 + dx_2^2 + dx_3^2) - dx_4^2 \\
&\quad - e^{-2a_4}\sin^{1/3}z\,(dx_5^2 + dx_6^2 + dx_7^2) + \cot^2 z\,dx_8^2, \qquad z = 6Hx_8 \in (0, \pi/2).
\end{aligned}
$$

The scale factor of 3-space is $e^{a_4}\sin^{1/6}z$ (inflating as $a_4$ increases), that of the extra times $e^{-a_4}\sin^{1/6}z$ (exponentially deflating). The diagonal vielbein $e^a{}_\mu = f_a\,\delta^a_\mu$ with frame metric $\eta_{ab} = \mathrm{diag}(+1, +1, +1, -1, -1, -1, -1, +1)$ has

$$
f_1 = f_2 = f_3 = e^{a_4}\sin^{1/6}z,\quad f_4 = 1,\quad f_5 = f_6 = f_7 = e^{-a_4}\sin^{1/6}z,\quad f_8 = \cot z
$$

and reproduces the metric entry by entry (`metric_is_the_authors`, `vielbein_inverse`; sympy `metric_from_vielbein_equals_SPEC`). The volume element is

$$
\sqrt{|g|} = f_1 f_2\cdots f_8 = \sin z\cot z = \cos z,
$$

independent of $x_4$: the inflation $e^{3a_4}$ of 3-space and the deflation $e^{-3a_4}$ of the extra times compensate (`sqrt_det_g_is_cos_z`, `sqrt_det_g_equals_cos_z`). $H = 0$ is not a member of the family but a degenerate limit ($g_{11} \to 0$, $g_{88} \to \infty$ at fixed $x_8$; `degenerate_at_H_0`); every statement below assumes $H > 0$ and $0 < z < \pi/2$.

The Levi-Civita connection has 25 independent nonzero symbols (`christoffel_count`, `christoffel_symmetric_metric_compatible`; formula key `christoffel_nonzero`):

$$
\begin{aligned}
\Gamma^{x_i}{}_{x_i x_4} &= a_4', & \Gamma^{x_i}{}_{x_i x_8} &= H\cot z, \\
\Gamma^{x_t}{}_{x_4 x_t} &= -a_4', & \Gamma^{x_t}{}_{x_t x_8} &= H\cot z, \\
\Gamma^{x_4}{}_{x_i x_i} &= e^{2a_4}\sin^{1/3}z\,a_4', & \Gamma^{x_4}{}_{x_t x_t} &= e^{-2a_4}\sin^{1/3}z\,a_4', \\
\Gamma^{x_8}{}_{x_i x_i} &= -e^{2a_4}H\,\frac{\sin^{4/3}z}{\cos z}, & \Gamma^{x_8}{}_{x_t x_t} &= e^{-2a_4}H\,\frac{\sin^{4/3}z}{\cos z}, \\
\Gamma^{x_8}{}_{x_8 x_8} &= -\frac{6H}{\sin z\cos z}.
\end{aligned}
$$

The mixed Ricci tensor is diagonal (`ricci_mixed_components`, `ricci_scalar`, `curvature_nonzero_flat_only_formally`):

$$
R^{x_i}{}_{x_i} = a_4'' - 6H^2,\quad R^{x_4}{}_{x_4} = 6(a_4')^2,\quad R^{x_t}{}_{x_t} = -a_4'' - 6H^2,\quad R^{x_8}{}_{x_8} = -6H^2,
$$

$$
R = 6\big((a_4')^2 - 7H^2\big).
$$

Since $R^{x_8}{}_{x_8} = -6H^2 < 0$ for every $H > 0$ and every function $a_4$ (a constant $a_4$ included), the metric is never flat for $H > 0$ (`never_flat_for_H_positive`).

## 3. The field dirac16complex: Clifford algebra, Pin(4,4) and Spin(4,4)

dirac16complex is a field $\Psi$ with 16 complex anticommuting components $\Psi_A(x)$, $A = 1, \dots, 16$ (elements of a Grassmann algebra; after quantisation, operators with canonical anticommutators, section 11). It transforms under a 16-dimensional irreducible representation of Pin(4,4), the double cover of O(4,4); for the transformations of determinant 1 it transforms under the direct sum of two inequivalent irreducible 8-dimensional representations of Spin(4,4), the double cover of SO(4,4). These representation facts are proved exactly below for the author's gamma matrices.

The gamma matrices are the author's real $16\times16$ matrices T16, rebuilt by Revision code from the author's formulas (the tau matrices of the notebook) in WolframScript and, independently, in Python, with the notebook's frame order mapped to the author's coordinates (SPEC section 2): $\gamma^{(8)} = $ T16[0], $\gamma^{(1,2,3)} = $ T16[1..3], $\gamma^{(4)} = $ T16[4], $\gamma^{(5,6,7)} = $ T16[5..7] (`T16_block_form`, `coordinate_map`; the two constructions agree entry by entry, `fixture_comparison_gammas_json`). Exact properties:

- Clifford relation $\{\gamma^{(a)}, \gamma^{(b)}\} = 2\eta^{ab}\,I_{16}$ for all 64 pairs; the squares are $+1$ for $x_1, x_2, x_3, x_8$ and $-1$ for $x_4, \dots, x_7$ (`Clifford_relation`, `clifford_relation`, `clifford_relation_sympy`). Every $\gamma^{(a)}$ is a real signed permutation matrix, symmetric for the space-like and antisymmetric for the time-like directions, $(\gamma^{(a)})^T = \eta_{aa}\gamma^{(a)}$ (`reality`, `signed_permutation_matrices`, `symmetry_pattern`).
- $C = \gamma^{(8)}\gamma^{(1)}\gamma^{(2)}\gamma^{(3)}$ (the notebook's sigma16) is real symmetric with $C^2 = 1$, and every $C\gamma^{(a)}$ is real antisymmetric, equivalently $C\gamma^{(a)}C^{-1} = -(\gamma^{(a)})^T$ (`C_real_symmetric`, `C_squared_identity`, `C_gamma_real_antisymmetric`; sympy `C_conjugation`). The Dirac adjoint is $\bar\Psi = \Psi^\dagger C$ and $S = \bar\Psi\Psi$.
- The chirality $\Gamma = \gamma^{(8)}\gamma^{(1)}\cdots\gamma^{(7)} = \mathrm{diag}(-I_8, I_8)$ anticommutes with every $\gamma^{(a)}$, $\Gamma^2 = 1$, $[\Gamma, C] = 0$ (`Gamma_definition`, `Gamma_diag`, `Gamma_anticommutes_with_gammas`, `Gamma_commutes_with_C`; sympy `chirality_diag`).
- $B = -iC\gamma^{(4)}$ is Hermitian with $B^2 = 1$ and eigenvalues $+1$ and $-1$, eight each: signature (8,8) (`B_definition`, `B_Hermitian`, `B_squared_identity`, `B_signature_8_8`; sympy `B_hermitian_involution_signature`). $B$ commutes with $\gamma^{(1)}, \gamma^{(2)}, \gamma^{(3)}, \gamma^{(4)}, \gamma^{(8)}$ and anticommutes with $\gamma^{(5)}, \gamma^{(6)}, \gamma^{(7)}$ (`B_gamma_relations`).
- The 28 generators $S^{ab} = \frac14[\gamma^{(a)}, \gamma^{(b)}]$ satisfy the relations of so(4,4) (`S_Lorentz_algebra`, `S_lorentz_algebra`), rotate the gammas as a vector (`S_gamma_commutator`, `S_vector_action`), satisfy $(S^{ab})^T C + CS^{ab} = 0$ so that $\bar\Psi\Psi$ is Spin(4,4)-invariant (`S_preserves_C`), and commute with $\Gamma$ (`S_commutes_with_Gamma`). The Hermitian form $\Psi^\dagger B\Psi$ is invariant only under the Spin(4,3) that fixes $x_4$ (`S_preserves_B_only_off_x4`).

**Representation theorem (exact).** The 256 ordered products of gammas are linearly independent and span the full matrix algebra $\mathrm{Mat}(16)$ (`Clifford_basis_spans_full_matrix_algebra`, `clifford_products_span_M16`), and the commutant of the gammas is one-dimensional (`Pin44_irreducible_commutant_dim_1`, `pin_commutant_dimension_1`): the 16-dimensional representation is irreducible under Pin(4,4). The commutant of the 28 generators $S^{ab}$ is two-dimensional, spanned by the chiral projectors $(1 \mp \Gamma)/2$ (`Spin44_commutant_dim_2_chiral_projectors`, `spin_commutant_dimension_2`); each chiral half (rows 1 to 8 with $\Gamma = -1$, rows 9 to 16 with $\Gamma = +1$) is irreducible (`chiral_halves_irreducible`, `spin_halves_irreducible`); the spaces of intertwiners between the halves are zero (`chiral_halves_inequivalent_intertwiners_0`, `spin_halves_inequivalent`); the even subalgebra is $\mathrm{Mat}(8) \oplus \mathrm{Mat}(8)$ (`even_subalgebra_dimension`, `even_products_span_M8_plus_M8`). Every $\gamma^{(a)}$, the lift of a reflection (an element of Pin(4,4) of determinant $-1$ in O(4,4)), exchanges the two halves (`Spin_Pin_reflection_swaps_halves`, `reflections_exchange_halves`). Hence under Spin(4,4) the 16 splits into $8_- \oplus 8_+$, two inequivalent irreducible 8-dimensional representations, which the reflections combine into the one irreducible representation of Pin(4,4).

## 4. Coupling through the canonical spin connection

The coupling to gravity uses the vielbein and the canonical spin connection (SPEC section 3): $\omega_\mu{}^a{}_b$ is defined by the vielbein postulate $\partial_\mu e^a{}_\nu - \Gamma^\lambda{}_{\mu\nu}e^a{}_\lambda + \omega_\mu{}^a{}_b\,e^b{}_\nu = 0$, $\omega_{\mu ab} = \eta_{ac}\omega_\mu{}^c{}_b$ is antisymmetric in $a, b$, and

$$
\begin{aligned}
\Omega_\mu &= \tfrac12\,\omega_{\mu ab}S^{ab}, & D_\mu\Psi &= \partial_\mu\Psi + \Omega_\mu\Psi, \\
\gamma^\mu &= e_a{}^\mu\gamma^{(a)} = \gamma^{(\mu)}/f_\mu, & D_\mu\bar\Psi &= \partial_\mu\bar\Psi - \bar\Psi\Omega_\mu.
\end{aligned}
$$

(This is the canonical connection with the frame metric; the notebook's contraction of the mixed $\omega_\mu{}^a{}_b$, which lacks a metric factor, is not used.) The postulate holds for all 512 components and $\omega_{\mu ab} = -\omega_{\mu ba}$ (`vielbein_postulate` in both field-theory reports, `omega_antisymmetric`, `spin_connection_antisymmetric`). Exactly 12 components with $a < b$ are nonzero (`omega_components`; formula key `omega_nonzero`):

$$
\begin{aligned}
\omega_{x_i\,(i)(4)} &= a_4'\,e^{a_4}\sin^{1/6}z, & \omega_{x_i\,(i)(8)} &= H\,e^{a_4}\sin^{1/6}z, \\
\omega_{x_t\,(4)(t)} &= -a_4'\,e^{-a_4}\sin^{1/6}z, & \omega_{x_t\,(t)(8)} &= -H\,e^{-a_4}\sin^{1/6}z,
\end{aligned}
$$

and $\omega_{x_4} = \omega_{x_8} = 0$. The spinor connection is (`Omega_components`; sympy `Omega_x4_and_Omega_x8_vanish`)

$$
\begin{aligned}
\Omega_{x_i} &= \tfrac12\,e^{a_4}\sin^{1/6}z\,\big(a_4'\,\gamma^{(i)}\gamma^{(4)} + H\,\gamma^{(i)}\gamma^{(8)}\big) \qquad (i = 1, 2, 3), \\
\Omega_{x_t} &= -\tfrac12\,e^{-a_4}\sin^{1/6}z\,\big(a_4'\,\gamma^{(4)}\gamma^{(t)} + H\,\gamma^{(t)}\gamma^{(8)}\big) \qquad (t = 5, 6, 7), \\
\Omega_{x_4} &= \Omega_{x_8} = 0.
\end{aligned}
$$

It makes the gammas covariantly constant, $D_\mu\gamma^\nu = \partial_\mu\gamma^\nu + \Gamma^\nu{}_{\mu\lambda}\gamma^\lambda + [\Omega_\mu, \gamma^\nu] = 0$ for all 64 pairs (`gamma_covariantly_constant`, `covariant_constancy_D_mu_gamma_nu`), and its curvature is the Riemann tensor, $[D_\mu, D_\nu]\Psi = \frac12 R_{ab\mu\nu}S^{ab}\Psi$ (`spin_curvature_equals_Riemann`, `spinor_curvature_equals_riemann`).

The contraction that enters the field equation, per direction (no sum; formula key `gammaOmega_per_direction`):

$$
\begin{aligned}
\gamma^{x_i}\Omega_{x_i} &= \tfrac12 a_4'\,\gamma^{(4)} + \tfrac12 H\,\gamma^{(8)} \qquad (i = 1, 2, 3), \\
\gamma^{x_t}\Omega_{x_t} &= -\tfrac12 a_4'\,\gamma^{(4)} + \tfrac12 H\,\gamma^{(8)} \qquad (t = 5, 6, 7), \\
\gamma^{x_4}\Omega_{x_4} &= \gamma^{x_8}\Omega_{x_8} = 0,
\end{aligned}
$$

and summed:

$$
\gamma^\mu\Omega_\mu = 3H\gamma^{(8)} = \frac{1}{2\sqrt{|g|}}\,\partial_\mu\big(\sqrt{|g|}\,\gamma^\mu\big)
$$

(`gammaOmega_equals_3H_gamma_x8`, `gammaOmega_x4_terms_cancel`, `gammaOmega_divergence_form`). The sympy verifier confirms each of these statements independently (`gamma_mu_Omega_mu_equals_3H_gamma_x8`, `time_terms_cancel_hidden_term_survives` and `divergence_of_sqrtg_gamma`). The field-equations branch verifies the same value again, in a Clifford representation of its own and with T16 (`ownrep_gravity_term`, `authorT16_gravity_term`). For each direction separately $\{\gamma^\mu, \Omega_\mu\} = 0$ (no sum), because $\Omega_\mu$ contains only generators $S^{(\mu)b}$ (`gamma_mu_anticommutes_with_Omega_mu_no_sum`, `anticommutator_gamma_Omega_vanishes`).

**The value $3H\gamma^{(8)}$ belongs to the diagonal vielbein.** The canonical spin connection depends on the choice of the local frame, and so does the contraction $\gamma^\mu\Omega_\mu$. Boost the frame in the $(x_4, x_8)$ plane, $e'^{(4)} = \cosh b\,e^{(4)} + \sinh b\,e^{(8)}$, $e'^{(8)} = \sinh b\,e^{(4)} + \cosh b\,e^{(8)}$, the other $e'^{(a)} = e^{(a)}$, with rapidity $b = \beta x_4 + b_0$: the frame reproduces the author's metric, its canonical connection satisfies the vielbein postulate, and exactly, for every $a_4$ and $H$,

$$
\gamma'^\mu\Omega'_\mu = \frac{6H - \beta}{2}\,\big(\cosh b\,\gamma^{(8)} - \sinh b\,\gamma^{(4)}\big),
$$

which is $3H\gamma^{(8)}$ for the unboosted frame and vanishes identically for $\beta = 6H$. Both engines verify the frame and its connection (`boosted_frame_reproduces_metric` and `boosted_frame_canonical_connection`) and the contraction (`boosted_frame_gammaOmega_formula` and `boosted_frame_gammaOmega_vanishes`). In that frame $\Omega'_\mu$ is nonzero for $\mu = x_1, \dots, x_7$ and its curvature is nonzero (`boosted_frame_curvature_nonzero`): what no frame removes is $\Omega_\mu$ itself, whose curvature is the Riemann tensor, not the contraction $\gamma^\mu\Omega_\mu$.

## 5. The Lagrangian

The Lagrangian density (SPEC section 3), with an explicit mass term linear in $m$ and quadratic in the spinor:

$$
\begin{aligned}
\mathcal{L} &= \sqrt{|g|}\,\Big[\tfrac12\big(\bar\Psi\gamma^\mu D_\mu\Psi - (D_\mu\bar\Psi)\gamma^\mu\Psi\big) - m\,\bar\Psi\Psi - U(\bar\Psi\Psi)\Big], \\
\bar\Psi &= \Psi^\dagger C,\qquad S = \bar\Psi\Psi,\qquad U(S) = \tfrac{\lambda}{2}S^2 \quad\text{(general $U$ where stated)}.
\end{aligned}
$$

Properties, proved exactly for an explicit Grassmann algebra (Wolfram: generators $\theta_1, \theta_2$ and their conjugates, $\Psi_A = \sum_k \phi_{A,k}(x)\theta_k$; sympy: an own jet super-algebra; `grassmann_algebra_structure`, `superalgebra_axioms`):

- $\mathcal{L}$ is real: $\mathcal{L}^* = \mathcal{L}$, where conjugation reverses the order of Grassmann factors and $m$, $\lambda$ are real (`L_real_G`, `grassmann_lagrangian_real`; the control `grassmann_controls_not_vacuous` shows that the unsymmetrised form is not real off shell).
- It differs from the unsymmetrised form by a total divergence (`L_total_divergence_to_unsymmetrised_G`, `grassmann_total_divergence_relation`):

$$
\mathcal{L} = \sqrt{|g|}\,\big[\bar\Psi\gamma^\mu D_\mu\Psi - mS - U(S)\big] - \tfrac12\,\partial_\mu\big(\sqrt{|g|}\,\bar\Psi\gamma^\mu\Psi\big).
$$

- In this metric the spin connection drops out of $\mathcal{L}$ itself, because $\bar\Psi\{\gamma^\mu, \Omega_\mu\}\Psi = 0$ term by term (`L_spin_connection_drops_out_G`):

$$
\mathcal{L} = \cos z\,\Big[\tfrac12\sum_{a=1}^{8}\frac{1}{f_a}\big(\bar\Psi\gamma^{(a)}\partial_a\Psi - \partial_a\bar\Psi\gamma^{(a)}\Psi\big) - mS - U(S)\Big].
$$

  It reaches the field equations only through this identity: varying the symmetrised kinetic term produces $\partial_\mu(\sqrt{|g|}\gamma^\mu) = 2\sqrt{|g|}\,\gamma^\mu\Omega_\mu$ (section 7). Hence the Euler-Lagrange equations of $\mathcal{L}$ are those of the connection-free symmetric Lagrangian (the display above), and the term $3H\gamma^{(8)}$ is its half-density (volume and vielbein divergence) term (`connection_free_lagrangian_same_equations`, both engines).
- $S$ is an even element of the Grassmann algebra and $U$ is a polynomial in $S$; in the two-generator test algebra $S^3 = 0$, so $U = u_1 S + \frac{\lambda}{2}S^2$ is the most general potential there (`grassmann_algebra_structure`).

Negative control: the notebook's real Majorana-type Lagrangian $L_g = \sqrt{|g|}\,\Theta^T C\gamma^\mu D_\mu\Theta$ with 16 real anticommuting components is a total derivative, $L_g = \frac12\partial_\mu(\sqrt{|g|}\,\Theta^T C\gamma^\mu\Theta)$: all its Euler-Lagrange expressions vanish identically and it has no field equations; moreover $\Theta^T C\Theta = 0$ (`Majorana_Lg_total_derivative_grassmann`, `negative_control_majorana_grassmann_total_derivative`). For real commuting components the same expression is not a total derivative (`Majorana_Lg_commuting_control`, `negative_control_majorana_commuting_contrast`). This is why the Dirac-type Lagrangian with $\bar\Psi = \Psi^\dagger C$ is used.

## 6. The exact covariant field equations (Euler-Lagrange)

**Theorem (Euler-Lagrange equations).** For the Lagrangian of section 5 with an arbitrary potential $U$, the variation with respect to $\Psi^\dagger$ (left derivatives) gives $\sqrt{|g|}\,C\,[\gamma^\mu D_\mu\Psi - (m + U'(S))\Psi]$ and the variation with respect to $\Psi$ (right derivatives) gives the adjoint expression, for every component and every Grassmann generator. The field equations are

$$
\gamma^\mu D_\mu\Psi = \big(m + U'(S)\big)\Psi,\qquad (D_\mu\bar\Psi)\gamma^\mu = -\big(m + U'(S)\big)\bar\Psi,
$$

with $U'(S) = \lambda S$ for the quadratic potential (`EL_Psibar_G`, `EL_Psi_G`, `grassmann_euler_lagrange_psibar_variation` with the control that $m \to -m$ fails, `grassmann_euler_lagrange_psi_variation`). The adjoint equation is the Dirac conjugate of the field equation, so the two form one system (`adjoint_equation_is_Dirac_conjugate_G`, `grassmann_adjoint_equation_is_conjugate`).

Written out in the primordial field (`Dirac_operator_explicit_G`; formula key `field_equation`):

$$
\begin{aligned}
&e^{-a_4}\sin^{-1/6}z\,\big(\gamma^{(1)}\partial_1 + \gamma^{(2)}\partial_2 + \gamma^{(3)}\partial_3\big)\Psi + \gamma^{(4)}\partial_4\Psi \\
&\quad + e^{a_4}\sin^{-1/6}z\,\big(\gamma^{(5)}\partial_5 + \gamma^{(6)}\partial_6 + \gamma^{(7)}\partial_7\big)\Psi \\
&\quad + \tan z\,\gamma^{(8)}\partial_8\Psi + 3H\gamma^{(8)}\Psi = \big(m + U'(S)\big)\Psi,
\end{aligned}
$$

and the adjoint equation (formula key `adjoint_equation`):

$$
\begin{aligned}
&e^{-a_4}\sin^{-1/6}z\,\big(\partial_1\bar\Psi\gamma^{(1)} + \partial_2\bar\Psi\gamma^{(2)} + \partial_3\bar\Psi\gamma^{(3)}\big) + \partial_4\bar\Psi\gamma^{(4)} \\
&\quad + e^{a_4}\sin^{-1/6}z\,\big(\partial_5\bar\Psi\gamma^{(5)} + \partial_6\bar\Psi\gamma^{(6)} + \partial_7\bar\Psi\gamma^{(7)}\big) \\
&\quad + \tan z\,\partial_8\bar\Psi\gamma^{(8)} + 3H\bar\Psi\gamma^{(8)} = -\big(m + U'(S)\big)\bar\Psi.
\end{aligned}
$$

Since $(\gamma^{(4)})^2 = -1$, the field equation is equivalent to the first-order evolution equation (`evolution_form_G`)

$$
\partial_4\Psi = -\gamma^{(4)}\Big[\big(m + U'(S)\big)\Psi - \sum_{a \neq 4}\frac{1}{f_a}\gamma^{(a)}\partial_a\Psi - 3H\gamma^{(8)}\Psi\Big],
$$

so the slices $x_4 = $ const are non-characteristic ($g^{44} = -1$). In the chiral split $\Psi = (\psi_-, \psi_+)$ (rows 1 to 8 with $\Gamma = -1$, rows 9 to 16 with $\Gamma = +1$) every gamma is block off-diagonal, $\gamma^{(a)} = \begin{pmatrix} 0 & \bar\tau_a \\ \tau_a & 0\end{pmatrix}$ with $\bar\tau_8 = \tau_8 = I_8$, and the field equation is the pair (`block_form`; formula key `field_equation_blocks`)

$$
\sum_{a}\frac{1}{f_a}\bar\tau_a\partial_a\psi_+ + 3H\psi_+ = V\psi_-,\qquad
\sum_{a}\frac{1}{f_a}\tau_a\partial_a\psi_- + 3H\psi_- = V\psi_+,\qquad V = m + U'(S).
$$

The 16 component equations, $(\gamma^\mu D_\mu\Psi)_A = V\Psi_A$ with $\psi_A = \Psi_A$ the components in the basis of the fixture gammas, $\epsilon_s = e^{-a_4}\sin^{-1/6}z = 1/f_{1}$ and $\epsilon_t = e^{a_4}\sin^{-1/6}z = 1/f_{5}$ (formula key `field_equation_components`; `Dirac_operator_explicit_G`, `EL_Psibar_G`; the publication test of this document re-derives them from the formula file and compares them with the independent sympy expressions `dirac_equation_components` of the sympy report): the eight equations of the $\Gamma = -1$ rows,

$$
\begin{aligned}
\epsilon_s(-\partial_1\psi_{16} + \partial_2\psi_{15} - \partial_3\psi_{14}) - \partial_4\psi_{14} + \epsilon_t(\partial_5\psi_{15} + \partial_6\psi_{16} + \partial_7\psi_{9}) + (\tan z\,\partial_8 + 3H)\psi_{9} &= V\psi_{1} \\
\epsilon_s(-\partial_1\psi_{15} - \partial_2\psi_{16} + \partial_3\psi_{13}) + \partial_4\psi_{13} + \epsilon_t(\partial_5\psi_{16} - \partial_6\psi_{15} + \partial_7\psi_{10}) + (\tan z\,\partial_8 + 3H)\psi_{10} &= V\psi_{2} \\
\epsilon_s(\partial_1\psi_{14} - \partial_2\psi_{13} - \partial_3\psi_{16}) + \partial_4\psi_{16} + \epsilon_t(-\partial_5\psi_{13} + \partial_6\psi_{14} + \partial_7\psi_{11}) + (\tan z\,\partial_8 + 3H)\psi_{11} &= V\psi_{3} \\
\epsilon_s(\partial_1\psi_{13} + \partial_2\psi_{14} + \partial_3\psi_{15}) - \partial_4\psi_{15} + \epsilon_t(-\partial_5\psi_{14} - \partial_6\psi_{13} + \partial_7\psi_{12}) + (\tan z\,\partial_8 + 3H)\psi_{12} &= V\psi_{4} \\
\epsilon_s(-\partial_1\psi_{12} + \partial_2\psi_{11} - \partial_3\psi_{10}) + \partial_4\psi_{10} + \epsilon_t(-\partial_5\psi_{11} - \partial_6\psi_{12} - \partial_7\psi_{13}) + (\tan z\,\partial_8 + 3H)\psi_{13} &= V\psi_{5} \\
\epsilon_s(-\partial_1\psi_{11} - \partial_2\psi_{12} + \partial_3\psi_{9}) - \partial_4\psi_{9} + \epsilon_t(-\partial_5\psi_{12} + \partial_6\psi_{11} - \partial_7\psi_{14}) + (\tan z\,\partial_8 + 3H)\psi_{14} &= V\psi_{6} \\
\epsilon_s(\partial_1\psi_{10} - \partial_2\psi_{9} - \partial_3\psi_{12}) - \partial_4\psi_{12} + \epsilon_t(\partial_5\psi_{9} - \partial_6\psi_{10} - \partial_7\psi_{15}) + (\tan z\,\partial_8 + 3H)\psi_{15} &= V\psi_{7} \\
\epsilon_s(\partial_1\psi_{9} + \partial_2\psi_{10} + \partial_3\psi_{11}) + \partial_4\psi_{11} + \epsilon_t(\partial_5\psi_{10} + \partial_6\psi_{9} - \partial_7\psi_{16}) + (\tan z\,\partial_8 + 3H)\psi_{16} &= V\psi_{8}
\end{aligned}
$$

and the eight equations of the $\Gamma = +1$ rows,

$$
\begin{aligned}
\epsilon_s(\partial_1\psi_{8} - \partial_2\psi_{7} + \partial_3\psi_{6}) + \partial_4\psi_{6} + \epsilon_t(-\partial_5\psi_{7} - \partial_6\psi_{8} - \partial_7\psi_{1}) + (\tan z\,\partial_8 + 3H)\psi_{1} &= V\psi_{9} \\
\epsilon_s(\partial_1\psi_{7} + \partial_2\psi_{8} - \partial_3\psi_{5}) - \partial_4\psi_{5} + \epsilon_t(-\partial_5\psi_{8} + \partial_6\psi_{7} - \partial_7\psi_{2}) + (\tan z\,\partial_8 + 3H)\psi_{2} &= V\psi_{10} \\
\epsilon_s(-\partial_1\psi_{6} + \partial_2\psi_{5} + \partial_3\psi_{8}) - \partial_4\psi_{8} + \epsilon_t(\partial_5\psi_{5} - \partial_6\psi_{6} - \partial_7\psi_{3}) + (\tan z\,\partial_8 + 3H)\psi_{3} &= V\psi_{11} \\
\epsilon_s(-\partial_1\psi_{5} - \partial_2\psi_{6} - \partial_3\psi_{7}) + \partial_4\psi_{7} + \epsilon_t(\partial_5\psi_{6} + \partial_6\psi_{5} - \partial_7\psi_{4}) + (\tan z\,\partial_8 + 3H)\psi_{4} &= V\psi_{12} \\
\epsilon_s(\partial_1\psi_{4} - \partial_2\psi_{3} + \partial_3\psi_{2}) - \partial_4\psi_{2} + \epsilon_t(\partial_5\psi_{3} + \partial_6\psi_{4} + \partial_7\psi_{5}) + (\tan z\,\partial_8 + 3H)\psi_{5} &= V\psi_{13} \\
\epsilon_s(\partial_1\psi_{3} + \partial_2\psi_{4} - \partial_3\psi_{1}) + \partial_4\psi_{1} + \epsilon_t(\partial_5\psi_{4} - \partial_6\psi_{3} + \partial_7\psi_{6}) + (\tan z\,\partial_8 + 3H)\psi_{6} &= V\psi_{14} \\
\epsilon_s(-\partial_1\psi_{2} + \partial_2\psi_{1} + \partial_3\psi_{4}) + \partial_4\psi_{4} + \epsilon_t(-\partial_5\psi_{1} + \partial_6\psi_{2} + \partial_7\psi_{7}) + (\tan z\,\partial_8 + 3H)\psi_{7} &= V\psi_{15} \\
\epsilon_s(-\partial_1\psi_{1} - \partial_2\psi_{2} - \partial_3\psi_{3}) - \partial_4\psi_{3} + \epsilon_t(-\partial_5\psi_{2} - \partial_6\psi_{1} + \partial_7\psi_{8}) + (\tan z\,\partial_8 + 3H)\psi_{8} &= V\psi_{16}
\end{aligned}
$$

For the quadratic potential $V = m + \lambda S$ with $S = \Psi^\dagger C\Psi$, an even (bilinear) element; the equations hold in the Grassmann algebra, and after quantisation as operator equations (section 11).

## 7. Non-triviality [1]

**Theorem 1 (non-triviality [1]).** Hypotheses: the metric of section 2 with $H > 0$ and $0 < z < \pi/2$; $a_4$ any twice differentiable function of $x_4$ (a constant $a_4$ included); real $m$ and $\lambda$ (or any real potential $U$); the canonical spin connection of the diagonal vielbein; $\Psi$ any dirac16complex configuration (Grassmann-valued components) that is not identically zero. Then:

1. in the diagonal vielbein the Euler-Lagrange operator contains the gravitational term $\gamma^\mu D_\mu\Psi - \gamma^\mu\partial_\mu\Psi = \gamma^\mu\Omega_\mu\Psi = 3H\gamma^{(8)}\Psi$, and $3H\gamma^{(8)}\Psi \neq 0$ (this value depends on the frame and on the field variables, see the Remarks);
2. per direction, the time-direction terms of the three inflating and the three deflating directions cancel ($\frac32 a_4' - \frac32 a_4' = 0$), while the hidden-direction terms of all six directions add ($6 \cdot \frac{H}{2} = 3H$);
3. in addition the vielbein enters every derivative term, $\gamma^\mu\partial_\mu = \epsilon_s\gamma^{(i)}\partial_i + \gamma^{(4)}\partial_4 + \epsilon_t\gamma^{(t)}\partial_t + \tan z\,\gamma^{(8)}\partial_8$, none of whose factors is identically 1; because of the cancellation in 2, $a_4$ enters the field equations through these factors $e^{\mp a_4}$;
4. all gravitational terms vanish together only in flat 4+4 space: $\Omega_\mu = 0$ for every $\mu$ if and only if $a_4' = 0$ and $H = 0$, and $H = 0$ lies outside the family (a degenerate limit); no choice of local frame removes $\Omega_\mu$, because its curvature is the Riemann tensor and $R^{x_8}{}_{x_8} = -6H^2 \neq 0$: the metric is never flat for $H > 0$.

*Proof.* (a) The connection components of section 4 are each $a_4'$ or $H$ times a factor $\pm e^{\pm a_4}\sin^{1/6}z$ that does not vanish on $0 < z < \pi/2$; since the $S^{ab}$ are linearly independent, the $a_4'$-part of $\Omega_\mu$ vanishes if and only if $a_4$ is constant and its $H$-part if and only if $H = 0$ (`Omega_vanishes_iff_a4prime_and_H_vanish`, `nontriviality_Omega_zero_iff_flat`). (b) Contracting with $\gamma^\mu = \gamma^{(\mu)}/f_\mu$ and using $(\gamma^{(i)})^2 = 1$, $(\gamma^{(t)})^2 = -1$ gives the per-direction values of section 4: the $\gamma^{(4)}$ coefficients are $+\frac12 a_4'$ for each of the three inflating and $-\frac12 a_4'$ for each of the three deflating directions and cancel, the $\gamma^{(8)}$ coefficients are $\frac12 H$ for all six and add to $3H$; hence $\gamma^\mu\Omega_\mu = 3H\gamma^{(8)}$, a constant matrix independent of $a_4$, $x_4$ and $x_8$ (`gammaOmega_x4_terms_cancel`, `gammaOmega_equals_3H_gamma_x8`, `time_terms_cancel_hidden_term_survives`, `gamma_mu_Omega_mu_equals_3H_gamma_x8`). The same value follows from the divergence form $\frac{1}{2\cos z}\partial_8(\cos z\tan z)\gamma^{(8)} = \frac{6H\cos z}{2\cos z}\gamma^{(8)} = 3H\gamma^{(8)}$ (`gammaOmega_divergence_form`, `divergence_of_sqrtg_gamma`). (c) $(\gamma^{(8)})^2 = I_{16}$ and $\gamma^{(8)}$ is a signed permutation matrix, so each component of $\gamma^{(8)}\Psi$ is $\pm$ a component of $\Psi$; therefore $3H\gamma^{(8)}\Psi = 0$ implies $\Psi = 0$ for $H > 0$ (`nontriviality_1_dirac16complex`). (d) The term is part of the Euler-Lagrange equation although the connection drops out of $\mathcal{L}$ in this metric: the variation of the symmetrised kinetic term produces $\partial_\mu(\sqrt{|g|}\gamma^\mu) = 2\sqrt{|g|}\gamma^\mu\Omega_\mu$, and the Euler-Lagrange expressions equal $\sqrt{|g|}\,C\,(\gamma^\mu D_\mu\Psi - V\Psi)$ with the full covariant derivative (`L_spin_connection_drops_out_G`, `EL_Psibar_G`). (e) The curvature of $\Omega_\mu$ is $\frac12 R_{ab\mu\nu}S^{ab}$ (`spin_curvature_equals_Riemann`) and $R^{x_8}{}_{x_8} = -6H^2$ (`never_flat_for_H_positive`); if $\Omega_\mu$ vanished in some frame, the Riemann tensor would vanish. $H = 0$ is a degenerate limit of the metric (`degenerate_at_H_0`). This completes the proof.

Remarks (the exact scope of Theorem 1). In the formal flat limit ($a_4' = 0$ and $H = 0$ with the factors frozen) all gravitational terms vanish and the equation becomes the flat 4+4 Dirac-type equation, as the test [1] requires ("unless we are in flat 4+4 spacetime"). Items 1 and 2 are statements about the diagonal vielbein and the field variables $\Psi$; read without these hypotheses they would overstate [1]:

- The canonical connection drops out of $\mathcal{L}$, so the Euler-Lagrange equations are those of the connection-free symmetric Lagrangian; $3H\gamma^{(8)} = \frac{1}{2\sqrt{|g|}}\partial_\mu(\sqrt{|g|}\gamma^\mu)$ is its half-density term (`connection_free_lagrangian_same_equations`).
- In the frame boosted in the $(x_4, x_8)$ plane with rapidity $6Hx_4 + b_0$ the term $\gamma'^\mu\Omega'_\mu$ is identically zero (section 4; `boosted_frame_gammaOmega_vanishes`); gravity then enters the Euler-Lagrange operator only through the frame vectors $e'_a{}^\mu$.
- In the diagonal frame the rescaling $\Psi = \sin^{-1/2}z\,\chi$ removes it: $\gamma^\mu D_\mu\Psi = \sin^{-1/2}z\,\gamma^\mu\partial_\mu\chi$ exactly, so $\gamma^\mu\partial_\mu\chi = (m + U')\chi$; for $U = \frac{\lambda}{2}S^2$ the term turns into the $x_8$-dependent coupling $\lambda S[\chi]/\sin z$. The checks are `rescaling_removes_the_connection_term` and `rescaled_equation_quadratic_potential`. The exact $U = 0$ family of section 8 at $\alpha = -\frac12$ is this statement ($M = -m\gamma^{(4)}$, no $H$).
- The deflation of the extra times contributes nothing to $\gamma^\mu\Omega_\mu$, although $R^{x_4}{}_{x_4} = 6(a_4')^2 \neq 0$: $a_4$ enters only through the factors $e^{\mp a_4}$ of the derivative terms (`gammaOmega_blind_to_the_deflation`).
- The frame-independent content of [1] is item 4 with item 3: $\Omega_\mu$ vanishes in no frame (its curvature is the Riemann tensor and $R^{x_8}{}_{x_8} = -6H^2$), the vielbein factors $e^{\mp a_4}\sin^{-1/6}z$ and $\tan z$ enter every derivative term, and the metric is curved for every $H > 0$. In the diagonal frame the connection also enters the energy-momentum tensor, for example the off-diagonal $K^{x_4}{}_{x_1}$ of a homogeneous configuration (`spin_connection_in_the_energy_momentum_tensor`).
- Interpretation (labelled): the hidden-direction operator $\tan z\,\partial_8 + 3H$ is antisymmetric for the measure $\cos z\,dx_8$ in the variables $\Psi$ up to a boundary term, $\cos z\,[p(\tan z\,\partial_8 + 3H)q + ((\tan z\,\partial_8 + 3H)p)q] = \partial_8(\sin z\,pq)$ (`good_sector_hermiticity_curved`; formula key `hidden_direction_hermiticity`); in the variables $\chi$ with the measure $dy = \cot z\,dx_8$ the operator $\partial_y$ has the same property without any $H$ term. This role of $3H$ therefore depends on the variables and the measure, and the boundary term does not vanish at $z = \pi/2$ (section 11).

Non-triviality [2], for the commuting field dirac16complex00, has the same algebraic content and the same scope (`nontriviality_2_dirac16complex00`) and is the subject of the companion document `Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md`.

## 8. Self-consistency

The field equations of section 6 are self-consistent in the following exact senses.

- One system. The adjoint equation is the Dirac conjugate of the field equation: with $E = \gamma^\mu D_\mu\Psi - (m + U')\Psi$ and $\bar E = (D_\mu\bar\Psi)\gamma^\mu + (m + U')\bar\Psi$, $E^\dagger C = -\bar E$ exactly (`adjoint_equation_is_Dirac_conjugate_G`, `grassmann_adjoint_equation_is_conjugate`).
- Evolution form, not a well-posed Cauchy problem. The evolution form of section 6 holds exactly (`evolution_form_G`), and the Heisenberg equation of the quantised field reproduces it: see the Wolfram check `Heisenberg_equation_reproduces_field_equation` and the sympy check `hamiltonian_form_and_heisenberg_equation`. The slices $x_4 = $ const are non-characteristic, but the Cauchy problem is not well posed in Hadamard's sense for data that depend on $x_5, x_6, x_7$: with frozen coefficients an extra-time momentum $k_5 = K$ gives the growth rate $\sqrt{K^2 - m^2 - k_1^2 - k_2^2 - k_3^2 - k_8^2}$, unbounded as $K$ grows (`extra_time_growth_rates_unbounded`), and in the metric the frame momentum $e^{a_4}\sin^{-1/6}z\,k_{x_5}$ grows as the extra times deflate. A well-posed evolution is available at most in the good sector (no extra-time dependence) and only with a boundary condition at $z = \pi/2$ (section 11).
- Integrability. The gammas are covariantly constant and the spinor curvature is the Riemann tensor (section 4). The square of the Dirac operator obeys the Lichnerowicz identity (`Lichnerowicz_identity_G`, `lichnerowicz_identity_on_fields`, `lichnerowicz_contraction`):

$$
(\gamma^\mu D_\mu)^2\Psi = g^{\mu\nu}\big(D_\mu D_\nu\Psi - \Gamma^\lambda{}_{\mu\nu}D_\lambda\Psi\big) - \frac{R}{4}\Psi,\qquad R = 6\big((a_4')^2 - 7H^2\big),
$$

  so the second-order consequence of the field equations is consistent with the curvature.
- Conserved current. $J^\mu = -i\bar\Psi\gamma^\mu\Psi$ is real, and off shell $\partial_\mu(\sqrt{|g|}J^\mu) = -i\sqrt{|g|}\,(\bar E\Psi + \bar\Psi E)$, so $\nabla_\mu J^\mu = 0$ on shell (`current_real_G`, `current_conservation_identity_G`, `grassmann_current_conservation`). The charge density is $J^{x_4} = \Psi^\dagger B\Psi$, so the conserved charge $Q = \int\cos z\,\Psi^\dagger B\Psi\,d^7x$ is an indefinite form (`charge_density_is_Krein_form_G`).
- Bianchi-type identity of the energy-momentum tensor. For the tensor $T^\mu{}_\nu$ of section 9 the invariance of the action under coordinate changes gives, off shell and for each $\lambda$, $\partial_\mu(\sqrt{|g|}T^\mu{}_\lambda) - \sqrt{|g|}\,T^\mu{}_a\,\partial_\lambda e^a{}_\mu = \sum_\phi \mathrm{EL}_\phi\,\partial_\lambda\phi$ (`Noether_identity_diffeomorphisms_G`), and the invariance under the 28 local frame rotations makes the antisymmetric part of $T$ a combination of Euler-Lagrange expressions (`Noether_identity_local_Lorentz_G`). On shell, therefore, $T$ is symmetric and $\nabla_\mu T^\mu{}_\nu = 0$ for general solutions (`conservation_on_shell_general`); the sympy side verifies $\nabla_\mu T^\mu{}_\nu = 0$ for all eight $\nu$ after the on-shell substitution, with a negative control (`grassmann_emt_conservation_on_shell`, `grassmann_emt_conservation_negative_control`). The gravitational side satisfies the matching identities $\nabla_\mu E_{(k)}{}^\mu{}_\nu = 0$ (section 13).
- Exact solutions as test points. For $U = 0$ and every $a_4$, $\Psi = \sin^\alpha z\,\big(\cosh(kx_4) + \frac{\sinh(kx_4)}{k}M\big)\chi$ with constant $\chi$, $M = -m\gamma^{(4)} + 3H(2\alpha + 1)\gamma^{(4)}\gamma^{(8)}$, $k^2 = 9H^2(2\alpha + 1)^2 - m^2$, solves the field equation, and conservation of $T$ and $J$ holds exactly there (`solution_matrix_square`, `exact_solution_x4_x8_G`, `exact_solution_family_x4_x8`); the scope of this test is stated in the report: at these solutions the pressures and the momentum density vanish and $\rho = mS$ is constant, so the general proof is the pair of Noether identities. An exact nonlinear homogeneous solution with $U = \frac{\lambda}{2}S^2$ exists in the explicit Grassmann algebra, $\Psi = \sum_k\big[e^{M_m x_4} + \lambda S_0\,\partial_m e^{M_m x_4}\big]\chi_k\theta_k$ with $M_m = -m\gamma^{(4)} + 3H\gamma^{(4)}\gamma^{(8)}$ (`exact_solution_nonlinear_homogeneous_G`; formula key `exact_solutions`).

## 9. The energy-momentum tensor

The energy-momentum tensor is defined by the vielbein variation of the action and has the closed form (`T_vielbein_variation_closed_form_G`; formula key `T_variation`; sympy `grassmann_emt_equals_general_vielbein_variation_on_shell` with all 64 components of a general first-order vielbein variation)

$$
\begin{aligned}
T^\nu{}_\mu &= e^b{}_\mu\,\frac{1}{\sqrt{|g|}}\,\frac{\delta S}{\delta e^b{}_\nu}
= \delta^\nu_\mu\,\mathcal{L}_0 - \tfrac12\big(\bar\Psi\gamma^\nu D_\mu\Psi - D_\mu\bar\Psi\gamma^\nu\Psi\big) \\
&\quad - \tfrac14\,g_{\mu\rho}\nabla_\lambda\big(\bar\Psi\{\gamma^\lambda, \Sigma^{\nu\rho}\}\Psi\big),
\qquad \Sigma^{\nu\rho} = \tfrac14[\gamma^\nu, \gamma^\rho],\qquad \mathcal{L}_0 = \mathcal{L}/\sqrt{|g|},
\end{aligned}
$$

where the last term (the totally antisymmetric spin density) comes from the variation of the spin connection. Its symmetric part is the Belinfante tensor (`T_symmetric_part_Belinfante_G`, `grassmann_emt_symmetric`; formula key `T_symmetric`),

$$
T^{\nu\rho} = g^{\nu\rho}\mathcal{L}_0 - \tfrac14\big(\bar\Psi\gamma^\nu D^\rho\Psi + \bar\Psi\gamma^\rho D^\nu\Psi - D^\rho\bar\Psi\gamma^\nu\Psi - D^\nu\bar\Psi\gamma^\rho\Psi\big),
$$

which equals the variation tensor on shell (section 8). Sign convention (SPEC section 4): the energy density is $\rho = -T^{x_4}{}_{x_4}$ and the pressures are $p_\mu = T^\mu{}_\mu$ (no sum) for $\mu \neq x_4$; with this convention $\rho = mS + U$ for homogeneous on-shell configurations (section 10).

Kinetic and potential parts (formula key `EMT_kinetic_potential`): $T^\nu{}_\mu = T_{\rm kin}{}^\nu{}_\mu + T_{\rm pot}{}^\nu{}_\mu$ with

$$
\begin{aligned}
T_{\rm pot}{}^\nu{}_\mu &= -\delta^\nu_\mu\,\big(mS + U(S)\big), \\
T_{\rm kin}{}^\nu{}_\mu &= \delta^\nu_\mu\sum_\lambda K_\lambda - \tfrac14\big(\bar\Psi\gamma^\nu D_\mu\Psi - D_\mu\bar\Psi\gamma^\nu\Psi + \bar\Psi\gamma_\mu D^\nu\Psi - D^\nu\bar\Psi\gamma_\mu\Psi\big).
\end{aligned}
$$

Diagonal components in the primordial field (no sum; `T_diagonal_components_G`, `grassmann_emt_equals_vielbein_variation_diagonal`; formula key `EMT_diagonal`): with the directional kinetic terms

$$
K_\mu = \frac{1}{2f_\mu}\big(\bar\Psi\gamma^{(\mu)}\partial_\mu\Psi - \partial_\mu\bar\Psi\gamma^{(\mu)}\Psi\big),\qquad \mathcal{L}_0 = \sum_\mu K_\mu - mS - U(S),
$$

$$
T^\mu{}_\mu = \mathcal{L}_0 - K_\mu .
$$

No spin-connection term survives in the diagonal components, because $\{\gamma^\mu, \Omega_\mu\} = 0$ for each $\mu$. The off-diagonal component $x_4$-$x_8$, which SPEC section 5 lists among the components of the field equations for $a_4$, is (`T_x4_x8_component_G`; formula key `EMT_offdiagonal_x4_x8`)

$$
T^{x_4}{}_{x_8} = -\tfrac14\big(B_{48} - \cot z\,B_{84}\big),\qquad T^{x_8}{}_{x_4} = -\tan^2 z\;T^{x_4}{}_{x_8},
$$

with $B_{48} = \bar\Psi\gamma^{(4)}\partial_8\Psi - \partial_8\bar\Psi\gamma^{(4)}\Psi$ and $B_{84} = \bar\Psi\gamma^{(8)}\partial_4\Psi - \partial_4\bar\Psi\gamma^{(8)}\Psi$. For homogeneous on-shell configurations both $T^{x_4}{}_{x_8}$ and $T^{x_8}{}_{x_4}$ vanish identically (`grassmann_T_x4x8_homogeneous`), so these configurations do not source the $x_4$-$x_8$ component of the $a_4$ equations; this is not claimed for the other off-diagonal components (42 of the remaining 54 are nonzero bilinears in general), whose vanishing is a separate condition on the state (section 13). The trace (off shell, an exact identity in both engines) and the on-shell kinetic sum are (`EMT_trace_G`, `grassmann_trace_on_shell`, `kinetic_sum_on_shell_G`)

$$
T^\mu{}_\mu = 7\sum_\mu K_\mu - 8\big(mS + U\big),\qquad \sum_\mu K_\mu = \big(m + U'(S)\big)S + \tfrac12\big(\bar\Psi E - \bar E\Psi\big),
$$

so on shell $\mathcal{L}_0 = SU' - U$ and $T^\mu{}_\mu = -mS + 7SU' - 8U = -mS + 3\lambda S^2$. For a diagonal tensor $T = \mathrm{diag}(p_3, p_3, p_3, -\rho, p_t, p_t, p_t, p_8)$ whose entries are functions of $x_4$ and $x_8$, the covariant divergence is, in all eight components (`energy_exchange_equation` in both field-theory reports; formula key `energy_exchange`),

$$
\nabla_\mu T^\mu{}_{x_4} = -\partial_4\rho - 3a_4'\,(p_3 - p_t),\qquad \nabla_\mu T^\mu{}_{x_8} = \partial_8 p_8 + 3H\cot z\,(2p_8 - p_3 - p_t),
$$

and $\nabla_\mu T^\mu{}_\nu = 0$ identically for $\nu = x_1, x_2, x_3, x_5, x_6, x_7$. Conservation is therefore exactly

$$
\partial_4\rho = -3a_4'\,(p_3 - p_t),\qquad \partial_8 p_8 = -3H\cot z\,(2p_8 - p_3 - p_t) :
$$

energy flows between 3-space and the extra times unless $p_3 = p_t$ (the volume $\sqrt{|g|} = \cos z$ does not depend on $x_4$); the $x_4$ component contains no $x_8$ derivative and no $H$, the $x_8$ component no $x_4$ derivative and no $a_4'$. For entries independent of $x_8$ the two conditions become $d\rho/dx_4 = -3a_4'(p_3 - p_t)$ and $p_8 = (p_3 + p_t)/2$.

For dirac16complex these expressions are even elements of the Grassmann algebra; they are the classical counterpart of the energy-momentum tensor operator of section 12, from which all numbers come.

## 10. Kinetic energy, potential energy, energy density, pressures and equations of state

From the diagonal components of section 9 (formula keys `EMT_diagonal`, `EMT_kinetic_potential`, `equation_of_state_definitions`):

$$
\begin{aligned}
\rho &= -T^{x_4}{}_{x_4} = \rho_{\rm kin} + \rho_{\rm pot},\qquad \rho_{\rm kin} = -\sum_{\mu\neq x_4}K_\mu,\qquad \rho_{\rm pot} = mS + U(S), \\
p_3 &= T^{x_1}{}_{x_1} = \sum_{\mu\neq x_1}K_\mu - mS - U(S), \\
p_t &= T^{x_5}{}_{x_5} = \sum_{\mu\neq x_5}K_\mu - mS - U(S), \\
p_8 &= T^{x_8}{}_{x_8} = \sum_{\mu\neq x_8}K_\mu - mS - U(S),
\end{aligned}
$$

with $p_3 = T^{x_1}{}_{x_1} = T^{x_2}{}_{x_2} = T^{x_3}{}_{x_3}$ for configurations isotropic in 3-space and $p_t = T^{x_5}{}_{x_5} = T^{x_6}{}_{x_6} = T^{x_7}{}_{x_7}$ for configurations isotropic in the extra times. The kinetic energy density is $\rho_{\rm kin}$, the potential energy density $\rho_{\rm pot} = mS + U$; the kinetic pressure in direction $\mu$ is $\sum_{\nu\neq\mu}K_\nu$ and the potential pressure is $-(mS + U)$ in every direction. The equations of state are

$$
w_3 = \frac{p_3}{\rho},\qquad w_t = \frac{p_t}{\rho},\qquad w_8 = \frac{p_8}{\rho}.
$$

Homogeneous on-shell configurations (depending on $x_4$ only): $K_\mu = 0$ for $\mu \neq x_4$ and $K_{x_4} = (m + U')S$, hence (`grassmann_homogeneous_on_shell_rho_p`, `exact_solution_nonlinear_homogeneous_G`; formula key `EMT_homogeneous_on_shell`)

$$
\rho = mS + U,\qquad p_3 = p_t = p_8 = SU' - U,\qquad \rho_{\rm kin} = 0,\qquad p_{\rm kin} = (m + U')S,
$$

$$
w_3 = w_t = w_8 = \frac{SU' - U}{mS + U},
$$

and for $U = \frac{\lambda}{2}S^2$

$$
\rho = mS + \tfrac{\lambda}{2}S^2,\qquad p = \tfrac{\lambda}{2}S^2,\qquad w_3 = w_t = w_8 = \frac{\lambda S}{2m + \lambda S} .
$$

For the exact homogeneous solutions $S = S_0$ is constant along $x_4$ (`exact_solution_nonlinear_homogeneous_G`), so $\rho$, $p$ and $w$ are constant in $x_4$, in agreement with the energy-exchange equation ($p_3 = p_t$ gives $d\rho/dx_4 = 0$). For dirac16complex all these quantities are Grassmann-algebra elements until they are evaluated as expectation values of the normal-ordered operators of section 12. The equation of state seen by a 3-space observer and its time dependence (the dark-sector hypotheses of SPEC section 8) are not computed in this document; they belong to the dark-sector record of SPEC section 8, which is planned and not yet written.

## 11. Canonical quantisation in 4 + 4 dimensions and the Krein structure

The evolution time is $x_4$. The momentum conjugate to $\Psi_A$ (right derivative) is $\pi_A = \frac{i}{2}\cos z\,(\Psi^\dagger B)_A$ for the symmetric Lagrangian and $i\cos z\,(\Psi^\dagger B)_A$ for the first-order form; it depends on $\Psi^\dagger$ only, a second-class constraint as for Dirac's field (`canonical_momentum` in both reports). Up to a total divergence $\mathcal{L} = \Psi^\dagger K\,\partial_4\Psi - (\text{terms without }\partial_4)$ with $K = \cos z\,C\gamma^{(4)} = i\cos z\,B$, and the canonical (Dirac-bracket) anticommutator on a slice $x_4 = $ const is (`first_order_form_and_anticommutator`, `canonical_anticommutator_B`)

$$
\{\Psi_A(x), \Psi^\dagger_C(y)\}_{x_4 = y_4} = B_{AC}\,\frac{\delta^7(x - y)}{\sqrt{|g|}} = B_{AC}\,\frac{\delta^7(x - y)}{\cos z} .
$$

With the Hamiltonian density $\mathcal{H} = \cos z\,\big[\Psi^\dagger\big(mC - \sum_{\mu\neq x_4}C\gamma^\mu D_\mu\big)\Psi + U(S)\big]$ (the unsymmetrised $\mathcal{L} = \Psi^\dagger K\partial_4\Psi - \mathcal{H}$ exactly), the Heisenberg equation $\partial_4\Psi = i[H, \Psi]$ equals the field equation solved for $\partial_4\Psi$, with the operator ordering of the classical expression (`Heisenberg_equation_reproduces_field_equation`, `hamiltonian_form_and_heisenberg_equation`).

**Theorem 2 (the canonical anticommutator forces a Krein structure).** Hypotheses: the canonical anticommutator above, and $\Psi^\dagger$ realised as the adjoint of $\Psi$ in a space with a positive-definite inner product. These are incompatible: there is no positive inner product with $\Psi^\dagger$ as the adjoint. *Proof.* $B$ has the eigenvalue $-1$ with multiplicity 8; for the exact unit vector $u$ with components $u_7 = -i/\sqrt2$, $u_{16} = 1/\sqrt2$ and all others zero, $Bu = -u$, and the smeared operator $X = \sum_A u_A^*\Psi_A(f)$ has $\{X, X^\dagger\} = (u^\dagger Bu)\,\lVert f\rVert^2 = -\lVert f\rVert^2 < 0$, whereas in a space with positive inner product $\{X, X^\dagger\} = XX^\dagger + X^\dagger X$ is a positive operator (`no_positive_inner_product` in both reports). Hence the state space carries an indefinite (Krein) inner product with fundamental symmetry $B$ ($B = B^\dagger$, $B^2 = 1$, signature (8,8)); equivalently, in a positive Hilbert space the canonical conjugate $\Psi^\dagger$ is not the Hilbert adjoint $\chi$ but $\Psi^\dagger = \chi B$, with $\{\Psi_A, \chi_C\} = \delta_{AC}$.

The one-particle Krein structure. The curved mode operator $h$ ($i\partial_4\Psi = h\Psi$ for $U = 0$) is formally self-adjoint for the Krein form $\int\cos z\,u^\dagger Bv\,d^7x$, that is up to boundary terms (`Krein_form_conserved_curved`). The boundary term of the hidden direction does not vanish at the patch end: $\cos z\,[u^\dagger(hv) - (hu)^\dagger v] = \partial_8(\sin z\,u^\dagger M_8 v)$ with $M_8 = i\gamma^{(4)}\gamma^{(8)}$ in the good sector at $k = 0$, which vanishes at the tip but not at $z = \pi/2$, a surface at finite proper distance where $\sin z = 1$ (`good_sector_hermiticity_up_to_the_brane_flux`, both engines). The Krein form is therefore conserved, and $h$ self-adjoint, only with a boundary condition at $z = \pi/2$ (for example the ASSUMED brane condition of the Kohn-Sham record); this record imposes none. For frozen coefficients (frame momenta $k_a$), plane waves $u\,e^{i(k\cdot x - Ex_4)}$ obey $Eu = h_k u$ with $h_k = m\beta + \sum_a k_a\alpha^a$, $\beta = -i\gamma^{(4)}$, $\alpha^a = -\gamma^{(4)}\gamma^{(a)}$; $\beta$ and $\alpha^{1,2,3,8}$ are Hermitian, $\alpha^{5,6,7}$ anti-Hermitian, $Bh_k = h_k^\dagger B$ (Krein self-adjoint), and (`mode_hamiltonian_good_sector`, `mode_hamiltonian_Krein_selfadjoint`, `mode_hamiltonian_B_selfadjoint_dispersion`)

$$
h_k^2 = \big(m^2 + k_1^2 + k_2^2 + k_3^2 + k_8^2 - k_5^2 - k_6^2 - k_7^2\big)\,I_{16} .
$$

Good sector (no dependence on the extra times, $k_5 = k_6 = k_7 = 0$): $h_k$ is Hermitian with eigenvalues $\pm E$, eight each, and commutes with $B$; $B$ also commutes with the curved term $3iH\gamma^{(4)}\gamma^{(8)}$ (`good_sector_spectrum_and_B_sectors`). The curved mode operator is symmetric for the measure $\cos z\,d^7x$ in this sector only up to the boundary term at $z = \pi/2$ (`good_sector_hermiticity_curved`, `good_sector_hermiticity_up_to_the_brane_flux`): on the good-sector functions that do not depend on $x_8$ (finite norm, $\int_0^{\pi/(12H)}\cos(6Hx_8)\,dx_8 = 1/(6H)$) it acts as the matrix $-im\gamma^{(4)} + 3iH\gamma^{(4)}\gamma^{(8)}$, which is not Hermitian and has the square $(m^2 - 9H^2)I_{16}$; at $m = H = 1$ its eigenvalues are $\pm 2\sqrt2\,i$ (`good_sector_x8_independent_modes_without_boundary_condition`). Without a boundary condition at $z = \pi/2$ the good sector of the author's metric therefore contains growing modes, for $U = 0$ whenever $m^2 < 9H^2$; the exact solutions of section 8 with $\alpha = 0$ ($k^2 = 9H^2 - m^2$) are such modes. Positive Fock realisation: $\Psi = \sum_s(b_s u_s + d_s^* v_s)$ with orthonormal eigenvectors $u_s$ (energy $+E$) and $v_s$ (energy $-E$), $\{b, b^*\} = \{d, d^*\} = 1$ on a positive Fock space, and $\Psi^\dagger = \chi B$, so that $\{\Psi_A, \Psi^\dagger_C\} = B_{AC}$. Exact examples (one momentum each): Wolfram, $m = 3$, $k = (4, 0, 0, 0)$ along $x_1$, $E = 5$, on the explicit fermionic Fock space of $2^{16}$ occupation states; sympy, $m = 2$, $(k_1, k_2, k_3, k_8) = (1, 2, 0, 4)$, $E = 5$. The Hamiltonian $\chi h_k\Psi$ has the vacuum value $-8E$ (the filled sea; $-40$ in the sympy example), and after normal ordering the energy is $+E$ for the particle $b_0^*|0\rangle$ and $+E$ for the antiparticle $d_0^*|0\rangle$; the charge $\Psi^\dagger B\Psi = \chi\Psi$ is $+1$ and $-1$ (`Fock_space_good_sector_example`, `good_sector_positive_fock_realisation`).

Expectation-value rule. In the positive realisation, $\langle u|{:}\Psi^\dagger M\Psi{:}|u\rangle = u^\dagger BMu$ for a particle and $-v^\dagger BMv$ for an antiparticle (verified for $M = C$, $-iC\gamma^{(4)}$, $-iC\gamma^{(1)}$, $C\gamma^{(2)}\gamma^{(3)}$, a dense integer matrix and a generic symbolic matrix). In the Krein-Fock realisation ($\Psi^\dagger$ the Krein adjoint, modes with $u_n^\dagger Bu_n = \epsilon_n$) the normalised expectation of ${:}\Psi^\dagger M\Psi{:}$ is $\epsilon_n u_n^\dagger Mu_n$, which equals $u_n^\dagger BMu_n$ when $Bu_n = \epsilon_n u_n$ and not for a Krein-boosted mode (`Fock_space_good_sector_example`, `good_sector_positive_fock_realisation`, `expectation_value_rule`).

Extra-time modes. With extra-time momentum, $E^2 = m^2 + k_s^2 - k_t^2$ is negative when $k_t^2 > m^2 + k_s^2$; exact example $m = 1$, $k_5 = 2$: $E = \pm i\sqrt3$, modes growing like $e^{\sqrt3\,x_4}$. The growth rate has no upper bound as the extra-time momentum grows (`extra_time_growth_rates_unbounded`). In the metric the frame momentum $k_{(5)} = e^{a_4}\sin^{-1/6}z\,k_{x_5}$ grows as the extra times deflate ($a_4$ increasing), so every extra-time mode eventually enters the growing regime (a local-frame statement); extra-time momenta mix the $B = \pm1$ sectors (`extra_time_modes_grow`, `mode_hamiltonian_good_sector`, `good_sector_spectrum_and_B_sectors`). Krein structure of the one-particle eigenspaces in flat 4+4 space (pairing record): every eigenspace of REAL frequency, $E^2 > 0$, with or without extra-time momentum, has Krein inertia (4,4) (proved for every real frequency: `Q_one_particle_Krein_inertia_real_frequencies`, `Q.one_particle_Krein_inertia_proof`), while the eigenspaces of imaginary or zero frequency, those of the growing modes, are Krein-neutral, $B$ vanishes on them identically (`Q_one_particle_complex_and_zero_frequencies_Krein_neutral`, `Q.one_particle_complex_frequency_Krein_neutral`; for $m = 1$, $k_5 = 2$ both 8-dimensional eigenspaces of $\pm i\sqrt3$).

Scope: the positive Fock realisation is constructed and checked for single good-sector momenta with frozen coefficients; together with the formal (up to the boundary term at $z = \pi/2$) Hermiticity of the curved good-sector mode operator and the formal conservation of the Krein form this is the quantisation recorded here. A complete construction for the interacting field ($\lambda \neq 0$), for the extra-time sector with its growing modes, and of the field algebra on a whole slice is not part of this record (section 15).

## 12. The energy-momentum tensor operator

The energy-momentum tensor operator of dirac16complex is the tensor of section 9 with the field replaced by the quantised field and normal ordered with respect to the good-sector modes (formula key `quantisation`):

$$
\hat T^\nu{}_\mu(x) = {:}\,T^\nu{}_\mu\big[\hat\Psi, \hat{\bar\Psi}\big]\,{:}\,,\qquad \hat{\bar\Psi} = \hat\Psi^\dagger C,\qquad \hat\Psi^\dagger = \hat\chi B \quad\text{(positive realisation)} .
$$

Explicitly, with $\hat S = \hat\Psi^\dagger C\hat\Psi$ and $\hat K_\mu = \frac{1}{2f_\mu}\big(\hat{\bar\Psi}\gamma^{(\mu)}\partial_\mu\hat\Psi - \partial_\mu\hat{\bar\Psi}\gamma^{(\mu)}\hat\Psi\big)$:

$$
\begin{aligned}
\hat\rho &= -\hat T^{x_4}{}_{x_4} = {:}\Big(-\sum_{\mu\neq x_4}\hat K_\mu + m\hat S + U(\hat S)\Big){:}, \\
\hat p_\mu &= \hat T^\mu{}_\mu = {:}\Big(\sum_{\nu\neq\mu}\hat K_\nu - m\hat S - U(\hat S)\Big){:} \qquad (\mu \neq x_4), \\
\hat T^{\nu\rho} &= {:}\Big(g^{\nu\rho}\hat{\mathcal{L}}_0 - \tfrac14\big(\hat{\bar\Psi}\gamma^\nu D^\rho\hat\Psi + \hat{\bar\Psi}\gamma^\rho D^\nu\hat\Psi - D^\rho\hat{\bar\Psi}\gamma^\nu\hat\Psi - D^\nu\hat{\bar\Psi}\gamma^\rho\hat\Psi\big)\Big){:},
\end{aligned}
$$

with the kinetic part ${:}\big(-\sum_{\mu\neq x_4}\hat K_\mu\big){:}$ and the potential part ${:}\big(m\hat S + U(\hat S)\big){:}$ of the energy density. Properties and status:

- Normal ordering removes the vacuum value of the filled sea ($-8E$ per good-sector momentum in the exact examples of section 11) and gives positive energy $+E$ to particles and antiparticles (`Fock_space_good_sector_example`, `good_sector_positive_fock_realisation`).
- For $\lambda = 0$ every component of $\hat T$ is a normal-ordered bilinear $\hat\Psi^\dagger M\hat\Psi$ (with $M$ containing the derivatives, which act on the mode functions), and its one-particle expectation values follow the expectation-value rule of section 11; in the sympy formulation the one-particle expectation of $\hat T$ is $\epsilon_n$ times the classical bilinear evaluated on the mode $u_n$ (formula key `quantisation` of the sympy report).
- For $\lambda \neq 0$ the potential term is quartic. The field-equations record states the rule used there: every bilinear is replaced by the expectation value of its normal-ordered operator in the state, with $\langle{:}U(S){:}\rangle \neq U(\langle{:}S{:}\rangle)$ in general, and it records the operator form of the on-shell identity $\sum_\mu\langle{:}K_\mu{:}\rangle = \langle{:}(m + U')S{:}\rangle$ as an assumption to be confirmed by the theory branch (key `dirac16complex` of `Revision/field_equations_a4/a4-equations.json`). The identity is verified exactly for the Grassmann-algebra field (`kinetic_sum_on_shell_G`); its normal-ordered operator form for $\lambda \neq 0$ is not verified by a Revision check. Numerical expectation values of $\hat T$ for many-fermion states are computed only in the Kohn-Sham approximation (`Revision/kohn_sham/`; its document is planned and not yet written) and are not quoted here.
- The Grassmann-algebra tensor of sections 9 and 10 obeys the identities of section 8 (symmetry and conservation on shell); the operator inherits them for the bilinear ($\lambda = 0$) part, where they are linear in the field equations; for the quartic part this is part of the open operator question just stated.

## 13. The field equations for a4[x4] with dirac16complex as the source

Einstein-Lovelock gravity (SPEC section 5), with the Lovelock tensors computed with the generalised Kronecker delta in `Revision/gkd_lovelock` and recomputed in both verifiers of the field-equations branch (for example `P3_direct_equals_gkd_branch_monomials`, `P1_direct_equals_minus_4_Einstein` and `P4_vanishes_pigeonhole`; sympy `P3_equals_gkd_branch_monomials`):

$$
\sum_{k=1}^{3}\alpha_k\,E_{(k)}{}^\mu{}_\nu + \Lambda\,\delta^\mu_\nu = \kappa\,T^\mu{}_\nu,\qquad E_{(k)} = -\frac{P_{(k)}}{2^{k+1}},\qquad E_{(1)} = G,
$$

with $\alpha_1 = 1$ for Einstein gravity and the source $T^\mu{}_\nu = \mathrm{diag}(p_3, p_3, p_3, -\rho, p_t, p_t, p_t, p_8) + q_{48} + q_{84}$ ($q_{48}$ at $\mu = x_4$, $\nu = x_8$; $q_{84}$ at $\mu = x_8$, $\nu = x_4$). The left-hand sides are divergence-free (`E1_divergence_free`, `E2_divergence_free`, `E3_divergence_free` in both reports). Their nonzero components are diagonal, with $x_1 = x_2 = x_3$ and $x_5 = x_6 = x_7$, free of $x_8$ and of $a_4$ itself; every off-diagonal left-hand side, including $x_4$-$x_8$, is zero (`independent_components`, `P1_structure`, `P2_structure`, `P3_structure`; sympy `other_components_vanish`). The diagonal components (formula key `lovelockTensors`; `json_lovelock_components`):

$$
\begin{aligned}
E_{(1)}{}^{x_1}{}_{x_1} &= -3 (a_4')^{2} + a_4'' + 15 H^{2} \\
E_{(1)}{}^{x_4}{}_{x_4} &= 3 (a_4')^{2} + 21 H^{2} \\
E_{(1)}{}^{x_5}{}_{x_5} &= -3 (a_4')^{2} - a_4'' + 15 H^{2} \\
E_{(1)}{}^{x_8}{}_{x_8} &= -3 (a_4')^{2} + 15 H^{2} \\
E_{(2)}{}^{x_1}{}_{x_1} &= 12 (a_4')^{4} - 24 (a_4')^{2} a_4'' + 168 (a_4')^{2} H^{2} - 40 a_4'' H^{2} - 180 H^{4} \\
E_{(2)}{}^{x_4}{}_{x_4} &= -36 (a_4')^{4} - 120 (a_4')^{2} H^{2} - 420 H^{4} \\
E_{(2)}{}^{x_5}{}_{x_5} &= 12 (a_4')^{4} + 24 (a_4')^{2} a_4'' + 168 (a_4')^{2} H^{2} + 40 a_4'' H^{2} - 180 H^{4} \\
E_{(2)}{}^{x_8}{}_{x_8} &= 12 (a_4')^{4} + 168 (a_4')^{2} H^{2} - 180 H^{4} \\
E_{(3)}{}^{x_1}{}_{x_1} &= -72 (a_4')^{6} + 360 (a_4')^{4} a_4'' - 648 (a_4')^{4} H^{2} + 432 (a_4')^{2} a_4'' H^{2} \\
&\quad - 1944 (a_4')^{2} H^{4} + 360 a_4'' H^{4} + 360 H^{6} \\
E_{(3)}{}^{x_4}{}_{x_4} &= 360 (a_4')^{6} + 648 (a_4')^{4} H^{2} + 1080 (a_4')^{2} H^{4} + 2520 H^{6} \\
E_{(3)}{}^{x_5}{}_{x_5} &= -72 (a_4')^{6} - 360 (a_4')^{4} a_4'' - 648 (a_4')^{4} H^{2} - 432 (a_4')^{2} a_4'' H^{2} \\
&\quad - 1944 (a_4')^{2} H^{4} - 360 a_4'' H^{4} + 360 H^{6} \\
E_{(3)}{}^{x_8}{}_{x_8} &= -72 (a_4')^{6} - 648 (a_4')^{4} H^{2} - 1944 (a_4')^{2} H^{4} + 360 H^{6}
\end{aligned}
$$

The independent field equations (formula key `generalSource`):

- constraint ($x_4$): $\sum_k\alpha_k E_{(k)}{}^{x_4}{}_{x_4} + \Lambda = -\kappa\rho$;
- 3-space ($x_1 = x_2 = x_3$): $\sum_k\alpha_k E_{(k)}{}^{x_1}{}_{x_1} + \Lambda = \kappa p_3$;
- extra times ($x_5 = x_6 = x_7$): $\sum_k\alpha_k E_{(k)}{}^{x_5}{}_{x_5} + \Lambda = \kappa p_t$;
- hidden direction ($x_8$): $\sum_k\alpha_k E_{(k)}{}^{x_8}{}_{x_8} + \Lambda = \kappa p_8$;
- off-diagonal: $0 = \kappa T^\mu{}_\nu$ for $\mu \neq \nu$, in particular $q_{48} = q_{84} = 0$.

The evolution equation is the 3-space minus extra-time combination; it contains $a_4''$ and factorises (`evolution_factorises_a4pp_times_F`, `evolution_factorises`; formula key `evolution_F`):

$$
a_4''\,F(a_4') = \kappa\,(p_3 - p_t),
$$

$$
F(a_4') = 2\,\alpha_1 + \alpha_2\,(-48 (a_4')^{2} - 80 H^{2}) + \alpha_3\,(720 (a_4')^{4} + 864 (a_4')^{2} H^{2} + 720 H^{4})
$$

and $F$ vanishes identically only for $\alpha_1 = \alpha_2 = \alpha_3 = 0$ (`evolution_F_not_identically_zero` in both reports). The constraint and the $x_8$ equation are first order (`x8_component_contains_no_a4pp`, `constraint_and_x8_first_order`). The remaining consistency conditions:

- algebraic condition: $\sum_k\alpha_k(E^{x_1}{}_{x_1} + E^{x_5}{}_{x_5} - 2E^{x_8}{}_{x_8}) = 0$ identically, so the source must satisfy $p_3 + p_t = 2p_8$ (`algebraic_identity_x1_plus_x5_minus_2x8`, `algebraic_identity`);
- $x_8$-dependence: since the left-hand sides do not depend on $x_8$, every component of $T^\mu{}_\nu$ must be independent of $x_8$, and $q_{48} = q_{84} = 0$ (key `x8_dependence`);
- constraint propagation (Bianchi identity): $\frac{d}{dx_4}\sum_k\alpha_k E_{(k)}{}^{x_4}{}_{x_4} = 3a_4'\sum_k\alpha_k\big(E^{x_1}{}_{x_1} - E^{x_5}{}_{x_5}\big)$ identically (`constraint_propagation_bianchi`, `bianchi_x4`); with the conservation law $\rho' = -3a_4'(p_3 - p_t)$ the evolution equation follows from the constraint wherever $a_4' \neq 0$. The conservation components of a general source are $\nabla_\mu T^\mu{}_{x_4} = -\partial_4\rho - 3a_4'(p_3 - p_t) + \partial_8 q_{84} - 6H\tan z\,q_{84}$ and $\nabla_\mu T^\mu{}_{x_8} = \partial_8 p_8 + 3H\cot z\,(2p_8 - p_3 - p_t) + \partial_4 q_{48}$ (`conservation_components` in both reports).

Einstein gravity ($\alpha_1 = 1$, $\alpha_2 = \alpha_3 = 0$; `einstein_components`; formula key `einstein`):

$$
\begin{aligned}
3 (a_4')^{2} + 21 H^{2} + \Lambda &= -\kappa\rho \\
-3 (a_4')^{2} + a_4'' + 15 H^{2} + \Lambda &= \kappa p_3 \\
-3 (a_4')^{2} - a_4'' + 15 H^{2} + \Lambda &= \kappa p_t \\
-3 (a_4')^{2} + 15 H^{2} + \Lambda &= \kappa p_8
\end{aligned}
$$

so $2a_4'' = \kappa(p_3 - p_t)$ and $\kappa(\rho + p_8) = -6\big((a_4')^2 + H^2\big) < 0$ for every $a_4$ and every $\Lambda$: the source must violate the null energy condition along the null direction $x_4 + x_8$ (`einstein_null_energy_x8`), and there is no vacuum solution for $H > 0$ (`einstein_no_vacuum_solution`, `einstein_no_vacuum`). Every twice differentiable $a_4$ is allowed if the source is the one these equations require (key `sourceRequiredByGivenA4`); $\kappa\rho > 0$ needs $\Lambda < -(3(a_4')^2 + 21H^2)$.

The linear member $a_4 = AHx_4 + a_0$ (3-space scale factor $e^{AHx_4}$, extra-time scale factor $e^{-AHx_4}$: exponential deflation for $A > 0$). The field equations then require $p_3 = p_t = p_8 = p$, with $\rho$ and $p$ constant, for any $\alpha_k$ (`linear_member_equal_pressures`; key `linearMember`):

$$
\begin{aligned}
\kappa\rho &= \alpha_1\,(-3 A^{2} H^{2} - 21 H^{2}) + \alpha_2\,(36 A^{4} H^{4} + 120 A^{2} H^{4} + 420 H^{4}) \\
&\quad + \alpha_3\,(-360 A^{6} H^{6} - 648 A^{4} H^{6} - 1080 A^{2} H^{6} - 2520 H^{6}) - \Lambda \\
\kappa p &= \alpha_1\,(-3 A^{2} H^{2} + 15 H^{2}) + \alpha_2\,(12 A^{4} H^{4} + 168 A^{2} H^{4} - 180 H^{4}) \\
&\quad + \alpha_3\,(-72 A^{6} H^{6} - 648 A^{4} H^{6} - 1944 A^{2} H^{6} + 360 H^{6}) + \Lambda \\
\mathcal{V}(A) &= \alpha_1 + \alpha_2\,(-8 A^{2} H^{2} - 40 H^{2}) + \alpha_3\,(72 A^{4} H^{4} + 144 A^{2} H^{4} + 360 H^{4})
\end{aligned}
$$

A vacuum ($\rho = p = 0$) needs $\mathcal{V}(A) = 0$ (`linear_member_vacuum_factor`); in Einstein-Gauss-Bonnet gravity ($\alpha_3 = 0$) this gives $A^2 = (1 - 40\alpha_2H^2)/(8\alpha_2H^2)$, real for $0 < \alpha_2H^2 \le 1/40$ (`einstein_gauss_bonnet_vacuum_linear`). For Einstein gravity $\kappa\rho = -(3A^2 + 21)H^2 - \Lambda$, $\kappa p = (15 - 3A^2)H^2 + \Lambda$ and $\kappa(\rho + p) = -6(A^2 + 1)H^2$.

Specialisation to dirac16complex. The source is the energy-momentum tensor of section 9 with the declared sign $\sigma_T = +1$ (key `emtConvention`: $T^\mu{}_\nu = \sigma_T(-K^{(\mu}{}_{\nu)} + \delta^\mu_\nu\mathcal{L}_0)$, the convention $\rho = -T^{x_4}{}_{x_4}$ of SPEC section 4; the relative sign of the gravitational and matter actions is carried as the parameter $\sigma_T$ in the field-equations record and is not fixed by a Revision check). For the quantised field every bilinear is replaced by the expectation value of its normal-ordered operator in the state (section 12), with $k_\mu = K_\mu$:

$$
\begin{aligned}
\rho &= \langle{:}k_4{:}\rangle - \langle{:}\mathcal{L}_0{:}\rangle, & p_3 &= \langle{:}\mathcal{L}_0{:}\rangle - \langle{:}k_1{:}\rangle, \\
p_t &= \langle{:}\mathcal{L}_0{:}\rangle - \langle{:}k_5{:}\rangle, & p_8 &= \langle{:}\mathcal{L}_0{:}\rangle - \langle{:}k_8{:}\rangle,
\end{aligned}
$$

and the equations become (key `dirac16complex` of the field-equations record):

- constraint: $\sum_k\alpha_k E_{(k)}{}^{x_4}{}_{x_4} + \Lambda = -\kappa\big(\langle{:}k_4{:}\rangle - \langle{:}\mathcal{L}_0{:}\rangle\big)$;
- evolution: $a_4''F(a_4') = \kappa\big(\langle{:}k_5{:}\rangle - \langle{:}k_1{:}\rangle\big)$: a state with $\langle{:}k_1{:}\rangle \neq \langle{:}k_5{:}\rangle$ would drive $a_4''$ if it also satisfied the conditions below ($p_3 + p_t = 2p_8$, every expectation value independent of $x_8$, vanishing off-diagonal components); no such state is constructed in Revision;
- hidden direction: $\sum_k\alpha_k E_{(k)}{}^{x_8}{}_{x_8} + \Lambda = \kappa\big(\langle{:}\mathcal{L}_0{:}\rangle - \langle{:}k_8{:}\rangle\big)$, and the algebraic condition $2\langle{:}k_8{:}\rangle = \langle{:}k_1{:}\rangle + \langle{:}k_5{:}\rangle$;
- every off-diagonal expectation value $\langle{:}T^\mu{}_\nu{:}\rangle$, $\mu \neq \nu$, must vanish, and every expectation value must be independent of $x_8$. For a homogeneous configuration the off-diagonal components are multiples of the 15 three-gamma bilinears $\bar\Psi\gamma^{(a)}\gamma^{(b)}\gamma^{(c)}\Psi$ with $\{a, b, c\} = \{i, 4, 8\}$ ($i = 1, 2, 3, 5, 6, 7$) and $\{i, 4, j\}$ ($i = 1, 2, 3$, $j = 5, 6, 7$), derived for the classical homogeneous condensate (`condensate_offdiagonal_are_three_gamma_bilinears`, `authorT16_condensate_offdiagonal_three_gamma`; key `offDiagonalConditions`); for dirac16complex their expectation values must vanish.

**Statement (states with equal 3-space and extra-time kinetic terms; key `homogeneousSingleMode`).** Hypotheses: a state whose normal-ordered expectation values depend on $x_4$ only, satisfy the off-diagonal conditions and have $\langle{:}k_1{:}\rangle = \langle{:}k_5{:}\rangle$ for every $x_4$ (for example all quanta at zero 3-momentum and zero extra-time momentum); $a_4$ twice continuously differentiable; $(\alpha_1, \alpha_2, \alpha_3) \neq (0, 0, 0)$. Then $a_4''F(a_4') = 0$; $F$ is a nonzero polynomial in $a_4'$ with finitely many roots (`evolution_F_not_identically_zero`) and $a_4'$ is continuous, so $a_4'' = 0$ on every interval and $a_4 = AHx_4 + a_0$ with real $A$: only the linear member is allowed (the same argument as the theorem for the classical condensate, key `theoremLinear`, with `linear_member_equal_pressures`). The equations contain $A$ only through $A^2$, so they are invariant under $A \to -A$: the extra times deflate for $A > 0$, which is a choice of sign (an initial condition) and is not selected by the equations; $A < 0$ is allowed on the same footing, and $A = 0$ is the static case. If in addition $\langle{:}k_\mu{:}\rangle = 0$ for every $\mu \neq x_4$, then $\rho = \langle{:}mS + U{:}\rangle$ exactly and $p = \langle{:}k_4{:}\rangle - \langle{:}mS + U{:}\rangle$, which equals $\langle{:}SU' - U{:}\rangle$ under the operator form of the on-shell identity of section 12 (an assumption for $\lambda \neq 0$). With it, Einstein gravity requires $\kappa\langle{:}mS + U{:}\rangle = -(3A^2 + 21)H^2 - \Lambda$ and $\kappa\langle{:}SU' - U{:}\rangle = (15 - 3A^2)H^2 + \Lambda$, hence $\kappa\langle{:}(m + U')S{:}\rangle = -6(A^2 + 1)H^2 < 0$ (key `einsteinConditions`; for the classical quadratic case `condensate_einstein_quadratic_U` in both reports).

What $a_4$ the equations allow, in summary: for a prescribed $a_4$ the equations fix the required source ($\rho$, $p_3$, $p_t$, $p_8$ above, with $p_3 + p_t = 2p_8$ and all components independent of $x_8$), and whether a state of dirac16complex supplies it is a separate question; states with $\langle{:}k_1{:}\rangle = \langle{:}k_5{:}\rangle$ allow only the linear member $a_4 = AHx_4 + a_0$ with constant $\rho$ and $p$ (the sign of $A$, and with it deflation or inflation of the extra times, is not selected); a non-linear $a_4$ needs $p_3 \neq p_t$, that is $\langle{:}k_1{:}\rangle \neq \langle{:}k_5{:}\rangle$, together with all the other conditions. The Kohn-Sham states computed in `Revision/kohn_sham/` (key `kohnSham` of the field-equations record) are not such a source: every recorded state with a nonzero energy-momentum tensor depends on $x_8$ and violates $p_3 + p_t = 2p_8$ pointwise and also after integration over $x_8$ (for $N = 136$, $\lambda = 0$ the ratio $(\int p_3 + \int p_t)/(2\int p_8)$ is 0.339767, 0.25969 and 0.239714 at $a_{4,0} = 0$, 1, 2, where the equations require 1), so the author's metric is not a solution with them (`ks_profiles_depend_on_x8`, `ks_profiles_violate_algebraic_condition`, `ks_integrals_violate_algebraic_condition`). The Kohn-Sham history $a_4 = AHx_4$ is a prescribed test-field background without back-reaction: the linear member needs $p_3 = p_t = p_8$ and constant $\rho$, which the Kohn-Sham gas along it does not have (`ks_history_is_a_prescribed_background`).

## 14. Relation to the pairing theorems

The pairing theorems of SPEC section 9 use the Lagrangian, the field equations and the energy-momentum tensor of this document; their full statements, hypotheses and limits are in `Revision/docs/PAIR_CREATION_PROOFS.md`. For dirac16complex, in brief:

- T1 (chirality): $\mathcal{L}_{m,\lambda}[\Gamma\Psi] = -\mathcal{L}_{-m,-\lambda}[\Psi]$, solutions of the $(m, \lambda)$ equations are mapped to solutions of the $(-m, -\lambda)$ equations, $T \to -T$ and $J \to -J$, in every gravitational field; the total energy-momentum and the total current of the pair vanish identically (Wolfram `T1_Lagrangian_primordial_grassmann` and `T1_energy_momentum_primordial_grassmann`, sympy `T1.metric.grassmann.pair_total_emt_zero`).
- T2 (chirality combined with a Pin(4,4) reflection of character $-1$, the mirror $z \to \pi - z$ across the assumed Z2 brane): $(m, \lambda) \to (-m, \lambda)$, $\mathcal{L} \to +\mathcal{L}$, with equal, not opposite, energy-momentum (`T2_mirror_Lagrangian_grassmann`, `T2_mirror_energy_momentum_and_current_grassmann`; sympy `T2.metric.grassmann.emt`).
- Quantum reading: the chirality image $\Gamma\Psi$ carries the Krein metric $-B$; there is no cancellation between two independently quantised universes (`Q_Krein_metric_of_images`, `Q_no_identification_of_independent_universes`; sympy `Q.no_cancellation_independent_universes`).
- T3 (the Kohn-Sham level): the block map of $\Gamma$ with the brane parities exchanged and the tip angle $\theta \to \pi - \theta$ maps every self-consistent instantaneous Kohn-Sham state with $(m, \lambda, \theta)$ onto one with $(-m, +\lambda, \pi - \theta)$, with equal levels, occupations, Kohn-Sham energies and energy-momentum profiles, and $S \to -S$; the Z2 brane is ASSUMED (`T3_energies_and_emt_profiles_equal`, `T3_exact_k0_spectra`; sympy `T3.energies_and_emt_profiles_equal`).

These are correspondences between solutions; no creation process, rate or amplitude follows from them (`not_established` in the sympy pairing report and in the T3 record).

## 15. What this document does not claim

- It derives no creation process, rate or amplitude for universes, and no statement that universes of masses $+m$ and $-m$ are created in pairs; the pairing theorems (section 14) map solutions to solutions.
- Non-triviality [1] is a statement about the Euler-Lagrange equations in the author's metric with $H > 0$; it is not a statement about observable effects of the gravitational term. The value $\gamma^\mu\Omega_\mu = 3H\gamma^{(8)}$ belongs to the diagonal vielbein and to the field variables $\Psi$: it vanishes identically in the frame boosted in the $(x_4, x_8)$ plane with rapidity $6Hx_4 + b_0$, and the rescaling $\Psi = \sin^{-1/2}z\,\chi$ removes it; the canonical connection drops out of $\mathcal{L}$, and the deflation $a_4$ makes no contribution to $\gamma^\mu\Omega_\mu$. What is frame-independent is that $\Omega_\mu$ vanishes in no frame (curvature $R^{x_8}{}_{x_8} = -6H^2$), together with the vielbein factors of the derivative terms (section 7, Remarks). That the term is "not cosmetic" is not claimed; its role for the Hermiticity of the mode operator depends on the measure and the variables (an interpretation).
- The quantisation recorded here is: the canonical anticommutator, the theorem that it forces a Krein structure when $\Psi^\dagger$ is realised as the Hilbert adjoint, the formal Krein self-adjointness of the evolution (up to the boundary term at $z = \pi/2$), and positive Fock realisations checked for single good-sector momenta with frozen coefficients. A positive-norm Hilbert space for the full field, a stable vacuum in the presence of the growing extra-time modes, and the interacting ($\lambda \neq 0$) operator theory are not constructed. In flat 4+4 space every eigenspace of REAL frequency of the one-particle generator has Krein inertia (4,4) (`Q_one_particle_Krein_signatures`, `Q.one_particle_Krein_inertia`, proved for every real frequency in `Q_one_particle_Krein_inertia_real_frequencies` and `Q.one_particle_Krein_inertia_proof`), and every eigenspace of imaginary or zero frequency is Krein-neutral (`Q_one_particle_complex_and_zero_frequencies_Krein_neutral`). In flat space the good-sector restriction removes the complex frequencies, not the indefiniteness of the real-frequency eigenspaces; in the curved good sector without a boundary condition at $z = \pi/2$ complex frequencies remain (section 11).
- Boundary conditions: none is imposed at $z = \pi/2$ in this record. The Hermiticity of the curved good-sector mode operator and the conservation of the Krein form hold up to the boundary term there; with no boundary condition the good sector contains growing $x_8$-independent modes (for $U = 0$ whenever $m^2 < 9H^2$).
- No well-posed Cauchy problem is claimed: the slices $x_4 = $ const are non-characteristic, but for data that depend on the extra times the growth rates are unbounded (Hadamard ill-posedness).
- The normal-ordered operator form of the on-shell trace identity for $\lambda \neq 0$ is an assumption of the field-equations record, not a verified result; no numerical expectation value of the energy-momentum tensor operator is quoted in this document.
- The relative sign $\sigma_T$ between the gravitational and the matter side of the $a_4$ equations is a declared convention ($\sigma_T = +1$), not derived.
- No solution $a_4(x_4)$ with a dirac16complex source is computed here beyond the statements of section 13; it is not claimed that any state of dirac16complex supplies a source that satisfies all the conditions of section 13 (in Einstein gravity such a source must violate the null energy condition along $x_4 + x_8$). The recorded Kohn-Sham states fail the conditions (section 13), and the Kohn-Sham history is a prescribed background without back-reaction; the equations do not select deflation ($A > 0$) over inflation of the extra times.
- The equation of state seen by a 3-space observer, its time dependence and the dark-sector hypotheses are not treated here.
- $H = 0$ is a degenerate limit, not a member of the family; the surface $z = \pi/2$ is degenerate ($g_{88} = 0$, $\sqrt{|g|} = 0$); nothing is claimed there.
- The comparison record of the field-theory branch agrees entirely (section 1); every formula is nevertheless cited by the separate checks of the two engines.

## 16. Reproduction

From the repository root (each verifier writes its outputs to the paths listed in section 1; the Wolfram verifier of each part runs first because the sympy verifier compares with its output at the end):

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
wolframscript -file Revision/pairing/kohn_sham/wolfram/verify_t3.wls
python Revision/pairing/kohn_sham/python/check_t3.py
python Revision/field_equations_a4/python/check_ks_source_conditions.py
```

The sympy field-theory checker exits with an error if its comparison with the Wolfram record does not agree entirely. It can write its report to another path, which leaves the recorded report untouched; it ran in about two minutes in this session (the scope checkers in about 17 s and 1 s, the T3 verifiers in about 3 s and 1 s):

```text
python Revision/theory/python/check_field_theory.py --out <path>
```

This document (md, tex, pdf) is built and verified with the first command below (one command line); with the optional last argument it records the edition dirac16complex-field-theory in `Revision/pdf-specifications.json`. The second command runs the publication test, the third prints the blocks that the test generates:

```text
python scripts/build_provenance_pdf.py Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.md
    --developer-layout --specifications Revision/pdf-specifications.json [--register]
python -m unittest Revision/tests/test_dirac16complex_field_theory_publication.py -v
python Revision/tests/test_dirac16complex_field_theory_publication.py --emit
```

The test checks that the .tex is the builder output of the .md, that the registered PDF is the PDF file next to it, that every cited check exists and passes in the reports, that the quoted check counts are those of the reports, and that the component field equations and the $a_4$ equations above are the output of its renderers applied to `Revision/theory/field-theory.json` and `Revision/field_equations_a4/a4-equations.json`.

## 17. Index of formulas and checks

| formula | section | Wolfram checks | sympy checks |
| --- | --- | --- | --- |
| metric, vielbein, volume element | 2 | `metric_is_the_authors`, `sqrt_det_g_is_cos_z` | `metric_from_vielbein_equals_SPEC`, `sqrt_det_g_equals_cos_z` |
| Christoffel symbols, Ricci tensor, curvature | 2 | `christoffel_count`, `ricci_mixed_components`, `ricci_scalar`, `never_flat_for_H_positive` | `christoffel_symmetric_metric_compatible`, `curvature_nonzero_flat_only_formally` |
| Clifford algebra, C, Gamma, B | 3 | `Clifford_relation`, `C_gamma_real_antisymmetric`, `Gamma_diag`, `B_signature_8_8` | `clifford_relation`, `C_conjugation`, `chirality_diag`, `B_hermitian_involution_signature` |
| Pin(4,4) irreducible; Spin(4,4): two inequivalent 8-dimensional irreducible halves | 3 | `Pin44_irreducible_commutant_dim_1`, `chiral_halves_irreducible`, `chiral_halves_inequivalent_intertwiners_0` | `pin_commutant_dimension_1`, `spin_halves_irreducible`, `spin_halves_inequivalent` |
| canonical spin connection, covariant constancy | 4 | `vielbein_postulate`, `omega_components`, `Omega_components`, `gamma_covariantly_constant` | `vielbein_postulate`, `Omega_x4_and_Omega_x8_vanish`, `covariant_constancy_D_mu_gamma_nu` |
| gravitational term 3H gamma8 (diagonal frame) | 4, 7 | `gammaOmega_equals_3H_gamma_x8`, `gammaOmega_x4_terms_cancel` | `gamma_mu_Omega_mu_equals_3H_gamma_x8`, `time_terms_cancel_hidden_term_survives` |
| frame and variable dependence of the term; frame-independent content | 4, 7 | `boosted_frame_gammaOmega_vanishes`, `boosted_frame_curvature_nonzero`, `rescaling_removes_the_connection_term`, `connection_free_lagrangian_same_equations` | `boosted_frame_gammaOmega_formula`, `rescaled_equation_quadratic_potential`, `gammaOmega_blind_to_the_deflation`, `spin_connection_in_the_energy_momentum_tensor` |
| Lagrangian: reality, total divergence | 5 | `L_real_G`, `L_total_divergence_to_unsymmetrised_G` | `grassmann_lagrangian_real`, `grassmann_total_divergence_relation` |
| Majorana-type negative control | 5 | `Majorana_Lg_total_derivative_grassmann` | `negative_control_majorana_grassmann_total_derivative` |
| Euler-Lagrange equations, explicit form | 6 | `EL_Psibar_G`, `EL_Psi_G`, `Dirac_operator_explicit_G`, `evolution_form_G`, `block_form` | `grassmann_euler_lagrange_psibar_variation`, `grassmann_euler_lagrange_psi_variation` |
| non-triviality [1] | 7 | `nontriviality_1_dirac16complex`, `Omega_vanishes_iff_a4prime_and_H_vanish`, `spin_curvature_equals_Riemann` | `nontriviality_Omega_zero_iff_flat`, `spinor_curvature_equals_riemann` |
| self-consistency | 8 | `adjoint_equation_is_Dirac_conjugate_G`, `Lichnerowicz_identity_G`, `current_conservation_identity_G`, `Noether_identity_diffeomorphisms_G`, `Noether_identity_local_Lorentz_G` | `grassmann_adjoint_equation_is_conjugate`, `lichnerowicz_identity_on_fields`, `grassmann_current_conservation`, `grassmann_emt_conservation_on_shell` |
| energy-momentum tensor | 9 | `T_vielbein_variation_closed_form_G`, `T_symmetric_part_Belinfante_G`, `T_diagonal_components_G`, `T_x4_x8_component_G`, `EMT_trace_G` | `grassmann_emt_equals_general_vielbein_variation_on_shell`, `grassmann_emt_symmetric`, `grassmann_trace_on_shell` |
| energy density, pressures, equations of state | 10 | `kinetic_sum_on_shell_G`, `exact_solution_nonlinear_homogeneous_G`, `energy_exchange_equation` | `grassmann_homogeneous_on_shell_rho_p`, `energy_exchange_equation` |
| canonical quantisation, Krein structure | 11 | `canonical_momentum`, `first_order_form_and_anticommutator`, `no_positive_inner_product`, `Krein_form_conserved_curved`, `good_sector_hermiticity_curved`, `Q_one_particle_Krein_inertia_real_frequencies` | `canonical_anticommutator_B`, `no_positive_inner_product`, `good_sector_spectrum_and_B_sectors`, `Q.one_particle_Krein_inertia_proof`, `Q.one_particle_complex_frequency_Krein_neutral` |
| boundary term at z = pi/2, growing modes, ill-posedness | 8, 11 | `good_sector_hermiticity_up_to_the_brane_flux`, `good_sector_x8_independent_modes_without_boundary_condition` | `extra_time_growth_rates_unbounded` |
| Fock space, normal ordering, expectation values | 11, 12 | `Fock_space_good_sector_example`, `mode_hamiltonian_Krein_selfadjoint` | `good_sector_positive_fock_realisation`, `expectation_value_rule`, `extra_time_modes_grow` |
| field equations for a4 | 13 | `evolution_factorises_a4pp_times_F`, `algebraic_identity_x1_plus_x5_minus_2x8`, `constraint_propagation_bianchi`, `einstein_null_energy_x8`, `linear_member_equal_pressures` | `evolution_factorises`, `algebraic_identity`, `bianchi_x4`, `einstein_null_energy_x8`, `linear_member_equal_pressures` |
| the Kohn-Sham states as a source | 13 | | `ks_profiles_depend_on_x8`, `ks_integrals_violate_algebraic_condition`, `ks_history_is_a_prescribed_background` (Python) |
| pairing (section 14) | 14 | `T1_Lagrangian_primordial_grassmann`, `T2_mirror_Lagrangian_grassmann`, `Q_Krein_metric_of_images`, `T3_energies_and_emt_profiles_equal` | `T1.metric.grassmann.lagrangian`, `T2.metric.grassmann.emt`, `Q.no_cancellation_independent_universes`, `T3.energies_and_emt_profiles_equal` |
