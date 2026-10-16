# dirac16complex in the author's primordial gravitational field

## Lagrangian, covariant field equations, non-triviality [1], energy-momentum tensor operator, equations of state and the field equations for a4[x4] and b4[x4] (Revision record)

## Abstract

This document records, for the fermion field dirac16complex coupled to the author's primordial gravitational field, the Lagrangian, its coupling through the canonical spin connection, the exact covariant field equations (Euler-Lagrange) written out component by component, the non-triviality test [1] with its proof, the self-consistency of the field equations, the energy-momentum tensor (as a Grassmann-algebra expression and as a normal-ordered operator after canonical quantisation in 4 + 4 dimensions, with the Krein structure that this quantisation forces), the kinetic and potential energy, the energy density, the pressures and the equations of state, and the Einstein-Lovelock field equations for a4[x4] and b4[x4] with dirac16complex as the source. The metric is the author's metric of 2026-10-14, in which the three extra-time components carry a second function $b_4(x_4) > 0$; on the user's order of 2026-10-15 every statement is proved for general functions $a_4$ and $b_4$, and $b_4$ is never 1 (the earlier metric with $b_4 = 1$ is withdrawn). Every formula is an output of Revision code (a WolframScript verifier and, for most statements, an independent sympy verifier) and is listed with the names of the checks that verify it. The main exact results are: in the diagonal vielbein the spin-connection term of the field equation is $\gamma^\mu\Omega_\mu = 3H\gamma^{(0)} + \tfrac34(b_4'/b_4)\gamma^{(4)}$ for every $a_4$ and $b_4$ (the $a_4'$ terms of the time direction cancel between the three inflating and the three deflating directions, the $b_4'$ terms of the three extra times add, and so do the hidden-direction terms of all six), with the square $\big(9H^2 - \tfrac{9}{16}(b_4'/b_4)^2\big)I_{16}$; this value belongs to the diagonal frame and to the field variables $\Psi$ (a frame boosted in the $(x_0, x_4)$ plane removes its $H$ part, no such boost removes its $b_4'$ part, and the rescaling $\Psi = b_4^{-3/4}\sin^{-1/2}z\,\chi$ removes all of it), while the frame-independent content of non-triviality [1] is that $\Omega_\mu$ vanishes in no frame (the metric is never flat for $H > 0$) and that the vielbein factors enter every derivative term; when $\Psi^\dagger$ is realised as the Hilbert adjoint, the canonical anticommutator $\{\Psi, \Psi^\dagger\} = B\,\delta^7/\sqrt{|g|}$, $\sqrt{|g|} = b_4^{3/2}\cos z$, with $B$ of signature (8,8) forces an indefinite (Krein) inner product (a positive Fock realisation with $\Psi^\dagger = \chi B$ is constructed and checked only for single good-sector momenta with frozen coefficients, `mode_hamiltonian_good_sector`, `Fock_space_good_sector_example`, `good_sector_positive_fock_realisation`; in the author's metric the curved good-sector mode operator is Hermitian only up to the boundary term at $z = \pi/2$, where this record imposes no boundary condition, and without one the good sector has complex frequencies, for $U = 0$ whenever $m^2 < 9H^2$, `good_sector_hermiticity_up_to_the_brane_flux`, `good_sector_x0_independent_modes_without_boundary_condition`; a positive-norm Hilbert space for the full field is not established); homogeneous on-shell configurations have $\rho = mS + U$ and $p = SU' - U$ in every direction, with $b_4^{3/2}S$ constant along $x_4$; the field equations for $a_4$ and $b_4$ consist of a first-order constraint, two second-order equations that are linear in $a_4''$ and $(b_4'/b_4)'$, the condition that every diagonal source component be independent of $x_0$, and an off-diagonal equation $\kappa\,T^{x_4}{}_{x_0} = \cot z\,(b_4'/b_4)\,Q$: in Einstein gravity $Q = \frac32H$, so a source without $T^{x_4}{}_{x_0}$ forces $b_4$ to be constant, and with the author's Lovelock weights such a source allows, among the histories with $a_4 = Hx_4$ and exponential $b_4$, exactly $b_4 = b_4(0)e^{(4/3)Hx_4}$, the history of `Revision/SPEC.md` section 1, which requires a constant source of negative energy density and is used as a prescribed background. Section 15 states what is not claimed, including the frame dependence of the gravitational term, the boundary terms at the patch end $z = \pi/2$ and the ill-posedness of the Cauchy problem for data that depend on the extra times. From the second wave of the record (2026-10-08, recomputed for the metric with $b_4$): the field equations for $a_4$ and $b_4$ with the Kohn-Sham source (section 13: no recorded Kohn-Sham state is an admissible source, and in a stated approximation the source does not start or select the deflation), the completion of the Kohn-Sham-level pairing T3 (section 14), the operator form of the on-shell identity for $\lambda \neq 0$ in a finite fermionic Fock model of one good-sector mode set with frozen coefficients, where, of the tested operator orderings, it holds exactly only when the potential and the energy-momentum tensor are both Wick ordered (section 12; nothing is proved for the field on a whole slice), the verdict of the dark-sector investigation for dirac16complex (section 15) and pointers to the documents on the Kohn-Sham model, the dark-sector hypotheses and the Lovelock tensors (section 1).

## 1. Scope, sources and status of the record

The binding plan is `Revision/SPEC.md`; the author's task is quoted in `Revision/README.md`. This document belongs to the new record under `Revision/` and uses nothing from the earlier stages of the repository: every statement below is an output of Revision code and is cited by the name of the check that verifies it. Numbers and formulas are taken only from the following files (verdicts as recorded in them when this document was written):

| part | files | checks |
| --- | --- | --- |
| algebra (SPEC section 2) | `Revision/algebra/reports/wolfram-algebra.json`, `Revision/algebra/reports/python-algebra.json` | Wolfram: 45 of 45 checks pass; sympy: 35 of 35 checks pass |
| field theory (SPEC sections 1, 3, 4, 6; the metric with $b_4$) | `Revision/theory/field-theory.json`, `Revision/theory/reports/wolfram-field-theory.json`, `Revision/theory/reports/python-field-theory.json` | Wolfram: 84 of 84 checks pass; sympy: 72 of 72 checks pass |
| field equations for $a_4$ and $b_4$ (SPEC section 5) | `Revision/field_equations_a4/a4-equations.json`, `Revision/field_equations_a4/reports/wolfram-a4-report.json`, `Revision/field_equations_a4/reports/python-a4-report.json` | Wolfram: 59 of 59 checks pass; sympy: 65 of 65 checks pass |
| pairing (SPEC section 9) | `Revision/pairing/pairing-theory.json`, `Revision/pairing/reports/wolfram-pairing.json`, `Revision/pairing/reports/python-pairing.json` | Wolfram: 102 of 102 checks pass; sympy: 67 of 67 checks pass |
| scope of the statements (frame dependence, boundary terms, growth, sign of the energy) | `Revision/theory/reports/wolfram-scope.json`, `Revision/theory/reports/python-scope.json` | Wolfram: 15 of 15 checks pass; sympy: 14 of 14 checks pass |
| Kohn-Sham pairing T3 (SPEC section 9) | `Revision/pairing/kohn_sham/t3-theory.json`, `Revision/pairing/kohn_sham/reports/wolfram-t3.json`, `Revision/pairing/kohn_sham/reports/python-t3.json` | Wolfram: 10 of 10 checks pass; sympy: 13 of 13 checks pass |
| the Kohn-Sham states as a source of the $a_4$ and $b_4$ equations | `Revision/field_equations_a4/reports/ks-source-conditions.json` | Python: 6 of 6 checks pass |
| the $a_4$ and $b_4$ equations with the Kohn-Sham source | `Revision/field_equations_a4/ks_source/reports/ks-source-a4.json` | Python: 22 of 22 checks pass |
| completion of T3 (2026-10-08) | `Revision/pairing/kohn_sham/t3-completion.json`, `Revision/pairing/kohn_sham/reports/wolfram-t3-completion.json`, `Revision/pairing/kohn_sham/reports/python-t3-completion.json` | Wolfram: 3 of 3 checks pass; sympy: 7 of 7 checks pass |
| the energy-momentum tensor operator for $\lambda \neq 0$ in a finite Fock model (SPEC sections 4, 6; 2026-10-08) | `Revision/theory/fock_quartic/reports/fock-quartic.json` | Python (sympy and its own exact engine for the anticommutation relations; no Wolfram counterpart): 21 of 21 checks pass |
| dark sector, Hypothesis (SPEC section 8) | `Revision/dark_sector/dirac16complex/reports/derivation-checks.json`, `Revision/dark_sector/dirac16complex/reports/ks-history-run.json`, `Revision/dark_sector/dirac16complex/reports/eos-checks.json`, `Revision/dark_sector/dirac16complex/reports/independent-checks.json` | derivation: 39 of 39 checks pass; Kohn-Sham history: 8 of 8 checks pass; equation of state: 15 of 15 checks pass; independent: 10 of 10 checks pass |

The parts with a Wolfram and a sympy count have two verifiers that share no code: a WolframScript verifier (exact symbolic arithmetic) and a sympy verifier (an independent re-derivation; the gamma matrices are rebuilt from the author's formulas on both sides and compared entry by entry). Where only one engine verifies a statement, only that engine's check is cited. A check is cited in typewriter type, for example `nontriviality_1_dirac16complex` (Wolfram) or `gamma_mu_Omega_mu_equals_3H_gamma_x0_plus_b4_term` (sympy); in the field-theory reports the Wolfram names end in `_G` for dirac16complex (explicit Grassmann algebra) and the sympy names begin with `grassmann_`. The proofs are exact identities in the stated generality (symbolic $H$, two general functions $a_4(x_4)$ and $b_4(x_4) > 0$, $m$, $\lambda$, and a general field configuration on its jet space); exact numerical examples are labelled as examples. The supplements of 2026-10-14 (`Revision/theory/field-theory-b4.json` with its reports), which re-checked part of the theory for general $b_4$ before the whole field-theory record was moved to the metric with $b_4$ on 2026-10-15, are superseded by the record above and are not cited.

**Related Revision documents.** The Kohn-Sham model of dirac16complex in the deflating field (SPEC section 7: the reduction to $2 \times 2$ blocks in the hidden coordinate, the instantaneous ground and first excited states along the prescribed history $a_4 = Hx_4$, $b_4 = b_4(0)e^{(4/3)Hx_4}$, Mermin thermodynamics, and the full cross-check of the Rust solver against the independent reference, `Revision/kohn_sham/reports/ks-crosscheck.json`: 31 of 31 checks pass) is described in `Revision/docs/KOHN_SHAM_DEFLATING_FIELD`. The generalized Kronecker delta and the Lovelock tensors $P_{(1)}$, $P_{(2)}$, $P_{(3)}$ behind the field equations for $a_4$ and $b_4$ of section 13 are described in `Revision/docs/LOVELOCK_GKD`. The dark-sector hypotheses of SPEC section 8 are investigated in `Revision/docs/DARK_SECTOR_HYPOTHESES` (its verdict for dirac16complex is summarised in section 15). The pairing theorems, with the completion of T3, are in `Revision/docs/PAIR_CREATION_PROOFS`.

**Status of the comparison record of the field-theory branch.** The sympy report contains a comparison with the current Wolfram side (`comparison_with_wolfram`): 33 of 33 formula records and 65 of 65 check pairs agree, against a Wolfram run of 84 checks. Every formula record of `Revision/theory/field-theory.json` is compared (the record `energy_exchange`, three Wolfram expressions, component by component against the divergence recomputed from the sympy Christoffel symbols; the prose records `nontriviality`, `majorana_negative_control`, `exact_solutions`, `equation_of_state_definitions`, `hidden_direction_hermiticity` and `quantisation` by re-deriving their formulas in sympy), and every one of the 84 Wolfram checks is paired with a sympy check (the list `wolfram_checks_without_sympy_counterpart` of the comparison is empty; the Grassmann and the commuting form of the nonlinear homogeneous solution, `exact_solution_nonlinear_homogeneous_G` and `exact_solution_nonlinear_homogeneous_C`, are both paired with `exact_nonlinear_homogeneous_solution`, which checks both statistics). The sympy verifier exits with an error unless the comparison agrees entirely, so a stale comparison cannot pass unnoticed. This document still cites each formula by the checks of each engine separately.

Conventions (SPEC sections 1 and 2): the author's coordinates $x_0, x_1, \dots, x_7$, in the author's order; $x_0$ is the hidden space direction, $x_1, x_2, x_3$ are ordinary 3-space, $x_4$ is the time, $x_5, x_6, x_7$ are the three extra times (time-like, deflating exponentially); $z = 6Hx_0 \in (0, \pi/2)$, $H > 0$ (until 2026-10-14 this record named the coordinates $x_1, \dots, x_8$, with the hidden direction $x_8$ listed last); $a_4 = a_4(x_4)$ and $b_4 = b_4(x_4) > 0$, $a_4' = da_4/dx_4$, $b_4' = db_4/dx_4$, and throughout

$$
u = \frac{b_4'}{b_4},\qquad v = u' = \frac{b_4''}{b_4} - u^2 ;
$$

$\partial_a = \partial/\partial x_a$. Frame indices are aligned with the coordinates and written in parentheses: $\gamma^{(a)}$ is the frame gamma matrix of direction $x_a$. Throughout, $i \in \{1, 2, 3\}$ labels the 3-space directions and $t \in \{5, 6, 7\}$ the extra times.

## 2. The primordial gravitational field

The author's metric (SPEC section 1, changed by the user on 2026-10-14), with signature (4,4) (space-like $x_0, x_1, x_2, x_3$; time-like $x_4, \dots, x_7$):

$$
\begin{aligned}
ds^2 &= \cot^2 z\,dx_0^2 + e^{2a_4}\sin^{1/3}z\,(dx_1^2 + dx_2^2 + dx_3^2) - dx_4^2 \\
&\quad - e^{-2a_4}\,b_4\sin^{1/3}z\,(dx_5^2 + dx_6^2 + dx_7^2), \qquad z = 6Hx_0 \in (0, \pi/2),
\end{aligned}
$$

with two functions of the time, $a_4(x_4)$ and $b_4(x_4) > 0$ (`metric_is_the_authors`; sympy `metric_from_vielbein_equals_SPEC`). The function $b_4$ was introduced by the user on 2026-10-14 (record `Revision/metric_b4/METRIC_CHANGE_PROVENANCE.md`); on the user's orders of 2026-10-15 ("b4 is a function of x4; b4 is NEVER 1"; "move everything to b4(x4); b4 is never 1") every statement of this document holds for general $a_4$ and $b_4$, and $b_4$ is never 1. The earlier metric with $b_4 = 1$ is withdrawn; a constant $b_4$ is a rescaling of $x_5, x_6, x_7$ and is excluded as well. Where a statement needs a history, it is the background history of SPEC section 1, $a_4 = Hx_4$, $b_4 = b_4(0)e^{(4/3)Hx_4}$ (section 13).

The scale factor of 3-space is $e^{a_4}\sin^{1/6}z$ (inflating as $a_4$ increases), that of the extra times $e^{-a_4}b_4^{1/2}\sin^{1/6}z$ (deflating at the rate $a_4' - \tfrac12u$; on the background history it is proportional to $e^{-a_4/3}$, an exponential deflation). The diagonal vielbein $e^a{}_\mu = f_a\,\delta^a_\mu$ with frame metric $\eta_{ab} = \mathrm{diag}(+1, +1, +1, +1, -1, -1, -1, -1)$ (in the order $x_0, \dots, x_7$) has

$$
f_0 = \cot z,\quad f_1 = f_2 = f_3 = e^{a_4}\sin^{1/6}z,\quad f_4 = 1,\quad f_5 = f_6 = f_7 = e^{-a_4}b_4^{1/2}\sin^{1/6}z
$$

and reproduces the metric entry by entry (`metric_is_the_authors`, `vielbein_inverse`; sympy `metric_from_vielbein_equals_SPEC`). The volume element is

$$
\sqrt{|g|} = f_0 f_1\cdots f_7 = b_4^{3/2}\sin z\cot z = b_4^{3/2}\cos z ,
$$

so $\partial_4\sqrt{|g|} = \tfrac32u\sqrt{|g|}$: the inflation $e^{3a_4}$ of 3-space and the factor $e^{-3a_4}$ of the extra times compensate, and the volume depends on $x_4$ through $b_4$ alone (`sqrt_det_g`, `sqrt_det_g_equals_b4_cos_z`). $H = 0$ is not a member of the family but a degenerate limit ($g_{11} \to 0$, $g_{55} \to 0$, $g_{00} \to \infty$ at fixed $x_0$; `degenerate_at_H_0`); every statement below assumes $H > 0$ and $0 < z < \pi/2$.

The Levi-Civita connection has 25 independent nonzero symbols (`christoffel_count`, `christoffel_symmetric_metric_compatible`; formula key `christoffel_nonzero`):

$$
\begin{aligned}
\Gamma^{x_i}{}_{x_i x_4} &= a_4', & \Gamma^{x_i}{}_{x_i x_0} &= H\cot z, \\
\Gamma^{x_t}{}_{x_4 x_t} &= -\big(a_4' - \tfrac12u\big), & \Gamma^{x_t}{}_{x_t x_0} &= H\cot z, \\
\Gamma^{x_4}{}_{x_i x_i} &= e^{2a_4}\sin^{1/3}z\,a_4', & \Gamma^{x_4}{}_{x_t x_t} &= e^{-2a_4}b_4\sin^{1/3}z\,\big(a_4' - \tfrac12u\big), \\
\Gamma^{x_0}{}_{x_i x_i} &= -e^{2a_4}H\,\frac{\sin^{4/3}z}{\cos z}, & \Gamma^{x_0}{}_{x_t x_t} &= e^{-2a_4}b_4H\,\frac{\sin^{4/3}z}{\cos z}, \\
\Gamma^{x_0}{}_{x_0 x_0} &= -\frac{6H}{\sin z\cos z}.
\end{aligned}
$$

The mixed Ricci tensor is diagonal except for the pair $x_4$-$x_0$, which is proportional to $b_4'$ (`ricci_mixed_components`, `ricci_scalar`, `curvature_nonzero_flat_only_formally`; formula key `ricci_mixed_nonzero`):

$$
\begin{aligned}
R^{x_0}{}_{x_0} &= -6H^2, & R^{x_i}{}_{x_i} &= a_4'' - 6H^2 + \tfrac32a_4'u, \\
R^{x_4}{}_{x_4} &= 6(a_4')^2 - 3a_4'u + \tfrac34u^2 + \tfrac32v, & R^{x_t}{}_{x_t} &= -a_4'' - 6H^2 - \tfrac32a_4'u + \tfrac34u^2 + \tfrac12v, \\
R^{x_4}{}_{x_0} &= \tfrac32Hu\cot z, & R^{x_0}{}_{x_4} &= -\tfrac32Hu\tan z,
\end{aligned}
$$

$$
R = 6(a_4')^2 - 3a_4'u + 3u^2 + 3v - 42H^2 .
$$

These equal the independent record of the metric change, `Revision/metric_b4/results/metric-b4.json`, which was compared there with the author's stored outputs of `Dirac_Einstein-Lovelock_4+4_Nash.nb` (`ricci_mixed_components`). Since $R^{x_0}{}_{x_0} = -6H^2 < 0$ for every $H > 0$ and all functions $a_4$, $b_4$, the metric is never flat for $H > 0$ (`never_flat_for_H_positive`).

## 3. The field dirac16complex: Clifford algebra, Pin(4,4) and Spin(4,4)

dirac16complex is a field $\Psi$ with 16 complex anticommuting components $\Psi_A(x)$, $A = 1, \dots, 16$ (elements of a Grassmann algebra; after quantisation, operators with canonical anticommutators, section 11). It transforms under a 16-dimensional irreducible representation of Pin(4,4), the double cover of O(4,4); for the transformations of determinant 1 it transforms under the direct sum of two inequivalent irreducible 8-dimensional representations of Spin(4,4), the double cover of SO(4,4). These representation facts are proved exactly below for the author's gamma matrices.

The gamma matrices are the author's real $16\times16$ matrices T16, rebuilt by Revision code from the author's formulas (the tau matrices of the notebook) in WolframScript and, independently, in Python, in the notebook's frame order, which is the order of the author's coordinates (SPEC section 2): $\gamma^{(a)} = $ T16[a] for $a = 0, \dots, 7$ ($\gamma^{(0)}$ of the hidden direction, $\gamma^{(4)}$ of the time) (`T16_block_form`, `coordinate_map`; the two constructions agree entry by entry, `fixture_comparison_gammas_json`). Exact properties:

- Clifford relation $\{\gamma^{(a)}, \gamma^{(b)}\} = 2\eta^{ab}\,I_{16}$ for all 64 pairs; the squares are $+1$ for $x_0, x_1, x_2, x_3$ and $-1$ for $x_4, \dots, x_7$ (`Clifford_relation`, `clifford_relation`, `clifford_relation_sympy`). Every $\gamma^{(a)}$ is a real signed permutation matrix, symmetric for the space-like and antisymmetric for the time-like directions, $(\gamma^{(a)})^T = \eta_{aa}\gamma^{(a)}$ (`reality`, `signed_permutation_matrices`, `symmetry_pattern`).
- $C = \gamma^{(0)}\gamma^{(1)}\gamma^{(2)}\gamma^{(3)}$ (the notebook's sigma16) is real symmetric with $C^2 = 1$, and every $C\gamma^{(a)}$ is real antisymmetric, equivalently $C\gamma^{(a)}C^{-1} = -(\gamma^{(a)})^T$ (`C_real_symmetric`, `C_squared_identity`, `C_gamma_real_antisymmetric`; sympy `C_conjugation`). The Dirac adjoint is $\bar\Psi = \Psi^\dagger C$ and $S = \bar\Psi\Psi$.
- The chirality $\Gamma = \gamma^{(0)}\gamma^{(1)}\cdots\gamma^{(7)} = \mathrm{diag}(-I_8, I_8)$ anticommutes with every $\gamma^{(a)}$, $\Gamma^2 = 1$, $[\Gamma, C] = 0$ (`Gamma_definition`, `Gamma_diag`, `Gamma_anticommutes_with_gammas`, `Gamma_commutes_with_C`; sympy `chirality_diag`).
- $B = -iC\gamma^{(4)}$ is Hermitian with $B^2 = 1$ and eigenvalues $+1$ and $-1$, eight each: signature (8,8) (`B_definition`, `B_Hermitian`, `B_squared_identity`, `B_signature_8_8`; sympy `B_hermitian_involution_signature`). $B$ commutes with $\gamma^{(0)}, \gamma^{(1)}, \gamma^{(2)}, \gamma^{(3)}, \gamma^{(4)}$ and anticommutes with $\gamma^{(5)}, \gamma^{(6)}, \gamma^{(7)}$ (`B_gamma_relations`).
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
\omega_{x_i\,(i)(4)} &= a_4'\,e^{a_4}\sin^{1/6}z, & \omega_{x_i\,(i)(0)} &= H\,e^{a_4}\sin^{1/6}z, \\
\omega_{x_t\,(4)(t)} &= -\big(a_4' - \tfrac12u\big)\,e^{-a_4}b_4^{1/2}\sin^{1/6}z, & \omega_{x_t\,(t)(0)} &= -H\,e^{-a_4}b_4^{1/2}\sin^{1/6}z,
\end{aligned}
$$

and $\omega_{x_0} = \omega_{x_4} = 0$; the time-direction rate of the extra times is $a_4' - \tfrac12u = -\frac{d}{dx_4}\ln\big(e^{-a_4}b_4^{1/2}\big)$. The spinor connection is real (sympy `spinor_connection_real`) and reads (`Omega_components`; sympy `Omega_x0_and_Omega_x4_vanish`)

$$
\begin{aligned}
\Omega_{x_i} &= \tfrac12\,e^{a_4}\sin^{1/6}z\,\big(a_4'\,\gamma^{(i)}\gamma^{(4)} + H\,\gamma^{(i)}\gamma^{(0)}\big) \qquad (i = 1, 2, 3), \\
\Omega_{x_t} &= -\tfrac12\,e^{-a_4}b_4^{1/2}\sin^{1/6}z\,\big(\big(a_4' - \tfrac12u\big)\,\gamma^{(4)}\gamma^{(t)} + H\,\gamma^{(t)}\gamma^{(0)}\big) \qquad (t = 5, 6, 7), \\
\Omega_{x_0} &= \Omega_{x_4} = 0.
\end{aligned}
$$

It makes the gammas covariantly constant, $D_\mu\gamma^\nu = \partial_\mu\gamma^\nu + \Gamma^\nu{}_{\mu\lambda}\gamma^\lambda + [\Omega_\mu, \gamma^\nu] = 0$ for all 64 pairs (`gamma_covariantly_constant`, `covariant_constancy_D_mu_gamma_nu`), and its curvature is the Riemann tensor, $[D_\mu, D_\nu]\Psi = \frac12 R_{ab\mu\nu}S^{ab}\Psi$ (`spin_curvature_equals_Riemann`, `spinor_curvature_equals_riemann`).

The contraction that enters the field equation, per direction (no sum; `gammaOmega_per_direction`, formula key of the same name):

$$
\begin{aligned}
\gamma^{x_i}\Omega_{x_i} &= \tfrac12 a_4'\,\gamma^{(4)} + \tfrac12 H\,\gamma^{(0)} \qquad (i = 1, 2, 3), \\
\gamma^{x_t}\Omega_{x_t} &= \big(-\tfrac12 a_4' + \tfrac14u\big)\,\gamma^{(4)} + \tfrac12 H\,\gamma^{(0)} \qquad (t = 5, 6, 7), \\
\gamma^{x_0}\Omega_{x_0} &= \gamma^{x_4}\Omega_{x_4} = 0,
\end{aligned}
$$

and summed:

$$
\gamma^\mu\Omega_\mu = 3H\gamma^{(0)} + \tfrac34u\,\gamma^{(4)} = \frac{1}{2\sqrt{|g|}}\,\partial_\mu\big(\sqrt{|g|}\,\gamma^\mu\big)
$$

(`gammaOmega_total`, `gammaOmega_divergence_form`): the $a_4'$ terms of the three inflating and the three deflating directions cancel, the $b_4'$ terms of the three extra times add to $\tfrac34u$, and the hidden-direction terms of all six directions add to $3H$; the result contains neither $a_4$ nor $x_0$. In the divergence form the $x_0$ part is $\frac{1}{2\sqrt{|g|}}\partial_0\big(b_4^{3/2}\sin z\big)\gamma^{(0)} = 3H\gamma^{(0)}$ and the $x_4$ part is $\frac{1}{2\sqrt{|g|}}\big(\partial_4\sqrt{|g|}\big)\gamma^{(4)} = \tfrac34u\,\gamma^{(4)}$. The sympy verifier confirms each of these statements independently (`gamma_mu_Omega_mu_equals_3H_gamma_x0_plus_b4_term`, `a4_time_terms_cancel_b4_terms_add` and `divergence_of_sqrtg_gamma`). The field-equations branch verifies the same value again, in a Clifford representation of its own and with T16 (`ownrep_gravity_term`, `authorT16_gravity_term`; Wolfram `gravity_term_gamma_mu_Omega_mu`). Since $\gamma^{(0)}$ and $\gamma^{(4)}$ anticommute, with squares $+1$ and $-1$,

$$
\big(\gamma^\mu\Omega_\mu\big)^2 = \big(9H^2 - \tfrac{9}{16}u^2\big)\,I_{16}
$$

(`gravity_term_square`; on the background history $u = \tfrac43H$ and the square is $8H^2I_{16}$). For each direction separately $\{\gamma^\mu, \Omega_\mu\} = 0$ (no sum), because $\Omega_\mu$ contains only generators $S^{(\mu)b}$ (`gamma_mu_anticommutes_with_Omega_mu_no_sum`, `anticommutator_gamma_Omega_vanishes`).

**The value of $\gamma^\mu\Omega_\mu$ belongs to the diagonal vielbein.** The canonical spin connection depends on the choice of the local frame, and so does the contraction $\gamma^\mu\Omega_\mu$. Boost the frame in the $(x_0, x_4)$ plane, $e'^{(4)} = \cosh b\,e^{(4)} + \sinh b\,e^{(0)}$, $e'^{(0)} = \sinh b\,e^{(4)} + \cosh b\,e^{(0)}$, the other $e'^{(a)} = e^{(a)}$, with rapidity $b = c\,x_4 + b_0$: the frame reproduces the author's metric, its canonical connection satisfies the vielbein postulate, and exactly, for every $a_4$, $b_4$ and $H$,

$$
\gamma'^\mu\Omega'_\mu = \frac{6H - c}{2}\,\big(\cosh b\,\gamma^{(0)} - \sinh b\,\gamma^{(4)}\big) + \tfrac34u\,\big(\cosh b\,\gamma^{(4)} - \sinh b\,\gamma^{(0)}\big),
$$

which is $3H\gamma^{(0)} + \tfrac34u\,\gamma^{(4)}$ for the unboosted frame. Both engines verify the frame and its connection (`boosted_frame_reproduces_metric` and `boosted_frame_canonical_connection`) and the contraction (`boosted_frame_gammaOmega_formula`). For $c = 6H$ the $H$ part vanishes identically and $\gamma'^\mu\Omega'_\mu = \tfrac34u\,\big(\cosh b\,\gamma^{(4)} - \sinh b\,\gamma^{(0)}\big)$; for every rapidity function $b(x_4)$ the coefficients $c_0$, $c_4$ of $\gamma'^\mu\Omega'_\mu = c_0\gamma^{(0)} + c_4\gamma^{(4)}$ satisfy $\cosh b\,c_4 + \sinh b\,c_0 = \tfrac34u$, so no boost in this plane removes the term unless $b_4' = 0$ (`boosted_frame_removes_only_the_H_term`). In the boosted frame $\Omega'_\mu$ is nonzero and its curvature is nonzero (`boosted_frame_curvature_nonzero`): what no frame removes is $\Omega_\mu$ itself, whose curvature is the Riemann tensor.

## 5. The Lagrangian

The Lagrangian density (SPEC section 3), with an explicit mass term linear in $m$ and quadratic in the spinor:

$$
\begin{aligned}
\mathcal{L} &= \sqrt{|g|}\,\Big[\tfrac12\big(\bar\Psi\gamma^\mu D_\mu\Psi - (D_\mu\bar\Psi)\gamma^\mu\Psi\big) - m\,\bar\Psi\Psi - U(\bar\Psi\Psi)\Big], \qquad \sqrt{|g|} = b_4^{3/2}\cos z, \\
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
\mathcal{L} = b_4^{3/2}\cos z\,\Big[\tfrac12\sum_{a=0}^{7}\frac{1}{f_a}\big(\bar\Psi\gamma^{(a)}\partial_a\Psi - \partial_a\bar\Psi\gamma^{(a)}\Psi\big) - mS - U(S)\Big].
$$

  It reaches the field equations only through this identity: varying the symmetrised kinetic term produces $\partial_\mu(\sqrt{|g|}\gamma^\mu) = 2\sqrt{|g|}\,\gamma^\mu\Omega_\mu$ (section 7). Hence the Euler-Lagrange equations of $\mathcal{L}$ are those of the connection-free symmetric Lagrangian (the display above), and the term $3H\gamma^{(0)} + \tfrac34u\,\gamma^{(4)}$ is its half-density (volume and vielbein divergence) term (`connection_free_lagrangian_same_equations`, both engines).
- $S$ is an even element of the Grassmann algebra and $U$ is a polynomial in $S$; in the two-generator test algebra $S^3 = 0$, so $U = u_1 S + \frac{\lambda}{2}S^2$ is the most general potential there (`grassmann_algebra_structure`; the constant $u_1$ of this potential is not the rate $u = b_4'/b_4$).

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
&\quad + e^{a_4}b_4^{-1/2}\sin^{-1/6}z\,\big(\gamma^{(5)}\partial_5 + \gamma^{(6)}\partial_6 + \gamma^{(7)}\partial_7\big)\Psi \\
&\quad + \tan z\,\gamma^{(0)}\partial_0\Psi + 3H\gamma^{(0)}\Psi + \tfrac34u\,\gamma^{(4)}\Psi = \big(m + U'(S)\big)\Psi,
\end{aligned}
$$

and the adjoint equation (formula key `adjoint_equation`):

$$
\begin{aligned}
&e^{-a_4}\sin^{-1/6}z\,\big(\partial_1\bar\Psi\gamma^{(1)} + \partial_2\bar\Psi\gamma^{(2)} + \partial_3\bar\Psi\gamma^{(3)}\big) + \partial_4\bar\Psi\gamma^{(4)} \\
&\quad + e^{a_4}b_4^{-1/2}\sin^{-1/6}z\,\big(\partial_5\bar\Psi\gamma^{(5)} + \partial_6\bar\Psi\gamma^{(6)} + \partial_7\bar\Psi\gamma^{(7)}\big) \\
&\quad + \tan z\,\partial_0\bar\Psi\gamma^{(0)} + 3H\bar\Psi\gamma^{(0)} + \tfrac34u\,\bar\Psi\gamma^{(4)} = -\big(m + U'(S)\big)\bar\Psi.
\end{aligned}
$$

Since $(\gamma^{(4)})^2 = -1$, the field equation is equivalent to the first-order evolution equation (`evolution_form_G`; formula key `evolution_form`)

$$
\partial_4\Psi = -\gamma^{(4)}\Big[\big(m + U'(S)\big)\Psi - \sum_{a \neq 4}\frac{1}{f_a}\gamma^{(a)}\partial_a\Psi - 3H\gamma^{(0)}\Psi\Big] - \tfrac34u\,\Psi,
$$

so the slices $x_4 = $ const are non-characteristic ($g^{44} = -1$); the last term is the factor $b_4^{-3/4}$ of the solutions (section 8). In the chiral split $\Psi = (\psi_-, \psi_+)$ (rows 1 to 8 with $\Gamma = -1$, rows 9 to 16 with $\Gamma = +1$) every gamma is block off-diagonal, $\gamma^{(a)} = \begin{pmatrix} 0 & \bar\tau_a \\ \tau_a & 0\end{pmatrix}$ with $\bar\tau_0 = \tau_0 = I_8$, and the field equation is the pair (`block_form`; formula key `field_equation_blocks`)

$$
\begin{aligned}
&\sum_{a}\frac{1}{f_a}\bar\tau_a\partial_a\psi_+ + 3H\psi_+ + \tfrac34u\,\bar\tau_4\psi_+ = V\psi_-,\\
&\sum_{a}\frac{1}{f_a}\tau_a\partial_a\psi_- + 3H\psi_- + \tfrac34u\,\tau_4\psi_- = V\psi_+,\qquad V = m + U'(S).
\end{aligned}
$$

The 16 component equations, $(\gamma^\mu D_\mu\Psi)_A = V\Psi_A$ with $\psi_A = \Psi_A$ the components in the basis of the fixture gammas, $\epsilon_s = e^{-a_4}\sin^{-1/6}z = 1/f_{1}$, $\epsilon_t = e^{a_4}b_4^{-1/2}\sin^{-1/6}z = 1/f_{5}$ and $\hat\partial_4 = \partial_4 + \tfrac34u$ (the $b_4$ term of the spin connection enters every component with the matrix $\gamma^{(4)}$, that is on the same component and with the same sign as $\partial_4$; formula key `field_equation_components`; `Dirac_operator_explicit_G`, `EL_Psibar_G`; the publication test of this document re-derives them from the formula file and compares them with the independent sympy expressions `dirac_equation_components` of the sympy report): the eight equations of the $\Gamma = -1$ rows,

$$
\begin{aligned}
\epsilon_s(-\partial_1\psi_{16} + \partial_2\psi_{15} - \partial_3\psi_{14}) - \hat\partial_4\psi_{14} + \epsilon_t(\partial_5\psi_{15} + \partial_6\psi_{16} + \partial_7\psi_{9}) + (\tan z\,\partial_0 + 3H)\psi_{9} &= V\psi_{1} \\
\epsilon_s(-\partial_1\psi_{15} - \partial_2\psi_{16} + \partial_3\psi_{13}) + \hat\partial_4\psi_{13} + \epsilon_t(\partial_5\psi_{16} - \partial_6\psi_{15} + \partial_7\psi_{10}) + (\tan z\,\partial_0 + 3H)\psi_{10} &= V\psi_{2} \\
\epsilon_s(\partial_1\psi_{14} - \partial_2\psi_{13} - \partial_3\psi_{16}) + \hat\partial_4\psi_{16} + \epsilon_t(-\partial_5\psi_{13} + \partial_6\psi_{14} + \partial_7\psi_{11}) + (\tan z\,\partial_0 + 3H)\psi_{11} &= V\psi_{3} \\
\epsilon_s(\partial_1\psi_{13} + \partial_2\psi_{14} + \partial_3\psi_{15}) - \hat\partial_4\psi_{15} + \epsilon_t(-\partial_5\psi_{14} - \partial_6\psi_{13} + \partial_7\psi_{12}) + (\tan z\,\partial_0 + 3H)\psi_{12} &= V\psi_{4} \\
\epsilon_s(-\partial_1\psi_{12} + \partial_2\psi_{11} - \partial_3\psi_{10}) + \hat\partial_4\psi_{10} + \epsilon_t(-\partial_5\psi_{11} - \partial_6\psi_{12} - \partial_7\psi_{13}) + (\tan z\,\partial_0 + 3H)\psi_{13} &= V\psi_{5} \\
\epsilon_s(-\partial_1\psi_{11} - \partial_2\psi_{12} + \partial_3\psi_{9}) - \hat\partial_4\psi_{9} + \epsilon_t(-\partial_5\psi_{12} + \partial_6\psi_{11} - \partial_7\psi_{14}) + (\tan z\,\partial_0 + 3H)\psi_{14} &= V\psi_{6} \\
\epsilon_s(\partial_1\psi_{10} - \partial_2\psi_{9} - \partial_3\psi_{12}) - \hat\partial_4\psi_{12} + \epsilon_t(\partial_5\psi_{9} - \partial_6\psi_{10} - \partial_7\psi_{15}) + (\tan z\,\partial_0 + 3H)\psi_{15} &= V\psi_{7} \\
\epsilon_s(\partial_1\psi_{9} + \partial_2\psi_{10} + \partial_3\psi_{11}) + \hat\partial_4\psi_{11} + \epsilon_t(\partial_5\psi_{10} + \partial_6\psi_{9} - \partial_7\psi_{16}) + (\tan z\,\partial_0 + 3H)\psi_{16} &= V\psi_{8}
\end{aligned}
$$

and the eight equations of the $\Gamma = +1$ rows,

$$
\begin{aligned}
\epsilon_s(\partial_1\psi_{8} - \partial_2\psi_{7} + \partial_3\psi_{6}) + \hat\partial_4\psi_{6} + \epsilon_t(-\partial_5\psi_{7} - \partial_6\psi_{8} - \partial_7\psi_{1}) + (\tan z\,\partial_0 + 3H)\psi_{1} &= V\psi_{9} \\
\epsilon_s(\partial_1\psi_{7} + \partial_2\psi_{8} - \partial_3\psi_{5}) - \hat\partial_4\psi_{5} + \epsilon_t(-\partial_5\psi_{8} + \partial_6\psi_{7} - \partial_7\psi_{2}) + (\tan z\,\partial_0 + 3H)\psi_{2} &= V\psi_{10} \\
\epsilon_s(-\partial_1\psi_{6} + \partial_2\psi_{5} + \partial_3\psi_{8}) - \hat\partial_4\psi_{8} + \epsilon_t(\partial_5\psi_{5} - \partial_6\psi_{6} - \partial_7\psi_{3}) + (\tan z\,\partial_0 + 3H)\psi_{3} &= V\psi_{11} \\
\epsilon_s(-\partial_1\psi_{5} - \partial_2\psi_{6} - \partial_3\psi_{7}) + \hat\partial_4\psi_{7} + \epsilon_t(\partial_5\psi_{6} + \partial_6\psi_{5} - \partial_7\psi_{4}) + (\tan z\,\partial_0 + 3H)\psi_{4} &= V\psi_{12} \\
\epsilon_s(\partial_1\psi_{4} - \partial_2\psi_{3} + \partial_3\psi_{2}) - \hat\partial_4\psi_{2} + \epsilon_t(\partial_5\psi_{3} + \partial_6\psi_{4} + \partial_7\psi_{5}) + (\tan z\,\partial_0 + 3H)\psi_{5} &= V\psi_{13} \\
\epsilon_s(\partial_1\psi_{3} + \partial_2\psi_{4} - \partial_3\psi_{1}) + \hat\partial_4\psi_{1} + \epsilon_t(\partial_5\psi_{4} - \partial_6\psi_{3} + \partial_7\psi_{6}) + (\tan z\,\partial_0 + 3H)\psi_{6} &= V\psi_{14} \\
\epsilon_s(-\partial_1\psi_{2} + \partial_2\psi_{1} + \partial_3\psi_{4}) + \hat\partial_4\psi_{4} + \epsilon_t(-\partial_5\psi_{1} + \partial_6\psi_{2} + \partial_7\psi_{7}) + (\tan z\,\partial_0 + 3H)\psi_{7} &= V\psi_{15} \\
\epsilon_s(-\partial_1\psi_{1} - \partial_2\psi_{2} - \partial_3\psi_{3}) - \hat\partial_4\psi_{3} + \epsilon_t(-\partial_5\psi_{2} - \partial_6\psi_{1} + \partial_7\psi_{8}) + (\tan z\,\partial_0 + 3H)\psi_{8} &= V\psi_{16}
\end{aligned}
$$

For the quadratic potential $V = m + \lambda S$ with $S = \Psi^\dagger C\Psi$, an even (bilinear) element; the equations hold in the Grassmann algebra, and after quantisation as operator equations (section 11).

## 7. Non-triviality [1]

**Theorem 1 (non-triviality [1]).** Hypotheses: the metric of section 2 with $H > 0$ and $0 < z < \pi/2$; $a_4$ and $b_4 > 0$ any twice differentiable functions of $x_4$ (constant ones included); real $m$ and $\lambda$ (or any real potential $U$); the canonical spin connection of the diagonal vielbein; $\Psi$ any dirac16complex configuration (Grassmann-valued components) that is not identically zero. Then:

1. in the diagonal vielbein the Euler-Lagrange operator contains the gravitational term $\gamma^\mu D_\mu\Psi - \gamma^\mu\partial_\mu\Psi = \gamma^\mu\Omega_\mu\Psi = G\Psi$ with $G = 3H\gamma^{(0)} + \tfrac34u\,\gamma^{(4)}$; $G$ is never zero (its $\gamma^{(0)}$ coefficient is $3H$), $G^2 = \big(9H^2 - \tfrac{9}{16}u^2\big)\,I_{16}$, so $G\Psi \neq 0$ wherever $u^2 \neq 16H^2$ (on the background history $u = \tfrac43H$ and $G^2 = 8H^2I_{16}$), while where $|u| = 4H$ the matrix $G = 3H(\gamma^{(0)} \pm \gamma^{(4)})$ has rank 8 and annihilates an 8-dimensional subspace (this value depends on the frame and on the field variables, see the Remarks);
2. per direction, the $a_4'$ terms of the time direction of the three inflating and the three deflating directions cancel ($\frac32 a_4' - \frac32 a_4' = 0$), the $b_4'$ terms of the three extra times add ($3 \cdot \frac{u}{4} = \tfrac34u$), and the hidden-direction terms of all six directions add ($6 \cdot \frac{H}{2} = 3H$);
3. in addition the vielbein enters every derivative term, $\gamma^\mu\partial_\mu = \epsilon_s\gamma^{(i)}\partial_i + \gamma^{(4)}\partial_4 + \epsilon_t\gamma^{(t)}\partial_t + \tan z\,\gamma^{(0)}\partial_0$, none of whose factors is identically 1; because of the cancellation in 2, $a_4$ enters the field equations through the factors $e^{\mp a_4}$, and $b_4$ through $b_4^{-1/2}$ in $\epsilon_t$ and through $\tfrac34u\,\gamma^{(4)}$;
4. all gravitational terms vanish together only in flat 4+4 space: $\Omega_\mu = 0$ for every $\mu$ if and only if $a_4' = 0$, $b_4' = 0$ and $H = 0$, and $H = 0$ lies outside the family (a degenerate limit); no choice of local frame removes $\Omega_\mu$, because its curvature is the Riemann tensor and $R^{x_0}{}_{x_0} = -6H^2 \neq 0$: the metric is never flat for $H > 0$.

*Proof.* (a) The connection components of section 4 are each $a_4'$, $a_4' - \tfrac12u$ or $H$ times a factor $\pm e^{\pm a_4}\sin^{1/6}z$ or $\pm e^{-a_4}b_4^{1/2}\sin^{1/6}z$ that does not vanish on $0 < z < \pi/2$; since the $S^{ab}$ are linearly independent, the $x_4$-part of $\Omega_{x_i}$ vanishes if and only if $a_4$ is constant, that of $\Omega_{x_t}$ if and only if $e^{-a_4}b_4^{1/2}$ is constant, and the $H$-part if and only if $H = 0$; all $x_4$-parts vanish if and only if $a_4$ and $b_4$ are both constant (`Omega_vanishes_iff_a4prime_b4prime_and_H_vanish`, `nontriviality_Omega_zero_iff_flat`). (b) Contracting with $\gamma^\mu = \gamma^{(\mu)}/f_\mu$ and using $(\gamma^{(i)})^2 = 1$, $(\gamma^{(t)})^2 = -1$ gives the per-direction values of section 4: the $\gamma^{(4)}$ coefficients are $+\frac12 a_4'$ for each of the three inflating and $-\frac12 a_4' + \frac14u$ for each of the three deflating directions, the $\gamma^{(0)}$ coefficients are $\frac12 H$ for all six; hence $\gamma^\mu\Omega_\mu = G$, independent of $a_4$ and $x_0$ (`gammaOmega_per_direction`, `gammaOmega_total`, `a4_time_terms_cancel_b4_terms_add`, `gamma_mu_Omega_mu_equals_3H_gamma_x0_plus_b4_term`). The same value follows from the divergence form of section 4 (`gammaOmega_divergence_form`, `divergence_of_sqrtg_gamma`). (c) $\gamma^{(0)}$ and $\gamma^{(4)}$ anticommute, $(\gamma^{(0)})^2 = I_{16}$ and $(\gamma^{(4)})^2 = -I_{16}$, so $G^2 = (9H^2 - \tfrac{9}{16}u^2)I_{16}$; $G\Psi = 0$ implies $G^2\Psi = 0$ and therefore $\Psi = 0$ wherever $u^2 \neq 16H^2$; where $|u| = 4H$, $G$ has rank 8 (`gravity_term_square`, `nontriviality_1_dirac16complex`). (d) The term is part of the Euler-Lagrange equation although the connection drops out of $\mathcal{L}$ in this metric: the variation of the symmetrised kinetic term produces $\partial_\mu(\sqrt{|g|}\gamma^\mu) = 2\sqrt{|g|}\gamma^\mu\Omega_\mu$, and the Euler-Lagrange expressions equal $\sqrt{|g|}\,C\,(\gamma^\mu D_\mu\Psi - V\Psi)$ with the full covariant derivative (`L_spin_connection_drops_out_G`, `EL_Psibar_G`). (e) The curvature of $\Omega_\mu$ is $\frac12 R_{ab\mu\nu}S^{ab}$ (`spin_curvature_equals_Riemann`) and $R^{x_0}{}_{x_0} = -6H^2$ (`never_flat_for_H_positive`); if $\Omega_\mu$ vanished in some frame, the Riemann tensor would vanish. $H = 0$ is a degenerate limit of the metric (`degenerate_at_H_0`). This completes the proof.

Remarks (the exact scope of Theorem 1). In the formal flat limit ($a_4' = 0$, $b_4' = 0$ and $H = 0$ with the factors frozen) all gravitational terms vanish and the equation becomes the flat 4+4 Dirac-type equation, as the test [1] requires ("unless we are in flat 4+4 spacetime"). Items 1 and 2 are statements about the diagonal vielbein and the field variables $\Psi$; read without these hypotheses they would overstate [1]:

- The canonical connection drops out of $\mathcal{L}$, so the Euler-Lagrange equations are those of the connection-free symmetric Lagrangian; $G = \frac{1}{2\sqrt{|g|}}\partial_\mu(\sqrt{|g|}\gamma^\mu)$ is its half-density term (`connection_free_lagrangian_same_equations`).
- In the frame boosted in the $(x_0, x_4)$ plane with rapidity $6Hx_4 + b_0$ the $H$ part of the term vanishes identically and $\gamma'^\mu\Omega'_\mu = \tfrac34u\,(\cosh b\,\gamma^{(4)} - \sinh b\,\gamma^{(0)})$ remains; no boost in this plane removes the $b_4'$ part (section 4; `boosted_frame_removes_only_the_H_term`).
- In the diagonal frame the rescaling $\Psi = b_4^{-3/4}\sin^{-1/2}z\,\chi$ removes the whole term: $\gamma^\mu D_\mu\Psi = b_4^{-3/4}\sin^{-1/2}z\,\gamma^\mu\partial_\mu\chi$ exactly, so $\gamma^\mu\partial_\mu\chi = (m + U')\chi$; for $U = \frac{\lambda}{2}S^2$ the term turns into the $x_0$- and $x_4$-dependent coupling $\lambda S[\chi]/(b_4^{3/2}\sin z)$. The checks are `rescaling_removes_the_connection_term` and `rescaled_equation_quadratic_potential`. The exact $U = 0$ family of section 8 at $\alpha = -\frac12$ is this statement ($M = -m\gamma^{(4)}$, no $H$).
- The deflation $a_4$ contributes nothing to $\gamma^\mu\Omega_\mu$, although the $a_4$ sector is curved ($R^{x_4}{}_{x_4} = 6(a_4')^2 - 3a_4'u + \tfrac34u^2 + \tfrac32v$): $a_4$ enters only through the factors $e^{\mp a_4}$ of the derivative terms, while $b_4$ enters also through $\tfrac34u\,\gamma^{(4)}$ (`gammaOmega_blind_to_the_deflation`).
- The frame-independent content of [1] is item 4 with item 3: $\Omega_\mu$ vanishes in no frame (its curvature is the Riemann tensor and $R^{x_0}{}_{x_0} = -6H^2$), the vielbein factors $e^{\mp a_4}\sin^{-1/6}z$, $e^{a_4}b_4^{-1/2}\sin^{-1/6}z$ and $\tan z$ enter every derivative term, and the metric is curved for every $H > 0$. In the diagonal frame the connection also enters the energy-momentum tensor, for example the off-diagonal $K^{x_4}{}_{x_1}$ of a homogeneous configuration (`spin_connection_in_the_energy_momentum_tensor`).
- Interpretation (labelled): the hidden-direction operator $\tan z\,\partial_0 + 3H$ is antisymmetric for the measure $\cos z\,dx_0$ in the variables $\Psi$ up to a boundary term, $\cos z\,[p(\tan z\,\partial_0 + 3H)q + ((\tan z\,\partial_0 + 3H)p)q] = \partial_0(\sin z\,pq)$ (`good_sector_hermiticity_curved`; formula key `hidden_direction_hermiticity`; the factor $b_4^{3/2}$ of the measure does not depend on $x_0$); in the variables $\chi$ with the measure $dy = \cot z\,dx_0$ the operator $\partial_y$ has the same property without any $H$ term. This role of $3H$ therefore depends on the variables and the measure, and the boundary term does not vanish at $z = \pi/2$ (section 11). The $b_4$ term plays the corresponding role for the $x_4$ dependence of the measure: in the mode operator it is the anti-Hermitian term $-i\tfrac34u$, which compensates $\partial_4\sqrt{|g|} = \tfrac32u\sqrt{|g|}$ (section 11).

Non-triviality [2], for the commuting field dirac16complex00, has the same algebraic content and the same scope (`nontriviality_2_dirac16complex00`) and is the subject of the companion document `Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md`.

## 8. Self-consistency

The field equations of section 6 are self-consistent in the following exact senses.

- One system. The adjoint equation is the Dirac conjugate of the field equation: with $E = \gamma^\mu D_\mu\Psi - (m + U')\Psi$ and $\bar E = (D_\mu\bar\Psi)\gamma^\mu + (m + U')\bar\Psi$, $E^\dagger C = -\bar E$ exactly (`adjoint_equation_is_Dirac_conjugate_G`, `grassmann_adjoint_equation_is_conjugate`).
- Evolution form, not a well-posed Cauchy problem. The evolution form of section 6 holds exactly (`evolution_form_G`), and the Heisenberg equation of the quantised field reproduces it, including the term $-\tfrac34u\,\Psi$, which comes from the spin connection of the extra times: see the Wolfram check `Heisenberg_equation_reproduces_field_equation` and the sympy check `hamiltonian_form_and_heisenberg_equation`. The slices $x_4 = $ const are non-characteristic, but the Cauchy problem is not well posed in Hadamard's sense for data that depend on $x_5, x_6, x_7$: with frozen coefficients an extra-time momentum $k_5 = K$ gives the growth rate $\sqrt{K^2 - m^2 - k_0^2 - k_1^2 - k_2^2 - k_3^2}$, unbounded as $K$ grows (`extra_time_growth_rates_unbounded`), and in the metric the frame momentum $e^{a_4}b_4^{-1/2}\sin^{-1/6}z\,k_{x_5}$ grows as the extra times deflate. A well-posed evolution is available at most in the good sector (no extra-time dependence) and only with a boundary condition at $z = \pi/2$ (section 11).
- Integrability. The gammas are covariantly constant and the spinor curvature is the Riemann tensor (section 4). The square of the Dirac operator obeys the Lichnerowicz identity (`Lichnerowicz_identity_G`, `lichnerowicz_identity_on_fields`, `lichnerowicz_contraction`):

$$
(\gamma^\mu D_\mu)^2\Psi = g^{\mu\nu}\big(D_\mu D_\nu\Psi - \Gamma^\lambda{}_{\mu\nu}D_\lambda\Psi\big) - \frac{R}{4}\Psi,\qquad R = 6(a_4')^2 - 3a_4'u + 3u^2 + 3v - 42H^2,
$$

  so the second-order consequence of the field equations is consistent with the curvature.
- Conserved current. $J^\mu = -i\bar\Psi\gamma^\mu\Psi$ is real, and off shell $\partial_\mu(\sqrt{|g|}J^\mu) = -i\sqrt{|g|}\,(\bar E\Psi + \bar\Psi E)$ with $\sqrt{|g|} = b_4^{3/2}\cos z$, so $\nabla_\mu J^\mu = 0$ on shell (`current_real_G`, `current_conservation_identity_G`, `grassmann_current_conservation`). The charge density is $J^{x_4} = \Psi^\dagger B\Psi$, and the charge of a slice of constant $x_4$, $Q = \int b_4^{3/2}\cos z\,\Psi^\dagger B\Psi\,d^7x$, is an indefinite form (`charge_density_is_Krein_form_G`). Only the local law $\nabla_\mu J^\mu = 0$ is established: $Q$ is constant in $x_4$ only if no charge flows through the boundary of the slice, and at the brane $z = \pi/2$ the flow is not zero in general (`good_sector_hermiticity_up_to_the_brane_flux`, both engines; the lead's independent check `u1_noether_matrix_identity` of `Revision/lead_checks/reports/charge-conjugation-and-u1.json` verifies the local law for general $a_4(x_4)$ and $b_4(x_4)$ and states that the constancy of $Q$ is not established). This record imposes no boundary condition at $z = \pi/2$ (sections 11 and 15).
- Bianchi-type identity of the energy-momentum tensor. For the tensor $T^\mu{}_\nu$ of section 9 the invariance of the action under coordinate changes gives, off shell, for each $\lambda$ and for general $a_4$ and $b_4$, $\partial_\mu(\sqrt{|g|}T^\mu{}_\lambda) - \sqrt{|g|}\,T^\mu{}_a\,\partial_\lambda e^a{}_\mu = \sum_\phi \mathrm{EL}_\phi\,\partial_\lambda\phi$ (`Noether_identity_diffeomorphisms_G`), and the invariance under the 28 local frame rotations makes the antisymmetric part of $T$ a combination of Euler-Lagrange expressions (`Noether_identity_local_Lorentz_G`). On shell, therefore, $T$ is symmetric and $\nabla_\mu T^\mu{}_\nu = 0$ for general solutions (`conservation_on_shell_general`); the sympy side verifies $\nabla_\mu T^\mu{}_\nu = 0$ for all eight $\nu$ after the on-shell substitution, with a negative control (`grassmann_emt_conservation_on_shell`, `grassmann_emt_conservation_negative_control`). The gravitational side satisfies the matching identities $\nabla_\mu E_{(k)}{}^\mu{}_\nu = 0$ (section 13).
- Exact solutions as test points. For $U = 0$ and all functions $a_4$, $b_4$, $\Psi = b_4^{-3/4}\sin^\alpha z\,\big(\cosh(kx_4) + \frac{\sinh(kx_4)}{k}M\big)\chi$ with constant $\chi$, $M = -m\gamma^{(4)} + 3H(2\alpha + 1)\gamma^{(4)}\gamma^{(0)}$, $k^2 = 9H^2(2\alpha + 1)^2 - m^2$, solves the field equation (the factor $b_4^{-3/4}$ compensates the term $\tfrac34u\,\gamma^{(4)}$), and conservation of $T$ and $J$ holds exactly there (`solution_matrix_square`, `exact_solution_x4_x0_G`, `exact_solution_family_x4_x0`); the scope of this test is stated in the report: at these solutions the pressures and the momentum density vanish and $\rho = mS$ with $S = b_4^{-3/2}S_\chi$, so the general proof is the pair of Noether identities. An exact nonlinear homogeneous solution with $U = \frac{\lambda}{2}S^2$ exists in the explicit Grassmann algebra for all functions $a_4$, $b_4$: $\Psi = b_4^{-3/4}\sum_k\big[Pc_k + \lambda S_0\,\eta_k\big]\theta_k$ with $P = \cosh(kx_4) + \frac{\sinh(kx_4)}{k}M$, $M = -m\gamma^{(4)} + 3H\gamma^{(4)}\gamma^{(0)}$, $k^2 = 9H^2 - m^2$, $\eta_k = -P\,(A_0I_0 + A_cI_c + A_sI_s)\,c_k$ with constant matrices $A_0$, $A_c$, $A_s$ and the integrals $I_0 = \int_0^{x_4}b_4^{-3/2}\,ds$, $I_c = \int_0^{x_4}b_4^{-3/2}\cosh(2ks)\,ds$, $I_s = \int_0^{x_4}b_4^{-3/2}\sinh(2ks)\,ds$, and $S_0 = \sum_{kl}\bar\theta_k\theta_l\,c_k^\dagger Cc_l$; then $S = b_4^{-3/2}S_0$ (`exact_solution_nonlinear_homogeneous_G`; formula key `exact_solutions`; for the commuting field every solution of the reduced linear system gives one, `exact_solution_nonlinear_homogeneous_C`, sympy `exact_nonlinear_homogeneous_solution` for both statistics).

## 9. The energy-momentum tensor

The energy-momentum tensor is defined by the vielbein variation of the action and has the closed form, for general $a_4$ and $b_4$ (`T_vielbein_variation_closed_form_G`; formula key `T_variation`; sympy `grassmann_emt_equals_general_vielbein_variation_on_shell` with all 64 components of a general first-order vielbein variation)

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

Diagonal components in the primordial field (no sum; `T_diagonal_components_G`, `grassmann_emt_equals_vielbein_variation_diagonal`; formula key `EMT_diagonal`): with the directional kinetic terms ($f_5 = f_6 = f_7 = e^{-a_4}b_4^{1/2}\sin^{1/6}z$)

$$
K_\mu = \frac{1}{2f_\mu}\big(\bar\Psi\gamma^{(\mu)}\partial_\mu\Psi - \partial_\mu\bar\Psi\gamma^{(\mu)}\Psi\big),\qquad \mathcal{L}_0 = \sum_\mu K_\mu - mS - U(S),
$$

$$
T^\mu{}_\mu = \mathcal{L}_0 - K_\mu .
$$

No spin-connection term survives in the diagonal components, because $\{\gamma^\mu, \Omega_\mu\} = 0$ for each $\mu$. The off-diagonal component $x_4$-$x_0$, which enters the off-diagonal field equation of section 13, is (`T_x4_x0_component_G`; formula key `EMT_offdiagonal_x4_x0`)

$$
T^{x_4}{}_{x_0} = -\tfrac14\big(B_{40} - \cot z\,B_{04}\big),\qquad T^{x_0}{}_{x_4} = -\tan^2 z\;T^{x_4}{}_{x_0},
$$

with $B_{40} = \bar\Psi\gamma^{(4)}\partial_0\Psi - \partial_0\bar\Psi\gamma^{(4)}\Psi$ and $B_{04} = \bar\Psi\gamma^{(0)}\partial_4\Psi - \partial_4\bar\Psi\gamma^{(0)}\Psi$. For homogeneous on-shell configurations both $T^{x_4}{}_{x_0}$ and $T^{x_0}{}_{x_4}$ vanish identically (`grassmann_T_x4x0_homogeneous`), so these configurations do not source the off-diagonal field equation $\kappa\,T^{x_4}{}_{x_0} = \cot z\,u\,Q$ of section 13, which for $b_4$ not constant then requires $Q = 0$; this is not claimed for the other off-diagonal components (42 of the remaining 54 are nonzero bilinears in general), whose vanishing is a separate condition on the state (section 13). The trace (off shell, an exact identity in both engines) and the on-shell kinetic sum are (`EMT_trace_G`, `grassmann_trace_on_shell`, `kinetic_sum_on_shell_G`)

$$
T^\mu{}_\mu = 7\sum_\mu K_\mu - 8\big(mS + U\big),\qquad \sum_\mu K_\mu = \big(m + U'(S)\big)S + \tfrac12\big(\bar\Psi E - \bar E\Psi\big),
$$

so on shell $\mathcal{L}_0 = SU' - U$ and $T^\mu{}_\mu = -mS + 7SU' - 8U = -mS + 3\lambda S^2$. For a diagonal tensor $T = \mathrm{diag}(p_0, p_3, p_3, p_3, -\rho, p_t, p_t, p_t)$ whose entries are functions of $x_0$ and $x_4$, the covariant divergence is, in all eight components (`energy_exchange_equation` in both field-theory reports; formula key `energy_exchange`),

$$
\nabla_\mu T^\mu{}_{x_4} = -\partial_4\rho - 3a_4'\,(p_3 - p_t) - \tfrac32u\,(\rho + p_t),\qquad \nabla_\mu T^\mu{}_{x_0} = \partial_0 p_0 + 3H\cot z\,(2p_0 - p_3 - p_t),
$$

and $\nabla_\mu T^\mu{}_\nu = 0$ identically for $\nu = x_1, x_2, x_3, x_5, x_6, x_7$. Conservation is therefore exactly

$$
\partial_4\rho = -3a_4'\,(p_3 - p_t) - \tfrac32u\,(\rho + p_t),\qquad \partial_0 p_0 = -3H\cot z\,(2p_0 - p_3 - p_t) :
$$

energy flows between 3-space and the extra times unless $p_3 = p_t$, and the extra-time volume factor $b_4^{3/2}$ dilutes $\rho + p_t$; the $x_4$ component contains no $x_0$ derivative and no $H$, the $x_0$ component no $x_4$ derivative, no $a_4'$ and no $b_4'$. For entries independent of $x_0$ the two conditions become $d\rho/dx_4 = -3a_4'(p_3 - p_t) - \tfrac32u(\rho + p_t)$ and $p_0 = (p_3 + p_t)/2$.

For dirac16complex these expressions are even elements of the Grassmann algebra; they are the classical counterpart of the energy-momentum tensor operator of section 12, from which all numbers come.

## 10. Kinetic energy, potential energy, energy density, pressures and equations of state

From the diagonal components of section 9 (formula keys `EMT_diagonal`, `EMT_kinetic_potential`, `equation_of_state_definitions`):

$$
\begin{aligned}
\rho &= -T^{x_4}{}_{x_4} = \rho_{\rm kin} + \rho_{\rm pot},\qquad \rho_{\rm kin} = -\sum_{\mu\neq x_4}K_\mu,\qquad \rho_{\rm pot} = mS + U(S), \\
p_3 &= T^{x_1}{}_{x_1} = \sum_{\mu\neq x_1}K_\mu - mS - U(S), \\
p_t &= T^{x_5}{}_{x_5} = \sum_{\mu\neq x_5}K_\mu - mS - U(S), \\
p_0 &= T^{x_0}{}_{x_0} = \sum_{\mu\neq x_0}K_\mu - mS - U(S),
\end{aligned}
$$

with $p_3 = T^{x_1}{}_{x_1} = T^{x_2}{}_{x_2} = T^{x_3}{}_{x_3}$ for configurations isotropic in 3-space and $p_t = T^{x_5}{}_{x_5} = T^{x_6}{}_{x_6} = T^{x_7}{}_{x_7}$ for configurations isotropic in the extra times. The kinetic energy density is $\rho_{\rm kin}$, the potential energy density $\rho_{\rm pot} = mS + U$; the kinetic pressure in direction $\mu$ is $\sum_{\nu\neq\mu}K_\nu$ and the potential pressure is $-(mS + U)$ in every direction. The equations of state are

$$
w_3 = \frac{p_3}{\rho},\qquad w_t = \frac{p_t}{\rho},\qquad w_{x_0} = \frac{p_0}{\rho}.
$$

Homogeneous on-shell configurations (depending on $x_4$ only): $K_\mu = 0$ for $\mu \neq x_4$ and $K_{x_4} = (m + U')S$ (the $b_4'$ terms of $\Psi$ and $\bar\Psi$ cancel in $K_{x_4}$), hence (`grassmann_homogeneous_on_shell_rho_p`, `exact_solution_nonlinear_homogeneous_G`; formula key `EMT_homogeneous_on_shell`)

$$
\rho = mS + U,\qquad p_3 = p_t = p_0 = SU' - U,\qquad \rho_{\rm kin} = 0,\qquad p_{\rm kin} = (m + U')S,
$$

$$
w_3 = w_t = w_{x_0} = \frac{SU' - U}{mS + U},
$$

and for $U = \frac{\lambda}{2}S^2$

$$
\rho = mS + \tfrac{\lambda}{2}S^2,\qquad p = \tfrac{\lambda}{2}S^2,\qquad w_3 = w_t = w_{x_0} = \frac{\lambda S}{2m + \lambda S} .
$$

For the exact homogeneous solutions $b_4^{3/2}S = S_0$ is constant along $x_4$ (`exact_solution_nonlinear_homogeneous_G`; for the classical condensate of the field-equations record `condensate_S_b4_three_halves_constant`), so $S = b_4^{-3/2}S_0$ follows the extra-time volume, and for $\lambda \neq 0$ the ratio $w = \lambda S/(2m + \lambda S)$ drifts as $b_4$ changes. This agrees with the energy-exchange equation: with $p_3 = p_t = p$ it reads $d\rho/dx_4 = -\tfrac32u(\rho + p)$, and $d\rho/dx_4 = (m + \lambda S)\,dS/dx_4 = -\tfrac32u\,(mS + \lambda S^2) = -\tfrac32u\,(\rho + p)$. For dirac16complex all these quantities are Grassmann-algebra elements until they are evaluated as expectation values of the normal-ordered operators of section 12. The equation of state seen by a 3-space observer and its time dependence (the dark-sector hypotheses of SPEC section 8) are not computed in this document; they are investigated in `Revision/docs/DARK_SECTOR_HYPOTHESES`, whose verdict for dirac16complex is summarised in section 15.

## 11. Canonical quantisation in 4 + 4 dimensions and the Krein structure

The evolution time is $x_4$. The momentum conjugate to $\Psi_A$ (right derivative) is $\pi_A = \frac{i}{2}b_4^{3/2}\cos z\,(\Psi^\dagger B)_A$ for the symmetric Lagrangian and $i\,b_4^{3/2}\cos z\,(\Psi^\dagger B)_A$ for the first-order form; it depends on $\Psi^\dagger$ only, a second-class constraint as for Dirac's field (`canonical_momentum` in both reports). Up to a total divergence $\mathcal{L} = \Psi^\dagger K\,\partial_4\Psi - (\text{terms without }\partial_4)$ with $K = b_4^{3/2}\cos z\,C\gamma^{(4)} = i\,b_4^{3/2}\cos z\,B$, and the canonical (Dirac-bracket) anticommutator on a slice $x_4 = $ const is (`first_order_form_and_anticommutator`, `canonical_anticommutator_B`)

$$
\{\Psi_A(x), \Psi^\dagger_C(y)\}_{x_4 = y_4} = B_{AC}\,\frac{\delta^7(x - y)}{\sqrt{|g|}} = B_{AC}\,\frac{\delta^7(x - y)}{b_4^{3/2}\cos z} .
$$

With the Hamiltonian density $\mathcal{H} = b_4^{3/2}\cos z\,\big[\Psi^\dagger\big(mC - \sum_{\mu\neq x_4}C\gamma^\mu D_\mu\big)\Psi + U(S)\big]$ (the unsymmetrised $\mathcal{L} = \Psi^\dagger K\partial_4\Psi - \mathcal{H}$ exactly), the Heisenberg equation $\partial_4\Psi = i[H, \Psi]$ equals the field equation solved for $\partial_4\Psi$, with the operator ordering of the classical expression; the spin connection of the seven slice directions contributes $\gamma^{(4)}\sum_{a\neq x_4}\gamma^a\Omega_a = 3H\gamma^{(4)}\gamma^{(0)} - \tfrac34u$ (`Heisenberg_equation_reproduces_field_equation`, `hamiltonian_form_and_heisenberg_equation`).

**Theorem 2 (the canonical anticommutator forces a Krein structure).** Hypotheses: the canonical anticommutator above, and $\Psi^\dagger$ realised as the adjoint of $\Psi$ in a space with a positive-definite inner product. These are incompatible: there is no positive inner product with $\Psi^\dagger$ as the adjoint. *Proof.* $B$ has the eigenvalue $-1$ with multiplicity 8; for the exact unit vector $u_-$ with components $(u_-)_7 = -i/\sqrt2$, $(u_-)_{16} = 1/\sqrt2$ and all others zero, $Bu_- = -u_-$, and the smeared operator $X = \sum_A (u_-)_A^*\Psi_A(f)$ has $\{X, X^\dagger\} = (u_-^\dagger Bu_-)\,\lVert f\rVert^2 = -\lVert f\rVert^2 < 0$, whereas in a space with positive inner product $\{X, X^\dagger\} = XX^\dagger + X^\dagger X$ is a positive operator (`no_positive_inner_product` in both reports). Hence the state space carries an indefinite (Krein) inner product with fundamental symmetry $B$ ($B = B^\dagger$, $B^2 = 1$, signature (8,8)); equivalently, in a positive Hilbert space the canonical conjugate $\Psi^\dagger$ is not the Hilbert adjoint $\chi$ but $\Psi^\dagger = \chi B$, with $\{\Psi_A, \chi_C\} = \delta_{AC}$.

The one-particle Krein structure. The curved mode operator ($i\partial_4\Psi = h\Psi$ for $U = 0$) is $h = m(-i\gamma^{(4)}) + \sum_{a\neq x_4}\frac{1}{f_a}\,i\gamma^{(4)}\gamma^{(a)}\partial_a + 3iH\gamma^{(4)}\gamma^{(0)} - i\tfrac34u$; its last term is anti-Hermitian and compensates exactly the $x_4$ dependence of the measure, $\partial_4\sqrt{|g|} = \tfrac32u\sqrt{|g|}$. It is formally self-adjoint for the Krein form $\int b_4^{3/2}\cos z\,u^\dagger Bv\,d^7x$, that is up to boundary terms (`Krein_form_conserved_curved`, `good_sector_hermiticity_curved`). The boundary term of the hidden direction does not vanish at the patch end: $\sqrt{|g|}\,[u^\dagger(hv) - (hu)^\dagger v] = \partial_0(b_4^{3/2}\sin z\,u^\dagger M_0 v) - i(\partial_4\sqrt{|g|})\,u^\dagger v$ with $M_0 = i\gamma^{(4)}\gamma^{(0)}$ in the good sector at $k = 0$, and the $x_0$ term vanishes at the tip but not at $z = \pi/2$, a surface at finite proper distance where $\sin z = 1$ (`good_sector_hermiticity_up_to_the_brane_flux`, both engines). The Krein form is therefore conserved, and $h$ self-adjoint, only with a boundary condition at $z = \pi/2$ (for example the ASSUMED brane condition of the Kohn-Sham record); this record imposes none. For frozen coefficients (frame momenta $k_a$), plane waves $u\,e^{i(k\cdot x - Ex_4)}$ obey $Eu = h_k u$ with $h_k = m\beta + \sum_a k_a\alpha^a$, $\beta = -i\gamma^{(4)}$, $\alpha^a = -\gamma^{(4)}\gamma^{(a)}$; $\beta$ and $\alpha^{0,1,2,3}$ are Hermitian, $\alpha^{5,6,7}$ anti-Hermitian, $Bh_k = h_k^\dagger B$ (Krein self-adjoint), and (`mode_hamiltonian_good_sector`, `mode_hamiltonian_Krein_selfadjoint`, `mode_hamiltonian_B_selfadjoint_dispersion`)

$$
h_k^2 = \big(m^2 + k_0^2 + k_1^2 + k_2^2 + k_3^2 - k_5^2 - k_6^2 - k_7^2\big)\,I_{16} .
$$

Good sector (no dependence on the extra times, $k_5 = k_6 = k_7 = 0$): $h_k$ is Hermitian with eigenvalues $\pm E$, eight each, and commutes with $B$; $B$ also commutes with the curved terms $3iH\gamma^{(4)}\gamma^{(0)}$ and $-i\tfrac34u$ (`good_sector_spectrum_and_B_sectors`). The curved mode operator is symmetric for the measure $b_4^{3/2}\cos z\,d^7x$ in this sector only up to the boundary term at $z = \pi/2$ (`good_sector_hermiticity_curved`, `good_sector_hermiticity_up_to_the_brane_flux`): on the good-sector functions that do not depend on $x_0$ (finite norm, $\int_0^{\pi/(12H)}\cos(6Hx_0)\,dx_0 = 1/(6H)$) it acts as $A - i\tfrac34u$ with the matrix $A = -im\gamma^{(4)} + 3iH\gamma^{(4)}\gamma^{(0)}$, so $\Psi = b_4^{-3/4}\chi$ with $i\partial_4\chi = A\chi$; $A$ is not Hermitian and has the square $(m^2 - 9H^2)I_{16}$; at $m = H = 1$ its eigenvalues are $\pm 2\sqrt2\,i$ (`good_sector_x0_independent_modes_without_boundary_condition`). Without a boundary condition at $z = \pi/2$ the good sector of the author's metric therefore contains growing modes, for $U = 0$ whenever $m^2 < 9H^2$; the exact solutions of section 8 with $\alpha = 0$ ($k^2 = 9H^2 - m^2$) are such modes. Positive Fock realisation: $\Psi = \sum_s(b_s u_s + d_s^* v_s)$ with orthonormal eigenvectors $u_s$ (energy $+E$) and $v_s$ (energy $-E$), $\{b, b^*\} = \{d, d^*\} = 1$ on a positive Fock space, and $\Psi^\dagger = \chi B$, so that $\{\Psi_A, \Psi^\dagger_C\} = B_{AC}$. Exact examples (one momentum each, flat frame): Wolfram, $m = 3$, $k = (4, 0, 0, 0)$ along $x_1$, $E = 5$, on the explicit fermionic Fock space of $2^{16}$ occupation states; sympy, $m = 2$, $(k_0, k_1, k_2, k_3) = (4, 1, 2, 0)$, $E = 5$. The Hamiltonian $\chi h_k\Psi$ has the vacuum value $-8E$ (the filled sea; $-40$ in the sympy example), and after normal ordering the energy is $+E$ for the particle $b_0^*|0\rangle$ and $+E$ for the antiparticle $d_0^*|0\rangle$; the charge $\Psi^\dagger B\Psi = \chi\Psi$ is $+1$ and $-1$ (`Fock_space_good_sector_example`, `good_sector_positive_fock_realisation`).

Expectation-value rule. In the positive realisation, $\langle u|{:}\Psi^\dagger M\Psi{:}|u\rangle = u^\dagger BMu$ for a particle and $-v^\dagger BMv$ for an antiparticle (verified for $M = C$, $-iC\gamma^{(4)}$, $-iC\gamma^{(1)}$, $C\gamma^{(2)}\gamma^{(3)}$, a dense integer matrix and a generic symbolic matrix). In the Krein-Fock realisation ($\Psi^\dagger$ the Krein adjoint, modes with $u_n^\dagger Bu_n = \epsilon_n$) the normalised expectation of ${:}\Psi^\dagger M\Psi{:}$ is $\epsilon_n u_n^\dagger Mu_n$, which equals $u_n^\dagger BMu_n$ when $Bu_n = \epsilon_n u_n$ and not for a Krein-boosted mode (`Fock_space_good_sector_example`, `good_sector_positive_fock_realisation`, `expectation_value_rule`).

Extra-time modes. With extra-time momentum, $E^2 = m^2 + k_s^2 - k_t^2$ is negative when $k_t^2 > m^2 + k_s^2$; exact example $m = 1$, $k_5 = 2$: $E = \pm i\sqrt3$, modes growing like $e^{\sqrt3\,x_4}$. The growth rate has no upper bound as the extra-time momentum grows (`extra_time_growth_rates_unbounded`). In the metric the frame momentum $k_{(5)} = e^{a_4}b_4^{-1/2}\sin^{-1/6}z\,k_{x_5}$ grows as the extra times deflate (the scale factor $e^{-a_4}b_4^{1/2}$ decreasing; on the background history it is proportional to $e^{-a_4/3}$), so every extra-time mode eventually enters the growing regime (a local-frame statement); extra-time momenta mix the $B = \pm1$ sectors (`extra_time_modes_grow`, `mode_hamiltonian_good_sector`, `good_sector_spectrum_and_B_sectors`). Krein structure of the one-particle eigenspaces in flat 4+4 space (pairing record): every eigenspace of REAL frequency, $E^2 > 0$, with or without extra-time momentum, has Krein inertia (4,4) (proved for every real frequency: `Q_one_particle_Krein_inertia_real_frequencies`, `Q.one_particle_Krein_inertia_proof`), while the eigenspaces of imaginary or zero frequency, those of the growing modes, are Krein-neutral, $B$ vanishes on them identically (`Q_one_particle_complex_and_zero_frequencies_Krein_neutral`, `Q.one_particle_complex_frequency_Krein_neutral`; for $m = 1$, $k_5 = 2$ both 8-dimensional eigenspaces of $\pm i\sqrt3$).

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
- For $\lambda \neq 0$ the potential term is quartic. The field-equations record states the rule used there: every bilinear is replaced by the expectation value of its normal-ordered operator in the state, with $\langle{:}U(S){:}\rangle \neq U(\langle{:}S{:}\rangle)$ in general, and it records the operator form of the on-shell identity $\sum_\mu\langle{:}K_\mu{:}\rangle = \langle{:}(m + U')S{:}\rangle$ for the normal-ordered operators of the field on a whole slice as ASSUMED, not proved, and as decided only in the finite model of `Revision/theory/fock_quartic/` (next bullet; entry `dirac16complex` of the formula key `fields` of `Revision/field_equations_a4/a4-equations.json`). The identity is verified exactly for the Grassmann-algebra field (`kinetic_sum_on_shell_G`).
- The operator form for $\lambda \neq 0$ in a finite model (record `Revision/theory/fock_quartic/`, 2026-10-08; one Python checker with sympy and its own exact engine for the canonical anticommutation relations, no Wolfram counterpart; 21 of 21 checks pass). The model is the positive fermionic Fock space ($\Psi^\dagger = \chi B$) of one good-sector plane-wave mode set with frozen coefficients: flat frame, volume 1, 16 modes, $2^{16}$ states, at rest ($k = 0$, symbolic $m$) and at $m = 3$, $k = (4, 0, 0, 0)$; at $\lambda = 0$ it reproduces the Fock example of section 11 (`control_record_Fock_example`). With the Wick-ordered potential $U = \frac{\lambda}{2}{:}SS{:}$ in the Hamiltonian and $K_\mu$ defined as Wick products with the Heisenberg derivative of the field, ${:}\sum_\mu K_\mu{:} = {:}(m + U'(S))S{:}$ holds as an exact operator identity on every state of the model, for the solution of the interacting operator field equation (`trace_identity_operator_identity_wick`), and at $k = 0$ the homogeneous values $\hat\rho = {:}mS + U{:}$ and $\hat p = {:}SU' - U{:}$ are operator identities in the same sense (`homogeneous_rho_p_operator_identities_wick`). Of the tested choices (four orderings of the potential, Wick product or vacuum subtraction on the left, two right-hand sides) only this one works: every other combination (30 of them on the two mode sets) fails by a nonzero one-body operator (sometimes plus a constant) linear in $\lambda$, and already in expectation values, at $k = 0$ on every state except the vacuum of the mode set (`trace_identity_fails_for_every_other_combination`, `expectation_classes_M0`, `expectation_values_M1`); so the identity holds in this model if and only if the potential and the energy-momentum tensor are both Wick ordered. It also fails for the free dynamics, so it is a statement about solutions of the interacting operator field equation (`negative_control_free_dynamics`). On states with $n$ quanta at $k = 0$, $\rho = mn + \frac{\lambda}{2}n(n - 1)$ and $p = \frac{\lambda}{2}n(n - 1)$, so $\langle{:}U(S){:}\rangle \neq U(\langle{:}S{:}\rangle)$ (`homogeneous_expectation_values_are_not_U_of_expectation`). Nothing is proved for the field on a whole slice (many momenta), for the curved $x_0$ dependence with its boundary term at $z = \pi/2$, or for the extra-time sector; the model gives no numerical expectation value for a physical many-fermion state.
- Numerical expectation values of $\hat T$ for many-fermion states are computed only in the Kohn-Sham approximation (`Revision/kohn_sham/`, document `Revision/docs/KOHN_SHAM_DEFLATING_FIELD`); this document quotes only quantities derived from them, in section 13 (the source-condition ratios, the relative defects and the runs of the approximation of the $a_4$ and $b_4$ equations with the Kohn-Sham source) and in section 15 (the equation-of-state values $w_{\rm eff}$ of the Kohn-Sham gas from the dark-sector record).
- The Grassmann-algebra tensor of sections 9 and 10 obeys the identities of section 8 (symmetry and conservation on shell); the operator inherits them for the bilinear ($\lambda = 0$) part, where they are linear in the field equations; for the quartic part they are not verified as operator statements (the finite model above decides the trace identity and the homogeneous $\rho$ and $p$, not symmetry or conservation).

## 13. The field equations for a4[x4] and b4[x4] with dirac16complex as the source

Einstein-Lovelock gravity (SPEC section 5), with the Lovelock tensors computed with the generalised Kronecker delta in `Revision/gkd_lovelock` and recomputed in both verifiers of the field-equations branch for general $a_4$ and $b_4$ (for example `P3_direct_equals_gkd_branch_monomials`, `P1_direct_equals_minus_4_Einstein` and `P4_vanishes_pigeonhole`; sympy `P3_equals_gkd_branch_monomials`; and equal to the independent record of the metric change, `lovelock_equals_metric_b4_set`):

$$
\sum_{k=1}^{3}\alpha_k\,E_{(k)}{}^\mu{}_\nu + \Lambda\,\delta^\mu_\nu = \kappa\,T^\mu{}_\nu,\qquad E_{(k)} = -\frac{P_{(k)}}{2^{k+1}},\qquad E_{(1)} = G,
$$

with $\alpha_1 = 1$ for Einstein gravity and the source $T^\mu{}_\nu = \mathrm{diag}(p_0, p_3, p_3, p_3, -\rho, p_t, p_t, p_t) + q_{40} + q_{04}$ ($q_{40}$ at $\mu = x_4$, $\nu = x_0$; $q_{04}$ at $\mu = x_0$, $\nu = x_4$). The left-hand sides are divergence-free (`E1_divergence_free`, `E2_divergence_free`, `E3_divergence_free` in both reports). They depend on $b_4$ only through $u = b_4'/b_4$ and $v = u'$, so a constant factor of $b_4$ is a rescaling of $x_5, x_6, x_7$ (`lovelock_depends_on_b4_through_u_and_v`); their diagonal components are free of $x_0$ and of $a_4$ itself, with $x_1 = x_2 = x_3$ and $x_5 = x_6 = x_7$; the only nonzero off-diagonal components are the pair $x_4$-$x_0$, $x_0$-$x_4$, each proportional to $u$, and every other off-diagonal left-hand side is zero (`independent_components`, `P1_structure`, `P2_structure`, `P3_structure`; sympy `other_components_vanish`). The diagonal components (formula key `lovelockTensors` of `Revision/field_equations_a4/a4-equations.json`; `json_lovelock_components`):

$$
\begin{aligned}
E_{(1)}{}^{x_0}{}_{x_0} &= -3 (a_4')^{2} + \tfrac{3}{2} a_4' u - \tfrac{3}{2} u^{2} - \tfrac{3}{2} v + 15 H^{2}
\end{aligned}
$$

$$
\begin{aligned}
E_{(1)}{}^{x_1}{}_{x_1} &= -3 (a_4')^{2} + 3 a_4' u + a_4'' - \tfrac{3}{2} u^{2} \\
&\quad - \tfrac{3}{2} v + 15 H^{2}
\end{aligned}
$$

$$
\begin{aligned}
E_{(1)}{}^{x_4}{}_{x_4} &= 3 (a_4')^{2} - \tfrac{3}{2} a_4' u - \tfrac{3}{4} u^{2} + 21 H^{2}
\end{aligned}
$$

$$
\begin{aligned}
E_{(1)}{}^{x_5}{}_{x_5} &= -3 (a_4')^{2} - a_4'' - \tfrac{3}{4} u^{2} - v + 15 H^{2}
\end{aligned}
$$

$$
\begin{aligned}
E_{(2)}{}^{x_0}{}_{x_0} &= 12 (a_4')^{4} - 12 (a_4')^{3} u + 18 (a_4')^{2} u^{2} + 12 (a_4')^{2} v \\
&\quad + 168 (a_4')^{2} H^{2} + 24 a_4' a_4'' u - \tfrac{15}{2} a_4' u^{3} - 12 a_4' u v \\
&\quad - 84 a_4' u H^{2} - 6 a_4'' u^{2} - \tfrac{3}{4} u^{4} - \tfrac{3}{2} u^{2} v \\
&\quad + 48 u^{2} H^{2} + 60 v H^{2} - 180 H^{4}
\end{aligned}
$$

$$
\begin{aligned}
E_{(2)}{}^{x_1}{}_{x_1} &= 12 (a_4')^{4} - 24 (a_4')^{3} u - 24 (a_4')^{2} a_4'' + 18 (a_4')^{2} u^{2} \\
&\quad + 12 (a_4')^{2} v + 168 (a_4')^{2} H^{2} + 24 a_4' a_4'' u - 3 a_4' u^{3} \\
&\quad - 6 a_4' u v - 120 a_4' u H^{2} - 3 a_4'' u^{2} - 40 a_4'' H^{2} \\
&\quad - \tfrac{3}{4} u^{4} - \tfrac{3}{2} u^{2} v + 42 u^{2} H^{2} + 60 v H^{2} \\
&\quad - 180 H^{4}
\end{aligned}
$$

$$
\begin{aligned}
E_{(2)}{}^{x_4}{}_{x_4} &= -36 (a_4')^{4} + 36 (a_4')^{3} u - 120 (a_4')^{2} H^{2} - \tfrac{9}{2} a_4' u^{3} \\
&\quad + 60 a_4' u H^{2} + 30 u^{2} H^{2} - 420 H^{4}
\end{aligned}
$$

$$
\begin{aligned}
E_{(2)}{}^{x_5}{}_{x_5} &= 12 (a_4')^{4} + 24 (a_4')^{2} a_4'' + 168 (a_4')^{2} H^{2} - 3 a_4' u^{3} \\
&\quad - 6 a_4' u v - 48 a_4' u H^{2} - 3 a_4'' u^{2} + 40 a_4'' H^{2} \\
&\quad + 24 u^{2} H^{2} + 40 v H^{2} - 180 H^{4}
\end{aligned}
$$

$$
\begin{aligned}
E_{(3)}{}^{x_0}{}_{x_0} &= -72 (a_4')^{6} + 108 (a_4')^{5} u - 216 (a_4')^{4} u^{2} - 108 (a_4')^{4} v \\
&\quad - 648 (a_4')^{4} H^{2} - 432 (a_4')^{3} a_4'' u + 171 (a_4')^{3} u^{3} + 216 (a_4')^{3} u v \\
&\quad + 648 (a_4')^{3} u H^{2} + 324 (a_4')^{2} a_4'' u^{2} - \tfrac{81}{2} (a_4')^{2} u^{4} - 81 (a_4')^{2} u^{2} v \\
&\quad - 324 (a_4')^{2} u^{2} H^{2} - 216 (a_4')^{2} v H^{2} - 1944 (a_4')^{2} H^{4} - 54 a_4' a_4'' u^{3} \\
&\quad - 432 a_4' a_4'' u H^{2} + 81 a_4' u^{3} H^{2} + 216 a_4' u v H^{2} + 972 a_4' u H^{4} \\
&\quad + 108 a_4'' u^{2} H^{2} + \tfrac{27}{2} u^{4} H^{2} + 27 u^{2} v H^{2} - 324 u^{2} H^{4} \\
&\quad - 540 v H^{4} + 360 H^{6}
\end{aligned}
$$

$$
\begin{aligned}
E_{(3)}{}^{x_1}{}_{x_1} &= -72 (a_4')^{6} + 216 (a_4')^{5} u + 360 (a_4')^{4} a_4'' - 216 (a_4')^{4} u^{2} \\
&\quad - 108 (a_4')^{4} v - 648 (a_4')^{4} H^{2} - 432 (a_4')^{3} a_4'' u + 90 (a_4')^{3} u^{3} \\
&\quad + 108 (a_4')^{3} u v + 432 (a_4')^{3} u H^{2} + 162 (a_4')^{2} a_4'' u^{2} + 432 (a_4')^{2} a_4'' H^{2} \\
&\quad - \tfrac{27}{2} (a_4')^{2} u^{4} - 27 (a_4')^{2} u^{2} v - 216 (a_4')^{2} v H^{2} - 1944 (a_4')^{2} H^{4} \\
&\quad - 18 a_4' a_4'' u^{3} - 432 a_4' a_4'' u H^{2} - 54 a_4' u^{3} H^{2} + 108 a_4' u v H^{2} \\
&\quad + 1080 a_4' u H^{4} + 54 a_4'' u^{2} H^{2} + 360 a_4'' H^{4} + \tfrac{27}{2} u^{4} H^{2} \\
&\quad + 27 u^{2} v H^{2} - 216 u^{2} H^{4} - 540 v H^{4} + 360 H^{6}
\end{aligned}
$$

$$
\begin{aligned}
E_{(3)}{}^{x_4}{}_{x_4} &= 360 (a_4')^{6} - 540 (a_4')^{5} u + 270 (a_4')^{4} u^{2} + 648 (a_4')^{4} H^{2} \\
&\quad - 45 (a_4')^{3} u^{3} - 648 (a_4')^{3} u H^{2} + 1080 (a_4')^{2} H^{4} + 81 a_4' u^{3} H^{2} \\
&\quad - 540 a_4' u H^{4} - 270 u^{2} H^{4} + 2520 H^{6}
\end{aligned}
$$

$$
\begin{aligned}
E_{(3)}{}^{x_5}{}_{x_5} &= -72 (a_4')^{6} - 360 (a_4')^{4} a_4'' + 54 (a_4')^{4} u^{2} + 72 (a_4')^{4} v \\
&\quad - 648 (a_4')^{4} H^{2} + 288 (a_4')^{3} a_4'' u - 18 (a_4')^{3} u^{3} - 36 (a_4')^{3} u v \\
&\quad + 864 (a_4')^{3} u H^{2} - 54 (a_4')^{2} a_4'' u^{2} - 432 (a_4')^{2} a_4'' H^{2} - 324 (a_4')^{2} u^{2} H^{2} \\
&\quad - 1944 (a_4')^{2} H^{4} + 54 a_4' u^{3} H^{2} + 108 a_4' u v H^{2} + 864 a_4' u H^{4} \\
&\quad + 54 a_4'' u^{2} H^{2} - 360 a_4'' H^{4} - 162 u^{2} H^{4} - 360 v H^{4} \\
&\quad + 360 H^{6}
\end{aligned}
$$

The off-diagonal components are $E_{(k)}{}^{x_4}{}_{x_0} = \cot z\,u\,Q_{(k)}$ and $E_{(k)}{}^{x_0}{}_{x_4} = -\tan^2 z\,E_{(k)}{}^{x_4}{}_{x_0} = -\tan z\,u\,Q_{(k)}$ with

$$
\begin{aligned}
Q_{(1)} &= \tfrac{3}{2} H \\
Q_{(2)} &= -36 (a_4')^{2} H + 18 a_4' u H + \tfrac{3}{2} u^{2} H - 60 H^{3} \\
Q_{(3)} &= 540 (a_4')^{4} H - 540 (a_4')^{3} u H + 135 (a_4')^{2} u^{2} H + 648 (a_4')^{2} H^{3} \\
&\quad - 324 a_4' u H^{3} - 27 u^{2} H^{3} + 540 H^{5}
\end{aligned}
$$

so that $\sum_k\alpha_k E_{(k)}{}^{x_4}{}_{x_0} = \cot z\,u\,Q$ and $\sum_k\alpha_k E_{(k)}{}^{x_0}{}_{x_4} = -\tan z\,u\,Q$ with $Q = \sum_k\alpha_kQ_{(k)}$ (`offdiagonal_factorises` in both reports; formula key `offDiagonalFactor_Q` of `generalSource`).

The independent field equations (formula key `generalSource`):

- constraint ($x_4$): $\sum_k\alpha_k E_{(k)}{}^{x_4}{}_{x_4} + \Lambda = -\kappa\rho$; it contains $a_4'$ and $u$ but neither $a_4''$ nor $v$ nor $x_0$ (`constraint_first_order` in both reports);
- 3-space ($x_1 = x_2 = x_3$): $\sum_k\alpha_k E_{(k)}{}^{x_1}{}_{x_1} + \Lambda = \kappa p_3$;
- extra times ($x_5 = x_6 = x_7$): $\sum_k\alpha_k E_{(k)}{}^{x_5}{}_{x_5} + \Lambda = \kappa p_t$;
- hidden direction ($x_0$): $\sum_k\alpha_k E_{(k)}{}^{x_0}{}_{x_0} + \Lambda = \kappa p_0$;
- the off-diagonal pair: $\kappa q_{40} = \cot z\,u\,Q$ and $\kappa q_{04} = -\tan z\,u\,Q$;
- every other off-diagonal component: $0 = \kappa T^\mu{}_\nu$.

The 3-space minus extra-time combination and the hidden-direction equation are linear in $(a_4'', v)$, with a Jacobian $J$ whose determinant (formula key `secondOrderJacobianDet`) equals $-3$ in Einstein gravity; where $\det J \neq 0$ they determine $a_4''$ and $v = (b_4'/b_4)'$ from the source, while the constraint is first order (`second_order_system_a4pp_vv`, `second_order_system`). The remaining conditions:

- the identity of the combination 3-space plus extra times minus twice the hidden direction: $\sum_k\alpha_k\big(E_{(k)}{}^{x_1}{}_{x_1} + E_{(k)}{}^{x_5}{}_{x_5} - 2E_{(k)}{}^{x_0}{}_{x_0}\big) = \sum_k\alpha_k I_{(k)}$ with

$$
\begin{aligned}
I_{(1)} &= \tfrac{3}{4} u^{2} + \tfrac{1}{2} v \\
I_{(2)} &= -18 (a_4')^{2} u^{2} - 12 (a_4')^{2} v - 24 a_4' a_4'' u + 9 a_4' u^{3} \\
&\quad + 12 a_4' u v + 6 a_4'' u^{2} + \tfrac{3}{4} u^{4} + \tfrac{3}{2} u^{2} v \\
&\quad - 30 u^{2} H^{2} - 20 v H^{2} \\
I_{(3)} &= 270 (a_4')^{4} u^{2} + 180 (a_4')^{4} v + 720 (a_4')^{3} a_4'' u - 270 (a_4')^{3} u^{3} \\
&\quad - 360 (a_4')^{3} u v - 540 (a_4')^{2} a_4'' u^{2} + \tfrac{135}{2} (a_4')^{2} u^{4} + 135 (a_4')^{2} u^{2} v \\
&\quad + 324 (a_4')^{2} u^{2} H^{2} + 216 (a_4')^{2} v H^{2} + 90 a_4' a_4'' u^{3} + 432 a_4' a_4'' u H^{2} \\
&\quad - 162 a_4' u^{3} H^{2} - 216 a_4' u v H^{2} - 108 a_4'' u^{2} H^{2} - \tfrac{27}{2} u^{4} H^{2} \\
&\quad - 27 u^{2} v H^{2} + 270 u^{2} H^{4} + 180 v H^{4}
\end{aligned}
$$

  (`algebraic_identity_x1_plus_x5_minus_2x0`, `algebraic_identity`; formula key `identity_x1_plus_x5_minus_2x0`), so the field equations give $\kappa(p_3 + p_t - 2p_0) = \sum_k\alpha_k I_{(k)}$. Every term of $I_{(k)}$ contains $u$ or $v$; at constant $b_4$ (the withdrawn metric) the condition was $p_3 + p_t = 2p_0$, and on the background history with the author's weights the right-hand side vanishes again (below), so there the source must satisfy $p_3 + p_t = 2p_0$;
- $x_0$-dependence: since the diagonal left-hand sides do not depend on $x_0$, every diagonal component of $T^\mu{}_\nu$ must be independent of $x_0$, while the off-diagonal pair must have the $x_0$ dependence $\cot z\,u\,Q/\kappa$ and $-\tan z\,u\,Q/\kappa$: unless $uQ = 0$ the source needs an $x_0$-dependent off-diagonal pair (formula key `x0_dependence`);
- constraint propagation (Bianchi identity): $\frac{d}{dx_4}\sum_k\alpha_k E_{(k)}{}^{x_4}{}_{x_4} = 3a_4'\sum_k\alpha_k\big(E^{x_1}{}_{x_1} - E^{x_5}{}_{x_5}\big) + \tfrac32u\sum_k\alpha_k\big(E^{x_5}{}_{x_5} - E^{x_4}{}_{x_4}\big) + 6HuQ$ identically (`constraint_propagation_bianchi`, `bianchi_x4`); with the conservation law below the derivative of the constraint follows from the other components. The conservation components of a general source are $\nabla_\mu T^\mu{}_{x_4} = -\partial_4\rho - 3a_4'(p_3 - p_t) - \tfrac32u(\rho + p_t) + \partial_0 q_{04} - 6H\tan z\,q_{04}$ and $\nabla_\mu T^\mu{}_{x_0} = \partial_0 p_0 + 3H\cot z\,(2p_0 - p_3 - p_t) + \partial_4 q_{40} + \tfrac32u\,q_{40}$ (`conservation_components` in both reports).

For a prescribed history the equations give the source it requires (formula key `sourceRequiredByGivenHistory`); whether a state of the field supplies it is a separate question.

Einstein gravity ($\alpha_1 = 1$, $\alpha_2 = \alpha_3 = 0$; `einstein_components`; formula key `einstein`):

$$
\begin{aligned}
3 (a_4')^{2} - \tfrac{3}{2} a_4' u - \tfrac{3}{4} u^{2} + 21 H^{2} + \Lambda &= -\kappa\rho \\
-3 (a_4')^{2} + 3 a_4' u + a_4'' - \tfrac{3}{2} u^{2} - \tfrac{3}{2} v + 15 H^{2} + \Lambda &= \kappa p_3 \\
-3 (a_4')^{2} - a_4'' - \tfrac{3}{4} u^{2} - v + 15 H^{2} + \Lambda &= \kappa p_t \\
-3 (a_4')^{2} + \tfrac{3}{2} a_4' u - \tfrac{3}{2} u^{2} - \tfrac{3}{2} v + 15 H^{2} + \Lambda &= \kappa p_0 \\
\cot z\,(\tfrac{3}{2} u H) &= \kappa q_{40}
\end{aligned}
$$

The off-diagonal factor is $Q = \frac32H \neq 0$: a source without $T^{x_4}{}_{x_0}$ forces $b_4' = 0$, so with $b_4$ not constant Einstein gravity needs the $x_0$-dependent off-diagonal source $\kappa q_{40} = \frac32H\cot z\,u$ (`einstein_offdiagonal_forces_b4_constant`). The combination of the constraint and the hidden-direction equation gives $\kappa(\rho + p_0) = -6H^2 - 3(a_4')^2 - \tfrac34(u - 2a_4')^2 - \tfrac32v$, negative wherever $v \geq 0$, in particular on every exponential history: there the source must violate the null energy condition along the null direction $x_4 + x_0$ (`einstein_null_energy_x0`). There is no vacuum solution for $H > 0$ and any $\Lambda$: the off-diagonal equation forces $u = 0$, and then the $x_4$ and $x_0$ components give $36H^2 + 2\Lambda = 0$ and $6(a_4')^2 + 6H^2 = 0$ (`einstein_no_vacuum_solution`, `einstein_no_vacuum`). The second-order equations have the constant Jacobian $\begin{pmatrix}2 & -1/(2b_4)\\ 0 & -3/(2b_4)\end{pmatrix}$ with respect to $(a_4'', b_4'')$ (`einstein_second_order_system`); and $\kappa(p_3 + p_t - 2p_0) = \tfrac34u^2 + \tfrac12v$.

Exponential histories (formula key `exponentialHistory`). On $a_4 = AHx_4 + a_0$, $b_4 = b_4(0)\,e^{\beta AHx_4}$ ($a_4' = AH$, $u = \beta AH$, $a_4'' = v = 0$; 3-space scale factor $e^{AHx_4}$, extra-time scale factor $e^{-(1 - \beta/2)AHx_4}$) the field equations require constant $\rho$, $p_3$, $p_t$, $p_0$, in general with unequal pressures, and the off-diagonal pair $\kappa q_{40} = \cot z\,\beta AH\,Q(A, \beta)$, $\kappa q_{04} = -\tan z\,\beta AH\,Q(A, \beta)$, for any $\alpha_k$ and $\Lambda$ (`exponential_history_required_source`; formula key `requiredSource`). The required diagonal source contains $A$ only through $A^2$ and the off-diagonal pair is odd in $A$: the equations are invariant under $A \to -A$ (with $q_{40} \to -q_{40}$, $q_{04} \to -q_{04}$); whether the extra times deflate ($(1 - \beta/2)A > 0$) or inflate is a choice of sign (an initial condition) and is not selected by the equations. In Einstein gravity $\kappa q_{40} = \frac32\beta AH^2\cot z \neq 0$ whenever $\beta A \neq 0$ (`einstein_exponential_history_offdiagonal_source`).

The author's weights (formula key `authorWeights`): $\alpha_k = w_k/H^{2k}$ with $w = (1, \tfrac{1}{32}, \tfrac{1}{1152})$ and $\Lambda = -10$ in the convention of this record (the notebook's $\Lambda = 10$; `Dirac_Einstein-Lovelock_4+4_Nash.nb`, Out[134] and Out[135]). Then

$$
Q(A, \beta) = \frac{3}{128H}\,\big(5 A^{4} \beta^{2} - 20 A^{4} \beta + 20 A^{4} + A^{2} \beta^{2} + 12 A^{2} \beta - 24 A^{2} + 4\big)
$$

and at $A = 1$, $Q = 3\beta(3\beta - 4)/(64H)$: a source without $T^{x_4}{}_{x_0}$ is possible exactly for $\beta = 0$ ($b_4$ constant, excluded) and $\beta = \tfrac43$ (`author_weights_branch`), that is on the history

$$
a_4 = Hx_4,\quad b_4 = b_4(0)\,e^{(4/3)Hx_4}
$$

of SPEC section 1, on which the extra times still deflate exponentially, with the scale factor $e^{-a_4}b_4^{1/2} \propto e^{-a_4/3}$. On it the field equations require, at $H = 1$, the constant source

$$
\kappa(\rho, p_3, p_t, p_0) = \big(-\tfrac{2}{27}, -\tfrac29, -\tfrac{22}{27}, -\tfrac{14}{27}\big),\qquad q_{40} = q_{04} = 0
$$

(`author_weights_history_source`): a negative energy density for $\kappa > 0$, with $p_3/\rho = 3$, $p_t/\rho = 11$, $p_0/\rho = 7$ and $p_3 + p_t = 2p_0$. It is not a vacuum solution, and the record uses it as a PRESCRIBED background. With the author's weights an exponential history is a vacuum solution exactly for $\beta = 0$ ($b_4$ constant: the withdrawn metric) and $A = \pm1$; none with $b_4$ not constant is (`author_weights_no_vacuum_with_b4_not_constant`; that every vacuum solution of the author's equations has $b_4$ constant is proved in `Revision/metric_b4/results/vacuum-b4.json`). In Einstein-Gauss-Bonnet gravity ($\alpha_1 = 1$, $\alpha_3 = 0$) the vacuum exponential histories with $b_4$ not constant are exactly $\beta = 4$ with $\alpha_2 = 1/(40H^2(1 - A^2))$ and $\beta = 2(1 + A^2)/A^2$ with $\alpha_2 = -A^2/(4H^2(A^2 - 1)^2) < 0$ ($A^2 \neq 1$): tuned couplings (`egb_exponential_vacuum_branches`).

Specialisation to dirac16complex. The source is the energy-momentum tensor of section 9 with the declared sign $\sigma_T = +1$ (formula key `emtConvention` of `fields`: $T^\mu{}_\nu = \sigma_T(-K^{(\mu}{}_{\nu)} + \delta^\mu_\nu\mathcal{L}_0)$, the convention $\rho = -T^{x_4}{}_{x_4}$ of SPEC section 4; the relative sign of the gravitational and matter actions is carried as the parameter $\sigma_T$ in the field-equations record and is not fixed by a Revision check). For the quantised field every bilinear is replaced by the expectation value of its normal-ordered operator in the state (section 12), with $k_\mu = K_\mu$:

$$
\begin{aligned}
\rho &= \langle{:}k_4{:}\rangle - \langle{:}\mathcal{L}_0{:}\rangle, & p_3 &= \langle{:}\mathcal{L}_0{:}\rangle - \langle{:}k_1{:}\rangle, \\
p_t &= \langle{:}\mathcal{L}_0{:}\rangle - \langle{:}k_5{:}\rangle, & p_0 &= \langle{:}\mathcal{L}_0{:}\rangle - \langle{:}k_0{:}\rangle,
\end{aligned}
$$

and the equations become (entry `dirac16complex` of the formula key `fields` of the field-equations record):

- constraint: $\sum_k\alpha_k E_{(k)}{}^{x_4}{}_{x_4} + \Lambda = -\kappa\big(\langle{:}k_4{:}\rangle - \langle{:}\mathcal{L}_0{:}\rangle\big)$;
- second-order equations: the 3-space minus extra-time combination with $\kappa(p_3 - p_t) = \kappa\big(\langle{:}k_5{:}\rangle - \langle{:}k_1{:}\rangle\big)$, and the hidden-direction equation $\sum_k\alpha_k E_{(k)}{}^{x_0}{}_{x_0} + \Lambda = \kappa\big(\langle{:}\mathcal{L}_0{:}\rangle - \langle{:}k_0{:}\rangle\big)$;
- the identity: $\kappa\big(2\langle{:}k_0{:}\rangle - \langle{:}k_1{:}\rangle - \langle{:}k_5{:}\rangle\big) = \sum_k\alpha_k I_{(k)}$;
- the off-diagonal pair: $-\sigma_T\langle{:}K^{(x_4}{}_{x_0)}{:}\rangle = \cot z\,u\,Q/\kappa$ (and its partner); every other off-diagonal expectation value $\langle{:}T^\mu{}_\nu{:}\rangle$, $\mu \neq \nu$, must vanish, and every diagonal expectation value must be independent of $x_0$. For a homogeneous configuration the off-diagonal components are multiples of the 15 three-gamma bilinears $\bar\Psi\gamma^{(a)}\gamma^{(b)}\gamma^{(c)}\Psi$ with $\{a, b, c\} = \{i, 4, 0\}$ ($i = 1, 2, 3, 5, 6, 7$) and $\{i, 4, j\}$ ($i = 1, 2, 3$, $j = 5, 6, 7$), with coefficients depending on $H$, $a_4'$ and $u$, derived for the classical homogeneous condensate (`condensate_offdiagonal_are_three_gamma_bilinears`, `authorT16_condensate_offdiagonal_three_gamma`); for dirac16complex their expectation values must vanish.

**Statement (sources of the homogeneous form).** The classical homogeneous condensate of the field-equations record has, on shell, $K^{x_4}{}_{x_4} = (m + U')S$, $K^\mu{}_\mu = 0$ for every other direction and $K^{x_4}{}_{x_0} = 0$ (`condensate_kinetic_tensor_diagonal`), hence $\rho = mS + U$, $p_3 = p_t = p_0 = SU' - U$ and $q_{40} = q_{04} = 0$, with $b_4^{3/2}S$ constant (`condensate_S_b4_three_halves_constant`). A source of this form (equal pressures and no $T^{x_4}{}_{x_0}$) with $b_4$ not constant is impossible in Einstein gravity (the off-diagonal equation forces $b_4' = 0$); with the author's weights it is supplied on no exponential history with $\beta \neq 0$ ($Q = 0$ and equal pressures have no common real solution); in Einstein-Gauss-Bonnet gravity only on the two tuned vacuum branches above; histories that are not exponential are not decided (`condensate_source_with_b4_not_constant` in both reports). A state of dirac16complex whose normal-ordered expectation values depend on $x_4$ only, have $\langle{:}k_\mu{:}\rangle = 0$ for $\mu \neq x_4$ and vanishing off-diagonal expectation values gives a source of the same form, so the same conclusions apply to it: the field equations contain the state only through $\rho$, $p_3$, $p_t$, $p_0$, $q_{40}$ and $q_{04}$. If in addition the operator form of the on-shell identity of section 12 holds (an assumption for $\lambda \neq 0$), then $\rho = \langle{:}mS + U{:}\rangle$ and $p = \langle{:}SU' - U{:}\rangle$.

What $a_4$ and $b_4$ the equations allow, in summary: for a prescribed history the equations fix the required source (the diagonal entries above, every one independent of $x_0$, and the $x_0$-dependent off-diagonal pair $\cot z\,u\,Q/\kappa$), and whether a state of dirac16complex supplies it is a separate question; a source without $T^{x_4}{}_{x_0}$ and with $b_4$ not constant needs $Q = 0$ at every instant, which is impossible in Einstein gravity and, with the author's weights and $a_4' = H$, fixes $u = \tfrac43H$, the background history. The Kohn-Sham states computed in `Revision/kohn_sham/` (along that history) are not an admissible source (`Revision/field_equations_a4/reports/ks-source-conditions.json`): every recorded state with a nonzero energy-momentum tensor depends on $x_0$, which the equations exclude for every $a_4$ and $b_4$ (`ks_profiles_depend_on_x0`); on the history, where the condition reads $p_3 + p_t = 2p_0$, they violate it pointwise and also after integration over $x_0$ (for $N = 136$, $\lambda = 0$ the ratio $(\int p_3 + \int p_t)/(2\int p_0)$ is 0.339767, 0.25969 and 0.239714 at $a_{4,0} = 0$, 1, 2, where the equations require 1; `ks_profiles_violate_algebraic_condition`, `ks_integrals_violate_algebraic_condition`); and the history needs the constant source of negative energy density above, while the Kohn-Sham gas has a positive energy density that changes along the history (`ks_history_is_a_prescribed_background`). The off-diagonal condition holds there: $Q = 0$ on the history and the Kohn-Sham states have no $T^{x_4}{}_{x_0}$ (`ks_offdiagonal_condition_on_history`). The Kohn-Sham history $a_4 = Hx_4$, $b_4 = b_4(0)e^{(4/3)Hx_4}$ is therefore a prescribed test-field background without back-reaction.

**The field equations for $a_4$ and $b_4$ with the Kohn-Sham source (`Revision/field_equations_a4/ks_source`).** A separate analysis (Python: 22 of 22 checks pass) makes the last statement exact and asks what the equations would do with the Kohn-Sham source. Exact: the $x_1 + x_5 - 2x_0$ combination reads $\kappa(p_3 + p_t - 2p_0) = I(a_4', a_4'', u, v)$ with $I = 0$ on the background history with the author's weights but not for general $b_4$ (`A1_x1_x5_x0_combination_with_b4`); the off-diagonal equation needs $Q(a_4', u) = 0$ at every instant of a history with $b_4$ not constant, because no Kohn-Sham state has $T^{x_4}{}_{x_0}$; in Einstein gravity $Q = \frac32H$, so there is no history with $b_4$ not constant and a Kohn-Sham source (`A2_offdiagonal_equation_needs_Q_zero`); at $a_4' = H$ the real roots of $Q(H, u) = 0$ are $u/H = 0$ and $\tfrac43$ for the author's weights, two negative roots for the stated Gauss-Bonnet coupling, and none for Einstein gravity and the stated cubic Lovelock case (`A6_branches_at_the_initial_rate`). In the Kohn-Sham coordinate $y$ the conservation law along $x_0$ gives $p_3 + p_t - 2p_0 = \partial_y p_0/(3H)$ on shell for every $b_4$ (`A5_x0_conservation_in_y`), and the recorded states obey that conservation law (`B2_x0_conservation_on_every_profile`), so their violation of the condition is exactly the $x_0$ dependence of $p_0$; at least a share 0.582938 of the energy density deviates from its hidden-direction average (L1 measure; `B4_hidden_direction_mismatch`). After averaging over the hidden direction the relative defect of the $x_1 + x_5 - 2x_0$ moment on the history stays between 0.411101 and 0.806379 over the 70 nonzero states (`C1_averaged_algebraic_condition_fails`), and the $x_4$ moment of the author's equations would need $\kappa\bar\rho = -\tfrac{2}{27}$ at every slice, while the averaged energy density of every series with a nonzero source changes along the history by a factor between 336.374 and 2966.92 (`C3_record_history_not_a_solution_of_the_x4_moment`). The coupled problem therefore has no solution, and nothing about $a_4$ or $b_4$ is derived from it. In a stated approximation (the $x_4$ moment and the off-diagonal equation kept, two algebraic equations for $a_4'$ and $u$; the other moments dropped, with residuals of order one, `D4_dropped_moments_residuals`), integrated for the free gas from $a_4'(0) = H$, the Kohn-Sham source does not start or select exponential deflation of the extra times: the initial rate and the branch of $Q = 0$ are initial data, and $\Lambda$ (or the source strength) is fixed by the constraint. With the author's weights and $\Lambda = -10$ the start on the background history needs $\kappa\bar\rho(0) = -\tfrac{2}{27}H^2$, that is $\kappa < 0$ for this gas of positive energy density (`C4_source_signs`): a negative gravitational coupling in the sign convention $\sigma_T = +1$ of the field-equations record; as the gas dilutes, the solution leaves the history and reaches a fold of the algebraic system at $a_4 = 0.024$, with $a_4'/H = 0.870762$ and $u/H = 1.09136$ there for $N = 136$, $\lambda = 0$ (on the history 1 and $\tfrac43$; `D2_author_weights_start_on_the_record_history`); what follows the fold is not computed. With the stated Gauss-Bonnet coupling ($\alpha_2H^2 = \tfrac{1}{80}$) the 28 integrated cases end regular at $a_4 = 2$ (8 cases), at a fold (12) or where the adiabaticity measure reaches 1 (8), after which the instantaneous Kohn-Sham states are no longer a valid source (`D5_outcomes`, `D6_adiabaticity_along_the_solutions`).

## 14. Relation to the pairing theorems

The pairing theorems of SPEC section 9 use the Lagrangian, the field equations and the energy-momentum tensor of this document; their full statements, hypotheses and limits are in `Revision/docs/PAIR_CREATION_PROOFS.md`. For dirac16complex, in brief:

- T1 (chirality): $\mathcal{L}_{m,\lambda}[\Gamma\Psi] = -\mathcal{L}_{-m,-\lambda}[\Psi]$, solutions of the $(m, \lambda)$ equations are mapped to solutions of the $(-m, -\lambda)$ equations, $T \to -T$ and $J \to -J$, in every gravitational field, the metric with $b_4$ included; the total energy-momentum and the total current of the pair vanish identically (Wolfram `T1_Lagrangian_primordial_grassmann` and `T1_energy_momentum_primordial_grassmann`, sympy `T1.metric.grassmann.pair_total_emt_zero`).
- T2 (chirality combined with a Pin(4,4) reflection of character $-1$, the mirror $z \to \pi - z$ across the assumed Z2 brane): $(m, \lambda) \to (-m, \lambda)$, $\mathcal{L} \to +\mathcal{L}$, with equal, not opposite, energy-momentum (`T2_mirror_Lagrangian_grassmann`, `T2_mirror_energy_momentum_and_current_grassmann`; sympy `T2.metric.grassmann.emt`).
- Quantum reading: the chirality image $\Gamma\Psi$ carries the Krein metric $-B$; there is no cancellation between two independently quantised universes (`Q_Krein_metric_of_images`, `Q_no_identification_of_independent_universes`; sympy `Q.no_cancellation_independent_universes`).
- T3 (the Kohn-Sham level): the block map of $\Gamma$ with the brane parities exchanged and the tip angle $\theta \to \pi - \theta$ maps every self-consistent instantaneous Kohn-Sham state with $(m, \lambda, \theta)$ onto one with $(-m, +\lambda, \pi - \theta)$, with equal levels, occupations, Kohn-Sham energies and energy-momentum profiles, and $S \to -S$; the Z2 brane is ASSUMED (`T3_energies_and_emt_profiles_equal`, `T3_exact_k0_spectra`; sympy `T3.energies_and_emt_profiles_equal`).
- Completion of T3 (2026-10-08): with the expectation rule of the canonical quantisation (section 11) the image state has $\rho' = -\Gamma\rho\Gamma$, so $n$ is unchanged, $S$ and $Q$ change sign, and every component of the 16-component energy-momentum tensor and of the current of the $(-m, +\lambda)$ image state equals that of the original state (statement S6; `T3C_krein_rule_16_component`, sympy `T3C.krein_rule_16_component`); the filling convention of the $+m$ member is carried onto the $-m$ member (`T3C_filling_convention_mapped`). Two numerical demonstrations on the background history with $b_4$, with the Rust solver (210 states) and with the independent reference solver (18 states), are demonstrations, not proofs.

These are correspondences between solutions; no creation process, rate or amplitude follows from them (`not_established` in the sympy pairing report, in the T3 record and in the completion record).

## 15. What this document does not claim

- It derives no creation process, rate or amplitude for universes, and no statement that universes of masses $+m$ and $-m$ are created in pairs; the pairing theorems (section 14) map solutions to solutions.
- Non-triviality [1] is a statement about the Euler-Lagrange equations in the author's metric with $H > 0$; it is not a statement about observable effects of the gravitational term. The value $\gamma^\mu\Omega_\mu = 3H\gamma^{(0)} + \tfrac34u\,\gamma^{(4)}$ belongs to the diagonal vielbein and to the field variables $\Psi$: its $H$ part vanishes identically in the frame boosted in the $(x_0, x_4)$ plane with rapidity $6Hx_4 + b_0$ (no boost in this plane removes its $b_4'$ part), and the rescaling $\Psi = b_4^{-3/4}\sin^{-1/2}z\,\chi$ removes all of it; the canonical connection drops out of $\mathcal{L}$, and the deflation $a_4$ makes no contribution to $\gamma^\mu\Omega_\mu$. What is frame-independent is that $\Omega_\mu$ vanishes in no frame (curvature $R^{x_0}{}_{x_0} = -6H^2$), together with the vielbein factors of the derivative terms (section 7, Remarks). That the term is "not cosmetic" is not claimed; its role for the Hermiticity of the mode operator depends on the measure and the variables (an interpretation).
- The quantisation recorded here is: the canonical anticommutator, the theorem that it forces a Krein structure when $\Psi^\dagger$ is realised as the Hilbert adjoint, the formal Krein self-adjointness of the evolution (up to the boundary term at $z = \pi/2$), and positive Fock realisations checked for single good-sector momenta with frozen coefficients. A positive-norm Hilbert space for the full field, a stable vacuum in the presence of the growing extra-time modes, and the interacting ($\lambda \neq 0$) operator theory beyond the finite model of section 12 are not constructed. In flat 4+4 space every eigenspace of REAL frequency of the one-particle generator has Krein inertia (4,4) (`Q_one_particle_Krein_signatures`, `Q.one_particle_Krein_inertia`, proved for every real frequency in `Q_one_particle_Krein_inertia_real_frequencies` and `Q.one_particle_Krein_inertia_proof`), and every eigenspace of imaginary or zero frequency is Krein-neutral (`Q_one_particle_complex_and_zero_frequencies_Krein_neutral`). In flat space the good-sector restriction removes the complex frequencies, not the indefiniteness of the real-frequency eigenspaces; in the curved good sector without a boundary condition at $z = \pi/2$ complex frequencies remain (section 11).
- Boundary conditions: none is imposed at $z = \pi/2$ in this record. The Hermiticity of the curved good-sector mode operator and the conservation of the Krein form hold up to the boundary term there; with no boundary condition the good sector contains growing $x_0$-independent modes (for $U = 0$ whenever $m^2 < 9H^2$).
- No well-posed Cauchy problem is claimed: the slices $x_4 = $ const are non-characteristic, but for data that depend on the extra times the growth rates are unbounded (Hadamard ill-posedness).
- The normal-ordered operator form of the on-shell trace identity for $\lambda \neq 0$ is an assumption of the field-equations record. It is verified only in the finite model of section 12 (one good-sector plane-wave mode set with frozen coefficients, record `Revision/theory/fock_quartic/`), where it holds as an exact operator identity if and only if the potential and the energy-momentum tensor are both Wick ordered and fails for every other tested ordering already in expectation values; for the field on a whole slice, the curved $x_0$ dependence and the extra-time sector it is not verified, and symmetry and conservation of the quartic operator are not verified. No numerical expectation value of the energy-momentum tensor operator for a physical many-fermion state is computed in this document (the finite model gives only its exact values on the occupation states of one mode set); the Kohn-Sham quantities it quotes, in section 13 (the source-condition ratios, the relative defects and the runs of the approximation of the $a_4$ and $b_4$ equations with the Kohn-Sham source) and in this section (the equation-of-state values $w_{\rm eff}$ of the Kohn-Sham gas from the dark-sector record, below), are computed from Kohn-Sham expectation values.
- The relative sign $\sigma_T$ between the gravitational and the matter side of the field equations is a declared convention ($\sigma_T = +1$), not derived.
- No solution $a_4(x_4)$, $b_4(x_4)$ with a dirac16complex source is computed here beyond the statements of section 13; it is not claimed that any state of dirac16complex supplies a source that satisfies all the conditions of section 13 (in Einstein gravity, with $b_4$ not constant, such a source must have the $x_0$-dependent off-diagonal component $\kappa q_{40} = \frac32H\cot z\,u$ and must violate the null energy condition along $x_4 + x_0$ wherever $(b_4'/b_4)' \geq 0$). The recorded Kohn-Sham states fail the conditions (section 13), and the background history $a_4 = Hx_4$, $b_4 = b_4(0)e^{(4/3)Hx_4}$ is a prescribed background without back-reaction; the equations do not select deflation over inflation of the extra times.
- The equation of state seen by a 3-space observer and its time dependence are not derived in this document; Hypothesis (dirac16complex as a mechanism for a time-varying dark-energy or dark-matter equation of state) is investigated in `Revision/docs/DARK_SECTOR_HYPOTHESES`, on the background history with $b_4$. Its verdict for dirac16complex, under its stated observer assumption (three definitions (A), (B), (C) of the 4-dimensional density, which on this history differ by exactly 1/3): a time-varying dark-matter-like equation of state ($w_{\rm eff}$ falling from 1/3 toward 0 under (A) and (B)) is present in the theory for quanta of the massive bulk band, which the computed ground states do not populate; the computed Kohn-Sham gas is radiation-like; dark energy is not found: under (C) the gas has $w_{\rm eff}$ between -0.040541 and -0.006532, close to 0, only a drifting condensate gives negative values, with a strongly thawing slope, no Kohn-Sham state comes near the Unite pair $(w_0, w_a) = (-0.861, -0.60)$ or crosses $w = -1$, and a drifting $\lambda < 0$ condensate crosses $-1$ toward the past; the Unite numbers are not reproduced. That record establishes neither Hypothesis nor Hypothesis00.
- $H = 0$ is a degenerate limit, not a member of the family; the surface $z = \pi/2$ is degenerate ($g_{00} = 0$, $\sqrt{|g|} = 0$); nothing is claimed there.
- The earlier metric with $b_4 = 1$ is withdrawn; no statement of this document is restricted to it, and its formulas are not results of this record (they are the values of the formulas above at $u = v = 0$, a case the record excludes).
- The comparison record of the field-theory branch agrees entirely (section 1); every formula is nevertheless cited by the separate checks of the two engines.

## 16. Reproduction

From the repository root (each verifier writes its outputs to the paths listed in section 1; the Wolfram verifier of each part runs first because the sympy verifier compares with its output at the end; every calculation stays below the limit of 7 min 3 s for one run):

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
wolframscript -file Revision/pairing/kohn_sham/wolfram/verify_t3.wls
python Revision/pairing/kohn_sham/python/check_t3.py
python Revision/field_equations_a4/python/check_ks_source_conditions.py
python Revision/field_equations_a4/ks_source/ks_source_a4.py
wolframscript -file Revision/pairing/kohn_sham/wolfram/verify_t3_completion.wls
python Revision/theory/fock_quartic/check_fock_quartic.py
```

The Wolfram field-theory verifier runs in six parts and a merge; on 2026-10-15 they took 35 s, 156 s, 108 s, 34 s, 51 s, 11 s and 5 s, the scope verifier 29 s, and the sympy checker 209 s for its part `--part nonlinear` (the nonlinear homogeneous solutions, written to a git-ignored part file that the full run reads only if its inputs are unchanged) and 128 s for the full run (`Revision/theory/wolfram/WOLFRAMSCRIPT_PROVENANCE.md`, section 6.9). The analysis of the $a_4$ and $b_4$ equations with the Kohn-Sham source re-derives the source-conditions report, so it runs after that checker (about 2 s); the checker of the finite Fock model for $\lambda \neq 0$ (it reads only `Revision/algebra/gammas.json`) ran in 6.7 s by its README. The sympy completion checker reads the reports of the two numerical demonstrations, so it runs after them, in the order given in section 10 of `Revision/docs/PAIR_CREATION_PROOFS`; the programs of the dark-sector record are listed in section 12 of `Revision/docs/DARK_SECTOR_HYPOTHESES`.

The sympy field-theory checker exits with an error if its comparison with the Wolfram record does not agree entirely. It can write its report to another path, which leaves the recorded report untouched:

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

The test checks that the .tex is the builder output of the .md, that the registered PDF is the PDF file next to it, that every cited check exists and passes in the reports, that the quoted check counts are those of the reports, that the component field equations and the Lovelock, Einstein and off-diagonal formulas of section 13 are the output of its renderers applied to `Revision/theory/field-theory.json` and `Revision/field_equations_a4/a4-equations.json` (and that their sums over $k$ equal the general formulas there), and that the hand-written formulas of sections 2 and 4 equal the formula file.

## 17. Index of formulas and checks

| formula | section | Wolfram checks | sympy checks |
| --- | --- | --- | --- |
| metric with $b_4$, vielbein, volume element $b_4^{3/2}\cos z$ | 2 | `metric_is_the_authors`, `sqrt_det_g` | `metric_from_vielbein_equals_SPEC`, `sqrt_det_g_equals_b4_cos_z` |
| Christoffel symbols, Ricci tensor (with $R^{x_4}{}_{x_0}$), curvature | 2 | `christoffel_count`, `ricci_mixed_components`, `ricci_scalar`, `never_flat_for_H_positive` | `christoffel_symmetric_metric_compatible`, `curvature_nonzero_flat_only_formally` |
| Clifford algebra, C, Gamma, B | 3 | `Clifford_relation`, `C_gamma_real_antisymmetric`, `Gamma_diag`, `B_signature_8_8` | `clifford_relation`, `C_conjugation`, `chirality_diag`, `B_hermitian_involution_signature` |
| Pin(4,4) irreducible; Spin(4,4): two inequivalent 8-dimensional irreducible halves | 3 | `Pin44_irreducible_commutant_dim_1`, `chiral_halves_irreducible`, `chiral_halves_inequivalent_intertwiners_0` | `pin_commutant_dimension_1`, `spin_halves_irreducible`, `spin_halves_inequivalent` |
| canonical spin connection, covariant constancy | 4 | `vielbein_postulate`, `omega_components`, `Omega_components`, `gamma_covariantly_constant` | `vielbein_postulate`, `Omega_x0_and_Omega_x4_vanish`, `covariant_constancy_D_mu_gamma_nu`, `spinor_connection_real` |
| gravitational term $3H\gamma^{(0)} + \tfrac34u\,\gamma^{(4)}$ (diagonal frame) and its square | 4, 7 | `gammaOmega_total`, `gammaOmega_per_direction`, `gammaOmega_divergence_form` | `gamma_mu_Omega_mu_equals_3H_gamma_x0_plus_b4_term`, `a4_time_terms_cancel_b4_terms_add`, `gravity_term_square` |
| frame and variable dependence of the term; frame-independent content | 4, 7 | `boosted_frame_gammaOmega_formula`, `boosted_frame_removes_only_the_H_term`, `boosted_frame_curvature_nonzero`, `rescaling_removes_the_connection_term`, `connection_free_lagrangian_same_equations` | `boosted_frame_gammaOmega_formula`, `boosted_frame_removes_only_the_H_term`, `rescaled_equation_quadratic_potential`, `gammaOmega_blind_to_the_deflation`, `spin_connection_in_the_energy_momentum_tensor` |
| Lagrangian: reality, total divergence | 5 | `L_real_G`, `L_total_divergence_to_unsymmetrised_G` | `grassmann_lagrangian_real`, `grassmann_total_divergence_relation` |
| Majorana-type negative control | 5 | `Majorana_Lg_total_derivative_grassmann` | `negative_control_majorana_grassmann_total_derivative` |
| Euler-Lagrange equations, explicit form | 6 | `EL_Psibar_G`, `EL_Psi_G`, `Dirac_operator_explicit_G`, `evolution_form_G`, `block_form` | `grassmann_euler_lagrange_psibar_variation`, `grassmann_euler_lagrange_psi_variation` |
| non-triviality [1] | 7 | `nontriviality_1_dirac16complex`, `Omega_vanishes_iff_a4prime_b4prime_and_H_vanish`, `spin_curvature_equals_Riemann` | `nontriviality_Omega_zero_iff_flat`, `spinor_curvature_equals_riemann`, `gravity_term_square` |
| self-consistency | 8 | `adjoint_equation_is_Dirac_conjugate_G`, `Lichnerowicz_identity_G`, `current_conservation_identity_G`, `Noether_identity_diffeomorphisms_G`, `Noether_identity_local_Lorentz_G` | `grassmann_adjoint_equation_is_conjugate`, `lichnerowicz_identity_on_fields`, `grassmann_current_conservation`, `grassmann_emt_conservation_on_shell` |
| exact solutions with the factor $b_4^{-3/4}$ | 8, 10 | `exact_solution_x4_x0_G`, `exact_solution_nonlinear_homogeneous_G` | `exact_solution_family_x4_x0`, `exact_nonlinear_homogeneous_solution` |
| energy-momentum tensor | 9 | `T_vielbein_variation_closed_form_G`, `T_symmetric_part_Belinfante_G`, `T_diagonal_components_G`, `T_x4_x0_component_G`, `EMT_trace_G` | `grassmann_emt_equals_general_vielbein_variation_on_shell`, `grassmann_emt_symmetric`, `grassmann_trace_on_shell` |
| energy density, pressures, equations of state, energy exchange with the $b_4'$ term | 9, 10 | `kinetic_sum_on_shell_G`, `exact_solution_nonlinear_homogeneous_G`, `energy_exchange_equation` | `grassmann_homogeneous_on_shell_rho_p`, `energy_exchange_equation` |
| canonical quantisation, Krein structure | 11 | `canonical_momentum`, `first_order_form_and_anticommutator`, `no_positive_inner_product`, `Krein_form_conserved_curved`, `good_sector_hermiticity_curved`, `Q_one_particle_Krein_inertia_real_frequencies` | `canonical_anticommutator_B`, `no_positive_inner_product`, `good_sector_spectrum_and_B_sectors`, `Q.one_particle_Krein_inertia_proof`, `Q.one_particle_complex_frequency_Krein_neutral` |
| boundary term at z = pi/2, growing modes, ill-posedness | 8, 11 | `good_sector_hermiticity_up_to_the_brane_flux`, `good_sector_x0_independent_modes_without_boundary_condition` | `extra_time_growth_rates_unbounded` |
| Fock space, normal ordering, expectation values | 11, 12 | `Fock_space_good_sector_example`, `mode_hamiltonian_Krein_selfadjoint` | `good_sector_positive_fock_realisation`, `expectation_value_rule`, `extra_time_modes_grow` |
| energy-momentum tensor operator for $\lambda \neq 0$ in a finite Fock model | 12 | | `trace_identity_operator_identity_wick`, `trace_identity_fails_for_every_other_combination`, `homogeneous_rho_p_operator_identities_wick`, `negative_control_free_dynamics` (Python) |
| field equations for $a_4$ and $b_4$ | 13 | `lovelock_depends_on_b4_through_u_and_v`, `offdiagonal_factorises`, `second_order_system_a4pp_vv`, `algebraic_identity_x1_plus_x5_minus_2x0`, `constraint_propagation_bianchi` | `offdiagonal_factorises`, `second_order_system`, `algebraic_identity`, `bianchi_x4`, `json_lovelock_components` |
| Einstein gravity | 13 | `einstein_components`, `einstein_offdiagonal_forces_b4_constant`, `einstein_null_energy_x0`, `einstein_no_vacuum_solution` | `einstein_components`, `einstein_null_energy_x0`, `einstein_no_vacuum` |
| exponential histories, the author's weights, the background history | 13 | `exponential_history_required_source`, `author_weights_branch`, `author_weights_history_source`, `author_weights_no_vacuum_with_b4_not_constant`, `egb_exponential_vacuum_branches` | `exponential_history_required_source`, `author_weights_branch`, `author_weights_history_source`, `author_weights_no_vacuum_with_b4_not_constant`, `egb_exponential_vacuum_branches` |
| sources of the homogeneous form | 13 | `condensate_kinetic_tensor_diagonal`, `condensate_S_b4_three_halves_constant`, `condensate_source_with_b4_not_constant` | `authorT16_condensate_kinetic_diagonal`, `condensate_source_with_b4_not_constant` |
| the Kohn-Sham states as a source | 13 | | `ks_profiles_depend_on_x0`, `ks_integrals_violate_algebraic_condition`, `ks_history_is_a_prescribed_background`, `ks_offdiagonal_condition_on_history` (Python) |
| the $a_4$ and $b_4$ equations with the Kohn-Sham source | 13 | | `A1_x1_x5_x0_combination_with_b4`, `A2_offdiagonal_equation_needs_Q_zero`, `A5_x0_conservation_in_y`, `B2_x0_conservation_on_every_profile`, `C1_averaged_algebraic_condition_fails`, `C3_record_history_not_a_solution_of_the_x4_moment`, `D2_author_weights_start_on_the_record_history`, `D5_outcomes` (Python) |
| completion of T3 (S6, filling convention) | 14 | `T3C_krein_rule_16_component`, `T3C_filling_convention_mapped` | `T3C.krein_rule_16_component`, `T3C.filling_convention_mapped` |
| pairing (section 14) | 14 | `T1_Lagrangian_primordial_grassmann`, `T2_mirror_Lagrangian_grassmann`, `Q_Krein_metric_of_images`, `T3_energies_and_emt_profiles_equal` | `T1.metric.grassmann.lagrangian`, `T2.metric.grassmann.emt`, `Q.no_cancellation_independent_universes`, `T3.energies_and_emt_profiles_equal` |
