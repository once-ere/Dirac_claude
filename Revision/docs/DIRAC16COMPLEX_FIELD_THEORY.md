# dirac16complex in the author's primordial gravitational field

## Lagrangian, covariant field equations, non-triviality [1], energy-momentum tensor operator, equations of state and the field equations for a4[x4] and b4[x4] (Revision record)

## Abstract

This document records, for the fermion field dirac16complex coupled to the author's primordial gravitational field, the Lagrangian, its coupling through the canonical spin connection, the exact covariant field equations (Euler-Lagrange) written out component by component, the non-triviality test [1] with its proof, the self-consistency of the field equations, the energy-momentum tensor (as a Grassmann-algebra expression and as a normal-ordered operator after canonical quantisation in 4 + 4 dimensions, with the Krein structure that this quantisation forces), the kinetic and potential energy, the energy density, the pressures and the equations of state, and the Einstein-Lovelock field equations for a4[x4] and b4[x4] with dirac16complex as the source. The metric is the corrected metric of 2026-10-16 (version 2; `Revision/SPEC.md` section 1): $g = \mathrm{diag}\big(e^{-2a_4}b_4\cot^2 z,\ e^{2a_4}\,(\times3),\ -1,\ -e^{-2a_4}b_4(\sin^2 z)^{1/6}\,(\times3)\big)$, $z = 6Hx_0$ real, with two functions $a_4(x_4)$ and $b_4(x_4) > 0$ of the time; every identity is proved for general $a_4$ and $b_4$ and every real $z$, while the values quoted on the background history and the numerical Kohn-Sham and dark-sector statements of sections 13 and 15 refer to the prescribed background history and the states computed on it ($b_4$ is never 1; the metric of 2026-10-14 is withdrawn). Every formula is an output of Revision code (a WolframScript verifier and, for most statements, an independent sympy verifier) and is listed with the names of the checks that verify it. The main exact results are: in the diagonal vielbein the spin-connection term of the field equation is $\gamma^\mu\Omega_\mu = c_g\gamma^{(0)} + v_g\gamma^{(4)}$ with $c_g = \tfrac32He^{a_4}b_4^{-1/2}$ and $v_g = b_4'/b_4 - \tfrac12a_4'$, for every $a_4$ and $b_4$ (the hidden direction and the three extra times share the rate $h_4 = b_4'/(2b_4) - a_4'$, the extra times carry the hidden-direction terms), with the square $(c_g^2 - v_g^2)I_{16}$; this value belongs to the diagonal frame and to the field variables $\Psi$ (a frame boosted in the $(x_0, x_4)$ plane removes its $c_g$ part, no such boost removes its $v_g$ part, and the rescaling $\Psi = e^{a_4/2}b_4^{-1}(\sin^2 z)^{-1/8}\chi$ removes all of it), while the frame-independent content of non-triviality [1] is that $\Omega_\mu$ vanishes in no frame wherever the metric is curved (it is curved on the background history; the family contains a flat member, $a_4 = 0$, $b_4 = H^2x_4^2$) and that the vielbein factors enter every derivative term; when $\Psi^\dagger$ is realised as the Hilbert adjoint, the canonical anticommutator $\{\Psi, \Psi^\dagger\} = B\,\delta^7/\sqrt{|g|}$, $\sqrt{|g|} = e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}$, with $B$ of signature (8,8) forces an indefinite (Krein) inner product (a positive Fock realisation with $\Psi^\dagger = \chi B$ is constructed and checked only for single good-sector momenta with frozen coefficients, `mode_hamiltonian_good_sector`, `Fock_space_good_sector_example`, `good_sector_positive_fock_realisation`; in the corrected metric the curved good-sector mode operator is Hermitian only up to the boundary term at the degenerate points $z = \pi/2 + n\pi$, where this record imposes no boundary condition, and without one the good sector has complex frequencies wherever $m^2 < c_g^2$, `good_sector_hermiticity_up_to_the_brane_flux`, `good_sector_x0_independent_modes_without_boundary_condition`; a positive-norm Hilbert space for the full field is not established); homogeneous on-shell configurations have $\rho = mS + U$ and $p = SU' - U$ in every direction, with $e^{-a_4}b_4^2S$ constant along $x_4$; the field equations for $a_4$ and $b_4$ consist of a first-order constraint, two second-order equations that are linear in $a_4''$ and $(b_4'/b_4)'$, the conditions that the source have no off-diagonal component and equal hidden and extra-time pressures, $p_0 = p_t$, and that every diagonal source component be independent of $x_0$; in Einstein gravity the flat member is a vacuum solution and no exponential history is, and with the author's Lovelock weights the background history $a_4 = Hx_4$, $b_4 = b_4(0)e^{(4/3)Hx_4}$ of `Revision/SPEC.md` section 1 requires an anisotropic source that grows with $x_4$ and is used as a prescribed background. Section 15 states what is not claimed, including the frame dependence of the gravitational term, the boundary terms at the degenerate points and the ill-posedness of the Cauchy problem for data that depend on the extra times. From the second wave of the record (2026-10-08; recomputed for the corrected metric where the metric enters, the finite Fock model being metric-independent): the field equations for $a_4$ and $b_4$ with the Kohn-Sham source (section 13: no recorded Kohn-Sham state is an admissible source), the completion of the Kohn-Sham-level pairing T3 (section 14), the operator form of the on-shell identity for $\lambda \neq 0$ in a finite fermionic Fock model of one good-sector mode set with frozen coefficients, where, of the tested operator orderings, it holds exactly only when the potential and the energy-momentum tensor are both Wick ordered (section 12; nothing is proved for the field on a whole slice), the verdict of the dark-sector investigation for dirac16complex (section 15) and pointers to the documents on the Kohn-Sham model, the dark-sector hypotheses and the Lovelock tensors (section 1).

## 1. Scope, sources and status of the record

The binding plan is `Revision/SPEC.md`; the author's task is quoted in `Revision/README.md`. This document belongs to the new record under `Revision/` and uses nothing from the earlier stages of the repository: every statement below is an output of Revision code and is cited by the name of the check that verifies it. Numbers and formulas are taken only from the following files (verdicts as recorded in them when this document was written):

| part | files | checks |
| --- | --- | --- |
| algebra (SPEC section 2) | `Revision/algebra/reports/wolfram-algebra.json`, `Revision/algebra/reports/python-algebra.json` | Wolfram: 45 of 45 checks pass; sympy: 35 of 35 checks pass |
| field theory (SPEC sections 1, 3, 4, 6; the corrected metric) | `Revision/theory/field-theory.json`, `Revision/theory/reports/wolfram-field-theory.json`, `Revision/theory/reports/python-field-theory.json` | Wolfram: 86 of 86 checks pass; sympy: 72 of 72 checks pass |
| field equations for $a_4$ and $b_4$ (SPEC section 5) | `Revision/field_equations_a4/a4-equations.json`, `Revision/field_equations_a4/reports/wolfram-a4-report.json`, `Revision/field_equations_a4/reports/python-a4-report.json` | Wolfram: 57 of 57 checks pass; sympy: 69 of 69 checks pass |
| pairing (SPEC section 9) | `Revision/pairing/pairing-theory.json`, `Revision/pairing/reports/wolfram-pairing.json`, `Revision/pairing/reports/python-pairing.json` | Wolfram: 102 of 102 checks pass; sympy: 67 of 67 checks pass |
| scope of the statements (frame dependence, boundary terms, growth, sign of the energy) | `Revision/theory/reports/wolfram-scope.json`, `Revision/theory/reports/python-scope.json` | Wolfram: 16 of 16 checks pass; sympy: 15 of 15 checks pass |
| Kohn-Sham pairing T3 (SPEC section 9) | `Revision/pairing/kohn_sham/t3-theory.json`, `Revision/pairing/kohn_sham/reports/wolfram-t3.json`, `Revision/pairing/kohn_sham/reports/python-t3.json` | Wolfram: 9 of 9 checks pass; sympy: 12 of 12 checks pass |
| the Kohn-Sham states as a source of the $a_4$ and $b_4$ equations | `Revision/field_equations_a4/reports/ks-source-conditions.json` | Python: 5 of 5 checks pass |
| the $a_4$ and $b_4$ equations with the Kohn-Sham source | `Revision/field_equations_a4/ks_source/reports/ks-source-a4.json` | Python: 19 of 19 checks pass |
| completion of T3 (2026-10-08) | `Revision/pairing/kohn_sham/t3-completion.json`, `Revision/pairing/kohn_sham/reports/wolfram-t3-completion.json`, `Revision/pairing/kohn_sham/reports/python-t3-completion.json` | Wolfram: 3 of 3 checks pass; sympy: 7 of 7 checks pass |
| the energy-momentum tensor operator for $\lambda \neq 0$ in a finite Fock model (SPEC sections 4, 6; 2026-10-08) | `Revision/theory/fock_quartic/reports/fock-quartic.json` | Python (sympy and its own exact engine for the anticommutation relations; no Wolfram counterpart): 21 of 21 checks pass |
| the lead's checks of the charge and the U(1) current | `Revision/lead_checks/reports/charge-conjugation-and-u1.json` | lead checks: 12 of 12 checks pass |
| dark sector, Hypothesis (SPEC section 8) | `Revision/dark_sector/dirac16complex/reports/derivation-checks.json`, `Revision/dark_sector/dirac16complex/reports/ks-history-run.json`, `Revision/dark_sector/dirac16complex/reports/eos-checks.json`, `Revision/dark_sector/dirac16complex/reports/independent-checks.json`, `Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json` | derivation: 37 of 37 checks pass; Kohn-Sham history: 8 of 8 checks pass; equation of state: 13 of 13 checks pass; independent: 10 of 10 checks pass; dirac16complex00 derivation (cited for the phantom window of the drifting condensate): 48 of 48 checks pass |

The parts with a Wolfram and a sympy count have two verifiers that share no code: a WolframScript verifier (exact symbolic arithmetic) and a sympy verifier (an independent re-derivation; the gamma matrices are rebuilt from the author's formulas on both sides and compared entry by entry). Where only one engine verifies a statement, only that engine's check is cited. A check is cited in typewriter type, for example `nontriviality_1_dirac16complex` (Wolfram) or `gamma_mu_Omega_mu_equals_hidden_block_terms` (sympy); in the field-theory reports the Wolfram names end in `_G` for dirac16complex (explicit Grassmann algebra) and the sympy names begin with `grassmann_`. The proofs are exact identities in the stated generality (symbolic $H$, two general functions $a_4(x_4)$ and $b_4(x_4) > 0$, every real $z$, $m$, $\lambda$, and a general field configuration on its jet space); exact numerical examples are labelled as examples.

**Related Revision documents.** The Kohn-Sham model of dirac16complex in the deflating field (SPEC section 7: the reduction to $2 \times 2$ blocks in the hidden coordinate, the instantaneous ground and first excited states along the prescribed history $a_4 = Hx_4$, $b_4 = b_4(0)e^{(4/3)Hx_4}$, Mermin thermodynamics, and the full cross-check of the Rust solver against the independent reference, `Revision/kohn_sham/reports/ks-crosscheck.json`: 31 of 31 checks pass) is described in `Revision/docs/KOHN_SHAM_DEFLATING_FIELD`. The generalized Kronecker delta and the Lovelock tensors $P_{(1)}$, $P_{(2)}$, $P_{(3)}$ behind the field equations for $a_4$ and $b_4$ of section 13 are described in `Revision/docs/LOVELOCK_GKD`. The dark-sector hypotheses of SPEC section 8 are investigated in `Revision/docs/DARK_SECTOR_HYPOTHESES` (its verdict for dirac16complex is summarised in section 15). The pairing theorems, with the completion of T3, are in `Revision/docs/PAIR_CREATION_PROOFS`. The commuting companion field dirac16complex00 is the subject of `Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY`.

**Status of the comparison record of the field-theory branch.** The sympy report contains a comparison with the current Wolfram side (`comparison_with_wolfram`): 33 of 33 formula records and 65 of 65 check pairs agree, against a Wolfram run of 86 checks. Every formula record of `Revision/theory/field-theory.json` is compared (the record `energy_exchange`, three Wolfram expressions, component by component against the divergence recomputed from the sympy Christoffel symbols; the prose records `nontriviality`, `majorana_negative_control`, `exact_solutions`, `equation_of_state_definitions`, `hidden_direction_hermiticity` and `quantisation` by re-deriving their formulas in sympy), and every one of the 86 Wolfram checks is paired with a sympy check (the list `wolfram_checks_without_sympy_counterpart` of the comparison is empty). The sympy verifier exits with an error unless the comparison agrees entirely, so a stale comparison cannot pass unnoticed. This document still cites each formula by the checks of each engine separately.

Conventions (SPEC sections 1 and 2): the author's coordinates $x_0, x_1, \dots, x_7$, in the author's order; $x_0$ is the hidden direction, space-like, $x_1, x_2, x_3$ are ordinary 3-space, $x_4$ is the time, $x_5, x_6, x_7$ are the three extra times (time-like, deflating exponentially); $z = 6Hx_0$ real, $H > 0$; $a_4 = a_4(x_4)$ and $b_4 = b_4(x_4) > 0$, $a_4' = da_4/dx_4$, $b_4' = db_4/dx_4$, and throughout

$$
u = \frac{b_4'}{b_4},\qquad v = u' = \frac{b_4''}{b_4} - u^2,\qquad k = \frac{e^{2a_4}}{b_4},\qquad h_4 = \tfrac12u - a_4' ;
$$

$\partial_a = \partial/\partial x_a$. Frame indices are aligned with the coordinates and written in parentheses: $\gamma^{(a)}$ is the frame gamma matrix of direction $x_a$. Throughout, $i \in \{1, 2, 3\}$ labels the 3-space directions and $t \in \{5, 6, 7\}$ the extra times.

## 2. The primordial gravitational field

The corrected metric (SPEC section 1, version 2 of 2026-10-16), with signature (4,4) (space-like $x_0, x_1, x_2, x_3$; time-like $x_4, \dots, x_7$):

$$
\begin{aligned}
ds^2 &= e^{-2a_4}b_4\cot^2 z\,dx_0^2 + e^{2a_4}(dx_1^2 + dx_2^2 + dx_3^2) - dx_4^2 \\
&\quad - e^{-2a_4}\,b_4(\sin^2 z)^{1/6}\,(dx_5^2 + dx_6^2 + dx_7^2), \qquad z = 6Hx_0 \text{ real},
\end{aligned}
$$

with two functions of the time, $a_4(x_4)$ and $b_4(x_4) > 0$ (`metric_is_the_corrected_metric`; sympy `metric_from_vielbein_equals_SPEC`; the correction is recorded in `Revision/metric_warped/`). $(\sin^2 z)^{1/6}$ is the positive root, so the metric is defined for every real $z$; it is degenerate at $z = n\pi/2$ (at $z = \pi/2 + n\pi$ the folds, $g_{00} = 0$ and $\sqrt{|g|} = 0$, where the two halves of a cell meet). Every identity of this document holds for general $a_4$ and $b_4$ and every real $z$ between these points; $b_4$ is never 1, and a constant $b_4 = c$, which becomes $b_4 = 1$ after the rescaling $x_k \to \sqrt{c}\,x_k$ of $x_0, x_5, x_6, x_7$ together with $H \to H/\sqrt{c}$, is excluded as a history as well. Where a statement needs a history, it is the background history of SPEC section 1, $a_4 = Hx_4$, $b_4 = b_4(0)e^{(4/3)Hx_4}$ (section 13).

The scale factor of 3-space is $e^{a_4}$ (inflating as $a_4$ increases); the hidden direction and the extra times form one block with the scale factor $e^{-a_4}b_4^{1/2}$ times the time-independent factors $|\cot z|$ and $(\sin^2 z)^{1/12}$ (it changes at the rate $h_4 = \tfrac12u - a_4'$ and deflates where $h_4 < 0$; on the flat member $a_4 = 0$, $b_4 = H^2x_4^2$ below it is $Hx_4$ and grows for $x_4 > 0$; on the background history $h_4 < 0$ and the scale factor is proportional to $e^{-a_4/3}$, an exponential deflation). The diagonal vielbein $e^a{}_\mu = f_a\,\delta^a_\mu$ with frame metric $\eta_{ab} = \mathrm{diag}(+1, +1, +1, +1, -1, -1, -1, -1)$ (in the order $x_0, \dots, x_7$) has

$$
f_0 = e^{-a_4}b_4^{1/2}\cot z,\quad f_1 = f_2 = f_3 = e^{a_4},\quad f_4 = 1,\quad f_5 = f_6 = f_7 = e^{-a_4}b_4^{1/2}(\sin^2 z)^{1/12}
$$

($f_0$ signed) and reproduces the metric entry by entry (`metric_is_the_corrected_metric`, `vielbein_inverse`; sympy `metric_from_vielbein_equals_SPEC`). The volume element is

$$
\sqrt{|g|} = \sigma_z f_0 f_1\cdots f_7 = e^{-a_4}b_4^2\,|\cot z|\,(\sin^2 z)^{1/4},\qquad \sigma_z = \mathrm{sign}(\cot z),
$$

so $\partial_4\sqrt{|g|} = (2u - a_4')\sqrt{|g|}$ (`sqrt_det_g` in both reports). $H = 0$ is not a member of the family but a degenerate limit ($g_{55} \to 0$, $g_{00} \to \infty$ at fixed $x_0 \neq 0$; `degenerate_at_H_0`); every statement below assumes $H > 0$.

The Levi-Civita connection has 21 independent nonzero symbols (`christoffel_count`, `christoffel_symmetric_metric_compatible`; formula key `christoffel_nonzero`):

$$
\begin{aligned}
\Gamma^{x_0}{}_{x_0 x_0} &= -12H\csc(12Hx_0), & \Gamma^{x_0}{}_{x_0 x_4} &= h_4, \\
\Gamma^{x_0}{}_{x_t x_t} &= H(\sin^2 z)^{1/6}\tan z, & \Gamma^{x_i}{}_{x_i x_4} &= a_4', \\
\Gamma^{x_4}{}_{x_0 x_0} &= e^{-2a_4}b_4\cot^2 z\,h_4, & \Gamma^{x_4}{}_{x_i x_i} &= e^{2a_4}a_4', \\
\Gamma^{x_4}{}_{x_t x_t} &= -e^{-2a_4}b_4(\sin^2 z)^{1/6}\,h_4, & \Gamma^{x_t}{}_{x_t x_0} &= H\cot z, \\
\Gamma^{x_t}{}_{x_t x_4} &= h_4 .
\end{aligned}
$$

The mixed Ricci tensor is diagonal and free of $x_0$ (`ricci_mixed_components`, `ricci_scalar`, `curvature_and_flat_member`; formula key `ricci_mixed_nonzero`):

$$
\begin{aligned}
R^{x_0}{}_{x_0} = R^{x_t}{}_{x_t} &= -3H^2k + (a_4')^2 - a_4'' - \tfrac52a_4'u + \tfrac12\frac{b_4''}{b_4} + \tfrac12u^2, & R^{x_i}{}_{x_i} &= -(a_4')^2 + a_4'' + 2a_4'u, \\
R^{x_4}{}_{x_4} &= 7(a_4')^2 - a_4'' - 4a_4'u + 2\frac{b_4''}{b_4} - u^2,
\end{aligned}
$$

$$
R = -12H^2k + 8(a_4')^2 - 2a_4'' - 8a_4'u + 4\frac{b_4''}{b_4} + u^2 .
$$

These equal the independent sympy record of the corrected metric, `Revision/metric_warped/results/warped-metric.json` (`ricci_mixed_components`). The metric is not curved for every member of the family: for $a_4 = 0$, $b_4 = H^2x_4^2$ all 4096 Riemann components vanish (8-dimensional flat space in Milne form), and on the background history it is curved, $R \neq 0$ (`flat_member_and_curvature`, `curvature_and_flat_member`).

## 3. The field dirac16complex: Clifford algebra, Pin(4,4) and Spin(4,4)

dirac16complex is a field $\Psi$ with 16 complex anticommuting components $\Psi_A(x)$, $A = 1, \dots, 16$ (elements of a Grassmann algebra; after quantisation, operators with canonical anticommutators, section 11). It transforms under a 16-dimensional irreducible representation of Pin(4,4), the double cover of O(4,4); for the transformations of determinant 1 it transforms under the direct sum of two inequivalent irreducible 8-dimensional representations of Spin(4,4), the double cover of SO(4,4). These representation facts are proved exactly below for the author's gamma matrices; they do not depend on the metric.

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

(This is the canonical connection with the frame metric; the notebook's contraction of the mixed $\omega_\mu{}^a{}_b$, which lacks a metric factor, is not used.) The postulate holds for all 512 components and $\omega_{\mu ab} = -\omega_{\mu ba}$ (`vielbein_postulate` in both field-theory reports, `omega_antisymmetric`, `spin_connection_antisymmetric`). Exactly 10 components with $a < b$ are nonzero (`omega_components`; formula key `omega_nonzero`; $s_b = e^{-a_4}b_4^{1/2}$):

$$
\begin{aligned}
\omega_{x_0\,(0)(4)} &= h_4\,s_b\cot z, & \omega_{x_i\,(i)(4)} &= a_4'\,e^{a_4}, \\
\omega_{x_t\,(4)(t)} &= h_4\,s_b\,(\sin^2 z)^{1/12}, & \omega_{x_t\,(0)(t)} &= H\,(\sin^2 z)^{1/12},
\end{aligned}
$$

and $\omega_{x_4} = 0$: the hidden direction follows the extra times in $x_4$, and 3-space does not depend on $x_0$. The spinor connection is real (sympy `spinor_connection_real`) and reads (`Omega_components`; sympy `Omega_x4_vanishes_Omega_x0_does_not`)

$$
\begin{aligned}
\Omega_{x_0} &= \tfrac12\,h_4\,s_b\cot z\;\gamma^{(0)}\gamma^{(4)}, \qquad \Omega_{x_i} = \tfrac12\,a_4'\,e^{a_4}\,\gamma^{(i)}\gamma^{(4)} \qquad (i = 1, 2, 3), \\
\Omega_{x_t} &= \tfrac12\,(\sin^2 z)^{1/12}\,\big(h_4\,s_b\,\gamma^{(4)}\gamma^{(t)} + H\,\gamma^{(0)}\gamma^{(t)}\big) \qquad (t = 5, 6, 7), \qquad \Omega_{x_4} = 0.
\end{aligned}
$$

It makes the gammas covariantly constant, $D_\mu\gamma^\nu = \partial_\mu\gamma^\nu + \Gamma^\nu{}_{\mu\lambda}\gamma^\lambda + [\Omega_\mu, \gamma^\nu] = 0$ for all 64 pairs (`gamma_covariantly_constant`, `covariant_constancy_D_mu_gamma_nu`), and its curvature is the Riemann tensor, $[D_\mu, D_\nu]\Psi = \frac12 R_{ab\mu\nu}S^{ab}\Psi$ (`spin_curvature_equals_Riemann`, `spinor_curvature_equals_riemann`).

The contraction that enters the field equation, per direction (no sum; `gammaOmega_per_direction`, formula key of the same name):

$$
\begin{aligned}
\gamma^{x_0}\Omega_{x_0} &= \tfrac12 h_4\,\gamma^{(4)}, \qquad \gamma^{x_i}\Omega_{x_i} = \tfrac12 a_4'\,\gamma^{(4)} \qquad (i = 1, 2, 3), \\
\gamma^{x_t}\Omega_{x_t} &= \tfrac12 h_4\,\gamma^{(4)} + \tfrac12He^{a_4}b_4^{-1/2}\,\gamma^{(0)} \qquad (t = 5, 6, 7), \qquad \gamma^{x_4}\Omega_{x_4} = 0,
\end{aligned}
$$

and summed:

$$
\gamma^\mu\Omega_\mu = c_g\gamma^{(0)} + v_g\gamma^{(4)} = \frac{1}{2\sqrt{|g|}}\,\partial_\mu\big(\sqrt{|g|}\,\gamma^\mu\big),\qquad c_g = \tfrac32He^{a_4}b_4^{-1/2},\qquad v_g = \frac{b_4'}{b_4} - \frac{a_4'}{2}
$$

(`gammaOmega_total`, `gammaOmega_divergence_form`): the $\gamma^{(4)}$ terms of the hidden direction, the three 3-space directions and the three extra times add to $4\cdot\tfrac12h_4 + \tfrac32a_4' = v_g$, half the logarithmic rate of the 7-volume, and the $\gamma^{(0)}$ terms of the three extra times add to $c_g$; the result is free of $x_0$ for every real $z$. In the divergence form the $x_0$ part is $\frac{1}{2\sqrt{|g|}}\partial_0\big(\sigma_zb_4^{3/2}(\sin^2 z)^{1/4}\big)\gamma^{(0)} = c_g\gamma^{(0)}$ and the $x_4$ part is $\frac{1}{2\sqrt{|g|}}\big(\partial_4\sqrt{|g|}\big)\gamma^{(4)} = v_g\gamma^{(4)}$. The sympy verifier confirms each of these statements independently (`gamma_mu_Omega_mu_equals_hidden_block_terms`, `per_direction_terms` and `divergence_of_sqrtg_gamma`). The field-equations branch verifies the same value again, in a Clifford representation of its own and with T16 (`ownrep_gravity_term`, `authorT16_gravity_term`; Wolfram `gravity_term_gamma_mu_Omega_mu`). Since $\gamma^{(0)}$ and $\gamma^{(4)}$ anticommute, with squares $+1$ and $-1$,

$$
\big(\gamma^\mu\Omega_\mu\big)^2 = \big(c_g^2 - v_g^2\big)\,I_{16} = \big(\tfrac94H^2k - (u - \tfrac12a_4')^2\big)\,I_{16}
$$

(`gravity_term_square`; on the background history with $b_4(0) = 1$, $c_g = \tfrac32He^{Hx_4/3}$, $v_g = \tfrac56H$ and the square is $H^2(\tfrac94e^{2Hx_4/3} - \tfrac{25}{36})I_{16} > 0$ for $x_4 \geq 0$; it is negative where $\tfrac94e^{2Hx_4/3} < \tfrac{25}{36}$, at negative $x_4$). For each direction separately $\{\gamma^\mu, \Omega_\mu\} = 0$ (no sum), because $\Omega_\mu$ contains only generators $S^{(\mu)b}$ (`gamma_mu_anticommutes_with_Omega_mu_no_sum`, `anticommutator_gamma_Omega_vanishes`).

**The value of $\gamma^\mu\Omega_\mu$ belongs to the diagonal vielbein.** The canonical spin connection depends on the choice of the local frame, and so does the contraction $\gamma^\mu\Omega_\mu$. Boost the frame in the $(x_0, x_4)$ plane, $e'^{(4)} = \cosh b\,e^{(4)} + \sinh b\,e^{(0)}$, $e'^{(0)} = \sinh b\,e^{(4)} + \cosh b\,e^{(0)}$, the other $e'^{(a)} = e^{(a)}$, with rapidity $b = \beta x_4 + b_0$: the frame reproduces the metric, its canonical connection satisfies the vielbein postulate, and exactly, for every $a_4$, $b_4$ and $H$,

$$
\gamma'^\mu\Omega'_\mu = \big(c_g - \tfrac{\beta}{2}\big)\,\big(\cosh b\,\gamma^{(0)} - \sinh b\,\gamma^{(4)}\big) + v_g\,\big(\cosh b\,\gamma^{(4)} - \sinh b\,\gamma^{(0)}\big),
$$

which is $c_g\gamma^{(0)} + v_g\gamma^{(4)}$ for the unboosted frame. Both engines verify the frame and its connection (`boosted_frame_reproduces_metric` and `boosted_frame_canonical_connection`) and the contraction (`boosted_frame_gammaOmega_formula`). A rapidity with $b' = 2c_g$ removes the $c_g$ part identically, and $\gamma'^\mu\Omega'_\mu = v_g\big(\cosh b\,\gamma^{(4)} - \sinh b\,\gamma^{(0)}\big)$ remains; for every rapidity function $b(x_4)$ the coefficients $c_0$, $c_4$ of $\gamma'^\mu\Omega'_\mu = c_0\gamma^{(0)} + c_4\gamma^{(4)}$ satisfy $\cosh b\,c_4 + \sinh b\,c_0 = v_g$, so no boost in this plane removes the term unless $b_4'/b_4 = a_4'/2$ (`boosted_frame_removes_only_the_H_term`). In the boosted frame $\Omega'_\mu$ is nonzero and its curvature is nonzero for general $a_4$, $b_4$ (`boosted_frame_curvature_nonzero`): what no frame removes, wherever the metric is curved, is $\Omega_\mu$ itself, whose curvature is the Riemann tensor.

## 5. The Lagrangian

The Lagrangian density (SPEC section 3), with an explicit mass term linear in $m$ and quadratic in the spinor:

$$
\begin{aligned}
\mathcal{L} &= \sqrt{|g|}\,\Big[\tfrac12\big(\bar\Psi\gamma^\mu D_\mu\Psi - (D_\mu\bar\Psi)\gamma^\mu\Psi\big) - m\,\bar\Psi\Psi - U(\bar\Psi\Psi)\Big], \qquad \sqrt{|g|} = e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}, \\
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
\mathcal{L} = \sqrt{|g|}\,\Big[\tfrac12\sum_{a=0}^{7}\frac{1}{f_a}\big(\bar\Psi\gamma^{(a)}\partial_a\Psi - \partial_a\bar\Psi\gamma^{(a)}\Psi\big) - mS - U(S)\Big].
$$

  It reaches the field equations only through this identity: varying the symmetrised kinetic term produces $\partial_\mu(\sqrt{|g|}\gamma^\mu) = 2\sqrt{|g|}\,\gamma^\mu\Omega_\mu$ (section 7). Hence the Euler-Lagrange equations of $\mathcal{L}$ are those of the connection-free symmetric Lagrangian (the display above), and the term $c_g\gamma^{(0)} + v_g\gamma^{(4)}$ is its half-density (volume and vielbein divergence) term (`connection_free_lagrangian_same_equations`, both engines).
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
&e^{a_4}b_4^{-1/2}\tan z\,\gamma^{(0)}\partial_0\Psi + e^{-a_4}\big(\gamma^{(1)}\partial_1 + \gamma^{(2)}\partial_2 + \gamma^{(3)}\partial_3\big)\Psi + \gamma^{(4)}\partial_4\Psi \\
&\quad + e^{a_4}b_4^{-1/2}(\sin^2 z)^{-1/12}\big(\gamma^{(5)}\partial_5 + \gamma^{(6)}\partial_6 + \gamma^{(7)}\partial_7\big)\Psi + c_g\gamma^{(0)}\Psi + v_g\gamma^{(4)}\Psi = \big(m + U'(S)\big)\Psi,
\end{aligned}
$$

and the adjoint equation (formula key `adjoint_equation`):

$$
\begin{aligned}
&e^{a_4}b_4^{-1/2}\tan z\,\partial_0\bar\Psi\gamma^{(0)} + e^{-a_4}\big(\partial_1\bar\Psi\gamma^{(1)} + \partial_2\bar\Psi\gamma^{(2)} + \partial_3\bar\Psi\gamma^{(3)}\big) + \partial_4\bar\Psi\gamma^{(4)} \\
&\quad + e^{a_4}b_4^{-1/2}(\sin^2 z)^{-1/12}\big(\partial_5\bar\Psi\gamma^{(5)} + \partial_6\bar\Psi\gamma^{(6)} + \partial_7\bar\Psi\gamma^{(7)}\big) + c_g\bar\Psi\gamma^{(0)} + v_g\bar\Psi\gamma^{(4)} = -\big(m + U'(S)\big)\bar\Psi.
\end{aligned}
$$

Since $(\gamma^{(4)})^2 = -1$, the field equation is equivalent to the first-order evolution equation (`evolution_form_G`; formula key `evolution_form`)

$$
\partial_4\Psi = -\gamma^{(4)}\Big[\big(m + U'(S)\big)\Psi - \sum_{a \neq 4}\frac{1}{f_a}\gamma^{(a)}\partial_a\Psi - c_g\gamma^{(0)}\Psi\Big] - v_g\,\Psi,
$$

so the slices $x_4 = $ const are non-characteristic ($g^{44} = -1$); the last term is the factor $e^{a_4/2}b_4^{-1}$ of the solutions (section 8). In the chiral split $\Psi = (\psi_-, \psi_+)$ (rows 1 to 8 with $\Gamma = -1$, rows 9 to 16 with $\Gamma = +1$) every gamma is block off-diagonal, $\gamma^{(a)} = \begin{pmatrix} 0 & \bar\tau_a \\ \tau_a & 0\end{pmatrix}$ with $\bar\tau_0 = \tau_0 = I_8$, and the field equation is the pair (`block_form`; formula key `field_equation_blocks`)

$$
\begin{aligned}
&\sum_{a}\frac{1}{f_a}\bar\tau_a\partial_a\psi_+ + c_g\psi_+ + v_g\,\bar\tau_4\psi_+ = V\psi_-,\\
&\sum_{a}\frac{1}{f_a}\tau_a\partial_a\psi_- + c_g\psi_- + v_g\,\tau_4\psi_- = V\psi_+,\qquad V = m + U'(S).
\end{aligned}
$$

The 16 component equations, $(\gamma^\mu D_\mu\Psi)_A = V\Psi_A$ with $\psi_A = \Psi_A$ the components in the basis of the fixture gammas, $\epsilon_s = e^{-a_4} = 1/f_1$, $\epsilon_t = e^{a_4}b_4^{-1/2}(\sin^2 z)^{-1/12} = 1/f_5$, $\epsilon_0 = e^{a_4}b_4^{-1/2}$ and $\hat\partial_4 = \partial_4 + v_g$ (the term $v_g\gamma^{(4)}$ of the spin connection enters every component on the same component and with the same sign as $\partial_4$, and the term $c_g\gamma^{(0)}$ next to the hidden-direction derivative; formula key `field_equation_components`; `Dirac_operator_explicit_G`, `EL_Psibar_G`; the publication test of this document re-derives them from the formula file and compares them with the independent sympy expressions `dirac_equation_components` of the sympy report): the eight equations of the $\Gamma = -1$ rows,

$$
\begin{aligned}
\epsilon_s(-\partial_1\psi_{16} + \partial_2\psi_{15} - \partial_3\psi_{14}) - \hat\partial_4\psi_{14} + \epsilon_t(\partial_5\psi_{15} + \partial_6\psi_{16} + \partial_7\psi_{9}) + \epsilon_0(\tan z\,\partial_0 + \tfrac32H)\psi_{9} &= V\psi_{1} \\
\epsilon_s(-\partial_1\psi_{15} - \partial_2\psi_{16} + \partial_3\psi_{13}) + \hat\partial_4\psi_{13} + \epsilon_t(\partial_5\psi_{16} - \partial_6\psi_{15} + \partial_7\psi_{10}) + \epsilon_0(\tan z\,\partial_0 + \tfrac32H)\psi_{10} &= V\psi_{2} \\
\epsilon_s(\partial_1\psi_{14} - \partial_2\psi_{13} - \partial_3\psi_{16}) + \hat\partial_4\psi_{16} + \epsilon_t(-\partial_5\psi_{13} + \partial_6\psi_{14} + \partial_7\psi_{11}) + \epsilon_0(\tan z\,\partial_0 + \tfrac32H)\psi_{11} &= V\psi_{3} \\
\epsilon_s(\partial_1\psi_{13} + \partial_2\psi_{14} + \partial_3\psi_{15}) - \hat\partial_4\psi_{15} + \epsilon_t(-\partial_5\psi_{14} - \partial_6\psi_{13} + \partial_7\psi_{12}) + \epsilon_0(\tan z\,\partial_0 + \tfrac32H)\psi_{12} &= V\psi_{4} \\
\epsilon_s(-\partial_1\psi_{12} + \partial_2\psi_{11} - \partial_3\psi_{10}) + \hat\partial_4\psi_{10} + \epsilon_t(-\partial_5\psi_{11} - \partial_6\psi_{12} - \partial_7\psi_{13}) + \epsilon_0(\tan z\,\partial_0 + \tfrac32H)\psi_{13} &= V\psi_{5} \\
\epsilon_s(-\partial_1\psi_{11} - \partial_2\psi_{12} + \partial_3\psi_{9}) - \hat\partial_4\psi_{9} + \epsilon_t(-\partial_5\psi_{12} + \partial_6\psi_{11} - \partial_7\psi_{14}) + \epsilon_0(\tan z\,\partial_0 + \tfrac32H)\psi_{14} &= V\psi_{6} \\
\epsilon_s(\partial_1\psi_{10} - \partial_2\psi_{9} - \partial_3\psi_{12}) - \hat\partial_4\psi_{12} + \epsilon_t(\partial_5\psi_{9} - \partial_6\psi_{10} - \partial_7\psi_{15}) + \epsilon_0(\tan z\,\partial_0 + \tfrac32H)\psi_{15} &= V\psi_{7} \\
\epsilon_s(\partial_1\psi_{9} + \partial_2\psi_{10} + \partial_3\psi_{11}) + \hat\partial_4\psi_{11} + \epsilon_t(\partial_5\psi_{10} + \partial_6\psi_{9} - \partial_7\psi_{16}) + \epsilon_0(\tan z\,\partial_0 + \tfrac32H)\psi_{16} &= V\psi_{8}
\end{aligned}
$$

and the eight equations of the $\Gamma = +1$ rows,

$$
\begin{aligned}
\epsilon_s(\partial_1\psi_{8} - \partial_2\psi_{7} + \partial_3\psi_{6}) + \hat\partial_4\psi_{6} + \epsilon_t(-\partial_5\psi_{7} - \partial_6\psi_{8} - \partial_7\psi_{1}) + \epsilon_0(\tan z\,\partial_0 + \tfrac32H)\psi_{1} &= V\psi_{9} \\
\epsilon_s(\partial_1\psi_{7} + \partial_2\psi_{8} - \partial_3\psi_{5}) - \hat\partial_4\psi_{5} + \epsilon_t(-\partial_5\psi_{8} + \partial_6\psi_{7} - \partial_7\psi_{2}) + \epsilon_0(\tan z\,\partial_0 + \tfrac32H)\psi_{2} &= V\psi_{10} \\
\epsilon_s(-\partial_1\psi_{6} + \partial_2\psi_{5} + \partial_3\psi_{8}) - \hat\partial_4\psi_{8} + \epsilon_t(\partial_5\psi_{5} - \partial_6\psi_{6} - \partial_7\psi_{3}) + \epsilon_0(\tan z\,\partial_0 + \tfrac32H)\psi_{3} &= V\psi_{11} \\
\epsilon_s(-\partial_1\psi_{5} - \partial_2\psi_{6} - \partial_3\psi_{7}) + \hat\partial_4\psi_{7} + \epsilon_t(\partial_5\psi_{6} + \partial_6\psi_{5} - \partial_7\psi_{4}) + \epsilon_0(\tan z\,\partial_0 + \tfrac32H)\psi_{4} &= V\psi_{12} \\
\epsilon_s(\partial_1\psi_{4} - \partial_2\psi_{3} + \partial_3\psi_{2}) - \hat\partial_4\psi_{2} + \epsilon_t(\partial_5\psi_{3} + \partial_6\psi_{4} + \partial_7\psi_{5}) + \epsilon_0(\tan z\,\partial_0 + \tfrac32H)\psi_{5} &= V\psi_{13} \\
\epsilon_s(\partial_1\psi_{3} + \partial_2\psi_{4} - \partial_3\psi_{1}) + \hat\partial_4\psi_{1} + \epsilon_t(\partial_5\psi_{4} - \partial_6\psi_{3} + \partial_7\psi_{6}) + \epsilon_0(\tan z\,\partial_0 + \tfrac32H)\psi_{6} &= V\psi_{14} \\
\epsilon_s(-\partial_1\psi_{2} + \partial_2\psi_{1} + \partial_3\psi_{4}) + \hat\partial_4\psi_{4} + \epsilon_t(-\partial_5\psi_{1} + \partial_6\psi_{2} + \partial_7\psi_{7}) + \epsilon_0(\tan z\,\partial_0 + \tfrac32H)\psi_{7} &= V\psi_{15} \\
\epsilon_s(-\partial_1\psi_{1} - \partial_2\psi_{2} - \partial_3\psi_{3}) - \hat\partial_4\psi_{3} + \epsilon_t(-\partial_5\psi_{2} - \partial_6\psi_{1} + \partial_7\psi_{8}) + \epsilon_0(\tan z\,\partial_0 + \tfrac32H)\psi_{8} &= V\psi_{16}
\end{aligned}
$$

For the quadratic potential $V = m + \lambda S$ with $S = \Psi^\dagger C\Psi$, an even (bilinear) element; the equations hold in the Grassmann algebra, and after quantisation as operator equations (section 11).

## 7. Non-triviality [1]

**Theorem 1 (non-triviality [1]).** Hypotheses: the corrected metric of section 2 with $H > 0$ and $z$ between degenerate points; $a_4$ and $b_4 > 0$ any twice differentiable functions of $x_4$ (a constant $a_4$ included; the identities hold for a constant $b_4$ as well, which section 2 excludes as a history); real $m$ and $\lambda$ (or any real potential $U$); the canonical spin connection of the diagonal vielbein; $\Psi$ any dirac16complex configuration (Grassmann-valued components) that is not identically zero. Then:

1. in the diagonal vielbein the Euler-Lagrange operator contains the gravitational term $\gamma^\mu D_\mu\Psi - \gamma^\mu\partial_\mu\Psi = \gamma^\mu\Omega_\mu\Psi = G\Psi$ with $G = c_g\gamma^{(0)} + v_g\gamma^{(4)}$; $G$ is never zero (its $\gamma^{(0)}$ coefficient $c_g$ is positive), $G^2 = (c_g^2 - v_g^2)\,I_{16}$, so $G\Psi \neq 0$ wherever $c_g^2 \neq v_g^2$ (on the background history with $b_4(0) = 1$, $G^2 = H^2(\tfrac94e^{2Hx_4/3} - \tfrac{25}{36})I_{16} > 0$ for $x_4 \geq 0$), while where $c_g = \pm v_g$ the matrix $G = c_g(\gamma^{(0)} \pm \gamma^{(4)})$ has rank 8 and annihilates an 8-dimensional subspace (this value depends on the frame and on the field variables, see the Remarks);
2. per direction, the hidden direction contributes $\tfrac12h_4\gamma^{(4)}$, each 3-space direction $\tfrac12a_4'\gamma^{(4)}$ and each extra time $\tfrac12h_4\gamma^{(4)} + \tfrac12He^{a_4}b_4^{-1/2}\gamma^{(0)}$; unlike the metric of 2026-10-14, where the $a_4'$ terms cancelled, the term sees the deflation of the block of the hidden direction and the extra times through $e^{a_4}b_4^{-1/2}$ and $h_4$;
3. in addition the vielbein enters every derivative term, $\gamma^\mu\partial_\mu = \epsilon_0\tan z\,\gamma^{(0)}\partial_0 + \epsilon_s\gamma^{(i)}\partial_i + \gamma^{(4)}\partial_4 + \epsilon_t\gamma^{(t)}\partial_t$, none of whose factors is identically 1;
4. all gravitational terms vanish together only if $\Omega_\mu = 0$ for every $\mu$, which holds if and only if $a_4' = 0$, $b_4' = 0$ and $H = 0$, and $H = 0$ lies outside the family (a degenerate limit); a local frame can remove $\Omega_\mu$ only where the Riemann tensor vanishes: the corrected metric is curved on the background history, and its flat member $a_4 = 0$, $b_4 = H^2x_4^2$ is the case "flat 4+4 spacetime" of the test [1].

*Proof.* (a) The connection components of section 4 are each $h_4$, $a_4'$ or $H$ times one of the factors $e^{a_4}$, $s_b\cot z$, $s_b(\sin^2 z)^{1/12}$, $(\sin^2 z)^{1/12}$, none of which vanishes between the degenerate points; since the $S^{ab}$ are linearly independent, the $x_4$-part of $\Omega_{x_i}$ vanishes if and only if $a_4$ is constant, those of $\Omega_{x_0}$ and $\Omega_{x_t}$ if and only if $e^{-a_4}b_4^{1/2}$ is constant, and the $H$-part if and only if $H = 0$; all $x_4$-parts vanish if and only if $a_4$ and $b_4$ are both constant (`Omega_vanishes_iff_a4prime_b4prime_and_H_vanish`, `nontriviality_Omega_zero_iff_flat`). (b) Contracting with $\gamma^\mu = \gamma^{(\mu)}/f_\mu$ and using $(\gamma^{(0)})^2 = (\gamma^{(i)})^2 = 1$, $(\gamma^{(t)})^2 = -1$ and $\gamma^{(t)}\gamma^{(4)}\gamma^{(t)} = \gamma^{(4)}$, $\gamma^{(t)}\gamma^{(0)}\gamma^{(t)} = \gamma^{(0)}$ gives the per-direction values of section 4; the scale factors cancel because $e^{a_4}b_4^{-1/2}s_b = 1$; hence $\gamma^\mu\Omega_\mu = G$, free of $x_0$ (`gammaOmega_per_direction`, `gammaOmega_total`, `per_direction_terms`, `gamma_mu_Omega_mu_equals_hidden_block_terms`). The same value follows from the divergence form of section 4 (`gammaOmega_divergence_form`, `divergence_of_sqrtg_gamma`). (c) $\gamma^{(0)}$ and $\gamma^{(4)}$ anticommute, $(\gamma^{(0)})^2 = I_{16}$ and $(\gamma^{(4)})^2 = -I_{16}$, so $G^2 = (c_g^2 - v_g^2)I_{16}$; $G\Psi = 0$ implies $G^2\Psi = 0$ and therefore $\Psi = 0$ wherever $c_g^2 \neq v_g^2$; where $c_g = \pm v_g$, $G$ has rank 8 (`gravity_term_square`, `nontriviality_1_dirac16complex`). (d) The term is part of the Euler-Lagrange equation although the connection drops out of $\mathcal{L}$ in this metric: the variation of the symmetrised kinetic term produces $\partial_\mu(\sqrt{|g|}\gamma^\mu) = 2\sqrt{|g|}\gamma^\mu\Omega_\mu$, and the Euler-Lagrange expressions equal $\sqrt{|g|}\,C\,(\gamma^\mu D_\mu\Psi - V\Psi)$ with the full covariant derivative (`L_spin_connection_drops_out_G`, `EL_Psibar_G`). (e) The curvature of $\Omega_\mu$ is $\frac12 R_{ab\mu\nu}S^{ab}$ (`spin_curvature_equals_Riemann`), the metric is curved on the background history and flat for $a_4 = 0$, $b_4 = H^2x_4^2$ (`flat_member_and_curvature`); if $\Omega_\mu$ vanished in some frame, the Riemann tensor would vanish. $H = 0$ is a degenerate limit of the metric (`degenerate_at_H_0`). This completes the proof.

Remarks (the exact scope of Theorem 1). On the flat member all gravitational effects are removable by a frame and the equation is the flat 4+4 Dirac-type equation, as the test [1] requires ("unless we are in flat 4+4 spacetime"). Items 1 and 2 are statements about the diagonal vielbein and the field variables $\Psi$; read without these hypotheses they would overstate [1]:

- The canonical connection drops out of $\mathcal{L}$, so the Euler-Lagrange equations are those of the connection-free symmetric Lagrangian; $G = \frac{1}{2\sqrt{|g|}}\partial_\mu(\sqrt{|g|}\gamma^\mu)$ is its half-density term (`connection_free_lagrangian_same_equations`).
- In the frame boosted in the $(x_0, x_4)$ plane with rapidity rate $2c_g$ the $c_g$ part of the term vanishes identically and $\gamma'^\mu\Omega'_\mu = v_g(\cosh b\,\gamma^{(4)} - \sinh b\,\gamma^{(0)})$ remains; no boost in this plane removes the $v_g$ part (section 4; `boosted_frame_removes_only_the_H_term`).
- In the diagonal frame the rescaling $\Psi = e^{a_4/2}b_4^{-1}(\sin^2 z)^{-1/8}\chi$ removes the whole term: $\gamma^\mu D_\mu\Psi = e^{a_4/2}b_4^{-1}(\sin^2 z)^{-1/8}\gamma^\mu\partial_\mu\chi$ exactly, so $\gamma^\mu\partial_\mu\chi = (m + U')\chi$; for $U = \frac{\lambda}{2}S^2$ the term turns into the $x_0$- and $x_4$-dependent coupling $\lambda e^{a_4}S[\chi]/(b_4^2|\sin z|^{1/2})$. The checks are `rescaling_removes_the_connection_term` and `rescaled_equation_quadratic_potential`. The exact $U = 0$ family of section 8 at $\alpha = -\frac14$ is this statement (no $H$ term).
- Unlike the metric of 2026-10-14, the term sees the hidden block: its $\gamma^{(0)}$ coefficient is $\tfrac32H$ times the inverse scale factor $e^{a_4}b_4^{-1/2}$ of the block, which grows as the block deflates (`gammaOmega_sees_the_hidden_block`).
- The frame-independent content of [1] is item 4 with item 3: $\Omega_\mu$ vanishes in no frame wherever the metric is curved (its curvature is the Riemann tensor), and the vielbein factors $e^{-a_4}$, $e^{a_4}b_4^{-1/2}(\sin^2 z)^{-1/12}$ and $e^{a_4}b_4^{-1/2}\tan z$ enter every derivative term. In the diagonal frame the connection also enters the energy-momentum tensor: for a homogeneous configuration the connection part of $K^{x_4}{}_{x_1}$ vanishes (3-space does not depend on $x_0$), but that of $K^{x_4}{}_{x_5}$ is $\tfrac12H(\sin^2 z)^{1/12}\bar\Psi\gamma^{(4)}\gamma^{(0)}\gamma^{(5)}\Psi$ (`spin_connection_in_the_energy_momentum_tensor`).
- Interpretation (labelled): the hidden-direction operator $e^{a_4}b_4^{-1/2}(\tan z\,\partial_0 + \tfrac32H)\gamma^{(0)}$ is antisymmetric for the measure $\sqrt{|g|}/f_0\,dx_0 = b_4^{3/2}(\sin^2 z)^{1/4}dx_0$ in the variables $\Psi$ up to a boundary term, $(\sin^2 z)^{1/4}[p(\partial_0 + \tfrac32H\cot z)q + ((\partial_0 + \tfrac32H\cot z)p)q] = \partial_0((\sin^2 z)^{1/4}pq)$ (`good_sector_hermiticity_curved`; formula key `hidden_direction_hermiticity`), which vanishes where $\sin z = 0$ and not where $\cos z = 0$; in the variables $\chi$ the operator has the same property without any $H$ term. This role of $c_g$ therefore depends on the variables and the measure (section 11). The $v_g$ term plays the corresponding role for the $x_4$ dependence of the measure: in the mode operator it is the anti-Hermitian term $-iv_g$, which compensates $\partial_4\sqrt{|g|} = 2v_g\sqrt{|g|}$ (section 11).

Non-triviality [2], for the commuting field dirac16complex00, has the same algebraic content and the same scope (`nontriviality_2_dirac16complex00`) and is the subject of the companion document `Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY`.

## 8. Self-consistency

The field equations of section 6 are self-consistent in the following exact senses.

- One system. The adjoint equation is the Dirac conjugate of the field equation: with $E = \gamma^\mu D_\mu\Psi - (m + U')\Psi$ and $\bar E = (D_\mu\bar\Psi)\gamma^\mu + (m + U')\bar\Psi$, $E^\dagger C = -\bar E$ exactly (`adjoint_equation_is_Dirac_conjugate_G`, `grassmann_adjoint_equation_is_conjugate`).
- Evolution form, not a well-posed Cauchy problem. The evolution form of section 6 holds exactly (`evolution_form_G`), and the Heisenberg equation of the quantised field reproduces it, including the term $-v_g\Psi$: see the Wolfram check `Heisenberg_equation_reproduces_field_equation` and the sympy check `hamiltonian_form_and_heisenberg_equation`. The slices $x_4 = $ const are non-characteristic, but the Cauchy problem is not well posed in Hadamard's sense for data that depend on $x_5, x_6, x_7$: with frozen coefficients an extra-time momentum $k_5 = K$ gives the growth rate $\sqrt{K^2 - m^2 - k_0^2 - k_1^2 - k_2^2 - k_3^2}$, unbounded as $K$ grows (`extra_time_growth_rates_unbounded`), and in the metric the frame momentum $e^{a_4}b_4^{-1/2}(\sin^2 z)^{-1/12}k_{x_5}$ grows as the block deflates. A well-posed evolution is available at most in the good sector (no extra-time dependence) and only with a boundary condition at the degenerate points (section 11).
- Integrability. The gammas are covariantly constant and the spinor curvature is the Riemann tensor (section 4). The square of the Dirac operator obeys the Lichnerowicz identity (`Lichnerowicz_identity_G`, `lichnerowicz_identity_on_fields`, `lichnerowicz_contraction`):

$$
(\gamma^\mu D_\mu)^2\Psi = g^{\mu\nu}\big(D_\mu D_\nu\Psi - \Gamma^\lambda{}_{\mu\nu}D_\lambda\Psi\big) - \frac{R}{4}\Psi,\qquad R = -12H^2k + 8(a_4')^2 - 2a_4'' - 8a_4'u + 4\frac{b_4''}{b_4} + u^2,
$$

  so the second-order consequence of the field equations is consistent with the curvature.
- Conserved current. $J^\mu = -i\bar\Psi\gamma^\mu\Psi$ is real, and off shell $\partial_\mu(\sqrt{|g|}J^\mu) = -i\sqrt{|g|}\,(\bar E\Psi + \bar\Psi E)$, so $\nabla_\mu J^\mu = 0$ on shell (`current_real_G`, `current_conservation_identity_G`, `grassmann_current_conservation`). The charge density is $J^{x_4} = \Psi^\dagger B\Psi$, and the charge of a slice of constant $x_4$, $Q = \int\sqrt{|g|}\,\Psi^\dagger B\Psi\,d^7x$, is an indefinite form (`charge_density_is_Krein_form_G`). Only the local law $\nabla_\mu J^\mu = 0$ is established: $Q$ is constant in $x_4$ only if no charge flows through the boundary of the slice, and at the degenerate points $z = \pi/2 + n\pi$ the flow is not zero in general (`good_sector_hermiticity_up_to_the_brane_flux`, both engines; the lead's independent check `u1_noether_matrix_identity` of `Revision/lead_checks/reports/charge-conjugation-and-u1.json` verifies the local law for general $a_4(x_4)$ and $b_4(x_4)$ and states that the constancy of $Q$ is not established). This record imposes no boundary condition there (sections 11 and 15).
- Bianchi-type identity of the energy-momentum tensor. For the tensor $T^\mu{}_\nu$ of section 9 the invariance of the action under coordinate changes gives, off shell, for each $\lambda$ and for general $a_4$ and $b_4$, $\partial_\mu(\sqrt{|g|}T^\mu{}_\lambda) - \sqrt{|g|}\,T^\mu{}_a\,\partial_\lambda e^a{}_\mu = \sum_\phi \mathrm{EL}_\phi\,\partial_\lambda\phi$ (`Noether_identity_diffeomorphisms_G`), and the invariance under the 28 local frame rotations makes the antisymmetric part of $T$ a combination of Euler-Lagrange expressions (`Noether_identity_local_Lorentz_G`). On shell, therefore, $T$ is symmetric and $\nabla_\mu T^\mu{}_\nu = 0$ for general solutions (`conservation_on_shell_general`); the sympy side verifies $\nabla_\mu T^\mu{}_\nu = 0$ for all eight $\nu$ after the on-shell substitution, with a negative control (`grassmann_emt_conservation_on_shell`, `grassmann_emt_conservation_negative_control`). The gravitational side satisfies the matching identities $\nabla_\mu E_{(k)}{}^\mu{}_\nu = 0$ (section 13).
- Exact solutions as test points. With $K = \gamma^{(4)}\gamma^{(0)}$ ($K^2 = 1$) and $F = e^{a_4/2}b_4^{-1}$, whose logarithmic derivative is $-v_g$ (`solution_matrix_square`), and for all functions $a_4$, $b_4$ and every real $z$: for $U = 0$ and $m = 0$, $\Psi = F(\sin^2 z)^{\alpha/2}(\cosh I + \sinh I\,K)\chi$ with constant $\chi$, $\alpha$ arbitrary and $I' = \tfrac32H(4\alpha + 1)e^{a_4}b_4^{-1/2}$ (`exact_solution_x4_x0_m0_G`); for $U = 0$, $\alpha = -\tfrac14$ and any $m$, $\Psi = F(\sin^2 z)^{-1/8}(\cos(mx_4) - \sin(mx_4)\gamma^{(4)})\chi$ (`exact_solution_x4_x0_quarter_G`); sympy `exact_solution_family_x4_x0`. Conservation of $T$ and $J$ holds exactly there; their $x_0$ dependence is a real scalar factor, so these are weak tests of conservation, and the general proof is the pair of Noether identities. An exact nonlinear homogeneous solution with $U = \frac{\lambda}{2}S^2$ and $m = 0$ exists in the explicit Grassmann algebra for all functions $a_4$, $b_4$: $\Psi = F\sum_k\big[Pc_k + \lambda S_0\,\eta_k\big]\theta_k$ with $P = \cosh I_0 + \sinh I_0\,K$, $I_0' = \tfrac32He^{a_4}b_4^{-1/2}$, $\eta_k = -P\gamma^{(4)}(I_c + I_sK)c_k$ with $I_c' = F^2\cosh 2I_0$, $I_s' = F^2\sinh 2I_0$, and $S_0 = \sum_{kl}\bar\theta_k\theta_l\,c_k^\dagger Cc_l$; then $S = e^{a_4}b_4^{-2}S_0$ (`exact_solution_nonlinear_homogeneous_G`; formula key `exact_solutions`; for the commuting field every solution of the reduced linear system gives one, `exact_solution_nonlinear_homogeneous_C`, sympy `exact_nonlinear_homogeneous_solution` for both statistics).

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

Diagonal components in the primordial field (no sum; `T_diagonal_components_G`, `grassmann_emt_equals_vielbein_variation_diagonal`; formula key `EMT_diagonal`): with the directional kinetic terms

$$
K_\mu = \frac{1}{2f_\mu}\big(\bar\Psi\gamma^{(\mu)}\partial_\mu\Psi - \partial_\mu\bar\Psi\gamma^{(\mu)}\Psi\big),\qquad \mathcal{L}_0 = \sum_\mu K_\mu - mS - U(S),
$$

$$
T^\mu{}_\mu = \mathcal{L}_0 - K_\mu .
$$

No spin-connection term survives in the diagonal components, because $\{\gamma^\mu, \Omega_\mu\} = 0$ for each $\mu$. The off-diagonal component $x_4$-$x_0$ is (`T_x4_x0_component_G`; formula key `EMT_offdiagonal_x4_x0`)

$$
T^{x_4}{}_{x_0} = -\tfrac14\big(B_{40} - e^{-a_4}b_4^{1/2}\cot z\,B_{04}\big),\qquad T^{x_0}{}_{x_4} = -e^{2a_4}b_4^{-1}\tan^2 z\;T^{x_4}{}_{x_0},
$$

with $B_{40} = \bar\Psi\gamma^{(4)}\partial_0\Psi - \partial_0\bar\Psi\gamma^{(4)}\Psi$ and $B_{04} = \bar\Psi\gamma^{(0)}\partial_4\Psi - \partial_4\bar\Psi\gamma^{(0)}\Psi$ ($\Omega_{x_0}$ drops out). For homogeneous on-shell configurations both $T^{x_4}{}_{x_0}$ and $T^{x_0}{}_{x_4}$ vanish identically (`grassmann_T_x4x0_homogeneous`). The field equations of section 13 require every off-diagonal component of the source to vanish; for a homogeneous configuration the other off-diagonal components are nonzero bilinears in general, whose vanishing is a separate condition on the state (section 13). The trace (off shell, an exact identity in both engines) and the on-shell kinetic sum are (`EMT_trace_G`, `grassmann_trace_on_shell`, `kinetic_sum_on_shell_G`)

$$
T^\mu{}_\mu = 7\sum_\mu K_\mu - 8\big(mS + U\big),\qquad \sum_\mu K_\mu = \big(m + U'(S)\big)S + \tfrac12\big(\bar\Psi E - \bar E\Psi\big),
$$

so on shell $\mathcal{L}_0 = SU' - U$ and $T^\mu{}_\mu = -mS + 7SU' - 8U = -mS + 3\lambda S^2$. For a diagonal tensor $T = \mathrm{diag}(p_0, p_3, p_3, p_3, -\rho, p_t, p_t, p_t)$ whose entries are functions of $x_0$ and $x_4$, the covariant divergence is, in all eight components (every real $z$, $\sigma_z$ cancels; `energy_exchange_equation` in both field-theory reports; formula key `energy_exchange`),

$$
\nabla_\mu T^\mu{}_{x_4} = -\partial_4\rho - 3a_4'\,(\rho + p_3) - 3h_4\,(\rho + p_t) - h_4\,(\rho + p_0),\qquad \nabla_\mu T^\mu{}_{x_0} = \partial_0 p_0 + 3H\cot z\,(p_0 - p_t),
$$

and $\nabla_\mu T^\mu{}_\nu = 0$ identically for $\nu = x_1, x_2, x_3, x_5, x_6, x_7$. Conservation is therefore exactly

$$
\partial_4\rho = -3a_4'\,(\rho + p_3) - 3h_4\,(\rho + p_t) - h_4\,(\rho + p_0),\qquad \partial_0 p_0 = -3H\cot z\,(p_0 - p_t) :
$$

the 3-space volume $e^{3a_4}$ dilutes $\rho + p_3$, and the block of the hidden direction and the extra times dilutes $\rho + p_t$ and $\rho + p_0$ with its rate $h_4$. For entries independent of $x_0$ the two conditions become $d\rho/dx_4 = -3a_4'(\rho + p_3) - 4h_4(\rho + p_t)$ and $p_0 = p_t$.

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

Homogeneous on-shell configurations (depending on $x_4$ only): $K_\mu = 0$ for $\mu \neq x_4$ and $K_{x_4} = (m + U')S$ (the scalar factor $e^{a_4/2}b_4^{-1}$ of $\Psi$ and $\bar\Psi$ cancels in $K_{x_4}$), hence (`grassmann_homogeneous_on_shell_rho_p`, `exact_solution_nonlinear_homogeneous_G`; formula key `EMT_homogeneous_on_shell`)

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

For the exact homogeneous solutions $e^{-a_4}b_4^2S = S_0$ is constant along $x_4$ (`exact_solution_nonlinear_homogeneous_G`; for the classical condensate of the field-equations record `condensate_S_law`), so $S = e^{a_4}b_4^{-2}S_0$ follows the inverse 7-volume, and for $\lambda \neq 0$ the ratio $w = \lambda S/(2m + \lambda S)$ drifts; on the background history $e^{a_4}b_4^{-2} \propto e^{-(5/3)a_4}$. This agrees with the energy-exchange equation: with equal pressures it reads $d\rho/dx_4 = -(3a_4' + 4h_4)(\rho + p)$, and $d\rho/dx_4 = (m + \lambda S)\,dS/dx_4 = -(2u - a_4')(mS + \lambda S^2) = -(3a_4' + 4h_4)(\rho + p)$. For dirac16complex all these quantities are Grassmann-algebra elements until they are evaluated as expectation values of the normal-ordered operators of section 12. The equation of state seen by a 3-space observer and its time dependence (the dark-sector hypotheses of SPEC section 8) are not computed in this document; they are investigated in `Revision/docs/DARK_SECTOR_HYPOTHESES`, whose verdict for dirac16complex is summarised in section 15.

## 11. Canonical quantisation in 4 + 4 dimensions and the Krein structure

The evolution time is $x_4$. The momentum conjugate to $\Psi_A$ (right derivative) is $\pi_A = \frac{i}{2}\sqrt{|g|}\,(\Psi^\dagger B)_A$ for the symmetric Lagrangian and $i\sqrt{|g|}\,(\Psi^\dagger B)_A$ for the first-order form; it depends on $\Psi^\dagger$ only, a second-class constraint as for Dirac's field (`canonical_momentum` in both reports). Up to a total divergence $\mathcal{L} = \Psi^\dagger K\,\partial_4\Psi - (\text{terms without }\partial_4)$ with $K = \sqrt{|g|}\,C\gamma^{(4)} = i\sqrt{|g|}\,B$, and the canonical (Dirac-bracket) anticommutator on a slice $x_4 = $ const is (`first_order_form_and_anticommutator`, `canonical_anticommutator_B`)

$$
\{\Psi_A(x), \Psi^\dagger_C(y)\}_{x_4 = y_4} = B_{AC}\,\frac{\delta^7(x - y)}{\sqrt{|g|}},\qquad \sqrt{|g|} = e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4} .
$$

With the Hamiltonian density $\mathcal{H} = \sqrt{|g|}\,\big[\Psi^\dagger\big(mC - \sum_{\mu\neq x_4}C\gamma^\mu D_\mu\big)\Psi + U(S)\big]$ (the unsymmetrised $\mathcal{L} = \Psi^\dagger K\partial_4\Psi - \mathcal{H}$ exactly), the Heisenberg equation $\partial_4\Psi = i[H, \Psi]$ equals the field equation solved for $\partial_4\Psi$, with the operator ordering of the classical expression (`Heisenberg_equation_reproduces_field_equation`, `hamiltonian_form_and_heisenberg_equation`).

**Theorem 2 (the canonical anticommutator forces a Krein structure).** Hypotheses: the canonical anticommutator above, and $\Psi^\dagger$ realised as the adjoint of $\Psi$ in a space with a positive-definite inner product. These are incompatible: there is no positive inner product with $\Psi^\dagger$ as the adjoint. *Proof.* $B$ has the eigenvalue $-1$ with multiplicity 8; for the exact unit vector $u_-$ with components $(u_-)_7 = -i/\sqrt2$, $(u_-)_{16} = 1/\sqrt2$ and all others zero, $Bu_- = -u_-$, and the smeared operator $X = \sum_A (u_-)_A^*\Psi_A(f)$ has $\{X, X^\dagger\} = (u_-^\dagger Bu_-)\,\lVert f\rVert^2 = -\lVert f\rVert^2 < 0$, whereas in a space with positive inner product $\{X, X^\dagger\} = XX^\dagger + X^\dagger X$ is a positive operator (`no_positive_inner_product` in both reports). Hence the state space carries an indefinite (Krein) inner product with fundamental symmetry $B$ ($B = B^\dagger$, $B^2 = 1$, signature (8,8)); equivalently, in a positive Hilbert space the canonical conjugate $\Psi^\dagger$ is not the Hilbert adjoint $\chi$ but $\Psi^\dagger = \chi B$, with $\{\Psi_A, \chi_C\} = \delta_{AC}$.

The one-particle Krein structure. The curved mode operator ($i\partial_4\Psi = h\Psi$ for $U = 0$) is $h = m(-i\gamma^{(4)}) + \sum_{a\neq x_4}\frac{1}{f_a}\,i\gamma^{(4)}\gamma^{(a)}\partial_a + ic_g\gamma^{(4)}\gamma^{(0)} - iv_g$; its last term is anti-Hermitian and compensates exactly the $x_4$ dependence of the measure, $\partial_4\sqrt{|g|} = 2v_g\sqrt{|g|}$. It is formally self-adjoint for the Krein form $\int\sqrt{|g|}\,u^\dagger Bv\,d^7x$, that is up to boundary terms (`Krein_form_conserved_curved`, `good_sector_hermiticity_curved`). The boundary term of the hidden direction does not vanish at the degenerate points $z = \pi/2 + n\pi$: $\sqrt{|g|}\,[u^\dagger(hv) - (hu)^\dagger v] = \partial_0(\sigma_zb_4^{3/2}(\sin^2 z)^{1/4}\,u^\dagger M_0 v) - i(\partial_4\sqrt{|g|})\,u^\dagger v$ with $M_0 = i\gamma^{(4)}\gamma^{(0)}$ in the good sector at $k = 0$, and the $x_0$ term vanishes where $\sin z = 0$ but not where $\cos z = 0$ (`good_sector_hermiticity_up_to_the_brane_flux`, both engines). The Krein form is therefore conserved, and $h$ self-adjoint, only with a boundary condition at the degenerate points (for example the fold conditions of the Kohn-Sham record, ASSUMED there); this record imposes none. For frozen coefficients (frame momenta $k_a$), plane waves $u\,e^{i(k\cdot x - Ex_4)}$ obey $Eu = h_k u$ with $h_k = m\beta + \sum_a k_a\alpha^a$, $\beta = -i\gamma^{(4)}$, $\alpha^a = -\gamma^{(4)}\gamma^{(a)}$; $\beta$ and $\alpha^{0,1,2,3}$ are Hermitian, $\alpha^{5,6,7}$ anti-Hermitian, $Bh_k = h_k^\dagger B$ (Krein self-adjoint), and (`mode_hamiltonian_good_sector`, `mode_hamiltonian_Krein_selfadjoint`, `mode_hamiltonian_B_selfadjoint_dispersion`)

$$
h_k^2 = \big(m^2 + k_0^2 + k_1^2 + k_2^2 + k_3^2 - k_5^2 - k_6^2 - k_7^2\big)\,I_{16} .
$$

Good sector (no dependence on the extra times, $k_5 = k_6 = k_7 = 0$): $h_k$ is Hermitian with eigenvalues $\pm E$, eight each, and commutes with $B$; $B$ also commutes with the curved terms $ic_g\gamma^{(4)}\gamma^{(0)}$ and $-iv_g$ (`good_sector_spectrum_and_B_sectors`). The curved mode operator is symmetric in this sector only up to the boundary term at the degenerate points (`good_sector_hermiticity_curved`, `good_sector_hermiticity_up_to_the_brane_flux`): on the good-sector functions that do not depend on $x_0$ (finite norm on each interval between degenerate points, $\int_0^{\pi/(12H)}\cot(6Hx_0)\sin^{1/2}(6Hx_0)\,dx_0 = 1/(3H)$) it acts as $A - iv_g$ with the matrix $A = -im\gamma^{(4)} + ic_g\gamma^{(4)}\gamma^{(0)}$, so $\Psi = e^{a_4/2}b_4^{-1}\chi$ with $i\partial_4\chi = A\chi$; $A$ is not Hermitian and has the square $(m^2 - c_g^2)I_{16}$: wherever $m^2 < c_g^2$ the instantaneous frequencies are imaginary, and on the background history ($b_4(0) = 1$) $c_g = \tfrac32He^{Hx_4/3}$ grows, so every mass falls below it at late $x_4$ (`good_sector_x0_independent_modes_without_boundary_condition`). Without a boundary condition at the degenerate points the good sector of the corrected metric therefore contains growing modes. Positive Fock realisation: $\Psi = \sum_s(b_s u_s + d_s^* v_s)$ with orthonormal eigenvectors $u_s$ (energy $+E$) and $v_s$ (energy $-E$), $\{b, b^*\} = \{d, d^*\} = 1$ on a positive Fock space, and $\Psi^\dagger = \chi B$, so that $\{\Psi_A, \Psi^\dagger_C\} = B_{AC}$. Exact examples (one momentum each, flat frame): Wolfram, $m = 3$, $k_1 = 4$ (the other momenta zero), $E = 5$, on the explicit fermionic Fock space of $2^{16}$ occupation states; sympy, $m = 2$, $(k_0, k_1, k_2, k_3) = (4, 1, 2, 0)$, $E = 5$. The Hamiltonian $\chi h_k\Psi$ has the vacuum value $-8E$ (the filled sea; $-40$ in the sympy example), and after normal ordering the energy is $+E$ for the particle $b_0^*|0\rangle$ and $+E$ for the antiparticle $d_0^*|0\rangle$; the charge $\Psi^\dagger B\Psi = \chi\Psi$ is $+1$ and $-1$ (`Fock_space_good_sector_example`, `good_sector_positive_fock_realisation`).

Expectation-value rule. In the positive realisation, $\langle u|{:}\Psi^\dagger M\Psi{:}|u\rangle = u^\dagger BMu$ for a particle and $-v^\dagger BMv$ for an antiparticle (verified for $M = C$, $-iC\gamma^{(4)}$, $-iC\gamma^{(1)}$, $C\gamma^{(2)}\gamma^{(3)}$, a dense integer matrix and a generic symbolic matrix). In the Krein-Fock realisation ($\Psi^\dagger$ the Krein adjoint, modes with $u_n^\dagger Bu_n = \epsilon_n$) the normalised expectation of ${:}\Psi^\dagger M\Psi{:}$ is $\epsilon_n u_n^\dagger Mu_n$, which equals $u_n^\dagger BMu_n$ when $Bu_n = \epsilon_n u_n$ and not for a Krein-boosted mode (`Fock_space_good_sector_example`, `good_sector_positive_fock_realisation`, `expectation_value_rule`).

Extra-time modes. With extra-time momentum, $E^2 = m^2 + k_s^2 - k_t^2$ is negative when $k_t^2 > m^2 + k_s^2$; exact example $m = 1$, $k_5 = 2$: $E = \pm i\sqrt3$, modes growing like $e^{\sqrt3\,x_4}$. The growth rate has no upper bound as the extra-time momentum grows (`extra_time_growth_rates_unbounded`). In the metric the frame momentum $k_{(5)} = e^{a_4}b_4^{-1/2}(\sin^2 z)^{-1/12}k_{x_5}$ grows as the block deflates (on the background history the scale factor $e^{-a_4}b_4^{1/2}$ is proportional to $e^{-a_4/3}$), so every extra-time mode eventually enters the growing regime (a local-frame statement); extra-time momenta mix the $B = \pm1$ sectors (`extra_time_modes_grow`, `mode_hamiltonian_good_sector`, `good_sector_spectrum_and_B_sectors`). Krein structure of the one-particle eigenspaces in flat 4+4 space (pairing record): every eigenspace of REAL frequency, $E^2 > 0$, with or without extra-time momentum, has Krein inertia (4,4) (proved for every real frequency: `Q_one_particle_Krein_inertia_real_frequencies`, `Q.one_particle_Krein_inertia_proof`), while the eigenspaces of imaginary or zero frequency, those of the growing modes, are Krein-neutral, $B$ vanishes on them identically (`Q_one_particle_complex_and_zero_frequencies_Krein_neutral`, `Q.one_particle_complex_frequency_Krein_neutral`; for $m = 1$, $k_5 = 2$ both 8-dimensional eigenspaces of $\pm i\sqrt3$).

Scope: the positive Fock realisation is constructed and checked for single good-sector momenta with frozen coefficients; together with the formal (up to the boundary term at the degenerate points) Hermiticity of the curved good-sector mode operator and the formal conservation of the Krein form this is the quantisation recorded here. A complete construction for the interacting field ($\lambda \neq 0$), for the extra-time sector with its growing modes, and of the field algebra on a whole slice is not part of this record (section 15).

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
- The operator form for $\lambda \neq 0$ in a finite model (record `Revision/theory/fock_quartic/`, 2026-10-08; one Python checker with sympy and its own exact engine for the canonical anticommutation relations, no Wolfram counterpart; 21 of 21 checks pass; it works in the flat frame and does not depend on the metric). The model is the positive fermionic Fock space ($\Psi^\dagger = \chi B$) of one good-sector plane-wave mode set with frozen coefficients: flat frame, volume 1, 16 modes, $2^{16}$ states, at rest ($k = 0$, symbolic $m$) and at $m = 3$, $k_1 = 4$ (the other momenta zero); at $\lambda = 0$ it reproduces the Fock example of section 11 (`control_record_Fock_example`). With the Wick-ordered potential $U = \frac{\lambda}{2}{:}SS{:}$ in the Hamiltonian and $K_\mu$ defined as Wick products with the Heisenberg derivative of the field, ${:}\sum_\mu K_\mu{:} = {:}(m + U'(S))S{:}$ holds as an exact operator identity on every state of the model, for the solution of the interacting operator field equation (`trace_identity_operator_identity_wick`), and at $k = 0$ the homogeneous values $\hat\rho = {:}mS + U{:}$ and $\hat p = {:}SU' - U{:}$ are operator identities in the same sense (`homogeneous_rho_p_operator_identities_wick`). Of the tested choices (four orderings of the potential, Wick product or vacuum subtraction on the left, two right-hand sides) only this one works: every other combination (30 of them on the two mode sets) fails by a nonzero one-body operator (sometimes plus a constant) linear in $\lambda$, and already in expectation values, at $k = 0$ on every state except the vacuum of the mode set (`trace_identity_fails_for_every_other_combination`, `expectation_classes_M0`, `expectation_values_M1`); so the identity holds in this model if and only if the potential and the energy-momentum tensor are both Wick ordered. It also fails for the free dynamics, so it is a statement about solutions of the interacting operator field equation (`negative_control_free_dynamics`). On states with $n$ quanta at $k = 0$, $\rho = mn + \frac{\lambda}{2}n(n - 1)$ and $p = \frac{\lambda}{2}n(n - 1)$, so $\langle{:}U(S){:}\rangle \neq U(\langle{:}S{:}\rangle)$ (`homogeneous_expectation_values_are_not_U_of_expectation`). Nothing is proved for the field on a whole slice (many momenta), for the curved $x_0$ dependence with its boundary term at the degenerate points, or for the extra-time sector; the model gives no numerical expectation value for a physical many-fermion state.
- Numerical expectation values of $\hat T$ for many-fermion states are computed only in the Kohn-Sham approximation (`Revision/kohn_sham/`, document `Revision/docs/KOHN_SHAM_DEFLATING_FIELD`); this document quotes only quantities derived from them, in section 13 (the source conditions and the analysis of the $a_4$ and $b_4$ equations with the Kohn-Sham source) and in section 15 (the equation-of-state values $w_{\rm eff}$ of the Kohn-Sham gas from the dark-sector record).
- The Grassmann-algebra tensor of sections 9 and 10 obeys the identities of section 8 (symmetry and conservation on shell); the operator inherits them for the bilinear ($\lambda = 0$) part, where they are linear in the field equations; for the quartic part they are not verified as operator statements (the finite model above decides the trace identity and the homogeneous $\rho$ and $p$, not symmetry or conservation).

## 13. The field equations for a4[x4] and b4[x4] with dirac16complex as the source

Einstein-Lovelock gravity (SPEC section 5), with the Lovelock tensors computed with the generalised Kronecker delta in `Revision/gkd_lovelock` and recomputed in both verifiers of the field-equations branch for general $a_4$ and $b_4$ (for example `P3_direct_equals_gkd_branch_monomials`, `P1_direct_equals_minus_4_Einstein` and `P4_vanishes_pigeonhole`; sympy `P3_equals_gkd_branch_monomials`; the Einstein tensor equals the independent record of the corrected metric, `einstein_equals_metric_warped_record`):

$$
\sum_{k=1}^{3}\alpha_k\,E_{(k)}{}^\mu{}_\nu + \Lambda\,\delta^\mu_\nu = \kappa\,T^\mu{}_\nu,\qquad E_{(k)} = -\frac{P_{(k)}}{2^{k+1}},\qquad E_{(1)} = G,
$$

with $\alpha_1 = 1$ for Einstein gravity and the source $T^\mu{}_\nu = \mathrm{diag}(p_0, p_3, p_3, p_3, -\rho, p_t, p_t, p_t)$. The left-hand sides are divergence-free (`E1_divergence_free`, `E2_divergence_free`, `E3_divergence_free` in both reports). Every mixed Riemann component is free of $x_0$ and sectional (`mixed_riemann_free_of_x0`, `mixed_riemann_only_sectional` in both reports), so every component of $E_{(k)}$ is a polynomial in $H$, $a_4'$, $a_4''$, $u$, $v$ and $k = e^{2a_4}/b_4$ (`lovelock_variables`; sympy `riemann_entries_polynomial`); every $E_{(k)}$ is diagonal, with $x_1 = x_2 = x_3$ and $x_0 = x_5 = x_6 = x_7$ (`independent_components`, `P1_structure`, `P2_structure`, `P3_structure` in both reports). The independent diagonal components (formula key `lovelockTensors` of `Revision/field_equations_a4/a4-equations.json`; `json_lovelock_components`), with $E_{(k)}{}^{x_5}{}_{x_5} = E_{(k)}{}^{x_0}{}_{x_0}$ for $k = 1, 2, 3$:

$$
\begin{aligned}
E_{(1)}{}^{x_0}{}_{x_0} &= -3 (a_4')^{2} + \tfrac{3}{2} a_4' u - \tfrac{3}{2} u^{2} - \tfrac{3}{2} v + 3 H^{2} k
\end{aligned}
$$

$$
\begin{aligned}
E_{(1)}{}^{x_1}{}_{x_1} &= -5 (a_4')^{2} + 6 a_4' u + 2 a_4'' - \tfrac{5}{2} u^{2} \\
&\quad - 2 v + 6 H^{2} k
\end{aligned}
$$

$$
\begin{aligned}
E_{(1)}{}^{x_4}{}_{x_4} &= 3 (a_4')^{2} - \tfrac{3}{2} u^{2} + 6 H^{2} k
\end{aligned}
$$

$$
\begin{aligned}
E_{(2)}{}^{x_0}{}_{x_0} &= 12 (a_4')^{4} - 12 (a_4')^{3} u + 18 (a_4')^{2} u^{2} + 12 (a_4')^{2} v \\
&\quad + 48 (a_4')^{2} H^{2} k + 24 a_4' a_4'' u - \tfrac{15}{2} a_4' u^{3} - 12 a_4' u v \\
&\quad + 6 a_4' u H^{2} k - 6 a_4'' u^{2} + 24 a_4'' H^{2} k - \tfrac{3}{4} u^{4} \\
&\quad - \tfrac{3}{2} u^{2} v + 3 u^{2} H^{2} k + 6 v H^{2} k
\end{aligned}
$$

$$
\begin{aligned}
E_{(2)}{}^{x_1}{}_{x_1} &= 28 (a_4')^{4} - 48 (a_4')^{3} u - 48 (a_4')^{2} a_4'' + 20 (a_4')^{2} u^{2} \\
&\quad + 16 (a_4')^{2} v + 48 (a_4')^{2} H^{2} k + 32 a_4' a_4'' u + 6 a_4' u^{3} \\
&\quad - 24 a_4' u H^{2} k - \tfrac{15}{4} u^{4} - 6 u^{2} v + 18 u^{2} H^{2} k \\
&\quad + 24 v H^{2} k - 12 H^{4} k^{2}
\end{aligned}
$$

$$
\begin{aligned}
E_{(2)}{}^{x_4}{}_{x_4} &= -36 (a_4')^{4} + 36 (a_4')^{2} u^{2} - 48 (a_4')^{2} H^{2} k - 12 a_4' u^{3} \\
&\quad + 48 a_4' u H^{2} k - \tfrac{3}{4} u^{4} + 6 u^{2} H^{2} k - 12 H^{4} k^{2}
\end{aligned}
$$

$$
\begin{aligned}
E_{(3)}{}^{x_0}{}_{x_0} &= -72 (a_4')^{6} + 108 (a_4')^{5} u - 216 (a_4')^{4} u^{2} - 108 (a_4')^{4} v \\
&\quad - 216 (a_4')^{4} H^{2} k - 432 (a_4')^{3} a_4'' u + 171 (a_4')^{3} u^{3} + 216 (a_4')^{3} u v \\
&\quad + 108 (a_4')^{3} u H^{2} k + 324 (a_4')^{2} a_4'' u^{2} - 432 (a_4')^{2} a_4'' H^{2} k - \tfrac{81}{2} (a_4')^{2} u^{4} \\
&\quad - 81 (a_4')^{2} u^{2} v + 54 (a_4')^{2} u^{2} H^{2} k + 108 (a_4')^{2} v H^{2} k - 54 a_4' a_4'' u^{3} \\
&\quad + 216 a_4' a_4'' u H^{2} k
\end{aligned}
$$

$$
\begin{aligned}
E_{(3)}{}^{x_1}{}_{x_1} &= -216 (a_4')^{6} + 432 (a_4')^{5} u + 720 (a_4')^{4} a_4'' - 180 (a_4')^{4} u^{2} \\
&\quad - 144 (a_4')^{4} v - 144 (a_4')^{4} H^{2} k - 576 (a_4')^{3} a_4'' u - 108 (a_4')^{3} u^{3} \\
&\quad + 144 (a_4')^{3} u H^{2} k + \tfrac{189}{2} (a_4')^{2} u^{4} + 108 (a_4')^{2} u^{2} v - 180 (a_4')^{2} u^{2} H^{2} k \\
&\quad - 144 (a_4')^{2} v H^{2} k - 216 (a_4')^{2} H^{4} k^{2} + 72 a_4' a_4'' u^{3} - 288 a_4' a_4'' u H^{2} k \\
&\quad - 18 a_4' u^{5} - 36 a_4' u^{3} v + 72 a_4' u^{3} H^{2} k + 144 a_4' u v H^{2} k \\
&\quad - 9 a_4'' u^{4} + 72 a_4'' u^{2} H^{2} k - 144 a_4'' H^{4} k^{2}
\end{aligned}
$$

$$
\begin{aligned}
E_{(3)}{}^{x_4}{}_{x_4} &= 360 (a_4')^{6} - 540 (a_4')^{4} u^{2} + 432 (a_4')^{4} H^{2} k + 360 (a_4')^{3} u^{3} \\
&\quad - 864 (a_4')^{3} u H^{2} k - \tfrac{135}{2} (a_4')^{2} u^{4} + 324 (a_4')^{2} u^{2} H^{2} k - 216 (a_4')^{2} H^{4} k^{2}
\end{aligned}
$$

The independent field equations (formula key `generalSource`):

- constraint ($x_4$): $\sum_k\alpha_k E_{(k)}{}^{x_4}{}_{x_4} + \Lambda = -\kappa\rho$; it contains $a_4'$, $u$ and $k$ but neither $a_4''$ nor $v$ nor $x_0$ (`constraint_first_order` in both reports);
- 3-space ($x_1 = x_2 = x_3$): $\sum_k\alpha_k E_{(k)}{}^{x_1}{}_{x_1} + \Lambda = \kappa p_3$;
- hidden direction and extra times ($x_0 = x_5 = x_6 = x_7$): $\sum_k\alpha_k E_{(k)}{}^{x_0}{}_{x_0} + \Lambda = \kappa p_0 = \kappa p_t$;
- every off-diagonal component: $0 = \kappa T^\mu{}_\nu$ (the left-hand sides vanish identically).

The field equations therefore require $p_0 = p_t$ and a source without off-diagonal components (unlike the metric of 2026-10-14, whose Lovelock tensors had an off-diagonal pair $E^{x_4}{}_{x_0} \propto \cot z\,u$). The 3-space and hidden-direction equations are linear in $(a_4'', v)$, with a Jacobian $J$ whose determinant (formula key `secondOrderJacobianDet`) is $-3$ in Einstein gravity ($-3/b_4$ in the variables $(a_4'', b_4'')$, `einstein_second_order_system`); where $\det J \neq 0$ they determine $a_4''$ and $v = (b_4'/b_4)'$ from the source, while the constraint is first order (`second_order_system_a4pp_vv`, `second_order_system`). The remaining conditions:

- $x_0$-dependence: since the left-hand sides do not depend on $x_0$, every diagonal component of $T^\mu{}_\nu$ must be independent of $x_0$ (formula key `x0_dependence`);
- constraint propagation (Bianchi identity): $\frac{d}{dx_4}\sum_k\alpha_k E_{(k)}{}^{x_4}{}_{x_4} = 3a_4'\sum_k\alpha_k\big(E^{x_1}{}_{x_1} - E^{x_4}{}_{x_4}\big) + 4h_4\sum_k\alpha_k\big(E^{x_0}{}_{x_0} - E^{x_4}{}_{x_4}\big)$ identically, with $k' = k(2a_4' - u)$ (`constraint_propagation_bianchi`, `bianchi_x4`); with the conservation law of section 9 the derivative of the constraint follows from the other components (`conservation_components` in both reports).

For a prescribed history the equations give the source it requires (formula key `sourceRequiredByGivenHistory`); whether a state of the field supplies it is a separate question.

Einstein gravity ($\alpha_1 = 1$, $\alpha_2 = \alpha_3 = 0$; `einstein_components`; formula key `einstein`):

$$
\begin{aligned}
3 (a_4')^{2} - \tfrac{3}{2} u^{2} + 6 H^{2} k + \Lambda &= -\kappa\rho \\
-5 (a_4')^{2} + 6 a_4' u + 2 a_4'' - \tfrac{5}{2} u^{2} - 2 v + 6 H^{2} k + \Lambda &= \kappa p_3 \\
-3 (a_4')^{2} + \tfrac{3}{2} a_4' u - \tfrac{3}{2} u^{2} - \tfrac{3}{2} v + 3 H^{2} k + \Lambda &= \kappa p_0 = \kappa p_t
\end{aligned}
$$

The flat member $a_4 = 0$, $b_4 = H^2(x_4 - c)^2$ solves the vacuum equations with $\Lambda = 0$ (`einstein_flat_vacuum`); no exponential history is a vacuum solution, for any $\Lambda$ (`einstein_no_exponential_vacuum`). The null combinations are $\kappa(\rho + p_0) = -\tfrac32\big(4(a_4')^2 - a_4'u + 2H^2k + v\big)$ and $\kappa(\rho + p_3) = -8(a_4')^2 + 6a_4'u + 2a_4'' - u^2 - 2v$ (`einstein_null_combinations`): wherever $v \geq 0$ and $4(a_4')^2 - a_4'u \geq 0$ the source violates the null energy condition along $x_4 + x_0$ (for $\kappa > 0$). The second-order equations have the Jacobian $\begin{pmatrix}2 & -2/b_4\\ 0 & -3/(2b_4)\end{pmatrix}$ with respect to $(a_4'', b_4'')$ (`einstein_second_order_system`).

Exponential histories (formula key `exponentialHistory`). On $a_4 = AHx_4 + a_0$, $b_4 = b_4(0)\,e^{\beta AHx_4}$ ($a_4' = AH$, $u = \beta AH$, $a_4'' = v = 0$; 3-space scale factor $e^{AHx_4}$, scale factor of the block $e^{-(1 - \beta/2)AHx_4}$; $k = (e^{2a_0}/b_4(0))e^{(2 - \beta)AHx_4}$, constant exactly for $\beta = 2$ or $A = 0$) the field equations require a diagonal source with $p_0 = p_t$ whose entries are polynomials of degree at most 2 in $k$, for any $\alpha_k$ and $\Lambda$ (`exponential_history_required_source`; formula key `requiredSource`): the source is constant only for $\beta = 2$ or $A = 0$. Written as functions of $k$ the required entries contain $A$ only through $A^2$: whether 3-space inflates or deflates is a choice of sign (an initial condition) and is not selected by the equations.

The author's weights (formula key `authorWeights`): $\alpha_k = w_k/H^{2k}$ with $w = (1, \tfrac{1}{32}, \tfrac{1}{1152})$ and $\Lambda = -10$ in the convention of this record (the notebook's $\Lambda = 10$; `Dirac_Einstein-Lovelock_4+4_Nash.nb`, Out[134] and Out[135]). On the background history

$$
a_4 = Hx_4,\quad b_4 = b_4(0)\,e^{(4/3)Hx_4}
$$

of SPEC section 1 ($A = 1$, $\beta = \tfrac43$, $b_4(0) = 1$, $k = e^{(2/3)Hx_4}$; the extra times still deflate exponentially, with the scale factor $e^{-a_4}b_4^{1/2} \propto e^{-a_4/3}$) the field equations require, at $H = 1$, the source (key `historySource_kappaT_minus_Lam`; `author_weights_history_source`)

$$
\begin{aligned}
-\kappa\rho - \Lambda &= -\tfrac{9}{16} k^{2} + \tfrac{161}{24} k + \tfrac{121}{432} \\
\kappa p_3 - \Lambda &= -\tfrac{9}{16} k^{2} + \tfrac{1601}{216} k - \tfrac{5359}{3888} \\
\kappa p_0 - \Lambda = \kappa p_t - \Lambda &= \tfrac{79}{16} k - \tfrac{497}{144}
\end{aligned}
$$

a diagonal, $x_0$-independent source with $p_0 = p_t$ that grows with $x_4$ (powers of $k$) and is anisotropic, $\kappa(p_3 - p_0) = -\tfrac{9}{16}k^2 + \tfrac{1069}{432}k + \tfrac{2015}{972}$. It is not a vacuum solution, and the record uses it as a PRESCRIBED background. With the author's weights no exponential history is a vacuum solution (`author_weights_no_exponential_vacuum`); in Einstein-Gauss-Bonnet gravity ($\alpha_1 = 1$, $\alpha_3 = 0$) there is no vacuum exponential history where $k$ varies, and for constant $k = k_0 > 0$ ($\beta = 2$, any $A$) the vacuum histories are exactly those with $k_0 \neq A^2$ and the tuned couplings $\alpha_2 = -1/(4H^2(A^2 - k_0))$ and $\Lambda = 3H^2(A^4 + 3A^2k_0 + k_0^2)/(A^2 - k_0)$ (`egb_exponential_vacuum_branches`, `egb_no_vacuum_where_k_varies`); on these constant-$k$ histories the scale factor $e^{-a_4}b_4^{1/2}$ of the extra times is constant, so they do not deflate, and none of them is a history of this record.

Specialisation to dirac16complex. The source is the energy-momentum tensor of section 9 with the declared sign $\sigma_T = +1$ (formula key `emtConvention` of `fields`: $T^\mu{}_\nu = \sigma_T(-K^{(\mu}{}_{\nu)} + \delta^\mu_\nu\mathcal{L}_0)$, the convention $\rho = -T^{x_4}{}_{x_4}$ of SPEC section 4; the relative sign of the gravitational and matter actions is carried as the parameter $\sigma_T$ in the field-equations record and is not fixed by a Revision check). For the quantised field every bilinear is replaced by the expectation value of its normal-ordered operator in the state (section 12), with $k_\mu = K_\mu$:

$$
\begin{aligned}
\rho &= \langle{:}k_4{:}\rangle - \langle{:}\mathcal{L}_0{:}\rangle, & p_3 &= \langle{:}\mathcal{L}_0{:}\rangle - \langle{:}k_1{:}\rangle, \\
p_t &= \langle{:}\mathcal{L}_0{:}\rangle - \langle{:}k_5{:}\rangle, & p_0 &= \langle{:}\mathcal{L}_0{:}\rangle - \langle{:}k_0{:}\rangle,
\end{aligned}
$$

and the equations become (entry `dirac16complex` of the formula key `fields` of the field-equations record): the constraint $\sum_k\alpha_k E_{(k)}{}^{x_4}{}_{x_4} + \Lambda = -\kappa\big(\langle{:}k_4{:}\rangle - \langle{:}\mathcal{L}_0{:}\rangle\big)$; the 3-space and hidden-direction equations with these entries; the condition $p_0 = p_t$, that is $\langle{:}k_0{:}\rangle = \langle{:}k_5{:}\rangle$; every off-diagonal expectation value $\langle{:}T^\mu{}_\nu{:}\rangle$, $\mu \neq \nu$, must vanish, and every diagonal expectation value must be independent of $x_0$. For a homogeneous configuration the off-diagonal components are combinations of the 24 three-gamma bilinears $\bar\Psi\gamma^{(a)}\gamma^{(b)}\gamma^{(c)}\Psi$ with $\{a, b, c\} = \{0, i, 4\}$, $\{0, i, t\}$, $\{i, 4, t\}$ and $\{0, 4, t\}$, with coefficients depending on $H$, $a_4'$, $u$, $e^{a_4}$, $b_4$ and $x_0$, derived for the classical homogeneous condensate (`condensate_offdiagonal_are_three_gamma_bilinears`, `authorT16_condensate_offdiagonal_three_gamma`); for dirac16complex their expectation values must vanish.

**Statement (sources of the homogeneous form).** The classical homogeneous condensate of the field-equations record has, on shell, $K^{x_4}{}_{x_4} = (m + U')S$, $K^\mu{}_\mu = 0$ for every other direction and $K^{x_4}{}_{x_0} = 0$ (`condensate_kinetic_tensor_diagonal`), hence $\rho = mS + U$ and $p_3 = p_t = p_0 = SU' - U$, with $e^{-a_4}b_4^2S$ constant (`condensate_S_law`). A source of this form (equal pressures and no off-diagonal component) needs $\sum_k\alpha_k(E^{x_1}{}_{x_1} - E^{x_0}{}_{x_0}) = 0$; on the exponential histories it is impossible in Einstein gravity, and with the author's weights possible only on constant-$k$ histories ($k_0 = (16 + 2A^2)/(2 + A^2)$ on $\beta = 2$, $k_0 = 8$ on the history $A = 0$ with constant $a_4$ and $b_4$, which section 2 excludes; on these constant-$k$ histories the scale factor $e^{-a_4}b_4^{1/2}$ of the extra times is constant, so they do not deflate, and none of them is a history of this record), not decided further; histories that are not exponential are not decided (`condensate_source_equal_pressures` in both reports). A state of dirac16complex whose normal-ordered expectation values depend on $x_4$ only, have $\langle{:}k_\mu{:}\rangle = 0$ for $\mu \neq x_4$ and vanishing off-diagonal expectation values gives a source of the same form, so the same conclusions apply to it: the field equations contain the state only through $\rho$, $p_3$, $p_t$ and $p_0$. In particular no such state is the source of the background history, which needs $p_3 \neq p_0$. If in addition the operator form of the on-shell identity of section 12 holds (an assumption for $\lambda \neq 0$), then $\rho = \langle{:}mS + U{:}\rangle$ and $p = \langle{:}SU' - U{:}\rangle$.

**The Kohn-Sham states as a source.** As the source of these equations, `Revision/SPEC.md` section 7 names the Kohn-Sham energy-momentum tensor of the Kohn-Sham record in `Revision/kohn_sham/`, which is described in section 11 of the document `Revision/docs/KOHN_SHAM_DEFLATING_FIELD`. By the statements above an admissible source must satisfy four conditions: (C1) every component is independent of $x_0$, for every $a_4$ and $b_4$; (C2) $p_0 = p_t$; (C3) there is no off-diagonal component, $T^{x_4}{}_{x_0} = 0$; (C4) on the background history with the author's weights and $\Lambda = -10$ it is the source quoted above (`A1_hidden_equals_extra_times_and_no_offdiagonal`, `A6_history_source_reproduced`). The recorded states (75 ground-state profiles on the history $a_4 = Hx_4$, $b_4 = e^{(4/3)Hx_4}$, $b_4(0) = 1$, at the slices $a_{4,0} = 0, 0.5, 1, 1.5, 2$ of the record; 70 of them with a nonzero energy-momentum tensor) are not an admissible source (`Revision/field_equations_a4/reports/ks-source-conditions.json`, Python: 5 of 5 checks pass):

- C1 fails for every nonzero state and for every $a_4(x_4)$ and $b_4(x_4)$: the energy density varies along the hidden coordinate, $(\max\rho - \min\rho)/\max|T| \geq 0.456213$ (`ks_profiles_depend_on_x0`);
- C2 holds to rounding for exactly the 10 nonzero states with $\lambda = 0$, whose occupied orbitals are fold-band orbitals without hidden kinetic pressure, and fails for every one of the 60 states with $\lambda \neq 0$ ($\max_y|p_0 - p_t|/\max|T| \geq 0.080929$; `ks_hidden_pressure_condition`): the interaction bends the orbitals;
- C3 holds for every recorded state (`ks_offdiagonal_condition`);
- C4 fails: the history needs $\kappa\rho = 3.57407$ at $a_{4,0} = 0$ and $-7.63383$ at $a_{4,0} = 2$, a source whose energy density changes sign along it, and the ratios $(p_3/\rho, p_0/\rho, p_t/\rho)$ of the Kohn-Sham sources, averaged over $x_0$ per proper volume, differ from the needed ratios (which do not depend on the unknown $\kappa$) by at least 1.3733 at every recorded state with a nonzero energy density (`ks_history_is_a_prescribed_background`);
- the five states with an identically vanishing tensor (the free $N = 8$ zero modes) are a zero source, which is not admissible either, because no exponential history is a vacuum solution for the author's weights (`ks_zero_source_states_listed`).

**The field equations for $a_4$ and $b_4$ with the Kohn-Sham source (`Revision/field_equations_a4/ks_source`).** A separate analysis (`Revision/field_equations_a4/ks_source/reports/ks-source-a4.json`, Python: 19 of 19 checks pass) refines this and asks what the equations would do with the Kohn-Sham source. Exact: without an off-diagonal source the $x_0$ component of the conservation law is $\partial_0 p_0 + 3H\cot z\,(p_0 - p_t) = 0$, that is $\partial_y p_0 + 3H(p_0 - p_t) = 0$ in the Kohn-Sham coordinate $y = \ln|\sin z|/(6H)$ (`A4_x0_conservation_in_y`). The recorded states satisfy it (largest residual 1.21233e-05 of the largest term on the output grid of the 70 nonzero profiles; `B2_x0_conservation_on_every_profile`), so they fail the field equations because their components depend on $x_0$, not because conservation fails: the L1 mismatch of the energy density from its hidden-direction average (with the volume weight $e^{3Hy}$; 0 for an $x_0$-independent source) lies between 0.147738 and 0.738255 (`B3_hidden_direction_mismatch`), and for $\lambda \neq 0$ the condition $p_0 = p_t$ fails even after averaging over $x_0$ (relative violation $\geq 0.00613418$; `C1_averaged_hidden_pressure_condition`).

The free gas ($\lambda = 0$, $N = 592$ and 2352) is an exact fold-band gas: averaged over $x_0$ per proper volume it is $\bar\rho = Cb_4^{-2}$ with $\bar p_3 = \bar\rho/3$ and $\bar p_0 = \bar p_t = 0$ along the dense history, to 2.88658e-15 ($C = 0.034125$ and 0.216249; `D0_free_gas_average_exact`), a source of the $x_0$-averaged equations that conserves energy for every $a_4$ and $b_4$ (`A5_free_fold_band_gas_conserves_energy`) as long as the gas stays on the fold band. It is not the source of the background history: with the author's weights the history needs $\kappa\rho = 3.57407$ at $a_4 = 0$ and $-7.63383$ at $a_4 = 2$, while the averaged free gas $N = 2352$ has $\bar\rho = 0.216249$ and $0.00104404$ there, so $\kappa$ would have to run from 16.5276 to $-7311.81$ along the history, and no constant $\kappa$ makes the gas the source (`C3_record_history_not_sourced_by_the_gas`). The averaged gas of $N = 592$ and 2352 has $\bar\rho > 0$ and $\bar\rho + \bar p_3 > 0$ in all 50 nonzero states, while the 10 nonzero $N = 8$ states with $\lambda > 0$ (only zero-momentum levels, pure interaction energy) violate the averaged null energy condition along 3-space (`C4_source_signs`).

In a stated APPROXIMATION (the $x_0$-dependent source replaced by its average over $x_0$ per proper volume, a dimensional reduction that C1 shows is not exact; the averaged free gas as the source; for the author's weights, with $\Lambda = -10$, the constraint at $x_4 = 0$ fixes $\kappa$, while for the three other theories $\sigma_0 = \kappa\bar\rho(0)/H^2$ is CHOSEN at the six values $-10, -1, -1/10, 1/10, 1, 10$ and the constraint fixes $\Lambda$) the $x_0$-averaged equations, started on the background history ($a_4'(0) = H$, $u(0) = \tfrac43H$, $b_4(0) = 1$), do not follow it. With the author's weights the constraint fixes $\kappa\bar\rho(0) = 3.57407$ ($\kappa > 0$, since $\bar\rho > 0$), and the second-order system becomes singular at $x_4 = 0.428813/H$ ($a_4 = 0.361572$, $b_4 = 0.862627$, $a_4'/H = 0.978369$, $u/H = -2.60176$, against 1 and $\tfrac43$ on the history; `D2_author_weights_from_the_record_history`). Over 38 cases (the two free series, with the author's weights and with three further theories, Einstein, Einstein-Gauss-Bonnet and cubic Lovelock gravity, each at the six CHOSEN values of $\sigma_0$) the outcomes are $a_4$ turning 24 times ($a_4'$ reaches 0), regular 6 times (through $x_4 = 2/H$), runaway 4 times and singular 4 times (`D4_outcomes`); the six regular cases are those with $\sigma_0 = -10$, a negative $\kappa$ for this gas of positive energy density (every case: `Revision/field_equations_a4/ks_source/results/ks-source-a4-cases.csv`). The integration gives the same outcomes at two step sizes and keeps the constraint (`D1_two_step_sizes_agree`, `D3_constraint_kept_along_the_solutions`). These are statements of that approximation, not of the field equations, and nothing about $a_4$ or $b_4$ is derived from them.

The Kohn-Sham history $a_4 = Hx_4$, $b_4 = b_4(0)e^{(4/3)Hx_4}$ is therefore a PRESCRIBED background for test fields, without back-reaction; the energies, pressures and equations of state of the Kohn-Sham gas along it (section 15) are not consequences of the coupled field equations.

## 14. Relation to the pairing theorems

The pairing theorems of SPEC section 9 use the Lagrangian, the field equations and the energy-momentum tensor of this document; their full statements, hypotheses and limits are in `Revision/docs/PAIR_CREATION_PROOFS.md`. For dirac16complex, in brief:

- T1 (chirality): $\mathcal{L}_{m,\lambda}[\Gamma\Psi] = -\mathcal{L}_{-m,-\lambda}[\Psi]$, solutions of the $(m, \lambda)$ equations are mapped to solutions of the $(-m, -\lambda)$ equations, $T \to -T$ and $J \to -J$, in every gravitational field, the corrected metric included; the total energy-momentum and the total current of the pair vanish identically (Wolfram `T1_Lagrangian_primordial_grassmann` and `T1_energy_momentum_primordial_grassmann`, sympy `T1.metric.grassmann.pair_total_emt_zero`).
- T2 (chirality combined with a Pin(4,4) reflection of character $-1$, realised in the primordial field by the isometry $z \to \pi - z$ across the fold $z = \pi/2$ between the two halves of a cell; the corrected metric has no Z2 orbifold): $(m, \lambda) \to (-m, \lambda)$, $\mathcal{L} \to +\mathcal{L}$, with equal, not opposite, energy-momentum (`T2_mirror_Lagrangian_grassmann`, `T2_mirror_energy_momentum_and_current_grassmann`; sympy `T2.metric.grassmann.emt`).
- Quantum reading: the chirality image $\Gamma\Psi$ carries the Krein metric $-B$; there is no cancellation between two independently quantised universes (`Q_Krein_metric_of_images`, `Q_no_identification_of_independent_universes`; sympy `Q.no_cancellation_independent_universes`).
- T3 (the Kohn-Sham level): the block map of $\Gamma$ with the two fold conditions exchanged and the tip angle $\theta \to \pi - \theta$ maps every self-consistent instantaneous Kohn-Sham state with $(m, \lambda, \theta)$ onto one with $(-m, +\lambda, \pi - \theta)$, with equal levels, occupations, Kohn-Sham energies and energy-momentum profiles, and $S \to -S$; both fold conditions are filled (ASSUMED) (`T3_energies_and_emt_profiles_equal`, `T3_exact_k0_spectra`, `T3_fold_conditions_exchanged`; sympy `T3.energies_and_emt_profiles_equal`).
- Completion of T3 (2026-10-08): with the expectation rule of the canonical quantisation (section 11) the image state has $\rho' = -\Gamma\rho\Gamma$, so $n$ is unchanged, $S$ and $Q$ change sign, and every component of the 16-component energy-momentum tensor and of the current of the $(-m, +\lambda)$ image state equals that of the original state (statement S6; `T3C_krein_rule_16_component`, sympy `T3C.krein_rule_16_component`); the filling convention of the $+m$ member is carried onto the $-m$ member (`T3C_filling_convention_mapped`). Two numerical demonstrations on the background history, with the Rust solver and with the independent reference solver, are demonstrations, not proofs.

These are correspondences between solutions; no creation process, rate or amplitude follows from them (`not_established` in the sympy pairing report, in the T3 record and in the completion record).

## 15. What this document does not claim

- It derives no creation process, rate or amplitude for universes, and no statement that universes of masses $+m$ and $-m$ are created in pairs; the pairing theorems (section 14) map solutions to solutions.
- Non-triviality [1] is a statement about the Euler-Lagrange equations in the corrected metric with $H > 0$; it is not a statement about observable effects of the gravitational term. The value $\gamma^\mu\Omega_\mu = c_g\gamma^{(0)} + v_g\gamma^{(4)}$ belongs to the diagonal vielbein and to the field variables $\Psi$: its $c_g$ part vanishes identically in the frame boosted in the $(x_0, x_4)$ plane with rapidity rate $2c_g$ (no boost in this plane removes its $v_g$ part), and the rescaling $\Psi = e^{a_4/2}b_4^{-1}(\sin^2 z)^{-1/8}\chi$ removes all of it; the canonical connection drops out of $\mathcal{L}$. What is frame-independent is that $\Omega_\mu$ vanishes in no frame wherever the metric is curved, together with the vielbein factors of the derivative terms (section 7, Remarks); on the flat member the term is a pure frame effect. That the term is "not cosmetic" is not claimed; its role for the Hermiticity of the mode operator depends on the measure and the variables (an interpretation).
- The quantisation recorded here is: the canonical anticommutator, the theorem that it forces a Krein structure when $\Psi^\dagger$ is realised as the Hilbert adjoint, the formal Krein self-adjointness of the evolution (up to the boundary term at the degenerate points), and positive Fock realisations checked for single good-sector momenta with frozen coefficients. A positive-norm Hilbert space for the full field, a stable vacuum in the presence of the growing extra-time modes, and the interacting ($\lambda \neq 0$) operator theory beyond the finite model of section 12 are not constructed. In flat 4+4 space every eigenspace of REAL frequency of the one-particle generator has Krein inertia (4,4) (`Q_one_particle_Krein_signatures`, `Q.one_particle_Krein_inertia`, proved for every real frequency in `Q_one_particle_Krein_inertia_real_frequencies` and `Q.one_particle_Krein_inertia_proof`), and every eigenspace of imaginary or zero frequency is Krein-neutral (`Q_one_particle_complex_and_zero_frequencies_Krein_neutral`). In flat space the good-sector restriction removes the complex frequencies, not the indefiniteness of the real-frequency eigenspaces; in the curved good sector without a boundary condition at the degenerate points complex frequencies remain (section 11).
- Boundary conditions: none is imposed at the degenerate points in this record. The Hermiticity of the curved good-sector mode operator and the conservation of the Krein form hold up to the boundary term there; with no boundary condition the good sector contains growing $x_0$-independent modes wherever $m^2 < c_g^2$.
- No well-posed Cauchy problem is claimed: the slices $x_4 = $ const are non-characteristic, but for data that depend on the extra times the growth rates are unbounded (not well posed in Hadamard's sense).
- The normal-ordered operator form of the on-shell trace identity for $\lambda \neq 0$ is an assumption of the field-equations record. It is verified only in the finite model of section 12 (one good-sector plane-wave mode set with frozen coefficients, record `Revision/theory/fock_quartic/`), where it holds as an exact operator identity if and only if the potential and the energy-momentum tensor are both Wick ordered and fails for every other tested ordering already in expectation values; for the field on a whole slice, the curved $x_0$ dependence and the extra-time sector it is not verified, and symmetry and conservation of the quartic operator are not verified. No numerical expectation value of the energy-momentum tensor operator for a physical many-fermion state is computed in this document (the finite model gives only its exact values on the occupation states of one mode set); the Kohn-Sham quantities it quotes, in section 13 and in this section (the equation-of-state values $w_{\rm eff}$ of the Kohn-Sham gas from the dark-sector record, below), are computed from Kohn-Sham expectation values.
- The relative sign $\sigma_T$ between the gravitational and the matter side of the field equations is a declared convention ($\sigma_T = +1$), not derived.
- No solution $a_4(x_4)$, $b_4(x_4)$ with a dirac16complex source is computed here beyond the statements of section 13; it is not claimed that any state of dirac16complex supplies a source that satisfies all the conditions of section 13 (no off-diagonal component, $p_0 = p_t$, diagonal components independent of $x_0$). The recorded Kohn-Sham states fail the conditions (section 13), and the background history $a_4 = Hx_4$, $b_4 = b_4(0)e^{(4/3)Hx_4}$ is a prescribed test-field background without back-reaction; the equations do not select deflation over inflation.
- The equation of state seen by a 3-space observer and its time dependence are not derived in this document. Hypothesis (dirac16complex provides a possible physical mechanism for a time-varying dark-energy and/or dark-matter equation of state; SPEC section 8) is investigated, not assumed, in the dark-sector record `Revision/dark_sector/dirac16complex/` (document `Revision/docs/DARK_SECTOR_HYPOTHESES`), on the PRESCRIBED background history $a_4 = Hx_4$, $b_4 = e^{(4/3)Hx_4}$ of the corrected metric. The 4-dimensional density $\rho_4$ of the observer is an ASSUMPTION, with three definitions: (A) the hidden direction and the extra times are compact with a fixed coordinate period; (B) $\rho_4$ is taken per unit of their coordinate volume; (C) $\rho_4$ is taken per unit proper 7-volume. With $w_{\rm eff} = -1 - \tfrac13\,d\ln\rho_4/d\ln a$ and the 3-space scale factor $a = e^{a_4}$, on this history $w_{\rm eff}(B) = w_{\rm eff}(A)$ and $w_{\rm eff}(C) = w_{\rm eff}(A) - 4/9$ (`w_eff_A`, `w_eff_B_equals_w_eff_A`, `w_eff_C`). The verdict of that record for dirac16complex (an INTERPRETATION of the computed numbers): no time-varying dark-matter-like equation of state ($w_{\rm eff}(A)$ falling from 1/3 toward 0) is found. The computed free Kohn-Sham gas ($\lambda = 0$) is an exact fold-band gas: for $N = 592$ and 2352 every occupied orbital is a fold-band orbital, and $w_{\rm eff}(A) = 1/3$ exactly (radiation-like), $w_{\rm eff}(C) = -1/9$, $w_a = 0$ (`free_gas_exact_fold_band`, `lambda0_series_exact_fold_band`, `fold_band_quantum_w_eff`; independently `free_gas_w_eff_one_third`); the interacting gas ($N = 592$ and 2352, $\lambda \neq 0$, 8 series), whose orbitals the interaction bends (section 13), has $w_{\rm eff}(A)$ between 0.330585 and 0.336132 (`interacting_gas_ranges`). The massive bulk band, which the computed $T = 0$ states do not populate, does not follow the dust-like law $1/3 \to 0$ either: the shrinking hidden direction blue-shifts its level like $e^{a_4}b_4^{-1/2} = e^{a_4/3}$, and its $w_{\rm eff}(A)$ falls monotonically from 0.318721 ($a_4 = -3$) to $-0.081074$ ($a_4 = 4$), changing sign between $a_4 = -0.5$ and $-0.25$ (`bulk_band_w_eff`; a single-level study by the independent collocation over $a_4 \in [-3, 4]$, beyond the range $a_4 \in [0, 2]$ in which the Kohn-Sham states are used).
- Nor is a dark-energy-like equation of state found. The Kohn-Sham gas is not dark-energy-like under any of the three definitions: $w_{\rm eff}(C) = -1/9$ (free) or between $-0.113860$ and $-0.108312$ (interacting), and $w_{\rm eff}(A)$ is near 1/3; in the CPL form $w = w_0 + w_a(1 - a)$ its tangent $w_a$ lies between $-0.003892$ and 0.003904 and its fitted $w_a$ between $-0.002392$ and 0.002261, far from the Unite pair $(w_0, w_a) = (-0.861, -0.60)$ quoted in that record (`gas_cpl_far_from_unite`); no computed Kohn-Sham state has $w_{\rm eff}(C) < -1$ (the condition for it is derived in `phantom_condition`); a drifting condensate with $\lambda < 0$ has $w_{\rm eff}(C) < -1$ while $\lambda S/m$ lies in $(-2, -1)$ (`Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json`, `condensate_phantom_interval`). Only the drifting condensate (the exact homogeneous solution, with $\lambda S/m \propto e^{-(5/3)a_4}$) gives values near the Unite $w_0$: at the condensate ratio $p/\rho = -0.764$ today (the Unite constant-$w$ value) it has $w_{\rm eff}(C) = -0.868889$ with $w_a = -1.247867$ (`condensate_drifts`), and the point closest to the Unite pair under (C), $(-0.7056, -0.6397)$ at the distance 0.1604, is a CHOSEN pure condensate (`Revision/dark_sector/dirac16complex/outputs/eos-summary.json`): a tuned value, NOT a prediction. The free gas $N = 2352$ mixed with a $\lambda = 0$ condensate stays at $w_{\rm eff}(C) \geq -0.444111$ (`mixture_C_cannot_reach_unite_w0_with_lambda0_condensate`). On this history the observer's expansion itself reads $w_{\rm exp} = -1$ exactly, for every $b_4$ (`expansion_inferred_w`). OPEN in that record: a self-consistent history with an admissible source (section 13), populated bulk-band or thermal states along the history, modes with extra-time momentum and the non-adiabatic problem. This document claims no dark-matter or dark-energy mechanism of dirac16complex, and none of the companion field dirac16complex00 (Hypothesis00 is the same question for that field; `Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY`). That record establishes neither Hypothesis nor Hypothesis00.
- $H = 0$ is a degenerate limit, not a member of the family; the points $z = n\pi/2$ are degenerate ($g_{00} = 0$, $\sqrt{|g|} = 0$ at the folds); nothing is claimed there.
- The metric of 2026-10-14 (with the factors $\sin^{1/3}z$ and $g_{00} = \cot^2 z$) and the version 1 of 2026-10-16 are withdrawn; no statement of this document is restricted to them, and their formulas are not results of this record.
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

The Wolfram field-theory verifier runs in six parts and a merge; on 2026-10-16 they took 14 s (base), 57 s (emt-C), 179 s (emt-G), 36 s (solutions), 17 s (solutions-G) and 5 s (quantisation), the scope verifier 2 s, and the sympy checker 32 s for its part `--part nonlinear` (the nonlinear homogeneous solutions, written to a git-ignored part file that the full run reads only if its inputs are unchanged) and 148 s to 161 s for the full run (`Revision/theory/wolfram/WOLFRAMSCRIPT_PROVENANCE.md`, section 6.10). The analysis of the $a_4$ and $b_4$ equations with the Kohn-Sham source re-derives the source-conditions report, so it runs after that checker; the checker of the finite Fock model for $\lambda \neq 0$ (it reads only `Revision/algebra/gammas.json`) ran in 6.7 s by its README. The sympy completion checker reads the reports of the two numerical demonstrations, so it runs after them, in the order given in section 10 of `Revision/docs/PAIR_CREATION_PROOFS`; the programs of the dark-sector record are listed in `Revision/docs/DARK_SECTOR_HYPOTHESES`.

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

The test checks that the .tex is the builder output of the .md, that the registered PDF is the PDF file next to it, that every cited check exists and passes in the reports, that the quoted check counts are those of the reports, that the component field equations and the Lovelock, Einstein and history-source formulas of section 13 are the output of its renderers applied to `Revision/theory/field-theory.json` and `Revision/field_equations_a4/a4-equations.json` (and that their sums over $k$ equal the general formulas there), and that the hand-written formulas of sections 2 and 4 equal the formula file.

## 17. Index of formulas and checks

| formula | section | Wolfram checks | sympy checks |
| --- | --- | --- | --- |
| the corrected metric, vielbein, volume element | 2 | `metric_is_the_corrected_metric`, `sqrt_det_g` | `metric_from_vielbein_equals_SPEC`, `sqrt_det_g` |
| Christoffel symbols, Ricci tensor (diagonal), curvature, the flat member | 2 | `christoffel_count`, `ricci_mixed_components`, `ricci_scalar`, `flat_member_and_curvature` | `christoffel_symmetric_metric_compatible`, `curvature_and_flat_member` |
| Clifford algebra, C, Gamma, B | 3 | `Clifford_relation`, `C_gamma_real_antisymmetric`, `Gamma_diag`, `B_signature_8_8` | `clifford_relation`, `C_conjugation`, `chirality_diag`, `B_hermitian_involution_signature` |
| Pin(4,4) irreducible; Spin(4,4): two inequivalent 8-dimensional irreducible halves | 3 | `Pin44_irreducible_commutant_dim_1`, `chiral_halves_irreducible`, `chiral_halves_inequivalent_intertwiners_0` | `pin_commutant_dimension_1`, `spin_halves_irreducible`, `spin_halves_inequivalent` |
| canonical spin connection, covariant constancy | 4 | `vielbein_postulate`, `omega_components`, `Omega_components`, `gamma_covariantly_constant` | `vielbein_postulate`, `Omega_x4_vanishes_Omega_x0_does_not`, `covariant_constancy_D_mu_gamma_nu`, `spinor_connection_real` |
| gravitational term $c_g\gamma^{(0)} + v_g\gamma^{(4)}$ (diagonal frame) and its square | 4, 7 | `gammaOmega_total`, `gammaOmega_per_direction`, `gammaOmega_divergence_form` | `gamma_mu_Omega_mu_equals_hidden_block_terms`, `per_direction_terms`, `gravity_term_square` |
| frame and variable dependence of the term; frame-independent content | 4, 7 | `boosted_frame_gammaOmega_formula`, `boosted_frame_removes_only_the_H_term`, `boosted_frame_curvature_nonzero`, `rescaling_removes_the_connection_term`, `connection_free_lagrangian_same_equations` | `boosted_frame_gammaOmega_formula`, `boosted_frame_removes_only_the_H_term`, `rescaled_equation_quadratic_potential`, `gammaOmega_sees_the_hidden_block`, `spin_connection_in_the_energy_momentum_tensor` |
| Lagrangian: reality, total divergence | 5 | `L_real_G`, `L_total_divergence_to_unsymmetrised_G` | `grassmann_lagrangian_real`, `grassmann_total_divergence_relation` |
| Majorana-type negative control | 5 | `Majorana_Lg_total_derivative_grassmann` | `negative_control_majorana_grassmann_total_derivative` |
| Euler-Lagrange equations, explicit form | 6 | `EL_Psibar_G`, `EL_Psi_G`, `Dirac_operator_explicit_G`, `evolution_form_G`, `block_form` | `grassmann_euler_lagrange_psibar_variation`, `grassmann_euler_lagrange_psi_variation` |
| non-triviality [1] | 7 | `nontriviality_1_dirac16complex`, `Omega_vanishes_iff_a4prime_b4prime_and_H_vanish`, `spin_curvature_equals_Riemann` | `nontriviality_Omega_zero_iff_flat`, `spinor_curvature_equals_riemann`, `gravity_term_square` |
| self-consistency | 8 | `adjoint_equation_is_Dirac_conjugate_G`, `Lichnerowicz_identity_G`, `current_conservation_identity_G`, `Noether_identity_diffeomorphisms_G`, `Noether_identity_local_Lorentz_G` | `grassmann_adjoint_equation_is_conjugate`, `lichnerowicz_identity_on_fields`, `grassmann_current_conservation`, `grassmann_emt_conservation_on_shell` |
| exact solutions with the factor $e^{a_4/2}b_4^{-1}$ | 8, 10 | `exact_solution_x4_x0_m0_G`, `exact_solution_x4_x0_quarter_G`, `exact_solution_nonlinear_homogeneous_G` | `exact_solution_family_x4_x0`, `exact_nonlinear_homogeneous_solution` |
| energy-momentum tensor | 9 | `T_vielbein_variation_closed_form_G`, `T_symmetric_part_Belinfante_G`, `T_diagonal_components_G`, `T_x4_x0_component_G`, `EMT_trace_G` | `grassmann_emt_equals_general_vielbein_variation_on_shell`, `grassmann_emt_symmetric`, `grassmann_trace_on_shell` |
| energy density, pressures, equations of state, energy exchange with the rate $h_4$ | 9, 10 | `kinetic_sum_on_shell_G`, `exact_solution_nonlinear_homogeneous_G`, `energy_exchange_equation` | `grassmann_homogeneous_on_shell_rho_p`, `energy_exchange_equation` |
| canonical quantisation, Krein structure | 11 | `canonical_momentum`, `first_order_form_and_anticommutator`, `no_positive_inner_product`, `Krein_form_conserved_curved`, `good_sector_hermiticity_curved`, `Q_one_particle_Krein_inertia_real_frequencies` | `canonical_anticommutator_B`, `no_positive_inner_product`, `good_sector_spectrum_and_B_sectors`, `Q.one_particle_Krein_inertia_proof`, `Q.one_particle_complex_frequency_Krein_neutral` |
| boundary term at the degenerate points, growing modes, ill-posedness | 8, 11 | `good_sector_hermiticity_up_to_the_brane_flux`, `good_sector_x0_independent_modes_without_boundary_condition` | `extra_time_growth_rates_unbounded` |
| Fock space, normal ordering, expectation values | 11, 12 | `Fock_space_good_sector_example`, `mode_hamiltonian_Krein_selfadjoint` | `good_sector_positive_fock_realisation`, `expectation_value_rule`, `extra_time_modes_grow` |
| energy-momentum tensor operator for $\lambda \neq 0$ in a finite Fock model | 12 | | `trace_identity_operator_identity_wick`, `trace_identity_fails_for_every_other_combination`, `homogeneous_rho_p_operator_identities_wick`, `negative_control_free_dynamics` (Python) |
| field equations for $a_4$ and $b_4$ | 13 | `lovelock_variables`, `independent_components`, `second_order_system_a4pp_vv`, `constraint_propagation_bianchi`, `conservation_components` | `second_order_system`, `bianchi_x4`, `json_lovelock_components`, `json_general_source_equations` |
| Einstein gravity | 13 | `einstein_components`, `einstein_null_combinations`, `einstein_flat_vacuum`, `einstein_no_exponential_vacuum` | `einstein_components`, `einstein_null_combinations`, `einstein_flat_vacuum`, `einstein_no_exponential_vacuum` |
| exponential histories, the author's weights, the background history | 13 | `exponential_history_required_source`, `author_weights_history_source`, `author_weights_no_exponential_vacuum`, `egb_exponential_vacuum_branches` | `exponential_history_required_source`, `author_weights_history_source`, `author_weights_no_exponential_vacuum`, `egb_exponential_vacuum_branches` |
| sources of the homogeneous form | 13 | `condensate_kinetic_tensor_diagonal`, `condensate_S_law`, `condensate_source_equal_pressures` | `authorT16_condensate_kinetic_diagonal`, `condensate_source_equal_pressures` |
| the Kohn-Sham states as a source (conditions C1 to C4) | 13 | | `ks_profiles_depend_on_x0`, `ks_hidden_pressure_condition`, `ks_offdiagonal_condition`, `ks_history_is_a_prescribed_background`, `ks_zero_source_states_listed` (Python) |
| the $a_4$ and $b_4$ equations with the Kohn-Sham source | 13 | | `A1_hidden_equals_extra_times_and_no_offdiagonal`, `A4_x0_conservation_in_y`, `A5_free_fold_band_gas_conserves_energy`, `B2_x0_conservation_on_every_profile`, `B3_hidden_direction_mismatch`, `C1_averaged_hidden_pressure_condition`, `C3_record_history_not_sourced_by_the_gas`, `D0_free_gas_average_exact`, `D2_author_weights_from_the_record_history`, `D4_outcomes` (Python) |
| completion of T3 (S6, filling convention) | 14 | `T3C_krein_rule_16_component`, `T3C_filling_convention_mapped` | `T3C.krein_rule_16_component`, `T3C.filling_convention_mapped` |
| pairing (section 14) | 14 | `T1_Lagrangian_primordial_grassmann`, `T2_mirror_Lagrangian_grassmann`, `Q_Krein_metric_of_images`, `T3_energies_and_emt_profiles_equal` | `T1.metric.grassmann.lagrangian`, `T2.metric.grassmann.emt`, `Q.no_cancellation_independent_universes`, `T3.energies_and_emt_profiles_equal` |
| dark-sector verdict for dirac16complex (observer definitions, fold-band gas, bulk band, condensate) | 15 | | `w_eff_A`, `w_eff_B_equals_w_eff_A`, `w_eff_C`, `free_gas_exact_fold_band`, `lambda0_series_exact_fold_band`, `interacting_gas_ranges`, `bulk_band_w_eff`, `gas_cpl_far_from_unite`, `phantom_condition`, `condensate_phantom_interval`, `condensate_drifts`, `mixture_C_cannot_reach_unite_w0_with_lambda0_condensate`, `expansion_inferred_w` (Python) |
