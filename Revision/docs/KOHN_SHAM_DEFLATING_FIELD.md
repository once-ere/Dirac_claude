# Kohn-Sham model of dirac16complex in the author's primordial field with the deflating extra times

## The block reduction, the instantaneous ground and first excited states along the prescribed history $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$, Mermin thermodynamics, adiabaticity, the energy-momentum tensor, the rescaling partners and the source conditions, with the verification records and an exact statement of what is computed and what is not

## Abstract

This document records the Kohn-Sham (density-functional) model of the fermion field dirac16complex in the author's primordial gravitational field, deliverable 4 of `Revision/SPEC.md` section 10, as computed by the code in `Revision/kohn_sham/`, in the corrected metric of 2026-10-16 (version 2): $g = \mathrm{diag}\big(e^{-2a_4}b_4\cot^2 z,\ e^{2a_4}\,(\times3),\ -1,\ -e^{-2a_4}b_4(\sin^2 z)^{1/6}\,(\times3)\big)$, $z = 6Hx_0$ real, with two functions $a_4(x_4)$ and $b_4(x_4) > 0$ ($b_4$ is never 1). Exact (two independent verifiers, WolframScript and sympy): in the good sector (no extra-time momentum) the ansatz $\Psi = e^{ik\cdot x}e^{-(3/2)Hy}e^{a_4/2}b_4^{-1}\chi(y,x_4)$ removes the spin-connection terms $\tfrac32(H/f)\gamma^0$ and $(b_4'/b_4 - \tfrac12a_4')\gamma^4$ and reduces the 16-component equation, for every history $a_4(x_4)$, $b_4(x_4)$, to eight $2 \times 2$ blocks $h_j = j[-(i/f)\sigma_1\,d/dy + M_{\mathrm{eff}}\sigma_2 + \kappa k\sigma_3] + v_v$ in the hidden coordinate $y = \ln|\sin z|/(6H)$, with the hidden scale $f = e^{-a_4}b_4^{1/2}$ (the hidden direction shrinks together with the extra times) and the constant momentum weight $\kappa = e^{-a_4}$; the deflation enters the instantaneous problem through $f$, through the redshift $\kappa k$ of the 3-momenta and through the proper cell volume, which grows like $e^{-a_4}b_4^2$, on the history like $e^{(5/3)a_4}$; the exact local exchange of the uniform good-sector gas gives $M_{\mathrm{eff}} = m + \frac{15}{16}\lambda S$ and $v_v = -\lambda n/16$. Computed (a Rust solver, an independent Python reference with a different discretisation, and a cross-check of the full canonical matrix, 31 of 31 checks PASS over 217571 comparisons): the instantaneous ground and first excited states of 75 parameter sets ($N = 8, 592, 2352$; five couplings $\hat\lambda$, held fixed while the cell grows, so that the effective coupling falls like $e^{-(5/3)a_{4,0}}$; five slices $a_{4,0}$ of the prescribed history $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$, $A = 1$), 135 Mermin states at three temperatures, the adiabaticity measure ($Q_{\max} \leq 0.1982205$ over the matrix), the Fermi-level crossings (none in the canonical matrix; a demonstration at $N = 2360$), the energy-momentum tensor profiles, the exact rescaling partners and the exact-exchange variant. The free states of the matrix are exact fold-band gases: their occupied levels are $\varepsilon = \kappa|k|$ with the orbital $(e^{fMy}, 0)$, so their energy redshifts exactly like $e^{-a_4}$, with $\int p_3 = E_{KS}/3$ and $\int p_0 = \int p_t = 0$. ASSUMED or chosen: both fold conditions filled at the fold $z = \pi/2$ where the two halves of a cell meet, the regular tip at $y = -3$, the filling convention. The dependence on the tip cutoff is measured ($L = 3$ to $6$): the free fold-band gases do not depend on it (except $N = 2352$ at $a_{4,0} = 0$), the interacting zero modes and the $k = 0$ bulk levels do (section 5). Not admissible as sources: no recorded Kohn-Sham state satisfies the source conditions of the $a_4$ and $b_4$ equations, so the history is a prescribed background without back-reaction. Not done: the time-dependent (non-adiabatic) Kohn-Sham problem, correlation beyond exchange, back-reaction.

## 1. The task and the answer

The author asked (2026-10-01, quoted from `Revision/README.md`): “plan and employ a DFT-motivated approximation similar to the one that you already created [...], with a Kohn-Sham fermion-gas thermodynamic effective potential, that employs the DFT ground and first-excited-state computation”. `Revision/SPEC.md` section 7 makes this precise: a Kohn-Sham fermion-gas model of dirac16complex in the good sector with the contact interaction $U = \frac{\lambda}{2}S^2$, the Hartree mean field plus the exact local exchange of the uniform gas, Mermin's finite-temperature functional, the reduction to $2 \times 2$ blocks in the hidden coordinate, the boundary conditions, the ground and first excited states, the thermodynamics, and, because $a_4$ and $b_4$ depend on $x_4$, the INSTANTANEOUS (adiabatic) Kohn-Sham states along the history with the extra times deflating, with an adiabaticity measure.

The answer of this record:

1. Exact (section 3, section 4): the block reduction, the exchange functional, the boundary conditions, the rescaling identity, the energy-momentum tensor and its conservation laws, the adiabaticity measure, all for the corrected metric. Every formula is in `Revision/kohn_sham/ks-theory.json` and verified twice, in `Revision/kohn_sham/reports/ks-theory-wolfram.json` (51 of 51 PASS) and independently in `Revision/kohn_sham/reports/ks-theory-python.json` (61 of 61 PASS).
2. Computed (sections 5 to 10): the instantaneous Kohn-Sham states of the canonical matrix by the Rust solver, independently by the Python reference, and compared state by state on the full matrix.
3. Not admissible (section 11): the recorded states are not sources of the field equations for $a_4$ and $b_4$; the history $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$ is PRESCRIBED.
4. Open (section 15): the time-dependent Kohn-Sham problem, correlation, back-reaction.

Every number below is read from the named Revision report or results file (the publication test re-reads them); units: $H = m = 1$, energies, momenta and temperatures in units of $m$, as in `Revision/kohn_sham/results/parameters.json`. Interpretations are labelled.

## 2. Setting: the author's field, the good sector and the hidden coordinate

The coordinates are the author's, $x_0, x_1, \dots, x_7$, in the author's order: $x_0$ is the hidden direction, space-like, $z = 6Hx_0$ real; $x_1, x_2, x_3$ are ordinary 3-space, inflating with the scale factor $e^{a_4}$; $x_4$ is the time; $x_5, x_6, x_7$ are the three extra times, which DEFLATE exponentially, with the scale factor $e^{-a_4}b_4^{1/2}(\sin^2 z)^{1/12}$ and $a_4$ increasing (they are never treated as static); the hidden direction has the scale factor $e^{-a_4}b_4^{1/2}|\cot z|$ and shrinks together with them. The metric of `Revision/SPEC.md` section 1 (version 2 of 2026-10-16; `Revision/metric_warped/`) is

$$
\begin{aligned}
ds^2 = {} & e^{-2a_4(x_4)}b_4(x_4)\cot^2 z\,dx_0^2 + e^{2a_4(x_4)}\big(dx_1^2+dx_2^2+dx_3^2\big) - dx_4^2 \\
& - e^{-2a_4(x_4)}\,b_4(x_4)(\sin^2 z)^{1/6}\,\big(dx_5^2+dx_6^2+dx_7^2\big) ;
\end{aligned}
$$

$b_4(x_4) > 0$ is a function of the time and never 1. The history of this record is

$$
a_4 = AHx_4,\qquad b_4 = b_4(0)\,e^{\beta AHx_4},\qquad A = 1,\quad \beta = \tfrac43 ,
$$

PRESCRIBED, not solved for: the record keeps the history of `Revision/SPEC.md` section 1 for continuity, and in the corrected metric it needs an anisotropic, $x_0$-independent source with $p_0 = p_t$ that grows with $x_4$ (`ks-theory.json`, key adiabaticity.historyBetaSource; section 11). On it the hidden scale is $f = e^{-a_4}b_4^{1/2} = e^{-a_4/3}$ ($b_4(0) = 1$).

The Kohn-Sham record uses the hidden coordinate $y = \ln|\sin z|/(6H) \in (-\infty, 0]$, with $dy = \cot z\,dx_0$, on every quarter of the period of $z$; the fold $\cos z = 0$ ($z = \pi/2$) is $y = 0$ and the tip $\sin z \to 0$ is $y \to -\infty$; the two halves $z < \pi/2$ and $z > \pi/2$ of a cell $(0, \pi)$ form the doubled system. In it the metric is exactly

$$
ds^2 = e^{2a_4}(dx_1^2+dx_2^2+dx_3^2) - dx_4^2 + f^2\big[dy^2 - e^{2Hy}(dx_5^2+dx_6^2+dx_7^2)\big],\qquad f = e^{-a_4}b_4^{1/2},
$$

with the warp $W = e^{Hy}$ on the extra times only (3-space has no warp) and $\sqrt{|g|} = e^{-a_4}b_4^2e^{3Hy}$ ($= e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}$ in the author's chart). The proper 7-volume of a coordinate cell grows like $e^{-a_4}b_4^2$, on the history like $e^{(5/3)a_4}$. The canonical spin connection gives $\gamma^\mu\Omega_\mu = \tfrac32(H/f)\gamma^0 + (b_4'/b_4 - \tfrac12a_4')\gamma^4$ for every $a_4(x_4)$, $b_4(x_4)$: the hidden direction contributes $\tfrac12h_4\gamma^4$, 3-space $\tfrac32a_4'\gamma^4$, the extra times $\tfrac32h_4\gamma^4 + \tfrac32(H/f)\gamma^0$, with $h_4 = b_4'/(2b_4) - a_4'$.

The good sector: no dependence on $x_5, x_6, x_7$ (zero extra-time momenta), a coordinate 3-torus of side $\ell$ with the momenta $k \in \Delta k\,\mathbb{Z}^3$, $\Delta k = 2\pi/\ell$, and the extra-time coordinate volume $v_t$; the proper cell volume is $\ell^3v_te^{-a_{4,0}}b_{4,0}^2$. With the fold conditions (ASSUMED filling of both) and the chosen tip condition (section 5; together they kill the $y$-current and make the blocks $h_j$ self-adjoint) the good sector is quantised in the positive realisation of the canonical quantisation of `Revision/SPEC.md` section 6; the field-theory record `Revision/docs/DIRAC16COMPLEX_FIELD_THEORY` (its section 11) constructs that realisation explicitly only for single good-sector momenta with frozen coefficients, and without a boundary condition at the degenerate points the curved good sector has complex frequencies wherever $m^2 < \tfrac94H^2e^{2a_4}/b_4$. The expectation-value rule $\langle\Psi^\dagger M\Psi\rangle = \mathrm{Tr}(M\rho)$, $\rho = \sum_{\mathrm{occ}} f\,uu^\dagger B$, defines the quasi-free (Slater or Mermin) states used here.

| item | Wolfram records | sympy records |
| --- | --- | --- |
| gammas, $C$, $B$, $\Gamma$ | `fixture_input`, `clifford_relation`, `C_B_Gamma` | `fixture_input`, `fixture_python_equals_wolfram`, `clifford_relation`, `C_B_Gamma`, `BC_and_Cg4` |
| hidden coordinate, line element, $\sqrt{\lvert g\rvert}$ | `geometry_hidden_coordinate`, `geometry_line_element`, `geometry_sqrt_det` | `geometry_hidden_coordinate`, `geometry_sqrt_det`, `geometry_line_element` |
| spin connection | `spin_connection_compatibility`, `spin_connection_slash`, `spin_connection_time_terms`, `spin_connection_slash_x0_chart` | `spin_connection_compatibility`, `spin_connection_slash`, `spin_connection_time_terms`, `spin_connection_slash_x0_chart` |

### 2.1 The corrected metric in the Kohn-Sham record

On 2026-10-16 the primordial metric was corrected (version 2; the hidden direction is space-like and carries $e^{-2a_4}b_4\cot^2 z$, 3-space carries $e^{2a_4}$ without a warp, the extra times $-e^{-2a_4}b_4(\sin^2 z)^{1/6}$, $z$ real); the metric of 2026-10-14, for which the earlier versions of this record were computed, is withdrawn. The Kohn-Sham record was recomputed for it (phase W5 of `HANDOFF.md`, 2026-10-16/17):

1. The reduction (records `ansatz_removes_spin_connection`, `ansatz_without_y_factor_term_survives`, `ansatz_without_x4_factor_term_survives`, `ansatz_norm`): the factor $e^{-(3/2)Hy}e^{a_4/2}b_4^{-1}$ of the orbitals is the half-density factor of $\sqrt{|g|}$; it removes both spin-connection terms, and the Hilbert norm of the reduced problem is $\int\chi^\dagger\chi\,dy$ for every $a_4$ and $b_4$. The hidden direction enters the block Hamiltonians through $1/f$, the 3-momenta through $\kappa = e^{-a_4}$, which does not depend on $y$ (before: $e^{-Hy - a_4}$).
2. The densities (records `ks_coupling_volume_scaling`, `history_solver_units`): a proper density is the orbital sum times $P = e^{-3Hy}/\mathrm{Vol}_7$ with $\mathrm{Vol}_7(a_{4,0}) = \ell^3v_t\,e^{(2\beta - 1)a_{4,0}} = \ell^3v_te^{(5/3)a_{4,0}}$ (the proper volume in units of $b_4(0)^2$); the solvers use the coupling $\hat\lambda = \lambda\,b_4(0)^{-2}$. A Kohn-Sham state depends on the coupling and the cell volume only through their ratio: the slice state at $(\hat\lambda, \mathrm{Vol}_7(a_{4,0}))$ is the state of the coordinate cell $\ell^3v_t$ at the effective coupling $\hat\lambda\,e^{-(5/3)a_{4,0}}$, at the same $f$ and $\kappa$.
3. The boundary conditions: the fold joins the two halves of a cell, a spinor continuous across it has the same $\chi(y)$ on both halves, and the two fold conditions $\chi_2(0) = 0$ and $\chi_1(0) = 0$ are both solved and filled (ASSUMED; section 5). The construction of the withdrawn metric, a Z2 orbifold at the patch end whose mirror copy carried $-m$, does not exist in the corrected metric.
4. The energy along the history (record `emt_energy_change_history`): $dE/da_4 = -3P_3 - 3(\beta/2 - 1)P_t - (\beta/2 - 1)P_0 = -3P_3 + P_t + \tfrac13P_0$ with $P = 2\mathrm{Vol}_7(a_{4,0})\int e^{3Hy}p\,dy$ (section 9).
5. The parameters were re-derived from the stated rules (section 5): $N = 8, 592, 2352$ and the couplings of the table there; every state of the matrix changed.

## 3. The exact block reduction

**Ansatz.** $\Psi = e^{ik\cdot x}e^{-(3/2)Hy}e^{a_4/2}b_4^{-1}\chi(y,x_4)$ gives EXACTLY, for a time-dependent $a_4$ and $b_4$,

$$
\tfrac1f\gamma^0\partial_y\chi + \gamma^4\partial_{x_4}\chi + i\kappa\,k\cdot\gamma\,\chi = (M_{\mathrm{eff}} - iv_v\gamma^4)\chi ,\qquad \kappa(x_4) = e^{-a_4(x_4)},\qquad f(x_4) = e^{-a_4}b_4^{1/2} ,
$$

i.e. $i\partial_{x_4}\chi = h(x_4)\chi$ with $h$ Hermitian in $\int dy\,\chi^\dagger\chi$. The factor $e^{-(3/2)Hy}$ removes the term $\tfrac32(H/f)\gamma^0$ and the factor $e^{a_4/2}b_4^{-1}$ the term $(b_4'/b_4 - \tfrac12a_4')\gamma^4$; without either the term survives. At a fixed instant the instantaneous (adiabatic) problem is $h(a_{4,0}, f_0)\chi = \varepsilon\chi$ with $a_{4,0} = a_4(x_4)$ and $f_0 = f(x_4)$.

**Blocks.** $J = \gamma^0\gamma^1\gamma^4$ ($J^2 = 1$), $K_1 = \gamma^2\gamma^3$ and $K_2 = \gamma^5\gamma^6$ ($K^2 = -1$) commute with each other and with $\gamma^0$, $\gamma^0\gamma^1$, $\gamma^0\gamma^4$, $B$ and $C$; their joint eigenspaces, labelled $(j, s_2, s_3)$ with $j, s_2, s_3 = \pm1$, are eight rank-2 blocks with an explicit unitary basis $V$ (entries of $2\sqrt2\,V$ in $\{0, \pm1, \pm i\}$). For $k$ along $x_1$ (the spinor rotation commutes with $\gamma^0$, $\gamma^4$, $B$, $C$, so the spectra depend on $|k|$ only), every block of type $j$ carries

$$
h_j = j\big[-\tfrac{i}{f}\sigma_1\,\tfrac{d}{dy} + M_{\mathrm{eff}}(y)\sigma_2 + \kappa k\sigma_3\big] + v_v(y) ,
$$

equivalently $\chi' = fN\chi$ with $N = M_{\mathrm{eff}}\sigma_3 - \kappa k\sigma_2 + ij(\varepsilon - v_v)\sigma_1$; in the real form $\chi = (a, ib)$, $a' = f[M_{\mathrm{eff}}a - (\kappa k + j(\varepsilon - v_v))b]$ and $b' = f[(j(\varepsilon - v_v) - \kappa k)a - M_{\mathrm{eff}}b]$. In the block basis $\gamma^0 = \sigma_3$, $B = js_2$ and $C = s_2\sigma_2$.

**Symmetries and degeneracies.** $h_{-1} - v = -(h_{+1} - v)$ and $\sigma_3h_j(k)\sigma_3 = h_{-j}(-k)$: the $(j,k)$ and $(-j,-k)$ orbitals are degenerate. On a lattice shell $|k|^2 = \Delta k^2n_2$ with $r_3(n_2)$ vectors every level of $h_j(|k|)$ is $4r_3(n_2)$-fold for each $j$; at $k = 0$ every level is 4-fold per $j$. The chirality $\Gamma$ maps block $(j, s_2, s_3)$ onto $(-j, s_2, s_3)$ with the $2 \times 2$ entry $s_2\sigma_2$, and $\sigma_2h_j(M,k)\sigma_2 = h_{-j}(-M,k)$ with the two fold conditions exchanged (the ingredient of T3, section 12).

**Where the deflation enters (exact).** $a_{4,0}$ and $b_{4,0}$ enter $h_j$ through $\kappa k = ke^{-a_{4,0}}$ (the 3-momenta redshift as $ke^{-a_4}$) and through the hidden scale $f_0 = e^{-a_{4,0}}b_{4,0}^{1/2}$, which multiplies the hidden derivative by $1/f_0$ (the proper hidden length of the cut-off cell is $f_0L$); because the good sector has no extra-time momentum, the extra times themselves enter only through the proper cell volume, that is through the densities and the mean field (sections 2.1 and 10).

| item | Wolfram records | sympy records |
| --- | --- | --- |
| ansatz and Hamiltonian | `ansatz_removes_spin_connection`, `ansatz_without_y_factor_term_survives`, `ansatz_without_x4_factor_term_survives`, `ansatz_norm`, `hamiltonian_16_hermitian` | `ansatz_removes_spin_connection`, `ansatz_without_y_factor_term_survives`, `ansatz_without_x4_factor_term_survives`, `ansatz_norm`, `hamiltonian_16_hermitian` |
| blocks | `blocks_commuting_set`, `blocks_basis_unitary`, `blocks_forms`, `blocks_relation_to_Gamma`, `block_hamiltonian`, `block_ode_equivalent` | `blocks_commuting_set`, `blocks_projectors`, `blocks_basis_unitary`, `blocks_forms`, `blocks_not_everything_block_diagonal`, `blocks_relation_to_Gamma`, `block_hamiltonian`, `block_ode_equivalent` |
| symmetries | `block_type_relation`, `block_Gamma_map`, `rotation_invariance` | `block_type_relation`, `block_Gamma_map`, `rotation_invariance` |
| solver (numerical basis) | | `theory_input_metric_forms`, `block_reduction_numeric`, `gamma_fixture_numeric` (Rust solver report) |

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

**Exact Fock exchange of the slab (diagnostic and variant).** For closed shells the exact Fock exchange of the Kohn-Sham determinant is also local, $e_x^{\mathrm{exact}} = -\frac{\lambda}{32}(n^2 + S^2 - Q^2 - Y^2)$ with $Q = \langle\Psi^\dagger B\gamma^0\Psi\rangle$ and $Y = 0$; the canonical functional is the uniform-gas one, the difference $\Delta E_x = \frac{\lambda}{32}\,2\mathrm{Vol}_7\int e^{3Hy}Q^2\,dy$ is reported for every state, and the exact-Fock functional is solved as a variant (60 states, `Revision/kohn_sham/results/exx/exact-fock-variant.csv`).

**Densities, energy, Mermin.** Per orbital, with $P(y) = e^{-3Hy}/\mathrm{Vol}_7(a_{4,0})$: $n_o = P\chi^\dagger\chi$, $s_o = P\chi^\dagger j\sigma_2\chi$, $t_o = P\chi^\dagger j\sigma_3\chi$, $q_o = P\chi^\dagger\sigma_3\chi$. Totals are $\sum w\,g\,f$ times these, $g = 4r_3(n_2)$, $w = 1/2$ (section 5). The Kohn-Sham energy of the doubled system is $E_{KS} = \sum g f\varepsilon - 2\mathrm{Vol}_7\int_{-L}^{0}e^{3Hy}e_{\mathrm{int}}\,dy$; Mermin's occupations are $f = 1/(1 + e^{(\varepsilon-\mu)/T})$ with $\mu$ fixed by $\sum g f = N$, the entropy is $S_{\mathrm{ent}} = -\sum g[f\ln f + (1-f)\ln(1-f)]$, the grand potential (the thermodynamic effective potential) is $\Omega = -T\sum g\ln(1 + e^{-(\varepsilon-\mu)/T}) - 2\mathrm{Vol}_7\int_{-L}^{0}e^{3Hy}e_{\mathrm{int}}\,dy$, and $F = \Omega + \mu N$.

Discrepancy recorded, not hidden: the line “mu fixed by sum w g f = N” of `ks-theory.json` is inconsistent with its own densities, energy and grand potential; the solver and the reference use $\sum g f = N$, and `Revision/kohn_sham/results/parameters.json` records the discrepancy.

| item | Wolfram records | sympy records |
| --- | --- | --- |
| uniform gas and exchange | `gas_mode_projector`, `gas_angular_average`, `gas_densities`, `exchange_uniform_gas` | `gas_mode_projector`, `gas_angular_average`, `gas_negative_energy_modes`, `gas_densities`, `hf_wick_contraction`, `exchange_uniform_gas`, `filled_shell_ratio` |
| Kohn-Sham potentials | `ks_potentials`, `ks_onshell_lagrangian` | `ks_potentials`, `ks_onshell_lagrangian`, `ks_theory_json_exchange` |
| coupling, cell volume and history | `ks_coupling_volume_scaling`, `history_solver_units` | `ks_coupling_volume_scaling`, `history_solver_units` |
| exact Fock exchange of the slab | `exchange_slab_exact_fock` | `exchange_slab_exact_fock` |

## 5. Boundary conditions, filling convention, numerics and parameters

**Fold (both fold conditions filled, ASSUMED).** The fold $\cos z = 0$ at $y = 0$ joins the two halves of a cell; the reduced equation is the same on both halves ($dy = \cot z\,dx_0$, $e^{x_0}dx_0 = f\,dy$, $\gamma^\mu\Omega_\mu$ free of $x_0$), so a spinor continuous across the fold has the same $\chi(y)$ on both halves; the boundary form of the doubled cell at the fold is $2(-ij/f)\phi^\dagger\sigma_1\chi(0)$, and self-adjointness needs $(1 - Q(\theta))\chi(0) = 0$. The record fills both fold conditions, the even $\theta = 0$ ($\chi_2(0) = 0$, $b(0) = 0$) and the odd $\theta = \pi$ ($\chi_1(0) = 0$, $a(0) = 0$), each normalised on one half; $N$ is the particle number of the whole cell, each half holds $N/2$, and $w = 1/2$ per half. That both are filled is ASSUMED (the record's convention); there is no mirror copy.

**Tip (chosen).** At $y = -L$: $(1 - Q(\theta))\chi(-L) = 0$, $Q(\theta) = \cos\theta\,\sigma_3 + \sin\theta\,\sigma_2$, canonical $\theta = 0$, cutoff $L = 3$. With $\kappa$ independent of $y$ nothing suppresses an orbital toward the tip: for constant $M$ and $v$ the branches are $e^{\pm f\lambda y}$, $\lambda = \sqrt{M^2 + \kappa^2k^2 - (\varepsilon - v)^2}$. The dependence on $L$ is measured in `Revision/kohn_sham/tip_convergence/` ($L = 3$ to $6$ in steps of $0.5$ with the record's step $h = 1/300$, every run repeated at $h/2$; a copy of the solver that reads $L$ from the environment reproduces the committed quick matrix byte for byte at $L = 3$; the reference solver agrees at $L = 3$ and $4$; report `Revision/kohn_sham/tip_convergence/tip-convergence.json`, 7 of 7 checks PASS; rerun for the corrected metric on 2026-10-17). The free states are exact fold-band gases and do not depend on $L$: $E_{KS}$, HOMO, LUMO and the gap of every free state with $N = 8$ and $592$ and of $N = 2352$ at $a_{4,0} = 1, 2$ are the same at every $L$; only the values at the fold change, through the normalisation of the fold-band orbital, $\rho(0; L) = \rho(0; \infty)/(1 - e^{-2fmL})$ (the recorded $L = 3$ fold values are high by 0.25%, 1.38% and 4.81% at $a_{4,0} = 0, 1, 2$). The $k = 0$ bulk levels approach $m$ only algebraically, like the levels of a box of proper length $fL$: the bulk edge 1.2923 that defines $N = 2352$ is an $L = 3$ value (1.0977 at $L = 6$), and the free $N = 2352$, $a_{4,0} = 0$ state changes its occupied set from $L = 3.5$ on (its gap 0.01754 closes; $E_{KS} = 2288.388$ at $L = 3$ and $2245.486$ at $L = 6$, not converged). The interacting zero modes depend on $L$, the more the later the slice: their proper density grows toward the tip like $e^{(3H - 2fm)|y|}$, and for $N = 8$ the recorded $E_{KS}$ is $\mp 3.7787\times10^{-2}$ against $\mp 3.8688\times10^{-2}$ at large $L$ at $a_{4,0} = 0$, $\mp 1.4571\times10^{-2}$ against $\mp 2.1622\times10^{-2}$ at $a_{4,0} = 1$ and $\mp 6.980\times10^{-3}$ against $\mp 3.239\times10^{-2}$ at $a_{4,0} = 2$ ($\hat\lambda = \pm\lambda_1$; 0.977, 0.674 and 0.215 of the large-$L$ values); the interaction shifts $E_{KS}(\pm\lambda_1) - E_{KS}(0)$ of $N = 592$ and $2352$ at $a_{4,0} = 2$ are 4.6 to 4.7 times larger at large $L$ than at $L = 3$. 17 of the 19 interacting states studied converge (geometric tails); the self-consistent iteration fails only for $N = 2352$ at $a_{4,0} = 0$, from $L = 3.5$ for $+\lambda_1$ and from $L = 4.5$ for $-\lambda_1$ (a failure of the iteration, not a proof that no self-consistent state exists). The record's calibration rule applied at each $L$ drives $\lambda_1$ to zero: $157.7$, $2.131$ and $0.5363$ at $L = 3$, $1.249$, $0.01687$ and $1.03\times10^{-5}$ at $L = 6$ ($N = 8, 592, 2352$).

**Exact $k = 0$ spectra.** For constant $M > 0$, $v = 0$, $\theta = 0$: the even fold condition has $\varepsilon = 0$ with the fold zero mode $\chi = (e^{fMy}, 0)$, and $\varepsilon = \pm\sqrt{M^2 + (n\pi/(fL))^2}$; the odd fold condition has $\varepsilon = \pm\sqrt{M^2 + p^2}$ with $\tan(pfL) = -p/M$. The even $j = +1$ fold band is $\varepsilon = \kappa k$ EXACTLY for every $k$, with the orbital $(e^{fMy}, 0)$ (record `free_rescaling_relation_and_band_monotone`); its slope is $c = e^{-a_{4,0}}$ for every $M$, $L$ and $f$ (record `brane_band_slope`; the record keeps the name of the earlier construction).

**Filling (CONVENTION, justification OPEN).** Particles occupy the positive branch (the levels with $\varepsilon > 0$ of the $\lambda = 0$ problem) and the $k = 0$ fold zero modes, each followed continuously in $\lambda$; the negative branch is the normal-ordered sea and contributes nothing to $N$, $n$, $S$ or the energy-momentum tensor. The excluded thermal sea holes are reported as a diagnostic (section 8).

**Numerics.** The Rust solver (`Revision/kohn_sham/solver`, own crate, no external crates) solves each block by shooting with RK4 on 900 steps, Pruefer counting and a root tolerance of 1e-13, Anderson-mixed SCF to 1e-11; when the direct iteration diverges it falls back to a continuation in the coupling ($\hat\lambda \times \frac14, \frac12, \frac34, 1$ with half the mixing). The independent Python reference (`Revision/kohn_sham/reference`) uses a staggered finite-difference discretisation on three grids (300, 600, 1200) with Richardson extrapolation and a stated uncertainty, validated on a fourth grid, with its own continuation fallback; its convergence order is two (record `free_convergence_order_two`).

**Parameters** (`Revision/kohn_sham/results/parameters.json`): $H = m = 1$, $L = 3$, $\Delta k = 0.25$, $v_t = 1$, $\mathrm{Vol}_7(0) = 15875.21366031351$ and $\mathrm{Vol}_7(a_{4,0}) = \mathrm{Vol}_7(0)\,e^{(5/3)a_{4,0}}$, tip $\theta = 0$, history $A = 1$, $\beta = 4/3$, slices $a_{4,0} \in \{0, 0.5, 1, 1.5, 2\}$, temperatures $T \in \{0.01, 0.02, 0.05\}$. Particle numbers: $N = 8$ (the $k = 0$ fold zero modes of both block types), $N = 2352$ (the largest closed shell of the free $a_{4,0} = 0$ aufbau whose last level lies below the bulk edge 1.292292828068783, the lowest level not on the even $j = +1$ fold band) and $N = 592$ (the closed shell nearest $2352/4$). Couplings: $\lambda_1$ and $\lambda_2$ (values of $\hat\lambda$) keep the first-order mean-field potential below 0.1 and 0.3 (units of $m$) along the whole history; the strength is the largest first-order potential per unit $\hat\lambda$ over the five slices, with the densities per $\mathrm{Vol}_7(a_{4,0})$:

| N | strength per unit lambda_hat | lambda_1 | lambda_2 |
| --- | --- | --- | --- |
| 8 | 0.0006341788 | 157.7 | 473.1 |
| 592 | 0.04692923 | 2.131 | 6.393 |
| 2352 | 0.1864486 | 0.5363 | 1.609 |

The canonical matrix holds 75 ground states ($3$ values of $N$, the five couplings $0, \pm\lambda_1, \pm\lambda_2$, five slices), each with its first excited state, its $a_4$ neighbours, its rescaling partner and, for $\lambda \neq 0$, its exact-Fock variant, and 135 Mermin states ($\hat\lambda \in \{0, \pm\lambda_1\}$, three temperatures).

| item | records |
| --- | --- |
| boundary conditions (Wolfram and sympy) | `bc_fold_same_equation_on_both_halves`, `bc_fold_conditions`, `bc_self_adjoint_boundary_term`, `bc_tip_family`, `bc_current_conserved_along_y`, `bc_exact_k0_spectra`, `bc_tip_asymptotics`, `brane_band_slope` |
| free problem (Rust solver) | `free_k0_analytic_spectra`, `free_zero_mode_exact`, `free_brane_band_slope`, `free_block_type_symmetries`, `free_particle_branch_labels`, `free_tip_angle_boundary_identity` |
| free problem and parameters (reference) | `free_k0_analytic_spectra`, `free_convergence_order_two`, `free_k0_block_type_symmetry`, `free_zero_mode`, `free_brane_band_slope`, `free_particle_branch`, `parameters_closed_shells`, `parameters_calibration`, `richardson_asymptotic_ratio`, `richardson_uncertainty_validated` |
| parameters (cross-check) | `problem_definition_identical`, `parameters_particle_numbers`, `parameters_couplings` |

## 6. Instantaneous ground and first excited states along the prescribed history

The history is $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$ with $A = 1$ (the exponentially deflating member: the scale factor of the extra times is $b_4(0)^{1/2}e^{-Hx_4/3}(\sin^2 z)^{1/12}$), PRESCRIBED, not solved for (section 11). At every slice $a_{4,0}$ the ground state is the self-consistent aufbau state of the instantaneous problem; the first excited state is computed three ways: the Kohn-Sham gap $\varepsilon_{\mathrm{LUMO}} - \varepsilon_{\mathrm{HOMO}}$; the ensemble $\Delta$-SCF energy (one particle moved from the highest occupied degenerate group to the lowest empty group, spread uniformly over each group, self-consistent); and the list of the 24 lowest particle-hole excitations (`Revision/kohn_sham/results/excited/particle-hole/`). Every ground state of the matrix is closed-shell.

Ground and first excited states for $N = 592$ (`Revision/kohn_sham/results/ground/summary.csv` and `Revision/kohn_sham/results/excited/summary.csv`):

| lambda_hat | a4,0 | E_KS | KS gap | Delta-SCF |
| --- | --- | --- | --- | --- |
| 0 | 0 | 361.1161 | 0.03858678 | 0.03858678 |
| 0 | 1 | 132.8472 | 0.01419528 | 0.01419528 |
| 0 | 2 | 48.87176 | 0.005222153 | 0.005222153 |
| 2.131 | 0 | 358.301 | 0.03858459 | 0.03858459 |
| 2.131 | 1 | 131.7652 | 0.01419487 | 0.01419487 |
| 2.131 | 2 | 48.35502 | 0.005222125 | 0.005222125 |
| -2.131 | 0 | 363.8955 | 0.03858511 | 0.03858511 |
| -2.131 | 1 | 133.9218 | 0.01419489 | 0.01419489 |
| -2.131 | 2 | 49.38796 | 0.005222125 | 0.005222125 |
| 6.393 | 0 | 352.798 | 0.03857391 | 0.03857391 |
| 6.393 | 1 | 129.6573 | 0.01419216 | 0.01419216 |
| 6.393 | 2 | 47.3264 | 0.005221902 | 0.005221903 |
| -6.393 | 0 | 369.2418 | 0.03857847 | 0.03857847 |
| -6.393 | 1 | 135.982 | 0.0141925 | 0.0141925 |
| -6.393 | 2 | 50.41245 | 0.005221906 | 0.005221906 |

The free Kohn-Sham gap along the history ($\lambda = 0$, `ground/summary.csv`):

| N | a4,0 = 0 | a4,0 = 0.5 | a4,0 = 1 | a4,0 = 1.5 | a4,0 = 2 |
| --- | --- | --- | --- | --- | --- |
| 8 | 0.25 | 0.1516327 | 0.09196986 | 0.05578254 | 0.03383382 |
| 592 | 0.03858678 | 0.02340407 | 0.01419528 | 0.008609875 | 0.005222153 |
| 2352 | 0.01753795 | 0.01472852 | 0.0089333 | 0.00541832 | 0.003286377 |

Reading (labelled interpretation of these numbers): the free ground states occupy the fold band $\varepsilon = \kappa|k|$ and the $k = 0$ zero modes, so as the extra times deflate the 3-momenta redshift as $ke^{-a_{4,0}}$ and the occupied free levels redshift with them: the free energies of $N = 592$ and $2352$ fall exactly like $e^{-a_{4,0}}$, the Kohn-Sham gap of $N = 8$ is $\kappa\Delta k = 0.25\,e^{-a_{4,0}}$ and that of $N = 592$ falls like $e^{-a_{4,0}}$; for $N = 2352$ the lowest empty level at $a_{4,0} = 0$ is the bulk edge (by the choice of $N$), and from $a_{4,0} = 0.5$ on, where the $k = 0$ bulk levels have risen above it, the next fold-band shell, so its gap falls like $e^{-a_{4,0}}$ from there; with interaction the energy changes also with the effective coupling $\hat\lambda e^{-(5/3)a_{4,0}}$. With $\lambda = 0$ the $\Delta$-SCF energy equals the Kohn-Sham gap (worst difference 3.086e-13 over 15 cases, record `excited_delta_scf_free_equals_gap`); with interaction the two differ slightly, because the $\Delta$-SCF state relaxes the mean field self-consistently.

| item | Rust solver records | reference records | cross-check records |
| --- | --- | --- | --- |
| ground states | `ground_runs_completed`, `ground_scf_converged`, `ground_closed_shell`, `ground_window_complete`, `ground_N_conservation`, `ground_energy_two_forms`, `ground_orbital_boundary_conditions` | `ground_scf_converged`, `ground_a4_neighbours_tight`, `ground_grid_consistency`, `ground_closed_shell`, `ground_window_complete`, `ground_N_conservation`, `ground_energy_two_forms` | `ground_occupations_and_groups`, `ground_energies`, `ground_homo_lumo_gap`, `ground_eigenvalues`, `ground_profiles` |
| first excited state | `excited_delta_scf_free_equals_gap`, `excited_scf_converged` | `excited_delta_scf_free_equals_gap`, `excited_particle_hole_lowest_is_gap` | `excited_delta_scf`, `excited_particle_hole_lists` |
| exact-Fock variant | `exx_variant_scf_converged`, `exx_variant_y_conservation`, `exx_variant_occupation_order` | `exx_scf_converged`, `exx_N_conservation`, `exx_energy_two_forms`, `exx_emt_energy_integral`, `exx_y_conservation_integrated` | `exchange_delta_E_x`, `exx_variant_scf` |
| SCF path (information) | `thermo_scf_path` | `scf_paths` | |

## 7. Adiabaticity and Fermi-level crossings

Exactly (mean field), $i\partial_{x_4}\chi = h(a_4(x_4), f(x_4))\chi$ conserves $k$, the block and the fold condition; transitions occur only between levels of the same $(k, j, \text{block}, \text{fold condition})$. The measure along $a_4 = AHx_4$ is

$$
\begin{aligned}
Q_{nm} &= AH\,\frac{\lvert\langle n\rvert\partial_ah\lvert m\rangle\rvert}{(\varepsilon_n - \varepsilon_m)^2} = AH\,\frac{\lvert\langle n\vert\partial_am\rangle\rvert}{\lvert\varepsilon_n - \varepsilon_m\rvert},\\
\partial_ah_j &= -j\kappa k\sigma_3 + \big(1 - \tfrac{\beta}{2}\big)\,j\big(-\tfrac{i}{f}\sigma_1\partial_y\big) + j(\partial_aM_{\mathrm{eff}})\sigma_2 + \partial_av_v ,
\end{aligned}
$$

for $n$ occupied and $m$ empty in the same sector (the second term, one third of the kinetic term, comes from the shrinking hidden direction); the state is adiabatic if $\max Q_{nm} \ll 1$, and $Q_{nm}^2$ is the leading-order transition probability. The self-consistent derivatives come from the states at $a_{4,0} \pm \delta$, $\pm 2\delta$ ($\delta = 2\times10^{-3}$, Richardson); they contain the change of the effective coupling $\hat\lambda/\mathrm{Vol}_7(a_{4,0})$ along the history. Hellmann-Feynman, $d\varepsilon_n/da = \langle n\rvert\partial_ah\lvert n\rangle$, is checked in 75 cases (worst 6.444e-11, record `adiabatic_hellmann_feynman`).

Results (`Revision/kohn_sham/results/adiabatic/adiabaticity.csv`): because the hidden direction shrinks, $Q_{\max}$ is not zero even for $N = 8$ at $\lambda = 0$ (state N8_lam0_a00: 0.06814928); over the $N = 8$ states the largest value is $Q_{\max} \leq 0.07273792$ (state N8_lamp2_a00, pair `0:-1:even:0 -> 0:-1:even:1`). The largest value over the whole matrix is 0.1982205 (state N2352_lamm1_a00, pair `26:+1:even:0 -> 26:+1:even:1`: two levels of the same shell, block type and fold condition). For $\lambda = 0$:

| N | a4,0 | Q_max | delta eps of the pair | dE/da4 (EMT) | dE/da4 (differences) |
| --- | --- | --- | --- | --- | --- |
| 592 | 0 | 0.1396883 | 0.8591647 | -361.1161 | -361.1161 |
| 592 | 0.5 | 0.09450268 | 1.181936 | -219.028 | -219.028 |
| 592 | 1 | 0.06819305 | 1.503745 | -132.8472 | -132.8472 |
| 592 | 1.5 | 0.05108696 | 1.826609 | -80.5759 | -80.5759 |
| 592 | 2 | 0.03879691 | 2.167139 | -48.87176 | -48.87176 |
| 2352 | 0 | 0.194329 | 0.6543959 | -2288.388 | -2288.388 |
| 2352 | 0.5 | 0.11849 | 0.9955121 | -1387.978 | -1387.978 |
| 2352 | 1 | 0.0782197 | 1.362942 | -841.851 | -841.851 |
| 2352 | 1.5 | 0.05520876 | 1.730963 | -510.6084 | -510.6084 |
| 2352 | 2 | 0.04047331 | 2.105635 | -309.6997 | -309.6997 |

The last two columns are the energy change along the history, from the energy-momentum tensor ($dE/da_4 = -3P_3 + P_t + \tfrac13P_0$, $P = 2\mathrm{Vol}_7(a_{4,0})\int e^{3Hy}p\,dy$, section 9) and from finite differences at fixed occupations; for the free fold-band gases both equal $-E_{KS}$.

**Fermi-level crossings.** When levels of different $k$ cross the Fermi level between slices, the instantaneous aufbau ground state differs from the adiabatically continued state, and the solver flags it. No crossing occurs in the canonical matrix: every one of the 15 series of `Revision/kohn_sham/results/adiabatic/history.json` has an empty crossing list, and `adiabatic/fermi-level-crossings.csv` records no change of the occupied set. A demonstration at $\lambda = 0$ and $N = 2360$ (the smallest closed shell of the $a_{4,0} = 0$ aufbau that occupies a level off the even $j = +1$ fold band; `adiabatic/crossing-demo.csv`):

| a4,0 | occupied set as at a4,0 = 0 | open shell | E aufbau | E adiabatically continued | difference |
| --- | --- | --- | --- | --- | --- |
| 0 | true | false | 2298.727 | 2298.727 | 0 |
| 0.5 | false | true | 1394.281 | 1398.957 | 4.676354 |
| 1 | false | true | 845.6741 | 853.6174 | 7.943281 |
| 1.5 | false | true | 512.9273 | 523.3331 | 10.40583 |
| 2 | false | true | 311.1061 | 323.5841 | 12.47799 |

From $a_{4,0} = 0.5$ on, the fold-band levels redshift ($\varepsilon = e^{-a_4}k$) while the $k = 0$ bulk levels rise ($\varepsilon = \sqrt{M^2 + (n\pi/(fL))^2}$, $f = e^{-a_4/3}$): the instantaneous ground state is not the adiabatically reached state, which lies above it by the last column.

Interpretation (labelled): with $Q_{\max} \leq 0.1982205$ the instantaneous states are self-consistently adiabatic for the same-sector transitions at the rate $A = 1$ in the canonical matrix only in the weak sense $Q_{\max} < 1$; the largest values approach 0.2 for $N = 2352$ at $a_{4,0} = 0$. This does not solve the time-dependent problem (OPEN), and where Fermi-level crossings occur (the demonstration) the instantaneous ground state is not the state that the evolution reaches.

| Rust solver records | reference records | cross-check records |
| --- | --- | --- |
| `adiabatic_hellmann_feynman`, `adiabatic_crossing_flag_demonstration` | `adiabatic_hellmann_feynman_discrete`, `crossing_demo_reference` | `adiabatic_dE_da4`, `adiabatic_Q_max`, `crossing_demonstration` |

## 8. Mermin thermodynamics

The Mermin states at $T = 0.01, 0.02, 0.05$ solve the self-consistent problem at fixed $N$ with $\mu$ the root of $\sum g f = N$ in a well-conditioned form (thermal particles above and holes below a split of the levels, `solver/src/mermin.rs`). The checks: $\Omega$ in its two forms, $-dF/dT = S_{\mathrm{ent}}$, $C_V = T\,dS_{\mathrm{ent}}/dT = dE/dT$ at fixed $N$, and the chemical potential against 40-digit roots on the solver's own final levels (40-digit and 50-digit roots agree to 1.5e-38, record `root_precision_self_check`). For $N = 592$, $\lambda = 0$ (`Revision/kohn_sham/results/thermo/thermodynamics.csv`):

| a4,0 | T | mu | E | entropy | Omega | sea holes / N |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0.01 | 0.8099438 | 361.6116 | 76.01079 | -118.6352 | 3.76e-48 |
| 0 | 0.02 | 0.8110736 | 362.7433 | 152.6427 | -120.4652 | 3.73e-25 |
| 0 | 0.05 | 0.8078443 | 369.9279 | 358.7396 | -126.2529 | 3.43e-11 |
| 2 | 0.01 | 0.1078013 | 51.39934 | 517.9789 | -17.59884 | 5e-08 |
| 2 | 0.02 | 0.09893307 | 58.47195 | 991.924 | -19.93491 | 0.000221 |
| 2 | 0.05 | 0.03959481 | 96.58455 | 2112.111 | -32.46113 | 0.234 |

**Validity of the particle-only ensemble (diagnostic of the CONVENTION).** For every thermal state the number of thermal holes that the excluded sea fold band would carry at the same $\mu$ and $T$ is computed. It exceeds 1% of $N$ in 27 of 135 states, most of them at $N = 8$ and all at $a_{4,0} \geq 0.5$; the largest is 594.496 N (record `thermo_sea_hole_diagnostic_computed`). There the particle-only Mermin ensemble is outside its range of validity and a thermal treatment of the sea (pairs) would be required; in the table above this is the row $a_{4,0} = 2$, $T = 0.05$ (state N592_lam0_a20_T50).

| Rust solver records | reference records | cross-check records |
| --- | --- | --- |
| `thermo_runs_completed`, `thermo_scf_converged`, `thermo_N_conservation`, `thermo_grand_potential_two_forms`, `thermo_entropy_identity`, `thermo_CV_identity`, `thermo_window_cut`, `thermo_window_shells_beyond`, `thermo_mu_well_conditioned_root`, `thermo_mu_vs_40digit_roots`, `thermo_sea_hole_diagnostic_computed`, `thermo_scf_path` | `thermo_scf_converged`, `thermo_N_conservation`, `thermo_grand_potential_two_forms`, `thermo_CV_identity`, `thermo_entropy_identity`, `thermo_window_cut`, `thermo_sea_holes_tail`, `scf_paths` | `thermo_state_functions`, `thermo_derivatives`, `thermo_sea_hole_diagnostic`, `thermo_levels`, `thermo_mu_high_precision`, `thermo_mu_rounding_diagnostic`, `thermo_mu_rust_stated_bound` |

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

with $T^{x_4}{}_y = 0$ for eigen-orbitals. The extra-time pressure $p_t$ has no kinetic part (good sector). Exact identities, checked for every state: the trace of the kinetic parts is $M_{\mathrm{eff}}S + v_vn$; conservation along the hidden direction, $p_0' + 3H(p_0 - p_t) = 0$; the energy change $\nabla_\mu T^\mu{}_{x_4} = -\partial_{x_4}\rho - 3a_4'(\rho + p_3) - 3h_4(\rho + p_t) - h_4(\rho + p_0)$, i.e. on the history $dE/da_4 = -3P_3 + P_t + \tfrac13P_0$ with $P = 2\mathrm{Vol}_7(a_{4,0})\int_{-L}^{0}e^{3Hy}p\,dy$; and $2\mathrm{Vol}_7\int e^{3Hy}\rho\,dy = E_{KS}$. Integrated profiles ($2\mathrm{Vol}_7(a_{4,0})\int_{-L}^{0}e^{3Hy}X\,dy$, `Revision/kohn_sham/results/ground/emt-integrals.csv`), $\lambda = 0$:

| N | a4,0 | int rho | int p3 | int p_t | int p0 |
| --- | --- | --- | --- | --- | --- |
| 592 | 0 | 361.1161 | 120.372 | 0 | 0 |
| 592 | 0.5 | 219.028 | 73.00934 | 0 | -9.693924e-17 |
| 592 | 1 | 132.8472 | 44.2824 | 0 | -6.658418e-16 |
| 592 | 1.5 | 80.5759 | 26.85863 | 0 | -1.115453e-15 |
| 592 | 2 | 48.87176 | 16.29059 | 0 | 0 |
| 2352 | 0 | 2288.388 | 762.7961 | 0 | 0 |
| 2352 | 0.5 | 1387.978 | 462.6592 | 0 | 3.00941e-14 |
| 2352 | 1 | 841.851 | 280.617 | 0 | -7.850057e-16 |
| 2352 | 1.5 | 510.6084 | 170.2028 | 0 | -6.395636e-17 |
| 2352 | 2 | 309.6997 | 103.2332 | 0 | 4.739727e-16 |

For a fold-band orbital $(e^{fMy}, 0)$ with $\varepsilon = \kappa|k|$ the hidden-direction kinetic pressure vanishes identically, so the free states have $p_0 = p_t = 0$ (the table shows rounding values) and $\int p_3 = E_{KS}/3$: a radiation-like gas of the 3-space momenta, whose energy falls like $e^{-a_4}$ ($dE/da_4 = -E_{KS}$, section 7). The profiles on 151 points $y = -3 + 0.02i$ are in `Revision/kohn_sham/results/ground/profiles/` (one file per state; densities per $\mathrm{Vol}_7(a_{4,0})$, that is the proper densities times $b_4(0)^2$). The energy density varies along the hidden direction in every state with a nonzero tensor (section 11). Equations of state seen by a 3-space observer are not part of this document; they are the work of `Revision/dark_sector/dirac16complex` (its Kohn-Sham history report `Revision/dark_sector/dirac16complex/reports/ks-history-run.json`: 8 of 8 PASS).

| item | Wolfram and sympy records | Rust solver records | reference and cross-check records |
| --- | --- | --- | --- |
| tensor and identities | `emt_orbital_components`, `emt_trace_identity`, `emt_y_conservation_orbital`, `emt_y_conservation_selfconsistent`, `emt_x4_component`, `emt_energy_change_history` | `emt_energy_integral`, `emt_trace_derivative_form`, `emt_y_conservation_integrated`, `emt_y_conservation_pointwise`, `emt_energy_change_dE_da4` | `emt_energy_integral`, `emt_y_conservation_integrated`, `emt_energy_change_dE_da4`, `emt_integrals`, `emt_brane_tip_values` |

## 10. The rescaling partners

**Exact identity.** With the proper hidden coordinate $Y = f_0y$, $f_0 = e^{-a_{4,0}}b_{4,0}^{1/2}$,

$$
\mathrm{KS}(a_{4,0}, b_{4,0};\,H, L, \Delta k, v_t, \lambda, N, T) = \mathrm{KS}\big(0, 1;\,H/f_0,\, f_0L,\, \Delta k\,e^{-a_{4,0}},\, v_t\,e^{-3a_{4,0}}b_{4,0}^{3/2},\, \lambda, N, T\big)
$$

for the levels, orbitals ($\chi_Y = \chi/\sqrt{f_0}$), proper densities and energy-momentum profiles; on the history ($b_{4,0} = e^{(4/3)a_{4,0}}$, $f_0 = e^{-a_{4,0}/3}$) the partner has $H e^{a_{4,0}/3}$, $Le^{-a_{4,0}/3}$, $\Delta k\,e^{-a_{4,0}}$ and $v_t\,e^{-a_{4,0}}$ at the same $\hat\lambda$. Reading (labelled): the slice $a_{4,0}$ of the deflating history is the slice 0 with a 3-torus larger by $e^{a_{4,0}}$ in each direction, a shorter and more strongly warped hidden direction and a smaller extra-time coordinate volume: the 3-momenta redshift while the hidden direction and the extra times shrink.

**Computed.** Each solver solves the partner independently (60 partners). The worst level difference is 1.643e-13 and the worst relative difference of $E_{KS}$ and of the profiles 8.193e-13 (records `rescaling_identity_between_slices` and `rescaling_identity_energy_profiles`). For $N = 592$, $\hat\lambda = \lambda_1$ (`Revision/kohn_sham/results/rescaling/rescaling.csv`):

| a4,0 | partner Delta k | partner v_t | partner H | partner L | max delta eps | relative delta E | partner E_KS |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.5 | 0.1516327 | 0.6065307 | 1.18136 | 2.539445 | 1.008e-13 | 1.307e-15 | 217.3785 |
| 1 | 0.09196986 | 0.3678794 | 1.395612 | 2.149594 | 8.704e-14 | 3.451e-14 | 131.7652 |
| 1.5 | 0.05578254 | 0.2231302 | 1.648721 | 1.819592 | 9.859e-14 | 3.952e-14 | 79.82634 |
| 2 | 0.03383382 | 0.1353353 | 1.947734 | 1.540251 | 9.148e-14 | 2.448e-13 | 48.35502 |

| Wolfram and sympy records | Rust solver records | reference and cross-check records |
| --- | --- | --- |
| `rescaling_identity` | `free_rescaling_relation_and_band_monotone`, `rescaling_identity_between_slices`, `rescaling_identity_energy_profiles` | `rescaling_identity_reference`, `rescaling_partners` |

## 11. The recorded states are not admissible sources of the $a_4$ and $b_4$ equations

`Revision/SPEC.md` section 7 names the Kohn-Sham energy-momentum tensor as the source of the field equations for $a_4$ and $b_4$. The Einstein-Lovelock equations of the corrected metric (`Revision/field_equations_a4`, key generalSource of `a4-equations.json`) require of any source: (C1) every component independent of $x_0$ (the left-hand sides contain no $x_0$ for every $a_4$, $b_4$); (C2) $p_0 = p_t$ (the hidden and the extra-time components of every left-hand side are equal); (C3) no off-diagonal component, $T^{x_4}{}_{x_0} = 0$; (C4) on the history $a_4 = Hx_4$, $b_4 = e^{(4/3)Hx_4}$ with the author's weights and $\Lambda = -10$, the source $\kappa T - \Lambda$ that `a4-equations.json` records for this history (key exponentialHistory, author's weights), a function of $k = e^{(2/3)Hx_4}$ with $p_0 = p_t$. The record `Revision/field_equations_a4/reports/ks-source-conditions.json` (5 of 5 PASS) finds:

1. Every one of the 70 nonzero ground-state profiles depends on $x_0$: $(\max\rho - \min\rho)/\max|T| \geq 0.456213$ (record `ks_profiles_depend_on_x0`); C1 fails for every $a_4(x_4)$ and $b_4(x_4)$.
2. C2 holds to rounding for exactly the 10 nonzero states with $\lambda = 0$ (their fold-band orbitals have no hidden kinetic pressure and $e_{\mathrm{int}} = 0$) and fails for every one of the 60 states with $\lambda \neq 0$ ($\max_y|p_0 - p_t|/\max|T| \geq 0.080929$; record `ks_hidden_pressure_condition`): the interaction bends the orbitals.
3. C3 holds: every Kohn-Sham eigen-orbital has $T^{x_4}{}_y = 0$ (record `ks_offdiagonal_condition`).
4. The history needs the source of C4, whose energy density changes sign along it ($\kappa\rho = 3.57407$ at $a_{4,0} = 0$ and $-7.63383$ at $a_{4,0} = 2$; its ratios do not depend on the unknown $\kappa$); the Kohn-Sham sources, averaged over $x_0$ per proper volume, have ratios $(p_3/\rho, p_0/\rho, p_t/\rho)$ that differ from the needed ones by at least 1.3733 at every recorded state with a nonzero energy density (the free gas: $p_3/\rho = 1/3$, $p_0 = p_t = 0$): the history is a PRESCRIBED background (record `ks_history_is_a_prescribed_background`).
5. Five states have an identically vanishing tensor (the free $N = 8$ zero modes), a zero source, which is not admissible either: no exponential history is a vacuum solution for the author's weights (record `ks_zero_source_states_listed`).

The full analysis `Revision/field_equations_a4/ks_source/reports/ks-source-a4.json` (19 of 19 PASS) refines this exactly: the recorded states SATISFY the $x_0$ conservation identity $p_{0,y} + 3H(p_0 - p_t) = 0$ (largest residual 1.21233e-05 of the largest term on the output grid), so they fail the field equations because their components depend on $x_0$ ($\mu_1$ of the energy density between 0.147738 and 0.738255 in the L1 measure) and, for $\lambda \neq 0$, because $p_0 \neq p_t$ even after averaging over $x_0$ (relative violation $\geq 0.00613418$), not because conservation fails. The free gas is an exact fold-band gas: averaged over $x_0$ per proper volume it is $\bar\rho = Cb_4^{-2}$ with $p_3 = \rho/3$ and $p_0 = p_t = 0$, a source that conserves energy for every $a_4$ and $b_4$. With the author's weights the record's history needs $\kappa\rho = 3.57407$ at $a_4 = 0$ and $-7.63383$ at $a_4 = 2$, while the averaged free gas $N = 2352$ has $\bar\rho = 0.216249$ and $0.00104404$ there: $\kappa$ would have to run from 16.5276 to $-7311.81$, so no constant $\kappa$ makes the gas the source. In a stated approximation (the $x_0$-averaged equations with the averaged free gas as the source, started on the record's history) the solution does not follow the history: with the author's weights the second-order system becomes singular at $x_4 = 0.428813$ ($a_4 = 0.361572$, $b_4 = 0.862627$, $a_4'/H = 0.978369$, $u/H = -2.60176$, against 1 and $\frac43$ on the history); over 38 cases with three further theories the outcomes are $a_4$ turning 24 times, regular 6 times, runaway 4 times and singular 4 times. These are statements of that approximation, not of the field equations.

Consequence: the Kohn-Sham gas of this record is a test field on the prescribed background $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$ without back-reaction; energies, pressures and equations of state along the history are not consequences of the coupled field equations.

| report | records |
| --- | --- |
| `Revision/field_equations_a4/reports/ks-source-conditions.json` | `ks_profiles_depend_on_x0`, `ks_hidden_pressure_condition`, `ks_offdiagonal_condition`, `ks_history_is_a_prescribed_background`, `ks_zero_source_states_listed` |
| `Revision/field_equations_a4/ks_source/reports/ks-source-a4.json` | `A1_hidden_equals_extra_times_and_no_offdiagonal`, `A2_constraint_first_order_second_order_system`, `A3_constraint_propagation`, `A4_x0_conservation_in_y`, `A5_free_fold_band_gas_conserves_energy`, `A6_history_source_reproduced`, `B0_source_condition_report_verified`, `B1_integrals_reproduced`, `B2_x0_conservation_on_every_profile`, `B3_hidden_direction_mismatch`, `C1_averaged_hidden_pressure_condition`, `C2_energy_relation_along_the_dense_history`, `C3_record_history_not_sourced_by_the_gas`, `C4_source_signs`, `D0_free_gas_average_exact`, `D1_two_step_sizes_agree`, `D2_author_weights_from_the_record_history`, `D3_constraint_kept_along_the_solutions`, `D4_outcomes` |
| Kohn-Sham theory (the record and the label of the history) | `adiabatic_offdiagonal_identity`, `ks_theory_json_written`, `ks_theory_json_basis`, `ks_theory_json_slope`, `ks_theory_json_history_label` |

## 12. The Kohn-Sham-level pairing T3

The block map of the chirality $\Gamma$, $(\chi, j) \to (\sigma_2\chi, -j)$, with the two fold conditions exchanged and the tip angle $\theta \to \pi - \theta$, maps every self-consistent instantaneous Kohn-Sham state with $(m, \lambda, \theta)$ onto one with $(-m, +\lambda, \pi - \theta)$, with equal levels, occupations, Kohn-Sham energies and energy-momentum profiles and $S \to -S$ (both fold conditions filled, ASSUMED; mean-field level); $a_4$ and $b_4$ enter $h_j$ only through the constants $f$ and $\kappa$ of the slice, so it holds slice by slice. The theorem, its hypotheses and its proof are in `Revision/docs/PAIR_CREATION_PROOFS.md` section 8, verified by `Revision/pairing/kohn_sham/reports/wolfram-t3.json` (9 of 9 PASS) and `Revision/pairing/kohn_sham/reports/python-t3.json` (12 of 12 PASS); its completion record (`Revision/pairing/kohn_sham/t3-completion.json`) by `Revision/pairing/kohn_sham/reports/wolfram-t3-completion.json` (3 of 3 PASS) and `Revision/pairing/kohn_sham/reports/python-t3-completion.json` (7 of 7 PASS). The Rust solver contains a numerical self-test, labelled in its report as NOT a proof of T3: $(m, \lambda, \theta = 0)$ and $(-m, \lambda, \theta = \pi)$, solved independently, agree with opposite $S$ (worst 3.62e-13, tolerance 1e-9; record `t3_block_map_solver_selftest`). T3 does not establish a creation process, a rate or an amplitude.

## 13. Verification records

### 13.1 Reports and their counts

Every check has a name, a verdict and a detail. Counts at the time of writing (the publication test re-reads them):

| report | checks | PASS | FAIL |
| --- | --- | --- | --- |
| `Revision/kohn_sham/reports/ks-theory-wolfram.json` | 51 | 51 | 0 |
| `Revision/kohn_sham/reports/ks-theory-python.json` | 61 | 61 | 0 |
| `Revision/kohn_sham/reports/ks-rust-solver.json` | 45 | 45 | 0 |
| `Revision/kohn_sham/reports/ks-rust-determinism.json` | 14 | 14 | 0 |
| `Revision/kohn_sham/reports/ks-rust-mermin-roots.json` | 5 | 5 | 0 |
| `Revision/kohn_sham/reports/ks-reference.json` | 39 | 39 | 0 |
| `Revision/kohn_sham/reports/ks-crosscheck.json` | 31 | 31 | 0 |
| `Revision/field_equations_a4/reports/ks-source-conditions.json` | 5 | 5 | 0 |
| `Revision/field_equations_a4/ks_source/reports/ks-source-a4.json` | 19 | 19 | 0 |
| `Revision/field_equations_a4/reports/wolfram-a4-report.json` | 57 | 57 | 0 |
| `Revision/field_equations_a4/reports/python-a4-report.json` | 69 | 69 | 0 |
| `Revision/pairing/kohn_sham/reports/wolfram-t3.json` | 9 | 9 | 0 |
| `Revision/pairing/kohn_sham/reports/python-t3.json` | 12 | 12 | 0 |
| `Revision/kohn_sham/tip_convergence/tip-convergence.json` | 7 | 7 | 0 |

### 13.2 The independent reference and the full cross-check

The reference shares no code with the Rust solver: different discretisation (staggered finite differences with Richardson extrapolation instead of RK4 shooting), its own SCF and continuation fallback, its own parameter derivation (it re-derives the particle numbers and couplings from the stated rules) and its own uncertainty, validated on a fourth grid (record `richardson_uncertainty_validated`). The checker `Revision/kohn_sham/checker/crosscheck_ks.py` compares the two on the FULL canonical matrix: 75 ground states, 135 thermal states, 60 exact-Fock-variant states, 60 rescaling partners, 75 particle-hole lists and the 5 slices of the crossing demonstration, 217571 comparisons in all, under a tolerance rule fixed before the comparison,

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

The Rust determinism report (14 of 14 PASS): a repeat of the canonical matrix is byte-identical in all 244 result files and in its check report; a run with refined tolerances (900 to 1800 RK4 steps, root tolerance 1e-14, SCF tolerance 1e-14 with at most 1000 iterations) agrees with the canonical run to 1.728e-11 in $E_{KS}$ (relative), 5.688e-10 in 50420 levels, 1.950e-10 in the profiles, 4.513e-08 in $Q_{\max}$ and $dE/da_4$, 1.874e-10 in the thermodynamics and 3.853e-09 in $C_V$. The refined run has the SCF tolerance 1e-14, three orders below the canonical one, so that the canonical-refined differences contain the canonical SCF stopping error (with an SCF tolerance only ten times smaller both runs could stop at the same iteration and carry the same stopping error; `claude_failures.md` H15).

| item | records of `Revision/kohn_sham/reports/ks-rust-determinism.json` |
| --- | --- |
| the repeat | `repeat_byte_identical`, `repeat_report_byte_identical`, `outputs_lf_only` |
| the refined run | `refined_same_inputs`, `refined_free_spectra_convergence_order`, `refined_ground_energies`, `refined_ground_homo_lumo_gap`, `refined_eigenvalues`, `refined_delta_scf`, `refined_profiles`, `refined_adiabatic_derivatives`, `refined_thermodynamics`, `refined_mermin_root_path`, `refined_heat_capacity` |

### 13.4 Re-verification for this document

For this document (2026-10-17, the corrected metric) the committed Rust binary was run on the canonical matrix again into a scratch work folder, in the three parts and the assembly of the gate (`revision_ks_solver all --cache <scratch> --part i/3 --inner-threads 2`, then `--out <scratch>/results --report <scratch>/report.json`; 76.7 s, 70.4 s, 85.7 s and 5.7 s): all 244 result files and the check report were byte-identical to the committed `Revision/kohn_sham/results` and `Revision/kohn_sham/reports/ks-rust-solver.json` (45 of 45 checks PASS). The whole Kohn-Sham record (the repeat, the refined run, the reference, its repeat, the cross-check, the tip-cutoff study, the dense history and the source analysis) was regenerated the same day in 57 steps, each under the time limit of 423 s for one calculation, every step with exit code 0 (`claude_failures.md` H15 and H16). The other reports cited are the files of the working tree; their counts are re-read by the publication test.

## 14. Reproduction

From the repository root, in this order (the Kohn-Sham theory record reads the gammas of `Revision/algebra`; the Rust solver reads `ks-theory.json`; the Mermin-root tool runs after the canonical matrix; the reference runs in six parts per stage with a job cache, each part within the limit of 423 s for one run, and a final run writes its outputs; the cross-checker runs after the reference and the refinement measurement, with its own repeat of the reference, also in parts; the source-conditions checker reads the Kohn-Sham results and the Kohn-Sham theory checker reads its record; the Kohn-Sham source analysis reads the dense free-gas history of the dark sector, `Revision/dark_sector/dirac16complex/compute/run_ks_history.py`; `<scratch>` is any empty directory outside the repository; the backslash is the line continuation of a POSIX shell; the gate scripts `Revision/verify_revision.sh` and `Revision/verify_revision.ps1` run the same steps in parts):

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
    --stage 1 --part 1/6 --jobs 20   # and so on up to --part 6/6, then --stage 2
python Revision/kohn_sham/reference/run_reference.py --cache <scratch>/cache --jobs 20
python Revision/kohn_sham/checker/measure_rust_refinement.py \
    --work <scratch>/rust-single --jobs 22
python Revision/kohn_sham/reference/run_reference.py --cache <scratch>/repeat-cache \
    --stage 1 --part 1/6 --jobs 20   # and so on, both stages
python Revision/kohn_sham/checker/crosscheck_ks.py --work <scratch>/cc --jobs 22 \
    --repeat-cache <scratch>/repeat-cache
python Revision/kohn_sham/tip_convergence/tip_convergence.py \
    --work <scratch>/tip --jobs 22 --stage scan --part 1/6   # parts, recal, final
python Revision/field_equations_a4/python/check_ks_source_conditions.py
python Revision/kohn_sham/theory/check_ks_theory.py
python Revision/dark_sector/dirac16complex/compute/run_ks_history.py \
    --solver Revision/kohn_sham/solver/target/release/revision_ks_solver --part 1/3
python Revision/field_equations_a4/ks_source/ks_source_a4.py
python -m unittest Revision/field_equations_a4/ks_source/test_ks_source_a4.py -v
wolframscript -file Revision/pairing/kohn_sham/wolfram/verify_t3.wls
python Revision/pairing/kohn_sham/python/check_t3.py
python scripts/build_provenance_pdf.py Revision/docs/KOHN_SHAM_DEFLATING_FIELD.md \
    --developer-layout --specifications Revision/pdf-specifications.json
python -m unittest Revision/tests/test_kohn_sham_deflating_field_publication.py -v
```

Expected output: every verifier ends with all of its checks passing and writes the report of section 13.1 with the counts given there (the Wolfram Kohn-Sham verifier prints 51/51 checks passed; the Rust solver prints SUCCESS after 45 PASS lines; the cross-checker writes 31 of 31 PASS; the tip-cutoff study prints 7 PASS lines and SUCCESS); every run is deterministic, and a second run gives byte-identical outputs. Run times recorded in the READMEs of the folders (longer when the machine is shared): the Wolfram Kohn-Sham verifier about 40 to 85 s and the sympy checker about 75 to 165 s (`Revision/kohn_sham/theory/WOLFRAMSCRIPT_PROVENANCE.md`); on 2026-10-16/17 with 22 threads the Rust canonical matrix in two parts of 134.6 s and 130.5 s with an assembly of 5.4 s, the repeat in three parts of 76.7 s, 70.4 s and 85.7 s, the refined-tolerance run in four parts of 176.5 s, 186.1 s, 183.0 s and 163.8 s (`Revision/kohn_sham/solver/README.md`); the reference in two stages of six parts, stage 1 193.0, 175.4, 214.0, 179.8, 100.7 and 191.2 s, stage 2 136.8, 143.7, 133.7, 133.7, 134.2 and 139.8 s (`Revision/kohn_sham/reference/README.md`); the refinement measurement 108.8 s and the cross-checker itself 87.6 s (`Revision/kohn_sham/checker/README.md`); the tip-cutoff study 966 s in ten parts (`Revision/kohn_sham/tip_convergence/README.md`); the Kohn-Sham source analysis about 4.4 s and its unit tests about 20 s (`Revision/field_equations_a4/ks_source/README.md`); the $a_4$ verifiers 20 s (Wolfram) and 8 s (sympy) (`Revision/field_equations_a4/README.md`); the T3 verifiers 5.8 s and 1.3 s (`Revision/pairing/kohn_sham/wolfram/WOLFRAMSCRIPT_PROVENANCE.md`).

The PDF build runs the Markdown-to-LaTeX builder twice (with different hash seeds), runs pdflatex three times into each of two fresh directories, requires warning-free logs and byte-identical PDFs, and checks the PDF against its entry `kohn-sham-deflating-field` in `Revision/pdf-specifications.json` (the Revision registry; the registry of the earlier stages is not touched).

## 15. What is proved, computed, assumed and not established

### 15.1 Proved (exact, two independent verifiers)

1. The block reduction (section 3): for every history $a_4(x_4)$, $b_4(x_4)$ the good-sector equation reduces exactly to eight $2 \times 2$ blocks $h_j$ in the hidden coordinate; the spin-connection terms $\tfrac32(H/f)\gamma^0$ and $(b_4'/b_4 - \tfrac12a_4')\gamma^4$ are removed by the half-density factor $e^{-(3/2)Hy}e^{a_4/2}b_4^{-1}$; the hidden direction enters through $1/f$ and the 3-momenta through the constant $\kappa = e^{-a_4}$.
2. The exchange functional (section 4): the exact local exchange of the uniform 8-fold good-sector gas at every temperature, $M_{\mathrm{eff}} = m + \frac{15}{16}\lambda S$, $v_v = -\lambda n/16$; the exact Fock exchange of the closed-shell slab differs by $+\lambda Q^2/32$; a state depends on the coupling and the cell volume only through their ratio.
3. The boundary-value structure (section 5): self-adjointness with current-killing ends, the fold conditions, the exact $k = 0$ spectra, the fold band $\varepsilon = \kappa k$ and its slope.
4. The rescaling identity (section 10), the energy-momentum tensor of the Kohn-Sham states with its trace and conservation identities and the energy change along the history (section 9), and the adiabaticity identity of the measure (section 7).
5. T3 (section 12; proved in `Revision/docs/PAIR_CREATION_PROOFS.md`), under its stated hypotheses.

### 15.2 Computed (numerical, two independent solvers, cross-checked)

1. The instantaneous ground states, first excited states (gap, $\Delta$-SCF, particle-hole lists), Mermin states, energy-momentum profiles, rescaling partners and exact-Fock variants of the canonical matrix (sections 6 to 10), with the Rust solver and the reference agreeing on the full matrix within the stated uncertainty (31 of 31 checks, 217571 comparisons).
2. The adiabaticity measure ($Q_{\max} \leq 0.1982205$) and the absence of Fermi-level crossings in the canonical matrix; the crossing demonstration at $N = 2360$ (section 7).
3. That the recorded states are not admissible sources of the $a_4$ and $b_4$ equations (section 11).
4. The dependence on the tip cutoff $L$ from 3 to 6 of 29 recorded states, the 27 ground states with $N \in \{8, 592, 2352\}$, $\lambda \in \{0, \pm\lambda_1\}$, $a_{4,0} \in \{0, 1, 2\}$ and two Mermin states of $N = 592$ ($\lambda = 0$, $a_{4,0} = 2$, $T = 0.05$; $\lambda = \lambda_1$, $a_{4,0} = 1$, $T = 0.02$) (section 5; `Revision/kohn_sham/tip_convergence/`, 7 of 7 checks PASS; the Rust solver at every $L$, the reference at $L = 3$ and $4$).

### 15.3 Assumed or chosen

1. Both fold conditions filled at the fold $z = \pi/2$, where the two halves of a cell meet (ASSUMED); the metric is degenerate there and no junction condition is derived.
2. The regular tip at the cutoff $L = 3$ with $\theta = 0$ (chosen). Its effect is measured (section 5): the free fold-band gases do not depend on $L$, except their values at the fold (the normalisation of the fold-band orbital) and except $N = 2352$ at $a_{4,0} = 0$; the interaction energies do: the recorded $N = 8$ interaction energy is 0.977, 0.674 and 0.215 of its large-$L$ value at $a_{4,0} = 0, 1, 2$. The couplings (calibrated at $L = 3$) and $N = 2352$ (bulk edge at $L = 3$) are themselves $L = 3$ choices.
3. The filling convention (particles on the positive branch and on the $k = 0$ zero modes; the sea not populated thermally), whose justification is OPEN; the sea-hole diagnostic shows where it fails (27 of 135 thermal states).
4. The history $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$, $A = 1$, PRESCRIBED, not solved for.
5. The parameters of section 5 ($N$, $\hat\lambda$, $L$, $\Delta k$, $v_t$, $T$).

### 15.4 Not established

1. The time-dependent (non-adiabatic) Kohn-Sham problem (TDDFT) is OPEN: only instantaneous states are computed; the measure $Q_{\max}$ is a consistency indicator, not a solution of the evolution.
2. Correlation: the functional is Hartree plus exchange only; no correlation functional is derived or used.
3. Back-reaction: the Kohn-Sham states are a test field on a prescribed background; no recorded state is an admissible source of the field equations for $a_4$ and $b_4$, and no history $a_4(x_4)$, $b_4(x_4)$ is derived from the Kohn-Sham source.
4. Equations of state and the dark-sector hypothesis are not part of this document (`Revision/dark_sector/dirac16complex`).
5. No creation process, rate or amplitude for universes follows from the Kohn-Sham model or from T3.
6. A thermal treatment of the Dirac sea (pairs) where the particle-only ensemble fails; states beyond the computed range $a_{4,0} \in [0, 2]$; the continuum limit $\Delta k \to 0$; Kohn-Sham states with extra-time momenta. The limit $L \to \infty$ is established (numerically, with uncertainties) only for the states and quantities marked converged in `Revision/kohn_sham/tip_convergence/README.md`; it is NOT established for $N = 2352$ at $a_{4,0} = 0$ (the $k = 0$ bulk levels approach $m$ algebraically and the occupied set changes; the iteration of its interacting partners fails), nor for the Mermin state N592_lam0_a20_T50 (successive changes of about $10^{-8}$ relative that do not meet the geometric-tail rule). It is not computed at $L \neq 3$ for $\lambda_2$, the slices 0.5 and 1.5, $T = 0.01$ and the other thermal states, the excited states and the adiabaticity measure, nor at $L > 6$. The record's calibration rule drives $\lambda_1$ to zero as $L$ grows.
