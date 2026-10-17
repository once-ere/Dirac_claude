# Pairing of universes of masses +m and -m: exact proofs for dirac16complex and dirac16complex00

## The pairing theorems T1, T2 and T3 and the quantum-level reading in the author's primordial gravitational field, with every hypothesis, the verification records and an exact statement of what they do not establish

## Abstract

The author asked on 2026-10-01: “PROVE that Universes of masses {+mass, -mass} are created in pairs for each case of the dirac16complex and the dirac16complex00 fields.” This document gives the exact answer computed by the code in `Revision/` for the corrected primordial metric of 2026-10-16 (version 2; `Revision/SPEC.md` section 1). Proved, for both fields and with every hypothesis stated: T1 (chirality pairing): the chirality matrix $\Gamma$ maps every configuration $\Psi$ of the theory with mass and coupling $(m,\lambda)$ to the configuration $\Gamma\Psi$ of the theory with $(-m,-\lambda)$, with $\mathcal{L}_{m,\lambda}[\Gamma\Psi] = -\mathcal{L}_{-m,-\lambda}[\Psi]$, solutions to solutions and the energy-momentum tensor and the current reversed, so that the pair has zero total energy-momentum, current and charge as classical bilinears, in every gravitational field. T2 (mirror pairing): $\Gamma$ combined with a Pin(4,4) reflection of character $-1$ maps $(m,\lambda)$ to $(-m,\lambda)$ with $\mathcal{L} \to +\mathcal{L}$; in the corrected metric it is realised by the isometry $z \to \pi - z$ across the fold $z = \pi/2$ between the two halves of a cell (the corrected metric has no Z2 orbifold, and no matching of the field across the fold is derived), and the partner has EQUAL, not opposite, energy-momentum. T3 (Kohn-Sham level, dirac16complex): the block map of $\Gamma$, with the two fold conditions exchanged and the tip angle $\theta \to \pi - \theta$, maps every self-consistent instantaneous Kohn-Sham state with $(m,\lambda,\theta)$ onto one with $(-m,+\lambda,\pi-\theta)$, with equal levels, occupations, Kohn-Sham energies and energy-momentum profiles (both fold conditions filled, ASSUMED; mean-field level); a completion adds the 16-component statement S6 (every component of the energy-momentum tensor and of the current is unchanged, $S$ and $Q$ change sign), carries the filling convention onto the $-m$ member and demonstrates T3 numerically with two independent Kohn-Sham solvers (demonstrations, not part of the proof). The quantum-level reading for dirac16complex: the chirality image carries the Krein metric $-B$ and is the same quantum system re-labelled; two independently quantised universes of masses $+m$ and $-m$ have identical one-particle ($\lambda = 0$) spectra (flat space, or frozen coefficients at a point) and their generators do not cancel. A corollary: a T1 pair taken as the complete classical source of the metric is a zero source; then $a_4$ and $b_4$ must solve the vacuum equations, and no exponential history, in particular not the background history of `Revision/SPEC.md` section 1, is a vacuum solution in Einstein gravity or with the author's Lovelock weights. Not established by any of these equations: a creation process, a rate, a probability or an amplitude for creating universes, in pairs or otherwise. T1, T2, T3 and the quantum reading Q are proved, each under its stated hypotheses; the creation of pairs is not.

## 1. The request and the exact answer

The author's request, quoted from `Revision/README.md`: “PROVE that Universes of masses {+mass, -mass} are created in pairs for each case of the dirac16complex and the dirac16complex00 fields.”

What a universe of mass $m$ means in this record: a configuration of one of the two fields with mass parameter $m$ and coupling $\lambda$ in the author's primordial gravitational field, i.e. a solution of the Euler-Lagrange equations of section 2.4. Two such universes are paired when an explicit invertible map takes every solution of the theory with mass $m$ to a solution of the theory with mass $-m$ and takes its Lagrangian, energy-momentum tensor and current to stated multiples of those of the partner.

The exact answer, for both fields:

1. Proved (sections 4 to 8): the pairing theorems T1 and T2, the quantum-level reading Q for dirac16complex, the corollary C1 for the field equations of $a_4$ and $b_4$ and the Kohn-Sham-level theorem T3 for dirac16complex, each with its exact hypotheses (T2 uses the isometry across the fold; T3 fills both fold conditions, ASSUMED).
2. Not proved, and not derivable from these equations: that such universes are CREATED. The equations are field equations on a fixed gravitational background and their canonical quantisation; no equation of this record produces a pair of universes from anything, and no creation process, rate or amplitude follows from them (section 11).
3. The Kohn-Sham level T3 of `Revision/SPEC.md` section 9 is proved in section 8 for the instantaneous (adiabatic) mean-field Kohn-Sham states of `Revision/kohn_sham/ks-theory.json`; the time-dependent Kohn-Sham problem is open. Its completion (section 8.5) closes the gaps found by an adversarial verification and adds two numerical demonstrations.

Every formula and number below is taken from the Revision reports listed in section 9; nothing is taken from the earlier stages of the repository. Interpretations are labelled as such.

Related Revision documents. The Kohn-Sham model of dirac16complex in the deflating field, whose states T3 maps, is described in `Revision/docs/KOHN_SHAM_DEFLATING_FIELD` (block reduction, instantaneous ground and first excited states along the prescribed history $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$, Mermin thermodynamics, the full cross-check of the Rust solver against the independent reference). The Lovelock tensors behind the field equations for $a_4$ and $b_4$ used by corollary C1 are described in `Revision/docs/LOVELOCK_GKD`. The field equations for $a_4$ and $b_4$ with the Kohn-Sham source (`Revision/field_equations_a4/ks_source`) show that no recorded Kohn-Sham state is an admissible source of the metric (section 8.4), so T3 is a statement about test-field states on a prescribed background. The dark-sector hypotheses for both fields are investigated in `Revision/docs/DARK_SECTOR_HYPOTHESES`; that record establishes neither Hypothesis nor Hypothesis00 (it states what each field can and cannot produce under its stated observer assumption), and nothing in it is used by, or changes, the theorems of this document.

## 2. Setting and conventions

### 2.1 The corrected metric and the coordinates

The coordinates are the author's, $x_0, x_1, \dots, x_7$, in the author's order: $x_0$ is the hidden direction, space-like, with $z = 6Hx_0$ real and $H > 0$ the author's constant; $x_1, x_2, x_3$ are ordinary 3-space (inflating); $x_4$ is the time; and $x_5, x_6, x_7$ are the three extra times, which DEFLATE exponentially as $a_4$ increases. The metric of `Revision/SPEC.md` section 1 (version 2 of 2026-10-16; `Revision/metric_warped/`) is

$$
\begin{aligned}
ds^2 = {} & e^{-2a_4(x_4)}b_4(x_4)\cot^2 z\,dx_0^2 + e^{2a_4(x_4)}\big(dx_1^2+dx_2^2+dx_3^2\big) - dx_4^2 \\
& - e^{-2a_4(x_4)}\,b_4(x_4)(\sin^2 z)^{1/6}\,\big(dx_5^2+dx_6^2+dx_7^2\big) ,
\end{aligned}
$$

with two metric functions $a_4(x_4)$ and $b_4(x_4) > 0$ of the time ($b_4$ is never 1); the hidden direction and the extra times form one block, which deflates with the scale factor $e^{-a_4}b_4^{1/2}$ times the $x_0$-dependent factors $|\cot z|$ and $(\sin^2 z)^{1/12}$. T1, T2, Q and T3 hold for arbitrary functions $a_4(x_4)$ and $b_4(x_4)$ (the pairing verifiers treat both as arbitrary); the Kohn-Sham record of section 8 uses the PRESCRIBED history $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$ with $A = 1$ and $b_4(0) = 1$ (`Revision/SPEC.md` section 1; `Revision/kohn_sham/ks-theory.json`, key adiabaticity), that is $a_4 = Hx_4$, $b_4 = e^{(4/3)Hx_4}$, on which the scale factor of the block is $b_4(0)^{1/2}e^{-a_4/3} = e^{-a_4/3}$: the extra times deflate exponentially. The metric has signature (4,4) (space-like $x_0, x_1, x_2, x_3$; time-like $x_4, x_5, x_6, x_7$), with $\sqrt{|g|} = e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}$; it is degenerate at $z = n\pi/2$, and the points $z = \pi/2 + n\pi$, where $g_{00} = 0$ and $\sqrt{|g|} = 0$, are the folds where the two halves of a cell meet. The pairing verifiers work on the patch $0 < z < \pi/2$ (where $(\sin^2 z)^{1/12} = \sin^{1/6}z$) and on the other half $\pi/2 < z < \pi$ of the cell. The diagonal vielbein is $e^a{}_\mu = f_a\delta^a_\mu$ with $f_0 = e^{-a_4}b_4^{1/2}\cot z$, $f_1 = f_2 = f_3 = e^{a_4}$, $f_4 = 1$ and $f_5 = f_6 = f_7 = e^{-a_4}b_4^{1/2}(\sin^2 z)^{1/12}$; the frame metric is $\eta = \mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1)$ in the order $x_0, \dots, x_7$. Frame indices $a = 0, \dots, 7$ are aligned with the coordinates, so $\gamma^0$ is the hidden-direction gamma $\gamma^{(x_0)}$ and $\gamma^4$ the time gamma $\gamma^{(x_4)}$.

The canonical spin connection (vielbein postulate) has the 10 nonzero components $\omega_{x_0,\,04} = h_4e^{-a_4}b_4^{1/2}\cot z$, $\omega_{x_i,\,i4} = a_4'e^{a_4}$ for the 3-space directions $i = 1, 2, 3$, and $\omega_{x_t,\,4t} = h_4e^{-a_4}b_4^{1/2}(\sin^2 z)^{1/12}$ and $\omega_{x_t,\,0t} = H(\sin^2 z)^{1/12}$ for the extra times $t = 5, 6, 7$, with $h_4 = \frac{b_4'}{2b_4} - a_4'$ the rate of the block and $\Omega_{x_4} = 0$. Contracted with the gammas,

$$
\gamma^\mu\Omega_\mu = c_g\,\gamma^0 + v_g\,\gamma^4,\qquad c_g = \tfrac32He^{a_4}b_4^{-1/2},\qquad v_g = \frac{b_4'}{b_4} - \frac{a_4'}{2} :
$$

the hidden direction contributes $\frac{h_4}{2}\gamma^4$, each 3-space direction $\frac{a_4'}{2}\gamma^4$ and each extra time $\frac{h_4}{2}\gamma^4 + \frac{H}{2}e^{a_4}b_4^{-1/2}\gamma^0$.

### 2.2 Clifford data

The gammas are the author's real $16 \times 16$ matrices T16, re-constructed in Revision code from the author's tau formulas, with $\gamma^a = T16[a]$ for $a = 0, \dots, 7$ ($\gamma^0$ the hidden direction, $\gamma^4$ the time). They are real signed permutation matrices with $\{\gamma^a,\gamma^b\} = 2\eta^{ab}$ and $(\gamma^a)^T = \eta_{aa}\gamma^a$. Further:

- $C = \gamma^0\gamma^1\gamma^2\gamma^3$ is real and symmetric, $C^2 = 1$, $C\gamma^a$ is real and antisymmetric and $C\gamma^aC^{-1} = -(\gamma^a)^T$; the Dirac adjoint is $\bar\Psi = \Psi^\dagger C$.
- $\Gamma = \gamma^0\gamma^1\gamma^2\gamma^3\gamma^4\gamma^5\gamma^6\gamma^7 = \mathrm{diag}(-I_8, I_8)$.
- $B = -iC\gamma^4$ is Hermitian with $B^2 = 1$ and signature (8,8).
- $S^{ab} = \frac14[\gamma^a,\gamma^b]$ satisfy the commutation relations of so(4,4).
- The 16-dimensional representation is irreducible under Pin(4,4) (commutant of dimension 1) and splits under Spin(4,4) into two inequivalent irreducible 8-dimensional representations, the chiral halves $\Gamma = -1$ (components 1 to 8, written $\psi_-$) and $\Gamma = +1$ (components 9 to 16, written $\psi_+$); every $\gamma^a$ exchanges the two halves.

### 2.3 The two fields and the Lagrangian

dirac16complex is $\Psi$: 16 complex ANTICOMMUTING (Grassmann) components, a Pin(4,4) spinor, quantised canonically (section 6). dirac16complex00 is $\Phi$: 16 complex COMMUTING components that transform as a Pin(4,4) spinor, a classical field. Both are coupled to gravity through the vielbein and the canonical spin connection. The theorems are stated with the letter $\Psi$ for both fields; “both statistics” means that the statement and its proof hold for Grassmann components and for commuting components. With $S = \bar\Psi\Psi$, $D_\mu\Psi = \partial_\mu\Psi + \Omega_\mu\Psi$, $D_\mu\bar\Psi = \partial_\mu\bar\Psi - \bar\Psi\Omega_\mu$, $\Omega_\mu = \frac12\omega_{\mu ab}S^{ab}$ and $\gamma^\mu = e^\mu{}_a\gamma^a$, the Lagrangian density of both fields is

$$
\mathcal{L}_{m,U}[\Psi] = \sqrt{|g|}\,\big[K[\Psi] - mS - U(S)\big],\qquad
K[\Psi] = \tfrac12\big(\bar\Psi\gamma^\mu D_\mu\Psi - (D_\mu\bar\Psi)\gamma^\mu\Psi\big),
$$

written $\mathcal{L}_{m,\lambda}$ for $U(S) = \frac{\lambda}{2}S^2$. It is real for both statistics.

### 2.4 Field equation, energy-momentum tensor, current

The Euler-Lagrange equations of $\mathcal{L}_{m,U}$ are, for both statistics,

$$
E_{m,U}[\Psi] \equiv \gamma^\mu D_\mu\Psi - \big(m + U'(S)\big)\Psi = 0,\qquad
(D_\mu\bar\Psi)\gamma^\mu = -\big(m + U'(S)\big)\bar\Psi .
$$

The symmetric (Belinfante) energy-momentum tensor of the theory record is

$$
T^\nu{}_\mu = \delta^\nu_\mu\,\frac{\mathcal{L}}{\sqrt{|g|}} - \frac14\Big(\bar\Psi\gamma^\nu D_\mu\Psi - (D_\mu\bar\Psi)\gamma^\nu\Psi + \bar\Psi\gamma_\mu D^\nu\Psi - (D^\nu\bar\Psi)\gamma_\mu\Psi\Big),
$$

with the energy density $\rho = -T^{x_4}{}_{x_4}$ and the pressures $p_\mu = T^\mu{}_\mu$ (no sum) of `Revision/SPEC.md` section 4; for homogeneous on-shell states $\rho = mS + U$ and $p = SU' - U$. The conserved current is $J^\mu = -i\bar\Psi\gamma^\mu\Psi$, with the charge density $J^{x_4} = \Psi^\dagger B\Psi$ and the charge $Q = \int\sqrt{|g|}\,\Psi^\dagger B\Psi\,d^7x$.

Convention note. The pairing records use the tensor

$$
T_{\mu\nu} = \tfrac14\big(\bar\Psi\gamma_\mu D_\nu\Psi + \bar\Psi\gamma_\nu D_\mu\Psi - (D_\mu\bar\Psi)\gamma_\nu\Psi - (D_\nu\bar\Psi)\gamma_\mu\Psi\big) - g_{\mu\nu}\,\mathcal{L}/\sqrt{|g|},
$$

which is minus the tensor above, and the currents $\bar\Psi\gamma^\mu\Psi$ (Wolfram) and $i\bar\Psi\gamma^\mu\Psi$ (sympy). Every statement of T1, T2 and Q about $T$ and $J$ is linear and homogeneous in them ($T' = \pm T$, $J' = \pm J$), so it holds unchanged for every overall sign and constant factor.

### 2.5 The field equation in the corrected metric

Written out in the corrected metric, the field equation of both fields is

$$
\begin{aligned}
& e^{a_4}b_4^{-1/2}\tan z\,\gamma^0\partial_0\Psi + e^{-a_4}\big(\gamma^1\partial_1+\gamma^2\partial_2+\gamma^3\partial_3\big)\Psi + \gamma^4\partial_4\Psi
+ e^{a_4}b_4^{-1/2}(\sin^2 z)^{-1/12}\big(\gamma^5\partial_5+\gamma^6\partial_6+\gamma^7\partial_7\big)\Psi \\
& \qquad + c_g\gamma^0\Psi + v_g\gamma^4\Psi = \big(m + U'(S)\big)\Psi ,
\end{aligned}
$$

where $G = c_g\gamma^0 + v_g\gamma^4 = \gamma^\mu\Omega_\mu$ is the spin-connection term in the diagonal vielbein of section 2.1 and in the field variables $\Psi$; in this frame and these variables it is nonzero for every $H > 0$ (its $\gamma^0$ coefficient $c_g$ is positive), and $G^2 = (c_g^2 - v_g^2)I_{16}$, so $G\Psi \neq 0$ for every $\Psi \neq 0$ wherever $c_g^2 \neq v_g^2$ (on the history of section 2.1 with $A = 1$, $b_4(0) = 1$: $c_g = \frac32He^{Hx_4/3}$, $v_g = \frac56H$ and $G^2 = H^2(\frac94e^{2Hx_4/3} - \frac{25}{36})I_{16}$, which is positive for $x_4 \geq 0$, where $\frac94e^{2Hx_4/3} \geq \frac94 > \frac{25}{36}$, in particular at the slices $a_{4,0} = 0$ to $2$ of section 8, and vanishes where $e^{2Hx_4/3} = \frac{25}{81}$, at a negative $x_4$; `nontriviality_1_dirac16complex`, `nontriviality_2_dirac16complex00`). This is non-triviality [1] and [2] of the theory record only in the qualified sense stated there: the value belongs to the frame and the variables. In a frame boosted in the $(x_0, x_4)$ plane whose rapidity has the rate $2c_g$ the $c_g$ part is removed and $v_g(\cosh b\,\gamma^4 - \sinh b\,\gamma^0)$ remains; no boost in this plane removes the $v_g$ part (`boosted_frame_gammaOmega_formula`, `boosted_frame_removes_only_the_H_term`); the rescaling $\Psi = e^{a_4/2}b_4^{-1}(\sin^2 z)^{-1/8}\chi$ removes the whole term (completely for $U = 0$; for $U \neq 0$ it becomes the $x_0$- and $x_4$-dependent coupling $\lambda e^{a_4}S[\chi]/(b_4^2|\sin z|^{1/2})$: `rescaling_removes_the_connection_term`, `rescaled_equation_quadratic_potential`); and the canonical spin connection drops out of $\mathcal{L}$ (`connection_free_lagrangian_same_equations`). What is frame-independent is that $\Omega_\mu$ vanishes in no frame wherever the metric is curved, because its curvature is the Riemann tensor (`boosted_frame_curvature_nonzero`, `spin_curvature_equals_Riemann`): the corrected metric is curved on the background history and flat for the special member $a_4 = 0$, $b_4 = H^2x_4^2$ (`flat_member_and_curvature`); and the vielbein factors enter every derivative term. In the chiral block form $\Psi = (\psi_-, \psi_+)$ every gamma is block off-diagonal, with upper-right block $\bar\tau^a$ and lower-left block $\tau^a$, and $\bar\tau^0 = \tau^0 = I_8$; the 16 equations become the two 8-component equations

$$
\begin{aligned}
&\sum_a f_a^{-1}\bar\tau^a\partial_a\psi_+ + c_g\psi_+ + v_g\bar\tau^4\psi_+ = V\psi_-,\\
&\sum_a f_a^{-1}\tau^a\partial_a\psi_- + c_g\psi_- + v_g\tau^4\psi_- = V\psi_+,\qquad V = m + U'(S).
\end{aligned}
$$

### 2.6 Records for section 2

| item | Wolfram records | sympy records |
| --- | --- | --- |
| metric, vielbein, $\sqrt{\lvert g\rvert}$ | `metric_is_the_corrected_metric`, `sqrt_det_g`, `primordial_vielbein` | `metric_from_vielbein_equals_SPEC`, `sqrt_det_g`, `geometry.fold_degenerate` |
| spin connection and $\gamma^\mu\Omega_\mu = c_g\gamma^0 + v_g\gamma^4$ | `omega_components`, `Omega_components`, `gammaOmega_total`, `gammaOmega_per_direction`, `primordial_connection_depends_on_b4` | `geometry.spin_connection_components`, `geometry.connection_depends_on_b4`, `gamma_mu_Omega_mu_equals_hidden_block_terms`, `per_direction_terms` |
| gammas | `coordinate_map`, `Clifford_relation`, `reality`, `signed_permutation_matrices`, `symmetry_pattern` | `clifford_relation`, `reality_signed_permutations`, `symmetry_pattern` |
| $C$, $\Gamma$, $B$, $S^{ab}$ | `C_real_symmetric`, `C_squared_identity`, `C_gamma_real_antisymmetric`, `C_gamma_C_inverse`, `Gamma_definition`, `Gamma_diag`, `B_Hermitian`, `B_squared_identity`, `B_signature_8_8`, `S_Lorentz_algebra` | `C_real_symmetric_involution`, `C_gamma_antisymmetric`, `C_conjugation`, `chirality_diag`, `B_hermitian_involution_signature`, `S_lorentz_algebra` |
| Pin(4,4) and Spin(4,4) | `Pin44_irreducible_commutant_dim_1`, `Spin44_commutant_dim_2_chiral_projectors`, `chiral_halves_irreducible`, `chiral_halves_inequivalent_intertwiners_0`, `Spin_Pin_reflection_swaps_halves` | `pin_commutant_dimension_1`, `spin_commutant_dimension_2`, `spin_halves_irreducible`, `spin_halves_inequivalent`, `reflections_exchange_halves` |
| reality of $\mathcal{L}$ | `L_real_G`, `L_real_C` | `grassmann_lagrangian_real`, `commuting_lagrangian_real` |
| Euler-Lagrange equations | `EL_Psi_G`, `EL_Psibar_G`, `EL_Psi_C`, `EL_Psibar_C`, `T1_Euler_Lagrange_derived_primordial_grassmann`, `T1_Euler_Lagrange_derived_primordial_commuting` | `grassmann_euler_lagrange_psi_variation`, `grassmann_euler_lagrange_psibar_variation`, `commuting_euler_lagrange_psi_variation`, `commuting_euler_lagrange_psibar_variation` |
| energy-momentum tensor | `T_symmetric_part_Belinfante_G`, `T_symmetric_part_Belinfante_C`, `kinetic_sum_on_shell_G`, `kinetic_sum_on_shell_C` | `grassmann_emt_symmetric`, `commuting_emt_symmetric`, `grassmann_homogeneous_on_shell_rho_p`, `commuting_homogeneous_on_shell_rho_p` |
| current and charge | `current_conservation_identity_G`, `current_conservation_identity_C`, `charge_density_is_Krein_form_G`, `charge_density_is_Krein_form_C` | `grassmann_current_conservation`, `commuting_current_conservation` |
| field equation in the metric, block form, non-triviality | `Dirac_operator_explicit_G`, `Dirac_operator_explicit_C`, `block_form`, `nontriviality_1_dirac16complex`, `nontriviality_2_dirac16complex00`, `flat_member_and_curvature` | `nontriviality_Omega_zero_iff_flat`, `gravity_term_square`, `curvature_and_flat_member` |
| scope of non-triviality: frame, variables, frame-independent content | `boosted_frame_gammaOmega_formula`, `boosted_frame_removes_only_the_H_term`, `boosted_frame_curvature_nonzero`, `rescaling_removes_the_connection_term`, `rescaled_equation_quadratic_potential`, `connection_free_lagrangian_same_equations`, `spin_curvature_equals_Riemann` | `boosted_frame_gammaOmega_formula`, `boosted_frame_removes_only_the_H_term`, `boosted_frame_curvature_nonzero`, `rescaling_removes_the_connection_term`, `rescaled_equation_quadratic_potential`, `connection_free_lagrangian_same_equations`, `spinor_curvature_equals_riemann` |

## 3. Algebraic lemmas

All four lemmas are exact matrix identities of the Revision gammas, verified by WolframScript and independently by sympy (records after each proof). They do not depend on the metric.

**Lemma 1 (the chirality matrix).** $\Gamma$ is real and symmetric, $\Gamma^2 = 1$, $\Gamma\gamma^a = -\gamma^a\Gamma$ for every $a$, $\Gamma C = C\Gamma$ and $\Gamma S^{ab} = S^{ab}\Gamma$. Hence $\Gamma\Omega_\mu = \Omega_\mu\Gamma$ for EVERY connection $\Omega_\mu = \frac12\omega_{\mu ab}S^{ab}$, and $D_\mu(\Gamma\Psi) = \Gamma D_\mu\Psi$, $D_\mu(\bar\Psi\Gamma) = (D_\mu\bar\Psi)\Gamma$.

Proof. $\Gamma$ is the product of all eight different $\gamma^a$. Moving $\gamma^b$ through it passes the seven factors $\gamma^a$, $a \neq b$, which anticommute with $\gamma^b$, and the factor $\gamma^b$ itself, which commutes with it: the sign is $(-1)^7 = -1$. $C$ is a product of four and $S^{ab}$ ($a \neq b$) a multiple of a product of two different gammas, so both commute with $\Gamma$. $\Gamma = \mathrm{diag}(-I_8, I_8)$ is computed exactly; it is real, symmetric and squares to 1. $\Gamma$ is constant and commutes with $\Omega_\mu$, which gives the statements about $D_\mu$. QED.

| Wolfram records | sympy records |
| --- | --- |
| `Gamma_properties`, `Gamma_diag`, `Gamma_anticommutes_with_gammas`, `Gamma_commutes_with_C`, `S_commutes_with_Gamma` | `gammas.Gamma`, `gammas.Gamma_anticommutes`, `chirality_anticommutes`, `chirality_C_relation`, `S_preserves_C_and_commutes_with_Gamma` |

**Lemma 2 (bilinears under the chirality map).** For $\Psi' = \Gamma\Psi$: $\bar\Psi' = \bar\Psi\Gamma$; $\bar\Psi' M\Psi' = (-1)^k\bar\Psi M\Psi$ for every product $M$ of $k$ gammas; in particular $S$ is invariant and every bilinear with $\gamma^a$, $\gamma^aS^{bc}$ or $S^{bc}\gamma^a$ changes sign. Moreover $\Gamma B\Gamma = -B$.

Proof. By Lemma 1, $\bar\Psi' = \Psi^\dagger\Gamma^\dagger C = \Psi^\dagger\Gamma C = \Psi^\dagger C\Gamma = \bar\Psi\Gamma$. Then $\bar\Psi'M\Psi' = \bar\Psi\,\Gamma M\Gamma\,\Psi$, and $\Gamma M\Gamma = (-1)^kM$ by Lemma 1. Finally $\Gamma B\Gamma = -iC\,\Gamma\gamma^4\Gamma = iC\gamma^4 = -B$. QED.

| Wolfram records | sympy records |
| --- | --- |
| `T1_kernel_scalar`, `T1_kernel_kinetic`, `T1_kernel_connection` (all 512 triples), `T1_kernel_field_equation`, `Q_Krein_metric_of_images` | `T1.general_field.matrix_identities` (456 kinetic and connection basis matrices), `Q.image_krein_metric` |

**Lemma 3 (reflections and their Pin(4,4) lifts).** Let $n$ be a frame direction and $R_n$ the diagonal matrix with $-1$ in place $n$ and $+1$ elsewhere (the reflection of that direction; $R_n\eta R_n = \eta$).

1. $(\gamma^n)^TC\gamma^n = -\eta_{nn}C$.
2. $\gamma^n\gamma^a(\gamma^n)^{-1} = -(R_n)^a{}_b\gamma^b$ and $\gamma^nS^{ab}(\gamma^n)^{-1} = (R_n)^a{}_c(R_n)^b{}_dS^{cd}$.
3. $P_n := \Gamma\gamma^n$ is plus or minus the product of the seven other gammas, hence an element of Pin(4,4); $P_n^{-1}\gamma^aP_n = (R_n)^a{}_b\gamma^b$ (it covers $R_n$); $P_n^\dagger CP_n = \chi_nC$ with the character $\chi_n = -\eta_{nn}$, i.e. $-1$ for the space-like $x_0, x_1, x_2, x_3$ and $+1$ for the time-like $x_4, x_5, x_6, x_7$; and $\Gamma P_n = \gamma^n$.

Proof. (1) From $C\gamma^nC^{-1} = -(\gamma^n)^T$ we have $C\gamma^n = -(\gamma^n)^TC$, so

$$
(\gamma^n)^TC\gamma^n = -\big((\gamma^n)^T\big)^2C = -\big((\gamma^n)^2\big)^TC = -\eta_{nn}C .
$$

(2) $\gamma^n$ anticommutes with $\gamma^a$ for $a \neq n$ and commutes with itself; the second identity follows by inserting the first into $S^{ab} = \frac14[\gamma^a,\gamma^b]$. (3) $\Gamma\gamma^n$ is, up to the sign of the reordering, the product of the eight gammas with $\gamma^n$ moved to the end, i.e. $\pm\eta_{nn}$ times the product of the other seven; each $\gamma^a$ is a unit vector ($(\gamma^a)^2 = \eta_{aa} = \pm1$), so the product lies in Pin(4,4). Using (2), $(\gamma^n)^{-1} = \eta_{nn}\gamma^n$, Lemma 1 and (1),

$$
\begin{aligned}
P_n^{-1}\gamma^aP_n &= (\gamma^n)^{-1}\Gamma\gamma^a\Gamma\gamma^n = -(\gamma^n)^{-1}\gamma^a\gamma^n = (R_n)^a{}_b\gamma^b ,\\
P_n^\dagger CP_n &= (\gamma^n)^T\Gamma C\Gamma\gamma^n = (\gamma^n)^TC\gamma^n = -\eta_{nn}C ,
\end{aligned}
$$

and $\Gamma P_n = \Gamma^2\gamma^n = \gamma^n$. QED. The signs of $P_n$ relative to the product of the other seven gammas (in the order of $\Gamma$) are @@PN_SIGNS@@ for $n = x_0, \dots, x_7$.

| Wolfram records | sympy records |
| --- | --- |
| `T2_Pn_in_Pin44`, `T2_Pn_covers_the_reflection`, `T2_character_of_Pn`, `T2_Gamma_times_Pn_is_gamma_n`, `T2_kernels_gamma_n_with_frame_reflection` | `T2.general_field.matrix_identities`, `T2.general_field.reflection_table`, `compare.theory.reflection_table` |

**Lemma 4 (Krein signs of the maps).** $MBM^\dagger = \sigma_MB$ with $\sigma_\Gamma = -1$; $\sigma_{\gamma^n} = +1$ for $n = x_0, x_1, x_2, x_3, x_4$ and $-1$ for $n = x_5, x_6, x_7$; and $\sigma_{P_n} = -\sigma_{\gamma^n}$, i.e. $-1$ for $P_{x_0}, P_{x_1}, P_{x_2}, P_{x_3}, P_{x_4}$ and $+1$ for $P_{x_5}, P_{x_6}, P_{x_7}$.

Proof. $\Gamma$: Lemma 2. For $\gamma^n$: it is real, so $(\gamma^n)^\dagger = (\gamma^n)^T = \eta_{nn}\gamma^n$, and transposing $C\gamma^nC^{-1} = -(\gamma^n)^T$ with $C^T = C = C^{-1}$ gives $\gamma^nC = -C(\gamma^n)^T$. Hence

$$
\gamma^nB(\gamma^n)^\dagger = -i\gamma^nC\gamma^4(\gamma^n)^T = iC(\gamma^n)^T\gamma^4(\gamma^n)^T = iC\gamma^n\gamma^4\gamma^n .
$$

For $n \neq 4$, $\gamma^n\gamma^4\gamma^n = -\eta_{nn}\gamma^4$ and the result is $\eta_{nn}B$; for $n = 4$, $\gamma^4\gamma^4\gamma^4 = -\gamma^4$ and the result is $B$. Finally $P_nBP_n^\dagger = \Gamma\,\gamma^nB(\gamma^n)^\dagger\,\Gamma = -\sigma_{\gamma^n}B$ by Lemma 2. QED.

| Wolfram records | sympy records |
| --- | --- |
| `Q_Krein_metric_of_images` | `compare.theory.krein_signs`, `Q.image_krein_metric`, `Q.T2_image_keeps_B` |

## 4. Theorem T1: the chirality pairing (both fields)

### 4.1 Hypotheses

- (H1) The gravitational field: any vielbein $e^a{}_\mu$ (metric $g = e^T\eta e$ of signature (4,4)) and any spin connection $\omega_{\mu ab} = -\omega_{\mu ba}$, in particular the canonical one of the corrected metric. The field is a fixed (test) background: it is NOT varied, and both members of the pair are evaluated in the SAME field.
- (H2) The statistics: $\Psi$ Grassmann-valued (dirac16complex) or commuting (dirac16complex00). The map acts at the same point, $\Psi'(x) = \Gamma\Psi(x)$, with no change of coordinates.
- (H3) The potential: $U(S) = \frac{\lambda}{2}S^2$; more generally any function $U$ (commuting field) or any polynomial $U$ (Grassmann field), mapped to $-U$.
- (H4) $\mathcal{L}$, $E$, $T$ and $J$ as in section 2, with any overall sign or constant factor of $T$ and $J$.

### 4.2 Statement

**Theorem T1.** Under (H1) to (H4), for both fields:

- (T1a) $\mathcal{L}_{m,\lambda}[\Gamma\Psi] = -\mathcal{L}_{-m,-\lambda}[\Psi]$ identically (off shell); for a general potential $\mathcal{L}_{m,U}[\Gamma\Psi] = -\mathcal{L}_{-m,-U}[\Psi]$. Separately, $S[\Gamma\Psi] = S[\Psi]$ and $K[\Gamma\Psi] = -K[\Psi]$.
- (T1b) $E_{m,\lambda}[\Gamma\Psi] = -\Gamma E_{-m,-\lambda}[\Psi]$: $\Gamma\Psi$ solves the field equations with $(m,\lambda)$ if and only if $\Psi$ solves those with $(-m,-\lambda)$; equivalently, $\Psi$ solves the $(m,\lambda)$ equations if and only if $\Gamma\Psi$ solves the $(-m,-\lambda)$ equations. The Euler-Lagrange expressions are mapped in the same way.
- (T1c) $T^{(-m,-\lambda)}_{\mu\nu}[\Gamma\Psi] = -T^{(m,\lambda)}_{\mu\nu}[\Psi]$ and $J^\mu[\Gamma\Psi] = -J^\mu[\Psi]$ pointwise, off and on shell.
- (T1d) The pair ($\Psi$ with $(m,\lambda)$; $\Gamma\Psi$ with $(-m,-\lambda)$) has the total energy-momentum density $T + T' = 0$, the total current $J + J' = 0$ and the total charge $Q + Q' = 0$, as classical bilinears (c-numbers for dirac16complex00, elements of the Grassmann algebra for dirac16complex).

### 4.3 Proof

Step 1 (bilinears). By Lemma 1, $D_\mu(\Gamma\Psi) = \Gamma D_\mu\Psi$ and $D_\mu(\overline{\Gamma\Psi}) = (D_\mu\bar\Psi)\Gamma$; by Lemma 2, $S[\Gamma\Psi] = S[\Psi]$ and

$$
\overline{\Gamma\Psi}\,\gamma^\mu D_\mu(\Gamma\Psi) = \bar\Psi\,\Gamma\gamma^\mu\Gamma\,D_\mu\Psi = -\bar\Psi\gamma^\mu D_\mu\Psi ,
\qquad
\big(D_\mu\overline{\Gamma\Psi}\big)\gamma^\mu\,\Gamma\Psi = -(D_\mu\bar\Psi)\gamma^\mu\Psi ,
$$

hence $K[\Gamma\Psi] = -K[\Psi]$. Written out,

$$
K = \tfrac12\,e^\mu{}_a\big(\bar\Psi\gamma^a\partial_\mu\Psi - \partial_\mu\bar\Psi\gamma^a\Psi\big) + \tfrac14\,e^\mu{}_a\,\omega_{\mu bc}\,\bar\Psi\{\gamma^a,S^{bc}\}\Psi ,
$$

a sum of coefficient functions of the gravitational field times bilinears with an odd number of gammas; each such bilinear changes sign by Lemma 2, whatever the coefficients are.

Step 2 (the Lagrangian). $U(S)$ is unchanged because $S$ is, so

$$
\mathcal{L}_{m,U}[\Gamma\Psi] = \sqrt{|g|}\,\big[-K - mS - U(S)\big] = -\sqrt{|g|}\,\big[K - (-m)S - (-U)(S)\big] = -\mathcal{L}_{-m,-U}[\Psi] ,
$$

which for $U = \frac{\lambda}{2}S^2$ is (T1a).

Step 3 (the field equations). $\gamma^\mu D_\mu(\Gamma\Psi) = \gamma^\mu\Gamma D_\mu\Psi = -\Gamma\gamma^\mu D_\mu\Psi$, so

$$
E_{m,\lambda}[\Gamma\Psi] = -\Gamma\gamma^\mu D_\mu\Psi - (m + \lambda S)\Gamma\Psi = -\Gamma\big[\gamma^\mu D_\mu\Psi - (-m - \lambda S)\Psi\big] = -\Gamma E_{-m,-\lambda}[\Psi] ,
$$

and $\Gamma$ is invertible, which gives (T1b). For the Euler-Lagrange expressions themselves, in any field and whatever their explicit form: (T1a) is an identity between functionals of $\Psi$, and $\Psi \mapsto \Gamma\Psi$ is a constant invertible linear substitution, so by the chain rule the Euler-Lagrange expressions of $\mathcal{L}_{m,\lambda}$ at $\Gamma\Psi$, multiplied by $\Gamma$, equal minus those of $\mathcal{L}_{-m,-\lambda}$ at $\Psi$; they vanish together.

Step 4 (energy-momentum tensor and current). $T^\nu{}_\mu$ is the sum of $\delta^\nu_\mu\mathcal{L}/\sqrt{|g|}$ and kinetic bilinears with one gamma. By Step 2 with $m \to -m$, $\mathcal{L}_{-m,-\lambda}[\Gamma\Psi] = -\mathcal{L}_{m,\lambda}[\Psi]$, and by Step 1 each kinetic bilinear changes sign; hence $T^{(-m,-\lambda)}[\Gamma\Psi] = -T^{(m,\lambda)}[\Psi]$. The same holds for the tensor of the vielbein variation, whose additional term $\nabla_\lambda(\bar\Psi\{\gamma^\lambda,\Sigma^{\nu\rho}\}\Psi)$ contains three gammas. $J^\mu$ is a multiple of $\bar\Psi\gamma^\mu\Psi$ and changes sign by Lemma 2, and so does $Q = \int\sqrt{|g|}\,J^{x_4}\,d^7x$. This is (T1c).

Step 5 (the pair). Adding (T1c) to the quantities of $\Psi$ gives (T1d).

Step 6 (statistics). $\Gamma = \mathrm{diag}(-I_8, I_8)$ multiplies each component by $+1$ or $-1$; no Grassmann factors are reordered, so Steps 1 to 5 hold verbatim for anticommuting components, as identities between Grassmann-algebra elements.

The proof uses only Lemmas 1 and 2 and the linearity of $\mathcal{L}$, $T$ and $J$ in the coefficient functions $\sqrt{|g|}$, $e^\mu{}_a$ and $\omega_{\mu ab}$; hence T1 holds in every gravitational field (H1). QED.

### 4.4 T1 in the block form of the primordial field

In the primordial field the proof can be read off the block equations of section 2.5. $\Gamma(\psi_-, \psi_+) = (-\psi_-, \psi_+)$, and $C$ is block diagonal (a product of four gammas; the algebra record gives $C = \mathrm{diag}(-\sigma, \sigma)$ with $\sigma$ the notebook's $8 \times 8$ involution), so $S = -\psi_-^\dagger\sigma\psi_- + \psi_+^\dagger\sigma\psi_+$ is unchanged and $V = m + \lambda S$ becomes $-m - \lambda S = -V$ for the parameters $(-m,-\lambda)$. The two block equations become

$$
\sum_a f_a^{-1}\bar\tau^a\partial_a\psi_+ + c_g\psi_+ + v_g\bar\tau^4\psi_+ = (-V)(-\psi_-),\qquad
-\Big(\sum_a f_a^{-1}\tau^a\partial_a\psi_- + c_g\psi_- + v_g\tau^4\psi_-\Big) = -V\psi_+ ,
$$

the same equations. None of the gravitational terms ($e^{-a_4}$, $e^{a_4}b_4^{-1/2}(\sin^2 z)^{-1/12}$, $e^{a_4}b_4^{-1/2}\tan z$, $c_g$, $v_g$) changes.

| Wolfram records (primordial field) | sympy records (primordial field) |
| --- | --- |
| `T1_Lagrangian_primordial_commuting` (408 monomials), `T1_Lagrangian_primordial_grassmann` (392 monomials), `T1_field_equation_covariance_primordial_commuting`, `T1_field_equation_covariance_primordial_grassmann`, `T1_energy_momentum_primordial_commuting`, `T1_energy_momentum_primordial_grassmann`, `T1_current_primordial_commuting`, `T1_current_primordial_grassmann` | `C_equals_notebook_sigma16`, `T1.metric.commuting.lagrangian`, `T1.metric.grassmann.lagrangian`, `T1.metric.commuting.euler_lagrange_map`, `T1.metric.grassmann.euler_lagrange_map`, `T1.metric.commuting.pair_total_emt_zero`, `T1.metric.grassmann.pair_total_emt_zero` |

### 4.5 Remarks on T1

- Negative controls: $\mathcal{L}_{m,\lambda}[\Gamma\Psi] + \mathcal{L}_{m,\lambda}[\Psi] \neq 0$ and $\mathcal{L}_{m,\lambda}[\Gamma\Psi] + \mathcal{L}_{-m,\lambda}[\Psi] \neq 0$: the mass AND the coupling must change sign. For $\lambda \neq 0$, T1 is therefore not a pure $+m$ / $-m$ pairing; for $\lambda = 0$ (free fields) it pairs $+m$ with $-m$ exactly.
- The partner's energy density, pressures and equations of state: $\rho' = -\rho$ and $p_\mu' = -p_\mu$ in every direction; for homogeneous on-shell states $\rho = mS + \frac{\lambda}{2}S^2$ and $p = \frac{\lambda}{2}S^2$ become $\rho' = -mS - \frac{\lambda}{2}S^2$ and $p' = -\frac{\lambda}{2}S^2$ (with $S' = S$). Every ratio of components, in particular $w_3 = p_3/\rho$, $w_t = p_t/\rho$ and $w_{x_0} = p_0/\rho$, is the same for both members.
- T1 is not a symmetry of one theory: it changes the parameters and the sign of the action. Because $-\mathcal{L}$ and $\mathcal{L}$ have the same Euler-Lagrange equations, $\Gamma\Psi$ is a solution of the $(-m,-\lambda)$ theory; nothing more is asserted.
- Representation content: $\Gamma$ is $-1$ on one irreducible Spin(4,4) half and $+1$ on the other (section 2.2); the partner differs from $\Psi$ by the relative sign of its two inequivalent Spin(4,4) components, and $\Gamma$ is itself an element of Pin(4,4) (a product of eight unit vectors).

| Wolfram records (negative controls) | sympy records (negative controls) |
| --- | --- |
| `T1_Lagrangian_negative_controls_primordial_commuting`, `T1_Lagrangian_negative_controls_primordial_grassmann`, `T1_Lagrangian_negative_controls_diagonal8_commuting`, `T1_Lagrangian_negative_controls_diagonal8_grassmann`, `T1_Lagrangian_negative_controls_pointwise_commuting`, `T1_Lagrangian_negative_controls_pointwise_grassmann` | `T1.metric.commuting.negative_controls`, `T1.metric.grassmann.negative_controls` |

## 5. Theorem T2: the mirror pairing (both fields)

### 5.1 Hypotheses

- (H5) $n$ is a space-like frame direction ($x_0$, $x_1$, $x_2$ or $x_3$), and $P_n = \Gamma\gamma^n$ is the Pin(4,4) lift of the reflection $R_n$, of character $-1$ (Lemma 3).
- (H6) General-field version: the frame is reflected, $e' = R_ne$ (the same metric, since $R_n\eta R_n = \eta$, and the same $\sqrt{|g|}$), with its canonical connection, and $\Psi'(x) = \Gamma P_n\Psi(x) = \gamma^n\Psi(x)$ at the same point.
- (H7) Primordial-field version: the map $\phi: x_0 \mapsto \pi/(6H) - x_0$ ($z \mapsto \pi - z$, the reflection across the fold $z = \pi/2$) takes the patch $z \in (0,\pi/2)$ onto the other half $z \in (\pi/2,\pi)$ of the cell; each half carries its own positive vielbein ($e^0 = e^{-a_4}b_4^{1/2}|\cot z|\,dx_0$, i.e. $-e^{-a_4}b_4^{1/2}\cot z\,dx_0$ on the other half); and $\Psi'(\phi(x)) = \gamma^0\Psi(x)$. The fold $z = \pi/2$ is a degenerate surface of the metric ($g_{00} = e^{-2a_4}b_4\cot^2 z = 0$ and $\sqrt{|g|} = 0$ there); the corrected metric has no Z2 orbifold, T2 relates solutions on the two halves of a cell, and no junction condition or matching of the field across the fold is derived (a field continuous across the fold is not thereby its own mirror image).
- (H8) Both statistics; $U(S) = \frac{\lambda}{2}S^2$ or any even function of $S$.

### 5.2 Statement

**Theorem T2.** Under (H5) to (H8), for both fields:

- (T2a) $\mathcal{L}_{m,\lambda}[\gamma^n\Psi;\,R_ne] = +\mathcal{L}_{-m,\lambda}[\Psi;\,e]$ in every gravitational field; in the primordial field $\mathcal{L}_{m,\lambda}[\Psi'](\phi(x)) = \mathcal{L}_{-m,\lambda}[\Psi](x)$.
- (T2b) $S' = -S$, and $E_{m,\lambda}[\gamma^n\Psi;\,R_ne] = -\gamma^nE_{-m,\lambda}[\Psi;\,e]$: $\Psi$ solves the $(-m,\lambda)$ equations if and only if its image solves the $(m,\lambda)$ equations (in the primordial field: on the patch and on the other half of the cell respectively).
- (T2c) In the general-field version $T'_{\mu\nu} = T^{(-m,\lambda)}_{\mu\nu}[\Psi]$ and $J'^\mu = J^\mu[\Psi]$. In the primordial field $T_{\mu\nu}[\Psi'](\phi(x)) = (R_0\,T^{(-m,\lambda)}[\Psi](x)\,R_0)_{\mu\nu}$ and $J'^\mu = (R_0)^\mu{}_\nu J^\nu$: the energy density and every component without an $x_0$ index are EQUAL, not opposite. T2 pairs $+m$ with $-m$ at equal energy-momentum.
- (T2d) For a time-like $n$ (character $+1$) the same construction gives $\mathcal{L} \to -\mathcal{L}_{-m,-\lambda}$, a T1-type map; the character $-1$ is what makes T2 a pairing $(m,\lambda) \to (-m,\lambda)$ with $\mathcal{L} \to +\mathcal{L}$.

### 5.3 Proof in a general field (frame reflection)

Step 1 (geometry). $g' = e'^T\eta e' = e^TR_n\eta R_ne = g$. The canonical connection of $e'$ is $R_n\omega R_n$: $R_n$ is a constant Lorentz transformation, and the canonical connection $\omega_\mu{}^a{}_b = e^a{}_\nu(\partial_\mu e^\nu{}_b + \Gamma^\nu{}_{\mu\lambda}e^\lambda{}_b)$ is built from the vielbein, its inverse and the Christoffel symbols $\Gamma^\nu{}_{\mu\lambda}$ of the unchanged metric (the symbol with indices is the Christoffel symbol, without indices the chirality matrix). By Lemma 3, $\Omega'_\mu = \frac12(R_n\omega_\mu R_n)_{ab}S^{ab} = \gamma^n\Omega_\mu(\gamma^n)^{-1}$, so $D'_\mu(\gamma^n\Psi) = \gamma^nD_\mu\Psi$.

Step 2 (adjoint). By Lemma 3, $(\gamma^n)^TC = -\eta_{nn}C(\gamma^n)^{-1}$, hence $\bar\Psi' = \Psi^\dagger(\gamma^n)^TC = -\eta_{nn}\bar\Psi(\gamma^n)^{-1}$ and $D'_\mu\bar\Psi' = -\eta_{nn}(D_\mu\bar\Psi)(\gamma^n)^{-1}$.

Step 3 (gammas). The reflected frame gives $\gamma'^\mu = e^\mu{}_b(R_n)^b{}_a\gamma^a$, and Lemma 3 gives $\gamma'^\mu\gamma^n = -\gamma^n\gamma^\mu$. Therefore

$$
\bar\Psi'\gamma'^\mu D'_\mu\Psi' = -\eta_{nn}\bar\Psi(\gamma^n)^{-1}\gamma'^\mu\gamma^nD_\mu\Psi = \eta_{nn}\bar\Psi\gamma^\mu D_\mu\Psi ,
\qquad
\bar\Psi'\Psi' = -\eta_{nn}\bar\Psi\Psi ,
$$

and in the same way $(D'_\mu\bar\Psi')\gamma'^\mu\Psi' = \eta_{nn}(D_\mu\bar\Psi)\gamma^\mu\Psi$, so $K' = \eta_{nn}K$ and $S' = -\eta_{nn}S$.

Step 4 (Lagrangian). For space-like $n$ ($\eta_{nn} = +1$): $K' = K$ and $S' = -S$, so

$$
\mathcal{L}_{m,\lambda}[\Psi';e'] = \sqrt{|g|}\,\big[K + mS - \tfrac{\lambda}{2}S^2\big] = \mathcal{L}_{-m,\lambda}[\Psi;e] ,
$$

which is (T2a). For time-like $n$: $K' = -K$ and $S' = S$, so $\mathcal{L}_{m,\lambda}[\Psi';e'] = -\mathcal{L}_{-m,-\lambda}[\Psi;e]$, which is (T2d).

Step 5 (field equations). For space-like $n$,

$$
E_{m,\lambda}[\Psi';e'] = \gamma'^\mu D'_\mu(\gamma^n\Psi) - (m + \lambda S')\gamma^n\Psi = -\gamma^n\gamma^\mu D_\mu\Psi - (m - \lambda S)\gamma^n\Psi = -\gamma^nE_{-m,\lambda}[\Psi;e] ,
$$

which is (T2b).

Step 6 (energy-momentum tensor and current). The kinetic bilinears $\bar\Psi\gamma_\mu D_\nu\Psi$ with free indices transform like the contracted one in Step 3 (factor $\eta_{nn} = +1$), and $\mathcal{L}/\sqrt{|g|}$ transforms by Step 4, so $T'_{\mu\nu} = T^{(-m,\lambda)}_{\mu\nu}[\Psi]$; $\bar\Psi'\gamma'^\mu\Psi' = \eta_{nn}\bar\Psi\gamma^\mu\Psi$ gives $J' = J$. This is (T2c) in the general-field version.

Step 7 (statistics). $\gamma^n$ is a constant signed permutation matrix; the substitution never reorders Grassmann factors, so Steps 1 to 6 hold for both statistics. QED.

### 5.4 Proof in the primordial field (the reflection across the fold)

$\phi$ is an isometry of the corrected metric: its components depend on $x_0$ only through $\cot^2 z$ and $(\sin^2 z)^{1/6}$, both invariant under $z \mapsto \pi - z$. The positive vielbein of the other half of the cell, pulled back by $\phi$, is $R_0e$: its hidden leg is $-e^{-a_4}b_4^{1/2}\cot(\pi - z)\,d(\pi/(6H) - x_0) = -e^{-a_4}b_4^{1/2}\cot z\,dx_0 = -e^0$, and the other legs are unchanged. $\sqrt{|g|}\,d^8x$ is invariant ($e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}$ is invariant and the Jacobian has modulus 1). Pulling the Lagrangian of the other half back by $\phi$ therefore gives the frame-reflected Lagrangian of section 5.3 with $n = x_0$, which proves (T2a) and (T2b) in the primordial field; the coordinate components of $T$ and $J$ pick up the Jacobian $R_0$ of $\phi$, which gives (T2c). QED.

In block form $\gamma^0$ has the blocks $\bar\tau^0 = \tau^0 = I_8$, so $\gamma^0(\psi_-, \psi_+) = (\psi_+, \psi_-)$: the mirror image exchanges the two inequivalent Spin(4,4) halves, and $S = -\psi_-^\dagger\sigma\psi_- + \psi_+^\dagger\sigma\psi_+$ changes sign.

| Wolfram records (primordial field) | sympy records (primordial field) |
| --- | --- |
| `T2_mirror_is_isometry`, `T2_mirror_Lagrangian_commuting`, `T2_mirror_Lagrangian_grassmann`, `T2_mirror_energy_momentum_and_current_commuting`, `T2_mirror_energy_momentum_and_current_grassmann`, `T2_mirror_Euler_Lagrange_commuting`, `T2_mirror_Euler_Lagrange_grassmann` | `geometry.mirror_isometry`, `geometry.fold_degenerate`, `T2.metric.commuting.euler_lagrange_map`, `T2.metric.grassmann.euler_lagrange_map`, `T2.metric.commuting.emt`, `T2.metric.grassmann.emt`, `T2.metric.commuting.current`, `T2.metric.grassmann.current`, `T2.metric.commuting.S_odd`, `T2.metric.grassmann.S_odd` |

### 5.5 The eight reflections

The sympy checker also shows that neither the plain mirror ($P = 1$) nor $\Gamma$ alone gives a relation $\mathcal{L}_{\mathrm{mirror}} = \pm\mathcal{L}_{\mathrm{patch}}$ with $(m,\lambda) \to (\pm m, \pm\lambda)$, that $P_0 = \Gamma\gamma^0$ alone gives $\mathcal{L} \to -\mathcal{L}_{m,-\lambda}$, and that its composition with $\Gamma$ gives T2. The frame reflections of all eight directions, from the data of the pairing theory record (the Wolfram pointwise frame-reflection checks of every direction and the sympy frame-reflection checks of the general diagonal field, both statistics; the record names are in the T2 tables of section 9.2):

@@REFLECTION_TABLE@@

In the primordial field only the reflection of $x_0$ is realised by an isometry that maps the patch onto another patch (the other half of the cell, across the fold); the reflections of $x_1, x_2, x_3$ are frame statements.

## 6. The quantum-level reading (dirac16complex)

### 6.1 Hypotheses

- (HQ1) dirac16complex is canonically quantised with $x_4$ as the evolution time. The $x_4$-derivative kernel of $\mathcal{L}_{m,\lambda}$ is $\frac{i}{2}\sqrt{|g|}\,N$ with $N = B$ (since $C\gamma^4 = iB$), and the canonical anticommutator on a slice $x_4 = \mathrm{const}$ is $\{\Psi_A(x), \Psi^\dagger_B(y)\} = (N^{-1})_{AB}\,\delta^7(x - y)/\sqrt{|g|} = B_{AB}\,\delta^7(x - y)/\sqrt{|g|}$.
- (HQ2) dirac16complex00 is a classical field and has no quantum reading.

### 6.2 Statements

- (Q1) The chirality image $\chi = \Gamma\Psi$ carries the Krein metric $-B$: $\{\chi_A, \chi^\dagger_B\} = (\Gamma B\Gamma)_{AB}\,\delta/\sqrt{|g|} = -B_{AB}\,\delta/\sqrt{|g|}$, which is also the anticommutator demanded by its own Lagrangian $\mathcal{L}_{m,\lambda}[\Gamma\chi] = -\mathcal{L}_{-m,-\lambda}[\chi]$.
- (Q2) The image's own generators (energy, momentum and charge from its own Lagrangian) coincide with those of $\Psi$: the pair $\Psi$, $\Gamma\Psi$ is ONE quantum system, and the T1 identity $T^{(-m,-\lambda)}[\Gamma\Psi] = -T^{(m,\lambda)}[\Psi]$ is an identity between operators of that one system.
- (Q3) An independently quantised $(-m,-\lambda)$ universe has the anticommutator $+B$ (from $\mathcal{L}_{-m,-\lambda}$), its own vacuum and its own generators; it cannot be identified with $\Gamma\Psi$ ($B \neq -B$); on the product state space the generators add, $P_{\mathrm{total}} = P_1\otimes 1 + 1\otimes P_2$, and no cancellation $P_1 + P_2 = 0$ follows.
- (Q4) The one-particle ($\lambda = 0$) Hamiltonians satisfy $\Gamma h_m\Gamma = h_{-m}$ (flat space, and a general field at a point with frozen coefficients) and $\gamma^0h_m(k)\gamma^0 = h_{-m}(R_0k)$: the $+m$ and $-m$ one-particle spectra are IDENTICAL, not opposite. In flat 4+4 space $h_m(k) = -im\gamma^4 - \gamma^4\sum_{a \neq 4}k_a\gamma^a$ and $h_m(k)^2 = w^2 I_{16}$ with $w^2 = m^2 + k_0^2 + k_1^2 + k_2^2 + k_3^2 - k_5^2 - k_6^2 - k_7^2$; for every REAL frequency ($w^2 > 0$, with or without extra-time momentum) each of the two eigenspaces has dimension 8 and Krein inertia (4,4), the same for $+m$ and $-m$, and for imaginary or zero frequency (the growing extra-time modes) the eigenspaces are Krein-neutral ($B$ vanishes on them).
- (Q5) The T2 image $\gamma^0\Psi$ keeps the anticommutator $+B$: the mirror $(-m,\lambda)$ universe is an ordinary, independently quantisable copy with equal energies.

### 6.3 Proofs

(Q1) By Lemma 2, $\{\Gamma\Psi, (\Gamma\Psi)^\dagger\} = \Gamma\{\Psi, \Psi^\dagger\}\Gamma^\dagger = \Gamma B\Gamma\,\delta/\sqrt{|g|} = -B\,\delta/\sqrt{|g|}$. For the image's own Lagrangian, the $x_4$-velocity term $\frac{i}{2}\sqrt{|g|}\,\chi^\dagger\Gamma B\Gamma\,\partial_4\chi$ has the kernel $N = -B$, hence the anticommutator $N^{-1} = -B$: the two agree.

(Q2) At $\chi = \Gamma\Psi$ the image Lagrangian $\mathcal{L}_{m,\lambda}[\Gamma\chi]$ is $\mathcal{L}_{m,\lambda}[\Psi]$, the same function of the same operators, so its Legendre energy density and its Noether densities coincide with those of $\Psi$; they are minus the generators of the $(-m,-\lambda)$ Lagrangian evaluated at $\chi$. With the metric $-B$ and the generator density $-h_m$ the image evolves by $(-B)(-h_m) = Bh_m$, exactly the $(m,\lambda)$ dynamics.

(Q3) The Lagrangian $\mathcal{L}_{-m,-\lambda}[\chi_2]$ of an independent universe has the kernel $N = +B$, hence $\{\chi_2, \chi_2^\dagger\} = +B\,\delta/\sqrt{|g|}$, while $\{\Gamma\Psi_1, (\Gamma\Psi_1)^\dagger\} = -B\,\delta/\sqrt{|g|}$; and independence requires $\{\Psi_1, \chi_2^\dagger\} = 0$, whereas $\{\Gamma\Psi_1, \Psi_1^\dagger\} = \Gamma B/\sqrt{|g|}$ has rank 16. So no identification $\chi_2 = \Gamma\Psi_1$ exists. On the product space the generators of the two systems add; the T1 identity relates operators of universe 1 only and gives no relation $P_2 = -P_1$. At zero momentum the block one-particle generator $\mathrm{diag}(Bh_m, Bh_{-m})$ has the eigenvalues $-m$ and $m$, each 16 times, all nonzero for $m \neq 0$.

(Q4) $\Gamma\gamma^4\Gamma = -\gamma^4$ and $\Gamma\gamma^4\gamma^a\Gamma = \gamma^4\gamma^a$ give $\Gamma h_m\Gamma = h_{-m}$. With $(\gamma^0)^2 = 1$,

$$
\gamma^0\gamma^4\gamma^0 = -\gamma^4,\qquad
\gamma^0\gamma^4\gamma^a\gamma^0 = \gamma^4\gamma^a \ (a \neq 0, 4),\qquad
\gamma^0\gamma^4\gamma^0\gamma^0 = -\gamma^4\gamma^0 ,
$$

which gives $\gamma^0h_m(k)\gamma^0 = h_{-m}(R_0k)$. Similar matrices have equal spectra. The square and the eigenspaces are computed exactly; the samples of `Revision/pairing/pairing-theory.json` are:

@@SAMPLE_TABLE@@

The entry $k_4$ is not used ($h_m$ contains no $\gamma^4\gamma^4$ term). The last two rows have an extra-time momentum and a real frequency. The general statement is proved, not sampled: (i) for real $w > 0$ the projectors $P_\pm = (1 \pm h_m/w)/2$ satisfy $P_+^\dagger BP_- = 0$ and $P_+^\dagger BP_+ = BP_+$ (from $Bh_m = h_m^\dagger B$ and $h_m^2 = w^2$), so the two eigenspaces are $B$-orthogonal and $B$ is nondegenerate on each; (ii) in the good sector $[B, h_m] = 0$ and $\mathrm{tr}\,B = \mathrm{tr}(Bh_m) = 0$, so $\mathrm{tr}(BP_\pm) = 0$ and $B$ has inertia (4,4) on each eigenspace; (iii) the region $w^2 > 0$ is connected and contains the good sector (lowering $k_5, k_6, k_7$ to zero only increases $w^2$), and $P_\pm$ depend continuously on $k$ there, so the inertia (4,4) holds at every real frequency. For imaginary $w$, $h u = wu$ and $hv = wv$ give $(w - \bar w)\,u^\dagger Bv = 0$: the eigenspace is Krein-neutral; for $w = 0$, $h^2 = 0$ with rank 8 and $\ker h = \mathrm{ran}\,h$ is $B$-neutral. Exact samples: $m = 1$, $k_5 = 2$ ($w = \pm i\sqrt3$); $m = 1$, $k_1 = 1$, $k_5 = 2$ ($w = \pm i\sqrt2$); $m = 1$, $k_5 = 1$ ($w = 0$): every eigenspace has dimension 8 and the form $u^\dagger Bv$ vanishes on it identically. In a general field at a point the same similarity $\Gamma h_m\Gamma = h_{-m}$ holds for symbolic momenta; in the pointwise test field $(\gamma^{x_4})^2 = g^{x_4x_4}I_{16} = -\frac{2307429}{1990921}I_{16}$ (the coefficients of that field are a formula in the list positions of the coordinates, the author's order).

(Q5) Lemma 4 gives $\gamma^0B(\gamma^0)^\dagger = +B$. QED.

| statement | Wolfram records | sympy records |
| --- | --- | --- |
| (HQ1) | `first_order_form_and_anticommutator` | `canonical_anticommutator_B`, `Q.canonical_anticommutator` |
| (Q1) | `Q_Krein_metric_of_images`, `Q_symplectic_kernel_commuting`, `Q_symplectic_kernel_grassmann` | `Q.image_krein_metric`, `Q.image_own_quantisation` |
| (Q2) | `Q_generators_of_the_image_commuting`, `Q_generators_of_the_image_grassmann` | `Q.image_generators_same_dynamics` |
| (Q3) | `Q_no_identification_of_independent_universes` | `Q.no_cancellation_independent_universes` |
| (Q4) | `Q_one_particle_flat_dispersion`, `Q_one_particle_maps`, `Q_one_particle_Krein_signatures`, `Q_one_particle_Krein_inertia_real_frequencies`, `Q_one_particle_complex_and_zero_frequencies_Krein_neutral`, `Q_one_particle_general_field` | `Q.one_particle_maps`, `Q.one_particle_Krein_inertia`, `Q.one_particle_Krein_inertia_proof`, `Q.one_particle_complex_frequency_Krein_neutral`, `compare.theory.one_particle` |
| (Q5) | `Q_Krein_metric_of_images` | `Q.T2_image_keeps_B` |

Relation to the good sector of the theory record. With $\Psi^\dagger$ realised as the Hilbert adjoint, the canonical anticommutator forces an indefinite (Krein) inner product (record `no_positive_inner_product`). The theory record constructs, in the good sector without extra-time momentum, a positive Fock representation in which $\Psi^\dagger$ is realised as $\chi B$ with $\chi$ the Hilbert adjoint, but only for single good-sector momenta with frozen coefficients (flat-frame plane waves, in which the deflation of the extra times does not enter; records `mode_hamiltonian_good_sector`, `Fock_space_good_sector_example` and `good_sector_positive_fock_realisation`). In the corrected metric the curved good-sector mode operator is Hermitian only up to a boundary term at the degenerate points $z = \pi/2 + n\pi$ (`good_sector_hermiticity_up_to_the_brane_flux`; the check keeps its name from the withdrawn metric of 2026-10-14, while its detail and the corrected metric have no brane: these degenerate points are the folds of section 2.1); the theory record imposes no boundary condition there, and without one the good sector has complex frequencies wherever $m^2 < c_g^2$ (for $U = 0$; on the background history $c_g$ grows, so every mass falls below it at late $x_4$: `good_sector_x0_independent_modes_without_boundary_condition`). A positive-norm Hilbert space for the full field is not established. The statements Q1 to Q5 are statements about the canonical anticommutator; they neither use nor establish a positive-norm Fock space for either universe.

## 7. Corollary C1: a T1 pair as the source of the field equations for $a_4$ and $b_4$

**Hypotheses.** (i) The gravitational field is the corrected metric and the Einstein-Lovelock equations $\sum_{k=1}^3\alpha_kE_{(k)}{}^\mu{}_\nu + \Lambda\delta^\mu_\nu = \kappa T^\mu{}_\nu$ of `Revision/SPEC.md` section 5. (ii) The complete source is the sum of the classical energy-momentum tensors of the two members of a T1 pair at the same points of the same patch (dirac16complex00, or dirac16complex as a Grassmann-algebra-valued classical bilinear). (iii) Nothing else sources the metric.

**Statement.** The total source vanishes identically, so $a_4$ and $b_4$ must solve the vacuum equations. (a) In Einstein gravity ($\alpha_1 = 1$, $\alpha_2 = \alpha_3 = 0$) the flat member $a_4 = 0$, $b_4 = H^2(x_4 - c)^2$ solves the vacuum equations with $\Lambda = 0$, while no exponential history $a_4 = AHx_4 + a_0$, $b_4 = b_4(0)e^{\beta AHx_4}$ is a vacuum solution, for any $\Lambda$ (the vacuum equations have no real solution with $k = e^{2a_4}/b_4 > 0$). (b) With the author's Lovelock weights ($\alpha_k = w_k/H^{2k}$, $w = (1, \frac{1}{32}, \frac{1}{1152})$, $\Lambda = -10$ in the sign convention of the equations in (i), which is the author's $\Lambda = 10$ of `Revision/SPEC.md` section 1) no exponential history is a vacuum solution. (c) In Einstein-Gauss-Bonnet gravity ($\alpha_1 = 1$, $\alpha_3 = 0$) there is no vacuum exponential history where $k$ varies, and for constant $k = k_0 > 0$ ($\beta = 2$, any $A$) the vacuum histories are exactly those with $k_0 \neq A^2$, the tuned coupling $\alpha_2 = -1/(4H^2(A^2 - k_0))$ and a tuned $\Lambda$, fixed by the $x_4$ component of the vacuum equations at the history: a vacuum exists only for these tuned couplings.

**Proof.** (T1d) gives $T + T' = 0$, so the right-hand side of the field equations is zero, and (a), (b) and (c) are the vacuum statements of `Revision/field_equations_a4` (records below). QED.

| statement | Wolfram records | sympy records |
| --- | --- | --- |
| (a) | `einstein_flat_vacuum`, `einstein_no_exponential_vacuum` | `einstein_flat_vacuum`, `einstein_no_exponential_vacuum` |
| (b) | `author_weights_no_exponential_vacuum` | `author_weights_no_exponential_vacuum` |
| (c) | `egb_exponential_vacuum_branches` | `egb_exponential_vacuum_branches`, `egb_no_vacuum_where_k_varies` |

Consequence (exact, under (i) to (iii)): a T1 pair cannot by itself be the source of any exponential history in Einstein gravity or with the author's weights, in particular not of the background history of `Revision/SPEC.md` section 1, which needs a source that grows with $x_4$; in Einstein gravity it is compatible with the flat member of the family. Histories that are not exponential are not decided. This is a statement about sources in one common geometry; it is not a derivation that such a geometry, or such a pair, is created. For a T2 pair the sources do not cancel: the mirror partner carries the pulled-back energy-momentum tensor $R_0TR_0$ of the $(-m,\lambda)$ configuration. For two independently quantised universes C1 does not apply (Q3).

## 8. Theorem T3: the Kohn-Sham level (dirac16complex)

`Revision/SPEC.md` section 9 asks for T3: at the Kohn-Sham level, the block map with the transformed boundary conditions maps the instantaneous Kohn-Sham problem with $(m,\lambda)$ to the one with $(-m,+\lambda)$ with equal energies. It is proved by two independent exact verifiers in `Revision/pairing/kohn_sham/` (theorem record `Revision/pairing/kohn_sham/t3-theory.json`).

### 8.1 Hypotheses

- (H3.1) The problem: the instantaneous Kohn-Sham problem of `Revision/kohn_sham/ks-theory.json` at a fixed slice $a_{4,0} = a_4(x_4)$, $b_{4,0} = b_4(x_4)$ of the corrected metric ($a_4$ and $b_4$ enter the block Hamiltonians only through the hidden scale $f = e^{-a_4}b_4^{1/2}$ and $\kappa = e^{-a_4}$, positive constants on a slice, and the proper densities through the cell volume): good sector (no extra-time momentum), a lattice of 3-space momenta $k$, and in each of the eight $2 \times 2$ blocks the Hamiltonian $h_j = j[-(i/f)\sigma_1\,d/dy + M_{\mathrm{eff}}(y)\sigma_2 + \kappa k\sigma_3] + v_v(y)$ on $y \in [-L, 0]$ ($j = \pm1$; four blocks $(s_2, s_3)$ per $j$; $y = \ln|\sin z|/(6H)$, the fold $\cos z = 0$ at $y = 0$, the tip at $y = -L$).
- (H3.2) The functional: Hartree plus the exact uniform-gas exchange, $M_{\mathrm{eff}} = m + \frac{15}{16}\lambda S$, $v_v = -\lambda n/16$, $e_{\mathrm{int}} = \frac{15}{32}\lambda S^2 - \frac{1}{32}\lambda n^2$, no correlation; the energy-momentum tensor of that record.
- (H3.3) The fold (both fold conditions filled, ASSUMED): the fold $\cos z = 0$ joins the two halves of a cell, a spinor continuous across it has the same $\chi(y)$ on both halves (no mirror copy), and both fold conditions, $\chi_2(0) = 0$ and $\chi_1(0) = 0$, are solved and filled together with the weight $\frac12$.
- (H3.4) The tip (chosen): $(1 - Q(\theta))\chi(-L) = 0$ with $Q(\theta) = \cos\theta\,\sigma_3 + \sin\theta\,\sigma_2$.
- (H3.5) Mermin occupations at fixed particle number $N$ and temperature $T$, with the filling convention of the Kohn-Sham record (positive branch of the $\lambda = 0$ problem plus the $k = 0$ zero modes, followed continuously in $\lambda$).
- (H3.6) The same $H$, $L$, $a_{4,0}$, $b_{4,0}$, lattice, extra-time volume, $N$ and $T$ for both members; quasi-free (mean-field) states.

### 8.2 Statement

For every self-consistent Kohn-Sham state with $(m,\lambda,\theta)$, the map $(\chi, j) \to (\sigma_2\chi, -j)$ at the same $k$, which is the chirality $\Gamma$ of the 16-component orbital in the block basis (up to the phase $s_2$ per block), with the two fold conditions exchanged, gives a self-consistent Kohn-Sham state with $(-m,+\lambda,\pi-\theta)$, and conversely (the map is an involution). The two states have the same levels with their degeneracies, the same occupations, chemical potential, particle number and entropy, EQUAL Kohn-Sham energy $E_{KS}$, grand potential and free energy, and equal energy-momentum profiles $\rho(y)$, $p_3(y)$, $p_t(y)$, $p_0(y)$; the densities transform as $n \to n$, $S \to -S$, $Q \to -Q$, so $M_{\mathrm{eff}} \to -M_{\mathrm{eff}}$ and $v_v \to v_v$. With the untransformed tip angle the spectra differ. (These are the statements S1 to S4 of the theorem record. The statement of the earlier record that a mirror copy inside a Z2 orbifold carries $(-m,+\lambda)$ belonged to the withdrawn metric of 2026-10-14 and is not a statement of the corrected metric, which has no orbifold.)

### 8.3 Proof

1. $\sigma_2h_j(M,k,v)\sigma_2 = h_{-j}(-M,k,v)$ as differential operators for every hidden scale $f$, and for the shooting form $\chi' = fN\chi$, $N = M\sigma_3 - \kappa k\sigma_2 + ij(\varepsilon - v)\sigma_1$: $\sigma_2N_j(M)\sigma_2 = N_{-j}(-M)$. So $\sigma_2\chi$ is an eigen-orbital of block $-j$ with $-M$ at the same level $\varepsilon$.
2. $\sigma_2Q(\theta)\sigma_2 = Q(\pi - \theta)$ and $\sigma_2(1 - \sigma_3)\sigma_2 = 1 + \sigma_3$: the tip condition goes into the one with $\pi - \theta$ (the canonical $\theta = 0$ into $\theta = \pi$) and the two fold conditions are exchanged; the boundary current $-ij\,\phi^\dagger\sigma_1\chi$ and the norm are invariant, so the image problem is self-adjoint with the same normalisation.
3. Per orbital, $n_o$ and $t_o$ are invariant and $s_o$, $q_o$ change sign; hence $n(y)$ is unchanged and $S(y)$ changes sign. $M_{\mathrm{eff}}[-m,+\lambda,-S] = -M_{\mathrm{eff}}[m,\lambda,S]$, $v_v$ and $e_{\mathrm{int}}$ are even in $S$: the self-consistency loop commutes with the map exactly for $(-m,+\lambda)$ (not for $(-m,-\lambda)$).
4. The map is a bijection between the eigen-orbitals of the two problems with equal levels (both $j$ and both fold conditions belong to each problem), so occupations, $\mu$, $N$ and entropy agree; every term of $E_{KS}$, $\Omega$, $F$ and of the energy-momentum profiles is a sum of invariant densities, or contains the product $M_{\mathrm{eff}}s_o$ of two odd factors, plus the even $e_{\mathrm{int}}$. QED.

Independent confirmations inside the same records: for $k = 0$, $v = 0$ and constant $M$ the characteristic functions of $(M, j, \theta = 0)$ and $(-M, -j, \theta = \pi)$ agree fold condition by fold condition, so the two spectra are equal level by level, while the untransformed tip gives a different characteristic function; the $2 \times 2$ map is the 16-component $\Gamma$ in the block basis $V$ of the Kohn-Sham record.

| step | Wolfram records | sympy records |
| --- | --- | --- |
| 1 | `T3_block_hamiltonian_map`, `T3_ode_map` | `T3.block_hamiltonian_map`, `T3.ode_map` |
| 2 | `T3_tip_condition_map`, `T3_fold_conditions_exchanged` | `T3.tip_condition_map`, `T3.fold_conditions_exchanged` |
| 3 | `T3_orbital_densities`, `T3_mean_field_map` | `T3.orbital_densities`, `T3.mean_field_map` |
| 4 | `T3_energies_and_emt_profiles_equal` | `T3.energies_and_emt_profiles_equal` |
| confirmations | `T3_exact_k0_spectra`, `T3_Gamma_is_the_block_map` | `T3.exact_k0_spectra`, `T3.Gamma_is_the_block_map` |
| comparison with the theorem record, numerical confirmation | | `compare.t3_theory.theorem`, `compare.t3_theory.not_established`, `T3.rust_selftest_numerical_confirmation` |

@@KS_THEORY_INGREDIENTS@@

### 8.4 Numerical confirmation and interpretation

A numerical self-test of the Rust solver, labelled in its report as NOT a proof of T3: $(m, \lambda, \text{tip } \theta = 0)$ and $(-m, \lambda, \text{tip } \theta = \pi)$, solved independently, give the same sorted levels, occupations, Kohn-Sham energies and energy-momentum integrals and opposite $S$ (worst deviation 3.62e-13, tolerance 1e-9). For $N = 8$, $\lambda = 157.7$ and $a_{4,0} = 1$: $E_{KS}$ = -1.457144423225e-2 in both runs (140 levels), while the negative control with the untransformed tip $b(-L) = 0$ gives $E_{KS}$ = -1.7604533053e0. For $N = 592$, $\lambda = 2.131$ and $a_{4,0} = 1$: $E_{KS}$ = 1.317651779781e2 in both runs (324 levels), negative control -8.1980434559e-1. The couplings are the solvers' $\hat\lambda$ and the units are those of `Revision/kohn_sham/ks-theory.json`.

Interpretation (labelled, not a theorem): in its parameters the Kohn-Sham-level map is of the T2 type, $(m,\lambda) \to (-m,+\lambda)$ at equal energies, not of the T1 type, although its 16-component matrix is the chirality $\Gamma$ of T1: the Kohn-Sham expectation values are taken with the fixed Krein metric $B$ of the canonical quantisation, under which $\Gamma$ flips the sign ($\Gamma B\Gamma = -B$, statement Q1), so $S \to -S$ at the Kohn-Sham level while $S[\Gamma\Psi] = S[\Psi]$ for the classical bilinear.

@@KS_SOURCE_PARAGRAPH@@

### 8.5 Completion of T3 (2026-10-08)

An adversarial verification of T3 (2026-10-08) re-ran both T3 verifiers, which reproduced the theorem record `t3-theory.json` and the two T3 reports byte for byte, and re-derived every step of the proof; no error was found in the statement or the proof. Three gaps were found. A completion closes them by exact computation in a separate record, `t3-completion.json`, written by the Wolfram verifier `verify_t3_completion.wls` and re-derived independently by the sympy checker `check_t3_completion.py` (all in the folder `Revision/pairing/kohn_sham`; the reports lie in its subfolder `reports/`); T3 and its statements S1 to S4 are unchanged.

1. At the adversarial verification the Kohn-Sham coefficients $15/16$, $-1/16$, $15/32$, $-1/32$ of (H3.2) were written into the T3 verifier instead of being read from the Kohn-Sham record, and one of its clauses about $v_v$ compared an expression with itself. The completion reads the potentials from `Revision/kohn_sham/ks-theory.json`, checks $M_{\mathrm{eff}} - m = \partial e_{\mathrm{int}}/\partial S$ and $v_v = \partial e_{\mathrm{int}}/\partial n$, and repeats the map of step 3 with them ($M_{\mathrm{eff}}[-m,+\lambda,-S] = -M_{\mathrm{eff}}[m,\lambda,S]$; with $(-m,-\lambda)$ it fails, the control). The T3 verifier itself was then fixed at the root (2026-10-08): it reads the coefficients from the Kohn-Sham record, and its check `T3_mean_field_map` compares $v_v$ as a function of $(m,\lambda,n,S)$ at the original and the image arguments.
2. The filling convention (H3.5) was used for the $-m$ member without showing that its particle set is the image of the $+m$ member's. The completion shows that the map sends the $\lambda = 0$ levels with $\varepsilon > 0$ onto those of the image problem, commutes with the continuation in $\lambda$, and takes the $k = 0$ fold zero mode $(e^{fMy}, 0)$ to the fold zero mode of the image in its own boundary conditions (the other fold condition, tip $\theta = \pi$); with the untransformed tip the image mode violates the tip condition (control). So the occupied set of the image is the image of the occupied set.
3. The proof covers the four diagonal energy-momentum components of the $2 \times 2$ reduction. Statement S6 extends it to the 16-component level: with the expectation rule $\rho = \sum f\,uu^\dagger B$ of the canonical quantisation and $\Gamma B\Gamma = -B$, the image state has $\rho' = -\Gamma\rho\Gamma$, so $n$ is unchanged, $S$ and $Q$ change sign, and every component of the 16-component energy-momentum tensor and of the current $J^a$ of the $(-m,+\lambda)$ image state equals that of the original state.

| gap | Wolfram records | sympy records |
| --- | --- | --- |
| 1 | `T3C_mean_field_coefficients_from_ks_theory` | `T3C.mean_field_coefficients_from_ks_theory` |
| 2 | `T3C_filling_convention_mapped` | `T3C.filling_convention_mapped` |
| 3 (S6) | `T3C_krein_rule_16_component` | `T3C.krein_rule_16_component` |
| T3 reports, the two demonstrations, comparison with the completion record | | `T3C.t3_reports_pass`, `T3C.rust_demo_numerical_demonstration`, `T3C.reference_demo_numerical_demonstration`, `compare.t3_completion` |

The numerical demonstrations (not part of the proof) solve, at slices of the prescribed background history $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$ (the Rust demonstration at $a_{4,0} = 0, 0.5, 1, 1.5, 2$, the reference demonstration at $a_{4,0} = 0, 1, 2$; $A = 1$, the extra times deflating as $e^{-a_4}b_4^{1/2} = b_4(0)^{1/2}e^{-a_4/3}$; the coupling $\hat\lambda$ of each state is held fixed while the cell volume $\mathrm{Vol}_7(a_{4,0}) = \ell^3v_te^{(5/3)a_{4,0}}$ grows), three members of each state: the $+m$ universe $(m,\lambda,\theta = 0)$, the $-m$ universe $(-m,+\lambda,\theta = \pi)$ and a control.

@@DEMOS@@

What the completion does not establish: the same limits as T3 (section 8.4); in addition the filling convention remains a CONVENTION whose justification is open, the demonstrations show the equalities only on the states solved and to their stated tolerances, and S6 is an equality of expectation values in Kohn-Sham (quasi-free) states with the fixed Krein metric $B$, not a statement about two independently quantised universes (the list of what is not established in the completion record).

## 9. Verification records

### 9.1 Reports and their counts

Every check has a name, a verdict and a detail. Counts at the time of writing (the publication test re-reads them):

@@COUNT_TABLE@@

The pairing theorems are verified in four gravitational fields: the corrected metric on the patch $z \in (0,\pi/2)$ (primordial); the same metric on the other half $z \in (\pi/2,\pi)$ of the cell (mirror patch); a general diagonal (4,4) field $e^a{}_\mu = h_a(x_0,\dots,x_7)\delta^a_\mu$ with eight arbitrary functions of all eight coordinates (diagonal8); and a general non-diagonal field at one point (pointwise), with exact rational $e^a{}_\mu$ and $\partial_\rho e^a{}_\mu$, $\det e = 1411/6561$, a non-diagonal metric and 448 of the 512 connection components nonzero; plus the linearity (kernel) argument that covers every field. The canonical connection of each test field satisfies the vielbein postulate exactly. The Wolfram side and the sympy side share no code; the sympy side re-builds the gammas from the author's tau formulas and compares them entry by entry with `Revision/algebra/gammas.json`.

### 9.2 Checks per theorem

The tables below list all @@NW@@ checks of the Wolfram pairing report and all @@NP@@ checks of the sympy pairing report (section 9.1), grouped by theorem; every one has the verdict PASS (the checks of T3 are listed in section 8.3). Among the common sympy checks, the three comparison checks for T1, T2 and Q record that the sympy side confirms each Wolfram theorem independently, and the comparison check for the limits records that the two independently written lists of what the theorems do not establish cover the same topics; section 11.2 merges them.

@@CHECK_TABLES@@

### 9.3 Re-verification for this document

For the first edition (2026-10-01) both pairing verifiers were re-run on a copy of the working tree: 99 of 99 and 64 of 64 checks passed and the outputs were byte-identical to the recorded files. After the review of the same day the pairing verifiers were extended (the Krein inertia of every real-frequency eigenspace, the Krein-neutral imaginary-frequency eigenspaces). On 2026-10-14 the record moved to the author's coordinates $x_0, \dots, x_7$, which it keeps, and on 2026-10-16 to the metric of 2026-10-14 with $b_4(x_4)$; the metrics of all these editions are withdrawn (section 9.4), and their runs are recorded in the git history of this document and in the provenance files of the pairing record.

@@RUNS@@

### 9.4 The corrected metric of 2026-10-16

On 2026-10-16 the primordial metric was corrected (version 2; `Revision/SPEC.md` section 1, `Revision/metric_warped/`): $g_{00} = e^{-2a_4}b_4\cot^2 z$, $g_{ii} = e^{2a_4}$, $g_{44} = -1$, $g_{tt} = -e^{-2a_4}b_4(\sin^2 z)^{1/6}$, with $z = 6Hx_0$ real; the earlier metric of 2026-10-14 (with the factors $\sin^{1/3}z$ in 3-space and the extra times and $g_{00} = \cot^2 z$) and the version 1 of 2026-10-16 are withdrawn. The pairing record was recomputed for it on 2026-10-17 (phase W6 of `HANDOFF.md`):

1. T1, T2 and Q: the pairing verifiers build the primordial field and the other half of the cell with the corrected vielbein and $\sqrt{|g|} = e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}$, $a_4$ and $b_4$ arbitrary functions of $x_4$, and check that the spin connection contains $b_4'$ (`primordial_connection_depends_on_b4`, `geometry.connection_depends_on_b4`), so every T1, T2 and Q check in these fields is made with $b_4$ not constant. The general-field checks (the linearity argument, the diagonal field with eight arbitrary functions, the pointwise field) cover every metric anyway. The reflection $x_0 \to \pi/(6H) - x_0$ across the fold is an isometry of the corrected metric for every $a_4$, $b_4$ (`T2_mirror_is_isometry`, `geometry.mirror_isometry`); the corrected metric has no Z2 orbifold, and the sympy check of the degenerate surface is now named for the fold (`geometry.fold_degenerate`).
2. T3: the Kohn-Sham record of the corrected metric enters the block Hamiltonians through the hidden scale $f$ and $\kappa = e^{-a_4}$ (both constant on a slice), and the map holds for every $f$; its fold conditions are exchanged by the map (`T3_fold_conditions_exchanged`, `T3.fold_conditions_exchanged`). The statement S5 and the check of the mirror copy carrying $(-m,+\lambda)$ belonged to the Z2 orbifold of the withdrawn metric and were removed (9 Wolfram and 12 sympy checks, before 10 and 13); T3 itself, the map $(m,\lambda,\theta) \to (-m,+\lambda,\pi - \theta)$, holds in the same form.
3. Corollary C1 (section 7) is stated for the corrected metric, whose flat member is a vacuum solution in Einstein gravity.

The answer of section 11.3 is unchanged. The correction of the metric adds no creation process: nothing about the creation of universes, in pairs or otherwise, is proved in the corrected metric either.

## 10. Reproduction

From the repository root (the Wolfram field-theory verifier runs in six parts and a merge, in this order, and the sympy field-theory checker runs its part `--part nonlinear` before the full run, as in section 16 of `Revision/docs/DIRAC16COMPLEX_FIELD_THEORY`; the sympy pairing checker reads the Wolfram theory record for its final comparison, so the Wolfram verifier runs first; the Kohn-Sham theory checker reads the record written by the Kohn-Sham source-conditions checker, so that one runs before it, and so does the analysis of the $a_4$ equations with the Kohn-Sham source, which re-derives that record; the T3 completion runs after the T3 verifiers: the Wolfram completion verifier first, then the Rust demonstration (it needs the built Rust solver; four parts and the assembly, each below the limit of 423 s for one run), then the reference demonstration (it compares its $-m$ universe with the Rust table; six parts and the assembly, each below the same limit), and the sympy completion checker last (it reads the completion record and both demonstration reports); `<target>` is the cargo target folder and `<scratch1>` and `<scratch2>` are two empty working folders; a line ending in a backslash continues on the next, indented line (the line continuation of a POSIX shell)):

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
wolframscript -file Revision/theory/wolfram/verify_scope.wls
python Revision/theory/python/check_scope.py
wolframscript -file Revision/pairing/wolfram/verify_pairing.wls
python Revision/pairing/python/check_pairing.py
wolframscript -file Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls
python Revision/field_equations_a4/python/check_field_equations_a4.py
wolframscript -file Revision/kohn_sham/theory/verify_ks_theory.wls
python Revision/field_equations_a4/python/check_ks_source_conditions.py
python Revision/field_equations_a4/ks_source/ks_source_a4.py
python Revision/kohn_sham/theory/check_ks_theory.py
wolframscript -file Revision/pairing/kohn_sham/wolfram/verify_t3.wls
python Revision/pairing/kohn_sham/python/check_t3.py
wolframscript -file Revision/pairing/kohn_sham/wolfram/verify_t3_completion.wls
cargo build --release --manifest-path Revision/kohn_sham/solver/Cargo.toml
python Revision/pairing/kohn_sham/numerics/t3_rust_demo.py \
    --solver <target>/release/revision_ks_solver --work <scratch1> --jobs 10 --part 1/4
python Revision/pairing/kohn_sham/numerics/t3_rust_demo.py \
    --solver <target>/release/revision_ks_solver --work <scratch1> --jobs 10 --part 2/4
python Revision/pairing/kohn_sham/numerics/t3_rust_demo.py \
    --solver <target>/release/revision_ks_solver --work <scratch1> --jobs 10 --part 3/4
python Revision/pairing/kohn_sham/numerics/t3_rust_demo.py \
    --solver <target>/release/revision_ks_solver --work <scratch1> --jobs 10 --part 4/4
python Revision/pairing/kohn_sham/numerics/t3_rust_demo.py \
    --solver <target>/release/revision_ks_solver --work <scratch1> --jobs 10 --reuse
python Revision/pairing/kohn_sham/numerics/t3_reference_demo.py \
    --jobs 22 --work <scratch2> --part 1/6
python Revision/pairing/kohn_sham/numerics/t3_reference_demo.py \
    --jobs 22 --work <scratch2> --part 2/6
python Revision/pairing/kohn_sham/numerics/t3_reference_demo.py \
    --jobs 22 --work <scratch2> --part 3/6
python Revision/pairing/kohn_sham/numerics/t3_reference_demo.py \
    --jobs 22 --work <scratch2> --part 4/6
python Revision/pairing/kohn_sham/numerics/t3_reference_demo.py \
    --jobs 22 --work <scratch2> --part 5/6
python Revision/pairing/kohn_sham/numerics/t3_reference_demo.py \
    --jobs 22 --work <scratch2> --part 6/6
python Revision/pairing/kohn_sham/numerics/t3_reference_demo.py \
    --jobs 22 --work <scratch2> --reuse
python Revision/pairing/kohn_sham/python/check_t3_completion.py
python scripts/build_provenance_pdf.py Revision/docs/PAIR_CREATION_PROOFS.md \
    --developer-layout --specifications Revision/pdf-specifications.json
python -m unittest Revision/tests/test_pair_creation_proofs_publication.py -v
```

The PDF build runs the Markdown-to-LaTeX builder twice (with different hash seeds), runs pdflatex three times into each of two fresh directories, requires warning-free logs and byte-identical PDFs, and checks the PDF against its entry `pair-creation-proofs` in `Revision/pdf-specifications.json` (the Revision registry; the registry of the earlier stages is not touched).

## 11. What is proved and what is not

### 11.1 Proved

Exactly, for both fields (dirac16complex with Grassmann components, dirac16complex00 with commuting components) unless stated, under the hypotheses stated with each result:

1. T1 (section 4): $\mathcal{L}_{m,\lambda}[\Gamma\Psi] = -\mathcal{L}_{-m,-\lambda}[\Psi]$; the solutions of the $(m,\lambda)$ theory and of the $(-m,-\lambda)$ theory correspond one to one; $T \to -T$ and $J \to -J$; the pair has zero total energy-momentum, current and charge as classical bilinears; in every gravitational field taken as a fixed background.
2. T2 (section 5): $\Gamma$ combined with a Pin(4,4) reflection of character $-1$ gives $\mathcal{L}_{m,\lambda}[\gamma^n\Psi; R_ne] = +\mathcal{L}_{-m,\lambda}[\Psi; e]$; in the primordial field the isometry across the fold $z = \pi/2$ pairs a $(-m,\lambda)$ solution on one half of a cell with an $(m,\lambda)$ solution on the other half at EQUAL energy-momentum and charge.
3. Q (section 6, dirac16complex only): the chirality image carries the Krein metric $-B$ and is the same quantum system re-labelled; an independently quantised $(-m,-\lambda)$ universe carries $+B$ and cannot be identified with it; the generators of two independent universes add without cancelling; the $+m$ and $-m$ one-particle ($\lambda = 0$) spectra are identical (flat space, or frozen coefficients at a point); the T2 image keeps $+B$.
4. C1 (section 7): a T1 pair as the complete classical source of the metric is a zero source; then no exponential history, in particular not the background history, is a solution in Einstein gravity or with the author's weights (in Einstein gravity the flat member of the family is a vacuum solution).
5. T3 (section 8, dirac16complex): every self-consistent instantaneous Kohn-Sham state with $(m,\lambda,\theta)$ is mapped by the block map of $\Gamma$, with the two fold conditions exchanged and $\theta \to \pi - \theta$, onto a self-consistent Kohn-Sham state with $(-m,+\lambda,\pi-\theta)$ with equal levels, occupations, Kohn-Sham energy and energy-momentum profiles, and $S \to -S$ (both fold conditions filled, ASSUMED); with the completion (section 8.5), at the 16-component level with the expectation rule of the canonical quantisation, every component of the energy-momentum tensor and of the current is unchanged and $S$, $Q$ change sign (S6), and the filling convention of the $+m$ member is carried onto the $-m$ member.

### 11.2 Not established

1. No creation process: the theorems map solutions to solutions and quantities to quantities; nothing in these equations produces a universe, a pair of universes or a change of the number of universes, and no transition between “no universe” and “two universes”, no initial state, no vacuum decay and no tunnelling process is derived.
2. No rate, probability or amplitude: no transition amplitude, probability, cross-section, rate or Bogoliubov coefficient for creating universes of masses $\{+m, -m\}$ is computed or implied; no wave function of the universe and no path integral is part of these theorems.
3. No dynamical necessity: no equation and no conservation law forces the partner to exist; a single universe with mass $+m$ is an equally valid solution without its partner. T1 and T2 are correspondences between solutions of two parameter sets, not a mechanism.
4. T1 is not a symmetry of a single theory: it changes the parameters and the sign of the action, and for $\lambda \neq 0$ it pairs $(m,\lambda)$ with $(-m,-\lambda)$, not $+m$ with $-m$ at fixed coupling. The pure pairing $(m,\lambda) \to (-m,\lambda)$ is T2, at equal, not opposite, energy-momentum: T2 does not reverse the sign of $T$.
5. The vanishing total energy-momentum and charge of a T1 pair holds for classical bilinears and as an operator identity within ONE quantum system; it does not hold for two independently quantised universes, whose generators add without cancelling.
6. Test-field statement: the gravitational field is fixed and the same for both members. The back-reaction through the field equations for $a_4$ and $b_4$ is not part of the theorems; corollary C1 is the only statement about it, and it concerns the sum of classical sources in one common geometry.
7. The fold: T2 relates the two halves of a cell through the isometry $z \to \pi - z$ across the fold $z = \pi/2$; the corrected metric has no Z2 orbifold, the metric is degenerate at the fold ($g_{00} = 0$ and $\sqrt{|g|} = 0$), and no junction condition or matching of the field across the fold is derived.
8. Quantum positivity: in flat 4+4 space every real-frequency eigenspace of the one-particle Hamiltonian has Krein inertia (4,4) (proved, section 6.3), and the eigenspaces of imaginary or zero frequency are Krein-neutral; a positive-norm Fock space for either universe is not established by these theorems (the good-sector construction of the theory record is a separate result, made only for single good-sector momenta with frozen coefficients and not used here; section 6.3).
9. dirac16complex00 is a classical field: no quantum statement is made for it.
10. The Kohn-Sham level T3 holds for the instantaneous (adiabatic) mean-field Kohn-Sham states only, with both fold conditions filled (ASSUMED) and the transformed tip condition; the time-dependent Kohn-Sham problem is open, no correlation is included, and T3 says nothing about back-reaction (section 8); the history $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$ of the numerical demonstrations is a prescribed background, the filling of the Kohn-Sham states is a CONVENTION, and the demonstrations of section 8.5 are numerical, not proofs.

### 11.3 The answer to the request

The request “PROVE that Universes of masses {+mass, -mass} are created in pairs” is answered exactly as follows, for dirac16complex and for dirac16complex00. Proved: to every solution with mass $m$ the explicit maps $\Gamma$ (T1: with $\lambda \to -\lambda$, opposite energy-momentum and charge, in every gravitational field) and $\gamma^0$ with the isometry across the fold (T2: same $\lambda$, equal energy-momentum, between the two halves of a cell of the primordial gravitational field) assign a solution with mass $-m$; for dirac16complex, at the Kohn-Sham level, the block map of $\Gamma$ with the transformed boundary conditions assigns to every self-consistent instantaneous Kohn-Sham state with $(m,\lambda)$ one with $(-m,+\lambda)$ at equal energies (T3, both fold conditions filled, ASSUMED). That universes occur in pairs is not proved: these are maps between the solutions of two parameter sets, and a single universe with mass $+m$ is an equally valid solution without its partner. At the quantum level of dirac16complex the chirality partner is the same quantum system with the Krein metric $-B$, and two independently quantised universes of masses $+m$ and $-m$ have identical one-particle ($\lambda = 0$) spectra (flat space, or frozen coefficients at a point) and no cancelling generators. Not proved: that such universes are CREATED, in pairs or otherwise. No creation process, rate or amplitude follows from these equations.
