# Kohn-Sham model of dirac16complex in the author's primordial field with the deflating extra times

## The block reduction, the instantaneous ground and first excited states along the prescribed history $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$, Mermin thermodynamics, adiabaticity, the energy-momentum tensor, the rescaling partners and the source conditions, with the verification records and an exact statement of what is computed and what is not

## Abstract

This document records the Kohn-Sham (density-functional) model of the fermion field dirac16complex in the author's primordial gravitational field, deliverable 4 of `Revision/SPEC.md` section 10, as computed by the code in `Revision/kohn_sham/`, in the author's metric with the function $b_4(x_4)$ in the three extra-time components ($b_4$ is never 1; since 2026-10-16). Exact (two independent verifiers, WolframScript and sympy): in the good sector (no extra-time momentum) the ansatz $\Psi = e^{ik\cdot x}W^{-3}b_4^{-3/4}\chi(y,x_4)$ removes the spin-connection terms $3H\gamma^0$ and $\frac34(b_4'/b_4)\gamma^4$ and reduces the 16-component equation, for every history $a_4(x_4)$, $b_4(x_4)$, to eight $2 \times 2$ blocks $h_j = j[-i\sigma_1\,d/dy + M_{\mathrm{eff}}\sigma_2 + \kappa k\sigma_3] + v_v$ in the hidden coordinate $y$, with $\kappa = e^{-Hy-a_4}$; $b_4$ does not enter $h_j$; the deflation of the extra times enters the instantaneous problem only through this redshift of the 3-momenta and through the proper cell volume, which grows like $b_4^{3/2}$; the exact local exchange of the uniform good-sector gas gives $M_{\mathrm{eff}} = m + \frac{15}{16}\lambda S$ and $v_v = -\lambda n/16$. Computed (a Rust solver, an independent Python reference with a different discretisation, and a cross-check of the full canonical matrix, 31 of 31 checks PASS over 162731 comparisons): the instantaneous ground and first excited states of 75 parameter sets ($N = 8, 136, 688$; five couplings $\hat\lambda$, held fixed while the cell grows, so that the effective coupling falls like $e^{-2a_{4,0}}$; five slices $a_{4,0}$ of the prescribed history $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$, $A = 1$), 135 Mermin states at three temperatures, the adiabaticity measure ($Q_{\max} \leq 0.0935336$ over the matrix), the Fermi-level crossings (none in the canonical matrix; a demonstration at $N = 696$), the energy-momentum tensor profiles, the exact rescaling partners and the exact-exchange variant. ASSUMED or chosen: the Z2 brane at the patch end, the regular tip at $y = -3$, the filling convention. Measured afterwards (`Revision/kohn_sham/tip_convergence/`, $L = 3$ to $6$, 7 of 7 checks PASS): the free results converge as the tip cutoff $L$ grows and the recorded $L = 3$ values of $E_{KS}$ lie within 1.4% of the large-$L$ values, except $N = 688$ at $a_{4,0} = 0$, which changes its occupied set from $L = 3.5$ on and does not converge up to $L = 6$; the interaction energy of the brane zero modes depends strongly on $L$ (the recorded $N = 8$ value is about one third of the large-$L$ value at $a_{4,0} = 0$ and about 1/22 of it at $a_{4,0} = 2$), and for 6 of the 19 interacting states studied (self-consistent iteration failing at larger $L$ before the differences settle) the limit $L \to \infty$ of $E_{KS}$ is not established. Not admissible as sources: no recorded Kohn-Sham state satisfies the source conditions of the $a_4$ and $b_4$ equations, so the history is a prescribed background without back-reaction. Not done: the time-dependent (non-adiabatic) Kohn-Sham problem, correlation beyond exchange, back-reaction.

## 1. The task and the answer

The author asked (2026-10-01, quoted from `Revision/README.md`): “plan and employ a DFT-motivated approximation similar to the one that you already created [...], with a Kohn-Sham fermion-gas thermodynamic effective potential, that employs the DFT ground and first-excited-state computation”. `Revision/SPEC.md` section 7 makes this precise: a Kohn-Sham fermion-gas model of dirac16complex in the good sector with the contact interaction $U = \frac{\lambda}{2}S^2$, the Hartree mean field plus the exact local exchange of the uniform gas, Mermin's finite-temperature functional, the reduction to $2 \times 2$ blocks in the hidden coordinate, the boundary conditions, the ground and first excited states, the thermodynamics, and, because $a_4$ and $b_4$ depend on $x_4$, the INSTANTANEOUS (adiabatic) Kohn-Sham states along the history with the extra times deflating, with an adiabaticity measure.

The answer of this record:

1. Exact (section 3, section 4): the block reduction, the exchange functional, the boundary conditions, the rescaling identity, the energy-momentum tensor and its conservation laws, the adiabaticity measure, all for the metric with $b_4(x_4)$. Every formula is in `Revision/kohn_sham/ks-theory.json` and verified twice, in `Revision/kohn_sham/reports/ks-theory-wolfram.json` (51 of 51 PASS) and independently in `Revision/kohn_sham/reports/ks-theory-python.json` (63 of 63 PASS).
2. Computed (sections 5 to 10): the instantaneous Kohn-Sham states of the canonical matrix by the Rust solver, independently by the Python reference, and compared state by state on the full matrix.
3. Not admissible (section 11): the recorded states are not sources of the field equations for $a_4$ and $b_4$; the history $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$ is PRESCRIBED.
4. Open (section 15): the time-dependent Kohn-Sham problem, correlation, back-reaction.

Every number below is read from the named Revision report or results file (the publication test re-reads them); units: $H = m = 1$, energies, momenta and temperatures in units of $m$, as in `Revision/kohn_sham/results/parameters.json`. Interpretations are labelled.

## 2. Setting: the author's field, the good sector and the hidden coordinate

The coordinates are the author's, $x_0, x_1, \dots, x_7$, in the author's order: $x_0$ is the hidden space direction, $z = 6Hx_0 \in (0,\pi/2)$; $x_1, x_2, x_3$ are ordinary 3-space, inflating with the scale factor $e^{a_4}\sin^{1/6}z$; $x_4$ is the time; $x_5, x_6, x_7$ are the three extra times, which DEFLATE exponentially, with the scale factor $e^{-a_4}b_4^{1/2}\sin^{1/6}z$ and $a_4$ increasing (they are never treated as static). (Until 2026-10-14 this record named them $x_1, \dots, x_8$, with the hidden direction $x_8$ listed last; the user ordered the author's coordinates on 2026-10-14.) The metric of `Revision/SPEC.md` section 1, as changed by the author on 2026-10-14 ($g_{55} = g_{66} = g_{77} = -e^{-2a_4(x_4)}\,b_4(x_4)\sin^{1/3}(6Hx_0)$; `Revision/metric_b4/METRIC_CHANGE_PROVENANCE.md`), is

$$
\begin{aligned}
ds^2 = {} & \cot^2 z\,dx_0^2 + e^{2a_4(x_4)}\sin^{1/3}z\,\big(dx_1^2+dx_2^2+dx_3^2\big) - dx_4^2 \\
& - e^{-2a_4(x_4)}\,b_4(x_4)\sin^{1/3}z\,\big(dx_5^2+dx_6^2+dx_7^2\big) ;
\end{aligned}
$$

$b_4(x_4) > 0$ is a function of the time and never 1 ($b_4 = 1$ is the withdrawn metric of the earlier version of this record). The history of this record is

$$
a_4 = AHx_4,\qquad b_4 = b_4(0)\,e^{\beta AHx_4},\qquad A = 1,\quad \beta = \tfrac43 ,
$$

PRESCRIBED, not solved for: with the author's Lovelock weights the mixed $x_4$-$x_0$ equation of a source without a $T^{x_4}{}_{x_0}$ component allows on $a_4 = Hx_4$ exactly $d\ln b_4/da_4 \in \{0, \frac43\}$, and $b_4$ is not constant (`ks-theory.json`, key adiabaticity.historyBetaSource; section 11). On it the extra-time scale factor is $b_4(0)^{1/2}e^{-AHx_4/3}\sin^{1/6}z$.

The Kohn-Sham record uses the hidden coordinate $y = \ln(\sin z)/(6H) \in (-\infty, 0]$, with $dy = \cot z\,dx_0$; the patch end $z = \pi/2$ is $y = 0$ (the brane) and the tip $z \to 0$ is $y \to -\infty$. In it the metric is exactly

$$
ds^2 = e^{2Hy}\big[e^{2a_4}(dx_1^2+dx_2^2+dx_3^2) - e^{-2a_4}b_4(dx_5^2+dx_6^2+dx_7^2)\big] - dx_4^2 + dy^2 ,
$$

with the warp $W = e^{Hy}$ and $\sqrt{|g|} = b_4^{3/2}e^{6Hy}$ ($= b_4^{3/2}\cos z$ in the author's chart). The 7-volume does not depend on $a_4$ (the inflation $e^{3a_4}$ of 3-space is compensated exactly by the factor $e^{-3a_4}$ of the extra times), but it grows like $b_4^{3/2}$, on the history like $b_4(0)^{3/2}e^{2a_4}$. The canonical spin connection gives $\gamma^\mu\Omega_\mu = 3H\gamma^0 + \frac34(b_4'/b_4)\gamma^4$ for every $a_4(x_4)$, $b_4(x_4)$: the $a_4'$ pieces of the three inflating directions, $+\frac32a_4'\gamma^4$, and of the three deflating directions, $-\frac32a_4'\gamma^4$, cancel, and the $b_4'$ piece of the deflating directions remains.

The good sector: no dependence on $x_5, x_6, x_7$ (zero extra-time momenta), a coordinate 3-torus of side $\ell$ with the momenta $k \in \Delta k\,\mathbb{Z}^3$, $\Delta k = 2\pi/\ell$, and the extra-time coordinate volume $v_t$; the proper cell volume is $\ell^3v_tb_4^{3/2}$. With the ASSUMED brane condition and the chosen tip condition (section 5; together they kill the $y$-current and make the blocks $h_j$ self-adjoint) the good sector is quantised in the positive realisation of the canonical quantisation of `Revision/SPEC.md` section 6; the field-theory record `Revision/docs/DIRAC16COMPLEX_FIELD_THEORY` (its section 11) constructs that realisation explicitly only for single good-sector momenta with frozen coefficients, and without a boundary condition at $z = \pi/2$ the curved good sector has complex frequencies (for $U = 0$ whenever $m^2 < 9H^2$, which includes the parameters $m = H = 1$ used here). The expectation-value rule $\langle\Psi^\dagger M\Psi\rangle = \mathrm{Tr}(M\rho)$, $\rho = \sum_{\mathrm{occ}} f\,uu^\dagger B$, defines the quasi-free (Slater or Mermin) states used here.

| item | Wolfram records | sympy records |
| --- | --- | --- |
| gammas, $C$, $B$, $\Gamma$ | `fixture_input`, `clifford_relation`, `C_B_Gamma` | `fixture_input`, `fixture_python_equals_wolfram`, `clifford_relation`, `C_B_Gamma`, `BC_and_Cg4` |
| hidden coordinate, $\sqrt{\lvert g\rvert}$ | `geometry_hidden_coordinate`, `geometry_sqrt_det` | `geometry_hidden_coordinate`, `geometry_sqrt_det`, `geometry_warped_form` |
| spin connection | `spin_connection_compatibility`, `spin_connection_slash`, `spin_connection_time_terms`, `spin_connection_slash_x0_chart` | `spin_connection_compatibility`, `spin_connection_slash`, `spin_connection_time_terms`, `spin_connection_time_term_value`, `spin_connection_slash_x0_chart` |

### 2.1 The metric with $b_4(x_4)$ in the Kohn-Sham record

On 2026-10-14 the author changed the extra-time components to $g_{55} = g_{66} = g_{77} = -e^{-2a_4(x_4)}\,b_4(x_4)\sin^{1/3}(6Hx_0)$ (the change, its source cells and every verification are recorded in `Revision/metric_b4/METRIC_CHANGE_PROVENANCE.md`), and on 2026-10-15 the user ordered that everything be moved to $b_4(x_4)$, $b_4$ never 1. The Kohn-Sham record was moved on 2026-10-16:

1. The reduction (records `ansatz_removes_spin_connection`, `ansatz_without_b4_factor_term_survives`, `ansatz_norm_b4`): the factor $b_4^{-3/4}$ of the orbitals is the half-density factor of the volume element; it removes the term $\frac34(b_4'/b_4)\gamma^4$, $b_4$ does not appear in the reduced operator, and the Hilbert norm of the reduced problem is $\int\chi^\dagger\chi\,dy$ for every $a_4$ and $b_4$.
2. The densities (records `ks_coupling_volume_scaling`, `history_solver_units`): a proper density is the orbital sum divided by the proper cell volume $\ell^3v_tb_{4,0}^{3/2}$. The solvers use the coupling $\hat\lambda = \lambda\,b_4(0)^{-3/2}$ and the cell volume $\mathrm{Vol}_7(a_{4,0}) = \ell^3v_t\,e^{(3/2)\beta a_{4,0}}$ (the proper volume in units of $b_4(0)^{3/2}$), so $b_4(0)$ never needs a value. A Kohn-Sham state depends on the coupling and the cell volume only through their ratio: the slice state at $(\hat\lambda, \mathrm{Vol}_7(a_{4,0}))$ is the state of the coordinate cell $\ell^3v_t$ at the effective coupling $\hat\lambda\,e^{-(3/2)\beta a_{4,0}} = \hat\lambda\,e^{-2a_{4,0}}$.
3. The energy along the history (record `emt_energy_change_history`): $dE/da_4 = -3(P_3 - P_t) - \frac32\beta P_t$ with $P = 2\mathrm{Vol}_7(a_{4,0})\int e^{6Hy}p\,dy$ (section 9).

What changed in the numbers: with $\lambda = 0$ nothing (the levels, energies and integrals of the free states are those of the earlier record); for $\lambda \neq 0$ the couplings were recalibrated on the new history (section 5) and every interacting state with $N > 8$ or $a_{4,0} > 0$ changed. The earlier factorisation proof `Revision/kohn_sham/reports/ks-b4-wolfram.json` (records `K1_dirac_operator_b4_factorisation`, `K2_good_sector_independent_of_b4`, `K3_norm_and_volume`; its fourth record described the withdrawn background $b_4 = 1$) remains valid and is superseded by the record above.

## 3. The exact block reduction

**Ansatz.** $\Psi = e^{ik\cdot x}W^{-3}b_4^{-3/4}\chi(y,x_4)$ gives EXACTLY, for a time-dependent $a_4$ and $b_4$,

$$
\gamma^0\partial_y\chi + \gamma^4\partial_{x_4}\chi + i\kappa\,k\cdot\gamma\,\chi = (M_{\mathrm{eff}} - iv_v\gamma^4)\chi ,\qquad \kappa(y,x_4) = e^{-Hy-a_4(x_4)} ,
$$

i.e. $i\partial_{x_4}\chi = h(x_4)\chi$ with $h$ Hermitian in $\int dy\,\chi^\dagger\chi$. The factor $W^{-3}$ removes the term $3H\gamma^0$ and the factor $b_4^{-3/4}$ the term $\frac34(b_4'/b_4)\gamma^4$; without either the term survives. At a fixed instant the instantaneous (adiabatic) problem is $h(a_{4,0})\chi = \varepsilon\chi$ with $a_{4,0} = a_4(x_4)$; it does not contain $b_{4,0} = b_4(x_4)$.

**Blocks.** $J = \gamma^0\gamma^1\gamma^4$ ($J^2 = 1$), $K_1 = \gamma^2\gamma^3$ and $K_2 = \gamma^5\gamma^6$ ($K^2 = -1$) commute with each other and with $\gamma^0$, $\gamma^0\gamma^1$, $\gamma^0\gamma^4$, $B$ and $C$; their joint eigenspaces, labelled $(j, s_2, s_3)$ with $j, s_2, s_3 = \pm1$, are eight rank-2 blocks with an explicit unitary basis $V$ (entries of $2\sqrt2\,V$ in $\{0, \pm1, \pm i\}$). For $k$ along $x_1$ (the spinor rotation commutes with $\gamma^0$, $\gamma^4$, $B$, $C$, so the spectra depend on $|k|$ only), every block of type $j$ carries

$$
h_j = j\big[-i\sigma_1\,\tfrac{d}{dy} + M_{\mathrm{eff}}(y)\sigma_2 + \kappa(y)k\sigma_3\big] + v_v(y) ,
$$

equivalently $\chi' = N\chi$ with $N = M_{\mathrm{eff}}\sigma_3 - \kappa k\sigma_2 + ij(\varepsilon - v_v)\sigma_1$; in the real form $\chi = (a, ib)$, $a' = M_{\mathrm{eff}}a - (\kappa k + j(\varepsilon - v_v))b$ and $b' = (j(\varepsilon - v_v) - \kappa k)a - M_{\mathrm{eff}}b$. In the block basis $\gamma^0 = \sigma_3$, $B = js_2$ and $C = s_2\sigma_2$.

**Symmetries and degeneracies.** $h_{-1} - v = -(h_{+1} - v)$ and $\sigma_3h_j(k)\sigma_3 = h_{-j}(-k)$: the $(j,k)$ and $(-j,-k)$ orbitals are degenerate. On a lattice shell $|k|^2 = \Delta k^2n_2$ with $r_3(n_2)$ vectors every level of $h_j(|k|)$ is $4r_3(n_2)$-fold for each $j$; at $k = 0$ every level is 4-fold per $j$. The chirality $\Gamma$ maps block $(j, s_2, s_3)$ onto $(-j, s_2, s_3)$ with the $2 \times 2$ entry $s_2\sigma_2$, and $\sigma_2h_j(M,k)\sigma_2 = h_{-j}(-M,k)$ with the brane parities exchanged (the ingredient of T3, section 12).

**Where the deflation enters (exact).** $a_{4,0}$ enters $h_j$ only through $\kappa k = e^{-Hy}(ke^{-a_{4,0}})$: the 3-momenta redshift as $ke^{-a_4}$. Because the good sector has no extra-time momentum, the extra-time scale factor $e^{-a_4}b_4^{1/2}$ enters the instantaneous problem only through the proper cell volume, that is through the densities and the mean field (section 2.1 and section 10).

| item | Wolfram records | sympy records |
| --- | --- | --- |
| ansatz and Hamiltonian | `ansatz_removes_spin_connection`, `ansatz_without_W3_term_survives`, `ansatz_without_b4_factor_term_survives`, `ansatz_norm_b4`, `hamiltonian_16_hermitian` | `ansatz_removes_spin_connection`, `ansatz_without_W3_term_survives`, `ansatz_without_b4_factor_term_survives`, `ansatz_norm_b4`, `hamiltonian_16_hermitian` |
| blocks | `blocks_commuting_set`, `blocks_basis_unitary`, `blocks_forms`, `blocks_relation_to_Gamma`, `block_hamiltonian`, `block_ode_equivalent` | `blocks_commuting_set`, `blocks_projectors`, `blocks_basis_unitary`, `blocks_forms`, `blocks_not_everything_block_diagonal`, `blocks_relation_to_Gamma`, `block_hamiltonian`, `block_ode_equivalent` |
| symmetries | `block_type_relation`, `block_Gamma_map`, `rotation_invariance` | `block_type_relation`, `block_Gamma_map`, `rotation_invariance` |
| solver (numerical basis) | | `block_reduction_numeric`, `gamma_fixture_numeric` (Rust solver report) |

## 4. The functional: Hartree, exact uniform-gas exchange, Mermin

**Exchange (exact for the uniform gas).** The interaction is $U = \frac{\lambda}{2}S^2$, $S = \bar\Psi\Psi$, normal ordered ($\lambda > 0$ repulsive). For a quasi-free state, Wick's theorem gives $\langle :S^2: \rangle = (\mathrm{Tr}\,C\rho)^2 - \mathrm{Tr}(C\rho C\rho)$. For every $p \to -p$ symmetric occupation of the 8-fold good-sector gas, at every temperature, $\rho = (nB + SC)/16$ and

$$
e_H = \tfrac{\lambda}{2}S^2 ,\qquad e_x = -\tfrac{\lambda}{32}\big(n^2 + S^2\big) ,\qquad
e_{\mathrm{int}} = \tfrac{15}{32}\lambda S^2 - \tfrac{1}{32}\lambda n^2 ,
$$

$$
M_{\mathrm{eff}}(y) = m + \tfrac{15}{16}\lambda S(y) ,\qquad v_v(y) = -\tfrac{\lambda}{16}n(y) ,
$$

with proper densities; for one filled level at rest $E_x/E_H = -1/8$, and on shell $\langle\mathcal{L}\rangle/\sqrt{|g|} = e_{\mathrm{int}}$. In the solvers' units (section 2.1) the same formulas hold with $\lambda \to \hat\lambda$ and every density per $\mathrm{Vol}_7(a_{4,0})$. No correlation is included (Hartree plus exchange only). The Rust solver reads the coefficients from `ks-theory.json` and checks them (`theory_input_coefficients`: $M_{\mathrm{eff}} = m + 0.9375\lambda S$, $v_v = -0.0625\lambda n$).

**Exact Fock exchange of the slab (diagnostic and variant).** For closed shells the exact Fock exchange of the Kohn-Sham determinant is also local, $e_x^{\mathrm{exact}} = -\frac{\lambda}{32}(n^2 + S^2 - Q^2 - Y^2)$ with $Q = \langle\Psi^\dagger B\gamma^0\Psi\rangle$ and $Y = 0$; the canonical functional is the uniform-gas one, the difference $\Delta E_x = \frac{\lambda}{32}\,2\mathrm{Vol}_7\int e^{6Hy}Q^2\,dy$ is reported for every state, and the exact-Fock functional is solved as a variant (60 states, `Revision/kohn_sham/results/exx/exact-fock-variant.csv`).

**Densities, energy, Mermin.** Per orbital, with $P(y) = e^{-6Hy}/\mathrm{Vol}_7(a_{4,0})$: $n_o = P\chi^\dagger\chi$, $s_o = P\chi^\dagger j\sigma_2\chi$, $t_o = P\chi^\dagger j\sigma_3\chi$, $q_o = P\chi^\dagger\sigma_3\chi$. Totals are $\sum w\,g\,f$ times these, $g = 4r_3(n_2)$, $w = 1/2$ (section 5). The Kohn-Sham energy of the doubled system is $E_{KS} = \sum g f\varepsilon - 2\mathrm{Vol}_7\int_{-L}^{0}e^{6Hy}e_{\mathrm{int}}\,dy$; Mermin's occupations are $f = 1/(1 + e^{(\varepsilon-\mu)/T})$ with $\mu$ fixed by $\sum g f = N$, the entropy is $S_{\mathrm{ent}} = -\sum g[f\ln f + (1-f)\ln(1-f)]$, the grand potential (the thermodynamic effective potential) is $\Omega = -T\sum g\ln(1 + e^{-(\varepsilon-\mu)/T}) - 2\mathrm{Vol}_7\int_{-L}^{0}e^{6Hy}e_{\mathrm{int}}\,dy$, and $F = \Omega + \mu N$.

Discrepancy recorded, not hidden: the line “mu fixed by sum w_Z2 g f = N” of `ks-theory.json` is inconsistent with its own densities, energy and grand potential; the solver and the reference use $\sum g f = N$, and `Revision/kohn_sham/results/parameters.json` records the discrepancy.

| item | Wolfram records | sympy records |
| --- | --- | --- |
| uniform gas and exchange | `gas_mode_projector`, `gas_angular_average`, `gas_densities`, `exchange_uniform_gas` | `gas_mode_projector`, `gas_angular_average`, `gas_negative_energy_modes`, `gas_densities`, `hf_wick_contraction`, `exchange_uniform_gas`, `filled_shell_ratio` |
| Kohn-Sham potentials | `ks_potentials`, `ks_onshell_lagrangian` | `ks_potentials`, `ks_onshell_lagrangian`, `ks_theory_json_exchange` |
| coupling, cell volume and history | `ks_coupling_volume_scaling`, `history_solver_units` | `ks_coupling_volume_scaling`, `history_solver_units` |
| exact Fock exchange of the slab | `exchange_slab_exact_fock` | `exchange_slab_exact_fock` |

## 5. Boundary conditions, filling convention, numerics and parameters

**Brane (ASSUMED).** The Z2 mirror (orbifold) at $y = 0$: $\Psi(-y) = \pm\gamma^0\Psi(y)$ with the mirror warp $e^{-H|y|}$; continuity gives $(1 \mp \gamma^0)\chi(0) = 0$, i.e. the even parity $\chi_2(0) = 0$ ($b(0) = 0$) and the odd parity $\chi_1(0) = 0$ ($a(0) = 0$). Both conditions kill the $y$-current and make $h_j$ self-adjoint. The mirror map $P_A$ takes $(M(y), v(y))$ to $(-M(-y), v(-y))$: the doubled problem is $P_A$-symmetric exactly when the mirror copy carries $(-m, +\lambda)$. Both parities are solved and filled together; $N$ is the particle number of the doubled system (universe and Z2 image), the patch holds $N/2$, and $w = 1/2$ per patch.

**Tip (chosen).** At $y = -L$: $(1 - Q(\theta))\chi(-L) = 0$, $Q(\theta) = \cos\theta\,\sigma_3 + \sin\theta\,\sigma_2$, canonical $\theta = 0$, cutoff $L = 3$. For $k \neq 0$ an orbital is suppressed toward the tip like $\exp(-|k|(\kappa(-L) - \kappa(y))/H)$. The dependence on $L$ is measured in `Revision/kohn_sham/tip_convergence/` ($L = 3$ to $6$ in steps of $0.5$ with the record's step $h = 1/300$, every run repeated at $h/2$; a copy of the solver that reads $L$ from the environment reproduces the committed matrix byte for byte at $L = 3$; the reference solver agrees at $L = 3$ and $4$; report `Revision/kohn_sham/tip_convergence/tip-convergence.json`, 7 of 7 checks PASS); the study was rerun for the record with $b_4$ on 2026-10-16. The free results with $k \neq 0$ converge faster than exponentially (this suppression), and the recorded $L = 3$ values are low by up to 1.4% in $E_{KS}$ and 12% in $2\mathrm{Vol}_7\int e^{6Hy}p_0\,dy$ ($N = 136$, $\lambda = 0$, $a_{4,0} = 2$: 12.44507 against the extrapolated 12.62207, and 8.47270 against 9.63839). The $k = 0$ bulk levels approach $\pm m$ only like $(n\pi)^2/(2mL^2)$, so $N = 688$ at $a_{4,0} = 0$ does not converge (Parameters below). The brane zero modes have a proper density that grows toward the tip like $e^{(6H - 2m)|y|}$ (exact, verified), so the interacting $N = 8$ energy depends strongly on $L$: at $a_{4,0} = 0$, $E_{KS} = \mp 9.868\times10^{-4}$ at $L = 3$ ($\hat\lambda = \pm\lambda_1$) against $\mp 3.0073\times10^{-3}$ at large $L$ (extrapolated; the self-consistent iteration fails from $L = 5$): the recorded value is about one third of the large-$L$ value. With $b_4$ the effective coupling falls like $e^{-2a_{4,0}}$, and the ratio falls with it: at $a_{4,0} = 2$, $E_{KS} = \mp 1.816\times10^{-5}$ at $L = 3$ against $\mp 4.063\times10^{-4}$ at large $L$ (extrapolated from $\lambda = -\lambda_1$ at $a_{4,0} = 2$, the only interacting $N = 8$ state solved up to $L = 6$; the self-consistent iteration of the other five fails from $L = 5$, $5.5$ or $6$), about 1/22 of the large-$L$ value. The $\pm\lambda_1$ partners are negatives of each other to $3.6\times10^{-14}$ relative at every $L$ where both converge. The self-consistent iteration fails at some larger $L$ for 14 of the 19 interacting states studied (a failure of the iteration, not a proof that no self-consistent state exists); for 6 of them the successive differences of $E_{KS}$ do not meet the geometric-tail rule of the study before it fails, so their limit is not established.

**Exact $k = 0$ spectra.** For constant $M > 0$, $v = 0$, $\theta = 0$: even parity $\varepsilon = 0$ with the brane zero mode $\chi = (e^{My}, 0)$, and $\varepsilon = \pm\sqrt{M^2 + (n\pi/L)^2}$; odd parity $\varepsilon = \pm\sqrt{M^2 + p^2}$ with $\tan(pL) = -p/M$. The brane band has the slope $d\varepsilon/dk = jc$ at $k = 0$, $c = e^{-a_{4,0}}\frac{2M}{2M-H}\frac{1 - e^{-(2M-H)L}}{1 - e^{-2ML}}$; for $M = H = 1$, $L = 3$: $c = 2/(1 + e^{-3}) = 1.905148253644866$ (record `brane_band_slope`).

**Filling (CONVENTION, justification OPEN).** Particles occupy the positive branch (the levels with $\varepsilon > 0$ of the $\lambda = 0$ problem) and the $k = 0$ brane zero modes, each followed continuously in $\lambda$; the negative branch is the normal-ordered sea and contributes nothing to $N$, $n$, $S$ or the energy-momentum tensor. The excluded thermal sea holes are reported as a diagnostic (section 8).

**Numerics.** The Rust solver (`Revision/kohn_sham/solver`, own crate, no external crates) solves each block by shooting with RK4 on 900 steps, Pruefer counting and a root tolerance of 1e-13, Anderson-mixed SCF to 1e-11; when the direct iteration diverges it falls back to a continuation in the coupling ($\hat\lambda \times \frac14, \frac12, \frac34, 1$ with half the mixing). The independent Python reference (`Revision/kohn_sham/reference`) uses a staggered finite-difference discretisation on three grids (300, 600, 1200) with Richardson extrapolation and a stated uncertainty, validated on a fourth grid, with its own continuation fallback; its convergence order is two (record `free_convergence_order_two`).

**Parameters** (`Revision/kohn_sham/results/parameters.json`): $H = m = 1$, $L = 3$, $\Delta k = 0.25$, $v_t = 1$, $\mathrm{Vol}_7(0) = 15875.21366031351$ and $\mathrm{Vol}_7(a_{4,0}) = \mathrm{Vol}_7(0)\,e^{2a_{4,0}}$, tip $\theta = 0$, history $A = 1$, $\beta = 4/3$, slices $a_{4,0} \in \{0, 0.5, 1, 1.5, 2\}$, temperatures $T \in \{0.01, 0.02, 0.05\}$. Particle numbers: $N = 8$ (the $k = 0$ brane zero modes of both block types), $N = 688$ (the largest closed shell of the free $a_{4,0} = 0$ aufbau whose last level lies below the bulk edge 1.292292828068783; the bulk edge is an $L = 3$ value: 1.0977 at $L = 6$ and $m$ as $L \to \infty$, and from $L = 3.5$ on the $N = 688$, $a_{4,0} = 0$ aufbau occupies $k = 0$ bulk levels, its KS gap 0.0452 closes and its energy does not converge up to $L = 6$) and $N = 136$ (the closed shell nearest $688/4$). Couplings: $\lambda_1$ and $\lambda_2$ (values of $\hat\lambda$) keep the first-order mean-field potential below 0.1 and 0.3 (units of $m$) along the whole history; the strength is the largest first-order potential per unit $\hat\lambda$ over the five slices, with the densities per $\mathrm{Vol}_7(a_{4,0})$:

| N | strength per unit lambda_hat | lambda_1 | lambda_2 |
| --- | --- | --- | --- |
| 8 | 5.138804 | 0.01946 | 0.05838 |
| 136 | 8.295194 | 0.01206 | 0.03617 |
| 688 | 15.04944 | 0.006645 | 0.01993 |

This calibration is an $L = 3$ statement: the strength grows with $L$ (for $N = 8$ it is the zero-mode potential at the tip, $\propto e^{4L}$), so the same rule applied at larger $L$ drives $\lambda_1$ to zero: $1.2\times10^{-7}$ ($N = 8$, falling like $e^{-4L}$ from 0.01946 at $L = 3$), $1.2\times10^{-7}$ ($N = 136$) and $1.0\times10^{-11}$ ($N = 688$) at $L = 6$ (`Revision/kohn_sham/tip_convergence/`).

The canonical matrix holds 75 ground states ($3$ values of $N$, the five couplings $0, \pm\lambda_1, \pm\lambda_2$, five slices), each with its first excited state, its $a_4$ neighbours, its rescaling partner and, for $\lambda \neq 0$, its exact-Fock variant, and 135 Mermin states ($\hat\lambda \in \{0, \pm\lambda_1\}$, three temperatures).

| item | records |
| --- | --- |
| boundary conditions (Wolfram and sympy) | `bc_mirror_map_PA`, `bc_mirror_parities_of_densities`, `bc_brane_parity_conditions`, `bc_self_adjoint_boundary_term`, `bc_tip_family`, `bc_current_conserved_along_y`, `bc_exact_k0_spectra`, `bc_tip_asymptotics`, `brane_band_slope` |
| free problem (Rust solver) | `free_k0_analytic_spectra`, `free_zero_mode_exact`, `free_brane_band_slope`, `free_block_type_symmetries`, `free_particle_branch_labels`, `free_tip_angle_insensitivity` |
| free problem and parameters (reference) | `free_k0_analytic_spectra`, `free_convergence_order_two`, `free_k0_block_type_symmetry`, `free_zero_mode`, `free_brane_band_slope`, `free_particle_branch`, `parameters_closed_shells`, `parameters_calibration`, `richardson_asymptotic_ratio`, `richardson_uncertainty_validated` |
| parameters (cross-check) | `problem_definition_identical`, `parameters_particle_numbers`, `parameters_couplings` |

## 6. Instantaneous ground and first excited states along the prescribed history

The history is $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$ with $A = 1$ (the exponentially deflating member: the extra-time scale factor is $b_4(0)^{1/2}e^{-Hx_4/3}\sin^{1/6}z$), PRESCRIBED, not solved for (section 11). At every slice $a_{4,0}$ the ground state is the self-consistent aufbau state of the instantaneous problem; the first excited state is computed three ways: the Kohn-Sham gap $\varepsilon_{\mathrm{LUMO}} - \varepsilon_{\mathrm{HOMO}}$; the ensemble $\Delta$-SCF energy (one particle moved from the highest occupied degenerate group to the lowest empty group, spread uniformly over each group, self-consistent); and the list of the 24 lowest particle-hole excitations (`Revision/kohn_sham/results/excited/particle-hole/`). Every ground state of the matrix is closed-shell.

Ground and first excited states for $N = 136$ (`Revision/kohn_sham/results/ground/summary.csv` and `Revision/kohn_sham/results/excited/summary.csv`):

| lambda_hat | a4,0 | E_KS | KS gap | Delta-SCF |
| --- | --- | --- | --- | --- |
| 0 | 0 | 80.28222 | 0.08267377 | 0.08267377 |
| 0 | 1 | 32.38412 | 0.03498894 | 0.03498894 |
| 0 | 2 | 12.44507 | 0.01445687 | 0.01445687 |
| 0.01206 | 0 | 80.30152 | 0.08264233 | 0.08264235 |
| 0.01206 | 1 | 32.39984 | 0.03496186 | 0.03496188 |
| 0.01206 | 2 | 12.44558 | 0.01446012 | 0.01446012 |
| -0.01206 | 0 | 80.26318 | 0.0827042 | 0.08270419 |
| -0.01206 | 1 | 32.36934 | 0.03501284 | 0.03501283 |
| -0.01206 | 2 | 12.44454 | 0.01445372 | 0.01445372 |
| 0.03617 | 0 | 80.3408 | 0.08257647 | 0.08257652 |
| 0.03617 | 1 | 32.4346 | 0.03489553 | 0.03489559 |
| 0.03617 | 2 | 12.44653 | 0.01446695 | 0.01446695 |
| -0.03617 | 0 | 80.22592 | 0.08276204 | 0.082762 |
| -0.03617 | 1 | 32.34221 | 0.03505303 | 0.035053 |
| -0.03617 | 2 | 12.44345 | 0.0144477 | 0.0144477 |

The free Kohn-Sham gap along the history ($\lambda = 0$, `ground/summary.csv`):

| N | a4,0 = 0 | a4,0 = 0.5 | a4,0 = 1 | a4,0 = 1.5 | a4,0 = 2 |
| --- | --- | --- | --- | --- | --- |
| 8 | 0.4307337 | 0.2726449 | 0.1703493 | 0.1050152 | 0.06415941 |
| 136 | 0.08267377 | 0.05383771 | 0.03498894 | 0.0226437 | 0.01445687 |
| 688 | 0.04518029 | 0.03145504 | 0.02048367 | 0.01330982 | 0.008610228 |

Reading (labelled interpretation of these numbers): as the extra times deflate, the 3-momenta redshift as $ke^{-a_{4,0}}$, the brane band flattens (its slope at $k = 0$ is $c$, proportional to $e^{-a_{4,0}}$, section 5), the Kohn-Sham gap falls for every $N$ and $E_{KS}$ falls for $N = 136$ and $688$; for $N = 8$ (the $k = 0$ zero modes, on which $\kappa k = 0$) the free energy is 0 at every slice, and the interacting energy falls with the effective coupling $\hat\lambda e^{-2a_{4,0}}$. With $\lambda = 0$ the $\Delta$-SCF energy equals the Kohn-Sham gap (worst difference 2.011e-11 over 15 cases, record `excited_delta_scf_free_equals_gap`); with interaction the two differ slightly, because the $\Delta$-SCF state relaxes the mean field self-consistently.

| item | Rust solver records | reference records | cross-check records |
| --- | --- | --- | --- |
| ground states | `ground_runs_completed`, `ground_scf_converged`, `ground_closed_shell`, `ground_window_complete`, `ground_N_conservation`, `ground_energy_two_forms`, `ground_orbital_boundary_conditions` | `ground_scf_converged`, `ground_grid_consistency`, `ground_closed_shell`, `ground_window_complete`, `ground_N_conservation`, `ground_energy_two_forms` | `ground_occupations_and_groups`, `ground_energies`, `ground_homo_lumo_gap`, `ground_eigenvalues`, `ground_profiles` |
| first excited state | `excited_delta_scf_free_equals_gap`, `excited_scf_converged` | `excited_delta_scf_free_equals_gap`, `excited_particle_hole_lowest_is_gap` | `excited_delta_scf`, `excited_particle_hole_lists` |
| exact-Fock variant | `exx_variant_scf_converged`, `exx_variant_y_conservation` | `exx_scf_converged`, `exx_N_conservation`, `exx_energy_two_forms`, `exx_emt_energy_integral`, `exx_y_conservation_integrated` | `exchange_delta_E_x`, `exx_variant_scf` |
| SCF path (information) | `thermo_scf_path` | `scf_paths` | |

## 7. Adiabaticity and Fermi-level crossings

Exactly (mean field), $i\partial_{x_4}\chi = h(a_4(x_4))\chi$ conserves $k$, the block and the brane parity; transitions occur only between levels of the same $(k, j, \text{block}, \text{parity})$. The measure along $a_4 = AHx_4$ is

$$
Q_{nm} = AH\,\frac{\lvert\langle n\rvert\partial_ah\lvert m\rangle\rvert}{(\varepsilon_n - \varepsilon_m)^2} = AH\,\frac{\lvert\langle n\vert\partial_am\rangle\rvert}{\lvert\varepsilon_n - \varepsilon_m\rvert},\qquad
\partial_ah_j = -j\kappa k\sigma_3 + j(\partial_aM_{\mathrm{eff}})\sigma_2 + \partial_av_v ,
$$

for $n$ occupied and $m$ empty in the same sector; the state is adiabatic if $\max Q_{nm} \ll 1$, and $Q_{nm}^2$ is the leading-order transition probability. The self-consistent derivatives come from the states at $a_{4,0} \pm \delta$, $\pm 2\delta$ ($\delta = 2\times10^{-3}$, Richardson); they contain the change of the effective coupling $\hat\lambda/\mathrm{Vol}_7(a_{4,0})$ along the history. Hellmann-Feynman, $d\varepsilon_n/da = \langle n\rvert\partial_ah\lvert n\rangle$, is checked in 75 cases (worst 2.614e-9, record `adiabatic_hellmann_feynman`).

Results (`Revision/kohn_sham/results/adiabatic/adiabaticity.csv`): $Q_{\max} = 0$ exactly for $N = 8$ at $\lambda = 0$ ($\partial_ah$ vanishes on the $k = 0$ sector); for the interacting $N = 8$ states the falling effective coupling gives $\partial_aM_{\mathrm{eff}} \neq 0$ on that sector, and $Q_{\max} \leq 3.865\times10^{-3}$ (state N8_lamm2_a00, pair `0:-1:even:0 -> 0:-1:even:1`). The largest value over the whole matrix is 0.0935336 (state N688_lamp2_a00, pair `11:+1:even:0 -> 11:+1:even:1`: two levels of the same shell, block type and parity). For $\lambda = 0$:

| N | a4,0 | Q_max | delta eps of the pair | dE/da4 (EMT) | dE/da4 (differences) |
| --- | --- | --- | --- | --- | --- |
| 136 | 0 | 0.08514877 | 2.05293 | -71.43976 | -71.43976 |
| 136 | 0.5 | 0.07455997 | 1.888369 | -46.47084 | -46.47084 |
| 136 | 1 | 0.06361841 | 1.745737 | -30.11922 | -30.11922 |
| 136 | 1.5 | 0.05274874 | 1.616341 | -19.33966 | -19.33966 |
| 136 | 2 | 0.03839473 | 1.524416 | -12.18614 | -12.18614 |
| 688 | 0 | 0.09345059 | 2.253405 | -597.9157 | -597.9157 |
| 688 | 0.5 | 0.08526 | 2.055018 | -388.9333 | -388.9333 |
| 688 | 1 | 0.0746905 | 1.890122 | -253.016 | -253.016 |
| 688 | 1.5 | 0.06373822 | 1.747327 | -163.9948 | -163.9948 |
| 688 | 2 | 0.05289328 | 1.617688 | -105.4063 | -105.4063 |

The last two columns are the energy change along the history, from the energy-momentum tensor ($dE/da_4 = -3(P_3 - P_t) - \frac32\beta P_t$, $P = 2\mathrm{Vol}_7(a_{4,0})\int e^{6Hy}p\,dy$, section 9) and from finite differences at fixed occupations.

**Fermi-level crossings.** When levels of different $k$ cross the Fermi level between slices, the instantaneous aufbau ground state differs from the adiabatically continued state, and the solver flags it. No crossing occurs in the canonical matrix: every one of the 15 series of `Revision/kohn_sham/results/adiabatic/history.json` has an empty crossing list, and `adiabatic/fermi-level-crossings.csv` records no change of the occupied set. A demonstration at $\lambda = 0$ and $N = 696$ (the smallest closed shell of the $a_{4,0} = 0$ aufbau that occupies a level off the even $j = +1$ brane band; `adiabatic/crossing-demo.csv`):

| a4,0 | occupied set as at a4,0 = 0 | open shell | E aufbau | E adiabatically continued | difference |
| --- | --- | --- | --- | --- | --- |
| 0 | true | false | 690.7796 | 690.7796 | 0 |
| 0.5 | false | true | 444.1946 | 447.8513 | 3.65669 |
| 1 | false | true | 283.7106 | 289.7632 | 6.052645 |
| 1.5 | false | true | 179.4593 | 187.0712 | 7.611827 |
| 2 | false | true | 112.1016 | 120.725 | 8.623384 |

From $a_{4,0} = 0.5$ on, the $k = 0$ odd bulk level is emptied and the $n_2 = 12$ brane-band shell is filled: the instantaneous ground state is not the adiabatically reached state, which lies above it by the last column.

Interpretation (labelled): with $Q_{\max} \leq 0.0935336$ the instantaneous states are self-consistently adiabatic for the same-sector transitions at the rate $A = 1$ in the canonical matrix; this does not solve the time-dependent problem (OPEN), and where Fermi-level crossings occur (the demonstration) the instantaneous ground state is not the state that the evolution reaches.

| Rust solver records | reference records | cross-check records |
| --- | --- | --- |
| `adiabatic_hellmann_feynman`, `adiabatic_crossing_flag_demonstration` | `adiabatic_hellmann_feynman_discrete`, `crossing_demo_reference` | `adiabatic_dE_da4`, `adiabatic_Q_max`, `crossing_demonstration` |

## 8. Mermin thermodynamics

The Mermin states at $T = 0.01, 0.02, 0.05$ solve the self-consistent problem at fixed $N$ with $\mu$ the root of $\sum g f = N$ in a well-conditioned form (thermal particles above and holes below a split of the levels, `solver/src/mermin.rs`). The checks: $\Omega$ in its two forms, $-dF/dT = S_{\mathrm{ent}}$, $C_V = T\,dS_{\mathrm{ent}}/dT = dE/dT$ at fixed $N$, and the chemical potential against 40-digit roots on the solver's own final levels (40-digit and 50-digit roots agree to 7.5e-35, record `root_precision_self_check`). The thermal state N688_lamm1_a00_T10 needs the coupling continuation in both solvers (record `thermo_scf_path` of the Rust solver names it; record `scf_paths` of the reference lists it as the only state that needed it, on its three grids). For $N = 136$, $\lambda = 0$ (`Revision/kohn_sham/results/thermo/thermodynamics.csv`):

| a4,0 | T | mu | E | entropy | Omega | sea holes / N |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0.01 | 0.8339283 | 80.34462 | 7.763517 | -33.14726 | 2.1e-56 |
| 0 | 0.02 | 0.8250861 | 80.74027 | 34.38332 | -32.1591 | 9.49e-29 |
| 0 | 0.05 | 0.7941344 | 82.71202 | 91.45989 | -29.86326 | 4.43e-12 |
| 2 | 0.01 | 0.1247136 | 12.99426 | 104.8261 | -5.015053 | 1.29e-09 |
| 2 | 0.02 | 0.1150668 | 14.49922 | 205.4874 | -5.259608 | 4.25e-05 |
| 2 | 0.05 | 0.05801333 | 23.38445 | 464.1395 | -7.712339 | 0.112 |

**Validity of the particle-only ensemble (diagnostic of the CONVENTION).** For every thermal state the number of thermal holes that the excluded sea brane band would carry at the same $\mu$ and $T$ is computed. It exceeds 1% of $N$ in 15 of 135 states, all at $a_{4,0} \geq 1$; the largest is 30.808 N (record `thermo_sea_hole_diagnostic_computed`). There the particle-only Mermin ensemble is outside its range of validity and a thermal treatment of the sea (pairs) would be required; in the table above this is the row $a_{4,0} = 2$, $T = 0.05$ (state N136_lam0_a20_T50).

| Rust solver records | reference records | cross-check records |
| --- | --- | --- |
| `thermo_runs_completed`, `thermo_scf_converged`, `thermo_N_conservation`, `thermo_grand_potential_two_forms`, `thermo_entropy_identity`, `thermo_CV_identity`, `thermo_window_cut`, `thermo_window_shells_beyond`, `thermo_mu_well_conditioned_root`, `thermo_mu_vs_40digit_roots`, `thermo_sea_hole_diagnostic_computed` | `thermo_scf_converged`, `thermo_N_conservation`, `thermo_grand_potential_two_forms`, `thermo_CV_identity`, `thermo_entropy_identity`, `thermo_window_cut`, `thermo_sea_holes_tail` | `thermo_state_functions`, `thermo_derivatives`, `thermo_sea_hole_diagnostic`, `thermo_levels`, `thermo_mu_high_precision`, `thermo_mu_rounding_diagnostic`, `thermo_mu_rust_stated_bound` |

| Mermin-root report | records |
| --- | --- |
| `Revision/kohn_sham/reports/ks-rust-mermin-roots.json` | `solver_runs_completed`, `root_precision_self_check`, `solver_mu_within_rounding_bound`, `single_reproduces_committed_matrix`, `fixture_written` |

## 9. Energy-momentum tensor profiles

With the sign convention of `Revision/SPEC.md` section 4 ($\rho = -T^{x_4}{}_{x_4}$, $p_\mu = T^\mu{}_\mu$) and $T^\mu{}_\nu = -\langle K^\mu{}_\nu\rangle + \delta^\mu_\nu e_{\mathrm{int}}$, the proper profiles are

$$
\begin{aligned}
\rho(y) &= \textstyle\sum w g f\,\varepsilon\,n_o - e_{\mathrm{int}} ,\qquad
p_3(y) = \textstyle\sum w g f\,\tfrac{\kappa|k|}{3}\,t_o + e_{\mathrm{int}} ,\qquad
p_t(y) = e_{\mathrm{int}} ,\\
p_0(y) &= \textstyle\sum w g f\,\big[(\varepsilon - v_v)n_o - M_{\mathrm{eff}}s_o - \kappa|k|\,t_o\big] + e_{\mathrm{int}} ,
\end{aligned}
$$

with $T^{x_4}{}_y = 0$ for eigen-orbitals. The extra-time pressure $p_t$ has no kinetic part (good sector). Exact identities, checked for every state: the trace of the kinetic parts is $M_{\mathrm{eff}}S + v_vn$; conservation along the hidden direction, $p_0' + 6Hp_0 = 3H(p_3 + p_t)$; the energy change $\nabla_\mu T^\mu{}_{x_4} = -\partial_{x_4}\rho - 3a_4'(p_3 - p_t) - \frac32(b_4'/b_4)(\rho + p_t)$, i.e. on the history $dE/da_4 = -3(P_3 - P_t) - \frac32\beta P_t$ with $P = 2\mathrm{Vol}_7(a_{4,0})\int_{-L}^{0}e^{6Hy}p\,dy$ ($\beta = \frac43$: $-3(P_3 - P_t) - 2P_t$); and $2\mathrm{Vol}_7\int e^{6Hy}\rho\,dy = E_{KS}$. Integrated profiles ($2\mathrm{Vol}_7(a_{4,0})\int_{-L}^{0}e^{6Hy}X\,dy$, `Revision/kohn_sham/results/ground/emt-integrals.csv`), $\lambda = 0$:

| N | a4,0 | int rho | int p3 | int p_t | int p0 |
| --- | --- | --- | --- | --- | --- |
| 136 | 0 | 80.28222 | 23.81325 | 0 | 35.04349 |
| 136 | 0.5 | 51.24519 | 15.49028 | 0 | 26.62178 |
| 136 | 1 | 32.38412 | 10.03974 | 0 | 19.33023 |
| 136 | 1.5 | 20.20308 | 6.446555 | 0 | 13.173 |
| 136 | 2 | 12.44507 | 4.062048 | 0 | 8.472703 |
| 688 | 0 | 680.4412 | 199.3052 | 0 | 240.5598 |
| 688 | 0.5 | 437.5129 | 129.6444 | 0 | 188.2465 |
| 688 | 1 | 279.4249 | 84.33868 | 0 | 143.2073 |
| 688 | 1.5 | 176.7328 | 54.66494 | 0 | 104.3887 |
| 688 | 2 | 110.3867 | 35.13543 | 0 | 71.5579 |

The profiles on 151 points $y = -3 + 0.02i$ are in `Revision/kohn_sham/results/ground/profiles/` (one file per state; densities per $\mathrm{Vol}_7(a_{4,0})$, that is the proper densities times $b_4(0)^{3/2}$). The energy density varies along the hidden direction in every state with a nonzero tensor (section 11). Equations of state seen by a 3-space observer are not part of this document; they are the work of `Revision/dark_sector/dirac16complex` (its Kohn-Sham history report `Revision/dark_sector/dirac16complex/reports/ks-history-run.json`: 8 of 8 PASS).

| item | Wolfram and sympy records | Rust solver records | reference and cross-check records |
| --- | --- | --- | --- |
| tensor and identities | `emt_orbital_components`, `emt_trace_identity`, `emt_y_conservation_orbital`, `emt_y_conservation_selfconsistent`, `emt_x4_component`, `emt_energy_change_history` | `emt_energy_integral`, `emt_trace_derivative_form`, `emt_y_conservation_integrated`, `emt_y_conservation_pointwise`, `emt_energy_change_dE_da4` | `emt_energy_integral`, `emt_y_conservation_integrated`, `emt_energy_change_dE_da4`, `emt_integrals`, `emt_brane_tip_values` |

## 10. The rescaling partners

**Exact identity.** Because $a_{4,0}$ enters only through $\kappa k = e^{-Hy}(ke^{-a_{4,0}})$ and $b_{4,0}$ only through the proper cell volume $\ell^3v_tb_{4,0}^{3/2}$,

$$
\mathrm{KS}(a_{4,0}, b_{4,0};\,\Delta k, v_t, \lambda, N, T) = \mathrm{KS}\big(0, b_4(0);\,\Delta k\,e^{-a_{4,0}},\, v_t\,e^{-3a_{4,0}}(b_{4,0}/b_4(0))^{3/2},\, \lambda, N, T\big)
$$

for the levels, orbitals, proper densities and energy-momentum profiles; on the history ($b_{4,0}/b_4(0) = e^{(4/3)a_{4,0}}$) the partner has $\Delta k\,e^{-a_{4,0}}$ and $v_t\,e^{-a_{4,0}}$ at the same $\hat\lambda$. Reading (labelled): the slice $a_{4,0}$ of the deflating history is the slice 0 with a 3-torus larger by $e^{a_{4,0}}$ in each direction and an extra-time coordinate volume smaller by $e^{-a_{4,0}}$: the same proper cell, because the factor $e^{-3a_{4,0}}$ of the extra times and the growth $b_4^{3/2}$ combine to $e^{-a_{4,0}}$ for the coordinate volume while the 3-torus grows by $e^{3a_{4,0}}$. The 3-momenta redshift while the proper cell stays the same.

**Computed.** Each solver solves the partner independently (60 partners). The worst level difference is 1.550e-13 and the worst relative difference of $E_{KS}$ and of the profiles 1.914e-13 (records `rescaling_identity_between_slices` and `rescaling_identity_energy_profiles`). For $N = 136$, $\hat\lambda = \lambda_1$ (`Revision/kohn_sham/results/rescaling/rescaling.csv`):

| a4,0 | partner Delta k | partner v_t | max delta eps | relative delta E | partner E_KS |
| --- | --- | --- | --- | --- | --- |
| 0.5 | 0.1516327 | 0.6065307 | 0 | 0 | 51.26441 |
| 1 | 0.09196986 | 0.3678794 | 9.504e-14 | 0 | 32.39984 |
| 1.5 | 0.05578254 | 0.2231302 | 2.665e-15 | 1.758e-16 | 20.20944 |
| 2 | 0.03383382 | 0.1353353 | 9.104e-14 | 0 | 12.44558 |

| Wolfram and sympy records | Rust solver records | reference and cross-check records |
| --- | --- | --- |
| `rescaling_identity` | `free_rescaling_relation_and_band_monotone`, `rescaling_identity_between_slices`, `rescaling_identity_energy_profiles` | `rescaling_identity_reference`, `rescaling_partners` |

## 11. The recorded states are not admissible sources of the $a_4$ and $b_4$ equations

`Revision/SPEC.md` section 7 names the Kohn-Sham energy-momentum tensor as the source of the field equations for $a_4$ and $b_4$. The Einstein-Lovelock equations of the author's metric (`Revision/field_equations_a4`, key generalSource of `a4-equations.json`) require of any source: (C1) every diagonal component independent of $x_0$ (the diagonal left-hand sides contain no $x_0$ for every $a_4$, $b_4$); (C2) the combination $p_3 + p_t - 2p_0$ equals $\sum_k\alpha_k(E^{x_1}{}_{x_1} + E^{x_5}{}_{x_5} - 2E^{x_0}{}_{x_0})/\kappa$, which vanishes on the history with the author's weights; (C3) on the history $a_4 = Hx_4$, $b_4 = b_4(0)e^{(4/3)Hx_4}$ with the author's weights and $\Lambda = -10$, the constant source $\kappa(\rho, p_3, p_t, p_0) = (-\frac{2}{27}, -\frac29, -\frac{22}{27}, -\frac{14}{27})$ ($H = 1$); (C4) the off-diagonal equation $\kappa q_{40} = \cot z\,(b_4'/b_4)\,Q$, where $Q = 0$ on the history (the reason for $\beta = \frac43$). The record `Revision/field_equations_a4/reports/ks-source-conditions.json` (6 of 6 PASS) finds:

1. Every one of the 70 nonzero ground-state profiles depends on $x_0$: $(\max\rho - \min\rho)/\max|T| \geq 0.0757506$ (record `ks_profiles_depend_on_x0`); C1 fails for every $a_4(x_4)$ and $b_4(x_4)$.
2. On the history $\max_y|p_3 + p_t - 2p_0|/\max|T|$ lies between 1.04172 and 3.99008 (record `ks_profiles_violate_algebraic_condition`): C2 fails pointwise.
3. Integrated over the patch, $(\int p_3 + \int p_t)/(2\int p_0)$ differs from 1 for every nonzero state (closest 0.416888); for the history $N = 136$, $\lambda = 0$ it is 0.339767, 0.25969 and 0.239714 at $a_{4,0} = 0, 1, 2$ (record `ks_integrals_violate_algebraic_condition`): even an $x_0$-averaged source violates C2.
4. The history needs the constant source of C3, a negative energy density with $p_3/\rho = 3$, $p_t/\rho = 11$, $p_0/\rho = 7$; the Kohn-Sham source has a positive energy density that changes along the history: the history is a PRESCRIBED background (record `ks_history_is_a_prescribed_background`).
5. The off-diagonal condition C4 holds: every Kohn-Sham state has $T^{x_4}{}_y = 0$, and $Q = 0$ on the history; in Einstein gravity a source with $q_{40} = 0$ would force $b_4' = 0$ (record `ks_offdiagonal_condition_on_history`).
6. Five states have an identically vanishing tensor (the free $N = 8$ zero modes), a zero source, which is not admissible either: with the author's weights every vacuum solution has $b_4$ constant, and Einstein gravity has no vacuum solution with $H > 0$ (record `ks_zero_source_states_listed`).

The full analysis `Revision/field_equations_a4/ks_source/reports/ks-source-a4.json` (22 of 22 PASS) refines this exactly: the states SATISFY the $x_0$ conservation identity, and $p_3 + p_t - 2p_0 = p_{0,y}/(3H)$ on shell, so the diagonal components depend on $x_0$, which the field equations exclude for every $a_4$ and $b_4$; at least a share 0.582938 of the energy density deviates from its hidden-direction average (L1 measure). The off-diagonal equation needs $Q = 0$ at every instant of a history with changing $b_4$; in Einstein gravity $Q = \frac32H$, so there is no such history at all. Its conclusion: the coupled problem “metric of `Revision/SPEC.md` section 1 with $b_4$ + Kohn-Sham source” has no solution, and nothing about $a_4$ or $b_4$ is derived from it. In a stated approximation (the $x_4$ moment and the off-diagonal equation kept, two algebraic equations for $a_4'$ and $b_4'/b_4$; the other moments dropped, with dropped residuals of order one) the Kohn-Sham source does not start or select the exponential deflation: with the author's weights the start on the record's history needs $\kappa\bar\rho(0) = -\frac{2}{27}H^2$ ($\kappa < 0$ for this gas of positive energy density), and as the gas dilutes the solution leaves the history and reaches a fold of the algebraic system at $a_4 = 0.024$ ($N = 136$, $\lambda = 0$; there $a_4'/H = 0.870762$ and $(b_4'/b_4)/H = 1.09136$, against 1 and $\frac43$ on the history); with the stated Gauss-Bonnet coupling the branch $u_0 = (-6 + 2\sqrt5)H$ runs through $a_4 = 2$ for $\kappa\bar\rho(0) \leq 0$ and ends at a fold for $\kappa\bar\rho(0) > 0$, and on the branch $u_0 = (-6 - 2\sqrt5)H$ the rates grow until the adiabaticity measure reaches 1 or a fold is reached. These are statements of that approximation, not of the field equations.

Consequence: the Kohn-Sham gas of this record is a test field on the prescribed background $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$ without back-reaction; energies, pressures and equations of state along the history are not consequences of the coupled field equations.

| report | records |
| --- | --- |
| `Revision/field_equations_a4/reports/ks-source-conditions.json` | `ks_profiles_depend_on_x0`, `ks_profiles_violate_algebraic_condition`, `ks_integrals_violate_algebraic_condition`, `ks_history_is_a_prescribed_background`, `ks_offdiagonal_condition_on_history`, `ks_zero_source_states_listed` |
| `Revision/field_equations_a4/ks_source/reports/ks-source-a4.json` | `A1_x1_x5_x0_combination_with_b4`, `A2_offdiagonal_equation_needs_Q_zero`, `A5_x0_conservation_in_y`, `A6_branches_at_the_initial_rate`, `B0_source_condition_report_verified`, `B2_x0_conservation_on_every_profile`, `B4_hidden_direction_mismatch`, `C1_averaged_algebraic_condition_fails`, `C3_record_history_not_a_solution_of_the_x4_moment`, `D2_author_weights_start_on_the_record_history`, `D5_outcomes` |
| Kohn-Sham theory (the record and the label of the history) | `adiabatic_offdiagonal_identity`, `ks_theory_json_written`, `ks_theory_json_basis`, `ks_theory_json_slope`, `ks_theory_json_history_label` |

## 12. The Kohn-Sham-level pairing T3

The block map of the chirality $\Gamma$, $(\chi, j) \to (\sigma_2\chi, -j)$, with the two brane parities exchanged and the tip angle $\theta \to \pi - \theta$, maps every self-consistent instantaneous Kohn-Sham state with $(m, \lambda, \theta)$ onto one with $(-m, +\lambda, \pi - \theta)$, with equal levels, occupations, Kohn-Sham energies and energy-momentum profiles and $S \to -S$ (ASSUMED Z2 brane, mean-field level); $b_4$ does not enter $h_j$, so it holds slice by slice for every $b_4$. The theorem, its hypotheses and its proof are in `Revision/docs/PAIR_CREATION_PROOFS.md` section 8, verified by `Revision/pairing/kohn_sham/reports/wolfram-t3.json` (10 of 10 PASS) and `Revision/pairing/kohn_sham/reports/python-t3.json` (13 of 13 PASS); its completion record (`Revision/pairing/kohn_sham/t3-completion.json`) by `Revision/pairing/kohn_sham/reports/wolfram-t3-completion.json` (3 of 3 PASS) and `Revision/pairing/kohn_sham/reports/python-t3-completion.json` (7 of 7 PASS). The Rust solver contains a numerical self-test, labelled in its report as NOT a proof of T3: $(m, \lambda, \theta = 0)$ and $(-m, \lambda, \theta = \pi)$, solved independently, agree with opposite $S$ (worst 8.35e-14, tolerance 1e-9; record `t3_block_map_solver_selftest`). T3 does not establish a creation process, a rate or an amplitude.

## 13. Verification records

### 13.1 Reports and their counts

Every check has a name, a verdict and a detail. Counts at the time of writing (the publication test re-reads them):

| report | checks | PASS | FAIL |
| --- | --- | --- | --- |
| `Revision/kohn_sham/reports/ks-theory-wolfram.json` | 51 | 51 | 0 |
| `Revision/kohn_sham/reports/ks-theory-python.json` | 63 | 63 | 0 |
| `Revision/kohn_sham/reports/ks-rust-solver.json` | 43 | 43 | 0 |
| `Revision/kohn_sham/reports/ks-rust-determinism.json` | 14 | 14 | 0 |
| `Revision/kohn_sham/reports/ks-rust-mermin-roots.json` | 5 | 5 | 0 |
| `Revision/kohn_sham/reports/ks-reference.json` | 38 | 38 | 0 |
| `Revision/kohn_sham/reports/ks-crosscheck.json` | 31 | 31 | 0 |
| `Revision/field_equations_a4/reports/ks-source-conditions.json` | 6 | 6 | 0 |
| `Revision/field_equations_a4/ks_source/reports/ks-source-a4.json` | 22 | 22 | 0 |
| `Revision/field_equations_a4/reports/wolfram-a4-report.json` | 59 | 59 | 0 |
| `Revision/field_equations_a4/reports/python-a4-report.json` | 65 | 65 | 0 |
| `Revision/pairing/kohn_sham/reports/wolfram-t3.json` | 10 | 10 | 0 |
| `Revision/pairing/kohn_sham/reports/python-t3.json` | 13 | 13 | 0 |
| `Revision/kohn_sham/tip_convergence/tip-convergence.json` | 7 | 7 | 0 |

### 13.2 The independent reference and the full cross-check

The reference shares no code with the Rust solver: different discretisation (staggered finite differences with Richardson extrapolation instead of RK4 shooting), its own SCF and continuation fallback, its own parameter derivation (it re-derives the particle numbers and couplings from the stated rules) and its own uncertainty, validated on a fourth grid (record `richardson_uncertainty_validated`). The checker `Revision/kohn_sham/checker/crosscheck_ks.py` compares the two on the FULL canonical matrix: 75 ground states, 135 thermal states, 60 exact-Fock-variant states, 60 rescaling partners, 75 particle-hole lists and the 5 slices of the crossing demonstration, 162731 comparisons in all, under a tolerance rule fixed before the comparison,

$$
\lvert x_{\mathrm{Rust}} - x_{\mathrm{ref}}\rvert \leq 3\,(U_{\mathrm{ref}} + U_{\mathrm{Rust}}) + 10^{-12}\,\mathrm{scale},\qquad
U_{\mathrm{Rust}} = \tfrac{16}{15}\,\lvert\mathrm{canonical} - \mathrm{refined}\rvert ,
$$

with $U_{\mathrm{ref}}$ the reference's three-grid Richardson uncertainty and $U_{\mathrm{Rust}}$ measured for every state of the matrix by the refinement measurement, whose script and record are `Revision/kohn_sham/checker/measure_rust_refinement.py` and `Revision/kohn_sham/checker/rust-refinement.json`. All 31 checks of the cross-check pass:

| check | check | check |
| --- | --- | --- |
| `inputs_all_pass` | `rust_refinement_applies_to_matrix` | `rust_refinement_applies_to_matrix_exx` |
| `problem_definition_identical` | `parameters_particle_numbers` | `parameters_couplings` |
| `ground_occupations_and_groups` | `ground_energies` | `ground_homo_lumo_gap` |
| `ground_eigenvalues` | `excited_delta_scf` | `excited_particle_hole_lists` |
| `emt_integrals` | `emt_brane_tip_values` | `ground_profiles` |
| `exchange_delta_E_x` | `adiabatic_dE_da4` | `adiabatic_Q_max` |
| `exx_variant_scf` | `rescaling_partners` | `crossing_demonstration` |
| `thermo_state_functions` | `thermo_derivatives` | `thermo_sea_hole_diagnostic` |
| `thermo_levels` | `thermo_mu_high_precision` | `thermo_mu_rounding_diagnostic` |
| `thermo_mu_rust_stated_bound` | `reference_outputs_lf_only` | `reference_manifest` |
| `reference_repeat_byte_identical` |  |  |

### 13.3 Determinism and the refinement measurement

The Rust determinism report (14 of 14 PASS): a repeat of the canonical matrix is byte-identical in all 244 result files and in its check report (`repeat_byte_identical`, `repeat_report_byte_identical`, `outputs_lf_only`); a run with refined tolerances (900 to 1800 RK4 steps, root tolerance 1e-14, SCF tolerance 1e-12) agrees with the canonical run to 2.000e-12 in $E_{KS}$ (relative), 2.143e-09 in 23724 levels, 7.050e-09 in the profiles, 1.435e-07 in $Q_{\max}$ and $dE/da_4$, 2.489e-10 in the thermodynamics and 5.689e-09 in $C_V$ (`refined_same_inputs`, `refined_free_spectra_convergence_order`, `refined_ground_energies`, `refined_ground_homo_lumo_gap`, `refined_eigenvalues`, `refined_delta_scf`, `refined_profiles`, `refined_adiabatic_derivatives`, `refined_thermodynamics`, `refined_mermin_root_path`, `refined_heat_capacity`).

### 13.4 Re-verification for this document

For this document (2026-10-16, the record with $b_4$) the committed Rust binary was run on the canonical matrix into a scratch directory (`revision_ks_solver all --out <scratch>/rerun --report <scratch>/rerun-report.json`): 43 of 43 checks PASS in 95.6 s of wall time, and all 244 result files and the check report were byte-identical to the committed `Revision/kohn_sham/results` and `Revision/kohn_sham/reports/ks-rust-solver.json`. The other reports cited are the files of the working tree; their counts are re-read by the publication test.

## 14. Reproduction

From the repository root, in this order (the Kohn-Sham theory record reads the gammas of `Revision/algebra`; the Rust solver reads `ks-theory.json`; the Mermin-root tool runs after the canonical matrix; the reference runs in six parts with a job cache, each part within a few minutes, and a final run writes its outputs; the cross-checker runs after the reference and the refinement measurement, with its own repeat of the reference, also in parts; the source-conditions checker reads the Kohn-Sham results and the Kohn-Sham theory checker reads its record; the Kohn-Sham source analysis reads the dense free-gas history of the dark sector, `Revision/dark_sector/dirac16complex/compute/run_ks_history.py`; `<scratch>` is any empty directory outside the repository; the backslash is the line continuation of a POSIX shell):

```text
wolframscript -file Revision/algebra/wolfram/verify_algebra.wls
python Revision/algebra/python/check_algebra.py
wolframscript -file Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls
python Revision/field_equations_a4/python/check_field_equations_a4.py
wolframscript -file Revision/kohn_sham/theory/verify_ks_theory.wls
cargo build --release --manifest-path Revision/kohn_sham/solver/Cargo.toml
cargo test --release --manifest-path Revision/kohn_sham/solver/Cargo.toml
Revision/kohn_sham/solver/target/release/revision_ks_solver all \
    --out Revision/kohn_sham/results \
    --report Revision/kohn_sham/reports/ks-rust-solver.json
python Revision/kohn_sham/solver/tools/mermin_roots_mp.py --work <scratch>/mermin-roots
Revision/kohn_sham/solver/target/release/revision_ks_solver all \
    --out <scratch>/repeat --report <scratch>/repeat-report.json
Revision/kohn_sham/solver/target/release/revision_ks_solver all --refined \
    --out <scratch>/refined --report <scratch>/refined-report.json
python Revision/kohn_sham/solver/tools/compare_runs.py \
    --canonical Revision/kohn_sham/results \
    --canonical-report Revision/kohn_sham/reports/ks-rust-solver.json \
    --repeat <scratch>/repeat \
    --repeat-report <scratch>/repeat-report.json --refined <scratch>/refined \
    --refined-report <scratch>/refined-report.json \
    --report Revision/kohn_sham/reports/ks-rust-determinism.json
python Revision/kohn_sham/reference/run_reference.py --cache <scratch>/cache \
    --part 1/6 --jobs 12          # and so on up to --part 6/6
python Revision/kohn_sham/reference/run_reference.py --cache <scratch>/cache --jobs 12
python Revision/kohn_sham/checker/measure_rust_refinement.py \
    --work <scratch>/rust-single --jobs 22
python Revision/kohn_sham/reference/run_reference.py --cache <scratch>/repeat-cache \
    --part 1/6 --jobs 12          # and so on up to --part 6/6
python Revision/kohn_sham/checker/crosscheck_ks.py --work <scratch>/cc --jobs 22 \
    --repeat-cache <scratch>/repeat-cache
python Revision/kohn_sham/tip_convergence/tip_convergence.py \
    --work <scratch>/tip --jobs 8
python Revision/field_equations_a4/python/check_ks_source_conditions.py
python Revision/kohn_sham/theory/check_ks_theory.py
python Revision/dark_sector/dirac16complex/compute/run_ks_history.py \
    --solver Revision/kohn_sham/solver/target/release/revision_ks_solver
python Revision/field_equations_a4/ks_source/ks_source_a4.py
python -m unittest Revision/field_equations_a4/ks_source/test_ks_source_a4.py -v
wolframscript -file Revision/pairing/kohn_sham/wolfram/verify_t3.wls
python Revision/pairing/kohn_sham/python/check_t3.py
python scripts/build_provenance_pdf.py Revision/docs/KOHN_SHAM_DEFLATING_FIELD.md \
    --developer-layout --specifications Revision/pdf-specifications.json
python -m unittest Revision/tests/test_kohn_sham_deflating_field_publication.py -v
```

Expected output: every verifier ends with all of its checks passing and writes the report of section 13.1 with the counts given there (the Wolfram Kohn-Sham verifier prints 51/51 checks passed; the Rust solver prints SUCCESS after 43 PASS lines; the cross-checker writes 31 of 31 PASS; the tip-cutoff study prints 7 PASS lines and SUCCESS); every run is deterministic, and a second run gives byte-identical outputs. Run times recorded in the READMEs of the folders (longer when the machine is shared): the Wolfram Kohn-Sham verifier about 40 to 85 s and the sympy checker about 75 to 165 s (`Revision/kohn_sham/theory/WOLFRAMSCRIPT_PROVENANCE.md`); on 2026-10-16, on an otherwise idle machine with 22 threads, the Rust canonical matrix 78.0 s, the repeat 75.7 s and the refined-tolerance run 340.6 s (`Revision/kohn_sham/solver/README.md`; 95.6 s in the re-run of section 13.4); the reference in six parts of 227 s, 190 s, 219 s, 232 s, 124 s and 120 s with 12 processes each (`Revision/kohn_sham/reference/README.md`); the refinement measurement 32.9 s, the repeat of the reference for the cross-check in six parts of 198 s, 179 s, 214 s, 234 s, 117 s and 122 s, and the cross-checker itself 20.5 s (`Revision/kohn_sham/checker/README.md`); the tip-cutoff study 187 s with 22 workers (`Revision/kohn_sham/tip_convergence/README.md`); the Kohn-Sham source analysis about 2 s and its unit tests about 12 s (`Revision/field_equations_a4/ks_source/README.md`); the $a_4$ verifiers 43 to 70 s (Wolfram) and 7 to 28 s (sympy) on 2026-10-07 (`Revision/field_equations_a4/README.md`); the T3 verifiers about 3 s and 1 s (`Revision/pairing/kohn_sham/README.md`).

The PDF build runs the Markdown-to-LaTeX builder twice (with different hash seeds), runs pdflatex three times into each of two fresh directories, requires warning-free logs and byte-identical PDFs, and checks the PDF against its entry `kohn-sham-deflating-field` in `Revision/pdf-specifications.json` (the Revision registry; the registry of the earlier stages is not touched).

## 15. What is proved, computed, assumed and not established

### 15.1 Proved (exact, two independent verifiers)

1. The block reduction (section 3): for every history $a_4(x_4)$, $b_4(x_4)$ the good-sector equation reduces exactly to eight $2 \times 2$ blocks $h_j$ in the hidden coordinate; the spin-connection terms $3H\gamma^0$ and $\frac34(b_4'/b_4)\gamma^4$ are removed by $W^{-3}$ and $b_4^{-3/4}$; the $a_4'$ terms of the inflating and the deflating directions cancel; $b_4$ does not enter $h_j$.
2. The exchange functional (section 4): the exact local exchange of the uniform 8-fold good-sector gas at every temperature, $M_{\mathrm{eff}} = m + \frac{15}{16}\lambda S$, $v_v = -\lambda n/16$; the exact Fock exchange of the closed-shell slab differs by $+\lambda Q^2/32$; a state depends on the coupling and the cell volume only through their ratio.
3. The boundary-value structure (section 5): self-adjointness with current-killing ends, the mirror map and the parities, the exact $k = 0$ spectra, the brane-band slope.
4. The rescaling identity (section 10), the energy-momentum tensor of the Kohn-Sham states with its trace and conservation identities and the energy change with the $b_4$ term (section 9), and the adiabaticity identity of the measure (section 7).
5. T3 (section 12; proved in `Revision/docs/PAIR_CREATION_PROOFS.md`), under its stated hypotheses.

### 15.2 Computed (numerical, two independent solvers, cross-checked)

1. The instantaneous ground states, first excited states (gap, $\Delta$-SCF, particle-hole lists), Mermin states, energy-momentum profiles, rescaling partners and exact-Fock variants of the canonical matrix (sections 6 to 10), with the Rust solver and the reference agreeing on the full matrix within the stated uncertainty (31 of 31 checks, 162731 comparisons).
2. The adiabaticity measure ($Q_{\max} \leq 0.0935336$) and the absence of Fermi-level crossings in the canonical matrix; the crossing demonstration at $N = 696$ (section 7).
3. That the recorded states are not admissible sources of the $a_4$ and $b_4$ equations (section 11).
4. The dependence on the tip cutoff $L$ from 3 to 6 of 29 recorded states, the 27 ground states with $N \in \{8, 136, 688\}$, $\lambda \in \{0, \pm\lambda_1\}$, $a_{4,0} \in \{0, 1, 2\}$ and two Mermin states of $N = 136$ ($\lambda = 0$, $a_{4,0} = 2$, $T = 0.05$; $\lambda = \lambda_1$, $a_{4,0} = 1$, $T = 0.02$) (section 5; `Revision/kohn_sham/tip_convergence/`, 7 of 7 checks PASS; the Rust solver at every $L$, the reference at $L = 3$ and $4$).

### 15.3 Assumed or chosen

1. The Z2 brane (orbifold) at the patch end $z = \pi/2$ (ASSUMED); the metric is degenerate there and no junction condition is derived.
2. The regular tip at the cutoff $L = 3$ with $\theta = 0$ (chosen). Its effect is measured (`Revision/kohn_sham/tip_convergence/`, $L = 3$ to $6$; section 5): the recorded free results, except $N = 688$ at $a_{4,0} = 0$, lie within 1.4% ($E_{KS}$) and 12% (the $p_0$ integral) of their large-$L$ values; the interaction effects do not: the proper zero-mode density grows toward the tip like $e^{(6H - 2m)|y|}$, the recorded $N = 8$ interaction energy is about one third of its large-$L$ value at $a_{4,0} = 0$ and about 1/22 at $a_{4,0} = 2$, and the interaction shift $E_{KS}(\pm\lambda_1) - E_{KS}(0)$ of $N = 136$ at $a_{4,0} = 2$ is at large $L$ about 51 ($+\lambda_1$, value at $L = 5.5$) and 34 ($-\lambda_1$, extrapolated) times its $L = 3$ value. The couplings (calibrated at $L = 3$) and $N = 688$ (bulk edge at $L = 3$) are themselves $L = 3$ choices.
3. The filling convention (particles on the positive branch and on the $k = 0$ zero modes; the sea not populated thermally), whose justification is OPEN; the sea-hole diagnostic shows where it fails (15 of 135 thermal states).
4. The history $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$, $A = 1$, PRESCRIBED, not solved for.
5. The parameters of section 5 ($N$, $\hat\lambda$, $L$, $\Delta k$, $v_t$, $T$).

### 15.4 Not established

1. The time-dependent (non-adiabatic) Kohn-Sham problem (TDDFT) is OPEN: only instantaneous states are computed; the measure $Q_{\max}$ is a consistency indicator, not a solution of the evolution.
2. Correlation: the functional is Hartree plus exchange only; no correlation functional is derived or used.
3. Back-reaction: the Kohn-Sham states are a test field on a prescribed background; no recorded state is an admissible source of the field equations for $a_4$ and $b_4$, and no history $a_4(x_4)$, $b_4(x_4)$ is derived from the Kohn-Sham source.
4. Equations of state and the dark-sector hypothesis are not part of this document (`Revision/dark_sector/dirac16complex`).
5. No creation process, rate or amplitude for universes follows from the Kohn-Sham model or from T3.
6. A thermal treatment of the Dirac sea (pairs) where the particle-only ensemble fails; states beyond the computed range $a_{4,0} \in [0, 2]$; the continuum limit $\Delta k \to 0$; Kohn-Sham states with extra-time momenta. The limit $L \to \infty$ is established (numerically, with uncertainties) only for the states and quantities marked converged or with a geometric tail in `Revision/kohn_sham/tip_convergence/README.md`; it is NOT established for $N = 688$ at $a_{4,0} = 0$ (the $k = 0$ bulk levels approach $m$ algebraically and the occupied set keeps changing), nor for the 6 interacting states whose successive differences of $E_{KS}$ do not meet the geometric-tail rule before the self-consistent iteration fails (it fails at some larger $L$ for 14 of the 19 studied; for $N = 8$ see section 5). It is not computed at $L \neq 3$ for $\lambda_2$, the slices 0.5 and 1.5, $T = 0.01$ and the other thermal states, the excited states and the adiabaticity measure, nor at $L > 6$. The record's calibration rule drives $\lambda_1$ to zero as $L$ grows.
