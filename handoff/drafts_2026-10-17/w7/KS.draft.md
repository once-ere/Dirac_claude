# Kohn-Sham model of dirac16complex in the author's primordial field with the deflating extra times

## The block reduction, the instantaneous ground and first excited states along the prescribed history $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$, Mermin thermodynamics, adiabaticity, the energy-momentum tensor, the rescaling partners and the source conditions, with the verification records and an exact statement of what is computed and what is not

## Abstract

This document records the Kohn-Sham (density-functional) model of the fermion field dirac16complex in the author's primordial gravitational field, deliverable 4 of `Revision/SPEC.md` section 10, as computed by the code in `Revision/kohn_sham/`, in the corrected metric of 2026-10-16 (version 2): $g = \mathrm{diag}\big(e^{-2a_4}b_4\cot^2 z,\ e^{2a_4}\,(\times3),\ -1,\ -e^{-2a_4}b_4(\sin^2 z)^{1/6}\,(\times3)\big)$, $z = 6Hx_0$ real, with two functions $a_4(x_4)$ and $b_4(x_4) > 0$ ($b_4$ is never 1). Exact (two independent verifiers, WolframScript and sympy): in the good sector (no extra-time momentum) the ansatz $\Psi = e^{ik\cdot x}e^{-(3/2)Hy}e^{a_4/2}b_4^{-1}\chi(y,x_4)$ removes the spin-connection terms $\tfrac32(H/f)\gamma^0$ and $(b_4'/b_4 - \tfrac12a_4')\gamma^4$ and reduces the 16-component equation, for every history $a_4(x_4)$, $b_4(x_4)$, to eight $2 \times 2$ blocks $h_j = j[-(i/f)\sigma_1\,d/dy + M_{\mathrm{eff}}\sigma_2 + \kappa k\sigma_3] + v_v$ in the hidden coordinate $y = \ln|\sin z|/(6H)$, with the hidden scale $f = e^{-a_4}b_4^{1/2}$ (the hidden direction shrinks together with the extra times) and the constant momentum weight $\kappa = e^{-a_4}$; the deflation enters the instantaneous problem through $f$, through the redshift $\kappa k$ of the 3-momenta and through the proper cell volume, which grows like $e^{-a_4}b_4^2$, on the history like $e^{(5/3)a_4}$; the exact local exchange of the uniform good-sector gas gives $M_{\mathrm{eff}} = m + \frac{15}{16}\lambda S$ and $v_v = -\lambda n/16$. Computed (a Rust solver, an independent Python reference with a different discretisation, and a cross-check of the full canonical matrix, @@CC_ABSTRACT@@): the instantaneous ground and first excited states of 75 parameter sets ($N = 8, 592, 2352$; five couplings $\hat\lambda$, held fixed while the cell grows, so that the effective coupling falls like $e^{-(5/3)a_{4,0}}$; five slices $a_{4,0}$ of the prescribed history $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$, $A = 1$), 135 Mermin states at three temperatures, the adiabaticity measure ($Q_{\max} \leq @@QMAX@@$ over the matrix), the Fermi-level crossings (none in the canonical matrix; a demonstration at $N = 2360$), the energy-momentum tensor profiles, the exact rescaling partners and the exact-exchange variant. The free states of the matrix are exact fold-band gases: their occupied levels are $\varepsilon = \kappa|k|$ with the orbital $(e^{fMy}, 0)$, so their energy redshifts exactly like $e^{-a_4}$, with $\int p_3 = E_{KS}/3$ and $\int p_0 = \int p_t = 0$. ASSUMED or chosen: both fold conditions filled at the fold $z = \pi/2$ where the two halves of a cell meet, the regular tip at $y = -3$, the filling convention. @@TIP_ABSTRACT@@ Not admissible as sources: no recorded Kohn-Sham state satisfies the source conditions of the $a_4$ and $b_4$ equations, so the history is a prescribed background without back-reaction. Not done: the time-dependent (non-adiabatic) Kohn-Sham problem, correlation beyond exchange, back-reaction.

## 1. The task and the answer

The author asked (2026-10-01, quoted from `Revision/README.md`): “plan and employ a DFT-motivated approximation similar to the one that you already created [...], with a Kohn-Sham fermion-gas thermodynamic effective potential, that employs the DFT ground and first-excited-state computation”. `Revision/SPEC.md` section 7 makes this precise: a Kohn-Sham fermion-gas model of dirac16complex in the good sector with the contact interaction $U = \frac{\lambda}{2}S^2$, the Hartree mean field plus the exact local exchange of the uniform gas, Mermin's finite-temperature functional, the reduction to $2 \times 2$ blocks in the hidden coordinate, the boundary conditions, the ground and first excited states, the thermodynamics, and, because $a_4$ and $b_4$ depend on $x_4$, the INSTANTANEOUS (adiabatic) Kohn-Sham states along the history with the extra times deflating, with an adiabaticity measure.

The answer of this record:

1. Exact (section 3, section 4): the block reduction, the exchange functional, the boundary conditions, the rescaling identity, the energy-momentum tensor and its conservation laws, the adiabaticity measure, all for the corrected metric. Every formula is in `Revision/kohn_sham/ks-theory.json` and verified twice, in `Revision/kohn_sham/reports/ks-theory-wolfram.json` (@@PW@@ of @@PW@@ PASS) and independently in `Revision/kohn_sham/reports/ks-theory-python.json` (@@PP@@ of @@PP@@ PASS).
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
@@T_RECORDS_2@@

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
@@T_RECORDS_3@@

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
@@T_RECORDS_4@@

## 5. Boundary conditions, filling convention, numerics and parameters

**Fold (both fold conditions filled, ASSUMED).** The fold $\cos z = 0$ at $y = 0$ joins the two halves of a cell; the reduced equation is the same on both halves ($dy = \cot z\,dx_0$, $e^{x_0}dx_0 = f\,dy$, $\gamma^\mu\Omega_\mu$ free of $x_0$), so a spinor continuous across the fold has the same $\chi(y)$ on both halves; the boundary form of the doubled cell at the fold is $2(-ij/f)\phi^\dagger\sigma_1\chi(0)$, and self-adjointness needs $(1 - Q(\theta))\chi(0) = 0$. The record fills both fold conditions, the even $\theta = 0$ ($\chi_2(0) = 0$, $b(0) = 0$) and the odd $\theta = \pi$ ($\chi_1(0) = 0$, $a(0) = 0$), each normalised on one half; $N$ is the particle number of the whole cell, each half holds $N/2$, and $w = 1/2$ per half. That both are filled is ASSUMED (the record's convention); there is no mirror copy.

**Tip (chosen).** At $y = -L$: $(1 - Q(\theta))\chi(-L) = 0$, $Q(\theta) = \cos\theta\,\sigma_3 + \sin\theta\,\sigma_2$, canonical $\theta = 0$, cutoff $L = 3$. With $\kappa$ independent of $y$ nothing suppresses an orbital toward the tip: for constant $M$ and $v$ the branches are $e^{\pm f\lambda y}$, $\lambda = \sqrt{M^2 + \kappa^2k^2 - (\varepsilon - v)^2}$. @@TIP_5@@

**Exact $k = 0$ spectra.** For constant $M > 0$, $v = 0$, $\theta = 0$: the even fold condition has $\varepsilon = 0$ with the fold zero mode $\chi = (e^{fMy}, 0)$, and $\varepsilon = \pm\sqrt{M^2 + (n\pi/(fL))^2}$; the odd fold condition has $\varepsilon = \pm\sqrt{M^2 + p^2}$ with $\tan(pfL) = -p/M$. The even $j = +1$ fold band is $\varepsilon = \kappa k$ EXACTLY for every $k$, with the orbital $(e^{fMy}, 0)$ (record `free_rescaling_relation_and_band_monotone`); its slope is $c = e^{-a_{4,0}}$ for every $M$, $L$ and $f$ (record `brane_band_slope`; the record keeps the name of the earlier construction).

**Filling (CONVENTION, justification OPEN).** Particles occupy the positive branch (the levels with $\varepsilon > 0$ of the $\lambda = 0$ problem) and the $k = 0$ fold zero modes, each followed continuously in $\lambda$; the negative branch is the normal-ordered sea and contributes nothing to $N$, $n$, $S$ or the energy-momentum tensor. The excluded thermal sea holes are reported as a diagnostic (section 8).

**Numerics.** The Rust solver (`Revision/kohn_sham/solver`, own crate, no external crates) solves each block by shooting with RK4 on 900 steps, Pruefer counting and a root tolerance of 1e-13, Anderson-mixed SCF to 1e-11; when the direct iteration diverges it falls back to a continuation in the coupling ($\hat\lambda \times \frac14, \frac12, \frac34, 1$ with half the mixing). The independent Python reference (`Revision/kohn_sham/reference`) uses a staggered finite-difference discretisation on three grids (300, 600, 1200) with Richardson extrapolation and a stated uncertainty, validated on a fourth grid, with its own continuation fallback; its convergence order is two (record `free_convergence_order_two`).

**Parameters** (`Revision/kohn_sham/results/parameters.json`): $H = m = 1$, $L = 3$, $\Delta k = 0.25$, $v_t = 1$, $\mathrm{Vol}_7(0) = @@VOL7@@$ and $\mathrm{Vol}_7(a_{4,0}) = \mathrm{Vol}_7(0)\,e^{(5/3)a_{4,0}}$, tip $\theta = 0$, history $A = 1$, $\beta = 4/3$, slices $a_{4,0} \in \{0, 0.5, 1, 1.5, 2\}$, temperatures $T \in \{0.01, 0.02, 0.05\}$. Particle numbers: $N = 8$ (the $k = 0$ fold zero modes of both block types), $N = 2352$ (the largest closed shell of the free $a_{4,0} = 0$ aufbau whose last level lies below the bulk edge @@BULK_EDGE@@, the lowest level not on the even $j = +1$ fold band) and $N = 592$ (the closed shell nearest $2352/4$). Couplings: $\lambda_1$ and $\lambda_2$ (values of $\hat\lambda$) keep the first-order mean-field potential below 0.1 and 0.3 (units of $m$) along the whole history; the strength is the largest first-order potential per unit $\hat\lambda$ over the five slices, with the densities per $\mathrm{Vol}_7(a_{4,0})$:

@@T_COUPLINGS@@

The canonical matrix holds 75 ground states ($3$ values of $N$, the five couplings $0, \pm\lambda_1, \pm\lambda_2$, five slices), each with its first excited state, its $a_4$ neighbours, its rescaling partner and, for $\lambda \neq 0$, its exact-Fock variant, and 135 Mermin states ($\hat\lambda \in \{0, \pm\lambda_1\}$, three temperatures).

| item | records |
| --- | --- |
@@T_RECORDS_5@@

## 6. Instantaneous ground and first excited states along the prescribed history

The history is $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$ with $A = 1$ (the exponentially deflating member: the scale factor of the extra times is $b_4(0)^{1/2}e^{-Hx_4/3}(\sin^2 z)^{1/12}$), PRESCRIBED, not solved for (section 11). At every slice $a_{4,0}$ the ground state is the self-consistent aufbau state of the instantaneous problem; the first excited state is computed three ways: the Kohn-Sham gap $\varepsilon_{\mathrm{LUMO}} - \varepsilon_{\mathrm{HOMO}}$; the ensemble $\Delta$-SCF energy (one particle moved from the highest occupied degenerate group to the lowest empty group, spread uniformly over each group, self-consistent); and the list of the 24 lowest particle-hole excitations (`Revision/kohn_sham/results/excited/particle-hole/`). Every ground state of the matrix is closed-shell.

Ground and first excited states for $N = 592$ (`Revision/kohn_sham/results/ground/summary.csv` and `Revision/kohn_sham/results/excited/summary.csv`):

@@T_GROUND@@

The free Kohn-Sham gap along the history ($\lambda = 0$, `ground/summary.csv`):

@@T_GAPS@@

Reading (labelled interpretation of these numbers): the free ground states occupy the fold band $\varepsilon = \kappa|k|$ and the $k = 0$ zero modes, so as the extra times deflate the 3-momenta redshift as $ke^{-a_{4,0}}$ and the occupied free levels redshift with them: the free energies of $N = 592$ and $2352$ fall exactly like $e^{-a_{4,0}}$, the Kohn-Sham gap of $N = 8$ is $\kappa\Delta k = 0.25\,e^{-a_{4,0}}$ and that of $N = 592$ falls like $e^{-a_{4,0}}$; for $N = 2352$ the lowest empty level at $a_{4,0} = 0$ is the bulk edge (by the choice of $N$), and from $a_{4,0} = 0.5$ on, where the $k = 0$ bulk levels have risen above it, the next fold-band shell, so its gap falls like $e^{-a_{4,0}}$ from there; with interaction the energy changes also with the effective coupling $\hat\lambda e^{-(5/3)a_{4,0}}$. With $\lambda = 0$ the $\Delta$-SCF energy equals the Kohn-Sham gap (worst difference @@DSCF@@ over 15 cases, record `excited_delta_scf_free_equals_gap`); with interaction the two differ slightly, because the $\Delta$-SCF state relaxes the mean field self-consistently.

| item | Rust solver records | reference records | cross-check records |
| --- | --- | --- | --- |
@@T_RECORDS_6@@

## 7. Adiabaticity and Fermi-level crossings

Exactly (mean field), $i\partial_{x_4}\chi = h(a_4(x_4), f(x_4))\chi$ conserves $k$, the block and the fold condition; transitions occur only between levels of the same $(k, j, \text{block}, \text{fold condition})$. The measure along $a_4 = AHx_4$ is

$$
\begin{aligned}
Q_{nm} &= AH\,\frac{\lvert\langle n\rvert\partial_ah\lvert m\rangle\rvert}{(\varepsilon_n - \varepsilon_m)^2} = AH\,\frac{\lvert\langle n\vert\partial_am\rangle\rvert}{\lvert\varepsilon_n - \varepsilon_m\rvert},\\
\partial_ah_j &= -j\kappa k\sigma_3 + \big(1 - \tfrac{\beta}{2}\big)\,j\big(-\tfrac{i}{f}\sigma_1\partial_y\big) + j(\partial_aM_{\mathrm{eff}})\sigma_2 + \partial_av_v ,
\end{aligned}
$$

for $n$ occupied and $m$ empty in the same sector (the second term, one third of the kinetic term, comes from the shrinking hidden direction); the state is adiabatic if $\max Q_{nm} \ll 1$, and $Q_{nm}^2$ is the leading-order transition probability. The self-consistent derivatives come from the states at $a_{4,0} \pm \delta$, $\pm 2\delta$ ($\delta = 2\times10^{-3}$, Richardson); they contain the change of the effective coupling $\hat\lambda/\mathrm{Vol}_7(a_{4,0})$ along the history. Hellmann-Feynman, $d\varepsilon_n/da = \langle n\rvert\partial_ah\lvert n\rangle$, is checked in 75 cases (worst @@HF@@, record `adiabatic_hellmann_feynman`).

Results (`Revision/kohn_sham/results/adiabatic/adiabaticity.csv`): because the hidden direction shrinks, $Q_{\max}$ is not zero even for $N = 8$ at $\lambda = 0$ (@@N8_FREE_Q@@); over the $N = 8$ states the largest value is $Q_{\max} \leq @@N8_Q@@$ (state @@N8_Q_ID@@, pair `@@N8_Q_PAIR@@`). The largest value over the whole matrix is @@QMAX@@ (state @@QMAX_ID@@, pair `@@QMAX_PAIR@@`: two levels of the same shell, block type and fold condition). For $\lambda = 0$:

@@T_ADIABATIC@@

The last two columns are the energy change along the history, from the energy-momentum tensor ($dE/da_4 = -3P_3 + P_t + \tfrac13P_0$, $P = 2\mathrm{Vol}_7(a_{4,0})\int e^{3Hy}p\,dy$, section 9) and from finite differences at fixed occupations; for the free fold-band gases both equal $-E_{KS}$.

**Fermi-level crossings.** When levels of different $k$ cross the Fermi level between slices, the instantaneous aufbau ground state differs from the adiabatically continued state, and the solver flags it. No crossing occurs in the canonical matrix: every one of the 15 series of `Revision/kohn_sham/results/adiabatic/history.json` has an empty crossing list, and `adiabatic/fermi-level-crossings.csv` records no change of the occupied set. A demonstration at $\lambda = 0$ and $N = 2360$ (the smallest closed shell of the $a_{4,0} = 0$ aufbau that occupies a level off the even $j = +1$ fold band; `adiabatic/crossing-demo.csv`):

@@T_CROSSING@@

From $a_{4,0} = 0.5$ on, the fold-band levels redshift ($\varepsilon = e^{-a_4}k$) while the $k = 0$ bulk levels rise ($\varepsilon = \sqrt{M^2 + (n\pi/(fL))^2}$, $f = e^{-a_4/3}$): the instantaneous ground state is not the adiabatically reached state, which lies above it by the last column.

Interpretation (labelled): with $Q_{\max} \leq @@QMAX@@$ the instantaneous states are self-consistently adiabatic for the same-sector transitions at the rate $A = 1$ in the canonical matrix only in the weak sense $Q_{\max} < 1$; the largest values approach 0.2 for $N = 2352$ at $a_{4,0} = 0$. This does not solve the time-dependent problem (OPEN), and where Fermi-level crossings occur (the demonstration) the instantaneous ground state is not the state that the evolution reaches.

| Rust solver records | reference records | cross-check records |
| --- | --- | --- |
| `adiabatic_hellmann_feynman`, `adiabatic_crossing_flag_demonstration` | `adiabatic_hellmann_feynman_discrete`, `crossing_demo_reference` | `adiabatic_dE_da4`, `adiabatic_Q_max`, `crossing_demonstration` |

## 8. Mermin thermodynamics

The Mermin states at $T = 0.01, 0.02, 0.05$ solve the self-consistent problem at fixed $N$ with $\mu$ the root of $\sum g f = N$ in a well-conditioned form (thermal particles above and holes below a split of the levels, `solver/src/mermin.rs`). The checks: $\Omega$ in its two forms, $-dF/dT = S_{\mathrm{ent}}$, $C_V = T\,dS_{\mathrm{ent}}/dT = dE/dT$ at fixed $N$, and the chemical potential against 40-digit roots on the solver's own final levels (40-digit and 50-digit roots agree to @@ROOT_PREC@@, record `root_precision_self_check`). For $N = 592$, $\lambda = 0$ (`Revision/kohn_sham/results/thermo/thermodynamics.csv`):

@@T_THERMO@@

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

@@T_EMT@@

For a fold-band orbital $(e^{fMy}, 0)$ with $\varepsilon = \kappa|k|$ the hidden-direction kinetic pressure vanishes identically, so the free states have $p_0 = p_t = 0$ (the table shows rounding values) and $\int p_3 = E_{KS}/3$: a radiation-like gas of the 3-space momenta, whose energy falls like $e^{-a_4}$ ($dE/da_4 = -E_{KS}$, section 7). The profiles on 151 points $y = -3 + 0.02i$ are in `Revision/kohn_sham/results/ground/profiles/` (one file per state; densities per $\mathrm{Vol}_7(a_{4,0})$, that is the proper densities times $b_4(0)^2$). The energy density varies along the hidden direction in every state with a nonzero tensor (section 11). Equations of state seen by a 3-space observer are not part of this document; they are the work of `Revision/dark_sector/dirac16complex` (its Kohn-Sham history report `Revision/dark_sector/dirac16complex/reports/ks-history-run.json`: @@HIST_COUNT@@ PASS).

| item | Wolfram and sympy records | Rust solver records | reference and cross-check records |
| --- | --- | --- | --- |
@@T_RECORDS_9@@

## 10. The rescaling partners

**Exact identity.** With the proper hidden coordinate $Y = f_0y$, $f_0 = e^{-a_{4,0}}b_{4,0}^{1/2}$,

$$
\mathrm{KS}(a_{4,0}, b_{4,0};\,H, L, \Delta k, v_t, \lambda, N, T) = \mathrm{KS}\big(0, 1;\,H/f_0,\, f_0L,\, \Delta k\,e^{-a_{4,0}},\, v_t\,e^{-3a_{4,0}}b_{4,0}^{3/2},\, \lambda, N, T\big)
$$

for the levels, orbitals ($\chi_Y = \chi/\sqrt{f_0}$), proper densities and energy-momentum profiles; on the history ($b_{4,0} = e^{(4/3)a_{4,0}}$, $f_0 = e^{-a_{4,0}/3}$) the partner has $H e^{a_{4,0}/3}$, $Le^{-a_{4,0}/3}$, $\Delta k\,e^{-a_{4,0}}$ and $v_t\,e^{-a_{4,0}}$ at the same $\hat\lambda$. Reading (labelled): the slice $a_{4,0}$ of the deflating history is the slice 0 with a 3-torus larger by $e^{a_{4,0}}$ in each direction, a shorter and more strongly warped hidden direction and a smaller extra-time coordinate volume: the 3-momenta redshift while the hidden direction and the extra times shrink.

**Computed.** Each solver solves the partner independently (60 partners). The worst level difference is @@RESC_LEV@@ and the worst relative difference of $E_{KS}$ and of the profiles @@RESC_PROF@@ (records `rescaling_identity_between_slices` and `rescaling_identity_energy_profiles`). For $N = 592$, $\hat\lambda = \lambda_1$ (`Revision/kohn_sham/results/rescaling/rescaling.csv`):

@@T_RESCALING@@

| Wolfram and sympy records | Rust solver records | reference and cross-check records |
| --- | --- | --- |
| `rescaling_identity` | `free_rescaling_relation_and_band_monotone`, `rescaling_identity_between_slices`, `rescaling_identity_energy_profiles` | `rescaling_identity_reference`, `rescaling_partners` |

## 11. The recorded states are not admissible sources of the $a_4$ and $b_4$ equations

@@SOURCE_11@@

## 12. The Kohn-Sham-level pairing T3

The block map of the chirality $\Gamma$, $(\chi, j) \to (\sigma_2\chi, -j)$, with the two fold conditions exchanged and the tip angle $\theta \to \pi - \theta$, maps every self-consistent instantaneous Kohn-Sham state with $(m, \lambda, \theta)$ onto one with $(-m, +\lambda, \pi - \theta)$, with equal levels, occupations, Kohn-Sham energies and energy-momentum profiles and $S \to -S$ (both fold conditions filled, ASSUMED; mean-field level); $a_4$ and $b_4$ enter $h_j$ only through the constants $f$ and $\kappa$ of the slice, so it holds slice by slice. The theorem, its hypotheses and its proof are in `Revision/docs/PAIR_CREATION_PROOFS.md` section 8, verified by `Revision/pairing/kohn_sham/reports/wolfram-t3.json` (@@T3W@@ of @@T3W@@ PASS) and `Revision/pairing/kohn_sham/reports/python-t3.json` (@@T3P@@ of @@T3P@@ PASS); its completion record (`Revision/pairing/kohn_sham/t3-completion.json`) by `Revision/pairing/kohn_sham/reports/wolfram-t3-completion.json` (@@T3CW@@ of @@T3CW@@ PASS) and `Revision/pairing/kohn_sham/reports/python-t3-completion.json` (@@T3CP@@ of @@T3CP@@ PASS). The Rust solver contains a numerical self-test, labelled in its report as NOT a proof of T3: $(m, \lambda, \theta = 0)$ and $(-m, \lambda, \theta = \pi)$, solved independently, agree with opposite $S$ (worst 3.62e-13, tolerance 1e-9; record `t3_block_map_solver_selftest`). T3 does not establish a creation process, a rate or an amplitude.

## 13. Verification records

### 13.1 Reports and their counts

Every check has a name, a verdict and a detail. Counts at the time of writing (the publication test re-reads them):

@@COUNT_TABLE@@

### 13.2 The independent reference and the full cross-check

The reference shares no code with the Rust solver: different discretisation (staggered finite differences with Richardson extrapolation instead of RK4 shooting), its own SCF and continuation fallback, its own parameter derivation (it re-derives the particle numbers and couplings from the stated rules) and its own uncertainty, validated on a fourth grid (record `richardson_uncertainty_validated`). The checker `Revision/kohn_sham/checker/crosscheck_ks.py` compares the two on the FULL canonical matrix: 75 ground states, 135 thermal states, 60 exact-Fock-variant states, 60 rescaling partners, 75 particle-hole lists and the 5 slices of the crossing demonstration, @@CC_COMPARISONS@@ comparisons in all, under a tolerance rule fixed before the comparison,

$$
\lvert x_{\mathrm{Rust}} - x_{\mathrm{ref}}\rvert \leq 3\,(U_{\mathrm{ref}} + U_{\mathrm{Rust}}) + 10^{-12}\,\mathrm{scale},\qquad
U_{\mathrm{Rust}} = \tfrac{16}{15}\,\lvert\mathrm{canonical} - \mathrm{refined}\rvert ,
$$

with $U_{\mathrm{ref}}$ the reference's three-grid Richardson uncertainty and $U_{\mathrm{Rust}}$ measured for every state of the matrix by the refinement measurement, whose script and record are `Revision/kohn_sham/checker/measure_rust_refinement.py` and `Revision/kohn_sham/checker/rust-refinement.json`. All @@CC_N@@ checks of the cross-check pass:

@@CC_TABLE@@

### 13.3 Determinism and the refinement measurement

The Rust determinism report (@@DET_N@@ of @@DET_N@@ PASS): a repeat of the canonical matrix is byte-identical in all 244 result files and in its check report; a run with refined tolerances (900 to 1800 RK4 steps, root tolerance 1e-14, SCF tolerance 1e-14 with at most 1000 iterations) agrees with the canonical run to @@DET_E@@ in $E_{KS}$ (relative), @@DET_LEV@@ in @@DET_NLEV@@ levels, @@DET_PROF@@ in the profiles, @@DET_ADIA@@ in $Q_{\max}$ and $dE/da_4$, @@DET_THERMO@@ in the thermodynamics and @@DET_CV@@ in $C_V$. The refined run has the SCF tolerance 1e-14, three orders below the canonical one, so that the canonical-refined differences contain the canonical SCF stopping error (with an SCF tolerance only ten times smaller both runs could stop at the same iteration and carry the same stopping error; `claude_failures.md` H15).

| item | records of `Revision/kohn_sham/reports/ks-rust-determinism.json` |
| --- | --- |
| the repeat | `repeat_byte_identical`, `repeat_report_byte_identical`, `outputs_lf_only` |
| the refined run | `refined_same_inputs`, `refined_free_spectra_convergence_order`, `refined_ground_energies`, `refined_ground_homo_lumo_gap`, `refined_eigenvalues`, `refined_delta_scf`, `refined_profiles`, `refined_adiabatic_derivatives`, `refined_thermodynamics`, `refined_mermin_root_path`, `refined_heat_capacity` |

### 13.4 Re-verification for this document

@@REVERIFY@@

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

@@RUNTIMES_14@@

The PDF build runs the Markdown-to-LaTeX builder twice (with different hash seeds), runs pdflatex three times into each of two fresh directories, requires warning-free logs and byte-identical PDFs, and checks the PDF against its entry `kohn-sham-deflating-field` in `Revision/pdf-specifications.json` (the Revision registry; the registry of the earlier stages is not touched).

## 15. What is proved, computed, assumed and not established

### 15.1 Proved (exact, two independent verifiers)

1. The block reduction (section 3): for every history $a_4(x_4)$, $b_4(x_4)$ the good-sector equation reduces exactly to eight $2 \times 2$ blocks $h_j$ in the hidden coordinate; the spin-connection terms $\tfrac32(H/f)\gamma^0$ and $(b_4'/b_4 - \tfrac12a_4')\gamma^4$ are removed by the half-density factor $e^{-(3/2)Hy}e^{a_4/2}b_4^{-1}$; the hidden direction enters through $1/f$ and the 3-momenta through the constant $\kappa = e^{-a_4}$.
2. The exchange functional (section 4): the exact local exchange of the uniform 8-fold good-sector gas at every temperature, $M_{\mathrm{eff}} = m + \frac{15}{16}\lambda S$, $v_v = -\lambda n/16$; the exact Fock exchange of the closed-shell slab differs by $+\lambda Q^2/32$; a state depends on the coupling and the cell volume only through their ratio.
3. The boundary-value structure (section 5): self-adjointness with current-killing ends, the fold conditions, the exact $k = 0$ spectra, the fold band $\varepsilon = \kappa k$ and its slope.
4. The rescaling identity (section 10), the energy-momentum tensor of the Kohn-Sham states with its trace and conservation identities and the energy change along the history (section 9), and the adiabaticity identity of the measure (section 7).
5. T3 (section 12; proved in `Revision/docs/PAIR_CREATION_PROOFS.md`), under its stated hypotheses.

### 15.2 Computed (numerical, two independent solvers, cross-checked)

1. The instantaneous ground states, first excited states (gap, $\Delta$-SCF, particle-hole lists), Mermin states, energy-momentum profiles, rescaling partners and exact-Fock variants of the canonical matrix (sections 6 to 10), with the Rust solver and the reference agreeing on the full matrix within the stated uncertainty (@@CC_N@@ of @@CC_N@@ checks, @@CC_COMPARISONS@@ comparisons).
2. The adiabaticity measure ($Q_{\max} \leq @@QMAX@@$) and the absence of Fermi-level crossings in the canonical matrix; the crossing demonstration at $N = 2360$ (section 7).
3. That the recorded states are not admissible sources of the $a_4$ and $b_4$ equations (section 11).
@@TIP_15_2@@

### 15.3 Assumed or chosen

1. Both fold conditions filled at the fold $z = \pi/2$, where the two halves of a cell meet (ASSUMED); the metric is degenerate there and no junction condition is derived.
@@TIP_15_3@@
3. The filling convention (particles on the positive branch and on the $k = 0$ zero modes; the sea not populated thermally), whose justification is OPEN; the sea-hole diagnostic shows where it fails (27 of 135 thermal states).
4. The history $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$, $A = 1$, PRESCRIBED, not solved for.
5. The parameters of section 5 ($N$, $\hat\lambda$, $L$, $\Delta k$, $v_t$, $T$).

### 15.4 Not established

1. The time-dependent (non-adiabatic) Kohn-Sham problem (TDDFT) is OPEN: only instantaneous states are computed; the measure $Q_{\max}$ is a consistency indicator, not a solution of the evolution.
2. Correlation: the functional is Hartree plus exchange only; no correlation functional is derived or used.
3. Back-reaction: the Kohn-Sham states are a test field on a prescribed background; no recorded state is an admissible source of the field equations for $a_4$ and $b_4$, and no history $a_4(x_4)$, $b_4(x_4)$ is derived from the Kohn-Sham source.
4. Equations of state and the dark-sector hypothesis are not part of this document (`Revision/dark_sector/dirac16complex`).
5. No creation process, rate or amplitude for universes follows from the Kohn-Sham model or from T3.
6. A thermal treatment of the Dirac sea (pairs) where the particle-only ensemble fails; states beyond the computed range $a_{4,0} \in [0, 2]$; the continuum limit $\Delta k \to 0$; Kohn-Sham states with extra-time momenta. @@TIP_15_4@@
